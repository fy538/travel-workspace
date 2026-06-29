#!/usr/bin/env bash
# tier-a-spot-check — verify Tier A catalog availability on local stack.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"

PROFILE="${PROFILE:-local}"
# shellcheck source=scripts/dogfood-env.sh
source "$SCRIPT_DIR/dogfood-env.sh"
AGENT_DIR="$AGENT_DIR" dogfood_apply_profile

cd "$AGENT_DIR"
# shellcheck disable=SC1091
[ -f .venv/bin/activate ] && source .venv/bin/activate
PYTHONPATH=. python scripts/tier_a_spot_check.py "$@"
