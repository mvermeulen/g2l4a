import os
import pytest
from datetime import date, timedelta
from src.domain import City, Itinerary, DailySchedule, Leg
from src.validation import extract_city_info, ValidationError, RequestParser
from src.solver_engine import BeamSearchSolver
from src.mocks import MockRoutingProvider, MockWeatherProvider, MockElevationProvider
from src.output import OutputFormatter

def test_extract_city_info():
    # Test valid string format
    name, rest = extract_city_info("Austin, Texas")
    assert name == "Austin, Texas"
    assert rest == 0

    # Test valid dictionary format
    name, rest = extract_city_info({"name": "Austin, Texas", "rest_days": 2})
    assert name == "Austin, Texas"
    assert rest == 2

    # Test valid dictionary format without rest_days
    name, rest = extract_city_info({"name": "Austin, Texas"})
    assert name == "Austin, Texas"
    assert rest == 0

    # Test invalid format type
    with pytest.raises(ValidationError) as exc:
        extract_city_info(123)
    assert exc.value.code == "INVALID_CITY_FORMAT"

    # Test dictionary without name
    with pytest.raises(ValidationError) as exc:
        extract_city_info({"rest_days": 2})
    assert exc.value.code == "INVALID_CITY_FORMAT"

    # Test dictionary with invalid name type
    with pytest.raises(ValidationError) as exc:
        extract_city_info({"name": 123, "rest_days": 2})
    assert exc.value.code == "INVALID_CITY_FORMAT"

    # Test negative rest_days
    with pytest.raises(ValidationError) as exc:
        extract_city_info({"name": "Austin, Texas", "rest_days": -1})
    assert exc.value.code == "INVALID_REST_DAYS"

    # Test non-integer rest_days
    with pytest.raises(ValidationError) as exc:
        extract_city_info({"name": "Austin, Texas", "rest_days": "two"})
    assert exc.value.code == "INVALID_REST_DAYS"


def test_request_parser_integration():
    parser = RequestParser()
    payload = {
        "start_city": {"name": "Austin, Texas", "rest_days": 1},
        "completion_city": "Manor, Texas",
        "via_cities": [
            {"name": "Bastrop, Texas", "rest_days": 2},
            "Giddings, Texas"
        ],
        "start_date": "2026-06-01"
    }

    itinerary, config = parser.parse_request_dict(payload)
    assert "Austin" in itinerary.start_city.name
    assert itinerary.start_city.rest_days == 1
    assert "Manor" in itinerary.completion_city.name
    assert itinerary.completion_city.rest_days == 0
    assert len(itinerary.via_cities) == 2
    assert "Bastrop" in itinerary.via_cities[0].name
    assert itinerary.via_cities[0].rest_days == 2
    assert "Giddings" in itinerary.via_cities[1].name
    assert itinerary.via_cities[1].rest_days == 0


def test_solver_engine_rest_days_scheduling():
    c_start = City(name="Austin, Texas", latitude=30.2672, longitude=-97.7431, rest_days=1)
    c_via = City(name="Bastrop, Texas", latitude=30.1105, longitude=-97.3153, rest_days=2)
    c_comp = City(name="Manor, Texas", latitude=30.3408, longitude=-97.5586, rest_days=1)

    it = Itinerary(
        start_city=c_start,
        completion_city=c_comp,
        via_cities=[c_via],
        start_date=date(2026, 6, 1)
    )

    config = {
        "routing_provider": MockRoutingProvider(),
        "weather_provider": MockWeatherProvider(),
        "elevation_provider": MockElevationProvider(),
        "routing_engine_name": "mock",
        "daily_constraints": {
            "max_miles_per_day": 200.0
        },
        "solver_constraints": {
            "beam_width": 2,
            "max_search_minutes": 1.0
        }
    }

    db_path = "tests/test_rest_days_solver.db"
    solver = BeamSearchSolver(db_path)
    try:
        results = solver.solve(it, config)
        assert len(results) > 0
        best = results[0]

        # Expect schedule:
        # Day 1: Start city rest day (Austin -> Austin)
        # Day 2: Austin -> Bastrop (travel day)
        # Day 3: Rest day at Bastrop (Bastrop -> Bastrop)
        # Day 4: Rest day at Bastrop (Bastrop -> Bastrop)
        # Day 5: Bastrop -> Manor (travel day)
        # Day 6: Rest day at Manor (Manor -> Manor)

        sched = best.schedule
        assert len(sched) == 6

        start_date = best.start_date

        # Day 1: Rest Day at Austin
        assert sched[0].date == start_date
        assert sched[0].origin.name == "Austin, Texas"
        assert sched[0].destination.name == "Austin, Texas"
        assert sched[0].is_rest_day is True

        # Day 2: Travel Austin -> Bastrop
        assert sched[1].date == start_date + timedelta(days=1)
        assert sched[1].origin.name == "Austin, Texas"
        assert sched[1].destination.name == "Bastrop, Texas"
        assert sched[1].is_rest_day is False

        # Day 3: Rest Day at Bastrop
        assert sched[2].date == start_date + timedelta(days=2)
        assert sched[2].origin.name == "Bastrop, Texas"
        assert sched[2].destination.name == "Bastrop, Texas"
        assert sched[2].is_rest_day is True

        # Day 4: Rest Day at Bastrop
        assert sched[3].date == start_date + timedelta(days=3)
        assert sched[3].origin.name == "Bastrop, Texas"
        assert sched[3].destination.name == "Bastrop, Texas"
        assert sched[3].is_rest_day is True

        # Day 5: Travel Bastrop -> Manor
        assert sched[4].date == start_date + timedelta(days=4)
        assert sched[4].origin.name == "Bastrop, Texas"
        assert sched[4].destination.name == "Manor, Texas"
        assert sched[4].is_rest_day is False

        # Day 6: Rest Day at Manor
        assert sched[5].date == start_date + timedelta(days=5)
        assert sched[5].origin.name == "Manor, Texas"
        assert sched[5].destination.name == "Manor, Texas"
        assert sched[5].is_rest_day is True

    finally:
        solver.close()
        if os.path.exists(db_path):
            try:
                os.remove(db_path)
            except OSError:
                pass


def test_output_formatting_rest_days():
    c_start = City(name="Austin, Texas", latitude=30.2, longitude=-97.7, rest_days=1)
    c_via = City(name="Bastrop, Texas", latitude=30.1, longitude=-97.3, rest_days=1)
    c_comp = City(name="Manor, Texas", latitude=30.3, longitude=-97.5, rest_days=1)

    legs = [
        Leg(origin=c_start, destination=c_via, distance_miles=30.0, ascent_feet=500.0, surface_breakdown={"paved": 20.0, "gravel": 10.0}),
        Leg(origin=c_via, destination=c_comp, distance_miles=25.0, ascent_feet=300.0, surface_breakdown={"asphalt": 25.0})
    ]

    sched = [
        DailySchedule(day_number=1, date=date(2026, 6, 1), origin=c_start, destination=c_start, distance_miles=0.0, ascent_feet=0.0, high_temp_f=85.0, low_temp_f=65.0, weather_source="mock", is_rest_day=True),
        DailySchedule(day_number=2, date=date(2026, 6, 2), origin=c_start, destination=c_via, distance_miles=30.0, ascent_feet=500.0, high_temp_f=86.0, low_temp_f=66.0, weather_source="mock", is_rest_day=False),
        DailySchedule(day_number=3, date=date(2026, 6, 3), origin=c_via, destination=c_via, distance_miles=0.0, ascent_feet=0.0, high_temp_f=87.0, low_temp_f=67.0, weather_source="mock", is_rest_day=True),
        DailySchedule(day_number=4, date=date(2026, 6, 4), origin=c_via, destination=c_comp, distance_miles=25.0, ascent_feet=300.0, high_temp_f=88.0, low_temp_f=68.0, weather_source="mock", is_rest_day=False),
        DailySchedule(day_number=5, date=date(2026, 6, 5), origin=c_comp, destination=c_comp, distance_miles=0.0, ascent_feet=0.0, high_temp_f=89.0, low_temp_f=69.0, weather_source="mock", is_rest_day=True)
    ]

    itinerary = Itinerary(
        start_city=c_start,
        completion_city=c_comp,
        via_cities=[c_via],
        start_date=date(2026, 6, 1),
        legs=legs,
        schedule=sched,
        is_feasible=True,
        routing_distance_source="mock"
    )

    markdown_table = OutputFormatter.format_schedule_markdown(itinerary)

    # Verify formatting structure and notes
    assert "Rest Day at Austin, Texas" in markdown_table
    assert "Rest Day at Bastrop, Texas" in markdown_table
    assert "Rest Day at Manor, Texas" in markdown_table
    
    # Each rest day should have 0.0 leg distance/miles
    lines = markdown_table.split("\n")
    # Verify rest day row distance and notes columns
    rest_austin_row = [l for l in lines if "Rest Day at Austin, Texas" in l]
    assert len(rest_austin_row) == 1
    assert "| 0.0 |" in rest_austin_row[0]

    rest_bastrop_row = [l for l in lines if "Rest Day at Bastrop, Texas" in l]
    assert len(rest_bastrop_row) == 1
    assert "| 0.0 |" in rest_bastrop_row[0]


def test_markdown_to_aligned_text_stripping():
    md = """
# Details Title
<details>
<summary>View Details of Route</summary>
This is the details content.
</details>
Some other markdown text.
"""
    txt = OutputFormatter.markdown_to_aligned_text(md)
    assert "<details>" not in txt
    assert "</details>" not in txt
    assert "=== View Details of Route ===" in txt
    assert "This is the details content." in txt


def test_format_summary_markdown_paved_gravel_breakdown():
    c_start = City(name="A", latitude=30.0, longitude=-90.0)
    c_comp = City(name="B", latitude=31.0, longitude=-91.0)
    legs = [
        Leg(
            origin=c_start,
            destination=c_comp,
            distance_miles=55.0,
            ascent_feet=400.0,
            surface_breakdown={"paved": 40.0, "gravel": 15.0}
        )
    ]
    itinerary = Itinerary(
        start_city=c_start,
        completion_city=c_comp,
        via_cities=[],
        legs=legs,
        is_feasible=True
    )
    summary_md = OutputFormatter.format_summary_markdown(itinerary)
    
    # Should display: Total Distance: 55.0 miles (40.0 mi paved, 15.0 mi gravel)
    assert "55.0 miles (40.0 mi paved, 15.0 mi gravel)" in summary_md
