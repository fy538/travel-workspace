---
doc_type: working
status: active
owner: AI systems / evaluation
created: 2026-08-10
last_verified: 2026-08-10
expires: 2026-09-09
why_new: Records the reproducible starting point for AI-R0 by mapping existing evaluation assets to the new decision, learning, group, proactive, security, and evaluator contracts.
source_of_truth_for:
  - ai-decision-and-learning-r0-baseline-inventory-2026-08
related:
  - ai-decision-and-learning-r0-fixture-manifest-2026-08-10.md
  - ai-decision-and-learning-research-agenda-2026-08-10.md
  - ai-decision-and-learning-engineering-plan-2026-08-10.md
---

# AI-R0 baseline inventory

## 1. Verdict

The repository has a credible set of specialized evaluation assets, but not yet
one AI decision-and-learning harness. The correct next move is adapter work and
shared evidence envelopes, not a second independent evaluator framework.

Current assets provide:

- product-level postcondition and privacy checks;
- deterministic taste-quality floors;
- fixture-level proactive relevance calibration;
- correction-aware memory projection checks;
- observational repeat-occasion metrics;
- a generic LLM taste judge.

They do not yet provide:

- a typed `DecisionState` and bounded `DecisionAction` contract;
- one trial envelope carrying scope, evidence, action, state, receipt, and
  evaluator revisions;
- claim promotion policy across personal, relationship, companion, and
  occasion scopes;
- authorization-first, temporal, multi-principal memory evaluation;
- group aggregation and inferential-privacy evaluation;
- causal intervention logs with propensity/no-send/delayed outcomes;
- travel-specific injection attacks and final-state assertions;
- a frozen human anchor set with judge calibration.

This is an inventory finding, not a product defect verdict. The specialized
evaluators should remain valuable while their adapters are built.

## 2. Reproducible commands and results

Commands were run on 2026-08-10 from the current backend branch using its
existing `.venv`, with no provider calls, database writes, or model judge calls.
The results are fixture evidence only.

### 2.1 Product proofs

```text
PYTHONPATH=. .venv/bin/python -c \
  'from eval.product_proofs.fixtures import TASKS; \
   from eval.product_proofs.run_eval import grade_records; \
   r=grade_records({}); print(r["task_count"], r["passed_count"])'
```

Result:

```text
task_count=24 passed_count=0
```

The empty-record run is expected: no observed trials were supplied, so every
task correctly remains unproven. The task bank is distributed as:

| Proof | Tasks | Coverage |
| --- | ---: | --- |
| P01 | 5 | occasion shape, idempotency, scope, private input, honesty |
| P02 | 5 | spatial reachability, fallback, provenance, accessibility, freshness |
| P03 | 5 | outcome proposal, confirmation, correction, rejection, receipt/privacy |
| P04 | 4 | repeat context, private correction, uncertainty, measurement |
| P06 | 5 | silence, consent, safety, notification/mutation boundaries |

The existing `ProductProofTask` and `grade_trial` already express:

- expected terminal state;
- required and forbidden effects;
- required evidence references;
- forbidden shared text;
- independent trial counts;
- observed tool effects rather than desired response text.

This is the strongest adapter source for `EvalTrial` hard gates. It still lacks
explicit principal/viewer/relationship/experience scope, action taxonomy,
freshness metadata, canonical-writer identity, and device-evidence identity.

### 2.2 Ambient relevance calibration

```text
PYTHONPATH=. .venv/bin/python -c \
  'from eval.ambient.relevance_calibration import run_fixture_calibration, render_report; \
   print(render_report(run_fixture_calibration()))'
```

Result:

```text
cases=6 labeled=5 judged=5 accepted=2
unknown_verdicts=1 unknown_verdict_rate=16.7%
tp=1 fp=1 fn=1 tn=2
precision=50.0% recall=50.0%
structured_verdicts=5 evidence_complete_rate=80.0%
```

This is a useful contract test for `should_fire`, unknown handling, and evidence
completeness. It is not a live relevance-quality estimate. The small confusion
matrix is a baseline for the admission rule, not a launch threshold.

### 2.3 Taste-quality hard checks

The six existing fixtures were ranked in-process and passed deterministic hard
checks without invoking the LLM judge:

| Fixture family | Result |
| --- | --- |
| seeded city / corpus | pass |
| unseeded city / provider-only | pass |
| cold user | pass |
| taste mismatch | pass |
| substring trap | pass |
| null meters/unicode/mixed case torture | pass |

The evaluator correctly separates hard trust invariants from the optional judge
quality bar. It remains a single ambient-surface evaluation, not a decision
policy or group/privacy evaluator.

### 2.4 Experience-loop metrics

The existing pure fixture run preserves unknown outcomes:

```text
measured_count=1
completion_rate=None
median_intent_to_action_minutes=None
mean_external_checks_required=None
mean_quality_rating=None
repeats=[]
```

This is aligned with the research agenda: no completion timestamp is not a
failure. The evaluator computes observational first/second-occasion effort and
quality deltas; it does not identify causal uplift or distinguish all
recommendation-induced behavior.

### 2.5 Dependency note

Running the same ambient import with the system Python failed because the
workspace environment does not expose SQLAlchemy. The backend `.venv` is the
valid offline evaluation environment for this branch. This is an environment
receipt, not a code-quality claim.

## 3. Asset-to-manifest mapping

| AI-R0 manifest | Existing asset | Reuse | Missing adapter work |
| --- | --- | --- | --- |
| DS / Decision Set | product proofs, taste fixtures, spatial/product tests | terminal/effect/privacy patterns | DecisionState, action set, acceptable-action labels, scope/freshness |
| CPL / Claim Promotion Lab | outcome reconciliation, experience loop, memory loop | correction and unknown semantics | claim candidate, promotion tiers, recommendation exposure, roster applicability |
| MB / MemoryBench | memory loop, preference engine tests, context compiler fixtures | projection/correction patterns | authorization-first retrieval, temporal resolution, forgetting, false premise |
| GDL / Group Decision Lab | group composer tests, multiplayer research fixtures | group-safe output boundary | aggregation baselines, fairness, steering, inferential privacy |
| PDL / Proactivity Ledger | ambient relevance calibration, notification outcome code | unknown/no-fire handling | eligibility, propensities, no-send, delayed/negative outcomes |
| TIS / Travel Injection Suite | inbound extraction and tool safety tests | untrusted evidence examples | paired attack corpus, persistent poisoning, final-state assertions |
| HAU / Human Anchor Set | taste judge rubric, product-proof human review where available | rubric vocabulary | frozen cross-family anchors, inter-rater labels, judge calibration |

## 4. Existing asset details

### Product proofs

Source: `travel-agent/eval/product_proofs/fixtures.py` and `grader.py`.

Strengths:

- treats observed effects and terminal state as authoritative evidence;
- supports required/forbidden effects and evidence references;
- explicitly tests private text not reaching shared surfaces;
- requires repeated trials for sensitive cases;
- can grade without an LLM or provider.

Adapter requirements:

- map `category` and `proof_id` to RDL case families;
- add principal, viewer, audience, relationship, and experience scope at the
  trial boundary;
- record evidence provenance/freshness and excluded evidence;
- identify the canonical executor/writer for mutation-capable effects;
- bind backend/app/build/deploy and device evidence when later available;
- distinguish a model-selected action from the executor result.

### Experience loop

Source: `travel-agent/eval/experience_loop/metrics.py` and `memory_loop.py`.

Strengths:

- three-valued completion (`True`, `False`, unknown) avoids fabricated failure;
- repeat comparisons sort chronologically before selecting occasions;
- missing effort, quality, and external-check values remain absent;
- memory-loop checks can compare before/after personal and companion
  projections;
- correction rows are applied through existing correction helpers rather than
  invented evaluator state.

Adapter requirements:

- add recommendation-exposure and treatment metadata;
- preserve companion/relationship and occasion scope in the observation;
- distinguish inferred occurrence from promoted preference candidate;
- add counterevidence, validity intervals, and roster changes;
- define distal and negative outcome windows before causal use.

### Ambient relevance

Source: `travel-agent/eval/ambient/relevance_calibration.py`.

Strengths:

- structured verdicts require evidence refs for completeness measurement;
- unknown verdicts are not counted as true negatives;
- reports precision, recall, unknown rate, and evidence-complete rate;
- explicitly labels itself fixture-only and not live judge quality.

Adapter requirements:

- rename the surface-specific `should_fire` output into an
  `InterventionDecision` adapter;
- record eligibility exclusions and no-send probability;
- add surface/channel, cooldown, consent, and competing-intervention fields;
- define intermediate, distal, and negative windows;
- retain the original relevance metrics as one slice, not the complete causal
  score.

### Taste quality

Source: `travel-agent/eval/taste_quality/fixtures.py`, `checks.py`,
`rubric.py`, and `run_eval.py`.

Strengths:

- hard checks block invented candidates and weak provider matches;
- cold/mismatch cases require an honest empty result;
- a judge scores taste fit, floor discipline, grounding, and non-generic
  quality separately;
- mock mode is provider-free and CI-compatible.

Adapter requirements:

- attach DecisionState and allowed action labels;
- record why the candidate was admitted and which evidence was excluded;
- add audience/privacy cases and no-send rationale;
- route judge output through the HAU calibration set;
- do not use taste judge scores as an authorization or state gate.

## 5. Missing cross-cutting capabilities

### 5.1 No shared trial envelope

Current evaluators each define their own fixture and result shapes. A later
report cannot reliably join an action decision to evidence scope, final state,
receipt, or delayed outcome. AI-001 and AI-002 should provide adapters and
validators before new model comparisons.

### 5.2 No typed action policy

The current assets test effects and outcomes but do not make “ask,” “show,”
“recommend,” “propose,” “execute,” “abstain,” and “silent” mutually inspectable
policy outputs. AI-004 through AI-006 depend on A–D scope/freshness contracts.

### 5.3 No promotion ladder

The memory loop can verify correction projections, but there is no shared
ClaimCandidate contract with explicitness, recommendation exposure, subject,
companion/occasion scope, validity, counterevidence, and promotion tier.

### 5.4 No multi-principal memory benchmark

Existing memory checks are useful but do not systematically test authorization
before retrieval, false-premise correction, temporal supersession, active
forgetting, or wrong-roster applicability.

### 5.5 No group process benchmark

Group composition is a safety boundary, not a group-decision quality benchmark.
There is no current common corpus for welfare, minimum-member utility,
participation, steering, direct leakage, and inferential leakage.

### 5.6 No causal intervention record

Relevance and experience-loop metrics are observational/fixture-level. They do
not provide treatment probabilities, no-send, delayed outcomes, negative
outcomes, or censoring needed for a causal proactivity study.

### 5.7 No calibrated evaluator registry

The taste judge is structured and useful, but there is no frozen cross-family
human anchor set, judge drift record, or model/prompt/rubric promotion registry.

## 6. AI-R0 backlog, ordered

| Order | Work item | Evidence | Owner boundary |
| ---: | --- | --- | --- |
| 1 | freeze shared case envelope from fixture manifest | S | workspace docs |
| 2 | write adapters for product-proof hard fields | S/M | future isolated backend eval lane |
| 3 | map experience-loop observations to outcome/claim fields | S/M | future isolated backend eval lane |
| 4 | define scope/privacy fixtures for MB and GDL | S/M | workspace corpus assets |
| 5 | define intervention ledger no-send fixtures | S/M | workspace corpus assets |
| 6 | define TIS attack goals and final-state assertions | S/M | workspace corpus assets |
| 7 | freeze HAU rubric and adjudication protocol | H | product/research review |
| 8 | record A–D dependency and integration SHA handoff | S | convergence integration owner |

No item above authorizes runtime model behavior.

## 7. AI-R1 entry criteria

The baseline inventory is ready for implementation handoff when:

- the fixture manifest is committed;
- the existing asset mapping has an owner for every adapter;
- A–D integration revisions and deferred contracts are recorded;
- backend `.venv` is available for offline evaluation;
- no untracked generated result is mistaken for an immutable receipt;
- the first HAU reviewers are named;
- the isolated AI-DL backend worktree is created from the recorded base.

The next code commit should add only the shared evaluation envelope and
deterministic validators in that isolated worktree. It should not add a live
policy, a memory writer, a notification treatment, or a group message path.

## 8. Evidence statement

As of this inventory:

> Existing offline evaluation assets are real and reusable. The AI-DL shared
> evaluation spine, decision policy, governed memory promotion, causal
> proactivity ledger, group decision lab, injection suite, and calibrated human
> anchor set are not yet implemented.

This statement is supported by S/M fixture inspection and local offline runs;
it makes no B, D, V, or C claim.
