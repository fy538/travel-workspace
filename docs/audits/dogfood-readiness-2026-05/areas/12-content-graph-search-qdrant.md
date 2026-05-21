# Area Audit: Content Graph, Search, Qdrant Consistency

Date: 2026-05-21  
Agent: Codex/Cursor Cloud audit session  
Scope: `Travel Agent` content docs, place/venue/site/accommodation/experience seed pipeline, Postgres brief generation, Qdrant embedding and retrieval code, concierge search handlers, `Travel App` Discover and For This Trip content rails.  
Mode: Audit only. No product-code changes.

## Executive Summary

- Dogfood risk: High
- Highest-risk finding: The post-seed drift gate can report a city clean while missing both actual Qdrant point absence and child-place content, so Lisbon or other dogfood cities can still feel empty after a "clean" seed.
- Checks run: `make contract-check` -> pass; `PYTHONPATH=. pytest tests/scripts/test_check_seed_drift.py -q` -> pass; `npm test -- --runTestsByPath __tests__/data/experiences.test.ts __tests__/screens/discover.smoke.test.tsx --runInBand` -> pass.
- Residual uncertainty: I did not connect to live Postgres/Qdrant, run the full seed pipeline, call live LLMs, or exercise production/provider APIs. Findings are from deterministic static analysis plus narrow local tests.

## Findings

### P1 - Post-seed drift checker can miss real Qdrant/Postgres divergence

Status: Confirmed  
User impact: A dogfood city can look "seeded" to operators while Qdrant-backed discovery and concierge retrieval return empty or stale results. Lisbon is specifically at risk because docs already show Postgres has Lisbon content while Qdrant-backed production search has little or none.  
Product promise affected: Grounded place-aware recommendations, content graph reliability, search/retrieval trust

References:

- `Travel Agent/docs/operations/Content Pipeline Audit.md:9` - documents that the Postgres to Qdrant link broke during the April places-tree migration.
- `Travel Agent/docs/operations/Content Pipeline Audit.md:43` - records severe Qdrant/Postgres overlap gaps, including `venue_briefs` 301 points vs 42 Postgres venues with overlap 2.
- `Travel Agent/docs/operations/Content Pipeline Audit.md:55` - records stale `city` and `place_id` payloads in `venue_briefs`.
- `Travel Agent/docs/operations/Content Pipeline Audit.md:116` - records production Brooklyn restaurant search, accommodation search, experience search, and Lisbon venue search as broken or partial.
- `Travel Agent/scripts/check_seed_drift.py:1` - advertises this script as post-seed Postgres to Qdrant verification.
- `Travel Agent/scripts/check_seed_drift.py:50` - `_check_city()` only opens Postgres and never reads Qdrant collections or point payloads.
- `Travel Agent/scripts/check_seed_drift.py:59` - venue checks scope to `venues.place_id == city_id`, missing venues seeded under child neighborhoods or districts.
- `Travel Agent/scripts/check_seed_drift.py:111` - site, accommodation, and experience drift checks repeat the same direct-city scope pattern.
- `Travel Agent/backend/research_agent/tasks/seed_venues.py:160` - the seed pipeline intentionally processes descendant neighborhoods and districts.
- `Travel Agent/backend/research_agent/tasks/seed_venues.py:343` - seeded entities are persisted to the current child place or a resolved neighborhood hint.
- `Travel Agent/backend/research_agent/tasks/seed_venues.py:474` - venues are created with `place_id=place_id`, which is usually the child place being processed.
- `Travel Agent/backend/core/db/content/_briefs.py:157` - brief generation uses `get_descendants(city_place.id)` and includes the city id, showing the correct city-subtree model elsewhere.
- `Travel Agent/tests/scripts/test_check_seed_drift.py:10` - existing tests use mocked scalar results, so they verify exit branching but not SQL scope, descendant coverage, or actual Qdrant point existence.

Why it matters:

The script is positioned as the deterministic "are both stores clean after seed?" gate. Today it can produce false confidence in two high-risk cases: Qdrant was wiped or stale while Postgres still has pointers, and content lives under city descendants rather than the city row itself. That lines up with the documented production failure mode: Postgres and Qdrant each have plausible-looking data, but retrieval surfaces are empty or stale for real users.

Repro or deterministic test idea:

1. Build a SQLite or mocked-SQL fixture with a city, a child neighborhood, and a venue/brief/state row under the child place.
2. Mark the child venue dirty or remove its Qdrant point while leaving `venue_brief_state.qdrant_point_id` non-null.
3. Run `PYTHONPATH=. python scripts/check_seed_drift.py --city <city-slug>`.
4. Expected: non-zero exit and a report showing child-place drift or missing Qdrant point overlap.
5. Current likely: direct `place_id == city_id` queries and pointer-only checks can report clean.

Suggested fix direction:

Make `check_seed_drift.py` resolve the full city subtree for every entity type, then verify actual Qdrant point existence and payload identity for each non-null `qdrant_point_id`. Add a deterministic fixture test covering child-place rows and a mocked Qdrant client test where Postgres pointers exist but the collection has no matching point. Wire that overlap assertion into the post-seed path and CI.

Related bug class:

Content store drift / false-negative operational gate

Confidence: High

### P2 - Concierge restaurant search computes empty-result diagnostics but drops them from the tool response

Status: Confirmed  
User impact: When restaurant search returns no candidates because Qdrant is empty, filters are too narrow, or all hits fail constraints, the concierge receives only an empty result set and count. That makes the assistant more likely to apologize generically, retry blindly, or invent an explanation instead of telling the user how to broaden the search.  
Product promise affected: Concierge trust, grounded search, empty-result explanation

References:

- `Travel Agent/backend/planning_agent/fan_out_search.py:167` - appends a diagnostic when no restaurants pass constraints.
- `Travel Agent/backend/planning_agent/fan_out_search.py:202` - `_explain_empty_fan_out()` explains no Qdrant hits, dedupe issues, or hard-filter failures.
- `Travel Agent/backend/planning_agent/fan_out_search.py:179` - returns the diagnostic in `FanOutSearchOutput.search_summary`.
- `Travel Agent/backend/concierge/tool_handlers/search.py:265` - concierge serialization intentionally limits result fields.
- `Travel Agent/backend/concierge/tool_handlers/search.py:296` - returned JSON includes `results`, `search_descriptions_used`, and `result_count`, but not `results.search_summary`.
- `Travel Agent/backend/planning_agent/restaurant_tools.py:190` - the planning-agent wrapper does include `search_summary`, so this is a concierge envelope loss rather than missing retrieval logic.

Why it matters:

The retrieval layer already does the work needed to make empty results safe and understandable. The concierge path is the dogfood-facing path, and it loses that explanation right before the LLM sees the tool result. This is especially risky while Lisbon/Brooklyn content coverage is uneven: "no candidates" is often an operational signal, not proof that the city has nothing useful.

Repro or deterministic test idea:

1. Mock `fan_out_restaurant_search()` to return `FanOutSearchOutput(results=[], search_summary="Diagnostic: No Qdrant hits ...")`.
2. Call `_execute_find_restaurants()` with one search description and a provider stub.
3. Expected: serialized JSON includes `search_summary` or another explicit diagnostic field.
4. Current likely: JSON contains `result_count: 0` and no diagnostic text.

Suggested fix direction:

Include `search_summary` in the concierge tool response, at least when `result_count == 0`, and add a unit test around `_execute_find_restaurants()` to preserve the diagnostic contract.

Related bug class:

Tool-envelope contract loss / empty-result hallucination risk

Confidence: High

### P2 - Discover and angle rails mask fetch failures as content gaps

Status: Confirmed  
User impact: A dogfood tester can see "No events found" or "Still curating" when the backend request actually failed. That makes a real outage, auth issue, or API error look like thin Lisbon coverage, with no retry affordance.  
Product promise affected: Content gap transparency, mock/real parity, app empty states

References:

- `Travel App/data/experiences.ts:12` - `useExperiences()` returns only `APIExperience[]`.
- `Travel App/data/experiences.ts:22` - the hook calls `useData()` but discards `isLoading`, `error`, and `refetch`.
- `Travel App/__tests__/data/experiences.test.ts:101` - the current test explicitly expects API rejection to return an empty array.
- `Travel App/app/(tabs)/discover/index.tsx:416` - Discover Events uses the array-only `useExperiences()` result.
- `Travel App/app/(tabs)/discover/index.tsx:1349` - an empty events array always renders "No events found" and suggests the city may not be indexed.
- `Travel App/app/(tabs)/discover/index.tsx:414` - Discover Angles destructures only `data` and `isLoading` from `usePlaceAngles()`.
- `Travel App/app/(tabs)/discover/index.tsx:929` - empty or failed angles render "Still curating" instead of an error/retry state.
- `Travel App/components/for-this-trip/TripAngleRail.tsx:42` - TripAngleRail also ignores `error`/`refetch` from `usePlaceAngles()`.
- `Travel App/components/for-this-trip/TripAngleRail.tsx:61` - TripAngleRail renders a content-gap message for empty or failed angle loads.
- `Travel App/components/for-this-trip/TripExperienceRail.tsx:43` - the trip experience rail is a useful contrast: it preserves `isError` and `refetch`.
- `Travel App/components/for-this-trip/TripExperienceRail.tsx:60` - that rail renders a compact retryable `ErrorState` when event loading fails.

Why it matters:

Dogfood readiness depends on distinguishing "the content graph is thin here" from "the app could not reach the real content graph." The Events and Angles surfaces currently collapse those states, which hides retrieval outages and makes city coverage look worse or more arbitrary than it is.

Repro or deterministic test idea:

1. In a real-mode Jest hook test, mock `api.searchExperiences()` to reject.
2. Render the Discover Events tab for a city.
3. Expected: retryable error state such as "Could not load events."
4. Current observed by existing test contract: `useExperiences()` returns `[]`, so Discover renders "No events found."
5. Repeat with `api.getPlaceAngles()` rejection for Discover Angles and `TripAngleRail`.

Suggested fix direction:

Return a structured result from `useExperiences()` that includes `experiences`, `isLoading`, `isError`, `error`, and `refetch`, or add a separate Discover-specific hook with that shape. Update Discover Events, Discover Angles, and TripAngleRail to render retryable error states when the request fails, matching the existing `TripExperienceRail` pattern.

Related bug class:

Mock-real drift / empty-state masks transport failure

Confidence: High

## Non-Findings / Things Ruled Out

- `make contract-check` passed; the OpenAPI snapshot and generated frontend schema are in sync.
- Qdrant venue ID handling is mostly string-normalized in the inspected retrieval path: payload builders stringify ids, and Qdrant filters match string ids.
- Venue retrieval filters include useful null-tolerant range handling for price and group size, and neighborhood filters try slug/display variants rather than a single accent-sensitive string.
- The dossier embedding path embeds new chunks before deleting old fragments, so a transient embedding failure should not wipe existing narration fragments in the inspected code path.
- Trip-scoped experience rails already distinguish error from empty and provide retry.

## Suggested Follow-Up Checks

- Add a real or mocked Qdrant overlap check to `check_seed_drift.py`: every non-null Postgres `qdrant_point_id` should resolve to a point with matching entity id, type, city/place payload, and collection.
- Add a descendant-place fixture for `check_seed_drift.py` so child neighborhood/district content is counted for the parent city.
- Add a concierge unit test that an empty fan-out restaurant response preserves `search_summary` through `_execute_find_restaurants()`.
- Add Discover/For This Trip tests that rejected experience and angle requests render retryable error states instead of content-gap copy.
