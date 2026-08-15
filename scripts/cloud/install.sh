#!/usr/bin/env bash
# install.sh — Cursor Cloud Agent install phase for the Travel Workspace.
#
# Idempotent repository bootstrap: symlinks the two child repos into the
# workspace, builds the backend virtualenv, installs backend + frontend
# dependencies, and writes a local backend .env with dev defaults.
#
# System dependencies (Python 3.13, Docker, fuse-overlayfs, Node) live in the
# base snapshot, not here. Per-boot services live in start.sh. This script must
# stay safe to run repeatedly against cached state.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
REPOS_PARENT="$(dirname "$WORKSPACE_DIR")"
AGENT_DIR="$REPOS_PARENT/travel-agent"
APP_DIR="$REPOS_PARENT/travel-app"

log() { printf '\033[1;36m▸ %s\033[0m\n' "$1"; }

# ── 1. Link child repos into the workspace ────────────────────────────────────
# The Makefile and workspace scripts expect ./travel-agent and ./travel-app to
# live inside the workspace. Cursor clones repositoryDependencies as siblings,
# so we symlink them in. Both paths are gitignored by the workspace repo.
if [ -d "$AGENT_DIR" ]; then
  log "Linking travel-agent -> $AGENT_DIR"
  ln -sfn "$AGENT_DIR" "$WORKSPACE_DIR/travel-agent"
else
  echo "✗ travel-agent not found at $AGENT_DIR" >&2
  exit 1
fi
if [ -d "$APP_DIR" ]; then
  log "Linking travel-app -> $APP_DIR"
  ln -sfn "$APP_DIR" "$WORKSPACE_DIR/travel-app"
else
  echo "✗ travel-app not found at $APP_DIR" >&2
  exit 1
fi

# ── 2. Backend: Python 3.13 virtualenv + dependencies ─────────────────────────
cd "$AGENT_DIR"
if [ ! -x .venv/bin/python ]; then
  log "Creating backend virtualenv (.venv) with python3.13"
  python3.13 -m venv .venv
fi
log "Installing backend dependencies (requirements-dev.txt)"
.venv/bin/python -m pip install --upgrade pip >/dev/null
.venv/bin/pip install -r requirements-dev.txt

# ── 3. Backend: local dev .env ────────────────────────────────────────────────
# Matches docker-compose.yml host mappings. SKIP_AUTH bypasses Clerk; the
# synthetic dev user (backend/api/auth.py::_get_dev_user) is used when
# DEFAULT_DEV_USER_ID has no seeded row. A real ANTHROPIC_API_KEY provided via
# the environment/secret overrides the placeholder here (dotenv loads with
# override=false), enabling live AI features.
if [ ! -f .env ]; then
  log "Writing backend .env with local dev defaults"
  cat > .env <<'ENV'
POSTGRES_HOST=localhost
POSTGRES_PORT=15432
POSTGRES_USER=vesper
POSTGRES_PASSWORD=localdev
POSTGRES_DB=vesper
QDRANT_URL=http://localhost:6333

SKIP_AUTH=true
DEFAULT_DEV_USER_ID=00000000-0000-0000-0000-000000000005

ANTHROPIC_API_KEY=sk-placeholder-not-configured
ENV
fi

# ── 4. Frontend: Node dependencies ────────────────────────────────────────────
cd "$APP_DIR"
log "Installing frontend dependencies (npm ci)"
npm ci

log "install.sh complete"
