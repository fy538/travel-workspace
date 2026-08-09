---
doc_type: working
status: active
owner: founder / engineering
created: 2026-08-09
expires: 2026-09-08
why_new: Re-baselines the next home-surfaces program against the external canonical bundle after the correctness and frontend-consolidation slices.
---

# Home Surfaces — Canonical Rebaseline and Execution Plan

**Date:** 2026-08-09

**Canonical design bundle:** `/Users/feihuyan/Downloads/vesper-home-surfaces`

**Frontend base:** `codex/home-surfaces-app-next` at `77fd99cd`

**Backend base:** `codex/home-surfaces-backend-next` at `8aa85d3b`

**Workspace base:** `codex/home-surfaces-coordination` at `ff0fd9f`

## 1. Executive position

The program has completed its first correctness and consolidation slice. It has
not completed the canonical product direction.

The next program must distinguish four different claims:

1. a semantic section or card kind exists;
2. a producer can emit it;
3. a dedicated composition faithfully renders it; and
4. the composition has been observed with real data on a supported device.

The canonical bundle makes the gap look smaller at the section level and larger
at the composition level:

- Places produces 14 of 15 declared section reasons, but most of the proposed
  one-place registers, candidate arrangements, reading registers, return
  compositions, social aggregates, and personal-record compositions have no
  dedicated composer.
- Trips has a mature crown and emits a broad vocabulary, but many kinds still
  fall back to the crown or generic queue because their dedicated below-crown
  composition is absent.
- The current governed inventory contains 33 composition families: 13 adopted,
  19 unresolved, and 1 relocated. Unresolved frames are not an implementation
  backlog until the founder records an adoption decision.

The next phase is therefore **adopt, complete vertically, compose the page, and
prove it**. It is not a frame-by-frame port of the HTML boards.

## 2. Authority and interpretation rules

Read the bundle in this order:

1. `HANDOFF.md`
2. `Build Manifest - Both Surfaces.dc.html` for re-verified state
3. `Canon - Home Surfaces.dc.html` for vocabulary and ownership
4. `Places - The Page.dc.html` and `Trips - The Page.dc.html` for compositions
5. the two `As Built` boards for historical render context

The source code remains implementation fact. When a board drawing and the
current component disagree, inspect `constants/cardSurface.ts`, the named
typography role, the producer, and the live render path before deciding which
one is wrong. Record disagreements; do not silently reconcile them.

The external bundle stays outside every repository. Runtime code and CI may use
semantic contracts and the checked-in authority/hash record, never the
operator's Downloads path or copied HTML/screenshots.

## 3. Visual rules that apply to every slice

- A card boundary means an object can be completed or resolved in place. A row
  normally points elsewhere. Containment follows the object, not the section.
- `paperBanded` is two hairlines only: no fill, side border, radius, bleed, or
  negative margin.
- `paperOutline` is a hairline outline with no fill.
- `paperQuiet` is lighter than the page, with a hairline and subtle lift.
- There is no adopted full-bleed home-surface material. A full-bleed board frame
  is a new-material proposal, not permission to emulate it with margins.
- Root media remains the existing illustration family unless a specific media
  direction is adopted. The boards do not authorize a photography migration.
- Productive structure uses the system sans. EB Garamond is a bounded editorial
  or journal voice, not the default interface face. Mono is used for stamps,
  labels, counts, and evidence apparatus. Italics require a named semantic role.
- Page rhythm belongs to the Trips plan or Places feed frame. Cards do not own
  outer spacing.
- Places Whole Pages variant A remains the current rhythm authority. The other
  variants remain exploration until explicitly adopted.

## 4. Canonical coverage map

### 4.1 Places

| Group | Canonical composition | Current state | Program disposition |
|---|---|---|---|
| A | One place, six registers | Generic candidate and notice paths exist; recommendation is intentionally dark; no register composer | Decide registers individually. Build only grounded register payloads. Keep conviction blocked. |
| B | Candidate sets and experience arrangements | Candidate rows, count doors, and experience rail ship; lead hierarchy is weak; comparison, stack, quiet-panel set, and ticket stub are absent | Fidelity-pass the adopted row/rail first. Adopt arrangements separately. |
| C | Composed map/route | Selector substrate exists; no Places-root caller; trip/day ownership is relocated to Trips | Keep root map dark until ownership and posture are decided. |
| D | Reading cover and registers | Editorial cover and angle fork ship; mirrored spine, lens switcher, preview registers, and overlay are absent | Fidelity-pass current reading. Require a typed register before new variants. |
| E | Memory and return | Anniversary memory ships; postcard, shelf, row, and Go Back are absent | Keep return compositions behind an adoption and destination decision. |
| F | People | Friend strip ships; co-sign, Again, and trip marker aggregation are absent | Preserve passive friend strip; require privacy-safe aggregate reads for new compositions. |
| G | Personal record | No dedicated belonging, tally, rhythm, or Rest composition | Wait for trustworthy visit/return aggregation and a page-length decision. |

High-leverage existing plumbing gaps:

- `PlacesCard.reason` is rendered but no backend producer populates it.
- `PlacesSection.note` and `.count` are legal and rendered, but only a small
  subset of producers populate them.
- `saved_unvisited` is declared and ranked but has no producer because the
  visit signal is absent.
- `conviction` is client-complete and intentionally unproduced because there is
  no non-proximity confidence signal.

### 4.2 Trips

| Group | Canonical composition | Current state | Program disposition |
|---|---|---|---|
| A | Crown and receipt vocabulary | Crown shell and receipt dispatcher ship; Near You lacks its own receipt | Fidelity and real-data proof first; decide the dedicated Near You receipt separately. |
| B | Now, countdown, temporal strip | Now and countdown ship; temporal strip is absent | Keep current pair; add a strip only with a real day-shape receipt. |
| C | Room, seat, people, trail | Group room and trail ship; dedicated seat/Your People compositions are absent | Complete a coherent, authorized view model before expanding. |
| D | Conditions and decision evidence | Conditions ships; work receipt, compare foot, open-loop table, price ladder, and table are not dedicated sections | Do not expose a decision composition without a real resolver/writer. |
| E | Also in Play, depth, draft shelf | Also in Play ships; dedicated depth and draft shelf are absent | These are the cheapest candidates if adopted because client state already exists. |
| F | Local plans, occasions, hosting | Local Plans exists behind dogfood posture; occasion/hosting model is unresolved | Decide what counts as an occasion before creating entities or cards. |
| G | Companion and pre-trip approach | Companion ships; This Week, This Weekend, and Saved Unplaced are absent | Require typed selectors/modules rather than mining the generic queue. |
| H | Return | Retrospective substrate can rank; dedicated Return and Since You Last Looked compositions are absent | Block on a real story destination and return action semantics. |
| I | Mast and asks | Mast, standing ask, and voice-gated ask ship | Fidelity/telemetry only unless voice posture changes. |
| J | Maps | Today Mapped is implemented and gated; crossing, whole-trip, member, neighborhood, photo, and reachable-cluster selectors are incomplete/absent | Prove Today Mapped first. Add selectors one at a time; keep location/photo privacy explicit. |
| K | Trip Feel | Current two-tile question ships; reduced/resumed/answered state family is incomplete | Decide persistence and resumption before implementing the state family. |

## 5. Target architecture

### 5.1 Trips

`TripsHomeSectionPlan` becomes the complete authority for current authored
sections. Each plan entry owns:

- semantic slot and authored order;
- ready, empty, unavailable, or dark render state;
- content identity and content revision;
- typed action or explicit passivity;
- containment recipe and adjacency rhythm;
- grounding summary and rejection reason; and
- telemetry identity.

The root must not separately rediscover section existence with one-off booleans.
Side data such as weather, roster, or live situation must join by the module's
trip/locality identity and expose unavailable on mismatch. The eventual body
renders typed entries through a bounded renderer registry rather than receiving
an ever-growing controller prop bag.

### 5.2 Places

Places remains server-produced. The frontend pipeline is:

```text
Places query/controller
  -> pure PlacesPresentationModel
  -> feed frame and page rhythm
  -> exhaustive family renderer registry
  -> typed actions through data/domain bridges
```

New adopted compositions extend the existing orthogonal identity:

```text
reason x card kind x treatment x register/arrangement
```

Add only the smallest discriminated union needed by an adopted vertical slice.
Do not send React component names, layout trees, style objects, or generic
metadata from the backend.

## 6. Execution phases

### Phase 0 — Land and prove the consolidated base

1. Review and integrate the three current `codex/home-surfaces-*` branches.
2. Capture a clean single-run iOS baseline for every existing Trips and Places
   state fixture. Eliminate simulator-runner contention before accepting pixels.
3. Add Android, 320/360/393-equivalent widths, large Dynamic Type, offline,
   empty, partial, error, and background/foreground dwell baselines.
4. Run one authenticated backend-real capture for each surface.
5. Update evidence receipts and the inventory without changing adoption state.

Exit: the current 13 adopted families have a trustworthy baseline, branch
history is integrated, and no proposed family is being evaluated against stale
pixels.

### Phase 1 — Founder adoption workshop

Record an explicit verdict for each of the 19 unresolved inventory families.
The workshop should decide families, not individual decorative frames.

Recommended defaults:

- preserve current candidate rows, experience rail, reading, memory, friend
  strip, crown, core modules, trail, companion, mast, and asks;
- keep conviction, saved-unvisited, raised return, belonging, and The Rest
  gated on their missing signals;
- keep expanded people/location/photo map concepts dark pending privacy review;
- keep hosting/local-plan expansion dark until "what is an occasion?" is
  answered;
- treat full-bleed, new photography, and alternate whole-page rhythms as
  separate design-system decisions;
- consider Trips depth/draft shelf, Places grounded reason/editor's note, and
  Today Mapped proof as the lowest-risk next candidates.

Exit: every inventory family is adopted, exploratory, relocated, rejected, or
deferred with an owner and blocker.

### Phase 2 — Finish the architecture authorities

#### Trips work package

- Promote the current plan from membership/identity authority to complete
  render/action/containment/rhythm authority.
- Fold leaf existence gates into pure entry construction.
- Create a typed section view model and bounded renderer registry.
- Replace the broad controller-to-body prop bag with grouped page, section,
  action, and telemetry models.
- Preserve authored order and the current containment sequence:
  Now 2 -> Crown 5 -> Countdown 3 -> Conditions 2 -> Group 0.

#### Places work package

- Keep the pure presentation model as the only feed-to-render adapter.
- Make renderer family exhaustiveness mechanically checked.
- Keep action/data hooks behind the data bridge.
- Move remaining family-specific helpers and visual components out of the feed
  dispatcher without creating premature generic abstractions.
- Add register/arrangement identity only for an adopted composition.

Exit: neither page root can render, space, or instrument a section that its
pure authority has rejected or omitted.

### Phase 3 — Complete existing plumbing before new families

#### Places tranche

1. Define a grounded `PlacesCard.reason` production policy. Populate it only
   when a producer can name the supporting signal; a save, distance, or category
   alone does not become a recommendation claim.
2. Populate honest section `note` and `count` fields where producers already
   possess qualified totals or editorial context.
3. Add producer/contract tests proving reason text is informative, attributable
   to stored evidence, and not a restatement of title/meta.
4. Keep conviction and saved-unvisited unproduced.

#### Trips tranche

1. Key Now situation, conditions/weather, and group roster joins to the planned
   module's trip/locality identity.
2. Render explicit unavailable states for mismatched or missing side receipts.
3. Verify old-server/cache compatibility or adopt an explicit minimum-version
   cutover with cache invalidation.
4. Make every current module fixture producible in the canonical mock lane.

Exit: existing adopted cards receive all fields the current contract can
honestly provide, and no card composes facts from different trips/localities.

### Phase 4 — Implement adopted families as vertical slices

Each family is one vertical work package:

```text
decision -> evidence model -> producer/selector -> generated contract
         -> pure presentation -> renderer -> action/destination
         -> exposure/engagement -> fixture -> backend-real -> device receipt
```

Recommended order after Phase 1 decisions:

1. **Today Mapped acceptance:** render and prove the existing read model before
   expanding map vocabulary.
2. **Trips depth or draft shelf:** low contract risk; state already exists on
   the client. Confirm it adds composition rather than duplicating Also in Play.
3. **Places grounded reason/editor's note:** one existing field unlocks why-lines
   across several adopted candidate arrangements.
4. **Places Changed register:** existing reason and scalar substrate, but add a
   typed state-diff payload rather than parsing prose.
5. **Trip Feel state family:** only after persistence/resumption is decided.
6. **One selector-only map expansion:** crossing or neighborhood before whole-
   trip/member/photo maps; no new generic map engine.

Do not schedule signal-gated families in this phase.

### Phase 5 — Page rhythm and posture composition

After adopted family slices are stable:

- produce whole-page fixtures for every Trips state and Places posture;
- make adjacency spacing a pure plan/feed-frame decision;
- cap repeated geometry and voices without arbitrary per-card margins;
- confirm the floating navigation never obscures the final meaningful section;
- verify empty/partial/unavailable sections collapse without wrapper gaps; and
- compare current pixels to the canonical compositions while treating the
  source token recipes as material truth.

This phase may tune rhythm variant A. It may not silently adopt exploratory
whole-page variants.

### Phase 6 — Signal-owned work

These are separate upstream programs, not card tasks:

- **Visit signal, spatial-owned:** unlocks `saved_unvisited`, a raised return,
  and higher belonging registers.
- **Non-proximity confidence, affinity-owned:** prerequisite for conviction.
- **Occasion/domain model:** prerequisite for hosting and ambiguous local-plan
  expansion.
- **Return destination/write path:** prerequisite for dedicated return stories
  and comparison resolution.

Home-surface agents consume these signals after they exist; they do not invent
surrogates in UI code.

### Phase 7 — Acceptance

For each adopted family and whole-page state:

- deterministic mock fixture reviewed against the verified design hashes;
- backend-real/authenticated canary;
- iOS and Android at supported widths;
- large Dynamic Type;
- offline, refresh failure, and partial producer failure;
- background/foreground dwell and exposure dedupe;
- privacy/action/mutation trace; and
- physical-device founder/design verdict recorded as an immutable receipt.

Only then may the inventory move `V` to `verified` or use accepted/shipped
language for that named state and platform.

## 7. Parallel dispatch plan

The coordinator owns hot roots, schema generation, inventory status, and branch
integration. Up to three bounded agents can run beside the coordinator.

| Wave | Agent lane A | Agent lane B | Agent lane C | Serialized coordinator work |
|---|---|---|---|---|
| 0 | Places fixture/capture inventory | Trips fixture/capture inventory | QA runner/device matrix | Branch integration and evidence receipts |
| 1 | Places adopted-family fidelity audit | Trips adopted-family fidelity audit | Adoption-ledger preparation | Founder decisions and ledger merge |
| 2 | Places reason/note producer tests | Trips plan/view-model extraction | Shared QA/state fixtures | Review hot roots; run schema train if needed |
| 3 | One adopted Places vertical slice | One adopted Trips vertical slice | Device/evidence automation | Contract generation, integration, cross-surface review |
| 4 | Places whole-page posture fixtures | Trips whole-page state fixtures | Accessibility/platform matrix | Rhythm adjudication and acceptance ledger |

Hot-file ownership remains single-writer:

- `TripsHomeController.ts` and `TripsHomeBody.tsx`: one Trips integrator;
- `PlacesWorkspace.tsx` and `PlacesSectionFeed.tsx`: one Places integrator;
- generated schema and OpenAPI snapshots: one schema owner;
- `cardSurface.ts` and typography tokens: one design-system owner;
- backend Places section/ranking/model files: one backend contract owner per
  schema train.

Each agent returns one reviewable commit, exact tests, evidence layer, files
touched, remaining blockers, and any discovered board/source disagreement.

## 8. Definition of a completed vertical slice

A composition is not complete because a component exists. Its ledger row must
answer all of the following:

- **D:** Which adopted canonical composition and hash?
- **C:** Which dedicated renderer and responsive policy?
- **P:** Which grounded producer or selector?
- **R:** Which generated wire contract and real caller?
- **A:** Which canonical destination/writer, receipt, retry, and reversal path?
- **F:** Which deterministic fixture and reviewed states?
- **B:** Which backend-real artifact?
- **V:** Which physical device/platform acceptance receipt?

An absent signal, producer, destination, or decision keeps the family dark. A
plausible mock is never used to bridge a missing product truth.

## 9. Immediate next slice

Start with Phase 0 and Phase 1 together:

1. integrate the current consolidated branches into one reviewable base;
2. run clean single-device current-state captures;
3. refresh the governed inventory from current source, because the external
   Build Manifest predates the latest correctness commits; and
4. hold one adoption workshop over the 19 unresolved families.

Once those decisions are recorded, dispatch Phase 2 in parallel: one Trips
authority lane, one Places plumbing/fidelity lane, and one QA/evidence lane.
Do not begin a new visual family before that gate.
