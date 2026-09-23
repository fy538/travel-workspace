---
doc_type: working
status: active
owner: founder / engineering
created: 2026-09-14
last_verified: 2026-09-14
expires: 2026-10-14
why_new: Records a code-grounded comparison of model execution, content production, mobile delivery and duplicated infrastructure; neither the generation charter nor a domain implementation roadmap owns this cross-system investigation.
supersedes: []
---

# Generation infrastructure and consolidation review

## Executive assessment

**Vesper has a substantial shared model-execution foundation, but not yet a consistently operated, reusable content-production lifecycle across its product.** We should build on the existing foundation, close specific lifecycle gaps, and retire superseded consumers—not introduce a new generation microservice or make every card its own generator.

The distinction matters. Most inspected text-generation paths already share provider access, model routing, prompt conventions, structured output, accounting and tracing. The fragmentation appears above that boundary: how work is admitted, scheduled, deduplicated, cached, invalidated, retried, retained and delivered. Several older surface-specific paths solve these questions differently. The newer Source contribution path solves many of them more rigorously, but remains a specialized, deliberately controlled path rather than the production system filling every designed section.[^1][^2][^3]

The strongest positive finding is that the current product architecture distinguishes canonical truth, human contributions, generated synthesis and their different presentations. That is exactly what the August pivot requires. The strongest negative finding is uneven lifecycle maturity: an excellent typed result and native renderer do not, by themselves, make useful content arrive reliably or economically.[^1][^4]

My recommendation is **shared execution mechanics, typed task-specific producers, existing domain ownership, and root-specific presentation**. Consolidation should deliver selected design features while reducing repeated implementation work. It should not become a repository-wide rewrite or postpone design completion.

## 1. Scope and evidence

This is an architectural investigation, not a deployment, refactor, production readiness certification or exhaustive security audit. No paid model/provider calls, live database inspection or product-code edits were performed. A provider-disabled local diagnostic inspected the registry and demonstrated two cache-key collisions. Other findings are static code/caller/configuration analysis; their evidence limits are stated below.

The primary checkout is the current receiving implementation lane, not the older canonical `main` checkout:

| Repository | Inspected revision |
| --- | --- |
| Workspace, `codex/receiving-completion-2026-09-10` | `a937f76f914a4f8d72030f28b5cff5cca7327bd0` |
| Backend in that coordinated lane | `b0d267c315b7cf295d491f86052b31bc7a967e76` |
| Mobile in that coordinated lane | `c5a80384e4f86048664ab7b72e7708e951642f31` |

All three were clean before creating this report. The situated-value lane was also compared at backend `8213bf82a3e612d7ffebff1011bd861262803d55`. Its inspected model wrapper, surface registry, Source producer, Source worker and Source continuity files are identical to the receiving lane. Its root selection/catalog differences are not evidence of another generation service. Neither comparison establishes that these revisions are deployed or on `main`.

The review followed representative paths across public-world material, private Source synthesis, conversational assistance, older Home/Atlas copy, media, background work and native rendering. It did not re-evaluate every Claude canvas or execute the full test suite. The existing roadmaps already distinguish design construction from actual-model quality and real supply; this investigation preserves that distinction.[^5]

## 2. What is genuinely centralized today

### Model and provider execution: a real reusable foundation

`backend/core/llm.py` exposes text, JSON, schema-based structured output and streaming. It resolves registered surfaces to model roles and providers, supports prompt metadata, handles provider-neutral messages and delegates actual transport to provider adapters. The canonical agent loop supports a different execution shape—multi-turn tool use—while sharing core infrastructure. It is not evidence that each agent invented an unrelated LLM SDK integration.[^2]

The inspected SDK call-site search places ordinary direct Anthropic/OpenAI client creation and transport inside designated core clients/adapters and the shared streaming/agent-loop paths. There is also an explicit provider-canary worker. The research pipeline's similarly named `call_llm_json` is a wrapper over core that adds research usage tracking, not a second model gateway. Sync compatibility likewise should not be removed merely because its name resembles the async entry point.[^2][^6]

The surface and prompt registries are useful existing extension points. A provider-disabled import found **86 declared surfaces**:

| Declared experience type | Count |
| --- | ---: |
| Live | 12 |
| Cached on request | 8 |
| Internal signal | 48 |
| Pre-generated on event | 13 |
| Human-gated | 2 |
| Deliberately no LLM | 3 |

These are declarations, not 86 customer features, activated generators or independent services. In particular, internal classification/extraction tasks should not be counted as feed-card generators. Registry presence also does not prove a caller is live or a declared strategy is implemented.[^3]

### Accounting exists; universal spend admission does not follow

`llm_accounting.py` records provider/model/token/cache/latency information with request, workflow and user lineage, and supports capability-level reporting. This is valuable shared infrastructure. Its writes are deliberately best-effort and asynchronous: they are observations after execution, not an atomic reservation that prevents overspending before a call.[^7]

There are also real controls elsewhere: research per-job call budgets, atomic daily-city reservation in Redis, voice quotas, and a commercial gateway with allowance reservations and settlement. These are not interchangeable. Customer benefit accounting, provider operational limits and shared supplier cost exposure answer different questions.[^6][^8]

### Worker transport and durable workflows already exist

The general Arq queue has one `WorkerSettings` entry point with multiple job categories. Durable agent workflows separately own request identity, leases, attempts, completion and recovery. Transport and durable business execution state are different layers; combining them into one universal table would not simplify their responsibilities.[^9]

There is no evidence here that Vesper needs another queue product or a separate deployment per content family. The first question should be whether existing durable work is connected to the existing worker correctly.

### Mobile has reusable receiving infrastructure

Home and Places share root-composition rendering and native anatomies for **evidence, sequence, comparison, spatial and prose**. They can vary density and presentation without inventing a second generated content owner. Source preparation/result hooks, exact-result navigation and root invalidation helpers also exist.[^4]

This is a useful basis for “one contribution, several expressions.” A new design section should generally need a producer/adaptor and its appropriate presentation—not a new endpoint, generation cache, polling protocol and result store by default.

## 3. Where generation capabilities diverge

| Family | Existing implementation | Assessment |
| --- | --- | --- |
| Immediate questions and assistance | Core LLM wrappers, shared agent loop, concierge and plan-assistance producers | Shared invocation is strong; task-specific context and consequences remain necessary. |
| Reusable public-world material | Research pipeline, reviewed content/dossiers, place-content primitives, Foundry promotion, existing Places/Home readers | Important shared supply; preparation, approved promotion and serving must stay distinct. |
| Private cross-source synthesis | `source_contribution_*`, composition compiler, durable attempts/results and exact readback | Strongest newer lifecycle example; specialized and not routinely worker-operated yet. |
| Older Home/Atlas copy | Hero/anchor copy, Pick, Settle, workbench voice, Atlas board-copy upgrades | Real duplication in caching/scheduling; disposition requires caller and product review. |
| Narration/audio/media | Guide prerender, audio jobs, voice stack, media rehosting/storage | Different resource and interaction constraints; reuse execution primitives, not one text-generation schema. |
| Canonical state and human sharing | Owner projections, factual adapters, attributed deliveries and notes | Much of this should not generate prose at all. |

### The newer Source pipeline is substantial—but narrower than “all generation”

The actual chain includes bounded opportunity discovery; exact owner reads; permitted source/context loading; known-claim history; structured generation; deterministic compilation; lease-backed reuse/persistence; current-authority revalidation; and Home/Places expression. It preserves source identity and keeps model-authored semantics separate from server-authored audience and authority.[^10]

The structured producer defaults to a three-evidence budget, 18,000 input characters, 3,200 output tokens, a 12-second deadline and up to two proposal attempts. It uses a registered LLM surface and provider-strict structured output, then hydrates immutable authority from the admitted seed. These are concrete implementation controls, not just policy prose.[^11]

It also deliberately models **multi-source synthesis**: selection requires at least two Sources, and the proposal schema requires synthesis claims with at least two supporting sources. That is appropriate for this contribution family. It is not an appropriate universal prerequisite for answering one question about one ticket, extracting a receipt, generating narration from an approved explanation, or rendering a friend's photograph.

The crucial operational gap: `POST /api/agent-workflows/source-contribution` persists a request but does not enqueue its execution. The worker adapter explicitly has no queue registration; the default deployment contract is `dark`. The runtime caller located in this checkout is the controlled rehearsal script, not a registered routine worker. The feature flag is off by default, and ordinary Home/Places GETs intentionally do not generate.[^12]

Therefore, **request/result plumbing and a working controlled executor are present; autonomous, routinely populated content supply is not established**. A future operating slice must connect bounded authorized triggers to this existing execution path. It must not solve that gap by moving provider calls into ordinary feed reads or silently enabling a flag.

### Shared surface policy is partly descriptive

The surface registry really drives model choice, status and temperature, and contributes to release/evaluation routing. But its schema explicitly says persistence is a target contract without a runtime reader, and context/tool/latency/fallback posture is declarative. Those fields do not automatically load safe context, enforce a deadline, cache an output or execute its fallback. Individual callers still implement those behaviors.[^3]

Similarly, common facts scanning is opt-in through a content contract key. The wrapper distinguishes logging from enforcement; a registered surface or schema-valid output is not blanket proof of fact correctness. The newer composition compiler adds substantive structural/authority checks, but typed “new to person” claims and repeat checks still do not establish that a model found an interesting, well-supported connection.[^13]

We should preserve good constraints while avoiding a false inference: **schema correctness, permission correctness, editorial quality and useful population are four different achievements**.

## 4. Confirmed consolidation candidates and engineering risks

### A. Surface-specific result-cache code — highest direct relevance

Older Home producers repeat L1 TTL lookup, Redis lookup, generation, serialization and cache-write logic. Pick and Settle explicitly describe mirroring other implementations. The problem is not the use of different TTLs; it is repeated mechanics with incomplete and inconsistent identity.[^14]

A local Python 3.13 probe, with `AI_MODE=off`, established:

```text
PICK_CHANGED_PROMPT_INPUT True
PICK_SAME_CACHE_KEY True
SETTLE_META_CHANGED_SAME_CACHE_KEY True
```

Pick's prompt includes candidate walking time, price and attributes, plus `place_label`. Its key includes decision and candidate identity/leading order, not those changing prompt values. Settle sends `structured.meta` to generation but omits it from its key. Consequently a cache hit can serve copy grounded in an earlier input. This is a code-level defect demonstration, not evidence of a measured production incident. It does not require a live model to reproduce.

The Takes fingerprint is a better existing reference: it incorporates memory/constraint/entity/group/prompt/model and place-projection dependencies. The Source pipeline additionally carries authority, provenance and correction dependencies. Neither should simply be pasted into every domain; their useful identity rules should become common mechanics with task-owned inputs.[^14][^15]

**Recommendation:** share a small typed result-reuse/fingerprint facility where active consumers need it. Include every output-affecting input, task/schema/prompt/model versions and appropriate audience scope. Preserve different freshness semantics, owner stores and author-edited histories. Do not put private generated prose in a public content cache.

Before investing in a legacy producer, decide whether its UI survives the design. If not, retire its callers and implementation when its replacement is complete instead of polishing a doomed service.

### B. Background copy upgrades and single-flight

Atlas board-copy upgrades use a separate fire-and-forget path and a Redis get-then-set inflight marker. The code explicitly admits this is not atomic. It also documents that absent Redis, reads miss and writes no-op while the upgrade job can still generate. With a configured model and a functioning dispatcher, this can spend on a result that cannot be reused; it is a reachable static failure mode, not a measured spend claim.[^16]

Ephemeral copy does not necessarily need a durable workflow. It does need deliberate behavior: an atomic best-effort lease if caching is useful, bounded concurrency, a cache-unavailable policy, and no repeated doomed upgrade on every read. Durable or user-requested results should use existing recoverable workflow machinery rather than fire-and-forget scheduling.

### C. Queue results and execution policy

The common `enqueue()` helper returns `None` for several different outcomes: successful inline completion, duplicate/no job returned, and refusal to run an expensive no-inline job when queue infrastructure is absent. Queue exceptions can also select inline fallback for eligible jobs. This is an ambiguous API even where individual callers safely recover from durable owner state.[^9]

**Recommendation:** improve this existing helper with explicit result outcomes and explicit per-job inline/failure policy. Preserve domain idempotency. Do not interpret “not queued” as “completed,” and do not add a second job framework. Worker retries, provider transport retries and structured-output retries should be accounted together under the work's deadline and cost envelope; a producer attempt is not necessarily one provider HTTP request.

### D. Transactional outbox mechanics

Memory, Life, itinerary, Intake and group propagation each contain outbox infrastructure. Side-by-side inspection of Memory and Life shows closely repeated SQL for due-row selection, `SKIP LOCKED`, lease-token assignment, acknowledgement, exponential backoff and cleanup.[^17]

There are meaningful differences: Memory fences a projection version; Life uses an event key, checks lease expiry on acknowledgement and records a dead-letter threshold. Intake also has bounded correction-fence continuation. Those are not details to erase with a generic base class.

**Recommendation:** consolidate tested claim/lease/ack/backoff primitives while keeping event schemas, canonical tables, generation predicates, transactional enqueue and domain handlers owned locally. Agree explicitly which lease and retry semantics are shared. Do not combine every outbox into one universal event table as a first step. This is worthwhile engineering-quality work, but ranks behind generation reuse/dispatch for immediate content completeness.

### E. Budget admission is fragmented

The provider/model ledger, Source per-attempt limits, research budgets, voice quotas, Places provider counts and commercial allowance holds are all useful, but they do not jointly establish an enforced shared generation spend envelope.

One concrete difference: Places checks a daily count before the call and records the call afterward. That is a soft admission check under concurrency, unlike an atomic reservation. Research's daily-city cap has already advanced to an atomic Redis Lua reservation. Reusing the reservation pattern is more useful than creating another counter for each new producer.[^8]

**Recommendation:** use compatible reservation/idempotency/deadline mechanics for metered execution, with separate policy and accounting scopes. Keep user allowances distinct from supplier exposure. Preserve uncertain provider outcomes for reconciliation rather than treating all timeouts as free failed work. The existing supply roadmap already names this unfinished supplier-cost boundary; do not implement a competing ledger casually.[^5]

### F. Semantic lookup cache is not a template for personal generation

The lookup cache reuses an `answer` plus raw data from semantically similar queries. Its filter uses city and freshness; `query_type` determines TTL but is not a matching filter. The agent returns cached prose before resolving the current venue. The hit branch also does not forward the source list supplied on a fresh response.[^18]

This does not establish a personal-data leak—the inspected synthesizer does not receive personal memory. It does establish a different and weaker reuse contract than exact-subject, evidence-versioned Source results. Cross-intent/entity reuse and citation preservation deserve a focused correction before extending this path. Approximate search can find candidate evidence; final personalized or operational claims should be rebuilt or revalidated against exact current owners.

### G. Legacy/current composition coexistence — disposition, not blind merging

`backend/composition` is the older Atlas board assembler; the newer composition compiler is rooted in Source/claim/authority contracts. They are not two equivalent implementations of the same semantics. Likewise, `content_surfaces.py` normalizes delivery addresses, while `core/surfaces` governs LLM execution. Similar names are not enough reason to merge them.[^19]

The old workbench is still consumed by the Chat/concierge root. Its Here/Season catalogs also contribute useful existing material. Removing `vesper_workbench` because it is “old Home” would remove more than a superseded Home screen. Route registration, current mobile callers and API-operation governance must determine retirement scope.[^20]

The actual cleanup opportunity is to retire superseded orchestration, copy and screen-specific contracts as selected replacements take ownership, while retaining shared material and domain capabilities. Do not preserve an operational booking surface merely because its generator exists; also do not delete a live reader merely because a newer Home renderer exists.

## 5. What should not be consolidated

Keep these distinctions explicit:

- **Public-world preparation and private synthesis.** Foundry validates reviewed promotion into canonical truth; it explicitly does not promote editorial drafts. Research acquisition, approved editorial material and private composition have different authority and reuse rights.[^21]
- **Facts and language.** Time, availability, route geometry, calculations and confirmation state stay owner/provider facts. A model can explain them, not replace their truth or arithmetic.
- **Human expression and AI expression.** A friend's photograph can be valuable without an AI caption or novelty test. Generation must not impersonate relational effort.[^1]
- **Live chat and asynchronous production.** They may share adapters and budgets without sharing latency, cancellation, tool access or retention contracts.
- **Text, audio and photographs.** Narration scripts can derive from an approved contribution, but TTS, audio storage and photo rights/transforms remain specialized. The media package is principally image acquisition/processing, not evidence of a general image-generation service.[^22]
- **Meaning and presentation.** A common result may become Home's comparison and Places' spatial explanation. It should not force identical cards or one generic renderer for every domain instrument.[^4]
- **Durable author work and regenerable caches.** A retained edited artifact cannot be overwritten according to the same policy as disposable status copy.

## 6. Target architecture: extend existing layers, not another platform

The following is a responsibility map, not a request to create seven new services:

```text
Existing owners and permitted public/private evidence
             ↓
Purpose-specific selection and context assembly
             ↓
Task-specific producer using shared execution mechanics
  registry • identity/reuse • budget • deadline • retries • transport
             ↓
Task-specific validation and existing owner persistence
             ↓
Current-authority readback and candidate admission
             ↓
Home / Places / Chat / Life / object-specific expression
```

A producer should declare its job, required evidence, output type, authority scope, resource envelope, reuse identity, failure posture and result owner. It should supply its specialized prompt/tool procedure and validator. Common code should own mechanics that are demonstrably repeated. The existing registry is the starting identity, not grounds for adding a competing “generation registry.”

The reusable seam should not be `generate_card(card_type, user)`. That binds intelligence to layout and invites a separate prompt/cache for every section. Nor should it be `generate_anything(context)`, which hides authority and useful output guarantees. A comparison, an explanation and a prepared practical response can share execution without sharing the same reasoning procedure or evidence requirements.

A useful first extraction can serve two genuinely different retained-content consumers. That tests the abstraction against the system's breadth while delivering product work; it does not make one loop the product architecture or require migrating every producer first.

## 7. How a rich Home avoids generating everything

The product canon is already clear that canonical state, an operational instrument, human contribution and Vesper synthesis are separate value lanes. The engineering consequence is substantial: **a longer valuable feed does not imply one model call per card, per person, per refresh**.[^1]

| Designed value | Sensible production strategy |
| --- | --- |
| A nearby event, opening hours, saved place or current Plan | Retrieve current typed records and project them; no LLM required. |
| A friend's shared photograph or note | Deliver the authorized original with attribution; no compulsory synthesis. |
| A useful place explanation | Reuse approved public material; generate only when new material is justified. |
| Sorrento cliffs contrasted with another place | Ground a mechanism/difference in permitted evidence, generate one contribution, retain/revalidate it, express it appropriately. |
| “Can this work before dinner?” | Compute/check timing and constraints; optionally generate a concise explanation of the actual result. |
| A trip route/timeline | Assemble canonical occurrences and geometry; make interpretation an optional separate contribution. |
| Narration of an explanation | Reuse its supported script/content, render audio when requested or otherwise authorized. |

Personalization can change selection, the relevant contrast, practical consequences or expression depth without rewriting every fact. Public material can be shared where its rights allow; personal overlays and friend material cannot inherit that public reuse scope.

Ordinary reads should serve current prepared material and deterministic value. Authorized preparation should occur through explicit work or later bounded event policy. More feed capacity must not become a quota that produces filler. Missing evidence may mean a missing supply source, a missing admitted producer, a selection problem or a presentation gap; those require different fixes.

## 8. Recommended engineering sequence

### First: use one feature-to-producer disposition map

Attach selected Home/Places and adjacent design sections to existing owners and classify each as deterministic state, original human material, reusable public content, private synthesis or generated media. Name actual caller, result owner, current activation and missing connection. Add this to the existing lane coverage material rather than starting a new roadmap.

This prevents two expensive mistakes: implementing a custom generator for a factual card, and calling a section complete because a fixture renderer exists.

### Second: consolidate mechanics while completing real consumers

Choose two currently needed generated-content families, with at least one outside the exact multi-source Source case. Reuse the current LLM/surface/workflow foundations. Implement only the shared fingerprint, result-reuse and dispatch mechanics their real differences require; retain task-specific input/output validators and domain storage.

Fix the demonstrated cache-input omissions for surviving consumers. If the selected designs retire those consumers, remove their callers and cache code when the replacement is ready. A stronger abstraction is valuable only if it replaces active duplication, not if it sits beside it.

### Third: finish the operating connection for supported production

Connect supported explicit work to the existing worker and recoverable outcome/readback, with bounded scheduling, cost policy, cancellation and queue-unavailable behavior. Preserve default-off activation until its existing gate is met. Runtime activation and paid production remain separately authorized; offline implementation and design completion need not wait for credentials.

Do not promise broad proactive content until trigger coverage, refresh/correction behavior and useful yield exist. Conversely, do not postpone the UI features that can already consume public material, canonical facts or originals.

### Fourth: reduce repeated infrastructure in bounded batches

Extract the repeated outbox primitives, rationalize queue-result semantics, and apply shared reservation mechanics where parallel metered execution needs them. Prioritize active paths and known failure modes, not similar filenames. Preserve distinct ledgers, source policies and owner-specific transaction boundaries.

### Fifth: assess usefulness and economics through assembled experiences

When real-model/supply evaluation is authorized, measure accepted useful results, repeat-read reuse, regeneration after relevant change, queue age, duplicate provider work and cost per useful delivered result. Record unknown charges and failures. Do not use token volume, schema-valid outputs or green fixtures as substitutes for worthwhile receiving.

Verification belongs inside these delivery slices: targeted key/lease/correction tests, focused backend-to-consumer checks where behavior crosses that boundary, and native inspection for changed presentation. This investigation does not recommend a separate testing-platform program or undo the roadmap's feature-completeness priority.

## 9. Documentation corrections to make with the owning changes

There is demonstrable map-versus-code drift:

1. The August 28 generation charter says there is no shared runtime for the contribution brief/known-to-person checks or page admission. The newer Source/compiler/root work now implements parts of those concerns. Replace absolute absence with a scoped maturity statement when the owner is updated; do not claim universal semantic novelty enforcement.[^10][^13]
2. The workers FEATURE still describes the daily seed cap as process-local; current code has an atomic Redis reservation with fallback. Correct the doc, not the code back toward the old description.[^8][^9]
3. The older consolidation plan contains phased proposals and historical cache/model assumptions that no longer describe the tree uniformly. Its status also contains fixes and deferrals that supersede earlier recommendations. It is research provenance, not an instruction to execute the old platform program.[^19]
4. Registry fields and release manifests should distinguish enforced behavior from declarations. Adding metadata without a runtime consumer must not appear as implemented generation capability.[^3]

This review itself does not adopt a new product policy, amend the canonical charter or reorder execution automatically. It supplies the evidence for a focused update of the existing roadmap and owners.

## 10. Bottom line

The foundation is worth building on. Vesper is not fundamentally a collection of independent LLM services with no common architecture. But it is also not yet a mature content-production platform that can populate the ambitious design simply by adding prompts.

The next improvement should make a **new content capability cheap to implement correctly**: mostly task-specific evidence and reasoning, using shared execution, reuse and delivery mechanics. Pair that improvement with shipping selected design content and removing the duplication it supersedes. Keep public facts, private meaning, human relationships and practical execution under their proper owners.

## Sources and verification notes

All sources below are repository-primary evidence at the revision tuple in §1. A source link is not a claim of current deployment. This review used code search, caller inspection, documentation comparison and one provider-disabled Python diagnostic. No model-quality, load, paid-provider or full integration tests were run. The registry count is an executed inventory; the two cache cases are executed pure-function probes; other risks are static findings.

[^1]: [Product Thesis](../../travel-agent/docs/product/Product%20Thesis.md), [Product Model](../../travel-agent/docs/product/Product%20Model.md), and [Editorial and Content Canon](../../travel-agent/docs/product/Vesper%20Editorial%20and%20Content%20Canon.md), especially value lanes, contribution fit, memory, Home and admission; [generation charter](../systems/content-generation.md).
[^2]: [LLM wrappers](../../travel-agent/backend/core/llm.py), [agent loop](../../travel-agent/backend/core/agent_loop.py), [model registry](../../travel-agent/backend/core/model_registry.py), [client factory](../../travel-agent/backend/core/llm_client.py), [Anthropic adapter](../../travel-agent/backend/core/providers/anthropic_adapter.py), [OpenAI adapter](../../travel-agent/backend/core/providers/openai_adapter.py), [prompt registry](../../travel-agent/backend/core/prompts/registry.py).
[^3]: [Surface schema](../../travel-agent/backend/core/surfaces/schema.py), [catalog](../../travel-agent/backend/core/surfaces/definitions.py), [registry](../../travel-agent/backend/core/surfaces/registry.py), [release manifest](../../travel-agent/backend/core/surfaces/release_manifest.py). Local import of `SurfaceRegistry.all()` under `AI_MODE=off`, Python 3.13.0, returned the counts in §2.
[^4]: [Root composition renderer](../../travel-app/components/root-projection/RootCompositionRenderer.tsx), [native media support](../../travel-app/utils/rootCompositionMedia.ts), [Source result hook](../../travel-app/hooks/useSourceContributionResult.ts), [root invalidation](../../travel-app/utils/invalidateRootProjections.ts), [Home source adapters](../../travel-agent/backend/root_projection/v2/home_source_adapters.py).
[^5]: [Program roadmap](vesper-program-roadmap.md), [technical integration roadmap](complete-system-integration-roadmap-2026-09-05.md), [world-supply roadmap](recommendation-world-supply-architecture-and-roadmap-2026-09-07.md), particularly the September 11 disposition and supplier-cost boundary.
[^6]: [Research wrapper and budget scope](../../travel-agent/backend/research_agent/pipeline/llm.py), [sync wrapper](../../travel-agent/backend/core/llm_sync.py), [shared retry policy](../../travel-agent/backend/core/llm_retry.py).
[^7]: [LLM accounting](../../travel-agent/backend/core/llm_accounting.py), especially `_insert_sync`, `schedule_call`, `record_wire_success` and capability attribution; [AI-mode guard](../../travel-agent/backend/core/ai_mode.py), whose live mode is not a shared spend reservation.
[^8]: [Research atomic seed reservation](../../travel-agent/backend/workers/research_jobs.py), `_reserve_daily_seed_budget`; [Places budget](../../travel-agent/backend/places/budget.py), `can_call` and `record_call`; [commercial control plane](../../travel-agent/backend/core/commercial_access/FEATURE.md), [usage ledger](../../travel-agent/backend/core/commercial_access/usage_ledger.py), [voice quota](../../travel-agent/backend/voice/quota.py).
[^9]: [Job queue](../../travel-agent/backend/core/job_queue.py), especially `enqueue` and `_NO_INLINE_JOBS`; [worker registration](../../travel-agent/backend/workers/audio_jobs.py), [workers FEATURE](../../travel-agent/backend/workers/FEATURE.md), [durable workflow repository](../../travel-agent/backend/core/db/agent_workflows.py).
[^10]: [Source discovery](../../travel-agent/backend/root_projection/v2/source_contribution_discovery.py), [pipeline](../../travel-agent/backend/root_projection/v2/source_contribution_pipeline.py), [compiler](../../travel-agent/backend/root_projection/v2/source_contribution.py), [continuity](../../travel-agent/backend/root_projection/v2/source_contribution_continuity.py), [serving](../../travel-agent/backend/root_projection/v2/source_contribution_serving.py), [canonical executor](../../travel-agent/backend/root_projection/v2/source_contribution_canonical_executor.py).
[^11]: [Structured Source producer](../../travel-agent/backend/root_projection/v2/source_contribution_producer.py), `_source_contribution_decision_schema`, `_hydrate_decision`, `SourceContributionProducerBudgetV1` and `StructuredSourceContributionProducer`.
[^12]: [Source request/result routes](../../travel-agent/backend/api/routes/agent_workflows.py), `submit_source_contribution_request`; [worker adapter](../../travel-agent/backend/root_projection/v2/source_contribution_worker.py); [deployment contract](../../travel-agent/backend/core/models/source_contribution_worker.py); [feature flags](../../travel-agent/backend/core/feature_flags.py); controlled rehearsal caller `scripts/provision_context_shaped_source_rehearsal.py` at the inspected revision (not present in current main).
[^13]: [Facts-contract wrapper](../../travel-agent/backend/core/llm.py), `_apply_facts_contract`; [known-to-person implementation](../../travel-agent/backend/root_projection/v2/known_to_person.py), [semantic compiler](../../travel-agent/backend/root_projection/v2/semantic_composition.py), [Source compilation](../../travel-agent/backend/root_projection/v2/source_contribution.py).
[^14]: [Pick judgment](../../travel-agent/backend/home/pick_judgment.py), `_candidate_line`, `compose_pick_judgment`, `_content_key`; [Settle take](../../travel-agent/backend/home/deck_take.py), `compose_settle_take`, `_settle_content_key`; [hero/anchor copy caches](../../travel-agent/backend/home/compose.py). Pure-function probe changed the same candidate's walk from `5 minutes` to `45 minutes` and price from `$` to `$$$$`; prompt candidate text changed and the key did not. Changing Settle `meta` likewise preserved the key.
[^15]: [Takes fingerprint](../../travel-agent/backend/core/takes/cache.py), [Source persistence](../../travel-agent/backend/core/db/source_contributions.py).
[^16]: [Atlas copy cache](../../travel-agent/backend/composition/copy_cache.py), `_upgrade_job`; [board-copy generator](../../travel-agent/backend/composition/core.py), `_llm_copy`; [Atlas caller](../../travel-agent/backend/atlas/taste_board.py).
[^17]: [Memory outbox](../../travel-agent/backend/core/db/memory_projection_outbox.py), [Life outbox](../../travel-agent/backend/core/db/life_projection_outbox.py), [itinerary outbox](../../travel-agent/backend/core/db/itinerary_mutation_outbox.py), [Intake outbox](../../travel-agent/backend/core/db/intake_outbox.py), [group outbox](../../travel-agent/backend/core/db/group_message_outbox.py).
[^18]: [Lookup cache](../../travel-agent/backend/lookup_agent/cache.py), `check_cache`; [lookup agent](../../travel-agent/backend/lookup_agent/agent.py), cache-hit branch; [synthesizer](../../travel-agent/backend/lookup_agent/synthesizer.py).
[^19]: [Older composition owner](../../travel-agent/backend/composition/FEATURE.md), [delivery-address normalization](../../travel-agent/backend/core/content_surfaces.py), [historical consolidation design](../../travel-agent/docs/architecture/vesper-consolidation/Design.md), [consolidation status](../../travel-agent/docs/architecture/vesper-consolidation/STATUS.md).
[^20]: [Chat root's workbench consumer](../../travel-app/app/%28tabs%29/concierge/index.tsx), [workbench owner](../../travel-agent/backend/home/vesper_workbench/FEATURE.md), [legacy concierge Home route](../../travel-agent/backend/api/routes/concierge_home.py), [API-operation policy](../governance/api-operation-policy.json).
[^21]: [Foundry owner](../../travel-agent/backend/world_foundry/FEATURE.md), [public Home adapters](../../travel-agent/backend/root_projection/v2/home_source_adapters.py), [public Places adapters](../../travel-agent/backend/root_projection/v2/adapters.py).
[^22]: [Media owner](../../travel-agent/backend/media/FEATURE.md), [voice owner](../../travel-agent/backend/voice/FEATURE.md), [guide prerender](../../travel-agent/backend/guide/prerender.py).
