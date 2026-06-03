# Check and Configure Meteostat Climate Provider

## Goal

Configure and build the local SQLite cache database with historical Meteostat climatology observations. This allows the solver to run offline using daily temperature averages derived from a 25-year observations range (2001–2025).

## Prerequisites

Install the `meteostat` and `pandas` Python packages in your virtual environment:

```bash
pip install meteostat pandas
```

*Note: Meteostat does not require any API keys.*

## Pre-fetch Climatology Data

Pre-populate the local SQLite database cache (`.g2l4a_cache.db`) for all registered cities to enable fully offline execution:

```bash
python scripts/build_meteostat_cache.py
```

To force download and update existing entries:

```bash
python scripts/build_meteostat_cache.py --force
```

## Configure Weather Provider

To configure a tour scenario to use Meteostat climatology observations, edit your scenario YAML config in the `examples/` directory and set the `weather_provider` name to `meteostat`:

```yaml
weather_provider:
  name: meteostat
```

## Run Scenario

Once configured, run the report generator command:

```bash
PYTHONPATH=. python src/example_report.py examples/dixie-fixed-date.yaml
```

If cached, it will execute instantly and completely offline without making external HTTP requests.
