---
doc_type: working
status: active
owner: founder / design
created: 2026-07-17
expires: 2026-08-16
why_new: Provides the bounded Claude Design execution prompts for the first Vesper 235 parity round without overloading the investigation or ledger.
supersedes: []
source_of_truth_for: [vesper-235-round-1-claude-design-prompts]
---

# Claude Design — Round 1 Prompts

Run these prompts sequentially in the same design project. After all three are complete, stop and return the revised design for validation. Do not silently expand into later itinerary, Chat, Atlas, route-governance, or implementation work.

## Prompt 1 — booking cancellation and Costs truth

Work inside the existing Booking, Stay, Costs, State System, and notification/receipt canvases. Preserve their current visual language, typography, spacing, surfaces, and canonical components. Do not alter the Trip header, navigation shell, itinerary spine, or unrelated product canvases.

Create exactly one new canvas adjacent to the existing Booking and Costs canon named **Booking Cancellation Truth**. A new canvas is warranted here because this is a missing cross-surface lifecycle connecting Booking, notification receipts, expense review, and settlement. Do not create separate canvases for each state. Update existing Booking or Costs boards only where a current specimen would otherwise contradict the new lifecycle.

Design the complete user-facing cancellation journey. Distinguish a cancellation request from a confirmed provider outcome. Cover: request submitted; processing or refreshing; still pending verification; cancelled; not cancelled; manual action required; retry when retry is safe; and the blocked state that prevents a duplicate cancellation request. Internal provider vocabulary may appear in the annotation matrix, but user-facing specimens must use calm, precise language and must never imply success before it is confirmed.

Add the completion receipt for all terminal outcomes: cancelled, not cancelled, and escalated/manual action required. The receipt must remain replay-safe and factual. Show who controlled the provider action, when the result was last checked, what changed, what did not change, and the single valid next action. Decide explicitly whether the existing generic notification card is the canonical receipt container or whether it needs a money-specific variant; prefer extending the existing canonical container unless its anatomy cannot express the truth.

Connect a confirmed cancellation to Costs. Show the **BOOKING CANCELLED · REVIEW COST** posture, with settlement paused only for the affected expense while review is active. Cover who can open review, who can withdraw it, payer or organizer resolution, and the requirement to void a live recorded payment before review can proceed. Also add compact supporting states for visible recorded and voided payments, settlement currency truth, estimated-rate labeling, masked-expense visibility, immutable split type during edit, and archived-trip behavior. These should extend the existing Costs system, not become a second Costs redesign.

Use existing Button/VBtn variants, StatusPill, CardSurface, InlineAbsence, ActionFailureInline, WorkerProgress, sheets, and receipt primitives. Do not draw local pills or bespoke buttons. Add a component only if the existing primitives genuinely cannot express a required state, and document that exception beside the component. Include annotations for controller versus viewer actions, uncertain versus terminal states, exact navigation into Costs review, recovery, Dynamic Type, VoiceOver reading order, minimum target size, and reduced motion.

End the canvas with a compact state-and-transition matrix mapping every designed specimen to: actor, visible truth, allowed action, blocked action, receipt, Costs consequence, and recovery. Mark unresolved implementation questions as **CODE AUDIT REQUIRED** rather than guessing.

## Prompt 2 — public projection and sharing privacy

Work primarily in the existing **External Sharing** canon and reuse the existing share-card, public landing, Story, Invite, Proposal, and Unpacked specimens. Do not redesign the app header, Trip header, share controls, or general visual style.

Create exactly one new canvas adjacent to External Sharing named **Public Projection Contract**. This canvas is justified because one shared privacy and redaction contract must govern four runtime projection types. Do not create four independent canvases. Update any existing External Sharing doctrine that contradicts the ruling below.

Make this canonical privacy ruling explicit: a public or unauthenticated proposal surface must not expose vote counts, individual votes, group-decision progress, or a status derived from those votes. Group decision detail belongs behind authenticated access. If a proposal can be shared publicly, its public projection may contain only stable trip/proposal context that the sharing actor is permitted to disclose, a neutral description of the proposed change, brand attribution, and an **Open in Vesper** authentication handoff. It must not imply approved, rejected, winning, losing, or waiting-for-N-votes. If the existing system cannot satisfy that rule, mark public proposal sharing unsupported until the code is gated or redacted.

Define one exact projection/redaction matrix for the four 9:16 public card types: Story, Invite, Proposal, and Unpacked. For each, list allowed fields, prohibited fields, actor-controlled fields, authentication requirement, expiry behavior, stale-data behavior, takedown/revocation behavior, and the destination after opening. Show representative cards and public landing states, but keep the matrix as the source of truth. Reuse the established 1080×1920 card grammar rather than inventing another share-card family.

Include loading, unavailable, expired where that object legitimately supports expiry, revoked, removed, authentication-required, and safe fallback states. Do not use an itinerary-operation `expired` state unless that state genuinely exists for that object family; booking proposal expiry is a separate domain. Make cache/staleness language truthful without asserting a deployment or cache policy that the design cannot verify.

Use only existing canonical buttons, cards, status labels, and authentication handoff patterns. No bespoke share buttons or local status chips. Add privacy annotations for public versus authenticated viewers, organizer versus recipient, and what must never appear in generated image alt text or metadata. End with a decision block stating which public projections are supported, gated, authenticated-only, or unsupported, and label implementation-dependent rows **CODE AUDIT REQUIRED**.

## Prompt 3 — participant consent and booking control

Work inside the existing Booking, Stay decision, traveler-selection, Trust & Controls, and receipt canvases. Reuse their established component system and visual hierarchy. Do not touch the Trip header, itinerary layout, navigation shell, or the cancellation canvas except to reference its canonical receipt and controller language.

Create exactly one new canvas adjacent to the existing Booking decision work named **Booking Consent & Control**. This is a missing role-and-lifecycle contract, so a dedicated canvas is appropriate. Keep all consent states, controller/viewer variants, and confirmation rules on this one canvas. Update existing approval specimens only when they conflict with this canonical ledger.

Design a participant-level consent ledger with the exact states **Pending**, **Approved**, **Declined**, and **Excluded**. Show mixed group states, the summary state for the booking, and the rule that final confirmation is blocked while required consent is unresolved. Design the declined path, including a clear **Narrow to myself** recovery when it is valid. Show reminder behavior with a four-hour cooldown: available, sent, cooling down, and available again. The design must identify who can remind whom and must not turn reminder cooldown into a fake progress indicator.

Define booking control separately from consent. The booking controller owns provider mutations; other travelers may inspect plan and status but see controller attribution and view-only explanations wherever an action is unavailable to them. Produce paired controller/viewer specimens for provider-action moments and their resulting receipts. Do not mechanically duplicate every receipt—create variants only where action ownership or available recovery actually differs.

Cover loading, partially known roster, traveler removed, controller unavailable, consent changed while confirming, provider action already in progress, and terminal receipt states. Connect organizer authority, booking controller authority, affected-participant consent, and ordinary viewer access in one compact role matrix. Where controller transfer or trip departure changes the answer, reference the existing Organizer Handoff pattern and mark the deeper succession behavior for a later authority pass; do not redesign succession in this round.

Reuse TravelerPicker, Button/VBtn, InlineChip, StatusPill, CardSurface, WorkerProgress, InlineAbsence, ActionFailureInline, sheets, and canonical receipt patterns. Do not spawn a new traveler picker, approval chip, or action-control family. Include Dynamic Type, VoiceOver labels and order, focus after state changes, minimum target size, reduced motion, and exact-return annotations.

End with two matrices: participant state × allowed action, and role × provider capability. Every rendered specimen must map to both. Mark unverified implementation details **CODE AUDIT REQUIRED** and stop after completing this canvas and any necessary corrections to contradictory existing specimens.
