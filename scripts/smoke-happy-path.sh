#!/usr/bin/env bash
# Smoke test the happy path against a Travel Agent backend.
#
# Drives the canonical user flow:
#   1. /health, /ready, /openapi.json — basic up/serving/DB
#   2. /.well-known/apple-app-site-association — AASA serving + Team ID set
#   3. GET /api/me — auth path (or dev-mode bypass)
#   4. POST /api/trips → GET /api/trips/{id} — trip CRUD
#
# Each step prints ✓ or ✗ with the failure detail and exits non-zero on
# the first failure. No cleanup — POST /api/trips creates a residual
# row. Acceptable for localhost; track on the prod target.
#
# Usage:
#   ./scripts/smoke-happy-path.sh                          # http://localhost:8000 (no auth)
#   PRELAUNCH_HOST=https://travelagent.app ./scripts/smoke-happy-path.sh
#   PRELAUNCH_JWT=<token> PRELAUNCH_HOST=https://... ./scripts/smoke-happy-path.sh
#
# Skip individual steps via env: SKIP_AASA=1, SKIP_TRIP_CRUD=1, etc.

set -uo pipefail

HOST="${PRELAUNCH_HOST:-http://localhost:8000}"
JWT="${PRELAUNCH_JWT:-}"
TIMEOUT="${PRELAUNCH_TIMEOUT:-10}"

PASS=0
FAIL=0
FIRST_FAIL=""

# All status output goes to stderr so callers can pipe response bodies
# from ``_check`` into JSON tooling without "✓..." prefix corruption.
pass() {
  printf "  \033[32m✓\033[0m %s\n" "$1" >&2
  PASS=$((PASS + 1))
}

fail() {
  printf "  \033[31m✗\033[0m %s\n" "$1" >&2
  FAIL=$((FAIL + 1))
  if [ -z "$FIRST_FAIL" ]; then
    FIRST_FAIL="$1"
  fi
}

step() {
  printf "\n\033[1m== %s ==\033[0m\n" "$1" >&2
}

# Common curl wrapper. Returns body on stdout, status on fd 3.
_request() {
  local method="$1"
  local path="$2"
  local body="${3:-}"
  local args=(-sS --max-time "$TIMEOUT" -X "$method" -w "\n%{http_code}")
  if [ -n "$JWT" ]; then
    args+=(-H "Authorization: Bearer $JWT")
  fi
  args+=(-H "Content-Type: application/json")
  if [ -n "$body" ]; then
    args+=(--data "$body")
  fi
  curl "${args[@]}" "$HOST$path"
}

# Returns 0 if HTTP status is 2xx, prints body on stdout.
_check() {
  local description="$1"
  local method="$2"
  local path="$3"
  local body="${4:-}"
  local out status
  out=$(_request "$method" "$path" "$body" 2>&1) || {
    fail "$description — curl failed: $out"
    return 1
  }
  status="${out##*$'\n'}"
  out="${out%$'\n'*}"
  if [[ "$status" =~ ^2[0-9][0-9]$ ]]; then
    pass "$description ($status)"
    printf "%s" "$out"
    return 0
  else
    fail "$description — got HTTP $status: ${out:0:200}"
    return 1
  fi
}

printf "\033[1mSmoke happy-path against:\033[0m %s\n" "$HOST" >&2
if [ -n "$JWT" ]; then
  printf "  auth: bearer token (length %d)\n" "${#JWT}" >&2
else
  printf "  auth: none (assumes SKIP_AUTH=true on backend)\n" >&2
fi
printf "  timeout per request: %ss\n" "$TIMEOUT" >&2

# 1. Basic liveness
step "1. Liveness"
_check "GET /health"     GET /health          > /dev/null
_check "GET /ready"      GET /ready           > /dev/null
_check "GET /openapi.json — backend exposes spec" GET /openapi.json > /tmp/_smoke_openapi.json
if [ -s /tmp/_smoke_openapi.json ]; then
  if python3 -c "import json,sys; d=json.load(open('/tmp/_smoke_openapi.json')); sys.exit(0 if d.get('paths') else 1)" 2>/dev/null; then
    pass "openapi.json parses + has paths"
  else
    fail "openapi.json malformed or empty paths"
  fi
fi

# 2. Universal Links / AASA (skip in dev mode)
if [ -z "${SKIP_AASA:-}" ]; then
  step "2. AASA (Universal Links)"
  if aasa=$(_request GET /.well-known/apple-app-site-association ""); then
    body="${aasa%$'\n'*}"
    status="${aasa##*$'\n'}"
    if [[ "$status" =~ ^2[0-9][0-9]$ ]]; then
      pass "AASA served ($status)"
      if printf "%s" "$body" | python3 -c "import json,sys; d=json.load(sys.stdin); apps=d.get('applinks',{}).get('details',[]); sys.exit(0 if apps and apps[0].get('appID','').count('.')>=1 and not apps[0]['appID'].startswith('REPLACE') else 1)" 2>/dev/null; then
        pass "AASA appID set (Team ID + bundle present)"
      else
        fail "AASA returned but appID looks like REPLACE_ME or is malformed"
      fi
    else
      fail "AASA path returned HTTP $status — Universal Links won't validate"
    fi
  fi
fi

# 3. Auth path
step "3. Auth surface"
_check "GET /api/me — auth path resolves" GET /api/me > /tmp/_smoke_me.json
if [ -s /tmp/_smoke_me.json ]; then
  user_id=$(python3 -c "import json; d=json.load(open('/tmp/_smoke_me.json')); print(d.get('id') or d.get('user_id') or '')" 2>/dev/null)
  if [ -n "$user_id" ]; then
    pass "/api/me returned a user_id ($user_id)"
  else
    fail "/api/me returned but has no id field"
  fi
fi

# 4. Trip CRUD
if [ -z "${SKIP_TRIP_CRUD:-}" ] && [ -n "${user_id:-}" ]; then
  step "4. Trip CRUD"
  trip_body='{"created_by":"'"$user_id"'","title":"smoke test trip"}'
  trip_resp=$(_check "POST /api/trips — create" POST /api/trips "$trip_body")
  if [ -n "$trip_resp" ]; then
    trip_id=$(printf "%s" "$trip_resp" | python3 -c "import json,sys; print(json.load(sys.stdin).get('id',''))" 2>/dev/null)
    if [ -n "$trip_id" ]; then
      pass "trip created (id=$trip_id)"
      _check "GET /api/trips/$trip_id — read back" GET "/api/trips/$trip_id" > /tmp/_smoke_trip_get.json
      if python3 -c "import json; d=json.load(open('/tmp/_smoke_trip_get.json')); assert d.get('title')=='smoke test trip'" 2>/dev/null; then
        pass "round-trip data matches"
      else
        fail "GET trip returned but title doesn't match what we POSTed"
      fi
    else
      fail "POST trip succeeded but response missing 'id'"
    fi
  fi
elif [ -n "${SKIP_TRIP_CRUD:-}" ]; then
  step "4. Trip CRUD"
  printf "  \033[2mskipped (SKIP_TRIP_CRUD=1)\033[0m\n" >&2
fi

# Summary
step "Summary"
printf "  passed: %d · failed: %d\n" "$PASS" "$FAIL" >&2
if [ "$FAIL" -eq 0 ]; then
  printf "\033[32mAll smoke checks passed.\033[0m\n" >&2
  exit 0
else
  printf "\033[31mSmoke checks failed.\033[0m First failure: %s\n" "$FIRST_FAIL" >&2
  exit 1
fi
