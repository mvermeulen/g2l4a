#!/usr/bin/env bash
set -euo pipefail

# One-liner helper to stop GraphHopper containers without deleting local OSM/graph files.
COMPOSE_FILE="${COMPOSE_FILE:-docker-compose.graphhopper.yml}"

compose_cmd() {
  if command -v docker-compose >/dev/null 2>&1; then
    docker-compose "$@"
  else
    docker compose "$@"
  fi
}

compose_cmd -f "$COMPOSE_FILE" down

echo "GraphHopper stopped. Persisted data in .graphhopper/ was not deleted."
