# Plan - Vesper Trust Receipts

> Status: proposal
> Owner: founder / engineering
> Last updated: 2026-06-12
> Source of truth for: the small, concrete alternative to a large knowledge-graph project

## One Sentence

Do not build a grand "knowledge graph" project for dogfood. Build a small,
boring Trust Receipts layer that records why Vesper did something, what sources
it used, what privacy boundary applies, what object changed, and how the user
can correct or undo it.

## Why This Exists

The phrase "knowledge graph" is too large for the current dogfood problem. It
invites ontology work, graph-database questions, and broad world-model language
before the first users can reliably trust the product.

Three partial receipt systems already exist in the codebase: `receipt_composer.py`
writing to `plan_events`, the booking confirmation card in `core/receipts.py`, and
Atlas's `derived_signal → observation` chain. This plan is their unification, not
a new system on top of them. Do not add a fourth siloed ledger.

The real dogfood problem is narrower:

- Why did Vesper show or suggest this?
- Did it use private context safely?
- Did it actually change, book, remember, or notify something?
- Does Home agree with Plan, Map, Chat, Atlas, and Notifications?
- Can the user correct or undo the action?
- Can we revoke memory that came from a deleted source?

A Trust Receipt answers those questions directly.

## Definition

A Trust Receipt is a durable record attached to a meaningful Vesper action:

```text
Vesper suggested / changed / remembered / notified / handed off something
because of these reasons,
using these sources,
within this privacy boundary,
affecting this object,
with this correction or undo path.
```

It is the AI equivalent of a transaction receipt plus an explanation.

## Non-Goals

This is not:

- a graph database migration
- a full ontology
- a global node/edge modeling project
- a replacement for Postgres, Qdrant, or generated API contracts
- a new agent architecture
- a reason to slow down dogfood journey promotion

If this layer grows into a richer graph later, fine. It should earn that shape
from real product pressure.

## Initial Surfaces

Start with only five surfaces.

| Surface | Receipt proves |
| --- | --- |
| Proposal accepted / reverted | What changed, why it changed, which plan object was affected, and how it can be reverted. |
| Home / proactive card | Why the card appeared, what triggered it, whether it was time-sensitive, and what happens if dismissed. |
| Atlas / Travel DNA | Which artifact or user action produced a learned signal, and whether deleting that source revokes the signal. |
| Discover -> Ask / Plan | Why an entity is relevant to this traveler or trip, and whether it is a trip action or only an Ask Vesper seed. |
| Booking / stay / expense | Whether Vesper booked, handed off, confirmed, logged, shared, or merely suggested something. |

## Minimal Schema

Use Postgres. Store source and reason detail as JSONB until repeated patterns
justify stricter tables.

```sql
CREATE TABLE vesper_action_receipts (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  trip_id UUID REFERENCES trips(id),

  surface TEXT NOT NULL,
  action_type TEXT NOT NULL,
  target_type TEXT NOT NULL,
  target_id TEXT NOT NULL,

  public_reasons JSONB NOT NULL DEFAULT '[]'::jsonb,
  private_influences JSONB NOT NULL DEFAULT '[]'::jsonb,
  source_refs JSONB NOT NULL DEFAULT '[]'::jsonb,

  visibility TEXT NOT NULL,
  status TEXT NOT NULL,
  undo_type TEXT,
  undo_ref TEXT,

  -- Traceability: tie receipt to the proactive event or conversation turn that
  -- produced it. correlation_id comes from proactive_events.correlation_id or
  -- the turn's x-idempotency-key header.
  correlation_id TEXT,
  -- Idempotency: callers supply this key; duplicate writes with the same key
  -- return the existing receipt id rather than creating a second active row.
  idempotency_key TEXT UNIQUE,
  -- Supersession: when a proposal is revised or a card is refreshed, point the
  -- old receipt at the new one so the chain is auditable.
  superseded_by UUID REFERENCES vesper_action_receipts(id),

  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX vesper_action_receipts_target_idx
  ON vesper_action_receipts (target_type, target_id);

CREATE INDEX vesper_action_receipts_trip_created_idx
  ON vesper_action_receipts (trip_id, created_at DESC);

CREATE INDEX vesper_action_receipts_user_created_idx
  ON vesper_action_receipts (user_id, created_at DESC);

CREATE INDEX vesper_action_receipts_correlation_idx
  ON vesper_action_receipts (correlation_id)
  WHERE correlation_id IS NOT NULL;
```

Suggested enums:

```text
surface:
  home | chat | atlas | discover | booking | plan | map | notifications

action_type:
  suggest | notify | propose_change | apply_change | revert_change |
  remember | revoke_memory | book_handoff | confirm_booking |
  create_stay | log_expense | dismiss

target_type:
  proposal | card | artifact | observation | itinerary_block |
  booking_session | booking_offer | stay | expense | place | venue |
  experience | conversation | notification

visibility:
  private | group | public | system

status:
  active | superseded | revoked | errored
```

## JSON Shapes

### Public reasons

Public reasons are safe to show to the current channel.

```json
[
  {
    "kind": "plan_context",
    "label": "Near tomorrow's planned walk",
    "source_type": "itinerary_block",
    "source_id": "block_123"
  },
  {
    "kind": "group_fit",
    "label": "Low-effort morning activity",
    "source_type": "trip_brief",
    "source_id": "vision"
  }
]
```

### Private influences

Private influences can affect Vesper's decision, but must not be rendered into a
group or public explanation.

**Invariant:** private influences are never stored raw. The only fields that may
be written are `user_id`, `kind`, and `safe_label`. The actual value — the budget
number, the dietary restriction text, the medical flag — must never appear in this
column. `may_surface` is always false; the field exists only as an explicit
reminder in code review, not as a runtime toggle.

```json
[
  {
    "user_id": "maya",
    "kind": "dietary_constraint",
    "safe_label": "private food constraint",
    "may_surface": false
  }
]
```

The serializer test for this is a hard ratchet: assert that no private-influence
object in a group- or public-channel response contains any field other than
`safe_label`.

### Source refs

Source refs connect the receipt to the evidence or system event that caused it.

```json
[
  {
    "source_type": "atlas_artifact",
    "source_id": "artifact_123",
    "label": "Porto photo memory"
  },
  {
    "source_type": "saved_place",
    "source_id": "venue_456",
    "label": "Saved tile museum"
  }
]
```

## Backend Contract

Create one internal writer helper:

```python
create_action_receipt(
    *,
    user_id: UUID | None,
    trip_id: UUID | None,
    surface: str,
    action_type: str,
    target_type: str,
    target_id: str,
    public_reasons: list[dict],
    private_influences: list[dict] | None = None,
    source_refs: list[dict] | None = None,
    visibility: str = "private",
    status: str = "active",
    undo_type: str | None = None,
    undo_ref: str | None = None,
) -> UUID
```

Create one serializer:

```python
serialize_receipt_for_viewer(
    receipt: ActionReceipt,
    *,
    viewer_user_id: UUID | None,
    channel: Literal["private", "group", "public", "system"],
) -> SerializedActionReceipt
```

The serializer is the trust boundary.

Rules:

- In a private channel, show full reasons for that user.
- In a group channel, show only public reasons.
- Never show another user's private influence.
- In a public channel, show only public/source-safe reasons.
- If the public explanation would be empty, render a safe generic line:
  "Vesper used private trip context without exposing individual details."
- If source_refs include deleted or revoked sources, mark the receipt degraded
  rather than silently pretending the evidence still exists.

## API Shape

Start with two endpoints:

```text
GET /api/receipts?target_type=proposal&target_id=...
GET /api/trips/{trip_id}/receipts/recent
```

Keep this as supporting infrastructure. Do not expose a broad query API until
real product surfaces need it.

## Frontend Contract

Build one reusable component:

```tsx
<VesperReceipt receipt={receipt} mode="compact" />
```

Modes:

```text
compact     Inline "Why this" block for cards and proposal sheets.
detail      Full receipt drawer/sheet for trust-sensitive actions.
source      Atlas-style "Learned from" provenance list.
status      Booking/stay/expense status proof.
```

Examples:

```text
Why Vesper suggested this
- Near tomorrow's planned walk
- Low-effort morning activity
- Fits the group's craft interest
```

```text
Learned from
- Porto photo memory
- Saved tile museum
- Trip story edit
```

```text
Status
- Handoff ready
- No payment made
- Organizer confirmation required
```

## Implementation Order

### 1. Proposal receipts

Normalize existing proposal receipt work first. Every accept, apply, reject, and
revert should write a receipt tied to the proposal and any affected
itinerary_block ids.

Done when:

- proposal detail can load its receipt
- Plan / Home / Chat can render the same receipt
- revert receipts distinguish "actually reverted" from "nothing changed"
- idempotent retries do not create duplicate active receipts

### 2. Atlas provenance

Connect:

```text
atlas_artifact -> atlas_derived_signal -> observation
```

Note: the chain stops at `observation`. The next hop — `observation -> Travel DNA
phrase` — crosses a synthesis boundary where the LLM composes multiple
observations into a single phrase. There is no durable FK from a DNA phrase back
to a specific observation yet. Do not claim this step is done until that FK
exists; absent it, "Learned from" on a DNA phrase is fabricated, not traced.

Concrete done-when:

- artifact → derived_signal → observation FK chain has a cascade-revoke migration
- the Atlas UI shows "Learned from" for observations (not DNA phrases)
- deleting or hiding an artifact marks related derived_signals as revoked and
  degrades any receipt that cites them
- DNA phrase attribution is explicitly deferred until a `sourced_from_observation_id`
  column exists on the phrase record

### 3. Home and proactive cards

Every Home/proactive card should carry a receipt or receipt reference.

Done when:

- a card explains why it appeared
- dismissed / muted / not-now outcomes attach to the same receipt chain
- private triggers never render as group-visible reasons

### 4. Discover to trip action

When Discover seeds Vesper, plans similar, or adds a place to a trip, write a
receipt that distinguishes browsing, asking, and mutating.

Pre-condition: add `sourced_from_angle_id UUID REFERENCES angles(id)` to
itinerary blocks before implementing this surface. The FK is a one-column
migration; without it, Discover → plan receipts have no durable provenance link
and the chain is unverifiable.

Done when:

- "Ask Vesper" does not look like "add to trip"
- plan-similar actions preserve destination identity and source context
- users can see why an entity was relevant

### 5. Booking / stay / expense

Use receipts to make financial and booking state honest.

Done when:

- UI can prove "handoff ready" vs "booked" vs "confirmed"
- no payment or shared expense is implied without an explicit receipt
- organizer/member visibility differences are represented in serialization

## Tests And Ratchets

Add targeted tests before broadening the layer:

- serializer test: private influence never appears in group/public output
- proposal test: accept/revert creates one active receipt under retry
- Atlas test: artifact deletion revokes or degrades derived receipts
- Home card test: card render has at least one public reason or safe fallback
- booking test: no "booked" status without a provider-confirmed receipt
- API auth test: users cannot fetch another trip's private receipts

Later ratchet:

```text
All action_type values in high-trust surfaces must either write a receipt or
explicitly opt out with a code comment and test.
```

## Product Principle

Ask this before adding any "graph" work:

```text
What dogfood bug does this prevent?
```

Good answers:

- prevents private budget/allergy info from leaking into group chat
- prevents Atlas memory from surviving after source deletion
- prevents Home recommending something already rejected in Plan
- prevents Vesper explaining a recommendation with a reason the group should not see
- prevents mock/real drift by making the same action receipt render everywhere

Weak answers:

- makes the system more semantic
- enables future intelligence
- creates a world model
- improves reasoning in principle
- gives us a moat someday

Those may become true later. They are not enough for the next dogfood gate.

## Summary

The product should behave as if it has a trustworthy relationship graph, but the
next implementation step should be smaller: record the reason, source, privacy
boundary, target object, and undo path for each important Vesper action.

Trust Receipts give users and engineers the part of a knowledge graph that
matters now: auditable action.
