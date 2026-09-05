---
doc_type: working
status: active
owner: founder / Life engineering / cross-repository architecture
created: 2026-09-05
last_verified: 2026-09-05
expires: 2026-10-05
why_new: Rebaselines the executed Life foundation into a complete engineering program with an explicit Atlas replacement, data migration, and deletion outcome requested by the founder.
depends_on:
  - ../contracts/life-v1-experience.md
  - ../systems/four-root-loop-object-surface.md
  - ../systems/contribution-and-consequence.md
  - life-v1-execution-status-2026-09-01.md
  - life-unfolding-decision-docket-2026-09-04.md
  - lightweight-arrangements-implementation-handoff-2026-09-04.md
supersedes:
  - life-v1-engineering-transformation-sequence-2026-09-01.md
  - life-v1-non-regrettable-engineering-execution-plan-2026-09-01.md
---

# Life complete system and Atlas replacement roadmap

## 1. Outcome and authority

**Life becomes the sole user-facing continuity experience in Home / Chat /
Places / Life. Atlas's root, competing archive, and product-specific workflows
are retired. Existing held material remains accessible through Life and its
canonical object destinations.** This is the founder's September 5 direction.

The new endpoint of the engineering program is a completed replacement, not an
indefinitely flagged Life prototype beside a maintained Atlas experience.
Atlas compatibility is a migration mechanism with explicit removal conditions.
It is not a second product or an acceptable final release state.

This roadmap supersedes the execution ordering and completion criteria in the
September 1/4 plans. Their source-ownership, incremental organization, no-filing-
work, and complete-scenario principles remain useful. It does not mark their
unfinished packages complete or reset the work already landed.

This turn produces an investigation and implementation plan. It does not switch
production flags, migrate user data, delete source code, or deploy anything.
Specific query/storage/API recommendations below are proposed engineering
decisions; the accepted Life and contribution contracts retain product authority.

There are three distinct milestones:

1. **Life-only application:** the supported app has one continuity root and one
   coherent route family; required existing material and controls work there.
2. **Complete Life system:** organization, all four lenses, custody, refinding,
   prospective/shared continuity, useful Returns, and repair work together.
3. **Atlas retirement complete:** obsolete runtime code, producers, API consumers,
   flags, tests, and assets are removed; any retained storage or external-link
   adapter is narrowly documented and no longer owns an Atlas experience.

An internal Life-only build can precede full richness. A public replacement
cannot strand existing material or controls. Full system completion includes
the broader experience; passing a navigation smoke flow is not its definition.

### Implementation receipt — September 5, 2026

The first execution pass has landed in the two child repositories. These are
real replacement seams, not a claim that the complete program is finished:

| Package | Landed | Deliberately still open |
|---|---|---|
| R0 | `/(tabs)/life` is the visible continuity root; legacy Atlas root/deep links redirect; graph/source fallbacks and Life back navigation land in Life; all four lens routes are accepted | Legacy nested readers, producers, tables and API routes still exist behind compatibility paths |
| R1 | Root and depth use one normalized corpus assembly; timeline reads no longer call the Atlas HTTP route; source chronology, source revisions, cursor identity and corpus-fingerprint conflict handling are explicit; depth exposes source revisions; an additive versioned `life_corpus_entries` index and bounded repository keyset reader now exist | The index is still dark: no owner backfill, incremental fan-out, shadow comparison, serving cutover, or deep anchor seek exists yet; the route still reconstructs the current snapshot from owner sources |
| R2 | Trip/memory correction invalidation now includes Life root and depth query families; stale-cursor restart is actionable in the reader | Incremental Life index, backfill, outbox fan-out and custody/refind invalidation are not implemented |
| R4 | Life is always reachable in the four-tab shell; Time/Places/People/Threads readers and bounded position restoration exist | People/Threads remain truthful sparse reads where no owner exists; root composition and dossier/custody behavior are still partial |
| R8 | No user data or source tables were deleted; all changes are committed locally and generated contracts are synchronized | Atlas retirement, migration certification, real-device QA and deployment remain future work |

The receipt was extended after the initial table: app `ea1bbd569`, backend
`f67775fee`, and workspace `fb1a299` (with the earlier execution commits in
each history). The Life-focused backend route/corpus tests, focused mobile Life tests,
contract check, and mobile typecheck pass. A full mobile run completed with
1,186 suites passing and 19 pre-existing or intentionally transitional suites
failing; the two failures directly caused by this replacement were corrected in
`935c804a0`; the focused rerun of both affected suites now passes. The full
mobile suite was not rerun after that two-test correction. The remaining
failures are tracked as baseline work, not hidden as Life completion evidence.
The full backend canary remains a baseline diagnostic
with 20,640 passes and six unrelated failures plus one external-health error.

The backend pre-commit size-budget check remains skipped only because of a
pre-existing oversized unrelated concierge prompt file; other hooks and the
focused Life checks pass. No push or deployment was performed in this pass.

### R1 index foundation receipt — September 5, 2026

The next R1 seam is now explicit in the backend rather than only in the plan:

| Commit | Landed | Boundary preserved |
|---|---|---|
| `0965db32d` | Added the additive `life_corpus_entries` Postgres projection table, with viewer/version/record identity, owner revision, separate time roles, lens membership, typed lifecycle/audience state, lineage/dependency manifests, renderer-neutral payload, withdrawal timestamps, and viewer-order/lens/owner indexes; added `build_life_index_query` | This is rebuildable read state, not a new Life truth owner; it is not populated by this change and it is not a server-driven UI tree |
| `de668635e` | Added `read_life_index_page`, a repository-level bounded reader with one-row lookahead and typed `(sort_at, record_id)` continuation | No HTTP route uses it yet; serving remains on the canonical snapshot path until backfill and shadow comparison certify equivalence |

Focused schema, query, repository-reader, and Alembic-chain tests pass (13
tests for the first unit and 11 for the reader/schema unit). Repository-wide
parity, size, and timeout ratchets remain pre-existing baseline gates and were
skipped for these isolated commits; no data was backfilled, deleted, or pushed.

## 2. Investigation baseline and evidence

Inspected the working workspace and both child repositories on September 5.
Branches observed: `main` in both children, with only remote `main` listed.
Concurrent integration advanced HEADs during the investigation. Later observed
heads at the start of the pass were workspace `03837fc`, backend `56d11b55f`,
and app `1ce1818b8`; the execution receipt below supersedes those inspection
points with workspace `079035c`, backend `332716f8b`, and app `4a4a85bf0`.
These are still not a frozen release candidate; recheck status before any
release work.

Read the current Life experience contract, September 4 rebaseline, execution
status, production-spec anatomy and lens rules, Life Unfolding docket,
contribution contract, arrangement handoff, Atlas retirement decision and
compatibility charter. Older research audits are historical leads; their
missing-capability claims must be checked against current code.

### 2.1 Foundations to retain

| Foundation | Current evidence | Boundary |
|---|---|---|
| Shared root/depth corpus | Backend `life_projection/corpus_query.py`; commit `1b085b19d` | Shared assembly exists; it is rebuilt from owner reads per request |
| Retained sources and confirmed anchors | `core/db/intake_anchors.py`, `life_projection/adapters.py` | Source-only material can be represented without a Plan; this is not a complete custody inventory |
| Versioned cursor and count corrections | `root_projections.py`, `core/models/life_projection_v1.py` | Scope/time/key fields and separate visible count exist; full snapshot and count semantics still need work |
| Explicit intake continuation | `8512a4f25`, page readers | Cap/truncation is now explicit; large-history serving is not solved |
| Native primitives and root | App `components/ui/Life*.tsx`, `components/life/LifeRootV1Screen.tsx` | Four lens choices and basic rows exist; designed digest composition is incomplete |
| Full record and position storage | `app/you/life-record.tsx`, `utils/lifeReadingPositionStorage.ts` | Virtualized Time/Places reader; stores record identity per account/lens |
| Generated contracts | `types/lifeRootProjection.ts`, `types/lifeRefind.ts`, generated schema | The refind alias file is already generated-type-based; do not repeat its completed migration |
| Refinding | Backend `life/refind_sources.py`; app `LifeRefindLane` | Useful truth-aware itinerary/booking retrieval; not yet whole-Life retrieval |
| Return policy | Backend `root_projection/v2/returns.py` | Reusable pure policy; Life's served corpus does not provide a Return candidate |
| Existing source controls | Atlas artifact/candidate/timeline owners, intake lifecycle, memory correction | Retain useful commands and data while replacing their presentation/transport boundaries |
| Design evidence | App `docs/surfaces/life-root/design-refs/`; external Life boards | Tracked rich-Time HTML exists; rich native design conformance is not certified |

### 2.2 Findings that change the roadmap

These are static code findings, not newly executed device or database tests.

| ID | Finding and evidence | Required correction |
|---|---|---|
| F01 | `app/(tabs)/atlas/index.tsx` selects Life only for `routeOwner='tab'` when its flag is enabled; otherwise the full Atlas landing implementation remains | Establish a Life route owner, then delete the old landing composition and its exclusive dependencies |
| F02 | `app/(tabs)/_layout.tsx` declares a Life-titled `atlas` screen, but the mounted custom `FloatingTabBar.tsx` still unconditionally hides `atlas` | Test and fix actual tab navigation, selection, and accessibility; deep-link smoke coverage bypasses this defect |
| F03 | `life-record.tsx`'s “Back to Life” calls `routes.you()`; `app/you/index.tsx` renders `YouPortraitScreen` | Distinguish Life from personal profile/settings and make the return target exact |
| F04 | `life_projection/record.py` routes an `atlas_artifact` ID to `/you/memories/artifacts/{id}`; that screen calls `useCanonicalArtifactProjection`, which fetches `/api/artifact-projections/intake/{anchor_id}` | Separate legacy kept-memory identity from intake-anchor identity; the route is syntactically accepted but reads the wrong owner unless an explicit mapping exists |
| F05 | Graph Plan/Occasion/Commitment/Outcome refs use `/you/history?...&record=<id>`; `app/you/history.tsx` reexports Atlas Long View, whose params omit `record` | Replace pseudo-exact links with kind-aware object readers; a valid path is not proof of exact destination |
| F06 | Source fallback goes to `/you/memories`, which redirects to `/you`; Everything kept opens the same record reader as the full-history door | Implement distinct custody and exploration queries/views; preserve an exact source fallback |
| F07 | Each root/depth read drains intake and Atlas, loads the graph, merges/sorts the entire available corpus, then slices in Python | Replace full-history reconstruction per page with indexed, bounded queries over a common derived index |
| F08 | Atlas drain calls its HTTP route directly; that route runs `ensure_timeline_projected`, counts, year queries, and enrichment for each page | Extract application/repository reads; move projection/backfill out of ordinary Life GET requests |
| F09 | Graph candidates normally sort at the request's `represented_at`; copying candidates into depth entries does not populate occurrence dates | Preserve authored/planned/occurred/imported timestamps and implement real chronological ordering, including undated items |
| F10 | Dedupe uses presentation IDs (`record.<timeline-id>`, `plan.<id>`, `anchor.<id>`); those do not establish equivalence between owners | Normalize identity and explicit lineage first; prevent duplicate representations without collapsing distinct source/claim objects |
| F11 | `LifeCorpusSnapshot.root_read()` supplies empty `source_revisions`; generation time is carried but underlying owner rows remain mutable | Restore dependency revisions; choose an explicit continuation consistency policy and enforce current authority on every read |
| F12 | Intake/Atlas truncation can set partial authority without corresponding degradation details; depth adds `snapshot.truncated` to `has_more` even when it has no way to fetch beyond the cap | Separate incomplete-source state from an executable next-page cursor; partial/unknown totals must not appear exact |
| F13 | Life root is one generic lens section capped at eight priority-sorted leaves; People/Threads are graph filters, Places is not accumulated place relationships | Build stable groups and meaningful lens projections before declaring the designed Life system complete |
| F14 | Legacy correction helpers invalidate Atlas and, via Home, root projections; `life-record` is a separate query-key family outside those prefixes | Define affected-consumer invalidation including depth, dossiers, custody, and refinding; verify immediate removal and delayed-response races |
| F15 | The current Maestro flow resets mock state, opens Time/Places, and returns to `you-screen` | Add real tab, owner-specific destinations, actual multi-page restoration, and real-backend coverage; previous pass does not certify those behaviors |

Reference entry points:
[corpus query](../../travel-agent/backend/life_projection/corpus_query.py),
[Life routes](../../travel-agent/backend/api/routes/root_projections.py),
[record adapters](../../travel-agent/backend/life_projection/record.py),
[native root](../../travel-app/components/life/LifeRootV1Screen.tsx),
[record reader](../../travel-app/app/you/life-record.tsx),
[destination resolver](../../travel-app/utils/resourceDestination.ts),
[tab bar](../../travel-app/components/nav/FloatingTabBar.tsx).

## 3. What replaces Atlas

Classify by user job and runtime dependencies, not by filename. Source/data
retention is independent of whether its original product treatment survives.

| Existing surface/capability | Final home | Migration treatment |
|---|---|---|
| Atlas landing, hero, shelves, timely-return/learning modules, stage composition | Life root | Replace with Life digest; delete root-exclusive composition and automatic fetches |
| Atlas Long View / `/you/history` | Life full record, with Time/Places filters and later all lenses | Transfer grouping/filter capability; retain old links as parameter-preserving redirects |
| Memory artifact reader under `/atlas/artifact` and `/you/memories/[id]` | Exact kept-memory object reader reached through Life | Move useful renderer/commands outside legacy route modules; retain original IDs |
| Intake anchor reader under `/you/memories/artifacts/[id]` | Exact intake-artifact reader | Keep distinct from legacy artifact IDs; owner identity determines dispatch |
| Retained intake submission | Source/original reader and Everything kept | Preserve original access before interpretation, without a review requirement |
| Candidate inbox/review and selected-photo import | Optional source-specific review/import and custody controls | Preserve resolution/correction jobs; remove inbox/scan pressure from Life's default path |
| Saved readings, kept boards, saved compositions | Exact kept-composition reader and custody inventory | Preserve deliberate saves, versions, provenance and generated labels; do not promote transient caches into keeps |
| Compose/parse/facet UI | Existing invoked Chat or contextual composition entry, where still useful | Audit consumers; retire obsolete standalone workflow; retained outputs remain readable |
| Removed timeline items, hide/restore/rename | Contextual record controls plus Everything kept where applicable | Preserve difference between hiding a projection and deleting its source |
| Personal memory, inference controls, privacy, account/data receipts | Profile/settings and contextual evidence controls | Keep reachable from Life's profile/settings door; no competing memory home |
| Saved places and historical place summaries | Places exploration and Life place-relationship view | Keep one place identity and save owner; kept is not visited |
| Recaps, postcards, shared links | Kept composition/object or appropriate share destination | Preserve existing retained/exported material; stop obsolete generation and publication flows after consumer audit |
| Chat artifact cards, notifications, onboarding and profile shortcuts | Exact Life object/record/kept destination | Migrate emitters and consumers, not only the tab label |
| `/atlas/*`, `/you/atlas/*`, old tab links | Thin redirect adapters | No legacy renderer behind an alias; owner, parameter mapping, telemetry and removal condition in compatibility ledger |
| Atlas timeline projection and artifact/source tables | Reused owner storage or migrated derived Life index | No blanket data deletion or table rename for branding; reconcile all historical IDs and user controls |
| Atlas model jobs, vector writers and facet jobs | Named retained capability or retired job | Inspect actual non-Atlas callers first; shared Places/memory consumers may still need them |

Use existing `docs/governance/compatibility-ledger.json` and API operation policy,
not a second lifecycle registry. Its Atlas tab entry currently points to `/you`;
the cutover must change that mapping to the actual Life root.

Internal table names can survive as documented storage compatibility without
preserving Atlas as an engineering product. The finish line does require
removing the obsolete Atlas root and business orchestration; an unused old UI
hidden behind another flag is unfinished retirement.

## 4. Target engineering architecture

```text
Source / artifact / memory / entity / Plan / Occasion / outcome owners
                  │ authorized changes + owner revisions
                  ▼
       Life corpus index and relationship projections
         identity · time roles · lineage · visibility
                  │
       ┌──────────┼───────────┬───────────┬────────────┐
       ▼          ▼           ▼           ▼            ▼
     digest    full record  dossier   Everything kept  refinding
       │          │           │           │            │
       └──────────┴───────────┴───────────┴────────────┘
                  one object/navigation identity

       Return generation + shared root allocation
       consume evidence and revisions independently
       of whether the record itself is available.
```

### 4.1 One derived index, existing domain owners

Recommend an indexed Postgres projection in the existing backend. Reuse the
Atlas timeline projector's useful owner adapters, dedupe history and migration
knowledge, but replace its travel-only public contract with Life records.
Choose extend-in-place versus a versioned replacement table after inspecting
existing keys, hide/rename overrides, backfill cost and deployed readers. Prefer
a versioned derived replacement when preserving the old key assumptions would
constrain all four lenses. Retire the old projection after comparison and
consumer migration. This is rebuildable read state, not a new truth owner.

Minimum index concepts, to specify concretely in R1:

- owner kind/ID, stable canonical resource identity, owner revision;
- typed record kind and presentation identity, explicit equivalence/lineage;
- independently named captured, authored, imported, planned, occurred, generated
  times, local timezone and uncertainty;
- canonical place/person/Plan/Occasion references and authorized containment;
- private/shared scope references, source dependencies, tombstone/suppression;
- derivative revision and event/checkpoint needed for rebuild and invalidation.

Sources, interpreted artifacts, lived episodes and kept compositions are
different counting units. A single email may support a ticket and a journey;
none should accidentally become three visits. Group membership is many-to-many.

### 4.2 Read contracts and cursor semantics

Keep current transports compatible while introducing new semantics explicitly,
likely through Life v2 read contracts. A model named v1 is not a reason to keep
misleading count, destination or state behavior.

Root, full record, dossier, custody and search share identity, eligibility,
time roles and authorization. They do not need identical ranking or SQL: search
matches cues, full record orders chronology, and root chooses finite groups.

Recommended first consistency policy: cursor-bound corpus revision plus keyset,
scoped to viewer, lens, filters, ordering version and expiry. Reject a changed
revision with an explicit restart response; mobile reopens around the stable
anchor. Do not label a mutable recomputed corpus a frozen snapshot. If real
usage shows unacceptable restart frequency, add versioned query membership;
do not build a permanent per-read copy of personal data speculatively.

Current authorization overrides any older cursor or cached projection. Deletes
and narrowed grants cannot be kept visible for pagination stability. Define
typed complete/partial/unavailable source states, count unit and exact/lower-
bound/unknown quality, indexed-through revision, and a next cursor only when
the backend can actually continue. Deep anchor seeking must not replay every
page from the newest record.

### 4.3 Incremental organization

Use source-local explicit links, canonical entities, authored containment and
time evidence first. Episodes and periods are derived groups, not automatically
new Plans or Occasions. Stable group IDs survive label changes; merge/split
keeps redirect/lineage rules and explicit corrections take precedence.

Add bounded model assistance only for useful interpretation and supported
cross-context thread proposals. It cannot decide custody, attendance, grants,
or whether silence means closure. A pasta observation may remain nested in its
trip; a later authored cooking attempt may establish a continuing thread.

Backfill authorized existing owners, then increment from their events. The
current intake outbox has a single acknowledgement lifecycle: do not attach a
second consumer that competes with the graph bridge. Specify transactional
fan-out, downstream events, or independent consumer receipts using existing
outbox/worker patterns. Enforce idempotency, revision checks, retries, bounded
work, dead-letter recovery and prevention of stale worker resurrection.

### 4.4 Human destinations

Recommend a canonical `/(tabs)/life` root and `/life/...` record, kept and
relationship-dossier routes. Keep profile/settings under `/you`. Existing
entity and arrangement routes remain their owners. Old links redirect into
this model while preserving kind, ID, filter, lens and return context.

Separate five destinations around one place: original source, world entity,
my relationship record, current arrangement, exact kept composition. Share the
object-page interaction kernel where appropriate; do not send every one to an
entity screen or a generic history list.

Return context names origin view, lens/filter and anchor. It must distinguish
root → object from full record → object, cover all four lenses, and survive
deep links, list growth, deletion, process restart and account change. Exact
means the receiver can read that owner ID, not merely that its URL is allowed.

### 4.5 Custody, discovery and generated value

Everything kept accounts for authorized retained originals and deliberate keeps,
including unplaced material. It provides kind filters and source-owner controls;
it does not require people to turn loose material into experiences. Hide,
detach, suppress resurfacing, release an interpretation, revoke a share and
delete an original remain distinct commands with accurate consequences.

Refinding must cover the corpus Life can browse, including source-only material,
negative occurrence evidence and saved generated work. Preserve lexical and
structured cue retrieval; semantic retrieval is an optional augmentation.
Use the existing search entry and Life scope rather than creating a separate
search product. Do not turn queries or reformulations into durable interests.

Returns require a real producer, evidence/version dependencies, novelty review,
budgets and shared allocation with Home/Places. Start with bounded useful
families such as reconstructing a journey from evidence and explaining a
cross-source distinction. Generation is off the critical browsing path. Only
explicitly kept versions become kept compositions; failed generation leaves
the factual record intact.

## 5. Execution packages

Package labels describe system dependencies, not separate product slices. Each
package includes backend, generated contract, native consumer and acceptance
work where those change. Do not declare a backend package done while its app
consumer reads the wrong contract.

### R0 — replacement contract and migration inventory

**Start here.** Confirm route/owner map and the findings above against the
implementation base. Inventory each Atlas endpoint, worker, route, source table,
query cache, persisted link, mobile emitter and named test; classify retain,
move, redirect or delete using section 3. Extend the existing compatibility and
operation registries with exact removal conditions.

Resolve planning conflicts: Atlas retirement is in scope; a separate Atlas
flag-off product is not the final state; four-root IA supersedes the August 12
three-root assignment. Adopt concrete corpus count/time/identity vocabulary and
mark only the unresolved prospective owner choices as pending.

Deliverables: operation/route disposition matrix; data preservation checklist;
API read contract proposal; representative migration fixtures. Fix F02–F06 in
early implementation commits so internal navigation becomes truthful. Preserve
the route skeleton while R1 supplies the final reader semantics.

Exit: every rendered family has an identified owner and exact destination or a
clearly unavailable state; the internal four-tab shell actually exposes Life;
old URLs have a named destination; there is no claim that the profile is Life.

### R1 — canonical query, identity and scalable corpus

Extract owner reads from Atlas HTTP routes. Implement the shared indexed Life
query and adapters for graph objects, legacy memories/candidates, confirmed
intake artifacts, retained originals and kept compositions where owner custody
exists. Include independent non-Trip material. Record unsupported producer
coverage explicitly; do not silently omit it from an exact total.

Implement timestamp roles, typed owner identity, equivalence rules, coherent
count quality, per-source availability, keyset continuation and anchor seeking.
Remove full-drain serving and the request-time fallback date for graph records.
Preserve hidden/renamed history and corrected place links during migration.

Commit units: identity/time/count contract and behavioral regressions; approved
index migration/query/adapters; generated API and root/depth consumer changes.

Exit: a corpus larger than every former cap remains fully reachable; read cost
does not grow by loading all history per page; a legacy artifact opens its own
reader; old imports keep historical dates; counts reconcile with the query's
unit and scope; concurrent mutations follow the declared cursor policy.

### R2 — organization, backfill and repair

Build stable period/episode groups, personal place relationships and membership
references on R1. Implement idempotent initial backfill and incremental updates
with explicit outbox fan-out. Preserve user-authored grouping and support
late evidence, dedupe, merge/split and unplaced material.

Wire owner correction/deletion/grant changes into projection invalidation and
rebuild. Reauthorize read candidates immediately; asynchronous rebuilding alone
does not make withdrawal safe. Extend native invalidation beyond root prefixes
to full records, custody, refind results and open dossiers.

Commit units: organization rules and lineage; worker/backfill/checkpoints;
correction and concurrent-read integration.

Exit: rebuilding from owners produces equivalent eligible records; one artifact
can belong to several views without duplicated truth; correction survives
rebuild; a stale worker or response cannot resurrect withdrawn content.

### R3 — dossiers, originals and Everything kept

Implement Life's relationship/episode reader and custody surface around the
shared object kernel. Cover journey/period, episode, place relationship,
shared-with record and attention thread as contracts; show only populated,
authorized organs. Canonical entities and arrangements open existing owners.

Expose original media/text, source provenance, containment, linked retained
conversations, kept generated versions and scoped owner controls. Transfer
legacy memory/candidate/timeline hide/restore/correct operations without a new
mandatory review queue. Audit export/deletion and existing shared-link recovery.

Commit units: dossier/custody read APIs; native views and exact dispatch;
owner-command readback and affected-consumer refresh.

Exit: every retained legacy family can be found and opened; source-only material
has a home; a count names precisely what its door reveals; custody is distinct
from the full chronological record; correction acts on the owning object.

### R4 — complete four-lens Life application

Compose the finite root using the accepted digest, full-record door, conditional
Returns/reflections and stable windows. Use existing Life primitives and the
promoted design evidence. Time groups actual periods; Places groups canonical
personal place relationships; People groups authorized shared records; Threads
uses supported attention continuity rather than Plan connectivity alone.

Provide full records for all four lenses, named filters, thin/zero/partial/
offline states, persistent lens and anchor context, accessible navigation and
bounded recovery when an anchor vanishes. Use contextual maps inside relevant
objects. The root remains an output surface without setup prompts.

Move the active root to Life; move needed legacy object renderers into neutral
components; replace legacy root/history routes with aliases to new readers.
Keep a previous-build rollout recovery path until R8, rather than retaining two
permanent user-selectable products. Coordinate tab chrome with Home/Chat/Places
without redesigning their page content.

Exit: the internal app is Life-only for continuity; no Atlas home or Long View
renderer is reachable through normal navigation; all four lenses have truthful
data behavior and full-depth access. An empty lens is valid; a mislabeled filter
or broken destination is not.

### R5 — refinding and cross-root object continuity

Extend the current Life refind service beyond itinerary/booking rows using R1's
identity/eligibility and R2 containment. Add retained sources, legacy memories,
compositions, groups, place/shared records and supported intentions/threads as
their owners become available. Keep historical negative truth searchable.

Wire the existing search UI with explicit Life scope, understandable match
reasons, exact destination and optional bounded “Around this.” Share return
context with Home/Places objects and contextual Chat continuation. Audit all old
notification, onboarding, profile and Chat-card links.

Exit: browsing and search agree on eligible identities; a source can be found
before interpretation; exact kept versions reopen; queries have no unintended
durable effect; returning through another root preserves the intended object.

### R6 — prospective life and multiplayer continuity

Consume the Plan lane's agreed intention/arrangement owner contracts. Recommend
retained wording with optional time/place and later Plan association, not a
default hidden Plan. Adopt the Life docket's Ahead behavior only after recording
the precise decision; reserve those fields/interfaces in R1/R4 meanwhile.

Integrate attributed shared contributions and relationship visibility with
current audience, purpose and withdrawal checks. Existing relationship and
Occasion code is substrate to audit, not evidence of complete Together support.
The canonical intake artifact endpoint currently rejects Together: do not
simply remove that check to make the People lens look populated.

Exit: kept jazz, arranged dinner and an occurred evening remain distinct; an
expired opportunity does not erase its retained source; a friend's recommendation
can inform a later shared context only within authority; withdrawal preserves
independent contributions and accepted commitments; counts do not leak hidden
participants. No obligation or overdue queue is added to Life.

### R7 — substantive Returns and kept compositions

Connect source-backed production to existing cross-root Return arbitration.
Allocation is coordinated by evidence/intent identity and version, not GET
requests independently racing for a delivery slot. Implement freshness,
suppression, correction dependencies, failure isolation and cost controls.

Retain factual summary value while enforcing the stronger novelty bar for
interpretation. Demonstrate a reconstruction and a new cross-source connection,
with substance before the tap. Store an exact version only when explicitly kept,
using the chosen composition custody owner; preserve authorship and later repair
semantics rather than treating generated prose as source evidence.

Exit: at least two complementary useful Return families consume real authorized
records; a current Home/Places delivery yields the overlapping Life Return while
its dossier remains; saved versions reopen; generation/revocation races cannot
publish stale evidence. Human content review is separate from test success.

### R8 — migration certification, release and Atlas deletion

Run owner inventories and repeatable dry-run backfills in the target environment
before writes. Reconcile source IDs, held counts by kind, overrides, links,
withdrawn/deleted state and media access. Explain differences from Atlas due to
new eligibility/count rules rather than expecting every aggregate to match.

Run real-backend navigation/correction tests and native design/accessibility QA;
cover supported iOS and Android builds. Exercise signed-in account switches,
offline/reconnect and actual multi-page restart. Measure query count, page
latency and memory with representative 100 / 10,000 / 100,000-record fixtures;
set release budgets from measured baselines, not invented pass numbers.

Publish compatible server reads first, then the Life app, then retire obsolete
API paths after the supported-client boundary permits. Remove Atlas-exclusive
UI, composition helpers, active producers, fetches, flags, obsolete query
families, fixtures and assets as their final consumer disappears. Replace
retained screen imports before deleting route files. Update surface QA, journey
docs, API operation policy, compatibility ledger, feature map and system charter.

Keep old external links as pure adapters only where needed. Every exception
names its owner, reason, destination and testable removal trigger. A retained
physical table is permissible; an independently maintained Atlas serving stack
without a consumer and removal condition is not.

Exit: section 8's complete-system and retirement criteria all hold; the release
cohort reaches Life consistently; no user is asked to migrate or organize data;
rollback preserves writes and existing custody. Database destruction is not a
prerequisite for completing the user-facing replacement.

## 6. Sequence and coordination

```text
R0 → R1 → R2 → R3 → R4 → internal Life-only milestone
             └────────→ R5 ─┐
R0 owner decisions ────→ R6 ├→ R8 migration/release/deletion
R1/R2 + shared policy ─→ R7 ┘
```

Design the R5–R7 contracts during R0/R1, and integrate their baseline behavior
into R4 as available. They remain part of complete-system acceptance. This is
not permission to reduce Life to browsing while indefinitely deferring value,
shared material or future continuity.

For one founder: finish one cross-repo package at a time; begin with identity
and reachable navigation, then the indexed corpus. Do not spend the next round
only expanding smoke tests or polishing placeholder rows. The first material
delivery should let the app open the correct objects through a real Life tab
and read a coherent corpus without the current full-history drains.

| Adjacent lane | Needs to supply | Life owns | Can proceed before it settles? |
|---|---|---|---|
| Entity/object kernel | Stable owner IDs, object reader/action contract, context return | Personal place relationship dossier and source/episode navigation | Yes; consume existing exact entity readers and version the adapter |
| Plan/Occasion | Retained-intention owner, arrangement state, participant/edit grants | Prospective projection and shared record/refinding | Yes for past/present/custody; do not invent future persistence |
| Chat/Intake | Authorized admission, source/subject readback, owner events and correction | Eligible indexing, linked context, source/episode visibility | Yes; no wholesale chat scan or Chat redesign required |
| Home/Places | Current-delivery allocation, object handles and repair events | Stable record plus optional Life-native Return | Yes for records; shared Return allocation is an integration dependency |
| Capability retirement | Historical provider evidence and retained-source boundary | Findable tickets/reservations independent of a Trip | Yes; do not resurrect booking execution or delete historical evidence |

Do not hold the whole build for every design lane. Unresolved owner decisions
block their writes, not the entire Life read system. No sub-agents or other tasks
were dispatched by this planning pass.

### First execution batch: concrete commit plan

1. **Route truth and migration contract:** resolve each source family to its
   actual owner in backend `life_projection/record.py` and `adapters.py`, app
   `utils/resourceDestination.ts`, `utils/routes.ts`, and the receiving screens.
   Until a graph dossier exists, return an explicit limited destination rather
   than labeling an ignored `record` query parameter exact. Cover legacy kept
   artifact versus intake-anchor IDs with owner-backed response fixtures.
2. **Actual Life navigation:** introduce the canonical Life route and use one
   visibility decision in `app/(tabs)/_layout.tsx`, `FloatingTabBar.tsx`, rollout
   helpers and back destinations. Keep profile/settings at `/you`. Verify tab
   tap, selected state, deep link and return independently of screenshot mode.
3. **R1 query design and implementation:** document the chosen index migration,
   owner adapter coverage, authorization boundary and cursor invalidation policy;
   implement bounded owner queries in the domain layer and remove route-to-route
   reads from `root_projections.py`. Do not merely lower the current page cap.
4. **Reader integration:** sync OpenAPI with `scripts/sync-types.sh`, update
   `data/rootProjections.ts`, root/depth consumers and fixtures together, and
   cover missing/changed anchor recovery without an unbounded page replay.

Existing regression homes to extend: backend `tests/life_projection/`,
`tests/life/`, `tests/api/test_root_projections.py`; app
`__tests__/components/LifeRootV1Screen.test.tsx`, `LifeRecordScreen.test.tsx`,
`__tests__/components/nav/FloatingTabBar.test.tsx`,
`__tests__/utils/resourceDestination.test.ts`, `productSystemRollout.test.ts`,
and `lifeReadingPositionStorage.test.ts`. Add PostgreSQL integration cases for
query/migration behavior and preserve historical test evidence separately.

The batch is complete when actual tab navigation and exact object reads work,
the replacement query has a measured bounded access path, and both generated
contract consumers agree. It does not complete the digest, Together, Returns or
retirement packages. Avoid a calendar estimate until R1's migration/query
choice is reviewed; current uncertainty is architectural scope and legacy-data
shape, not how quickly the existing tests run.

## 7. Acceptance portfolio

Use the whole portfolio to constrain contracts from the beginning. Test the
observable outcome rather than merely matching a helper's implementation.

| Scenario | Required result |
|---|---|
| Existing Atlas user, years of trips/memories/readings | All retained material survives with exact destinations and applicable controls; no Atlas home needed |
| Fresh user with no record | Four roots and a calm zero state; no scan, classification or setup obligation |
| Europe journey + ordinary NYC week | Useful periods and episodes; travel is not a prerequisite for organization |
| Photo/article sent alone vs supporting an Ask | Only admitted material persists; retained unplaced source stays findable |
| Legacy memory ID vs intake anchor ID | Each opens its own owner; no syntactic-route false positive |
| Ticket bought but never used | Purchase survives; no false attendance or visit; query can find negative truth |
| Old material imported today / timezone boundary / undated source | Appropriate historical or undated placement; no artificial recent occurrence |
| 10,000+ records; sparse authorized pages | Bounded reads reach the oldest record; counts and continuation remain honest |
| Late source, duplicate, corrected place, episode split | Stable links, explainable membership and equivalent rebuild |
| Keep place / keep intention / keep composition | Distinct durable result with the same canonical place reference where relevant |
| Optional Saturday jazz / confirmed dinner / unretained Portugal idea | Correctly different custody and prospective states; no overdue or inferred participation |
| Maya note → private keep → shared dinner → withdrawal | Attribution and authorized reuse; independent history/commitments survive |
| Pasta observation → later cooking at home | Nested observation can become supported continuity without automatic project creation |
| Life Return yields to Home/Places | Underlying source/dossier stays accessible; no duplicate present delivery |
| Open from root vs search vs page 20, restart or back | Same object; correct origin/lens/filter/anchor restored with bounded recovery |
| Delete/revoke while fetch or worker is in flight | No stale resurrection in root, depth, search, custody, open object or generated output |
| Account switch, offline cache, source outage | No cross-account record or position; honest partial/unknown state and reliable recovery |
| Legacy URL and old supported client | Exact compatible landing or explicit retirement response; no render of an obsolete Atlas root |

Verification families: PostgreSQL owner/query/backfill/worker race tests;
generated contract parity; native real/mock consumer parity; route/identity
matrix; registered Life visual QA; large text/VoiceOver/TalkBack; two-account
shared/correction scenarios; current supported-client compatibility checks.

Prior evidence: 36 focused backend tests, frontend typecheck and the mock
simulator entry/lens/back flow passed in the previous round. No fresh full test
run, physical-device evidence, production-data audit, or scale measurement was
performed for this planning document. Those results do not certify R0–R8.

## 8. Completion checklist

- [ ] One actual Life tab and one continuity root; profile/settings are distinct.
- [ ] No active Atlas landing, Long View, or competing memory home.
- [ ] Complete authorized corpus with typed identity and real chronological time.
- [ ] Root, depth, custody, dossier and search agree on eligibility and identity.
- [ ] All four lenses express their intended organization, with honest thinness.
- [ ] Existing retained artifacts, readings, originals and historical controls survive.
- [ ] Non-Trip sources and future intentions are useful without user filing work.
- [ ] Shared records preserve author, audience and independent personal outcomes.
- [ ] Substantive Returns and kept compositions operate over real evidence.
- [ ] Corrections, revocation and deletion propagate across all dependent reads.
- [ ] Native restoration, accessibility and real-backend flows are validated.
- [ ] Large-history serving is measured and bounded; pagination does not truncate access.
- [ ] Backfill/rebuild is repeatable and migration accounting explains all differences.
- [ ] Supported releases use Life; obsolete Atlas clients/producers are retired.
- [ ] Compatibility is limited to documented data/link/version adapters with removal triggers.
- [ ] Obsolete Atlas code, tests, flags, API exposure and assets are removed.

## 9. Documentation landing and maintenance

This document owns the forward execution roadmap. The Life execution status
owns receipts of completed work. The experience contract owns product behavior;
the production spec/design references own accepted composition; the Life
Unfolding docket owns pending prospective rulings. Do not accumulate several
documents that each claim a different next package.

R0 must reconcile the app Life surface contract, August 12 retirement decision's
old IA, personal-memory compatibility charter, current-state page and machine
compatibility registry with the Life-only target. Preserve historical decisions
as provenance; current product architecture is the four-root contract.

Update package status with code references and bounded evidence after each
delivery. Record partial packages as partial. A passing helper test, mock board,
generated schema or smoke flow never substitutes for the package exit behavior.
