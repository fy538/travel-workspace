# Prompt 03 — Trip Creation, Destination, And Place Identity

```text
You are a Cursor Cloud agent auditing Travel Workspace for dogfood readiness.

Use the common rules in:
docs/audits/dogfood-readiness-2026-05/prompts/00-common-instructions.md

Area:
Trip creation, current trip identity, destination/place persistence, plan-similar entry points.

Output:
docs/audits/dogfood-readiness-2026-05/areas/03-trip-creation-destination-identity.md

Product promise:
When a user starts or clones a trip from chat/discover/social/story, the destination and place identity persist into Trip Home, Chat, Plan, Map, For This Trip, content rails, and backend state after refetch.

Inspect:
- Travel Agent trip create/patch routes, place lookup, place_id resolution, membership add behavior.
- Travel Agent place models and import assumptions.
- Travel App TripContext, trip creation helpers, Discover plan-similar, social/story plan-similar, trip selection/current trip context.
- For This Trip preview and destination slug derivation.

Start with:
- docs/reliability/traces/home-plan-map-coherence.md
- Travel App/docs/page-specs/trip-page.md
- Travel App/docs/Brief - For This Trip.md
- Travel Agent/docs/architecture/Trip State Architecture.md
- Travel Agent/tests/api/test_trips_api.py
- Travel App/context/TripContext.tsx

Audit questions:
1. Are all trip creation entry points using one canonical persistence path?
2. Does destination survive backend refetch in real mode?
3. Does `place_id` resolution handle accents, city prefixes, and missing places safely?
4. Are orphan trips possible if membership creation fails?
5. Does current-trip context recover after app restart, auth detour, or notification tap?
6. Can mock mode hide missing destination/place fields?
7. Are generated types used for backend-shaped trip data?

Run if cheap:
- make contract-check
- make api-coverage-check
- targeted trip API tests
- targeted TripContext/data hook tests

Deliver:
Prioritize bugs that make a dogfood trip feel destinationless, disconnected from content, or routed to the wrong workspace.
```

