#!/usr/bin/env bash
# sync-types.sh — Pull the OpenAPI schema from Travel Agent and regenerate
# TypeScript types in Travel App.
#
# Usage:
#   ./scripts/sync-types.sh              # fetch live schema from running backend
#   ./scripts/sync-types.sh --from-snapshot  # use committed docs/openapi.json
#
# Requirements:
#   - node/npm available (for openapi-typescript)
#   - Backend running at localhost:8000 (unless --from-snapshot)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
BACKEND_URL="${BACKEND_URL:-http://localhost:8000}"
SNAPSHOT_PATH="$WORKSPACE_DIR/docs/openapi.json"
TRAVEL_APP_DIR="$WORKSPACE_DIR/Travel App"
OUTPUT_FILE="$TRAVEL_APP_DIR/utils/api/schema.gen.ts"

# ── Parse args ─────────────────────────────────────────────────────────────
FROM_SNAPSHOT=false
for arg in "$@"; do
  case "$arg" in
    --from-snapshot) FROM_SNAPSHOT=true ;;
    *) echo "Unknown argument: $arg" && exit 1 ;;
  esac
done

# ── Step 1: Get the schema ──────────────────────────────────────────────────
if [ "$FROM_SNAPSHOT" = true ]; then
  echo "→ Using committed snapshot: $SNAPSHOT_PATH"
  if [ ! -f "$SNAPSHOT_PATH" ]; then
    echo "✗ Snapshot not found at $SNAPSHOT_PATH"
    echo "  Run without --from-snapshot to fetch a fresh copy."
    exit 1
  fi
  SCHEMA_SOURCE="$SNAPSHOT_PATH"
else
  echo "→ Fetching live schema from $BACKEND_URL/openapi.json ..."
  mkdir -p "$(dirname "$SNAPSHOT_PATH")"
  if curl --silent --fail --max-time 5 "$BACKEND_URL/openapi.json" -o "$SNAPSHOT_PATH.tmp"; then
    mv "$SNAPSHOT_PATH.tmp" "$SNAPSHOT_PATH"
    echo "  ✓ Saved to $SNAPSHOT_PATH"
  else
    echo "✗ Could not reach $BACKEND_URL/openapi.json"
    echo "  Is the backend running? Try: cd 'Travel Agent' && PYTHONPATH=. uvicorn backend.api.main:app --reload"
    echo "  Or use --from-snapshot to regenerate from the last committed schema."
    exit 1
  fi
  SCHEMA_SOURCE="$SNAPSHOT_PATH"
fi

# ── Step 2: Generate TypeScript types ──────────────────────────────────────
echo "→ Generating TypeScript types → $OUTPUT_FILE ..."
cd "$TRAVEL_APP_DIR"
npx openapi-typescript "$SCHEMA_SOURCE" --output "$OUTPUT_FILE"
echo "  ✓ Generated $OUTPUT_FILE"

# ── Step 3: Type-check ──────────────────────────────────────────────────────
echo "→ Running tsc --noEmit to check for type breakage ..."
if npx tsc --noEmit 2>&1; then
  echo "  ✓ No type errors"
else
  echo ""
  echo "  ⚠  Type errors found. These are likely places where Travel App"
  echo "     uses a field that changed in the backend."
  echo "  Fix them before committing."
  exit 1
fi

# ── Done ────────────────────────────────────────────────────────────────────
echo ""
echo "✓ Done. Next steps:"
echo "  1. Review the diff in utils/api/schema.gen.ts"
echo "  2. Commit docs/openapi.json alongside any Travel App changes"
echo "     (keeps the schema snapshot and code changes atomic)"
