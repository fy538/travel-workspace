#!/usr/bin/env bash
# Run focused deterministic checks for the MVP golden paths.

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

header "Backend journey scenarios (J02, J05, J06)"
(
  cd "$AGENT_DIR"
  PYTHONPATH=. pytest \
    tests/scenarios/test_j02_invite_acceptance.py \
    tests/scenarios/test_j05_proposal_plan_mutation.py \
    tests/scenarios/test_j06_home_plan_map_changes_coherence.py \
    -q \
    -m requires_postgres
)

header "Frontend journey mock-walks (J02, J05, J06)"
(
  cd "$APP_DIR"
  npx jest --runInBand \
    __tests__/journeys/journey-02-mock-walk.smoke.test.tsx \
    __tests__/journeys/05-group-planning-proposal-mutation.test.ts \
    __tests__/journeys/06-cross-surface-coherence.test.ts
)

printf "\nGolden-path QA passed.\n"
