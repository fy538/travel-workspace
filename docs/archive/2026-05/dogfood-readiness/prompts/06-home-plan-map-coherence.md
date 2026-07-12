# Prompt 06 — Home, Plan, And Map Coherence

```text
You are a Cursor Cloud agent auditing Travel Workspace for dogfood readiness.

Use the common rules in:
docs/audits/dogfood-readiness-2026-05/prompts/00-common-instructions.md

Area:
Trip Home, Plan, Map, and cross-surface read-model coherence.

Output:
docs/audits/dogfood-readiness-2026-05/areas/06-home-plan-map-coherence.md

Product promise:
The same trip state should appear consistently across Home, Plan, Map, Chat, and notifications. A tester should never wonder which surface is telling the truth.

Inspect:
- Travel Agent home feed/card generation, itinerary API, plan-state API, map-state API.
- Cache keys, dismissal lifecycle, tiering, critical card behavior.
- Travel App trip home, plan v2, map v2, data hooks, cache invalidation after mutations.

Start with:
- docs/reliability/traces/home-plan-map-coherence.md
- Travel App/docs/page-specs/trip-page.md
- Travel App/docs/page-specs/trip-plan-v2.md
- Travel App/docs/page-specs/trip-map-v2.md
- Travel Agent/tests/api/test_home.py
- Travel Agent/tests/api/test_home_group_invites.py
- Travel App/__tests__/utils/tripMapStateParity.test.ts

Audit questions:
1. Do Home cards, Plan blocks, Map pins, and proposal affected IDs share stable identifiers?
2. Can dismissed cards hide critical state forever?
3. Are unplaced items and null coordinates handled without crashes?
4. Are read models computed off the event loop where needed?
5. Do mutations invalidate all affected surfaces?
6. Do mock fixtures cover realistic sparse/empty/half-baked trips?
7. Are during-trip vs pre-trip vs post-trip defaults coherent?

Run if cheap:
- make golden-path-qa
- targeted home/plan/map tests

Deliver:
Find cross-surface contradictions and stale-cache paths. Include a minimal state_before/action/state_after trace for each major finding.
```
