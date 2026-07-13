# Trips / Folio — System Charter

> Surface: Trips
> Maturity (for MVP): MVP-required
> Status: wired (beta; not yet validated on-device)
> Last updated: 2026-06-27

## Purpose
The single backend-authored read model for the Trip Home surface — it answers
"*what is the current truth of this trip, and what's the next move?*" across the
ideation → pre-trip → live → post-trip lifecycle. Serves belief #17 (*if a user is in
the product without a trip context, that's a design failure* — the trip is the spine).

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
- Frontend: `travel-app/app/(tabs)/trips/[tripId]/index` (Trip Home), `components/trip-home/*`, `components/focus-home/*` (Deck), `data/folio.ts`.
- Tables read: itinerary (`itineraries`/`_days`/`_blocks`, `plan_state`), `trips`, `trip_members`, expenses, proposals, story/Atlas, saves, trip photos. **Folio owns no tables.**

## Public interface (what other systems may call / read)
- **Inbound (FE → BE):** `GET /api/trips/{trip_id}/folio` (membership-verified).
- **Entry point:** `read_model.py::assemble_trip_folio(trip_id, user_id, today=None)` → `TripFolio` shape.
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
- DoD state: assembly + degraded-source + contract tests ✅ (`tests/api/test_trip_folio.py`) · **mock-walk ❌ · Maestro ❌ · live-walk ❌**.
- Known gap (journey 06): no unified block-id parity test proving the same trip truth across Home / Plan / Map / Changes after a mutation.

## Canonical docs
- why → `product/Trips Vision.md` · how → `architecture/Trip Folio Read Model.md` · `architecture/Trip State Architecture.md` · what(be) → `backend/folio/FEATURE.md` · what(fe) → `page-specs/trips-home-hero.md` · `trip-page.md`.
- Tests: `tests/api/test_trip_folio.py`.

## Open risks / known gaps
- **Coherence (journey 06)** is the headline risk: a mutation must propagate identically to every surface. `invalidateTripReadModels` exists on the FE but there is no cross-surface block-id parity test. This is the first thing to harden for the wedge.
- Mode-derivation (ideation/pre/live/post) is now date-derived (the dead status column was retired 06-25) — verify the boundaries with the time-travel clock across persona states.
