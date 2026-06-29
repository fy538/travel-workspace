#!/usr/bin/env bash
# import-latent-corpus — Phase 2c catalog import for proof_only cities.
#
# Ensures city place rows, imports editorial MD from content/staging/{city}/,
# and runs embed passes for fan-out search. No dogfood manifest fixtures.
#
# Usage:
#   scripts/import-latent-corpus.sh TIER=a              # dry-run city list
#   APPLY=1 PROFILE=local make import-latent-corpus TIER=a
#   APPLY=1 PROFILE=local make import-latent-corpus CITY=paris
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"

TIER=""
CITY=""
for arg in "$@"; do
  case "$arg" in
    TIER=*) TIER="${arg#TIER=}" ;;
    CITY=*) CITY="${arg#CITY=}" ;;
    PROFILE=*) PROFILE="${arg#PROFILE=}" ;;
  esac
done
TIER="${TIER:-${TIER_ENV:-a}}"
CITY="${CITY:-${CITY_ENV:-}}"
PROFILE="${PROFILE:-${PROFILE_ENV:-local}}"
APPLY="${APPLY:-0}"
GLOBAL_EMBED_ONLY="${GLOBAL_EMBED_ONLY:-0}"

# shellcheck source=scripts/dogfood-env.sh
source "$SCRIPT_DIR/dogfood-env.sh"
dogfood_apply_profile

if [ -n "$CITY" ]; then
  CITIES=("$CITY")
elif [ "$TIER" = "a" ]; then
  CITIES=(paris barcelona venice amalfi-coast nice)
elif [ "$TIER" = "b" ]; then
  CITIES=(
    athens bilbao bologna bordeaux cagliari catania dubrovnik florence genoa
    granada ibiza lecce lyon madrid malaga mallorca marseille milan naples
    palermo porto san-sebastian seville split thessaloniki valencia valletta
  )
else
  echo "usage: import-latent-corpus.sh [TIER=a|b] [CITY=paris] [PROFILE=local|fly]" >&2
  exit 2
fi

if [ "$APPLY" = "1" ]; then
  MODE="APPLY (profile=$PROFILE)"
else
  MODE="DRY-RUN (profile=$PROFILE)"
fi

echo "▸ import-latent-corpus tier=${TIER:-single} cities=${CITIES[*]} mode=$MODE"
dogfood_print_stack
cd "$AGENT_DIR"
# shellcheck disable=SC1091
[ -f .venv/bin/activate ] && source .venv/bin/activate

if [ "$APPLY" = "1" ]; then
  if ! PYTHONPATH=. python -c "import sentence_transformers, einops" 2>/dev/null; then
    echo "ERROR: requires sentence-transformers and einops in travel-agent .venv." >&2
    exit 1
  fi
  if [ "$PROFILE" = "local" ]; then
    if ! PYTHONPATH=. python -c "
from backend.core.vector.client import get_qdrant_client
get_qdrant_client().get_collections()
" 2>/dev/null; then
      echo "ERROR: local Qdrant unreachable at $QDRANT_URL" >&2
      exit 1
    fi
    PYTHONPATH=. python -c "from backend.core.vector.collections import ensure_collections; ensure_collections()"
  else
    if ! PYTHONPATH=. python -c "
from backend.core.vector.client import get_qdrant_client
get_qdrant_client().get_collections()
" 2>/dev/null; then
      echo "ERROR: Fly Qdrant unreachable at $QDRANT_URL" >&2
      exit 1
    fi
    PYTHONPATH=. python -c "from backend.core.vector.collections import ensure_collections; ensure_collections()"
  fi
else
  echo "Would import: ${CITIES[*]}"
  for city in "${CITIES[@]}"; do
    count=$(ls "content/staging/$city"/*.md 2>/dev/null | wc -l | tr -d ' ')
    echo "  $city: ~$count MD files"
  done
  exit 0
fi

if [ "$GLOBAL_EMBED_ONLY" = "1" ]; then
  echo ""
  echo "== Global embed passes only (GLOBAL_EMBED_ONLY=1) =="
  PYTHONPATH=. python scripts/embed_experience_briefs.py
  PYTHONPATH=. python scripts/embed_place_angles_staging.py || \
    echo "  (place angles embed skipped — non-fatal)"
  echo ""
  echo "✓ global embed complete (profile=$PROFILE qdrant=$DOGFOOD_QDRANT_HOST)."
  exit 0
fi

echo "== 1. Ensure city place rows =="
if [ -n "$CITY" ]; then
  PYTHONPATH=. python scripts/ensure_corpus_cities.py --city "$CITY"
else
  PYTHONPATH=. python scripts/ensure_corpus_cities.py --tier "${TIER:-a}"
fi

for city in "${CITIES[@]}"; do
  echo ""
  echo "== 2. Import editorial dossiers: $city =="
  if [ ! -d "content/staging/$city" ]; then
    echo "  (skip — no content/staging/$city)" >&2
    continue
  fi
  PYTHONPATH=. python scripts/import_cursor_dossiers.py --city "$city"

  echo ""
  echo "== 3. Embed eval briefs: $city =="
  PYTHONPATH=. python scripts/embed_eval_briefs.py --city "$city"
done

echo ""
echo "== 4. Global embed passes =="
PYTHONPATH=. python scripts/embed_experience_briefs.py
PYTHONPATH=. python scripts/embed_place_angles_staging.py || \
  echo "  (place angles embed skipped — non-fatal)"

echo ""
echo "✓ import-latent-corpus complete for ${CITIES[*]} ($MODE)."
