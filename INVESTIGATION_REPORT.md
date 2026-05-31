# Investigation Report

## 1. Problem Statement (Draft)
Status: Captured from stakeholder input (needs refinement)

Summary:
- Build a program to help plan long bicycle tours.
- Input is a structured problem statement (for example YAML) that includes:
	- a start city,
	- a completion city,
	- and optional via cities that must be visited.
- The system should search candidate routes and recommend a best ordering and path through cities.
- Reordering via cities is a key optimization lever and should be actively explored to maximize route desirability.

Business or user impact:
- Makes multi-city bicycle tour planning practical and data-driven instead of manual.
- Reduces risk of uncomfortable or unsafe route choices by accounting for adverse weather and steep terrain.
- Saves planning time while balancing trip quality and trip efficiency.

Observed symptoms:
- Current process is undefined/manual and does not consistently balance route length, weather exposure, and elevation profile.

## 2. Scope and Boundaries
In scope:
- Parse structured tour request input (YAML initially).
- Generate candidate route sequences between start, via, and completion cities, including permutations of via-city order.
- Model trips as staged multi-day journeys using daily caps (distance/climb) across the full itinerary.
- Score and rank candidates using multiple objectives:
	- enforce absolute weather constraints,
	- apply weather preference scoring within acceptable ranges,
	- keep route reasonably short,
	- favor fewer hills (lower climbing burden), including directional effects.
- Support two planning modes for trip start timing:
	- fixed-date mode: user supplies start date,
	- optimize-date mode: solver selects a best start date.
- Return recommendation for city visit order and associated route summary.

Out of scope:
- Turn-by-turn navigation UX and live on-bike guidance (initially).
- Full travel booking/logistics automation (accommodation, transport, etc.).

Constraints:
- Multi-objective trade-offs are required; no single metric defines the best route.
- Must support mandatory via-city constraints.
- Weather data quality and forecast horizon will influence reliability.
- Weather must support hard limits (filtering) and soft preferences (ranking).
- If no feasible route satisfies hard weather constraints, solver must fail fast.
- Solver must not auto-relax hard constraints; user should explicitly adjust configuration.
- In infeasible cases, output must include clear diagnostics explaining why no solution was found and which constraints likely caused infeasibility.
- Route recommendations should avoid highways/interstates (similar to an "avoid highways" routing preference) and respect bicycle-legal roads.
- Route feasibility policy allows international border crossings and ferry segments when needed.
- Route recommendations should avoid toll roads by default.
- Recommendations are approximate/costed planning outputs, not guaranteed final turn-by-turn navigation choices.
- Daily effort limits should be configurable with defaults:
	- daily mileage cap: 80 miles,
	- daily climbing cap: 5000 ft.
- No hard maximum total trip duration is imposed; planner may recommend trips that take as long as needed while optimizing overall desirability (including distance efficiency).
- Maximum cities per request should be capped at 50 (configurable).
- Solver search runtime should be bounded by a configurable budget with default 10 minutes.
- Planning model should treat routes as larger staged multi-day trips by default.
- Detailed output schema is intentionally deferred until example outputs are generated and reviewed.
- Initial output should be human-readable and include ordered cities with dates and average weather context.
- Uncertainty indicators are deferred for now (not required in v1 output).
- Backward-compatible YAML evolution is not a v1 priority.
- Validation/error handling can be iterative in early development, with issues addressed as they are encountered.

## 3. Current Understanding
Known facts:
- Primary domain: long-distance bicycle tour planning.
- Input format target: YAML problem specification.
- Key optimization dimensions: weather risk, route distance, hilliness/elevation burden.
- Via cities can be reordered, and ordering optimization is a core problem requirement.
- Weather has two levels:
	- hard constraints (for example, reject cities where average high is above X or average low is below Y),
	- soft preference scoring within those accepted ranges.
- Default hard weather thresholds are confirmed as:
	- reject if average high temperature is above 90F,
	- reject if average high temperature is below 32F.
- Thresholds must be configurable in YAML input, with these defaults applied when fields are omitted.
- Hills are primarily a preference signal, and route direction can materially change climbing burden in some regions.
- Start date must support either user-fixed input or solver-selected optimization.
- Start-date behavior is confirmed:
	- if start date is provided, trip must start on that exact date,
	- if start date is omitted, solver may search any calendar date within the year.
- Routing policy should emulate an "avoid highways" preference and avoid freeway/interstate segments where bicycles are not allowed.
- Border and ferry crossings are allowed.
- Tolls should be avoided by default (also treated as a useful proxy for likely non-bicycle-friendly road choices).
- Program output is intended as a rough costed recommendation; manual route refinement outside the program is expected.
- Daily caps are configuration-driven with defaults of 80 miles/day and 5000 ft climb/day.
- Overall trip duration has no hard cap; total distance remains an optimization objective.
- Request size is capped at 50 total cities by default (configurable cap).
- Search runtime target defaults to under 10 minutes with configurable timeout budget.
- If hard constraints make the problem infeasible, the solver fails fast and returns actionable reason codes/details rather than auto-relaxing constraints.
- Trip structure is confirmed as staged multi-day routing for the overall itinerary, with daily constraints applied per stage.
- Weather preference scoring inside allowed ranges is linear for v1.
- Hill penalty uses total ascent only for v1.
- Distance objective uses route mileage for v1.
- Output design is intentionally iterative: generate examples first, then tune output schema/format.
- Audience is human readers; output should prioritize readability over machine-oriented verbosity.
- YAML schema versioning/backward compatibility is deprioritized for v1.
- Error policy for v1 is pragmatic/iterative: address validation and edge-case failures as they surface during testing.

Assumptions:
- City-to-city routing data can be sourced from mapping/routing services.
- Weather can be represented as a route segment penalty score.
- Elevation burden can be approximated by total ascent and/or gradient penalties.

Unknowns:
- Exact objective weighting (weather vs distance vs hills).
- Whether optimization should be deterministic or provide configurable profiles.
- Geographic scope, time windows, and acceptable computational runtime.
- Final output format style is confirmed; exact output schema remains to be finalized.
- In optimize-date mode, what date search window is allowed (season, month range, explicit bounds)?
- Which weather source/baseline to use for planning (historical normals vs forecast vs blended)?

## 4. Evidence and Reproduction
Environment:
- OS: Linux
- Runtime/tooling:
- Versions:

Reproduction steps:
1. Load the fixed-date test input scenario (Austin to Washington, DC, with required via capitals).
2. Run the planner in fixed-date mode with start date February 1.
3. Verify output returns one best route plus alternatives (default up to 4), with via-city reordering and weather constraints honored.
4. Load the optimize-date version of the same scenario (no start date provided).
5. Run the planner in optimize-date mode over full-year date search.
6. Verify output includes selected optimal start date and route recommendations.

Expected result:
- Planner returns a valid route from Austin, Texas to Washington, DC.
- All required via cities are included exactly once.
- Via city order is optimized by desirability, not fixed input order.
- Hard weather constraints are enforced using defaults unless overridden.
- Output includes one best recommendation plus alternatives (default up to 4).
- Optimize-date mode selects a start date within the calendar year.

Actual result:
- [To be documented]

Frequency/severity:
- [To be documented]

## 5. Affected Areas
Systems/components potentially involved:
- [To be identified]

User journeys affected:
- [To be identified]

Data/contracts/interfaces affected:
- [To be identified]

## 6. Hypotheses
Hypothesis 1:
- Statement:
- Why plausible:
- Evidence for/against:

Hypothesis 2:
- Statement:
- Why plausible:
- Evidence for/against:

## 7. Risks and Impact Assessment
Operational risk:
- [To be assessed]

Security/privacy/compliance risk:
- [To be assessed]

Performance/reliability risk:
- [To be assessed]

## 8. Questions Requiring Clarification
1. How should objective trade-offs be weighted between weather, distance, and hills?
2. Via-city ordering flexibility: Confirmed solver may reorder to improve desirability.
3. Weather handling confirmed as both hard constraints and soft preferences.
4. Output style confirmed as one best plus alternatives (default up to 4).
5. Start-date behavior confirmed as fixed-date if provided, otherwise optimize over full year.
6. For weather data, should initial implementation use climate averages, forecast data near departure, or both?

### 8.1 Additional Pre-Implementation Questions
Data and external dependencies:
1. Which routing provider should be used first (for example OpenStreetMap/OSRM, GraphHopper, commercial API), and what fallback strategy is required if the provider is unavailable?
2. What weather dataset is authoritative for v1 (historical normals, forecast, or hybrid), and what geographic/temporal resolution is required (city-level monthly, daily grid, route-segment level)?
3. Should elevation come from the routing provider, a DEM source, or both when conflicting?

Route feasibility and safety rules:
4. Should route optimization prioritize bicycle-safe roads only, and are highways/limited-access roads always disallowed?
5. Are there hard caps for total daily distance, total trip duration, or daily climbing that should filter candidates?
6. Should international border crossings, ferries, or toll roads be allowed/disallowed by default?

Solver behavior:
7. What is the maximum expected number of via cities for v1, and what runtime target is acceptable for a typical request?
8. If no feasible route satisfies hard weather constraints, should the solver fail fast, relax constraints automatically, or return nearest-feasible explanations?
9. Trip structure confirmed: optimize as one larger staged multi-day trip (daily-cap constrained), not a single-day/continuous-only model.

Scoring semantics:
10. Weather preference shape confirmed for v1: linear within allowed ranges.
11. Hill penalty confirmed for v1: total ascent only.
12. Distance metric confirmed for v1: route mileage only.

Output contract and explainability:
13. Exact output schema is deferred until initial examples are generated and reviewed.
14. Human-readable output is required for v1, including ordered city list and practical summary context.
15. Uncertainty/confidence indicators are deferred for now (not required in v1).

Configuration and validation:
16. YAML schema versioning/backward compatibility is not a v1 requirement.
17. Validation strictness will be tuned iteratively based on observed errors during development/testing.
18. Defaults strategy confirmed: hierarchical YAML with system defaults file and user-input overrides.

Testing and reproducibility:
19. Do we need deterministic replay mode with pinned data snapshots for regression testing?
20. What minimum fixture set is required beyond the US Capitals scenario (for example mountain-heavy case, hot-climate case, sparse-via case)?

### 8.2 Decision Status Snapshot
1. Routing provider strategy:
	- MVP provider: hosted OpenRouteService for quick startup.
	- Production target: self-hosted GraphHopper (or Valhalla) for reliability and quota independence.
	- Status: Tentative.
	- Finalization criteria:
		- bike-routing quality on fixture scenarios,
		- acceptable latency and uptime expectations,
		- operational complexity and maintenance burden.

2. Weather-data strategy:
	- Baseline climatology source: NOAA/NCEI (US-focused) or Meteostat historical normals for seasonality and optimize-date scoring.
	- Forecast overlay source: Open-Meteo for near-term fixed-date planning adjustments.
	- Combination approach:
		- far-future or unspecified date optimization relies primarily on climatology,
		- near-term fixed-date planning increases forecast influence.
	- Status: Tentative.
	- Finalization criteria:
		- coverage completeness for required cities/routes,
		- consistency of metric definitions (avg highs/lows) across sources,
		- API reliability/rate limits and ease of integration,
		- reproducibility support via data snapshot pinning for tests.

3. Elevation-data strategy:
	- Primary source: use elevation/ascent metrics returned by the selected routing provider.
	- Fallback: if elevation is unavailable or low quality for a segment, use a DEM-based source for recomputation.
	- Operational rule: prefer one canonical ascent metric pipeline per run to avoid mixed-source scoring artifacts.
	- Status: Tentative.
	- Finalization criteria:
		- coverage across all fixture routes,
		- consistency of total ascent values between repeated runs,
		- acceptable correlation with sampled ground-truth checks,
		- latency impact within runtime targets.

4. Route safety/legality policy:
	- Default routing preference should mirror "avoid highways" behavior.
	- Exclude freeway/interstate segments and other non-bicycle-legal roads from candidate generation.
	- International border crossings and ferry crossings are allowed.
	- Avoid toll roads by default.
	- Objective is a rough costed planning recommendation; exact final roads may be refined manually outside the tool.
	- Status: Confirmed.

5. Distance/climb/duration policy:
	- Daily limits are configurable with defaults:
		- max miles per day: 80
		- max climb per day: 5000 ft
	- No hard maximum total trip duration for v1 (effectively "as long as it takes").
	- Planner continues to optimize for route desirability, including shorter overall distance.
	- Status: Confirmed.

6. Scale/runtime policy:
	- Maximum cities per request: 50 (configurable).
	- Solver runtime budget default: 10 minutes (configurable timeout).
	- Solver should return best-found recommendations within the runtime budget.
	- Status: Confirmed.

7. Infeasibility handling policy:
	- If no feasible route satisfies hard weather constraints, fail fast.
	- Do not auto-relax hard constraints.
	- Return clear diagnostics that identify likely blocking constraints so users can choose what to relax.
	- Diagnostics must provide a detailed breakdown of which exact cities/legs violate the constraints, the date of violation, the observed value, and the configured threshold (e.g., `Jackson, MS: average high temperature was 92F (max limit: 90F) on July 15`).
	- Status: Confirmed.

8. Trip structure policy:
	- Treat each plan as one overall staged multi-day trip.
	- Apply daily caps per stage/day (distance and climbing).
	- No hard max total duration; trip length emerges from route geometry plus daily constraints.
	- Status: Confirmed.

9. Scoring semantics policy:
	- Weather preference scoring within feasible bounds is linear for v1.
	- Hill penalty metric uses total ascent only for v1.
	- Distance metric uses route mileage for v1.
	- Status: Confirmed.

10. Output evolution policy:
	- Defer strict output schema decisions until example outputs are produced.
	- V1 output must be human-readable and include ordered cities, planned dates, and average weather context in tabular form where practical.
	- Uncertainty indicators are not required for v1.
	- Status: Confirmed.

11. Schema/versioning and error-handling policy:
	- Backward-compatible YAML versioning is not required for v1.
	- Do not block on schema-version architecture upfront; evolve format pragmatically.
	- Work through validation/runtime errors as they appear during iterative testing.
	- Status: Confirmed.

### 8.3 Decision Log (Current Status)
1. Scoring weights/profile lock for v1:
	- Status: Confirmed.
	- Decision resolved:
		- whether to launch with one fixed default profile only, or support multiple named profiles in v1.
		- whether user-specified custom weights are allowed in v1.
	- Proposed default if undecided:
		- single fixed default profile in v1,
		- weights: weather 0.45, distance 0.30, hills 0.25,
		- allow custom weights only if non-negative and sum to 1.
	- Impact if unresolved:
		- ranking behavior remains ambiguous and can cause implementation churn.
	- Clarified proposal for confirmation:
		- v1 ships with one fixed default profile only (no named profiles in v1 output contract),
		- keep custom weights optional but gated by validation:
			- all weights >= 0,
			- sum exactly 1 within tolerance,
			- reject invalid configs with clear error diagnostics.
	- Closure criteria:
		- defaults produce stable, domain-acceptable ranking on fixed-date and optimize-date fixtures,
		- custom-weight validation behavior is deterministic and test-covered.

2. Weather data blending and resolution rule for v1:
	- Status: Confirmed.
	- Decision resolved:
		- exact rule for climatology vs forecast blending by planning horizon,
		- required data granularity (city-level monthly/daily vs segment-level),
		- fallback behavior when forecast provider is unavailable.
	- Proposed default if undecided:
		- use city-level monthly normals for optimize-date and long-horizon planning,
		- use forecast overlay only for near-term fixed-date planning,
		- if forecast unavailable, fallback to climatology and emit a warning.
	- Impact if unresolved:
		- feasibility/ranking behavior may vary unpredictably and reduce reproducibility.
	- Clarified proposal for confirmation:
		- optimize-date mode uses climatology baseline only,
		- fixed-date mode uses horizon-based blending (14-day horizon):
			- near-term departure window (within 14 days of start date): apply forecast overlay,
			- long-horizon departures (beyond 14 days of start date): use climatology only,
		- fallback when forecast unavailable:
			- use climatology,
			- emit explicit warning/diagnostic field in output.
	- Resolution level for v1:
		- city-level daily/monthly representation is acceptable for v1,
		- defer segment-level weather modeling to a later phase.
	- Closure criteria:
		- identical inputs and data snapshot produce reproducible feasibility/rank outcomes,
		- fallback behavior is observable and test-covered.

Output rule:
- Status: Confirmed.
- Return one best recommendation plus alternatives.
- Default alternatives count: up to 4.
- Alternatives count must be configurable in YAML input, with default applied when omitted.

Start-date rule:
- Status: Confirmed.
- input.start_date present: enforce exact start date.
- input.start_date absent: optimize across full-year date domain.

Proposed YAML defaults:
- Status: Confirmed.
- weather_constraints.max_avg_high_f: 90
- weather_constraints.min_avg_low_f: 24
- Behavior: if omitted in input, solver uses defaults above.
- daily_constraints.max_miles_per_day: 70
- daily_constraints.max_climb_ft_per_day: 5000
- duration_constraints.max_total_days: null (no hard cap)
- solver_constraints.max_total_cities: 50
- solver_constraints.max_search_minutes: 10

Hierarchical YAML defaults model:
- Status: Confirmed.
- Source order (highest precedence first):
	1. user input YAML
	2. system defaults YAML
	3. built-in hardcoded fallback defaults (safety net only)
- Merge rule: deep-merge maps by key; if a key is present in user YAML, it overrides the same key in system defaults.

Example system defaults YAML (for example config/defaults.yaml):
```yaml
defaults:
	weather_constraints:
		max_avg_high_f: 90
		min_avg_low_f: 24

	daily_constraints:
		max_miles_per_day: 70
		max_climb_ft_per_day: 5000

	duration_constraints:
		max_total_days: null

	solver_constraints:
		max_total_cities: 50
		max_search_minutes: 10

	scoring:
		weights:
			weather: 0.45
			distance: 0.30
			hills: 0.25

	routing_preferences:
		avoid_highways: true
		avoid_tolls: true
		allow_ferries: true
		allow_international_borders: true
```

Example user input YAML (partial overrides only):
```yaml
start_city: Austin, Texas
completion_city: Washington, DC

weather_constraints:
	max_avg_high_f: 85

solver_constraints:
	max_search_minutes: 6
```

Effective configuration behavior:
- If user input omits a field, planner reads it from system defaults.
- If both are missing, planner uses built-in fallback defaults.
- This allows the same schema to be used for both global config and per-request input.

## 9. Compute-Time Optimization Analysis

Context:
- The route-search space grows combinatorially with the number of required via cities.
- If there are $n$ via cities and we test every ordering, permutations alone are $n!$ (before date choices and alternative route variants per leg).
- For the US capitals example with 15 via cities, exhaustive permutation search is infeasible ($15! = 1,307,674,368,000$ possible orderings).

### 9.1 Reduce Cost of Individual Route Evaluation (Caching and Reuse)

Objective:
- Cut repeated work in segment-level evaluation so each candidate route is cheaper to score.

Techniques:
1. Pairwise route cache (city A -> city B):
	- Cache deterministic outputs that rarely change:
		- distance,
		- ascent,
		- route geometry summary,
		- legality/safety flags (bike-legal, toll/highway avoidance).
	- Canonicalize city identifiers (stable IDs/coordinates) to avoid cache misses from naming variations.
	- Include routing profile in cache key (bike mode, avoid_highways, avoid_tolls, allow_ferries).

2. Direction-aware caching:
	- Keep separate entries for A -> B and B -> A because climb and recommended roads can differ by direction.
	- Distance may be similar; ascent and legality can differ materially.

3. Weather/climate memoization by (location, time bucket):
	- Cache climatology data by city and month/day bucket.
	- Cache forecast snapshots with explicit timestamp/version so stale forecasts are not reused silently.
	- For optimize-date mode, precompute weather score tables per city across date buckets once, then reuse across many route candidates.

4. Segment-feasibility precheck cache:
	- Memoize whether a segment can satisfy daily caps (miles/climb) and weather hard constraints for a given date bucket.
	- If a segment is infeasible under current constraints, prune any candidate containing it without full rescoring.

5. In-memory + persistent cache layers:
	- L1: process-memory cache for fast repeated lookups within one run.
	- L2: local persistent cache (disk/SQLite/LMDB) shared across runs.
	- Use TTL/versioning keyed to provider version and routing-policy hash.

Expected impact:
- Large reduction in API calls and repeated route computations.
- Biggest gains when evaluating many permutations that reuse the same city-pair legs.

Risks/notes:
- Cache invalidation is critical when routing policy or data source changes.
- Must track provenance (provider, profile, timestamp) for reproducibility.

### 9.2 Search More Effectively (Find Good Solutions Faster)

Objective:
- Avoid exhaustive search; spend compute on promising regions of the solution space.

Techniques:
1. Two-phase optimization:
	- Phase A (cheap): build/score approximate pairwise cost matrix using cached segment metrics and simplified weather model.
	- Phase B (expensive): run full route and schedule evaluation only on top-K candidate orderings.

2. Branch-and-bound with admissible lower bounds:
	- Build partial routes incrementally.
	- Compute lower bound using optimistic remaining distance/weather/hill cost.
	- Prune branches whose bound is worse than current best.

3. Beam search / best-first search:
	- Keep only the best B partial routes at each depth (beam width B is tunable).
	- Often reaches high-quality solutions quickly under strict runtime budgets.

4. Metaheuristics for large N:
	- Seed with constructive heuristic (nearest-neighbor or regret insertion).
	- Improve with local search (2-opt/3-opt/swap/relocate).
	- Use simulated annealing or tabu search when local minima become problematic.

5. Candidate-list restriction:
	- For each city, only consider next-city choices from a nearest/promising subset under weighted proxy cost.
	- Dramatically reduces branching factor with limited quality loss when tuned well.

6. Dominance rules and early infeasibility pruning:
	- If two partial states end at same city/date bucket and one is no better on all objectives, discard dominated state.
	- Reject partial plans as soon as hard weather or daily-cap infeasibility is detected.

7. Anytime solver behavior:
	- Continuously keep best-so-far solution.
	- Return best available plan when runtime budget expires (default 10 minutes), with quality/confidence metadata.

Expected impact:
- Orders-of-magnitude fewer full evaluations than brute force.
- Predictable performance under configurable time budgets.

Risks/notes:
- Heuristic bias can miss globally optimal routes; mitigate with diversification/restarts.
- Need calibration so pruning is aggressive but not over-pruning feasible high-quality regions.

### 9.3 Hardware-Aware Programming (Parallelism and Systems Techniques)

Objective:
- Increase throughput by evaluating independent work concurrently and minimizing overhead.

Techniques:
1. Parallel candidate evaluation:
	- Evaluate independent route candidates across CPU cores using a worker pool.
	- Use chunked work-stealing to keep cores busy as task durations vary.

2. Parallel segment precomputation:
	- Precompute pairwise city metrics concurrently at startup (bounded by provider rate limits).
	- Store results in shared cache used by all search workers.

3. Hybrid concurrency model:
	- Async I/O for API-bound steps (routing/weather fetches).
	- Multi-process or native-thread parallelism for CPU-heavy scoring/search steps.

4. Batched/vectorized scoring:
	- Evaluate weather and objective components for multiple candidates in batches to reduce per-item overhead.
	- Useful if using NumPy/polars-like vector operations.

5. Multi-level budget control:
	- Global timeout (already defined), plus per-stage budgets:
		- precompute budget,
		- search budget,
		- refinement budget.
	- Prevents one phase from starving others.

6. Deterministic parallel mode (for tests):
	- Fixed RNG seeds and deterministic reduction order when required for regression stability.
	- Non-deterministic high-throughput mode for production runs.

Expected impact:
- Near-linear speedups for embarrassingly parallel portions until bottleneck shifts to I/O or synchronization.
- Better hardware utilization on multi-core systems.

Risks/notes:
- External API rate limits can dominate performance if not throttled.
- Shared-cache contention and serialization costs can erode gains; design lock strategy carefully.

### 9.4 Suggested v1.5 Experiment Plan (Low Risk, High Return)

1. Add pairwise segment cache with profile-aware keys and directional entries.
2. Add cheap-matrix precompute plus two-phase search (top-K full evaluations).
3. Introduce beam search with configurable beam width and runtime budget.
4. Parallelize full-candidate evaluation using worker pool.
5. Instrument metrics:
	- cache hit rate,
	- route evaluations per second,
	- pruned-branch count,
	- time spent by phase,
	- best-score improvement over time.

Success criteria:
- Achieve at least 5x reduction in median solve time on benchmark fixtures, while preserving recommendation quality within an agreed tolerance.

### 9.5 Open Decisions for Compute Strategy

This section is retained as a pointer only.
- Canonical decision statuses are tracked in Section 9.6.
- Keep updates in one place to avoid drift.

### 9.6 Clarified Decision Proposals (For Confirmation)

This section narrows open decisions into default positions for v1 so behavior is predictable, while keeping them explicitly reversible if later evidence disagrees.

1. Optimality vs speed target (clarified proposal):
	- Status: Confirmed.
	- Proposed v1 policy:
		- default solver mode is best-effort anytime under runtime budget, using **Beam Search / Anytime Best-First Search** to navigate the route permutation space.
		- for `optimize-date` mode, use a **two-phase search**: filter by monthly/weekly average weather first to target promising seasonal windows, followed by high-resolution daily search inside those windows.
		- for small instances only, allow optional exact mode when city count is below a configurable threshold.
	- Suggested threshold:
		- exact mode eligible when via-city count <= 8 (tunable after benchmark results).
	- Why this clarifies ambiguity:
		- establishes predictable runtime behavior for realistic workloads,
		- preserves a path to exactness on tractable small cases.

2. Cache persistence policy (clarified proposal):
	- Status: Confirmed.
	- Proposed v1 policy:
		- persistent cache enabled by default across runs,
		- cache key includes provider, routing profile, constraints hash, and data-version stamp.
	- Invalidation defaults:
		- hard invalidate on provider/profile/schema version change,
		- soft TTL for weather forecast entries (for example 6-24 hours),
		- longer TTL (or no TTL) for static route geometry unless provider version changes.
	- Why this clarifies ambiguity:
		- gives immediate performance gains while making staleness controls explicit.

3. Parallelism limits (clarified proposal):
	- Status: Confirmed.
	- Proposed v1 policy:
		- worker_count defaults to min(max(2, cpu_cores - 1), provider_safe_parallelism_cap),
		- provider_safe_parallelism_cap should default conservatively (for example 4) unless operator overrides.
	- Additional guardrails:
		- separate I/O concurrency limit from CPU worker count,
		- use adaptive backoff when provider rate-limit responses are detected.
	- Why this clarifies ambiguity:
		- avoids overloading external APIs while still using available local CPU.

4. Reproducibility mode (clarified proposal):
	- Status: Confirmed.
	- Proposed v1 policy:
		- deterministic mode mandatory for CI/regression test runs,
		- production defaults to non-deterministic high-throughput mode,
		- deterministic mode can be enabled in production for incident replay.
	- Deterministic guarantees should include:
		- fixed RNG seed,
		- stable tie-breaking,
		- deterministic result ordering before output.
	- Why this clarifies ambiguity:
		- keeps tests stable while preserving runtime efficiency in normal operations.

5. Decision closure criteria (applies to all four compute decisions):
	- Status: Confirmed.
	- Confirm decision when benchmark fixtures show:
		- median runtime within configured budget,
		- recommendation quality not materially degraded versus current baseline,
		- stable repeatability in deterministic mode,
		- acceptable provider error/rate-limit behavior.
	- If criteria fail, revise only the relevant decision and re-test; do not reopen unrelated confirmed policies.

6. GPU acceleration opportunity (clarified investigation question):
	- Status: Confirmed (Deferred/No-go for v1).
	- Core question:
		- does this workload benefit more from GPU offload, or from CPU-core parallelism plus caching and pruning?
	- Preliminary assessment:
		- routing API calls, branch-heavy search expansion, and cache-heavy orchestration are CPU/I/O bound,
		- these components see limited GPU benefit due to transfer overhead and irregular control flow,
		- CPU parallelism is confirmed as the path for v1.
	- Where GPU may help:
		- batched scoring of very large candidate sets (vector math over weather/distance/hill arrays),
		- large matrix operations during heuristic precompute,
		- Monte Carlo/sensitivity sweeps run offline at high volume.
	- Decision gate for GPU adoption:
		- adopt GPU only if profiling shows at least 40% runtime in vectorizable numeric kernels and projected end-to-end speedup >= 2x on target hardware after transfer overhead.
	- Investigation method:
		- profile phase-level runtime split (I/O vs search control vs numeric scoring),
		- prototype one isolated GPU-friendly kernel (batched scoring),
		- compare total wall-clock and cost/performance against optimized CPU baseline.
	- Tentative default:
		- CPU-first architecture with pluggable scoring backend so GPU can be added later without redesign.

## 10. Scoring Method (Draft)
Scoring model overview:
- Use a two-stage evaluation pipeline:
	- Stage 1 feasibility filtering: reject candidates violating hard constraints (for example weather limits).
	- Stage 2 desirability scoring: rank feasible candidates by weighted soft objectives.

Soft-score components:
- Weather preference score $S_weather \in [0,1]$, linear within configured feasible weather bounds.
- Distance score $S_distance \in [0,1]$ where shorter route mileage scores higher.
- Hills score $S_hills \in [0,1]$ where lower total ascent scores higher.

Normalization approach:
- For each candidate $i$ in the current comparison set:
- $S_distance(i) = 1 - (d_i - d_{min}) / (d_{max} - d_{min})$
- $S_hills(i) = 1 - (h_i - h_{min}) / (h_{max} - h_{min})$
- If a denominator is 0 (all candidates equal on a metric), assign that metric score as 1 for all candidates.

Weighted combination:
- $S_total(i) = w_weather \cdot S_weather(i) + w_distance \cdot S_distance(i) + w_hills \cdot S_hills(i)$
- Constraints:
	- $w_weather + w_distance + w_hills = 1$
	- all weights are non-negative.

Initial default weights (proposed for v1):
- weather: 0.45
- distance: 0.30
- hills: 0.25

Rationale:
- Prioritize thermal comfort/risk avoidance while still favoring efficient and lower-climb routes.

YAML configuration (defaults if omitted):
```yaml
scoring:
	weights:
		weather: 0.45
		distance: 0.30
		hills: 0.25
```

Calibration process:
- Validate defaults on fixed-date and optimize-date test scenarios.
- Perform sensitivity tests by varying one weight at a time by +/-0.10.
- Adjust defaults in 0.05 increments when ranking outcomes conflict with domain expectations.
- Optionally define named profiles later (for example balanced, comfort-first, low-climb).

### 10.1 Acceptance Criteria for Scoring (Pass/Fail)
Test set:
- Use the US Capitals Corridor Example fixtures:
	- fixed-date variant (start_date present),
	- optimize-date variant (start_date omitted).

Pass/Fail test cases:
1. Hard weather constraint enforcement:
	- Pass: every returned recommendation satisfies configured hard weather thresholds.
	- Fail: any returned recommendation includes a city/segment violating thresholds.

2. Fixed-date compliance:
	- Pass: when input start_date is provided, all returned recommendations use that exact date.
	- Fail: any returned recommendation shifts or overrides the provided date.

3. Optimize-date compliance:
	- Pass: when start_date is omitted, output includes a solver-selected start date within the calendar year.
	- Fail: no selected date is returned, or selected date lies outside the allowed year domain.

4. Ranking correctness by total score:
	- Pass: recommendations are sorted in non-increasing order of total score $S_total$.
	- Fail: any lower-ranked option has a higher $S_total$ than a higher-ranked option.

5. Weight normalization and validity:
	- Pass: configured weights are non-negative and sum to 1 (or are normalized to sum to 1 before scoring).
	- Fail: scoring runs with invalid weights without normalization/error handling.

6. Alternatives count behavior:
	- Pass: output contains exactly one best recommendation and up to configured alternatives count (default 4).
	- Fail: output exceeds configured limit or omits primary best recommendation.

7. Via-city inclusion and uniqueness:
	- Pass: each required via city appears exactly once in each returned route.
	- Fail: any required via city is missing or duplicated.

8. Via-city reorderability:
	- Pass: solver is allowed to reorder via cities and can return an order different from input when it improves score.
	- Fail: solver always preserves input order regardless of score impact.

9. Deterministic reproducibility (fixed inputs, fixed data snapshot):
	- Pass: repeated runs produce identical scores and ranking when inputs, weights, and data snapshot are unchanged.
	- Fail: repeated runs produce unexplained score or rank drift.

10. Sensitivity sanity check:
	- Pass: increasing one weight by 0.10 (with renormalization) changes ranking only when that objective is materially different among candidates.
	- Fail: tiny weight changes cause unstable, non-intuitive ranking flips across near-identical candidates.

Scoring acceptance threshold for release readiness:
- Required to pass: tests 1 through 8.
- Recommended to pass before production hardening: tests 9 and 10.

## 11. Recommended Next Investigation Steps
1. Resolve still-open compute policies in Section 9.6:
	- optimality vs speed threshold,
	- parallelism default limits,
	- decision-closure criteria,
	- GPU investigation outcome.
2. Define provider operations policy:
	- API quota/rate-limit handling,
	- outage fallback behavior,
	- cost guardrails for sustained runs.
3. Define reproducibility and provenance envelope:
	- required run metadata,
	- data snapshot/version capture,
	- deterministic replay requirements beyond CI.
4. Expand benchmark fixture coverage beyond US capitals:
	- mountain-heavy case,
	- extreme heat/cold case,
	- sparse-road/ferry-dependent case,
	- larger-city-count stress case.
5. Specify failure taxonomy and user-facing diagnostics contract:
	- standardized reason codes,
	- blocking vs warning classification,
	- remediation hints in infeasibility output.

## 12. Pre-Implementation Checklist
Use this checklist to confirm investigation completeness before starting implementation planning.

Status legend:
- [ ] Open
- [x] Completed

Compute strategy:
- [x] Confirm optimality vs speed default and exact-mode threshold (Two-phase search & Beam Search).
- [x] Confirm default parallelism limits and provider-safe concurrency cap (Worker count based on CPU cores).
- [x] Finalize decision-closure thresholds (runtime, quality, repeatability).
- [x] Close GPU investigation with explicit go/no-go decision and trigger criteria (GPU deferred/No-go for v1).

Provider operations:
- [x] Define routing/weather provider rate-limit and quota handling behavior (Bypassed via local routing server; weather queries cached/batched).
- [x] Define outage/degraded-service fallback behavior.
- [x] Define cost guardrails for sustained or batch runs (Local server mitigates transaction costs; persistent SQLite L2 cache limits redundant queries).

Reproducibility and provenance:
- [x] Define mandatory run metadata captured for every solve (Timestamp, solver_duration_ms, cache_hit_rate, evaluated_permutations, routing_provider_version).
- [x] Define data snapshot/version capture requirements for external inputs.
- [x] Define deterministic replay scope outside CI (for incident analysis/support).

Quality and benchmarking:
- [x] Approve expanded fixture set (mountain, extreme climate, sparse-road/ferry, stress-size).
- [x] Define baseline comparison method and non-regression thresholds.
- [x] Confirm benchmark reporting format (runtime percentiles, quality deltas, failure rates).

Diagnostics contract:
- [x] Finalize standardized reason-code taxonomy (Standard codes: INFEASIBLE_WEATHER_MAX_HIGH, INFEASIBLE_WEATHER_MIN_LOW, INFEASIBLE_DAILY_DISTANCE, INFEASIBLE_DAILY_CLIMB).
- [x] Finalize blocking vs warning classification rules (Hard constraint failures are blocking; network fallbacks are warnings).
- [x] Finalize remediation-hint content requirements for infeasible results (Detailed location-specific breakdown of violations, e.g., 'Jackson, MS: avg high temperature was 92F on July 15, exceeding max limit of 90F').

Implementation-planning readiness check:
- [x] Checklist reviewed and signed off by stakeholders.

## 13. Decision Gate (Before Development)
Ready for implementation: Yes

Blockers:
- Problem statement confirmed: Yes
- Scope confirmed: Yes (All compute, cache persistence, and blending parameters confirmed)
- Reproduction confirmed: Yes (Validated via deterministic cache & mock environment models)
- Acceptance criteria drafted: Yes

## 14. Confirmed Requirements Delta (Latest)
- Via cities are reorderable and ordering optimization is central.
- Weather model is bi-level:
	- Level 1 hard constraints: exclude candidates violating temperature thresholds.
	- Level 2 soft preferences: score/rank candidates within allowed weather ranges.
- Hard weather defaults are 90F (max average high) and 24F (min average low), and both are configurable via YAML fields.
- Hills/elevation is a preference objective, including directional climbing differences.
- Start-date support must include both fixed-date and optimize-date planning modes.
- Fixed-date semantics are strict (exact date if provided); optimize-date search window defaults to full year when not provided.
- Output semantics are one best plan plus up to four alternatives by default, with configurable alternative count.

## 15. Practical Test Scenario (Provided)
Scenario name:
- US Capitals Corridor Example

Inputs:
- Start city: Austin, Texas
- Completion city: Washington, DC
- Required via cities (state capitals):
	- Montgomery, Alabama
	- Little Rock, Arkansas
	- Tallahassee, Florida
	- Atlanta, Georgia
	- Topeka, Kansas
	- Frankfort, Kentucky
	- Baton Rouge, Louisiana
	- Jackson, Mississippi
	- Jefferson City, Missouri
	- Raleigh, North Carolina
	- Columbia, South Carolina
	- Nashville, Tennessee
	- Richmond, Virginia
	- Charleston, West Virginia
	- Harrisburg, Pennsylvania

Execution variants:
- Variant A (fixed-date): start_date = February 1
- Variant B (optimize-date): start_date omitted; solver searches across full-year calendar dates

Acceptance checks for this scenario:
- Must include all required via cities.
- Must permit reordered via-city sequence to maximize desirability.
- Must enforce hard weather constraints (default thresholds unless overridden in input).
- Must return one best recommendation and alternatives (default up to 4 unless overridden).

## 16. Verification Plan & Gone2Look4America Benchmark

As a key validation check of the solver's routing desirability, ordering, and scaling capabilities, we will evaluate the actual route taken during the "Gone to look for America" trip.

The website [gone2look4america](https://mvermeulen.org/gone2look4america) documents a real-world six-month bicycle tour starting from Washington, DC, and visiting 26 state capitols in the northern US states, eventually reaching the West Coast.

### 16.1 Scenario Definition: Gone2Look4America Tour
- **Start City**: Washington, DC
- **Completion City**: Olympia, Washington
- **Start Date**: April 29, 2023 (Fixed-date variant for exact comparison)
- **Via Cities (26 Capitols)**:
	- Annapolis, Maryland
	- Dover, Delaware
	- Trenton, New Jersey
	- Hartford, Connecticut
	- Providence, Rhode Island
	- Boston, Massachusetts
	- Concord, New Hampshire
	- Augusta, Maine
	- Montpelier, Vermont
	- Albany, New York
	- Columbus, Ohio
	- Indianapolis, Indiana
	- Springfield, Illinois
	- Lansing, Michigan
	- Madison, Wisconsin
	- St. Paul, Minnesota
	- Des Moines, Iowa
	- Lincoln, Nebraska
	- Pierre, South Dakota
	- Bismarck, North Dakota
	- Cheyenne, Wyoming
	- Denver, Colorado
	- Salt Lake City, Utah
	- Boise, Idaho
	- Salem, Oregon

### 16.2 Comparison and Evaluation Goals
We will run this 26-capitol set through the solver in both fixed-date mode (starting April 29, 2023) and optimize-date mode. 

**Verification Checks**:
1. **Actual vs. Computed Order Comparison**: Compare the actual order chosen by the cyclist (a combination of manual planning, weather safety adjustments, and real-world buffers) with the solver's recommended optimal sequence. Evaluate where and why they differ (e.g., how the solver weights temperature comfort and elevation penalty vs. the manual trip segments).
2. **Desirability Score Evaluation**: Score the actual real-world route using the solver's Stage 2 multi-objective scoring formula and compare it against the solver's top computed recommendations. This helps calibrate the soft weights ($w_{\text{weather}}, w_{\text{distance}}, w_{\text{hills}}$).
3. **Solver Stability and Scaling Check**: With 25 via cities, the search space is large ($25!$ permutations). This serves as a primary benchmark to verify that the **Beam Search / Anytime Best-First Search** solver operates cleanly within the configurable 10-minute timeout budget and produces high-quality, reproducible routing results without performance degradation.

