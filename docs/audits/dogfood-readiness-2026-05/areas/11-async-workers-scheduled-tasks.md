# Area Audit: Async Workers And Scheduled Tasks

Date: 2026-05-21  
Agent: Codex / Cursor Cloud audit session  
Scope: `Travel Agent/backend/api/lifecycle.py`, `backend/workers/`, `backend/core/job_queue.py`, `backend/core/event_bus.py`, `backend/core/event_subscribers.py`, `backend/core/scheduled_tasks.py`, post-trip/task subscribers, worker/task tests, operations docs listed in the prompt.  
Mode: Audit only. No product-code changes.

## Executive Summary

- Dogfood risk: Medium
- Highest-risk finding: `DISABLE_LLM_BACKGROUND_LOOPS=true` does not stop several post-trip background LLM paths, so cheap dogfood mode can still spend tokens when a trip completes.
- Checks run: `make doctor` -> pass with `uvicorn not found` warning; `PYTHONPATH=. python scripts/check_async_sync_db.py --ci` -> pass; targeted scheduled-task/subscriber pytest -> pass; targeted subscriber-registration pytest selector -> pass.
- Residual uncertainty: I did not run Postgres-backed scheduled-task crash/restart repros, arq workers against Redis, or any live LLM/provider calls.

## Findings

### P1 - Dogfood Pause Flag Misses Post-Trip LLM Work

Status: Confirmed  
User impact: A local or dogfood backend started in cheap mode can still generate post-trip summaries, reflections, debrief turns, memory refreshes, trip stories, pushes, and Curator Takes after a trip flips to `completed`. A dogfooder may see unexpected background spend even though the runbooks say credits are not burning.  
Product promise affected: offline-first QA, concierge trust, cost control

References:

- `Travel Agent/backend/api/lifecycle.py:206` - reads `DISABLE_LLM_BACKGROUND_LOOPS`.
- `Travel Agent/backend/api/lifecycle.py:266` - gates only selected loops behind the flag.
- `Travel Agent/backend/api/lifecycle.py:251` - `trip_completion` always runs.
- `Travel Agent/backend/api/lifecycle.py:256` - `scheduled_tasks` always runs.
- `Travel Agent/backend/tasks/trip_lifecycle.py:85` - completion task calls `update_trip(..., status="completed")`.
- `Travel Agent/backend/core/db/trips.py:187` - `trip.completed` emits on the status transition.
- `Travel Agent/backend/core/db/trips.py:198` - `_fire_post_trip_tasks()` runs on the same transition.
- `Travel Agent/backend/core/db/trips.py:219` - post-trip summary generation is scheduled.
- `Travel Agent/backend/core/db/trips.py:227` - post-trip reflection is scheduled.
- `Travel Agent/backend/concierge/post_trip_subscribers.py:145` - schedules the post-trip debrief task.
- `Travel Agent/backend/concierge/post_trip_memory_refresh.py:106` - schedules post-trip memory refresh.
- `Travel Agent/backend/tasks/trip_story_subscriber.py:142` - schedules trip-story prewarm.
- `Travel Agent/backend/tasks/trip_story.py:204` - trip-story composition calls `call_llm_json`.
- `Travel Agent/backend/concierge/refresh_memory.py:364` - memory refresh calls the LLM.
- `Travel Agent/docs/operations/E2E Dogfooding Runbook.md:11` - documents cheap dogfood mode as `DISABLE_LLM_BACKGROUND_LOOPS=true` with no credits burning.

Why it matters:

The flag is treated operationally as the dogfood pause switch for ambient LLM work, but the post-trip path sits outside the gated loop list. This is especially easy to trigger during dogfood because `trip_completion` drains all trips whose `end_date <= yesterday`, so a stale local seed trip can activate background LLM work five minutes after startup.

Repro or deterministic test idea:

1. In a test app lifespan, set `DISABLE_LLM_BACKGROUND_LOOPS=true`.
2. Patch `generate_trip_summary`, `run_reflection`, `compose_trip_story`, and `refresh_personal_memory` with no-call assertions.
3. Emit `trip.completed` or call `update_trip(..., status="completed")` for a trip that has members.
4. Expected: no LLM-bearing post-trip tasks are scheduled or dispatched while the pause flag is true.
5. Current observed from static trace: completion, scheduled tasks, and post-trip dispatchers are outside the pause gate.

Suggested fix direction:

Centralize an `llm_background_loops_enabled()` or `dogfood_background_llm_enabled()` helper and apply it at every autonomous post-trip entry point: `_fire_post_trip_tasks`, LLM-bearing `trip.completed` subscribers, and the scheduled-task dispatcher for LLM task kinds. Keep DB-only status transitions and cleanup running.

Related bug class:

Background LLM loop bypass / dogfood pause flag gap

Confidence: High

### P1 - Claimed Scheduled Tasks Can Stick Forever After A Crash

Status: Confirmed  
User impact: If the API process dies after claiming a due scheduled task but before `mark_done()` or `mark_failed()`, the row stays `status='claimed'` and is never selected again. The affected dogfooder silently misses delayed post-trip debriefs, trip story prewarms, memory refreshes, or transport nudges.  
Product promise affected: concierge trust, post-trip loop, plan/transport coherence

References:

- `Travel Agent/backend/core/scheduled_tasks.py:178` - `claim_due_tasks()` is the only due-task claimer.
- `Travel Agent/backend/core/scheduled_tasks.py:201` - claimer only selects `status == "pending"`.
- `Travel Agent/backend/core/scheduled_tasks.py:216` - rows are changed to `status="claimed"`.
- `Travel Agent/backend/core/scheduled_tasks.py:244` - success path marks done.
- `Travel Agent/backend/core/scheduled_tasks.py:256` - failure path marks failed or resets pending.
- `Travel Agent/backend/core/db/_tables/scheduled_tasks.py:39` - table stores `claimed_at`.
- `Travel Agent/backend/core/db/_tables/scheduled_tasks.py:49` - due index only covers pending rows.
- `Travel Agent/backend/api/lifecycle.py:488` - lifespan loop claims rows before dispatching handlers.

Why it matters:

The move from `asyncio.sleep(7200)` to durable rows fixes restart during the delay window, but not restart during the claim/dispatch window. Since delayed post-trip and transport work is user-visible and only scheduled once per `(task_kind, scope_id)`, a permanently claimed row is a silent drop.

Repro or deterministic test idea:

1. Insert a due scheduled task.
2. Call `claim_due_tasks()` and simulate process death before dispatch.
3. Start a fresh process and call `claim_due_tasks()` after a generous timeout.
4. Expected: stale claimed row is reclaimed or reset to pending.
5. Current observed from static trace: only pending rows are selected; there is no stale-claimed sweeper.

Suggested fix direction:

Add a stale-claim recovery path, either in `claim_due_tasks()` or a small reaper: rows with `status='claimed'` and old `claimed_at` should return to `pending` with a retry cooldown, or fail terminally after max attempts. Add a Postgres integration test for claim-then-restart.

Related bug class:

Durable scheduled task lost after claim / silent background drop

Confidence: High

### P2 - Some Scheduled LLM Handlers Still Run Sync DB On The Event Loop

Status: Confirmed  
User impact: When delayed post-trip tasks fire, sync SQLAlchemy calls run directly inside async handlers. During group post-trip fanout this can block the API event loop, making foreground chat, SSE, polling, or notification routes feel stuck while background work is doing DB reads.  
Product promise affected: app responsiveness, concierge trust

References:

- `Travel Agent/backend/tasks/trip_story_subscriber.py:82` - async scheduled-task handler.
- `Travel Agent/backend/tasks/trip_story_subscriber.py:102` - calls sync `get_trip_members()` directly.
- `Travel Agent/backend/tasks/trip_story_subscriber.py:69` - calls sync `get_latest_trip_story()` inside async member composition.
- `Travel Agent/backend/concierge/post_trip_subscribers.py:100` - async scheduled-task handler.
- `Travel Agent/backend/concierge/post_trip_subscribers.py:111` - calls sync `get_trip_members()` directly.
- `Travel Agent/backend/tasks/post_trip_character_read.py:153` - async character-read loop body.
- `Travel Agent/backend/tasks/post_trip_character_read.py:167` - calls sync `find_trips_ending_recently()` directly.
- `Travel Agent/backend/tasks/post_trip_character_read.py:179` - calls sync `get_trip_summary()` directly.
- `Travel Agent/backend/tasks/post_trip_character_read.py:186` - calls sync `get_trip_members()` directly.
- `Travel Agent/scripts/check_async_sync_db_baseline.tsv:123` - this class is currently baselined rather than failing CI.
- `Travel Agent/scripts/check_async_sync_db_baseline.tsv:237` - trip-story sync calls are also baselined.

Why it matters:

The project has already identified sync DB in async code as a recurring reliability class. These sites are not new according to the checker, but they are in the audited background-worker surface and can concentrate around exactly the dogfood moment when several delayed post-trip jobs wake up together.

Repro or deterministic test idea:

1. Patch `get_trip_members()` or `get_latest_trip_story()` to sleep for several seconds.
2. Run `_prewarm_trip_story()` or `_run_post_trip_debrief()` in an event loop next to a heartbeat coroutine.
3. Expected: heartbeat continues because DB work is offloaded.
4. Current likely: heartbeat pauses while the sync DB function runs.

Suggested fix direction:

Move sync DB reads in async scheduled-task handlers behind `asyncio.to_thread()` or `run_in_executor()`, then remove these rows from the async/sync DB baseline so regressions fail CI.

Related bug class:

Sync DB in event loop

Confidence: High

### P3 - Cross-Trip Thread Subscriber Is Not In The Canonical Registration Bundle

Status: Confirmed  
User impact: Cross-trip thread recomputation after `trip.completed` does not eagerly run in the FastAPI or worker startup bundle. Users can still get a lazy recompute when opening the cross-trip threads endpoint, but the proactive freshness promised by the subscriber module is silently absent.  
Product promise affected: post-trip memory loop, cross-trip personalization

References:

- `Travel Agent/backend/core/personalization/cross_trip_thread_subscriber.py:20` - doc says it is loaded by `backend/core/event_subscribers.py`.
- `Travel Agent/backend/core/personalization/cross_trip_thread_subscriber.py:112` - registers a `trip.completed` subscriber.
- `Travel Agent/backend/core/event_subscribers.py:48` - canonical subscriber list starts.
- `Travel Agent/backend/core/event_subscribers.py:58` - list ends without `backend.core.personalization.cross_trip_thread_subscriber`.
- `Travel Agent/tests/core/test_cross_trip_thread_subscriber.py:11` - tests the handler directly, not bundle registration.

Why it matters:

Subscriber registration is explicitly centralized so worker and API processes do not diverge. This module follows that contract in its docstring, but the bundle omits it. The result is not dogfood-blocking because the read path has a lazy staleness gate, but it is a quiet miss in the post-trip compounding loop.

Repro or deterministic test idea:

1. Clear the event bus subscribers.
2. Call `register_all_subscribers()`.
3. Assert that `trip.completed` includes `cross_trip_thread_subscriber._on_trip_completed`.
4. Current observed: `trip.completed` has four handlers from the bundle; the cross-trip handler is not among them.

Suggested fix direction:

Add `("backend.core.personalization.cross_trip_thread_subscriber", "register_all")` to `_SUBSCRIBER_HOOKS` and extend the registration test to enumerate every module with a `subscribe()` plus `register` or `register_all` hook.

Related bug class:

Subscriber registration drift / silent event no-op

Confidence: High

## Non-Findings / Things Ruled Out

- `arq==0.28.0`, `asyncpg==0.31.0`, and `redis==5.3.1` are present in `Travel Agent/requirements.txt`.
- `backend/workers/audio_jobs.py::WorkerSettings.functions` registers audio, research, OCR, and trip-story worker jobs, including `seed_city_full`, `answer_one_question`, and `compose_trip_story_job`.
- The previous "worker only imports research subscribers" issue appears mostly fixed by `backend.core.event_subscribers.register_all_subscribers()` being called from both FastAPI lifespan and the arq worker import path.
- `make doctor` completed successfully apart from a local `uvicorn not found` warning.
- `scripts/check_async_sync_db.py --ci` reported zero new async/sync DB violations and zero stale allowlist entries.
- Targeted scheduled-task and post-trip subscriber tests passed: `42 passed`.
- Targeted subscriber-registration selector passed: `7 passed, 7131 deselected`.

## Suggested Follow-Up Checks

- Add a deterministic pause-flag test asserting `DISABLE_LLM_BACKGROUND_LOOPS=true` suppresses all autonomous post-trip LLM paths, not only the named lifespan loops.
- Add a Postgres integration test for scheduled-task claim recovery after simulated process death.
- Add a subscriber-bundle completeness test that compares modules containing `subscribe()` and `register_all()` or `register()` against `_SUBSCRIBER_HOOKS`.
- Gradually remove post-trip task modules from `check_async_sync_db_baseline.tsv` after offloading their sync DB reads.
