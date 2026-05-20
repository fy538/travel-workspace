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
#
# Extra deploy-verification steps (off by default — opt in once the
# corresponding piece of infra is in place):
#   SMOKE_VERIFY_AUTH=1        — confirm /api/me returns 401 without JWT
#                                and 200 with JWT (proves Clerk JWKS is
#                                wired and SKIP_AUTH is false). Requires
#                                PRELAUNCH_JWT to be set.
#   SMOKE_VERIFY_APPLE_CDN=1   — fetch the AASA via Apple's external CDN
#                                (app-site-association.cdn-apple.com) and
#                                verify it matches the host-served copy.
#                                Apple's CDN re-caches every ~24h; this
#                                proves Universal Links will resolve for
#                                a real device. PRELAUNCH_HOST must be
#                                an https://… domain (not localhost).
#   SMOKE_VERIFY_WORKER=1      — GET /health/external and assert Redis is
#                                reachable (the arq worker's job intake).
#                                Catches the "API green but background
#                                jobs dead" deploy. Also surfaces the
#                                Anthropic / Tavily provider probes.
#   SMOKE_VERIFY_CONCIERGE=1   — exercise the core product flow: POST a
#                                real message to
#                                /api/trips/{id}/messages/stream and
#                                assert an SSE reply streams back. Runs a
#                                real LLM turn (costs tokens, needs
#                                ANTHROPIC_API_KEY on the backend) — opt
#                                in only. Reuses the trip from step 4.

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
  host_aasa_body=""
  if aasa=$(_request GET /.well-known/apple-app-site-association ""); then
    body="${aasa%$'\n'*}"
    status="${aasa##*$'\n'}"
    if [[ "$status" =~ ^2[0-9][0-9]$ ]]; then
      pass "AASA served ($status)"
      host_aasa_body="$body"
      if printf "%s" "$body" | python3 -c "import json,sys; d=json.load(sys.stdin); apps=d.get('applinks',{}).get('details',[]); sys.exit(0 if apps and apps[0].get('appID','').count('.')>=1 and not apps[0]['appID'].startswith('REPLACE') else 1)" 2>/dev/null; then
        pass "AASA appID set (Team ID + bundle present)"
      else
        fail "AASA returned but appID looks like REPLACE_ME or is malformed"
      fi
    else
      fail "AASA path returned HTTP $status — Universal Links won't validate"
    fi
  fi

  # 2b. Optional: cross-check via Apple's external CDN. Apple re-fetches
  # the AASA every ~24h and caches it. A real iOS device validates
  # Universal Links against the CDN copy, not the origin — if the CDN
  # has a stale REPLACE_ME copy (e.g. a previous bad deploy), Universal
  # Links break even after the origin is fixed. Requires an https domain.
  if [ -n "${SMOKE_VERIFY_APPLE_CDN:-}" ]; then
    apple_host="${HOST#https://}"
    apple_host="${apple_host#http://}"
    apple_host="${apple_host%%/*}"
    if [[ "$HOST" != https://* ]] || [[ "$apple_host" == localhost* ]] || [[ "$apple_host" == 127.0.0.1* ]]; then
      printf "  \033[2mApple CDN check skipped — HOST must be an https://… public domain\033[0m\n" >&2
    else
      cdn_url="https://app-site-association.cdn-apple.com/a/v1/$apple_host"
      if cdn_resp=$(curl -sS --max-time "$TIMEOUT" -w "\n%{http_code}" "$cdn_url" 2>&1); then
        cdn_body="${cdn_resp%$'\n'*}"
        cdn_status="${cdn_resp##*$'\n'}"
        if [[ "$cdn_status" =~ ^2[0-9][0-9]$ ]]; then
          pass "Apple CDN AASA fetched ($cdn_status)"
          if [ -n "$host_aasa_body" ]; then
            host_appid=$(printf "%s" "$host_aasa_body" | python3 -c "import json,sys; d=json.load(sys.stdin); apps=d.get('applinks',{}).get('details',[]); print(apps[0].get('appID','') if apps else '')" 2>/dev/null)
            cdn_appid=$(printf "%s" "$cdn_body" | python3 -c "import json,sys; d=json.load(sys.stdin); apps=d.get('applinks',{}).get('details',[]); print(apps[0].get('appID','') if apps else '')" 2>/dev/null)
            if [ -n "$host_appid" ] && [ "$host_appid" = "$cdn_appid" ]; then
              pass "Apple CDN appID matches origin ($cdn_appid)"
            else
              fail "Apple CDN appID ($cdn_appid) differs from origin ($host_appid) — CDN cache is stale"
            fi
          fi
        else
          fail "Apple CDN returned HTTP $cdn_status — first cache may not be populated yet (wait ~24h after first deploy)"
        fi
      else
        fail "Apple CDN curl failed: ${cdn_resp:0:200}"
      fi
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

# 3b. Optional: prove Clerk JWT validation is actually wired. The
# default smoke is permissive enough to work with SKIP_AUTH=true in dev,
# but in production we want both directions:
#   - GET /api/me WITHOUT bearer → must return 401 (auth required)
#   - GET /api/me WITH bearer    → must return 200 (JWT validates)
# Requires both PRELAUNCH_JWT to be set.
if [ -n "${SMOKE_VERIFY_AUTH:-}" ]; then
  step "3b. Clerk JWT round-trip"
  if [ -z "$JWT" ]; then
    fail "SMOKE_VERIFY_AUTH=1 set but PRELAUNCH_JWT is empty — cannot verify the authenticated leg"
  else
    unauth_resp=$(curl -sS --max-time "$TIMEOUT" -o /dev/null -w "%{http_code}" "$HOST/api/me" 2>&1)
    if [ "$unauth_resp" = "401" ]; then
      pass "/api/me without bearer → 401 (auth gate is live)"
    elif [ "$unauth_resp" = "200" ]; then
      fail "/api/me without bearer → 200 — backend is in SKIP_AUTH mode or auth is bypassed"
    else
      fail "/api/me without bearer → HTTP $unauth_resp (expected 401)"
    fi
    # Re-run /api/me WITH the bearer to prove the bearer leg, distinct
    # from step 3 (which may have passed via SKIP_AUTH dev mode).
    auth_resp=$(curl -sS --max-time "$TIMEOUT" -o /dev/null -w "%{http_code}" \
      -H "Authorization: Bearer $JWT" "$HOST/api/me" 2>&1)
    if [ "$auth_resp" = "200" ]; then
      pass "/api/me with bearer → 200 (JWKS validates the JWT)"
    else
      fail "/api/me with bearer → HTTP $auth_resp (expected 200; JWKS may not be configured or the JWT is expired)"
    fi
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

# 5. Background-job dependencies (opt-in). /health/external is the
# monitoring surface for the arq worker's deps — Redis especially, since
# /ready deliberately doesn't gate on it. This catches the "API deploy
# is green but the worker can't consume jobs" failure that otherwise
# ships silently.
if [ -n "${SMOKE_VERIFY_WORKER:-}" ]; then
  step "5. Background dependencies (/health/external)"
  ext_resp=$(_request GET /health/external "")
  ext_body="${ext_resp%$'\n'*}"
  ext_status="${ext_resp##*$'\n'}"
  if [[ "$ext_status" =~ ^2[0-9][0-9]$ ]]; then
    redis_state=$(printf "%s" "$ext_body" | python3 -c "import json,sys; print(json.load(sys.stdin).get('checks',{}).get('redis','(missing)'))" 2>/dev/null)
    case "$redis_state" in
      ok)
        pass "redis reachable — arq worker can consume jobs"
        ;;
      skipped*)
        fail "redis skipped — REDIS_URL is unset on the backend; audio prerender, digests, and pre-trip jobs will NOT run"
        ;;
      *)
        fail "redis unhealthy ($redis_state) — arq worker cannot consume jobs"
        ;;
    esac
    # Surface (but don't fail the smoke on) the LLM/search provider probes.
    for dep in anthropic tavily; do
      dep_state=$(printf "%s" "$ext_body" | python3 -c "import json,sys; print(json.load(sys.stdin).get('checks',{}).get('$dep','(missing)'))" 2>/dev/null)
      case "$dep_state" in
        ok) pass "$dep reachable" ;;
        skipped*) printf "  \033[2m· %s %s\033[0m\n" "$dep" "$dep_state" >&2 ;;
        *) fail "$dep unhealthy ($dep_state)" ;;
      esac
    done
  else
    fail "GET /health/external → HTTP $ext_status"
  fi
fi

# 6. Concierge turn — the actual product flow (opt-in; runs a real LLM
# turn so it costs tokens and needs ANTHROPIC_API_KEY on the backend).
# Reuses the trip created in step 4. POSTs a message to the SSE endpoint
# and asserts a reply streams back without an error event.
if [ -n "${SMOKE_VERIFY_CONCIERGE:-}" ]; then
  step "6. Concierge turn (SSE)"
  if [ -z "${user_id:-}" ]; then
    fail "SMOKE_VERIFY_CONCIERGE=1 but no user_id (step 3 failed or was skipped)"
  elif [ -z "${trip_id:-}" ]; then
    fail "SMOKE_VERIFY_CONCIERGE=1 but no trip_id (step 4 was skipped — unset SKIP_TRIP_CRUD)"
  else
    msg_body='{"user_id":"'"$user_id"'","user_name":"Smoke Test","message":"Hi! In one sentence, what can you help me with?","modality":"text"}'
    sse_args=(-sS -N --max-time 60 -X POST -H "Content-Type: application/json")
    if [ -n "$JWT" ]; then
      sse_args+=(-H "Authorization: Bearer $JWT")
    fi
    sse_args+=(--data "$msg_body")
    sse_out=$(curl "${sse_args[@]}" "$HOST/api/trips/$trip_id/messages/stream" 2>&1)
    if printf "%s" "$sse_out" | grep -q "^event: error"; then
      err_line=$(printf "%s" "$sse_out" | grep -A1 "^event: error" | grep "^data:" | head -1)
      fail "concierge stream returned an error event: ${err_line:0:200}"
    elif printf "%s" "$sse_out" | grep -qE "^event: (text_delta|metadata)"; then
      deltas=$(printf "%s" "$sse_out" | grep -c "^event: text_delta")
      pass "concierge streamed a reply ($deltas text_delta events; terminal metadata present)"
    else
      fail "concierge stream produced no text_delta/metadata events: ${sse_out:0:200}"
    fi
  fi
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
