---
doc_type: decision
status: accepted
owner: founder / engineering
created: 2026-08-11
decided: 2026-08-11
why_new: Record why the entity-status block was shipped despite near-zero production coverage, and name the two structural gaps that cause the coverage — a decision that governs how to read the field until the gaps close.
supersedes: []
source_of_truth_for: [entity-status-block, place-truth-write-coverage]
---

# Ship the entity status block as correct plumbing over an unwired pipe

## Context

[2026-08-11-entity-and-place-two-axes](./2026-08-11-entity-and-place-two-axes.md)
identified that no entity detail endpoint exposes the place-truth substrate's
adjudicated operating status (`entity_fact_claims` → `entity_fact_resolutions`
→ `place_projections`) — the system can determine a venue is permanently
closed, with source-weighted confidence, and no page can say so. The one
app-side copy that existed, `'Reported permanently closed'` in
`components/places/core/PlacesCore.tsx`, had zero code importers.

Before building the fix, coverage was measured directly against the database
rather than assumed:

```
place_projections by entity_type:  venue  1     (of 1030 venues, 116 sites, 47 accommodations, 57 experiences)
entity_fact_resolutions field='operating_status':  0 rows, anywhere
entity_fact_resolutions field='open_now':  0 rows, anywhere
```

That single row was not organic traffic — `values: {}`, `claim_ids:
{'regular_hours': None}` — adjudication resolved nothing. It is a fixture
from `feat(foundry): persist accepted place evidence` (2026-08-08).

Tracing the write path found the coverage isn't a sweep-in-progress, it is
**structurally near-zero from two independent causes**:

1. **No trigger.** `enqueue_place_refresh` — the only function that would
   ever queue a provider check producing `open_now`/`operating_status`/
   `regular_hours` claims — has zero callers anywhere in the codebase. The
   handler is registered on the event bus, but nothing publishes the event
   that fires it.
2. **Venue-only, even if triggered.** `places/refresh_queue.py` hard-codes
   `entity_ref.type != "venue"` as a raised `ValueError` in two places. Sites,
   accommodations, and experiences cannot get a claim from this producer
   regardless of the trigger gap. A World Foundry promotion could still
   populate any entity type — that path is generic — but none has targeted a
   non-venue entity yet.

## Decision

**Ship the status block anyway, on all four catalog detail endpoints, as
correct plumbing over a pipe with (currently) nothing flowing through it —
not as a fabricated fact over a working one.**

The distinguishing test: every field is honestly `null`/`"unknown"` when no
claim has been adjudicated, never guessed. `get_entity_status` never raises
and never omits the block — an entity with no projection at all gets the
all-unknown response, which makes the absence visible in the wire contract
rather than silently missing.

This is a deliberate bet that plumbing correctness and data-source
population are separable concerns, and that shipping the read side first
makes the write-side gap a visible, assignable problem instead of an
invisible one. It is explicitly **not** a claim that coverage is adequate
today.

### Why not build the trigger first

Considered and rejected as the immediate next step. Wiring
`enqueue_place_refresh` to a real event is separate, larger, product-scoped
work: which event should fire a refresh (entity viewed? saved? planned?),
what cadence and priority tiers, and — because it calls Google/Foursquare —
real provider cost and rate-limit exposure. None of that is a read-endpoint
decision, and blocking the read side on it would leave the substrate
unconsumed indefinitely, repeating the same built-and-unconsumed pattern
this work exists to close.

### Field naming exception

`experiences.py`'s `ExperienceResponse` already has a `status: str` field
(the row's lifecycle — "active"/etc.), so the block is named
`entity_status` there instead of `status`. Populated only on the
single-entity detail path, never on search results — each lookup is its own
DB round trip, and computing it per row in a list would be an N+1 query.

### Privacy

Verified, not assumed: `place_projections`' read path
(`_load_claims`) filters `entity_fact_claims.scope == "global"` explicitly,
so an owner-scoped private claim can never be adjudicated into the shared
projection this endpoint reads — the same boundary
[2026-08-08-place-identity-and-provenance](./2026-08-08-place-identity-and-provenance.md)
established. The venue endpoint's public-projection allowlist
(`tests/api/test_public_projection_shapes.py`) was updated consciously: the
block is the same trust category as the existing `hours` field — public
operating logistics, no user-derived state — and `sources` carries provider
names, never a user identifier.

## Non-goals

- **Not** building the refresh trigger. Separate, larger, product-scoped
  work (see above).
- **Not** generalizing `refresh_queue.py` beyond venue. Blocked on the
  trigger decision landing first — no point widening a producer nothing
  calls.
- **Not** exposing per-field confidence on the wire. `PlaceDecisionContext`
  (the existing "safe evidence envelope" Takes already consumes) does not
  carry it, and widening that shared type was out of scope for a read-only
  addition to four endpoints.
- **Not** deciding product behavior for a closed entity (can it still be
  added to a plan? does it disappear from feeds? does an existing itinerary
  block get flagged?). Rendering "permanently closed" is the easy half of
  this problem; this decision does not resolve the other half.

## Consequences

- Four detail endpoints (`venues`, `sites`, `accommodations`, `experiences`)
  carry a `status`/`entity_status` field that is, honestly, `null`/`"unknown"`
  for effectively all production entities today.
- The coverage gap is now a visible, assignable engineering task (wire the
  trigger) rather than an invisible one (nobody reads the table that would
  reveal it's empty).
- Whoever builds the trigger does not also need to build the read side —
  coverage improving is the only thing that changes this field's behavior at
  runtime, not a code change.
