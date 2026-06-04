import math
from typing import Dict, Any, Optional
from datetime import date
from src.domain import City, Leg
from src.providers import RoutingProvider, WeatherProvider, ElevationProvider, WeatherMetrics

def stable_hash(s: str) -> int:
    """A deterministic polynomial rolling hash stable across Python processes."""
    h = 0
    for char in s:
        h = (31 * h + ord(char)) & 0xFFFFFFFF
    return h

class MockRoutingProvider(RoutingProvider):
    """Deterministic Mock Routing Provider.
    
    Uses latitude/longitude Euclidean distance to calculate deterministic miles
    and a stable formula for ascent to ensure byte-identical execution.
    """
    def __init__(self, seed: int = 42):
        self.seed = seed

    def get_leg_metrics(self, origin: City, destination: City, preferences: Dict[str, Any]) -> Leg:
        # Approximate miles per degree lat/lon
        dx = (destination.longitude - origin.longitude) * math.cos(math.radians((origin.latitude + destination.latitude) / 2.0))
        dy = destination.latitude - origin.latitude
        distance = math.sqrt(dx*dx + dy*dy) * 69.0
        
        # Ensure minimum distance to avoid zero division/scoring issues
        distance = max(1.0, distance)
        
        # Stable deterministic ascent calculation based on city name hashing
        name_hash = abs(stable_hash(origin.name) + stable_hash(destination.name) + self.seed)
        ascent = (name_hash % 200) * 10.0  # Range: 0 to 1990 ft climb
        
        # Honor routing preferences
        is_legal = True
        # If avoid_highways or avoid_tolls is requested, simulate success
        avoided_highways = preferences.get("avoid_highways", True)
        avoided_tolls = preferences.get("avoid_tolls", True)
        
        return Leg(
            origin=origin,
            destination=destination,
            distance_miles=distance,
            ascent_feet=ascent,
            is_bicycle_legal=is_legal,
            avoided_highways=avoided_highways,
            avoided_tolls=avoided_tolls,
            allowed_ferries=preferences.get("allow_ferries", True),
            allowed_borders=preferences.get("allow_international_borders", True),
            road_class_breakdown={},
            surface_breakdown={},
            geometry=[(origin.latitude, origin.longitude), (destination.latitude, destination.longitude)],
        )


class MockWeatherProvider(WeatherProvider):
    """Deterministic Mock Weather Provider.
    
    Uses mathematical functions of latitude and calendar month to return stable,
    realistic temperature profiles for testing and optimization validation.
    """
    def __init__(self, seed: int = 42):
        self.seed = seed

    def get_weather_metrics(self, city: City, travel_date: date, current_time: Optional[date] = None) -> WeatherMetrics:
        month = travel_date.month
        
        # Base temperature drops by absolute latitude (warmer near equator)
        lat_factor = 85.0 - abs(city.latitude) * 0.8
        
        # Annual seasonal swing using a sine wave peaking in July (month 7)
        # Shift phase so peak is at month 7 (July)
        annual_phase = (month - 4) * (math.pi / 6.0)
        seasonal_swing = 18.0 * math.sin(annual_phase)
        
        avg_high = lat_factor + seasonal_swing
        avg_low = avg_high - 20.0  # 20 degree diurnal range
        
        # Deterministic random noise using stable mathematical hash
        h = abs(stable_hash(city.name) + travel_date.toordinal() + self.seed)
        noise = (h % 10 - 5) * 0.5  # Range: -2.5°F to +2.5°F
        
        avg_high += noise
        avg_low += noise
        
        # Near-term forecast overlay simulation (within 14 days)
        is_forecast = False
        if current_time:
            days_diff = (travel_date - current_time).days
            if 0 <= days_diff <= 14:
                is_forecast = True
                # Add a deterministic forecast anomaly (e.g. a slight heat wave or cold snap)
                forecast_hash = abs(stable_hash(city.name) + travel_date.toordinal() + self.seed + 100)
                forecast_anomaly = (forecast_hash % 6 - 3) * 1.0  # Range: -3°F to +3°F
                
                # Enforce that forecast anomaly is non-zero so we can test the anomaly injection
                if forecast_anomaly == 0.0:
                    forecast_anomaly = 1.0
                    
                avg_high += forecast_anomaly
                avg_low += forecast_anomaly
                
        return {
            "high_temp_f": round(avg_high, 1),
            "low_temp_f": round(avg_low, 1),
            "is_forecast": is_forecast,
            "source": "mock",
        }


class MockElevationProvider(ElevationProvider):
    """Deterministic Mock Elevation Provider."""
    def __init__(self, seed: int = 42):
        self.seed = seed

    def get_elevation_profile(self, origin: City, destination: City) -> float:
        name_hash = abs(stable_hash(origin.name) + stable_hash(destination.name) + self.seed)
        return (name_hash % 200) * 10.0

