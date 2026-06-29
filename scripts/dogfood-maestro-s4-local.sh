#!/usr/bin/env bash
# Maestro wedge on dogfood S4 trip — real local API (SKIP_AUTH as Mara).
#
# Prerequisites: local Postgres seeded (APPLY=1 make dogfood-city CITY=lisbon),
# iOS simulator, maestro in PATH.
#
# Usage:
#   scripts/dogfood-maestro-s4-local.sh
#   RUN_MAESTRO=0 scripts/dogfood-maestro-s4-local.sh   # API eval only
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"
APP_DIR="$WORKSPACE_DIR/travel-app"
RUN_MAESTRO="${RUN_MAESTRO:-1}"

bold() { printf "\033[1m%s\033[0m\n" "$1"; }
ok() { printf "  \033[32m✓\033[0m %s\n" "$1"; }
fail() { printf "  \033[31m✗\033[0m %s\n" "$1"; }
warn() { printf "  \033[33m⚠\033[0m %s\n" "$1"; }

bold "S4 Maestro (local real API)"

bold "1/3 J04 chat eval (TestClient)"
if PROFILE=local TRANSPORT=testclient "$SCRIPT_DIR/dogfood-journey-j04-chat-eval.sh"; then
  ok "J04 chat eval passed"
else
  fail "J04 chat eval failed — seed: APPLY=1 make dogfood-city CITY=lisbon"
  exit 1
fi

if [[ "$RUN_MAESTRO" != "1" ]]; then
  bold "2/3 Maestro — skipped (RUN_MAESTRO=0)"
  bold "S4 local Maestro PASSED (API eval only)."
  exit 0
fi

if ! command -v maestro >/dev/null 2>&1; then
  warn "maestro not in PATH — skip UI (install: brew tap mobile-dev-inc/tap && brew install maestro)"
  exit 0
fi

bold "2/3 Docker + local API (SKIP_AUTH as Mara)"
cd "$AGENT_DIR"
if ! docker compose ps --status running 2>/dev/null | grep -q postgres; then
  docker compose up -d
  sleep 3
fi

MARA_ID="$(cd "$AGENT_DIR" && source .venv/bin/activate && PROFILE=local PYTHONPATH=. python - <<'PY'
from sqlalchemy import select
from backend.core.db.engine import get_connection
from backend.core.db.tables import users
with get_connection() as conn:
    print(conn.execute(select(users.c.id).where(users.c.email == "mara@dogfood.local")).scalar())
PY
)"

API_PID=""
METRO_PID=""
cleanup() {
  [[ -n "$API_PID" ]] && kill "$API_PID" 2>/dev/null || true
  [[ -n "$METRO_PID" ]] && kill "$METRO_PID" 2>/dev/null || true
}
trap cleanup EXIT

cd "$AGENT_DIR"
source .venv/bin/activate
export SKIP_AUTH=true
export DEFAULT_DEV_USER_ID="$MARA_ID"
export AI_MODE=replay
export ATLAS_BOARD_COPY_LLM_ENABLED=false
export DISABLE_LLM_BACKGROUND_LOOPS=true
PYTHONPATH=. uvicorn backend.api.main:app --host 127.0.0.1 --port 8765 >/tmp/dogfood-s4-api.log 2>&1 &
API_PID=$!
for _ in $(seq 1 30); do
  curl -sf http://127.0.0.1:8765/ready >/dev/null && break
  sleep 1
done
if ! curl -sf http://127.0.0.1:8765/ready >/dev/null; then
  fail "local API did not become ready — see /tmp/dogfood-s4-api.log"
  exit 1
fi
ok "local API on :8765"

bold "3/3 Maestro 26 (S4 mara-lisbon)"
cd "$APP_DIR"
export EXPO_PUBLIC_USE_MOCK_API=false
export EXPO_PUBLIC_SKIP_AUTH=true
export EXPO_PUBLIC_API_URL=http://127.0.0.1:8765
unset EXPO_PUBLIC_DOGFOOD_JWT 2>/dev/null || true
export JAVA_HOME="${JAVA_HOME:-/opt/homebrew/opt/openjdk}"
export PATH="$JAVA_HOME/bin:$HOME/.maestro/bin:$PATH"

npx expo start --ios --non-interactive >/tmp/dogfood-s4-metro.log 2>&1 &
METRO_PID=$!
sleep 25

if maestro test .maestro/26-journey-s4-mara-lisbon.yaml; then
  ok "Maestro 26 passed"
else
  fail "Maestro 26 failed — see /tmp/dogfood-s4-metro.log"
  exit 1
fi

bold "S4 local Maestro PASSED."
