# Gone2Look4America Calibration & Quality Report

This report documents the calibration of the `g2l4a` multi-objective route optimizer against the cyclist's actual real-world journey.

## Route Comparison Overview
| Route Metric | Cyclist Actual Path | Solver Optimized Path | Difference |
| :--- | :---: | :---: | :---: |
| **Total Distance (mi)** | 5115.2 | 5085.7 | -29.5 |
| **Total Ascent (ft)** | 30,680 | 24,680 | -6,000 |
| **Weather Comfort Score** | 0.7330 | 0.7782 | +0.0452 |
| **Distance Detour Score** | 0.9908 | 1.0000 | +0.0092 |
| **Hill Climb Score** | 0.7640 | 0.0000 | -0.7640 |
| **Total Desirability Score** | **0.8439** | **0.6724** | **-0.1715** |
| **Feasibility Status** | Feasible ✅ | Feasible ✅ | - |

## Weight Sensitivity Analysis
Each weight perturbed by +/- 0.10 and normalized to sum to 1.0.

| Weight Shift / Label | Weights (W_w / W_d / W_h) | Cyclist Actual Score | Solver Optimized Score | Improvement |
| :--- | :---: | :---: | :---: | :---: |
| Baseline | 0.35 / 0.40 / 0.25 | 0.8439 | 0.6724 | -0.1715 |
| Shift weather by -0.10 | 0.28 / 0.44 / 0.28 | 0.8562 | 0.8856 | +0.0294 |
| Shift weather by +0.10 | 0.41 / 0.36 / 0.23 | 0.8338 | 0.8661 | +0.0323 |
| Shift distance by -0.10 | 0.39 / 0.33 / 0.28 | 0.8275 | 0.8610 | +0.0335 |
| Shift distance by +0.10 | 0.32 / 0.45 / 0.23 | 0.8572 | 0.8863 | +0.0291 |
| Shift hills by -0.10 | 0.39 / 0.44 / 0.17 | 0.8527 | 0.8821 | +0.0294 |
| Shift hills by +0.10 | 0.32 / 0.36 / 0.32 | 0.8366 | 0.8690 | +0.0324 |

## Solver Execution Performance
- **Execution Duration**: 18365.4 ms
- **Evaluated Candidates**: 5 recommendations returned

## Sequence Ordered Visits Comparison

### Cyclist Actual Via Cities Order:
Annapolis, Maryland, Dover, Delaware, Trenton, New Jersey, Hartford, Connecticut, Providence, Rhode Island, Boston, Massachusetts, Concord, New Hampshire, Augusta, Maine, Montpelier, Vermont, Albany, New York, Columbus, Ohio, Indianapolis, Indiana, Springfield, Illinois, Lansing, Michigan, Madison, Wisconsin, St. Paul, Minnesota, Des Moines, Iowa, Lincoln, Nebraska, Pierre, South Dakota, Bismarck, North Dakota, Cheyenne, Wyoming, Denver, Colorado, Salt Lake City, Utah, Boise, Idaho, Salem, Oregon

### Solver Recommended Via Cities Order:
Annapolis, Maryland, Dover, Delaware, Trenton, New Jersey, Hartford, Connecticut, Providence, Rhode Island, Boston, Massachusetts, Concord, New Hampshire, Augusta, Maine, Montpelier, Vermont, Albany, New York, Lansing, Michigan, Columbus, Ohio, Indianapolis, Indiana, Springfield, Illinois, Madison, Wisconsin, Des Moines, Iowa, Lincoln, Nebraska, St. Paul, Minnesota, Bismarck, North Dakota, Pierre, South Dakota, Cheyenne, Wyoming, Denver, Colorado, Salt Lake City, Utah, Boise, Idaho, Salem, Oregon
