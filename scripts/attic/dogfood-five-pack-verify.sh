#!/usr/bin/env bash
# Automated five-pack substrate verification (maps to EAS phone-walk checklist).
#
# Complements manual device walk — checks Fly/local Postgres + offline discover compose.
#
# Usage:
#   scripts/dogfood-five-pack-verify.sh
#   PROFILE=local scripts/dogfood-five-pack-verify.sh
set -euo pipefail

ATTIC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPTS_DIR="$(dirname "$ATTIC_DIR")"
WORKSPACE_DIR="$(dirname "$SCRIPTS_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"
PROFILE="${PROFILE:-fly}"

AGENT_DIR="$AGENT_DIR" source "$SCRIPTS_DIR/dogfood-env.sh"
dogfood_apply_profile || exit 1

cd "$AGENT_DIR"
# shellcheck disable=SC1091
source .venv/bin/activate

export AI_MODE="${AI_MODE:-replay}"
export ATLAS_BOARD_COPY_LLM_ENABLED="${ATLAS_BOARD_COPY_LLM_ENABLED:-false}"

PYTHONPATH=. python scripts/dogfood_five_pack_verify.py "$@"
