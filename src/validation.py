import os
import yaml
from datetime import datetime, date
from typing import Dict, Any, List, Tuple, Optional
from src.domain import City, Itinerary, ScoringWeights
from src.config import ConfigManager

# Standardized offline geocoding registry for test fixtures and state capitals
CITY_REGISTRY: Dict[str, Tuple[float, float]] = {
    "montgomery, alabama": (32.3792, -86.3077),
    "juneau, alaska": (58.3019, -134.4197),
    "phoenix, arizona": (33.4484, -112.0740),
    "little rock, arkansas": (34.7465, -92.2896),
    "sacramento, california": (38.5816, -121.4944),
    "denver, colorado": (39.7392, -104.9903),
    "hartford, connecticut": (41.7637, -72.6851),
    "dover, delaware": (39.1582, -75.5244),
    "tallahassee, florida": (30.4383, -84.2807),
    "atlanta, georgia": (33.7490, -84.3880),
    "honolulu, hawaii": (21.3069, -157.8583),
    "boise, idaho": (43.6150, -116.2023),
    "springfield, illinois": (39.7817, -89.6501),
    "indianapolis, indiana": (39.7684, -86.1581),
    "des moines, iowa": (41.5868, -93.6250),
    "topeka, kansas": (39.0473, -95.6752),
    "frankfort, kentucky": (38.2009, -84.8733),
    "baton_rouge, louisiana": (30.4515, -91.1871),
    "baton rouge, louisiana": (30.4515, -91.1871),
    "augusta, maine": (44.3106, -69.7795),
    "annapolis, maryland": (38.9784, -76.4922),
    "boston, massachusetts": (42.3601, -71.0589),
    "lansing, michigan": (42.7325, -84.5555),
    "st. paul, minnesota": (44.9537, -93.0900),
    "st paul, minnesota": (44.9537, -93.0900),
    "jackson, mississippi": (32.2988, -90.1848),
    "jefferson city, missouri": (38.5767, -92.1735),
    "helena, montana": (46.5891, -112.0391),
    "lincoln, nebraska": (40.8136, -96.7026),
    "carson city, nevada": (39.1638, -119.7674),
    "concord, new hampshire": (43.2081, -71.5375),
    "trenton, new jersey": (40.2170, -74.7429),
    "santa fe, new mexico": (35.6870, -105.9378),
    "albany, new york": (42.6526, -73.7562),
    "raleigh, north carolina": (35.7796, -78.6382),
    "bismarck, north dakota": (46.8083, -100.7837),
    "columbus, ohio": (39.9612, -82.9988),
    "oklahoma city, oklahoma": (35.4676, -97.5164),
    "salem, oregon": (44.9429, -123.0351),
    "harrisburg, pennsylvania": (40.2732, -76.8867),
    "providence, rhode island": (41.8240, -71.4128),
    "columbia, south carolina": (33.9988, -81.0348),
    "pierre, south dakota": (44.3683, -100.3512),
    "nashville, tennessee": (36.1627, -86.7816),
    "austin, texas": (30.2672, -97.7431),
    "salt lake city, utah": (40.7608, -111.8910),
    "montpelier, vermont": (44.2601, -72.5754),
    "richmond, virginia": (37.5407, -77.4360),
    "olympia, washington": (47.0379, -122.9007),
    "charleston, west virginia": (38.3498, -81.6326),
    "madison, wisconsin": (43.0731, -89.4012),
    "cheyenne, wyoming": (41.1400, -104.8203),
    "washington, dc": (38.9072, -77.0369),
    "washington dc": (38.9072, -77.0369),
    "portland, oregon": (45.5152, -122.6784),
}


class ValidationError(Exception):
    """Exception raised for input validation and schema failures."""
    def __init__(self, code: str, message: str, location: Optional[str] = None):
        super().__init__(message)
        self.code = code
        self.location = location

    def to_dict(self) -> Dict[str, Any]:
        return {
            "code": self.code,
            "message": str(self),
            "location": self.location
        }


class RequestParser:
    """Parses, deep-merges, and validates planning requests into Itineraries."""
    
    def __init__(self, system_defaults_path: Optional[str] = None):
        self.config_manager = ConfigManager(system_defaults_path=system_defaults_path)

    def _resolve_city(self, name: str) -> City:
        normalized = name.strip().lower()
        if normalized not in CITY_REGISTRY:
            raise ValidationError(
                code="INVALID_CITY",
                message=f"City '{name}' is not in the recognized geocoding registry.",
                location=name
            )
        lat, lon = CITY_REGISTRY[normalized]
        return City(name=name, latitude=lat, longitude=lon)

    def parse_request_dict(self, payload: Dict[str, Any]) -> Tuple[Itinerary, Dict[str, Any]]:
        """Parses a dictionary request payload, resolves types, and enforces constraints."""
        
        # 1. Check required top-level parameters
        start_name = payload.get("start_city")
        comp_name = payload.get("completion_city")
        
        if not start_name:
            raise ValidationError("MISSING_START_CITY", "A starting city must be specified.")
        if not comp_name:
            raise ValidationError("MISSING_COMPLETION_CITY", "A completion city must be specified.")
            
        # 2. Resolve geocoding for cities
        start_city = self._resolve_city(start_name)
        completion_city = self._resolve_city(comp_name)
        
        via_names = payload.get("via_cities", [])
        if not isinstance(via_names, list):
            raise ValidationError("INVALID_VIA_CITIES", "via_cities must be a list of city name strings.")
            
        via_cities = [self._resolve_city(name) for name in via_names]
        
        # 3. Parse date (fixed-date vs optimize-date)
        start_date: Optional[date] = None
        date_val = payload.get("start_date")
        if date_val:
            if isinstance(date_val, date):
                start_date = date_val
            elif isinstance(date_val, str):
                try:
                    start_date = datetime.strptime(date_val, "%Y-%m-%d").date()
                except ValueError:
                    raise ValidationError(
                        code="INVALID_DATE",
                        message=f"Start date '{date_val}' must be in YYYY-MM-DD format.",
                        location="start_date"
                    )
            else:
                 raise ValidationError(
                     code="INVALID_DATE",
                     message="Start date must be a YYYY-MM-DD date or string.",
                     location="start_date"
                 )
        
        # 4. Hierarchical configuration load & merge
        effective_config = self.config_manager.get_effective_config(user_overrides=payload)
        
        # 5. Enforce Solver Constraints (City count limits)
        max_cities = effective_config.get("solver_constraints", {}).get("max_total_cities", 50)
        total_cities_count = len(via_cities) + 2
        if total_cities_count > max_cities:
            raise ValidationError(
                code="CITY_COUNT_EXCEEDED",
                message=f"Requested {total_cities_count} cities exceeds the solver limit of {max_cities}.",
                location="via_cities"
            )
            
        # 6. Validate Scoring Weights (non-negative, sum-to-1)
        weights_config = effective_config.get("scoring", {}).get("weights", {})
        try:
            ScoringWeights(
                weather=float(weights_config.get("weather", 0.0)),
                distance=float(weights_config.get("distance", 0.0)),
                hills=float(weights_config.get("hills", 0.0))
            )
        except (ValueError, TypeError) as e:
            raise ValidationError(
                code="INVALID_SCORING_WEIGHTS",
                message=f"Scoring weights are invalid: {str(e)}",
                location="scoring.weights"
            )
            
        # 7. Validate Constraints sanity
        weather_conf = effective_config.get("weather_constraints", {})
        max_high = weather_conf.get("max_avg_high_f")
        min_high = weather_conf.get("min_avg_high_f")
        if max_high is not None and min_high is not None:
            if max_high < min_high:
                raise ValidationError(
                    code="INVALID_WEATHER_RANGE",
                    message=f"max_avg_high_f ({max_high}) cannot be less than min_avg_high_f ({min_high}).",
                    location="weather_constraints"
                )
                
        daily_conf = effective_config.get("daily_constraints", {})
        max_miles = daily_conf.get("max_miles_per_day", 0.0)
        max_climb = daily_conf.get("max_climb_ft_per_day", 0.0)
        if max_miles <= 0.0 or max_climb <= 0.0:
            raise ValidationError(
                code="INVALID_DAILY_LIMIT",
                message=f"Daily limits must be positive. Got miles={max_miles}, climb={max_climb}",
                location="daily_constraints"
            )
            
        # 8. Create Itinerary
        itinerary = Itinerary(
            start_city=start_city,
            completion_city=completion_city,
            via_cities=via_cities,
            start_date=start_date
        )
        
        return itinerary, effective_config

    def parse_request_file(self, file_path: str) -> Tuple[Itinerary, Dict[str, Any]]:
        """Parses a YAML request file, deep-merges config defaults, and validates."""
        if not os.path.exists(file_path):
            raise ValidationError(
                code="FILE_NOT_FOUND",
                message=f"Request YAML file not found: {file_path}",
                location=file_path
            )
            
        try:
            with open(file_path, "r") as f:
                payload = yaml.safe_load(f)
                if not payload:
                    raise ValidationError("EMPTY_REQUEST", "Request YAML file is empty.")
        except ValidationError:
            raise
        except Exception as e:
            raise ValidationError(
                code="YAML_PARSE_ERROR",
                message=f"Failed to parse request YAML: {str(e)}"
            )
            
        return self.parse_request_dict(payload)
