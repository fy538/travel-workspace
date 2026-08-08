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
PROOFS=(P01 P02 P03 P04)

usage() {
  cat <<'EOF'
Usage: scripts/dogfood-gate.sh {fast|local|device|staging}

fast     Deterministic client contracts and static registry checks.
local    fast plus the Postgres/local-plan canary.
device   local plus an explicitly supplied P01/P03 device command.
staging  an explicitly supplied deployed-environment command.

For device or staging, set DOGFOOD_DEVICE_COMMAND or DOGFOOD_STAGING_COMMAND
to the exact command that exercises the intended environment. The command is
stored in the evidence receipt; it must use the current build and test identity.
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
  local layer="$1" environment="$2" label="$3"
  shift 3
  local started status exit_code
  started="$(date +%s)"
  set +e
  "$@"
  exit_code=$?
  set -e
  if [[ "$exit_code" -eq 0 ]]; then
    status=pass
  else
    status=fail
  fi
  record "$layer" "$status" "$environment" "$label" "$(( $(date +%s) - started ))" "${PROOFS[@]}"
  return "$exit_code"
}

run_fast() {
  run_and_record contract local "dogfood-fast deterministic product-proof contracts" run_fast_contracts
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
  run_and_record database local "scripts/pre-dogfood.sh" "$SCRIPT_DIR/pre-dogfood.sh"
}

run_external() {
  local mode="$1" command_variable="$2" layer="$3" environment="$4"
  local command="${!command_variable:-}"
  if [[ -z "$command" ]]; then
    printf '✗ %s gate needs %s to be set to the exact current-build command.\n' "$mode" "$command_variable" >&2
    printf '  No %s receipt was written; this checkout remains UNRUN at that layer.\n' "$layer" >&2
    return 2
  fi
  run_and_record "$layer" "$environment" "$command" bash -lc "$command"
}

case "${1:-}" in
  fast) run_fast ;;
  local) run_local ;;
  device)
    run_local
    run_external device DOGFOOD_DEVICE_COMMAND device_mock founder-device
    ;;
  staging) run_external staging DOGFOOD_STAGING_COMMAND staging staging ;;
  *) usage; exit 2 ;;
esac
