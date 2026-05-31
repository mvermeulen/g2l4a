# Developer Guide

Welcome to the development guide for `g2l4a`. This document outlines the local run, test, and verification workflow.

## Local Environment Scaffolding

The codebase is built on **Python 3.14+**. Follow these steps to prepare your local virtual environment:

```bash
# 1. Create a clean virtual environment
python3 -m venv .venv

# 2. Activate the virtual environment
source .venv/bin/activate

# 3. Install all dependencies, testing, and linting tools
pip install -r requirements.txt
```


---

## Workspace Directory Map

- **`src/`**: Primary application source code.
  - `domain.py`: Entities, validations, and data models.
  - `config.py`: Precedence loading and recursive merges.
  - `providers.py`: ABC definitions for routing, climate, and elevation.
  - `mocks.py`: High-fidelity deterministic mock implementations for test replays.
  - `metrics.py`: Runtime statistics and timing collection.
  - `solver.py`: Base solver interface.
  - `output.py`: Text formatters and serializations.
- **`config/`**: System default YAML configurations (`defaults.yaml`).
- **`examples/`**: Predefined validation request payloads (e.g., capitals corridor, Gone2Look4America benchmark).
- **`tests/`**: Unit and integration test suites.

---

## Test & Verification Workflow

We use **Pytest** for testing. To keep the import paths clean, run tests from the root directory by specifying `PYTHONPATH=.`:

```bash
# Run the complete test suite
PYTHONPATH=. .venv/bin/pytest

# Run tests in verbose mode with output printing enabled
PYTHONPATH=. .venv/bin/pytest -v -s
```

All new features and optimizations must be verified locally through this test harness before commit, ensuring no regression on our core deterministic fixtures.

---

## Generate Example Reports

Use the report generator module to convert YAML requests in examples/ into markdown reports in reports/:

```bash
# One example config -> one report file
PYTHONPATH=. .venv/bin/python -m src.example_report examples/eastern-capitals-fixed-date-february.yaml

# Explicit output path
PYTHONPATH=. .venv/bin/python -m src.example_report examples/eastern-capitals-fixed-date-march.yaml --output reports/eastern-capitals-fixed-date-march-report.md

# Write JSON only for one example
PYTHONPATH=. .venv/bin/python -m src.example_report examples/eastern-capitals-fixed-date-february.yaml --format json

# Emit both markdown and JSON for one example
PYTHONPATH=. .venv/bin/python -m src.example_report examples/eastern-capitals-fixed-date-february.yaml --format both

# Explicit JSON output path (single example only)
PYTHONPATH=. .venv/bin/python -m src.example_report examples/eastern-capitals-fixed-date-february.yaml --json-output reports/eastern-capitals-fixed-date-february-report.json

# Generate reports for all examples/*.yaml
PYTHONPATH=. .venv/bin/python -m src.example_report --all-examples

# Generate markdown + JSON for all examples/*.yaml
PYTHONPATH=. .venv/bin/python -m src.example_report --all-examples --format both
```

By default, output files are named reports/<example-stem>-report.md.
When --format is json or both, JSON files are named reports/<example-stem>-report.json.
Use --json-output only with --format json or --format both.
