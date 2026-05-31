#!/usr/bin/env bash
set -euo pipefail

# One-liner helper to check container status and endpoint readiness.
COMPOSE_FILE="${COMPOSE_FILE:-docker-compose.graphhopper.yml}"
ENDPOINT_URL="${ENDPOINT_URL:-http://localhost:8989/info}"
LOG_FILE="${LOG_FILE:-.graphhopper/logs/graphhopper.log}"

compose_cmd() {
  if command -v docker-compose >/dev/null 2>&1; then
    docker-compose "$@"
  else
    docker compose "$@"
  fi
}

compose_cmd -f "$COMPOSE_FILE" ps

echo
if curl -fsS "$ENDPOINT_URL" >/dev/null 2>&1; then
  echo "GraphHopper endpoint is ready: $ENDPOINT_URL"
else
  echo "GraphHopper endpoint is not ready: $ENDPOINT_URL"
fi

if [[ -f "$LOG_FILE" ]]; then
  echo
  echo "Latest GraphHopper log line:"
  tail -n 1 "$LOG_FILE"
fi
