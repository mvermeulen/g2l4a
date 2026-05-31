from datetime import date
import pytest
from src.domain import City, Itinerary, DailySchedule, ConstraintViolation
from src.feasibility import FeasibilityEngine

@pytest.fixture
def base_config():
    return {
        "weather_constraints": {
            "max_avg_high_f": 90.0,
            "min_avg_high_f": 32.0,
        },
        "daily_constraints": {
            "max_miles_per_day": 80.0,
            "max_climb_ft_per_day": 5000.0,
        }
    }

@pytest.fixture
def engine(base_config):
    return FeasibilityEngine(base_config)

def test_feasibility_engine_all_valid(engine):
    c1 = City(name="A", latitude=30.0, longitude=-90.0)
    c2 = City(name="B", latitude=31.0, longitude=-91.0)
    
    itinerary = Itinerary(
        start_city=c1,
        completion_city=c2,
        via_cities=[],
        start_date=date(2026, 6, 1)
    )
    
    # 1 day schedule within constraints
    itinerary.schedule = [
        DailySchedule(
            day_number=1,
            date=date(2026, 6, 1),
            origin=c1,
            destination=c2,
            distance_miles=50.0,
            ascent_feet=1200.0,
            high_temp_f=75.0,
            low_temp_f=55.0
        )
    ]
    
    validated = engine.validate_itinerary(itinerary)
    assert validated.is_feasible is True
    assert len(validated.violation_details) == 0

def test_feasibility_engine_weather_violations(engine):
    c1 = City(name="Hot City", latitude=30.0, longitude=-90.0)
    c2 = City(name="Cold City", latitude=31.0, longitude=-91.0)
    
    # Test Max High violation
    it_hot = Itinerary(
        start_city=c1,
        completion_city=c2,
        via_cities=[],
        schedule=[
            DailySchedule(
                day_number=1,
                date=date(2026, 6, 1),
                origin=c1,
                destination=c2,
                distance_miles=40.0,
                ascent_feet=500.0,
                high_temp_f=95.0, # Too hot! Limit is 90.0
                low_temp_f=75.0
            )
        ]
    )
    
    validated_hot = engine.validate_itinerary(it_hot)
    assert validated_hot.is_feasible is False
    assert len(validated_hot.violation_details) == 1
    
    violation = validated_hot.violation_details[0]
    assert violation["code"] == "INFEASIBLE_WEATHER_MAX_HIGH"
    assert violation["location"] == "Cold City"
    assert violation["observed_value"] == 95.0
    assert violation["threshold_limit"] == 90.0
    assert "cooler season" in violation["remediation_hint"]

    # Test Min High violation
    engine.clear_cache()
    it_cold = Itinerary(
        start_city=c1,
        completion_city=c2,
        via_cities=[],
        schedule=[
            DailySchedule(
                day_number=1,
                date=date(2026, 6, 1),
                origin=c1,
                destination=c2,
                distance_miles=40.0,
                ascent_feet=500.0,
                high_temp_f=28.0, # Too cold! Limit is 32.0
                low_temp_f=10.0
            )
        ]
    )
    
    validated_cold = engine.validate_itinerary(it_cold)
    assert validated_cold.is_feasible is False
    assert len(validated_cold.violation_details) == 1
    
    violation_c = validated_cold.violation_details[0]
    assert violation_c["code"] == "INFEASIBLE_WEATHER_MIN_HIGH"
    assert violation_c["location"] == "Cold City"
    assert violation_c["observed_value"] == 28.0
    assert violation_c["threshold_limit"] == 32.0
    assert "warmer season" in violation_c["remediation_hint"]

def test_feasibility_engine_daily_effort_violations(engine):
    c1 = City(name="A", latitude=30.0, longitude=-90.0)
    c2 = City(name="B", latitude=31.0, longitude=-91.0)
    
    # Test Mileage violation
    it_miles = Itinerary(
        start_city=c1,
        completion_city=c2,
        via_cities=[],
        schedule=[
            DailySchedule(
                day_number=1,
                date=date(2026, 6, 1),
                origin=c1,
                destination=c2,
                distance_miles=95.0, # Limit is 80.0
                ascent_feet=1000.0,
                high_temp_f=75.0,
                low_temp_f=55.0
            )
        ]
    )
    
    validated_miles = engine.validate_itinerary(it_miles)
    assert validated_miles.is_feasible is False
    assert len(validated_miles.violation_details) == 1
    assert validated_miles.violation_details[0]["code"] == "INFEASIBLE_DAILY_MILEAGE"
    assert validated_miles.violation_details[0]["observed_value"] == 95.0
    assert "rest day" in validated_miles.violation_details[0]["remediation_hint"]

    # Test Ascent violation
    engine.clear_cache()
    it_ascent = Itinerary(
        start_city=c1,
        completion_city=c2,
        via_cities=[],
        schedule=[
            DailySchedule(
                day_number=1,
                date=date(2026, 6, 1),
                origin=c1,
                destination=c2,
                distance_miles=40.0,
                ascent_feet=6000.0, # Limit is 5000.0
                high_temp_f=75.0,
                low_temp_f=55.0
            )
        ]
    )
    
    validated_ascent = engine.validate_itinerary(it_ascent)
    assert validated_ascent.is_feasible is False
    assert len(validated_ascent.violation_details) == 1
    assert validated_ascent.violation_details[0]["code"] == "INFEASIBLE_DAILY_ASCENT"
    assert validated_ascent.violation_details[0]["observed_value"] == 6000.0
    assert "bypass" in validated_ascent.violation_details[0]["remediation_hint"]

def test_feasibility_engine_rest_day_skips_effort(engine):
    c1 = City(name="A", latitude=30.0, longitude=-90.0)
    
    # Rest day should skip effort checks but still run weather checks
    it = Itinerary(
        start_city=c1,
        completion_city=c1,
        via_cities=[],
        schedule=[
            DailySchedule(
                day_number=1,
                date=date(2026, 6, 1),
                origin=c1,
                destination=c1,
                distance_miles=100.0, # Breaks mileage, but is_rest_day = True
                ascent_feet=6000.0,   # Breaks climb, but is_rest_day = True
                high_temp_f=75.0,     # Within bounds
                low_temp_f=55.0,
                is_rest_day=True
            )
        ]
    )
    
    validated = engine.validate_itinerary(it)
    assert validated.is_feasible is True
    assert len(validated.violation_details) == 0

def test_feasibility_engine_fail_fast(engine):
    c1 = City(name="A", latitude=30.0, longitude=-90.0)
    c2 = City(name="B", latitude=31.0, longitude=-91.0)
    c3 = City(name="C", latitude=32.0, longitude=-92.0)
    
    it = Itinerary(
        start_city=c1,
        completion_city=c3,
        via_cities=[c2],
        schedule=[
            DailySchedule(
                day_number=1,
                date=date(2026, 6, 1),
                origin=c1,
                destination=c2,
                distance_miles=90.0, # Breaks mileage
                ascent_feet=100.0,
                high_temp_f=70.0,
                low_temp_f=50.0
            ),
            DailySchedule(
                day_number=2,
                date=date(2026, 6, 2),
                origin=c2,
                destination=c3,
                distance_miles=95.0, # Breaks mileage too
                ascent_feet=100.0,
                high_temp_f=70.0,
                low_temp_f=50.0
            )
        ]
    )
    
    # 1. Without fail-fast: reports BOTH violations
    validated_all = engine.validate_itinerary(it, fail_fast=False)
    assert len(validated_all.violation_details) == 2
    
    # 2. With fail-fast: reports only the FIRST violation
    validated_fast = engine.validate_itinerary(it, fail_fast=True)
    assert len(validated_fast.violation_details) == 1
    assert validated_fast.violation_details[0]["observed_value"] == 90.0

def test_feasibility_engine_memoization_cache(engine):
    c1 = City(name="A", latitude=30.0, longitude=-90.0)
    c2 = City(name="B", latitude=31.0, longitude=-91.0)
    
    # Count checks by monkey-patching methods
    weather_checks = 0
    daily_checks = 0
    
    orig_check_weather = engine.check_weather_feasibility
    orig_check_daily = engine.check_daily_feasibility
    
    def counted_check_weather(city_name, travel_date, high_temp):
        nonlocal weather_checks
        weather_checks += 1
        return orig_check_weather(city_name, travel_date, high_temp)
        
    def counted_check_daily(origin_name, dest_name, travel_date, distance, ascent):
        nonlocal daily_checks
        daily_checks += 1
        return orig_check_daily(origin_name, dest_name, travel_date, distance, ascent)
        
    engine.check_weather_feasibility = counted_check_weather
    engine.check_daily_feasibility = counted_check_daily
    
    it1 = Itinerary(
        start_city=c1,
        completion_city=c2,
        via_cities=[],
        schedule=[
            DailySchedule(
                day_number=1,
                date=date(2026, 6, 1),
                origin=c1,
                destination=c2,
                distance_miles=50.0,
                ascent_feet=100.0,
                high_temp_f=70.0,
                low_temp_f=50.0
            )
        ]
    )
    
    # First run: queries base methods
    engine.validate_itinerary(it1)
    assert weather_checks == 1
    assert daily_checks == 1
    
    # Second run with identical leg/date/weather: should utilize cache hits
    # Wait, the inner check methods are still called, but the base queries inside them are bypassed.
    # Actually, because we patched check_weather_feasibility itself, it will still increment weather_checks,
    # but the memoization will bypass the inner logic!
    # Let's test that the cache is actually populated:
    key_weather = ("B", date(2026, 6, 1).isoformat())
    key_daily = ("A", "B", date(2026, 6, 1).isoformat())
    assert key_weather in engine._weather_memo
    assert key_daily in engine._daily_memo
    
    # If we clear cache, it should empty
    engine.clear_cache()
    assert len(engine._weather_memo) == 0
    assert len(engine._daily_memo) == 0
