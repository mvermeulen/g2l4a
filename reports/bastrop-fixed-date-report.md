# Route Recommendations Comparison

## Overview Comparison
| Option | Start Date | Feasible? | Total Score | Weather Score | Distance Score | Hills Score | Total Distance | Distance Source | Total Climb | Key Difference |
|---|---|---|---|---|---|---|---|---|---|---|
| **Best Recommendation** | 2026-05-16 | Yes | 0.6581 | 0.2650 | 0.7883 | 1.0000 | 38.5 mi | graphhopper | 1052 ft | Baseline / Optimal Route |
| Alternative 1 | 2026-05-30 | Yes | 0.5986 | 0.0950 | 0.7883 | 1.0000 | 38.5 mi | graphhopper | 1052 ft | Different start date (2026-05-30), same sequence |
| Alternative 2 | 2026-06-13 | No ❌ | N/A | N/A | N/A | N/A | 38.5 mi | graphhopper | 1052 ft | Different start date (2026-06-13), same sequence |

## Detailed Recommendations
### Best Recommendation
**Feasible**: Yes
- **Start Date**: 2026-05-16
- **Total Distance**: 38.5 miles (38.5 mi paved)
- **Distance Source**: graphhopper
- **Total Climbing**: 1052 ft
- **Desirability Scores**:
  - Weather Preference: 0.265
  - Distance Score: 0.788
  - Climbing Score: 1.000
  - **Total Desirability Score**: 0.658

<details>
<summary>Click to view daily travel schedule</summary>

| Start Date | End Date | Days | Origin | Destination | Distance (mi/day) | Ascent (ft/day) | Leg Distance (mi) | Leg Ascent (ft) | Distance Source | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-05-16 | 2026-05-16 | 1 | Oak Hill, West US Highway 290, Austin, Travis County, Texas, 78749, United States | Bastrop, Bastrop County, Texas, United States | 38.5/day | 1052/day | 38.5 mi (38.5 mi paved) | 1052 | graphhopper | Avg High: 84.7°F, Low: 66.7°F (meteostatweatherprovider) |  |

</details>

---

### Alternative 1
**Feasible**: Yes
- **Start Date**: 2026-05-30
- **Total Distance**: 38.5 miles (38.5 mi paved)
- **Distance Source**: graphhopper
- **Total Climbing**: 1052 ft
- **Desirability Scores**:
  - Weather Preference: 0.095
  - Distance Score: 0.788
  - Climbing Score: 1.000
  - **Total Desirability Score**: 0.599

<details>
<summary>Click to view daily travel schedule</summary>

| Start Date | End Date | Days | Origin | Destination | Distance (mi/day) | Ascent (ft/day) | Leg Distance (mi) | Leg Ascent (ft) | Distance Source | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-05-30 | 2026-05-30 | 1 | Oak Hill, West US Highway 290, Austin, Travis County, Texas, 78749, United States | Bastrop, Bastrop County, Texas, United States | 38.5/day | 1052/day | 38.5 mi (38.5 mi paved) | 1052 | graphhopper | Avg High: 88.1°F, Low: 70.4°F (meteostatweatherprovider) |  |

</details>

---

### Alternative 2
**Feasible**: No ❌
- **Start Date**: 2026-06-13
- **Total Distance**: 38.5 miles (38.5 mi paved)
- **Distance Source**: graphhopper
- **Total Climbing**: 1052 ft
- **Violated Constraints**:
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Bastrop, Bastrop County, Texas, United States on 2026-06-13: observed 93.3 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Bastrop, Bastrop County, Texas, United States.

<details>
<summary>Click to view daily travel schedule</summary>

ROUTE INFEASIBLE


</details>

---

## Data Attribution
- Weather data provided by [Meteostat](https://meteostat.net/) under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Data has been transformed into itinerary-level schedule summaries.
- Routing and elevation data powered by [GraphHopper](https://www.graphhopper.com/) using [OpenStreetMap](https://www.openstreetmap.org/copyright) data licensed under [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/).


