---
doc_type: decision
status: accepted
owner: founder / engineering
created: 2026-08-16
decided: 2026-08-16
why_new: Make differentiated place interpretation lossless and expose one evidence-backed relationship projection without creating a universal place or memory table.
supersedes: []
source_of_truth_for: [place-content-primitive-persistence, place-relationship-projection]
---

# Persist place interpretation losslessly and derive relationship state

## Context

The storage-neutral `PlaceContentPrimitive` captures observable target,
authority, conditions, spatial and temporal scope, limits, disagreement,
eligible surfaces and actions, proactivity, privacy, review, and provenance.
Current semantic tables can retain only a subset. Broad content generation
would therefore produce dossiers that cannot be promoted without semantic
loss.

Places also has real evidence for saved, planned, happened, skipped, corrected,
and relationship-scoped outcomes, but each surface currently assembles a
different subset and vocabulary.

## Decision

### Lossless primitive persistence

Promoted place interpretation uses an additive canonical primitive envelope,
owned by `backend/core/models/place_content.py` and
`backend/core/db/place_content.py`. The physical schema will use:

- one versioned primitive row for identity, type, entity reference, content,
  scope, validity, privacy, proactivity, review state, and source artifact;
- ordered joins to existing `source_observations`;
- explicit disagreement edges between primitive versions;
- typed projection eligibility and action applicability.

The migration must use SQLAlchemy Core and an Alembic revision. JSON may store
typed condition/detail payloads, but required identity, lifecycle, privacy,
proactivity, and validity fields remain queryable columns with constraints.
Existing lens and conditional-judgment tables become compatibility projections;
they are not silently treated as lossless source rows.

### `PlaceRelationshipProjection` v1

Add a read-only, viewer-relative projection owned by
`backend/places/relationships.py` with a public model in
`backend/core/models/place_relationship.py`.

It returns:

- canonical `EntityRef` and viewer/relationship scope;
- evidence-backed states: `new`, `saved`, `planned`, `lived`, `skipped`, and
  `corrected`;
- the winning state plus all non-private supporting evidence references;
- occurrence count and latest safe timestamp where known;
- relationship-specific meaning only when visibility permits;
- correction and unknown markers.

Precedence is evidence-based: corrected occurrence evidence outranks inferred
or planned state; current Plan membership does not erase lived history; private
relationship claims never leak through a shared projection.

## Migration

1. Add schema and exact round-trip tests for all primitive fields.
2. Promote only reviewed calibration anchors, preserving old projections.
3. Build relationship projection over existing canonical writers.
4. Migrate Place, Home, Chat, Map, Plan, and You readers independently.
5. Remove compatibility ownership only after production-zero consumer receipts.

## Rollback and compatibility

Primitive writes are additive and versioned; rollback disables new reads rather
than deleting evidence. Existing semantic tables and legacy relationship
markers stay readable until consumers migrate. Projection failure returns
unknown, never a fabricated cold-start or lived state.

## Proof gates

- byte/field-exact primitive round trip, including disagreement and limits;
- source observation deletion or retraction cannot leave an accepted primitive
  looking fully grounded;
- one `EntityRef` produces coherent state across every supported surface;
- planned, happened, skipped, corrected, and private outcomes obey precedence;
- correction changes later projection and future eligibility;
- no runtime LLM or provider call is needed to read either projection.

## Non-goals

- A graph database or universal place table.
- Promoting the entire seeded corpus before calibration anchors pass.
- Treating relationship state as one permanent funnel stage.
- Converting private memory into public place ranking.
