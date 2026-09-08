#!/usr/bin/env bash
# Verify all three committed lane revisions before optionally publishing their
# branches for protected-main review. Never push main or mutate another checkout.
set -euo pipefail
exec python3 "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/worktree_lane.py" land "$@"
