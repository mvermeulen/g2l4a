from datetime import date
import json
from typing import Optional

from src.cached_providers import CachedWeatherProvider
from src.cache import SQLiteCacheManager
from src.domain import City
from src.providers import WeatherProvider, WeatherMetrics
from src.open_meteo_weather import OpenMeteoWeatherProvider
from src.monthly_normals_weather import StateCapitalMonthlyNormalsWeatherProvider


def test_open_meteo_weather_provider_success(monkeypatch):
    city = City(name="Austin, Texas", latitude=30.2672, longitude=-97.7431)
    provider = OpenMeteoWeatherProvider()

    def fake_request_json(_url, _params):
        return {
            "daily": {
                "time": ["2026-03-01"],
                "temperature_2m_max": [71.2],
                "temperature_2m_min": [52.4],
            }
        }

    monkeypatch.setattr(provider, "_request_json", fake_request_json)

    metrics = provider.get_weather_metrics(city, date(2026, 3, 1), date(2025, 1, 1))
    assert metrics["high_temp_f"] == 71.2
    assert metrics["low_temp_f"] == 52.4
    assert metrics["is_forecast"] is False


def test_open_meteo_weather_provider_fallback(monkeypatch):
    city = City(name="Austin, Texas", latitude=30.2672, longitude=-97.7431)
    provider = OpenMeteoWeatherProvider()

    def raise_request_error(_url, _params):
        raise RuntimeError("open-meteo unavailable")

    monkeypatch.setattr(provider, "_request_json", raise_request_error)

    metrics = provider.get_weather_metrics(city, date(2026, 3, 1), date(2026, 2, 20))
    assert "high_temp_f" in metrics
    assert "low_temp_f" in metrics
    assert metrics["is_forecast"] is True


def test_cached_weather_provider_reuses_open_meteo_results(tmp_path, monkeypatch):
    city = City(name="Austin, Texas", latitude=30.2672, longitude=-97.7431)
    travel_date = date(2026, 3, 1)
    current_date = date(2025, 1, 1)

    provider = OpenMeteoWeatherProvider()
    calls = {"count": 0}

    def fake_request_json(_url, _params):
        calls["count"] += 1
        return {
            "daily": {
                "time": ["2026-03-01"],
                "temperature_2m_max": [70.0],
                "temperature_2m_min": [50.0],
            }
        }

    monkeypatch.setattr(provider, "_request_json", fake_request_json)

    cache_path = tmp_path / "weather_cache.db"
    manager = SQLiteCacheManager(str(cache_path))
    cached_provider = CachedWeatherProvider(provider, manager)

    first = cached_provider.get_weather_metrics(city, travel_date, current_date)
    second = cached_provider.get_weather_metrics(city, travel_date, current_date)

    assert first == second
    assert calls["count"] == 1

    manager.close()


def test_provider_aware_cache_keys_isolate_entries(tmp_path):
    class ConstantWeatherProvider(WeatherProvider):
        def __init__(self, high: float, low: float):
            self.high = high
            self.low = low

        def get_weather_metrics(self, city: City, travel_date: date, current_time: Optional[date] = None) -> WeatherMetrics:
            return {
                "high_temp_f": self.high,
                "low_temp_f": self.low,
                "is_forecast": False,
                "source": "constant",
            }

    city = City(name="Austin, Texas", latitude=30.2672, longitude=-97.7431)
    travel_date = date(2026, 3, 1)

    cache_path = tmp_path / "weather_cache_isolation.db"
    manager = SQLiteCacheManager(str(cache_path))

    provider_a = CachedWeatherProvider(
        ConstantWeatherProvider(71.0, 50.0),
        manager,
        provider_key="provider_a",
    )
    provider_b = CachedWeatherProvider(
        ConstantWeatherProvider(61.0, 40.0),
        manager,
        provider_key="provider_b",
    )

    a_metrics = provider_a.get_weather_metrics(city, travel_date)
    b_metrics = provider_b.get_weather_metrics(city, travel_date)

    assert a_metrics["high_temp_f"] == 71.0
    assert b_metrics["high_temp_f"] == 61.0

    manager.close()


def test_state_capital_monthly_normals_provider_reads_dataset(tmp_path):
    dataset = {
        "metadata": {"source": "test"},
        "cities": {
            "Phoenix, Arizona": {
                "aliases": ["Phoenix, Arizona", "phoenix, arizona"],
                "monthly": {
                    "8": {"high_temp_f": 105.1, "low_temp_f": 83.6}
                },
            }
        },
    }
    dataset_path = tmp_path / "state_capitals_monthly_normals.json"
    dataset_path.write_text(json.dumps(dataset), encoding="utf-8")

    provider = StateCapitalMonthlyNormalsWeatherProvider(dataset_path=str(dataset_path))
    city = City(name="Phoenix, Arizona", latitude=33.4484, longitude=-112.0740)

    metrics = provider.get_weather_metrics(city, date(2026, 8, 18), date(2026, 8, 1))
    assert metrics["high_temp_f"] == 105.1
    assert metrics["low_temp_f"] == 83.6
    assert metrics["is_forecast"] is False


def test_open_meteo_falls_back_to_monthly_normals_before_mock(tmp_path, monkeypatch):
    dataset = {
        "metadata": {"source": "test"},
        "cities": {
            "Phoenix, Arizona": {
                "aliases": ["Phoenix, Arizona", "phoenix, arizona"],
                "monthly": {
                    "8": {"high_temp_f": 105.1, "low_temp_f": 83.6}
                },
            }
        },
    }
    dataset_path = tmp_path / "state_capitals_monthly_normals.json"
    dataset_path.write_text(json.dumps(dataset), encoding="utf-8")

    monthly_provider = StateCapitalMonthlyNormalsWeatherProvider(dataset_path=str(dataset_path))
    provider = OpenMeteoWeatherProvider(fallback_provider=monthly_provider)

    def raise_request_error(_url, _params):
        raise RuntimeError("open-meteo unavailable")

    monkeypatch.setattr(provider, "_request_json", raise_request_error)

    city = City(name="Phoenix, Arizona", latitude=33.4484, longitude=-112.0740)
    metrics = provider.get_weather_metrics(city, date(2026, 8, 18), date(2026, 8, 1))

    assert metrics["high_temp_f"] == 105.1
    assert metrics["low_temp_f"] == 83.6
    assert metrics["is_forecast"] is False