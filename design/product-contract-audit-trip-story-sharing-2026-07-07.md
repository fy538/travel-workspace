# Product Contract Audit — Trip Story Public Sharing (2026-07-07)

Audits the "Implement MVP public story sharing" feature (shipped `travel-app` + `travel-agent`, last ~24h) against `Vesper Trip Story and Memory Handoff.html` (handoff 118/119) — specifically its **19 canonical decisions**, **8 redaction-composition rules**, **26-item implementation checklist**, and **26 tracked events**. Method: 3 parallel code-grounding investigations against the verbatim canon text (not paraphrase), each independently verified with file:line evidence. Companion doc: `surface-inventory-diff-trip-story-sharing-2026-07-07.md`.

Existing FE doc `travel-app/docs/surfaces/external-sharing/contract.md` covers some of this ground already — this audit is broader (checks against the full 118/119 canon, not just the FE's own acceptance rules) and found gaps that doc doesn't mention.

## 🔴 Real privacy leaks — fix before dogfood, regardless of any Atlas/Trip-Story freeze decision

### LEAK 1 — Story title can name the hidden destination
**Canon acknowledges this exact gap already** ("the story title itself may name the destination... title redaction is not yet modeled — flag for a follow-up pass"). Confirmed **still open** in shipped code, and now spans **three surfaces**, not the one canon anticipated:
- `backend/core/story_projection.py:70-82` (`safe_hero_title`) filters titles against `check_private_signal` + co-traveler names only — it does **not** check whether the title names the destination when `show_destination=False`.
- A title like *"What Lisbon Gave Us"* with destination hidden sails through unfiltered and renders verbatim in:
  - JSON projection `hero_title` field
  - HTML `<title>`/`<h1>`/OG title/Twitter title (`backend/api/routes/story_landing.py:154,187,190,194`)
  - The 9:16 share card's title text (`backend/core/story_card.py:319`)

**Fix shape**: `safe_hero_title` needs a destination-name check (against the trip's actual place name/aliases) parallel to its existing private-signal check, applied whenever `show_destination=False`.

### LEAK 2 — 9:16 share card's map thumbnail bypasses redaction entirely
`backend/core/story_card.py:227-316` (`_place_lonlat_for_trip` → `build_story_card_png`) fetches **real city-level coordinates from `places.centroid`** and overlays a geographic map thumbnail on the card — **unconditionally**, never checking `RedactionPolicy.show_destination` or consulting `route_cue`/`route_cue_is_geographic` at all. This is a **second, projection-blind code path**: while the JSON/HTML projection correctly nulls out destination fields, the PNG card generator queries raw trip/place data independently and can render a real map of the trip's actual location even when the owner explicitly hid the destination.

**Fix shape**: gate the map-fetch call on `policy.show_destination` (or better, have the card renderer consume `route_cue`/`route_cue_is_geographic` off the already-built projection instead of independently querying `places`/`trips` — this also closes the architectural gap where a second builder can drift from the first).

## 🟡 Confirmed canon-decision violations

### Decision #19 violated — owner opening their own link doesn't route to Share/Manage
> *"'Open in Vesper' never exposes owner-only controls to a public recipient; the owner's own link always routes to Share/Manage, never the public-only viewer."*

The backend groundwork is **built correctly** — `GET /api/public/stories/{slug}/viewer-context` returns `PublicStoryViewerContext{is_owner, is_available, trip_id}`, scoped so only the real owner sees `trip_id` populated (`story_landing.py:84-113`). But it has **zero FE consumers** — grep across the entire `travel-app` repo for `viewer-context`/`viewerContext`/`is_owner` returns nothing. `app/stories/[slug].tsx` always renders the anonymous public view. **An owner tapping their own shared link today sees the stranger's view of their own story** — not a leak (no private data exposed), but a real, confirmed contract violation and a bad owner experience (no path back to Share/Manage from the link itself).

### Decision #16 violated — "Plan Similar continues into a conversation" is a static illusion, not a real conversation
> *"Plan Similar continues into a conversation, not a picker form, matching Trip Creation's conversation-first canon."*

`handlePlanSimilar` (`app/stories/[slug].tsx:324-327`) only flips local UI state (`setPlanStarted(true)`). The subsequent `PlanCTA` block renders **hardcoded static text** styled to look like a Vesper chat turn (`planSimilarOpeningLine`/`planSimilarPrompt`, pure string functions, lines 282-307) — it never navigates to the real concierge chat screen, never imports `utils/conversationSeed.ts`, never constructs a `ConversationSeed`. Tapping "Save this trip" fires a plain REST POST, not a chat message. **This is a third thing, not "conversation" or "picker form"** — an in-place fake-chat illusion. Notably, the existing smoke test (`__tests__/screens/public-story.smoke.test.tsx:115-129`) only asserts the static text swap — it doesn't test real navigation, so it certifies the illusion rather than catching the gap.

**Fix shape**: `handlePlanSimilar` should navigate into the real conversational entry (the same `app/trip-begin.tsx` → concierge-chat path this session's own loop-closure work uses), seeded via `ConversationSeed` built from the `PlanSimilarSeed` fields — not render fake chat bubbles in place.

### Decision #17 not met — Inspired Trip attribution is written but never shown
> *"A saved Inspired Trip carries quiet source attribution ('Inspired by a public Vesper story') without leaking any field the source projection had hidden."*

Backend correctly writes attribution to `trip_sources` (`backend/core/db/plan_similar.py:98-143`, `_create_trip_with_source`) — but grep across the FE trip-folio/trip-home code for `public_story_source`/`TripSource`/`source_share_id`/"Inspired Trip" returns **zero matches**. The attribution renders exactly once — pre-save, in `PlanSeedPreview` on the public landing page — and is **never read back or shown anywhere after the trip is created.** So the write path works, the read path doesn't exist.

**Secondary, smaller issue**: the shipped copy is *"Inspired by a public Vesper story"* — canon's mandated string is *"Based on a shared Vesper story."* Consistent throughout code/tests (a deliberate string, not a bug), but doesn't match canon; flag for a copy fix alongside the read-path build.

## 🟢 Confirmed clean — worth stating so this audit isn't read as all-negative

- **Decision #03** (opt-in, redaction-first, no auto-publish) — clean.
- **Decision #05** (public viewer never exposes owner-only controls) — clean; verified no Rewrite/Add Photo/Edit/Atlas-toggle reachable from the public route.
- **Decision #11** (Plan Similar seed generated only from the projection, never raw data) — clean, with one narrow watch-item: `create_trip_from_share` does pull `source_trip.place_id` directly, but only when `destination_seed_is_exact=True` (i.e., only when the projection already disclosed it exactly) — defensible, but worth a second look if that exactness gate is ever loosened.
- **Decision #18** (preflight is advisory, never blocking) — clean; verified `OwnerPreflight`'s readiness booleans feed nothing into the "Create link" button's `disabled` state.
- **Public viewer never touches raw trip/story data directly** — architecturally sound (types exclusively as `PublicTripStory`, single fetch path) — **except** for LEAK 2's independent map-fetch side channel, which is the same architectural crack.
- **"Public unavailable" collapses to one generic state** for every real call site in this feature today (`app/stories/[slug].tsx` never passes a specific reason; backend collapses revoked/paused/wrong-visibility to a uniform `None`/404/410). **Caveat**: this is caller discipline, not a structural guarantee — `PublicUnavailableState.tsx` itself supports a `reason` prop that *could* leak a specific cause if a future call site passed one. Worth hardening with a lint/type-level guard, not urgent today.
- **Auth-gating** (Plan Similar: free to start, login only to save) — clean, verified via 401-redirect flow.
- **Photo allowlist hardening** (`_public_photo_urls`, `trip_story_shares.py:566-604`) — real, deliberate defense against a co-traveler's private photo landing in a shared slot.
- **Non-owner reaching owner controls** — does not occur (the violation found is one-directional: owner reaching the *public* view, never the reverse).

## 🟠 Data-contract gaps (narrower schema than canon specifies — not leaks, but real scope gaps)

- **`RedactionPolicy` ships 3 of canon's 8 fields**: `show_dates`, `show_destination`, `hidden_section_ids`. Missing: `hide_people_names` (people-redaction is auto-applied via name-detection, not an owner toggle), `hidden_photo_ids`, `hidden_place_ids`, `hide_route_cue`. Semantics are also inverted vs. canon (`show_*` vs. canon's `hide_*`) — cosmetic, but worth normalizing if the schema ever needs to interop with anything written against the canon's naming.
- **`generalized_place_chips` and `route_cue` exist on the `PublicTripStory` model but are permanently hardcoded to empty/`None`** (`story_projection.py:208-211`) — never populated even when destination is hidden, which is exactly when canon wants them to carry the fallback experience. Dead code on both ends (FE renders them conditionally; BE never populates them).
- **`ShareLink` ships 7 of canon's 13 fields cleanly; 6 are absent**: `paused_at`, `rotated_at`, `replaced_by_share_id`, `expires_at`, `unique_viewers`, and `plan_similar_starts` as a named field (a `conversions` count exists but measures something subtly different — completed trip-derivations, not "starts"). Rotation creates a disconnected new share row with no lineage back to the old one.
- **Redaction composition rules 2/3/4** (destination-hidden variants) are functionally safe (no leak) but their canon-specified fallback experience — generalized place chips, non-geographic route cue, specific copy like *"A trip, kept private"* — **doesn't exist**; the real FE just shows generic fallback text, and rule 4 (hide destination + hide place chips) can't even be exercised since there's no `hidden_place_ids` control at all.
- **"Full recipient preview before publish"** (a distinct checklist item) isn't built as a separate pre-publish surface — pre-publish, the owner only sees the compact inline `PreviewCard`; the "full" preview reuses the live post-publish page.
- **"Open in Vesper" logged-in vs. logged-out differentiation** doesn't exist — the public viewer always renders the same anonymous view regardless of auth state.

## 🔵 Analytics — the tracked-events layer is effectively non-functional

**All 13 canon-named events checked (9 owner-side + 4 Plan-Similar-side) are MISSING as literal strings** in either repo. The real implementation uses a completely different, pre-existing taxonomy: `logShareEvent()` → `POST /api/memory/interactions` → a generic `MemoryInteractionCreate{surface, interaction, metadata_}` shape, where `interaction` is one of a small fixed enum (`dwell|share|save|unsave|view`) and the actual action lives in free-form `metadata_.action`.

**More severe**: `backend/api/routes/memory.py:754-776`'s own docstring states *"memory_interactions table was dropped 2026-06-20 (insert-only, no consumers)."* The endpoint now only synthesizes a side-effect for `interaction in ("save","share")` — **everything else is silently discarded**, including a fake ack UUID returned to make the caller think it worked. So most of these 13 events don't just have the wrong name — they write to nothing.

Two server-side events do exist independently (`opened`, `plan_similar_started`, in `trip_story_share_events`), but: `opened` fires on *every page load*, not the canon-specified CTA-tap moment; `plan_similar_started` fires at **save** time, not when the seed screen is first reached pre-login as canon specifies ("seed screen reached BEFORE login") — the event name survived but its lifecycle meaning didn't.

**Practical consequence**: there is currently no way to answer "how many people copied the link vs. shared it vs. tapped Plan Similar vs. actually started the seed flow" — the feature is unmeasured beyond a crude, mostly-discarded save/share fold.

## Recommended fix order

1. **LEAK 1 + LEAK 2** (title destination-leak, map-thumbnail bypass) — genuine privacy bugs in shipped code. Fix regardless of any Atlas/Trip-Story investment-freeze decision; these are bugs in what already exists, not new feature work.
2. **Decision #19** (owner-routing) — the fix is almost free: the backend endpoint already exists correctly; this is a small FE wiring task (call `viewer-context` on load, redirect to Share/Manage if `is_owner`).
3. **Analytics** — either wire the 13 real event names into a working pipe, or consciously accept the current fold-into-generic-engagement model and update canon to match reality. Don't leave it silently half-built; the underlying table being dropped means today's design intent (per-event owner-side analytics) is unreachable without new backend work.
4. **Decision #16** (fake conversation) and **Decision #17** (missing Inspired-Trip attribution read-path) — real product-experience gaps, not privacy risks. Scope as a proper follow-up batch once 1–3 are closed.
5. **Data-contract gaps** — lowest urgency; the MVP subset works for what's actually exposed in the UI today. Expand only when a UI need for pause-timestamps/expiry/rotation-lineage/unique-viewer-counts actually arises.
