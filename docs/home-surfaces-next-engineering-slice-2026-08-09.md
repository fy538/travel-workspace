---
doc_type: working
status: active
owner: founder / engineering
created: 2026-08-09
expires: 2026-09-08
why_new: Defines the next bounded engineering slice after the home-surface correctness and schema consolidation pass.
---

# Home Surfaces — Next Engineering Slice

## Recommendation

Run one **land, shrink, and prove** slice before implementing another proposed
Page-board family.

The current integration work has corrected the main state, contract, exposure,
and producer defects, but it is still a long-lived branch rather than a
releasable trunk state:

- frontend `codex/home-surfaces-app-integration` is 37 commits ahead of and 2
  commits behind `origin/main` by unique history (`53` ahead of local `main`);
- backend `codex/home-surfaces-backend-integration` is 33 commits ahead of and
  20 commits behind `origin/main`;
- the frontend branch changes 128 files relative to local `main`;
- `app/(tabs)/trips/index.tsx` is 1,808 lines, even though its two principal
  functions are now individually below the 800-line function budget;
- `PlacesSectionFeed.tsx` is 2,214 lines, and the new renderer-family modules
  mostly contain pure helpers or markers rather than the visual components;
- `TripsHomeSectionPlan` owns membership and identity, but not yet the full
  render-state, action, containment, and adjacency-rhythm contract described in
  the roadmap;
- 19 of the 33 inventoried compositions remain unresolved, so their visual
  implementation is still a product decision rather than engineering backlog;
- all 13 adopted compositions still lack backend-real and/or device evidence.

The goal of this slice is to produce clean current-main integration branches,
finish the architectural seams, and obtain evidence for the already-adopted
families. It must not turn unresolved frames into product behavior by momentum.

## Slice boundaries

### In scope

- Reconcile the home-surface commits onto current frontend and backend
  `origin/main` without dragging unrelated integration history.
- Finish physical Trips root separation and the Places renderer strangler.
- Promote both pure models to the single page-composition authority for current
  behavior.
- Add whole-page state and adjacency-rhythm matrices.
- Run backend-real and device QA for the currently adopted compositions.
- Produce a decision packet for the first genuinely new family.

### Out of scope until a recorded decision

- Places one-place recommendation/conviction registers.
- General comparison, physical-stack, ticket-stub, postcard, co-sign, personal
  record, “The Rest,” or root-map compositions.
- Trips temporal day pips, Trip Feel resumption, return Story, hosting, expanded
  maps, or Today Mapped release enablement.
- Any new group-visible copy path or parallel proposal/booking/itinerary writer.
- Copying the external canonical design bundle into a repository.

## Phase 0 — Current-main landing lane

**Purpose:** remove branch divergence before more product work obscures merge
conflicts.

1. Create new clean integration worktrees from current `origin/main`:
   `codex/home-surfaces-app-next` and `codex/home-surfaces-backend-next`.
2. Generate a commit manifest with `git range-diff`; classify every unique
   commit as home-surface, already-equivalent upstream, or unrelated.
3. Replay only the home-surface commits. Do not merge the old integration
   branches wholesale.
4. Resolve frontend overlap with the canonical Trip query-cache changes in
   `f322f09c`; the current branch predates that authority change.
5. Resolve backend overlap with the newer home boundary/request-clock
   refactors (`eb108834`, `c3270845`) semantically rather than retaining old
   file structure through conflict resolution.
6. Land backend models/producers first, run one schema train, then land the
   frontend consumers.
7. Re-run the six full-suite failures after reconciliation. Fix only failures
   reproducible on the new branch; do not absorb unrelated work merely to make
   a branch-local number green.

### Phase 0 parallel dispatch

| Owner | Work | Exclusive files/artifacts |
|---|---|---|
| Frontend reconciliation agent | Range-diff and replay home frontend commits; resolve current-main parity | Frontend integration worktree; no generated schema edits |
| Backend reconciliation agent | Range-diff and replay home backend commits; adapt to upstream home boundaries | Backend integration worktree; no workspace snapshots |
| Coordinator | Commit classification, conflict review, schema train, workspace policy/inventory | `docs/openapi*.json`, generated frontend schema, governance docs |

### Phase 0 exit

- Both new integration branches are clean and based on current `origin/main`.
- No unrelated commit is carried solely because it existed below the old home
  commit range.
- Contract projection, generated schema check, frontend typechecks, API
  boundaries, state ownership, and focused home suites pass.
- Remaining repository-wide failures are reproduced and classified against the
  same current-main base.

## Phase 1 — Finish the strangler architecture

This phase is behavior-preserving and may run in three parallel lanes after
Phase 0 lands.

### NS-TR-A — Physical Trips separation

- Reduce `app/(tabs)/trips/index.tsx` to a route/composition boundary.
- Move `useTripsHomeScreenController`, body rendering, and styles into named
  modules with explicit typed inputs.
- Keep the controller and body independently below the 800-line function
  budget and avoid a single giant props bag that duplicates the model.
- Preserve canonical destinations and proposal resolution; introduce no new
  writer.

### NS-PL-A — Complete the Places renderer strangler

- Move the real visual components and their styles from
  `PlacesSectionFeed.tsx` into the existing `candidate`, `editorial`,
  `experience`, `memory`, `social`, and `noticePrompt` family modules.
- Leave the feed responsible only for backend-ordered iteration, section
  framing, exposure boundaries, responsive arrangement selection, and
  exhaustive family dispatch.
- Each family receives a narrow typed render context rather than the entire
  workspace controller.
- Move tests with each family and delete the original implementation in the
  same commit.

### NS-QA-A — Deterministic architecture characterization

- Add import-boundary and render-parity tests in new test files.
- Freeze the current minimal, ordinary, and maximal page fixtures before the
  physical moves.
- Add a local home-surface size report so these two files cannot silently grow
  back even while broader repository size debt remains.

### Phase 1 hot-file rule

Only NS-TR-A edits the Trips root. Only NS-PL-A edits
`PlacesSectionFeed.tsx`. NS-QA-A may add tests and tooling but may not edit
either hot file. Leaf-family parallelism begins only after NS-PL-A freezes the
render-context interfaces.

### Phase 1 exit

- Trips route file is a small boundary; orchestration, body, and styles have
  named ownership.
- Places feed contains no leaf card implementation or family-specific style
  sheet.
- Generated card-kind exhaustiveness still fails compilation for an unmapped
  kind.
- No home-surface function exceeds 800 lines and local file-size ratchets are
  lower than this slice's starting measurements.
- Focused screenshots show no intentional visual delta; this is regression
  evidence, not design acceptance.

## Phase 2 — Complete the page-composition authorities

### NS-TR-P — Trips composition plan v2

Extend the pure plan so every current section entry carries:

- render state (`ready`, `empty`, `unavailable`, or `dark`);
- stable section, content, and revision identity;
- typed destination/action identity or explicit passivity;
- containment and adjacency-rhythm role;
- grounding summary and rejection reason.

The root must render and instrument only plan entries. Side inputs such as
weather and roster data must join through one typed module view model with an
explicit unavailable state; independently refreshed data may not silently
change the trip or locality represented by a module.

### NS-PL-P — Places feed presentation v2

Extend `PlacesPresentationModel` so each backend-ordered section carries:

- resolved family and current treatment;
- render state and partial-producer context;
- content revision/exposure identity;
- door/action identity or explicit passivity;
- containment and adjacency-rhythm role.

This remains an adapter over the generated transport contract. It must not add
new server semantic registers or infer unsupported arrangements.

### NS-MATRIX — Whole-page state matrices

Add pure fixture matrices for:

- Trips: pending, valid empty, degraded ranked, ordinary ranked, urgent, live,
  returned, dark capability, and unavailable side input;
- Places: initial, fresh, refresh-cached, offline-cached, error-empty, partial
  feed, search empty/results, and starter/quiet/full postures;
- widths 320/360/393 and normal/~1.35 font scale for representative page
  compositions.

### Phase 2 exit

- Page membership, existence, telemetry identity, and rhythm all consume the
  same pure plan/model.
- A child renderer cannot return `null` after the page has allocated a gap; an
  invalid payload becomes an observable rejected/unavailable entry before
  layout.
- Places and Trips have no second client-side ranking path.
- The state matrices pass in mock mode and against backend-shaped fixtures.

## Phase 3 — Prove the adopted baseline on real surfaces

Do not introduce a new family in this phase. Review the existing adopted set:

- Places: candidate rows, experience rail, editorial reading, anniversary
  memory, and passive friend strip.
- Trips: crown, room/group, Connect/trail, Conditions, Also in Play, Local
  Plans, Companion, and page voice.

### Backend-real gate

- Run with the committed Postgres schema, including the projection-outbox
  migration that previously blocked one Places test.
- Verify producer `available`/`empty`/`unavailable` behavior and Trips module
  coherence from real API responses.
- Trace group-room visibility and copy for authorization/privacy; private member
  constraints must not enter the shared destination or visible text.
- Confirm all proposal/plan actions route to their canonical writer and produce
  the owning surface's receipt.

### Device/design gate

- Verify the external canonical bundle by hash; do not copy it into the repo.
- Capture Trips and Places at 320/360/393-equivalent widths, normal and large
  Dynamic Type, long/short pages, partial/offline states, header occlusion, and
  background/foreground dwell transitions.
- Run both iOS and Android because system sans metrics and mono legibility
  differ.
- Correct the known Places memory typography-role misuse during this phase.
- Attach immutable backend/device receipts to the composition inventory.

### Phase 3 exit language

Static, mock, backend-real, and device status are recorded separately. No
family is called accepted unless the named platform, width, state, design hash,
and receipt are present.

## Phase 4 — Select the first genuinely new family

Present the Phase 3 evidence with a short founder decision packet. The packet
must resolve the affected inventory item before implementation begins.

### Recommended Trips candidate

`TR-F01a`: coherent Now/Conditions/Group modules plus the existing simple
countdown. Keep the temporal strip and itinerary-day pips absent unless a
canonical day receipt is adopted. This exercises the typed module architecture
without inventing calendar truth.

### Recommended Places candidate

`PL-F03a`: a restrained reading spine backed by existing guide/dossier identity
and a real reader destination. Keep lens switchers, quote extracts, and overlays
absent until lens naming and attributable-extract contracts are adopted.

Do **not** choose lead-plus-siblings as the first new Places slice without a
contract correction. Today `lead=true` is emitted only by the gap producer and
is set on every alternative to mean equal full treatment, not “one ranked lead.”
Giving that bit a singular visual hierarchy would contradict its current
backend semantics.

## Validation commands

### Frontend static/mock

```bash
npm run typecheck
npm run test:typecheck:contracts
npm run api-boundaries
npm run state-ownership
npm run size-budgets
npm run containment-budget
npm run spacing-budget
npm run typography-budget
npm run typography-role-usage
npm run typography-roman-only
HOME_SURFACES_CANON_DIR=/Users/feihuyan/Downloads/vesper-home-surfaces npm run qa:design:check
```

Run focused Trips/Places suites after every package, then run the full Jest
suite on the reconciled branch. A pre-existing failure is evidence to classify,
not permission to hide a new one.

### Cross-repo and backend

```bash
make contract-check
make typecheck
make test-backend
```

Add focused backend-real Postgres canaries for the exact producer/module states
claimed by the slice.

### Device

```bash
npm run qa:surface -- trips-home --after
npm run qa:surface -- places-workspace --after
```

Use the structured verdict and evidence-receipt workflow. A dry run proves only
the harness path.

## Commit and merge boundaries

1. Frontend reconciliation manifest and replay.
2. Backend reconciliation manifest and replay.
3. One coordinated schema-train commit in workspace and frontend.
4. Trips physical extraction.
5. Places family extraction, one family per commit after interfaces freeze.
6. Trips plan v2.
7. Places presentation v2.
8. Whole-page state/rhythm fixtures.
9. Backend-real fixes and receipts.
10. Device-only evidence and inventory update.

Every commit stages explicit filenames. Each phase updates the inventory in the
same integration batch that changes evidence status. Compatibility code is
removed only after backend deployment, minimum-client, and device gates prove
that supported clients no longer need it.

## Definition of success for this slice

This slice succeeds when the current adopted home surfaces are represented on
current main by small owned modules, one composition authority per page, green
touched-surface gates, current generated contracts, and honest backend/device
evidence. It does not succeed merely because another card component exists.
