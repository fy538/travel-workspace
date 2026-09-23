#!/usr/bin/env bash
# A lane always includes the workspace plus both child checkouts, so contracts
# and hooks resolve against this task. See --help for explicit base/path options.
set -euo pipefail
exec python3 "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/worktree_lane.py" create "$@"
