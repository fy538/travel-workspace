# Retired Discover surface — compatibility charter

> Product status: retired
> Canonical owners: Places and Vesper
> Last updated: 2026-08-12

## Purpose

Discover is no longer a product surface. Its useful capabilities belong to
Places (exploration, maps, editorial context, and saves) and Vesper
(contextual judgment and handoff into Trips). The `discover` backend module may
remain temporarily as implementation substrate while its contracts are moved or
retired; its name does not create a fourth destination, feature stream, or
roadmap.

## Compatibility boundary

- **Legacy mobile URL:** `/(tabs)/discover` redirects to Places and preserves
  supplied place context.
- **Legacy map transport:** `GET /api/discover/map` is deprecated. New clients
  use `GET /api/places/map`; both routes must return the same map projection
  until deployed-version evidence permits removal.
- **Legacy feed transport:** `GET /api/discover/feed` has no canonical mobile
  home. Do not add a caller; classify it for retirement or migrate a concrete,
  validated Places use before extending it.

## Invariants

- A Places entry supplies concrete entity context before Vesper receives a
  question; it never opens an empty, generic chat.
- Vesper may advise or explain, but Trips remains the owner of shared plan
  mutations and receipts.
- No new user-facing copy, route, telemetry surface, journey, or release
  capability uses Discover as a product owner.
- Existing persisted data and historical telemetry remain readable without
  inventing a new Discover UI.

## Validation

The canonical product loop is [Journey 07](../journeys/07-discover-to-contextual-vesper-to-trip-action.md): Places → Vesper → Trips. The legacy URL redirect
has a focused mobile test; the Places workspace and map require the real
surface-level device coverage.

## References

- Product decision: [retire Discover and Atlas product surfaces](../decisions/2026-08-12-retire-discover-and-atlas-product-surfaces.md)
- Backend implementation: `travel-agent/backend/discover/`
- Mobile Places workspace: `travel-app/components/places/PlacesWorkspace.tsx`
