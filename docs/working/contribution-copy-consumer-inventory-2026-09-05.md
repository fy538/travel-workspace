---
doc_type: working
status: active
owner: strategy integration / contribution and consequence
created: 2026-09-05
last_verified: 2026-09-05
expires: 2026-10-05
why_new: Records every source or derivative copy that can outlive a Bring/Ask gesture before lifecycle cleanup changes are made.
source_of_truth_for:
  - contribution source and derivative copy/consumer inventory
depends_on:
  - contribution-contract-and-legacy-memory-migration-plan-2026-08-29.md
  - ../systems/contribution-and-consequence.md
  - ../../travel-agent/backend/inbound/FEATURE.md
---

# Contribution copy / consumer inventory

This inventory separates custody of the thing a person gave Vesper from the
derived records that may help Vesper answer or organize it. It is an evidence
map, not authorization to delete historical data. The unresolved product
decision is ordinary conversation history versus source-retention history;
until that is settled, cleanup must not silently erase a user's transcript or
pretend that a generated answer can recreate a released original.

| Copy / consumer | Current owner and location | Purpose | Current lifetime / read rule | Required lifecycle decision |
| --- | --- | --- | --- | --- |
| Original upload / inline source | `intake_source_objects.storage_ref`, owned by Intake v2 | Re-open the exact private thing that crossed Bring/share | Verified custody, explicit `retention_mode`, `retention_expires_at`; expiry/delete workers revoke bytes and emit outbox events | Keep the deadline from admission; never extend it when semantic work finishes (implemented in `ff3915b6b`). |
| Normalized text/image representation | `intake_processing_runs.output`, `workers/intake_v2_jobs.py` | Deterministic normalization input for semantic interpretation | Replayable processing receipt; source-local and owner-scoped | Decide whether normalized text is retained with derived history or purged with original bytes; it must not restore released source content invisibly. |
| Audio transcript / future decoder output | Adapter output under the Intake processing run | Make audio usable without granting the transcript more authority than the recording | Audio currently stops at truthful `needs_review`; no semantic claim is admitted from an unsupported representation | Add only with a decoder, source hash, expiry, and native evidence; do not route raw audio metadata to semantic interpretation. |
| Semantic observations and candidates | `intake_observations`, `intake_artifact_candidates` | Quarantined, source-bound interpretation and owner review | Derived rows retain evidence locators and source IDs; candidate confirmation/correction is owner-scoped | Preserve lineage and correction; an unconfirmed candidate cannot become a canonical Place, Plan, Occasion, memory, or vector. |
| Consequence proposals / handoffs | `intake_consequence_proposals`, `intake_consequence_handoffs`, `agent_workflows` | Content-free queue into a domain owner after explicit activation | Proposal and handoff readback are owner-scoped; revocation cancels live work | Keep the owner receipt as the causal repair root; no proposal may copy source bytes into a domain writer. |
| Pending Chat payload | `pending_chat_turns.payload` and pending-turn images | Bridge an admitted source into one Chat gesture before canonical message persistence | Device-scoped, stateful outbox; accepted/cancelled/expired states are reconciled before retry | Persist authored note and source refs separately; a retry reuses the gesture identity, while a later Ask gets a new identity (implemented in `9f00c92ce` and `3ff5dac62`). |
| Canonical flattened user message | `messages.content` plus `messages.metadata_.turn_metadata` | Ordinary conversation history and model input | Conversation history policy, not Intake custody, currently governs it | Decide whether source-derived flattened text remains readable after original release; if retained, label source unavailability honestly and never treat it as a live source. |
| Canonical Chat image copy | `chat_images` row plus `CHAT_IMAGE_STORAGE_DIR` filesystem | Multi-turn vision history and future “what I asked” readback | Current module explicitly defers cleanup, expiry, and per-user budgets | Attach a declared owner/expiry to the copy or make the image a source reference. This is the main unclosed lifecycle gap; do not claim Ask expiry is complete until resolved. |
| Generated agent answer | Agent `messages` row / response history | Value delivered for the immediate Ask | Conversation history policy; no raw source bytes should be embedded as a hidden retention exemption | Keep answer readable as an answer, but mark missing source/expired evidence where later re-read would otherwise imply availability. |
| Observations, profile, vectors, and Home/Places projections | Existing observation/profile/vector/projection owners | Later personalization and useful selection | Each owner has its own correction/read path; derived writers now mark non-authoritative provenance | Maintain source lineage and invalidation. Independent user-authored evidence survives release of an unrelated source; dependent projections must be withdrawn. |
| Lifecycle/outbox/audit events | Intake outbox and processing-run receipts | Reconciliation, monitoring, and causal repair | Durable metadata without source payload | Retain enough identifiers and status to explain what happened; never use an audit event as permission to resurrect source content. |

## Required next implementation decision

Before changing `backend/core/db/chat_images.py`, settle one narrow rule:

> Does ordinary Chat history retain an image attachment after an Ask source
> expires, or is the attachment a processing copy that expires with the
> source?

The recommended default is to treat an image attached through a deliberate
Ask/Bring as a processing copy unless the user explicitly keeps it in the
source lane. The message and answer may remain under conversation history, but
image readback must return an honest “original unavailable” state after the
copy's deadline. Implement that policy with a small owner/expiry field and a
cleanup worker only after the founder chooses the history rule; do not perform
a broad historical purge or a dual-write migration.

## Evidence already landed

- `e0885b98d` makes Life retained-source counts bounded and source-local.
- `9f00c92ce` preserves server-owned authored authority across Chat retry and
  rejects forged metadata on both Chat request models.
- `ff3915b6b` preserves original transient custody deadlines through semantic
  completion.
- `add16495d` labels behavioral and engagement observations as reversible,
  non-authoritative derived signals.
- The owner/activation portfolio currently passes 44 focused tests.

The unresolved Chat-image policy is therefore a deliberate boundary, not an
accidental omission. It is the next CC-2 decision before claiming complete
source/derivative lifecycle conformance.
