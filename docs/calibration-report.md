# Gone2Look4America Calibration & Quality Report

This report documents the calibration of the `g2l4a` multi-objective route optimizer against the cyclist's actual real-world journey.

## Route Comparison Overview
| Route Metric | Cyclist Actual Path | Solver Optimized Path | Difference |
| :--- | :---: | :---: | :---: |
| **Total Distance (mi)** | 5115.2 | 10751.4 | +5636.2 |
| **Total Ascent (ft)** | 30,680 | 12,680 | -18,000 |
| **Weather Comfort Score** | 0.4504 | 0.7448 | +0.2944 |
| **Distance Detour Score** | 1.0000 | 0.4763 | -0.5237 |
| **Hill Climb Score** | 0.7640 | 0.9025 | +0.1385 |
| **Total Desirability Score** | **0.6937** | **0.7037** | **+0.0100** |
| **Feasibility Status** | Infeasible ❌ | Feasible ✅ | - |

## Weight Sensitivity Analysis
Each weight perturbed by +/- 0.10 and normalized to sum to 1.0.

| Weight Shift / Label | Weights (W_w / W_d / W_h) | Cyclist Actual Score | Solver Optimized Score | Improvement |
| :--- | :---: | :---: | :---: | :---: |
| Baseline | 0.45 / 0.30 / 0.25 | 0.6937 | 0.7037 | +0.0100 |
| Shift weather by -0.10 | 0.39 / 0.33 / 0.28 | 0.7207 | 0.6991 | -0.0216 |
| Shift weather by +0.10 | 0.50 / 0.27 / 0.23 | 0.6715 | 0.7074 | +0.0359 |
| Shift distance by -0.10 | 0.50 / 0.22 / 0.28 | 0.6596 | 0.7290 | +0.0694 |
| Shift distance by +0.10 | 0.41 / 0.36 / 0.23 | 0.7215 | 0.6830 | -0.0385 |
| Shift hills by -0.10 | 0.50 / 0.33 / 0.17 | 0.6859 | 0.6816 | -0.0043 |
| Shift hills by +0.10 | 0.41 / 0.27 / 0.32 | 0.7001 | 0.7218 | +0.0217 |

## Solver Execution Performance
- **Execution Duration**: 3930.6 ms
- **Evaluated Candidates**: 5 recommendations returned

## Sequence Ordered Visits Comparison

### Cyclist Actual Via Cities Order:
Annapolis, Maryland, Dover, Delaware, Trenton, New Jersey, Hartford, Connecticut, Providence, Rhode Island, Boston, Massachusetts, Concord, New Hampshire, Augusta, Maine, Montpelier, Vermont, Albany, New York, Columbus, Ohio, Indianapolis, Indiana, Springfield, Illinois, Lansing, Michigan, Madison, Wisconsin, St. Paul, Minnesota, Des Moines, Iowa, Lincoln, Nebraska, Pierre, South Dakota, Bismarck, North Dakota, Cheyenne, Wyoming, Denver, Colorado, Salt Lake City, Utah, Boise, Idaho, Salem, Oregon

### Solver Recommended Via Cities Order:
Salt Lake City, Utah, Springfield, Illinois, Boston, Massachusetts, Lansing, Michigan, Annapolis, Maryland, Dover, Delaware, Trenton, New Jersey, Hartford, Connecticut, Albany, New York, Providence, Rhode Island, Augusta, Maine, Concord, New Hampshire, Montpelier, Vermont, Columbus, Ohio, Indianapolis, Indiana, St. Paul, Minnesota, Des Moines, Iowa, Madison, Wisconsin, Lincoln, Nebraska, Cheyenne, Wyoming, Denver, Colorado, Bismarck, North Dakota, Pierre, South Dakota, Boise, Idaho, Salem, Oregon
