#!/usr/bin/env bash
# Layered pre-dogfood gate for the product proof spine.
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
device   local, then fail closed until a governed proof-specific device runner exists.
physical Reserved; fails closed and directs operators to dogfood-physical.
staging  fail closed until a deployed-API runner is registered for the requested proof.

Physical evidence is never accepted from an arbitrary
shell command; use `make dogfood-physical RUN_LIVE=1` so hardware and artifacts
are verified by the first-class runner.
Device-mock and staging passes must be added as governed runners in
docs/journeys/evidence-runners.yaml; arbitrary operator shell commands cannot
produce promotable evidence.
EOF
}

record() {
  local layer="$1" status="$2" environment="$3" command="$4" duration="$5" runner_id="$6"
  shift 6
  local args=()
  local proof
  for proof in "$@"; do
    args+=(--journey "$proof")
  done
  "${EVIDENCE_TOOL[@]}" record \
    --layer "$layer" --status "$status" --environment "$environment" \
    --command "$command" --runner-id "$runner_id" --duration-seconds "$duration" \
    "${args[@]}" >/dev/null
}

run_and_record() {
  local layer="$1" environment="$2" label="$3" runner_id="$4" runner="$5"
  shift 5
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
      P01|P02|P03|P04|P05|P06|P07) ;;
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
  "$runner" "${runner_args[@]+"${runner_args[@]}"}"
  exit_code=$?
  set -e
  if [[ "$exit_code" -eq 0 ]]; then
    status=pass
  else
    status=fail
  fi
  record "$layer" "$status" "$environment" "$label" "$(( $(date +%s) - started ))" \
    "$runner_id" "${proof_args[@]}"
  return "$exit_code"
}

run_fast() {
  run_and_record contract local "dogfood-fast deterministic product-proof contracts" \
    dogfood-fast-contract-v1 run_fast_contracts \
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
  run_and_record database local "scripts/pre-dogfood.sh" dogfood-local-database-v1 \
    "$SCRIPT_DIR/pre-dogfood.sh" \
    -- P01 P02 P03 P04
}

case "${1:-}" in
  fast) run_fast ;;
  local) run_local ;;
  device)
    run_local
    printf '✗ No governed device-mock product-proof runner is registered yet.\n' >&2
    printf '  Add a proof-specific runner to docs/journeys/evidence-runners.yaml.\n' >&2
    exit 2
    ;;
  physical)
    printf '✗ Arbitrary physical commands cannot produce evidence.\n' >&2
    printf '  Run: make dogfood-physical RUN_LIVE=1\n' >&2
    exit 2
    ;;
  staging)
    printf '✗ No governed deployed-API staging runner is registered yet.\n' >&2
    printf '  Direct database scripts and arbitrary shell commands cannot certify staging.\n' >&2
    exit 2
    ;;
  *) usage; exit 2 ;;
esac
