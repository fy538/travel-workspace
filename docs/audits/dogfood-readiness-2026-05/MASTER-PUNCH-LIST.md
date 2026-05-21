# Master Punch List — Dogfood Readiness Audit (2026-05)

Date: 2026-05-21
Synthesis of: `docs/audits/dogfood-readiness-2026-05/areas/01..15`
Mode: Audit synthesis only. No product code changed.

Raw findings across 15 area reports: **60**. After cross-area dedup: **~58 unique** (3 P0, 22 P1, ~33 P2/P3). Two confirmed duplicates merged (photo-learning consent: 07≡10; stale proposal block IDs: 05≡06). Several cost-control findings (04/11/15) are distinct mechanisms in one cluster.

> Severity is taken from the source reports and not inflated. "P0" here means a concrete blocking path for the *named dogfood phase*. Most P1s are not mechanics-blockers but are unacceptable in front of a real group — they gate the **external** phase, not necessarily the first internal one.

---

## 1. Executive Verdict

| Phase | Ready? | Gating reasons |
|---|---|---|
| **Local dogfood** (mock + local backend, single operator — current phase) | **Yes** | No finding blocks single-operator local use. The P0s are deploy/account (area 14) and the multi-user invite loop (area 02), neither of which bites local self-dogfood. Continue. |
| **TestFlight / internal real-backend dogfood** (small trusted group on the deployed stack) | **No — Blocked** | Area 14 P0s: backend hosts unhealthy (`travel-agent.fly.dev` DNS fails, `travelagent.app` empty reply) and `make preflight-eas` is red (no EAS CLI + placeholder projectId). You cannot produce or point a build. Plus area 02 P0 breaks the tap-invite→sign-in→join loop for any second user. |
| **External / semi-external testers** (real groups, real trips) | **No** | Everything above, **plus** the privacy-to-group + auth/financial-integrity P1 cluster that is catastrophic in front of a real group: proposal redactor cross-user leak (01), private interjection→group (08), public angle Personal-Memory leak (10), booking cross-trip IDOR + expense identity spoofing (13), photo-learning cross-user consent (07/10). Plus App-Store/legal drift (14 P1s). |

**Highest single risk:** the deploy chain (area 14) blocks *all* real-backend phases, and the privacy/auth P1 cluster blocks the *external* phase. Neither is fixed by more code polish alone — 14 is largely owner/account work.

---

## 2. P0 Dogfood Blockers (deduped)

| # | Finding | Owner surface | Source | Exact repro / check | Fix direction |
|---|---------|---------------|--------|---------------------|---------------|
| P0-1 | **EAS production preflight is red** — no EAS CLI on PATH; `app.json` projectId still `00000000-…`; release runtime guard throws on placeholder. | account + workspace | [14](areas/14-release-testflight-deploy-mobile.md) `Travel App/app.json:54`, `app/_layout.tsx:124`, `scripts/preflight-eas-build.sh:88` | `make preflight-eas` → aborts step 1; `jq -r '.expo.extra.eas.projectId' "Travel App/app.json"` → placeholder | `eas init`, commit real projectId, set `pk_live_` Clerk key via `eas env`, re-run preflight (OWNER-DEPLOY-CHECKLIST). |
| P0-2 | **Documented preview & prod backend hosts are not healthy** — prod profile points at `travelagent.app`; both health curls fail. | account + deploy | [14](areas/14-release-testflight-deploy-mobile.md) `Travel App/eas.json:26,34`, `backend/api/main.py:104` | `curl -fsS https://travel-agent.fly.dev/health` → DNS fail; `…travelagent.app/health` → empty reply | Deploy/repair Fly app + custom domain (or correct `eas.json`/docs to the live host); do not ship a prod build until `/health` is 200 and preflight green. |
| P0-3 | **Unauthenticated invite accept loses invite context after sign-in** — public `GET /invites/{token}` never 401s, so token is only persisted on a 401 that never happens; accept-time 401 then routes to Trips/onboarding, dropping the join. | frontend | [02](areas/02-invite-join-auth-deeplinks.md) `Travel App/app/invite/[slug].tsx:130,350`, `components/auth/SignInImpl.tsx:137`, `utils/api/http.ts:358` | Real-auth, no session: open invite → enter intake → Join → sign-in → lands in Trips, not the trip. | Persist invite token before any auth-required redirect; make sign-in/up completion consume the pending-invite destination. Add a regression: `viewInvite` 200 then `acceptInvite` 401 ⇒ `setPendingInviteToken` + post-auth return. |

*Note:* P0-1/P0-2 are largely **owner/account** work already captured in `OWNER-DEPLOY-CHECKLIST.md`. P0-3 is the only code P0 and is the cheapest high-leverage fix in the set.

---

## 3. P1 Must-Fix Before Broader Dogfood (grouped by golden path)

### Privacy / group-safe synthesis (the catastrophic-in-front-of-a-group cluster)
- **Proposal redactor misses other members' exact private phrases** — loads only the proposer's private corpus; an organizer/agent proposal can surface another member's exact budget/medical phrase into group-visible proposal cards. [01] `_propose_present.py:225`, `core/privacy_signal.py:59`. *Fix:* load a trip-scoped corpus for all members at the proposal boundary; broaden budget-phrase coverage (`$50 ceiling`, `price cap`).
- **Private group-interjection targets fall back to group chat** — triage encodes `target` but routing reads `target_audience`, so a private nudge can persist into the group conversation. [08] `group_interjection.py:529`, `triggers.py:75`. *Fix:* normalize interjection metadata to the triage contract (`target_audience`/`target_user_id`/`conversation_id`).
- **Public angle browse leaks Personal Memory** — `GET /places/{slug}/angles?user_id=<uuid>` is no-auth but personalizes from that user's Personal Memory and spends LLM tokens. [10] `angles.py:254,404`, `angle_rank.py:87`. *Fix:* drop `user_id` from the public route; gate personalization behind auth+self+rate-limit.
- **Photo-learning opt-in upgrades other members' photos** *(merged 07≡10)* — `opt-in-learning` bulk-updates all `group` photos on the trip, not just the actor's. [07] `trip_photos.py:325,485` / [10] `trip_photos.py:485`. *Fix:* scope update to `uploaded_by_user_id == actor.id`; fix copy/counts.

### Invite / auth / deeplinks
- **Raw invite tokens flow through home-card IDs, dismissals, logs, provenance** — bearer tokens become durable UI state and appear in one exception log + observation provenance. [02] `home/feed.py:431-461`, `invites.py:1000,1059`. *Fix:* use `_token_fp()`/synthetic card keys everywhere.

### Trip creation / destination identity
- **Story plan-similar trips persist `place_id` but lose the destination label** the app gates on; cloned trip feels destinationless. [03] `plan_similar.py:134`, `for-this-trip.tsx:69`. *Fix:* persist `trip_summary.destination` from the seed (or derive from a generated place field).
- **Discover/social "Plan similar" can create trips whose destination is a venue/site/recommendation title** — `createTrip({destination: item.name})` leaves `place_id` null while the app shows a string. [03] `discover/index.tsx:463`, `FeedItemRenderer.tsx:215`. *Fix:* separate "plan a destination" from "ask about this entity"; pass canonical place_id/slug.

### Concierge chat / cost / recovery
- **Streaming concierge turns bypass the daily chat quota** — the app's primary SSE path skips `check_chat_quota`/`commit_chat_quota`. [04] `session.py:1060,1199`. *Fix:* mirror the non-streaming quota gate + spend commit in `send_message_streaming()`.

### Proposal trust loop
- **Apply can "succeed" after zero mutations** — forks a version, changes nothing, route reports `succeeded`. [05] `proposal_apply.py:266`, `proposals.py:401`. *Fix:* compute mutation count; fail when non-add proposals affect zero blocks.
- **Revert reports success even when nothing was reverted** — `revert_*_v2()` returns `None` (e.g. <2 versions) but route flips to `withdrawn`. [05] `proposals.py:512`. *Fix:* treat `None` as failed revert; keep `accepted`, return conflict.
- **Retrying accept without an idempotency header can apply twice** — frontend `resolveProposal` sends no key; backend re-runs apply on a stale-status return. [05] `change_proposals.py:314`, `http.ts:790`. *Fix:* detect whether the DB transition happened; thread stable idempotency keys.

### Home / plan / map coherence
- **Backend home-feed 60s TTL cache re-surfaces stale decisions** after proposal resolve/dismiss, contradicting Plan even though the app invalidates React Query. [06] `home/feed.py:84,508`, `api/routes/home.py:121`. *Fix:* add `invalidate_home_feed_cache()` on mutations, or version the cache key (or cache only the anchor line).

### Notifications / push routing
- **Proactive push/in-app taps lack a reliable conversation target** — backend drops `conversation_id` before delivery; in-app rows always open group chat, so private proactive turns can misroute. [08] `session.py:738`, `notifications/index.tsx:217`. *Fix:* thread `conversation_id` through dispatch; route by `target_audience`/`conversation_id`.

### Content graph / search
- **Post-seed drift checker can miss real Qdrant/Postgres divergence** — `check_seed_drift.py` reads only Postgres and only direct-city `place_id`, so a wiped/stale Qdrant or child-place content reports "clean." [12] `check_seed_drift.py:50,59`. *Fix:* resolve the full city subtree and verify actual Qdrant point existence/payload for each non-null pointer.

### Booking / expense trust
- **Booking routes allow cross-trip session/offer mutations (IDOR)** — nested IDs aren't proven to belong to the path trip; cart-confirm can confirm a foreign session, emit an event on the wrong trip, and auto-create expenses cross-trip. [13] `booking.py:203,314,326`, `expenses/auto_log.py:75`. *Fix:* shared guards loading+validating each parent resource (mirror the proposal route's `proposal.trip_id` check).
- **Expense create trusts client `paid_by` and share `user_id`s** — a member can attribute payment to others or include non-members. [13] `expenses.py:145,882`. *Fix:* validate `paid_by`/share users are trip members; default to `actor.id`.
- **Booking UI claims "Booked" / "AI books directly" before any provider order exists** — no provider `book()`/`create_order()` in the ABC yet. [13] `BookingConfirmationCard.tsx:31`, `booking/[sessionId].tsx:322`. *Fix:* reserve "booked/confirmed" for provider-confirmed states; rename to "in progress/handoff ready"; gate behind the live-booking flag.

### Frontend data contract
- **Narration audio preflight uses HEAD against a GET-only route (405)** — cached audio silently treated as unavailable. [09] `useNarrationAudio.ts:192`, `narration.py:586`, `docs/openapi.json:7908`. *Fix:* add a backend `HEAD` route or switch the probe to a contract method; extend coverage to raw `fetch()` sites.

### Async workers / scheduled tasks
- **`DISABLE_LLM_BACKGROUND_LOOPS=true` misses post-trip LLM work** — summaries/reflections/debrief/memory-refresh/story still spend in "cheap" mode. [11] `lifecycle.py:251,256`, `db/trips.py:198`. *Fix:* centralize a `background_llm_enabled()` gate at every autonomous post-trip entry point.
- **Claimed scheduled tasks can stick forever after a crash** — only `pending` rows are selected; a process death between claim and `mark_done` strands the row. [11] `scheduled_tasks.py:201,216`. *Fix:* stale-claim reaper resetting old `claimed` rows to `pending` with a cooldown.

### Release / platform (App Store gating)
- **Microphone/audio privacy claims don't match the generated native permission surface** — docs say "no mic," but `expo-av` generates `NSMicrophoneUsageDescription`/`RECORD_AUDIO` and `MicPrivacyDisclosure` requests it. [14] `MicPrivacyDisclosure.tsx:107`, `package.json:37`. *Fix:* pick one posture; align App Privacy, Review Notes, Expo plugin text.
- **Public privacy policy is still draft/placeholder** and contradicts the disclosure set (PostHog, voice recordings, "Download My Data", `your-domain.com`). [14] `docs/legal/privacy.md:13,251`, `legal.py:91`. *Fix:* finalize served policy to match the actual build before submission.

---

## 4. P2 / P3 Backlog (grouped by area)

- **01 Privacy:** P2 raw intake in accept-time `invite.consumed` event (`invites.py:1021`); P2 group synthesis treats missing privacy rows as shareable *(Suspected)*; P2 privacy audit omits preference/memory/intake use; P3 debug log echoes raw tool inputs (`agent.py:841`).
- **02 Invite:** P2 preview Universal-Link host mismatch before custom domain *(Suspected)*; P3 stale privacy assertion in `tests/api/test_invites_api.py:440` (red).
- **03 Trip create:** P2 direct `POST /trips` can orphan a trip if organizer-member insert fails (`trips.py:404`).
- **04 Concierge:** P2 personal stream silently drops images/`angle_id` metadata (`conversations.py:135`); P2 token-budget exhaustion not surfaced as a recoverable state (`agent.py:1270`).
- **05/06 Proposals+coherence:** P2 **proposal detail uses raw affected block IDs after forks** *(merged 05≡06)* (`proposals.py:637` vs `plan_state.py:371`); P2 delegation downgrade → non-resolving vote when voting off (`_propose_present.py:150`); P2 stay/booking mutations don't invalidate plan/map/home (`data/booking.ts:85`, `data/accommodations.ts:35`).
- **07 Memory/story:** P2 public story projection can expose third-party named moments; P3 mock memory days richer than real digest mapping.
- **08 Notifications:** P2 concurrent expense-settle duplicate pushes *(Suspected)*; P2 unread feed uses mock-only `last_message_at`.
- **09 Frontend contract:** P2 venue detail hand-mirror + mock omits required fields; P2 api-boundaries guard misses component escape hatches + dynamic import.
- **10 Auth/security:** P2 cost-sensitive routes escape rate limits (lint blind spot: `personalize_angles`, `experience_fan_out_search`, booking graph); P2 upload/rehost/receipt-OCR not rate-limited; P3 `/health/background-tasks` exposes task names + raw error strings publicly.
- **11 Workers:** P2 some scheduled LLM handlers run sync DB on the loop (baselined); P3 cross-trip thread subscriber not in canonical registration bundle.
- **12 Content:** P2 concierge restaurant search drops empty-result diagnostics (`search.py:296`); P2 Discover/angle rails mask fetch failures as content gaps (`data/experiences.ts:22`).
- **13 Booking:** (all P1, listed above).
- **14 Release:** P2 AASA smoke checks `appID` while route emits `appIDs`; P3 Dockerfile healthcheck still probes `/docs`.
- **15 Perf/observability/cost:** P2 shared Anthropic clients lack explicit `timeout`/`max_retries` (`llm_client.py:44,63`); P2 no absolute token/cost ceiling; P2 cost attribution gap (no `source_type`/`cost_usd` in token log); P3 no circuit breaker on Qdrant/geocoding/LLM; P3 no global request-timeout middleware; P3 real audio lifecycle (Phase 6b) teardown to verify when wired.

---

## 5. Structural Gates To Add (recurring bug classes → lints/tests/CI)

| Bug class | Seen in | Gate to add |
|---|---|---|
| **Cross-trip / nested-resource auth (IDOR)** | 13 (booking), 13 (expense IDs), 10 (angle `user_id`) | Test/lint: every `/api/trips/{trip_id}/.../{resource_id}` route loads the resource and asserts `resource.trip_id == trip_id`; validate all client-supplied `user_id`/`paid_by`/`shares[]` against trip membership. |
| **Private-data → group/public leak** | 01, 08, 07, 10 | Privacy-phrase leak tests at every group/public write boundary (proposal, interjection, story projection, angle); extend `privacy_signal`/`group_compose` detectors; named-person redaction policy. |
| **Rate-limit blind spots on indirect LLM/provider spend** | 10, 04, 11 | Extend `check_route_auth.py` to wrapper names (or tag cost routes with metadata); add streaming-quota parity; add `upload`/`personalization`/`booking_session` scopes. |
| **Mock-real drift / hand-written mirrors / empty-state masking** | 09, 08, 07, 12, 03 | Pull `npm run api-boundaries` into `make mock-real-parity`; scan raw `fetch()`/HEAD in coverage check; generated-type conformance for mock responses; lint requiring `isError`+`refetch` on data hooks (error≠empty). |
| **Sibling read-model invalidation / stale identifier** | 05, 06 | Cross-read-model coherence tests (plan/map/home block IDs); home-feed cache invalidation test; require `invalidateTripReadModels` in trip-mutating hooks. |
| **Idempotency / side-effect duplication** | 05, 08 | Thread + assert `X-Idempotency-Key` on accept/vote/revert and settle pushes; duplicate-call tests. |
| **Non-atomic persistence / orphan + stranded state** | 03, 11 | Atomicity tests for direct trip create (mirror plan-similar); scheduled-task claim-then-restart recovery test. |
| **Content store drift (Postgres↔Qdrant)** | 12 | `check_seed_drift.py` subtree resolution + real/mocked Qdrant point-overlap assertion wired into post-seed + CI. |
| **Async DB on event loop** | 11, 15 | Keep `check_async_sync_db` ratchet; drain baselined post-trip handlers. |
| **Bearer-token / PII in logs/IDs** | 02, 01, 10, 15 | `_token_fp` everywhere + test that home-card `ref_id` ≠ raw token; shared `redact_tool_input_for_log()`; gate `/health/background-tasks` + verify trace files don't store raw content. |
| **External-call resilience** | 15 | Explicit `timeout=` on the Anthropic SDK client (CI grep, mirroring `check_httpx_timeout`); circuit breakers on Qdrant/geocoding. |
| **Release/preflight/deploy drift** | 14 | `make preflight-eas` green as the release gate; fix AASA smoke shape (`appIDs`); config check comparing `PUBLIC_INVITE_BASE_URL` host vs app associated-domains per EAS profile; Dockerfile healthcheck → `/health`. |

---

## 6. Suggested Fix Order

**A. Shortest path to first safe *internal* (TestFlight, trusted) dogfood**
1. P0-1 + P0-2 — owner deploy chain: `eas init` + real projectId + `pk_live_` key; bring up Fly + `travelagent.app`, `/health` green; `make preflight-eas` green. *(account-bound; start now)*
2. P0-3 — invite-context persistence across sign-in. *(cheapest code P0; unblocks 2nd user)*
3. The two security P1s most likely to bite even a trusted group: booking cross-trip IDOR (13) and public angle Personal-Memory leak (10) — both are simple auth scoping fixes.
4. Streaming chat quota (04) + background-LLM pause gate (11) — cap spend before real traffic.

**B. Path to a clean TestFlight submission (App Store review)**
5. Mic/audio disclosure alignment (14 P1) + finalized privacy policy (14 P1) + AASA smoke shape (14 P2) + Dockerfile `/health` (14 P3).
6. Add the structural gates for IDOR + privacy-leak + rate-limit so review-time regressions can't reappear.

**C. Path to external beta (real groups)**
7. Remaining privacy-to-group cluster: proposal redactor (01), private interjection routing (08), photo-learning scope (07/10), public story names (07).
8. Proposal trust loop integrity: apply-zero-mutation (05), revert false-success (05), accept idempotency (05).
9. Financial integrity: expense payer/share validation (13); booking UI honesty (13).
10. Coherence + content trust: home-feed cache (06), destination identity (03), seed-drift checker (12), Discover error-vs-empty (12).
11. Observability/cost hardening: Anthropic timeout (15), cost ceiling + attribution (15/04/11), claimed-task reaper (11).

---

## 7. Tests / Commands Summary (across reports)

| Command | Result | Source |
|---|---|---|
| `make contract-check` | **pass** (all areas that ran it; 210 paths / 241 ops) | 01,02,03,05,06,09,10,12,13,14 |
| `make api-coverage-check` | **pass** (175/175 covered, 0 drift) | 02,03,06,09,14 |
| `make mock-real-parity` | **pass** | 01,02,03,06,07,08,09 |
| `make golden-path-qa` | **pass** | 02,05,06 |
| `make doctor` | **pass** (warn: `uvicorn not found`) | 06,11,14,15 |
| `make preflight-eas` | **FAIL** (no EAS CLI; placeholder projectId) | 14 |
| `curl …/health` (fly + app) | **FAIL** (DNS / empty reply) | 14 |
| `scripts/check_route_auth.py` | **pass** (but blind spots noted) | 10 |
| `scripts/check_async_sync_db.py --ci` | **pass** (240 baselined, 0 new) | 11,15 |
| `scripts/check_httpx_timeout.py` | **pass** (0 missing) | 15 |
| `npm run api-boundaries` | **pass** (10 allowlisted; dynamic import missed) | 09 |
| targeted `pytest` suites | **pass** except **`tests/api/test_invites_api.py`** (1 stale-assertion failure) | most areas; fail in 02 |
| targeted `npm test` suites | **pass** | 01,03,04,06,07,08,09 |
| `check_seed_drift.py` test | pass (but checker logic gap, 12 P1) | 12 |

---

## Final Recommendation

**Fix now (this/next session — cheap, high-leverage, mostly code):**
- P0-3 invite-context persistence across sign-in (the only code P0).
- Booking cross-trip IDOR (13) and public angle `user_id` Personal-Memory leak (10) — small auth-scoping fixes, highest privacy/$$ blast radius.
- Photo-learning opt-in scoping (07/10) — one-line `uploaded_by_user_id` filter.
- Streaming chat quota parity (04) + close the `DISABLE_LLM_BACKGROUND_LOOPS` post-trip gap (11) — spend safety before any real traffic.
- Fix the red test `tests/api/test_invites_api.py:440` (02 P3) so the invite suite is green.

**Gate now (add the CI/lint guards so these classes can't regress):**
- Nested-resource trip-ownership test/lint (IDOR class).
- Privacy-phrase leak tests at group/public write boundaries.
- Rate-limit lint extended to wrapper/cost routes + streaming quota.
- `check_seed_drift` Postgres↔Qdrant overlap + subtree.
- Anthropic SDK `timeout=` grep (mirror `check_httpx_timeout`).
- `api-boundaries` folded into `make mock-real-parity`; raw `fetch`/HEAD coverage.

**Defer (real but lower urgency, or owner/phase-bound):**
- P0-1/P0-2 deploy chain is **owner/account work** — sequence per `OWNER-DEPLOY-CHECKLIST.md`; not a coding task.
- App-Store/legal items (14 P1/P2/P3) — required for submission, not for internal dogfood.
- Cost ceiling + attribution, circuit breakers, request-timeout middleware, mock-memory richness, AASA/Docker hygiene, audio-lifecycle (Phase 6b) — backlog after the privacy/auth/coherence cluster.

**Bottom line:** local self-dogfood is fine to continue today. Internal TestFlight is **blocked on the owner deploy chain + the one invite P0**. External beta additionally requires clearing the privacy-to-group + auth/financial-integrity P1 cluster — the same catastrophic-failure-mode class the product's moat depends on.
