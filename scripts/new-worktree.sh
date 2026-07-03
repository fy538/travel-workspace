#!/usr/bin/env bash
# new-worktree.sh — Create isolated git worktrees for a concurrent agent lane.
#
# The problem this solves: two coding-agent sessions (Claude Code, Codex,
# Cursor, ...) pointed at the SAME travel-agent/travel-app checkout will
# clobber each other's uncommitted edits and produce a confusing combined
# git status. This gives each concurrent session its own working directory
# and branch, in both child repos, under one coordinated name — so two
# sessions can run at once without touching each other's files.
#
# Usage:
#   ./scripts/new-worktree.sh my-feature
#   ./scripts/new-worktree.sh --agent-only my-feature
#   ./scripts/new-worktree.sh --app-only my-feature
#   ./scripts/new-worktree.sh --prefix feature/ my-feature
#   ./scripts/new-worktree.sh --base origin/main my-feature

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"
APP_DIR="$WORKSPACE_DIR/travel-app"
# Worktrees live as DIRECT siblings of travel-agent/ and travel-app/ (not
# nested one level deeper, e.g. under .worktrees/) because both repos'
# .pre-commit-config.yaml hooks reference workspace scripts via a hardcoded
# "../scripts/..." — that only resolves correctly when the checkout is
# exactly one directory below the workspace root. Nesting worktrees deeper
# silently breaks the secret-prefix pre-commit hook (found the hard way).
WORKTREES_DIR="$WORKSPACE_DIR"
WT_SEP="--"

PREFIX="codex/"
RUN_AGENT=true
RUN_APP=true
BASE_REF=""

usage() {
  cat <<'EOF'
Usage:
  ./scripts/new-worktree.sh [--agent-only | --app-only] [--prefix PREFIX] [--base REF] <name>

Examples:
  ./scripts/new-worktree.sh trip-group-chat
  ./scripts/new-worktree.sh --agent-only booking-event-fix
  ./scripts/new-worktree.sh --base origin/main home-routing-audit

Creates a sibling working directory per repo at:
  travel-agent--<name>/
  travel-app--<name>/
each on its own branch (default prefix "codex/"), so a second agent
session can point at it without sharing files with any other session.

Land the branch back into main with:
  ./scripts/land-worktree.sh <name>
EOF
}

create_worktree() {
  local repo_dir="$1"
  local repo_short="$2"   # "travel-agent" | "travel-app"
  local branch_name="$3"
  local wt_path="$WORKTREES_DIR/${repo_short}${WT_SEP}${NAME}"

  if [ -d "$wt_path" ]; then
    printf "  \033[33m!\033[0m %s worktree already exists at %s — skipping\n" "$repo_short" "$wt_path"
    return
  fi

  if git -C "$repo_dir" show-ref --verify --quiet "refs/heads/$branch_name"; then
    echo "Branch $branch_name already exists in $repo_short — checking it out into the new worktree." >&2
    git -C "$repo_dir" worktree add "$wt_path" "$branch_name" >/dev/null
  else
    local base="${BASE_REF:-HEAD}"
    git -C "$repo_dir" worktree add -b "$branch_name" "$wt_path" "$base" >/dev/null
  fi

  printf "  \033[32m✓\033[0m %s worktree ready: %s  (branch %s)\n" "$repo_short" "$wt_path" "$branch_name"
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
    --base)
      [ $# -ge 2 ] || { usage; exit 1; }
      BASE_REF="$2"
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

printf "\n\033[1mIsolated worktree lane\033[0m\n"
printf "  Branch: %s\n" "$BRANCH_NAME"
printf "  Base:   %s\n\n" "${BASE_REF:-current HEAD of each repo}"

if [ "$RUN_AGENT" = true ]; then
  create_worktree "$AGENT_DIR" "travel-agent" "$BRANCH_NAME"
fi

if [ "$RUN_APP" = true ]; then
  create_worktree "$APP_DIR" "travel-app" "$BRANCH_NAME"
fi

printf "\n\033[32mDone.\033[0m Point your next agent session at:\n"
[ "$RUN_AGENT" = true ] && printf "  %s\n" "$WORKTREES_DIR/travel-agent${WT_SEP}${NAME}"
[ "$RUN_APP" = true ] && printf "  %s\n" "$WORKTREES_DIR/travel-app${WT_SEP}${NAME}"
printf "\nWhen the work is ready to merge: ./scripts/land-worktree.sh %s\n" "$NAME"
