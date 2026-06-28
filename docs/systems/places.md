# Places (hours/open) — System Charter

> Surface: Trips
> Maturity (for MVP): Should-have (support)
> Status: wired
> Last updated: 2026-06-27

## Purpose
The real-time operational layer of the place model — answers the one fact that
goes stale in our corpus: *is this venue open right now / what are its hours / has
it permanently closed?* Serves belief #16 (the place model's surface layer) and
backs journey 08's "what's open now" answer. Owns no place *content* — only the
live wire.

## Spans (cross-repo)
- Backend: [`travel-agent/backend/places/`](../../travel-agent/backend/places/FEATURE.md) — `linker.py` (the real handler entry point: cache → SWR → metered provider → lazy discovery → write-back), `service.py` (primary→fallback orchestration), `discovery.py` / `taste.py` (coverage + taste floor), `cache.py`, `budget.py`, `factory.py`, `foursquare.py`, `google_places.py`, `proactive_refresh.py`.
- Frontend: consumed indirectly via Concierge tool replies and "what-now" / "near you" surfaces; no dedicated Places screen.
- Tables of record: `place_status_cache`, `place_provider_calls` (audit). Reads `venues`, `itinerary_blocks`.

## Public interface (what other systems may call / read)
- **Entry points (internal):** `linker.get_status_for_venue(service, venue_id)` (in-corpus) · `linker.get_status_for_named_place(service, name, lat, lng)` (ad-hoc) · `taste.discover_nearby_ranked(...)` ("near you") · `proactive_refresh.refresh_upcoming_venues()` (cron pre-warm).
- **Consumes:** the corpus (`venues`, PostGIS proximity), Foursquare + Google Places (metered), the shared `booking_agent/providers/resilience` `CircuitBreaker`.
- **Never:** call `PlacesService` directly from a tool handler — it has no cache or budget; you'd bypass the cost controls. The linker is the only sanctioned production path.

## Owns (source of truth)
The provider plumbing, the per-field TTL cache (`place_status_cache`), and the daily
per-provider budget/audit (`place_provider_calls`). It is the sole writer of those
tables and of the discovered `fsq_id` / `google_place_id` it persists back onto a
venue row. It owns **no** place content or corpus.

## Invariants (must always be true)
- **`None` means "we don't know," never "false."** `open_now` / `hours_today` are `None` when the provider didn't return them; a linker `None` return = "no live data for this venue." Callers MUST surface uncertainty — **never fabricate hours or render `None` as "closed."** This is the load-bearing honesty invariant.
- **No-credentials path is `None`, not an exception** — `get_places_service()` returns `None` with no key configured; callers null-check and skip the network entirely.
- **Budget gate is hard and counts failures** — both success and failure write a `place_provider_calls` row; `can_call` blocks at the daily UTC-day limit (Foursquare 500/day, Google 100/day; 0 = unlimited). Each provider gated independently.
- **Per-field TTL + stale-while-revalidate** — `open_now` (10 min), `hours` (24 h), closure (7 d); a live-but-stale row is served immediately while a bounded background refresh fires off-path. The caller never waits.
- **Asymmetric quality floor** — curated corpus rows pass; generic live-provider POIs are dropped unless they match a real taste signal, so a generic "3 restaurants near you" card never surfaces.
- **Google place-id retention** — discovered Google ids are purged after 30 days (ToS) so the next lookup re-discovers.

## Failure modes
- Provider miss / `PlacesProviderError` → primary falls through to fallback → both miss → negative-cache (30 min) + return `None` (degrade to "don't know," never fabricate).
- Background refresh semaphore full → skip rather than queue (a stale-by-5s straggler is worse than letting the next caller re-trigger); all refresh errors swallowed.
- No provider key → `factory` returns `None`; the whole subsystem is a no-op, not an error.

## Maturity & validation
- Serves journey: 08 (live what-now / is-it-open).
- DoD state: provider-chain + cache + budget + SWR tests ✅ · honesty (`None` ≠ closed) covered ✅ · **on-device walk against a live provider key ❌ · live "near you" taste-floor walk ❌**.
- Support-tier: a journey can be faked/manual-ed for first ~10 users; not on the wedge critical path.

## Canonical docs
- why → `product/Product Architecture Principles.md` ("Location Context Model") · what(be) → `backend/places/FEATURE.md`.
- Tests: `tests/places/*` (cache TTL, budget gate, linker pipeline, taste floor).

## Open risks / known gaps
- The honesty invariant is the audit-bait: a UI that renders a `None` field as "closed," or a tool reply that fills in plausible hours, breaks belief #16's trust. Verify the full path surfaces "we don't have live data."
- `service.py`'s docstring calls `PlacesService` "the single entry point" — misleading; handlers that take it at its word skip cache + budget. Confirm no handler calls it directly.
- Live provider keys are the common-dev `None` case — the metered/budget/discovery paths are largely untested against real Foursquare/Google traffic.
