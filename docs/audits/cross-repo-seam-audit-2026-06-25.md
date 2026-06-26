# Cross-Repo Seam / Contract Audit — 2026-06-25 v2

Repos: `travel-agent` (Python/FastAPI backend) ↔ `travel-app` (Expo/React Native frontend)
Seam chain: **BE handlers → `docs/openapi.json` → `schema.gen.ts` (generated) → `types.ts` (hand-written) → `interface.ts` (typed client) → `http.ts` → `mock/*.ts`**
Verification posture: every confirmed finding cleared an adversarial stage whose default verdict was **refute**.

**Coverage:** Full — 13 domains across two passes (7 domains in pass 1, 6 domains in pass 2; 6 domains were rate-limited during the initial fan-out and re-audited separately).

> **v2 context:** This audit ran after v1 (same day) fixed 10 bugs and added 4 automated ratchets. The ratchets are working within their defined scopes; residual findings cluster in gaps the ratchets don't yet cover.

---

## 1. TL;DR

The ratchet layer from v1 is holding: none of the v1 fixes regressed, and the three new ratchets (`check_event_type_parity.py`, `check_response_model_floor.py`, `check_fe_dead_client.sh`) confirmed clean in their domains. The **headline new finding is `settleBookingHold` sending no body — every pay-later hold confirmation fails with HTTP 422 in production**; this is a single-line fix in `http.ts`. Two more production-affecting bugs: `getAtlasFacets` returns `suggestions` but the FE reads `facets` (compose chips always empty), and `getVenueDossier` fetches a list but the FE casts it as a detail (venue editorial block always blank).

24 confirmed findings total; 4 high, 9 med, 11 low. The 9 med/11 low findings are correctness/observability/dev-experience debt with no data loss or hard crash.

---

## 2. Confirmed Findings — Full Table

| # | Sev | Domain | Seam | Title | BE loc | FE loc |
|---|-----|--------|------|-------|--------|--------|
| 1 | **HIGH** | booking | error-contract | `settleBookingHold` sends no body → always 422; hold confirmation is broken | `booking.py:568-588` | `http.ts:1631-1635` |
| 2 | **HIGH** | atlas | shape-drift | `getAtlasFacets`: BE field `suggestions`, FE reads `facets` → chips always empty | `atlas.py:690` | `types/atlas.ts:405-407`, `data/atlas.ts:434` |
| 3 | **HIGH** | discover | shape-drift | `getVenueDossier`: BE returns `DossierListResponse`, FE casts as `DossierDetail` → editorial blank | `dossiers.py:575` | `http.ts:2035`, `app/venue/[venueId]/index.tsx:132,420,550` |
| 4 | **HIGH** | discover | mock-drift | `getVenueDossier` mock returns `DossierDetail`, real BE returns `DossierListResponse` — masks #3 | `dossiers.py:575` | `mock/discover.ts:874-895` |
| 5 | med | booking | error-contract | `settleBookingHold` 410 `hold_expired` swallowed as generic toast | `booking.py:605-612` | `hooks/useBookingDecision.ts:66-69` |
| 6 | med | trips | shape-drift | `decommitTrip` typed `Promise<void>` but BE returns `{trip_id, conversation_id}` — freed thread invisible | `trips.py:538-567` | `interface.ts:1565`, `http.ts:2066-2068` |
| 7 | med | notifications | enum-drift | `story_ready` archetype missing from `homeCardRoute` — tap routes to Discover instead of Trip Story | `home/cards.py:559-567` | `utils/homeCardRoutes.ts`, `data/home.ts:56-72` |
| 8 | med | social | mock-drift | Social feed mock uses `'saved_venue'`/`'trip_created'` — wrong `event_type` values; feed empty in dev | `api/routes/events.py:36` | `mock/social.ts:629,642,655,668` |
| 9 | med | experiences | enum-drift | `ExperienceDetailSheet` branches on `availability === 'always'`; BE emits `'on_demand'` | `_tables/experiences.py:117` | `ExperienceDetailSheet.tsx:375` |
| 10 | med | memory | shape-drift | `createVoiceToken` body still sends removed fields `user_id`/`user_role` (removed post-B1 audit) | `voice.py` (VoiceTokenRequest) | `interface.ts:852-866`, `http.ts:1220-1236` |
| 11 | med | users-auth | shape-drift | `postUserHeartbeat` request body missing Phase-7.3 presence fields (`trip_id`, `device_id`, `current_lat`, `current_lng`) | `heartbeat.py:52-89` | `interface.ts:789-797`, `http.ts:1196-1201` |
| 12 | med | expenses | mock-drift | Mock expense currency `'€'` (symbol) vs real BE `'EUR'` (ISO) → `formatCostAmount` renders differently | `expenses.py` | `constants/mocks/expenses.ts:28-93` |
| 13 | med | expenses | error-contract | 403 from expense update/delete/settle shows generic toast — no permission context | `expenses.py:316-416` | `hooks/useUpdateExpense.ts:58`, `useDeleteExpense.ts:42`, `useSettleShares.ts:40` |
| 14 | low | trips | mock-drift | Mock `getTripFolio` never returns `mode='cold'` — `ColdStartPanel` untestable in mock mode | `folio/read_model.py:936-955` | `mock/trips.ts:1163-1176` |
| 15 | low | social | missing-client | `GET /api/trips/{trip_id}/action-receipts/recent` has no FE client | `action_receipts.py:70-105` | `interface.ts` (absent) |
| 16 | low | plan-core | missing-client | `POST /api/plan-similar` has no FE client (FE uses concierge flow instead) | `plan_similar.py:42` | `interface.ts` (absent) |
| 17 | low | plan-core | missing-client | `GET /api/public/stories/{slug}/plan-seed` has no FE client (public, no-auth seed endpoint) | `plan_similar.py:32` | `interface.ts` (absent) |
| 18 | low | booking | missing-client | 4 booking endpoints have no FE client: readiness, travel-insurance affiliate, restaurant-attempts, retry | `booking.py:407-435` | `interface.ts` (absent) |
| 19 | low | memory | error-contract | `getTripStory`/`regenerateTripStory` catch 422 but BE never returns 422 for these paths (returns 202) | `memory.py:249` | `http.ts:2129-2138`, `http.ts:2151-2160` |
| 20 | low | memory | missing-client | `GET /api/trips/{trip_id}/geofence-events` has no FE client (organizer debug surface) | `voice_guide.py:177-216` | `interface.ts` (absent) |
| 21 | low | users-auth | shape-drift | `postUserHeartbeat` response missing `presence_recorded` field | `heartbeat.py:91-93` | `interface.ts:797`, `http.ts`, `mock/social.ts:218` |
| 22 | low | users-auth | openapi-drift | `AuditResponse.data_source` schema `@default v1_stub` is stale; BE always returns `'warehouse'` | `privacy_audit.py:309` | `schema.gen.ts:9622-9626` |
| 23 | low | expenses | missing-client | `GET /expenses/{expense_id}/comments` has no FE client | `expenses.py:584` | `interface.ts` (absent) |
| 24 | low | expenses | missing-client | `GET /expenses/suggest-category` re-exists on BE after client triple was removed in v1 | `expenses.py:204` | `interface.ts` (absent), `types.ts:1649` (type remains) |
| 25 | low | mechanical | shape-drift | Hand-typed `StayCandidate` in `types.ts` missing `freeform_lat`/`freeform_lng` fields | `trip_stay_candidates.py:35-36` | `types.ts:1450-1472` |

---

## 3. Detail: High and Medium Findings

### #1 — `settleBookingHold` sends no body → always 422 (**booking, error-contract, HIGH**)

The BE `POST /booking/holds/{offer_id}/settle` requires `{ terms_accepted: true, final_human_approval: true }`. If the body is absent or either flag is false, FastAPI raises a `ValidationError` (→ HTTP 422). `http.ts:1631-1635` sends a bare POST with no `body` key at all. Every call from `useBookingDecision.confirm({ kind: 'hold' })` receives a 422 and falls through to the generic `"Couldn't confirm that"` toast. The mock bypasses the body requirement entirely. **The pay-later hold confirmation flow is completely broken in production.**

**Fix:** In `http.ts` `settleBookingHold`, add `body: JSON.stringify({ terms_accepted: true, final_human_approval: true })`. `schema.gen.ts:17720` already has `SettleHoldRequest`. Update `interface.ts` signature to accept an optional body for future `correlation_id` support.

---

### #2 — `getAtlasFacets`: `suggestions` vs `facets` (**atlas, shape-drift, HIGH**)

`GET /api/atlas/facets` returns `{ "generated_at": ..., "suggestions": [...] }` (BE model `AtlasFacetSuggestions`). The FE hand-typed `AtlasFacetsResult` with field `facets`. `data/atlas.ts:434` reads `data?.facets` → always `undefined` in production. The compose surface at `app/atlas/compose.tsx:63` always sees `[]`. Recognition-first suggestion chips **never render in production**. The mock returns `{ facets: [...] }` matching the wrong FE type — the bug is invisible in dev mode.

**Fix:** Rename `AtlasFacetsResult.facets` → `suggestions` in `types/atlas.ts` and update `data/atlas.ts:434`. Fix mock `_buildAtlasFacets()` to emit `suggestions` not `facets`.

---

### #3 + #4 — `getVenueDossier`: list vs detail shape mismatch (**discover, shape-drift + mock-drift, HIGH**)

`GET /api/dossiers/venue/{venue_id}` is declared `response_model=DossierListResponse` (`{ items: DossierSummary[], count: int }`). `http.ts:2035` casts the response as `APIDossier` (`DossierDetail`). `DossierSummary` has no `content`, `place_slug`, or `city_slug`. `app/venue/[venueId]/index.tsx:132,420,550-553` reads all three — all return `undefined`. The "ABOUT THIS PLACE" editorial block is **silently blank for every venue in production**. The neighborhood breadcrumb link is always suppressed. No crash because all accesses use optional chaining. The mock returns a fully populated `DossierDetail` as `as APIDossier`, masking the bug completely.

**Fix (Option A):** Add a dedicated BE endpoint `GET /api/dossiers/venue/{venue_id}/primary` returning `DossierDetail` directly. **(Option B, less invasive):** In `http.ts`, fetch the list, take `items[0].id`, then fetch `/api/dossiers/{id}` for the full detail. After either fix, remove `as APIDossier` from the mock and align mock shape with the fixed response.

---

### #5 — `settleBookingHold` 410 `hold_expired` swallowed (**booking, error-contract, med**)

When the hold deadline pre-check fires, BE raises `HTTPException(status_code=410, detail={'code': 'hold_expired', 'offer_id': ...})`. The `onError` handler in `useBookingDecision.ts:66-69` shows a generic toast for all errors. HTTP 410 maps to `kind='unknown'` in `http.ts`'s `_kindFromStatus`. A user whose hold has expired sees "Couldn't confirm that" with no guidance to rebook.

**Fix:** In `useBookingDecision.ts` `onError`: `if (err instanceof APIError && err.status === 410)` → `toast?.error('Hold has expired — the reservation is no longer available.')`. Add `410: 'expired'` to `_kindFromStatus` in `http.ts`.

---

### #6 — `decommitTrip` typed `Promise<void>` (**trips, shape-drift, med**)

BE returns `DecommitResponse(trip_id, conversation_id: UUID | None)` — the freed planning thread. `interface.ts:1565` and `http.ts:2066-2068` type/implement as `Promise<void>`, silently discarding the payload. `TripContext.tsx:407` can only invalidate caches; it cannot navigate to the freed conversation without a second API call.

**Fix:** Change to `Promise<{ trip_id: string; conversation_id: string | null }>` in `interface.ts` and `http.ts`. Update `TripContext.tsx:407` to optionally navigate to the freed conversation.

---

### #7 — `story_ready` missing from `homeCardRoute` (**notifications, enum-drift, med**)

BE emits `archetype='story_ready'` when a composed Trip Story exists. `homeCardRoute` has no `case 'story_ready'` and falls through to `default: routes.discover()`. A user tapping "Your story is ready" on the home feed lands on **the Discover tab** instead of `routes.tripStory(ctx.tripId)`. `HomeCardArchetype` union in `data/home.ts` also omits the value, so TypeScript provides no guard.

**Fix:** Add `case 'story_ready': return ctx.tripId ? routes.tripStory(ctx.tripId) : routes.discover()` in `homeCardRoutes.ts`. Add `'story_ready'` to `HomeCardArchetype` union in `data/home.ts`.

---

### #8 — Social feed mock wrong `event_type` values (**social, mock-drift, med**)

`mock/social.ts` emits `event_type: 'saved_venue'`, `'trip_created'`, `'trip_completed'`. None are in `ALLOWED_EVENT_TYPES`; none match any case in `feedItemToActivity()`. All fall through to `default: return null`. In dev/mock mode the social activity feed (Me tab) and Discover social-proof cards **render completely empty**.

**Fix:** Replace `'saved_venue'` with `'venue_saved'` (lines 629, 655). Replace `'trip_created'`/`'trip_completed'` with handled values or add handler cases for those events.

---

### #9 — `ExperienceDetailSheet` `availability === 'always'` (**experiences, enum-drift, med**)

DB CHECK constraint and BE default both use `'on_demand'` for bookable-anytime experiences. `ExperienceDetailSheet.tsx:375` branches on `'always'` — the BE **never emits this**. The "Book anytime" label is never rendered for `on_demand` experiences. `utils/experienceDisplay.ts:47` correctly uses `'on_demand'`, confirming the intended value.

**Fix:** Change `=== 'always'` to `=== 'on_demand'` at `ExperienceDetailSheet.tsx:375`. One-line change.

---

### #10 — `createVoiceToken` sends removed fields (**memory, shape-drift, med**)

The B1 security audit removed `user_id` and `user_role` from `VoiceTokenRequest` — the BE now derives identity from the JWT. `schema.gen.ts` reflects this. But `interface.ts:852-866` still declares `{ user_id: string; user_name: string; user_role?: 'organizer' | 'member' }`, `http.ts:1220-1236` sends all three, and `useVoiceSession.ts:156-160` passes `user_id`/`user_role` explicitly. FastAPI ignores extra body fields (no validation error), so this is not a runtime failure — but the fields are dead weight and will cause confusion when new developers read them.

**Fix:** Update `interface.ts` body type to `{ user_name: string }`. Remove `user_id`/`user_role` from `http.ts` call and `useVoiceSession.ts`.

---

### #11 — `postUserHeartbeat` missing Phase-7.3 presence fields (**users-auth, shape-drift, med**)

`HeartbeatRequest` accepts `trip_id`, `device_id`, `current_lat`, `current_lng` to trigger the Phase-7.3 `live_trip_sessions` upsert. The FE interface only declares `{ active_in_chat, headphones_connected, motion, ambient_db }`. TypeScript prevents callers from passing presence context without a type assertion — the live-trip presence layer is silently inert on the FE side.

**Fix:** Extend `postUserHeartbeat` body type in `interface.ts` to include `trip_id?: string | null; device_id?: string | null; current_lat?: number | null; current_lng?: number | null`. Propagate to `http.ts` and mock.

---

### #12 — Mock expense currency `'€'` vs `'EUR'` (**expenses, mock-drift, med**)

All 10 mock expenses use `currency: '€'` (Unicode symbol). Real BE emits ISO codes (`'EUR'`). `formatCostAmount` (utils/costsViewModel.ts:251) branches on `currency.length <= 2` — symbol path produces `€192`; ISO path produces `EUR 192`. Developers see prefix-symbol format in dev; production users see ISO-code format. Inconsistency makes currency display bugs harder to catch in dev.

**Fix:** Replace all `currency: '€'` with `'EUR'` and `settlement_currency: '€'` with `'EUR'` in `constants/mocks/expenses.ts`.

---

### #13 — 403 from expense edit/delete/settle shows generic toast (**expenses, error-contract, med**)

BE returns HTTP 403 with a clear permission detail when a non-creator/non-organizer tries to edit or delete another member's expense. The `onError` handlers in `useUpdateExpense.ts`, `useDeleteExpense.ts`, and `useSettleShares.ts` catch all errors uniformly. `err.kind === 'forbidden'` is already set by `http.ts` for 403s — the hooks just don't use it. A non-payer sees "Couldn't save" with no indication that retrying won't help.

**Fix:** In all three hooks' `onError`: check `err instanceof APIError && err.kind === 'forbidden'` and show `"You don't have permission to edit/delete/settle this expense"`.

---

## 4. Systemic Patterns

**Pattern 1 — Hand-typed FE response shapes diverge from BE Pydantic models after changes.**
Findings #2, #3, #10, #11, #21, #25 all stem from a FE hand-typed interface not being updated when the BE model changed. `schema.gen.ts` is fresh and has the correct shape in every case — the bug lives in the hand-typed mirror. The `check_response_model_floor.py` ratchet ensures BE routes declare a `response_model`; it does not catch field-name or field-presence divergence between the declared model and FE counterparts. A linting step that diffs `types.ts` hand-typed interfaces against `schema.gen.ts`-generated equivalents would catch this class at CI time.

**Pattern 2 — Mocks paper over the bugs they should expose.**
Findings #4, #8, #12 involve mocks that return the FE-expected (wrong) shape rather than the BE-actual shape. In all three cases the mock was written using the hand-typed FE interface as ground truth — so dev mode and mock-mode tests pass while production silently fails. A mock-parity lint that validates mock return shapes against `schema.gen.ts` schemas would catch these before they reach production.

**Pattern 3 — Error-contract gaps remain at action boundaries.**
Findings #1, #5, #13, #19 are all places where the FE's `onError` handler (or no body at all) diverges from the BE's actual response path. `check_response_model_floor.py` guards the BE side; there is no equivalent FE-side check that `_request<T>` bodies and error handlers match the declared contract. The `test_enum_contracts.py` suite covers booking status and `trip_ended` — extending it to cover `settleBookingHold` body requirements and `hold_expired` 410 would have caught #1 and #5.

**Pattern 4 — Missing clients accumulate as BE features ship ahead of FE.**
10 of the 25 findings are `missing-client` or `dead-endpoint` (findings #15-#20, #23-#24). These represent completed BE work with no FE surface: `plan-similar`, `plan-seed`, booking readiness/affiliate/restaurant-attempts, geofence-events, action-receipts, expense comments, `suggest-category`. The `check_fe_dead_client.sh` ratchet catches dead clients (wired FE, no callers); it does not catch missing clients (no FE wiring at all). An API coverage check (all BE routes have a corresponding `interface.ts` method, or are explicitly allowlisted as DARK) would close this.

---

## 5. Uncertain / Noted (No Action Required)

| Domain | Item | Status |
|--------|------|--------|
| plan-core | `revertProposal` mock omits `revert_mode`/`revert_conflicts`; FE has null-guards so no crash | Mock fidelity gap; no runtime break |
| plan-core | `voteOnProposal` 409 `proposal_already_resolved` uses structured dict detail; FE rolls back without differentiated toast | Graceful degradation; no wrong state |
| booking | `POST /api/trips/{trip_id}/digest/email` has no FE client or UI | Intentionally dark (likely admin/Phase-N trigger); BE fully built |
| memory | `GET /api/trips/{trip_id}/geofence-events` — cannot confirm if admin-only or future organizer panel | Mark KNOWN-DARK until organizer panel ships |
| users-auth | `answer_then_resume` not explicitly handled in `decisionForInterruptionAction` | `continue_handoff` is the correct runtime path by voice gateway design |
| users-auth | `card_dismiss_undone` readable but never writable | Dead legacy alias; cleanup candidate |
| social | Mock `acceptInvite` fault uses `detail: 'invite_consumed'`; BE emits `{error: 'invite_not_redeemable', reason: ...}` | FE gates on `status === 410` only — no current bug; risk only if detail narrowing is added |
| notifications | `GET /api/events/users/{user_id}` has no FE client | Server-side pipeline consumption only; correct by design |
| expenses | `SuggestCategoryResponse` type remains in `types.ts:1649` after client triple was removed | Stale type; delete in next cleanup pass |
| discover | Stale comment in `types.ts:599-602` claims BE doesn't accept `entity_types`/`limit`/`offset` | Comment only; wire contract is correct |

---

## 6. Remediation Order

**Immediate — production-affecting, no feature flag needed:**

1. **#1 `settleBookingHold` missing body** — `http.ts:1631`. Add `body: JSON.stringify({ terms_accepted: true, final_human_approval: true })`. One-line fix; pay-later hold confirmation completely broken without it.

2. **#3+#4 `getVenueDossier` list vs detail** — add `/primary` endpoint on BE *or* chain list→fetch in `http.ts`. Fix companion mock. "ABOUT THIS PLACE" block is blank for every venue in production.

3. **#2 `getAtlasFacets` `suggestions` vs `facets`** — rename in `types/atlas.ts` + `data/atlas.ts:434` + mock. Compose suggestion chips are blank in production.

4. **#9 `ExperienceDetailSheet` `availability === 'always'`** — one line: `=== 'always'` → `=== 'on_demand'` at `ExperienceDetailSheet.tsx:375`.

5. **#7 `story_ready` missing from `homeCardRoute`** — add case + union value. Post-trip users tapping the home card land on Discover instead of their story.

**Near-term — dev experience / test fidelity:**

6. **#8 Social feed mock wrong `event_type`** — fix `'saved_venue'`→`'venue_saved'` in `mock/social.ts`. Social feed empty in every dev session.

7. **#12 Mock expense currency `'€'`→`'EUR'`** — three-char change across `constants/mocks/expenses.ts`.

8. **#5 `settleBookingHold` 410 swallowed** — add 410 branch in `useBookingDecision.ts` `onError`.

9. **#13 403 generic toast in expense hooks** — add `err.kind === 'forbidden'` branch in all three hooks.

10. **#10 `createVoiceToken` dead fields** — remove `user_id`/`user_role` from `interface.ts`, `http.ts`, `useVoiceSession.ts`.

11. **#11 `postUserHeartbeat` missing presence fields** — extend body type in `interface.ts`.

12. **#6 `decommitTrip` typed `Promise<void>`** — update `interface.ts`, `http.ts`, `TripContext.tsx`.

**Deferred — shape correctness, missing clients, test coverage:**

13. **#21 `postUserHeartbeat` response missing `presence_recorded`** — add field to interface/mock.
14. **#25 `StayCandidate` missing `freeform_lat`/`freeform_lng`** — add to `types.ts`.
15. **#14 Mock `getTripFolio` never returns `mode='cold'`** — add blank-trip detection in mock.
16. **#19 Dead 422 catch in story hooks** — remove stale catch blocks.
17. **#22 `AuditResponse.data_source` stale `@default`** — update Pydantic default; regenerate schema.
18. **#24 `suggest-category` re-exists** — either re-wire client or add a formal DARK comment + delete `SuggestCategoryResponse` from `types.ts`.
19. **#15-#18, #20, #23** Missing clients — prioritize by roadmap: plan-similar and plan-seed when "Plan something like this" ships; booking readiness when live checkout goes live; others as features reach FE.

---

## 7. What the Ratchets Caught / Confirmed

**`check_event_type_parity.py`:** Working in its domain. Did not catch #8 (social mock wrong `event_type`) because mock fixture files are outside its scope. Extending to validate mock `event_type` literals against `ALLOWED_EVENT_TYPES` would close this gap.

**`check_response_model_floor.py` (0 violations):** Confirmed every BE route declares a `response_model`. This is necessary but not sufficient — both `getAtlasFacets` and `getVenueDossier` have correct BE `response_model` declarations; the bugs live in FE hand-typed mirrors. A schema-diff step comparing `types.ts` against `schema.gen.ts` would make this ratchet sufficient for the shape-drift class.

**`check_fe_dead_client.sh`:** Confirmed no new dead clients since v1. The 10 missing-client findings (#15-#20, #23-#24, plus two plan-core) are **missing clients** (no FE wiring at all) — a distinct category from dead clients (wired but uncalled). An inverse check (all BE routes have an `interface.ts` method or an explicit DARK allowlist entry) would catch this class.

**`tests/api/test_enum_contracts.py` (6 tests, all passing):** Correctly locked in v1 fixes for `offer.status` and `trip_ended`. Findings #7 (`story_ready`) and #9 (`availability`) are enum-drift in domains not yet covered by this suite. Adding `HomeCardArchetype` and `ExperienceAvailability` contract tests would have caught both.

---

## 8. Domain Health Summary

| Domain | Health | Confirmed | Notes |
|--------|--------|-----------|-------|
| plan-core | minor-issues | 2 | Two missing-client endpoints; active plan flow clean |
| booking | needs-attention | 3 | #1 is active production break; hold confirmation completely broken |
| trips | minor-issues | 2 | `decommitTrip` void typing; mock cold-start gap |
| atlas | minor-issues | 1 | `getAtlasFacets` field name; active production break |
| discover | needs-attention | 2 | `getVenueDossier` shape + mock; venue editorial blank in production |
| concierge | **clean** | 0 | — |
| memory | minor-issues | 3 | Dead body fields; stale 422 catch; missing geofence client |
| expenses | minor-issues | 4 | Currency mock; 403 toast; two missing clients |
| social | minor-issues | 2 | Mock event_type; action-receipts missing client |
| notifications | minor-issues | 1 | `story_ready` routing |
| users-auth | minor-issues | 3 | Heartbeat fields; stale schema annotation |
| experiences-photos | minor-issues | 1 | Availability enum one-liner |
| mechanical | minor-issues | 2 | Confirmed #1 (settleBookingHold); StayCandidate drift |
