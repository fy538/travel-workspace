#!/usr/bin/env bash
# corpus-check — fail if any dogfood manifest references a slug that resolves
# neither in Postgres nor in authored staging files (missing > 0), or if manifest
# governance checks fail (corpus_tier, inline entity copies, block slug refs).
#
# Wraps travel-agent's read-only `tools.dogfood.content.corpus_refs` and
# `tools.dogfood.content.corpus_governance`.
#
# Usage:
#   scripts/corpus-check.sh                  # default wedge manifests (5 city packs)
#   CORPUS_MANIFESTS="lisbon-phase1 elif-rome" scripts/corpus-check.sh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"
MANIFEST_DIR="tools/dogfood/content/manifests"

export DATABASE_URL="${DATABASE_URL:-postgresql://vesper:localdev@localhost:5432/vesper}"

# Default: all five city packs. Override with CORPUS_MANIFESTS (space-separated stems).
MANIFESTS="${CORPUS_MANIFESTS:-lisbon-phase1 elif-rome istanbul-phase1 tokyo-phase1 brooklyn-phase1}"
# Governance runs on every manifest in the directory unless overridden.
GOVERNANCE_MANIFESTS="${GOVERNANCE_MANIFESTS:-}"

cd "$AGENT_DIR"
# shellcheck disable=SC1091
[ -f .venv/bin/activate ] && source .venv/bin/activate

fail=0

echo "== corpus-check: slug resolution =="
for stem in $MANIFESTS; do
  echo "-- $stem --"
  if PYTHONPATH=. python -m tools.dogfood.content.corpus_refs "$MANIFEST_DIR/$stem.yaml" | tail -1; then
    echo "  ✓ $stem: all refs resolve (missing=0)"
  else
    echo "  ✗ $stem: has missing refs — see audit above"
    fail=1
  fi
  echo ""
done

echo "== corpus-check: manifest governance =="
if [ -n "$GOVERNANCE_MANIFESTS" ]; then
  gov_stems="$GOVERNANCE_MANIFESTS"
else
  gov_stems=""
  for f in "$MANIFEST_DIR"/*.yaml; do
    gov_stems="$gov_stems $(basename "$f" .yaml)"
  done
fi
for stem in $gov_stems; do
  if PYTHONPATH=. python -m tools.dogfood.content.corpus_governance "$MANIFEST_DIR/$stem.yaml"; then
    :
  else
    fail=1
  fi
done

if [ "$fail" -ne 0 ]; then
  echo "corpus-check FAILED." >&2
  exit 1
fi
echo "corpus-check PASSED: slugs resolve and manifest governance is clean."
