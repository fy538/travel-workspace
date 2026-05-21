# Pre-Dogfood Audit: Dogfood Readiness

Date: 2026-05-21  
Scope: Travel Workspace cross-repo readiness for first internal/TestFlight dogfood  
Mode: audit only; no product-code changes

## Product Frame Used

The audit used the required product and reliability docs as the standard:

- The product promise is a place-aware concierge relationship, with group trips as the launch wedge.
- The dogfood risk surface is privacy, invite/join success, state coherence across Home/Plan/Map/Chat, and mock/real drift.
- Golden paths are not ready for live canary unless deterministic contract, backend/frontend tests, and mock-mode user paths are green.

## Cheap Deterministic Checks

Commands run from `/Users/feihuyan/Documents/Claude/Travel Workspace`:

| Check | Result | Notes |
|---|---:|---|
| `make doctor` | PASS with warning | Workspace/child repos present; warned `uvicorn not found`. |
| `make contract-check` | PASS | `docs/openapi.json` has 210 paths, 241 operations, 330 schemas; generated app schema matches. |
| `make api-coverage-check` | PASS | 175/175 unique frontend HTTP call sites covered by OpenAPI; 0 drift. |
| `make mock-real-parity` | PASS | 7 suites, 93 tests passed. |
| `make golden-path-qa` | PASS | Backend 247 tests passed; frontend 7 suites / 37 tests passed. |
| `make preflight-eas` | FAIL | Aborted at step 1: `eas CLI not on PATH`. Static config would also fail on placeholder `projectId`. |
| `curl https://travel-agent.fly.dev/health` | FAIL | DNS did not resolve from this machine. |
| `curl https://travelagent.app/health` | FAIL | Connection returned empty reply / HTTP `000`. |

## Findings

### P0 — Invite intake answers are exposed to the organizer despite the invite screen promising privacy

References:

- `Travel App/app/invite/[slug].tsx:233-235` says the group will not see invitee answers.
- `Travel App/app/invite/[slug].tsx:300-302` says the private signal stays between the invitee and the Concierge.
- `Travel Agent/backend/core/models/trip_invites.py:203-218` turns either `chip_answer` or free text into a surfaceable summary.
- `Travel Agent/backend/api/routes/_notifications_feed.py:190-200` includes that summary in `PendingInviteAnswer.answer_summary`.
- `Travel App/data/notifications.ts:83-92` renders the answer summary in the organizer's notification body.
- `Travel App/app/trip-info/index.tsx:413-423` renders `pending_intake_summary` on the Pending Invites surface.
- `Travel Agent/tests/api/test_invites_api.py:847-878` and `Travel App/__tests__/data/notifications.test.ts:187-205` currently assert this exposure as expected behavior.

Why it matters to a real tester:

The first invited friend is explicitly told that budget, pace, food, and accessibility notes are private. If they type "I need to keep this cheap" or select "Keep costs sane," the organizer can see the substance of that answer in notifications / pending invites. That is exactly the product's highest-risk promise: private input can inform group-safe planning without leaking the individual constraint.

Repro / deterministic test idea:

1. Create a trip invite.
2. POST `/api/invites/{token}/intake` with `{"free_text": "I cannot afford expensive dinners"}`.
3. Fetch the organizer notification feed and trip invite list.
4. Assert neither response includes the free text, chip text, or close paraphrase; only a neutral engagement state such as "Sam answered privately" is allowed.

Suggested fix direction:

Split "invitee engaged" from "invitee answer content." Keep the raw intake for the invitee's personal memory / concierge context, but make organizer-facing notifications and invite rows neutral: "Sam answered privately" or "New private signal received." Add regression tests that use sensitive budget/accessibility/free-text examples and fail if those strings appear in organizer-visible payloads.

Confidence: High.

### P0 — Release backend hosts are not reachable for preview or production dogfood builds

References:

- `Travel App/eas.json:18-27` points preview builds at `https://travel-agent.fly.dev`.
- `Travel App/eas.json:29-35` points production builds at `https://travelagent.app`.
- `docs/Deploy & Rollback Runbook.md:51-53` documents those same profiles and says release builds rely on them.
- `docs/Owner Action Items.md:46-50` marks deploying `travelagent.app` as red and says `curl -fsS https://travelagent.app/health` must return 200.
- `scripts/preflight-eas-build.sh:189-204` correctly gates release on `GET {EXPO_PUBLIC_API_URL}/health`.

Why it matters to a real tester:

A TestFlight build with `EXPO_PUBLIC_USE_MOCK_API=false` will boot against one of these URLs. If the host is unreachable, testers cannot sign in, create/join trips, accept invites, fetch notifications, or use chat. This is a dogfood blocker independent of app code quality.

Repro / deterministic test idea:

Run:

```bash
curl -sS --max-time 10 -o /dev/null -w '%{http_code}\n' https://travel-agent.fly.dev/health
curl -sS --max-time 10 -o /dev/null -w '%{http_code}\n' https://travelagent.app/health
```

Observed in this audit:

- `travel-agent.fly.dev`: DNS resolution failed.
- `travelagent.app`: empty reply / HTTP `000`.

Suggested fix direction:

Bring up a managed backend host first, wire DNS/TLS, then make both `preview` and `production` EAS URLs point at a host that returns 200 for `/health` and valid JSON for `/openapi.json`. Do not skip the live probe for dogfood builds except as an explicitly documented local-only bypass.

Confidence: High.

### P0 — EAS production build identity is still placeholder and preflight cannot run on this machine

References:

- `Travel App/app.json:52-55` has `expo.extra.eas.projectId` set to `00000000-0000-0000-0000-000000000000`.
- `docs/Owner Action Items.md:43-44` says that value must not be the placeholder and `make preflight-eas` should pass.
- `scripts/preflight-eas-build.sh:1-9` describes this preflight as the required cheap gate before EAS production builds.
- `scripts/preflight-eas-build.sh:71-78` aborts if `eas` is not on PATH; this audit hit that failure.
- `scripts/preflight-eas-build.sh:88-93` would fail next on the placeholder project id.

Why it matters to a real tester:

Even with a healthy backend, the team cannot reliably produce or submit the intended TestFlight build from this workspace. If someone works around preflight manually, the placeholder project identity can create confusing EAS behavior or build against the wrong Expo project.

Repro / deterministic test idea:

Run `make preflight-eas` from the workspace root. Current observed result: aborts because `eas CLI not on PATH`. After installing the CLI, expect the project-id check to fail until `eas init` has replaced the placeholder.

Suggested fix direction:

Install `eas-cli` in the dogfood build environment, run `eas init` in `Travel App`, commit the real `projectId`, set the Clerk publishable key in EAS env, and require `make preflight-eas` green before queuing any TestFlight build.

Confidence: High.

### P0 — Raw invite bearer tokens are logged and persisted despite a local "never log tokens" rule

References:

- `Travel Agent/backend/api/routes/invites.py:66-77` states raw invite tokens are bearer credentials and must never be written to logs.
- `Travel Agent/backend/api/routes/invites.py:751-762` persists raw `token` in the `invite.intake_received` trip event payload.
- `Travel Agent/backend/api/routes/invites.py:766-769` logs raw `token` on intake event logging failure.
- `Travel Agent/backend/api/routes/invites.py:841-855` dispatches notification content and logs `invite.token` on failure.
- `Travel Agent/backend/api/routes/invites.py:936-947` persists raw `token` in the `invite.consumed` trip event payload.
- `Travel Agent/backend/api/routes/invites.py:948-949` uses the fingerprint helper correctly in one failure log, showing the intended pattern.

Why it matters to a real tester:

Invite tokens are join credentials. During dogfood, logs and event payloads are likely to be copied into debugging tools, support screenshots, or analytics exports. A raw token in those places can let someone join a trip, inspect the invite landing state, or correlate private pre-auth intake with a specific recipient.

Repro / deterministic test idea:

1. Patch `append_trip_event` to raise inside `submit_intake`.
2. POST `/api/invites/tok_secret/intake`.
3. Capture logs and assert `tok_secret` never appears; only `_token_fp(token)` appears.
4. Separately assert `append_trip_event` payloads use a token fingerprint or invite id, not the raw token.

Suggested fix direction:

Use `_token_fp(token)` everywhere outside the invite table itself. For events, store `invite_token_fp` or an internal invite row id. For frontend notification IDs, use an opaque notification id rather than the invite token unless the user is explicitly on an organizer-only invite management surface that needs the share URL.

Confidence: High.

### P1 — Invite accept is not idempotent for the realistic "success response lost, retry after consumed" case

References:

- `Travel App/app/invite/[slug].tsx:126-149` creates and sends a stable idempotency key when accepting an invite.
- `Travel Agent/backend/api/routes/invites.py:867-893` accepts `X-Idempotency-Key` but does not use it.
- `Travel Agent/backend/api/routes/invites.py:883-889` rejects non-redeemable invites before checking whether the same authenticated user is already a member.
- `Travel App/app/invite/[slug].tsx:152-164` treats only status `409` as "already a member"; it surfaces non-409 errors.
- `Travel Agent/tests/api/test_invites_api.py:719-735` only covers "already member while invite is still redeemable."
- `Travel Agent/tests/api/test_invites_api.py:743-757` asserts a consume race returns `410`, which is correct for another redeemer but not for the same-user retry.

Why it matters to a real tester:

The first dogfood acquisition loop is "tap invite, join trip." On flaky mobile networks, the backend can add the user and consume the single-use token, but the client may never receive the 200. The retry then sees a consumed invite and shows "expired/not redeemable" even though the user actually joined. That creates a scary first impression and likely support/debug churn.

Repro / deterministic test idea:

1. Simulate accept call A adding `actor.id` to the trip and consuming the invite, but dropping the response.
2. Retry POST `/api/invites/{token}/accept` with the same authenticated user and same idempotency key.
3. Expected: 200 with the existing membership and trip id.
4. Current likely result for a consumed single-use invite: 410 before membership is checked.

Suggested fix direction:

Honor `X-Idempotency-Key` on accept, or reorder same-user membership recovery before the redeemability failure for consumed invites. Distinguish "already consumed by this actor" from "consumed by someone else." Update the frontend only after backend semantics are clear; do not broadly treat all 410s as success.

Confidence: Medium-high.

### P1 — Destination-created trips lose their destination after the real backend refetch

References:

- `Travel App/app/(tabs)/discover/index.tsx:457-473` creates a new trip from a destination card with `{ title: destination, destination }` and routes to a destination-shaped chat prefill.
- `Travel App/context/TripContext.tsx:262-279` stores `options.destination` only in the optimistic local `trip_summary`.
- `Travel App/context/TripContext.tsx:302-304` sends only `{ created_by, title }` to `api.createTrip`; destination, dates, and place identity are not persisted.
- `Travel Agent/backend/api/routes/trips.py:83-91` supports structured create fields such as `place_id`, `start_date`, and `end_date`, but not a plain destination string or `trip_summary.destination`.
- `Travel App/context/TripContext.tsx:167-174` replaces local trip state with the backend result on refetch, preserving travelers only.
- `Travel App/components/for-this-trip/ForThisTripPreview.tsx:68-107` hides the preview entirely when `trip_summary.destination` cannot become a slug.
- `Travel App/app/(tabs)/trips/[tripId]/for-this-trip.tsx:69-77` and `:125-132` fall back to destinationless placeholder behavior.

Why it matters to a real tester:

The product docs say the next phase is surfacing the built content graph. A tester who taps "Plan similar to Lisbon" should see a Lisbon-shaped trip. Instead, the destination exists only optimistically and can disappear after the trips query refetches, disabling "For this trip" destination rails and making the concierge/chat state feel disconnected from the trip object.

Repro / deterministic test idea:

In a real-backend test, call the same flow as `handlePlanSimilar("Lisbon")`, wait for the trips query invalidation/refetch, then assert the resulting trip still has a destination/place slug sufficient for `ForThisTripPreview` to render. The test should fail if destination only appears before the backend response lands.

Suggested fix direction:

Choose one canonical persistence path for destination creation: pass a resolved `place_id`, add a backend-supported destination field that populates `trip_summary.destination`, or promote the conversation intent scratchpad into trip state before routing. Then add a mock/real parity test around "Plan similar" so mock mode cannot mask the persistence gap.

Confidence: Medium.

## Positive Signals

- The generated OpenAPI contract is in sync with frontend generated types.
- Frontend HTTP call sites are covered by the OpenAPI snapshot.
- Mock/real parity and golden-path deterministic suites pass.
- Proposal review now invalidates proposal, chat, itinerary, map, and plan-state read models together in `Travel App/components/trip/ProposalReviewSheet.tsx:179-184`, which directly supports the Home/Plan/Map coherence goal.

## Dogfood Gate Recommendation

Do not invite external or semi-external dogfood testers until the P0s are closed. The deterministic core is in better shape than the deployment/privacy surface: tests pass, but the current invite privacy behavior and unreachable release hosts would break trust before the product can prove its concierge value.
