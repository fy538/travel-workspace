# Pre-Dogfood Audit — Area 10: Data Layer / Migrations / Async DB

Date: 2026-05-20
Auditor: senior backend reviewer
Scope: `Travel Agent/alembic/`, `backend/core/db/`, RTBF (commit `125f711d`),
voice 30-day audio purge, async/sync DB on hot request paths, multi-table
write atomicity, hot-path index coverage.
Mode: read-only. No code changes proposed in this pass — fix directions only.

---

## Summary

The data layer is in mostly-good shape relative to what a first dogfood
needs. **Both gates pass cleanly**: `scripts/check_alembic_single_head.py`
reports `1 head(s) across 49 migrations`, and
`scripts/check_async_sync_db.py` reports `0 new violation(s), 0 stale
allowlist entries` (252 baselined sites). The 2026-05-11 squash baseline
plus the 2026-05-20 RTBF cascade are real, working pieces of work.

However, **three categories of finding survive the gates** and would bite
a real dogfood tester:

1. **RTBF cascade has two PII-survival holes** that the residual scan
   correctly detects but only *warns* about (does not auto-fix). The most
   concrete is `plan_events.actor_id` (FK SET NULL) — Alice's verbatim
   plan-edit notes survive in `plan_events.payload` after she deletes
   her account, with the actor link nulled but the content intact and
   joinable via `trip_id`. This is the closest thing to "PII that
   survives account deletion" the audit was asked to hunt for.
2. **Three multi-table writes on hot product paths are non-atomic**
   across separate connections/transactions: invite accept
   (`add_trip_member` → `consume_invite` → `append_trip_event`),
   plan-similar `create_trip_from_share` (5 sequential INSERTs), and
   trip-story section edit (read-modify-write across two connections).
   Each has a documented or undocumented partial-success state that
   produces either token-reuse, orphan trips, or lost-update bugs.
3. **The hottest read paths still block the event loop** on multi-call
   sync DB work. `GET /api/trips/{trip_id}/plan-state` runs at least
   five sync DB helpers inline in an async route (opened on every map
   tab); `backend/home/feed.py` has five sync calls remaining inline
   despite a docstring claiming they were all offloaded; the voice
   narrate route (`POST /api/trips/{trip_id}/concierge/narrate`) calls
   five sync helpers on a geofence-triggered hot path.

No irreversible/destructive operation found in any `upgrade()` body
(every `op.drop_table` / `op.drop_column` lives in a `downgrade()`).
Downgrades are present on every revision; 4 are intentionally empty
(3 merge revisions + 1 chain-stub) which is correct.

Hot-path index coverage is reasonable after `b9e4f1a2c3d5` (added
`ix_concierge_turns_user_id`, which the RTBF cascade depends on for
performant per-user delete sweeps) — but that index creation does NOT
use `CONCURRENTLY`, so a non-trivially-populated `concierge_turns`
table will be locked for the duration of the migration. Fine for
dogfood; flagged here for prod.

---

## Findings

### [P0] — RTBF cascade leaves `plan_events.payload` (verbatim user edits) tied to the deleted user's trip; residual scan logs a warning but never deletes

**References:**
- `Travel Agent/backend/core/db/account_deletion.py:227-238` — section F sweep keys ONLY on column literal name `user_id`.
- `Travel Agent/backend/core/db/account_deletion.py:68-76` — `_AUTHOR_COLUMNS` list of columns the residual scan inspects; does NOT include `actor_id`, `resolved_by`, `requested_by_user_id`, `consumed_by`, `holder_user_id`, `viewer_user_id`, `uploaded_by_user_id`.
- `Travel Agent/backend/core/db/account_deletion.py:283-291` — residual scan emits `logger.warning` for hits but does NOT delete; returns the dict in `summary["residual"]` instead.
- `Travel Agent/backend/core/db/_tables/itinerary.py:316-356` — `plan_events.actor_id` is `ForeignKey("users.id", ondelete="SET NULL")` and `plan_events.payload` is JSONB carrying per-block diffs that include user-typed text (block titles, notes).
- `Travel Agent/backend/core/db/_tables/itinerary.py:226-256` — `change_proposals.resolved_by` is also `SET NULL`; `change_proposals.payload` JSONB likewise survives.

**Why it matters to a real tester:**

The privacy promise is that account deletion erases personal content. The cascade gets nearly everything (FK CASCADE handles the long tail; section F handles bare-UUID `user_id` columns; section D handles `proposed_by` / `sender_id` / `paid_by` / `uploaded_by` / `initiated_by`). But the **payload bodies of audit / event tables stay intact** when the row's user link is `SET NULL`:

| Table | User-link column (post-delete state) | PII-carrying body column |
|---|---|---|
| `plan_events` | `actor_id` → NULL | `payload` JSONB carries the user's verbatim edits |
| `change_proposals` | `resolved_by` → NULL (when Bob resolved Alice's proposal) | `payload` keeps Bob's proposal body which may quote Alice |
| `trip_invites` | `consumed_by` → NULL | `contact_hint`, `pending_intake` stay until retention purge fires (30d cutoff) |
| `agent_events` | already handled by section F via `user_id` column — OK |  |

`plan_events` is the cleanest concrete example: Alice's trip-block edits (with whatever she typed: dietary notes, accessibility callouts, a relationship aside) are written to `plan_events.payload` by `_record_event` and stay forever, attributed to `actor_id=NULL` but joinable to the trip Alice and Bob co-authored — i.e. Bob can still see them post-deletion. The residual scan misses this because `actor_id` isn't in `_AUTHOR_COLUMNS`; even if it were, the scan only *prints a warning* — it does not delete or scrub.

The cascade architecture today is **structurally weak against new tables**: any future Alembic migration that adds a table with a user-attribution column whose name doesn't match `user_id` exactly, with FK SET NULL, will silently leak PII through any JSONB / Text body the row carries. There's no test that loops every `users.id`-referencing column and asserts the cascade reaches it.

**Repro / deterministic test idea:**

```python
@pytest.mark.requires_postgres
def test_plan_events_payload_purged_on_account_delete():
    alice = create_user(...)
    bob = create_user(...)
    trip = create_trip(created_by=alice.id, ...)
    add_trip_member(trip_id=trip.id, user_id=bob.id, role="member")
    # Alice edits a block — writes plan_events row with her note
    record_plan_event(
        trip_id=trip.id,
        event_type="manual_edit",
        source_type="manual_edit",
        actor_id=alice.id,
        payload={"new_title": "alice's secret cafe", "note": "I told the group I'm gluten-free"},
    )

    delete_user_data(alice.id)

    with get_connection() as conn:
        rows = conn.execute(
            select(plan_events).where(plan_events.c.trip_id == trip.id)
        ).mappings().all()
    assert rows == [], (
        f"plan_events should be empty after account deletion, "
        f"found: {[r['payload'] for r in rows]}"
    )
```

Today this test fails — `rows[0]['payload']` still contains Alice's note. Same pattern works for `change_proposals.payload` via the resolved-by path.

A second deterministic check: write a CI gate that introspects `metadata.tables`, enumerates every FK to `users.id`, asserts every column is either (a) handled in section D explicitly, (b) named `user_id` for section F to catch, or (c) on the documented allowlist of "intentionally retained editorial content" — and fails the build when a new migration adds a column that doesn't fit one of those three buckets.

**Suggested fix direction:**

Two complementary fixes:

1. **Promote the residual scan from warn-only to fix-and-fail.** Extend `_AUTHOR_COLUMNS` to include `actor_id`, `resolved_by`, `holder_user_id`, `requested_by_user_id`, `consumed_by`, `viewer_user_id`, `uploaded_by_user_id`. For each, either (a) add an explicit `_del(table, table.c.<col> == user_id, ...)` in section D, or (b) explicitly scrub the row's PII-bearing body columns (`payload`, `context`, `metadata`) to `{}` rather than just nulling the user link. Make `_scan_residual_references` raise (or write a `users.deletion_residual` audit row) instead of just `logger.warning` — silent leaks are the failure mode the cascade was written against.
2. **Add the CI introspection gate** described in the repro section as a `scripts/check_rtbf_coverage.py` lint that asserts every `ForeignKey("users.id", ...)` is one of: explicitly enumerated in account_deletion, FK CASCADE, or on a documented "editorial / aggregate analytics" allowlist (e.g. `place_angles.requested_by_user_id` with the existing "editorial content survives" comment).

**Confidence:** High. The cascade comment at `backend/core/db/account_deletion.py:283-285` explicitly says the residual scan is non-fatal — "the user row is gone — but a non-empty result means a data class slipped past the cascade and needs a code fix." This finding identifies two classes that slipped past.

---

### [P0] — Invite-accept multi-step write is non-atomic; a crash between `add_trip_member` and `consume_invite` lets a different user reuse the "single-use" token

**References:**
- `Travel Agent/backend/api/routes/invites.py:940-984` — `_accept_trip_invite` runs `is_trip_member` → `add_trip_member` → `consume_invite` → `append_trip_event` in four separate sync DB calls, no enclosing transaction.
- `Travel Agent/backend/core/db/trip_invites.py:234-306` — `consume_invite` docstring explicitly says: "The membership add-then-consume sequence is NOT inside a single transaction (would require widening the API-layer connection boundary), but the consume itself is the atomic gate ... a duplicate-membership unique constraint already prevents the prior `add_trip_member` call from creating two memberships."
- `Travel Agent/backend/core/db/trips.py:292` — `add_trip_member` opens its own connection + commits.
- `Travel Agent/backend/api/routes/invites.py:751-762` — the `invite.intake_received` event was already flagged in `dogfood-readiness.md` for logging raw tokens; here the audit `invite.consumed` event at line 972 is best-effort try/except that only logs on failure — even when intake/consume succeeds, a failed event write leaves no audit trail.
- `Travel Agent/scripts/check_async_sync_db_baseline.tsv:47-68` — every one of these helpers is on the allowlist (`add_participant`, `add_trip_member`, `append_trip_event`, `consume_invite`, `is_trip_member`) because they're all sync DB.

**Why it matters to a real tester:**

The `consume_invite` docstring is wrong about the duplicate-membership argument. The unique constraint prevents adding the *same* user twice — it does NOT prevent adding *different* users. Concrete failure scenario:

1. Bob taps Alice's single-use invite link (max_uses=1).
2. `add_trip_member(trip_id, bob)` succeeds. Bob is in the trip.
3. `consume_invite(...)` fails (network blip, process killed, FastAPI worker recycled, DB timeout). Invite row still says `consumed_at IS NULL` and `use_count=0`.
4. Bob retries — `_recover_consumed_invite` returns success because Bob is already a member. Fine.
5. **But Carol also has the link** (Alice posted it in a group Slack). Carol taps. `is_redeemable` passes (invite is still un-consumed). `add_trip_member(trip_id, carol)` succeeds (different user, no unique-constraint hit). `consume_invite` succeeds. Carol is in the trip.

End state: a max_uses=1 invite let two people in. For a launch-wedge product where invites carry **`pending_intake`** (the budget / dietary / accessibility chip answers that the dogfood-readiness audit P0 flagged as private), Carol receives Bob's intake-flow framing or Alice receives Carol's free text inadvertently attributed to Bob — privacy + correctness gone.

The window is small (between line 942 and line 961), but it's a real interleaving on flaky mobile networks where the dogfood is going to live.

A second issue on the same call sequence: the audit `invite.consumed` event at lines 971-984 is wrapped in `try / except Exception: logger.exception(...)`. If that write fails (Postgres briefly unavailable after consume succeeded), the audit row is missing and there's no record of who consumed the invite. The `trip_invites.consumed_by` column captures it for single-use, but multi-use links rely on `trip_events` as the per-consumption audit trail (per the docstring at `trip_invites.py:241-243`). Lost audit for multi-use shares.

**Repro / deterministic test idea:**

```python
@pytest.mark.requires_postgres
async def test_invite_token_reuse_after_consume_crash():
    organizer = create_user(...)
    bob = create_user(...)
    carol = create_user(...)
    trip = create_trip(created_by=organizer.id, ...)
    invite = create_invite(trip_id=trip.id, created_by=organizer.id, max_uses=1, ...)

    # Bob's accept: succeed at add_trip_member, then short-circuit before consume.
    with mock.patch(
        "backend.api.routes.invites.consume_invite",
        side_effect=RuntimeError("simulated network blip"),
    ):
        with pytest.raises(Exception):
            await _accept_trip_invite(invite, bob, invite.token, BackgroundTasks())

    assert is_trip_member(trip.id, bob.id) is True
    assert get_invite(invite.token).consumed_at is None  # token still "redeemable"

    # Carol now hits the same link — should fail, currently succeeds.
    response = await accept_invite(invite.token, BackgroundTasks(), None, carol)
    # Expected: 410 invite-not-redeemable, because Bob already consumed the implicit slot.
    # Current: 200 — Carol is in the trip, and trip now has 2 invited members from a max_uses=1 link.
    assert is_trip_member(trip.id, carol.id) is False, (
        "max_uses=1 invite admitted two different users via consume-failure window"
    )
```

**Suggested fix direction:**

Three options, in order of cleanness:

1. **Reverse the order: consume FIRST, then add member.** `consume_invite` is the atomic gate already; doing it first means a crash before `add_trip_member` leaves the user un-added but the invite consumed — they retry, `_recover_consumed_invite` sees `is_member=False` and returns `None`, the route then raises "invite not redeemable: consumed." That's a worse UX (legitimate user told their invite expired). Mitigation: if consumed && current user is NOT a member but `consumed_by == current_user`, re-add them as a member and return success. This makes the same-user retry idempotent without the cross-user reuse hole.
2. **Widen the transaction boundary.** Run `add_trip_member` + `consume_invite` + `append_trip_event` inside a single `with get_connection() as conn` block, passing `conn` into each helper. Requires plumbing a `conn=` parameter through three helpers — biggest blast radius, cleanest result.
3. **Add an idempotency table keyed by `X-Idempotency-Key`** (the header the frontend already sends per `Travel App/app/invite/[slug].tsx:126-149`, and which the backend currently ignores per `dogfood-readiness.md` P1). This is the cross-cutting fix and would also close the unrelated "lost-response retry" gap flagged in the dogfood-readiness audit.

**Confidence:** High. The code comment in `consume_invite` itself acknowledges the non-atomicity and articulates a load-bearing claim (duplicate-membership unique constraint) that is wrong against the multi-user adversary.

---

### [P1] — `GET /api/trips/{trip_id}/plan-state` runs 5+ sync DB calls inline in the async route; blocks the worker loop on every map/plan-tab open

**References:**
- `Travel Agent/backend/api/routes/plan_state.py:17-24` — `async def get_plan_state` returns `get_trip_plan_state(...)` directly, no `asyncio.to_thread`, no `run_in_executor`.
- `Travel Agent/backend/core/db/plan_state.py:686-749` — `get_trip_plan_state` calls `get_trip`, `get_trip_proposals`, `get_full_itinerary`, plus `list_booking_sessions_sync` at line 584 and `list_for_trip` at line 595 of the same module via interior helpers.
- `Travel Agent/backend/core/db/plan_state.py:55-61` — `_accommodation_entity_name` opens an additional `get_connection()` per typed accommodation lookup (N queries when multiple typed stays exist).
- `Travel Agent/scripts/check_async_sync_db_baseline.tsv:79` — `get_trip_plan_state` is allowlisted, so the lint passes.

**Why it matters to a real tester:**

`plan-state` is the read-model behind the Plan/Map tab — opened every time the user lands on a trip or pulls to refresh. The entire build runs at least 5 sequential round-trip queries on the event loop:

1. `get_trip(trip_id)` — single-row read.
2. `get_trip_proposals(trip_id, limit=80)` — fan-out to proposals + their votes/comments.
3. `get_full_itinerary(trip_id)` — fan-out to days + blocks + venue snapshots (this one is genuinely fat).
4. `list_booking_sessions_sync(trip_id)` — booking-session read.
5. `list_for_trip(trip_id, include_retired=False)` — trip accommodations read.
6. Per-accommodation `_accommodation_entity_name` round trips.

Each blocks the FastAPI worker's event loop while the next async request waits. A 50ms p50 per query × 5–10 queries = 250–500ms of blocking per Plan-state response. Under 5 concurrent TestFlight users opening the Plan tab simultaneously the worker stalls; with a single uvicorn worker (default) this serializes the whole API. The dogfood is going to look "slow" without any single query being slow — exactly the failure mode `scripts/check_async_sync_db.py` was written to detect, masked here by the allowlist.

The companion paths `backend/api/routes/concierge_narrate.py` (5 sync calls on the geofence trigger), `backend/notifications/group_interjection.py` (the 5-min loop scan), and the home-feed gaps below are the same shape on slightly less hot paths.

**Repro / deterministic test idea:**

Fire 20 concurrent `GET /api/trips/{trip_id}/plan-state` against the same trip from `pytest-asyncio` with `httpx.AsyncClient(app=app)`. Capture p50 and p99 latency. Then wrap the route body in `await asyncio.to_thread(get_trip_plan_state, ...)`. Re-run. The unblocked variant's p99 should drop materially (>30%) as a function of the executor's thread pool absorbing the concurrent DB work. The opposite result (no improvement) means the bottleneck is single-query DB time, not loop blocking — but observed inline-sync-on-async patterns almost always show the speedup.

**Suggested fix direction:**

Smallest-blast-radius fix: wrap the call in the route.

```python
@router.get("/plan-state", response_model=TripPlanState)
async def get_plan_state(trip_id: UUID, actor: User = Depends(get_current_user)) -> TripPlanState:
    require_trip_member(trip_id, actor)
    return await asyncio.to_thread(get_trip_plan_state, trip_id, viewer_id=actor.id)
```

Then update `scripts/check_async_sync_db_baseline.tsv` to remove the `backend/api/routes/plan_state.py	get_trip_plan_state` row (stale-allowlist gate will demand the removal once the new code is clean). Repeat the same one-line wrap for `concierge_narrate.py`'s five entries and the home-feed gaps below.

Bigger play (not required for dogfood): split `get_trip_plan_state` into an `async def` whose body uses `await asyncio.gather(...)` over the 5 reads concurrently. That cuts wall-clock too, not just unblocks the loop. But the simple `to_thread` wrap unblocks the loop today.

**Confidence:** High. The pattern is exactly the one the lint script's docstring describes as "throughput collapses but no one query is slow," and `plan-state` is the read that the frontend hits constantly (it's the proposal-review invalidation target called out in the dogfood-readiness audit's Positive Signals).

---

### [P1] — Multi-table write for "Plan similar" (`create_trip_from_share`) is non-atomic across 5 sequential INSERTs; partial-success leaves orphan trips with no membership row

**References:**
- `Travel Agent/backend/core/db/plan_similar.py:106-149` — 5 writes in sequence: `create_trip` → `add_trip_member` → `save_planning_brief` → `record_trip_source` → `log_share_event`.
- `Travel Agent/backend/core/db/plan_similar.py:124-126` — dedup is via `find_existing_derived_trip(share.id, user_id)` which reads from `trip_sources` (= step 4 above).
- `Travel App/app/(tabs)/discover/index.tsx:457-473` and the dogfood-readiness P1 finding — this is the "Plan similar to X" entry into a new trip; the next-phase product surface relies on it.

**Why it matters to a real tester:**

Each of the 5 INSERT helpers opens its own connection and commits. A crash, OOM kill, FastAPI worker rotation, or DB connection drop between steps produces:

| Crash after step | State | Consequence |
|---|---|---|
| 1 (create_trip) | Trip exists, no membership | User can't even open the trip — `require_trip_member` 403s. Retry: `find_existing_derived_trip` returns None (no `trip_sources` row), creates a second trip. **Two orphans.** |
| 2 (add_trip_member) | Trip + membership, no brief | User opens the trip, gets an empty plan. Retry: still creates a second trip (no `trip_sources` row). |
| 3 (save_planning_brief) | Trip + membership + brief, no source attribution | User has a working trip, but the dedup gate misses on retry — second trip created. Looks like a 2x bug to the user. |
| 4 (record_trip_source) | Step 4 succeeded, only step 5 missing | Retry: dedup hits, returns existing trip. **Idempotent — good.** |

The dedup gate (step 4) is the LAST functional INSERT, which means it can only suppress dupes when steps 1-3 succeeded — exactly the wrong end of the sequence. Most realistic crash points produce orphan trips that the user sees as duplicate empty Lisbon trips on their home screen.

There's no FK CASCADE that helps clean these up either: a trip with no members survives indefinitely until manually purged.

**Repro / deterministic test idea:**

```python
@pytest.mark.requires_postgres
def test_plan_similar_idempotent_under_crash_between_create_and_member():
    user = create_user(...)
    share = create_test_share(...)
    with mock.patch(
        "backend.core.db.plan_similar.add_trip_member",
        side_effect=RuntimeError("simulated crash"),
    ):
        with pytest.raises(Exception):
            create_trip_from_share(share.slug, user.id)

    # Now retry without the crash. Should return the SAME trip, not create a second one.
    trip = create_trip_from_share(share.slug, user.id)
    assert trip is not None
    trips = list_trips_for_user(user.id)
    assert len([t for t in trips if t.title == share.suggested_title]) == 1, (
        f"plan_similar created {len(trips)} duplicate trips after a crash mid-flow"
    )
```

Today: trip count is 2 (the orphaned half-built one + the retry's full one).

**Suggested fix direction:**

Move the entire 5-write sequence inside one `with get_connection() as conn` block so a crash rolls everything back to "no trip created." Each helper accepts an optional `conn=` parameter (the `account_deletion.py` cascade uses this exact pattern at line 115).

Cheaper interim fix: reorder so that `record_trip_source` runs FIRST after `create_trip`, before membership. Then `find_existing_derived_trip` is a real dedup against any half-built trip. Less elegant but smaller blast radius.

**Confidence:** Medium-high. The non-atomicity is mechanically visible; whether it triggers in real dogfood depends on worker restart frequency. With a single uvicorn worker on Fly's auto-rollout cadence, this is a realistic interleaving in the first week of TestFlight.

---

### [P1] — `backend/home/feed.py` docstring promises "every sync DB call offloaded" but five remain inline on the home-screen response path

**References:**
- `Travel Agent/backend/home/feed.py:503-505` — claims "PR3 fix: every sync DB call is now offloaded via `_to_async`. The loop stays responsive while DB queries run in the executor pool."
- `Travel Agent/backend/home/feed.py:786` — `list_expenses(trip_id)` direct sync call inside `async def assemble_home_feed`.
- `Travel Agent/backend/home/feed.py:795` — `get_shares_for_expenses(...)` direct sync.
- `Travel Agent/backend/home/feed.py:820` — `get_active_observations(user_id, trip_id=trip_id, category=None)` direct sync.
- `Travel Agent/backend/home/feed.py:874` — `experiences_by_ids([top.experience_id])` direct sync.
- `Travel Agent/backend/home/feed.py:892` — `get_angles_for_place(trip.place_id, written_only=True)` direct sync.
- `Travel Agent/scripts/check_async_sync_db_baseline.tsv:186-191` — all six baselined, so the lint passes silently.

**Why it matters to a real tester:**

The home feed renders on every cold app open and every pull-to-refresh of the Trips tab. The five remaining inline sync calls block the loop. The docstring lie is itself a hazard — a future developer will read it and assume the file is loop-safe, build on top, and ship a regression. The lint allowlist masks the gap.

Most of the un-wrapped calls are inside post-trip branches (`phase_info.phase == "post"`) — lower-frequency than the during-trip path that PR3 fixed — but the home feed is the place users land most often, and post-trip is where settlement / memory-highlight cards live; those are the cards the social-loop launch wedge depends on.

**Repro / deterministic test idea:**

Trivial: grep the file for `_to_async(` vs direct sync helper invocations and assert the latter is empty inside `async def assemble_home_feed`. Or: load-test the route with 10 concurrent users on a post-trip home feed; compare p99 before/after wrapping the remaining 5 calls.

**Suggested fix direction:**

Wrap each of the 5 sites in `_to_async(...)` consistently with the surrounding code; remove their entries from the baseline. Update the docstring or — better — delete the "every call is offloaded" claim and let the lint be the source of truth.

**Confidence:** High. Verified by line-by-line inspection.

---

### [P1] — Voice narrate route (geofence trigger) runs 5 sync DB calls inline; user-perceived latency on the highest-stakes "I'm at the place" moment

**References:**
- `Travel Agent/backend/api/routes/concierge_narrate.py:30-42` — imports `append_arc_entry`, `get_active_session`, `get_latest_personal_memory`, `list_recent_interactions`, `create_message`, `get_or_create_personal_trip_conversation` (all sync).
- `Travel Agent/scripts/check_async_sync_db_baseline.tsv:27-31` — five entries: `append_arc_entry`, `get_active_session`, `get_latest_personal_memory`, `list_recent_interactions`, `record_response`.

**Why it matters to a real tester:**

This is the route that fires when a user crosses a geofence at a place (Mateus speaking up about Mouraria) — the highest-stakes "place-aware concierge relationship" moment in the product. Every ms of added loop-blocking sits between the user crossing the threshold and the audio starting. The same pattern as plan-state, just on a hotter path where the user can physically feel the latency.

**Repro / deterministic test idea:**

Same shape as plan-state — concurrent narrate requests, measure p99, then wrap the sync helpers in `to_thread`.

**Suggested fix direction:**

Same as plan-state: wrap the calls inline at the route layer with `await asyncio.to_thread(...)`. The handler `handle_narrator_turn` itself is already async; only the DB helpers it depends on need offloading.

**Confidence:** High.

---

### [P2] — `update_trip_story_section` and `update_trip_story_photo_slot` are read-modify-write across two separate connections; concurrent edits silently clobber each other (lost-update)

**References:**
- `Travel Agent/backend/core/db/trip_stories.py:146-188` — `update_trip_story_section`: opens connection A inside `get_latest_trip_story` (reads `sections` JSONB), mutates Python list, opens connection B to write the full `sections` array back.
- `Travel Agent/backend/core/db/trip_stories.py:191-231` — same pattern for `update_trip_story_photo_slot`.

**Why it matters to a real tester:**

Trip Stories are the post-trip social-loop artifact (the launch wedge for follower-visible content). Two users editing different sections of the same story concurrently — perfectly reasonable on a group trip's shared retrospective — produce a lost-update:

1. Alice and Bob both fetch the story (each gets the same `sections` array).
2. Alice edits section "afternoon-1", writes the full array back.
3. Bob edits section "afternoon-2" (on his stale copy), writes the full array back.
4. Alice's "afternoon-1" edit is silently overwritten by Bob's stale copy.

No version column, no row-level locking, no optimistic concurrency token. The `updated_at` is set but never read for conflict detection.

**Repro / deterministic test idea:**

```python
@pytest.mark.requires_postgres
def test_concurrent_section_edits_dont_clobber():
    story = create_trip_story(... with sections=[s1, s2] ...)
    # Two clients read the same story
    story_a = get_latest_trip_story(story.trip_id, story.user_id)
    story_b = get_latest_trip_story(story.trip_id, story.user_id)

    update_trip_story_section(
        trip_id=story.trip_id, user_id=story.user_id,
        section_id=s1.id, body="alice's update",
    )
    update_trip_story_section(
        trip_id=story.trip_id, user_id=story.user_id,
        section_id=s2.id, body="bob's update",
    )

    final = get_latest_trip_story(story.trip_id, story.user_id)
    assert final.sections[0].body == "alice's update", (
        "Alice's section-1 edit was clobbered by Bob's stale-snapshot section-2 write"
    )
    assert final.sections[1].body == "bob's update"
```

(The interleaving needs to happen — pytest threads or `asyncio.gather` against the two sync helpers via `to_thread` reliably reproduces.)

**Suggested fix direction:**

Either (a) move the read + write into a single transaction and add `FOR UPDATE` row-locking, or (b) use a single `UPDATE ... SET sections = jsonb_set(sections, '{<idx>,body}', '"<body>"')` so the modify happens server-side in one round trip. Option (b) is the smaller change and removes the read entirely.

**Confidence:** High on the bug; severity is P2 because trip stories are post-trip and dogfood load is low. Worth fixing before any concurrent-edit UX ships.

---

### [TECH-DEBT] — `b9e4f1a2c3d5_add_missing_indexes.py` creates `ix_concierge_turns_user_id` without `CONCURRENTLY`; locks the table on prod-sized data

**References:**
- `Travel Agent/alembic/versions/b9e4f1a2c3d5_add_missing_indexes.py:17-21` — `op.create_index("ix_concierge_turns_user_id", "concierge_turns", ["user_id"])` with no `postgresql_concurrently=True`.
- `concierge_turns` is the per-turn telemetry table that's written on every concierge reply; in any non-tiny deployment this is the largest single table.
- The index is load-bearing for RTBF cascade speed (section F's `DELETE FROM concierge_turns WHERE user_id = $1`).

**Why it matters to a real tester:**

Pre-dogfood the table is small enough that the lock is invisible. The risk surfaces at first prod restore or first multi-thousand-user-day: the migration runs again on the populated table, takes an `ACCESS EXCLUSIVE` lock for the duration of the build, and queues every concierge_turn insert (= every concierge reply) behind it. Brief stall to total outage of the chat surface depending on table size.

**Repro / deterministic test idea:**

Seed `concierge_turns` with ~1M rows in a staging DB, time `alembic upgrade head` against the migration. Note duration. Then run the same migration with `op.create_index(..., postgresql_concurrently=True)` (also requires removing the autocommit context, or using `op.execute("CREATE INDEX CONCURRENTLY ...")` in a non-transactional Alembic context). Compare lock duration via `pg_stat_activity` during the run.

**Suggested fix direction:**

Convert the index creation to `CREATE INDEX CONCURRENTLY` form before the migration goes near a real prod load:

```python
def upgrade() -> None:
    # Cannot run inside a transaction — use the autocommit path.
    with op.get_context().autocommit_block():
        op.create_index(
            "ix_concierge_turns_user_id",
            "concierge_turns",
            ["user_id"],
            postgresql_concurrently=True,
        )
```

Same treatment for `ix_messages_status` (the partial index in the same migration). At dogfood scale today this is purely a hygiene fix; before any first real-user backfill it becomes mandatory.

**Confidence:** Medium. The lock impact depends on actual table size; the fix is well-understood Alembic idiom.

---

### [TECH-DEBT] — `b5e6a7d9c0f3_backfill_constraint_severity_by_type` downgrade is not a clean inverse; can promote unrelated rows from `strong`/`preference` to `absolute`

**References:**
- `Travel Agent/alembic/versions/b5e6a7d9c0f3_backfill_constraint_severity_by_type.py:40-50` — upgrade only flips `dietary + absolute → strong` and `language + absolute → preference`.
- `Travel Agent/alembic/versions/b5e6a7d9c0f3_backfill_constraint_severity_by_type.py:53-63` — downgrade unconditionally flips `dietary + strong → absolute` and `language + preference → absolute`.

**Why it matters to a real tester:**

If an operator (post-migration) intentionally sets a `dietary` constraint to `strong` because a user has a non-allergy preference they want stronger than the default, running `alembic downgrade` would promote that row to `absolute` and hard-exclude every non-matching venue — exactly the bug the upgrade was written to *fix*. Same on the language axis.

This is the "migration that loses information on reverse" smell — not as severe as data destruction, but the audit asks for reversibility-with-no-data-loss.

**Suggested fix direction:**

Either (a) accept it as a one-way data migration and document in the docstring that downgrade only reverses the migration's own writes for cohorts the migration created (which would mean tagging the rows the migration touched, e.g. via a marker in `metadata_` or a sentinel `updated_at` value, then downgrading only those), or (b) make the migration truly idempotent + reversible by sampling row counts before each direction and asserting the inverse matches.

Real-world: this category of fix-data migration is usually fine to flag as one-way and remove the downgrade entirely (`pass` with a docstring explaining why), which is more honest than the current "downgrade that lies about reversibility."

**Confidence:** Medium. The risk only fires if `alembic downgrade` is ever actually used on a populated DB — under the squash runbook the operator path is stamp-forward, not roll-back.

---

## Known / Accepted

These are observed-and-noted but explicitly out of scope for this audit or
already tracked elsewhere; recording them here so the next pass can see
they were considered.

- **No-op downgrades on 4 revisions** (`78fa859c2fa2`, `d0e1f2a3b4c5`,
  `e2f3a4b5c6d7`, `e9d0f1a2b3c4`): three are merge revisions
  reconciling diverged heads (intentionally empty per Alembic
  convention — there's no schema state to reverse), and one is a
  chain-stub fill for a missing link in the pre-squash history. All
  acceptable.
- **No `op.drop_table` / `op.drop_column` in any `upgrade()` body**:
  every destructive op lives in a `downgrade()` reversing a prior
  additive upgrade. The pre-squash `g6s7t8u9v0w1_drop_guide_sessions_table.py`
  archived in `_archive/` did genuinely drop a table; that's history
  that the squash baseline absorbed and no longer needs to be carried.
- **Alembic single-head gate is green**: 1 head across 49 migrations
  per `scripts/check_alembic_single_head.py`. The squash runbook
  (`docs/operations/Migration Squash Runbook.md`) is the operator
  path; followed correctly.
- **`scripts/check_async_sync_db.py` is green**: 252 baselined
  sync-on-async sites, 0 new violations, 0 stale entries. The lint
  works as designed — every finding above is on a site the baseline
  *intentionally* allowlists. The findings here argue that some of
  those allowlist entries are on hot enough paths to warrant
  graduating off the allowlist before dogfood.
- **`concierge handle_turn` itself is loop-safe** — `backend/concierge/agent.py`
  and `backend/concierge/session.py` have zero entries in the
  baseline, which means every DB helper they touch is already wrapped
  in `to_thread` / `run_in_executor`. Good.
- **Voice 30-day audio purge is correctly wired** — `purge_old_audio_recordings`
  in `backend/core/db/retention.py:86-102` is invoked by
  `scripts/purge_user_data.py:116-118` with `--audio-days 30`, called
  from `.github/workflows/cron.yml:187` on a daily 02:00 UTC schedule.
  The privacy-policy commitment to 30-day voice retention is honored
  on the existing-account side; account-delete cascade (CASCADE FK on
  `narration_audio_cache.user_id`) handles the immediate-delete side.
- **`narration_leases.holder_user_id`, `trip_photos.uploaded_by_user_id`,
  `trip_story_shares.owner_user_id`, `follows.follower_id/followed_id`**
  all CASCADE on user delete — RTBF picks them up via FK cascade in
  section G of the deletion. Not in `_AUTHOR_COLUMNS` but not a leak;
  worth adding to the residual-scan list anyway as defense-in-depth
  per the P0 fix above.
- **`place_angles.requested_by_user_id`** explicitly SET NULL by design
  per the column comment: "editorial content survives account deletion."
  Acceptable retention policy (the angle is a city-level editorial
  request, not personal PII), but worth surfacing on the allowlist
  for the proposed RTBF coverage CI gate.
- **`messages.parent_message_id` SET NULL on parent delete** means
  thread structure breaks when an upstream message is purged. By design
  — surviving messages stay, the reply just loses its anchor. Accepted.
- **`messages.content` of OTHER members that quote Alice survives**
  Alice's account deletion — text-level PII redaction is out of scope
  (no text-parsing scrubber). Documented in the privacy policy's
  "co-authored group content may remain for the other members" clause.
- **`prompt_calls.user_id` and `concierge_turns.user_id` are bare-UUID
  (no FK)** — section F catches both via the literal `user_id` name
  match. The new `ix_concierge_turns_user_id` index makes the per-user
  delete sweep performant.
- **`rate_limit_events.user_id` is TEXT** (not UUID) — the section F
  delete's `WHERE user_id == user_id_uuid` compiles to a string
  comparison after SQLAlchemy's parameter binding. Postgres handles
  the implicit UUID→TEXT cast cleanly given the canonical lower-case
  hyphenated form the writer side uses. Verified no functional gap.
- **The dogfood-readiness `P0 — Raw invite bearer tokens are logged
  and persisted`** (event payload at `invites.py:751-762` and `:936-947`)
  is in scope of the invite-related layer but tracked in
  `docs/audits/pre-dogfood-2026-05/dogfood-readiness.md`; not
  re-litigated here.
- **TR-1 `search_transport` disabled / G-10 transport-nudge dormant
  / S-5 allergen enforcement** are tracked in
  `docs/working/Known Gaps Register.md`; data-layer-adjacent but not
  this area's findings.
