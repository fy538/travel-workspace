# Area Audit: Trip Creation, Destination Identity, Plan-Similar

Date: 2026-05-21  
Agent: Cursor Cloud agent / Codex audit session  
Scope: backend trip create/patch, place resolution, plan-similar conversion, frontend TripContext, Discover/social/story plan-similar entry points, current-trip route context, For This Trip destination derivation, generated API usage.  
Mode: Audit only. No product-code changes unless explicitly noted.

## Executive Summary

- Dogfood risk: High
- Highest-risk finding: story/social/discover trip starts do not share one canonical destination persistence path, so a dogfood trip can have backend `place_id` while app surfaces still behave as destinationless or, worse, create a trip whose "destination" is a venue/site name.
- Checks run: `make contract-check` -> pass; `make api-coverage-check` -> pass; `make mock-real-parity` -> pass; `PYTHONPATH=. pytest tests/api/test_trips_api.py tests/api/test_plan_similar_api.py tests/core/test_plan_similar_atomicity.py -q` -> pass; `npm test -- --runTestsByPath __tests__/data/trips.test.tsx __tests__/components/for-this-trip/ForThisTripPreview.test.tsx __tests__/screens/for-this-trip.smoke.test.tsx --runInBand` -> pass.
- Residual uncertainty: I did not run live backend or device navigation. The findings are static plus deterministic-test based.

## Findings

### P1 — Story plan-similar trips persist `place_id` but lose the destination label the app uses

Status: Confirmed  
User impact: A user cloning a shared Lisbon story can get a new trip that has `place_id` in backend state, but Trip Home's For This Trip preview hides and the deep page treats it as destinationless because `trip_summary.destination` is empty after refetch. This makes the cloned trip feel disconnected from place-aware content even though the backend knows the place.  
Product promise affected: plan coherence / place-aware concierge trust

References:

- `Travel Agent/backend/core/story_projection.py:204` — the plan-similar seed includes `public.destination`.
- `Travel Agent/backend/core/story_projection.py:209` — `PlanSimilarSeed.destination` and `suggested_title` are populated from the public story.
- `Travel Agent/backend/core/db/plan_similar.py:128` — `seed = build_plan_seed(...)` is available during clone creation.
- `Travel Agent/backend/core/db/plan_similar.py:131` — source trip `place_id` is copied.
- `Travel Agent/backend/core/db/plan_similar.py:134` — the derived trip is created with `title` and `place_id`, but no `trip_summary={"destination": seed.destination}`.
- `Travel App/components/for-this-trip/ForThisTripPreview.tsx:68` — preview derives destination only from `currentTrip.trip.trip_summary.destination`.
- `Travel App/components/for-this-trip/ForThisTripPreview.tsx:107` — preview returns `null` when the derived slug is missing.
- `Travel App/app/(tabs)/trips/[tripId]/for-this-trip.tsx:69` — deep page also derives destination only from `trip_summary.destination`.
- `Travel App/app/(tabs)/trips/[tripId]/for-this-trip.tsx:127` — when destination is absent, the place-angle and trip-experience rails are suppressed.
- `Travel Agent/tests/core/test_plan_similar_db.py:87` — existing DB test asserts brief, membership, and attribution, but not `trip_summary.destination`.

Why it matters:

The backend and frontend currently disagree about which field makes a trip destinationful. The clone path copies `place_id`, while the app's most place-aware trip surface gates on `trip_summary.destination`. That is exactly the dogfood promise under test: destination/place identity should survive refetch into Trip Home, Chat, Plan, Map, For This Trip, content rails, and backend state.

Repro or deterministic test idea:

1. Seed or mock a public Trip Story whose public projection has `destination="Lisbon"`.
2. Call `create_trip_from_share(slug, viewer_id)` or `POST /api/plan-similar`.
3. Expected: returned/refetched trip has both `place_id=<Lisbon id>` and `trip_summary.destination == "Lisbon"`, or the app can derive a slug from a generated place field.
4. Current likely/observed from code: trip has copied `place_id`, but `trip_summary` remains default/empty because the clone path never writes the seed destination.
5. Add a frontend regression with `currentTrip.trip.place_id` set and empty `trip_summary`; For This Trip should still render using a canonical place slug/name, or backend should guarantee the summary label.

Suggested fix direction:

Pick one canonical contract. The conservative backend fix is to persist `trip_summary={"destination": seed.destination}` in `create_trip_from_share` whenever the public seed has a destination. Longer term, expose a generated place summary/slug on backend-shaped trip data and update For This Trip to derive from that instead of treating `trip_summary` as the only source of place identity.

Related bug class:

Mock-real drift / dual source of truth / place identity drift

Confidence: High

### P1 — Discover/social "Plan similar" can create trips whose destination is a venue, site, or recommendation title

Status: Confirmed  
User impact: Tapping "Plan similar" from several Discover/social cards can create a new trip with `destination` set to an entity name rather than a city. If that label does not resolve to a place slug, backend `place_id` stays null while the app still shows a destination string, causing Map/Home/For This Trip/content rails to disagree or go empty after refetch.  
Product promise affected: plan coherence / routed to the correct workspace

References:

- `Travel App/app/(tabs)/discover/index.tsx:457` — shared handler accepts only a destination string.
- `Travel App/app/(tabs)/discover/index.tsx:463` — handler creates a trip through generic `createTrip({ title: destination, destination })`, not a plan-similar-specific path carrying canonical place identity.
- `Travel App/app/(tabs)/discover/index.tsx:469` — user is routed to global concierge chat with a free-text prefill, not the new trip workspace.
- `Travel App/components/discover/FeedItemRenderer.tsx:203` — accommodation/site teaser comments say these route through plan-similar behavior.
- `Travel App/components/discover/FeedItemRenderer.tsx:215` — accommodation/site teaser passes `item.name` as the destination.
- `Travel App/components/discover/FeedItemRenderer.tsx:250` — recommendation hero passes `rec.title` as the destination.
- `Travel App/components/discover/FeedItemRenderer.tsx:267` — recommendation row passes `rec.title` as the destination.
- `Travel Agent/backend/api/routes/trips.py:386` — backend create only resolves `place_id` from the supplied destination label when no explicit `place_id` is sent.
- `Travel Agent/backend/core/db/places.py:395` — label resolver keeps only the first comma segment and slugifies it.
- `Travel Agent/backend/core/db/places.py:401` — if the slug is not a known place, resolution returns `None`.

Why it matters:

This path makes a new trip from user intent, so the first saved state must be right. A card for a hotel, site, venue, or generic recommendation can mint a trip titled and summarized as that entity, with no backend place identity. Mock mode can still look coherent because it echoes the `destination` string into `trip_summary`, but real place-aware backend surfaces key off `place_id`.

Repro or deterministic test idea:

1. In Discover, render an `accommodation_teaser` or `site_teaser` with `name="Hotel Santa Clara"` and no city payload.
2. Tap it.
3. Expected: either no trip is created and chat asks about the item in the current destination, or trip creation sends a canonical city/place id plus source entity metadata.
4. Current likely/observed from code: `POST /api/trips` receives `destination="Hotel Santa Clara"`; `resolve_place_id_from_label` slugifies `hotel-santa-clara`; `place_id` remains null unless that exact place is seeded as a place root.

Suggested fix direction:

Separate "plan a destination" from "ask about this entity" and "clone this story". Destination-led cards should pass a canonical `place_id` or slug/name pair. Entity-led cards should route to item detail or trip chat with metadata, not create a new destination workspace from `item.name`. Story/social clones should use `/api/plan-similar` or an equivalent canonical helper that persists both place identity and source attribution.

Related bug class:

Wrong workspace creation / noncanonical entry point / mock-real drift

Confidence: High

### P2 — Direct trip creation can still leave orphan trips if organizer membership insert fails

Status: Confirmed  
User impact: A transient DB failure after the trip row insert but before organizer membership insert can leave an invisible trip: it exists in `trips`, but the creator cannot list, open, or delete it because trip reads are membership-gated. Retrying may create another trip.  
Product promise affected: create trip and invite group / backend state integrity

References:

- `Travel Agent/backend/api/routes/trips.py:392` — direct `POST /api/trips` calls `db_create_trip`.
- `Travel Agent/backend/api/routes/trips.py:404` — organizer membership is inserted after the trip is already created.
- `Travel Agent/backend/core/db/trips.py:96` — `create_trip` inserts and commits the trip row.
- `Travel Agent/backend/core/db/trips.py:297` — `add_trip_member` opens a separate connection.
- `Travel Agent/backend/core/db/trips.py:307` — `add_trip_member` commits separately.
- `Travel Agent/backend/core/db/plan_similar.py:140` — plan-similar documents the same create+member split as an orphan risk.
- `Travel Agent/backend/core/db/plan_similar.py:145` — plan-similar compensates by deleting the trip if membership add fails.
- `Travel Agent/tests/core/test_plan_similar_atomicity.py:26` — regression coverage exists for plan-similar orphan cleanup, but not for direct `POST /api/trips`.

Why it matters:

The golden path invariant says creating a trip returns a stable trip id and organizer membership. Plan-similar has already patched this risk, which makes the direct create route the inconsistent sibling. This is lower severity than the destination bugs because it needs a membership insert failure, but the failure mode is concrete and hard for dogfooders to recover from.

Repro or deterministic test idea:

1. Unit-test `backend.api.routes.trips.create_trip` with `db_create_trip` returning a trip and `add_trip_member` raising.
2. Expected: the route either performs both writes in one transaction or compensates by deleting the created trip before returning an error.
3. Current likely/observed from code: the exception propagates after the trip insert committed; no cleanup path runs.

Suggested fix direction:

Move trip creation plus organizer membership into one DB transaction/helper, or mirror the plan-similar compensating delete in the direct create route. Add a direct-create atomicity regression test next to `test_plan_similar_atomicity.py`.

Related bug class:

Non-atomic persistence / orphaned state

Confidence: High

## Non-Findings / Things Ruled Out

- Direct `POST /api/trips` does resolve accent-bearing and country-suffixed destination labels through a shared slug helper: backend `resolve_place_id_from_label` strips country suffixes and diacritics, and frontend `slugFromDestination` mirrors that behavior.
- Generated types are used for backend-shaped trip data in `Travel App/utils/api/types.ts`; `APITrip`, `CreateTripRequest`, and `PatchTripRequest` derive from `utils/api/schema.gen.ts`.
- Current trip context does recover for trip-workspace routes that include `[tripId]`: the workspace layout reads route params and calls `selectTrip(tripId)`. Several standalone screens also have query-param helpers for cold-launch recovery.
- Contract drift is not the cause here: OpenAPI snapshot, generated TypeScript schema, and `http.ts` coverage all pass.

## Suggested Follow-Up Checks

- Add a backend plan-similar regression asserting the created trip has `trip_summary.destination == seed.destination` when the public seed has a destination.
- Add a frontend For This Trip regression for a refetched trip with `place_id` present and `trip_summary.destination` missing.
- Add a Discover/FeedItemRenderer test proving entity-led cards do not call destination trip creation with `item.name`.
- Add direct `POST /api/trips` atomicity coverage mirroring `tests/core/test_plan_similar_atomicity.py`.
