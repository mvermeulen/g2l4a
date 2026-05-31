# Output Contract Schema & Formatting Reference

This document serves as the canonical output contract reference for the `g2l4a` Route Optimizer, detailing both Markdown format structures and JSON serialization schemas.

---

## 1. Human-Readable Markdown format

The `OutputFormatter.format_recommendations_markdown` generates a comprehensive comparison document:

### A. Overview Comparison Table
Compares the total desirability scores, individual comfort/efficiency attributes, and overall itinerary stats across all candidates:

| Option | Feasible? | Total Score | Weather Score | Distance Score | Hills Score | Total Distance | Total Climb |
|---|---|---|---|---|---|---|---|
| **Best Recommendation** | Yes | 0.9000 | 1.0000 | 1.0000 | 0.5000 | 60.0 mi | 2000 ft |
| Alternative 1 | Yes | 0.8500 | 0.8000 | 0.9000 | 0.9000 | 65.0 mi | 400 ft |

### B. Detailed Section with Collapsible Schedules
Each itinerary displays its scoring or constraint breaches, and wraps the detailed daily travel schedule in an elegant collapsible HTML block:

```markdown
### Best Recommendation
**Feasible**: Yes
- **Total Distance**: 60.0 miles
- **Total Climbing**: 2000 ft
- **Desirability Scores**:
  - Weather Preference: 1.000
  - Distance Score: 1.000
  - Climbing Score: 0.500
  - **Total Desirability Score**: 0.900

<details>
<summary>Click to view daily travel schedule</summary>

| Day | Date | Origin | Destination | Distance (mi) | Ascent (ft) | Weather Context | Notes |
|---|---|---|---|---|---|---|---|
| 1 | 2026-06-01 | A | B | 60.0 | 2000 | Avg High: 70.0°F, Low: 50.0°F | |

</details>
```

---

## 2. Structured JSON payload Schema

The `OutputFormatter.serialize_recommendations_json` returns a complete, predictable, and strictly formatted JSON payload:

```json
{
  "solver_metrics": {
    "duration_ms": 12.5,
    "evaluated_permutations": 25,
    "pruned_branches": 4,
    "routing_api_calls": 10,
    "weather_api_calls": 10,
    "l1_cache_hits": 8,
    "l2_cache_hits": 6,
    "cache_hit_rate": 0.5833
  },
  "recommendations": [
    {
      "is_feasible": true,
      "start_city": "A",
      "completion_city": "B",
      "via_cities": [],
      "start_date": "2026-06-01",
      "scores": {
        "weather": 1.0,
        "distance": 1.0,
        "hills": 0.5,
        "total": 0.9
      },
      "legs": [
        {
          "origin": "A",
          "destination": "B",
          "distance_miles": 60.0,
          "ascent_feet": 2000.0
        }
      ],
      "schedule": [
        {
          "day_number": 1,
          "date": "2026-06-01",
          "origin": "A",
          "destination": "B",
          "distance_miles": 60.0,
          "ascent_feet": 2000.0,
          "high_temp_f": 70.0,
          "low_temp_f": 50.0,
          "is_rest_day": false
        }
      ],
      "violations": []
    }
  ]
}
```
For unfeasible itineraries, the values in `"scores"` are set to `null`, and the array `"violations"` contains the list of `ConstraintViolation` payloads.
