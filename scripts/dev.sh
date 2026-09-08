#!/usr/bin/env bash
# Portable process supervision and lane runtime selection live in Python.
set -euo pipefail
exec python3 "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/dev_runtime.py" "$@"
