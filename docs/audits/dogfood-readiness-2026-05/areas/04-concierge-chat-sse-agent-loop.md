# Area Audit: Concierge Chat, SSE, Agent Loop

Date: 2026-05-21  
Agent: Codex audit session  
Scope: `Travel Agent` concierge loop/session/SSE routes/tool dispatch/replay docs; `Travel App` concierge chat screen, `useConciergeChat`, SSE parser, upload auth paths; reliability and product docs listed in prompt.  
Mode: Audit only. No product-code changes.

## Executive Summary

- Dogfood risk: Medium
- Highest-risk finding: the app's normal SSE chat path bypasses the backend daily chat-token quota gate and commit path, leaving only per-minute rate limits and per-turn loop caps.
- Checks run: `make contract-check` -> pass; `PYTHONPATH=. pytest tests/api/test_message_flow.py tests/api/test_conversations_api.py -q -k 'stream or in_flight or metadata or timeout'` -> pass, 13 passed; `npm test -- --runTestsByPath __tests__/utils/sse.test.ts __tests__/hooks/useConciergeChatMidStreamFallback.test.tsx --runInBand` -> pass, 8 passed.
- Residual uncertainty: no live LLM/SSE end-to-end run was performed; group compose recovery quality and real mobile abort timing were assessed statically only.

## Findings

### P1 — Streaming Concierge Turns Bypass Daily Chat Quota

Status: Confirmed  
User impact: A normal dogfood user in the app can keep sending streamed concierge turns after the daily token budget should stop them. This is not an infinite loop by itself, but it weakens the main cost-control promise on the exact path mobile uses.  
Product promise affected: cost control / recovery / dogfood reliability

References:

- `Travel App/hooks/useConciergeChat.ts:489` — real-mode chat prefers `/api/conversations/{conversation_id}/messages/stream` when a personal conversation exists.
- `Travel Agent/backend/concierge/session.py:322` — non-streaming `send_message()` checks `check_chat_quota` before paying for the LLM call.
- `Travel Agent/backend/concierge/session.py:425` — non-streaming `send_message()` commits actual token spend with `commit_chat_quota`.
- `Travel Agent/backend/concierge/session.py:1060` — streaming `send_message_streaming()` runs guardrails, then resolves/persists the turn without the same quota check.
- `Travel Agent/backend/concierge/session.py:1199` — streaming completion persists the message and side effects, but has no matching `commit_chat_quota` call.

Why it matters:

The frontend's primary concierge surface is SSE. The non-streaming path has a thoughtful daily quota gate, but the streaming path skips both enforcement and accounting. Rate limits, turn timeouts, max iterations, and token caps still reduce blast radius, so this is not P0; however, a dogfood session can materially exceed the intended daily budget without a visible stop.

Repro or deterministic test idea:

1. Unit-test `ConciergeSession.send_message_streaming()` with `check_chat_quota` patched to return `allowed=False`.
2. Expected: no `handle_turn()` call, agent placeholder marked failed with `chat_quota_exhausted`, and SSE reports a recoverable quota error.
3. Current likely/observed: streaming code path never imports/checks `check_chat_quota`, so the turn proceeds.

Suggested fix direction:

Mirror the non-streaming quota gate and token-spend commit in `send_message_streaming()`. Keep cached idempotency replies exempt, and make the quota refusal produce the same failed placeholder/retry-visible state as other early refusals.

Related bug class:

streaming/non-streaming sibling inconsistency; cost-control gap

Confidence: High

### P2 — Personal Concierge Stream Silently Drops Images And Turn Metadata

Status: Confirmed  
User impact: In the current private concierge screen, sending an image or angle deep-link metadata can appear to work from the UI but the conversation-scoped backend request ignores those fields. A user asking "what is this menu?" or entering chat from an angle may get a generic answer because the agent never receives the image or `angle_id`.  
Product promise affected: trip-aware conversation / multimodal concierge trust

References:

- `Travel App/data/conversations.ts:75` — the app resolves a private 1:1 conversation for a trip.
- `Travel App/app/(tabs)/concierge/chat.tsx:132` — the chat screen passes that personal conversation id into `useConciergeChat`.
- `Travel App/hooks/useConciergeChat.ts:72` — the hook contract says `sendMessage` images trigger vision and metadata carries `angle_id`.
- `Travel App/hooks/useConciergeChat.ts:489` — when `conversationIdProp` is present, the hook posts to `/api/conversations/{conversation_id}/messages/stream`.
- `Travel App/hooks/useConciergeChat.ts:524` — the request body includes `images` and `metadata` when provided.
- `Travel Agent/backend/api/routes/conversations.py:135` — the conversation-scoped `SendMessageRequest` has `user_id`, `user_name`, `user_role`, `message`, `modality`, `trigger_agent`, and `location`, but no `images` or `metadata`.
- `Travel Agent/backend/api/routes/conversations.py:629` — the conversation-scoped stream call does not pass `images` or `turn_metadata` into `run_stream_turn`.
- `Travel Agent/backend/api/routes/chat.py:122` — the legacy trip-scoped request model does support `images`.
- `Travel Agent/backend/api/routes/chat.py:138` — the legacy trip-scoped request model does support per-turn `metadata`.

Why it matters:

This is a silent capability mismatch. The app routes the most important chat surface through the personal conversation endpoint, while the richer image/context contract exists only on the trip-scoped legacy endpoint. Silent dropped context is worse than a visible unsupported state because the concierge appears inattentive rather than unavailable.

Repro or deterministic test idea:

1. Add a conversation-stream API test that posts `{"images": [...], "metadata": {"angle_id": 123}}`.
2. Patch `get_or_create_session_for_conversation().send_message_streaming` and assert it receives `images` and `turn_metadata`.
3. Expected: both fields are forwarded.
4. Current likely/observed: Pydantic ignores the extra fields and the session receives neither.

Suggested fix direction:

Bring the conversation-scoped request model and `run_stream_turn` call to parity with the trip-scoped chat route, including `MessageImage`, `images`, and `metadata`. Add a generated-contract/pytest assertion so the two send models do not drift again.

Related bug class:

API sibling drift; silent context loss; mock-real drift

Confidence: High

### P2 — Token-Budget Early Exits Are Not Visible As Budget Exhaustion

Status: Confirmed  
User impact: If the shared agent loop terminates because `max_total_tokens_per_turn` is exceeded, the user and dogfood operators may see a normal-looking completion rather than a recoverable budget-exhausted state.  
Product promise affected: recovery / cost visibility / operator trust

References:

- `Travel Agent/backend/core/agent_loop.py:251` — the shared loop checks `max_total_tokens_per_turn`.
- `Travel Agent/backend/core/agent_loop.py:915` — on budget exceed, the loop sets `budget_exceeded=True` and `budget_exceeded_reason`.
- `Travel Agent/backend/concierge/agent.py:1002` — concierge opts into `max_total_tokens_per_turn`.
- `Travel Agent/backend/concierge/agent.py:1270` — concierge copies reply, iterations, hit-max flag, tokens, and latency into `TurnResult`, but not `budget_exceeded` or reason.
- `Travel Agent/backend/concierge/session.py:584` — persisted `error_state` only recognizes `composition_skipped`, `hit_max_iterations`, and `empty_reply`.
- `Travel Agent/backend/api/routes/_message_flow.py:259` — SSE metadata sends tokens/iterations/composition flags, but no budget-exhausted flag.

Why it matters:

The cost guard does stop further looping, which is good. The missing part is visibility and recoverability: max-iteration exhaustion is queryable and gets special handling, while token-budget exhaustion is flattened into an ordinary result. That makes it harder to diagnose expensive turns and harder for the UI to explain why Vesper stopped early.

Repro or deterministic test idea:

1. Unit-test `handle_turn()` with a fake loop result where `budget_exceeded=True`, `budget_exceeded_reason="tokens ..."` and `hit_max_iterations=False`.
2. Expected: `TurnResult` carries the budget flag/reason, telemetry `error_state="budget_exhausted"`, and SSE metadata includes a recoverable budget signal.
3. Current likely/observed: those fields are dropped.

Suggested fix direction:

Add budget-exhausted fields to `TurnResult`, copy them from `LoopResult`, persist them in `concierge_turns`, and include a small SSE metadata field. Treat this separately from `hit_max_iterations` so dashboards can distinguish loop-shape failures from prompt/context bloat.

Related bug class:

observability gap; cost-control state dropped at boundary

Confidence: High

## Non-Findings / Things Ruled Out

- Generic backend SSE exceptions are sanitized before reaching the client; targeted `test_message_flow.py` coverage passed.
- `in_flight` and timeout SSE events are aligned with frontend parser behavior; targeted backend and frontend tests passed.
- Stream and multipart upload 401 paths both retry once with a fresh token and then route through a shared sign-in redirect guard.
- Conversation and trip chat routes enforce actor/body user matching plus participant/trip membership before streaming.
- Replay mode has a real side-effect interceptor at `execute_concierge_tool()`, short-circuits background doc updates/inline judge paths, and tags replay telemetry as `origin='replay'`. Known caveat: production `result_preview` truncation can reduce replay fidelity, but that is documented in the runbook.
- Stuck message placeholders have a background reaper (`reap_stuck_messages`) that flips abandoned pending/streaming rows to failed after a cutoff.

## Suggested Follow-Up Checks

- Add a streaming quota regression test beside the non-streaming quota tests.
- Add a contract parity test for trip-scoped vs conversation-scoped chat request fields.
- Add a fake-loop unit test proving token-budget exhaustion survives into `TurnResult`, SSE metadata, and telemetry.
- Add one frontend hook test for image/metadata sends against a personal conversation URL.
