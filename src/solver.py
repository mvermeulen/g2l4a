from abc import ABC, abstractmethod
from typing import List, Dict, Any
from src.domain import Itinerary

class Solver(ABC):
    """Abstract Base Class representing the route sequence solver interface."""
    
    @abstractmethod
    def solve(self, itinerary: Itinerary, config: Dict[str, Any]) -> List[Itinerary]:
        """Runs the solver to optimize via-city ordering and dates.
        
        Returns a ranked list of feasible Itineraries (best recommendation first) 
        plus alternative recommendations up to the configured limit.
        """
        pass
