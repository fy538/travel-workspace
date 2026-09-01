---
doc_type: working
status: active
owner: founder / product / architecture / engineering
created: 2026-09-01
last_verified: 2026-09-01
expires: 2026-10-01
why_new: Turns the accepted Life v1 contract and the current three-task convergence state into an execution-grade, collision-safe program with exact packages, commit units, gates, and stop lines.
depends_on:
  - ../contracts/life-v1-experience.md
  - ../decisions/2026-09-01-adopt-life-v1-behavior-sequences.md
  - life-v1-engineering-transformation-sequence-2026-09-01.md
  - home-and-places-root-implementation-status-2026-09-01.md
  - ../systems/four-root-loop-object-surface.md
  - ../systems/contribution-and-consequence.md
---

# Life v1 — non-regrettable engineering execution plan

## 1. Objective

Build the durable seams needed by the accepted Life experience without
prematurely freezing its complete renderer, expanding the ontology, or
duplicating work active in Home/Places and Artifacts.

The execution target is:

```text
accepted Life canon
→ tested native primitives
→ generated contract integrity
→ one canonical object-handle seam
→ pure Life read projection
→ shared cross-root arbitration
→ flagged Time root
→ canonical destinations and refinding
```

This plan does **not** authorize Together persistence, generalized Occasion
architecture, a universal artifact renderer, every Life lens, or legacy Atlas
removal.

## 2. Current task ownership and dependency gates

### Strategy task — active owner

Owns the Home/Places v2 projection contracts, producer policy, root operation
registry, generated app contract, Home renderer, and root-v2 cache/navigation
seams. Its current turn is adding server-authored Home posture, week shape, and
read scale.

**Do not touch while active:**

- `travel-agent/backend/core/models/root_projection_v2.py`
- `travel-agent/backend/root_projection/v2/**`
- Home/Places v2 routes
- generated root-v2 schema in its app worktree
- Home root renderer/composition policy
- Home/Places operation-policy entries

### Artifacts task — reviewed, not mergeable yet

The fixture-only conformance ratchet has a sound goal but currently admits
semantic false positives: missing non-silence return context, ownerless
receipts, foreign active instruments, duplicate portfolio substitution,
root-as-owner language, and incorrect receipt command identity.

**Dependency rule:** Life does not import, promote, or conform production code
to this branch until every P1 is corrected and the review is rerun. Life may
continue using the accepted canonical artifact doctrine.

### Life task — owner of this plan

Owns the Life contract, behavior rulings, production composition, refinding
behavior, Life-native primitives, future Life read projection, canonical Life
destinations, and Life's participation in cross-root arbitration.

## 3. Branch and worktree strategy

Wait for the active Strategy turn to finish. Record its final app and backend
heads; never invent or assume the base commit.

Then create isolated Life worktrees:

```bash
git -C travel-app worktree add \
  worktrees/life-foundation-app \
  -b codex/life-native-foundation \
  <landed-strategy-app-head>

git -C travel-agent worktree add \
  worktrees/life-root-agent \
  -b codex/life-root-projection \
  <landed-strategy-backend-head>
```

If Strategy has not yet been merged into the child repositories, use the clean
heads of its two worktrees as bases and document that relationship. Do not
modify those worktrees directly.

The seven uncommitted primitives in the main `travel-app` checkout are source
material. Recreate them in the Life worktree with an explicit patch and leave
the original checkout untouched until the Life commit is verified. Do not use
`git add .` or `git add -A` anywhere.

The parent workspace remains on its current coordination branch. Stage only
the explicitly named Life documents when committing canon.

## 4. Package L0 — land authority and design evidence

### Purpose

Make the accepted Life product decisions durable before implementation begins.

### Parent-repository commit

Stage explicitly:

- `docs/contracts/life-v1-experience.md`
- `docs/decisions/2026-09-01-adopt-life-v1-behavior-sequences.md`
- `docs/decisions/2026-08-30-adopt-life-consumer-anatomy.md`
- `docs/working/life-v1-engineering-transformation-sequence-2026-09-01.md`
- this execution plan
- the accepted arbitration policy and Life production spec amendments
- the narrow `docs/systems/README.md` link amendment

Do not sweep unrelated August research documents into this commit.

### App design authority

Before strict native visual QA, promote the single accepted production
composition from the external `vesper-life-anchors` project into a repo-tracked
Life root design reference. Preserve the external project as evidence; do not
copy all sixty boards.

Create or update:

- `travel-app/docs/surfaces/life-root/contract.md` — thin app-facing pointer to
  the workspace Life contract, not a restatement.
- `travel-app/docs/surfaces/life-root/design-refs/` — one exported rich-Time
  reference plus manifest.
- surface registry entry for `life-root` only when a flagged native route
  exists; until then classify the design reference as planned, not evidenced.

### Verification

```bash
git diff --check -- <explicit files>
npm run docs:check
```

### Exit

The product authority, build plan, and one production composition are
repo-addressable. No product code changes.

## 5. Package L1 — stabilize the Life-native primitive foundation

### Scope

Bring the seven accepted primitives into the isolated app worktree:

- `components/ui/AnchorKindMark.tsx`
- `components/ui/LifeAnchorRow.tsx`
- `components/ui/LifeEpisodeGroup.tsx`
- `components/ui/LifeEpisodeRow.tsx`
- `components/ui/LifeKeepsake.tsx`
- `components/ui/LifeScrollDoor.tsx`
- `components/ui/LifeSectionBar.tsx`

Update the component catalog files explicitly.

### Corrections before commit

- Audit every `numberOfLines={1}` against Dynamic Type. Identity and truthful
  count must not disappear merely to preserve a mockup's height.
- Decorative SVG marks must not create redundant screen-reader stops.
- Interactive rows and doors need one complete accessibility label, a button
  role, and a reliable minimum touch target.
- A group renders at most one door. A partial label/action pair renders no
  misleading affordance.
- Optional stamp/window metadata must never become the only expression of
  state.
- No component imports a Life API payload or embeds a route.

### Tests

Add focused tests under `__tests__/components/ui/` for:

- expanded versus collapsed entry behavior;
- disclosure and collapse labels;
- scroll-door label plus honest count;
- open versus held mark treatment without using color as the only cue;
- optional keepsake interactivity;
- multi-line and large-text survival;
- absence of a door when either half of its contract is missing.

Prefer behavioral assertions over broad snapshots.

### Verification

```bash
npx eslint components/ui/AnchorKindMark.tsx \
  components/ui/LifeAnchorRow.tsx \
  components/ui/LifeEpisodeGroup.tsx \
  components/ui/LifeEpisodeRow.tsx \
  components/ui/LifeKeepsake.tsx \
  components/ui/LifeScrollDoor.tsx \
  components/ui/LifeSectionBar.tsx
npm test -- --runInBand __tests__/components/ui/Life*.test.tsx
npm run typecheck
npm run components:check
npm run accessibility-governance
```

If `components:check` still fails on `MediaPlate`, `RestClose`, or
`RouteStrip`, confirm whether Strategy's landed app head owns their registry
entries. Do not silently absorb those files into the Life commit.

### Commit

`feat(life): stabilize native continuity primitives`

### Exit

Seven tested, registered, route-free primitives. No Life screen, no fixture
payload, and no visual-promotion claim.

## 6. Package L2 — close the Life API contract lane

### Prerequisite

Strategy's root-v2 OpenAPI and operation-registry work is landed or otherwise
available in the chosen base. The parent `make contract-check` must no longer
fail from stale/missing Home/Places consumers.

### Work

1. Run the complete snapshot and app projection workflow.
2. Confirm `POST /api/life/refind` and `LifeRefindResultV1` appear in
   `docs/openapi.app.json` and generated `schema.gen.ts`.
3. Replace every import from `types/lifeRefind.ts` with generated component
   types or a thin alias module composed entirely from generated types.
4. Delete the handwritten mirror.
5. Preserve the ergonomic presentation helpers; only their type source changes.
6. Re-run the mock and hook contracts against generated request/response names.

### Likely app files

- `utils/api/schema.gen.ts` — generated only
- `utils/api/http.ts`
- `utils/api/interface.ts`
- `utils/api/mock/discover.ts`
- `hooks/useLifeRefind.ts`
- `utils/lifeRefindPresentation.ts`
- `components/search/LifeRefindLane.tsx`
- existing Life refind tests
- delete `types/lifeRefind.ts`

### Verification

```bash
make contract-check
make sync-types-snapshot
npm run generate-api-types:check
npm run schema-bridge
npm run api-boundaries
npm test -- --runInBand \
  __tests__/components/LifeRefindLane.test.tsx \
  __tests__/utils/lifeRefindPresentation.test.ts
npm run typecheck
```

### Commits

- Parent: `chore(api): project Life refind into the mobile contract`
- App: `refactor(life): consume generated refind types`

### Exit

No handwritten Life API mirror and no Life-specific schema drift.

## 7. Package L3 — canonical object handle and destination seam

### Purpose

Make “the same object opens everywhere” executable before building the Life
root or dossiers.

### Contract

Backend `ResourceRef` remains canonical:

```text
kind + id + revision + canonical_path
```

The app may derive a native destination from that handle, but semantic payloads
must not name React components or arbitrary navigation instructions.

### App work

Create a small resolver with a closed output union such as:

```text
supported native owner
supported guide deep link
truthful source fallback
unsupported
```

Requirements:

- allowlist canonical app path families;
- parse, never concatenate, external payload paths;
- preserve revision and selected substate where supported;
- return `unsupported` instead of guessing a legacy destination;
- carry the original `ResourceRef` into Chat continuation context;
- no navigation side effect inside the resolver.

### Tests

- journey, trip, place, source, and guide handles;
- malformed/unknown path;
- unsupported but truthful fallback;
- same handle from Home, Places, and Life produces the same owner destination;
- revision survives resolution;
- no arbitrary URL navigation.

### Commit

`feat(navigation): add canonical resource destination resolver`

### Exit

Root units and search results can share one destination seam, even before every
destination is implemented.

## 8. Package L4 — pure Life root read projection

### Prerequisite

Root-v2 shared identity, authority, degradation, and source-revision seams have
landed. Do not copy the Home/Places compiler or widen its closed kind union
without first extracting an explicitly shared base.

### Backend contract

Add a Life-specific, versioned read projection that is semantic but faithful to
the accepted anatomy:

- viewer and selected lens;
- root state: rich / ordinary / thin / yielded;
- earned speaking read or factual fallback;
- deterministic digest groups and rows with canonical `ResourceRef`s;
- one full-record destination and honest count/span;
- zero to three already-arbitrated record-native Returns;
- zero to two conditional reflections;
- zero to two fixed cross-lens windows;
- Everything-kept destination;
- source revisions, degradations, authority footprint, and projection revision.

It must not contain component names, coordinates, typography, route strings
outside canonical resource handles, or model-authored UI trees.

### Pure fixtures first

Implement four replayable fixtures:

1. **Rich post-return** — the accepted Europe/New York composition.
2. **Ordinary local life** — no travel spectacle and at most one Return.
3. **Thin** — honest digest, no placeholder Return or invitation to add data.
4. **Yielded** — the same evidence has an active Home/Places seat; Life's
   corresponding Return is absent while its dossier handle remains.

Add authority mutations:

- source withdrawn;
- attributed note grant narrowed;
- object corrected;
- count changes after deletion;
- partial owner read.

### Invariants

- four to five digest blocks maximum;
- exactly one full-record door when a history exists;
- zero placeholder/empty modules;
- every visible count reconciles with the fixture corpus;
- every visible entry has one canonical handle;
- windows are deterministic for a stable record revision;
- authority changes invalidate the projection revision;
- user input is never required to complete the root.

### Initial implementation boundary

Pure model + compiler + tests only. No route and no database migration in the
first commit.

### Commits

- `feat(life): define the v1 read projection contract`
- `test(life): characterize rich thin ordinary and yielded roots`

### Exit

A deterministic, renderer-neutral Life payload exists and cannot overclaim
completeness. It remains dark and fixture-driven.

## 9. Package L5 — shared cross-root Return arbitration

### Prerequisite

Use the landed Strategy arbitration substrate. Do not create a Life-only
candidate ranker.

### Work

- Extract only the genuinely root-neutral gate and cluster/seat concepts.
- Add Life as a possible durable/root-native seat without making Life a truth
  owner.
- Keep Home/Places current-delivery priority and Life's yield law explicit.
- Preserve one candidate identity when a material trigger changes its dominant
  job.
- Ensure suppressed candidates are not engagement queues.

### Golden tests

Implement the ten accepted arbitration fixtures from
`life-return-arbitration-policy-2026-09-01.md`, including:

- merge compatible jobs;
- no-trigger silence;
- forecast-triggered job change;
- Home-delivery yield;
- attributed-source withdrawal;
- thin-evidence demotion;
- “do not bring this back” suppression;
- zero duplicate present-delivery seats across roots.

### Commit

`feat(roots): arbitrate one return seat across Home Places and Life`

### Exit

Home, Places, and Life consume one policy decision for overlapping evidence.
No root owns or rewrites canonical truth.

## 10. Package L6 — first flagged native Life root

### Prerequisites

L1–L5 are green. The accepted design reference is repo-tracked. Canonical
destinations exist for every object rendered in the fixture.

### App work

- Add a new default-off internal flag for the Life v1 root.
- Mount a dedicated `LifeRootV1Screen`; do not extend the legacy Atlas screen.
- Implement Time at rest using the generated read projection and L1 primitives.
- Keep all four labeled lenses visible; only Time needs full data coverage in
  this package.
- Implement loading, error, offline, partial, ordinary, thin, rich, and yielded
  states together.
- Use a closed Life unit renderer owned by the app.
- Preserve Atlas as the flag-off compatibility route.

### Explicit exclusions

- no global Life map;
- no hero photography;
- no prompt or input module;
- no infinite scroll or novelty rotation;
- no client-authored Returns;
- no dead-end row;
- no generalized dossier renderer.

### QA

Register `life-root` in the polish-QA surface only when the route is reachable.
Add stable scenario IDs and capture at minimum:

- rich Time at rest;
- thin;
- yielded;
- loading/error/partial;
- large text;
- VoiceOver traversal.

Run the app/design comparison against the promoted production composition.

### Commits

- `feat(life): add the flagged v1 root shell`
- `feat(life): render Time from the Life projection`
- `test(life): certify root states and accessibility`

### Exit

A truthful internal Life root runs from a generated backend contract. It is not
yet promoted for public release.

## 11. Package L7 — destinations and navigable refinding

Build only the destinations required by the Time fixture and refinding
benchmark:

1. journey/episode dossier;
2. place-relationship dossier or truthful existing owner page;
3. thread dossier;
4. viewer-relative shared-record dossier;
5. Everything kept custody view.

Every destination must show canonical identity, containment, plan-versus-
occurrence truth, sources/claims, current authority, and a context-preserving
Chat door. Unsupported object kinds degrade to a truthful source/object view.

Only after these destinations exist should `LifeRefindLane` rows become
navigable. “Around this” remains session-local and search remains no-write.

### Exit

All deterministic refinding benchmark targets open a canonical destination or
an explicit truthful fallback. No result ends in legacy Atlas by accident.

## 12. Deferred packages

Do not begin until L0–L7 produce device evidence:

- full Places, Threads, and People lens digests;
- Together durable grant propagation and block/withdrawal UI;
- contribution receipts and causal repair across real state;
- generalized semantic search;
- saved Composition renderer promotion;
- photographic composition;
- Atlas retirement.

These remain valid product requirements, but they are not prerequisite
foundations.

## 13. Commit and ownership ledger

| Package | Parent | Backend | App | Can start now? |
| --- | --- | --- | --- | --- |
| L0 canon | yes | no | design ref only | after Strategy parent commit check |
| L1 primitives | no | no | yes | after choosing Strategy app head |
| L2 contract | yes | maybe snapshot only | yes | after Strategy contract landing |
| L3 handles | no | no | yes | after L2 |
| L4 projection | no | yes | fixture type use later | after Strategy backend landing |
| L5 arbitration | maybe status doc | yes | no | after L4 + shared policy review |
| L6 root | flag/status | route only if compiler ready | yes | after L1–L5 |
| L7 dossiers | status | read models as needed | yes | after L3/L6 |

## 14. Promotion gates

### Gate A — foundation clean

- Strategy branches complete and their heads recorded.
- Artifact ratchet is not in the Life dependency graph while P1s remain.
- Life canon committed explicitly.
- L1 tests and component catalog pass.

### Gate B — contract clean

- `make contract-check` passes from the parent against the chosen child heads.
- no handwritten Life response mirror;
- one canonical ResourceRef destination seam;
- no semantic payload contains component or arbitrary route vocabulary.

### Gate C — read model clean

- four root-state fixtures deterministic;
- counts reconcile;
- authority mutation recompiles correctly;
- ten arbitration fixtures pass;
- duplicate present-delivery seats = zero.

### Gate D — internal native proof

- native Time root runs behind default-off internal flag;
- no dead ends;
- loading/partial/offline/large-text/VoiceOver evidence captured;
- app-versus-design comparison reviewed;
- no public promotion claim.

## 15. Recommended execution order for one founder

Do one package at a time, with one clean commit series per repository:

```text
L0 canon
→ L1 primitives
→ L2 generated contract
→ L3 object handles
→ L4 pure Life projection
→ L5 shared arbitration
→ L6 flagged Time root
→ L7 canonical destinations/refinding
```

Do not parallelize L4, L5, and L6. Each defines the input boundary of the next.
The only safe parallel work is:

- Artifacts P1 correction in its existing isolated worktree; and
- Life L1 primitive tests after Strategy's app base is frozen.

## 16. Definition of done for this program

The program is complete—not shipped—when:

- the accepted Life contract is repository authority;
- native Life primitives are tested and registered;
- all Life HTTP types are generated;
- canonical handles open one owner destination everywhere;
- Life projection fixtures cover rich, ordinary, thin, and yielded states;
- one shared arbitration policy prevents root duplication;
- a dedicated flagged Time root renders from real typed payloads;
- refinding opens real destinations without writing state;
- Atlas remains a reversible flag-off compatibility path;
- device and accessibility evidence exists for the first native root.
