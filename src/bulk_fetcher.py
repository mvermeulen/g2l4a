from typing import List, Tuple, Dict, Any
from concurrent.futures import ThreadPoolExecutor, as_completed
from src.domain import City, Leg
from src.providers import RoutingProvider

class BulkLegFetcher:
    """Helper to query multiple routing legs concurrently using a thread pool."""
    
    def __init__(self, routing_provider: RoutingProvider, concurrency_limit: int = 10):
        self.routing_provider = routing_provider
        self.concurrency_limit = concurrency_limit

    def fetch_legs(self, leg_requests: List[Tuple[City, City, Dict[str, Any]]]) -> List[Leg]:
        """Resolves multiple leg metrics concurrently.
        
        Args:
            leg_requests: A list of (origin, destination, preferences) tuples.
            
        Returns:
            A list of resolved Leg objects in the same order as leg_requests.
        """
        if not leg_requests:
            return []

        results: Dict[int, Leg] = {}
        
        def worker(idx: int, origin: City, dest: City, prefs: Dict[str, Any]) -> Tuple[int, Leg]:
            leg = self.routing_provider.get_leg_metrics(origin, dest, prefs)
            return idx, leg

        # Execute concurrently with capped thread pool size
        max_workers = min(self.concurrency_limit, max(1, len(leg_requests)))
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [
                executor.submit(worker, idx, origin, dest, prefs)
                for idx, (origin, dest, prefs) in enumerate(leg_requests)
            ]
            for future in as_completed(futures):
                idx, leg = future.result()
                results[idx] = leg

        # Assemble list in the original requested order
        return [results[i] for i in range(len(leg_requests))]
