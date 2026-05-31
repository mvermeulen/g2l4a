# Changelog

All notable changes to the `g2l4a` multi-objective route optimizer project will be documented in this file.

## [1.0.0-rc1] - 2026-05-30

### Added
- **Calibration Engine**: Implemented Gone2Look4America calibration benchmarking suite in `src/calibration.py` and sequential route scoring engine.
- **Sensitivity Analysis**: Enabled automated soft-objective scoring sensitivity analysis varying weights by +/- 0.10.
- **Verification Gates**: Added automated calibration and scale regression tests in `tests/test_phase7.py`.
- **Output Formatter Contract**: Created `format_recommendations_markdown` (with GFM multi-itinerary comparisons and collapsible daily schedules) and `serialize_recommendations_json` formatting interfaces.
- **Anytime Solver Engine**: Implemented `BeamSearchSolver` with Nearest-Neighbor constructive TSP warm-starts, polynomial search constraints, fail-fast early pruning, and dynamic runtime budgeting.
- **Bulk Segment Fetcher**: Integrated parallel composite execution layers with multi-threaded rate-limited composite matrices caching.
- **Persistent Cache Manager**: Designed threat-safe SQLite L2 caching backing L1 execution memory layers.
- **Hierarchical Config precedence**: Established recursive deep-merging configurations supporting custom user profiles.

### Documented
- Release checklist, rollout plans, and verification steps in `docs/release-checklist.md`.
- Maintenance, caching operations, retry policies, and performance monitoring telemetry in `docs/operations.md`.
- Output formatting guides and schemas in `docs/output-contract.md`.
- Result interpretation, parameter adjustment, and error handling in `docs/user-guide.md`.
