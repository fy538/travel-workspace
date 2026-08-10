---
doc_type: working
status: active
owner: product / AI systems / research
created: 2026-08-10
last_verified: 2026-08-10
expires: 2026-09-09
why_new: Defines the research program needed to turn Vesper's new product thesis into a governed decision-and-learning system, without conflating model quality, engagement, product value, privacy, or device proof.
source_of_truth_for:
  - ai-decision-and-learning-research-agenda-2026-08
related:
  - intentional-convergence-engineering-plan-2026-08-10.md
  - ai-decision-and-learning-engineering-plan-2026-08-10.md
---

# AI decision and learning research agenda

## 1. Executive decision

Vesper should not become a more autonomous version of a generic travel agent.
It should become a **governed decision system**: one that knows which evidence it
may use, whose preferences apply, what remains uncertain, when to ask, when to
recommend, when to propose a reversible change, and when to stay silent.

The recent product pivot makes seven research questions urgent:

1. How should Vesper choose among asking, showing, recommending, proposing,
   acting through a canonical executor, abstaining, and remaining silent?
2. When does an observation deserve promotion into a durable personal or
   relationship claim?
3. How can memory improve decisions while remaining authorized, temporal,
   correctable, and forgettable?
4. How should Vesper help a group decide without leaking private information,
   steering invisibly, or manufacturing a false feeling of inclusion?
5. How can the product learn whether a proactive intervention caused value,
   rather than merely caused a tap?
6. How should the system defend decisions, memory, group communication, and
   mutations from untrusted travel content?
7. How do we know whether our automated evaluators themselves are reliable?

These questions are related, but they must not collapse into one end-to-end
model score. A fluent response can still be unauthorized, wrongly scoped,
causally useless, privacy-revealing, or impossible to reproduce on a device.

The research program therefore studies a bounded pipeline:

> authorize evidence → resolve scope and time → construct a decision state →
> select a bounded speech/action move → execute through canonical paths →
> observe outcomes → promote only justified learning

## 2. Authority and evidence boundary

This is a research agenda, not production authorization. It may produce
fixtures, offline evaluations, shadow observations, study protocols, and
recommendations. It does **not** authorize:

- a new group-visible model path;
- autonomous itinerary, proposal, booking, or expense mutations;
- silent promotion of inferred preferences into durable memory;
- experimentation with privacy, audience, authorization, or mutation safety;
- proactive messaging to real users without an approved eligibility policy,
  consent model, holdout design, kill switch, and device validation;
- calling a journey or feature complete on the strength of tests or model
  scores alone.

Evidence labels in this agenda are intentionally strict:

| Label | Meaning |
| --- | --- |
| **S** | Static/source or type evidence |
| **M** | Deterministic fixture, simulation, or mock-walk evidence |
| **B** | Backend-real behavior on a pinned revision and database state |
| **D** | Controlled simulator/device-mock evidence |
| **V** | Physical-device evidence bound to app build and backend deployment |
| **A** | AI evaluation evidence, including model-judge results |
| **H** | Human judgment or study evidence with a recorded protocol |
| **C** | Causal evidence from a valid randomized or otherwise identified design |

No lower layer implies a higher one. In particular, **A is not V**, engagement
is not product value, and observational association is not C.

## 3. Relationship to the convergence program

This agenda is a separate workstream from the four active implementation lanes
in the [intentional convergence engineering plan](intentional-convergence-engineering-plan-2026-08-10.md).
It does not redirect, broaden, or share code ownership with Worktrees A–D.

It consumes their eventual contracts:

- **A — evidence integrity:** trustworthy evidence layers, receipts, generated
  status, and non-fabricated certification;
- **B — Home truth:** honest unavailable/partial/empty states and reliable
  private delivery surfaces;
- **C — context trust:** relationship and experience scope, roster revocation,
  authorized projection, and coherent context admission;
- **D — map/projection coherence:** grounded, fresh, revision-bound spatial and
  plan projections.

Until those contracts land on recorded integration revisions, this agenda may
advance through document work, corpus design, immutable fixtures, deterministic
baselines, and read-only analysis. It should not compete with A–D by editing
their shared runtime surfaces.

This agenda also extends rather than replaces:

- the [Vesper AI system improvement plan](vesper-ai-system-improvement-plan-2026-08-01.md), especially trajectory evaluation, golden journeys, routing, and the decision to defer fine-tuning;
- [AI harness and the long loop](../../travel-agent/docs/working/ai-harness-and-the-long-loop-2026-08-04.md), especially its ask-versus-act and long-horizon evaluation work;
- the [notification intelligence research agenda](../../travel-agent/docs/research/notification-intelligence-research-agenda.md), whose timing and aggregation questions become causal intervention questions here;
- [multiplayer activation psychology](../../travel-agent/docs/research/multiplayer-activation-psychology-2026-08-09.md), whose group-product hypotheses need decision-process and inferential-privacy evaluation;
- [outcome inference and reconciliation](../../travel-agent/docs/working/outcome-inference-and-reconciliation-2026-08-06.md), whose conservative separation of occurrence inference from preference learning is retained.

## 4. Research principles

### 4.1 Separate facts, feasibility, preference, and action

A venue can be objectively open, feasible for the route, disliked by one
traveler, and still inappropriate to mention to the group because the reason is
private. These are different judgments. Every experiment must preserve four
layers:

1. **Option facts:** sourced attributes and freshness.
2. **Feasibility:** time, route, weather, availability, cost, and hard
   constraints.
3. **Preference:** whose preference, its evidence, durability, context, and
   companion/occasion scope.
4. **Speech/action policy:** what Vesper is authorized and justified to do now.

### 4.2 Uncertainty must be decision-relevant

The useful question is not “how confident is the model?” It is “could resolving
this unknown change the decision or make the action safe?” The system should
distinguish at least:

- missing fact;
- stale fact;
- preference ambiguity;
- relationship-scope ambiguity;
- audience/authorization ambiguity;
- outcome ambiguity;
- execution-state ambiguity.

### 4.3 Learn claims, not vibes

An outcome or interaction may create a **claim candidate**. It does not directly
rewrite the user's profile. Promotion requires provenance, subject, scope,
time, counterevidence, and a revocation path.

### 4.4 Silence is a first-class policy action

No-send, abstain, and defer are not missing predictions. They are intentional
actions that need expected-value and trust evaluation.

### 4.5 Safety is structural

Prompts and evaluators can supplement but cannot replace audience projection,
authorization checks, canonical writers, append-only receipts, redaction, and
kill switches.

### 4.6 Evaluate the decision and resulting state

String similarity and response pleasantness are secondary. Evaluation should
inspect the selected action, admitted evidence, tool trajectory, final database
state, visible projections, receipts, reversibility, and forbidden leakage.

## 5. RDL-01 — Decision policy: ask, show, recommend, propose, act, abstain, or remain silent

### Research question

Given a scoped travel decision, which bounded move creates the most expected
value without exceeding the system's authority or the user's tolerance for
friction and interruption?

### Why this remains open

Conversational recommendation work increasingly separates preference
elicitation from final choice, and recent evidence suggests that more
clarifying questions can reduce quality when they are badly timed or
uninformative. The local system has pieces of this logic, but it does not yet
have one explicit, testable decision policy shared across chat, Home, inbox,
and proactive delivery.

### Vesper hypotheses

- Early in a broad decision, one material attribute question will often
  dominate item-by-item comparison.
- Later, when the option set is small, comparison questions will outperform
  additional abstract elicitation.
- A question is justified only when its expected decision value exceeds its
  friction cost and it could change the selected safe action.
- “Recommend” and “propose” require stronger feasibility and scope evidence
  than “show options.”
- “Execute” is not a model speech act; it is an authorization result followed
  by a canonical, receipt-producing executor.
- A calibrated abstention policy will improve trust-weighted utility even if
  it lowers raw task-completion rate.

### Protocol: Vesper Decision Set

Create revisioned cases spanning trip planning, live-trip disruption, local
discovery, saved-place follow-up, group decisions, and post-outcome learning.
Each case includes:

- permitted evidence and deliberately excluded evidence;
- relationship and experience scope;
- option facts, freshness, and provenance;
- hard constraints and soft preferences;
- typed unknowns with materiality;
- audience and action authority;
- allowed decision actions;
- expected acceptable action set, not merely one golden sentence;
- forbidden actions and forbidden evidence disclosures;
- expected final state and receipt when execution is permitted.

Compare at least:

1. deterministic risk/authority rules;
2. an unconstrained answer-producing model;
3. a structured decision policy using explicit facts, feasibility,
   preferences, unknowns, and bounded actions;
4. a routing policy that escalates only hard or high-risk cases.

### Metrics

- acceptable-action accuracy;
- material-question efficiency;
- avoidable-question rate;
- unsafe or unauthorized action rate;
- abstention precision and recall by risk class;
- regret against expert-labeled option utilities;
- factual/freshness errors;
- tool and token cost;
- latency;
- human preference and trust, reported separately from correctness.

### Falsification and decision gate

Do not ship a general learned policy if a deterministic baseline performs as
well on decision quality, or if gains depend on higher privacy, mutation, or
fabrication error. If different surfaces need different action spaces, retain
surface-specific policies behind a shared contract instead of forcing one
universal agent.

### Research output

- Decision action taxonomy;
- Decision Set schema and initial corpus;
- baseline report;
- policy/routing recommendation with explicit non-goals.

## 6. RDL-02 — Claim promotion and relationship learning

### Research question

When should explicit statements, corrections, choices, refusals, saves,
itinerary outcomes, or repeated behavior become durable personal,
relationship, or occasion-scoped knowledge?

### Core distinction

The system must separately estimate:

1. whether an event happened;
2. what the event means;
3. whether it supports a preference claim;
4. whose claim it supports;
5. where and for how long that claim applies.

The recommendation itself may shape the user's response. A choice after an AI
recommendation is therefore not clean evidence of a pre-existing preference.

### Vesper hypotheses

- One implicit behavior should not produce a durable claim.
- Explicit correction should outrank repeated weak inference.
- Repetition across occasions is stronger than repetition within one tightly
  coupled trip.
- Group outcomes do not become personal claims without per-person evidence.
- Companion and occasion scope are part of the claim, not optional metadata.
- Departing a relationship scope must invalidate claims whose applicability
  depended on that exact roster, regardless of who originally authored them.

### Protocol: Claim Promotion Lab

Build longitudinal bundles rather than isolated turns. Each bundle contains a
sequence of statements, recommendations, selections, outcomes, corrections,
roster changes, and later decisions. Human reviewers label:

- occurrence status and confidence;
- candidate claim;
- subject and source;
- explicitness;
- scope and applicability;
- validity interval;
- counterevidence;
- permissible promotion level;
- required confirmation or correction affordance.

Test promotion policies ranging from conservative deterministic rules to
model-assisted candidate extraction. Measure the downstream decision effect,
not merely extraction agreement.

### Metrics

- false durable-promotion rate;
- missed useful-promotion rate;
- cross-person and wrong-roster contamination;
- correction latency and deletion completeness;
- temporal/version-resolution accuracy;
- later decision lift from admitted claims;
- recommendation-induced preference bias;
- user comprehension of “why Vesper believes this.”

### Falsification and decision gate

If inferred claims cannot outperform explicit-only memory without materially
raising contamination or correction burden, keep inference as ephemeral
decision context. Do not promote a policy on aggregate precision alone; the
tail risk of wrong-person and private-to-group errors is a separate hard gate.

### Research output

- ClaimCandidate contract;
- promotion ladder and revocation semantics;
- longitudinal fixture set;
- explanation/correction interaction study;
- recommendation on which evidence classes remain ephemeral.

## 7. RDL-03 — Governed memory and active forgetting

### Research question

How can long-term memory improve Vesper's decisions across trips and
relationships while respecting authorization, temporal change, correction,
and deletion?

### Research basis

Long-horizon memory benchmarks show persistent weaknesses in information
extraction, multi-session reasoning, temporal reasoning, knowledge updates,
and abstention. Newer work also exposes a gap between retrieving a relevant
sentence and correctly applying an implicit constraint. Multi-principal memory
adds access control and active forgetting as first-class requirements.

### Vesper hypotheses

- Retrieval quality must be evaluated at the final decision, not by lexical
  match alone.
- Authorization must precede semantic retrieval so that private candidates are
  never exposed to an inappropriate downstream context.
- Temporal/version resolution should precede application to a decision.
- Active forgetting requires both removal from future retrieval and a test
  proving the removed claim no longer affects behavior.
- Memory should fail closed on ambiguous audience/scope and fail soft on
  ordinary relevance uncertainty.

### Protocol: Vesper MemoryBench

Construct multi-session travel histories with:

- stable facts and changing facts;
- corrections and superseded claims;
- private, shared, relationship, trip, and occasion scopes;
- shared facts with different viewer projections;
- implicit constraints whose cue differs from the final decision language;
- roster additions and removals;
- deletion/forgetting requests;
- false-premise questions where correct behavior is to abstain or correct the
  premise.

Evaluate the full pipeline:

> authorize → retrieve → resolve version/time → rank relevance → apply or
> abstain → compose for audience

### Metrics

- final-decision accuracy and regret;
- unauthorized retrieval and visible leak rate;
- stale/superseded application rate;
- correction and forgetting completeness;
- false-premise awareness;
- cue-trigger application success;
- latency, storage, and token cost;
- helpful abstention rate.

### Falsification and decision gate

Reject any memory architecture that improves broad recall while leaking across
principals, applying superseded claims, or failing active-forgetting tests.
Retain a smaller typed memory if it produces better decisions than a larger
general conversational store.

### Research output

- MemoryBench corpus and runner;
- authorization-first retrieval specification;
- temporal-resolution and forgetting tests;
- memory architecture recommendation.

## 8. RDL-04 — Group decision quality, facilitation, and inferential privacy

### Research question

How can Vesper help a travel group surface constraints and make a decision
without disclosing private information, privileging one member invisibly,
steering the group, or creating only an illusion of participation?

### Research basis

Recent controlled studies of LLM group facilitation suggest an important split:
people may prefer an AI-facilitated process and share more information without
achieving better consensus or decisions. Facilitation can also steer outcomes
and displace human turns. Product desirability, information sharing, consensus,
decision quality, and procedural fairness must therefore be measured
separately.

### Vesper hypotheses

- Recommendation and facilitation are distinct policies and should not share a
  single free-form prompt.
- Deterministic aggregation baselines will remain competitive for many travel
  decisions when hard constraints and disagreement are explicit.
- A bounded facilitator can improve minimum information coverage and perceived
  fairness without composing a consensus on the group's behalf.
- Output text may reveal a private constraint even when it does not quote it;
  inferential privacy requires counterfactual testing.
- Organizer authority applies only when explicitly granted for that decision.

### Protocol: Vesper Group Lab

Create multi-person scenarios with public, private, relationship-scoped, and
unknown preferences. Compare:

- hard-constraint filtering;
- average utility;
- average utility plus explicit disagreement;
- max-min utility;
- sequential fairness across repeated choices;
- explicitly granted organizer tie-break;
- bounded LLM facilitation;
- unconstrained group answer generation as a negative/control baseline.

Allowed facilitator speech acts should be typed, for example:

- summarize only group-safe stated criteria;
- ask each member for one missing public criterion;
- show disagreement without attributing a private reason;
- propose a reversible vote or shortlist;
- defer because a safe explanation cannot be formed.

Every candidate group message must pass the existing group composition boundary
or an explicitly reviewed equivalent. Add a counterfactual privacy attack:
change one hidden private constraint while holding group-visible inputs fixed
and test whether the output difference lets an observer infer the secret.

### Metrics

- hard-constraint satisfaction;
- group welfare and minimum-member utility;
- decision quality against scenario ground truth;
- consensus, information coverage, and time to decision;
- participation balance and human-turn displacement;
- perceived inclusion and procedural fairness;
- direct and inferential privacy leakage;
- steering sensitivity;
- reversibility and receipt correctness for proposals.

### Falsification and decision gate

If facilitation improves preference ratings but not decisions or fairness, do
not market or deploy it as better group judgment. Any group-visible canary
requires deterministic privacy tests, backend-real state verification, and a
physical multi-device walk; model-judge approval is insufficient.

### Research output

- group scenario corpus;
- aggregation baseline library;
- bounded facilitator action contract;
- inferential-privacy suite;
- human study protocol.

## 9. RDL-05 — Causal proactivity and earned interruption

### Research question

At which eligible moments does an unsolicited Vesper intervention cause a
better travel outcome than silence, and when does it create distraction,
dependency, annoyance, or loss of trust?

### Why engagement is insufficient

Notification trials in other domains show that pushes can substantially raise
opens and in-app engagement without changing the target behavior. Delayed
outcomes also bias naive uplift estimates. Vesper's target is therefore not a
click. It is incremental distal value, net of interruption and trust costs.

### Vesper hypotheses

- Proactivity should be earned by high relevance, materiality, actionability,
  and evidence freshness—not by model confidence alone.
- The right comparison is against silence at an eligible decision point.
- Effects vary by trip phase, urgency, relationship, channel, and prior
  notification load.
- Private, reversible, low-cost interventions are the only reasonable first
  randomized surface.
- A personalized timing model is valuable only if it improves distal outcomes,
  not just response speed.

### Protocol

Use a micro-randomized design at predeclared eligible decision points. Log:

- eligibility reason and excluded reasons;
- decision/context/policy versions;
- candidate interventions;
- treatment set and randomization probabilities;
- chosen treatment or no-send;
- channel, copy family, urgency, and cooldown state;
- immediate, intermediate, delayed, and negative outcomes;
- censoring, missingness, and competing interventions.

Randomization is permitted only among options already judged safe and
authorized. It must never vary privacy, audience, authorization, irreversible
mutation, or required warnings.

Outcome families:

| Horizon | Examples |
| --- | --- |
| Proximal | seen, dismissed, opened, replied |
| Intermediate | compared options, corrected context, accepted proposal |
| Distal | avoided disruption, reduced planning effort, completed desired experience, improved later decision |
| Negative | mute, disable, complaint, rapid undo, trust decline, notification fatigue |

### Metrics

- incremental distal value versus no-send;
- heterogeneous treatment effect by declared segments;
- interruption and fatigue cost;
- delayed-response-adjusted uplift;
- calibration of eligibility and no-send policies;
- consent comprehension;
- safety and rollback events.

### Falsification and decision gate

Do not promote a policy that improves opens but not distal value, or whose
benefit disappears after accounting for notification load and delayed outcomes.
Do not begin randomized live work until shadow logs establish enough eligible
events, instrumentation is complete, and private-device flows are validated.

### Research output

- eligible-decision-point taxonomy;
- intervention logging schema;
- causal analysis plan;
- consent and trust study;
- canary/no-send recommendation.

## 10. RDL-06 — Untrusted evidence and agent security

### Research question

How reliably does Vesper preserve user intent, audience boundaries, and
canonical mutation rules when travel evidence contains adversarial or
instruction-like content?

### Threat model

Untrusted text and media may enter through:

- place descriptions and reviews;
- event and search results;
- booking emails and confirmations;
- imported itineraries and documents;
- OCR and photos;
- shared notes;
- group messages;
- remembered content from an earlier session.

Attack goals include private-data exfiltration, unsafe group disclosure,
authorization bypass, false-fact injection, direct mutation, booking action,
memory poisoning, and suppression of required warnings.

### Protocol: Travel Injection Suite

Build paired benign/adversarial cases and dynamic multi-turn scenarios. Measure
both the model trajectory and the resulting database/surface state. Include
persistent attacks that reappear through memory and attacks that exploit one
principal's content against another.

Defenses should be evaluated as layers:

- trust labels and provenance;
- separation of data from instructions;
- least-privilege tools;
- audience authorization;
- typed decision actions;
- canonical mutation executors;
- group-safe projection;
- postcondition and receipt validation;
- active removal of poisoned memory.

### Metrics

- attack success rate by goal and source;
- unauthorized tool/action rate;
- private or inferential leakage;
- persistence across sessions;
- benign utility and overblocking;
- final-state integrity;
- detection, containment, and recovery time.

### Falsification and decision gate

Prompt-only defenses do not satisfy this workstream. A model or tool policy may
advance only when structural controls keep prohibited state transitions at
zero in the tested corpus and the residual benign-utility cost is understood.
Live adversarial coverage remains a separate security decision.

### Research output

- travel-specific threat model;
- paired corpus and dynamic attack runner;
- control-ablation report;
- release-blocking security cases.

## 11. RDL-07 — Evaluator science and model promotion

### Research question

When can automated evaluators be trusted to rank Vesper policies, and what
human calibration is required to prevent false-green releases?

### Vesper hypotheses

- Deterministic evaluators should own authorization, privacy, state, receipt,
  freshness, and exact forbidden-output checks.
- Model judges are useful for graded decision and interaction qualities, not as
  the sole arbiter of hard invariants.
- One structured judge call plus a small, stable human-calibration layer may be
  more reliable and economical than many independent free-form judges.
- Judge-family diversity helps detect correlated error but does not establish
  validity by itself.
- Model, prompt, rubric, context compiler, and surface changes can all invalidate
  prior calibration.

### Evaluator stack

Apply evaluators in order:

1. deterministic authorization, state, receipt, privacy, and provenance checks;
2. factuality and freshness checks;
3. decision-action and constraint-satisfaction grading;
4. interaction-quality grading;
5. group-process or proactive-appropriateness grading where relevant;
6. human anchor review and disagreement adjudication;
7. simulator/device evidence for rendered behavior;
8. physical-device evidence before live journey claims.

### Protocol

Create a frozen human-labeled anchor set across every research track. Record
annotator instructions, disagreements, adjudication, and confidence. Evaluate
candidate judges for:

- false-green and false-negative rate;
- agreement by case family and risk;
- calibration, not just correlation;
- position, verbosity, self-preference, and style bias;
- sensitivity to rubric wording;
- drift after model or prompt changes;
- cost and latency.

Hard safety cases remain release-blocking even if aggregate judge agreement is
high.

### Falsification and decision gate

If a judge fails to detect regressions in the human anchor set, it cannot gate
promotion. If human reviewers lack adequate agreement, improve the construct
and rubric before optimizing models against it.

### Research output

- evaluator registry;
- human anchor set and annotation guide;
- calibration report;
- model/prompt/policy promotion protocol;
- drift and rollback policy.

## 12. Shared experimental record

Every offline, shadow, dogfood, or causal trial should emit a common envelope.
The exact storage format is an engineering decision, but the research contract
requires:

| Field family | Required content |
| --- | --- |
| Identity | immutable trial ID, case ID, run ID, parent/variant IDs |
| Revisions | app, backend, workspace, schema, data fixture, model, prompt, policy, evaluator |
| Principals | subject, viewer, audience, relationship scope, experience scope, consent class |
| Evidence | admitted references, excluded references, provenance, freshness, authority |
| Decision | candidates, typed unknowns, allowed actions, selected action, abstain/no-send reason |
| Trajectory | tool calls, canonical executor, errors, retries, latency, token/cost |
| State | initial state, expected state, actual final state, ledger/receipt references |
| Safety | forbidden reads/actions/strings, privacy counterfactuals, reversibility |
| Outcomes | proximal, intermediate, distal, negative; timestamps and observation windows |
| Evaluation | deterministic results, judge outputs, human labels, device layer, adjudication |

The local product-proof fixtures already establish a useful pattern by binding
expected terminal state, effects, evidence, private-string checks, and trial
counts in [product proof fixtures](../../travel-agent/eval/product_proofs/fixtures.py).
The shared record should extend that discipline rather than create an unrelated
evaluation ontology.

## 13. Research waves

### Wave R0 — Contracts and corpus design

- freeze action, claim, memory, intervention, and evaluator vocabularies;
- inventory reusable local fixtures and real anonymized failure modes;
- define human annotation instructions and adjudication;
- establish deterministic baselines before model experiments;
- record the clean integration revisions used for every corpus export.

**Exit:** schemas and rubrics are reviewable; no product behavior changes.

### Wave R1 — Offline baselines

- run deterministic, unconstrained-model, and structured-policy baselines;
- calibrate judges against the human anchor set;
- perform privacy counterfactuals and injection attacks;
- publish category-level errors, not only aggregate scores.

**Exit:** reproducible M/A/H evidence and a decision about which hypotheses
deserve shadow implementation.

### Wave R2 — Shadow observation

- produce decisions without delivering messages or executing mutations;
- compare against actual eligible moments and canonical outcomes;
- measure coverage, latency, missing context, and policy disagreement;
- validate that logs contain propensities and no-send decisions where causal
  work is contemplated.

**Exit:** B evidence on a pinned backend revision, with zero user-visible
behavior attributed to the shadow system.

### Wave R3 — Controlled dogfood

- begin with private, reversible, low-cost surfaces;
- use explicit flags, cohorts, cooldowns, and kill switches;
- bind each result to app build, backend deploy, data state, and policy version;
- run group-visible work only after multi-device privacy and projection gates.

**Exit:** D/V evidence for the exact scoped behavior. This is still not broad
release authorization.

### Wave R4 — Causal learning and promotion

- randomize only among pre-approved safe treatments including no-send;
- evaluate delayed and negative outcomes;
- promote policies only through the calibrated evaluator and device gates;
- retain holdouts and rollback paths.

**Exit:** C evidence for the defined population and outcome window, plus a
separate product decision about broader rollout.

Corpus-size targets in early waves are coverage targets, not statistical-power
claims. Power, minimum detectable effect, and duration must be calculated from
pilot event rates before any live causal study.

## 14. Explicit deferrals

The following are intentionally outside the first research cycle:

- fine-tuning a general travel model before policy and evaluator baselines are
  stable;
- unconstrained autonomous itinerary or booking execution;
- a universal memory store with every conversation as durable truth;
- live group facilitation before inferential-privacy and multi-device gates;
- personalization optimized directly for taps or response rate;
- model self-certification;
- replacing deterministic domain authorities with LLM-generated facts;
- cross-user learning that cannot preserve principal-level consent and
  deletion.

## 15. Primary literature and external benchmarks

### Decision and elicitation

- [COPE: stage-aware conversational preference elicitation](https://arxiv.org/abs/2607.06765)
- [DECISIVE: decision-oriented preference elicitation](https://aclanthology.org/2026.acl-long.1465/)
- [Asking clarifying questions for preference elicitation](https://research.google/pubs/asking-clarifying-questions-for-preference-elicitation-with-large-language-models/)
- [How much should an AI ask?](https://elischolar.library.yale.edu/cowles-discussion-paper-series/2968/)
- [When more questions make conversational recommendation worse](https://aclanthology.org/2025.coling-main.561/)
- [Conformal abstention policies](https://proceedings.mlr.press/v304/tayebati26a.html)
- [Limits of conformal risk control](https://arxiv.org/abs/2606.29054)
- [Psychology-aware preference construction](https://link.springer.com/article/10.1007/s10844-021-00674-5)

### Memory

- [LongMemEval](https://arxiv.org/abs/2410.10813)
- [LoCoMo-Plus](https://aclanthology.org/2026.acl-long.1150/)
- [LongMemEval-V2](https://arxiv.org/abs/2605.12493)
- [GateMem](https://arxiv.org/abs/2606.18829)

### Group decision systems

- [Real-time group dynamics with LLM facilitation](https://arxiv.org/abs/2605.14097)
- [Bringing everyone to the table](https://arxiv.org/abs/2508.08242)

### Causal proactivity

- [Micro-randomized trials for just-in-time interventions](https://pmc.ncbi.nlm.nih.gov/articles/PMC8887814/)
- [Push engagement versus target behavior](https://pmc.ncbi.nlm.nih.gov/articles/PMC12779098/)
- [Delayed uplift modeling](https://ojs.aaai.org/index.php/AAAI/article/view/38686)
- [Off-policy evaluation for slate recommendations](https://proceedings.neurips.cc/paper/2017/hash/5352696a9ca3397beb79f116f3a33991-Abstract.html)

### Agent security and evaluators

- [AgentDojo](https://proceedings.neurips.cc/paper_files/paper/2024/hash/97091a5177d8dc64b1da8bf3e1f6fb54-Abstract-Datasets_and_Benchmarks_Track.html)
- [AgentDyn](https://arxiv.org/abs/2602.03117)
- [PiSAs: multi-user contextual integrity](https://arxiv.org/abs/2607.05318)
- [Judging LLM-as-a-judge with MT-Bench](https://proceedings.neurips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html)
- [Judging the judges](https://aclanthology.org/2025.gem-1.33/)
- [SAJA: structured assessment with judge adaptation](https://aclanthology.org/2026.acl-industry.45/)

## 16. Research-to-engineering handoff

A research result enters engineering only when it contains:

1. a versioned construct and hypothesis;
2. a reproducible corpus or data definition;
3. at least one deterministic or simple baseline;
4. category-level results and known failure modes;
5. safety, privacy, and scope implications;
6. a falsification result or explicit uncertainty;
7. the evidence layer actually achieved;
8. a proposed rollout and rollback boundary.

The implementation sequence, worktree isolation, contracts, gates, and backlog
for that handoff live in the separate
[AI decision and learning engineering plan](ai-decision-and-learning-engineering-plan-2026-08-10.md).
