import sys
from datetime import date, datetime
from typing import Any, cast

import pandas as pd

from src.cache import SQLiteCacheManager
from src.domain import City
from src.providers import WeatherProvider
from src.meteostat_weather import MeteostatWeatherProvider


def test_meteostat_cache_hit(tmp_path):
    # Set up mock cache DB
    cache_path = tmp_path / "test_meteostat_cache.db"
    manager = SQLiteCacheManager(str(cache_path))
    
    # Store a specific climatology entry in the cache
    climatology = [
        {
            "month": 6,
            "day": 2,
            "avg_high_f": 85.5,
            "avg_low_f": 65.2,
            "station_id": "TEST01",
            "station_distance_m": 1200.0
        }
    ]
    manager.save_meteostat_climatology(30.0, -90.0, climatology)
    
    # Initialize provider
    provider = MeteostatWeatherProvider(cache_manager=manager)
    city = City(name="Test City", latitude=30.0, longitude=-90.0)
    
    # Run query
    metrics = provider.get_weather_metrics(city, date(2026, 6, 2))
    
    # Verify cache hit
    assert metrics["high_temp_f"] == 85.5
    assert metrics["low_temp_f"] == 65.2
    assert metrics["is_forecast"] is False
    assert metrics["source"] == "meteostat"
    
    manager.close()


def test_meteostat_dynamic_fetch_and_cache(tmp_path, monkeypatch):
    cache_path = tmp_path / "test_meteostat_dynamic.db"
    manager = SQLiteCacheManager(str(cache_path))
    
    provider = MeteostatWeatherProvider(cache_manager=manager)
    city = City(name="Test City", latitude=30.0, longitude=-90.0)
    
    # Mocking meteostat classes/functions
    class MockPoint:
        def __init__(self, lat, lon):
            self.lat = lat
            self.lon = lon

    class MockStations:
        def nearby(self, point):
            return pd.DataFrame(
                {"distance": [5000.0]},
                index=["TEST02"]
            )

    class MockDailyQuery:
        def fetch(self):
            # Create a 3-day series to test aggregation
            dates = [
                datetime(2001, 6, 2),
                datetime(2002, 6, 2),
                datetime(2003, 6, 2)
            ]
            df = pd.DataFrame(
                {
                    "tmax": [30.0, 31.0, 29.0], # Mean C: 30.0 -> F: 30.0 * 9/5 + 32 = 86.0
                    "tmin": [20.0, 21.0, 19.0], # Mean C: 20.0 -> F: 20.0 * 9/5 + 32 = 68.0
                },
                index=pd.DatetimeIndex(dates)
            )
            return df

    def mock_daily_func(station_id, start, end):
        return MockDailyQuery()

    # Patch meteostat imports in src.meteostat_weather
    import sys
    from types import ModuleType
    
    mock_meteostat: Any = ModuleType("meteostat")
    mock_meteostat.Point = MockPoint
    mock_meteostat.stations = MockStations()
    mock_meteostat.daily = mock_daily_func
    cast(Any, sys.modules)["meteostat"] = mock_meteostat

    # Perform query
    metrics = provider.get_weather_metrics(city, date(2026, 6, 2))
    
    # Assert return values
    assert metrics["high_temp_f"] == 86.0
    assert metrics["low_temp_f"] == 68.0
    assert metrics["is_forecast"] is False
    assert metrics["source"] == "meteostat"
    
    # Assert database cache got populated
    cached = manager.get_meteostat_day_average(30.0, -90.0, 6, 2)
    assert cached is not None
    assert cached["high_temp_f"] == 86.0
    assert cached["low_temp_f"] == 68.0
    
    manager.close()


def test_meteostat_fallback_on_failure(tmp_path, monkeypatch):
    cache_path = tmp_path / "test_meteostat_fallback.db"
    manager = SQLiteCacheManager(str(cache_path))
    
    class FakeFallbackProvider(WeatherProvider):
        def get_weather_metrics(self, city, travel_date, current_time=None):
            return {
                "high_temp_f": 99.9,
                "low_temp_f": 11.1,
                "is_forecast": True,
                "source": "fake-fallback"
            }

    provider = MeteostatWeatherProvider(
        cache_manager=manager,
        fallback_provider=FakeFallbackProvider()
    )
    city = City(name="Test City", latitude=30.0, longitude=-90.0)

    # Force dynamic fetch failure by removing/mocking meteostat to raise error
    cast(Any, sys.modules)["meteostat"] = None  # Force import error

    metrics = provider.get_weather_metrics(city, date(2026, 6, 2))
    
    # Assert it fell back correctly
    assert metrics["high_temp_f"] == 99.9
    assert metrics["low_temp_f"] == 11.1
    assert metrics["is_forecast"] is True
    assert metrics["source"] == "fake-fallback"
    
    manager.close()
