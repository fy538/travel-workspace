#!/usr/bin/env bash
# Tier-4 certify-live — automatable preflight for the physical dogfood run.
#
# Automates: Fly health, S4 substrate audit on Fly, wedge doc pointers.
# The physical walk itself is a separate fail-closed command:
# `make dogfood-physical RUN_LIVE=1`.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"
FLY_HOST="${PRELAUNCH_HOST:-https://vesper-backend.fly.dev}"

bold() { printf "\033[1m%s\033[0m\n" "$1"; }
ok() { printf "  \033[32m✓\033[0m %s\n" "$1"; }
PREFLIGHT_BLOCKED=0
warn() {
  PREFLIGHT_BLOCKED=1
  printf "  \033[33m⚠\033[0m %s\n" "$1"
}
step() { printf "\n  %s\n" "$1"; }

bold "Certify-live preflight (automated)"

step "1/6 Fly backend reachable"
if curl -sf "$FLY_HOST/ready" >/dev/null; then
  ok "$FLY_HOST/ready"
else
  warn "$FLY_HOST/ready failed — is vesper-backend deployed?"
fi

step "2/7 Fly dogfood substrate (mara + dao + elif)"
if [[ -f "$AGENT_DIR/.env.prod" ]]; then
  if "$SCRIPT_DIR/attic/dogfood-fly-smoke.sh" 2>&1 | tee /tmp/certify-live-fly-smoke.txt; then
    ok "dogfood-fly-smoke passed"
  else
    warn "dogfood-fly-smoke failed — see output above (promote with: APPLY=1 make dogfood-promote CITY=lisbon)"
  fi
else
  warn "No .env.prod — skip Fly substrate smoke"
fi

step "3/8 Journey live API (J02/J04/J05/J10 two-persona)"
if "$SCRIPT_DIR/dogfood-journey-live-api.sh" 2>&1 | tee /tmp/certify-live-journey-api.txt; then
  ok "dogfood-journey-live-api passed"
else
  warn "dogfood-journey-live-api failed — fix API gates before device walk"
fi

step "4/8 J04 chat eval (S4 substrate + group-history egress)"
if "$SCRIPT_DIR/attic/dogfood-journey-j04-chat-eval.sh" 2>&1 | tee /tmp/certify-live-j04-chat-eval.txt; then
  ok "dogfood-journey-j04-chat-eval passed"
else
  warn "J04 chat eval failed — seed dao-quiet-mornings: APPLY=1 make dogfood-promote CITY=lisbon"
fi

step "5/8 S4 companion personas (dao + reza readiness)"
if [[ -f "$AGENT_DIR/.env.prod" ]]; then
  cd "$AGENT_DIR"
  # shellcheck disable=SC1091
  source .venv/bin/activate 2>/dev/null || true
  AGENT_DIR="$AGENT_DIR" source "$SCRIPT_DIR/dogfood-env.sh"
  if ! dogfood_apply_profile 2>/dev/null; then
    warn "dogfood profile could not be applied"
  fi
  for persona in dao@dogfood.local reza@dogfood.local; do
    if PYTHONPATH=. python scripts/dogfood_audit.py --summary --persona "$persona" --no-target-banner 2>&1 | tee "/tmp/certify-live-${persona//@/_}.txt" | grep -q "Persona readiness"; then
      line="$(grep -E "ready|partial|gap" "/tmp/certify-live-${persona//@/_}.txt" | head -1 || true)"
      if echo "$line" | grep -q "ready"; then
        ok "$persona — $line"
      else
        warn "$persona — $line (re-promote: APPLY=1 make dogfood-promote CITY=lisbon)"
      fi
    else
      warn "$persona audit failed"
    fi
  done
  cd "$WORKSPACE_DIR"
else
  warn "No .env.prod — skip Fly companion persona audit"
fi

step "6/8 Maestro wedge (DoD gate 4)"
if [[ "${CERTIFY_VISUAL_OK:-}" == "1" ]]; then
  ok "Maestro 24/25 reported green this session"
elif [[ "${CERTIFY_S4_MAESTRO_OK:-}" == "1" ]]; then
  ok "Maestro 26 (S4 real API) reported green this session"
else
  warn "Run: make certify-visual (mock 24/25) or make dogfood-maestro-s4-local (S4 real API 26)"
fi

step "7/8 Fly Maestro (optional — needs PRELAUNCH_JWT_MARA)"
if [[ -n "${PRELAUNCH_JWT_MARA:-}" ]]; then
  if RUN_MAESTRO=0 "$SCRIPT_DIR/attic/dogfood-maestro-fly.sh" 2>&1 | tee /tmp/certify-live-fly-maestro.txt; then
    ok "Fly J04 HTTP eval passed (set RUN_MAESTRO=1 make dogfood-maestro-fly for UI)"
  else
    warn "Fly Maestro HTTP eval failed — see /tmp/certify-live-fly-maestro.txt"
  fi
else
  warn "Set PRELAUNCH_JWT_MARA to run Fly HTTP eval (make dogfood-maestro-fly)"
fi

step "8/8 Physical device walk"
cat <<'EOF'

  Runbook: docs/working/journey-live-full-cert-04-05-10.md

  This preflight does not execute physical assertions. Run:
    make dogfood-physical RUN_LIVE=1

EOF

printf "  Physical assertions are not run by certify-live; no physical pass is claimed.\n"

if [[ "$PREFLIGHT_BLOCKED" != "0" ]]; then
  bold "Certify-live preflight BLOCKED — resolve warnings, then run dogfood-physical."
  exit 2
fi

bold "Certify-live preflight passed — run dogfood-physical for physical evidence."
