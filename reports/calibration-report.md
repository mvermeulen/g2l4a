# Gone2Look4America Calibration & Quality Report

This report documents the calibration of the `g2l4a` multi-objective route optimizer against the cyclist's actual real-world journey.

## Route Comparison Overview
| Route Metric | Cyclist Actual Path | Solver Optimized Path | Difference |
| :--- | :---: | :---: | :---: |
| **Total Distance (mi)** | 5115.2 | 5085.7 | -29.5 |
| **Total Ascent (ft)** | 30,680 | 24,680 | -6,000 |
| **Weather Comfort Score** | 0.6709 | 0.6789 | +0.0080 |
| **Distance Detour Score** | 0.9908 | 1.0000 | +0.0092 |
| **Hill Climb Score** | 0.7640 | 0.8102 | +0.0462 |
| **Total Desirability Score** | **0.7901** | **0.8081** | **+0.0180** |
| **Feasibility Status** | Feasible ✅ | Feasible ✅ | - |

## Weight Sensitivity Analysis
Each weight perturbed by +/- 0.10 and normalized to sum to 1.0.

| Weight Shift / Label | Weights (W_w / W_d / W_h) | Cyclist Actual Score | Solver Optimized Score | Improvement |
| :--- | :---: | :---: | :---: | :---: |
| Baseline | 0.45 / 0.30 / 0.25 | 0.7901 | 0.8081 | +0.0180 |
| Shift weather by -0.10 | 0.39 / 0.33 / 0.28 | 0.8034 | 0.8224 | +0.0190 |
| Shift weather by +0.10 | 0.50 / 0.27 / 0.23 | 0.7793 | 0.7963 | +0.0170 |
| Shift distance by -0.10 | 0.50 / 0.22 / 0.28 | 0.7678 | 0.7867 | +0.0189 |
| Shift distance by +0.10 | 0.41 / 0.36 / 0.23 | 0.8084 | 0.8255 | +0.0171 |
| Shift hills by -0.10 | 0.50 / 0.33 / 0.17 | 0.7930 | 0.8078 | +0.0148 |
| Shift hills by +0.10 | 0.41 / 0.27 / 0.32 | 0.7878 | 0.8082 | +0.0204 |

## Solver Execution Performance
- **Execution Duration**: 4323.0 ms
- **Evaluated Candidates**: 5 recommendations returned

## Sequence Ordered Visits Comparison

### Cyclist Actual Via Cities Order:
Annapolis, Maryland, Dover, Delaware, Trenton, New Jersey, Hartford, Connecticut, Providence, Rhode Island, Boston, Massachusetts, Concord, New Hampshire, Augusta, Maine, Montpelier, Vermont, Albany, New York, Columbus, Ohio, Indianapolis, Indiana, Springfield, Illinois, Lansing, Michigan, Madison, Wisconsin, St. Paul, Minnesota, Des Moines, Iowa, Lincoln, Nebraska, Pierre, South Dakota, Bismarck, North Dakota, Cheyenne, Wyoming, Denver, Colorado, Salt Lake City, Utah, Boise, Idaho, Salem, Oregon

### Solver Recommended Via Cities Order:
Annapolis, Maryland, Dover, Delaware, Trenton, New Jersey, Hartford, Connecticut, Providence, Rhode Island, Boston, Massachusetts, Concord, New Hampshire, Augusta, Maine, Montpelier, Vermont, Albany, New York, Lansing, Michigan, Columbus, Ohio, Indianapolis, Indiana, Springfield, Illinois, Madison, Wisconsin, Des Moines, Iowa, Lincoln, Nebraska, St. Paul, Minnesota, Bismarck, North Dakota, Pierre, South Dakota, Cheyenne, Wyoming, Denver, Colorado, Salt Lake City, Utah, Boise, Idaho, Salem, Oregon
