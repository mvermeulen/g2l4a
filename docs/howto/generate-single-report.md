# Generate One Report

## Goal

Build one example report for quick iteration.

## Command

```bash
PYTHONPATH=. python -m src.example_report examples/eastern-capitals-fixed-date-february.yaml
```

## Common Variants

```bash
PYTHONPATH=. python -m src.example_report examples/eastern-capitals-fixed-date-february.yaml --format json
PYTHONPATH=. python -m src.example_report examples/eastern-capitals-fixed-date-february.yaml --format both
PYTHONPATH=. python -m src.example_report examples/eastern-capitals-fixed-date-february.yaml --format all
PYTHONPATH=. python -m src.example_report examples/eastern-capitals-fixed-date-february.yaml --output reports/custom.md
```

## Verify

```bash
ls -l reports/eastern-capitals-fixed-date-february-report.*
ls -1 gpx | grep eastern-capitals-fixed-date-february || true
```

## Notes

- `--format all` is the easiest way to get markdown, JSON, text, and GPX together.
- GPX files are only written when `output.gpx: true` and GraphHopper routing is enabled.