import json
from datetime import date
from src.domain import City, Leg, Itinerary, DailySchedule
from src.graphhopper_routing import GraphHopperRoutingProvider
from src.cache import SQLiteCacheManager, compute_profile_hash
from src.output import OutputFormatter


def test_graphhopper_query_params_custom_model():
    provider = GraphHopperRoutingProvider(base_url="http://localhost:8989", profile="bike")
    origin = City(name="Austin", latitude=30.2672, longitude=-97.7431)
    destination = City(name="Dallas", latitude=32.7767, longitude=-96.7970)

    # Test 1: avoid_gravel is False
    body_false = provider._build_post_body(origin, destination, preferences={"avoid_gravel": False})
    assert "custom_model" not in body_false
    assert "ch.disable" not in body_false
    assert body_false["details"] == ["road_class", "surface", "track_type"]

    # Test 2: avoid_gravel is True
    body_true = provider._build_post_body(origin, destination, preferences={"avoid_gravel": True})
    assert "custom_model" in body_true
    assert body_true["ch.disable"] is True
    assert "multiply_by" in json.dumps(body_true["custom_model"])


def test_graphhopper_distance_attribution_and_breakdowns():
    provider = GraphHopperRoutingProvider(base_url="http://localhost:8989", profile="bike")

    # Mock response payload
    # Austin coordinates (roughly 0.1 deg apart is ~6.9 miles)
    mock_payload = {
        "paths": [
            {
                "distance": 11100.0,
                "ascend": 100.0,
                "points": {
                    "coordinates": [
                        [-97.7431, 30.2672],    # P0
                        [-97.7431, 30.3172],    # P1 (~3.45 miles from P0)
                        [-97.7431, 30.3672],    # P2 (~3.45 miles from P1)
                    ]
                },
                "details": {
                    "road_class": [
                        [0, 1, "primary"],
                        [1, 2, "track"]
                    ],
                    "surface": [
                        [0, 1, "asphalt"],
                        [1, 2, "gravel"]
                    ],
                    "track_type": [
                        [1, 2, "grade2"]
                    ]
                }
            }
        ]
    }

    # Monkeypatch _route_request to return our mock payload
    def mock_route_request(origin, destination, preferences, include_elevation=True):
        return mock_payload

    provider._route_request = mock_route_request

    origin = City(name="Austin", latitude=30.2672, longitude=-97.7431)
    destination = City(name="Destination", latitude=30.3672, longitude=-97.7431)

    leg = provider.get_leg_metrics(origin, destination, preferences={})

    # The coordinates distance calculation should produce roughly ~3.45 miles per segment
    # Let's verify breakdowns are populated
    assert "primary" in leg.road_class_breakdown
    assert "track" in leg.road_class_breakdown
    assert "asphalt" in leg.surface_breakdown
    assert "gravel" in leg.surface_breakdown
    # grade2 is track type, but since surface is gravel, it should use surface ("gravel")
    # Let's make sure it doesn't double-count
    total_surf_miles = sum(leg.surface_breakdown.values())
    assert abs(total_surf_miles - leg.distance_miles) < 0.1


def test_cache_serialization_and_migration(tmp_path):
    db_file = str(tmp_path / "test_cache.db")
    cache = SQLiteCacheManager(db_file)

    origin = City(name="Austin", latitude=30.2672, longitude=-97.7431)
    destination = City(name="Dallas", latitude=32.7767, longitude=-96.7970)

    # Save a leg with breakdowns
    leg = Leg(
        origin=origin,
        destination=destination,
        distance_miles=195.0,
        ascent_feet=250.0,
        road_class_breakdown={"primary": 100.0, "secondary": 95.0},
        surface_breakdown={"asphalt": 150.0, "gravel": 45.0}
    )

    prefs = {"avoid_gravel": True}
    cache.save_leg(leg, "graphhopper:test", prefs, source="test_source")

    # Read the leg back
    loaded_leg = cache.get_leg(origin, destination, "graphhopper:test", prefs, source="test_source")
    assert loaded_leg is not None
    assert loaded_leg.distance_miles == 195.0
    assert loaded_leg.road_class_breakdown == {"primary": 100.0, "secondary": 95.0}
    assert loaded_leg.surface_breakdown == {"asphalt": 150.0, "gravel": 45.0}

    # Verify cache isolation works (profile hash changes with avoid_gravel)
    different_prefs = {"avoid_gravel": False}
    assert compute_profile_hash(prefs) != compute_profile_hash(different_prefs)
    assert cache.get_leg(origin, destination, "graphhopper:test", different_prefs, source="test_source") is None

    cache.close()


def test_output_formatter_with_surface_breakdown():
    city_a = City(name="Austin", latitude=30.2672, longitude=-97.7431)
    city_b = City(name="Dallas", latitude=32.7767, longitude=-96.7970)

    leg = Leg(
        origin=city_a,
        destination=city_b,
        distance_miles=195.0,
        ascent_feet=250.0,
        road_class_breakdown={"primary": 100.0, "track": 95.0},
        surface_breakdown={"asphalt": 100.0, "gravel": 95.0}
    )

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
    )

    md_sched = OutputFormatter.format_schedule_markdown(itinerary)
    # Total distance is 195.0, paved is 100.0, gravel is 95.0. 
    # With scaling and rounding, it should format as: 195.0 mi (100.0 mi paved, 95.0 mi gravel)
    assert "195.0 mi (100.0 mi paved, 95.0 mi gravel)" in md_sched
