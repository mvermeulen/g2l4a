# Top 20 Improvement Ideas for g2l4a

Following a comprehensive review of the `g2l4a` project codebase, documentation, configurations, and test suites, here is a curated list of the top 20 improvement ideas. These recommendations aim to enhance solver performance, system reliability, operational safety, functionality, and user experience.

---

## I. Core Solver & Algorithm Optimization

### 1. Integrate Parallel Leg Pre-fetching (`BulkLegFetcher`)
> [!IMPORTANT]
> **Current State**: The `BulkLegFetcher` utility is implemented and tested (`test_phase2.py`) but remains unused in the core search loop of `BeamSearchSolver`.
>
> **Improvement**: During each beam-width depth expansion in the solver, the front of candidate routes must evaluate transitions to all remaining unvisited via-cities. Instead of making synchronous `get_leg_metrics` calls one by one, use `BulkLegFetcher` to fetch all next-step leg candidates concurrently. This will dramatically reduce search latency on cache-miss runs.

### 2. Enforce Duration Constraints (`max_total_days`)
> [!IMPORTANT]
> **Current State**: `max_total_days` is parsed from request configs, but it is never checked by the `FeasibilityEngine` or used to abort search branches in `BeamSearchSolver`.
>
> **Improvement**: Implement checks in `FeasibilityEngine.validate_itinerary` and `BeamSearchSolver` to enforce `max_total_days`. If a candidate itinerary's travel and rest days exceed this threshold, prune the branch early to prevent useless exploration and return structured `INFEASIBLE_TRIP_DURATION` violations.

### 3. Topography-Aware Segment Splitting (Realistic Daily Effort)
> [!TIP]
> **Current State**: When a leg requires multiple days (e.g., due to long distance or steep climbing), the solver splits the leg's distance and ascent equally across all transition days. This assumes a flat, uniform landscape.
>
> **Improvement**: Parse the detailed GPX elevation profile or track coordinate indices returned by GraphHopper to segment the leg into daily riding stages based on actual topography. This prevents a rider from being scheduled to climb a massive pass on a day modeled as flat, leading to much more realistic daily effort validation.

---

## II. Data Cache & Storage Management

### 4. Cache Database Index Optimization for Purges
> [!NOTE]
> **Current State**: `SQLiteCacheManager` defines a primary key index on coordinates, engine, and profile hash, but lacks indices on individual fields like `source` or `routing_engine`.
>
> **Improvement**: Cache purge methods (such as `purge_routing_cache_by_source` or `purge_routing_cache_by_engine`) execute table-scan deletes. Adding secondary indices on `source` and `routing_engine` will speed up these database maintenance routines, especially as the database grows to hundreds of megabytes.

### 5. Add Cache Size Limits and LRU Eviction Policies
> [!WARNING]
> **Current State**: The persistent cache database (`.g2l4a_cache.db`) grows indefinitely. There is no automated size limit or pruning mechanism for old, unused climatology or leg records.
>
> **Improvement**: Introduce a size cap or a maximum record count configuration. Implement an Least-Recently-Used (LRU) cache eviction script or background thread that prunes old records and performs an SQLite `VACUUM` to reclaim disk space.

### 6. SQLite Schema Migration Versioning (`user_version`)
> [!NOTE]
> **Current State**: Schema migrations are handled with ad-hoc `PRAGMA table_info` checks and table alterations inside `_init_db`.
>
> **Improvement**: Use SQLite's built-in `PRAGMA user_version` to track schema versions. Write a standard, linear migration runner. This keeps the database initialization clean, readable, and less error-prone when introducing future tables or indexes.

---

## III. External API Integrations & Resiliency

### 7. Enforce Rate Limiting on Nominatim Geocoding
> [!CAUTION]
> **Current State**: `RequestParser._resolve_city` issues rapid-fire HTTP queries to OpenStreetMap's Nominatim geocoder if multiple cities are not present in the offline `CITY_REGISTRY`. Nominatim requires strict client rate-limiting of 1 request per second.
>
> **Improvement**: Implement a small delay (e.g., `time.sleep(1.0)`) between sequential online geocoding lookups, and add a local cache check before starting the requests. This prevents Nominatim from blocking the application's IP address (HTTP 429/403).

### 8. Separate Tolerances for High and Low Temperature Comfort
> [!TIP]
> **Current State**: Weather scoring evaluates high temperatures against a single symmetric tolerance band around the ideal temperature. High and low temperature deviations are scored identically.
>
> **Improvement**: Allow configuring independent comfort profiles (e.g., ideal high temp vs. ideal low temp) and tolerances. A cold overnight low is often manageable with camping gear or hotels, whereas extreme daytime highs directly impact physical safety during cycling.

### 9. Asynchronous/Concurrent GPX Route Exports
> [!NOTE]
> **Current State**: GPX track downloads are fetched synchronously inside `example_report.py` and can take up to 90 seconds per file before timing out.
>
> **Improvement**: Fetch and write GPX outputs concurrently using a thread pool or an event loop. This ensures that generating reports for multiple scenarios concurrently does not get blocked by a slow GPX routing server response.

---

## IV. Configuration & Usability

### 10. Request-Level Validation using JSON Schema or Pydantic
> [!WARNING]
> **Current State**: Request YAML overrides are parsed into raw dictionaries. Type or value mismatches (e.g., passing a string for a score weight) fail late during execution with cryptic tracebacks.
>
> **Improvement**: Integrate a schema validator (like `jsonschema` or a lightweight validator class) to validate the input configuration structure *before* solver execution. Provide clear error messages showing exactly which YAML keys are invalid and why.

### 11. Per-Leg Custom Routing Profiles
> [!TIP]
> **Current State**: The routing profile (e.g., `bike`) is a global configuration applied to every leg in the itinerary.
>
> **Improvement**: Support specifying per-leg profile overrides (e.g., selecting `racingbike` for flat highway segments and `mtb` for gravel bypasses) in the request YAML. This will calculate much more accurate speeds, times, and suitability scores.

### 12. Timezone-Aware Weather Forecast Window Comparison
> [!NOTE]
> **Current State**: The 14-day weather forecast window is evaluated using local computer dates, which can cause timezone mismatches and caching errors around midnight.
>
> **Improvement**: Standardize all date calculations, current-time evaluations, and weather caching timestamps to UTC. This ensures consistent data retrieval and TTL checks regardless of the server's local timezone.

---

## V. Testing & Developer Experience

### 13. Mock Weather Provider Requests in Integration/Report Tests
> [!WARNING]
> **Current State**: Tests in `tests/test_phase8.py` run `generate_report_for_example` with the default `open_meteo` provider. Since they do not mock the outgoing network requests, the tests attempt real HTTP connections, causing severe execution delays or failures when running offline.
>
> **Improvement**: Add a mock patching fixture in `conftest.py` that automatically intercepts all outgoing HTTP weather queries in non-integration tests, ensuring the test suite remains fast, deterministic, and 100% offline-compatible.

### 14. Expand Mock Weather Provider to Support Seasons
> [!TIP]
> **Current State**: The `MockWeatherProvider` returns static/constant temperatures regardless of the simulated date, which makes it difficult to write realistic test scenarios for the optimize-date solver.
>
> **Improvement**: Update the mock weather provider to calculate temperatures using a simple sinusoidal curve based on the day of the year (representing summer/winter transitions). This will enable rich, offline tests of optimize-date selection without relying on remote climate databases.

---

## VI. UX & Output Enhancements

### 15. Rich GPX Output with Rest Day and Station Markers
> [!TIP]
> **Current State**: The exported GPX files merge all legs into a single continuous track with waypoints, but do not differentiate travel days, rest days, or scheduled daily stops.
>
> **Improvement**: Segment the GPX output using GPX Track Segments (`<trkseg>`) for each day of travel, and embed Waypoints (`<wpt>`) with metadata for rest-day cities and overnight stays. This will allow route viewers (like Garmin Connect, Strava, or Komoot) to display structured, multi-day itineraries.

---

## VII. New Functional Features

### 16. Loop / Round-Trip Tour Optimization
> [!TIP]
> **Current State**: The solver requires a distinct `start_city` and `completion_city` and finds an optimal path between them. It does not natively support round-trip loops.
>
> **Improvement**: Add support for a `loop: true` request option (or allow `completion_city` to match `start_city`). When active, the solver automatically treats the start city as the final destination and optimizes the intermediate via-cities sequence as a closed loop.

### 17. Dynamic, Forecast-Based Rest Day Insertion
> [!IMPORTANT]
> **Current State**: Rest days are statically configured at the city level (`rest_days`) and must be spent at that specific location, regardless of the active forecast during travel.
>
> **Improvement**: Introduce dynamic rest days where the solver can automatically schedule a rest day when a severe weather event (like heavy rain or extreme heat/cold) is forecasted for a travel day. Shifting travel days to rest days dynamically avoids dangerous riding conditions and preserves safety.

### 18. Road Surface Preference Scoring
> [!TIP]
> **Current State**: GraphHopper queries retrieve road surface statistics (e.g. paved vs unpaved mileage), and they are displayed in reports, but the `ScoringEngine` does not use them when ranking itineraries.
>
> **Improvement**: Introduce a new scoring category (`surface`) in `ScoringEngine` and add a corresponding weight override in `config/defaults.yaml`. Allow users to specify a preference (e.g., gravel-heavy vs asphalt-paved) and score candidate routes higher if their physical surface breakdown matches the user's preference.

### 19. Geographically Diverse Leg Alternatives (Scenic vs Direct)
> [!NOTE]
> **Current State**: The routing provider returns only the primary path for each leg. If the solver evaluates a segment, it is locked into one specific route.
>
> **Improvement**: Request alternative routes from GraphHopper (using the `algorithm=alternative_route` parameters) to fetch multiple geographically distinct paths for the same leg (e.g., a direct highway route vs a scenic, lower-traffic country bypass). Allow the solver to choose between these physical route variants during sequence search.

### 20. Multi-Rider / Group Constraint Merging
> [!IMPORTANT]
> **Current State**: The optimizer solves for a single set of constraints (e.g. a single rider's max miles, climb limit, and temperature bounds).
>
> **Improvement**: Support defining multiple rider profiles in the request YAML, each with their own capability parameters (e.g. Rider A: 50 mi max, Rider B: 75 mi max). The parser should automatically intersect these bounds (taking the minimum of maximums and the tightest comfort limits) to solve for a route safe for the entire group.
