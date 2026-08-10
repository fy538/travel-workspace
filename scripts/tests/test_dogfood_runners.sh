#!/usr/bin/env bash
# Focused, dependency-free checks for proof-runner wiring and fail-closed modes.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

bash -n scripts/dogfood-gate.sh scripts/dogfood-device-cert-live.sh scripts/certify-live.sh

set +e
staging_output="$(./scripts/dogfood-gate.sh staging 2>&1)"
staging_status=$?
physical_output="$(DOGFOOD_PHYSICAL_COMMAND=true ./scripts/dogfood-gate.sh physical 2>&1)"
physical_status=$?
set -e

[[ "$staging_status" -eq 2 ]]
[[ "$staging_output" == *"proof list is required"* ]]
[[ "$physical_status" -eq 2 ]]
[[ "$physical_output" == *"PHYSICAL_APP_BUILD_ID"* ]]

grep -q '^dogfood-physical:' Makefile
grep -q 'record_physical_external' scripts/dogfood-gate.sh
grep -q -- '--app-build-id' scripts/dogfood-gate.sh
! grep -q 'Record pass/fail in docs/journeys/STATUS.md' scripts/certify-live.sh

printf 'dogfood runner wiring and fail-closed checks passed.\n'
