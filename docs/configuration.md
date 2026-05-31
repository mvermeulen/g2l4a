# Configuration Guide

The `g2l4a` solver uses a hierarchical deep-merge configuration system. This allows global defaults to be maintained centrally, while individual requests can selectively override nested parameters without repeating unchanged defaults.

## Configuration Precedence

When the solver runs, the configuration is resolved in the following priority (highest precedence first):

1. **User Request YAML**: Constraints or preferences supplied directly in the API or run payload.
2. **System Defaults YAML**: Central settings (loaded from `config/defaults.yaml`) maintained by system administrators.
3. **Hardcoded Fallbacks**: Safety defaults embedded directly in the solver source code as a fail-safe.

---

## Recursive Deep-Merging Rules

Flat dictionaries are typically overwritten entirely. However, nested options (like scoring weights and constraints) are merged recursively key-by-key.

For example, if the System Default defines:
```yaml
scoring:
  weights:
    weather: 0.45
    distance: 0.30
    hills: 0.25
```

And the User Request overrides only:
```yaml
scoring:
  weights:
    weather: 0.60
```

The resulting effective configuration is:
```yaml
scoring:
  weights:
    weather: 0.60    # Overridden by user
    distance: 0.30   # Preserved from system defaults
    hills: 0.10      # Recalculated / validated to sum to 1.0
```

---

## Schema Reference & Default Values

Below is the absolute default schema used by the system when a setting is omitted in both user and system configs:

| Category | Parameter | Type | Default Value | Description |
|---|---|---|---|---|
| **Weather** | `max_avg_high_f` | float | `90.0` | Maximum average high temperature allowed for a city. |
| | `min_avg_low_f` | float | `24.0` | Minimum average low temperature allowed for a city. |
| **Daily limits** | `max_miles_per_day`| float | `70.0` | Absolute daily distance mileage cap. |
| | `max_climb_ft_per_day`| float | `5000.0` | Absolute daily climbing ascent cap. |
| **Duration** | `max_total_days` | int/null | `null` | Optional total trip duration limit (no cap by default). |
| **Solver** | `max_total_cities` | int | `50` | Maximum cities permitted in a single plan request. |
| | `max_search_minutes` | float | `10.0` | Runtime timeout budget for solver search. |
| **Scoring** | `weights.weather` | float | `0.45` | Weight for weather desirability (must sum to 1). |
| | `weights.distance` | float | `0.30` | Weight for shortest route (must sum to 1). |
| | `weights.hills` | float | `0.25` | Weight for lower elevation gain (must sum to 1). |
| **Routing** | `avoid_highways` | bool | `true` | Mirror 'avoid highways' preference to exclude freeways. |
| | `avoid_tolls` | bool | `true` | Disfavor toll roads by default to favor bike legal roads. |
| | `allow_ferries` | bool | `true` | Permit necessary ferry connections when generating routes. |
| | `allow_borders` | bool | `true` | Permit international border segments. |
