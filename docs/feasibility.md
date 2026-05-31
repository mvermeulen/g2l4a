# Feasibility Engine (Hard Constraints)

This document outlines the validation algorithms, mathematical thresholds, rest day policies, and memoization optimizations managed by the `g2l4a` Feasibility Engine.

---

## 1. Constraint Calculations & Logic

The feasibility engine checks candidate itineraries against system constraints to reject unworkable plans as early in the search process as possible.

### A. Weather Comfort Violations
For each day in the schedule, the engine validates the destination's high temperature $T_{\text{high}}$ against the user's bounds:
$$\min T_{\text{high}} \le T_{\text{high}} \le \max T_{\text{high}}$$

* **Code: `INFEASIBLE_WEATHER_MAX_HIGH`**
  - Triggered if: $T_{\text{high}} > \max T_{\text{high}}$
  - Hint: Suggests adjusting start dates to cooler months or routing around extreme climate zones.
* **Code: `INFEASIBLE_WEATHER_MIN_HIGH`**
  - Triggered if: $T_{\text{high}} < \min T_{\text{high}}$
  - Hint: Suggests scheduling tours in warmer months or lower elevations.

### B. Daily Effort Violations
For each travel day, physical effort metrics (distance $D$ and ascent $A$) are checked:
$$D \le \max D_{\text{day}}$$
$$A \le \max A_{\text{day}}$$

* **Code: `INFEASIBLE_DAILY_MILEAGE`**
  - Triggered if: $D > \max D_{\text{day}}$
  - Hint: Suggests introducing rest days, splitting segments, or adjusting endpoints.
* **Code: `INFEASIBLE_DAILY_ASCENT`**
  - Triggered if: $A > \max A_{\text{day}}$
  - Hint: Suggests mountain bypasses or smaller climbing stages.

---

## 2. Rest Day Logic

To accommodate long-distance bicycle touring realities, the engine supports **Rest Days** (`is_rest_day = True`):
- **Weather checks**: Still apply to rest days (climates remain extreme even when not riding).
- **Effort checks**: Mileage and climbing validations are completely skipped for rest days, allowing riders to recover.

---

## 3. Search Optimization: Precheck Memoization

In beam searches, path branches frequently share segments and dates. Validating these repeatedly introduces massive compute bottlenecks. The `FeasibilityEngine` includes precheck memoization tables:

```python
self._weather_memo: Dict[Tuple[str, str], List[ConstraintViolation]]
self._daily_memo: Dict[Tuple[str, str, str], List[ConstraintViolation]]
```

1. **Weather Memoization**: Keyed by `(city_name, date_iso)`. Weather evaluations are cached globally so that other routes checking the same destination on that day receive instant diagnostic lookups.
2. **Segment Memoization**: Keyed by `(origin_name, dest_name, date_iso)`. Evaluates efforts for specific directional leg segments.

This memoization reduces itinerary constraint checks to $O(1)$ operations during hot search iterations.
