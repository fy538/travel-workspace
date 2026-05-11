#!/usr/bin/env bash
# new-branch.sh — Create or switch coordinated branches in the child repos.
#
# Usage:
#   ./scripts/new-branch.sh my-feature
#   ./scripts/new-branch.sh --agent-only my-feature
#   ./scripts/new-branch.sh --app-only my-feature
#   ./scripts/new-branch.sh --prefix feature/ my-feature

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/Travel Agent"
APP_DIR="$WORKSPACE_DIR/Travel App"

PREFIX="codex/"
RUN_AGENT=true
RUN_APP=true

usage() {
  cat <<'EOF'
Usage:
  ./scripts/new-branch.sh [--agent-only | --app-only] [--prefix PREFIX] <name>

Examples:
  ./scripts/new-branch.sh trip-group-chat
  ./scripts/new-branch.sh --agent-only booking-event-fix
  ./scripts/new-branch.sh --prefix feature/ home-routing-audit
EOF
}

switch_or_create() {
  local repo_dir="$1"
  local branch_name="$2"
  local label="$3"

  if git -C "$repo_dir" show-ref --verify --quiet "refs/heads/$branch_name"; then
    git -C "$repo_dir" switch "$branch_name" >/dev/null
    printf "  \033[32m✓\033[0m %s switched to existing branch %s\n" "$label" "$branch_name"
  else
    git -C "$repo_dir" switch -c "$branch_name" >/dev/null
    printf "  \033[32m✓\033[0m %s created branch %s\n" "$label" "$branch_name"
  fi
}

while [ $# -gt 0 ]; do
  case "$1" in
    --agent-only)
      RUN_AGENT=true
      RUN_APP=false
      shift
      ;;
    --app-only)
      RUN_AGENT=false
      RUN_APP=true
      shift
      ;;
    --prefix)
      [ $# -ge 2 ] || { usage; exit 1; }
      PREFIX="$2"
      shift 2
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    --*)
      printf "Unknown option: %s\n\n" "$1" >&2
      usage
      exit 1
      ;;
    *)
      break
      ;;
  esac
done

[ $# -eq 1 ] || { usage; exit 1; }

NAME="$1"
BRANCH_NAME="${PREFIX}${NAME}"

[ -d "$AGENT_DIR/.git" ] || { echo "Travel Agent repo missing at $AGENT_DIR" >&2; exit 1; }
[ -d "$APP_DIR/.git" ] || { echo "Travel App repo missing at $APP_DIR" >&2; exit 1; }

printf "\n\033[1mCoordinated branch setup\033[0m\n"
printf "  Branch: %s\n\n" "$BRANCH_NAME"

if [ "$RUN_AGENT" = true ]; then
  switch_or_create "$AGENT_DIR" "$BRANCH_NAME" "Travel Agent"
fi

if [ "$RUN_APP" = true ]; then
  switch_or_create "$APP_DIR" "$BRANCH_NAME" "Travel App"
fi

printf "\n\033[32mDone.\033[0m\n"
