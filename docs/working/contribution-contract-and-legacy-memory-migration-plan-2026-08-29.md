---
doc_type: working
status: active
owner: founder / product / architecture / backend / mobile
created: 2026-08-29
last_verified: 2026-09-05
expires: 2026-09-28
why_new: Translates the accepted Contribution and Consequence Contract into a code-grounded, architecture-spanning migration plan for Chat, Intake, memory, synthesis, behavioral inference, receipts, correction, and mobile contribution surfaces without prematurely committing to a database migration.
promotes_to: null
supersedes: []
---

# Contribution Contract and Legacy Memory Migration Plan

> **Current execution plan — September 5:** [§11](#11-completion-plan--september-5)
> records the fresh baseline, remaining repairs, product sequences, owner
> dependencies, and next commit order. It supersedes earlier suggestions that
> only native/P5 verification remains. [§10](#10-contribution-and-capture-execution-plan--september-4)
> remains the full P0–P5 scope and acceptance framework. Sections 1–9 preserve the
> August 29 architectural rationale and migration inventory; their descriptions
> of current code are historical, not fresh findings. In particular, the pure
> policy/models now exist, some unsafe prompts and privacy paths have been
> corrected, and mobile experience design must run alongside—not after—the
> backend migration. The accepted system contract remains authoritative; this
> working plan does not itself adopt new product decisions or authorize rollout.

### Execution receipt — September 4, continued

The first implementation pass has now crossed the main backend/mobile seams.
These are repository commits, not a claim of production rollout:

| Area | Delivered | Commit(s) |
| --- | --- | --- |
| Explicit retention authority | `observe()` is an explicit, source-bound retention action; ordinary questions and booking execution no longer require bookkeeping writes. | `eea52e068` |
| Authored attention | User-authored notes travel into interpretation as attributed context, never as source evidence. | `423e8beb0` |
| Source-first Life addressability | A retained original gets a source-only Life door before interpretation is confirmed; no semantic claim is fabricated. | `79b00f294` |
| Admission parity | A shared core adapter resolves Admission → Contribution for pending Chat and the explicit Intake attachment path; durable requests fail closed until T1 custody/authority exists. | `124f8b40f` |
| Canonical Chat receipt | The resolved policy decision travels with the canonical pending-turn metadata for downstream receipt/audit, without becoming model-minted authority. | `2e3664e26` |
| Access to immediate Chat value | Unresolved shares can continue into contextual Chat with source refs and `answer_only` retention. The primary share-screen composition still leads with candidate review; this commit does not complete value-first capture. | `09b80dbaa` |
| Media/recovery truthfulness | Mobile preserves server-side HEIC/scanner capability errors instead of collapsing them into generic retry copy; local retry and custody resumability remain covered by tests. | `cdf048617` |

PDF, Apple Wallet, and HEIC/HEIF remain deliberately unsupported at the
intake boundary: the backend security contract rejects them until a document
scanner/conversion path is actually available. The mobile layer must mirror
that boundary, not advertise a normalizer class as a supported product
capability.

The P5 work includes operational evidence, alongside the unfinished P1–P4
work now specified in §11:
controlled native/share-extension runs, interrupted-finalize and relaunch
receipts, mixed-success batch evidence, and a separately reviewed readiness
decision for each new document family. No connector, ambient ingestion, or
legacy-writer retirement is implied by these commits.

The mobile cold-start handoff now has an explicit regression guard: the app
replays the `guide://dataUrl=…` marker after `expo-share-intent` reports that
its native listener is ready. This closes the observed race in which the native
extension had received a share but the first JS refresh happened before the
`onChange` listener existed, leaving the app on Home. The guard is covered by
`ShareIntentHandler.test.tsx`; it does not broaden supported payload types or
pretend that a source was admitted.

### Native evidence checkpoint — September 4

The local iOS native target was rebuilt against the current app-config
contract with Sentry source-map upload disabled (the local environment has no
Sentry organization configured):

- `xcodebuild -workspace ios/TravelApp.xcworkspace -scheme TravelApp -configuration Debug -destination 'platform=iOS Simulator,id=AF31B886-E837-4962-834A-5CBAD5C306DB' CODE_SIGNING_ALLOWED=NO build` → `BUILD SUCCEEDED` when run with `SENTRY_DISABLE_AUTO_UPLOAD=true`;
- the build included `ShareExtension.appex`, and the generated activation rule
  accepted the configured 16-image/16-file capacity;
- the app installed and launched on the booted simulator and accepted a
  `guide://dataUrl=…` marker without an unmatched-route crash.
- the Android Gradle path reached Expo configuration but could not compile in
  this machine because no Android SDK is installed (`ANDROID_HOME`/
  `android/local.properties` is absent); no Android native result is claimed.

This is native compilation and intent-boundary evidence, not proof of a full
payload round trip. A controlled iOS Safari run did launch the native share
extension and emit the `HandleUrl guide://dataUrl=…` marker in both Debug and
Release builds; the pre-fix run exposed the cold-start race by returning to
Home. The Release build now contains the listener-ready replay and the
regression test passes, but a clean OS share-sheet run that visibly reaches
`/share-capture` is still required, followed by server readback and
relaunch/interrupted-finalize evidence for text, image, audio, and multi-file
payloads. The committed source of truth for the native extension is
`app.json`/`app.config.js`; generated `ios/` output is ignored and must not be
treated as a separately landed contract.

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

The sequence below is the August 29 baseline. Use §10.8 for execution now;
do not postpone contribution experience design until all memory work is done.

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

## 10. Contribution and capture execution plan — September 4

### 10.1 Outcome, scope, and evidence limits

Build the experience of giving something to Vesper, not another upload feature:

> Give Vesper a question, observation, photo, ticket, link, or thought. Receive
> something useful immediately. Where warranted, it becomes accessible material
> and informs the next useful consequence without filing or classification work.

This is system construction across a representative portfolio, not a single
behavior-loop experiment. It spans entry, interpretation, authorized retention,
owner handoff, correction, and recovery. It does not redesign the four roots.

The September 4 investigation read current backend/mobile code, the accepted
contribution contract, the prior admission receipt and lifecycle audit, and the
recent Chat handoff. Focused offline checks passed: 36 backend tests, 7
deselected; 31 mobile tests across six suites. These are not live model-quality,
database-migration, provider, native, or deployed acceptance evidence. The named
`Downloads/vesper-chat` export was unavailable; do not claim a fresh visual review.

Baseline evidence to recheck before implementation (paths are relative to the
workspace unless prefixed below by `backend/`, meaning `travel-agent/backend/`):

| Area | Current evidence | Consequence for this plan |
| --- | --- | --- |
| Pure policy | `backend/core/models/contribution.py`, `backend/core/contribution_policy.py` exist; Concierge façade is `off`/`shadow` only | Reuse and complete the resolver; do not recreate it or confuse shadow output with enforcement |
| Ordinary Chat | `backend/concierge/session.py` persists images through `core/db/chat_images.py`; cleanup/expiry is deferred; `memory_tools.py` has actor guards but no complete contribution gate | Carry decisions through ordinary sends, source derivatives, tools, and spawned jobs |
| Admitted-source Chat | `api/routes/pending_chat_turns.py` stamps admission metadata, materializes sources, and invokes ordinary send | Pending-row expiry does not prove end-to-end Ask source expiry; branch existence is not accessible consumer completion |
| Intake utility | `travel-app/app/share-capture/index.tsx` leads with processing and Keep/Correct candidates | Replace the primary result composition, not merely its wording |
| Authored attention | `user_note` is stored; `workers/intake_semantic_jobs.py` does not supply it to `inbound/semantic_interpreter.py` | Preserve the person's words as a distinct attributed input to the immediate job and relevant interpretation |
| Stable retention | General `inbound/anchor_runtime.py` requires confirmed candidates; `core/db/intake_source_attachments.py` already reads explicit entity-photo attachments independently | Separate source addressability from endorsing interpretation; retain the narrow existing authority checks |
| Media | `travel-app/components/chat/composerAddCapabilities.ts` exposes camera/library; `data/inboundItems.ts` rejects PDF, PKPass, HEIC/HEIF | Add truthful format coverage through the common path; do not advertise unsupported inputs |
| Multiplayer | Legacy trip photos have private/group/group-and-learn states; canonical artifact Together reads reject absent graph sharing authority | Reuse existing owners, but do not equate a visibility enum with the complete shared contribution contract |
| Production | Historical Intake production baseline is dated August 23 | Obtain fresh deployment evidence later; neither repeat an old blocker as current fact nor presume readiness |

The [prior lifecycle audit](life-contribution-lifecycle-code-audit-2026-09-01.md)
is a writer-discovery seed, not a current bug count. Reconcile its applied-fix
appendices and current commits before creating implementation tickets.

### 10.2 Product decisions to settle through the design portfolio

These are recommended resolutions. Record founder acceptance or amendments in
the appropriate canon before relying on a changed promise in implementation.

| Decision | Recommendation | Why / boundary |
| --- | --- | --- |
| Entry | Chat is the primary expressive entry; OS share and contextual Bring remain first-class | No Capture tab, duplicate inbox, or mandatory detour into a conversation |
| First value | Complete the current job before presenting administration | Extraction, a direct answer, or reliable preservation may suffice; every source need not generate an essay |
| Ask vs Bring | Resolve from wording, invoked affordance, and context; preserve existing conservative defaults | Do not expose internal gesture labels as a questionnaire or treat every attachment as a save |
| Chat history | Distinguish visible conversation history from original-file retention and future personal learning | Specify history/source-derived-summary retention explicitly; no silent exemption from the accepted Ask-source lifecycle |
| Retained source | Make it addressable independently of a confirmed semantic candidate | Keeping a ticket is not confirming attendance or approving every extracted field |
| Receipt | Value first; compact actual scope/destination when useful; details on demand | A safe storage acknowledgment is not editorial value, but remains sufficient when storage itself was the job |
| Context | Inherit the exact visible object as a reference, not authority | Being on an Occasion page is not enough to publish a private derivative or edit arrangements |
| Correction | Correct the relation or claim in question; distinguish delete, detach, release, and undo | Do not make users delete an original to remove a wrong interpretation |
| Leaving | User can leave after acknowledgment; processing continues under existing authority | No surprise push for routine completion, no review debt, no promise that an unuploaded local file is safe |
| Shared contribution | Preserve contributor, source author where known, audience, and affected-person boundaries | A friend's forwarded note must not become the recipient's authored experience |

Two decisions are load-bearing before broad release: the ordinary-history
retention promise and the source-only destination contract with Life. Design
exploration, writer inventory, pure-policy tests, and source-context adapters
can proceed while those are being settled.

### 10.3 Design package D0 — six complete consumer sequences

Extend [Chat work package A](claude-design-integration-2026-09-04/04-chat.md),
not the whole Chat root. Keep detailed visual composition in the dedicated
design tool. Phone-scale sequences must show real contents, not only boxes,
generic status labels, or idealized happy-path captions.

| ID | Contribution | First useful result | Retention / consequence | Re-entry and repair |
| --- | --- | --- | --- | --- |
| C1 | Ticket + “What time should I arrive?” | Answer from the actual ticket; explain a material ambiguity only if necessary | Ask by default; no attendance, tracking, or learning by implication | Reopen the answer under declared history policy; supporting source expires under its own policy |
| C2 | Same ticket deliberately sent alone | Useful readable details; any supported practical issue | Private Bring where permitted; no booking execution or assumed attendance | Find the original without confirming a speculative interpretation |
| C3 | Photo + “Look how the buildings sit on these cliffs” | Respond to the directed observation; add substance where supported | Preserve authored attention separately from source extraction and model interpretation | Correct the place or interpretation without erasing the photo or the person's words |
| C4 | “Keep jazz in mind for Saturday” | Acknowledge the specific retained intention, not a generic “got it” | Smallest appropriate intention owner; no compulsory Plan or naming wizard | Find/change the intention; Home may later use it within scope |
| C5 | Photo or note contributed to an existing Occasion | Show the useful authored contribution in its actual shared context | Current audience, attribution, and applicable grant; no automatic personal learning or arrangement edit | Inspect contribution and withdraw the permitted projection without claiming to erase others' private originals |
| C6 | “That ticket was cancelled; I never went” | Correct the specific misconception and show actual accepted change | Retain ticket if desired; revoke unsupported occurrence and dependent uses | Check changed journey/content/current state; preserve independently supported later events |

Overlay the following variants across these six sequences, rather than adding
six new screens: cold start, denied photo access, no network, duplicate retry,
leave/relaunch, partial multi-file processing, unsupported format, source
deleted mid-processing, unavailable destination, and account/audience change.

D0 deliverables:

1. Six entry → value → consequence → leave → return → correction sequences.
2. One shared result/receipt interaction vocabulary with density variants.
3. An explicit contract for when a source goes to Chat versus finishes inline.
4. A reuse/delta list against composer, source preview, receipt, owner reader,
   and correction controls already implemented.
5. A decision log resolving §10.2; label all simulated facts and model responses.

D0 acceptance: the person can understand the returned value, whether anything
was retained/shared/changed, and how to return or correct it without learning
the internal ontology. Ignoring optional continuation creates no unfinished task.

### 10.4 Runtime architecture and integration agreement

Use one policy vocabulary over existing owners, not one universal persistence
service and not separate policies for each input medium.

```text
authenticated gesture + authored words + source refs + entry context
  -> common contribution decision (incremental, server-owned)
  -> permitted source processing + immediate useful response
  -> stop | bounded private retention/update | exact material boundary
  -> existing canonical owner accepts / rejects
  -> versioned readback + quiet receipt + correction destination
  -> eligible Life / Home / Places / Occasion projections
```

Technical upload/retry custody may precede the response. “Value first” means
no classification/filing work before value and no successful-effect claim before
owner readback; it does not require keeping unverified bytes outside safe custody
until a sentence has streamed. Source processing, lasting retention, and future
influence remain separate decisions.

The shared handoff must carry, or resolve authoritatively:

- stable contribution/turn identity and existing source identifiers;
- original human words, source author when known, and authenticated contributor;
- requested immediate job and exact originating object/context;
- resolved use, retention, inference, audience, action, expiry, and basis;
- source/claim/projection identity and revision, without treating one as another;
- canonical destination, processing/readback state, and available repair actions;
- causal dependencies required to invalidate derived use after correction.

Use current admission/provenance/receipt structures where lossless. Extend a
schema when durable lookup, lifecycle enforcement, or repair genuinely requires
it; do not force independent source identity into a fabricated confirmed claim.
Produce a field-to-owner mapping before a migration. No blanket universal
contribution table, no parallel copy of source bytes, and no model-issued grant.

Policy resolution occurs before each effect. Revalidate current owner/audience
authority and source eligibility at execution and asynchronous completion, not
only against a snapshot stored when the job was queued. A model can propose a
gesture; authenticated language/affordance evidence and deterministic policy
must establish what it can actually authorize. Preserve explicit authored
preferences and constraints rather than fixing hidden memory by disabling all
useful continuity.

### 10.5 Engineering work packages

#### P0 — baseline, writer coverage, and decision adapters

**Depends on:** nothing beyond this plan and current canon. Run alongside D0.

- Refresh the prior writer inventory for ordinary/pending Chat, Intake, direct
  entity capture, group contribution, voice, reflection, and background writers.
- For each reachable writer record: entry, trigger, owner, current gate, source
  lineage, retention, downstream consumers, and proposed retain/restrict/retire
  disposition. Include images, vision summaries, location samples, telemetry,
  indexing, synthesis, and replay—not only `observe()`.
- Reconcile AdmissionRetention with the three-layer contribution policy; name
  lossy mappings. Classify an equivalent user act consistently across entries,
  while preserving meaningful differences between a question and invoked Bring.
- Extend pure policy fixtures for C1–C6 and adversarial variants. Add positive
  cases for explicit preferences/constraints as well as no-write denials.
- Agree the source-only handoff fields with Life and contextual identity with
  entity/Plan owners. Identify existing modules to reuse or adapt.

**Exit:** reviewed writer/mapping ledger; every identified effect has a target
policy treatment and test owner; no assertion that shadow policy is enforcement.

#### P1 — effective policy, source lifecycle, and write containment

**Depends on:** P0; agreed history semantics before promising user-visible Ask
retention. Implement as several bounded commits, not one enormous migration.

- Resolve a server-owned decision on ordinary and pending-turn admission; keep
  it through source materialization, retries, tools, and background execution.
- Gate observations, facts, notes, contextual state, and other reachable writes
  according to the ledger. Adapt existing action authority rather than replacing
  it. Prevent missing metadata or legacy fallback from increasing permissions.
- Apply retention separately to raw files, source-derived summaries, claims,
  and projection caches; ensure expiry/deletion reaches copied representations.
- Converge new Chat source handling onto the appropriate existing custody owner;
  do not leave a permanent local-byte copy outside its lifecycle. Preserve legacy
  reads during a bounded migration; no indiscriminate deletion or dual writing.
- Restrict reflection/synthesis and behavioral producers to eligible evidence.
  Hold uncertain legacy inputs out of new personal inferences without erasing
  authored history. Remove obsolete mandatory-observe prompts/telemetry in the
  same rollout that introduces effective replacement behavior.
- Recheck grants on delayed shared work; distinguish operational participation
  state from personality or preference inference.

**Exit:** C1 and context-follow-up variants cannot create prohibited personal
claims or outliving source copies; explicit authorized continuity still works;
background work cannot bypass the same boundary. A policy flag must not make
disabled new functionality fall back to known non-conforming writes.

#### P2 — authored attention and immediate utility

**Depends on:** P0 contract; integrates under P1 before general release. D0
provides response treatments; pure adapters can be built in parallel with P1.

- Thread authored text/notes alongside sources into the immediate job. Keep
  user assertions distinct from source observations and model interpretation.
- Preserve origin identity and the referent of “this”; clarify only when the
  ambiguity changes a consequential result.
- Connect existing response/interpretation machinery to source-backed utility.
  Do not turn the source-local semantic extractor into an unrestricted new agent.
- Distinguish source receipt, usable partial result, interpretation completion,
  and owner acceptance. Return independent useful facts while a sibling source
  is pending, but never publish a cross-source conclusion requiring that sibling.
- Avoid redundant extraction where an existing verified result suffices; retain
  separately justified immediate vision and background processing when needed.
- No mandatory trailing question; optional research/depth should not withhold
  the basic answer. Keep generated prose and summaries from becoming evidence.

**Exit:** changing C3's authored observation changes the relevant interpretation
and response; C1/C2 differ appropriately despite identical bytes; partial results
remain source-bound and cannot imply completion or invented context.

#### P3 — source-first addressability and adjacent-owner handoff

**Depends on:** P0 owner mapping, P1 retention decisions. Can build in parallel
with P2 once the stable source contract is agreed.

- Extend the existing source attachment/read pattern to justified non-entity
  contributions without widening its narrow authority by assumption.
- Ensure a retained original and authored note have a durable inspectable
  destination even when no interpretation is confirmed.
- Keep association, occurrence, personal meaning, and original custody distinct.
  Optional interpretation confirmation must not be a prerequisite to find a file.
- Send Life a source reference, revision, declared relation/time where supported,
  readback, media availability, and correction destination—not a second corpus.
- Hand loose intentions and shared contributions to their existing agreed
  owners. If an owner capability is unavailable, preserve permitted private
  material and report the unapplied effect; do not claim the Plan/Occasion changed.
- Provide Home/Places with eligible references and invalidations, not guaranteed
  feed placement or a demand to emit a card for every input.

**Exit:** C2/C3 have reliable source-only re-entry; C4 uses the agreed intention
owner; no guessed attendance or fake semantic confirmation is required. Life
can consume the adapter independently of settling its final visual organization.

#### P4 — value-first mobile flow, receipts, and causal repair

**Depends on:** D0, P1–P3 contracts. Build components against fixtures earlier;
integrated acceptance requires the real owner/readback paths.

- Replace review-first share composition with the accepted useful-result
  treatment. Support finishing inline or continuing into contextual Chat;
  do not merely redirect every share to an empty conversation.
- Reuse the composer, source preview, compact receipts, and canonical readers.
  Keep detailed processing/interpretation inspection secondary.
- Display only actual applied state. Correct/Undo must reach the owner, not
  dismiss the card; navigation back must not undo an accepted change.
- Connect source deletion, interpretation release, relation detachment, and
  shared withdrawal to their distinct existing authorities.
- Invalidate dependent use immediately at read/admission boundaries; background
  recomputation may lag but cannot serve the revoked claim. Preserve independent
  contributions and unrelated supported facts.
- Make pending/failure state local, recoverable, and audience-safe across
  account switches and navigation. Do not require a separate management inbox.

**Exit:** C1–C6 complete with correct origin return, inspectable destination, and
repair. Native evidence covers value hierarchy, partial/error states, keyboard,
accessibility, long content, and small-screen behavior—not just test fixtures.

#### P5 — media coverage, recovery, and rollout

**Depends on:** common contracts. Format adapters can be developed earlier;
advertising/adopting them requires P1–P4 acceptance.

- Prioritize PDF and reliable phone-image decoding/conversion; document scanner,
  parser limits, malformed/encrypted documents, extraction quality, page/size
  budgets, and unsupported responses. Never bypass the existing safety rejection
  merely because a normalizer class exists.
- Add document selection through the same composer/source contract. Validate
  actual formats across OS share, direct selection, and server byte detection;
  MIME aliases and audio acceptance must agree end to end.
- Reconcile live voice, dictation where actually implemented, and imported audio
  as distinct entrances with one contribution behavior. Feature flags alone are
  not evidence of working dictation. Preserve transcript lineage and scope.
- Complete upload identity, local-file lifetime, relaunch reconciliation,
  interrupted finalize, duplicate send, and mixed-success batch recovery. Define
  what is safely on the server versus still pending on the device.
- Verify forwarded email with an explicitly authorized controlled delivery,
  deployed schema, worker cadence, object access, and correction/release receipt.
- Keep Wallet passes and broader connectors behind separate readiness decisions;
  no ambient inbox/camera-roll ingestion as incidental scope expansion.

**Exit:** advertised source types survive device-to-owner round trips; controlled
environment receipts cover processing, recovery, deletion, and worker retries.
Do not confuse the old August 23 deployment report with a new production audit.

### 10.6 Lane ownership and collision boundaries

| Lane | Owns | Agreement needed from this lane |
| --- | --- | --- |
| Contribution/capture (this thread) | Input intent, authored attention, source processing, effective policy, immediate value, receipt and repair handoff | Stable source/decision/readback contracts; no competing owner stores |
| Life — `01a06ecc-1a79-74a1-9c47-9f24461313ea` | Organization, connected record, source refinding and browsing | Source-only destination and adapter; revision/availability/correction semantics |
| Components/Plan — `01a06e71-b35c-7ca0-8307-367db90a8a6a` | Intention/arrangement owner, editing grants, participation, current shared state | Commands and current authorization/readback; contribution does not imply adoption |
| Entity — `01a0649a-f267-7d31-a788-81669e1822a8` | Identity resolution, object page, source association with exact entity | Typed subject reference, redirects, access validation, return destination |
| Home/Places output | Later selection, substantive value, spatial/current-life expression | Eligible source/attention references and invalidation; no compulsory output per capture |

Coordinate contracts and overlapping file ownership at package boundaries, not
every local component decision. No messages or implementation tasks have been
dispatched to those threads by this planning update. Recheck their latest state
before claiming agreement. Use descriptive branches/worktrees for overlapping
implementation, and never sweep another session's dirty files into commits.

### 10.7 Verification plan

| Test layer | Required evidence |
| --- | --- |
| Pure policy | C1–C6, positive explicit continuity, conservative ambiguity, no model-issued grant, independent authority axes |
| Entry parity | Same meaning across ordinary Chat, pending send, OS share, entity Bring, voice/audio, and shared channel; different gestures are not artificially forced into identical outcomes |
| Writers and jobs | Negative assertions for forbidden DB/vector/file writes; positive assertions for authorized changes; queued jobs recheck revocation |
| Source lifecycle | Ask processing ends; original/derivative policies honored; retention independent of semantic confirmation; no hidden second copy |
| Causality | C6 before/after projection; delete during processing; stale job/read cache; independent later fact survives |
| Authored attention | Same photo with different authored observations; quotes/forwarded authors; no user claim mislabeled as photo evidence |
| Mobile and recovery | Useful-first result, actual receipts, inline finish/contextual continuation, retry idempotency, relaunch, denied access, logout, stale mutation callback |
| Cross-owner | Life source-only retrieval, exact entity return, intention readback, bounded shared contribution; unavailable owner does not yield a success claim |
| Media and deployment | Real representative bytes, bounded model evaluation, controlled private storage/provider round trips, worker heartbeat and schema compatibility |

Keep the initial regression commands from the September 4 investigation:

```bash
# From travel-agent; offline only
.venv/bin/pytest -q tests/core/test_contribution_policy.py tests/core/test_admission_contract.py tests/inbound/test_v2_security.py tests/inbound/test_submission_composer.py tests/inbound/test_intake_lifecycle.py tests/inbound/test_intake_v2_retention.py tests/inbound/test_intake_anchor_jobs.py tests/inbound/test_intake_content_bridge.py tests/concierge/test_inbound_screenshot_tool.py -m 'not requires_postgres and not requires_api_keys'

# From travel-app
npx jest --runInBand __tests__/screens/share-capture-intake-v2.test.tsx __tests__/screens/share-capture-audio.test.tsx __tests__/data/intakeV2Resumability.test.ts __tests__/components/sharing/ShareIntentHandler.test.tsx __tests__/utils/pendingChatTurnOutbox.test.ts __tests__/components/chat/composerAddCapabilities.test.ts
```

These are a starting regression set, not acceptance for new behavior. Add the
new portfolio, database-backed lifecycle tests, real-backend streaming tests,
and native QA as packages land. Follow mobile Task Intake: this is
parity-sensitive, streaming-sensitive, and product-shape-sensitive work. Extend
registered surface coverage for the new capture sequence; the old trip-photo
find screen alone is insufficient. Do not use Jest as visual acceptance.

For API/model changes, run workspace `./scripts/sync-types.sh`, review full and
active-mobile snapshots and generated TypeScript, and run operation governance.
Avoid starting the full backend for a read-only check: startup may dispatch
scheduled external work. Use isolated offline/test applications; external
provider verification needs its own explicit controlled execution authority.

### 10.8 Execution order, checkpoints, and commit plan

Work in dependency order, not an invented one-week deadline:

1. **D0 + P0:** design the portfolio while refreshing writer coverage and
   mapping existing contracts. Founder reviews the six sequences and §10.2
   decisions. Agree the minimal source-only handoff with Life.
2. **P1 + early P2/P3 adapters:** enforce policy and lifecycle; develop authored
   context and source-reader adapters behind tests. Do not activate the façade
   wholesale or require unrelated tool-catalog migration.
3. **P2 + P3:** connect useful responses and addressable originals to their
   actual owners. Resolve the intention/shared-owner gaps with the owning lane.
4. **P4:** integrate the designed result/re-entry/repair sequences across all
   representative cases. This is not six isolated mock screens.
5. **P5 and portfolio acceptance:** close advertised format/recovery gaps and
   obtain controlled environment/native evidence before broad enablement.

Suggested reviewable commit boundaries (split further where necessary):

| Batch | Deliverable |
| --- | --- |
| 1 | Refreshed writer ledger, policy mapping, D0 accepted decisions/refs |
| 2 | Contribution decision adapters + policy regression fixtures |
| 3 | Ordinary/pending send propagation + source lifecycle tests |
| 4 | Memory/background-writer gates + corresponding prompt/consumer adjustments |
| 5 | Authored-note/attention propagation + immediate utility contracts |
| 6 | Source-only reader and canonical destination adapter + Life integration tests |
| 7 | Value-first mobile flow and truthful compact readback |
| 8 | Cross-owner repair, re-entry, revocation-race tests |
| 9 | Format adapters and document entry, one supported family per bounded change |
| 10 | Recovery, controlled runtime/native evidence, rollout and legacy retirement receipt |

Backend, mobile, and root remain separate repos. Each API-bearing batch needs
compatible snapshots/types and corresponding consumer tests before handoff.
Stage explicit files only. This document update is planning, not authorization
to commit code, deploy, delete legacy data, or enable providers.

### 10.9 Completion and rollout posture

Call this lane implemented only when the portfolio delivers immediate useful
value, justified continuity, reliable refinding, and causal repair through real
owners. A green upload test, attractive result screen, or pure resolver is not
the complete contribution experience.

Measure time to first useful result separately from upload acknowledgment;
successful source refinding separately from storage; and required user actions
separately from total interactions. Track unsupported-format failures, recovery
success, missed explicit contributions, blocked unauthorized writes, and stale
post-correction reads. Use content-free operational telemetry, not personality
inference or more user homework. Set latency/cost budgets from representative
measurements before expanding rollout; do not invent success thresholds here.

Deploy schema/read compatibility before new writers. Enable only reviewed paths
for a bounded cohort after owner, media, worker, retention, and native evidence
exist. Rollback stops new processing/effects while preserving legitimate sources
and readback; it must not silently reactivate unsafe legacy retention. Retire a
legacy writer only after caller inventory, read compatibility, recovery, and
correction coverage show the replacement is sufficient.

A partial executable pass covers admission policy, source custody, admitted
Chat handoff, and mobile recovery slices. The full P0–P4 acceptance bar is not
yet landed. The September 5 review found remaining lifecycle, retry, writer,
and result-composition work; §11 now owns the immediate execution order.
Controlled P5 evidence runs alongside those repairs. Work can proceed without
waiting for every Life, Plan, entity, or Home visual decision; consumer handoffs
still require implemented owner contracts.

## 11. Completion plan — September 5

### 11.1 Outcome and current evidence

Complete the contribution experience across the existing product:

> I give Vesper something that has my attention. It helps with that thing now.
> If I intended to keep or contribute it, it remains easy to find in the right
> context. I can correct it, and later uses respect that correction.

This is implementation planning, not a new product canon or release receipt.
The work below completes P0–P5 using the same source, policy, conversation,
Life, and domain owners. The CC batch identifiers describe executable pieces
of that scope; they are not another architecture or a competing roadmap.

Fresh inspection used backend `120c34b31`, mobile `73f89ffa8`, and workspace
`8682452` as planning references. Concurrent work is active. Re-pin commits and
file ownership before implementation; a reference here does not freeze another
lane. The earlier contribution repairs are backend `42964124e` and mobile
`5a2b02ed4`; mobile `ee8b6588c` subsequently added capture return continuity.

| Capability | Evidence-backed status | Remaining work |
| --- | --- | --- |
| Ask/Bring admission | Shared `contribution_admission.py` adapter, explicit Intake retention, and pending-turn decisions exist | Complete enforcement across ordinary Chat, replay, copies, and background writers |
| Authored attention | Semantic worker supplies `user_note` separately from normalized source evidence | Preserve that distinction durably through canonical send/retry and test its effect on returned value |
| Retained originals | Source-only projections and Life intake readers exist independently of confirmed interpretation | Repair count query; verify large collections, sibling sources, exact re-entry, and correction |
| Capture to Chat | Durable pending-turn handoff, audio-not-ready handling, reconciliation, and recovery controls exist | Stable identity for one gesture, distinct identities for later gestures, authoritative reconstruction after relaunch |
| Visible result | Receipts and contextual Chat continuation exist | Generic share result still makes interpretation review primary; deliver usable value before controls |
| Native evidence | September 4 iOS build included the extension and accepted the marker URL | Full supported-payload round trips, cold/warm repeated shares, real server readback, and interruption/relaunch remain unevidenced; Android build was blocked by missing local SDK |
| Wider continuity | Life, Home/Places, entity, and repair substrates exist | Approved loose-intention and attributed shared-material commands; complete downstream repair evidence |

The preceding status review reran **337 offline backend tests** (20 deselected)
and **31 mobile tests** successfully. Those selections did not exercise the
retained-source count query: a separate local call reproduced
`TypeError: FromClause.select() takes 1 positional argument but 2 were given`.
The exact failing expression is in
`backend/core/db/intake_anchors.py::count_retained_source_projections`.
Treat the green selections as regression evidence, not full conformance.

Additional code-inspected gaps, requiring the integration reproductions below:

- Pending send adds `__server_authority_user_message` after request validation,
  but session persistence removes it from saved turn metadata. Canonical retry
  restores the saved metadata; its fingerprint and authority input therefore
  need a durable, consistent replacement. The legacy trip Chat route also has
  a separate request model to audit for reserved-field injection.
- Semantic completion resets transient expiry to completion time plus 24 hours.
  Intake expiry currently selects verified sources with non-null deadlines;
  old null deadlines and abandoned other custody states need explicit inventory.
- Canonical Chat image persistence creates its own filesystem-backed copy.
  That copy is not automatically governed by Intake source cleanup.
- Share capture uses the submission UUID as the Chat gesture ID, while other
  staging callers default to a new UUID per invocation. Reopened media kind is
  partly reconstructed from route parameters. These cannot establish complete
  retry/new-gesture parity.
- Native replay deduplication retains a content/URL signature. It needs tests
  for a legitimate later identical share, including platforms without a unique
  URL marker, and ordering between URL and payload delivery.

### 11.2 Decisions and ownership boundaries

The accepted contribution contract already settles: value before administration;
Ask does not imply personal learning; deliberate Bring can retain a private
original; a model interpretation cannot authorize itself; correction follows
dependencies. Implement those rules rather than reopening them as hypotheses.

| Decision | Recommended implementation direction | When it must be settled |
| --- | --- | --- |
| Authored input versus evidence | Preserve authenticated authored input and typed source references separately in server-owned admission/replay provenance. Build display/model text from them; never reconstruct authority from flattened source text. | CC-1 design, before modifying retry persistence |
| One gesture versus one source | A source has a durable identity. Each intentional Chat question/send has its own identity. Network retry reuses that gesture's immutable request; a later question about the same source starts a new gesture. | CC-1; applies to every staging caller |
| Conversation history versus source retention | Define authored message history, generated answer history, extracted source text, transcripts, original files, and copied images separately. Recommended default: retain ordinary conversation under its explicit history policy, keep Ask processing copies transient, and make original-source unavailability legible. A source-derived answer cannot be a hidden exemption that reconstructs released material. | CC-2 must record the exact history rule before promising complete Ask expiry or migrating historical content |
| Inline result versus Chat | A deliberate import can finish with useful source details inline. A question receives its answer in the existing conversation. Contextual Chat is available for depth; creating a conversation is not a prerequisite for source custody. | CC-4 sequences, before changing result hierarchy |
| Source-only Life destination | Use the existing submission/source reader and exact owner identity; an unconfirmed interpretation is never required to retrieve an original. | CC-0/CC-5 adapter agreement with Life |
| Loose intention and social material | Reuse an approved intention/arrangement or attributed-contribution owner. If existing owners cannot represent it, document the missing command and minimum schema choice with Integration/Plan. | Before those CC-5 writes; does not block private capture or source readers |
| Additional media | Keep current supported types and accurate rejection. A future PDF/Wallet/HEIC intake adapter requires scanner, normalization, lifecycle, renderer, and native evidence ownership. | Separate follow-on; not on this completion path |

For behavioral writers, use the canon's distinction between product/situation
signals and governed person/relationship evidence. A generated preference in
the first person is not an authored claim. Unresolved semantics must restrict
promotion rather than permit it. Any proposal to expand longitudinal learning
is a separately recorded product decision; conservative enforcement of the
existing rule is ordinary repair work.

This lane owns input meaning, source processing, admission, immediate result,
receipt, and repair handoff. Life owns organization; Home/Places own later
selection and expression; Entity owns exact object identity; Plan/Occasion
owners own arrangement and participant consequences. Detailed composition
belongs in the dedicated design tool. Production Chat-root redesign and new
Life navigation are outside this plan.

### 11.3 Execution batches and dependencies

| Batch | Existing scope | Deliverable | Dependencies |
| --- | --- | --- | --- |
| CC-0 | P0/P3 | Correct source counts and a current acceptance ledger | Can start immediately |
| CC-1 | P1/P5 | Durable authored authority and gesture-stable retry across entries | Current source/policy owners; independent of visual design |
| CC-2 | P1/P5 | One enforced lifecycle across original and processing copies | History decision; coordinates provenance fields with CC-1 |
| CC-3 | P0/P1 | Remaining writer enforcement and repair lineage | Existing canon; shares policy vocabulary with CC-1/2 |
| CC-4 | D0/P2/P4 | Useful-first result composition across the consumer portfolio | Design begins immediately; integration uses CC-1/2, CC-3 for learning and CC-5 for owner effects |
| CC-5 | P3/P4 | Exact owner return, intention/social handoffs, cross-surface correction | CC-0–3 where relevant; new owner commands require their owner agreement |
| CC-6 | P5 + all exits | Real transport, native, model-quality, and rollout evidence | Collect incrementally; final acceptance after dependent batches |

#### CC-0 — source-reader repair and acceptance ledger

**Code:** `backend/core/db/intake_anchors.py`,
`backend/life_projection/intake_page.py`; existing
`tests/inbound/test_intake_anchor_projection.py` and
`tests/life_projection/test_life_intake_page.py`.

Replace the invalid column-select construction. Express the source-local
unrepresented-source rule as a reusable SQL predicate used consistently by
count and page eligibility, with a database aggregate for totals. Avoid reading
every submission, candidate, and observation into Python to count a large corpus.
Preserve the current product cardinality: a retained submission contributes one
source-only record when at least one eligible sibling remains unrepresented.
Confirm this against Life's latest index and compatibility-reader paths before
changing their interfaces.

Add database-backed cases for: no records; one source; a confirmed candidate
representing one of several siblings; all siblings represented; revoked/deleted
sources; expired transient custody; another owner; and a corpus exceeding the
page limit. Invoke the real counter through the paginated Life adapter, not a
mock counter. Verify deterministic continuation and consistent totals under
the declared represented-time/read semantics.

**Exit:** the reproduced crash is fixed; reader/count predicates agree; the
production count does not materialize the full corpus. Record baseline failures
and their exact test owner in this document before larger changes.

#### CC-1 — authored authority and reliable gesture identity

**Backend:** pending-turn model/route/store; canonical and legacy Chat request
adapters; `_message_flow.py`; `concierge/session.py`, `turn_admission.py`,
`agent.py`, and `action_authority.py`.
**Mobile:** `utils/chat/pendingChatTurnOutbox.ts`,
`components/sharing/ShareIntentHandler.tsx`, `app/share-capture/index.tsx`,
`hooks/useConciergeHomeConversationEntry.ts`, and
`app/conversations/create.tsx`.

1. Define one server-owned representation for authenticated authored input,
   source refs, admission decision/basis, and request identity. Prefer extending
   the existing pending/message provenance owner over a new table. Persist the
   minimum replayable provenance or a reference whose lifetime covers retry;
   do not make message replay depend on an already-released outbox payload.
2. Make send, failed-message retry, reconnect, and queued execution resolve the
   same authored authority. Current custody/audience must still be rechecked.
   Keep all client metadata paths unable to manufacture server provenance.
   Old flattened messages with insufficient provenance cannot gain write
   authority through fallback text parsing.
   Explicit narrowing such as “only answer; do not keep this” outranks a
   share/import affordance. Define and test that admission path before durable
   source retention; an Ask about an independently retained original is a
   different case and must not silently revoke the earlier Keep.
3. Specify fingerprint inputs and versioned compatibility. Authored content,
   source selection, audience, requested job, and retention changes remain
   meaningful conflicts. Server-added receipts, volatile execution state, and
   metadata stripping cannot make an unchanged logical retry conflict. Do not
   solve conflicts by dropping policy fields from the fingerprint.
4. Allocate the client gesture ID before the first stage attempt. Preserve the
   same request and identity after an ambiguous network result or process
   restart using the existing scoped resumability mechanisms. Account/device
   boundaries and local-file availability must remain explicit. Do not store
   source bytes in route parameters or create a second general-purpose outbox.
5. Give a deliberate later Ask a new ID while retaining the same source refs.
   Reconcile accepted/cancelled/expired pending records before offering retry;
   opening a retained source is not automatically resending its old question.
6. Rebuild media kind, source refs, and authored note from canonical submission
   readback after relaunch. Route parameters may carry navigation context but
   must not change the admitted payload on retry.
7. Deduplicate native delivery events without suppressing a later intentional
   identical share. Test stale-payload/new-marker ordering and reset/replay.
   Apply the same contract on platforms with no unique marker; document the
   actual native event identity available before choosing the adapter.

**Required tests:** an accepted stage whose response is lost creates one pending
turn and one canonical user message on retry; failure after message persistence
replays the original authority/fingerprint; a new question about the same source
creates a new turn; changed content/audience/retention cannot reuse an ID; forged
server metadata cannot authorize writes through either Chat route; source text
containing “remember/save/note” cannot authorize memory; an explicit authored
Keep still works; an explicit no-retention instruction narrows a new OS import.
Cover photo/audio/text relaunch, multi-source selection,
cancel/retry, expiry, logout, and repeated identical native shares.

**Exit:** one gesture survives recovery without duplication or lost authority;
separate gestures remain possible. These are transport changes within existing
Chat, not a redesign of its root.

#### CC-2 — source and derivative lifecycle

**Code:** `core/db/intake_v2.py`, `intake_semantics.py`, `intake_lifecycle.py`,
`chat_images.py`; `workers/intake_semantic_jobs.py`; source deletion/expiry
outbox consumers; canonical Chat materialization and image readers.

Create a concrete copy/consumer inventory before changing cleanup: original
upload, normalized text/image, transcript, pending payload, canonical Chat image,
flattened extracted message text, generated answer, observations, vectors, and
cached projections. For each, record owner, purpose, expiry trigger, maximum
retry lifetime, lineage, read-time rejection, and physical cleanup mechanism.

- Establish temporary custody at first admission. Processing completion,
  failed retry, or re-interpretation cannot extend its maximum 24-hour backstop.
  Natural completion should release Ask processing material earlier when safe
  for the declared retry/history contract.
- Keep explicitly retained originals retained across semantic completion,
  failure, and replay. Asking about an already retained original does not revoke
  its prior custody; the new answer's use and learning remain independently scoped.
- Stop serving expired/revoked sources immediately, even if object deletion or
  projection recomputation is still queued. Recheck authority before committing
  late worker results and before hydrating copied media.
- Converge new source-backed Chat reads on the existing source owner wherever
  possible. If a derivative copy is necessary, record its parent, purpose and
  expiry and connect cleanup; avoid indefinitely duplicating Intake bytes into
  `chat_images`.
- Inventory old null deadlines, legacy message copies, orphan uploads, and
  non-verified custody states. Use the appropriate existing upload/security
  lifecycle for quarantined material; do not sweep it with an assumed Ask rule.
  Prepare a bounded, dry-run migration/report and compatibility reader before
  any historical cleanup. Uncertain legacy custody cannot be reclassified from
  filenames, model guesses, or the date alone.
- Enforce separate claim/projection eligibility; deleting raw bytes alone does
  not prove expiry of extracted text or a derived personal claim. Reconcile this
  with the explicit conversation-history decision in §11.2.

**Tests:** frozen-clock admission/processing/retry beyond the original deadline;
retained Bring with failed extraction; null-deadline legacy inventory; expiry
with worker unavailable; delete while extraction is running; retry against
revoked media; duplicate cleanup delivery; surviving independent sibling; copied
Chat media rejection and cleanup. Include PostgreSQL/outbox and temporary-file
evidence, not only model assertions.

**Exit:** each supported entry has a traceable lifecycle for its originals and
copies; expiry blocks use before cleanup completes; migration preserves legitimate
retention. A history decision or historical cleanup approval can gate that part
without delaying the non-extension fix for new temporary sources.

#### CC-3 — remaining memory and background writers

Use the [I3 writer audit](i3-writer-authority-audit-2026-09-05.md) as the discovery
list, then recheck actual callers and enabled paths. Include explicit memory
tools, `preference_engine/edit_inference.py`,
`core/personalization/discover_synthesizer.py`, `core/memory_signal.py`,
accommodation/planning hooks, reflection, `refresh_memory.py`, and group synthesis.

For each reachable writer, record input gesture/evidence, destination, allowed
learning target/level, policy gate, replay identity, source revision, and repair
consumer. Enforce before persistence or promotion. A browser interaction can
remain bounded product/situation evidence without becoming first-person taste.
Low importance or `source_mode="inferred"` alone is not a permission gate.

Preserve positive functionality: explicit Keep, authored preferences and
constraints within their granted scope, and source-bound Point/Bring behavior
must still work. Do not turn conformance into a demand that users say “remember”
for every legitimate source import or explicit observation. A retained photo,
an authored observation, an inferred preference, and a shared contribution have
different destinations and authority.

Synthesis must consume eligible evidence and retain dependency/version labels.
Correction or release invalidates its use immediately and triggers bounded
recomputation through existing jobs. Generated prose cannot return as new
evidence. Keep independently authored observations and affected participants'
private context intact. Prompt changes receive the prompt-sensitive validation
required by Task Intake and remain confined to this behavior, not Chat redesign.

**Exit:** every inventoried reachable writer has an enforced disposition and
positive/negative tests. Exercise explicit Keep, source-only Bring, behavioral
signals, correction, late jobs, private/group scope, and synthesis together;
do not call an audit table itself an enforcement result.

#### CC-4 — useful-first result and receipt design

Extend D0 and [Chat work package A](claude-design-integration-2026-09-04/04-chat.md)
in the dedicated design tool. Use one reusable interaction vocabulary expressed
in the existing capture surface and Chat. No new Capture tab or maintenance inbox.

The composition rule is: useful answer/extraction/connection first; compact
actual custody or owner result where relevant; optional depth and repair.
Interpretation review is secondary unless a specific uncertainty changes the
requested consequence. Do not replace review cards with an equally verbose
policy explanation. Pending analysis must not make an already retained original
look like an unfinished task the person owes the app.

| Sequence | Complete first result | Quiet consequence and continuation |
| --- | --- | --- |
| C1: ticket + arrival question | Answer the question from supported details; expose a material ambiguity only if needed | Ask treatment, no attendance/tracking claim; answer remains reachable under history policy |
| C2: same ticket deliberately imported | Readable ticket details and a supported practical issue if present | Original retained where authorized; exact Life/source door; analysis can finish later |
| C3: cliff photo + authored observation | Respond to the buildings/cliffs observation and contribute a supported comparison or explanation beyond paraphrase | Keep permitted original/attention, not an inferred personality; Place/depth continuation is optional |
| C4: “Keep jazz in mind for Saturday” | Show the precise intention accepted by its owner, or honestly identify an unapplied effect | Soft time and original wording; no naming wizard or invented Trip; later Home use only within scope |
| C5: contribution to an Occasion | Authored photo/note appears in its actual permitted shared context | Attribution and audience visible where useful; no automatic edit, attendance or personal learning |
| C6: “That ticket was cancelled; I never went” | The specific supported correction and actual owner readback | Original may remain; dependent occurrence/use is withdrawn; independent later events survive |

Use a supported image or text ticket fixture until document formats are enabled.
The sequence is about the human job, not a claim that PDF/PKPass support exists.
Add a receipt-only versus explicitly allocated expense variant using the
[assisted-expense brief](assisted-expense-contraction-brief-2026-09-05.md): useful
extraction does not create debt; approved commands go through the existing exact
Trip expense owner. Expense screen retirement is owned elsewhere.

For every sequence, design entry → first result → leave → reopen → correct,
including a thin result, partial batch, long note, pending/failure, denied
permission, lost connection, unavailable owner, and account/audience change.
Do not create a bespoke full-screen workflow for each case.

**Implementation:** reuse the existing composer/context attachments,
`IntakeLifecycleReceipt`, source readers, response renderers, and correction
controls. Extract result-state selection from the large share screen where it
reduces duplicated branches. Distinguish successful storage from useful model
output; surface independent verified details while optional interpretation is
pending. Bound generation, reuse verified extraction, and let the user leave
after actual server acknowledgment. Routine completion does not require push.

**Exit:** useful value is reachable without Keep/classification first; Chat is
not an extra toll for already-available details; processing, result and retention
states remain distinct. Keep/Correct/Undo describe real effects. Receipt/error
copy exposes no internal authority taxonomy, preserves a clear Done/return, and
never claims unuploaded local material is safe.

#### CC-5 — owner handoffs and causal repair

Publish a field-to-owner mapping over existing models before adding schema.
The common handoff needs authenticated contributor/authorship, source identity
and revision, authored note, truth status, permitted purpose/audience/expiry,
origin context, canonical destination, actual effect receipt, and repair targets.
Reuse existing fields and lookups; navigation context does not grant authority.

| Receiving owner | Integration obligation | Completion evidence |
| --- | --- | --- |
| Life | Find retained originals independently of candidates; preserve note, media availability, exact identity and appropriate time/place associations | Capture → leave/relaunch → exact original, including unclassified and mixed-success sources; no guessed visit/time |
| Entity / Places | Preserve exact subject and originating Places context; source association remains distinct from visit, review or public contribution | Return after capture/correction to the same valid object/context; changed permissions fail closed |
| Home/Places output | Consume eligible evidence and revisions; recompute or reject invalidated dependencies | Correction removes the false basis from a later return; no obligation to emit a card per input |
| Intention / Plan | Preserve authored wish, soft time, revision, release and optional association through an approved command | C4 survives without compulsory Trip/Plan creation and does not acquire commitment by inference |
| Occasion / social | Keep contributor, subjects, custody, recipients and canonical owner distinct | C5 attribution/audience survive projection; withdrawal reaches shared uses without deleting unrelated private originals |
| Expense | Consume the shared receipt Source and explicit instruction; deterministic owner handles allocation/correction | Receipt-only creates no debt; explicit supported allocation produces exact owner readback |

Adopt existing Integration work, including capture return continuity and
Life-to-Places correction invalidation, after verifying its current contract.
Do not rebuild those systems. Browser navigation and cache invalidation alone
do not establish server-side repair or block stale queued work.

For each mutation/release, test canonical source/claim change → owner readback
→ read-time exclusion → Home/Places/Life/Chat reader updates → queued work
revalidation. Include an offline/stale client and a delayed projection job.
Delete, detach, interpretation release, occurrence correction, and audience
withdrawal are separate commands; only expose those supported by the owner.

**Exit:** C2/C3 refinding and C6 repair run through real owners; intention/social
sequences name an approved command and implemented consumer. If an owner is not
ready, ship permitted private handling with honest unapplied-effect readback
and leave that sequence explicitly incomplete. Do not counterfeit success with
a chat message, fake semantic confirmation, or pseudo-Trip.

#### CC-6 — integrated evidence and release posture

Run acceptance incrementally as batches land; final certification uses the
same recorded backend/mobile/schema revisions. Maintain one evidence matrix in
this plan keyed by C1–C6 and failure variant, with code test, database/transport
receipt, native capture, content assessment, remaining gap, and owner.

Initial sequence ledger (September 5; component presence is not journey acceptance):

| Sequence | Available foundation | Acceptance still required | Lead / receiving owner |
| --- | --- | --- | --- |
| C1: question + source | Source-backed send, authored note, answer-only admission | Retry authority, all processing-copy expiry, actual answer quality and native return | Capture / Chat |
| C2: deliberate import | Verified retention, source-only reader and Life adapter | Useful inline result, corrected paginated reads, relaunch/refinding with failed interpretation | Capture / Life |
| C3: authored observation | Separate semantic note input and retained-source path | Note-dependent substantive result, scope-preserving continuity, correction without original loss | Capture / Life / output owners |
| C4: loose intention | Product contract and existing domain capabilities to evaluate | Accepted exact owner/command, persistence, soft-time readback and scoped later use | Integration / Plan |
| C5: shared contribution | Existing Occasion/audience and receipt substrates | Approved attributed-material command, actual projection, withdrawal and changed-membership evidence | Occasion owner / Capture |
| C6: correction | Source/candidate repair and some downstream invalidation | End-to-end dependency exclusion, queued-job rejection and independent-evidence survival | Capture / all affected readers |

All six remain **open at full-journey acceptance**. Replace each cell with dated
test/receipt references as it closes; keep native, transport and content evidence
separate rather than turning one green unit test into a journey pass.

1. **Deterministic:** policy/fingerprint tests plus actual DB readers, lifecycle,
   writer denials and authorized positive cases. Expand the current tests where
   failures occur at route/session/worker boundaries; helper-only assertions
   cannot substitute for those paths.
2. **Real transport:** isolated test application and private test data for stage,
   send/SSE, lost response, interrupted finalize, partial extraction and repair.
   Do not start the full scheduled backend simply to check a route.
3. **Native:** use registered `photo-media-intake` for capture and `vesper-chat`
   for conversation. Extend the former's contract/registry with share-capture
   sequences; its current trip-photo-find evidence does not cover them. Exercise
   true OS delivery, cold/warm start, duplicate callbacks, later identical share,
   supported text/image/audio/multi-file, permission denial, background/relaunch,
   account switch, small screen, dynamic type and keyboard.
4. **Content:** assess C1/C3 and thin/partial variants for actual job completion,
   added substance, source grounding, latency and cost. Fixtures prove rendering;
   a bounded real-model run is needed to assess generated usefulness. Repeating
   the user's own observation is not sufficient added value.
5. **Readback/repair:** retrieve the same original from Life; inspect current
   entity/Places context; execute C6 and verify downstream exclusion plus survival
   of independent evidence. Test shared withdrawal under a changed audience.

Follow the repository's registered screenshot/verdict workflow. Record a
missing Android SDK or unavailable provider as the exact unproven lane; neither
an iOS build nor mocked screenshots imply cross-platform end-to-end success.
Keep historical native receipts dated rather than overwriting them with a pass.

Measure elapsed time to acknowledgment and to first useful result separately;
record required user actions, source-refinding success, retry duplicates,
unsupported-format failures and stale post-correction reads. Use representative
measurements to set latency/cost budgets. C1/C2/C3 require no classification
action before value; ignoring an optional continuation creates no review debt.
Avoid content-bearing telemetry or automatic personal interpretation of usage.

Deploy compatible readers/schema before writers, then enable only the paths
with matching evidence. Rollback disables new processing/effects while preserving
legitimate sources, reads, correction and receipts. Never route rollback to a
known unsafe legacy writer. This planning update deploys nothing and authorizes
no historical deletion or new external connector.

### 11.4 Solo-founder sequence and reviewable commits

Begin **CC-0 and CC-1 engineering** while the dedicated design tool explores
**CC-4's complete sequences**. These can proceed independently. Coordinate
CC-1/CC-2 provenance fields together; execute lifecycle and writer changes in
small batches. Owner discussions for CC-5 can happen early without blocking
private capture. Integrate the designed result once its underlying readback
and retry semantics are stable. Collect CC-6 evidence throughout.

Do not assign an artificial one-week deadline. Reliability fixes are bounded;
history semantics, remaining writer migration and shared-owner gaps carry the
larger uncertainty. Review the concrete user sequences and boundary decisions,
not every helper function. Reuse current tests/readers and the agreed four roots.

Suggested commit order (split by child repository and further when necessary):

1. Correct retained-source count and add real pagination/sibling-source tests.
2. Persist server-owned authored provenance; make send and retry authority and
   fingerprints consistent; cover canonical and legacy request adapters.
3. Stabilize per-gesture client admission/recovery across all staging callers;
   distinguish repeat Ask and native event replay; recover media from readback.
4. Preserve original temporary deadline and retained-source custody across
   workers; test expiry/delete races and cleanup outbox.
5. Reconcile new Chat processing copies with source lifecycle; add compatibility
   reads and a dry-run historical inventory under the settled history policy.
6. Enforce writer dispositions and dependent synthesis repair, writer family by
   writer family; retain authorized positive behaviors.
7. Record accepted CC-4 sequences and implement shared useful-result hierarchy,
   compact receipt, clear leave/retry, and bounded Chat continuation.
8. Complete existing Life/entity/Home/Places handoff and correction tests;
   implement approved intention/social/expense adapters in separately scoped
   owner-coordinated commits.
9. Add native/real-transport/content evidence, update the completion matrix and
   prepare the bounded rollout/compatibility receipt.

**Validation classification:** documentation planning now; implementation is
backend contract-sensitive and, for writer/synthesis behavior, prompt-sensitive.
Mobile is parity-sensitive/streaming-sensitive with product-shape review for
CC-4. Read the relevant Task Intake and surface contract for each batch. Schema,
authority-model or background-posture decisions receive the required founder
review as concrete proposals; routine regression repairs need no new product
decision.

For backend route/model changes, run workspace `./scripts/sync-types.sh`, review
full/mobile snapshots and generated types, and fix mobile parity before handing
off. Run required local backend checks plus applicable PostgreSQL tests; run
mobile typecheck and focused Jest, real-backend validation for streaming changes,
and native verdicts for visible changes. Record any unavailable required check
accurately. Respect size/import/doc checks; use a small shared helper or module
where it improves ownership rather than bypassing a failing local gate.

Use isolated worktrees for overlapping code work. Check branches, worktree and
index before every commit; stage explicit owned files and inspect the entire
staged diff. Another task's staged changes must not enter a contribution commit.
Root documentation, backend and mobile retain separate histories. Update this
plan's receipts and the Integration I3 handoff at package boundaries; refresh
stale implementation statements in the system contract after behavior lands.

### 11.5 Definition of completion

The lane is complete for its declared supported portfolio when:

- giving material produces useful value before optional administration;
- Ask, Point/Bring, Keep, shared contribution and correction exercise their
  actual separate authority without a user-facing classification form;
- originals are findable independently of interpretation confirmation;
- a lost response/relaunch cannot duplicate a gesture, and a later deliberate
  gesture about the same source remains possible;
- original/derived/source-copy lifecycles match their declared policy;
- every inventoried active writer has an enforced and tested disposition;
- correction/withdrawal blocks dependent reads and delayed work while preserving
  independent evidence;
- owner effects and unavailable effects are represented honestly; and
- real transport, native and generated-content evidence support the paths being
  enabled, with remaining format/platform/owner limits stated precisely.

Completion is not conditional on supporting every possible media family or
finishing every root's visual design. It is conditional on the supported
contribution experience actually working across the relevant owners.

### 11.6 Execution receipt — September 5

The first implementation pass has now landed in bounded commits. These are
engineering receipts, not a claim that the entire portfolio is production
proven:

| Batch | Commit / evidence | Result |
| --- | --- | --- |
| CC-0 | Backend `e0885b98d`; focused Life reader/count suite: 11 passed | Retained-source page and count share one bounded, source-local SQL projection; the invalid full-corpus count expression is gone. |
| CC-1 | Backend `9f00c92ce`; retry/authority and action-authority tests pass; mobile `3ff5dac62`; pending-turn outbox: 5 passed | Server-owned authored authority survives persistence/retry; canonical and legacy Chat routes reject forged authority metadata; a share's Chat gesture ID is distinct from the intake submission and stable across retry. |
| CC-2 | Backend `ff3915b6b`; semantic-worker retention tests: 2 passed | Semantic completion preserves the original transient custody deadline and does not extend it; derived-only retention remains deadline-free. |
| CC-3 | Backend `add16495d`; writer/refresh focused suite: 53 passed | Behavioral and engagement writers are explicitly non-authoritative, reversible derived signals with bounded importance, provenance, confidence/expiry, and visible derived labeling during Personal Memory synthesis. |
| CC-5 | Existing owner/activation/correction portfolio: 44 passed | Handoff receipts, exact owner readback, activation replay, and semantic correction helpers remain fail-closed and owner-scoped; no new owner command was invented without an owner contract. |

The mobile outbox and capture tests provide local transport evidence, but the
app-wide typecheck is currently blocked by an unrelated concurrent entity/Places
change in `app/venue/[venueId]/index.tsx`. The backend pre-commit size budget
and one pre-existing error-category registration finding also remain outside
these bounded commits; they were explicitly skipped and must be cleared before
publication. CC-2 still needs the copy/consumer inventory and Chat-image
cleanup policy, CC-4 still needs the full useful-first result sequence and
registered native evidence, and CC-6 remains open for real transport, native,
and generated-content runs.
