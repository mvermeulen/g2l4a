# Run Unattended Regeneration

## Goal

Regenerate all example outputs in the background without blocking the terminal.

## Prerequisites

- GraphHopper is running at `http://localhost:8989`
- You are in the repository root

## Start It

```bash
nohup env PYTHONUNBUFFERED=1 PYTHONPATH=. python -u -m src.example_report --all-examples --format all > reports/regenerate-reports.log 2>&1 < /dev/null &
```

## Monitor It

```bash
pgrep -af "python -u -m src.example_report --all-examples --format all"
tail -f reports/regenerate-reports.log
```

## Stop It

```bash
pkill -f "python -u -m src.example_report --all-examples --format all"
```

## Verify

```bash
ls -1 reports | sort | tail
ls -1 gpx | sort
```

## Notes

- Use `--format all` to generate markdown, JSON, text, and GPX together.
- GPX export stops after `output.gpx_timeout_seconds` so the run does not hang on a slow route export.