import json
import math
from typing import Dict, Any
from urllib.error import HTTPError
from urllib.request import urlopen, Request

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

    def _haversine_miles(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """Calculates the great-circle distance in miles between two coordinates."""
        R = 3958.8  # Earth radius in miles
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)

        dlat = lat2_rad - lat1_rad
        dlon = lon2_rad - lon1_rad

        a = math.sin(dlat / 2.0)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2.0)**2
        c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
        return R * c

    def _build_post_body(self, origin: City, destination: City, preferences: Dict[str, Any], include_elevation: bool = True) -> Dict[str, Any]:
        body = {
            "points": [
                [origin.longitude, origin.latitude],
                [destination.longitude, destination.latitude]
            ],
            "profile": self.profile,
            "points_encoded": False,
            "calc_points": True,
            "instructions": False,
            "details": ["road_class", "surface", "track_type"],
        }
        if include_elevation:
            body["elevation"] = True
        else:
            body["elevation"] = False

        if preferences.get("avoid_gravel", False):
            body["ch.disable"] = True
            body["custom_model"] = {
                "priority": [
                    {
                        "if": "surface == GRAVEL || surface == UNPAVED || surface == DIRT || surface == SAND || track_type == GRADE2 || track_type == GRADE3 || track_type == GRADE4 || track_type == GRADE5",
                        "multiply_by": 0.1
                    }
                ]
            }

        return body

    def _route_request(self, origin: City, destination: City, preferences: Dict[str, Any], include_elevation: bool = True) -> Dict[str, Any]:
        body = self._build_post_body(origin, destination, preferences, include_elevation=include_elevation)
        url = f"{self.base_url}/route"
        req = Request(
            url,
            data=json.dumps(body).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        try:
            with urlopen(req, timeout=self.timeout_seconds) as response:
                payload = response.read().decode("utf-8")
        except HTTPError as exc:
            error_payload = exc.read().decode("utf-8", errors="replace")
            if include_elevation and exc.code == 400 and "Elevation not supported" in error_payload:
                return self._route_request(origin, destination, preferences, include_elevation=False)
            raise RuntimeError(
                f"GraphHopper HTTP {exc.code} for {origin.name} -> {destination.name}: {error_payload}"
            ) from exc
        return json.loads(payload)

    def _build_geodesic_fallback_leg(self, origin: City, destination: City, preferences: Dict[str, Any]) -> Leg:
        distance_miles = max(1.0, self._haversine_miles(origin.latitude, origin.longitude, destination.latitude, destination.longitude))
        return Leg(
            origin=origin,
            destination=destination,
            distance_miles=distance_miles,
            ascent_feet=0.0,
            is_bicycle_legal=True,
            avoided_highways=preferences.get("avoid_highways", True),
            avoided_tolls=preferences.get("avoid_tolls", True),
            allowed_ferries=preferences.get("allow_ferries", True),
            allowed_borders=preferences.get("allow_international_borders", True),
            road_class_breakdown={},
            surface_breakdown={},
            geometry=[(origin.latitude, origin.longitude), (destination.latitude, destination.longitude)],
        )

    def get_leg_metrics(self, origin: City, destination: City, preferences: Dict[str, Any]) -> Leg:
        try:
            payload = self._route_request(origin, destination, preferences)
        except RuntimeError as exc:
            err = str(exc)
            if "PointDistanceExceededException" in err or "too far from" in err:
                return self._build_geodesic_fallback_leg(origin, destination, preferences)
            raise
        except TimeoutError as exc:
            # Fallback for long cross-country bike routes where custom-model expansion can time out.
            if preferences.get("avoid_gravel", False):
                fallback_preferences = dict(preferences)
                fallback_preferences["avoid_gravel"] = False
                try:
                    payload = self._route_request(origin, destination, fallback_preferences)
                except TimeoutError as retry_exc:
                    raise RuntimeError(
                        f"GraphHopper timed out for {origin.name} -> {destination.name} "
                        f"(profile={self.profile}, timeout={self.timeout_seconds}s, "
                        "including fallback without avoid_gravel)"
                    ) from retry_exc
            else:
                raise RuntimeError(
                    f"GraphHopper timed out for {origin.name} -> {destination.name} "
                    f"(profile={self.profile}, timeout={self.timeout_seconds}s)"
                ) from exc
        paths = payload.get("paths", [])
        if not paths:
            hints = payload.get("hints") or payload.get("message") or "unknown routing error"
            raise RuntimeError(f"GraphHopper route request failed: {hints}")

        path = paths[0]
        distance_meters = float(path.get("distance", 0.0))
        ascend_meters = float(path.get("ascend", 0.0))

        coordinates = path.get("points", {}).get("coordinates", [])
        details = path.get("details", {})

        road_class_breakdown = {}
        surface_breakdown = {}

        num_segments = len(coordinates) - 1
        if num_segments > 0:
            segment_road_classes = [None] * num_segments
            segment_surfaces = [None] * num_segments
            segment_track_types = [None] * num_segments

            for start, end, val in details.get("road_class", []):
                for idx in range(start, end):
                    if idx < num_segments:
                        segment_road_classes[idx] = val

            for start, end, val in details.get("surface", []):
                for idx in range(start, end):
                    if idx < num_segments:
                        segment_surfaces[idx] = val

            for start, end, val in details.get("track_type", []):
                for idx in range(start, end):
                    if idx < num_segments:
                        segment_track_types[idx] = val

            for idx in range(num_segments):
                p1 = coordinates[idx]
                p2 = coordinates[idx + 1]
                dist = self._haversine_miles(p1[1], p1[0], p2[1], p2[0])

                rc = segment_road_classes[idx] or "missing"
                road_class_breakdown[rc] = road_class_breakdown.get(rc, 0.0) + dist

                surf = segment_surfaces[idx]
                tr = segment_track_types[idx]
                if (not surf or surf.lower() == "missing") and tr and tr.lower() != "missing":
                    surf_val = tr
                else:
                    surf_val = surf or "missing"
                surface_breakdown[surf_val] = surface_breakdown.get(surf_val, 0.0) + dist

        geom = [(float(pt[1]), float(pt[0])) for pt in coordinates if len(pt) >= 2]

        return Leg(
            origin=origin,
            destination=destination,
            distance_miles=distance_meters / 1609.344,
            ascent_feet=ascend_meters * 3.28084,
            is_bicycle_legal=True,
            avoided_highways=preferences.get("avoid_highways", True),
            avoided_tolls=preferences.get("avoid_tolls", True),
            allowed_ferries=preferences.get("allow_ferries", True),
            allowed_borders=preferences.get("allow_international_borders", True),
            road_class_breakdown=road_class_breakdown,
            surface_breakdown=surface_breakdown,
            geometry=geom,
        )

