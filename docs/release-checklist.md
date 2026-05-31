# Release Checklist (v1.0.0-rc1)

This checklist specifies the exit criteria, quality gates, and rollback plans required for the official production release of the `g2l4a` bicycle tour route optimizer.

## 1. Pre-Release Quality Gates

- [x] **Linter Compliance**: Zero linter errors or warnings when running `pyrefly check src/`.
- [x] **Test Suite Coverage**: Enforce a strict minimum of **90%** coverage across the codebase. Current actual repository coverage: **94%**.
- [x] **Deterministic Replay Guarantee**: Multi-itinerary search results must produce byte-identical sequences, schedules, and scores on repeated solver seeds:
  ```bash
  PYTHONPATH=. .venv/bin/pytest tests/test_phase5.py -k test_solver_deterministic_replay
  ```
- [x] **Gone2Look4America Calibration**: The soft desirability scoring and anytime beam search solver must validate successfully against the historical G2L4A benchmark and produce `reports/calibration-report.md`:
  ```bash
  PYTHONPATH=. .venv/bin/python -m src.calibration
  ```

## 2. Release Steps

1. **Tag Repository**: Create and push a semver release tag:
   ```bash
   git tag -a v1.0.0-rc1 -m "Release Candidate 1 for g2l4a bicycle tour optimizer"
   git push origin v1.0.0-rc1
   ```
2. **Database Migration**: Ensure the standard cache schema is synchronized:
   - Run unit tests to auto-generate the static SQL schema on clean systems.
3. **Verify Documentation**: Confirm that all user and architecture guides under `docs/` are formatted and accurate.

## 3. Post-Deployment Smoke Tests

- Run the Capitals optimize-date variant using the workspace runner or tests:
  ```bash
  PYTHONPATH=. .venv/bin/pytest tests/test_phase1.py -k test_positive_fixtures_loading
  ```
- Verify that standard markdown formatters and JSON payloads are cleanly generated inside output pathways.

## 4. Emergency Rollback Plan

In the event of a blocking runtime error or severe regression in production:
1. **Revert Branch**: Reset the `main` branch to the last known stable tag:
   ```bash
   git checkout tags/v0.9.0 -b stable-hotfix
   ```
2. **Clear SQLite L2 Cache**: If the failure is caused by L2 cache schema corruption, run the cache clean utility or delete the `.g2l4a_cache.db` file to trigger safe fallbacks.
3. **Rollback Release Tag**: Force-delete the failing remote release tag:
   ```bash
   git tag -d v1.0.0-rc1
   git push --delete origin v1.0.0-rc1
   ```
