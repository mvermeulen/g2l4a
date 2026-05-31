#!/usr/bin/env bash
set -euo pipefail

GH_VERSION="${GH_VERSION:-11.0}"
GH_DIR="${GH_DIR:-/opt/graphhopper}"
GH_JAR="${GH_JAR:-$GH_DIR/graphhopper-web-${GH_VERSION}.jar}"
GH_CONFIG_FILE="${GH_CONFIG_FILE:-$GH_DIR/config.yml}"
GH_GRAPH_LOCATION="${GH_GRAPH_LOCATION:-$GH_DIR/graph-cache}"
GH_OSM_FILE="${GH_OSM_FILE:-$GH_DIR/map.osm.pbf}"
GH_OSM_URL="${GH_OSM_URL:-}"
JAVA_OPTS="${JAVA_OPTS:--Xms1g -Xmx4g}"

mkdir -p "$GH_DIR" "$GH_GRAPH_LOCATION"

if [[ ! -f "$GH_JAR" ]]; then
  echo "Downloading GraphHopper web jar ${GH_VERSION}..."
  curl -fsSL "https://repo1.maven.org/maven2/com/graphhopper/graphhopper-web/${GH_VERSION}/graphhopper-web-${GH_VERSION}.jar" -o "$GH_JAR"
fi

if [[ ! -f "$GH_CONFIG_FILE" ]]; then
  echo "Creating GraphHopper config from upstream template..."
  curl -fsSL "https://raw.githubusercontent.com/graphhopper/graphhopper/11.x/config-example.yml" -o "$GH_CONFIG_FILE"
fi

if [[ ! -f "$GH_OSM_FILE" ]]; then
  if [[ -z "$GH_OSM_URL" ]]; then
    echo "ERROR: GH_OSM_FILE does not exist and GH_OSM_URL is empty."
    echo "Set GH_OSM_URL to a downloadable .osm.pbf URL or mount GH_OSM_FILE."
    exit 1
  fi
  echo "Downloading OSM extract from GH_OSM_URL..."
  curl -fsSL "$GH_OSM_URL" -o "$GH_OSM_FILE"
fi

# The upstream sample config binds HTTP connectors to localhost, which is not reachable
# through Docker port publishing. Rewrite bind_host entries for container use.
sed -i 's/bind_host:[[:space:]]*localhost/bind_host: 0.0.0.0/g' "$GH_CONFIG_FILE"

# Defensive normalization: fix malformed heap flags like "-Xms4g-Xmx12g".
JAVA_OPTS="$(echo "$JAVA_OPTS" | sed -E 's/(-Xms[^[:space:]]+)(-Xmx)/\1 \2/g')"

exec java $JAVA_OPTS \
  -Ddw.graphhopper.datareader.file="$GH_OSM_FILE" \
  -Ddw.graphhopper.graph.location="$GH_GRAPH_LOCATION" \
  -jar "$GH_JAR" server "$GH_CONFIG_FILE"
