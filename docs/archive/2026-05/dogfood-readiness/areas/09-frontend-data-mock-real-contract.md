# Area Audit: Frontend Data Hooks, Mock/Real Parity, API Contract

Date: 2026-05-21  
Agent: Codex/Cursor Cloud audit session  
Scope: `Travel App` data hooks, `utils/api/{http,mock,interface,types,schema.gen}.ts`, app/component API imports, mock fixtures, workspace OpenAPI snapshot, API coverage tooling, release mock/auth guards.  
Mode: Audit only. No product-code changes.

## Executive Summary

- Dogfood risk: Medium
- Highest-risk finding: Narration audio uses `HEAD` from the app, but the backend route and OpenAPI contract only expose `GET`, so cached audio can be silently treated as unavailable.
- Checks run: `make contract-check` -> pass; `make api-coverage-check` -> pass; `make mock-real-parity` -> pass; `npm run api-boundaries` -> pass; targeted backend route probe for narration audio `HEAD` -> confirmed 405.
- Residual uncertainty: I did not run broad Jest or Expo UI tests beyond the requested parity gate; direct fetch call sites were statically inspected against OpenAPI, not exercised end-to-end with a running backend.

## Findings

### P1 — Narration audio preflight uses HEAD against a GET-only backend route

Status: Confirmed  
User impact: A dogfood user may see narration text but never get the cached audio affordance, because the mobile hook treats the `HEAD` probe's 405 as "no audio cached" even when a later `GET` could stream the MP3. This is especially risky because cache miss is intentionally silent.  
Product promise affected: Mock/real parity, voice/narration trust, API boundary correctness

References:

- `Travel App/hooks/useNarrationAudio.ts:192` — `loadFromCache()` probes the audio URL with `method: 'HEAD'`.
- `Travel Agent/backend/api/routes/narration.py:586` — backend registers the narration audio endpoint with `@router.get(...)` only.
- `docs/openapi.json:7908` — OpenAPI snapshot exposes `GET /api/trips/{trip_id}/narration/audio/{entity_type}/{entity_id}` and no `HEAD` operation.

Why it matters:

Voice/narration is already labeled high-drift-risk, and this path fails quietly by design: `!check.ok` sets `hasAudio=false`. Mock mode cannot reveal the mismatch because it does not issue this real HTTP preflight.

Repro or deterministic test idea:

1. From `Travel Agent`, run:
   `PYTHONPATH=. python - <<'PY' ... TestClient(app).head('/api/trips/00000000-0000-4000-8000-000000000001/narration/audio/venue/1') ... PY`
2. Observed during audit: status `405`, `Allow: GET`.
3. Expected: either `HEAD` is explicitly supported for this endpoint, or the app uses a contract-listed method.
4. Add a backend TestClient test asserting `HEAD` behavior if the app keeps the probe.

Suggested fix direction:

Either add an explicit backend `HEAD` route for the audio cache existence check, sharing the same auth/cache logic without streaming bytes, or change the frontend preflight to a contract-supported `GET` strategy. Then extend API coverage to include raw `fetch()` call sites outside `utils/api/http.ts`.

Related bug class:

Uncovered direct HTTP method drift

Confidence: High

### P2 — Venue detail still uses a hand-maintained backend mirror, and the mock omits required real fields

Status: Confirmed  
User impact: Venue detail currently renders through defensive UI defaults, but new code using `api.getVenueDetail()` in mock mode can believe the response shape is valid while required real fields are absent. Future backend field changes would not fail the generated-type contract at this call site.
Product promise affected: Generated contract truth, mock-real payload parity

References:

- `Travel App/utils/api/types.ts:517` — comment says no generated schema exists and keeps `APIVenueDetail` hand-written.
- `docs/openapi.json:33459` — `VenueDetailResponse` now exists in the committed schema.
- `Travel App/utils/api/http.ts:972` — real `getVenueDetail()` returns `_request<APIVenueDetail>(...)` instead of the generated `VenueDetailResponse`.
- `Travel App/utils/api/mock.ts:1150` — mock `getVenueDetail()` casts an object to `APIVenueDetail`.
- `Travel App/utils/api/mock.ts:1152` — mock object omits required schema fields `avg_duration_minutes`, `reservation_required`, and `wheelchair_accessible`.
- `Travel App/data/venues.ts:21` — adapter maps the API venue shape into richer UI-only `VenueDetail` defaults.

Why it matters:

The workspace contract says backend-shaped types should be generated or derived. This one has become stale: the OpenAPI schema now has the exact response model, but the frontend still preserves a handwritten copy and a mock cast that bypasses structural checking.

Repro or deterministic test idea:

1. Compare `components['schemas']['VenueDetailResponse']` in `schema.gen.ts` to `APIVenueDetail`.
2. Add a type-level or runtime mock test that `mockApi.getVenueDetail()` returns every required key from `VenueDetailResponse`.
3. Current likely/observed: the mock returns no `avg_duration_minutes`, `reservation_required`, or `wheelchair_accessible`.

Suggested fix direction:

Alias `APIVenueDetail` to `components['schemas']['VenueDetailResponse']`, remove the obsolete TODO, and make the mock object satisfy the generated type without `as APIVenueDetail`.

Related bug class:

Handwritten backend mirror / mock payload drift

Confidence: High

### P2 — API boundary guard passes while component escape hatches and a dynamic API import remain

Status: Confirmed  
User impact: Existing component-level API calls can keep data fetching, mutation behavior, optimistic cache updates, and error handling outside the `data/` bridge. That makes it easier for mock mode to pass while real-mode loading, auth, or cache invalidation behaves differently.
Product promise affected: API boundary rules, mock-real behavior parity

References:

- `Travel App/scripts/check-api-boundaries.mjs:5` — scans `app` and `components`.
- `Travel App/scripts/check-api-boundaries.mjs:10` — allowlists 10 existing component escape hatches.
- `Travel App/scripts/check-api-boundaries.mjs:41` — parser only handles static imports, not dynamic `import(...)`.
- `Travel App/components/auth/SignUpImpl.tsx:211` — dynamic `await import('../../utils/api')` pulls `api.getMe()` directly and is not caught by the boundary script.
- `Travel App/components/discover/ExperienceDetailSheet.tsx:19` and `Travel App/components/trip/ProposalReviewSheet.tsx:33` — representative allowlisted static component imports of raw `api`.
- `Travel App/eslint.config.js:68` — ESLint enforces the raw-API restriction only for `app/**/*`, not components.

Why it matters:

No `app/` screen statically imports `{ api }` directly, which is good. But the component layer still has 10 declared raw-API exceptions plus one dynamic import that the boundary script misses. The custom guard is useful, but because it is allowlist-based and not part of `make mock-real-parity`, this debt can persist without showing up in the main reliability ladder.

Repro or deterministic test idea:

1. Run `cd "Travel App" && npm run api-boundaries`.
2. Observed during audit: pass, "10 existing component escape hatches allowlisted."
3. Run `rg -n "import\\([^)]*utils/api|\\bapi\\b" Travel\ App/components --glob '*.{ts,tsx}'`.
4. Current observed: direct component API imports remain, and `SignUpImpl.tsx` dynamic import is not reported by the script.

Suggested fix direction:

Promote `npm run api-boundaries` into `make mock-real-parity` or `offline-qa`, teach it to catch dynamic imports, and shrink the allowlist by moving component fetch/mutation logic behind `data/` or dedicated hooks.

Related bug class:

Data-boundary escape hatch / lint coverage gap

Confidence: High

## Non-Findings / Things Ruled Out

- `schema.gen.ts` matches the workspace `docs/openapi.json`; `make contract-check` passed.
- `http.ts` call sites are covered by OpenAPI; `make api-coverage-check` reported 175/175 covered and 0 drift.
- Static screen imports do not call `{ api }` directly from `utils/api`; the direct runtime API calls I found are in components, hooks, context, and data modules.
- Release builds are guarded against mock/skip-auth leakage: `app/_layout.tsx` hard-fails non-dev builds when mock or skip-auth is true, and `utils/api/index.ts` gates `SKIP_AUTH` behind `__DEV__`.
- Mock mode has useful latency and fault-injection hooks: `_MOCK_LATENCY_MS` defaults to 120ms, and `EXPO_PUBLIC_MOCK_FAULTS` covers invite substance, in-flight send, and consumed-invite paths.
- Raw direct fetch call sites found during audit currently map to committed OpenAPI paths: SSE stream endpoints, `/api/events`, receipt image GET, and narration audio GET. The narration audio `HEAD` method is the exception above.

## Suggested Follow-Up Checks

- Add raw `fetch()`/`BASE_URL` scanning to `scripts/api-coverage-check.py`, or ban raw fetch outside `utils/api/http.ts` and `utils/sse.ts` with explicit allowlisted exceptions.
- Add a generated-schema conformance test for selected `mockApi` responses, starting with `getVenueDetail()`.
- Include `npm run api-boundaries` in `make mock-real-parity` so the main parity gate also protects the data bridge.
- Add a backend TestClient check for `HEAD /api/trips/{trip_id}/narration/audio/{entity_type}/{entity_id}` if the frontend keeps using HEAD.
