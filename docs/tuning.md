# Desirability Tuning & Weights Configuration

This guide provides practical instructions for adjusting multi-objective weights and comfort parameters to optimize itinerary desirability for distinct cyclist profiles.

---

## 1. Cyclist Profile Archetypes

By shifting the weights ($w_{\text{weather}}, w_{\text{distance}}, w_{\text{hills}}$), you can calibrate the route optimizer to favor specific cycling preferences:

### A. The Climate Comfort Seeker (Weather-Focused)
*Favors pleasant, mild temperatures over distance or climbing challenges.*
* **Recommended Weights**: `weather: 0.70`, `distance: 0.15`, `hills: 0.15`
* **Result**: The solver will select longer detour paths to routing destinations if they bypass extreme cold or heat waves.

### B. The Speed Tourer (Distance Efficiency-Focused)
*Favors direct, fast paths to minimize excess mileage.*
* **Recommended Weights**: `weather: 0.15`, `distance: 0.70`, `hills: 0.15`
* **Result**: The solver prioritizes the shortest mileage paths, ignoring rolling hills or slight temp swings.

### C. The Flatlander (Ascent Avoidance-Focused)
*Favors flat pathways to minimize vertical climbing burden.*
* **Recommended Weights**: `weather: 0.15`, `distance: 0.15`, `hills: 0.70`
* **Result**: The solver actively selects longer paths or detours that bypass mountainous passes.

---

## 2. Parameter Tuning Guidelines

To adjust parameters, edit the `scoring` block in `config/defaults.yaml` or pass a `scoring` dict override in the user request:

### A. Adjusting Weights
All weights must be non-negative and sum to exactly **`1.0`** (within a `1e-6` precision tolerance threshold):
```yaml
scoring:
  weights:
    weather: 0.50
    distance: 0.30
    hills: 0.20
```

### B. Adjusting Ideal Temperatures
By default, the engine models $70^{\circ}\text{F}$ as perfect riding weather with a $20^{\circ}\text{F}$ comfort decay threshold (so $50^{\circ}\text{F}$ and $90^{\circ}\text{F}$ yield a weather score of $0.0$). If a rider prefers warmer weather, adjust these metrics:
```yaml
scoring:
  comfort:
    ideal_temp_f: 78.0       # Favorites warmer, sunny climates
    temp_tolerance_f: 15.0   # Highly restrictive decay: drops to 0.0 at 63°F or 93°F
```
