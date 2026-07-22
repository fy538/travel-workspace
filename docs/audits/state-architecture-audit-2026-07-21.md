---
doc_type: working
status: active
owner: engineering / design
created: 2026-07-21
last_verified: 2026-07-21
expires: 2026-08-20
why_new: Records the cross-repository state ownership and reconciliation audit, including current residual risks and implementation guidance.
source_of_truth_for: [state-architecture-audit-2026-07-21]
---

# State-Architecture Audit — 2026-07-21

**Scope:** read-only audit of application-state ownership, lifecycle semantics, mock/production parity, and reconciliation across `travel-agent` (backend) and `travel-app` (frontend). Nothing was modified; all uncommitted work was preserved and audited in place.

**Method:** 10 parallel domain investigations (A–J) plus direct diff-reads of the in-flight working tree. Every finding is tagged with a confidence class and cited to `file:symbol:line` + the relevant recent commit.

**Repos audited (real code):** `/Users/feihuyan/travel-workspace/travel-agent`, `/Users/feihuyan/travel-workspace/travel-app`. (The launch cwd `~/Documents/Claude/travel-workspace` is a symlink shell and holds no code.)

**Confidence legend:** `CONFIRMED` defect · `LIKELY RACE` · `ARCH RISK` (architectural) · `INTENTIONAL` duplication · `HARMLESS` derived state · `INSUFFICIENT` evidence.

---

## 1. Executive Summary

The system is, on the whole, **well-governed**: identity has a real hard gate, the backend concurrency model on the wedge (voting, settlement, membership) uses correct primitives (row locks, trips-first lock ordering, conditional-UPDATE claims, `revision` rebasing, partial-unique idempotency indexes), the money-settlement "two truths" separation holds, the chat supersede engine is deterministic for dispatched turns, the Atlas acceptance predicate is canonicalized on both sides, and the FE/BE chat clock contract genuinely agrees. Most domains show evidence of prior hardening passes that landed correctly.

The defects that remain cluster around **three architectural seams**, and the current in-flight branch sits on top of two of them:

1. **Home-bootstrap fan-out hydration has no reconciliation contract.** One `/api/me/home-bootstrap` payload is exploded into four+ React Query caches (`utils/hydrateHomeBootstrap.ts`). This single seam produces the audit's only **P0** (a notifications shape-mismatch that crashes the always-mounted `NotificationBell`), plus stale-representation risks (invite-accept refreshes 1 of 4 seeded caches) and is adjacent to the home composition split below.

2. **Selection/derivation authorities are materialized copies kept convergent by discipline, not by invariant.** `TripContext` holds the rendered trip list in local state (React Query is only an upstream feed); the Vesper home hero and card-deck are selected by two orthogonal mechanisms with **no shared grounding trip-id and no generation-id anywhere in the contract**. Both converge for the common case and diverge for multi-trip users / partial-hydration windows.

3. **Three independent clocks (`device now` / `dogfood_today` / server `now`).** The itinerary lane is now correctly destination-tz and h23, and the chat clock contract agrees — but the chat temporal context ignores `dogfood_today`/`mockNow`, so on a pinned dogfood/cert trip the guide reasons about the real date while every UI surface shows the pinned date.

The **uncommitted proposal-authorship feature** (new `authorship_origin` column + `proposal_eligibility.py`) is a genuinely *good* consolidation — it replaces ~6 scattered `== proposed_by` proxy checks with one canonical resolver and fixes a real cross-vocabulary hazard. But it ships with three issues: a **deploy-ordering hazard** (untracked migration vs. code that unconditionally reads the column → 500s every vote if code lands first), a **wire-level privacy regression** (`human_private_shielded` serialized to all viewers, defeating the diplomacy shield), and **mock defaults that invert the backend** (so the new gating is untested in dogfood).

**Headline counts:** 1 P0, 8 P1, 13 P2, 18 P3. The P0 and two of the P1s are introduced by the current uncommitted branch and should block its merge.

---

## 2. State Authority Matrix

Canonical owner → derived views → reconciliation rule, per domain. "Second authority?" flags where a copy can diverge from its source.

| Domain | Canonical owner | Derived / persisted views | Reconciliation precedence | Second authority? |
|---|---|---|---|---|
| **Identity** | Backend `User.id` (UUID), resolved from Clerk JWT `sub` (`travel-agent/backend/api/auth.py:113-189`) | FE `UserContext.profile.user.id`; `useCurrentUserId()` (fallback `user-5`) vs `useCurrentUserIdOrNull()` (uuid-guarded); `authSessionKey`=clerkUserId | JWT `sub` > backend UUID > Clerk name > `'Traveler'`; `authSessionKey` outranks `profileLoaded` for boundary detection | No — but the safe-hook invariant is unenforced outside `data/`+`hooks/` (P1-8) |
| **Trip selection** | Server trips (`get_trips_for_user`) via RQ `['trips',userId]` | **`TripContext` local `trips[]` (useState) is what renders**; `['trip',id]`; member-board; `currentTripId` | Optimistic write → local `trips[]`; every mutator invalidates `['trips']` to re-pull | **YES** — local `trips[]` is a materialized copy (P1-B / P1-2) |
| **Mock vs prod** | Backend HTTP (`httpApi`) | `mockApi` (synchronous); `useData` bridges | `USE_MOCK` build/runtime flag selects one; no reconciliation (mutually exclusive) | No (exclusive), but mock never exercises loading/error/401 (P3) |
| **Query/persistence** | Server truth via RQ queryFns | RQ cache (mem) + persisted `vesper:react-query-home:v2` (disk, busted per clerk id) + AsyncStorage/SecureStore | `setQueryData` (hydrate) marks fresh; queryFn on staleTime | Home-bootstrap seeds 4 caches from 1 payload; mutations must invalidate each (P0-1, P2-4) |
| **Home/Vesper** | `/concierge_home` feed assembler (hero + cards) | FE `useConciergeHomeState` fallback; mocks; persona fixtures | `noteText = backend ?? fallback`; `cards = backendHasCards ? backend : fallback` (**independent per-slot**) | **YES** — hero and cards select trips independently; no shared grounding id (P1-6, P2-2) |
| **Chat** | Server turn (SSE terminal metadata frame) | `deliveryPhase` + `isServerTurnActive` + 5 refs + `queuedTurns` (persisted); RQ `conversationMessages` | `beginTurn()` tears down prior turn; merge correlates user rows by sender+text+60s | Optimistic + persisted reconciled by merge; agent rows never suppressed (P2-9) |
| **Atlas** | `atlas_artifacts` row (`state` + `generation_status`) | `is_accepted_artifact` (BE) / `isAcceptedAtlasArtifact` (FE) = `kept AND ready`; shelf `items` list = `kept` incl. non-ready | Canonical surfaces gate on both axes; two FE consumers gate on `kept` only | No divergent hidden state; latent looser-predicate leak (P2-3) |
| **Planning/booking/settlement** | Each vocabulary owns its column; money = `compute_settlement()` ledger | `PlanCommitmentState` projection; `is_settled` display flag; booking `BOOKED_STATES` | Documented precedence in `_derive_commitment_state`; ledger is money truth, `is_settled` never decides closeout | No — separation holds (two-truths fix) |
| **Temporal** | Server `datetime.now(UTC)` (instant); client nominates IANA tz | itinerary=destination tz/h23; phase: FE device-tz, BE dest-tz; `dogfood_today`/`mockNow` overrides | Server owns instant; client owns tz label | **YES** — 3 clocks; chat ignores dogfood/mock overrides (P1-5, P2-7) |
| **Concurrency** | DB row + conditional-UPDATE claim | optimistic RQ + idempotency keys | Row lock serializes; `revision_stale`→rebase; loser 409 | No — backend authoritative, FE optimistic+rollback |

---

## 3. State Vocabulary / Glossary

### Identity
- `useCurrentUserId()` — returns the **mock fallback `user-5`** during cold start (risk hook).
- `useCurrentUserIdOrNull()` — null-until-hydrated, `isUuid`-guarded (safe hook).
- `authSessionKey` — account-boundary key: real=`clerkUserId`, mock=`mock:${personaId}`, skip-auth=`'skip-auth'`.

### Proposal authorship (NEW, uncommitted)
- `proposed_by` — **always** a user UUID; a durable audit principal, **not** always the semantic author.
- `authorship_origin` ∈ `human_group` (visible human; agent=false; can withdraw) · `human_private_shielded` (private human ask shown as Vesper; agent=true; **has** a human champion) · `vesper_autonomous` (agent=true; no human proposer).
- Invariant (write-time): `human_group ⇔ ¬agent`, enforced at `itinerary_proposal_gateway.py:491-493`.

### Proposal overlay vs. others
- Proposal `status`: `open/accepted/rejected/superseded/withdrawn` — distinct from itinerary block `status` (`draft/tentative/confirmed/cancelled`) and from apply-outcome (`change_applied` requires `accepted AND apply_succeeded`).

### Attendance vs. commitment vs. booking
- Attendance (`attendance_intention`): `attending/not_attending/undecided`.
- `PlanCommitmentState` (display projection): `open/tentative/confirmed/booked/booking_in_progress/handed_off/proposed/cancelled`.
- Booking: offer `status` (`available/selected/held_for_payment/confirmed`), `checkout_status`, `BOOKED_STATES={confirmed,booked,user_reported_booked}`.

### Settlement — two truths
- `is_settled` (per-share boolean) = **display flag only**; must never decide closeout existence.
- `net_balance` from `compute_settlement()` + `trip.settled` event = **money truth**.

### Atlas lifecycle
- candidate `status`: `pending/approved/dismissed` · artifact `state`: `composed/kept` (user intent) · `generation_status`: `pending/generating/ready/failed` (compose readiness) · `render_status`: `none/pending/ready/failed` (riso, dark) · `signal_state`: `signals_on/off/shareable` · signal `user_state`: `active/disputed/forgotten`.
- **Acceptance predicate = `state=='kept' AND generation_status=='ready'`** (canonical both sides).

### Chat states (not first-class enums; derived)
`idle · locally-queued · submitting · server-turn-active · receiving-tokens · visually-smoothing · reconnect-scheduled · reconnecting · terminal-success · terminal-failure · cancelled · superseded` — product of `deliveryPhase` (11-value union) + `isStreaming`/`isServerTurnActive`/`reconnectReason` + `MessageStatus(sent|sending|failed)` + 5 refs. `cancelled`/`superseded` are implicit.

### Temporal contexts
`system UTC` · `device tz` · `destination tz` · `explicit ISO offset` · `trip-local date` · `dogfood_today` · `mockNow`.

---

## 4. Transition Tables

### 4a. Trip selection

| From → event | currentTripId | trips[] | RQ `['trips']` | Notes |
|---|---|---|---|---|
| Cold launch | `null` | seeded, bootstrap hydrates then effect copies | seeded by hydrate | `tripsQueryHasPendingLocalHydration` masks empty-table flash |
| Tap B (A selected) | eager `selectTrip(B)`; layout re-affirms | unchanged | unchanged | converges |
| Deep-link B while A | layout effect `selectTrip(B)` | unchanged | unchanged | converges via effect |
| Rapid A→B→back | `lastSelectedTripIdRef` suppresses stale re-set | — | — | intended guard |
| Account switch | `null` | `[]` | re-keyed | `authSessionKey` boundary; no carry-over ✓ |
| `/api/me` UUID blip (same clerk id) | preserved | preserved | preserved | intentional |
| Archive | unchanged | status→archived optimistic | invalidate `['trips']` | **`['trip',id]` NOT invalidated → P1-2** |
| Delete empty | `null` | filtered | `removeQueries(['trip',id])`+invalidate | correct pattern ✓ |
| Deleted on other device | ghost id | dropped on refetch → `currentTrip=null` | refetch drops | fail-safe (P3) |

### 4b. Chat (authority per transition)

| State | Representation | Authority |
|---|---|---|
| idle | `deliveryPhase='idle'` | mount / scope reset |
| locally-queued | `queuedTurns[]` (persisted) | user (send while busy) |
| submitting | `deliveryPhase='sending'`, optimistic bubbles | user |
| server-turn-active | `isServerTurnActive=true` | server SSE (`onResponse`) |
| receiving-tokens | `deliveryPhase='responding'` | server SSE (`onTextDelta`) |
| visually-smoothing | `isStreaming` true, buffer drains | local timer (smoother) |
| reconnect-scheduled | `reconnecting`+`reconnectReason`, timer armed | SSE arms, local timer fires |
| reconnecting | id re-streamed | local timer / foreground / poller |
| terminal-success | `complete`, ids swapped | **server SSE terminal metadata** |
| terminal-failure | `failed` | server SSE / socket close |
| cancelled | `complete`+interrupted | user (Stop) |
| superseded | implicit: `abortRef()`+timers cleared | user (new turn → `beginTurn`) |

**Supersede engine** = `beginTurn()` (`useChatTransportLifecycle.ts:96-109`): `clearPollTimers` + `abortRef` + `textSmoother.cancel` + `setIsServerTurnActive(false)`. Deterministic **only for dispatched turns**; a turn *queued* behind a phantom active turn never runs it (see P1-3).

### 4c. Atlas acceptance

`composed` → (approve/keep) → `kept` + `generation_status: pending→generating→ready` → **accepted** (kept AND ready). `failed` generation ⇒ kept-but-not-accepted (canonical surfaces exclude; two FE consumers don't — P2-3). Invariant 2 (accepted can't disappear) HOLDS; invariant 1 (pending/failed can't appear accepted) latently violated.

### 4d. Home composition (the split)

```
/concierge_home ─┬─ hero  = phase ladder (active→imminent→shaping→returned)  ← trip H
                 └─ cards = _rank_cards by numeric priority (hold 96 > held 95 > proposal 94 > live 92)  ← trip C
FE fallback     ─┬─ note  = resolveLeadNote (phase ladder)
                 └─ cards = buildCards (priority; needs-you=98)
```
Hero sub-slots are mutually coherent; hero↔cards coherence is emergent (single-trip) and unbounded for multi-trip. `noteText = backend ?? fallback` while `cards = backendHasCards ? backend : fallback` → **real backend hero can sit over FE-invented cards for a different trip** (P1-6).

---

## 5. Persistence Inventory

### React Query — persisted to disk
| Key | Owner | Account scope | Schema ver | TTL | Bad-parse | Sign-out clear |
|---|---|---|---|---|---|---|
| `vesper:react-query-home:v2` (allow-list: profile, trips, member-board, open-proposals, concierge-home-feed) | `queryPersistence.ts` | busted per `clerk:${userId}` ✓ | manual `:v2` only (P3-4) | `maxAge` | discard ✓ | `clearPersistedHomeQueries` ✓ |

### AsyncStorage
| Key | Account scope | Sign-out clear | Note |
|---|---|---|---|
| `universal_search_recents_v1` | **GLOBAL** | **No** | cross-account leak (P2-5) |
| `universal_search_opened_entities_v1` | **GLOBAL** | **No** | cross-account leak (P2-5); `clear*()` has 0 callers |
| `vesper:deferred-safety-nudge:v1`, `deferredDiaryNudge`, `atlasLandingHint` | GLOBAL | No | may misfire once for next account |
| `atlas:last_scanned_at` / `_asset_count` / `_change_token` | device-bound | No | harmless |
| `atlas_timely_return_retirements_v1:{userId}` / `atlas_home_last_visit_v1:{userId}` | per-user ✓ | No (orphans) | harmless |
| `session_recovery_*` | GLOBAL | self-clears/30-min | ok |
| push `_DEVICE_ID_STORAGE_KEY` | device | **not on signOut** | P2-6 / P1-7 |

### SecureStore
| Key | Scope | Sign-out clear |
|---|---|---|
| Clerk token cache | Clerk | ✓ |
| `pending_invite_token` / `_claim` | anonymous, 2h TTL | ✓ |
| `voice.ghost_mode_v1` / `mic_disclosure_shown_v1` | **per-user** (`base:{userId}`) ✓ | No (orphans, ok) |
| device install id | device ✓ | No (correct) |

### Module-level singletons (survive `queryClient.clear()`)
`push.ts`, `location._cachedReading`, `deviceId._cached`, `gpsStream`, `onboardingDiaryScanBridge`, `personas._activePersonaId`, `now._overrideMs`. Almost all device-bound; only `onboardingDiaryScanBridge` + `location` are account-relevant (low).

---

## 6. Mock / Production Parity Matrix

| Concern | Mock | Production | Verdict |
|---|---|---|---|
| Sync vs async | synchronous, data always present | async `useQuery` | ARCH RISK — loading never exercised |
| Loading / error / 401 | never emitted (except dev force-state) | real | error/401/timeout paths untested in dogfood (P3) |
| Empty | fixture (often non-empty) | real empty | divergent |
| Mutation visibility | `useMockCache`+`setQueryData` | optimistic + invalidate | parity deliberate; mock skips server reconciliation |
| Persona switch | `resetMockClientState`+`queryClient.clear()` | N/A / account re-gate | correct both sides |
| **Proposal permission flags (new)** | `viewer_can_vote??true`, `proposed_by_agent??true`, `viewer_can_withdraw` always-false | backend `@default false` | **DIVERGENCE — P2-1**: "cannot vote" gate never fires, `isAuthor` always false in mock |
| Home-bootstrap notifications (new) | mock returns empty feed; `useNotificationsQuery` reads persona notifications | hydrate seeds cache from 1 round trip | hydration optimization never exercised in mock — **and the real path crashes (P0-1)** |
| 8s timeout / retry:1 | never hit | real | recoverable-error UX untested in mock |

---

## 7. Temporal Context Matrix

| Displayed / computed time | Owning "now" | Timezone | Formatter | Risk |
|---|---|---|---|---|
| Itinerary block times | fixed instant | destination tz | `formatBlockTime.ts` (h23) | OK; null-tz→UTC fallback (intentional) |
| Plan/map stop times | fixed instant | destination tz | `formatBlockTime` via adapters | map double-shift on bare HH:MM (P2-8) |
| Live destination wall-clock header | device `new Date()` | destination tz | `plan.tsx:411` | OK |
| **Now/next home card, trip phase (FE)** | `dogfood_today`??`mockNow`??device | **device tz** | `helpers.ts:computeTripPhase:116` | P2-7 |
| Trip lifecycle/countdown (BE) | `dogfood_today`??server | **destination tz** | `trip_phase.py:compute_trip_lifecycle:78` | P2-7 |
| **Chat model "today/tonight/tomorrow"** | **server `now(UTC)` only — ignores `dogfood_today`+`mockNow`** | device tz | `turn_context.py:191`→`temporal_context.py:85` | **P1-5 (the drift)** |
| Live clock label | device | device (h23) | `TripsHomeModel.ts:991` | fixed (`fb1209b2`) |
| Chat/expense/stay timestamps | device | device, **12h AM/PM** | `MessageBubble.tsx:292` etc. | P3 (cosmetic) |
| Trip date ranges | date-only | UTC-noon anchor | `PlanDaySection.tsx:510` | OK |

**Test cases:** midnight→`00:00` (fixed) · noon/midnight am-pm eliminated in itinerary lane (h23) · DST correct display+write (two-pass) · device≠destination date → phase off-by-one (P2-7) · explicit-offset ISO → instant respected but re-localized to `tz??UTC` (P3) · null tz → explicit UTC fallback (intentional) · mock instant provenance unverified (INSUFFICIENT).

---

## 8. Findings — Ranked P0–P3

### P0 — user-facing crash, from the uncommitted branch

**P0-1 · Home-bootstrap seeds the notifications cache with the wrong shape → `NotificationBell` crash.** `CONFIRMED`
`utils/hydrateHomeBootstrap.ts:15` does `setQueryData(queryKeys.notifications(userId), bootstrap.notifications)` with a raw `APINotificationFeed` **object**, but that query key returns `AppNotification[]` (mapped by `mapNotificationFeed`, `data/notifications.ts:62,184`; no `select`). `setQueryData` marks it fresh and `staleTime:5min` means the queryFn never re-runs, so the raw object is served and `NotificationBell` (always mounted on Trips-home, `NotificationBell.tsx:36`) calls `.filter` on an object → `TypeError`. Re-corrupts on every profile refetch (`UserContext` re-seeds). `tsc` misses it (`setQueryData` loosely typed); the added test `__tests__/utils/hydrateHomeBootstrap.test.ts` asserts the raw feed is stored by reference — **encoding the bug**. Commit anchor: uncommitted working tree (backend `home_bootstrap.py` `notifications` field + FE hydrate line).

### P1 — confirmed defects / high-risk

**P1-1 · Deploy-ordering: `authorship_origin` migration untracked while code reads it unconditionally.** `ARCH RISK` (operational)
`alembic/versions/proposalauthor01_proposal_authorship_origin.py`, `backend/core/proposal_eligibility.py`, `backend/api/services/notification_feed.py` are **untracked**; `create_itinerary_operation_proposal` INSERTs `authorship_origin` (`itinerary_proposal_gateway.py:509`) and the locked vote SELECT reads `change_proposals.c.authorship_origin` (`:302`). If code ships before the migration, **proposal-create and every itinerary vote 500** (missing column). Matches the prior prod-deploy incident pattern (scan untracked `.py`, migrate before deploy).

**P1-2 · Archive/cancel/recover invalidate `['trips']` but not `['trip',tripId]` → stale single-trip status.** `CONFIRMED`
`TripContext.tsx:731/904/810` invalidate only `queryKeyPrefixes.allTrips()`=`['trips']`, which does not prefix-match `['trip',tripId]` (`data/trips.ts:181`). Screens on `useTrip(tripId)` (trip-settings, trip-info, `conversations/create`, `useRouteTrip`) keep the pre-mutation status until that key's staleTime. `deleteEmptyTrip` does it right (`removeQueries(queryKeys.trip(id))`, `:777`) — proving the intended pattern.

**P1-3 · Chat `in_flight` recovery branch omits the supersede flag (incomplete fix of `424d52a0`).** `LIKELY RACE`
`useConciergeChat.ts:859-871` (mirror `useGroupChat.ts`): `recoverDuplicateInFlight` leaves `isServerTurnActive=true` until `onDone` (`:904`), so a new turn sent in that window is **queued, not dispatched** — `beginTurn`/`clearPollTimers` never runs, and the exponential-backoff history-invalidation poll chain (`useConciergeReconnectRecovery.ts:122-140`, ~43s/7 attempts) survives the newer turn. Commit `424d52a0` fixed only the reconnect branch. Also never restores `deliveryPhase` off `'reconnecting'`, so the queued turn can't drain (`useChatTurnQueue.ts:76-86`).

**P1-4 · Wire-level privacy: `human_private_shielded` serialized to all viewers.** `ARCH RISK` (privacy), from the uncommitted branch
`proposals.py:337,1031` return raw `authorship_origin` in `ProposalSummary`/`ProposalDetail` to every member. The client only needs the already-computed `viewer_can_vote`/`viewer_can_withdraw` booleans. Previously `proposed_by_agent=true` collapsed autonomous-Vesper and shielded-human into one bucket; the new field **re-separates them on the wire**, so a member inspecting the API learns a "Vesper" proposal was a hidden member's private ask — defeating the shield `_propose_present.py:589-596` exists to preserve. Secondary inference channel: `missing_voter_ids` excludes the shielded human proposer (`eligible_voter_ids`→`is_human_proposer`), so the "who still needs to vote" list silently omits them. Currently latent (no FE branches on the field yet).

**P1-5 · Chat temporal context ignores `dogfood_today`/`mockNow` → guide vs. UI date drift.** `CONFIRMED` (dogfood/cert) / `ARCH RISK` (prod)
`load_temporal_context`→`build_temporal_context` uses `datetime.now(UTC)` with no dogfood/mock plumb (`turn_context.py:191`, `temporal_context.py:85`), while home-feed/phase/notifications all honor `dogfood_today_override(trip)`. On a pinned dogfood/cert trip the guide reasons about the real date while the UI shows the pinned date ("Day 2 of 4" on screen; "your trip is in 3 weeks" from Vesper). Dominant defect on the exact surfaces used for screenshots and device-cert demos.

**P1-6 · Real backend hero rendered over FE-invented fallback cards.** `CONFIRMED`
`utils/conciergeHomeFeedModel.ts:49` sets `noteText = backendFeed?.lead_note.text ?? fallback` while `:72-73` sets `cards = backendHasCards ? backend : fallback`. The designed "meaningful hero, quiet queue" state (real hero, no cards) makes the FE fill the queue from `useConciergeHomeState.buildCards` at a different snapshot → a `source:"vesper"` trip-A hero sits above a FE `needs-you` card (priority 98) for trip B, and the backend's authored quiet is overridden with invented cards. No shared grounding id to detect it.

**P1-7 · 401-forced sign-out tears down almost nothing.** `LIKELY DEFECT` (session hygiene)
`utils/api/http.ts:273-307` (`redirectToSignIn`, from 401 in `http.ts:418,539` and `sse.ts:315`) only stashes the route and routes to session-recovery. It does not `queryClient.clear()`, `clearPersistedHomeQueries()`, or `unregisterPushNotifications()` — unlike `AuthUserProvider.signOut` (`:58-88`). Session expiry → different account on same device: account A's in-memory + persisted caches survive until B refetches, and the device push token stays registered to A on the backend (A's pushes land on B's device). `TripContext.authSessionKey` partially catches the trip residue.

**P1-8 · Identity convention guard covers only `data/`+`hooks/`; `app/`+`components/` network callers rely on an unenforced gate.** `ARCH RISK`
`__tests__/conventions/backendIdentityBoundary.test.ts:5` scopes enforcement to `['data','hooks']`. ~12 network-authority call sites use the fallback-returning `useCurrentUserId()` (clearest: `conversations/create.tsx:240` `created_by: userId`; also trip-dates/trip-info/plan/changes membership gate/object composer/venue+experience save-take/trip-settings leave/notifications register/VoiceOverlay send). They are safe **only** because `BackendProfileGate` (`app/_layout.tsx:262-414`) sits above them — an invariant undocumented at the call sites and unenforced by any test. Any sibling-of-gate modal or future pre-hydration mount sends `user-5` (backend 422s → spurious failure, not cross-account read, because user-id params are UUID-typed).

### P2 — architectural risk / lower-impact confirmed / parity

| # | Finding | Class | Evidence |
|---|---|---|---|
| P2-1 | Mock proposal-permission defaults invert backend → new gating untested in dogfood | ARCH RISK | `mock/helpers.ts:55-58`, `mock/social.ts` vs `schema.gen.ts` `@default false` |
| P2-2 | Hero and now_card can bind different trips; no shared grounding/generation id in contract | ARCH RISK | `producers.py:208,219`; `models.py:596` (`hero_voice_context.trip_id` `exclude=True`) |
| P2-3 | Place "memories here" + Trips returned-desk render non-ready kept artifacts as accepted | ARCH RISK (latent) | `app/place/[placeSlug].tsx:161-169`; `app/(tabs)/trips/index.tsx:554-557,630-639` (missing `generation_status` gate) |
| P2-4 | Invite-accept invalidates 1 of 4 seeded home reps (misses `userTripMemberBoard`, `userOpenProposals`) | ARCH RISK | `app/invite/[slug].tsx:689-693` vs `hydrateHomeBootstrap.ts:12-15` |
| P2-5 | Global AsyncStorage keys leak across accounts on shared device | CONFIRMED (low) | `universalSearchRecents.ts:7`, `universalSearchOpened.ts:7` (no userId; `clear*` unused) |
| P2-6 | Delete-account skips push deregistration | LIKELY DEFECT | `app/atlas/account.tsx:217-263` vs `:158`; INSUFFICIENT on backend device cascade |
| P2-7 | FE phase (device tz + `mockNow`) vs BE lifecycle (dest tz + `dogfood_today` only) → off-by-one + override-set mismatch | ARCH RISK | `helpers.ts:116` vs `trip_phase.py:78` |
| P2-8 | `tripMapStateAdapter` double-shift on bare `HH:MM` (zoneless 1970 anchor → device-local parse → re-project) | LIKELY RACE (conditional) | `tripMapStateAdapter.ts:32,386,568` |
| P2-9 | Duplicate assistant bubble after accepted-disconnect with partial text | LIKELY RACE | `reconcileMessages.ts:18-43` (agent rows never suppressed) + `useConciergeReconnectRecovery.ts:74-82` |
| P2-10 | Optimistic trip status reverted by concurrent background refetch | LIKELY RACE | `TripContext.tsx:276-293` (sync effect preserves only `travelers`, not optimistic `status`) |
| P2-11 | Per-share settle has no FE idempotency key (safe only via backend share-state claim) | HARMLESS (brittle) | `useSettleShares.ts`/`useSettleOwedShares.ts`→`http.ts:1378,1385`; backend `expenses.py:~1339-1395` |
| P2-12 | Restaurant confirmation writes block `status='confirmed'`; flight/hotel offer confirmations don't | ARCH RISK | `itinerary_booking_projection_gateway.py:204` vs `:143,249` |
| P2-13 | `HomeBootstrapResponse.notifications` required-typing hides deploy-ordering (undefined path self-heals; object path = P0-1) | ARCH RISK | `interface.ts:214`, `schema.gen.ts:13194` |

### P3 — harmless derived / cleanup / test / low

| # | Finding | Class |
|---|---|---|
| P3-1 | Trip role reset on every list refetch (fail-safe toward less privilege) | ARCH RISK (fail-safe) |
| P3-2 | `selectTrip` fired in 3 places (mitigated by `lastSelectedTripIdRef`) | LIKELY RACE (mitigated) |
| P3-3 | Ghost `currentTripId` after selected trip leaves list (reads go through `find`) | HARMLESS |
| P3-4 | Persisted RQ cache has only manual `:v2`, no per-entry schema version | ARCH RISK |
| P3-5 | Skip-auth `authSessionKey` is a constant (dev-only stale state) | ARCH RISK (dev) |
| P3-6 | `profileLoaded` non-monotonic blip can remount whole tree (not a leak; `retry 2→1` shrinks window) | LIKELY RACE (mitigated) |
| P3-7 | Queued turn wedges on non-`complete`/`idle` terminal phase (manual `sendQueuedNow` exists) | ARCH RISK |
| P3-8 | `refetchOnReconnect` history refetch ungated by turn identity (safe via merge) | HARMLESS |
| P3-9 | Explicit-offset ISO re-localized to `tz??UTC` for display | ARCH RISK |
| P3-10 | Non-itinerary timestamps still 12h device-local (`StayCompare`, `MessageBubble`, `ExpenseDetail`) | INTENTIONAL (cosmetic) |
| P3-11 | Atlas near-you count uses `items.length` not accepted `total` | HARMLESS |
| P3-12 | Dogfood artifact validator doesn't enforce `kept ⇒ ready` | ARCH RISK |
| P3-13 | `get_kept_artifact_place_labels` uses `kept` only (no ready gate) — scoring substrate | HARMLESS |
| P3-14 | Durable Vesper cards carry stale generation, no revision id (timestamps dropped on wire) | ARCH RISK |
| P3-15 | Enum-contract guard weakened (subtracts trip+consent vocab; loses receiver-type awareness) | ARCH RISK (test) |
| P3-16 | Chat vote + membership mutations lack wire idempotency keys (backend idempotent anyway) | INTENTIONAL (low) |
| P3-17 | `clamp_to_balance=True` on manual settlement route (creditor net≤0 direct repayment 409s; unreachable today) | ARCH RISK (edge) |
| P3-18 | Synchronous mock never exercises loading/error/401/timeout paths | ARCH RISK (coverage) |

---

## 9. Evidence Index (per finding: file · symbol · commit)

- **P0-1** `travel-app/utils/hydrateHomeBootstrap.ts:15` · `hydrateHomeBootstrapCaches` · uncommitted; consumer `data/notifications.ts:62,184`, `components/ui/NotificationBell.tsx:36`.
- **P1-1** `travel-agent/alembic/versions/proposalauthor01_*.py` (untracked) · `itinerary_proposal_gateway.py:302,509` · uncommitted; table `core/db/_tables/itinerary.py:419`.
- **P1-2** `travel-app/context/TripContext.tsx:731,810,904` vs `:777`; keys `utils/queryKeys.ts:397`, `data/trips.ts:181` · commit `e1702bbe` (trip-start area).
- **P1-3** `travel-app/hooks/useConciergeChat.ts:859-871,904`; `hooks/useConciergeReconnectRecovery.ts:122-140`; `hooks/useChatTurnQueue.ts:44,76-86` · commit `424d52a0`.
- **P1-4** `travel-agent/backend/api/routes/proposals.py:337,1031`; `backend/core/proposal_eligibility.py:60-90`; `backend/concierge/tool_handlers/planning/_propose_present.py:589-596` · uncommitted.
- **P1-5** `travel-agent/backend/concierge/turn_context.py:191`; `backend/core/temporal_context.py:85`; `backend/core/dogfood_dates.py` · commit `62a17f7d`.
- **P1-6** `travel-app/utils/conciergeHomeFeedModel.ts:49,72-73`; `hooks/useConciergeHomeState.ts:918,1055` · commits `9ad06c7b`, `2c7a229b`.
- **P1-7** `travel-app/utils/api/http.ts:273-307,418,539`; `utils/api/sse.ts:315`; `context/AuthUserProvider.tsx:58-88` · commit `9293b336`.
- **P1-8** `travel-app/__tests__/conventions/backendIdentityBoundary.test.ts:5`; `app/conversations/create.tsx:240`; `components/auth/BackendProfileGate.tsx`; `app/_layout.tsx:262-414` · commit `2eaa4a3e`.
- **P2-1..13 / P3-1..18** — see the tables in §8 (each row carries its `file:line`).

Recent-commit context that is **correct** (verified, not defects): `2b88f418`/`cc64127c` (concurrency races + harness), `0e2729b0` (Atlas projector/timeline acceptance gate), `32e9f9b0` (FE Atlas predicate unification), `fb1209b2`/`8c2f1422`/`7fa0fbc5` (temporal h23/destination consolidation), `d52d2d30` (PostGIS read fix, not concurrency), `9af75f9c` (advisory-lock card lifecycle), `8ade3313`/`2fd77c8b` (private-output/telemetry sanitization).

---

## 10. Reproduction Scenarios (P0–P2)

- **P0-1** Real-auth sign-in → `fetchMyProfile` seeds `['notifications',userId]` with the raw feed → Trips-home mounts `NotificationBell` → `notifications.filter(...)` throws → error boundary. Heals only after explicit refetch (pull-to-refresh).
- **P1-1** Point the app at a DB pinned to `atlasrailcopy01` (pre-migration) and run the create-proposal or itinerary-vote path → 500 (`column change_proposals.authorship_origin does not exist`).
- **P1-2** As organizer, archive trip X (card drops to Past) → immediately open Trip Settings for X (cached route) → `useTrip` still returns `status:'active'`, settings shows live-trip affordances while the home card shows archived.
- **P1-3** Send turn A → force a duplicate/409 (`kind='in_flight'`) → within the same tick send turn B → B enters `queuedTurns` and A's backoff `invalidateHistory` timers keep firing (never cleared by any dispatched turn).
- **P1-4** Create a proposal from a private (non-group) thread → `GET /trips/{id}/proposals` as another member → response shows `authorship_origin:"human_private_shielded"` (and the author is absent from `missing_voter_ids`).
- **P1-5** Dogfood trip pinned `dogfood_today=2026-08-14` (mid-trip). Home shows "Day 2 of 4." Ask the guide "what's on for tomorrow?" → it grounds "tomorrow" on the real 2026-07-21, resolves an out-of-trip date, contradicts the itinerary.
- **P1-6** Backend returns a real hero for active trip A + empty card queue; FE cache also holds trip B with a hero-read → `buildNeedsYouCards` emits a priority-98 card for B → home shows hero(A) over card(B).
- **P1-7** Let a session expire (401) → bounce to session-recovery → sign in a different account on the same device → account A's persisted home caches render until B refetches; backend still pushes A's notifications to this device.
- **P2-3 / P2-2 / P2-8 / P2-9 / P2-10 / P2-4 / P2-5** — see the per-row repro in §8 (each is triggered by: a `kept+generating` artifact existing; a multi-trip user with a higher-priority non-hero card; a bare-`HH:MM` block round-tripped through mapstate; an accepted-disconnect with partial text + reconnect refetch; a tab blur/focus mid-archive; joining a trip via invite then reading the member board; user B signing in after A on a shared device).

---

## 11. Recommended Target Architecture

Stated per seam as **canonical owner → derived views → reconciliation rule → lifecycle boundary** (no generic "one global store").

**Seam 1 — Home-bootstrap hydration.** Owner: server `HomeBootstrapResponse`. Derived views: the individual RQ caches. Reconciliation rule: hydration must pass each field through the **same transform the field's queryFn uses** — introduce a per-key `hydrate(bootstrapField) → cacheShape` adapter registry so `notifications` is `mapNotificationFeed`-ed before seeding (fixes P0-1 structurally, not just this instance). Lifecycle boundary: bootstrap seeds; each domain's mutations own subsequent invalidation. Add a "seeded-representation" registry so a mutation touching a bootstrap-embedded resource invalidates **every** representation (fixes P2-4).

**Seam 2 — Trip selection.** Owner: RQ `['trips',userId]` (server). Derived view: `TripContext` should be an **overlay** carrying only `currentTripId` + optimistic patches, reading trip *bodies* from RQ (via `tripCachePatch`, which already patches list+detail coherently) rather than copying into local `useState`. Reconciliation rule: optimistic writes go through `tripCachePatch` to **both** `['trips']` and `['trip',id]` (fixes P1-2 and P2-10 by construction; collapses the second authority P1-B). Lifecycle boundary: `authSessionKey` change resets selection only.

**Seam 3 — Home composition.** Owner: `/concierge_home` feed. Add a **feed-level `grounding` block**: `{ trip_id, generation_id }` plus per-card `generation_id`. Reconciliation rule: the FE renders backend hero+cards **together or not at all** — if the backend returns a hero with an empty queue, that IS the state (render quiet), never backfill from a different snapshot (fixes P1-6). Invariant to encode + test: "when hero and a card share a narrative context they share `grounding.trip_id`; a card older than the feed's `generation_id` is stale." Document the intentional exception (always-on hero) as an explicit `hero_independent: true` flag rather than emergent behavior.

**Seam 4 — Temporal.** Owner: server instant; single client-nominated tz. Reconciliation rule: the concierge temporal path must consume the **same** `now` resolver as home-feed/phase (thread `dogfood_today`/`mockNow` into `build_temporal_context`), so there is exactly one "today" per request (fixes P1-5, and P2-7 by making FE phase consume server lifecycle rather than recomputing on device tz).

**Seam 5 — Proposal authorship (in-flight).** The consolidation is right; finish it: (a) **wire projection** — never emit raw `authorship_origin` to non-authors; collapse `human_private_shielded → vesper_autonomous` on the wire and keep the `viewer_can_*` booleans as the only client contract (fixes P1-4); (b) land the migration + module **before** the reading code (fixes P1-1); (c) mock fixtures mirror backend defaults + add author/can't-vote cases (fixes P2-1).

**Seam 6 — Chat supersede.** Owner: `beginTurn()`. Reconciliation rule: make **every** recovery branch (reconnect *and* in-flight) set `isServerTurnActive=false` and restore `deliveryPhase`, so a new turn always takes the dispatch path and `clearPollTimers` runs (fixes P1-3, P3-7). Treat `refetchOnReconnect` history as server-truth reconciliation (keep; it's safe via merge) but never as a supersede path.

**Seam 7 — Atlas acceptance.** Owner: `is_accepted_artifact`. Reconciliation rule: the two out-of-module consumers (Place, Trips desk) must call `isAcceptedAtlasArtifact`, not raw `items` (fixes P2-3); add the `kept ⇒ ready` validator to the dogfood schema (fixes P3-12).

**Seam 8 — Sign-out/account teardown.** Owner: one `teardownSession()` routine invoked from **both** context `signOut` and the 401 `redirectToSignIn` and delete-account paths, clearing RQ + persisted caches + push registration + the account-relevant global stores (fixes P1-7, P2-5, P2-6).

---

## 12. Staged Remediation Plan

**Stage 0 — Block-the-merge (this branch, before it lands).**
1. P0-1: map before seeding notifications in `hydrateHomeBootstrap.ts` (or drop the seed line); fix the test to assert mapped shape.
2. P1-1: commit the migration + `proposal_eligibility.py` + `notification_feed.py`; verify import-test + migration-before-code deploy order.
3. P1-4: stop emitting raw `authorship_origin` to non-authors.
4. P2-1: mock fixtures mirror backend `false` defaults + add the two missing coverage cases.

**Stage 1 — Safe consolidations (no contract change).**
5. P1-2 / P2-10: route trip optimism through `tripCachePatch` (list+detail); stop wholesale-overwriting optimistic `status` in the sync effect.
6. P1-3 / P3-7: add `setIsServerTurnActive(false)` + phase restore to the in-flight recovery branch (both concierge and group mirrors).
7. P2-4: extend invite-accept invalidation to `userTripMemberBoard` + `userOpenProposals` (use `refreshGlobalTripsHome`).
8. P2-3: point Place + Trips-desk consumers at `isAcceptedAtlasArtifact`.

**Stage 2 — Contract changes.**
9. Seam 1: per-key hydration adapter registry + seeded-representation invalidation registry.
10. Seam 3: add `grounding {trip_id, generation_id}` to `ConciergeHomeFeed`; render backend hero+cards atomically; FE stops backfilling.
11. Seam 4/P1-5/P2-7: thread `dogfood_today`/`mockNow` into the concierge temporal path; FE phase consumes server lifecycle.
12. Seam 8: single `teardownSession()` wired into `signOut` + 401 + delete-account (P1-7, P2-5, P2-6).

**Stage 3 — Migrations / backfills.**
13. Itinerary block `status` write consistency (P2-12): decide and codify whether offer confirmations should advance block status; backfill if the answer changes existing rows.
14. Persisted-cache schema versioning (P3-4): per-entry version so a shape change busts stale entries, not just the manual `:v2` key.

**Stage 4 — Test additions.**
15. Convention test scope → `app/` + `components/` (P1-8), or make `useCurrentUserId()` throw outside a hydrated profile.
16. Invariant tests: home `grounding.trip_id` coherence (P2-2); `kept ⇒ ready` dogfood validator (P3-12); a mock/prod parity test that asserts fixture permission defaults equal backend defaults (P2-1).
17. A multi-actor chat test for the in-flight supersede path (P1-3), and a home-bootstrap hydration shape-contract test (P0-1 regression).

**Stage 5 — Observability.**
18. Counter on `useData.reportError` already exists — add a dashboard alert on masked-empty notification/hero fetches (P2 masking class).
19. Deploy-time check: fail CI if a route/gateway references a column whose migration is untracked (P1-1 class).
20. Emit `feed.generation_id` + per-card age so the client (and telemetry) can detect stale durable cards (P3-14).

---

*Prepared read-only. The single most important near-term action is Stage 0: three of its four items (P0-1, P1-1, P1-4) are defects introduced by the current uncommitted branch and should gate its merge.*
