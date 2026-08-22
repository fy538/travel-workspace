---
doc_type: working
status: active
owner: product / AI systems / mobile / backend / evidence
created: 2026-08-16
last_verified: 2026-08-16
expires: 2026-09-15
why_new: Converts the current in-chat artifact audit and external research into a bounded cross-repo execution program for artifact selection, durable action truth, owner-surface handoff, evaluation, and rollout.
promotes_to: null
supersedes: []
related:
  - in-chat-artifact-system-inventory-and-sota-research-2026-08-12.md
  - product-loop-coherence-maestro-and-environment-strategy-2026-08-12.md
  - ai-decision-and-learning-engineering-plan-2026-08-10.md
  - ../Card Catalog.md
  - ../../travel-app/docs/working/vesper-conversational-artifact-language-native-implementation-plan-2026-08-14.md
  - ../../travel-app/docs/working/chat-artifact-language-phase-5-mac-agent-2026-08-15.md
  - ../../travel-app/docs/surfaces/vesper-chat/contract.md
  - ../../travel-agent/backend/concierge/FEATURE.md
---

# Chat artifact closed-loop optimization plan

> **Execution-ready working plan, not permanent authority.** This document
> coordinates changes that belong to three repositories and several existing
> authorities. Accepted product policy must be promoted into the Card Catalog
> and concierge guidance. Accepted mobile behavior must live in the Vesper Chat
> surface contract. Accepted backend behavior must live in the concierge
> feature/eval contracts. This document should expire after those promotions.

## 1. Executive decision

The next artifact program should **not** be another broad visual redesign, a
universal-card rewrite, or a migration to A2UI/AG-UI/MCP Apps. The current
native renderer, typed attachment registry, bounded declarative card, durable
message mapping, lifecycle language, and four golden families are a strong
substrate.

The missing layer is closed-loop reliability:

```text
user intent
  -> artifact warranted?
  -> correct family and producer selected
  -> one structured projection persisted
  -> client reveals the exact durable projection
  -> explicit action reaches the canonical domain authority
  -> known commit, known failure, or honest uncertainty
  -> owner surface renders canonical truth after refresh
  -> a later turn resumes the object instead of reposting it
```

The program therefore has five outcomes:

1. one unambiguous artifact-selection and prose-complement policy;
2. truthful payload, action, lifecycle, and telemetry contracts;
3. a strict artifact-decision eval suite that is harder to satisfy than a
   self-authored agent judgment;
4. four real journeys proving chat-to-owner state after refresh; and
5. calibrated visual and production evidence without expanding all twenty
   artifact families.

The renderer should be considered **presentation-ready but not yet
loop-certified** until all five outcomes pass.

## Execution receipts (2026-08-16)

- G0 base check: `make status` and `make doctor` passed. The local Postgres
  lane is reachable at the canonical Docker DSN. The primary `travel-app`
  checkout is intentionally left untouched because concurrent Places/profile
  work is dirty there; mobile artifact work uses
  `travel-app--artifact-closed-loop` instead.
- Historical composed-card audit (read-only local database query): **0**
  composed-card rows and **0** rows with more than two actions. Tightening the
  mobile parser therefore needs no legacy read adapter in the local certifying
  dataset. Production remains a separately required read-only audit before
  rollout.
- G1 implemented on the dedicated backend/mobile branches: prompt and
  capability policy, a two-action server/client contract, no renderer action
  truncation, uncertainty-capable telemetry vocabulary, and callback/resolver
  events that do not claim durable commit or owner render.
- G2 started with a strict deterministic `artifact_contract` evaluator and
  four existing high-signal scenarios. The 48-row independently worded corpus,
  retrieval comparison report, domain readback instrumentation, and real
  owner-surface journeys remain open gates; they are not claimed complete by
  the commits recorded here.

## 2. Baseline and concurrency boundary

### 2.1 Inspected revisions

| Repository | Revision | Branch/state at planning time |
| --- | --- | --- |
| workspace | `5c275a80de2e7eed0b4e514d92f22381bb236fe5` | `main`, three commits ahead of `origin/main` |
| backend | `21b288e3a341bf7b58f2ab210d15057dedc8be7c` | `main`, two commits ahead of `origin/main`, clean |
| mobile | `b523bcb65d5390ebae7f58a31b72106a82483ef2` | `codex/profile-polish-pass`, concurrent uncommitted profile/trust-control QA work |

This plan does not treat the mobile branch as an implementation lane. Before
mobile artifact work starts, either let `codex/profile-polish-pass` settle or
create a dedicated app worktree from an explicitly recorded base SHA. Never
stage its profile/trust-control files into artifact commits.

### 2.2 Verified artifact baseline

On 2026-08-16 the following commands passed in `travel-app`:

```bash
npm run chat-artifacts:test --silent                 # 12/12
npm run chat-artifacts:language:check --silent       # pass
npm run design:chat-artifacts:check --silent         # audit/handoff current
npm run chat-artifacts:check --silent                # 20 types; 4 golden journeys
```

The current inventory reports:

| Measure | Current |
| --- | ---: |
| registered artifact types | 20 |
| executable golden journeys | 4 |
| artifact types with requirement-only lifecycle coverage | 16 |
| artifacts requiring action-budget review | 5 |
| required native artifact evidence views | 26 |
| locally captured core artifact views | 22 |
| locally missing artifact views | 4: three xxxLarge, one 320pt |
| accepted/tracked artifact evidence | 0/26 |

Passing conformance checks proves that code, inventories, fixtures, and design
references agree. It does not prove correct agent selection, domain mutation,
owner-surface state, or visual acceptance.

## 3. Product contract to lock before implementation

### 3.1 Artifact role

An artifact is a compact stateful projection, control, or receipt that helps a
user move work toward a durable owner. It is not an automatically generated
mini-app and is not valuable merely because information can be card-shaped.

An artifact is warranted when it does at least one of these jobs better than
prose:

- identifies a grounded object that can be revisited;
- exposes a small, consequential choice;
- makes progress, uncertainty, or recovery inspectable;
- lets the user steer without writing another prompt;
- proves that canonical state changed and provides a return path.

Plain prose is preferred when the response is explanatory, relational,
ephemeral, or has no useful state/action/owner.

### 3.2 Turn grammar

Lock this default rule:

> A single assistant turn emits at most one primary structured artifact.
> Alternatives live inside that artifact. Prose introduces, interprets, or
> qualifies it but does not restate the same payload.

Explicit exceptions:

- a progress projection may later be superseded by a result projection with
  the same object identity/version lineage;
- a distinct settlement receipt may arrive after a user action, but it must
  replace or clearly supersede the actionable state rather than stack as an
  unrelated recommendation;
- background system notices are not counted as a second assistant judgment,
  but must not visually compete with it.

The policy must resolve the current conflict between the “one card per moment”
guidance in `backend/concierge/_prompts_skill_cards.py` and the one-to-three
venue-card guidance in `backend/concierge/_prompts_skills.py`.

### 3.3 Four state layers

Do not use one generic “message complete” state for all meanings. Maintain four
explicit layers:

| Layer | Example | Authority |
| --- | --- | --- |
| agent trajectory | tool selected, tool result returned | agent trace/eval |
| durable projection | structured message persisted with identity/version | conversation/message store |
| domain outcome | save, Plan version, vote, booking, or reaction persisted | owning domain |
| client interaction | ready, acting, committed, failed, uncertain, reconciling | mobile state machine |

The product reports success only when the relevant domain outcome is observed.
A tool result or resolved callback is not, by itself, a durable commit.

### 3.4 Action and owner grammar

Every active artifact must declare:

- audience: private or group;
- lifecycle state;
- durable owner or explicitly `none`;
- permitted operation class: inspect, steer, mutate, confirm, revert, open;
- authoritative postcondition;
- failure and uncertainty behavior;
- return path;
- maximum visible action count.

For `composed_card.v1`, lock a maximum of **two** actions: at most one primary
and at most one secondary. The server and client schemas must agree. The client
must never silently discard a valid server action.

## 4. Program boundaries

### 4.1 In scope

- selection policy and prompt/capability consistency;
- strict deterministic eval checks and a focused scenario corpus;
- contextual tool-retrieval comparison and promotion gate;
- composed-card action-contract truth;
- uncertainty-preserving telemetry;
- durable mutation and owner-render instrumentation;
- four real end-to-end artifact journeys;
- completion and skeptical adjudication of the 26-view native matrix;
- selective follow-up on the five highest-risk remaining families;
- authority/documentation reconciliation.

### 4.2 Out of scope

- adopting A2UI, AG-UI, or MCP Apps as a new transport;
- replacing specialized proposal, booking, or receipt components with a
  universal card;
- arbitrary model-authored routes, styles, callbacks, or executable UI;
- redesigning all twenty artifact types;
- creating a new durable shortlist aggregate before evidence demands it;
- making onboarding depend on the artifact program;
- changing tuned prompts solely to make screenshots easier;
- resurrecting Discover or Atlas as active owners;
- production-wide retrieval enforcement before shadow and eval gates pass.

### 4.3 Research constraints carried into execution

The plan deliberately borrows principles without adopting another protocol:

- Google A2UI keeps model output declarative and gives the trusted client
  control of native components, rendering, style, security, and accessibility.
  That supports the existing bounded-blueprint/native-registry architecture,
  not an unconstrained renderer:
  [A2UI introduction](https://developers.googleblog.com/introducing-a2ui-an-open-project-for-agent-driven-interfaces/).
- Vercel separates model-facing messages from complete application UI state.
  That supports the four state layers in section 3.3:
  [UIMessage](https://ai-sdk.dev/docs/reference/ai-sdk-core/ui-message).
- Anthropic recommends evaluating tool selection on representative tasks,
  combining deterministic/model/human graders, and using multiple trials for
  nondeterministic agent behavior. That drives G2 and G3:
  [tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool),
  [agent evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents),
  and [tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents).
- Human-AI interaction guidance emphasizes visible consequences, graceful
  correction, and appropriately calibrated control. That is why a tap is not
  considered complete until its canonical result can be inspected:
  [Microsoft human-AI guidelines](https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/)
  and [Google PAIR feedback and control](https://pair.withgoogle.com/chapter/feedback-controls/).

These sources validate the direction; they do not prove Vesper’s product
metrics. The gates below supply the Vesper-specific evidence.

## 5. Gate G0 — establish an uncontested execution base

**Effort:** half a day.

**Owner:** root integrator.

**Mutations:** workspace planning/status only.

### Tasks

1. Record final workspace/backend/mobile base SHAs after current app work
   settles.
2. Run `make status`, `make doctor`, and the four artifact checks above.
3. Record current relevant feature flags and environment defaults, especially
   contextual retrieval mode and mock/real API mode.
4. Verify that no artifact implementation work is occurring in the chosen
   app/backend files on another branch or worktree.
5. Create dedicated worktrees with descriptive branches rather than editing
   the current profile branch.
6. Capture a baseline audit JSON and store the command receipt; do not rewrite
   inventories merely to produce a new timestamp.

### Exit gate

- base SHAs and dirty-file ownership are explicit;
- all conformance checks pass or failures are classified before implementation;
- one integrator owns shared schemas, manifests, and final promotion;
- implementation agents have non-overlapping worktrees and file ownership.

## 6. Gate G1 — repair contract truth

**Effort:** one to two days.

**Owners:** backend contract owner + mobile state owner + root integrator.

**Risk:** medium; includes a tuned-prompt decision and a cross-repo schema bound.

### WP1.1 — lock the selection policy

Likely backend touchpoints:

- `backend/concierge/_prompts_skill_cards.py`;
- `backend/concierge/_prompts_skills.py`;
- prompt golden snapshots under `tests/concierge/golden_prompts/`;
- `backend/concierge/FEATURE.md`;
- workspace `docs/Card Catalog.md`.

Steps:

1. Add the turn grammar to the Card Catalog as product policy.
2. Enumerate the current prompt fragments that describe card count, venue
   recommendation, group choice, and progress/result behavior.
3. Resolve contradictions without broad prompt rewriting.
4. Regenerate or update prompt snapshots only after product approval because
   backend instructions classify tuned-prompt changes as ask-first.
5. Add static tests that fail if “up to three venue cards” or equivalent
   stacking language reappears in active prompt composition.

Acceptance:

- delegated recommendation produces one committed venue artifact;
- genuine group tradeoff produces one decision/reaction artifact containing
  the alternatives;
- explanation-only turns can remain prose;
- follow-up on an existing artifact updates or refers to it rather than
  reposting the same object.

### WP1.2 — eliminate the composed-card action mismatch

Backend touchpoints:

- `backend/core/models/chat_card_blueprints.py`;
- `tests/core/test_chat_card_blueprints.py`;
- OpenAPI snapshot generated through the workspace workflow.

Mobile touchpoints:

- `utils/chat/cardBlueprint.ts`;
- `components/chat/ComposedChatCard.tsx`;
- `__tests__/components/chat/ComposedChatCard.test.tsx`;
- generated `utils/api/schema.gen.ts` only through code generation.

Steps:

1. Run a read-only audit for already-persisted `composed_card` rows with more
   than two actions; record the count and versions before changing validation.
2. Change the new-write canonical action bound from three to two.
3. Express “at most one primary and at most one secondary” in server validation.
4. Mirror the bound in the mobile Zod parser when no historical rows require a
   compatibility read. If historical rows exist, keep a narrow, documented
   read adapter that renders every legacy action or uses explicit text fallback;
   do not silently truncate it.
5. Remove the renderer’s silent `.slice(0, 1)` loss behavior.
6. Replace the test that celebrates hiding a third action with rejection tests
   at both contract boundaries.
7. Run `./scripts/sync-types.sh` from the workspace root and review both OpenAPI
   snapshots and generated mobile types.

Acceptance:

- a new three-action payload fails server validation;
- malformed historical content degrades to useful text fallback rather than
  partially changing meaning;
- every accepted action is rendered or explicitly unavailable;
- contract checks and generated types are current.

### WP1.3 — preserve uncertainty in telemetry

Mobile touchpoints:

- `utils/chat/artifactTelemetrySemantics.ts`;
- `components/chat/ChatCardTelemetryContext.tsx`;
- `components/chat/AttachmentRenderer.tsx`;
- `__tests__/utils/chat/artifactTelemetrySemantics.test.ts`;
- `__tests__/components/chat/ChatCardTelemetryContext.test.tsx`.

Steps:

1. Add `uncertain` to the telemetry lifecycle vocabulary.
2. Keep retryable failure distinct from uncertain reconciliation.
3. Rename or reinterpret `chat_card_action_completed` as
   `resolver_returned` unless a domain postcondition is actually observed.
4. Preserve existing event compatibility for dashboards during a short dual
   emission window if production consumers already rely on it.
5. Ensure event fields remain content-free.

Acceptance:

- `failed`, `uncertain`, `reconciling`, `committed`, and `superseded` can be
  separated in product metrics;
- no UI callback is counted as a domain commit without a postcondition;
- uncertain actions remain locked until reconciliation or explicit recovery.

### WP1.4 — make the evidence ledger honest

1. Update the Vesper Chat contract from the audit’s current five, not seven,
   action-budget findings.
2. Describe local capture truth precisely: 22 core artifact screenshots exist;
   the four required accessibility/narrow views are absent; tracked acceptance
   remains 0/26.
3. Do not import partial evidence as a pass.

### G1 exit gate

- one turn grammar is authoritative;
- server/client composed-card bounds agree;
- no accepted payload is silently truncated;
- uncertainty survives from interaction state into telemetry;
- contracts describe current evidence without promotion language.

## 7. Gate G2 — build a strict artifact-decision eval

**Effort:** three to five days.

**Owner:** backend eval lane.

**Dependency:** G1 policy locked.

**Goal:** detect wrong/no/too-many artifacts before changing retrieval or prompts.

### 7.1 Dataset contract

Create a focused suite of approximately 48 scenarios. Start small enough to
review every row manually; expand only from production failures.

Each labeled turn should declare:

```yaml
artifact_expectation:
  warranted: true
  family: venue_card
  required_tool: post_venue_card
  max_primary_artifacts: 1
  allowed_settlement_receipts: []
  durable_owner: places
  postcondition: structured_message_persisted
  prose_relationship: complements
  followup_behavior: update_or_reference
```

Negative turns set `warranted: false` and list prohibited structured tools.
Do not derive scenario wording from capability-catalog examples; that would
overfit the selector to its own documentation.

Primary artifact counts and settlement receipts are graded separately. A
receipt is allowed only when the scenario declares it and it carries the same
object/mutation lineage; it cannot be used as a loophole for stacking two
independent assistant judgments.

### 7.2 Initial corpus matrix

| Scenario class | Positive | Negative/counterexample | Total |
| --- | ---: | ---: | ---: |
| delegated place judgment | 6 | 4 | 10 |
| group choice vs “you pick” | 5 | 5 | 10 |
| Plan creation/revision/progress | 6 | 4 | 10 |
| reaction/decision follow-up | 4 | 4 | 8 |
| explanation, relationship, or chit-chat | 0 | 6 | 6 |
| stale/retry/follow-up on existing artifact | 3 | 1 | 4 |
| **total** | **24** | **24** | **48** |

Represent:

- private and group contexts;
- terse and detailed prompts;
- local/home-city and trip contexts;
- user-named place vs open discovery;
- explicit alternatives vs delegated judgment;
- consequential vs non-consequential edits;
- a follow-up that should not repeat the prior card;
- grounded-result absence and safe abstention;
- privacy-sensitive group turns.

### 7.3 Deterministic graders

Do not weaken the generic framework for existing suites. Add an explicit
artifact contract check or exact-count check rather than changing every legacy
`tool_called` warning into a failure.

Required hard graders:

- required tool called;
- prohibited artifact tool not called;
- exact/max tool count;
- exact/max structured-message count;
- persisted attachment type matches expectation;
- persisted identity/version is present;
- successful tool result has the declared postcondition;
- fallback text is non-empty;
- no private evidence appears in group-visible payloads;
- no route/style/callback/executable code appears in blueprints;
- follow-up does not duplicate the same object as a new unrelated artifact.

Likely touchpoints:

- `tools/eval/plugins/concierge/checks.py`;
- `tools/eval/plugins/concierge/runner.py`;
- `tests/eval/test_concierge_runner_structured_messages.py`;
- new focused tests under `tests/eval/`;
- new configs under `tools/eval/configs/concierge/artifact_selection/`.

### 7.4 Subjective grader

Use an LLM judge only for:

- was a structured object actually more useful than prose?;
- did prose complement rather than duplicate the artifact?;
- did the artifact represent the user’s requested degree of agency?;
- was the receipt appropriately concise and comprehensible?

Calibration protocol:

1. Human-label 20 balanced examples before seeing the judge’s verdict.
2. Run the judge with artifact payload and surrounding turn but exclude private
   chain-of-thought.
3. Measure pass/fail agreement, false-lenient rate, false-harsh rate, and
   uncertainty/escalation rate.
4. Rewrite the rubric, not the examples, when disagreement reveals ambiguity.
5. Keep deterministic failures authoritative even when the LLM judge passes.

Initial promotion target: at least 85% human/judge agreement and no more than
10% false-lenient judgments on the 20-example calibration set. These are pilot
thresholds, not permanent SLOs.

### 7.5 Trial and promotion thresholds

Run all 48 scenarios once during iteration. Run the 12 highest-consequence
scenarios three times before promotion.

Initial gate:

| Measure | Promotion target |
| --- | ---: |
| deterministic contract/privacy failures | 0 |
| warranted artifact recall | >= 90% overall; 100% critical |
| artifact precision | >= 90% |
| family accuracy when artifact emitted | >= 95% |
| count/action-budget compliance | 100% |
| repeated-card violations | 0 critical; <= 5% overall |
| critical three-trial success | 3/3 for every row |

Do not tune directly against the final holdout. Reserve at least eight
paraphrased scenarios for promotion-only runs.

### 7.6 Efficient run ladder

```bash
# Backend, free and deterministic first
PYTHONPATH=. python -m tools.eval.cli lint --agent concierge
PYTHONPATH=. pytest tests/eval/ tests/concierge/test_contextual_tool_retrieval.py -q
PYTHONPATH=. python -m tools.eval.cli replay --all --strict \
  --results-dir tools/eval/baselines

# Then one bounded live config or resume from a known checkpoint
PYTHONPATH=. python -m tools.eval.cli run --config <artifact-config>
```

Never use full paid Qdrant/LLM runs as the prompt-debugging loop. Fixture tools
can rewrite YAML; inspect `git status` and `git diff` after every run.

### G2 exit gate

- scenario schema, 48-row corpus, deterministic graders, and calibration set
  are code-reviewed;
- baseline metrics are recorded for the current legacy selector;
- failure examples are inspectable by scenario and trace;
- the suite fails deliberately injected wrong-family, extra-card, missing-card,
  privacy, and unpersisted-output defects.

## 8. Gate G3 — evaluate contextual tool selection without risking recall

**Effort:** two to three days after G2.

**Owner:** backend retrieval lane.

**Default runtime:** remain `shadow`.

### 8.1 Variants

Compare on the same artifact corpus:

1. current eligible legacy tool surface;
2. current local contextual BM25 capability retrieval;
3. local retrieval with semantically coupled grounding + presentation bundles;
4. Anthropic provider tool search/deferred loading in eval-only mode, if the
   current SDK/model supports it without a runtime migration.

### 8.2 Bundle repair hypothesis

The current venue-discovery bundle exposes grounding/search tools while
`post_venue_card` is separately retrievable from examples that sound like an
explicit request for a card. Ordinary users request a recommendation, not a
renderer.

Test two bounded designs:

- **Coupled bundle:** venue judgment makes both search and presentation tools
  available.
- **Deterministic projection policy:** after a grounded decisive venue result,
  the agent retains or receives the presentation tool independently of lexical
  retrieval.

Prefer the coupled bundle unless it materially increases irrelevant tool
exposure. It is easier to reason about and keeps presentation semantics visible
to the agent.

### 8.3 Measurements

- artifact recall, precision, and family accuracy from G2;
- critical capability recall;
- eligible-vs-retrieved tool count;
- tool-definition input tokens;
- tool-selection latency;
- invalid or unavailable tool calls;
- group/private privacy violations;
- disagreement by terse follow-up, local context, and group context.

### 8.4 Promotion rule

Enforcement is allowed only if:

- it meets every G2 critical threshold;
- it has no statistically meaningful regression from the legacy surface on the
  holdout;
- presentation-tool recall is 100% on critical artifact-positive rows;
- token/tool-surface reduction is material enough to justify rollout;
- shadow telemetry has enough volume to expose terse and follow-up failures;
- rollback is a configuration change, not a deploy.

If the custom retriever does not outperform the legacy surface enough to
justify its complexity, leave it in shadow or remove the custom layer. The
goal is selection reliability, not ownership of a retrieval subsystem.

### G3 exit gate

- a dated comparison report records all variants on the same corpus;
- one approach is selected, explicitly deferred, or rejected;
- production default remains shadow until the rollout gate is separately met.

## 9. Gate G4 — instrument durable loop truth

**Effort:** two to four days.

**Owners:** mobile telemetry + backend/domain event owners.

**Dependency:** G1 lifecycle vocabulary.

### 9.1 Event chain

Use content-free correlation fields and existing causal/mutation identifiers
where available. Do not log prompt or card prose.

Recommended event chain:

| Event | Meaning |
| --- | --- |
| `artifact_impression` | >=800ms qualifying exposure |
| `artifact_action_started` | user initiated an action |
| `artifact_resolver_returned` | client/server resolver returned; not a commit |
| `artifact_domain_commit_observed` | owning read model proves mutation |
| `artifact_uncertain` | commit cannot be confirmed within reconciliation window |
| `artifact_reconciled` | later read establishes committed/superseded/failed truth |
| `artifact_owner_opened` | user followed the handoff |
| `artifact_owner_rendered` | owner surface rendered matching object/version |
| `artifact_rollback_observed` | optimistic state returned to canonical prior truth |
| `artifact_resumed` | later turn/surface refers to the same durable object |

Required dimensions:

- attachment family and version;
- private/group scope;
- action class, not user-visible text;
- opaque artifact/message/mutation correlation id;
- owner type;
- lifecycle transition;
- environment/build revision;
- no place name, user message, recommendation copy, or private-memory content.

### 9.2 Domain join

For each golden family, name the authoritative postcondition:

| Family | Authoritative truth |
| --- | --- |
| Place | saved-place/relationship read returns canonical entity |
| Plan | current Plan/itinerary version contains expected revision |
| Decision | proposal/reaction state plus policy resolution and resulting Plan effect |
| Reaction | persisted selection/version visible after a new read |

Telemetry joins must not substitute for database assertions in tests. They are
production observability, not the domain authority.

### 9.3 Dashboard metrics

- artifact precision and recall from sampled judged turns;
- family accuracy;
- cards per assistant turn and stacking rate;
- action-start to resolver-return rate;
- resolver-return to durable-commit rate;
- uncertainty and recovery rate;
- owner-open and owner-render rate;
- artifact-to-loop-closure rate;
- repeated/reposted artifact rate;
- second-occasion resume rate;
- results split by artifact family, scope, build, and environment.

Clicks are diagnostic only. The primary operational metric is durable commit
plus matching owner render.

### G4 exit gate

- event semantics and privacy review are accepted;
- uncertain and known failure can be separated;
- every golden family has a named postcondition and owner-render join;
- one local run produces a coherent event chain without private content.

## 10. Gate G5 — certify four real product loops

**Effort:** five to eight days depending on environment readiness.

**Owners:** full-stack integration lane + evidence lane.

**Dependencies:** G1, G2, and relevant G4 events.

### 10.1 Environment ladder

Use one outcome contract across progressively stronger environments:

| Lane | Data/provider | What it proves |
| --- | --- | --- |
| offline component | typed fixtures + mock API | rendering, actions, lifecycle, accessibility |
| backend contract | in-memory/offline test providers | validation, privacy, persistence protocol, postconditions |
| local real stack | seeded Postgres + Qdrant; deterministic provider where possible | tool selection, real writes, read-back, message mapping |
| local device | local real stack + iOS simulator + Maestro | stream/reveal/action/refresh/owner UI |
| controlled cloud | isolated test account/data + real auth/provider | network/auth/multi-device behavior |
| production canary | aggregated content-free telemetry | real frequency, latency, failure shape |

Mocks may prove UI mechanics; they may never promote durable loop closure.
Shared production data must not be used as an E2E fixture.

### 10.2 Journey A — Place judgment to Places

Setup:

- seeded city/occasion with at least one grounded eligible place;
- authenticated private conversation;
- Places saved state empty for the target entity.

Happy path:

1. Ask a delegated recommendation such as “somewhere good for dinner tonight.”
2. Assert one `venue_card`, not a list of independent cards.
3. Assert complementary prose and useful fallback text.
4. Tap Save once; block duplicate writes while acting.
5. Read saved-place truth from the backend.
6. Terminate/relaunch or force a fresh query.
7. Open Places and assert the exact entity renders as saved.
8. Ask a follow-up and assert the original object is referenced or updated,
   not reposted as an unrelated artifact.

Failure variants:

- no grounded candidate -> prose/abstention, no decorative card;
- network fails before write -> retryable failure;
- response is lost after write -> uncertain, reconcile to saved;
- double tap -> one logical mutation;
- stale/deleted entity -> recovery state, no generic-root fallback.

Exit oracle: saved-place row + fresh Places render + correlated artifact action.

### 10.3 Journey B — Plan work to current Trips truth

Setup:

- controlled Trip with known Plan version;
- private or authorized group context.

Happy path:

1. Request bounded Plan generation/revision.
2. Observe building projection and persisted lineage.
3. Observe ready/revised projection with current version identity.
4. Open Trips through the artifact handoff.
5. Fresh-read the Plan and assert expected blocks/version.
6. Exercise undo where authorized and prove the subsequent version.

Failure variants:

- app restart during building;
- stale ready card after a newer Plan version;
- undo transport loss after server write -> uncertain then reconciliation;
- unauthorized undo -> rejected without optimistic false success.

Exit oracle: current Plan version/read model + matching Trips render.

### 10.4 Journey C — group decision to Plan effect

Setup:

- organizer and member accounts;
- open group decision with known policy and current Plan version.

Happy path:

1. Prompt a genuine tradeoff and assert one decision/reaction artifact.
2. Member votes/reacts; second reader observes the persisted state.
3. Organizer resolves under the configured policy.
4. Assert proposal/decision state transition.
5. Assert `change_applied` or equivalent settlement receipt.
6. Open Trips and prove the resulting Plan effect/version.
7. Refresh both clients and prove convergence.

Failure variants:

- delegated “you pick” must not produce a group vote;
- member attempts organizer-only resolution;
- duplicate vote/double resolution;
- stale card after withdrawal or expiry;
- misery-aware negative reaction blocks false group consensus.

Exit oracle: decision/proposal row + Plan diff/version + receipt + two-reader
agreement.

### 10.5 Journey D — reaction persistence and rollback

Setup:

- persisted reaction card with known message/version and viewer state.

Happy path:

1. Select a reaction once.
2. Confirm persisted selection via a fresh read.
3. Refresh/relaunch and assert the selected state remains.
4. Continue the conversation and assert Vesper consumes the state without
   reposting the same card.

Failure variants:

- transport failure before commit -> rollback/retryable;
- ambiguous response after commit -> uncertain then reconcile;
- rapid change/double tap -> final server state wins;
- stale message/version -> superseded, no overwrite.

Exit oracle: persisted reaction/version + refreshed rendering + rollback or
reconciliation proof.

### 10.6 Test implementation rules

- reset each journey from an independent seeded state;
- prefer stable `testID`/accessibility selectors over coordinates;
- critical actions are never optional in Maestro;
- a retry may classify infrastructure flakiness but may not erase first-attempt
  failure from the receipt;
- pair screenshots with backend postconditions;
- preserve request/mutation/message ids in the evidence receipt;
- do not let LLM copy differences make deterministic domain assertions brittle;
- run two-account flows with genuinely distinct sessions.

### G5 exit gate

- all four journeys pass the local real-stack contract;
- Place and Plan pass device + refresh proof;
- Decision passes two-account controlled-cloud proof;
- Reaction demonstrates both rollback and uncertain reconciliation;
- evidence receipts bind app/backend revisions, environment, fixture, and
  first-attempt result.

## 11. Gate G6 — close visual evidence without reopening the language

**Effort:** one Mac session plus review.

**Owner:** visual evidence lane; final verdict by a reviewer who did not author
the component changes.

### Tasks

1. Run the existing default matrix if the 22 core screenshots need a clean
   revision-bound recapture.
2. Capture the three xxxLarge artifact shells:

   ```bash
   npm run qa:chat-artifacts:a11y
   ```

3. Capture the 320pt Place state:

   ```bash
   npm run qa:chat-artifacts:narrow
   ```

4. Import exactly the required 26 screenshots:

   ```bash
   npm run design:chat-artifacts:export -- --screenshots=<run-screenshot-dir>
   npm run design:chat-artifacts:check --silent
   ```

5. Run comparison, material health, verdict scaffold/validation, and inspect
   every comparison rather than accepting from manifest status.
6. Judge hierarchy, text fit, action prominence, state differentiation,
   transcript fit, accessibility reflow, narrow integrity, and whether prose
   duplicates the artifact.
7. Keep findings concrete. Visual acceptance does not certify backend truth.

### Exit gate

- accepted tracked evidence is 26/26;
- the verdict is revision-bound and postdates the artifact implementation;
- no clipping, inaccessible action, first-viewport domination, or misleading
  success state remains;
- unresolved defects are assigned rather than converted to an optimistic pass.

## 12. Gate G7 — selective remaining-family expansion

**Effort:** optional, after G5 and G6.

**Rule:** no blanket sixteen-family migration.

Prioritize by consequence, demo exposure, mutation complexity, and owner
handoff. Recommended first wave:

1. `trip_creation_proposal` — creation authority and pre/post-create lifecycle;
2. `change_applied` — canonical Plan receipt and revert truth;
3. `booking_proposal` — consequential confirmation boundary;
4. `booking_confirmation` — provider truth and uncertainty;
5. `composed_card` — bounded cross-family contract and unavailable actions.

For each family, require before visual work:

- lifecycle fixture;
- durable owner;
- action budget and authority;
- postcondition;
- failure/uncertainty state;
- transcript fixture;
- exact reason it belongs in the flagship or a high-risk path.

Disposition options are `reuse`, `refine`, `preserve dedicated composition`,
`compatibility only`, or `retire`. “Redesign because it exists” is not an
admissible disposition.

## 13. Rollout plan

### Stage 0 — offline baseline

- run conformance, unit, replay, and the G2 corpus;
- record metrics for the legacy and shadow selectors;
- no runtime behavior change.

### Stage 1 — local real stack

- enable candidate selection behavior only in the isolated seeded environment;
- run four journeys and inspect traces/postconditions;
- fail closed to the current selector.

### Stage 2 — controlled dogfood

- dedicated accounts and isolated records;
- keep retrieval mode independently reversible;
- collect content-free action/uncertainty/owner-render telemetry;
- manually review a small stratified sample, not every turn.

### Stage 3 — 10% canary

Prerequisites:

- G2 and G5 thresholds pass;
- no privacy or critical persistence defect;
- telemetry delivery verified end to end;
- on-call owner and one-flag rollback documented.

Rollback triggers:

- any privacy leak;
- critical artifact recall below threshold;
- stacking/repetition spike;
- durable commit rate materially below baseline;
- uncertainty without reconciliation above agreed threshold;
- owner render mismatch;
- material latency/cost regression.

### Stage 4 — measured expansion

Promote 10% -> 50% -> 100% only after a fixed observation window and minimum
sample size. Do not promote on a handful of founder successes. Keep legacy
behavior available through the observation period.

## 14. Worktree and parallel execution model

Parallel work is useful only after G1 policy and schema decisions are serially
locked. The maximum useful shape is one integrator plus three bounded lanes.

| Lane | Owns | Must not edit |
| --- | --- | --- |
| root/integration | policy decision, shared schema, OpenAPI sync, central inventories, rollout decision | concurrent profile branch files |
| backend eval/retrieval | G2 corpus/checks and G3 comparison | tuned prompts until approval; mobile files |
| mobile state/telemetry | uncertainty semantics, action truth, targeted component tests | backend schema, central visual verdict |
| evidence/E2E | Maestro flows, evidence receipts, skeptical read-only review | shared renderer grammar until findings are accepted |

Serial-only work:

- product turn grammar;
- backend prompt modification;
- shared blueprint schema change;
- OpenAPI/type regeneration;
- central artifact inventories/manifests;
- final visual verdict;
- retrieval enforcement decision;
- production rollout.

Recommended coordinated worktrees after the base settles:

```bash
./scripts/new-worktree.sh --backend-only --base <backend-sha> artifact-selection-eval
./scripts/new-worktree.sh --app-only --base <app-sha> artifact-state-telemetry
./scripts/new-worktree.sh --app-only --base <app-sha> artifact-loop-evidence
```

If the workspace script uses different flags, inspect its help before running;
the requirement is separate worktrees and recorded SHAs, not these exact names.

## 15. Commit and integration sequence

Keep commits reviewable and stage explicit filenames only.

### Backend

```text
test(evals): add strict artifact decision contract graders
test(evals): add balanced artifact selection corpus
fix(concierge): unify one-artifact turn policy
fix(concierge): couple artifact presentation capability retrieval
fix(cards): enforce truthful composed-card action bound
docs(concierge): record artifact selection and rollout contract
```

Prompt and retrieval commits occur only if their preceding eval commits expose
and then verify the need. Avoid combining corpus changes with behavior changes,
so baseline and treatment remain comparable.

### Mobile

```text
fix(chat): preserve uncertain artifact telemetry semantics
fix(chat): render every accepted composed-card action
test(chat): add durable artifact reconciliation cases
test(e2e): prove artifact owner-surface handoffs
docs(chat): commit skeptical 26-view artifact verdict
```

### Workspace

```text
docs(product): lock chat artifact turn and owner grammar
chore(api): sync composed-card action contract
docs(evidence): record artifact loop promotion receipts
```

Integration order:

1. deterministic eval/check infrastructure;
2. baseline corpus result;
3. product policy;
4. server/client action and telemetry truth;
5. prompt/capability change, if justified;
6. local real journeys;
7. OpenAPI/type sync, if schema changed;
8. visual evidence and verdict;
9. controlled cloud proof;
10. governance promotion and rollout decision.

## 16. Validation matrix

| Change | Required validation |
| --- | --- |
| eval checks/corpus | eval unit tests, lint, strict replay, injected-defect tests |
| prompt policy | golden prompt snapshots, 48-row suite, holdout, three-trial critical set |
| capability retrieval | contextual retrieval unit tests, variant report, shadow metrics |
| blueprint action bound | backend model tests, OpenAPI diff, generated type diff, mobile Zod/component tests |
| telemetry semantics | utility/context tests, privacy field audit, local event-chain receipt |
| Place/Plan/Decision/Reaction loop | backend postcondition + fresh owner read + device assertion |
| visual evidence | 26/26 imports, comparison review, validated skeptical verdict |
| production rollout | canary dashboard, rollback test, minimum sample/window |

Per-commit minimums:

```bash
# Backend, narrowed to touched surfaces first
PYTHONPATH=. pytest <targeted-tests> -q
ruff check <touched-python-files>

# Mobile
npx jest <targeted-suites> --runInBand
npx tsc --noEmit
npm run chat-artifacts:check --silent
npm run design:chat-artifacts:check --silent

# Cross-repo only when API/schema changes
./scripts/sync-types.sh
make contract-check
```

Run broader offline suites before merging, but do not treat unrelated known
pre-existing failures as evidence for or against the artifact change. Record
them separately with exact command output.

## 17. Metrics and decision docket

### 17.1 Product/AI metrics

| Metric | Definition |
| --- | --- |
| artifact precision | warranted emitted artifacts / emitted artifacts |
| artifact recall | warranted turns with correct artifact / warranted turns |
| family accuracy | correct family / turns where artifact emitted |
| stacking rate | assistant turns with >1 primary artifact |
| repetition rate | follow-ups reposting the same object without lifecycle need |
| durable commit rate | domain commits observed / mutation actions started |
| uncertainty rate | uncertain outcomes / mutation actions started |
| uncertainty recovery | reconciled uncertain outcomes / uncertain outcomes |
| owner-render rate | matching owner renders / successful handoffs |
| loop closure | matching owner renders / artifact turns intended to create/change state |
| second-occasion resume | later object resumes / eligible prior durable objects |

### 17.2 Engineering/evidence metrics

- artifact corpus pass rate by grader and trial;
- first-attempt vs eventual E2E pass rate;
- flake rate and retry count;
- environment/infrastructure vs product failure split;
- stale-evidence age;
- active families with lifecycle fixture/postcondition/owner;
- human/judge agreement and false-lenient rate;
- selector tool count, tokens, latency, and recall;
- time from defect to deterministic regression case.

### 17.3 Decisions to record explicitly

1. exact one-artifact exceptions;
2. composed-card max action count;
3. whether `chat_card_action_completed` is deprecated or redefined;
4. whether venue search and presentation are one capability bundle;
5. whether provider tool search is worth adopting;
6. promotion thresholds after the first baseline;
7. test-data isolation for controlled cloud runs;
8. minimum canary sample/window;
9. which remaining artifact family earns the next lifecycle investment.

## 18. Risks and countermeasures

| Risk | Countermeasure |
| --- | --- |
| eval overfits capability examples | independent paraphrases and held-out rows |
| LLM judge is lenient | deterministic graders dominate; human calibration and false-lenient metric |
| screenshots are mistaken for system proof | require backend postcondition and fresh owner render |
| mock success is mistaken for persistence | promote only local-real/cloud receipts |
| retries hide flakiness | report first-attempt and eventual results separately |
| retrieval drops presentation tools | critical 100% presentation recall gate; stay shadow |
| prompt change improves eval but harms naturalness | keep corpus balanced; human read and holdout |
| telemetry exposes private content | content-free schema and privacy review |
| generic card absorbs consequential behavior | preserve specialized authorities and postconditions |
| all twenty families consume the program | stop at four golden plus justified high-risk wave |
| concurrent app work contaminates commits | separate worktrees and explicit staging |
| schema change breaks client contract | workspace sync-types workflow and reviewed diffs |
| stale visual verdict survives new code | revision-bound evidence and verdict age checks |

## 19. Stop conditions

Stop and create a separate decision/RFC if the work appears to require:

- arbitrary model-authored UI or executable payloads;
- a new universal card with family-specific flags;
- a new durable domain object only to satisfy chat presentation;
- drawing cross-row continuity through a virtualized transcript;
- changing specialized booking/proposal authority into client-local behavior;
- logging private prompt/card content for measurement;
- production retrieval enforcement before independent recall evidence;
- redesigning the full attachment inventory without a cross-portfolio
  authority, lifecycle, and consumer analysis; four real loops are useful
  evidence but neither necessary nor sufficient to define the architecture;
- accepting a visual verdict without the required screenshots;
- editing on the unsettled profile branch or staging unrelated files.

## 20. Definition of done

The program is complete only when:

- [ ] one artifact-selection policy is promoted into current authority;
- [ ] every active prompt fragment obeys the policy;
- [ ] composed-card server and client contracts accept the same maximum two
      actions and no accepted action is silently dropped;
- [ ] telemetry distinguishes retryable failure, uncertainty, reconciliation,
      commit, supersession, and rollback;
- [ ] the 48-row eval and held-out set meet promotion thresholds;
- [ ] the eval fails injected wrong/no/extra artifact defects;
- [ ] contextual retrieval has a dated legacy/local/provider comparison;
- [ ] retrieval enforcement remains shadow or passes its explicit gate;
- [ ] Place save survives refresh and renders in Places;
- [ ] Plan work survives refresh and renders the current version in Trips;
- [ ] group decision state converges for two readers and affects Plan truth;
- [ ] reaction state persists and both rollback and uncertainty are proven;
- [ ] all four journeys have backend postconditions and revision-bound receipts;
- [ ] accepted Vesper Chat native evidence is 26/26 with a skeptical verdict;
- [ ] product dashboards distinguish resolver return from durable commit;
- [ ] no Discover/Atlas authority or unconstrained UI is reintroduced;
- [ ] accepted rules are promoted and this working document is archived.

## 21. Recommended schedule

This is a three-block program, not necessarily a three-calendar-week project.
With clean worktrees and bounded parallelism:

### Execution block A — truth and evaluation foundation

Days 1–5:

- G0 base freeze;
- G1 policy/action/telemetry contracts;
- G2 grader infrastructure and first 32–48 rows;
- baseline legacy-selector report.

### Execution block B — selection and loop proof

Days 6–12:

- complete G2 holdout/calibration;
- G3 retrieval variants and decision;
- G4 event chain;
- Place and Plan local-real/device journeys;
- Reaction rollback/reconciliation journey.

### Execution block C — multiplayer, evidence, and promotion

Days 13–17:

- two-account Decision journey;
- four missing artifact captures and 26/26 import;
- skeptical verdict;
- controlled-cloud receipts;
- authority promotion and rollout docket.

Do not begin G7 remaining-family expansion merely because a lane becomes idle.
Use the first real failures to decide whether the next investment belongs in
selection, reconciliation, owner surfaces, or one high-risk family.

## 22. Immediate next move

The first implementation tranche should be only:

1. settle/create clean app and backend worktrees;
2. add the strict artifact eval contract and balanced corpus skeleton;
3. lock the one-artifact turn policy;
4. repair composed-card action truth and uncertain telemetry;
5. complete/import the four missing native evidence views.

Do not modify contextual retrieval or broaden the renderer until this tranche
produces a measured baseline. That baseline determines whether the next defect
is agent policy, capability recall, durable mutation, or presentation—not
intuition alone.
