#!/usr/bin/env bash
# Verify the full contract projects deterministically to the committed app
# contract and that generated frontend types agree with that projection.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
APP_DIR="$WORKSPACE_DIR/travel-app"
FULL_SNAPSHOT_PATH="$WORKSPACE_DIR/docs/openapi.json"
APP_SNAPSHOT_PATH="$WORKSPACE_DIR/docs/openapi.app.json"
GENERATED_PATH="$APP_DIR/utils/api/schema.gen.ts"
TMP_DIR="$(mktemp -d)"
TMP_SCHEMA="$TMP_DIR/schema.gen.ts"
TMP_DIFF="$TMP_DIR/schema.diff"

cleanup() {
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT

header() {
  printf "\n== %s ==\n" "$1"
}

fail() {
  printf "ERROR: %s\n" "$1" >&2
  exit 1
}

[ -d "$APP_DIR" ] || fail "Travel App repo missing at $APP_DIR"
[ -f "$FULL_SNAPSHOT_PATH" ] || fail "OpenAPI snapshot missing at $FULL_SNAPSHOT_PATH"
[ -f "$APP_SNAPSHOT_PATH" ] || fail "App OpenAPI projection missing at $APP_SNAPSHOT_PATH"
[ -f "$GENERATED_PATH" ] || fail "Generated schema missing at $GENERATED_PATH"

header "Validate complete OpenAPI snapshot"
python3 - "$FULL_SNAPSHOT_PATH" <<'PY'
from __future__ import annotations

import json
import sys
from pathlib import Path

path = Path(sys.argv[1])
data = json.loads(path.read_text())
paths = data.get("paths", {})
schemas = data.get("components", {}).get("schemas", {})
methods = {"get", "put", "post", "delete", "options", "head", "patch", "trace"}
operations = sum(
    1
    for path_item in paths.values()
    if isinstance(path_item, dict)
    for method in path_item
    if method.lower() in methods
)

if not paths:
    raise SystemExit("OpenAPI snapshot has no paths")

print(f"Snapshot: {len(paths)} paths, {operations} operations, {len(schemas)} schemas")
PY

header "Verify active mobile projection"
python3 "$WORKSPACE_DIR/scripts/project_app_openapi.py" \
  --openapi "$FULL_SNAPSHOT_PATH" \
  --output "$APP_SNAPSHOT_PATH" \
  --check

header "Regenerate TypeScript schema"
if [ -x "$APP_DIR/node_modules/.bin/openapi-typescript" ]; then
  OPENAPI_TS=("$APP_DIR/node_modules/.bin/openapi-typescript")
else
  OPENAPI_TS=(npx --no-install openapi-typescript)
fi

(
  cd "$APP_DIR"
  "${OPENAPI_TS[@]}" "$APP_SNAPSHOT_PATH" --output "$TMP_SCHEMA"
)

header "Compare generated API types"
if diff -u "$GENERATED_PATH" "$TMP_SCHEMA" > "$TMP_DIFF"; then
  printf "Contract check passed: schema.gen.ts matches docs/openapi.app.json\n"
else
  cat "$TMP_DIFF"
  fail "schema.gen.ts is out of date. Run: make sync-types-snapshot"
fi
