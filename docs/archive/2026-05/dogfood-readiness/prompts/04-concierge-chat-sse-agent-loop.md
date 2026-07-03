# Prompt 04 — Concierge Chat, SSE, And Agent Tool Loop

```text
You are a Cursor Cloud agent auditing Travel Workspace for dogfood readiness.

Use the common rules in:
docs/audits/dogfood-readiness-2026-05/prompts/00-common-instructions.md

Area:
Concierge chat, SSE streaming, tool loop, tool validation, retry/stop/recovery.

Output:
docs/audits/dogfood-readiness-2026-05/areas/04-concierge-chat-sse-agent-loop.md

Product promise:
The concierge can hold a reliable trip-aware conversation, stream useful progress, use tools safely, recover from errors, and avoid silent failure or infinite cost loops.

Inspect:
- Travel Agent concierge agent loop, tool handlers, message persistence, SSE routes, output guards, replay mode.
- Shared agent_loop, LLM wrappers, model registry, token/cost caps.
- Tool input/output validators and tool status labels.
- Travel App chat hooks, SSE parser, retry/stop behavior, 401 redirect, tool-status UI, group chat rendering.

Start with:
- Travel Agent/backend/concierge/FEATURE.md
- Travel Agent/docs/architecture/Conversation System Architecture.md
- Travel Agent/docs/operations/Replay Handle Turn Runbook.md
- Travel App/docs/page-specs/agent-chat.md
- Travel App/docs/design-decisions/agent-chat.md
- Travel App/hooks/useConciergeChat.ts

Audit questions:
1. Can a failed or malformed tool call leak raw errors or leave the UI hanging?
2. Are max-iteration, wallclock, token, and stop-button paths visible and recoverable?
3. Are SSE event names and payloads aligned between backend and frontend?
4. Are 401/expired auth events handled consistently for stream and upload paths?
5. Are tool status labels stable and not misleading?
6. Do group vs personal channel routes prevent cross-channel context leakage?
7. Does replay mode avoid side effects while preserving enough behavior for debugging?

Run if cheap:
- make contract-check
- targeted concierge/chat tests
- targeted frontend SSE/chat tests

Deliver:
Separate product-quality issues from reliability blockers. P0 only if a normal dogfood chat can hang, leak private context, silently fail, or burn uncontrolled cost.
```

