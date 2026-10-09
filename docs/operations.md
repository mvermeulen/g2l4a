# Operations & Maintenance Manual

This manual details the system administration, runtime tuning, and telemetry metrics for the `g2l4a` bicycle tour route optimizer in production environments.

## 1. Persistent L2 Cache Management

The L2 spatial and weather caches are backed by a local SQLite database (`.g2l4a_cache.db`). Coordinates are stored with a rounded 6-decimal-place coordinate key format (providing approx. 11 cm precision) to optimize retrieval efficiency.

### Cache Schema Layout
- `routing_cache`: Caches path distance, ascent, and bicycle legality using composite keys: `(origin_id, destination_id, routing_engine_version, profile_hash)`.
- `weather_cache`: Stores average high/low temperatures by city name and date.

### Cache Maintenance and Invalidation
- **L2 Cache Pruning**: To clear stale weather forecasts or reset corrupted keys, execute the following script logic or delete the database file directly:
  ```bash
  rm .g2l4a_cache.db
  ```
- **Concurrency & Thread Safety**: SQLite connections cannot be shared across multiple concurrent execution threads. Connections must be instantiated using thread-local instances (`threading.local()`), and workers should always execute `manager.close()` during thread teardown to prevent connection leakage.

## 2. API Rate Limits & Backoff Strategies

To prevent external weather and routing provider blocks:
- **Bulk Leg Fetcher**: Segment lookups must use the parallel composite matrix solver (`BulkLegFetcher`) to handle L1 memory cache checks prior to executing batch remote API queries.
- **Exponential Backoff**: Concrete routing adapters should utilize an exponential backoff retry decorator with:
  - Base wait time: `1.0` second.
  - Multiplier: `2.0`.
  - Max retries: `3`.
- **Weather Forecast Failures**: If weather forecast API requests fail or exceed the 14-day window, the `CachedWeatherProvider` automatically falls back to climatology normals to maintain high reliability.

## 3. Telemetry and Diagnostics Metrics

The Anytime search solver collects execution diagnostics via `SolverMetrics` to measure and monitor solver health. Key performance indicators to track in server logs:

| Metric Name | Description | Alert Threshold (Soft / Hard) |
| :--- | :--- | :--- |
| `duration_ms` | Elapsed solver runtime for query | $> 60,000$ ms / $> 300,000$ ms |
| `evaluated_permutations` | Total branch node states evaluated | $> 50,000$ / $> 200,000$ |
| `pruned_branches` | Total early constraint pruning events | - / - |
| `l1_cache_hits` | Memory spatial cache lookups hit | $< 20\%$ |
| `l2_cache_hits` | Database spatial cache lookups hit | $< 30\%$ |

### Generating Logs Example
When running the solver, serialize recommendation performance telemetry combining solver metrics inside the recommendations JSON:
```json
{
  "solver_metrics": {
    "duration_ms": 142.5,
    "evaluated_permutations": 450,
    "pruned_branches": 850,
    "l1_cache_hits": 45,
    "l2_cache_hits": 90
  },
  "recommendations": [ ... ]
}
```
Use these telemetry payloads to trigger operational alerts or tune solver `beam_width` variables dynamically.

## 4. GraphHopper Service Lifecycle

When using `routing_provider.name: graphhopper`, GraphHopper must be running and ready before solver/report execution.

If `output.gpx` is enabled, report generation also exports a GPX file into `gpx/` using the best itinerary. The export is skipped automatically if it exceeds `output.gpx_timeout_seconds`.

### Startup and Readiness

```bash
docker compose -f docker-compose.graphhopper.yml up -d
curl -fsS http://localhost:8989/info | head -c 300 && echo
```

Helper scripts:

```bash
./scripts/graphhopper-stop.sh
./scripts/graphhopper-start.sh
./scripts/graphhopper-status.sh
```

OOM restart flow (without deleting downloaded data):

```bash
./scripts/graphhopper-stop.sh
./scripts/graphhopper-start.sh --mem-preset high --build
./scripts/graphhopper-status.sh
```

Start helper memory presets:

```bash
./scripts/graphhopper-start.sh --mem-preset medium
./scripts/graphhopper-start.sh --mem-preset high --build
./scripts/graphhopper-start.sh --mem-preset xxlarge --build
```

Supported presets: `low`, `medium`, `high`, `xlarge`, `xxlarge`.
`xxlarge` is tuned for a machine where roughly 64 GB RAM is available to Docker/CPU workloads, leaving headroom for the OS, page cache, and background services.
You can also set `GRAPHHOPPER_JAVA_OPTS` directly for custom heap sizes.

Example custom override above the built-in presets:

```bash
GRAPHHOPPER_JAVA_OPTS="-Xms32g -Xmx56g" ./scripts/graphhopper-start.sh --build
```

If `/info` does not return JSON yet, the server is still initializing.

Report generation commands that depend on GraphHopper should be treated as long-running operations. If you are regenerating all examples unattended, use the `--format all` mode so markdown, JSON, text, and GPX outputs are produced together.

### Reuse Across Scenarios

The Compose stack bind-mounts `.graphhopper/`, so OSM downloads and graph imports are persistent.

Keep these artifacts to avoid expensive rebuilds:
- `.graphhopper/map.osm.pbf`
- `.graphhopper/graph-cache/`

This allows repeated scenario runs with high route-cache hit rates in SQLite and faster end-to-end report generation.

### Periodic OSM Refresh Procedure

Use this when you want newer road network data:

```bash
docker compose -f docker-compose.graphhopper.yml down
rm -rf .graphhopper/graph-cache
rm -f .graphhopper/map.osm.pbf
GH_OSM_URL=https://download.geofabrik.de/north-america-latest.osm.pbf \
docker compose -f docker-compose.graphhopper.yml up -d --build
```

Equivalent helper script (safe by default):

```bash
./scripts/graphhopper-refresh.sh --yes
```

The refresh helper refuses to run unless `--yes` is supplied, to avoid interrupting an active download/import accidentally.

Guidance:
- Refresh cadence: monthly or quarterly for general touring use.
- Rebuild cost: expect long first startup after refresh (download + import + CH preparation).
- Coverage: choose a broader extract (for example North America) when routes may cross US/Canada borders.
