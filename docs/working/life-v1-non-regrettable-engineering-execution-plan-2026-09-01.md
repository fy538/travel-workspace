---
doc_type: working
status: active
owner: founder / product / architecture / engineering
created: 2026-09-01
last_verified: 2026-09-04
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

# Life — engineering execution plan

## September 4 rebaseline — current plan

**Read this section first.** Sections 1–16 below preserve the September 1
foundation plan for provenance. Their task statuses, branch instructions,
Time-only scope, sequencing, and definition of done are historical, not the
current implementation program. This rebaseline supersedes those planning
instructions; it does not silently amend the canonical Life contract.

This is an investigation and proposed engineering roadmap, not authorization
to implement schema, authority, or background-processing changes. At the
planning baseline no runtime code had changed; the small execution commits
listed below are the first implementation slices. The program designs the whole Life system;
packages are dependency-ordered implementation units, not an attempt to reduce
the product to one behavior loop.

### A. Decision and outcome

**Proceed to engineering planning now. Do not require another broad Claude
Design iteration first.** The design sufficiently establishes the experience:
one personal corpus, Time / Places / Threads / People, a finite digest,
progressive depth, Everything Kept, contextual refinding, and optional Returns.
The main missing work is an organizing and serving system beneath that design.

Life should let someone recognize, revisit, and use what they have lived,
kept, and have unfolding—without asking them to maintain a database. It is not
the rendered version of the agent's personal-memory prompt, a chronological
dump of chat, or a new owner of Plans, people, places, and artifacts.

The current implementation is useful foundation code, **not the full designed
Life experience**. Preserve and extend its good boundaries. Replace provisional
adapters and root composition where their semantics cannot serve that experience.

### B. Evidence and authority

Audit workspace: `/Users/feihuyan/travel-workspace`; design export:
`/Users/feihuyan/Downloads/vesper-life-anchors/project`.

- Workspace HEAD observed: `704f4c2`; backend: `9f3d80959`.
- App HEAD moved during the audit from `464e7da98` through `ea10e4482` as the
  Entity lane added Places tests. This was a concurrent working-tree audit,
  not a frozen three-repository release assessment.
- Root and backend contain concurrent documentation changes, notably
  Contribution and Consequence, arrangements, and entity handoffs. Those were
  inspected as working context and left untouched. The app was clean at the
  final status check. Recheck all branches/statuses before implementation.
- The latest completed turn of **Components and Plan** was a design handover,
  not completed arrangement persistence. **Entities** was still running;
  no completion or ownership transfer is inferred from its status.

Authority order: accepted product/cross-root/C&C contracts and decisions first;
accepted design behavior second; newer design proposals as explicit open
decisions; runtime code as evidence of what exists, not proof of intended policy.
Some September 1 code-status prose is already stale. A board's fixture-level
acceptance is not native implementation or observed consumer usability.

| Design material | How this plan uses it |
|---|---|
| `00A Canon and Open Arcs` | Selects accepted references; the export README's suggested open board is not authority |
| `25 Life v1 Root - Production Composition` | Root composition baseline, not another concept contest |
| 26–29 lens, thinness, growth, and chip studies | State portfolio; resolve any conflict with the current contract explicitly |
| 06 dossier family, 10 Everything Kept, 11 search | Depth and navigation requirements; conditional organs, not twelve mandatory sections |
| 21–24 Together, refinding, arbitration, contribution | Behavior fixtures to translate into executable contracts |
| 30 mixed corpus, 31 kept-intention lifecycle, 32 five doors | Strong prospective direction; owner semantics remain gated |
| 34 decisions and deltas | Decision docket, not authorization for new persistence or a canonical Ahead section |

In particular, the older empty-lens illustration study does not override the
current contract's compact treatment when the overall corpus is nonempty.
Retain the accepted distinction between a genuinely empty Life and an empty lens.

### C. What exists, what it does not yet provide

Paths in this table are relative to the named child repository.

| Area | Observed implementation | Engineering consequence |
|---|---|---|
| Life API | Backend `api/routes/root_projections.py`, `core/models/life_projection_v1.py`, `life_projection/*`: typed, authenticated, pure read projection | Reuse boundary and generated models; evolve the content contract |
| Corpus | `life_projection/corpus.py` normalizes a bounded inventory from graph adapters | It is not yet the complete personal corpus or a paginated custody index |
| Input coverage | `adapters.py` projects Plan, Occasion, Commitment, Outcome; upstream graph read has bounded default limits | Kept artifacts, source-only material, meaningful chat references, and future intentions are not covered simply by increasing root row limits |
| Lens semantics | Threads currently derives from Plan relationships; Places/People from subsets of graph records | Implement attention continuity and personal place/person relationships, not renamed graph filters |
| Counts and depth | Compiler caps visible entries; `total_entry_count` reflects that result | A preview count cannot promise the full record; use explicit count scope and a real full-record query |
| Arbitration | Life yielded state clears sections/counts; model also disallows candidates in that state | Violates the contract if only a Return should yield: retain the record and suppress just that delivery |
| Return utility | `root_projection/v2/returns.py` has a pure arbitration policy; no runtime caller was found in the backend search | Tested policy is reusable, but coordinated Life/Home/Places allocation is not established |
| Native root | App `components/life/LifeRootV1Screen.tsx` has four selectable lenses and generic rows behind an internal flag | This is not yet the designed period/chapter, chip, dossier, or complete-corpus experience |
| Destinations | Adapter links fall back to `/you/history?...&record=...`; legacy reader does not resolve that record parameter | Fix semantic navigation before promoting generic rows as complete objects |
| Root controls | Search/archive icons are not actionable; full-record doors are limited; loading/error replace the surface | Complete the actual browsing loop, not just first-viewport rendering |
| Mock parity | `useLifeRoot` supplies no mock data while `useData` bypasses fetch in mock mode | Provide real typed fixtures; hook-mocked component tests do not catch a blank mock root |
| Canonical artifact | `api/routes/artifact_projections.py` reads confirmed private intake anchors; canonical mobile reader exists | Reuse exact artifact identity and reader. Together currently returns 403; do not claim shared corpus support |
| Refinding | `backend/life/refind_sources.py` searches a bounded itinerary/block/trip corpus | Extend candidate coverage and containment; do not mistake it for full personal-memory search |
| Intake and repair | Durable intake outbox/worker/graph bridge; versioned memory correction outbox and root invalidation utilities exist | Reuse mechanisms after owner audit; they do not automatically organize or repair every Life view |
| QA | Life surface is registered but its design manifest fails the current checker | Repair the reference manifest and capture native evidence; HTML fixtures alone cannot close this gap |

The current corpus route also needs explicit unavailable/partial-source
semantics. A successful subset must not be presented as a complete Life record.

### D. Architecture recommendation: an organized read model, not another owner

```text
Authorized source and object owners
  → normalized corpus references + lineage
  → incremental organization and relationship projections
  → scoped root / full-record / dossier / search read models
  → native Life views and existing canonical owner destinations

Optional Return production and cross-root allocation consume this corpus;
they do not decide whether the underlying record continues to exist.
```

**D1. Preserve source ownership and custody.** Sources, confirmed artifacts,
governed claims, arrangements, Occasions, Commitments, and canonical entities
remain with their existing owners. A corpus reference identifies owner, object,
revision, authorized scope, provenance, and relevant timestamps. It does not
duplicate every owner's payload or acquire authority by being indexed.

Chat is not an indiscriminate memory feed. An Ask may remain in conversation
history without becoming a durable personal claim or Life item. Explicit
Bring/Keep and other permitted write-back follow C&C. Link eligible conversation
context rather than copying every message or treating the personal-memory
narrative as a factual Life record. No extra filing step should be required
merely to make already-authorized material findable.

**D2. Separate admission, organization, and presentation.** Admission asks what
the actor may retain/read. Organization asks how existing material relates.
Presentation selects a finite useful view. A source can be in Everything Kept
and search before it belongs to a rich episode. Failure to infer a group must
not make retained material disappear.

Use deterministic explicit links, canonical place identity, authored context,
and temporal evidence first. Use bounded model work for ambiguous relationship
proposals, meaningful thread continuity, and grounded labeling—not for grants,
attendance, ownership, or arbitrary screen layout. A planned flight or passed
date does not establish a completed journey. A dozen photos is not a dozen visits.

**D3. Represent organization without inventing an Occasion for everything.**
A derived episode/group can span a journey, neighborhood week, or local dinner
without a user-created Plan. Give persistent navigable groups stable identity
and revision/lineage semantics; mutable titles are not primary keys. Choose the
smallest projection storage needed after schema review. Do not add a universal
Experience owner table merely because several views need grouping.

Membership must be explainable and repairable. Support late evidence, merge and
split, explicit correction, duplicates, and material that remains ungrouped.
Do not force single-parent filing: one source can illuminate a time period,
place, person, and meaningful thread through references rather than copies.

**D4. Organize incrementally.** Build from authorized owner events and scoped
initial backfill, not repeated scans of every chat on each Life read. Each event
needs an idempotency key, owner/object revision, changed dependencies, retry and
dead-letter behavior. Coalesce rebuilds by affected subject/group where safe.

The existing intake outbox has a single published/acknowledged lifecycle.
**Do not attach a competing Life consumer to that same claim/ack stream.**
Design explicit fan-out, a downstream durable event, or independent consumer
receipts transactionally at the appropriate boundary. The correction outbox's
versioned acknowledgement is a useful pattern, not proof of complete Life repair.

Read endpoints remain side-effect-free and never run an unbounded model pass.
Materialized summaries improve latency; current authority must still be checked
when serving them. Async recomputation and client invalidation are not sufficient
revocation controls. Prevent an older worker or in-flight response from reviving
withdrawn material after a correction.

**D5. Serve one corpus through several purpose-built queries.** Define root,
full-record, dossier, Everything Kept, and search contracts together:

- Root: the accepted finite digest, typically four or five meaningful outer
  blocks—not eight arbitrary leaves. It exposes depth without dumping it.
- Full record: stable pagination/cursors, deterministic ordering, explicit
  scope and unit of count. Preview count, total items, groups, lived visits,
  and kept possibilities are different quantities. Unknown totals stay unknown.
- Dossier: conditional modules with representative evidence and real doors to
  depth. A place's world object, my relationship with it, original source,
  arrangement, and saved composition are related but different destinations.
- Everything Kept: durable retained material remains reachable without being
  elevated into a personal narrative or a standalone thread.
- Search: authorized candidates with containment/context and exact owner
  destinations. Start with sound corpus coverage and lexical/context filters;
  semantic retrieval augments, rather than substitutes for, that foundation.

Maintain captured/imported, authored, planned, occurred, and generated time
separately, including uncertainty and timezone. Treat maps as contextual views
of the relevant record, not a competing fifth root or a requirement for every
artifact. People views must not leak hidden participation through labels/counts.

**D6. Keep optional value delivery separate from memory availability.** Factual
records need no novelty test. Generated Returns do. Use the existing arbitration
policy behind a coordinated, versioned allocation consumed by the roots—not
independent GET requests racing to claim seats. Home urgency may remove a
duplicated Return from Life, never its dossier or source record. A generation
failure must not break browsing. Define cost budgets, backpressure, and a stale
delivery policy before enabling background generation.

**D7. Evolve contracts deliberately.** Reuse backend models and generated app
types. Additive fields may extend v1; changed count, state, and destination
semantics require an explicit compatibility decision, potentially a v2 read
model with a v1 adapter. Separate corpus availability from Return delivery state.
Do not preserve a misleading `yielded` meaning just to avoid a schema version.

### E. Dependencies and decisions—not reasons to pause the whole system

| Decision | Recommendation | What waits / what can proceed |
|---|---|---|
| Kept intention before a Plan | Reconcile with arrangements D1: person-owned prospective material with optional Plan association; stable ID, lineage, release, authored temporal hint | Persistence and real future-item writes wait for the owner/schema decision; corpus, past/present records, readers, and fixtures proceed |
| Ahead composition | A conditional view of approved prospective owners, not a fifth lens or Life-owned planning engine | Accept the precise behavior through the Life docket before changing canon; preserve intended versus occurred in all contracts now |
| Thread admission | Meaningful attention continuing across contexts; source-specific questions can remain nested | Approve examples and counterexamples before automatic promotion; retained material remains findable meanwhile |
| Group correction | Reversible source-bound membership correction, no routine organizing homework | New mutation/persistence requires owner review; deterministic projection and lineage tests proceed |
| Shared material | Read from the existing authorized owner; preserve contributor identity and independent accepted commitments | Together production waits for explicit read/grant contracts; private Life and authorization-negative tests proceed |
| Saved composition | Exact deliberately kept version, distinguished from ephemeral generated contribution | Confirm custody owner and retrieval contract; do not use short-lived `source_contributions` as an archive |
| Read-model persistence and workers | Small derived index/projection layer in current backend, no new microservice by default | Schema/background-loop posture requires founder review; pure compiler/query contract work proceeds |

Coordinate against the [arrangements handoff](lightweight-arrangements-implementation-handoff-2026-09-04.md)
and [Life Unfolding docket](life-unfolding-decision-docket-2026-09-04.md), which are
working proposals. In particular, do not implement the older mandatory-Plan
parent rule by creating hidden pseudo-Plans or by storing intentions as user
preferences. The [Plans in Real Life design handover](claude-design-plans-in-real-life-handoff-2026-09-04.md)
can refine arrangement surfaces without reopening Life's entire layout.

Entity integration consumes stable entity identity and the current canonical
resolver; this lane owns the personal relationship view, not a second entity
page. Chat integration needs clear intake/keep receipts and object context, not
a Chat redesign here. No edits to those lanes are authorized by this document.

### F. Complete scenario portfolio

Design and test contracts against this portfolio from the start; do not select
one journey as the architecture for all of Life:

1. Multi-city Europe trip with tickets, photos, restaurants, and conversations:
   digest → chapters → evidence → exact originals, without duplicate records.
2. A normal New York week and local dinner with less material: no empty travel
   shell, invented significance, or demand to complete a memory.
3. A standalone photo or saved article, without Plan/Occasion/group: immediately
   reachable through authorized custody and later enriched by relevant context.
4. Ask-only conversation versus deliberate Bring/Keep: different durable effects.
5. A friend's restaurant note, kept place, personal intention, arrangement, and
   saved composition: the five doors remain distinguishable around one entity.
6. An undated possibility, an upcoming dinner, and a date that passes without
   attendance evidence: no accidental conversion into a lived visit.
7. A question about pasta that belongs inside a trip, versus a genuine thread
   continuing into cooking at home: no automatic thread proliferation.
8. Shared dinner contributions, contributor withdrawal, and a separately accepted
   commitment: repair the affected material, not unrelated social history.
9. Old material imported today, unknown dates, and conflicting source dates:
   useful placement without pretending import time was occurrence time.
10. Years of material exceeding all current graph limits: counts reconcile,
    pagination reaches the oldest item, and root brevity does not limit access.
11. A late photo changes a grouping; a duplicate arrives; an incorrect relation
    is corrected: stable links and predictable merge/split behavior.
12. Home currently owns a live Return: Life retains its record; stale or failed
    generation does not create an empty Life.
13. Partial source outage, offline cache, account switch, grant revocation, and
    delayed worker completion: no false completeness or cross-account recovery.

### G. Proposed execution packages

Each package has backend/app/workspace commit units where applicable. Stage
explicit files and recheck current branches before every commit. Commit/push
authorization will come from the execution request, not this planning pass.

| Package | Work and likely seams | Exit condition |
|---|---|---|
| P0 — executable contract baseline | Characterize current defects; specify corpus scope, timestamps, count units, grouping, destination types, availability vs Return state; reconcile design manifest against boards 25/06 and approved behaviors | Full scenario matrix and contract decisions are written; known failures have targeted regression cases; pending prospective semantics remain labeled |
| P1 — complete eligible corpus | Extend owner adapters beyond bounded graph results; include retained source/artifact records without requiring a Plan; implement authorized full-record/custody query and pagination | Material beyond root/graph limits is reachable; count semantics reconcile; private and revoked material are filtered before aggregates |
| P2 — organization and repair | Stable derived group/membership model, deterministic relationships, scoped backfill, incremental work scheduling, idempotency and correction; bounded semantic proposals only after baseline | Late evidence/duplicate/merge/split/revocation scenarios pass; rebuild yields equivalent authorized records; no whole-chat GET scan |
| P3 — browsing and destination APIs | Root digests across all four lenses, full records, conditional dossiers, Everything Kept, contextual search; replace legacy record pseudo-links with real typed destinations | Every root leaf and depth door resolves to its intended object/view; no unsupported owner state labeled complete |
| P4 — native Life experience | Compose accepted root and dossiers, wire search/archive, accurate depth counts, typed real/mock data, last-lens behavior, loading/partial/offline/large-text/accessibility states | All four lenses consume real contracts; native navigation and data parity work, not just mocked hook snapshots |
| P5 — prospective and multiplayer integration | Consume approved intention/arrangement ownership and shared-material grants; five-door identity, mixed-time views, contextual People/Places, source withdrawal repair | Future material is not attendance; shared views preserve custody and do not expose private context; no extra planning workflow in Life |
| P6 — Returns and cross-root continuity | Integrate existing candidate policy with coordinated allocation, lineage, freshness, budgets and affected-root invalidation; exact kept-composition custody after owner decision | Life record survives Return yield; no duplicate delivery seat; stale/corrected evidence cannot regenerate an invalid Return |
| P7 — cutover and operational readiness | Legacy mapping/backfill, comparison audits, opt-in internal rollout, real DB/concurrency tests, native QA, monitoring and rollback | All required scenarios have end-to-end evidence; old material has a real destination; flag rollback remains safe before any Atlas pruning |

Dependency order: P0 → P1 → P2/P3 → P4 → P7. Specify P5/P6 interfaces during
P0; land their runtime work as owner dependencies settle, and include both in
the complete-system acceptance before retiring compatibility. Pure reader and
native work can overlap once contracts are stable, but a solo founder should
finish coherent package boundaries rather than run several conflicting root
rewrites. P2 schema approval precedes migrations. P5 waits only on its own
unresolved owners, not every upstream package.

Suggested commit boundaries within a package: backend model/compiler/tests;
backend owner queries or approved migration/worker/tests; workspace OpenAPI
and app-generated types; mobile reader/fixtures/tests; status/acceptance docs.
Run `scripts/sync-types.sh` for backend API changes and resolve frontend breakage
in the same coordinated package. Do not claim completion between an incompatible
backend change and its generated mobile consumer.

Risk classification: query/model changes are contract-sensitive; semantic
organization is also prompt-sensitive; schema, auth, and background processing
are founder-only review work. Mobile hooks/navigation are parity-sensitive and
route architecture may require founder review. Follow both Task Intake guides.

### H. Focused design work that remains

Do a bounded finishing pass alongside P0/P3/P4, using realistic payloads:

- Sparse versus rich dossiers and how representative rows lead into complete
  records; avoid making all optional dossier organs mandatory.
- A source with no group, a useful empty lens, and unavailable/partial data.
- Five doors around one entity; distinguish original source from relationship
  record and future arrangement without introducing a management dashboard.
- Approved future/past mixture and kept-versus-lived counts.
- Direct correction entry, a changed grouping, and a yielded Return with the
  unchanged record still visible.
- Native text scaling, scrolling, long labels, map context, and navigation back.

These are state and interaction acceptance questions, not a request to reopen
the whole visual language. Repair the registered Life design-reference manifest
first; then use the surface contract's native screenshot/QA path. No screenshot
or mobile usability acceptance was produced by this investigation.

### I. Research implications

Research reinforces the architecture but does not validate Vesper's complete
experience. Sellen and Whittaker distinguish useful remembering activities from
indiscriminate capture. Our application: optimize Life for recognizable cues,
revisiting and future usefulness, not capture volume or mandatory reflection.
Their work is conceptual guidance, not evidence for this specific four-lens UI.
[Beyond total capture](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/p70-sellen.pdf).

OmniQuery studies how contextual connections across captured material improve
personal question answering. Our application: preserve atomic evidence and
derive cross-source context so the same corpus supports browsing and refinding.
Its evaluated system is primarily question answering, not proof that an
automatically organized Life tab will work; inferred context still needs
lineage and correction. [OmniQuery, CHI 2025](https://arxiv.org/html/2409.08250v2).

The practical conclusion is not “add a larger memory prompt.” Build trustworthy
organization and progressive access around the material, then layer grounded
interpretation and optional delivery on top.

### J. Validation recorded September 4

- Backend targeted offline run: **39 passed** across `tests/life_projection`,
  `tests/life`, and `tests/eval/test_life_refinding_checks.py`.
- Mobile targeted run: **26 passed in five suites**: LifeRootV1Screen,
  LifeRefindLane, LifePrimitives, lifeRefindPresentation, and canonical-artifact
  Life smoke coverage.
- App `npm run typecheck`: passed.
- Workspace `make contract-check`: passed, including active mobile projection,
  generated types, place identity seams, schema bridge, and Occasion behavior.
- `npm run qa:design:check -- life-root`: **failed** because the manifest lacks
  the checker's required string `surface` and nonempty `pairs` array.

The manifest failure was repaired in app commit `efdcc9471`, after which the
Life design-reference check passes (with a warning that the tracked evidence is
HTML rather than a native screenshot). Runtime execution commits are:

- backend `9eeeb88e1`: preserve the record when Return delivery yields;
- backend `e2058817c`: label bounded corpus previews as partial;
- app `ca83daf49`: provide typed Life mock data;
- app `14b5e892d`: distinguish bounded root previews in the native door;
- app `18e51de7e`: align the surface contract with yielded behavior;
- app `89367c36e`: keep mock lens destinations aligned.

Passing tests establish the current foundations, not a complete organizer,
real Together support, coordinated Returns, exact dossiers, real-backend native
parity, production concurrency safety, or visual acceptance. No production
data, scheduled provider loop, database migration, or full application test run
was exercised. Implementation must add real-Postgres tests for leases,
fan-out/acknowledgement, pagination and repair races, plus native/device evidence.

Track operational correctness as well as delivery: eligible-but-unreachable
items, stale projection lag, unresolved destinations, count mismatches, dead
letters, grouping repair rate, duplicate Return seats, and authorization-denial
behavior. These are engineering acceptance signals, not invented product-market
fit targets.

**Next authorized step to request:** execute P0 and P1, with founder review of
the narrow schema/owner decisions before P2 migrations. This starts building
the shared system while the arrangement lane finishes its bounded decisions.

---

## Historical September 1 foundation plan

The following sections are retained as historical planning context. Do not
use their old branch/task status or Time-only completion scope as current truth.

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
