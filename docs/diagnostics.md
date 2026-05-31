# Diagnostics & Violation Codes Reference

This document provides a taxonomy of feasibility violation codes, structured response schemas, and advice for implementing diagnostics in user interfaces.

---

## 1. Diagnostics Payload Schema

When an itinerary violates hard constraints, `Itinerary.is_feasible` is marked `False`, and `Itinerary.violation_details` is populated with a list of dictionaries mapping the following contract:

```json
{
  "code": "string (The constraint validation key)",
  "location": "string (City name or directional segment leg name)",
  "date": "string (ISO Date YYYY-MM-DD)",
  "observed_value": "float (The actual value checked)",
  "threshold_limit": "float (The constraint threshold that was breached)",
  "remediation_hint": "string (Actionable help to bypass the error)"
}
```

---

## 2. Violation Codes Index

| Code | Severity | Context | Description |
| :--- | :--- | :--- | :--- |
| `INFEASIBLE_WEATHER_MAX_HIGH` | Blocking | Weather | Travel destination high temperature exceeds the maximum comfortable limit. |
| `INFEASIBLE_WEATHER_MIN_HIGH` | Blocking | Weather | Travel destination high temperature falls below the minimum comfortable limit. |
| `INFEASIBLE_DAILY_MILEAGE` | Blocking | Mileage | A single travel day segment distance exceeds the maximum daily mileage cap. |
| `INFEASIBLE_DAILY_ASCENT` | Blocking | Ascent | A single travel day total climbing elevation exceeds the maximum daily ascent cap. |

---

## 3. Solver Optimization: Fail-Fast Verification

During routing optimizations (e.g. beam search, anytime search), verifying every single constraint on every step of an itinerary is unnecessary if an early day already breaches a limit.

To optimize, `FeasibilityEngine.validate_itinerary(..., fail_fast=True)` aborts verification and returns immediately on the **very first violation**. 

- **Search Phase**: Uses `fail_fast=True` to prune infeasible branches instantly and maximize pruning efficiency.
- **Reporting Phase**: Uses `fail_fast=False` when preparing the final itinerary results to provide a comprehensive, actionable diagnostic list of all breaches across the selected plan.
