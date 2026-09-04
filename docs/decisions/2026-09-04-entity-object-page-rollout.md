---
doc_type: decision
status: accepted
owner: founder / product / design / engineering
created: 2026-09-04
decided: 2026-09-04
why_new: Turns the existing entity-object-page work into a release program with explicit authority, freshness, and rollout boundaries.
supersedes: []
source_of_truth_for: [entity-object-page-rollout]
---

# Entity object page rollout

## Decision

The object page is a durable identity and relationship surface. It is not a
second place database, a navigation product, or a synchronous research view.

The first production family is venue, site, and experience. Accommodation
keeps its booking/commitment-oriented screen until its lifecycle is separately
approved.

The ordinary object verbs are:

- **Keep** — the viewer's reversible relationship, owned by saves.
- **Ask Vesper** — a private Chat handoff carrying the canonical entity and
  return context.
- **Leave for someone** — an addressed relationship action requiring an
  explicit recipient, preview, owner confirmation/readback, receipt, and
  revocation path.
- **Tonight?** — shown only when an Occasion is live and owned by the
  Occasion/Plan flow.

There is no generic **Add to trip** action on a cold object page. A Plan or
Occasion surface may open the same entity with its own explicit context and
owner controls; the object page does not grow a second trip/day picker.

## Data boundaries

The durable page reads canonical identity, curated facts, relationship state,
and already-completed research. It never performs provider I/O or prose
generation on the read path. Missing evidence remains absent or a typed
unknown.

Google and other providers may supply volatile status, routing, attribution,
and permitted media through explicit, budgeted checks. Provider identifiers
are retained only as provenance and resolution aids; they do not become a
global Vesper entity corpus.

Research begins as an explicit, idempotent **Read up** request. Automatic
page-open enqueue is deferred until cost, usefulness, source retention, and
cache behavior have been measured.

No broad entity or provider backfill is part of this rollout. Lazy,
owner-private provisional shells remain the only materialization path until a
separate seed-and-dedupe decision is made.

## Release gates

Production enablement requires:

1. Native QA coverage for rich, sparse, provisional, redirected, no-media,
   and failure states.
2. Situation reads that are explicitly scoped to a Plan or a user location
   gesture, with expiry and no precise coordinates in navigation or logs.
3. Canonical action dispatch with owner readback, idempotency, and dependent
   cache invalidation.
4. If Leave remains visible, the addressed handoff flow and two-user privacy
   certification.
5. Merge, correction, revocation, expiry, and source-retraction checks across
   Places, Chat, Plan, Life, and the Experience Graph.

Operational status, generalized media, and research enrichment may follow
the durable page launch; they must degrade to an honest sparse page.

## Non-goals

- competing with Google Maps' global catalog or navigation surface;
- universal opening-hours, review, pricing, or booking coverage;
- model-generated judgments from provider facts;
- automatic GPS-derived attendance or affection;
- public sharing of owner-private provisional shells;
- replacing the owner of Saves, Plans, Occasions, Chat, Outcomes, or Graph.

