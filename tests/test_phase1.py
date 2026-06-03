import os
import pytest
from datetime import date
from src.validation import RequestParser, ValidationError, CITY_REGISTRY
from src.domain import Itinerary

def test_positive_fixtures_loading():
    parser = RequestParser(system_defaults_path="config/defaults.yaml")
    
    # 1. Load US Capitals fixed date example
    itinerary_fixed, config_fixed = parser.parse_request_file("examples/eastern-capitals-fixed-date-february.yaml")
    assert itinerary_fixed.start_city.name == "Austin, Texas"
    assert itinerary_fixed.completion_city.name == "Washington, DC"
    assert itinerary_fixed.start_date == date(2027, 2, 1)
    assert len(itinerary_fixed.via_cities) == 16
    assert config_fixed["weather_constraints"]["max_avg_high_f"] == 90.0
    
    # 2. Load US Capitals optimize date example
    itinerary_opt, config_opt = parser.parse_request_file("examples/eastern-capitals-optimize-date.yaml")
    assert itinerary_opt.start_city.name == "Austin, Texas"
    assert itinerary_opt.start_date is None
    assert len(itinerary_opt.via_cities) == 16
    
    # 3. Load Gone2Look4America benchmark example
    itinerary_g2l, config_g2l = parser.parse_request_file("examples/gone2look4america.yaml")
    assert itinerary_g2l.start_city.name == "Washington, DC"
    assert itinerary_g2l.completion_city.name == "Olympia, Washington"
    assert itinerary_g2l.start_date == date(2023, 4, 29)
    assert len(itinerary_g2l.via_cities) == 25


def test_missing_required_fields():
    parser = RequestParser()
    
    # Missing start city
    payload_no_start = {
        "completion_city": "Washington, DC"
    }
    with pytest.raises(ValidationError, match="A starting city must be specified") as exc_info:
        parser.parse_request_dict(payload_no_start)
    assert exc_info.value.code == "MISSING_START_CITY"
    
    # Missing completion city
    payload_no_comp = {
        "start_city": "Austin, Texas"
    }
    with pytest.raises(ValidationError, match="A completion city must be specified") as exc_info:
        parser.parse_request_dict(payload_no_comp)
    assert exc_info.value.code == "MISSING_COMPLETION_CITY"


def test_invalid_cities_resolution(tmp_path, monkeypatch):
    import io
    def mock_urlopen(req, timeout=None):
        return io.BytesIO(b"[]")
    monkeypatch.setattr("urllib.request.urlopen", mock_urlopen)

    parser = RequestParser()
    
    payload_bad_city = {
        "start_city": "Atlantis",
        "completion_city": "Washington, DC",
        "cache": {
            "db_path": str(tmp_path / "test_invalid_cities_resolution.db")
        }
    }
    with pytest.raises(ValidationError, match="City 'Atlantis' is not in the recognized geocoding registry") as exc_info:
        parser.parse_request_dict(payload_bad_city)
    assert exc_info.value.code == "INVALID_CITY"
    assert exc_info.value.location == "Atlantis"
    
    payload_bad_via = {
        "start_city": "Austin, Texas",
        "completion_city": "Washington, DC",
        "via_cities": "Not A List"
    }
    with pytest.raises(ValidationError, match="via_cities must be a list of city name strings") as exc_info:
        parser.parse_request_dict(payload_bad_via)
    assert exc_info.value.code == "INVALID_VIA_CITIES"


def test_date_validations():
    parser = RequestParser()
    
    # Invalid string format
    payload_bad_date = {
        "start_city": "Austin, Texas",
        "completion_city": "Washington, DC",
        "start_date": "02/01/2026"
    }
    with pytest.raises(ValidationError, match="Start date '02/01/2026' must be in YYYY-MM-DD format") as exc_info:
        parser.parse_request_dict(payload_bad_date)
    assert exc_info.value.code == "INVALID_DATE"
    
    # Invalid type
    payload_bad_type = {
        "start_city": "Austin, Texas",
        "completion_city": "Washington, DC",
        "start_date": 12345
    }
    with pytest.raises(ValidationError, match="Start date must be a YYYY-MM-DD date or string") as exc_info:
        parser.parse_request_dict(payload_bad_type)
    assert exc_info.value.code == "INVALID_DATE"


def test_solver_limits_validation():
    parser = RequestParser()
    
    # Default city cap is 50. Let's pass 50 via cities (making total 52 cities)
    payload_too_many = {
        "start_city": "Austin, Texas",
        "completion_city": "Washington, DC",
        "via_cities": ["Austin, Texas"] * 49, # 49 via + 2 = 51 cities
        "solver_constraints": {
            "max_total_cities": 50
        }
    }
    with pytest.raises(ValidationError, match="exceeds the solver limit of 50") as exc_info:
        parser.parse_request_dict(payload_too_many)
    assert exc_info.value.code == "CITY_COUNT_EXCEEDED"


def test_scoring_weights_validation():
    parser = RequestParser()
    
    # Sum to 1 violation
    payload_bad_weights = {
        "start_city": "Austin, Texas",
        "completion_city": "Washington, DC",
        "scoring": {
            "weights": {
                "weather": 0.5,
                "distance": 0.5,
                "hills": 0.5
            }
        }
    }
    with pytest.raises(ValidationError, match="Scoring weights are invalid: Weights must sum to 1.0") as exc_info:
        parser.parse_request_dict(payload_bad_weights)
    assert exc_info.value.code == "INVALID_SCORING_WEIGHTS"
    assert exc_info.value.location == "scoring.weights"


def test_weather_range_validation():
    parser = RequestParser()
    
    payload_bad_range = {
        "start_city": "Austin, Texas",
        "completion_city": "Washington, DC",
        "weather_constraints": {
            "max_avg_high_f": 40.0,
            "min_avg_low_f": 60.0
        }
    }
    with pytest.raises(ValidationError, match="max_avg_high_f \\(40.0\\) cannot be less than min_avg_low_f \\(60.0\\)") as exc_info:
        parser.parse_request_dict(payload_bad_range)
    assert exc_info.value.code == "INVALID_WEATHER_RANGE"


def test_daily_limit_validation():
    parser = RequestParser()
    
    payload_bad_miles = {
        "start_city": "Austin, Texas",
        "completion_city": "Washington, DC",
        "daily_constraints": {
            "max_miles_per_day": -10.0
        }
    }
    with pytest.raises(ValidationError, match="Daily limits must be positive") as exc_info:
        parser.parse_request_dict(payload_bad_miles)
    assert exc_info.value.code == "INVALID_DAILY_LIMIT"


def test_yaml_files_not_found():
    parser = RequestParser()
    
    with pytest.raises(ValidationError, match="Request YAML file not found") as exc_info:
        parser.parse_request_file("nonexistent.yaml")
    assert exc_info.value.code == "FILE_NOT_FOUND"


def test_yaml_parse_error():
    parser = RequestParser()
    
    bad_yaml_path = "tests/corrupt.yaml"
    with open(bad_yaml_path, "w") as f:
        f.write("start_city: [unclosed list")
        
    try:
        with pytest.raises(ValidationError, match="Failed to parse request YAML") as exc_info:
            parser.parse_request_file(bad_yaml_path)
        assert exc_info.value.code == "YAML_PARSE_ERROR"
    finally:
        if os.path.exists(bad_yaml_path):
            os.remove(bad_yaml_path)


def test_empty_yaml_error():
    parser = RequestParser()
    
    empty_yaml_path = "tests/empty.yaml"
    with open(empty_yaml_path, "w") as f:
        f.write("")
        
    try:
        with pytest.raises(ValidationError, match="Request YAML file is empty") as exc_info:
            parser.parse_request_file(empty_yaml_path)
        assert exc_info.value.code == "EMPTY_REQUEST"
    finally:
        if os.path.exists(empty_yaml_path):
            os.remove(empty_yaml_path)


def test_validation_error_to_dict():
    err = ValidationError(code="TEST_CODE", message="test message", location="test_loc")
    d = err.to_dict()
    assert d["code"] == "TEST_CODE"
    assert d["message"] == "test message"
    assert d["location"] == "test_loc"


def test_dynamic_geocoding_success(tmp_path, monkeypatch):
    import io
    import json
    from src.cache import SQLiteCacheManager

    db_file = tmp_path / "test_geocoding.db"
    payload = {
        "start_city": "Elgin, Texas",
        "completion_city": "Austin, Texas",
        "cache": {
            "db_path": str(db_file)
        }
    }

    calls = []

    def mock_urlopen(req, timeout=None):
        url = req.full_url if hasattr(req, "full_url") else req
        calls.append(url)
        if "nominatim" in url:
            res_content = json.dumps([
                {
                    "lat": "30.3495084",
                    "lon": "-97.3711180",
                    "display_name": "Elgin, Bastrop County, Texas, United States"
                }
            ])
            return io.BytesIO(res_content.encode("utf-8"))
        raise RuntimeError("Unexpected URL")

    monkeypatch.setattr("urllib.request.urlopen", mock_urlopen)

    parser = RequestParser()
    itinerary, config = parser.parse_request_dict(payload)

    assert itinerary.start_city.name == "Elgin, Bastrop County, Texas, United States"
    assert itinerary.start_city.latitude == 30.3495084
    assert itinerary.start_city.longitude == -97.3711180
    assert len(calls) == 1

    cache_mgr = SQLiteCacheManager(str(db_file))
    cached = cache_mgr.get_geocoding("elgin, texas")
    assert cached is not None
    assert cached[0] == 30.3495084
    assert cached[1] == -97.3711180
    assert cached[2] == "Elgin, Bastrop County, Texas, United States"
    cache_mgr.close()

