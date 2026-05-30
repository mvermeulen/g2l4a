import time
from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class SolverMetrics:
    """Collects performance, timing, and solver search execution metrics."""
    start_time: float = field(default_factory=time.time)
    duration_ms: float = 0.0
    evaluated_permutations: int = 0
    pruned_branches: int = 0
    routing_api_calls: int = 0
    weather_api_calls: int = 0
    l1_cache_hits: int = 0
    l2_cache_hits: int = 0
    
    def start(self):
        """Starts the timing clock."""
        self.start_time = time.time()
        
    def stop(self):
        """Stops the timing clock and calculates elapsed duration in milliseconds."""
        self.duration_ms = (time.time() - self.start_time) * 1000.0
        
    @property
    def total_cache_lookups(self) -> int:
        return self.l1_cache_hits + self.l2_cache_hits + self.routing_api_calls
        
    @property
    def cache_hit_rate(self) -> float:
        lookups = self.total_cache_lookups
        if lookups == 0:
            return 0.0
        return (self.l1_cache_hits + self.l2_cache_hits) / lookups

    def to_dict(self) -> Dict[str, Any]:
        """Returns standard metrics payload dictionary."""
        return {
            "duration_ms": round(self.duration_ms, 2),
            "evaluated_permutations": self.evaluated_permutations,
            "pruned_branches": self.pruned_branches,
            "routing_api_calls": self.routing_api_calls,
            "weather_api_calls": self.weather_api_calls,
            "l1_cache_hits": self.l1_cache_hits,
            "l2_cache_hits": self.l2_cache_hits,
            "cache_hit_rate": round(self.cache_hit_rate, 4)
        }
