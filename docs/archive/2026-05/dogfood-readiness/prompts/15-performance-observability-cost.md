# Prompt 15 — Performance, Observability, And Cost Controls

```text
You are a Cursor Cloud agent auditing Travel Workspace for dogfood readiness.

Use the common rules in:
docs/audits/dogfood-readiness-2026-05/prompts/00-common-instructions.md

Area:
Performance, latency, observability, cost controls, logging/tracing hygiene.

Output:
docs/audits/dogfood-readiness-2026-05/areas/15-performance-observability-cost.md

Product promise:
Dogfooders should not experience avoidable hangs, runaway token spend, blank loading states, missing diagnostics, or privacy-leaking traces.

Inspect:
- Travel Agent LLM wrapper, token tracking, cost rollups, request_id/trace_id, SSE sanitization, health/external, slow turn metrics.
- Event loop blocking in hot routes, DB indexes, request timeouts, provider circuit breakers.
- Travel App performance work: images, memoization, GPS/audio lifecycle, Sentry consent, loading/error states.
- CI/pre-commit quality ratchets for recurring performance/cost bug classes.

Start with:
- Travel Agent/docs/operations/Background LLM Loops.md
- Travel Agent/docs/architecture/Event Bus.md
- Travel Agent/docs/architecture/Eval Harness System Design.md
- Travel App/docs/Mock vs Real Parity.md
- docs/reliability/Agent Reliability Playbook.md

Audit questions:
1. Are expensive model/provider calls centrally tracked with source_type, model role, token/cost, and request correlation?
2. Are hot endpoints avoiding sync DB on the event loop?
3. Are timeouts, circuit breakers, retries, and fallback behavior explicit for external calls?
4. Can slow or failed turns be debugged from logs without private-data leakage?
5. Are frontend loading/error states bounded and retryable?
6. Are image/audio/GPS lifecycles safe for mobile battery and memory?
7. Are live canaries and scheduled workflows paused or budgeted before dogfood?

Run if cheap:
- targeted observability/perf tests
- static async DB checks if available
- make doctor

Deliver:
Group findings by user-perceived latency, runaway cost, missing debug signal, and privacy/logging risk.
```

