# Pre-Dogfood Final Audit — Cursor Cloud Agent Prompts

Twelve area-scoped prompts for a final, read-only pre-dogfood audit. Each prompt is
**self-contained** — launch each as its own cloud Cursor agent. Each agent writes ONE
markdown file to `docs/audits/pre-dogfood-2026-05/areas/`.

## How to run

1. Launch one cloud Cursor agent per area below (run Tier 1 first if you want early signal).
2. Each agent is **read-only on code** and writes only its own `areas/NN-slug.md` file
   (unique filename per area → no conflicts when you merge the agents' branches).
3. When all are done, merge the branches, then we consolidate every `areas/*.md` into a
   single ranked **Master Punch List v4** and fix together.

## Conventions shared by every prompt

- **Mode:** read-only; no product-code/test/config changes. Output is one md file.
- **Severity (comprehensive):** P0 = privacy leak / data loss / auth bypass / crash /
  dogfood-blocking · P1 = breaks a golden path under realistic conditions · P2 = real but
  non-blocking · TECH-DEBT = maintainability/perf/missing-tests (separate section).
- **Don't re-litigate decisions:** confirmed deferred-by-design items from the Known Gaps
  Register go under "Known / Accepted," not as new findings.
- **Finding template (exact):**

```
### [P0|P1|P2|TECH-DEBT] — <one-line title>
**References:** <file:line>, ...
**Why it matters to a real tester:** ...
**Repro / deterministic test idea:** ...
**Suggested fix direction:** ...
**Confidence:** High|Medium|Low
```

---

## Tier 1 — newest / most-coupled / catastrophic surface

### Area 01 — Privacy & group-safe synthesis

```
You are a senior security/privacy auditor doing a FINAL pre-dogfood audit of ONE area of
"Vesper", an AI travel concierge: FastAPI backend in `Travel Agent/`, Expo/React Native app
in `Travel App/`, coordinated from the workspace root. Group trips are the launch wedge. THE
catastrophic failure mode is leaking one group member's private constraint
(budget/dietary/accessibility/health/free-text) to the rest of the group, the organizer, or
any public surface.

MODE: READ-ONLY. Do not modify any product code, test, or config. Output is one md file.

READ FIRST (so you don't re-report intentional behavior):
- docs/audits/pre-dogfood-2026-05/dogfood-readiness.md  (prior audit; its privacy P0s are FIXED)
- Travel Agent/docs/working/Known Gaps Register.md  (deferred-by-design → "Known / Accepted", not findings)
- Travel Agent/CLAUDE.md  (architecture + subsystem entry points)
- docs/reliability/traces/private-input-to-group-safe-context.md  (the golden-path contract)

YOUR AREA: the private→public boundary end-to-end, INCLUDING the social sharing paths added
2026-05-20 that no prior audit covered. Verify every boundary below is default-deny:
- backend/preference_engine/retrieval/preference_retriever.py :: get_group_context()
- backend/synthesis/group_synthesizer.py and hard_constraints handling
- backend/core/story_projection.py (the ONE place a story becomes public) + the public-photo
  allowlist in backend/core/db/trip_story_shares.py
- backend/api/routes/profiles.py (public profile default-deny: must never expose
  hard_constraints/budget/health)
- backend/api/routes/_notifications_feed.py and backend/core/models/trip_invites.py
  (intake summary must be neutral) + invite intake provenance
- follow-influenced recommendations: backend/core/personalization/follow_affinity.py
  (does any per-follow signal leak who-saved-what beyond an anonymized count?)
- the concierge group-compose path in backend/concierge/ (what enters group-visible context)
- frontend render points in Travel App/ that display any of the above payloads

METHOD: use realistic sensitive example strings (e.g. "I can't afford expensive dinners",
"I'm in a wheelchair", a specific allergy) and check they never surface in any group-,
organizer-, or public-facing payload. Prefer a deterministic repro/test for each finding.
Severity: P0 = any leak. Also log P1/P2/TECH-DEBT comprehensively.

OUTPUT: write to docs/audits/pre-dogfood-2026-05/areas/01-privacy-group-safe-synthesis.md.
Start with a Summary (counts by severity + your single biggest concern). Use the exact
finding template. End with "## Known / Accepted (not new findings)".
Finding template:
### [P0|P1|P2|TECH-DEBT] — <title>
**References:** <file:line>, ...
**Why it matters to a real tester:** ...
**Repro / deterministic test idea:** ...
**Suggested fix direction:** ...
**Confidence:** High|Medium|Low
```

### Area 02 — Social loop & sharing (newest code)

```
You are a senior auditor doing a FINAL pre-dogfood audit of ONE area of "Vesper" (FastAPI
backend in `Travel Agent/`, Expo/RN app in `Travel App/`). Group trips are the wedge; the
catastrophic failure mode is leaking a member's private constraint to the group or any public
surface. This area is the NEWEST code (shipped 2026-05-20→21) and its integration tests have
run only once — treat it as the highest-risk surface.

MODE: READ-ONLY. Output is one md file.

READ FIRST:
- Travel Agent/docs/product/MVP Social Loop.md  (the spec, incl. paywall/visibility intent)
- docs/audits/pre-dogfood-2026-05/dogfood-readiness.md
- Travel Agent/docs/working/Known Gaps Register.md
- Travel Agent/CLAUDE.md

YOUR AREA: the trip→artifact→share→viewer→plan-similar loop + the follow graph. Audit:
- Public projection / default-deny: backend/core/story_projection.py,
  backend/core/db/trip_story_shares.py, backend/api/routes/story_shares.py,
  backend/api/routes/story_landing.py (unauthenticated public HTML/JSON + card.png)
- Visibility state machine: private/group/link/public + revoke vs reversible-pause + slug
  reuse on rotate; does an old link ever resurrect content after revoke?
- plan-similar: backend/core/db/plan_similar.py, backend/api/routes/plan_similar.py,
  trip_sources provenance, idempotency per (viewer,share), the plan_similar rate limit
- profiles + follow graph: backend/api/routes/profiles.py, backend/core/db/follows.py,
  backend/api/routes/follows.py (social_feed), backend/core/personalization/follow_affinity.py
- card/og rendering: backend/core/story_card.py, backend/core/static_map.py (token-gated)
- analytics events: trip_story_share_events (no PII in referrer/viewer fields?)
- frontend: Travel App/components/memory/ShareStorySheet.tsx,
  Travel App/app/(tabs)/trips/[tripId]/story.tsx, app/profile/[userId].tsx,
  data/storyShare.ts, the story_shared feed card in components discover
- migrations f1a2b3c4d5e6 → a7b8c9d0e1f2 → b2c3d4e5f6a7 → c3d4e5f6a7b8 → d4e5f6a7b8c9:
  CHECK constraints, FK on-delete behavior, single-head cleanliness
- card cache invalidation on revoke/rotate (per-pod TTL — note multi-pod correctness)

Hunt specifically for: a private/hidden section or photo reaching the public card; an
unauthenticated route returning more than the intended public projection; rate-limit /
abuse gaps on public + plan-similar routes; mock-vs-real drift in the share API triad.

OUTPUT: docs/audits/pre-dogfood-2026-05/areas/02-social-loop-sharing.md. Summary first,
exact finding template, "## Known / Accepted" last. Template:
### [P0|P1|P2|TECH-DEBT] — <title>
**References:** <file:line>, ...
**Why it matters to a real tester:** ...
**Repro / deterministic test idea:** ...
**Suggested fix direction:** ...
**Confidence:** High|Medium|Low
```

### Area 03 — Invite & join flow

```
You are a senior auditor doing a FINAL pre-dogfood audit of ONE area of "Vesper" (FastAPI
backend `Travel Agent/`, Expo/RN app `Travel App/`). Group trips are the wedge, so the
invite→join loop IS the acquisition path; its failures break first impressions. The
catastrophic failure mode is leaking a member's private constraint; invite tokens are bearer
credentials and must never be logged or exposed.

MODE: READ-ONLY. Output is one md file.

READ FIRST:
- docs/audits/pre-dogfood-2026-05/dogfood-readiness.md  (its invite P0s + the idempotency P1
  are now FIXED — confirm, don't re-file; look for what's still open)
- docs/reliability/traces/create-trip-and-invite-group.md
- Travel Agent/docs/working/Known Gaps Register.md
- Travel Agent/CLAUDE.md

YOUR AREA:
- backend/api/routes/invites.py (mint/dispatch/intake/accept/consume), the _token_fp helper,
  and every place a raw token could reach a log or event payload
- backend/api/routes/invite_landing.py (unauthenticated landing, OG tags, AASA deep-link)
- backend/core/models/trip_invites.py (intake summary neutrality)
- idempotency + races: accept after consumed (same user vs other user), double-accept,
  X-Idempotency-Key handling, single-use vs multi-use semantics
- quotas: per-user daily invite caps; abuse on public invite landing
- deep links: Travel App/app/invite/[slug].tsx, Universal Links / AASA correctness,
  invite-token survival across the sign-in flow (the token must persist through auth)
- delivery: SendGrid/Twilio paths (deferred? confirm) — graceful degradation if unset
- mock-vs-real parity for the whole invite client surface

Hunt for: any raw token in logs/events; an accept path that 410s a user who actually joined;
a deep link that drops the token across auth; intake content leaking to the organizer;
a landing page that exposes trip internals pre-auth.

OUTPUT: docs/audits/pre-dogfood-2026-05/areas/03-invite-join-flow.md. Summary first, exact
finding template, "## Known / Accepted" last.
### [P0|P1|P2|TECH-DEBT] — <title>
**References:** <file:line>, ...
**Why it matters to a real tester:** ...
**Repro / deterministic test idea:** ...
**Suggested fix direction:** ...
**Confidence:** High|Medium|Low
```

### Area 04 — Cross-surface state coherence (Home / Plan / Map / Chat)

```
You are a senior auditor doing a FINAL pre-dogfood audit of ONE area of "Vesper" (FastAPI
backend `Travel Agent/`, Expo/RN app `Travel App/`). A named top dogfood risk is STATE
INCOHERENCE across surfaces: the agent edits the itinerary in chat and Home/Plan/Map show
stale or conflicting state. This area is integration-level — it won't show up in any single
file.

MODE: READ-ONLY. Output is one md file.

READ FIRST:
- docs/reliability/traces/home-plan-map-coherence.md
- docs/reliability/traces/proposal-review-and-plan-mutation.md
- Travel Agent/docs/working/Known Gaps Register.md
- Travel Agent/CLAUDE.md and Travel App/CLAUDE.md

YOUR AREA: the read models behind the four surfaces and the frontend cache that ties them:
- Backend read models: plan-state API + map read model, trip home/attention feed, the
  itinerary read path, conversation/chat state — confirm they derive from one source of
  truth (the plan_events ledger / committed itinerary), not divergent computations
- Frontend query invalidation: after a proposal apply/revert, which React Query keys are
  invalidated? Check Travel App/components/trip/ProposalReviewSheet.tsx,
  context/TripContext.tsx (the split Trips/CurrentTrip/Actions contexts), data/ hooks for
  plan/map/home/chat, and utils/sse.ts. Find any surface that can show stale data after a
  mutation, an optimistic update that doesn't reconcile with the refetch, or an SSE
  reconnect that loses in-flight state
- Destination/trip identity persistence: does a trip created from a destination card keep
  its destination after the real backend refetch? (Travel App/context/TripContext.tsx,
  app/(tabs)/discover/index.tsx, components/for-this-trip/) — write a mock/real parity check
- Mock-vs-real drift that could hide any of the above in mock mode

Hunt for: a mutation whose effects are visible on one surface but not another until reload;
optimistic state that survives a failed mutation; invalidation that misses map or home.

OUTPUT: docs/audits/pre-dogfood-2026-05/areas/04-cross-surface-coherence.md. Summary first,
exact finding template, "## Known / Accepted" last.
### [P0|P1|P2|TECH-DEBT] — <title>
**References:** <file:line>, ...
**Why it matters to a real tester:** ...
**Repro / deterministic test idea:** ...
**Suggested fix direction:** ...
**Confidence:** High|Medium|Low
```

---

## Tier 2 — core agent & trip mechanics

### Area 05 — Concierge agent loop, tools, output guards, recovery

```
You are a senior auditor doing a FINAL pre-dogfood audit of ONE area of "Vesper" (FastAPI
backend `Travel Agent/`). The concierge is the core product surface. The catastrophic
failure mode is leaking a private constraint; secondary risks are confabulation (inventing
venues/facts) and broken tool-calling under error.

MODE: READ-ONLY. Output is one md file.

READ FIRST:
- Travel Agent/CLAUDE.md (esp. the output-guard mode section and eval discipline)
- Travel Agent/docs/working/Known Gaps Register.md
- docs/audits/pre-dogfood-2026-05/dogfood-readiness.md

YOUR AREA:
- backend/concierge/agent.py :: handle_turn() and the shared loop backend/core/agent_loop.py
  (stop_reason handling, parallel tool execution, token/loop-budget caps, streaming)
- tools: backend/concierge/tools.py, backend/concierge/tool_handlers/* (booking_flow,
  itinerary, whereabouts) — argument validation, error classification, retry budget
- output guards: backend/concierge/output_guards.py — confirm guard runs in `log` mode
  (intended for week 1) and that grounding/provenance/entity-existence checks actually fire;
  assess false-positive risk and whether any P0 (e.g. confabulated venue) ships unflagged
- agent-loop recovery: tool-error classifier, retry budget, telemetry
  (concierge_turns/reasoning_spans) — does a tool failure degrade gracefully or hang/crash?
- session + skill selection: backend/concierge/session.py, prompts.py modular skills
  (_select_skills) — does the right skill set load per phase/conversation type?
- LLM discipline: all calls via backend/core/llm.py; model roles via model_registry.py

Hunt for: a tool path that can crash or infinite-loop the turn; an output guard that's
effectively a no-op; confabulation that reaches the user; a skill mis-selection that drops
privacy or grounding instructions.

OUTPUT: docs/audits/pre-dogfood-2026-05/areas/05-concierge-agent-loop-tools.md. Summary
first, exact finding template, "## Known / Accepted" last.
### [P0|P1|P2|TECH-DEBT] — <title>
**References:** <file:line>, ...
**Why it matters to a real tester:** ...
**Repro / deterministic test idea:** ...
**Suggested fix direction:** ...
**Confidence:** High|Medium|Low
```

### Area 06 — Proposals / plan-state / itinerary mutation & revert

```
You are a senior auditor doing a FINAL pre-dogfood audit of ONE area of "Vesper" (FastAPI
backend `Travel Agent/`, Expo/RN app `Travel App/`). This is the "Propose stage" trust loop:
the agent edits a shared itinerary as reviewable diffs the group can approve/revert. Trust
breaks if an apply lies about its result or a revert corrupts state.

MODE: READ-ONLY. Output is one md file.

READ FIRST:
- docs/reliability/traces/proposal-review-and-plan-mutation.md
- Travel Agent/docs/working/Known Gaps Register.md
- Travel Agent/CLAUDE.md and Travel App/CLAUDE.md

YOUR AREA:
- backend propose/apply/revert: the propose_change path, the append-only plan_events ledger,
  block-id forward chaining (recent_change_ids), diff-safe revert (incl. diff_safe_partial /
  force-full-revert), and "honest apply state" (does reported success match actual mutation?)
- plan-state API + map read model consistency after mutation
- concurrency: two members acting on the same block; a revert racing an apply; idempotency
- frontend: Travel App/components/trip-plan/* (BlockChangedBanner, BlockDiffChip,
  ChangeTimelineRow, RevertConflictSheet, PendingVotesSection),
  components/trip/ProposalReviewSheet.tsx, app/(tabs)/trips/[tripId]/{plan,changes}.tsx,
  the revert mutation + conflict UX, votes/delegation
- delegation preferences (Act-stage groundwork): is anything auto-acting without approval?

Hunt for: an apply that reports success but didn't mutate (or vice-versa); a revert that
leaves the ledger and itinerary inconsistent; a conflict path that loses a user's change; a
diff shown to the user that doesn't match what applied.

OUTPUT: docs/audits/pre-dogfood-2026-05/areas/06-proposals-plan-state-revert.md. Summary
first, exact finding template, "## Known / Accepted" last.
### [P0|P1|P2|TECH-DEBT] — <title>
**References:** <file:line>, ...
**Why it matters to a real tester:** ...
**Repro / deterministic test idea:** ...
**Suggested fix direction:** ...
**Confidence:** High|Medium|Low
```

### Area 07 — Memory / Trip Story / post-trip / photos

```
You are a senior auditor doing a FINAL pre-dogfood audit of ONE area of "Vesper" (FastAPI
backend `Travel Agent/`, Expo/RN app `Travel App/`). The post-trip memory artifact is the
compounding asset and the share source. Photos carry consent + EXIF/location privacy risk.

MODE: READ-ONLY. Output is one md file.

READ FIRST:
- docs/reliability/traces/memory-and-post-trip-loop.md
- Travel Agent/docs/product/Post-Trip Lifecycle.md
- Travel Agent/docs/working/Known Gaps Register.md
- Travel Agent/CLAUDE.md

YOUR AREA:
- Trip Story composer + Memory API (story archive, regenerate, photo_slot prompts,
  background trigger) — confirm a regenerate can't drop or duplicate sections, and that
  private content never enters a story that later becomes shareable (coordinate with the
  story_projection default-deny in Area 01/02)
- Trip photo album: upload, EXIF auto-tag, GPS extraction, per-photo privacy
  (group/group_and_learn/private), consent — does a private photo ever leak via itinerary
  attachment, story slot, or behavioral signal? Is GPS/EXIF stripped where it should be?
- post-trip loop: character read, proposal diffs, Personal Memory write-back from in-trip
  behavior (pins/votes/photos/dwell) — does the loop actually close, and only from
  consented signals?
- frontend: Travel App/components/memory/*, app/(tabs)/trips/[tripId]/story.tsx, the album +
  lightbox + consent UI, dwell instrumentation

Hunt for: a private photo or section reaching a shareable/group surface; EXIF/GPS leaking;
a regenerate that corrupts the story; memory write-back from non-consented signals.

OUTPUT: docs/audits/pre-dogfood-2026-05/areas/07-memory-trip-story-photos.md. Summary first,
exact finding template, "## Known / Accepted" last.
### [P0|P1|P2|TECH-DEBT] — <title>
**References:** <file:line>, ...
**Why it matters to a real tester:** ...
**Repro / deterministic test idea:** ...
**Suggested fix direction:** ...
**Confidence:** High|Medium|Low
```

### Area 08 — Notifications / triage / digest / proactive turns

```
You are a senior auditor doing a FINAL pre-dogfood audit of ONE area of "Vesper" (FastAPI
backend `Travel Agent/`, Expo/RN app `Travel App/`). Notifications are how the agent is
proactively present; over-notifying or leaking private content into a notification is a
trust break. The catastrophic failure mode is leaking a member's private constraint.

MODE: READ-ONLY. Output is one md file.

READ FIRST:
- docs/reliability/traces/notifications-and-proactive-help.md
- Travel Agent/docs/working/Known Gaps Register.md
- Travel Agent/CLAUDE.md

YOUR AREA:
- the gate→triage→trigger pipeline: backend/notifications/gates.py → triage.py →
  backend/concierge/triggers.py, notifications/prompts.py
- digest: backend/digest/engine/daily.py — content selection, quiet hours
- the notification feed: backend/api/routes/_notifications_feed.py (PendingInviteAnswer and
  any payload that could carry a member's private answer to the organizer/group)
- proactive turns: triggering criteria, rate/quiet-hours caps, dedupe, per-user quotas
- push delivery: APNs/Expo push, push deregister on logout/delete (privacy), graceful
  degradation if push creds unset
- frontend: Travel App/data/notifications.ts, the feed render, mark-read, bell badge

Hunt for: any private answer/constraint in a notification body; a proactive trigger that can
spam; quiet hours bypass; a notification that survives account deletion / push deregister.

OUTPUT: docs/audits/pre-dogfood-2026-05/areas/08-notifications-triage-digest.md. Summary
first, exact finding template, "## Known / Accepted" last.
### [P0|P1|P2|TECH-DEBT] — <title>
**References:** <file:line>, ...
**Why it matters to a real tester:** ...
**Repro / deterministic test idea:** ...
**Suggested fix direction:** ...
**Confidence:** High|Medium|Low
```

---

## Tier 3 — platform & cross-repo

### Area 09 — Auth, route security, rate-limiting, quotas

```
You are a senior security auditor doing a FINAL pre-dogfood audit of ONE area of "Vesper"
(FastAPI backend `Travel Agent/`). With real testers on a real host, every route's auth +
rate-limit posture matters. Unauthenticated routes that expose PII or burn LLM spend are P0.

MODE: READ-ONLY. Output is one md file.

READ FIRST:
- docs/audits/pre-dogfood-2026-05/dogfood-readiness.md
- Travel Agent/docs/working/Known Gaps Register.md (auth/rate-limit class items)
- Travel Agent/CLAUDE.md and Travel Agent/docs/operations/Auth Modes.md

YOUR AREA:
- centralized auth: how every route under backend/api/routes/ declares its auth dependency;
  enumerate routes that are intentionally unauthenticated (invite/story landing, public
  story JSON, health, openapi) vs accidentally unauthenticated. Flag any authed-data route
  missing the auth dependency, and any membership-gated resource not checking membership
- the SKIP_AUTH dev bypass: confirm it cannot be enabled in a release build
- rate limiting + quotas: the _LIMITS scopes, per-user daily chat/invite/plan-similar caps,
  and any expensive route (LLM, search, seeding) with no cap
- the scripts/check_route_auth.py gate — does it pass clean, and does it actually cover the
  current route set?
- admin/metrics endpoints (e.g. /metrics/tokens, /admin/*) — are they protected?
- input validation at the boundary (request models, file upload limits)

Hunt for: an unauthenticated route returning user data or triggering LLM spend; a
membership check missing on a trip-scoped resource; a release-time SKIP_AUTH risk; an
uncapped expensive endpoint.

OUTPUT: docs/audits/pre-dogfood-2026-05/areas/09-auth-route-security-ratelimit.md. Summary
first, exact finding template, "## Known / Accepted" last.
### [P0|P1|P2|TECH-DEBT] — <title>
**References:** <file:line>, ...
**Why it matters to a real tester:** ...
**Repro / deterministic test idea:** ...
**Suggested fix direction:** ...
**Confidence:** High|Medium|Low
```

### Area 10 — Data layer / migrations / async-sync DB / RTBF

```
You are a senior backend auditor doing a FINAL pre-dogfood audit of ONE area of "Vesper"
(FastAPI backend `Travel Agent/`). The data layer is SQLAlchemy Core (never ORM); a wrong
migration or a blocking DB call under load is a dogfood reliability risk. RTBF/data-deletion
correctness is a privacy + legal risk.

MODE: READ-ONLY. Output is one md file.

READ FIRST:
- Travel Agent/CLAUDE.md (shared-db rules) and the shared-db rule file
- Travel Agent/docs/working/Known Gaps Register.md
- Travel Agent/docs/operations/Migration Squash Runbook.md

YOUR AREA:
- migrations under Travel Agent/alembic/: single-head cleanliness, every migration
  reversible (downgrade), CHECK/FK constraints match the Pydantic models, no data-destroying
  op without a guard. Confirm scripts/check_alembic_single_head.py passes
- async/sync DB debt: scripts/check_async_sync_db_baseline.tsv allowlists ~252 sync-DB calls
  in async coroutines. Spot-check the hottest paths (concierge handle_turn, plan-state, home
  feed, story routes) for event-loop-blocking calls on the request path; rank the worst
- get_connection() usage: any leaked connection, missing context manager, or transaction
  that should be atomic but isn't (esp. multi-table writes like accept-invite, plan-similar,
  story create)
- RTBF / data retention: the privacy(data-retention) cascade + purge (commit 125f711d) and
  voice 30-day audio purge — does account deletion actually remove every PII row across
  trips/photos/memories/events/shares? Any orphaned PII after delete?
- index coverage on the hot read paths

Hunt for: an irreversible/destructive migration; a blocking DB call on a hot request path; a
non-atomic multi-table write that can half-commit; PII that survives account deletion.

OUTPUT: docs/audits/pre-dogfood-2026-05/areas/10-data-layer-migrations-async-db.md. Summary
first, exact finding template, "## Known / Accepted" last.
### [P0|P1|P2|TECH-DEBT] — <title>
**References:** <file:line>, ...
**Why it matters to a real tester:** ...
**Repro / deterministic test idea:** ...
**Suggested fix direction:** ...
**Confidence:** High|Medium|Low
```

### Area 11 — Places / venues / retrieval / cost & booking deep-link safety

```
You are a senior auditor doing a FINAL pre-dogfood audit of ONE area of "Vesper" (FastAPI
backend `Travel Agent/`). Recommendation quality + cost control matter for dogfood: a
confabulated/closed venue erodes trust, and an uncapped external-API path burns money.
Booking is deep-link-out for dogfood — verify nothing auto-charges.

MODE: READ-ONLY. Output is one md file.

READ FIRST:
- Travel Agent/docs/working/Known Gaps Register.md (places cache O-14, retrieval R-1,
  transport TR-1, booking items — confirm deferred ones, don't re-file)
- Travel Agent/CLAUDE.md (places cache cron section, booking-providers rule)

YOUR AREA:
- retrieval: backend/planning_agent/fan_out_search.py + backend/core/vector/* (Qdrant
  hybrid/rerank) — grounding (do returned venues exist in the graph?), namespace/city
  filtering correctness, empty-result handling
- places cache: get_venue_status tool, the Postgres cache, the daily budget gate, and the
  cron scripts (refresh_upcoming_venues.py, purge_places_cache.py) — Google ToS retention
- cost control: every external call (Google/Foursquare/Tavily/Amadeus) under a cap +
  circuit breaker + timeout; the seeding path's budget cap and dead-letter behavior
- venues router (was a 404 earlier — confirm registered and correct)
- booking deep-link safety: backend/booking_agent/* — confirm deep-link-only providers
  (e.g. Viator) are filtered out of any auto-cart and nothing can auto-charge a tester;
  resilience decorators applied per the booking-providers rule

Hunt for: a confabulated/stale venue surfaced as real; an external call with no
cap/timeout/breaker; a booking path that could auto-charge; Google place_id retained past
ToS window.

OUTPUT: docs/audits/pre-dogfood-2026-05/areas/11-places-retrieval-cost-booking.md. Summary
first, exact finding template, "## Known / Accepted" last.
### [P0|P1|P2|TECH-DEBT] — <title>
**References:** <file:line>, ...
**Why it matters to a real tester:** ...
**Repro / deterministic test idea:** ...
**Suggested fix direction:** ...
**Confidence:** High|Medium|Low
```

### Area 12 — Frontend platform: API contract/parity, errors/offline/permissions, deploy/EAS config

```
You are a senior mobile auditor doing a FINAL pre-dogfood audit of ONE area of "Vesper"
(Expo/React Native app in `Travel App/`, plus cross-repo deploy config). On a real device
against a real backend, the failure modes are: mock/real API drift, unhandled errors/offline
states, missing permission recovery, and a misconfigured release build that can't reach the
backend at all (a known open blocker).

MODE: READ-ONLY. Output is one md file.

READ FIRST:
- Travel App/CLAUDE.md and the workspace CLAUDE.md (the OpenAPI contract section)
- docs/audits/pre-dogfood-2026-05/dogfood-readiness.md (the deploy/EAS P0s are still OPEN)
- docs/Owner Action Items.md, docs/Deploy & Rollback Runbook.md

YOUR AREA:
- API triad parity: Travel App/utils/api/{interface.ts,http.ts,mock.ts} vs the generated
  schema.gen.ts — find endpoints where mock and http diverge in shape/behavior (mock mode
  could hide a real bug). Confirm http.ts call sites all exist in docs/openapi.json
  (api-coverage); flag any hand-written type duplicating a backend model
- error/offline/loading: unhandled promise rejections, missing error states, SSE 401/
  reconnect handling (utils/sse.ts), offline behavior, retry/idempotency on mutations
- permissions: camera/photos/location/notifications request + recovery flows; what happens
  when a permission is denied
- crash safety: error boundaries; Sentry behind consent; AppState transitions
- deploy/release config (cross-repo): Travel App/eas.json (preview→fly.dev, prod→
  travelagent.app — both unreachable), Travel App/app.json (projectId placeholder
  00000000-…), Travel Agent/fly.toml, scripts/preflight-eas-build.sh, env wiring
  (EXPO_PUBLIC_API_URL, USE_MOCK_API, Clerk key). Document exactly what must change for a
  buildable, backend-reachable release — these are known P0s; capture the precise diff

Hunt for: mock/real drift that masks a backend bug; an unhandled error/offline path a tester
will hit; a permission denial with no recovery; the exact release-config changes needed.

OUTPUT: docs/audits/pre-dogfood-2026-05/areas/12-frontend-platform-deploy-config.md. Summary
first, exact finding template, "## Known / Accepted" last.
### [P0|P1|P2|TECH-DEBT] — <title>
**References:** <file:line>, ...
**Why it matters to a real tester:** ...
**Repro / deterministic test idea:** ...
**Suggested fix direction:** ...
**Confidence:** High|Medium|Low
```
