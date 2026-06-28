#!/usr/bin/env bash
# Tier-4 certify-live — automatable preflight + human live-walk checklist.
#
# Automates: Fly health, S4 substrate audit on Fly, wedge doc pointers.
# Human-only: two Clerk accounts, two devices, I1–I10 on EAS dogfood build.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"
FLY_HOST="${PRELAUNCH_HOST:-https://vesper-backend.fly.dev}"

bold() { printf "\033[1m%s\033[0m\n" "$1"; }
ok() { printf "  \033[32m✓\033[0m %s\n" "$1"; }
warn() { printf "  \033[33m⚠\033[0m %s\n" "$1"; }
step() { printf "\n  %s\n" "$1"; }

bold "Certify-live preflight (automated)"

step "1/4 Fly backend reachable"
if curl -sf "$FLY_HOST/ready" >/dev/null; then
  ok "$FLY_HOST/ready"
else
  warn "$FLY_HOST/ready failed — is vesper-backend deployed?"
fi

step "2/4 S4 substrate on Fly (mara@dogfood.local)"
if [[ -f "$AGENT_DIR/.env.prod" ]]; then
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
  if [[ -n "$PROD_DATABASE_URL" ]]; then
    export DATABASE_URL="$PROD_DATABASE_URL"
    export ENVIRONMENT=production
    if PYTHONPATH=. python scripts/dogfood_audit.py \
      --summary --persona mara@dogfood.local --no-target-banner 2>&1 | tee /tmp/certify-live-audit.txt | grep -q "Persona readiness"; then
      ok "dogfood audit ran against Fly DB"
      grep -E "mara@|trips=|proposals=" /tmp/certify-live-audit.txt 2>/dev/null || true
    else
      warn "S4 not seeded on Fly yet — run: SEED_S4_FLY_APPLY=1 make seed-s4-fly"
    fi
  else
    warn "PROD_DATABASE_URL missing in .env.prod — skip Fly audit"
  fi
else
  warn "No .env.prod — skip Fly substrate audit"
fi

step "3/4 Maestro wedge (DoD gate 4)"
if [[ "${CERTIFY_VISUAL_OK:-}" == "1" ]]; then
  ok "Maestro 24/25 reported green this session"
else
  warn "Run: make certify-visual (needs simulator + Metro dev client)"
fi

step "4/4 Human live walk (DoD gates 5–8) — two Clerk accounts on EAS dogfood build"
cat <<'EOF'

  Prerequisites:
    • EAS dogfood build installed (USE_MOCK=false, API=https://vesper-backend.fly.dev)
    • Device A: organizer (your founder account)
    • Device B: invitee (second Clerk account — test user or second phone)
    • S4 seeded on Fly (make seed-s4-fly with SEED_S4_FLY_APPLY=1) OR create fresh trip live

  Walk J02 → J05 (docs/working/wedge-journey-02-05-path-to-dogfood.md):

  J02 — Create + invite
    [ ] I1 Organizer creates trip → single workspace
    [ ] I1 Mint invite → token maps to exactly one trip
    [ ] I2 Invitee signs in mid-flow → token survives auth detour
    [ ] I1/I3 Accept → invitee lands in organizer's trip; non-member saw nothing pre-accept

  J05 — Propose + mutate
    [ ] Ask Vesper (group) for a plan change → proposal appears
    [ ] I5 Accept → receipt visible; plan block updates
    [ ] I5 Reject alternate → original remains; receipt confirms
    [ ] I6 Revert accepted change → Plan + Home reflect revert (no ghost blocks)
    [ ] I7 Stale edit → 409 surfaced in UI (optional stress test)
    [ ] I8 Double-apply / retry → no duplicate mutation

  J06 — Coherence (I9)
    [ ] After mutation: Home, Plan, Changes, Map agree on block ids / titles

  Privacy (I4 — critical)
    [ ] DM a private constraint → group thread never shows raw private text

  Dark sweep (DoD 7)
    [ ] No booking checkout, voice mic, or postcard surfaces leak into slice

  Record pass/fail in docs/journeys/STATUS.md Live column when done.

EOF

bold "Certify-live preflight complete."
