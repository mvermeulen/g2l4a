# Route Recommendations Comparison

## Overview Comparison
| Option | Start Date | Feasible? | Total Score | Weather Score | Distance Score | Hills Score | Total Distance | Distance Source | Total Climb | Key Difference |
|---|---|---|---|---|---|---|---|---|---|---|
| **Best Recommendation** | 2027-02-15 | No ❌ | N/A | N/A | N/A | N/A | 4880.0 mi | graphhopper | 262682 ft | Baseline / Optimal Route |
| Alternative 1 | 2027-03-01 | No ❌ | N/A | N/A | N/A | N/A | 4880.0 mi | graphhopper | 262682 ft | Different start date (2027-03-01), same sequence |
| Alternative 2 | 2027-03-15 | Yes | 0.6553 | 0.5242 | 0.5545 | 1.0000 | 4880.0 mi | graphhopper | 262682 ft | Different start date (2027-03-15), same sequence |
| Alternative 3 | 2027-02-15 | Yes | 0.4787 | 0.6817 | 0.2828 | 0.5079 | 6833.7 mi | graphhopper | 362377 ft | Alternative via-city sequence, same date |
| Alternative 4 | 2027-02-15 | Yes | 0.4615 | 0.6723 | 0.2699 | 0.4729 | 6995.2 mi | graphhopper | 369458 ft | Alternative via-city sequence, same date |
| Alternative 5 | 2027-02-15 | Yes | 0.4580 | 0.6621 | 0.2755 | 0.4643 | 6923.8 mi | graphhopper | 371196 ft | Alternative via-city sequence, same date |
| Alternative 6 | 2027-02-15 | Yes | 0.4467 | 0.6493 | 0.2624 | 0.4578 | 7094.6 mi | graphhopper | 372522 ft | Alternative via-city sequence, same date |

## Detailed Recommendations
### Best Recommendation
**Feasible**: No ❌
- **Start Date**: 2027-02-15
- **Total Distance**: 4880.0 miles (4645.1 mi paved, 234.9 mi gravel)
- **Distance Source**: graphhopper
- **Total Climbing**: 262682 ft
- **Violated Constraints**:
  - [INFEASIBLE_WEATHER_MIN_LOW] at Jefferson City, Missouri on 2027-02-28: observed 21.8 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Jefferson City, Missouri.

<details>
<summary>Click to view daily travel schedule</summary>

ROUTE INFEASIBLE


</details>

---

### Alternative 1
**Feasible**: No ❌
- **Start Date**: 2027-03-01
- **Total Distance**: 4880.0 miles (4645.1 mi paved, 234.9 mi gravel)
- **Distance Source**: graphhopper
- **Total Climbing**: 262682 ft
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

### Alternative 2
**Feasible**: Yes
- **Start Date**: 2027-03-15
- **Total Distance**: 4880.0 miles (4645.1 mi paved, 234.9 mi gravel)
- **Distance Source**: graphhopper
- **Total Climbing**: 262682 ft
- **Desirability Scores**:
  - Weather Preference: 0.524
  - Distance Score: 0.554
  - Climbing Score: 1.000
  - **Total Desirability Score**: 0.655

<details>
<summary>Click to view daily travel schedule</summary>

| Start Date | End Date | Days | Origin | Destination | Distance (mi/day) | Ascent (ft/day) | Leg Distance (mi) | Leg Ascent (ft) | Distance Source | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2027-03-15 | 2027-03-21 | 7 | Austin, Texas | Oklahoma City, Oklahoma | 64.7/day | 2429/day | 452.9 mi (446.9 mi paved, 6.0 mi gravel) | 17000 | graphhopper | Avg High: 56.3-79.9°F, Low: 34.5-49.3°F (open-meteo) |  |
| 2027-03-22 | 2027-03-27 | 6 | Oklahoma City, Oklahoma | Topeka, Kansas | 62.4/day | 2085/day | 374.5 mi (356.5 mi paved, 18.0 mi gravel) | 12509 | graphhopper | Avg High: 52.1-74.9°F, Low: 33.0-52.3°F (open-meteo) |  |
| 2027-03-28 | 2027-03-31 | 4 | Topeka, Kansas | Jefferson City, Missouri | 57.7/day | 2910/day | 230.9 mi (167.1 mi paved, 63.9 mi gravel) | 11638 | graphhopper | Avg High: 57.0-78.6°F, Low: 37.3-47.8°F (open-meteo) |  |
| 2027-04-01 | 2027-04-05 | 5 | Jefferson City, Missouri | Little Rock, Arkansas | 68.5/day | 4982/day | 342.5 mi (311.5 mi paved, 31.1 mi gravel) | 24909 | graphhopper | Avg High: 56.0-72.5°F, Low: 37.7-52.4°F (open-meteo) |  |
| 2027-04-06 | 2027-04-10 | 5 | Little Rock, Arkansas | Jackson, Mississippi | 66.7/day | 1539/day | 333.4 mi (306.7 mi paved, 26.6 mi gravel) | 7693 | graphhopper | Avg High: 74.2-82.9°F, Low: 46.5-63.7°F (open-meteo) |  |
| 2027-04-11 | 2027-04-13 | 3 | Jackson, Mississippi | Baton Rouge, Louisiana | 57.6/day | 2454/day | 172.9 mi (172.9 mi paved) | 7362 | graphhopper | Avg High: 82.0-85.3°F, Low: 57.2-64.8°F (open-meteo) |  |
| 2027-04-14 | 2027-04-19 | 6 | Baton Rouge, Louisiana | Montgomery, Alabama | 68.3/day | 2882/day | 409.9 mi (409.9 mi paved) | 17294 | graphhopper | Avg High: 76.4-83.1°F, Low: 49.5-65.9°F (open-meteo) |  |
| 2027-04-20 | 2027-04-23 | 4 | Montgomery, Alabama | Tallahassee, Florida | 55.5/day | 2540/day | 222.0 mi (212.2 mi paved, 9.8 mi gravel) | 10161 | graphhopper | Avg High: 79.6-84.7°F, Low: 63.5-73.2°F (open-meteo) |  |
| 2027-04-24 | 2027-04-28 | 5 | Tallahassee, Florida | Atlanta, Georgia | 63.0/day | 2864/day | 315.0 mi (302.6 mi paved, 12.4 mi gravel) | 14321 | graphhopper | Avg High: 71.2-77.7°F, Low: 46.0-56.9°F (open-meteo) |  |
| 2027-04-29 | 2027-05-03 | 5 | Atlanta, Georgia | Nashville, Tennessee | 58.6/day | 3589/day | 293.2 mi (293.2 mi paved) | 17944 | graphhopper | Avg High: 61.0-83.5°F, Low: 43.0-64.2°F (open-meteo) |  |
| 2027-05-04 | 2027-05-07 | 4 | Nashville, Tennessee | Frankfort, Kentucky | 57.1/day | 3572/day | 228.5 mi (228.5 mi paved) | 14287 | graphhopper | Avg High: 56.3-78.3°F, Low: 37.0-51.7°F (open-meteo) |  |
| 2027-05-08 | 2027-05-11 | 4 | Frankfort, Kentucky | Charleston, West Virginia | 64.1/day | 4912/day | 256.4 mi (256.0 mi paved, 0.3 mi gravel) | 19646 | graphhopper | Avg High: 79.3-87.7°F, Low: 53.6-65.4°F (open-meteo) |  |
| 2027-05-12 | 2027-05-19 | 8 | Charleston, West Virginia | Columbia, South Carolina | 54.3/day | 4823/day | 434.7 mi (422.3 mi paved, 12.3 mi gravel) | 38581 | graphhopper | Avg High: 76.2-88.0°F, Low: 60.0-68.5°F (open-meteo) |  |
| 2027-05-20 | 2027-05-23 | 4 | Columbia, South Carolina | Raleigh, North Carolina | 57.8/day | 2586/day | 231.3 mi (231.3 mi paved) | 10345 | graphhopper | Avg High: 76.6-80.6°F, Low: 53.5-70.1°F (open-meteo) |  |
| 2027-05-24 | 2027-05-26 | 3 | Raleigh, North Carolina | Richmond, Virginia | 65.2/day | 3602/day | 195.7 mi (195.7 mi paved) | 10806 | graphhopper | Avg High: 86.3-89.9°F, Low: 58.6-66.5°F (open-meteo) |  |
| 2027-05-27 | 2027-05-30 | 4 | Richmond, Virginia | Harrisburg, Pennsylvania | 64.2/day | 4515/day | 257.0 mi (239.8 mi paved, 17.2 mi gravel) | 18058 | graphhopper | Avg High: 78.4-83.5°F, Low: 58.3-70.3°F (open-meteo) |  |
| 2027-05-31 | 2027-06-02 | 3 | Harrisburg, Pennsylvania | Washington, DC | 43.1/day | 3376/day | 129.2 mi (116.6 mi paved, 12.6 mi gravel) | 10127 | graphhopper | Avg High: 79.2-82.4°F, Low: 57.4-72.5°F (open-meteo) |  |

</details>

---

### Alternative 3
**Feasible**: Yes
- **Start Date**: 2027-02-15
- **Total Distance**: 6833.7 miles (6457.1 mi paved, 376.6 mi gravel)
- **Distance Source**: graphhopper
- **Total Climbing**: 362377 ft
- **Desirability Scores**:
  - Weather Preference: 0.682
  - Distance Score: 0.283
  - Climbing Score: 0.508
  - **Total Desirability Score**: 0.479

<details>
<summary>Click to view daily travel schedule</summary>

| Start Date | End Date | Days | Origin | Destination | Distance (mi/day) | Ascent (ft/day) | Leg Distance (mi) | Leg Ascent (ft) | Distance Source | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2027-02-15 | 2027-02-23 | 9 | Austin, Texas | Little Rock, Arkansas | 63.5/day | 2357/day | 571.6 mi (490.4 mi paved, 81.1 mi gravel) | 21211 | graphhopper | Avg High: 57.3-74.1°F, Low: 41.0-60.1°F (open-meteo) |  |
| 2027-02-24 | 2027-03-01 | 6 | Little Rock, Arkansas | Oklahoma City, Oklahoma | 62.5/day | 3322/day | 375.0 mi (332.8 mi paved, 42.3 mi gravel) | 19932 | graphhopper | Avg High: 52.6-69.2°F, Low: 34.0-54.8°F (open-meteo) |  |
| 2027-03-02 | 2027-03-17 | 16 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8/day | 2863/day | 1100.3 mi (1052.2 mi paved, 48.1 mi gravel) | 45810 | graphhopper | Avg High: 53.9-77.6°F, Low: 33.1-68.3°F (open-meteo) |  |
| 2027-03-18 | 2027-03-25 | 8 | Tallahassee, Florida | Baton Rouge, Louisiana | 65.5/day | 2248/day | 523.9 mi (523.9 mi paved) | 17982 | graphhopper | Avg High: 62.7-74.4°F, Low: 37.6-58.6°F (open-meteo) |  |
| 2027-03-26 | 2027-03-28 | 3 | Baton Rouge, Louisiana | Jackson, Mississippi | 57.6/day | 2527/day | 172.8 mi (172.8 mi paved) | 7581 | graphhopper | Avg High: 70.7-72.7°F, Low: 43.6-55.6°F (open-meteo) |  |
| 2027-03-29 | 2027-04-01 | 4 | Jackson, Mississippi | Montgomery, Alabama | 67.6/day | 3054/day | 270.3 mi (253.8 mi paved, 16.5 mi gravel) | 12216 | graphhopper | Avg High: 74.4-75.5°F, Low: 49.8-69.3°F (open-meteo) |  |
| 2027-04-02 | 2027-04-04 | 3 | Montgomery, Alabama | Atlanta, Georgia | 66.4/day | 3698/day | 199.3 mi (199.3 mi paved) | 11095 | graphhopper | Avg High: 61.5-64.0°F, Low: 48.1-57.8°F (open-meteo) |  |
| 2027-04-05 | 2027-04-08 | 4 | Atlanta, Georgia | Columbia, South Carolina | 64.1/day | 3717/day | 256.3 mi (249.5 mi paved, 6.8 mi gravel) | 14869 | graphhopper | Avg High: 66.4-83.2°F, Low: 47.7-70.6°F (open-meteo) |  |
| 2027-04-09 | 2027-04-12 | 4 | Columbia, South Carolina | Raleigh, North Carolina | 57.8/day | 2586/day | 231.3 mi (231.3 mi paved) | 10345 | graphhopper | Avg High: 71.4-84.2°F, Low: 41.5-53.8°F (open-meteo) |  |
| 2027-04-13 | 2027-04-15 | 3 | Raleigh, North Carolina | Richmond, Virginia | 65.2/day | 3602/day | 195.7 mi (195.7 mi paved) | 10806 | graphhopper | Avg High: 67.8-81.8°F, Low: 52.5-60.3°F (open-meteo) |  |
| 2027-04-16 | 2027-04-24 | 9 | Richmond, Virginia | Charleston, West Virginia | 42.2/day | 4494/day | 380.0 mi (333.8 mi paved, 46.2 mi gravel) | 40442 | graphhopper | Avg High: 68.3-79.0°F, Low: 37.1-66.3°F (open-meteo) |  |
| 2027-04-25 | 2027-04-28 | 4 | Charleston, West Virginia | Frankfort, Kentucky | 63.9/day | 4850/day | 255.7 mi (255.3 mi paved, 0.3 mi gravel) | 19398 | graphhopper | Avg High: 69.1-71.2°F, Low: 42.9-57.3°F (open-meteo) |  |
| 2027-04-29 | 2027-05-02 | 4 | Frankfort, Kentucky | Nashville, Tennessee | 57.0/day | 3529/day | 227.8 mi (227.8 mi paved) | 14115 | graphhopper | Avg High: 77.2-83.5°F, Low: 51.2-64.2°F (open-meteo) |  |
| 2027-05-03 | 2027-05-09 | 7 | Nashville, Tennessee | Jefferson City, Missouri | 65.9/day | 4236/day | 461.2 mi (416.9 mi paved, 44.3 mi gravel) | 29655 | graphhopper | Avg High: 53.1-85.0°F, Low: 34.3-57.6°F (open-meteo) |  |
| 2027-05-10 | 2027-05-13 | 4 | Jefferson City, Missouri | Topeka, Kansas | 58.1/day | 3041/day | 232.4 mi (167.7 mi paved, 64.7 mi gravel) | 12165 | graphhopper | Avg High: 72.3-88.8°F, Low: 56.1-65.5°F (open-meteo) |  |
| 2027-05-14 | 2027-05-31 | 18 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5/day | 3591/day | 1250.8 mi (1214.1 mi paved, 36.8 mi gravel) | 64629 | graphhopper | Avg High: 59.9-84.8°F, Low: 45.2-70.3°F (open-meteo) |  |
| 2027-06-01 | 2027-06-03 | 3 | Harrisburg, Pennsylvania | Washington, DC | 43.1/day | 3376/day | 129.2 mi (116.6 mi paved, 12.6 mi gravel) | 10127 | graphhopper | Avg High: 79.2-82.2°F, Low: 54.1-66.2°F (open-meteo) |  |

</details>

---

### Alternative 4
**Feasible**: Yes
- **Start Date**: 2027-02-15
- **Total Distance**: 6995.2 miles (6638.5 mi paved, 356.8 mi gravel)
- **Distance Source**: graphhopper
- **Total Climbing**: 369458 ft
- **Desirability Scores**:
  - Weather Preference: 0.672
  - Distance Score: 0.270
  - Climbing Score: 0.473
  - **Total Desirability Score**: 0.462

<details>
<summary>Click to view daily travel schedule</summary>

| Start Date | End Date | Days | Origin | Destination | Distance (mi/day) | Ascent (ft/day) | Leg Distance (mi) | Leg Ascent (ft) | Distance Source | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2027-02-15 | 2027-02-23 | 9 | Austin, Texas | Little Rock, Arkansas | 63.5/day | 2357/day | 571.6 mi (490.4 mi paved, 81.1 mi gravel) | 21211 | graphhopper | Avg High: 57.3-74.1°F, Low: 41.0-60.1°F (open-meteo) |  |
| 2027-02-24 | 2027-03-01 | 6 | Little Rock, Arkansas | Oklahoma City, Oklahoma | 62.5/day | 3322/day | 375.0 mi (332.8 mi paved, 42.3 mi gravel) | 19932 | graphhopper | Avg High: 52.6-69.2°F, Low: 34.0-54.8°F (open-meteo) |  |
| 2027-03-02 | 2027-03-17 | 16 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8/day | 2863/day | 1100.3 mi (1052.2 mi paved, 48.1 mi gravel) | 45810 | graphhopper | Avg High: 53.9-77.6°F, Low: 33.1-68.3°F (open-meteo) |  |
| 2027-03-18 | 2027-03-25 | 8 | Tallahassee, Florida | Baton Rouge, Louisiana | 65.5/day | 2248/day | 523.9 mi (523.9 mi paved) | 17982 | graphhopper | Avg High: 62.7-74.4°F, Low: 37.6-58.6°F (open-meteo) |  |
| 2027-03-26 | 2027-03-28 | 3 | Baton Rouge, Louisiana | Jackson, Mississippi | 57.6/day | 2527/day | 172.8 mi (172.8 mi paved) | 7581 | graphhopper | Avg High: 70.7-72.7°F, Low: 43.6-55.6°F (open-meteo) |  |
| 2027-03-29 | 2027-04-01 | 4 | Jackson, Mississippi | Montgomery, Alabama | 67.6/day | 3054/day | 270.3 mi (253.8 mi paved, 16.5 mi gravel) | 12216 | graphhopper | Avg High: 74.4-75.5°F, Low: 49.8-69.3°F (open-meteo) |  |
| 2027-04-02 | 2027-04-04 | 3 | Montgomery, Alabama | Atlanta, Georgia | 66.4/day | 3698/day | 199.3 mi (199.3 mi paved) | 11095 | graphhopper | Avg High: 61.5-64.0°F, Low: 48.1-57.8°F (open-meteo) |  |
| 2027-04-05 | 2027-04-08 | 4 | Atlanta, Georgia | Columbia, South Carolina | 64.1/day | 3717/day | 256.3 mi (249.5 mi paved, 6.8 mi gravel) | 14869 | graphhopper | Avg High: 66.4-83.2°F, Low: 47.7-70.6°F (open-meteo) |  |
| 2027-04-09 | 2027-04-15 | 7 | Columbia, South Carolina | Richmond, Virginia | 60.2/day | 2990/day | 421.2 mi (415.4 mi paved, 5.8 mi gravel) | 20928 | graphhopper | Avg High: 66.4-88.4°F, Low: 39.4-60.3°F (open-meteo) |  |
| 2027-04-16 | 2027-04-18 | 3 | Richmond, Virginia | Raleigh, North Carolina | 65.5/day | 3717/day | 196.4 mi (196.4 mi paved) | 11151 | graphhopper | Avg High: 69.3-75.4°F, Low: 44.1-53.6°F (open-meteo) |  |
| 2027-04-19 | 2027-04-26 | 8 | Raleigh, North Carolina | Charleston, West Virginia | 43.9/day | 4574/day | 351.1 mi (336.5 mi paved, 14.6 mi gravel) | 36594 | graphhopper | Avg High: 66.2-77.3°F, Low: 54.5-66.3°F (open-meteo) |  |
| 2027-04-27 | 2027-04-30 | 4 | Charleston, West Virginia | Frankfort, Kentucky | 63.9/day | 4850/day | 255.7 mi (255.3 mi paved, 0.3 mi gravel) | 19398 | graphhopper | Avg High: 69.1-84.1°F, Low: 42.9-60.0°F (open-meteo) |  |
| 2027-05-01 | 2027-05-04 | 4 | Frankfort, Kentucky | Nashville, Tennessee | 57.0/day | 3529/day | 227.8 mi (227.8 mi paved) | 14115 | graphhopper | Avg High: 57.1-78.1°F, Low: 37.4-64.2°F (open-meteo) |  |
| 2027-05-05 | 2027-05-11 | 7 | Nashville, Tennessee | Jefferson City, Missouri | 65.9/day | 4236/day | 461.2 mi (416.9 mi paved, 44.3 mi gravel) | 29655 | graphhopper | Avg High: 69.8-87.3°F, Low: 40.2-66.4°F (open-meteo) |  |
| 2027-05-12 | 2027-05-15 | 4 | Jefferson City, Missouri | Topeka, Kansas | 58.1/day | 3041/day | 232.4 mi (167.7 mi paved, 64.7 mi gravel) | 12165 | graphhopper | Avg High: 72.3-87.0°F, Low: 56.1-63.8°F (open-meteo) |  |
| 2027-05-16 | 2027-06-02 | 18 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5/day | 3591/day | 1250.8 mi (1214.1 mi paved, 36.8 mi gravel) | 64629 | graphhopper | Avg High: 59.9-84.8°F, Low: 45.2-70.3°F (open-meteo) |  |
| 2027-06-03 | 2027-06-05 | 3 | Harrisburg, Pennsylvania | Washington, DC | 43.1/day | 3376/day | 129.2 mi (116.6 mi paved, 12.6 mi gravel) | 10127 | graphhopper | Avg High: 79.2-89.0°F, Low: 54.1-71.2°F (open-meteo) |  |

</details>

---

### Alternative 5
**Feasible**: Yes
- **Start Date**: 2027-02-15
- **Total Distance**: 6923.8 miles (6463.8 mi paved, 460.0 mi gravel)
- **Distance Source**: graphhopper
- **Total Climbing**: 371196 ft
- **Desirability Scores**:
  - Weather Preference: 0.662
  - Distance Score: 0.276
  - Climbing Score: 0.464
  - **Total Desirability Score**: 0.458

<details>
<summary>Click to view daily travel schedule</summary>

| Start Date | End Date | Days | Origin | Destination | Distance (mi/day) | Ascent (ft/day) | Leg Distance (mi) | Leg Ascent (ft) | Distance Source | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2027-02-15 | 2027-02-23 | 9 | Austin, Texas | Little Rock, Arkansas | 63.5/day | 2357/day | 571.6 mi (490.4 mi paved, 81.1 mi gravel) | 21211 | graphhopper | Avg High: 57.3-74.1°F, Low: 41.0-60.1°F (open-meteo) |  |
| 2027-02-24 | 2027-03-01 | 6 | Little Rock, Arkansas | Oklahoma City, Oklahoma | 62.5/day | 3322/day | 375.0 mi (332.8 mi paved, 42.3 mi gravel) | 19932 | graphhopper | Avg High: 52.6-69.2°F, Low: 34.0-54.8°F (open-meteo) |  |
| 2027-03-02 | 2027-03-17 | 16 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8/day | 2863/day | 1100.3 mi (1052.2 mi paved, 48.1 mi gravel) | 45810 | graphhopper | Avg High: 53.9-77.6°F, Low: 33.1-68.3°F (open-meteo) |  |
| 2027-03-18 | 2027-03-25 | 8 | Tallahassee, Florida | Baton Rouge, Louisiana | 65.5/day | 2248/day | 523.9 mi (523.9 mi paved) | 17982 | graphhopper | Avg High: 62.7-74.4°F, Low: 37.6-58.6°F (open-meteo) |  |
| 2027-03-26 | 2027-03-28 | 3 | Baton Rouge, Louisiana | Jackson, Mississippi | 57.6/day | 2527/day | 172.8 mi (172.8 mi paved) | 7581 | graphhopper | Avg High: 70.7-72.7°F, Low: 43.6-55.6°F (open-meteo) |  |
| 2027-03-29 | 2027-04-01 | 4 | Jackson, Mississippi | Montgomery, Alabama | 67.6/day | 3054/day | 270.3 mi (253.8 mi paved, 16.5 mi gravel) | 12216 | graphhopper | Avg High: 74.4-75.5°F, Low: 49.8-69.3°F (open-meteo) |  |
| 2027-04-02 | 2027-04-04 | 3 | Montgomery, Alabama | Atlanta, Georgia | 66.4/day | 3698/day | 199.3 mi (199.3 mi paved) | 11095 | graphhopper | Avg High: 61.5-64.0°F, Low: 48.1-57.8°F (open-meteo) |  |
| 2027-04-05 | 2027-04-08 | 4 | Atlanta, Georgia | Columbia, South Carolina | 64.1/day | 3717/day | 256.3 mi (249.5 mi paved, 6.8 mi gravel) | 14869 | graphhopper | Avg High: 66.4-83.2°F, Low: 47.7-70.6°F (open-meteo) |  |
| 2027-04-09 | 2027-04-12 | 4 | Columbia, South Carolina | Raleigh, North Carolina | 57.8/day | 2586/day | 231.3 mi (231.3 mi paved) | 10345 | graphhopper | Avg High: 71.4-84.2°F, Low: 41.5-53.8°F (open-meteo) |  |
| 2027-04-13 | 2027-04-15 | 3 | Raleigh, North Carolina | Richmond, Virginia | 65.2/day | 3602/day | 195.7 mi (195.7 mi paved) | 10806 | graphhopper | Avg High: 67.8-81.8°F, Low: 52.5-60.3°F (open-meteo) |  |
| 2027-04-16 | 2027-04-24 | 9 | Richmond, Virginia | Charleston, West Virginia | 42.2/day | 4494/day | 380.0 mi (333.8 mi paved, 46.2 mi gravel) | 40442 | graphhopper | Avg High: 68.3-79.0°F, Low: 37.1-66.3°F (open-meteo) |  |
| 2027-04-25 | 2027-04-28 | 4 | Charleston, West Virginia | Frankfort, Kentucky | 63.9/day | 4850/day | 255.7 mi (255.3 mi paved, 0.3 mi gravel) | 19398 | graphhopper | Avg High: 69.1-71.2°F, Low: 42.9-57.3°F (open-meteo) |  |
| 2027-04-29 | 2027-05-05 | 7 | Frankfort, Kentucky | Jefferson City, Missouri | 69.1/day | 3494/day | 483.6 mi (398.7 mi paved, 84.8 mi gravel) | 24455 | graphhopper | Avg High: 53.1-83.2°F, Low: 34.3-61.2°F (open-meteo) |  |
| 2027-05-06 | 2027-05-09 | 4 | Jefferson City, Missouri | Topeka, Kansas | 58.1/day | 3041/day | 232.4 mi (167.7 mi paved, 64.7 mi gravel) | 12165 | graphhopper | Avg High: 78.4-85.3°F, Low: 52.2-61.2°F (open-meteo) |  |
| 2027-05-10 | 2027-05-20 | 11 | Topeka, Kansas | Nashville, Tennessee | 66.9/day | 3199/day | 736.2 mi (650.0 mi paved, 86.2 mi gravel) | 35188 | graphhopper | Avg High: 75.6-87.4°F, Low: 59.5-72.2°F (open-meteo) |  |
| 2027-05-21 | 2027-06-01 | 12 | Nashville, Tennessee | Harrisburg, Pennsylvania | 67.5/day | 4798/day | 810.3 mi (807.5 mi paved, 2.8 mi gravel) | 57574 | graphhopper | Avg High: 72.9-84.8°F, Low: 49.4-70.3°F (open-meteo) |  |
| 2027-06-02 | 2027-06-04 | 3 | Harrisburg, Pennsylvania | Washington, DC | 43.1/day | 3376/day | 129.2 mi (116.6 mi paved, 12.6 mi gravel) | 10127 | graphhopper | Avg High: 79.2-89.0°F, Low: 54.1-61.0°F (open-meteo) |  |

</details>

---

### Alternative 6
**Feasible**: Yes
- **Start Date**: 2027-02-15
- **Total Distance**: 7094.6 miles (6671.2 mi paved, 423.4 mi gravel)
- **Distance Source**: graphhopper
- **Total Climbing**: 372522 ft
- **Desirability Scores**:
  - Weather Preference: 0.649
  - Distance Score: 0.262
  - Climbing Score: 0.458
  - **Total Desirability Score**: 0.447

<details>
<summary>Click to view daily travel schedule</summary>

| Start Date | End Date | Days | Origin | Destination | Distance (mi/day) | Ascent (ft/day) | Leg Distance (mi) | Leg Ascent (ft) | Distance Source | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2027-02-15 | 2027-02-23 | 9 | Austin, Texas | Little Rock, Arkansas | 63.5/day | 2357/day | 571.6 mi (490.4 mi paved, 81.1 mi gravel) | 21211 | graphhopper | Avg High: 57.3-74.1°F, Low: 41.0-60.1°F (open-meteo) |  |
| 2027-02-24 | 2027-03-01 | 6 | Little Rock, Arkansas | Oklahoma City, Oklahoma | 62.5/day | 3322/day | 375.0 mi (332.8 mi paved, 42.3 mi gravel) | 19932 | graphhopper | Avg High: 52.6-69.2°F, Low: 34.0-54.8°F (open-meteo) |  |
| 2027-03-02 | 2027-03-17 | 16 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8/day | 2863/day | 1100.3 mi (1052.2 mi paved, 48.1 mi gravel) | 45810 | graphhopper | Avg High: 53.9-77.6°F, Low: 33.1-68.3°F (open-meteo) |  |
| 2027-03-18 | 2027-03-25 | 8 | Tallahassee, Florida | Baton Rouge, Louisiana | 65.5/day | 2248/day | 523.9 mi (523.9 mi paved) | 17982 | graphhopper | Avg High: 62.7-74.4°F, Low: 37.6-58.6°F (open-meteo) |  |
| 2027-03-26 | 2027-03-28 | 3 | Baton Rouge, Louisiana | Jackson, Mississippi | 57.6/day | 2527/day | 172.8 mi (172.8 mi paved) | 7581 | graphhopper | Avg High: 70.7-72.7°F, Low: 43.6-55.6°F (open-meteo) |  |
| 2027-03-29 | 2027-04-01 | 4 | Jackson, Mississippi | Montgomery, Alabama | 67.6/day | 3054/day | 270.3 mi (253.8 mi paved, 16.5 mi gravel) | 12216 | graphhopper | Avg High: 74.4-75.5°F, Low: 49.8-69.3°F (open-meteo) |  |
| 2027-04-02 | 2027-04-04 | 3 | Montgomery, Alabama | Atlanta, Georgia | 66.4/day | 3698/day | 199.3 mi (199.3 mi paved) | 11095 | graphhopper | Avg High: 61.5-64.0°F, Low: 48.1-57.8°F (open-meteo) |  |
| 2027-04-05 | 2027-04-08 | 4 | Atlanta, Georgia | Columbia, South Carolina | 64.1/day | 3717/day | 256.3 mi (249.5 mi paved, 6.8 mi gravel) | 14869 | graphhopper | Avg High: 66.4-83.2°F, Low: 47.7-70.6°F (open-meteo) |  |
| 2027-04-09 | 2027-04-12 | 4 | Columbia, South Carolina | Raleigh, North Carolina | 57.8/day | 2586/day | 231.3 mi (231.3 mi paved) | 10345 | graphhopper | Avg High: 71.4-84.2°F, Low: 41.5-53.8°F (open-meteo) |  |
| 2027-04-13 | 2027-04-15 | 3 | Raleigh, North Carolina | Richmond, Virginia | 65.2/day | 3602/day | 195.7 mi (195.7 mi paved) | 10806 | graphhopper | Avg High: 67.8-81.8°F, Low: 52.5-60.3°F (open-meteo) |  |
| 2027-04-16 | 2027-04-19 | 4 | Richmond, Virginia | Harrisburg, Pennsylvania | 64.2/day | 4515/day | 257.0 mi (239.8 mi paved, 17.2 mi gravel) | 18058 | graphhopper | Avg High: 61.2-72.6°F, Low: 35.8-60.7°F (open-meteo) |  |
| 2027-04-20 | 2027-04-28 | 9 | Harrisburg, Pennsylvania | Charleston, West Virginia | 44.6/day | 4688/day | 401.1 mi (386.9 mi paved, 14.2 mi gravel) | 42195 | graphhopper | Avg High: 66.2-75.6°F, Low: 40.6-66.3°F (open-meteo) |  |
| 2027-04-29 | 2027-05-02 | 4 | Charleston, West Virginia | Frankfort, Kentucky | 63.9/day | 4850/day | 255.7 mi (255.3 mi paved, 0.3 mi gravel) | 19398 | graphhopper | Avg High: 74.3-84.1°F, Low: 51.6-60.3°F (open-meteo) |  |
| 2027-05-03 | 2027-05-06 | 4 | Frankfort, Kentucky | Nashville, Tennessee | 57.0/day | 3529/day | 227.8 mi (227.8 mi paved) | 14115 | graphhopper | Avg High: 57.1-74.6°F, Low: 35.2-43.2°F (open-meteo) |  |
| 2027-05-07 | 2027-05-17 | 11 | Nashville, Tennessee | Topeka, Kansas | 67.1/day | 3217/day | 738.5 mi (649.9 mi paved, 88.6 mi gravel) | 35389 | graphhopper | Avg High: 72.3-89.5°F, Low: 56.1-65.5°F (open-meteo) |  |
| 2027-05-18 | 2027-05-21 | 4 | Topeka, Kansas | Jefferson City, Missouri | 57.7/day | 2910/day | 230.9 mi (167.1 mi paved, 63.9 mi gravel) | 11638 | graphhopper | Avg High: 70.1-79.9°F, Low: 51.5-61.6°F (open-meteo) |  |
| 2027-05-22 | 2027-06-06 | 16 | Jefferson City, Missouri | Washington, DC | 67.9/day | 3743/day | 1087.0 mi (1023.9 mi paved, 63.2 mi gravel) | 59882 | graphhopper | Avg High: 75.5-89.0°F, Low: 51.6-72.5°F (open-meteo) |  |

</details>

---

## Data Attribution
- Weather data by [Open-Meteo.com](https://open-meteo.com/) under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Data has been transformed into itinerary-level schedule summaries.
- Routing and elevation data powered by [GraphHopper](https://www.graphhopper.com/) using [OpenStreetMap](https://www.openstreetmap.org/copyright) data licensed under [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/).


