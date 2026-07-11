#!/usr/bin/env bash
# Seed S4 (Lisbon group planning) to local Postgres — no LLM calls.
set -euo pipefail

ATTIC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPTS_DIR="$(dirname "$ATTIC_DIR")"
WORKSPACE_DIR="$(dirname "$SCRIPTS_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"
MANIFEST="$AGENT_DIR/tools/dogfood/content/manifests/lisbon-phase1.yaml"

export DATABASE_URL="${DATABASE_URL:-postgresql://vesper:localdev@localhost:5432/vesper}"

cd "$AGENT_DIR"
source .venv/bin/activate

echo "== Migrate =="
PYTHONPATH=. alembic upgrade head

echo "== Eval fixtures (venue catalog) =="
PYTHONPATH=. python scripts/load_eval_fixtures.py

echo "== Validate manifest =="
PYTHONPATH=. python -m tools.dogfood.content.validate "$MANIFEST"

echo "== Bootstrap dogfood users =="
PYTHONPATH=. python -m tools.dogfood.content.bootstrap_users --apply "$MANIFEST"

echo "== Seed lisbon-phase1 =="
PYTHONPATH=. python -m tools.dogfood.content.seed "$MANIFEST" --apply

echo "S4 local seed complete."
