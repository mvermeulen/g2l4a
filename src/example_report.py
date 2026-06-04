import argparse
import re
import signal
from pathlib import Path
from typing import Iterable, List, Optional
from urllib.parse import urlencode
from urllib.request import urlopen

from src.output import OutputFormatter
from src.solver_engine import BeamSearchSolver
from src.validation import RequestParser


def _default_output_path(example_path: Path) -> Path:
    return Path("reports") / f"{example_path.stem}-report.md"


def _default_json_output_path(example_path: Path) -> Path:
    return Path("reports") / f"{example_path.stem}-report.json"


def _default_txt_output_path(example_path: Path) -> Path:
    return Path("reports") / f"{example_path.stem}-report.txt"


def _slugify_city_name(city_name: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", city_name.lower())
    return slug.strip("-") or "city"


def _default_gpx_output_path(example_path: Path, start_city_name: str, end_city_name: str) -> Path:
    start_slug = _slugify_city_name(start_city_name)
    end_slug = _slugify_city_name(end_city_name)
    return Path("gpx") / f"{example_path.stem}--{start_slug}-to-{end_slug}.gpx"


def _extract_gpx_points(itinerary) -> list:
    if itinerary.legs:
        points = [itinerary.legs[0].origin]
        points.extend(leg.destination for leg in itinerary.legs)
        return points

    points = [itinerary.start_city]
    points.extend(itinerary.via_cities)
    points.append(itinerary.completion_city)
    return points


def _fetch_gpx_payload(url: str, request_timeout_seconds: float, total_timeout_seconds: float) -> bytes:
    if request_timeout_seconds <= 0:
        raise ValueError("request_timeout_seconds must be > 0")
    if total_timeout_seconds <= 0:
        raise ValueError("total_timeout_seconds must be > 0")

    if not hasattr(signal, "SIGALRM") or not hasattr(signal, "setitimer"):
        with urlopen(url, timeout=request_timeout_seconds) as response:
            return response.read()

    def _timeout_handler(_signum, _frame):
        raise TimeoutError(f"GPX request exceeded {total_timeout_seconds:.1f}s total timeout")

    previous_handler = signal.getsignal(signal.SIGALRM)
    previous_timer = signal.setitimer(signal.ITIMER_REAL, 0.0)
    try:
        signal.signal(signal.SIGALRM, _timeout_handler)
        signal.setitimer(signal.ITIMER_REAL, total_timeout_seconds)
        with urlopen(url, timeout=request_timeout_seconds) as response:
            return response.read()
    finally:
        signal.setitimer(signal.ITIMER_REAL, previous_timer[0], previous_timer[1])
        signal.signal(signal.SIGALRM, previous_handler)


def _downsample_coordinates(coords: list, target_distance_km: float = 3.0) -> list:
    if len(coords) <= 2:
        return coords

    def haversine_km(lat1, lon1, lat2, lon2):
        import math
        R = 6371.0 # Earth radius in km
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)
        dlat = lat2_rad - lat1_rad
        dlon = lon2_rad - lon1_rad
        a = math.sin(dlat / 2.0)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2.0)**2
        c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
        return R * c

    sampled = [coords[0]]
    last_pt = coords[0]
    for pt in coords[1:]:
        dist = haversine_km(last_pt[0], last_pt[1], pt[0], pt[1])
        if dist >= target_distance_km:
            sampled.append(pt)
            last_pt = pt
    if sampled[-1] != coords[-1]:
        sampled.append(coords[-1])
    return sampled


def _fetch_itinerary_lodging(
    coords: list,
    radius_meters: int,
    types: list,
    cache_db_path: str,
    is_mock: bool,
) -> list:
    if not coords:
        return []

    import urllib.request
    import urllib.parse
    import json
    import logging
    import hashlib

    # Dynamic downsampling to target ~40 points maximum to prevent Overpass timeouts
    target_points = 40
    if len(coords) > target_points:
        step = max(1, len(coords) // target_points)
        sampled_coords = coords[::step]
        # Ensure destination point is included
        if sampled_coords[-1] != coords[-1]:
            sampled_coords.append(coords[-1])
    else:
        sampled_coords = coords

    # Compute stable route hash for itinerary level caching
    rounded_coords = [(round(lat, 5), round(lon, 5)) for lat, lon in sampled_coords]
    coord_str = json.dumps(rounded_coords)
    types_str = ",".join(sorted(types))
    hash_input = f"{coord_str}|{radius_meters}|{types_str}"
    route_hash = hashlib.sha256(hash_input.encode('utf-8')).hexdigest()

    from src.cache import SQLiteCacheManager
    cache_mgr = SQLiteCacheManager(cache_db_path)
    try:
        cached = cache_mgr.get_itinerary_lodging(route_hash)
        if cached is not None:
            return cached
    finally:
        cache_mgr.close()

    if is_mock:
        hotels = []
        if len(sampled_coords) >= 1:
            hotels.append({
                "name": "Mock Cozy Inn near Start",
                "lat": sampled_coords[0][0] + 0.001,
                "lon": sampled_coords[0][1] + 0.001,
            })
        if len(sampled_coords) >= 2:
            hotels.append({
                "name": "Mock Route Motel near End",
                "lat": sampled_coords[-1][0] - 0.001,
                "lon": sampled_coords[-1][1] - 0.001,
            })
        cache_mgr = SQLiteCacheManager(cache_db_path)
        try:
            cache_mgr.save_itinerary_lodging(route_hash, radius_meters, types, hotels)
        finally:
            cache_mgr.close()
        return hotels

    points_str = ", ".join(f"{lat},{lon}" for lat, lon in sampled_coords)
    types_pattern = "|".join(types)

    query = f"""
    [out:json][timeout:40];
    (
      node["tourism"~"{types_pattern}"](around:{radius_meters}, {points_str});
      way["tourism"~"{types_pattern}"](around:{radius_meters}, {points_str});
    );
    out body center;
    """

    url = "https://overpass-api.de/api/interpreter"
    hotels = []
    try:
        data = urllib.parse.urlencode({"data": query}).encode("utf-8")
        req = urllib.request.Request(
            url,
            data=data,
            headers={"User-Agent": "g2l4a-client/1.0"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=45) as response:
            payload = json.loads(response.read().decode("utf-8"))
            for element in payload.get("elements", []):
                tags = element.get("tags", {})
                name = tags.get("name")
                lat = element.get("lat") or element.get("center", {}).get("lat")
                lon = element.get("lon") or element.get("center", {}).get("lon")
                if name and lat and lon:
                    hotels.append({
                        "name": str(name),
                        "lat": float(lat),
                        "lon": float(lon),
                    })
    except Exception as exc:
        logging.warning(f"Lodging fetch via Overpass failed: {exc}")
        return []

    cache_mgr = SQLiteCacheManager(cache_db_path)
    try:
        cache_mgr.save_itinerary_lodging(route_hash, radius_meters, types, hotels)
    finally:
        cache_mgr.close()

    return hotels


def _maybe_generate_gpx(
    example_path: Path,
    config: dict,
    itinerary,
    cache_db_path: str = ".g2l4a_cache.db",
) -> Optional[Path]:
    output_cfg = config.get("output", {})
    if not bool(output_cfg.get("gpx", False)):
        return None

    routing_cfg = config.get("routing_provider", {})
    if str(routing_cfg.get("name", "mock")) != "graphhopper":
        return None

    points = _extract_gpx_points(itinerary)
    if len(points) < 2:
        return None

    params = [
        ("profile", str(routing_cfg.get("profile", "bike"))),
        ("type", "gpx"),
        ("gpx.track", "true"),
        ("gpx.route", "true"),
        ("gpx.waypoints", "true"),
        ("instructions", "true"),
        ("elevation", "true"),
    ]
    for point in points:
        params.append(("point", f"{point.latitude},{point.longitude}"))

    base_url = str(routing_cfg.get("base_url", "http://localhost:8989")).rstrip("/")
    request_timeout_seconds = float(routing_cfg.get("timeout_seconds", 12.0))
    gpx_timeout_seconds = float(output_cfg.get("gpx_timeout_seconds", 90.0))
    effective_request_timeout = min(request_timeout_seconds, gpx_timeout_seconds)
    url = f"{base_url}/route?{urlencode(params)}"

    output_path = _default_gpx_output_path(
        example_path,
        itinerary.start_city.name,
        itinerary.completion_city.name,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        gpx_payload = _fetch_gpx_payload(
            url,
            request_timeout_seconds=effective_request_timeout,
            total_timeout_seconds=gpx_timeout_seconds,
        )
    except (TimeoutError, OSError, ValueError) as exc:
        print(f"Skipped GPX for {example_path.name}: {exc}")
        return None

    lodging_cfg = output_cfg.get("lodging_overlay", {})
    if bool(lodging_cfg.get("enabled", False)):
        import xml.etree.ElementTree as ET
        try:
            ET.register_namespace("", "http://www.topografix.com/GPX/1/1")
            
            radius = int(lodging_cfg.get("radius_meters", 800))
            types = list(lodging_cfg.get("types", ["hotel"]))
            is_mock = str(routing_cfg.get("name", "mock")).lower() == "mock"
            
            all_coords = []
            for leg in itinerary.legs:
                if leg.geometry:
                    all_coords.extend(leg.geometry)

            all_hotels = []
            if all_coords:
                all_hotels = _fetch_itinerary_lodging(
                    coords=all_coords,
                    radius_meters=radius,
                    types=types,
                    cache_db_path=cache_db_path,
                    is_mock=is_mock
                )

            if all_hotels:
                root = ET.fromstring(gpx_payload)
                ns = "http://www.topografix.com/GPX/1/1"
                if root.tag.startswith("{"):
                    ns = root.tag.split("}")[0].strip("{")

                # Find insertion index (before any trk or rte element)
                insert_idx = 0
                for idx, child in enumerate(root):
                    tag_local = child.tag.split("}")[-1]
                    if tag_local in ("trk", "rte"):
                        insert_idx = idx
                        break

                seen = set()
                for hotel in all_hotels:
                    coord_key = (round(hotel["lat"], 5), round(hotel["lon"], 5))
                    if coord_key in seen:
                        continue
                    seen.add(coord_key)

                    wpt = ET.Element(f"{{{ns}}}wpt", lat=f"{hotel['lat']:.6f}", lon=f"{hotel['lon']:.6f}")
                    name_elem = ET.SubElement(wpt, f"{{{ns}}}name")
                    name_elem.text = hotel["name"]
                    desc_elem = ET.SubElement(wpt, f"{{{ns}}}desc")
                    desc_elem.text = "Hotel (Corridor Overlay)"
                    sym_elem = ET.SubElement(wpt, f"{{{ns}}}sym")
                    sym_elem.text = "Lodging"

                    root.insert(insert_idx, wpt)
                    insert_idx += 1

                gpx_payload = ET.tostring(root, encoding="utf-8", xml_declaration=True)
        except Exception as exc:
            print(f"Warning: Failed to inject lodging waypoints into GPX: {exc}")

    output_path.write_bytes(gpx_payload)
    return output_path


def _resolve_example_paths(example_paths: Iterable[str], all_examples: bool) -> List[Path]:
    if all_examples:
        return sorted(Path("examples").glob("*.yaml"))
    return [Path(path) for path in example_paths]


def _build_data_attribution(config: dict) -> Optional[dict]:
    weather_provider_name = str(config.get("weather_provider", {}).get("name", "mock"))
    routing_provider_name = str(config.get("routing_provider", {}).get("name", "mock"))

    weather_attribution = None
    routing_attribution = None

    if weather_provider_name == "open_meteo":
        weather_attribution = {
            "provider": "Open-Meteo",
            "provider_url": "https://open-meteo.com/",
            "license": "CC BY 4.0",
            "license_url": "https://creativecommons.org/licenses/by/4.0/",
            "note": "Data has been transformed into itinerary-level schedule summaries.",
        }
    elif weather_provider_name == "meteostat":
        weather_attribution = {
            "provider": "Meteostat",
            "provider_url": "https://meteostat.net/",
            "license": "CC BY-NC 4.0",
            "license_url": "https://creativecommons.org/licenses/by-nc/4.0/",
            "note": "Historical weather data provided by Meteostat under CC BY-NC 4.0.",
        }

    if routing_provider_name == "graphhopper":
        routing_attribution = {
            "provider": "GraphHopper",
            "provider_url": "https://www.graphhopper.com/",
            "license": "OpenStreetMap ODbL 1.0",
            "license_url": "https://opendatacommons.org/licenses/odbl/1-0/",
            "note": "Routing distances and elevation metrics are computed via GraphHopper using OpenStreetMap data.",
        }

    if weather_attribution and routing_attribution:
        return {
            "weather": weather_attribution,
            "routing": routing_attribution,
        }

    if weather_attribution:
        return weather_attribution

    if routing_attribution:
        return routing_attribution

    return None


def _build_weather_attribution_markdown() -> str:
    return (
        "Weather data by [Open-Meteo.com](https://open-meteo.com/)"
        " under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)."
        " Data has been transformed into itinerary-level schedule summaries."
    )


def _build_meteostat_attribution_markdown() -> str:
    return (
        "Weather data provided by [Meteostat](https://meteostat.net/)"
        " under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)."
        " Data has been transformed into itinerary-level schedule summaries."
    )


def _build_routing_attribution_markdown() -> str:
    return (
        "Routing and elevation data powered by [GraphHopper](https://www.graphhopper.com/)"
        " using [OpenStreetMap](https://www.openstreetmap.org/copyright)"
        " data licensed under [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/)."
    )


def _apply_data_attribution(markdown: str, config: dict) -> str:
    weather_provider_name = str(config.get("weather_provider", {}).get("name", "mock"))
    routing_provider_name = str(config.get("routing_provider", {}).get("name", "mock"))

    attribution_lines = []
    if weather_provider_name == "open_meteo":
        attribution_lines.append(_build_weather_attribution_markdown())
    elif weather_provider_name == "meteostat":
        attribution_lines.append(_build_meteostat_attribution_markdown())
        
    if routing_provider_name == "graphhopper":
        attribution_lines.append(_build_routing_attribution_markdown())

    if not attribution_lines:
        return markdown

    attribution = "\n\n## Data Attribution\n"
    for line in attribution_lines:
        attribution += f"- {line}\n"
    return markdown.rstrip() + attribution + "\n"


def generate_report_for_example(
    example_path: Path,
    output_path: Optional[Path] = None,
    json_output_path: Optional[Path] = None,
    txt_output_path: Optional[Path] = None,
    system_defaults_path: str = "config/defaults.yaml",
    cache_db_path: str = ".g2l4a_cache.db",
    max_alternatives: Optional[int] = None,
) -> Path:
    """Parse one YAML request, solve it, and persist report outputs."""
    parser = RequestParser(system_defaults_path=system_defaults_path)
    itinerary, config = parser.parse_request_file(str(example_path))

    effective_max_alternatives = max_alternatives
    if effective_max_alternatives is None:
        effective_max_alternatives = int(config.get("output", {}).get("alternatives_count", 4))

    run_config = dict(config)
    run_config["max_alternatives"] = effective_max_alternatives

    solver = BeamSearchSolver(cache_db_path)
    try:
        itineraries = solver.solve(itinerary, run_config)
    finally:
        solver.close()

    if not itineraries:
        raise RuntimeError(f"No recommendations were generated for {example_path}.")

    gpx_output_path = _maybe_generate_gpx(example_path, config, itineraries[0], cache_db_path=cache_db_path)

    markdown = OutputFormatter.format_recommendations_markdown(itineraries)
    markdown = _apply_data_attribution(markdown, config)
    text_payload = OutputFormatter.markdown_to_aligned_text(markdown)
    json_payload = OutputFormatter.serialize_recommendations_json(
        itineraries,
        data_attribution=_build_data_attribution(config),
    )

    final_output_path = output_path if output_path is not None else _default_output_path(example_path)
    if output_path is not None:
        final_output_path.parent.mkdir(parents=True, exist_ok=True)
        final_output_path.write_text(markdown + "\n", encoding="utf-8")

    if json_output_path is not None:
        json_output_path.parent.mkdir(parents=True, exist_ok=True)
        json_output_path.write_text(json_payload + "\n", encoding="utf-8")
    if txt_output_path is not None:
        txt_output_path.parent.mkdir(parents=True, exist_ok=True)
        txt_output_path.write_text(text_payload + "\n", encoding="utf-8")
    if gpx_output_path is not None:
        print(f"Generated GPX: {gpx_output_path}")
    if output_path is None and json_output_path is not None:
        return json_output_path
    if output_path is None and txt_output_path is not None:
        return txt_output_path
    return final_output_path


def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate markdown itinerary recommendation reports from example YAML configurations."
    )
    parser.add_argument(
        "examples",
        nargs="*",
        help="One or more example YAML files (for example: examples/eastern-capitals-fixed-date-february.yaml).",
    )
    parser.add_argument(
        "--all-examples",
        action="store_true",
        help="Generate reports for all .yaml files in examples/.",
    )
    parser.add_argument(
        "--format",
        choices=("md", "txt", "json", "both", "all"),
        default="md",
        help="Output format: md (default), txt, json, both (md+json), or all (md+json+txt).",
    )
    parser.add_argument(
        "--output",
        help="Optional markdown output path (used when --format is md or both). Allowed only for a single example.",
    )
    parser.add_argument(
        "--json-output",
        help="Optional JSON output path (used when --format is json or both). Allowed only for a single example.",
    )
    parser.add_argument(
        "--txt-output",
        help="Optional text output path (used when --format is txt or all). Allowed only for a single example.",
    )
    parser.add_argument(
        "--cache-db",
        default=".g2l4a_cache.db",
        help="SQLite cache file path used by the solver.",
    )
    parser.add_argument(
        "--max-alternatives",
        type=int,
        help="Override maximum number of alternative itineraries in addition to the best recommendation.",
    )
    return parser


def main() -> int:
    parser = build_argument_parser()
    args = parser.parse_args()

    if not args.examples and not args.all_examples:
        parser.error("Provide at least one example path or use --all-examples.")

    if args.max_alternatives is not None and args.max_alternatives < 0:
        parser.error("--max-alternatives must be >= 0.")

    resolved_examples = _resolve_example_paths(args.examples, args.all_examples)
    if not resolved_examples:
        parser.error("No example YAML files were found.")

    if args.output and len(resolved_examples) != 1:
        parser.error("--output can only be used when processing a single example file.")

    if args.json_output and len(resolved_examples) != 1:
        parser.error("--json-output can only be used when processing a single example file.")

    if args.txt_output and len(resolved_examples) != 1:
        parser.error("--txt-output can only be used when processing a single example file.")

    selected_format = args.format

    generated_paths: List[Path] = []
    generated_json_paths: List[Path] = []
    generated_txt_paths: List[Path] = []
    for example_path in resolved_examples:
        if selected_format in ("json", "txt"):
            output_path = None
        elif args.output:
            output_path = Path(args.output)
        else:
            output_path = _default_output_path(example_path)

        if args.json_output:
            json_output_path = Path(args.json_output)
        elif selected_format in ("json", "both", "all"):
            json_output_path = _default_json_output_path(example_path)
        else:
            json_output_path = None

        if args.txt_output:
            txt_output_path = Path(args.txt_output)
        elif selected_format in ("txt", "all"):
            txt_output_path = _default_txt_output_path(example_path)
        else:
            txt_output_path = None

        written = generate_report_for_example(
            example_path=example_path,
            output_path=output_path,
            json_output_path=json_output_path,
            txt_output_path=txt_output_path,
            cache_db_path=args.cache_db,
            max_alternatives=args.max_alternatives,
        )
        if output_path is not None:
            generated_paths.append(written)
        if json_output_path is not None:
            generated_json_paths.append(json_output_path)
        if txt_output_path is not None:
            generated_txt_paths.append(txt_output_path)

    for path in generated_paths:
        print(f"Generated: {path}")
    for path in generated_json_paths:
        print(f"Generated JSON: {path}")
    for path in generated_txt_paths:
        print(f"Generated TXT: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())