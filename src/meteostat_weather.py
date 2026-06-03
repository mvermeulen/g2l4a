import logging
from datetime import date
from typing import Optional, Tuple, Any, cast

from src.domain import City
from src.mocks import MockWeatherProvider
from src.providers import WeatherProvider, WeatherMetrics
from src.cache import SQLiteCacheManager


class MeteostatWeatherProvider(WeatherProvider):
    """Weather provider backed by Meteostat climatology observations.

    Reads day-of-year historical temperature averages from a local SQLite database.
    If the requested coordinates are not cached locally, dynamically downloads
    the last 25 years of daily observations for the closest weather station,
    aggregates the observations to produce daily means, caches them locally,
    and returns the metrics for the requested day of year.
    """

    def __init__(
        self,
        cache_manager: SQLiteCacheManager,
        fallback_provider: Optional[WeatherProvider] = None,
    ):
        self.cache_manager = cache_manager
        self.fallback_provider = fallback_provider or MockWeatherProvider()

    def get_weather_metrics(
        self, city: City, travel_date: date, current_time: Optional[date] = None
    ) -> WeatherMetrics:
        # Check local climatology cache first
        cached = self.cache_manager.get_meteostat_day_average(
            city.latitude, city.longitude, travel_date.month, travel_date.day
        )
        if cached:
            return {
                "high_temp_f": cached["high_temp_f"],
                "low_temp_f": cached["low_temp_f"],
                "is_forecast": False,
                "source": "meteostat",
            }

        # Cache miss: Attempt dynamic fetch via Meteostat library
        try:
            from datetime import datetime
            import pandas as pd
            from meteostat import Point, stations, daily

            # Disable meteostat console printouts if verbose
            logging.getLogger("meteostat").setLevel(logging.WARNING)

            # Find nearest station
            station_df = stations.nearby(Point(city.latitude, city.longitude))

            if not station_df.empty:
                station_id = station_df.index[0]
                distance = float(station_df.iloc[0]["distance"])

                # Fetch 25 years of daily historical data (e.g. 2001-01-01 to 2025-12-31)
                start = datetime(2001, 1, 1)
                end = datetime(2025, 12, 31)
                df = cast(pd.DataFrame, daily(station_id, start, end).fetch())

                if not df.empty:
                    # Index is datetime; extract month and day
                    df["month"] = cast(Any, df.index).month
                    df["day"] = cast(Any, df.index).day

                    # Compute mean max/min temperature in Celsius
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

                    if climatology_list:
                        # Write the full 366 days of climatology to cache
                        self.cache_manager.save_meteostat_climatology(
                            city.latitude, city.longitude, climatology_list
                        )

                        # Find and return the target day
                        for entry in climatology_list:
                            if (
                                entry["month"] == travel_date.month
                                and entry["day"] == travel_date.day
                            ):
                                return {
                                    "high_temp_f": entry["avg_high_f"],
                                    "low_temp_f": entry["avg_low_f"],
                                    "is_forecast": False,
                                    "source": "meteostat",
                                }
        except Exception as exc:
            logging.warning(
                f"Dynamic Meteostat fetch failed for '{city.name}' ({city.latitude:.4f}, {city.longitude:.4f}): {exc}"
            )

        # Fallback if both cache and remote query failed
        return self.fallback_provider.get_weather_metrics(
            city, travel_date, current_time
        )
