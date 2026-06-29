#!/usr/bin/env bash
# Print active dogfood stack (Postgres + Qdrant pairing) and warn on mismatch.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"

PROFILE="${PROFILE:-local}"
APPLY="${APPLY:-0}"

# shellcheck source=scripts/dogfood-env.sh
source "$SCRIPT_DIR/dogfood-env.sh"
dogfood_apply_profile
dogfood_print_stack

cd "$AGENT_DIR"
# shellcheck disable=SC1091
[ -f .venv/bin/activate ] && source .venv/bin/activate

echo ""
echo "== Postgres connectivity =="
PYTHONPATH=. python - <<'PY'
from sqlalchemy import text
from backend.core.db.engine import get_connection

with get_connection() as conn:
    n = conn.execute(text("SELECT COUNT(*) FROM venues")).scalar()
    print(f"  venues={n}")
PY

echo ""
echo "== Qdrant connectivity =="
PYTHONPATH=. python - <<'PY'
from backend.core.vector.client import get_qdrant_client
from backend.core.vector.collections import VENUE_BRIEFS_COLLECTION, ensure_collections

ensure_collections()
client = get_qdrant_client()
info = client.get_collection(VENUE_BRIEFS_COLLECTION)
print(f"  collection={VENUE_BRIEFS_COLLECTION} points={info.points_count}")
PY

echo ""
echo "✓ dogfood-env-check profile=$PROFILE"
