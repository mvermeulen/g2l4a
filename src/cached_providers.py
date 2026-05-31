from datetime import datetime, date, timezone, timedelta
from typing import Dict, Any, Optional, Tuple
from src.domain import City, Leg
from src.providers import RoutingProvider, WeatherProvider, ElevationProvider, WeatherMetrics
from src.cache import SQLiteCacheManager

class CachedRoutingProvider(RoutingProvider):
    """Wrapper that adds L1 memory and L2 SQLite caching to any RoutingProvider."""
    
    def __init__(
        self,
        base_provider: RoutingProvider,
        cache_manager: SQLiteCacheManager,
        routing_engine: str = "mock",
        source: Optional[str] = None,
    ):
        self.base_provider = base_provider
        self.cache_manager = cache_manager
        self.routing_engine = routing_engine
        self.source = source or self.base_provider.__class__.__name__.lower()
        # L1 cache key: (origin_lat, origin_lon, dest_lat, dest_lon, routing_engine, profile_hash)
        self._l1_cache: Dict[Tuple[float, float, float, float, str, str], Leg] = {}

    def get_leg_metrics(self, origin: City, destination: City, preferences: Dict[str, Any]) -> Leg:
        from src.cache import compute_profile_hash, round_coord
        o_lat = round_coord(origin.latitude)
        o_lon = round_coord(origin.longitude)
        d_lat = round_coord(destination.latitude)
        d_lon = round_coord(destination.longitude)
        p_hash = compute_profile_hash(preferences)

        l1_key = (o_lat, o_lon, d_lat, d_lon, self.routing_engine, p_hash)
        
        # 1. Check L1 in-memory cache
        if l1_key in self._l1_cache:
            return self._l1_cache[l1_key]

        # 2. Check L2 SQLite cache
        leg = self.cache_manager.get_leg(
            origin,
            destination,
            self.routing_engine,
            preferences,
            source=self.source,
        )
        if leg:
            self._l1_cache[l1_key] = leg
            return leg

        # 3. Cache Miss: call base provider
        leg = self.base_provider.get_leg_metrics(origin, destination, preferences)

        # 4. Save to L2 SQLite and L1 in-memory
        self.cache_manager.save_leg(
            leg,
            self.routing_engine,
            preferences,
            source=self.source,
        )
        self._l1_cache[l1_key] = leg

        return leg


class CachedWeatherProvider(WeatherProvider):
    """Wrapper that adds L1 memory and L2 SQLite caching to any WeatherProvider.
    
    Manages forecast-horizon rules and distinct TTLs for near-term forecasts (24h)
    vs historical climatology (30 days).
    """
    
    def __init__(
        self,
        base_provider: WeatherProvider,
        cache_manager: SQLiteCacheManager,
        forecast_ttl_hours: int = 24,
        climatology_ttl_days: int = 30,
        provider_key: Optional[str] = None,
    ):
        self.base_provider = base_provider
        self.cache_manager = cache_manager
        self.forecast_ttl_hours = forecast_ttl_hours
        self.climatology_ttl_days = climatology_ttl_days
        derived_key = provider_key
        if derived_key is None:
            derived_key = self.base_provider.__class__.__name__.lower()
            climate_model = getattr(self.base_provider, "climate_model", None)
            if climate_model:
                derived_key = f"{derived_key}:{climate_model}"
        self.provider_key = derived_key
        # L1 cache key: (city_lat, city_lon, travel_date_iso, is_forecast) -> (metrics, cached_at)
        self._l1_cache: Dict[Tuple[float, float, str, bool], Tuple[WeatherMetrics, datetime]] = {}

    def get_weather_metrics(self, city: City, travel_date: date, current_time: Optional[date] = None) -> WeatherMetrics:
        from src.cache import round_coord
        c_lat = round_coord(city.latitude)
        c_lon = round_coord(city.longitude)
        date_str = travel_date.isoformat()

        # Determine if date is within 14 days of current_time
        is_forecast = False
        if current_time:
            days_diff = (travel_date - current_time).days
            if 0 <= days_diff <= 14:
                is_forecast = True

        l1_key = (c_lat, c_lon, date_str, is_forecast)
        now = datetime.now(timezone.utc).replace(tzinfo=None)
        ttl_hours = self.forecast_ttl_hours if is_forecast else (self.climatology_ttl_days * 24)

        # 1. Check L1 in-memory cache
        if l1_key in self._l1_cache:
            metrics, cached_at = self._l1_cache[l1_key]
            if now - cached_at <= timedelta(hours=ttl_hours):
                return metrics
            else:
                del self._l1_cache[l1_key]

        # 2. Check L2 SQLite cache
        cached_res = self.cache_manager.get_weather(
            city,
            travel_date,
            is_forecast,
            ttl_hours,
            provider_key=self.provider_key,
        )
        
        def _clean_source(src: str) -> str:
            src_lower = src.lower()
            if "mock" in src_lower:
                return "mock"
            if "statecapitalmonthlynormals" in src_lower or "wikipedia" in src_lower:
                return "wikipedia"
            if "openmeteo" in src_lower or "open-meteo" in src_lower:
                return "open-meteo"
            return src

        if cached_res:
            metrics: WeatherMetrics = {
                "high_temp_f": float(cached_res["high_temp_f"]),
                "low_temp_f": float(cached_res["low_temp_f"]),
                "is_forecast": bool(cached_res["is_forecast"]),
                "source": _clean_source(str(cached_res.get("source", self.provider_key or "unknown"))),
            }
            self._l1_cache[l1_key] = (metrics, now)
            return metrics

        # 3. Cache Miss: call base provider
        raw_metrics = self.base_provider.get_weather_metrics(city, travel_date, current_time)
        metrics: WeatherMetrics = {
            "high_temp_f": raw_metrics["high_temp_f"],
            "low_temp_f": raw_metrics["low_temp_f"],
            "is_forecast": raw_metrics.get("is_forecast", is_forecast),
            "source": _clean_source(raw_metrics.get("source", self.provider_key or "unknown")),
        }

        # 4. Save to L2 SQLite and L1 in-memory
        self.cache_manager.save_weather(city, travel_date, dict(metrics), provider_key=self.provider_key)
        self._l1_cache[l1_key] = (metrics, now)

        return metrics


class CachedElevationProvider(ElevationProvider):
    """Wrapper that adds L1 memory caching to any ElevationProvider."""
    
    def __init__(self, base_provider: ElevationProvider, cache_manager: SQLiteCacheManager):
        self.base_provider = base_provider
        self.cache_manager = cache_manager
        # L1 cache key: (origin_lat, origin_lon, dest_lat, dest_lon)
        self._l1_cache: Dict[Tuple[float, float, float, float], float] = {}

    def get_elevation_profile(self, origin: City, destination: City) -> float:
        from src.cache import round_coord
        o_lat = round_coord(origin.latitude)
        o_lon = round_coord(origin.longitude)
        d_lat = round_coord(destination.latitude)
        d_lon = round_coord(destination.longitude)

        l1_key = (o_lat, o_lon, d_lat, d_lon)
        
        # Check L1 memory
        if l1_key in self._l1_cache:
            return self._l1_cache[l1_key]

        # Fetch and cache
        elevation = self.base_provider.get_elevation_profile(origin, destination)
        self._l1_cache[l1_key] = elevation
        return elevation
