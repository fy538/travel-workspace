#!/usr/bin/env bash
# tier-b-spot-check — verify Tier B catalog availability (PG + Qdrant search).
#
# Usage:
#   make tier-b-spot-check                  # local profile (default)
#   make tier-b-spot-check PROFILE=fly    # Fly Postgres + cloud Qdrant
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"

PROFILE="${PROFILE:-local}"
APPLY="${APPLY:-1}"
export APPLY
# shellcheck source=scripts/dogfood-env.sh
source "$SCRIPT_DIR/dogfood-env.sh"
dogfood_apply_profile

echo "▸ tier-b-spot-check profile=$PROFILE"
dogfood_print_stack

cd "$AGENT_DIR"
# shellcheck disable=SC1091
[ -f .venv/bin/activate ] && source .venv/bin/activate
PYTHONPATH=. python scripts/tier_b_spot_check.py "$@"
