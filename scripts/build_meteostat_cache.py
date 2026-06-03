#!/usr/bin/env python3
"""
Meteostat Cache Builder
Pre-fetches historical daily temperature data for all registered cities from Meteostat,
computes the day-of-year average high and low temperatures (Fahrenheit) over a 25-year period,
and writes the climatology averages into the SQLite cache database.
Allows the solver to run in fully offline mode using the 'meteostat' weather provider.
"""

import argparse
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import cast, Any, Tuple

# Add project root directory to sys.path to support importing from src
root_dir = Path(__file__).resolve().parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

try:
    from src.cache import SQLiteCacheManager, round_coord
    from src.validation import CITY_REGISTRY
except ImportError as err:
    print(f"Error: Failed to import src modules. Make sure this script is run from the project root: {err}")
    sys.exit(1)


def is_already_cached(cache_manager: SQLiteCacheManager, lat: float, lon: float) -> bool:
    """Checks if the database already contains cached climatology entries for the coordinate."""
    conn = cache_manager._get_conn()
    lat_rounded = round_coord(lat)
    lon_rounded = round_coord(lon)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT COUNT(*) FROM meteostat_climatology WHERE city_lat = ? AND city_lon = ?",
        (lat_rounded, lon_rounded),
    )
    row = cursor.fetchone()
    return row and row[0] > 0


def build_cache_for_city(
    cache_manager: SQLiteCacheManager,
    city_name: str,
    lat: float,
    lon: float,
    start_year: int,
    end_year: int,
    force: bool,
) -> bool:
    """Fetches Meteostat station data, averages tmax/tmin, and caches them in the SQLite DB."""
    if is_already_cached(cache_manager, lat, lon) and not force:
        print(f"Skipping: '{city_name}' (already cached)")
        return True

    # Import meteostat inside function to avoid immediate dependency failures if not installed
    try:
        from meteostat import Point, stations, daily
        import pandas as pd
    except ImportError:
        print("Error: The 'meteostat' and 'pandas' packages must be installed. Run: pip install meteostat")
        sys.exit(1)

    print(f"Processing: '{city_name}' ({lat:.4f}, {lon:.4f})...")

    try:
        # Find closest station
        station_df = stations.nearby(Point(lat, lon))

        if station_df.empty:
            print(f"  Error: No weather stations found near '{city_name}'")
            return False

        station_id = station_df.index[0]
        station_name = station_df["name"].values[0]
        distance = float(station_df.iloc[0]["distance"])
        print(f"  Found station: {station_name} (ID: {station_id}, Distance: {distance/1000:.2f} km)")

        # Fetch daily observations for the specified period
        start = datetime(start_year, 1, 1)
        end = datetime(end_year, 12, 31)
        df = cast(pd.DataFrame, daily(station_id, start, end).fetch())

        if df.empty:
            print(f"  Error: No daily historical records found for station ID {station_id}")
            return False

        # Compute averages grouped by month and day of year
        df["month"] = cast(Any, df.index).month
        df["day"] = cast(Any, df.index).day
        grouped = df.groupby(["month", "day"])[["tmax", "tmin"]].mean()

        climatology_list = []
        for idx, row in grouped.iterrows():
            month_idx, day_idx = cast(Tuple[int, int], idx)
            tmax = row["tmax"]
            tmin = row["tmin"]
            if not pd.isna(tmax) and not pd.isna(tmin):
                climatology_list.append(
                    {
                        "month": month_idx,
                        "day": day_idx,
                        "avg_high_f": round(tmax * 9 / 5 + 32, 1),
                        "avg_low_f": round(tmin * 9 / 5 + 32, 1),
                        "station_id": str(station_id),
                        "station_distance_m": distance,
                    }
                )

        if not climatology_list:
            print(f"  Error: All records were incomplete/NaN for station {station_id}")
            return False

        # Save to SQLite database
        cache_manager.save_meteostat_climatology(lat, lon, climatology_list)
        print(f"  Successfully cached {len(climatology_list)} days of climatology for '{city_name}'.")
        return True

    except Exception as exc:
        print(f"  Failed to build cache for '{city_name}': {exc}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Pre-populate local SQLite database with day-of-year climatology from Meteostat."
    )
    parser.add_argument(
        "--cache-db",
        default=".g2l4a_cache.db",
        help="SQLite cache database file path (default: .g2l4a_cache.db)",
    )
    parser.add_argument(
        "--start-year",
        type=int,
        default=2001,
        help="Start year of historical observations range (default: 2001)",
    )
    parser.add_argument(
        "--end-year",
        type=int,
        default=2025,
        help="End year of historical observations range (default: 2025)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force download and regeneration of cached cities",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose library logging outputs",
    )

    args = parser.parse_args()

    # Configure logging
    log_level = logging.INFO if args.verbose else logging.WARNING
    logging.getLogger("meteostat").setLevel(log_level)

    cache_manager = SQLiteCacheManager(args.cache_db)

    print(f"Starting Meteostat cache pre-fetching (years {args.start_year}-{args.end_year})...")
    print(f"Target Database: {args.cache_db}")
    print(f"Registered Cities: {len(CITY_REGISTRY)}\n")

    success_count = 0
    skipped_count = 0
    failed_count = 0

    try:
        # Group and sort cities to make logs clean
        for city_name, (lat, lon) in sorted(CITY_REGISTRY.items()):
            if is_already_cached(cache_manager, lat, lon) and not args.force:
                skipped_count += 1
                continue

            success = build_cache_for_city(
                cache_manager=cache_manager,
                city_name=city_name,
                lat=lat,
                lon=lon,
                start_year=args.start_year,
                end_year=args.end_year,
                force=args.force,
            )
            if success:
                success_count += 1
            else:
                failed_count += 1
    finally:
        cache_manager.close()

    print("\nSummary:")
    print(f"  Successfully Cached: {success_count}")
    print(f"  Skipped (Up-to-Date): {skipped_count}")
    print(f"  Failed:               {failed_count}")

    return 1 if failed_count > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
