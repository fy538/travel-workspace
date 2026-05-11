#!/usr/bin/env bash
# bootstrap-repos.sh — Clone or validate the child repos used by this workspace.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"

TRAVEL_AGENT_REPO="${TRAVEL_AGENT_REPO:-https://github.com/fy538/travel-agent.git}"
TRAVEL_APP_REPO="${TRAVEL_APP_REPO:-https://github.com/fy538/travel-app.git}"

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

clone_or_validate() {
  local label="$1"
  local dirname="$2"
  local repo_url="$3"
  local target="$WORKSPACE_DIR/$dirname"

  header "$label"

  if [ -d "$target/.git" ]; then
    ok "$dirname already exists as a git repo"
    local origin
    origin="$(git -C "$target" remote get-url origin 2>/dev/null || true)"
    if [ -n "$origin" ]; then
      ok "origin: $origin"
    else
      warn "$dirname has no origin remote"
    fi
    return
  fi

  if [ -e "$target" ]; then
    fail "$dirname exists but is not a git repo: $target"
  fi

  git clone "$repo_url" "$target"
  ok "cloned $repo_url into $dirname"
}

header "Workspace"
[ -d "$WORKSPACE_DIR/.git" ] || fail "Run this from a cloned Travel Workspace repo"
ok "workspace repo present at $WORKSPACE_DIR"

clone_or_validate "Travel Agent" "Travel Agent" "$TRAVEL_AGENT_REPO"
clone_or_validate "Travel App" "Travel App" "$TRAVEL_APP_REPO"

header "Next"
printf "Run: make doctor\n"
printf "Run: make contract-check\n"
