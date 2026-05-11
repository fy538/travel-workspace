#!/usr/bin/env bash
# Check the seams that keep frontend mock mode aligned with the real API.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
APP_DIR="$WORKSPACE_DIR/Travel App"

header() {
  printf "\n== %s ==\n" "$1"
}

export EXPO_PUBLIC_USE_MOCK_API="${EXPO_PUBLIC_USE_MOCK_API:-true}"
export EXPO_PUBLIC_SKIP_AUTH="${EXPO_PUBLIC_SKIP_AUTH:-true}"

header "OpenAPI contract"
"$WORKSPACE_DIR/scripts/contract-check.sh"

header "TypeScript API interface parity"
(
  cd "$APP_DIR"
  npx tsc --noEmit
)

header "Mock and HTTP seam tests"
(
  cd "$APP_DIR"
  npx jest --runInBand \
    __tests__/utils/api/mock.test.ts \
    __tests__/utils/api/http.test.ts \
    __tests__/data/itinerary.test.ts \
    __tests__/data/notifications.test.ts \
    __tests__/data/proposals.test.ts \
    __tests__/data/privacy.test.ts \
    __tests__/data/planState.test.ts
)

printf "\nMock/real parity passed.\n"
