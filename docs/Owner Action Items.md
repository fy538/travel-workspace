# Owner Action Items

Single source of truth for everything that requires a human decision, account access, or
calendar time between today and first TestFlight. Delegable code work is broken out in
Section 3; founder-console work no agent can do is in Section 2.

**Last verified:** 2026-08-09 against the release and journey authorities,
current GitHub Actions state, and live `/health`, `/ready`, and `/privacy`
probes. External-console rows remain explicitly unverified. Supersedes the
2026-05-22 version, most of which is now done or was misdiagnosed.

**Status legend:** 🔴 blocks first TestFlight · 🟠 before external cohort · 🟡 before public
launch · ✅ done (evidence cited) · ❓ FOUNDER-MUST-CONFIRM (external console — not visible
from the repo)

---

## Honest status (one paragraph)

Backend `/health`, `/ready`, and `/privacy` returned HTTP 200 on 2026-08-09.
Real Clerk auth was last verified separately on 2026-07-04. The v1 scope is
locked and flag-gated ([V1 release contract](release/v1-scope.md)), but release
readiness is **not certified**: all 28 journey contracts and their test/flow
anchors are defined, current receipt-backed execution is unrecorded, and the
required physical-device lane is **0/3 current** for J04/J05/J10. Seeded replay
is **28/28 passing** as of 2026-08-10 (`make certify-logic` at `travel-agent
b56b38823`) — J08 is fixed and is no longer a blocker. The critical path is
therefore: restore a reliable green child-repo CI signal; cut a production EAS
build; record current-revision and two-device evidence; then submit to TestFlight.
App Store Connect, APNs, Clerk review credentials, and key rotation remain
founder-console confirmations.

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
| 0 | **Restore a reliable green child-repo CI signal.** App CI run `31322965305` executed on 2026-08-09 but failed multiple code/contract gates; the latest backend CI runs `31232999675` and `31120695581` remain queued with no jobs. Determine whether the backend queue is account capacity, concurrency, or Actions configuration, then rerun both current heads. | **A/B** | 🔴 open — app executes but is red; backend is queued |
| 1 | **Verify `/privacy` stays reachable in the release build** — `https://vesper-backend.fly.dev/privacy` returned HTTP 200 with the privacy policy on 2026-08-09. Apple requires this URL to remain live; recheck after the next backend deployment. | **B** | ✅ live probe verified 2026-08-09; release-build / post-deploy recheck remains |
| 2 | **Verify v1 microphone posture in the release build** — voice remains flag-OFF. `app.config.js` now strips stale microphone and audio-background capabilities when voice is disabled, while preserving the explicit dogfood voice opt-in. | **B** | ✅ static Expo introspection verified 2026-07-26; inspect the generated production IPA before submission |
| 3 | **Confirm App Store Connect app exists** (bundle `com.fyan.vesper`, iOS 17+) + set `INVITE_IOS_APP_STORE_ID` / `INVITE_APP_STORE_URL` in Fly secrets. Old A5. | **A** | ❓ FOUNDER-MUST-CONFIRM (external console) |
| 4 | **Confirm APNs auth key uploaded to Expo** (old A6) — required for push on a physical device. | **A** | ❓ FOUNDER-MUST-CONFIRM (external console) |
| 5 | **Rotate Anthropic + Tavily keys** before any build leaves the machine, set fresh keys in Fly secrets, revoke old (old B1 / deploy-surface #3). | **A** | ❓ FOUNDER-MUST-CONFIRM (external console) |
| 6 | **Add Clerk review-only test phone** `+15555555555` / OTP `424242` (per Apple Review Notes) so the reviewer doesn't hit a real OTP send. | **A** | ❓ FOUNDER-MUST-CONFIRM (Clerk dashboard) |
| 7 | **Cut production iOS build** — `eas build --platform ios --profile production`. Needs founder Apple/Expo auth. Note: the `production` EAS profile currently has **no Clerk key** (dogfood profile uses `pk_test` on the `picked-firefly-95` dev tenant) — either wire a `pk_live` prod tenant or point the first build at the working dogfood config. | **A** | 🔴 open |
| 8 | **Record the required J04/J05/J10 two-device certification on that build.** The current lane is `0/3`; the runbook is `docs/working/journey-live-full-cert-04-05-10.md`. A broader J01–J12 release walk remains useful QA, but it is not interchangeable with these three credentialed receipts. | **B** (founder-assisted on-device taps) | 🔴 open — medium |
| 9 | **Submit to TestFlight** from App Store Connect once the build passes the device walk. | **A** | 🔴 open |

**Not blockers (verified done or off-path):** custom domain / DNS, SendGrid, Twilio, Google
Play — all deferred (Section 5). Eval baselines — done (Section 4). Secret hooks — installed
(Section 4).

---

## Section 2 — Founder-only ops checklist (no agent can do these)

| Item | Status | Evidence / note |
|------|--------|-----------------|
| GitHub Actions execution | 🔴 REQUIRES TRIAGE | App CI currently executes, disproving the older claim that every child job is billing-blocked. Backend runs remain queued without jobs. Check Actions concurrency and account capacity, then rerun current heads; do not reuse the obsolete `29069359543` diagnosis as current evidence. |
| Custom domain `travelagent.app` → Fly | ❓ OPEN but **OFF critical path** | Live probe: apex serves a marketing lander (`/lander` redirect), not the backend; AASA/health there fail. App uses Fly host directly — see scope correction above. Deferred to Section 5. |
| App Store Connect app + listing | ❓ FOUNDER-MUST-CONFIRM | Copy ready in `docs/launch/App Store Connect Copy.md`. **Bundle must be `com.fyan.vesper`** (matches app.json + live AASA) — the launch docs' `com.travelagent.app` is stale; use the app.json value. |
| APNs auth key (.p8) → Expo | ❓ FOUNDER-MUST-CONFIRM | `EXPO_ACCESS_TOKEN` is set in Fly; `EXPO_PUSH_ENABLED` default is `false` (registry.yaml) — confirm the Fly secret is `true` for real push. |
| Clerk prod config | ⚠️ PARTLY DONE / decision needed | Clerk verified live on Fly (401 on garbage token, Step 0 2026-07-04). **But that's the `picked-firefly-95` dev tenant (`pk_test`).** Fine for the dogfood cohort; a real public launch needs a `pk_live` prod tenant wired into the `production` EAS profile. Also add the review test-phone (Section 1 #6). |
| Rotate live API keys (Anthropic, Tavily) | ❓ FOUNDER-MUST-CONFIRM | Deploy-surface #3. Do before any build ships. |
| Final privacy policy published + reachable | ✅ LIVE; RECHECK AT BUILD | `/privacy` returned HTTP 200 with HTML on 2026-08-09. Re-probe after the release-candidate backend deployment and before submission. |
| EAS / TestFlight build submission | 🔴 OPEN | Section 1 #7/#9. Requires Apple Developer + Expo login. |
| Cohort recruitment (first 10 testers) | 🟠 OPEN | Plan is written: `docs/launch/TestFlight Tester Onboarding.md` §C/§D + `dogfood-loop-validation-2026-07-04.md` Part 2. Do NOT self-seed groups (that contaminates the re-invite signal — the one bet being measured). |
| Anthropic monthly spend cap set in console | ❓ FOUNDER-MUST-CONFIRM | Pre-flight sanity checklist item. |

---

## Section 3 — Delegable engineering (an agent / you-with-an-agent can close)

| Item | Size | Note |
|------|------|------|
| **Re-probe `/privacy` after the release deployment** (Section 1 #1) | S | It returned 200 on 2026-08-09. Preserve that result through the release-candidate deployment and record the probe. |
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

## Section 6 — Device-cert-walk & dogfood-funnel prerequisites (set before the J04/J05/J10 walk)

Four ops settings that no code change can fix and that silently degrade the device-cert walk or
the dogfood funnel if left as-is. Each is dark/unset **by default**, so a fresh device build will
appear to work while emitting nothing (funnel) or delivering nothing (push). Set these on the
backend the device build points at *before* the walk. `(A)` = founder-only ops.

| # | Item | A/B | Status |
|---|------|-----|--------|
| 1 | **Set `POSTHOG_API_KEY` — the entire activation funnel is currently log-only/dark.** With the key unset, `backend/core/telemetry.py` logs `"telemetry: POSTHOG_API_KEY unset — events log-only"` (telemetry.py:284) and drops every event on the floor. That means the whole activation funnel — `activation.account_created`, `activation.onboarding_signal`, `activation.first_turn` (first-value), `activation.trip_created`, `activation.invite_minted/landing_viewed/accepted` (telemetry.py:194–210) — emits **nothing** to PostHog, so the dogfood walk produces zero measurable funnel. Set the PostHog project key as a Fly secret on the device build's backend so account-creation, onboarding, and first-value are actually captured. | **A** | 🟠 FOUNDER-MUST-SET — `fly secrets set POSTHOG_API_KEY=<project key>` (external PostHog console); verify a walk event lands in the PostHog project before the cert walk. |
| 2 | **Set `EXPO_PUSH_ENABLED=true` + the Expo push secret — zero pushes reach the two physical cert devices.** `EXPO_PUSH_ENABLED` defaults to `false` (`backend/notifications/receipt_reaper.py:39`); with it unset the dispatcher is log-only and makes **no** HTTP call to Expo (`channel_dispatch.py:461` — real send only fires on `=true`). On a real device that silently breaks the **J09** push demo and yields **no** push open/engagement data for the funnel. Set the Fly secret to `true` **and** confirm the Expo push credential is present (`EXPO_ACCESS_TOKEN` in Fly + APNs `.p8` uploaded to Expo — see Section 1 #4 / Section 2). Without both, "push works" is indistinguishable from "push silently dropped." | **A** | 🟠 FOUNDER-MUST-SET — `fly secrets set EXPO_PUSH_ENABLED=true`; confirm APNs key + `EXPO_ACCESS_TOKEN` (Section 1 #4). |
| 3 | **Give the device build's backend live LLM creds (or a J01 replay cassette) — else the J01 opener stalls at a blank thread.** `AI_MODE` unset defaults to `live` (`backend/core/ai_mode.py:96–97`), so the J01 front-door ("Vesper shapes the idea") needs a real, rotated `ANTHROPIC_API_KEY` in Fly for the opening turn to generate. The only alternative is `AI_MODE=replay` **with** `LLM_VCR_MODE=replay` and a recorded cassette covering the J01 opener (`ai_mode.py:237` / `dogfood_preflight.py:458` — replay fails closed without the VCR). Pick one before the walk: a live key (with a spend cap, Section 1 #5) **or** a verified J01 cassette. If neither is set, the opener returns nothing and the first-value moment never fires. | **A** | 🔴 FOUNDER-MUST-DECIDE — either `fly secrets set ANTHROPIC_API_KEY=<rotated key>` (`AI_MODE` left/set `live`), or `AI_MODE=replay` + `LLM_VCR_MODE=replay` + J01 cassette. |
| 4 | **Confirm mara's Clerk device account is linked to the seeded `mara@dogfood.local` row (J03).** J03 signs in on-device as mara; the seeded persona row uses the reserved `@dogfood.local` TLD that Clerk rejects, so the account is linked by writing `external_auth_id` on the existing row via `tools/dogfood/link_clerk_accounts.py` (LINKS maps `mara@dogfood.local` → `user_3G61xwb0fxRgMjBfRba8Rvgox4F`, link_clerk_accounts.py:40). Confirm that mapping is actually applied **against the backend the device build points at** (not just local) before the walk — a stale/unlinked row lands mara in a fresh empty account with none of her seeded lisbon-phase1 group/trip state, breaking J03. | **A** | 🟠 FOUNDER-MUST-CONFIRM — dry-run `python -m tools.dogfood.link_clerk_accounts --dry-run` against the device-build target; if unlinked, `--apply --allow-prod`; verify mara's row shows the Clerk `external_auth_id`. |

---

## Pre-build sanity checklist (run before `eas build --profile production`)

- [ ] `ANTHROPIC_API_KEY` is a rotated production key with a monthly spend cap set. *(§2)*
- [ ] `CLERK_JWKS_URL` + `CLERK_ISSUER` point at the intended tenant; `EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY`
      matches. *(dev tenant OK for cohort; §2)*
- [ ] `SKIP_AUTH=false` (BE) **and** `EXPO_PUBLIC_SKIP_AUTH=false` (app). ✅ verified on Fly.
- [ ] `EXPO_PUBLIC_API_URL` is HTTPS → `vesper-backend.fly.dev` (not localhost).
- [ ] AASA returns valid JSON on the Fly host. ✅ verified.
- [ ] `curl vesper-backend.fly.dev/privacy` → **200** (verified 2026-08-09; rerun for the release candidate).
- [ ] `app.json` mic string removed for v1 (voice OUT). *(§1 #2)*
- [ ] Bundle ID `com.fyan.vesper` matches App Store Connect. *(§2)*
- [ ] `EXPO_PUSH_ENABLED=true` in Fly + APNs key uploaded. *(§2)*
- [ ] Working trees committed / merged to main so the build is reproducible. *(§3)*
- [ ] `DISABLE_LLM_BACKGROUND_LOOPS=true` for the first 48h.
