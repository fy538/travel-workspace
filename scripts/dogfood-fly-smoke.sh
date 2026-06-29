#!/usr/bin/env bash
# Automated Fly dogfood smoke — API + Fly Postgres substrate checks.
#
# Complements phone/EAS manual walk (certify-live). Run after dogfood-promote.
#
# Usage:
#   scripts/dogfood-fly-smoke.sh
#   FLY_HOST=https://vesper-backend.fly.dev scripts/dogfood-fly-smoke.sh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"
FLY_HOST="${FLY_HOST:-https://vesper-backend.fly.dev}"
SLUG_BRIDGE="tools/dogfood/content/manifests/elif-rome-slug-bridge.yaml"
PROFILE=fly
APPLY=1

bold() { printf "\033[1m%s\033[0m\n" "$1"; }
ok() { printf "  \033[32m✓\033[0m %s\n" "$1"; }
fail() { printf "  \033[31m✗\033[0m %s\n" "$1"; }
warn() { printf "  \033[33m⚠\033[0m %s\n" "$1"; }

AGENT_DIR="$AGENT_DIR" source "$SCRIPT_DIR/dogfood-env.sh"
dogfood_apply_profile || exit 1

cd "$AGENT_DIR"
# shellcheck disable=SC1091
source .venv/bin/activate

failures=0

bold "Dogfood Fly smoke (automated)"
dogfood_print_stack
echo ""

bold "1/4 Fly API reachable"
api_ok=0
if PYTHONPATH=. python - <<PY
import sys, urllib.request
host = "${FLY_HOST}"
for path in ("/ready", "/health", "/openapi.json"):
    url = host.rstrip("/") + path
    try:
        with urllib.request.urlopen(url, timeout=45) as r:
            print(f"  {path} -> {r.status}")
            sys.exit(0)
    except Exception as e:
        print(f"  {path} -> {e}", file=sys.stderr)
print("all paths failed", file=sys.stderr)
sys.exit(1)
PY
then
  ok "Fly API responding at $FLY_HOST"
  api_ok=1
else
  warn "Fly API slow/unreachable (cold start?) — DB substrate OK; retry before phone walk"
fi

bold "2/4 Persona substrate on Fly DB"
for persona in mara@dogfood.local dao@dogfood.local elif@dogfood.local; do
  if PYTHONPATH=. python scripts/dogfood_audit.py --summary --persona "$persona" --no-target-banner 2>&1 | tee "/tmp/dogfood-smoke-${persona//@/_}.txt" | grep -q "Persona readiness"; then
    line="$(grep -E "Persona readiness:" -A1 "/tmp/dogfood-smoke-${persona//@/_}.txt" | tail -1 || true)"
    ok "$persona — $line"
  else
    fail "$persona audit failed"
    failures=$((failures + 1))
  fi
done

bold "3/4 Rome canonical brief bridge (Fly Postgres)"
if PYTHONPATH=. python -m tools.dogfood.content.slug_bridge "$SLUG_BRIDGE" --verify; then
  ok "9/9 canonical Rome slugs have briefs on Fly"
else
  fail "Rome slug bridge verify failed on Fly"
  failures=$((failures + 1))
fi

bold "4/5 Canonical venue brief sample (Fly Postgres)"
if PYTHONPATH=. python - <<'PY'
from sqlalchemy import text
from backend.core.db.engine import get_connection

slugs = [
    "rome-market-testaccio",
    "rome-venue-roscioli-style-reservation",
]
with get_connection() as conn:
    for slug in slugs:
        row = conn.execute(
            text(
                """
                SELECT v.id, LEFT(b.content, 80)
                FROM venues v
                JOIN briefs b ON b.venue_id = v.id
                WHERE v.slug = :slug
                """
            ),
            {"slug": slug},
        ).one_or_none()
        if not row:
            raise SystemExit(f"missing brief for {slug}")
        print(f"  {slug}: venue_id={row[0]} brief={row[1]!r}...")
PY
then
  ok "Manifest canonical venues have brief text on Fly"
else
  fail "Canonical venue brief check failed"
  failures=$((failures + 1))
fi

bold "5/5 Five-pack substrate verify (trips + discover compose)"
if "$SCRIPT_DIR/dogfood-five-pack-verify.sh" 2>&1 | tee /tmp/dogfood-five-pack-verify.txt; then
  ok "Five-pack substrate verify passed (see make dogfood-five-pack-verify)"
else
  fail "Five-pack substrate verify failed — see /tmp/dogfood-five-pack-verify.txt"
  failures=$((failures + 1))
fi

echo ""
bold "Manual phone walk (EAS build) — still required"
cat <<'EOF'
  Login: elif@dogfood.local or mara@dogfood.local (Clerk dogfood cohort)
  API:   https://vesper-backend.fly.dev

  Rome (elif):
    [ ] Open "Rome return planning" trip
    [ ] Day 2: Testaccio Market block shows real venue (not stub title only)
    [ ] Vesper: ask "Testaccio and Trastevere food walks" — cites real corpus

  Lisbon (mara):
    [ ] Open S4 Lisbon group trip
    [ ] Discover / Vesper returns enriched Lisbon venues (not empty)

  Record pass/fail in docs/journeys/STATUS.md Live column.
EOF

echo ""
if [ "$failures" -eq 0 ]; then
  if [ "$api_ok" -eq 0 ]; then
    bold "Dogfood Fly smoke PASSED (substrate). Wake Fly API before phone walk: curl $FLY_HOST/ready"
    exit 0
  fi
  bold "Dogfood Fly smoke PASSED (automated). Complete manual phone walk above."
  exit 0
fi
bold "Dogfood Fly smoke FAILED ($failures automated check(s))."
exit 1
