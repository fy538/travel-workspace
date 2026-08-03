---
doc_type: working
status: active
owner: founder / eng
created: 2026-08-03
expires: 2026-09-02
why_new: Companion to pre-trip-commission-flow-2026-08-03.md, covering the
  post-trip half of the same session. Venture Path names the exit artifact as
  the E6 conversion mechanism ("not a reward"), and Product Thesis [07-29]
  says the product has "no moment where a joiner becomes an owner of
  anything." A code inventory found the artifact itself and its entire public
  share stack ALREADY BUILT — and found three specific, verifiable reasons the
  conversion still cannot happen. This doc owns those three gaps and their
  fixes. It does NOT own sequencing.
promotes_to: docs/product/ if the dogfood cohort reads S2/S3 attribution
supersedes: []
depends_on:
  - docs/working/trip-record-adjudication-2026-07-28.md   # one-artifact-per-scope; steps 1-5 shipped
  - docs/working/pre-trip-commission-flow-2026-08-03.md   # pre-trip half of this session
  - docs/product/Venture Path.md                          # E5/E6 seams; the gate metric
  - docs/product/Product Thesis.md                        # [07-29] step-5-is-the-conversion-mechanism
source_of_truth_for:
  - post-trip-exit-artifact-gaps
  - cta-ladder-by-viewer-class
  - attendance-derived-atlas-seeding
  - exit-artifact-attribution
---

# Post-trip exit artifact — the three gaps

## 0. What already ships

Verified against code 2026-08-03. The artifact and its distribution rails are
**built**; nothing here needs a new generator.

| Layer | Location | State |
|---|---|---|
| Artifact | `trip_stories` — per-member (`UNIQUE(trip_id,user_id,version)`), composed at T+24h | live |
| Sections | Credits / The Almost / Letter compose automatically per member via `_attach_extra_sections()` (AD12, commit `49f13bf1`) | live |
| Substrate | `backend/core/trip_record.py::build_trip_record()` — pure per-(trip,member) assembly | live |
| Warm landing | T+2h post-trip turn per member (`concierge/post_trip_subscribers.py`) | live |
| Share API | `backend/api/routes/story_shares.py` — create / preview / update / get / **stats** / revoke / rotate | dark |
| Public read | `GET /api/public/stories/{slug}` + share-events + viewer-context | dark |
| Link preview | `GET /stories/{slug}/card.png` — rendered 9:16 card, doubles as og:image | dark |
| Landing | SSR HTML at `/stories/{slug}`, with members-only and error paths | dark |

Dark behind `STORY_SHARING_ENABLED` (backend) + `STORY_SHARE_ENABLED` (app).
**Flipping those flags is the prerequisite for everything below** — none of
the fixes here are testable while the share stack is off.

## 1. Gap A — the CTA is intent-shaped but routes to the artifact, not to a trip

**⚠️ Corrected 2026-08-03 (same day).** An earlier revision of this doc said
the landing's only CTA was `Get the app`. That was wrong — it was read off a
partial grep that caught the secondary buttons and missed the primary one.
The actual stack, bottom of the template in `story_landing.py`:

```html
<a class="cta" href="vesper://stories/{slug}">Plan something like this</a>
<a class="cta ghost" href="{APP_STORE_URL}">Get the app — iOS</a>
<a class="cta ghost" href="{PLAY_STORE_URL}">Get the app — Android</a>
```

So a primary, filled, **intent-shaped** CTA already exists, with the store
buttons demoted to ghost secondaries (and omitted entirely when the URL is
unset — a deliberate choice, per `invite_landing.py`'s docstring, to avoid
linking a dead placeholder store page).

The real gap is narrower and still real:

1. **It routes to the artifact, not to trip creation.** `vesper://stories/{slug}`
   deep-links to *viewing this story again*. "Plan something like this" promises
   composition and delivers re-reading. Venture Path's E6 wants "start your next
   one" — trip creation, ideally seeded from this trip.
2. **For a non-installer the primary CTA is dead.** The custom scheme silently
   fails with no app installed, so the highest-intent viewer — a friend who just
   read the whole story — taps the big dark button and nothing happens, then has
   to find a ghost button. That re-imposes the E1 App Store wall at peak intent,
   which is the failure mode E1 hardening exists to remove.

Fix is unchanged in shape (a CTA ladder keyed to viewer class) but smaller in
scope than first written: **re-target the primary CTA and give it a working
web fallback**, rather than introduce one.

**Fix — a CTA ladder keyed to viewer class.** `viewer-context` already
distinguishes owner from non-owner, and `get_share_access_status` already
computes openability, so the routing data exists:

| Viewer | Ask |
|---|---|
| Owner / trip member | *"Start your next one"* — scaffold a trip pre-seeded with **this group**, since the strongest predictor of the next trip is the same people |
| Signed-in non-member | *"Start your own"* — no group seed, but their Atlas is already warm |
| Anonymous | Artifact first, then the **zero-install trip sheet** (E1 rails), not a store wall |

The anonymous row is where the E1 and E6 hardenings meet: the App Store wall
is already named as the E1 failure mode, and putting the same wall at the end
of the exit artifact re-imposes it at the exact moment intent is highest.

## 2. Gap B — the owner's own artifact has no next-trip trigger either

The in-app story screen's action set is: save, share, regenerate, edit
section, mark-wrong, remove, restore-Vesper-version, open itinerary, photo
actions. **There is no "start your next trip" affordance anywhere on it.**

So even the member who loved their story has no path from *"that was
lovely"* to *"let's do it again"* — the artifact is a terminus. E6's failure
mode ("no moment triggers organizing") is currently literal: no such moment
exists in the product.

**⚠️ Corrected 2026-08-03 (same day): NOT a fourth deterministic section.**
An earlier revision recommended appending the CTA via
`upsert_deterministic_section()`. That is wrong on three verified counts:

1. `TripStorySection` is `body: str` — no action field, so a section cannot
   carry a CTA without a contract change rippling through OpenAPI → TS → FE.
2. **Sections flow into the public projection.** `story_projection.py:265`
   passes every non-removed, non-empty section into `PublicTripStory`, so a
   CTA section would render as prose on the public landing (which has its own
   CTA) and count toward the "2 of 3 sections shown" privacy preview.
3. Sections carry provenance, `source_signals`, corrections, mark-wrong and
   `removed_by_user` — all meaningless for an invitation, and the last would
   let one stray swipe permanently destroy it.

A CTA is not a record of what happened. Credits/Almost/Letter are all *about
the trip*; this is about the future.

**Fix — screen chrome on the owner's story, outside `sections[]`.**

- **Seed it from The Almost.** `trip_story_almost.py` already assembles, from
  `change_proposals`' terminal statuses, the things this group wanted and
  didn't do — a zero-LLM backlog of trips they have already expressed
  appetite for. "Sintra never happened" is the artifact completing itself;
  "Start your next trip" is marketing. Fallback: the group ("the same five of
  you"). Second fallback: **render nothing** — the same "nothing to say"
  posture `build_credits_section` takes.
- **Separate it from the Letter.** A hairline rule and generous air, so the
  artifact visibly *ends* before the app speaks. A solid button pinned to the
  Letter turns a private letter into a landing page.
- **Use the demoted affordance.** The solid dark `.cta` is the public
  landing's conversion button aimed at strangers; the owner gets the
  ghost/gold treatment. Weaker affordance is the point.
- **Not on first view.** Show from the second visit — a user returning to
  their own story has already shown the intent the CTA is trying to create.
  View-gating is trivial in chrome and impossible in a persisted section.
- **⚠️ Privacy: name the thing, never the vote.** Almosts are sourced from
  proposals that were voted down, so someone lost. Surfacing Strategy's
  ruling stands — dimension-level consensus is fine, person-level tension is
  corrosive and `Tensions` is excluded server-side. "Sintra never happened"
  ✓ / "3 of you wanted Sintra" ✗. Encode this on the builder, not as a copy
  guideline.
- **Reuse:** `planSimilarSeed.ts` + `createTripFromPublicStoryShare` already
  build a seeded ConversationSeed and create the trip. The owner variant is
  *simpler* than the shipped public one — full access means real destination,
  real dates and the actual member list, with no generalization step.

Placement study (4 states incl. the funnel anti-pattern):
`scratchpad/next-trip-invitation.html`, 2026-08-03.

## 3. Gap C — the passive joiner's taste model never gets seeded (the deep one)

> **⚠️ Reframed 2026-08-03**, after the founder noted that **Atlas is retired
> as a core IA surface** — bottom tab retired, surviving as private memory
> inside **You** (`docs/working/global-navigation-ia-proposal-2026-07-25.md`).
> The tab still exists in code, so the decision is ahead of the
> implementation.
>
> This section originally argued "the joiner ends with an empty Atlas." Wrong
> emphasis. `traveler_place_affinity` was never Atlas-owned — its readers are
> `concierge/turn_loader.py:252` (the loved-places block on **every concierge
> turn**), `tool_handlers/planning/_plan.py:273`, and `memory_tools.py`. Atlas
> was one consumer, and now the retired one.
>
> The claim that survives is stronger: **Vesper never learns how this person
> travels**, degrading personalization on every future trip — which is the
> relational-personalization moat claim itself, not a surface.
>
> **Retirement makes this worse, not moot.** With no Atlas destination,
> affinity has no user-visible surface at all, so nothing will ever reveal the
> gap to anyone. It fails silently and invisibly.
>
> The *ownership* half of E5 doesn't need Atlas: what the joiner owns is the
> **Trip Story** — per-member, theirs, outward-shareable. ⚠️ Venture Path's E5
> hardening still reads "exit artifact + **Atlas seeded from the shared
> trip**"; that clause is now stale and should be revisited on the next
> strategy edit.

Product Thesis [07-29]: *"Today the product has no moment where a joiner
becomes an owner of anything; that is the loop's missing link."* This is
where that becomes concrete.

Atlas is composed over `traveler_place_affinity`. The trip-side write path is
`record_place_affinity()` called from `commit_trip_venue()`
(`core/db/trip_commitments.py:74`) — **scoped to the committing user**:

```python
record_place_affinity(
    user_id=user_id,          # the actor who tapped commit
    signal_weight=_COMMIT_AFFINITY_WEIGHT,
    signal_source=source or "pick_commit",
)
```

**Amended 2026-08-03 — all three write paths traced, not just this one.**
There are exactly three callers of `record_place_affinity()`:
`save_application.py:99` (a save), `itinerary_operation_commands.py:190` via
`_record_planned_venue_affinity` (a plan-add, `_PLAN_AFFINITY_WEIGHT = 1.5`),
and `trip_commitments.py:74` (a commit). **All three are actor-scoped** — the
saver, the acting principal, the committer.

So the precise claim is: a **fully passive** joiner finishes with an empty
Atlas; a joiner who saved a place or two finishes with a *thin* one. Either
way the plan-add path accrues to whoever does the planning — the organizer —
so the asymmetry the loop depends on runs the wrong way: the person who
already has an Atlas earns more of one, and the person who needs seeding gets
nothing. Nothing errors; the absence is silent.

That is the worst possible targeting: the passive joiner is exactly the
person E2 and E6 are about, and the "Atlas seeded from the shared trip" claim
in Venture Path's E5 hardening is **not true for them today**.

**Fix — attendance-derived affinity at trip completion.**

- On `trip.completed`, for **every member**, write an affinity row for every
  venue the trip actually *happened* at (the confirmed/happened blocks that
  `build_trip_record()` already assembles).
- The adjudication's MVP ruling already settles the hard question here:
  **attendance = membership**. No per-member attendance data is needed.
- Use a distinct `signal_source="trip_attendance"` and a weight materially
  **below** `_COMMIT_AFFINITY_WEIGHT`.

The weight and source separation are load-bearing, not hygiene. A commit
means *"I chose this"*; attendance means *"I was there."* Collapsing them
pollutes the taste model that the entire moat claim rests on — and Atlas's
`significance` blend can discount an attendance-sourced row explicitly if
`signal_source` is preserved. Getting this wrong makes every joiner's taste
profile a copy of the organizer's.

**What this buys:** every member leaves every trip with a non-empty Atlas,
honestly grounded, without claiming a preference they never expressed. That
is the "becomes an owner of something" moment, and it costs one subscriber on
an event that already fires.

## 4. Attribution — otherwise you ship the mechanism and can't read the gate

`scripts/invite_loop_funnel.py` computes S1 joined → S2 created-own-trip → S3
invited-others from `trip_events`, and reads zero because no cohort has run.
The share stack already has a `share-events` endpoint and a `stats` route.

**Wire share → view → signup → first-trip as an attributed chain**, so S2/S3
can be split by whether the exit artifact touched that user. Without it, a
cohort that converts tells you *that* it converted, not that the artifact
caused it — and the artifact's entire justification is causal.

This is cheap now and unrecoverable later: the events are only capturable at
the moment they happen.

## 5. Scope compliance

No new artifact object. Every fix above is a **section, a CTA, a subscriber,
or an event** on existing objects.

**⚠️ Updated 2026-08-03: the one-artifact-per-scope table has collapsed to one
row.** The 07-28 ruling read trip → Trip Story, year → Unpacked, moment →
Atlas artifact. With **Atlas retired as a core IA surface and Unpacked retired
outright**, the year and moment scopes are vacant and **trip → Trip Story is
the only live artifact scope**.

Three consequences that matter here:

1. **The Trip Story is now the product's only exit artifact**, so everything
   in this doc gets more load-bearing, not less. There is no second artifact
   to carry E5.
2. **The story share is now the only public share path.** The `/unpacked/*`
   HMAC-signed public share retires with Unpacked, leaving `/stories/*` (the
   AASA-claimed one) as the sole route by which a non-user ever sees anything
   from Vesper. That makes Gap A — the landing and its CTA — the single
   highest-traffic external surface in the product.
3. **The ruling no longer constrains a Commission** (pre-trip half): with the
   scope table down to one row, a per-member commissioned piece competes with
   nothing.

Note the symmetry with the pre-trip half: in both, the generation is done and
the **loop** is the missing part. Neither half needs a new generator, and
neither needs the "Artifacts page" the session originally proposed.

## 5b. The share card is off-canon — and its reference implementation is
being retired (added 2026-08-03)

Found by rendering the landing and reading the card compositor. The two
halves of one share moment are in **different design systems**:

| | Landing (`story_landing.py`) | Story card (`core/story_card.py`) |
|---|---|---|
| Background | `#efeae0` paper | `#ffffff` white |
| Ink | `#1b1714` warm | `#1a1a1a` neutral |
| Accent | `#8a6628` gold | **`#4338ca` indigo** |
| Type | EB Garamond + JetBrains Mono | `load_system_font` (host-dependent) |

The card is the unfurl in the group chat; the landing is what you get when
you tap it. Today they look like two different products, and the card's own
comment calls itself *"the generic story-card brand."* The system-font path
also means the most-shared image in the product renders **differently
depending on host fonts**.

The paper values are the **product canon, not "the Atlas palette"** — they
are byte-identical to the landing page's CSS variables, and the landing has
nothing to do with Atlas.

**⚠️ Time-sensitive.** The only image-layer implementation of that canon
(`_PAPER`, `_ATLAS_INK`, `_ATLAS_GOLD`, `_ATLAS_FONT_FILES` + the bundled
EB Garamond / JetBrains Mono TTFs) lives *inside the Unpacked card face* in
`story_card.py` — and `card_kit.py`, the shared kit, owns only the canvas
size, font loaders and drawing primitives, **not** the palette or the font
filenames. If the Unpacked face is deleted with the retirement, the canon
implementation goes with it and whoever ports the story card later
re-derives the palette by hand.

**Do this before deleting Unpacked's card face:** lift the paper palette and
the bundled-font map out of the Unpacked section and into `card_kit.py`,
then point the story card at them. That converts a port-from-a-corpse into a
port-from-the-shared-kit, and it is the cheapest moment to do it.

Minor: the landing's `.chip` is 14px and inherits the serif body font —
below the 15px serif floor the ratchet enforces elsewhere.

## 6. Falsifier

The gate metric is already defined (re-invite, S2/S3). For this work
specifically:

- **If flipping the share flags produces ~zero shares**, the exit artifact is
  not outward-shareable in practice and Gaps A/B are moot — fix desirability
  before conversion.
- **If shares happen but attributed S2 stays flat**, the artifact is a nice
  souvenir and *not* the conversion mechanism Venture Path claims. That
  finding would be worth more than the feature: it falsifies a load-bearing
  strategy claim cheaply.

## 7. Build order

0. Flip `STORY_SHARING_ENABLED` + `STORY_SHARE_ENABLED` (nothing else is
   testable first).
1. Attribution events (Gap C's and A's value is unreadable without them, and
   they are unrecoverable retroactively).
2. Attendance-derived affinity on `trip.completed` (Gap C) — the ownership
   half, and the one that silently fails today.
3. Next-trip deterministic section (Gap B).
4. CTA ladder on the landing (Gap A), anonymous row gated on whether the
   zero-install trip sheet exists.

## 8. Open

- Exact attendance affinity weight relative to `_COMMIT_AFFINITY_WEIGHT`, and
  whether `significance` should discount `trip_attendance` explicitly or rely
  on weight alone.
- Whether the next-trip CTA seeds the same group by default (strongest
  signal) or asks — pre-seeding a group is a social act with its own risk.
- Whether the anonymous CTA waits on the E1 zero-install trip sheet or ships
  an interim path.
- `AD7` (light postcard) and `AD8` (light sharing) remain open from the
  adjudication; the postcard render is ~373 LOC of tested code two config
  values from live and would give the share card a second visual form.
- **Unpacked retirement cleanup**: whether the `/unpacked/*` share routes,
  `atlas_unpacked_landing.py`, and the Unpacked card face are deleted or left
  dormant, and — if deleted — that the paper palette / bundled-font map are
  lifted into `card_kit.py` **first** (§5b).
