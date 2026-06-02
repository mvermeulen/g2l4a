# Run Tests

## Goal

Check the code after a change.

## Quick Commands

```bash
PYTHONPATH=. pytest -q tests/test_phase8.py
PYTHONPATH=. pytest -q tests/test_phase8.py tests/test_phase0.py tests/test_phase6.py
```

## Full Suite

```bash
PYTHONPATH=. pytest -q
```

## Verify

- The command should exit with code 0.
- If a test fails, fix the touched slice and rerun the same command.

## Notes

- Keep `PYTHONPATH=.` so local imports resolve correctly.
- Use targeted tests first, then widen to the full suite.