---
doc_type: working
status: active
owner: founder / product / architecture / backend / mobile
created: 2026-08-29
last_verified: 2026-09-04
expires: 2026-09-28
why_new: Translates the accepted Contribution and Consequence Contract into a code-grounded, architecture-spanning migration plan for Chat, Intake, memory, synthesis, behavioral inference, receipts, correction, and mobile contribution surfaces without prematurely committing to a database migration.
promotes_to: null
supersedes: []
---

# Contribution Contract and Legacy Memory Migration Plan

> **Execution update — September 4:** [§10](#10-contribution-and-capture-execution-plan--september-4)
> is the current proposed work breakdown, baseline, dependency order, and
> acceptance plan for the contribution/capture lane. Sections 1–9 preserve the
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
| Value-first capture | Unresolved shares can continue into contextual Chat with source refs and `answer_only` retention rather than forcing a review workflow. | `09b80dbaa` |
| Media/recovery truthfulness | Mobile preserves server-side HEIC/scanner capability errors instead of collapsing them into generic retry copy; local retry and custody resumability remain covered by tests. | `cdf048617` |

PDF, Apple Wallet, and HEIC/HEIF remain deliberately unsupported at the
intake boundary: the backend security contract rejects them until a document
scanner/conversion path is actually available. The mobile layer must mirror
that boundary, not advertise a normalizer class as a supported product
capability.

The remaining P5 work is operational evidence, not a reason to widen scope:
controlled native/share-extension runs, interrupted-finalize and relaunch
receipts, mixed-success batch evidence, and a separately reviewed readiness
decision for each new document family. No connector, ambient ingestion, or
legacy-writer retirement is implied by these commits.

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

This is native compilation and intent-boundary evidence, not proof of an OS
share-sheet round trip. We still need a controlled simulator/device share of a
text, image, audio, and multi-file payload, followed by server readback and
relaunch/interrupted-finalize evidence. The committed source of truth for the
native extension is `app.json`/`app.config.js`; generated `ios/` output is
ignored and must not be treated as a separately landed contract.

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

The first executable pass (P0–P4 plus the safe part of P5) is now landed in
the child repositories. The next executable scope is controlled P5 evidence:
native/share-extension round trips, relaunch/interrupted-finalize receipts,
mixed-success recovery in the real transport, and owner agreement for any
new document family. We can continue that work without waiting for every Life,
Plan, entity, or Home visual decision, but should not promise a consumer
handoff those owners have not actually agreed to or implemented.
