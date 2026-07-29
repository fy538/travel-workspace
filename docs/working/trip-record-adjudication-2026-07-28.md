---
doc_type: working
status: active
owner: founder / eng
created: 2026-07-28
expires: 2026-08-27
why_new: The trip-artifacts vision doc (same day) proposed a disposition
  table for ~9 post-trip generator mechanisms and a Trip Record contract,
  both marked "needs founder ruling / verify against code". This doc is
  that verification pass. It contains RULINGS grounded in a full code
  trace, and it CORRECTS three load-bearing errors in the vision doc.
promotes_to: folds into docs/product/ with the vision doc if the dogfood validates
supersedes: []
amends:
  - docs/working/trip-artifacts-vision-2026-07-28.md   # AD1, AD2, build order, "postcard unbuilt"
depends_on:
  - docs/working/home-surfaces-program-2026-07-28.md   # seam S1/S3 rules
source_of_truth_for:
  - trip-artifact-mechanism-rulings
  - trip-record-assembly-contract
---

# Trip Record — adjudication

> **Headline: the vision doc was wrong in a useful way.** It assumed this
> area was 9 fragmented half-built generators needing a new substrate.
> The code says otherwise: **Trip Story is already the per-member trip
> artifact, it is LIVE IN PRODUCTION, and it already has the public share
> path, the photo slots, the voice, and the FE surfaces the vision
> proposed building.** The consolidation is therefore not "build a record,
> then renderers." It is: **extract the assembly Trip Story already does
> into a shared record, and make every other artifact a SECTION or a
> SCOPE of it rather than a competing object.**

## Three corrections to the vision doc

**C1 — AD2 is REVERSED. Trip Story survives; it is the primary artifact.**
The vision doc proposed "Unpacked survives; trip_story is merge-or-kill."
That was based on LOC count, not behaviour. In fact:

- `trip_stories` is keyed `UNIQUE (trip_id, user_id, version)` — **already
  per-member**, exactly the granularity the vision asked for
  (`backend/core/db/_tables/trip_stories.py:44-72`).
- Composition **fans out over `get_trip_members(trip_id)`**, one story per
  member, with per-member failure isolation
  (`backend/tasks/trip_story_subscriber.py:129-132`).
- It is **live in prod**: no feature flag gates composition. The only gate
  is `DISABLE_LLM_BACKGROUND_LOOPS`, which **`fly.toml:274` sets to
  `"false"`** ⇒ enabled. Three composition paths run: `trip.completed` →
  T+24h scheduled task, on-demand `GET /api/trips/{id}/story` (202
  composing), and a daily backfill loop (`lifecycle.py:500`).
- It has **5 tables** (story, audio, shares, sources, share_events), **~15
  API routes** + 7 share routes + a public landing, and full FE:
  `app/(tabs)/trips/[tripId]/story.tsx` (912 LOC),
  `app/stories/[slug].tsx` (962), `ShareStorySheet.tsx` (1212).
- It has **photo slots**, **TTS narration**, **provenance**, **user
  corrections**, and **feed producers** (`home/feed.py:1013`,
  `concierge_feed/producers.py:1031-1046`, tier 2 in `home/policy.py:45`).

**Unpacked is not its competitor — it is a different scope.**
`build_unpacked(user_id, year)` is **per-user, per-calendar-year**, not
per-trip (`backend/atlas/unpacked.py:57`). Trips contribute only a count.
The vision doc's "The Year, Unpacked" *is* this mechanism, already built.
Both survive. Nothing merges.

**C2 — The Postcard is not a design; it is real code, two config values
from live.** The vision doc listed it as "designed: 10 rules". Reality:
`backend/postcard/` (~373 LOC) with a **complete `ReplicatePostcardProvider`**
(httpx predictions API, polling loop, timeout, CDN rehost of the expiring
provider URL), `render.py` guard ladder, DB columns migrated
(`atlas_artifacts.hero_photo_url`, `rendered_image_url`, `render_status`;
`users.atlas_render_enabled`), a real upload endpoint
(`POST /api/atlas/photos/upload`, `routes/atlas.py:1827-1880`), a real
render endpoint (`:2010-2068`), unit tests, and a wired FE
(`components/atlas/MakePostcardButton.tsx` with picker → upload → render).
Dark at three gates: `postcard_render_enabled=False`
(`core/settings.py:170`), `provider="null"` + empty key/model
(`:177-181`), and per-user `atlas_render_enabled=false`.
**Note: "riso" is a prompt string, not image processing** —
`_RISO_STYLE_PROMPT` at `routes/atlas.py:2002-2007`. All styling is
delegated to the hosted img2img model. Env prefix is `RESEARCH_`, so the
var is `RESEARCH_POSTCARD_RENDER_ENABLED` (set nowhere).

**C3 — The public "share to a non-user" path already exists, twice, and
is dark by one flag.** The vision doc treated web artifact render as a
later question (AD6). Both implementations are complete:
- **Stories** — `/stories/{slug}` landing + `card.png` og:image, and
  `/stories/*` **is claimed in AASA** (`routes/invite_landing.py:604-615`).
- **Unpacked** — HMAC token → revocable `atlas_unpacked_shares` row →
  unauthenticated server-rendered HTML with og:image + open tracking +
  owner revoke UI. `/unpacked/*` is **not** AASA-claimed.
Both minting paths gate on `STORY_SHARING_ENABLED` (unset ⇒ off) plus FE
`STORY_SHARE_ENABLED = false` (`constants/featureFlags.ts:17`). Serving of
existing links is **not** gated. Needs `ATLAS_SHARE_SECRET` +
`STORY_SHARE_BASE_URL` to go live.

## The rulings (AD1)

| # | Mechanism | RULING | Evidence / rationale |
|---|---|---|---|
| 1 | **Trip Story** | **KEEP — promote to THE trip artifact.** Its `sections[]` array becomes the extension point for every new trip-scoped artifact idea. | Per-member, live in prod, 5 tables, 15 routes, public share, photo slots, narration, feed producers, full FE. Already ~80% of what the vision proposed building. |
| 2 | **Character read** | **KILL.** Fold its intent into a Trip Story section. | Produces no artifact — only a chat turn in the personal side-chat (`post_trip_character_read.py:102`). Zero consumers repo-wide beyond that chat. **And it is broken** — see Defect D1. Its one distinct value (an interpretive POV on who you were) is a *section*, not a mechanism. |
| 3 | **Unpacked** | **KEEP — it is "The Year", a different scope.** Not a competitor to Trip Story. | `build_unpacked(user_id, year)`, per-user-per-year, recomputed on read, no persistence. |
| 4 | **On This Day / anniversary** | **KEEP as a re-surfacer.** In-app strip live; push stays dark for now. | `list_on_this_day` derived query, no table. In-app path has **no flag** (`routes/atlas.py:168`). Push gated by `ANNIVERSARY_PUSH_ENABLED`, unset everywhere in repo. |
| 5 | **Postcard (img2img)** | **KEEP — reclassify from "unbuilt" to "config-gated".** First artifact to light up. | See C2. Two config values + one flag. |
| 5b | **Postcard (artifact *style*)** | **KEEP, distinct thing.** Do not conflate. | `ArtifactStyle` literal + `ATLAS_COMPOSE_SYSTEM_POSTCARD` prompt (`atlas/prompts.py:155-196`) — a narrative voice, fully live. Unrelated to the image render. |
| 6 | **Daily reflection** | **KEEP as infrastructure, NOT an artifact.** Out of this area's scope. | `reflection_log` has no product consumer (admin route only, `admin.py:345`). Its real value is side effects: `observations` + `personal_memories` → Atlas DNA. |
| 7 | **Atlas letter-hero suite** | **FREEZE surface.** No polish work. | Confirmed off the tab bar (`href:null`); lives under You. Vision's "The Letter" is ruled a Trip Story section (see below), so the substrate is not needed as a separate artifact. |
| 8 | **Place affinity** | **KEEP — widest-consumed mechanism in the codebase.** | No flags, live. ~25 consumer sites across routes, feed producers, concierge context, planning, world model, Atlas, Discover, and Trip Story itself (`trip_story.py:455-458`). |
| 9 | **Digest** | **OUT OF SCOPE.** Not a trip artifact. | Confirmed. |

### The architectural ruling that falls out of this

The vision doc listed 8 artifact ideas (Postcard, Credits, Letter, Almost,
Map, Ledger, Year, Return) as peers. **They are not peers.** Ruling:

- **One artifact per SCOPE.** Trip → Trip Story. Year → Unpacked.
  Moment → Atlas artifact. Nothing else mints a new object type.
- **Everything else is a SECTION or a RENDER of those.**
  - *The Letter* → a Trip Story section (voice/POV). **Not a new object.**
    Absorbs the killed character read.
  - *The Credits* → a Trip Story section, **deterministic** (no LLM,
    `confidence=1.0`, zero fabrication surface).
  - *The Almost* → a Trip Story section, sourced from `change_proposals`.
  - *The Map* → a render of existing `map_points`.
  - *The Companion Ledger* → a cross-trip **aggregate query**, surfaced in
    Unpacked and in next-trip concierge context. Not an object.
  - *The Return* → On This Day, already built.
- **Consequence:** the extension point is `trip_stories.sections[]`
  (`models/trip_stories.py:48-59`). One small change is required —
  today sections are produced only by the LLM composer; deterministic
  sections need a non-LLM insertion path. That is the single highest-value
  piece of new plumbing in this whole area.

## The Trip Record contract

**Ruling: the Trip Record is an ASSEMBLY FUNCTION, not a new table.**
Trip Story already fans out per member and already reads most of these
sources — it just does so inline. Adding a parallel persisted record would
duplicate `trip_stories`. Instead:

```
build_trip_record(trip_id, user_id) -> TripRecord      # pure, no LLM, no writes
```

- `compose_trip_story` consumes it (replacing `_load_composition_signals`
  + its inline reads at `trip_story.py:357-458`).
- Deterministic sections (Credits, Almost) consume it directly, no LLM.
- Future renderers consume it. **No renderer may read raw tables.**
- Persist only if profiling demands it. Derived-first, same posture as
  `build_unpacked`.

### Fields, mapped to real sources

| Field | Source (verified) | Status |
|---|---|---|
| Trip identity (title, dates, destination) | `trips` + `trip_summary` | ✅ exists |
| Members + roles | `trip_members` (`role ∈ organizer\|member`, `joined_at`) | ✅ exists |
| Happened blocks | `itinerary_blocks ⋈ itinerary_days`, `event_state='happened' AND status != 'cancelled'`, latest itinerary | ✅ exists (`trip_story.py:413-434`) |
| Narrative arc | `trip_digests` where `digest_type='trip_summary'` → `content["overall_arc"]` | ✅ exists |
| Personal observations | `observations`, user+trip scoped, `get_active_observations` | ✅ exists |
| Loved places | `place_affinity.get_loved_places(user_id, destination_name)` | ✅ exists |
| Photos | `trip_photos` via `list_geotagged_photos_for_map` | ✅ exists |
| **Credits — who proposed/decided** | `change_proposals.proposed_by` + status | 🟡 exists, retention unverified |
| **Credits — who booked/claimed** | booking claim mechanic | ❌ **NOT BUILT** — booking plan WS3.1 |
| **Credits — who settled** | expenses/settlement ledger | 🟡 exists, never joined to this area |
| **Counterfactuals (The Almost)** | `change_proposals` (rejected/superseded), `active_proposals` | 🟡 exists, retention of *rejected* options unverified |
| **Companion tally (cross-trip)** | `trip_members` self-join across the user's trips | 🟡 derivable, not built |
| **Per-member attendance** | — | ❌ **GAP.** No per-member block presence exists. **MVP ruling: attendance = membership** (all members "were there" for happened blocks). Revisit only if a real trip disproves it. |

### The joiner problem — partially already solved

The vision doc claimed a quiet joiner ends a trip with nothing. **Partly
false.** `has_trip_story_composition_signal` skips only when *all three* of
(digest arc, observations, happened blocks) are empty
(`trip_story.py:236-243`), and **happened blocks are trip-scoped, not
user-scoped** — so a silent joiner still gets a story. What they get is a
*generic* one: no personal observations, and `get_loved_places(user_id,…)`
returns empty. **The gap is quality, not existence** — which is a much
cheaper problem, and the Credits/Almost sections (group-sourced, not
signal-sourced) fix it directly.

## Defects found (report-only; not fixed in this pass)

**D1 — Character read never notifies, and burns the group budget.**
`post_trip_character_read.py:116` sets `target_audience: "individual"` —
a value used nowhere else in the repo (`"private"` / `"group"` are the
real ones). `record_notification_dispatch` branches `== "private"`, else
**group fan-out** (`notifications/state_updater.py:270,296`). The group
path calls `on_notification_sent` with `content_provenance=None`, which
raises `ValueError("group proactive copy must carry verified
group_compose provenance")` (`:82-83`) — caught and swallowed per
recipient (`:324-330`). Net: **no `notification_outcomes` row and no push
for any character read**, while `increment_group_messages_today(trip_id)`
still fires once per member (`:333`), consuming the trip's group
notification budget. Moot if D1's mechanism is killed per ruling #2 —
but the budget consumption is live in prod today.

**D2 — Trip Story ships un-tuned prompts with nothing gating them.**
`trip_story.py:15-17` self-flags the v1 prompts as "un-tuned … should be
evaluated … before production", yet composition has no feature flag and
runs in prod. Worth a deliberate look before the dogfood, since this is
the artifact users will actually receive.

**D3 — `atlas_almanac_summaries` has no production writer.** Only the
dogfood seeder writes it (`tools/dogfood/content/seed.py:1313`);
`upsert_almanac_summary_pending` has zero callers. Unpacked's `year_named`
card therefore **always** falls back to the deterministic `The year 'YY`
outside dogfood.

**D4 — Unpacked actor controls are dark from the app.** `card_kinds` and
`expires_in_days` are accepted by `POST /share` but the FE client sends
only `?year=` (`utils/api/http.ts:3216-3221`), so the declared
`actor_controls={stats,highlights,expiry}` in the projection contract are
unreachable. Also: the projection contract's `allowed`/`prohibited` sets
are **declarative only** — nothing enforces them at runtime; safety is by
construction plus tests.

**D5 — Story section edits can be silently lost on regeneration.**
Preservation matches on section `id`; if the composer re-mints ids for the
same beats, user edits vanish (`trip_story.py:308-312`, acknowledged
in-code). Unverified whether it occurs in practice.

## Revised build order (amends the vision doc)

The vision said Postcard → Credits → Letter. Corrected:

0. **Config unlock, not a build** *(hours)* — decide on lighting
   `RESEARCH_POSTCARD_RENDER_ENABLED` + Replicate key/model, and
   `STORY_SHARING_ENABLED` + `ATLAS_SHARE_SECRET` + `STORY_SHARE_BASE_URL`.
   Two entire artifact capabilities are behind config, not code. **⬜ Not
   started — a founder config decision (AD7/AD8), not an engineering task.**
1. ✅ **DONE (`0ff653ca`).** `build_trip_record()` assembly function +
   refactor `compose_trip_story` onto it — no behaviour change, pure
   consolidation. Lives in `backend/core/trip_record.py`.
2. ✅ **DONE (`0ff653ca`).** Deterministic section insertion path —
   `upsert_deterministic_section()` in `backend/core/db/trip_stories.py`.
3. ✅ **DONE (`6547ff48`).** The Credits section —
   `backend/tasks/trip_story_credits.py`. Organizer + booking-claim credit
   (via the booking coverage work that landed the same day) + settlement
   credit, all three sourced through `TripRecord.credits`.
4. ✅ **DONE (`0cf660fb`).** The Almost section —
   `backend/tasks/trip_story_almost.py`. Verified `change_proposals` DOES
   retain rejected/superseded options (real DB CHECK, not derived) — the
   adjudication's own open question, resolved in the same pass.
5. ✅ **DONE (`9df26e25`).** The Letter section —
   `backend/tasks/trip_story_letter.py` (LLM-authored, v1/un-tuned prompt
   ported from character_read). `post_trip_character_read.py` and its test
   are deleted; the two files that referenced it are updated.
6. ⬜ **Not started.** Companion tally → Unpacked + next-trip context. On
   This Day push. Goes through the home-surfaces stream (touches the
   surfacing layer, unlike everything above).

## Open decisions

| # | Decision | Recommendation | Status |
|---|---|---|---|
| AD7 | Light the postcard render? (cost: Replicate per-image + a daily cap already at 3) | Yes for dogfood — it is the highest visual payoff per unit effort in the codebase right now | ⬜ open |
| AD8 | Light `STORY_SHARING_ENABLED` for dogfood? | Yes — the share loop is the venture-gate mechanism and it is fully built and tested | ⬜ open |
| AD9 | D2 — evaluate/tune the v1 story prompts before dogfood? | Yes; this is what users receive. Now also covers The Letter's v1 prompt (step 5). | ⬜ open |
| AD10 | Kill character read now, or after The Letter section lands? | Kill the *loop* now (stops the budget burn), keep the file until the section exists | ✅ done — loop killed `9238bc31`, file deleted `9df26e25` |
| AD11 | AASA-claim `/unpacked/*` to match `/stories/*`? | Only if Unpacked sharing ships to real users | ⬜ open |
| AD12 | Wire steps 3-5's compose_* functions to a trigger (new) | Fold into `trip_story_subscriber.py`'s existing per-member fan-out, right after narrative composition — same file, one more call each, no new loop | ✅ done — `49f13bf1` |

## Sequencing

Nothing here touches `concierge_feed` except step 6's surfacing, so
**steps 0–5 are free of the home-surfaces program's seam S1/S3 ordering**
and can proceed in parallel with it. Step 6 goes through that stream.

**Status as of 2026-07-29: steps 1-5 complete AND wired (AD12).** Every
Trip Story section — narrative, Credits, The Almost, The Letter — now
composes automatically at T+24h for every member, via the existing
`trip_story_subscriber.py` fan-out. Remaining: step 0 (config unlock,
founder decision — AD7/AD8), step 6 (companion tally + On This Day
push, goes through the home-surfaces stream), and AD9/AD11 (prompt
tuning, AASA claim — both open, both non-blocking).
