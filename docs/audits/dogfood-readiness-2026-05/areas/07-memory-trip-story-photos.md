# Area Audit: Memory, Trip Story, Photos

Date: 2026-05-21  
Agent: Codex  
Scope: backend memory/story/photo routes, Trip Story composer/projection/share helpers, post-trip tasks/subscribers, retention/account deletion, frontend Memory Home/Trip Story/Trip Log/photo album/share/consent surfaces, targeted tests and docs listed in the prompt.  
Mode: Audit only. No product-code changes.

## Executive Summary

- Dogfood risk: Medium
- Highest-risk finding: photo learning consent is trip-wide, so one member can opt other members' group-visible photos into `group_and_learn`.
- Checks run: `make contract-check` -> pass; `make api-coverage-check` -> pass; `make mock-real-parity` -> pass; `PYTHONPATH=. pytest tests/tasks/test_post_trip_character_read.py tests/concierge/test_post_trip_memory_refresh.py tests/test_story_projection.py -q` -> pass; `npm test -- --runTestsByPath __tests__/data/memory.test.ts __tests__/data/memory-hooks.test.ts __tests__/components/memory/ShareStorySheet.test.tsx --runInBand` -> pass.
- Residual uncertainty: I did not run Postgres-required account deletion/share integration tests or any live LLM/post-trip composition jobs.

## Findings

### P1 — Photo Learning Opt-In Applies To Other Members' Photos

Status: Confirmed  
User impact: A dogfood traveler can tap "Let Vesper learn from these" and silently upgrade every group-visible photo on the trip, including photos uploaded by other members, into the learning tier. Co-travelers only consented to group album visibility, not future learning.  
Product promise affected: photo privacy / future-learning consent

References:

- `Travel Agent/backend/api/routes/trip_photos.py:312` — authenticated opt-in endpoint accepts only `trip_id`, not a per-owner scope.
- `Travel Agent/backend/api/routes/trip_photos.py:325` — calls `_bulk_opt_in_learning(trip_id=trip_id)` without passing `actor.id`.
- `Travel Agent/backend/api/routes/trip_photos.py:478` — helper says it upgrades all `group` photos in a trip.
- `Travel Agent/backend/api/routes/trip_photos.py:485` — update filters by `trip_id` and `visibility == "group"` only, not `uploaded_by_user_id`.
- `Travel App/components/trip/GroupAndLearnConsentSheet.tsx:84` — sheet frames the action as "Your photos, working harder."
- `Travel App/components/trip/GroupAndLearnConsentSheet.tsx:86` — copy says "your trip photos" will refine "your Taste DNA."
- `Travel App/app/(tabs)/trips/[tripId]/memory.tsx:60` — `groupPhotos` includes every visible group photo, not just the current user's uploads.

Why it matters:

`group` and `group_and_learn` are distinct privacy states in the model. The backend doc explicitly defines `group_and_learn` as permission for Personal Memory/Taste DNA derivation, while the current bulk update turns one member's consent into consent for the whole album.

Repro or deterministic test idea:

1. Seed `trip_photos` with two `group` rows on one trip: one uploaded by Alice, one by Bob.
2. Call `POST /api/trips/{trip_id}/photos/opt-in-learning` as Alice.
3. Expected: only Alice's row becomes `group_and_learn`; Bob's remains `group`.
4. Current likely/observed from code path: both rows become `group_and_learn`.

Suggested fix direction:

Scope the update by `uploaded_by_user_id == actor.id`, and update frontend copy/counts to show "your group-visible photos." If the product wants group-level album learning later, make it an explicit per-member or organizer-mediated consent model.

Related bug class:

cross-user consent leak / privacy tier escalation

Confidence: High

### P2 — Public Story Projection Can Expose Third-Party Personal Moments

Status: Confirmed  
User impact: A shared story can include a named co-traveler's personal moment, e.g. "Diana cried during fado," because public projection only strips known private-keyword patterns and hidden sections. There is no "hide people names" control even though the product requirement lists it.  
Product promise affected: public story privacy / third-party facts / share trust

References:

- `Travel Agent/docs/product/MVP Social Loop.md:217` — user polishing requirements include removing sections, adding/hiding photos, and hiding people names.
- `Travel Agent/docs/product/MVP Social Loop.md:224` — "hide people names" is an explicit product control.
- `Travel Agent/backend/core/story_projection.py:92` — public sections are filtered by hidden IDs, empty body, and `check_private_signal`.
- `Travel Agent/backend/core/story_projection.py:99` — otherwise the raw section body is emitted as `PublicStorySection`.
- `Travel Agent/backend/core/privacy_signal.py:41` — private-signal detector is keyword/regex based.
- `Travel Agent/backend/core/privacy_signal.py:83` — third-party attribution patterns cover "privately mentioned"/"because Sarah said" style phrases, not ordinary named personal moments.
- `Travel App/components/memory/ShareStorySheet.tsx:274` — share sheet offers dates, destination, and follower visibility toggles.
- `Travel App/components/memory/ShareStorySheet.tsx:295` — section-level inclusion is the only granular content control.

Why it matters:

The server-side projection is the right trust boundary for public artifacts, but it is not sufficient for non-keyword third-party facts. I verified with a deterministic probe that `check_private_signal("Diana cried during fado and nobody mentioned it.")` returns safe, and `build_public_story_payload` publishes that section.

Repro or deterministic test idea:

1. Add a pure unit test in `Travel Agent/tests/test_story_projection.py` with a story section body `Diana cried during fado and nobody mentioned it.`
2. Build the public payload with default `RedactionPolicy`.
3. Expected for the share promise: either names are redacted/hidden by policy, or the section is excluded until the owner opts into named people.
4. Current observed: the section appears unchanged in `public.sections`.

Suggested fix direction:

Add a privacy control for people names in `RedactionPolicy` and the share sheet, defaulting conservatively for public/link shares. Short term, the composer can be instructed to avoid co-traveler names and third-party emotional facts in public-shareable sections, but server-side projection should own the final guarantee.

Related bug class:

public artifact redaction gap / third-party fact leak

Confidence: High

### P3 — Mock Memory Days Are Much Richer Than Real Digest Mapping

Status: Confirmed  
User impact: In mock mode, Memory looks like a photo-rich trip journal with hero moments, clusters, grids, captions, and attributed quotes. In real mode, `useMemoryDays` currently maps each digest into one quote-like text moment. A dogfood tester can approve a surface in mock mode that the real backend cannot populate with the same richness.  
Product promise affected: mock-real parity / false UX promise

References:

- `Travel App/constants/mocks/memory.ts:7` — mock memory days include rich `hero`, `cluster`, `grid`, and `quote` moments.
- `Travel App/constants/mocks/memory.ts:18` — mock clusters include multiple photos and captions.
- `Travel App/data/memory.ts:18` — real digest mapping starts from `APITripDigest`.
- `Travel App/data/memory.ts:21` — real path only uses `rendered_markdown` or `content.day_arc`.
- `Travel App/data/memory.ts:28` — real path emits a single `quote` moment per digest.
- `Travel App/app/(tabs)/trips/[tripId]/memory.tsx:241` — screen renders `memoryDays` directly, so the mock richness materially changes the visible product.

Why it matters:

Memory and post-trip surfaces are already labeled "partially mock-safe / real-check required." This particular mismatch makes the trip memory feel more complete in mock than the real backend data can support today, especially around photos and attribution.

Repro or deterministic test idea:

1. Run the Memory screen in mock mode and note photo clusters/hero moments.
2. Run `useMemoryDays` against a realistic digest response like `Travel App/__tests__/data/memory.test.ts`.
3. Expected: mock fixtures exercise the same shape real data can provide, or the mock labels clearly represent future-only design.
4. Current observed: mock has multiple rich moment types; real mapping returns quote-only summaries.

Suggested fix direction:

Either downgrade the default mock memory days to the real digest shape, or add a separate clearly named future-state fixture. If rich moments are intended for dogfood, define the backend contract for photos/captions/attribution and update `useMemoryDays` to consume it.

Related bug class:

mock-real drift / overstated memory artifact

Confidence: High

## Non-Findings / Things Ruled Out

- Story share projection does protect private photo URLs: public story photos are allowlisted to the story owner's `group` / `group_and_learn` trip photos, and targeted tests cover private-photo exclusion.
- GPS coordinates are owner-only in photo API projection: `_row_to_trip_photo` returns `gps_lat/gps_lng` only to the uploader, and targeted tests cover owner vs non-owner behavior.
- Regeneration copy is honest about edit preservation: the app says attached photos are kept, while section edits survive only if the new draft keeps that section. Backend merge logic matches that limitation.
- Account deletion is deliberately broad: `delete_user_data` removes `user_id` rows, explicit authored content, uploaded photos, messages, memory interactions, and the user row. FKs cover trip stories/shares/photos; I did not run the Postgres test suite.
- Post-trip character read and memory-refresh wiring has offline coverage and passed. Character reads use an idempotency key; scheduled post-trip tasks are durable and deduped by task kind/scope.

## Suggested Follow-Up Checks

- Add a backend regression for `opt_in_trip_photos_learning` proving one user's opt-in cannot upgrade another user's photo.
- Add a pure story-projection test for named third-party moments and a UI test asserting the share sheet exposes the chosen people-name policy.
- Add a memory mock-real parity test that compares `mockMemoryDays` moment types against what `useMemoryDays` can produce from `APITripDigest`.
