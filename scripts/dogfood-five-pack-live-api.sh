#!/usr/bin/env bash
# Live HTTP five-pack verification (TestClient local or Fly with JWT).
#
# Usage:
#   scripts/dogfood-five-pack-live-api.sh                    # TestClient (local PG)
#   TRANSPORT=http PRELAUNCH_JWT=<jwt> scripts/dogfood-five-pack-live-api.sh
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
export DOGFOOD_LIVE_API_TRANSPORT="$TRANSPORT"

PYTHONPATH=. python scripts/dogfood_five_pack_live_api.py \
  --transport "$TRANSPORT" \
  --host "$PRELAUNCH_HOST" \
  "$@"
