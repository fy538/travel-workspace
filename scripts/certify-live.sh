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

step "1/6 Fly backend reachable"
if curl -sf "$FLY_HOST/ready" >/dev/null; then
  ok "$FLY_HOST/ready"
else
  warn "$FLY_HOST/ready failed — is vesper-backend deployed?"
fi

step "2/6 Fly dogfood substrate (mara + elif)"
if [[ -f "$AGENT_DIR/.env.prod" ]]; then
  if "$SCRIPT_DIR/dogfood-fly-smoke.sh" 2>&1 | tee /tmp/certify-live-fly-smoke.txt; then
    ok "dogfood-fly-smoke passed"
  else
    warn "dogfood-fly-smoke failed — see output above (promote with: APPLY=1 make dogfood-promote CITY=lisbon)"
  fi
else
  warn "No .env.prod — skip Fly substrate smoke"
fi

step "3/6 Journey live API (J02/J04/J05/J10 two-persona)"
if "$SCRIPT_DIR/dogfood-journey-live-api.sh" 2>&1 | tee /tmp/certify-live-journey-api.txt; then
  ok "dogfood-journey-live-api passed"
else
  warn "dogfood-journey-live-api failed — fix API gates before device walk"
fi

step "4/6 Maestro wedge (DoD gate 4)"
if [[ "${CERTIFY_VISUAL_OK:-}" == "1" ]]; then
  ok "Maestro 24/25 reported green this session"
else
  warn "Run: make certify-visual (needs simulator + Metro dev client)"
fi

step "5/6 Device live walk — J04/J05/J10 (two Clerk accounts on EAS)"
cat <<'EOF'

  Runbook: docs/working/journey-live-full-cert-04-05-10.md

  Prerequisites:
    • make dogfood-journey-live-api green (15/15 TestClient)
    • make certify-visual green (Maestro 24/25)
    • EAS dogfood build; mara@dogfood.local + dao@dogfood.local
    • S4 Lisbon promoted on Fly

  J05 — Propose + mutate (two devices)
    [ ] Ask Vesper (group) for a plan change → proposal appears
    [ ] I5 Accept → receipt visible; plan block updates
    [ ] I5 Reject alternate → original remains; receipt confirms
    [ ] I6 Revert accepted change → Plan + Home reflect revert (no ghost blocks)
    [ ] I7 Stale edit → 409 surfaced in UI (optional stress test)
    [ ] I8 Double-apply / retry → no duplicate mutation

  J06 — Coherence (I9)
    [ ] After mutation: Home, Plan, Changes, Map agree on block ids / titles

  Privacy (I4 — critical, J04)
    [ ] DM private constraint on Device B → group thread never shows raw text

  J10 — Stay / expense trust (two devices)
    [ ] Organizer stay + expense opt-in; member sees public-safe state only

  Dark sweep (DoD 7)
    [ ] No booking checkout, voice mic, or postcard surfaces leak into slice

  Record pass/fail in docs/journeys/STATUS.md Live column when done.

EOF

bold "Certify-live preflight complete."
