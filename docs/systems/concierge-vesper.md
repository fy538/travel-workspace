# Concierge (Vesper) — System Charter

> Surface: Vesper
> Maturity (for MVP): MVP-required
> Status: wired (not yet validated end-to-end on-device against live backend)
> Last updated: 2026-06-27

## Purpose
The conversational spine of the product — a place-aware companion that chats, calls
tools, streams, captures memory, acts on the plan, and (Phase 1+) narrates on the
ground. Serves belief #0.5 (*the product is a concierge companion, not a planning
tool*).

## Spans (cross-repo)
- Backend: [`travel-agent/backend/concierge/`](../../travel-agent/backend/concierge/FEATURE.md) (96 files) — runs on the shared `core/agent_loop.py` (custom Anthropic tool_use loop, **not** LangGraph).
- Frontend: `travel-app/app/(tabs)/concierge/*`, `trips/[tripId]/chat`, `components/chat/*` (44), `hooks/useConciergeChat`, `useGroupChat`, `utils/sse.ts`.
- Tables of record: `conversations`, `conversation_participants`, `messages`, `concierge_turns` + reasoning/quality telemetry.

## Public interface (what other systems may call / read)
- **Inbound (FE → BE):** `POST /api/trips/{id}/messages` (blocking) · `/messages/stream` (SSE) · `POST /api/trips/{id}/concierge/narrate`.
- **Entry points (internal):** `session.py::ConciergeSession.send_message[_streaming]()`, `agent.py::handle_turn()`, `triggers.py::run_proactive_turn()` (the common path for all system-initiated messages).
- **Consumes:** Memory & Preference (`get_group_context`), Planning, Booking, Research, Places, Situation — **all via tool calls, never direct imports** (lazy cross-agent imports are the only exemption; see `CLAUDE.md`).
- **Never:** other systems must not compose group-bound text directly — `group_compose.py` is the only sanctioned path (it strips attribution).

## Owns (source of truth)
The conversation thread and turn telemetry. Personal/group memory is **owned by
Memory & Preference** — Concierge only reads it and emits observations.

## Invariants (must always be true)
- **Privacy egress:** never reveal an individual's private constraint to the group (belief #3/#8). All group-bound text flows through `group_compose.py`; free-text replies into a group conversation are **not delivered** under strict mode.
- **Grounding:** every recommendation is grounded in the knowledge base; output grounding guard runs on every reply (`output_guards.py`).
- **Fail-open context:** a single failed per-turn context loader returns empty, never aborts the turn (`turn_context.py`).
- **`<notes>` are stripped** from the user-visible reply before return.
- **Guardrail** runs on every user turn (prompt-injection→block, self-harm→988, abusive→block); skipped only for proactive turns.
- **Telemetry origin** is tagged on every `concierge_turns` row; eval/test/synthetic never pollute production dashboards or traces.

## Failure modes
- Tool error → structured feedback to the loop (classifier + retry budget), not a crash.
- Re-anchor at ~iteration 7 if the model loops without converging.
- Model/provider error → surfaced via `core/llm.py` retry/backoff; turn fails loud rather than fabricating.

## Maturity & validation
- Serves journeys: 01 (vague→shaped), 04 (private constraint→group-safe), 05 (propose→mutate), 07 (discover→contextual), 08 (live what-now).
- DoD state: backend replay tests ✅ · grounding/privacy guards ✅ · **mock-walk ❌ · Maestro on-device ❌ · live-walk ❌**.
- Dark/flagged: narration text ships (persists as `message_type='narration'`); the live mic path is dark — gated by absent voice credentials (`voice_settings.is_configured`) + the commented-out `voice` process in `fly.toml`, not a `VOICE_ENABLED` flag.

## Canonical docs
- why → `product/Concierge Behavior Spec.md` · how → `architecture/Conversation System Architecture.md` · what(be) → `backend/concierge/FEATURE.md` · what(fe) → `page-specs/agent-chat.md`.
- Tests: `tests/concierge/*`, eval `configs/` (~21 concierge scenarios) + CI replay baselines.

## Open risks / known gaps
- The privacy-egress invariant is the **unrecoverable-trust-event** risk — the highest-value thing to verify with a live group walk (journey 04).
- `conversation_locations` is a **phantom table** (reverted feature) — any query against it fails at runtime.
- Streaming SSE on RN uses a custom fetch parser (`utils/sse.ts`); the on-device streaming path is unvalidated.
