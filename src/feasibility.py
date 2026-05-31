from typing import Dict, Any, List, Tuple
from datetime import date
from src.domain import Itinerary, ConstraintViolation

class FeasibilityEngine:
    """Validator for bicycle tour schedules against hard constraints (weather, mileage, ascent)."""
    
    def __init__(self, system_config: Dict[str, Any]):
        self.config = system_config
        self.weather_constraints = self.config.get("weather_constraints", {})
        self.daily_constraints = self.config.get("daily_constraints", {})
        
        # Segment precheck memoization tables
        self._weather_memo: Dict[Tuple[str, str], List[ConstraintViolation]] = {}
        self._daily_memo: Dict[Tuple[str, str, str], List[ConstraintViolation]] = {}

    def clear_cache(self):
        """Clears the internal memoization tables."""
        self._weather_memo.clear()
        self._daily_memo.clear()

    def check_weather_feasibility(self, city_name: str, travel_date: date, high_temp: float) -> List[ConstraintViolation]:
        """Validates high temperature bounds for a city on a travel date."""
        key = (city_name, travel_date.isoformat())
        if key in self._weather_memo:
            return self._weather_memo[key]

        violations = []
        max_high = self.weather_constraints.get("max_avg_high_f")
        min_high = self.weather_constraints.get("min_avg_high_f")

        if max_high is not None and high_temp > max_high:
            violations.append(ConstraintViolation(
                code="INFEASIBLE_WEATHER_MAX_HIGH",
                location=city_name,
                date=travel_date.isoformat(),
                observed_value=high_temp,
                threshold_limit=max_high,
                remediation_hint=f"Consider traveling during a cooler season or modifying the route to bypass {city_name}."
            ))

        if min_high is not None and high_temp < min_high:
            violations.append(ConstraintViolation(
                code="INFEASIBLE_WEATHER_MIN_HIGH",
                location=city_name,
                date=travel_date.isoformat(),
                observed_value=high_temp,
                threshold_limit=min_high,
                remediation_hint=f"Consider traveling during a warmer season or modifying the route to bypass {city_name}."
            ))

        self._weather_memo[key] = violations
        return violations

    def check_daily_feasibility(self, origin_name: str, dest_name: str, travel_date: date, distance: float, ascent: float) -> List[ConstraintViolation]:
        """Validates daily mileage and climbing efforts for a non-rest day segment."""
        key = (origin_name, dest_name, travel_date.isoformat())
        if key in self._daily_memo:
            return self._daily_memo[key]

        violations = []
        max_miles = self.daily_constraints.get("max_miles_per_day")
        max_climb = self.daily_constraints.get("max_climb_ft_per_day")

        if max_miles is not None and distance > max_miles:
            violations.append(ConstraintViolation(
                code="INFEASIBLE_DAILY_MILEAGE",
                location=f"Leg: {origin_name} -> {dest_name}",
                date=travel_date.isoformat(),
                observed_value=distance,
                threshold_limit=max_miles,
                remediation_hint="Consider adding a rest day, shortening the leg, or splitting it."
            ))

        if max_climb is not None and ascent > max_climb:
            violations.append(ConstraintViolation(
                code="INFEASIBLE_DAILY_ASCENT",
                location=f"Leg: {origin_name} -> {dest_name}",
                date=travel_date.isoformat(),
                observed_value=ascent,
                threshold_limit=max_climb,
                remediation_hint="Consider bypassing the mountainous section or splitting the daily climb."
            ))

        self._daily_memo[key] = violations
        return violations

    def validate_itinerary(self, itinerary: Itinerary, fail_fast: bool = False) -> Itinerary:
        """Validates an itinerary's schedule against weather and daily effort caps.
        
        Args:
            itinerary: The Itinerary object containing schedule items.
            fail_fast: If True, aborts verification on the first violation.
            
        Returns:
            The mutated Itinerary containing is_feasible status and structured violation details.
        """
        violations: List[ConstraintViolation] = []

        for day in itinerary.schedule:
            # 1. Weather checks apply to both travel and rest days
            weather_violations = self.check_weather_feasibility(
                day.destination.name,
                day.date,
                day.high_temp_f
            )
            violations.extend(weather_violations)

            if fail_fast and violations:
                break

            # 2. Daily effort checks only apply to travel days
            if not day.is_rest_day:
                daily_violations = self.check_daily_feasibility(
                    day.origin.name,
                    day.destination.name,
                    day.date,
                    day.distance_miles,
                    day.ascent_feet
                )
                violations.extend(daily_violations)

                if fail_fast and violations:
                    break

        itinerary.is_feasible = (len(violations) == 0)
        itinerary.violation_details = [v.to_dict() for v in violations]
        return itinerary
