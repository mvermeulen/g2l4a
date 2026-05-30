import os
import pytest
from datetime import date
from src.config import ConfigManager, deep_merge
from src.domain import City, ScoringWeights, Scores, Leg
from src.mocks import MockRoutingProvider, MockWeatherProvider, MockElevationProvider
from src.metrics import SolverMetrics

def test_deep_merge():
    base = {
        "scoring": {
            "weights": {
                "weather": 0.45,
                "distance": 0.30,
                "hills": 0.25
            }
        },
        "routing_preferences": {
            "avoid_highways": True,
            "avoid_tolls": True
        }
    }
    overrides = {
        "scoring": {
            "weights": {
                "weather": 0.60
            }
        },
        "routing_preferences": {
            "avoid_highways": False
        }
    }
    
    merged = deep_merge(base, overrides)
    
    # Check deep merge succeeded
    assert merged["scoring"]["weights"]["weather"] == 0.60
    assert merged["scoring"]["weights"]["distance"] == 0.30  # Preserved
    assert merged["scoring"]["weights"]["hills"] == 0.25     # Preserved
    assert merged["routing_preferences"]["avoid_highways"] is False
    assert merged["routing_preferences"]["avoid_tolls"] is True  # Preserved


def test_config_manager_hierarchy():
    # Write a temporary system defaults YAML file
    temp_defaults_path = "tests/temp_defaults.yaml"
    os.makedirs("tests", exist_ok=True)
    
    system_defaults_content = """
defaults:
  weather_constraints:
    max_avg_high_f: 85.0
  daily_constraints:
    max_miles_per_day: 75.0
  scoring:
    weights:
      weather: 0.50
      distance: 0.30
      hills: 0.20
"""
    with open(temp_defaults_path, "w") as f:
        f.write(system_defaults_content)
        
    try:
        manager = ConfigManager(system_defaults_path=temp_defaults_path)
        
        # Test 1: No overrides (merges system defaults with built-in fallbacks)
        config1 = manager.get_effective_config()
        assert config1["weather_constraints"]["max_avg_high_f"] == 85.0  # System default
        assert config1["weather_constraints"]["min_avg_high_f"] == 32.0  # Built-in fallback
        assert config1["daily_constraints"]["max_miles_per_day"] == 75.0 # System default
        assert config1["daily_constraints"]["max_climb_ft_per_day"] == 5000.0 # Built-in fallback
        
        # Test 2: User overrides (highest precedence)
        user_overrides = {
            "weather_constraints": {
                "max_avg_high_f": 80.0
            },
            "routing_preferences": {
                "avoid_highways": False
            }
        }
        config2 = manager.get_effective_config(user_overrides)
        assert config2["weather_constraints"]["max_avg_high_f"] == 80.0  # User override
        assert config2["weather_constraints"]["min_avg_high_f"] == 32.0  # Built-in fallback
        assert config2["daily_constraints"]["max_miles_per_day"] == 75.0 # System default
        assert config2["routing_preferences"]["avoid_highways"] is False # User override
        assert config2["routing_preferences"]["avoid_tolls"] is True   # Built-in fallback
        
    finally:
        if os.path.exists(temp_defaults_path):
            os.remove(temp_defaults_path)


def test_domain_model_validation():
    # Valid City
    austin = City(name="Austin", latitude=30.2672, longitude=-97.7431)
    assert austin.name == "Austin"
    
    # Invalid City (Latitude out of bounds)
    with pytest.raises(ValueError, match="Latitude must be between -90 and 90"):
        City(name="Invalid", latitude=95.0, longitude=0.0)
        
    # Invalid City (Longitude out of bounds)
    with pytest.raises(ValueError, match="Longitude must be between -180 and 180"):
        City(name="Invalid", latitude=0.0, longitude=-190.0)
        
    # Valid weights
    w = ScoringWeights(weather=0.45, distance=0.30, hills=0.25)
    assert w.weather == 0.45
    
    # Negative weights
    with pytest.raises(ValueError, match="Weights must be non-negative"):
        ScoringWeights(weather=-0.1, distance=0.6, hills=0.5)
        
    # Sum not 1
    with pytest.raises(ValueError, match="Weights must sum to 1.0"):
        ScoringWeights(weather=0.5, distance=0.5, hills=0.5)


def test_mock_routing_provider_determinism():
    city_a = City(name="City A", latitude=30.0, longitude=-90.0)
    city_b = City(name="City B", latitude=35.0, longitude=-95.0)
    
    preferences = {
        "avoid_highways": True,
        "avoid_tolls": True,
        "allow_ferries": True,
        "allow_international_borders": True
    }
    
    provider1 = MockRoutingProvider(seed=42)
    provider2 = MockRoutingProvider(seed=42)
    provider3 = MockRoutingProvider(seed=99)  # Different seed
    
    leg1 = provider1.get_leg_metrics(city_a, city_b, preferences)
    leg2 = provider2.get_leg_metrics(city_a, city_b, preferences)
    leg3 = provider3.get_leg_metrics(city_a, city_b, preferences)
    
    # Verify exact determinism for same seed
    assert leg1.distance_miles == leg2.distance_miles
    assert leg1.ascent_feet == leg2.ascent_feet
    assert leg1.is_bicycle_legal == leg2.is_bicycle_legal
    
    # Verify different seeds yield different ascent values (due to seed hashing)
    assert leg1.ascent_feet != leg3.ascent_feet


def test_mock_weather_provider_determinism_and_forecast():
    city = City(name="Chicago", latitude=41.8781, longitude=-87.6298)
    travel_date = date(2026, 7, 15)  # Mid summer July
    
    provider1 = MockWeatherProvider(seed=42)
    provider2 = MockWeatherProvider(seed=42)
    
    weather1 = provider1.get_weather_metrics(city, travel_date)
    weather2 = provider2.get_weather_metrics(city, travel_date)
    
    # Determinism
    assert weather1["high_temp_f"] == weather2["high_temp_f"]
    assert weather1["low_temp_f"] == weather2["low_temp_f"]
    assert weather1["is_forecast"] is False
    
    # Realistic seasonal check (Chicago in July should be warm)
    assert 65.0 <= weather1["high_temp_f"] <= 95.0
    
    # Forecast overlay test within 14 days of travel
    current_time = date(2026, 7, 10)  # 5 days before travel
    weather_fc = provider1.get_weather_metrics(city, travel_date, current_time=current_time)
    assert weather_fc["is_forecast"] is True
    # Verify anomaly injection worked (high temp changed slightly)
    assert weather_fc["high_temp_f"] != weather1["high_temp_f"]


def test_metrics_collection():
    metrics = SolverMetrics()
    metrics.start()
    
    metrics.evaluated_permutations += 10
    metrics.pruned_branches += 5
    metrics.routing_api_calls += 2
    metrics.l1_cache_hits += 8
    
    metrics.stop()
    
    payload = metrics.to_dict()
    assert payload["evaluated_permutations"] == 10
    assert payload["pruned_branches"] == 5
    assert payload["l1_cache_hits"] == 8
    assert payload["routing_api_calls"] == 2
    assert payload["cache_hit_rate"] == 0.80  # 8 / (8 + 0 + 2)
    assert payload["duration_ms"] >= 0.0


def test_output_formatting():
    from src.output import OutputFormatter
    from src.domain import Itinerary, DailySchedule, Scores, Leg
    import json
    
    city_a = City(name="Austin", latitude=30.2672, longitude=-97.7431)
    city_b = City(name="Dallas", latitude=32.7767, longitude=-96.7970)
    
    leg = Leg(origin=city_a, destination=city_b, distance_miles=195.0, ascent_feet=250.0)
    
    sched = DailySchedule(
        day_number=1,
        date=date(2026, 6, 1),
        origin=city_a,
        destination=city_b,
        distance_miles=195.0,
        ascent_feet=250.0,
        high_temp_f=88.0,
        low_temp_f=68.0
    )
    
    itinerary = Itinerary(
        start_city=city_a,
        completion_city=city_b,
        via_cities=[],
        legs=[leg],
        schedule=[sched],
        scores=Scores(weather=0.8, distance=0.7, hills=0.9, total=0.81)
    )
    
    # 1. Test schedule markdown
    md_sched = OutputFormatter.format_schedule_markdown(itinerary)
    assert "| Day | Date | Origin | Destination |" in md_sched
    assert "Austin" in md_sched
    assert "Dallas" in md_sched
    assert "195.0" in md_sched
    
    # 2. Test summary markdown (feasible)
    md_sum = OutputFormatter.format_summary_markdown(itinerary)
    assert "Total Distance" in md_sum
    assert "0.810" in md_sum
    
    # 3. Test JSON serialization
    js = OutputFormatter.serialize_json(itinerary)
    data = json.loads(js)
    assert data["is_feasible"] is True
    assert data["start_city"] == "Austin"
    assert len(data["legs"]) == 1
    
    # 4. Test summary markdown (infeasible)
    itinerary.is_feasible = False
    itinerary.violation_details = [{
        "code": "INFEASIBLE_WEATHER_MAX_HIGH",
        "location": "Dallas",
        "date": "2026-06-01",
        "observed_value": 95.0,
        "threshold_limit": 90.0,
        "remediation_hint": "Cool down"
    }]
    md_infeasible = OutputFormatter.format_summary_markdown(itinerary)
    assert "Violated Constraints" in md_infeasible
    assert "INFEASIBLE_WEATHER_MAX_HIGH" in md_infeasible
    
    # 5. Infeasible schedule return
    md_sched_inf = OutputFormatter.format_schedule_markdown(itinerary)
    assert md_sched_inf == "ROUTE INFEASIBLE\n"

