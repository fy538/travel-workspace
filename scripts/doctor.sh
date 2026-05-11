#!/usr/bin/env bash
# doctor.sh — Lightweight workspace health check.
#
# Validates that the parent workspace and both child repos are present,
# then checks for the core tools used in the current workflow.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/Travel Agent"
APP_DIR="$WORKSPACE_DIR/Travel App"
SNAPSHOT_PATH="$WORKSPACE_DIR/docs/openapi.json"

ok() {
  printf "  \033[32m✓\033[0m %s\n" "$1"
}

warn() {
  printf "  \033[33m⚠\033[0m %s\n" "$1"
}

fail() {
  printf "  \033[31m✗\033[0m %s\n" "$1"
  exit 1
}

header() {
  printf "\n\033[1m%s\033[0m\n" "$1"
}

check_command() {
  local cmd="$1"
  local label="${2:-$1}"
  if command -v "$cmd" >/dev/null 2>&1; then
    ok "$label available"
  else
    warn "$label not found"
  fi
}

check_ignored() {
  local path="$1"
  local label="$2"
  if git -C "$WORKSPACE_DIR" check-ignore -q "$path"; then
    ok "$label ignored by workspace git"
  else
    warn "$label is not ignored by workspace git"
  fi
}

header "Workspace"

[ -d "$AGENT_DIR" ] || fail "Travel Agent repo missing at $AGENT_DIR"
[ -d "$APP_DIR" ] || fail "Travel App repo missing at $APP_DIR"
[ -d "$WORKSPACE_DIR/.git" ] || fail "Workspace repo missing .git at $WORKSPACE_DIR"
ok "Workspace repo present"
ok "Travel Agent repo present"
ok "Travel App repo present"

tracked_child_files="$(
  git -C "$WORKSPACE_DIR" ls-files -- "Travel Agent" "Travel App" 2>/dev/null || true
)"
if [ -n "$tracked_child_files" ]; then
  fail "Workspace is tracking files inside child repos. Remove them from the parent index."
else
  ok "Workspace is not tracking child repo source"
fi

check_ignored "Travel Agent/README.md" "Travel Agent"
check_ignored "Travel App/README.md" "Travel App"

if [ -f "$SNAPSHOT_PATH" ]; then
  ok "Committed OpenAPI snapshot present"
else
  warn "Committed OpenAPI snapshot missing at $SNAPSHOT_PATH"
fi

header "Git"

check_command git

if git -C "$AGENT_DIR" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  ok "Travel Agent git repo healthy"
else
  fail "Travel Agent is not a valid git repo"
fi

if git -C "$APP_DIR" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  ok "Travel App git repo healthy"
else
  fail "Travel App is not a valid git repo"
fi

agent_branch="$(git -C "$AGENT_DIR" branch --show-current || true)"
app_branch="$(git -C "$APP_DIR" branch --show-current || true)"
ok "Travel Agent branch: ${agent_branch:-detached HEAD}"
ok "Travel App branch: ${app_branch:-detached HEAD}"

header "Tooling"

check_command docker "Docker"
check_command uvicorn "uvicorn"
check_command npx "npx"
check_command python3 "python3"
check_command node "node"

header "Remotes"

workspace_remote="$(git -C "$WORKSPACE_DIR" remote get-url origin 2>/dev/null || true)"
agent_remote="$(git -C "$AGENT_DIR" remote get-url origin 2>/dev/null || true)"
app_remote="$(git -C "$APP_DIR" remote get-url origin 2>/dev/null || true)"

if [ -n "$workspace_remote" ]; then
  ok "Workspace origin: $workspace_remote"
else
  warn "Workspace has no origin remote"
fi

if [ -n "$agent_remote" ]; then
  ok "Travel Agent origin: $agent_remote"
else
  warn "Travel Agent has no origin remote"
fi

if [ -n "$app_remote" ]; then
  ok "Travel App origin: $app_remote"
else
  warn "Travel App has no origin remote"
fi

printf "\n\033[32mWorkspace doctor complete.\033[0m\n"
