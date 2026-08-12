#!/usr/bin/env bash
# Thin wrapper so the fast-path gate has the filename the working note
# names (scripts/verify-changed.sh) while the actual routing logic lives
# in verify_changed.py, where it discovers the workspace and both independent
# child repositories using explicit base refs.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$SCRIPT_DIR/verify_changed.py" "$@"
