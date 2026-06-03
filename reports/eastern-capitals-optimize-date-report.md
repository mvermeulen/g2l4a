# Route Recommendations Comparison

## Overview Comparison
| Option | Start Date | Feasible? | Total Score | Weather Score | Distance Score | Hills Score | Total Distance | Distance Source | Total Climb | Key Difference |
|---|---|---|---|---|---|---|---|---|---|---|
| **Best Recommendation** | 2026-03-01 | No ❌ | N/A | N/A | N/A | N/A | 4880.0 mi | graphhopper | 262682 ft | Baseline / Optimal Route |
| Alternative 1 | 2026-11-01 | No ❌ | N/A | N/A | N/A | N/A | 4880.0 mi | graphhopper | 262682 ft | Different start date (2026-11-01), same sequence |
| Alternative 2 | 2026-10-01 | Yes | 0.6368 | 0.4715 | 0.5545 | 1.0000 | 4880.0 mi | graphhopper | 262682 ft | Different start date (2026-10-01), same sequence |
| Alternative 3 | 2026-09-01 | No ❌ | N/A | N/A | N/A | N/A | 4880.0 mi | graphhopper | 262682 ft | Different start date (2026-09-01), same sequence |
| Alternative 4 | 2026-04-01 | No ❌ | N/A | N/A | N/A | N/A | 4880.0 mi | graphhopper | 262682 ft | Different start date (2026-04-01), same sequence |
| Alternative 5 | 2026-02-01 | No ❌ | N/A | N/A | N/A | N/A | 4880.0 mi | graphhopper | 262682 ft | Different start date (2026-02-01), same sequence |
| Alternative 6 | 2026-12-01 | No ❌ | N/A | N/A | N/A | N/A | 4880.0 mi | graphhopper | 262682 ft | Different start date (2026-12-01), same sequence |

## Detailed Recommendations
### Best Recommendation
**Feasible**: No ❌
- **Start Date**: 2026-03-01
- **Total Distance**: 4880.0 miles
- **Distance Source**: graphhopper
- **Total Climbing**: 262682 ft
- **Violated Constraints**:
  - [INFEASIBLE_WEATHER_MIN_LOW] at Jefferson City, Missouri on 2026-03-15: observed 22.2 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Jefferson City, Missouri.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Jefferson City, Missouri on 2026-03-16: observed 20.8 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Jefferson City, Missouri.

<details>
<summary>Click to view daily travel schedule</summary>

ROUTE INFEASIBLE


</details>

---

### Alternative 1
**Feasible**: No ❌
- **Start Date**: 2026-11-01
- **Total Distance**: 4880.0 miles
- **Distance Source**: graphhopper
- **Total Climbing**: 262682 ft
- **Violated Constraints**:
  - [INFEASIBLE_WEATHER_MIN_LOW] at Harrisburg, Pennsylvania on 2027-01-13: observed 22.6 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Harrisburg, Pennsylvania.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Harrisburg, Pennsylvania on 2027-01-15: observed 14.8 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Harrisburg, Pennsylvania.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Harrisburg, Pennsylvania on 2027-01-16: observed 16.7 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Harrisburg, Pennsylvania.

<details>
<summary>Click to view daily travel schedule</summary>

ROUTE INFEASIBLE


</details>

---

### Alternative 2
**Feasible**: Yes
- **Start Date**: 2026-10-01
- **Total Distance**: 4880.0 miles
- **Distance Source**: graphhopper
- **Total Climbing**: 262682 ft
- **Desirability Scores**:
  - Weather Preference: 0.471
  - Distance Score: 0.554
  - Climbing Score: 1.000
  - **Total Desirability Score**: 0.637

<details>
<summary>Click to view daily travel schedule</summary>

| Start Date | End Date | Days | Origin | Destination | Distance (mi/day) | Ascent (ft/day) | Leg Distance (mi) | Leg Ascent (ft) | Distance Source | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-01 | 2026-10-07 | 7 | Austin, Texas | Oklahoma City, Oklahoma | 64.7/day | 2429/day | 452.9 | 17000 | graphhopper | Avg High: 73.2-89.4°F, Low: 46.4-63.0°F (open-meteo) |  |
| 2026-10-08 | 2026-10-13 | 6 | Oklahoma City, Oklahoma | Topeka, Kansas | 62.4/day | 2085/day | 374.5 | 12509 | graphhopper | Avg High: 60.5-89.1°F, Low: 45.5-74.5°F (open-meteo) |  |
| 2026-10-14 | 2026-10-17 | 4 | Topeka, Kansas | Jefferson City, Missouri | 57.7/day | 2910/day | 230.9 | 11638 | graphhopper | Avg High: 61.9-82.5°F, Low: 42.3-63.5°F (open-meteo) |  |
| 2026-10-18 | 2026-10-22 | 5 | Jefferson City, Missouri | Little Rock, Arkansas | 68.5/day | 4982/day | 342.5 | 24909 | graphhopper | Avg High: 83.2-85.4°F, Low: 60.2-68.9°F (open-meteo) |  |
| 2026-10-23 | 2026-10-27 | 5 | Little Rock, Arkansas | Jackson, Mississippi | 66.7/day | 1539/day | 333.4 | 7693 | graphhopper | Avg High: 62.9-84.9°F, Low: 45.4-72.0°F (open-meteo) |  |
| 2026-10-28 | 2026-10-30 | 3 | Jackson, Mississippi | Baton Rouge, Louisiana | 57.6/day | 2454/day | 172.9 | 7362 | graphhopper | Avg High: 63.3-75.4°F, Low: 40.6-50.6°F (open-meteo) |  |
| 2026-10-31 | 2026-11-05 | 6 | Baton Rouge, Louisiana | Montgomery, Alabama | 68.3/day | 2882/day | 409.9 | 17294 | graphhopper | Avg High: 70.7-73.5°F, Low: 42.3-65.2°F (open-meteo) |  |
| 2026-11-06 | 2026-11-09 | 4 | Montgomery, Alabama | Tallahassee, Florida | 55.5/day | 2540/day | 222.0 | 10161 | graphhopper | Avg High: 58.2-79.8°F, Low: 39.0-67.4°F (open-meteo) |  |
| 2026-11-10 | 2026-11-14 | 5 | Tallahassee, Florida | Atlanta, Georgia | 63.0/day | 2864/day | 315.0 | 14321 | graphhopper | Avg High: 47.6-60.1°F, Low: 33.1-44.0°F (open-meteo) |  |
| 2026-11-15 | 2026-11-19 | 5 | Atlanta, Georgia | Nashville, Tennessee | 58.6/day | 3589/day | 293.2 | 17944 | graphhopper | Avg High: 60.3-64.2°F, Low: 34.1-40.5°F (open-meteo) |  |
| 2026-11-20 | 2026-11-23 | 4 | Nashville, Tennessee | Frankfort, Kentucky | 57.1/day | 3572/day | 228.5 | 14287 | graphhopper | Avg High: 44.5-65.7°F, Low: 28.3-47.7°F (open-meteo) |  |
| 2026-11-24 | 2026-11-27 | 4 | Frankfort, Kentucky | Charleston, West Virginia | 64.1/day | 4912/day | 256.4 | 19646 | graphhopper | Avg High: 50.4-55.8°F, Low: 29.4-30.1°F (open-meteo) |  |
| 2026-11-28 | 2026-12-05 | 8 | Charleston, West Virginia | Columbia, South Carolina | 54.3/day | 4823/day | 434.7 | 38581 | graphhopper | Avg High: 55.7-70.7°F, Low: 37.1-54.3°F (open-meteo) |  |
| 2026-12-06 | 2026-12-09 | 4 | Columbia, South Carolina | Raleigh, North Carolina | 57.8/day | 2586/day | 231.3 | 10345 | graphhopper | Avg High: 57.8-66.1°F, Low: 37.8-52.8°F (open-meteo) |  |
| 2026-12-10 | 2026-12-12 | 3 | Raleigh, North Carolina | Richmond, Virginia | 65.2/day | 3602/day | 195.7 | 10806 | graphhopper | Avg High: 56.5-63.1°F, Low: 31.8-46.7°F (open-meteo) |  |
| 2026-12-13 | 2026-12-16 | 4 | Richmond, Virginia | Harrisburg, Pennsylvania | 64.2/day | 4515/day | 257.0 | 18058 | graphhopper | Avg High: 36.7-50.2°F, Low: 30.0-38.0°F (open-meteo) |  |
| 2026-12-17 | 2026-12-19 | 3 | Harrisburg, Pennsylvania | Washington, DC | 43.1/day | 3376/day | 129.2 | 10127 | graphhopper | Avg High: 43.8-50.2°F, Low: 31.9-36.8°F (open-meteo) |  |

</details>

---

### Alternative 3
**Feasible**: No ❌
- **Start Date**: 2026-09-01
- **Total Distance**: 4880.0 miles
- **Distance Source**: graphhopper
- **Total Climbing**: 262682 ft
- **Violated Constraints**:
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Topeka, Kansas on 2026-09-10: observed 91.6 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Topeka, Kansas.
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Topeka, Kansas on 2026-09-11: observed 95.4 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Topeka, Kansas.
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Topeka, Kansas on 2026-09-12: observed 92.6 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Topeka, Kansas.
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Little Rock, Arkansas on 2026-09-19: observed 95.0 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Little Rock, Arkansas.
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Little Rock, Arkansas on 2026-09-20: observed 90.3 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Little Rock, Arkansas.
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Jackson, Mississippi on 2026-09-23: observed 90.7 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Jackson, Mississippi.

<details>
<summary>Click to view daily travel schedule</summary>

ROUTE INFEASIBLE


</details>

---

### Alternative 4
**Feasible**: No ❌
- **Start Date**: 2026-04-01
- **Total Distance**: 4880.0 miles
- **Distance Source**: graphhopper
- **Total Climbing**: 262682 ft
- **Violated Constraints**:
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Nashville, Tennessee on 2026-05-18: observed 93.1 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Nashville, Tennessee.
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Raleigh, North Carolina on 2026-06-06: observed 90.1 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Raleigh, North Carolina.
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Raleigh, North Carolina on 2026-06-07: observed 90.8 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Raleigh, North Carolina.
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Richmond, Virginia on 2026-06-12: observed 91.7 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Richmond, Virginia.
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Harrisburg, Pennsylvania on 2026-06-13: observed 92.3 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Harrisburg, Pennsylvania.
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Washington, DC on 2026-06-17: observed 92.2 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Washington, DC.
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Washington, DC on 2026-06-19: observed 92.4 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Washington, DC.

<details>
<summary>Click to view daily travel schedule</summary>

ROUTE INFEASIBLE


</details>

---

### Alternative 5
**Feasible**: No ❌
- **Start Date**: 2026-02-01
- **Total Distance**: 4880.0 miles
- **Distance Source**: graphhopper
- **Total Climbing**: 262682 ft
- **Violated Constraints**:
  - [INFEASIBLE_WEATHER_MIN_LOW] at Oklahoma City, Oklahoma on 2026-02-01: observed 5.5 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Oklahoma City, Oklahoma.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Oklahoma City, Oklahoma on 2026-02-02: observed -1.9 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Oklahoma City, Oklahoma.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Oklahoma City, Oklahoma on 2026-02-03: observed -1.8 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Oklahoma City, Oklahoma.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Oklahoma City, Oklahoma on 2026-02-04: observed -0.6 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Oklahoma City, Oklahoma.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Oklahoma City, Oklahoma on 2026-02-05: observed 9.4 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Oklahoma City, Oklahoma.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Oklahoma City, Oklahoma on 2026-02-06: observed 21.7 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Oklahoma City, Oklahoma.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Topeka, Kansas on 2026-02-08: observed 23.0 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Topeka, Kansas.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Topeka, Kansas on 2026-02-13: observed 19.0 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Topeka, Kansas.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Jefferson City, Missouri on 2026-02-14: observed 14.8 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Jefferson City, Missouri.

<details>
<summary>Click to view daily travel schedule</summary>

ROUTE INFEASIBLE


</details>

---

### Alternative 6
**Feasible**: No ❌
- **Start Date**: 2026-12-01
- **Total Distance**: 4880.0 miles
- **Distance Source**: graphhopper
- **Total Climbing**: 262682 ft
- **Violated Constraints**:
  - [INFEASIBLE_WEATHER_MIN_LOW] at Frankfort, Kentucky on 2027-01-20: observed 22.6 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Frankfort, Kentucky.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Frankfort, Kentucky on 2027-01-22: observed 16.4 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Frankfort, Kentucky.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Frankfort, Kentucky on 2027-01-23: observed 4.3 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Frankfort, Kentucky.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Charleston, West Virginia on 2027-01-24: observed -0.5 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Charleston, West Virginia.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Charleston, West Virginia on 2027-01-25: observed 15.9 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Charleston, West Virginia.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Charleston, West Virginia on 2027-01-26: observed 15.2 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Charleston, West Virginia.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Charleston, West Virginia on 2027-01-27: observed 9.5 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Charleston, West Virginia.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Columbia, South Carolina on 2027-01-28: observed 22.1 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Columbia, South Carolina.

<details>
<summary>Click to view daily travel schedule</summary>

ROUTE INFEASIBLE


</details>

---

## Data Attribution
- Weather data by [Open-Meteo.com](https://open-meteo.com/) under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Data has been transformed into itinerary-level schedule summaries.
- Routing and elevation data powered by [GraphHopper](https://www.graphhopper.com/) using [OpenStreetMap](https://www.openstreetmap.org/copyright) data licensed under [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/).


