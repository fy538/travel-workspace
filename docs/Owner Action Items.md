# Owner Action Items

Single source of truth for everything that requires a human decision, account access, or
calendar time between today and first TestFlight. Delegable code work is broken out in
Section 3; founder-console work no agent can do is in Section 2.

**Last verified:** 2026-07-09 (against git logs in all three repos + live probes of
`vesper-backend.fly.dev` + the launch/ docs). Supersedes the 2026-05-22 version, most of
which is now done or was misdiagnosed.

**Status legend:** 🔴 blocks first TestFlight · 🟠 before external cohort · 🟡 before public
launch · ✅ done (evidence cited) · ❓ FOUNDER-MUST-CONFIRM (external console — not visible
from the repo)

---

## Honest status (one paragraph)

Backend is **live and healthy** at `https://vesper-backend.fly.dev` (`/health`, `/ready` →
Postgres+Qdrant ok). Real Clerk auth is **verified active** (garbage token → 401; Step 0 of
the dogfood runbook confirmed `SKIP_AUTH=false` + JWKS reachable on Fly, 2026-07-04). The v1
scope is **locked and flag-gated** (`mvp-scope-and-flag-manifest-2026-06-30.md`; FE flag layer
+ BE story-share guard merged 2026-07-01). Journeys are **12/12 agent-certified but 0/12
device-certified on a real build** — that device walk is the headline gate. Of the original
A0–A10 owner list, **most is done**: EAS projectId bound, AASA live on Fly, Google/Foursquare
keys set, eval baselines filled, secret hooks installed. The genuinely open critical-path items
are few: **(1)** cut a production EAS/TestFlight build (A) + device-walk J01–J12 on it (B);
**(2)** fix the `/privacy` 503 in prod and reconcile the mic-permission contradiction, both of
which will fail App Review as-is (B); **(3)** confirm the founder-console prerequisites
(App Store Connect app, APNs key, key rotation) that no agent can see (A). The **single biggest
blocker is the production EAS build** — nothing downstream (device cert, TestFlight submit,
Apple review) can start without it, and it needs a founder Apple/Expo login.

**Scope correction that shrinks this list:** the app's `associatedDomains` is
`applinks:vesper-backend.fly.dev` and the live, valid AASA is served **from the Fly host**
(`QNZ5K23A74.com.fyan.vesper`, components `/invite/*` + `/stories/*`). Universal links work on
the Fly domain **today**. The `travelagent.app` custom domain (old A2) is therefore **NOT on
the TestFlight critical path** — it's a nice-to-have for the marketing lander + email sender,
deferred to Section 5.

---

## Section 1 — What actually blocks first TestFlight (ordered)

The critical path only. `(A)` = founder-only ops · `(B)` = delegable engineering.

| # | Item | A/B | Status |
|---|------|-----|--------|
| 1 | **Fix `/privacy` 503 in prod** — route exists but returns 503 on Fly; `docs/legal/privacy.md` isn't in the deployed image (or image predates the 06-28 commit). Apple requires a working privacy-policy URL; the App Store copy points at it. | **B** | 🔴 open — small (ensure file ships in Docker context / redeploy; then verify `curl vesper-backend.fly.dev/privacy` → 200) |
| 2 | **Reconcile mic-permission posture** — `app.json` ships a `microphonePermission` string, but Apple Review Notes + App Privacy Disclosures both say "no microphone requested / no audio recorded." A reviewer will see the mismatch. Voice is flag-OFF for v1, so the clean fix is to **remove the mic string** (and any mic entitlement) from the v1 build. | **B** | 🔴 open — small (decision is trivial: voice is OUT in v1, so drop the string) |
| 3 | **Confirm App Store Connect app exists** (bundle `com.fyan.vesper`, iOS 17+) + set `INVITE_IOS_APP_STORE_ID` / `INVITE_APP_STORE_URL` in Fly secrets. Old A5. | **A** | ❓ FOUNDER-MUST-CONFIRM (external console) |
| 4 | **Confirm APNs auth key uploaded to Expo** (old A6) — required for push on a physical device. | **A** | ❓ FOUNDER-MUST-CONFIRM (external console) |
| 5 | **Rotate Anthropic + Tavily keys** before any build leaves the machine, set fresh keys in Fly secrets, revoke old (old B1 / deploy-surface #3). | **A** | ❓ FOUNDER-MUST-CONFIRM (external console) |
| 6 | **Add Clerk review-only test phone** `+15555555555` / OTP `424242` (per Apple Review Notes) so the reviewer doesn't hit a real OTP send. | **A** | ❓ FOUNDER-MUST-CONFIRM (Clerk dashboard) |
| 7 | **Cut production iOS build** — `eas build --platform ios --profile production`. Needs founder Apple/Expo auth. Note: the `production` EAS profile currently has **no Clerk key** (dogfood profile uses `pk_test` on the `picked-firefly-95` dev tenant) — either wire a `pk_live` prod tenant or point the first build at the working dogfood config. | **A** | 🔴 open |
| 8 | **Device-walk J01–J12 on that build** — the `0/12 full-cert` gap. Runbook exists (`docs/working/journey-live-full-cert-04-05-10.md`); J04/J05/J10 need two real Clerk accounts on two devices. This is also the dogfood two-device pre-flight walk. | **B** (founder-assisted on-device taps) | 🔴 open — medium |
| 9 | **Submit to TestFlight** from App Store Connect once the build passes the device walk. | **A** | 🔴 open |

**Not blockers (verified done or off-path):** custom domain / DNS, SendGrid, Twilio, Google
Play — all deferred (Section 5). Eval baselines — done (Section 4). Secret hooks — installed
(Section 4).

---

## Section 2 — Founder-only ops checklist (no agent can do these)

| Item | Status | Evidence / note |
|------|--------|-----------------|
| Custom domain `travelagent.app` → Fly | ❓ OPEN but **OFF critical path** | Live probe: apex serves a marketing lander (`/lander` redirect), not the backend; AASA/health there fail. App uses Fly host directly — see scope correction above. Deferred to Section 5. |
| App Store Connect app + listing | ❓ FOUNDER-MUST-CONFIRM | Copy ready in `docs/launch/App Store Connect Copy.md`. **Bundle must be `com.fyan.vesper`** (matches app.json + live AASA) — the launch docs' `com.travelagent.app` is stale; use the app.json value. |
| APNs auth key (.p8) → Expo | ❓ FOUNDER-MUST-CONFIRM | `EXPO_ACCESS_TOKEN` is set in Fly; `EXPO_PUSH_ENABLED` default is `false` (registry.yaml) — confirm the Fly secret is `true` for real push. |
| Clerk prod config | ⚠️ PARTLY DONE / decision needed | Clerk verified live on Fly (401 on garbage token, Step 0 2026-07-04). **But that's the `picked-firefly-95` dev tenant (`pk_test`).** Fine for the dogfood cohort; a real public launch needs a `pk_live` prod tenant wired into the `production` EAS profile. Also add the review test-phone (Section 1 #6). |
| Rotate live API keys (Anthropic, Tavily) | ❓ FOUNDER-MUST-CONFIRM | Deploy-surface #3. Do before any build ships. |
| Final privacy policy published + reachable | 🔴 OPEN | `docs/legal/privacy.md` exists in repo (06-28) but `/privacy` 503s in prod (Section 1 #1 — that's the delegable fix; confirming it's live after redeploy is the founder's tick). |
| EAS / TestFlight build submission | 🔴 OPEN | Section 1 #7/#9. Requires Apple Developer + Expo login. |
| Cohort recruitment (first 10 testers) | 🟠 OPEN | Plan is written: `docs/launch/TestFlight Tester Onboarding.md` §C/§D + `dogfood-loop-validation-2026-07-04.md` Part 2. Do NOT self-seed groups (that contaminates the re-invite signal — the one bet being measured). |
| Anthropic monthly spend cap set in console | ❓ FOUNDER-MUST-CONFIRM | Pre-flight sanity checklist item. |

---

## Section 3 — Delegable engineering (an agent / you-with-an-agent can close)

| Item | Size | Note |
|------|------|------|
| **Fix `/privacy` 503** (Section 1 #1) | S | Ensure `docs/legal/privacy.md` is in the deployed image; redeploy; verify 200. Likely a Dockerfile copy / build-context gap. |
| **Strip mic-permission string** from v1 `app.json` (Section 1 #2) | S | Voice is flag-OFF for v1; the string invites an App Review question. Confirm no residual mic entitlement in the config plugin. |
| **Device-cert automation / runbook execution** (Section 1 #8) | M | The taps are on-device (founder), but the agent preps the seed data, the two-account setup, the funnel-event assertions, and triages any break (deeplink → AASA; 401 → JWKS; missing `invite.consumed` → event emission). |
| **Reachability audit on a release build** | M | v1 DoD open item: walk every entry point on the actual EAS build, confirm no OUT surface (voice/booking-txn/postcards/ambient/story-share) is reachable and no IN surface lost a load-bearing dep (Discover→trip-create, Atlas→Story, Search→profiles). Needs the build from Section 1 #7. |
| **App Store asset finalization** | S–M | Copy is written; remaining is capturing 5 real-device screenshots (list in App Store Connect Copy §Screenshots) — needs the build. Text fields are paste-ready. |
| **Deploy-surface `.env.example` hygiene** (items #1/#2/#4/#5/#6/#10) | S | ~30–45 min of doc/config: R2 vars, geofence toggle, mark `REDIS_URL` required, boot-fail on `SKIP_AUTH=false`+empty JWKS, "Production toggles" section, guard-mode table. Non-blocking but cheap. |
| **Commit the dirty working trees** | S | `travel-agent` has ~9 modified BE files uncommitted; `travel-app` is on branch `cc1-atom-adoption` (not main). Branch/commit/merge before cutting the build so the build is reproducible. |

---

## Section 4 — Verified-done since 2026-05-22 (bank these)

Cross-checked against git logs + live probes. The founder is further along than the old doc reads.

- ✅ **EAS init / projectId bound** — `app.json` has real `projectId 1cd69dac-…`, `owner: fyan`,
  `updates.url` set. (old A4)
- ✅ **AASA live + valid on the Fly host** — `GET vesper-backend.fly.dev/.well-known/apple-app-site-association`
  → `QNZ5K23A74.com.fyan.vesper`, `/invite/*` + `/stories/*`. Team ID is real (not `REPLACE_ME`).
  (old A1/A2 — the load-bearing half)
- ✅ **Clerk auth active in prod** — garbage token → 401; `SKIP_AUTH=false` on Fly; JWKS reachable
  (dogfood runbook Step 0, 2026-07-04). (old A3, on the dev tenant)
- ✅ **Google Places + Foursquare keys** — set in Fly (old A9/A10; code reads unprefixed
  `FOURSQUARE_API_KEY`).
- ✅ **Eval baselines complete** — all 11 previously-missing scenarios are committed under
  `tools/eval/baselines/` (the `20260522_16…` batch: cold_start, voice_quick_dinner_pick,
  solo_emergency_lost_phone, accessibility_wheelchair_dumbo, bushwick, dev_budget_direct_conflict,
  group_disagreement, time_critical, large_group_reunion, handoff_multi_day, family_generational).
  (old B4 — DONE)
- ✅ **Secret-prefix pre-commit hook installed** in all three repos (`.git/hooks/pre-commit`
  present; `.pre-commit-config.yaml` references the check). (old A0 — DONE)
- ✅ **v1 flag layer live + typecheck green** — FE `featureFlags.ts` gates voice/booking-txn/
  postcards/ambient/story-share; merged to main (Phase A `6a5177d4`, Phase B `a2489737`,
  Phase 7 `1251fc0d`). BE story-share + venue-disruption guards added.
- ✅ **Expenses `rate=1.0` cross-currency bug fixed** (`auto_log.py:124`) — unblocks Expenses IN.
- ✅ **Booking record stub confirmed** to work with the transaction engine flagged off
  (pre-existing gate; no new code).
- ✅ **Account deletion route wired** (`backend/api/routes/users/me.py:546 delete_account`) —
  satisfies Apple 5.1.1(v).
- ✅ **Multi-vendor LLM portability + planning cost/latency + AI-suite P0/P1 hardening** shipped
  (large body of `travel-agent` commits 05-22→07-08) — not launch-blocking but banks reliability.

---

## Section 5 — Explicitly deferred / post-cohort (NOT blocking)

- **Custom domain `travelagent.app` → Fly** (old A2) — off critical path (universal links use the
  Fly host). Needed only to (a) serve the marketing lander at a branded URL and (b) verify the
  SendGrid sender domain. Do before public launch, not before TestFlight.
- **SendGrid (email invites)** (old C1) — depends on the custom domain; in-app iMessage share
  covers the cohort. 🟡
- **Twilio (SMS invites)** (old C2) — 🟡, independent, defer.
- **Google Play Console / Android** (old C3) — 🟡, TestFlight is iOS-only.
- **Ops crons** (old B5) — pre-warm/purge places cache, quality sampling/drift — run manually at
  first; wire after there's real traffic. 🟡
- **`DISABLE_LLM_BACKGROUND_LOOPS=true` for first 48h**, then flip — operational tuning, not a
  gate. Confirm at build time.
- **Booking transaction engine, live voice, postcards, ambient, story-sharing** — deliberately
  flag-OFF for v1 per the 2026-06-30 decision record; each flips only after its own certify pass.
- **`VENUE_DISRUPTION_PROPOSALS_ENABLED`** — stays dark for cohort 1 by decision (2026-07-06);
  evaluate against real cohort-1 data, then decide for cohort 2. Not a v1 gap.
- **Live-transport JWT harness** (`dogfood-journey-live-api` over HTTP) — CI-automation
  nice-to-have (~3–5h internal glue); does NOT gate device-cert and real humans never hit it.
- **Prod Clerk tenant (`pk_live`)** — the dogfood cohort runs fine on the dev tenant; a `pk_live`
  tenant + `production` EAS profile wiring is a public-launch item.
- **Monetization paywall / place-relationship scoping / Fly auto-stop policy** (old D1–D3) —
  decisions to make *after* dogfood data exists, not tasks.

---

## Pre-build sanity checklist (run before `eas build --profile production`)

- [ ] `ANTHROPIC_API_KEY` is a rotated production key with a monthly spend cap set. *(§2)*
- [ ] `CLERK_JWKS_URL` + `CLERK_ISSUER` point at the intended tenant; `EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY`
      matches. *(dev tenant OK for cohort; §2)*
- [ ] `SKIP_AUTH=false` (BE) **and** `EXPO_PUBLIC_SKIP_AUTH=false` (app). ✅ verified on Fly.
- [ ] `EXPO_PUBLIC_API_URL` is HTTPS → `vesper-backend.fly.dev` (not localhost).
- [ ] AASA returns valid JSON on the Fly host. ✅ verified.
- [ ] `curl vesper-backend.fly.dev/privacy` → **200** (currently 503 — §1 #1).
- [ ] `app.json` mic string removed for v1 (voice OUT). *(§1 #2)*
- [ ] Bundle ID `com.fyan.vesper` matches App Store Connect. *(§2)*
- [ ] `EXPO_PUSH_ENABLED=true` in Fly + APNs key uploaded. *(§2)*
- [ ] Working trees committed / merged to main so the build is reproducible. *(§3)*
- [ ] `DISABLE_LLM_BACKGROUND_LOOPS=true` for the first 48h.
