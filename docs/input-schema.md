# Input Schema Contract Reference

This document serves as the canonical contract reference for planning request payloads. The planning solver accepts request payloads in YAML or native Python dictionaries.

---

## 📋 Field Reference

| Path | Type | Required? | Default Value | Description |
|---|---|---|---|---|
| `start_city` | string | **Yes** | — | Name of the starting city. Must match recognized names in the [Geocoding Registry](#geocoding-registry). |
| `completion_city` | string | **Yes** | — | Name of the final completion city. Must match recognized names. |
| `via_cities` | list[string] | No | `[]` | List of state capitals that must be visited along the route. |
| `start_date` | string / date | No | `null` | Start date in `YYYY-MM-DD` format. If omitted, `optimize-date` mode is activated. |
| `weather_constraints.max_avg_high_f` | float | No | `90.0` | Maximum average high temperature allowed (hard constraint). |
| `weather_constraints.min_avg_low_f` | float | No | `24.0` | Minimum average low temperature allowed (hard constraint). |
| `daily_constraints.max_miles_per_day` | float | No | `70.0` | Maximum allowed daily mileage cap. |
| `daily_constraints.max_climb_ft_per_day`| float | No | `5000.0` | Maximum allowed daily climbing ascent cap (feet). |
| `solver_constraints.max_total_cities` | int | No | `50` | Maximum cities (via + start + completion) permitted in a single request. |
| `solver_constraints.max_search_minutes` | float | No | `10.0` | Search budget timeout limit in minutes. |
| `scoring.weights.weather` | float | No | `0.45` | Weight for weather desirability (linear score). |
| `scoring.weights.distance` | float | No | `0.30` | Weight for shortest route mileage score. |
| `scoring.weights.hills` | float | No | `0.25` | Weight for lower elevation ascent score. |
| `routing_preferences.avoid_highways` | bool | No | `true` | Mirror 'avoid highways' routing behavior. |
| `routing_preferences.avoid_tolls` | bool | No | `true` | Disfavor toll roads to keep routes bicycle legal. |

---

## 🗺️ Geocoding Registry

To support stable, rapid, and offline-reliable testing, the solver integrates a built-in coordinates registry for all 50 U.S. State Capitals and major transition cities. Examples include:
*   `"Austin, Texas"`: `(30.2672, -97.7431)`
*   `"Washington, DC"`: `(38.9072, -77.0369)`
*   `"Olympia, Washington"`: `(47.0379, -122.9007)`

*Any city name string passed in a request must resolve case-insensitively to a key in the geocoding registry (e.g. `"austin, texas"` or `"Denver, Colorado"`).*

---

## 💡 Valid Request Examples

### 1. Fixed-Date Mode Request
```yaml
scenario_name: US Capitals Corridor Example (Fixed Date)
start_city: Austin, Texas
completion_city: Washington, DC
start_date: "2026-02-01"

via_cities:
  - Montgomery, Alabama
  - Little Rock, Arkansas
  - Tallahassee, Florida
  - Atlanta, Georgia
  - Topeka, Kansas

weather_constraints:
  max_avg_high_f: 90
  min_avg_low_f: 24
```

### 2. Optimize-Date Mode Request
```yaml
scenario_name: Gone2Look4America Benchmark (Optimize Date)
start_city: Washington, DC
completion_city: Olympia, Washington

via_cities:
  - Annapolis, Maryland
  - Dover, Delaware
  - Trenton, New Jersey
  - Hartford, Connecticut
  - Providence, Rhode Island
```
