import os
import yaml
from typing import Dict, Any, Optional

# Hardcoded built-in fallback defaults (the absolute safety net)
BUILTIN_DEFAULTS: Dict[str, Any] = {
    "weather_constraints": {
        "max_avg_high_f": 90.0,
        "min_avg_low_f": 24.0,
    },
    "daily_constraints": {
        "max_miles_per_day": 70.0,
        "max_climb_ft_per_day": 5000.0,
    },
    "duration_constraints": {
        "max_total_days": None,
    },
    "solver_constraints": {
        "max_total_cities": 50,
        "max_search_minutes": 10.0,
    },
    "scoring": {
        "weights": {
            "weather": 0.45,
            "distance": 0.30,
            "hills": 0.25,
        },
        "comfort": {
            "ideal_temp_f": 70.0,
            "temp_tolerance_f": 20.0,
        }
    },
    "routing_preferences": {
        "avoid_highways": True,
        "avoid_tolls": True,
        "allow_ferries": True,
        "allow_international_borders": True,
    },
    "routing_provider": {
        "name": "mock",
        "routing_engine_name": "mock",
        "base_url": "http://localhost:8989",
        "profile": "car",
        "timeout_seconds": 12.0,
        "purge_mock_cache": False,
    },
    "weather_provider": {
        "name": "mock",
        "timeout_seconds": 8.0,
        "climate_model": "CMCC_CM2_VHR4",
        "capital_monthly_normals_path": "data/state_capitals_monthly_normals.json",
    },
    "cache": {
        "db_path": ".g2l4a_cache.db",
        "forecast_ttl_hours": 24,
        "climatology_ttl_days": 30,
        "concurrency_limit": 10,
    }
}


def deep_merge(base: Dict[str, Any], overrides: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merges overrides into base."""
    merged = base.copy()
    for key, value in overrides.items():
        if isinstance(value, dict) and key in merged and isinstance(merged[key], dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


class ConfigManager:
    """Handles hierarchical configuration loading with deep-merging.
    
    Hierarchy (highest precedence first):
    1. User input dictionary / YAML file
    2. System defaults YAML file (e.g., config/defaults.yaml)
    3. Built-in hardcoded defaults
    """
    def __init__(self, system_defaults_path: Optional[str] = None):
        self.system_defaults_path = system_defaults_path
        self._system_defaults: Dict[str, Any] = {}
        self._load_system_defaults()

    def _load_system_defaults(self):
        if self.system_defaults_path and os.path.exists(self.system_defaults_path):
            try:
                with open(self.system_defaults_path, "r") as f:
                    data = yaml.safe_load(f)
                    if data:
                        # Accommodate both flat or nested under "defaults" key
                        self._system_defaults = data.get("defaults", data)
            except Exception as e:
                # Fallback to empty if load fails
                self._system_defaults = {}
        else:
            self._system_defaults = {}

    def get_effective_config(self, user_overrides: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Calculates the final effective configuration after merging precedence."""
        # 1. Start with built-in fallbacks
        config = BUILTIN_DEFAULTS.copy()
        
        # 2. Merge system defaults
        if self._system_defaults:
            config = deep_merge(config, self._system_defaults)
            
        # 3. Merge user overrides
        if user_overrides:
            # Handle nesting if user passes a complete request YAML containing non-constraint fields
            # Extract only constraint/preference related structures to merge, or merge full structure
            config = deep_merge(config, user_overrides)
            
        return config
