# Area Audit: Invite / Join / Auth / Deeplinks

Date: 2026-05-21  
Agent: Codex / Cursor Cloud audit  
Scope: Workspace instructions; reliability docs; invite API routes/models/db helpers; invite landing HTML/AASA; backend auth startup guards; frontend invite route, auth redirect, sign-in/up flows, notification and pending-invite surfaces; targeted deterministic checks.  
Mode: Audit only. No product-code changes.

## Executive Summary

- Dogfood risk: High
- Highest-risk finding: An unauthenticated invite recipient can view the invite, submit private intake, hit sign-in on accept, and then land in Trips without returning to the invite.
- Checks run: `make contract-check` -> pass; `make api-coverage-check` -> pass; `make mock-real-parity` -> pass; `make golden-path-qa` -> pass; `PYTHONPATH=. pytest tests/api/test_invites_api.py tests/api/test_invite_landing.py -q` -> fail, 1 stale test; `npm test -- --runTestsByPath __tests__/screens/invite-landing.smoke.test.tsx __tests__/data/notifications.test.ts --runInBand` -> pass.
- Residual uncertainty: I did not run a real Clerk device flow or hit live Universal Link CDN behavior; deep-link production behavior is inferred from committed config and docs.

## Findings

### P0 — Unauthenticated invite accept loses invite context after sign-in

Status: Confirmed  
User impact: A friend who is not signed in can tap an invite, see the landing page, enter private signal, tap join, get sent to sign-in, and then land in the generic Trips/onboarding flow instead of joining the trip. They likely need to re-tap the original link, and their “I just joined” moment feels broken.  
Product promise affected: invite loop / auth detour / private intake continuity

References:

- `Travel Agent/backend/api/routes/invites.py:586` — `GET /api/invites/{token}` is public, so anonymous users can load the invite without a 401.
- `Travel App/app/invite/[slug].tsx:130` — the app submits intake before accept, so the private signal can be recorded pre-auth.
- `Travel App/app/invite/[slug].tsx:145` — `acceptInvite` is the first authenticated step in the tap-to-join path.
- `Travel App/app/invite/[slug].tsx:153` — non-409 accept errors are treated as failure; there is no 401-specific pending-invite persistence here.
- `Travel App/utils/api/http.ts:358` — any 401 redirects to sign-in at the HTTP layer.
- `Travel App/app/invite/[slug].tsx:350` — pending invite token persistence only happens if `viewInvite` returns 401, which the backend public endpoint will not do.
- `Travel App/components/auth/SignInImpl.tsx:133` — email sign-in sets the Clerk session.
- `Travel App/components/auth/SignInImpl.tsx:137` — email sign-in routes directly to `/tabs/trips`, bypassing `AuthRedirect`.
- `Travel App/components/auth/SignInImpl.tsx:180` — OAuth sign-in routes to onboarding safety, also bypassing pending-invite handling.
- `Travel App/components/auth/AuthRedirect.tsx:38` — pending invite restoration exists, but only runs when this component is in the route path.

Why it matters:

The core dogfood acquisition loop is “tap invite → sign in if needed → join correct trip.” Today the code path only preserves the token for a 401 during invite view, but invite view is explicitly public. The 401 happens later on accept, after the user has already invested effort in the page.

Repro or deterministic test idea:

1. In real-auth mode, clear Clerk session.
2. Open `/invite/{token}` for a valid trip invite; `viewInvite` returns 200.
3. Select a chip or enter private note, then tap “Join this trip.”
4. Expected: token is persisted, sign-in completes, app returns to `/invite/{token}` or completes accept and lands in `routes.tripChat(tripId)`.
5. Current likely: accept 401 triggers sign-in; sign-in routes to tabs/onboarding with no pending invite restoration.

Suggested fix direction:

Persist the invite token before any auth-required accept redirect, and make sign-in/sign-up completion consume the pending invite destination instead of hard-routing to Trips/onboarding. A small regression test should simulate `viewInvite` success followed by `acceptInvite` 401 and assert `setPendingInviteToken(slug)` plus post-auth return.

Related bug class:

Auth redirect state loss / pre-auth context drop

Confidence: High

### P1 — Raw invite tokens still flow through non-join IDs, logs, and provenance

Status: Confirmed  
User impact: Bearer invite tokens can appear in trip-home card IDs, dismissal persistence/API payloads, one exception log path, and observation provenance. A tester is unlikely to notice, but this violates the promise that invite tokens are absent from logs/events/analytics/IDs where not needed.  
Product promise affected: bearer-token handling / privacy

References:

- `Travel Agent/backend/home/feed.py:431` — `just_accepted` home card uses `inv.token` as `ref_id`.
- `Travel Agent/backend/home/feed.py:449` — `pending_too_long` home card uses `inv.token` as `ref_id`.
- `Travel Agent/backend/home/feed.py:461` — `unread_intake` home card uses `inv.token` as `ref_id`.
- `Travel Agent/backend/api/routes/home.py:101` — dismiss/undismiss accepts arbitrary `ref_id` from the client.
- `Travel Agent/backend/api/routes/home.py:141` — dismissal writes that `ref_id` through to persistence.
- `Travel Agent/backend/core/db/home_dismissals.py:40` — persisted dismissal rows store `ref_id`, so invite tokens can become durable UI state.
- `Travel Agent/backend/api/routes/invites.py:1000` — add-member failure log includes raw `token` in the formatted exception arguments.
- `Travel Agent/backend/api/routes/invites.py:1059` — invite intake observation provenance stores raw `"token": tok`.

Why it matters:

The frontend routing for these cards does not need the actual invite token; it routes by archetype and trip context. Keeping bearer tokens as UI IDs and stored dismissal keys unnecessarily broadens where a live join credential can appear.

Repro or deterministic test idea:

1. Create or fixture a trip with an unconsumed invite older than three days.
2. Call `GET /api/trips/{trip_id}/home_cards`.
3. Expected: invite-related cards use a non-redeemable ID such as `token_fp` or a synthetic stable card key.
4. Current: `ref_id` equals the raw token and dismissing the card persists that value.

Suggested fix direction:

Use `_token_fp(token)` or a scoped synthetic card key for invite-related home cards and dismissal IDs. Replace raw-token observation provenance with `token_fp` or invite row metadata that cannot redeem the link. Change the exception log to `_token_fp(token)`.

Related bug class:

Bearer-token leakage / analytics identifier leak

Confidence: High

### P2 — Preview Universal Link testing is not production-realistic before the custom domain is live

Status: Suspected  
User impact: The runbook says the preview build can test on a device before `travelagent.app` is wired, but the app only claims `travelagent.app`. A preview invite hosted or minted under `travel-agent.fly.dev` would open Safari instead of the app unless the build also claims that host.  
Product promise affected: Universal Links / fallback reliability

References:

- `Travel App/eas.json:23` — preview API points at `https://travel-agent.fly.dev`.
- `Travel App/app.json:20` — iOS Associated Domains only includes `applinks:travelagent.app`.
- `Travel App/app.json:38` — Android intent filter only claims host `travelagent.app`.
- `Travel Agent/backend/api/routes/invites.py:87` — invite URL host is controlled by `PUBLIC_INVITE_BASE_URL`, defaulting to `https://travelagent.app/invite`.
- `Travel Agent/backend/api/routes/invite_landing.py:287` — AASA is served for whatever backend host is requested, but the app must also claim that exact host.
- `docs/Owner Action Items.md:44` — docs say preview points at Fly so device testing can happen before the custom domain is wired.

Why it matters:

Universal Links require an exact match among link host, app associated domain, and served AASA host. The current production path can work once `travelagent.app` is live, but the documented preview path appears to test a different host than the app claims.

Repro or deterministic test idea:

1. Build preview with `EXPO_PUBLIC_API_URL=https://travel-agent.fly.dev`.
2. Mint an invite whose `PUBLIC_INVITE_BASE_URL` is `https://travel-agent.fly.dev/invite`.
3. Install preview build on a device and tap that link from Messages.
4. Expected: app opens to `/invite/{token}`.
5. Current likely: Safari opens because `applinks:travel-agent.fly.dev` is not in entitlements.

Suggested fix direction:

Either make preview mints still use `travelagent.app` and require that domain before Universal Link testing, or add a preview associated domain/intent filter and matching AASA/assetlinks setup for the Fly host. Document which path is canonical.

Related bug class:

Deploy config drift / deep-link host mismatch

Confidence: Medium

### P3 — Targeted backend invite suite has a stale privacy assertion

Status: Confirmed  
User impact: No direct user-facing breakage found, but the area’s cheapest backend test command is red, which lowers confidence for future invite changes.  
Product promise affected: reliability tooling

References:

- `Travel Agent/backend/api/routes/invites.py:757` — intake event payload now stores `token_fp`.
- `Travel Agent/backend/api/routes/invites.py:762` — comment says raw chip/free-text stays out of `trip_events`.
- `Travel Agent/backend/api/routes/invites.py:765` — payload stores `intake_digest`, not raw `intake`.
- `Travel Agent/tests/api/test_invites_api.py:440` — failing test still expects `payload["intake"]["chip_answer"]`.

Why it matters:

The implementation moved in the right privacy direction, but the test was not updated. A red targeted suite makes it easier to miss a future real invite regression.

Repro or deterministic test idea:

1. Run `PYTHONPATH=. pytest tests/api/test_invites_api.py tests/api/test_invite_landing.py -q` from `Travel Agent`.
2. Current: one failure in `TestSubmitIntake.test_intake_logs_invite_intake_received_event`.
3. Expected: assert `intake_digest` shape and absence of raw `intake`.

Suggested fix direction:

Update the test to assert `intake_digest.chip_present`, `free_text_present`, and no raw `intake` field.

Related bug class:

Test drift after privacy hardening

Confidence: High

## Non-Findings / Things Ruled Out

- Backend trip invite accept has same-user retry recovery for consumed/exhausted tokens: `_recover_consumed_invite` returns success when the actor is already a member or owns the consumed single-use slot.
- Organizer-visible invite answer summaries are privacy-safe in the real backend: notification feed emits token fingerprints and `Answered privately`, not raw intake.
- Auth-disabled release builds are guarded on both sides: backend prod-like startup rejects `SKIP_AUTH=true`, and the app release guard rejects mock or skip-auth mode.
- AASA JSON shape is covered and production startup rejects placeholder Apple Team IDs in prod-like environments.
- Contract, API coverage, mock-real parity, frontend invite/notification tests, and golden-path QA passed.

## Suggested Follow-Up Checks

- Add a frontend test for anonymous `viewInvite` success followed by `acceptInvite` 401 to prove pending invite restoration.
- Add an API test asserting invite-related home card `ref_id` never equals the raw invite token.
- Add a deploy/config check that compares `PUBLIC_INVITE_BASE_URL` host with app associated domains / intent filter hosts for each EAS profile.
