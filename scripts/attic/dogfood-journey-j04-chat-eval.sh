#!/usr/bin/env bash
# J04 chat/privacy eval — substrate + group-history egress gates on S4 trip.
#
# Usage:
#   scripts/dogfood-journey-j04-chat-eval.sh
#   TRANSPORT=http PRELAUNCH_JWT_MARA=... scripts/dogfood-journey-j04-chat-eval.sh
set -euo pipefail

ATTIC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPTS_DIR="$(dirname "$ATTIC_DIR")"
WORKSPACE_DIR="$(dirname "$SCRIPTS_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"
PROFILE="${PROFILE:-local}"
TRANSPORT="${TRANSPORT:-testclient}"
PRELAUNCH_HOST="${PRELAUNCH_HOST:-https://vesper-backend.fly.dev}"

AGENT_DIR="$AGENT_DIR" source "$SCRIPTS_DIR/dogfood-env.sh"
dogfood_apply_profile || exit 1

cd "$AGENT_DIR"
# shellcheck disable=SC1091
source .venv/bin/activate

export AI_MODE="${AI_MODE:-replay}"
export ATLAS_BOARD_COPY_LLM_ENABLED="${ATLAS_BOARD_COPY_LLM_ENABLED:-false}"
export DOGFOOD_J04_CHAT_TRANSPORT="$TRANSPORT"

PYTHONPATH=. python scripts/dogfood_journey_j04_chat_eval.py \
  --transport "$TRANSPORT" \
  --host "$PRELAUNCH_HOST" \
  "$@"
