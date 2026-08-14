#!/usr/bin/env bash
# start.sh — Cursor Cloud Agent start phase for the Travel Workspace.
#
# Per-boot runtime reconciliation: starts the Docker daemon, brings up the
# Postgres + Qdrant infra containers, waits for Postgres, and applies Alembic
# migrations. Idempotent and safe to re-run; it must reach a clear success or
# failure state and then return so the terminals can start.

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
for i in $(seq 1 60); do
  if docker compose exec -T postgres pg_isready -U vesper >/dev/null 2>&1; then
    log "Postgres ready after ${i}s"
    break
  fi
  if [ "$i" -eq 60 ]; then
    echo "✗ Postgres did not become ready — see 'docker compose logs postgres'" >&2
    exit 1
  fi
  sleep 1
done

# ── 3. Database migrations ────────────────────────────────────────────────────
log "Applying Alembic migrations"
DATABASE_URL="$DEV_DATABASE_URL" PYTHONPATH=. .venv/bin/alembic upgrade head

log "start.sh complete — infra up, migrations applied"
