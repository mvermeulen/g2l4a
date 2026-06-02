# Route Recommendations Comparison

## Overview Comparison
| Option | Start Date | Feasible? | Total Score | Weather Score | Distance Score | Hills Score | Total Distance | Distance Source | Total Climb | Key Difference |
|---|---|---|---|---|---|---|---|---|---|---|
| **Best Recommendation** | 2027-02-15 | No ❌ | N/A | N/A | N/A | N/A | 4880.0 mi | graphhopper | 262682 ft | Baseline / Optimal Route |
| Alternative 1 | 2027-02-01 | Yes | 0.6795 | 0.5847 | 0.5545 | 1.0000 | 4880.0 mi | graphhopper | 262682 ft | Different start date (2027-02-01), same sequence |
| Alternative 2 | 2027-01-18 | No ❌ | N/A | N/A | N/A | N/A | 4880.0 mi | graphhopper | 262682 ft | Different start date (2027-01-18), same sequence |
| Alternative 3 | 2027-02-15 | Yes | 0.5385 | 0.6817 | 0.2828 | 0.5876 | 6833.7 mi | graphhopper | 362377 ft | Alternative via-city sequence, same date |
| Alternative 4 | 2027-02-15 | Yes | 0.5231 | 0.6723 | 0.2699 | 0.5583 | 6995.2 mi | graphhopper | 369458 ft | Alternative via-city sequence, same date |
| Alternative 5 | 2027-02-15 | Yes | 0.5184 | 0.6621 | 0.2755 | 0.5511 | 6923.8 mi | graphhopper | 371196 ft | Alternative via-city sequence, same date |
| Alternative 6 | 2027-02-01 | Yes | 0.5175 | 0.6771 | 0.2606 | 0.5383 | 7118.0 mi | graphhopper | 374305 ft | Different start date (2027-02-01) & alternative sequence |

## Detailed Recommendations
### Best Recommendation
**Feasible**: No ❌
- **Start Date**: 2027-02-15
- **Total Distance**: 4880.0 miles
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
**Feasible**: Yes
- **Start Date**: 2027-02-01
- **Total Distance**: 4880.0 miles
- **Distance Source**: graphhopper
- **Total Climbing**: 262682 ft
- **Desirability Scores**:
  - Weather Preference: 0.585
  - Distance Score: 0.554
  - Climbing Score: 1.000
  - **Total Desirability Score**: 0.679

<details>
<summary>Click to view daily travel schedule</summary>

| Day | Date | Origin | Destination | Distance (mi) | Distance Source | Ascent (ft) | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | 2027-02-01 | Austin, Texas | Oklahoma City, Oklahoma | 64.7 | graphhopper | 2429 | Avg High: 60.0°F, Low: 42.3°F (open-meteo) |  |
| 2 | 2027-02-02 | Austin, Texas | Oklahoma City, Oklahoma | 64.7 | graphhopper | 2429 | Avg High: 59.5°F, Low: 43.1°F (open-meteo) |  |
| 3 | 2027-02-03 | Austin, Texas | Oklahoma City, Oklahoma | 64.7 | graphhopper | 2429 | Avg High: 63.3°F, Low: 44.6°F (open-meteo) |  |
| 4 | 2027-02-04 | Austin, Texas | Oklahoma City, Oklahoma | 64.7 | graphhopper | 2429 | Avg High: 61.8°F, Low: 38.9°F (open-meteo) |  |
| 5 | 2027-02-05 | Austin, Texas | Oklahoma City, Oklahoma | 64.7 | graphhopper | 2429 | Avg High: 61.2°F, Low: 41.6°F (open-meteo) |  |
| 6 | 2027-02-06 | Austin, Texas | Oklahoma City, Oklahoma | 64.7 | graphhopper | 2429 | Avg High: 64.3°F, Low: 51.2°F (open-meteo) |  |
| 7 | 2027-02-07 | Austin, Texas | Oklahoma City, Oklahoma | 64.7 | graphhopper | 2429 | Avg High: 69.0°F, Low: 49.2°F (open-meteo) |  |
| 8 | 2027-02-08 | Oklahoma City, Oklahoma | Topeka, Kansas | 62.4 | graphhopper | 2085 | Avg High: 63.3°F, Low: 49.5°F (open-meteo) |  |
| 9 | 2027-02-09 | Oklahoma City, Oklahoma | Topeka, Kansas | 62.4 | graphhopper | 2085 | Avg High: 58.9°F, Low: 50.5°F (open-meteo) |  |
| 10 | 2027-02-10 | Oklahoma City, Oklahoma | Topeka, Kansas | 62.4 | graphhopper | 2085 | Avg High: 66.5°F, Low: 45.6°F (open-meteo) |  |
| 11 | 2027-02-11 | Oklahoma City, Oklahoma | Topeka, Kansas | 62.4 | graphhopper | 2085 | Avg High: 64.1°F, Low: 47.3°F (open-meteo) |  |
| 12 | 2027-02-12 | Oklahoma City, Oklahoma | Topeka, Kansas | 62.4 | graphhopper | 2085 | Avg High: 58.0°F, Low: 37.6°F (open-meteo) |  |
| 13 | 2027-02-13 | Oklahoma City, Oklahoma | Topeka, Kansas | 62.4 | graphhopper | 2085 | Avg High: 67.8°F, Low: 46.3°F (open-meteo) |  |
| 14 | 2027-02-14 | Topeka, Kansas | Jefferson City, Missouri | 57.7 | graphhopper | 2910 | Avg High: 59.1°F, Low: 48.4°F (open-meteo) |  |
| 15 | 2027-02-15 | Topeka, Kansas | Jefferson City, Missouri | 57.7 | graphhopper | 2910 | Avg High: 62.5°F, Low: 49.1°F (open-meteo) |  |
| 16 | 2027-02-16 | Topeka, Kansas | Jefferson City, Missouri | 57.7 | graphhopper | 2910 | Avg High: 62.3°F, Low: 51.7°F (open-meteo) |  |
| 17 | 2027-02-17 | Topeka, Kansas | Jefferson City, Missouri | 57.7 | graphhopper | 2910 | Avg High: 52.8°F, Low: 44.8°F (open-meteo) |  |
| 18 | 2027-02-18 | Jefferson City, Missouri | Little Rock, Arkansas | 68.5 | graphhopper | 4982 | Avg High: 70.6°F, Low: 50.7°F (open-meteo) |  |
| 19 | 2027-02-19 | Jefferson City, Missouri | Little Rock, Arkansas | 68.5 | graphhopper | 4982 | Avg High: 73.7°F, Low: 58.5°F (open-meteo) |  |
| 20 | 2027-02-20 | Jefferson City, Missouri | Little Rock, Arkansas | 68.5 | graphhopper | 4982 | Avg High: 74.1°F, Low: 59.4°F (open-meteo) |  |
| 21 | 2027-02-21 | Jefferson City, Missouri | Little Rock, Arkansas | 68.5 | graphhopper | 4982 | Avg High: 72.2°F, Low: 57.2°F (open-meteo) |  |
| 22 | 2027-02-22 | Jefferson City, Missouri | Little Rock, Arkansas | 68.5 | graphhopper | 4982 | Avg High: 63.8°F, Low: 55.2°F (open-meteo) |  |
| 23 | 2027-02-23 | Little Rock, Arkansas | Jackson, Mississippi | 66.7 | graphhopper | 1539 | Avg High: 58.8°F, Low: 44.1°F (open-meteo) |  |
| 24 | 2027-02-24 | Little Rock, Arkansas | Jackson, Mississippi | 66.7 | graphhopper | 1539 | Avg High: 70.2°F, Low: 42.3°F (open-meteo) |  |
| 25 | 2027-02-25 | Little Rock, Arkansas | Jackson, Mississippi | 66.7 | graphhopper | 1539 | Avg High: 64.2°F, Low: 47.3°F (open-meteo) |  |
| 26 | 2027-02-26 | Little Rock, Arkansas | Jackson, Mississippi | 66.7 | graphhopper | 1539 | Avg High: 73.9°F, Low: 47.1°F (open-meteo) |  |
| 27 | 2027-02-27 | Little Rock, Arkansas | Jackson, Mississippi | 66.7 | graphhopper | 1539 | Avg High: 69.4°F, Low: 48.6°F (open-meteo) |  |
| 28 | 2027-02-28 | Jackson, Mississippi | Baton Rouge, Louisiana | 57.6 | graphhopper | 2454 | Avg High: 60.9°F, Low: 43.9°F (open-meteo) |  |
| 29 | 2027-03-01 | Jackson, Mississippi | Baton Rouge, Louisiana | 57.6 | graphhopper | 2454 | Avg High: 62.4°F, Low: 36.0°F (open-meteo) |  |
| 30 | 2027-03-02 | Jackson, Mississippi | Baton Rouge, Louisiana | 57.6 | graphhopper | 2454 | Avg High: 73.9°F, Low: 56.8°F (open-meteo) |  |
| 31 | 2027-03-03 | Baton Rouge, Louisiana | Montgomery, Alabama | 68.3 | graphhopper | 2882 | Avg High: 61.3°F, Low: 42.1°F (open-meteo) |  |
| 32 | 2027-03-04 | Baton Rouge, Louisiana | Montgomery, Alabama | 68.3 | graphhopper | 2882 | Avg High: 52.4°F, Low: 31.3°F (open-meteo) |  |
| 33 | 2027-03-05 | Baton Rouge, Louisiana | Montgomery, Alabama | 68.3 | graphhopper | 2882 | Avg High: 73.3°F, Low: 46.8°F (open-meteo) |  |
| 34 | 2027-03-06 | Baton Rouge, Louisiana | Montgomery, Alabama | 68.3 | graphhopper | 2882 | Avg High: 71.0°F, Low: 53.5°F (open-meteo) |  |
| 35 | 2027-03-07 | Baton Rouge, Louisiana | Montgomery, Alabama | 68.3 | graphhopper | 2882 | Avg High: 53.1°F, Low: 35.0°F (open-meteo) |  |
| 36 | 2027-03-08 | Baton Rouge, Louisiana | Montgomery, Alabama | 68.3 | graphhopper | 2882 | Avg High: 54.6°F, Low: 32.4°F (open-meteo) |  |
| 37 | 2027-03-09 | Montgomery, Alabama | Tallahassee, Florida | 55.5 | graphhopper | 2540 | Avg High: 68.7°F, Low: 42.5°F (open-meteo) |  |
| 38 | 2027-03-10 | Montgomery, Alabama | Tallahassee, Florida | 55.5 | graphhopper | 2540 | Avg High: 73.8°F, Low: 63.2°F (open-meteo) |  |
| 39 | 2027-03-11 | Montgomery, Alabama | Tallahassee, Florida | 55.5 | graphhopper | 2540 | Avg High: 64.2°F, Low: 48.4°F (open-meteo) |  |
| 40 | 2027-03-12 | Montgomery, Alabama | Tallahassee, Florida | 55.5 | graphhopper | 2540 | Avg High: 59.1°F, Low: 41.5°F (open-meteo) |  |
| 41 | 2027-03-13 | Tallahassee, Florida | Atlanta, Georgia | 63.0 | graphhopper | 2864 | Avg High: 60.8°F, Low: 32.1°F (open-meteo) |  |
| 42 | 2027-03-14 | Tallahassee, Florida | Atlanta, Georgia | 63.0 | graphhopper | 2864 | Avg High: 61.7°F, Low: 38.2°F (open-meteo) |  |
| 43 | 2027-03-15 | Tallahassee, Florida | Atlanta, Georgia | 63.0 | graphhopper | 2864 | Avg High: 68.0°F, Low: 48.2°F (open-meteo) |  |
| 44 | 2027-03-16 | Tallahassee, Florida | Atlanta, Georgia | 63.0 | graphhopper | 2864 | Avg High: 64.4°F, Low: 46.0°F (open-meteo) |  |
| 45 | 2027-03-17 | Tallahassee, Florida | Atlanta, Georgia | 63.0 | graphhopper | 2864 | Avg High: 59.4°F, Low: 37.8°F (open-meteo) |  |
| 46 | 2027-03-18 | Atlanta, Georgia | Nashville, Tennessee | 58.6 | graphhopper | 3589 | Avg High: 47.3°F, Low: 35.7°F (open-meteo) |  |
| 47 | 2027-03-19 | Atlanta, Georgia | Nashville, Tennessee | 58.6 | graphhopper | 3589 | Avg High: 49.4°F, Low: 31.0°F (open-meteo) |  |
| 48 | 2027-03-20 | Atlanta, Georgia | Nashville, Tennessee | 58.6 | graphhopper | 3589 | Avg High: 46.1°F, Low: 33.6°F (open-meteo) |  |
| 49 | 2027-03-21 | Atlanta, Georgia | Nashville, Tennessee | 58.6 | graphhopper | 3589 | Avg High: 63.4°F, Low: 31.7°F (open-meteo) |  |
| 50 | 2027-03-22 | Atlanta, Georgia | Nashville, Tennessee | 58.6 | graphhopper | 3589 | Avg High: 62.5°F, Low: 40.6°F (open-meteo) |  |
| 51 | 2027-03-23 | Nashville, Tennessee | Frankfort, Kentucky | 57.1 | graphhopper | 3572 | Avg High: 53.0°F, Low: 33.8°F (open-meteo) |  |
| 52 | 2027-03-24 | Nashville, Tennessee | Frankfort, Kentucky | 57.1 | graphhopper | 3572 | Avg High: 53.4°F, Low: 37.1°F (open-meteo) |  |
| 53 | 2027-03-25 | Nashville, Tennessee | Frankfort, Kentucky | 57.1 | graphhopper | 3572 | Avg High: 47.6°F, Low: 32.3°F (open-meteo) |  |
| 54 | 2027-03-26 | Nashville, Tennessee | Frankfort, Kentucky | 57.1 | graphhopper | 3572 | Avg High: 64.2°F, Low: 42.3°F (open-meteo) |  |
| 55 | 2027-03-27 | Frankfort, Kentucky | Charleston, West Virginia | 64.1 | graphhopper | 4912 | Avg High: 64.0°F, Low: 38.0°F (open-meteo) |  |
| 56 | 2027-03-28 | Frankfort, Kentucky | Charleston, West Virginia | 64.1 | graphhopper | 4912 | Avg High: 54.2°F, Low: 37.9°F (open-meteo) |  |
| 57 | 2027-03-29 | Frankfort, Kentucky | Charleston, West Virginia | 64.1 | graphhopper | 4912 | Avg High: 51.7°F, Low: 26.2°F (open-meteo) |  |
| 58 | 2027-03-30 | Frankfort, Kentucky | Charleston, West Virginia | 64.1 | graphhopper | 4912 | Avg High: 67.0°F, Low: 47.1°F (open-meteo) |  |
| 59 | 2027-03-31 | Charleston, West Virginia | Columbia, South Carolina | 54.3 | graphhopper | 4823 | Avg High: 77.4°F, Low: 65.1°F (open-meteo) |  |
| 60 | 2027-04-01 | Charleston, West Virginia | Columbia, South Carolina | 54.3 | graphhopper | 4823 | Avg High: 82.3°F, Low: 70.5°F (open-meteo) |  |
| 61 | 2027-04-02 | Charleston, West Virginia | Columbia, South Carolina | 54.3 | graphhopper | 4823 | Avg High: 71.5°F, Low: 53.5°F (open-meteo) |  |
| 62 | 2027-04-03 | Charleston, West Virginia | Columbia, South Carolina | 54.3 | graphhopper | 4823 | Avg High: 58.0°F, Low: 54.5°F (open-meteo) |  |
| 63 | 2027-04-04 | Charleston, West Virginia | Columbia, South Carolina | 54.3 | graphhopper | 4823 | Avg High: 72.9°F, Low: 58.1°F (open-meteo) |  |
| 64 | 2027-04-05 | Charleston, West Virginia | Columbia, South Carolina | 54.3 | graphhopper | 4823 | Avg High: 66.4°F, Low: 47.7°F (open-meteo) |  |
| 65 | 2027-04-06 | Charleston, West Virginia | Columbia, South Carolina | 54.3 | graphhopper | 4823 | Avg High: 80.6°F, Low: 55.2°F (open-meteo) |  |
| 66 | 2027-04-07 | Charleston, West Virginia | Columbia, South Carolina | 54.3 | graphhopper | 4823 | Avg High: 83.2°F, Low: 69.2°F (open-meteo) |  |
| 67 | 2027-04-08 | Columbia, South Carolina | Raleigh, North Carolina | 57.8 | graphhopper | 2586 | Avg High: 71.1°F, Low: 59.5°F (open-meteo) |  |
| 68 | 2027-04-09 | Columbia, South Carolina | Raleigh, North Carolina | 57.8 | graphhopper | 2586 | Avg High: 71.5°F, Low: 47.5°F (open-meteo) |  |
| 69 | 2027-04-10 | Columbia, South Carolina | Raleigh, North Carolina | 57.8 | graphhopper | 2586 | Avg High: 71.4°F, Low: 41.5°F (open-meteo) |  |
| 70 | 2027-04-11 | Columbia, South Carolina | Raleigh, North Carolina | 57.8 | graphhopper | 2586 | Avg High: 83.4°F, Low: 47.2°F (open-meteo) |  |
| 71 | 2027-04-12 | Raleigh, North Carolina | Richmond, Virginia | 65.2 | graphhopper | 3602 | Avg High: 88.4°F, Low: 56.7°F (open-meteo) |  |
| 72 | 2027-04-13 | Raleigh, North Carolina | Richmond, Virginia | 65.2 | graphhopper | 3602 | Avg High: 81.8°F, Low: 60.3°F (open-meteo) |  |
| 73 | 2027-04-14 | Raleigh, North Carolina | Richmond, Virginia | 65.2 | graphhopper | 3602 | Avg High: 70.7°F, Low: 55.0°F (open-meteo) |  |
| 74 | 2027-04-15 | Richmond, Virginia | Harrisburg, Pennsylvania | 64.2 | graphhopper | 4515 | Avg High: 49.0°F, Low: 42.7°F (open-meteo) |  |
| 75 | 2027-04-16 | Richmond, Virginia | Harrisburg, Pennsylvania | 64.2 | graphhopper | 4515 | Avg High: 61.8°F, Low: 35.8°F (open-meteo) |  |
| 76 | 2027-04-17 | Richmond, Virginia | Harrisburg, Pennsylvania | 64.2 | graphhopper | 4515 | Avg High: 64.9°F, Low: 39.2°F (open-meteo) |  |
| 77 | 2027-04-18 | Richmond, Virginia | Harrisburg, Pennsylvania | 64.2 | graphhopper | 4515 | Avg High: 61.2°F, Low: 48.1°F (open-meteo) |  |
| 78 | 2027-04-19 | Harrisburg, Pennsylvania | Washington, DC | 43.1 | graphhopper | 3376 | Avg High: 76.9°F, Low: 60.0°F (open-meteo) |  |
| 79 | 2027-04-20 | Harrisburg, Pennsylvania | Washington, DC | 43.1 | graphhopper | 3376 | Avg High: 69.3°F, Low: 54.7°F (open-meteo) |  |
| 80 | 2027-04-21 | Harrisburg, Pennsylvania | Washington, DC | 43.1 | graphhopper | 3376 | Avg High: 58.8°F, Low: 49.3°F (open-meteo) |  |

</details>

---

### Alternative 2
**Feasible**: No ❌
- **Start Date**: 2027-01-18
- **Total Distance**: 4880.0 miles
- **Distance Source**: graphhopper
- **Total Climbing**: 262682 ft
- **Violated Constraints**:
  - [INFEASIBLE_WEATHER_MIN_LOW] at Topeka, Kansas on 2027-01-26: observed 20.4 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Topeka, Kansas.

<details>
<summary>Click to view daily travel schedule</summary>

ROUTE INFEASIBLE


</details>

---

### Alternative 3
**Feasible**: Yes
- **Start Date**: 2027-02-15
- **Total Distance**: 6833.7 miles
- **Distance Source**: graphhopper
- **Total Climbing**: 362377 ft
- **Desirability Scores**:
  - Weather Preference: 0.682
  - Distance Score: 0.283
  - Climbing Score: 0.588
  - **Total Desirability Score**: 0.538

<details>
<summary>Click to view daily travel schedule</summary>

| Day | Date | Origin | Destination | Distance (mi) | Distance Source | Ascent (ft) | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | 2027-02-15 | Austin, Texas | Little Rock, Arkansas | 63.5 | graphhopper | 2357 | Avg High: 66.0°F, Low: 60.1°F (open-meteo) |  |
| 2 | 2027-02-16 | Austin, Texas | Little Rock, Arkansas | 63.5 | graphhopper | 2357 | Avg High: 70.9°F, Low: 53.8°F (open-meteo) |  |
| 3 | 2027-02-17 | Austin, Texas | Little Rock, Arkansas | 63.5 | graphhopper | 2357 | Avg High: 66.8°F, Low: 51.3°F (open-meteo) |  |
| 4 | 2027-02-18 | Austin, Texas | Little Rock, Arkansas | 63.5 | graphhopper | 2357 | Avg High: 70.6°F, Low: 50.7°F (open-meteo) |  |
| 5 | 2027-02-19 | Austin, Texas | Little Rock, Arkansas | 63.5 | graphhopper | 2357 | Avg High: 73.7°F, Low: 58.5°F (open-meteo) |  |
| 6 | 2027-02-20 | Austin, Texas | Little Rock, Arkansas | 63.5 | graphhopper | 2357 | Avg High: 74.1°F, Low: 59.4°F (open-meteo) |  |
| 7 | 2027-02-21 | Austin, Texas | Little Rock, Arkansas | 63.5 | graphhopper | 2357 | Avg High: 72.2°F, Low: 57.2°F (open-meteo) |  |
| 8 | 2027-02-22 | Austin, Texas | Little Rock, Arkansas | 63.5 | graphhopper | 2357 | Avg High: 63.8°F, Low: 55.2°F (open-meteo) |  |
| 9 | 2027-02-23 | Austin, Texas | Little Rock, Arkansas | 63.5 | graphhopper | 2357 | Avg High: 57.3°F, Low: 41.0°F (open-meteo) |  |
| 10 | 2027-02-24 | Little Rock, Arkansas | Oklahoma City, Oklahoma | 62.5 | graphhopper | 3322 | Avg High: 65.8°F, Low: 48.9°F (open-meteo) |  |
| 11 | 2027-02-25 | Little Rock, Arkansas | Oklahoma City, Oklahoma | 62.5 | graphhopper | 3322 | Avg High: 69.1°F, Low: 41.0°F (open-meteo) |  |
| 12 | 2027-02-26 | Little Rock, Arkansas | Oklahoma City, Oklahoma | 62.5 | graphhopper | 3322 | Avg High: 69.2°F, Low: 54.8°F (open-meteo) |  |
| 13 | 2027-02-27 | Little Rock, Arkansas | Oklahoma City, Oklahoma | 62.5 | graphhopper | 3322 | Avg High: 62.6°F, Low: 46.3°F (open-meteo) |  |
| 14 | 2027-02-28 | Little Rock, Arkansas | Oklahoma City, Oklahoma | 62.5 | graphhopper | 3322 | Avg High: 52.6°F, Low: 34.0°F (open-meteo) |  |
| 15 | 2027-03-01 | Little Rock, Arkansas | Oklahoma City, Oklahoma | 62.5 | graphhopper | 3322 | Avg High: 65.7°F, Low: 41.0°F (open-meteo) |  |
| 16 | 2027-03-02 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 63.4°F, Low: 38.1°F (open-meteo) |  |
| 17 | 2027-03-03 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 60.9°F, Low: 46.9°F (open-meteo) |  |
| 18 | 2027-03-04 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 53.9°F, Low: 33.1°F (open-meteo) |  |
| 19 | 2027-03-05 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 69.9°F, Low: 45.5°F (open-meteo) |  |
| 20 | 2027-03-06 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 77.6°F, Low: 68.3°F (open-meteo) |  |
| 21 | 2027-03-07 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 67.6°F, Low: 40.3°F (open-meteo) |  |
| 22 | 2027-03-08 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 58.0°F, Low: 36.2°F (open-meteo) |  |
| 23 | 2027-03-09 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 68.7°F, Low: 42.5°F (open-meteo) |  |
| 24 | 2027-03-10 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 73.8°F, Low: 63.2°F (open-meteo) |  |
| 25 | 2027-03-11 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 64.2°F, Low: 48.4°F (open-meteo) |  |
| 26 | 2027-03-12 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 59.1°F, Low: 41.5°F (open-meteo) |  |
| 27 | 2027-03-13 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 64.8°F, Low: 36.3°F (open-meteo) |  |
| 28 | 2027-03-14 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 72.2°F, Low: 39.1°F (open-meteo) |  |
| 29 | 2027-03-15 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 70.8°F, Low: 53.3°F (open-meteo) |  |
| 30 | 2027-03-16 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 70.4°F, Low: 64.2°F (open-meteo) |  |
| 31 | 2027-03-17 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 74.6°F, Low: 48.1°F (open-meteo) |  |
| 32 | 2027-03-18 | Tallahassee, Florida | Baton Rouge, Louisiana | 65.5 | graphhopper | 2248 | Avg High: 72.7°F, Low: 57.8°F (open-meteo) |  |
| 33 | 2027-03-19 | Tallahassee, Florida | Baton Rouge, Louisiana | 65.5 | graphhopper | 2248 | Avg High: 65.2°F, Low: 37.6°F (open-meteo) |  |
| 34 | 2027-03-20 | Tallahassee, Florida | Baton Rouge, Louisiana | 65.5 | graphhopper | 2248 | Avg High: 62.7°F, Low: 41.5°F (open-meteo) |  |
| 35 | 2027-03-21 | Tallahassee, Florida | Baton Rouge, Louisiana | 65.5 | graphhopper | 2248 | Avg High: 69.9°F, Low: 39.1°F (open-meteo) |  |
| 36 | 2027-03-22 | Tallahassee, Florida | Baton Rouge, Louisiana | 65.5 | graphhopper | 2248 | Avg High: 71.7°F, Low: 51.6°F (open-meteo) |  |
| 37 | 2027-03-23 | Tallahassee, Florida | Baton Rouge, Louisiana | 65.5 | graphhopper | 2248 | Avg High: 74.4°F, Low: 58.6°F (open-meteo) |  |
| 38 | 2027-03-24 | Tallahassee, Florida | Baton Rouge, Louisiana | 65.5 | graphhopper | 2248 | Avg High: 72.1°F, Low: 50.6°F (open-meteo) |  |
| 39 | 2027-03-25 | Tallahassee, Florida | Baton Rouge, Louisiana | 65.5 | graphhopper | 2248 | Avg High: 68.5°F, Low: 43.4°F (open-meteo) |  |
| 40 | 2027-03-26 | Baton Rouge, Louisiana | Jackson, Mississippi | 57.6 | graphhopper | 2527 | Avg High: 72.7°F, Low: 43.6°F (open-meteo) |  |
| 41 | 2027-03-27 | Baton Rouge, Louisiana | Jackson, Mississippi | 57.6 | graphhopper | 2527 | Avg High: 70.7°F, Low: 51.2°F (open-meteo) |  |
| 42 | 2027-03-28 | Baton Rouge, Louisiana | Jackson, Mississippi | 57.6 | graphhopper | 2527 | Avg High: 72.2°F, Low: 55.6°F (open-meteo) |  |
| 43 | 2027-03-29 | Jackson, Mississippi | Montgomery, Alabama | 67.6 | graphhopper | 3054 | Avg High: 74.4°F, Low: 49.8°F (open-meteo) |  |
| 44 | 2027-03-30 | Jackson, Mississippi | Montgomery, Alabama | 67.6 | graphhopper | 3054 | Avg High: 75.5°F, Low: 55.9°F (open-meteo) |  |
| 45 | 2027-03-31 | Jackson, Mississippi | Montgomery, Alabama | 67.6 | graphhopper | 3054 | Avg High: 75.5°F, Low: 69.3°F (open-meteo) |  |
| 46 | 2027-04-01 | Jackson, Mississippi | Montgomery, Alabama | 67.6 | graphhopper | 3054 | Avg High: 74.7°F, Low: 58.7°F (open-meteo) |  |
| 47 | 2027-04-02 | Montgomery, Alabama | Atlanta, Georgia | 66.4 | graphhopper | 3698 | Avg High: 64.0°F, Low: 48.1°F (open-meteo) |  |
| 48 | 2027-04-03 | Montgomery, Alabama | Atlanta, Georgia | 66.4 | graphhopper | 3698 | Avg High: 63.0°F, Low: 49.6°F (open-meteo) |  |
| 49 | 2027-04-04 | Montgomery, Alabama | Atlanta, Georgia | 66.4 | graphhopper | 3698 | Avg High: 61.5°F, Low: 57.8°F (open-meteo) |  |
| 50 | 2027-04-05 | Atlanta, Georgia | Columbia, South Carolina | 64.1 | graphhopper | 3717 | Avg High: 66.4°F, Low: 47.7°F (open-meteo) |  |
| 51 | 2027-04-06 | Atlanta, Georgia | Columbia, South Carolina | 64.1 | graphhopper | 3717 | Avg High: 80.6°F, Low: 55.2°F (open-meteo) |  |
| 52 | 2027-04-07 | Atlanta, Georgia | Columbia, South Carolina | 64.1 | graphhopper | 3717 | Avg High: 83.2°F, Low: 69.2°F (open-meteo) |  |
| 53 | 2027-04-08 | Atlanta, Georgia | Columbia, South Carolina | 64.1 | graphhopper | 3717 | Avg High: 77.8°F, Low: 70.6°F (open-meteo) |  |
| 54 | 2027-04-09 | Columbia, South Carolina | Raleigh, North Carolina | 57.8 | graphhopper | 2586 | Avg High: 71.5°F, Low: 47.5°F (open-meteo) |  |
| 55 | 2027-04-10 | Columbia, South Carolina | Raleigh, North Carolina | 57.8 | graphhopper | 2586 | Avg High: 71.4°F, Low: 41.5°F (open-meteo) |  |
| 56 | 2027-04-11 | Columbia, South Carolina | Raleigh, North Carolina | 57.8 | graphhopper | 2586 | Avg High: 83.4°F, Low: 47.2°F (open-meteo) |  |
| 57 | 2027-04-12 | Columbia, South Carolina | Raleigh, North Carolina | 57.8 | graphhopper | 2586 | Avg High: 84.2°F, Low: 53.8°F (open-meteo) |  |
| 58 | 2027-04-13 | Raleigh, North Carolina | Richmond, Virginia | 65.2 | graphhopper | 3602 | Avg High: 81.8°F, Low: 60.3°F (open-meteo) |  |
| 59 | 2027-04-14 | Raleigh, North Carolina | Richmond, Virginia | 65.2 | graphhopper | 3602 | Avg High: 70.7°F, Low: 55.0°F (open-meteo) |  |
| 60 | 2027-04-15 | Raleigh, North Carolina | Richmond, Virginia | 65.2 | graphhopper | 3602 | Avg High: 67.8°F, Low: 52.5°F (open-meteo) |  |
| 61 | 2027-04-16 | Richmond, Virginia | Charleston, West Virginia | 42.2 | graphhopper | 4494 | Avg High: 68.3°F, Low: 37.1°F (open-meteo) |  |
| 62 | 2027-04-17 | Richmond, Virginia | Charleston, West Virginia | 42.2 | graphhopper | 4494 | Avg High: 75.7°F, Low: 45.9°F (open-meteo) |  |
| 63 | 2027-04-18 | Richmond, Virginia | Charleston, West Virginia | 42.2 | graphhopper | 4494 | Avg High: 79.0°F, Low: 57.3°F (open-meteo) |  |
| 64 | 2027-04-19 | Richmond, Virginia | Charleston, West Virginia | 42.2 | graphhopper | 4494 | Avg High: 77.3°F, Low: 63.0°F (open-meteo) |  |
| 65 | 2027-04-20 | Richmond, Virginia | Charleston, West Virginia | 42.2 | graphhopper | 4494 | Avg High: 69.8°F, Low: 65.9°F (open-meteo) |  |
| 66 | 2027-04-21 | Richmond, Virginia | Charleston, West Virginia | 42.2 | graphhopper | 4494 | Avg High: 75.6°F, Low: 64.8°F (open-meteo) |  |
| 67 | 2027-04-22 | Richmond, Virginia | Charleston, West Virginia | 42.2 | graphhopper | 4494 | Avg High: 75.5°F, Low: 66.3°F (open-meteo) |  |
| 68 | 2027-04-23 | Richmond, Virginia | Charleston, West Virginia | 42.2 | graphhopper | 4494 | Avg High: 74.6°F, Low: 66.2°F (open-meteo) |  |
| 69 | 2027-04-24 | Richmond, Virginia | Charleston, West Virginia | 42.2 | graphhopper | 4494 | Avg High: 70.6°F, Low: 60.8°F (open-meteo) |  |
| 70 | 2027-04-25 | Charleston, West Virginia | Frankfort, Kentucky | 63.9 | graphhopper | 4850 | Avg High: 70.4°F, Low: 52.2°F (open-meteo) |  |
| 71 | 2027-04-26 | Charleston, West Virginia | Frankfort, Kentucky | 63.9 | graphhopper | 4850 | Avg High: 70.8°F, Low: 57.3°F (open-meteo) |  |
| 72 | 2027-04-27 | Charleston, West Virginia | Frankfort, Kentucky | 63.9 | graphhopper | 4850 | Avg High: 69.1°F, Low: 48.8°F (open-meteo) |  |
| 73 | 2027-04-28 | Charleston, West Virginia | Frankfort, Kentucky | 63.9 | graphhopper | 4850 | Avg High: 71.2°F, Low: 42.9°F (open-meteo) |  |
| 74 | 2027-04-29 | Frankfort, Kentucky | Nashville, Tennessee | 57.0 | graphhopper | 3529 | Avg High: 81.7°F, Low: 51.2°F (open-meteo) |  |
| 75 | 2027-04-30 | Frankfort, Kentucky | Nashville, Tennessee | 57.0 | graphhopper | 3529 | Avg High: 83.5°F, Low: 57.2°F (open-meteo) |  |
| 76 | 2027-05-01 | Frankfort, Kentucky | Nashville, Tennessee | 57.0 | graphhopper | 3529 | Avg High: 77.2°F, Low: 58.3°F (open-meteo) |  |
| 77 | 2027-05-02 | Frankfort, Kentucky | Nashville, Tennessee | 57.0 | graphhopper | 3529 | Avg High: 78.1°F, Low: 64.2°F (open-meteo) |  |
| 78 | 2027-05-03 | Nashville, Tennessee | Jefferson City, Missouri | 65.9 | graphhopper | 4236 | Avg High: 53.1°F, Low: 39.1°F (open-meteo) |  |
| 79 | 2027-05-04 | Nashville, Tennessee | Jefferson City, Missouri | 65.9 | graphhopper | 4236 | Avg High: 59.0°F, Low: 34.3°F (open-meteo) |  |
| 80 | 2027-05-05 | Nashville, Tennessee | Jefferson City, Missouri | 65.9 | graphhopper | 4236 | Avg High: 69.8°F, Low: 40.2°F (open-meteo) |  |
| 81 | 2027-05-06 | Nashville, Tennessee | Jefferson City, Missouri | 65.9 | graphhopper | 4236 | Avg High: 76.5°F, Low: 49.2°F (open-meteo) |  |
| 82 | 2027-05-07 | Nashville, Tennessee | Jefferson City, Missouri | 65.9 | graphhopper | 4236 | Avg High: 81.5°F, Low: 54.1°F (open-meteo) |  |
| 83 | 2027-05-08 | Nashville, Tennessee | Jefferson City, Missouri | 65.9 | graphhopper | 4236 | Avg High: 81.7°F, Low: 57.6°F (open-meteo) |  |
| 84 | 2027-05-09 | Nashville, Tennessee | Jefferson City, Missouri | 65.9 | graphhopper | 4236 | Avg High: 85.0°F, Low: 53.3°F (open-meteo) |  |
| 85 | 2027-05-10 | Jefferson City, Missouri | Topeka, Kansas | 58.1 | graphhopper | 3041 | Avg High: 87.1°F, Low: 63.7°F (open-meteo) |  |
| 86 | 2027-05-11 | Jefferson City, Missouri | Topeka, Kansas | 58.1 | graphhopper | 3041 | Avg High: 88.8°F, Low: 65.5°F (open-meteo) |  |
| 87 | 2027-05-12 | Jefferson City, Missouri | Topeka, Kansas | 58.1 | graphhopper | 3041 | Avg High: 87.0°F, Low: 63.4°F (open-meteo) |  |
| 88 | 2027-05-13 | Jefferson City, Missouri | Topeka, Kansas | 58.1 | graphhopper | 3041 | Avg High: 72.3°F, Low: 56.1°F (open-meteo) |  |
| 89 | 2027-05-14 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 69.2°F, Low: 47.4°F (open-meteo) |  |
| 90 | 2027-05-15 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 66.5°F, Low: 45.6°F (open-meteo) |  |
| 91 | 2027-05-16 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 59.9°F, Low: 52.8°F (open-meteo) |  |
| 92 | 2027-05-17 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 68.3°F, Low: 45.2°F (open-meteo) |  |
| 93 | 2027-05-18 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 71.7°F, Low: 51.1°F (open-meteo) |  |
| 94 | 2027-05-19 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 77.8°F, Low: 59.6°F (open-meteo) |  |
| 95 | 2027-05-20 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 79.1°F, Low: 64.5°F (open-meteo) |  |
| 96 | 2027-05-21 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 80.1°F, Low: 60.2°F (open-meteo) |  |
| 97 | 2027-05-22 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 72.9°F, Low: 56.2°F (open-meteo) |  |
| 98 | 2027-05-23 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 75.8°F, Low: 49.4°F (open-meteo) |  |
| 99 | 2027-05-24 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 74.0°F, Low: 53.5°F (open-meteo) |  |
| 100 | 2027-05-25 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 81.9°F, Low: 63.9°F (open-meteo) |  |
| 101 | 2027-05-26 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 77.7°F, Low: 51.1°F (open-meteo) |  |
| 102 | 2027-05-27 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 81.9°F, Low: 61.6°F (open-meteo) |  |
| 103 | 2027-05-28 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 83.5°F, Low: 58.3°F (open-meteo) |  |
| 104 | 2027-05-29 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 81.8°F, Low: 59.1°F (open-meteo) |  |
| 105 | 2027-05-30 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 78.4°F, Low: 70.3°F (open-meteo) |  |
| 106 | 2027-05-31 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 84.8°F, Low: 63.6°F (open-meteo) |  |
| 107 | 2027-06-01 | Harrisburg, Pennsylvania | Washington, DC | 43.1 | graphhopper | 3376 | Avg High: 82.2°F, Low: 66.2°F (open-meteo) |  |
| 108 | 2027-06-02 | Harrisburg, Pennsylvania | Washington, DC | 43.1 | graphhopper | 3376 | Avg High: 79.2°F, Low: 57.4°F (open-meteo) |  |
| 109 | 2027-06-03 | Harrisburg, Pennsylvania | Washington, DC | 43.1 | graphhopper | 3376 | Avg High: 79.2°F, Low: 54.1°F (open-meteo) |  |

</details>

---

### Alternative 4
**Feasible**: Yes
- **Start Date**: 2027-02-15
- **Total Distance**: 6995.2 miles
- **Distance Source**: graphhopper
- **Total Climbing**: 369458 ft
- **Desirability Scores**:
  - Weather Preference: 0.672
  - Distance Score: 0.270
  - Climbing Score: 0.558
  - **Total Desirability Score**: 0.523

<details>
<summary>Click to view daily travel schedule</summary>

| Day | Date | Origin | Destination | Distance (mi) | Distance Source | Ascent (ft) | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | 2027-02-15 | Austin, Texas | Little Rock, Arkansas | 63.5 | graphhopper | 2357 | Avg High: 66.0°F, Low: 60.1°F (open-meteo) |  |
| 2 | 2027-02-16 | Austin, Texas | Little Rock, Arkansas | 63.5 | graphhopper | 2357 | Avg High: 70.9°F, Low: 53.8°F (open-meteo) |  |
| 3 | 2027-02-17 | Austin, Texas | Little Rock, Arkansas | 63.5 | graphhopper | 2357 | Avg High: 66.8°F, Low: 51.3°F (open-meteo) |  |
| 4 | 2027-02-18 | Austin, Texas | Little Rock, Arkansas | 63.5 | graphhopper | 2357 | Avg High: 70.6°F, Low: 50.7°F (open-meteo) |  |
| 5 | 2027-02-19 | Austin, Texas | Little Rock, Arkansas | 63.5 | graphhopper | 2357 | Avg High: 73.7°F, Low: 58.5°F (open-meteo) |  |
| 6 | 2027-02-20 | Austin, Texas | Little Rock, Arkansas | 63.5 | graphhopper | 2357 | Avg High: 74.1°F, Low: 59.4°F (open-meteo) |  |
| 7 | 2027-02-21 | Austin, Texas | Little Rock, Arkansas | 63.5 | graphhopper | 2357 | Avg High: 72.2°F, Low: 57.2°F (open-meteo) |  |
| 8 | 2027-02-22 | Austin, Texas | Little Rock, Arkansas | 63.5 | graphhopper | 2357 | Avg High: 63.8°F, Low: 55.2°F (open-meteo) |  |
| 9 | 2027-02-23 | Austin, Texas | Little Rock, Arkansas | 63.5 | graphhopper | 2357 | Avg High: 57.3°F, Low: 41.0°F (open-meteo) |  |
| 10 | 2027-02-24 | Little Rock, Arkansas | Oklahoma City, Oklahoma | 62.5 | graphhopper | 3322 | Avg High: 65.8°F, Low: 48.9°F (open-meteo) |  |
| 11 | 2027-02-25 | Little Rock, Arkansas | Oklahoma City, Oklahoma | 62.5 | graphhopper | 3322 | Avg High: 69.1°F, Low: 41.0°F (open-meteo) |  |
| 12 | 2027-02-26 | Little Rock, Arkansas | Oklahoma City, Oklahoma | 62.5 | graphhopper | 3322 | Avg High: 69.2°F, Low: 54.8°F (open-meteo) |  |
| 13 | 2027-02-27 | Little Rock, Arkansas | Oklahoma City, Oklahoma | 62.5 | graphhopper | 3322 | Avg High: 62.6°F, Low: 46.3°F (open-meteo) |  |
| 14 | 2027-02-28 | Little Rock, Arkansas | Oklahoma City, Oklahoma | 62.5 | graphhopper | 3322 | Avg High: 52.6°F, Low: 34.0°F (open-meteo) |  |
| 15 | 2027-03-01 | Little Rock, Arkansas | Oklahoma City, Oklahoma | 62.5 | graphhopper | 3322 | Avg High: 65.7°F, Low: 41.0°F (open-meteo) |  |
| 16 | 2027-03-02 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 63.4°F, Low: 38.1°F (open-meteo) |  |
| 17 | 2027-03-03 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 60.9°F, Low: 46.9°F (open-meteo) |  |
| 18 | 2027-03-04 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 53.9°F, Low: 33.1°F (open-meteo) |  |
| 19 | 2027-03-05 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 69.9°F, Low: 45.5°F (open-meteo) |  |
| 20 | 2027-03-06 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 77.6°F, Low: 68.3°F (open-meteo) |  |
| 21 | 2027-03-07 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 67.6°F, Low: 40.3°F (open-meteo) |  |
| 22 | 2027-03-08 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 58.0°F, Low: 36.2°F (open-meteo) |  |
| 23 | 2027-03-09 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 68.7°F, Low: 42.5°F (open-meteo) |  |
| 24 | 2027-03-10 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 73.8°F, Low: 63.2°F (open-meteo) |  |
| 25 | 2027-03-11 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 64.2°F, Low: 48.4°F (open-meteo) |  |
| 26 | 2027-03-12 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 59.1°F, Low: 41.5°F (open-meteo) |  |
| 27 | 2027-03-13 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 64.8°F, Low: 36.3°F (open-meteo) |  |
| 28 | 2027-03-14 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 72.2°F, Low: 39.1°F (open-meteo) |  |
| 29 | 2027-03-15 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 70.8°F, Low: 53.3°F (open-meteo) |  |
| 30 | 2027-03-16 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 70.4°F, Low: 64.2°F (open-meteo) |  |
| 31 | 2027-03-17 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 74.6°F, Low: 48.1°F (open-meteo) |  |
| 32 | 2027-03-18 | Tallahassee, Florida | Baton Rouge, Louisiana | 65.5 | graphhopper | 2248 | Avg High: 72.7°F, Low: 57.8°F (open-meteo) |  |
| 33 | 2027-03-19 | Tallahassee, Florida | Baton Rouge, Louisiana | 65.5 | graphhopper | 2248 | Avg High: 65.2°F, Low: 37.6°F (open-meteo) |  |
| 34 | 2027-03-20 | Tallahassee, Florida | Baton Rouge, Louisiana | 65.5 | graphhopper | 2248 | Avg High: 62.7°F, Low: 41.5°F (open-meteo) |  |
| 35 | 2027-03-21 | Tallahassee, Florida | Baton Rouge, Louisiana | 65.5 | graphhopper | 2248 | Avg High: 69.9°F, Low: 39.1°F (open-meteo) |  |
| 36 | 2027-03-22 | Tallahassee, Florida | Baton Rouge, Louisiana | 65.5 | graphhopper | 2248 | Avg High: 71.7°F, Low: 51.6°F (open-meteo) |  |
| 37 | 2027-03-23 | Tallahassee, Florida | Baton Rouge, Louisiana | 65.5 | graphhopper | 2248 | Avg High: 74.4°F, Low: 58.6°F (open-meteo) |  |
| 38 | 2027-03-24 | Tallahassee, Florida | Baton Rouge, Louisiana | 65.5 | graphhopper | 2248 | Avg High: 72.1°F, Low: 50.6°F (open-meteo) |  |
| 39 | 2027-03-25 | Tallahassee, Florida | Baton Rouge, Louisiana | 65.5 | graphhopper | 2248 | Avg High: 68.5°F, Low: 43.4°F (open-meteo) |  |
| 40 | 2027-03-26 | Baton Rouge, Louisiana | Jackson, Mississippi | 57.6 | graphhopper | 2527 | Avg High: 72.7°F, Low: 43.6°F (open-meteo) |  |
| 41 | 2027-03-27 | Baton Rouge, Louisiana | Jackson, Mississippi | 57.6 | graphhopper | 2527 | Avg High: 70.7°F, Low: 51.2°F (open-meteo) |  |
| 42 | 2027-03-28 | Baton Rouge, Louisiana | Jackson, Mississippi | 57.6 | graphhopper | 2527 | Avg High: 72.2°F, Low: 55.6°F (open-meteo) |  |
| 43 | 2027-03-29 | Jackson, Mississippi | Montgomery, Alabama | 67.6 | graphhopper | 3054 | Avg High: 74.4°F, Low: 49.8°F (open-meteo) |  |
| 44 | 2027-03-30 | Jackson, Mississippi | Montgomery, Alabama | 67.6 | graphhopper | 3054 | Avg High: 75.5°F, Low: 55.9°F (open-meteo) |  |
| 45 | 2027-03-31 | Jackson, Mississippi | Montgomery, Alabama | 67.6 | graphhopper | 3054 | Avg High: 75.5°F, Low: 69.3°F (open-meteo) |  |
| 46 | 2027-04-01 | Jackson, Mississippi | Montgomery, Alabama | 67.6 | graphhopper | 3054 | Avg High: 74.7°F, Low: 58.7°F (open-meteo) |  |
| 47 | 2027-04-02 | Montgomery, Alabama | Atlanta, Georgia | 66.4 | graphhopper | 3698 | Avg High: 64.0°F, Low: 48.1°F (open-meteo) |  |
| 48 | 2027-04-03 | Montgomery, Alabama | Atlanta, Georgia | 66.4 | graphhopper | 3698 | Avg High: 63.0°F, Low: 49.6°F (open-meteo) |  |
| 49 | 2027-04-04 | Montgomery, Alabama | Atlanta, Georgia | 66.4 | graphhopper | 3698 | Avg High: 61.5°F, Low: 57.8°F (open-meteo) |  |
| 50 | 2027-04-05 | Atlanta, Georgia | Columbia, South Carolina | 64.1 | graphhopper | 3717 | Avg High: 66.4°F, Low: 47.7°F (open-meteo) |  |
| 51 | 2027-04-06 | Atlanta, Georgia | Columbia, South Carolina | 64.1 | graphhopper | 3717 | Avg High: 80.6°F, Low: 55.2°F (open-meteo) |  |
| 52 | 2027-04-07 | Atlanta, Georgia | Columbia, South Carolina | 64.1 | graphhopper | 3717 | Avg High: 83.2°F, Low: 69.2°F (open-meteo) |  |
| 53 | 2027-04-08 | Atlanta, Georgia | Columbia, South Carolina | 64.1 | graphhopper | 3717 | Avg High: 77.8°F, Low: 70.6°F (open-meteo) |  |
| 54 | 2027-04-09 | Columbia, South Carolina | Richmond, Virginia | 60.2 | graphhopper | 2990 | Avg High: 66.4°F, Low: 48.9°F (open-meteo) |  |
| 55 | 2027-04-10 | Columbia, South Carolina | Richmond, Virginia | 60.2 | graphhopper | 2990 | Avg High: 71.9°F, Low: 39.4°F (open-meteo) |  |
| 56 | 2027-04-11 | Columbia, South Carolina | Richmond, Virginia | 60.2 | graphhopper | 2990 | Avg High: 82.5°F, Low: 50.0°F (open-meteo) |  |
| 57 | 2027-04-12 | Columbia, South Carolina | Richmond, Virginia | 60.2 | graphhopper | 2990 | Avg High: 88.4°F, Low: 56.7°F (open-meteo) |  |
| 58 | 2027-04-13 | Columbia, South Carolina | Richmond, Virginia | 60.2 | graphhopper | 2990 | Avg High: 81.8°F, Low: 60.3°F (open-meteo) |  |
| 59 | 2027-04-14 | Columbia, South Carolina | Richmond, Virginia | 60.2 | graphhopper | 2990 | Avg High: 70.7°F, Low: 55.0°F (open-meteo) |  |
| 60 | 2027-04-15 | Columbia, South Carolina | Richmond, Virginia | 60.2 | graphhopper | 2990 | Avg High: 67.8°F, Low: 52.5°F (open-meteo) |  |
| 61 | 2027-04-16 | Richmond, Virginia | Raleigh, North Carolina | 65.5 | graphhopper | 3717 | Avg High: 69.3°F, Low: 44.1°F (open-meteo) |  |
| 62 | 2027-04-17 | Richmond, Virginia | Raleigh, North Carolina | 65.5 | graphhopper | 3717 | Avg High: 74.4°F, Low: 44.9°F (open-meteo) |  |
| 63 | 2027-04-18 | Richmond, Virginia | Raleigh, North Carolina | 65.5 | graphhopper | 3717 | Avg High: 75.4°F, Low: 53.6°F (open-meteo) |  |
| 64 | 2027-04-19 | Raleigh, North Carolina | Charleston, West Virginia | 43.9 | graphhopper | 4574 | Avg High: 77.3°F, Low: 63.0°F (open-meteo) |  |
| 65 | 2027-04-20 | Raleigh, North Carolina | Charleston, West Virginia | 43.9 | graphhopper | 4574 | Avg High: 69.8°F, Low: 65.9°F (open-meteo) |  |
| 66 | 2027-04-21 | Raleigh, North Carolina | Charleston, West Virginia | 43.9 | graphhopper | 4574 | Avg High: 75.6°F, Low: 64.8°F (open-meteo) |  |
| 67 | 2027-04-22 | Raleigh, North Carolina | Charleston, West Virginia | 43.9 | graphhopper | 4574 | Avg High: 75.5°F, Low: 66.3°F (open-meteo) |  |
| 68 | 2027-04-23 | Raleigh, North Carolina | Charleston, West Virginia | 43.9 | graphhopper | 4574 | Avg High: 74.6°F, Low: 66.2°F (open-meteo) |  |
| 69 | 2027-04-24 | Raleigh, North Carolina | Charleston, West Virginia | 43.9 | graphhopper | 4574 | Avg High: 70.6°F, Low: 60.8°F (open-meteo) |  |
| 70 | 2027-04-25 | Raleigh, North Carolina | Charleston, West Virginia | 43.9 | graphhopper | 4574 | Avg High: 69.8°F, Low: 54.5°F (open-meteo) |  |
| 71 | 2027-04-26 | Raleigh, North Carolina | Charleston, West Virginia | 43.9 | graphhopper | 4574 | Avg High: 66.2°F, Low: 55.8°F (open-meteo) |  |
| 72 | 2027-04-27 | Charleston, West Virginia | Frankfort, Kentucky | 63.9 | graphhopper | 4850 | Avg High: 69.1°F, Low: 48.8°F (open-meteo) |  |
| 73 | 2027-04-28 | Charleston, West Virginia | Frankfort, Kentucky | 63.9 | graphhopper | 4850 | Avg High: 71.2°F, Low: 42.9°F (open-meteo) |  |
| 74 | 2027-04-29 | Charleston, West Virginia | Frankfort, Kentucky | 63.9 | graphhopper | 4850 | Avg High: 79.0°F, Low: 51.6°F (open-meteo) |  |
| 75 | 2027-04-30 | Charleston, West Virginia | Frankfort, Kentucky | 63.9 | graphhopper | 4850 | Avg High: 84.1°F, Low: 60.0°F (open-meteo) |  |
| 76 | 2027-05-01 | Frankfort, Kentucky | Nashville, Tennessee | 57.0 | graphhopper | 3529 | Avg High: 77.2°F, Low: 58.3°F (open-meteo) |  |
| 77 | 2027-05-02 | Frankfort, Kentucky | Nashville, Tennessee | 57.0 | graphhopper | 3529 | Avg High: 78.1°F, Low: 64.2°F (open-meteo) |  |
| 78 | 2027-05-03 | Frankfort, Kentucky | Nashville, Tennessee | 57.0 | graphhopper | 3529 | Avg High: 61.0°F, Low: 43.0°F (open-meteo) |  |
| 79 | 2027-05-04 | Frankfort, Kentucky | Nashville, Tennessee | 57.0 | graphhopper | 3529 | Avg High: 57.1°F, Low: 37.4°F (open-meteo) |  |
| 80 | 2027-05-05 | Nashville, Tennessee | Jefferson City, Missouri | 65.9 | graphhopper | 4236 | Avg High: 69.8°F, Low: 40.2°F (open-meteo) |  |
| 81 | 2027-05-06 | Nashville, Tennessee | Jefferson City, Missouri | 65.9 | graphhopper | 4236 | Avg High: 76.5°F, Low: 49.2°F (open-meteo) |  |
| 82 | 2027-05-07 | Nashville, Tennessee | Jefferson City, Missouri | 65.9 | graphhopper | 4236 | Avg High: 81.5°F, Low: 54.1°F (open-meteo) |  |
| 83 | 2027-05-08 | Nashville, Tennessee | Jefferson City, Missouri | 65.9 | graphhopper | 4236 | Avg High: 81.7°F, Low: 57.6°F (open-meteo) |  |
| 84 | 2027-05-09 | Nashville, Tennessee | Jefferson City, Missouri | 65.9 | graphhopper | 4236 | Avg High: 85.0°F, Low: 53.3°F (open-meteo) |  |
| 85 | 2027-05-10 | Nashville, Tennessee | Jefferson City, Missouri | 65.9 | graphhopper | 4236 | Avg High: 86.8°F, Low: 56.9°F (open-meteo) |  |
| 86 | 2027-05-11 | Nashville, Tennessee | Jefferson City, Missouri | 65.9 | graphhopper | 4236 | Avg High: 87.3°F, Low: 66.4°F (open-meteo) |  |
| 87 | 2027-05-12 | Jefferson City, Missouri | Topeka, Kansas | 58.1 | graphhopper | 3041 | Avg High: 87.0°F, Low: 63.4°F (open-meteo) |  |
| 88 | 2027-05-13 | Jefferson City, Missouri | Topeka, Kansas | 58.1 | graphhopper | 3041 | Avg High: 72.3°F, Low: 56.1°F (open-meteo) |  |
| 89 | 2027-05-14 | Jefferson City, Missouri | Topeka, Kansas | 58.1 | graphhopper | 3041 | Avg High: 75.1°F, Low: 57.9°F (open-meteo) |  |
| 90 | 2027-05-15 | Jefferson City, Missouri | Topeka, Kansas | 58.1 | graphhopper | 3041 | Avg High: 80.5°F, Low: 63.8°F (open-meteo) |  |
| 91 | 2027-05-16 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 59.9°F, Low: 52.8°F (open-meteo) |  |
| 92 | 2027-05-17 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 68.3°F, Low: 45.2°F (open-meteo) |  |
| 93 | 2027-05-18 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 71.7°F, Low: 51.1°F (open-meteo) |  |
| 94 | 2027-05-19 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 77.8°F, Low: 59.6°F (open-meteo) |  |
| 95 | 2027-05-20 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 79.1°F, Low: 64.5°F (open-meteo) |  |
| 96 | 2027-05-21 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 80.1°F, Low: 60.2°F (open-meteo) |  |
| 97 | 2027-05-22 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 72.9°F, Low: 56.2°F (open-meteo) |  |
| 98 | 2027-05-23 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 75.8°F, Low: 49.4°F (open-meteo) |  |
| 99 | 2027-05-24 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 74.0°F, Low: 53.5°F (open-meteo) |  |
| 100 | 2027-05-25 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 81.9°F, Low: 63.9°F (open-meteo) |  |
| 101 | 2027-05-26 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 77.7°F, Low: 51.1°F (open-meteo) |  |
| 102 | 2027-05-27 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 81.9°F, Low: 61.6°F (open-meteo) |  |
| 103 | 2027-05-28 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 83.5°F, Low: 58.3°F (open-meteo) |  |
| 104 | 2027-05-29 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 81.8°F, Low: 59.1°F (open-meteo) |  |
| 105 | 2027-05-30 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 78.4°F, Low: 70.3°F (open-meteo) |  |
| 106 | 2027-05-31 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 84.8°F, Low: 63.6°F (open-meteo) |  |
| 107 | 2027-06-01 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 78.3°F, Low: 58.0°F (open-meteo) |  |
| 108 | 2027-06-02 | Topeka, Kansas | Harrisburg, Pennsylvania | 69.5 | graphhopper | 3591 | Avg High: 78.7°F, Low: 54.3°F (open-meteo) |  |
| 109 | 2027-06-03 | Harrisburg, Pennsylvania | Washington, DC | 43.1 | graphhopper | 3376 | Avg High: 79.2°F, Low: 54.1°F (open-meteo) |  |
| 110 | 2027-06-04 | Harrisburg, Pennsylvania | Washington, DC | 43.1 | graphhopper | 3376 | Avg High: 89.0°F, Low: 61.0°F (open-meteo) |  |
| 111 | 2027-06-05 | Harrisburg, Pennsylvania | Washington, DC | 43.1 | graphhopper | 3376 | Avg High: 84.8°F, Low: 71.2°F (open-meteo) |  |

</details>

---

### Alternative 5
**Feasible**: Yes
- **Start Date**: 2027-02-15
- **Total Distance**: 6923.8 miles
- **Distance Source**: graphhopper
- **Total Climbing**: 371196 ft
- **Desirability Scores**:
  - Weather Preference: 0.662
  - Distance Score: 0.276
  - Climbing Score: 0.551
  - **Total Desirability Score**: 0.518

<details>
<summary>Click to view daily travel schedule</summary>

| Day | Date | Origin | Destination | Distance (mi) | Distance Source | Ascent (ft) | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | 2027-02-15 | Austin, Texas | Little Rock, Arkansas | 63.5 | graphhopper | 2357 | Avg High: 66.0°F, Low: 60.1°F (open-meteo) |  |
| 2 | 2027-02-16 | Austin, Texas | Little Rock, Arkansas | 63.5 | graphhopper | 2357 | Avg High: 70.9°F, Low: 53.8°F (open-meteo) |  |
| 3 | 2027-02-17 | Austin, Texas | Little Rock, Arkansas | 63.5 | graphhopper | 2357 | Avg High: 66.8°F, Low: 51.3°F (open-meteo) |  |
| 4 | 2027-02-18 | Austin, Texas | Little Rock, Arkansas | 63.5 | graphhopper | 2357 | Avg High: 70.6°F, Low: 50.7°F (open-meteo) |  |
| 5 | 2027-02-19 | Austin, Texas | Little Rock, Arkansas | 63.5 | graphhopper | 2357 | Avg High: 73.7°F, Low: 58.5°F (open-meteo) |  |
| 6 | 2027-02-20 | Austin, Texas | Little Rock, Arkansas | 63.5 | graphhopper | 2357 | Avg High: 74.1°F, Low: 59.4°F (open-meteo) |  |
| 7 | 2027-02-21 | Austin, Texas | Little Rock, Arkansas | 63.5 | graphhopper | 2357 | Avg High: 72.2°F, Low: 57.2°F (open-meteo) |  |
| 8 | 2027-02-22 | Austin, Texas | Little Rock, Arkansas | 63.5 | graphhopper | 2357 | Avg High: 63.8°F, Low: 55.2°F (open-meteo) |  |
| 9 | 2027-02-23 | Austin, Texas | Little Rock, Arkansas | 63.5 | graphhopper | 2357 | Avg High: 57.3°F, Low: 41.0°F (open-meteo) |  |
| 10 | 2027-02-24 | Little Rock, Arkansas | Oklahoma City, Oklahoma | 62.5 | graphhopper | 3322 | Avg High: 65.8°F, Low: 48.9°F (open-meteo) |  |
| 11 | 2027-02-25 | Little Rock, Arkansas | Oklahoma City, Oklahoma | 62.5 | graphhopper | 3322 | Avg High: 69.1°F, Low: 41.0°F (open-meteo) |  |
| 12 | 2027-02-26 | Little Rock, Arkansas | Oklahoma City, Oklahoma | 62.5 | graphhopper | 3322 | Avg High: 69.2°F, Low: 54.8°F (open-meteo) |  |
| 13 | 2027-02-27 | Little Rock, Arkansas | Oklahoma City, Oklahoma | 62.5 | graphhopper | 3322 | Avg High: 62.6°F, Low: 46.3°F (open-meteo) |  |
| 14 | 2027-02-28 | Little Rock, Arkansas | Oklahoma City, Oklahoma | 62.5 | graphhopper | 3322 | Avg High: 52.6°F, Low: 34.0°F (open-meteo) |  |
| 15 | 2027-03-01 | Little Rock, Arkansas | Oklahoma City, Oklahoma | 62.5 | graphhopper | 3322 | Avg High: 65.7°F, Low: 41.0°F (open-meteo) |  |
| 16 | 2027-03-02 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 63.4°F, Low: 38.1°F (open-meteo) |  |
| 17 | 2027-03-03 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 60.9°F, Low: 46.9°F (open-meteo) |  |
| 18 | 2027-03-04 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 53.9°F, Low: 33.1°F (open-meteo) |  |
| 19 | 2027-03-05 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 69.9°F, Low: 45.5°F (open-meteo) |  |
| 20 | 2027-03-06 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 77.6°F, Low: 68.3°F (open-meteo) |  |
| 21 | 2027-03-07 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 67.6°F, Low: 40.3°F (open-meteo) |  |
| 22 | 2027-03-08 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 58.0°F, Low: 36.2°F (open-meteo) |  |
| 23 | 2027-03-09 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 68.7°F, Low: 42.5°F (open-meteo) |  |
| 24 | 2027-03-10 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 73.8°F, Low: 63.2°F (open-meteo) |  |
| 25 | 2027-03-11 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 64.2°F, Low: 48.4°F (open-meteo) |  |
| 26 | 2027-03-12 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 59.1°F, Low: 41.5°F (open-meteo) |  |
| 27 | 2027-03-13 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 64.8°F, Low: 36.3°F (open-meteo) |  |
| 28 | 2027-03-14 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 72.2°F, Low: 39.1°F (open-meteo) |  |
| 29 | 2027-03-15 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 70.8°F, Low: 53.3°F (open-meteo) |  |
| 30 | 2027-03-16 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 70.4°F, Low: 64.2°F (open-meteo) |  |
| 31 | 2027-03-17 | Oklahoma City, Oklahoma | Tallahassee, Florida | 68.8 | graphhopper | 2863 | Avg High: 74.6°F, Low: 48.1°F (open-meteo) |  |
| 32 | 2027-03-18 | Tallahassee, Florida | Baton Rouge, Louisiana | 65.5 | graphhopper | 2248 | Avg High: 72.7°F, Low: 57.8°F (open-meteo) |  |
| 33 | 2027-03-19 | Tallahassee, Florida | Baton Rouge, Louisiana | 65.5 | graphhopper | 2248 | Avg High: 65.2°F, Low: 37.6°F (open-meteo) |  |
| 34 | 2027-03-20 | Tallahassee, Florida | Baton Rouge, Louisiana | 65.5 | graphhopper | 2248 | Avg High: 62.7°F, Low: 41.5°F (open-meteo) |  |
| 35 | 2027-03-21 | Tallahassee, Florida | Baton Rouge, Louisiana | 65.5 | graphhopper | 2248 | Avg High: 69.9°F, Low: 39.1°F (open-meteo) |  |
| 36 | 2027-03-22 | Tallahassee, Florida | Baton Rouge, Louisiana | 65.5 | graphhopper | 2248 | Avg High: 71.7°F, Low: 51.6°F (open-meteo) |  |
| 37 | 2027-03-23 | Tallahassee, Florida | Baton Rouge, Louisiana | 65.5 | graphhopper | 2248 | Avg High: 74.4°F, Low: 58.6°F (open-meteo) |  |
| 38 | 2027-03-24 | Tallahassee, Florida | Baton Rouge, Louisiana | 65.5 | graphhopper | 2248 | Avg High: 72.1°F, Low: 50.6°F (open-meteo) |  |
| 39 | 2027-03-25 | Tallahassee, Florida | Baton Rouge, Louisiana | 65.5 | graphhopper | 2248 | Avg High: 68.5°F, Low: 43.4°F (open-meteo) |  |
| 40 | 2027-03-26 | Baton Rouge, Louisiana | Jackson, Mississippi | 57.6 | graphhopper | 2527 | Avg High: 72.7°F, Low: 43.6°F (open-meteo) |  |
| 41 | 2027-03-27 | Baton Rouge, Louisiana | Jackson, Mississippi | 57.6 | graphhopper | 2527 | Avg High: 70.7°F, Low: 51.2°F (open-meteo) |  |
| 42 | 2027-03-28 | Baton Rouge, Louisiana | Jackson, Mississippi | 57.6 | graphhopper | 2527 | Avg High: 72.2°F, Low: 55.6°F (open-meteo) |  |
| 43 | 2027-03-29 | Jackson, Mississippi | Montgomery, Alabama | 67.6 | graphhopper | 3054 | Avg High: 74.4°F, Low: 49.8°F (open-meteo) |  |
| 44 | 2027-03-30 | Jackson, Mississippi | Montgomery, Alabama | 67.6 | graphhopper | 3054 | Avg High: 75.5°F, Low: 55.9°F (open-meteo) |  |
| 45 | 2027-03-31 | Jackson, Mississippi | Montgomery, Alabama | 67.6 | graphhopper | 3054 | Avg High: 75.5°F, Low: 69.3°F (open-meteo) |  |
| 46 | 2027-04-01 | Jackson, Mississippi | Montgomery, Alabama | 67.6 | graphhopper | 3054 | Avg High: 74.7°F, Low: 58.7°F (open-meteo) |  |
| 47 | 2027-04-02 | Montgomery, Alabama | Atlanta, Georgia | 66.4 | graphhopper | 3698 | Avg High: 64.0°F, Low: 48.1°F (open-meteo) |  |
| 48 | 2027-04-03 | Montgomery, Alabama | Atlanta, Georgia | 66.4 | graphhopper | 3698 | Avg High: 63.0°F, Low: 49.6°F (open-meteo) |  |
| 49 | 2027-04-04 | Montgomery, Alabama | Atlanta, Georgia | 66.4 | graphhopper | 3698 | Avg High: 61.5°F, Low: 57.8°F (open-meteo) |  |
| 50 | 2027-04-05 | Atlanta, Georgia | Columbia, South Carolina | 64.1 | graphhopper | 3717 | Avg High: 66.4°F, Low: 47.7°F (open-meteo) |  |
| 51 | 2027-04-06 | Atlanta, Georgia | Columbia, South Carolina | 64.1 | graphhopper | 3717 | Avg High: 80.6°F, Low: 55.2°F (open-meteo) |  |
| 52 | 2027-04-07 | Atlanta, Georgia | Columbia, South Carolina | 64.1 | graphhopper | 3717 | Avg High: 83.2°F, Low: 69.2°F (open-meteo) |  |
| 53 | 2027-04-08 | Atlanta, Georgia | Columbia, South Carolina | 64.1 | graphhopper | 3717 | Avg High: 77.8°F, Low: 70.6°F (open-meteo) |  |
| 54 | 2027-04-09 | Columbia, South Carolina | Raleigh, North Carolina | 57.8 | graphhopper | 2586 | Avg High: 71.5°F, Low: 47.5°F (open-meteo) |  |
| 55 | 2027-04-10 | Columbia, South Carolina | Raleigh, North Carolina | 57.8 | graphhopper | 2586 | Avg High: 71.4°F, Low: 41.5°F (open-meteo) |  |
| 56 | 2027-04-11 | Columbia, South Carolina | Raleigh, North Carolina | 57.8 | graphhopper | 2586 | Avg High: 83.4°F, Low: 47.2°F (open-meteo) |  |
| 57 | 2027-04-12 | Columbia, South Carolina | Raleigh, North Carolina | 57.8 | graphhopper | 2586 | Avg High: 84.2°F, Low: 53.8°F (open-meteo) |  |
| 58 | 2027-04-13 | Raleigh, North Carolina | Richmond, Virginia | 65.2 | graphhopper | 3602 | Avg High: 81.8°F, Low: 60.3°F (open-meteo) |  |
| 59 | 2027-04-14 | Raleigh, North Carolina | Richmond, Virginia | 65.2 | graphhopper | 3602 | Avg High: 70.7°F, Low: 55.0°F (open-meteo) |  |
| 60 | 2027-04-15 | Raleigh, North Carolina | Richmond, Virginia | 65.2 | graphhopper | 3602 | Avg High: 67.8°F, Low: 52.5°F (open-meteo) |  |
| 61 | 2027-04-16 | Richmond, Virginia | Charleston, West Virginia | 42.2 | graphhopper | 4494 | Avg High: 68.3°F, Low: 37.1°F (open-meteo) |  |
| 62 | 2027-04-17 | Richmond, Virginia | Charleston, West Virginia | 42.2 | graphhopper | 4494 | Avg High: 75.7°F, Low: 45.9°F (open-meteo) |  |
| 63 | 2027-04-18 | Richmond, Virginia | Charleston, West Virginia | 42.2 | graphhopper | 4494 | Avg High: 79.0°F, Low: 57.3°F (open-meteo) |  |
| 64 | 2027-04-19 | Richmond, Virginia | Charleston, West Virginia | 42.2 | graphhopper | 4494 | Avg High: 77.3°F, Low: 63.0°F (open-meteo) |  |
| 65 | 2027-04-20 | Richmond, Virginia | Charleston, West Virginia | 42.2 | graphhopper | 4494 | Avg High: 69.8°F, Low: 65.9°F (open-meteo) |  |
| 66 | 2027-04-21 | Richmond, Virginia | Charleston, West Virginia | 42.2 | graphhopper | 4494 | Avg High: 75.6°F, Low: 64.8°F (open-meteo) |  |
| 67 | 2027-04-22 | Richmond, Virginia | Charleston, West Virginia | 42.2 | graphhopper | 4494 | Avg High: 75.5°F, Low: 66.3°F (open-meteo) |  |
| 68 | 2027-04-23 | Richmond, Virginia | Charleston, West Virginia | 42.2 | graphhopper | 4494 | Avg High: 74.6°F, Low: 66.2°F (open-meteo) |  |
| 69 | 2027-04-24 | Richmond, Virginia | Charleston, West Virginia | 42.2 | graphhopper | 4494 | Avg High: 70.6°F, Low: 60.8°F (open-meteo) |  |
| 70 | 2027-04-25 | Charleston, West Virginia | Frankfort, Kentucky | 63.9 | graphhopper | 4850 | Avg High: 70.4°F, Low: 52.2°F (open-meteo) |  |
| 71 | 2027-04-26 | Charleston, West Virginia | Frankfort, Kentucky | 63.9 | graphhopper | 4850 | Avg High: 70.8°F, Low: 57.3°F (open-meteo) |  |
| 72 | 2027-04-27 | Charleston, West Virginia | Frankfort, Kentucky | 63.9 | graphhopper | 4850 | Avg High: 69.1°F, Low: 48.8°F (open-meteo) |  |
| 73 | 2027-04-28 | Charleston, West Virginia | Frankfort, Kentucky | 63.9 | graphhopper | 4850 | Avg High: 71.2°F, Low: 42.9°F (open-meteo) |  |
| 74 | 2027-04-29 | Frankfort, Kentucky | Jefferson City, Missouri | 69.1 | graphhopper | 3494 | Avg High: 83.2°F, Low: 61.2°F (open-meteo) |  |
| 75 | 2027-04-30 | Frankfort, Kentucky | Jefferson City, Missouri | 69.1 | graphhopper | 3494 | Avg High: 79.4°F, Low: 57.6°F (open-meteo) |  |
| 76 | 2027-05-01 | Frankfort, Kentucky | Jefferson City, Missouri | 69.1 | graphhopper | 3494 | Avg High: 77.4°F, Low: 58.7°F (open-meteo) |  |
| 77 | 2027-05-02 | Frankfort, Kentucky | Jefferson City, Missouri | 69.1 | graphhopper | 3494 | Avg High: 69.3°F, Low: 46.1°F (open-meteo) |  |
| 78 | 2027-05-03 | Frankfort, Kentucky | Jefferson City, Missouri | 69.1 | graphhopper | 3494 | Avg High: 53.1°F, Low: 39.1°F (open-meteo) |  |
| 79 | 2027-05-04 | Frankfort, Kentucky | Jefferson City, Missouri | 69.1 | graphhopper | 3494 | Avg High: 59.0°F, Low: 34.3°F (open-meteo) |  |
| 80 | 2027-05-05 | Frankfort, Kentucky | Jefferson City, Missouri | 69.1 | graphhopper | 3494 | Avg High: 69.8°F, Low: 40.2°F (open-meteo) |  |
| 81 | 2027-05-06 | Jefferson City, Missouri | Topeka, Kansas | 58.1 | graphhopper | 3041 | Avg High: 78.4°F, Low: 52.2°F (open-meteo) |  |
| 82 | 2027-05-07 | Jefferson City, Missouri | Topeka, Kansas | 58.1 | graphhopper | 3041 | Avg High: 82.2°F, Low: 57.8°F (open-meteo) |  |
| 83 | 2027-05-08 | Jefferson City, Missouri | Topeka, Kansas | 58.1 | graphhopper | 3041 | Avg High: 82.4°F, Low: 58.4°F (open-meteo) |  |
| 84 | 2027-05-09 | Jefferson City, Missouri | Topeka, Kansas | 58.1 | graphhopper | 3041 | Avg High: 85.3°F, Low: 61.2°F (open-meteo) |  |
| 85 | 2027-05-10 | Topeka, Kansas | Nashville, Tennessee | 66.9 | graphhopper | 3199 | Avg High: 81.2°F, Low: 62.0°F (open-meteo) |  |
| 86 | 2027-05-11 | Topeka, Kansas | Nashville, Tennessee | 66.9 | graphhopper | 3199 | Avg High: 84.6°F, Low: 68.4°F (open-meteo) |  |
| 87 | 2027-05-12 | Topeka, Kansas | Nashville, Tennessee | 66.9 | graphhopper | 3199 | Avg High: 87.4°F, Low: 63.7°F (open-meteo) |  |
| 88 | 2027-05-13 | Topeka, Kansas | Nashville, Tennessee | 66.9 | graphhopper | 3199 | Avg High: 83.3°F, Low: 65.7°F (open-meteo) |  |
| 89 | 2027-05-14 | Topeka, Kansas | Nashville, Tennessee | 66.9 | graphhopper | 3199 | Avg High: 81.6°F, Low: 59.5°F (open-meteo) |  |
| 90 | 2027-05-15 | Topeka, Kansas | Nashville, Tennessee | 66.9 | graphhopper | 3199 | Avg High: 80.4°F, Low: 68.2°F (open-meteo) |  |
| 91 | 2027-05-16 | Topeka, Kansas | Nashville, Tennessee | 66.9 | graphhopper | 3199 | Avg High: 84.1°F, Low: 70.8°F (open-meteo) |  |
| 92 | 2027-05-17 | Topeka, Kansas | Nashville, Tennessee | 66.9 | graphhopper | 3199 | Avg High: 82.0°F, Low: 70.5°F (open-meteo) |  |
| 93 | 2027-05-18 | Topeka, Kansas | Nashville, Tennessee | 66.9 | graphhopper | 3199 | Avg High: 78.5°F, Low: 71.7°F (open-meteo) |  |
| 94 | 2027-05-19 | Topeka, Kansas | Nashville, Tennessee | 66.9 | graphhopper | 3199 | Avg High: 75.6°F, Low: 72.2°F (open-meteo) |  |
| 95 | 2027-05-20 | Topeka, Kansas | Nashville, Tennessee | 66.9 | graphhopper | 3199 | Avg High: 81.9°F, Low: 67.2°F (open-meteo) |  |
| 96 | 2027-05-21 | Nashville, Tennessee | Harrisburg, Pennsylvania | 67.5 | graphhopper | 4798 | Avg High: 80.1°F, Low: 60.2°F (open-meteo) |  |
| 97 | 2027-05-22 | Nashville, Tennessee | Harrisburg, Pennsylvania | 67.5 | graphhopper | 4798 | Avg High: 72.9°F, Low: 56.2°F (open-meteo) |  |
| 98 | 2027-05-23 | Nashville, Tennessee | Harrisburg, Pennsylvania | 67.5 | graphhopper | 4798 | Avg High: 75.8°F, Low: 49.4°F (open-meteo) |  |
| 99 | 2027-05-24 | Nashville, Tennessee | Harrisburg, Pennsylvania | 67.5 | graphhopper | 4798 | Avg High: 74.0°F, Low: 53.5°F (open-meteo) |  |
| 100 | 2027-05-25 | Nashville, Tennessee | Harrisburg, Pennsylvania | 67.5 | graphhopper | 4798 | Avg High: 81.9°F, Low: 63.9°F (open-meteo) |  |
| 101 | 2027-05-26 | Nashville, Tennessee | Harrisburg, Pennsylvania | 67.5 | graphhopper | 4798 | Avg High: 77.7°F, Low: 51.1°F (open-meteo) |  |
| 102 | 2027-05-27 | Nashville, Tennessee | Harrisburg, Pennsylvania | 67.5 | graphhopper | 4798 | Avg High: 81.9°F, Low: 61.6°F (open-meteo) |  |
| 103 | 2027-05-28 | Nashville, Tennessee | Harrisburg, Pennsylvania | 67.5 | graphhopper | 4798 | Avg High: 83.5°F, Low: 58.3°F (open-meteo) |  |
| 104 | 2027-05-29 | Nashville, Tennessee | Harrisburg, Pennsylvania | 67.5 | graphhopper | 4798 | Avg High: 81.8°F, Low: 59.1°F (open-meteo) |  |
| 105 | 2027-05-30 | Nashville, Tennessee | Harrisburg, Pennsylvania | 67.5 | graphhopper | 4798 | Avg High: 78.4°F, Low: 70.3°F (open-meteo) |  |
| 106 | 2027-05-31 | Nashville, Tennessee | Harrisburg, Pennsylvania | 67.5 | graphhopper | 4798 | Avg High: 84.8°F, Low: 63.6°F (open-meteo) |  |
| 107 | 2027-06-01 | Nashville, Tennessee | Harrisburg, Pennsylvania | 67.5 | graphhopper | 4798 | Avg High: 78.3°F, Low: 58.0°F (open-meteo) |  |
| 108 | 2027-06-02 | Harrisburg, Pennsylvania | Washington, DC | 43.1 | graphhopper | 3376 | Avg High: 79.2°F, Low: 57.4°F (open-meteo) |  |
| 109 | 2027-06-03 | Harrisburg, Pennsylvania | Washington, DC | 43.1 | graphhopper | 3376 | Avg High: 79.2°F, Low: 54.1°F (open-meteo) |  |
| 110 | 2027-06-04 | Harrisburg, Pennsylvania | Washington, DC | 43.1 | graphhopper | 3376 | Avg High: 89.0°F, Low: 61.0°F (open-meteo) |  |

</details>

---

### Alternative 6
**Feasible**: Yes
- **Start Date**: 2027-02-01
- **Total Distance**: 7118.0 miles
- **Distance Source**: graphhopper
- **Total Climbing**: 374305 ft
- **Desirability Scores**:
  - Weather Preference: 0.677
  - Distance Score: 0.261
  - Climbing Score: 0.538
  - **Total Desirability Score**: 0.517

<details>
<summary>Click to view daily travel schedule</summary>

| Day | Date | Origin | Destination | Distance (mi) | Distance Source | Ascent (ft) | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | 2027-02-01 | Austin, Texas | Baton Rouge, Louisiana | 64.5 | graphhopper | 1974 | Avg High: 69.2°F, Low: 41.0°F (open-meteo) |  |
| 2 | 2027-02-02 | Austin, Texas | Baton Rouge, Louisiana | 64.5 | graphhopper | 1974 | Avg High: 65.3°F, Low: 43.5°F (open-meteo) |  |
| 3 | 2027-02-03 | Austin, Texas | Baton Rouge, Louisiana | 64.5 | graphhopper | 1974 | Avg High: 68.2°F, Low: 46.5°F (open-meteo) |  |
| 4 | 2027-02-04 | Austin, Texas | Baton Rouge, Louisiana | 64.5 | graphhopper | 1974 | Avg High: 68.5°F, Low: 45.9°F (open-meteo) |  |
| 5 | 2027-02-05 | Austin, Texas | Baton Rouge, Louisiana | 64.5 | graphhopper | 1974 | Avg High: 70.2°F, Low: 45.6°F (open-meteo) |  |
| 6 | 2027-02-06 | Austin, Texas | Baton Rouge, Louisiana | 64.5 | graphhopper | 1974 | Avg High: 68.6°F, Low: 56.2°F (open-meteo) |  |
| 7 | 2027-02-07 | Austin, Texas | Baton Rouge, Louisiana | 64.5 | graphhopper | 1974 | Avg High: 70.3°F, Low: 60.7°F (open-meteo) |  |
| 8 | 2027-02-08 | Austin, Texas | Baton Rouge, Louisiana | 64.5 | graphhopper | 1974 | Avg High: 70.5°F, Low: 61.3°F (open-meteo) |  |
| 9 | 2027-02-09 | Austin, Texas | Baton Rouge, Louisiana | 64.5 | graphhopper | 1974 | Avg High: 74.9°F, Low: 62.8°F (open-meteo) |  |
| 10 | 2027-02-10 | Baton Rouge, Louisiana | Montgomery, Alabama | 68.3 | graphhopper | 2882 | Avg High: 71.8°F, Low: 52.7°F (open-meteo) |  |
| 11 | 2027-02-11 | Baton Rouge, Louisiana | Montgomery, Alabama | 68.3 | graphhopper | 2882 | Avg High: 75.7°F, Low: 49.1°F (open-meteo) |  |
| 12 | 2027-02-12 | Baton Rouge, Louisiana | Montgomery, Alabama | 68.3 | graphhopper | 2882 | Avg High: 72.1°F, Low: 60.5°F (open-meteo) |  |
| 13 | 2027-02-13 | Baton Rouge, Louisiana | Montgomery, Alabama | 68.3 | graphhopper | 2882 | Avg High: 67.8°F, Low: 47.4°F (open-meteo) |  |
| 14 | 2027-02-14 | Baton Rouge, Louisiana | Montgomery, Alabama | 68.3 | graphhopper | 2882 | Avg High: 62.6°F, Low: 54.8°F (open-meteo) |  |
| 15 | 2027-02-15 | Baton Rouge, Louisiana | Montgomery, Alabama | 68.3 | graphhopper | 2882 | Avg High: 71.0°F, Low: 58.5°F (open-meteo) |  |
| 16 | 2027-02-16 | Montgomery, Alabama | Atlanta, Georgia | 66.4 | graphhopper | 3698 | Avg High: 71.7°F, Low: 63.3°F (open-meteo) |  |
| 17 | 2027-02-17 | Montgomery, Alabama | Atlanta, Georgia | 66.4 | graphhopper | 3698 | Avg High: 67.7°F, Low: 49.1°F (open-meteo) |  |
| 18 | 2027-02-18 | Montgomery, Alabama | Atlanta, Georgia | 66.4 | graphhopper | 3698 | Avg High: 69.5°F, Low: 46.7°F (open-meteo) |  |
| 19 | 2027-02-19 | Atlanta, Georgia | Tallahassee, Florida | 62.7 | graphhopper | 2895 | Avg High: 77.6°F, Low: 54.1°F (open-meteo) |  |
| 20 | 2027-02-20 | Atlanta, Georgia | Tallahassee, Florida | 62.7 | graphhopper | 2895 | Avg High: 72.8°F, Low: 58.3°F (open-meteo) |  |
| 21 | 2027-02-21 | Atlanta, Georgia | Tallahassee, Florida | 62.7 | graphhopper | 2895 | Avg High: 70.6°F, Low: 66.3°F (open-meteo) |  |
| 22 | 2027-02-22 | Atlanta, Georgia | Tallahassee, Florida | 62.7 | graphhopper | 2895 | Avg High: 70.6°F, Low: 62.1°F (open-meteo) |  |
| 23 | 2027-02-23 | Atlanta, Georgia | Tallahassee, Florida | 62.7 | graphhopper | 2895 | Avg High: 69.4°F, Low: 57.0°F (open-meteo) |  |
| 24 | 2027-02-24 | Tallahassee, Florida | Jackson, Mississippi | 68.0 | graphhopper | 3276 | Avg High: 70.2°F, Low: 42.3°F (open-meteo) |  |
| 25 | 2027-02-25 | Tallahassee, Florida | Jackson, Mississippi | 68.0 | graphhopper | 3276 | Avg High: 64.2°F, Low: 47.3°F (open-meteo) |  |
| 26 | 2027-02-26 | Tallahassee, Florida | Jackson, Mississippi | 68.0 | graphhopper | 3276 | Avg High: 73.9°F, Low: 47.1°F (open-meteo) |  |
| 27 | 2027-02-27 | Tallahassee, Florida | Jackson, Mississippi | 68.0 | graphhopper | 3276 | Avg High: 69.4°F, Low: 48.6°F (open-meteo) |  |
| 28 | 2027-02-28 | Tallahassee, Florida | Jackson, Mississippi | 68.0 | graphhopper | 3276 | Avg High: 56.6°F, Low: 36.5°F (open-meteo) |  |
| 29 | 2027-03-01 | Tallahassee, Florida | Jackson, Mississippi | 68.0 | graphhopper | 3276 | Avg High: 56.8°F, Low: 32.6°F (open-meteo) |  |
| 30 | 2027-03-02 | Tallahassee, Florida | Jackson, Mississippi | 68.0 | graphhopper | 3276 | Avg High: 65.5°F, Low: 48.3°F (open-meteo) |  |
| 31 | 2027-03-03 | Jackson, Mississippi | Little Rock, Arkansas | 66.8 | graphhopper | 1552 | Avg High: 61.7°F, Low: 37.5°F (open-meteo) |  |
| 32 | 2027-03-04 | Jackson, Mississippi | Little Rock, Arkansas | 66.8 | graphhopper | 1552 | Avg High: 60.3°F, Low: 40.3°F (open-meteo) |  |
| 33 | 2027-03-05 | Jackson, Mississippi | Little Rock, Arkansas | 66.8 | graphhopper | 1552 | Avg High: 71.1°F, Low: 59.7°F (open-meteo) |  |
| 34 | 2027-03-06 | Jackson, Mississippi | Little Rock, Arkansas | 66.8 | graphhopper | 1552 | Avg High: 66.6°F, Low: 31.5°F (open-meteo) |  |
| 35 | 2027-03-07 | Jackson, Mississippi | Little Rock, Arkansas | 66.8 | graphhopper | 1552 | Avg High: 48.0°F, Low: 30.7°F (open-meteo) |  |
| 36 | 2027-03-08 | Little Rock, Arkansas | Columbia, South Carolina | 68.9 | graphhopper | 4009 | Avg High: 53.7°F, Low: 33.3°F (open-meteo) |  |
| 37 | 2027-03-09 | Little Rock, Arkansas | Columbia, South Carolina | 68.9 | graphhopper | 4009 | Avg High: 64.0°F, Low: 39.1°F (open-meteo) |  |
| 38 | 2027-03-10 | Little Rock, Arkansas | Columbia, South Carolina | 68.9 | graphhopper | 4009 | Avg High: 76.0°F, Low: 55.6°F (open-meteo) |  |
| 39 | 2027-03-11 | Little Rock, Arkansas | Columbia, South Carolina | 68.9 | graphhopper | 4009 | Avg High: 66.7°F, Low: 41.5°F (open-meteo) |  |
| 40 | 2027-03-12 | Little Rock, Arkansas | Columbia, South Carolina | 68.9 | graphhopper | 4009 | Avg High: 53.0°F, Low: 34.0°F (open-meteo) |  |
| 41 | 2027-03-13 | Little Rock, Arkansas | Columbia, South Carolina | 68.9 | graphhopper | 4009 | Avg High: 61.9°F, Low: 29.4°F (open-meteo) |  |
| 42 | 2027-03-14 | Little Rock, Arkansas | Columbia, South Carolina | 68.9 | graphhopper | 4009 | Avg High: 67.5°F, Low: 38.8°F (open-meteo) |  |
| 43 | 2027-03-15 | Little Rock, Arkansas | Columbia, South Carolina | 68.9 | graphhopper | 4009 | Avg High: 67.9°F, Low: 54.5°F (open-meteo) |  |
| 44 | 2027-03-16 | Little Rock, Arkansas | Columbia, South Carolina | 68.9 | graphhopper | 4009 | Avg High: 66.3°F, Low: 60.1°F (open-meteo) |  |
| 45 | 2027-03-17 | Little Rock, Arkansas | Columbia, South Carolina | 68.9 | graphhopper | 4009 | Avg High: 58.5°F, Low: 37.6°F (open-meteo) |  |
| 46 | 2027-03-18 | Little Rock, Arkansas | Columbia, South Carolina | 68.9 | graphhopper | 4009 | Avg High: 68.2°F, Low: 47.4°F (open-meteo) |  |
| 47 | 2027-03-19 | Little Rock, Arkansas | Columbia, South Carolina | 68.9 | graphhopper | 4009 | Avg High: 55.7°F, Low: 36.3°F (open-meteo) |  |
| 48 | 2027-03-20 | Columbia, South Carolina | Raleigh, North Carolina | 57.8 | graphhopper | 2586 | Avg High: 47.7°F, Low: 38.2°F (open-meteo) |  |
| 49 | 2027-03-21 | Columbia, South Carolina | Raleigh, North Carolina | 57.8 | graphhopper | 2586 | Avg High: 53.1°F, Low: 28.3°F (open-meteo) |  |
| 50 | 2027-03-22 | Columbia, South Carolina | Raleigh, North Carolina | 57.8 | graphhopper | 2586 | Avg High: 67.6°F, Low: 42.1°F (open-meteo) |  |
| 51 | 2027-03-23 | Columbia, South Carolina | Raleigh, North Carolina | 57.8 | graphhopper | 2586 | Avg High: 71.8°F, Low: 42.2°F (open-meteo) |  |
| 52 | 2027-03-24 | Raleigh, North Carolina | Richmond, Virginia | 65.2 | graphhopper | 3602 | Avg High: 62.5°F, Low: 56.2°F (open-meteo) |  |
| 53 | 2027-03-25 | Raleigh, North Carolina | Richmond, Virginia | 65.2 | graphhopper | 3602 | Avg High: 55.0°F, Low: 36.5°F (open-meteo) |  |
| 54 | 2027-03-26 | Raleigh, North Carolina | Richmond, Virginia | 65.2 | graphhopper | 3602 | Avg High: 66.7°F, Low: 35.0°F (open-meteo) |  |
| 55 | 2027-03-27 | Richmond, Virginia | Charleston, West Virginia | 42.2 | graphhopper | 4494 | Avg High: 64.0°F, Low: 38.0°F (open-meteo) |  |
| 56 | 2027-03-28 | Richmond, Virginia | Charleston, West Virginia | 42.2 | graphhopper | 4494 | Avg High: 54.2°F, Low: 37.9°F (open-meteo) |  |
| 57 | 2027-03-29 | Richmond, Virginia | Charleston, West Virginia | 42.2 | graphhopper | 4494 | Avg High: 51.7°F, Low: 26.2°F (open-meteo) |  |
| 58 | 2027-03-30 | Richmond, Virginia | Charleston, West Virginia | 42.2 | graphhopper | 4494 | Avg High: 67.0°F, Low: 47.1°F (open-meteo) |  |
| 59 | 2027-03-31 | Richmond, Virginia | Charleston, West Virginia | 42.2 | graphhopper | 4494 | Avg High: 79.3°F, Low: 58.0°F (open-meteo) |  |
| 60 | 2027-04-01 | Richmond, Virginia | Charleston, West Virginia | 42.2 | graphhopper | 4494 | Avg High: 68.6°F, Low: 59.2°F (open-meteo) |  |
| 61 | 2027-04-02 | Richmond, Virginia | Charleston, West Virginia | 42.2 | graphhopper | 4494 | Avg High: 61.0°F, Low: 38.0°F (open-meteo) |  |
| 62 | 2027-04-03 | Richmond, Virginia | Charleston, West Virginia | 42.2 | graphhopper | 4494 | Avg High: 65.1°F, Low: 43.6°F (open-meteo) |  |
| 63 | 2027-04-04 | Richmond, Virginia | Charleston, West Virginia | 42.2 | graphhopper | 4494 | Avg High: 59.0°F, Low: 47.2°F (open-meteo) |  |
| 64 | 2027-04-05 | Charleston, West Virginia | Frankfort, Kentucky | 63.9 | graphhopper | 4850 | Avg High: 58.7°F, Low: 33.7°F (open-meteo) |  |
| 65 | 2027-04-06 | Charleston, West Virginia | Frankfort, Kentucky | 63.9 | graphhopper | 4850 | Avg High: 73.9°F, Low: 46.3°F (open-meteo) |  |
| 66 | 2027-04-07 | Charleston, West Virginia | Frankfort, Kentucky | 63.9 | graphhopper | 4850 | Avg High: 72.4°F, Low: 38.9°F (open-meteo) |  |
| 67 | 2027-04-08 | Charleston, West Virginia | Frankfort, Kentucky | 63.9 | graphhopper | 4850 | Avg High: 64.3°F, Low: 44.1°F (open-meteo) |  |
| 68 | 2027-04-09 | Frankfort, Kentucky | Nashville, Tennessee | 57.0 | graphhopper | 3529 | Avg High: 67.0°F, Low: 38.4°F (open-meteo) |  |
| 69 | 2027-04-10 | Frankfort, Kentucky | Nashville, Tennessee | 57.0 | graphhopper | 3529 | Avg High: 77.7°F, Low: 44.8°F (open-meteo) |  |
| 70 | 2027-04-11 | Frankfort, Kentucky | Nashville, Tennessee | 57.0 | graphhopper | 3529 | Avg High: 85.1°F, Low: 52.4°F (open-meteo) |  |
| 71 | 2027-04-12 | Frankfort, Kentucky | Nashville, Tennessee | 57.0 | graphhopper | 3529 | Avg High: 80.8°F, Low: 58.3°F (open-meteo) |  |
| 72 | 2027-04-13 | Nashville, Tennessee | Jefferson City, Missouri | 65.9 | graphhopper | 4236 | Avg High: 84.0°F, Low: 46.5°F (open-meteo) |  |
| 73 | 2027-04-14 | Nashville, Tennessee | Jefferson City, Missouri | 65.9 | graphhopper | 4236 | Avg High: 63.5°F, Low: 51.4°F (open-meteo) |  |
| 74 | 2027-04-15 | Nashville, Tennessee | Jefferson City, Missouri | 65.9 | graphhopper | 4236 | Avg High: 71.5°F, Low: 40.0°F (open-meteo) |  |
| 75 | 2027-04-16 | Nashville, Tennessee | Jefferson City, Missouri | 65.9 | graphhopper | 4236 | Avg High: 69.3°F, Low: 47.0°F (open-meteo) |  |
| 76 | 2027-04-17 | Nashville, Tennessee | Jefferson City, Missouri | 65.9 | graphhopper | 4236 | Avg High: 74.7°F, Low: 54.6°F (open-meteo) |  |
| 77 | 2027-04-18 | Nashville, Tennessee | Jefferson City, Missouri | 65.9 | graphhopper | 4236 | Avg High: 76.8°F, Low: 65.2°F (open-meteo) |  |
| 78 | 2027-04-19 | Nashville, Tennessee | Jefferson City, Missouri | 65.9 | graphhopper | 4236 | Avg High: 75.6°F, Low: 69.7°F (open-meteo) |  |
| 79 | 2027-04-20 | Jefferson City, Missouri | Topeka, Kansas | 58.1 | graphhopper | 3041 | Avg High: 77.8°F, Low: 50.8°F (open-meteo) |  |
| 80 | 2027-04-21 | Jefferson City, Missouri | Topeka, Kansas | 58.1 | graphhopper | 3041 | Avg High: 77.0°F, Low: 55.0°F (open-meteo) |  |
| 81 | 2027-04-22 | Jefferson City, Missouri | Topeka, Kansas | 58.1 | graphhopper | 3041 | Avg High: 79.6°F, Low: 56.8°F (open-meteo) |  |
| 82 | 2027-04-23 | Jefferson City, Missouri | Topeka, Kansas | 58.1 | graphhopper | 3041 | Avg High: 78.6°F, Low: 54.1°F (open-meteo) |  |
| 83 | 2027-04-24 | Topeka, Kansas | Oklahoma City, Oklahoma | 62.4 | graphhopper | 2129 | Avg High: 65.5°F, Low: 51.0°F (open-meteo) |  |
| 84 | 2027-04-25 | Topeka, Kansas | Oklahoma City, Oklahoma | 62.4 | graphhopper | 2129 | Avg High: 70.8°F, Low: 45.7°F (open-meteo) |  |
| 85 | 2027-04-26 | Topeka, Kansas | Oklahoma City, Oklahoma | 62.4 | graphhopper | 2129 | Avg High: 70.0°F, Low: 50.7°F (open-meteo) |  |
| 86 | 2027-04-27 | Topeka, Kansas | Oklahoma City, Oklahoma | 62.4 | graphhopper | 2129 | Avg High: 76.2°F, Low: 51.1°F (open-meteo) |  |
| 87 | 2027-04-28 | Topeka, Kansas | Oklahoma City, Oklahoma | 62.4 | graphhopper | 2129 | Avg High: 77.5°F, Low: 58.7°F (open-meteo) |  |
| 88 | 2027-04-29 | Topeka, Kansas | Oklahoma City, Oklahoma | 62.4 | graphhopper | 2129 | Avg High: 75.8°F, Low: 58.7°F (open-meteo) |  |
| 89 | 2027-04-30 | Oklahoma City, Oklahoma | Harrisburg, Pennsylvania | 67.8 | graphhopper | 3411 | Avg High: 81.8°F, Low: 49.2°F (open-meteo) |  |
| 90 | 2027-05-01 | Oklahoma City, Oklahoma | Harrisburg, Pennsylvania | 67.8 | graphhopper | 3411 | Avg High: 84.2°F, Low: 59.4°F (open-meteo) |  |
| 91 | 2027-05-02 | Oklahoma City, Oklahoma | Harrisburg, Pennsylvania | 67.8 | graphhopper | 3411 | Avg High: 75.1°F, Low: 61.0°F (open-meteo) |  |
| 92 | 2027-05-03 | Oklahoma City, Oklahoma | Harrisburg, Pennsylvania | 67.8 | graphhopper | 3411 | Avg High: 65.0°F, Low: 45.8°F (open-meteo) |  |
| 93 | 2027-05-04 | Oklahoma City, Oklahoma | Harrisburg, Pennsylvania | 67.8 | graphhopper | 3411 | Avg High: 52.0°F, Low: 36.0°F (open-meteo) |  |
| 94 | 2027-05-05 | Oklahoma City, Oklahoma | Harrisburg, Pennsylvania | 67.8 | graphhopper | 3411 | Avg High: 58.0°F, Low: 34.9°F (open-meteo) |  |
| 95 | 2027-05-06 | Oklahoma City, Oklahoma | Harrisburg, Pennsylvania | 67.8 | graphhopper | 3411 | Avg High: 70.0°F, Low: 45.2°F (open-meteo) |  |
| 96 | 2027-05-07 | Oklahoma City, Oklahoma | Harrisburg, Pennsylvania | 67.8 | graphhopper | 3411 | Avg High: 75.6°F, Low: 49.9°F (open-meteo) |  |
| 97 | 2027-05-08 | Oklahoma City, Oklahoma | Harrisburg, Pennsylvania | 67.8 | graphhopper | 3411 | Avg High: 80.2°F, Low: 56.1°F (open-meteo) |  |
| 98 | 2027-05-09 | Oklahoma City, Oklahoma | Harrisburg, Pennsylvania | 67.8 | graphhopper | 3411 | Avg High: 77.6°F, Low: 54.1°F (open-meteo) |  |
| 99 | 2027-05-10 | Oklahoma City, Oklahoma | Harrisburg, Pennsylvania | 67.8 | graphhopper | 3411 | Avg High: 78.8°F, Low: 52.0°F (open-meteo) |  |
| 100 | 2027-05-11 | Oklahoma City, Oklahoma | Harrisburg, Pennsylvania | 67.8 | graphhopper | 3411 | Avg High: 87.9°F, Low: 56.1°F (open-meteo) |  |
| 101 | 2027-05-12 | Oklahoma City, Oklahoma | Harrisburg, Pennsylvania | 67.8 | graphhopper | 3411 | Avg High: 78.2°F, Low: 64.0°F (open-meteo) |  |
| 102 | 2027-05-13 | Oklahoma City, Oklahoma | Harrisburg, Pennsylvania | 67.8 | graphhopper | 3411 | Avg High: 68.3°F, Low: 50.4°F (open-meteo) |  |
| 103 | 2027-05-14 | Oklahoma City, Oklahoma | Harrisburg, Pennsylvania | 67.8 | graphhopper | 3411 | Avg High: 69.2°F, Low: 47.4°F (open-meteo) |  |
| 104 | 2027-05-15 | Oklahoma City, Oklahoma | Harrisburg, Pennsylvania | 67.8 | graphhopper | 3411 | Avg High: 66.5°F, Low: 45.6°F (open-meteo) |  |
| 105 | 2027-05-16 | Oklahoma City, Oklahoma | Harrisburg, Pennsylvania | 67.8 | graphhopper | 3411 | Avg High: 59.9°F, Low: 52.8°F (open-meteo) |  |
| 106 | 2027-05-17 | Oklahoma City, Oklahoma | Harrisburg, Pennsylvania | 67.8 | graphhopper | 3411 | Avg High: 68.3°F, Low: 45.2°F (open-meteo) |  |
| 107 | 2027-05-18 | Oklahoma City, Oklahoma | Harrisburg, Pennsylvania | 67.8 | graphhopper | 3411 | Avg High: 71.7°F, Low: 51.1°F (open-meteo) |  |
| 108 | 2027-05-19 | Oklahoma City, Oklahoma | Harrisburg, Pennsylvania | 67.8 | graphhopper | 3411 | Avg High: 77.8°F, Low: 59.6°F (open-meteo) |  |
| 109 | 2027-05-20 | Oklahoma City, Oklahoma | Harrisburg, Pennsylvania | 67.8 | graphhopper | 3411 | Avg High: 79.1°F, Low: 64.5°F (open-meteo) |  |
| 110 | 2027-05-21 | Oklahoma City, Oklahoma | Harrisburg, Pennsylvania | 67.8 | graphhopper | 3411 | Avg High: 80.1°F, Low: 60.2°F (open-meteo) |  |
| 111 | 2027-05-22 | Harrisburg, Pennsylvania | Washington, DC | 43.1 | graphhopper | 3376 | Avg High: 76.1°F, Low: 60.2°F (open-meteo) |  |
| 112 | 2027-05-23 | Harrisburg, Pennsylvania | Washington, DC | 43.1 | graphhopper | 3376 | Avg High: 75.5°F, Low: 51.6°F (open-meteo) |  |
| 113 | 2027-05-24 | Harrisburg, Pennsylvania | Washington, DC | 43.1 | graphhopper | 3376 | Avg High: 84.4°F, Low: 57.5°F (open-meteo) |  |

</details>

---

## Data Attribution
Weather data by [Open-Meteo.com](https://open-meteo.com/) under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Data has been transformed into itinerary-level schedule summaries.


