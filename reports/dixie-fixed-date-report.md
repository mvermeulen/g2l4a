# Route Recommendations Comparison

## Overview Comparison
| Option | Start Date | Feasible? | Total Score | Weather Score | Distance Score | Hills Score | Total Distance | Distance Source | Total Climb | Key Difference |
|---|---|---|---|---|---|---|---|---|---|---|
| **Best Recommendation** | 2027-01-16 | Yes | 0.6006 | 0.3604 | 0.5611 | 1.0000 | 2500.9 mi | graphhopper | 116207 ft | Baseline / Optimal Route |
| Alternative 1 | 2027-01-02 | No ❌ | N/A | N/A | N/A | N/A | 2500.9 mi | graphhopper | 116207 ft | Different start date (2027-01-02), same sequence |
| Alternative 2 | 2027-01-02 | No ❌ | N/A | N/A | N/A | N/A | 2590.9 mi | graphhopper | 123593 ft | Different start date (2027-01-02) & alternative sequence |
| Alternative 3 | 2026-12-19 | Yes | 0.5776 | 0.2948 | 0.5611 | 1.0000 | 2500.9 mi | graphhopper | 116207 ft | Different start date (2026-12-19), same sequence |
| Alternative 4 | 2026-12-19 | Yes | 0.5623 | 0.3302 | 0.5227 | 0.9504 | 2590.9 mi | graphhopper | 123593 ft | Different start date (2026-12-19) & alternative sequence |
| Alternative 5 | 2027-01-16 | Yes | 0.5622 | 0.5958 | 0.3498 | 0.8550 | 3167.4 mi | graphhopper | 137806 ft | Alternative via-city sequence, same date |
| Alternative 6 | 2027-01-16 | Yes | 0.5279 | 0.5797 | 0.3304 | 0.7714 | 3259.1 mi | graphhopper | 150248 ft | Alternative via-city sequence, same date |

## Detailed Recommendations
### Best Recommendation
**Feasible**: Yes
- **Start Date**: 2027-01-16
- **Total Distance**: 2500.9 miles (2411.4 mi paved, 89.5 mi gravel)
- **Distance Source**: graphhopper
- **Total Climbing**: 116207 ft
- **Desirability Scores**:
  - Weather Preference: 0.360
  - Distance Score: 0.561
  - Climbing Score: 1.000
  - **Total Desirability Score**: 0.601

<details>
<summary>Click to view daily travel schedule</summary>

| Start Date | End Date | Days | Origin | Destination | Distance (mi/day) | Ascent (ft/day) | Leg Distance (mi) | Leg Ascent (ft) | Distance Source | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2027-01-16 | 2027-01-25 | 10 | Austin, Texas | Baton Rouge, Louisiana | 58.0/day | 1777/day | 580.1 mi (554.8 mi paved, 25.3 mi gravel) | 17769 | graphhopper | Avg High: 44.6-71.2°F, Low: 29.8-46.4°F (meteostatweatherprovider) |  |
| 2027-01-26 | 2027-01-28 | 3 | Baton Rouge, Louisiana | Jackson, Mississippi | 57.6/day | 2527/day | 172.8 mi (172.8 mi paved) | 7581 | graphhopper | Avg High: 44.1-45.9°F, Low: 26.4-28.2°F (meteostatweatherprovider) |  |
| 2027-01-29 | 2027-02-02 | 5 | Jackson, Mississippi | Montgomery, Alabama | 54.1/day | 2443/day | 270.3 mi (253.8 mi paved, 16.5 mi gravel) | 12216 | graphhopper | Avg High: 59.5-63.5°F, Low: 35.6-40.2°F (meteostatweatherprovider) |  |
| 2027-02-03 | 2027-02-06 | 4 | Montgomery, Alabama | Tallahassee, Florida | 55.5/day | 2540/day | 222.0 mi (212.2 mi paved, 9.8 mi gravel) | 10161 | graphhopper | Avg High: 65.7-67.4°F, Low: 42.5-44.3°F (meteostatweatherprovider) |  |
| 2027-02-07 | 2027-02-12 | 6 | Tallahassee, Florida | Atlanta, Georgia | 52.5/day | 2387/day | 315.0 mi (302.6 mi paved, 12.4 mi gravel) | 14321 | graphhopper | Avg High: 55.2-58.7°F, Low: 35.8-39.0°F (meteostatweatherprovider) |  |
| 2027-02-13 | 2027-02-17 | 5 | Atlanta, Georgia | Columbia, South Carolina | 51.3/day | 2974/day | 256.3 mi (249.5 mi paved, 6.8 mi gravel) | 14869 | graphhopper | Avg High: 58.3-60.9°F, Low: 35.9-40.7°F (meteostatweatherprovider) |  |
| 2027-02-18 | 2027-02-21 | 4 | Columbia, South Carolina | Raleigh, North Carolina | 57.8/day | 2586/day | 231.3 mi (231.3 mi paved) | 10345 | graphhopper | Avg High: 53.9-60.5°F, Low: 30.5-36.0°F (meteostatweatherprovider) |  |
| 2027-02-22 | 2027-02-25 | 4 | Raleigh, North Carolina | Richmond, Virginia | 48.9/day | 2701/day | 195.7 mi (195.7 mi paved) | 10806 | graphhopper | Avg High: 53.8-56.6°F, Low: 33.4-34.7°F (meteostatweatherprovider) |  |
| 2027-02-26 | 2027-02-28 | 3 | Richmond, Virginia | Washington, DC | 42.2/day | 2528/day | 126.5 mi (122.2 mi paved, 4.3 mi gravel) | 7584 | graphhopper | Avg High: 48.7-50.8°F, Low: 33.3-35.1°F (meteostatweatherprovider) |  |
| 2027-03-01 | 2027-03-03 | 3 | Washington, DC | Washington, DC | 0.0/day | 0/day | 0.0 | 0 | graphhopper | Avg High: 50.4-53.2°F, Low: 33.5-36.0°F (meteostatweatherprovider) | Rest Day at Washington, DC |
| 2027-03-04 | 2027-03-06 | 3 | Washington, DC | Harrisburg, Pennsylvania | 43.6/day | 3519/day | 130.7 mi (118.7 mi paved, 12.0 mi gravel) | 10556 | graphhopper | Avg High: 44.8-48.4°F, Low: 27.9-28.3°F (meteostatweatherprovider) |  |

</details>

---

### Alternative 1
**Feasible**: No ❌
- **Start Date**: 2027-01-02
- **Total Distance**: 2500.9 miles (2411.4 mi paved, 89.5 mi gravel)
- **Distance Source**: graphhopper
- **Total Climbing**: 116207 ft
- **Violated Constraints**:
  - [INFEASIBLE_WEATHER_MIN_LOW] at Harrisburg, Pennsylvania on 2027-02-19: observed 23.6 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Harrisburg, Pennsylvania.

<details>
<summary>Click to view daily travel schedule</summary>

ROUTE INFEASIBLE


</details>

---

### Alternative 2
**Feasible**: No ❌
- **Start Date**: 2027-01-02
- **Total Distance**: 2590.9 miles (2513.5 mi paved, 77.5 mi gravel)
- **Distance Source**: graphhopper
- **Total Climbing**: 123593 ft
- **Violated Constraints**:
  - [INFEASIBLE_WEATHER_MIN_LOW] at Harrisburg, Pennsylvania on 2027-02-19: observed 23.6 vs threshold 24. Hint: Consider traveling during a warmer season or modifying the route to bypass Harrisburg, Pennsylvania.

<details>
<summary>Click to view daily travel schedule</summary>

ROUTE INFEASIBLE


</details>

---

### Alternative 3
**Feasible**: Yes
- **Start Date**: 2026-12-19
- **Total Distance**: 2500.9 miles (2411.4 mi paved, 89.5 mi gravel)
- **Distance Source**: graphhopper
- **Total Climbing**: 116207 ft
- **Desirability Scores**:
  - Weather Preference: 0.295
  - Distance Score: 0.561
  - Climbing Score: 1.000
  - **Total Desirability Score**: 0.578

<details>
<summary>Click to view daily travel schedule</summary>

| Start Date | End Date | Days | Origin | Destination | Distance (mi/day) | Ascent (ft/day) | Leg Distance (mi) | Leg Ascent (ft) | Distance Source | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-12-19 | 2026-12-28 | 10 | Austin, Texas | Baton Rouge, Louisiana | 58.0/day | 1777/day | 580.1 mi (554.8 mi paved, 25.3 mi gravel) | 17769 | graphhopper | Avg High: 59.4-72.7°F, Low: 40.6-55.0°F (meteostatweatherprovider) |  |
| 2026-12-29 | 2026-12-31 | 3 | Baton Rouge, Louisiana | Jackson, Mississippi | 57.6/day | 2527/day | 172.8 mi (172.8 mi paved) | 7581 | graphhopper | Avg High: 48.9-49.9°F, Low: 33.8-34.4°F (meteostatweatherprovider) |  |
| 2027-01-01 | 2027-01-05 | 5 | Jackson, Mississippi | Montgomery, Alabama | 54.1/day | 2443/day | 270.3 mi (253.8 mi paved, 16.5 mi gravel) | 12216 | graphhopper | Avg High: 52.0-59.6°F, Low: 32.9-43.8°F (meteostatweatherprovider) |  |
| 2027-01-06 | 2027-01-09 | 4 | Montgomery, Alabama | Tallahassee, Florida | 55.5/day | 2540/day | 222.0 mi (212.2 mi paved, 9.8 mi gravel) | 10161 | graphhopper | Avg High: 61.6-65.9°F, Low: 36.2-40.7°F (meteostatweatherprovider) |  |
| 2027-01-10 | 2027-01-15 | 6 | Tallahassee, Florida | Atlanta, Georgia | 52.5/day | 2387/day | 315.0 mi (302.6 mi paved, 12.4 mi gravel) | 14321 | graphhopper | Avg High: 53.1-55.6°F, Low: 33.1-37.9°F (meteostatweatherprovider) |  |
| 2027-01-16 | 2027-01-20 | 5 | Atlanta, Georgia | Columbia, South Carolina | 51.3/day | 2974/day | 256.3 mi (249.5 mi paved, 6.8 mi gravel) | 14869 | graphhopper | Avg High: 54.9-59.2°F, Low: 35.2-37.8°F (meteostatweatherprovider) |  |
| 2027-01-21 | 2027-01-24 | 4 | Columbia, South Carolina | Raleigh, North Carolina | 57.8/day | 2586/day | 231.3 mi (231.3 mi paved) | 10345 | graphhopper | Avg High: 44.9-52.8°F, Low: 27.5-30.6°F (meteostatweatherprovider) |  |
| 2027-01-25 | 2027-01-28 | 4 | Raleigh, North Carolina | Richmond, Virginia | 48.9/day | 2701/day | 195.7 mi (195.7 mi paved) | 10806 | graphhopper | Avg High: 47.8-49.6°F, Low: 28.3-29.0°F (meteostatweatherprovider) |  |
| 2027-01-29 | 2027-01-31 | 3 | Richmond, Virginia | Washington, DC | 42.2/day | 2528/day | 126.5 mi (122.2 mi paved, 4.3 mi gravel) | 7584 | graphhopper | Avg High: 44.1-44.7°F, Low: 29.3-30.3°F (meteostatweatherprovider) |  |
| 2027-02-01 | 2027-02-03 | 3 | Washington, DC | Washington, DC | 0.0/day | 0/day | 0.0 | 0 | graphhopper | Avg High: 46.1-47.5°F, Low: 30.8-31.2°F (meteostatweatherprovider) | Rest Day at Washington, DC |
| 2027-02-04 | 2027-02-06 | 3 | Washington, DC | Harrisburg, Pennsylvania | 43.6/day | 3519/day | 130.7 mi (118.7 mi paved, 12.0 mi gravel) | 10556 | graphhopper | Avg High: 40.2-41.9°F, Low: 25.0-26.1°F (meteostatweatherprovider) |  |

</details>

---

### Alternative 4
**Feasible**: Yes
- **Start Date**: 2026-12-19
- **Total Distance**: 2590.9 miles (2513.5 mi paved, 77.5 mi gravel)
- **Distance Source**: graphhopper
- **Total Climbing**: 123593 ft
- **Desirability Scores**:
  - Weather Preference: 0.330
  - Distance Score: 0.523
  - Climbing Score: 0.950
  - **Total Desirability Score**: 0.562

<details>
<summary>Click to view daily travel schedule</summary>

| Start Date | End Date | Days | Origin | Destination | Distance (mi/day) | Ascent (ft/day) | Leg Distance (mi) | Leg Ascent (ft) | Distance Source | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-12-19 | 2026-12-28 | 10 | Austin, Texas | Baton Rouge, Louisiana | 58.0/day | 1777/day | 580.1 mi (554.8 mi paved, 25.3 mi gravel) | 17769 | graphhopper | Avg High: 59.4-72.7°F, Low: 40.6-55.0°F (meteostatweatherprovider) |  |
| 2026-12-29 | 2026-12-31 | 3 | Baton Rouge, Louisiana | Jackson, Mississippi | 57.6/day | 2527/day | 172.8 mi (172.8 mi paved) | 7581 | graphhopper | Avg High: 48.9-49.9°F, Low: 33.8-34.4°F (meteostatweatherprovider) |  |
| 2027-01-01 | 2027-01-08 | 8 | Jackson, Mississippi | Tallahassee, Florida | 59.5/day | 2854/day | 476.3 mi (459.1 mi paved, 17.2 mi gravel) | 22832 | graphhopper | Avg High: 61.5-66.0°F, Low: 36.2-46.3°F (meteostatweatherprovider) |  |
| 2027-01-09 | 2027-01-12 | 4 | Tallahassee, Florida | Montgomery, Alabama | 55.5/day | 2539/day | 221.9 mi (208.0 mi paved, 13.8 mi gravel) | 10156 | graphhopper | Avg High: 53.8-60.2°F, Low: 37.2-40.6°F (meteostatweatherprovider) |  |
| 2027-01-13 | 2027-01-16 | 4 | Montgomery, Alabama | Atlanta, Georgia | 49.8/day | 2774/day | 199.3 mi (199.3 mi paved) | 11095 | graphhopper | Avg High: 53.3-53.8°F, Low: 33.0-35.1°F (meteostatweatherprovider) |  |
| 2027-01-17 | 2027-01-21 | 5 | Atlanta, Georgia | Columbia, South Carolina | 51.3/day | 2974/day | 256.3 mi (249.5 mi paved, 6.8 mi gravel) | 14869 | graphhopper | Avg High: 52.2-59.2°F, Low: 34.6-37.8°F (meteostatweatherprovider) |  |
| 2027-01-22 | 2027-01-25 | 4 | Columbia, South Carolina | Raleigh, North Carolina | 57.8/day | 2586/day | 231.3 mi (231.3 mi paved) | 10345 | graphhopper | Avg High: 44.9-52.8°F, Low: 27.5-30.7°F (meteostatweatherprovider) |  |
| 2027-01-26 | 2027-01-29 | 4 | Raleigh, North Carolina | Richmond, Virginia | 48.9/day | 2701/day | 195.7 mi (195.7 mi paved) | 10806 | graphhopper | Avg High: 48.9-49.6°F, Low: 28.3-29.0°F (meteostatweatherprovider) |  |
| 2027-01-30 | 2027-02-01 | 3 | Richmond, Virginia | Washington, DC | 42.2/day | 2528/day | 126.5 mi (122.2 mi paved, 4.3 mi gravel) | 7584 | graphhopper | Avg High: 44.1-47.1°F, Low: 29.3-30.9°F (meteostatweatherprovider) |  |
| 2027-02-02 | 2027-02-04 | 3 | Washington, DC | Washington, DC | 0.0/day | 0/day | 0.0 | 0 | graphhopper | Avg High: 46.1-48.0°F, Low: 30.8-32.1°F (meteostatweatherprovider) | Rest Day at Washington, DC |
| 2027-02-05 | 2027-02-07 | 3 | Washington, DC | Harrisburg, Pennsylvania | 43.6/day | 3519/day | 130.7 mi (118.7 mi paved, 12.0 mi gravel) | 10556 | graphhopper | Avg High: 40.2-43.7°F, Low: 25.0-26.1°F (meteostatweatherprovider) |  |

</details>

---

### Alternative 5
**Feasible**: Yes
- **Start Date**: 2027-01-16
- **Total Distance**: 3167.4 miles (3111.0 mi paved, 56.3 mi gravel)
- **Distance Source**: graphhopper
- **Total Climbing**: 137806 ft
- **Desirability Scores**:
  - Weather Preference: 0.596
  - Distance Score: 0.350
  - Climbing Score: 0.855
  - **Total Desirability Score**: 0.562

<details>
<summary>Click to view daily travel schedule</summary>

| Start Date | End Date | Days | Origin | Destination | Distance (mi/day) | Ascent (ft/day) | Leg Distance (mi) | Leg Ascent (ft) | Distance Source | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2027-01-16 | 2027-02-02 | 18 | Austin, Texas | Tallahassee, Florida | 58.9/day | 1932/day | 1060.5 mi (1047.6 mi paved, 12.9 mi gravel) | 34772 | graphhopper | Avg High: 63.0-66.9°F, Low: 36.0-43.4°F (meteostatweatherprovider) |  |
| 2027-02-03 | 2027-02-11 | 9 | Tallahassee, Florida | Baton Rouge, Louisiana | 58.2/day | 1998/day | 523.9 mi (523.9 mi paved) | 17982 | graphhopper | Avg High: 61.2-75.2°F, Low: 44.7-54.6°F (meteostatweatherprovider) |  |
| 2027-02-12 | 2027-02-14 | 3 | Baton Rouge, Louisiana | Jackson, Mississippi | 57.6/day | 2527/day | 172.8 mi (172.8 mi paved) | 7581 | graphhopper | Avg High: 44.6-47.4°F, Low: 27.1-29.2°F (meteostatweatherprovider) |  |
| 2027-02-15 | 2027-02-19 | 5 | Jackson, Mississippi | Montgomery, Alabama | 54.1/day | 2443/day | 270.3 mi (253.8 mi paved, 16.5 mi gravel) | 12216 | graphhopper | Avg High: 61.8-64.6°F, Low: 38.9-43.0°F (meteostatweatherprovider) |  |
| 2027-02-20 | 2027-02-23 | 4 | Montgomery, Alabama | Atlanta, Georgia | 49.8/day | 2774/day | 199.3 mi (199.3 mi paved) | 11095 | graphhopper | Avg High: 57.9-62.3°F, Low: 35.0-45.4°F (meteostatweatherprovider) |  |
| 2027-02-24 | 2027-02-28 | 5 | Atlanta, Georgia | Columbia, South Carolina | 51.3/day | 2974/day | 256.3 mi (249.5 mi paved, 6.8 mi gravel) | 14869 | graphhopper | Avg High: 62.0-66.6°F, Low: 41.5-44.6°F (meteostatweatherprovider) |  |
| 2027-03-01 | 2027-03-04 | 4 | Columbia, South Carolina | Raleigh, North Carolina | 57.8/day | 2586/day | 231.3 mi (231.3 mi paved) | 10345 | graphhopper | Avg High: 58.6-61.1°F, Low: 35.1-38.9°F (meteostatweatherprovider) |  |
| 2027-03-05 | 2027-03-08 | 4 | Raleigh, North Carolina | Richmond, Virginia | 48.9/day | 2701/day | 195.7 mi (195.7 mi paved) | 10806 | graphhopper | Avg High: 54.8-61.2°F, Low: 32.9-36.0°F (meteostatweatherprovider) |  |
| 2027-03-09 | 2027-03-11 | 3 | Richmond, Virginia | Washington, DC | 42.2/day | 2528/day | 126.5 mi (122.2 mi paved, 4.3 mi gravel) | 7584 | graphhopper | Avg High: 57.5-59.9°F, Low: 37.8-40.0°F (meteostatweatherprovider) |  |
| 2027-03-12 | 2027-03-14 | 3 | Washington, DC | Washington, DC | 0.0/day | 0/day | 0.0 | 0 | graphhopper | Avg High: 57.7-58.3°F, Low: 39.2-40.3°F (meteostatweatherprovider) | Rest Day at Washington, DC |
| 2027-03-15 | 2027-03-17 | 3 | Washington, DC | Harrisburg, Pennsylvania | 43.6/day | 3519/day | 130.7 mi (118.7 mi paved, 12.0 mi gravel) | 10556 | graphhopper | Avg High: 52.3-54.6°F, Low: 34.8-35.8°F (meteostatweatherprovider) |  |

</details>

---

### Alternative 6
**Feasible**: Yes
- **Start Date**: 2027-01-16
- **Total Distance**: 3259.1 miles (3198.0 mi paved, 61.1 mi gravel)
- **Distance Source**: graphhopper
- **Total Climbing**: 150248 ft
- **Desirability Scores**:
  - Weather Preference: 0.580
  - Distance Score: 0.330
  - Climbing Score: 0.771
  - **Total Desirability Score**: 0.528

<details>
<summary>Click to view daily travel schedule</summary>

| Start Date | End Date | Days | Origin | Destination | Distance (mi/day) | Ascent (ft/day) | Leg Distance (mi) | Leg Ascent (ft) | Distance Source | Weather Context | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2027-01-16 | 2027-02-02 | 18 | Austin, Texas | Tallahassee, Florida | 58.9/day | 1932/day | 1060.5 mi (1047.6 mi paved, 12.9 mi gravel) | 34772 | graphhopper | Avg High: 63.0-66.9°F, Low: 36.0-43.4°F (meteostatweatherprovider) |  |
| 2027-02-03 | 2027-02-06 | 4 | Tallahassee, Florida | Montgomery, Alabama | 55.5/day | 2539/day | 221.9 mi (208.0 mi paved, 13.8 mi gravel) | 10156 | graphhopper | Avg High: 59.6-64.2°F, Low: 39.5-43.2°F (meteostatweatherprovider) |  |
| 2027-02-07 | 2027-02-13 | 7 | Montgomery, Alabama | Baton Rouge, Louisiana | 58.3/day | 2505/day | 408.1 mi (404.5 mi paved, 3.5 mi gravel) | 17534 | graphhopper | Avg High: 62.0-75.2°F, Low: 41.0-54.6°F (meteostatweatherprovider) |  |
| 2027-02-14 | 2027-02-16 | 3 | Baton Rouge, Louisiana | Jackson, Mississippi | 57.6/day | 2527/day | 172.8 mi (172.8 mi paved) | 7581 | graphhopper | Avg High: 47.2-50.1°F, Low: 29.2-31.4°F (meteostatweatherprovider) |  |
| 2027-02-17 | 2027-02-24 | 8 | Jackson, Mississippi | Atlanta, Georgia | 56.9/day | 3256/day | 455.4 mi (455.4 mi paved) | 26045 | graphhopper | Avg High: 56.9-64.2°F, Low: 35.0-45.4°F (meteostatweatherprovider) |  |
| 2027-02-25 | 2027-03-01 | 5 | Atlanta, Georgia | Columbia, South Carolina | 51.3/day | 2974/day | 256.3 mi (249.5 mi paved, 6.8 mi gravel) | 14869 | graphhopper | Avg High: 62.0-66.6°F, Low: 41.5-46.0°F (meteostatweatherprovider) |  |
| 2027-03-02 | 2027-03-05 | 4 | Columbia, South Carolina | Raleigh, North Carolina | 57.8/day | 2586/day | 231.3 mi (231.3 mi paved) | 10345 | graphhopper | Avg High: 58.6-61.1°F, Low: 35.1-38.9°F (meteostatweatherprovider) |  |
| 2027-03-06 | 2027-03-09 | 4 | Raleigh, North Carolina | Richmond, Virginia | 48.9/day | 2701/day | 195.7 mi (195.7 mi paved) | 10806 | graphhopper | Avg High: 54.8-61.8°F, Low: 33.4-37.0°F (meteostatweatherprovider) |  |
| 2027-03-10 | 2027-03-12 | 3 | Richmond, Virginia | Washington, DC | 42.2/day | 2528/day | 126.5 mi (122.2 mi paved, 4.3 mi gravel) | 7584 | graphhopper | Avg High: 57.5-59.9°F, Low: 38.9-40.0°F (meteostatweatherprovider) |  |
| 2027-03-13 | 2027-03-15 | 3 | Washington, DC | Washington, DC | 0.0/day | 0/day | 0.0 | 0 | graphhopper | Avg High: 57.7-59.6°F, Low: 39.9-41.6°F (meteostatweatherprovider) | Rest Day at Washington, DC |
| 2027-03-16 | 2027-03-18 | 3 | Washington, DC | Harrisburg, Pennsylvania | 43.6/day | 3519/day | 130.7 mi (118.7 mi paved, 12.0 mi gravel) | 10556 | graphhopper | Avg High: 52.3-54.2°F, Low: 34.7-35.2°F (meteostatweatherprovider) |  |

</details>

---

## Data Attribution
- Weather data provided by [Meteostat](https://meteostat.net/) under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Data has been transformed into itinerary-level schedule summaries.
- Routing and elevation data powered by [GraphHopper](https://www.graphhopper.com/) using [OpenStreetMap](https://www.openstreetmap.org/copyright) data licensed under [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/).


