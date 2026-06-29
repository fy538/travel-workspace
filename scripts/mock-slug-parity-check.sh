#!/usr/bin/env bash
# mock-slug-parity-check — dogfood corpus cities must have mock angle fixtures.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
APP_DIR="$(dirname "$SCRIPT_DIR")/travel-app"

cd "$APP_DIR"
npx jest --runInBand __tests__/conventions/mockSlugParity.test.ts
