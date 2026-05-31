import json
from urllib.error import HTTPError
from urllib.error import URLError
from urllib.request import urlopen

import pytest

from src.cache import SQLiteCacheManager
from src.cached_providers import CachedRoutingProvider
from src.domain import City
from src.graphhopper_routing import GraphHopperRoutingProvider


def _graphhopper_info(base_url: str):
    try:
        with urlopen(f"{base_url.rstrip('/')}/info", timeout=2.0) as response:
            if response.status != 200:
                return None
            return json.loads(response.read().decode("utf-8"))
    except (URLError, TimeoutError, ValueError, ConnectionResetError, OSError):
        return None


@pytest.mark.integration
def test_graphhopper_provider_roundtrip_when_local_endpoint_available(tmp_path):
    base_url = "http://localhost:8989"
    info = _graphhopper_info(base_url)
    if info is None:
        pytest.skip("Local GraphHopper endpoint is not available at http://localhost:8989")

    bbox = info.get("bbox")
    if not isinstance(bbox, list) or len(bbox) != 4:
        pytest.skip("GraphHopper /info did not include a usable bbox")

    min_lon, min_lat, max_lon, max_lat = [float(v) for v in bbox]

    # Prefer a known routable pair inside Austin for the default Texas map extract.
    austin_origin = (30.2672, -97.7431)
    austin_destination = (30.2720, -97.7150)

    if min_lat <= austin_origin[0] <= max_lat and min_lon <= austin_origin[1] <= max_lon:
        origin_lat, origin_lon = austin_origin
        dest_lat, dest_lon = austin_destination
    else:
        # Fallback for non-Texas extracts: use two nearby points from the bbox interior.
        lat_span = max(max_lat - min_lat, 1e-4)
        lon_span = max(max_lon - min_lon, 1e-4)
        origin_lat = min_lat + (0.45 * lat_span)
        origin_lon = min_lon + (0.45 * lon_span)
        dest_lat = min_lat + (0.55 * lat_span)
        dest_lon = min_lon + (0.55 * lon_span)

    provider = GraphHopperRoutingProvider(base_url=base_url, profile="car", timeout_seconds=8.0)
    cache = SQLiteCacheManager(str(tmp_path / "graphhopper_integration_cache.db"))
    cached_provider = CachedRoutingProvider(
        provider,
        cache,
        routing_engine="graphhopper:test",
        source="graphhopper",
    )

    origin = City(name="Integration Origin", latitude=origin_lat, longitude=origin_lon)
    destination = City(name="Integration Destination", latitude=dest_lat, longitude=dest_lon)

    prefs = {
        "avoid_highways": True,
        "avoid_tolls": True,
        "allow_ferries": True,
        "allow_international_borders": True,
    }

    try:
        first = cached_provider.get_leg_metrics(origin, destination, prefs)
    except HTTPError as exc:
        if exc.code == 400:
            pytest.skip("GraphHopper route request returned HTTP 400 for selected integration points")
        raise
    second = cached_provider.get_leg_metrics(origin, destination, prefs)

    assert first.distance_miles > 0.0
    assert first.ascent_feet >= 0.0
    assert second.distance_miles == first.distance_miles
    assert second.ascent_feet == first.ascent_feet

    cache.close()
