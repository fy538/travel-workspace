# Prompt 07 — Memory, Trip Story, Photos, And Post-Trip Loop

```text
You are a Cursor Cloud agent auditing Travel Workspace for dogfood readiness.

Use the common rules in:
docs/audits/dogfood-readiness-2026-05/prompts/00-common-instructions.md

Area:
Memory surfaces, Trip Story, photos, post-trip character read, retention/deletion.

Output:
docs/audits/dogfood-readiness-2026-05/areas/07-memory-trip-story-photos.md

Product promise:
The trip compounds into useful memory without feeling creepy, leaking private data, losing photos, or making false claims about edit preservation.

Inspect:
- Travel Agent memory APIs, post-trip tasks, trip story composer/regeneration, photo/media models, retention and RTBF cascade.
- Travel App Memory Home, Trip Story, story archive, Trip Log, photo album, consent/privacy controls, regenerate/edit/save/share flows.

Start with:
- docs/reliability/traces/memory-and-post-trip-loop.md
- Travel Agent/docs/product/Post-Trip Lifecycle.md
- Travel Agent/docs/product/MVP Social Loop.md
- Travel App/docs/Brief — Post-Trip Debrief.md
- Travel App/docs/Brief — Memory Surface.md
- Travel Agent/tests/tasks/test_post_trip_character_read.py
- Travel App/__tests__/data/memory.test.ts

Audit questions:
1. Can private or third-party facts appear in public/shared story artifacts?
2. Do photo privacy flags, GPS owner-only rules, and future-learning consent persist?
3. Does regeneration preserve user edits/photos as promised?
4. Does account deletion/RTBF purge authored events, photos, memory interactions, and derived story data?
5. Are post-trip background jobs idempotent and safe if retried?
6. Can users inspect, dispute, or retire remembered facts?
7. Do mock surfaces overstate what real backend data provides?

Run if cheap:
- targeted memory/story/photo tests
- make contract-check

Deliver:
Prioritize privacy, data loss, false UX promises, and post-trip job failures.
```

