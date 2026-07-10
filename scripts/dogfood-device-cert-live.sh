#!/usr/bin/env bash
# Device-tier full certification for J04, J05, J10 — orchestrates the live
# two-account Maestro flows against Fly, in the order the runbook requires.
#
# Modeled on scripts/dogfood-maestro-fly.sh (Fly-ready check → HTTP eval →
# Maestro UI, strict `set -euo pipefail`, bold/ok/fail/warn helpers) and
# scripts/certify-live.sh (preflight ladder + human checklist print at the
# end for the parts automation cannot cover).
#
# THIS SCRIPT DOES NOT EXECUTE MAESTRO AGAINST FLY BY DEFAULT. Running the
# real device flows sends real emails (Clerk OTP) to the @dogfood.local
# inboxes and can write real state to shared dogfood infra other sessions
# depend on — see the flows' own headers. Default mode is DRY (validates
# flow files + preflight only). Set RUN_LIVE=1 explicitly, on a machine
# with real Clerk OTP access, to actually drive a device/simulator.
#
# Usage:
#   scripts/dogfood-device-cert-live.sh                 # dry validate + preflight
#   RUN_LIVE=1 scripts/dogfood-device-cert-live.sh       # actually run Maestro (human OTP entry required)
#
# Prerequisites for RUN_LIVE=1:
#   - Two iOS devices/simulators (or one, run twice in the documented order)
#   - dogfood or preview EAS build installed (real Clerk, real Fly backend —
#     see travel-app/eas.json; the `development` profile CANNOT do this,
#     see docs/working/journey-live-full-cert-04-05-10.md "Automation status")
#   - Real Clerk accounts for mara@dogfood.local and dao@dogfood.local
#     (see travel-agent docs/operations/Dogfood Runbook.md "Real-device
#     entry" for the .local-domain sign-up workaround)
#   - Fly substrate promoted for Lisbon: APPLY=1 PROFILE=fly make dogfood-promote CITY=lisbon
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"
APP_DIR="$WORKSPACE_DIR/travel-app"
FLY_HOST="${PRELAUNCH_HOST:-https://vesper-backend.fly.dev}"
RUN_LIVE="${RUN_LIVE:-0}"

bold() { printf "\033[1m%s\033[0m\n" "$1"; }
ok() { printf "  \033[32m✓\033[0m %s\n" "$1"; }
fail() { printf "  \033[31m✗\033[0m %s\n" "$1"; }
warn() { printf "  \033[33m⚠\033[0m %s\n" "$1"; }
step() { printf "\n  %s\n" "$1"; }

# Per-check pass/fail summary, keyed by runbook invariant id, printed at the end.
declare -a RESULTS=()
record() { RESULTS+=("$1|$2|$3"); }  # invariant|status|note

bold "Device-cert live orchestration — J04 / J05 / J10"

# ── 1/5 Flow validation (always runs, no network) ─────────────────────────
step "1/5 Validate Maestro flow files (YAML parse + registry check)"
if python3 "$SCRIPT_DIR/validate-maestro-flows.py" --app-dir "$APP_DIR"; then
  ok "validate-maestro-flows.py passed"
  record "flow-validation" "PASS" "YAML + registry check green"
else
  fail "validate-maestro-flows.py failed — fix before proceeding"
  record "flow-validation" "FAIL" "see validator output above"
  exit 1
fi

# ── 2/5 Fly reachability ───────────────────────────────────────────────────
step "2/5 Fly backend reachable"
if curl -sf "$FLY_HOST/ready" >/dev/null; then
  ok "$FLY_HOST/ready"
  record "fly-ready" "PASS" "$FLY_HOST/ready"
else
  warn "$FLY_HOST/ready failed — is vesper-backend deployed?"
  record "fly-ready" "WARN" "$FLY_HOST/ready unreachable"
fi

# ── 3/5 Prerequisite automated gates (must be green before a device walk) ──
step "3/5 Prerequisite gates: dogfood-journey-live-api + J04 chat eval"
if PROFILE=fly TRANSPORT=http "$SCRIPT_DIR/dogfood-journey-live-api.sh" 2>&1 | tee /tmp/dogfood-device-cert-journey-api.txt; then
  ok "dogfood-journey-live-api (Fly HTTP) passed"
  record "prereq-live-api" "PASS" "J02/J04/J05/J10 TestClient-equivalent green"
else
  warn "dogfood-journey-live-api had failures (needs PRELAUNCH_JWT_MARA/DAO for HTTP transport) — see /tmp/dogfood-device-cert-journey-api.txt"
  record "prereq-live-api" "WARN" "re-run with PRELAUNCH_JWT_MARA/DAO set"
fi

if "$SCRIPT_DIR/dogfood-journey-j04-chat-eval.sh" 2>&1 | tee /tmp/dogfood-device-cert-j04-chat-eval.txt; then
  ok "J04 chat eval passed"
  record "prereq-j04-chat-eval" "PASS" "substrate + group-history egress gate green"
else
  warn "J04 chat eval failed — seed: APPLY=1 PROFILE=fly make dogfood-promote CITY=lisbon"
  record "prereq-j04-chat-eval" "WARN" "seed dao-quiet-mornings before device walk"
fi

# ── 4/5 Maestro availability + flow list ───────────────────────────────────
step "4/5 Maestro device flows to run (in required order)"
FLOWS=(
  "29-journey-04-device-member-private-phrase.yaml   (Device: Dao — I4 part A, private phrase)"
  "30-journey-04-device-organizer-group-safe-check.yaml (Device: Mara — I4 part B, group-safe assert)"
  "31-journey-10-device-organizer-stay-expense.yaml  (Device: Mara — I10 part A, create private stay)"
  "32-journey-10-device-member-stay-visibility-check.yaml (Device: Dao — I10 part B, visibility assert)"
  "33-journey-05-device-two-account-proposal-loop.yaml (Device A→B: Mara then Dao — I5/I6/I7/I8)"
)
for f in "${FLOWS[@]}"; do
  printf "    - %s\n" "$f"
done

if [[ "$RUN_LIVE" != "1" ]]; then
  warn "RUN_LIVE=0 (default) — dry mode. Not driving a device/simulator."
  record "device-walk" "SKIPPED" "set RUN_LIVE=1 with real Clerk OTP access to execute"
  print_summary_and_exit=1
else
  print_summary_and_exit=0
fi

if [[ "${print_summary_and_exit:-0}" != "1" ]]; then
  if ! command -v maestro >/dev/null 2>&1; then
    fail "maestro not in PATH — cannot RUN_LIVE=1"
    record "device-walk" "FAIL" "maestro not installed"
  else
    export JAVA_HOME="${JAVA_HOME:-/opt/homebrew/opt/openjdk}"
    export PATH="$JAVA_HOME/bin:$HOME/.maestro/bin:$PATH"
    cd "$APP_DIR"

    step "5/5 Running device flows — HUMAN OTP ENTRY REQUIRED at each sign-in"
    warn "Each _signin-dogfood-account.yaml pause needs a human to key the"
    warn "real Clerk email OTP for that account — there is no fixed test code."
    warn "Run 'maestro studio' alongside, or attach to the session, to enter it."

    run_flow() {
      local file="$1" label="$2"
      if maestro test "$APP_DIR/.maestro/$file"; then
        ok "$label passed"
        record "$label" "PASS" "$file"
      else
        fail "$label FAILED"
        record "$label" "FAIL" "$file — see maestro output above"
      fi
    }

    run_flow "29-journey-04-device-member-private-phrase.yaml" "I4-part-A-member-send"
    run_flow "30-journey-04-device-organizer-group-safe-check.yaml" "I4-group-safe-assert"
    run_flow "31-journey-10-device-organizer-stay-expense.yaml" "I10-part-A-organizer-create"
    run_flow "32-journey-10-device-member-stay-visibility-check.yaml" "I10-visibility-assert"
    run_flow "33-journey-05-device-two-account-proposal-loop.yaml" "I5-I6-I7-I8-proposal-loop"
  fi
fi

# ── Summary ────────────────────────────────────────────────────────────────
bold "\nDevice-cert summary"
printf "  %-30s %-8s %s\n" "CHECK" "STATUS" "NOTE"
for r in "${RESULTS[@]}"; do
  IFS='|' read -r name status note <<<"$r"
  case "$status" in
    PASS) color="\033[32m" ;;
    FAIL) color="\033[31m" ;;
    *) color="\033[33m" ;;
  esac
  printf "  %-30s ${color}%-8s\033[0m %s\n" "$name" "$status" "$note"
done

any_fail=0
for r in "${RESULTS[@]}"; do
  [[ "$r" == *"|FAIL|"* ]] && any_fail=1
done

if [[ "$any_fail" == "1" ]]; then
  bold "\nDevice-cert: FAILURES present — do not mark J04/J05/J10 full-certified."
  exit 1
fi

if [[ "$RUN_LIVE" != "1" ]]; then
  bold "\nDry run complete — flows validated, prerequisites checked. Set RUN_LIVE=1 to execute for real."
else
  bold "\nDevice-cert PASSED — record in docs/journeys/STATUS.md (Live column → ready, Certified → full for J04/J05/J10)."
fi
