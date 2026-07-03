# Area Audit: Performance, Observability, And Cost Controls

Date: 2026-05-21  
Agent: Claude Code (Sonnet) audit session — area 15  
Scope: `Travel Agent/backend/core/llm.py`, `backend/core/llm_client.py`, `backend/core/logging_config.py`, `backend/core/request_context.py`, `backend/core/db/_tables/telemetry.py`, `backend/core/db/_tables/conversations.py`, `backend/api/main.py` (health), `backend/api/routes/_message_flow.py`, `backend/concierge/session.py` + `output_guards.py`, `backend/core/agent_loop.py`, booking/places resilience, `backend/core/vector/`, `scripts/check_async_sync_db*`, `scripts/check_httpx_timeout.py`, both CI cron workflows; Travel App `utils/observability.ts`, `utils/sse.ts`, `hooks/useConciergeChat.ts`, `utils/gpsStream.ts`, `components/ui/AppImage.tsx`, list screens.  
Mode: Audit only. No product-code changes.

## Executive Summary

- Dogfood risk: **Low–Medium**
- Highest-risk finding: the shared Anthropic SDK clients are built with **no explicit `timeout=` / `max_retries=`** (`llm_client.py:44,63`), so any LLM call that is *not* wrapped by the route-layer 60s turn budget (background synthesis, digest, memory refresh, trip story, research) inherits the SDK's ~10-minute default and can wedge a worker + compound retries.
- Checks run:
  - `scripts/check_async_sync_db.py --ci` -> **pass** (472 sync symbols, 322 call sites, 240 baselined, 0 new, 0 stale)
  - `scripts/check_httpx_timeout.py` -> **pass** (0 backend httpx clients missing `timeout=`)
  - `make doctor` (workspace) -> **pass** (only local `uvicorn not found` warning)
- Residual uncertainty: I did not run Postgres/Qdrant-backed latency repros, did not exercise live LLM/provider calls, and did not open local trace files to confirm whether on-disk traces store raw prompt/reply content (flagged as a follow-up). Frontend references are from static reads, not a device profile.

This area is in good shape. The foreground concierge turn is bounded (60s budget + iteration cap), output-guarded *before* streaming, and richly instrumented (request_id, trace_id, latency_ms, tokens, guard_violations, source_type per turn). There is **no P0**. The findings are reliability-under-failure and cost-attribution gaps, plus one positive confirmation that the pre-dogfood cron/canary pause (audit Q7) is in place.

---

## Findings

### P2 — Shared Anthropic clients have no explicit timeout or retry cap (runaway cost / wedged worker)

Status: Confirmed (missing config); Suspected (impact, only under slow/stalled API responses)  
User impact: A background LLM job (digest, post-trip summary/reflection, memory refresh, trip-story compose, research) that hits a slow or stalled Anthropic response can hang for up to the SDK default (~600s) and, with SDK-level retries stacking on top of `call_llm`'s own retries, burn extra tokens before failing. Foreground chat is unaffected (it is cancelled by the 60s turn budget), so this shows up as delayed/duplicated background work and avoidable spend rather than a visible chat hang.  
Product promise affected: cost control, "no avoidable hangs"

References:

- `Travel Agent/backend/core/llm_client.py:44` — `Anthropic(**kwargs)` built with only `default_headers` (+ optional `api_key`); no `timeout=`, no `max_retries=`.
- `Travel Agent/backend/core/llm_client.py:63` — same for `AsyncAnthropic(**kwargs)`.
- `Travel Agent/backend/core/llm.py:393` — `call_llm` streaming path has its own `max_retries = 2` (stacks on the SDK's default of 2).
- `Travel Agent/backend/api/routes/_message_flow.py` (turn budget) — foreground turns are wrapped in `asyncio.timeout(turn_timeout_seconds≈60)`, which bounds the *chat* path only; non-turn `call_llm` callers have no equivalent wrapper.

Why it matters:

The only thing currently bounding an LLM call is the route-layer 60s `asyncio.timeout`. Every LLM call that does not flow through a concierge turn (all background/synthesis/digest/research paths) therefore relies on the Anthropic SDK default timeout (~10 min) and gets SDK retries it didn't ask for. During dogfood this is the difference between a background job that fails fast and one that pins an executor/worker thread for minutes while spending tokens.

Repro or deterministic test idea:

1. Patch the Anthropic async client's `messages.stream`/`create` to sleep well past 60s.
2. Invoke a background LLM path (e.g. `refresh_memory` / `compose_trip_story`) directly (not via a chat route).
3. Expected: the call aborts within a bounded timeout (e.g. 60–120s).
4. Current likely: it runs until the SDK's ~600s default elapses.

Suggested fix direction:

Pass an explicit `timeout=` (e.g. 60–120s) and `max_retries=0` when constructing the shared clients in `llm_client.py`, letting `call_llm` own retry policy. Optionally add a CI grep asserting the SDK clients are always constructed with a `timeout=`.

Related bug class: missing external-call timeout / unbounded background work

Confidence: High (config fact); Medium (impact)

---

### P2 — No absolute token/cost ceiling; runaway-spend control is time/iteration-based + a pause flag with known gaps (runaway cost)

Status: Confirmed  
User impact: Spend is bounded per-turn (60s budget, iteration cap → `error_state="budget_exhausted"`) and ambient loops are gated by `DISABLE_LLM_BACKGROUND_LOOPS`, but there is **no hard per-trip / per-user / per-day token or dollar ceiling** and no automatic alert when spend spikes. Detection during dogfood is manual (token tracker / `/debug/tokens` / dashboard). A misbehaving loop or an enthusiastic tester can accrue cost with no enforced cap.  
Product promise affected: cost control

References:

- `Travel Agent/backend/core/logging_config.py` (TokenTracker) — records per-call model/tokens/duration and computes cost from `MODEL_COSTS`, but totals are in-memory and reset on restart; no enforcement ceiling.
- `Travel Agent/backend/api/routes/_message_flow.py` — per-turn *time* budget (`turn_timeout_seconds`), not a token/cost budget.
- Cross-reference: **area 11 finding "Dogfood Pause Flag Misses Post-Trip LLM Work"** — `DISABLE_LLM_BACKGROUND_LOOPS=true` does not stop several post-trip LLM paths (`backend/api/lifecycle.py:251,256`), so the one operational "stop spending" switch is leaky.

Why it matters:

The runbooks treat `DISABLE_LLM_BACKGROUND_LOOPS` as the spend brake, but per area 11 it misses post-trip work, and there is no absolute backstop if a loop misbehaves. For ~10 dogfooders the expected volume is low, so this is not blocking — but it is the most likely "surprise on the Anthropic bill" vector.

Repro or deterministic test idea:

1. Confirm there is no code path that halts/declines LLM calls once a cumulative token/cost threshold is crossed (grep for a ceiling — none found beyond per-turn budgets).
2. Expected (desired): a daily token/cost ceiling or alert exists.
3. Current: only per-turn time/iteration bounds + the (leaky) background pause flag.

Suggested fix direction:

Add a lightweight cumulative daily token/cost ceiling (or at minimum a threshold alert wired to the dashboard), and close the area-11 pause-flag gap so a single switch reliably stops all autonomous LLM work in cheap/dogfood mode.

Related bug class: runaway cost / missing spend ceiling

Confidence: Medium

---

### P2 — Cost attribution is hard from the token log: no `source_type` and no per-call/per-turn `cost_usd` (missing debug signal)

Status: Confirmed  
User impact: Per-turn telemetry is strong, but the **LLM token log itself** does not record `source_type` (user-initiated vs proactive/background) and there is **no `cost_usd` column** — cost must be reconstructed at query time via `MODEL_COSTS`. Non-turn LLM calls (digest, synthesis, research) have no `source_type` anywhere. During a dogfood cost spike it is therefore slow to answer "which traffic class spent this."  
Product promise affected: cost observability

References:

- `Travel Agent/backend/core/logging_config.py` (TokenTracker.record) — logs model/input_tokens/output_tokens/duration_ms/request_id/prompt_id, but **not** `source_type` and no derived cost.
- `Travel Agent/backend/core/db/_tables/telemetry.py:104-106` — `concierge_turns` stores `input_tokens`, `output_tokens`, `latency_ms` but no `cost_usd` (cost is query-time only).
- `Travel Agent/backend/core/db/_tables/telemetry.py` (`source_type`) — present on `concierge_turns` (good for turns) but not propagated to the token log / non-turn calls.

Why it matters:

The per-turn record is excellent (`request_id`, `trace_id`, `latency_ms`, `guard_violations`, `iterations`, `error_state`, `source_type`). The gap is specifically cost slicing across *all* LLM traffic, including background. This is a debug-signal gap, not a correctness bug.

Suggested fix direction:

Thread `source_type` (or a coarse traffic-class tag) through `call_llm` into the token log, and consider a materialized `v_*_cost_summary` view (or a `cost_usd` column) so per-trip/per-day spend is a cheap query.

Related bug class: cost-attribution / observability gap

Confidence: High

---

### P3 — No circuit breaker on Qdrant, geocoding, or LLM calls (latency under dependency failure)

Status: Confirmed  
User impact: Booking and Places integrations have retry **and** circuit breakers; Qdrant vector search, Nominatim geocoding, and LLM calls have retries (or a timeout) but **no breaker**. During a sustained dependency outage, every venue-search/geocode turn pays full retry latency (e.g. Qdrant 5s timeout × attempts) before failing, instead of failing fast via an open breaker.  
Product promise affected: user-perceived latency under partial outage

References:

- `Travel Agent/backend/places/*` — `@retry_with_backoff()` + `@with_circuit_breaker` present (good).
- `Travel Agent/backend/core/vector/` (briefs/client) — bare `search()`/`upsert()` with a 5s timeout but no circuit breaker.
- `Travel Agent/backend/research_agent/tools/nominatim.py` — explicit per-call timeout + rate limiting, but no breaker; returns `None` on failure (graceful).
- `Travel Agent/backend/core/llm.py` — retries, no breaker (acceptable; the timeout fix above is the bigger lever).

Why it matters:

Low volume during dogfood makes this minor, but it is the cleanest "make a degraded turn feel slow" path. Adding the existing resilience decorators to Qdrant/geocoding would make outages fail fast.

Suggested fix direction:

Reuse `resilience.py`'s `@with_circuit_breaker` on the Qdrant client wrapper and the geocoding call; keep the graceful `None`/skip fallbacks.

Related bug class: missing circuit breaker / slow-fail under outage

Confidence: Medium

---

### P3 — No global request-timeout middleware (latency)

Status: Confirmed  
User impact: The chat/turn path is bounded by the 60s turn budget, and outbound clients have per-call timeouts, but there is no Starlette/FastAPI middleware bounding *total* request time for other routes. A pathological non-chat request relies on OS socket defaults.  
Product promise affected: no avoidable hangs (minor)

References:

- `Travel Agent/backend/api/` middleware — request-context/timing middleware present; no timeout middleware.
- `Travel Agent/backend/api/routes/_message_flow.py` — per-turn `asyncio.timeout` covers chat only.

Suggested fix direction:

Optional: add a coarse request-timeout middleware (e.g. 90–120s) as a backstop. Low priority for dogfood.

Related bug class: unbounded request

Confidence: Medium

---

### P3 — Frontend: real audio lifecycle not yet wired (forward-looking)

Status: Confirmed (by design — Phase 6b)  
User impact: None today (mock adapter). When the real `expo-audio`/native audio session lands, the `NarrationPlaybackAdapter.dispose()` + mic-session teardown must be called on unmount or it becomes a battery/memory leak.  
Product promise affected: mobile battery/memory (future)

References:

- `Travel App/utils/voice/narrationPlayback.ts:31-92` — adapter contract defines `dispose()` / `onPlaybackEnded` unsubscribe (mock implements it fully).
- `Travel App/utils/voice/micStateMachine.ts` — real provider deferred to Phase 6b skeleton.

Suggested fix direction:

When wiring real audio, add a teardown test asserting `dispose()` runs on unmount and the audio session category is reset after capture.

Related bug class: native lifecycle leak (future)

Confidence: High

---

## Non-Findings / Things Ruled Out

- **Request correlation is solid.** `backend/core/request_context.py` (contextvars: request_id/trip_id/session_id/user_id) → `RequestContextFilter` → `JSONFormatter` → also persisted on `concierge_turns.request_id`/`trace_id`. A slow/failed turn is traceable end-to-end.
- **SSE is sanitized before streaming, not after.** Output guards (`backend/concierge/session.py` guard/regenerate path → `output_guards.py`) run and can rewrite `result.reply` *before* `complete_agent_message()` and before the SSE pump in `backend/api/routes/_message_flow.py`. Violations recorded to `concierge_turns.guard_violations`.
- **Per-turn instrumentation is rich.** `latency_ms` (`agent_loop.py` monotonic clock → `telemetry.py:106`), input/output tokens, iterations, `error_state` (incl. `budget_exhausted`), `source_type`, `trace_id`, `session_id`, tool-call durations.
- **Health coverage is good.** `/health` (liveness), `/ready` (Postgres SELECT 1 + Qdrant `get_collections`), `/health/external` (Anthropic/Tavily/Redis), `/health/background-tasks` (`backend/api/main.py:104-291`).
- **`concierge_turns` and `user_events` are properly indexed** — *corrected an over-claim from sub-agent triage.* `idx_concierge_turns_trip_created`, `_origin_created`, `_created` (`telemetry.py:135-144`) and `idx_user_events_user_time (user_id, created_at desc)`, `_trip`, `_entity`, `_type` (`conversations.py:303-310`). Not a finding.
- **httpx timeouts: clean.** `check_httpx_timeout.py` → 0 backend clients missing `timeout=`; Qdrant client carries an explicit (configurable, ~5s) timeout; geocoding/Wikidata/TTS/webhooks all set timeouts.
- **Sync-DB-on-event-loop: clean ratchet.** 240 baselined, 0 new, 0 stale; remaining baselined entries are background/admin/telemetry paths (see area 11 for the post-trip subset).
- **Frontend perf hygiene is strong** (static read): `expo-image` with caching/transition (`components/ui/AppImage.tsx`), FlatList windowing + memoized `renderItem`/`keyExtractor` (chat, discover, stories), `React.memo` on `MessageBubble`; GPS is a singleton watcher that starts on first subscriber and tears down on the last (`utils/gpsStream.ts`), incl. AppState listener cleanup.
- **Sentry is privacy-safe.** Consent + DSN gated, no-op in dev/mock, `sendDefaultPii:false`, `beforeSend` scrubs user/IP/device, `tracesSampleRate:0`, plus a context PII scrubber (`Travel App/utils/observability.ts`).
- **Frontend loading/error states are bounded + retryable.** SSE has a 45s inactivity timeout and classifies 409/504 (`utils/sse.ts`); `useConciergeChat.ts` does bounded exponential backoff (~44s ceiling) with an idempotency key and ends in a `failed` state with a retry affordance — no infinite spinner.
- **Audit Q7 (canaries/scheduled workflows paused) — PASS.** `Travel Agent/.github/workflows/cron.yml:23` and `live-booking-canary.yml:25` have their `schedule:` blocks commented out (paused pre-dogfood; `workflow_dispatch` retained). Re-enable is documented in `OWNER-DEPLOY-CHECKLIST.md` §9.

## Suggested Follow-Up Checks

- Add `timeout=`/`max_retries=0` to the shared Anthropic clients (`llm_client.py`) and a CI grep asserting the SDK clients always carry a `timeout=` (mirrors `check_httpx_timeout.py` for the one HTTP client that check can't see).
- Add a deterministic test: a non-turn `call_llm` path aborts within a bounded timeout when the SDK stalls.
- Thread `source_type` through `call_llm` into the token log; consider a `v_cost_summary` view or `cost_usd` column for cheap per-trip/per-day spend queries.
- Add a cumulative daily token/cost ceiling or threshold alert; close the area-11 `DISABLE_LLM_BACKGROUND_LOOPS` post-trip gap so one switch reliably stops all autonomous LLM spend.
- Wrap the Qdrant client and geocoding call in the existing `@with_circuit_breaker`.
- Verify whether on-disk local trace files (`trace_id` linkage) store raw prompt/reply content; if so, gate them behind a dev-only flag to avoid private-data-at-rest during dogfood.
