---
doc_type: working
status: active
owner: AI systems / evaluation / product
created: 2026-08-10
last_verified: 2026-08-10
expires: 2026-09-09
why_new: Converts the AI decision-and-learning research agenda into a gated engineering workstream that remains isolated from the four active intentional-convergence worktrees.
source_of_truth_for:
  - ai-decision-and-learning-engineering-workstream-2026-08
related:
  - ai-decision-and-learning-research-agenda-2026-08-10.md
  - intentional-convergence-engineering-plan-2026-08-10.md
---

# AI decision and learning engineering plan

## 1. Executive decision

Create a fifth, explicitly separate program named **Workstream AI-DL — Decision
and Learning**. It will build the evaluation spine and bounded policy layer that
let Vesper learn when to ask, recommend, propose, act through canonical paths,
remember, facilitate, and stay silent.

This is **not Worktree E in the current convergence round**. It is not a fifth
peer modifying the same product surfaces while Worktrees A–D are active. The
four convergence lanes remain the priority because they repair the truth,
scope, delivery, and projection contracts on which responsible AI behavior
depends.

The recommended execution is:

1. While A–D are active, do only research artifacts, schemas, fixture design,
   baselines, and read-only analysis that cannot collide with their code.
2. After the A–D integration candidate is recorded, create one coordinated
   AI-DL workspace lane from those exact workspace/backend/mobile revisions.
3. Build the evaluation and decision contracts before changing user-visible AI
   behavior.
4. Progress from offline to shadow to private dogfood to causal canary.
5. Treat group-visible and mutating behavior as later, separately gated phases.

The companion [research agenda](ai-decision-and-learning-research-agenda-2026-08-10.md)
owns the questions and evidence needed to answer them. This document owns the
engineering sequence and boundaries.

## 2. Authority and non-overlap with the convergence worktrees

The current [intentional convergence engineering plan](intentional-convergence-engineering-plan-2026-08-10.md)
has four active implementation lanes:

| Lane | Contract AI-DL will consume | AI-DL must not duplicate |
| --- | --- | --- |
| **A — evidence integrity** | truthful evidence levels, immutable receipts, generated status, device-proof semantics | certification scripts, current-state generation, journey evidence repair |
| **B — Home truth** | honest unavailable/partial/empty states, correct cache identity, reliable private Home projection | Trips/Places Home state fixes, save/proposal invalidation, door routing |
| **C — context trust** | relationship and experience scope, applicability/revocation, viewer-safe public projection | current context compiler, profile, outcome, roster, and privacy fixes |
| **D — map/projection** | grounded spatial facts, freshness, canonical Plan/Map revision coherence | Riviera/map/search transport and projection implementation |

AI-DL must not edit those worktrees or assume their unlanded interfaces. During
their execution, this workstream may add only isolated docs, proposed schemas,
new fixtures, and evaluation code whose dependency boundary is explicit and
whose files do not overlap active ownership.

### Start gate

Runtime implementation begins only after the integration owner records:

- workspace base SHA;
- backend base SHA;
- mobile base SHA;
- A–D landed or explicitly deferred commits;
- passing cross-repo contract check;
- known dirty worktrees and ownership;
- current evidence-layer report.

If one convergence lane is deferred, this plan must mark the dependent AI-DL
phase unavailable rather than recreating the missing contract locally.

## 3. Product and architecture boundary

AI-DL is a decision control plane around existing domain authorities. It does
not become a new source of trip, place, route, weather, booking, or itinerary
truth.

```text
domain truth + provenance + freshness
relationship scope + experience scope + viewer/audience
                     │
                     ▼
             authorized DecisionState
                     │
                     ▼
        bounded policy + deterministic vetoes
                     │
     ┌───────────────┼────────────────┐
     ▼               ▼                ▼
 ask/show/recommend  abstain/silent   propose/execute intent
     │               │                │
     └───────────────┴────────┬───────┘
                              ▼
            canonical executor / group-safe composer
                              │
                              ▼
              state + projection + visible receipt
                              │
                              ▼
            outcome evidence → ClaimCandidate gate
                              │
                              ▼
                  governed, correctable memory

          evaluation and audit envelope surrounds every step
```

The model may rank or select among authorized bounded actions. It may not:

- invent domain facts;
- override audience or authorization rules;
- write a proposal, itinerary, booking, or expense through a parallel writer;
- convert a group outcome directly into a personal preference;
- certify its own correctness;
- reinterpret a failed or stale dependency as an authoritative empty result.

## 4. Core contracts

These are proposed logical contracts. Names and module locations should be
finalized after the A–D integration base is known; they are not instructions to
create duplicate types beside contracts already landing in those lanes.

### 4.1 DecisionState

One immutable, serializable input to a policy decision:

| Field family | Minimum content |
| --- | --- |
| Identity | decision ID, request/turn ID, trip or local occasion, timestamps |
| Principals | subject, viewer, audience, relationship scope, experience scope |
| Evidence | references, source authority, freshness, validity, trust class |
| Options | stable option IDs and objective attributes; no free-text-only identity |
| Feasibility | hard constraints, route/time/weather/cost/availability status |
| Preferences | claims with subject, source, durability, scope, and applicability |
| Unknowns | typed uncertainty, materiality, and possible resolving action |
| Authority | allowed reads, allowed speech acts, allowed canonical executors |
| Risk | audience, reversibility, cost, time pressure, mutation class |
| Policy | policy, prompt, model, feature-flag, and schema versions |

The current backend `AIRunContext` carries trip/workflow/occasion and can carry
`RelationshipScope`, but production scope construction and `ExperienceScope`
coverage are incomplete. AI-DL should consume the Worktree C contract rather
than adding a competing scope mechanism in
[AI run context](../../travel-agent/backend/core/ai_runs.py).

### 4.2 DecisionAction

The first policy action set should be narrow:

- `ask_attribute`;
- `ask_item_comparison`;
- `show_options`;
- `recommend`;
- `propose_canonical_change`;
- `request_execution_confirmation`;
- `execute_canonical` only when authorization is independently satisfied;
- `abstain`;
- `silent`.

Every result carries a reason code, admitted evidence references, unresolved
material unknowns, confidence/calibration metadata, and the next permitted
action. Free-form copy is a downstream projection of the action, not the
policy's primary output.

### 4.3 ClaimCandidate

Outcome and interaction learning should emit a candidate with:

- subject and predicate/value;
- evidence type and source reference;
- explicitness and recommendation-exposure status;
- source, relationship, companion, and occasion scope;
- `valid_from`, optional `valid_to`, and observed time;
- occurrence confidence separate from preference confidence;
- counterevidence and supersession links;
- proposed durability/promotion tier;
- confirmation, correction, and removal status;
- policy and model versions that produced the candidate.

No ClaimCandidate becomes durable merely because a model emitted it.

### 4.4 InterventionDecision

Proactive instrumentation needs:

- eligibility and exclusion reasons;
- safe candidate treatments;
- treatment probabilities including no-send;
- chosen treatment, surface/channel, and cooldown state;
- policy/context versions;
- delivery and device receipt;
- proximal, intermediate, distal, and negative outcome windows;
- censoring and competing-intervention fields.

### 4.5 EvalTrial

Extend the discipline already present in
[product-proof fixtures](../../travel-agent/eval/product_proofs/fixtures.py):

- initial and expected terminal state;
- actual terminal state;
- exact expected/forbidden effects and strings;
- evidence and scope inputs;
- model/prompt/policy/evaluator revisions;
- tool trajectory and canonical writer used;
- deterministic, judge, human, simulator, and physical-device results;
- immutable artifact references.

## 5. Phase plan

### Phase AI-0 — Evaluation spine and immutable contracts

**Purpose:** make every later model or policy comparison reproducible without
changing product behavior.

**Work:**

- establish versioned schemas for DecisionState, DecisionAction,
  ClaimCandidate, InterventionDecision, and EvalTrial;
- create a registry for corpora, policies, prompts, models, evaluators, and
  evidence artifacts;
- adapt existing product-proof, journey, ambient, experience-loop, and AI-run
  records into the common EvalTrial envelope without discarding their domain
  receipts;
- build deterministic validators for authorization, audience, private-string
  exclusion, freshness, canonical writer, final state, receipt, and
  reversibility;
- create a frozen human anchor set and annotation/adjudication guide;
- record current deterministic and model baselines before optimization;
- add generated reports that never promote M/A evidence to D/V evidence.

**Likely ownership:** backend evaluation packages and workspace evidence/docs.
Mobile work is limited to consuming existing device receipts; no new UI.

**Exit gate:**

- fixtures replay on a pinned integration revision;
- report identifies every artifact and evaluator version;
- deterministic safety checks cannot be overridden by a model score;
- deliberate false-green fixtures are caught;
- evidence labels remain distinct end to end.

**Claim allowed at exit:** “AI-DL evaluation spine passes its offline fixture
suite at M/A/H on revision X.” Not “AI behavior is complete.”

### Phase AI-1 — Bounded decision policy in offline and shadow modes

**Purpose:** replace implicit one-shot answer generation with an inspectable
choice among bounded moves.

**Work:**

- build the Vesper Decision Set from the research agenda;
- implement simple deterministic baselines first;
- add a structured policy that consumes DecisionState and emits
  DecisionAction;
- keep deterministic vetoes for unavailable evidence, wrong scope,
  unauthorized audience, irreversible action, and canonical-executor absence;
- add action-specific copy composition only after the decision result exists;
- build a policy router that can choose deterministic, fast-model,
  high-quality-model, ask, or abstain paths by risk and expected value;
- run shadow decisions beside selected concierge turns without changing the
  user-visible response or executing a mutation;
- include system-triggered and no-response cases; the existing generic quality
  sampler excludes important proactive behavior and cannot be the sole judge.

**Exit gate:**

- structured policy exceeds deterministic and unconstrained baselines on the
  predeclared decision metrics;
- no regression on privacy, authorization, freshness, state, or receipt gates;
- shadow coverage, latency, disagreement, and missing-context rates are known;
- the integration owner approves any live surface adapter separately.

**Rollback:** disable the policy flag and retain the prior response path. No
state migration or durable learning depends on the new policy.

### Phase AI-2 — Claim promotion and governed memory

**Purpose:** turn outcomes into correctable learning without converting
behavioral residue into unscoped profile truth.

**Work:**

- implement ClaimCandidate production behind an audit-only flag;
- preserve the current outcome doctrine: an inferred occurrence is not itself
  a preference update;
- add conservative deterministic promotion tiers for explicit statements,
  explicit corrections, repeated scoped evidence, and ambiguous inference;
- require exact subject, companion/relationship, occasion, and validity scope;
- make roster changes invalidate applicability that depended on the departed
  member, not merely claims authored by that member;
- implement authorization-first retrieval, temporal/supersession resolution,
  correction, and active-forgetting verification;
- run Claim Promotion Lab and MemoryBench cases through final decisions;
- add a user-legible provenance/correction projection only after Worktree C's
  viewer-safe profile contract is available.

**Exit gate:**

- zero cross-principal and wrong-roster application in the release-blocking
  corpus;
- correction and forgetting remove downstream behavioral influence, not only
  the source row;
- governed memory improves decision quality over explicit-only memory without
  breaching the hard contamination budget;
- migrations and deletion behavior are reversible and audited;
- any visible correction flow has D/V evidence for its exact surface.

**Rollback:** disable inferred promotion, retain ClaimCandidates for audited
analysis only where consent and retention permit, and fall back to explicit
scoped claims.

### Phase AI-3 — Group Decision Lab and dark bounded facilitator

**Purpose:** establish whether Vesper can improve group process and decisions
without privacy leakage or invisible steering.

**Work:**

- implement deterministic aggregation baselines over group-safe projections;
- define bounded facilitator actions; do not expose a general free-form group
  agent;
- route every group-visible candidate through
  `travel-agent/backend/concierge/group_compose.py` or an explicitly reviewed
  equivalent boundary;
- build direct and counterfactual inferential-privacy tests;
- compare hard constraints, average, disagreement-aware, max-min, sequential
  fairness, and explicit organizer-authority policies;
- record participation, coverage, decision, fairness, and steering outcomes
  separately;
- keep the entire facilitator dark/shadow until group device prerequisites are
  satisfied.

**Exit gate for dark implementation:**

- deterministic and model policies replay reproducibly at M/A/H;
- zero direct privacy disclosure in release-blocking cases;
- inferential leakage is characterized with an approved threshold and known
  residual risks;
- no group proposal bypasses the canonical proposal builder or receipt path;
- product approves one narrow use case for device dogfood.

This phase does **not** authorize group-visible rollout.

### Phase AI-4 — Proactive eligibility and causal instrumentation in shadow

**Purpose:** create a valid learning loop before sending more messages.

**Work:**

- define eligible decision points and hard exclusions;
- log complete InterventionDecision records, including no-send and treatment
  probabilities;
- preserve quiet hours, cooldowns, channel eligibility, consent, and global
  kill switches as deterministic controls;
- model candidate value, interruption cost, delayed outcomes, and negative
  outcomes without delivering new interventions;
- validate delivery/observation joins and missingness;
- calculate event rates and a real power/duration plan for a future
  micro-randomized trial;
- distinguish private Home cards, private inbox messages, and private pushes;
  do not combine their outcomes as one treatment.

**Exit gate:**

- eligible and excluded events reconcile to source truth;
- propensities, no-send, delayed outcomes, and negative outcomes are complete
  enough for the declared analysis;
- shadow policy stays inside latency/cost budgets;
- consent and study protocol receive product/privacy approval;
- private surface has passed its convergence and device gates.

### Phase AI-5 — Private earned-proactivity canary

**Purpose:** learn whether a narrow, reversible intervention creates distal
value compared with silence.

**Initial scope:** one private surface, one decision family, one declared
population, and pre-approved treatments that include no-send. No group delivery,
booking, direct itinerary mutation, or inferred durable learning.

**Work:**

- implement cohort/consent checks and stable randomization;
- bind delivery receipts to app build, backend deploy, policy, and context;
- operate cooldown, quiet-hour, fatigue, and kill-switch controls;
- monitor safety and negative outcomes continuously;
- analyze the predeclared proximal, intermediate, distal, and negative windows;
- retain a no-send holdout and delayed-outcome correction.

**Exit gate:**

- physical-device proof exists for eligibility, delivery, deep link, dismissal,
  cooldown, and kill switch;
- no privacy, stale-state, wrong-scope, or phantom-delivery defect is open;
- the causal analysis shows incremental distal value, not merely opens;
- trust/negative outcomes remain inside the predeclared budget;
- product makes an explicit promote, iterate, or stop decision.

**Rollback:** global policy off, surface flag off, scheduled candidates canceled
without deleting audit history, and user-visible state remains truthful.

### Phase AI-6 — Travel injection suite and adaptive model routing

**Purpose:** harden the decision system and spend model cost only where it buys
measured value.

**Work:**

- run place/review/event/search/booking-email/import/OCR/photo/shared-note/group-
  message/memory attacks;
- test cross-principal and persistent memory poisoning;
- add least-privilege tool scopes and state postconditions where gaps remain;
- compare deterministic, fast, high-quality, ask, and abstain routes;
- calibrate model judges against the frozen human anchor set;
- introduce a promotion registry with policy/model/judge revisions and rollback;
- rerun calibration after any model, prompt, rubric, context compiler, or
  surface change.

**Exit gate:**

- prohibited state transitions remain zero in release-blocking attack cases;
- attack success and benign overblocking meet approved category-level budgets;
- routing reduces cost/latency without degrading hard invariants or declared
  decision quality;
- rollback restores the prior model/policy without data repair.

Security evidence from this suite is necessary but not a substitute for a
broader security review.

### Phase AI-7 — Narrow group-visible canary, if research supports it

**Purpose:** test one bounded facilitation move in the real multi-device group
loop.

This phase is optional. It proceeds only if RDL-04 shows decision or procedural
value beyond a deterministic baseline.

**Prerequisites:**

- Worktrees A–D integrated;
- roster revocation and viewer-safe scope proven;
- group composition and canonical proposal paths verified;
- inferential-privacy cases pass;
- Plan/Map projections share the accepted revision;
- physical multi-member device script and explicit participant consent exist.

**Allowed first canary examples:** ask for one missing group-safe criterion;
show a disagreement-safe shortlist; propose a reversible vote. No hidden
organizer authority and no explanation derived from private constraints.

**Exit gate:** direct and inferential privacy, decision quality, participation,
steering, state coherence, receipts, and device evidence all pass separately.
A pleasant group chat is not sufficient evidence.

## 6. Work packages and dependency graph

| ID | Package | Depends on | Primary artifact | Earliest safe phase |
| --- | --- | --- | --- | --- |
| AI-001 | Common EvalTrial envelope | A evidence semantics | schemas + adapters | AI-0 |
| AI-002 | Deterministic invariant validators | A; canonical writers | validator library | AI-0 |
| AI-003 | Human anchor set and annotation guide | research agenda | corpus + adjudication | AI-0 |
| AI-004 | DecisionState adapter | C scope contract; D freshness contract | immutable context builder | AI-1 |
| AI-005 | DecisionAction policy and router | AI-001–004 | offline/shadow policy | AI-1 |
| AI-006 | Decision Set runner and report | AI-001, AI-003 | evaluation suite | AI-1 |
| AI-007 | ClaimCandidate ledger | C roster/scope; outcome authority | audit-only candidate store | AI-2 |
| AI-008 | Governed memory retrieval and forgetting | AI-007 | retrieval pipeline + tests | AI-2 |
| AI-009 | Group aggregation baselines | C group-safe projection | Group Lab | AI-3 |
| AI-010 | Bounded facilitator and privacy counterfactuals | AI-005, AI-009 | dark policy | AI-3 |
| AI-011 | InterventionDecision logging | A receipts; B delivery surfaces | shadow ledger | AI-4 |
| AI-012 | Causal analysis and experiment registry | AI-011 | analysis plan + reports | AI-4 |
| AI-013 | Private proactive canary | B device-valid surface; AI-011–012 | one scoped experiment | AI-5 |
| AI-014 | Travel Injection Suite | AI-004–010 | security corpus/runner | AI-6 |
| AI-015 | Model/evaluator promotion registry | AI-003, AI-006, AI-014 | governed promotion | AI-6 |
| AI-016 | Narrow group device canary | A–D; AI-009–010; group V gate | device-bound study | AI-7 |

The dependency direction is intentional: AI-DL consumes scope, evidence, and
projection truth. It must not make those contracts depend on a particular model
or policy.

## 7. Test and evidence matrix

| Concern | Deterministic/fixture | Backend-real | Device | Human/causal |
| --- | --- | --- | --- | --- |
| Decision action | allowed-action and forbidden-evidence checks | shadow replay on real scoped state | exact rendered action/deep link | decision usefulness and trust |
| Claim promotion | longitudinal promotion/correction cases | persisted applicability and deletion | correction/provenance UI | comprehension and downstream utility |
| Memory | authorization, version, forgetting cases | final-decision behavior on real store | viewer-specific rendering | user correction burden |
| Group | aggregation and privacy counterfactuals | canonical proposal + group composer | physical multi-member Plan/Map/chat | fairness, steering, inclusion, decision quality |
| Proactivity | eligibility and no-send replay | real decision-point logging | receipt, cooldown, kill switch | randomized distal and negative outcomes |
| Security | paired and dynamic attacks | final-state/postcondition checks | attack-bearing import/render paths | red-team review where warranted |
| Evaluators | frozen anchor regressions | versioned report generation | evidence-layer integrity | reviewer agreement and judge calibration |

Each phase report must include failures and exclusions. A skipped device or human
layer remains `not_run`; it must not be serialized as pass.

## 8. Rollout controls

Every runtime phase needs independently operable controls:

- global AI-DL kill switch;
- per-policy and per-surface enablement;
- shadow-only mode;
- allowlisted cohort;
- model and prompt pinning;
- deterministic fallback;
- max latency/cost and circuit breaker;
- per-user cooldown and quiet hours for interventions;
- no-send eligibility reason;
- durable audit/receipt even after rollback;
- independent disablement of inferred claim promotion;
- independent disablement of group-visible composition and mutation intents.

Flags must be declared in the canonical registry and checked by the same
governance tooling as backend and app flags. A flag without a production
consumer or a consumer without a registry entry is a failing integration
condition, not a harmless documentation issue.

## 9. Worktree and session topology

### While A–D are active

Keep this orchestration workspace read-mostly for planning. Do not start a
second implementation of context, Home, evidence, or map contracts. Safe work
is limited to:

- the two AI-DL planning documents;
- corpus manifests and anonymized fixture specifications in new paths;
- evaluator rubric design;
- read-only baseline analysis;
- proposed schemas that do not become imported runtime dependencies.

### After the convergence integration candidate

Create one coordinated workspace lane, for example:

```text
travel-workspace--ai-decision-learning/
  travel-agent/   # dedicated backend worktree from recorded integration SHA
  travel-app/     # added only for phases that require a mobile surface
```

Use the workspace worktree scripts where possible. Record all three base SHAs
in the branch notes and first PR. Do not reuse one of the four convergence
worktrees after it lands; that obscures lineage and ownership.

### Recommended staffing pattern

Use one durable integration session as owner. It owns schemas, migrations,
contract changes, flags, cross-repo tests, and final evidence. It may delegate
bounded, non-overlapping tasks after the file graph is stable:

- corpus/fixture construction;
- deterministic validator implementation;
- baseline model runs and error analysis;
- security attack generation;
- human-annotation tooling;
- read-only review of privacy, causal design, or evaluator calibration.

Do not let parallel agents independently modify shared core contracts, database
migrations, generated OpenAPI files, or the same evaluation registry. Those
remain single-owner integration work.

## 10. Proposed module boundaries

Final paths require codebase review after integration. The desired ownership is
more important than these provisional names:

```text
travel-agent/
  backend/core/decision/          # typed state/action and deterministic vetoes
  backend/core/learning/          # candidate promotion, correction, forgetting
  backend/concierge/              # thin surface adapters and safe composition
  eval/decision_policy/           # Decision Set and reports
  eval/memory/                    # Claim Lab and MemoryBench
  eval/group_decision/            # aggregation, facilitation, privacy
  eval/proactivity/               # eligibility, shadow, causal analysis
  eval/security/                  # Travel Injection Suite
  eval/calibration/               # human anchors and judge calibration

travel-app/
  data/                           # generated/API consumers only when needed
  features/...                    # one narrow private or group canary surface

workspace/
  docs/working/                   # agenda, plan, decision records
  docs/evidence/                  # immutable/generated evidence references
  scripts/                        # cross-repo checks, not model business logic
```

Before creating a module, search for the existing authority. Extend the context
compiler, outcome pipeline, proposal builder, group composer, and product-proof
harness where appropriate; do not create parallel writers or truth stores.

## 11. Engineering acceptance rules

### Always true

- A private constraint never reaches a group-visible surface, directly or by a
  trivially inferable explanation.
- Group-bound text uses the sanctioned group-safe composition path.
- A stale, failed, mocked, or unavailable dependency is represented honestly.
- Proposal, itinerary, booking, and expense changes use canonical writers,
  ledger events, visible receipts, and truthful reversal.
- A model suggestion is not mutation authority.
- An inferred occurrence is not automatically a durable preference.
- Scope includes subject, viewer, relationship/companion, experience/occasion,
  time, and audience where applicable.
- No experiment randomizes privacy, authorization, required warnings, or
  irreversible safety.
- No result is described beyond its achieved evidence layer.

### Definition vocabulary

| Term | Required evidence |
| --- | --- |
| **research-supported** | stated hypothesis, reproducible protocol, relevant H/A/M or C result, limitations |
| **implemented dark** | code exists behind unreachable/disabled path; S/M/B only as stated |
| **shadow-verified** | decisions recorded on real backend state with no user-visible action; B |
| **device-validated** | exact scoped flow passed on recorded physical device/build/deploy; V |
| **causally supported** | predeclared analysis identifies incremental effect for stated population/window; C |
| **release-approved** | separate product/security/release decision after all required gates |

“Research-supported” and “implemented dark” do not imply “device-validated” or
“release-approved.”

## 12. Risks and mitigations

| Risk | Consequence | Mitigation |
| --- | --- | --- |
| AI-DL starts before A–D settle | duplicate scope/evidence/projection systems | enforce recorded integration start gate |
| One universal score hides safety regressions | fluent but unsafe promotion | hard deterministic gates plus category metrics |
| Preference inference becomes self-fulfilling | recommendations manufacture memory | record recommendation exposure; conservative promotion |
| Retrieval precedes authorization | cross-principal leakage | authorize before semantic retrieval |
| Group explanations leak by implication | unrecoverable trust event | counterfactual inferential-privacy tests + group composer |
| Engagement becomes the target | more taps, no traveler value | no-send holdout and distal/negative outcomes |
| Judge overfitting | false-green model promotion | frozen human anchors, drift checks, deterministic gates |
| Shadow logs lack propensities/no-send | invalid causal inference | InterventionDecision completeness gate |
| Model path creates a second writer | incoherent plan state | canonical executor adapters only |
| Parallel sessions collide | mixed branches and unreviewable changes | single integration owner; filename-explicit commits |
| Offline evidence becomes release language | unsupported product claims | evidence-layer-aware generated reports |

## 13. First two execution rounds

### Round AI-R0 — now, without colliding with A–D

1. Approve the research constructs and explicit deferrals.
2. Inventory existing fixtures, evaluators, logs, and receipts against the
   shared experimental record.
3. Draft Decision Set, Claim Lab, MemoryBench, Group Lab, and Injection Suite
   manifests in new isolated paths.
4. Freeze the first human annotation guide and adjudication protocol.
5. Select deterministic baselines and predeclare category metrics.
6. Record unresolved dependencies on A–D; do not patch around them.

**Deliverable:** reviewable research assets and a dependency report. No runtime
behavior or release claim.

### Round AI-R1 — after A–D integration

1. Create the dedicated AI-DL workspace/backend worktrees from recorded heads.
2. Implement Phase AI-0 schemas, validators, adapters, and reports.
3. Replay current product proofs and deliberate false-green cases.
4. Establish the human-anchor and evaluator baseline.
5. Implement Phase AI-1 deterministic and structured decision policies
   offline.
6. Decide whether shadow integration is justified by the preregistered gate.

**Deliverable:** reproducible M/A/H baseline and an explicit promote/iterate/stop
decision for shadow work.

Do not schedule Phase AI-2 or later by calendar alone. Each begins only when its
dependency and evidence gates are satisfied.

## 14. Immediate decisions requested

Before runtime implementation, product and engineering should explicitly agree
on:

1. the initial narrow decision family for the Decision Set;
2. which inferred evidence, if any, may ever become durable without explicit
   confirmation;
3. the first private surface eligible for a future causal canary;
4. the hard privacy and contamination budgets, which should be zero for
   release-blocking wrong-person/group cases;
5. the human anchor owners and adjudication cadence;
6. the integration SHA and owner after A–D land;
7. whether the optional group canary remains in scope after offline research.

The default when these are unresolved is conservative: evaluate offline,
remain silent in production, retain no unjustified durable claim, and route no
new mutation or group-visible message.
