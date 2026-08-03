---
doc_type: working
status: active
owner: founder / eng
created: 2026-08-03
expires: 2026-09-02
why_new: A 2026-08-03 brainstorm ("I created a trip, got an itinerary — what
  now?") started as a proposal for a new Artifacts page and a new pre-trip
  generation pipeline. A code inventory found that the pre-trip generated
  Reading ALREADY SHIPS end-to-end (`backend/home/trip_reading/*`, persisted,
  routed, surfaced on Trips Home). This doc records that correction, the two
  genuinely-missing deltas (pull instead of push; per-member instead of
  trip-scoped), and the one real engineering problem underneath them — the
  place-fact grounding extension. It does NOT own build sequencing; that
  defers to the dogfood gate and Venture Path process rule 3.
promotes_to: docs/product/ only if the dogfood cohort shows commission uptake
supersedes: []
depends_on:
  - docs/product/Surfacing Strategy.md      # §2 rejection of visible-intelligence surfaces
  - docs/product/Venture Path.md            # E2/E5 seams; process rule 3
  - docs/product/Product Thesis.md          # [07-29] wedge amendments
  - docs/working/trip-record-adjudication-2026-07-28.md  # one-artifact-per-scope ruling
source_of_truth_for:
  - pre-trip-commission-flow
  - trip-reading-shipped-state-inventory
  - place-fact-grounding-extension
  - personal-memory-steers-selection-invariant
---

# Pre-trip commission flow

## 0. The correction that reframes everything

The session opened intending to design "after the itinerary commits, Vesper
generates something to read, and it appears as a section on Trips Home."

**That ships today.** `backend/home/trip_reading/` is a complete, persisted,
surfaced system:

| Layer | Location | State |
|---|---|---|
| Trigger | `trip_reading/subscriber.py` — `itinerary.committed` schedules generate **now** + a second run at **T-7** | live |
| Compose | `trip_reading/composer.py` (527 LOC) — 3–5 sections, title, thread, `read_minutes` | live |
| Grounding | `trip_reading/grounding.py` — deterministic quantity/date gates + an independent low-temperature semantic entailment verifier, **fail-closed** | live |
| Persist | `trip_readings` table; upsert-on-conflict; `source_hash` | live |
| Serve | `load_current_trip_reading` — recomputes the fact bundle at read time and **suppresses sections whose cited facts went stale** | live |
| Route | `GET /api/.../reading` → `TripReadingPublic` (`backend/api/routes/home.py:51`) | live |
| FE | `app/(tabs)/trips/[tripId]/reading.tsx`; `companionTripId` slot on Trips Home with section-index deep-linking | live |

Two adjacent claims in `docs/product/Surfacing Strategy.md` were also found
stale and have been corrected in that doc (see §7 below).

## 1. What is actually missing

Three deltas separate shipped behavior from the brainstormed feature. Only
the third is hard.

1. **Push, not pull.** The Reading appears unbidden. Nobody commissions
   anything, so nobody has expressed what they want.
2. **Trip-scoped, not per-member.** One Reading per trip; all four members
   read identical text. The private per-member channel that
   `_produce_pre_trip_drip` already uses sits unused here.
3. **Plan-grounded, not place-grounded.** `TripReadingFactKind =
   Literal["trip", "itinerary", "decision"]`. The composer may cite only the
   trip's own world model. It has no access to the place graph.

Delta 3 is not an oversight. `facts.py`'s module docstring and
`grounding.py`'s `_GROUNDING_SYSTEM` both enforce it deliberately: the
verifier is instructed to FAIL any draft that "invents city, neighborhood,
venue, history, atmosphere, or transport facts."

**Consequence:** today's Reading can say *"you have three fado nights and an
open Thursday."* It cannot say *"here is why fado sounds the way it does."*
Every commission example from the brainstorm was in the second category.

## 2. The design

### 2.1 Two grounding regimes, one composer

```
itinerary.committed
   ├─→ [exists] trip_reading   — trip facts,  group-safe, push, trip-scoped
   └─→ [new]    commission     — trip + place facts, private, pull, per-member
```

The commission reuses the composer, the grounding ladder, the stale-fact
suppression, and `read_minutes`. What changes is the **fact bundle** and the
**visibility rules** around it.

### 2.2 The place-fact extension

Add a fourth kind:

```python
TripReadingFactKind = Literal["trip", "itinerary", "decision", "place"]
```

A `place` fact's `text` is a **verbatim claim lifted from already-vetted
content** — a GREEN-gated dossier passage, a venue brief, an angle body —
carried with its provenance. It is not model-generated at bundle time.

This works with the existing verifier almost unchanged, because the verifier
tests *entailment against the cited bundle*, not world knowledge. One prompt
edit is required: the "invents city, neighborhood, venue, history,
atmosphere, or transport facts" clause must become conditional — invention
remains a failure, citation of a place fact **present in the bundle** does
not. Left as-is, the clause and the new bundle contradict each other and the
verifier will fail-closed on every commissioned piece.

The deterministic quantity/date gates need no change: they compare a claim's
tokens against its own citations' text, and place facts carry their numbers
with them.

**Where the safety burden moves.** Today the risk is "did the model
hallucinate about the plan," answered by the verifier. With place facts the
risk becomes "is the dossier true," answered by the research pipeline's
existing GREEN/YELLOW/RED quality gate and source-credibility scoring. That
is a defensible relocation, but it must be explicit: **admit only
GREEN-gated material into the bundle.** No live web search, no
model-recalled place knowledge.

**Free side effect.** Because place facts carry provenance, a commissioned
piece can link back to the dossier it drew on — a "keep reading" path from a
personal artifact into Discover, which is currently a funnel with no
personalized entry point.

### 2.3 The privacy invariant that makes sharing safe

The Reading is trip-scoped and group-safe; `facts.py` deliberately excludes
member briefs, group-profile prose, planning rationale, and
`UserTripContext` identity fields. A commission is private, so it *could*
draw on Personal Memory — and that is exactly where a leak would occur if a
member later shares the piece into the trip.

**Invariant: Personal Memory steers selection; it never enters the text.**

- Personal Memory may decide *which* angle to offer and *which* place facts
  to pull. It is never admitted to the fact bundle, so it is never citable,
  so it cannot appear in the body.
- A shared piece is therefore indistinguishable from one any member could
  have commissioned.

This makes share-safety a structural property of the bundle rather than a
policy the composer has to be trusted to follow — consistent with how
`facts.py` already handles the group-safety boundary.

### 2.4 Flow

1. **Offer.** After the Reading composes, Vesper offers 2–3 *specific*
   commissions in each member's 1:1 trip conversation, built from Personal
   Memory × committed itinerary × available angles for the destination.
   Concrete ("you're staying between Alfama and Mouraria"), never a blank
   prompt — blank prompts do not get answered in a low-frequency product.
   Reuses the drip's private routing and the arbiter's gating/capping.
2. **Commission.** Tap an offer, or ask freeform. Record
   `origin: offered | requested`.
3. **Compose.** Same composer; bundle = trip facts + GREEN place facts.
   Async; the piece lands when ready.
4. **Surface.** No new home slot. The existing Reading screen gains a
   "yours" shelf beneath the trip Reading; a ready commission emits a
   `ConciergeHomeCard` and the existing `concierge_feed` ranker decides
   whether it earns a Trips Home slot (`trips_stack.py` projects cards —
   adopt, do not build).
5. **Share (optional, user-initiated).** Posts the piece only, never the
   reason — guaranteed by §2.3 rather than by prompt discipline.

### 2.5 Drip displacement (ruled)

`_produce_pre_trip_drip` returns `[]` for any member holding a commission in
`queued | generating | ready` state within the current drip window. One
content stream per person per window. The drip remains the fallback for
members who never commission anything.

## 3. Data model

```
Commission {
  id
  trip_id
  owner_user_id                    # per-member; private by default
  origin: offered | requested      # the experiment
  request_text                     # their words, when requested
  status: queued|generating|ready|failed
  payload                          # reuses the TripReading shape
  source_refs[]                    # itinerary blocks + dossier/angle provenance
  shared_to_trip: bool
}
```

Deliberate calls:

- **Render is not a kind.** Audio would be TTS over the same text via the
  path already backing `narration_audio_cache`. One generation, two renders.
  Modelling audio as a separate type builds the pipeline twice. **v1 is
  read-only** (ruled 2026-08-03).
- **`origin` is the metric.** Offered-tap rate vs. requested rate answers
  whether users want curation or authorship, and that answer determines
  whether the surface ever deserves to grow.
- **Scope compliance.** The one-artifact-per-scope ruling
  (`trip-record-adjudication-2026-07-28.md`) assigned trip→Trip Story,
  year→Unpacked, moment→Atlas artifact. **⚠️ Updated 2026-08-03: Atlas is
  retired as a core IA surface and Unpacked is retired outright, so the year
  and moment scopes are vacant and trip→Trip Story is the only live artifact
  scope.** A Commission still claims a scope nothing else covers — **(person ×
  trip × occasion)** — and now competes with nothing at all. It remains not a
  trip record and must not accrete trip-record responsibilities; the ruling's
  *principle* (one artifact per scope, everything else is a section or a
  render) survives its table.

## 4. Why this is not the surface Surfacing Strategy killed

`Surfacing Strategy.md` §2 rejects visible-intelligence surfaces, daily
digests, and living profiles, on evidence that explainability raises
self-reported trust without improving outcomes. A shelf of AI-generated
content is one design decision away from being exactly that.

Three properties keep the commission on the right side of that line:

1. **User-pulled, not manufactured presence.** The user names what they
   want; nothing new interrupts them (and per §2.5, the existing
   interruption is reduced).
2. **It displaces rather than adds.** Net notification volume goes down for
   commissioning members.
3. **Its success metric is outward share, not open rate.** Consumption is
   not a loop. Share → group visibility → the E2 seam is the loop.

## 5. Where it sits in the venture chain

`Venture Path.md`'s critical-event chain names two seams this touches:

- **E2** — "joiner spectates, never converts" → hardening is "give a job
  with a visible group effect." A shared commission is a contribution the
  quiet member can make without proposing anything socially risky, which
  suits precisely the personality the privacy invariant exists to protect.
- **E5/E6** — the post-trip half (out of scope here) is where the declared
  conversion mechanism lives.

Note **process rule 3**: strategy is closed until the gate reads. This work
is admissible only as E2 hardening — a declared link in the chain — not as a
new feature area. Framed as "add an artifacts feature," it should be parked.

## 6. Falsifier (pre-committed)

The shipped Reading is the control: it already exists and nobody asked for
it.

- **If fewer than ~1 in 3 members tap an offered commission**, this is a
  content shelf. Kill it; do not iterate on copy.
- **If commissioned pieces are not read more than the auto-composed
  Reading**, the commission mechanic adds nothing — invest in the Reading
  instead.
- **If shares are ~zero**, the E2 justification fails and the feature loses
  its claim on being wedge work.

## 7. Doc corrections made 2026-08-03

`docs/product/Surfacing Strategy.md`, build-queue item 4, claimed the
pre-trip prep feed was "backend filter + FE component DONE, not wired."
Verified against code:

- `PreTripPrepFeed.tsx` **does not exist** — deleted in the era-1/era-2
  cleanups; only its orphaned test was catalogued in
  `docs/archive/2026-07/adjudicated/dead-code-inventory-2026-07-02.md:136`.
- The reference-id tagging defect described there is **already fixed**:
  `_drip_reply_marker` (`proactive.py:1830`) writes the reply prose itself
  as the marker body, with a silent dedup-only marker when the turn produced
  no reply.
- The doc does not mention `trip_reading` at all, despite it being the
  shipped implementation of that queue item's intent.

Item 4 has been rewritten accordingly.

## 8. Open

- Which GREEN-gated content types are admissible as `place` facts —
  dossiers only, or briefs and angle bodies too?
- Cost/latency budget per commission, and whether it shares the research
  pipeline's queue or gets its own.
- Whether the "yours" shelf eventually justifies a standalone page. Current
  read: **no** — 1–3 items per trip is a section, not a library; the page
  earns existence at trip #2 on cross-trip accumulation.
- Naming. "Artifact" is already triple-booked:
  `backend/core/derived_artifacts.py` (a Qdrant lifecycle registry), the
  trip-artifacts vision doc, and Atlas artifacts.
