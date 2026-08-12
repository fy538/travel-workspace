---
doc_type: decision
status: accepted
owner: founder / engineering
created: 2026-08-11
decided: 2026-08-11
why_new: Land one entity read contract additively, composing what venues/sites/accommodations/experiences each assemble independently, without migrating or retiring anything yet.
supersedes: []
source_of_truth_for: [entity-envelope-contract]
---

# One entity read contract, landed additively

## Context

[2026-08-11-entity-and-place-two-axes](./2026-08-11-entity-and-place-two-axes.md)
named the remaining gap after the vocabulary consolidation and the sites
endpoint: the entity page renders facts from four independent catalog
endpoints (`venues.py`, `sites.py`, `accommodations.py`, `experiences.py`)
and judgment from the governed substrate
(`entity_fact_resolutions`/`place_projections`, reached via
[2026-08-11-entity-status-block](./2026-08-11-entity-status-block.md)'s
`get_entity_status`), and the two have never been composed behind one
contract.

Each of the four endpoints independently resolves neighborhood-vs-city
lineage (the same correction, copied three times: a joined `place_id` is
not reliably a neighborhood, so it is only trusted as one when the joined
row's `place_type` says so), independently decides whether it has a brief,
and would each need to independently grow a `status` block. Four callers
of the same idea is the shape the earlier vocabulary work exists to close.

## Decision

**`GET /api/entities/{entity_type}/{entity_id}`** — one envelope: identity
(`EntityRef`, not a raw int — see below), place lineage, geometry, brief,
adjudicated status, and a per-kind `tail` discriminated on `kind`.

**Landed additively.** The four standalone endpoints are untouched.
Nothing has been migrated onto the envelope yet — no frontend consumer
exists, so this commit does not touch `docs/openapi.json`'s app projection
(the existing consumer-registry gate would refuse it, correctly: an
endpoint with no consumer is exactly the built-and-unconsumed pattern this
whole effort exists to close). The envelope is real, tested, and mergeable
on its own; migrating faces onto it and retiring the standalone routes are
separate follow-on slices.

### Identity is `EntityRef`, not a raw id

Venue, site and accommodation ids are autoincrement integers; experience
ids are UUIDs. A single `id: int` field cannot represent both. Rather than
inventing a new identity shape, the envelope reuses `EntityRef` — already
canonical per
[2026-08-08-place-identity-and-provenance](./2026-08-08-place-identity-and-provenance.md)
— so `ref.id` is always a string and the type-specific id shape stays
internal to each builder.

### Status carries provenance; the tail does not

`status` is the one field with a visible `sources`/`as_of` — everything
else in the envelope is a flat fact with no way to ask "who says so." That
asymmetry is deliberate: it is what makes "adjudicated, multi-source,
time-sensitive" visibly different from "stable, curated, single-producer"
at the wire level, rather than blending both into one bag a client has to
already know the provenance rules to interpret correctly.

### The neighborhood/city helper is shared only by the new route

`entity_lineage.py` extracts the three-times-duplicated logic, but only the
new envelope route uses it — `venues.py`/`sites.py`/`accommodations.py`
keep their own inline, independently-tested copies unchanged. Consolidating
the three onto the shared helper is a fast-follow, not done here: it would
touch three already-shipped, already-tested endpoints for a benefit
(one fewer copy of ~15 lines) that does not justify the behavior-change
risk in a change whose whole point is to be additive.

### A bug the postgres-leak test guard caught, not inspection

The first version opened a database connection before validating that a
venue/site/accommodation id was even numeric — a garbage id paid for a
connection it could never use, and the invalid-id path was untestable
without a DB mock. Restructured so id-shape validation
(`_has_valid_id_shape`) runs before `get_connection()`, in
`get_entity_envelope` rather than duplicated per-builder. Found by
`tests/conftest.py`'s "no test may touch real Postgres" assertion firing on
a test that expected zero DB calls for a malformed id — worth noting
because it is exactly the kind of layering bug a manual read does not
reliably catch.

## Non-goals

- **Not** migrating any face onto the envelope.
- **Not** retiring the four standalone endpoints.
- **Not** consolidating the three existing neighborhood/city lookups onto
  the shared helper — only the new route uses it.
- **Not** exposing per-field confidence in the tail, or in `status` beyond
  what `PlaceDecisionContext` already carries (see the status-block
  decision's identical non-goal).
- **Not** widening coverage. The envelope reads the same near-empty
  substrate `status` already does — see that decision for the numbers.

## Consequences

- A caller that wants "the object page's data" for any catalog kind has one
  contract to call instead of branching on four, once something calls it.
- The next slice (migrating venue and site onto this) is unblocked and
  scoped: swap the data-fetch layer under `ObjectPageShell`, which both
  faces already share.
- The four standalone endpoints remain load-bearing until that migration
  and the retirement slice after it — this decision does not shrink their
  surface today.
