import json
import xml.etree.ElementTree as ET
from pathlib import Path
from types import SimpleNamespace

import pytest

from src.cache import SQLiteCacheManager
from src.domain import City, Leg, Itinerary
from src.example_report import (
    _downsample_coordinates,
    _fetch_itinerary_lodging,
    _maybe_generate_gpx,
)


def test_downsample_coordinates_preserves_endpoints():
    coords = [(0.0, 0.0), (0.01, 0.0), (0.02, 0.0), (0.03, 0.0)]
    # 0.01 degrees is ~1.1 km. Total path is ~3.3 km.
    # At 3.0km downsample target, it should keep the first and last point
    sampled = _downsample_coordinates(coords, target_distance_km=3.0)
    assert len(sampled) >= 2
    assert sampled[0] == coords[0]
    assert sampled[-1] == coords[-1]


def test_fetch_itinerary_lodging_mock_and_cache(tmp_path):
    cache_path = tmp_path / "test_lodging.db"
    coords = [(30.0, -90.0), (30.05, -90.05)]

    # Fetch in mock mode
    hotels = _fetch_itinerary_lodging(
        coords=coords,
        radius_meters=800,
        types=["hotel"],
        cache_db_path=str(cache_path),
        is_mock=True,
    )

    assert len(hotels) == 2
    assert "Mock Cozy Inn" in hotels[0]["name"]
    assert "Mock Route Motel" in hotels[1]["name"]

    # Verify L2 Cache hit by verifying table entry exists
    import hashlib
    import json
    rounded_coords = [(round(lat, 5), round(lon, 5)) for lat, lon in coords]
    coord_str = json.dumps(rounded_coords)
    types_str = ",".join(sorted(["hotel"]))
    hash_input = f"{coord_str}|800|{types_str}"
    route_hash = hashlib.sha256(hash_input.encode('utf-8')).hexdigest()

    cache_mgr = SQLiteCacheManager(str(cache_path))
    try:
        cached = cache_mgr.get_itinerary_lodging(route_hash)
        assert cached is not None
        assert len(cached) == 2
        assert cached[0]["name"] == hotels[0]["name"]
    finally:
        cache_mgr.close()


def test_fetch_itinerary_lodging_api_overpass(tmp_path, monkeypatch):
    cache_path = tmp_path / "test_lodging_api.db"
    coords = [(30.0, -90.0), (30.05, -90.05)]

    # Mock Overpass response
    class FakeResponse:
        def read(self):
            return json.dumps({
                "elements": [
                    {
                        "type": "node",
                        "lat": 30.01,
                        "lon": -90.01,
                        "tags": {"name": "Overpass Hotel"},
                    }
                ]
            }).encode("utf-8")

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            pass

    def mock_urlopen(*args, **kwargs):
        return FakeResponse()

    import urllib.request
    monkeypatch.setattr(urllib.request, "urlopen", mock_urlopen)

    hotels = _fetch_itinerary_lodging(
        coords=coords,
        radius_meters=800,
        types=["hotel"],
        cache_db_path=str(cache_path),
        is_mock=False,
    )

    assert len(hotels) == 1
    assert hotels[0]["name"] == "Overpass Hotel"
    assert hotels[0]["lat"] == 30.01
    assert hotels[0]["lon"] == -90.01


def test_maybe_generate_gpx_injects_waypoints(tmp_path, monkeypatch):
    # Dummy GPX template
    gpx_xml = """<?xml version="1.0" encoding="UTF-8"?>
<gpx version="1.1" creator="GraphHopper" xmlns="http://www.topografix.com/GPX/1/1">
  <metadata>
    <name>Route</name>
  </metadata>
  <trk>
    <name>Track</name>
    <trkseg>
      <trkpt lat="30.0" lon="-90.0"/>
      <trkpt lat="30.05" lon="-90.05"/>
    </trkseg>
  </trk>
</gpx>"""

    # Mock fetching GPX payload from GraphHopper
    monkeypatch.setattr("src.example_report._fetch_gpx_payload", lambda *args, **kwargs: gpx_xml.encode("utf-8"))
    # Mock lodging retrieval
    monkeypatch.setattr("src.example_report._fetch_itinerary_lodging", lambda *args, **kwargs: [
        {"name": "Mock Cozy Inn near Start", "lat": 30.001, "lon": -90.001},
        {"name": "Mock Route Motel near End", "lat": 30.049, "lon": -90.049},
    ])

    origin = City(name="Start", latitude=30.0, longitude=-90.0)
    dest = City(name="End", latitude=30.05, longitude=-90.05)
    leg = Leg(
        origin=origin,
        destination=dest,
        distance_miles=5.0,
        ascent_feet=10.0,
        geometry=[(30.0, -90.0), (30.05, -90.05)],
    )

    itinerary = Itinerary(
        start_city=origin,
        completion_city=dest,
        via_cities=[],
        legs=[leg],
    )

    config = {
        "output": {
            "gpx": True,
            "gpx_timeout_seconds": 10.0,
            "lodging_overlay": {
                "enabled": True,
                "radius_meters": 800,
                "types": ["hotel"],
            },
        },
        "routing_provider": {
            "name": "graphhopper",
            "profile": "bike",
            "base_url": "http://localhost:8989",
            "timeout_seconds": 5.0,
        },
    }

    cache_db = tmp_path / "gpx_test.db"

    out_gpx = _maybe_generate_gpx(
        example_path=Path("examples/test-route.yaml"),
        config=config,
        itinerary=itinerary,
        cache_db_path=str(cache_db),
    )

    assert out_gpx is not None
    assert out_gpx.exists()

    # Parse output GPX XML
    tree = ET.parse(out_gpx)
    root = tree.getroot()

    # Verify that <wpt> nodes exist and are located before <trk> nodes
    namespaces = {"": "http://www.topografix.com/GPX/1/1"}
    wpts = root.findall("wpt", namespaces)
    trks = root.findall("trk", namespaces)

    assert len(wpts) == 2
    assert wpts[0].find("name", namespaces).text == f"Mock Cozy Inn near {origin.name}"
    assert wpts[1].find("name", namespaces).text == f"Mock Route Motel near {dest.name}"

    # Verify GPX schema-compliant order: wpt nodes come before trk nodes in children list
    children_tags = [child.tag.split("}")[-1] for child in root]
    first_wpt_idx = children_tags.index("wpt")
    first_trk_idx = children_tags.index("trk")
    assert first_wpt_idx < first_trk_idx
