import json
from datetime import date
from typing import Dict, Optional, Tuple, Any
from urllib.parse import urlencode
from urllib.request import urlopen

from src.domain import City
from src.mocks import MockWeatherProvider
from src.providers import WeatherProvider, WeatherMetrics


class OpenMeteoWeatherProvider(WeatherProvider):
    """Weather provider backed by Open-Meteo with graceful fallback behavior."""

    FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
    CLIMATE_URL = "https://climate-api.open-meteo.com/v1/climate"

    def __init__(
        self,
        timeout_seconds: float = 8.0,
        climate_model: str = "CMCC_CM2_VHR4",
        fallback_provider: Optional[WeatherProvider] = None,
    ):
        self.timeout_seconds = timeout_seconds
        self.climate_model = climate_model
        self.fallback_provider = fallback_provider or MockWeatherProvider()

    @staticmethod
    def _is_forecast_window(travel_date: date, current_time: Optional[date]) -> bool:
        if current_time is None:
            return False
        days_diff = (travel_date - current_time).days
        return 0 <= days_diff <= 14

    def _request_json(self, url: str, params: Dict[str, str]) -> Dict[str, Any]:
        query = urlencode(params)
        with urlopen(f"{url}?{query}", timeout=self.timeout_seconds) as response:
            body = response.read().decode("utf-8")
        return json.loads(body)

    @staticmethod
    def _extract_daily_temps(payload: Dict[str, Any], target_date: date) -> Tuple[float, float]:
        daily = payload.get("daily", {})
        days = daily.get("time", [])
        highs = daily.get("temperature_2m_max", [])
        lows = daily.get("temperature_2m_min", [])

        date_key = target_date.isoformat()
        idx = days.index(date_key)
        return float(highs[idx]), float(lows[idx])

    def _fetch_open_meteo(self, city: City, travel_date: date, is_forecast: bool) -> WeatherMetrics:
        shared_params = {
            "latitude": f"{city.latitude}",
            "longitude": f"{city.longitude}",
            "temperature_unit": "fahrenheit",
            "daily": "temperature_2m_max,temperature_2m_min",
            "timezone": "UTC",
            "start_date": travel_date.isoformat(),
            "end_date": travel_date.isoformat(),
        }

        if is_forecast:
            payload = self._request_json(self.FORECAST_URL, shared_params)
        else:
            climate_params = dict(shared_params)
            climate_params["models"] = self.climate_model
            payload = self._request_json(self.CLIMATE_URL, climate_params)

        high, low = self._extract_daily_temps(payload, travel_date)
        return {
            "high_temp_f": round(high, 1),
            "low_temp_f": round(low, 1),
            "is_forecast": is_forecast,
            "source": "open-meteo",
        }

    def get_weather_metrics(self, city: City, travel_date: date, current_time: Optional[date] = None) -> WeatherMetrics:
        is_forecast = self._is_forecast_window(travel_date, current_time)

        try:
            return self._fetch_open_meteo(city, travel_date, is_forecast=is_forecast)
        except Exception:
            return self.fallback_provider.get_weather_metrics(
                city, travel_date, current_time
            )