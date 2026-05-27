#!/usr/bin/env bash
# Print a cheap workspace reliability snapshot without running tests.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"
APP_DIR="$WORKSPACE_DIR/travel-app"
SNAPSHOT_PATH="$WORKSPACE_DIR/docs/openapi.json"

header() {
  printf "\n== %s ==\n" "$1"
}

status_block() {
  local label="$1"
  local dir="$2"
  header "$label"
  if [ -d "$dir/.git" ]; then
    local branch
    branch="$(git -C "$dir" branch --show-current 2>/dev/null || true)"
    printf "Branch: %s\n" "${branch:-detached HEAD}"
    local status
    status="$(git -C "$dir" status --short 2>/dev/null || true)"
    if [ -n "$status" ]; then
      printf "%s\n" "$status"
    else
      printf "Clean working tree\n"
    fi
  else
    printf "No git repository found at %s\n" "$dir"
  fi
}

header "Reliability Snapshot"
date -u +"Generated: %Y-%m-%dT%H:%M:%SZ"

header "OpenAPI Snapshot"
python3 - "$SNAPSHOT_PATH" <<'PY'
from __future__ import annotations

import json
import sys
from pathlib import Path

path = Path(sys.argv[1])
if not path.exists():
    print(f"Missing: {path}")
    raise SystemExit(0)

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

print(f"Path: {path}")
print(f"Shape: {len(paths)} paths, {operations} operations, {len(schemas)} schemas")
PY

header "Test Surface"
backend_tests="$(find "$AGENT_DIR/tests" -name 'test_*.py' 2>/dev/null | wc -l | tr -d ' ')"
frontend_tests="$(find "$APP_DIR/__tests__" -type f 2>/dev/null | wc -l | tr -d ' ')"
printf "Backend pytest files: %s\n" "$backend_tests"
printf "Frontend test files: %s\n" "$frontend_tests"

status_block "Workspace Git" "$WORKSPACE_DIR"
status_block "travel-agent Git" "$AGENT_DIR"
status_block "travel-app Git" "$APP_DIR"

header "Recommended Commands"
printf "make contract-check      # cheapest schema drift check\n"
printf "make mock-real-parity    # frontend mock/http seam check\n"
printf "make golden-path-qa      # focused MVP journey checks\n"
printf "make offline-qa          # full offline reliability ladder\n"
