# Implementation Plan (Phased)

This document converts the investigation into an execution plan with explicit quality gates and documentation milestones at each phase.

## 1. Review Summary of Investigation Report

The investigation is strong and implementation-ready. It provides:
- Clear scope and boundaries (routing, weather constraints, scoring, fixed-date and optimize-date modes).
- Confirmed defaults and configuration behavior (hierarchical YAML merge and fallback rules).
- Confirmed compute strategy (beam/anytime search, caching, runtime budget).
- Concrete verification scenarios (US Capitals and Gone2Look4America benchmark).

Implementation risks to actively manage:
- Runtime/quality tradeoff tuning can drift without benchmark guardrails.
- External data provider behavior (rate limits, outages, changing responses) can reduce reproducibility.
- Infeasibility diagnostics must remain precise and user-actionable as complexity grows.

Execution principle:
- Do not advance phases without passing phase verification gates.

## 2. Delivery Strategy

- Incremental vertical slices over big-bang build.
- Deterministic regression mode required for all CI verification.
- Every feature phase includes docs updates before phase closure.
- Maintain one canonical source of defaults and one canonical output contract once stabilized.

## 3. Phased Implementation Plan

## Phase 0 - Foundations and Project Scaffolding
**Status: Completed** ✅

Goal:
- Establish repo structure, baseline tooling, deterministic test harness, and config loading skeleton.

Scope:
- Create core modules:
  - `config` (defaults + user override merge)
  - `domain` (city, leg, itinerary, constraints, scores)
  - `providers` (routing/weather/elevation interfaces)
  - `solver` (search interfaces + placeholders)
  - `output` (human-readable formatter)
- Add deterministic-mode switch and seed plumbing.
- Add timing/metrics collection scaffolding.

Verification gate:
- Unit tests pass for config merge precedence and default resolution.
- Deterministic mode produces byte-identical outputs for fixed fixture + mocked providers.
- Lint/type checks pass.

Documentation milestone:
- `docs/architecture.md`: module boundaries and data flow.
- `docs/configuration.md`: defaults hierarchy and override examples.
- `docs/development.md`: local run/test workflow.

## Phase 1 - Input Contract and Validation
**Status: Completed** ✅

Goal:
- Parse YAML requests into validated internal models with clear error diagnostics.

Scope:
- Implement YAML parser + schema validation for required and optional fields.
- Enforce constraints:
  - city count cap
  - weight validity (non-negative, sum-to-1 tolerance)
  - fixed-date vs optimize-date semantics
- Implement standardized validation error format.

Verification gate:
- Positive fixtures load successfully (provided examples).
- Negative fixtures return stable error codes/messages.
- Tests prove default weather/daily/solver values are applied when omitted.

Documentation milestone:
- `docs/input-schema.md`: field reference, defaults, examples.
- `docs/errors.md`: validation error taxonomy with remediation guidance.

## Phase 2 - Provider Integration (Routing, Weather, Elevation)
**Status: Completed** ✅

Goal:
- Build provider adapters and caching so segment and weather data are fetchable and reproducible.

Scope:
- Implement provider interfaces and one concrete integration path.
- Add L1 in-memory cache and L2 persistent cache (using SQLite).
- Implement profile-aware composite L2 cache keys: `(origin_id, destination_id, routing_engine_version, profile_hash)`, where `profile_hash` covers routing preferences (`avoid_highways`, `avoid_tolls`, `allow_ferries`, `allow_borders`).
- Implement directional route cache keys and weather snapshot versioning.
- Implement **Leg Matrix / Bulk Leg fetcher** to resolve multiple cold leg segments concurrently via bulk APIs or parallel worker pools, avoiding startup latency on large runs.
- Add rate-limit handling and retry/backoff policy.

Verification gate:
- Integration tests pass against mocked and live-sandbox providers.
- Cache hit rate improves repeat-run latency on fixtures.
- Bulk leg queries successfully resolve within timing limits without triggering rate limit blocks.
- Provider outage simulation returns controlled warnings/failures (no silent corruption).

Documentation milestone:
- `docs/providers.md`: provider choices, failover behavior, rate-limit strategy.
- `docs/caching.md`: key design, invalidation, TTLs, reproducibility rules.

## Phase 3 - Feasibility Engine (Hard Constraints)
**Status: Completed** ✅

Goal:
- Reject infeasible candidates early and return actionable diagnostics.

Scope:
- Implement hard weather checks and daily-cap feasibility checks.
- Implement precheck memoization for repeated segment/date evaluations.
- Define a standardized `ConstraintViolation` data contract and structured schema list in the output:
  - Fields: `code` (e.g., INFEASIBLE_WEATHER_MAX_HIGH), `location`, `date`, `observed_value`, `threshold_limit`, and `remediation_hint`.
- Implement standardized infeasibility reason codes and detailed breakdown output.

Verification gate:
- Returned plans never violate hard constraints.
- Infeasible scenarios fail fast with structured city/leg/date/value/threshold details.
- Regression tests cover all confirmed blocking reason codes.

Documentation milestone:
- `docs/feasibility.md`: hard constraint logic and fail-fast policy.
- `docs/diagnostics.md`: reason codes, warning vs blocking semantics.

## Phase 4 - Scoring and Ranking (Soft Objectives)

Goal:
- Implement Stage 2 desirability scoring and stable ranking behavior.

Scope:
- Implement normalized distance/hills scores and weather preference score.
- Implement weighted total score and tie-break policy.
- Add configurable alternatives count behavior.

Verification gate:
- Ranking order is monotonic by total score.
- Sensitivity tests behave as expected under controlled weight changes.
- Output always includes one best result and up to configured alternatives.

Documentation milestone:
- `docs/scoring.md`: formulas, normalization, defaults, examples.
- `docs/tuning.md`: practical guidance for adjusting weights safely.

## Phase 5 - Search Engine and Runtime Budgeting

Goal:
- Produce high-quality routes within runtime budgets using anytime/beam strategy.

Scope:
- Implement **Warm-Start Seeding Heuristic**: run a cheap constructive heuristic first (e.g., greedy nearest-neighbor TSP or 2-opt search) on the distance/ascent leg matrix under monthly averages to set tight bounds and seed the beam queue.
- Implement two-phase search:
  - cheap candidate filtering
  - full evaluation of top-K candidates
- Implement beam search / anytime best-first behavior.
- Add timeout handling and best-so-far return semantics.
- Add concurrency controls and worker pool tuning.

Verification gate:
- US Capitals fixtures complete within configured time budget.
- Gone2Look4America benchmark completes within budget with reproducible deterministic output.
- Warm-start heuristic seeds valid high-quality bounds instantly on high-capitol fixtures.
- Performance metrics captured: eval/sec, prune counts, cache hit rate, best-score-over-time.

Documentation milestone:
- `docs/solver.md`: search algorithm behavior and runtime controls.
- `docs/performance.md`: benchmark methodology, baseline, and acceptance thresholds.

## Phase 6 - Output Contract and UX Readability

Goal:
- Finalize human-readable output contract and ensure explainability.

Scope:
- Define and lock output schema/format for recommendations.
- Include route order, dates, weather context, and score breakdown.
- Include warnings/diagnostics in a consistent structure.

Verification gate:
- Golden-file tests for output formatting consistency.
- Users can identify why route A outranked route B from output alone.
- Diagnostics remain complete and readable in both feasible and infeasible runs.

Documentation milestone:
- `docs/output-contract.md`: final output fields and examples.
- `docs/user-guide.md`: interpret results, tune inputs, handle infeasible cases.

## Phase 7 - Hardening, CI/CD, and Release Readiness

Goal:
- Prepare for stable release with confidence in correctness, performance, and operations.

Scope:
- Add CI gates for unit/integration/regression/performance smoke tests.
- Add deterministic replay workflow for incidents.
- Finalize run metadata/provenance recording.
- Implement **Gone2Look4America Quality Calibration Gate**: score the cyclist's actual real-world route using the solver's Stage 2 soft scoring formulas and compare it directly to computed recommendations to validate and tune weights ($w_{\text{weather}}, w_{\text{distance}}, w_{\text{hills}}$).
- Conduct release candidate validation on benchmark fixture suite.

Verification gate:
- All required acceptance tests (from investigation) pass in CI.
- Quality calibration gate successfully establishes soft weight sensitivity boundaries on real-world benchmark data.
- Deterministic replay reproduces prior ranked outputs for snapshot data.
- No open P0/P1 defects; release checklist complete.

Documentation milestone:
- `docs/release-checklist.md`: release criteria and rollback plan.
- `docs/operations.md`: runtime monitoring, provider health checks, incident response.
- `CHANGELOG.md`: v1 release notes.

## 4. Cross-Phase Verification Matrix

Required in every phase before closure:
- Correctness: tests for new logic and no regression on existing fixtures.
- Reproducibility: deterministic mode regression run updated and passing.
- Performance: no unapproved degradation against tracked baseline.
- Diagnostics: errors/warnings are explicit and user-actionable.
- Documentation: phase docs merged in the same change window as code.

## 5. Suggested Milestones and Exit Criteria

Milestone A (Phases 0-2 complete):
- System can parse validated input and fetch/cache provider data reliably.

Milestone B (Phases 3-4 complete):
- Feasible candidate filtering and scoring/ranking are correct and test-covered.

Milestone C (Phase 5 complete):
- Solver returns high-quality best-so-far recommendations under runtime budgets.

Milestone D (Phases 6-7 complete):
- Output contract is stable, docs are complete, CI/release gates are green.

## 6. Immediate Next Actions

1. Implement Phases 0 and 1 as one initial delivery slice.
2. Add fixture-driven tests from provided example YAML files as baseline regression assets.
3. Establish benchmark dashboard artifact (runtime, quality, reproducibility metrics) before search optimization work starts.
