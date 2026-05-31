#!/usr/bin/env bash
set -euo pipefail

# Rebuild GraphHopper with a fresh OSM extract.
# Safety: requires --yes to avoid accidental interruption of active imports/downloads.
COMPOSE_FILE="${COMPOSE_FILE:-docker-compose.graphhopper.yml}"
GRAPH_DIR="${GRAPH_DIR:-.graphhopper}"
GH_OSM_URL_DEFAULT="https://download.geofabrik.de/north-america-latest.osm.pbf"
GH_OSM_URL="${GH_OSM_URL:-$GH_OSM_URL_DEFAULT}"
JAVA_OPTS_DEFAULT="-Xms4g -Xmx12g"
GRAPHHOPPER_JAVA_OPTS="${GRAPHHOPPER_JAVA_OPTS:-$JAVA_OPTS_DEFAULT}"

compose_cmd() {
  if command -v docker-compose >/dev/null 2>&1; then
    docker-compose "$@"
  else
    docker compose "$@"
  fi
}

if [[ "${1:-}" != "--yes" ]]; then
  echo "Refusing to refresh without explicit confirmation."
  echo "This command stops GraphHopper and deletes local graph/import data:"
  echo "  $GRAPH_DIR/graph-cache"
  echo "  $GRAPH_DIR/map.osm.pbf"
  echo
  echo "Run again with --yes when you are ready."
  exit 1
fi

compose_cmd -f "$COMPOSE_FILE" down
rm -rf "$GRAPH_DIR/graph-cache"
rm -f "$GRAPH_DIR/map.osm.pbf"
GH_OSM_URL="$GH_OSM_URL" GRAPHHOPPER_JAVA_OPTS="$GRAPHHOPPER_JAVA_OPTS" compose_cmd -f "$COMPOSE_FILE" up -d --build

echo "GraphHopper refresh command submitted."
echo "OSM URL: $GH_OSM_URL"
