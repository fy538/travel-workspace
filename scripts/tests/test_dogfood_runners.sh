#!/usr/bin/env bash
# Focused, dependency-free checks for proof-runner wiring and fail-closed modes.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

bash -n scripts/dogfood-gate.sh scripts/dogfood-device-cert-live.sh scripts/certify-live.sh

set +e
staging_output="$(./scripts/dogfood-gate.sh staging 2>&1)"
staging_status=$?
physical_output="$(./scripts/dogfood-gate.sh physical 2>&1)"
physical_status=$?
set -e

[[ "$staging_status" -eq 2 ]]
[[ "$staging_output" == *"proof list is required"* ]]

set +e
staging_p07_output="$(DOGFOOD_STAGING_PROOFS=P07 ./scripts/dogfood-gate.sh staging 2>&1)"
staging_p07_status=$?
set -e
[[ "$staging_p07_status" -eq 2 ]]
[[ "$staging_p07_output" == *"DOGFOOD_STAGING_COMMAND"* ]]
[[ "$staging_p07_output" != *"Invalid proof id"* ]]

[[ "$physical_status" -eq 2 ]]
[[ "$physical_output" == *"Arbitrary physical commands cannot produce evidence"* ]]

grep -q '^dogfood-physical:' Makefile
grep -q -- 'maestro test --udid' scripts/dogfood-device-cert-live.sh
grep -q 'physical_evidence.py' scripts/dogfood-device-cert-live.sh
! grep -q 'DOGFOOD_PHYSICAL_COMMAND' scripts/dogfood-gate.sh
! grep -q 'Record pass/fail in docs/journeys/STATUS.md' scripts/certify-live.sh

printf 'dogfood runner wiring and fail-closed checks passed.\n'
