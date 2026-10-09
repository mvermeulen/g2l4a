# Route Recommendations Comparison

## Overview Comparison
| Option | Start Date | Feasible? | Total Score | Weather Score | Distance Score | Hills Score | Total Distance | Distance Source | Total Climb | Key Difference |
|---|---|---|---|---|---|---|---|---|---|---|
| **Best Recommendation** | 2027-02-15 | No ❌ | N/A | N/A | N/A | N/A | 9381.0 mi | graphhopper | 129317 ft | Baseline / Optimal Route |
| Alternative 1 | 2027-02-15 | No ❌ | N/A | N/A | N/A | N/A | 4885.7 mi | graphhopper | 235567 ft | Alternative via-city sequence, same date |
| Alternative 2 | 2027-03-01 | No ❌ | N/A | N/A | N/A | N/A | 4885.7 mi | graphhopper | 235567 ft | Different start date (2027-03-01) & alternative sequence |
| Alternative 3 | 2027-03-15 | Yes | 0.4047 | 0.5240 | 0.5532 | 0.0000 | 4885.7 mi | graphhopper | 235567 ft | Different start date (2027-03-15) & alternative sequence |

## Detailed Recommendations
### Best Recommendation
**Feasible**: No ❌
- **Start Date**: 2027-02-15
- **Total Distance**: 9381.0 miles (8757.6 mi paved, 623.3 mi gravel)
- **Distance Source**: graphhopper
- **Total Climbing**: 129317 ft
- **Violated Constraints**:
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Washington, DC on 2027-07-04: observed 94.1 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Washington, DC.
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Washington, DC on 2027-07-05: observed 97.8 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Washington, DC.
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Washington, DC on 2027-07-06: observed 98.5 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Washington, DC.
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Washington, DC on 2027-07-07: observed 92.2 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Washington, DC.

<details>
<summary>Click to view daily travel schedule</summary>

ROUTE INFEASIBLE


</details>

---

### Alternative 1
**Feasible**: No ❌
- **Start Date**: 2027-02-15
- **Total Distance**: 4885.7 miles (4570.3 mi paved, 315.5 mi gravel)
- **Distance Source**: graphhopper
- **Total Climbing**: 235567 ft
- **Violated Constraints**:
  - [INFEASIBLE_WEATHER_MIN_LOW] at Jefferson City, Missouri on 2027-02-28: observed 21.8 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Jefferson City, Missouri.

<details>
<summary>Click to view daily travel schedule</summary>

ROUTE INFEASIBLE


</details>

---

### Alternative 2
**Feasible**: No ❌
- **Start Date**: 2027-03-01
- **Total Distance**: 4885.7 miles (4570.3 mi paved, 315.5 mi gravel)
- **Distance Source**: graphhopper
- **Total Climbing**: 235567 ft
- **Violated Constraints**:
  - [INFEASIBLE_WEATHER_MIN_LOW] at Topeka, Kansas on 2027-03-08: observed 19.9 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Topeka, Kansas.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Topeka, Kansas on 2027-03-09: observed 20.1 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Topeka, Kansas.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Topeka, Kansas on 2027-03-10: observed 18.4 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Topeka, Kansas.
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Richmond, Virginia on 2027-05-12: observed 90.4 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Richmond, Virginia.

<details>
<summary>Click to view daily travel schedule</summary>

ROUTE INFEASIBLE


</details>

---

### Alternative 3
**Feasible**: Yes
- **Start Date**: 2027-03-15
- **Total Distance**: 4885.7 miles (4570.3 mi paved, 315.5 mi gravel)
- **Distance Source**: graphhopper
- **Total Climbing**: 235567 ft
- **Desirability Scores**:
  - Weather Preference: 0.524
  - Distance Score: 0.553
  - Climbing Score: 0.000
  - **Total Desirability Score**: 0.405

<details>
<summary>Click to view daily travel schedule</summary>

| Start Date | End Date | Days | Origin | Destination | Distance (mi/day) | Ascent (ft/day) | Leg Distance (mi) | Leg Ascent (ft) | Distance Source | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2027-03-15 | 2027-03-21 | 7 | Austin, Texas | Oklahoma City, Oklahoma | 64.2/day | 2300/day | 449.3 mi (414.0 mi paved, 35.4 mi gravel) | 16102 | graphhopper | Avg High: 56.3-79.9°F, Low: 34.5-49.3°F (open-meteo) |  |
| 2027-03-22 | 2027-03-27 | 6 | Oklahoma City, Oklahoma | Topeka, Kansas | 61.9/day | 1837/day | 371.7 mi (352.9 mi paved, 18.8 mi gravel) | 11019 | graphhopper | Avg High: 52.1-74.9°F, Low: 33.0-52.3°F (open-meteo) |  |
| 2027-03-28 | 2027-03-31 | 4 | Topeka, Kansas | Jefferson City, Missouri | 57.6/day | 2657/day | 230.6 mi (166.3 mi paved, 64.2 mi gravel) | 10630 | graphhopper | Avg High: 57.0-78.6°F, Low: 37.3-47.8°F (open-meteo) |  |
| 2027-04-01 | 2027-04-05 | 5 | Jefferson City, Missouri | Little Rock, Arkansas | 68.7/day | 4526/day | 343.7 mi (312.3 mi paved, 31.4 mi gravel) | 22628 | graphhopper | Avg High: 56.0-72.5°F, Low: 37.7-52.4°F (open-meteo) |  |
| 2027-04-06 | 2027-04-10 | 5 | Little Rock, Arkansas | Jackson, Mississippi | 66.9/day | 1043/day | 334.7 mi (279.4 mi paved, 55.3 mi gravel) | 5213 | graphhopper | Avg High: 74.2-82.9°F, Low: 46.5-63.7°F (open-meteo) |  |
| 2027-04-11 | 2027-04-13 | 3 | Jackson, Mississippi | Baton Rouge, Louisiana | 57.6/day | 2002/day | 172.8 mi (172.8 mi paved) | 6006 | graphhopper | Avg High: 82.0-85.3°F, Low: 57.2-64.8°F (open-meteo) |  |
| 2027-04-14 | 2027-04-19 | 6 | Baton Rouge, Louisiana | Montgomery, Alabama | 68.7/day | 2405/day | 412.1 mi (412.1 mi paved) | 14430 | graphhopper | Avg High: 76.4-83.1°F, Low: 49.5-65.9°F (open-meteo) |  |
| 2027-04-20 | 2027-04-23 | 4 | Montgomery, Alabama | Tallahassee, Florida | 55.3/day | 2195/day | 221.0 mi (202.9 mi paved, 18.1 mi gravel) | 8780 | graphhopper | Avg High: 79.6-84.7°F, Low: 63.5-73.2°F (open-meteo) |  |
| 2027-04-24 | 2027-04-28 | 5 | Tallahassee, Florida | Atlanta, Georgia | 62.6/day | 2701/day | 312.9 mi (309.0 mi paved, 3.8 mi gravel) | 13506 | graphhopper | Avg High: 71.2-77.7°F, Low: 46.0-56.9°F (open-meteo) |  |
| 2027-04-29 | 2027-05-03 | 5 | Atlanta, Georgia | Nashville, Tennessee | 61.5/day | 3520/day | 307.6 mi (307.6 mi paved) | 17599 | graphhopper | Avg High: 61.0-83.5°F, Low: 43.0-64.2°F (open-meteo) |  |
| 2027-05-04 | 2027-05-07 | 4 | Nashville, Tennessee | Frankfort, Kentucky | 57.8/day | 3069/day | 231.1 mi (231.1 mi paved) | 12275 | graphhopper | Avg High: 56.3-78.3°F, Low: 37.0-51.7°F (open-meteo) |  |
| 2027-05-08 | 2027-05-11 | 4 | Frankfort, Kentucky | Charleston, West Virginia | 64.2/day | 4122/day | 256.6 mi (255.3 mi paved, 1.3 mi gravel) | 16489 | graphhopper | Avg High: 79.3-87.7°F, Low: 53.6-65.4°F (open-meteo) |  |
| 2027-05-12 | 2027-05-19 | 8 | Charleston, West Virginia | Columbia, South Carolina | 54.2/day | 4733/day | 433.4 mi (420.5 mi paved, 12.9 mi gravel) | 37863 | graphhopper | Avg High: 76.2-88.0°F, Low: 60.0-68.5°F (open-meteo) |  |
| 2027-05-20 | 2027-05-23 | 4 | Columbia, South Carolina | Raleigh, North Carolina | 58.8/day | 2356/day | 235.1 mi (235.1 mi paved) | 9424 | graphhopper | Avg High: 76.6-80.6°F, Low: 53.5-70.1°F (open-meteo) |  |
| 2027-05-24 | 2027-05-26 | 3 | Raleigh, North Carolina | Richmond, Virginia | 63.1/day | 2711/day | 189.3 mi (172.2 mi paved, 17.1 mi gravel) | 8134 | graphhopper | Avg High: 86.3-89.9°F, Low: 58.6-66.5°F (open-meteo) |  |
| 2027-05-27 | 2027-05-30 | 4 | Richmond, Virginia | Harrisburg, Pennsylvania | 63.8/day | 4087/day | 255.2 mi (236.7 mi paved, 18.5 mi gravel) | 16349 | graphhopper | Avg High: 78.4-83.5°F, Low: 58.3-70.3°F (open-meteo) |  |
| 2027-05-31 | 2027-06-01 | 2 | Harrisburg, Pennsylvania | Washington, DC | 64.3/day | 4561/day | 128.6 mi (114.5 mi paved, 14.2 mi gravel) | 9122 | graphhopper | Avg High: 82.2-82.4°F, Low: 66.2-72.5°F (open-meteo) |  |

</details>

---

## Data Attribution
- Weather data by [Open-Meteo.com](https://open-meteo.com/) under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Data has been transformed into itinerary-level schedule summaries.
- Routing and elevation data powered by [GraphHopper](https://www.graphhopper.com/) using [OpenStreetMap](https://www.openstreetmap.org/copyright) data licensed under [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/).


