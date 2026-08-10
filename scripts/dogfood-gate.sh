#!/usr/bin/env bash
# Layered pre-dogfood gate for the P01–P04 product proof spine.
#
# This records only evidence the invoked command actually establishes. A local
# database run is not device evidence; a missing staging/device command is a
# deliberate non-zero stop rather than an invented green result.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
EVIDENCE_TOOL=(python3 "$SCRIPT_DIR/journey_evidence.py")
PROOF_IDS=(P01 P02 P03 P04)

usage() {
  cat <<'EOF'
Usage: scripts/dogfood-gate.sh {fast|local|device|physical|staging}

fast     Deterministic client contracts and static registry checks (P01–P04 contract anchors).
local    fast plus the Postgres/local-plan canary (P01–P04 database anchors).
device   local plus an explicitly supplied P01/P03 device-mock command.
physical Reserved; fails closed and directs operators to dogfood-physical.
staging  an explicitly supplied deployed-environment command and proof list.

For device, set DOGFOOD_DEVICE_COMMAND to the exact command that exercises the
device-mock environment. It records only P01/P03 (the proofs whose registry
requires device_mock). Physical evidence is never accepted from an arbitrary
shell command; use `make dogfood-physical RUN_LIVE=1` so hardware and artifacts
are verified by the first-class runner.
For staging, set DOGFOOD_STAGING_COMMAND and DOGFOOD_STAGING_PROOFS (a
comma-separated list of P01–P04) explicitly. Missing commands or proof lists
are a blocked run and never produce a pass receipt.
EOF
}

record() {
  local layer="$1" status="$2" environment="$3" command="$4" duration="$5"
  shift 5
  local args=()
  local proof
  for proof in "$@"; do
    args+=(--journey "$proof")
  done
  "${EVIDENCE_TOOL[@]}" record \
    --layer "$layer" --status "$status" --environment "$environment" \
    --command "$command" --duration-seconds "$duration" "${args[@]}" >/dev/null
}

run_and_record() {
  local layer="$1" environment="$2" label="$3" runner="$4"
  shift 4
  local runner_args=() proof_args=() arg
  while [[ "$#" -gt 0 && "$1" != "--" ]]; do
    runner_args+=("$1")
    shift
  done
  [[ "$#" -gt 0 && "$1" == "--" ]] || {
    printf '✗ Internal runner error: missing proof separator for %s.\n' "$label" >&2
    return 2
  }
  shift
  proof_args=("$@")
  for arg in "${proof_args[@]}"; do
    case "$arg" in
      P01|P02|P03|P04) ;;
      *) printf '✗ Unknown proof id: %s\n' "$arg" >&2; return 2 ;;
    esac
  done
  [[ "${#proof_args[@]}" -gt 0 ]] || {
    printf '✗ Runner %s must declare at least one proof id.\n' "$label" >&2
    return 2
  }
  local started status exit_code
  started="$(date +%s)"
  set +e
  "$runner" "${runner_args[@]}"
  exit_code=$?
  set -e
  if [[ "$exit_code" -eq 0 ]]; then
    status=pass
  else
    status=fail
  fi
  record "$layer" "$status" "$environment" "$label" "$(( $(date +%s) - started ))" "${proof_args[@]}"
  return "$exit_code"
}

run_fast() {
  run_and_record contract local "dogfood-fast deterministic product-proof contracts" run_fast_contracts \
    -- P01 P02 P03 P04
}

run_fast_contracts() {
  cd "$WORKSPACE_DIR"
  ./scripts/contract-check.sh
  python3 scripts/check_journey_registry.py
  python3 scripts/validate-maestro-flows.py --app-dir travel-app
  cd travel-app
  npx jest --runInBand \
    __tests__/journeys/local-occasion-closure.replay.test.tsx \
    __tests__/journeys/local-occasion-transport.replay.test.tsx \
    __tests__/components/trip-plan/OccurrenceArtifactCard.test.tsx
  npm run --silent typecheck
  npm run --silent test:typecheck:contracts
}

run_local() {
  run_fast
  run_and_record database local "scripts/pre-dogfood.sh" "$SCRIPT_DIR/pre-dogfood.sh" \
    -- P01 P02 P03 P04
}

run_shell_command() {
  bash -lc "$1"
}

run_external() {
  local mode="$1" command_variable="$2" layer="$3" environment="$4"
  shift 4
  local proofs=("$@")
  local command="${!command_variable:-}"
  if [[ -z "$command" ]]; then
    printf '✗ %s gate needs %s to be set to the exact current-build command.\n' "$mode" "$command_variable" >&2
    printf '  No %s receipt was written; this checkout remains UNRUN/BLOCKED at that layer.\n' "$layer" >&2
    return 2
  fi
  run_and_record "$layer" "$environment" "$command" run_shell_command "$command" -- "${proofs[@]}"
}

parse_proofs() {
  local raw="$1" item
  PARSED_PROOFS=()
  [[ -n "$raw" ]] || { printf '✗ A comma-separated proof list is required.\n' >&2; return 2; }
  IFS=',' read -r -a PARSED_PROOFS <<<"$raw"
  [[ "${#PARSED_PROOFS[@]}" -gt 0 ]] || return 2
  for item in "${PARSED_PROOFS[@]}"; do
    [[ "$item" =~ ^P0[1-4]$ ]] || { printf '✗ Invalid proof id in list: %s\n' "$item" >&2; return 2; }
  done
}

case "${1:-}" in
  fast) run_fast ;;
  local) run_local ;;
  device)
    run_local
    run_external device DOGFOOD_DEVICE_COMMAND device_mock founder-device P01 P03
    ;;
  physical)
    printf '✗ Arbitrary physical commands cannot produce evidence.\n' >&2
    printf '  Run: make dogfood-physical RUN_LIVE=1\n' >&2
    exit 2
    ;;
  staging)
    parse_proofs "${DOGFOOD_STAGING_PROOFS:-}"
    run_external staging DOGFOOD_STAGING_COMMAND staging staging "${PARSED_PROOFS[@]}"
    ;;
  *) usage; exit 2 ;;
esac
