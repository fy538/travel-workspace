#!/usr/bin/env bash
# Two-persona live API certification for J02, J04, J05, J10.
#
# Usage:
#   scripts/dogfood-journey-live-api.sh                    # TestClient (local PG)
#   TRANSPORT=http PRELAUNCH_JWT_MARA=... PRELAUNCH_JWT_DAO=... \\
#       scripts/dogfood-journey-live-api.sh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"
PROFILE="${PROFILE:-local}"
TRANSPORT="${TRANSPORT:-testclient}"
PRELAUNCH_HOST="${PRELAUNCH_HOST:-https://vesper-backend.fly.dev}"

AGENT_DIR="$AGENT_DIR" source "$SCRIPT_DIR/dogfood-env.sh"
dogfood_apply_profile || exit 1

cd "$AGENT_DIR"
# shellcheck disable=SC1091
source .venv/bin/activate

export AI_MODE="${AI_MODE:-replay}"
export ATLAS_BOARD_COPY_LLM_ENABLED="${ATLAS_BOARD_COPY_LLM_ENABLED:-false}"
export DOGFOOD_JOURNEY_LIVE_TRANSPORT="$TRANSPORT"

PYTHONPATH=. python scripts/dogfood_journey_cert.py live-api \
  --transport "$TRANSPORT" \
  --host "$PRELAUNCH_HOST" \
  "$@"
