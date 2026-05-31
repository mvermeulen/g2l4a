import os
import sqlite3
import threading
from datetime import date, datetime, timedelta, timezone
from typing import Dict, Any, List
import pytest
from src.domain import City, Leg
from src.mocks import MockRoutingProvider, MockWeatherProvider
from src.cache import SQLiteCacheManager, round_coord
from src.cached_providers import CachedRoutingProvider, CachedWeatherProvider, CachedElevationProvider
from src.bulk_fetcher import BulkLegFetcher

DB_PATH = "tests/test_cache.db"

@pytest.fixture(autouse=True)
def cleanup_db():
    # Remove test database if it exists before and after tests
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    yield
    if os.path.exists(DB_PATH):
        try:
            os.remove(DB_PATH)
        except OSError:
            pass

def test_sqlite_cache_manager_basic():
    manager = SQLiteCacheManager(DB_PATH)
    
    city_a = City(name="City A", latitude=40.0, longitude=-80.0)
    city_b = City(name="City B", latitude=41.0, longitude=-81.0)
    prefs = {"avoid_highways": True, "avoid_tolls": True}
    
    leg = Leg(
        origin=city_a,
        destination=city_b,
        distance_miles=123.4,
        ascent_feet=450.0,
        is_bicycle_legal=True,
        avoided_highways=True,
        avoided_tolls=True
    )
    
    # 1. Assert get_leg misses initially
    assert manager.get_leg(city_a, city_b, "mock", prefs) is None
    
    # 2. Save leg and assert retrieve works
    manager.save_leg(leg, "mock", prefs)
    cached = manager.get_leg(city_a, city_b, "mock", prefs)
    
    assert cached is not None
    assert cached.distance_miles == 123.4
    assert cached.ascent_feet == 450.0
    assert cached.is_bicycle_legal is True
    
    # 3. Assert coordinate rounding works (e.g. slight float precision variation still hits cache)
    city_a_approx = City(name="City A Approx", latitude=40.0000001, longitude=-80.0000002)
    cached_approx = manager.get_leg(city_a_approx, city_b, "mock", prefs)
    assert cached_approx is not None
    assert cached_approx.distance_miles == 123.4

    # 4. Save and retrieve weather
    weather_metrics = {
        "high_temp_f": 75.5,
        "low_temp_f": 55.5,
        "is_forecast": True
    }
    travel_date = date(2026, 6, 1)
    
    assert manager.get_weather(city_a, travel_date, is_forecast=True, ttl_hours=24) is None
    
    manager.save_weather(city_a, travel_date, weather_metrics)
    cached_weather = manager.get_weather(city_a, travel_date, is_forecast=True, ttl_hours=24)
    
    assert cached_weather is not None
    assert cached_weather["high_temp_f"] == 75.5
    assert cached_weather["low_temp_f"] == 55.5
    assert cached_weather["is_forecast"] is True
    
    manager.close()


def test_cached_routing_provider_flow():
    manager = SQLiteCacheManager(DB_PATH)
    base = MockRoutingProvider(seed=100)
    cached_provider = CachedRoutingProvider(base, manager, "mock")
    
    city_a = City(name="City A", latitude=30.0, longitude=-90.0)
    city_b = City(name="City B", latitude=31.0, longitude=-91.0)
    prefs = {"avoid_highways": True}
    
    # Track base calls by shadowing/counting calls
    original_get_leg = base.get_leg_metrics
    call_count = 0
    
    def counted_get_leg(origin, destination, preferences):
        nonlocal call_count
        call_count += 1
        return original_get_leg(origin, destination, preferences)
        
    base.get_leg_metrics = counted_get_leg
    
    # First call (cold)
    leg1 = cached_provider.get_leg_metrics(city_a, city_b, prefs)
    assert call_count == 1
    
    # Second call (warm - L1 hit)
    leg2 = cached_provider.get_leg_metrics(city_a, city_b, prefs)
    assert call_count == 1
    assert leg1 == leg2
    
    # Clear L1 to force L2 hit
    cached_provider._l1_cache.clear()
    leg3 = cached_provider.get_leg_metrics(city_a, city_b, prefs)
    assert call_count == 1
    assert leg1 == leg3
    
    manager.close()


def test_cached_weather_provider_forecast_vs_climatology():
    manager = SQLiteCacheManager(DB_PATH)
    base = MockWeatherProvider(seed=200)
    cached_provider = CachedWeatherProvider(base, manager, forecast_ttl_hours=24, climatology_ttl_days=30)
    
    city = City(name="Test City", latitude=45.0, longitude=-122.0)
    current_time = date(2026, 6, 1)
    
    # Within 14 days (Forecast)
    forecast_date = date(2026, 6, 10)
    metrics_fc = cached_provider.get_weather_metrics(city, forecast_date, current_time)
    assert metrics_fc["is_forecast"] is True
    
    # Outside 14 days (Climatology)
    clima_date = date(2026, 6, 20)
    metrics_clima = cached_provider.get_weather_metrics(city, clima_date, current_time)
    assert metrics_clima["is_forecast"] is False
    
    manager.close()


def test_cached_weather_provider_ttl_expiration():
    manager = SQLiteCacheManager(DB_PATH)
    base = MockWeatherProvider(seed=300)
    cached_provider = CachedWeatherProvider(base, manager, forecast_ttl_hours=2, climatology_ttl_days=10)
    
    city = City(name="Test City", latitude=35.0, longitude=-95.0)
    current_time = date(2026, 6, 1)
    travel_date = date(2026, 6, 5) # Forecast (4 days out)
    
    # 1. Warm-up cache
    metrics1 = cached_provider.get_weather_metrics(city, travel_date, current_time)
    
    # Verify cache is populated in L2 DB
    c_lat = round_coord(city.latitude)
    c_lon = round_coord(city.longitude)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT fetched_at FROM weather_cache WHERE city_lat = ?", (c_lat,))
    row = cursor.fetchone()
    assert row is not None
    conn.close()
    
    # 2. Artificially set fetched_at to 3 hours ago (exceeding the 2-hour forecast TTL)
    past_time = (datetime.now(timezone.utc).replace(tzinfo=None) - timedelta(hours=3)).strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(DB_PATH)
    with conn:
        conn.execute("UPDATE weather_cache SET fetched_at = ? WHERE city_lat = ?", (past_time, c_lat))
    conn.close()
    
    # 3. Request weather again - L1 will evict and L2 will miss and delete the expired entry
    cached_provider._l1_cache.clear() # Clear L1 to force L2 validation
    metrics2 = cached_provider.get_weather_metrics(city, travel_date, current_time)
    
    # Assert L2 entry was refreshed/re-saved with new fetched_at
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT fetched_at FROM weather_cache WHERE city_lat = ?", (c_lat,))
    row2 = cursor.fetchone()
    assert row2 is not None
    assert row2[0] != past_time
    conn.close()
    
    manager.close()


def test_bulk_leg_fetcher():
    base = MockRoutingProvider(seed=400)
    fetcher = BulkLegFetcher(base, concurrency_limit=3)
    
    c1 = City(name="City A", latitude=40.0, longitude=-70.0)
    c2 = City(name="City B", latitude=41.0, longitude=-71.0)
    c3 = City(name="City C", latitude=42.0, longitude=-72.0)
    
    requests = [
        (c1, c2, {"avoid_highways": True}),
        (c2, c3, {"avoid_highways": True}),
        (c3, c1, {"avoid_highways": True}),
    ]
    
    legs = fetcher.fetch_legs(requests)
    assert len(legs) == 3
    assert legs[0].origin == c1 and legs[0].destination == c2
    assert legs[1].origin == c2 and legs[1].destination == c3
    assert legs[2].origin == c3 and legs[2].destination == c1
    
    # Empty requests check
    assert fetcher.fetch_legs([]) == []


def test_thread_safety_database_concurrency():
    manager = SQLiteCacheManager(DB_PATH)
    
    c1 = City(name="A", latitude=30.0, longitude=-90.0)
    c2 = City(name="B", latitude=31.0, longitude=-91.0)
    prefs = {}
    
    def run_worker(thread_id: int):
        # Each thread gets its own CachedRoutingProvider wrapping the shared cache manager
        base = MockRoutingProvider(seed=thread_id)
        provider = CachedRoutingProvider(base, manager, "mock")
        for _ in range(10):
            provider.get_leg_metrics(c1, c2, prefs)
        manager.close()
            
    threads = []
    for i in range(5):
        t = threading.Thread(target=run_worker, args=(i,))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    # Verify records exist in DB
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM routing_cache")
    count = cursor.fetchone()[0]
    conn.close()
    assert count > 0
    
    manager.close()
