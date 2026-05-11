# Golden Path Traces

These traces turn the product vision into inspectable reliability artifacts.
They are not live evals. They describe the expected state transitions, API/tool
calls, and invariants that deterministic tests or agent-assisted review should
protect.

Start here when asking Codex or Claude Code to audit a journey:

1. Read the relevant trace.
2. Inspect the current backend route/model, app hook, and mock data anchors.
3. Add or update deterministic tests for one missing invariant.
4. Run `make golden-path-qa` or the smallest targeted command.

## Traces

- [Create Trip And Invite Group](./create-trip-and-invite-group.md)
- [Private Input To Group-Safe Context](./private-input-to-group-safe-context.md)
- [Proposal Review And Plan Mutation](./proposal-review-and-plan-mutation.md)
- [Home, Plan, And Map Coherence](./home-plan-map-coherence.md)
- [Notifications And Proactive Help](./notifications-and-proactive-help.md)
- [Memory And Post-Trip Loop](./memory-and-post-trip-loop.md)
