---
doc_type: working
status: active
owner: founder / product / engineering
created: 2026-08-22
updated: 2026-08-22
last_verified: 2026-08-22
expires: 2026-09-21
why_new: Record the bounded integration state for addressed place relationships, shared occasions, and existing app surfaces.
source_of_truth_for: [multiplayer-place-relationship-integration]
---

# Multiplayer × place relationship integration

## Decision

The first differentiated multiplayer verb is an addressed place handoff: one
person leaves a source-bound observation for another person without requiring
a durable circle. The recipient can keep it or open a shared Occasion. The
shared Occasion is a relationship consequence, not a second trip planner.

This keeps the product thesis intact: a place can become part of a relationship
between people, while Chat remains the low-friction entry surface and existing
Home, Places, and Plan surfaces remain the readback surfaces.

## Verified implementation

- UUID handoffs accept an existing recipient, pair conversation, or circle
  authority; no durable circle is fabricated for a one-to-one handoff.
- Handoff cards compile sender and canonical place labels at creation time.
  Source lines distinguish a private artifact, saved place moment, or personal
  observation without embedding source IDs or private payload references.
- `open_together` creates one shared overlap Occasion with both participants,
  stores the handoff-to-occasion binding idempotently, and returns
  `occasion_id` to the mobile client.
- Occasion graph projections preserve the reviewed `world_entity_id`, allowing
  future Places/Plans readers to join by canonical identity instead of slug or
  message text.
- The mobile card shows a settled receipt, invalidates existing Home and graph
  readers, and publishes the existing private consequence banner to Trips Home,
  Places, Plan, and Vesper Home. No new tab or public feed is introduced.
- Card metadata is validated before opening a database transaction, so malformed
  composed cards fail closed without a write attempt.

## Evidence

Focused backend evidence: relationship routes, graph projection/commands,
occasion schema/migration, composed-card validation — 87 tests passed on
2026-08-22; the broader portfolio reached 109 passing tests before an existing
baseline card-validation defect was fixed. The corrected portfolio is green.

Focused mobile evidence: ComposedChatCard, experience-graph selector, and
relationship mock handoff suites — 15 tests passed; TypeScript passed. The
workspace contract check passes with the generated `ProjectedOccasion` field.

No production/cloud/Qdrant promotion was performed by this slice.

## Remaining integration work

1. Mount the graph projection in one existing Home/Places/Plan composition and
   render only source-bound openings or shared place occasions; do not add a
   standalone social feed.
2. Add a viewer-scoped place reader that resolves the UUID to the existing
   place presentation model before rendering a relationship line.
3. Add plural outcome capture after an Occasion is lived; keep outcomes
   private-by-default and independently correctable.
4. Bridge mature Trip proposals/votes only when a handoff is explicitly attached
   to a Trip; never infer Trip membership from a shared place.
5. Run the two-account device walk and record real receipts separately from
   automated evidence. The feature flags remain the release boundary.

## Negative oracles

- A recipient action never exposes another user’s artifact ID, payload, or
  private memory.
- A handoff never creates a social circle as a side effect.
- A shared Occasion never becomes a booking, itinerary mutation, or public post
  without an explicit later command.
- A missing/expired/revoked handoff action remains retryable or unavailable as
  appropriate; it never falls back to a generic route.
- Public or non-participant readers receive no handoff content.
