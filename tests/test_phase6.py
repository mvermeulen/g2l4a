import json
from datetime import date
import pytest
from src.domain import City, Itinerary, DailySchedule, Leg, Scores
from src.metrics import SolverMetrics
from src.output import OutputFormatter

def test_format_recommendations_markdown():
    c1 = City(name="A", latitude=30.0, longitude=-90.0)
    c2 = City(name="B", latitude=31.0, longitude=-91.0)
    
    it1 = Itinerary(
        start_city=c1, completion_city=c2, via_cities=[],
        start_date=date(2026, 6, 1),
        legs=[Leg(origin=c1, destination=c2, distance_miles=50.0, ascent_feet=100.0)],
        schedule=[DailySchedule(day_number=1, date=date(2026, 6, 1), origin=c1, destination=c2, distance_miles=50.0, ascent_feet=100.0, high_temp_f=70.0, low_temp_f=50.0)],
        scores=Scores(weather=1.0, distance=1.0, hills=1.0, total=1.0)
    )
    
    it2 = Itinerary(
        start_city=c1, completion_city=c2, via_cities=[],
        start_date=date(2026, 6, 1),
        legs=[Leg(origin=c1, destination=c2, distance_miles=150.0, ascent_feet=100.0)],
        schedule=[DailySchedule(day_number=1, date=date(2026, 6, 1), origin=c1, destination=c2, distance_miles=150.0, ascent_feet=100.0, high_temp_f=70.0, low_temp_f=50.0)],
        is_feasible=False,
        violation_details=[{"code": "INFEASIBLE_DAILY_MILEAGE", "location": "Leg: A -> B", "date": "2026-06-01", "observed_value": 150.0, "threshold_limit": 80.0, "remediation_hint": "Bypass"}]
    )
    
    metrics = SolverMetrics()
    metrics.start()
    time_spent = 0.05
    metrics.duration_ms = time_spent * 1000.0
    metrics.evaluated_permutations = 10
    metrics.pruned_branches = 2
    metrics.l1_cache_hits = 5
    metrics.l2_cache_hits = 3
    
    md_output = OutputFormatter.format_recommendations_markdown([it1, it2], metrics)
    
    # Assert main markdown sections
    assert "# Route Recommendations Comparison" in md_output
    assert "## Overview Comparison" in md_output
    assert "**Best Recommendation**" in md_output
    assert "Alternative 1" in md_output
    assert "Yes" in md_output
    assert "No ❌" in md_output
    assert "<details>" in md_output
    assert "<summary>Click to view daily travel schedule</summary>" in md_output
    assert "## Solver Execution Performance" in md_output
    assert "Execution Duration" in md_output
    assert "Evaluated Candidates" in md_output

def test_serialize_recommendations_json():
    c1 = City(name="A", latitude=30.0, longitude=-90.0)
    c2 = City(name="B", latitude=31.0, longitude=-91.0)
    
    it1 = Itinerary(
        start_city=c1, completion_city=c2, via_cities=[],
        start_date=date(2026, 6, 1),
        legs=[Leg(origin=c1, destination=c2, distance_miles=50.0, ascent_feet=100.0)],
        schedule=[DailySchedule(day_number=1, date=date(2026, 6, 1), origin=c1, destination=c2, distance_miles=50.0, ascent_feet=100.0, high_temp_f=70.0, low_temp_f=50.0)],
        scores=Scores(weather=1.0, distance=1.0, hills=1.0, total=1.0)
    )
    
    metrics = SolverMetrics()
    metrics.duration_ms = 150.0
    metrics.evaluated_permutations = 25
    metrics.pruned_branches = 4
    
    json_output = OutputFormatter.serialize_recommendations_json([it1], metrics)
    data = json.loads(json_output)
    
    # Assert JSON payload schema compliance
    assert "solver_metrics" in data
    assert "recommendations" in data
    assert len(data["recommendations"]) == 1
    
    # Verify metrics fields
    assert data["solver_metrics"]["duration_ms"] == 150.0
    assert data["solver_metrics"]["evaluated_permutations"] == 25
    assert data["solver_metrics"]["pruned_branches"] == 4
    
    # Verify itinerary fields
    best = data["recommendations"][0]
    assert best["is_feasible"] is True
    assert best["start_city"] == "A"
    assert best["completion_city"] == "B"
    assert best["start_date"] == "2026-06-01"
    assert best["scores"]["total"] == 1.0
    assert len(best["schedule"]) == 1
    assert best["schedule"][0]["high_temp_f"] == 70.0


def test_serialize_recommendations_json_with_data_attribution():
    c1 = City(name="A", latitude=30.0, longitude=-90.0)
    c2 = City(name="B", latitude=31.0, longitude=-91.0)

    it = Itinerary(
        start_city=c1,
        completion_city=c2,
        via_cities=[],
        start_date=date(2026, 6, 1),
        legs=[Leg(origin=c1, destination=c2, distance_miles=50.0, ascent_feet=100.0)],
        schedule=[
            DailySchedule(
                day_number=1,
                date=date(2026, 6, 1),
                origin=c1,
                destination=c2,
                distance_miles=50.0,
                ascent_feet=100.0,
                high_temp_f=70.0,
                low_temp_f=50.0,
            )
        ],
        scores=Scores(weather=1.0, distance=1.0, hills=1.0, total=1.0),
    )

    attribution = {
        "provider": "Open-Meteo",
        "provider_url": "https://open-meteo.com/",
        "license": "CC BY 4.0",
        "license_url": "https://creativecommons.org/licenses/by/4.0/",
    }

    json_output = OutputFormatter.serialize_recommendations_json([it], data_attribution=attribution)
    data = json.loads(json_output)
    assert "data_attribution" in data
    assert data["data_attribution"]["provider"] == "Open-Meteo"


def test_serialize_json_with_data_attribution():
    c1 = City(name="A", latitude=30.0, longitude=-90.0)
    c2 = City(name="B", latitude=31.0, longitude=-91.0)

    it = Itinerary(
        start_city=c1,
        completion_city=c2,
        via_cities=[],
        start_date=date(2026, 6, 1),
        legs=[Leg(origin=c1, destination=c2, distance_miles=50.0, ascent_feet=100.0)],
        schedule=[
            DailySchedule(
                day_number=1,
                date=date(2026, 6, 1),
                origin=c1,
                destination=c2,
                distance_miles=50.0,
                ascent_feet=100.0,
                high_temp_f=70.0,
                low_temp_f=50.0,
            )
        ],
        scores=Scores(weather=1.0, distance=1.0, hills=1.0, total=1.0),
    )

    attribution = {
        "provider": "Open-Meteo",
        "provider_url": "https://open-meteo.com/",
        "license": "CC BY 4.0",
        "license_url": "https://creativecommons.org/licenses/by/4.0/",
    }

    json_output = OutputFormatter.serialize_json(it, data_attribution=attribution)
    data = json.loads(json_output)
    assert "data_attribution" in data
    assert data["data_attribution"]["license"] == "CC BY 4.0"
