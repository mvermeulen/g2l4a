#!/usr/bin/env bash
set -euo pipefail

# One-liner helper to start GraphHopper without interrupting existing persisted data.
COMPOSE_FILE="${COMPOSE_FILE:-docker-compose.graphhopper.yml}"
BUILD_FLAG=""
MEM_PRESET="${GH_MEM_PRESET:-}"

usage() {
  echo "Usage: ./scripts/graphhopper-start.sh [--build] [--mem-preset low|medium|high|xlarge|xxlarge]"
  echo
  echo "Environment overrides:"
  echo "  COMPOSE_FILE=<path>"
  echo "  GH_MEM_PRESET=low|medium|high|xlarge|xxlarge"
  echo "  GRAPHHOPPER_JAVA_OPTS=\"-Xms24g -Xmx48g\""
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --build)
      BUILD_FLAG="--build"
      shift
      ;;
    --mem-preset)
      if [[ $# -lt 2 ]]; then
        echo "ERROR: --mem-preset requires a value"
        usage
        exit 1
      fi
      MEM_PRESET="$2"
      shift 2
      ;;
    --mem-preset=*)
      MEM_PRESET="${1#*=}"
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "ERROR: unknown argument: $1"
      usage
      exit 1
      ;;
  esac
done

compose_cmd() {
  if command -v docker-compose >/dev/null 2>&1; then
    docker-compose "$@"
  else
    docker compose "$@"
  fi
}

resolve_java_opts_from_preset() {
  case "$1" in
    "")
      echo ""
      ;;
    low)
      echo "-Xms1g -Xmx4g"
      ;;
    medium)
      echo "-Xms4g -Xmx8g"
      ;;
    high)
      echo "-Xms8g -Xmx16g"
      ;;
    xlarge)
      echo "-Xms12g -Xmx24g"
      ;;
    xxlarge)
      echo "-Xms24g -Xmx48g"
      ;;
    *)
      echo "ERROR: invalid memory preset '$1' (expected: low|medium|high|xlarge|xxlarge)" >&2
      exit 1
      ;;
  esac
}

JAVA_OPTS_TO_USE="${GRAPHHOPPER_JAVA_OPTS:-}"
if [[ -z "$JAVA_OPTS_TO_USE" ]]; then
  JAVA_OPTS_TO_USE="$(resolve_java_opts_from_preset "$MEM_PRESET")"
fi

if [[ "$BUILD_FLAG" == "--build" ]]; then
  if [[ -n "$JAVA_OPTS_TO_USE" ]]; then
    GRAPHHOPPER_JAVA_OPTS="$JAVA_OPTS_TO_USE" compose_cmd -f "$COMPOSE_FILE" up -d --build
  else
    compose_cmd -f "$COMPOSE_FILE" up -d --build
  fi
else
  if [[ -n "$JAVA_OPTS_TO_USE" ]]; then
    GRAPHHOPPER_JAVA_OPTS="$JAVA_OPTS_TO_USE" compose_cmd -f "$COMPOSE_FILE" up -d
  else
    compose_cmd -f "$COMPOSE_FILE" up -d
  fi
fi

echo "GraphHopper start command submitted."
if [[ -n "$JAVA_OPTS_TO_USE" ]]; then
  echo "Using GRAPHHOPPER_JAVA_OPTS=$JAVA_OPTS_TO_USE"
fi
