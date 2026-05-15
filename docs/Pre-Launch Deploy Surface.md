# Pre-Launch Deploy Surface

**Audit date:** 2026-05-15 · **Repos:** Travel Agent + Travel App · **Total secrets/env vars scanned:** ~80

What this document is: every secret, environment variable, third-party key, and signed-URL TTL the running app touches, classified by deploy-time risk. Use this as a pre-TestFlight checklist.

Status legend:
- 🟢 documented in `.env.example`, scoped appropriately, no action needed
- 🟡 used in code, default-safe, *but* rotation policy or doc could be clearer
- 🟠 will work in production but creates ambiguity or fails silently in some configs — fix before user testing
- 🔴 will break in a fresh production deployment or constitutes a real leak risk — fix before TestFlight

---

## 🔴 Critical items (fix before TestFlight)

### 1. R2 storage config not in `.env.example`
**Where:** [Travel Agent/backend/core/audio_storage.py:202-256](Travel Agent/backend/core/audio_storage.py)
**What:** the audio storage module reads `R2_ENABLED`, `R2_ACCOUNT_ID`, `R2_BUCKET_NAME`, `R2_CDN_BASE_URL`, `R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY` but none of these appear in `Travel Agent/.env.example`.
**Impact:** a fresh deploy that enables R2 will silently fail to configure storage — narration audio + uploads break with no clear error.
**Fix:** add an `# ── Audio Storage (Cloudflare R2) ──` section to `.env.example` documenting all 6 vars + that `R2_ENABLED=false` is the safe default.
**Verify:** `grep R2_ Travel\ Agent/.env.example | wc -l` returns 6.

### 2. `EXPO_PUBLIC_CONTENT_GRAPH_GEOFENCE` not in frontend `.env.example`
**Where:** [Travel App/utils/api/index.ts:30](Travel App/utils/api/index.ts)
**What:** frontend toggle read but not documented. Backend has the matching `CONTENT_GRAPH_GEOFENCE_ENABLED` and that one IS also undocumented.
**Impact:** developers don't know the toggle exists; QA can't reproduce the feature without spelunking source.
**Fix:** add to `Travel App/.env.example` AND `Travel Agent/.env.example` under a "Feature flags" section.
**Verify:** `grep CONTENT_GRAPH_GEOFENCE Travel\ App/.env.example Travel\ Agent/.env.example` returns 2 lines.

### 3. Live API keys present in local `.env`
**Where:** `Travel Agent/.env` (file is gitignored — not in any repo).
**What:** ANTHROPIC_API_KEY and TAVILY_API_KEY are real, working keys that have been on the dev machine for the duration of the project.
**Impact:** these keys *are not* leaked publicly, but anything that has touched the dev machine (cloud sync, recent backups, time-machine snapshots, clipboard history, shared screen recordings) has them. Standard hygiene says rotate before handing TestFlight builds (or backend access) to anyone else.
**Fix:** generate fresh keys, replace in `.env`, revoke the old ones in each provider's dashboard.
**Verify:** Anthropic and Tavily dashboards show the previous key as "revoked".

---

## 🟠 Moderate (fix before public traffic)

### 4. `REDIS_URL` is silently optional
**Where:** [Travel Agent/backend/core/job_queue.py:106](Travel Agent/backend/core/job_queue.py)
**What:** Redis backs the arq job queue used for audio jobs, digest scheduling, and background pre-trip work. Missing `REDIS_URL` doesn't error — those features just don't run.
**Fix:** mark `REDIS_URL` as required in `.env.example` (`# Required for production: audio jobs, digests, pre-trip`). Add a startup check that warns when `REDIS_URL` is unset AND `DISABLE_LLM_BACKGROUND_LOOPS=false`.
**Verify:** booting with no `REDIS_URL` and `DISABLE_LLM_BACKGROUND_LOOPS=false` logs a clear warning.

### 5. `SKIP_AUTH=false` + missing `CLERK_JWKS_URL` fails silently
**Where:** [Travel Agent/backend/api/auth.py:36-42](Travel Agent/backend/api/auth.py)
**What:** if `SKIP_AUTH=false` (the production setting) and `CLERK_JWKS_URL` is empty, JWT validation can't happen. Today the code path's behavior depends on what `clerk-backend-api` does with an empty URL — likely fails on first request, not at boot.
**Fix:** add an explicit startup check: `if not skip_auth and not clerk_jwks_url: raise RuntimeError(...)`. This converts a runtime 500 into a fast-fail boot error.
**Verify:** booting with `SKIP_AUTH=false` and `CLERK_JWKS_URL=` exits with a non-zero code and a clear message.

### 6. Booking sandbox defaults are safe but un-toggled
**Where:** [Travel Agent/backend/booking_agent/config/settings.py:10,14](Travel Agent/backend/booking_agent/config/settings.py)
**What:** `BOOKING_AMADEUS_SANDBOX=true` and `BOOKING_DUFFEL_SANDBOX=true` are safe defaults but production deploys MUST flip them. Currently no documented mechanism makes that visible.
**Fix:** add a "Production toggles" section to `.env.example` listing every flag that defaults to dev-safe but must change in prod. Reference this section in the OAI checklist for item #4 (`eas build` production).
**Verify:** ops can grep `.env.example` for "PRODUCTION:" and see the full list.

### 7. `INVITE_APPLE_TEAM_ID` still `REPLACE_ME`
**Where:** `Travel Agent/.env` (gitignored, dev only)
**What:** Universal Links won't work in any build until this is real. Already tracked in Owner Action Items #1.
**Fix:** see OAI #1.

---

## 🟡 Hygiene (track but not blocking)

### 8. Rotation policy undocumented for ~5 third-party keys
**Where:** TAVILY_API_KEY, RESEARCH_TRIPADVISOR_API_KEY, RESEARCH_FOURSQUARE_API_KEY, RESEARCH_VIATOR_API_KEY, RESEARCH_TICKETMASTER_API_KEY.
**What:** no comment in code or docs about expected rotation cadence.
**Fix:** add a `## Key rotation schedule` section to this doc once you decide a policy. Annual is conventional; quarterly is paranoid; never is the current de-facto policy.

### 9. `LLM_VCR_*` not in `.env.example`
**Where:** [Travel Agent/backend/core/llm_vcr.py:79-252](Travel Agent/backend/core/llm_vcr.py)
**What:** test-only env vars that control cassette recording. Acceptable to leave out of `.env.example` — they're CI/eval concerns, not deploy.
**Fix:** none, but mention in `tools/eval/` README if the eval docs aren't already covering them.

### 10. `CONCIERGE_OUTPUT_GUARD_MODE` not in `.env.example`
**Where:** [Travel Agent/backend/concierge/output_guards.py:59](Travel Agent/backend/concierge/output_guards.py)
**What:** the guard mode flag introduced in `Travel Agent/CLAUDE.md`. Default is `log` which is the right pre-launch setting.
**Fix:** add to `.env.example` with the full mode table from `CLAUDE.md` so ops can see it without grepping.

---

## TTLs and signed URLs (informational)

| Resource | TTL | Configurable | Notes |
|---|---|---|---|
| Anthropic prompt cache | 5 min default, 1h ephemeral | Per-call | Standard SDK behavior |
| Clerk JWT session | Clerk default | Clerk dashboard | Not overridden in code |
| Invite tokens | **14 days, hardcoded** | No | [TripInvite.expires_in_days](Travel Agent/backend/core/db/_tables/trip_invites.py) — if invite reuse becomes a problem, parameterize |
| Amadeus OAuth | Auto-refresh 60s before expiry | Auto | [backend/core/oauth.py:64](Travel Agent/backend/core/oauth.py:64) |
| Booking offer expiration | 60s configurable | `offer_expiry_check_interval_seconds` | Fine |

---

## Action summary

The actions below are the consolidated TODO from this audit. Each is small.

- [ ] **#1 / #2:** add R2 + content-graph-geofence to both `.env.example` files
- [ ] **#3:** rotate Anthropic + Tavily keys, revoke old ones
- [ ] **#4:** mark `REDIS_URL` required + add startup warning
- [ ] **#5:** add `if not skip_auth and not clerk_jwks_url: raise` to backend boot
- [ ] **#6:** add "Production toggles" section to `.env.example`
- [ ] **#10:** add `CONCIERGE_OUTPUT_GUARD_MODE` to `.env.example` with mode table

Estimated total time to complete all 6 items: **30-45 minutes**. None require external accounts; they're code/config changes only.

After this, the gating items are the calendar tasks in `docs/Owner Action Items.md` (Apple Team ID, EAS init, domain, SSL, Clerk app, APNs key).
