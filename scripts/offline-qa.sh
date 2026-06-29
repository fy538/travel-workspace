#!/usr/bin/env bash
# Offline-first reliability ladder for Travel Workspace.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"
APP_DIR="$WORKSPACE_DIR/travel-app"

header() {
  printf "\n== %s ==\n" "$1"
}

export DISABLE_LLM_BACKGROUND_LOOPS="${DISABLE_LLM_BACKGROUND_LOOPS:-true}"
export EXPO_PUBLIC_USE_MOCK_API="${EXPO_PUBLIC_USE_MOCK_API:-true}"
export EXPO_PUBLIC_SKIP_AUTH="${EXPO_PUBLIC_SKIP_AUTH:-true}"

header "Workspace doctor"
"$WORKSPACE_DIR/scripts/doctor.sh"

header "Contract drift"
"$WORKSPACE_DIR/scripts/contract-check.sh"

header "API coverage"
python3 "$WORKSPACE_DIR/scripts/api-coverage-check.py"

header "Backend import boundaries"
(
  cd "$AGENT_DIR"
  python3 scripts/check_imports.py --ci
)

header "Backend offline tests"
(
  cd "$AGENT_DIR"
  SKIP_AUTH=true PYTHONPATH=. pytest tests/ -q -k "not requires_postgres and not requires_api_keys"
)

header "Journey mock-walk (tier 1)"
(
  cd "$APP_DIR"
  npm test -- __tests__/journeys/
)

header "Frontend typecheck"
(
  cd "$APP_DIR"
  npx tsc --noEmit
)

header "Frontend offline tests"
(
  cd "$APP_DIR"
  npm run test:offline
)

printf "\nOffline QA passed. Live LLM canaries are optional next, not required.\n"
