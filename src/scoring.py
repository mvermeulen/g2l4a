import math
from typing import Dict, Any, List, Tuple
from src.domain import Itinerary, Scores, City

def haversine_distance(c1: City, c2: City) -> float:
    """Calculates the great-circle distance (miles) between two cities."""
    R = 3958.8  # Earth radius in miles
    lat1 = math.radians(c1.latitude)
    lon1 = math.radians(c1.longitude)
    lat2 = math.radians(c2.latitude)
    lon2 = math.radians(c2.longitude)
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = math.sin(dlat / 2.0)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2.0)**2
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
    return R * c

def compute_geodesic_baseline(itinerary: Itinerary) -> float:
    """Calculates the baseline sequential geodesic distance across all requested points."""
    current = itinerary.start_city
    total = 0.0
    for city in itinerary.via_cities:
        total += haversine_distance(current, city)
        current = city
    total += haversine_distance(current, itinerary.completion_city)
    return total

def compute_shortest_geodesic_baseline(itinerary: Itinerary) -> float:
    """Calculates the baseline sequential geodesic distance along the shortest 2-opt refined TSP path."""
    unvisited = list(itinerary.via_cities)
    sequence = [itinerary.start_city]
    
    # 1. Greedy NN seed
    while unvisited:
        current = sequence[-1]
        best_city = min(unvisited, key=lambda c: haversine_distance(current, c))
        unvisited.remove(best_city)
        sequence.append(best_city)
    sequence.append(itinerary.completion_city)
    
    # 2. 2-opt refinement
    n = len(sequence)
    if n <= 3:
        total = 0.0
        for i in range(n - 1):
            total += haversine_distance(sequence[i], sequence[i+1])
        return total

    def path_dist(seq: List[City]) -> float:
        return sum(haversine_distance(seq[idx], seq[idx+1]) for idx in range(len(seq) - 1))
        
    best_dist = path_dist(sequence)
    improved = True
    
    while improved:
        improved = False
        for i in range(1, n - 2):
            for j in range(i + 1, n - 1):
                new_sequence = sequence[:i] + sequence[i:j+1][::-1] + sequence[j+1:]
                new_dist = path_dist(new_sequence)
                if new_dist < best_dist - 1e-2:
                    sequence = new_sequence
                    best_dist = new_dist
                    improved = True
                    break
            if improved:
                break
                
    return best_dist

class ScoringEngine:
    """Computes soft objective desirability scores and deterministically ranks itineraries."""
    
    def __init__(self, system_config: Dict[str, Any]):
        self.config = system_config
        self.scoring_config = self.config.get("scoring", {})
        self.weights = self.scoring_config.get("weights", {"weather": 0.45, "distance": 0.30, "hills": 0.25})
        self.comfort = self.scoring_config.get("comfort", {"ideal_temp_f": 70.0, "temp_tolerance_f": 20.0})
        self.daily_constraints = self.config.get("daily_constraints", {"max_climb_ft_per_day": 5000.0})

    def compute_weather_score(self, itinerary: Itinerary) -> float:
        """Computes the weather comfort score [0.0, 1.0] across all days."""
        if not itinerary.schedule:
            return 0.0
        
        ideal = self.comfort.get("ideal_temp_f", 70.0)
        tol = self.comfort.get("temp_tolerance_f", 20.0)
        if tol <= 0:
            tol = 20.0

        total_score = 0.0
        for day in itinerary.schedule:
            diff = abs(day.high_temp_f - ideal)
            day_score = max(0.0, 1.0 - (diff / tol))
            total_score += day_score

        return total_score / len(itinerary.schedule)

    def compute_distance_score(self, itinerary: Itinerary) -> float:
        """Computes the detour distance efficiency score [0.0, 1.0] using a quadratic relationship."""
        actual = sum(leg.distance_miles for leg in itinerary.legs)
        if actual <= 0 and itinerary.schedule:
            actual = sum(day.distance_miles for day in itinerary.schedule)

        if actual <= 0:
            return 0.0

        if itinerary.original_geodesic_baseline is not None and itinerary.original_geodesic_baseline > 0.0:
            base = itinerary.original_geodesic_baseline
        else:
            base = compute_geodesic_baseline(itinerary)
        
        ratio = min(1.0, base / actual)
        return ratio ** 2

    def compute_hills_score(self, itinerary: Itinerary) -> float:
        """Computes the climbing burden score [0.0, 1.0]."""
        total_climb = sum(leg.ascent_feet for leg in itinerary.legs)
        if total_climb <= 0 and itinerary.schedule:
            total_climb = sum(day.ascent_feet for day in itinerary.schedule)

        travel_days = sum(1 for leg in itinerary.legs)
        if travel_days <= 0 and itinerary.schedule:
            travel_days = sum(1 for day in itinerary.schedule if not day.is_rest_day)

        if travel_days <= 0:
            return 1.0

        max_climb = self.daily_constraints.get("max_climb_ft_per_day", 5000.0)
        if max_climb <= 0:
            max_climb = 5000.0

        max_possible_climb = travel_days * max_climb
        score = 1.0 - (total_climb / max_possible_climb)
        return max(0.0, min(1.0, score))

    def score_itinerary(self, itinerary: Itinerary) -> Itinerary:
        """Calculates and populates the Scores dataclass for an itinerary."""
        w_weather = self.weights.get("weather", 0.45)
        w_dist = self.weights.get("distance", 0.30)
        w_hills = self.weights.get("hills", 0.25)

        s_weather = self.compute_weather_score(itinerary)
        s_dist = self.compute_distance_score(itinerary)
        s_hills = self.compute_hills_score(itinerary)

        total = (w_weather * s_weather) + (w_dist * s_dist) + (w_hills * s_hills)

        itinerary.scores = Scores(
            weather=round(s_weather, 4),
            distance=round(s_dist, 4),
            hills=round(s_hills, 4),
            total=round(total, 4)
        )
        return itinerary

    def rank_itineraries(self, itineraries: List[Itinerary]) -> List[Itinerary]:
        """Ranks itineraries deterministically in descending order of total desirability score."""
        for it in itineraries:
            self.score_itinerary(it)

        def sorting_key(it: Itinerary) -> Tuple[float, float, float, float, str]:
            total_dist = sum(leg.distance_miles for leg in it.legs)
            if total_dist <= 0:
                total_dist = sum(day.distance_miles for day in it.schedule)
                
            total_ascent = sum(leg.ascent_feet for leg in it.legs)
            if total_ascent <= 0:
                total_ascent = sum(day.ascent_feet for day in it.schedule)

            via_names = "-".join(c.name for c in it.via_cities)

            # Negate descendable metrics for default ascending sort key
            return (
                -it.scores.total,
                -it.scores.weather,
                total_dist,
                total_ascent,
                via_names
            )

        return sorted(itineraries, key=sorting_key)
