#!/usr/bin/env bash
# Emit a paste-ready ``fly secrets set`` block for first-time deploy.
#
# Reads ``travel-agent/.env.example`` and prints one ``fly secrets set``
# invocation per category, with placeholder values. Pipe to a file,
# fill in real values, then paste each block into your terminal.
#
# Why not generate one giant ``fly secrets set`` command? Fly redeploys
# the app on each ``fly secrets set`` invocation. Batching by category
# keeps redeploys to a handful instead of one-per-key, while still
# letting you commit credentials in logical groups (e.g. set the LLM
# keys, verify, then move on to Clerk).
#
# Usage:
#   ./scripts/fly-secrets-template.sh > /tmp/fly-secrets.sh
#   $EDITOR /tmp/fly-secrets.sh        # fill in <REPLACE_*> placeholders
#   bash /tmp/fly-secrets.sh           # run each fly secrets set block
#
# Or pipe a subset:
#   ./scripts/fly-secrets-template.sh required
#   ./scripts/fly-secrets-template.sh production-toggles

set -uo pipefail

# What category to emit. "all" (default) prints every category in order.
WHICH="${1:-all}"

emit_section() {
  local title="$1"
  shift
  # The output is meant to be pasted into a shell. Each ``fly secrets
  # set`` is one redeploy, so we put each KEY=VALUE on its own line
  # with a real backslash + newline. Values are single-quoted because
  # placeholders often contain ``<…>`` which bash would otherwise treat
  # as redirection (a real ``bash -n`` syntax error on the template).
  # The LAST KEY=VALUE has no trailing ``\`` — shell backslash-
  # continuation would otherwise consume the next blank/comment line
  # as an additional argument to ``fly secrets set``.
  printf '# === %s ===\n' "$title"
  printf '%b' 'fly secrets set \\\n'
  local n=$#
  local i=0
  local var
  for var in "$@"; do
    i=$((i + 1))
    if [ "$i" -lt "$n" ]; then
      printf '%b' "  ${var%%=*}='${var#*=}' \\\\\n"
    else
      printf "  %s='%s'\n" "${var%%=*}" "${var#*=}"
    fi
  done
  printf '\n'
}

want() {
  [ "$WHICH" = "all" ] || [ "$WHICH" = "$1" ]
}

cat <<'HEADER'
#!/usr/bin/env bash
# Paste-ready ``fly secrets set`` template — first-time deploy.
#
# Each block redeploys the app once. To skip a category, comment its
# block out. To dry-run, prepend ``echo``:
#   echo fly secrets set ANTHROPIC_API_KEY=... \
#        ...
#
# Required: ANTHROPIC, Auth, Production toggles, Apple Universal Links,
#   and infra (Postgres + Qdrant + Redis). The app is non-functional
#   without Postgres/Qdrant, and the arq worker process needs Redis —
#   so `required` now includes them (matches the "Minimum" list in
#   travel-agent/fly.toml).
# Optional: research keys, push, transactional email/SMS.

set -euo pipefail
HEADER

printf "\n"

if want required || want llm; then
  emit_section "LLM (required)" \
    "ANTHROPIC_API_KEY=<REPLACE_ANTHROPIC_KEY>"
fi

if want required || want auth; then
  emit_section "Authentication (Clerk — required for production)" \
    "SKIP_AUTH=false" \
    "CLERK_JWKS_URL=https://<your-instance>.clerk.accounts.dev/.well-known/jwks.json" \
    "CLERK_ISSUER=https://<your-instance>.clerk.accounts.dev"
fi

if want required || want production-toggles; then
  emit_section "Production toggles (flip dev defaults — caught by _validate_startup)" \
    "ENVIRONMENT=production" \
    "BOOKING_AMADEUS_SANDBOX=false" \
    "BOOKING_DUFFEL_SANDBOX=false" \
    "LANGFUSE_CAPTURE_USER_CONTENT=false" \
    "TRACE_CAPTURE_USER_CONTENT=false" \
    "CONCIERGE_OUTPUT_GUARD_MODE=log"
fi

if want required || want apple; then
  emit_section "Apple Universal Links (required for invite deep-link)" \
    "INVITE_APPLE_TEAM_ID=<10-char Team ID from developer.apple.com Account>" \
    "INVITE_APPLE_BUNDLE_ID=com.travelagent.app" \
    "INVITE_IOS_APP_STORE_ID=<numeric App Store ID after first listing>" \
    "INVITE_APP_STORE_URL=https://apps.apple.com/app/id<APP_STORE_ID>"
fi

if want required || want infra; then
  emit_section "Postgres (required — external Neon/Supabase/Fly Postgres)" \
    "DATABASE_URL=postgres://<user>:<pass>@<host>:5432/<db>?sslmode=require"

  emit_section "Redis (required for the arq worker — Upstash via fly extensions create upstash-redis)" \
    "REDIS_URL=redis://<host>:<port>"

  emit_section "Qdrant (required — Qdrant Cloud free tier)" \
    "QDRANT_URL=https://<cluster>.qdrant.cloud:6333" \
    "QDRANT_API_KEY=<REPLACE_QDRANT_KEY>"
fi

if want research; then
  emit_section "Research + content keys (optional — graceful degradation if unset)" \
    "TAVILY_API_KEY=tvly-<REPLACE>" \
    "GOOGLE_PLACES_API_KEY=AIza<REPLACE>" \
    "PLACES_FOURSQUARE_API_KEY=<REPLACE>" \
    "RESEARCH_TICKETMASTER_API_KEY=<REPLACE>" \
    "RESEARCH_TRIPADVISOR_API_KEY=<REPLACE>"
fi

if want booking; then
  emit_section "Booking provider keys (required only for real-money inventory)" \
    "BOOKING_AMADEUS_API_KEY=<REPLACE>" \
    "BOOKING_AMADEUS_API_SECRET=<REPLACE>" \
    "BOOKING_DUFFEL_API_KEY=<REPLACE>" \
    "BOOKING_VIATOR_API_KEY=<REPLACE>" \
    "BOOKING_VIATOR_PARTNER_ID=<REPLACE>" \
    "BOOKING_VIATOR_MCID=<REPLACE>"
fi

if want observability; then
  emit_section "Observability (Langfuse — silently no-op if unset)" \
    "LANGFUSE_PUBLIC_KEY=pk-lf-<REPLACE>" \
    "LANGFUSE_SECRET_KEY=sk-lf-<REPLACE>"
fi

if want push; then
  emit_section "Expo push (required for real-device notifications)" \
    "EXPO_ACCESS_TOKEN=<from expo.dev → Account → Access Tokens>" \
    "EXPO_PUSH_ENABLED=true"
fi

if want messaging; then
  emit_section "Transactional messaging (SendGrid + Twilio — for invite delivery)" \
    "SENDGRID_API_KEY=SG.<REPLACE>" \
    "SENDGRID_FROM_EMAIL=invites@travelagent.app" \
    "SENDGRID_FROM_NAME=Vesper" \
    "TWILIO_ACCOUNT_SID=AC<REPLACE>" \
    "TWILIO_AUTH_TOKEN=<REPLACE>" \
    "TWILIO_FROM_NUMBER=+1<REPLACE>"
fi

cat <<'FOOTER'

# ── After all secrets are set ───────────────────────────────────────────────
# 1. Verify with: fly secrets list
# 2. Deploy:      fly deploy
# 3. Tail logs:   fly logs
# 4. Smoke:       PRELAUNCH_HOST=https://<app>.fly.dev SMOKE_VERIFY_AUTH=1 \
#                   PRELAUNCH_JWT=<test JWT> make smoke
FOOTER
