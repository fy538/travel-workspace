---
doc_type: working
status: active
owner: founder / product / engineering
created: 2026-08-23
last_verified: 2026-08-23
expires: 2026-09-22
why_new: Records the first M3 identity-integration packet between the viewer-relative experience graph and the existing Places readers.
supersedes: []
promotes_to: null
source_of_truth_for: [m3-canonical-place-reader]
---

# M3 canonical place-reader execution receipt

## Scope

The first M3 packet closes the graph-to-Places identity seam identified in the
multiplayer integration audit. The backend public projection already resolves a
viewer-authorized `canonical_entity_ref` and deliberately redacts the internal
`world_entity_id`. Mobile was still attempting to join occasions by that
redacted graph UUID, so the join could never work against the real public
projection.

## Change

`travel-app/data/experienceGraph.ts` now exposes
`selectOccasionsForCanonicalEntity(context, entityRef)`, matching occasions by
the typed `{ type, id }` reference that the backend authorizes. Surface
summaries also carry the optional canonical reference for an occasion or
outcome. No graph UUID is promoted into a Places identity, and no slug or
message text is used as a fallback.

This is a read-only identity bridge. It does not create a Place, alter an
Occasion, infer a relationship, or open a public feed. Existing Places and
venue readers remain the owners of presentation and navigation.

## Evidence

- Mobile `experienceGraph` suite: 8 tests passed, including canonical-entity
  joins, unresolved refs, and graph-UUID redaction behavior.
- `npx tsc --noEmit` passed.
- Targeted ESLint passed.
- Commit: mobile `966edeca` — `fix(m3): join graph context by canonical entity`.

## Remaining M3 work

1. Add an explicit viewer-scoped navigation/read action from a canonical ref to
   the appropriate Place, venue, or site owner surface.
2. Add plural private outcome capture after an Occasion is lived, with
   independent correction and source lineage.
3. Bridge Trip proposals/votes only when a handoff is explicitly attached to a
   Trip; never infer Trip membership from a shared place.
4. Run the two-account device walk and capture real receipts; feature flags
   remain the release boundary.
