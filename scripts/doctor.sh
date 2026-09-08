#!/usr/bin/env bash
# doctor.sh — Lightweight workspace health check.
#
# Validates that the parent workspace and both child repos are present,
# then checks for the core tools used in the current workflow.

set -euo pipefail
unset GIT_DIR GIT_WORK_TREE GIT_COMMON_DIR GIT_INDEX_FILE

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"
APP_DIR="$WORKSPACE_DIR/travel-app"
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

[ -d "$AGENT_DIR" ] || fail "travel-agent repo missing at $AGENT_DIR"
[ -d "$APP_DIR" ] || fail "travel-app repo missing at $APP_DIR"
[ -e "$WORKSPACE_DIR/.git" ] || fail "Workspace repo missing .git at $WORKSPACE_DIR"
ok "Workspace repo present"
ok "travel-agent repo present"
ok "travel-app repo present"

tracked_child_files="$(
  git -C "$WORKSPACE_DIR" ls-files -- "travel-agent" "travel-app" 2>/dev/null || true
)"
if [ -n "$tracked_child_files" ]; then
  fail "Workspace is tracking files inside child repos. Remove them from the parent index."
else
  ok "Workspace is not tracking child repo source"
fi

check_ignored "travel-agent/README.md" "travel-agent"
check_ignored "travel-app/README.md" "travel-app"

if [ -f "$SNAPSHOT_PATH" ]; then
  ok "Committed OpenAPI snapshot present"
else
  warn "Committed OpenAPI snapshot missing at $SNAPSHOT_PATH"
fi

header "Git"

check_command git

if [ -e "$AGENT_DIR/.git" ] && git -C "$AGENT_DIR" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  ok "travel-agent git repo healthy"
else
  fail "travel-agent is not a valid git repo"
fi

if [ -e "$APP_DIR/.git" ] && git -C "$APP_DIR" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  ok "travel-app git repo healthy"
else
  fail "travel-app is not a valid git repo"
fi

agent_branch="$(git -C "$AGENT_DIR" branch --show-current || true)"
app_branch="$(git -C "$APP_DIR" branch --show-current || true)"
ok "travel-agent branch: ${agent_branch:-detached HEAD}"
ok "travel-app branch: ${app_branch:-detached HEAD}"

header "Tooling"

check_command docker "Docker"
check_command uvicorn "uvicorn"
check_command npx "npx"
check_command python3 "python3"
check_command node "node"

if command -v maestro >/dev/null 2>&1; then
  ok "Maestro CLI available"
  if [ -n "${JAVA_HOME:-}" ] && [ -x "${JAVA_HOME}/bin/java" ]; then
    ok "JAVA_HOME set ($JAVA_HOME)"
  elif [ -x /opt/homebrew/opt/openjdk/bin/java ]; then
    ok "Homebrew openjdk available (/opt/homebrew/opt/openjdk)"
  elif /usr/libexec/java_home >/dev/null 2>&1; then
    ok "Java runtime available (required for Maestro)"
  else
    warn "Java runtime not found — make certify-visual / maestro test will fail"
    warn "Install: brew install openjdk (or brew install --cask temurin)"
  fi
else
  warn "Maestro not found (optional for make certify-visual)"
fi

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
  ok "travel-agent origin: $agent_remote"
else
  warn "travel-agent has no origin remote"
fi

if [ -n "$app_remote" ]; then
  ok "travel-app origin: $app_remote"
else
  warn "travel-app has no origin remote"
fi

header "Selected runtime (credentials omitted)"
python3 "$SCRIPT_DIR/dev_runtime.py" --print-runtime || fail "Runtime configuration is invalid"
if [ "${1:-}" = "--services" ]; then
  python3 "$SCRIPT_DIR/dev_runtime.py" --check-services || fail "Selected Compose Postgres is unavailable"
  ok "Selected Compose Postgres service is ready"
else
  ok "Service probes unrun (use --services after selecting the lane runtime)"
fi
printf "\n\033[32mWorkspace doctor complete.\033[0m\n"
