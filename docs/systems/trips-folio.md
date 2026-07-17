# Trips / Folio — System Charter

> Surface: Trips
> Maturity (for MVP): retired compatibility surface
> Status: retired (canonical itinerary/lifecycle projections now own the read path)
> Last updated: 2026-07-16

## Purpose
Historical charter for the removed backend-authored Folio read model and
hero-led Trip Home. Preserve it as migration provenance only. It is not a
current route, fallback, read authority, or target design input.

**Redesign disposition (completed locally 2026-07-16):** the `/folio` endpoint,
assembly package, frontend aggregate, and hero-led Trip Home are removed. The UI
was decomposed rather than expanded. Folio's useful lifecycle, ranked
attention, source-status/partial-data, stay/cost/booking, recent-change,
discovery, and keepsake responsibilities now live in canonical Lifecycle,
Itinerary/Plan State, Trip Details, History, Discover, or Memory projections.

## Spans (cross-repo)
- Backend: retired; the former Folio route and assembly package have been removed.
- Frontend: retired Folio components/data are removed. The trip index is a
  redirect-only entry resolver; `plan.tsx` is the Itinerary List/Map workspace.
- Tables read: none. **Folio owns no tables.**

## Public interface (what other systems may call / read)
- No current public interface. Deleted endpoint/module names remain denylisted
  by deletion-reference and import-boundary checks.

## Owns (source of truth)
**Nothing.** Current trip truth belongs to canonical lifecycle, Itinerary,
Trip Details, History, and their source systems.

## Invariants (must always be true)
- A new Folio route, aggregate, fallback, or mutation path is a regression.
- Retained useful behavior must be added to its owning canonical projection,
  never reconstructed as another all-purpose trip dashboard.

## Failure modes
- Old bookmark targets the trip index → resolver selects canonical Itinerary or
  meaningful completed Memory.
- Canonical source degrades → its owning projection reports honest partial data;
  no Folio substitution exists.

## Maturity & validation
- Historical journeys: 03 and 06.
- Current journey authority: the itinerary-first J03/J05/J06/J08/J10/J12
  one-pagers and Trip Itinerary surface contract.
- Local deletion-reference scans report zero Folio production callers.

## Canonical docs
- Why → [`Trips Vision`](../../travel-agent/docs/product/Trips%20Vision.md).
- Historical compatibility architecture → [`Trip Folio Read Model`](../../travel-agent/docs/architecture/Trip%20Folio%20Read%20Model.md) and [`Trip State Architecture`](../../travel-agent/docs/architecture/Trip%20State%20Architecture.md).
- Target product contract → [`Trip Itinerary`](../../travel-app/docs/surfaces/trip-itinerary/contract.md); historical surface provenance only → [`Single Trip Home`](../../travel-app/docs/surfaces/single-trip-home/contract.md).
- Migration contract → [`IR-12 coherent read models`](../working/itinerary-redesign-ir12-read-model-contract-2026-07-13.md).
- Retirement guards → `travel-agent/scripts/certify_itinerary_deletion_lanes.py`
  and the itinerary legacy-reader/consumer-boundary checks.

## Open risks / known gaps
- Deployed artifact/caller absence and on-device journey evidence remain part of
  formal cutover certification; they do not authorize restoring Folio locally.
- Historical `cold`/`pre`/`imminent`/`live`/`post` Folio mode must not reappear.
  Target clients consume the canonical lifecycle projection.
