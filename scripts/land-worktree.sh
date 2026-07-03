#!/usr/bin/env bash
# land-worktree.sh — Rebase, push, and tear down a worktree lane created by
# new-worktree.sh. This replaces an open-ended "clean up the repo" agent
# session with one bounded, scripted step per lane.
#
# What it does, per repo (agent/app), if a matching worktree exists:
#   1. fetch + rebase the lane's branch onto origin/main
#      (stops and tells you exactly what conflicts — never auto-resolves)
#   2. push straight to main (matches this workspace's existing no-PR-gate
#      convention; the repo's installed pre-push hooks run here for free,
#      since worktrees share the parent repo's .git/hooks)
#   3. fast-forward the canonical travel-agent/ or travel-app/ checkout
#   4. remove the worktree + delete the now-merged local branch
#
# Usage:
#   ./scripts/land-worktree.sh my-feature
#   ./scripts/land-worktree.sh --agent-only my-feature
#   ./scripts/land-worktree.sh --app-only my-feature
#   ./scripts/land-worktree.sh --keep my-feature   # land but don't remove the worktree

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"
APP_DIR="$WORKSPACE_DIR/travel-app"
# Must match new-worktree.sh: worktrees are direct siblings of travel-agent/
# and travel-app/, not nested — see the comment there for why.
WORKTREES_DIR="$WORKSPACE_DIR"
WT_SEP="--"

PREFIX="codex/"
RUN_AGENT=true
RUN_APP=true
KEEP_WORKTREE=false
ANY_FAILED=false

usage() {
  cat <<'EOF'
Usage:
  ./scripts/land-worktree.sh [--agent-only | --app-only] [--prefix PREFIX] [--keep] <name>

Lands the worktree(s) created by:
  ./scripts/new-worktree.sh <name>

On a rebase conflict, the script stops for that repo, tells you the
conflicted files and the exact commands to resolve or abort, then
continues on to the other repo rather than leaving both half-done.
EOF
}

land_one() {
  local repo_dir="$1"
  local repo_short="$2"
  local branch_name="$3"
  local wt_path="$WORKTREES_DIR/${repo_short}${WT_SEP}${NAME}"

  if [ ! -d "$wt_path" ]; then
    printf "  \033[33m!\033[0m %s — no worktree at %s, skipping\n" "$repo_short" "$wt_path"
    return
  fi

  printf "\n\033[1m%s\033[0m  (%s)\n" "$repo_short" "$wt_path"

  git -C "$wt_path" fetch origin main --quiet

  if ! git -C "$wt_path" rebase origin/main; then
    printf "  \033[31m✗\033[0m rebase conflict — repo left mid-rebase, nothing else touched.\n"
    printf "    Conflicted files:\n"
    git -C "$wt_path" diff --name-only --diff-filter=U | sed 's/^/      /'
    printf "    Resolve in %s, then:\n" "$wt_path"
    printf "      git -C \"%s\" add <file>...\n" "$wt_path"
    printf "      git -C \"%s\" rebase --continue\n" "$wt_path"
    printf "    (or git -C \"%s\" rebase --abort to bail)\n" "$wt_path"
    printf "    Re-run this script once the rebase is clean.\n"
    ANY_FAILED=true
    return
  fi
  printf "  \033[32m✓\033[0m rebased cleanly onto origin/main\n"

  if ! git -C "$wt_path" push origin "HEAD:main"; then
    printf "  \033[31m✗\033[0m push rejected — main moved again since the rebase. Re-run this script.\n"
    ANY_FAILED=true
    return
  fi
  printf "  \033[32m✓\033[0m pushed to main\n"

  git -C "$repo_dir" fetch origin main --quiet
  git -C "$repo_dir" pull --ff-only --quiet
  printf "  \033[32m✓\033[0m canonical %s checkout fast-forwarded\n" "$repo_short"

  if [ "$KEEP_WORKTREE" = false ]; then
    git -C "$repo_dir" worktree remove "$wt_path"
    git -C "$repo_dir" branch -d "$branch_name" >/dev/null 2>&1 || true
    printf "  \033[32m✓\033[0m worktree removed, branch %s deleted\n" "$branch_name"
  else
    printf "  \033[33m!\033[0m --keep set: worktree left in place at %s\n" "$wt_path"
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
    --keep)
      KEEP_WORKTREE=true
      shift
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

printf "\033[1mLanding worktree lane\033[0m  (branch %s)\n" "$BRANCH_NAME"

if [ "$RUN_AGENT" = true ]; then
  land_one "$AGENT_DIR" "travel-agent" "$BRANCH_NAME"
fi

if [ "$RUN_APP" = true ]; then
  land_one "$APP_DIR" "travel-app" "$BRANCH_NAME"
fi

if [ "$ANY_FAILED" = true ]; then
  printf "\n\033[31mOne or more repos need manual attention — see above.\033[0m\n"
  exit 1
fi

printf "\n\033[32mLanded.\033[0m Run the cross-repo gate once both repos are in:\n"
printf "  cd \"%s\" && make certify-fast\n" "$WORKSPACE_DIR"
