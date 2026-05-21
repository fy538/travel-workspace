# Area Audit: Backend Auth, Security, And Rate Limits

Date: 2026-05-21  
Agent: Codex (Cursor Cloud audit role)  
Scope: `Travel Agent/backend/api` routes, auth/service-auth/rate-limit helpers, upload/media routes, route-auth lint, selected API/security tests, reliability/product docs listed in the prompt.  
Mode: Audit only. No product-code changes.

## Executive Summary

- Dogfood risk: High
- Highest-risk finding: A public no-auth angle browse endpoint accepts arbitrary `user_id` and uses that user's Personal Memory to generate `why_for_you` personalization, leaking private preference signal and spending LLM tokens.
- Checks run: `PYTHONPATH=. python scripts/check_route_auth.py` -> pass; `PYTHONPATH=. pytest tests/api/test_route_auth_coverage.py -q` -> pass; `make contract-check` -> pass; `PYTHONPATH=. pytest tests/api/test_auth.py tests/api/test_trip_photos.py tests/api/test_voice_api.py -q` -> pass.
- Residual uncertainty: I did not run DB-backed integration tests or live provider/LLM paths. Findings are static-confirmed from route code and deterministic lint/test coverage.

## Findings

### P1 — Public Angle Browse Leaks Personal Memory Personalization

Status: Confirmed  
User impact: Anyone who can guess or obtain a user UUID can call the public angle endpoint with `?user_id=<uuid>` and receive `why_for_you` strings/ranking derived from that user's Personal Memory. This can expose private tastes, constraints, past travel signal, or sensitive preference themes in a public content response. It also lets unauthenticated traffic trigger LLM spend.  
Product promise affected: privacy / concierge trust / LLM spend

References:

- `Travel Agent/backend/api/routes/angles.py:254` — route is explicitly documented as no-auth public content browsing.
- `Travel Agent/backend/api/routes/angles.py:256` — `user_id` is accepted as an unauthenticated query parameter.
- `Travel Agent/backend/api/routes/angles.py:285` — any supplied `user_id` triggers personalization.
- `Travel Agent/backend/api/routes/angles.py:404` — loads `get_latest_personal_memory(user_id)` for that arbitrary UUID.
- `Travel Agent/backend/api/routes/angles.py:418` — sends the memory-derived prompt through `personalize_angles`.
- `Travel Agent/backend/core/personalization/angle_rank.py:87` — prompt includes raw Personal Memory markdown.
- `Travel Agent/backend/core/personalization/angle_rank.py:92` — personalization calls `call_llm_json`.

Why it matters:

Private input to group-safe context is a golden path. This endpoint bypasses both "self" auth and group-safe redaction by letting a public caller ask the backend to interpret a user's memory against public place angles. Even if the raw markdown is not returned, the generated `why_for_you` can reveal private underlying facts.

Repro or deterministic test idea:

1. In `tests/api/test_angles_api.py`, patch `get_latest_personal_memory` to return markdown like `Avoids seafood because of a severe shellfish allergy`.
2. Patch `personalize_angles` to assert it receives that markdown and return a `why_for_you` containing the private signal.
3. Call `GET /api/places/lisbon/angles?user_id=<victim_uuid>` without auth.
4. Expected: public route should ignore `user_id`, require auth/self for personalization, or return only editorial content.
5. Current observed from code: route loads the victim memory and returns personalized overlays.

Suggested fix direction:

Remove `user_id` from the public route. If personalized angle browsing is needed, make a separate authenticated route that derives `user_id` from `get_current_user` and applies `check_rate_limit`. Keep the public endpoint strictly editorial.

Related bug class:

private-data leak / noauth route with user-scoped personalization / LLM rate-limit bypass

Confidence: High

### P1 — Trip Photo Learning Opt-In Lets One Member Opt In Everyone's Shared Photos

Status: Confirmed  
User impact: A single trip member can call the learning opt-in endpoint and convert every `group` photo on the trip to `group_and_learn`, including photos uploaded by other members. Those other members consented to group visibility, not necessarily memory/learning use.  
Product promise affected: privacy / consent / memory trust

References:

- `Travel Agent/backend/api/routes/trip_photos.py:308` — member-authenticated route for `/api/trips/{trip_id}/photos/opt-in-learning`.
- `Travel Agent/backend/api/routes/trip_photos.py:316` — route describes bulk-upgrading all group-visible photos.
- `Travel Agent/backend/api/routes/trip_photos.py:318` — docstring frames the call as "a user consents".
- `Travel Agent/backend/api/routes/trip_photos.py:325` — handler calls `_bulk_opt_in_learning` with only `trip_id`.
- `Travel Agent/backend/api/routes/trip_photos.py:485` — update filters by `trip_id`, `visibility == "group"`, and not deleted.
- `Travel Agent/backend/api/routes/trip_photos.py:491` — update sets all matching rows to `group_and_learn`; uploader is not constrained.

Why it matters:

The product promise depends on private and semi-private signals being used only with the right scope. "Group-visible image" and "can be learned from for memory/taste" are different consents. This route collapses them for the whole group.

Repro or deterministic test idea:

1. Insert two `trip_photos` rows for the same trip: one uploaded by actor A, one by actor B, both `visibility="group"`.
2. Authenticate as actor A and call `POST /api/trips/{trip_id}/photos/opt-in-learning`.
3. Expected: only actor A's photos change, or the route requires organizer/admin plus explicit group policy.
4. Current observed from code: both A and B rows match the update.

Suggested fix direction:

Scope the update to `uploaded_by_user_id == actor.id`, or replace the route with explicit per-photo/per-user consent state. Add a regression test with mixed uploaders.

Related bug class:

ownership/consent-scope bug

Confidence: High

### P2 — Cost-Sensitive Routes Escape Rate Limits Because The Static Gate Only Sees Direct Helper Calls

Status: Confirmed  
User impact: Authenticated dogfood users can repeatedly hit several routes that trigger LLM, embedding, Qdrant, provider, or background-agent work without a server-side rate-limit check. A compromised dogfood token or buggy client loop can create spend/latency spikes even though `check_route_auth.py` passes.  
Product promise affected: LLM spend / provider-cost controls / dogfood stability

References:

- `Travel Agent/scripts/check_route_auth.py:22` — lint intends every LLM/agent/embedding route to call `check_rate_limit`.
- `Travel Agent/scripts/check_route_auth.py:61` — trigger list is name-based and misses wrapper functions like `personalize_angles`, `score_cold_angles`, `experience_fan_out_search`, and `get_booking_graph`.
- `Travel Agent/scripts/check_route_auth.py:326` — scan only covers `backend/api/routes/*.py`, not app-level routes in `main.py`.
- `Travel Agent/backend/api/routes/users/insights.py:262` — `GET /api/users/{user_id}/for-you` has auth/self but no `check_rate_limit`.
- `Travel Agent/backend/api/routes/users/insights.py:341` — for-you route can call `personalize_angles`.
- `Travel Agent/backend/api/routes/users/insights.py:356` — for-you route can call `score_cold_angles`.
- `Travel Agent/backend/api/routes/trips.py:1074` — `GET /api/trips/{trip_id}/experiences` has no `check_rate_limit`.
- `Travel Agent/backend/api/routes/trips.py:1128` — `ranked=true` path calls `experience_fan_out_search`.
- `Travel Agent/backend/planning_agent/experience_fan_out_search.py:76` — helper documents each call as Haiku + embedding + Qdrant work with no caching.
- `Travel Agent/backend/planning_agent/experience_fan_out_search.py:104` — helper calls `call_llm_json`.
- `Travel Agent/backend/planning_agent/experience_fan_out_search.py:132` — helper calls `generate_embeddings`.
- `Travel Agent/backend/api/routes/booking.py:86` — `POST /api/trips/{trip_id}/booking/sessions` has membership but no rate limit.
- `Travel Agent/backend/api/routes/booking.py:126` — route launches the booking graph in the background.
- `Travel Agent/backend/booking_agent/agents/booking_graph.py:41` — booking graph wrapper calls core `call_llm_json`.
- `Travel Agent/backend/api/routes/users/phone.py:121` — phone verification explicitly documents no server-side rate limit beyond Twilio.
- `Travel Agent/backend/api/routes/users/phone.py:160` — phone verification dispatches SMS.

Why it matters:

The existing `check_route_auth.py` passing is a false sense of coverage for indirect spend paths. The dogfood product has several "personalized feed" and "ranked recommendations" surfaces that feel harmless as GETs but can spend model and embedding budget.

Repro or deterministic test idea:

1. Add a route-lint fixture where a handler calls `personalize_angles`, `experience_fan_out_search`, or `get_booking_graph().ainvoke(...)` without `check_rate_limit`.
2. Expected: lint fails with `llm_no_rate_limit`.
3. Current observed: `PYTHONPATH=. python scripts/check_route_auth.py` reports 0 violations.
4. Add targeted API tests that monkeypatch these helpers and assert repeated calls hit 429 after the configured cap.

Suggested fix direction:

Add explicit scopes for `personalization`, `ranked_experiences`, `booking_session`, `sms_verification`, and `upload`. Extend `check_route_auth.py` to include known wrapper names or, better, tag cost-sensitive route functions with a decorator/metadata that the lint can enforce.

Related bug class:

rate-limit gap / static-lint blind spot / indirect LLM/provider spend

Confidence: High

### P2 — Upload And Rehost Endpoints Are Bounded By Type/Size But Not Rate-Limited

Status: Confirmed  
User impact: Any authenticated trip member can repeatedly trigger image rehosting, multipart photo processing, and receipt upload/OCR enqueue work. Size/type checks reduce per-request blast radius, but there is no per-user upload rate/cost gate.  
Product promise affected: upload limits / provider-cost controls / dogfood stability

References:

- `Travel Agent/backend/api/routes/trip_photos.py:74` — source-URL trip photo upload route.
- `Travel Agent/backend/api/routes/trip_photos.py:91` — source URL path calls `rehost`, which downloads/processes/uploads image variants.
- `Travel Agent/backend/api/routes/trip_photos.py:134` — multipart trip photo upload route.
- `Travel Agent/backend/api/routes/trip_photos.py:156` — validates MIME type before processing.
- `Travel Agent/backend/api/routes/expenses.py:634` — receipt upload route.
- `Travel Agent/backend/api/routes/expenses.py:665` — validates MIME type.
- `Travel Agent/backend/api/routes/expenses.py:670` — reads the full upload content before checking size.
- `Travel Agent/backend/api/routes/expenses.py:673` — enforces 15 MB after read.

Why it matters:

The prompt's upload-limit question is mostly satisfied for individual files, but repeated uploads remain a cheap storage/CPU/OCR pressure path during dogfood. Receipt upload additionally enqueues OCR work after accepting the file.

Repro or deterministic test idea:

1. Patch `rehost`, `rehost_from_bytes`, or `enqueue(process_receipt_ocr)` to avoid real provider calls.
2. Send N upload requests as the same user.
3. Expected: after a reasonable cap, responses return 429 and no processing/enqueue happens.
4. Current observed from code: there is no `check_rate_limit` call in these handlers.

Suggested fix direction:

Add an `upload` or per-surface scope to `rate_limits.py`, call it before expensive processing, and add a lint/test rule for routes using `UploadFile` or `rehost`. Where practical, reject oversize multipart requests using request/content-length or streaming reads before loading the whole file into memory.

Related bug class:

upload rate-limit gap / resource-exhaustion

Confidence: High

### P3 — Background Task Health Exposes Internal Task Names And Error Strings Publicly

Status: Confirmed  
User impact: Anyone who can reach the backend can see which background loops are enabled/running and any exception strings from completed tasks. This is less severe than token/cost/debug endpoints, but it is still debug-internal surface area.  
Product promise affected: debug internals

References:

- `Travel Agent/backend/api/main.py:270` — `/health/background-tasks` is public.
- `Travel Agent/backend/api/main.py:281` — reads task exceptions.
- `Travel Agent/backend/api/main.py:283` — returns raw `str(exc)` in the response.
- `Travel Agent/backend/api/main.py:294` — `/debug/tokens` is admin-gated, showing the intended pattern for sensitive operational data.

Why it matters:

The route does not expose user data by design, but background loop names and exception messages can reveal operational internals and dependency failures. If an exception includes hostnames, provider names, or malformed payload fragments, the response becomes a public debug leak.

Repro or deterministic test idea:

1. In a test app, set `app.state.background_tasks` to a completed task that raised `RuntimeError("provider X failed with detail Y")`.
2. Call `/health/background-tasks` without `X-Service-Token`.
3. Expected: public health returns coarse status only, or detailed task/error view requires admin token.
4. Current observed from code: detailed task map and error string are returned.

Suggested fix direction:

Keep `/health` and `/ready` public, but gate `/health/background-tasks` with `require_admin_token` or return only aggregate counts publicly and move detailed errors to an admin endpoint.

Related bug class:

debug/admin gate gap

Confidence: Medium

## Non-Findings / Things Ruled Out

- Main debug token/cost endpoints are admin-gated: `/debug/tokens` and `/debug/cost` both use `Depends(require_admin_token)`.
- `/metrics/tokens` is admin-gated at router level with `Depends(require_admin_token)`.
- `/admin/*` and `/api/curator/photos` are gated with service tokens and deny by default when env vars are absent.
- Webhook routes are documented no-auth but verify Bland/Twilio signatures inline and reject when secrets are unset.
- `SKIP_AUTH` defaults false, and startup validation rejects `SKIP_AUTH=true` in prod-like environments and requires `CLERK_JWKS_URL` when auth is enabled.
- Trip photo list hides GPS from non-owners in response projection.
- Existing deterministic checks passed: route-auth lint, per-trip mutation membership coverage, contract check, and selected auth/photo/voice API tests.

## Suggested Follow-Up Checks

- Add a regression test that unauthenticated `GET /api/places/{slug}/angles?user_id=...` does not call `get_latest_personal_memory` or `personalize_angles`.
- Extend route-auth lint to cover app-level routes in `backend/api/main.py`.
- Extend rate-limit lint triggers to include wrapper functions: `personalize_angles`, `score_cold_angles`, `experience_fan_out_search`, `get_booking_graph`, `rehost`, `rehost_from_bytes`, `UploadFile`, and SMS dispatch helpers.
- Add mixed-uploader trip photo tests for `opt-in-learning`.
- Add per-user rate-limit tests for for-you, ranked trip experiences, booking session creation, phone verification, trip photo upload, and receipt upload.
