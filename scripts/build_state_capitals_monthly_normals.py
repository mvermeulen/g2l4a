#!/usr/bin/env python3
"""Build monthly temperature normals for all 50 US state capitals plus Washington, DC and Chicago.

Source strategy:
- Fetch each capital's public Wikipedia page.
- Parse the monthly climate table for mean daily max/min in Fahrenheit.
- Persist a local dataset used by the runtime fallback weather provider.

Usage:
    /home/mev/source/g2l4a/.venv/bin/python scripts/build_state_capitals_monthly_normals.py
"""

from __future__ import annotations

import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup


CAPITAL_WIKI_TITLES: Dict[str, str] = {
    "Montgomery, Alabama": "Montgomery,_Alabama",
    "Juneau, Alaska": "Juneau,_Alaska",
    "Phoenix, Arizona": "Phoenix,_Arizona",
    "Little Rock, Arkansas": "Little_Rock,_Arkansas",
    "Sacramento, California": "Sacramento,_California",
    "Denver, Colorado": "Denver,_Colorado",
    "Hartford, Connecticut": "Hartford,_Connecticut",
    "Dover, Delaware": "Dover,_Delaware",
    "Tallahassee, Florida": "Tallahassee,_Florida",
    "Atlanta, Georgia": "Atlanta",
    "Honolulu, Hawaii": "Honolulu",
    "Boise, Idaho": "Boise,_Idaho",
    "Springfield, Illinois": "Springfield,_Illinois",
    "Indianapolis, Indiana": "Indianapolis",
    "Des Moines, Iowa": "Des_Moines,_Iowa",
    "Topeka, Kansas": "Topeka,_Kansas",
    "Frankfort, Kentucky": "Frankfort,_Kentucky",
    "Baton Rouge, Louisiana": "Baton_Rouge,_Louisiana",
    "Augusta, Maine": "Augusta,_Maine",
    "Annapolis, Maryland": "Annapolis,_Maryland",
    "Boston, Massachusetts": "Boston",
    "Lansing, Michigan": "Lansing,_Michigan",
    "St. Paul, Minnesota": "Saint_Paul,_Minnesota",
    "Jackson, Mississippi": "Jackson,_Mississippi",
    "Jefferson City, Missouri": "Jefferson_City,_Missouri",
    "Helena, Montana": "Helena,_Montana",
    "Lincoln, Nebraska": "Lincoln,_Nebraska",
    "Carson City, Nevada": "Carson_City,_Nevada",
    "Concord, New Hampshire": "Concord,_New_Hampshire",
    "Trenton, New Jersey": "Trenton,_New_Jersey",
    "Washington, DC": "Washington,_D.C.",
    "Santa Fe, New Mexico": "Santa_Fe,_New_Mexico",
    "Albany, New York": "Albany,_New_York",
    "Raleigh, North Carolina": "Raleigh,_North_Carolina",
    "Bismarck, North Dakota": "Bismarck,_North_Dakota",
    "Columbus, Ohio": "Columbus,_Ohio",
    "Oklahoma City, Oklahoma": "Oklahoma_City",
    "Salem, Oregon": "Salem,_Oregon",
    "Harrisburg, Pennsylvania": "Harrisburg,_Pennsylvania",
    "Providence, Rhode Island": "Providence,_Rhode_Island",
    "Columbia, South Carolina": "Columbia,_South_Carolina",
    "Pierre, South Dakota": "Pierre,_South_Dakota",
    "Nashville, Tennessee": "Nashville,_Tennessee",
    "Austin, Texas": "Austin,_Texas",
    "Salt Lake City, Utah": "Salt_Lake_City",
    "Montpelier, Vermont": "Montpelier,_Vermont",
    "Richmond, Virginia": "Richmond,_Virginia",
    "Olympia, Washington": "Olympia,_Washington",
    "Charleston, West Virginia": "Charleston,_West_Virginia",
    "Madison, Wisconsin": "Madison,_Wisconsin",
    "Cheyenne, Wyoming": "Cheyenne,_Wyoming",
    "Chicago, Illinois": "Chicago",
}


HEADER_CANDIDATES_HIGH = (
    "Mean daily maximum",
    "Average high",
    "Mean maximum",
)
HEADER_CANDIDATES_LOW = (
    "Mean daily minimum",
    "Average low",
    "Mean minimum",
)


def _fetch_wikipedia_html(title: str) -> str:
    url = f"https://en.wikipedia.org/wiki/{title}"
    req = Request(
        url,
        headers={
            "User-Agent": "g2l4a-weather-builder/1.0 (state-capital-monthly-normals)",
        },
    )
    with urlopen(req, timeout=25) as response:
        return response.read().decode("utf-8", errors="ignore")


def _extract_first_float(text: str) -> Optional[float]:
    match = re.search(r"-?\d+(?:\.\d+)?", text)
    if not match:
        return None
    return float(match.group(0))


def _extract_monthly_row(cells: List) -> Optional[List[float]]:
    values: List[float] = []
    for cell in cells[1:13]:
        value = _extract_first_float(cell.get_text(" ", strip=True))
        if value is None:
            return None
        values.append(value)
    if len(values) != 12:
        return None
    return values


def _parse_capital_monthly_normals(html: str) -> Tuple[List[float], List[float]]:
    soup = BeautifulSoup(html, "html.parser")
    highs: Optional[List[float]] = None
    lows: Optional[List[float]] = None

    for row in soup.select("table.wikitable tr"):
        cells = row.find_all(["th", "td"])
        if len(cells) < 13:
            continue

        label = " ".join(cells[0].get_text(" ", strip=True).split())
        parsed = _extract_monthly_row(cells)
        if parsed is None:
            continue

        if highs is None and any(token in label for token in HEADER_CANDIDATES_HIGH):
            highs = parsed
        if lows is None and any(token in label for token in HEADER_CANDIDATES_LOW):
            lows = parsed

        if highs is not None and lows is not None:
            return highs, lows

    raise RuntimeError("Unable to locate monthly high/low temperature rows in climate table")


def _build_aliases(city_name: str) -> List[str]:
    aliases = {
        city_name,
        city_name.lower(),
        city_name.replace("St.", "St"),
        city_name.replace("St.", "Saint"),
        city_name.replace("_", " "),
    }
    if city_name == "Baton Rouge, Louisiana":
        aliases.add("baton_rouge, louisiana")
    if city_name == "St. Paul, Minnesota":
        aliases.add("st paul, minnesota")
    return sorted(alias for alias in aliases if alias)


def build_dataset() -> Dict[str, object]:
    cities_payload: Dict[str, object] = {}

    total = len(CAPITAL_WIKI_TITLES)
    for idx, (city_name, wiki_title) in enumerate(CAPITAL_WIKI_TITLES.items(), start=1):
        html = _fetch_wikipedia_html(wiki_title)
        highs, lows = _parse_capital_monthly_normals(html)

        monthly = {
            str(month): {
                "high_temp_f": round(float(highs[month - 1]), 1),
                "low_temp_f": round(float(lows[month - 1]), 1),
            }
            for month in range(1, 13)
        }

        cities_payload[city_name] = {
            "aliases": _build_aliases(city_name),
            "wikipedia_title": wiki_title,
            "monthly": monthly,
        }

        print(f"[{idx:02d}/{total}] Parsed {city_name}")
        time.sleep(0.2)

    return {
        "metadata": {
            "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
            "source": "Wikipedia climate tables",
            "units": "F",
            "coverage": "50 US state capitals + Washington, DC + Chicago, Illinois",
            "high_row": list(HEADER_CANDIDATES_HIGH),
            "low_row": list(HEADER_CANDIDATES_LOW),
        },
        "cities": cities_payload,
    }


def main() -> int:
    dataset = build_dataset()
    output_path = Path("data/state_capitals_monthly_normals.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(dataset, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
