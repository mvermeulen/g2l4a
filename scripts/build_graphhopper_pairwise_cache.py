#!/usr/bin/env python3
"""Build a pairwise GraphHopper route matrix and export DB-importable SQL.

This script assumes a running GraphHopper endpoint. By default it uses the
cities in data/state_capitals_monthly_normals.json (50 state capitals +
Washington, DC + Chicago).

Outputs:
- JSON records with route metrics
- CSV for ad-hoc inspection
- Readable text report
- SQL script with INSERT OR REPLACE statements for routing_cache

Example:
    python scripts/build_graphhopper_pairwise_cache.py \
      --base-url http://localhost:8989 \
      --profile bike \
      --db-import-sql data/state_capitals_pairwise_import.sql
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime, timezone
from itertools import permutations
from pathlib import Path
from typing import Iterable

# Allow running this script directly from arbitrary working directories.
REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.cache import compute_profile_hash
from src.domain import City
from src.graphhopper_routing import GraphHopperRoutingProvider
from src.validation import CITY_REGISTRY


DEFAULT_DATASET_PATH = Path("data/state_capitals_monthly_normals.json")
DEFAULT_JSON_PATH = Path("data/state_capitals_pairwise_graphhopper.json")
DEFAULT_CSV_PATH = Path("data/state_capitals_pairwise_graphhopper.csv")
DEFAULT_TEXT_REPORT_PATH = Path("reports/state_capitals_pairwise_graphhopper.txt")
DEFAULT_SQL_PATH = Path("data/state_capitals_pairwise_graphhopper_import.sql")

# Keep defaults aligned with cache behavior where missing preferences resolve to True.
DEFAULT_PREFERENCES = {
    "avoid_highways": True,
    "avoid_tolls": True,
    "allow_ferries": True,
    "allow_international_borders": True,
}


@dataclass(frozen=True)
class RouteRecord:
    origin_name: str
    origin_lat: float
    origin_lon: float
    dest_name: str
    dest_lat: float
    dest_lon: float
    distance_miles: float
    ascent_feet: float


def _load_default_city_names(dataset_path: Path) -> list[str]:
    payload = json.loads(dataset_path.read_text(encoding="utf-8"))
    cities = payload.get("cities", {})
    if not isinstance(cities, dict) or not cities:
        raise RuntimeError(f"No city dataset found in {dataset_path}")
    return list(cities.keys())


def _load_city_names(cities_file: Path | None, dataset_path: Path) -> list[str]:
    if cities_file is None:
        return _load_default_city_names(dataset_path)

    suffix = cities_file.suffix.lower()
    raw = cities_file.read_text(encoding="utf-8")
    if suffix == ".json":
        data = json.loads(raw)
        if isinstance(data, dict) and "cities" in data and isinstance(data["cities"], list):
            names = data["cities"]
        elif isinstance(data, list):
            names = data
        else:
            raise RuntimeError("JSON cities file must be a list or an object with a 'cities' list")
    else:
        names = [line.strip() for line in raw.splitlines() if line.strip() and not line.strip().startswith("#")]

    cleaned = [str(name).strip() for name in names if str(name).strip()]
    if not cleaned:
        raise RuntimeError(f"No cities found in {cities_file}")
    return cleaned


def _normalize_city_key(name: str) -> str:
    return name.strip().lower()


def _resolve_cities(city_names: Iterable[str]) -> tuple[list[City], list[str]]:
    resolved: list[City] = []
    skipped: list[str] = []
    seen: set[str] = set()

    for name in city_names:
        key = _normalize_city_key(name)
        if key in seen:
            continue
        seen.add(key)

        if key not in CITY_REGISTRY:
            skipped.append(name)
            continue

        lat, lon = CITY_REGISTRY[key]
        resolved.append(City(name=name, latitude=lat, longitude=lon))

    return resolved, skipped


def _pairwise_directed(cities: list[City]) -> Iterable[tuple[City, City]]:
    return permutations(cities, 2)


def _fetch_route(
    provider: GraphHopperRoutingProvider,
    origin: City,
    destination: City,
) -> RouteRecord:
    leg = provider.get_leg_metrics(origin, destination, preferences=DEFAULT_PREFERENCES)
    return RouteRecord(
        origin_name=origin.name,
        origin_lat=origin.latitude,
        origin_lon=origin.longitude,
        dest_name=destination.name,
        dest_lat=destination.latitude,
        dest_lon=destination.longitude,
        distance_miles=float(leg.distance_miles),
        ascent_feet=float(leg.ascent_feet),
    )


def _write_json(path: Path, records: list[RouteRecord], metadata: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "metadata": metadata,
        "routes": [
            {
                "origin": {
                    "name": rec.origin_name,
                    "latitude": rec.origin_lat,
                    "longitude": rec.origin_lon,
                },
                "destination": {
                    "name": rec.dest_name,
                    "latitude": rec.dest_lat,
                    "longitude": rec.dest_lon,
                },
                "distance_miles": round(rec.distance_miles, 6),
                "ascent_feet": round(rec.ascent_feet, 6),
            }
            for rec in records
        ],
    }
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _write_csv(path: Path, records: list[RouteRecord]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "origin_name",
                "origin_lat",
                "origin_lon",
                "dest_name",
                "dest_lat",
                "dest_lon",
                "distance_miles",
                "ascent_feet",
            ]
        )
        for rec in records:
            writer.writerow(
                [
                    rec.origin_name,
                    f"{rec.origin_lat:.6f}",
                    f"{rec.origin_lon:.6f}",
                    rec.dest_name,
                    f"{rec.dest_lat:.6f}",
                    f"{rec.dest_lon:.6f}",
                    f"{rec.distance_miles:.6f}",
                    f"{rec.ascent_feet:.6f}",
                ]
            )


def _sql_quote(value: str) -> str:
    return value.replace("'", "''")


def _write_sql(
    path: Path,
    records: list[RouteRecord],
    routing_engine: str,
    source: str,
    profile_hash: str,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    lines: list[str] = []
    lines.append("BEGIN TRANSACTION;")
    lines.append(
        "CREATE TABLE IF NOT EXISTS routing_cache ("
        "origin_lat REAL,"
        "origin_lon REAL,"
        "dest_lat REAL,"
        "dest_lon REAL,"
        "routing_engine TEXT,"
        "profile_hash TEXT,"
        "source TEXT,"
        "distance_miles REAL,"
        "ascent_feet REAL,"
        "is_bicycle_legal INTEGER,"
        "avoided_highways INTEGER,"
        "avoided_tolls INTEGER,"
        "allowed_ferries INTEGER,"
        "allowed_borders INTEGER,"
        "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
        "PRIMARY KEY (origin_lat, origin_lon, dest_lat, dest_lon, routing_engine, profile_hash)"
        ");"
    )
    engine_q = _sql_quote(routing_engine)
    source_q = _sql_quote(source)
    hash_q = _sql_quote(profile_hash)

    for rec in records:
        lines.append(
            "INSERT OR REPLACE INTO routing_cache ("
            "origin_lat, origin_lon, dest_lat, dest_lon, routing_engine, profile_hash, source, "
            "distance_miles, ascent_feet, is_bicycle_legal, avoided_highways, avoided_tolls, "
            "allowed_ferries, allowed_borders, created_at"
            ") VALUES ("
            f"{rec.origin_lat:.6f}, {rec.origin_lon:.6f}, {rec.dest_lat:.6f}, {rec.dest_lon:.6f}, "
            f"'{engine_q}', '{hash_q}', '{source_q}', "
            f"{rec.distance_miles:.6f}, {rec.ascent_feet:.6f}, "
            "1, 1, 1, 1, 1, CURRENT_TIMESTAMP"
            ");"
        )

    lines.append("COMMIT;")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_text_report(
    path: Path,
    records: list[RouteRecord],
    city_count: int,
    skipped: list[str],
    errors: list[str],
    metadata: dict[str, object],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    lines: list[str] = []
    lines.append("GraphHopper Pairwise Route Export")
    lines.append("=" * 32)
    lines.append(f"Generated (UTC): {metadata['generated_at_utc']}")
    lines.append(f"Base URL: {metadata['graphhopper_base_url']}")
    lines.append(f"Profile: {metadata['graphhopper_profile']}")
    lines.append(f"Cities resolved: {city_count}")
    lines.append(f"Directed routes exported: {len(records)}")
    lines.append(f"Skipped cities: {len(skipped)}")
    lines.append(f"Route errors: {len(errors)}")
    lines.append("")

    if skipped:
        lines.append("Skipped cities (not in CITY_REGISTRY):")
        lines.extend(f"- {name}" for name in skipped)
        lines.append("")

    if errors:
        lines.append("Route errors:")
        lines.extend(f"- {err}" for err in errors)
        lines.append("")

    lines.append("Routes (origin -> destination):")
    for rec in records:
        lines.append(
            f"- {rec.origin_name} -> {rec.dest_name}: "
            f"{rec.distance_miles:.2f} miles, {rec.ascent_feet:.0f} ft ascent"
        )

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", default="http://localhost:8989", help="GraphHopper base URL")
    parser.add_argument("--profile", default="bike", help="GraphHopper routing profile")
    parser.add_argument(
        "--dataset-path",
        default=str(DEFAULT_DATASET_PATH),
        help="Dataset used for default city list when --cities-file is not set",
    )
    parser.add_argument(
        "--cities-file",
        default=None,
        help="Optional city list (.txt or .json). Defaults to cities from dataset.",
    )
    parser.add_argument("--json-out", default=str(DEFAULT_JSON_PATH), help="Output JSON path")
    parser.add_argument("--csv-out", default=str(DEFAULT_CSV_PATH), help="Output CSV path")
    parser.add_argument("--text-out", default=str(DEFAULT_TEXT_REPORT_PATH), help="Readable text report path")
    parser.add_argument("--db-import-sql", default=str(DEFAULT_SQL_PATH), help="SQL import script output path")
    parser.add_argument("--routing-engine", default="graphhopper", help="routing_cache.routing_engine value")
    parser.add_argument("--source", default="graphhopper-precompute", help="routing_cache.source value")
    parser.add_argument("--workers", type=int, default=8, help="Parallel worker count")
    parser.add_argument(
        "--fail-fast",
        action="store_true",
        help="Stop immediately on the first route request failure",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()

    dataset_path = Path(args.dataset_path)
    cities_file = Path(args.cities_file) if args.cities_file else None
    json_out = Path(args.json_out)
    csv_out = Path(args.csv_out)
    text_out = Path(args.text_out)
    sql_out = Path(args.db_import_sql)

    city_names = _load_city_names(cities_file, dataset_path)
    cities, skipped = _resolve_cities(city_names)
    if len(cities) < 2:
        raise RuntimeError("Need at least two resolvable cities to compute pairwise routes")

    pairs = list(_pairwise_directed(cities))
    total_pairs = len(pairs)

    provider = GraphHopperRoutingProvider(base_url=args.base_url, profile=args.profile)
    records: list[RouteRecord] = []
    errors: list[str] = []

    print(f"Resolved {len(cities)} cities ({len(skipped)} skipped).")
    print(f"Requesting {total_pairs} directed routes from GraphHopper...")

    futures = {}
    completed = 0
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        for origin, dest in pairs:
            future = executor.submit(_fetch_route, provider, origin, dest)
            futures[future] = (origin.name, dest.name)

        for future in as_completed(futures):
            completed += 1
            origin_name, dest_name = futures[future]
            try:
                records.append(future.result())
            except Exception as exc:  # noqa: BLE001
                msg = f"{origin_name} -> {dest_name}: {exc}"
                errors.append(msg)
                print(f"ERROR {msg}")
                if args.fail_fast:
                    raise

            if completed % 100 == 0 or completed == total_pairs:
                print(f"Progress: {completed}/{total_pairs}")

    records.sort(key=lambda rec: (rec.origin_name.lower(), rec.dest_name.lower()))

    profile_hash = compute_profile_hash(DEFAULT_PREFERENCES)
    metadata = {
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "graphhopper_base_url": args.base_url,
        "graphhopper_profile": args.profile,
        "city_count": len(cities),
        "skipped_city_count": len(skipped),
        "directed_route_count": len(records),
        "error_count": len(errors),
        "routing_engine": args.routing_engine,
        "source": args.source,
        "profile_hash": profile_hash,
    }

    _write_json(json_out, records, metadata)
    _write_csv(csv_out, records)
    _write_sql(sql_out, records, routing_engine=args.routing_engine, source=args.source, profile_hash=profile_hash)
    _write_text_report(text_out, records, city_count=len(cities), skipped=skipped, errors=errors, metadata=metadata)

    print(f"Wrote JSON: {json_out}")
    print(f"Wrote CSV: {csv_out}")
    print(f"Wrote SQL import script: {sql_out}")
    print(f"Wrote text report: {text_out}")

    if errors:
        print(f"Completed with {len(errors)} route errors. See report for details.")
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
