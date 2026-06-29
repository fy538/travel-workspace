#!/usr/bin/env bash
# Promote a dogfood city pack to Fly (Postgres + cloud Qdrant).
#
# Wrapper around dogfood-city with PROFILE=fly APPLY=1 ENRICH=1.
#
# Usage:
#   scripts/dogfood-promote.sh CITY=lisbon              # dry-run
#   APPLY=1 scripts/dogfood-promote.sh CITY=rome        # write to Fly + cloud Qdrant
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CITY=""
for arg in "$@"; do
  case "$arg" in
    CITY=*) CITY="${arg#CITY=}" ;;
  esac
done
CITY="${CITY:-${CITY_ENV:-}}"
if [[ -z "$CITY" ]]; then
  echo "usage: scripts/dogfood-promote.sh CITY=<lisbon|rome|tokyo|istanbul|brooklyn>" >&2
  exit 2
fi

APPLY="${APPLY:-0}"
export PROFILE=fly

echo "▸ dogfood-promote CITY=$CITY PROFILE=fly APPLY=$APPLY"
exec env APPLY="$APPLY" ENRICH=1 PROFILE=fly "$SCRIPT_DIR/dogfood-city.sh" "CITY=$CITY"
