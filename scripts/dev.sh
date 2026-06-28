#!/usr/bin/env bash
# dev.sh — Start the full Travel workspace in one terminal.
#
# Launches three services with prefixed, color-coded output:
#   [DOCKER]  docker compose up (Postgres + Qdrant)
#   [API]     uvicorn backend.api.main:app --reload (travel-agent)
#   [APP]     npx expo start --ios (travel-app)
#
# Usage:
#   ./scripts/dev.sh              # start all three services
#   ./scripts/dev.sh --no-expo    # skip Expo (backend + infra only)
#   ./scripts/dev.sh --no-migrate # skip alembic upgrade head
#
# Ctrl-C shuts everything down cleanly.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"
APP_DIR="$WORKSPACE_DIR/travel-app"

# ── Flags ────────────────────────────────────────────────────────────────────

RUN_EXPO=true
RUN_MIGRATE=true

for arg in "$@"; do
  case "$arg" in
    --no-expo)    RUN_EXPO=false ;;
    --no-migrate) RUN_MIGRATE=false ;;
    --help|-h)
      echo "Usage: $0 [--no-expo] [--no-migrate]"
      exit 0
      ;;
  esac
done

# ── Colors ───────────────────────────────────────────────────────────────────

RESET='\033[0m'
BOLD='\033[1m'
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
DIM='\033[2m'

# ── Process tracking ─────────────────────────────────────────────────────────

PIDS=()

cleanup() {
  echo ""
  echo -e "${YELLOW}${BOLD}▸ Shutting down all services...${RESET}"
  for pid in "${PIDS[@]}"; do
    kill "$pid" 2>/dev/null || true
  done
  # Give processes a moment to flush
  sleep 0.5
  # Force-kill anything still alive
  for pid in "${PIDS[@]}"; do
    kill -9 "$pid" 2>/dev/null || true
  done
  echo -e "${DIM}  Done.${RESET}"
}

trap cleanup EXIT INT TERM

# ── Helpers ──────────────────────────────────────────────────────────────────

# Stream a command's stdout+stderr, prefixing each line with a colored label.
# Runs in background; appends the PID to PIDS[].
stream_prefixed() {
  local label="$1"
  local color="$2"
  shift 2
  # Run the command, pipe through awk for line prefixing
  ("$@" 2>&1 | awk -v lbl="$label" -v col="$color" -v rst="$RESET" \
    '{printf "%s[%s]%s %s\n", col, lbl, rst, $0; fflush()}') &
  PIDS+=($!)
}

log() {
  echo -e "${BOLD}${CYAN}▸ $1${RESET}"
}

warn() {
  echo -e "${YELLOW}⚠  $1${RESET}"
}

die() {
  echo -e "${RED}✗  $1${RESET}" >&2
  exit 1
}

# ── Preflight checks ──────────────────────────────────────────────────────────

command -v docker >/dev/null 2>&1 || die "docker not found. Install Docker Desktop."
command -v uvicorn >/dev/null 2>&1 || die "uvicorn not found. Run: pip install -r requirements.txt (inside travel-agent/)"
if $RUN_EXPO; then
  command -v npx >/dev/null 2>&1 || die "npx not found. Install Node.js."
fi

# ── Header ───────────────────────────────────────────────────────────────────

echo ""
echo -e "${BOLD}${MAGENTA}╔══════════════════════════════════════╗"
echo -e "║       Travel Dev Environment         ║"
echo -e "╚══════════════════════════════════════╝${RESET}"
echo ""
echo -e "  ${BLUE}[API]${RESET}    http://localhost:8000"
echo -e "  ${BLUE}[DOCS]${RESET}   http://localhost:8000/docs"
if $RUN_EXPO; then
  echo -e "  ${GREEN}[APP]${RESET}    Expo Dev Client → iOS Simulator"
fi
echo ""
echo -e "${DIM}  Ctrl-C to stop all services${RESET}"
echo ""

# ── Step 1: Docker infra ──────────────────────────────────────────────────────

log "Starting Docker infrastructure (Postgres + Qdrant)..."
(cd "$AGENT_DIR" && docker compose up -d) 2>&1 | \
  awk -v col="$BLUE" -v rst="$RESET" '{printf "%s[DOCKER]%s %s\n", col, rst, $0; fflush()}'

# ── Step 2: Wait for Postgres ─────────────────────────────────────────────────

log "Waiting for Postgres..."
attempts=0
until (cd "$AGENT_DIR" && docker compose exec -T postgres pg_isready -U vesper > /dev/null 2>&1); do
  attempts=$((attempts + 1))
  if [ $attempts -ge 30 ]; then
    die "Postgres did not become ready after 30s. Check 'docker compose logs postgres'."
  fi
  sleep 1
done
echo -e "  ${GREEN}✓${RESET} Postgres ready"

# ── Step 3: Alembic migrations ────────────────────────────────────────────────

if $RUN_MIGRATE; then
  log "Running database migrations..."
  (cd "$AGENT_DIR" && PYTHONPATH=. alembic upgrade head 2>&1) | \
    awk -v col="$BLUE" -v rst="$RESET" '{printf "%s[MIGRATE]%s %s\n", col, rst, $0; fflush()}'
  echo -e "  ${GREEN}✓${RESET} Migrations applied"
fi

# ── Step 4: Start API server ──────────────────────────────────────────────────

log "Starting API server..."
stream_prefixed "API" "$BLUE" \
  bash -c "cd '$AGENT_DIR' && PYTHONPATH=. uvicorn backend.api.main:app --reload --port 8000"

# Brief pause so the API banner prints before Expo output starts
sleep 2

# ── Step 5: Start Expo ────────────────────────────────────────────────────────

if $RUN_EXPO; then
  log "Starting Expo (iOS Simulator)..."
  stream_prefixed "APP" "$GREEN" \
    bash -c "cd '$APP_DIR' && npx expo start --ios"
fi

# ── Wait (Ctrl-C triggers cleanup via trap) ───────────────────────────────────

echo ""
echo -e "${DIM}  All services launched. Press Ctrl-C to stop.${RESET}"
echo ""

# Wait for all background processes; exit when any exits abnormally
wait
