#!/usr/bin/env bash
# sync-types.sh — Regenerate the OpenAPI snapshot and the travel-app
# TypeScript types from it. Single source of truth: docs/openapi.json
# (this workspace repo). The travel-app npm scripts read the same file
# via ../docs/openapi.json, so there is exactly one snapshot every tool
# generates from.
#
# Usage:
#   ./scripts/sync-types.sh                 # regenerate snapshot OFFLINE
#                                           # (no running backend needed)
#   ./scripts/sync-types.sh --from-snapshot # use the committed snapshot as-is
#   ./scripts/sync-types.sh --live          # pull from a running backend
#
# Default (offline) generation runs travel-agent's deterministic exporter
# (scripts/export_openapi.py → app.openapi()) so the snapshot can be
# regenerated without standing up Postgres/Qdrant. Requires the Travel
# Agent Python deps to be importable (pip install -r requirements-dev.txt).
#
# Requirements:
#   - node/npm available (for openapi-typescript)
#   - Default/--live: travel-agent present as a sibling dir

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
BACKEND_URL="${BACKEND_URL:-http://localhost:8000}"
SNAPSHOT_PATH="$WORKSPACE_DIR/docs/openapi.json"
TRAVEL_AGENT_DIR="$WORKSPACE_DIR/travel-agent"
TRAVEL_APP_DIR="$WORKSPACE_DIR/travel-app"
OUTPUT_FILE="$TRAVEL_APP_DIR/utils/api/schema.gen.ts"

# ── Parse args ─────────────────────────────────────────────────────────────
MODE="offline"
for arg in "$@"; do
  case "$arg" in
    --from-snapshot) MODE="snapshot" ;;
    --live) MODE="live" ;;
    *) echo "Unknown argument: $arg" && exit 1 ;;
  esac
done

mkdir -p "$(dirname "$SNAPSHOT_PATH")"

# ── Step 1: Produce docs/openapi.json ───────────────────────────────────────
case "$MODE" in
  snapshot)
    echo "→ Using committed snapshot: $SNAPSHOT_PATH"
    if [ ! -f "$SNAPSHOT_PATH" ]; then
      echo "✗ Snapshot not found at $SNAPSHOT_PATH"
      echo "  Run without --from-snapshot to regenerate it."
      exit 1
    fi
    ;;
  live)
    echo "→ Fetching live schema from $BACKEND_URL/openapi.json ..."
    if curl --silent --fail --max-time 5 "$BACKEND_URL/openapi.json" -o "$SNAPSHOT_PATH.tmp"; then
      mv "$SNAPSHOT_PATH.tmp" "$SNAPSHOT_PATH"
      echo "  ✓ Saved to $SNAPSHOT_PATH"
    else
      echo "✗ Could not reach $BACKEND_URL/openapi.json"
      echo "  Is the backend running? Or use the default (offline) mode."
      exit 1
    fi
    ;;
  offline)
    echo "→ Generating schema offline via travel-agent export_openapi.py ..."
    if [ ! -d "$TRAVEL_AGENT_DIR" ]; then
      echo "✗ travel-agent not found at $TRAVEL_AGENT_DIR"
      echo "  Offline generation needs the backend source. Use --from-snapshot instead."
      exit 1
    fi
    (
      cd "$TRAVEL_AGENT_DIR"
      PYTHONPATH=. python scripts/export_openapi.py --out "$SNAPSHOT_PATH"
    )
    echo "  ✓ Wrote $SNAPSHOT_PATH"
    ;;
esac

# ── Step 2: Generate TypeScript types ──────────────────────────────────────
echo "→ Generating TypeScript types → $OUTPUT_FILE ..."
cd "$TRAVEL_APP_DIR"
npx openapi-typescript "$SNAPSHOT_PATH" --output "$OUTPUT_FILE"
echo "  ✓ Generated $OUTPUT_FILE"

# ── Step 3: Type-check ──────────────────────────────────────────────────────
echo "→ Running tsc --noEmit to check for type breakage ..."
if npx tsc --noEmit 2>&1; then
  echo "  ✓ No type errors"
else
  echo ""
  echo "  ⚠  Type errors found. These are likely places where travel-app"
  echo "     uses a field that changed in the backend."
  echo "  Fix them before committing."
  exit 1
fi

# ── Done ────────────────────────────────────────────────────────────────────
echo ""
echo "✓ Done. Next steps:"
echo "  1. Review the diff in utils/api/schema.gen.ts"
echo "  2. Commit docs/openapi.json alongside the travel-app changes"
echo "     (keeps the schema snapshot and generated types atomic)"
