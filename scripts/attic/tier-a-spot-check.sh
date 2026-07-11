#!/usr/bin/env bash
# tier-a-spot-check — verify Tier A catalog availability (PG + Qdrant search).
#
# Usage:
#   make tier-a-spot-check                  # local profile (default)
#   make tier-a-spot-check PROFILE=fly    # Fly Postgres + cloud Qdrant
set -euo pipefail

ATTIC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPTS_DIR="$(dirname "$ATTIC_DIR")"
WORKSPACE_DIR="$(dirname "$SCRIPTS_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"

PROFILE="${PROFILE:-local}"
APPLY="${APPLY:-1}"
export APPLY
# shellcheck source=scripts/dogfood-env.sh
source "$SCRIPTS_DIR/dogfood-env.sh"
dogfood_apply_profile

echo "▸ tier-a-spot-check profile=$PROFILE"
dogfood_print_stack

cd "$AGENT_DIR"
# shellcheck disable=SC1091
[ -f .venv/bin/activate ] && source .venv/bin/activate
PYTHONPATH=. python scripts/tier_a_spot_check.py "$@"
