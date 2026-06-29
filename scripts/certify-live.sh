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

step "1/5 Fly backend reachable"
if curl -sf "$FLY_HOST/ready" >/dev/null; then
  ok "$FLY_HOST/ready"
else
  warn "$FLY_HOST/ready failed — is vesper-backend deployed?"
fi

step "2/5 Fly dogfood substrate (mara + elif)"
if [[ -f "$AGENT_DIR/.env.prod" ]]; then
  if "$SCRIPT_DIR/dogfood-fly-smoke.sh" 2>&1 | tee /tmp/certify-live-fly-smoke.txt; then
    ok "dogfood-fly-smoke passed"
  else
    warn "dogfood-fly-smoke failed — see output above (promote with: APPLY=1 make dogfood-promote CITY=lisbon)"
  fi
else
  warn "No .env.prod — skip Fly substrate smoke"
fi

step "3/5 Maestro wedge (DoD gate 4)"
if [[ "${CERTIFY_VISUAL_OK:-}" == "1" ]]; then
  ok "Maestro 24/25 reported green this session"
else
  warn "Run: make certify-visual (needs simulator + Metro dev client)"
fi

step "4/5 Human live walk (DoD gates 5–8) — two Clerk accounts on EAS dogfood build"
cat <<'EOF'

  Prerequisites:
    • EAS dogfood build installed (USE_MOCK=false, API=https://vesper-backend.fly.dev)
    • Device A: organizer (your founder account)
    • Device B: invitee (second Clerk account — test user or second phone)
    • Lisbon + Rome promoted on Fly (APPLY=1 make dogfood-promote CITY=lisbon|rome)
    • Automated preflight: make dogfood-fly-smoke

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
