---
doc_type: working
status: active
owner: founder / coordination task
created: 2026-09-07
last_verified: 2026-09-26
expires: 2026-10-07
why_new: Owns the single current execution queue, accountable packages and system reassessment without duplicating product or implementation contracts.
supersedes:
  - current assignments and sequencing in the historical program and Integration roadmaps
source_of_truth_for:
  - cross-lane program priorities and accountable assignments
  - cross-lane dependency routing and system reassessment
depends_on:
  - ../decisions/2026-09-06-reconcile-consumer-strategy.md
  - ../systems/four-root-loop-object-surface.md
  - ../systems/contribution-and-consequence.md
---

# Vesper program roadmap

## Current direction — September 25

Build a coherent product from the capabilities already implemented. Treat the
merged recovery work as the working baseline; then execute
**complete Home value delivery on that system**: supported material reaching
useful composition, polished presentation, meaningful depth/action and return.
Do not start overlapping Home work from older main or mistake a thin screen
for a presentation-only problem.
This is a delivery priority, not a narrower product thesis or a requirement to
prove one behavior loop before designing the system.

Vesper's four moves remain **Make sense. Open possibility. Help it work. Carry
forward.** Home returns value for now and the anticipated future; Places opens
the situated world; Chat makes bringing and asking easy; Life organizes what
the person can revisit. Multiplayer and practical adaptation run through these
experiences rather than becoming separate products. Follow the
[Product Thesis](../../travel-agent/docs/product/Product%20Thesis.md) and
[four-root contract](../systems/four-root-loop-object-surface.md).

This file is the only current dispatch queue. The
[integration reference](complete-system-integration-roadmap-2026-09-05.md)
preserves technical obligations, not a second schedule. Specialist plans supply
detail only when a package below invokes them. Historical receipts are in the
[program archive](../archive/vesper-program-roadmap-history-through-2026-09-25.md) and
[integration archive](../archive/complete-system-integration-history-through-2026-09-25.md).

## Inspected baseline and evidence limits

The recovery baseline is now merged. The three authorized PRs landed on the
independent repository mains on September 26 UTC; original branch protections
were restored and verified afterward:

| Repository | Merged main revision | Landing |
| --- | --- | --- |
| Workspace | `6ef3dca09be2b4ea40c83ae21d8cbf112ee17f24` | [#36](https://github.com/fy538/travel-workspace/pull/36) |
| Backend | `c8c9f578594a98beb41300c1a780f86ebb30eca4` | [#233](https://github.com/fy538/travel-agent/pull/233) |
| App | `43225df35a01295993def384b5958c53ab8f1c8b` | [#201](https://github.com/fy538/travel-app/pull/201) |

The current implementation owner is the coordinated `codex/home-value-delivery`
lane. Its workspace checkout carries local roadmap/execution-record commits
after the merged baseline; its backend checkout remains at merged revision
`c8c9f57`.
Its app checkout has the first H1 share-time treatment committed locally as
`66e2c3c`, renderer-level owner-read regression coverage in `122f4d2`, and an
explicit UTC fallback correction in `e0bf0a7`. The latest app slice,
`8fc767355`, preserves the Home unit's viewport position on return when the
same projection remains valid; if it changed, Home retains strict recomposition.
Its focused check passed (4 suites, 53 tests), TypeScript and targeted ESLint.
A seven-posture native fixture capture now exists on the lane simulator;
design-reference acceptance, real-owner readback, the full verification gate
and release readiness remain open. Do not treat the coordinated lane as ready
to publish.
The older recovery worktree and detached native-presentation checkout are
separate, already-merged work; do not reuse or retire them without a fresh
owner/runtime check. The former 145-branch inventory is historical, not
today's state.

At landing, backend/app CI reported passed. The workspace reliability job failed
at private-backend checkout authentication before product tests, and its
Maestro smoke was skipped. Those are not product-test results. The merged PRs
are landed, but the workspace full gate, a clean combined verification,
production-data acceptance, design-reference parity and release readiness have
not thereby been certified. No branch
protection bypass is currently in effect.

Code inspection confirms an existing bounded Home owner portfolio, application
composer, native root experience, semantic renderer registry and exact-return
machinery. The app registry currently lists 20 renderable Home kinds. A kind's
presence does not establish sufficient supply, attractive composition or full
design parity. The September 22 test totals in the archives are dated evidence;
the targeted checks run during H1 are recorded in its active execution plan.
External design hashes and release readiness remain unverified. No
percentage-complete claim is supported by this inspection.

Two additional implementation boundaries change H1's scope. Ordinary Home reads
consume prepared Source results without generating/enqueueing work; the existing
controlled Source worker accepts explicit preparation, not arbitrary signal-based
production. Recurring useful supply must therefore be traced, not assumed from
the presence of a generator. Separately, the registered `home-root` QA surface
currently has no visual `designRefs` and judges against doctrine. Select/adopt
and register the specific accepted Home references before claiming Claude-design
parity; the old external Home-surfaces registry is not blanket authority for it.

Documentation validation on this rebaseline: `python3 scripts/check_docs.py
--all` passed, including the compatibility ledger checks. The expired bridge
entries found in the older main-based inspection were reconciled by the merged
recovery work; they are not current blockers. Do not carry that stale finding
forward or reopen the repair without new evidence.

## One queue, bounded work in progress

| Order / state | Package and accountable owner | Outcome / exit |
| --- | --- | --- |
| 0 — complete | **Recovered candidate baseline**, merged through #36 / #233 / #201 | Reuse recovered Home/Places and app behavior; original protections restored. The workspace checkout/reliability gate remains a pre-publication evidence gap, not a reason to reopen or bypass the merged PRs |
| 1 — active | **H1: Complete Home value delivery**, `codex/home-value-delivery` lane owner | Execute the [bounded package](home-value-composition-execution-plan-2026-09-25.md): close supply/selection/presentation/continuation gaps across ordinary, social and healthy live situations; include accepted native reference alignment. The first social-material refinement now shows exact recipient-local share time on a currently revalidated original (`66e2c3c`); package exit is not yet met |
| 2 — select from H1's actual bottleneck, not tab order | **Recurring supply / Places depth / Life continuity**, same owner by default | Choose the specific missing producer connection, spatial depth, refinding or permitted later-use path that most improves the delivered experience; do not activate three standing lanes |
| Cross-cutting within each package | **Practical help, live-engine behavior and production cost**, package owner | Current facts and permitted context materially change an appropriate result; freshness, authority, degradation, latency and generation costs stay explicit |
| Before publishing each integrated package / before cutover | **Landing and retirement**, implementation owner with coordination review | Review combined changes, run required gates, publish only with authorization, record landed revisions and disposition the branch/worktree; migrations, replacement retirement and release retain their separate gates |

H1 includes existing multiplayer and practical value from the start, not only
editorial content. It may resolve a narrow dependency in another surface without
rewriting that surface. Later packages are candidates, not estimated commitments.
At the first working result, choose the next package from the exposed bottleneck.
No speculative subsystem, new retention grant or ambient production policy is
authorized by this table.

A second implementation task is optional, not the default. Start it only with
an independent outcome, disjoint write ownership, stable shared contracts and
available review/landing capacity. A useful candidate is a bounded Life
refinding/media gap that does not change H1's owner or navigation contracts.
If those conditions fail, use one implementation owner with temporary bounded
workers instead. Do not create permanent lanes for every product domain.

## Operating model

- **Coordination task:** owns this queue, consequential decisions and reviews of
  the combined product. It does not relay every technical message or routinely
  implement large slices. A new coordination task can take over from this file;
  a very long conversation is not the source of truth.
- **Implementation task:** owns one coherent outcome through inspection,
  implementation, focused tests, review corrections and handoff. Continue across
  ordinary obstacles; stop only at a genuine missing authority or dependency.
  Start a fresh task when the outcome changes, not for every commit.
- **Temporary workers/reviewers:** use only when delegation is authorized and
  work is concrete and independent. Give file ownership, interfaces, finish
  conditions and evidence boundaries. Keep shared schemas/navigation with one
  owner. A reviewer is not proof; resolve findings against code and tests.
- **Integration is a responsibility, not a permanent waiting lane.** Integrate
  a coherent, reviewable package, or earlier for a changing shared contract.
  Do not force a combined environment after every small change; do not leave
  completed work indefinitely on disconnected branches either.

Use the existing [workspace lane lifecycle](../Workspace%20Repo%20Setup.md)
and root `AGENTS.md`; do not create another registry or enforcement service.
One package has one owner until its branch is landed, intentionally held, or
discarded with authorization. Report residual worktree/branch disposition at
handoff. Do not switch another task's checkout or assume isolation includes
devices and services.

## Checkpoints and roadmap maintenance

Check in at the **first working result, a consequential blocker, and the final
reviewed result**. Ordinary debugging and successful intermediate tests need no
founder round trip. Owners coordinate interfaces directly; coordination resolves
priority conflicts and changes to product, authority or architecture.

At a checkpoint ask:

1. What can a person now receive or accomplish that they could not before?
2. Does context materially improve it, and how much work remains with them?
3. Did we reuse the right owners, or add competing state/policy/generation?
4. What evidence is current, and what remains mocked, unrun or blocked?
5. Is the next package still the best investment?

Update this file's baseline, package state and next decision in place. Do not
prepend another “current override.” Keep implementation details and the latest
verification receipt in the active package; keep large historical evidence in
closed package records. Do not duplicate test counts across both roadmaps.
Retire the package's active status when finished. At most one or two execution
plans are active; product/system/design references do not count as execution
queues. Review this working roadmap by its expiry rather than silently extending
dated claims.

Judge execution by completed consumer outcomes, rework, blocked time and founder
intervention, with actual measurements when making productivity claims. Agent
count, commit count and document volume are not progress measures.

## Historical link compatibility

These anchors preserve older references. They do not reactivate old queues.

<a id="2-inspected-baseline--september-22"></a>
<a id="2-inspected-baseline--september-8-after-reliability-landing"></a>
Historical baselines: [September 22](../archive/vesper-program-roadmap-history-through-2026-09-25.md#2-inspected-baseline--september-22)
and [September 8](../archive/vesper-program-roadmap-history-through-2026-09-25.md#historical-september-8-reliability-and-acceptance-evidence).

<a id="4-current-package-register"></a>
<a id="6-coordination-completion-and-next-system-review"></a>
<a id="7-current-acceptance-round--dispatched-september-8"></a>
Historical [package register](../archive/vesper-program-roadmap-history-through-2026-09-25.md#4-current-package-register),
[system review](../archive/vesper-program-roadmap-history-through-2026-09-25.md#6-coordination-completion-and-next-system-review)
and [acceptance round](../archive/vesper-program-roadmap-history-through-2026-09-25.md#7-current-acceptance-round--dispatched-september-8).

<a id="connected-dogfood-experience"></a>
<a id="current-round--meaning-based-discovery-and-exact-original-receiving"></a>
<a id="execution-order-and-event-triggered-reviews"></a>
Historical [connected experience record](../archive/vesper-program-roadmap-history-through-2026-09-25.md),
[discovery/receiving round](../archive/vesper-program-roadmap-history-through-2026-09-25.md#current-round--meaning-based-discovery-and-exact-original-receiving)
and [execution order](../archive/vesper-program-roadmap-history-through-2026-09-25.md#execution-order-and-event-triggered-reviews).
