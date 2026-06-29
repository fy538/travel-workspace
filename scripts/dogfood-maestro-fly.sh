#!/usr/bin/env bash
# Maestro wedge against Fly API — S4 mara-lisbon trip + J04 chat eval.
#
# Requires:
#   - PRELAUNCH_JWT_MARA (Clerk JWT for mara@dogfood.local on Fly)
#   - iOS simulator + maestro
#   - Fly substrate promoted (make dogfood-fly-smoke green)
#
# Usage:
#   PRELAUNCH_JWT_MARA=eyJ... scripts/dogfood-maestro-fly.sh
#   RUN_MAESTRO=0 PRELAUNCH_JWT_MARA=... scripts/dogfood-maestro-fly.sh  # HTTP eval only
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"
APP_DIR="$WORKSPACE_DIR/travel-app"
FLY_HOST="${PRELAUNCH_HOST:-https://vesper-backend.fly.dev}"
RUN_MAESTRO="${RUN_MAESTRO:-1}"
JWT="${PRELAUNCH_JWT_MARA:-${PRELAUNCH_JWT:-}}"

bold() { printf "\033[1m%s\033[0m\n" "$1"; }
ok() { printf "  \033[32m✓\033[0m %s\n" "$1"; }
fail() { printf "  \033[31m✗\033[0m %s\n" "$1"; }
warn() { printf "  \033[33m⚠\033[0m %s\n" "$1"; }

if [[ -z "$JWT" ]]; then
  fail "PRELAUNCH_JWT_MARA (or PRELAUNCH_JWT) required for Fly Maestro"
  exit 1
fi

bold "S4 Maestro (Fly API)"

bold "1/4 Fly ready"
if curl -sf "$FLY_HOST/ready" >/dev/null; then
  ok "$FLY_HOST/ready"
else
  fail "$FLY_HOST/ready failed"
  exit 1
fi

bold "2/4 J04 chat eval (HTTP)"
if PROFILE=fly TRANSPORT=http PRELAUNCH_JWT_MARA="$JWT" PRELAUNCH_HOST="$FLY_HOST" \
  "$SCRIPT_DIR/dogfood-journey-j04-chat-eval.sh"; then
  ok "J04 chat eval on Fly"
else
  fail "J04 chat eval failed — promote substrate: APPLY=1 make dogfood-promote CITY=lisbon"
  exit 1
fi

bold "3/4 Journey live API read-only on S4 (HTTP)"
if PROFILE=fly TRANSPORT=http PRELAUNCH_JWT_MARA="$JWT" PRELAUNCH_HOST="$FLY_HOST" \
  "$SCRIPT_DIR/dogfood-journey-live-api.sh" 2>&1 | tee /tmp/dogfood-maestro-fly-journey-api.txt; then
  ok "journey live API HTTP"
else
  warn "journey live API HTTP had failures — see /tmp/dogfood-maestro-fly-journey-api.txt"
fi

if [[ "$RUN_MAESTRO" != "1" ]]; then
  bold "4/4 Maestro — skipped (RUN_MAESTRO=0)"
  bold "Fly Maestro PASSED (HTTP eval only)."
  exit 0
fi

if ! command -v maestro >/dev/null 2>&1; then
  warn "maestro not in PATH — skip UI"
  exit 0
fi

bold "4/4 Maestro 26 against Fly"
METRO_PID=""
cleanup() {
  [[ -n "$METRO_PID" ]] && kill "$METRO_PID" 2>/dev/null || true
}
trap cleanup EXIT

cd "$APP_DIR"
export EXPO_PUBLIC_USE_MOCK_API=false
export EXPO_PUBLIC_SKIP_AUTH=false
export EXPO_PUBLIC_DOGFOOD_JWT="$JWT"
export EXPO_PUBLIC_API_URL="$FLY_HOST"
export JAVA_HOME="${JAVA_HOME:-/opt/homebrew/opt/openjdk}"
export PATH="$JAVA_HOME/bin:$HOME/.maestro/bin:$PATH"

npx expo start --ios --non-interactive >/tmp/dogfood-fly-metro.log 2>&1 &
METRO_PID=$!
sleep 25

if maestro test .maestro/26-journey-s4-mara-lisbon.yaml; then
  ok "Maestro 26 on Fly passed"
else
  fail "Maestro 26 failed — see /tmp/dogfood-fly-metro.log"
  exit 1
fi

bold "Fly Maestro PASSED."
