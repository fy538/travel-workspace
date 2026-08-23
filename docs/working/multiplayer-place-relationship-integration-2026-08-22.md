---
doc_type: working
status: active
owner: founder / product / engineering
created: 2026-08-22
updated: 2026-08-23
last_verified: 2026-08-23
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

## M3 closure update — 2026-08-23

The bounded loop is now exercised end to end in code and mock read-after-write:
the recipient's `open_together` action produces a viewer-relative Occasion,
each participant can retain a separate private encounter Outcome, and the
owner can correct that Outcome with an expected revision. Mobile now mounts the
sender's pair-circle handoff action on graph summaries and a recipient private
Outcome composer/correction action. It exposes the canonical entity route
handoff through the existing exhaustive entity router.
The backend regression explicitly proves that this opening does not create a
Trip link. See the [M3 multiplayer loop receipt](m3-multiplayer-loop-2026-08-23.md)
for commit-level evidence and the release boundary.

## Evidence

Focused backend evidence: relationship routes, graph projection/commands,
occasion schema/migration, composed-card validation — 110 tests passed on
2026-08-22, including the early metadata-validation regression fixed in this
slice. The corrected portfolio is green.

Focused mobile evidence: ComposedChatCard, experience-graph selector/action,
summary-card, and relationship mock handoff suites — 17 tests passed;
ESLint and TypeScript passed. The relationship mock suite includes an explicit
two-person privacy/correction certification. Maestro syntax passed, but no
M3-specific device flow or screenshot receipt was produced.

No production/cloud/Qdrant promotion was performed by this slice.

## Surface wiring audit — 2026-08-22

- Trips Home and Places already mount the shared viewer-relative graph
  projection through `useExperienceGraphContext("my")` and render the same
  `ExperienceGraphSummaryCard` handoff. No second social feed was introduced.
- The legacy trip Plan route is intentionally not another graph owner. Its
  existing Trip/itinerary contract remains authoritative for itinerary edits;
  mounting a second graph card there would duplicate state until a canonical
  Plan reader is ready.
- Outcome capture is available as a typed mobile action facade and the backend
  exposes private-by-default encounter-outcome commands. The mock now reads
  back multiple participant-owned outcomes and revision corrections. The
  recipient composer and correction action are mounted on lived Occasion and
  Outcome summaries; a real device proof remains unimplemented.
- The projection correctly carries `world_entity_id`, but the mobile Places
  model still uses legacy numeric venue/place IDs. A UUID-to-canonical-place
  reader is therefore still an explicit integration seam, not something the
  client should infer by slug or message text.

## Remaining integration work

1. Carry the graph world UUID into canonical Place detail so the sender action
   is not limited to graph summaries.
2. Run a dedicated two-account device walk for this UUID handoff surface and
   record real receipts separately from automated evidence.
3. Bridge mature Trip proposals/votes only when a handoff is explicitly
   attached to a Trip; never infer Trip membership from a shared place.
4. Keep the feature flags as the release boundary; use only the checked-in
   local/demo launcher for development validation.

## Negative oracles

- A recipient action never exposes another user’s artifact ID, payload, or
  private memory.
- A handoff never creates a social circle as a side effect.
- A shared Occasion never becomes a booking, itinerary mutation, or public post
  without an explicit later command.
- A missing/expired/revoked handoff action remains retryable or unavailable as
  appropriate; it never falls back to a generic route.
- Public or non-participant readers receive no handoff content.
