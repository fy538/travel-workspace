---
doc_type: working
status: active
owner: founder / Life engineering / cross-repository architecture
created: 2026-09-05
last_verified: 2026-09-07
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

## Current execution baseline — September 7

**Latest inspected checkpoint — September 7 architecture review and planning:**
backend local `main` is `7a1d18070`; the latest Life rehearsal, organization,
repair and scoped-reader packages remain on
`codex/life-shadow-rehearsal-2026-09-07` at `f0a8d4f69`, not merged into
backend main. The branches have 65 main-only and
46 Life-only commits at inspection; these counts do not describe equivalent
amounts of Life work. Earlier Life foundation packages were integrated; that
does not include every later receipt below. App `f4401ef73`, currently checked
out on `codex/entity-object-design-completion`, contains the earlier exact
reader-restoration correction `17eea1980`. Canonical workspace main is
`55f2bcb` with concurrent uncommitted strategy/design work. This plan is edited
in the initially clean isolated Life documentation lane based at `b4f828f`.
The [execution receipt](life-system-execution-receipt-2026-09-06.md)
preserves historical package evidence; this paragraph corrects any broader
claim that all later Life work is already merged. [§10](#10-design-independent-execution-plan--september-6)
is retained as the acceptance checklist; [§11](#11-bounded-shadow-rehearsal-execution-packet--september-7)
owns shadow-rehearsal acceptance, and [§12](#12-connected-organization-and-reader-implementation-plan--september-7)
owns organization-and-reader requirements. [§13](#13-architecture-review-follow-through--september-7)
is the current corrective execution order inside those packages. Original
implementation instructions are historical where a package has landed. None
of this establishes a populated real corpus, complete parity, indexed serving
or release.

R0–R8 remains Life's sole forward roadmap. The engine design supplies behavior
and implementation detail; the execution-status file preserves receipts. The
[coordination register](complete-system-integration-roadmap-2026-09-05.md#2-current-coordination-register--september-6)
owns current cross-lane assignments. Historical findings below describe their
inspection date, not a request to repeat completed work.

| Layer | Current implementation | Next work / limitation |
| --- | --- | --- |
| R0 / R4 root and reading | Canonical Life route, Atlas redirects, four depth lenses, exact-owner and identity-restoration improvements | Rich lens organization and complete owner/destination coverage are not certified |
| R1 common reads | Shared snapshot assembly, chronology, owner revisions and conflict-aware cursors | Routes still assemble owner snapshots; indexed serving has not cut over |
| R1 / R2 index helpers | Typed bounded reads/writes, all-lens planner, owner capability matrix, owner-specific projectors, resumable backfill, reconciliation and complete typed comparison; bounded four-viewer corpus rehearsal now passes with canonical owner-time ordering | Establish broader corpus/viewer parity and future-version delivery boundaries; future-version targets do not yet receive live owner fanout |
| R2 change safety | Revision guards, withdrawal/restore, dependency CAS, separate Life outbox and repair; retained-source, Plan, Occasion and Outcome projectors, audience repair and fenced index publication/delivery | Organization repair results are not consumed; live/backfill completion differs; close the organization publication race and retain Intake's independent acknowledgement |
| R2 organization | Stable groups, typed memberships/links, exclusions, controls, identity resolution, content/read epochs, evidence envelopes and bounded internal group reader | Plan/Occasion callbacks cover owner containment; source/Outcome organization and public group reading are not connected. See §13 |
| R3 / R5 retrieval | Retained sources and canonical destinations have landed | Broader custody/refinding, dependent repairs and retained booking-reader mapping remain |
| R6 prospective/shared | Consumer requirements established | [Pre-Plan intention proposal](retained-intention-before-plan-decision-proposal-2026-09-06.md) is unadopted; missing owner adapters cannot be replaced by Life writes |
| R7 / R8 richness and replacement | Design/scenario portfolio and migration obligations are explicit | Returns, organization quality, whole-corpus cutover and Atlas deletion remain incomplete |

**Target-capability checkpoint:** backend `77eb3780b` now exposes
`owner_fanout_status` and `receives_live_owner_fanout` on the existing backfill
run and worker result. Non-`life.v1` builds remain historical shadow targets;
the default is covered by current version-less owner events. This is capability
metadata, not measured successful delivery or permission to switch readers.
Dry-run/comparison and explicit shadow targets remain supported. No writer,
subscription, schema or activation policy changed. See the
[joint receipt](complete-system-integration-roadmap-2026-09-05.md#92-cv-1-and-life-target-capability-execution-receipt--september-6)
for the implementation and validation boundary.

**Restore correction — September 7:** the retained-source projector now allows
an owner-authorized `source_unrepresented` event to restore an existing
withdrawn row; ordinary replay remains fail-closed. It also uses the event's
authoritative owner revision as the read clock when an explicit represented-at
clock is absent. Both previously failing PostgreSQL restore cases now pass,
alongside the offline projector tests. Evidence and commit are recorded in the
integration roadmap receipt; this remains shadow-index/readback evidence only.

**Code-review correction pass — September 7 (working patch):** a fresh review
of the Life shadow path corrected the remaining safety edges in the isolated
`codex/life-shadow-rehearsal-2026-09-07` worktree. Retained-source eligibility
now evaluates expiry against the current authorization clock while preserving
the historical `represented_at` snapshot for cursor stability; a record-level
backfill failure reopens its owner-family checkpoint so unresolved work is
reachable on retry; Plan/Occasion/Outcome replays cannot restore revoked,
suppressed or deleted rows without an explicit restore change kind; rehearsal
reports reject false-green comparisons, cases, phases and blocking findings;
and retained-source reads are pinned to the requested projection version.
The root digest now reserves bounded representation for each owner kind,
scheduled Plan and authored Outcome timestamps no longer populate public
`occurred_*` fields, and Plan subtitles label schedule dates as planned.
Graph-owned Life destinations are lens-neutral identities; the mobile reader
applies the originating lens when reopening an exact row. Mobile Life
restoration now filters unsupported rows before indexing, stops
repeating a failed cursor request, and preserves identity-based restoration
across query rerenders; stale-cursor restart also resets the restoration
attempt. Focused evidence is 170 offline Life tests, 81 Life-related mobile
tests, mobile TypeScript, Ruff and `git diff --check`; no serving cutover,
database migration or remote publication is included. The backend patch is
committed as `6fefdb756` on the isolated Life worktree and the mobile patch as
`17eea1980` on the app branch. The repository-wide backend size-budget hook
remains a pre-existing failure and was explicitly skipped for the backend
commit; all other commit hooks passed.

**Code-review closure — September 7:** the follow-up pass in the same isolated
worktree is committed as `163b18e8b` (`fix(life): close organization and reader
safety gaps`). It closes the remaining reviewed R1/R2 edges without changing
the serving path or adding a second index: owner-self exclusions remain
effective when `supports_occurrence` rows migrate to neutral containment;
complete-set reconciliation requires the current per-group content revision;
episode memberships can be explicitly restored while ordinary replay remains
non-resurrecting; and organization evidence now preserves purpose/time-role
metadata and rejects scheduled/refind evidence from occurrence relations.
Topology checks serialize per viewer/version so disjoint concurrent links
cannot close a longer cycle. Evidence refreshes advance content/read epochs,
resolution repairs fence affected groups, and membership/child cursors carry
viewer, version, group scope and freshness. Immediate child reads are bounded
with an explicit continuation cursor. The Life corpus route now rejects
non-object or incomplete cursor payloads as typed 422 errors before constructing
the pagination model.

The retained-source worker test now waits on its own durable outbox row rather
than assuming a globally bounded repair sweep will claim that event first; this
removes a local-queue ordering flake while preserving worker-path coverage.
Validation: the complete `tests/life_projection` selection passed **228 tests**
on the isolated PostgreSQL-backed environment; the focused migration,
organization, reader and route selection passed **29 tests**; Ruff and
whitespace checks passed. The commit hook's repository-wide size-budget and
status-dead-gate checks remain pre-existing baseline failures and were skipped
explicitly; all other applicable hooks passed. This is still shadow-index
evidence only: no serving cutover, owner-producer change, migration, Atlas
deletion or remote publication follows from this package.

**Maintained-delivery follow-through — September 7:** commit `0b822c3aa`
(`fix(life): unify maintenance completion`) adds the shared
`LifeMaintenanceResult` boundary and routes Plan, Occasion, Outcome and
retained-source live handlers through it. Required organization repair can now
remain `pending` instead of being acknowledged as success, while a stale owner
whose successor is current is explicitly `superseded`. Production backfill uses
the same maintainer by default; injected projectors remain a migration-test
seam. Commit `767f70499` preserves explicit non-default shadow projection
versions through the identifier-only event bridge, restores retained-source
rows through an exact owner-state read rather than a viewer-wide scan, and adds
regressions for default backfill dispatch and authorized restore. The offline
Life selection passes **199 tests** with **34** database/API-key cases
deselected. The repository-wide size-budget and status-dead-gate hooks remain
pre-existing baseline failures and were skipped explicitly; all other
applicable hooks passed. This closes the shared completion and bounded-lookup
package, but not the transaction-atomicity requirement: index and
organization still use separate repository transactions and require the
controlled race package below.

**Reverse-reconciliation follow-through — September 7:** commit `91024a856`
(`fix(life): align reconciliation with maintenance`) makes the bounded reverse
reconciler use `maintain_life_owner_change` by default whenever repair is
requested and no migration projector is injected. It carries the maintainer's
index result and exposes `repair_pending`/`withdrawal_pending` rather than
reporting a partially completed repair as final. Existing pure projector
injection remains available for migration tests. The focused reconciler and
maintenance tests pass, and the complete Life selection with the connected
database passes **235 tests** under `-m 'not requires_api_keys'`. The next M1
checkpoint is durable multi-slice progress for affected scopes; no new queue or
schema was introduced here.

**M2 source-evidence handoff — September 7:** commit `bac99b1b0` adds a
read-only `retained_source_evidence_unit` adapter over the existing
authoritative retained-source projection. It records exact submission/source
references, owner revision and immutable capture time with `CAPTURED` role;
the evidence contract rejects using that unit as `supports_occurrence` proof.
No Capture transaction, producer, organization write or new owner is added.
The offline Life selection passes **204 tests** with **34** database/API-key
cases deselected. The next dependency is Capture's agreed bounded evidence
read (occurred/place/people roles and lifecycle/locator semantics); until that
seam exists, retained originals remain safely findable but ungrouped beyond
source-only organization.

**Publication-fence follow-through — September 7:** commit `3a44caf0f`
(`fix(life): fence index and owner materialization`) adds an optional existing
connection to the index writer and primary organization materializer/archive.
The default maintainer now opens one short transaction for the index plus
owner-group publication, and queues resolution repair until that lock is
released while still folding its result into `pending` completion. Injected
projectors retain their old call shape. A barrier-style regression proves the
order `begin → materialize → commit → reconcile`; offline Life validation is
**200 passed, 34 deselected**. This closes the primary publication interleave
for supported owner groups but does not make resolution repair atomic or add
multi-slice consumer checkpoints; those remain explicit follow-up work.

**Roadmap rebaseline — September 7:** implementation packages for R1/R2-A
through F have landed. Their functions and tests do not complete every package
exit. Fresh code inspection found Time-only owner materialization, a
single-owner reconciliation primitive without a bounded corpus traversal,
unresolved-work recovery still to connect, and comparison/report assembly
still to implement. [§11.1](#111-inspected-code-and-remaining-connections)
records these distinctions. Extend the existing components at those seams.
The next Life checkpoint is a bounded local corpus rehearsal across supported
owners and an explicit viewer cohort: exercise late and out-of-order updates,
withdrawal, authorized restoration, audience changes and lease/replay failure;
emit a machine-readable coverage/parity report; and classify every mismatch as
fixable, unsupported or blocked. In parallel, advance R2-G's deterministic
organization and durable correction seam against the same authoritative rows.

Use `life.v1` in the isolated local rehearsal database. Other versions may
remain explicit historical-only diagnostic builds, with no continuity claim.
Do not switch readers, activate a new continuously maintained version, delete Atlas or call the
rehearsal a release certificate. No native session is required for this
engineering checkpoint; preserve later native/release acceptance separately
under the founder's current deferral.

**Bounded corpus rehearsal — September 7 (working evidence):** the connected
`test_life_shadow_corpus_postgres.py` case now provisions four viewers (owner,
participant, second participant, unrelated viewer) and the four supported
shadow owner families, runs bounded resumable backfill, publishes the durable
outbox events through the registered owner consumers, delivers Plan revisions
out of order, and verifies Occasion/Encounter Outcome withdrawal followed by
an explicit rejoin restoration. The graph producer now distinguishes
`occasion_membership_restored` and `outcome_audience_restored` from ordinary
membership changes so the projector's fail-closed replay rule does not block a
legitimate restoration. The report writer emits the expected
`vesper.life-shadow-rehearsal.v1` envelope. Owner/audience identity assertions
are green, but the report is intentionally `inconclusive`: undated Plan and
Occasion rows receive a materialization-clock `sort_at` while the canonical
snapshot uses its request clock. Resolve that stable ordering authority before
any indexed comparison can be called green or a reader cutover can be
considered. This package does not activate serving, migrate/delete Atlas, or
claim unsupported owner coverage. The backend package is committed as
`e03f8f980` on the isolated Life worktree; focused connected and producer/
projector regressions pass. The repository-wide size-budget hook remains a
pre-existing failure and was skipped for this commit only.

**Stable ordering authority — September 7 (working evidence):** the follow-up
package closes the rehearsal's ordering mismatch without changing the reader
or activating the index. The owner graph models and repository projection now
carry immutable Plan/Occasion `created_at` values (and Occasion `lived_at`);
canonical Life ordering uses scheduled Plan time, owner-lived time, or owner
creation time as applicable. Retained-source rows use immutable submission
creation time rather than mutable processing `updated_at`. Every canonical
record now carries a `sort_precision` basis into the shadow row, while public
`occurred_*` fields remain null unless an occurrence assertion exists. Legacy
storage-neutral fixtures may still fall back to an explicitly labeled
`read_clock`, but production owner reads supply the owner timestamps and the
rehearsal must reject that fallback before serving cutover. The bounded corpus
rehearsal is now green: four viewers, all supported owner families, replay and
out-of-order delivery, withdrawal/rejoin restoration, lens parity and cursor
ordering all pass. Focused evidence is 19 Life unit tests and 24 connected
Life delivery/projector/producer tests (including the corpus rehearsal). The
backend ordering implementation is committed as `a1a0e3632` plus the
public-contract-preserving metadata follow-up `73fe1ebae` on the isolated Life
worktree. This remains shadow evidence only; no serving cutover, Atlas deletion
or production activation is included. The repository-wide size-budget gate
remains a pre-existing failure. The rehearsal's fail-closed `read_clock` guard
is committed separately as `ce12ee3c5`.

Capture supplies source identity, revision, lifecycle and repair events; Life
owns derived indexing. Home/Places consumes exact record destinations, not a
Life-owned generator. Retirement supplies the existing booking-evidence mapping
for R3/R5. Keep the newer Life walkthroughs in the existing W1–W6/design portfolio,
not a competing engine or roadmap; illustrative transitions are not test passes.

### Organization and reader-value investigation — September 7

The [engine design §16](life-organization-and-composition-engine-system-design-2026-09-05.md#16-organization-quality-and-reader-value-investigation--september-7)
now contains the bounded research findings, five executed code probes, W1–W5
grouping/read examples, twelve challenge variants, update policy and B0/B1/B2
comparison protocol. This refines R2-G and R3–R7; it is not a second roadmap
or a completed model/user-quality evaluation.

**New code-backed findings:** the current organization primitive automatically
groups only Plan/Occasion owner rows; source-only periods/episodes and their
useful readers remain to connect. Its owner-containment proposal is typed
`supports_occurrence` even for a Plan without occurrence evidence. Correct that
relation boundary, including stored-row/consumer treatment, before interpreting
memberships as lived evidence. A dark organization group is not an occurrence
owner. The existing W2 fixture's hidden Plan prerequisite was removed and a
validator guard added; separate Plan coverage remains in the broader portfolio.

**Next connected product package:** R2-G source-backed organization together
with R3–R5 bounded group previews/depth and exact originals. Carry source-only
ordinary life, journeys, separate visits, explicit continuity and shared
contributions through the same package; unsupported owner capabilities remain
explicit. Final visual composition stays in Claude Design. Bounded model
assistance is an experiment for supported misses, not a prerequisite for
deterministic organization or a selected new memory framework. R7 evaluates
factual reconstruction and attributed social value separately from AI novelty.

**Parallel engineering acceptance:** reconcile the unmerged Life branch and
finish migration evidence. In particular, a current-row
`legacy_rebuild_required` test does not establish a populated
`lifeorg04` → `lifeorg05` upgrade; that real historical upgrade test remains
open. Research does not authorize merge/push, serving cutover, Atlas deletion
or production activation. Capture supplies exact source/claim references and
repair identities; Life owns derived organization/readers; Integration owns
current delivery. No source-owned transaction or pending intention writer was
changed here.

**Research verification:** five pure-code probes executed; fourteen existing
focused Life backend tests passed. The corrected replay manifest, six fixture
validator regressions, scoped lifecycle metadata, Ruff and whitespace checks
passed. The initial investigation checked 57 relative links across these two
documents, resolving child-repository targets against the canonical workspace.
These results are not measured clustering quality or native usability evidence.
Section 12 records the subsequent implementation plan, not executed product code.

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

### September 5 engine-design refinement

The [Life Organization and Composition Engine system design](life-organization-and-composition-engine-system-design-2026-09-05.md)
now specifies the evolving record behavior and engineering contracts behind
R1/R2 and the organization-bearing portions of R3–R7. It adds six multi-step
scenarios, typed grouping and identity rules, incremental maintenance and repair,
editorial selection, evaluation comparisons, and a later manual-authorship seam.
This roadmap remains the only forward package sequence; the design is not a
second execution status or evidence that those capabilities shipped.

The next phase is system implementation guided by that design, with targeted
experiments for grouping/retrieval quality—not another broad memory-framework
survey. Sections 6 and 9 below point to the next connected batch. User-directed
manual composition is a later extension; protected authorship, source lineage
and version behavior must be preserved now, but a full editor does not gate
the automatic Life engine or Atlas replacement.

### Historical implementation receipt — September 5, 2026

Read the September 6 baseline and §6 for current remaining work. The following
table preserves the first-pass snapshot, including gaps subsequently closed.
The first execution pass has landed in the two child repositories. These are
real replacement seams, not a claim that the complete program is finished:

| Package | Landed | Deliberately still open |
|---|---|---|
| R0 | `/(tabs)/life` is the visible continuity root; legacy Atlas root/deep links redirect; graph/source fallbacks and Life back navigation land in Life; all four lens routes are accepted | Legacy nested readers, producers, tables and API routes still exist behind compatibility paths |
| R1 | Root and depth use one normalized corpus assembly; timeline reads no longer call the Atlas HTTP route; source chronology, source revisions, cursor identity and corpus-fingerprint conflict handling are explicit; depth exposes source revisions; an additive versioned `life_corpus_entries` index, bounded repository keyset reader, strict write contract, idempotent writer, explicit snapshot projector/merge adapter, all-lens batch planner, typed row/record decoder, exact anchor cursor seek, typed indexed record-page reader, and bounded-page continuation comparator now exist | The index is still dark: no owner backfill, incremental fan-out, shadow runtime, or serving cutover exists yet; the route still reconstructs the current snapshot from owner sources and mobile restoration still uses the legacy reader |
| R2 | Trip/memory correction invalidation now includes Life root and depth query families; stale-cursor restart is actionable in the reader; the derived index now has an owner-scoped withdrawal primitive and refuses stale upserts over withdrawn rows; the separate Life outbox now has an identifier-only publisher/repair path and retained-source shadow projector | Broader owner fan-out, semantic-representation withdrawal, incremental index/backfill, explicit reauthorization/restore, and custody/refind invalidation remain |
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
| `efc27308c` | Added `compare_life_index_snapshot`, a deterministic shadow comparator for missing, extra, duplicate, kind, sort-key, and lens-membership differences | It compares only fields the canonical snapshot can prove; owner revision, grants, payload, and lineage remain projector-contract checks |
| `c59697ccb` | Added the strict `LifeIndexProjectionEntry` write contract and atomic, idempotent `upsert_life_index_entries` repository; duplicate logical identities are rejected before opening a transaction | The writer still requires an owner-backed caller; no owner adapter, backfill worker, outbox fan-out, or serving cutover is implied |
| `5d5393fc4` | Added the pure `index_entries_from_snapshot` adapter and `merge_life_index_entries` seam; a lens snapshot can become write entries only when callers provide an explicit record-to-owner-revision map, and repeated lens rows merge by logical identity while rejecting conflicting owner/payload evidence | This is an adapter contract, not an owner read or backfill. It does not infer authority from presentation IDs, populate the index, fan out changes, compare at runtime, or change Life serving |
| `cd5a5f1df` | Added `index_entries_from_snapshots`, which validates unique lenses and one `represented_at` clock before merging the lens-specific entries into one deterministic write batch | This is still a pure planner. It does not schedule a worker, choose owner revisions, persist rows, or imply that all four lenses currently have complete producers |
| `28cc53a5e` | Added typed `decode_life_index_entry` and `decode_life_index_record` boundaries; future readers validate DB mappings against the strict contract and refuse payload identity, kind, or requested-lens mismatches before returning a depth record | Decoder is not authorization, a query, or a route cutover; it intentionally leaves viewer scoping and withdrawal filtering to the repository query |
| `7e9119028` | Added `find_life_index_cursor`, an exact viewer/version/lens-scoped lookup that returns a stable `(sort_at, record_id)` boundary for a live row without scanning the corpus | This enables a future restoration adapter but is not wired into the mobile reader or HTTP depth route; absent, revoked, suppressed, or deleted rows resolve to no cursor |
| `3e4210172` | Added `read_life_index_record_page`, a typed repository wrapper that decodes every bounded row into `LifeRecordEntry` while preserving `has_more` and the keyset cursor | No route uses this reader yet; viewer scoping and withdrawal predicates remain owned by the underlying repository query, and malformed rows fail closed rather than being silently dropped |
| `0f6da7c43` | Added `compare_life_index_page`, which slices the canonical snapshot at the same keyset boundary and compares row parity plus `has_more`/next-cursor metadata | This is a pure shadow policy and test seam; it does not run in production, record metrics, or authorize a serving switch |
| `7b3995c0d` | Added `compare_life_index_viewers`, which applies the bounded canonical-vs-index comparator to an explicit viewer cohort, proves empty non-participant buckets, rejects unexpected viewer buckets, and flags stored rows whose `viewer_id` disagrees with their bucket | This is still a pure shadow/test seam; it does not emit metrics, compare payload/grant parity, or authorize a serving switch |
| `bb836993e` | Added owner-scoped `withdraw_life_index_owner_entries` and a conflict `WHERE` guard so correction/deletion can revoke derived rows and a stale projector cannot resurrect them through an ordinary upsert | No event subscriber or outbox calls this yet; reauthorization is intentionally a separate future command, and source truth remains untouched |
| `647950ede` | Tightened the upsert guard to reject existing `status='revoked'` rows even if legacy data lacks withdrawal timestamps | This closes a monotonicity edge only; it does not add the explicit restore/reauthorize command or connect withdrawal to owner events |

Focused schema, query, repository-reader, projector-contract, and Alembic-chain tests pass (the focused Life index tests cover the table, query, reader, comparator, contract, writer, and projector seams). Repository-wide
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

The versioned Postgres replacement foundation now exists as
`life_corpus_entries` (see the implementation receipts above). Continue that
choice rather than reopening extend-in-place versus replacement. Reuse the
Atlas timeline projector's useful owner adapters, dedupe history and migration
knowledge, but replace its travel-only public contract with Life records.
Preserve existing hide/rename controls and inspect deployed-reader coverage
during backfill design. Retire the old projection after comparison and consumer
migration. This is rebuildable read state, not a new truth owner; its current
existence does not imply population or serving cutover.

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

Implementation detail is in [engine design sections 5–7](life-organization-and-composition-engine-system-design-2026-09-05.md#5-system-boundaries-and-proposed-data-contracts):
typed relations, stable identity, human controls, a durable downstream Life
change journal, revision/authorization publication checks, and rebuild policy.
Its six evolving examples constrain the whole system before model tuning.

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

[Engine design sections 8–9](life-organization-and-composition-engine-system-design-2026-09-05.md#8-from-organized-evidence-to-a-useful-life-page)
distinguish factual records, Vesper synthesis and human-authored compositions.
Exact keep/reopen remains part of this package. A full manual-first editor is
a later extension, not a new prerequisite for R8; source references, protected
authored choices, saved-version validity and repair must already support it.

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

For one founder: finish one connected cross-repo package at a time. Life tab
navigation and the index foundation have landed; do not restart those steps.
The next material delivery connects authorized owner changes to a populated,
repairable shadow index, then extends owner coverage toward serving cutover.
Design grouping, synthesis and later authorship contracts alongside that work
so early storage does not constrain the product. Do not spend the next round
only expanding isolated helper tests or polishing placeholder rows.

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

### Next connected execution batch: owner changes to shadow Life records

This replaces the original navigation/index-foundation batch, whose partial
completion is recorded above. [Engine design section 12](life-organization-and-composition-engine-system-design-2026-09-05.md#12-implementation-units-inside-the-existing-roadmap)
maps the detailed units back to R1–R7; no new package numbering supersedes R0–R8.

The non-regrettable contract portion of this batch is now landed in the
backend/workspace: W1–W6 replay manifests, the owner capability matrix,
revision-guarded publication and explicit restore, an owner-checked shadow
batch, pure replay/race decisions, and a separate downstream Life outbox. The
remaining items below are the connected production work; they are intentionally
not implied by the scaffolding commits.

1. **Behavior and owner contracts — landed:** the replay manifests and
   owner/revision/authority matrix account for retained originals, admitted
   anchors, graph owners, historical Atlas material, shared records and future
   composition custody; unavailable paths fail closed.
2. **Transaction and schema review — landed as additive seams:** the separate
   downstream outbox, owner revision CAS, and explicit restore operation are
   present. The September 6 delivery bridge now adds the after-commit
   `life_projection.ready` handoff, identifier/revision-only
   `life_projection.changed` publication, and minute repair sweep. The
   retained-source Intake transactions now call that bridge and a
   current-authority shadow projector writes or withdraws `life.v1` rows.
   Commit `073d33b9d` extends the same narrow path across semantic
   representation: Experience Graph confirmation emits `source_represented`
   and candidate retraction emits `source_unrepresented` in the owner
   transaction, so the retained-source projector withdraws or restores its
   private shadow row under the exact owner revision. Follow-up commit
   `420176821` makes those withdrawal/restore branches explicit and stale-safe.
   The local `lifeoutbox01` migration is now applied; focused projector/bridge
   tests and 17 PostgreSQL bridge/intake tests pass.
   Commit `a669541b2` then adds the versioned, content-free
   `source-owner-change.v1` envelope to Intake lifecycle events, including
   owner revision, retry identity and source/candidate references. This is a
   contract hardening step only; it does not authorize a Life reader cutover.
   Existing owner transactions still need to call the outbox only after their
   own authority/revision contracts are reviewed; no broader owner projector
   or serving cutover is implied.
3. **Connected shadow population — next:** wire source-custody and eligible
   owner changes through owner-backed projectors into the existing versioned
   index. Do not compete with the intake bridge for the same single-ack outbox
   events or infer authority from a presentation ID.
4. **Replay, repair and coverage — partially landed:** pure stale/restore/race
   decisions and scenario expectations are executable; production replay,
   paged backfill, fan-out, and shadow comparison of payload, grants,
   dependencies and coverage remain.
5. **Reader integration after coverage:** retain actual owner destinations,
   bounded restoration and current authorization at read time. When transports
   change, sync OpenAPI via `scripts/sync-types.sh` and update root/depth/mobile
   consumers together. A first connected adapter does not authorize a whole-
   corpus serving switch.

Existing regression homes to extend: backend `tests/life_projection/`,
`tests/life/`, `tests/api/test_root_projections.py`; app
`__tests__/components/LifeRootV1Screen.test.tsx`, `LifeRecordScreen.test.tsx`,
`__tests__/components/nav/FloatingTabBar.test.tsx`,
`__tests__/utils/resourceDestination.test.ts`, `productSystemRollout.test.ts`,
and `lifeReadingPositionStorage.test.ts`. Add PostgreSQL integration cases for
query/migration behavior and preserve historical test evidence separately.

The first connected portion is complete when an authorized owner transition
reliably produces a correct shadow Life record and repair survives replay and
concurrency. The current commits stop before that producer/worker connection;
record remaining owner coverage explicitly as it lands. Serving cutover still
requires whole-corpus coverage, measured bounded access, current authorization,
and matching generated consumers. This does not complete digest, Together,
Returns or retirement. Avoid a calendar estimate until the delivery/owner
contracts and migration shape are reviewed.

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

The [engine system design](life-organization-and-composition-engine-system-design-2026-09-05.md)
owns the detailed proposed grouping, maintenance, synthesis and later authorship
contracts within this sequence. Promote accepted enduring contracts into their
canonical homes during implementation; keep empirical thresholds labeled as
experimental until evaluated. Documentation progress is not runtime completion.

R0 must reconcile the app Life surface contract, August 12 retirement decision's
old IA, personal-memory compatibility charter, current-state page and machine
compatibility registry with the Life-only target. Preserve historical decisions
as provenance; current product architecture is the four-root contract.

Update package status with code references and bounded evidence after each
delivery. Record partial packages as partial. A passing helper test, mock board,
generated schema or smoke flow never substitutes for the package exit behavior.

### R1/R2 owner-change delivery package — 2026-09-06

**Consumer side and first owner adapter landed.** The Life lane now consumes
the existing `life_projection.ready` → `life_projection.changed` bridge
(`travel-agent` `b4d87161f`) through
`backend/life_projection/delivery.py`. It validates viewer scope and owner
metadata, re-reads current authority at one clock, derives all four lenses
through the existing corpus builder, filters unavailable owner families, and
persists to the existing shadow index with revision-CAS. The retained-source
adapter (`77d4a8474`) handles its own narrow current-owner read, producer
handoff, withdrawal tombstone, and explicit restore CAS; the generic consumer
skips it to avoid duplicate writes. Ordinary replay cannot restore withdrawn
rows; stale/out-of-order revisions converge safely. The worker remains the
already-landed `backend/workers/life_projection_jobs.py`; no second worker or
outbox was created.

The owner-private Plan adapter now follows the same path for canonical Plan
create/update/lifecycle mutations in `travel-agent` commits `7b6e97d7f` and
`f12dca534`. Plan remains shadow-only and does not add loose intention or
shared arrangement material.

Focused local evidence is 103 passing Life/bridge/worker tests across the new
consumer, retained-source adapter, current authority, CAS/withdrawal/restore,
bridge, propagation, and worker suites. The package does not claim full owner
coverage, indexed serving, PostgreSQL transaction evidence, production
activation, or Atlas retirement. Graph owners must still call
`register_life_projection_propagation` from their own transaction with
`payload.viewer_ids` and (when available) an aware `represented_at`; the exact
contract is recorded in
[`life-owner-change-delivery-handoff-2026-09-06.md`](life-owner-change-delivery-handoff-2026-09-06.md).

The combined focused Life/Plan/Occasion evidence now passes 60 tests, including
PostgreSQL producer/projector proofs and retained-source worker repair.

**Historical next checkpoint (superseded by §10):** define the Outcome shared-audience/revocation contract
before adding an Outcome producer. The pure resolver and content-free
event-envelope seam now land in `travel-agent` commits `134bb021b`, `4ef82cce8`,
and `9aa75ff3d`; canonical event fan-out, erasure propagation, the separate
audience/content CAS dimension, shadow projection, and owner-matrix evidence
remain. Review the [Outcome audience CAS proposal](life-outcome-audience-cas-decision-proposal-2026-09-06.md)
before changing the index writer. Keep serving cutover and unsupported owners
gated until whole-corpus coverage, repair, authorization, and destination
evidence are complete.

## 10. Design-independent execution plan — September 6

> **Status note — September 7:** implementation packages for R1/R2-A through F
> have landed in the current backend line; their complete exit conditions have
> not. Section 11 records the remaining connected implementation and evidence.
> The sections below serve as acceptance, race, and coverage checklists. Do
> not re-implement a landed package because an older paragraph still describes
> it as future work; record only the remaining evidence or owner gap.

### 10.1 Objective, scope, and inspected baseline

Build the system that makes existing and newly contributed experience reliably
available to Life while Claude Design refines presentation. A person should be
able to find old material, see later contributions in the appropriate historical
context, and keep their corrections through subsequent updates. This batch
advances the whole-corpus replacement; it is not a request to reduce Life to one
behavior loop or wait for every screen to settle.

Planning baseline: backend local `main` includes Life shadow delivery and the
September 7 coverage, temporal-admission and venue-fact corrections through
`21f2e3085`; app `38d3a6521` includes lens/refind-destination continuity. The
execution receipt records the package commits and focused evidence. Any
isolated worktree named in the historical receipt is not a current execution
base. Test descriptions below are acceptance evidence still required where the
receipt does not provide it; they are not implied by a passing helper test.

| Area | Code observed | Implication for this plan |
| --- | --- | --- |
| Owner delivery | `retained_source_projector.py`, `plan_projector.py`, `occasion_projector.py`, `outcome_projector.py`; graph owner event modules; separate Life outbox and worker | Extend the existing path. Do not recreate the old generic whole-corpus consumer. |
| Audience repair | Outcome projection `ba9463c2a`, encounter membership repair `fd66f9f1f`, erasure fixes through `68e72d3f7` | Reconcile tests and owner declarations before scheduling work already landed. Shared Outcomes do not establish a generic friend-note owner. |
| Capability declaration | `owner_contracts.py` exposes only the owner scope proven by current adapters | Keep unsupported families explicit; update coverage from evidence, not from registration alone. All current families remain shadow-only. |
| Publication | `index_writer.py` supports content-revision CAS, optional dependency CAS, withdrawal, explicit restore and replay-safe outcomes | Run the remaining PostgreSQL first-insert, withdrawal/restore, audience and lease interleavings; do not infer safety from helper tests alone. |
| Historical population | `life_projection_jobs.py` provides bounded, resumable population and repair with durable checkpoints | Run it against an explicit local corpus/viewer cohort and account for every item; event repair alone does not prove untouched history is covered. |
| Comparison | `index_compare.py` compares identity, kind, sort, lens membership, typed fields and page continuation | Produce a machine-readable report for the rehearsal, including content, authority, dependencies, destinations, coverage stage and unsupported/blocked rows. |
| Serving | `root_projections.py::_read_life_snapshot` still fans in graph, Intake and Atlas owners | Keep this serving path during shadow work. A first backfill is not a reader-cutover certificate. |
| Mobile | `LifeRootV1Screen.tsx`, full-record reader, refind and reading-position utilities exist | Extend their behavior against stable contracts; final editorial composition can proceed separately. |

### 10.2 Dependencies on design and adjacent lanes

Proceed now with identity, time semantics, owner-based authorization, durable
delivery, bounded history reads, checkpointing, repair, comparison and direct
navigation contracts. None depends on the final wording of the pasta Return,
Maya comparison, or the ordering of visible dossier sections.

Organizational controls can be specified against the existing engine design;
their persistence/schema and command contract must be reviewed before implementation.
The exact grouping policy and consumer treatment of splits remain subject to
the existing design decisions. Start deterministic explicit relationships first.

| Lane | Exact interface needed | Life responsibility / fallback |
| --- | --- | --- |
| Capture | Exact retained-source identity/read, current custody and representation state, canonical revision, expiry/deletion/unrepresentation semantics | Reuse its readers/events. Agree any missing exact-read or publication-fence contract before changing source-owned transactions. Original retrieval must not wait for Life organization. |
| Plan / Occasion / Outcome owners | Exact owner reads; current and departed eligible viewers; content and audience revision semantics; bounded enumerators; restoration authority | Implement derived consumers and owner-specific reconciliation. Unsupported scope stays explicitly incomplete rather than guessed. |
| Integration | Durable Life delivery completion semantics, shared dependency/repair envelope, checkpoint schema review where needed | Reuse the existing Life queue and worker conventions. Do not claim Intake's upstream acknowledgement or introduce a competing generic indexing service. |
| Entities | Canonical resource handles and exact destinations | Reuse them for Place/person/source context; Life does not re-resolve entities or redesign their pages. |
| Home / Places | Exact record handles, current eligibility, return context and invalidation targets | Supply stable reads and destinations. No separate Life generator or dependency on opening Life for the live engine to operate. |
| Retirement | Retained booking/legacy evidence mapping and obligations inventory | Inventory and preserve access; no deletion simply because another owner backfills successfully. |
| Claude Design | Selected detail/section composition and remaining P1–P4 decisions | Consume semantic fixtures while code foundations advance; do not hard-code fixture prose into production. |

Pre-Plan intention custody, a generic social-contribution owner, authored
composition custody/editor, and kept-path retention remain outside the immediate
batch. They block their own capabilities, not existing owner coverage.

### 10.3 Execution order and reviewable commit packages

These packages refine R1/R2 and then R3–R5; they do not create another roadmap.

| Commit package | Scope | Exit condition |
| --- | --- | --- |
| R1/R2-A | Reconcile owner coverage and reproduce delivery/publication gaps | **Landed in part;** current owner/event matrix is evidence-backed, with remaining gaps named rather than claimed complete |
| R1/R2-B | Correct publication ordering and durable delivery accounting | **Landed in part;** focused CAS/replay protections exist; PostgreSQL interleavings and any remaining owner fences are the exit evidence |
| R1/R2-C | Exact owner readers, paged enumeration and shared materialization seam | **Partial;** bounded exact-owner readers exist; connect eligible lens materialization and verify incomplete reads across the direct event path |
| R1/R2-D | Resumable backfill, version targeting and operator controls | **Landed;** run against an explicit cohort and account for every enumerated item before treating population as operationally ready |
| R1/R2-E | Concurrent catch-up and repair of disappeared/viewer-removed records | **Partial;** single-owner reconciliation exists; bounded corpus traversal, unresolved-work recovery and catch-up evidence remain |
| R1/R2-F | Full shadow comparison and coverage report | **Landed as tooling;** produce and review the first complete report, with unavailable owners visible as gaps |
| R2-G | Deterministic organization, identities and durable correction controls | W1–W5-supported relationships survive late arrival, rebuild, rename/detach/split within accepted authority |
| R3/R4/R5-H | Mobile record access, refinding and return continuity | Same supported object opens through every entry path with honest state and restored context |

The immediate work has two tracks inside the Life lane: connect and rehearse
A–F using §11, while advancing R2-G's organization/control contract and accepted
deterministic implementation. R3/R4/R5-H exact retrieval can proceed against
stable handles. Organization need not wait for every unsupported owner family;
only dependent behaviors wait on a missing owner. UI reads do not trigger organization. Each
package ends with explicit-file commits and updates to this roadmap and the
execution-status receipt. No production activation, serving cutover or Atlas
deletion is included until its separate gates pass.

### 10.4 R1/R2-A and B — close publication gaps before historical fan-out

First reconcile owner declarations across create, content update, representation,
membership/visibility change, expiry, withdrawal, erasure and explicit restoration.
Distinguish code presence, focused tests, database evidence and serving eligibility.
Audit worker registration as well as producer calls. Confirm the current branch
and test changes before editing anything in a concurrent lane.

The inspected code warrants these concrete tests:

1. **Old content overwrites new content:** worker A reads owner revision 1;
   worker B publishes revision 2; A then reads index revision 2 and uses it as
   its expected CAS token while publishing the revision-1 payload. Plan and
   Outcome currently read authority before index state. Equality against that
   later index read alone does not bind the draft to current authority.
2. **First insert after withdrawal:** A reads an eligible owner, which is then
   deleted/revoked before A inserts an index row that never existed. An existing
   row's tombstone cannot protect this case.
3. **Old withdrawal after restoration:** withdrawal currently updates an owner's
   index rows without an expected revision/dependency predicate. Interleave it
   with a new authorized restoration and check the final state.
4. **Audience-only change:** hold the content revision fixed while membership
   changes. Both the content token and the audience/dependency token must guard
   publication and re-entry, including account erasure.
5. **Successful write, lost acknowledgement:** replay after writing a row but
   before acknowledging the event, including restoration and partially completed
   multi-viewer delivery. Repeated restoration must be idempotent under the
   current owner contract, not a permanent retry or automatic authorization.
6. **Missing consumer / failed acknowledgement:** `emit_and_wait` returns true
   with no subscribers, while the Life publisher currently ignores the boolean
   result of `mark_life_projection_event_published`. An event needs evidence
   that its intended owner consumer handled it; unrelated subscribers do not
   establish completion. A failed lease acknowledgement must not count as published.
7. **Expired lease / process restart:** the old claimant cannot mark another
   claimant's work complete; lease expiry/reclaim cannot make stale publication
   safe merely because an event was once claimed.

Implement the narrowest shared publication contract that covers these cases.
Preferred direction: prepare content outside long transactions; within a short
publication transaction validate/lock the relevant canonical owner and audience
generation, validate the observed derived-row state, then apply the write or
withdrawal. Include missing-row protection. Reuse owner repositories and current
CAS helpers; agree any owner-side locking/generation seam with its lane. Merely
reordering two independent reads or adding another Python check is insufficient
for all cases. Establish a consistent lock order to avoid deadlocks.

Separate the current authorization clock from historical event/occurrence time.
Delayed events and backfill must evaluate expiry at current authority, while
preserving original time metadata. Never compare opaque revisions lexically.

Retain the existing Life outbox. Strengthen its completion contract locally
without silently changing semantics for unrelated event-bus users. A stale hint
can be acknowledged as obsolete only when current state is safely represented or
durable newer/reconciliation work accounts for it. Return explicit outcomes such
as applied, withdrawn, already-current, obsolete, retryable, unsupported and
terminal-error; a submitted write count is not proof of successful publication.

### 10.5 R1/R2-C — bounded reads and one projection path

Reuse the retained-source exact read. Plan/Occasion/Outcome currently call
`get_experience_projection` and select their target from the returned graph.
That repository is unbounded by default; simply adding a preview limit would
make a missing target ambiguous and could cause erroneous withdrawal.

Introduce or reuse owner-local exact lookup and paged enumeration contracts:

- Enumerate stable owner IDs with a keyset cursor and an explicit continuation.
- Read a named owner with the authority dependencies needed for this viewer.
- Distinguish eligible, authoritatively absent/ineligible, and unknown/incomplete/error.
- Page large viewer sets and dependency sets independently of owner enumeration.
- Resolve a current build input with content revision, audience/dependency tokens,
  time roles, represented/source/owner refs and current status.

Share that input-to-entry builder and guarded publication between live events,
backfill and repair. Extract only repeated owner projection logic; do not build
another all-history compiler or use a root GET as the worker's data source.
Thread a configured target projection version through the materialization seam;
current helpers often default to `life.v1` and cannot implicitly populate a
different rebuild version.

Cover all eligible lens memberships of an owner in its one stored record.
Several current builders begin with a Time snapshot; audit actual lens output
before claiming four-lens parity. No unsupported owner or missing lens may be
silently filtered out of the coverage denominator.

### 10.6 R1/R2-D — resumable historical population

`life_projection/backfill.py::run_life_projection_backfill` and
`workers/life_projection_jobs.py::run_life_projection_backfill_job` now provide
the bounded runner and worker entry. The run/checkpoint repository is
`core/db/life_projection_backfill.py`; `lifebackfill02` added its table. Reuse
them. No standalone Life operator CLI or complete rehearsal driver was found
in this inspection. Section 11 uses the existing pytest infrastructure for the
first local executable packet. The requirements below remain acceptance criteria.

The runner requires explicit viewer/cohort scope, owner families, target shadow
version, page size and work budget. Default to a dry-run inventory; writing must
select a shadow version explicitly. Do not enumerate the entire user population
or run against production as an incidental local test.

Persist a checkpoint with:

- Run identity, selected scope, target version, code/policy version and status.
- Per-owner enumeration cursor and any owner-supported replay boundary.
- Viewer/dependency continuation where one item fans out to many recipients.
- Durable unresolved work identities and retry/error classifications.
- Applied, already-current, withdrawn, deferred, unsupported and failed counts.
- Last completed unit and lease/ownership evidence for concurrent runners.

The existing `life_projection_backfill_runs` table owns progress only. Use its
lease and checkpoint operations; do not introduce another checkpoint table or
move this system job into a user-facing workflow. Missing retry/reconciliation
state must first be assessed against its existing checkpoint and unresolved-work
fields before proposing a schema change.

Advance a page checkpoint only after each item is applied, confirmed current,
or durably assigned unresolved work. A crash after row commit but before progress
commit must replay safely. An unsupported owner can be recorded as a known gap,
but cannot make a whole-corpus run complete.

A separate target version prevents rebuilding from mutating a served version.
The version-routing design must also account for live changes while a build is
active: use the existing Life delivery path with explicit durable work for each
active target, or a replay journal with independent persisted offsets. A single
global published flag cannot stand in for delivery to several build versions.
Choose and record the narrower implementation in the schema/transaction review;
do not start an orphaned shadow version that stops receiving changes.

### 10.7 R1/R2-E — catch-up and reverse reconciliation

Scan historical owners, process subsequent changes, then verify current state
through both directions:

1. Owner → index finds missing or outdated derived records.
2. Index → current owner finds deleted owners, removed viewers, superseded
   representation, and obsolete identities no longer emitted by enumeration.

Compute the affected viewer set from current authority plus prior derived
recipients, using the owner contract for which former recipients must lose access.
Only scanning current members misses the people who left. Never infer revocation
from an incomplete or failed read. Historical Atlas is a separate migration family
with its own eligibility and retained-source mapping, not a new incremental owner.

Use owner-supported ordering and a demonstrated catch-up protocol. Timestamp
alone, a random UUID cursor, or a sequence allocated before commit is not proof
that every concurrent committed mutation was observed. A late commit can fall
behind an apparent boundary. Where no commit-safe replay boundary exists, record
that limitation and use durable overlapping reconciliation/dirty tracking until
it can be certified; do not call one pass a global snapshot.

The Life publisher prunes published events after seven days by default. A build
must not depend on replay data that can expire underneath it. Bound replay retention
to active build checkpoints or choose the durable per-target work approach above.
A missing replay interval requires a new reconciliation pass, not guessed progress.

Repair must honor current custody and explicit restoration generations. Repeated
ordinary scans cannot restore material simply because an old source is still
physically present. Preserve tombstones and rejected memberships as applicable.
Do not mass-delete unmatched rows on the basis of a partial backfill.

### 10.8 R1/R2-F — comparison and coverage report

Extend `index_compare.py`; retain its existing bounded-page checks. Separate:

**Structural parity:** identity, unique count unit, kind, time basis, ordering,
lens membership, cursor/has-more and exact position restoration.

**Typed projection parity:** expected owner-derived entries versus stored entries,
including viewer/version/owner identity, content revision, authority/dependency
token, represented and source refs, grants, lineage, payload, exact destination,
status/lifecycle and withdrawal state. Normalize only declared unordered fields
and incidental write timestamps. Do not sort content whose order has meaning or
ignore differing claims just to make a report green.

**Coverage:** inventory every family separately as incremental, backfilled,
reconciled, compared, unsupported, or blocked. Include retained originals,
represented anchors, Plans, Occasions, Outcomes, historical Atlas material and
any commitments emitted by the canonical corpus. Matrix omissions are findings.
Generic social contributions and authored compositions remain unavailable until
their own owner contracts exist.

Compare at matching owner/authority revisions. Concurrent drift is an explicit
retry/inconclusive result, not an equality failure to ignore. Keep per-record
revision evidence; a shared wall-clock label does not create cross-owner consistency.

The legacy serving snapshot is one comparator, not the complete product oracle.
For example, its `my` graph mode and newer shared Outcome projection can have
intentionally different populations. Record owner-contract expectations and
classify intended additions separately from regressions. Validate selected
source-level facts independently to avoid two consumers sharing the same builder
bug and appearing equal.

Emit a machine-readable report plus a concise operator summary: examined scope,
versions, revision basis, coverage, missing/extra/mismatched rows, stale-viewer
findings, unresolved work and actual timing/query measurements. Logs should use
opaque references and field-level classifications rather than raw private content.

### 10.9 Verification portfolio for the first connected batch

Use the existing `tests/life_projection/`, core outbox/propagation tests and
worker tests. Extend PostgreSQL fixtures for actual transaction behavior; mocked
CAS calls cannot establish concurrency safety. Use local tests, with model/API
calls and device testing deferred for this batch.

Required scenarios:

- Untouched historical originals, an ordinary local occasion, an owner-private
  Plan, and private/shared Outcomes populate from enumeration.
- Repeated pages/events and restart at each checkpoint do not duplicate records.
- Mutations during enumeration, including backdated insertion and a transaction
  committing behind a traversal boundary, eventually appear.
- Old content, audience changes, first insert, withdrawal, restoration, failed
  acknowledgement and lease reclaim exercise §10.4's interleavings.
- A departed/erased viewer loses dependent rows while independent records remain.
- Source expiry and represented/unrepresented transitions retain exact-original
  access only where the source owner permits it.
- More records/viewers/dependencies than one page drain completely without
  lifetime-history reads or accidental omission-based withdrawal.
- Payload, destination, source/grant/dependency and time mismatches are detected
  even when IDs/order match.
- Unsupported owner families and missing replay intervals prevent a false
  completion certificate.
- Comparison reads themselves do not create Atlas rows, perform generation,
  change canonical owners, or count as user activity.

Run focused suites and repository-required checks for touched code, then record
exact commands and counts. Classify additive checkpoint schema/publication-owner
changes under the repository's schema/architecture review rules. Follow workspace
schema export/type-generation workflow if public models/routes change; internal
worker-only changes do not require invented public endpoints. Before migrations,
check the actual Alembic head and preserve a single lineage.

First-batch exit: supported owners have bounded, restartable historical population
and live reconciliation; concurrency regressions pass locally; the comparison
report accounts for the full declared cohort and identifies every remaining
family gap. Serving stays on the existing reader. R8 requires additional complete
owner coverage, read-time authorization, measured access, mobile acceptance and
an explicit release decision.

### 10.10 R2-G — organization and durable human corrections

Proceed from the system-design D2–D7 and W1–W5 contracts. Index population by itself
does not create good episodes, place relationships, or attention threads.

First specify and review the minimal persistence delta for stable group identity,
membership with supporting refs/revisions, alias/split resolution, and durable
human controls. Reuse existing canonical owners for journeys and Occasions;
derived organization cannot mutate their participants, plans, audience or sources.

Implement deterministic explicit containment and time/place relations before
learned clustering. Separate occurred/captured/authored/imported/planned time;
`updated_at` is a revision clock, not occurrence evidence. Source-only and undated
items are valid final states. A September import can update August without moving
September's rows. Preserve exact links even when optional similarity work is capped.

Implement scoped rename, detach-with-exclusion, and accepted split/merge behavior
with revision-bound commands, readback and valid Undo. Persist these choices so
rebuilds cannot erase them. Keep old links resolvable with no automatic first-child
choice where ambiguous. Translate natural language through existing contextual
Chat/owner commands; do not build another Life chat or correction inbox.

Reproject only affected memberships, counts, search/destinations and dependent
content. Model-assisted relation proposals remain bounded and optional; they
cannot grant authority, establish attendance, or rename authored material.
No new model experiment or generated Return is required for custody and repair
to function. Calibrate ambiguity on W1–W5 before proposing automatic broad joins.

### 10.11 R3/R4/R5-H — mobile work that can proceed during visual refinement

Audit the current root, full-record reader, `useLifeRefind`, resource destination
resolver, query keys and `lifeReadingPositionStorage` against the selected design
semantics. Reuse existing components and return envelopes. Concrete work includes:

- Direct chips/search results and exploratory rows reaching the same object.
- Lens/query/row identity and offset restored after opening details, account
  switching, and app restart; bounded fallback when the row disappears.
- Original-source access distinct from the full organized history. The current
  root archive control routes to the full-record reader; do not relabel that
  route Everything kept without implementing the corresponding source access.
- Explicit Life search scope, accurate unsupported destinations, partial results,
  and no silent disappearance/count mismatch when a record cannot open.
- Loading/error/offline behavior that preserves usable prior content and the
  root's navigation anatomy, with no fabricated completeness.
- Contextual correction and source-owner handoffs using accepted commands;
  invalidate both root and depth after durable change.

Backend transport changes must update generated mobile types in the same package.
Use focused component/navigation tests while native testing remains deferred;
carry device accessibility, touch, cold-start and visual checks to the release
checkpoint. Final section order, editorial copy and illustration treatment can
land after the Claude pass without changing canonical object identity.

### 10.12 Solo-founder sequencing and first action

The next code action is §11's corpus/expectation fixture and connected rehearsal
driver using the existing functions. Pin the integration baseline, inventory
the isolated local corpus, then populate and reconcile its shadow rows in a
separate writing run before producing the comparison report. Inventory alone
does not test materialization. Reproduce the
remaining publication cases (first insert after withdrawal, withdrawal versus
restore, audience-only change, lost acknowledgement and lease reclaim) in
PostgreSQL where evidence is still absent. Every result must be classified as
fixed, unsupported or blocked; a helper test or empty corpus is not a completion
certificate.

In parallel, prepare the minimal R2-G organization/correction contract and
implement only deterministic, evidence-backed containment and revision-bound
human controls. Keep it downstream of canonical owners and use the same index
projection seam. R3/R4/R5-H retrieval work may proceed when it consumes stable
handles, but it must not trigger organization or indexed serving.

Use a fresh isolated `codex/` worktree for code packages based on the verified
integration baseline. Do not reset or rebase concurrent work blindly. Commit
explicit files only. Coordinate proposed owner/schema changes through the
existing register; continue consumer, comparison and organization work when an
owner seam is unavailable, recording the exact dependency.

At each package close, record implemented scope, test commands/results, known
coverage gaps, schema/API impact and the next checkpoint in the existing roadmap
and status file. Keep R7 content production and R8 cutover explicit downstream
work; neither a passing shadow comparison nor a polished design silently enables
them. Estimate later work after the rehearsal classifies concrete owner,
publication and organization gaps.

## 11. Bounded shadow rehearsal execution packet — September 7

Status: rehearsal foundations executed; bounded population, replay, restore and
race evidence are now green on an isolated local database. This section
operationalizes
R1/R2-A–F and the parallel R2-G contract within the existing roadmap. The outcome
is a reproducible local corpus whose supported records remain correct through
population, owner changes, repair and retrieval. User-visible organization is
a separate acceptance track over those same records.

### 11.1 Inspected code and remaining connections

Inspection base: backend `3f7e25da6`, mobile `c8d88437f`, workspace `3b98c52`.
Concurrent Integration commits can advance these independently. Record actual
SHAs and dirty-file scope when execution starts; use an isolated backend
`codex/life-shadow-rehearsal-2026-09-07` worktree for implementation.

| Existing component | What the code currently establishes | Remaining connection or test |
| --- | --- | --- |
| [Backfill repository](../../travel-agent/backend/core/db/life_projection_backfill.py) | `create_life_projection_backfill_run`, claim/advance/pause/finish operations, persisted scope and unresolved work | Database tests for restart, stale leases, counter recovery and unresolved-item retry; `completed` alone is not parity |
| [Backfill runner](../../travel-agent/backend/life_projection/backfill.py) and [worker](../../travel-agent/backend/workers/life_projection_jobs.py) | `build_life_backfill_event`, bounded `run_life_projection_backfill`, explicit `run_life_projection_backfill_job` | Fixture/report wiring and a connected writing run now exist; successful owner retries remove resolved identities from live unresolved work (`d062d1810`), and transient enumeration failures retain their cursor for retry (`f9b687055`). Paused-run persistence and the broader retry/lease matrix remain follow-up evidence. Dry-run still creates/updates control rows but does not materialize corpus rows |
| [Owner enumeration](../../travel-agent/backend/life_projection/owner_reads.py) | Paged Plan/Occasion/Outcome/source identities and exact-owner dependency limits | Timestamp/ID traversal is not a commit-safe snapshot; test behind-cursor mutations, broad candidate eligibility and dependency truncation |
| [Owner projectors](../../travel-agent/backend/life_projection/plan_projector.py) and [lens adapter](../../travel-agent/backend/life_projection/index_projector.py) | Four owner projectors with fences; reusable multi-snapshot merger exists | `index_entries_from_all_lenses` now derives eligible memberships at one represented-at clock; Plan/Occasion/Outcome no longer silently write Time-only rows. Canonical ordering now carries owner-time precision through the index (`a1a0e3632`). Retained sources remain Time-only until place/people evidence is owned |
| [Reconciliation](../../travel-agent/backend/life_projection/reconciliation.py) | `reconcile_life_owner` compares/repairs one supplied owner and requires explicit absence evidence | `enumerate_indexed_life_owners` and `reconcile_life_owners` now provide bounded keyset discovery, including withdrawn rows and unknown-family classification. The viewer-only `read_life_index_owner_rows` overload remains unsuitable for corpus traversal |
| [Comparison](../../travel-agent/backend/life_projection/index_compare.py) | Structural, bounded-page, viewer-bucket and typed-entry comparisons | Assemble independently expected entries and database rows at matching revisions; invoke typed comparison separately per viewer/version because its identity key is `record_id` |
| [Coverage](../../travel-agent/backend/life_projection/coverage.py) | `LifeCoverageReport` and one stage per owner family | Coverage now rejects empty/partial denominators; `backend/life_projection/rehearsal.py` and the opt-in pytest writer emit `vesper.life-shadow-rehearsal.v1` evidence with non-production/serving gates |
| Existing PostgreSQL suites | Owner mutation, audience removal/rejoin, erasure and retained-source restoration examples | Reused and extended with a deterministic two-connection owner-commit/publication race; broader audience/lease interleavings remain in the matrix |

Further code observations to reproduce before changing behavior:

- `unresolved_work` is copied into each run slice and appended to, while completed
  cursors are skipped. A repaired item needs an explicit retry/readback/removal
  path; simply calling a paused run again may retain unresolved work forever.
- Backfill treats zero projector counters as already current. Require readback
  to distinguish idempotence, suppressed/represented material, unsupported work
  and a missing write. An authoritatively ineligible enumerated source is a
  resolved exclusion, not endless retry work; an unavailable read is unresolved.
  Likewise, do not infer completeness from raw counters.
- Enumeration errors currently become `enumeration_unavailable` and mark a
  family cursor done. A transient database/read error must remain retryable and
  distinguishable from an unsupported owner; exercise this through real resume.
- Backfill rejects truncated graph reads, but direct projector delivery needs
  its own incomplete-read cases. Missing entries from incomplete reads cannot
  establish withdrawal.
- Owner fences, source eligibility and event clocks must agree at publication.
  Test expiry during a paused projection and events carrying historical clocks;
  advancing the request clock must not preserve expired source use.

These are implementation observations and regression targets, not fresh test
results. Fix only failures demonstrated by the connected cases.

### 11.2 Fixture corpus, independent expectations and scope

Use an isolated local PostgreSQL database named
`vesper_life_rehearsal_20260907`, with the current migration head. Existing
pytest setup deletes matching test-place rows and existing repair jobs claim
global due work, so a shared development database is unsuitable for this run.
No provider, model, Redis worker process or native app is required: call the
registered worker functions in-process against the real database.

Implemented rehearsal files (the fixture remains test-only and is not a source
of owner truth):

- `tests/life_projection/fixtures/shadow_rehearsal_v1.json`: bounded viewer,
  owner-family and W1–W6 scenario manifest.
- `tests/life_projection/rehearsal_support.py`: schema-checked fixture loader
  and scenario identity helpers; it does not replace a production projector.
- `tests/life_projection/test_life_shadow_rehearsal_postgres.py`: connected
  Plan/Occasion population, all-lens projection, withdrawal/restore,
  inventory/reconciliation and report cases.
- `tests/life_projection/test_life_shadow_corpus_postgres.py`: connected
  four-viewer/four-owner corpus rehearsal, bounded resumable backfill, durable
  out-of-order Plan delivery, Occasion/Outcome withdrawal and explicit rejoin
  restoration, plus lens parity reporting.
- `tests/life_projection/test_life_shadow_races_postgres.py`: deterministic
  publication race with a separate owner-commit thread and bounded barriers.
- `tests/life_projection/conftest.py`: opt-in report option/writer; a test
  abort emits an inconclusive envelope rather than leaving a false green gap.

Four primary viewers: A (owner/host), B (participant who later leaves/rejoins),
C (Occasion member outside a particular Commitment), D (unrelated viewer).
Keep all four comparison buckets, including D's intentionally empty bucket.
A separate erasure case may create a disposable fifth actor so the baseline
cohort remains comparable after destructive fixture transitions.

Baseline corpus has seven canonical records in each supported owner family:

| Family | Required fixture mix | What independent assertions establish |
| --- | --- | --- |
| Plan | Five A-owned and two B-owned Plans; ordinary local and travel contexts; planned/completed/cancelled states where supported | Owner-private visibility, canonical state, exact identity; a Plan or elapsed date does not prove attendance |
| Occasion | Seven A-hosted occasions with explicit varying membership of A/B/C | Common record follows current membership; one evening does not need a Trip; participant changes do not rewrite private source custody |
| Outcome | Two private, three shared Commitment Outcomes, two shared Encounter Outcomes | Private meaning stays private; Commitment audience is participants plus its owner, not every Occasion member; separate accounts remain attributable |
| Retained source | Five A-owned and two B-owned eligible originals: ticket, photograph, note, reading, ordinary local material, an old import and undated material | Original remains findable, time roles stay distinct, retention creates neither attendance nor a compulsory group |

Seven per family is the fixture inventory, not an asserted visible-row count.
Declare exact eligible identity sets for every viewer and transition separately.
Add four source controls beyond those 28 records: transient Ask source,
expired source, deleted source and represented source. Their expected eligibility
comes from the source owner; a represented original can remain owner-accessible
while its source-only Life row is withdrawn. Missing anchor index coverage must
stay visible rather than being filled with a duplicate source row.

Use owner-page size 3, per-call work budget 2 and record-page size 3, then repeat
the final read with size 1 and 5. These are test parameters, not product defaults.
Include equal sort times and a page-boundary identity, and put the same material
in two supported lenses without counting it as two distinct corpus records.
Add a separate dependency-boundary test with a deliberately small injected cap
and cap + 1 dependents; measure that the production query still respects its
configured limit. Extra fixture people are scoped to that case.

Map the existing [W1–W6 manifest](fixtures/life-engine/life-engine-replay-v0.1.json)
to actual behavior without treating its symbolic events/revisions as producer
payloads. Use actual owner commands and returned revision tokens:

- W1/W5: original custody, historical/undated placement and ticket truth are
  executable now; complete journeys and anchor-driven attendance repair remain
  named coverage until their owner adapters exist.
- W2: include an ordinary week with source-only records and no Plan. A separate
  Plan fixture exercises prospective authority; do not turn the whole week into one.
- W3: exercise an independently retained reading and corrected evidence;
  Ask alone must not create retained material. Thread formation belongs to G.
- W4: Occasion and shared Outcome cases execute now. They do not certify
  generic friend-note/social-contribution custody by analogy.
- W6: keep authored-composition cases as explicit future contract coverage;
  an expected unavailable result is not implemented authoring.

The coverage denominator includes all eight entries in `LIFE_OWNER_CONTRACTS`,
plus named obligations for Commitments emitted by canonical reads, retained
booking evidence and saved-Place representation. Those obligations need mappings
to existing owners; do not fabricate index owner kinds just to fill a matrix.

### 11.3 Run sequence and reviewable packages

| Commit package within R0–R8 | Work and principal files | Exit evidence |
| --- | --- | --- |
| R1/R2-A/F — executable corpus and assertions | Add the test files above; call current backfill/worker/read/compare functions; produce an initial report | All four supported families and four viewers have declared expected sets; failures identify code gaps, unsupported capability or infrastructure blockage |
| R1/R2-C/D — complete population and lens projection | Extend existing owner projectors/merger and backfill/repository only where the corpus reproduces gaps | Writing run populates supported rows, all eligible lens memberships survive later events, resume works after each durable boundary, unresolved work can converge |
| R1/R2-E — bounded reconciliation | Extend `reconciliation.py` and bounded index repository reads with current-owner absence proof and persisted traversal/retry state where needed | Both directions visit every fixture identity, including removed recipients; late commits converge after catch-up; incomplete reads preserve prior rows |
| R1/R2-B — publication and delivery races | Extend current PostgreSQL suites/fences/outbox tests with deterministic barriers; coordinate any owner transaction correction | Actual committed rows and event/run lease states satisfy §11.4; no missing-consumer acknowledgement or stale restoration |
| R1/R2-F + R3/R5-H — final report and exact reads | Assemble existing comparators, typed decoder and anchor seek; record source-owner destination obligations | Supported scope is explained and correct across every page/viewer/lens; full portfolio gaps remain explicit; documentation records exact commands and results |

Start the G contract work after the corpus/expectations package; it can proceed
while C–F hardening runs. This is one Life lane with independent work, not a
request to create another persistent task. Fix a blocker in the owning package
when found rather than completing all test infrastructure before correcting it.

Detailed execution order inside the rehearsal:

1. Validate local database scope before importing pytest. Verify migration head,
   capture code and fixture revisions, and construct synthetic owners. Register
   the Life bridge/required owner consumers before live mutation tests.
2. Historical case: seed via owner commands with their real transactional
   producers, deliberately defer after-commit delivery in the fixture, and
   inventory using a new `dry_run=True` backfill run. Assert corpus tables are
   unchanged by inventory. Durable run/checkpoint writes are expected.
3. Create a distinct `dry_run=False` run targeting `life.v1`. Call
   `run_life_projection_backfill_job(None, str(run.id))` for bounded slices,
   preserving checkpoints. Do not toggle the inventory run into a writing run.
4. Deliver the deferred and new events through the real bridge and required
   consumers, then the existing repair function for missed delivery. Preserve
   original event/retry identities; do not substitute direct projector calls
   for the producer-to-outbox-to-worker evidence. Direct calls remain useful in
   narrowly isolated race tests.
5. Apply the lifecycle matrix. Enumerate owners and previously indexed
   identities separately. Confirm absence through owner reads/commands before
   withdrawal, and retry revision drift explicitly.
6. After fixture mutations settle, run two complete comparison passes separated
   by replay and restart. This proves convergence for this corpus; it does not
   prove global snapshot semantics or an indefinite replay guarantee.
7. Read every eligible lens and cursor page. Validate typed records, canonical
   destinations and exact anchor seeking, including missing/withdrawn anchors.
   Compare source originals separately from organized record availability.
8. Emit report/JUnit and a brief receipt. Keep explicit unresolved dependencies
   with owning lane and next check. Clean up only run-owned fixture identities;
   retain failed-run diagnostics without raw private payloads.

### 11.4 Lifecycle, concurrency and failure matrix

Use existing sequential PostgreSQL cases as baseline, and add actual
interleavings only where absent. Each race uses separate connections and a
barrier at read/publication or commit/acknowledgement, with both orderings where
relevant. Sleep timing alone is insufficient.

| Case | Required observation |
| --- | --- |
| Old projection vs newer content commit | Revision-1 draft cannot replace revision-2 material; a later replay converges using current authority |
| First insert vs owner deletion/withdrawal | A draft read before removal cannot insert a newly visible row after removal; missing prior index row supplies no exemption |
| Old withdrawal vs explicit restoration | Final row corresponds to the later authorized owner state; ordinary replay cannot impersonate restoration |
| Audience-only update | Unchanged content revision with changed member/participant generation repairs all current and former viewers; C never receives participant-only material |
| Leave/rejoin and erasure | Old audience replay cannot resurrect access; explicit eligible rejoin follows the owner contract; independent surviving history remains |
| Source representation/unrepresentation | Source-only row withdraws and may restore under the explicit owner revision; generic backfill must not recreate a representation duplicate |
| Expiry during projection / delayed event | Current eligibility is rechecked before publication; an earlier event timestamp cannot extend custody or shift occurrence dates |
| Commit before acknowledgement failure | Replayed event produces no duplicate and reaches durable acknowledgement only after the required consumer succeeds |
| Missing or wrong consumer | An unrelated subscriber cannot satisfy delivery; missing intended consumer leaves recoverable work |
| Expired event lease and run lease | Old claimant cannot acknowledge/checkpoint after reclaim; failed failure-reporting under a lost lease cannot overwrite the new claimant |
| Crash after row write, before checkpoint | Resume inspects current state and accounts for the unit without duplication, omission or inflated distinct coverage |
| Error/deferred unit later resolves | Resume/reconciliation retries the exact unresolved identity and removes it only after verified resolution; errors cannot become unsupported completion |
| Commit behind enumeration cursor | Overlapping repair/second enumeration discovers the missed current owner; timestamp cursor alone earns no snapshot guarantee |
| Incomplete owner/dependency read | Prior permitted rows are not withdrawn by omission; exact dependencies remain bounded and the gap is retryable/inconclusive |
| Non-default version control | It remains `historical_shadow_only`; version-less live events update `life.v1`. Exercise this in a separate finite diagnostic, not the maintained rehearsal target |
| Comparator negative controls | Independently alter a copied row's payload, refs, audience token, lens, destination, cursor or viewer bucket; each specific fault is detected |

Where a mutation command does not exist, record the precise unavailable owner
operation. Fixture SQL may arrange commit timing or simulate a disappeared row,
but cannot be presented as evidence that a nonexistent producer works.

### 11.5 Comparison oracle and report contract

Expected identity, audience, truth/time and destination facts come from the
fixture plus current canonical owner reads. Reuse the pure corpus/compiler for
full expected representations while keeping independent assertions for those
facts; comparing a projector's output with itself cannot detect a shared bug.
Do not use a Life/Atlas GET that performs projection maintenance as the worker
or oracle. The legacy serving snapshot is an additional compatibility comparator;
shared Outcome additions relative to `my` mode need declared expectations.

Build one proposed test-report envelope, `vesper.life-shadow-rehearsal.v1`, around
the existing comparison/coverage results. It is a local artifact, not a new API
or database. Minimum fields:

| Field | Meaning |
| --- | --- |
| `run_id`, `fixture_revision`, `code_revisions`, `migration_head`, `not_production_data` | Reproducible run and implementation identity |
| `scope` | Local database label (no DSN), viewer aliases, owner families, obligation list, selected version, page/work budgets and scenario IDs |
| `target_capability` | Existing `owner_fanout_status` plus measured event-delivery evidence; capability declaration alone is not proof |
| `phases` | Inventory, population, catch-up, replay, comparison and retrieval statuses; backfill run IDs and checkpoint/lease outcomes |
| `coverage` | Existing report plus per-family/per-viewer expected, enumerated, eligible, indexed, withdrawn, unresolved and compared identity counts; separate evidence for incremental/backfilled/reconciled/compared stages |
| `comparisons` | Structural, typed, lens/page/cursor and viewer results; exact mismatched field names and opaque identities |
| `cases` | Scenario/race test node, pass/fail/skip, observed outcome, evidence location and any remaining dependency |
| `measurements` | SQL count, largest fetched page, examined owner/dependency counts, slice duration, retries and maximum retained batch size |
| `findings` | `defect`, `unsupported`, `blocked` or `revision_drift`; named owner/next action; repaired findings retain regression evidence |
| `result` | `supported_scope`: pending/pass/fail/inconclusive; `whole_portfolio_complete`: boolean; `serving_ready`: always false for this packet |

Do not print original text/media, SQL parameters, credentials or exception
payloads in the report. Store field-level mismatches and fixture aliases; retain
ordered payload comparisons internally without sorting away meaningful differences.
Counters such as `applied_count` may count repeated writes or several viewers;
derive distinct coverage from actual identity sets.

Acceptance thresholds for this bounded engineering packet:

- All required cases execute; zero unexpected skips, missing viewer buckets or
  undeclared families. Each supported family has nonempty positive evidence;
  D's empty result is an explicitly expected negative control.
- Zero unexplained missing, extra, duplicate, typed, audience, lens or cursor
  mismatches for supported eligible records at matching revisions. Zero
  unauthorized rows visible through the tested indexed reader after repair.
- Zero unresolved supported units after the two settled comparison passes.
  Retry/infrastructure failure is inconclusive, not pass; classify an unsupported
  family without dropping it from the whole-portfolio result.
- Reads honor configured limits plus documented lookahead; no viewer-wide
  unbounded owner-row scan. Use at most 100 slices and a 120-second watchdog per
  connected case initially; hitting either fails/inconcludes with diagnostics.
  These are test hang bounds, not mobile latency or production SLOs. Report
  actual timings and query counts before setting production thresholds.
- Whole-portfolio coverage stays incomplete while anchors, Atlas migration or
  another required obligation lacks implementation, even if supported scope
  passes. No aggregate `ok` flag may mask that difference.

### 11.6 Exact commands and environment boundary

The W1–W6 structure check is available now, from the workspace root:

```bash
make life-engine-fixture-check
```

The following test commands use existing suites. Run from the chosen backend
worktree with the repository virtual environment. First provision the isolated
local database above and set `LIFE_REHEARSAL_DATABASE_URL` to that database.
Before importing tests, export both settings forms so an existing `.env`
cannot select a different database. Run this block in a dedicated shell with
failure stopping enabled; do not print the URL:

```bash
set -e
: "${LIFE_REHEARSAL_DATABASE_URL:?Set the isolated local rehearsal database URL}"
export DATABASE_URL="$LIFE_REHEARSAL_DATABASE_URL"
export RESEARCH_DATABASE_URL="$LIFE_REHEARSAL_DATABASE_URL"
export PYTHONPATH=.
.venv/bin/python - <<'PY'
from sqlalchemy.engine import make_url
from alembic.config import Config
from alembic.script import ScriptDirectory
from backend.core.settings import core_settings
url = make_url(core_settings.postgres_dsn)
assert url.host in {"127.0.0.1", "localhost", "::1"}, "Local database required"
assert url.database == "vesper_life_rehearsal_20260907", "Wrong rehearsal database"
assert len(ScriptDirectory.from_config(Config("alembic.ini")).get_heads()) == 1, "Expected one migration head"
print("Life rehearsal database scope verified")
PY
.venv/bin/python -m alembic heads
.venv/bin/python -m alembic upgrade head
.venv/bin/python -m alembic current
.venv/bin/python -m pytest -q -m 'not requires_postgres and not requires_api_keys' \
  tests/life_projection tests/workers/test_life_projection_jobs.py \
  tests/core/test_life_projection_broadcast.py \
  tests/core/test_life_projection_propagation.py tests/core/test_event_bus.py
.venv/bin/python -m pytest -q -rs -m requires_postgres \
  tests/life_projection \
  tests/domains/experience_graph/test_occasion_life_events_postgres.py \
  tests/domains/experience_graph/test_outcome_life_producers_postgres.py
```

Verify exactly one code head before upgrading; if multiple heads exist, resolve
the integration dependency first. The local database must exist before the
upgrade. Database unavailability can cause current `requires_postgres` markers
to skip: inspect results and require the expected selected cases to execute.
Do not run the broad workspace Postgres target for this packet; it selects
unrelated suites and supplies a shared-database default.

The test driver and report option are now executable as the connected entry
point:

```bash
LIFE_REHEARSAL_OUTPUT_DIR=$(mktemp -d /tmp/vesper-life-rehearsal.XXXXXX)
.venv/bin/python -m pytest -q -rs \
  tests/life_projection/test_life_shadow_rehearsal_postgres.py \
  tests/life_projection/test_life_shadow_races_postgres.py \
  --junitxml="$LIFE_REHEARSAL_OUTPUT_DIR/junit.xml" \
  --life-rehearsal-report="$LIFE_REHEARSAL_OUTPUT_DIR/report.json"
```

The report writer emits incomplete/failure evidence on assertion failure, not
only successful teardown; a missing/truncated report fails the checkpoint.
Run without xdist initially because event subscriber registration and the
cohort are process-scoped. Use synchronous calls or the existing async worker
entry as appropriate, preserving registration and after-commit semantics.

Implementation classification: test fixture/report wiring is `safe-backend`;
runtime fixes remain scoped to Life unless a demonstrated owner/schema contract
changes. Review those through the relevant owner/Integration interface. Only
public model/route changes require the workspace schema/type workflow; this
test report does not. No models, migrations or API changes are proposed solely
to make the rehearsal runnable.

### 11.7 Organization track and interfaces to other lanes

R2-G starts with a concrete persistence/command proposal using system-design
D2–D7 and the current Claude Life P2 scenarios. Specify stable group identity,
typed memberships with supporting revisions, persistent exclusions and rename
controls, and unambiguous alias/split resolution. First acceptance examples:

1. An old Italy photo joins its supported August context without displacing an
   ordinary September week or changing unrelated group IDs.
2. A source stays unplaced when evidence is insufficient; the original remains
   directly accessible without a filing task.
3. An authorized detach or rename survives replay/rebuild; duplicate commands
   are idempotent, stale edits receive current readback, and Undo has an exact basis.
4. A membership/audience change removes dependent presentation while independent
   authored material remains; shared meaning is never synthesized into one voice.

Implement accepted deterministic rules and controls against supported owners
while coverage work continues. Broader learned clustering and saved-composition
editing have their own R7 gates. A test corpus passing A–F does not certify
organization quality, and a missing future composition owner does not block G's
existing-source work.

**September 7 checkpoint:** commit `143c54079` lands the first persistence
slice in the isolated backend worktree. `lifeorg02` now stores stable
viewer/version-scoped group identities, evidence-backed memberships, and
revision-bound rename/detach/Undo controls. The materializer leaves excluded
memberships excluded and updates evidence only when it changes. Plan/Occasion
owner-driven wiring and the accepted alias/merge/split registry now exist; this
is not yet affected-membership reconciliation, broader owner coverage, or
indexed serving. Resolution lifecycle controls now exist, but a replacement or
revocation after a membership transfer is reported for repair rather than
silently attempting to reverse derived memberships without per-relation lineage.

Follow-up commit `a6c21a0ca` closes the command-ledger race: rename, detach, and
Undo now claim their globally unique viewer/version/control key with
`ON CONFLICT DO NOTHING` before mutating any derived group or membership row.
The losing first attempt rereads and returns the committed control result, so a
concurrent duplicate cannot apply a second mutation under a different target.

Commit `29d2a799b` connects that organization seam to the existing Plan and
Occasion owner projectors. A successfully fenced current entry materializes its
owner group/membership; a fenced withdrawal archives the group and marks active
memberships superseded; only an explicit restoration reactivates those derived
rows. Missing current authority on a restore now fails instead of being treated
as a withdrawal. The adapter is injected at the existing event consumer, so no
second queue or Life-owned source transaction is introduced.

Commit `2defe2692` adds the first identity-resolution registry on top of that
seam. Accepted alias/merge/split decisions are evidence-backed, idempotent and
viewer/version scoped; old handles remain resolvable, while a split returns all
active descendants instead of silently choosing the first child. The migration
head is now `lifeorg02`. Applying resolutions to affected memberships, chaining
or revoking decisions, and exposing them through Life readers remain separate
steps; the first unambiguous alias/merge application is recorded below.

Commit `04e9ab8fd` adds the bounded application step. A single active target
(alias/merge) copies active or excluded memberships with deterministic evidence
 union, preserves target-side exclusions, supersedes the old memberships, and
 redirects the old group. Multiple active split targets return an explicit
 ambiguity result and move nothing. Reapplication is a no-op after redirect;
 resolution replacement/revocation and reader exposure remain separate.

Commit `1854e4740` adds the lifecycle seam and owner trigger. A replacement
atomically creates an evidence-backed successor and records `superseded_by_id`;
a revision-bound revoke is replay-safe. The existing Plan and Occasion owner
projector callbacks invoke organization reconciliation on the current owner
group, so an accepted active alias/merge can be applied on the owner-change
path without creating another queue. A split remains ambiguous. If a lifecycle
change arrives after a prior membership transfer, the derived rows require an
explicit lineage-aware repair package; this commit does not infer or silently
undo those rows.
The local migration head is now `lifeorg03`.

Commit `c718fc0cc` makes the owner-triggered reconciliation result explicit.
If an owner group is redirected and its active resolution changed, or a
resolution was revoked after transfer, the callback returns a repair-required
status instead of presenting a no-op as convergence. Missing owner groups and
ambiguous split decisions are separately classified. This is a reporting and
safety boundary; actual affected-set rebuilding remains the next implementation
package.

Commit `1e49ba0b5` adds per-membership transfer lineage in `lifeorg04` and a
bounded repair-plan reader. Each accepted merge/alias transfer records the
source and target membership IDs plus the source evidence/revision. Lifecycle
reconciliation now exposes the exact affected set when available; it falls
back to an explicit group rebuild requirement when older rows have no lineage.
This package still plans the repair and does not reverse memberships or change
Life readers. The local migration head is now `lifeorg04`.
Follow-up `e00123f3d` makes replacement-kind replay comparisons value-based.

Commit `c82f6ceb4` completes the first bounded repair mutation. `lifeorg05`
captures target pre-state and post-transfer revisions, removes cascading
membership FKs so lineage survives deletion, and performs reverse-order
CAS-guarded rollback. Revoked transfers restore the source group/memberships;
replacements can then apply their successor in a separate transaction. Any
later membership revision, unrelated active transfer, archived group, or
legacy lineage fails closed for review. This is not a general group rebuild,
and readers remain shadow-only.

Follow-up `c6cc768fc` closes the remaining lifecycle-state hole at the mutation
boundary: repair refuses to run unless the source is still `redirected` and
each affected target group is still `active`. Its three PostgreSQL regression
cases cover a two-membership transfer, a later target detach (the repair
transaction fails before changing any row), and an archived owner target.
The connected resolution selection passes all 8 cases; legacy lineage fallback
remains the next package.

Commit `59cab4f88` extends the archived-target regression through explicit
reactivation. The restored target's newer membership revision still blocks
the stale transfer rollback, making restoration a current-authority boundary
rather than an implicit permission to replay historical repair.

Commit `6f4a977bb` adds the legacy-lineage boundary case. A transfer row
without usable lineage returns `group_rebuild_required` from both the planner
and mutation entry point; no reverse mutation is attempted.

| Lane/interface | Concrete dependency | Work that can continue here |
| --- | --- | --- |
| Capture/source owners | Exact custody/expiry/representation reads, current revision and authorized restore event; agree any missing transaction change before editing its producer | Receiver tests, replay, report and source-only organization using existing contracts |
| Graph owners | Current/former recipient sets; Commitment participation, Occasion membership and Outcome content/audience revisions; absence/restore evidence | Existing projections, population and bounded reconciliation; no Life-owned intention writer |
| Integration/Home/Places | Canonical record ref and current revision, exact destination, return lens/anchor, affected-query/dependency repair signals | Supply tested record interfaces and named receiving gaps. Integration owns prepared-value delivery and practical facts; its live engine reads canonical owners directly |
| Retirement | Explicit mapping for Atlas/historical artifacts and retained booking evidence, including hide/rename/refind controls | Keep migration obligations in the denominator; preserve canonical original destinations |
| Design/founder | Resolve split navigation or group-control choices only where they change persistence/commands | Complete deterministic containment, exact retrieval and replay without waiting for final visual composition |

After each package, update this section's status and the existing execution
receipt with exact commits, executed tests, report location, remaining owner
gaps and next checkpoint. Commit only explicit files. This planning packet
authorizes no push, merge, production activation, reader cutover or Atlas deletion.

### 11.8 Execution receipt — September 7

The bounded packet was implemented in backend worktree
`/Users/feihuyan/travel-agent-life-shadow-rehearsal-2026-09-07` from baseline
`3f7e25da6`. Reviewable commits are:

- `41e07297e` — all-lens owner materialization, non-empty coverage denominators,
  fixture/report foundations, bounded indexed-owner traversal and unit/connected
  rehearsal tests.
- `ca559b2f7` — versioned report envelope, non-production/serving gates and
  opt-in pytest report writer with inconclusive failure output.
- `bfb26e6a9` — connected indexed-owner reconciliation evidence.
- `27258111c` — deterministic owner-commit/publication race.
- `d062d1810` — successful backfill retries now remove their resolved identity
  from the persisted unresolved-work set, including already-current convergence.
- `f9b687055` — transient enumeration failures now pause without advancing the
  family cursor; a later successful page clears the retryable family finding.
- `b7425b548` — connected Plan owner mutations now exercise the durable outbox
  publisher and current-authority consumer, including out-of-order replay.
- `d7714e38c` — the connected delivery test isolates event-bus registrations so
  its explicit publisher cannot leak asynchronous work into neighboring tests.
- `6c7d07847` — graph owner events now defer to their specialized current-
  authority consumers; the generic handler no longer double-writes or loses
  Outcome audience dependency tokens. Connected delivery coverage includes
  Plan, Occasion and shared Outcome.
- `949fdd524` — `require_handler=True` now requires an explicit owner-consumer
  acknowledgement; an unrelated subscriber returning `None` cannot establish
  durable publication completion.
- `09d6f9b69` — connected PostgreSQL evidence now covers persisted backfill
  pause/restart, stale backfill-lease fencing, and outbox lease reclaim/lost
  acknowledgement.
- `143c54079` — `lifeorg01` adds the first R2-G persistence slice: stable,
  viewer/version-scoped group identities, evidence-backed memberships, and a
  revision-bound control ledger for rename, detach/exclusion, and exact Undo.
  The deterministic proposal/materialization seam is implemented without
  learned clustering or a Life-owned source of truth; wiring and identity
  reconciliation remain follow-up work.
- `a6c21a0ca` — command-ledger inserts are conflict-safe and happen before
  derived-state mutation, fencing concurrent duplicate rename, detach, and
  Undo attempts behind the viewer/version/control-key idempotency boundary.
- `29d2a799b` — the existing Plan/Occasion owner consumers now invoke a thin
  organization adapter after successful index publication, archive derived
  owner groups on fenced withdrawal, and require an explicit restore to
  reactivate superseded memberships. Callback-level tests and PostgreSQL
  archive/restore evidence cover the connection; Outcome/source organization
  remains intentionally unimplemented.
- `2defe2692` — `lifeorg02` adds an accepted identity-resolution registry for
  alias/merge/split mappings with evidence and stable source/target handles.
  Resolution replay is idempotent and split reads preserve every active target;
  no membership rewrite or reader cutover is implied.
- `04e9ab8fd` — applies one unambiguous active alias/merge resolution to the
  derived membership layer with exclusion/evidence preservation, while leaving
  multi-target splits explicitly unresolved. The redirected source group and
  target membership updates are revisioned and replay-safe.
- `3b17dacd9` — treats multiple active resolution rows as ambiguous even when
  they happen to name the same target, avoiding a hidden alias/merge choice.
- `7c5154740` — adds connected merge evidence with a target-side exclusion;
  the merge keeps that exclusion while unioning the source evidence.

The follow-up repair work is also committed in the isolated Life worktree:
`c82f6ceb4` provides the first CAS-guarded affected-set rollback,
`c6cc768fc` adds source/target lifecycle fences and multi-transfer/stale-control
regressions, `59cab4f88` proves an explicit restored target cannot be overwritten
by an old transfer, and `4e41b23c4` aligns a retained-source route fixture with
the canonical `created_at` ordering contract. The connected resolution
selection passes 9 cases; the full `tests/life_projection` selection passes
205 cases, and the combined Life worker/event-bus selection passes 228 cases.

The explicitly provisioned local database `vesper_life_rehearsal_20260907` was
migrated to `lifeorg05` (single head). Evidence executed against that
database:

| Check | Result |
| --- | --- |
| Offline Life/event-bus selection | 165 passed, 17 provider/Postgres cases deselected |
| Full `tests/life_projection` selection on isolated PostgreSQL | 182 passed |
| Retry/enumeration unit selection | 9 passed |
| Complete `tests/life_projection` connected selection | 17 passed, 165 offline cases deselected |
| Connected report command with JUnit + `--life-rehearsal-report` | 2 passed; report schema `vesper.life-shadow-rehearsal.v1`, `supported_scope=pass`, `whole_portfolio_complete=false`, `serving_ready=false` |
| R2-G organization proposal/materialization and PostgreSQL control sequence | 12 passed across the focused Plan/Occasion/organization selection; stable identity, evidence revision, replay, exclusion non-resurrection, stale readback, rename/detach, exact Undo, conflict-safe control insertion, owner-group archive, explicit restore, and projector callbacks |
| R2-G identity-resolution registry and migration | 7 passed across the resolution/organization selection; idempotent alias, merge/split persistence, all-target split readback, and `lifeorg02` downgrade/upgrade |
| R2-G unambiguous resolution application | 2 passed; merge membership transfer, target-side exclusion preservation, source redirect, idempotent reapplication, and explicit split ambiguity |
| R2-G CAS-guarded repair lifecycle | 9 passed; multi-transfer reverse rollback, later target detach atomic rejection, archived target fencing, explicit restored-target stale-repair rejection, and legacy lineage rebuild classification |
| Broad Life verification | 228 passed across `tests/life_projection`, Life projection workers, event bus, and projection broadcast suites |
| Ruff on changed files | Passed |

The rehearsal proves the supported Plan path, linked Occasion lens membership,
current-authority fencing, withdrawal/explicit restoration, bounded derived-owner
inventory, real durable Plan/Occasion/Outcome outbox-to-consumer paths with
out-of-order replay, and one real commit/publication interleaving. The connected
control-plane cases additionally prove that a paused checkpoint can be reclaimed,
that a stale backfill claimant cannot checkpoint after lease takeover, and that a
lost outbox acknowledgement cannot be performed by the old lease holder. The
unit-level backfill retry cases additionally prove that resolved or already-current
identities are removed from live unresolved work rather than retained as an
append-only error, and that a transient enumeration read preserves its retry
cursor. It does not
yet prove the full seven-record/four-viewer corpus, the broader lease/retry
interleaving matrix, paused-run restart with a persisted unresolved identity
reprocessed by the runner, Atlas/anchor migration, social/authored owner
adapters, or a Life serving
cutover. The report's false-green protections are intentional: the supported-
scope pass is not a whole-portfolio certificate.

The new repair cases close the first affected-set mutation boundary but do not
eliminate the legacy path: transfers without current lineage remain an
explicit group-rebuild requirement, and restored or archived owner states are
accepted only through current revisions. No reader, serving, or Atlas
retirement decision follows from these connected passes.

The local commit hook's repository-wide size-budget check remains red on
pre-existing unrelated files; it was the only skipped hook for these commits.

## 12. Connected organization and reader implementation plan — September 7

### 12.1 Decision, scope and implementation baseline

**Build the source-backed organizer and the reader experience together.** The
next system increment should turn eligible material into recognizable periods,
journeys, outings and continuity, expose the evidence through four useful
lenses, and maintain those records when reality or the user's choices change.
This is the next connected R2-G / R3–R5 package, not a new roadmap, a single
travel demo, a cosmetic card pass or another indexing framework.

Use the existing W1–W5 portfolio throughout: journey, ordinary local life,
explicit continuity, shared occasion, and kept-but-not-lived evidence. W6's
later human-composition custody remains a separate R7 dependency. A small
first commit is a review boundary, not a narrower definition of the product.

Planning inspection: Life backend branch `6f4a977bb`; canonical backend main
advanced to `9efb3d9d9`; app `c3feb89f0`; research workspace branch
`codex/life-organization-value-research-2026-09-07` based at `83e2ae1`.
Canonical root main was `517744f` during this pass and contains concurrent
work. The Life branch's later packages remain unmerged. Recheck these facts
before implementation; this document does not authorize integration or moving
someone else's work. Edit in an isolated `codex/` lane and stage explicit files.

The existing [engine design §16](life-organization-and-composition-engine-system-design-2026-09-05.md#16-organization-quality-and-reader-value-investigation--september-7)
contains product judgments, probes and comparison baselines. This section
adds implementation decisions and work packages. New fields, helpers and
relation names below are **proposed**, unless explicitly described as existing.
No production migration, model experiment or app implementation ran in this
planning pass.

### 12.2 What the targeted online research changes

Sources accessed September 7, 2026. These support specific choices; none
validates Life's whole product or supplies Vesper performance thresholds.

| Question | Primary evidence and limitation | Recommendation for this repository |
| --- | --- | --- |
| Should one AI memory hierarchy determine Life's groups? | [ES-Mem, January 2026 preprint](https://arxiv.org/html/2601.07582v1) separates dialogue by topic/intent; its limitations explicitly identify relatively static memories and primarily text-modal inputs | Borrow coherent source-passage retrieval if useful. Keep conversation segmentation, real-life grouping and presentation separate; do not adopt its hierarchy as lived-event identity |
| How should grouping change as evidence arrives? | [Incremental constrained clustering, CP 2023](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CP.2023.10) studies stable partition changes as expert constraints accumulate, including a satellite-data case | Prefer the smallest justified affected-set change. Do not import its expert-labeling workflow, solver or relaxable constraints; withdrawal and explicit exclusion are hard boundaries |
| What should a reader make easy? | [Stuff I've Seen, SIGIR 2003](https://www.microsoft.com/en-us/research/publication/stuff-ive-seen-a-system-for-personal-information-retrieval-and-re-use/) reports time and people as useful refinding cues in an internal workplace deployment | Test recognition and exact-original retrieval through several cues, not summary attractiveness alone. Its workplace findings are not validation of our consumer Life design |
| Can a revision plus several ordinary SQL reads form one coherent page? | [PostgreSQL 15 isolation](https://www.postgresql.org/docs/15/transaction-iso.html) documents statement snapshots at Read Committed and transaction snapshots at Repeatable Read | Assemble a bounded response in one statement where practical, otherwise one short read-only consistent transaction. Keep current-authority fencing distinct; do not hold transactions across mobile pagination or change isolation globally |
| Does a hierarchy require new graph infrastructure? | [PostgreSQL recursive queries](https://www.postgresql.org/docs/15/queries-with.html) supports traversal and cycle detection; an outer LIMIT is not a reliable production traversal bound | Use narrow relational group links, explicit ordering and bounded immediate-child reads. Validate cycles on writes. No graph database or eager whole-tree expansion |
| How do we paginate stable groups? | [PostgreSQL LIMIT/OFFSET](https://www.postgresql.org/docs/15/queries-limit.html) requires unique ordering for predictable subsets and notes that skipped OFFSET rows still require computation | Extend existing keyset/cursor conventions with group scope and content freshness; restore by stable row identity, not array index |
| How do index and organization updates survive crashes? | [AWS transactional-outbox guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html) describes atomic producer-side event persistence and duplicate-safe consumers | Reuse Life's awaited consumer and downstream outbox. Ensure replay completes organization even when the index is already current; don't add another source producer or treat cache invalidation as delivery |
| How should existing shadow data evolve? | [Alembic data-migration guidance](https://alembic.sqlalchemy.org/en/latest/cookbook.html#data-migrations-general-techniques) distinguishes schema changes from application-specific data migration and warns that data downgrades can be unsafe | Separate additive DDL from bounded, resumable relation repair. Rehearse populated historical upgrades; do not reset shadow data merely to make migration tests green |

**Research conclusion:** enough is known to design and implement the connected
system. Remaining research should measure a named organizer/reader failure,
not restart a broad search for a memory platform. B1 structured evidence and
B2 bounded semantic assistance remain comparison candidates, not a claim that
either already produces the intended experience.

### 12.3 Verified gaps that determine the order

Paths in this subsection are relative to the Life backend branch above.

| Inspected implementation | What exists | What the next package must add |
| --- | --- | --- |
| `backend/life_projection/organization.py` | Owner seeds for Plan/Occasion, explicit proposals, exclusion filtering and deduplication | Source-backed periods/episodes; supported continuity; neutral containment instead of treating owner inclusion as occurrence support |
| `backend/core/models/retained_source.py` and `backend/core/db/intake_anchors.py` | Authored note, source refs, custody/status and created/updated clocks; exact retained-source read | Agreed, purpose-permitted structured evidence and exact locators. These fields do not currently provide occurrence intervals, participant roles or canonical places |
| `backend/core/models/source_owner_event.py` | Content-free lifecycle contract; purposes `source_refind` and `projection_repair` | Explicit agreement on whether/how organization can consume eligible evidence. Receiving an event is not extraction authorization |
| `backend/core/db/_tables/life_organization.py` | Groups, record memberships and controls with revision checks | Typed group-to-group navigation, queryable temporal scope, efficient reverse evidence lookup and content-read freshness |
| `backend/core/db/life_organization.py` | Add/update proposal materialization; member revisions; durable rename/detach/Undo | Scoped reconciliation of relationships that disappeared. Ordinary member writes do not advance group revision; future group cursors cannot rely on it alone |
| `organization_projector.py`, Plan/Occasion projectors | Awaited organization callbacks after index writes | Retained-source/Outcome organization coverage and crash/retry completion for each stage, including restore replays |
| `backend/core/life_projection_broadcast.py` | `emit_and_wait`, durable defer, lease-fenced acknowledgement | Keep organization completion or a durable continuation before Life acknowledgement; no second Intake acknowledgement |
| `corpus_query.py`, `index_records.py`, root routes | Shared canonical snapshot; bounded indexed record primitives; stable record semantics | One lens/scope-aware group query used by root and depth, bounded previews/members, exact-source bypass and content-aware cursors |
| `lifeorg05_transfer_repair_cas.py` | Current-schema lineage/CAS safety; legacy rows explicitly marked for rebuilding | Actual populated `lifeorg04` → `lifeorg05` test, schema-constraint audit and subsequent semantic relation migration |

Do not reinterpret a `ResourceRef` for a whole submission as an exact passage,
an internal sort timestamp as attendance, an Outcome creation time as when its
subject happened, or a shared Occasion as permission to read private Outcomes.
Confirmed anchors, retained originals and graph records need explicit coverage;
an original disappearing from the retained-only projection after representation
must not disappear from Life's complete custody/refinding path.

### 12.4 Proposed evidence and organization contracts

#### A. An owner-readable evidence view, not a new fact owner

Define a small Life-internal envelope with the owning lanes. Reuse existing
models and source locators where they fit; do not add a parallel public API
merely to carry this internal view. Each supported relation needs:

- canonical owner/source identity, opaque current revision and original route;
- exact source locator and locator revision where finer-than-source evidence
  exists; original lineage for crops/duplicates, without multiplying witnesses;
- typed time basis, precision/timezone and any negative or disputed assertion;
- canonical place/participant/occasion refs **when actually supported**, with
  attributed roles such as author, contributor or explicitly reported attendee;
- relationship basis and permitted purpose/audience, plus the owner event or
  dependency identity that makes withdrawal/correction repair discoverable.

Missing fields remain missing. A label alone does not become a canonical Place;
a name in prose does not become a participant. Whole-source association is
allowed only when the whole-source meaning justifies it. A multi-event note
requires narrower locators before selective event attachment. Do not run a
model over raw chats to fill gaps outside the accepted contribution lifecycle.

**Exact Capture dependency:** an authorized read contract for already-retained
evidence/claims with locators, revisions, time roles and repair identity; explicit
organization-purpose treatment; and represented/unrepresented handoff to the
confirmed owner without losing the original. Capture owns any required source
producer/transaction change. Life can implement the consumer contract, mocks,
safe kept-date periods and original readers while that agreement is pending.
Those fallbacks do not complete source-backed event organization.

#### B. Stable groups with several relationships and a simple default path

Keep `owner`, `episode`, `period` and `thread` in the existing registry. A derived
journey can use an episode group with supported children; it does not require a
new Journey owner or a Plan. The group key is allocated/reused through the
registry, not hashed from the current title, summary or member set.

Propose a narrow relational group-link seam alongside existing record
memberships: default containment and calendar reference are different roles.
Allow at most one active default parent per child, scoped by viewer/version;
allow a journey to be referenced from two calendar periods without duplicating
it. Enforce same-scope foreign keys, no self-link and no containment cycles.
Serialize topology changes within the relevant viewer/version scope before
cycle checks; document lock order shared with member/control writes. Do not
rely on two concurrent application-only preflight checks. Read immediate
children by default; don't implement a general-purpose relationship graph UI.

Places and People initially use canonical-subject facets over these same
records and relationships. They are not additional generic group kinds or
Life-owned world-place/person records. Two supported visits can appear under
one Place without merging their episodes. A People reader shows eligible shared
records and attributed contributions, not a generated dossier. Threads need an
explicit retained continuity relation first; semantic resemblance can propose
a relation but does not establish one.

For calendar navigation, persist the calendar/timezone policy and date role.
Month/year scaffolding is sufficient initially; a week/day layer is optional
when it improves recognition. Separate supported lived intervals from captured,
authored, scheduled and kept-date navigation. Unknown-time material remains
directly findable. Device timezone changes must not re-key existing periods.

#### C. Minimal storage additions, reviewed before migration

Reuse the current registry, membership, control and resolution-transfer tables.
The migration proposal should cover only these missing responsibilities:

1. Typed group navigation and indexed scope/time lookup as described above.
2. Reverse-queryable supporting dependencies linking owner/source/locator
   identity and revision to the derived membership/consumer. Reuse any compatible
   shared dependency facility after inspecting it; otherwise add a narrow Life
   relation table, not another corpus or event framework. Bounded JSON preview
   refs are not the complete repair inventory.
3. A content epoch for group reads, separate from current command CAS revision,
   plus a conservative viewer/version/lens scope epoch for list membership and
   ordering. Advance affected epochs transactionally on observable changes,
   including source content changes with unchanged membership. No-op replay
   should advance neither. Measure contention before adding finer partitions.
4. A small renderer-neutral preview selection manifest: selected stable refs,
   evidence revision, selection-policy version and authored-label status. Reuse
   an existing derived-payload seam where appropriate; do not create a second
   copy of source bytes or a server-selected layout language.

Membership revisions continue to fence membership edits; existing group
revisions continue to protect their current command/repair dependencies. Do not
silently redefine Undo to fail on every unrelated preview refresh. Audit all
existing revision checks before introducing the separate read epoch.

#### D. Correct owner containment without erasing genuine occurrence evidence

Propose `contained_record` as the neutral owner/group membership relation;
reserve `supports_occurrence` for evidence actually supporting an occurrence.
Confirm the vocabulary against shared consumers before finalizing it. A stored
membership row is not a new assertion that somebody attended an event.

The migration must identify generated owner-self memberships by their exact
owner/group/record shape and provenance, not globally rename every
`supports_occurrence` row. Preserve stable row IDs, exclusions, accepted control
targets, idempotency results and transfer before-images. Produce a dry-run
inventory of convertible, genuine, ambiguous and colliding rows. Ambiguous
rows remain non-occurrence evidence to readers and require scoped repair;
never choose an active row over a conflicting exclusion. This must include
legacy control/replay compatibility, not just a new enum and clean fixtures.

### 12.5 How changes become maintained records

Use the existing owner-change → Life outbox → current-authority projector →
shadow index path. Extend the awaited Life consumer with organization work:

1. Re-read the exact current owner and applicable purpose/audience. Stale events
   are hints, not a license to republish old facts. Opaque revision strings must
   not be ordered lexicographically as a substitute for owner authority.
2. Resolve previous memberships and reverse dependencies for the changed
   evidence. Build a bounded candidate neighborhood from explicit context,
   compatible typed time/place and existing groups; do not scan all raw chats
   or compare the whole corpus pairwise.
3. Compute B1 proposals outside write transactions: justified links, forbidden
   joins, no-link outcomes and affected previous/new scopes. Time/place helps
   select candidates but cannot establish the same dinner by itself. Preserve
   independent support when only one contributing source changes.
4. Recheck owner/dependency/control revisions, lock in a documented order, then
   reconcile the affected relation set. Add justified relations; supersede
   unsupported old ones; preserve exclusions and explicit title choices.
   Superseding a membership does not delete its original or unrelated facets.
5. Update dependencies, navigation, eligible preview selection and read epochs
   in the same derived transaction. Repair both the old and new parents when
   an item moves. Identity resolution uses the existing lineage registry;
   ambiguous splits return all valid targets, never an arbitrary first child.
6. Acknowledge the Life delivery only after this bounded work completes or an
   explicit durable continuation is committed. A crash after index success
   must replay organization even when that index row is already current.
   Replaying a completed authorized restore must converge rather than require
   the row to still be withdrawn. It must not authorize ordinary resurrection.

Keep this first deterministic path in the existing awaited consumer. If measured
fan-out exceeds a safe job bound, extend Life's existing repair/checkpoint work
with a resumable affected-scope continuation before acknowledging. Record its
dedupe identity, lease, target revision, cursor and supersession behavior; do not
launch untracked background work or create a parallel Intake acknowledgement.

Safety invalidation cannot wait for enrichment. Current-owner checks remove
revoked/expired support, counts and previews from read eligibility; asynchronous
repair then converges stored organization. A dependency mismatch hides/rebuilds
the dependent excerpt, not independent originals. On transient worker failure,
the original can remain available while enrichment is pending. No root/depth
GET runs a model, mutates organization or starts a corpus rebuild.

Duplicate-source handling distinguishes display deduplication from deletion.
Retain exact original routes and lineage; do not collapse separately authored
accounts because they share a photograph or subject. Late imports should change
their supported historical context, not take over the user's current month.

### 12.6 Reader contract and the actual user payoff

Extend the canonical Life query abstraction so root and depth use the same
viewer, projection version, lens, scope, eligibility and ordering semantics.
Keep the legacy snapshot adapter while indexed/group serving remains dark.
Do not create a separate root compiler with a different definition of belonging.

The group reader returns a bounded recognition preview, typed date/context,
stable group identity, eligible count **with its unit**, immediate child
references, selected evidence with exact routes, coverage/availability, content
revision and a continuation. Original-record lookup remains a separate exact
operation on the same authority model. A preview list is not an exhaustive
manifest; page the full membership/dependency set on its own bounded path.

| Lens or entry path | Recognition/payoff | Reader obligation |
| --- | --- | --- |
| Time | A recognizable journey or local period with the meaningful parts visible | Distinguish actual, planned and kept dates; don't force city → day → meal traversal to retrieve an original |
| Places | Different visits/accounts related to the same Place | Keep visits distinct; show kept-not-lived evidence truthfully; don't duplicate the Places root's discovery feed |
| People | The shared dinner and what a person actually contributed | Preserve author/source identity and viewer-relative access; no mention-as-attendance or composite group voice |
| Threads | The observation, retained explanation and explicitly connected later attempt | Preserve source-backed steps; no culinary/personality label synthesized from similarity alone |
| Everything kept / source search | Find a ticket, note or reading directly | Include retained and represented originals without duplicate witnesses; no mandatory group path or generic full-record substitute |

Selection baseline: prefer evidence that helps distinguish this record and
recover useful details. Keep a still-useful incumbent preview when new material
adds no better recognition; replace invalid/withdrawn evidence immediately.
Use text, receipts or attributed contributions without requiring a photo.
Don't optimize for one item from every owner type. Reconstruction may be useful
without novelty; human contribution does not require AI rewriting. An AI Return
still needs substantive added work under the Editorial Canon.

**Pagination and restoration:** use a unique stable sort tuple and keyset cursor
bound to viewer/version/lens/scope and content epoch. Check cursor context and
version using existing conflict conventions. A changed scope produces explicit
stale-cursor readback; the client restarts and resolves the previous stable
group/record/block anchor where still eligible. Do not silently concatenate old
and new snapshots. Revisions changing on unrelated groups should not reset an
open exact reader. Measure list-level epoch churn before making it more granular.

Assemble each bounded response under one consistent database snapshot; release
it before the next request. Preserve the current-authority publication/read
boundary, including eligibility checks at a defined point before response.
An old cursor or consistent snapshot is never authorization to show revoked
content. Bound scanned candidates as well as returned rows; when authority
filtering creates a sparse page, return a truthful continuation/coverage result
instead of scanning indefinitely or falsely declaring the corpus exhausted.

Mobile implementation should reuse `components/life/LifeRootV1Screen.tsx`,
`app/you/life-record.tsx`, existing hooks and
`utils/lifeReadingPositionStorage.ts`. Add only the semantic distinctions the
approved Life design needs. Keep exact-source search, grouped depth and
Everything kept distinct; preserve loading, unavailable, empty, sparse and
retry states. Final card geometry stays in Claude Design; no new Chat surface,
composition editor or generic dossier shell is part of this package.

### 12.7 Reviewable implementation packages

These labels subdivide existing R2-G/R3–R5/R7 work, not new roadmap tracks.
Each package ends with explicit code/test evidence in this section. Commit only
owned files; do not push/merge or switch serving as an internal implementation
choice. File boundaries below are existing extension points; new small modules
may separate evidence, reconciliation and readers rather than growing the
already large `backend/core/db/life_organization.py` into a whole engine.

| Package | Concrete work and principal surfaces | Exit evidence / next dependency |
| --- | --- | --- |
| P0 — baseline and migration evidence | Inspect branch divergence, current schema head and shared lane changes. Add a populated `lifeorg04` → `lifeorg05` test; audit table declarations, historical transfer FKs, legacy flags and repair refusal | Fresh-schema and historical-upgrade results agree with intended current constraints. Legacy sentinel revisions are never trusted as real before-images. Record branch-integration needs without merging |
| P1 — evidence and semantic contract | Agree Capture/graph evidence envelope, supported owners and purpose. Specify neutral containment and old-row inventory in `organization.py`, owner models and organization storage | Fixtures distinguish kept/planned/occurred/negative claims; exact field-by-field availability matrix and producer dependencies. Reviewed additive schema/migration proposal before table changes |
| P2 — stable organization and reconciliation | Extend existing group/member storage with justified navigation, temporal lookup, reverse dependencies and read epochs. Implement B1 periods/episodes, explicit continuity, scoped set reconciliation and revision-safe preview selection | Source-only W2 works without Plan/Occasion. Separate visits, cross-month journey identity, undated refinding, exclusions, no-op replay and multi-event source locators tested. Unsupported real owner reads remain named gaps |
| P3 — connect durable maintenance | Extend retained-source/Outcome and existing Plan/Occasion organization callbacks; connect previous/new affected groups, withdrawal, current-authority restore and bounded continuations if needed | Crash after index write, retry after organization commit, lost ack lease, new revision overtaking old work, withdrawal during work and restore replay all converge. No second queue framework or source-side producer authored by Life |
| P4 — one bounded group query and exact readers | Extend `corpus_query.py`/indexed adapter, `compiler.py`, Life models and existing routes with shared scope semantics, immediate children, previews, counts and exact-original bypass | Root/depth agree; lexical/exact retrieval bypasses hierarchy; tie-heavy keyset pages, stale cursors, sparse filtering, alias/split destinations and current-authority checks pass. Still dark |
| P5 — native data integration | Run cross-repo schema sync; reuse Life root/depth/hooks/storage to consume typed group and original destinations and restore stable anchors | Generated schema/typecheck, focused Jest and route/restoration regressions pass. All W1–W5 are inspectable through fixtures; app/device session remains deferred, not claimed complete |
| P6 — quality and bounded semantic experiment | Extend existing replay/rehearsal reporting with organization/reader judgments. Compare B0/B1; only run B2 for evidenced misses through the registered model gateway with an authorized budget/data scope | Report per-world useful grouping, false joins, exact findability, churn, latency/cost and unsupported coverage separately. B2 earns adoption only if it improves supported misses without relaxing hard constraints |
| P7 — replacement readiness, not automatic activation | Reuse §11 corpus parity and R8 custody/Atlas mapping, broaden supported owner coverage and verify fallback preserves originals/controls | A release decision has populated migration evidence, durable delivery coverage, exact destinations, performance budgets, native acceptance when resumed and explicit activation authority. This planning package does not grant it |

**Dependency order (refined by §13 after implementation):** P0 and P1 establish
the baseline and contracts; P2 and P3 form one maintained organization capability;
P4 is designed alongside P1/P2
so storage earns its place in the reader; P5 follows the typed reader contract.
P6's corpus and evaluation work starts with P1, not after all the implementation.
P7 uses their receipts plus the existing broader R0–R8 acceptance conditions.
This is an engineering sequence, not a promise of a one-week calendar schedule.

When an owner seam is unavailable, continue P0, internal contract tests,
bounded reader fixtures, deterministic safe fallbacks and replay simulations.
Do not mark P2/P3 portfolio-complete using fabricated owner reads. Return the
exact missing interface and which acceptance scenario it blocks. The first
review checkpoint is P0 plus P1's contract/storage proposal; the next connected
checkpoint is P2–P4 working against all currently supported W1–W5 evidence.

### 12.8 Verification and evaluation matrix

All cases here are planned, except historical receipts explicitly recorded
above. Tests that use authored/mock evidence do not establish production owner
coverage, and inspecting an example does not count as a model experiment.

| Area | Required cases and assertions |
| --- | --- |
| Truth and semantic types | Plan self-containment without attendance; unused ticket plus explicit nonattendance; source/event/import clocks differ; conflicting participant accounts; retention purpose does not widen |
| Organization | W1–W5 plus design §16's V1–V12; source-only W2; same Place/two dates; month boundary; uncertain midnight/timezone; long multi-event note; no photo; duplicate lineage; sparse unplaced reading |
| Stability and voluntary edits | Late import preserves unrelated IDs and open anchors; unchanged replay preserves epochs; rename survives automatic refresh; detach survives replay/rebuild; exact Undo rejects genuine intervening conflicts without unrelated-preview conflicts |
| Scoped repair | Source correction moves only justified memberships; old and new parents updated; remaining independent support survives; preview/count dependencies withdrawn; explicit restored evidence obeys current exclusions; unresolved repair has a reachable checkpoint |
| PostgreSQL concurrency | Duplicate first insert, concurrent detach/materialize, opposing containment-edge insertion, alias/split repair versus source update, revoke during selection, duplicate restore, lost worker lease and out-of-order delivery; use controlled interleavings, not sleeps as proof |
| Migration | Seed pre-upgrade groups, active/excluded memberships, controls and transferred lineage at `lifeorg04`; upgrade; inspect constraints and legacy repair behavior. Separately test neutral-relation conversion/collisions/control replay and resumable interruption |
| Reader bounds | Multiple small page sizes, equal sort values, empty/partial page, sparse authorization, changing cursor scope, missing owner, redirected/split handle and deep/wide hierarchy. Assert bounded scanned/returned work, no N+1 full-corpus reads and no duplicate/omitted rows within an unchanged scope |
| Native data integration | Same typed identity through root → group → original → back; exact source deep link bypasses grouping; lens/query preserved; removed-anchor safe fallback; no repeated failed cursor loop; offline/retry/unavailable handled |
| Useful value | Recognize the right outing, retrieve the specific original, distinguish visits, find someone's actual contribution, understand a corrected movement without entering new data; report backtracking and wrong doors as well as successful completion |

Run focused offline backend tests before connected PostgreSQL selections;
keep migration databases isolated and disposable under the repository's test
workflow. The historical upgrade is not simulated by changing a status field
in a current-schema row. `lifeorg05` intentionally removes cascading membership
FKs to retain transfer lineage; its downgrade does not currently recreate them.
Audit and test the intended rollback contract explicitly, including historical
rows whose referenced membership was removed. Do not promise a lossless data
downgrade or execute one against the user's working/production database.

For a public model/route change, run the required workspace
`scripts/sync-types.sh` workflow, review both OpenAPI snapshots and generated
`travel-app/utils/api/schema.gen.ts`, then run TypeScript and relevant Jest.
No hand-maintained TypeScript copy of the backend group contract. Scope tests
to explicit files, record commands and branch hashes, and distinguish any
pre-existing repository gate failure from a Life regression.

**Quality reporting:** evaluate required-link recall and false joins together;
counting only forbidden joins rewards an organizer that never groups anything.
Measure exact-source findability, useful subgroup coverage and unplaced-but-
findable material. Track visible intermediate churn separately from final-state
equivalence after incremental versus rebuilt processing. Allow several valid
hierarchies; compare meaning, authority, controls and preserved registry identity
rather than require byte-identical generated titles or one universal tree.

For B2, freeze calibration cases and independently prepare unseen variants
before the measured run. Reuse the existing model gateway/registry, structured
output validation, timeouts and bounded candidate set. A model may suggest a
relationship with exact support or abstain; it may not mint canonical identities,
rewrite authored meaning or override exclusions. Measure marginal quality gain,
cost and latency per task. Paper leaderboard numbers are not our thresholds.
Choose explicit product tolerances from local baselines before promotion;
audience leakage, invented attendance, resurrection and lost originals are hard
failures, not average-score tradeoffs. No private artifacts or paid inference
were sent to external models during this documentation pass.

### 12.9 Cross-lane handoffs and rollout boundaries

| Owner | Exact handoff needed | Not delegated to Life |
| --- | --- | --- |
| Capture / confirmed-source owners | Permitted evidence/locator read; claim and source revisions; original/representation mapping; withdrawal and restore dependency identities | Raw-chat retention, source-side transaction changes, duplicate intake acknowledgement or source repair authority |
| Plan / Occasion / Outcome and social owners | Explicit context/participant roles, negative/occurrence claims where owned, canonical subject refs, current/former viewer scopes and repair events | Synthetic Plans for ordinary life, a pre-Plan intention writer or access to another person's private Outcome |
| Home / Places / Integration | Stable record/original destination, eligible content revision, exact lens/return anchor and affected-consumer repair identity | A second Life-owned current-world engine, duplicate delivery allocation or public release activation |
| Design / mobile | Reader semantics, representative evidence examples and every sparse/error/restoration state using the current Life boards | Another visual-language sprint or a new filing workflow |
| R7 human composition | Eventual custody for selected refs, stable block IDs, authored ordering/captions and revision-pinned edits | Saving an authored composition into a disposable projection or letting later grouping overwrite it |

Raw-index parity and richer-group usefulness are different checks. Preserve
owner eligibility, original custody, exact destinations and canonical claim
semantics; grouping intentionally changes presentation, so do not require its
cards to equal the old flat list. Conversely, better-looking group previews do
not waive raw-record coverage or durable repair requirements.

Keep indexed/group readers dark until the relevant acceptance and activation
decision. Any later fallback must preserve current-authority checks, original
access, group handle resolution and human controls; a stale legacy snapshot is
not automatically a safe fallback. Future projection versions still need the
documented live-fanout capability. No serving switch, Atlas deletion, destructive
migration, remote push/merge or deployment is included here.

**Recommended next action, updated after architecture review:** execute §13's
M0 baseline delta and M1 unified maintenance package. P1/P2/P4 already have the
storage, evidence-envelope and bounded-reader foundations in §12.11; do not
recreate them. Prepare the missing real-owner evidence mapping and reader
composition alongside M1, then connect them through M2–M4. This remains the
complete organizer-and-reader increment across W1–W5.

### 12.11 Execution receipt — connected storage and bounded depth reader

The first unblocked implementation slices are now committed on the isolated
Life backend branch (recheck branch divergence before integration):

- `43043a035` separates generated owner containment from occurrence evidence,
  adds the incremental `lifeorg06` relation migration, and covers the exact
  owner-self conversion/collision guard. Existing genuine `supports_occurrence`
  rows and control/lineage IDs are preserved.
- `49b92b3ad` adds `content_revision` and `read_epoch` as freshness fields
  distinct from command CAS revision, creates typed `life_organization_group_links`
  for `contains` and `calendar_reference`, locks topology endpoints in stable
  order, rejects self/cyclic containment, and adds `lifeorg07`.
- `9e34fc03d` adds a bounded renderer-neutral group-depth reader with immediate
  children, active membership keyset pagination, stable identity restoration,
  and stale content/read-epoch rejection.
- `acb8ed40a` adds PostgreSQL evidence that membership refresh advances content
  freshness without changing command revision, and that topology links are
  bounded and cycle-safe.
- `ce6905139` adds the strict internal evidence-unit envelope, policy-scoped
  calendar-period seeds and a deterministic source-evidence-to-membership
  adapter. Model-candidate evidence is rejected from B1 materialization until
  the separate B2 evaluation path explicitly accepts it.
- `a11aae244` adds an opt-in, complete-set membership reconciliation seam. It
  plans and applies only the supplied group's affected set, supersedes active
  relations that disappeared, preserves excluded and historical rows, and is
  replay-safe. The default incremental materializer remains unchanged, so an
  incomplete owner read cannot cause an accidental withdrawal.
- `36ff8053e` makes the canonical corpus continuation typed and shared by the
  root/depth route path. `LifeCorpusCursor` fences lens, represented-at time,
  corpus revision and the `(sort_at, record_id)` identity boundary in one
  pure contract; malformed partial boundaries are rejected before a page can
  be concatenated with a different scope.
- `8893cf518` tightens the evidence envelope's contract version to a closed
  literal and adds a regression for unknown versions, preventing a future
  producer from silently changing the meaning of an organization unit.
- `0f2d004db` makes the bounded group reader assemble group metadata, immediate
  topology and membership pages in one short `REPEATABLE READ` snapshot. The
  connection is released before pagination; freshness epochs still fence a
  later continuation.
- `622ab741e` adds runtime type checks to `LifeCorpusCursor`, so an invalid
  lens, timestamp, identity or revision cannot cross the pure pagination
  boundary merely because a caller bypassed HTTP validation.

The local development database was at `lifeorg05`; the additive `lifeorg06` →
`lifeorg07` upgrade was applied transactionally for test evidence. Focused
organization, migration, reader and PostgreSQL tests passed (**20**), and the
full `tests/life_projection` selection passed (**221**, including the scoped
reconciliation, typed-cursor and evidence-version cases). The typed
corpus-cursor and route selection passed their focused suite (**21**). Ruff and
migration-chain checks passed. Pre-existing
repository hooks for event-type parity (the
isolated worktree environment lacks the hook's SQLAlchemy import), repository
size budgets, and status-dead-gates were skipped for commits; they are not Life
regressions and remain release blockers to resolve in the owning baseline.

This receipt completes the storage/reader and deterministic contract foundation
of P0/P1/P2/P4 and the first scoped P2 reconciliation mutation. It does not
implement Capture's structured evidence read, retained-source/Outcome
organization callbacks, public routes or mobile schema integration. The
reconciliation seam still requires a caller with a complete, authority-checked
proposal set; broad owner coverage, durable continuations and automatic
classifier evaluation remain future packages. Calendar-period identity and
evidence adapters are safe primitives, not an automatic classifier. The next
code package must connect them against the agreed cross-lane evidence contract;
it must not infer missing fields from the new tables.

### 12.10 Planning verification receipt

- Re-read the retained-source model/read, source event purposes, awaited Life
  delivery, organization storage/materialization, owner callback wiring,
  historical migration, canonical corpus and native reader extension points.
- Consulted the eight primary sources in §12.2; recommendations and transfer
  limits are explicit. No clustering benchmark, user study or inference call
  was performed by this planning pass.
- Replay manifest validation and all six fixture-validator regressions passed;
  Ruff on both checker files passed. These preserve the preceding research's
  source-only W2 correction, not a newly implemented organizer.
- Scoped lifecycle metadata and `git diff --check` passed. All 59 relative
  links across the updated roadmap and engine design resolve, with child-repo
  targets checked against the canonical workspace.
- Existing backend test results quoted earlier are their historical receipts;
  no additional backend/database/mobile tests were represented as run here.
  Product code, APIs, source transactions, serving flags and design canvases
  were not changed. The additions are research, planning and the preceding
  fixture correction, isolated from concurrent canonical-workspace changes.

## 13. Architecture review follow-through — September 7

### 13.1 Decision and definition of completion

Continue R0–R8 with one maintained Life system. Preserve canonical owners,
the existing corpus index, durable Life outbox, typed organization, human
controls and native readers. The correction is to connect their execution and
completion contracts. M0–M6 below are subdivisions of existing work, not a new
roadmap or a new indexing framework.

**Connected completion:** an eligible owner change reaches current index state,
required organization, reverse dependencies and read freshness; either all
required work completes or its remainder stays durably reachable. A successful
index write, cache invalidation or acknowledged source event alone is not that
completion. Original access need not wait for optional enrichment.

The product outcome is recognizable, useful continuity without filing:
Time explains periods and episodes; Places distinguishes experiences at a
Place; People preserves attributed shared records; Threads exposes supported
continuity. Exact originals remain directly findable across these views.
Home/Places can consume exact eligible references, while the live engine keeps
reading canonical owners independently of whether Life has ever been opened.

This section is the execution plan and ledger. Packages are marked executed
only by the receipts below; inclusion does not authorize schema changes,
source-owned producer edits, prompt changes, paid inference, merges, pushes,
activation or destructive retirement. Follow the owning repository's approval
rules when a later implementation requires those boundaries.

### 13.2 Review evidence and what it changes

Paths below refer to the Life backend at `767f70499` unless an app path is named.
The canonical backend has overlapping fixes absent from that branch, including
`270acb53e` passing target projection versions through withdrawal fences.
Reconcile those changes before evaluating an integrated candidate.

| Finding | Code evidence | Planning consequence |
| --- | --- | --- |
| Organization repair can be silently treated as success | `plan_projector.py::project_plan_change` discards `reconcile_organization`'s return; its subscriber returns `True`. Occasion uses the same callback shape | M1 gives required maintenance a typed completion result and connects that result to durable acknowledgement |
| Organization publication follows a separately committed index write | `index_writer.py` and `core/db/life_organization.py` open independent transactions; ordinary owner materialization lacks a current-owner publication fence | M1 closes the interleaving boundary instead of relying on group-local CAS to establish current source authority |
| Backfill and live delivery have different effects | `backfill.py` calls bare projectors without organization callbacks and short-circuits on current index revision | M1 routes every entry path through the same maintainer; current index plus missing organization remains pending work |
| Automatic organization coverage is narrow | `organization_projector.py` materializes Plan/Occasion owner containment; the evidence envelope and period seeds are not an owner evidence producer | M2 connects authorized evidence across source-only life and Outcomes; unavailable owners stay explicit dependencies |
| Public reads do not use the new organization | `api/routes/root_projections.py::_read_life_snapshot` gathers graph/Intake/timeline snapshots; `organization_reader.py` is internal and not route-wired | M3 composes one reader contract with bounded index/group adapters before M4 adopts it |
| Some bounded-looking operations still do lifetime work | `retained_source_projector.py` asks `read_life_index_owner_rows` for every viewer row; root/depth fan-in drains source pages; `timeline_source.py` may ensure Atlas projection during a GET | M1 makes changed-record lookup exact; M3 bounds scanned candidates, moves maintenance off the future read path, and preserves historical originals |
| Refinding and organized browsing use different substrates | `life/refind_sources.py` remains itinerary/participation/booking based | M3/M4 preserve its useful truth-aware envelope while moving retrieval to the common identity/eligibility contract |

Review verification: the Life offline selection passed **194**, with **34**
database-dependent cases deselected. A separate in-memory probe supplied
`requires_repair=True` and observed `updated=1, withdrawn=0, stale=0` from the
Plan projector. This confirms discarded repair status, not a production
incident. The cross-transaction ordering concern was identified by inspection;
M1 must reproduce it with controlled database interleavings. Earlier connected
test receipts remain historical evidence, not tests rerun by this planning pass.

### 13.3 Execution map

| Package | Existing scope | Deliverable | Depends on |
| --- | --- | --- | --- |
| M0 — integration and migration baseline | P0 / R0–R2 | Exact change inventory, test baseline, schema/rollback evidence, integration handoff | Current branches and worktrees |
| M1 — one maintained-owner operation | P3 plus P2 repair / R1–R2 | Same completion semantics for delivery, replay, backfill and reconciliation | M0 delta inspection; no new source extraction required |
| M2 — evidence-backed organization | P1/P2/P3 / R2, R6 | Source-only and graph-backed organization with scoped repair and durable controls | M1; agreed owner evidence read |
| M3 — bounded, eligible Life reads | P4 / R1, R3, R5 | Digest, group depth, exact-original and refinding contracts over shared semantics | Contract design can start with M1; connected validation needs M2 |
| M4 — complete four-lens receiving | P5 / R3–R6 | Existing mobile roots/depths receive useful groups and exact destinations | M3 public contracts and generated schema |
| M5 — quality and substantive value | P6 / R2, R7 | Organization evaluation, justified model assistance, one admitted Return family | Evaluation starts immediately; model adoption follows measured deterministic gaps |
| M6 — coverage, cutover and Atlas retirement | P7 / R8 | Reviewed replacement candidate, safe rollback and separately authorized retirement | M0–M5 evidence and relevant owner/native acceptance |

M1 is the first engineering checkpoint, not the product's finish line. M2–M4
form the next connected product checkpoint across W1–W5. M5 evaluation is
continuous; later manual composition remains separate work inside R7.
Use dependency checkpoints rather than a fixed one-week schedule.

### 13.4 M0 — establish the integration baseline without sweeping other lanes

1. Recheck root/backend/app branches, worktrees, staged files and dirty paths.
   Record the exact Life, integration and mobile revisions used for each test.
   Read live workspace roadmap edits that may not be committed; do not copy
   another lane's uncommitted implementation into the Life branch.
2. Inventory overlapping main changes by file and behavior. Preserve source
   lifecycle/expiry, explicit restoration, target-version fences, generated
   contracts and exact Home destinations. Identify which Life-only commits
   are foundations, repairs, tests, or documentation rather than proposing a
   blanket replay of all 46 commits.
3. Prepare an isolated integration candidate only under an execution request
   that authorizes it. Record remaining conflicts/dependencies for Integration;
   no merging, rebasing another lane or pushing follows from this plan.
   M1's independent regressions may proceed on the pinned Life branch while
   integration is coordinated; revalidate them on the candidate before landing.
4. Verify one Alembic head on the eventual combined branch and the populated
   historical-schema upgrade obligations in P0/§12.8. Use a disposable test
   database; do not migrate or downgrade the shared development database for
   convenience. Classify rollback as reader rollback versus data downgrade;
   do not promise lossless downgrade of retained transfer lineage.
5. Restore navigability: add/update the Life projection `FEATURE.md` and feature
   map as part of implementation; distinguish `life/` refinding from
   `life_projection/` organization/serving. Update current-state pointers,
   not every historical receipt or legacy filename.
6. Audit capability declarations separately from rollout permission. In
   particular, the current `can_incrementally_write` predicate excludes opaque
   revisions, although Occasion uses an opaque composite revision with an owner
   fence. Promotion must depend on a validated equality/fencing contract, not
   require changing that owner to a fictitious sortable revision or marking its
   shadow implementation unavailable for the wrong reason.

**Exit:** a named branch/schema baseline, an overlap/landing list, focused test
results and an explicit unresolved integration list. Clean worktree status is
not evidence of deployed behavior or permission to activate Life readers.

### 13.5 M1 — one maintained-owner operation and honest completion

#### A. Keep owner-specific authority; centralize execution obligations

Introduce a small Life-internal orchestration boundary (working name
`maintain_life_owner_change`) using existing Plan, Occasion, Outcome and
retained-source adapters. Reuse builders and fences; do not create a universal
owner model or merge domain-specific authority into a generic callback.

The boundary accepts typed owner identity, viewer scope, target projection
version, event/repair identity and reason. It loads current authority and
previous indexed state, prepares required changes, publishes, and returns a
typed result. Pure tests may inject collaborators; runtime callers must use one
explicit adapter registry, not optional organization callbacks whose omission
changes correctness.

Proposed result dimensions, internal until reviewed:

- observed owner/dependency revisions and maintained projection version;
- index result: applied, already current, withdrawn or not applicable;
- organization result: current, changed, valid no-link, unsupported, retryable
  or blocked, with affected-scope identity and repair reason;
- completion: complete, superseded with a durable successor, or pending;
- durable continuation/checkpoint identity when one exists.

Only required stages determine completion. Unsupported organization coverage
may be reported while authorized original/index work completes; it must not
be counted as complete organization or silently loop forever. An ambiguous
association may validly remain unplaced. An accepted identity resolution that
still requires repair is pending correctness work, not that valid no-link case.
Telemetry is content-free and separates index progress, organization progress,
pending age, retries, supersession and unsupported coverage.

#### B. Close the transaction boundary for bounded deterministic maintenance

For the currently bounded Plan/Occasion path, prefer one short derived
transaction covering the fenced index write and required organization changes.
Extract narrow in-transaction primitives from existing repository functions;
keep standalone wrappers for appropriate callers. Do not call helpers that
open another `get_tx()` and assume the outer transaction makes them atomic.

Prepare candidates outside the transaction. Inside it, recheck the canonical
owner, relevant policy/dependency revisions, controls, and expected group
content. Then apply normalized rows, memberships, identity-resolution effects,
reverse-dependency changes and affected read epochs together. Audit the lock
order across publication, detach/Undo, topology and resolution before combining
them; preserve sorted multi-group locking and the topology scope lock where
needed. Any conflicting evidence causes a fresh preparation/retry, not a stale
proposal applied after a newer index write. No model/provider calls or full
corpus scans occur under these locks.

If an existing resolution operation cannot safely fit that bounded transaction,
retain the original Life event as unfinished, durably identify the remaining
scope, and recheck current authority in its own publication transaction. Do
not retain the present commit-index/ignore-repair behavior as a fallback.

#### C. Make every entry path use the same completion rule

| Entry path | Required change |
| --- | --- |
| Live `life_projection.changed` subscribers | Dispatch through the runtime maintainer; acknowledge only required completed work or a safely recorded handoff |
| Duplicate/replay | Re-evaluate missing organization even if index revision is current; unchanged completed work does not churn epochs |
| Backfill | Replace bare projector dispatch and index-only skip with maintenance-aware completion; preserve existing budgets, leases and family checkpoints |
| Reverse reconciliation | Compare required organization/dependency state as well as index state; absence remains owner-proven, never inferred from omission |
| Withdrawal | Immediately invalidate eligibility; remove only unsupported derived relations and preview/count support, retaining independent originals/evidence |
| Explicit restore | Replayed authorized restore converges even after an earlier index restore committed; current exclusions and grants still apply |
| Stale event | Never publish its stale payload; complete it only when current state needs no work or a reachable successor owns that work |

Replace the retained-source event's whole-viewer index lookup with the existing
exact record-state operation, extending its returned lifecycle fields if needed.
Keep bulk/reconciliation enumeration explicitly separate; eliminate the API
shape that returns an unbounded mapping for one call and a bounded tuple for
another when touching those callers.

#### D. Bounded continuation, when the affected set exceeds a transaction

The existing Life outbox owns live-delivery recovery; existing backfill run
rows own historical progress. Keep them. The first implementation should retain
unfinished events for retry without adding a scheduler or another source queue.

Before expanding to fan-out beyond a bounded transaction, review a minimal
consumer-progress extension to that Life journal. Preferred shape: separate
consumer-owned checkpoint metadata, not mutations to the immutable source-event
payload. Record maintainer version, viewer/target scope, stage, stable scan
cursor, examined revision/epoch, pending reason and supersession evidence.
Use the existing event identity, lease token and retry schedule. Do not persist
raw source content or an unbounded list of members in that checkpoint.

Each slice commits its derived changes and checkpoint together under the
current lease. A reclaimed worker cannot advance progress or acknowledge.
Moving evidence to another group requires revisiting both old and new scopes;
an interrupted scan must not skip them. Newer owner revisions invalidate stale
prepared work. A successor may subsume prior work only if withdrawal, restore,
exclusion and both parent repairs are preserved. Terminal unsupported/blocked
work gets a visible operator reason and resumable recovery, not rapid endless
retry or a user-facing maintenance queue.

Shared table/model changes remain a reviewed migration proposal, not something
approved by this text. Until continuation persistence exists, do not acknowledge
a truncated correctness operation as complete.

#### E. Reviewable commit order and acceptance

1. Add failing regressions for discarded repair, current-index/missing-group
   replay, and live/backfill divergence using existing tests and adapters.
2. Add typed maintenance results and runtime dispatch; wire required completion
   through event handling. No public API change is necessary for this step.
3. Close the publication transaction/fence boundary and add controlled race
   tests. A callback throwing after index work must not strand organization.
4. Adopt the maintainer in backfill/reconciliation; make exact source lookups
   bounded. Test already-current, withdrawal, restoration and stale successors.
5. Add continuation persistence only for the demonstrated affected-scope need,
   with schema review, lease-loss/interruption tests and operator diagnostics.
6. Update this roadmap with actual commits, commands, gaps and next checkpoint.

**M1 exit:** live, replay, backfill and repair yield equivalent required index,
organization and eligibility state for currently supported adapters. There is
no success acknowledgement while required repair has no durable owner. Include
newer revision overtaking old organization, withdrawal between prepare/publish,
duplicate restore, lease takeover, merge/split repair, and user detach racing
materialization. Use synchronization barriers, not timing sleeps, for races.

### 13.6 M2 — turn admitted evidence into maintained experience

Do not repeat `LifeEvidenceUnit`, group/link storage, content epochs or the
complete-set reconciliation foundation. Connect their real inputs and callers.

**Owner handoff:** Capture supplies an authorized bounded evidence/locator read;
Life consumes it. Agree its exact method/shape before editing source-owned
transactions. Existing content-free events trigger reads but do not grant an
`organization` purpose merely because they allow `source_refind` or repair.
Map every required envelope field to a real owner field or mark it unavailable.

| Evidence | Minimum usable owner information | Missing-data treatment |
| --- | --- | --- |
| Retained original | Exact source/owner identity, revision, lawful custody, original route and current eligibility | Preserve findability; no graph object required |
| Time | Role, supported interval, precision/timezone or explicit unknown | Import/capture time cannot masquerade as occurrence; undated material stays findable |
| Place | Resolved Place reference and evidence basis | Do not geocode a label or infer a visit merely to fill the lens |
| People | Author/contributor/subject/attendee roles when owner-supported | Mention is not attendance; preserve separate perspectives |
| Multi-event source | Stable locator and locator revision for each supported unit | No selective event attachment from an undifferentiated whole-source note |
| Lifecycle/dependencies | Current owner/grant checks, dependency identities, correction/withdrawal/restore coverage | Unsupported scope is withheld; independent support remains |

Implement the deterministic path with bounded affected-neighborhood reads:
explicit owner context and links first, compatible time/place for candidate
selection second, unsupported associations left unplaced. Preserve one default
containment path plus typed cross-links. Calendar references do not create a
second journey; two dinners at the same restaurant do not become one event.
Explicit continuity can connect episodes without turning a thread into a task.

Use indexed reverse dependencies to discover prior and new affected groups.
Audit existing membership-by-record lookup and shared dependency stores first;
JSON evidence is useful provenance but is not a complete reverse-repair index.
Add only the missing relational edges through a reviewed migration. Track exact
support so retracting one source does not erase another participant's account.
Repairs must reach transferred memberships and redirected identities, not only
the original owner group.

Human controls and accepted identity choices are durable inputs. Verify their
mapping across projection versions: current storage scopes groups/controls by
projection version, so rebuilding into a new version must explicitly port or
resolve them. A new target version must not reset exclusions or mint a new
episode merely because its title or members changed. This is part of rebuild
acceptance, separate from algorithm re-derivation.

**M2 exit portfolio:** W1 cross-month journey; W2 source-only ordinary week;
W3 explicitly continued attention; W4 attributed shared occasion with two
viewer scopes; W5 retained-but-not-lived evidence. Test late import, sparse/no
photo, negative occurrence, conflicting accounts, source move, revoke/restore,
and durable rename/detach. For each, report real-owner coverage separately from
fixture-only expectations. W6 reserves composition authorship; it is not a
reason to build an editor now or to declare that owner implemented.

### 13.7 M3 — one semantic reader contract, several bounded operations

Extend `corpus_query.py`, indexed adapters and the existing Life models/routes.
Keep the legacy snapshot implementation dark-switch compatible until acceptance;
do not switch the public route merely because the new query compiles.

Share viewer, target version, owner eligibility, stable record/group identity,
time semantics, typed count units and destination resolution. Keep specialized
query plans for distinct jobs:

| Operation | Required result and bound |
| --- | --- |
| Root digest | Finite recognizable groups with eligible preview, count unit, stable handle and coverage; no full-history collection to choose a handful of rows |
| Group depth | Metadata, immediate child handles and paged eligible members; preserve independent child/member continuations and freshness fences |
| Exact original | Direct identity lookup/readback through its owner; no requirement to traverse episodes or paginate all history |
| Everything kept | Paged custody-oriented originals, including represented originals through canonical mapping; display deduplication does not delete witnesses |
| Refinding | Exact/lexical/contextual retrieval over supported corpus families, opening the same objects and preserving negative/unknown occurrence truth |
| Anchor resolution | Seek an eligible record/group/block and its local continuation by stable identity; do not make mobile scan all preceding pages |

The internal group reader is not sufficient public authorization by itself.
Compose bounded current-owner/purpose/audience checks before returning visible
text, previews, counts or source access. A stored group, cached audience, old
cursor or repeatable-read snapshot is not an authorization grant. Define the
response's eligibility checkpoint, fail closed on unknown restricted support,
and preserve safe independent originals. Observe current restrictions even
when chronology is pinned to an earlier represented-at time.

Bind continuations to viewer/version/lens/scope and appropriate content epoch;
extend the shadow index cursor before exposing it as a public continuation.
Keep a consistent short database snapshot per bounded response and release it
before the next request. Cap scanned candidates as well as returned rows; a
sparse filtered page returns honest continuation/coverage. Unrelated group
changes should not force an exact open reader to restart. Scope invalidation
as narrowly as justified, retaining explicit stale-cursor handling.

Migration work moves `ensure_timeline_projected` and historical gathering off
the future GET path into existing maintenance/backfill. Retained Atlas/booking
evidence stays readable until its owner mapping and original routes are
certified. Refinding's envelope can survive while its substrate changes.
Add dependency-safe reuse for digest previews; do not invoke models on reads.

**M3 exit:** root, group, original and refinding agree on identity/eligibility;
query-count/rows-scanned tests show bounded work; source removal changes all
dependent counts/previews; repeated small-page reads have no duplicates or
omissions within unchanged scope; direct old-record access requires no lifetime
scan. Public models/routes require schema review and the workspace sync workflow.

### 13.8 M4 — connect the four-lens experience and cross-root continuity

Reuse `components/life/LifeRootV1Screen.tsx`, `app/you/life-record.tsx`,
`data/rootProjections.ts`, exact resource routing and reading-position storage.
The current shell and cursor recovery are foundations, not replacements to
rewrite. Detailed visual composition stays in the approved Life design lane.

- **Time:** recognizable periods/journeys/episodes, truthful date roles and
  direct access to originals. Late imports enrich their supported period.
- **Places:** distinguish visits and kept-not-lived material at the same Place;
  do not recreate the Places discovery feed inside Life.
- **People:** shared records and actual contributions with attribution and
  viewer-relative visibility; no person dossier or implicit relationship score.
- **Threads:** supported steps across moments, with complete useful material;
  no unresolved-task count or prompt to finish a personal project.

Adopt typed group/original destinations without implementing a parallel entity
shell. Preserve origin/lens/record anchor through Home or Places → Life →
original → back. A missing or split target gets exact unavailable/choice
readback, never an arbitrary child or generic archive substitution. Deep anchor
restoration uses M3's seek operation. Preserve empty, thin, yielded, partial,
offline, stale-cursor and retry states without adding filing homework.

Before implementation, agree the exact destination and eligible revision
contract with Home/Places/Integration. Their roots consume it; they do not
write Life state or depend on Life rendering to activate the live engine.
Current production/reuse owners remain responsible for generated-result
invalidation; React Query invalidation is only foreground freshness.

**M4 exit:** run `scripts/sync-types.sh` from the correctly paired workspace;
review full OpenAPI, active app projection and generated TypeScript; then run
focused Jest, typecheck and operation governance. W1–W5 work through the
actual data contracts, not mobile-only invented projections. Device and visual
acceptance remain explicitly deferred until resumed through the app's QA path;
no screenshot or usability claim follows from Jest.

### 13.9 M5 — useful organization, optional models, and substantive Returns

Begin the evaluation dataset with M1 and add assertions as M2/M3 connect. Reuse
existing W1–W6 fixtures, validators and rehearsal reporting rather than create
another quality framework. Track both required links and forbidden joins;
an organizer that leaves everything unplaced is not automatically good.

Report exact-original findability, recognizable episode coverage, multiple
visits kept distinct, attributed contribution recovery, stable controls/IDs,
visible churn during updates, bounded query cost and maintenance lag. Keep
index parity, organization usefulness, model quality and native usability as
separate evidence levels. Resource budgets must be explicit before promotion;
measure a local baseline before promising latency or throughput numbers.

B0/B1 deterministic behavior is the mandatory comparison. Evaluate B2 model
assistance only on evidenced misses with authorized data/budget, held-out
variants and the existing model registry/gateway. The model returns bounded,
evidence-addressed relationship proposals or abstention. It cannot create
occurrence truth, durable personal traits, permissions, identity decisions or
silent edits to authored material. Preserve useful output when model work is
unavailable; hard truth/audience/control failures cannot be averaged away.

R7's first Return family should use the existing production/reuse contract,
versioned evidence and cross-root allocation. It must contribute reconstruction,
explanation or a supported new distinction, not paraphrase the user's attention
or ask for more input. Separate generating value from choosing its surface.
Manual-first composition remains later: select its custody owner, authored
block/version model and edit-preservation rules before any saved-editor API.

### 13.10 M6 — certify replacement before activation or deletion

Use R8 and §11/§12 acceptance, adding the maintained-organization evidence:

1. Inventory all retained Atlas/source families and exact legacy destinations;
   account for represented originals, private/shared scopes and negative truth.
2. Rebuild a shadow target from current owners plus durable controls/identity
   decisions. Catch up through the same M1 operation. Non-default targets remain
   historical until their explicit live-fanout mechanism is implemented and
   verified; capability metadata alone is not freshness.
3. Compare raw coverage and authority independently of richer presentation.
   Test historical-schema upgrades, race recovery, dependency repair, targeted
   source access, query budgets and cross-version control survival.
4. Prepare reader rollback that preserves current revocations, exact-original
   routes and user controls. Document any old-reader limitation rather than
   silently falling back to unsafe or incomplete content.
5. Obtain relevant native acceptance and explicit serving/production authority.
   Integrate a reviewed candidate with its actual generated contracts. Only
   then activate using the owning rollout process and observe lag/errors.
6. After accepted replacement and its agreed rollback window, separately
   approve removal of Atlas presentation, obsolete call paths and eventually
   storage. Retain necessary historical ownership/read mappings. No blanket
   deletion based on an `atlas` filename search.

### 13.11 Dependencies, unblocked work and first checkpoint

| Adjacent owner | Exact interface/decision needed | Life can continue without it |
| --- | --- | --- |
| Capture | Revisioned, purpose-authorized bounded evidence units/locators; original-to-representation mapping; current eligibility and lifecycle repair identity | M1; evidence consumer/contract tests; exact-original lookup; safe source-only retention/refinding |
| Graph / social | Author/participant roles, claim/occurrence truth, current/former viewer fan-out, owner revisions and explicit restoration | Existing Plan/Occasion/Outcome maintenance; viewer-isolation tests; mark additional real-owner coverage unsupported |
| Integration | Reviewed branch baseline, shared schema landing, target-version live-fanout and eventual activation authority | Isolated owned work and local regressions; no unilateral merge or producer changes |
| Home / Places | Exact record/group/original destination, eligible revision and return anchor; generated-result repair ownership | Life query/destination fixtures and depth implementation; do not edit their composition policy |
| Design / mobile | Approved semantic anatomy and sparse/error/redirect states; final geometry later | Backend contracts, generated types, existing component integration and non-device tests |
| Founder / canon | Any adoption of pre-Plan intention, ordinary-Ask continuity, wider social use or later composition custody | All already-authorized evidence/organization work; do not reinterpret an open proposal as permission |

**First checkpoint to execute:** M0's focused baseline delta followed by M1's
regressions, maintainer completion contract, bounded transaction/fence repair,
and live/backfill adoption. Start M2's field availability matrix and M3's
reader examples alongside it, without waiting for every visual decision.

After each connected package, append commits, test commands/results, remaining
owner/activation gaps and next checkpoint here. Maintain the execution-status
pointer; offer an exact handoff for shared contracts rather than editing the
concurrently active integration register or source producer independently.
If Capture's evidence read is unavailable, name the blocked W2/W3/W4 behavior
and continue maintenance, safe originals, readers and fixtures. Do not call a
fixture stub production coverage or declare Life complete after the first owner.

### 13.12 Planning verification and mutation boundary

This pass rechecked branch/worktree/dirty state, the live workspace coordination
register, source/contribution policy, Life experience contract, prior execution
packets, and the relevant projector/outbox/backfill/evidence/reader extension
points. It edited only the isolated Life roadmap, companion system-design
amendment and execution-status pointer. Scoped lifecycle metadata validation
passed for all three documents; all 66 relative link targets and the new section
anchors resolve (child-repository links checked against the canonical
workspace); `git diff --check` passed. Review test results in §13.2 are from
the preceding architecture review, not a new connected run in this planning
turn. No code, schema, database, mobile UI, design project, deployment or remote
branch was changed. The planning edits and execution receipts are committed in
the isolated documentation lane; no source-owned producer, public reader,
mobile UI, deployment or remote branch was changed by this section.

### 13.13 Execution receipt — M0/M1 and conservative M2 follow-through — September 7

The first architecture checkpoint is now executed in bounded packages on the
isolated Life backend branch. M0's branch/dirty-state and dependency audit was
performed before mutation; no concurrent source-owned or mobile work was
swept into the lane. M1's shared maintainer is implemented by commits
`0b822c3aa`, `767f70499`, `91024a856` and `3a44caf0f`: live owner delivery,
non-dry-run backfill and reverse reconciliation now share typed completion;
stale successors are superseded; explicit retained-source restoration uses an
exact owner-state read; target projection versions survive the identifier-only
bridge; and index plus primary Plan/Occasion owner-group publication share one
short transaction. Resolution repair remains a bounded post-commit stage and
is surfaced as pending rather than acknowledged as complete.

The conservative M2 consumer seam is `bac99b1b0`. It exposes retained-source
capture-time evidence with exact source references and owner revision while
rejecting that unit as occurrence proof. Capture producers and source-owned
transactions were not changed. The complete Life projection selection passes
**238 tests** on the local PostgreSQL-backed environment with API-key cases
excluded; focused maintenance, backfill, reconciliation, delivery, restore,
ordering and evidence regressions are included. Backend repository-wide
size-budget and status-dead-gate hooks remain pre-existing baseline failures
and were explicitly skipped only for these commits; other applicable hooks and
whitespace checks pass.

The first bounded M3 reader seam is `bb2677abd` plus the fail-closed follow-up
`f0a8d4f69` (`fix(life): reject unscoped index cursors`). Newly issued
derived-index cursors now carry viewer, lens and projection-version scope;
replaying a cursor across any of those dimensions, or passing a legacy
two-field cursor to a repository reader, is rejected before the bounded SQL
query. Invalid lens values fail closed. Legacy two-field cursors remain
accepted only by pure comparison fixtures; repository readers always bind the
new scope fields. Focused index, typed-reader, comparator and connected corpus
checks pass. The Life package passes **226 tests** when the unrelated root-route
test is excluded because this isolated worktree does not have the pre-existing
`openai` dependency; collection failure is recorded rather than presented as
a Life regression. This closes only the internal cursor boundary: public route
wiring, complete authorization composition, scanned-candidate budgets and
serving cutover remain M3 work.

These receipts do not close M2's richer evidence contract, M3 bounded public
reader composition, M4 mobile receiving, M5 evaluation/Returns, or M6
replacement/Atlas retirement. The next checkpoint is either Capture's agreed
occurred/place/people/locator read or a demonstrated affected scope that
requires reviewed multi-slice continuation metadata. Until then, keep Life
shadow-only, preserve unsupported owner coverage, and do not merge, push,
activate readers, migrate/delete Atlas, or add another indexing framework.
