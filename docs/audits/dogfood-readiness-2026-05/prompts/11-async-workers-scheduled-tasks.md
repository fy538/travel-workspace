# Prompt 11 — Async Jobs, Workers, Scheduled Tasks, And Background LLM Loops

```text
You are a Cursor Cloud agent auditing Travel Workspace for dogfood readiness.

Use the common rules in:
docs/audits/dogfood-readiness-2026-05/prompts/00-common-instructions.md

Area:
Async jobs, arq worker, scheduled tasks, event subscribers, background LLM loops.

Output:
docs/audits/dogfood-readiness-2026-05/areas/11-async-workers-scheduled-tasks.md

Product promise:
Background work should improve the concierge without silently dropping jobs, blocking the event loop, running with stale module state, or burning uncontrolled LLM/API spend.

Inspect:
- Travel Agent backend/workers, tasks, lifecycle startup, scheduled tasks, event bus subscribers.
- arq/Redis dependencies, worker registration, dead-letter/error handling.
- Background LLM loops and DISABLE_LLM_BACKGROUND_LOOPS behavior.
- Sync DB calls inside async routes/jobs.
- Module-level mutable state in workers/scripts.

Start with:
- Travel Agent/docs/operations/Background LLM Loops.md
- Travel Agent/docs/operations/Offline First QA.md
- Travel Agent/docs/operations/Replay Handle Turn Runbook.md
- Travel Agent/backend/tasks/FEATURE.md
- Travel Agent/docs/working/Pre-Dogfood Audit Master Punch List v3.md if present

Audit questions:
1. Are all required subscribers imported in the worker process?
2. Can jobs be retried safely without duplicate notifications, stories, pushes, or plan mutations?
3. Are sync DB calls offloaded from async handlers?
4. Do scheduled tasks respect dogfood pause flags and budget gates?
5. Are background errors visible enough to debug but privacy-safe?
6. Does local/offline mode avoid live LLM/API calls by default?
7. Are worker dependencies present in deploy requirements?

Run if cheap:
- targeted worker/task tests
- static async/sync DB checks if available
- make doctor

Deliver:
Prioritize silent drops and production-only failures: worker does not boot, subscribers missing, jobs run forever, or background loops spend money unexpectedly.
```

