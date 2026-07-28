---
doc_type: working
status: active
owner: founder / product / frontend
created: 2026-07-28
expires: 2026-08-27
why_new: No document owns the Vesper Home redesign decided across the 2026-07-27/28 sessions — the surface stops being a second decision queue and becomes the place where work with the agent lives. The shipped vesper-home surface contract describes the rail-and-Deck composition this supersedes; the trips-home stack model is its counterpart on the other home.
promotes_to: travel-app/docs/surfaces/vesper-home/contract.md (supersession) plus a navigation/ownership decision record
supersedes: []
source_of_truth_for:
  - vesper-home-workbench-model
  - vesper-home-ownership-rule
  - vesper-composer-gesture-model
  - vesper-voice-two-paths
---

# Vesper Home — The Workbench

> **Working spec, not shipped canon.** Records the design decided in the
> 2026-07-27/28 sessions and the code investigation run on 2026-07-28.
> Design of record: **Claude Design → Vesper → "Vesper Home - Workbench.html"**
> (+ `vesper-workbench.jsx`, `-voice.jsx`, `-keyboard.jsx`). Bundle snapshot:
> `~/Downloads/vesper 400`, exported 2026-07-28 01:37.
>
> Every claim marked **VERIFIED** was read out of the running code on
> 2026-07-28. Everything else is proposal.

## One sentence

**Trips owns objects; Vesper owns sessions** — so Vesper Home stops being a
second decision surface and becomes one situated read, one panel of work
with the agent, and a composer.

## Why this exists

Vesper Home currently carries a decision rail: votes, proposal approvals,
readiness checks, settlement actions, all reachable through a full-screen
Deck. The trips-home stack model
(`trips-home-promotion-model-2026-07-27.md`) makes Trips Home *"one ranked
queue of everything that wants the traveler, across all their trips."*
Those are the same material. Two surfaces cannot both own it.

The ownership line that resolves it:

```
Trips owns OBJECTS    — trips, drafts, seeds, and the decisions on them
Vesper owns SESSIONS  — the process of working with the agent
```

Vesper may *mention* something urgent and open a door into the trip. It
may not host the resolution. The moment it does, the two homes compete
again.

## The page

```
ON the paper    the read line · the ghost · the composer
                (voice, potential, input — EXPRESSIVE)

IN the paper    one well: context facts · the urgent seam · the threads
                (instrument — PRODUCTIVE)
```

**Depth is the register border.** The register model requires hybrid
surfaces to have expressive and productive regions that "never silently
blend"; a recess is the least verbal way to draw that line — no rules, no
labels, no second typeface. Nothing on this page is raised, which is a
deliberate fork from Trips: **Trips raises its material** (crowned cards on
the page), **Vesper sinks its own**. Same tokens, opposite direction — a
named fork in the sense the Places register bridge uses, not drift.

Well material: `paper30` (surfaceSunken), radius 16,
`inset 0 1px 3px rgba(27,23,20,0.075)`. Fixed, **not** tinted by place —
tinting is prettier and puts a colour off the token ladder, which is the
exact drift the Places session caught and fixed this week.

## The rules that survived

Each removes a decision that would otherwise be made case by case.

| Rule | What it settles |
|---|---|
| **No italic** — *amended, see erratum* | As written 2026-07-28 AM: Roman-only, verified (no face bundled, 0 `fontStyle:'italic'` hits, `fonts.ts:18-21` forbids synthesized slant). **Superseded same day by Trips D4 (founder): italic APPROVED as a limited register** — face + one named role registered together, **never below 17px**, ratchet extended. Landed in app `aee56838`; History rows and the transcript remain sans. The read line's gold-weight emphasis may now adopt the named role for cross-home rhyme. |
| **No coloured left accent borders** | Project CLAUDE.md. A card is distinguished by material, never by an edge. |
| **Grounded or absent** | A fact with no data renders nothing — no placeholder, no chrome over emptiness. |
| **Potential, not buttons** | Capability renders as unwritten (ghost) text, never as a control. A pill is a button; a button promises a destination. |
| **Say it once** | No fact appears twice — not as material and again as text, and **not in two channels at once**. This rule independently caught three defects during design: the nearest-save tile restating the read line, the plate restating the trip kicker, and a receipt nested inside a seam already built from receipt material. |
| **A door, never a decision** | Urgency is mentioned here and resolved in Trips. |
| **Emptiness has no chrome** | Inherited from the stack model. No headers over nothing, no placeholder cells. |
| **Occlude, never reorganise** | Nothing collapses or folds to make room. The composer floats, content dissolves beneath it, and the keyboard raises the floor. |
| **Colour and family are the speaker** | Ink meter = you, gold meter = Vesper. Both still = neither, which is how *working* and *paused* read without a spinner. |

## Four states

The grammar never changes; what changes is how much of it exists.

| State | Read line | Well | Ghost |
|---|---|---|---|
| **live** | situated, from `situation/nearby.py` | facts + **seam** + threads | 3 lines |
| **home** | situated | facts + threads | 3 lines |
| **quiet** — trips exist, nothing open | floor-tier recall | **does not render** | 5 lines |
| **cold** — nothing at all | an invitation | **does not render** | 5 lines |

The quiet/cold rule is the load-bearing one: **a well containing only the
weather is a weather widget**, and this is not a weather app. With no
threads the panel is absent, context collapses to one mono line, and the
space goes to the ghost — the page reallocates room to *potential* when
there is no *actuality*. The read line grows 22 → 25.

**Open risk, stated plainly:** the cold state is one sentence, five faded
lines and a composer. Whether that reads as confident or as unfinished is
not a question a mock can answer.

## The row

The atom both this surface and History share. Four things legible at a
glance: **where** it belongs, **who** is in it, **what** it is, **what
state** it is in.

```
line 1   mono kicker  · · · · · · · · · · ·  mono stamp     (both provenance)
line 2   TITLE, full width, up to two lines
line 3   state sentence  · · · · · · · · · ·  facepile
```

**Scope is the kicker and only the kicker.** An earlier draft encoded it
twice — a paper plate *and* a mono trip kicker saying the same thing. At
list scale that reads as two components, not as meaning. Withdrawn.

**The reflow was forced by a render, not by taste.** The first draft put
the facepile, a state word and a chevron in a right-hand rail, and the
title took whatever width was left — truncating at about twenty-four
characters. The title is the most useful thing in the row and was the
first thing sacrificed.

### Reconciliation with Trips Home — Row Studies

`trips-home-row-studies.jsx` (bundle `vesper 400`) explores six treatments
of the Trips queue row. The shared spine to hold:

| Element | Trips rows | This row | Status |
|---|---|---|---|
| mono kicker | 7.5–9px, ls 1.1–1.5, weight 700 | 8px, ls 1.5 | **aligned** |
| facepile | 18–20px, overlap −7/−8 | 19px, overlap −6 | **align to −8** |
| fact/title | sans 14–14.5, single-line clip | sans 15/500, 2-line clamp | **deliberate fork** — see below |
| chevron | soft `Chev`, 10–11px, rgba(27,23,20,0.28) | none | **unresolved — adopt theirs** |
| height | fixed 54–64 | variable | fork, follows from line count |

**The fork is justified by content, not taste.** A Trips queue row carries
*one fact* and is a cursor into a trip. A Vesper row carries a *name* (the
Haiku-generated conversation title) **and** a *state*. Two lines versus
three follows from that. The kicker, the pile and the chevron should not
fork, because those are the shared spine.

**Recommendation: adopt the Trips soft `Chev`.** Dropping it was a taste
call and it costs a rhyme between the two homes for no gain.

Worth noting: Row Studies variant **F** renders each row as an inset plate
on `T.bg` inside a raised card — the Trips session independently reached
for recess as a row treatment. Corroboration for the well.

## The urgent seam

When a live trip has something time-critical, it enters the well **between
the facts and the threads** — under one hard constraint:

> **A mention with a door, never a place to act.**
> ALLOWED: state the fact · name the clock · open the trip.
> FORBIDDEN: the vote · the approve · the settle-up · the rebook.

Urgency is tier 0 on Trips Home — the only tier that pushes and the only
one that can usurp the crown intraday. The moment this band grows a button
that resolves something, Vesper has taken the queue back.

Two severities, using status hues already on the ladder — a **deadline** is
gold (nothing is wrong yet, there is only a clock); a **breakage** is
`ox60`, defined on the primitive ladder as exactly *broken / urgent*.

**Typed proof, one per severity, not one ornament reused.** A deadline gets
the window (a hold order has a real start and expiry, so a depletion bar
states a fact). A breakage gets one mono line — it is binary, and the
struck fact says everything. *Typed proof means the proof is typed, not
that every severity gets a picture.*

The seam is built from `SK.goldTint` / `SK.goldLine` — the stack model's
own receipt material. **Do not nest a receipt panel inside it**; it already
is one.

**Consistency requirement found while drawing this:** if tonight's table is
cancelled, the facts row above must not still assert the booking. The fact
goes struck and marked cancelled; the seam carries what changed.

## The composer

**VERIFIED** against `components/chat/ComposerBar.tsx`, inline (home)
variant. Four things every earlier mock had wrong.

| Property | Value | Source |
|---|---|---|
| container | radius.full · `cardWarm` #FBF7EC · hairline border | `:828-837` |
| padding | left 14 (`spacing.lgl`) · right 4 (`spacing.xs`) · vertical 0 | `:833-835` |
| shadow | `0 8px 22px -14px rgba(0,0,0,0.18)` | `:836` |
| field | `chatComposerInput` — sans **17**, letterSpacing 0 | `constants/typography.ts:419` |
| placeholder | `colors.surface.mute` **#6E6862** | `:648` |
| trailing | 36×36 circle, radius.full, **ink fill**, mic when empty | `:971-990` |
| send | ink-blue; stop is ink — a deliberate distinction | `:988-994` |

**The leading slot is a `+`, not the sparkle.** Shipped code renders
`VSparkle` on home (`showInlineSparkle = inlineMode`) and a `+` attach only
in chat (`showInlineAttach = floatingThreadMode && visionEnabled`). One
position, two meanings across two surfaces — and on home it is a 17pt gold
target with **no press handler**. The mark is retired from the composer,
which also makes the placeholder honest: "paste, or drop anything" now has
a control behind it.

**The dissolve.** The composer floats over the scroll, so content fades
into it — ~64px, always, not only when a keyboard is up. This replaces an
earlier design in which the well collapsed to its first row: that turned
the appearance of a keyboard into a layout event, needed two animations to
agree in a runtime where keyboard timing is hard to sync, and said
*removed* when the truth is *occluded*. The ghost needed no rule as a
result — it sits inside the dissolve zone and simply goes.

## Voice — two paths

**TAP dictates. HOLD converses.** One control; the gesture chooses, and the
assignment tracks frequency: dictating is common so it costs a tap;
conversing is rare and deliberate so it costs a hold.

**The hold covers your first turn.** Release ends that utterance and sends
it — exactly as WhatsApp and every walkie-talkie taught — and what you land
in is a full screen you can see. The gesture spans one turn; the mode
carries the rest.

Required for safety, all three:

- **A previewed threshold.** The circle grows from 150ms; haptic at ~450ms.
  Releasing early is just a tap and you land in dictation having lost
  nothing.
- **Slide to cancel**, abandoning the turn without sending.
- **An accessible alternative.** Long-press is hard with motor impairment
  and invisible to screen readers. VoiceOver action plus a setting that
  turns voice into a plain second button. The gesture is the default, never
  the only way in. **House precedent exists**: `PeoplePills.tsx:37-69` uses
  `delayLongPress={450}` with a visible hint and `accessibilityActions`.

### What the screen shows while audio talks

A **two-sided transcript at reading scale** — a *record*, not a delivery.
Where a phrase names something the system already holds, it carries a
hairline mark and the turn carries one mono provenance line
("you starred it in march · 240 m") — evidence attached to the sentence,
not extracted into a card beside it.

An earlier draft replaced the reply with extracted "talked about" object
cards. Withdrawn: they need an entity-extraction step nobody costed, most
turns contain no objects at all, and a transcript is the honest artifact
where cards are a derived summary. **The transcript is also an
accessibility requirement** — someone hard of hearing can use voice mode
only if the words are on screen.

**Scroll and tap want different things.** Scroll = "let me read while you
carry on" — detaches from the live tail, playback continues, fade flips to
the bottom, a Live pill appears. Tap = "hold on" — it stops, the floor is
yours, and the left control flips from *Hold on* to *Resume*, so
tap-anywhere is only a shortcut to the button already there.

### ⚠ Typography conflict — resolved against this design

`chat-typography-plan-2026-07-28.md` records a founder-settled rule:

> **Body** — System Sans 16/26, every speaker, both rooms. Identity comes
> from two registers, never from type.

The design board renders Vesper's turns in serif and yours in sans, which
is identity-from-type. **The chat rule wins.** A voice transcript *is* a
chat transcript — the session becomes an ordinary thread in history, so if
it renders one way while spoken and another when reopened, the same object
has two typographies.

Consequences:

1. Both sides become **sans 16/26**; Vesper's turns carry the
   **signature** (Guiding Star + "Vesper" in EB Garamond **Roman** 15px +
   mono stamp) via a new `scale='signature'` role.
2. **"Record versus delivery" dies.** The no-headphones case does *not*
   step the reply up to 25pt serif — it is a transcript turn rendered like
   a transcript turn, in a conversation where nothing is spoken. One fewer
   special case.
3. The meter rule is untouched — ink/gold is not type, so it carries the
   live-speaker signal the family was carrying.

**V1 excludes group threads.** There, "talking to Vesper" and "talking to
the group" are one channel, so something said aloud in confidence could
land in front of four people — which collides with the privacy invariant
regardless of which gesture opened the mic.

**Owed before voice ships:** `situation/voice_memory.py` writes
observations to Personal Memory from spoken moments. A voice session
changes what Vesper knows, and nothing in this design shows it happening or
lets the traveller take it back.

## What the wire can carry — VERIFIED 2026-07-28

### Free today (on the wire, never rendered)

`conversation_type` · `trip_id` (nullable — the kicker, and the **only**
scope signal) · `title` (Haiku-generated after turn 1) ·
`last_message_preview` / `_sender` / `_at` · `unread_count` — which today
reaches the accessibility label **only**: no dot, no weight, nothing
visual.

### The serializer cut — cheaper than claimed

`get_conversation_list_for_user` delegates to a `select(conversations)` —
the **whole table** — so `intent_state` (JSONB, same row, `NOT NULL DEFAULT
'{}'`), `session_status` and `last_active_at` are **already read off disk
and already hydrated**. No query change, no migration, no plan change.

Both enums are already CHECK-constrained in Postgres — `session_status IN
('active','idle','closed')` and `intent_state->>'phase'` pinned to the five
values — so they can be typed as literals with the database guaranteeing
it.

**≈3 hours.** Project the scalars; do not dump raw `intent_state` (it nests
`planning_direction` and would bloat 50 rows for no benefit).

### The busy flag — a different category. Defer.

There is **no index on `agent_workflows.conversation_id`** (Postgres does
not auto-index FKs; the four existing indexes don't lead with it). The
discoverable-status version sequential-scans on every history open — the
most-hit surface in the product. Fixing it means a partial index, an
Alembic revision, and two migration tests.

And the part that is not SQL: **a busy flag in a list is stale the moment
it is serialized.** The list is fetched through react-query with no
invalidation tied to workflow lifecycle. A row saying "working…" about
something that finished forty seconds ago is worse than no row.

**Stopgap:** `session_status` plus `phase == 'drafting'` gives most of the
"something is happening here" signal for zero cost.

### Grounded, best-effort

- **weather** — `digest/engine/weather.py`, open-meteo; returns `None` →
  the fact is absent, never invented. Client side already exists:
  `useAmbientWeather` (228 LOC) and the feed endpoint already accepts
  lat/lng/condition/temp/precip/wind.
- **the read line's nearby fact, and the transcript's marked phrases** —
  `situation/nearby.py`: the user's **own saves ≤250m**, next plan block
  ≤275m, fresh location only. The transcript marks only what this already
  knows, so it needs no new source and no extraction step.
- **the seam** — hold expiry (Duffel hold-order) · venue disruption.

## The ledger

### Frontend — exclusive to Vesper Home

| Path | LOC |
|---|---|
| `app/(tabs)/concierge/index.tsx` | 814 |
| `components/decision-deck/` (16 files) | 4,486 |
| `components/vesper-cards/` | 110 |
| `hooks/useConciergeHomeState.ts` | 1,100 |
| 12 further exclusive hooks | ~1,100 |
| `utils/conciergeHome*` (4 files) | ~810 |
| `data/conciergeHome.ts` | 298 |
| dev routes | 161 |
| **Production subtotal** | **~9,093** |
| Tests | ~5,151 |

`index.tsx` is **814 lines of which ~640 are handlers** — the JSX is 74.
The screen is not a rendering problem, it is a behaviour surface: eleven
lead-note action kinds, nine Deck action kinds, four structured writes, and
an optimistic hide/undo with rollback.

### Backend

`concierge_feed/` is **Vesper-home-only** — Trips Home merely *prefetches*
it to warm the next tab and renders a different engine
(`useTripHomeCards` → `GET /api/trips/{id}/home_cards` → `backend/home/feed.py`).
The import arrow points one way: `concierge_feed` imports **from**
`feed.py`, so killing the rail does not orphan the per-trip assembler.

**⚠ Corrected 2026-07-28.** An earlier draft of this ledger counted
≈4,800 LOC of `concierge_feed` as dead — ~2,000 of 2,279 in
`producers.py`, ~750 of 815 in `ranking.py`, ~640 of 723 in `models.py`.
**That is wrong if the stack adopts it**, which build-plan D1 recommends.
Under adoption the producers, the ladder and the card model all **survive
under new ownership**; what stops is the Vesper-side *rendering*.

So the honest backend ledger is conditional:

| | If Trips adopts `concierge_feed` (D1 = adopt) | If it builds parallel |
|---|---|---|
| `producers.py` / `ranking.py` / `models.py` | **survive**, re-owned by Trips | ≈3,400 dead |
| `deck_payloads.py` (960) | survives only if the crown needs Deck substrate — **open** | dead |
| `pick_judgment.py` (285), `deck_take.py` (180) | dead either way — sole consumer is `concierge_home.py` | dead |
| `/cards/{feedback,lifecycle,restore}` routes | dead either way | dead |

Note the second column is the case the Trips plan explicitly warns
against: *"two rankers over the same trip state will disagree."*

### The Deck — retire, do not delete

**Vesper Home is the Deck's only production entrance.** ~3,950 LOC across
`Deck.tsx` and five faces; the only non-dev importer of anything in
`components/decision-deck/` is `concierge/index.tsx`. Push notifications route
*through* it — `notificationDestination.ts` returns
`routes.conciergeHome(cardId)`, which the screen forwards as
`initialFocusedCardId`.

**Decision: keep, framed as a handover in waiting.** `DeckStructuredFace`
handles proposal approval, choice vote, settle, plan readiness, traveler
readiness — precisely the interactions the stack model says Trips will own.
This is not dead code we are nervous about deleting; it is **the candidate
decision-UI kit awaiting its new host**. Deletion is cheap later;
recreation is expensive; and the stack model is still untracked in git.

Conditions for keeping it from rotting:

1. **The dev routes are the keep-alive.** `app/dev/deck-gallery.tsx` and
   `deck-qa.tsx` stay reachable so the code stays exercised.
2. **The naming must move.** Landed 2026-07-28: the neutral owner is
   `components/decision-deck/`.
3. **The type block moves first.** Landed 2026-07-28:
   `components/decision-deck/model.ts` owns the canonical Deck/card types
   and defensive parsers; `useConciergeHomeState.ts` now owns only the
   Vesper fallback state machine and keeps compatibility re-exports.
4. **Expiry:** if Trips ships its queue without adopting these faces,
   delete then.

**Extraction landed:** app `8947b1c7` (program seam S2). Both dev routes
remain compiled and their focused gallery/face suites pass.

### Must survive

`ComposerBar.tsx` (shared with concierge chat, trip chat,
conversations/create) · `YouEntryControl` · `VesperSignature` (16 files) ·
`components/ui/*` · `utils/cardActionContract.ts` (**split** — only
`deckCardActionContract` is Deck-exclusive) · `conversationSeed.ts`.

**The one contract a replacement must keep emitting:** `cardSeed()` →
`ConversationSeed`, consumed by `chat.tsx` via `parseSeed`. That is the
seam between home and chat and it survives regardless.

### Traps

- Eight convention tests hard-code focus-home paths and will fail on
  delete.
- `ConsequenceContext` lists `'vesper_home'` as a surface; four write hooks
  tag receipts with it.
- `data/conversations.ts` has **two duplicate map bodies** — inline in
  `useConversationHistory` and in `mapRawToSessions`. Editing one silently
  diverges the hooks.
- There is **no DB-level test of `get_conversation_list_for_user`**;
  existing coverage patches it out.

## Voice — honest status, VERIFIED

| Path | Built | Blocker |
|---|---|---|
| **TAP** (dictation) | **~5%** | No STT of any kind. One audio dep (`expo-audio`, playback only); `liveAudioSessionProvider` and `sileroVadWrapper` are DI shells against uninstalled packages. Needs a recognizer — **on-device is dramatically cheaper** than record-and-upload (no backend, no LiveKit, no secrets). |
| **HOLD** (conversation) | **~65%** (backend ~90%, FE ~45%) | `@livekit/react-native` is not installed and `configureVoiceRoomConnector()` is called **only from a test**. Behind that: `docs/VOICE_NATIVE_WIRING.md` states no native audio behaviour has been exercised on hardware. |

**Behind the gate: ~3,100 LOC, substantially complete** — a full LiveKit
Agents worker with Deepgram STT and Cartesia TTS routed through the same
concierge session as text, token endpoint with auth hardening and
per-phase quotas, narration-interrupt handoff, Python deps pinned, tests
landed.

**Narration TTS is real and partly ungated.** In-thread `NarrationCard` is
**not** flag-gated. On a backend with a Cartesia key and the arq worker
running, **Vesper already speaks in chat today.**

**Build trap:** `app.config.js:87` injects `NSMicrophoneUsageDescription`
**only** when `EXPO_PUBLIC_VOICE_ENABLED=true`, and iOS hard-terminates on
any mic call without it. This blocks the TAP path too. Decide the
permission posture once, early.

## Three open decisions

These gate the page. None are resolved.

1. **The Deck's fate.** Retire-and-keep is recommended above, but the
   *destination* is unanswered: does Trips adopt these five faces, or
   rebuild? That is the difference between a contained project and a
   two-surface one.
2. **Where the hero's grounding comes from.** The lead note's only
   substantive input is `focus_title` / `focus_detail`, **copied off the
   top-ranked card**. Remove the rail and the prompt renders "Relevant
   focus: None" — you get *"Barcelona in 4 days."* **Recommendation: one
   ranker, two consumers** — Trips renders the stack ranker as a queue and
   owns the decisions; Vesper reads the winning item as grounding for one
   sentence. Cost: couples this timeline to unbuilt stack-model work.
   Fallback: keep a headless slice of Vesper's own ranking, which
   reintroduces a second cross-trip ranker.
3. **The promotion moment.** Does a session become a draft trip eagerly, or
   only at an explicit "make this a trip"? Lazy matches this design; eager
   keeps Trips the sole owner of anything trip-shaped.

### ⚠ Updated 2026-07-28, later the same day

The stack model **was committed while this spec was being written** —
`86c41ba` (spec + canon registration) and `2320818` (five-phase build
plan). That build plan changes two of the three decisions above.

**Decision 2 is resolved, and the resolution is that nothing has to
change.** Build-plan **D1** — **ratified by founder 2026-07-28 (program
F1), conditions appended to the Trips plan** — has the stack **adopt
`concierge_feed` as its ranker** rather than build a second one: *"the
stack model is a new projection over the same ranked candidates, not a
fork of the ranker."*
If Trips renders `concierge_feed`'s output and Vesper's hero already reads
`concierge_feed`'s top-ranked card for `focus_title` / `focus_detail`,
then **the grounding pipe is untouched.** The ranker keeps running; only
the Vesper-side *rendering* stops. "One ranker, two consumers" turns out
not to be a new architecture — it is the existing one, with one consumer
changing what it draws.

**Decision 1 is now a stated recommendation on both sides.** Build-plan
**D2** ("what happens to the Concierge tab") lists three answers and
recommends: *"Trips home becomes the queue; Concierge stays sessions…
`FocusHome` retires or narrows to the Deck experience. Cleanest story,
matches the Workbench session's framing (**'Trips owns objects, Vesper
owns sessions'**)."* Two sessions reached the same ownership line
independently, and the Trips plan cites this one. It remains **blocking**
until the founder rules — the plan says do not start its phase 2 without
an answer.

## Sequencing

**Superseded by the program doc for ordering** —
`home-surfaces-program-2026-07-28.md` owns execution order across all
three surfaces (founder ruled one sequential worktree stream,
2026-07-28). The sequencing below survives as the *within-Vesper*
rationale; the page's gate is now concrete: **program step 5 (Trips
crown cutover) complete**, not abstract decisions.

**Do not plan the page yet.** It has two unresolved dependencies. The row
has none.

**1 · The row, on History.** History is broken today in exactly the ways
the row fixes — an identical gold "V" avatar on every row so a four-person
group thread looks like a solo one, unread reaching the a11y label but
never the glass, no scope signal. Every field is on the wire except
`phase` / `current_goal`, which is the 3-hour cut. No Deck decision, no
ranker, no contested surface. **And it puts the design on a device**, which
nothing in it has been.

**2 · The composer corrections.** `+` in the leading slot, 17px field,
`mute` placeholder (not `muteSoft`, which the ladder declares
*decorative only, never text*), and the dissolve. Independent of
everything above, and improves chat and trip chat at the same time since
`ComposerBar` is shared.

**3 · The page.** Gated on decisions 1 and 2.

**Voice: do not start.** Decide the iOS permission posture; park the rest.
The hold path's last mile is native audio never run on hardware — a
device-lab project, not a design one.

## Corrections owed to other docs

Found while verifying. All four actively mislead.

| Doc | Claim | Truth |
|---|---|---|
| `docs/systems/concierge-vesper.md` | live mic gated by "the commented-out `voice` process in fly.toml, not a `VOICE_ENABLED` flag" | **Both halves false.** `fly.toml:98` defines `voice = "python -m backend.voice.worker"`; the header at `:33-48` says so explicitly. And `EXPO_PUBLIC_VOICE_ENABLED` is exactly such a flag. Real gates: six unset `VOICE_*` secrets, machines at `count=0`, client flag false + SDK not installed. |
| `backend/voice/worker.py:212` | logs "uncomment the 'voice' process group in fly.toml" | Stale. Likely the origin of the above. |
| `travel-app/utils/api/types.ts:1580-1588` | schema regen "is currently hand-bridged" | Scoped to two types not emitted as named schemas. The three-hop chain works — both snapshot checks pass and `ConversationListItem` is fully generated. Narrow the comment. |
| `ComposerBar.tsx:107-111` | "The button renders regardless of `VOICE_ENABLED`" | False — both callers gate the `onVoice` prop itself. |

## Falsifiers

Reconsider this model if:

- The row does not survive History on a device.
- The cold state reads as unfinished rather than confident.
- Removing the rail degrades the read line and no grounding replacement
  lands — at which point the page's centrepiece is worse than what it
  replaced.
- Trips ships its queue without adopting the Deck faces **and** without a
  ranker Vesper can read — which would mean the ownership split cost more
  than it bought.
- Travellers reach for Vesper expecting the decision queue and cannot find
  it. Findability, not click count, is the measure.

## References

- Design of record: Claude Design → Vesper → **"Vesper Home - Workbench.html"**
  (+ `vesper-workbench.jsx`, `-voice.jsx`, `-keyboard.jsx`). Bundle:
  `~/Downloads/vesper 400`, 2026-07-28 01:37.
- `docs/working/trips-home-promotion-model-2026-07-27.md` — the counterpart home (committed `86c41ba`)
- `docs/working/trips-home-stack-build-plan-2026-07-28.md` — its build plan (`2320818`); **D1** recommends adopting `concierge_feed` as the ranker, **D2** recommends this spec's ownership rule and is blocking
- `docs/working/chat-typography-plan-2026-07-28.md` — the type rule this defers to
- `docs/working/global-navigation-ia-proposal-2026-07-25.md` — Vesper's ownership clause
- `travel-app/docs/surfaces/vesper-home/contract.md` — superseded on promotion
- `travel-app/components/chat/ComposerBar.tsx` — the measured composer
- `travel-agent/backend/home/concierge_feed/` — the engine that retires with the rail
- `travel-agent/backend/voice/` + `docs/VOICE_NATIVE_WIRING.md` — voice status
- Claude Design → Vesper → `trips-home-row-studies.jsx` — the row spine to hold
