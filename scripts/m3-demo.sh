#!/usr/bin/env bash
# Start a deliberately local/demo-only backend configuration for the M3
# relationship handoff slice. The production-shaped dev command remains dark;
# this wrapper is the only checked-in launcher that opts into the UUID handoff
# flag, and it requires an explicit confirmation so the choice is visible in
# shell history and CI logs.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ "${M3_DEMO_CONFIRM:-}" != "1" ]]; then
  printf '%s\n' \
    "M3 demo mode is local-only and enables RELATIONSHIP_UUID_HANDOFFS_ENABLED." \
    "Re-run with M3_DEMO_CONFIRM=1 (or use: make m3-demo-backend)." >&2
  exit 2
fi

export RELATIONSHIP_UUID_HANDOFFS_ENABLED=true
printf '%s\n' \
  "M3 demo mode: RELATIONSHIP_UUID_HANDOFFS_ENABLED=true" \
  "This process is not a production rollout; stop it before running dogfood or release commands." >&2

exec "$SCRIPT_DIR/dev.sh" "$@"
