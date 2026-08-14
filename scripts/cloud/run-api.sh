#!/usr/bin/env bash
# run-api.sh — Cursor Cloud Agent API terminal for the Travel Workspace.
#
# Runs the FastAPI backend (uvicorn) in the foreground so its logs stay visible
# and it can be restarted from the terminal. Depends on start.sh having brought
# up Postgres + Qdrant and applied migrations.
#
# ANTHROPIC_API_KEY falls back to a placeholder so the server boots for non-AI
# development; provide a real key via the environment/secret to enable live AI.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
REPOS_PARENT="$(dirname "$WORKSPACE_DIR")"
AGENT_DIR="$REPOS_PARENT/travel-agent"

# Ensure infra (Docker + Postgres + Qdrant + migrations) is up before serving.
# start.sh is idempotent, so this is a no-op when the start phase already ran.
bash "$SCRIPT_DIR/start.sh"

cd "$AGENT_DIR"

export DATABASE_URL="${DATABASE_URL:-postgresql://vesper:localdev@localhost:15432/vesper}"
export SKIP_AUTH="${SKIP_AUTH:-true}"
export DEFAULT_DEV_USER_ID="${DEFAULT_DEV_USER_ID:-00000000-0000-0000-0000-000000000005}"
export ANTHROPIC_API_KEY="${ANTHROPIC_API_KEY:-sk-placeholder-not-configured}"
export PYTHONPATH=.

exec .venv/bin/uvicorn backend.api.main:app --host 0.0.0.0 --port 8000 --no-access-log
