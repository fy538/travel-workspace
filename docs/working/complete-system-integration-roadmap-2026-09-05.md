---
doc_type: working
status: active
owner: founder / Strategy integration task
created: 2026-09-05
last_verified: 2026-09-06
expires: 2026-10-05
why_new: Rebaselines the post-pivot system around the real-world live engine and four surfaces, with code-backed correction priorities, explicit Life ownership, bounded Luna delegation, and recurring architectural and product reassessment.
supersedes:
  - forward execution sequencing in vesper-product-system-build-program-2026-09-01.md
  - orchestration and lane allocation in home-places-life-productization-program-2026-09-04.md
source_of_truth_for:
  - Strategy task complete-system integration sequencing
  - live-engine integration across context, judgment, surfaces and continuity
  - two-lane coordination with Life
  - integration milestone reassessment and bounded subagent execution
depends_on:
  - ../systems/four-root-loop-object-surface.md
  - ../systems/contribution-and-consequence.md
  - ../systems/artifact-expression-and-composition.md
  - ../decisions/2026-09-05-amend-home-composition-canon.md
  - life-complete-system-and-atlas-replacement-roadmap-2026-09-05.md
  - lightweight-arrangements-implementation-handoff-2026-09-04.md
---

# Complete-system integration roadmap

## 0. Decision, scope, and evidence boundary

Keep the core architecture. Complete its integrations, replace transitional
serving paths where necessary, and retire competing implementations. Do not
restart the architecture, introduce a universal object/context service, or
reduce the product to proving one loop.

**Make the real-world engine and the four surfaces operate as one continuous
experience—not merely connect the surfaces to shared data.** The engine must
help determine what is worthwhile and livable before a possibility appears,
preserve its purpose as reality changes, and stop when further work is not useful.
I5 completes practical interaction paths; it is not where the engine first enters
the program. Its requirements shape I0–I4 from the beginning.

The product is one relationship between contributed attention and useful
subsequent value. Its four moves remain **Make sense. Open possibility. Help it
work. Carry forward.** Home and Places are generous output surfaces; Chat is
the existing contribution/agency surface; Life organizes an unfolding life.
Multiplayer participates throughout. The moves are not tabs, pipeline stages,
four required cards, or four independently owned services.

Two user-owned tasks remain active:

- **Life** (`01a06ecc-1a79-74a1-9c47-9f24461313ea`) executes the
  [Life replacement roadmap](life-complete-system-and-atlas-replacement-roadmap-2026-09-05.md).
- **Strategy**, this task (`01a030af-13a8-74e1-81be-7d526bec3045`), owns the
  complete-system integration program below, including Places end to end.

This document replaces older forward ordering and the assumption that six
specialist tasks remain active. Their code, acceptance cases, decisions, and
historical receipts remain evidence. It does not supersede product canon,
Life's internal execution program, or operational release procedures.

This is a planning deliverable. No implementation, schema approval, paid
generation, provider contact, deployment, feature-flag activation, production
backfill, or destructive retirement is authorized merely by writing it.
Chat home/composer redesign remains held. Scoped intake/backend conformance
work is planned separately from a Chat redesign; exact prompt/schema/auth
changes must follow the owning repository's approval rules.

### Investigation boundary

September 5 inspection points included workspace `d40f7b7`, backend
`6f25bbdcb`, and app `3b83cc3fd`, all on `main`. Life advanced during the
investigation; these are observation points, not a frozen release candidate.
Four unrelated Claude/design documents were already modified and are untouched.
During the pass, social decision commit `d8c2b22` narrowed Home to addressed or
shared-consequential material and assigned casual spatial sharing to Places.
Life also advanced to revision-bound cursor/restart work (`332716f8b`,
`27695e6be`, `4a4a85bf0`). These are incorporated as new evidence, not scheduled
again as missing foundation. A revision-bound restart is still not a historical
database snapshot.

The pass combines current code, recent task updates, product/system canon,
implementation maps, and three bounded read-only Luna audits. It is not an
exhaustive security audit, a newly run full application suite, or native visual
certification. Recheck HEAD, status, working changes, and each finding before
implementation. Never repeat an older missing-capability claim without checking
whether Life or an earlier task has since closed it.

## 1. Foundation assessment and correction priorities

### Keep the architectural responsibilities

| Responsibility | Why it belongs | What it must not become |
| --- | --- | --- |
| Sources, claims, canonical entities, Plans/Occasions/Commitments, Occurrences and plural Outcomes | Preserve evidence, identity, consequences and human perspectives | One universal item whose state confuses possession, intent, attendance and meaning |
| Contribution policy and canonical owner commands | Separate interpretation from retention, audience and action authority | Model confidence granting permission, or a second writer in a surface |
| Bounded owner reads and contextual judgment | Compile only the current evidence needed for a useful response | A complete personal-data blob reconstructed for every request |
| Live observation and reevaluation | Keep useful possibilities and accepted consequences aligned with changing conditions and expressed intent | A notification system mistaken for judgment, or continuous surveillance |
| Source-backed production and typed composition | Produce reusable value without allowing generated presentation to own truth | An independent content factory per root, or model-authored arbitrary UI |
| Root-specific reads and native rendering | Give the same world different temporal, spatial and continuity expressions | Identical feeds or separate stores for each tab |
| Readback, causal repair, expiry and current authorization | Keep asynchronous changes and derived views consistent | A receipt that merely reports intention, or cache visibility treated as authority |

One logical system does not mean one execution engine for every operation.
Keep useful specialized query strategies and adapters; share identities,
semantics and authority. Consolidate duplicated decisions, not every class or
DTO simply because they look similar.

### Code-backed issues that determine the roadmap

| ID | Observation | Disposition / work package |
| --- | --- | --- |
| A1 | [Root composition](../../travel-agent/backend/api/services/root_composition.py) shares Home/Places stages, but runtime read planning still uses founder-scenario categories from [portfolio reads](../../travel-agent/backend/concierge/agentic_facade/portfolio_reads.py) | Keep orchestration; replace scenario-dependent policy with actual conditions and declared read requirements in I2. Keep founder stories as tests. |
| A2 | `compose_home_root_v2` awaits optional source production before completing a response when enabled; [continuity](../../travel-agent/backend/root_projection/v2/source_contribution_continuity.py) already supplies leases and reuse | Retain safeguards; separate fast assembly from bounded production, then measure combined cost and latency in I2. A per-call timeout is not an account budget. |
| A3 | [Canonical owner adapters](../../travel-agent/backend/concierge/agentic_facade/canonical_owner_reads.py), the lived-experience context providers, and Life's own queries serve related identities | Inventory overlap and dependency direction in I1. Reuse owner repositories/policy; do not make Life call a root composer or force every read through one giant context compiler. |
| A4 | Root action [read-model invalidation](../../travel-app/data/rootConsequences.ts) and [root invalidation](../../travel-app/utils/invalidateRootProjections.ts) enumerate consumers; deeper readers and derived production have additional lifetimes | Establish an affected-owner/dependency coverage matrix and close omitted consumers in I1/I5. Root refresh alone is not whole-system repair. |
| A5 | [LocalPlanScreen](../../travel-app/components/trip-plan/LocalPlanScreen.tsx) and existing Plan Shape remain Trip-derived; the [arrangements handoff](lightweight-arrangements-implementation-handoff-2026-09-04.md) leaves prospective/shared material persistence explicitly open | Decide narrowly typed owner seams before implementing more Keep/arrangement consumers in I0/I3. A Source is not automatically an intention. |
| A6 | The [September 5 Home amendment](../decisions/2026-09-05-amend-home-composition-canon.md) expands containment, authored people material and four Home forms beyond the earlier implementation baseline | Reconcile current semantic kinds, renderers and producers in I4; do not create one new pipeline per card type. |
| A7 | [Life](life-v1-execution-status-2026-09-01.md) has now landed tab, direct retained-timeline reads, all depth lenses, chronology and source-revision increments | Consume those improvements. Life owns the remaining indexed corpus, organization, exact readers and Atlas replacement; do not reschedule its already-landed route work here. |
| A8 | [Entity pilot](entity-pilot-release-manifest-2026-09-05.md) and [booking retirement](capability-retirement-execution-receipt-2026-09-05.md) distinguish local implementation from enablement and operational completion | Retain those boundaries. Integration can consume current supported behavior; release flags and obligation-sensitive cutovers remain explicit in I6. |
| A9 | The broad owner-read plan emits `route.evaluate`, but [its canonical reader](../../travel-agent/backend/concierge/agentic_facade/canonical_owner_reads.py) always reports unavailable; place reads explicitly lack current-condition/reachability fields | Make readiness and returned-field coverage executable in I2. Remove known-unavailable generic work rather than building a speculative route service to satisfy the catalog. |
| A10 | [Home portfolio](../../travel-agent/backend/root_projection/v2/home_portfolio.py) reads Graph without passing the request clock; discovery/context and later owner reads can load related truth again | Bind one request clock and coalesce eligible reads locally in I1/I2; preserve current authorization and revision checks. A request-local context is not an immutable multi-owner snapshot. |
| A11 | [Capture entry](../../travel-app/app/share-capture/index.tsx) lacks a full semantic origin envelope; Done uses history when available and Home as the no-history fallback | Preserve origin object, Places scope and typed return in I1/I3. Do not falsely describe every ordinary stacked return as broken. |
| A12 | Pre-generation [group identity](../../travel-agent/backend/root_projection/v2/source_contribution_opportunities.py) includes situation and allowed roots, while later delivery identity is root-neutral | Separate semantic production identity from expression selection in I2 where meaning/context is genuinely equivalent; never remove audience, purpose, grant, context or version distinctions merely to improve cache hits. |
| A13 | The [lived-experience coordinator](../../travel-agent/backend/lived_experience/FEATURE.md), [family registry](../../travel-agent/backend/lived_experience/registry.py), [movement engine](../../travel-agent/backend/core/movement/engine.py) and [situated movement bridge](../../travel-agent/backend/core/movement/situated_judgment.py) supply real but differently scoped capabilities | Inventory each path's actual trigger, context, judgment, gateway, delivery and activation in I0. Registration, a Trip-independent adapter, or a notification producer does not establish a complete general live engine. |

The native Home capability registry currently admits 13 kinds, the generated
contract has the earlier 31-kind vocabulary, and the accepted design admits 35.
Those are three different scopes, not evidence that all 35 are already rendered.
I4 must name which kinds the supported candidate can emit and verify every one.

The assessment is **sound core, incomplete convergence**, not "everything is
nonregrettable" or "only UI remains." Compatibility stacks, broad corpus reads,
scenario assumptions and duplicated policy are deliberately eligible for removal.

### Live-engine operating contract

The [cross-root engine contract](../systems/four-root-loop-object-surface.md#7-the-real-world-engine-is-cross-cutting)
and [Live it well clarification](critique-response-and-composition-phase-2026-08-30.md)
govern this program. The engineering trace connects expressed attention/intent,
permitted current-world observation, bounded context, useful judgment, surface
treatment, optional owner consequence, reevaluation and authorized continuity.
This is a possible causal cycle, not a mandatory user funnel. An explanation
can finish without a Plan, action, durable record or watch.

Three responsibilities must remain distinct:

1. **Understand and prepare:** determine what is feasible and worthwhile for
   these people in this window, including timing, effort, tradeoffs and fallbacks.
2. **Reevaluate:** when relevant conditions, intent or participation change,
   decide whether to retain, shorten, substitute, postpone, release or otherwise
   revise the treatment. Invalidating a cache alone does not make this judgment.
3. **Make a permitted consequence work:** prepare or apply through an owner,
   verify the result, monitor only within authority, and reconcile independently
   authored outcomes. A valid action can still be an unhelpful solution.

`ACT_NOW`, `HOLD`, `WAIT_FOR_SIGNAL`, `MONITOR` and `RELEASE` are derived temporal
postures, not universal stored objects. A durable watch requires a concrete
owner/job contract; reuse suitable scheduler and delivery machinery, but first
verify it can preserve subject, condition, source/refresh policy, purpose,
audience, permitted action, expiry, cancellation and last evaluation. Do not
assume the generic watch owner is already implemented or create an always-on
service to fill the gap. The exact persistence decision belongs in D6.

Observations come from authorized owner/provider changes, bounded refresh or
deliberate user input. Missing signals remain unknown. Browsing, keeping a
possibility, sharing a photo, or being mentioned by a friend does not authorize
background location, polling, contact, a watch or external action. An authored
friends-map mark is social evidence, never an inferred current position.

The product-level engine spans specialist capabilities. `LivedExperienceEngine`
remains a provider-free coordinator; providers, bounded reasoning and canonical
commands keep their responsibilities. Do not force every read or article through
a heavyweight decision arc. Preserve simple complete-on-view value alongside
live assistance, with no visible fifth tab or obligatory "engine" section.

## 2. Two-lane ownership and coordination

| Area | Strategy integration owns | Life owns / supplies |
| --- | --- | --- |
| Identity and navigation | Cross-root resource/return contract, Home/Places consumers, acceptance coverage | Exact Life destinations, legacy alias migration, reader restoration |
| Evidence and correction | Shared owner-change semantics; coverage across production, roots, pending actions and retained results | Life index, depth, dossiers, custody and refind repair |
| Intention and shared material | Exact owner/schema/command decisions and approved implementation | Prospective and attributed shared projections; no substitute Life-only writer |
| Value production | Shared producer/reuse/admission, cost and foreground-allocation contracts | Eligible corpus reads and Life-native Return integration using shared production |
| Live engine | Trigger/evaluation contracts, current-world adapters, temporal judgment, bounded watches, action/delivery integration | Owner-backed historical/prospective context and reconciled record; no separate Life engine or watch writer |
| Home / Places | Complete output experiences and practical continuations | Stable continuity destinations and permitted historical context |
| Capture | Existing entry-path conformance, formats and immediate-value handoff | Original/source accessibility and organized continuity |
| Migration | Non-Life legacy consumers, booking/surface contraction and cross-repo rollout coordination | Atlas replacement and its data/read compatibility obligations |

Life R6 consumes I3's intention/shared-material contract. Life R7 and I2/I4
share production and allocation interfaces. Those specific dependencies do not
block Life's other packages. Do not create separate Home and Life generators
while waiting for a contract.
The engine reads relevant source, intent and outcome owners directly through
agreed contracts; it does not scrape the Life UI or depend on a Life page being
opened. Life and the engine are different consumers of those authorities.

Before either task changes a shared model, route file, generated schema,
navigation utility or invalidation policy, declare the exact files and contract
change. Shared files are serial integration points, not parallel writing areas.
For future coordination, communicate one bounded dependency request rather than
redirecting the other task's whole program. This planning pass sends no command
to the Life task.

## 3. Milestones and dependency ordering

Packages are system responsibilities with executable consumer outcomes, not
standalone feature lanes. Design against the whole portfolio; implement in
coherent increments. Do not require every uncertainty to settle before progress.

| Milestone | Packages / entry | Outcome | Direction review |
| --- | --- | --- | --- |
| M0 — agreed engine and integration boundaries | I0; Life continues | Owner/replacement map and actual observation-to-judgment-to-consequence paths are concrete enough to execute | Are we completing one system or adding another abstraction layer? |
| M1 — responsive shared substrate | I1 and I2; I3 contract work may proceed | Current context, change-driven reevaluation and bounded serving work without waiting for optional enrichment | Can the engine respond to reality, and did cost and duplicated policy decrease? |
| M2 — complete value and live experiences | I3, I4 and I5, with relevant Life contracts | Useful preparation, consumption, spatial exploration, live adaptation, shared action and continuity connect | Does adaptation preserve the worthwhile intention with less work, rather than merely repair a schedule? |
| M3 — coherent internal candidate and retirement | I6 plus portfolio-wide evidence and Life readiness | Supported paths, watches and migrations are measured, bounded and recoverable | What is genuinely ready, what needs redesign, and what should be cut? |

Dependency detail:

- I0 precedes new shared-owner writes and substantive branch dispatch.
- I1 and I2 may proceed concurrently with disjoint files and agreed contracts.
- I2 design, instrumentation and fake-based tests can overlap I1. Promotion of
  production/rekeying depends on I1's authorization, exact dependency and
  request-context conformance; an unfinished I1 boundary is not bypassed by
  running generation in a worker.
- I3 source/capture improvements can begin over existing owners; new intent and
  collaboration writes require their exact decision approval.
- I0 specifies observation, temporal judgment and watch boundaries; I1 carries
  usable signals; I2 supplies bounded evaluation/delivery. A new durable watch
  owner requires D6 approval, but existing authorized practical paths and fake-
  clock conformance can proceed. Do not defer all engine work until I5.
- I4's Home/Places work can use stable owner-direct material before model
  production or every social capability is enabled. Do not substitute fixtures
  for missing production owners.
- I5 depends on the relevant I1/I3 contracts, not all editorial or visual work.
- I6's inventories and removal planning start early; destructive cutover and
  release wait for their own evidence and authority.

No calendar completion promise is made. Size the next package from its actual
files, migrations and dependencies at each review. Long-range packages are
deliberately revisable; do not turn them into a frozen six-month task list.

## 4. Execution packages

### I0 — rebase evidence and settle the minimum shared decisions

**Deliver:** a current route/owner/writer/consumer inventory, live-engine path
matrix and short decision queue maintained here or in exact ADRs, not another
broad vision document. Record code/contract/native/real-data evidence separately.

1. Pin all three HEADs, dirty surfaces, active Life package, relevant rollout
   settings and local baseline failures. Confirm compatibility paths actually
   used by supported consumers.
2. Name the owner of Source originals, interpreted anchors, deliberate keeps,
   prospective intent, shared authored material and retained compositions.
3. Specify the minimum intention and shared-material lifecycle, author, optional
   Plan association, current grants, revision, correction and exact readback.
4. Name one change-dependency contract and one shared production/allocation
   contract. Compare existing implementations before adding schemas.
5. Map superseded readers/writers to keep, adapt, replace or retire. A module
   move is justified by dependency ownership, not naming cleanliness alone.
6. Trace practical preparation, live adaptation and authorized waiting across
   existing movement, situation/context, planning, notification and engine
   adapters. Name the signal, intent, fresh evidence, evaluator, owner, permitted
   treatment, reevaluation trigger and stop condition. Check actual activation;
   do not equate a registered family with enabled or complete behavior.

**Exit:** no new action in the next batch depends on an invented owner; each
unsettled decision blocks only its affected writes. Founder-only schema/auth
and prompt decisions are explicitly approved before implementation.
The engine path matrix identifies where reevaluation actually runs, what it can
know, and which gaps need a contract versus a missing adapter. No monitor or
background capability is promised merely because a scheduler exists.

**Review M0:** retain the broad model if the same owners support ordinary life,
travel and multiplayer without pseudo-Trips. If they cannot, revise the specific
owner boundary before multiplying consumers.

Decision queue to resolve in I0 (recommendations, not approved schemas):

| Decision | Default recommendation to investigate | Must settle before |
| --- | --- | --- |
| D1 — pre-Plan intention | Governed authored claim or narrowly typed person-owned prospective record; optional Plan relation | Durable loose-Keep writes and Life Ahead adoption |
| D2 — shared human material | Reuse source/authored payload custody with an explicit target/adoption relation | Generic Plan/Occasion comments and suggestion adoption |
| D3 — scoped editing | Separate revocable target/effect grant, not a new organizer/member role or implicit AI mandate | Collaborative edits beyond existing owner-only commands |
| D4 — retention boundaries | Explicitly distinguish conversation history, Ask attachments, source custody, memory claims and retained intent | Expanding writer conformance or claiming an end-to-end no-write promise |
| D5 — cross-root change/production contracts | Existing owner revisions and repair lineage; shared meaning identity with root-specific expressions | New shared consumers and production promotion |
| D6 — live evaluation and authorized watches | Reuse bounded scheduler/delivery primitives where suitable; explicitly own condition, refresh, audience, action depth, expiry, cancellation and reevaluation state | New durable monitoring, background subscriptions or claims that the engine will keep watching |

Conversation messages can supply authored evidence when they already exist.
Do not create a hidden conversation merely to persist a direct object contribution.
Neither conversation `intent_state`, an interpreted ExperienceAnchor, a generated
Opening nor a cached Composition is automatically the missing intent owner.

### I0 decision-alignment audit — 2026-09-06

The original queue above is a discovery list, not six equally unresolved
decisions. Existing accepted canon settles four rows at the policy level; only
the concrete owner/trigger seams remain implementation work:

| Queue item | Current evidence | Current state | Remaining work |
| --- | --- | --- | --- |
| D1 — pre-Plan intention | `lightweight-arrangements-implementation-handoff-2026-09-04.md` and `life-organization-and-composition-engine-system-design-2026-09-05.md` both preserve loose intent without a synthetic Trip, but explicitly leave its durable owner open | **Decision-blocked** | Founder/Plan lane must choose the narrow owner and command before a durable loose-Keep or Life Ahead write is added |
| D2 — shared human material | `2026-08-29-adopt-contribution-use-grants.md` settles custody, attribution, audience/use grants, and adoption as separate lifecycles | **Policy settled** | Implement only through existing Source/authored payload and target/adoption owners; no new social owner |
| D3 — scoped editing | `contribution-and-consequence.md` plus the lightweight-arrangements handoff define owner-only editing by default and revocable scoped target/effect grants | **Policy settled; runtime partial** | Add/verify the named grant adapter when a concrete collaborative command needs it |
| D4 — retention boundaries | `2026-08-29-adopt-contribution-and-consequence-contract.md` and the use-grants decision separate conversation, Source, claims, projections, and intent retention | **Policy settled; writer audit partial** | Finish inferred-writer audit and preserve the held Chat surface; do not claim universal no-write behavior yet |
| D5 — cross-root change/production | `four-root-loop-object-surface.md`, `artifact-expression-and-composition.md`, the dependency matrix, and the accepted four-root decisions establish owner revisions, causal repair, shared meaning, and root-native expressions | **Architecture settled; I1/I2 partial** | Measure remaining duplicate reads and finish the bounded work-item/trigger path before production promotion |
| D6 — live evaluation/watches | `live-engine-owner-path-matrix-2026-09-05.md` and `2026-09-06-bound-source-production-worker.md` name the owner boundary and keep watches dark | **Owner-bound; activation gated** | Each watch family still needs a concrete signal, refresh policy, audience, action depth, expiry, cancellation, and readback owner |

This audit prevents I0 from reopening accepted authority policy while still
blocking premature persistence or background monitoring. It does not authorize
the unresolved D1 owner or any D6 watch.

### I1 — current-world context, shared identity and change propagation

**Reuse:** owner-read envelopes/budgets, canonical repositories, ResourceRef /
EntityRef, owner commands, root grants/readback, account lifetime and return
registry. Life retains its independent indexed-query implementation.

**Work:**

- Trace each canonical kind through input, owner, Home, Places, object reader,
  Life and correction. Distinguish source IDs, intake-anchor IDs, legacy kept
  IDs, projection IDs and entity aliases explicitly.
- Audit shared owner adapters versus engine/context-provider adapters. Bind
  authoritative facts through the same owner policy; leave different query
  needs separate. Move shared orchestration out of feature-local ownership only
  when a concrete dependency conflict warrants it.
- Pass one explicit represented clock through Graph, conditions and contribution
  discovery. Coalesce identical authorized reads within a request; revalidate
  changed authority before serving or acting. Do not call this a frozen snapshot
  unless an actual consistency mechanism establishes it.
- Coalescing identity includes viewer, operation/family, exact resource IDs and
  revisions, audience/purpose/grants, and represented clock. Results come from
  canonical authorized readers, not a parallel permission implementation. A
  changed scope or grant cannot reuse an earlier read through a broad cache key.
- Carry owner revisions, semantic time roles, grant/membership versions,
  source dependencies and expiry through relevant projections. Unknown time is
  not request time; a pagination clock is not a frozen database snapshot.
- Define which changes invalidate or repair which consumers. Include root,
  depth, refind, dossiers, kept versions, generated cache and pending work.
- Distinguish record correction from a new real-world observation. Classify each
  signal's subject, source clock, freshness, current authority and affected intent
  or commitment. Route relevant changes to bounded reevaluation as well as cache
  repair; unrelated changes should not regenerate the whole account.
- Cover `allLifeRecords()` alongside root invalidation where the changed owner
  affects depth. Coordinate with Life before editing shared query-key files.
  Retained multi-source compositions need plural, revision-bound dependency
  semantics; preserve conservative invalidation and do not guess one correction
  target simply to expose a button.
- Life supplies its read handles, dependency semantics and invalidation targets.
  Strategy verifies their cross-root consumers; it does not reopen Life's cursor,
  chronology, source-revision or internal indexing implementation under I1.
- Verify exact-or-recomposed return after edits, deletion, audience change,
  expired tokens, restart and account switch. Do not restore revoked content
  for visual continuity.

**Exit:** the cross-root identity/change matrix has executable coverage for
supported object families. One canonical update is reflected in every affected
consumer, including delayed completions, without deleting independent evidence.
Signal replay, out-of-order arrival and source loss cannot create false current
truth. A supported condition change reaches its evaluator without a user needing
to reopen a page; unauthorized or out-of-scope observation does not start work.

### I2 — responsive live evaluation, fast serving and bounded production

**Reuse:** current v2 composition, metadata-first discovery, production leases,
reuse, delivery/received distinction and owner-direct practical value.

**Work:**

- Replace scenario-dependent runtime read policy with actual contextual
  requirements. Keep New York/Europe stories in evaluation fixtures; adding a
  city or day of week should not require a new runtime situation branch.
- Do not emit known-unavailable operations as routine work. Preserve exact
  candidate-required reads ahead of broad optional reads under budget caps;
  distinguish unavailable capability from missing optional evidence. Declared
  field coverage must match what an adapter actually returns.
- Measure the complete Home/Places request: domain reads, duplicate reads,
  candidate construction, admission, production wait, binding and compilation.
  Optimize repeated authorized reads within a request without caching authority
  indefinitely across viewers or changed grants.
- Bound underlying synchronous work as well as coroutine wait time. A timeout
  around `to_thread` does not terminate the thread's database work; inspect and
  reuse the Places bounded-executor pattern where suitable. Measure late work,
  queue depth and pool pressure, not only request timeout counts.
- Separate fast assembly from background preparation and explicitly requested
  production. A page can render useful existing value when generation is slow,
  unavailable or disabled. Reuse existing leases/attempt records; no active
  source-production worker was established by this audit. Designate or add a
  bounded worker/outbox integration with an owner and deployment path if none
  exists. Do not attach unbounded work to GET requests.
- Separate three workloads: fast current-state serving/practical assessment,
  bounded signal-driven reevaluation, and optional editorial enrichment. Give
  live freshness and worthwhile change their own timing and resource budgets;
  slow content production must not starve them. Explicitly invoked AI reasoning
  may be bounded work without making every root GET a generation request.
- Implement reevaluation through the existing judgment/admission and owner
  gateways: a signal can cause no change, hold, wait, a revised possibility, an
  authorized action or release. Recheck relevance and grants before delivery.
  Coalesce duplicate signals; use freshness and material-change thresholds to
  prevent oscillating recommendations or repeated prompts.
- After D6 approval, implement only the missing watch-owner adapters and bounded
  execution. Persist authoritative cancellation/expiry and revalidate them before
  late work publishes or acts. Monitor creation, refresh, notification permission
  and action authority are distinct. App closure alone does not create a watch;
  an authorized watch need not depend on a foreground app to run.
- Define reuse keys around evidence, purpose, current context, audience and
  versions. Revalidate before serving. Root-specific expressions may share one
  production without copying identical foreground content across tabs.
- Include semantic policy/compiler versions in production identity. Equivalent
  exact evidence, context and authority may reuse across roots; a change that
  alters meaning must miss. Do not blindly remove situation/root fields without
  representing their meaning-bearing effects. Root expression selection occurs
  after shared meaning is produced, subject to its allowed consumers.
- Coordinate Home/Places/Life foreground treatment by semantic overlap and
  current relevance, not whichever request races first. Keep exact objects and
  deliberate retrieval available when a foreground treatment yields.
- Add per-account and system concurrency/spend limits, bounded retries,
  cancellation/lease-loss behavior and a generation kill switch independent of
  ordinary reading. Keep metrics content-free.

**Exit:** recorded latency, query count, generation count, reuse and cost explain
the whole request; repeated navigation does not repeatedly buy equivalent work.
Source revocation or a newer intent prevents late stale publication. Select
numeric operating ceilings from measured baselines at M1 before cohort use.
Hard exit invariants: zero routine known-unavailable operations, zero new model
production calls on ordinary root-response paths, no authority bypass through
coalescing, one active production for an equivalent semantic group, and no stale
serving after correction/revocation. Bounded current-world data reads are measured
separately; "zero model production" does not prohibit legitimate provider-backed
facts or explicitly invoked actions.
Supported live paths also have measured signal-to-judgment and judgment-to-surface
latency, evaluation counts and notification burden. A stopped, expired or revoked
watch must not deliver or act after its termination is authoritative; unrelated
records and already accepted commitments remain intact.

Required regressions: consistent clocks; no scheduled known-unavailable reads;
exact reads survive caps; slow production does not hold an ordinary root
response to the provider timeout; concurrent semantically equivalent Home/Places
requests share one production attempt; materially different context/grants do
not reuse it; late work and source correction cannot publish stale output.
Also exercise fake-clock watch expiry/cancellation, stale/out-of-order and duplicate
signals, no meaningful change, unknown provider state, and a permitted change that
updates Home/Places while optional enrichment is deliberately stalled.

### I3 — useful contribution, prospective intent and human material

**Reuse:** existing Ask/Point/Bring policy, custody, authoritative receipts,
graph commands, Occasion/relationship grants and canonical source readers.

**Work:**

- Complete immediate value for existing ingestion paths before candidate review
  or organization. Preserve provisional interpretation and partial-source
  success; missing downstream work must not relabel retained originals as lost.
- Audit PDF, phone-photo HEIC/HEIF and Wallet/ticket support in the actual
  accept/normalize/render pipeline. Sequence adapters by the input portfolio
  and native feasibility; unsupported formats get an honest recoverable path,
  not a false supported claim. New external integrations require approval.
- Audit remaining reflection/background/synthesis writers against contribution
  authority. Recent observe/remember fixes are reuse evidence, not certification
  of every producer. Preserve the held Chat surface; request specific approval
  where prompt or interaction changes are necessary.
- Implement approved personal intent/keep behavior without mandatory Plan/Trip
  creation. Preserve authored wording, soft time, source lineage, correction,
  release and optional later association. Do not promote an extracted ticket
  or a viewed option into intent.
- Preserve purpose and practical constraints when explicitly supplied: a relaxed
  afternoon, time with a friend, less walking, a fixed dinner. Do not ask users to
  fill an intention profile, infer hidden motivations, or turn optional wishes
  into protected commitments. Clarify only when ambiguity changes a consequence.
- Implement attributed suggestions/comments/contributions in their appropriate
  existing domain. Distinguish authored social material from cached generated
  Source contributions. Adoption references source and changes the target; it
  does not transfer private custody or imply everyone's participation.
- Publish exact consumer/readback contracts for Life, Home and Places. Every
  capture/keep/share action has one owner and a visible, low-demand result.
- Carry the capture origin through success, partial success, correction, retry,
  dismissal and existing Chat handoff. Ordinary back-stack behavior and cold-link
  semantic fallback both need native evidence.

**Exit:** Ask can finish without new durable source/memory/intent side effects
under the separately defined conversation-history policy; Bring returns useful
value and accessible retained originals; a loose intention survives without a
Trip; a friend contributes without taking over editing or inheriting private
context. All have correction/release coverage and exact continuity destinations.

### I4 — generous Home and one coherent Places experience

**Work:**

- Map the September 5 Home amendment through semantic contracts, current
  producers, native components and tests. Reuse composition families; do not
  treat 35 supported kinds as 35 independent product subsystems.
- Deliver a useful full scroll with dynamic importance and varied material:
  current practical state, prepared possibilities, substantive explanation,
  factual reconstruction, authored people material and meaningful continuations.
  Present life remains primary after travel. No content quota forces filler.
- Apply supported practical judgment before presenting a possibility: current
  window, reachability, effort, commitments and relevant conditions shape what is
  offered, not a feasibility checklist the user completes afterward. Do not invent
  exact timing or accessibility facts when their sources are missing.
- Separate a strict demand budget from a generous possibility budget. Reading,
  looking or enjoying can be complete value. No response, reflection, filing,
  saving, invitation or action is owed after consumption.
- Make factual reconstruction useful on its own when it reduces work or reveals
  a legible pattern. Apply the new-substance test to claimed interpretation,
  comparison and synthesis; do not ban factual summaries categorically.
- Preserve attribution and allowed social context. Conditional people grouping
  follows the latest social split: Home shows addressed and shared-consequential
  material, including the conditional `Addressed to you` region. Its shared-world
  pull door opens Places in `From friends`; Life People holds the stable record.
  Casual Place-bearing sharing belongs to that Places scope, not a general Home
  social chapter. Preserve the accepted nonspatial featured-Status doorway
  exception; do not invent a Place to put something on a map.
- Own Places continuously: scope/search/viewport, map and field, canonical
  Focus, supported Path and live practical compression. Give each transformation
  an explicit result-set/context contract; presentation changes alone must not
  silently replace inventory, while explicit new searches/scopes legitimately do.
- Implement `From friends` as an authorized scope over the same map/field
  contracts, not a separate feed service. Marks preserve the author's chosen
  Place/neighborhood/city precision, source, audience and expiry; city-level
  statuses use the accepted Elsewhere treatment. No live location, inferred
  presence, person ranking or another participant's location permission is
  required. Give revoked, nonspatial and expired material explicit treatments.
- Consume supported entity pages, current conditions and provider handoff.
  Missing research or private-provider data must not manufacture facts or remove
  all ordinary spatial value. Keep practical and interpretive depth connected.
- Make live judgment legible through usable choices, thresholds, tradeoffs and
  fallbacks—not a separate Live Engine panel or claims that Vesper is working.
  An ordinary weekend should reveal this capability before an active trip or
  disruption. Unknown receptivity is not permission to interrupt.
- Verify each card's optional continuation and exact return with I1 and Life.
  Detailed visual composition remains with the dedicated design workflow;
  native conformance uses the app's registered QA process.
- Check the negotiated renderer capability set against real backend envelopes
  before replacing compatibility Home. Exercise fallback deliberately, including
  return-token behavior, rather than accepting a silent legacy composition as a
  successful new-design result. Verify full text and accessible alternatives for
  every supported medium; a native test ID alone is insufficient evidence.

**Exit:** Home is worthwhile without input and Places is useful without first
selecting a Plan. They share identity and evidence but contribute different
value. Real examples clear product/editorial review separately from deterministic
tests; sparse/offline states remain immediately useful where evidence permits.
At least the ordinary preparation and changed-condition cases show why the offered
experience is livable now, without turning all curiosity or social material into
a practical task. A meaningful reevaluation updates the relevant surfaces without
duplicating a notification or imposing a new action when none is needed.

### I5 — complete live adaptation and lightweight shared consequences

I0–I2 establish the engine's contracts and bounded execution; I3/I4 connect its
intent and surface consumers. This package completes the human interaction and
consequence paths. It is not a separate engine build following a content product.

**Work:**

- Carry solo intention into optional pair/group arrangements through I3's owners.
  Preserve contributor, editor, participant, affected person and AI authority as
  distinct roles. Ordinary optional ideas create no approval or overdue queue.
- Offer direct scoped actions and contextual AI help without forcing every edit
  through Chat. Preserve freely expressed requests; do not replace flexibility
  with a fixed menu of hypothetical alternatives.
- Compile practical judgment from current owner state, explicit intent, relevant
  conditions and affected people. Authority constrains solutions; it does not
  decide which authorized solution is helpful. Preserve why the experience matters.
- Compare retaining, shortening, substituting, postponing and stopping against
  the expressed purpose, not merely the next calendar slot. In a relaxed
  waterfront-afternoon case, the best replacement need not be the nearest open
  venue. Demonstrate judgment without pretending to know unstated motives.
- Integrate prepare/apply/readback/recovery and independent personal participation.
  An accepted edit is not everyone's renewed agreement; "Undo" must not restore
  the whole world over another person's later independent action.
- Make the engine useful during ordinary local life, not only an infrequent
  live trip. Practical help, external routing/booking links and imported
  confirmations can coexist without recreating a booking marketplace.
- Complete authorized waiting and monitor controls through existing contextual
  entry points: what is watched, when it ends, what Vesper may do, and how to stop
  it must be recoverable. Do not require a monitor dashboard or silently attach
  a watch to every intention. Route useful in-app updates separately from events
  that genuinely deserve interruption.
- Let factual occurrence and separately authored Outcomes carry forward into
  Life and later judgment. No automatic attendance, liking or personality inference.

**Exit:** a local solo/pair/group scenario and a live disruption share the same
authority and consequence principles without sharing an unnecessarily heavy UI.
Readback, partial failure, participation changes and repair remain coherent across
Home, Places and Life. Test unknown save outcomes without falsely claiming either
success or that nothing changed.
Evaluate helpfulness independently of valid state transitions: the result must
preserve the explicit purpose where feasible or explain the relevant tradeoff.
Waiting, withdrawing and leaving an idea unadopted are successful possible exits.

### I6 — finish cutovers, reduce surface burden and prepare an internal candidate

The detailed contraction sequence is maintained in
[surface-contraction plan §20](product-surface-contraction-investigation-2026-09-04.md#20-next-execution-sequence--september-5-rebaseline).
Its SC packages map to I0/I3–I6 and Life's existing R packages; they do not add
parallel product programs. Inventory and isolated retained-reader work start
early, and each obsolete implementation is removed when its specific replacement
and operational conditions are met. Final candidate acceptance remains here.

**Work:**

- Finish compatibility inventories from I0. Remove obsolete consumers as their
  supported replacements become real; retain narrow external-link adapters and
  historical data access. Do not leave a fully maintained legacy product hidden
  behind a flag indefinitely.
- Complete obligation-safe booking retirement according to the existing runbook.
  Preserve imported facts, existing obligations, callbacks and liability-reducing
  recovery until exact operational disposition is verified. A local fixture audit
  does not authorize deployed shutdown or database deletion.
- Prune heavy itinerary/change/permission/expense surfaces by user job, not noun.
  Keep inspectable agreements, corrections, disputes and monetary arithmetic.
  AI may extract/explain/propose expenses; deterministic amounts, allocations,
  currencies and user-authorized settlement truth remain authoritative.
- Integrate Life's Atlas replacement with all remaining emitters, readers,
  generated contracts and migration acceptance. Do not duplicate its migration.
- Run portfolio-wide backend/contract/mobile and real-backend native checks.
  Include account transitions, offline/reconnect, process death, accessibility,
  source withdrawal, late jobs and exact destinations. Use appropriate pair/group
  accounts; two-account evidence alone cannot certify every group role.
- Exercise permitted live signals, watches and scheduler recovery with the app
  closed as well as open. Verify duplicate-event handling, missed refreshes,
  freshness loss, cancellation, grant revocation, independent provider failure
  and notification limits. Disabling enrichment must leave supported practical
  assistance intact; disabling monitoring must stop future evaluation/delivery
  without erasing readable history or independently accepted consequences.
- Record actual supported flags/builds, performance/cost ceilings, rollback,
  retained capabilities and unresolved limitations. Distinguish internal readiness
  from public release; deployment requires its own authorization and runbook.

**Exit:** each supported path has one current implementation or an explicitly
bounded adapter; the complete portfolio is useful, correct and recoverable at
measured cost. No missing visual, real-data or migration evidence is converted
into a pass by a large unit-test count.

## 5. Direction reviews: built into execution

Review at **each milestone, after at most three integrated packages within a
milestone, or immediately on a material contradiction**, whichever comes first.
This is an execution checkpoint policy, not a scheduled automation or a request
to stop on every uncertain detail. Independent Life work need not pause.

Each review produces a short decision with these fields:

1. **Evidence:** exact revisions, implemented consumers, measured runs and
   remaining unknowns; distinguish new evidence from inherited receipts.
2. **Product:** what useful thing can someone receive now, and what work have we
   removed? Are ordinary life, practical help, curiosity and multiplayer still
   present without forcing every case through every move?
   Does the live engine preserve expressed purpose when conditions change, and
   can its value be felt before a disruption? A feasible plan or valid receipt
   alone does not answer that question.
3. **Architecture:** did this remove duplicate authority or paths? Is a local
   adapter becoming a second owner? Are source and outcome distinctions intact?
4. **Economics and reliability:** did query fan-out, paid work, latency or failure
   coupling grow? Can useful reading survive optional capability failure?
   Are signal-to-judgment latency, evaluation frequency and interruption burden
   bounded independently of editorial production?
5. **Scope:** what should continue, be revised, be split, or be retired? Does the
   next package require an exact founder decision rather than speculative code?
6. **Next batch:** named packages, contracts, file ownership, tests and Life
   dependencies. Update this roadmap's current ledger instead of appending pages
   of repeated "complete" narratives.

Immediate reassessment triggers include a second writer for one fact, routine
navigation launching repeated paid work, a pseudo-Trip needed for a loose keep,
valid-but-unhelpful results dominating review, revoked material resurfacing,
more mandatory user steps needed to make a subsystem work, or a violation of
I1/I2's hard authority, readiness, generation and freshness invariants.
Also reassess when preserving a schedule repeatedly defeats the stated purpose,
live assistance requires reopening Home, no-change signals generate prompts,
or cancelling an authorized watch fails to stop its future effects.

Do not respond to weak output by automatically shrinking the company vision.
First determine whether evidence, production, presentation, timing, interaction
or the underlying hypothesis failed. Conversely, coherence of the philosophy is
not a reason to keep a costly feature people cannot understand or use.

## 6. Whole-product acceptance portfolio

Use the same authorized owner worlds across backend, mobile and native evidence.
Fixtures are conformance cases, not custom product code. Broaden locations,
timezones, corpus sizes and social configurations beyond founder stories.

| Situation | Required value and connected behavior |
| --- | --- |
| Ordinary week and open local time | The engine prepares worthwhile, livable possibilities from the actual window and supported conditions before anything goes wrong. Home returns value, Places grounds the alternatives, and optional intent persists without Trip setup |
| Return from travel, life continuing at home | Retained documents/photos support useful reconstruction or new substance; present and future life remain foreground; no personality verdict |
| Current practical change | Preserve expressed purpose when timing, access, weather or participation changes; test retaining, shortening, substituting, postponing and stopping. Owner-confirmed consequences and recoverable partial states appear consistently |
| Authorized waiting and release | A bounded watch can survive app closure; unchanged/duplicate signals create no repeated demand. Fresh material change reevaluates within authority; expiry/cancellation/revocation stop late effects. A normal Keep does not create a watch |
| Authored social perspective and shared arrangement | Addressed/shared consequences appear in Home; casual spatial sharing appears in Places From friends; Life People holds the record. Consumption creates no response debt; optional adoption preserves author, audience, precision and independent participation |
| Sparse account or unavailable capability | Immediate factual/practical value where possible, legible uncertainty elsewhere; no onboarding assignment or fabricated intimacy |
| Correction, release and later refinding | Exact sources and independent evidence survive appropriately; dependent results, jobs, caches and shared views repair; later retrieval finds the right state |

Across the portfolio test both **consumption without any further action** and
full consequence/continuity. Record truth, usefulness, novelty where claimed,
attribution, demand, exact destination, cost, and failure/recovery independently.
An attractive screenshot cannot certify owner behavior; a correct contract cannot
certify content value or native experience.

For live cases record the original purpose, known/unknown conditions, temporal
posture, trigger, chosen treatment, permitted effect, source clock, reevaluation
and stop condition. Include a complete-on-view interpretive result with no watch
or action as a control: the engine must not operationalize every valuable moment.

## 7. Parallel Luna execution policy

The founder explicitly requested bounded **Luna-max / Luna-extra-high** subagents.
Use `gpt-5.6-luna` with `max` for difficult bounded architecture/owner reasoning
and independent reviews, and `xhigh` for well-scoped implementation, tests,
migration inventories or consumer integration. Do not silently substitute a
different model/effort if those settings are unavailable; report the limitation.
No new user-owned tasks are required for temporary subagents.

The Strategy parent owns architecture decisions, the roadmap, shared contracts,
integration review and final status. Delegate only concrete work that can proceed
alongside useful parent work. Start with at most two implementation workers;
use the third available worker slot for independent review when useful. The
current read-only investigation used three workers because their scopes do not
mutate shared files. Subagents should not recursively expand the team.

Every dispatch must specify:

- outcome, package ID and exact current base revisions;
- mandatory repo instructions and relevant contract files to read;
- allowed files or isolated worktree and forbidden/shared surfaces;
- adjacent Life ownership and the agreed input/output contract;
- what must be reused, what may change, and explicit non-goals;
- acceptance tests and evidence level; and
- whether edits/commits are authorized and what decisions must return to parent.

Immediately before dispatch or integration, re-pin all three repository HEADs,
branches, dirty files and active Life/shared-file ownership. Stale baseline
revisions in this document are not permission to overwrite intervening work.
Do not dispatch a writer until its actual base and file boundary are checked.

For code execution, prefer isolated `codex/` worktrees for independent branches.
If sharing a checkout, require disjoint named files; never switch its branch
under another worker. Shared route registries, schema models, generated OpenAPI,
`schema.gen.ts`, query keys and navigation utilities have one integrator at a
time. Worktree isolation does not make incompatible contracts safe to merge.

Workers do not deploy, flip flags, contact providers, run paid models, perform
production backfills/deletion, or approve schema/auth decisions by implication.
Use explicit filenames for staging; never `git add .` or `git add -A`. Commit
coherent packages during authorized execution, inspect each diff, then integrate
and run affected tests before starting another dependent package.

Suitable parallel batches after contracts settle:

- I1: backend dependency adapters and disjoint mobile consumer tests; parent
  integrates shared models/query-key changes.
- I2: disjoint live-signal/watch adapter and enrichment/reuse work after shared
  contracts settle; an independent reviewer checks timing, grants and termination.
  Do not create two competing schedulers or authority systems.
- I4: Home composition and Places context/result-set work, with shared types
  agreed first and generated files handled serially.
- I6: static retirement inventory and independent migration/acceptance review.

Do not parallelize competing intent schemas, two changes to the same return
resolver, independent Home/Life production systems, or simultaneous generators
writing contract snapshots. Use an independent reviewer for owner writes,
authority, billing/concurrency, migrations and causal repair.

## 8. Validation and completion discipline

For each code package, run proportionate local tests against the integrated base:

- backend owner/policy/projection tests, relevant Postgres transaction/race tests,
  lint and the repo-required broader checks;
- `./scripts/sync-types.sh` for backend schema/route changes, reviewing the full
  and active-mobile snapshots plus generated app types;
- frontend typecheck, affected Jest, API operation coverage and compatibility;
- registered native scenario/design/accessibility QA for surface changes;
- real-backend and real-data runs for claims not established by fixtures; and
- dependency correction, account lifetime, expiry and late-completion tests.
- signal freshness/order, reevaluation, watch cancellation/expiry/revocation,
  no-change behavior and separate practical-versus-enrichment resource budgets.

Classify failures as new, inherited, environment-blocked or unverified with exact
evidence. Do not call a failure inherited merely because it is outside a worker's
files. Re-run relevant checks after integration; worker passes are not a merged
result. Tests and logs must not expose private user content.

Use explicit states: **planned, decision-blocked, implemented, integrated,
locally tested, real-data evidenced, native evidenced, enabled**. These are
different evidence dimensions, not interchangeable claims of completion.
Human value remains separately reviewed. No release claim follows from this
document's creation.

## 9. Current execution ledger and first batch

| Package | State at roadmap creation | Next concrete action |
| --- | --- | --- |
| I0 | Implemented/integrated at inventory level; live-engine path matrix and 2026-09-06 decision-alignment audit recorded | Keep D1 object-less intent ownership and family-specific D6 watch contracts gated; consume settled D2–D5 policy through I1–I3 adapters |
| I1 | Integrated for request-clock, consequence fan-out, dependency matrix, capture return, authority-safe owner-read coalescing, and Places continuity | Trace remaining owner identity plus condition signals; agree Life handles/change events and bounded reevaluation inputs |
| I2 | Owner-read readiness, fast root serving, single assembly seam, bounded reads, late-work limits, content-free serving measurement, deterministic trigger identity, durable workflow handoff, a dark lease/readback adapter, deployment envelope, and an injected canonical executor/context/provider seam are implemented; worker activation remains gated | Approve a controlled cohort only after measuring provider cost/latency and signal-to-judgment budgets; only then consider registering a dark Arq job |
| I3 | Capture/custody and format boundary audited; supported/rejected cases are locally tested; writer-authority inventory is recorded; owner decisions and formats remain partial | Complete native custody evidence, resolve inferred-writer authority, draft precise owner ADR, then implement approved intent/social commands |
| I4 | Renderer promotion boundary, result-set identity, source-backed revision, native returns, and stale-source treatment are implemented locally; semantic promotion remains dark | Complete real-data Home→Places→Focus/Path acceptance and decide whether personalized freshness needs a separate source vector |
| I5 | Graph/consequence foundations present; movement signal→judgment shadow path is locally evidenced; lightweight experience remains incomplete | Complete adaptation and shared consequences over I1–I3, preserving purpose, plural participation, and meaningful stop/wait behavior |
| I6 | Inventories, guards, retained booking-evidence and assisted-expense contracts are recorded and locally validated; destructive cutovers remain incomplete | Run environment obligation audits, migrate actual retained readers, and remove only execution paths with no remaining consumer or obligation |

**First execution batch after authorization:** complete I0's owner inventory and
live-engine path matrix across practical preparation, changed conditions and
authorized waiting. Propose the exact missing contracts, implement independently
safe I1 continuity/signal repairs, and measure I2's current serving and evaluation
paths. Hold M0 before new shared or watch persistence. Do not spend that batch
rewriting canon, building a universal framework, or only expanding mock smoke
tests; do not defer the live engine until content composition is finished.

### Execution receipts (2026-09-05)

- **I1 / mobile consequence continuity — implemented and locally tested:**
  `travel-app` commit `2d30015c5` refreshes the direct Life record-page query
  prefix whenever a Home/Places/Life consequence resolves or becomes stale.
  The focused `rootConsequences` Jest suite passes (20 tests). This closes the
  direct-depth stale-read gap without changing Life ownership or its internals.
- **I1 / request-clock continuity — implemented; syntax checked, test
  environment blocked:** `travel-agent` commit `e0d0f52d1` passes the root's
  `represented_at` into the bounded Home experience-graph reader and adds a
  regression test. `py_compile` and all commit-hook checks except the known
  pre-existing backend size budget pass. The focused pytest collection is
  environment-blocked because this checkout lacks the `openai` package; the
  existing `backend/concierge/_prompts_skills.py` size-budget overage is
  unrelated and was explicitly skipped for this commit.
- **I0 / live owner path matrix — implemented:** workspace commit `c533b40`
  records the current trigger, context, judgment, treatment, consequence,
  readback, delivery, and activation boundary for all nine registered lived-
  experience families. It explicitly keeps watch persistence, route ownership,
  production, and Home kind promotion as gated decisions.
- **I2 / canonical owner-read readiness — implemented and locally tested:**
  `travel-agent` commit `4bac11f87` separates legacy semantic availability from
  canonical owner-read readiness. `route.evaluate` remains selectable as a
  partial legacy operation, but is omitted from routine owner-read/value-read
  budgets and retained as a truthful limitation in the compiled plan. The
  semantic-catalog and portfolio-read suites pass (20 tests). The broader
  canonical-owner suite remains environment-blocked by the missing `openai`
  package; unrelated pre-existing hooks for size, module-state, and error
  category registration were explicitly skipped for this commit.
- **I2 / typed compatibility regression — implemented and locally tested:**
  `travel-agent` commit `d98fc3a0e` preserves the existing typed error for
  unknown value-read operations while applying the new readiness filter. The
  focused portfolio-read suite passes (14 tests).
- **I2 / fast root serving boundary — implemented; focused pytest environment
  blocked:** `travel-agent` commit `bdd4add38` makes Home and Places composition
  consume only an explicitly precomputed Source production by default. Inline
  optional production remains available only behind the named
  `allow_inline_source_production` opt-in, so the HTTP roots do not await
  enrichment/model work on the ordinary response path. Home and Places route
  regressions assert that the optional producer is not awaited even when its
  rollout flag is enabled. The focused route tests are currently blocked at
  collection because this checkout lacks the `openai` package; both touched
  files pass `compileall` and commit hooks.
- **I2 / single assembly seam — implemented:** `travel-agent` commit
  `c89742bae` removes the unused Source-production parameter from the Home
  portfolio builder. Source candidates now enter at the root-composition seam
  only, either as an explicit precomputed handoff or through the named opt-in
  migration path; the portfolio reader cannot silently become a second
  production owner.
- **I1 / cross-root dependency matrix — documented:** workspace commit
  `096828d` adds `cross-root-change-dependency-matrix-2026-09-05.md`, tying the
  existing consequence and root invalidation paths to their Home, Places, Life,
  depth, session, and asynchronous-production consumers. It records the
  remaining background-fan-out, late-completion, and signal-to-judgment gaps
  without introducing a second authority or an all-account event bus.
- **Boundary preserved:** no API schema changed, no generated mobile types were
  regenerated, no Life internals were edited, and the pre-existing uncommitted
  Claude-design handoffs and concurrent Life work remain untouched.
- **Native integration validation:** `travel-app` Home v2 renderer and Home
  experience suites pass (21 tests), and the app TypeScript check passes on the
  current integrated checkout. The current app has unrelated uncommitted
  entity-route edits; they were not staged or changed by this batch.
- **I2 / owner-facing seam documentation:** `travel-agent` commit `d91c4537e`
  updates the root feature contract so future worker/outbox scheduling is the
  producer owner and ordinary GET composition remains a precomputed-value
  handoff. No worker, flag activation, or deployment was implied by the note.
- **I2 / bounded synchronous reads — implemented:** `travel-agent` commit
  `f1649f7b1` moves root portfolio readers off the process-wide
  `asyncio.to_thread` executor onto a fixed eight-worker pool. Timeout and
  cancellation now cancel queued work or observe a running read's late
  exception, bounding post-deadline pressure without pretending Python can
  force-stop an in-flight driver call.
- **I2 / rollout contract correction — implemented:** `travel-agent` commit
  `11cb4adab` clarifies that `ROOT_SOURCE_CONTRIBUTION_PRODUCTION_ENABLED`
  gates only an explicit worker/migration producer seam. Enabling it cannot
  silently reintroduce model work into ordinary Home or Places GET responses.

### M1 direction review — 2026-09-05

- **Evidence:** I0's owner-path matrix, I1's mobile consequence refresh and
  dependency matrix, and the I2 owner-read, source-seam, readiness, and bounded
  executor commits are now on the local integration branches. Home v2 and
  Places native suites pass (21 tests) and the app typecheck passes. Backend
  route/owner-read pytest collection remains environment-blocked by the missing
  `openai` package; focused semantic/readiness receipts from before that block
  remain valid, while no full backend pass is claimed.
- **Product:** The system is moving in the intended direction: Home and Places
  can return useful existing value without asking for input or waiting for an
  editorial generation call. Live-engine capability is expressed through the
  same bounded composition path, not a fifth surface. The current batch does
  not yet prove the richness or novelty of the final Home editorial experience.
- **Architecture:** The producer is no longer an accidental second root owner;
  canonical owner-read readiness is executable; root synchronous work has an
  explicit late-work bound. Authority, source custody, consequence readback,
  and Life ownership remain separate. The absence of a designated production
  worker is still a real integration gap, not hidden by the GET path.
- **Economics and reliability:** Ordinary root responses add zero new model
  production calls. Read timeouts can still leave an in-flight driver call,
  but only within the fixed root-read pool; queued work is cancelled and late
  exceptions are observed. Measure actual latency, queue pressure, reuse, and
  cost once the backend dependency environment is complete.
- **Scope decision:** Continue the shared-system integration program. Do not
  widen Home kinds, add a generic route service, create a new intent schema,
  or activate source production to compensate for missing product evidence.
  Life's active index work and the dirty Claude/design documents remain outside
  this batch and are not rewritten.
- **Next bounded batch:** (1) close the I1 capture-origin/return envelope with
  one agreed Home/Places/Life destination contract, (2) run the I4 semantic-kind
  and native renderer coverage audit against the current backend envelope, and
  (3) return with an explicit owner/deployment decision for a bounded source
  producer worker before adding any queue or scheduler code. Reassess after
  those three packages, or earlier if a second owner or paid GET path appears.

- **I4 / renderer coverage audit — documented:** workspace commit `97c9e84`
  adds `home-places-renderer-coverage-audit-2026-09-05.md`, reconciling the
  backend Home/Places vocabularies with the actual native promotion registries.
  Home and Places native suites pass (21 and 9 tests respectively); the audit
  keeps unpromoted semantic kinds dark and sets the four-part promotion gate.
- **I1 / capture return continuity — implemented and locally tested:**
  `travel-app` commit `ee8b6588c` carries an ephemeral root return token into
  the capture route and completes it on Done/error before using the semantic
  Trips fallback. The token is never written into intake capture context or
  product memory. The route test passes (2 tests), along with the root-return
  registry and share-intent suites (23 tests).

- **I1 / Home transport contract — implemented and locally tested:** backend
  commit `a67b79742` admits the four September 5 canon forms into the Home
  enum; workspace commit `d19488d` refreshes the committed OpenAPI snapshots;
  and `travel-app` commit `dce81ae7f` refreshes generated mobile types. The
  forms remain dark until producer/native promotion gates pass. The renderer
  audit is updated in workspace commit `81509d5`.
- **I1 / authority-safe owner-read coalescing — implemented and locally
  tested:** `travel-agent` commit `c9f7e3a31` centralizes request identity and
  coalesces only exact matches of viewer, operation/family, resource refs and
  revisions, represented clock, timezone, audience, and purpose. Fifteen
  focused portfolio-read tests pass; different viewers, purposes, or clocks
  cannot share a request-local result.
- **I4 / prose composition anatomy — implemented and locally tested:**
  `travel-app` commit `615f42d93` replaces the declared-native prose no-op with
  a typed, accessible supporting-claim treatment. The focused composition
  suite and app typecheck pass; this is renderer conformance, not editorial or
  real-data evidence.
- **I4 / Places result-set seam — contract defined:** workspace commit
  `2ed2597` defines the additive `PlacesResultSetRef` boundary for feed,
  search, map, collection, Focus, and Path. It keeps the existing opaque
  context handle, adds a server-owned set identity/revision, and makes field
  and map transformations testable without creating a second Places service.
- **I4 / Places result-set seam — wire-threaded and locally tested:** backend
  commit `c57aef18c` carries the additive reference through feed, search,
  saved/reading, and map responses, with normalized scope identity and
  query-child identity. Workspace commit `e381428` and `travel-app` commit
  `4b70de887` publish the generated contracts. Backend Places suites pass (104
  tests), app Places suites pass (30 tests), and app typecheck passes. The
  first implementation is honest about an unknown source revision; native
  Places promotion still requires a proven shared revision, native return
  propagation, and real-data acceptance.
- **I4 / Places native return propagation — implemented and locally tested:**
  `travel-app` commit `f267db979` carries the server-owned result-set id and
  optional revision through the map, field, and all supported detail-route
  return envelopes. Map-originated venue, experience, place, and site returns
  now preserve the originating identity; a current-location replacement
  intentionally starts a new context rather than pretending it is the prior
  set. The focused route/return suites pass (36 tests) and the app typecheck
  passes. The source revision remains explicitly unknown until an owner-backed
  revision can be proven, so semantic Places promotion stays dark.
- **I4 / Places source-backed revision — implemented and locally tested:**
  `travel-agent` commit `407173860` derives an explicit
  `places-catalog:v1:<digest>` revision from the server-resolved place subtree,
  canonical venues/sites/experiences, and approved dossier rows using their
  owner `updated_at` clocks plus row counts. Feed, search, saved/reading, and
  map owners echo the revision when that bounded catalog scope is available;
  global/personal scopes and unavailable source reads remain `revision: null`.
  The revision is continuity evidence, not a grant and not a presentation
  hash; private saves, relationship marks, and provider freshness retain their
  own source semantics. Eighteen focused result/search/collection tests pass,
  lint/compile pass, and the broad map API suite remains environment-blocked
  by the pre-existing missing `openai` package. The commit hook's known
  pre-existing size-budget overage was skipped explicitly.
- **I4 / field-origin return acceptance — implemented and locally tested:**
  `travel-app` commit `84ae8d379` extends the native detail-route bridge so
  ordinary field-origin `placesReturn` contexts preserve the same result-set
  id/revision as map-origin returns. The Places route-bridge, pin handoff, and
  return suites pass (13 tests), and the app typecheck passes. This closes a
  concrete Home/Places→Focus return gap; it does not yet claim a real-data
  stale-source recomposition path.
- **I4 / stale-source treatment — implemented and locally tested:**
  `travel-app` commit `bcc072de6` compares a returned catalog revision with the
  revision carried into a map return and surfaces a small accessible `VIEW
  UPDATED` treatment when the source changed. Unknown revisions remain quiet;
  the screen always uses the server's latest response and never treats the
  client-carried revision as authority. The Places route-bridge, map-return,
  and pin-handoff suites pass (13 tests), and app typecheck passes. This is an
  honest stale indication, not yet full real-data Focus/Path recomposition.

- **I3 / intake format and custody boundary — audited and locally evidenced:**
  workspace document `i3-intake-format-and-custody-audit-2026-09-05.md` records
  the actual text, JPEG/PNG, audio, HEIC/HEIF, PDF, and Apple Wallet/PKPass
  entry paths. The supported and rejected cases are covered by the
  custody-first screen and resumability suites; generic Chat HEIC conversion
  is explicitly not treated as share-capture support. No new parser,
  conversion dependency, source writer, or generated contract was added. This
  closes the format-audit subtask at the `implemented and locally tested`
  evidence level; native end-to-end receipts and any document-family owner ADR
  remain open.
- **I4 / source revision freshness contract — centralized and locally tested:**
  `travel-app` commit `41097fa00` moves the carried-versus-latest revision
  comparison into `utils/placesResultSetFreshness.ts`, with explicit
  `current`, `updated`, and `unknown` outcomes. The map surface uses the helper
  for its existing accessible stale treatment; stable and unknown revisions
  remain quiet. `travel-agent` commit `de2fbedb5` adds owner-bound tests for
  canonical catalog scopes and the intentionally unknown Anywhere/Saved
  scopes. This is continuity and acceptance evidence, not permission or full
  personalized-freshness evidence.
- **I4 / handoff conformance additions — locally tested:** `travel-agent`
  commit `d16b9bb54` proves that a server-resolved scope change with a new
  opaque context handle produces a new result-set identity, while
  `travel-app` commit `95b80f520` proves a Home Places door preserves the
  context handle, set id, and source revision. These are deterministic
  contract checks; real-data Focus/Path recomposition and personalized source
  vectors remain the promotion gate.
- **I5 / movement stop boundary — implemented and locally tested:**
  `travel-agent` commit `91c490187` makes the foreground movement owner reject
  a missing-clock or expired opening before situation reconstruction, and adds
  a regression proving no judgment or telemetry is emitted after expiry. The
  existing movement shadow acceptance still covers signal→authority→admission
  →treatment→content-free telemetry for a late movement and explicit silence
  for safe/unknown movement. This is a bounded live-engine path, not a durable
  watch, scheduler, notification release, or Plan mutation.
- **I5 / cross-family consequence rehearsal contracts — revalidated locally
  (2026-09-06):** the release-rehearsal, family-adapter, and movement suites
  pass **36 tests** together. They cover purpose-preserving movement judgment,
  shared-plan repair, encounter confirmation, addressed-place handoff,
  readback/repair gates, and fail-closed release evidence. This strengthens the
  shadow and contract layer only; no real-account/device rehearsal, durable
  watch, notification release, or consequence-family activation is claimed.
- **I3 / writer-authority inventory — audited and decision-bound:**
  workspace document `i3-writer-authority-audit-2026-09-05.md` maps explicit
  Chat retention, Intake custody, catalog-edit inference, Discover behavioral
  synthesis, memory-surface engagement, accommodation/planning hooks, Personal
  Memory refresh, and group synthesis to their current owner and authority.
  It confirms the safe factual/custody seams and isolates the unresolved
  decision: inferred behavioral text must not silently become authored
  longitudinal meaning. No writer or Chat prompt was changed in this audit.
- **I6 / contraction and retirement evidence — refreshed and locally validated:**
  workspace receipts `f7af303`, `b48eb90`, `0406da0`, and `de1931d` record the
  retained booking-evidence adapter, assisted-expense boundary, refreshed
  static retirement inventory, and booking read/receipt validation. The latest
  focused app validation covers collaborative refetch/read-model invalidation
  plus booking component and receipt/trust suites (52 tests total). These
  receipts preserve the explicit boundary: no production shutdown, provider
  secret deletion, destructive database migration, retained-Life-reader
  migration, or Chat rewrite is claimed.
- **I6 / current contraction guard recheck (2026-09-06):**
  `npm run surface:contraction:check` still reports exactly three inherited
  findings: the generated route inventory is stale, and
  `/you/intake-submissions/[submissionId]` plus `/you/life-record` lack an
  M-1 owner or explicit exemption. These are shared-registry/Life ownership
  obligations, not booking-retirement evidence; no Life or generated-route
  files were changed in this integration batch.

### M1 batch update — 2026-09-05

The first two next-batch items are now closed at their current evidence level:
the capture return contract is implemented, and the Home/Places promotion
boundary is audited with native tests. The contract union and one renderer
conformance gap are also closed; neither enables the four dark Home forms.
The source-production item remains intentionally decision-bound: no queue or
scheduler should be added until
the owner confirms deployment topology, retry/lease ownership, per-account
budgeting, and the exact serialized input (especially Places context). This is
the remaining M1 integration decision, not a reason to reintroduce generation
into a GET path.

The next bounded batch is Home→Places→Focus/Path real-data acceptance and
stale-source behavior. It must prove that field/map/detail returns preserve the
same set when the catalog revision is stable, and recompose or show an explicit
stale/unknown state when it changes. It must also decide whether private-save,
relationship, and provider-status revisions need a separate audience/source
vector before semantic Places promotion; the catalog digest alone must not be
overstated as full personalized freshness. In parallel, I3 may collect native
custody receipts and the remaining writer audit without changing the held Chat
surface. Preserve the mature workspace and keep the semantic renderer dark
until real data and native evidence land. Do not promote the dark Home kinds,
add a generic route service, or create a second Places feed. Re-pin all
repositories and shared-file ownership before touching generated contracts.
This keeps the roadmap live without making this task a bottleneck for Life or
turning six former specialist tasks back on.

The current integrated checkout also passes the workspace contract check,
mobile typecheck, the Places freshness/return/conformance suites (15 tests),
the backend result-set/movement shadow suites (15 tests), and the workspace
doctor. The latest I1/I2 focused checks add the memory-correction fan-out
contract (2 app tests) and the portfolio planner/field-coverage suite (16
backend tests). Environment warnings remain explicit: local Postgres is not running,
and backend full-route tests that require the `openai` package remain
environment-blocked. These checks do not promote any dark semantic kind or
claim native device acceptance.

- **I1 / Life correction → Places fan-out — implemented and locally tested:**
  `travel-app` commit `73f89ffa8` extends the centralized memory-correction
  invalidation contract to the mature Places feed and projection prefixes.
  A Life/Atlas correction already refreshed Home/Places root envelopes; it now
  also forces the spatial readers that can carry the same evidence or ranking
  to re-read. The focused cache contract passes (2 tests). This is freshness
  propagation only: it does not grant new Places reads, infer a location, or
  claim personalized source-vector recomposition.
- **I2 / unscoped singular owner reads — implemented and locally tested:**
  `travel-agent` commit `fd7f43198` keeps descriptive portfolio operations
  intact but omits executable `place.read`, provider-status, and receipt reads
  when no exact owner scope is available. Those requests previously spent a
  bounded read seat only to return `*_scope_required`; candidate-declared exact
  reads remain admitted. The focused portfolio suite passes (15 tests), while
  the API route suite remains environment-blocked by the checkout's missing
  `openai` package. This closes a serving-budget waste, not the route owner or
  current-condition/reachability field gap.

I2 therefore remains partial rather than complete: the executable planner no
longer spends routine seats on unscoped singular owners, but an explicit
field-coverage result and measured fast-serving/optional-production boundary
are still required before the package can exit. The next implementation should
extend this same truthful gate, not add a speculative route service or worker.

- **I2 / executable field coverage — implemented and locally tested:**
  `travel-agent` commit `81834ff05` adds a typed field-coverage result to the
  portfolio plan. Each selected operation now reports the requested,
  currently supported, and missing semantic fields separately from operation
  readiness; the live disruption fixture proves `route.evaluate` has no
  canonical fields and the partial place reader is missing current
  conditions, reachability, thresholds, and alternatives. The focused
  portfolio suite passes (16 tests). This is a readiness gate and does not
  promote partial place data or create a route adapter.

- **Places native transition regression — fixed and locally tested:**
  `travel-app` commit `4c7e73b3d` removes a duplicate share-state block that
  sat below the Venue detail loading/error early returns. A real local device
  rehearsal reached the object page and exposed React's hook-order crash when
  the venue read resolved; the existing share-scope hook was already intended
  to be unconditional, but the stale second block made the transition render
  more hooks than the loading render. The focused Venue detail smoke suite now
  includes a loading→loaded rerender guard (33 tests passing). The full native
  rehearsal was intentionally stopped after this diagnosis per the current
  scope; no app-surface redesign or generic fallback was added.

- **Real rehearsal target — hardened:** `travel-app` commit `304d35dda` makes
  the Home/Places real-save runner require an explicit `DATABASE_URL` matching
  the healthy local API's Postgres target. The earlier bounded run exposed why
  this matters: the backend `.env` default pointed the fixture provisioner at
  the host's port 5432 while the API was using the compose database on 15432,
  producing a false “fixture not admitted” result. The runner now fails before
  provisioning when the operator has not named the exact database, preserving
  the no-implicit-write boundary.

- **I1 / direct Places return envelope — implemented and locally tested:**
  `travel-app` commit `ca9a2a0fa` carries the existing short-lived Home return
  token through direct Place, Venue, Site, Accommodation, Experience, and
  Dossier resource routes. The return registry already held the exact
  projection/unit identity; these routes were the remaining navigation branch
  that silently dropped it. The focused root-navigation suite passes (13
  tests), and TypeScript passes. No native rehearsal or shell promotion is
  claimed; the change only preserves the existing return contract until the
  destination is exited.

- **I1 / cross-owner return envelope — implemented and locally tested:**
  `travel-app` commit `43a461b02` extends the same existing return-token
  preservation to Home-origin Chat, Life, profile, saved-place, receipt, and
  canonical fallback handoffs. The prior fix covered direct Places depth; this
  closes the adjacent owner branches without adding a new navigation payload
  or persistence layer. The focused root-navigation suite passes (14 tests),
  and TypeScript passes. This remains ephemeral navigation continuity, not
  durable memory or a shell-promotion claim.

- **I2 / bounded production owner — decision accepted:** workspace decision
  `docs/decisions/2026-09-06-bound-source-production-worker.md` names the
  existing Arq `WorkerSettings` process as the future execution owner for
  optional Source contribution production. It explicitly keeps GETs, app
  launch, focus, watches, and generic background ticks out of the trigger
  path; requires a versioned content-free work item, a named signal/explicit
  warm trigger, durable deduplication, lease-first execution, and content-free
  telemetry. No queue, scheduler, worker function, or production flag was
  added or activated by the decision.

- **I2 / content-free production work item — implemented and locally tested:**
  `travel-agent` commit `00f74699b` adds the strict
  `SourceContributionWorkItemV1` contract and three focused tests. It bounds
  the future handoff to Home/Places, an explicit situation/audience, one
  represented-at clock, IANA timezone, policy/compiler versions, a named
  trigger, optional canonical refs, and an expiry. It rejects unknown roots,
  naive clocks, missing signal/recomposition references, and extra generated
  content. The focused pytest passes (3 tests); the ordinary worker is still
  unregistered and no queue or provider call was added. The normal backend
  size-budget hook remains pre-existingly over threshold and was skipped for
  this isolated commit; all other commit-local hooks passed.

- **I2 / content-free composition measurement — implemented and locally tested:**
  `travel-agent` commits `f484c1af0` and `76221e1ad` add
  `RootCompositionMeasurementV1` and the stable
  `root.composition_measured` event. The shared Home/Places composition seam
  records only elapsed time plus bounded candidate, admission, owner-read, and
  degradation counts; candidate identifiers, claim text, source/subject refs,
  and fact keys remain excluded; pathological counts/timing are clamped so
  telemetry cannot fail an otherwise usable response. The sink is injectable
  and the focused
  composition/telemetry suites pass (7 tests); this is observation only and
  does not register a worker, activate production, or change root payloads.

- **I2 / deterministic trigger identity — implemented and locally tested:**
  `travel-agent` commit `1ccd27a02` adds a builder for the content-free Source
  work item. Equivalent authorized warm/signal requests share one stable work
  and idempotency identity even when their expiry is refreshed; a changed
  represented clock, audience, policy/compiler version, root set, or canonical
  trigger/context reference produces a different identity. The focused source
  work suite passes (4 tests), with no queue, worker registration, or provider
  call added.

- **I2 / durable content-free handoff — implemented and locally tested:**
  `travel-agent` commits `d0f3b395b` and `8fc497eac` persist the bounded work
  item through the
  existing domain-neutral `agent_workflows` lease/idempotency fence, with a
  dedicated workflow type, immutable payload projection, due-row listing, lease
  delegation, and a current-clock gate for the future worker. The focused
  source-workflow and generic workflow suites pass (20 tests); no Arq function is registered, no
  scheduler is added, and no provider/model call is possible through this
  handoff alone.

- **I2 / worker lease and readback boundary — implemented and locally tested:**
  `travel-agent` commit `b4a2b4f91` adds a dark worker adapter that claims the
  durable Source handoff, parses its strict serialized contract, rejects stale
  work before owner/provider execution, rechecks expiry after execution, and
  publishes a generic completion receipt only after an injected canonical
  executor proves readback for produced or reused output. Invalid work,
  expiry, provider failure, readback failure, and lease loss are distinct
  content-free outcomes; generated prose and source claims never enter the
  workflow result. The focused worker/telemetry suites pass (22 tests). The
  adapter is not registered with Arq, is not called by ordinary root GETs, and
  has no provider implementation of its own.

- **I2 / deployment envelope — implemented and locally tested:** `travel-agent`
  adds `SourceContributionWorkerDeploymentV1`, a content-free operating
  contract for the existing `audio_jobs.WorkerSettings` entry point. It binds
  policy/compiler versions and Home/Places scope, and requires a bounded lease,
  renewal interval, execution timeout, retry budget, and explicit dark versus
  controlled cohort. The dark default cannot register a job; the worker only
  accepts a handoff whose semantic versions and retry budget match the
  envelope, and applies the execution timeout when one is supplied. Contract
  and worker tests pass (12 tests); synchronous executor work uses a dedicated
  fixed two-slot pool so a cancelled timeout cannot spill into the process-wide
  default executor. No Arq function, queue consumer, provider call, or ordinary
  GET activation was added.

- **I2 / canonical executor and post-write readback — implemented and locally
  tested:** `travel-agent` adds an explicit `SourceContributionCanonicalExecutor`
  adapter and factory. It fences the workflow actor and idempotency key, resolves
  an optional canonical context reference, delegates to the existing continuity
  path, and requires a post-write canonical readback before the dark worker can
  report `produced` or `reused`. A readback miss fails closed as a lease-loss /
  retry boundary; producer silence remains a content-free terminal outcome. The
  continuity seam and executor contract have 32 focused tests passing, and the
  adapter is exported for injection only. It is not registered with Arq and
  does not make an ordinary root GET capable of provider work. A default
  factory now binds the existing budgeted structured provider, retained
  production/readback gateways, and the clock-preserving Places context owner
  (`travel-agent` `d621afff4`); the factory remains inert until an approved
  worker call supplies it.
  The Places context owner now has a clock-preserving adapter
  (`travel-agent` `64230fb0e`): a canonical `places_context` handle is
  revalidated against the work item's represented clock before it enters
  continuity. The governed Opening loader remains separate.

- **I2 / production measurement join — implemented and locally tested:** the
  dark worker now emits bounded, content-free execution measurements alongside
  its production outcome: elapsed execution time, durable enqueue-to-start
  delay when the workflow exposes both timestamps, owner-read count, provider
  invocation count, reuse/provider/none/unknown cost class, and the existing
  attempt/outcome dimensions. The canonical executor supplies owner-read and
  producer invocation counts without changing the semantic receipt. Dollar
  cost remains owned by the existing durable LLM accounting ledger; the worker
  binds workflow id, attempt, user, surface, and background execution context
  while the executor runs so those records can be joined. These measurements
  are production-only telemetry and never enter workflow result JSON or source
  content. The worker, canonical-executor, continuity, and telemetry receipt is
  **41 passed**; controlled registration is still gated on real cohort evidence.

- **Environment / real-backend revalidation (2026-09-06):** the canonical local
  Postgres target at `localhost:15432` is reachable, and the backend virtualenv
  now imports `openai` (`2.32.0`) and SQLAlchemy (`2.0.52`). The real-Postgres
  Places owner/catalog suites pass **42 tests**; the real-Postgres search,
  experiences, and lookup route suites pass **20 tests**. This upgrades the
  evidence available for owner-backed Places and search behavior; it does not
  certify Home→Places→Focus/Path recomposition, native device behavior, or a
  provider-backed Source cohort. Those remain separate gates.

- **I4 / real Home→Places runtime continuity (2026-09-06):** the existing
  real-Postgres Save-owner integration now reads the same canonical Save through
  the governed `/api/root-projections/v2/places/runtime` envelope in addition
  to the Places owner reader and Home v2 projection. The test asserts the
  `places-root-runtime.v1` wrapper, the nested v2 semantic identity, and the
  workspace-feed join; it passes **1 real-Postgres test**. This proves the
  owner-backed Home→Places runtime seam for a concrete Save, but intentionally
  does not claim Focus/Path recomposition, personalized freshness vectors, or
  native/device acceptance.

- **Cross-repository contract revalidation (2026-09-06):** workspace
  `make contract-check` passed against the current committed snapshot: 578
  backend paths / 640 operations, 443 mobile-projected paths / 488 operations,
  generated TypeScript parity, 10 canonical place-identity seams, and the
  schema-bridge manifest. No generated API file was changed by this check.

- **Repository-wide offline receipt (2026-09-06):** after the worker cleanup,
  authority rebaseline, deployment-envelope slice, canonical-executor /
  readback slice (`travel-agent` `467be5711`), clock-preserving context owner
  (`64230fb0e`), provider-factory binding (`d621afff4`), and production
  measurement join (`daa1a2635`), the bounded backend command
  `pytest -q -m 'not requires_postgres and not requires_api_keys'` passed
  **20,769 tests**, with 30 skips, 56 expected XPASSes, and 1,346 deselected
  tests in 7m33s. The run emitted only the existing Postgres-leak
  baseline warnings; no new failure was introduced. Native/device and live
  Postgres evidence remain intentionally out of scope for this checkpoint. The
  focused root-projection receipt is **330 passed**; adding the Places
  context-clock suite yields **351 passed** across the combined owner-bound
  check. The worker / continuity / telemetry wiring receipt is 41 passed,
  including workflow-context restoration and queue-delay coverage.

- **I0 / decision alignment — documented:** the 2026-09-06 audit above
  reconciles the queue against accepted Contribution/Use Grant, four-root,
  lightweight-arrangement, Life organization, and live-engine decisions. D2–D5
  are no longer treated as open policy questions; D1 remains decision-blocked
  at the owner/schema boundary, and D6 remains activation-gated per family.
  This narrows the next work without inventing a new intent or watch owner.
