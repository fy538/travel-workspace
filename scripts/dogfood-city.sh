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
# Environment profiles (Phase 0.5):
#   PROFILE=local  — Docker Postgres + Docker Qdrant (default workbench)
#   PROFILE=fly    — PROD_DATABASE_URL + cloud Qdrant (EAS / AI QA)
#
# Usage:
#   scripts/dogfood-city.sh CITY=lisbon                         # dry-run (local profile)
#   APPLY=1 scripts/dogfood-city.sh CITY=rome                   # write to local Postgres
#   APPLY=1 ENRICH=1 PROFILE=local make dogfood-city CITY=rome  # full enrich on local stack
#   APPLY=1 scripts/dogfood-promote.sh CITY=lisbon              # Fly promotion wrapper
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"

# ── Args ────────────────────────────────────────────────────────────────────
CITY=""
for arg in "$@"; do
  case "$arg" in
    CITY=*) CITY="${arg#CITY=}" ;;
    PROFILE=*) PROFILE="${arg#PROFILE=}" ;;
  esac
done
CITY="${CITY:-${CITY_ENV:-}}"
PROFILE="${PROFILE:-${PROFILE_ENV:-local}}"
if [ -z "$CITY" ]; then
  echo "usage: scripts/dogfood-city.sh CITY=<lisbon|rome|tokyo|istanbul|brooklyn> [PROFILE=local|fly]" >&2
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
SLUG_BRIDGE="tools/dogfood/content/manifests/elif-rome-slug-bridge.yaml"
APPLY="${APPLY:-0}"
ENRICH="${ENRICH:-0}"

# shellcheck source=scripts/dogfood-env.sh
source "$SCRIPT_DIR/dogfood-env.sh"
dogfood_apply_profile

if [ "$APPLY" = "1" ]; then
  WRITE="--apply"
  MODE="APPLY (profile=$PROFILE postgres=$DOGFOOD_PG_HOST qdrant=$DOGFOOD_QDRANT_HOST)"
else
  WRITE=""
  MODE="DRY-RUN (profile=$PROFILE)"
fi

echo "▸ dogfood-city CITY=$CITY  manifest=$STEM  mode=$MODE"
dogfood_print_stack
cd "$AGENT_DIR"
# shellcheck disable=SC1091
[ -f .venv/bin/activate ] && source .venv/bin/activate

echo ""
echo "== 1. Corpus audit (read-only) =="
PYTHONPATH=. python -m tools.dogfood.content.corpus_refs "$MANIFEST" | tail -1

echo ""
echo "== 2. Import staged corpus refs $WRITE =="
PYTHONPATH=. python -m tools.dogfood.content.import_staged_refs "$MANIFEST" $WRITE $(dogfood_allow_prod_flag)

if [ "$ENRICH" = "1" ]; then
  echo ""
  echo "== 2b. Editorial dossiers + embed (ENRICH) =="
  if [ "$APPLY" = "1" ]; then
    if ! PYTHONPATH=. python -c "import sentence_transformers, einops" 2>/dev/null; then
      echo "ERROR: ENRICH requires sentence-transformers and einops in travel-agent .venv." >&2
      echo "  Run: cd travel-agent && .venv/bin/pip install sentence-transformers einops" >&2
      exit 1
    fi
    if [ "$PROFILE" = "local" ]; then
      if ! PYTHONPATH=. python -c "
from backend.core.vector.client import get_qdrant_client
get_qdrant_client().get_collections()
" 2>/dev/null; then
        echo "ERROR: local Qdrant unreachable at $QDRANT_URL — start with: cd travel-agent && docker compose up -d qdrant" >&2
        exit 1
      fi
      PYTHONPATH=. python -c "from backend.core.vector.collections import ensure_collections; ensure_collections()"
    fi
    if [ -d "content/staging/$CITY" ]; then
      PYTHONPATH=. python scripts/import_cursor_dossiers.py --city "$CITY"
    else
      echo "  (no content/staging/$CITY — skipping MD dossier import)"
    fi
    case "$CITY" in
      tokyo|brooklyn)
        echo ""
        echo "== 2b1. Staging JSON briefs for manifest slugs =="
        PYTHONPATH=. python -m tools.dogfood.content.import_staged_briefs \
          "$MANIFEST" --apply $(dogfood_allow_prod_flag)
        ;;
    esac
    if [ "$CITY" = "istanbul" ]; then
      echo ""
      echo "== 2b2. Istanbul experience briefs from staging MD =="
      PYTHONPATH=. python -m tools.dogfood.content.import_experience_briefs \
        --city istanbul --apply $(dogfood_allow_prod_flag)
    fi
    if [ "$CITY" = "rome" ] && [ -f "$SLUG_BRIDGE" ]; then
      echo ""
      echo "== 2c. Rome manifest ↔ editorial slug bridge =="
      PYTHONPATH=. python -m tools.dogfood.content.slug_bridge "$SLUG_BRIDGE" --apply --re-embed $(dogfood_allow_prod_flag)
    fi
    case "$CITY" in
      lisbon|rome|istanbul|tokyo)
        PYTHONPATH=. python scripts/embed_eval_briefs.py --city "$CITY"
        ;;
      brooklyn)
        PYTHONPATH=. python -m tools.dogfood.content.embed_manifest_briefs "$MANIFEST"
        ;;
      *)
        echo "  (embed_eval_briefs: no city config for $CITY — import_cursor_dossiers inline embed only)"
        ;;
    esac
    PYTHONPATH=. python scripts/embed_experience_briefs.py
    PYTHONPATH=. python scripts/embed_place_angles_staging.py || \
      echo "  (place angles embed skipped — see errors above; often non-$CITY slugs in staging JSON)"
  else
    echo "  (dry-run: would run import_cursor_dossiers + slug_bridge + embed_*; needs network/keys)"
    if [ -d "content/staging/$CITY" ]; then
      PYTHONPATH=. python scripts/import_cursor_dossiers.py --city "$CITY" --dry-run | tail -5
    fi
    if [ "$CITY" = "rome" ] && [ -f "$SLUG_BRIDGE" ]; then
      PYTHONPATH=. python -m tools.dogfood.content.slug_bridge "$SLUG_BRIDGE"
    fi
  fi
fi

echo ""
echo "== 3. Validate manifest =="
PYTHONPATH=. python -m tools.dogfood.content.validate "$MANIFEST"

if [ "$APPLY" = "1" ]; then
  echo ""
  echo "== 4. Bootstrap dogfood users =="
  PYTHONPATH=. python -m tools.dogfood.content.bootstrap_users --apply "$MANIFEST" $(dogfood_allow_prod_flag)

  echo ""
  echo "== 5. Seed fixtures =="
  PYTHONPATH=. python -m tools.dogfood.content.seed "$MANIFEST" --apply $(dogfood_allow_prod_flag)
else
  echo ""
  echo "== 4-5. Bootstrap + seed (dry-run preview) =="
  PYTHONPATH=. python -m tools.dogfood.content.seed "$MANIFEST"
fi

echo ""
echo "✓ dogfood-city CITY=$CITY complete ($MODE)."
[ "$APPLY" = "1" ] || echo "  Re-run with APPLY=1 to write, APPLY=1 ENRICH=1 to also import dossiers."
