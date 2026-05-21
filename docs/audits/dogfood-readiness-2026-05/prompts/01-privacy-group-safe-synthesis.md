# Prompt 01 — Privacy And Group-Safe Synthesis

```text
You are a Cursor Cloud agent auditing Travel Workspace for dogfood readiness.

Use the common rules in:
docs/audits/dogfood-readiness-2026-05/prompts/00-common-instructions.md

Area:
Privacy and group-safe synthesis.

Output:
docs/audits/dogfood-readiness-2026-05/areas/01-privacy-group-safe-synthesis.md

Product promise:
Travelers can share private constraints, budget pressure, medical/accessibility/dietary needs, pace, and social concerns. The concierge may use those signals internally, but group-facing surfaces must not expose who said what or leak sensitive phrasing.

Inspect:
- Travel Agent concierge prompts, guardrails, output checks, and tool handlers.
- Preference engine observation/privacy tags, Personal Memory synthesis, group profile synthesis.
- Proposal creation and group message composition.
- Notification/feed/home surfaces that summarize private inputs.
- Travel App privacy audit screen, invite intake, group chat, proposal cards, notifications, trip info.

Start with:
- docs/reliability/traces/private-input-to-group-safe-context.md
- Travel Agent/docs/product/Product Architecture Principles.md
- Travel Agent/docs/product/Interaction Design and Social Dynamics.md
- Travel Agent/tests/eval/test_concierge_checks.py
- Travel Agent/tests/eval/test_planning_checks.py
- Travel App/__tests__/data/privacy.test.ts

Audit questions:
1. Where can private input enter before auth, during invite intake, in chat, in profile/memory, or through photos?
2. Which payloads become visible to organizer, group chat, Home, Plan, Map, notifications, or public/social surfaces?
3. Are privacy tiers explicit at every write path, or inferred later?
4. Do tests use realistic sensitive phrases such as budget, medical, accessibility, family conflict, dietary, and pace?
5. Are privacy audit surfaces honest about what was used without exposing third-party private facts?
6. Are logs, events, analytics, and debug traces redacted?

Run if cheap:
- make contract-check
- targeted backend privacy/eval tests
- targeted frontend privacy tests

Deliver:
Find confirmed leaks first. Then list suspected leak vectors and missing regression tests. Include exact file/line references and one deterministic private-phrase test proposal per P0/P1.
```

