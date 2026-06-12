#!/usr/bin/env bash
# Pre-flight gate before invoking ``eas build --platform ios --profile production``.
#
# An EAS production build queues for 5-15 minutes and then runs for 20+
# minutes on Expo's infra. A build that fails after that wait because
# the EAS projectId is still the placeholder UUID, or because the API
# types are stale, or because Clerk isn't configured, is a 30-45 minute
# round-trip to discover a 30-second fixable problem. This script does
# every cheap check first.
#
# Exits non-zero on the first failure with a clear message naming the
# fix. Run from the workspace root.
#
# Usage:
#   ./scripts/preflight-eas-build.sh
#
# Skip individual checks via env:
#   SKIP_TESTS=1                  — skip frontend Jest run
#   SKIP_BACKEND_TESTS=1          — skip backend pytest run
#   SKIP_LIVE_API_PROBE=1         — skip the GET against EXPO_PUBLIC_API_URL/health

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"
APP_DIR="$WORKSPACE_DIR/travel-app"

PASS=0
FAIL=0
FIRST_FAIL=""

pass() {
  printf "  \033[32m✓\033[0m %s\n" "$1"
  PASS=$((PASS + 1))
}

fail() {
  printf "  \033[31m✗\033[0m %s\n" "$1"
  FAIL=$((FAIL + 1))
  if [ -z "$FIRST_FAIL" ]; then
    FIRST_FAIL="$1"
  fi
}

step() {
  printf "\n\033[1m== %s ==\033[0m\n" "$1"
}

abort() {
  printf "\n\033[31mPre-flight aborted. First failure:\033[0m %s\n" "$FIRST_FAIL"
  printf "Fix it and re-run. Do NOT invoke eas build until this passes green.\n"
  exit 1
}

require_command() {
  if ! command -v "$1" >/dev/null 2>&1; then
    fail "$1 is not on PATH — install before running EAS build"
    return 1
  fi
}

printf "\033[1mEAS production-build pre-flight\033[0m\n"
printf "  workspace: %s\n" "$WORKSPACE_DIR"

# ── 1. Toolchain ─────────────────────────────────────────────────────────────
step "1. Toolchain present"
require_command node && pass "node $(node --version)" || true
require_command npm && pass "npm $(npm --version)" || true
require_command npx && pass "npx present" || true
if command -v eas >/dev/null 2>&1; then
  pass "eas CLI $(eas --version 2>/dev/null | head -1)"
else
  fail "eas CLI not on PATH — 'npm i -g eas-cli' then re-run"
fi
require_command python3 && pass "python3 $(python3 --version | awk '{print $2}')" || true

[ "$FAIL" -eq 0 ] || abort

# ── 2. EAS project identity ──────────────────────────────────────────────────
step "2. EAS project identity"
APP_JSON="$APP_DIR/app.json"
if [ ! -f "$APP_JSON" ]; then
  fail "travel-app/app.json missing"
  abort
fi

EAS_PROJECT_ID=$(python3 -c "import json; d=json.load(open('$APP_JSON')); print(d['expo'].get('extra',{}).get('eas',{}).get('projectId',''))" 2>/dev/null)
if [ -z "$EAS_PROJECT_ID" ]; then
  fail "expo.extra.eas.projectId missing from app.json — run 'cd travel-app && eas init'"
elif [ "$EAS_PROJECT_ID" = "00000000-0000-0000-0000-000000000000" ]; then
  fail "EAS projectId is still the placeholder UUID — run 'cd travel-app && eas init' (OAI #3)"
else
  pass "EAS projectId set ($EAS_PROJECT_ID)"
fi

BUNDLE_ID=$(python3 -c "import json; d=json.load(open('$APP_JSON')); print(d['expo'].get('ios',{}).get('bundleIdentifier',''))" 2>/dev/null)
if [ -z "$BUNDLE_ID" ]; then
  fail "expo.ios.bundleIdentifier missing from app.json"
else
  pass "ios bundleIdentifier set ($BUNDLE_ID)"
fi

ASSOCIATED_DOMAINS=$(python3 -c "import json; d=json.load(open('$APP_JSON')); print(','.join(d['expo'].get('ios',{}).get('associatedDomains',[])))" 2>/dev/null)
if [ -z "$ASSOCIATED_DOMAINS" ] || [[ "$ASSOCIATED_DOMAINS" != *"applinks:"* ]]; then
  fail "ios.associatedDomains missing or has no applinks: entry — Universal Links won't work"
else
  pass "ios.associatedDomains set ($ASSOCIATED_DOMAINS)"
fi

[ "$FAIL" -eq 0 ] || abort

# ── 3. EAS production profile (eas.json — the authoritative source) ─────────
step "3. EAS production profile (eas.json)"

# An EAS build resolves env vars in this order:
#   1. eas.json `build.production.env` block      ← checked here (committed)
#   2. Expo dashboard / `eas env` (secrets)       ← Clerk key lives here (3b)
#   3. Local .env files (dev mode only)
#
# The three run-mode flags + API URL are committed in eas.json, so we read
# them straight from the file — this is the real check, not a shell proxy.
# The runtime leak guard in app/_layout.tsx (`!__DEV__ && (useMock ||
# skipAuth)` throws at boot) is the backstop if the profile is ever wrong.

EAS_JSON="$APP_DIR/eas.json"
if [ ! -f "$EAS_JSON" ]; then
  fail "travel-app/eas.json missing — run 'cd travel-app && eas build:configure' (OAI #3)"
  abort
fi

read_eas_env() {
  python3 -c "import json; d=json.load(open('$EAS_JSON')); print(d.get('build',{}).get('production',{}).get('env',{}).get('$1',''))" 2>/dev/null
}

eas_mock="$(read_eas_env EXPO_PUBLIC_USE_MOCK_API)"
eas_skip="$(read_eas_env EXPO_PUBLIC_SKIP_AUTH)"
eas_url="$(read_eas_env EXPO_PUBLIC_API_URL)"

if [ "$(printf '%s' "$eas_mock" | tr '[:upper:]' '[:lower:]')" = "false" ]; then
  pass "production.env EXPO_PUBLIC_USE_MOCK_API=false"
else
  fail "production.env EXPO_PUBLIC_USE_MOCK_API='$eas_mock' (must be 'false' for release builds)"
fi

if [ "$(printf '%s' "$eas_skip" | tr '[:upper:]' '[:lower:]')" = "false" ]; then
  pass "production.env EXPO_PUBLIC_SKIP_AUTH=false"
else
  fail "production.env EXPO_PUBLIC_SKIP_AUTH='$eas_skip' (must be 'false' for release builds)"
fi

if [ -z "$eas_url" ]; then
  fail "production.env EXPO_PUBLIC_API_URL is unset"
elif [[ "$eas_url" == *localhost* ]] || [[ "$eas_url" == http://127.0.0.1* ]]; then
  fail "production.env EXPO_PUBLIC_API_URL=$eas_url points at localhost — won't work in a TestFlight build"
elif [[ "$eas_url" != https://* ]]; then
  fail "production.env EXPO_PUBLIC_API_URL=$eas_url is not https — Apple rejects mixed-content traffic"
else
  pass "production.env EXPO_PUBLIC_API_URL=$eas_url"
fi

[ "$FAIL" -eq 0 ] || abort

# ── 3b. Clerk publishable key (secret — Expo dashboard / `eas env`) ─────────
step "3b. Clerk key (shell proxy for the EAS secret)"

# The Clerk publishable key is intentionally NOT committed in eas.json —
# it's a per-deploy credential set as an EAS environment variable
# ('eas env:create --environment production --name
# EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY'). We can't read the Expo dashboard
# from here, so we use the shell as a proxy: if it's set locally you
# almost certainly set the EAS env var too. Bypass with
# SKIP_CLERK_SHELL_CHECK=1 if you manage it purely via the dashboard.
clerk_key="${EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY:-}"
if [ -n "${SKIP_CLERK_SHELL_CHECK:-}" ]; then
  printf "  \033[2mskipped (SKIP_CLERK_SHELL_CHECK=1) — ensure it's set as an EAS env var\033[0m\n"
elif [ -z "$clerk_key" ]; then
  fail "EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY not in shell — set it as an EAS env var ('eas env:create --environment production --name EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY') and export it locally, or pass SKIP_CLERK_SHELL_CHECK=1 if it's already in the dashboard"
elif [[ "$clerk_key" == pk_test_* ]]; then
  fail "EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY is a pk_test_ key — release builds need pk_live_"
elif [[ "$clerk_key" == pk_live_* ]]; then
  pass "EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY is a pk_live_ key (length ${#clerk_key})"
else
  pass "EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY set (length ${#clerk_key})"
fi

[ "$FAIL" -eq 0 ] || abort

# ── 4. Backend reachable from outside ────────────────────────────────────────
# Probe the URL the production build will actually ship with (from
# eas.json, parsed in step 3) — not the shell's EXPO_PUBLIC_API_URL,
# which may differ from the release profile. If the custom domain isn't
# live yet (OAI #5/#6), pass SKIP_LIVE_API_PROBE=1 deliberately.
step "4. Backend reachable at production EXPO_PUBLIC_API_URL"
if [ -n "${SKIP_LIVE_API_PROBE:-}" ]; then
  printf "  \033[2mskipped (SKIP_LIVE_API_PROBE=1)\033[0m\n"
else
  url="${eas_url%/}/health"
  health_status=$(curl -sS --max-time 10 -o /dev/null -w "%{http_code}" "$url" 2>/dev/null || echo "000")
  if [ "$health_status" = "200" ]; then
    pass "GET $url → 200"
  else
    fail "GET $url → HTTP $health_status — TestFlight build will be unable to reach the backend"
  fi
fi

# ── 5. Contract drift + API coverage ─────────────────────────────────────────
step "5. API surface integrity"
if "$WORKSPACE_DIR/scripts/contract-check.sh" >/dev/null 2>&1; then
  pass "OpenAPI snapshot ↔ generated types in sync"
else
  fail "contract-check failed — run scripts/sync-types.sh and re-commit docs/openapi.json"
fi

if python3 "$WORKSPACE_DIR/scripts/api-coverage-check.py" >/dev/null 2>&1; then
  pass "All http.ts URLs exist in docs/openapi.json"
else
  fail "api-coverage-check failed — http.ts is calling routes not in the OpenAPI snapshot"
fi

# ── 6. Frontend type + lint + tests ──────────────────────────────────────────
step "6. Frontend type check"
if (cd "$APP_DIR" && npx tsc --noEmit) >/dev/null 2>&1; then
  pass "tsc --noEmit clean"
else
  fail "tsc --noEmit failed — fix type errors before building"
fi

step "7. Frontend offline tests"
if [ -n "${SKIP_TESTS:-}" ]; then
  printf "  \033[2mskipped (SKIP_TESTS=1)\033[0m\n"
else
  if (cd "$APP_DIR" && npm run test:offline) >/dev/null 2>&1; then
    pass "frontend offline tests pass"
  else
    fail "frontend offline tests failed — re-run 'npm run test:offline' from travel-app/ to see details"
  fi
fi

# ── 7. Backend offline tests (final sanity) ──────────────────────────────────
step "8. Backend offline tests"
if [ -n "${SKIP_BACKEND_TESTS:-}" ]; then
  printf "  \033[2mskipped (SKIP_BACKEND_TESTS=1)\033[0m\n"
else
  if (cd "$AGENT_DIR" && PYTHONPATH=. pytest tests/ -q -k "not requires_postgres and not requires_api_keys") >/dev/null 2>&1; then
    pass "backend offline pytest pass"
  else
    fail "backend offline tests failed — re-run 'make test-backend' to see details"
  fi
fi

# ── Summary ──────────────────────────────────────────────────────────────────
step "Summary"
printf "  passed: %d · failed: %d\n" "$PASS" "$FAIL"

if [ "$FAIL" -eq 0 ]; then
  printf "\n\033[32mPre-flight green.\033[0m You can now run:\n"
  printf "  cd \"%s\" && eas build --platform ios --profile production\n" "$APP_DIR"
  printf "Then submit to TestFlight from App Store Connect when the build finishes.\n"
  exit 0
else
  abort
fi
