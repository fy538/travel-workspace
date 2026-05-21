# Pre-Dogfood Master Punch List (v4)

Date: 2026-05-20
Source: the 12 area audits in `areas/` (read-only Cursor cloud-agent pass).
Raw findings: **21 P0 · 43 P1 · 36 P2 · 25 tech-debt = 125**. After merging cross-area
duplicates, ~110 distinct issues.

Each item is tagged `[NN]` with its source area file. Status tags:
**VERIFIED** = I checked the cited code this session · **BY-DESIGN** = matches a documented
decision, downgrade to Known/Accepted · **VERIFY** = plausible but re-check against a prior
carve-out before fixing.

---

## Headline

The earlier read ("privacy hardened; only deploy/ops left") is **wrong**. This pass found a
real, **verified** cluster of privacy leaks in the agent/notification *routing* layer — the
exact catastrophic failure mode (one member's private constraint reaching the group). The
basic invite/intake leaks were fixed last session; these deeper routing leaks are live and
were missed by audits v1–v4 because they live in the newest code (the social on-ramp and the
proactive-private dispatch path).

**There are now TWO true dogfood gates, both in-code-fixable during the Apple wait:**
1. **Gate A — Privacy-to-group cluster** (verified real; trust-unrecoverable if a tester hits it).
2. **Gate B — Deploy/release config** (no reachable backend; can't ship any non-mock build).

Everything else is correctness/polish that can largely be fixed-forward, but several Gate-C
items (proposal consent, photo GPS, RTBF) are close behind the gates.

---

## Gate A — Privacy leaks to the group (CATASTROPHIC — fix before any real group)

- **[08] P0 — "Private" proactive notifications land in the group conversation. VERIFIED.**
  `run_proactive_turn` (triggers.py:60) always opens the trip's *group* session;
  `target_audience`/`target_user_id` are documented as routing fields but never branch the
  session. Private taste/constraint nudges get persisted to the group `messages` row. Root of
  the cluster.
- **[01] P0 — Pre-trip group conversations bypass `strict_group_compose`. VERIFIED.**
  `strict_compose_active = … and is_group and has_trip` (agent.py:873; also 819/1063/1143). A
  `trip_id=None` group conversation (the 2026-05-20 social on-ramp) ships raw identity/constraint
  text with no Haiku launder, no identity/constraint check.
- **[08] P0 — `events_tonight` pastes raw Personal Memory (`markdown_content[:400]`) into the
  agent prompt → group chat.** High-frequency leak channel (fires daily on trips).
- **[08] P0 — Quiet hours bypassed on group push fan-out.** Per-recipient push ignores each
  member's quiet hours when a "group" notification fans out (gates filter triage *context*, not
  dispatch). Trust break, not a content leak.
- **[08] P1 — Booking-proposal / story_ready / shares_settled pushes inherit the same
  group-routing bug** (reuse `run_proactive_turn`).
- **[08] P1 — Triage prompt assembles per-member taste snippets *with names*** that the agent
  then carries into a group reply.
- **[01] P1 — `group_compose` constraint detector has no patterns for budget / fatigue /
  medical** — the exact vocabulary the proposal redactor already catches.
- **[01] P1 — Public profile `interests` filled by an LLM extractor with no privacy allowlist**;
  constraint phrases can reach the public payload.
- **[02] P1 — Public story sections are not scanned for constraint-shaped vocabulary.**
- **[05] P1 — `third_party_disclosure` guard is a no-op** (production channel is `"personal"`,
  guard expects `"private"`) — defense-in-depth that doesn't fire. (Also Gate H.)
- **[01] P2 — Group-profile aggregated constraints become deanonymizing in 2-person trips.**
- **[01] P2 — `follow_affinity.follower_count` leaks which followed user engaged when count=1.**

## Gate B — Deploy / release config (blocks any non-mock build)

- **[12] P0 — Production EAS build can't reach a backend:** both release hosts unreachable,
  `app.json` projectId still `0000…`, Fly app not initialised.
- **[12] P0 — Release-build leak guard validates USE_MOCK/SKIP_AUTH/Clerk but NOT the EAS
  projectId placeholder.**
- **[12] P0 — Five real-only error paths the mock never exercises** will hit a tester on first
  real traffic.
- **[03/12] P1 — AASA ships `REPLACE_ME` as the Apple Team ID** → iOS Universal Links (invite
  deep links) silently fail.
- **[12] P1 — `app.json` has no applinks fallback for the preview backend** → preview deep links
  break silently.
- **[09] TECH-DEBT — `.env.example` defaults `SKIP_AUTH=true`** (easy to mis-deploy).
- **[12] P2 — `_resolveBaseUrl` lets a mock-mode release build silently target localhost.**

---

## Gate C — High-priority correctness (fix alongside / right after the gates)

### Proposal trust loop & consent
- **[06] P0 — Revert never flips proposal status to `withdrawn`** → UI still shows "Accepted"
  with a live Revert button.
- **[06] P0 — "Force full revert" is silently a no-op** → users can't escape
  `diff_safe_partial`.
- **[06] P0 — `auto_approve` proposals bypass delegation prefs + `trips.voting_enabled`** →
  agent mutates the plan without consent. (Trust-critical.)
- [06] P1 — Double-accept race re-forks the itinerary → phantom version.
- [06] P1 — Diff shown to the user can drift from what the apply actually mutated.
- [06] P1 — `apply_accepted_proposal` title-match fallback can apply to the wrong block.
- [06] P1 — Vote-loss race at the deadline (cron auto-resolve vs late vote).
- [06] P2 — `_do_resolve` skip-detection wrong → reruns can re-apply the same proposal.
- [06] P2 — Diff-safe revert can DELETE an `add`-proposal block members later annotated.
- [06] P2 — `BlockChangedBanner` shows Undo for rejected/reverted/failed proposals → 409 on tap.
- [06] P2 — `revert_conflicts` shows raw UUIDs to the user.

### Photo / memory privacy & integrity
- **[07] P0 — Trip Story regenerate silently destroys photo assignments and (probabilistically)
  user edits.**
- **[07] P1 — GPS coordinates from every group photo leak to every other group member.**
- **[02/07] P1 — A member can attach another member's photo to their own public share.** (dup)
- [07] P1 — `group_and_learn` consent does nothing (no code reads the flag).
- [07] P1 — Default photo visibility is `group` with no per-upload consent moment.
- [07] P1 — Story composer ingests arbitrary user-typed block titles into the share prompt with
  no redaction.
- [07] P1 — Section edits funnel the full edited paragraph into an importance-8 observation that
  feeds Personal Memory synthesis.
- [07] P2 — `albumSectionPhotos` falls back to *private* photos as story slot fillers.

### Invite-token handling (bearer credentials) — VERIFY against prior carve-out
- **[03] P0 — Raw token persisted to `observations.provenance` at accept. VERIFY** (last session
  determined the invitee's *own* provenance is the allowed carve-out; confirm this is that line).
- **[03] P0 — `LogOnlyDispatcher` (default w/o Twilio/SendGrid) logs the share URL with the raw
  token. VERIFY** (likely real & new).
- **[03] P0 — Home feed `group_state` cards ship the raw invite token as `ref_id` to the client.
  VERIFY** (likely real & new — token leaves the server).
- **[03] P0 — Raw token logged when `add_trip_member`/`add_participant` raises a non-duplicate
  error. VERIFY.**

### RTBF / data atomicity
- **[10] P0 — RTBF cascade leaves `plan_events.payload` (verbatim user edits) tied to the
  deleted user's trip;** residual scan only logs a warning. Privacy/legal.
- **[10] P0 — Invite-accept multi-step write is non-atomic;** a crash between `add_trip_member`
  and `consume_invite` lets a *different* user reuse the "single-use" token. (Concurrency twin of
  the 03 token cluster.)
- [10] P2 — `update_trip_story_section`/`_photo_slot` are read-modify-write across two
  connections → concurrent edits clobber (lost-update).

---

## Gate D — Correctness / reliability (fix-forward acceptable)

### Cross-surface coherence (stale UI after mutation)
- **[04] P0 — `invalidateTripReadModels` does not invalidate Home cards.**
- **[04/12] P0/P1 — Destination identity splits between `trip_summary.destination` and
  `trip.place_id`;** `createTrip` from a destination card still discards `destination` even
  though the backend now has the field. (dup across 04 + 12)
- [04] P1 — Hardcoded plan-mutating tool allowlist in chat invalidation.
- [04] P1 — `voteOnProposal` only invalidates chat history; misses proposals/plan/home.
- [04] P1 — Mid-stream SSE failure / aborted turn never invalidates plan/map/home even when the
  backend committed the mutation.
- [04] P1 — `resolveMutation` closes the modal before the apply outcome is visible.
- [04] P2 — Home `staleTime: 60s` is the floor on cross-surface lag; `useTripMapState` shows mock
  Lisbon pins during first real fetch.

### Output-guard correctness (so week-1 `log` mode is meaningful)
- **[05] P0 — Confabulation/privacy violations ship unchanged in `log` mode. BY-DESIGN** (CLAUDE.md:
  log mode is the intended pre-launch + week-1 setting). Downgrade to Known/Accepted — BUT it's
  only acceptable if the guard actually *logs* useful data, which the P1s below break.
- [05] P1 — Grounding guard ignores production `result_preview` (JSON string) → tool-backed venue
  names never whitelisted → false positives.
- [05] P1 — `guard_reply` omits itinerary + traveler allow-lists → itinerary mentions false-flagged.
- [05] P1 — Hit-max-iterations can commit tool side effects without a coherent user reply.
- [05] P2 — guards evaluated after text is delivered on the streaming (voice/SSE) path.

### Notification respect / abuse
- [08] P1 — Daily cap is per-(user, trip) not per-user → multi-trip members can be spammed (20+/day).
- [08] P2 — Triage dispatches can slip out even when zero members pass gates.
- [08] P2 — Invite-intake dispatch skips per-user daily limit + per-trip interval.

### Auth / unauth routes / rate-limit
- [09] P1 — `/debug/tokens` and `/debug/cost` are unauthenticated on the live app.
- [09] P1 — `check_route_auth.py` passes clean but doesn't cover the full mounted route set.
- [02/09] P1/P2 — Unauthenticated public routes have no rate limits (card render + search/spatial
  are expensive). (dup theme)
- [09] P2 — `/health/external` is unauthenticated and triggers an outbound Anthropic `count_tokens`.
- [09] P2 — Multipart photo/receipt uploads have no API-level size cap.

### Async-DB latency on hot request paths
- [10] P1 — `GET /plan-state` runs 5+ sync DB calls inline (every map/plan-tab open).
- [10] P1 — `create_trip_from_share` ("Plan similar") non-atomic across 5 sequential INSERTs →
  orphan trips with no membership row.
- [10] P1 — `home/feed.py` claims "every sync call offloaded" but 5 remain inline.
- [10] P1 — Voice narrate (geofence) runs 5 sync DB calls inline → latency on the "I'm at the
  place" moment.

---

## Cross-cutting tech-debt (batch when convenient)

- **Multi-worker state**: in-process rate limits + idempotency caches don't coordinate across Fly
  machines — [02], [03], [08], [09], [02 plan_similar]. Decide Redis vs accept-per-pod for dogfood.
- **Mock/real contract drift** (mock hides real bugs): mock returns literal chip text as the
  privacy summary [01/03]; mock privacy preview skips the photo allowlist [02]; mock latency 120ms
  vs real p95 600–1500ms [12]; hand-written `Itinerary*` types duplicate generated [12].
- **Migrations**: `b9e4f1a2c3d5` index without `CONCURRENTLY` locks the table [10]; constraint-
  severity backfill downgrade isn't a clean inverse [10]; workspace vs `Travel Agent/docs/openapi.json`
  drift [03].
- **Guard/test hygiene**: output-guard tests diverge from prod `tool_calls` shape [05]; route-auth
  test only checks mutating methods [09]; story composer prompt un-tuned, no eval [07].
- **Misc**: Sentry plugin loads even when consent off [12]; deprecated `ImagePicker.MediaTypeOptions`
  in chat composer [12]; raw `Referer` stored in share analytics [02]; `list_followers/following`
  not self-gated [01].

---

## Area 11 (places/retrieval/cost/booking): clean

Zero P0/P1. Booking is deep-link-out for dogfood and the cost/cap/breaker posture held up.
Only minor P2/tech-debt — confirms the earlier read that this surface is dogfood-ready.

---

## Proposed fix order

1. **Wave 1 — Gate A (privacy-to-group).** Root fix: make `target_audience` actually route at
   the session layer (private → personal conversation) in `triggers.py`/`session.py`; drop the
   `has_trip` half of the strict-compose gate; stop injecting raw PM in `events_tonight`; add the
   missing budget/fatigue/medical constraint patterns; quiet-hours per-recipient on fan-out.
   Regression test each: a private/pre-trip turn must never write a constraint into a group surface.
2. **Wave 2 — Gate C consent + integrity:** proposal revert status + force-full-revert +
   auto_approve consent; story-regenerate data loss; photo GPS leak; RTBF `plan_events`; invite
   atomicity (after verifying the 03 token carve-out items).
3. **Wave 3 — Gate B deploy** (do in parallel with Apple wait): Fly init + reachable host, real
   projectId, AASA team id, leak-guard projectId check.
4. **Wave 4 — Gate D + tech-debt:** cross-surface invalidation, output-guard correctness,
   unauth routes/rate-limit, async-DB hot paths, then the cross-cutting batch.
