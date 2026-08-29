---
doc_type: working
status: active
owner: founder / product / architecture / backend / mobile
created: 2026-08-29
expires: 2026-09-28
why_new: Translates the accepted Contribution and Consequence Contract into a code-grounded, architecture-spanning migration plan for Chat, Intake, memory, synthesis, behavioral inference, receipts, correction, and mobile contribution surfaces without prematurely committing to a database migration.
promotes_to: null
supersedes: []
---

# Contribution Contract and Legacy Memory Migration Plan

## Outcome

Make every Vesper input obey one shared rule:

> Return useful value first, then apply only the smallest consequence the
> person's gesture and current authority actually warrant.

This plan implements the accepted [Contribution and Consequence
Contract](../systems/contribution-and-consequence.md). It is not a feature-loop
prototype and does not authorize a repository-wide noun rewrite. It is an
architecture-spanning migration across the places where one human contribution
currently becomes context, memory, social state, action, projection, or repair.

## 1. What the repository already gives us

The migration should reuse rather than replace these seams:

| Existing seam | Reusable capability | Missing contract |
| --- | --- | --- |
| `backend/core/models/admission.py` | Retry-stable actor, audience, source, immediate job, retention request, and readback | Inference, action, gesture, authority tier, canonical owner, and policy reason |
| `backend/inbound/semantic_contract.py` | Source-bound candidates, truth modes, and the rule that a candidate cannot self-grant authority | One policy shared with ordinary Chat and direct UI contribution |
| `backend/core/control_plane.py` | System-issued `AuthorityEvidence`; the model cannot mint its own action authority | Contribution authority before memory and projection writes |
| `backend/concierge/tool_contracts.py` | Effect, confirmation, context, retry, and parameter checks for consequential tools | `observe()` is absent; retention and inference are not first-class axes |
| observation rows and `create_observation()` | Source mode, provenance, scope, confidence, visibility, supersession, and expiry | Proof that the source was admitted for this exact claim and consequence |
| pending Chat turns | `answer_only`, custody, idempotency, binding, release, and reconciliation | The same contribution decision used after the turn is sent |
| Intake v2 | Source custody, admission, review, consequence recipes, and lineage | Common gesture and T0/T1/T2 evaluation with Chat |
| action and Vesper receipts | Structured outcomes, sources, reversibility, and compact UI primitives | One causal receipt that names the canonical owner and dependent projections |
| correction caches and APIs | Immediate frontend correction affordances and backend repair paths | Cross-owner invalidation proof rather than surface-local patching |

No initial database migration is needed to learn whether this policy can be
enforced. Existing fields can carry the first conformance slice. A schema
change becomes justified only when the mapping table in section 4 proves that
a required invariant cannot be represented honestly.

## 2. Current non-conforming paths

### 2.1 Prompt-directed memory writes

- `backend/concierge/_prompts_skills.py` tells the model to call `observe()` for
  anything worth remembering, personality insight, mood, emotional investment,
  booking preferences, and repeated silence.
- `backend/concierge/_prompts_templates.py` has flows where `observe()` is the
  mandatory first or only tool.
- `backend/concierge/agent.py::_check_booking_observe_gap` treats a booking
  without a memory write as an instrumentation failure.
- `backend/core/agent_loop.py` and `backend/core/telemetry.py` still encode the
  assumption that `observe()` is bookkeeping alongside useful work.

This is the largest blocker. The reasoning model currently decides retention
and interpretation by deciding to call a tool. Under the accepted contract,
the model may propose a candidate, but only a system-owned policy decision may
authorize the write.

### 2.2 Interpretation promoted to personal truth

- `backend/concierge/refresh_memory.py` synthesizes identity-led “Who they are,”
  taste dimensions, social style, energy, and “DNA” language.
- `backend/concierge/reflection.py` can produce observations through the same
  memory dispatcher.
- `backend/preference_engine/synthesis/group_synthesizer.py` derives group
  profiles from Personal Memory narratives.
- `backend/preference_engine/retrieval/preference_retriever.py` encourages
  inference from phrasing, energy, pace, and group dynamics in sparse cases.

These can remain derived projections only after their inputs are restricted to
admitted evidence and their output stops presenting conjecture as identity.

### 2.3 Behavioral exhaust converted into preference

- `backend/core/personalization/discover_synthesizer.py` creates inferred
  observations from Discover signals.
- `backend/preference_engine/edit_inference.py` converts itinerary replacements
  into durable preference observations.
- `backend/core/memory_signal.py` converts save, share, and regenerate events
  into claims that a trip “resonated.”
- related vote, reply, read, silence, and dwell producers must be audited even
  where they do not currently write observations.

Operational events may tune the current session or Occasion. They cannot become
longitudinal taste or identity merely because they are deliberate UI events.

### 2.4 Receipt and correction asymmetry

Share capture already offers Keep, Correct, and Delete, and pending Chat can be
answer-only. But the underlying policy is not shared, receipts do not always
name the exact owner changed, and a correction is not yet certified to
invalidate every dependent Home, Places, group, and Personal Memory projection.

## 3. Target runtime shape

```text
authenticated event + current scope + prior mandate
                       ↓
              contribution resolver
                       ↓
 gesture + Use / Retention / Inference / Audience / Action
 authority tier + reasons + canonical owner + reversibility
                       ↓
             immediate-value job runs
                       ↓
       T0 stop │ T1 private apply │ T2 exact preview
                       ↓
       owner mutation + causal receipt + projection invalidation
```

The contribution resolver is deterministic policy around model-assisted
semantic candidates. The model may help classify an utterance or propose an
interpretation. It must never decide that its own interpretation is authorized.

### 3.1 Proposed storage-neutral models

Add `backend/core/models/contribution.py` with frozen, provider-neutral types:

- `ContributionGesture`: Ask, Point, Bring, Keep, Share, Decide, Correct;
- `ContributionAxes`: use, retention, inference, audience, action;
- `ContributionAuthorityTier`: T0, T1, T2;
- `ContributionScope`: actor, conversation, Trip, Occasion, source, audience;
- `ContributionCandidate`: model- or adapter-proposed literal claim,
  interpretation, destination, and consequence;
- `ContributionDecision`: system-owned allowed axes, tier, reasons, owner,
  expiry, required preview, and correction path; and
- `ContributionReceipt`: source refs, admitted claims, owner mutation refs,
  invalidated projections, audience effects, and Undo/Correct capability.

The first implementation should serialize the decision into existing
provenance and receipt metadata. Do not add a table until queries, retention,
or repair require an independently addressable contribution record.

### 3.2 Resolver precedence

Implement a pure resolver in `backend/core/contribution_policy.py` using this
precedence:

1. current explicit instruction;
2. narrow standing mandate or setting;
3. current channel, Plan, or Occasion authority;
4. gesture default;
5. conservative fallback.

It must return T0 for ordinary questions, T1 only for clear private
source-bound Point/Bring contributions, and T2 for audience changes, affected
people, providers, spend, public state, sensitive inference, or weakly
reversible actions. Ambiguity triggers a question only when the answer changes
truth or consequence.

## 4. Initial mapping onto existing fields

| Contract field | Existing representation for phase one |
| --- | --- |
| actor and scope | authenticated actor, conversation, `trip_id`, pending-turn binding |
| source | `SourceRef`, source message id, Intake item id, provenance |
| Use | immediate job plus transient turn context |
| Retention | `AdmissionRetention`; presence or absence of owner mutation |
| Inference | literal claim vs derived candidate in provenance and truth mode |
| Audience | Admission audience, conversation type, `shared`, owner policy |
| Action | control-plane effect, confirmation policy, `AuthorityEvidence` |
| authority tier | contribution decision metadata; T2 binds system-issued authority evidence |
| owner | resource reference in receipt and existing canonical object id |
| correction | supersession/retirement plus receipt continuation |
| expiry | observation expiry or pending custody expiry |

This mapping is intentionally lossless enough to enforce policy but not yet
optimized for analytics. If a field cannot be reconstructed for a receipt or
repair test, promote it to a durable column or contribution table in a separate
reviewed migration.

## 5. Architecture-spanning implementation sequence

Each increment crosses the necessary backend and client seams. None is framed
as proving one isolated behavior loop.

### Increment A — executable policy and fixture portfolio

1. Add the storage-neutral models and pure resolver.
2. Encode the ten cases from the [fixture
   pack](contribution-contract-fixture-pack-2026-08-29.md) as table-driven unit
   tests: practical Ask, Point, journey artifact, food evidence, cultural
   evidence, operational change, social juxtaposition, Occasion contribution,
   correction, and temporary no-write continuity.
3. Add adversarial variants for ambiguous audience, proxy claims about another
   person, silence, dwell, repeated browse behavior, public sharing, spending,
   and correction after projection.
4. Require every decision to explain its precedence and denial reason.

Primary files:

- `backend/core/models/contribution.py`
- `backend/core/contribution_policy.py`
- `tests/core/test_contribution_policy.py`
- `tests/scenarios/test_contribution_contract_portfolio.py`

Exit gate: the same input and scope always produce the same authority decision;
no model output can increase its own authority tier.

### Increment B — Chat and Intake share admission

1. Extend or adapt `AdmissionEnvelope` into a contribution candidate; do not
   make it a competing policy vocabulary.
2. Resolve the decision before the admitted content reaches durable memory or
   an action tool.
3. Preserve `answer_only` through pending-turn send, not just staging.
4. Make Intake consequence recipes consume the same decision object.
5. Keep source bytes in their current custody owner; the decision carries only
   identifiers and policy.

Primary files:

- `backend/core/models/admission.py`
- `backend/api/routes/pending_chat_turns.py`
- `backend/core/models/pending_chat_turns.py`
- `backend/inbound/semantic_contract.py`
- `backend/inbound/consequence_recipes.py`
- `tests/core/test_pending_chat_turns.py`
- `tests/inbound/test_intake_v2_retention.py`
- `tests/inbound/test_consequence_recipes.py`

Exit gate: an equivalent Ask, Point, or Bring gets the same retention,
inference, audience, and action outcome through Chat and Intake.

### Increment C — put `observe()` behind authority

1. Register `observe` as a durable tool contract and require a system-issued
   `ContributionDecision` reference or equivalent authority evidence.
2. Treat the model's `observe()` payload as a candidate, never authorization.
3. Reject writes that lack admitted source, actor, scope, and allowed inference.
4. Remove mandatory-observe language from `_prompts_skills.py` and
   `_prompts_templates.py` only after the gate exists.
5. Retire `_check_booking_observe_gap`; replace it with policy telemetry:
   unauthorized write blocked, explicit contribution missed, and no-write
   correctly preserved.
6. Remove agent-loop and telemetry comments/tests that equate memory with
   bookkeeping.

Primary files:

- `backend/concierge/memory_tools.py`
- `backend/concierge/tool_contracts.py`
- `backend/concierge/agent.py`
- `backend/concierge/_prompts_skills.py`
- `backend/concierge/_prompts_templates.py`
- `backend/core/agent_loop.py`
- `backend/core/telemetry.py`
- `tests/concierge/test_memory_workflow.py`
- `tests/concierge/test_agent_audit_pass.py`
- `tests/concierge/test_prompt_golden.py`

Exit gate: ordinary questions and booking execution cannot cause observation
writes; an explicit authorized preference can, with source and scope intact.

### Increment D — make Personal Memory a derived projection

1. Restrict reflection input to admitted evidence, corrections, and owned
   Outcomes.
2. Prevent reflection from writing a newly inferred personal claim without a
   separate policy decision.
3. Replace identity/DNA synthesis with bounded, evidence-labeled current
   preferences, constraints, open uncertainty, and scopes.
4. Make correction supersession effective before any asynchronous synthesis.
5. Prevent group synthesis from receiving private narrative or turning
   individual evidence into interpersonal identity.
6. Preserve current useful retrieval while labeling source, scope, freshness,
   and disagreement.

Primary files:

- `backend/concierge/reflection.py`
- `backend/concierge/refresh_memory.py`
- `backend/concierge/memory_workflow.py`
- `backend/preference_engine/retrieval/preference_retriever.py`
- `backend/preference_engine/synthesis/group_synthesizer.py`
- `tests/eval/test_memory_loop.py`
- `tests/concierge/test_post_trip_memory_refresh.py`
- `tests/preferences/test_group_profile_freshness.py`

Exit gate: deleting or correcting a source changes downstream behavior
immediately; narrative projection lag cannot resurrect or continue serving the
old claim.

### Increment E — quarantine behavioral inference

For each producer, choose exactly one treatment:

1. current-session ranking input;
2. current-Occasion coordination state with expiry;
3. aggregate product telemetry; or
4. explicit contribution candidate requiring user authorship.

Then:

- stop Discover synthesis from writing personal observations;
- keep itinerary replacements as operational Outcomes and recommendation
  feedback, not inferred taste;
- record save/share/regenerate as object actions, not proof that an experience
  “resonated”; and
- certify that silence, dwell, response timing, and ignored content do not enter
  Personal Memory.

Primary files:

- `backend/core/personalization/discover_synthesizer.py`
- `backend/preference_engine/edit_inference.py`
- `backend/core/memory_signal.py`
- related notification, vote, reaction, and analytics producers found by the
  inventory test
- `tests/preferences/test_edit_inference.py`
- `tests/preferences/test_signal_pipeline.py`
- new `tests/core/test_behavioral_signal_boundaries.py`

Exit gate: each behavioral event has a named owner, scope, expiry, and allowed
consumer; none becomes durable personal truth by default.

### Increment F — causal receipts and repair across projections

1. Compose one compact receipt from the contribution decision and actual owner
   mutation, not from model prose.
2. Name what was used, kept, shared, changed, or deliberately not retained.
3. Attach Correct/Undo to the canonical owner.
4. On correction, supersede or retire the owning claim and invalidate Home,
   Places, Personal Memory, group, and generated-content projections that cite
   it.
5. Preserve historical receipts as audit truth without continuing to serve the
   invalidated claim.

Primary files:

- existing action-receipt and Vesper-receipt models/composers
- canonical owner mutation services
- projection caches and invalidation subscribers
- correction routes and scenario tests
- `tests/scenarios/test_j27_memory_provenance_correction.py`
- `tests/concierge/test_settlement_receipts.py`

Exit gate: the causal repair test passes from source correction through every
dependent surface, with no stale personalized output.

### Increment G — value-first mobile contribution UX

1. Chat remains the cleanest contribution surface: input first, immediate
   useful response, compact consequence receipt only when state changed.
2. Refactor share capture away from leading with “Vesper found one thing to
   keep.” Lead with the useful interpretation or action; make retention a quiet
   consequence when T1 applies and an exact preview when T2 applies.
3. Reuse `ChatReceiptDisclosure` and `VesperReceipt`, but display only the axes
   that changed; never make every turn a permission form.
4. Route Correct/Undo to the canonical owner and refresh Home, Places, and Life
   from the same repair result.

Primary files:

- `travel-app/app/share-capture/index.tsx`
- `travel-app/components/chat/ChatReceiptDisclosure.tsx`
- `travel-app/components/receipts/VesperReceipt.tsx`
- correction caches, generated API types, and affected tests

Exit gate: T0 produces value and no receipt clutter; T1 produces value plus a
quiet reversible receipt; T2 shows the exact material consequence before it
crosses the boundary.

## 6. Conformance portfolio

Certification is portfolio-wide, not “one loop first.” At minimum, CI should
cover these connected invariants:

| Invariant | Required cases |
| --- | --- |
| no-write Ask | personal, group, source attachment, follow-up using existing context |
| private source-bound apply | Point and Bring with literal claim, expiry, correction, and Undo |
| material preview | share, invite, provider action, spend, public state, proxy claim |
| authority symmetry | same gesture through Chat, Intake, direct UI, and Occasion |
| owner integrity | Trip, Plan, Place relation, Occasion, artifact, preference, constraint |
| causal repair | correction before and after Home/Places/group/Personal Memory projection |
| multiplayer boundary | attributed contribution, private constraint, group-visible source, organizer mandate |
| no behavioral identity | silence, dwell, read, save, replace, regenerate, repeated browsing |
| value-first response | useful answer precedes optional consequence; no trailing homework by default |

## 7. Solo-founder sequence

The highest-leverage order is:

1. executable policy and fixtures;
2. Chat/Intake admission parity;
3. hard runtime gate in front of `observe()`;
4. prompt cleanup and legacy telemetry retirement;
5. synthesis and behavioral-producer quarantine;
6. causal receipts and repair;
7. mobile value-first presentation; and
8. cross-surface certification.

This order establishes authority before polishing copy and prevents new Home,
Places, Life, Occasion, or dynamic-interface work from compounding hidden
memory semantics. It still works across the product architecture: each
increment protects all future surfaces rather than tunnel-visioning on a
single behavioral demo.

## 8. Explicit non-goals and deferred decisions

- Do not benchmark current ChatGPT or current Vesper as the product judge.
- Do not rewrite all product nouns or repositories before the policy exists.
- Do not add an Occasion-specific profile.
- Do not make every private contribution review-first.
- Do not interpret quiet receipts as authority; hidden friction is still
  unauthorized if the underlying consequence is material.
- Do not delete legacy observations in this migration. Quarantine their use,
  label uncertain provenance, and design a separate reversible cleanup pass.
- Do not choose a permanent contribution table until repair and query needs
  prove the existing provenance mapping insufficient.

## 9. Definition of done

The legacy memory migration is complete only when:

1. every input path resolves the five axes under one policy;
2. immediate value is independent from durable retention;
3. no reasoning-model tool choice can self-authorize memory or action;
4. Personal Memory is a revisable projection over admitted evidence;
5. multiplayer contribution preserves actor, subject, audience, and mandate;
6. corrections reach the canonical owner and invalidate all dependents;
7. receipts disclose the actual consequence without turning Home or Chat into
   homework; and
8. the full conformance portfolio passes across backend and mobile contracts.
