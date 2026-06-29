#!/usr/bin/env bash
# Simulator integration gate — local API stack + optional Maestro wedge flows.
#
# 1. Docker Postgres/Qdrant up
# 2. Live API checks via in-process TestClient (all five personas)
# 3. Optional: Maestro 24/25 against Metro (real API to localhost)
#
# Usage:
#   scripts/dogfood-five-pack-simulator.sh
#   RUN_MAESTRO=0 scripts/dogfood-five-pack-simulator.sh   # skip Maestro
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"
APP_DIR="$WORKSPACE_DIR/travel-app"
RUN_MAESTRO="${RUN_MAESTRO:-1}"

bold() { printf "\033[1m%s\033[0m\n" "$1"; }
ok() { printf "  \033[32m✓\033[0m %s\n" "$1"; }
fail() { printf "  \033[31m✗\033[0m %s\n" "$1"; }

bold "Five-pack simulator integration"

bold "1/3 Docker infra"
cd "$AGENT_DIR"
if docker compose ps --status running 2>/dev/null | grep -q postgres; then
  ok "Postgres container running"
else
  docker compose up -d
  sleep 3
  ok "Started docker compose"
fi

bold "2/3 Live API (TestClient → local Postgres)"
if PROFILE=local TRANSPORT=testclient "$SCRIPT_DIR/dogfood-five-pack-live-api.sh"; then
  ok "live API testclient passed"
else
  fail "live API testclient failed — seed with: APPLY=1 make dogfood-city CITY=lisbon"
  exit 1
fi

if [[ "$RUN_MAESTRO" != "1" ]]; then
  bold "3/3 Maestro — skipped (RUN_MAESTRO=0)"
  bold "Simulator integration PASSED (API layer)."
  exit 0
fi

bold "3/3 Maestro wedge flows (real API, local SKIP_AUTH)"
if ! command -v maestro >/dev/null 2>&1; then
  warn_msg="maestro not in PATH — skip UI flows (install: brew tap mobile-dev-inc/tap && brew install maestro)"
  printf "  \033[33m⚠\033[0m %s\n" "$warn_msg"
  bold "Simulator integration PASSED (API layer only)."
  exit 0
fi

# Resolve Mara user for SKIP_AUTH dev server Maestro will hit via Metro env.
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
PYTHONPATH=. uvicorn backend.api.main:app --host 127.0.0.1 --port 8765 >/tmp/dogfood-sim-api.log 2>&1 &
API_PID=$!
for _ in $(seq 1 30); do
  if curl -sf http://127.0.0.1:8765/ready >/dev/null; then
    break
  fi
  sleep 1
done
if ! curl -sf http://127.0.0.1:8765/ready >/dev/null; then
  fail "local API did not become ready — see /tmp/dogfood-sim-api.log"
  exit 1
fi
ok "local API on :8765 (SKIP_AUTH as mara)"

cd "$APP_DIR"
export EXPO_PUBLIC_USE_MOCK_API=false
export EXPO_PUBLIC_SKIP_AUTH=true
export EXPO_PUBLIC_API_URL=http://127.0.0.1:8765
export JAVA_HOME="${JAVA_HOME:-/opt/homebrew/opt/openjdk}"
export PATH="$JAVA_HOME/bin:$HOME/.maestro/bin:$PATH"

npx expo start --ios --non-interactive >/tmp/dogfood-sim-metro.log 2>&1 &
METRO_PID=$!
sleep 25

if maestro test .maestro/24-journey-02-create-invite.yaml .maestro/25-journey-05-proposal-mutation.yaml; then
  ok "Maestro 24 + 25 passed (real API)"
else
  fail "Maestro failed — see metro log /tmp/dogfood-sim-metro.log"
  exit 1
fi

bold "Simulator integration PASSED (API + Maestro wedge)."
