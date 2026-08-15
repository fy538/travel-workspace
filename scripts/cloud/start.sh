#!/usr/bin/env bash
# start.sh — Cursor Cloud Agent start phase for the Travel Workspace.
#
# Per-boot runtime reconciliation: starts the Docker daemon, brings up the
# Postgres + Qdrant infra containers, waits for Postgres, applies Alembic
# migrations, and launches the FastAPI backend (uvicorn) in the background so
# the API is live on boot. Idempotent and safe to re-run; it reaches a clear
# success or failure state and then returns.
#
# For an attached/foreground API with live logs instead, use `make dev-backend`
# from the workspace root (reads travel-agent/.env). Background API logs are at
# /tmp/api-server.log.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
REPOS_PARENT="$(dirname "$WORKSPACE_DIR")"
AGENT_DIR="$REPOS_PARENT/travel-agent"

DEV_DATABASE_URL="${DATABASE_URL:-postgresql://vesper:localdev@localhost:15432/vesper}"

log() { printf '\033[1;36m▸ %s\033[0m\n' "$1"; }

# ── 1. Docker daemon ──────────────────────────────────────────────────────────
# The nested-container VM does not auto-start dockerd. Storage driver
# (fuse-overlayfs) and iptables-legacy are configured in the base snapshot.
if ! docker info >/dev/null 2>&1; then
  log "Starting Docker daemon"
  sudo bash -c 'dockerd >/tmp/dockerd.log 2>&1 &'
  for _ in $(seq 1 30); do
    if sudo docker info >/dev/null 2>&1; then break; fi
    sleep 1
  done
fi
# Allow non-root docker access for this and later sessions.
sudo chmod 666 /var/run/docker.sock 2>/dev/null || true
if ! docker info >/dev/null 2>&1; then
  echo "✗ Docker daemon did not become ready — see /tmp/dockerd.log" >&2
  exit 1
fi

# ── 2. Infra containers (Postgres + Qdrant) ───────────────────────────────────
cd "$AGENT_DIR"
log "Starting Postgres + Qdrant (docker compose up -d)"
docker compose up -d

log "Waiting for Postgres to accept connections"
# On a fresh pgdata volume the postgis entrypoint runs initdb and briefly
# starts a temporary server before restarting the real one, so a single
# pg_isready can pass during that window. Require a real `SELECT 1` against the
# vesper database (authoritative that the real server + db are up) before
# proceeding.
pg_ready=false
for i in $(seq 1 90); do
  if docker compose exec -T postgres pg_isready -U vesper -d vesper >/dev/null 2>&1 \
     && docker compose exec -T postgres psql -U vesper -d vesper -tAc 'SELECT 1' >/dev/null 2>&1; then
    log "Postgres ready after ${i}s"
    pg_ready=true
    break
  fi
  sleep 1
done
if [ "$pg_ready" != true ]; then
  echo "✗ Postgres did not become ready — see 'docker compose logs postgres'" >&2
  exit 1
fi

# ── 3. Qdrant health (fuse-overlayfs stale-volume guard) ──────────────────────
# On the nested-container VM, Qdrant can crash-loop on a volume carried inside a
# base snapshot ("Invalid cross-device link" while cleaning its snapshots temp
# dir). If it does not report healthy shortly after boot, recreate its volume
# from clean. Qdrant holds no durable dev state until a seeding script runs.
PROJECT="$(basename "$AGENT_DIR")"
qdrant_ok=false
for _ in $(seq 1 15); do
  if curl -fsS http://localhost:6333/healthz >/dev/null 2>&1; then qdrant_ok=true; break; fi
  sleep 1
done
if [ "$qdrant_ok" != true ]; then
  log "Qdrant not healthy — recreating its volume from clean"
  docker compose rm -sf qdrant >/dev/null 2>&1 || true
  docker volume rm "${PROJECT}_qdrant_data" >/dev/null 2>&1 || true
  docker compose up -d qdrant
fi

# ── 4. Database migrations ────────────────────────────────────────────────────
log "Applying Alembic migrations"
migrated=false
for attempt in 1 2 3 4 5; do
  if DATABASE_URL="$DEV_DATABASE_URL" PYTHONPATH=. .venv/bin/alembic upgrade head; then
    migrated=true
    break
  fi
  echo "  migration attempt ${attempt} failed (Postgres may still be settling) — retrying" >&2
  sleep 3
done
if [ "$migrated" != true ]; then
  echo "✗ Alembic migrations failed after retries" >&2
  exit 1
fi

# ── 5. API server (background) ────────────────────────────────────────────────
# Launch uvicorn detached so the API is live on boot. Idempotent: skip if
# something is already serving on :8000. A real ANTHROPIC_API_KEY from the
# environment/secret is used when present; otherwise a placeholder lets the
# server boot for non-AI development.
if curl -fsS http://localhost:8000/health >/dev/null 2>&1; then
  log "API already serving on :8000 — not relaunching"
else
  log "Launching API server (background) — logs at /tmp/api-server.log"
  DATABASE_URL="$DEV_DATABASE_URL" \
    SKIP_AUTH="${SKIP_AUTH:-true}" \
    DEFAULT_DEV_USER_ID="${DEFAULT_DEV_USER_ID:-00000000-0000-0000-0000-000000000005}" \
    ANTHROPIC_API_KEY="${ANTHROPIC_API_KEY:-sk-placeholder-not-configured}" \
    PYTHONPATH=. nohup .venv/bin/uvicorn backend.api.main:app \
    --host 0.0.0.0 --port 8000 --no-access-log >/tmp/api-server.log 2>&1 &
fi

log "start.sh complete — infra up, migrations applied, API server launched"
