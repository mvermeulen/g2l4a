import json
from datetime import date
from pathlib import Path
from typing import Dict, Optional

from src.domain import City
from src.mocks import MockWeatherProvider
from src.providers import WeatherProvider, WeatherMetrics


class StateCapitalMonthlyNormalsWeatherProvider(WeatherProvider):
    """Monthly temperature normals provider for US state capitals.

    Uses a locally stored dataset generated from public monthly climate normals
    tables (for example, Wikipedia city climate tables). This provider is
    designed as a robust fallback when live weather APIs are unavailable.
    """

    DEFAULT_DATASET_PATH = "data/state_capitals_monthly_normals.json"

    def __init__(
        self,
        dataset_path: str = DEFAULT_DATASET_PATH,
        fallback_provider: Optional[WeatherProvider] = None,
    ):
        self.dataset_path = dataset_path
        self.fallback_provider = fallback_provider or MockWeatherProvider()
        self._monthly_by_alias = self._load_monthly_normals(dataset_path)

    @staticmethod
    def _normalize_city_name(name: str) -> str:
        return " ".join(name.strip().lower().replace("_", " ").split())

    @staticmethod
    def _is_forecast_window(travel_date: date, current_time: Optional[date]) -> bool:
        if current_time is None:
            return False
        days_diff = (travel_date - current_time).days
        return 0 <= days_diff <= 14

    def _load_monthly_normals(self, dataset_path: str) -> Dict[str, Dict[int, Dict[str, float]]]:
        path = Path(dataset_path)
        if not path.exists():
            return {}

        payload = json.loads(path.read_text(encoding="utf-8"))
        cities = payload.get("cities", {})

        indexed: Dict[str, Dict[int, Dict[str, float]]] = {}
        for city_name, city_payload in cities.items():
            monthly_raw = city_payload.get("monthly", {})
            monthly_index: Dict[int, Dict[str, float]] = {}
            for month_str, temps in monthly_raw.items():
                month = int(month_str)
                monthly_index[month] = {
                    "high_temp_f": float(temps["high_temp_f"]),
                    "low_temp_f": float(temps["low_temp_f"]),
                }

            aliases = [city_name] + list(city_payload.get("aliases", []))
            for alias in aliases:
                indexed[self._normalize_city_name(alias)] = monthly_index

        return indexed

    def get_weather_metrics(self, city: City, travel_date: date, current_time: Optional[date] = None) -> WeatherMetrics:
        is_forecast = self._is_forecast_window(travel_date, current_time)
        city_key = self._normalize_city_name(city.name)

        monthly = self._monthly_by_alias.get(city_key)
        if monthly:
            temps = monthly.get(travel_date.month)
            if temps:
                return {
                    "high_temp_f": temps["high_temp_f"],
                    "low_temp_f": temps["low_temp_f"],
                    "is_forecast": False,
                    "source": "wikipedia",
                }

        # Fallback to closest state capital
        import math
        from src.validation import CITY_REGISTRY

        def cap_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
            R = 3958.8  # Earth radius in miles
            phi1 = math.radians(lat1)
            phi2 = math.radians(lat2)
            dphi = math.radians(lat2 - lat1)
            dlambda = math.radians(lon2 - lon1)
            a = math.sin(dphi / 2.0)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2.0)**2
            c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
            return R * c

        closest_capital = None
        min_dist = float("inf")
        for cap_key, coords in CITY_REGISTRY.items():
            if cap_key in self._monthly_by_alias:
                dist = cap_distance(city.latitude, city.longitude, coords[0], coords[1])
                if dist < min_dist:
                    min_dist = dist
                    closest_capital = cap_key

        if closest_capital:
            monthly = self._monthly_by_alias[closest_capital]
            temps = monthly.get(travel_date.month)
            if temps:
                return {
                    "high_temp_f": temps["high_temp_f"],
                    "low_temp_f": temps["low_temp_f"],
                    "is_forecast": False,
                    "source": "wikipedia",
                }

        return self.fallback_provider.get_weather_metrics(
            city, travel_date, current_time
        )
