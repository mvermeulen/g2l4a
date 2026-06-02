# g2l4a

`g2l4a` is a long-distance bicycle tour route optimizer. It builds itinerary recommendations from YAML example files, scores them against weather, distance, and hills, and can export markdown, JSON, text tables, and GPX route files.

## Release Note

`v0.1.0` is the initial public release. It includes the core solver, GraphHopper-backed routing, scored itinerary reports, GPX export, calibration and regression test coverage, and the docs/HOWTO workflow for regenerating outputs locally.

## What This Repo Contains

- `src/`: solver, routing, scoring, validation, and output code
- `config/`: system defaults, including output and routing defaults
- `examples/`: scenario YAML files used to generate reports
- `reports/`: generated markdown, JSON, and text outputs
- `gpx/`: generated GPX route files when GPX output is enabled
- `docs/`: developer, operations, configuration, and user guides
- `docs/howto/`: short task recipes for common local workflows
- `tests/`: pytest coverage for report generation, scoring, and solver behavior

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If you are running against GraphHopper-backed routing, make sure the local service is ready:

```bash
docker-compose -f docker-compose.graphhopper.yml up -d
curl -fsS http://localhost:8989/info | head -c 300 && echo
```

## Common Commands

Generate one report:

```bash
PYTHONPATH=. python -m src.example_report examples/eastern-capitals-fixed-date-february.yaml
```

Generate all examples, including markdown, JSON, text, and GPX outputs:

```bash
PYTHONUNBUFFERED=1 PYTHONPATH=. python -u -m src.example_report --all-examples --format all
```

Run tests:

```bash
PYTHONPATH=. pytest -q
```

## Output Files

- Markdown reports are written to `reports/<example-stem>-report.md`
- JSON reports are written to `reports/<example-stem>-report.json`
- Text reports are written to `reports/<example-stem>-report.txt`
- GPX files are written to `gpx/<example-stem>--<start-city>-to-<end-city>.gpx` when `output.gpx: true`

GPX export is skipped automatically if it runs longer than `output.gpx_timeout_seconds`, so report generation can continue.

## Documentation

- [Developer guide](docs/development.md)
- [Configuration guide](docs/configuration.md)
- [Operations manual](docs/operations.md)
- [User guide](docs/user-guide.md)
- [HOWTO index](docs/howto/README.md)

## Notes

- Example reports assume GraphHopper is available when `routing_provider.name: graphhopper` is configured.
- Generated artifacts in `reports/` and `gpx/` are meant to be recreated locally and kept out of version control where appropriate.