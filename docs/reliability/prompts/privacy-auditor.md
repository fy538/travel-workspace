# Privacy Auditor Prompt

```text
You are auditing privacy reliability for Travel Workspace.

Do not call live LLMs or external APIs.
Do not use real user secrets or real private user data.

Target:
- Journey: [JOURNEY]
- Private phrase fixture: [PRIVATE_PHRASE]
- Group-facing surface: [CHAT_PROPOSAL_HOME_PLAN_OR_NOTIFICATION]

Audit goals:
1. Find where private context enters the system.
2. Find where group-facing output is composed.
3. Verify tests distinguish internal reasoning from group-visible copy.
4. Check privacy audit visibility for the owner.
5. Add a deterministic regression test only if a clear invariant is missing.

Required references:
- docs/reliability/traces/private-input-to-group-safe-context.md
- Travel Agent/tests/eval/test_concierge_checks.py
- Travel Agent/tests/eval/test_planning_checks.py
- Travel Agent/tests/eval/test_restaurant_checks.py
- Travel App/__tests__/data/privacy.test.ts

Pass condition:
- The private phrase may appear in owner-private context or internal fixtures.
- The private phrase must not appear in group-facing copy.
- The user can inspect privacy-relevant usage where the product claims they can.

Return:
- Surfaces inspected.
- Leak vectors found or ruled out.
- Tests added or recommended.
- Commands run and results.
```
