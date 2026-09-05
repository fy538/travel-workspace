---
doc_type: working
status: active
owner: founder / Strategy integration task
created: 2026-09-05
last_verified: 2026-09-05
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
| I0 | Planned; investigation baseline recorded | Verify actual engine paths and branch/flag/consumer map; resolve intent/material, shared-change and watch-owner decisions |
| I1 | Reusable infrastructure present; integration gaps remain | Trace owner identity plus condition signals; agree Life handles/change events and bounded reevaluation inputs |
| I2 | Reuse/leases and engine adapters present; general live integration partial | Measure serving and signal-to-judgment paths; separate fast practical assessment, authorized reevaluation and optional production |
| I3 | Capture foundations landed; owner decisions and formats partial | Audit writers/formats, draft precise owner ADR, then implement approved intent/social commands |
| I4 | Earlier root implementation present; latest Home design ahead | Make live judgment visible through useful preparation and alternatives; integrate accepted Home forms and the complete Places journey |
| I5 | Graph/consequence foundations present; lightweight experience incomplete | Complete adaptation and shared consequences over I1–I3, preserving purpose, plural participation and meaningful stop/wait behavior |
| I6 | Inventories/guards partially present; cutovers not complete | Refresh compatibility and obligation evidence; plan removal and readiness per actual supported consumers |

**First execution batch after authorization:** complete I0's owner inventory and
live-engine path matrix across practical preparation, changed conditions and
authorized waiting. Propose the exact missing contracts, implement independently
safe I1 continuity/signal repairs, and measure I2's current serving and evaluation
paths. Hold M0 before new shared or watch persistence. Do not spend that batch
rewriting canon, building a universal framework, or only expanding mock smoke
tests; do not defer the live engine until content composition is finished.

At the next checkpoint update this ledger in place, attach exact receipts, and
decide the next bounded batch. This keeps the roadmap live without making this
task a bottleneck for Life or turning six former specialist tasks back on.
