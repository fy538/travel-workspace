# Area Audit: Privacy and Group-Safe Synthesis

Date: 2026-05-21  
Agent: Cursor Cloud / Codex audit session  
Scope: Travel Agent concierge compose/proposal/privacy redaction, preference synthesis, invite intake, privacy audit routes; Travel App invite intake, proposal cards, privacy audit, notifications/invite status surfaces; reliability traces and targeted tests.  
Mode: Audit only. No product-code changes.

## Executive Summary

- Dogfood risk: Medium
- Highest-risk finding: Proposal redaction only loads the proposing user's private corpus, so organizer-created proposal copy can leak another member's exact private budget phrase and then render in group-visible proposal cards.
- Checks run:
  - `make contract-check` -> pass
  - `make mock-real-parity` -> pass
  - `PYTHONPATH=. pytest tests/eval/test_concierge_checks.py tests/eval/test_planning_checks.py tests/eval/test_restaurant_checks.py tests/concierge/test_group_compose.py tests/concierge/test_privacy_redactor.py -q` -> pass, 200 tests
  - `npm test -- --runInBand __tests__/data/privacy.test.ts __tests__/screens/privacy-audit.smoke.test.tsx` -> pass, 20 tests
  - Deterministic redactor probes -> confirmed gap for `"Dev's $50 ceiling"` when not in proposer corpus
- Residual uncertainty: I did not run live LLM canaries, provider APIs, or a live Postgres end-to-end invite flow. Some risks below are static-confirmed code paths but need DB-backed repro to measure how often they surface in current dogfood data.

## Findings

### P1 — Proposal Redactor Misses Other Members' Exact Private Phrases

Status: Confirmed  
User impact: A traveler can privately share a budget/medical/social phrase, but a group proposal created by the organizer or agent can expose that exact phrase to the group if the generic keyword regex does not catch it.  
Product promise affected: privacy / proposal review / concierge trust

References:

- `Travel Agent/backend/concierge/tool_handlers/planning/_propose_present.py:214` — proposal privacy boundary runs before persisting group-visible proposal copy.
- `Travel Agent/backend/concierge/tool_handlers/planning/_propose_present.py:225` — loads `private_corpus` only for `proposed_by`.
- `Travel Agent/backend/concierge/privacy_redactor.py:72` — checks title, description, and impact text using keyword + supplied corpus.
- `Travel Agent/backend/core/privacy_signal.py:59` — budget regex catches phrases like `tight budget`, but not bare phrases such as `$50 ceiling`.
- `Travel Agent/backend/core/db/change_proposals.py:57` — persists title, description, and impact analysis as-is.
- `Travel Agent/backend/api/routes/proposals.py:119` — proposal detail returns group-visible description and impact analysis to any trip member.
- `Travel App/components/chat/VoteWidgetCard.tsx:87` — group chat vote widget renders proposal title/description.
- `Travel App/components/trip/ProposalReviewSheet.tsx:347` and `Travel App/components/trip/ProposalReviewSheet.tsx:560` — proposal detail renders description and impact text verbatim.

Why it matters:

Existing eval tests correctly verify that `Dev's $50 ceiling` fails when explicitly configured as a forbidden phrase, but the production proposal redactor only gets the proposer's private corpus. If Sarah privately told the concierge about Dev's budget, or the organizer proposes on behalf of the group using Dev's constraint, Dev's exact phrase is not in the corpus being checked.

Repro or deterministic test idea:

1. Add a unit test around `_execute_propose_change` where `proposed_by=organizer_id`, another member has private corpus phrase `"Dev's $50 ceiling"`, and proposal description is `"Move dinner because Dev's $50 ceiling rules out Belcanto."`
2. Expected: proposal creation is rejected before DB write.
3. Current observed by deterministic probe: `check_proposal_privacy(..., private_corpus=[])` returns safe for `"Move dinner because Dev's $50 ceiling rules out Belcanto."`; the same phrase fails only when `"Dev's $50 ceiling"` is supplied as corpus.
4. Add a direct regression in `Travel Agent/tests/concierge/test_privacy_redactor.py` or a handler-level test in the planning tool tests.

Suggested fix direction:

At the proposal boundary, load a trip-scoped private corpus for all members, or run the same constraint-topic detector used by `compose_group_message` against all trip constraints. Also expand budget phrase coverage for `"$50 ceiling"`, `"50 ceiling"`, `"price cap"`, and similar realistic budget-pressure phrasings.

Related bug class:

private-data leak / cross-user corpus gap / group-visible proposal copy

Confidence: High

### P2 — Raw Invite Intake Is Stored In Trip Events After Accept

Status: Confirmed  
User impact: Invitees are told their private intake stays between them and the concierge, but accept-time audit events duplicate the raw `pending_intake` payload into the append-only `trip_events` journal. This is not currently rendered in organizer invite rows, but it is an internal event/log leak and a future feed/digest footgun.  
Product promise affected: privacy / invite intake / logs and events redaction

References:

- `Travel App/app/invite/[slug].tsx:233` — invite UI says the group will not see answers and the concierge uses them to shape the plan.
- `Travel App/app/invite/[slug].tsx:255` — free-text placeholder invites sensitive budget, pace, food, and accessibility input.
- `Travel App/app/invite/[slug].tsx:300` — CTA copy says private signal stays between the user and concierge.
- `Travel Agent/backend/api/routes/invites.py:752` — pre-auth intake event stores only a digest.
- `Travel Agent/backend/api/routes/invites.py:759` — comment explicitly says raw chip/free-text should not live in the append-only journal.
- `Travel Agent/backend/api/routes/invites.py:1013` — accept-time `invite.consumed` event is appended.
- `Travel Agent/backend/api/routes/invites.py:1021` — raw `pending_intake` is stored in that event payload.
- `Travel Agent/tests/api/test_invites_api.py:718` — existing test asserts the raw pending intake is present.
- `Travel Agent/backend/core/db/trip_invites.py:524` — concierge later reads raw intake back out of `trip_events`.

Why it matters:

The code has a safer owner-scoped store already: `trip_invites.pending_intake`. Duplicating raw private free text into `trip_events` creates a broader internal data surface and contradicts the digest-only treatment added for `invite.intake_received`. A future Home, digest, admin, or analytics reader of `trip_events` can accidentally expose the private phrase.

Repro or deterministic test idea:

1. Submit invite intake with `free_text="I am worried about costs and need a low-key pace because of my knee."`
2. Accept the invite.
3. Expected: `invite.consumed` event payload contains only an intake pointer or digest, not raw `chip_answer` / `free_text`.
4. Current: handler and existing test store/assert raw `pending_intake`.

Suggested fix direction:

Keep raw intake in `trip_invites.pending_intake` until the concierge consumes it, and have `invite.consumed` store only a digest plus a reference. Update `get_unsurfaced_pending_intake` to read from the invite row or a scoped private table rather than the general trip event payload.

Related bug class:

private-data leak / event-log redaction gap / invite intake trust loop

Confidence: High

### P2 — Group Synthesis Treats Missing Privacy Rows As Shareable For Narrative Context

Status: Suspected  
User impact: A traveler who never opens the privacy settings can have Personal Memory narrative and structured constraints included in group synthesis inputs, even though invite and product copy frame private facts as private unless explicitly shareable. This increases the chance that group-level text, proposals, or chat composition inherit sensitive phrasing.  
Product promise affected: privacy tiers / group profile synthesis / private constraints

References:

- `Travel Agent/backend/core/privacy_catalog.py:15` — defaults include `budget`, `energy`, and `social` as private, but `dietary` and `interests` as shareable.
- `Travel Agent/backend/core/privacy_catalog.py:66` — group synthesis omission only triggers on explicitly stored private rows.
- `Travel Agent/backend/core/privacy_catalog.py:90` — doc says a user who has not interacted with privacy screen has not opted in/out.
- `Travel Agent/backend/preference_engine/synthesis/group_synthesizer.py:98` — loads stored privacy rows only.
- `Travel Agent/backend/preference_engine/synthesis/group_synthesizer.py:124` — constraint blocking checks only `prefs_map.get(dim) == "private"`.
- `Travel Agent/backend/preference_engine/synthesis/group_synthesizer.py:187` — full Personal Memory markdown is passed into group synthesis when no explicit private row exists.
- `Travel Agent/backend/preference_engine/synthesis/group_synthesizer.py:189` — structured constraints are appended into synthesis input.
- `Travel Agent/backend/concierge/group_compose.py:703` — group composer also receives aggregated hard constraints.

Why it matters:

This may be a deliberate product tradeoff to avoid empty group profiles, but it is not aligned with the audit prompt's invariant: privacy tiers should be explicit at every write path, not inferred later. Invite intake is especially risky because the user has not yet had an authenticated privacy-settings moment.

Repro or deterministic test idea:

1. Unit-test `generate_group_profile` with captured LLM input: one member has Personal Memory containing `"I can only do $50 dinners because money is tight"` and no stored privacy rows.
2. Expected for dogfood privacy promise: budget/private phrase is withheld or transformed before group synthesis input.
3. Current likely: full `memory.markdown_content` reaches the group synthesis LLM input.

Suggested fix direction:

Separate "usable internally" from "shareable into group synthesis" with explicit source tags. At minimum, do not treat missing privacy rows as shareable for budget, medical, accessibility, family/social conflict, or invite free text. Add per-dimension redaction before group synthesis rather than all-or-nothing narrative omission.

Related bug class:

ambiguous privacy semantics / default consent mismatch / synthesis input leak

Confidence: Medium

### P2 — Privacy Audit Omits Preference/Memory/Private-Intake Use

Status: Confirmed  
User impact: The app can say "a log of how your data has been used," but current audit events only cover voice/location/narration signals. A dogfood tester who shared budget, accessibility, dietary, or social constraints cannot see when those facts shaped a group proposal or plan.  
Product promise affected: privacy audit honesty / concierge trust

References:

- `docs/reliability/traces/private-input-to-group-safe-context.md:13` — trace expects privacy audit to record relevant context use.
- `Travel Agent/backend/api/routes/privacy_audit.py:1` — endpoint is scoped to mic/location style signal use.
- `Travel Agent/backend/api/routes/privacy_audit.py:70` — event kind enum has only geofence, narration, voice, and location chat kinds.
- `Travel Agent/backend/api/routes/privacy_audit.py:124` — implementation merges narration interactions and privacy sensor events only.
- `Travel App/app/(tabs)/me/privacy-audit.tsx:80` — screen copy says it logs how user data was used in the last day.
- `Travel App/constants/mocks/privacy.ts:15` — mock audit examples contain only voice/location/narration events.

Why it matters:

For this area, the highest-risk data is not just sensors; it is private preference and constraint use. The audit surface is honest for location/voice but incomplete for the product promise users are being asked to trust during invite intake and group planning.

Repro or deterministic test idea:

1. Create a proposal or group compose path using a private budget/accessibility phrase through fakes.
2. Expected: the owning user sees a privacy audit event such as `private_constraint_used_for_group_plan` with a non-revealing reason.
3. Current: schema has no such event kind, and the endpoint cannot return it.

Suggested fix direction:

Add redacted context-use events for private intake, Personal Memory, and hard constraints. Keep owner-only audit details non-attributive when third-party facts are involved, e.g. "A private constraint was used to avoid an incompatible dinner" without naming another traveler.

Related bug class:

privacy transparency gap / missing audit event taxonomy

Confidence: High

### P3 — Debug Logging Can Echo Raw Tool Inputs

Status: Confirmed  
User impact: In development or server logs, private facts passed to memory/proposal tools can be logged raw or near-raw. This is less directly group-facing but undermines the "logs, events, analytics, and debug traces are redacted" requirement.  
Product promise affected: logs/debug trace redaction

References:

- `Travel Agent/backend/concierge/agent.py:838` — logs every concierge tool call.
- `Travel Agent/backend/concierge/agent.py:841` — dumps `json.dumps(block.input)[:200]`, enough to include private values in `memory_constraint_set`, proposal descriptions, or compose intents.
- `Travel App/utils/observability.ts:105` — dev `reportError` logs raw error context before remote scrubbing.
- `Travel App/utils/observability.ts:110` — remote Sentry context is scrubbed, so the main residual issue is local/dev console logging.

Why it matters:

The remote observability path is thoughtfully gated and scrubbed, but the local/server logging path can still capture the sensitive phrases this audit is trying to protect. Dogfood sessions are exactly when engineers are likely to inspect logs.

Repro or deterministic test idea:

1. Run a fake concierge tool call with `memory_constraint_set` input value `"panic attacks in crowds"`.
2. Expected: log line includes tool name and redacted field names only.
3. Current likely: first 200 chars of raw tool input include the phrase.

Suggested fix direction:

Introduce a shared tool-input redactor keyed by tool name and sensitive fields (`value`, `description`, `impact_analysis`, `free_text`, `intent`, `must_avoid`). Keep counts/types for debugging, not raw private text.

Related bug class:

debug-log PII / sensitive trace leakage

Confidence: High

## Non-Findings / Things Ruled Out

- Strict group compose is enabled by default (`Travel Agent/backend/concierge/config.py:31`) and group replies with trips must route through `compose_group_message`.
- Group compose rejects member names in intents and outputs (`Travel Agent/backend/concierge/group_compose.py:824`, `Travel Agent/backend/concierge/group_compose.py:938`).
- Group compose rejects constraint-topic vocabulary in intents and outputs when a matching hard constraint exists (`Travel Agent/backend/concierge/group_compose.py:857`, `Travel Agent/backend/concierge/group_compose.py:966`).
- Organizer-facing invite lists and Trip Info rows render `Answered privately`, not raw invite intake (`Travel Agent/backend/core/models/trip_invites.py:206`, `Travel App/app/trip-info/index.tsx:421`).
- Privacy audit endpoint enforces self-access only (`Travel Agent/backend/api/routes/privacy_audit.py:119`).
- Frontend remote observability requires explicit consent and scrubs obvious PII keys before sending to Sentry (`Travel App/utils/observability.ts:72`, `Travel App/utils/observability.ts:82`).

## Suggested Follow-Up Checks

- Add a handler-level proposal privacy regression for another member's phrase: `"Dev's $50 ceiling rules out Belcanto."`
- Add an invite accept regression asserting `invite.consumed` stores only digest/pointer metadata, not `pending_intake.free_text`.
- Add group synthesis input-capture tests for no-privacy-row users with realistic private phrases: budget pressure, medical limitation, accessibility need, family/social conflict, dietary constraint, and pace/fatigue.
- Add privacy-audit tests for owner-only private-context-use events that do not expose third-party facts.
- Add a log-redaction unit test around the concierge tool-call logger or a shared `redact_tool_input_for_log()` helper.
