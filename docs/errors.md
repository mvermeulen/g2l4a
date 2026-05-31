# Error Taxonomy & Diagnostics Guide

The `g2l4a` solver implements an upfront parser validation engine that fails fast and outputs clear, structured exception diagnostics. All user-input issues are raised under the `ValidationError` exception class.

---

## 🛑 Standard Error Codes

Below is the stable taxonomy of validation error codes returned by the solver, along with their root causes and actionable remediation hints:

| Error Code | Location Field | Root Cause | Actionable Remediation Hint |
|---|---|---|---|
| **`MISSING_START_CITY`** | `start_city` | The starting city field is omitted or empty. | Ensure `start_city` is provided (e.g. `start_city: Austin, Texas`). |
| **`MISSING_COMPLETION_CITY`** | `completion_city` | The completion city field is omitted or empty. | Ensure `completion_city` is provided (e.g. `completion_city: Washington, DC`). |
| **`INVALID_CITY`** | Affected city string | The city name cannot be resolved in the geocoding registry. | Verify the spelling matches a recognized U.S. State Capital or city in the [Geocoding Registry](input-schema.md#geocoding-registry). |
| **`INVALID_VIA_CITIES`** | `via_cities` | The `via_cities` block is not a list. | Format `via_cities` as a YAML sequence list of string names. |
| **`INVALID_DATE`** | `start_date` | The provided start date is not in `YYYY-MM-DD` format. | Format the start date exactly as `YYYY-MM-DD` (e.g. `start_date: "2026-06-15"`). |
| **`CITY_COUNT_EXCEEDED`** | `via_cities` | Total requested cities exceeds `max_total_cities`. | Reduce the number of via capitals or raise `solver_constraints.max_total_cities` in overrides. |
| **`INVALID_SCORING_WEIGHTS`** | `scoring.weights` | Desirability weights are negative or do not sum to 1.0. | Ensure all weights are `>= 0.0` and `weather + distance + hills` sums to exactly `1.0`. |
| **`INVALID_WEATHER_RANGE`** | `weather_constraints` | The `max_avg_high_f` is less than `min_avg_high_f`. | Adjust temperature bounds so maximum high is greater than minimum high. |
| **`INVALID_DAILY_LIMIT`** | `daily_constraints` | The daily mileage or climbing cap is zero or negative. | Set `max_miles_per_day` and `max_climb_ft_per_day` to positive values. |
| **`FILE_NOT_FOUND`** | file path | The request file path does not exist. | Double check that the requested YAML file path is correct. |
| **`YAML_PARSE_ERROR`** | file payload | The file is syntactically invalid YAML. | Run your request through a YAML linter to fix formatting issues (such as mismatched list brackets). |
| **`EMPTY_REQUEST`** | file payload | The request file contains no data. | Provide a valid, structured planning request payload. |

---

## 📊 Structured Error Response Example

When the parser fails during a dictionary execution, it raises a `ValidationError` which can serialize to a clean JSON/YAML dictionary:

```json
{
  "code": "INVALID_SCORING_WEIGHTS",
  "message": "Scoring weights are invalid: Weights must sum to 1.0. Got weather=0.5, distance=0.5, hills=0.5 (sum=1.5)",
  "location": "scoring.weights"
}
```

This ensures machine-readable integration for client dashboards or clear console logging for manual planners.
