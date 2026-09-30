---
doc_type: working
status: active
owner: founder / program roadmap owner / context and research engineering
created: 2026-09-29
last_verified: 2026-09-29
expires: 2026-10-13
why_new: The artifact experience plan owns recognizable objects and readers, while the program owns dispatch. Neither should absorb this detailed cross-system code audit, nine-topic research synthesis, and proposed implementation dependencies for shared context, discovery, research, maintenance and evaluation.
supersedes: []
source_of_truth_for: []
---

# Adaptive context and research engineering roadmap

Vesper needs to turn a person's material and present circumstances into useful
understanding, discovery, practical help and enjoyable return. This document
maps the September research to the actual repositories and proposes how to
complete the shared machinery without rebuilding existing owners.

**Recommendation:** preserve originals and stable subject identity, retrieve
eligible evidence, investigate the public world selectively, and reconsider
results when relevant circumstances change. Keep the reasoning implementation
replaceable as models improve. Do not build a world encyclopedia, research every
saved item continuously, or make Chat the gateway to every useful result.

The foundations are substantial. Source custody, evidence coordinates, memory
admission, explicit Source preparation, publication fences, original readers,
root composition and notification delivery already exist. The missing coherent
path is **selected artifact or component → applicable context → worthwhile
candidate → bounded acquisition → supported treatment → maintained receiving**.
Some pieces work for Places or Trips but are not general artifact capabilities.

This is a **supporting plan, not an activated execution lane or another queue**.
The [program roadmap](../vesper-program-roadmap.md) owns assignments. Its newer
[delivery-lane version](../vesper-program-roadmap.md)
was the execution reference inspected here. Existing capture/share work and
the [Home package](../home-value-composition-execution-plan-2026-09-25.md) retain
their owner. No provider, background posture, sharing policy, deployment or
release is enabled by this document.

## 1 Scope and evidence baseline

This is a cross-repository investigation of the value-delivery system, including
its mobile consumers. It is not a line-by-line review of every product feature,
an independent security certification, or an observation of deployed behavior.

Inspection date is September 29 in New York; the final evidence snapshot was
taken around September 30 at 03:10 UTC. Branches advanced during the inspection.
The table records the later observed state rather than repeating an older
claim that all local main checkouts lag implementation.

| Repository or working material | Inspected state | Evidence boundary |
| --- | --- | --- |
| Canonical workspace | `8a14d87da8d4cab3cf86c59386c1fb3eafdc900d`, main | Extensive pre-existing uncommitted design/strategy work; preserved |
| Delivery workspace | `1df49834`, `codex/home-value-delivery` | Newer program/H1 guidance and concurrent working changes; not copied wholesale |
| Backend main and delivery | `3c170d21fc0ca9231b956f2b9de7f9f195231768` | Clean at inspection; merge from `ffe147856` has no code diff, so reads at that earlier revision still apply |
| App main and delivery | `87eceee24512d9086962eea5b844cef9d7bffbeb` | Clean at inspection; Expo `~55.0.31`, React Native `0.83.10`; no upgrade proposed |
| Strategy workspace | `530f0459ea6e36e3822073f3546fbcd073380454` plus working changes | September 29 product amendments and artifact roadmap include uncommitted material; direction/planning evidence, not implementation |

The strategy roadmap changed during this investigation to add catalog anchoring
and newer artifact design references. The inspected file's SHA-256 was
`73aeec70d9a1ce830cedf7e0a60d4309a17fb36086374a36ea5550a59b1bc594`.
Re-read it before admission rather than treating this snapshot as its latest
word. The [Artifact experience engineering roadmap](../artifact-experience-engineering-roadmap-2026-09-29.md)
was inspected in the product-direction worktree. It is now integrated into this
repository; the relative link follows that integration without changing the
dated evidence above.

Three read-only investigators covered ingestion/retrieval/research,
runtime/temporal/delivery, and memory/privacy/evaluation/mobile. The coordinator
read authority documents, checked disputed paths and reconciled their findings.
No product tests, live model calls, provider benchmarks, database races,
simulator captures or production probes ran in this investigation. Test paths
below identify **defined coverage**, not newly passing evidence. H1's previous
receipts remain evidence only for their recorded environments and revisions.

## 2 Product requirements and authority

Read the accepted [documenting and composer decision](../../decisions/2026-09-27-documenting-core-loop-and-one-composer.md)
and [collections decision](../../decisions/2026-09-28-collections-are-the-spine.md)
alongside the [contribution contract](../../systems/contribution-and-consequence.md),
not as though its older entry table overrides their explicit amendments.

The latest strategy-lane Thesis/Model and September 29 record-value amendment
make recognizing, keeping, enjoying and refinding independently complete value.
Those current working changes must be reconciled by their owner when landed;
this roadmap does not declare all affected contracts updated.

The engineering requirements are:

1. **Immediate recognizable value.** The original or supported structured thing
   remains usable without optional public research, personal history or friends.
2. **One thing across entrances and surfaces.** Preserve original sources,
   selected components, subject identity and collection memberships without
   treating them as one universal database object.
3. **Actual additional substance.** Connections should explain, contrast,
   reveal a relevant possibility or provide practical relief. Repetition of
   the person's observation is not enrichment. Original-only remains valid.
4. **Current intent governs.** Attention does not imply enduring preference;
   preference validity does not establish applicability to this interaction.
5. **Independent human contributions.** A friend can add value without equal
   effort. Display, synthesis, onward sharing and persistent copying remain
   distinct authorities. Preserve authorship and differing perspectives.
6. **Practical claims have appropriate evidence.** A nearby possibility is not
   a confirmed opening, available ticket, booking, commitment or visited place.
   Current operational questions use current provider/domain truth where needed.
7. **Useful change without arbitrary rewriting.** New context may change the
   best addition, not the original or an exact edition deliberately kept.
   Correction and loss of permission can still change availability.
8. **Low effort and bounded attention.** No routine reflection homework,
   classification questionnaire, mandatory conversation or generated card quota.
   Research completion does not automatically justify push.
9. **Accountable operating cost.** Recognition, indexing, research, composition,
   retry and unused preparation all count. A telemetry field is not a spend cap.

The September 27 amendment matters specifically: a deliberate composer share
with a question is Bring plus Ask, with visible private keeping and an Ask-only
escape. It does not adopt general conversational-history reuse. Do not restore
the older blanket transient-attachment rule, and do not interpret every question
as permission to retain or monitor.

Collections organize consumer material; Source, Place, Plan, Commitment and
other existing owners retain truth. The backend editorial `collections` table
is not a consumer collection owner merely because the names match.

## 3 Current system and concrete gaps

Backend references beginning `backend/`, `tests/` or `tools/` are relative to
`travel-agent/`; abbreviated implementation paths such as `concierge/` or
`core/db/` are relative to `travel-agent/backend/`. Mobile paths are relative
to `travel-app/`. Line references are observations at the revisions above and
may move. Start with the owning function and nearest tests.

### 3.1 Capture and original evidence

The current path is Intake create/upload/finalize → verified Source custody →
normalization → semantic interpretation → submission-scoped admission. Keeping
does not require semantic interpretation to complete first.

`backend/api/routes/intake.py:178,234` provides custody and original-media
routes. The original route validates current availability and content identity,
including a check after fetching bytes. `backend/inbound/normalizers.py:22`
defines page/frame/character locators; `backend/core/intake_evidence.py:15`
also validates bounded rectangles and source/snapshot/custody hashes.

**Reuse:** authoritative original reads, provisional interpretation, idempotent
custody, locator validation and Source-to-Life handoffs.

**Gap:** those coordinates are not yet a general, stable selected-component
identity and retrieval contract. A locator must refer to a specific source
representation; stale coordinates must not silently select different content.

Image normalization is metadata-only at `normalizers.py:208`. The semantic
worker separately downloads pixels at
`backend/workers/intake_semantic_jobs.py:403`; that does not constitute a
searchable OCR/region corpus. The active scanner/decoder boundary still rejects
some media such as PDF/PKPass/HEIC, despite broader future-facing forms. New
retrieval work must not imply that every proposed capture format is supported.

### 3.2 Refinding and retrieval

`POST /api/life/originals/refind` uses
`backend/core/db/intake_original_refind.py:20` and
`backend/life/original_refind.py:99`. It searches bounded retained-original
metadata such as notes, filenames and capture information; it deliberately
does not search private body text or fetch original bytes. Its tests assert
that boundary and preserve similar-but-distinct originals.

Universal Search (`backend/search/dispatch.py`) federates existing owners.
Atlas combines lexical and semantic paths, but its vector representation at
`backend/core/vector/atlas.py:60` is one point per artifact built from title,
one-line reading and Place label. A detail absent from those fields cannot be
recovered merely by improving the ranker.

**Reuse:** search federation, rank fusion, filters, exact relationships and
metadata refinding. **Extend:** source text/passages, useful visual detail and
collection relationships, grouped back to distinct underlying evidence.
Indexes remain rebuildable projections; hydrate current owners before use.

### 3.3 Context compilation and personalization

`backend/core/context_compiler/compiler.py:189` has typed evidence, purpose,
audience and budget machinery, but it authorizes a Trip and compiles Trip member
facets. Its scope vocabulary is trip/day/period/gap. It is not an arbitrary
artifact context compiler today.

Personal Memory is more mature than older workspace prose suggests.
`backend/concierge/tool_contracts.py:313` gives `observe` an explicit-user
authority requirement; `memory_tools.py:167,586` describes and enforces scoped,
actor-bound use. `preference_engine/retrieval/preference_retriever.py:120`
returns first-contact context when memory is missing/stale rather than
generating during the read. `core/db/personal_memory_evidence.py:302` binds
aggregate eligibility to current evidence; synthesis publication and later
reads use evidence manifests.

**Do not redispatch a wholesale memory-admission rebuild.** Add the missing
consumer applicability decision: which admitted evidence is useful for this
object, purpose, situation and requested form of help? Current aggregates and
valid preferences can still be irrelevant. Reuse observation/correction owners
before proposing a second preference store.

### 3.4 Source discovery and composition

The Source contribution path already discovers governed opportunities,
selects a compatible source group, hydrates exact owners/material and invokes
a structured producer before root admission. Relevant files are
`backend/root_projection/v2/source_contribution_discovery.py:86`,
`source_contribution_opportunities.py:294,485`,
`source_contribution_pipeline.py:212` and `source_contribution_producer.py`.

The selector is substantially Place-oriented. It supports approved pairings
such as anchor plus dossier or handoff plus dossier, normally requiring at
least two current Sources. The producer contract requires new synthesis and
Home/Places expressions. These are legitimate rules for that job, not the
universal grammar of every focused artifact.

The photo material adapter at `source_contribution_materials.py:192` supplies
count, MIME and canonical Place, **not image pixels or OCR**. Its tests require
the producer not to infer image contents. A current photo-to-Place contribution
therefore does not prove visual-detail understanding.

Repetition controls include exact attempted-group exclusion and a bounded
history of claims delivered through Home/Places (`pipeline.py:137`). They do
not represent everything a person knows or every claim they authored.

**Extend:** selected-object discovery and a distinct focused treatment policy.
Preserve the existing two-source Home policy. Original-only, attributed
juxtaposition and single-source explanation need no forced second citation.

### 3.5 Public research and evidence quality

`backend/research_agent/agents/quick_research.py:28` already accepts purpose,
scope, gaps, locality/time, deadline, operation limit and `answer_only`.
`pipeline/schemas.py:37` defines a typed bounded request/result. This is the
preferred consolidation seam, not a new research microservice.

The quick path still uses the dossier-oriented graph and a per-invocation
`MemorySaver` (`quick_research.py:103`). Answer-only routing avoids persistence;
legacy behavior remains for existing callers. Independent subqueries run
concurrently with bounded cancellation in `pipeline/source_gathering.py:792`.
Reflection considers iteration, coverage and convergence; it is not a
calibrated value-of-information controller.

`pipeline/bounded_result.py:80` checks that citations resolve to gathered page
sources and rejects ambiguous bindings/provider summaries. **Source binding
is not semantic entailment.** A matching URL does not establish that its
passage supports the generated claim. `pipeline/disposition.py` is a useful
write-free handoff mapper, but the inspected caller search found no production
adoption beyond its declaration. Treat it as scaffolding, not completed reuse.

The inspected profile currency/subagent/cache fields are not proof of runtime
enforcement. The operation count covers routed subqueries, which can fan out
to several providers. A hard spending boundary must account at chargeable
dispatches, not infer cost from that count.

Existing research callers remain specialized. `workers/research_jobs.py:146`
expects a Place and personal conversation. Missing-coverage subscribers
deliberately omit raw private queries and disable query-specific background
research until a reviewed public request exists (`research_agent/subscribers.py:102`).
Do not reactivate that path simply because the function is registered.

There is a useful privacy specimen in
`concierge/tool_handlers/trip_direction_research.py:212` and `web_search.py:121`:
canonical public destination fields go to a fixed public search, while private
preferences stay in private synthesis. Generalize this boundary, not the full
private prompt.

### 3.6 Runtime and temporal execution

Explicit Source production is already connected:

```text
user invoked Source request
  → agent_workflows route and durable workflow
  → worker dispatch when explicitly enabled and canonical executor
  → current source reads and structured production
  → attempt fenced publication
  → exact result readback
```

`backend/api/routes/agent_workflows.py:432`,
`backend/workers/source_contribution_jobs.py`,
`backend/root_projection/v2/source_contribution_canonical_executor.py` and
`backend/core/db/source_contributions.py:121` are the relevant owners. The
canonical executor accepts explicit warming and rejects unbound signal labels.
Production admission is default-off; worker registration, dispatch and recovery
also require the worker flag and named cohort (`core/feature_flags.py:191,203`,
`api/routes/agent_workflows.py:489`). A durable workflow can exist without being
dispatched. Ordinary Home/Places reads at `application/root_composition.py:746,802` consume
prepared eligible results; misses do not generate or enqueue work.

H1 records a real local API/disposable-DB/native connection with synthetic
material and a provider-free authored producer. That establishes the connected
path, not real-model usefulness or recurring useful supply. Do not repeat that
fixture proof under a new name or build a second generator to fill the gap.

There are already general execution mechanisms: Arq workers and Postgres
`scheduled_tasks`. The latter claims due work with `SKIP LOCKED`, supports
priority/retry/stale-claim handling, and is used for Place refresh. Neither a
new scheduler nor migration to a new workflow vendor is the starting point.

There is also a specialized entity-research queue. The entity route admits
supported catalog targets; `core/db/content/_review_queue.py:245,336` claims
rows but completes by row identity rather than a claim generation. The inspected
`tasks/process_research_queue.py` caller was a CLI; no deployed automatic drain
binding was found in the inspected callers. This is unresolved deployment
evidence, not proof that no external scheduler exists or that the queue is dead.

The inspected general scheduler completion is keyed by task ID rather than a
claim generation. Before using it for long research, test a stale worker
finishing after takeover and add the appropriate fencing if absent. Do not
infer that the stronger Source publication path has the same weakness.

Budget controls differ by path: city seeding now uses an atomic Redis
reservation (`research_jobs.py:447,542`); Places budget checks still count
before calling and record afterward. The latter is not an atomic shared spend
reservation. A universal daily cap is not established by either local example.

### 3.7 Mobile receiving and notification ownership

Home and Places use governed root projections, expiry and return-context
machinery. `hooks/useRootSourceInspection.ts:44` can request explicit preparation;
`app/source-contribution/[workflowId].tsx` and
`hooks/useSourceContributionResult.ts:33` provide exact-result reading and
pending-only polling. Failed/unavailable reads do not silently submit new work.

The canonical artifact route `app/you/memories/artifacts/[id].tsx:24` renders
the existing projection; `utils/canonicalArtifactActions.ts:31` executes only
available `open_owner` actions. It is not yet the proposed focused discovery,
selected-component or kept-edition experience. Extend these consumers through
the data facade rather than create an unrelated research-report destination.

Life now directly mounts `LifeRootV1Screen`; older flag descriptions are not
accurate tab-entry evidence. Governed Home/Places still have internal rollout
controls and `releaseEligible=false` in `utils/productSystemRollout.ts:36`.
Reachable code is not release certification.

Notifications already own attention identity, interruption decisions and
delivery through their registry/arbiter/delivery spine. Preserve that owner.
A completed research job can make a result available, but cannot select its
own recipient, push urgency or attention policy. New organizing structure and
friends' actions follow accepted placement decisions; silent private filing
does not become a notification. New cadence/automatic-trigger policy remains
separate from reliable execution.

### 3.8 Existing evaluation and documentation drift

Reuse the retrieval/research plugins under `tools/eval/plugins/`, the Source
editorial judge, correction/privacy tests and registered native QA. Their
current scope is uneven: venue retrieval, dossier research and Home/Places
expression are not general artifact support-set evaluation. The venue runner
can omit queries lacking expected IDs/filter assertions; useful silence needs
an explicit verdict rather than disappearing from the denominator.

Older workspace memory/contribution status paragraphs and worker budget prose
conflict with newer implementation. Preserve their policy rationale, but have
the owning package reconcile status text when adopting work. The September 26
product-map percentages and production observations are dated evidence, not
updated estimates supplied by this audit. No percentage complete is claimed.

## 4 Research conclusions translated into engineering choices

These are recommendations and experiment hypotheses, not vendor selections.
Recent preprints supply useful failure cases; none proves Vesper's consumer
advantage. Older production references remain relevant where they establish
better understood properties.

| Research topic | Recommendation for this system | Stronger alternative and adoption test |
| --- | --- | --- |
| Multimodal retrieval | Preserve original plus inexpensive reusable extraction; hybrid retrieval, then inspect a few originals | Add multimodal embeddings/region retrieval only when artifact support-set recall and downstream usefulness improve after ingestion/index costs |
| Discovery without a question | Diversify a few object-anchored relationship candidates, verify the useful ones, allow no addition | Hypothesis-generating exploration must beat direct retrieval on distinct supported substance, not paragraph count |
| Adaptive effort | Reuse, targeted lookup, bounded discovery and extended research with simple observable rules | Learned routing or agent teams must beat rules/parallel tools at equal cost and latency budgets |
| Temporal knowledge | Separate valid time, received time, freshness, selection and preparation; track bounded dependencies | Fine-grained dependency graphs or predictive refresh must outperform coarse revision checks after maintenance and wasted-work cost |
| Assistance personalization | Apply admitted preferences only when relevant; current request overrides default treatment | Learned ranking requires suitable exposure logs, worthwhile outcomes and evidence beyond clicks |
| Model evolution | Stable evidence/job contracts, replaceable planning loop and versioned recipes | Compare new model/current orchestration against new model/simplified orchestration; remove obsolete workarounds |
| Shared execution | Reuse workers; coalesce equivalent acquisition; reserve interactive capacity and aggregate budgets | Adopt another durable workflow platform only if recovery/deployment complexity remains a measured bottleneck |
| Private and social research | Minimal permitted public queries; private synthesis; current grants at read and publish | More elaborate information-flow tracking earns adoption against real leakage cases, not framework novelty |
| Compounding evaluation | Matched current-only/history/correction comparisons over evolving artifact portfolios | Learned policies require human usefulness and longitudinal evidence, not just simulated users or judge agreement |

The primary-source evidence and limitations are recorded in section 11.

## 5 Target architecture and final state

### Responsibilities to consolidate

Consolidate research acquisition, provider dispatch/accounting, evidence
normalization and shared execution semantics. Do **not** consolidate custody,
memory, ranking, collection membership, notification policy and consequential
actions into a single omniscient agent.

| Responsibility | Owning boundary to reuse or extend |
| --- | --- |
| Original bytes, custody, representation version and source locators | Intake/Source owner |
| Stable public subject and licensed catalog fields | Entity/Place and approved catalog adapters |
| Personal material identity and collection membership | Artifact P1 owner mapping; not editorial guide tables |
| Admitted preferences and correction | Preference/contribution owners |
| Selected-object evidence request and candidate discovery | Existing retrieval/composition seams with a new bounded adapter |
| Public research and evidence acquisition | Existing bounded research module and permitted adapters |
| Durable execution, reservations and result publication | Existing workflow/worker/scheduler owners, with explicit responsibilities |
| Useful treatment and root prominence | Focused treatment policy or Home/Places composition owner |
| Exact kept expression | Artifact P4 saved-composition owner, once resolved |
| Interruption and delivery | Existing attention/notification owner |
| Operational changes | Plan, Commitment, provider and other domain owners |

Keep the Trip compiler's strong invariants. Extract genuinely shared evidence
types/helpers only where needed; do not make every Trip field optional to
pretend it is a universal context compiler.

### Contract requirements

Review the following semantics before parallel implementation. These are
requirements for existing contracts/adapters, not instructions to create one
table or service per row.

- **Selected target:** owner reference, optional component/locator,
  representation revision, viewer, originating surface/collection, purpose,
  current explicit instructions and relevant time/place. No fabricated Trip or
  conversation ID. Unknown subject identity remains representable.
- **Research request:** `resolve` or `discover`, public subject/allowed fields,
  specified uncertainty or discovery purpose, required evidence, scope,
  freshness, provider policy, operation/token/time/spend limits and authorized
  completion consumers. Private context is not a free-form pass-through.
- **Evidence result:** stable source references, retrieved/effective dates,
  exact excerpts or permitted locators, candidate versus supported claims,
  conflicts, gaps, coverage, stop reason and measured usage. Reuse/retention is
  opt-in under the owner, not implied by a URL.
- **Execution identity:** request equivalence, scope, recipe version, attempt
  and lease generation, budget reservation, subscribers, cancellation and
  publication pointer. Account for possible duplicate provider spend even if
  only one result can become current.
- **Influence manifest:** support, selection context, novelty history,
  preference applicability and authority are different dependency roles.
  Include the candidate scope and index progress even when nothing was found.
- **Consumer result:** distinguish original-only, useful silence, incomplete
  discovery, rejected proposal, provider failure, revoked evidence and expired
  practical facts. Use existing state models where possible.

The proposed clarification to artifact P3 is: bounded public research may
**resolve a specified uncertainty or discover candidates for a named purpose**,
anchored to the selected object and circumstances, within explicit limits.
Verify claims before presenting an addition. The existing line restricting
research to a named missing fact is too narrow if applied to all discovery.
This document proposes that change; it does not edit the other owner's plan.

### Public storage is selective rather than absent

On-demand research does not eliminate stable catalog IDs, licensed artwork,
facts reused across openings, cached evidence or independent personal records.
The new artifact PC package legitimately needs canonical work/venue anchors and
licensed media. Preserve source terms, provenance and field-level freshness.
Do not treat web search as a substitute for permitted catalog art or provider
availability, and do not expand catalog anchoring into speculative dossiers for
every world entity.

### Temporal behavior

Maintain separate content validity, selection freshness and preparation state.
Recheck cheap selection before commissioning expensive generation. A new Source
can invalidate an earlier empty candidate set; a provider timeout is not reusable
proof that nothing exists. Source publication time, effective time, encounter
time and received time are not interchangeable.

Event notifications can make selection eligible for reconsideration without
authorizing generation. Coalesce changes by a bounded candidate scope, not a
global user revision that invalidates everything. Search over the open web
cannot supply exhaustive dependencies; use explicit coverage and freshness
policies rather than claiming full incremental knowledge of the world.

Model/provider calls stay outside database locks. Short publication checks
validate the current attempt, relevant owner/grant revisions and selection
generation. Later reads still revalidate authority. Cache validation is not a
substitute for source eligibility.

### Definition of the completed capability

Within an explicitly supported family/mode matrix, a person can open their
material immediately, receive a substantive eligible addition when warranted,
and revisit an exact kept edition without new work. Authorized new material or
changed circumstances can improve later selection. Sources remain attributed,
corrections propagate, and denied/failed research leaves independent value
intact. Home, Places, Chat, Life and notifications consume the same owners with
different purposes; none invents a new copy of truth or acquires extra authority.

The implementation has measured cold/warm latency, end-to-end spend, waste,
recovery and quality. Consumer desirability and release approval are separate
evidence checkpoints, not consequences of checking every engineering box.

## 6 Proposed implementation packages

All packages below are **proposed and unscheduled**. Identifiers are local to
this supporting plan. The program owner can absorb their work into existing
artifact packages rather than create additional standing lanes.

| Package | Complete outcome | Existing artifact alignment | Dependencies |
| --- | --- | --- | --- |
| R0 | Current owner/contracts/evidence baseline admitted | P0 and PC source boundaries | Current program checkpoint |
| R1 | Caller-independent bounded public research with privacy and honest outcomes | P3 acquisition; PC remains separate | R0 |
| R2 | Selected-object/component evidence retrieval and useful selection | P1/P2/P3 | R0; usable owner references; integrates R1 |
| R3 | Accountable shared execution with concurrency, reservations and recovery | P5 runtime | R0/R1 contracts |
| R4 | Selective change handling and exact-result continuity | P4/P5 | R2/R3; P4 owner for durable editions |
| R5 | Situation-appropriate assistance preferences | P3 selection | R0/R2 contracts; existing admitted evidence |
| R6 | Connected artifact/root/social receiving | P2/P6 | Early work uses existing results; full scope uses R1–R5 |
| R7 | Comparative quality, lifecycle and operating acceptance | P0/P7 | Starts in R0 and accompanies every package |

### R0 Reconcile the actual baseline and contracts

**Outcome:** one interface/owner map and representative evidence portfolio,
without restarting completed Home or capture connections.

- Recheck revisions, dirty files and program assignments. Preserve current
  capture/extension/signing, authenticated readback and Home residual owners.
- Resolve selected-object versus Trip context; source/component/subject identity;
  candidate versus verified finding; exact result versus kept edition.
- Read accepted amendments into affected contracts. Reconcile stale status
  paragraphs without rewriting historical decisions.
- Establish fixtures across tickets, venue/work anchors, passages, photographs,
  practical records, permitted human contributions and sparse history.
- Record current flags and known live-provider/device gaps, not just callable
  entry points or configured test names.

**Acceptance:** each scenario has a real owner, exact inputs and revision,
consumer, repair path and evidence boundary. Pending decisions name only the
behavior they block. No universal new schema or duplicate scheduler is assumed.

### R1 Generalize bounded acquisition

**Outcome:** an existing or focused consumer can request public lookup or
bounded discovery without inventing a Place/Trip/conversation.

- Extend `BoundedResearchRequest/Result` and reviewed adapters; retain compatibility
  for current callers and explicit completion treatment.
- Apply a typed public disclosure boundary using the existing destination-only
  fallback as a specimen. Private synthesis requests a specified public
  uncertainty or bounded candidate-discovery purpose through that boundary,
  not unrestricted browsing.
- Separate candidate discovery from factual verification. Preserve source
  binding and add claim-support evidence/checks appropriate to consequence;
  never call URL matching semantic verification.
- Preserve answer-only non-persistence semantics, but give lookup/discovery
  purpose-specific planning and stop criteria. Today the quick path still
  selects a dossier graph, and unknown target types default to site dimensions
  in `backend/research_agent/agents/deep_research.py:400`; `answer_only` does not
  remove those assumptions. Do not invent an entity or seek irrelevant dossier
  completeness. Preserve the legacy path for its authorized callers. Adopt
  the disposition mapper through an actual owner caller, not an unused layer.
- Own a small observable effort policy here, with R3 enforcing its resource
  allocation. Distinguish difficulty, urgency and consequence; choose existing
  evidence, targeted acquisition or bounded discovery. Stop when evidence
  suffices, supported gain stalls or limits expire; escalate or abstain on
  consequential unresolved conflict. Higher queue priority or a larger model
  does not itself authorize more spend or weaker evidence.
- Record meaningful partial/empty/failed/stopped outcomes and actual provider
  fan-out. Keep raw-query coverage research disabled until this boundary is
  exercised end to end.

**Acceptance:** public fact lookup and bounded discovery both pass through the
actual disclosure adapter from a selected object with unresolved optional
subject identity. A non-place lookup stops when its stated evidence requirement
is met, without fabricated identity or irrelevant site-dimension coverage.
Compare easy-but-consequential and difficult-but-low-stakes requests. Private
markers must not reach provider arguments, including follow-up calls after
adversarial retrieved text, OCR or image content. Untrusted content remains
evidence, never authority; test tool/egress compromise separately from an
injected but non-exfiltrating false answer. Unsupported claims cannot be
promoted by citation shape alone; deadlines and partial failures are honest;
there are no unintended writes. Run compatibility tests for existing users.

R1 can proceed with provider-free fixtures or existing explicitly bounded paid
authorization. A new paid acquisition path needs applicable admission limits
and chargeable-attempt accounting before enablement, including on-demand work.
That dependency does not require all of R3's later scheduling improvements.

### R2 Retrieve the evidence and select a worthwhile addition

**Outcome:** the system can find and use information omitted from a one-line
artifact summary, without making every original expensive to ingest.

- Add a selected-object adapter around current owner reads, not a fake Trip.
- Reuse source locators and define stable component identity/revision semantics
  with P1. Start against existing original references while that contract grows.
- Implement a baseline combining exact identifiers/relationships, literal
  text and semantic passages. Group representations by underlying evidence.
- Hydrate current eligible originals or selected regions after recall; preserve
  surrounding context. Indexing cannot grant access or establish occurrence.
- Allocate a bounded candidate set across useful relation directions, then
  evaluate support, additional substance and situational relevance separately.
- Give focused artifacts their own reviewed treatment policy while preserving
  existing Home pair requirements and avoiding generic trivia.
- Compare visual embeddings, richer extraction, reranking and original
  inspection as alternatives on the same corpus before adopting complexity.

**Acceptance:** passage/detail support sets are retrieved; same-title subjects
and repeated visits stay distinct; a supported contrast and an original-only
case both succeed; prior user-supplied connections are not repackaged as new;
failed indexing differs from a complete empty search. Include retrieval and
selection metrics independently, with equal-quality original baselines.

### R3 Share execution and account for its cost

**Outcome:** foreground and background consumers can reuse compatible work
without starving interactions or multiplying unbounded spend.

- Assign job ownership across existing durable workflows, Arq and scheduled
  tasks. Do not nest independent retry owners around the same provider effect.
- Inventory the entity queue's actual drain owner, deployment and stale-worker
  completion before reusing or retiring it. Preserve specialized Places refresh.
- Deduplicate by substantive request equivalence, public/private scope,
  freshness and recipe—not merely entity ID. Model surface subscriptions
  separately from evidence results; cancellation detaches one consumer unless
  no authorized consumer or permitted preparation purpose remains.
- Reserve finite resources before chargeable dispatch, with conservative token/
  provider reservations and usage settlement where available. Keep unmeasured
  billing unknown rather than recording zero. Reuse the seed reservation pattern
  where appropriate; do not generalize its policy automatically.
- Protect interactive capacity and enforce per-user/provider limits across
  callers. Priority alone does not preempt a provider call already running.
- Choose durable checkpointing for long/expensive work; short jobs may restart
  under a finite retry budget. Pin compatible recipe versions across resumption.
- Exercise claim takeover and publication fencing, including general scheduled
  tasks if reused. Preserve the stronger existing Source-specific fence.

**Acceptance:** duplicate compatible requests share work, incompatible dates/
purposes do not; one subscriber cancel does not break another; burst capture
does not exhaust foreground capacity; concurrent dispatches cannot oversubscribe
the adopted reservation; stale attempts cannot publish; ambiguous provider
completion records possible duplicate spend. Do not promise exactly-once billing.
Two-user fixtures must show compatible public acquisition reuse while rejecting
reuse of private results. Subscriber identities, private selection context and
personalized synthesis remain separately scoped even when acquisition is shared.
Test cancellation/lease expiry with a provider call still in flight: do not
release its reservation as if no charge could occur, then admit replacement
spend unchecked. Reconcile unknown completion and settlement after a crash.
Test deadlines expiring during calls, not only before dispatch; specify each
owner's late-result/publication behavior instead of assuming every current
refresh path already enforces it.

### R4 Maintain relevance without rewriting the record

**Outcome:** relevant arrivals and corrections change future selection, while
stable originals and deliberately kept editions retain their identities.

- Extend existing owner events/outboxes with bounded candidate-scope progress
  and complete influence manifests, including empty selections and novelty
  history. Advance index readiness only when preceding relevant work is resolved.
- Distinguish support validity from selection freshness and preparation.
  Coalesce changes, reselect cheaply and reuse equivalent eligible output.
- Use field/purpose-sensitive public freshness, conditional refetch where
  available, and owner/provider truth for operational claims. A page's unchanged
  representation does not prove its assertions correct.
- Bind exact kept editions through artifact P4. Workflow readback and its
  temporary retention are not permanent saved-expression ownership.
- Recheck grants on publication/read; repair derived results without deleting
  independent originals or promising recall of already delivered bytes.

**Acceptance:** Day 1 ticket/Day 2 kept edition/Day 5 photo; new candidate after
empty selection; late historical upload; correction to novelty history; index
lag; revoked source during generation; mounted expiry; account change and
reconnect. Unchanged warm opens cause no generation. New ambient production
requires its separate adopted trigger policy.

### R5 Apply assistance preferences in context

**Outcome:** admitted context changes the type or depth of help only when it
applies to the present request.

- Select scoped evidence through existing memory/contribution owners, preserving
  current explicit overrides, attribution and correction dependencies.
- Distinguish current attention, session adjustment, standing preference and
  aggregate product learning. Do not promote opening/dwell/silence into identity.
- Make applicability inspectable for evaluation with content-minimized reasons;
  do not create a user-facing profile-maintenance task.
- Defer bandits until eligible alternatives, exposure selection and worthwhile
  outcome logging support valid comparisons. No experimentation on authority.

**Acceptance:** concise default plus explicit depth; practical question today
versus reflective opening later; parents' constraints not becoming the user's;
one correction versus standing rule; valid-but-inapplicable preference; correct
withdrawal; capable no-history tie. Better preference compliance alone is not
enough if usefulness or current-intent respect declines.

### R6 Connect receiving without inventing another product

**Outcome:** the shared capability reaches the focused artifact and appropriate
roots through their existing readers and owner-backed navigation.

- Extend the canonical artifact/data facade and exact-result reader to preserve
  selected component, original, attribution and return position. Optional
  intelligence never blocks the original with a whole-page generation spinner.
- Keep Home prominence, Places spatial relevance and Life organization with
  their existing owners. Chat continuation is optional and explicitly invoked.
- Preserve native distinction between useful silence, unavailable evidence,
  failed acquisition and pending work. Read/poll never silently creates work.
- Reuse exact-original recipient access and current relationship checks.
  Add synthesis only for the exact purposes actually granted; preserve separate
  human perspectives and private viewer context.
- Send eligible completion/change events to existing attention policy. Do not
  expose each research step, silent filing or every available result as a push.
- Reuse current owner-backed practical facts; route changes/actions through
  domain owners. Do not add booking execution or mistake a link for availability.

**Acceptance:** original-first inspection and useful addition on real owner
readback; detour and exact return; receiving without reply or contribution;
withdrawal and account-switch races; appropriately quiet completion; native
accessibility and visible failure states. Broader shared/offline policies block
only their affected modes, not all private progress.

### R7 Establish quality and operating evidence throughout

**Outcome:** we can tell whether each added mechanism helps, what it costs,
and which part fails when the experience is weak.

- Extend existing runners/judges instead of building another evaluation system.
  Support complete evidence sets and explicit empty/rejected outcomes.
- Compare matched current-only, correct-history, irrelevant-history,
  outdated-history, corrected-history and manually selected evidence.
- Separate retrieval recall, selection quality, source support, applicability,
  permissions, human benefit and operating cost. Preserve historical truth
  while excluding obsolete facts from present judgment.
- Keep related histories in the same split and prevent future-evidence leakage.
  Counterbalance human comparisons; account for shared-collection spillovers.
- Compare model and orchestration versions jointly. Remove planner/reflection/
  compaction steps only when their absence improves or preserves the relevant
  quality/cost boundary.

**Acceptance:** reproducible offline comparison, required disposable-DB races,
bounded authorized live-provider evidence, authenticated native receiving and
human comparisons have separate receipts. Natural-use evidence addresses
voluntary return, reduced repeated explanation, unwanted effort and recipient
benefit. Synthetic users and model judges do not certify those outcomes.

## 7 Sequence and parallel execution

Do not schedule eight permanent lanes. Preserve one accountable package owner
and use temporary workers when delegation is authorized.

1. **Admission checkpoint:** reconcile this plan with the newest program and
   artifact PC/P0–P7 packages. Finish R0 and select exact interfaces and scope.
   Existing capture/share work continues; signing and design polish do not
   block independent backend contracts or offline fixtures.
2. **First engineering wave:** R1 bounded acquisition and the existing-original
   portion of R2, with R7 fixtures/measurement alongside. This builds shared
   capability across several artifact families, not a single demonstration
   that defines the whole architecture.
3. **Second wave:** R3 execution hardening and the richer R2 selection/consumer
   connection. Keep R6's real receiving path involved so backend output does
   not become an isolated report. Catalog PC proceeds under its own approved
   provider/identity owner.
4. **Third wave:** R4 selective maintenance and R5 applicability, then complete
   the chosen private/shared R6 modes and R7 acceptance. Some work can overlap
   once owner contracts are stable; exact saved editions depend on P4.

Useful parallel assignments are evidence retrieval versus public acquisition,
and later native receiving versus runtime hardening. Shared schemas, migrations,
request/result semantics, reservations and generated API types have one owner.
Independent evaluation fixtures may proceed throughout. Never let two workers
change the same authority model without a named integrator.

Each assignment includes outcome, baseline revisions, file ownership, contracts,
allowed effects, acceptance commands and escalation conditions. Carry diagnosis,
implementation, focused checks and review corrections through one complete
assignment. Check in at the first connected result, a consequential blocker and
completion; ordinary debugging does not require founder relay.

Integrate at a meaningful interface or complete outcome, not after every tiny
commit. Do not leave finished work indefinitely on disconnected branches.
Publishing/deployment and policy changes retain their separate authorization.

### Reassessment checkpoints

| Checkpoint | Question | Possible change |
| --- | --- | --- |
| R0 contract review | Can the same boundaries support sparse artifacts, practical help and authorized shared originals? | Revise ownership before adding tables or generic optional fields |
| First R1/R2/R6 connection | Is the addition substantive, and is the original still immediately useful? | Improve retrieval or treatment rather than merely generating longer prose |
| R3 load and recovery | Do reuse and preparation improve experienced latency at bounded cost? | Reduce prefetch, isolate capacity or change recovery granularity |
| R4/R5 longitudinal replay | Does later evidence improve judgment without overwriting or overpersonalizing? | Change dependency scope/applicability before adding learning complexity |
| Selected-scope receiving review | Does an ordinary person benefit without rich setup or equal social effort? | Adjust product treatment and supported scope before broader exposure |

## 8 Decisions and nonblocking boundaries

| Decision | Recommended posture | Blocks only |
| --- | --- | --- |
| Selected component and artifact identity | Reuse Source revision/locator and P1 mapping; no fake Trip or universal artifact table | Incompatible identity/schema implementations |
| Focused discovery versus named-fact-only research | Admit both bounded request kinds, with purpose, evidence and limits | New discovery policy; existing exact fact lookups remain usable |
| Catalog sources and display/caching rights | Select per medium through PC; use approved fields and house fallbacks | Real catalog art/facts from unapproved suppliers |
| Automatic preparation | Separate cheap reconsideration from paid generation; permit only named adopted triggers | New ambient generation, not explicit research or pure reads |
| Shared synthesis and saved derivatives | Apply current grants; do not infer synthesis from display or invent survival after withdrawal | Affected shared AI/retained derivative modes |
| Shared offline retention | Define cached content, duration and reconnect behavior; do not promise instant remote recall | Persistent shared offline promise |
| Notification cadence | Preserve delivery owner and accepted placement; research cannot self-escalate | New automatic/push policy, not available in-app value |
| Currency budgets and spend authority | Adopt applicable limits/accounting before new paid path enablement | Unbounded new paid on-demand or recurring work, not provider-free engineering |
| Consumer collection owner | Follow accepted many-to-many semantics through P1 | Durable new collection writes, not single-object retrieval |

No universal blocker follows from this table. Resolve a policy only when the
next proposed behavior needs it; continue independent work inside existing
authority. Product choices must not be smuggled into retry or cache code.

## 9 Verification plan and acceptance portfolio

### Representative scenarios

| Scenario | Required evidence |
| --- | --- |
| First ticket with no history | Recognizable original; correct subject uncertainty; no attendance inference; supported context optional |
| Passage and photograph | Retrieve exact support, inspect visual detail when necessary, preserve author and original |
| Film ticket and current screening | Historical connection and present availability use different freshness; discovery can find a new public candidate |
| Dish/menu/home attempt | Compare observable differences without inventing cooking technique or personal identity |
| Practical record | Correct units/arithmetic and conditions; no personality interpretation |
| Friend's original | Recipient value without reciprocal contribution; display and synthesis grants remain separate |
| Already stated connection | Avoid paraphrase; a new evidenced mechanism may still be worthwhile |
| No worthwhile addition | Original remains good; valid empty differs from failed/incomplete discovery |
| Day 1 capture, Day 2 edition, Day 5 arrival | New selection and stable kept edition coexist; correction/access affect availability correctly |
| Competing jobs and worker crash | Foreground capacity, reservation integrity, retry limits and stale-publication rejection |
| Account/grant change midflight | No old-account response/cache leak; stale authorization cannot publish or serve |

### Checks to reuse and extend

These are inspected starting points, not a declaration that all new acceptance
cases exist. Resolve current paths before execution.

- Backend Intake/originals: `tests/life/test_original_refind.py`,
  `test_original_refind_postgres.py`, Intake route/semantic-worker tests and
  `tests/api/test_original_delivery_content.py`.
- Backend research: `tests/research_agent/test_quick_research.py`,
  `test_disposition.py`, `test_source_result_metadata.py`,
  `test_worker_wiring.py`, `test_research_queue.py`, plus privacy assertions in
  `tests/concierge/test_trip_direction_research.py`.
- Source composition/execution: `tests/root_projection/test_source_contribution_*.py`,
  especially materials, opportunities, producer, canonical executor, workflow,
  serving and continuity; current owner tests and disposable-DB variants.
- Runtime/publication: `tests/core/test_source_contribution_attempts_postgres.py`
  for atomic publication and cancellation/takeover races;
  `tests/core/test_scheduled_tasks.py` for priority/recovery;
  `tests/api/test_entity_research_requests.py` for entity admission.
  `tests/places/test_budget_postgres.py` and `test_refresh_queue.py` cover their
  current budget/refresh behavior, not proposed concurrent reservations or
  universally enforced post-call deadlines.
- Memory: `tests/core/test_personal_memory_evidence.py`, preference subsystem
  tests and `tests/eval/test_memory_loop.py`.
- Quality: `tools/eval/plugins/retrieval/runner.py`,
  `tools/eval/plugins/research/runner.py`,
  `tools/eval/judges/source_contribution_editorial.py` and
  `core/vector/embedding_retrieval_evaluation.py` under backend. Keep their
  current non-personal/canary/provider authorities; new datasets need explicit
  scope rather than silently broadening an existing evaluator.
- Mobile: source-inspection/result, canonical-artifact and original-delivery
  data/screen tests, including `__tests__/data/originalDeliveries.test.tsx`,
  plus existing registered Home/Places/Life/original-reader QA contracts.

For each slice, follow [Backend Task Intake](../../../travel-agent/docs/operations/Task%20Intake.md)
and [Frontend Task Intake](../../../travel-app/docs/Task%20Intake.md). Schema/API
work is contract-sensitive; prompts/selection are prompt-sensitive; consumer
cache/navigation changes are generally parity-sensitive. Core authority and
unapproved schema/model-posture choices retain the named founder review.

Run focused offline checks during iteration. DB tests require explicit
`TEST_DATABASE_URL` and `TEST_DATABASE_DISPOSABLE=1`; do not probe or clean an
ambient database. Schema changes require the lane's `scripts/sync-types.sh`,
reviewed full/app projections, generated app types and `make api-coverage-check`.

Use the actual implementing checkout's backend `make ci-static` and
`make merge-check BASE_REF=<explicit-base>`, and app `npm run verify:fast`
and `npm run verify:merge -- --base <explicit-base>`. The workspace instructions
retain coordinated `make verify` at delivery. Reconcile evolving CI policy
through its owner; this plan neither waives required checks nor makes
experimental `verify-changed` a replacement by declaration.

For visible changes, validate the registered reference/build/data source before
native capture and structured review. Mock screenshots, synthetic DB/device
rehearsals, live-model quality and authenticated receiving prove different
things. A dry run does not prove pixels. No new visual exploration or SDK
migration is required by this roadmap.

### Measurements

Record p50/p95 time to recognizable original separately from time to useful
addition, with cold/warm conditions, queue/index lag and error rate. Account
for extraction, embeddings, research, model calls, retries, repair, storage and
prepared-but-unused results. Preserve unknown spend and ambiguous completion.

Measure support-set recall, selection relevance and repetition, claim support,
applicability and authority independently. Human comparisons should identify
the actual benefit and unwanted effort. Later natural use should assess
refinding, enjoyable return, reduced re-explanation, corrections and recipient
value—not merely daily opens or action conversion. No numerical latency/cost
SLO is asserted until representative runs measure it.

## 10 Migration consolidation and deferred work

Prefer additive request/result versions, adapters and reversible migrations.
Retain old source links and compatible readers until consumers migrate. Do not
backfill attendance, preference, new grants or occurrence time from capture time.

Inventory actual research callers before retiring anything. Catalog-backed
entity research, CLI queue drains, Source workflows and explicit questions have
different owners. A callable with no automatic trigger is not necessarily dead;
a trigger without an inspected deployed drain is not a complete live service.

As new bounded consumers adopt R1, remove duplicate provider invocation,
private-query serialization and cache logic only after parity. Do not delete
catalog anchoring, domain facts or exact original custody in the name of
on-demand research. Keep the legacy dossier path for its actual authorized
users until replaced or deliberately retired.

Defer by default:

- a universal world knowledge graph or speculative encyclopedia;
- a second context/memory/notification authority;
- automatic research teams or learned effort controllers;
- new preference embeddings or a separate personality store;
- continuous archive-wide public research and generation on ordinary reads;
- automatic group synthesis or shared retention without the relevant grant;
- a workflow-platform migration before existing recovery costs justify it;
- a new evaluation platform or an engagement reward based only on clicks.

Revisit each only when a named workload, failed simpler baseline and acceptable
cost/authority boundary establish the need.

## 11 Research sources and limits

Sources were investigated in the preceding parallel research round and checked
against this implementation audit. Dates describe publications/updates, not
Vesper implementation. Recommendations elsewhere are our engineering inferences.

| Source | Relevant finding and limit |
| --- | --- |
| [MIDR](https://arxiv.org/html/2609.01316v1), September 1, 2026 | Verified multimodal indexing can help text retrieval; ingestion cost and fine-detail visual advantages mean it is not a universal replacement for original inspection. Document benchmarks are not personal-photo evidence. |
| [SMMBench](https://arxiv.org/html/2605.15710v1), May 15, 2026 | Retrieval coverage and combining distributed multimodal evidence are separate failure points. More retrieved context can add noise. |
| [SerenQA](https://arxiv.org/html/2511.12472v1), November 2025 and AAAI 2026 | Relevance, novelty and surprise require separate evaluation. Biomedical graph discovery is not a consumer usefulness benchmark. |
| [Baikal](https://arxiv.org/html/2607.27726v1), July 30, 2026 | Diversified structured search is promising; more elaborate selection can overconcentrate. Small data-lake evaluation and model judgments limit transfer. |
| [Rerank Before You Reason](https://arxiv.org/html/2601.14224v1), January 20, 2026 | Retrieval/reranking can be a better intervention than additional reasoning under studied budgets. Fixed-corpus and model-family assumptions require local comparison. |
| [Agentic Abstention](https://arxiv.org/abs/2606.28733), June 27, 2026 | Timely stopping is a distinct agent capability; stronger models do not eliminate wasteful continuation or premature stopping. |
| [Time in XTDB](https://docs.xtdb.com/about/time-in-xtdb.html), living documentation | Valid time and recorded time separate historical correction from arrival order. Modeling precedent, not a database recommendation. |
| [Bazel Skyframe](https://bazel.build/reference/skyframe), living documentation | Incremental correctness depends on complete dependencies. Model nondeterminism and unobservable public-web changes limit direct analogy. |
| [HTTP caching RFC 9111](https://www.rfc-editor.org/rfc/rfc9111.html), June 2022 | Freshness/revalidation can avoid redundant acquisition. Representation validity is not claim truth. |
| [PairPref](https://arxiv.org/abs/2609.34526), September 28, 2026 | Valid preferences may be inappropriate in a changed situation. Very recent synthetic preprint; useful diagnostic cases, not established consumer evidence. |
| [RealPref](https://arxiv.org/abs/2603.04191v2), revised August 31, 2026 | Implicit and long-context preference use is difficult; synthetic users/model grading do not validate behavioral profiling. |
| [Managed Agents](https://www.anthropic.com/engineering/managed-agents), April 8, 2026 | Durable state and replaceable execution permit model upgrades and removal of obsolete interventions. Vendor experience report, not a hosted-platform selection. |
| [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence), living documentation | In-memory checkpoints do not establish process-restart recovery; checkpoint state and long-term personal memory are different. |
| [Temporal priority and fairness](https://docs.temporal.io/develop/task-queue-priority-fairness), living documentation | Queue priority and fairness differ; already-dispatched work constrains responsiveness. Existing Vesper workers should be measured before platform migration. |
| [Temporal activities](https://docs.temporal.io/activity-definition), living documentation | Retries after ambiguous completion can repeat effects; durable execution does not mean exactly-once provider charging. |
| [CaMeL](https://arxiv.org/abs/2503.18813v2), revised June 2025 | Runtime information-flow checks strengthen separation from untrusted content; guarantees depend on threat model and policy and do not cover every answer manipulation. |
| [ToolPrivacyBench](https://arxiv.org/abs/2606.28061), June 26, 2026 | Intermediate tool arguments can disclose unnecessary private information despite successful tasks. Mock workflow results do not establish Vesper's exposure rate. |
| [Zanzibar](https://www.usenix.org/conference/atc19/presentation/pang), July 2019 | Permission/content ordering matters for stale authorization. Reuse the property rather than Google's infrastructure. |
| [WorldMemArena](https://arxiv.org/abs/2605.29341v2), revised June 1, 2026 | Storage, maintenance, retrieval and use must be evaluated separately. Constructed histories are not longitudinal consumer proof. |
| [Agent evaluation guidance](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), January 9, 2026 | Combine deterministic, model and human grading and calibrate against outcomes; guidance is not causal product evidence. |

## 12 Document delivery and next handoff

The next implementation assignment should be **R0 plus the shared R1 boundary
and an existing-original R2 adapter**, admitted into artifact P0/P3 by the
program owner. It should establish the general seam, its privacy/cost evidence
and several artifact fixtures while preserving current native/capture progress.
This is a recommendation for the next checkpoint, not an instruction sent to
another lane and not a requirement to wait for every design or policy decision.

The document lives alongside the product-map references under the existing
`keep_reference` inventory rule. It does not replace the dated September 26
maps, modify their findings, or change the active program queue. When admitted,
move the detailed tasks into the appropriate owner/package and keep this as
the research/audit rationale; do not maintain duplicate live status tables.

**Documentation validation:**

- `python3 scripts/check_doc_governance.py docs/working/product-map/adaptive-context-and-research-roadmap-2026-09-29.md`
  passed. The combined `python3 scripts/check_docs.py --governance --inventory --links`
  also passed metadata and inventory checks, but failed on 16 broken links in
  other, unchanged documents. These are not fixed or waived by this task.
- Targeted link validation using the repository's living-link parser passed
  for this roadmap and `docs/README.md`.
- Scoped whitespace checks found no issue in the two files changed here.
  The repository-wide diff check reports an unrelated existing extra blank
  line at EOF in `docs/working/multiplayer-threads-life-continuity-response-2026-09-22.md:148`;
  that concurrent work is preserved.
- The measured combined-check receipt is at
  `/tmp/vesper-adaptive-research-roadmap-checks/measurements.json`. It records
  the checkout tuple, environment, command and failed link-check status;
  the temporary receipt is not a permanent verification archive.

Product tests, `make verify`, live-provider, database-race and native-device
checks remain **unrun** in this documentation-only investigation. Defined tests
and read-only reviewer agreement do not establish runtime acceptance.
