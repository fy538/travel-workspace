---
doc_type: working
status: active
owner: strategy integration / Places
created: 2026-09-05
last_verified: 2026-09-05
expires: 2026-10-05
why_new: Closes the remaining Places identity seam before the native field and Focus/Path journey is promoted.
source_of_truth_for:
  - Places result-set identity and revision handoff
depends_on:
  - complete-system-integration-roadmap-2026-09-05.md
  - ../systems/four-root-loop-object-surface.md
  - ../decisions/2026-08-30-adopt-home-and-places-consumer-anatomy.md
---

# Places result-set and context identity contract

## Why this seam exists

`PlacesContextRef.handle` is a safe continuation identity for a resolved
scope. It is not, by itself, an identity for the inventory that the user is
currently seeing. The mature feed, search, map, and future Focus/Path readers
can therefore carry the same opaque handle while silently representing
different result sets or different source revisions.

The Places contract requires one navigable encounter: field, map, search,
Focus, and Path should transform or narrow a known result set rather than
quietly replace it. This document names the smallest additional seam needed
to make that testable. It does not create a Places event bus, a generic query
service, or a client-owned cache.

## Proposed wire value

Add an additive `PlacesResultSetRef` to the Places-owned feed/search/map and
collection responses. It is a server-authored value with these fields:

| Field | Meaning | Rule |
| --- | --- | --- |
| `set_id` | Stable semantic identity for the inventory and question | Opaque to clients; derived from the resolved context plus the query/filter semantics. Never derive it from a route string or display label. |
| `context_handle` | The existing opaque continuation handle | Must equal the response's resolved `PlacesContextRef.handle` when one exists. A missing handle is an explicit unavailable-context state, not a client-generated fallback. |
| `revision` | Server-owned revision of the represented inventory/context | Changes when the authoritative scope, audience/grant, source corpus, or material current-world inputs change. Unknown revision remains explicit; clients must not invent one. |
| `scope` | The normalized scope identity | Echoes the server-owned scope kind and canonical ID. Coordinates are never identity fields. |

The value is a reference, not a snapshot. Rows, claims, provider freshness,
friend marks, and section revisions retain their own evidence and correction
semantics. A result-set revision tells a reader whether it is still reading
the same represented inventory; it does not grant access or prove that every
row is current.

## Identity and transformation rules

1. **Field and map share a set.** A field response and a map response opened
   from the same resolved scope and question carry the same `set_id` and
   `revision`. Map viewport, pin density, and visual ordering are
   transformations of that set. A map opened with a new explicit scope starts
   a new set.
2. **Search narrows or replaces the question deliberately.** A query inside
   the current scope derives a query-specific `set_id` whose parent context
   handle remains the same. Clearing the query returns to the parent field
   set. Search must not silently widen a city/trip scope to global.
3. **Focus and Path retain provenance.** Selecting a pin, row, or Home door
   carries the originating `set_id`, `revision`, context handle, and selected
   canonical entity ref. Focus/Path may add a new entity-local revision, but
   they may not claim to be a fresh field inventory.
4. **Home doors preserve the handoff.** A Home Places opening includes the
   same context/result-set reference when it is based on a known Places
   field. A generic Places opening may resolve a fresh automatic set, and must
   say so through the normal root freshness state.
5. **No authority by identity.** A set reference is not a grant, membership
   proof, location permission, or permission to fetch a row. Every endpoint
   re-resolves the handle and re-checks viewer authority before returning
   data.
6. **No client synthesis.** The client may echo or drop a reference when a
   route ends. It must not construct revisions, concatenate coordinates, or
   reuse a stale reference after a `409`/revocation response.

## Suggested implementation boundary

Implement this in the existing Places owners, not a new service:

- resolve the context once at each entry point;
- compute the normalized set reference beside the existing feed/search/map
  result construction;
- echo it through `PlacesFeed`, `PlacesSearchResponse`,
  `PlacesSavedPage`, `PlacesReadingPage`, and `DiscoverMapResponse` (the
  historic class name remains for OpenAPI compatibility);
- carry it through the v1 root projection and `places-root-runtime.v1`;
- thread it into native return envelopes before enabling the semantic Places
  renderer; and
- leave existing row/source revisions and Life ownership unchanged.

The first implementation may use the existing root/feed revision as the
authoritative revision when it is available. If an endpoint cannot prove a
shared revision, it must return an explicit unknown revision and remain dark
for cross-view identity claims; it must not hash presentation JSON and call
that a world revision.

## Acceptance portfolio

| Case | Required evidence |
| --- | --- |
| Home → Places field | Context handle and set reference survive the opening; the field is either the same set or explicitly a fresh automatic set. |
| Field → map → venue → back | Map and field share `set_id`/`revision`; selected venue preserves the originating set and exact scope/filter return. |
| Field → search → clear search | Search has a query-specific child identity; clearing returns to the parent field identity without widening scope. |
| Scope change | NEW YORK → RED HOOK produces a new set; old rows are not relabeled as the new scope. |
| Source correction/revision | A changed source revision prevents stale set reuse and triggers recomposition or an honest stale state. |
| Revoked membership/grant | Handle resolution fails closed; no cached set reference restores private rows or friend marks. |
| Offline/unknown revision | The client can still show previously authorized value, but does not claim that map/search/focus are the current same set. |

This contract is a prerequisite for Places native promotion, not a reason to
block the mature workspace or to add a generic route layer. Until the
producer and consumers are implemented and tested, keep the semantic Places
renderer dark and treat the current opaque-handle behavior as compatibility
only.
