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

### 8.2 Tentative Decisions (Finalize Later)
1. Routing provider strategy (tentative):
	- MVP provider: hosted OpenRouteService for quick startup.
	- Production target: self-hosted GraphHopper (or Valhalla) for reliability and quota independence.
	- Status: Tentative now, finalize later.
	- Finalization criteria:
		- bike-routing quality on fixture scenarios,
		- acceptable latency and uptime expectations,
		- operational complexity and maintenance burden.

2. Weather-data strategy (tentative, free-first):
	- Baseline climatology source: NOAA/NCEI (US-focused) or Meteostat historical normals for seasonality and optimize-date scoring.
	- Forecast overlay source: Open-Meteo for near-term fixed-date planning adjustments.
	- Combination approach:
		- far-future or unspecified date optimization relies primarily on climatology,
		- near-term fixed-date planning increases forecast influence.
	- Status: Tentative now, finalize later.
	- Finalization criteria:
		- coverage completeness for required cities/routes,
		- consistency of metric definitions (avg highs/lows) across sources,
		- API reliability/rate limits and ease of integration,
		- reproducibility support via data snapshot pinning for tests.

3. Elevation-data strategy (tentative):
	- Primary source: use elevation/ascent metrics returned by the selected routing provider.
	- Fallback: if elevation is unavailable or low quality for a segment, use a DEM-based source for recomputation.
	- Operational rule: prefer one canonical ascent metric pipeline per run to avoid mixed-source scoring artifacts.
	- Status: Tentative now, finalize later.
	- Finalization criteria:
		- coverage across all fixture routes,
		- consistency of total ascent values between repeated runs,
		- acceptable correlation with sampled ground-truth checks,
		- latency impact within runtime targets.

4. Route safety/legality policy (confirmed):
	- Default routing preference should mirror "avoid highways" behavior.
	- Exclude freeway/interstate segments and other non-bicycle-legal roads from candidate generation.
	- International border crossings and ferry crossings are allowed.
	- Avoid toll roads by default.
	- Objective is a rough costed planning recommendation; exact final roads may be refined manually outside the tool.
	- Status: Confirmed.

5. Distance/climb/duration policy (confirmed):
	- Daily limits are configurable with defaults:
		- max miles per day: 80
		- max climb per day: 5000 ft
	- No hard maximum total trip duration for v1 (effectively "as long as it takes").
	- Planner continues to optimize for route desirability, including shorter overall distance.
	- Status: Confirmed.

6. Scale/runtime policy (confirmed):
	- Maximum cities per request: 50 (configurable).
	- Solver runtime budget default: 10 minutes (configurable timeout).
	- Solver should return best-found recommendations within the runtime budget.
	- Status: Confirmed.

7. Infeasibility handling policy (confirmed):
	- If no feasible route satisfies hard weather constraints, fail fast.
	- Do not auto-relax hard constraints.
	- Return clear diagnostics that identify likely blocking constraints so users can choose what to relax.
	- Status: Confirmed.

8. Trip structure policy (confirmed):
	- Treat each plan as one overall staged multi-day trip.
	- Apply daily caps per stage/day (distance and climbing).
	- No hard max total duration; trip length emerges from route geometry plus daily constraints.
	- Status: Confirmed.

9. Scoring semantics policy (confirmed):
	- Weather preference scoring within feasible bounds is linear for v1.
	- Hill penalty metric uses total ascent only for v1.
	- Distance metric uses route mileage for v1.
	- Status: Confirmed.

10. Output evolution policy (confirmed):
	- Defer strict output schema decisions until example outputs are produced.
	- V1 output must be human-readable and include ordered cities, planned dates, and average weather context in tabular form where practical.
	- Uncertainty indicators are not required for v1.
	- Status: Confirmed.

11. Schema/versioning and error-handling policy (confirmed):
	- Backward-compatible YAML versioning is not required for v1.
	- Do not block on schema-version architecture upfront; evolve format pragmatically.
	- Work through validation/runtime errors as they appear during iterative testing.
	- Status: Confirmed.

### 8.3 Decision Needed Now
1. Scoring weights/profile lock for v1:
	- Decision needed:
		- whether to launch with one fixed default profile only, or support multiple named profiles in v1.
		- whether user-specified custom weights are allowed in v1.
	- Proposed default if undecided:
		- single fixed default profile in v1,
		- weights: weather 0.45, distance 0.30, hills 0.25,
		- allow custom weights only if non-negative and sum to 1.
	- Impact if unresolved:
		- ranking behavior remains ambiguous and can cause implementation churn.

2. Weather data blending and resolution rule for v1:
	- Decision needed:
		- exact rule for climatology vs forecast blending by planning horizon,
		- required data granularity (city-level monthly/daily vs segment-level),
		- fallback behavior when forecast provider is unavailable.
	- Proposed default if undecided:
		- use city-level monthly normals for optimize-date and long-horizon planning,
		- use forecast overlay only for near-term fixed-date planning,
		- if forecast unavailable, fallback to climatology and emit a warning.
	- Impact if unresolved:
		- feasibility/ranking behavior may vary unpredictably and reduce reproducibility.

Output rule (confirmed):
- Return one best recommendation plus alternatives.
- Default alternatives count: up to 4.
- Alternatives count must be configurable in YAML input, with default applied when omitted.

Start-date rule (confirmed):
- input.start_date present: enforce exact start date.
- input.start_date absent: optimize across full-year date domain.

Proposed YAML defaults (confirmed):
- weather_constraints.max_avg_high_f: 90
- weather_constraints.min_avg_high_f: 32
- Behavior: if omitted in input, solver uses defaults above.
- daily_constraints.max_miles_per_day: 80
- daily_constraints.max_climb_ft_per_day: 5000
- duration_constraints.max_total_days: null (no hard cap)
- solver_constraints.max_total_cities: 50
- solver_constraints.max_search_minutes: 10

Hierarchical YAML defaults model (confirmed):
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
		min_avg_high_f: 32

	daily_constraints:
		max_miles_per_day: 80
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

## 9. Scoring Method (Draft)
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

### 9.1 Acceptance Criteria for Scoring (Pass/Fail)
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

## 10. Recommended Next Investigation Steps
1. Finalize objective scoring weights (weather vs distance vs hills) and whether profiles are user-configurable.
2. Finalize weather data source strategy for v1 (historical normals, forecast, or hybrid by lead time).
3. Lock YAML schema fields for constraints, preferences, and output configuration.
4. Convert the Austin to Washington, DC scenario into executable test fixtures for both fixed-date and optimize-date modes.

## 11. Decision Gate (Before Development)
Ready for implementation: No

Blockers:
- Problem statement confirmed: Yes
- Scope confirmed: Mostly (pending weather data-source decision and scoring weights)
- Reproduction confirmed: No
- Acceptance criteria drafted: Yes

## 12. Confirmed Requirements Delta (Latest)
- Via cities are reorderable and ordering optimization is central.
- Weather model is bi-level:
	- Level 1 hard constraints: exclude candidates violating temperature thresholds.
	- Level 2 soft preferences: score/rank candidates within allowed weather ranges.
- Hard weather defaults are 90F (max average high) and 32F (min average high), and both are configurable via YAML fields.
- Hills/elevation is a preference objective, including directional climbing differences.
- Start-date support must include both fixed-date and optimize-date planning modes.
- Fixed-date semantics are strict (exact date if provided); optimize-date search window defaults to full year when not provided.
- Output semantics are one best plan plus up to four alternatives by default, with configurable alternative count.

## 13. Practical Test Scenario (Provided)
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
