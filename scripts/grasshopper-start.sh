#!/usr/bin/env bash
set -euo pipefail

# Compatibility wrapper for common typo.
exec "$(dirname "$0")/graphhopper-start.sh" "$@"
