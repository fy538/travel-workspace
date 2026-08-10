---
doc_type: working
status: active
owner: frontend / backend / product
created: 2026-08-09
last_reviewed: 2026-08-10
expires: 2026-09-08
why_new: Reconciles the post-consolidation Places and Trips implementation, the August external design authority, and the latest read-only code-review findings into one executable engineering plan.
source_of_truth_for:
  - home-surfaces-post-consolidation-engineering-plan
---

# Home Surfaces — Post-Consolidation Engineering Plan

## 1. Purpose

This document records the next engineering program for the Places and Trips
home surfaces after the August 9 consolidation. It combines:

- the external `vesper-home-surfaces` design bundle;
- the current consolidated frontend and backend source;
- the machine-readable composition inventory;
- the most recent state, full-stack, typography, card-rhythm, action, privacy,
  and telemetry code review;
- the project's MVP evidence rules.

The immediate objective is not to add more speculative card families. It is to
make the currently adopted surface honest, deterministic, polished, maintainable,
and provable before selecting another design family.

This is a working execution plan, not a claim that either surface has passed
backend-real or physical-device acceptance.

## Rebaseline addendum — 2026-08-10

This addendum is the current execution authority for the rest of this document.
The original August 9 investigation remains below as useful history, but its
open/closed finding statuses and pinned revisions are superseded here.

### Revisions and validation

| Repository / authority | Current pinned identity | Worktree state |
|---|---|---|
| Workspace | `travel-workspace` at `78e4a8e34bed22e288b669aa9e03cf14869801d4` | clean `main`, aligned with `origin/main` |
| Frontend | `travel-app` at `c9becf7032199c1eeb8d947e2fc5df0a5f4444da` | clean `main`, aligned with `origin/main` |
| Backend | `travel-agent` at `1bde69535841f849ccdc55550a1d1c6c71fec59d` | clean `main`, aligned with `origin/main` |
| External design authority | `vesper-home-surfaces-2026-08-09` | operator-owned, external only |
| Composition inventory | `home-surfaces-compositions-2026-08-10` | 36 atomic rows, 0 evidence receipts |

The canonical Places and Trips Page/As-Built pairs were revalidated locally
from `/Users/feihuyan/Downloads/vesper-home-surfaces` using
`HOME_SURFACES_CANON_DIR`. The Trips check verified seven registered pairs and
the Places check verified six. The 30 registered polish scenarios also passed
schema validation. The bundle was not copied into application source.

The current frontend passes the home-surface source budgets. Important current
ratchets are:

| Owner | Current / limit | Meaning |
|---|---:|---|
| `TripsHomeController.ts` | 823 / 825 | effectively no safe headroom |
| `TripsHomeBody.tsx` | 745 / 842 | improved, but still a hot composition owner |
| `PlacesWorkspace.tsx` | 758 / 769 | effectively no safe headroom |
| `PlacesSectionFeed.tsx` | 282 / 334 | acceptable executor headroom |
| `PlacesFeedCardView.tsx` | 172 / 176 | registry boundary needs care |

The immediately preceding focused baseline remains green for the unchanged
home-surface source: 100 frontend tests across nine suites, frontend typecheck,
home-surface budgets, and 57 targeted backend Trips fallback tests. These are
source/fixture checks only. No backend-real or physical-device acceptance was
performed, and no `F`, `B`, or `V` receipt may be inferred from them.

### How to read the design bundle now

The bundle has three different kinds of authority and they must not be merged
into one checklist:

1. **Page boards** define current design intent and the allowed composition
   vocabulary.
2. **As-Built/source files** describe implementation fact at their recorded
   date; current repository source wins when those historical files are stale.
3. **The composition inventory** records adoption and evidence. A component can
   be coded and wired while its family remains `unresolved` and unproven.

Several handoff facts are now historical rather than current:

- Places now produces grounded `reason`, `note`, and exact collection `count`
  values. The handoff's “zero producer” statement no longer describes source.
- Local Plans now has an explicit `trip_kind=local` aggregate and promotion
  path. The Page board's earlier question about whether a local plan is a trip
  is settled by current product/source behavior unless product reopens it.
- Today Mapped has authenticated cache-only backend selection, an app query,
  gating, and a renderer. That makes it technically wired, not automatically
  adopted or accepted: its inventory row is still unresolved and has no proof.
- Encounter/occurrence and affinity substrates are richer, but neither
  `saved_unvisited` nor non-proximity conviction is an accepted semantic
  producer. The client must not infer either state.
- `reachable_cluster` remains vocabulary/substrate only; it has no complete
  selector-to-renderer vertical slice.

### Current implementation map

#### Places

The current data path is:

`backend producers/ranking → generated Places feed → strict renderability →`
`presentation sections → responsive feed render plan → section/card registry`

This is the correct architectural direction. Backend order remains the sole
ranking authority; malformed wide-wire payloads are excluded before identity
and exposure are calculated; rail/fork/stack behavior is pure and responsive;
and section impressions are gated by viewport, focus, foreground, and dwell.

| Canonical group | Current implementation | Engineering/adoption result |
|---|---|---|
| A — One Place | candidate/list row is built; grounded reasons now have producer and renderer substrate | Keep the existing row. Select any additional verdict/log/apparatus register explicitly; do not build all six variants by default. |
| B — Several Places | list and experience rail are built; door producer/wiring exists; lead/peer, comparison, stack, stub remain unsettled | Door needs an adoption ruling and proof. Lead hierarchy has conflicting authorities and must not be silently changed. |
| C — Composed Plan | area/map selection substrate exists; day/trip cross-reference relocated to Trips | Keep root map dark until ownership, permission, empty/offline, and privacy policy are decided. |
| D — Reading | existing cover/fork is built | Mirrored spine, lens switcher, dial, and overlay remain design-only. |
| E — Memory | anniversary is built | Postcard, shelf, row, and Go Back remain unresolved. |
| F — People | friend strip is built | Co-sign, Again, and trip marker remain unresolved and need privacy/provenance review. |
| G — Personal Record | no accepted record family | Belonging/tally/rhythm/Rest require explicit product semantics and producers. |

The canonical Places rhythm currently represented in source—7-point card
spacing, 12-point row rhythm, 32-point section rhythm, and one section rule—is
the baseline to preserve. Page-rhythm explorations B–H are not an implicit
refactor brief.

#### Trips

The current data path is:

`trips/ambient queries → controller → transport section plan → route-safe render`
`model → physical page plan → exhaustive body phases → leaf renderers`

The thin route and physical page plan are meaningful consolidation gains. The
remaining problem is that the controller still returns a discovery-heavy flat
surface and contains almost no budget headroom.

| Canonical group | Current implementation | Engineering/adoption result |
|---|---|---|
| A — Crown | all current receipt bodies are supported through the crown renderer | Preserve receipt semantics and canonical writers; focus on state/device proof. |
| B — Time | Now and Countdown are built; temporal strip is not | Split the mixed inventory row before calling this family implemented. |
| C — Room | Group and Trail/Connect are built | Invite seat and Your People remain unresolved. |
| D — Evidence | Conditions is built and intentionally passive | Comparison foot, work receipt, open loops, price ladder, and table remain unresolved. |
| E — Stack | bounded Also In Play queue is built | Depth/draft shelf remain unresolved; queue exposure identity still needs correction. |
| F — What Is the Plan | Local Plans is built on the local-trip aggregate | Hosting and additional registers remain unresolved. |
| G — Approach | Companion is built | This Week/Weekend and Saved Unplaced remain unresolved. |
| H — Return | no adopted return composition | Since You Last Looked/Return need new semantics and producer decisions. |
| I — Voice | mast, Standing Ask, Voice Ask, and offers have current implementations/gates | Standing Ask membership must use authoritative posture rather than legacy hero kind. |
| J — Maps | Today Mapped is full-stack wired behind its own gate | Keep expansion variants dark; decide adoption and prove Today Mapped before adding collaborative/photo/location maps. |
| K — Trip Feel | a static selector/card exists | Persistence, resumption, receded state, and “what remains” are not implemented as a stateful family. |

### Reconciled review findings

The five original Phase 1 correctness defects have landed: honest degraded feed
handling, stable rain/wind weather keys, offline/cache precedence, the dedicated
editorial-map gate with dark-query behavior, and a Places unavailable state.
Six important Phase 2 findings also landed: queue and legacy-row proposal cache
subtraction, ambient placeholder sanitization/auth guards, dark ambient query
suppression, partial/stale banner precedence, exhaustive guide-door routing,
and separation of candidate detail versus save semantics.

The following work remains actionable.

| Priority | Surface | Finding | Required result |
|---|---|---|---|
| P1 | Places | A zero-renderable unavailable/partial response can compose redundant availability messaging, and offline copy can imply a preserved feed when no cards are renderable. | One root-state authority selects exactly one truthful notice/hero/feed state from transport, cache, renderability, and connectivity. |
| P1 | Trips | Standing Ask still derives membership/revision from legacy `heroKind`, which can conflict with authoritative server posture. | Derive the section from normalized projection posture and cover conflicting urgent/crownless states. |
| P2 | Trips | Loading “See all N trips →” is visually a door but is noninteractive text. | Make it an actual typed action or remove door styling/copy while loading. |
| P2 | Trips | Aggregate queue exposure identity is composed from content revisions rather than stable fact/content IDs. | Separate stable entity identity from mutable revision and retain max-two aggregation. |
| P2 | Trips | Local Plans and Day Map share a wrapper without child rhythm; a failed map image can retain empty allocated space. | Plan renderability before allocation and apply an explicit cluster gap without changing global page rhythm. |
| P2 | Places | Loading visibly replaces authored standfirst copy with “Finding your places.” despite the surface contract requiring transport status to be accessibility-only. | Preserve an authored/static visual floor and expose transport status through accessibility semantics. |
| P2 | Places | Full-width editorial supporting previews use System Sans caption 12 instead of the canonical bounded literary register. | Add/use an approved semantic serif preview role near the Page's 16/1.4 target; do not repurpose generic caption. |
| P2 | Places | Grounded candidate reason can extend to two lines, but default/narrow/large-type optical rhythm has no evidence. | Verify plate height, truncation, and sibling alignment with deterministic long-copy fixtures and physical devices. |
| P3 | Both | Hot root owners sit on their line ratchets and still expose prop-bag/discovery architecture. | Extract behavior-preserving adapters/controllers with at least 20% measured headroom. |
| P3 | Governance | Mixed inventory rows and zero receipts obscure what is implemented versus adopted versus accepted. | Split rows, record decisions, and issue immutable F/B/V receipts only from qualifying evidence. |

### Design conflicts that require a ruling

These are not safe “polish fixes”:

- **Places lead hierarchy:** the Page board proposes strong scale/orientation
  hierarchy, a local contract records a different 62/50 plate treatment, and
  current source intentionally renders equal 92-point geometry while producers
  mark every item as lead. Product/design must define lead semantics and select
  one geometry before engineering changes it.
- **Places tonal material:** one local contract describes memory/prompt paper,
  while the Page/As-Built and current source use uncarded treatment. Source
  remains the implementation truth until the contract is reconciled.
- **Places notice/prompt ownership:** the Page suggests moving the spine to
  Trips/Plans, while current backend producers still intentionally emit these
  families. Relocation requires a producer and destination decision, not merely
  hiding the cards.
- **Today Mapped:** technical implementation exists, but product adoption,
  privacy/permission behavior, and evidence remain open. “Rendered in source”
  is not equivalent to “adopted.”
- **Conditions interaction:** the transport plan can carry a route, but the
  canonical/current UI is deliberately passive. Do not invent a weather CTA.

### Revised engineering roadmap

#### R0 — Make the ledger honest

One governance owner updates the composition inventory before new family work:

1. Split Trips Time into adopted Now, adopted Countdown, and unresolved
   Temporal Strip rows.
2. Split Trip Feel's current static selector from stateful persistence,
   resumption, receded, and “what remains” variants.
3. Record Today Mapped as technically source-complete but adoption-unresolved;
   keep map expansions separate.
4. Reconcile Local Plans with the current `trip_kind=local` product model.
5. Record grounded Places `reason`/`note`/`count` producer progress without
   silently adopting new register compositions.
6. Add explicit product-decision fields: verdict, owner, rationale,
   prerequisite, and review date.

Exit gate: every inventory row describes one independently adoptable family;
`D/C/P/R/A` and `F/B/V` states are not conflated.

#### R1 — Correct state and semantic truth

These packages are behavior changes and should land before visual work.

**R1-P — Places root-state authority**

- Add a pure state selector over request status, cached transport content,
  renderable section count, unavailable producers, refresh failure, and offline
  status.
- Produce one mutually exclusive result for loading, unavailable, empty,
  partial-with-content, stale-with-content, offline-with-content, and ready.
- Delete duplicate notice/hero decisions from `PlacesWorkspace` after parity
  tests exist.
- Test the all-optional-producers-unavailable case and offline zero-renderable
  case explicitly.

**R1-T — Trips posture and loading action**

- Normalize authoritative server posture once in the controller composition
  layer.
- Make Standing Ask visibility, revision, and copy consume that posture.
- Characterize urgent, crownless, cached, partial, and fallback combinations.
- Resolve “See all N trips” as a real action or honest non-door copy.

**R1-Q — Stable queue telemetry identity**

- Give the aggregate queue separate stable content IDs and mutable revision.
- Preserve the current two-item visible cap and one physical exposure boundary.
- Ensure copy-only revision changes do not remint entity identity.

Exit gate: focused tests, typecheck, source budgets, and no invented product
state. These commits make no visual/device acceptance claim.

#### R2 — Polish only the adopted baseline

**R2-P — Places typography and loading voice**

- Keep visible loading voice authored/static; use accessibility state for
  transport progress.
- Introduce a named editorial-supporting semantic text role, or a bounded local
  spec style if no system role fits. Target the Page's EB Garamond-like
  16-point/1.4 register without globally changing caption.
- Exercise ordinary and maximal editorial copy at narrow width and large type.
- Add long grounded-reason fixtures for candidate rows.

**R2-T — Trips cluster rhythm and failed-media allocation**

- Compute Day Map leaf renderability, including valid media, before the body
  allocates its wrapper.
- Add a local, tokenized gap between Local Plans and Today Mapped when both
  render.
- Verify one-leaf and zero-leaf clusters do not retain phantom margin.
- Check footer/floating-create clearance without changing the overall page
  rhythm.

Exit gate: deterministic screenshot fixtures at approximately 320, 360, and
393 points plus baseline and enlarged text. Screenshots are regression evidence,
not physical-device acceptance.

#### R3 — Restore architectural headroom

Behavior and architecture commits must remain separate.

**R3-P — Places workspace decomposition**

- Extract query/location orchestration from root rendering.
- Extract the mutually exclusive root-state presenter from R1-P.
- Package search/map/saved/reading doors into a typed navigation adapter.
- Remove the production-dead legacy `utils/placesWorkspace.ts` model after its
  remaining tests are migrated.
- Keep ranking, section order, card mutations, and leaf route destinations
  unchanged.

**R3-T — Trips controller/body decomposition**

- Replace the approximately 80-field controller return with cohesive `page`,
  `sections`, `actions`, `chrome`, and `telemetry` adapters.
- Move query interpretation and composition into pure builders; keep hooks and
  effects in the controller.
- Extract phase renderers from the body without changing SoftReveal/crown
  containment or canonical writers.
- Retain the page plan as the sole physical-order authority.

Exit gate: each hot owner has at least 20% ratchet headroom, focused behavior
tests are unchanged, full typecheck passes, and architecture contracts prevent
responsibility from migrating back into the roots.

#### R4 — Founder/product decision packets

No new family is coded until its packet receives `adopt`, `defer`, `reject`, or
`relocate` plus an owner and rationale.

1. **Places registers:** choose among verdict, log, apparatus, caveat, and
   recommendation; settle door and lead/peer semantics.
2. **Places composition/record:** root map, reading variants, return/memory,
   social variants, and personal record.
3. **Trips time/people:** temporal strip, Near You, invite seat, Your People.
4. **Trips evidence/depth/local:** comparison evidence, depth/draft shelf,
   Local Plans extensions, and hosting.
5. **Trips maps/return:** Today Mapped adoption, map expansions, pretrip, and
   Return.
6. **Trips Trip Feel:** persistence, resumption, receded state, and remaining
   work.

Recommended no-regret posture:

- adopt and prove grounded Places reason/note/count inside already accepted
  row/collection patterns;
- evaluate Today Mapped as the only map slice before any collaborative,
  member-location, photo-location, or reachable-now expansion;
- defer conviction and `saved_unvisited` until accepted producer semantics
  exist;
- defer hosting, return/personal record, collaborative maps, and stateful Trip
  Feel until their privacy/domain decisions are explicit;
- do not create client-side section ranking or server-provided style/component
  metadata.

#### R5 — Build selected vertical slices

Each adopted family travels as one vertical slice:

`semantic producer → additive schema → generated types → client selector/state →`
`renderer/action → fixture proof → backend-real proof → device proof`

Likely slice shapes:

- **Today Mapped hardening:** mostly existing schema/plumbing; concentrate on
  permission, offline/cache, media failure, privacy, and proof.
- **One Places register:** reuse grounded reason/note/count only if the selected
  Page composition can be represented without client inference.
- **Stateful Trip Feel:** requires a single canonical writer, persistence and
  revision semantics, unavailable/cached behavior, and resumption policy before
  UI variants.
- **Temporal/depth/draft:** first define whether state is authoritative backend
  truth, bounded local draft, or derived read model; do not start from the card.

For schema-bearing slices, merge order is backend additive contract, workspace
OpenAPI snapshots/generated app types, frontend consumption, backend deployment,
then app rollout. Destructive removals wait for minimum-client and cache-expiry
policy.

#### R6 — Evidence and acceptance

For every adopted visible family:

- `F`: exact fixture, authority hash, width, font scale, state, and screenshot;
- `B`: authenticated backend-real projection with real IDs/revisions/routes,
  including partial and cached/offline behavior;
- `V`: physical iOS and Android, baseline and a large Dynamic Type setting,
  online, offline-with-cache, offline-cold, loading, empty, partial, error, and
  relevant permission-denied/background-foreground paths.

Receipts are immutable, workspace-relative, and name item ID, layer, kind,
source, date, summary, and platform for `V`. A source-complete family remains
unaccepted while any required receipt is absent.

### Parallel execution and file ownership

Use no more than three implementation lanes plus one integration coordinator.
Parallelism is by repository and hot-file ownership, not by arbitrary card
count.

| Wave | Lane A | Lane B | Lane C | Dependency |
|---|---|---|---|---|
| A | R1-P Places state | R1-T Trips posture/action | R0 inventory/governance | independent; coordinator owns cross-doc reconciliation |
| B | R2-P Places typography/voice | R2-T Trips rhythm/media | R1-Q queue identity | begins after relevant R1 behavior lands |
| C | R3-P Places architecture | R3-T Trips architecture | fixture/evidence harness | interface freeze after Waves A/B |
| D | product decision workshop | producer/privacy investigation | evidence-state audit | no speculative UI implementation |
| E | one backend/schema owner | one frontend owner per selected surface | backend-real/device QA | only for adopted slices |

Exclusive hot-file locks:

- one owner at a time for `PlacesWorkspace.tsx` and its root-state tests;
- one owner at a time for `TripsHomeController.ts` and controller contracts;
- one owner at a time for `TripsHomeBody.tsx` and phase renderer ownership;
- one schema owner for backend models, OpenAPI snapshots, and generated types;
- one inventory owner for adoption/evidence fields.

Every commit reports base SHA, explicit touched paths, focused tests, broader
verification, compatibility statement, and evidence limitations. Stage by
filename, never broad-add. Integration order follows dependency order; old
branches/worktrees are historical evidence and are not merged merely because
they contain a similarly named fix.

### Immediate next engineering slice

Start with Wave A. It is the smallest set that makes the current surface honest
before visual tuning:

1. land R0's inventory split and status reconciliation in the workspace;
2. land R1-P as a pure Places root-state selector plus root consumption;
3. land R1-T as authoritative Trips posture plus the loading-action correction;
4. land R1-Q separately if it does not collide with the Trips controller owner;
5. rerun focused suites, full frontend typecheck, home-surface budgets, design
   hash checks, and composition inventory validation;
6. only then begin the typography/rhythm wave.

This ordering avoids polishing dishonest states, keeps behavior fixes separate
from consolidation, and leaves unresolved Page-board families dark until the
product decision packet is complete.

## 2. Review baseline

The investigation that produced this plan was read-only and pinned to:

| Repository / authority | Revision or identity |
|---|---|
| Frontend | `travel-app` at `f7549bd7` |
| Backend | `travel-agent` at `43ba3e4e` |
| Workspace composition inventory | `home-surfaces-composition-v1`, as of 2026-08-09 |
| External design authority | `vesper-home-surfaces-2026-08-09` |
| External bundle | Operator-owned `/Users/feihuyan/Downloads/vesper-home-surfaces` |

The external bundle remains outside the repositories. CI and production source
must not import or copy it. Local design review supplies it through
`HOME_SURFACES_CANON_DIR` and validates the registered content hashes.

The investigation found that the core consolidation work is present, but the
existing audit, roadmap, ledger, and inventory documents lag the final merged
implementation. Phase 0 below reconciles that documentation before it becomes
the basis for further dispatch.

## 3. Current implementation state

### 3.1 Inventory status

The current machine inventory has 36 atomic rows:

| Adoption state | Count |
|---|---:|
| Adopted | 15 |
| Exploratory | 1 |
| Unresolved | 19 |
| Relocated | 1 |

Its evidence boundary is still static/source-only:

| Evidence layer | Current result |
|---|---|
| Fixture/visual, `F` | 36 not verified |
| Backend-real, `B` | 34 not verified, 2 not applicable |
| Physical device, `V` | 36 not verified |
| Immutable evidence receipts | 0 |

Several inventory rows combine implemented and missing variants. For example,
`trips-b-time` combines shipping Now and Countdown modules with an absent
temporal strip. These rows must be split before the inventory can accurately
drive implementation or adoption decisions.

### 3.2 What is implemented

#### Trips

- Thin route boundary into a controller and pure presentation/composition
  chain.
- Route-safe crown, dedicated Now, Countdown, Conditions, and Group modules.
- One bounded aggregate Also in Play queue.
- Physical page plan and exhaustive body-render phases.
- Standing Ask, Local Plans, Day Map, Companion, Dreams, Trip Feel, Trail,
  footer, and floating create entries with their current gates.
- Typed destinations and canonical proposal resolution paths.
- Section exposure boundaries and content revisions.

#### Places

- Server-produced, server-ordered section feed.
- Pure presentation and responsive render plans.
- Strict card kind/payload renderability guards.
- Candidate, editorial, experience, memory, social, notice, and prompt families.
- Conviction, single, fork, and choice client treatments; conviction remains
  intentionally unproduced.
- Responsive fork and experience-rail degradation.
- Viewport/focus/foreground/dwell-aware exposure handling.
- Grounded candidate reasons and compact collection counts.
- Typed handoffs for place details, reader, map, saved collections, private
  debrief, and Trips-owned add-to-day preview/commit.

### 3.3 What is not implemented end to end

- `saved_unvisited` and the Places raised-return composition: no trustworthy
  visit signal.
- Places conviction: no non-proximity confidence signal.
- Singular Places lead-versus-peer hierarchy: the existing `lead=true` means
  equal complete treatment for both gap alternatives.
- `reachable_cluster`: declared map story kind without a producer and without
  complete composition-coherence validation.
- Expanded map selectors/compositions over crossings, neighborhoods,
  destinations, and members.
- Durable Trip Feel persistence, resumption, reduced, and contrast states.
- Several new return, personal-record, hosting, evidence/decision, temporal,
  and social compositions represented in Page or Prototype boards.
- Backend-real and physical-device acceptance for every inventory row.

These gaps are not all an implementation backlog. Some are deliberately dark,
exploratory, signal-blocked, or awaiting an adoption decision.

## 4. Confirmed review findings

All findings below were rechecked against the consolidated source rather than
copied forward from an older audit.

### 4.1 P1 — state and product-truth defects

#### HS-P1-01 — Trips assembly failure becomes authoritative empty

The Concierge Home delivery boundary catches assembly exceptions and returns a
quiet empty fallback. Trips projects that feed as `projection_state="empty"`,
discarding the degradation distinction. The client can therefore show “nothing
needs attention” during a producer or database outage.

Required behavior:

- Concierge Home may retain its quiet, usable fallback.
- Trips Stack must expose a retryable failure/degraded read, never an
  authoritative empty projection.
- Cached ranked content remains visible when available.
- Without ranked cache, committed trips remain reachable through an explicit
  unranked/degraded state.

#### HS-P1-02 — weather inputs are absent from the query identity

`precipitation_mm` and `wind_kph` affect backend weather production and ranking
but do not participate in the frontend query key. A material weather change can
therefore leave an older crown or nearby ordering cached under the same key.

#### HS-P1-03 — offline Trips can remain in initial loading

The page-state reducer checks a pending stack before returning the cached/offline
state. A user with cached committed trips but no stack projection can remain on
“Vesper is reading your trips” indefinitely while offline.

The implementation currently conflates:

- cached trip-list content;
- cached ranked-stack content;
- placeholder content from a previous ambient key.

These must become separate state inputs.

#### HS-P1-04 — Day Map uses the wrong feature gate

`TRIP_EDITORIAL_MAP_ENABLED` has no production consumer. Day Map membership is
tied to `LOCAL_PLAN_DOGFOOD_ENABLED`, while its endpoint is queried even when the
map surface is dark.

#### HS-P1-05 — zero-renderable partial Places feed becomes a blank page

Any unavailable producer currently makes a feed `partial`, even when no section
has a renderable card. Workspace then says “Showing what’s available” and mounts
an empty feed instead of showing an honest unavailable/retry state.

### 4.2 P2 — action, cache, telemetry, and polish defects

#### Trips

- Terminal proposal cache subtraction filters legacy `rows` but not the current
  `queue`.
- Previous-location placeholder projection data can appear current during
  ambient re-keying.
- Standing Ask follows legacy `heroKind` rather than authoritative server
  posture.
- Loading shows a gold `See all N trips →` label that has no interaction and is
  hidden from accessibility.
- Local Plans and Day Map share a wrapper without a child gap, creating
  touching/doubled outlined borders.
- A disabled Ambient surface still triggers its real trip-home feed query and
  potential LLM-composed work.
- Aggregate queue exposure uses revision bundles as identity rather than stable
  fact/content IDs.
- A Day Map image failure can return `null` after the parent has already
  allocated cluster rhythm.

#### Places

- Loading visibly renders transport copy as the Vesper standfirst even though
  the surface contract requires transport copy to remain accessibility-only.
- Full-width editorial supporting previews use 12pt System Sans caption rather
  than the approved bounded serif reading role.
- Partial-producer and failed-refresh notices can render simultaneously.
- Door routing is non-exhaustive; a future `guide` target falls through to Map.
- A candidate with `verb=save` can label its detail-navigation tap as Save even
  though the actual save is a separate control.
- The new two-line grounded reason has static bounds but no device evidence for
  the longest title/meta/kicker/reason/action combination.

### 4.3 P3 — architecture and governance debt

- `PlacesWorkspace.tsx` is 768 lines against a 769-line ratchet and owns query,
  location, search, root states, mast, navigation, and feed wiring.
- `TripsHomeController.ts` is 809 lines against an 825-line ratchet.
- `TripsHomeBody.tsx` remains a large physical dispatcher at 745 lines.
- The legacy `utils/placesWorkspace.ts` is test-only and preserves an older
  client-owned scope model.
- The composition inventory and execution ledgers do not reflect all merged
  work or the latest review findings.

## 5. Non-negotiable boundaries

### 5.1 Design authority

- Read the external Build Manifest first.
- Use `Canon - Home Surfaces` for vocabulary, not current implementation state.
- Use `Places - The Page` and `Trips - The Page` for the composition under
  review.
- Treat `As Built` boards as implementation history.
- Do not implement superseded or exploratory boards as accepted product.
- Preserve Places page-rhythm variant A. Variants B–H remain explorations.
- Source material recipes in `constants/cardSurface.ts` win over inaccurate
  visual approximations in a board.

### 5.2 Product truth

- No plausible stub may look live.
- Empty, unavailable, degraded, stale, and offline are distinct states.
- Places never mutates an itinerary directly.
- A private constraint never enters group-visible copy or projection data.
- Proposal, itinerary, booking, and expense writes remain on their canonical
  ledgered paths.
- Component presence is not the same as production reachability or acceptance.

### 5.3 Completion language

Static tests, mock walks, backend-real canaries, and physical-device evidence
are separate layers. No family is “accepted,” “complete,” or “certified” until
the exact claimed layer has an immutable receipt.

## 6. Target architecture

### 6.1 Trips

```text
route
  -> controller/orchestration
    -> exact server/query snapshots
      -> pure presentation model
        -> physical page plan
          -> exhaustive body render plan
            -> leaf renderer
```

The page plan owns membership, order, state, action/passivity, identity,
containment, and adjacency rhythm. A leaf must not silently return `null` after
the plan has allocated a section. Runtime resource failures, such as a map image
failure, return to the page plan as typed availability.

### 6.2 Places

```text
server producers and ranking
  -> generated PlacesFeed
    -> strict renderability projection
      -> presentation model
        -> responsive render plan
          -> section/exposure executor
            -> exhaustive card-family renderer
```

The client never introduces a second semantic order, promotes attrition into
conviction, or interprets a wide payload as a component/style instruction.

### 6.3 Shared infrastructure

Trips and Places may share:

- semantic text primitives;
- containment/material vocabulary;
- viewport/exposure infrastructure;
- evidence receipts and state vocabulary.

They must not share one page engine. Trips is an authored physical sequence;
Places is a server-produced feed.

## 7. Engineering roadmap

### Phase 0 — reconcile baseline and inventory

Work:

1. Wait for concurrent consolidation/cleanup to leave clean child branches.
2. Re-run frontend, backend, generated-contract, and governance baselines on one
   immutable revision.
3. Split mixed inventory rows:
   - Now/Countdown versus temporal strip;
   - current editorial reading versus new reading registers;
   - Today Mapped versus expanded maps;
   - current Trip Feel question versus persistence/resumption.
4. Record the current producer, contract, renderer, action, and reachability for
   every independently adoptable composition.
5. Add HS-P1/P2/P3 findings to the active ledger.
6. Retain `F/B/V=not_verified` until real receipts exist.

Exit:

- clean repositories;
- current generated contracts;
- one inventory row per independently adoptable composition;
- exact baseline commands and results recorded.

### Phase 1 — state and data honesty

#### Package TR-HONEST-1 — backend degradation

Recommended compatibility-safe implementation:

- Add an internal/excluded delivery-state marker to `ConciergeHomeFeed`.
- Mark `degraded_home_feed()` explicitly.
- Keep Concierge Home's quiet 200 response.
- Make `/trips-stack` return a retryable service failure when its source feed is
  degraded instead of projecting `empty`.

This reuses the existing frontend projection-error fallback and avoids adding a
new public projection enum that old clients may mishandle.

Tests:

- main Home fallback remains usable;
- Trips Stack does not return `empty` after assembly failure;
- promotion reads do not convert the failure into ranked truth;
- endpoint error remains authorization-safe and contains no exception detail.

#### Package TR-HONEST-2 — offline and ambient identity

- Add rounded precipitation and wind inputs to `homeFeedKeyParams`.
- Model cached trip list, cached ranked projection, and placeholder projection
  separately.
- Use TanStack's `isPlaceholderData` as a presentation input.
- Preserve non-location content while clearly marking refresh.
- Suppress location-sensitive modules from a previous key.
- If the placeholder crown is weather/Near You-derived, render the explicit
  unranked fallback until the exact projection arrives.
- Render offline-unranked trips when committed trips exist but the stack does
  not.

Required matrix:

| Network/query state | Expected result |
|---|---|
| Offline + cached projection | Cached ranked content + offline notice |
| Offline + committed trips only | Unranked trips + offline notice |
| Offline cold | Offline empty/error posture with retry |
| Ambient re-key + ordinary crown | Clearly stale/refreshing content |
| Ambient re-key + ambient crown | Ambient crown/module withheld |
| Refresh error + ranked cache | Cached content + one stale notice |

#### Package PL-HONEST-1 — Places availability

- Permit a feed-backed presentation model to classify `unavailable`.
- Derive availability from both unavailable producers and renderable section
  count.
- When nothing is renderable and any producer is unavailable, show one honest
  unavailable/retry state.
- Introduce a pure notice-precedence adapter:
  `offline > failed refresh with cache > partial producer failure`.
- Never render two state banners for one snapshot.

Phase 1 parallelism:

- backend degradation owner;
- Trips query/state owner;
- Places presentation/state owner.

The Trips and Places root hot files remain single-owner within their lanes.

### Phase 2 — actions, gates, cache, and telemetry

#### Package TR-GATES-1

- Gate Day Map membership with `TRIP_EDITORIAL_MAP_ENABLED`.
- Disable the editorial-map query while the gate is dark.
- Disable the trip-home/Ambient query while `AMBIENT_ENABLED` is dark, unless a
  separate visible consumer is explicitly introduced.
- Derive Standing Ask membership and copy from authoritative projection posture.
- Make the loading “See all” affordance a real accessible action or remove its
  door styling.

Hot-file lock: one owner for `TripsHomeController.ts`,
`tripsHomePageComposition.ts`, and `TripsHomeBody.tsx`.

#### Package TR-CACHE-1

- Subtract resolved proposals from `queue`, `rows`, and crown.
- Add mixed current/legacy projection fixtures.
- Preserve authoritative refetch while ensuring stale actionable UI disappears
  immediately.

#### Package TR-TELEMETRY-1

- Build aggregate queue content identity from stable item content IDs.
- Keep content revision as a separate stable hash of IDs and revisions.
- Specify whether an aggregate impression means the queue frame was visible or
  each individual row was visible.
- Do not add a backend fatigue consumer until that semantic decision is explicit.

#### Package PL-ACTIONS-1

- Replace door fallthrough with an exhaustive generated-union switch.
- Decide whether `guide` maps to the existing reading collection or is removed
  from the currently unproduced contract.
- Assert exhaustiveness in tests; remove invalid legacy `map` fixture values.
- Separate candidate navigation labeling from save verb labeling.

### Phase 3 — polish the adopted baseline

Do not redesign the whole page rhythm in this phase.

#### Package PL-POLISH-1

- Keep Places loading standfirst geometry without visibly typing transport
  status as authored voice.
- Retain transport copy in the progress accessibility label.
- Render full-width editorial supporting previews in the approved bounded Roman
  serif role; keep compact forks within their measured content envelope.
- Exercise the longest title/meta/kicker/reason/action candidate at 320, 360,
  and 393pt, normal and approximately 1.35 font scale.
- Review candidate copy height against the fixed 92pt plate.

#### Package TR-POLISH-1

- Add plan-owned separation between Local Plans and Day Map.
- Feed map image availability back into the body render plan so a failed image
  removes the section and its rhythm together.
- Verify Crown -> Conditions -> Group -> queue adjacency with long real copy.
- Verify footer and floating-create clearance above both tab implementations.

#### Blocked package PL-LEAD-1

Do not style `lead=true` as a singular winner. The current gap producer assigns
it to both alternatives to mean equal complete treatment. If product adopts a
lead/peer hierarchy, add a new explicit server-owned semantic such as
`presentation_role: lead | peer`; do not reinterpret the existing boolean.

### Phase 4 — architecture headroom

Correctness and bounded visual changes land before these behavior-preserving
extractions.

#### Places extraction

Split `PlacesWorkspace` into:

- query/context/location controller hook;
- pure root-state presentation adapter;
- search-door composition;
- notice/state frame;
- existing feed executor.

Delete or formally retire the test-only legacy `utils/placesWorkspace.ts`.
Ratchet file sizes only after the extraction passes characterization tests.

#### Trips extraction

Extract from the controller:

- ambient/editorial-map/reading ancillary queries;
- stable action/navigation adapters;
- local resource-availability state;
- telemetry adapters.

Extract from the body:

- phase renderers that own no state discovery;
- typed cluster renderers;
- runtime unavailable-to-plan reconciliation.

Target at least 20% headroom below root/controller ratchets before adding a new
family. Line count is not the architecture goal; singular responsibility and
stable ownership are.

### Phase 5 — product decision packet

Resolve the unresolved inventory in six packets:

1. Places registers, lead/peer semantics, doors, comparison/stack/stub.
2. Places root maps, return, friend/co-sign, and personal record.
3. Trips Near You, temporal strip, and Your People.
4. Trips evidence/decision, draft shelf, Local Plans extensions, hosting,
   pretrip, and return.
5. Today Mapped versus expanded map concepts.
6. Trip Feel persistence, resumption, reduced, and contrast states.

Every decision records:

- adopted, exploratory, deferred, rejected, or relocated;
- evidence required to render honestly;
- producer and schema owner;
- destination or canonical mutation owner;
- privacy/audience classification;
- next review date.

Recommended near-term rulings:

- Adopt the existing Places count door independently from speculative quiet
  panel variants.
- Adopt existing Now and Countdown independently from the missing temporal
  strip.
- Decide whether Today Mapped is production, internal dogfood, or dark.
- Decide Trip Feel persistence before adding more tile states.
- Defer saved-unvisited, raised return, conviction, and reachable cluster until
  their missing signals exist.

### Phase 6 — new vertical slices

Only begin after the adopted baseline has backend-real and device evidence.

Recommended order:

1. Today Mapped, because most producer/contract/renderer/action plumbing exists.
2. One deliberately adopted Places reading register using existing dossier
   identity and a real reader destination.
3. Trip Feel persistence/resumption, if adopted.
4. A dedicated Near You receipt and composition.
5. Return or personal-record families only after their signals and destinations
   exist.

Continue to defer:

- visit-dependent saved-unvisited and raised return;
- non-proximity conviction;
- reachable cluster;
- hosting;
- co-sign, Again, belonging, tally, and rhythm;
- expanded multi-person maps.

### Phase 7 — backend-real and device acceptance

#### Backend-real matrix

- Trips source degradation.
- Ambient weather re-ranking.
- Offline/cached stack behavior.
- Fully unavailable and partially unavailable Places feed.
- Proposal resolution removing queue content.
- Private reasoning and friend-sharing boundaries.
- Day Map membership, authorization, and no-data behavior.
- Canonical mutation destinations and durable receipts.

#### Device matrix

- iOS and Android.
- 320/360/393-equivalent widths.
- Normal and large Dynamic Type.
- Loading, empty, partial, stale, offline-cached, offline-cold, and error.
- Map image failure and permission denial.
- Background/foreground exposure dwell.
- Long and short canonical pages.
- Bottom navigation and floating affordance clearance.

Every accepted inventory row receives separate F/B/V receipts with the design
hash, fixture or backend state, platform, width, font scale, date, and reviewer.

## 8. Parallel dispatch model

Use at most three implementation workers plus one integration coordinator.

| Wave | Worker A | Worker B | Worker C | Serialized handoff |
|---|---|---|---|---|
| 0 | Frontend baseline | Backend baseline | Inventory/governance | Coordinator records exact SHAs |
| 1 | Backend degradation | Trips state/query | Places availability | Cross-repo behavior gate |
| 2 | Trips root/gates | Cache/telemetry utilities | Places actions | Root hot-file integration |
| 3 | Trips polish | Places polish | Responsive/state fixtures | Visual characterization |
| 4 | Trips extraction | Places extraction | QA/evidence harness | Architecture and budget gate |
| 6+ | One backend/schema family | One Trips or Places frontend family | QA/canary | Schema sync then vertical integration |

### Hot-file locks

The following files may have only one owner in a wave:

- `components/trips/TripsHomeController.ts`
- `components/trips/TripsHomeBody.tsx`
- `utils/tripsHomePageComposition.ts`
- `components/places/PlacesWorkspace.tsx`
- `components/places/PlacesSectionFeed.tsx`
- `utils/placesPresentationModel.ts`
- workspace OpenAPI snapshots and generated frontend schema

Workers stage explicit filenames only and report:

- base SHA;
- touched paths;
- tests and exact results;
- compatibility statement;
- evidence receipts created;
- known remaining risks.

## 9. Validation gates

### 9.1 Frontend static/mock

Focused suites include:

- `homeSurfaceStateMatrix.test.ts`
- `tripsHomePresentationModel.test.ts`
- `tripsHomePageComposition.test.ts`
- `tripsHomePageSectionPlan.test.ts`
- `tripsHomeBodyRenderPlan.test.ts`
- `invalidateHomeProjections.test.ts`
- `placesPresentationModel.test.ts`
- `PlacesWorkspaceState.test.tsx`
- `PlacesWorkspaceLoading.test.tsx`
- `PlacesSectionFeed.test.tsx`
- `placesWorkspaceFeedNavigation.test.ts`

Repository gates:

```bash
npm run typecheck
npm run test:typecheck:contracts
npm run api-boundaries
npm run home-surface-budgets
npm run verify:fast
npm test -- --ci --runInBand --no-cache
HOME_SURFACES_CANON_DIR=/absolute/path/to/vesper-home-surfaces \
  npm run qa:design:check -- places-workspace
HOME_SURFACES_CANON_DIR=/absolute/path/to/vesper-home-surfaces \
  npm run qa:design:check -- trips-home
```

### 9.2 Backend

Focused suites include:

- `tests/api/test_concierge_home.py`
- `tests/home/test_trips_stack_projection.py`
- `tests/home/test_trips_stack_projection_identity.py`
- `tests/places/test_feed_orchestration.py`
- `tests/places/test_sections_contract.py`
- `tests/places/test_supporting_copy.py`

Then run the complete relevant offline and Postgres-backed gates with the
repository virtual environment, plus Ruff and formatting checks.

### 9.3 Cross-repo contract

For every backend schema or route change:

1. Change backend source and tests.
2. Run the workspace type-sync workflow.
3. Review `docs/openapi.json`.
4. Review `docs/openapi.app.json`.
5. Review `travel-app/utils/api/schema.gen.ts`.
6. Fix frontend type and behavior fallout.
7. Deploy additive backend compatibility before client reliance.

The recommended Trips degradation solution avoids a new public enum and may not
require generated-type changes, but the contract check still runs.

### 9.4 Evidence

```bash
npm run qa:polish:scenarios
npm run qa:surface -- trips-home --after
npm run qa:surface -- places-workspace --after
```

A dry run proves only the harness. It is not visual or device evidence.

## 10. Commit and merge boundaries

Recommended narrow commits:

1. Backend degraded-source truth.
2. Trips offline/placeholder/query identity.
3. Places unavailable state and notice precedence.
4. Trips feature gates and dark-query suppression.
5. Proposal queue reconciliation.
6. Trips exposure identity.
7. Places exhaustive door routing and accessibility semantics.
8. Places loading and typography polish.
9. Trips Local Plans/Day Map rhythm and runtime failure handling.
10. Places root extraction.
11. Trips controller/body extraction.
12. Inventory and evidence receipts.

Do not mix:

- schema generation with unrelated UI work;
- route centralization with visual layout changes;
- architecture extraction with behavior fixes;
- design-adoption decisions with implementation commits;
- evidence-only changes with source behavior.

## 11. Definition of success

The immediate program—Phases 0 through 3—succeeds when:

- no backend failure appears as authoritative empty truth;
- offline, placeholder, stale, partial, unavailable, and empty states are
  distinct and covered;
- dark features do not fetch or incur model work;
- actions and doors are exhaustive, accessible, and owned by their canonical
  destination;
- current adopted card typography and rhythm match the August direction at
  representative widths and text scales;
- focused and broad automated gates are green on one immutable revision;
- the inventory accurately separates implemented, unresolved, gated, and
  signal-blocked work.

The broader program succeeds only when adopted families also have backend-real
and physical-device receipts. Another component existing in the source tree is
not a completion criterion.

## 12. Execution record — 2026-08-10

This record distinguishes source-layer implementation from acceptance. It is
intentionally not an F/B/V receipt.

### Landed implementation packages

| Package | Result | Commits |
|---|---|---|
| Places root truth | One pure selector now chooses cold offline, error, loading, unavailable, empty, and feed states from request/cache/renderability/availability truth. Zero-renderable unavailable and offline snapshots no longer mount a dishonest empty feed. | App `1615f7b7` |
| Trips posture and queue semantics | Standing Ask now derives from normalized projection posture; loading no longer impersonates an action; aggregate queue identity is durable across copy-only revisions. | App `e856761b`, `008ff522` |
| Places typography and loading voice | The visual loading floor remains authored while transport detail is accessibility-only. Full-width editorial preview copy uses the bounded semantic serif role. | App `b934cfee` |
| Trips Local Plans / Day Map rhythm | Failed map leaves suppress themselves before cluster layout and Local Plans/Day Map have an explicit internal gap. | App `2e65b2e8` |
| Root consolidation | Places state/search responsibilities moved into focused components; Trips actions and settled performance effects moved out of the controller. | App `b06571a2`, `a8230c3e`, `d9ea207b` |
| Governance | Inventory rows are independently adoptable: Time and Trip Feel are split, and technical source completion is not confused with adoption or acceptance. | Workspace `f7427f7`, `929a538` |
| Projection resilience | A failed supplemental Trips posture read no longer discards an otherwise grounded ranked home projection. | Backend `08adf7a67` |
| Private Places prompt routing | Malformed cached prompt payloads are inert unless they carry the private trip-debrief continuation; they cannot navigate into booking or proposal owners. | App `0b8ecfeb` |
| Trips fixture and QA parity | Cardless mock Trips uses the backend-equivalent starter crown; active capture expectations no longer require the retired cold-invitation UI. | App `99178d57` |
| Cross-repo guard coherence | The identity contract guard recognizes the already-published `transport_hub` reference type. | Workspace `6f603bd` |

### Verification on the settled source tree

- Frontend focused regression suites, typecheck, home-surface budgets, and
  `verify:fast` pass. The latter finished with lint warnings but no errors.
- Backend `tests/home` plus `tests/places`: **1084 passed, 1 skipped**.
- Generated API contract check passes; Places identity contract remains
  10 kinds × 2 payloads.
- Home-surface governance validation passes for all 36 inventory items;
  external-authority hash checks pass for both current surfaces.

### Acceptance still intentionally open

- The design-ledger inventory remains at `F=not_verified` for all 36 items,
  `B=not_verified` for the 34 applicable items, and `V=not_verified` for all
  36. No backend-real or physical-device receipt was fabricated from unit
  tests or a simulator.
- Both detected physical iPhones are offline. They must be connected before
  the required physical-device matrix can be run.
- The simulator polish runner began with `trips-home` and its cold-invitation
  scenario failed because the expected `trips-home-cold-invitation` test ID was
  not present after launch. This is a capture-harness/app-fixture discrepancy
  to diagnose before screenshot evidence can be trusted; it is not an
  acceptance result.
- The 19 unresolved families and the Trip Feel stateful follow-up remain
  product/adoption decisions, not engineering defects that can safely be
  invented. The lead hierarchy, map expansion/privacy, return registers, and
  notice/prompt relocation remain explicitly blocked by those decisions.

## 13. Source landmarks

### Authority and status

- External `HANDOFF.md`
- External `Build Manifest - Both Surfaces.dc.html`
- External `Places - The Page.dc.html`
- External `Trips - The Page.dc.html`
- `docs/status/home-surfaces-composition-inventory.json`
- `docs/home-surfaces-section-card-ledger-2026-08-09.md`

### Frontend

- `components/trips/TripsHomeController.ts`
- `components/trips/TripsHomeBody.tsx`
- `utils/tripsHomePageComposition.ts`
- `utils/tripsHomePageSectionPlan.ts`
- `utils/homeSurfaceStateMatrix.ts`
- `data/conciergeHome.ts`
- `components/places/PlacesWorkspace.tsx`
- `components/places/PlacesSectionFeed.tsx`
- `utils/placesPresentationModel.ts`
- `utils/placesFeedRenderPlan.ts`

### Backend

- `backend/api/routes/concierge_home.py`
- `backend/home/concierge_feed/fallback.py`
- `backend/home/concierge_feed/models.py`
- `backend/home/trips_stack.py`
- `backend/core/models/places_sections.py`
- `backend/places/`
