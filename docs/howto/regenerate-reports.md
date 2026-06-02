# Regenerate All Reports

## Goal

Rebuild every example report and, when enabled, its GPX file.

## Prerequisites

- GraphHopper is running at `http://localhost:8989`
- You are in the repository root

## Command

```bash
PYTHONUNBUFFERED=1 PYTHONPATH=. python -u -m src.example_report --all-examples --format all
```

## What It Writes

- `reports/<example-stem>-report.md`
- `reports/<example-stem>-report.json`
- `reports/<example-stem>-report.txt`
- `gpx/<example-stem>--<start-city>-to-<end-city>.gpx` when `output.gpx: true`

## Verify

```bash
ls -1 reports | sort | tail
ls -1 gpx | sort
```

## Notes

- GPX export is skipped automatically if it exceeds `output.gpx_timeout_seconds`.
- Use this command for unattended regeneration jobs.