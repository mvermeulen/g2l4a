import time
from datetime import date
import pytest
from src.domain import City, Itinerary
from src.solver_engine import BeamSearchSolver
from src.mocks import MockRoutingProvider, MockWeatherProvider, MockElevationProvider

@pytest.fixture
def clean_solver():
    solver = BeamSearchSolver("tests/test_solver_cache.db")
    yield solver
    solver.close()
    import os
    if os.path.exists("tests/test_solver_cache.db"):
        try:
            os.remove("tests/test_solver_cache.db")
        except OSError:
            pass

def test_greedy_tsp_warm_start_seeding(clean_solver):
    c_start = City(name="Montgomery", latitude=32.3668, longitude=-86.3006)
    c_via1 = City(name="Portland", latitude=45.5152, longitude=-122.6784)
    c_via2 = City(name="Atlanta", latitude=33.7490, longitude=-84.3880)
    c_comp = City(name="Boise", latitude=43.6150, longitude=-116.2023)
    
    it = Itinerary(
        start_city=c_start,
        completion_city=c_comp,
        via_cities=[c_via1, c_via2],
        start_date=date(2026, 6, 1)
    )
    
    # Montgomery is closer to Atlanta than Portland, so Atlanta must be visited first!
    # TSP Sequence: Montgomery -> Atlanta -> Portland -> Boise
    config = {
        "routing_provider": MockRoutingProvider(),
        "weather_provider": MockWeatherProvider(),
        "elevation_provider": MockElevationProvider(),
        "routing_engine_name": "mock",
        "solver_constraints": {
            "beam_width": 1,
            "max_search_minutes": 1.0
        }
    }
    
    results = clean_solver.solve(it, config)
    assert len(results) > 0
    best = results[0]
    
    atl_idx = -1
    port_idx = -1
    for idx, day in enumerate(best.schedule):
        if day.destination.name == "Atlanta":
            atl_idx = idx
        elif day.destination.name == "Portland":
            port_idx = idx
            
    assert atl_idx != -1
    assert port_idx != -1
    assert atl_idx < port_idx
    
def test_beam_search_solver_basic(clean_solver):
    c_start = City(name="Montgomery", latitude=32.3668, longitude=-86.3006)
    c_via1 = City(name="Atlanta", latitude=33.7490, longitude=-84.3880)
    c_comp = City(name="Tallahassee", latitude=30.4383, longitude=-84.2807)
    
    it = Itinerary(
        start_city=c_start,
        completion_city=c_comp,
        via_cities=[c_via1],
        start_date=date(2026, 6, 1)
    )
    
    config = {
        "routing_provider": MockRoutingProvider(),
        "weather_provider": MockWeatherProvider(),
        "elevation_provider": MockElevationProvider(),
        "routing_engine_name": "mock",
        "daily_constraints": {
            "max_miles_per_day": 250.0
        },
        "solver_constraints": {
            "beam_width": 5,
            "max_search_minutes": 1.0
        }
    }
    
    results = clean_solver.solve(it, config)
    assert len(results) > 0
    
    best = results[0]
    assert best.start_city == c_start
    assert best.completion_city == c_comp
    assert len(best.via_cities) == 1
    assert best.via_cities[0] == c_via1
    assert len(best.schedule) == 2
    assert best.is_feasible is True
    assert best.scores.total > 0.0

def test_solver_timeout_budgeting(clean_solver):
    c_start = City(name="Montgomery", latitude=32.3668, longitude=-86.3006)
    c_via1 = City(name="Portland", latitude=45.5152, longitude=-122.6784)
    c_comp = City(name="Boise", latitude=43.6150, longitude=-116.2023)
    
    it = Itinerary(
        start_city=c_start,
        completion_city=c_comp,
        via_cities=[c_via1],
        start_date=date(2026, 6, 1)
    )
    
    # Set timeout extremely small (0.0 minutes) to trigger immediate search abort
    config = {
        "routing_provider": MockRoutingProvider(),
        "weather_provider": MockWeatherProvider(),
        "elevation_provider": MockElevationProvider(),
        "routing_engine_name": "mock",
        "solver_constraints": {
            "beam_width": 5,
            "max_search_minutes": 0.0
        }
    }
    
    # The solver should gracefully abort full search and still return the warm-start seed!
    results = clean_solver.solve(it, config)
    assert len(results) > 0
    assert results[0].start_date == date(2026, 6, 1)

def test_solver_early_pruning_constraints(clean_solver):
    c_start = City(name="Montgomery", latitude=32.3668, longitude=-86.3006)
    c_via1 = City(name="Atlanta", latitude=33.7490, longitude=-84.3880)
    c_comp = City(name="Tallahassee", latitude=30.4383, longitude=-84.2807)
    
    it = Itinerary(
        start_city=c_start,
        completion_city=c_comp,
        via_cities=[c_via1],
        start_date=date(2026, 6, 1)
    )
    
    # Restrict weather constraints to be extremely cold/impossible.
    # The search branches will be pruned instantly due to weather infeasibility!
    config = {
        "routing_provider": MockRoutingProvider(),
        "weather_provider": MockWeatherProvider(),
        "elevation_provider": MockElevationProvider(),
        "routing_engine_name": "mock",
        "weather_constraints": {
            "max_avg_high_f": 10.0
        },
        "solver_constraints": {
            "beam_width": 5,
            "max_search_minutes": 1.0
        }
    }
    
    results = clean_solver.solve(it, config)
    assert len(results) > 0
    # The search branches were pruned, so only the fallback warm-start seed (which is marked unfeasible due to weather) is returned!
    assert results[0].is_feasible is False

def test_solver_deterministic_replay(clean_solver):
    c_start = City(name="Montgomery", latitude=32.3668, longitude=-86.3006)
    c_via1 = City(name="Atlanta", latitude=33.7490, longitude=-84.3880)
    c_via2 = City(name="Tallahassee", latitude=30.4383, longitude=-84.2807)
    c_comp = City(name="Boise", latitude=43.6150, longitude=-116.2023)
    
    it = Itinerary(
        start_city=c_start,
        completion_city=c_comp,
        via_cities=[c_via1, c_via2],
        start_date=date(2026, 6, 1)
    )
    
    config = {
        "routing_provider": MockRoutingProvider(),
        "weather_provider": MockWeatherProvider(),
        "elevation_provider": MockElevationProvider(),
        "routing_engine_name": "mock",
        "solver_constraints": {
            "beam_width": 10,
            "max_search_minutes": 1.0
        }
    }
    
    res1 = clean_solver.solve(it, config)
    res2 = clean_solver.solve(it, config)
    
    assert len(res1) == len(res2)
    for i in range(len(res1)):
        assert res1[i].via_cities == res2[i].via_cities
        assert res1[i].scores.total == res2[i].scores.total
