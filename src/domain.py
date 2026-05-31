from dataclasses import dataclass, field
from typing import List, Optional, Dict
from datetime import date

@dataclass(frozen=True)
class City:
    name: str
    latitude: float
    longitude: float

    def __post_init__(self):
        # Validate coordinate boundaries
        if not (-90 <= self.latitude <= 90):
            raise ValueError(f"Latitude must be between -90 and 90, got {self.latitude}")
        if not (-180 <= self.longitude <= 180):
            raise ValueError(f"Longitude must be between -180 and 180, got {self.longitude}")


@dataclass(frozen=True)
class Leg:
    origin: City
    destination: City
    distance_miles: float
    ascent_feet: float
    is_bicycle_legal: bool = True
    avoided_highways: bool = True
    avoided_tolls: bool = True
    allowed_ferries: bool = True
    allowed_borders: bool = True


@dataclass(frozen=True)
class WeatherConstraints:
    max_avg_high_f: float
    min_avg_high_f: float


@dataclass(frozen=True)
class DailyConstraints:
    max_miles_per_day: float
    max_climb_ft_per_day: float


@dataclass(frozen=True)
class SolverConstraints:
    max_total_cities: int
    max_search_minutes: float


@dataclass(frozen=True)
class ScoringWeights:
    weather: float
    distance: float
    hills: float

    def __post_init__(self):
        # Check non-negativity
        if self.weather < 0 or self.distance < 0 or self.hills < 0:
            raise ValueError(f"Weights must be non-negative. Got weather={self.weather}, distance={self.distance}, hills={self.hills}")
        # Validate sum is 1 within tolerance
        total = self.weather + self.distance + self.hills
        if abs(total - 1.0) > 1e-6:
            raise ValueError(f"Weights must sum to 1.0. Got weather={self.weather}, distance={self.distance}, hills={self.hills} (sum={total})")


@dataclass
class Scores:
    weather: float = 0.0
    distance: float = 0.0
    hills: float = 0.0
    total: float = 0.0


@dataclass
class DailySchedule:
    day_number: int
    date: date
    origin: City
    destination: City
    distance_miles: float
    ascent_feet: float
    high_temp_f: float
    low_temp_f: float
    is_rest_day: bool = False


@dataclass
class Itinerary:
    start_city: City
    completion_city: City
    via_cities: List[City]
    start_date: Optional[date] = None
    legs: List[Leg] = field(default_factory=list)
    schedule: List[DailySchedule] = field(default_factory=list)
    scores: Scores = field(default_factory=Scores)
    is_feasible: bool = True
    violation_details: List[Dict] = field(default_factory=list)
    original_geodesic_baseline: Optional[float] = None


@dataclass(frozen=True)
class ConstraintViolation:
    code: str
    location: str
    date: str
    observed_value: float
    threshold_limit: float
    remediation_hint: str

    def to_dict(self) -> dict:
        return {
            "code": self.code,
            "location": self.location,
            "date": self.date,
            "observed_value": self.observed_value,
            "threshold_limit": self.threshold_limit,
            "remediation_hint": self.remediation_hint
        }

