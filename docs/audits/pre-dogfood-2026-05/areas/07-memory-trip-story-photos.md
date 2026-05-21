# Pre-Dogfood Area Audit 07 — Memory, Trip Story & Photos

Date: 2026-05-20
Scope: post-trip Trip Story composer + Memory API, trip photo album (upload,
EXIF/GPS extraction, per-photo privacy, group_and_learn consent), post-trip
loop (character read + memory refresh + observation write-back), and the
Travel App surfaces in `components/memory/*`, `app/(tabs)/trips/[tripId]/story.tsx`
and the album / lightbox / consent UI.

Mode: read-only; no product code, test, fixture or config was modified.

## Summary

| Severity | Count |
|---|---:|
| P0 | 1 |
| P1 | 6 |
| P2 | 3 |
| TECH-DEBT | 2 |

**Biggest concern (P0):** the Trip Story composer's "edits are preserved on
regenerate" promise is a coincidence, not a contract. The merge keyed on
`section.id` (`trip_story.py:153-156, 195`) relies on Sonnet emitting the
*same* slug on a re-run, but the composer prompt never tells the LLM about
prior IDs and never asks it to keep them stable; tests pin the happy path
where the same IDs come back, but nothing forces it. Worse, **`photo_slots`
are not merged at all on regenerate** — every user-attached photo slot
(`photo_url` set via PATCH `/sections/{section_id}/photo`) is silently
discarded into the prior version. The frontend's "Rewrite story" alert tells
the user "Your edited sections will be preserved" — that copy is misleading
in two directions. For a dogfood tester whose trip story is the share asset,
"the sparkle button erased my photos" or "the sparkle button rewrote the
paragraph I wrote about my mum" both kill trust in the post-trip artifact
permanently.

**Privacy posture (P1 cluster):**

- **GPS coords leak to every group viewer.** `_list_trip_photos`
  (`trip_photos.py:368-398`) returns `gps_lat` / `gps_lng` to anyone who can
  see a photo. EXIF is stripped from served *image bytes* in
  `media/variants.py:42`, but the GPS that the backend extracted in
  `photo_metadata.py:_extract_gps` is hoisted into a separate column and
  shipped in the typed API response (`TripPhoto.gps_lat/gps_lng`). The
  expo-image-picker `exif: false` flag (`photos.tsx:109`) only controls what
  metadata is returned to *JS*; the uploaded bytes still carry GPS, and the
  server still pulls it. The user is given no UI to inspect or strip it.
- **A trip member can plant another member's group photo into their own
  publicly-shared story.** `_validate_story_photo_url` (`memory.py:415-444`)
  only checks scheme + CDN host; it never verifies the photo belongs to the
  patching user. The `_public_photo_urls` allowlist (`trip_story_shares.py:494-529`)
  is per-trip, so *any* group/group_and_learn photo on the trip survives the
  projection. A trip member can take a co-traveler's group photo URL, PATCH
  it onto a slot in their own story, publish to "link", and that co-traveler's
  photo now appears on a public landing they did not consent to.
- **`group_and_learn` consent is theatre.** The `GroupAndLearnConsentSheet`
  promises "Let Vesper analyze your trip photos to refine your Taste DNA" and
  lists the DNA dimensions that "get richer", and
  `opt-in-learning` flips visibility to `group_and_learn` — but **no code in
  `backend/` reads the `group_and_learn` value for any learning purpose**
  (the only consumers treat it as a synonym for `group` in visibility checks).
  A tester who taps "Let Vesper learn from these" is consenting to something
  that does not happen.
- **The composer is fed arbitrary user-typed block titles with no
  redaction.** `_load_confirmed_moments` (`trip_story.py:227-274`) feeds
  `itinerary_blocks.title` for every block the user marked `event_state='happened'`
  into the composer's user prompt as anchors. If a user renamed a block
  ("anniversary surgery follow-up", "Tom's intervention dinner") that title
  lands verbatim in the Sonnet prompt that produces the section bodies
  that become the share asset.

The post-trip loop **does** close — `post_trip_memory_refresh.py` schedules a
durable T+3h refresh on `trip.completed`, the daily backfill picks up missed
work, and `record_memory_engagement_observation` is correctly gated on
deliberate actions (`save` / `share` / `regenerate`) with passive
`view`/`dwell` explicitly excluded (`core/memory_signal.py:11-12, 47-49`). I
did not find a path by which a passive signal (dwell, scroll, view) writes an
observation. The character-read prompt at `post_trip_character_read.py:53-74`
correctly scopes to the *member's* own observations and only ships into the
member's personal 1:1 session, so no cross-member observation leak there.

The default-deny `PublicTripStory` allowlist
(`backend/core/story_projection.py`) and the per-trip `_public_photo_urls`
allowlist do the heavy lifting — they catch a private photo dropped into a
slot, and they catch every implicit field on the row. The escape routes are
the two P1s above (own-trip group photos that aren't the user's, and the
section *body* path which is allowlisted-in by default — see P1 below).

---

## Findings

### [P0] — Trip Story regenerate silently destroys photo assignments and (probabilistically) user edits

**References:**
- `Travel Agent/backend/tasks/trip_story.py:113-221` (`compose_trip_story`)
- `Travel Agent/backend/tasks/trip_story.py:152-156` (collects `edited_sections_by_id` by `s.id`)
- `Travel Agent/backend/tasks/trip_story.py:185-205` (`merged = [edited_sections_by_id.get(s.id, s) for s in sections]`; `photo_slots=photo_slots` — composer's freshly parsed slots, *not* merged with prior's persisted slots)
- `Travel Agent/backend/tasks/trip_story.py:46-107` (composer system prompt: never mentions stable section IDs, gives `"arrival"` as a sample)
- `Travel Agent/backend/api/routes/memory.py:324-368` (`patch_trip_story_photo_slot` writes `slot.photo_url` to the **current latest** version only)
- `Travel App/app/(tabs)/trips/[tripId]/story.tsx:169-186` (`handleRegenerate` shows alert text *"Your edited sections will be preserved"*)
- `Travel Agent/tests/tasks/test_trip_story.py:238-323` — the existing
  `test_preserves_user_edited_sections_on_regeneration` *assumes* the same
  IDs come back; no test covers a divergent-ID composer or photo slot
  preservation.

**Why it matters to a real tester:** the regenerate (sparkles ✨) button is
front-and-center in the story screen header (`story.tsx:255-260`). Two
plausible-and-likely failure modes:
1. The user spends 10 minutes attaching three photos to slots in their
   Lisbon story, then taps ✨ to "try a fresh angle". The new version's
   `photo_slots` come straight off the composer payload with
   `photo_url=None` for every slot, and the prior version's slot-with-URLs
   stay quietly on a v1 row that the GET endpoint never returns again
   (`get_latest_trip_story` orders by `version DESC LIMIT 1`). Their photos
   are gone from the surface. There is no undo and no toast.
2. Sonnet at temperature ~0.5 on the same arc + observations is not
   guaranteed to emit the same section slugs (`"arrival"`, `"sunday-lunch"`,
   `"the-walk-home"`) it picked the first time — and the prompt never
   instructs it to. A regenerate that returns
   `"touchdown"`, `"long-lunch"`, `"walking-back"` for the same beats means
   `edited_sections_by_id.get(s.id, s)` always misses, and every user edit
   is silently overwritten. The frontend alert literally tells the user they
   *will* be preserved.

Either of these alone burns trust in the post-trip artifact, which is the
compounding asset and the share source.

**Repro / deterministic test idea:**
- Photo loss: insert a `trip_stories` row v1 with two `photo_slots`, both
  with `photo_url` set to real CDN URLs; mock the composer to return the
  same section IDs but `photo_slots` with `photo_url=None`. Call
  `compose_trip_story`. Assert that the latest version returned by
  `get_latest_trip_story` has `photo_url=None` on every slot. (Currently
  passes — that *is* the bug; this test is the regression seat.)
- Edit loss: same setup but with v1's `arrival` section
  `edited_at=now, body="User edit"`. Mock the composer to return
  `{"id": "the-arrival", ...}` instead of `{"id": "arrival", ...}`. Assert
  the merged sections include `body == "User edit"` — today they do not.

**Suggested fix direction:**
1. Merge `photo_slots` on regenerate, keyed on `section_id`: any prior
   slot whose `photo_url` is non-null AND whose `section_id` survives in
   the new version keeps its URL. New slots not present before stay
   prompt-only as composed.
2. For edits, give the composer the prior section IDs (or, simpler,
   regenerate one section at a time and never re-mint IDs server-side).
   Until that lands, **change the frontend alert** in `story.tsx:171-172`
   to be honest: *"The Concierge will compose a fresh version. Your edits
   are kept only if the new draft uses the same section structure — they
   may be lost."*
3. Add the two regression tests above and seat them as the merge contract
   for any future LLM tuning.

**Confidence:** High

---

### [P1] — GPS coordinates from every group photo leak to every other group member

**References:**
- `Travel Agent/backend/api/routes/trip_photos.py:368-398` (`_list_trip_photos` selects `gps_lat`, `gps_lng` for all visible rows)
- `Travel Agent/backend/api/routes/trip_photos.py:386-388` (visibility filter passes group/group_and_learn photos from *other* members; column projection includes GPS unconditionally)
- `Travel Agent/backend/api/routes/trip_photos.py:489-504` (`_row_to_trip_photo` includes GPS in the typed response body)
- `Travel Agent/backend/core/models/trip_photos.py:27-28` (`TripPhoto.gps_lat/gps_lng` in the public-API schema)
- `Travel Agent/backend/media/photo_metadata.py:86-103` (server-side extracts GPS from EXIF — independent of the picker's `exif:false` flag)
- `Travel App/app/(tabs)/trips/[tripId]/photos.tsx:104-109` (mobile picker sets `exif:false, quality:0.85` — only suppresses JS-side metadata; the bytes the picker hands the upload still contain EXIF)
- `Travel App/components/memory/PhotoSlotCard.tsx:50-55` (story-slot picker does not even pass `exif:false`)

**Why it matters to a real tester:** the photographer expects that when they
share a photo with the group, what travels is the *image*. The current
contract leaks 7-decimal-place lat/lng of where every photo was taken — a
hotel room, a friend's apartment, a private meeting spot, the home of a
sensitive contact in a destination city — to every other group member, with
no UI affordance to inspect, blur, or strip the data. The image bytes
*themselves* have EXIF stripped at variant generation (`variants.py:42`,
Pillow's WEBP encoder drops EXIF by default) so this looks like privacy
hygiene from the outside, while the structured GPS column round-trips
through the JSON API. A dogfood tester who is tech-literate enough to verify
the bytes are clean will not think to check the typed response.

The combined "I trusted you because the bytes were clean" + "the typed
response has my exact apartment coords" is the worst version of this.

**Repro / deterministic test idea:**
1. As user A, multipart-upload a photo with EXIF GPS at (40.6782, -73.9442)
   to a trip both A and B belong to (visibility defaults to `group`).
2. As user B, `GET /api/trips/{trip_id}/photos`. Assert the response
   contains the photo with `gps_lat`/`gps_lng` populated to ≈7 dp.
3. Assert there is no API surface for A to clear those coordinates without
   deleting the whole photo, and no UI affordance in the album/lightbox
   that even surfaces "this photo will share your GPS with your group".

**Suggested fix direction:** make GPS coords *owner-only* in the API — only
return `gps_lat/lng` when `row.uploaded_by_user_id == viewer_id`. The
internal auto-tag use case (`find_nearest_block`) already runs at upload
time before visibility is consulted, and it lives behind a DB read, not the
API — no functional regression. Separately, add a one-line "GPS is used to
auto-tag stops on your phone, not shared with your group" line in the
`PermissionRationale` so the consent model is honest.

**Confidence:** High

---

### [P1] — A trip member can attach another member's photo to their own publicly-shared story

**References:**
- `Travel Agent/backend/api/routes/memory.py:324-368` (`patch_trip_story_photo_slot` — no ownership check on the photo)
- `Travel Agent/backend/api/routes/memory.py:415-444` (`_validate_story_photo_url` only validates scheme + CDN host)
- `Travel Agent/backend/core/db/trip_story_shares.py:494-529` (`_public_photo_urls` allowlists *any* group/group_and_learn photo on the trip — not just the owner's)
- `Travel Agent/backend/core/story_projection.py:102-108` (projection trusts the per-trip allowlist)

**Why it matters to a real tester:** trip stories are per-(trip, user); the
share is also per-user (`trip_story_shares.owner_user_id == story owner`).
A trip member viewing the GET `/photos` response (which returns all
group/group_and_learn photos across members, complete with CDN URLs) can
copy a co-traveler's CDN URL, PATCH it into their own story's photo slot,
and publish a public share link. The `_public_photo_urls` allowlist is
keyed only on `trip_id`, so the co-traveler's group photo is treated as
the publisher's "own" public material. The co-traveler's photo is now on
the open web at a `travelagent.app/stories/<slug>` URL they never approved.

This isn't a malicious-stranger scenario; group trips are exactly the
setting where one member shares the trip publicly and others don't. They
expect their own group-photos stay inside the album.

**Repro / deterministic test idea:**
1. User A uploads a `group` photo to trip T. Note its `cdn_url`.
2. User B (also in T) calls
   `PATCH /api/trips/{T}/story/sections/{any section id}/photo`
   with `{"photo_url": "<A's cdn_url>"}`. Expect 200.
3. User B creates a `link` share and opens
   `GET /api/stories/{share_slug}` unauthenticated.
4. Assert A's photo URL is absent from `photo_urls`. Today it is *present*.

**Suggested fix direction:** in `_public_photo_urls` (or `patch_trip_story_photo_slot`),
require the photo row to also have `uploaded_by_user_id == owner_user_id`
(the story owner). The current `is_shared` rule in `_update_block` already
treats group photos as a collaborative surface for *re-tagging* — but
re-tagging is reversible inside the album and only co-members see it;
public publishing crosses a different threshold and needs the tighter
check.

**Confidence:** High

---

### [P1] — `group_and_learn` consent ceremony does nothing — no code reads the flag for taste/preference learning

**References:**
- `Travel App/components/trip/GroupAndLearnConsentSheet.tsx:84-89` (sheet copy: *"Let Vesper analyze your N trip photos to refine your Taste DNA — the places you actually spent time, not just what you said you liked."*)
- `Travel App/components/trip/GroupAndLearnConsentSheet.tsx:112-130` ("Taste DNA dimensions that get richer" with named DNA chips)
- `Travel Agent/backend/api/routes/trip_photos.py:300-318` (`opt_in_trip_photos_learning` — flips visibility to `group_and_learn`)
- `Travel Agent/backend/api/routes/trip_photos.py:470-486` (`_bulk_opt_in_learning` — UPDATE only, no downstream wiring)
- `grep -rn "group_and_learn" backend/` — the only consumers are the visibility-allowlist checks in `_list_trip_photos`, `_update_block`, `_public_photo_urls`, and the CHECK constraint. **No taste/DNA/preference pipeline reads the flag.**
- `Travel Agent/backend/concierge/refresh_memory.py:218-490` — the Personal Memory synthesizer reads observations + user_facts + constraints; never reads `trip_photos.visibility` or photo content.

**Why it matters to a real tester:** the sheet is one of the most explicit
consent moments in the entire product. It names the DNA dimensions that
will allegedly get richer — and then nothing happens. There is no
post-trip task that vision-summarizes the photos, no embedding pipeline,
no observation creation tied to the photos, no Taste DNA refresh wired to
the new visibility tier. A tester who taps "Let Vesper learn from these"
and then opens the Memory home expecting the dimensions to feel sharper
will see the same dimensions, with no change. Worse, they have just
*broadened the visibility scope* of every group photo (technically a
no-op in current code, but a future feature lights up retroactively
against this opted-in cohort with no fresh consent) in exchange for a
promise that is not kept.

This is the kind of finding a privacy-curious user will write a tweet
about. It also normalizes the pattern of "consent first, build the
pipeline later" inside the codebase.

**Repro / deterministic test idea:**
1. Seed a completed trip with five `group` photos.
2. Open the Memory screen, snapshot `dna_dimensions` from
   `GET /api/me/memory`.
3. Tap "Let Vesper learn from these" in the consent sheet.
4. Assert no observation, user_fact, personal_memory row, or queued job
   was created naming the photo IDs. Assert the next call to
   `GET /api/me/memory` returns byte-identical `dna_dimensions`.
5. The test should pass today — the bug is that nothing happened, but
   the user was told something would.

**Suggested fix direction:** either (a) ship the wiring before dogfood —
the minimum viable being a Haiku vision summary per opted-in photo
(reuses VI-1 infrastructure in `concierge/agent.py`) that lands as an
observation in `category=photo_evidence`, which then folds into the next
Personal Memory refresh; or (b) gate the sheet behind a feature flag and
remove the DNA-chip promise until the pipeline is real. Pre-dogfood, (b)
is the honest move; the consent ceremony can be brought back the day the
wiring lands.

**Confidence:** High

---

### [P1] — Default photo visibility is `group` with no per-upload consent moment

**References:**
- `Travel Agent/backend/core/db/_tables/trip_photos.py:67` (`visibility` server_default `'group'`)
- `Travel Agent/backend/api/routes/trip_photos.py:140` (`visibility: Visibility = Form(default="group")`)
- `Travel App/app/(tabs)/trips/[tripId]/photos.tsx:120-126` (upload call hard-codes `visibility: 'group'`)
- `Travel App/components/trip/FindPhotosSheet.tsx:156` (batch upload hard-codes `visibility: 'group'`)
- `Travel App/components/memory/PhotoSlotCard.tsx:50-58` → `story.tsx:138` (story-slot upload hard-codes `visibility: 'group'`)
- `Travel App/app/(tabs)/trips/[tripId]/photos.tsx:357-362` (empty-state copy mentions "Everyone in the group can contribute" but does not say "Everything you add is visible to the group by default — long-press to make private.")

**Why it matters to a real tester:** the user taps "Add photos", selects a
photo, and it is *immediately* visible to every other group member
(including its GPS — see the prior finding). The privacy control exists
(long-press → toggle) but is purely opt-out and discoverable only by
accident. For a use case where someone takes 80 trip photos and one of
them is a screenshot of a text from their mom, or a quick shot of a
prescription bottle, that screenshot is now in the shared album by
default. The dogfood tester who notices this after the fact gets a sharp
"why did you publish that?" signal that erodes trust in every default the
product picks.

The "long-press to change visibility" affordance is only mentioned inside
the lightbox accessibilityHint and via an `Alert` triggered on long-press
in the grid — there is no first-upload consent moment, no batch-upload
"these will be visible to your group" confirmation, no per-photo
visibility preview in the album grid (the private lock-overlay only
appears *after* the user has marked it private).

**Repro / deterministic test idea:**
1. Fresh user, fresh group trip with 2 other members.
2. Tap "Add photos", select an arbitrary image, complete the upload.
3. Open the same trip as User B. Assert the photo is visible in
   `GET /api/trips/{trip_id}/photos` with no prompt to User A about
   sharing.
4. Open user A's lightbox on the photo; assert the "Shared" footer pill
   is the *only* hint that this is now group-visible.

**Suggested fix direction:** the minimum honest change pre-dogfood is to
add an inline notice on the first add-photo flow per trip ("Photos you add
are visible to your group — long-press any tile to make it private"). A
stronger version flips the default to `private` until the user
deliberately chooses "share with group" on the first upload (the
empty-state explicitly frames the album as collaborative, so this
question has a sensible answer either way). The current state is "we
chose for you, and we didn't tell you".

**Confidence:** High

---

### [P1] — Trip Story composer ingests arbitrary user-typed block titles into the share-source prompt with no redaction

**References:**
- `Travel Agent/backend/tasks/trip_story.py:227-274` (`_load_confirmed_moments` pulls `itinerary_blocks.title` for every `event_state='happened'` block)
- `Travel Agent/backend/tasks/trip_story.py:299-307, 312-313` (titles land verbatim under `"Events confirmed as happened (anchor the story to these when relevant):"`)
- `Travel Agent/backend/tasks/trip_story.py:46-107` (system prompt has no constraint-omission or "do not surface private-shaped strings" rule)
- `Travel Agent/backend/core/story_projection.py:91-96` (public projection includes every section body that is not on `hidden_section_ids` — the section *body* is always-allowed; redaction is opt-out, not opt-in)

**Why it matters to a real tester:** itinerary block titles are
user-editable. A real tester is going to rename blocks to whatever they
were ("dinner at Yvette's apartment", "doctor visit", "Tom's intervention
talk", "anniversary surgery follow-up"). The composer is told these are
"confirmed moments" to "anchor the story to". The Sonnet system prompt
explicitly encourages opening *in scene* with *specific imagery* from the
anchors. The first paragraph of the story can plausibly read "On Thursday
the visit to the clinic took longer than you'd planned…". That section
body is then default-included in the public projection on share — the
default-deny allowlist guards everything *around* the body (dates, exact
IDs, photo URLs) but the body itself ships unless the owner manually
toggles "hide this section" in the share sheet.

The owner *does* see truncated section bodies in the share sheet's
toggles (`ShareStorySheet.tsx:299-307`), so they have a fighting chance —
but the truncation is 56 characters, which is exactly long enough to
disguise a sensitive second half of a paragraph. And on a per-section
basis, when one of five sections looks innocuous in its first 56 chars
but contains a clinic anecdote in the second half, the owner will tap
"include" and publish it.

**Repro / deterministic test idea:**
1. Seed a trip with an itinerary block titled
   `"Tuesday — surgery follow-up at Hospital São José"`, mark its
   `event_state='happened'`.
2. Run `compose_trip_story` and read the generated section bodies.
3. Assert no section body contains `"surgery"`, `"hospital"`,
   `"follow-up"` (or any term from `_PRIVATE_KEYWORD_PATTERNS` defined in
   `privacy_redactor.py`).
4. With current code the test will fail — the LLM is given the title as
   anchor with no instruction to abstract sensitive nouns away.

**Suggested fix direction:** before sending block titles to the composer,
run them through the same `_PRIVATE_KEYWORD_PATTERNS` family already used
by the group-channel synthesizer (the catalog lives in
`backend/core/privacy_redactor.py`). Substitute hits with a neutral
re-phrasing ("an appointment", "a personal stop") before the prompt is
built. Optionally add a single line to the composer system prompt: *"Do
not name medical, financial, or personal-relationship specifics — if an
anchor mentions one, summarize as 'a personal stop' and move on."*

**Confidence:** Medium — the LLM may shrug off the anchor, but
relying on Sonnet to spontaneously self-censor a "confirmed moment" is
not a guarantee a dogfood tester should bet sensitive trip details on.

---

### [P1] — Section edits funnel the full user-edited paragraph into an importance-8 observation that feeds Personal Memory synthesis

**References:**
- `Travel Agent/backend/api/routes/memory.py:285-309` (every PATCH section creates an observation with `importance=8, source_mode='reflection', category='post_trip_reflection'`)
- `Travel Agent/backend/core/db/observations.py:36-72` (`post_trip_reflection` is not in `_SHAREABLE_CATEGORIES` → auto-inferred `shared=False`)
- `Travel Agent/backend/concierge/refresh_memory.py:30-135` (system prompt instructs to abstract `[private]` observations — but the *content* of the observation is the user-typed paragraph verbatim)

**Why it matters to a real tester:** the Trip Story edit sheet is a
free-text writing surface, often used at a vulnerable moment after a
trip. Whatever the user types goes into the observations table with
importance 8 (top tier — outranks almost every agent-captured
observation), category `post_trip_reflection`, and is fed into the next
`refresh_personal_memory` synthesis. The synthesizer is told the
observation is `[private]` and to paraphrase, but the *raw text* is still
in `observations.content` and is still rendered into the synthesis
prompt. If a future agent path reads the raw observation row (without
going through synthesis) — and there are several: digest pipeline, deep
research, story regenerate's next observation pass — the verbatim
sensitive content can reach a group-visible context. The Personal Memory
drift audit (M-2 in Known Gaps) explicitly flags "Personal Memory is also
read by the group profile synthesizer".

The on-screen toast says
*"Saved · your Concierge learns from edits"* (`story.tsx:219`). The user
has no way to know that a reflection on their mum's funeral trip is now
weighted at importance 8 in the synthesis substrate that other agents
read.

**Repro / deterministic test idea:**
1. Edit a Trip Story section to a body containing
   `"This trip was about saying goodbye to my mother in hospice."`.
2. Read `observations` where `user_id = caller AND category =
   'post_trip_reflection'`. Assert the verbatim string is the
   `content` and `importance = 8`.
3. Trigger `refresh_personal_memory(user_id, trigger='post_trip')`.
4. Inspect the rendered synthesis prompt — assert the verbatim phrase
   appears in the input under the `[private]` tag.

**Suggested fix direction:** keep the edit-as-signal behavior, but
(a) drop the importance from 8 to 4-5 so it sits alongside other reflective
signals rather than dominating, and (b) store a derived summary (e.g.
the first sentence, or a 1-line Haiku abstraction) as the observation
content instead of the full paragraph. The trip_story row already
preserves the raw edited body; the observation only needs the *signal*.

**Confidence:** Medium — depends on how aggressively downstream agents
read raw observations vs. the synthesized Personal Memory. Worth a
formal threat-model review during the M-2 follow-ups.

---

### [P2] — `albumSectionPhotos` falls back to *private* photos as story slot fillers when no group photos exist

**References:**
- `Travel App/app/(tabs)/trips/[tripId]/story.tsx:100-114` (`pool = visible.length > 0 ? visible : photos` — silently includes private photos when no group photos are available)
- `Travel App/app/(tabs)/trips/[tripId]/story.tsx:86-94` (same fallback for `coverPhoto`)
- `Travel App/app/(tabs)/trips/[tripId]/story.tsx:117-129` (priority chain: `albumSectionPhotos < persistedSectionPhotos < sectionPhotos` — auto-fill never gets PATCHed into the slot, so the server-side `_public_photo_urls` allowlist correctly filters it out of public projection)

**Why it matters to a real tester:** the user opens their story and sees
their private bedroom photo prominently used as the hero image and slot
filler — because they had no group photos and the client decided that
*any* photo is better than none. They tap "share" and the privacy preview
correctly shows the slot empty (the server-side allowlist filters the
private URL out). The local view and the published view diverge silently:
the user thinks they are sharing a story with cover X, but their
audience sees no cover. This isn't a *leak* — the server doesn't ship
the private URL — but it is a UX trap where the owner does not realize
their published story is missing imagery, and may have made narrative
choices ("the rain-slicked pavement above") that no longer match what
viewers see.

**Repro / deterministic test idea:**
1. Trip with 0 group photos and 2 private photos.
2. Render `story.tsx` — assert `coverPhoto` is one of the private photos.
3. Open the share sheet — assert the privacy preview shows
   `photos_shown=0` (it will).
4. The bug: the surface above the share sheet showed a hero image; the
   share itself ships none.

**Suggested fix direction:** drop the `visible.length > 0 ? visible :
photos` fallback. If no group photos exist, show the story with no
imagery — and use the empty hero as the user-facing signal that they
should add group-visible photos to give their published story a cover.

**Confidence:** High

---

### [P2] — The Trip Story composer prompt is marked v1 / un-tuned; no eval coverage exists

**References:**
- `Travel Agent/backend/tasks/trip_story.py:14-18` ("Prompts in this module are **v1 / un-tuned** — they should be evaluated and iterated through the eval framework before production.")
- `tools/eval/configs/concierge/` — no scenario evaluates the composer; the only Trip Story tests are unit-mock the LLM output.
- No `judge_*` or `reply_acknowledges` check exists for hero_title quality, section body grounding, or anchor_observation_id usage.

**Why it matters to a real tester:** the Trip Story is the compounding
artifact and the share source. Its prompt has been shipped without ever
being exercised against a real fixture trip with real observations under
the eval framework. Regressions on hero quality, anchor accuracy, or
voice will be detected only by dogfood eyeballing. The eval-coverage
audit O-17 already flags `SKILL_PHASE_POST_TRIP` and post-trip surfaces
as a top-tier gap; the composer prompt is the next layer of that gap.

**Repro / deterministic test idea:** N/A — the gap is the absence of
test coverage, not a defect.

**Suggested fix direction:** add a `trip_story_compose` scenario under
`tools/eval/configs/concierge/` with a fixture trip whose
`overall_arc`, observations, and confirmed moments are all hand-tuned.
Check (a) hero_title length 4-8 words and no city name unless earned,
(b) all section IDs slug-valid and unique, (c) each section body is
2-4 sentences and does not contain banned openers ("On day…"), (d)
`anchor_observation_id` is either null or in the input set. Land before
the first prompt tweak — currently any edit ships blind.

**Confidence:** High

---

### [P2] — Section-toggle labels in `ShareStorySheet` truncate at 56 chars, hiding the sensitive tail

**References:**
- `Travel App/components/memory/ShareStorySheet.tsx:77` (`_truncate(s, n=56)`)
- `Travel App/components/memory/ShareStorySheet.tsx:295-310` (per-section "include" toggles use `_truncate(s.body)` as label)

**Why it matters to a real tester:** the per-section toggles are the
owner's last line of defense before publishing — if the composer wrote
something they'd rather not share, this is where they catch it. A 56-char
truncation of a 200-300 char section body shows only the first sentence
or so. A section body that opens "The morning was the best part of the
trip — coffee in the square, the light just before noon, and then the
afternoon at the hospital with my dad's results" is going to look
shareable in the toggle label; the user toggles "include", publishes,
and the latter half ships.

**Repro / deterministic test idea:**
1. Compose a story with a section body whose first 56 chars are
   innocuous and whose 57th+ chars contain a sensitive keyword.
2. Render `ShareStorySheet` — assert the toggle label shows only the
   innocuous prefix.

**Suggested fix direction:** either render the *full* body in a
scrollable preview row in the share sheet (the sheet is already
modal-tall, room is available), or expand the truncation to ~140 chars
*and* add an inline "tap to preview full" disclosure for any
section that exceeds the truncated label.

**Confidence:** High

---

### [TECH-DEBT] — `_validate_story_photo_url` requires CDN config to be set, otherwise 503s

**References:**
- `Travel Agent/backend/api/routes/memory.py:430-438` (raises 503 when `media_settings.cdn_base_url` is empty)

**Why it matters to a real tester:** a fresh local dev environment that
hasn't set `MEDIA_CDN_BASE_URL` will see story photo PATCH endpoints
respond 503 with `"photo upload destination is not configured"`, which
reads as "the service is broken". This is the right *security* posture
(don't accept arbitrary hosts), but the failure message is opaque and
the surrounding photo *upload* path works (CDN config is also used
there). The mismatch confuses devs.

**Suggested fix direction:** in dev/local mode (or when
`ENV != production`), allow a permissive `localhost:*` allowlist with a
loud warning log, and keep the 503 only in production environments.
Alternatively, fail at *startup* when CDN is unconfigured so the
inconsistency surfaces immediately.

**Confidence:** Medium

---

### [TECH-DEBT] — `compose_trip_story` reads `get_active_observations(user_id, trip_id=trip_id, limit=7)` — top-N selection ignores `importance`

**References:**
- `Travel Agent/backend/tasks/trip_story.py:143`
- `backend/core/db/observations.py` — `get_active_observations` orders by `created_at DESC` by default.

**Why it matters to a real tester:** the composer's "top observations"
anchors come from the latest 7 observations on this trip, regardless of
importance score. A user who had a chatty afternoon will dominate the
story with low-importance recency over higher-importance trip-defining
moments. Compared to `post_trip_character_read._fire_character_read_for_member`
which uses the same limit-3 call (also recency-ordered, same caveat
applies there), the inconsistency means the character read and the trip
story can disagree on what the trip was about.

**Suggested fix direction:** order by `importance DESC, created_at
DESC` (matches `_format_observations_for_synthesis`'s ranking key in
`refresh_memory.py:528-534`), and pull a wider window (e.g. 15) so the
composer has signal density without losing the high-importance head.

**Confidence:** High

---

## Known / Accepted

The following items were inspected and judged *out of scope for this
audit's P0-P2 list* — they belong to existing gaps or to areas owned by
sibling audits.

- **Post-trip personal memory refresh path (M-2 residuals).** The
  `Personal Memory drift modes` are tracked as M-2 in `Known Gaps
  Register.md` and were not re-litigated here. The `post_trip_memory_refresh`
  subscriber correctly schedules durable T+3h refreshes with idempotent
  `scheduled_tasks` rows; the audit does not introduce findings that
  would change the M-2 trigger criteria.
- **`PublicTripStory` default-deny allowlist.** The projection in
  `backend/core/story_projection.py` is exactly the right shape — every
  finding above either feeds the allowlist (and is filtered out) or
  bypasses it through a separate channel (block titles, embedded
  co-traveler photos). The allowlist itself is not a defect.
- **EXIF stripping on served bytes.** `media/variants.py` correctly
  strips EXIF via Pillow's WEBP encoder defaults. The only EXIF that
  survives is the GPS data the backend deliberately extracted into a
  typed column (covered in the GPS finding).
- **Captured-moment / dwell write-back.** `core/memory_signal.py`
  correctly excludes `view`/`dwell` from observation creation; only
  deliberate `save`/`share`/`regenerate` actions become observations,
  and even those are stamped `shared=False, importance=4`.
- **Character read scope.** `post_trip_character_read._fire_character_read_for_member`
  uses `get_active_observations(user_id, trip_id=trip_id, limit=3)` and
  delivers into the member's personal 1:1 session — no cross-member
  observation leak. The recency-vs-importance ordering caveat is tracked
  under the TECH-DEBT above.
- **`trip_story_subscriber` durable scheduling (Reliability F0-1).** The
  T+2h pre-warm uses `scheduled_tasks` with `UNIQUE (task_kind,
  scope_id)`, the daily backfill covers missed runs within 7 days, and
  the GET endpoint enqueues on demand with a deduping `_job_id`. The
  audit does not surface scheduling gaps beyond the T+2h `_PREWARM_DELAY_SECONDS`
  constant which is documented and consistent across this module and
  `post_trip_subscribers.py`.
- **SSRF / image-bytes guard.** `_validate_public_url` + the redirect
  re-validation in `media/rehost.py:_download` are correct (B11 audit
  fix). No new finding.
- **Story share allowlist for plan-similar derivation.** `build_plan_seed`
  reads only from the `PublicTripStory` projection — no private inputs
  reach the derived trip seed. Coordinated with the privacy area's P0
  (which lives in invite_snapshot, not story share) — no overlap.
