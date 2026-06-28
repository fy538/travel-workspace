#!/usr/bin/env bash
# Seed S4 (Lisbon group planning) to Fly Postgres — no LLM calls.
#
# Requires travel-agent/.env.prod with PROD_DATABASE_URL (Neon/Fly postgres).
# Uses --allow-prod guard on bootstrap_users + seed (cohort @dogfood.local only).
#
# Usage:
#   ./scripts/seed-s4-fly.sh              # dry-run (default)
#   SEED_S4_FLY_APPLY=1 ./scripts/seed-s4-fly.sh   # write to Fly DB
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"
ENV_PROD="$AGENT_DIR/.env.prod"
MANIFEST="$AGENT_DIR/tools/dogfood/content/manifests/lisbon-phase1.yaml"
APPLY="${SEED_S4_FLY_APPLY:-0}"

if [[ ! -f "$ENV_PROD" ]]; then
  echo "Missing $ENV_PROD — add PROD_DATABASE_URL for Fly/Neon postgres." >&2
  exit 1
fi

cd "$AGENT_DIR"
source .venv/bin/activate

PROD_DATABASE_URL="$(
  PYTHONPATH=. python - <<'PY'
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(Path(".env.prod"), override=False)
print(os.environ.get("PROD_DATABASE_URL", ""))
PY
)"

if [[ -z "$PROD_DATABASE_URL" ]]; then
  echo "PROD_DATABASE_URL is not set in $ENV_PROD" >&2
  exit 1
fi

export DATABASE_URL="$PROD_DATABASE_URL"
export ENVIRONMENT="${ENVIRONMENT:-production}"

APPLY_FLAG=()
ALLOW_PROD=()
if [[ "$APPLY" == "1" ]]; then
  APPLY_FLAG=(--apply)
  ALLOW_PROD=(--allow-prod)
  echo "== APPLY mode — writing to remote Postgres =="
else
  echo "== Dry-run mode — pass SEED_S4_FLY_APPLY=1 to write =="
fi

# Prod DB should already have Lisbon catalog rows; dogfood seed creates venue stubs as needed.
# Do NOT run load_eval_fixtures here — it targets eval harness data, not dogfood cohort writes.

echo "== Validate manifest =="
PYTHONPATH=. python -m tools.dogfood.content.validate "$MANIFEST"

echo "== Bootstrap dogfood users =="
if ((${#APPLY_FLAG[@]})); then
  PYTHONPATH=. python -m tools.dogfood.content.bootstrap_users \
    "${APPLY_FLAG[@]}" "${ALLOW_PROD[@]}" "$MANIFEST"
else
  PYTHONPATH=. python -m tools.dogfood.content.bootstrap_users "$MANIFEST"
fi

echo "== Seed lisbon-phase1 =="
if ((${#APPLY_FLAG[@]})); then
  PYTHONPATH=. python -m tools.dogfood.content.seed \
    "$MANIFEST" "${APPLY_FLAG[@]}" "${ALLOW_PROD[@]}"
else
  PYTHONPATH=. python -m tools.dogfood.content.seed "$MANIFEST"
fi

if [[ "$APPLY" == "1" ]]; then
  echo "== Post-seed audit (mara@dogfood.local) =="
  PYTHONPATH=. python scripts/dogfood_audit.py \
    --summary --persona mara@dogfood.local --no-target-banner
  echo "S4 Fly seed complete."
else
  echo "Dry-run complete. Re-run with SEED_S4_FLY_APPLY=1 to apply."
fi
