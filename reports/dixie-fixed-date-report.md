# Route Recommendations Comparison

## Overview Comparison
| Option | Start Date | Feasible? | Total Score | Weather Score | Distance Score | Hills Score | Total Distance | Distance Source | Total Climb | Key Difference |
|---|---|---|---|---|---|---|---|---|---|---|
| **Best Recommendation** | 2027-01-02 | Yes | 0.7525 | 0.7426 | 0.5611 | 1.0000 | 2500.9 mi | graphhopper | 116207 ft | Baseline / Optimal Route |
| Alternative 1 | 2026-12-19 | No ❌ | N/A | N/A | N/A | N/A | 2500.9 mi | graphhopper | 116207 ft | Different start date (2026-12-19), same sequence |
| Alternative 2 | 2027-01-16 | Yes | 0.7303 | 0.6932 | 0.5611 | 1.0000 | 2500.9 mi | graphhopper | 116207 ft | Different start date (2027-01-16), same sequence |
| Alternative 3 | 2027-01-02 | Yes | 0.4835 | 0.7767 | 0.1418 | 0.3656 | 4974.0 mi | graphhopper | 222636 ft | Alternative via-city sequence, same date |
| Alternative 4 | 2027-01-02 | Yes | 0.4713 | 0.7723 | 0.1460 | 0.3200 | 4902.8 mi | graphhopper | 230284 ft | Alternative via-city sequence, same date |
| Alternative 5 | 2026-12-19 | Yes | 0.4700 | 0.7469 | 0.1418 | 0.3656 | 4974.0 mi | graphhopper | 222636 ft | Different start date (2026-12-19) & alternative sequence |
| Alternative 6 | 2026-12-19 | Yes | 0.4644 | 0.7568 | 0.1470 | 0.3191 | 4886.3 mi | graphhopper | 230433 ft | Different start date (2026-12-19) & alternative sequence |

## Detailed Recommendations
### Best Recommendation
**Feasible**: Yes
- **Start Date**: 2027-01-02
- **Total Distance**: 2500.9 miles
- **Distance Source**: graphhopper
- **Total Climbing**: 116207 ft
- **Desirability Scores**:
  - Weather Preference: 0.743
  - Distance Score: 0.561
  - Climbing Score: 1.000
  - **Total Desirability Score**: 0.752

<details>
<summary>Click to view daily travel schedule</summary>

| Start Date | End Date | Days | Origin | Destination | Distance (mi/day) | Ascent (ft/day) | Leg Distance (mi) | Leg Ascent (ft) | Distance Source | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2027-01-02 | 2027-01-10 | 9 | Austin, Texas | Baton Rouge, Louisiana | 64.5/day | 1974/day | 580.1 | 17769 | graphhopper | Avg High: 77.5°F, Low: 41.6°F (wikipedia) |  |
| 2027-01-11 | 2027-01-13 | 3 | Baton Rouge, Louisiana | Jackson, Mississippi | 57.6/day | 2527/day | 172.8 | 7581 | graphhopper | Avg High: 75.2°F, Low: 36.6°F (wikipedia) |  |
| 2027-01-14 | 2027-01-17 | 4 | Jackson, Mississippi | Montgomery, Alabama | 67.6/day | 3054/day | 270.3 | 12216 | graphhopper | Avg High: 75.6°F, Low: 36.5°F (wikipedia) |  |
| 2027-01-18 | 2027-01-21 | 4 | Montgomery, Alabama | Tallahassee, Florida | 55.5/day | 2540/day | 222.0 | 10161 | graphhopper | Avg High: 78.4°F, Low: 40.5°F (wikipedia) |  |
| 2027-01-22 | 2027-01-26 | 5 | Tallahassee, Florida | Atlanta, Georgia | 63.0/day | 2864/day | 315.0 | 14321 | graphhopper | Avg High: 70.3°F, Low: 35.6°F (wikipedia) |  |
| 2027-01-27 | 2027-01-30 | 4 | Atlanta, Georgia | Columbia, South Carolina | 64.1/day | 3717/day | 256.3 | 14869 | graphhopper | Avg High: 74.5°F, Low: 34.6°F (wikipedia) |  |
| 2027-01-31 | 2027-02-03 | 4 | Columbia, South Carolina | Raleigh, North Carolina | 57.8/day | 2586/day | 231.3 | 10345 | graphhopper | Avg High: 71.9-74.4°F, Low: 31.8-34.2°F (wikipedia) |  |
| 2027-02-04 | 2027-02-06 | 3 | Raleigh, North Carolina | Richmond, Virginia | 65.2/day | 3602/day | 195.7 | 10806 | graphhopper | Avg High: 72.6°F, Low: 30.4°F (wikipedia) |  |
| 2027-02-07 | 2027-02-08 | 2 | Richmond, Virginia | Washington, DC | 63.3/day | 3792/day | 126.5 | 7584 | graphhopper | Avg High: 68.1°F, Low: 31.8°F (wikipedia) |  |
| 2027-02-09 | 2027-02-11 | 3 | Washington, DC | Harrisburg, Pennsylvania | 43.6/day | 3519/day | 130.7 | 10556 | graphhopper | Avg High: 61.4°F, Low: 24.7°F (wikipedia) |  |

</details>

---

### Alternative 1
**Feasible**: No ❌
- **Start Date**: 2026-12-19
- **Total Distance**: 2500.9 miles
- **Distance Source**: graphhopper
- **Total Climbing**: 116207 ft
- **Violated Constraints**:
  - [INFEASIBLE_WEATHER_MIN_LOW] at Harrisburg, Pennsylvania on 2027-01-26: observed 23.0 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Harrisburg, Pennsylvania.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Harrisburg, Pennsylvania on 2027-01-27: observed 23.0 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Harrisburg, Pennsylvania.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Harrisburg, Pennsylvania on 2027-01-28: observed 23.0 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Harrisburg, Pennsylvania.

<details>
<summary>Click to view daily travel schedule</summary>

ROUTE INFEASIBLE


</details>

---

### Alternative 2
**Feasible**: Yes
- **Start Date**: 2027-01-16
- **Total Distance**: 2500.9 miles
- **Distance Source**: graphhopper
- **Total Climbing**: 116207 ft
- **Desirability Scores**:
  - Weather Preference: 0.693
  - Distance Score: 0.561
  - Climbing Score: 1.000
  - **Total Desirability Score**: 0.730

<details>
<summary>Click to view daily travel schedule</summary>

| Start Date | End Date | Days | Origin | Destination | Distance (mi/day) | Ascent (ft/day) | Leg Distance (mi) | Leg Ascent (ft) | Distance Source | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2027-01-16 | 2027-01-24 | 9 | Austin, Texas | Baton Rouge, Louisiana | 64.5/day | 1974/day | 580.1 | 17769 | graphhopper | Avg High: 77.5°F, Low: 41.6°F (wikipedia) |  |
| 2027-01-25 | 2027-01-27 | 3 | Baton Rouge, Louisiana | Jackson, Mississippi | 57.6/day | 2527/day | 172.8 | 7581 | graphhopper | Avg High: 75.2°F, Low: 36.6°F (wikipedia) |  |
| 2027-01-28 | 2027-01-31 | 4 | Jackson, Mississippi | Montgomery, Alabama | 67.6/day | 3054/day | 270.3 | 12216 | graphhopper | Avg High: 75.6°F, Low: 36.5°F (wikipedia) |  |
| 2027-02-01 | 2027-02-04 | 4 | Montgomery, Alabama | Tallahassee, Florida | 55.5/day | 2540/day | 222.0 | 10161 | graphhopper | Avg High: 80.4°F, Low: 43.5°F (wikipedia) |  |
| 2027-02-05 | 2027-02-09 | 5 | Tallahassee, Florida | Atlanta, Georgia | 63.0/day | 2864/day | 315.0 | 14321 | graphhopper | Avg High: 73.5°F, Low: 38.9°F (wikipedia) |  |
| 2027-02-10 | 2027-02-13 | 4 | Atlanta, Georgia | Columbia, South Carolina | 64.1/day | 3717/day | 256.3 | 14869 | graphhopper | Avg High: 78.0°F, Low: 37.3°F (wikipedia) |  |
| 2027-02-14 | 2027-02-17 | 4 | Columbia, South Carolina | Raleigh, North Carolina | 57.8/day | 2586/day | 231.3 | 10345 | graphhopper | Avg High: 74.4°F, Low: 34.2°F (wikipedia) |  |
| 2027-02-18 | 2027-02-20 | 3 | Raleigh, North Carolina | Richmond, Virginia | 65.2/day | 3602/day | 195.7 | 10806 | graphhopper | Avg High: 72.6°F, Low: 30.4°F (wikipedia) |  |
| 2027-02-21 | 2027-02-22 | 2 | Richmond, Virginia | Washington, DC | 63.3/day | 3792/day | 126.5 | 7584 | graphhopper | Avg High: 68.1°F, Low: 31.8°F (wikipedia) |  |
| 2027-02-23 | 2027-02-25 | 3 | Washington, DC | Harrisburg, Pennsylvania | 43.6/day | 3519/day | 130.7 | 10556 | graphhopper | Avg High: 61.4°F, Low: 24.7°F (wikipedia) |  |

</details>

---

### Alternative 3
**Feasible**: Yes
- **Start Date**: 2027-01-02
- **Total Distance**: 4974.0 miles
- **Distance Source**: graphhopper
- **Total Climbing**: 222636 ft
- **Desirability Scores**:
  - Weather Preference: 0.777
  - Distance Score: 0.142
  - Climbing Score: 0.366
  - **Total Desirability Score**: 0.483

<details>
<summary>Click to view daily travel schedule</summary>

| Start Date | End Date | Days | Origin | Destination | Distance (mi/day) | Ascent (ft/day) | Leg Distance (mi) | Leg Ascent (ft) | Distance Source | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2027-01-02 | 2027-01-17 | 16 | Austin, Texas | Atlanta, Georgia | 68.7/day | 2966/day | 1099.5 | 47452 | graphhopper | Avg High: 70.3°F, Low: 35.6°F (wikipedia) |  |
| 2027-01-18 | 2027-01-21 | 4 | Atlanta, Georgia | Columbia, South Carolina | 64.1/day | 3717/day | 256.3 | 14869 | graphhopper | Avg High: 74.5°F, Low: 34.6°F (wikipedia) |  |
| 2027-01-22 | 2027-01-28 | 7 | Columbia, South Carolina | Richmond, Virginia | 60.2/day | 2990/day | 421.2 | 20928 | graphhopper | Avg High: 70.1°F, Low: 28.8°F (wikipedia) |  |
| 2027-01-29 | 2027-01-30 | 2 | Richmond, Virginia | Washington, DC | 63.3/day | 3792/day | 126.5 | 7584 | graphhopper | Avg High: 66.7°F, Low: 30.1°F (wikipedia) |  |
| 2027-01-31 | 2027-02-04 | 5 | Washington, DC | Raleigh, North Carolina | 62.9/day | 3629/day | 314.6 | 18143 | graphhopper | Avg High: 71.9-74.4°F, Low: 31.8-34.2°F (wikipedia) |  |
| 2027-02-05 | 2027-02-14 | 10 | Raleigh, North Carolina | Montgomery, Alabama | 67.6/day | 2543/day | 675.5 | 25430 | graphhopper | Avg High: 78.8°F, Low: 40.4°F (wikipedia) |  |
| 2027-02-15 | 2027-02-18 | 4 | Montgomery, Alabama | Jackson, Mississippi | 69.8/day | 2986/day | 279.0 | 11944 | graphhopper | Avg High: 78.6°F, Low: 39.8°F (wikipedia) |  |
| 2027-02-19 | 2027-02-21 | 3 | Jackson, Mississippi | Baton Rouge, Louisiana | 57.6/day | 2454/day | 172.9 | 7362 | graphhopper | Avg High: 80.3°F, Low: 45.3°F (wikipedia) |  |
| 2027-02-22 | 2027-03-01 | 8 | Baton Rouge, Louisiana | Tallahassee, Florida | 65.5/day | 2252/day | 524.0 | 18020 | graphhopper | Avg High: 80.4-86.0°F, Low: 43.5-48.6°F (wikipedia) |  |
| 2027-03-02 | 2027-03-17 | 16 | Tallahassee, Florida | Harrisburg, Pennsylvania | 69.0/day | 3181/day | 1104.5 | 50903 | graphhopper | Avg High: 72.7°F, Low: 32.3°F (wikipedia) |  |

</details>

---

### Alternative 4
**Feasible**: Yes
- **Start Date**: 2027-01-02
- **Total Distance**: 4902.8 miles
- **Distance Source**: graphhopper
- **Total Climbing**: 230284 ft
- **Desirability Scores**:
  - Weather Preference: 0.772
  - Distance Score: 0.146
  - Climbing Score: 0.320
  - **Total Desirability Score**: 0.471

<details>
<summary>Click to view daily travel schedule</summary>

| Start Date | End Date | Days | Origin | Destination | Distance (mi/day) | Ascent (ft/day) | Leg Distance (mi) | Leg Ascent (ft) | Distance Source | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2027-01-02 | 2027-01-17 | 16 | Austin, Texas | Atlanta, Georgia | 68.7/day | 2966/day | 1099.5 | 47452 | graphhopper | Avg High: 70.3°F, Low: 35.6°F (wikipedia) |  |
| 2027-01-18 | 2027-01-24 | 7 | Atlanta, Georgia | Raleigh, North Carolina | 68.6/day | 4304/day | 480.1 | 30128 | graphhopper | Avg High: 71.9°F, Low: 31.8°F (wikipedia) |  |
| 2027-01-25 | 2027-01-27 | 3 | Raleigh, North Carolina | Richmond, Virginia | 65.2/day | 3602/day | 195.7 | 10806 | graphhopper | Avg High: 70.1°F, Low: 28.8°F (wikipedia) |  |
| 2027-01-28 | 2027-01-29 | 2 | Richmond, Virginia | Washington, DC | 63.3/day | 3792/day | 126.5 | 7584 | graphhopper | Avg High: 66.7°F, Low: 30.1°F (wikipedia) |  |
| 2027-01-30 | 2027-02-06 | 8 | Washington, DC | Columbia, South Carolina | 67.1/day | 3437/day | 536.7 | 27494 | graphhopper | Avg High: 74.5-78.0°F, Low: 34.6-37.3°F (wikipedia) |  |
| 2027-02-07 | 2027-02-12 | 6 | Columbia, South Carolina | Montgomery, Alabama | 64.0/day | 3098/day | 383.8 | 18590 | graphhopper | Avg High: 78.8°F, Low: 40.4°F (wikipedia) |  |
| 2027-02-13 | 2027-02-16 | 4 | Montgomery, Alabama | Jackson, Mississippi | 69.8/day | 2986/day | 279.0 | 11944 | graphhopper | Avg High: 78.6°F, Low: 39.8°F (wikipedia) |  |
| 2027-02-17 | 2027-02-19 | 3 | Jackson, Mississippi | Baton Rouge, Louisiana | 57.6/day | 2454/day | 172.9 | 7362 | graphhopper | Avg High: 80.3°F, Low: 45.3°F (wikipedia) |  |
| 2027-02-20 | 2027-02-27 | 8 | Baton Rouge, Louisiana | Tallahassee, Florida | 65.5/day | 2252/day | 524.0 | 18020 | graphhopper | Avg High: 80.4°F, Low: 43.5°F (wikipedia) |  |
| 2027-02-28 | 2027-03-15 | 16 | Tallahassee, Florida | Harrisburg, Pennsylvania | 69.0/day | 3181/day | 1104.5 | 50903 | graphhopper | Avg High: 61.4-72.7°F, Low: 24.7-32.3°F (wikipedia) |  |

</details>

---

### Alternative 5
**Feasible**: Yes
- **Start Date**: 2026-12-19
- **Total Distance**: 4974.0 miles
- **Distance Source**: graphhopper
- **Total Climbing**: 222636 ft
- **Desirability Scores**:
  - Weather Preference: 0.747
  - Distance Score: 0.142
  - Climbing Score: 0.366
  - **Total Desirability Score**: 0.470

<details>
<summary>Click to view daily travel schedule</summary>

| Start Date | End Date | Days | Origin | Destination | Distance (mi/day) | Ascent (ft/day) | Leg Distance (mi) | Leg Ascent (ft) | Distance Source | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-12-19 | 2027-01-03 | 16 | Austin, Texas | Atlanta, Georgia | 68.7/day | 2966/day | 1099.5 | 47452 | graphhopper | Avg High: 70.3-71.5°F, Low: 35.6-38.4°F (wikipedia) |  |
| 2027-01-04 | 2027-01-07 | 4 | Atlanta, Georgia | Columbia, South Carolina | 64.1/day | 3717/day | 256.3 | 14869 | graphhopper | Avg High: 74.5°F, Low: 34.6°F (wikipedia) |  |
| 2027-01-08 | 2027-01-14 | 7 | Columbia, South Carolina | Richmond, Virginia | 60.2/day | 2990/day | 421.2 | 20928 | graphhopper | Avg High: 70.1°F, Low: 28.8°F (wikipedia) |  |
| 2027-01-15 | 2027-01-16 | 2 | Richmond, Virginia | Washington, DC | 63.3/day | 3792/day | 126.5 | 7584 | graphhopper | Avg High: 66.7°F, Low: 30.1°F (wikipedia) |  |
| 2027-01-17 | 2027-01-21 | 5 | Washington, DC | Raleigh, North Carolina | 62.9/day | 3629/day | 314.6 | 18143 | graphhopper | Avg High: 71.9°F, Low: 31.8°F (wikipedia) |  |
| 2027-01-22 | 2027-01-31 | 10 | Raleigh, North Carolina | Montgomery, Alabama | 67.6/day | 2543/day | 675.5 | 25430 | graphhopper | Avg High: 75.6°F, Low: 36.5°F (wikipedia) |  |
| 2027-02-01 | 2027-02-04 | 4 | Montgomery, Alabama | Jackson, Mississippi | 69.8/day | 2986/day | 279.0 | 11944 | graphhopper | Avg High: 78.6°F, Low: 39.8°F (wikipedia) |  |
| 2027-02-05 | 2027-02-07 | 3 | Jackson, Mississippi | Baton Rouge, Louisiana | 57.6/day | 2454/day | 172.9 | 7362 | graphhopper | Avg High: 80.3°F, Low: 45.3°F (wikipedia) |  |
| 2027-02-08 | 2027-02-15 | 8 | Baton Rouge, Louisiana | Tallahassee, Florida | 65.5/day | 2252/day | 524.0 | 18020 | graphhopper | Avg High: 80.4°F, Low: 43.5°F (wikipedia) |  |
| 2027-02-16 | 2027-03-03 | 16 | Tallahassee, Florida | Harrisburg, Pennsylvania | 69.0/day | 3181/day | 1104.5 | 50903 | graphhopper | Avg High: 61.4-72.7°F, Low: 24.7-32.3°F (wikipedia) |  |

</details>

---

### Alternative 6
**Feasible**: Yes
- **Start Date**: 2026-12-19
- **Total Distance**: 4886.3 miles
- **Distance Source**: graphhopper
- **Total Climbing**: 230433 ft
- **Desirability Scores**:
  - Weather Preference: 0.757
  - Distance Score: 0.147
  - Climbing Score: 0.319
  - **Total Desirability Score**: 0.464

<details>
<summary>Click to view daily travel schedule</summary>

| Start Date | End Date | Days | Origin | Destination | Distance (mi/day) | Ascent (ft/day) | Leg Distance (mi) | Leg Ascent (ft) | Distance Source | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-12-19 | 2027-01-03 | 16 | Austin, Texas | Atlanta, Georgia | 68.7/day | 2966/day | 1099.5 | 47452 | graphhopper | Avg High: 70.3-71.5°F, Low: 35.6-38.4°F (wikipedia) |  |
| 2027-01-04 | 2027-01-13 | 10 | Atlanta, Georgia | Richmond, Virginia | 65.0/day | 4009/day | 649.8 | 40092 | graphhopper | Avg High: 70.1°F, Low: 28.8°F (wikipedia) |  |
| 2027-01-14 | 2027-01-15 | 2 | Richmond, Virginia | Washington, DC | 63.3/day | 3792/day | 126.5 | 7584 | graphhopper | Avg High: 66.7°F, Low: 30.1°F (wikipedia) |  |
| 2027-01-16 | 2027-01-20 | 5 | Washington, DC | Raleigh, North Carolina | 62.9/day | 3629/day | 314.6 | 18143 | graphhopper | Avg High: 71.9°F, Low: 31.8°F (wikipedia) |  |
| 2027-01-21 | 2027-01-24 | 4 | Raleigh, North Carolina | Columbia, South Carolina | 57.9/day | 2585/day | 231.6 | 10341 | graphhopper | Avg High: 74.5°F, Low: 34.6°F (wikipedia) |  |
| 2027-01-25 | 2027-01-30 | 6 | Columbia, South Carolina | Montgomery, Alabama | 64.0/day | 3098/day | 383.8 | 18590 | graphhopper | Avg High: 75.6°F, Low: 36.5°F (wikipedia) |  |
| 2027-01-31 | 2027-02-03 | 4 | Montgomery, Alabama | Jackson, Mississippi | 69.8/day | 2986/day | 279.0 | 11944 | graphhopper | Avg High: 75.2-78.6°F, Low: 36.6-39.8°F (wikipedia) |  |
| 2027-02-04 | 2027-02-06 | 3 | Jackson, Mississippi | Baton Rouge, Louisiana | 57.6/day | 2454/day | 172.9 | 7362 | graphhopper | Avg High: 80.3°F, Low: 45.3°F (wikipedia) |  |
| 2027-02-07 | 2027-02-14 | 8 | Baton Rouge, Louisiana | Tallahassee, Florida | 65.5/day | 2252/day | 524.0 | 18020 | graphhopper | Avg High: 80.4°F, Low: 43.5°F (wikipedia) |  |
| 2027-02-15 | 2027-03-02 | 16 | Tallahassee, Florida | Harrisburg, Pennsylvania | 69.0/day | 3181/day | 1104.5 | 50903 | graphhopper | Avg High: 61.4-72.7°F, Low: 24.7-32.3°F (wikipedia) |  |

</details>

---

## Data Attribution
- Routing and elevation data powered by [GraphHopper](https://www.graphhopper.com/) using [OpenStreetMap](https://www.openstreetmap.org/copyright) data licensed under [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/).


