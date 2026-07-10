# Agent Reliability Playbook

This workspace should treat reliability as an offline-first operating system.
The goal is to use Codex and Claude Code to trace, review, and expand tests
without making every quality check depend on live LLM calls or API-token spend.

## Reliability Ladder

Run the cheapest deterministic checks first. Only run live LLM canaries after
the lower layers are green.

| Layer | Question | Workspace command |
| --- | --- | --- |
| Workspace health | Are both repos present and configured? | `make doctor` |
| Contract drift | Does the backend OpenAPI snapshot match app types? | `make contract-check` |
| Mock/real parity | Do mock and HTTP clients still satisfy one API surface? | `make mock-real-parity` |
| Golden path | Can the core MVP journeys run without backend or LLM calls? | `make golden-path-qa` |
| Offline QA | Do contract, backend, frontend, and golden-path checks pass together? | `make offline-qa` |
| Live canary | Do a few high-risk agent journeys work with real models? | Manual, tiny budget |

## Principles

- Prefer invariant tests over subjective evals. Assert privacy, state
  consistency, typed contracts, idempotency, and visible proposal state.
- Keep product LLM calls off by default in reliability runs.
- Use mock API mode for frontend journey testing:
  `EXPO_PUBLIC_USE_MOCK_API=true`.
- Use backend markers to skip infra and key-dependent tests:
  `not requires_postgres and not requires_api_keys`.
- Use Codex and Claude Code as test authors, trace readers, and reviewers,
  not as the only judge of whether output is good.
- Spend live API tokens only after deterministic checks have narrowed the
  likely failure surface.

## Agent Workflows

### Test Author

Use this when a feature feels fragile but you do not want to run live evals.

```text
You are adding deterministic reliability coverage for Travel Workspace.
Do not call external APIs or use live LLMs.
Run make contract-check and the smallest relevant existing test command.
Trace the code path for <feature>.
Add one regression test that asserts an invariant, not subjective quality.
Prefer backend fakes or frontend mock mode.
Report the exact invariant covered and the command that proves it.
```

### Reviewer

Use this before merging a cross-repo diff.

```text
You are reviewing Travel Workspace for reliability regressions.
Do not modify files.
Inspect backend, generated OpenAPI, frontend data hooks, mocks, and screens.
Focus on privacy leaks, mock/real drift, schema drift, hidden live API calls,
and Home/Plan/Map state incoherence.
Run make contract-check and targeted offline tests if dependencies are present.
Return findings first with file and line references.
```

### Trace Builder

Use this when the product behavior is hard to reason about from tests alone.

```text
You are building an offline trace for a Travel Workspace golden path.
Do not call live LLMs or external APIs.
Identify the backend models/routes, frontend hooks, mock data, and UI surfaces
involved in <journey>.
Write a short trace artifact showing state_before, action, tool_or_api_calls,
state_after, and invariants.
If a missing invariant is testable, add the smallest deterministic test.
```

## Live Canary Budget

Live model runs should be rare and explicit. A useful MVP canary set is:

- Private preference synthesis does not leak sensitive inputs into group copy.
- Group proposal creation produces a visible, reviewable change.
- Rejecting or modifying a proposal updates Plan and Home state.
- Location-aware recommendation cites current trip context.
- The concierge recovers gracefully when a tool returns no result.

Keep these canaries small. Five to ten cases is enough while the deterministic
ladder is still catching most regressions.

## What Reliability Means For MVP

For this product, reliability is not just "the agent gives a good answer."
The higher-risk failure mode is cross-surface incoherence:

- Home, Plan, Map, and Group Chat disagree about the same trip state.
- A private preference appears in group-facing copy.
- A proposal is created but not reviewable, reversible, or visible.
- Mock mode passes while real API types have drifted.
- Notifications or proactive cards reference stale or hidden state.

The workspace reliability layer should keep those failures cheap to catch.

## Related Artifacts

- [Canonical Journeys](../journeys/README.md)
- [Golden Path Traces](./traces/README.md)
- [Agent Prompt Templates](./prompts/README.md)
- [Tiny Live Canary Plan](./Live%20Canary%20Plan.md)
- [Reliability CI Plan](./CI%20Plan.md)
