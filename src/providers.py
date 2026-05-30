from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from datetime import date
from src.domain import City, Leg

class RoutingProvider(ABC):
    """Abstract Base Class representing a routing provider interface."""
    
    @abstractmethod
    def get_leg_metrics(self, origin: City, destination: City, preferences: Dict[str, Any]) -> Leg:
        """Computes routing metrics (distance, ascent, legality) between two cities."""
        pass


class WeatherProvider(ABC):
    """Abstract Base Class representing a weather/climate provider interface."""
    
    @abstractmethod
    def get_weather_metrics(self, city: City, travel_date: date, current_time: Optional[date] = None) -> Dict[str, float]:
        """Fetches weather metrics (high_temp_f, low_temp_f) for a city and date.
        
        If current_time is provided and travel_date falls within 14 days,
        uses near-term forecast data overlay; otherwise uses historical climatology averages.
        """
        pass


class ElevationProvider(ABC):
    """Abstract Base Class representing an elevation provider interface."""
    
    @abstractmethod
    def get_elevation_profile(self, origin: City, destination: City) -> float:
        """Fetches recomputed total ascent (feet) for a route segment as a fallback."""
        pass
