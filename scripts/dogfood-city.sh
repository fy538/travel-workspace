#!/usr/bin/env bash
# dogfood-city — one-command corpus connection + fixture seed for a dogfood city.
#
# Generalizes seed-s4-local.sh into the full A+B+fixture connection from
# docs/working/dogfood-corpus-connection-plan-2026-06-28.md:
#   audit (corpus_refs) → import staged corpus refs → validate → bootstrap users → seed
#
# Dossier/Qdrant enrichment (import_cursor_dossiers + embed) is intentionally a
# SEPARATE opt-in step (needs network/keys) — pass ENRICH=1 to include it.
#
# Usage:
#   scripts/dogfood-city.sh CITY=lisbon                 # dry-run (no writes)
#   APPLY=1 scripts/dogfood-city.sh CITY=rome           # write to local Postgres
#   APPLY=1 ENRICH=1 scripts/dogfood-city.sh CITY=rome  # also import dossiers + embed
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"

# ── Args ────────────────────────────────────────────────────────────────────
CITY=""
for arg in "$@"; do
  case "$arg" in
    CITY=*) CITY="${arg#CITY=}" ;;
  esac
done
CITY="${CITY:-${CITY_ENV:-}}"
if [ -z "$CITY" ]; then
  echo "usage: scripts/dogfood-city.sh CITY=<lisbon|rome|tokyo|istanbul|brooklyn>" >&2
  exit 2
fi

# ── City → manifest stem map ─────────────────────────────────────────────────
case "$CITY" in
  lisbon)   STEM="lisbon-phase1" ;;
  rome)     STEM="elif-rome" ;;
  tokyo)    STEM="tokyo-phase1" ;;
  istanbul) STEM="istanbul-phase1" ;;
  brooklyn) STEM="brooklyn-phase1" ;;
  *) echo "unknown CITY '$CITY' (expected lisbon|rome|tokyo|istanbul|brooklyn)" >&2; exit 2 ;;
esac

MANIFEST="tools/dogfood/content/manifests/$STEM.yaml"
APPLY="${APPLY:-0}"
ENRICH="${ENRICH:-0}"
export DATABASE_URL="${DATABASE_URL:-postgresql://vesper:localdev@localhost:5432/vesper}"

if [ "$APPLY" = "1" ]; then WRITE="--apply"; MODE="APPLY (writes to $DATABASE_URL)"; else WRITE=""; MODE="DRY-RUN (no writes)"; fi

echo "▸ dogfood-city CITY=$CITY  manifest=$STEM  mode=$MODE"
cd "$AGENT_DIR"
# shellcheck disable=SC1091
[ -f .venv/bin/activate ] && source .venv/bin/activate

echo ""
echo "== 1. Corpus audit (read-only) =="
PYTHONPATH=. python -m tools.dogfood.content.corpus_refs "$MANIFEST" | tail -1

echo ""
echo "== 2. Import staged corpus refs $WRITE =="
PYTHONPATH=. python -m tools.dogfood.content.import_staged_refs "$MANIFEST" $WRITE

if [ "$ENRICH" = "1" ]; then
  echo ""
  echo "== 2b. Editorial dossiers + embed (ENRICH) =="
  if [ "$APPLY" = "1" ]; then
    PYTHONPATH=. python scripts/import_cursor_dossiers.py --city "$CITY" || echo "  (dossier import skipped/failed — see output)"
    PYTHONPATH=. python scripts/embed_eval_briefs.py || true
    PYTHONPATH=. python scripts/embed_experience_briefs.py || true
  else
    echo "  (dry-run: would run import_cursor_dossiers --city $CITY + embed_*; needs network/keys)"
  fi
fi

echo ""
echo "== 3. Validate manifest =="
PYTHONPATH=. python -m tools.dogfood.content.validate "$MANIFEST"

if [ "$APPLY" = "1" ]; then
  echo ""
  echo "== 4. Bootstrap dogfood users =="
  PYTHONPATH=. python -m tools.dogfood.content.bootstrap_users --apply "$MANIFEST"

  echo ""
  echo "== 5. Seed fixtures =="
  PYTHONPATH=. python -m tools.dogfood.content.seed "$MANIFEST" --apply
else
  echo ""
  echo "== 4-5. Bootstrap + seed (dry-run preview) =="
  PYTHONPATH=. python -m tools.dogfood.content.seed "$MANIFEST"
fi

echo ""
echo "✓ dogfood-city CITY=$CITY complete ($MODE)."
[ "$APPLY" = "1" ] || echo "  Re-run with APPLY=1 to write, APPLY=1 ENRICH=1 to also import dossiers."
