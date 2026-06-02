import json
from typing import Dict, Any
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import urlopen

from src.domain import City, Leg
from src.providers import RoutingProvider


class GraphHopperRoutingProvider(RoutingProvider):
    """Routing provider backed by a local or remote GraphHopper route API."""

    def __init__(
        self,
        base_url: str = "http://localhost:8989",
        profile: str = "bike",
        timeout_seconds: float = 12.0,
    ):
        self.base_url = base_url.rstrip("/")
        self.profile = profile
        self.timeout_seconds = timeout_seconds

    def _build_query_params(self, origin: City, destination: City, include_elevation: bool = True) -> str:
        params = [
            ("profile", self.profile),
            ("points_encoded", "false"),
            ("calc_points", "true"),
            ("instructions", "false"),
            ("point", f"{origin.latitude},{origin.longitude}"),
            ("point", f"{destination.latitude},{destination.longitude}"),
        ]
        if include_elevation:
            params.append(("elevation", "true"))
        return urlencode(params)

    def _route_request(self, origin: City, destination: City, include_elevation: bool = True) -> Dict[str, Any]:
        query = self._build_query_params(origin, destination, include_elevation=include_elevation)
        url = f"{self.base_url}/route?{query}"
        try:
            with urlopen(url, timeout=self.timeout_seconds) as response:
                payload = response.read().decode("utf-8")
        except HTTPError as exc:
            error_payload = exc.read().decode("utf-8", errors="replace")
            if include_elevation and exc.code == 400 and "Elevation not supported" in error_payload:
                return self._route_request(origin, destination, include_elevation=False)
            raise RuntimeError(
                f"GraphHopper HTTP {exc.code} for {origin.name} -> {destination.name}: {error_payload}"
            ) from exc
        return json.loads(payload)

    def get_leg_metrics(self, origin: City, destination: City, preferences: Dict[str, Any]) -> Leg:
        del preferences  # GraphHopper profile settings control route behavior in this provider.

        payload = self._route_request(origin, destination)
        paths = payload.get("paths", [])
        if not paths:
            hints = payload.get("hints") or payload.get("message") or "unknown routing error"
            raise RuntimeError(f"GraphHopper route request failed: {hints}")

        path = paths[0]
        distance_meters = float(path.get("distance", 0.0))
        ascend_meters = float(path.get("ascend", 0.0))

        return Leg(
            origin=origin,
            destination=destination,
            distance_miles=distance_meters / 1609.344,
            ascent_feet=ascend_meters * 3.28084,
            is_bicycle_legal=True,
            avoided_highways=True,
            avoided_tolls=True,
            allowed_ferries=True,
            allowed_borders=True,
        )
