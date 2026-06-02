#!/usr/bin/env python3
"""
Segment GPX Generator
Scans the reports directory for unique route segments (legs), and queries
GraphHopper to generate corresponding GPX files in the gpx directory.
Uses file modification times to skip regeneration of up-to-date GPX files.
"""

import argparse
import glob
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

# Add project root directory to sys.path to support importing from src
root_dir = Path(__file__).resolve().parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

try:
    from src.validation import CITY_REGISTRY
except ImportError as err:
    print(f"Error: Failed to import CITY_REGISTRY from src.validation. Make sure this script is run from the project root: {err}")
    sys.exit(1)


def slugify_city_name(city_name: str) -> str:
    """Slugify city names to match the pattern in example_report.py."""
    slug = re.sub(r"[^a-z0-9]+", "-", city_name.lower())
    return slug.strip("-") or "city"


def scan_reports_for_segments(reports_dir: Path):
    """
    Scans all JSON report files in the reports directory.
    Returns a dictionary mapping unique segments (origin, destination) to
    a list of report files (and sibling txt/md files) that contain them.
    """
    segments = {}
    json_files = glob.glob(os.path.join(reports_dir, "*.json"))

    for json_path_str in json_files:
        json_path = Path(json_path_str)
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"Warning: Failed to parse JSON file {json_path}: {e}")
            continue

        recommendations = data.get("recommendations", [])
        if not isinstance(recommendations, list):
            continue

        for rec in recommendations:
            legs = rec.get("legs", [])
            if not isinstance(legs, list):
                continue

            for leg in legs:
                origin = leg.get("origin")
                destination = leg.get("destination")
                if not origin or not destination:
                    continue

                segment = (origin, destination)
                if segment not in segments:
                    segments[segment] = []

                # Add the JSON report path
                if json_path not in segments[segment]:
                    segments[segment].append(json_path)

                # Check for sibling .md and .txt reports and include them in dependency tracking
                for ext in (".md", ".txt"):
                    sibling_path = json_path.with_suffix(ext)
                    if sibling_path.exists() and sibling_path not in segments[segment]:
                        segments[segment].append(sibling_path)

    return segments


def resolve_city_coords(city_name: str):
    """Resolves coordinates for a given city from the CITY_REGISTRY."""
    normalized = city_name.strip().lower()
    
    # Try exact match
    if normalized in CITY_REGISTRY:
        return CITY_REGISTRY[normalized]

    # Try replacement of spaces with underscores
    alt_name_1 = normalized.replace(" ", "_")
    if alt_name_1 in CITY_REGISTRY:
        return CITY_REGISTRY[alt_name_1]

    # Try replacement of underscores with spaces
    alt_name_2 = normalized.replace("_", " ")
    if alt_name_2 in CITY_REGISTRY:
        return CITY_REGISTRY[alt_name_2]

    return None


def generate_gpx_for_segment(
    origin: str,
    destination: str,
    output_path: Path,
    base_url: str,
    profile: str,
    timeout: float
) -> bool:
    """Queries GraphHopper for a segment route and writes it to output_path as GPX."""
    origin_coords = resolve_city_coords(origin)
    dest_coords = resolve_city_coords(destination)

    if not origin_coords:
        print(f"  Error: Could not resolve coordinates for origin: '{origin}'")
        return False
    if not dest_coords:
        print(f"  Error: Could not resolve coordinates for destination: '{destination}'")
        return False

    origin_lat, origin_lon = origin_coords
    dest_lat, dest_lon = dest_coords

    params = [
        ("profile", profile),
        ("type", "gpx"),
        ("gpx.track", "true"),
        ("gpx.route", "true"),
        ("gpx.waypoints", "true"),
        ("instructions", "true"),
        ("elevation", "true"),
        ("point", f"{origin_lat},{origin_lon}"),
        ("point", f"{dest_lat},{dest_lon}"),
    ]

    query_str = urllib.parse.urlencode(params)
    url = f"{base_url.rstrip('/')}/route?{query_str}"

    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=timeout) as response:
            payload = response.read()
    except Exception as e:
        print(f"  Error: Failed to request route from GraphHopper: {e}")
        return False

    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_bytes(payload)
        return True
    except Exception as e:
        print(f"  Error: Failed to write GPX data to {output_path}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Scan reports for unique segments and generate GPX files."
    )
    parser.add_argument(
        "--reports-dir",
        default="reports",
        help="Path to the reports directory (default: reports)"
    )
    parser.add_argument(
        "--gpx-dir",
        default="gpx/segment",
        help="Path to the GPX output directory (default: gpx/segment)"
    )
    parser.add_argument(
        "--base-url",
        default="http://localhost:8989",
        help="Base URL of the GraphHopper routing service (default: http://localhost:8989)"
    )
    parser.add_argument(
        "--profile",
        default="bike",
        help="Routing profile to use (default: bike)"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force regeneration of all GPX files, bypassing timestamp checks"
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=15.0,
        help="Request timeout in seconds (default: 15.0)"
    )

    args = parser.parse_args()

    reports_dir = Path(args.reports_dir)
    gpx_dir = Path(args.gpx_dir)

    if not reports_dir.exists():
        print(f"Error: Reports directory {reports_dir} does not exist.")
        return 1

    print(f"Scanning {reports_dir} for route segments...")
    segments = scan_reports_for_segments(reports_dir)

    if not segments:
        print("No segments found in the reports directory.")
        return 0

    print(f"Found {len(segments)} unique segments across reports.")

    generated_count = 0
    skipped_count = 0
    failed_count = 0

    for (origin, destination), report_paths in sorted(segments.items()):
        origin_slug = slugify_city_name(origin)
        destination_slug = slugify_city_name(destination)
        gpx_filename = f"{origin_slug}-to-{destination_slug}.gpx"
        gpx_path = gpx_dir / gpx_filename

        # Timestamp logic
        need_regeneration = True
        if gpx_path.exists() and not args.force:
            gpx_mtime = gpx_path.stat().st_mtime
            latest_report_mtime = max(p.stat().st_mtime for p in report_paths)
            if gpx_mtime >= latest_report_mtime:
                need_regeneration = False

        if not need_regeneration:
            print(f"Skipping: {gpx_filename} (up to date)")
            skipped_count += 1
            continue

        print(f"Generating: {gpx_filename} ({origin} -> {destination})")
        success = generate_gpx_for_segment(
            origin=origin,
            destination=destination,
            output_path=gpx_path,
            base_url=args.base_url,
            profile=args.profile,
            timeout=args.timeout
        )

        if success:
            generated_count += 1
        else:
            failed_count += 1

    print("\nSummary:")
    print(f"  Generated: {generated_count}")
    print(f"  Skipped:   {skipped_count}")
    print(f"  Failed:    {failed_count}")

    return 1 if failed_count > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
