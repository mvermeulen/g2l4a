# Route Recommendations Comparison

## Overview Comparison
| Option | Start Date | Feasible? | Total Score | Weather Score | Distance Score | Hills Score | Total Distance | Distance Source | Total Climb | Key Difference |
|---|---|---|---|---|---|---|---|---|---|---|
| **Best Recommendation** | 2027-02-15 | No ❌ | N/A | N/A | N/A | N/A | 4145.8 mi | graphhopper | 171037 ft | Baseline / Optimal Route |
| Alternative 1 | 2027-03-15 | No ❌ | N/A | N/A | N/A | N/A | 4145.8 mi | graphhopper | 171037 ft | Different start date (2027-03-15), same sequence |
| Alternative 2 | 2027-03-01 | No ❌ | N/A | N/A | N/A | N/A | 4145.8 mi | graphhopper | 171037 ft | Different start date (2027-03-01), same sequence |
| Alternative 3 | 2027-02-15 | Yes | 0.5114 | 0.6795 | 0.2808 | 0.4854 | 6857.5 mi | graphhopper | 266029 ft | Alternative via-city sequence, same date |
| Alternative 4 | 2027-03-15 | No ❌ | N/A | N/A | N/A | N/A | 6466.6 mi | graphhopper | 298637 ft | Different start date (2027-03-15) & alternative sequence |
| Alternative 5 | 2027-03-15 | No ❌ | N/A | N/A | N/A | N/A | 6646.7 mi | graphhopper | 305279 ft | Different start date (2027-03-15) & alternative sequence |
| Alternative 6 | 2027-03-15 | No ❌ | N/A | N/A | N/A | N/A | 6710.6 mi | graphhopper | 305780 ft | Different start date (2027-03-15) & alternative sequence |

## Detailed Recommendations
### Best Recommendation
**Feasible**: No ❌
- **Start Date**: 2027-02-15
- **Total Distance**: 4145.8 miles
- **Distance Source**: graphhopper
- **Total Climbing**: 171037 ft
- **Violated Constraints**:
  - [INFEASIBLE_WEATHER_MIN_LOW] at Jefferson City, Missouri on 2027-02-28: observed 21.8 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Jefferson City, Missouri.

<details>
<summary>Click to view daily travel schedule</summary>

ROUTE INFEASIBLE


</details>

---

### Alternative 1
**Feasible**: No ❌
- **Start Date**: 2027-03-15
- **Total Distance**: 4145.8 miles
- **Distance Source**: graphhopper
- **Total Climbing**: 171037 ft
- **Violated Constraints**:
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Richmond, Virginia on 2027-05-12: observed 90.4 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Richmond, Virginia.

<details>
<summary>Click to view daily travel schedule</summary>

ROUTE INFEASIBLE


</details>

---

### Alternative 2
**Feasible**: No ❌
- **Start Date**: 2027-03-01
- **Total Distance**: 4145.8 miles
- **Distance Source**: graphhopper
- **Total Climbing**: 171037 ft
- **Violated Constraints**:
  - [INFEASIBLE_WEATHER_MIN_LOW] at Topeka, Kansas on 2027-03-07: observed 18.5 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Topeka, Kansas.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Topeka, Kansas on 2027-03-08: observed 19.9 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Topeka, Kansas.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Topeka, Kansas on 2027-03-09: observed 20.1 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Topeka, Kansas.
  - [INFEASIBLE_WEATHER_MIN_LOW] at Topeka, Kansas on 2027-03-10: observed 18.4 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Topeka, Kansas.

<details>
<summary>Click to view daily travel schedule</summary>

ROUTE INFEASIBLE


</details>

---

### Alternative 3
**Feasible**: Yes
- **Start Date**: 2027-02-15
- **Total Distance**: 6857.5 miles
- **Distance Source**: graphhopper
- **Total Climbing**: 266029 ft
- **Desirability Scores**:
  - Weather Preference: 0.679
  - Distance Score: 0.281
  - Climbing Score: 0.485
  - **Total Desirability Score**: 0.511

<details>
<summary>Click to view daily travel schedule</summary>

| Day | Date | Origin | Destination | Distance (mi) | Distance Source | Ascent (ft) | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | 2027-02-15 | Austin, Texas | Montgomery, Alabama | 66.1 | graphhopper | 1281 | Avg High: 71.0°F, Low: 58.5°F (open-meteo) |  |
| 2 | 2027-02-16 | Austin, Texas | Montgomery, Alabama | 66.1 | graphhopper | 1281 | Avg High: 77.6°F, Low: 65.6°F (open-meteo) |  |
| 3 | 2027-02-17 | Austin, Texas | Montgomery, Alabama | 66.1 | graphhopper | 1281 | Avg High: 73.3°F, Low: 51.1°F (open-meteo) |  |
| 4 | 2027-02-18 | Austin, Texas | Montgomery, Alabama | 66.1 | graphhopper | 1281 | Avg High: 73.4°F, Low: 50.1°F (open-meteo) |  |
| 5 | 2027-02-19 | Austin, Texas | Montgomery, Alabama | 66.1 | graphhopper | 1281 | Avg High: 70.9°F, Low: 53.5°F (open-meteo) |  |
| 6 | 2027-02-20 | Austin, Texas | Montgomery, Alabama | 66.1 | graphhopper | 1281 | Avg High: 67.8°F, Low: 58.8°F (open-meteo) |  |
| 7 | 2027-02-21 | Austin, Texas | Montgomery, Alabama | 66.1 | graphhopper | 1281 | Avg High: 69.0°F, Low: 61.2°F (open-meteo) |  |
| 8 | 2027-02-22 | Austin, Texas | Montgomery, Alabama | 66.1 | graphhopper | 1281 | Avg High: 69.1°F, Low: 59.8°F (open-meteo) |  |
| 9 | 2027-02-23 | Austin, Texas | Montgomery, Alabama | 66.1 | graphhopper | 1281 | Avg High: 66.5°F, Low: 49.8°F (open-meteo) |  |
| 10 | 2027-02-24 | Austin, Texas | Montgomery, Alabama | 66.1 | graphhopper | 1281 | Avg High: 61.7°F, Low: 38.1°F (open-meteo) |  |
| 11 | 2027-02-25 | Austin, Texas | Montgomery, Alabama | 66.1 | graphhopper | 1281 | Avg High: 65.4°F, Low: 50.5°F (open-meteo) |  |
| 12 | 2027-02-26 | Austin, Texas | Montgomery, Alabama | 66.1 | graphhopper | 1281 | Avg High: 69.3°F, Low: 42.3°F (open-meteo) |  |
| 13 | 2027-02-27 | Montgomery, Alabama | Baton Rouge, Louisiana | 61.1 | graphhopper | 1332 | Avg High: 70.8°F, Low: 54.8°F (open-meteo) |  |
| 14 | 2027-02-28 | Montgomery, Alabama | Baton Rouge, Louisiana | 61.1 | graphhopper | 1332 | Avg High: 60.9°F, Low: 43.9°F (open-meteo) |  |
| 15 | 2027-03-01 | Montgomery, Alabama | Baton Rouge, Louisiana | 61.1 | graphhopper | 1332 | Avg High: 62.4°F, Low: 36.0°F (open-meteo) |  |
| 16 | 2027-03-02 | Montgomery, Alabama | Baton Rouge, Louisiana | 61.1 | graphhopper | 1332 | Avg High: 73.9°F, Low: 56.8°F (open-meteo) |  |
| 17 | 2027-03-03 | Montgomery, Alabama | Baton Rouge, Louisiana | 61.1 | graphhopper | 1332 | Avg High: 67.9°F, Low: 49.0°F (open-meteo) |  |
| 18 | 2027-03-04 | Montgomery, Alabama | Baton Rouge, Louisiana | 61.1 | graphhopper | 1332 | Avg High: 65.7°F, Low: 45.6°F (open-meteo) |  |
| 19 | 2027-03-05 | Baton Rouge, Louisiana | Tallahassee, Florida | 63.2 | graphhopper | 1224 | Avg High: 69.9°F, Low: 45.5°F (open-meteo) |  |
| 20 | 2027-03-06 | Baton Rouge, Louisiana | Tallahassee, Florida | 63.2 | graphhopper | 1224 | Avg High: 77.6°F, Low: 68.3°F (open-meteo) |  |
| 21 | 2027-03-07 | Baton Rouge, Louisiana | Tallahassee, Florida | 63.2 | graphhopper | 1224 | Avg High: 67.6°F, Low: 40.3°F (open-meteo) |  |
| 22 | 2027-03-08 | Baton Rouge, Louisiana | Tallahassee, Florida | 63.2 | graphhopper | 1224 | Avg High: 58.0°F, Low: 36.2°F (open-meteo) |  |
| 23 | 2027-03-09 | Baton Rouge, Louisiana | Tallahassee, Florida | 63.2 | graphhopper | 1224 | Avg High: 68.7°F, Low: 42.5°F (open-meteo) |  |
| 24 | 2027-03-10 | Baton Rouge, Louisiana | Tallahassee, Florida | 63.2 | graphhopper | 1224 | Avg High: 73.8°F, Low: 63.2°F (open-meteo) |  |
| 25 | 2027-03-11 | Baton Rouge, Louisiana | Tallahassee, Florida | 63.2 | graphhopper | 1224 | Avg High: 64.2°F, Low: 48.4°F (open-meteo) |  |
| 26 | 2027-03-12 | Tallahassee, Florida | Jackson, Mississippi | 61.1 | graphhopper | 1773 | Avg High: 59.9°F, Low: 32.5°F (open-meteo) |  |
| 27 | 2027-03-13 | Tallahassee, Florida | Jackson, Mississippi | 61.1 | graphhopper | 1773 | Avg High: 67.2°F, Low: 39.1°F (open-meteo) |  |
| 28 | 2027-03-14 | Tallahassee, Florida | Jackson, Mississippi | 61.1 | graphhopper | 1773 | Avg High: 70.7°F, Low: 45.4°F (open-meteo) |  |
| 29 | 2027-03-15 | Tallahassee, Florida | Jackson, Mississippi | 61.1 | graphhopper | 1773 | Avg High: 70.0°F, Low: 59.3°F (open-meteo) |  |
| 30 | 2027-03-16 | Tallahassee, Florida | Jackson, Mississippi | 61.1 | graphhopper | 1773 | Avg High: 63.0°F, Low: 44.4°F (open-meteo) |  |
| 31 | 2027-03-17 | Tallahassee, Florida | Jackson, Mississippi | 61.1 | graphhopper | 1773 | Avg High: 69.5°F, Low: 44.6°F (open-meteo) |  |
| 32 | 2027-03-18 | Tallahassee, Florida | Jackson, Mississippi | 61.1 | graphhopper | 1773 | Avg High: 65.8°F, Low: 48.0°F (open-meteo) |  |
| 33 | 2027-03-19 | Jackson, Mississippi | Little Rock, Arkansas | 63.5 | graphhopper | 1177 | Avg High: 56.0°F, Low: 40.2°F (open-meteo) |  |
| 34 | 2027-03-20 | Jackson, Mississippi | Little Rock, Arkansas | 63.5 | graphhopper | 1177 | Avg High: 60.9°F, Low: 35.7°F (open-meteo) |  |
| 35 | 2027-03-21 | Jackson, Mississippi | Little Rock, Arkansas | 63.5 | graphhopper | 1177 | Avg High: 69.2°F, Low: 42.9°F (open-meteo) |  |
| 36 | 2027-03-22 | Jackson, Mississippi | Little Rock, Arkansas | 63.5 | graphhopper | 1177 | Avg High: 65.9°F, Low: 47.6°F (open-meteo) |  |
| 37 | 2027-03-23 | Little Rock, Arkansas | Atlanta, Georgia | 64.1 | graphhopper | 2730 | Avg High: 65.7°F, Low: 45.3°F (open-meteo) |  |
| 38 | 2027-03-24 | Little Rock, Arkansas | Atlanta, Georgia | 64.1 | graphhopper | 2730 | Avg High: 62.9°F, Low: 46.4°F (open-meteo) |  |
| 39 | 2027-03-25 | Little Rock, Arkansas | Atlanta, Georgia | 64.1 | graphhopper | 2730 | Avg High: 55.5°F, Low: 37.4°F (open-meteo) |  |
| 40 | 2027-03-26 | Little Rock, Arkansas | Atlanta, Georgia | 64.1 | graphhopper | 2730 | Avg High: 69.6°F, Low: 36.4°F (open-meteo) |  |
| 41 | 2027-03-27 | Little Rock, Arkansas | Atlanta, Georgia | 64.1 | graphhopper | 2730 | Avg High: 67.5°F, Low: 44.2°F (open-meteo) |  |
| 42 | 2027-03-28 | Little Rock, Arkansas | Atlanta, Georgia | 64.1 | graphhopper | 2730 | Avg High: 69.0°F, Low: 45.3°F (open-meteo) |  |
| 43 | 2027-03-29 | Little Rock, Arkansas | Atlanta, Georgia | 64.1 | graphhopper | 2730 | Avg High: 63.0°F, Low: 40.5°F (open-meteo) |  |
| 44 | 2027-03-30 | Little Rock, Arkansas | Atlanta, Georgia | 64.1 | graphhopper | 2730 | Avg High: 72.9°F, Low: 47.6°F (open-meteo) |  |
| 45 | 2027-03-31 | Atlanta, Georgia | Nashville, Tennessee | 62.0 | graphhopper | 2929 | Avg High: 73.6°F, Low: 63.9°F (open-meteo) |  |
| 46 | 2027-04-01 | Atlanta, Georgia | Nashville, Tennessee | 62.0 | graphhopper | 2929 | Avg High: 72.3°F, Low: 45.5°F (open-meteo) |  |
| 47 | 2027-04-02 | Atlanta, Georgia | Nashville, Tennessee | 62.0 | graphhopper | 2929 | Avg High: 64.3°F, Low: 39.3°F (open-meteo) |  |
| 48 | 2027-04-03 | Atlanta, Georgia | Nashville, Tennessee | 62.0 | graphhopper | 2929 | Avg High: 72.8°F, Low: 46.0°F (open-meteo) |  |
| 49 | 2027-04-04 | Nashville, Tennessee | Frankfort, Kentucky | 68.6 | graphhopper | 3199 | Avg High: 66.9°F, Low: 39.9°F (open-meteo) |  |
| 50 | 2027-04-05 | Nashville, Tennessee | Frankfort, Kentucky | 68.6 | graphhopper | 3199 | Avg High: 58.7°F, Low: 33.7°F (open-meteo) |  |
| 51 | 2027-04-06 | Nashville, Tennessee | Frankfort, Kentucky | 68.6 | graphhopper | 3199 | Avg High: 73.9°F, Low: 46.3°F (open-meteo) |  |
| 52 | 2027-04-07 | Frankfort, Kentucky | Charleston, West Virginia | 65.8 | graphhopper | 4181 | Avg High: 65.6°F, Low: 49.6°F (open-meteo) |  |
| 53 | 2027-04-08 | Frankfort, Kentucky | Charleston, West Virginia | 65.8 | graphhopper | 4181 | Avg High: 65.5°F, Low: 48.9°F (open-meteo) |  |
| 54 | 2027-04-09 | Frankfort, Kentucky | Charleston, West Virginia | 65.8 | graphhopper | 4181 | Avg High: 60.2°F, Low: 42.7°F (open-meteo) |  |
| 55 | 2027-04-10 | Charleston, West Virginia | Richmond, Virginia | 61.5 | graphhopper | 4844 | Avg High: 71.9°F, Low: 39.4°F (open-meteo) |  |
| 56 | 2027-04-11 | Charleston, West Virginia | Richmond, Virginia | 61.5 | graphhopper | 4844 | Avg High: 82.5°F, Low: 50.0°F (open-meteo) |  |
| 57 | 2027-04-12 | Charleston, West Virginia | Richmond, Virginia | 61.5 | graphhopper | 4844 | Avg High: 88.4°F, Low: 56.7°F (open-meteo) |  |
| 58 | 2027-04-13 | Charleston, West Virginia | Richmond, Virginia | 61.5 | graphhopper | 4844 | Avg High: 81.8°F, Low: 60.3°F (open-meteo) |  |
| 59 | 2027-04-14 | Charleston, West Virginia | Richmond, Virginia | 61.5 | graphhopper | 4844 | Avg High: 70.7°F, Low: 55.0°F (open-meteo) |  |
| 60 | 2027-04-15 | Richmond, Virginia | Raleigh, North Carolina | 51.4 | graphhopper | 2237 | Avg High: 77.6°F, Low: 54.4°F (open-meteo) |  |
| 61 | 2027-04-16 | Richmond, Virginia | Raleigh, North Carolina | 51.4 | graphhopper | 2237 | Avg High: 69.3°F, Low: 44.1°F (open-meteo) |  |
| 62 | 2027-04-17 | Richmond, Virginia | Raleigh, North Carolina | 51.4 | graphhopper | 2237 | Avg High: 74.4°F, Low: 44.9°F (open-meteo) |  |
| 63 | 2027-04-18 | Raleigh, North Carolina | Columbia, South Carolina | 67.5 | graphhopper | 2640 | Avg High: 75.0°F, Low: 53.4°F (open-meteo) |  |
| 64 | 2027-04-19 | Raleigh, North Carolina | Columbia, South Carolina | 67.5 | graphhopper | 2640 | Avg High: 77.8°F, Low: 55.9°F (open-meteo) |  |
| 65 | 2027-04-20 | Raleigh, North Carolina | Columbia, South Carolina | 67.5 | graphhopper | 2640 | Avg High: 83.4°F, Low: 59.5°F (open-meteo) |  |
| 66 | 2027-04-21 | Columbia, South Carolina | Jefferson City, Missouri | 64.7 | graphhopper | 3596 | Avg High: 79.2°F, Low: 52.7°F (open-meteo) |  |
| 67 | 2027-04-22 | Columbia, South Carolina | Jefferson City, Missouri | 64.7 | graphhopper | 3596 | Avg High: 72.3°F, Low: 62.8°F (open-meteo) |  |
| 68 | 2027-04-23 | Columbia, South Carolina | Jefferson City, Missouri | 64.7 | graphhopper | 3596 | Avg High: 75.8°F, Low: 56.9°F (open-meteo) |  |
| 69 | 2027-04-24 | Columbia, South Carolina | Jefferson City, Missouri | 64.7 | graphhopper | 3596 | Avg High: 71.8°F, Low: 56.9°F (open-meteo) |  |
| 70 | 2027-04-25 | Columbia, South Carolina | Jefferson City, Missouri | 64.7 | graphhopper | 3596 | Avg High: 71.1°F, Low: 55.2°F (open-meteo) |  |
| 71 | 2027-04-26 | Columbia, South Carolina | Jefferson City, Missouri | 64.7 | graphhopper | 3596 | Avg High: 69.4°F, Low: 49.6°F (open-meteo) |  |
| 72 | 2027-04-27 | Columbia, South Carolina | Jefferson City, Missouri | 64.7 | graphhopper | 3596 | Avg High: 77.1°F, Low: 46.6°F (open-meteo) |  |
| 73 | 2027-04-28 | Columbia, South Carolina | Jefferson City, Missouri | 64.7 | graphhopper | 3596 | Avg High: 82.4°F, Low: 54.0°F (open-meteo) |  |
| 74 | 2027-04-29 | Columbia, South Carolina | Jefferson City, Missouri | 64.7 | graphhopper | 3596 | Avg High: 83.2°F, Low: 61.2°F (open-meteo) |  |
| 75 | 2027-04-30 | Columbia, South Carolina | Jefferson City, Missouri | 64.7 | graphhopper | 3596 | Avg High: 79.4°F, Low: 57.6°F (open-meteo) |  |
| 76 | 2027-05-01 | Columbia, South Carolina | Jefferson City, Missouri | 64.7 | graphhopper | 3596 | Avg High: 77.4°F, Low: 58.7°F (open-meteo) |  |
| 77 | 2027-05-02 | Columbia, South Carolina | Jefferson City, Missouri | 64.7 | graphhopper | 3596 | Avg High: 69.3°F, Low: 46.1°F (open-meteo) |  |
| 78 | 2027-05-03 | Columbia, South Carolina | Jefferson City, Missouri | 64.7 | graphhopper | 3596 | Avg High: 53.1°F, Low: 39.1°F (open-meteo) |  |
| 79 | 2027-05-04 | Jefferson City, Missouri | Oklahoma City, Oklahoma | 69.8 | graphhopper | 2553 | Avg High: 58.8°F, Low: 40.7°F (open-meteo) |  |
| 80 | 2027-05-05 | Jefferson City, Missouri | Oklahoma City, Oklahoma | 69.8 | graphhopper | 2553 | Avg High: 66.9°F, Low: 46.3°F (open-meteo) |  |
| 81 | 2027-05-06 | Jefferson City, Missouri | Oklahoma City, Oklahoma | 69.8 | graphhopper | 2553 | Avg High: 74.4°F, Low: 49.1°F (open-meteo) |  |
| 82 | 2027-05-07 | Jefferson City, Missouri | Oklahoma City, Oklahoma | 69.8 | graphhopper | 2553 | Avg High: 83.8°F, Low: 56.5°F (open-meteo) |  |
| 83 | 2027-05-08 | Jefferson City, Missouri | Oklahoma City, Oklahoma | 69.8 | graphhopper | 2553 | Avg High: 85.6°F, Low: 58.6°F (open-meteo) |  |
| 84 | 2027-05-09 | Jefferson City, Missouri | Oklahoma City, Oklahoma | 69.8 | graphhopper | 2553 | Avg High: 86.3°F, Low: 62.5°F (open-meteo) |  |
| 85 | 2027-05-10 | Oklahoma City, Oklahoma | Topeka, Kansas | 58.4 | graphhopper | 1606 | Avg High: 87.1°F, Low: 63.7°F (open-meteo) |  |
| 86 | 2027-05-11 | Oklahoma City, Oklahoma | Topeka, Kansas | 58.4 | graphhopper | 1606 | Avg High: 88.8°F, Low: 65.5°F (open-meteo) |  |
| 87 | 2027-05-12 | Oklahoma City, Oklahoma | Topeka, Kansas | 58.4 | graphhopper | 1606 | Avg High: 87.0°F, Low: 63.4°F (open-meteo) |  |
| 88 | 2027-05-13 | Oklahoma City, Oklahoma | Topeka, Kansas | 58.4 | graphhopper | 1606 | Avg High: 72.3°F, Low: 56.1°F (open-meteo) |  |
| 89 | 2027-05-14 | Oklahoma City, Oklahoma | Topeka, Kansas | 58.4 | graphhopper | 1606 | Avg High: 75.1°F, Low: 57.9°F (open-meteo) |  |
| 90 | 2027-05-15 | Topeka, Kansas | Harrisburg, Pennsylvania | 67.5 | graphhopper | 2821 | Avg High: 66.5°F, Low: 45.6°F (open-meteo) |  |
| 91 | 2027-05-16 | Topeka, Kansas | Harrisburg, Pennsylvania | 67.5 | graphhopper | 2821 | Avg High: 59.9°F, Low: 52.8°F (open-meteo) |  |
| 92 | 2027-05-17 | Topeka, Kansas | Harrisburg, Pennsylvania | 67.5 | graphhopper | 2821 | Avg High: 68.3°F, Low: 45.2°F (open-meteo) |  |
| 93 | 2027-05-18 | Topeka, Kansas | Harrisburg, Pennsylvania | 67.5 | graphhopper | 2821 | Avg High: 71.7°F, Low: 51.1°F (open-meteo) |  |
| 94 | 2027-05-19 | Topeka, Kansas | Harrisburg, Pennsylvania | 67.5 | graphhopper | 2821 | Avg High: 77.8°F, Low: 59.6°F (open-meteo) |  |
| 95 | 2027-05-20 | Topeka, Kansas | Harrisburg, Pennsylvania | 67.5 | graphhopper | 2821 | Avg High: 79.1°F, Low: 64.5°F (open-meteo) |  |
| 96 | 2027-05-21 | Topeka, Kansas | Harrisburg, Pennsylvania | 67.5 | graphhopper | 2821 | Avg High: 80.1°F, Low: 60.2°F (open-meteo) |  |
| 97 | 2027-05-22 | Topeka, Kansas | Harrisburg, Pennsylvania | 67.5 | graphhopper | 2821 | Avg High: 72.9°F, Low: 56.2°F (open-meteo) |  |
| 98 | 2027-05-23 | Topeka, Kansas | Harrisburg, Pennsylvania | 67.5 | graphhopper | 2821 | Avg High: 75.8°F, Low: 49.4°F (open-meteo) |  |
| 99 | 2027-05-24 | Topeka, Kansas | Harrisburg, Pennsylvania | 67.5 | graphhopper | 2821 | Avg High: 74.0°F, Low: 53.5°F (open-meteo) |  |
| 100 | 2027-05-25 | Topeka, Kansas | Harrisburg, Pennsylvania | 67.5 | graphhopper | 2821 | Avg High: 81.9°F, Low: 63.9°F (open-meteo) |  |
| 101 | 2027-05-26 | Topeka, Kansas | Harrisburg, Pennsylvania | 67.5 | graphhopper | 2821 | Avg High: 77.7°F, Low: 51.1°F (open-meteo) |  |
| 102 | 2027-05-27 | Topeka, Kansas | Harrisburg, Pennsylvania | 67.5 | graphhopper | 2821 | Avg High: 81.9°F, Low: 61.6°F (open-meteo) |  |
| 103 | 2027-05-28 | Topeka, Kansas | Harrisburg, Pennsylvania | 67.5 | graphhopper | 2821 | Avg High: 83.5°F, Low: 58.3°F (open-meteo) |  |
| 104 | 2027-05-29 | Topeka, Kansas | Harrisburg, Pennsylvania | 67.5 | graphhopper | 2821 | Avg High: 81.8°F, Low: 59.1°F (open-meteo) |  |
| 105 | 2027-05-30 | Topeka, Kansas | Harrisburg, Pennsylvania | 67.5 | graphhopper | 2821 | Avg High: 78.4°F, Low: 70.3°F (open-meteo) |  |
| 106 | 2027-05-31 | Harrisburg, Pennsylvania | Washington, DC | 56.2 | graphhopper | 3597 | Avg High: 82.4°F, Low: 72.5°F (open-meteo) |  |
| 107 | 2027-06-01 | Harrisburg, Pennsylvania | Washington, DC | 56.2 | graphhopper | 3597 | Avg High: 82.2°F, Low: 66.2°F (open-meteo) |  |

</details>

---

### Alternative 4
**Feasible**: No ❌
- **Start Date**: 2027-03-15
- **Total Distance**: 6466.6 miles
- **Distance Source**: graphhopper
- **Total Climbing**: 298637 ft
- **Violated Constraints**:
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Washington, DC on 2027-06-21: observed 91.0 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Washington, DC.
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Washington, DC on 2027-06-22: observed 99.7 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Washington, DC.
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Washington, DC on 2027-06-23: observed 96.5 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Washington, DC.
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Washington, DC on 2027-06-24: observed 98.6 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Washington, DC.

<details>
<summary>Click to view daily travel schedule</summary>

ROUTE INFEASIBLE


</details>

---

### Alternative 5
**Feasible**: No ❌
- **Start Date**: 2027-03-15
- **Total Distance**: 6646.7 miles
- **Distance Source**: graphhopper
- **Total Climbing**: 305279 ft
- **Violated Constraints**:
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Washington, DC on 2027-06-21: observed 91.0 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Washington, DC.
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Washington, DC on 2027-06-22: observed 99.7 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Washington, DC.
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Washington, DC on 2027-06-23: observed 96.5 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Washington, DC.
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Washington, DC on 2027-06-24: observed 98.6 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Washington, DC.
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Washington, DC on 2027-06-25: observed 98.9 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Washington, DC.
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Washington, DC on 2027-06-27: observed 90.3 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Washington, DC.

<details>
<summary>Click to view daily travel schedule</summary>

ROUTE INFEASIBLE


</details>

---

### Alternative 6
**Feasible**: No ❌
- **Start Date**: 2027-03-15
- **Total Distance**: 6710.6 miles
- **Distance Source**: graphhopper
- **Total Climbing**: 305780 ft
- **Violated Constraints**:
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Washington, DC on 2027-06-21: observed 91.0 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Washington, DC.
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Washington, DC on 2027-06-22: observed 99.7 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Washington, DC.
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Washington, DC on 2027-06-23: observed 96.5 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Washington, DC.
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Washington, DC on 2027-06-24: observed 98.6 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Washington, DC.
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Washington, DC on 2027-06-25: observed 98.9 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Washington, DC.
  - [INFEASIBLE_WEATHER_MAX_HIGH] at Washington, DC on 2027-06-27: observed 90.3 vs threshold 90. Hint: Consider traveling during a cooler season or modifying the route to bypass Washington, DC.

<details>
<summary>Click to view daily travel schedule</summary>

ROUTE INFEASIBLE


</details>

---

## Data Attribution
Weather data by [Open-Meteo.com](https://open-meteo.com/) under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Data has been transformed into itinerary-level schedule summaries.


