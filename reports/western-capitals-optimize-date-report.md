# Route Recommendations Comparison

## Overview Comparison
| Option | Start Date | Feasible? | Total Score | Weather Score | Distance Score | Hills Score | Total Distance | Total Climb | Key Difference |
|---|---|---|---|---|---|---|---|---|---|
| **Best Recommendation** | 2026-03-01 | No ❌ | N/A | N/A | N/A | N/A | 2114.3 mi | 3090 ft | Baseline / Optimal Route |
| Alternative 1 | 2026-12-01 | No ❌ | N/A | N/A | N/A | N/A | 2114.3 mi | 3090 ft | Different start date (2026-12-01), same sequence |
| Alternative 2 | 2026-02-01 | Yes | 0.7636 | 0.5433 | 1.0000 | 0.8764 | 2114.3 mi | 3090 ft | Different start date (2026-02-01), same sequence |
| Alternative 3 | 2026-02-01 | Yes | 0.7636 | 0.5433 | 1.0000 | 0.8764 | 2114.3 mi | 3090 ft | Different start date (2026-02-01), same sequence |
| Alternative 4 | 2026-11-01 | Yes | 0.7295 | 0.4676 | 1.0000 | 0.8764 | 2114.3 mi | 3090 ft | Different start date (2026-11-01), same sequence |

## Detailed Recommendations
### Best Recommendation
**Feasible**: No ❌
- **Start Date**: 2026-03-01
- **Total Distance**: 2114.3 miles
- **Total Climbing**: 3090 ft
- **Violated Constraints**:
  - [INFEASIBLE_WEATHER_MIN_LOW] at Santa Fe, New Mexico on 2026-03-19: observed 22.6 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Santa Fe, New Mexico.

<details>
<summary>Click to view daily travel schedule</summary>

ROUTE INFEASIBLE


</details>

---

### Alternative 1
**Feasible**: No ❌
- **Start Date**: 2026-12-01
- **Total Distance**: 2114.3 miles
- **Total Climbing**: 3090 ft
- **Violated Constraints**:
  - [INFEASIBLE_WEATHER_MIN_LOW] at Carson City, Nevada on 2026-12-08: observed 23.9 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Carson City, Nevada.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Carson City, Nevada on 2026-12-09: observed 23.9 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Carson City, Nevada.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Santa Fe, New Mexico on 2026-12-19: observed 17.6 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Santa Fe, New Mexico.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Santa Fe, New Mexico on 2026-12-20: observed 17.6 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Santa Fe, New Mexico.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Santa Fe, New Mexico on 2026-12-21: observed 17.6 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Santa Fe, New Mexico.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Santa Fe, New Mexico on 2026-12-22: observed 17.6 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Santa Fe, New Mexico.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Santa Fe, New Mexico on 2026-12-23: observed 17.6 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Santa Fe, New Mexico.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Santa Fe, New Mexico on 2026-12-24: observed 17.6 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Santa Fe, New Mexico.

<details>
<summary>Click to view daily travel schedule</summary>

ROUTE INFEASIBLE


</details>

---

### Alternative 2
**Feasible**: Yes
- **Start Date**: 2026-02-01
- **Total Distance**: 2114.3 miles
- **Total Climbing**: 3090 ft
- **Desirability Scores**:
  - Weather Preference: 0.543
  - Distance Score: 1.000
  - Climbing Score: 0.876
  - **Total Desirability Score**: 0.764

<details>
<summary>Click to view daily travel schedule</summary>

| Day | Date | Origin | Destination | Distance (mi) | Ascent (ft) | Weather Context | Notes |
|---|---|---|---|---|---|---|---|
| 1 | 2026-02-01 | Salem, Oregon | Sacramento, California | 63.7 | 24 | Avg High: 55.9°F, Low: 31.2°F (open-meteo) |  |
| 2 | 2026-02-02 | Salem, Oregon | Sacramento, California | 63.7 | 24 | Avg High: 57.4°F, Low: 36.2°F (open-meteo) |  |
| 3 | 2026-02-03 | Salem, Oregon | Sacramento, California | 63.7 | 24 | Avg High: 60.8°F, Low: 37.5°F (open-meteo) |  |
| 4 | 2026-02-04 | Salem, Oregon | Sacramento, California | 63.7 | 24 | Avg High: 61.7°F, Low: 39.9°F (open-meteo) |  |
| 5 | 2026-02-05 | Salem, Oregon | Sacramento, California | 63.7 | 24 | Avg High: 63.5°F, Low: 35.9°F (open-meteo) |  |
| 6 | 2026-02-06 | Salem, Oregon | Sacramento, California | 63.7 | 24 | Avg High: 68.6°F, Low: 41.1°F (open-meteo) |  |
| 7 | 2026-02-07 | Salem, Oregon | Sacramento, California | 63.7 | 24 | Avg High: 69.5°F, Low: 49.0°F (open-meteo) |  |
| 8 | 2026-02-08 | Sacramento, California | Carson City, Nevada | 50.5 | 255 | Avg High: 41.2°F, Low: 26.4°F (open-meteo) |  |
| 9 | 2026-02-09 | Sacramento, California | Carson City, Nevada | 50.5 | 255 | Avg High: 41.7°F, Low: 29.6°F (open-meteo) |  |
| 10 | 2026-02-10 | Carson City, Nevada | Phoenix, Arizona | 64.6 | 61 | Avg High: 67.5°F, Low: 39.6°F (open-meteo) |  |
| 11 | 2026-02-11 | Carson City, Nevada | Phoenix, Arizona | 64.6 | 61 | Avg High: 67.7°F, Low: 40.3°F (open-meteo) |  |
| 12 | 2026-02-12 | Carson City, Nevada | Phoenix, Arizona | 64.6 | 61 | Avg High: 67.5°F, Low: 39.5°F (open-meteo) |  |
| 13 | 2026-02-13 | Carson City, Nevada | Phoenix, Arizona | 64.6 | 61 | Avg High: 70.9°F, Low: 42.6°F (open-meteo) |  |
| 14 | 2026-02-14 | Carson City, Nevada | Phoenix, Arizona | 64.6 | 61 | Avg High: 71.0°F, Low: 42.5°F (open-meteo) |  |
| 15 | 2026-02-15 | Carson City, Nevada | Phoenix, Arizona | 64.6 | 61 | Avg High: 69.4°F, Low: 41.7°F (open-meteo) |  |
| 16 | 2026-02-16 | Carson City, Nevada | Phoenix, Arizona | 64.6 | 61 | Avg High: 69.7°F, Low: 44.0°F (open-meteo) |  |
| 17 | 2026-02-17 | Carson City, Nevada | Phoenix, Arizona | 64.6 | 61 | Avg High: 72.4°F, Low: 43.1°F (open-meteo) |  |
| 18 | 2026-02-18 | Carson City, Nevada | Phoenix, Arizona | 64.6 | 61 | Avg High: 72.5°F, Low: 43.5°F (open-meteo) |  |
| 19 | 2026-02-19 | Phoenix, Arizona | Santa Fe, New Mexico | 63.6 | 177 | Avg High: 40.6°F, Low: 24.9°F (open-meteo) |  |
| 20 | 2026-02-20 | Phoenix, Arizona | Santa Fe, New Mexico | 63.6 | 177 | Avg High: 40.2°F, Low: 29.2°F (open-meteo) |  |
| 21 | 2026-02-21 | Phoenix, Arizona | Santa Fe, New Mexico | 63.6 | 177 | Avg High: 47.6°F, Low: 28.7°F (open-meteo) |  |
| 22 | 2026-02-22 | Phoenix, Arizona | Santa Fe, New Mexico | 63.6 | 177 | Avg High: 51.2°F, Low: 26.4°F (open-meteo) |  |
| 23 | 2026-02-23 | Phoenix, Arizona | Santa Fe, New Mexico | 63.6 | 177 | Avg High: 53.6°F, Low: 28.6°F (open-meteo) |  |
| 24 | 2026-02-24 | Phoenix, Arizona | Santa Fe, New Mexico | 63.6 | 177 | Avg High: 52.8°F, Low: 27.8°F (open-meteo) |  |
| 25 | 2026-02-25 | Santa Fe, New Mexico | Austin, Texas | 67.1 | 89 | Avg High: 76.9°F, Low: 47.7°F (open-meteo) |  |
| 26 | 2026-02-26 | Santa Fe, New Mexico | Austin, Texas | 67.1 | 89 | Avg High: 75.8°F, Low: 56.1°F (open-meteo) |  |
| 27 | 2026-02-27 | Santa Fe, New Mexico | Austin, Texas | 67.1 | 89 | Avg High: 65.2°F, Low: 47.5°F (open-meteo) |  |
| 28 | 2026-02-28 | Santa Fe, New Mexico | Austin, Texas | 67.1 | 89 | Avg High: 52.8°F, Low: 46.4°F (open-meteo) |  |
| 29 | 2026-03-01 | Santa Fe, New Mexico | Austin, Texas | 67.1 | 89 | Avg High: 64.5°F, Low: 45.8°F (open-meteo) |  |
| 30 | 2026-03-02 | Santa Fe, New Mexico | Austin, Texas | 67.1 | 89 | Avg High: 72.1°F, Low: 50.3°F (open-meteo) |  |
| 31 | 2026-03-03 | Santa Fe, New Mexico | Austin, Texas | 67.1 | 89 | Avg High: 83.0°F, Low: 52.5°F (open-meteo) |  |
| 32 | 2026-03-04 | Santa Fe, New Mexico | Austin, Texas | 67.1 | 89 | Avg High: 83.2°F, Low: 62.0°F (open-meteo) |  |
| 33 | 2026-03-05 | Santa Fe, New Mexico | Austin, Texas | 67.1 | 89 | Avg High: 82.9°F, Low: 65.6°F (open-meteo) |  |

</details>

---

### Alternative 3
**Feasible**: Yes
- **Start Date**: 2026-02-01
- **Total Distance**: 2114.3 miles
- **Total Climbing**: 3090 ft
- **Desirability Scores**:
  - Weather Preference: 0.543
  - Distance Score: 1.000
  - Climbing Score: 0.876
  - **Total Desirability Score**: 0.764

<details>
<summary>Click to view daily travel schedule</summary>

| Day | Date | Origin | Destination | Distance (mi) | Ascent (ft) | Weather Context | Notes |
|---|---|---|---|---|---|---|---|
| 1 | 2026-02-01 | Salem, Oregon | Sacramento, California | 63.7 | 24 | Avg High: 55.9°F, Low: 31.2°F (open-meteo) |  |
| 2 | 2026-02-02 | Salem, Oregon | Sacramento, California | 63.7 | 24 | Avg High: 57.4°F, Low: 36.2°F (open-meteo) |  |
| 3 | 2026-02-03 | Salem, Oregon | Sacramento, California | 63.7 | 24 | Avg High: 60.8°F, Low: 37.5°F (open-meteo) |  |
| 4 | 2026-02-04 | Salem, Oregon | Sacramento, California | 63.7 | 24 | Avg High: 61.7°F, Low: 39.9°F (open-meteo) |  |
| 5 | 2026-02-05 | Salem, Oregon | Sacramento, California | 63.7 | 24 | Avg High: 63.5°F, Low: 35.9°F (open-meteo) |  |
| 6 | 2026-02-06 | Salem, Oregon | Sacramento, California | 63.7 | 24 | Avg High: 68.6°F, Low: 41.1°F (open-meteo) |  |
| 7 | 2026-02-07 | Salem, Oregon | Sacramento, California | 63.7 | 24 | Avg High: 69.5°F, Low: 49.0°F (open-meteo) |  |
| 8 | 2026-02-08 | Sacramento, California | Carson City, Nevada | 50.5 | 255 | Avg High: 41.2°F, Low: 26.4°F (open-meteo) |  |
| 9 | 2026-02-09 | Sacramento, California | Carson City, Nevada | 50.5 | 255 | Avg High: 41.7°F, Low: 29.6°F (open-meteo) |  |
| 10 | 2026-02-10 | Carson City, Nevada | Phoenix, Arizona | 64.6 | 61 | Avg High: 67.5°F, Low: 39.6°F (open-meteo) |  |
| 11 | 2026-02-11 | Carson City, Nevada | Phoenix, Arizona | 64.6 | 61 | Avg High: 67.7°F, Low: 40.3°F (open-meteo) |  |
| 12 | 2026-02-12 | Carson City, Nevada | Phoenix, Arizona | 64.6 | 61 | Avg High: 67.5°F, Low: 39.5°F (open-meteo) |  |
| 13 | 2026-02-13 | Carson City, Nevada | Phoenix, Arizona | 64.6 | 61 | Avg High: 70.9°F, Low: 42.6°F (open-meteo) |  |
| 14 | 2026-02-14 | Carson City, Nevada | Phoenix, Arizona | 64.6 | 61 | Avg High: 71.0°F, Low: 42.5°F (open-meteo) |  |
| 15 | 2026-02-15 | Carson City, Nevada | Phoenix, Arizona | 64.6 | 61 | Avg High: 69.4°F, Low: 41.7°F (open-meteo) |  |
| 16 | 2026-02-16 | Carson City, Nevada | Phoenix, Arizona | 64.6 | 61 | Avg High: 69.7°F, Low: 44.0°F (open-meteo) |  |
| 17 | 2026-02-17 | Carson City, Nevada | Phoenix, Arizona | 64.6 | 61 | Avg High: 72.4°F, Low: 43.1°F (open-meteo) |  |
| 18 | 2026-02-18 | Carson City, Nevada | Phoenix, Arizona | 64.6 | 61 | Avg High: 72.5°F, Low: 43.5°F (open-meteo) |  |
| 19 | 2026-02-19 | Phoenix, Arizona | Santa Fe, New Mexico | 63.6 | 177 | Avg High: 40.6°F, Low: 24.9°F (open-meteo) |  |
| 20 | 2026-02-20 | Phoenix, Arizona | Santa Fe, New Mexico | 63.6 | 177 | Avg High: 40.2°F, Low: 29.2°F (open-meteo) |  |
| 21 | 2026-02-21 | Phoenix, Arizona | Santa Fe, New Mexico | 63.6 | 177 | Avg High: 47.6°F, Low: 28.7°F (open-meteo) |  |
| 22 | 2026-02-22 | Phoenix, Arizona | Santa Fe, New Mexico | 63.6 | 177 | Avg High: 51.2°F, Low: 26.4°F (open-meteo) |  |
| 23 | 2026-02-23 | Phoenix, Arizona | Santa Fe, New Mexico | 63.6 | 177 | Avg High: 53.6°F, Low: 28.6°F (open-meteo) |  |
| 24 | 2026-02-24 | Phoenix, Arizona | Santa Fe, New Mexico | 63.6 | 177 | Avg High: 52.8°F, Low: 27.8°F (open-meteo) |  |
| 25 | 2026-02-25 | Santa Fe, New Mexico | Austin, Texas | 67.1 | 89 | Avg High: 76.9°F, Low: 47.7°F (open-meteo) |  |
| 26 | 2026-02-26 | Santa Fe, New Mexico | Austin, Texas | 67.1 | 89 | Avg High: 75.8°F, Low: 56.1°F (open-meteo) |  |
| 27 | 2026-02-27 | Santa Fe, New Mexico | Austin, Texas | 67.1 | 89 | Avg High: 65.2°F, Low: 47.5°F (open-meteo) |  |
| 28 | 2026-02-28 | Santa Fe, New Mexico | Austin, Texas | 67.1 | 89 | Avg High: 52.8°F, Low: 46.4°F (open-meteo) |  |
| 29 | 2026-03-01 | Santa Fe, New Mexico | Austin, Texas | 67.1 | 89 | Avg High: 64.5°F, Low: 45.8°F (open-meteo) |  |
| 30 | 2026-03-02 | Santa Fe, New Mexico | Austin, Texas | 67.1 | 89 | Avg High: 72.1°F, Low: 50.3°F (open-meteo) |  |
| 31 | 2026-03-03 | Santa Fe, New Mexico | Austin, Texas | 67.1 | 89 | Avg High: 83.0°F, Low: 52.5°F (open-meteo) |  |
| 32 | 2026-03-04 | Santa Fe, New Mexico | Austin, Texas | 67.1 | 89 | Avg High: 83.2°F, Low: 62.0°F (open-meteo) |  |
| 33 | 2026-03-05 | Santa Fe, New Mexico | Austin, Texas | 67.1 | 89 | Avg High: 82.9°F, Low: 65.6°F (open-meteo) |  |

</details>

---

### Alternative 4
**Feasible**: Yes
- **Start Date**: 2026-11-01
- **Total Distance**: 2114.3 miles
- **Total Climbing**: 3090 ft
- **Desirability Scores**:
  - Weather Preference: 0.468
  - Distance Score: 1.000
  - Climbing Score: 0.876
  - **Total Desirability Score**: 0.730

<details>
<summary>Click to view daily travel schedule</summary>

| Day | Date | Origin | Destination | Distance (mi) | Ascent (ft) | Weather Context | Notes |
|---|---|---|---|---|---|---|---|
| 1 | 2026-11-01 | Salem, Oregon | Sacramento, California | 63.7 | 24 | Avg High: 77.1°F, Low: 49.8°F (open-meteo) |  |
| 2 | 2026-11-02 | Salem, Oregon | Sacramento, California | 63.7 | 24 | Avg High: 64.7°F, Low: 43.8°F (open-meteo) |  |
| 3 | 2026-11-03 | Salem, Oregon | Sacramento, California | 63.7 | 24 | Avg High: 69.4°F, Low: 45.6°F (open-meteo) |  |
| 4 | 2026-11-04 | Salem, Oregon | Sacramento, California | 63.7 | 24 | Avg High: 69.8°F, Low: 42.5°F (open-meteo) |  |
| 5 | 2026-11-05 | Salem, Oregon | Sacramento, California | 63.7 | 24 | Avg High: 76.5°F, Low: 42.7°F (open-meteo) |  |
| 6 | 2026-11-06 | Salem, Oregon | Sacramento, California | 63.7 | 24 | Avg High: 76.5°F, Low: 42.7°F (open-meteo) |  |
| 7 | 2026-11-07 | Salem, Oregon | Sacramento, California | 63.7 | 24 | Avg High: 78.0°F, Low: 48.4°F (open-meteo) |  |
| 8 | 2026-11-08 | Sacramento, California | Carson City, Nevada | 50.5 | 255 | Avg High: 70.7°F, Low: 28.4°F (open-meteo) |  |
| 9 | 2026-11-09 | Sacramento, California | Carson City, Nevada | 50.5 | 255 | Avg High: 61.6°F, Low: 45.6°F (open-meteo) |  |
| 10 | 2026-11-10 | Carson City, Nevada | Phoenix, Arizona | 64.6 | 61 | Avg High: 88.4°F, Low: 58.3°F (open-meteo) |  |
| 11 | 2026-11-11 | Carson City, Nevada | Phoenix, Arizona | 64.6 | 61 | Avg High: 87.9°F, Low: 57.2°F (open-meteo) |  |
| 12 | 2026-11-12 | Carson City, Nevada | Phoenix, Arizona | 64.6 | 61 | Avg High: 88.9°F, Low: 53.7°F (open-meteo) |  |
| 13 | 2026-11-13 | Carson City, Nevada | Phoenix, Arizona | 64.6 | 61 | Avg High: 88.9°F, Low: 53.7°F (open-meteo) |  |
| 14 | 2026-11-14 | Carson City, Nevada | Phoenix, Arizona | 64.6 | 61 | Avg High: 88.9°F, Low: 53.7°F (open-meteo) |  |
| 15 | 2026-11-15 | Carson City, Nevada | Phoenix, Arizona | 64.6 | 61 | Avg High: 88.9°F, Low: 53.7°F (open-meteo) |  |
| 16 | 2026-11-16 | Carson City, Nevada | Phoenix, Arizona | 64.6 | 61 | Avg High: 88.9°F, Low: 53.7°F (open-meteo) |  |
| 17 | 2026-11-17 | Carson City, Nevada | Phoenix, Arizona | 64.6 | 61 | Avg High: 88.9°F, Low: 53.7°F (open-meteo) |  |
| 18 | 2026-11-18 | Carson City, Nevada | Phoenix, Arizona | 64.6 | 61 | Avg High: 88.9°F, Low: 53.7°F (open-meteo) |  |
| 19 | 2026-11-19 | Phoenix, Arizona | Santa Fe, New Mexico | 63.6 | 177 | Avg High: 67.3°F, Low: 24.4°F (open-meteo) |  |
| 20 | 2026-11-20 | Phoenix, Arizona | Santa Fe, New Mexico | 63.6 | 177 | Avg High: 67.3°F, Low: 24.4°F (open-meteo) |  |
| 21 | 2026-11-21 | Phoenix, Arizona | Santa Fe, New Mexico | 63.6 | 177 | Avg High: 67.3°F, Low: 24.4°F (open-meteo) |  |
| 22 | 2026-11-22 | Phoenix, Arizona | Santa Fe, New Mexico | 63.6 | 177 | Avg High: 67.3°F, Low: 24.4°F (open-meteo) |  |
| 23 | 2026-11-23 | Phoenix, Arizona | Santa Fe, New Mexico | 63.6 | 177 | Avg High: 67.3°F, Low: 24.4°F (open-meteo) |  |
| 24 | 2026-11-24 | Phoenix, Arizona | Santa Fe, New Mexico | 63.6 | 177 | Avg High: 67.3°F, Low: 24.4°F (open-meteo) |  |
| 25 | 2026-11-25 | Santa Fe, New Mexico | Austin, Texas | 67.1 | 89 | Avg High: 85.3°F, Low: 50.5°F (open-meteo) |  |
| 26 | 2026-11-26 | Santa Fe, New Mexico | Austin, Texas | 67.1 | 89 | Avg High: 85.3°F, Low: 50.5°F (open-meteo) |  |
| 27 | 2026-11-27 | Santa Fe, New Mexico | Austin, Texas | 67.1 | 89 | Avg High: 85.3°F, Low: 50.5°F (open-meteo) |  |
| 28 | 2026-11-28 | Santa Fe, New Mexico | Austin, Texas | 67.1 | 89 | Avg High: 85.3°F, Low: 50.5°F (open-meteo) |  |
| 29 | 2026-11-29 | Santa Fe, New Mexico | Austin, Texas | 67.1 | 89 | Avg High: 85.3°F, Low: 50.5°F (open-meteo) |  |
| 30 | 2026-11-30 | Santa Fe, New Mexico | Austin, Texas | 67.1 | 89 | Avg High: 85.3°F, Low: 50.5°F (open-meteo) |  |
| 31 | 2026-12-01 | Santa Fe, New Mexico | Austin, Texas | 67.1 | 89 | Avg High: 80.5°F, Low: 43.4°F (open-meteo) |  |
| 32 | 2026-12-02 | Santa Fe, New Mexico | Austin, Texas | 67.1 | 89 | Avg High: 80.5°F, Low: 43.4°F (open-meteo) |  |
| 33 | 2026-12-03 | Santa Fe, New Mexico | Austin, Texas | 67.1 | 89 | Avg High: 80.5°F, Low: 43.4°F (open-meteo) |  |

</details>

---

## Data Attribution
Weather data by [Open-Meteo.com](https://open-meteo.com/) under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Data has been transformed into itinerary-level schedule summaries.


