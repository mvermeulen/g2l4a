import sqlite3
import threading
import hashlib
import json
import os
from datetime import datetime, date, timedelta, timezone
from typing import Optional, Dict, Any, Tuple
from src.domain import City, Leg

def compute_profile_hash(preferences: Dict[str, Any]) -> str:
    """Computes a stable SHA-256 hash of routing preferences."""
    keys_of_interest = {
        "avoid_highways",
        "avoid_tolls",
        "allow_ferries",
        "allow_international_borders"
    }
    # Standardize missing preferences as True
    filtered = {k: preferences.get(k, True) for k in keys_of_interest}
    sorted_prefs = sorted(filtered.items())
    pref_str = json.dumps(sorted_prefs)
    return hashlib.sha256(pref_str.encode('utf-8')).hexdigest()

def round_coord(val: float) -> float:
    """Rounds coordinates to 6 decimal places for key stability."""
    return round(val, 6)

class SQLiteCacheManager:
    """Thread-safe SQLite caching layer for Routing and Weather providers."""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._local = threading.local()
        self._init_db()

    def _get_conn(self) -> sqlite3.Connection:
        if not hasattr(self._local, "conn"):
            # Ensure containing directory exists
            db_dir = os.path.dirname(os.path.abspath(self.db_path))
            if db_dir:
                os.makedirs(db_dir, exist_ok=True)
            self._local.conn = sqlite3.connect(self.db_path)
            self._local.conn.row_factory = sqlite3.Row
        return self._local.conn

    def _init_db(self):
        conn = self._get_conn()
        with conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS routing_cache (
                    origin_lat REAL,
                    origin_lon REAL,
                    dest_lat REAL,
                    dest_lon REAL,
                    routing_engine TEXT,
                    profile_hash TEXT,
                    source TEXT,
                    distance_miles REAL,
                    ascent_feet REAL,
                    is_bicycle_legal INTEGER,
                    avoided_highways INTEGER,
                    avoided_tolls INTEGER,
                    allowed_ferries INTEGER,
                    allowed_borders INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (origin_lat, origin_lon, dest_lat, dest_lon, routing_engine, profile_hash)
                )
            """)
            # Lightweight schema migration for older caches created before `source` existed.
            cols = {
                row["name"]
                for row in conn.execute("PRAGMA table_info(routing_cache)")
            }
            if "source" not in cols:
                conn.execute("ALTER TABLE routing_cache ADD COLUMN source TEXT")
            conn.execute("UPDATE routing_cache SET source = 'unknown' WHERE source IS NULL")
            conn.execute("""
                CREATE TABLE IF NOT EXISTS weather_cache (
                    city_lat REAL,
                    city_lon REAL,
                    travel_date TEXT,
                    high_temp_f REAL,
                    low_temp_f REAL,
                    is_forecast INTEGER,
                    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (city_lat, city_lon, travel_date, is_forecast)
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS weather_cache_v2 (
                    city_lat REAL,
                    city_lon REAL,
                    travel_date TEXT,
                    high_temp_f REAL,
                    low_temp_f REAL,
                    is_forecast INTEGER,
                    provider_key TEXT,
                    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (city_lat, city_lon, travel_date, is_forecast, provider_key)
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS meteostat_climatology (
                    city_lat REAL,
                    city_lon REAL,
                    month INTEGER,
                    day INTEGER,
                    avg_high_f REAL,
                    avg_low_f REAL,
                    station_id TEXT,
                    station_distance_m REAL,
                    PRIMARY KEY (city_lat, city_lon, month, day)
                )
            """)

    def close(self):
        """Closes the thread-local database connection if it exists."""
        if hasattr(self._local, "conn"):
            self._local.conn.close()
            del self._local.conn

    # --- Routing Cache Operations ---

    def get_leg(
        self,
        origin: City,
        destination: City,
        routing_engine: str,
        preferences: Dict[str, Any],
        source: Optional[str] = None,
    ) -> Optional[Leg]:
        """Retrieves a cached Leg if available."""
        conn = self._get_conn()
        o_lat = round_coord(origin.latitude)
        o_lon = round_coord(origin.longitude)
        d_lat = round_coord(destination.latitude)
        d_lon = round_coord(destination.longitude)
        p_hash = compute_profile_hash(preferences)

        cursor = conn.cursor()
        if source is None:
            cursor.execute(
                """
                SELECT distance_miles, ascent_feet, is_bicycle_legal, avoided_highways, avoided_tolls, allowed_ferries, allowed_borders
                FROM routing_cache
                WHERE origin_lat = ? AND origin_lon = ? AND dest_lat = ? AND dest_lon = ?
                  AND routing_engine = ? AND profile_hash = ?
                """,
                (o_lat, o_lon, d_lat, d_lon, routing_engine, p_hash),
            )
        else:
            cursor.execute(
                """
                SELECT distance_miles, ascent_feet, is_bicycle_legal, avoided_highways, avoided_tolls, allowed_ferries, allowed_borders
                FROM routing_cache
                WHERE origin_lat = ? AND origin_lon = ? AND dest_lat = ? AND dest_lon = ?
                  AND routing_engine = ? AND profile_hash = ? AND source = ?
                """,
                (o_lat, o_lon, d_lat, d_lon, routing_engine, p_hash, source),
            )
        
        row = cursor.fetchone()
        if row:
            return Leg(
                origin=origin,
                destination=destination,
                distance_miles=row["distance_miles"],
                ascent_feet=row["ascent_feet"],
                is_bicycle_legal=bool(row["is_bicycle_legal"]),
                avoided_highways=bool(row["avoided_highways"]),
                avoided_tolls=bool(row["avoided_tolls"]),
                allowed_ferries=bool(row["allowed_ferries"]),
                allowed_borders=bool(row["allowed_borders"])
            )
        return None

    def save_leg(self, leg: Leg, routing_engine: str, preferences: Dict[str, Any], source: str = "unknown"):
        """Saves a Leg into the cache."""
        conn = self._get_conn()
        o_lat = round_coord(leg.origin.latitude)
        o_lon = round_coord(leg.origin.longitude)
        d_lat = round_coord(leg.destination.latitude)
        d_lon = round_coord(leg.destination.longitude)
        p_hash = compute_profile_hash(preferences)

        with conn:
            conn.execute("""
                INSERT OR REPLACE INTO routing_cache (
                    origin_lat, origin_lon, dest_lat, dest_lon, routing_engine, profile_hash,
                    source, distance_miles, ascent_feet, is_bicycle_legal, avoided_highways, avoided_tolls,
                    allowed_ferries, allowed_borders, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            """, (
                o_lat, o_lon, d_lat, d_lon, routing_engine, p_hash,
                source,
                leg.distance_miles, leg.ascent_feet, int(leg.is_bicycle_legal),
                int(leg.avoided_highways), int(leg.avoided_tolls),
                int(leg.allowed_ferries), int(leg.allowed_borders)
            ))

    def purge_routing_cache_by_engine(self, routing_engine: str) -> int:
        """Deletes cached routing rows for an exact routing engine key."""
        conn = self._get_conn()
        with conn:
            cursor = conn.execute(
                "DELETE FROM routing_cache WHERE routing_engine = ?",
                (routing_engine,),
            )
        return int(cursor.rowcount)

    def purge_routing_cache_by_source(self, source: str) -> int:
        """Deletes cached routing rows for a given source/provider tag."""
        conn = self._get_conn()
        with conn:
            cursor = conn.execute(
                "DELETE FROM routing_cache WHERE source = ?",
                (source,),
            )
        return int(cursor.rowcount)

    # --- Weather Cache Operations ---

    def get_weather(
        self,
        city: City,
        travel_date: date,
        is_forecast: bool,
        ttl_hours: int,
        provider_key: str = "default",
    ) -> Optional[Dict[str, Any]]:
        """Retrieves cached weather metrics if not expired."""
        conn = self._get_conn()
        c_lat = round_coord(city.latitude)
        c_lon = round_coord(city.longitude)
        date_str = travel_date.isoformat()
        is_fc_int = 1 if is_forecast else 0

        cursor = conn.cursor()
        cursor.execute("""
            SELECT high_temp_f, low_temp_f, fetched_at
            FROM weather_cache_v2
            WHERE city_lat = ? AND city_lon = ? AND travel_date = ? AND is_forecast = ? AND provider_key = ?
        """, (c_lat, c_lon, date_str, is_fc_int, provider_key))

        row = cursor.fetchone()
        if row:
            fetched_at_str = row["fetched_at"]
            # Parse fetched_at string. Format: "YYYY-MM-DD HH:MM:SS" or similar ISO
            # SQLite CURRENT_TIMESTAMP is "YYYY-MM-DD HH:MM:SS"
            try:
                fetched_at = datetime.strptime(fetched_at_str, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                # Fallback if SQLite returned it in another ISO format
                try:
                    fetched_at = datetime.fromisoformat(fetched_at_str)
                except ValueError:
                    # In case of any parsing issues, treat as cache miss
                    return None

            age = datetime.now(timezone.utc).replace(tzinfo=None) - fetched_at
            if age > timedelta(hours=ttl_hours):
                # Expired cache entry, prune it
                with conn:
                    conn.execute("""
                        DELETE FROM weather_cache_v2
                        WHERE city_lat = ? AND city_lon = ? AND travel_date = ? AND is_forecast = ? AND provider_key = ?
                    """, (c_lat, c_lon, date_str, is_fc_int, provider_key))
                return None

            return {
                "high_temp_f": row["high_temp_f"],
                "low_temp_f": row["low_temp_f"],
                "is_forecast": is_forecast
            }
        return None

    def save_weather(self, city: City, travel_date: date, metrics: Dict[str, Any], provider_key: str = "default"):
        """Saves weather metrics into the cache."""
        conn = self._get_conn()
        c_lat = round_coord(city.latitude)
        c_lon = round_coord(city.longitude)
        date_str = travel_date.isoformat()
        is_forecast = 1 if metrics.get("is_forecast", False) else 0

        with conn:
            conn.execute("""
                INSERT OR REPLACE INTO weather_cache_v2 (
                    city_lat, city_lon, travel_date, is_forecast, provider_key, high_temp_f, low_temp_f, fetched_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            """, (
                c_lat, c_lon, date_str, is_forecast,
                provider_key, metrics["high_temp_f"], metrics["low_temp_f"]
            ))

    def get_meteostat_day_average(self, lat: float, lon: float, month: int, day: int) -> Optional[Dict[str, float]]:
        """Retrieves cached day-of-year average temperatures from Meteostat climatology."""
        conn = self._get_conn()
        lat_rounded = round_coord(lat)
        lon_rounded = round_coord(lon)
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT avg_high_f, avg_low_f
            FROM meteostat_climatology
            WHERE city_lat = ? AND city_lon = ? AND month = ? AND day = ?
            """,
            (lat_rounded, lon_rounded, month, day)
        )
        row = cursor.fetchone()
        if row:
            return {
                "high_temp_f": row["avg_high_f"],
                "low_temp_f": row["avg_low_f"]
            }
        return None

    def save_meteostat_climatology(self, lat: float, lon: float, climatology: list):
        """Saves daily climatology list (e.g. 366 days) in a single transaction."""
        conn = self._get_conn()
        lat_rounded = round_coord(lat)
        lon_rounded = round_coord(lon)
        with conn:
            conn.executemany(
                """
                INSERT OR REPLACE INTO meteostat_climatology (
                    city_lat, city_lon, month, day, avg_high_f, avg_low_f, station_id, station_distance_m
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                [
                    (
                        lat_rounded,
                        lon_rounded,
                        item["month"],
                        item["day"],
                        item["avg_high_f"],
                        item["avg_low_f"],
                        item["station_id"],
                        item["station_distance_m"]
                    )
                    for item in climatology
                ]
            )
