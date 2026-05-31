from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, Protocol, TypedDict
from datetime import date
from src.domain import City, Leg

class RoutingProvider(ABC):
    """Abstract Base Class representing a routing provider interface."""
    
    @abstractmethod
    def get_leg_metrics(self, origin: City, destination: City, preferences: Dict[str, Any]) -> Leg:
        """Computes routing metrics (distance, ascent, legality) between two cities."""
        pass


from typing import Dict, Any, Optional, Protocol, TypedDict, runtime_checkable

class WeatherMetrics(TypedDict):
    high_temp_f: float
    low_temp_f: float
    is_forecast: bool
    source: str


@runtime_checkable
class WeatherProvider(Protocol):
    def get_weather_metrics(
        self, city: "City", travel_date: date, current_time: Optional[date] = None
    ) -> WeatherMetrics:
        ...


class ElevationProvider(ABC):
    """Abstract Base Class representing an elevation provider interface."""
    
    @abstractmethod
    def get_elevation_profile(self, origin: City, destination: City) -> float:
        """Fetches recomputed total ascent (feet) for a route segment as a fallback."""
        pass
