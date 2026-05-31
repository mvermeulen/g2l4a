import os
import pytest
from datetime import date
from src.domain import City, Itinerary, DailySchedule, Leg, Scores
from src.validation import RequestParser
from src.config import ConfigManager
from src.cached_providers import CachedRoutingProvider, CachedWeatherProvider
from src.mocks import MockRoutingProvider, MockWeatherProvider, MockElevationProvider
from src.feasibility import FeasibilityEngine
from src.scoring import ScoringEngine
from src.solver_engine import BeamSearchSolver
from src.calibration import build_actual_itinerary, run_sensitivity_analysis, main

def test_build_actual_itinerary():
    c1 = City(name="Washington, DC", latitude=38.9072, longitude=-77.0369)
    c2 = City(name="Annapolis, Maryland", latitude=38.9784, longitude=-76.4922)
    c3 = City(name="Olympia, Washington", latitude=47.0379, longitude=-122.9007)
    
    it = Itinerary(
        start_city=c1,
        completion_city=c3,
        via_cities=[c2],
        start_date=date(2023, 4, 29)
    )
    
    config = {
        "scoring": {
            "weights": {
                "weather": 0.45,
                "distance": 0.30,
                "hills": 0.25
            }
        }
    }
    
    routing_prov = MockRoutingProvider()
    weather_prov = MockWeatherProvider()
    solver = BeamSearchSolver("tests/test_calib_cache.db")
    
    routing_cached = CachedRoutingProvider(routing_prov, solver._cache_manager, "mock")
    weather_cached = CachedWeatherProvider(weather_prov, solver._cache_manager)
    
    feasibility_eng = FeasibilityEngine(config)
    scoring_eng = ScoringEngine(config)
    
    prefs = {
        "avoid_highways": True,
        "avoid_tolls": True,
        "allow_ferries": True,
        "allow_international_borders": True
    }
    
    actual_it = build_actual_itinerary(
        it, date(2023, 4, 29), routing_cached, weather_cached,
        date(2023, 4, 29), feasibility_eng, scoring_eng, prefs
    )
    
    assert actual_it.start_city == c1
    assert actual_it.completion_city == c3
    assert len(actual_it.via_cities) == 1
    assert actual_it.via_cities[0] == c2
    assert len(actual_it.schedule) == 32
    assert actual_it.scores is not None
    assert actual_it.scores.total > 0.0
    
    solver.close()
    if os.path.exists("tests/test_calib_cache.db"):
        try:
            os.remove("tests/test_calib_cache.db")
        except OSError:
            pass

def test_run_sensitivity_analysis():
    c1 = City(name="Washington, DC", latitude=38.9072, longitude=-77.0369)
    c2 = City(name="Olympia, Washington", latitude=47.0379, longitude=-122.9007)
    
    it_actual = Itinerary(
        start_city=c1, completion_city=c2, via_cities=[],
        schedule=[DailySchedule(day_number=1, date=date(2023, 4, 29), origin=c1, destination=c2, distance_miles=100.0, ascent_feet=500.0, high_temp_f=70.0, low_temp_f=50.0)],
        legs=[Leg(origin=c1, destination=c2, distance_miles=100.0, ascent_feet=500.0)],
        scores=Scores(weather=0.8, distance=0.9, hills=0.7, total=0.8)
    )
    
    it_opt = Itinerary(
        start_city=c1, completion_city=c2, via_cities=[],
        schedule=[DailySchedule(day_number=1, date=date(2023, 4, 29), origin=c1, destination=c2, distance_miles=90.0, ascent_feet=400.0, high_temp_f=70.0, low_temp_f=50.0)],
        legs=[Leg(origin=c1, destination=c2, distance_miles=90.0, ascent_feet=400.0)],
        scores=Scores(weather=0.8, distance=0.95, hills=0.8, total=0.85)
    )
    
    base_weights = {"weather": 0.45, "distance": 0.30, "hills": 0.25}
    scoring_eng = ScoringEngine({"scoring": {"weights": base_weights}})
    
    sensitivity = run_sensitivity_analysis(it_actual, it_opt, base_weights, scoring_eng)
    
    # 1 baseline + 3 keys * 2 perturbations = 7 variations
    assert len(sensitivity) == 7
    assert sensitivity[0]["label"] == "Baseline"
    assert abs(sensitivity[0]["actual_score"] - 0.8) < 1e-4
    assert abs(sensitivity[0]["opt_score"] - 0.85) < 1e-4

def test_main_execution():
    # Verify that calling main completes successfully and generates the report
    report_path = "reports/calibration-report.md"
    if os.path.exists(report_path):
        os.remove(report_path)
        
    main()
    
    assert os.path.exists(report_path)
    with open(report_path, "r") as f:
        content = f.read()
    assert "# Gone2Look4America Calibration & Quality Report" in content
    assert "## Route Comparison Overview" in content
