# Trips / Folio — System Charter

> Surface: Trips
> Maturity (for MVP): compatibility-required during migration
> Status: wired (transitional; target read authority established, frontend migration pending)
> Last updated: 2026-07-13

## Purpose
The compatibility backend-authored read model for the currently shipped,
hero-led Trip Home. It composes "*what is the current truth of this trip, and
what's the next move?*" across the ideation → pre-trip → live → post-trip
lifecycle while the product migrates to the itinerary-first trip shell. It is
not the target trip authority.

**Redesign disposition (accepted 2026-07-13):** the current `/folio` endpoint and
hero-led Trip Home are compatibility surfaces during the itinerary-first
migration. The UI is decomposed rather than expanded. Preserve Folio's useful
lifecycle, ranked attention, source-status/partial-data, stay/cost/booking,
recent-change, discovery, and keepsake responsibilities by assigning each to
canonical Lifecycle, Itinerary/Plan State, Trip Details, History, Discover, or
Memory projections. Retire `/folio` only after field parity, first-paint
performance, degradation behavior, and old-client compatibility are proven.

## Spans (cross-repo)
- Backend: [`travel-agent/backend/folio/`](../../travel-agent/backend/folio/FEATURE.md) (`read_model.py::assemble_trip_folio`) + `backend/api/routes/folio.py`.
- Frontend: `travel-app/app/(tabs)/trips/[tripId]/index.tsx` (Trip Home), `travel-app/components/trip/TripFolioHome.tsx`, `travel-app/components/trip/TripFolioPostTrip.tsx`, `travel-app/components/trip/FolioReceiptCard.tsx`, and `travel-app/data/folio.ts`.
- Tables read: itinerary (`itineraries`/`_days`/`_blocks`, `plan_state`), `trips`, `trip_members`, expenses, proposals, story/Atlas, saves, trip photos. **Folio owns no tables.**

## Public interface (what other systems may call / read)
- **Inbound (FE → BE):** `GET /api/trips/{trip_id}/folio` (membership-verified).
- **Entry point:** `read_model.py::assemble_trip_folio(...)` receives the trip, viewer, member, attention, and leave-by inputs assembled by the route and returns `TripFolioReadModel`.
- **Authored slices:** mode + `source_status`, itinerary spine, ranked facets (plan/group/expenses/memory/Atlas), attention/discovery, group consensus, prep/leave-by, readiness/keepsake.
- **Consumes:** every Trips source system (read-only).

## Owns (source of truth)
**Nothing.** Folio is a pure **read model** — a deterministic composition over other
systems' truth. This is the load-bearing boundary: it must never become a second
write path.

## Invariants (must always be true)
- **Read-only:** all mutations stay owned by the source systems (itinerary, expenses, proposals, story/Atlas, saves, photos). A Folio that writes is a bug.
- **Honest degradation:** when a source fails, Folio degrades and reports it in `source_status`; only the known `FOLIO_SOURCE_ERRORS` are swallowed — unexpected exceptions surface loudly.
- **FE fallback discipline:** the app may fall back to legacy plan-state paths **only** when Folio errors or `source_status.plan_state` says plan state is unavailable.
- **No fabrication:** honest absence over manufactured content (empty state never invents a hero).

## Failure modes
- Single source down → that slice degrades, `source_status` flags it, rest of the Folio renders.
- Folio route error → FE falls back to legacy plan-state read paths.

## Maturity & validation
- Serves journeys: 03 (cold setup → useful workspace), 06 (home/plan/map/changes coherence).
- Current Folio assembly, degraded-source, and contract tests pass (`travel-agent/tests/api/test_trip_folio.py`).
- IR-12 backend evidence now proves one projection version and stable object/operation identity across List, Map, Details, Chat attachments, Changes, Bookings, and the Folio compatibility measurement.
- Remaining evidence: target-shell frontend dogfood, first-paint comparison, mock walk, Maestro capture, and live walk.

## Canonical docs
- Why → [`Trips Vision`](../../travel-agent/docs/product/Trips%20Vision.md).
- Current compatibility architecture → [`Trip Folio Read Model`](../../travel-agent/docs/architecture/Trip%20Folio%20Read%20Model.md), [`Trip State Architecture`](../../travel-agent/docs/architecture/Trip%20State%20Architecture.md), and [`backend/folio/FEATURE.md`](../../travel-agent/backend/folio/FEATURE.md).
- Target product contract → [`Trip Itinerary`](../../travel-app/docs/surfaces/trip-itinerary/contract.md); shipped-surface QA only → [`Single Trip Home`](../../travel-app/docs/surfaces/single-trip-home/contract.md).
- Migration contract → [`IR-12 coherent read models`](../working/itinerary-redesign-ir12-read-model-contract-2026-07-13.md).
- Tests → `travel-agent/tests/api/test_trip_folio.py`.

## Open risks / known gaps
- **Frontend migration and first paint** are now the headline risks: backend parity is proven, but the itinerary-first shell must demonstrate equal or better first-paint latency, honest partial-data behavior, exact-return navigation, and on-device coherence before Folio retirement.
- Folio's `cold`/`pre`/`imminent`/`live`/`post` mode remains compatibility-only. Target clients consume the canonical lifecycle projection and must not derive product behavior from Folio mode.
