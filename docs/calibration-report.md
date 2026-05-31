# Gone2Look4America Calibration & Quality Report

This report documents the calibration of the `g2l4a` multi-objective route optimizer against the cyclist's actual real-world journey.

## Route Comparison Overview
| Route Metric | Cyclist Actual Path | Solver Optimized Path | Difference |
| :--- | :---: | :---: | :---: |
| **Total Distance (mi)** | 5115.2 | 8728.3 | +3613.1 |
| **Total Ascent (ft)** | 30,680 | 28,680 | -2,000 |
| **Weather Comfort Score** | 0.4504 | 0.7278 | +0.2774 |
| **Distance Detour Score** | 1.0000 | 0.9969 | -0.0031 |
| **Hill Climb Score** | 0.7640 | 0.7794 | +0.0154 |
| **Total Desirability Score** | **0.6937** | **0.8214** | **+0.1277** |
| **Feasibility Status** | Infeasible ❌ | Feasible ✅ | - |

## Weight Sensitivity Analysis
Each weight perturbed by +/- 0.10 and normalized to sum to 1.0.

| Weight Shift / Label | Weights (W_w / W_d / W_h) | Cyclist Actual Score | Solver Optimized Score | Improvement |
| :--- | :---: | :---: | :---: | :---: |
| Baseline | 0.45 / 0.30 / 0.25 | 0.6937 | 0.8214 | +0.1277 |
| Shift weather by -0.10 | 0.39 / 0.33 / 0.28 | 0.7207 | 0.8318 | +0.1111 |
| Shift weather by +0.10 | 0.50 / 0.27 / 0.23 | 0.6715 | 0.8129 | +0.1414 |
| Shift distance by -0.10 | 0.50 / 0.22 / 0.28 | 0.6596 | 0.8019 | +0.1423 |
| Shift distance by +0.10 | 0.41 / 0.36 / 0.23 | 0.7215 | 0.8374 | +0.1159 |
| Shift hills by -0.10 | 0.50 / 0.33 / 0.17 | 0.6859 | 0.8261 | +0.1402 |
| Shift hills by +0.10 | 0.41 / 0.27 / 0.32 | 0.7001 | 0.8176 | +0.1175 |

## Solver Execution Performance
- **Execution Duration**: 4752.9 ms
- **Evaluated Candidates**: 5 recommendations returned

## Sequence Ordered Visits Comparison

### Cyclist Actual Via Cities Order:
Annapolis, Maryland, Dover, Delaware, Trenton, New Jersey, Hartford, Connecticut, Providence, Rhode Island, Boston, Massachusetts, Concord, New Hampshire, Augusta, Maine, Montpelier, Vermont, Albany, New York, Columbus, Ohio, Indianapolis, Indiana, Springfield, Illinois, Lansing, Michigan, Madison, Wisconsin, St. Paul, Minnesota, Des Moines, Iowa, Lincoln, Nebraska, Pierre, South Dakota, Bismarck, North Dakota, Cheyenne, Wyoming, Denver, Colorado, Salt Lake City, Utah, Boise, Idaho, Salem, Oregon

### Solver Recommended Via Cities Order:
Annapolis, Maryland, Dover, Delaware, Trenton, New Jersey, Hartford, Connecticut, Providence, Rhode Island, Boston, Massachusetts, Concord, New Hampshire, Montpelier, Vermont, Albany, New York, Augusta, Maine, Columbus, Ohio, Indianapolis, Indiana, Springfield, Illinois, Madison, Wisconsin, St. Paul, Minnesota, Des Moines, Iowa, Lincoln, Nebraska, Pierre, South Dakota, Bismarck, North Dakota, Cheyenne, Wyoming, Denver, Colorado, Salt Lake City, Utah, Boise, Idaho, Salem, Oregon, Lansing, Michigan
