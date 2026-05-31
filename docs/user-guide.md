# User Manual & Troubleshooting Recipes

Welcome to the user manual for `g2l4a`, the long-distance bicycle tour route optimizer. This guide provides a comprehensive overview of input setups, weights tuning, and diagnostic troubleshooting steps.

---

## 1. Structuring Request YAML Payloads

Optimizer requests are parsed using YAML. You can configure tours in either **fixed-date** or **optimize-date** modes:

### A. Fixed-Date Mode Example
*Runs weather comfort evaluations for a specific departure date.*
```yaml
start_city: "Montgomery, Alabama"
completion_city: "Boise, Idaho"
via_cities:
  - "Atlanta, Georgia"
  - "Portland, Oregon"
start_date: "2026-06-01"  # Fixed-date YYYY-MM-DD
```

### B. Optimize-Date Mode Example
*Omit the `start_date` parameter to let the solver search across 12 month-start options to determine which month offers the peak desirability score.*
```yaml
start_city: "Montgomery, Alabama"
completion_city: "Boise, Idaho"
via_cities:
  - "Atlanta, Georgia"
  - "Portland, Oregon"
# Omitted start_date triggers optimize-date search!
```

---

## 2. Calibrating Constraints and Weights

Fine-tune the solver's limits by declaring daily effort caps or desirability weights under `defaults` overrides:

```yaml
daily_constraints:
  max_miles_per_day: 100.0     # Maximum travel distance allowed in a single day
  max_climb_ft_per_day: 6000.0  # Maximum climbing ascent allowed in a single day

scoring:
  weights:
    weather: 0.50   # 50% priority on temperate weather comfort
    distance: 0.30  # 30% priority on minimizing excess detours
    hills: 0.20     # 20% priority on avoiding steep hill climbs
```

---

## 3. Troubleshooting Infeasible Results

If the optimizer returns itineraries marked as `is_feasible: False` (or outputs warnings), look at `violations` or `Constraint Violations` inside the detailed summary:

### Common Violations & Remediation Recipes

#### 1. `INFEASIBLE_DAILY_MILEAGE`
* **Why**: A leg segment exceeds your `max_miles_per_day` limit.
* **Fix**: Increase the `max_miles_per_day` cap in your request, introduce rest days in your schedule, or select endpoints closer together.

#### 2. `INFEASIBLE_WEATHER_MAX_HIGH` / `INFEASIBLE_WEATHER_MIN_LOW`
* **Why**: The target date high/low temperatures violate comfort bounds (e.g. excessive daytime heat or overnight cold).
* **Fix**: Change your `start_date` to a milder travel season, broaden the comfort temperature boundaries (`max_avg_high_f` or `min_avg_low_f`), or route around extreme climate zones.

#### 3. `INFEASIBLE_DAILY_ASCENT`
* **Why**: A segment climb exceeds your `max_climb_ft_per_day` cap.
* **Fix**: Bypasses mountainous segments or increase your daily ascent limit.
