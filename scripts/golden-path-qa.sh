#!/usr/bin/env bash
# Run focused deterministic checks for the MVP golden paths.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/Travel Agent"
APP_DIR="$WORKSPACE_DIR/Travel App"

header() {
  printf "\n== %s ==\n" "$1"
}

export DISABLE_LLM_BACKGROUND_LOOPS="${DISABLE_LLM_BACKGROUND_LOOPS:-true}"
export EXPO_PUBLIC_USE_MOCK_API="${EXPO_PUBLIC_USE_MOCK_API:-true}"
export EXPO_PUBLIC_SKIP_AUTH="${EXPO_PUBLIC_SKIP_AUTH:-true}"

header "Backend golden-path invariants"
(
  cd "$AGENT_DIR"
  PYTHONPATH=. pytest \
    tests/api/test_home.py \
    tests/api/test_home_group_state.py \
    tests/api/test_plan_state.py \
    tests/api/test_proposals_api.py \
    tests/api/test_proposal_apply.py \
    tests/api/test_privacy_audit.py \
    tests/eval/test_concierge_checks.py \
    tests/eval/test_planning_checks.py \
    tests/eval/test_restaurant_checks.py \
    -q \
    -k "not requires_postgres and not requires_api_keys"
)

header "Frontend offline golden path"
(
  cd "$APP_DIR"
  npx jest --runInBand \
    __tests__/offline/goldenPath.test.ts \
    __tests__/data/planState.test.ts \
    __tests__/data/proposals.test.ts \
    __tests__/data/privacy.test.ts \
    __tests__/utils/tripMapStateParity.test.ts \
    __tests__/screens/plan.smoke.test.tsx \
    __tests__/screens/map.smoke.test.tsx
)

printf "\nGolden-path QA passed.\n"
