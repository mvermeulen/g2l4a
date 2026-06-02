# Generate Segment-Level GPX Files

## Goal

Generate segment-level GPX files for all unique routes (legs) found in generated JSON reports.

## Prerequisites

- GraphHopper service must be running locally (default: `http://localhost:8989`).
- JSON reports must be present in the `reports/` directory.

## Run Script

Run the GPX generator script:

```bash
python scripts/generate_segment_gpx.py
```

## Verify Outputs

List the files in `gpx/segment/` to verify they exist:

```bash
ls -1 gpx/segment | head
```

## CLI Configuration Options

You can customize execution with flags:

- `--reports-dir`: Custom reports path (default: `reports`)
- `--gpx-dir`: Custom GPX destination path (default: `gpx/segment`)
- `--base-url`: GraphHopper server endpoint (default: `http://localhost:8989`)
- `--profile`: Routing engine profile (default: `bike`)
- `--force`: Force generation of all GPX files, bypassing timestamp checks

Example:

```bash
python scripts/generate_segment_gpx.py --force --profile hike
```
