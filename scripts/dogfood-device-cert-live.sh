#!/usr/bin/env bash
# Fail-closed physical device certification for the active dogfood wedge.
#
# This runner validates the live prerequisites and then executes the five
# Maestro flows required by the J04/J05/J10 runbook. A dry run is deliberately
# a blocked result: it never claims physical evidence. A physical pass/fail
# receipt is written only when the runner resolves two physical UDIDs and
# hashes artifacts created during this exact run.
#
# Usage:
#   RUN_LIVE=0 scripts/dogfood-device-cert-live.sh   # validate, exit 2 (blocked)
#   RUN_LIVE=1 scripts/dogfood-device-cert-live.sh   # execute physical walk
#
# Required metadata for RUN_LIVE=1 (comma-separated where noted):
#   PHYSICAL_APP_BUILD_ID
#   PHYSICAL_BACKEND_DEPLOY_DIGEST
#   PHYSICAL_MIGRATION_REVISION
#   PHYSICAL_SEED_CORPUS_HASH=sha256:<64 hex>
#   PHYSICAL_DEVICE_UDIDS="hardware-udid-1,hardware-udid-2"
#   PHYSICAL_IDENTITIES="mara@dogfood.local,dao@dogfood.local"
#   PHYSICAL_REVIEWER
#   PHYSICAL_ARTIFACT_PATHS="/path/flow.zip,/path/screenshot.png"
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
APP_DIR="$WORKSPACE_DIR/travel-app"
FLY_HOST="${PRELAUNCH_HOST:-https://vesper-backend.fly.dev}"
RUN_LIVE="${RUN_LIVE:-0}"
CERT_STARTED_EPOCH="$(date +%s)"
EVIDENCE_HELPER="$SCRIPT_DIR/physical_evidence.py"
ORACLE_PATH="$WORKSPACE_DIR/docs/working/journey-live-full-cert-04-05-10.md"

bold() { printf "\033[1m%s\033[0m\n" "$1"; }
ok() { printf "  \033[32m✓\033[0m %s\n" "$1"; }
fail() { printf "  \033[31m✗\033[0m %s\n" "$1"; }
warn() { printf "  \033[33m⚠\033[0m %s\n" "$1"; }
step() { printf "\n  %s\n" "$1"; }

declare -a RESULTS=()
declare -a PHYSICAL_DEVICE_UDID_LIST=()
declare -a PHYSICAL_DEVICE_DESCRIPTORS=()
record_check() { RESULTS+=("$1|$2|$3"); }

split_csv() {
  local raw="$1" item
  CSV_ITEMS=()
  [[ -n "$raw" ]] || return 0
  IFS=',' read -r -a CSV_ITEMS <<<"$raw"
  for item in "${CSV_ITEMS[@]}"; do
    [[ -n "$item" ]] || return 1
  done
}

resolve_physical_devices() {
  local raw_udids="${PHYSICAL_DEVICE_UDIDS:-}" output value existing
  local seen_udids=()
  if ! split_csv "$raw_udids" || [[ "${#CSV_ITEMS[@]}" -lt 2 ]]; then
    printf 'PHYSICAL_DEVICE_UDIDS must name at least two unique connected hardware UDIDs.\n' >&2
    return 1
  fi
  PHYSICAL_DEVICE_UDID_LIST=("${CSV_ITEMS[@]}")
  for value in "${PHYSICAL_DEVICE_UDID_LIST[@]}"; do
    for existing in "${seen_udids[@]}"; do
      [[ "$existing" != "$value" ]] || {
        printf 'Duplicate physical UDID: %s\n' "$value" >&2
        return 1
      }
    done
    seen_udids+=("$value")
  done
  local device_args=()
  for value in "${PHYSICAL_DEVICE_UDID_LIST[@]}"; do device_args+=(--udid "$value"); done
  if ! output="$(python3 "$EVIDENCE_HELPER" devices "${device_args[@]}")"; then
    return 1
  fi
  PHYSICAL_DEVICE_DESCRIPTORS=()
  while IFS= read -r value; do
    [[ -n "$value" ]] && PHYSICAL_DEVICE_DESCRIPTORS+=("$value")
  done <<<"$output"
  [[ "${#PHYSICAL_DEVICE_DESCRIPTORS[@]}" -eq "${#PHYSICAL_DEVICE_UDID_LIST[@]}" ]]
}

physical_metadata_args() {
  PHYSICAL_METADATA_ARGS=()
  local missing=()
  [[ -n "${PHYSICAL_APP_BUILD_ID:-}" ]] || missing+=(app_build_id)
  [[ -n "${PHYSICAL_BACKEND_DEPLOY_DIGEST:-}" ]] || missing+=(backend_deploy_digest)
  [[ -n "${PHYSICAL_MIGRATION_REVISION:-}" ]] || missing+=(migration_revision)
  [[ -n "${PHYSICAL_SEED_CORPUS_HASH:-}" ]] || missing+=(seed_corpus_hash)
  [[ -n "${PHYSICAL_REVIEWER:-}" ]] || missing+=(reviewer)
  local identities=() artifact_paths=() artifacts=() value output
  if [[ "${#PHYSICAL_DEVICE_DESCRIPTORS[@]}" -lt 2 ]]; then missing+=(devices); fi
  if ! split_csv "${PHYSICAL_IDENTITIES:-}"; then missing+=(identities); fi
  identities=("${CSV_ITEMS[@]}")
  if ! split_csv "${PHYSICAL_ARTIFACT_PATHS:-}"; then missing+=(artifacts); fi
  artifact_paths=("${CSV_ITEMS[@]}")
  [[ "${#identities[@]}" -ge 2 ]] || missing+=(identities)
  [[ "${#artifact_paths[@]}" -gt 0 ]] || missing+=(artifacts)
  if [[ "${#missing[@]}" -gt 0 ]]; then
    printf 'Missing physical receipt metadata: %s\n' "${missing[*]}" >&2
    return 1
  fi

  PHYSICAL_METADATA_ARGS+=(--app-build-id "${PHYSICAL_APP_BUILD_ID}")
  PHYSICAL_METADATA_ARGS+=(--backend-deploy-digest "${PHYSICAL_BACKEND_DEPLOY_DIGEST}")
  PHYSICAL_METADATA_ARGS+=(--migration-revision "${PHYSICAL_MIGRATION_REVISION}")
  PHYSICAL_METADATA_ARGS+=(--seed-corpus-hash "${PHYSICAL_SEED_CORPUS_HASH}")
  PHYSICAL_METADATA_ARGS+=(--oracle-hash "$(python3 "$EVIDENCE_HELPER" digest --path "$ORACLE_PATH")")
  local flow_args=()
  for value in "${FLOWS[@]}"; do flow_args+=(--path "$APP_DIR/.maestro/$value"); done
  PHYSICAL_METADATA_ARGS+=(--flow-hash "$(python3 "$EVIDENCE_HELPER" bundle "${flow_args[@]}")")
  PHYSICAL_METADATA_ARGS+=(--reviewer "${PHYSICAL_REVIEWER}")
  for value in "${PHYSICAL_DEVICE_DESCRIPTORS[@]}"; do
    PHYSICAL_METADATA_ARGS+=(--device "$value")
  done
  for value in "${identities[@]}"; do PHYSICAL_METADATA_ARGS+=(--identity "$value"); done
  local artifact_args=()
  for value in "${artifact_paths[@]}"; do artifact_args+=(--path "$value"); done
  if ! output="$(python3 "$EVIDENCE_HELPER" artifacts --not-before "$CERT_STARTED_EPOCH" "${artifact_args[@]}")"; then
    return 1
  fi
  while IFS= read -r value; do [[ -n "$value" ]] && artifacts+=("$value"); done <<<"$output"
  for value in "${artifacts[@]}"; do PHYSICAL_METADATA_ARGS+=(--artifact "$value"); done
}

record_physical_receipt() {
  local status="$1" reason="$2"
  local command="RUN_LIVE=${RUN_LIVE} scripts/dogfood-device-cert-live.sh"
  local args=(
    record --layer physical --status "$status" --environment founder-physical
    --command "$command" --journey J04 --journey J05 --journey J10
  )
  if [[ "$status" == "blocked" ]]; then
    args+=(--reason "$reason")
  else
    if ! physical_metadata_args; then
      printf 'Cannot write physical %s receipt without complete metadata.\n' "$status" >&2
      return 1
    fi
    args+=("${PHYSICAL_METADATA_ARGS[@]}")
  fi
  python3 "$SCRIPT_DIR/journey_evidence.py" "${args[@]}" >/dev/null
}

bold "Physical device certification — J04 / J05 / J10"

step "1/5 Validate Maestro flow files (YAML parse + registry check)"
if python3 "$SCRIPT_DIR/validate-maestro-flows.py" --app-dir "$APP_DIR"; then
  ok "validate-maestro-flows.py passed"
  record_check flow-validation PASS "YAML + registry check green"
else
  fail "validate-maestro-flows.py failed — fix before proceeding"
  record_check flow-validation FAIL "see validator output above"
fi

step "2/5 Fly backend reachable"
if curl -sf "$FLY_HOST/ready" >/dev/null; then
  ok "$FLY_HOST/ready"
  record_check fly-ready PASS "$FLY_HOST/ready"
else
  warn "$FLY_HOST/ready failed — physical run is blocked"
  record_check fly-ready BLOCKED "$FLY_HOST/ready unreachable"
fi

step "3/5 Automated prerequisites: live API + J04 chat eval"
if PROFILE=fly TRANSPORT=http "$SCRIPT_DIR/dogfood-journey-live-api.sh" 2>&1 | tee /tmp/dogfood-device-cert-journey-api.txt; then
  ok "dogfood-journey-live-api passed"
  record_check prereq-live-api PASS "J02/J04/J05/J10 API checks green"
else
  warn "dogfood-journey-live-api failed — physical run is blocked"
  record_check prereq-live-api BLOCKED "see /tmp/dogfood-device-cert-journey-api.txt"
fi

if "$SCRIPT_DIR/attic/dogfood-journey-j04-chat-eval.sh" 2>&1 | tee /tmp/dogfood-device-cert-j04-chat-eval.txt; then
  ok "J04 chat eval passed"
  record_check prereq-j04-chat-eval PASS "substrate + group-history egress gate green"
else
  warn "J04 chat eval failed — physical run is blocked"
  record_check prereq-j04-chat-eval BLOCKED "see /tmp/dogfood-device-cert-j04-chat-eval.txt"
fi

step "4/5 Device and assertion prerequisites"
FLOWS=(
  "29-journey-04-device-member-private-phrase.yaml"
  "30-journey-04-device-organizer-group-safe-check.yaml"
  "31-journey-10-device-organizer-stay-expense.yaml"
  "32-journey-10-device-member-stay-visibility-check.yaml"
  "33-journey-05-device-two-account-proposal-loop.yaml"
)
for flow in "${FLOWS[@]}"; do printf "    - %s\n" "$flow"; done

if [[ "$RUN_LIVE" == "1" ]]; then
  if resolve_physical_devices; then
    ok "Resolved ${#PHYSICAL_DEVICE_DESCRIPTORS[@]} physical devices by UDID"
    record_check device-binding PASS "hardware inventory resolved"
  else
    warn "physical hardware identity could not be verified"
    record_check device-binding BLOCKED "UDID missing, duplicate, disconnected, or virtual"
  fi
fi

prereq_failed=0
for result in "${RESULTS[@]}"; do
  [[ "$result" == *"|FAIL|"* || "$result" == *"|BLOCKED|"* ]] && prereq_failed=1
done

if [[ "$RUN_LIVE" != "1" ]]; then
  warn "RUN_LIVE=0 — no physical device assertions were executed"
  record_check device-walk BLOCKED "set RUN_LIVE=1 to execute"
elif [[ "$prereq_failed" == "1" ]]; then
  warn "required physical prerequisites are not green — device assertions were not executed"
  record_check device-walk BLOCKED "resolve prerequisite failures first"
elif ! command -v maestro >/dev/null 2>&1; then
  warn "maestro is not in PATH — physical run is blocked"
  record_check device-walk BLOCKED "maestro not installed"
else
  export JAVA_HOME="${JAVA_HOME:-/opt/homebrew/opt/openjdk}"
  export PATH="$JAVA_HOME/bin:${HOME:-}/.maestro/bin:$PATH"
  cd "$APP_DIR"
  step "5/5 Run device flows — HUMAN OTP ENTRY REQUIRED"
  run_flow() {
    local udid="$1" file="$2" label="$3"
    if maestro test --udid "$udid" "$APP_DIR/.maestro/$file"; then
      ok "$label passed"
      record_check "$label" PASS "$file"
    else
      fail "$label FAILED"
      record_check "$label" FAIL "$file"
    fi
  }
  run_flow "${PHYSICAL_DEVICE_UDID_LIST[0]}" \
    "29-journey-04-device-member-private-phrase.yaml" "I4-part-A-member-send"
  run_flow "${PHYSICAL_DEVICE_UDID_LIST[1]}" \
    "30-journey-04-device-organizer-group-safe-check.yaml" "I4-group-safe-assert"
  run_flow "${PHYSICAL_DEVICE_UDID_LIST[1]}" \
    "31-journey-10-device-organizer-stay-expense.yaml" "I10-part-A-organizer-create"
  run_flow "${PHYSICAL_DEVICE_UDID_LIST[0]}" \
    "32-journey-10-device-member-stay-visibility-check.yaml" "I10-visibility-assert"
  run_flow "${PHYSICAL_DEVICE_UDID_LIST[1]}" \
    "33-journey-05-device-two-account-proposal-loop.yaml" "I5-I6-I7-I8-proposal-loop"
fi

bold "Physical certification summary"
printf "  %-30s %-10s %s\n" CHECK STATUS NOTE
for result in "${RESULTS[@]}"; do
  IFS='|' read -r name status note <<<"$result"
  printf "  %-30s %-10s %s\n" "$name" "$status" "$note"
done

has_failure=0
has_block=0
for result in "${RESULTS[@]}"; do
  [[ "$result" == *"|FAIL|"* ]] && has_failure=1
  [[ "$result" == *"|BLOCKED|"* ]] && has_block=1
done

if [[ "$RUN_LIVE" != "1" || "$has_block" == "1" ]]; then
  reason="physical assertions or prerequisites were skipped"
  [[ "$RUN_LIVE" == "1" ]] || reason="RUN_LIVE=0; physical assertions were skipped"
  record_physical_receipt blocked "$reason" || true
  bold "Physical certification BLOCKED — no pass receipt written."
  exit 2
fi

if [[ "$has_failure" == "1" ]]; then
  if ! record_physical_receipt fail "one or more required physical assertions failed"; then
    record_physical_receipt blocked "physical assertions failed and receipt metadata was incomplete" || true
  fi
  bold "Physical certification FAILED — do not promote."
  exit 1
fi

if ! record_physical_receipt pass ""; then
  record_physical_receipt blocked "all assertions passed but required receipt metadata was incomplete" || true
  bold "Physical certification BLOCKED — metadata is incomplete; no pass receipt written."
  exit 2
fi

bold "Physical certification PASSED — receipt recorded for P01/P03."
