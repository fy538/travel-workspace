---
doc_type: working
status: active
owner: founder / Integration task
created: 2026-09-05
last_verified: 2026-09-07
expires: 2026-10-05
why_new: Rebaselines the post-pivot system around the real-world live engine and four surfaces, with code-backed correction priorities, explicit Life ownership, bounded Luna delegation, and recurring architectural and product reassessment.
supersedes:
  - forward execution sequencing in vesper-product-system-build-program-2026-09-01.md
  - orchestration and lane allocation in home-places-life-productization-program-2026-09-04.md
source_of_truth_for:
  - Integration task complete-system sequencing
  - live-engine integration across context, judgment, surfaces and continuity
  - current cross-lane coordination and receiving interfaces
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

**September 6 strategic reconciliation:** the accepted
[consumer-strategy decision](../decisions/2026-09-06-reconcile-consumer-strategy.md)
makes everyday value intrinsic, with travel a demanding specialization rather
than a mandatory launch entrance. Continue the complete portfolio and existing
milestones; no new architecture, release flag or lane is created by that change.
Optional conversational continuity is accepted direction but its policy remains
unadopted: D4/history work must preserve current Ask authority. D1/pre-Plan intent
still needs its owner decision. Retaining intent is not accepting a watch;
I2/I5 must distinguish present assessment, monitoring and authorized changes.
Provider execution stays retired in product scope with finite recovery duties.
Consumer-paid depth/capacity is an economic hypothesis: preserve bounded serving,
production and watch costs without adding billing or paid authority now. Exact
prices, geography and entitlement/service-period behavior remain open. This
paragraph does not upgrade any implementation or production readiness receipt.

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

The **Integration** task (`01a030af-13a8-74e1-81be-7d526bec3045`) owns this
cross-system program. The September 7 receiving update in §2 retains Integration
and Life engineering ownership and adds Content's supplier responsibility. The
separate **Strategy** task supplies product decisions, not a competing execution
queue. Assignment here does not claim a task is running or was dispatched.

**September 7 supply clarification:** the system has three complementary ways
to obtain value—explicit investigation, bounded reusable public/world
preparation, and authorized private preparation. They share judgment and root
delivery, but not authority, privacy or retention. Home/Places must be useful
from eligible prepared material without initiating acquisition on every read;
private Source production is one path, not the universal recommendation
backend. CV-3 and the checkpoints in §9 make this distinction executable.

This document replaces older cross-system ordering and lane allocation. Lane
roadmaps retain internal package detail; their code, acceptance cases and
historical receipts remain evidence. Product canon and operational release
procedures retain their authority.

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

<a id="2-current-coordination-register--september-6"></a>

## 2. Current coordination register — September 7

**September 7 receiving update:** Integration and Life remain the engineering
owners below. The active Content task (`01a07c63-5ebe-71d2-9cb0-314ec4e06963`)
now owns world-supply research and its implementation handoff. Strategy
(`01a072c6-2735-7152-94ea-bb6958ead53d`) proposes a bounded Social participation
task; it has not been dispatched by this register. This supersedes the older
two-task allocation wherever it would exclude these complementary responsibilities.
Integration remains the sole landing owner for shared read, judgment and root
composition changes. Current receiving work and checkpoints are in §9.5.

| Additional responsibility | Authoritative context | Current package | Promised interface | Dependency / next checkpoint |
| --- | --- | --- | --- | --- |
| Content — active research task | Editorial canon; Strategy September 7 world-supply discussion; CV-3 below | Provider coverage, proactive supply, selective indexing and economics evaluation | Supported candidate identity, evidence, freshness, permitted reuse/display, continuation and acquisition/refresh cost | Integration receives a concrete supplier contract before adding provider-dependent runtime paths; private preparation and public retrieval retain distinct authority |
| Social — proposed bounded task | Multiplayer Product Strategy; lightweight-arrangements handoff; Home J2 | Audit share-from-day, addressed recommendation and optional gathering as complete sender/recipient experiences | Original material, sender/recipient scope, source identity, expiry/withdrawal, exact response or owner continuation | Integration owns common composition, Life owns indexing; no new social store/feed or automatic dispatch |

**Post-investigation rebaseline, September 6:** the founder accepted two
persistent engineering lanes: **Integration** owns connected value delivery and
live integration, including Home/Places consumers; **Life** owns continuity,
organization and reader migration. This supersedes the earlier same-day
three-delivery-lane assignment, not I0–I6 or the lane plans' acceptance criteria.
Home, Capture, Entities, Components and Plan, and Retirement remain bounded
support responsibilities, not separate expanding engineering programs. Strategy
continues to resolve product choices without becoming an engineering gate for
already accepted contracts. Existing user-owned tasks are not automatically
started by this register; temporary subagents execute explicitly bounded work.

September 6 implementation bases: workspace `1a2d2ac`, backend `329c91f87`, app
`38d3a6521`. Backend `d37967e6f` already merged Life population/reconciliation;
app `38d3a6521` already merged lens/refind continuity. Root design/inventory and
market-research edits present at this checkpoint belong to concurrent work and
are outside this package.

**September 7 planning refresh:** audited backend base `7b1d8a6b0`, workspace
base `2f78a82`, app base `38d3a6521`. CV-1 serving and Life restore/target
capability work have advanced. The audit found incomplete practical-field
coverage and judgment integration; the next implementation sequence is
[§9.4](#94-cv-2-detailed-execution-plan--september-7). Its packages are planned,
not additional implementation receipts. Concurrent design, inventory and
market-research edits remain outside this refresh.

| Lane / cadence | Authoritative execution plan | Current package | Promised interface | Dependency / receiving owner | Next checkpoint |
| --- | --- | --- | --- | --- | --- |
| **Integration** — persistent connected-value/live lane | This roadmap I0–I6; [Home/Places implementation map](home-connected-experience-implementation-map-2026-09-04.md) | CV-1 implemented; CV-2 A/B coverage and temporal repair, then C/D cache-backed venue facts into judgment (§9.4) | Field-specific current evidence and claim-specific practical assessment through existing root contracts; source/context revisions; no production on GET | Existing Places cache and owner reads; shared value judgment; Home/Places portfolio; Life exact destinations | First coverage/revision checkpoint, then actual open/closed/unknown facts change the appropriate offer while independent value survives |
| **Life** — persistent continuity lane | [Life R0–R8](life-complete-system-and-atlas-replacement-roadmap-2026-09-05.md) | R2 target-version continuity, coverage and reconciliation; then R2-G organization and R3–R5 reader/custody integration | Exact eligible record/ref, revision, bounded query/restore, withdrawal, and truthful population versus live-delivery status | Existing source/graph owner events; indexed serving requires parity and target delivery; D1 only for prospective writes | Default shadow continuity and future-target limitations explicit; coverage/parity evidence before any serving switch |
| **Home** — bounded support within Integration | [Connected implementation map](home-connected-experience-implementation-map-2026-09-04.md), consuming I4 | Receiving renderer/destination failures from CV-1/CV-2; complete varied value, not more kinds | Existing typed producer-to-renderer mapping and exact return | Integration supply; Entities depth; Life readers | A named consumer gap closes; no separate generator or expanding feature backlog |
| **Contribution and Capture** — bounded support | [CC-0–CC-6](contribution-contract-and-legacy-memory-migration-plan-2026-08-29.md#11-completion-plan--september-5) | Named lifecycle/correction failures exposed by connected value or Life | Effective gesture/authority, source refs, retry identity, lifecycle and owner readback | History proposal for history-specific expiry; Life consumes source events; D1 only for loose intent | Source and derivatives obey custody across use, retry and repair; immediate value precedes optional management |
| **Components and Plan** — design/decision, then engineering | [Arrangement A0–A4](lightweight-arrangements-implementation-handoff-2026-09-04.md), [design handoff](claude-design-plans-in-real-life-handoff-2026-09-04.md) | A0 owner/command packet; latest §0.8 continuation refinements | Distinct propose/update/send/participate/adopt effects, exact arrangement ref and readback | D1; settled use-grant policy plus concrete adapters; live engine supplies practical judgment | Map reduced designs to commands; ratify any seven-sentence exceptions before building them |
| **Entities** — targeted support/closure | [C0–C8 acceptance plan](entity-system-acceptance-plan-2026-09-05.md) | Concrete receiving-lane failures and scoped lifecycle closure | Canonical venue/site/experience reads, citations, independently gated research/people, exact return | Home/Places and Life callers; no new entity-family scope | Reproduce and close a named cross-entry/withdrawal failure; no generic expansion or backfill |
| **Retirement** — replacement-bound batches | [SC-0–SC-6](product-surface-contraction-investigation-2026-09-04.md#20-next-execution-sequence--september-5-rebaseline) | SC-0/1 retained-reader adoption, then family-specific removal | Existing booking evidence refs, external continuation and deterministic expense owner | Life/Home receive evidence; Capture receives receipts; Plan owns arrangement replacements | Receiving path works and remaining caller/obligation inventory names what may be removed |
| **Strategy** — bounded decisions | Product canon; proposals linked below, not a separate engineering roadmap | Adaptive/social policy alignment and decision ratification | Explicit adopted versus proposed behavior; no implicit runtime/retention grants | Founder choices; lane feedback on concrete conflicts | Resolve one blocking choice; preserve accepted baseline until explicitly amended |
| **Repo Clean Up** — on demand | Current landing package and this register | Coordinated landing and repository verification | Exact repo/commit/worktree disposition; current remote evidence | Owners finish their packages; shared generators serialize | Land approved work without sweeping concurrent edits; no perpetual cleanup program |

### Decision queue and autonomous work

- **D1:** [retained-intention proposal](retained-intention-before-plan-decision-proposal-2026-09-06.md).
  Components and Plan proposes the owner; Integration, Life and Capture review
  commands/consumers. It remains unadopted; no synthetic Plan or Life-only writer.
- **D4 refinement:** [history/source-expiry proposal](conversation-history-source-expiry-decision-proposal-2026-09-06.md).
  Five-axis policy is settled, but history-specific lifecycle/migration is not.
  Optional conversational continuity remains unadopted.
- **Social baseline:** September 5 assigns casual place-sharing browse to
  Places' friends scope and durable history to Life People. September 6 research
  can refine effort, discoverability and presentation; it does not silently
  reopen root ownership. A placement change needs an explicit amendment.
- **Design exceptions:** crown access/priority and seven-sentence Plan exceptions
  remain proposals where the receiving handoff labels them so. No broad redesign
  or invisible authority change follows from a compelling board.
- **D6:** a production worker is not a watch owner. Each live family still needs
  a signal, freshness, reevaluation, expiry/cancel and consequence contract.

Proceed independently on accepted contracts and owned files. Bring changes to
canonical owners/schema, shared commands/events, API contracts, cross-root
navigation, activation, retirement or accepted product decisions to Integration.
Visual refinement, internal adapters and scoped tests do not require a universal
approval round. A handoff names source SHA, interface/guarantees, unavailable
cases, receiving consumer, files, regression evidence and next checkpoint.

Life R6 consumes I3's intention/shared-material contract. Life R7 and I2/I4
share production and allocation interfaces. Those specific dependencies do not
block Life's other packages. Do not create separate Home and Life generators
while waiting for a contract.
The engine reads relevant source, intent and outcome owners directly through
agreed contracts; it does not scrape the Life UI or depend on a Life page being
opened. Life and the engine are different consumers of those authorities.

Before any task changes a shared model, route file, generated schema,
navigation utility or invalidation policy, declare the exact files and contract
change. Shared files are serial integration points, not parallel writing areas.
For future coordination, communicate one bounded dependency request rather than
redirecting the other task's whole program. The current execution uses temporary
bounded implementation/review agents, not new user-owned tasks. Use isolated
`codex/` worktrees for concurrent implementation;
serialize shared schema/route generation and landing. Explicit filename staging
does not protect against another task's already-staged changes. Inspect staged
paths before committing and never reset another lane to obtain a clean tree.

Review after a connected package, after at most three integrated packages, or
when a material contradiction appears. Use local tests during current execution;
the founder deferred app/device testing for now. Keep native/release gates
explicit without making them a prerequisite for unrelated engineering. A
checkpoint records what to continue, revise or retire, not another blanket
revalidation loop. This register is the current assignment map; older task
activity tables and receipts elsewhere are dated evidence.

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
| D1 — pre-Plan intention | [Review-ready owner proposal](retained-intention-before-plan-decision-proposal-2026-09-06.md); no required Plan | Adoption and schema review before durable loose-Keep writes and Life Ahead adoption |
| D2 — shared human material | Reuse source/authored payload custody with an explicit target/adoption relation | Generic Plan/Occasion comments and suggestion adoption |
| D3 — scoped editing | Separate revocable target/effect grant, not a new organizer/member role or implicit AI mandate | Collaborative edits beyond existing owner-only commands |
| D4 — retention boundaries | Settled five-axis contract plus [history/source-expiry proposal](conversation-history-source-expiry-decision-proposal-2026-09-06.md) | History-specific migration and any continuity expansion await adoption; unaffected writer repairs proceed |
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
| D4 — retention boundaries | Existing decisions separate Source, claims, projections, purposes and retention; the September 6 history proposal specifies the remaining copy/answer-lifecycle choice | **General policy settled; history-specific proposal unadopted; writer audit partial** | Complete unaffected repairs; obtain explicit history semantics before migration; optional conversational continuity is not enabled |
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
- Apply the [accepted bounded worker decision](../decisions/2026-09-06-bound-source-production-worker.md)
  to the [useful-preparation specimens](situated-value-decision-matrix-2026-09-06.md#12-useful-preparation-three-concrete-receiving-experiences):
  bind each produced result to a permitted named trigger, eligible source/use
  scope, bounded executor/budget, deadline, canonical readback and delivery path.
  Ordinary GETs, focus and app launch cannot enqueue optional production. Reuse
  current work-item/lease/executor seams; their existence is not activation or
  proof a particular specimen has its trigger and producer. Resolve the missing
  binding, not a new scheduler. Keep source revocation, late completion,
  unsupported production and requested-work failure in acceptance coverage.
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
- Implement the [Home receiving requirements](home-connected-experience-implementation-map-2026-09-04.md#useful-preparation-receiving-requirements)
  across ready, accepted-work-pending and unsupported results. Deliver substance
  when ready; preserve useful existing material while waiting without implying
  fit or filling Home with jobs. Receive later completion without scroll jumps,
  duplicate cards or automatic push; remove invalid claims promptly. Refreshing
  an existing offer need not promote it as new. Review E1–E3 for actual benefit,
  optional continuation and total organizer/recipient effort, separately from
  technical correctness. These are varied system acceptance cases, not a single
  showcase loop or authorization to expose gated kinds.
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

The Integration parent owns architecture coordination, the roadmap, shared contracts,
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

## 9. Current execution ledger and next batch

| Package | State rebaselined September 6 | Next concrete action |
| --- | --- | --- |
| I0 | Implemented/integrated at inventory level; live-engine path matrix and 2026-09-06 decision-alignment audit recorded | Keep D1 retained-intention ownership and family-specific D6 watch contracts gated; consume accepted general D2–D5 policy through I1–I3 adapters without treating D4's history/source-expiry proposal as adopted |
| I1 | Integrated for request-clock, consequence fan-out, source/graph Life delivery, owner-fenced publication, audience/withdrawal repair, bounded enumeration, resumable backfill, reconciliation and full typed comparison; source representation transitions and Outcome adapters are no longer missing foundation | Establish population/coverage and target-version live delivery before indexed serving; PostgreSQL interleaving evidence remains distinct from offline tests |
| I2 | Bounded reads, fast assembly, source storage/reuse, trigger/workflow identity, dark worker budgets/leases, canonical executor/context/provider binding and telemetry are implemented; CV-1 now connects current prepared results to ordinary Home/Places reads (§9.2) | Close the ordinary-read acquisition leak, then connect practical truth and the three supply modes (explicit investigation, reusable public/world preparation, and authorized private preparation) through judgment→delivery. Cost/cohort evidence and worker registration remain separately gated |
| I3 | CC-0/1 reader/authority/retry repairs, deadline/custody/processing-copy restrictions, source-owner handoff metadata, bounded writer conformance (itinerary, Atlas, Discover), and useful-first capture ordering are locally evidenced; history-specific lifecycle and owner commands remain gated | Capture coordinates Life readback/correction over the existing envelope; review the two September 6 decision proposals before dependent writes; native/content evidence stays deferred for current engineering |
| I4 | Renderer promotion, result-set identity, source-backed revision, native returns, stale-source treatment and a four-value-family owner-backed Home portfolio are implemented and locally tested; rollout remains internal | Receive prepared results through existing native kinds and complete practical/social/continuity handoffs; real-data and native quality remain unevidenced by these tests |
| I5 | Graph/consequence foundations present; movement signal→judgment shadow path is locally evidenced; lightweight experience remains incomplete | Complete adaptation and shared consequences over I1–I3, preserving purpose, plural participation, and meaningful stop/wait behavior |
| I6 | Inventories, guards, retained booking-evidence and assisted-expense contracts are recorded and locally validated; destructive cutovers remain incomplete | Run environment obligation audits, migrate actual retained readers, and remove only execution paths with no remaining consumer or obligation |

**Next connected work:** CV-2 below alongside Life's R2 coverage and
reconciliation work; the first CV-1/target-capability receipt is in §9.2.
Do not rebuild source delivery, representation withdrawal,
Outcome adapters, backfill or reconciliation from older receipts. The next
stage connects existing capabilities and makes migration claims precise. New
persistence, paid/provider work, watches and activation retain their own gates.
Use §2's register for responsibility and the existing lane plans for detail.

### 9.1 Connected-value execution sequence

This is the next sequence within I1–I5, not a new product architecture or a
one-loop proof program. All four moves remain represented by the acceptance
portfolio. A package is reviewable scope, not the definition of Vesper.

| Order | Outcome / implementation boundary | Exit and reassessment |
| --- | --- | --- |
| **CV-0 — ordinary serving is acquisition-free** | Trace every Home/Places root caller, including the nearby corpus/provider fallback and optional reachability/travel-time branches. Split read-only serving from explicit discovery/preparation while preserving useful corpus and prepared material on a miss. | Under cold-cache/thin-corpus fixtures, an ordinary Home/Places read makes no provider, model, enqueue or write call. Explicit map/search/investigation paths retain their own bounded acquisition authority. This is a boundary gate for all later CV packages. |
| **CV-1 — prepared value reaches ordinary root reads** | Reuse current Source opportunity identities, `root_source_contributions`, canonical loaders, shared root composition, value admission and existing native anatomy. Add read-only admission of eligible retained results to Home and both Places v2 callers. Do not call the producer-or-reuse orchestration from GET. | Eligible complete-on-view value survives; misses, expired/revoked/changed sources and unavailable reads omit optional value while owner-backed material remains. Zero enqueue, lease claims, provider calls or new retention from a root read. |
| **CV-2 — practical truth reaches common judgment** | Audit and join existing route/movement, Place conditions and Moment owners to the supported read mesh. Start from an available exact route/condition owner, not another coordinator or speculative `route.evaluate` implementation. | Known versus unknown feasibility changes a prepared possibility or live adaptation; stale facts do not become confident claims. Reassess owner coverage before widening a family. No new watch or provider integration implied. |
| **CV-3 — supply modes reach judgment and delivery** | Connect three deliberately different paths to the same receiving system: (a) explicit investigation for a user request, (b) bounded reusable public/world preparation for approved places, topics or time windows, and (c) authorized private preparation through the existing Source work item, executor, lease and readback. Carry evidence, rights, freshness, cost and exact continuation into common judgment, live assessment and Home/Places composition. | Each supported value family has a named supply owner and an end-to-end fixture from candidate/evidence to useful output. A public candidate does not require private history; private production does not become public supply. Unsupported triggers remain unavailable. Controlled paid measurement/worker registration requires separate gates; no generation on launch/focus/GET. |
| **CV-4 — whole-system consumer completion and contraction** | Resolve exact Home/Places→owner→Life handoffs, practical shared effects, source correction and low-burden effect copy. Accept named support packages from Capture/Entities/Plan/Retirement. | A varied everyday, practical, social and continuity portfolio operates coherently. Remove replaced consumers only after obligations and receiving paths are established. No Chat entrance redesign or production cutover implied. |

**CV-1 implementation packet:**

- Classify as `safe-backend` while limited to root-projection internal reads,
  composition and tests. Any schema/API/auth change exits this packet and
  follows the repository's approval and contract-sync workflow.
- Owner: Integration. Files: `backend/root_projection/v2/` read-only serving
  adapter, `backend/api/services/root_composition.py`, focused root/API tests,
  and the subsystem `FEATURE.md`. No new store, prompt, queue or mobile kind.
- Resolve the current viewer, situation, allowed roots and exact evidence /
  subject / context / audience identity through existing metadata owners.
  A retained production is not authority by itself; current source reads and
  ordinary value admission remain mandatory. Do not broaden cross-root reuse
  by stripping meaning-bearing context from a key.
- Bound the optional read with the existing bounded blocking-reader mechanism;
  do not rely on cancelling `to_thread` to stop underlying work. Timeout or
  missing storage cannot erase the base portfolio. Keep metrics content-free.
- Reuse one semantic production with its distinct Home/Places expressions;
  preserve source refs, expiry and delivery identity. Neither a cache hit nor
  a root GET is evidence of user receipt or new knowledge.
- Local acceptance: cache hit and miss; changed/removed/revoked source;
  context/situation/viewer/audience mismatch; expired value; delayed/unavailable
  storage; both root consumers including Places runtime; no inline producer or
  work scheduling even when the production flag is enabled. Keep base state,
  human contributions and practical instruments available.
- Report separately: implemented, locally tested, integrated, real-data
  evidenced, native evidenced and enabled. This packet does not establish
  plentiful production supply or consumer delight just by serving a fixture.

#### CV-3 supply-mode receiving contract

CV-3 is deliberately a **three-path supply program**, not a decision to make
every Home item a private background job. The paths share candidate, evidence,
judgment and root-delivery contracts, but they do not share authority or
retention semantics:

| Supply mode | Initial owner / trigger | Appropriate output | Explicit boundary |
| --- | --- | --- | --- |
| **Explicit investigation** | Existing Chat/action request with authenticated request identity, bounded place/topic/time scope and a finite deadline | A ready answer or small set of worthwhile possibilities, including a qualified world-first option when evidence supports it | It may acquire on demand, but it must not silently become a watch, durable intention, or global catalog write |
| **Public/world preparation** | A separately approved Content/Integration preparation job for a supported market, topic or time window | Selective reusable world evidence and candidate possibilities that can be judged for multiple people | Queries contain no private conversation or friend constraints; provider rights, refresh, cost and admission are explicit before activation |
| **Authorized private preparation** | An explicit user-requested warm action first; an adopted signal owner only after its authority, cancellation and expiry are implemented | Source-derived preparation scoped to the viewer, allowed roots, current purpose and eligible private material | The current Source executor remains explicit-warm only; source correction/refind and projection repair are not fresh-generation mandates |

All three paths must end at the same typed receiving boundary: candidate
identity, decisive evidence, claim-specific validity, rights/display policy,
judgment, practical dependencies, cost and exact continuation. Home and Places
then choose the appropriate expression for the current situation. A prepared
item is not automatically a Life artifact, shared contribution, notification,
booking action or durable user fact.

**CV-3 checkpoint:** exercise at least one representative case for each mode
through supply → evidence → judgment → Home/Places delivery → exact
continuation, plus missing, stale, conflicting, revoked and cancelled variants.
The portfolio must include cold-start world value, a private cross-source
connection and an ordinary practical/social possibility. Passing means the
system can explain what it knows, what it cannot verify and what the person can
do next without another input exercise. It does not require live providers,
production worker registration or a comprehensive world index.

**Parallel Life checkpoint:** continue R2–R5 from the merged implementation.
First make explicit that non-`life.v1` historical target builds currently lack
live owner fanout; preserve useful shadow rebuilds and dry-run comparison.
Then establish owner coverage and reconciliation evidence, close true
publication-race gaps, and implement deterministic organization/correction.
Reader cutover still requires population, delta continuity, viewer parity and
withdrawal correctness. Merely finishing a backfill is not cutover readiness.

Reassess after CV-1 plus the parallel Life package, then after each connected
package or at most three integrated packages. The questions are: did users gain
a supported value path; did we duplicate an owner; what remains unavailable;
and what should stop or change before the next batch? Do not reopen settled
philosophy or require every design lane to finish before accepted work proceeds.

### 9.2 CV-1 and Life target-capability execution receipt — September 6

The first two-lane batch connects an existing result to its consumers; it does
not add a fifth root, generator, owner, retention policy or product grammar.

**Integration implementation:** backend `59f323b31` adds read-only prepared
Source admission to ordinary Home v2, Places v2 and Places-runtime composition.
It resolves the current viewer/situation and exact source/context group,
reads the existing retained result, revalidates canonical source and context
custody, and rebuilds candidates through the existing compiler. A miss remains
a miss: no enqueue, lease claim, provider invocation or new retention occurs.
Expired, shortened-custody, changed, unavailable or mismatched material cannot
borrow the retained payload's old authority. A private result cannot become
shared through root consumption. Retained JSON database values now pass through
JSON-mode validation rather than the incompatible strict Python-input path.

Backend `b25702bb1` preserves the final owner boundary: Source refs require
`source.inspect`, while exact Opening dependencies require `moment.read`.
Unrelated unknown conditions/position do not invalidate an interpretation, but
a missing, changed, withdrawn or expired Opening does. Home and Places retain
their distinct expressions and the same meaning-bearing identity. Final root
owner reads and value admission still run; prepared discovery is not authority.

Optional reads use a 350 ms initial internal deadline, not a measured latency
SLO. Known read errors are sanitized before they can reach late-work logging.
Base owner-backed material remains available on optional timeout or failure.
Backend `7a8a6f58c` additionally caps optional submitted/running/queued work at
eight on the existing executor. Saturation returns unavailable without another
submission. Cancelled queued work remains a no-op holding its permit until the
physical item drains, preventing repeated deadlines from accumulating queued
closures. Mandatory supporting-read semantics are unchanged; this is not a
claim that all backend work queues have been bounded.
No new public model, route shape, schema, mobile type or mobile screen changed.

**Parallel Life implementation:** backend `77eb3780b` exposes target fanout
capability on the existing backfill run and worker result. The default
`life.v1` target is covered by current version-less owner events;
non-default targets remain `historical_shadow_only`. This preserves legitimate
shadow builds without treating completion as continuous reconciliation.
Capability metadata is not evidence that workers ran, a corpus is populated,
all owners are covered, or indexed serving is ready. No subscription, writer,
serving flag or release policy was changed.

**Local evidence:**

- Combined root, API, retained-record, canonical-owner, Life, Life-worker and
  Places orchestration offline suites: **621 passed, 9 deselected** after the
  restore correction and CV-2 proof.
  HTTP tests exercise all three callers with production disabled and enabled;
  canonical-owner tests separately exercise actual read compilation and value
  judgment. Neither is native or paid-production evidence.
- Broader backend run on the initial CV-1 state, before final review fixes
  and Life integration:
  **20,931 passed, 1 failed, 30 skipped, 1,361 deselected, 56 xpassed**.
  The failing `test_hpl_manifest_keeps_social_authority_explicit` compares a
  legacy revision `3` against the current Occasion audience fingerprint. It
  also fails on unchanged backend `329c91f87`; this is a reproduced baseline
  failure, not a green full-suite claim. Some tests explicitly allow baseline
  local PostgreSQL access despite the offline marker selection.
- Life's PostgreSQL restore cases now pass: **2 passed, 10 deselected** for
  the retained-source projector file, including the old-revision and revoked
  row cases. Backend `7b1d8a6b0` makes `source_unrepresented` an explicit
  owner-authorized restoration path for an existing withdrawn row and uses the
  event owner revision as its read clock. This is shadow-index/readback proof;
  it does not establish corpus coverage, live target fanout, or reader cutover.
- Ruff, formatting, diff checks and applicable commit guards passed. The
  existing size-budget hook failed on seven untouched function/file entries;
  only that hook was explicitly skipped for commits. No baseline was raised.
  Workspace link validation retains two unrelated missing targets (`runs/`
  and `state`). The isolated baseline inventory reports 32 existing
  unclassified documents; no document was created by this batch, and the
  concurrent main-checkout inventory edits were left untouched. Spine and
  touched-document commit guards passed.

Reproduce the final focused check from the backend root with its development
environment active:

```bash
PYTHONPATH=. python -m pytest -q tests/root_projection \
  tests/api/test_root_composition_service.py tests/api/test_root_projections.py \
  tests/core/test_source_contributions.py tests/concierge/test_canonical_owner_reads.py \
  tests/life_projection tests/workers/test_life_projection_jobs.py \
  tests/places/test_feed_orchestration.py tests/places/test_feed_orchestration_characterization.py \
  -m 'not requires_postgres and not requires_api_keys' --tb=short --maxfail=3
```

The five backend commits are integrated at `7b1d8a6b0` on local `main`;
workspace roadmap changes are locally committed. Neither repository was
pushed by this batch. Concurrent workspace inventory/design/research edits
and the unchanged mobile checkout remain outside this landing.

**Direction review:** keep the architecture and two persistent lanes. CV-2 now
has an evidence-backed Place/Moment boundary; the next work is owner coverage
and one concrete practical adapter at a time. Life's next work is population,
target continuity and viewer parity, then deterministic organization. Do not
treat a served fixture as plentiful, interesting supply;
CV-3 still owns the end-to-end preparation path and activation evidence.
Paid worker activation, new watch/intention/history policy, indexed serving,
native acceptance and release remain separately gated.

### 9.3 CV-2 practical-fact boundary — September 7

The first fixture establishes **omission-policy behavior**: a candidate is
admitted with an accepted `current_conditions_unavailable` omission and
suppressed with an unaccepted `route_unavailable` omission. The latter is a
fabricated test code; the canonical Place reader reports
`reachability_unavailable`. The fixture does not establish an actual route
failure, open/closed feasibility, or retention of the saved door in a composed
response. Preserving independent saved material remains an acceptance
requirement, not an outcome demonstrated by that test's name.

Evidence: `tests/root_projection/test_home_portfolio.py::test_place_reachability_changes_value_judgment_without_erasing_the_saved_door`.
Narrow this test's description and add actual owner-to-consumer cases in CV-2.
The subsequent audit ran 79 focused local tests across canonical reads,
portfolio planning/composition, entity situation, RouteFact and weather-rescue
behavior. Passing those tests did not close the uncovered paths below.

The implementation gap has two sides. The read plan overstates certain fields
and assigns aggregate requirements to unrelated operations. Separately,
common value judgment primarily checks read identity, state, evidence and
accepted omissions; receiving a reference alone does not teach it that a
venue is closed. CV-2 must connect a typed practical observation to the
specific claim it can support or invalidate.

### 9.4 CV-2 detailed execution plan — September 7

#### Outcome and boundaries

The next milestone is **practical context changes the value Vesper delivers**.
Home can give a useful opening into this afternoon, Places can explain and
compare relevant places, and both can qualify what is actually possible.
An original friend note, saved place or historical explanation remains useful
when a visit-now suggestion is unavailable. Life continues to retain and
organize underlying material. These outcomes must not require another input
exercise from the person.

Keep the four moves — Make sense, Open possibility, Help it work, Carry
forward — in one acceptance portfolio throughout execution. Venue status is
the first practical adapter because an existing cache-only owner path already
supplies relevant facts. It is a dependency-sized implementation package;
Vesper's scope still spans everyday, social, practical and continuity value.
Home must retain interesting, substantive value alongside operational help.

Use two persistent lanes. Integration owns this sequence and its Home/Places
consumers; Life continues its existing R2–R5 plan. Dates follow evidence and
dependency completion. This plan does not impose a one-week launch or require
the founder to freeze all product thinking before engineering proceeds.

#### Code baseline and selected seam

| Existing capability | Audited gap | Planning consequence |
| --- | --- | --- |
| [Portfolio planning](../../travel-agent/backend/concierge/agentic_facade/portfolio_reads.py) | Coverage includes Moment conditions although the reader reports them unavailable; aggregate fields are copied to each operation | Repair operation-specific coverage before using it to choose infrastructure |
| [Canonical owner reads](../../travel-agent/backend/concierge/agentic_facade/canonical_owner_reads.py) | Place dependency revisions and evidence later than the represented clock need stronger checks | Make exact dependency and time semantics executable |
| [Places cache](../../travel-agent/backend/places/cache.py) | Cache-only venue batches expose opening/closure facts with separate freshness rules; the DTO drops raw field deadlines and provider identity | Reuse this owner boundary for verifiable field-level facts |
| [Places projection](../../travel-agent/backend/places/projection.py) | Aggregate fresh/stale does not establish each field's validity | Share fact interpretation where appropriate; preserve other callers until explicitly migrated |
| [Value judgment](../../travel-agent/backend/lived_experience/value_composition.py) and [root composition](../../travel-agent/backend/api/services/root_composition.py) | Read validation does not interpret practical payload values; candidate feasibility is supplied separately | Add a narrow deterministic assessment after owner reads and before final judgment |
| [RouteFact](../../travel-agent/backend/core/distance/route_fact.py), movement and [entity situation](../../travel-agent/backend/places/entity_situation.py) | Scoped route capabilities exist; generic canonical `route.evaluate` remains unavailable | Reuse specialist facts through an explicit input contract after the first integration package |
| [Weather provider](../../travel-agent/backend/core/weather_provider.py) | Current observations and forecasts have different provenance/time contracts | Require adequate source/validity metadata for the particular use before generic admission |

Moment `availability` currently describes active Opening context. It does not
establish free calendar time, venue inventory or bookability. Entity catalog
lifecycle status is also distinct from operational opening status. Preserve
these distinctions in coverage reports and visible copy.

#### CV-2A — correct the coverage contract

Owner: Integration. Principal files: `portfolio_reads.py`, its focused tests,
and the semantic catalog only where readiness declarations need correction.

1. Map each visible field to its actual operation or named derived evaluator.
   Preserve collective coverage: a field with no owner remains explicitly
   missing rather than disappearing from the report.
2. Remove unsupported Moment-condition claims. Audit other supported-field
   declarations against returned payloads, including relationship, group and
   source fields. A reference does not establish that the referenced facts
   were read.
3. Distinguish registration, executable reader readiness, field capability,
   request-specific evidence and activation. Continue omitting the known-
   unavailable generic route operation from routine read budgets.
4. Narrow the existing omission-policy regression. Test actual reader output,
   including `False`, `None` and explicit gaps; do not simply repeat the same
   hard-coded capability map in the test.

Exit: every required field has a named obligation or explicit gap. Route is
not responsible for Place identity, and Source inspection is not credited
with unrelated relationship facts. Supported candidates continue to compose.

#### CV-2B — repair revision and temporal admission

Owner: Integration. Principal files: canonical adapters and owner-read/value-
composition tests; shared admission code only where a reproduced failure
requires it.

1. Validate pinned Place dependencies against the current owner revision.
   A changed revision requires current recomposition or explicit mismatch;
   never silently satisfy an old dependency with a different revision.
2. Exclude evidence observed after the represented instant. Distinguish provider
   observation, cache-write and request time. Where an owner lacks historical
   reads, do not imply reconstruction of an earlier snapshot. An absent usable
   timestamp remains an explicit limitation.
3. Test validity again at composition completion. Facts expiring during other
   reads cannot support newly emitted confident claims. Bound a dependent
   result by the expiry of facts it actually uses; unrelated stale optional
   facts must not expire all independent material.
4. Cover changed/deleted/redirected identity, missing timestamps, cross-viewer
   references and partial reads. Preserve audience/use checks and bounded
   optional-read admission.

Exit: the future-observation and pinned-revision regressions fail correctly,
and ordinary current reads remain useful. One represented clock does not
promise a global multi-owner database snapshot.

**Checkpoint 1:** review A/B together with a corrected coverage report and
test receipt. Confirm which remaining gaps are real before adding an adapter.
This is the correctness baseline; the end-user milestone follows in C/D.

#### Early consumer repair — CV-4 receiving support alongside CV-2

The concurrent September 7 [Home receiving correction](home-connected-experience-implementation-map-2026-09-04.md#september-6-portfolio-checkpoint--owner-backed-value-is-connected)
identified an existing exact-destination defect. Reinspection confirms that
[`rootProjectionNavigation.ts`](../../travel-app/utils/rootProjectionNavigation.ts)
supports direct dossier resources, but `places.open_entity` selects only venue,
site, accommodation and experience refs. A dossier-only explanation destination
therefore falls back to the Places root.

Do this bounded mobile packet alongside A/B or C/D when an owner is available;
it does not depend on venue status or justify another persistent lane:

1. Route the supported dossier-bearing destination to the exact reading and
   preserve the existing return context. Define subject precedence when refs
   contain both a Place and a reading; do not choose arbitrarily by list order.
2. Test the actual destination resolver and rendered tap for dossier-only,
   mixed refs, invalid/deleted subject and changed-result return. A valid
   candidate envelope alone is insufficient.
3. Audit addressed-note/source continuity through depth and contextual Ask.
   The root Chat seed helper only covers graph/Trip subjects; separate entity
   Ask paths require inspection before deciding what is missing. Do not expand
   this routing repair into a Chat redesign or claim all contextual Ask is absent.
4. Keep saved Place, retained reading and dated possibility semantics distinct.
   Standalone entity-save representation in Life remains a receiving-owner
   question; report the needed projection instead of adding another save store.

Exit: a surfaced explanation opens that explanation with supported return;
source/Ask/Life gaps are either covered by actual journey tests or named as
dependencies. The broader CV-4 portfolio remains open. The concurrent review's
doc changes retain their ownership; this plan consumes, rather than absorbs,
that work.

#### CV-2C — admit cache-backed venue facts

Owner: Integration; bounded Places-owner support can take the adapter after
A/B's interface is stable. Reuse `backend/places/cache.py` and the Place owner
payload in `backend/core/models/owner_read.py`.

1. Add the smallest typed operational snapshot for `open_now` and
   `permanently_closed`, carrying canonical venue identity, evidence/provider
   identity, source version, observation time and field-specific expiry.
   Preserve durable entity revision separately from transient observation
   identity. Reuse an existing contract if it already preserves these meanings.
2. Evaluate eligibility against the supplied clock. Preserve original
   observation time; cache insertion and root assembly cannot renew evidence.
   Check existing rows' payload versus column timestamps before choosing a
   legacy fallback. Unverifiable provenance cannot support a confident claim.
3. Keep lookup cache-only, bounded and batched, using existing provider policy
   and venue mapping. Define deterministic tie handling and conflicting-source
   behavior. Unresolved disagreement remains unknown.
4. Distinguish miss, negative lookup, unsupported entity type, stale observation
   and explicit closure. Lookup failure never means closed. `open_now` does
   not prove opening at arrival or this weekend; interval reasoning needs
   timezone and schedule semantics before admission.
5. Use the existing Place read boundary for these conditions. Introduce another
   owner family only if a concrete consumer demonstrates the need for an
   independently addressable contract.

Exit: actual cache-to-owner reads supply attributed values and field-specific
gaps, without network access, enqueue, leases or writes during root serving.
Unit cases and a local database reader test cover valid, stale, future, missing
and conflicting rows. This establishes local integration; it does not establish
real-world provider coverage or populated production supply.

#### CV-2D — turn observations into useful output

C and D form one connected delivery package, even if committed separately.
Owner: Integration, including Home/Places consumers.

1. Name the practical question attached to a candidate claim, initially whether
   a venue is open now. Use a narrow typed assessment: supported, unsupported
   or unknown, with reason, evidence and validity. “Open” is not complete
   feasibility; avoid introducing a universal scoring framework.
2. Assess after owner reads and before common judgment. Bind the result to the
   claim it supports. Existing `feasible` or posture flags cannot substitute
   for missing travel time, capacity or opening-at-arrival evidence. Exercise
   all three states rather than treating missing information as `True`.
3. Use existing root anatomy and destinations. Revise or withdraw a dependent
   visit-now offer when closed or unverifiable. Preserve valid browsing,
   explanation, the independent saved door and original attributed messages.
   Permanent closure may affect current visit suggestions more broadly while
   the historical record and social source remain independently useful.
4. Home emphasizes the temporal consequence; Places supports exploration and
   detail. Avoid duplicating all status information or rewriting a friend's
   note as generated copy. Suggest an alternative only when its own facts
   support it.
5. Exercise Home and both Places v2 callers through production composition.
   Assert actual content/claims and preserved owner destinations, not just an
   intermediate candidate or accepted omission code.

| Evidence/event | Dependent practical output | Independent value |
| --- | --- | --- |
| Fresh `open_now=True` | May support “open now”; no implied arrival, capacity or route guarantee | Existing exploration and source remain |
| Fresh `open_now=False` | Revise/withdraw immediate-open claim; no invented reopening time | Saved place, history, explanation and friend note remain reachable |
| Missing/stale/future/conflicting status | No confident opening claim; a worthwhile exploration can remain with the relevant limitation | No demand to re-document the place to rescue the feed |
| Fact expires during assembly or source changes | Reassess/remove the dependent assertion, preserving exact current refs | Unrelated valid material survives |
| Friend note withdrawn | Remove that note and results whose use depends on it | Independent public facts and viewer-owned material retain their own eligibility |

**Checkpoint 2:** compare composed portfolios across ordinary NYC, emerging
weekend, trip disruption, post-return curiosity and addressed social material.
Review useful substance, low input burden, exact continuation and bounded cost
together. A page containing only warnings does not pass. Use local tests for
this checkpoint; native acceptance remains separately recorded and deferred.
C/D closes when actual facts change the appropriate output and the independent
material demonstrably survives in the response.

#### CV-2E — extend through existing practical specialists

After checkpoint 2, route/movement evidence is the next candidate when the
portfolio contains a concrete timing question. Reuse RouteFact and routing
policy. Specify destination, authorized origin, origin quality/age, mode,
departure/arrival time, intended use, provider policy, observation identity
and expiry. Origin remains request/session scoped; a previous route is not
permission for background location.

Entity situation, movement and leave-by demonstrate scoped capabilities. Root
composition should not call an object-page HTTP endpoint or start a provider
lookup to imitate them. Identify an authorized owner already supplying an
eligible observation. If absent, name the missing input/refresh contract first.
Keep canonical `route.evaluate` unavailable until that contract and adapter
work. Radius fallback cannot certify route feasibility; current weather cannot
certify a forecast.

Use deterministic local observations to test stale origin, future observation,
expiry, degradation, policy mismatch and unavailable routes. Add weather or
future-hours reasoning when a named result needs it and its fact contract is
adequate. This sequence does not authorize a provider, durable watch or scheduler.

#### Following milestones: supply, continuity and contraction

| Stage | Work/dependency | Exit evidence |
| --- | --- | --- |
| **CV-3 supply completion** | Trace existing accepted trigger → work item → bounded executor → stored result → current-use validation → CV-1 consumer for explanation, possibility and addressed contribution | Local end-to-end reuse, failure, cancellation, revocation, late completion and useful fallback; distinguish actual supply from empty supported renderers. Paid activation follows the accepted worker decision. |
| **Parallel Life R2 → R2-G → R3–R5** | Owner/target coverage and reconciliation, then deterministic organization and exact readers/custody; Integration consumes ref, revision, restore/withdrawal and target-capability contracts | Population, delta continuity, viewer parity and withdrawal evidence before indexed serving. Future-target shadow builds are not live delivery. This work need not wait for venue status. |
| **CV-4 consumer completion** | Exact Home/Places → source/entity/arrangement → Life destinations, return and changed-source repair; bounded Capture/Entity/Plan help for named receiving failures | Varied connected value, social attribution and private/public separation survive correction and return without duplicate objects or forced inputs |
| **Replacement-bound contraction** | Remove superseded readers/screens in caller-inventoried batches; retain booking evidence/external continuation and deterministic expense correctness | Working replacement destination, remaining-obligation inventory, deletion tests and local regressions before removal |

Inspect the full portfolio, remaining user work, duplicate ownership, source
availability, latency and cost at each checkpoint. Reorder when evidence shows
a different binding constraint. Supply-path inspection can proceed alongside
CV-2; shared composition changes land serially. Consumer quality and supply
must not wait indefinitely for “all infrastructure” to finish.

#### Execution and verification

- First batch: A and B as separate reviewable commits, then checkpoint 1.
  Second batch: C and D with an integrated receipt, then checkpoint 2.
  The independent early CV-4 destination packet may land alongside either.
  Later batches follow the dependencies above. Each receipt names repo SHAs,
  changed contracts, tests and remaining gaps. This refresh implements none
  of these planned packages.
- Keep Integration and Life persistent. Bounded cache-adapter work or an
  exact-destination repair or regression audit can run in parallel once
  interfaces/files are fixed. Integration owns landing shared owner-read, judgment, composition and
  generated-contract changes. This plan does not start additional tasks.
- Run affected portfolio, canonical-read, value-composition, Places cache/
  projection and Home/Places API tests. Add local database tests for the cache
  join, no-provider/no-write assertions, optional-read saturation and
  completion-time expiry. Record actual counts and baseline failures; earlier
  receipts do not replace rerunning affected suites.
- Classify typed-boundary changes through backend task intake. API model/route
  changes require workspace `scripts/sync-types.sh`, review of both OpenAPI
  snapshots and generated mobile types, then typecheck and focused renderer/
  navigation tests. Internal adapters alone do not justify new mobile kinds.
- Check branch/status before touching each repo and stage explicit owned files.
  Preserve concurrent Life/design/strategy work and attach dependent repo SHAs
  to cross-repo receipts.
- Reassess before a second owner/store, new write authority, undocumented
  history/watch semantics, provider execution, unbounded root work, or an
  inability to preserve independent material. Report the concrete conflict;
  unrelated accepted work can continue.

Recommended defaults are cache-backed venue facts first, claim-specific
consequences, specialist-owner reuse and existing root forms. Loose intention,
optional history, watches and activation retain their separate decisions;
they do not block the accepted read/judgment work.

### 9.5 Receiving and execution rebaseline — September 7

The founder accepted the Integration task's next-step recommendation after
reviewing Strategy, Content and Life. Execute the following packages within
CV-2–CV-4; do not introduce another roadmap or universal owner.

1. **Practical delivery repair — locally implemented.** Backend `ea816526d`
   closes exact audience/revision/time admission, bounded optional cache
   behavior, dependent expiry through the delivered unit, and the reviewed
   open-now alternative producer. Mobile main `9326c34a4` observes that deadline.
   Connected Home and both Places response tests preserve independent
   explanation/exploration. This is not certification of all human-material
   paths, provider coverage or native behavior; see the receipt below.
2. **CV-3 supply and CV-4 continuation can overlap.** Trace supported triggers
   through existing preparation, durable readback and ordinary root serving.
   Private prepared Source output (currently at most one per read) does not
   establish public world supply. Consume Content's supplier findings; no
   dossier requirement for every discovery and no AI-enrichment requirement
   for original social material. Keep misses useful without work on GET.
3. **Complete exact continuation.** Mobile `c8d88437f` fixes dossier destination
   routing. Mobile main `8860a34bd` adds existing place/reading-specific seed
   kinds to root contextual Ask. Remaining packages inspect
   addressed-source continuity through depth, and owner-backed save-to-Life
   mapping. Keep Place bookmark, retained reading and dated intention distinct.
   Life owns its projection; Integration does not add another bookmark owner.
4. **Then extend practical adaptation.** Consume existing route/movement facts
   for a named timing question. Changed facts must lead to useful revision,
   qualification, alternatives or release, rather than only invalidation.
   Watches and external execution retain their existing decision boundaries.

Review after the repair and after each two connected packages: sparse-context
Home, an ordinary question, original friend material, a practical change and
return after absence. Check delivered substance, work removed, exact continuation,
changed-source repair and combined cost/latency. These are independent encounters,
not a required tab journey or a one-loop product definition. Native testing
remains deferred by the founder; record local evidence separately.

Life continues its roadmap §11 corpus, lens, reconciliation and race packet in
its isolated worktree. Optional conversational continuity remains a concrete
upcoming decision: define receiving/dependency repair now, but the proposed
90-day ceiling is not adopted retention policy. Social can advance casual
sharing without waiting for the pre-Plan owner decision.

Historical receipts below describe the earlier implementation, not completion
of this receiving pass. In particular, ordinary Place cards no longer universally
assert an open-now question, and the earlier missing-`openai` test blocker was
an interpreter mismatch: use the backend `.venv/bin/python` for verification.

#### Receiving checkpoint: practical delivery and contextual Ask

- Backend `ea816526d`: **574 affected tests passed**, including **21 connected
  cases** over Home composition, Places root and Places runtime assembly.
  Open, closed, missing, stale, permanent-closure, future-observation and
  completion-time expiry cases use synthetic catalog/cache boundaries and
  real adapters, canonical Place reads and common judgment. Independent
  reading and ordinary Place exploration survive an unsupported claim.
  A **78-test** reader/delivery rerun passed after cleanup.
- Opening claims are alternatives to the same ordinary Place candidate, not
  a blanket feasibility gate. Both compete for the same seat. The assessment's
  evidence and shortest used deadline survive composition, delivery binding
  and the generated API contract. A second clock check handles expiry while
  delivery-history lookup runs.
- Cache work uses the existing physically bounded optional Places executor
  concurrently with identity lookup. Slow, saturated and failed optional reads
  preserve identity. Lookup is still per venue: portfolio-wide batching and
  real-database conflict handling are not certified by this packet.
- Mobile expiry/navigation/root-rendering checks: **39 tests passed** before
  the continuation packet; routing/seed/create-intent then passed **42 tests**.
  Typecheck passed after both changes; lint passed with 176 existing warnings.
  Existing backend seed-resolution tests passed **43 tests**. These counts
  overlap; do not sum them as distinct cases.
- Mobile main `9326c34a4` observes value expiry. Main `8860a34bd` reuses
  venue/site/accommodation/experience/dossier seeds at root contextual Ask,
  prioritizes the exact dossier over an incidental venue, retains return,
  and uses the existing new-private-conversation path. It adds no prompt or
  retention rule. Equivalent commits `c2d2b16e0` / `6296287ef` also remain on
  the concurrent entity branch; its unrelated changes were not merged.
- Mobile still uses its existing whole-root expiry fallback and refresh,
  not per-unit stable replacement. Selected-text, prior-session,
  source-revision and addressed-note continuity are not certified here.
  No native, live-provider, populated-corpus or activation claim is made.
- Backend commit hooks passed except existing size-budget violations in
  unchanged files; only that hook was skipped. Workspace link checking still
  reports the pre-existing `state` link in
  `claude-design-interaction-kernel-lab-v2-3-arrangements-execution-report-2026-09-04.md:53`.

#### CV-3 supply audit: what exists versus what can run

| Boundary inspected | Current evidence | Next scoped work / gate |
| --- | --- | --- |
| Explicit investigation | Existing Chat/action tools can perform bounded lookup, and the web/Places adapters are metered and guarded; the complete candidate→judgment→root receipt is not yet a single tested path | Name the receiving command and exercise a user-requested place/topic/time case. Keep acquisition request-scoped; do not make its result a watch or durable fact by default. |
| Public/world preparation | Content has supplied provider/code/rights/economics findings; no activated public preparation job or reusable admitted world pool exists | Define a narrow supported market/topic/window and an admission/refresh contract. Use recorded fixtures first; provider account and retention approval remain gates. |
| Private trigger identity | `build_source_contribution_work_item` supports authorized signal, explicit warm and source recomposition; no runtime caller found under `backend/` | Bind an explicit request first. A signal or source-owner repair event needs a separately implemented authority, deduplication, cancellation and expiry contract. Never substitute focus/GET for the missing event. |
| Durable handoff | `create_source_contribution_workflow` reuses `agent_workflows`; no runtime caller found | Connect only the selected private trigger to its durable outbox/workflow handoff and exercise replay locally. An enum/workflow alone is not populated supply. |
| Execution/readback | Dark worker, bounded canonical executor, Places context resolver and default producer factory exist with local tests | Verify private trigger→executor→durable readback with deterministic production first. Approved provider/cohort and cost evidence remain activation gates. |
| Scheduling | No Source-contribution registration found under `backend/workers` | Remain dark under the accepted worker decision. No new scheduler, deployment or provider calls are authorized by this audit. |
| Root consumption | Prepared-source reader checks current use and private audience; at most one eligible prepared production per root read | Preserve ordinary material on a miss. Private retained production does not establish public world coverage or require dossiers for all discovery. |
| Common receiving boundary | Root composition, value admission, claim-specific practical assessment and exact mobile continuation exist in pieces; no cross-mode receipt covers all three paths | Add the CV-3 portfolio fixture and verify the same evidence/rights/freshness/cost fields survive into Home and Places with distinct expressions. |

Next checkpoint is a **supply-to-value portfolio receipt**, not another generic
worker-infrastructure packet. It should cover one explicit investigation, one
bounded public/world preparation case and one explicit private preparation case
through evidence, judgment, Home/Places delivery and exact continuation. Pair it
with the addressed-source depth/Ask audit and receive Life's
bookmark/retained-reading projection contract without building a second save
owner. Withdrawal, current-use repair, claim expiry and cancellation must hold
through production and continuation. Provider activation, optional continuity
and watches remain separate decisions. CV-3 and the broader CV-4 remain open.

#### Trigger-owner follow-up — scope repair before activation

Reinspection found that naming an event was not enough to connect safe supply.
`SourceOwnerChangeEventV1.scope.purpose` currently permits `source_refind` or
`projection_repair`; it does not authorize a new generation job. Its opaque
Intake references are also not automatically the exact Source opportunities
accepted by the producer. Existing deletion/candidate-retraction paths already
invalidate dependent production through `invalidate_source_contributions_for_source`.
Do not duplicate that owner or turn the repair event into a new warm request.

The canonical executor previously ignored work-item root scope, accepted an
unowned workflow, and could continue automatic discovery after a requested
Places context resolved to nothing. Backend `778494b62` corrects those prerequisites:

- only explicit-warm items are supported by this executor until another
  trigger has an implemented owner binding;
- actor/key/unsupported-trigger failures are terminal contract failures, not
  retryable provider failures;
- an explicit Places context must resolve to the requested handle; blocking
  resolution runs off the event loop so cancellation remains responsive;
- root scope reaches continuity selection and new generation, without changing
  the Sources' permissions or the root-neutral group identity;
- wider cached output does not substitute for a narrower job or falsely count
  as reuse. A scoped result remains readable by its matching root and cannot
  appear on an excluded root.

Local verification: **426 tests passed** across `tests/root_projection` and
the root API/composition/practical-delivery suites. New connected cases cover
Home-only and Places-only generation→readback→serving, plus missing/changed
context, cancellation, missing actor and unsupported signal rejection. Imports,
lazy-import inventory and changed-file lint passed. Tests use synthetic owner
and persistence boundaries; there is no PostgreSQL, paid-provider or native
receipt. API schemas, prompts and mobile surfaces are unchanged. Backend commit
hooks passed except the same existing size-budget violations in unchanged
files; that hook alone was skipped. Workspace links still report the existing
`state` target in the September 4 arrangements execution report.

**Recommended next trigger, pending founder interface approval:** an explicit
private preparation request in the existing conversation/action workflow,
such as preparing options for a named Place/time window. This is not a proposed
new Home input card or a requirement to prepare before browsing. Bind the
authenticated request identity, exact supported context, requested roots,
current-use authority and finite deadline to the existing work item; store
only its content-free handoff in the existing workflow. Preserve a useful
immediate answer and report completion/failure where the person requested work.
Source correction during the job must invalidate/recheck its dependencies,
not renew its deadline or create a recurring mandate.

Before wiring a runtime caller, settle the existing command/handler that owns
this explicit request and its cancellation/expiry receipt. Adding a new tool,
prompt or API contract requires its normal approval; no such change is implied
by the trigger enum. Then test durable retry/deduplication and execution through
canonical readback. Controlled provider measurement and Arq activation remain
later gates. Intake-to-generation, generic background ticks and production on
GET remain excluded. This packet closes execution-scope holes, **not CV-3's
runtime supply connection**; the prior “named trigger-owner” next step was too
optimistic without this distinction.

### Execution receipts (2026-09-07)

- **CV-2A / operation-specific field coverage — implemented:** backend commit
  `153cf746b` gives each semantic operation its own requested-field set instead
  of copying a requirement's aggregate fields to every operation. The Moment
  reader no longer claims current conditions. The focused portfolio suite
  passes **17 tests**, including a collective-coverage regression. Readiness,
  field capability, evidence and activation remain separate axes.
- **CV-2B / Place revision and represented-clock admission — implemented:**
  backend commit `c15068fcb` rejects stale pinned Place/transport-hub/entity
  revisions and owner rows updated after the requested represented instant.
  Focused canonical-owner collection remains environment-blocked in this
  checkout because the `openai` package is unavailable; the changed modules
  pass `compileall` and lint. The new regressions are committed but require the
  normal dependency-complete run before they are a green runtime receipt.
- **CV-2C / cache-backed venue facts — implemented:** backend commit
  `21f2e3085` preserves provider/place identity, provider observation time and
  field expiry metadata in the existing cache reader, adds a synchronous
  cache-only bridge for the canonical Place adapter, and exposes a typed
  `PlaceOperationalFact`. Cache failure, missing provenance and future
  observations remain unknown; no provider call, write or new owner is added
  to root serving. Commit `3f7e25da6` also treats malformed or timezone-less
  legacy observation timestamps as unknown instead of failing the owner read.
  Existing Places projection/actionability tests pass (**41**).
- **CV-2D / claim-specific practical assessment — implemented:** backend
  commit `07baa364c` adds an opt-in `place.open_now` assessment after owner
  reads and before common value admission. Fresh true evidence is supported,
  fresh false or permanent closure suppresses the dependent candidate, and
  missing/stale evidence is unknown while independent candidates remain
  eligible. The focused value-composition suite passes **13 tests**. Backend
  commits `46652e1d5` and `140d46a2b` then opt the existing Home Place adapter
  into the question for actual Place candidates and match canonical refs by
  stable identity. Existing explanation and social producers do not claim this
  question until their visible copy is ready.
- **CV-4 / exact editorial destination — implemented:** mobile commit
  `c8d88437f` makes a `places.open_entity` destination prefer its exact dossier
  subject (including when a context ref is also present), preserving the root
  return token. The focused navigation suite passes **15 tests** and app
  typecheck passes.

These receipts establish local implementation and focused contracts, not live
provider coverage, populated supply, native visual acceptance or production
activation. The later receiving checkpoint in §9.5 supersedes the earlier
canonical-owner test blocker and blanket Home Place opt-in described here.
Next comes the named supply handoff and remaining exact continuations before
broadening route/movement coverage. Life remains independent.

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
- **I1 / Life downstream delivery bridge — implemented and locally tested:**
  `travel-agent` adds an after-commit registration helper, an
  identifier/revision-only `life_projection.changed` publisher, and a minute
  repair worker over the existing Life outbox. Thirteen focused tests cover
  payload redaction, commit handoff, consumer failure/defer behavior, retry
  repair, and worker registration. This closes the outbox-to-event seam only;
  no owner producer, current-authority projector, index population, Home/Places
  consumer, or serving cutover is claimed.
- **I1 / retained-source shadow projection — implemented and locally tested:**
  `travel-agent` commit `77d4a8474` connects retained-source verification,
  provider-archive attachment, and owner deletion to the Life outbox. A
  current-authority reader and owner-revision-checked projector write or
  withdraw private `life.v1` shadow rows without changing serving. The focused
  Life/intake suite passes 114 tests; semantic candidate representation,
  broader owner families, and indexed cutover remain open.
- **I1 / retained-source semantic representation — implemented and locally
  tested:** `travel-agent` commit `073d33b9d` connects Experience Graph anchor
  confirmation and candidate retraction to the same owner transaction. A
  confirmed candidate emits `source_represented`; a retracted candidate emits
  `source_unrepresented`; the current-authority retained-source projector then
  withdraws or restores the private `life.v1` shadow row by owner revision.
  Follow-up commit `420176821` makes the projector honor those change kinds
  explicitly, with stale-event protection and an explicit restore path. The
  focused projector/bridge suite passes 24 tests; after applying the existing
  `lifeoutbox01` migration locally, the PostgreSQL bridge/intake suite passes
  17 tests. No fallback or serving cutover was added.
- **I1 / source-owner lifecycle envelope — implemented and locally tested:**
  `travel-agent` commit `a669541b2` adds the versioned, content-free
  `source-owner-change.v1` payload, lifecycle vocabulary, retry identity,
  owner revision and source/candidate references to Intake lifecycle events.
  It preserves legacy top-level outbox fields while making downstream Life,
  Home, Places and graph consumers explicit. The combined focused suite passes
  42 tests; this remains a delivery contract, not a serving or activation
  change.
- **I1 / Occasion audience contract — implemented and locally tested:**
  `travel-agent` commit `6d4365a83` adds deterministic hashing of the
  canonical Occasion revision plus active-member role/visibility revisions,
  and a before/after viewer union that includes departed viewers for
  withdrawal. Five pure contract tests pass. No Occasion producer, reader,
  projector, or owner-matrix promotion is claimed yet.
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
  The corresponding mobile root-consequence and Places state suites pass **35
  tests**, covering account-bound grants, verified readback/repair messaging,
  and cross-root invalidation without changing Chat or Life internals.
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

- **I4 / real Home→Places runtime boundary (2026-09-06):** the existing
  real-Postgres Save-owner integration now also reaches the governed
  `/api/root-projections/v2/places/runtime` envelope alongside the Places owner
  reader and Home v2 projection. The test asserts the `places-root-runtime.v1`
  wrapper, nested v2 semantic identity, and workspace-feed join; it passes **1
  real-Postgres test**. The fixture's Save is proven independently through the
  canonical Places owner and Home unit. **Corrected on the September 6
  orchestration review:** the test does not assert card presence in the runtime,
  and its default scope does not select the Saved collection. The earlier
  attribution to semantic admission was unsupported; no new promotion rule
  follows from this probe. Focus/Path recomposition, personalized
  freshness vectors, and native/device acceptance remain unclaimed.

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

### M1 follow-up review — 2026-09-06, corrected baseline

- **Evidence:** the real-Postgres test proves Save-owner readback, the concrete
  Home unit, and the Places runtime envelope. It does not prove saved-card
  rendering in the governed runtime. `places/sections.py::_load_saved_items`
  selects saved/trip/city/area scopes; the fixture never selects one. Its
  absence therefore did not establish a semantic-admission defect.
- **Next evidence:** use an explicit supported scope, trace producer output
  before admission and assert the represented saved identity and return after
  a change. Keep the result distinct from field/map/search/depth acceptance.
- **Product/architecture:** do not invent a producer, client merge or generic
  semantic kind to satisfy an incorrectly scoped test. Also do not close I4
  with a non-promotion rationale derived from that test. Existing owner and
  renderer boundaries remain; change them only on actual value/coverage evidence.
- **Next execution:** follow §2 and §9 rather than repeating receipt-only runs.
  The Source worker is implemented but inactive; live judgment and authorized
  watches remain separate responsibilities. Current work needs no app/device
  session, queue activation, production migration or Chat redesign.

### CC-2/CC-5 Contribution/Capture receipt — 2026-09-06

The Contribution and Capture lane delivered backend commits `a669541b2`,
`fce385207`, and `780677110` on `codex/contribution-capture-cc2-cc5`. This is an accepted-contract repair, not
an adoption of either September 6 decision proposal.

- **Lifecycle/read boundary:** semantic admission, semantic completion, and
  normalization now refuse late work after transient source expiry. Expiry
  sweeps pending/uploaded/verified/deletion-pending custody, scrubs only the
  selected source IDs, and dead-letters unfinished work before cleanup.
  Semantic loading, anchor image reads, and pending-Chat source/image/text
  reads fail closed on expired/revoked custody.
- **Source-owner handoff:** Intake and the existing Life outbox now carry a
  content-free `source-owner-change.v1` envelope with stable event/retry
  identity, owner revision, private scope and purpose, source/causal refs,
  affected consumers, and owner-partition ordering. The Life delivery bridge
  validates and forwards this metadata only; Capture does not write Life rows.
- **Causal repair:** verified/normalized/represented/unrepresented,
  candidate-confirmed/retracted, deleted, and expired transitions preserve
  distinct event keys; representation handoffs carry the candidate that
  caused them as an opaque causal dependency. No source-ID-only dedupe or
  synthetic owner was added.

Evidence: **61 offline** lifecycle/handoff tests, a further **17 offline**
pending-Chat read tests, and **9 PostgreSQL** focused tests passed, together
with Ruff, compile, and diff checks. The broad-exception and backend size
budget hooks remain over their pre-existing baselines and were explicitly
skipped for this commit. The receiving interface is
`backend/core/models/source_owner_event.py`; Life remains responsible for its
projector/index and exact current-authority readback.

Remaining CC work is intentionally unchanged: founder selection of the
ordinary-Chat versus Ask-image history rule and any historical cleanup; the
remaining CC-3 writer family; CC-4's full useful-first result composition;
approved intention/social/expense owner commands; and CC-6 real transport,
native, and generated-content evidence. Next package: finish the new-source
copy/consumer expiry cases and exercise the source envelope through Life
readback/correction without inventing a new owner or enabling either proposal.

### CC-2/CC-5 follow-up receipt — custody-proof reads and aligned delivery — 2026-09-06

The next focused package keeps the accepted source lifecycle fail-closed at
the read and delivery boundaries. Canonical pending-Chat source/image/text
reads, retained-source Life reads, and confirmed-anchor source status now
require the existing owner-bound custody receipt in addition to custody status
and transient-deadline predicates. Normalization and semantic workers reject
invalid source receipts before prompting or producing derivatives; URL and
transcript materializers re-check the locked parent receipt before binding a
new child. This does not change the unadopted ordinary-Chat history rule and
does not add a new copy or cleanup policy.

The Life delivery bridge now cross-checks a nested `source-owner-change.v1`
envelope against its legacy outbox fields (event key, owner id, owner revision,
lifecycle, and viewer scope) before forwarding it. A mismatched or malformed
content-free handoff is rejected rather than acknowledged; source bytes and
prose remain excluded. Life still owns its projector/index and exact readback.

Evidence: **95 offline** focused lifecycle/read/handoff tests and **9
PostgreSQL** retention/attempt tests passed, with Ruff, compile, and diff
checks clean. The package is committed on
`codex/contribution-capture-cc2-cc5` as the next bounded source-read/delivery
change (`travel-agent` commit `0aeb8611b`). No API schema, mobile code,
Chat root, Life rows, or proposal policy changed. The next package remains the
accepted new-source copy/consumer expiry evidence and Life readback/correction
journey; history-specific Chat-image treatment, intention/social/expense
commands, and native/real-transport evidence remain separately gated.

### CC-3 writer-conformance receipt — itinerary edit signals — 2026-09-06

The accepted itinerary-edit writer now marks its factual swap/add/remove
observations as reversible operational evidence: explicit
`evidence_origin=operational_event`, `promotion_policy=derived_unconfirmed`,
`authority=non_authoritative`, bounded confidence/importance, a 90-day expiry,
and a source-operation subject key. Legacy edit-log and canonical committed
Replace paths share the same policy while retaining their distinct source
receipts and exact transition lineage. No Personal Memory prompt, authored
preference, or group writer was changed.

Evidence: `travel-agent` commit `fe87dc34f`; the focused edit-inference suite
passes **23 offline tests**. Remaining writer families (Discover synthesis,
engagement/reflection, accommodation/planning, and group synthesis) stay on
their existing bounded paths and require their own owner/policy evidence; no
universal memory audit was reopened.

### CC-2/CC-5 follow-up receipt — owner readback redaction during cleanup lag — 2026-09-06

The canonical `GET /intake/submissions/{id}` owner read now redacts
`storage_ref`, `original_filename`, and raw `metadata` whenever a source is
past its transient deadline, revoked, deleted, or fails its owner-bound custody
receipt. It still returns content-free lifecycle metadata, so the receipt is
accurate while cleanup is pending and cannot leak a stale byte address or
inline source payload. This is a source-side read boundary only: it changes no
retention policy, Chat history rule, Life row, API schema, or mobile surface.

Evidence: `travel-agent` commit `444f2dfe9`; the PostgreSQL-gated negative case
is in `tests/inbound/test_intake_v2_retention.py`. The focused lifecycle/
handoff portfolio remains **95 offline tests** and the retention/attempt
portfolio remains **9 PostgreSQL tests**, with Ruff, compile, format, and diff
checks clean. The pre-existing broad-exception and size-budget baselines remain
outside this bounded package and were skipped only for commit validation.

The accepted cleanup-lag read seam is now closed. Next package: source/
derivative copy-consumer expiry evidence and the source envelope through Life
readback/correction; history-specific Chat-image treatment, remaining writer
families, useful-first composition, intention/social/expense commands, and
native/real-transport evidence remain separately gated.

### CC-3 follow-up receipt — Atlas reflection writer conformance — 2026-09-06

The Atlas-derived-signal reflection writer now emits explicit operational,
non-authoritative provenance, a signal-confidence mapping, a 90-day expiry, and
`subject_key=atlas_signal:{signal_id}`. A retry therefore reinforces the same
derived signal, while separate signal IDs and later gestures remain distinct.
Existing learning gates, signal pause, and Atlas back-link behavior are
unchanged; this does not promote generated taste or alter Personal Memory
prompts.

Evidence: `travel-agent` commit `79702ee87`; **31 offline** Atlas/reflection
tests passed, with Ruff, format, compile, and the owned-file safety hooks
clean. The repository's vulture, sync-DB, surface-key, broad-exception, and
size-budget hooks were skipped for this bounded commit due pre-existing
ratchet/stash behavior; the sync-DB and surface-key scans reported no new
violations. Discover, memory-engagement, accommodation/planning, and group
synthesis writers remain separately gated.

### CC-2/CC-5 follow-up receipt — submission-level Chat source admission — 2026-09-06

`validate_admitted_source_refs` now treats an `intake_submission` reference as
usable only when its owner-scoped submission envelope is active **and** at
least one verified child source object still passes the immutable custody
receipt. A stale/tampered submission row therefore cannot pass admission and
reach the Chat prompt while its materializer has no safe evidence. Direct
`intake_source_object` references keep their existing object-level receipt
check; separate gestures remain separate identities.

Evidence: `travel-agent` commit `a7cbec6cf`; **19 offline** pending-Chat tests
pass, including the all-child-receipts-invalid negative case. The connected
focused lifecycle/read/handoff portfolio is **108 offline tests**; Ruff,
format, compile, and diff checks are clean. No API/schema, Chat-root, Life
projector, retention-policy, or history-migration change was made. The
pre-existing vulture, sync-DB, surface-key, broad-exception, and size-budget
ratchets were skipped only for commit validation; the skipped checks reported
no new sync-DB or surface-key findings.

This closes the remaining accepted submission-level prompt/read rejection
seam. Life still receives only the content-free source-owner event and owns
its index/readback; Home/Places remain downstream consumers of canonical owner
revisions. Next package: source/derivative copy-consumer expiry evidence that
does not depend on the unadopted Chat-history proposal, then a joint Life
readback/correction rehearsal. History-specific image treatment, remaining
writer families, useful-first composition, intention/social/expense commands,
and native/real-transport evidence remain separately gated.

### CC-5 follow-up receipt — Life handoff causality evidence — 2026-09-06

The existing source→Life registration path now has an explicit conformance
case for a representation withdrawal. The test asserts that the outbox
payload retains the `source-owner-change.v1` lifecycle, event/retry identity,
owner revision, private viewer scope, and the candidate that caused the
withdrawal as an opaque causal dependency. It exercises the source-side
handoff only; Capture does not write Life rows and no new projector or owner
command was introduced.

Evidence: `travel-agent` commit `9802c047c`; **7 offline** source-owner
propagation/envelope tests pass. No API/schema or mobile change was made. The
next package remains source/derivative copy-consumer expiry evidence that is
independent of the unadopted Chat-history proposal, then a joint Life
readback/correction rehearsal when the receiving lane is ready.

### CC-2/CC-5 follow-up receipt — whole-submission admission positive control — 2026-09-06

Pending-Chat admission now has paired conformance evidence: a whole-submission
source ref fails closed when every child source receipt is invalid, while the
same path remains accepted when one owner-scoped child is verified and its
immutable custody receipt matches. This is a regression guard for the accepted
source/ref boundary, not a new source store or dedupe rule.

Evidence: `travel-agent` commit `e33268064`; **20 offline** pending-Chat tests
pass. No API/schema, Chat-root, Life projector/index, retention/history policy,
or owner command changed. The remaining accepted lane work is source/derivative
copy-consumer expiry evidence independent of the unadopted Chat-history
proposal, then a joint Life readback/correction rehearsal when the receiving
lane is ready; native, real-transport, and content-usefulness evidence remain
separate CC-6 gates.

### CC-4 follow-up receipt — useful-first capture display evidence — 2026-09-06

The Share Capture surface has direct regression coverage for the accepted
value-first ordering: source-extracted observations render as “Already useful”
before the candidate “Keep this interpretation” control. The test preserves
the existing compact receipt and optional Chat continuation; it adds no result
schema, Chat-root behavior, or mandatory review step.

Evidence: `travel-app` commit `d7d1a3271`; **11 offline Jest** tests pass for the
Share Capture screen. This is native-adjacent evidence, not OS/real-transport
or generated-content acceptance. The remaining CC-4 journey and CC-6 content,
native, and transport evidence stay separate; source/derivative expiry and
Life readback/correction remain the next accepted cross-root checks.

### CC-2 follow-up receipt — processing-copy expiry evidence — 2026-09-06

The expiry path now has PostgreSQL coverage for both normalization and semantic
processing copies. Crossing an ephemeral source deadline clears each selected
run's content-bearing `output`, while content-free lifecycle/provenance fields
remain available and unfinished work is dead-lettered before cleanup. This is
independent of the unadopted Chat-history/image policy and does not purge
conversation history or Life-owned derived records.

Evidence: `travel-agent` commit `49ec11e21`; the targeted case passes and the
connected retention/attempt portfolio remains **9 PostgreSQL tests**. No
API/schema, mobile, Chat-root, Life projector/index, or owner command changed.
The remaining history-specific image treatment is decision-blocked; native,
real-transport, and generated-content acceptance remain separate CC-6 gates.

### Contribution/Capture current boundary — September 6

The accepted source-side boundary is now locally evidenced for custody-proof
reads and prompt admission, distinct retry identity, transient expiry and
processing-copy cleanup, content-free source-owner events, causal Life handoff
metadata, and useful-first Share Capture ordering. Capture still owns source
emission; Life owns its projector/index and canonical readback. No Source is
promoted here to intention, social membership, expense debt, or a synthetic
Plan.

The next connected action is the receiving-lane Life readback/correction
rehearsal over the existing envelope. Ordinary-Chat versus Ask-image history
semantics remain proposal-gated; remaining CC-3 writers require family-specific
authority receipts; full CC-4 journeys require real content/native evidence;
and CC-5 intention/social/expense commands require their existing owner
decisions. The September 6 decision documents remain proposals and are not
runtime dependencies for this source boundary.

### I3 / CC-3 follow-up receipt — Discover writer conformance — September 6

The Discover-session synthesis writer now makes its already-derived behavior
explicitly bounded: emitted observations carry fixed 0.4 confidence, a
90-day expiry, capped importance, inferred/non-authoritative provenance, and a
hashed subject key only when one source session owns the synthesis. Multiple
model outputs remain distinct by category/ordinal; mixed or missing session
identity receives no invented key. This preserves separate behavioral windows
and keeps explicit confirmation as the promotion boundary.

Evidence: `travel-agent` commit `8b6bab422`; 16 focused Discover tests and 56
combined Discover/edit-inference/Atlas/engagement tests pass, with Ruff,
format, compile, and owned-file safety checks clean. The change is writer-local:
no Chat redesign, source-custody/history policy, Life row, owner command, or
Personal Memory promotion was introduced. The remaining CC-3 families and the
CC-5 Life readback/correction rehearsal stay in their existing gates.

### I1 / Life owner-private Plan shadow delivery — September 6

The next Life owner family is now wired without broadening product grammar:
canonical Plan create, owner update, and lifecycle transitions enqueue
owner-private Life events; the Plan projector re-reads the viewer's current
graph projection and writes the existing shadow index with integer revision
CAS, withdrawal, stale replay protection, and explicit restoration. The owner
matrix now declares Plan delta delivery and audience rechecks while retaining
`SHADOW_ONLY` availability.

Evidence: `travel-agent` commits `7b6e97d7f` and `f12dca534`; the combined
focused Life/Plan/Occasion suite passes **60 tests**. The package does not add
loose intention, shared arrangement material, a Plan-specific queue, serving
cutover, or Outcome delivery. Outcome remains gated on an explicit shared
audience/revocation contract.

### CC-2/CC-4 follow-up receipt — derivative expiry and receiver evidence — September 6

The Capture lane now closes the accepted derivative-consumer expiry seam:
URL retrieval and audio transcription re-check verified custody and the
transient source deadline before reading source bytes or binding a child
source, including the already-existing URL-child retry path. Explicit
`source_and_derived` retention remains durable; invalid custody and malformed
clocks fail closed.

Evidence: `travel-agent` commits `70762af24` and `7966cdb9f`; 15 focused offline tests passed,
with Ruff, compile, and diff checks clean. The current Share Capture, audio,
and resumability paths were rerun by explicit test path with 23 mobile tests
passing. This is native-adjacent regression evidence, not real OS transport,
device, or generated-content acceptance.

The initial parallel Life receiver (`codex/life-owner-delivery`, commit
`b4d87161f`) is retained as provenance for the shadow delivery shape; it is
superseded by the landed shared-backend receiver and repair commits recorded
in the CC-5 receipt below. The joint Outcome source mutation → durable outbox
→ Life shadow index/readback rehearsal is now complete for shared Commitment
and Encounter Outcomes. Capture does not write Life rows or merge a receiver
branch implicitly.

Next connected checkpoint: complete CC-4's useful-first journey with real
representative content/native evidence. Life remains shadow-only; its next
hardening checkpoint is broader cross-viewer/race comparison. History-specific
Chat-image policy, remaining writer families, intention/social/expense
commands, and production transport remain separately gated.

### CC-5 follow-up receipt — Outcome Life rehearsal complete — September 6

The Outcome receiving checkpoint is now exercised against the shared local
PostgreSQL database. The landed Life shadow consumer and graph repair paths
cover both canonical audience shapes: active Occasion members for Encounter
Outcomes and active Commitment participants for Commitment Outcomes. The
rehearsal verifies source mutation → Life outbox event → current-authority
projector → indexed readback, then member departure withdrawal, stale replay
non-resurrection, explicit rejoin restoration, owner erasure withdrawal, and
surviving-audience repair.

Evidence: `travel-agent` commits `ba9463c2a`, `fd66f9f1f`, `329060a88`,
`afb13c6fa`, `6c42c92f7`, and `68e72d3f7`; **6 PostgreSQL tests passed** across
`tests/life_projection/test_outcome_projector_postgres.py` and
`tests/domains/experience_graph/test_outcome_life_producers_postgres.py`.
This is shadow-index/readback evidence only. Outcome serving, reader cutover,
and owner-matrix promotion remain disabled. The next Capture checkpoint is
CC-4 real-content/native evidence; the next Life hardening checkpoint is
broader cross-viewer/race comparison. Life withdrawal CAS hardening is now
also landed in `travel-agent` commit `1faa8a49c`; the first-insert-after-
deletion interleaving still requires an owner-side publication fence before
historical fan-out or serving cutover.

### CC-2/CC-5 follow-up receipt — retained-source Life replay — September 6

The canonical inline retained-source capture boundary now emits its
content-free Life owner event in `travel-agent` commit `5a6fce1f2`, aligning
direct Share Capture with the existing upload/finalize path. Commit
`33028d1cc` adds the retained-source representation/unrepresentation replay
transition: representation withdraws the Life row, and an
owner-revision-advanced unrepresentation restores it without allowing an old
replay to win. The focused source-to-Life lifecycle suite passes **28 tests**.
This remains shadow delivery; retained-source serving and any owner-matrix
promotion remain disabled.

### CC-5 follow-up receipt — bounded Life shadow rehearsal and lease safety — September 7

The receiving Life lane now has a reproducible bounded shadow rehearsal over
the existing owner/event seams. Plan, Occasion, shared Outcome and retained
source paths use current-authority reads and specialized consumers; generic
event delivery cannot acknowledge a graph event in their place or discard an
Outcome audience dependency token. The rehearsal also records all-lens
materialization, indexed-owner traversal/reconciliation, withdrawal and
explicit restoration, out-of-order replay, owner-commit/publication fencing,
and live-set retry cleanup. Persisted backfill pause/restart, stale claimant
rejection after lease takeover, and outbox lost-acknowledgement fencing now
have connected PostgreSQL evidence.

Evidence: `travel-agent` commits `41e07297e`, `ca559b2f7`, `bfb26e6a9`,
`27258111c`, `d062d1810`, `f9b687055`, `b7425b548`, `d7714e38c`,
`6c7d07847`, `949fdd524`, and `09d6f9b69`; the isolated Life projection
selection passes **182 tests** (165 offline and 17 connected on
`vesper_life_rehearsal_20260907`, migration head `lifebackfill02`). The
machine-readable report emits `vesper.life-shadow-rehearsal.v1` with
`supported_scope=pass`, `whole_portfolio_complete=false`, and
`serving_ready=false`. No API/schema or mobile change was made, and no reader
cutover or Atlas deletion is authorized.

This is evidence for the supported owner families, not a whole-portfolio
certificate. Full seven-record/four-viewer parity, broader lease/retry
interleavings, persisted unresolved-item replay through the runner,
Atlas/anchor migration, social/authored owner adapters, and serving acceptance
remain separately gated. Capture still owns source lifecycle/emission; the
next cross-lane dependency is the agreed owner contract for any additional
family, not a Life-owned writer.
