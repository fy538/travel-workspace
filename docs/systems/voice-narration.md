# Voice / Narration — System Charter

> Surface: Vesper
> Maturity (for MVP): Built-dark
> Status: dark
> Last updated: 2026-06-27

## Purpose
The audio companion — a real-time voice conversation with the concierge plus
persona-aware, geofenced narration on the ground. Serves belief #18 (*the audio
companion knows when to stop talking*). Deferred by design: it is **not** one of
the 12 wedge journeys. Two paths split sharply: the **narration text path ships**;
the **live mic path is dark**.

## Spans (cross-repo)
- Backend: [`travel-agent/backend/voice/`](../../travel-agent/backend/voice/FEATURE.md) — `worker.py` + `agent.py` (LiveKit cascading STT→LLM→TTS), `quota.py` (per-phase caps), `deferred_tool.py` (5s budget + graceful deferral), `metrics.py`. [`travel-agent/backend/guide/`](../../travel-agent/backend/guide/FEATURE.md) — `prerender.py` (audio cache pipeline), `subscribers.py`, `tts.py` (Cartesia); endpoints under `api/routes/narration.py`.
- Frontend: `useNarrationGeofence`, `useNarrationAudio` (the narration text/audio path, which ships); the live LiveKit mic UI (dark).
- Tables of record: `voice_quota_counters`, `voice_turn_metrics`, `narration_audio_cache`. Narrated-stop flag derives from `messages` (`message_type='narration'`).

## Public interface (what other systems may call / read)
- **Inbound (narration, ships):** `GET /api/trips/{trip_id}/narration/stops` (geofence metadata; `narrated` derives from `message_type='narration'`) · `GET /api/trips/{trip_id}/narration/audio/{entity_type}/{entity_id}` (pre-rendered MP3 or 404).
- **Inbound (live mic, dark):** `api/routes/voice.py` (LiveKit token generation) → `worker.py` cascading session.
- **Entry points (internal):** `quota.check_quota` / `commit_quota` · `deferred_tool.run_with_budget` → `post_deferred_result`.
- **Consumes:** Concierge `session.send_message()` (non-streaming, `modality="voice"`, `CONCIERGE_VOICE` Haiku) · `core/personas.py` (TTS voice + destination personas) · `itinerary.committed` / `trip.phase_changed` (prerender triggers).
- **Never:** stream the voice reply to an SSE client — the voice reply goes to TTS, blocking `send_message()` is intentional.

## Owns (source of truth)
The voice quota counters, per-turn voice metrics, and the per-user narration audio
cache. It owns no conversation content — narration persists as `messages` rows
(`message_type='narration'`), owned by Concierge.

## Invariants (must always be true)
- **Knows when to stop talking (belief #18)** — the interrupt classifier (in `concierge/`) decides whether a VAD interrupt is substantive (pauses narration) or a backchannel (ignored); narration yields to the user.
- **Quota enforced at token issuance** — per `(user_id, trip_phase, day_utc)`; refusing a new session token is strictly better than degrading mid-call. Atomic Postgres upsert (`INSERT … ON CONFLICT … WHERE count < cap`) — multi-worker safe, survives restarts.
- **Deferred-tool budget = 5s** — a tool past the voice budget ends the turn with a deferral phrase and posts its result later to the user's personal trip conversation; no silent dead air past ~800ms.
- **Narration honesty** — the `narrated` flag is sourced from real `message_type='narration'` rows, not a fabricated session log (Phase-5 source-of-truth migration; `guide_sessions` dropped in Phase 6).

## Failure modes
- No LiveKit/Deepgram/Cartesia credentials → `voice_settings.is_configured` is false and the whole live subsystem is inert (the prod posture).
- Slow tool mid-call → deferral phrase + background completion → chat-message delivery; the call never blocks on dead air.
- Audio cache miss → narration endpoint returns 404; the FE falls back rather than fabricating audio.

## Maturity & validation
- Serves: deferred-by-design (not in the 12 journeys); the narration *text* path supports the ground experience adjacent to journey 08.
- **Dark posture:** the live mic path is gated off — in prod by the absence of LiveKit/Deepgram/Cartesia credentials (`is_configured`) **and** the voice process is commented out in `fly.toml` (no 3rd Fly process running). (The `VOICE_ENABLED` framing in older notes maps to this credential + process gate; the code has no such flag.)
- **Ships:** narration text generation + TTS prerender + the two `/narration` endpoints are live; narration persists as `message_type='narration'`.
- DoD state: quota concurrency + deferred-tool budget + narration source-of-truth tests ✅ · **on-device live mic / interrupt / barge-in walk ❌ · on-device audio QA ❌**.

## Canonical docs
- why → `product/Voice Canon.md` (belief #18 / #10) · what(be) → `backend/voice/FEATURE.md` · `backend/guide/FEATURE.md`.
- Tests: `tests/voice/*` (quota upsert, deferred budget), narration prerender + stops-endpoint tests.

## Open risks / known gaps
- The live-mic path is entirely unwalked on-device — interrupt classification, barge-in, and TTFT are the audit-bait when it's eventually un-darked (~$0.13–0.20/min).
- No on-device STT fallback — voice is unavailable offline (V-3).
- Lighting it up requires 6 Fly secrets + a 3rd Fly process + uncommenting `fly.toml`; until then narration ships but the conversation does not.
