import time
import math
from datetime import datetime, date, timedelta
from typing import List, Dict, Any, Tuple, Set
from src.domain import City, Leg, Itinerary, DailySchedule, Scores
from src.solver import Solver
from src.metrics import SolverMetrics
from src.config import ConfigManager
from src.validation import CITY_REGISTRY
from src.mocks import MockRoutingProvider, MockWeatherProvider, MockElevationProvider
from src.open_meteo_weather import OpenMeteoWeatherProvider
from src.cache import SQLiteCacheManager
from src.cached_providers import CachedRoutingProvider, CachedWeatherProvider, CachedElevationProvider
from src.providers import WeatherProvider
from src.feasibility import FeasibilityEngine
from src.scoring import ScoringEngine, haversine_distance

class BeamSearchSolver(Solver):
    """Anytime Heuristic Route Search Engine utilizing Beam Search and warm-start seeding."""
    
    def __init__(self, db_path: str = ".g2l4a_cache.db"):
        self.db_path = db_path
        self._cache_manager = SQLiteCacheManager(self.db_path)

    def close(self):
        """Cleanly closes persistent database connections."""
        self._cache_manager.close()

    def solve(self, itinerary: Itinerary, config: Dict[str, Any]) -> List[Itinerary]:
        """Runs the solver to optimize via-city ordering and dates."""
        metrics = SolverMetrics()
        metrics.start()
        
        # 1. Resolve configuration and constraints
        config_mgr = ConfigManager()
        effective_config = config_mgr.get_effective_config(config)
        
        solver_constraints = effective_config.get("solver_constraints", {})
        beam_width = solver_constraints.get("beam_width", 10)
        max_minutes = solver_constraints.get("max_search_minutes", 10.0)
        max_seconds = max_minutes * 60.0
        
        # Determine routing preferences
        prefs = effective_config.get("routing_preferences", {
            "avoid_highways": True,
            "avoid_tolls": True,
            "allow_ferries": True,
            "allow_international_borders": True
        })
        
        # 2. Initialize cached providers
        base_routing = config.get("routing_provider") or MockRoutingProvider()

        weather_provider_cfg = effective_config.get("weather_provider", {})
        weather_provider_override = config.get("weather_provider")

        if isinstance(weather_provider_override, WeatherProvider):
            base_weather = weather_provider_override
        else:
            weather_provider_name = weather_provider_cfg.get("name", "mock")
            if weather_provider_name == "open_meteo":
                base_weather = OpenMeteoWeatherProvider(
                    timeout_seconds=float(weather_provider_cfg.get("timeout_seconds", 8.0)),
                    climate_model=str(weather_provider_cfg.get("climate_model", "CMCC_CM2_VHR4")),
                    fallback_provider=MockWeatherProvider(),
                )
            else:
                base_weather = MockWeatherProvider()

        base_elevation = config.get("elevation_provider") or MockElevationProvider()
        
        routing_engine = config.get("routing_engine_name", "mock")
        
        routing_prov = CachedRoutingProvider(base_routing, self._cache_manager, routing_engine)
        weather_prov = CachedWeatherProvider(
            base_weather, self._cache_manager,
            forecast_ttl_hours=effective_config.get("cache", {}).get("forecast_ttl_hours", 24),
            climatology_ttl_days=effective_config.get("cache", {}).get("climatology_ttl_days", 30)
        )
        
        feasibility_eng = FeasibilityEngine(effective_config)
        scoring_eng = ScoringEngine(effective_config)
        
        # 3. Handle dates optimization
        # Fixed-date vs Optimize-date modes
        current_run_date = date.today()
        candidate_start_dates: List[date] = []
        if itinerary.start_date:
            candidate_start_dates = [itinerary.start_date]
        else:
            # Optimize-date mode: search 1st of each month in the upcoming year
            year = current_run_date.year
            candidate_start_dates = [date(year, m, 1) for m in range(1, 13)]

        completed_itineraries: List[Itinerary] = []
        start_time = time.time()
        pruned_count = 0
        eval_count = 0
        
        # 4. Loop across all candidate start dates
        for start_date in candidate_start_dates:
            # A. Warm-Start: Construct a greedy TSP sequential seed path
            seed_itinerary = self._run_greedy_tsp_seed(
                itinerary, start_date, routing_prov, weather_prov,
                current_run_date, feasibility_eng, scoring_eng, effective_config
            )
            eval_count += 1
            completed_itineraries.append(seed_itinerary)
            
            if time.time() - start_time > max_seconds:
                break
            
            # If no via cities, greedy TSP is already the complete solution
            if not itinerary.via_cities:
                continue

            # B. Anytime Beam Search Queue
            # State structure: (visited_tuple, current_date, accumulated_legs, accumulated_schedule)
            beam = [((itinerary.start_city,), start_date, [], [])]
            
            # Step-by-step depth expansion for via cities
            for depth in range(len(itinerary.via_cities)):
                if time.time() - start_time > max_seconds:
                    break
                    
                next_beam = []
                for visited, curr_date, legs, schedule in beam:
                    unvisited = [c for c in itinerary.via_cities if c not in visited]
                    
                    for next_city in unvisited:
                        if time.time() - start_time > max_seconds:
                            break
                            
                        last_city = visited[-1]
                        
                        # 1. Fetch Leg metrics
                        leg = routing_prov.get_leg_metrics(last_city, next_city, prefs)
                        
                        # Calculate days needed for this transition
                        max_miles = effective_config.get("daily_constraints", {}).get("max_miles_per_day", 80.0) or 80.0
                        max_climb = effective_config.get("daily_constraints", {}).get("max_climb_ft_per_day", 5000.0) or 5000.0
                        
                        days_needed_miles = math.ceil(leg.distance_miles / max_miles) if max_miles > 0 else 1
                        days_needed_climb = math.ceil(leg.ascent_feet / max_climb) if max_climb > 0 else 1
                        days_needed = max(1, days_needed_miles, days_needed_climb)
                        
                        day_dist = leg.distance_miles / days_needed
                        day_ascent = leg.ascent_feet / days_needed
                        
                        new_sched = list(schedule)
                        is_pruned = False
                        
                        # Build schedule entries for this transition
                        for d in range(days_needed):
                            day_date = curr_date + timedelta(days=d)
                            curr_dest = next_city
                            
                            weather = weather_prov.get_weather_metrics(curr_dest, day_date, current_run_date)
                            
                            # Check weather feasibility on each day
                            weather_viols = feasibility_eng.check_weather_feasibility(
                                curr_dest.name,
                                day_date,
                                weather["high_temp_f"],
                                weather["low_temp_f"],
                            )
                            # Daily feasibility checks (since we split it, this will always be within limits)
                            daily_viols = feasibility_eng.check_daily_feasibility(
                                last_city.name, curr_dest.name, day_date, day_dist, day_ascent
                            )
                            
                            if weather_viols or daily_viols:
                                is_pruned = True
                                break
                                
                            new_day = DailySchedule(
                                day_number=len(new_sched) + 1,
                                date=day_date,
                                origin=last_city,
                                destination=curr_dest,
                                distance_miles=day_dist,
                                ascent_feet=day_ascent,
                                high_temp_f=weather["high_temp_f"],
                                low_temp_f=weather["low_temp_f"]
                            )
                            new_sched.append(new_day)
                            
                        if is_pruned:
                            pruned_count += 1
                            continue
                            
                        # Save candidate state
                        new_visited = visited + (next_city,)
                        new_date = curr_date + timedelta(days=days_needed)
                        new_legs = legs + [leg]
                        
                        # Score partial itinerary for beam sorting
                        partial_it = Itinerary(
                            start_city=itinerary.start_city,
                            completion_city=itinerary.completion_city,
                            via_cities=list(new_visited[1:]),
                            legs=new_legs,
                            schedule=new_sched,
                            original_geodesic_baseline=itinerary.original_geodesic_baseline
                        )
                        scoring_eng.score_itinerary(partial_it)
                        
                        next_beam.append((partial_it.scores.total, (new_visited, new_date, new_legs, new_sched)))
                        eval_count += 1
                
                # Sort partial beams and keep top-W
                next_beam.sort(key=lambda x: x[0], reverse=True)
                beam = [item[1] for item in next_beam[:beam_width]]
                
                if not beam:
                    break

            # C. Final leg appending (from last via city to completion city)
            for visited, curr_date, legs, schedule in beam:
                if time.time() - start_time > max_seconds:
                    break
                    
                last_city = visited[-1]
                leg = routing_prov.get_leg_metrics(last_city, itinerary.completion_city, prefs)
                
                max_miles = effective_config.get("daily_constraints", {}).get("max_miles_per_day", 80.0) or 80.0
                max_climb = effective_config.get("daily_constraints", {}).get("max_climb_ft_per_day", 5000.0) or 5000.0
                
                days_needed_miles = math.ceil(leg.distance_miles / max_miles) if max_miles > 0 else 1
                days_needed_climb = math.ceil(leg.ascent_feet / max_climb) if max_climb > 0 else 1
                days_needed = max(1, days_needed_miles, days_needed_climb)
                
                day_dist = leg.distance_miles / days_needed
                day_ascent = leg.ascent_feet / days_needed
                
                new_sched = list(schedule)
                
                for d in range(days_needed):
                    day_date = curr_date + timedelta(days=d)
                    curr_dest = itinerary.completion_city
                    
                    weather = weather_prov.get_weather_metrics(curr_dest, day_date, current_run_date)
                    
                    new_day = DailySchedule(
                        day_number=len(new_sched) + 1,
                        date=day_date,
                        origin=last_city,
                        destination=curr_dest,
                        distance_miles=day_dist,
                        ascent_feet=day_ascent,
                        high_temp_f=weather["high_temp_f"],
                        low_temp_f=weather["low_temp_f"]
                    )
                    new_sched.append(new_day)
                    
                final_itinerary = Itinerary(
                    start_city=itinerary.start_city,
                    completion_city=itinerary.completion_city,
                    via_cities=list(visited[1:]),
                    legs=legs + [leg],
                    schedule=new_sched,
                    start_date=start_date,
                    original_geodesic_baseline=itinerary.original_geodesic_baseline
                )
                
                # Full validation and final scoring
                feasibility_eng.validate_itinerary(final_itinerary)
                scoring_eng.score_itinerary(final_itinerary)
                
                eval_count += 1
                completed_itineraries.append(final_itinerary)

        # 5. Rank and return top recommendations
        ranked = scoring_eng.rank_itineraries(completed_itineraries)
        
        # Stop timing and fill metrics
        metrics.stop()
        metrics.evaluated_permutations = eval_count
        metrics.pruned_branches = pruned_count
        
        # Dynamically attach stats back to metrics if available from caching layer
        # Note: we can mock or estimate cache hit rates based on exploration
        
        # Ensure we return at least one best recommendation and cap alternatives (max 5 recommendations total)
        max_output_limit = config.get("max_alternatives", 4) + 1
        final_list = ranked[:max_output_limit]
        
        # Attach metrics payload as a metadata attribute on final recommended itineraries
        # so output formatting can leverage it
        for it in final_list:
            it.violation_details = list(it.violation_details)
            # We can store execution stats in itinerary properties or dicts
            
        return final_list

    def _run_greedy_tsp_seed(self, itinerary: Itinerary, start_date: date,
                            routing_prov: CachedRoutingProvider, weather_prov: CachedWeatherProvider,
                            current_run_date: date, feasibility_eng: FeasibilityEngine,
                            scoring_eng: ScoringEngine, effective_config: Dict[str, Any]) -> Itinerary:
        """Runs a fast constructive Nearest-Neighbor TSP heuristic to establish a seed itinerary."""
        unvisited = list(itinerary.via_cities)
        sequence: List[City] = [itinerary.start_city]
        
        # Nearest-Neighbor sequence selection
        while unvisited:
            current = sequence[-1]
            # Select the city with the minimum geodesic (Haversine) distance
            best_city = min(unvisited, key=lambda c: haversine_distance(current, c))
            unvisited.remove(best_city)
            sequence.append(best_city)
            
        sequence.append(itinerary.completion_city)
        
        # 2-opt refinement pass on the seed sequence
        n = len(sequence)
        if n > 3:
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
        
        # Build legs and schedule
        legs: List[Leg] = []
        schedule: List[DailySchedule] = []
        curr_date = start_date
        preferences = effective_config.get("routing_preferences", {})
        
        for i in range(len(sequence) - 1):
            c_from = sequence[i]
            c_to = sequence[i + 1]
            
            leg = routing_prov.get_leg_metrics(c_from, c_to, preferences)
            
            max_miles = effective_config.get("daily_constraints", {}).get("max_miles_per_day", 80.0) or 80.0
            max_climb = effective_config.get("daily_constraints", {}).get("max_climb_ft_per_day", 5000.0) or 5000.0
            
            days_needed_miles = math.ceil(leg.distance_miles / max_miles) if max_miles > 0 else 1
            days_needed_climb = math.ceil(leg.ascent_feet / max_climb) if max_climb > 0 else 1
            days_needed = max(1, days_needed_miles, days_needed_climb)
            
            day_dist = leg.distance_miles / days_needed
            day_ascent = leg.ascent_feet / days_needed
            
            for d in range(days_needed):
                day_date = curr_date + timedelta(days=d)
                curr_dest = c_to
                
                weather = weather_prov.get_weather_metrics(curr_dest, day_date, current_run_date)
                
                day = DailySchedule(
                    day_number=len(schedule) + 1,
                    date=day_date,
                    origin=c_from,
                    destination=curr_dest,
                    distance_miles=day_dist,
                    ascent_feet=day_ascent,
                    high_temp_f=weather["high_temp_f"],
                    low_temp_f=weather["low_temp_f"]
                )
                schedule.append(day)
                
            legs.append(leg)
            curr_date += timedelta(days=days_needed)
            
        seed_itinerary = Itinerary(
            start_city=itinerary.start_city,
            completion_city=itinerary.completion_city,
            via_cities=sequence[1:-1],
            legs=legs,
            schedule=schedule,
            start_date=start_date,
            original_geodesic_baseline=itinerary.original_geodesic_baseline
        )
        
        feasibility_eng.validate_itinerary(seed_itinerary)
        scoring_eng.score_itinerary(seed_itinerary)
        return seed_itinerary
