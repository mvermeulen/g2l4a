# Check GraphHopper and GPX Output

## Goal

Make sure GraphHopper is ready and GPX output is working.

## Start GraphHopper

```bash
docker-compose -f docker-compose.graphhopper.yml up -d
curl -fsS http://localhost:8989/info | head -c 300 && echo
```

## Run One GPX-Enabled Example

```bash
PYTHONUNBUFFERED=1 PYTHONPATH=. python -u -m src.example_report examples/heartland-fixed-date.yaml --format md
```

## Verify

```bash
ls -1 gpx | sort
```

## Notes

- GPX files are written into `gpx/` and ignored by git.
- If GPX export takes too long, the generator skips it after `output.gpx_timeout_seconds`.