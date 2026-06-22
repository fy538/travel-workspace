# Codebase Progress Investigation - 2026-06-21

Status: investigation note  
Scope: `/Users/feihuyan/travel-workspace`, especially `travel-agent`, `travel-app`, and workspace docs  
Method: git history, current docs, current code structure, reliability snapshot, and contract check

## Executive Read

The project has moved from "ambitious substrate" to "presentable product system." The most important accomplishment is not any single surface; it is that Vesper now has a coherent architecture for a travel concierge relationship: memory, place intelligence, group coordination, itinerary truth, Discover, Atlas, and consequence receipts are all connected by real backend and frontend contracts.

The product direction is also much sharper than it was at the start. The vision docs frame Vesper as a place-aware concierge companion with group travel as the launch wedge, not a generic AI trip planner. The recent engineering work increasingly matches that frame: Plan is becoming the structured truth of a trip, Discover is becoming the place-facing editorial surface, Atlas is becoming the memory/trust surface, and Vesper/Home/Chat are the relationship layer.

MVP progress is strong, but dogfood readiness is not the same as feature completeness. The canonical journey matrix still marks all 12 journeys as not dogfood-ready, mostly because live canaries, mock walks, and deterministic screen-level tests are incomplete. That is the right kind of conservatism. The system is feature-rich enough to present an MVP, but the next push should be narrow: prove a small canonical world end to end, close two itinerary/proposal backend holes, verify Atlas/Discover composition on device, and run the real canaries that turn confidence from "built" into "dogfoodable."

## Evidence Inventory

- Backend repo: `/Users/feihuyan/travel-workspace/travel-agent`
  - First commit: 2026-04-12
  - Current branch: `main`
  - Commits at final status check: 1407
  - Ahead of origin at final status check: 36
  - Working tree: dirty; uncommitted files changed during the investigation, so treat current status as active parallel work rather than committed history.
- Frontend repo: `/Users/feihuyan/travel-workspace/travel-app`
  - First commit: 2026-04-12
  - Current branch: `main`
  - Commits: 869
  - Ahead of origin: 21
  - Working tree: clean.
- Workspace repo: `/Users/feihuyan/travel-workspace`
  - First commit: 2026-05-01
  - Current branch: `main`
  - Commits: 128
  - Ahead of origin: 6
  - Working tree: untracked `wt-edit-preview/` and `wt-guard/`.
- Reliability snapshot:
  - OpenAPI snapshot: 295 paths, 330 operations, 542 schemas.
  - Backend pytest files: 632.
  - Frontend test files: 240.
- Verification run:
  - `make contract-check` passed on 2026-06-21.

## Day-by-Day Accomplishment Timeline

Dates not listed had no local commits in the three repos I inspected.

| Date | What got accomplished |
|---|---|
| 2026-04-12 | Initialized both repos. Backend landed the first travel-agent backend/tools/docs, early memory consolidation, and expense foundations. App scaffolded Expo navigation, design system, and mock screens. |
| 2026-04-13 | Backend explored events, preference, and signal-deprecation thinking. App did an early broad follow-up pass. |
| 2026-04-14 | Backend built early content knowledge graph, BFS research, and agent cleanup foundations. |
| 2026-04-15 | Backend added seeding and notebook setup. |
| 2026-04-16 | Backend expanded notifications and tour/location-adjacent thinking. |
| 2026-04-17 | Backend made a big platform leap: Discover/editorial collections, eval tooling, API coverage, research tracing, brief regeneration, Alembic repair, and early UX exploration. |
| 2026-04-18 | Backend and app both shifted toward real dogfood: dev flags, real API mode, Clerk auth, SKIP_AUTH bypass, data-layer bug fixes, seeding hardening, and frontend real-API bug fixes. |
| 2026-04-19 | Backend focused on seed data, venue quality, booking/push/location, and backfill cleanup. |
| 2026-04-20 | Backend built location context agent and cleanup. |
| 2026-04-24 | Backend continued backfill work. |
| 2026-04-25 | Backend attacked agent reliability: Brooklyn concierge evals, privacy checks, group-compose leak fixes, recovery loops, booking urgency, and MCP personal-channel evals. |
| 2026-04-26 | Backend expanded eval portfolios across planning/restaurant/concierge, fixed retrieval/tool issues, added namespace filtering, and tuned anti-confabulation/time-window behavior. |
| 2026-04-27 | Backend added preference display names, handoff evals, concerts/nightlife skills, and research/brief regression guards. App removed mock bleeding and began Discover component extraction. |
| 2026-04-30 | Backend refactored concierge tool handlers and fixed tests/booking headers. App wired plan/journal/proposal/venue actions and fixed chat/proposal component structure. |
| 2026-05-01 | Backend added real itinerary coordinates, digest endpoint, OpenAPI MCP tool, and route cleanup. App wired mock-only hooks to real backend data, added Zod/test/CI scaffolding, and improved QA. Workspace coordination repo began. |
| 2026-05-02 | Backend added insight/For You/trip-highlight endpoints, pin_experience, SSE tool status, social intent state, and synthesis eval. App wired those endpoints, Events tab, API error visibility, and hook tests. |
| 2026-05-03 | Huge full-stack expansion: backend added guide agent, trust-layer recommendations, opinionated index, photos, summary endpoints, post-trip subscriber, and many review fixes. App added streaming group chat, invite landing, expenses CRUD, experience blocks, Discover angles/search, notifications, guide/place screens, daily digest, and generated schema sync. |
| 2026-05-04 | Backend built guide streaming/TTS, narration pre-render, outcome tracking, tests, and dead-code cleanup. App wired notification response tracking and guide SSE. |
| 2026-05-05 | Backend added onboarding intake, skill registry, SendGrid invites, Voice Guide phases, named personas, geofence stops, tool extraction, and many reliability fixes. App built immersive guide/audio and guide persona/geofence UI. |
| 2026-05-06 | App added accommodations, follow/booking/member APIs, member role UI, conversation creation, and accommodation CRUD. |
| 2026-05-08 | Backend and app connected taste DNA, Discover loop, post-trip/memory beginnings, invites, proactive notifications, and personal memory surfaces. |
| 2026-05-09 | Major hardening day. Backend added voice-guide foundation, invite push/SMS, TTFT telemetry, vision history, red-team/retrieval evals, type/mypy cleanup to zero, For You entity model, and prompt/table modularization. App added invites, HAPPENING events, privacy audit, polymorphic For You cards, schema sync, and generated-type adoption. |
| 2026-05-10 | Trip Home v1-v5 shipped backend and frontend: attention sections, three-zone feed, dismissal/undo, new archetypes, capture/activity framing, and group-state cards. |
| 2026-05-11 | Trust loop and CI day: backend added plan-state API, map read model, proposal reliability invariants, plan_events ledger, diff-safe revert, privacy redactor, VCR/Soul QA, migration squash, reliability gates. App shipped Plan v2/Map v2, proposal trust surfaces, Expo SDK 55, For This Trip, and CI dispatch. |
| 2026-05-12 | Backend built memory/trip story APIs, post-trip composition, content-safety scanner, eval replay, Brooklyn/Lisbon seeding promotion, traveler-depth backfill, delegation preferences, and baseline gates. App shipped proposal timeline/conflict UX, Memory home/story editing/share/bookmarks/archive/regeneration/photo slots, delegation persistence, and tests. |
| 2026-05-13 | Backend added booking foundation, Lisbon promotion, traveler backfill, legal/privacy, photos, event_state, expense tools, and migrations. App added photo album, mark-as-done, live-trip detection, expenses settlement, and Discover stability fixes. |
| 2026-05-14 | Backend closed eval and seed bugs, migrated baselines to Qdrant tier, and tightened venue-naming/scope constraints. |
| 2026-05-15 | Backend did major excellence work: eval promotion, content graph backend, turn telemetry, grounding guard, research/concierge refactors, quality drift, deploy hygiene, prompt-diff harness, dogfood tooling, Fly config, and self-review fixes. App shipped Discover content gap work, geofence refactor, chat stop/status, broad mobile polish, haptics, skeletons, permission recovery, and API/design cleanup. |
| 2026-05-16 | Backend added cross-trip threading, safety elicitation, tool consolidation, booking canary docs, architecture review, and many prompt/tool refactors. App shipped onboarding safety chips, empty-state and cold-start fixes, Travel DNA cards/disputes, trip creation audit fixes, mobile/a11y polish, cross-trip threading UI, push fixes, and many audit repairs. |
| 2026-05-17 | Backend worked heavily on memory drift, agent planning/tool consolidation, route guards, contract fixes, and eval/reliability. App fixed API error/SSE handling, expenses field drift, invite token survival, lazy-research badge, frontend audit issues, and schema sync. |
| 2026-05-18 | Backend continued audit hardening and endpoint triage. App ran frontend audit batches: auth/security/type safety, RN hygiene, type consolidation, mutation/idempotency, AppState, offline/errors/forms/a11y, performance, and hook/screen fixes. |
| 2026-05-19 | Backend and workspace unified OpenAPI and release runbooks. App fixed data-contract/mocks, added transport-gap callout, release profiles, API-type CI gate, and a11y/design-system pass. |
| 2026-05-20 | Backend pushed large dogfood and social-loop substrate work. App added Sentry, privacy/account deletion/export, social loop, performance reliability, destination-led trip creation, push persistence, release guards, and Discover retry/error states. |
| 2026-05-21 | Backend and workspace consolidated dogfood-readiness docs. App fixed Home/Plan/Map coherence, silent SSE auth redirect, and added fault injection. |
| 2026-05-22 | Workspace consolidated owner checklist. App fixed invite persistence, booking/voice honesty, Discover plan-similar city bug, and page-spec naming. |
| 2026-05-23 | App focused on TestFlight/dogfood boot: EAS project, Expo audio migration, dependency audit, internal error boundaries, module-load diagnostics, auth against Fly backend, OTA updates, and startup crash fixes. Backend had a small targeted fix. |
| 2026-05-24 | The largest frontend product/design day: chat card kit, markdown policy, per-person stays, Discover blended feed and real dossiers/photos/riso fallbacks, Trips home simplification, immersive trip workspace/chat/map, Plan redesign, visual polish, nav/header experiments, story share landing, and production backend config. Backend simultaneously removed large old surface/code, synced contracts, and supported Atlas/cards/stays/Discover. |
| 2026-05-25 | Live-trip/voice/proactive layer: app wired trip situation, ambient notices, narration interruption, proactive routing, and group/prep/live companion cards. Workspace synced OpenAPI. |
| 2026-05-26 | Atlas became a product surface: app integrated Atlas surfaces and Mapbox lazy-load fallback; backend shipped Atlas V1/openapi/leave-by/proactive support. Workspace renamed child repos to lowercase and added Atlas engineering plans. |
| 2026-05-27 | App refined chat/composer/streaming, Discover reader, riso city slugs, Atlas review/artifact flows, trip overhaul phases, route correctness, and performance. Backend smaller support fixes. |
| 2026-05-28 | App completed trip-overhaul phases: standalone-to-trip promotion, Discover chooser, no eager trip creation, global Discover feed, and dedupe/header tests. Backend small support work. |
| 2026-06-02 | App frontend revamp landed: Claude design system, palette/shadows/typography/cards consolidation, Atlas/trips/concierge/discover/me redesign, honest degradation, crash guards, Vesper chat editorial scroll. |
| 2026-06-03 | App continued chat/trip/Atlas design alignment and Document Edit spec. Backend had small support commits. |
| 2026-06-04 | Workspace added design mockups and OpenAPI sync. Backend and app worked on docs, design-system consolidation, typography roles, mock splits, Trip Home group-consensus/prep feed, and API boundary cleanup. |
| 2026-06-05 | Backend added dogfood/dev-persona and QA tools plus many substrate changes. App added ConversationSeed migration, query-key registry work, bottom-sheet unification, dogfood QA sweep, offline gating, and user-journey fixes. |
| 2026-06-06 | Atlas Almanac/Timeline/removed moments landed on app; backend added Atlas timeline stack support. |
| 2026-06-09 | App fixed push deep-link/card focus and Ask Vesper seed gap. Backend had supporting commits. |
| 2026-06-10 | Workspace added 12 canonical journey docs and Atlas timeline/onboarding/discover design docs. App did large Home/Trips/Atlas/card-contract/design work. Backend added journey/Atlas/openapi support and composition-related work. |
| 2026-06-11 | App polished home/trips/Atlas, content contract clamping, and typed fixes. Backend small support work. |
| 2026-06-12 | Workspace documented dogfood trust journey contracts and Vesper Trust Receipts. App added Atlas v3 UI, query-key/sheet/empty-state refinements, design token bridge, forward-compatible action fallback, and fixed stale Jest tests. Backend added trust receipt/support contracts and broader substrate work. |
| 2026-06-13 | App built Trips Home hero phases, loading primitive, typography/brand refactors, Focus Home fixes, and hero contract wiring. Backend worked on TripHero/openapi, product docs, and architecture status. |
| 2026-06-14 | App shipped Focus Home pick deck face, changes attribution/votes, Atlas mocks/contracts, rich far-out hero, and many card/home fixes. Backend shipped atlas composer/trips routes and home batch support. |
| 2026-06-15 | App merged folio/deck work, TripFolioHome alignment, AtlasMemoryReel, conversation archive, editorial UI primitives, tests, notifications, and route/card fixes. Backend merged Vesper pick substrate. |
| 2026-06-16 | App reconciled tests, tuned home feedback, fixed trip-less chat routes and Concierge feed refresh, and kept a WIP home session. |
| 2026-06-17 | App shipped Discover Cover home with recall band, plan reasoning/feasibility explanations, booking trust receipt/mark booked, background location push, Trip Story listen, and itinerary feel pass. Backend shipped corresponding personal-frame/openapi and plan/home support. |
| 2026-06-18 | App fixed card-system gaps, started Change Studio/Health Strip, rendered plan-ready/proposal cards, added invite fallback, instant card resolution, and many home/discover/booking/atlas improvements. Workspace copied the itinerary-edit audits. Backend added plan reasoning schema and card-system support. |
| 2026-06-19 | App executed a huge itinerary hardening round: edit-preview/commit integration, conflict keep/dismiss, Now Mode, timezone fix, proposal voter counts, ghost/withdraw/supersede, idempotency, venue lat/lng, mark-happened, and many journey-audit bugs. Backend added matching plan edit/commit/conflict/decision contracts. |
| 2026-06-20 | App retired legacy itinerary read model, made row tap edit-first, unified conflict resolution, lazy-mounted row sheets, fixed Atlas/Discover bugs, and aligned FE board contracts. Backend shipped related Atlas/discover/plan changes. |
| 2026-06-21 | App and backend consolidated Atlas/Discover composition, AI ops types, query keys, date parsing guard, Discover composed boards, CardSurface cleanup, product audit docs, and dogfood substrate plan. Contract check passes. |

## Progress Against Vision

The vision has three big claims:

1. Vesper should help people get more out of trips, not merely plan them.
2. Group trips are the launch wedge, but the moat is the world model connecting people, places, trips, memories, groups, and taste.
3. The product must make AI consequences inspectable and controllable so the magic feels earned.

Progress is strong on all three.

- Concierge relationship: streaming chat, skills, memory, prompt/tool gates, proactive systems, Vesper Home, consequence receipts, and voice/narration scaffolding exist.
- Trip truth: Plan state, map state, proposals, plan_events, Change Studio, Review Stack, ghost proposals, Now Mode, booking/stay/expense semantics, and recent changes exist.
- Place intelligence: content graph, seeded city pipeline, briefs, dossiers, Discover feed, composed Discover boards, and world-corpus search exist.
- Memory and trust: Personal Memory, Atlas, trip stories, story archive, photo slots, Atlas candidates/artifacts, privacy audit, disputes, and discovery reflection exist.
- Engineering excellence: OpenAPI is central, frontend generated types are checked, backend import boundaries and safety gates are explicit, eval replay and VCR reduce live LLM dependence, and both repos have serious CI.

The gap is no longer "we do not have the pieces." The gap is "we need fewer, more credible, end-to-end proofs."

## Engineering Architecture Assessment

Strengths:

- The backend has a sane domain split: `core`, `concierge`, `planning_agent`, `preference_engine`, `research_agent`, `booking_agent`, `voice`, `discover`, `atlas`, `composition`, `home`, `situation`, `notifications`, and API routes.
- Cross-agent imports are intentionally forbidden and guarded. Data moves through DB/vector/API contracts instead of casual imports.
- Model usage is centralized through role-based model registry and `call_llm()` wrappers with tracing/retry/token tracking.
- The frontend has a mature Expo/RN architecture: Expo Router, React Query, generated OpenAPI types, `data/` hooks, `components/` by domain, design-system primitives, and mock/persona systems.
- Quality gates are unusually advanced for this stage: OpenAPI freshness, API-boundary checks, mock/real parity, golden paths, ruff/mypy, async/sync DB checks, prompt/tool drift checks, eval replay, design-token budgets, date parsing guard, and docs checks.

Architectural risks:

- Client aggregation still appears where product-authored magic wants backend read models. The magic-flows audit calls out missing backend `GET /api/trips/home` and trip `/folio` read models.
- The dogfood persona system is richer in frontend mocks than in backend truth. This is useful for design speed but dangerous if used as MVP proof.
- Atlas/Discover composition is functionally shipped, but the audit still flags realization risks: perceived latency, image rendering on device, prose quality, and full contract coverage.
- Itinerary editing has two backend holes: proposal apply atomicity and chat-tool convergence onto the shared proposal service.
- Journey status is honest but sobering: all 12 canonical journeys remain "not dogfood-ready" until missing mock walks, deterministic tests, and live canaries are done.

## MVP and Dogfood Readiness

Presentable MVP: yes, with careful framing.

What is safe to present:

- Vesper as a relationship surface.
- Trips as the operational truth of planning/live travel.
- Discover as place-facing editorial intelligence.
- Atlas as memory and trust surface.
- Change Studio as proof that itinerary edits are intelligent, reversible, and group-aware.
- Consequence receipts as the system-wide grammar of "what changed."

What not to overclaim:

- Fully autonomous booking. Booking is scaffolded and increasingly hardened, but live provider canaries/smokes remain required.
- Fully live voice companion. Voice is substantial but still has deferred latency/offline/provider work.
- Full journey dogfood readiness. The journey matrix says "no" for every journey.
- Backend-real persona worlds. Current canonical persona substrate is still being consolidated.

## Highest-Leverage Next Work

1. Make one canonical dogfood world backend-real.
   - Start with Elif if speed matters because Rome/Lisbon are already seeded.
   - Start with Ben if MVP narrative matters because planning/editing demonstrates the core loop.
   - Create a manifest that hydrates backend truth and frontend preview from one source.

2. Close itinerary/proposal backend holes.
   - Make proposal resolve/apply atomic.
   - Route chat-created proposals through `build_and_persist_proposal`.
   - Add comprehensive rollback/apply/dedup/supersede tests.

3. Promote Journey 05, 07, and 11 from "built" to "dogfood-ready."
   - Journey 05: add app-level Changes walk and make proposal canary a standing gate.
   - Journey 07: run live Discover feed/search canary on seeded data; de-afford no-trip share if needed.
   - Journey 11: run optional staging spot-check and confirm Atlas memory control against legacy data.

4. Verify Atlas/Discover composition on a real device.
   - Confirm riso imagery paints.
   - Confirm copy latency and fallback behavior.
   - Add the on-device/snapshot guard so this does not regress invisibly.

5. Build backend-authored Trip Home/Folio read models where consequences should feel authored.
   - This is the next big architecture quality step after the client consequence layer.

6. Turn dogfood QA into a short ritual.
   - Run `make contract-check`, `make mock-real-parity`, `make golden-path-qa`, then the smallest live canary.
   - Use post-session review tooling to capture weird turns and promote failures into deterministic tests.

## Bottom Line

You have accomplished the hard part: the product is no longer a set of disconnected demos. It has a thesis, a real backend spine, typed contracts, serious reliability gates, and product surfaces that increasingly express one system.

The remaining work is not "build more." It is consolidation, proof, and polish:

- fewer canonical personas,
- fewer unverified journeys,
- fewer client-only illusions,
- fewer split paths,
- more backend-authored truth,
- more deterministic gates,
- more on-device visual proof.

That is exactly the right phase before dogfooding and MVP presentation.
