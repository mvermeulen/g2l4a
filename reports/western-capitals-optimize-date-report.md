# Route Recommendations Comparison

## Overview Comparison
| Option | Start Date | Feasible? | Total Score | Weather Score | Distance Score | Hills Score | Total Distance | Distance Source | Total Climb | Key Difference |
|---|---|---|---|---|---|---|---|---|---|---|
| **Best Recommendation** | 2026-02-01 | Yes | 0.6030 | 0.5798 | 0.3858 | 0.9832 | 3407.0 mi | graphhopper | 37112 ft | Baseline / Optimal Route |
| Alternative 1 | 2026-02-01 | Yes | 0.5092 | 0.5288 | 0.1853 | 1.0000 | 4916.6 mi | graphhopper | 35230 ft | Alternative via-city sequence, same date |
| Alternative 2 | 2026-02-01 | Yes | 0.4486 | 0.5213 | 0.2822 | 0.6131 | 3983.5 mi | graphhopper | 78594 ft | Alternative via-city sequence, same date |
| Alternative 3 | 2026-02-01 | Yes | 0.3925 | 0.5332 | 0.5146 | 0.0000 | 2950.1 mi | graphhopper | 147318 ft | Alternative via-city sequence, same date |
| Alternative 4 | 2026-02-01 | Yes | 0.3925 | 0.5332 | 0.5146 | 0.0000 | 2950.1 mi | graphhopper | 147318 ft | Alternative via-city sequence, same date |
| Alternative 5 | 2026-03-01 | No ❌ | N/A | N/A | N/A | N/A | 2950.1 mi | graphhopper | 147318 ft | Different start date (2026-03-01) & alternative sequence |
| Alternative 6 | 2026-03-01 | No ❌ | N/A | N/A | N/A | N/A | 3746.5 mi | graphhopper | 96782 ft | Different start date (2026-03-01) & alternative sequence |

## Detailed Recommendations
### Best Recommendation
**Feasible**: Yes
- **Start Date**: 2026-02-01
- **Total Distance**: 3407.0 miles (2773.6 mi paved, 633.4 mi gravel)
- **Distance Source**: graphhopper
- **Total Climbing**: 37112 ft
- **Desirability Scores**:
  - Weather Preference: 0.580
  - Distance Score: 0.386
  - Climbing Score: 0.983
  - **Total Desirability Score**: 0.603

<details>
<summary>Click to view daily travel schedule</summary>

| Start Date | End Date | Days | Origin | Destination | Distance (mi/day) | Ascent (ft/day) | Leg Distance (mi) | Leg Ascent (ft) | Distance Source | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-02-01 | 2026-02-15 | 15 | Salem, Oregon | Phoenix, Arizona | 65.7/day | 0/day | 985.6 | 0 | graphhopper | Avg High: 60.7-71.0°F, Low: 32.6-42.6°F (open-meteo) |  |
| 2026-02-16 | 2026-02-25 | 10 | Phoenix, Arizona | Sacramento, California | 63.4/day | 0/day | 634.3 | 0 | graphhopper | Avg High: 70.0-76.5°F, Low: 40.2-49.1°F (open-meteo) |  |
| 2026-02-26 | 2026-03-01 | 4 | Sacramento, California | Carson City, Nevada | 39.5/day | 3937/day | 157.9 mi (157.0 mi paved, 0.9 mi gravel) | 15747 | graphhopper | Avg High: 49.8-52.9°F, Low: 37.7-45.8°F (open-meteo) |  |
| 2026-03-02 | 2026-03-13 | 12 | Carson City, Nevada | Santa Fe, New Mexico | 66.2/day | 0/day | 795.0 | 0 | graphhopper | Avg High: 46.1-57.2°F, Low: 28.3-40.0°F (open-meteo) |  |
| 2026-03-14 | 2026-03-25 | 12 | Santa Fe, New Mexico | Austin, Texas | 69.5/day | 1780/day | 834.3 mi (612.1 mi paved, 222.2 mi gravel) | 21364 | graphhopper | Avg High: 42.9-80.0°F, Low: 27.9-65.1°F (open-meteo) |  |

</details>

---

### Alternative 1
**Feasible**: Yes
- **Start Date**: 2026-02-01
- **Total Distance**: 4916.6 miles (2540.0 mi paved, 2376.6 mi gravel)
- **Distance Source**: graphhopper
- **Total Climbing**: 35230 ft
- **Desirability Scores**:
  - Weather Preference: 0.529
  - Distance Score: 0.185
  - Climbing Score: 1.000
  - **Total Desirability Score**: 0.509

<details>
<summary>Click to view daily travel schedule</summary>

| Start Date | End Date | Days | Origin | Destination | Distance (mi/day) | Ascent (ft/day) | Leg Distance (mi) | Leg Ascent (ft) | Distance Source | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-02-01 | 2026-02-15 | 15 | Salem, Oregon | Phoenix, Arizona | 65.7/day | 0/day | 985.6 | 0 | graphhopper | Avg High: 60.7-71.0°F, Low: 32.6-42.6°F (open-meteo) |  |
| 2026-02-16 | 2026-02-27 | 12 | Phoenix, Arizona | Carson City, Nevada | 66.0/day | 2936/day | 792.3 mi (409.3 mi paved, 383.0 mi gravel) | 35230 | graphhopper | Avg High: 43.3-58.6°F, Low: 25.3-39.7°F (open-meteo) |  |
| 2026-02-28 | 2026-03-11 | 12 | Carson City, Nevada | Santa Fe, New Mexico | 66.2/day | 0/day | 795.0 | 0 | graphhopper | Avg High: 46.1-57.1°F, Low: 28.3-40.0°F (open-meteo) |  |
| 2026-03-12 | 2026-03-24 | 13 | Santa Fe, New Mexico | Sacramento, California | 67.6/day | 0/day | 878.8 | 0 | graphhopper | Avg High: 57.2-73.0°F, Low: 34.8-49.8°F (open-meteo) |  |
| 2026-03-25 | 2026-04-14 | 21 | Sacramento, California | Austin, Texas | 69.8/day | 0/day | 1465.0 | 0 | graphhopper | Avg High: 61.9-87.8°F, Low: 43.4-70.4°F (open-meteo) |  |

</details>

---

### Alternative 2
**Feasible**: Yes
- **Start Date**: 2026-02-01
- **Total Distance**: 3983.5 miles (2793.1 mi paved, 1190.4 mi gravel)
- **Distance Source**: graphhopper
- **Total Climbing**: 78594 ft
- **Desirability Scores**:
  - Weather Preference: 0.521
  - Distance Score: 0.282
  - Climbing Score: 0.613
  - **Total Desirability Score**: 0.449

<details>
<summary>Click to view daily travel schedule</summary>

| Start Date | End Date | Days | Origin | Destination | Distance (mi/day) | Ascent (ft/day) | Leg Distance (mi) | Leg Ascent (ft) | Distance Source | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-02-01 | 2026-02-10 | 10 | Salem, Oregon | Sacramento, California | 63.4/day | 4095/day | 634.3 mi (586.3 mi paved, 48.0 mi gravel) | 40946 | graphhopper | Avg High: 55.9-69.5°F, Low: 31.2-49.0°F (open-meteo) |  |
| 2026-02-11 | 2026-02-20 | 10 | Sacramento, California | Phoenix, Arizona | 63.4/day | 0/day | 634.3 | 0 | graphhopper | Avg High: 67.5-72.5°F, Low: 39.5-48.5°F (open-meteo) |  |
| 2026-02-21 | 2026-02-28 | 8 | Phoenix, Arizona | Santa Fe, New Mexico | 66.4/day | 4706/day | 531.2 mi (222.8 mi paved, 308.4 mi gravel) | 37648 | graphhopper | Avg High: 46.7-53.6°F, Low: 26.4-33.8°F (open-meteo) |  |
| 2026-03-01 | 2026-03-12 | 12 | Santa Fe, New Mexico | Carson City, Nevada | 66.2/day | 0/day | 795.0 | 0 | graphhopper | Avg High: 44.0-56.2°F, Low: 28.6-47.7°F (open-meteo) |  |
| 2026-03-13 | 2026-04-01 | 20 | Carson City, Nevada | Austin, Texas | 69.4/day | 0/day | 1388.7 | 0 | graphhopper | Avg High: 42.9-80.0°F, Low: 27.9-70.4°F (open-meteo) |  |

</details>

---

### Alternative 3
**Feasible**: Yes
- **Start Date**: 2026-02-01
- **Total Distance**: 2950.1 miles (1928.8 mi paved, 1021.3 mi gravel)
- **Distance Source**: graphhopper
- **Total Climbing**: 147318 ft
- **Desirability Scores**:
  - Weather Preference: 0.533
  - Distance Score: 0.515
  - Climbing Score: 0.000
  - **Total Desirability Score**: 0.393

<details>
<summary>Click to view daily travel schedule</summary>

| Start Date | End Date | Days | Origin | Destination | Distance (mi/day) | Ascent (ft/day) | Leg Distance (mi) | Leg Ascent (ft) | Distance Source | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-02-01 | 2026-02-10 | 10 | Salem, Oregon | Sacramento, California | 63.4/day | 4095/day | 634.3 mi (586.3 mi paved, 48.0 mi gravel) | 40946 | graphhopper | Avg High: 55.9-69.5°F, Low: 31.2-49.0°F (open-meteo) |  |
| 2026-02-11 | 2026-02-14 | 4 | Sacramento, California | Carson City, Nevada | 39.5/day | 3937/day | 157.9 mi (157.0 mi paved, 0.9 mi gravel) | 15747 | graphhopper | Avg High: 41.4-48.5°F, Low: 28.3-29.6°F (open-meteo) |  |
| 2026-02-15 | 2026-02-26 | 12 | Carson City, Nevada | Phoenix, Arizona | 66.0/day | 2634/day | 792.3 mi (414.6 mi paved, 377.8 mi gravel) | 31612 | graphhopper | Avg High: 68.5-78.5°F, Low: 41.7-51.5°F (open-meteo) |  |
| 2026-02-27 | 2026-03-06 | 8 | Phoenix, Arizona | Santa Fe, New Mexico | 66.4/day | 4706/day | 531.2 mi (222.8 mi paved, 308.4 mi gravel) | 37648 | graphhopper | Avg High: 46.7-55.7°F, Low: 30.6-40.0°F (open-meteo) |  |
| 2026-03-07 | 2026-03-18 | 12 | Santa Fe, New Mexico | Austin, Texas | 69.5/day | 1780/day | 834.3 mi (612.1 mi paved, 222.2 mi gravel) | 21364 | graphhopper | Avg High: 42.9-75.0°F, Low: 27.9-65.1°F (open-meteo) |  |

</details>

---

### Alternative 4
**Feasible**: Yes
- **Start Date**: 2026-02-01
- **Total Distance**: 2950.1 miles (1928.8 mi paved, 1021.3 mi gravel)
- **Distance Source**: graphhopper
- **Total Climbing**: 147318 ft
- **Desirability Scores**:
  - Weather Preference: 0.533
  - Distance Score: 0.515
  - Climbing Score: 0.000
  - **Total Desirability Score**: 0.393

<details>
<summary>Click to view daily travel schedule</summary>

| Start Date | End Date | Days | Origin | Destination | Distance (mi/day) | Ascent (ft/day) | Leg Distance (mi) | Leg Ascent (ft) | Distance Source | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-02-01 | 2026-02-10 | 10 | Salem, Oregon | Sacramento, California | 63.4/day | 4095/day | 634.3 mi (586.3 mi paved, 48.0 mi gravel) | 40946 | graphhopper | Avg High: 55.9-69.5°F, Low: 31.2-49.0°F (open-meteo) |  |
| 2026-02-11 | 2026-02-14 | 4 | Sacramento, California | Carson City, Nevada | 39.5/day | 3937/day | 157.9 mi (157.0 mi paved, 0.9 mi gravel) | 15747 | graphhopper | Avg High: 41.4-48.5°F, Low: 28.3-29.6°F (open-meteo) |  |
| 2026-02-15 | 2026-02-26 | 12 | Carson City, Nevada | Phoenix, Arizona | 66.0/day | 2634/day | 792.3 mi (414.6 mi paved, 377.8 mi gravel) | 31612 | graphhopper | Avg High: 68.5-78.5°F, Low: 41.7-51.5°F (open-meteo) |  |
| 2026-02-27 | 2026-03-06 | 8 | Phoenix, Arizona | Santa Fe, New Mexico | 66.4/day | 4706/day | 531.2 mi (222.8 mi paved, 308.4 mi gravel) | 37648 | graphhopper | Avg High: 46.7-55.7°F, Low: 30.6-40.0°F (open-meteo) |  |
| 2026-03-07 | 2026-03-18 | 12 | Santa Fe, New Mexico | Austin, Texas | 69.5/day | 1780/day | 834.3 mi (612.1 mi paved, 222.2 mi gravel) | 21364 | graphhopper | Avg High: 42.9-75.0°F, Low: 27.9-65.1°F (open-meteo) |  |

</details>

---

### Alternative 5
**Feasible**: No ❌
- **Start Date**: 2026-03-01
- **Total Distance**: 2950.1 miles (1928.8 mi paved, 1021.3 mi gravel)
- **Distance Source**: graphhopper
- **Total Climbing**: 147318 ft
- **Violated Constraints**:
  - [INFEASIBLE_WEATHER_MIN_LOW] at Carson City, Nevada on 2026-03-14: observed 18.5 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Carson City, Nevada.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Santa Fe, New Mexico on 2026-03-30: observed 18.9 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Santa Fe, New Mexico.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Santa Fe, New Mexico on 2026-03-31: observed 20.2 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Santa Fe, New Mexico.

<details>
<summary>Click to view daily travel schedule</summary>

ROUTE INFEASIBLE


</details>

---

### Alternative 6
**Feasible**: No ❌
- **Start Date**: 2026-03-01
- **Total Distance**: 3746.5 miles (2226.3 mi paved, 1520.1 mi gravel)
- **Distance Source**: graphhopper
- **Total Climbing**: 96782 ft
- **Violated Constraints**:
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Austin, Texas on 2026-04-20: observed 90.3 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Austin, Texas.

<details>
<summary>Click to view daily travel schedule</summary>

ROUTE INFEASIBLE


</details>

---

## Data Attribution
- Weather data by [Open-Meteo.com](https://open-meteo.com/) under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Data has been transformed into itinerary-level schedule summaries.
- Routing and elevation data powered by [GraphHopper](https://www.graphhopper.com/) using [OpenStreetMap](https://www.openstreetmap.org/copyright) data licensed under [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/).


