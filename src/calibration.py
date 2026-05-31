import sys
import os
import time
from datetime import date, datetime, timedelta
from typing import Dict, Any, List, Optional
import copy

from src.domain import City, Leg, Itinerary, DailySchedule
from src.solver_engine import BeamSearchSolver
from src.validation import RequestParser
from src.config import ConfigManager
from src.cached_providers import CachedRoutingProvider, CachedWeatherProvider
from src.mocks import MockRoutingProvider, MockWeatherProvider, MockElevationProvider
from src.feasibility import FeasibilityEngine
from src.scoring import ScoringEngine
from src.metrics import SolverMetrics
from src.output import OutputFormatter

def build_actual_itinerary(
    itinerary: Itinerary,
    start_date: date,
    routing_prov: CachedRoutingProvider,
    weather_prov: CachedWeatherProvider,
    current_run_date: date,
    feasibility_eng: FeasibilityEngine,
    scoring_eng: ScoringEngine,
    preferences: Dict[str, Any]
) -> Itinerary:
    """Constructs and scores the cyclist's actual chronological route sequence without reordering."""
    sequence = [itinerary.start_city] + list(itinerary.via_cities) + [itinerary.completion_city]
    
    legs: List[Leg] = []
    schedule: List[DailySchedule] = []
    curr_date = start_date
    
    max_miles = feasibility_eng.daily_constraints.get("max_miles_per_day", 80.0) or 80.0
    max_climb = feasibility_eng.daily_constraints.get("max_climb_ft_per_day", 5000.0) or 5000.0
    
    for i in range(len(sequence) - 1):
        c_from = sequence[i]
        c_to = sequence[i + 1]
        
        leg = routing_prov.get_leg_metrics(c_from, c_to, preferences)
        
        import math
        days_needed_miles = math.ceil(leg.distance_miles / max_miles) if max_miles > 0 else 1
        days_needed_climb = math.ceil(leg.ascent_feet / max_climb) if max_climb > 0 else 1
        days_needed = max(1, days_needed_miles, days_needed_climb)
        
        day_dist = leg.distance_miles / days_needed
        day_ascent = leg.ascent_feet / days_needed
        
        for d in range(days_needed):
            day_date = curr_date + timedelta(days=d)
            weather = weather_prov.get_weather_metrics(c_to, day_date, current_run_date)
            
            day = DailySchedule(
                day_number=len(schedule) + 1,
                date=day_date,
                origin=c_from,
                destination=c_to,
                distance_miles=day_dist,
                ascent_feet=day_ascent,
                high_temp_f=weather["high_temp_f"],
                low_temp_f=weather["low_temp_f"]
            )
            schedule.append(day)
            
        legs.append(leg)
        curr_date += timedelta(days=days_needed)
        
    actual_itinerary = Itinerary(
        start_city=itinerary.start_city,
        completion_city=itinerary.completion_city,
        via_cities=list(itinerary.via_cities),
        legs=legs,
        schedule=schedule,
        start_date=start_date,
        original_geodesic_baseline=itinerary.original_geodesic_baseline
    )
    
    feasibility_eng.validate_itinerary(actual_itinerary)
    scoring_eng.score_itinerary(actual_itinerary)
    return actual_itinerary

def run_sensitivity_analysis(
    actual_it: Itinerary,
    opt_it: Itinerary,
    base_weights: Dict[str, float],
    scoring_eng: ScoringEngine
) -> List[Dict[str, Any]]:
    """Runs score sensitivity analysis by varying each weight by +/-0.10."""
    variations = []
    keys = ["weather", "distance", "hills"]
    perturbations = [-0.10, 0.10]
    
    # Include the baseline
    variations.append({
        "label": "Baseline",
        "weights": base_weights.copy(),
        "actual_score": actual_it.scores.total if actual_it.scores else 0.0,
        "opt_score": opt_it.scores.total if opt_it.scores else 0.0
    })
    
    for key in keys:
        for delta in perturbations:
            perturbed = base_weights.copy()
            perturbed[key] = max(0.0, perturbed[key] + delta)
            
            # Normalize to sum to 1.0
            total_w = sum(perturbed.values())
            if total_w > 0:
                for k in perturbed:
                    perturbed[k] = round(perturbed[k] / total_w, 4)
            else:
                perturbed = base_weights.copy()
                
            temp_config = copy.deepcopy(scoring_eng.config)
            temp_config["scoring"] = temp_config.get("scoring", {}).copy()
            temp_config["scoring"]["weights"] = perturbed
            
            temp_eng = ScoringEngine(temp_config)
            
            actual_copy = copy.deepcopy(actual_it)
            opt_copy = copy.deepcopy(opt_it)
            
            temp_eng.score_itinerary(actual_copy)
            temp_eng.score_itinerary(opt_copy)
            
            variations.append({
                "label": f"Shift {key} by {delta:+.2f}",
                "weights": perturbed,
                "actual_score": actual_copy.scores.total if actual_copy.scores else 0.0,
                "opt_score": opt_copy.scores.total if opt_copy.scores else 0.0
            })
            
    return variations

def main():
    print("Starting Gone2Look4America Calibration Benchmarking...")
    
    # 1. Load benchmark request
    yaml_path = "examples/gone2look4america.yaml"
    parser = RequestParser(system_defaults_path="config/defaults.yaml")
    
    try:
        itinerary, config = parser.parse_request_file(yaml_path)
    except Exception as e:
        print(f"Error parsing {yaml_path}: {e}")
        sys.exit(1)
        
    config_mgr = ConfigManager(system_defaults_path="config/defaults.yaml")
    effective_config = config_mgr.get_effective_config(config)
    
    # Setup mock providers for clean, fast, deterministic testing/caching
    routing_prov = MockRoutingProvider()
    weather_prov = MockWeatherProvider()
    elevation_prov = MockElevationProvider()
    
    effective_config["routing_provider"] = routing_prov
    effective_config["weather_provider"] = weather_prov
    effective_config["elevation_provider"] = elevation_prov
    
    # Ensure database caching is set up
    solver = BeamSearchSolver("tests/calibration_cache.db")
    
    # Directional routing preferences
    prefs = effective_config.get("routing_preferences", {
        "avoid_highways": True,
        "avoid_tolls": True,
        "allow_ferries": True,
        "allow_international_borders": True
    })
    
    routing_cached = CachedRoutingProvider(routing_prov, solver._cache_manager, "mock")
    weather_cached = CachedWeatherProvider(weather_prov, solver._cache_manager)
    
    feasibility_eng = FeasibilityEngine(effective_config)
    scoring_eng = ScoringEngine(effective_config)
    
    # 2. Build the Cyclist's Actual sequential route
    print("Building and scoring the cyclist's actual chronological route...")
    start_date = itinerary.start_date or date(2023, 4, 29)
    current_run_date = date(2023, 4, 29)
    
    actual_it = build_actual_itinerary(
        itinerary, start_date, routing_cached, weather_cached,
        current_run_date, feasibility_eng, scoring_eng, prefs
    )
    
    # 3. Solve for the Optimized route
    print("Running Anytime Beam Search solver (beam_width=25) to compute optimized route...")
    # Set search constraints for the calibration benchmark run
    effective_config["solver_constraints"] = {
        "beam_width": 25,
        "max_search_minutes": 1.5
    }
    
    solver_start = time.time()
    results = solver.solve(itinerary, effective_config)
    solver_duration = time.time() - solver_start
    
    if not results:
        print("Solver failed to return any itineraries.")
        solver.close()
        sys.exit(1)
        
    opt_it = results[0]
    
    print("Comparing route outcomes...")
    
    # 4. Sensitivity Analysis
    base_weights = effective_config.get("scoring", {}).get("weights", {"weather": 0.45, "distance": 0.30, "hills": 0.25})
    sensitivity = run_sensitivity_analysis(actual_it, opt_it, base_weights, scoring_eng)
    
    # 5. Generate Markdown Report
    report = []
    report.append("# Gone2Look4America Calibration & Quality Report")
    report.append("\nThis report documents the calibration of the `g2l4a` multi-objective route optimizer against the cyclist's actual real-world journey.")
    
    report.append("\n## Route Comparison Overview")
    report.append("| Route Metric | Cyclist Actual Path | Solver Optimized Path | Difference |")
    report.append("| :--- | :---: | :---: | :---: |")
    
    actual_miles = sum(leg.distance_miles for leg in actual_it.legs)
    opt_miles = sum(leg.distance_miles for leg in opt_it.legs)
    report.append(f"| **Total Distance (mi)** | {actual_miles:.1f} | {opt_miles:.1f} | {opt_miles - actual_miles:+.1f} |")
    
    actual_climb = sum(leg.ascent_feet for leg in actual_it.legs)
    opt_climb = sum(leg.ascent_feet for leg in opt_it.legs)
    report.append(f"| **Total Ascent (ft)** | {actual_climb:,.0f} | {opt_climb:,.0f} | {opt_climb - actual_climb:+,.0f} |")
    
    actual_w = actual_it.scores.weather if actual_it.scores else 0.0
    opt_w = opt_it.scores.weather if opt_it.scores else 0.0
    report.append(f"| **Weather Comfort Score** | {actual_w:.4f} | {opt_w:.4f} | {opt_w - actual_w:+.4f} |")
    
    actual_d = actual_it.scores.distance if actual_it.scores else 0.0
    opt_d = opt_it.scores.distance if opt_it.scores else 0.0
    report.append(f"| **Distance Detour Score** | {actual_d:.4f} | {opt_d:.4f} | {opt_d - actual_d:+.4f} |")
    
    actual_h = actual_it.scores.hills if actual_it.scores else 0.0
    opt_h = opt_it.scores.hills if opt_it.scores else 0.0
    report.append(f"| **Hill Climb Score** | {actual_h:.4f} | {opt_h:.4f} | {opt_h - actual_h:+.4f} |")
    
    actual_tot = actual_it.scores.total if actual_it.scores else 0.0
    opt_tot = opt_it.scores.total if opt_it.scores else 0.0
    report.append(f"| **Total Desirability Score** | **{actual_tot:.4f}** | **{opt_tot:.4f}** | **{opt_tot - actual_tot:+.4f}** |")
    report.append(f"| **Feasibility Status** | {'Feasible ✅' if actual_it.is_feasible else 'Infeasible ❌'} | {'Feasible ✅' if opt_it.is_feasible else 'Infeasible ❌'} | - |")
    
    report.append("\n## Weight Sensitivity Analysis")
    report.append("Each weight perturbed by +/- 0.10 and normalized to sum to 1.0.")
    report.append("\n| Weight Shift / Label | Weights (W_w / W_d / W_h) | Cyclist Actual Score | Solver Optimized Score | Improvement |")
    report.append("| :--- | :---: | :---: | :---: | :---: |")
    
    for s in sensitivity:
        w_str = f"{s['weights']['weather']:.2f} / {s['weights']['distance']:.2f} / {s['weights']['hills']:.2f}"
        report.append(f"| {s['label']} | {w_str} | {s['actual_score']:.4f} | {s['opt_score']:.4f} | {s['opt_score'] - s['actual_score']:+.4f} |")
        
    report.append("\n## Solver Execution Performance")
    report.append(f"- **Execution Duration**: {solver_duration * 1000:.1f} ms")
    report.append(f"- **Evaluated Candidates**: {len(results)} recommendations returned")
    
    report.append("\n## Sequence Ordered Visits Comparison")
    report.append("\n### Cyclist Actual Via Cities Order:")
    actual_names = [c.name for c in actual_it.via_cities]
    report.append(", ".join(actual_names))
    
    report.append("\n### Solver Recommended Via Cities Order:")
    opt_names = [c.name for c in opt_it.via_cities]
    report.append(", ".join(opt_names))
    
    # Save the report
    report_content = "\n".join(report) + "\n"
    os.makedirs("reports", exist_ok=True)
    with open("reports/calibration-report.md", "w") as f:
        f.write(report_content)
        
    print("Calibration benchmarking complete! Report saved to reports/calibration-report.md")
    
    solver.close()
    if os.path.exists("tests/calibration_cache.db"):
        try:
            os.remove("tests/calibration_cache.db")
        except OSError:
            pass

if __name__ == "__main__":
    main()
