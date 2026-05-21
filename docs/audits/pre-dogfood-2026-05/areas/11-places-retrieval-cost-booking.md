# Pre-Dogfood Area Audit 11 — Places, Retrieval, Cost Control & Booking Safety

Date: 2026-05-21
Scope: fan-out retrieval + Qdrant brief search; places cache + provider providers +
budget gate + cron + Google ToS retention; external-API cost controls
(Google Places / Foursquare / Tavily / Amadeus / Duffel / Viator / Rome2Rio);
venues router registration; booking-agent deep-link safety + auto-charge
verification + resilience decorator coverage.
Mode: read-only; no product code or config was modified.

## Summary

| Severity | Count |
|---|---:|
| P0 | 0 |
| P1 | 4 |
| P2 | 4 |
| TECH-DEBT | 3 |

**Booking auto-charge: confirmed safe for dogfood.** Every code path that could put
real money on the table was traced and verified inert:

- `BookingProvider.create_order` raises `NotImplementedError` in the base, and **no
  subclass overrides it** (Amadeus flights/hotels/cars, Duffel, Rome2Rio, Viator,
  Restaurant — none). `Travel Agent/backend/booking_agent/providers/base.py:89-95`,
  grep `create_order` across `providers/` returns only the base definition.
- L3 `auto_select_best` **explicitly skips** `booking_method == "deep_link"` offers
  before building the cart (`booking_graph.py:399-401`), so Viator activities and
  the Amadeus/Restaurant deep-link rows never enter `selected_offers` and never get
  totalled into `cart_total_amount`.
- `persist_seed_offer` writes single-venue seeds at `status="available"`, not
  `"selected"` (`booking_graph.py:606-623`) — pre-fix comment captures the exact
  regression this defends against ("downstream charging logic keyed on 'selected'
  then treated them as user-confirmed even though no /confirm step existed").
- `confirm_booking` at L1/deep_link returns a `handoff` envelope with the deep
  link / phone number; at L2/L3 with `booking_method=api` it spawns a
  `booking_session` but the dispatched graph terminates at status `review` or
  `offers_ready` without ever calling `create_order`
  (`session_dispatcher.py:79-114`).
- Concierge → Booking handoff `BookingCapability.api_bookable` is hard-False for
  restaurant (`capability.py:227`) and activity (`capability.py:231`), and even for
  hotels the `_API_CAPABLE_PROVIDERS` set is "aspirational" with no provider
  actually wired (`capability.py:111-119`).

Net: a tester cannot trigger an actual payment from any UI path. The
`POST /api/trips/{trip_id}/booking/sessions/{session_id}/cart/confirm` endpoint
(`backend/api/routes/booking.py:301-334`) marks the session "confirmed" and
auto-logs expenses, but **does not invoke any provider order endpoint**. The
state-coherence consequence is filed below as P1-3.

**Venues router: registered (the earlier 404 is closed).** Imported at
`backend/api/router_registry.py:53` and attached to `_ROUTERS` at line 108.
`register_routes` iterates and calls `app.include_router(router)` at line 121.
`GET /api/venues/{venue_id}` returns lean venue detail joined with
`places` + `briefs` (`backend/api/routes/venues.py:57-112`).

**Retrieval grounding:** `fan_out_restaurant_search`
(`backend/planning_agent/fan_out_search.py`) treats the Qdrant brief payload as the
source of truth for `venue_id` and never re-checks it against Postgres `venues`.
Trip-scope filtering is correct (`place_ids` from `provider.place_scope_ids()`
maps onto the `place_id` payload field that `_venue_payload` does write;
`payload_builders.py:64`). `eval_world` is honoured. `_parallel_searches` is
fault-tolerant (`return_exceptions=True`, lane-level fallback). Empty-result
diagnostic is good. **The biggest gap is permanently-closed venues
silently passing through fan-out** (P1-1 below).

**Cost gates:** `backend.places.budget` is well-built — daily caps per provider,
audited via `place_provider_calls`, breaker check via `places.linker._get_status_metered`
+ `_find_place_metered`. **It only protects the concierge `get_venue_status` path.**
The Booking-Agent `RestaurantProvider` (`backend/booking_agent/providers/restaurant.py`)
calls the same Google Places API directly with the same shared key but **does not go
through `places.budget`** (P1-2 below). Tavily has a circuit breaker but no daily
spend cap and its 8s timeout is set on a config object the `AsyncTavilyClient`
never reads (P1-4 below).

**Google ToS retention:** `purge_stale_google_ids` nulls `venues.google_place_id`
older than 30 days, but `place_status_cache.place_id` and `.payload['place_id']`
retain the same identifier past the 30-day window (up to ~37d in practice). And
the cron is documented but not wired by default (Known Gap O-14). For dogfood
that has no automation host yet, the ToS purge is effectively manual (P2-2).

---

## Findings

### P1 — Permanently-closed venues are not filtered out of restaurant fan-out
**References:**
- `Travel Agent/backend/planning_agent/fan_out_search.py:50-184` (`fan_out_restaurant_search`)
- `Travel Agent/backend/core/vector/briefs.py:249-327` (`_build_venue_filter` — no
  `permanently_closed` condition)
- `Travel Agent/backend/research_agent/pipeline/payload_builders.py:55-93`
  (`_venue_payload` — payload omits closure status)
- `Travel Agent/backend/places/base.py:50` (`PlaceStatus.permanently_closed` exists)
- `Travel Agent/backend/core/db/_tables/places.py:44` (`places.permanently_closed`
  column exists)
- No `venues.permanently_closed` column; no Qdrant payload field; no post-filter

**Why it matters to a real tester:** The product's main trust contract is "no
confabulated / closed venue". Today, a venue that closed since the brief was
written — captured in either `places.permanently_closed` (Postgres) or
`place_status_cache.permanently_closed` (live) — will still surface in
`search_restaurants` results, with its curator brief excerpt and route info,
ready for the agent to recommend. The brief looks real because the venue row IS
real. The grounding output guard (`output_guards.py::_check_grounding`) is
heuristic title-case matching and will not flag a closed venue whose name still
appears in the tool output. The agent only learns about closure if it
independently calls `get_venue_status` for that specific venue, which the prompt
encourages but doesn't enforce — and `get_venue_status` itself is best-effort
(returns `unavailable` when keys aren't configured or the daily cap is hit).

**Repro / deterministic test idea:**
1. Seed a venue, embed its brief into Qdrant.
2. Set `places.permanently_closed=true` for the venue's parent place (or insert a
   `place_status_cache` row with `permanently_closed=true, not_found=false,
   expires_at=NOW()+7d`).
3. Call `fan_out_restaurant_search` with descriptions that semantically match the
   brief.
4. Assert the closed venue is excluded from `results`. Today it is present.

**Suggested fix direction:** Add `permanently_closed` to the Qdrant venue payload
(populated from `places.permanently_closed` at brief write time, refreshed by
the existing `update_brief_payload` hot-path hook once a closure is detected
via `places.linker`). Add a `must_not` clause in `_build_venue_filter` that
excludes `permanently_closed=true`. As a defense-in-depth, have
`_enrich_results_async` consult `place_status_cache.permanently_closed` for the
candidate venue ids and drop matches before the LLM ever sees them. Same shape
as the `null-tolerant` post-filter that already exists for `open_at`.

**Confidence:** High.

---

### P1 — Booking-Agent `RestaurantProvider` calls Google Places outside the daily budget cap
**References:**
- `Travel Agent/backend/booking_agent/providers/restaurant.py:38-96` (calls
  `POST /v1/places:searchText` directly via `self._get_client()`)
- `Travel Agent/backend/booking_agent/providers/registry.py:66-71` (always
  registered, keyed on `config.google_places_api_key`)
- `Travel Agent/backend/places/budget.py:37-51` (`can_call("google_places")` is
  the cap)
- `Travel Agent/backend/places/linker.py:169-203` (`_get_status_metered` — the
  ONLY caller of `can_call`/`record_call`)

**Why it matters to a real tester:** Booking-Agent restaurant searches re-use the
same `GOOGLE_PLACES_API_KEY` that the places subsystem meters at
`PLACES_GOOGLE_DAILY_LIMIT=100/day` (~$1.70/day Google Place Details spend).
But the booking provider bypasses `places.budget` entirely — every block in an
itinerary that maps to `category=restaurant` (via `_map_block_to_category` in
`booking_graph.py:781-795`) fires one `POST /v1/places:searchText` request per
block when `extra["venue_data"]` is not present. A 7-day trip itinerary with
10 restaurant blocks dispatched by `execute_searches` runs in parallel and
spends 10 unmetered Google Text Search calls (~$0.32). The `places.budget` row
count won't reflect any of this — it tracks `provider_name="google_places"`
inserted by `places.budget.record_call`, not Booking-Agent traffic — so the
dashboard panel that operators read for "are we burning Google?" silently
under-reports. The circuit breaker on the provider helps after 5 consecutive
failures, but does nothing for spend control while everything is succeeding.

**Repro / deterministic test idea:**
1. Set `PLACES_GOOGLE_DAILY_LIMIT=1` in env; insert one row into
   `place_provider_calls(provider='google_places', called_at=now())` to exhaust
   the budget for today.
2. Confirm `await can_call("google_places")` returns False.
3. Run `await create_providers(booking_settings)["restaurant"].search(...)` with
   `params.destination='Lisbon'` and no `venue_data`.
4. Expect the call to be short-circuited or at least metered. Observed: the
   HTTP request goes out anyway, no row is added to `place_provider_calls`, no
   cap is enforced.

**Suggested fix direction:** Either (a) factor `places.budget.can_call` +
`record_call` into a shared decorator that wraps any Google-Places-billed
provider call, and apply it to `RestaurantProvider.search` (cleanest), or
(b) route `RestaurantProvider`'s Google calls through `places.service` /
`places.linker` so the existing metering kicks in (more refactor). Bonus:
move `restaurant` provider registration behind a feature flag so an operator
who doesn't intend to use Booking-Agent restaurant search can disable it
without unsetting the Google key (the key is needed by the places subsystem).

**Confidence:** High.

---

### P1 — `cart/confirm` marks session "confirmed" and auto-logs expenses without a real provider order
**References:**
- `Travel Agent/backend/api/routes/booking.py:301-334` (`confirm_cart`)
- `Travel Agent/backend/booking_agent/agents/booking_graph.py:639-648`
  (`finalize_session` — graph ends at `review` for L3, no order step)
- `Travel Agent/backend/booking_agent/providers/base.py:89-95`
  (`create_order` is `NotImplementedError`)
- `backend/expenses/auto_log.py::auto_create_expenses_from_booking` invoked from
  `routes/booking.py:323-330`

**Why it matters to a real tester:** Auto-charge is verifiably impossible (see
Summary), but a tester who taps "Confirm" on the cart UI sees the
booking_session transition to `"confirmed"` AND **expenses get auto-logged on
the trip** for the items in the cart. There is no real reservation behind any
of those expenses — `create_order` was never called. The expense rows look
authentic enough that a tester checking the trip total a day later would
believe a hotel was booked. For dogfood this is misleading state, not a
charge — but it pollutes the expenses test data and could be reported as a
"booking succeeded" UX bug. Restricted blast radius today because L3
`auto_select_best` filters out deep-link offers and no API provider is wired
(`_API_CAPABLE_PROVIDERS` is "aspirational" per `capability.py:111-113`), so
the cart will usually be empty — but the moment `BOOKING_AMADEUS_API_KEY`
lands (Known Gap O-13 canary), hotel offers join the cart and the gap opens.

**Repro / deterministic test idea:**
1. Manually insert a `booking_offers` row with `session_id=X, status='selected',
   price_amount=200, price_currency='USD'`.
2. POST `/api/trips/{trip_id}/booking/sessions/{X}/cart/confirm`.
3. Assert no provider order was placed (today: true — there's no call).
4. Assert no expense row was created for the unbooked item, OR ensure the
   session can't transition to `confirmed` until a per-offer "ordered" state
   exists. Today: the expense row is created and the session is confirmed.

**Suggested fix direction:** Either (a) make `cart/confirm` reject when any
selected offer's `booking_method == "api"` and there's no provider with a real
`create_order` (returns a 409 "API booking not enabled — use deep-link
flows"); or (b) split session status into `cart_review_finished` vs
`provider_orders_placed` so the expense auto-log only fires after a real
order step exists. Add a feature flag `BOOKING_API_ORDERS_ENABLED=false`
that short-circuits `cart/confirm` for dogfood.

**Confidence:** Medium.

---

### P1 — Tavily `search_web` has no per-day spend cap and the 8s timeout is unenforced
**References:**
- `Travel Agent/backend/core/tools/web_search.py:22-101` (no daily cap; circuit
  breaker only)
- `Travel Agent/backend/core/tools/web_search.py:53-59` (`_get_client` constructs
  `AsyncTavilyClient(api_key=key)` — no timeout kwarg)
- `Travel Agent/backend/concierge/tool_handlers/web_search.py:32-48`
  (`_TIMEOUT_SECONDS = 8` is set on `ToolConfig` but never wired into the SDK
  client)
- `Travel Agent/backend/concierge/tool_handlers/web_search.py:88` comment "fast-fail
  without paying the 8-second timeout per call" — the 8-second timeout doesn't
  actually exist
- Compare: `places.budget.can_call` enforces a daily cap per Google/Foursquare
  provider (`backend/places/budget.py:37-51`)

**Why it matters to a real tester:** Tavily basic search is ~$0.004/call and
advanced is ~$0.008/call. The concierge tool defaults to `max_results=5` →
basic mode. An LLM that fans out 3-5 web searches per turn over a debug-loop
chat session can rack up ~$0.04/turn unmetered — comparable to a single full
Sonnet turn. The places subsystem has a 100/day Google cap precisely for this
reason; web_search has no equivalent. The circuit breaker only opens after 5
consecutive transient failures, so a sustained-success-but-expensive workload
slips through. Separately: a hung Tavily call can block the concierge turn
for the SDK default timeout (typically ~60s) rather than the documented 8s,
because `AsyncTavilyClient` is instantiated without `timeout=8` and the
ToolConfig's `timeout_seconds` field is never read. This compounds with the
"agent fans out" pattern — a stuck Tavily call can hold a tool slot for
minutes.

**Repro / deterministic test idea:**
1. Mock the Tavily endpoint to sleep 30s then respond.
2. Call `concierge.tool_handlers.web_search.execute_search_web({"query": "x"})`.
3. Assert the call returns within 8s (configured timeout). Observed: it waits
   the full mock duration (or the SDK default), proving the 8s is unenforced.

**Suggested fix direction:**
1. Pass `timeout=self.config.timeout_seconds` (or a hard 8s) into
   `AsyncTavilyClient(api_key=key, ...)` if the SDK supports it, or wrap each
   `client.search(...)` in `asyncio.wait_for(..., timeout=8)`.
2. Add a daily Tavily call cap mirroring `places.budget` — same table shape
   (`provider='tavily'` rows in `place_provider_calls`, or a new
   `tool_call_counters` table) with a settings field
   `TAVILY_DAILY_LIMIT=200` (≈$0.80/day basic-tier ceiling). Apply via the
   shared `can_call` API so future external tools (Foursquare-as-tool, etc.)
   benefit.

**Confidence:** High on missing cap; Medium on unenforced timeout (depends on
the installed `tavily` SDK version's default behaviour; either way the
documented 8s is not honoured by the code path).

---

### P2 — Google `place_id` is retained past the 30-day ToS window in `place_status_cache`
**References:**
- `Travel Agent/backend/places/cache.py:300-310` (`_purge_stale_google_ids_sync`
  — nulls **only** `venues.google_place_id`)
- `Travel Agent/backend/places/cache.py:260-267` (`_purge_expired_sync` — drops
  cache rows only when `expires_at < now - grace_days` (default 30))
- `Travel Agent/backend/places/cache.py:313-364` (`_put_cached_sync` — `payload`
  JSONB contains the full `PlaceStatus` including `place_id`; outer `expires_at`
  = `max(open_now, hours, identity_expires)` = `now + 7d` by default)
- `Travel Agent/backend/places/cache.py:32-40` (default `identity_ttl=7d`)
- `Travel Agent/scripts/purge_places_cache.py:84-91` (refuses
  `--google-max-age-days > 30` — the intent is well-documented)

**Why it matters to a real tester:** Even when `purge_stale_google_ids` runs on
schedule, `place_status_cache.place_id` (the column) and
`place_status_cache.payload['place_id']` (inside the JSONB) still carry the
Google place identifier for up to ~37 days after the last write (7d identity
TTL + 30d grace before row deletion). Google Places ToS reads as 30-day
retention; we're nominally compliant on `venues.google_place_id` but not on
the cache. A compliance review would flag this; a real user has no direct
impact, but the next time legal reviews data retention this is the row that
fails the audit.

**Repro / deterministic test idea:**
```sql
SELECT provider, place_id, fetched_at, expires_at,
       (NOW() - fetched_at) AS age
FROM place_status_cache
WHERE provider = 'google_places'
  AND (NOW() - fetched_at) > interval '30 days';
```
Today: returns rows whenever a venue's cache row has gone untouched for >30
days but <37 days post-write.

**Suggested fix direction:** Extend `_purge_stale_google_ids_sync` to also (a)
DELETE `place_status_cache` rows where `provider='google_places' AND fetched_at
< now() - 30d`, and (b) consider stripping `payload['place_id']` from rows
that are kept but older than 30 days (less invasive than deletion). Document
the 30d cap as a hard ceiling in `PlacesSettings` so a future config push
can't quietly raise it.

**Confidence:** High on the policy gap; Medium on legal interpretation (the
30-day rule applies to "place_id cached on user-facing personalization data" —
internal operational cache may have a different read, but the safer side is
to purge).

---

### P2 — Cron scripts are documented but not wired; ToS purge and proactive refresh are operator-manual today
**References:**
- `Travel Agent/CLAUDE.md:177-208` (cron lines listed under "Places cache cron
  (O-14 ops wiring)" — described as suggested, not active)
- `Travel Agent/docs/working/Known Gaps Register.md:688-720` (O-14 confirms
  "Wire ... into cron" is still operator-side TODO)
- `Travel Agent/scripts/refresh_upcoming_venues.py:1-77`
- `Travel Agent/scripts/purge_places_cache.py:1-101`

**Why it matters to a real tester:** Without the cron actively running:
(a) the proactive refresh that warms tomorrow's trip venues doesn't fire, so
the first read of every venue is a cold-cache foreground fetch — fine for
correctness but a worst-case latency hit on the user's first scroll;
(b) `purge_stale_google_ids` never runs, so the Google ToS protection
disappears entirely (the 30-day clock starts at first dogfood traffic and
keeps running with no purger); (c) `purge_expired` never runs, so
`place_status_cache` grows unbounded. None of this breaks tomorrow but it all
quietly compounds. The dogfood-readiness doc already calls out that release
backend hosts aren't reachable (P0 in `dogfood-readiness.md`) — until an ops
host exists, the cron lines in CLAUDE.md are aspirational documentation, not
running code.

**Repro / deterministic test idea:** N/A — this is a deployment gap, not a code
defect. Verify by checking deployed cron tab / scheduled tasks once an ops
host is up. If there's no entry calling
`python scripts/purge_places_cache.py`, the gap is live.

**Suggested fix direction:** Bundle the two cron lines into the same
`docs/Deploy & Rollback Runbook.md` checklist that gates dogfood backend
deployment. Add a `make places-cron-check` target that hits a `/admin/cron`
endpoint or reads `place_provider_calls`'s most recent row and warns if no
purge job has run in N days. Lightweight alternative: extend
`scripts/check_quality_drift.py` (already daily) to also assert
`max(place_status_cache.expires_at) - now() < N days`, so a missed purge
shows up in the daily Slack post.

**Confidence:** High (the cron isn't wired by default; the only mitigation is
the operator remembering to add it).

---

### P2 — `_check_grounding` is heuristic and has no link to live venue closure / Postgres existence
**References:**
- `Travel Agent/backend/concierge/output_guards.py:1012-1052`
  (`_check_grounding` matches title-case phrases against allowed names)
- `Travel Agent/backend/concierge/output_guards.py:1093-1098` (allowed set
  comes from tool calls + itinerary + user message)
- `Travel Agent/CLAUDE.md:123-148` (default mode is `log` — violations
  recorded but reply ships)

**Why it matters to a real tester:** The grounding guard is the last line of
defense against "agent recommends a closed/non-existent venue", but it
only catches the case where the agent invents a name that doesn't appear
anywhere in tool output. It does NOT verify that the venue's `venue_id`
in the tool output corresponds to a row in `venues` (relevant if a venue
was deleted post-brief-write), nor that the venue is operationally open
per `place_status_cache.permanently_closed` (interlocks with P1-1 above).
Default `log` mode means violations are observed, not blocked — fine for
calibration, but if P1-1 surfaces a closed venue the guard won't catch it
because the closed venue's name IS in the tool output (it's a real Qdrant
brief).

**Repro / deterministic test idea:** Compose a reply that names "Roberta's"
when the venue exists in fixtures and `place_status_cache` says
`permanently_closed=true`. `_check_grounding` returns 0 violations.

**Suggested fix direction:** Add a second guard `_check_operationally_open`
that takes the venue_ids from `tool_calls` and consults
`place_status_cache.permanently_closed` (single batched read) — flag any
reply that names a closed venue as a `closure_leak` violation. Cheaper
than re-running grounding and orthogonal to title-case matching. Or fold
the closure filter into fan-out (P1-1 fix) and treat the guard as the
defense-in-depth backstop.

**Confidence:** Medium (the issue is real but downstream of P1-1; fixing P1-1
significantly reduces blast radius).

---

### P2 — `_resolve_destination_id` in Viator pages `/destinations` without retry/timeout discipline
**References:**
- `Travel Agent/backend/booking_agent/providers/viator.py:60-89` (raw httpx GET
  inside helper; only the parent `search` has `@with_circuit_breaker` +
  `@retry_with_backoff`)
- `Travel Agent/backend/booking_agent/providers/viator.py:77-82` (swallows
  `httpx.HTTPError` → returns None → "no Viator results for this destination")

**Why it matters to a real tester:** A Viator search needs to resolve a city
name ("Lisbon") to a numeric `destinationId` first via a `/destinations`
fetch. The result is cached in a process-local class-var dict
(`_destinations_by_name`) so the call only fires on the first miss per
process — but a cold-process or restart triggers it. If the call fails
transiently, the helper silently returns None and the parent `search`
returns `[]`. From the user's perspective: Viator activities disappear for
that turn. There's no retry, no backoff, no telemetry. The parent's
breaker only counts the parent `search` call as a failure if the
`httpx.HTTPError` raised — but here it's caught and swallowed, so the
breaker stays closed and the next user hits the same failure mode.

**Repro / deterministic test idea:** Patch the `/destinations` response to
500 once; observe Viator returns no results without any retry attempt and
without recording a breaker failure.

**Suggested fix direction:** Either bubble the `httpx.HTTPError` so the
parent's `@retry_with_backoff(max_retries=2)` retries the whole search, or
add explicit retry+timeout inside `_resolve_destination_id` (the call is
cheap to retry — destination list is static-ish). Add a `logger.warning`
on the failure path so operators see when this is happening.

**Confidence:** Medium (Viator activities are deep-link-only in our flow
and missing them isn't a user catastrophe, but it's silent failure that
hides from the breaker).

---

### TECH-DEBT — Inconsistent decorator order (`@retry_with_backoff` vs `@with_circuit_breaker`) across providers
**References:**
- `Travel Agent/backend/places/google_places.py:87-129` —
  `@retry_with_backoff() / @with_circuit_breaker` (retry is OUTER)
- `Travel Agent/backend/places/foursquare.py:60-101` — same order as
  google_places
- `Travel Agent/backend/booking_agent/providers/viator.py:91-92` —
  `@with_circuit_breaker / @retry_with_backoff` (breaker is OUTER)
- `Travel Agent/backend/booking_agent/providers/duffel.py:43-44` — breaker outer
- `Travel Agent/backend/booking_agent/providers/amadeus_flights.py:66-67` —
  breaker outer
- `Travel Agent/backend/booking_agent/providers/restaurant.py:36-37` — breaker
  outer

**Why it matters:** The two orderings have different failure semantics. With
breaker outer (booking providers), the circuit is checked once, then
internal retries happen; a single user-facing call counts as a single
breaker event. With retry outer (places providers), each retry attempt
re-enters the breaker, and an OPEN circuit raises `ProviderUnavailable`
inside the retry — which is NOT in `TRANSIENT_EXCEPTIONS`, so the retry
loop won't catch it; the function still fails fast. But repeated
record_failure calls from the same logical user request can trip the
breaker faster than intended. Not a dogfood-blocking bug, but worth
documenting + standardizing before more providers land.

**Suggested fix direction:** Pick one canonical order
(`@with_circuit_breaker` outer is more conventional — "is the circuit
open? if not, do work with retries") and apply it consistently. Add a
docstring on `core/resilience.py` or `booking_agent/providers/resilience.py`
documenting the expected stacking.

**Confidence:** Medium.

---

### TECH-DEBT — `BookingProvider.timeout_seconds` defaults to 30s; consider tightening for dogfood
**References:**
- `Travel Agent/backend/booking_agent/providers/base.py:32` (`timeout_seconds: int = 30`)
- `Travel Agent/backend/places/base.py:31` (`timeout_seconds: int = 10` —
  much tighter for places, "operational lookups must be fast")

**Why it matters:** A 30s timeout on a flight/hotel search is borderline
acceptable for L1 deep-link flows but is generous for user-perceived
latency. Combined with `@retry_with_backoff(max_retries=2)`, a hung
provider can hold the booking dispatcher's task for ~90s before the slot
opens up — and the dispatcher batch size is only 5
(`session_dispatcher.py:27`). Five hung calls = no booking traffic for
90s. The places subsystem chose 10s for exactly this reason.

**Suggested fix direction:** Drop default to 15s for booking providers
(or per-provider — Amadeus needs more headroom than Duffel). Make the
value an env var so an outage can be ridden out without a deploy.

**Confidence:** Low (no concrete user incident; relies on judgment about
acceptable dogfood latency budgets).

---

### TECH-DEBT — Briefs can outlive their Postgres venue (no Qdrant-sync on venue delete)
**References:**
- `Travel Agent/backend/core/vector/briefs.py:543-558` (`delete_brief` exists
  but no caller in `entities.py` / venue-delete paths)
- `Travel Agent/backend/planning_agent/fan_out_search.py:559-580`
  (`RestaurantSearchResult` is built entirely from Qdrant payload — no
  cross-check that `venues.id` still exists)

**Why it matters:** If a venue is ever hard-deleted from Postgres (today
"never" for dogfood, but the schema doesn't prevent it), its Qdrant
brief stays. The next fan-out surfaces the deleted venue with its full
brief payload. Constraint/distance lookups would silently fail
(returning `{}` per `_enrich_results_async`'s null-tolerant code path)
and the result would pass through.

**Suggested fix direction:** Wire a venue-delete hook that calls
`delete_brief(point_id)` (the venue→point_id mapping exists in
`brief_state` per the briefs.py comment). Or run a weekly
reconciliation job (`scripts/audit_brief_orphans.py`) that lists Qdrant
brief venue_ids missing from `venues` and emits them for cleanup. Low
urgency until a real venue gets deleted.

**Confidence:** Low (no current delete path in production).

---

## Positive Signals

- **Auto-charge is provably impossible.** `create_order` is `NotImplementedError`
  in the base and **zero** subclass overrides exist; deep-link offers are filtered
  out of L3 cart; seed offers persist as `available` not `selected`.
- **Viator is correctly filtered out of any auto-cart path** via the
  `booking_method == "deep_link"` check in `auto_select_best`
  (`booking_graph.py:399-401`) and via `capability.api_bookable=False` for
  activity category (`capability.py:231`).
- **Venues router is registered** (`router_registry.py:53, 108`); the earlier
  404 is closed.
- **Fan-out search is fault-tolerant.** `_parallel_searches` uses
  `return_exceptions=True` so a single Qdrant lane failure doesn't abort the
  whole search (`fan_out_search.py:288-305`).
- **Trip-scope (`place_ids`) filtering is correct end-to-end.** Production
  briefs carry `place_id` in payload (`payload_builders.py:64`); the filter is
  applied in `_build_venue_filter` (`briefs.py:279-285`) and is mutex with
  `city` to avoid double-scoping.
- **`eval_world` namespace pin works correctly** for the eval framework
  (`fan_out_search.py:657-658`, `briefs.py:273-277`).
- **Empty-result diagnostic is well-built.** `_explain_empty_fan_out` enumerates
  the binding filters most likely to be over-narrowing
  (`fan_out_search.py:202-259`), avoiding the "agent burns retries on
  no-results" trap.
- **Places provider chain is correctly metered.** `_get_status_metered` and
  `_find_place_metered` each call `can_call` before the request, and
  `record_call` after (success or failure both count toward the daily limit per
  `places.budget`).
- **Negative cache + per-field TTLs + SWR + bounded background refresh** are
  well-architected; `_BG_REFRESH_CONCURRENCY=10` semaphore +
  `_BG_REFRESH_TIMEOUT_SECONDS=30` prevent runaway fan-in
  (`places/linker.py:48-114`).
- **Indirect-prompt-injection scan on retrieved briefs** runs by default
  (`fan_out_search.py:120-122, 384-431`), redacting on detection, fail-open on
  classifier error.
- **Seeding LLM budget cap is correctly per-job (context-var scoped), not
  per-process.** The audit-v4 fix (`pipeline/llm.py:53-156`) prevents the
  multi-city batch from getting a `8000×N` budget by accident.

---

## Known / Accepted

These were verified during the audit and confirmed to be either intentionally
deferred per `docs/working/Known Gaps Register.md` or accepted design tradeoffs
— **do not re-file**:

- **O-14 (places cache refresh strategy)** — All 4 phases shipped 2026-05-17.
  Cron wiring is operator-side per the gap entry; surfaced as P2 above with
  the deployment-gap framing the gap entry already documents.
- **O-13 (Amadeus live-booking canary unactivated)** — Confirmed the canary
  scaffold exists at `tests/booking/test_amadeus_flights_live.py` and CI
  workflow `.github/workflows/live-booking-canary.yml` is wired but
  green-skipped until Amadeus secrets land. The "no provider API booking is
  live" property in the audit summary depends on this staying skipped for
  dogfood.
- **R-1 (Cohere reranker not active)** — Confirmed the
  `is_reranker_active()` short-circuit and graceful RRF fallback in
  `fan_out_search.py:333-358`. Expected.
- **R-4 (Behavioral score payload fields)** — Confirmed `update_brief_payload`
  has no callers; the live tiebreaker reads `venue_ratings` Postgres table
  instead (`fan_out_search.py:_ranking_sort_key`).
- **TR-1 (`search_transport` skeleton — live calls gated off)** — Confirmed,
  out of scope for this area.
- **S-5 (venue allergen enforcement — only gluten filterable)** — Confirmed,
  noted as documented gap, out of scope for this area.
- **Booking auto-charge: deferred-by-design.** `create_order` is intentionally
  `NotImplementedError`; capability.py:111-113 documents the
  `_API_CAPABLE_PROVIDERS` set as aspirational. The combination is the
  dogfood-safe state.
