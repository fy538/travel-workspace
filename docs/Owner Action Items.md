# Owner Action Items

Single source of truth for everything that requires a human decision, account access, or calendar time. Code tasks live in GitHub issues; this file is the owner-only punch list.

**Last updated:** 2026-05-22

**Status legend:** 🔴 do now · 🟠 before TestFlight · 🟡 before public launch · ✅ done

**Reference docs (don't need to read unless you want the detail):**
- `docs/Pre-Launch Deploy Surface.md` — full secret/env-var security audit
- `docs/Deploy & Rollback Runbook.md` — ops procedures
- `docs/TestFlight Tester Onboarding.md` — tester copy, welcome email
- `docs/App Store Connect Copy.md` — listing text
- `docs/Apple Review Notes.md` — review guidance

---

## Where we are right now

```
Backend:   ✅ LIVE at https://vesper-backend.fly.dev
           /health → ok  /ready (Postgres + Qdrant) → ok
           /health/external (Anthropic + Tavily + Redis) → ok
           19/19 background tasks running  •  arq worker connected

Custom domain:  ✗  travelagent.app not yet pointed at Fly
TestFlight:     ✗  no production build yet
Clerk:          ✓  configured  (CLERK_JWKS_URL set in Fly secrets)
```

---

## Phase 1 — Platform & accounts (pre-TestFlight)

Roughly sequential. Most items take < 30 min of actual work; calendar time is dominated by Apple propagation and DNS TTLs.

---

### A0 — Install secret-prefix pre-commit hook 🔴

**Time est:** 5 min  
**Why:** The built-in `detect-secrets` hook covers AWS/Stripe/GitHub/Slack/Twilio/OpenAI. This layer adds OUR stack — `sk-ant-…`, `pk_live_…`, `AIzaSy…`, `phc_…`, `tvly-…`, `pk-lf-…`, `sk-lf-…`, `fsq3…`, and JWTs. Install once per repo; runs automatically on every `git commit`.

```bash
# From workspace root (requires: pip install pre-commit)
cd "Travel Agent" && pre-commit install && cd ..
cd "Travel App"   && pre-commit install && cd ..
pre-commit install   # workspace repo
```

See `Travel Agent/docs/operations/Secret Rotation Runbook.md` for what to do when it fires.

---

### A1 — Apple Team ID into local `.env` ✅ (Fly) / 🔴 (local)

**Time est:** 2 min  
**Done in Fly secrets:** `INVITE_APPLE_TEAM_ID=QNZ5K23A74`  
**Still needed:** paste the same value into `Travel Agent/.env` so local dev serves a valid AASA.

```bash
# Travel Agent/.env
INVITE_APPLE_TEAM_ID=QNZ5K23A74
```

**Verify (local):**
```bash
curl -s http://localhost:8000/.well-known/apple-app-site-association | grep -q QNZ5K23A74 && echo ok
```
**Verify (prod, once custom domain is live):**
```bash
curl -s https://travelagent.app/.well-known/apple-app-site-association | grep -q QNZ5K23A74 && echo ok
```
**Notes:** Apple's CDN re-fetches AASA within ~24h after domain goes live. Force a refresh at `https://app-site-association.cdn-apple.com/a/v1/travelagent.app`.

---

### A2 — Custom domain: point `travelagent.app` at Fly 🔴

**Time est:** 15 min + DNS propagation (~1–24h)  
**Depends on:** own the domain, Fly app is live (✅ done)

```bash
# 1. Add cert to the Fly app
fly certs add travelagent.app --app vesper-backend

# 2. Get the IP to create the A record
fly ips list --app vesper-backend

# 3. In your DNS registrar: add A record  travelagent.app → <Fly IPv4>
#    (and AAAA for the IPv6 if you want dual-stack)

# 4. Update CORS_ORIGINS in Fly to accept the new domain
fly secrets set CORS_ORIGINS="https://travelagent.app,https://vesper-backend.fly.dev" --app vesper-backend
```

**Verify:**
```bash
curl -fsS https://travelagent.app/health   # once DNS propagates
```
**Notes:** Fly auto-provisions the Let's Encrypt cert once the DNS record is live. The cert may take a few minutes after propagation.

---

### A3 — Clerk application 🔴

**Time est:** 30 min (incl. phone OTP testing)  
**Depends on:** none (run in parallel with A2)

- dashboard.clerk.com → Create application → enable **Phone Number** sign-in
- Copy credentials into Fly secrets (CLERK_JWKS_URL and CLERK_ISSUER are already set; you may need to update them if creating a new Clerk application):
  ```bash
  fly secrets set \
    CLERK_JWKS_URL=https://<your-instance>.clerk.accounts.dev/.well-known/jwks.json \
    CLERK_ISSUER=https://<your-instance>.clerk.accounts.dev \
    --app vesper-backend
  ```
- In `Travel App/.env` (local dev):
  ```
  EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_live_...
  EXPO_PUBLIC_SKIP_AUTH=false
  ```

**Verify:**
```bash
# With valid JWT → 200
curl -fsS -H "Authorization: Bearer $TEST_JWT" https://travelagent.app/api/me

# Without JWT → 401
curl -fsS https://travelagent.app/api/me
```
**Notes:** Test with phone+OTP flow (production path) and the Clerk dashboard's "Impersonate user" feature (dev iteration).

---

### A4 — `eas init` and EAS env vars ✅ (projectId bound) / 🟠 (EAS Clerk secrets)

> **DONE 2026-06-26:** `eas init` complete — real `extra.eas.projectId` (`1cd69dac-…`),
> `updates.url`, and `owner: "fyan"` are committed in `travel-app/app.json`. Residual: confirm
> EAS-side Clerk env secrets for cloud builds.

**Time est:** 10 min  
**Depends on:** Expo account, Clerk publishable key (from A3)

`eas.json` is already committed with correct profiles — **do NOT run `eas build:configure`** (it would overwrite the committed profiles). Only run `eas init` to bind the real projectId:

```bash
cd "Travel App"
eas init   # writes real projectId into app.json — commit this change

# Set Clerk key as an EAS secret (not committed to eas.json)
eas env:create --environment production --name EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY \
    --value pk_live_... --visibility sensitive
eas env:create --environment preview --name EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY \
    --value pk_live_... --visibility sensitive
```

**Verify:**
```bash
jq -r '.expo.extra.eas.projectId' "Travel App/app.json"
# must NOT be: 00000000-0000-0000-0000-000000000000
```

---

### A5 — App Store Connect listing 🟠

**Time est:** 30 min  
**Depends on:** Apple Developer account

appstoreconnect.apple.com → Apps → New App
- Bundle ID: `com.travelagent.app`
- Minimum iOS: 17.0
- App name / category / description: see `docs/App Store Connect Copy.md`

After creating:
```bash
# Travel Agent/.env  +  Fly secrets
INVITE_IOS_APP_STORE_ID=1234567890
INVITE_APP_STORE_URL=https://apps.apple.com/app/id1234567890
```

```bash
fly secrets set \
  INVITE_IOS_APP_STORE_ID=1234567890 \
  INVITE_APP_STORE_URL=https://apps.apple.com/app/id1234567890 \
  --app vesper-backend
```

**Verify:** `open https://apps.apple.com/app/id<your-id>` loads (shows "not yet available" until published).

---

### A6 — APNs key for production push 🟠

**Time est:** 15 min  
**Depends on:** Apple Developer, A5

developer.apple.com → Certificates, Identifiers & Profiles → Keys → New Key → APNs  
Download the `.p8` file → upload via expo.dev dashboard.

**Verify:** trigger push from backend to a physical device running the TestFlight build → notification arrives within 10s. (Simulator does NOT prove this.)

---

### A7 — Production iOS build via EAS 🟠

**Time est:** ~30 min build + queue  
**Depends on:** A1 (local .env), A3, A4, A5

```bash
cd "Travel App"
eas build --platform ios --profile production
# When finished: submit to TestFlight from App Store Connect
```

**Verify:** TestFlight shows build in "Internal Testing"; install on a real device; tap an invite link from outside the app → deep-link opens the app at the correct screen.

---

### A8 — Expo push token ✅

**Done.** `EXPO_ACCESS_TOKEN` is set in Fly secrets. `EXPO_PUSH_ENABLED` is not explicitly set — verify:

```bash
fly secrets list --app vesper-backend | grep EXPO
# If EXPO_PUSH_ENABLED is missing:
fly secrets set EXPO_PUSH_ENABLED=true --app vesper-backend
```

---

### A9 — Google Places API key ✅

**Done.** `GOOGLE_PLACES_API_KEY` is set in Fly secrets.

**Verify (live):**
```bash
fly ssh console --app vesper-backend --command \
  "curl -fsS 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=coffee+brooklyn&key=$GOOGLE_PLACES_API_KEY' | python3 -c \"import sys,json; print(json.load(sys.stdin)['status'])\""
# Should print: OK
```

---

### A10 — Foursquare API key ✅ (local) / 🟠 (verify Fly secret)

> **DONE 2026-06-26 (local):** real `FOURSQUARE_API_KEY` is set in `travel-agent/.env`. Note the
> var name: code reads the **unprefixed** `FOURSQUARE_API_KEY` (`backend/core/settings_base.py:50`,
> `backend/places/settings.py:23` — "no PLACES_FOURSQUARE_API_KEY needed"), not `PLACES_FOURSQUARE_API_KEY`.
> Residual: confirm the Fly secret is set (can't verify from repo).

**Time est:** 5 min  
**Why:** Primary live-ops venue provider (cheaper than Google). Powers cache fan-out. Default daily limit 500 — free tier covers dogfood comfortably.

1. foursquare.com/developers → Create API key
2. Set in Fly secrets:
```bash
fly secrets set FOURSQUARE_API_KEY=fsq3... --app vesper-backend  # unprefixed shared key — code reads this, not PLACES_*
```

---

## Phase 2 — Pre-external-dogfood hardening

Items to clear before handing out invite links to people outside your immediate circle.

---

### B1 — Rotate live API keys before sharing any TestFlight build 🔴

**Time est:** 15 min  
**Why:** your `.env` has working keys from dev. Any build that ships with `ANTHROPIC_API_KEY` embedded (or any log/crash report that leaks it) exposes production credits. Rotate first, then share.

- Anthropic: console.anthropic.com → API Keys → Create new → copy into Fly secrets → revoke old one
- Tavily: app.tavily.com → API → Regenerate

```bash
fly secrets set ANTHROPIC_API_KEY=sk-ant-... --app vesper-backend
# (Tavily similarly)
```

---

### B2 — Privacy policy finalized 🔴

**Status:** draft/placeholder is in the app.  
**Time est:** 1–2 h (write) + legal review if you want it

The current privacy policy text needs to match the actual build (voice recording, photo analysis, location, group data sharing). See `docs/App Privacy Disclosures.md` for the inventory of what the app collects. Apple requires a valid privacy policy URL before TestFlight submission.

**Verify:** navigate to the privacy policy URL in the app → content accurately describes actual data practices.

---

### B3 — Microphone/audio privacy disclosure aligned 🟠

**Time est:** 30 min (decision) + 1h (code)  
**What:** the app has two conflicting postures — "voice companion for narration" vs "voice input for concierge". The App Store privacy nutrition label and NSMicrophoneUsageDescription string need to pick one posture and be consistent.  
**Decision:** which use case is primary in the initial TestFlight build?  
**Then:** Claude Code can update the strings and Info.plist entries to match.

---

### B4 — Eval baselines (11 missing) 🟠

**Time est:** ~70 min sequential / ~25 min parallel | ~$0.33 total API cost  
**What:** 11 of 33 concierge eval scenarios have no committed baseline. CI's `check-baseline-coverage` gate fails, and the pre-push hook tier can't be installed until they're filled.  
**How:** use the prompt in [separate thread — see session 2026-05-22].

Missing scenarios:
```
accessibility_wheelchair_dumbo    bushwick_tired_group_dinner
cold_start_first_turn             dev_budget_direct_conflict
family_generational_balance       group_disagreement_afternoon
handoff_multi_day_weekend         large_group_reunion_dinner
solo_emergency_lost_phone         time_critical_dinner_before_show
voice_quick_dinner_pick
```

After all 11 are promoted: `PYTHONPATH=. python -m tools.eval.cli replay --all --strict --results-dir tools/eval/baselines` should show 0 regressions across all 33.

---

### B5 — Wire ops crons 🟡

**Time est:** 30 min  
**Depends on:** backend stable + at least one active trip

Two scripts need to be scheduled (or run manually at first):

```bash
# Pre-warm places cache — daily at 04:00 UTC
PYTHONPATH=. python scripts/refresh_upcoming_venues.py

# Purge stale places cache entries — weekly
PYTHONPATH=. python scripts/purge_places_cache.py

# Quality sampling — weekly (after you have real traffic)
PYTHONPATH=. python scripts/run_quality_samples.py

# Quality drift check — daily (after quality samples exist)
PYTHONPATH=. python scripts/check_quality_drift.py
```

For now: add these to a `crontab` on any machine that stays on, or schedule via `fly console` once you have a dedicated ops machine. Cron lines are documented in `Travel Agent/CLAUDE.md` → "Quality sampling cron" and "Places cache cron".

---

## Phase 3 — Invite delivery & distribution

Defer until you're actively sending external invites.

---

### C1 — SendGrid (email invites) 🟡

**Time est:** 30 min (incl. DNS TXT verification)  
**Depends on:** custom domain (A2)

sendgrid.com → API Keys → Create (Mail Send permission) → verify `invites@travelagent.app` as sender via DNS TXT record.

```bash
fly secrets set \
  SENDGRID_API_KEY=SG.... \
  SENDGRID_FROM_EMAIL=invites@travelagent.app \
  SENDGRID_FROM_NAME=Vesper \
  --app vesper-backend
```

**Verify:** invite flow sends email to a real address.

---

### C2 — Twilio (SMS invites) 🟡

**Time est:** 20 min

twilio.com → Console → Phone Numbers → Buy a number.

```bash
fly secrets set \
  TWILIO_ACCOUNT_SID=AC... \
  TWILIO_AUTH_TOKEN=... \
  TWILIO_FROM_NUMBER=+15555550123 \
  --app vesper-backend
```

**Verify:** trigger SMS invite to your own phone → message arrives.

---

### C3 — Google Play Console (Android) 🟡

**Time est:** 1–2 h  
**Depends on:** none (can start anytime)

play.google.com/console → Create app → Package: `com.travelagent.app` → grab SHA-256 cert fingerprint for Digital Asset Links.

```bash
fly secrets set \
  INVITE_PLAY_STORE_URL=https://play.google.com/store/apps/details?id=com.travelagent.app \
  --app vesper-backend
```

**Verify:** `assetlinks.json` at `https://travelagent.app/.well-known/assetlinks.json` includes the SHA-256.

---

## Phase 4 — Post-dogfood strategy (discuss, don't schedule yet)

These are decisions, not tasks. File them as "decide when dogfood data exists."

---

### D1 — Monetization paywall design

**Current thinking (2026-05-20):** paywall the *depth* (live concierge, planning, group coordination, deeper memory) — NOT the shareable artifact, which would strangle the distribution loop. Low-frequency travel reframe: the moat is the personal asset (trip history, taste graph) users won't abandon, not daily engagement.

**Decision gate:** after first 10 paying users — what are they actually paying for?

---

### D2 — Place-relationship vision scoping

**Current thinking (2026-05-20):** Vesper is ultimately about a person's relationship with *places in general*, not just travel. "I live in Brooklyn but spending a day in Williamsburg" — same concierge applies. This resolves the low-frequency tension (home city = authentically high-frequency use).

**Decision gate:** after dogfood data shows how often users engage between trips.

---

### D3 — Auto-stop policy for Fly machines

**Current setting:** `auto_stop_machines = false` (machines stay warm). Fine for dogfood (cold starts are 8s+, painful for first morning message). Revisit once you have enough traffic that the cost of always-on exceeds the UX penalty of cold starts.

**Fly config:** `Travel Agent/fly.toml` → `[http_service]` → flip `auto_stop_machines = true` when ready.

---

## Pre-TestFlight sanity checklist

Run this before `eas build --profile production --platform ios`. Every box must be checked or the build will silently degrade.

- [ ] `ANTHROPIC_API_KEY` is a production key with a monthly spend cap set in the Anthropic console.
- [ ] `CLERK_JWKS_URL` + `CLERK_ISSUER` point at a real Clerk tenant (not the placeholder).
- [ ] `EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY` is the matching `pk_live_…`.
- [ ] `SKIP_AUTH=false` in backend `.env` **and** `EXPO_PUBLIC_SKIP_AUTH=false` in `Travel App/.env`.
- [ ] `EXPO_PUBLIC_API_URL` is HTTPS pointing at the managed backend (not localhost).
- [ ] `INVITE_APPLE_TEAM_ID` is your real Team ID (not `REPLACE_ME`). ✅ set in Fly as `QNZ5K23A74`.
- [ ] `eas.projectId` in `app.json` is not the all-zeros placeholder.
- [ ] AASA file at `https://travelagent.app/.well-known/apple-app-site-association` returns valid JSON.
- [ ] Managed Postgres / Qdrant / Redis are reachable from the backend host. ✅ (Fly.io)
- [ ] Google Places + Foursquare API keys set, with a GCP daily budget alert configured.
- [ ] `ENVIRONMENT=production` is set on the backend.
- [ ] `DISABLE_LLM_BACKGROUND_LOOPS=true` for the first 48h of dogfood; flip to `false` after foreground turn budget calibrates.

---

## Status board (one-glance)

| # | Item | Status | Est. time |
|---|------|--------|-----------|
| A0 | Install secret-prefix pre-commit hook | 🔴 | 5 min |
| A1 | Apple Team ID → local `.env` | 🔴 | 2 min |
| A2 | Custom domain `travelagent.app` → Fly | 🔴 | 15 min + DNS wait |
| A3 | Clerk application | 🔴 | 30 min |
| A4 | `eas init` + EAS env vars | ✅ projectId bound | — |
| A5 | App Store Connect listing | 🟠 | 30 min |
| A6 | APNs key | 🟠 | 15 min |
| A7 | Production iOS EAS build + TestFlight | 🟠 | 30 min + queue |
| A8 | Expo push token | ✅ | — |
| A9 | Google Places API key | ✅ | — |
| A10 | Foursquare API key | ✅ local / verify Fly | — |
| B1 | Rotate API keys before first external share | 🔴 | 15 min |
| B2 | Privacy policy finalized | 🔴 | 1–2 h |
| B3 | Microphone posture decision + strings | 🟠 | 30 min decision |
| B4 | Eval baselines (11 missing) | 🟠 | 70 min / $0.33 |
| B5 | Ops crons wired | 🟡 | 30 min |
| C1 | SendGrid (email invites) | 🟡 | 30 min |
| C2 | Twilio (SMS invites) | 🟡 | 20 min |
| C3 | Google Play Console | 🟡 | 1–2 h |

**Estimated calendar time to "first external user on TestFlight":** 1–2 focused days. Most items are < 30 min of actual work; the blockers are Apple propagation and DNS TTLs.

---

## Dependency graph

```
Phase 1 critical path:

  Clerk (A3) ──────────────────────────────────┐
  Apple Dev → Team ID (A1, local .env) ────────┤
             → App Store listing (A5) ──────────┤──→ EAS build (A7) → TestFlight
             → APNs key (A6) ───────────────────┘
  EAS init (A4) ──────────────────────────────→ build (A7)
  Domain (A2) → travelagent.app live ──────────→ AASA + SSL

Before first external share:
  B1 (key rotation)  B2 (privacy policy)  B3 (mic disclosure)

Invite delivery (defer):
  C1 SendGrid ← needs domain (A2)
  C2 Twilio   ← independent
  C3 Play Console ← independent
```
