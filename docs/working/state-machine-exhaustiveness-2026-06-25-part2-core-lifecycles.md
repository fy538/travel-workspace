# State-Machine Exhaustiveness Audit — Part 2: Core Lifecycles — 2026-06-25

> **RESOLVED 2026-06-26 — findings below are a historical record; the criticals are now fixed.**
> Closed in the 2026-06-24..26 fix sprint via `travel-agent` commits `e9c9abe1`
> (*close 36 lifecycle defects from exhaustiveness audit*), `20ff2168` (stay-saga atomicity),
> `31d2544b` (3 migrations), and `ef6c52f7` (booking-hold + plan-event-cursor hardening).
> Spot-verified at HEAD:
> - **Booking/change proposal terminal-escape (the headline critical)** — FIXED: confirm/reject
>   and revert paths now carry conditional `from_status=` guards
>   (`backend/api/routes/proposals.py:631,752`); unconditional terminal-state UPDATEs are gone.
> - Invite atomicity — `consume_and_add_trip_member` now wraps consume + membership in one
>   transaction with a redemption-ledger INSERT (`travel-agent` commit `01c84afa`).
>
> Treat this as the diagnostic record behind those fixes, not an open backlog. Reconcile any
> remaining "Recommended Sequence" item against HEAD before acting.

## Summary

This audit covers five core lifecycle machines: Change proposal lifecycle, Booking proposal + booking agent, Trip phase + conversation→trip promotion, Stay candidates & votes, and Plan commitment + block state. Across these machines, 20 defects were confirmed from the adversarial verification pass: 5 critical, 8 high, 5 medium, and 2 medium/high. The single worst issue is the booking proposal terminal escape pair — any authenticated trip member can call `POST /proposals/{id}/confirm` or `/reject` on a terminal-status row and the unconditional `UPDATE` succeeds, because neither route nor DB function carries a `WHERE status='pending'` guard. The change proposal and booking proposal machines are both materially defective; the stay candidates machine has two critical and two non-trivial defects; the plan commitment machine has three confirmed defects including a booking resurrection bug via delayed webhooks. No machine in this batch is clean.

---

## Confirmed Defects

### 1. Change Proposal — Dead state `expired`: DB CHECK constraint rejects every write; open proposals are never cleaned up after replan

**Severity:** High (root cause of defects 1 and 2, and the orphan-state defect)

**Location:** `backend/core/db/change_proposals.py:172` (write); `backend/core/db/_tables/itinerary.py:317-320` and `alembic/versions/73a1ca90a2ef_initial_schema.py:3781` (constraint); `backend/concierge/tool_handlers/planning/_plan.py:886-897` (swallowing caller)

**What breaks:** The DB CHECK constraint `ck_change_proposals_change_proposals_status` permits only `('open','accepted','rejected','superseded','withdrawn')`. `expire_open_proposals_for_trip` writes `status='expired'`, which PostgreSQL rejects with a `CheckViolation`. The caller at `_plan.py:895` wraps the call in a bare `except Exception` and proceeds. After every replan, all pre-replan proposals remain `status='open'` with `affected_block_ids` pointing to blocks that no longer exist in the new itinerary version. The FE at `VoteWidgetCard.tsx:95`, `BlockProposedBanner.tsx:51`, and `VesperReceipt.tsx:207` all branch on `status === 'expired'` — those branches are permanently unreachable dead code.

**Exploit:**
1. Trip has open proposal P touching block B on itinerary version V1.
2. Organizer triggers a full replan; `expire_open_proposals_for_trip` is called, raises `CheckViolation`, exception is swallowed. P stays `status='open'`.
3. New itinerary version V2 is live; block B no longer exists.
4. A member opens the changes screen; P surfaces as a live pending proposal.
5. Another member votes on P; `vote_on_proposal` acquires `FOR UPDATE` and writes the vote — P still has no itinerary context.
6. Auto-resolution or organizer accepts P; `apply_accepted_proposal` tries to resolve `affected_block_ids` against V2 — all UUID lookups fail, title-match fallback may mutate the wrong block or records `apply_status='failed'`. The plan silently corrupts or produces a misleading accepted-but-not-applied outcome.

**Fix:** Either (A) change `expire_open_proposals_for_trip` line 172 to write `status='withdrawn'` (already in the constraint, semantically appropriate for "plan replaced") and update all callers and FE branches, or (B) add a new Alembic migration that extends the CHECK constraint to include `'expired'`. Option A is a two-line change and ships without a migration. Option B makes the FE's dead branches live but requires a coordinated schema change. Remove the bare `except Exception` at `_plan.py:895-898` or at minimum assert `count > 0` after the call so failures surface.

```python
# tests/core/db/test_expire_proposals_constraint.py
import pytest
from uuid import uuid4
from backend.core.db.change_proposals import (
    create_change_proposal,
    expire_open_proposals_for_trip,
    get_trip_proposals,
    get_change_proposal,
)

@pytest.mark.integration
def test_expire_open_proposals_transitions_rows_and_removes_from_open_list(
    db_session, make_trip, make_user, make_itinerary
):
    trip_id = make_trip()
    user_id = make_user()
    itinerary_id = make_itinerary(trip_id)

    p1 = create_change_proposal(
        trip_id=trip_id, proposed_by=user_id, itinerary_id=itinerary_id,
        proposal_type="swap", title="Swap museum", description="Switch to gallery",
        affected_block_ids=[uuid4()],
    )
    p2 = create_change_proposal(
        trip_id=trip_id, proposed_by=user_id, itinerary_id=itinerary_id,
        proposal_type="add", title="Add dinner", description="Add rooftop dinner",
        affected_block_ids=[uuid4()],
    )

    count = expire_open_proposals_for_trip(trip_id)

    assert count == 2, (
        f"Expected 2 rows updated; got {count}. "
        "CheckViolation is likely being raised and swallowed."
    )
    assert get_trip_proposals(trip_id, status="open") == []
    for pid in (p1.id, p2.id):
        refreshed = get_change_proposal(pid)
        assert refreshed.status != "open"
        assert refreshed.resolved_at is not None
```

---

### 2. Booking Proposal — REST confirm endpoint writes to terminal proposals: no status guard on UPDATE

**Severity:** Critical

**Location:** `backend/api/routes/booking.py:490` → `backend/core/db/booking_proposals.py:91-98`

**What breaks:** `mark_booking_proposal_confirmed` issues `UPDATE booking_proposals SET status='confirmed', confirmed_at=now WHERE id=:id` with no `WHERE status='pending'` clause. The route reads the existing row and checks `trip_id` membership but never inspects `existing.status`. Any terminal status — `rejected`, `expired`, or `superseded` — can be overwritten to `confirmed` by any trip member. The mirror defect exists on the reject endpoint (finding 3 below).

**Exploit:**
1. Concierge confirm triggers; proposal transitions to `rejected`.
2. A second trip member (or a network retry) POSTs `/proposals/{id}/confirm`.
3. Route fetches row — `status='rejected'`, `trip_id` matches, actor is a member — all checks pass.
4. `mark_booking_proposal_confirmed` fires `UPDATE SET status='confirmed'` unconditionally.
5. The rejected proposal is now `confirmed`; push notification fires; the home card resurfaces.

**Fix:** Add `if existing.status != "pending": raise HTTPException(status_code=409, detail="Proposal is already closed")` in the confirm route immediately after the `trip_id` check (booking.py line 489), before calling `mark_booking_proposal_confirmed`. Apply the same guard to the reject endpoint. As defence-in-depth, add `AND status='pending'` to the WHERE clause in both `mark_booking_proposal_confirmed` and `mark_booking_proposal_rejected` and treat zero rowcount as a 409 signal at the route layer.

```python
# tests/booking/test_booking_proposal_terminal_escape.py
import pytest
from unittest.mock import patch, MagicMock
from uuid import uuid4

TRIP_ID = uuid4()
PROPOSAL_ID = uuid4()
ACTOR_ID = uuid4()

def _make_proposal(status: str):
    return MagicMock(id=PROPOSAL_ID, trip_id=TRIP_ID, status=status, user_id=ACTOR_ID)

@pytest.mark.asyncio
@pytest.mark.parametrize("terminal_status", ["rejected", "expired", "superseded"])
async def test_confirm_refuses_terminal_proposal(terminal_status, authed_client):
    with (
        patch("backend.core.db.booking_proposals.get_booking_proposal",
              return_value=_make_proposal(terminal_status)),
        patch("backend.core.db.booking_proposals.mark_booking_proposal_confirmed") as mock_write,
    ):
        resp = await authed_client.post(f"/trips/{TRIP_ID}/proposals/{PROPOSAL_ID}/confirm")

    assert resp.status_code == 409, (
        f"Expected 409 for terminal status '{terminal_status}', got {resp.status_code}"
    )
    mock_write.assert_not_called()
```

---

### 3. Booking Proposal — REST reject endpoint writes to terminal proposals: no status guard on UPDATE

**Severity:** Critical

**Location:** `backend/api/routes/booking.py:525` → `backend/core/db/booking_proposals.py:105-113`

**What breaks:** `mark_booking_proposal_rejected` issues `UPDATE booking_proposals SET status='rejected', rejected_at=now WHERE id=:id` with no `WHERE status='pending'` guard. A confirmed proposal can be re-opened and rejected, destroying the temporal integrity of `confirmed_at` and leaving `session_id` still pointing at an orphaned booking session. The concierge tool path correctly guards via `_check_loaded_proposal_state` (state_preconditions.py:257); the REST path has no equivalent.

**Exploit:**
1. User confirms a booking via the concierge tool — proposal is `confirmed`, push sent, receipt rendered.
2. A rogue trip member POSTs `/proposals/{id}/reject`.
3. Route fetches row — `confirmed`, trip membership passes.
4. `mark_booking_proposal_rejected` fires unconditionally: `status='rejected'`, `rejected_at=now`.
5. `confirmed_at` is preserved but `status='rejected'` — an incoherent terminal state. Home-feed cache is evicted; booking receipt is corrupted.

**Fix:** Same pattern as finding 2: add `if existing.status != "pending": raise HTTPException(409, "Proposal is already closed")` in the reject route after the `trip_id` check (booking.py line 524). Add `AND status='pending'` to the `mark_booking_proposal_rejected` WHERE clause as defence-in-depth.

```python
@pytest.mark.asyncio
@pytest.mark.parametrize("terminal_status", ["confirmed", "expired", "superseded"])
async def test_reject_refuses_non_pending_proposal(terminal_status, authed_client):
    with (
        patch("backend.core.db.booking_proposals.get_booking_proposal",
              return_value=_make_proposal(terminal_status)),
        patch("backend.core.db.booking_proposals.mark_booking_proposal_rejected") as mock_write,
    ):
        resp = await authed_client.post(f"/trips/{TRIP_ID}/proposals/{PROPOSAL_ID}/reject")

    assert resp.status_code == 409, (
        f"Expected 409 for status '{terminal_status}', got {resp.status_code}"
    )
    mock_write.assert_not_called()
```

---

### 4. Stay Candidates — `withdraw_candidate` has no status guard: `chosen → withdrawn` corrupts the choose saga

**Severity:** Critical

**Location:** `backend/core/db/trip_stay_candidates.py:159-176` (`_set_status`); `backend/api/routes/stay_candidates.py:122-135` (DELETE endpoint)

**What breaks:** `_set_status` builds its WHERE clause using only `id` and `trip_id` — no `AND status != 'chosen'` predicate. The DELETE route calls `withdraw_candidate` without ever inspecting `candidate.status`. A candidate in `status='chosen'` mid-saga (after `claim_candidate` commits but before `link_chosen_accommodation` runs) can be moved to `withdrawn` by any authorized organizer or the candidate's adder. `link_chosen_accommodation` then finds no `status='chosen'` row and returns None. `release_candidate` requires `status='chosen'` (line 143) — finds `'withdrawn'` — silently no-ops. The `trip_accommodations` row committed by `create_accommodation` (including the retirement of the prior primary stay) is permanently orphaned. All other mutation endpoints (`vote_for_candidate` line 147, `choose_stay_candidate` line 221) guard with `if candidate.status != "active"` — the DELETE is the only endpoint that omits this pattern.

**Exploit:**
1. Trip has booked primary stay P. Organizer calls `/choose` on candidate X.
2. `claim_candidate` commits: X.`status='chosen'`.
3. `create_accommodation` commits: new accommodation Q created; P is retired.
4. Concurrent DELETE arrives; `_set_status` fires with no guard: X goes `chosen → withdrawn`.
5. `link_chosen_accommodation` finds no `status='chosen'` row → returns None.
6. `release_candidate` finds `status='withdrawn'` — no-op.
7. Final state: P permanently retired, Q is active primary with no candidate link, X is `withdrawn`. Trip accommodation state is corrupted with no error surfaced.

**Fix:** Add `if candidate.status in ("chosen", "withdrawn"): raise HTTPException(status_code=409, detail="Cannot withdraw a candidate that is chosen or already withdrawn")` in `remove_stay_candidate` immediately after the authz check (stay_candidates.py line 134). Additionally add `AND status NOT IN ('chosen')` to `_set_status`'s WHERE clause when called from `withdraw_candidate`, or add a separate `withdraw_candidate` helper that includes a status precondition. The sagas's `finally` block compensation also needs to be hardened (see finding 11 below).

```python
async def test_withdraw_chosen_candidate_is_rejected(
    async_client, trip_with_two_organizers, active_candidate
):
    trip_id, organizer_a, organizer_b = trip_with_two_organizers
    candidate_x = active_candidate

    from backend.core.db.trip_stay_candidates import _set_status
    _set_status(trip_id, candidate_x.id, "chosen")  # simulate mid-saga

    resp = await async_client.delete(
        f"/api/trips/{trip_id}/stay-candidates/{candidate_x.id}",
        headers=auth_headers(organizer_b),
    )
    assert resp.status_code == 409

    from backend.core.db.trip_stay_candidates import get_candidate
    refreshed = get_candidate(candidate_x.id)
    assert refreshed.status == "chosen"
```

---

### 5. Change Proposal — Race condition: two concurrent `/revert` requests both mutate the itinerary before the status guard fires

**Severity:** Critical

**Location:** `backend/api/routes/proposals.py:657-731`; `backend/core/db/proposal_apply.py:1195-1382` (`revert_accepted_proposal_v2`)

**What breaks:** The `/revert` route reads `proposal.status` via a plain `SELECT` (no `FOR UPDATE` lock) and checks `status != 'accepted'` at line 661. Neither that read nor the subsequent call to `revert_accepted_proposal_v2` holds a row lock. `revert_accepted_proposal_v2` does not re-check proposal status before mutating the itinerary. The only serialization point — `UPDATE ... WHERE status IN ('accepted',)` at line 725 — fires after the itinerary is already mutated. In the version-restore path: R1 creates V(N+1) from V(N-1); R2 then reads the updated history and creates V(N+2) from V(N) — the post-accept version — silently undoing R1's revert. The proposal ends up `withdrawn` while the itinerary HEAD reflects the post-accept state. R2 receives a 404 and the organizer sees no indication that the undo failed.

**Exploit:**
1. Accepted proposal P has `apply_status='succeeded'`. Organizer double-taps 'Undo' — two concurrent POSTs R1 and R2 in-flight.
2. Both read `proposal.status='accepted'`; both pass line 661.
3. R1 calls `revert_accepted_proposal_v2` (version-restore path) → creates V(N+1) from V(N-1).
4. R2 calls `revert_accepted_proposal_v2` → reads history as [V(N-1), V(N), V(N+1)] → `history[-2] = V(N)` → creates V(N+2) from V(N), the post-accept version, undoing R1's revert.
5. R1 wins `db_resolve` → proposal is `withdrawn`. R2 gets NotFoundError → 404.
6. Net state: proposal `withdrawn`, itinerary HEAD is the post-accept version. Revert silently failed. No error surfaced.

**Fix:** Add a `SELECT ... FOR UPDATE` on the proposal row inside an explicit transaction that spans the status check, the itinerary mutation, and the conditional UPDATE — mirroring the pattern used by `vote_on_proposal` at `change_proposals.py:524`. Alternatively, atomically do `UPDATE change_proposals SET status='in_revert' WHERE id=? AND status='accepted' RETURNING *` before calling `revert_accepted_proposal_v2` and roll back if the update returns zero rows. The diff-safe path degrades to benign idempotency with the current code; the version-restore path is the harmful sub-case that requires the lock.

```python
# tests/api/test_proposal_revert_race.py
import threading
from unittest.mock import patch
from uuid import uuid4
import pytest

def test_concurrent_revert_version_restore_creates_exactly_one_version():
    proposal_id = uuid4()
    trip_id = uuid4()

    history_call_count = 0

    def fake_get_history(tid):
        nonlocal history_call_count
        history_call_count += 1
        # First call sees [v1, v2]; second sees [v1, v2, v3] after R1 committed
        if history_call_count == 1:
            return [_make_itinerary(1), _make_itinerary(2)]
        return [_make_itinerary(1), _make_itinerary(2), _make_itinerary(3)]

    created_versions = []

    def fake_create_version(**kwargs):
        v = _make_itinerary(len(created_versions) + 3)
        created_versions.append(kwargs)
        return v

    # ... patch setup omitted for brevity; see full stub in verified defects ...

    results = [None, None]
    errors = [None, None]

    def run(idx):
        try:
            results[idx] = revert_accepted_proposal_v2(proposal_id, force_version_restore=True)
        except Exception as exc:
            errors[idx] = exc

    t1 = threading.Thread(target=run, args=(0,))
    t2 = threading.Thread(target=run, args=(1,))
    t1.start(); t2.start(); t1.join(); t2.join()

    assert len(created_versions) == 1, (
        f"Expected 1 new itinerary version, got {len(created_versions)}. "
        "Second concurrent revert cloned the post-accept version, undoing the first revert."
    )
```

---

### 6. Booking Proposal — TOCTOU race on concierge confirm: two concurrent `confirm_booking` calls both pass status check

**Severity:** High

**Location:** `backend/concierge/tool_handlers/booking_flow.py:632-666` and `757/887`; `backend/core/db/booking_proposals.py:78`

**What breaks:** The concierge confirm path calls `get_booking_proposal` (plain `SELECT`, no `FOR UPDATE`), checks status in memory via `_check_loaded_proposal_state`, then writes confirmation. `mark_booking_proposal_confirmed` has no `WHERE status='pending'` guard. Two concurrent confirm invocations — e.g., phone + watch tapping simultaneously — both read `status='pending'` and both reach `mark_booking_proposal_confirmed`. In the L2+ path, each call first creates a distinct `booking_session` row; the second write overwrites `session_id` on the proposal, orphaning the first session permanently. Two push notifications fire. The sibling `change_proposals.py:527` uses `with_for_update()` for exactly this race class — booking proposals do not.

**Exploit:**
1. Pending proposal, two concurrent confirm invocations.
2. Both read `status='pending'`; both pass `_check_loaded_proposal_state`.
3. Both reach `create_booking_session` — two distinct session rows created.
4. Both call `mark_booking_proposal_confirmed` with their respective `session_id`; second write overwrites first.
5. First session is orphaned (`session_id` FK is `ON DELETE SET NULL`, so it persists indefinitely detached). Two push notifications fire.

**Fix:** Add `AND status='pending'` to `mark_booking_proposal_confirmed`'s WHERE clause. Check `rowcount == 0` after the UPDATE and return a sentinel or raise so the caller can surface `already_closed` to the second concurrent caller. This is identical to the fix pattern already applied to `change_proposals.py:527`. The REST confirm endpoint (booking.py:490) has the same exposure and needs the same DB-layer guard.

```python
@pytest.mark.asyncio
async def test_concurrent_confirm_booking_only_one_session_created(
    db_session, make_trip, make_user, make_venue, make_conversation
):
    # ... arrange: pending proposal with L2 capability ...

    created_sessions = []

    async def tracked_create_session(**kwargs):
        result = await original_create_session(**kwargs)
        created_sessions.append(result)
        return result

    with patch(f"{TOOLS_MOD}.create_booking_session", side_effect=tracked_create_session):
        results = await asyncio.gather(
            _execute_confirm_booking(tool_input, ...),
            _execute_confirm_booking(tool_input, ...),
            return_exceptions=True,
        )

    statuses = [json.loads(r).get("status") for r in results if isinstance(r, str)]
    assert statuses.count("handoff") == 1
    assert "already_closed" in statuses
    assert len(created_sessions) == 1, (
        f"Expected 1 booking_session, got {len(created_sessions)} — orphaned session created"
    )
    final = get_booking_proposal(proposal.id)
    assert final.session_id == created_sessions[0].id
```

---

### 7. Change Proposal — Terminal escape: reverting an accepted proposal with `apply_status='failed'` triggers `version_restore` to an unintended prior version

**Severity:** High

**Location:** `backend/api/routes/proposals.py:661-700`; `backend/core/db/proposal_apply.py:1266-1382` (`version_restore` fallback)

**What breaks:** The `/revert` route guards only on `proposal.status != 'accepted'` — it never checks `apply_status`. A proposal with `status='accepted'` and `apply_status='failed'` means the itinerary was never forked and no `proposal_applied` event was written. When `/revert` is called: `_try_diff_safe_revert` finds no event and returns `None`; execution falls through to `version_restore`; `get_itinerary_history` returns `history[-2]` which is the version before the last legitimately applied proposal. A new version is created from that older state, silently erasing prior legitimate changes. The route stamps `was_reverted=True` and transitions the proposal to `withdrawn`.

**Exploit:**
1. P1 accepted+applied: itinerary at V2 (forked from V1).
2. P2 accepted; `apply_accepted_proposal` raises (unknown `proposal_type`) → `apply_status='failed'`. Itinerary still V2.
3. Organizer calls `/revert` on P2.
4. No `proposal_applied` event → `_try_diff_safe_revert` returns `None` → `version_restore` runs.
5. `history = [V1, V2]`; `history[-2] = V1`. New version V3 cloning V1 becomes HEAD.
6. P2 marked `was_reverted=True`, `status='withdrawn'`. Members see "Proposal reverted". P1's applied changes are silently erased.

**Fix:** Add `if proposal.apply_status == "failed": raise HTTPException(status_code=409, detail="Cannot revert a proposal whose apply failed — the itinerary was never changed")` immediately after the existing status guard at `proposals.py:665`. This prevents `version_restore` from treating a no-op acceptance as a reversible change. Two lines; no schema migration required.

```python
def test_revert_rejected_when_apply_status_failed(client, organizer_auth_headers, db_session):
    # Arrange: two versions; P2 status='accepted', apply_status='failed'
    trip = create_trip_with_two_versions(db_session)
    p2 = create_failed_apply_proposal(db_session, trip)

    resp = client.post(
        f"/trips/{trip.id}/proposals/{p2.id}/revert",
        json={"mode": "diff_safe"},
        headers=organizer_auth_headers(trip),
    )

    assert resp.status_code == 409
    history = get_itinerary_history(trip.id)
    assert len(history) == 2  # no new version created
    p2_reloaded = get_change_proposal(p2.id)
    assert p2_reloaded.status == "accepted"
    assert p2_reloaded.was_reverted is False
```

---

### 8. Trip Phase — Concurrent promote on same conversation creates a duplicate orphan trip

**Severity:** High

**Location:** `backend/core/db/promotion.py:260-365`

**What breaks:** The "already promoted" guard at line 260 reads `conv.trip_id` via `get_conversation()` (plain READ COMMITTED outside any transaction). Two concurrent promotions both see `trip_id=NULL` and proceed. The UPDATE at line 329-333 has no `AND trip_id IS NULL` predicate — T2's write overwrites T1's link. T1's trip persists with members but `conversations.trip_id` points to T2. No UNIQUE constraint exists on `conversations.trip_id`. T1 is an orphaned trip, billed against storage, invisible to the user, analytics-polluting.

**Exploit:**
1. Client sends `POST /api/trips/{conversation_id}/promote`; request times out.
2. Client retries — T1 and T2 both see `trip_id=NULL`.
3. T1 commits: `trip_1` created, `conv.trip_id=trip_1`.
4. T2 commits: `trip_2` created, `conv.trip_id=trip_2` (overwrites).
5. `trip_1` exists with members, no primary conversation reference, never displayed, never reaped.

**Fix:** Change the conversations UPDATE at line 329-333 to include `AND trip_id IS NULL` in the WHERE clause: `.where(conversations.c.id == conversation_id, conversations.c.trip_id.is_(None))`. Check `rowcount == 1` and roll back + raise `PromotionError` if it is 0. This makes the guard atomic with the write inside the same transaction, eliminating the TOCTOU window without requiring a new UNIQUE constraint (though adding a partial UNIQUE on `conversations.trip_id WHERE trip_id IS NOT NULL` would add defence-in-depth).

```python
def test_concurrent_promote_does_not_create_orphan_trip(db_session, make_user):
    user = make_user()
    conv = make_conversation_with_intent(created_by=user.id)

    results = []
    errors = []

    def do_promote():
        try:
            r = promote_conversation_to_trip(conv.id)
            results.append(r.trip.id)
        except PromotionError as e:
            errors.append(str(e))

    t1 = threading.Thread(target=do_promote)
    t2 = threading.Thread(target=do_promote)
    t1.start(); t2.start(); t1.join(); t2.join()

    all_trip_ids = set(results)
    assert len(all_trip_ids) == 1, (
        f"Expected 1 unique trip, got {len(all_trip_ids)} — TOCTOU race in promote_conversation_to_trip"
    )
```

---

### 9. Trip Phase — `decommit_trip` called on archived trip after conversation re-promoted clobbers the new trip's primary conversation link

**Severity:** High

**Location:** `backend/core/db/promotion.py:460-502`

**What breaks:** `decommit_trip` has no guard preventing re-execution on an `archived` trip. It reads `T1.primary_conversation_id` (still pointing to conv A after re-promotion), then executes `UPDATE conversations SET trip_id=NULL WHERE id=conv_A` with no `AND conversations.trip_id = trip_id` predicate. After re-promotion, `conv_A.trip_id = T2`, but the UPDATE fires anyway and nulls it. `update_intent_state(conv_A, {'phase': 'drafting'})` then overwrites the `'committed'` phase. T2 loses its primary conversation reference; the concierge cannot resume the thread.

**Exploit:**
1. `conv_A → T1` (promote). `T1 decommitted` (conv_A.trip_id=NULL, phase='drafting').
2. `conv_A → T2` (re-promote): conv_A.trip_id=T2, phase='committed', T2.primary_conversation_id=conv_A.
3. Stale client or agent retries decommit on T1.
4. `UPDATE conversations SET trip_id=NULL WHERE id=conv_A` fires (no trip_id guard).
5. T2 has no conversation link. `phase='drafting'` overwrites `'committed'`.

**Fix:** Two changes are required in `decommit_trip`: (1) Add `if row["status"] == "archived": return early` — a stale decommit on an already-archived trip is a no-op and should not touch any other rows. (2) Change line 485 to a conditional update: `.where(conversations.c.id == conv_id, conversations.c.trip_id == trip_id)` — prevents clobbering if the conversation has been relinked. Both changes are needed; the status check prevents the `update_intent_state` clobber, the conditional WHERE is a defence-in-depth guard.

```python
def test_decommit_archived_trip_does_not_clobber_repromoted_conversation(
    make_user, make_conversation_with_intent
):
    user = make_user()
    conv_a = make_conversation_with_intent(created_by=user.id)

    result1 = promote_conversation_to_trip(conv_a.id)
    t1_id = result1.trip.id
    decommit_trip(t1_id)
    result2 = promote_conversation_to_trip(conv_a.id)
    t2_id = result2.trip.id
    assert t2_id != t1_id

    # Stale retry
    decommit_trip(t1_id)

    with get_connection() as conn:
        row = conn.execute(select(conversations).where(conversations.c.id == conv_a.id)).mappings().one()
    assert row["trip_id"] == t2_id, f"conv_A.trip_id was clobbered to {row['trip_id']!r}"

    intent = get_intent_state(conv_a.id)
    assert intent.get("phase") == "committed", f"phase was overwritten to {intent.get('phase')!r}"
```

---

### 10. Plan Commitment — `restaurant_writeback` escapes `cancelled`: stamps `status='confirmed'` unconditionally

**Severity:** Critical

**Location:** `backend/booking_agent/db/restaurant_writeback.py:110-115`

**What breaks:** `_stamp_block` calls `update_block(block_id, status='confirmed', booking_ref=...)` with no guard on the block's current status. `update_block`'s only status guard (trips.py:1837) fires when the NEW status is `'cancelled'` — it is inert when the caller writes `'confirmed'`. A block the user explicitly removed (`status='cancelled'`) is silently resurrected to `status='confirmed'`, `commitment_state='booked'` when a delayed provider webhook arrives. `_load_context` in `restaurant_writeback.py:47` reads from `restaurant_booking_attempts` and `booking_offers` — it never reads the block's current status.

**Exploit:**
1. User adds restaurant block (status='tentative'). Concierge initiates booking attempt.
2. User cancels the block → `status='cancelled'`.
3. Provider webhook fires confirming the attempt.
4. `maybe_record_restaurant_confirmation` → `_stamp_block` → `update_block(block_id, status='confirmed', ...)`.
5. `update_block` computes `intrinsic_commitment_state('confirmed', ...)` = `'booked'` from the incoming value, never reading the stored `'cancelled'`.
6. Block flipped to `status='confirmed'`, `commitment_state='booked'`. User sees a resurrected confirmed booking on a removed block.

**Fix:** In `_stamp_block` (restaurant_writeback.py), read the block's current status before calling `update_block`. If the block is `'cancelled'` or does not exist, log a warning and return without writing. A two-line guard: `current_status = get_block_status(ctx['block_id'])` followed by `if current_status in ('cancelled', None): return`. As defence-in-depth, `update_block` should also check `old_row.get('status') == 'cancelled'` and refuse to overwrite a cancelled block with any live status.

```python
def test_stamp_block_skips_cancelled_block():
    from unittest.mock import patch
    from backend.booking_agent.db.restaurant_writeback import _stamp_block

    ctx = {
        "block_id": uuid4(), "attempt_id": uuid4(), "offer_id": uuid4(),
        "venue_id": 7, "channel": "voice", "session_id": uuid4(),
        "provider": "voice_booking", "trip_id": uuid4(), "initiated_by": uuid4(),
        "venue_name": "Le Comptoir",
        "requested_datetime": datetime(2026, 8, 1, 19, 30, tzinfo=UTC), "party_size": 2,
    }
    details = {"confirmation_number": "XYZ999", "confirmed_datetime": "2026-08-01T19:30:00+00:00",
               "venue_brief_shared_text": None}

    with (
        patch("backend.booking_agent.db.restaurant_writeback.get_block_booking_ref", return_value=None),
        patch("backend.booking_agent.db.restaurant_writeback.update_block") as mock_update,
        patch("backend.core.db.trips.get_block_status", return_value="cancelled"),
    ):
        _stamp_block(ctx, details)

    mock_update.assert_not_called()
```

---

### 11. Stay Candidates — Saga compensation (`release_candidate`) does not delete the orphaned `trip_accommodations` row

**Severity:** High

**Location:** `backend/api/routes/stay_candidates.py:265-281` (saga `finally` block); `backend/core/db/trip_stay_candidates.py:131-156` (`release_candidate`)

**What breaks:** The choose saga performs three independent autocommitting writes: `claim_candidate` → `create_accommodation` (commits, retires prior primary P) → `link_chosen_accommodation`. The `finally` block calls `release_candidate` if `linked=False`. `release_candidate` only resets `candidate.status` back to `active` — it does not delete or un-retire the `trip_accommodations` row committed at step 2. If a concurrent withdraw races between steps 2 and 3 (see finding 4), `release_candidate` is also a no-op (status is already `withdrawn`). Result: prior primary P permanently retired, new accommodation Q active-primary with no candidate link, no error surfaced.

**Exploit:** See finding 4's exploit — same race window, same compensation failure outcome.

**Fix:** `release_candidate` must be extended to also (a) delete or retire the orphaned `trip_accommodations` row it indirectly created, and (b) un-retire the prior primary if one was retired during `create_accommodation`. These steps are recorded in the `trip_accommodations` audit data at creation time. As a simpler approach, the saga should be restructured so `create_accommodation` is only called after `link_chosen_accommodation` succeeds, or the entire saga should run inside a single distributed advisory lock (`pg_advisory_lock(trip_id)`) covering all three writes. The concurrent-withdraw finding (4) must also be fixed independently — the compensation fix here is a backstop, not a substitute.

```python
@pytest.mark.asyncio
async def test_choose_saga_concurrent_withdraw_leaves_no_orphan(
    db_session, trip_with_primary_stay, active_candidate
):
    trip_id = trip_with_primary_stay.trip_id
    prior_primary_id = trip_with_primary_stay.accommodation_id

    original_link = link_chosen_accommodation
    def link_with_race(t_id, c_id, acc_id):
        withdraw_candidate(t_id, c_id)  # concurrent withdraw injected here
        return original_link(t_id, c_id, acc_id)

    with patch("backend.api.routes.stay_candidates.link_chosen_accommodation", side_effect=link_with_race):
        with pytest.raises(Exception):
            await choose_stay_candidate_endpoint(trip_id, active_candidate.id, actor=...)

    from backend.core.db.trip_accommodations import get_active_primary_accommodation, get_accommodation
    orphan = get_active_primary_accommodation(trip_id)

    if orphan is None:
        # clean rollback: prior primary must still be active
        prior = get_accommodation(prior_primary_id, include_retired=True)
        assert prior.retired_at is None, "Prior primary was retired but no replacement linked"
    else:
        # if a primary exists, it must have a valid candidate link
        from backend.core.db.trip_stay_candidates import get_candidate
        cand = get_candidate(trip_id, active_candidate.id)
        assert cand is not None and cand.chosen_accommodation_id == orphan.id
```

---

### 12. Plan Commitment — `PATCH /blocks/{id}` accepts writes to cancelled blocks including `status='tentative'` un-cancel

**Severity:** High

**Location:** `backend/api/routes/trips.py:1418`

**What breaks:** `update_itinerary_block` calls `get_block_for_trip(trip_id, block_id)` without `require_active=True`. Cancelled blocks are returned. `update_block`'s guard (line 1837) only checks if the NEW incoming status is `'cancelled'` — it has no guard against writing to an already-cancelled block. Any trip member can `PATCH {status: 'tentative'}` a cancelled block and receive HTTP 200, re-activating the block and bypassing the `plan_events` ledger undo path. The undo route at line 1556 correctly passes `require_active=True`; the PATCH route does not.

**Exploit:**
1. Trip member A removes a block → `status='cancelled'`.
2. Trip member B has a stale plan view; sends `PATCH /blocks/{block_id}` with `{"status": "tentative"}`.
3. `get_block_for_trip` (without `require_active=True`) returns the cancelled block.
4. `update_block` writes `status='tentative'` — guard does not fire (incoming status is not `'cancelled'`).
5. Block is re-activated. Cancellation is silently undone; no undo ledger entry created.

**Fix:** Change line 1418 from `get_block_for_trip(trip_id, block_id)` to `get_block_for_trip(trip_id, block_id, require_active=True)`. This causes the existing 404 guard at line 1419 to fire for cancelled blocks. Apply the same fix to the `move_block` route at line 1961, which has the identical omission.

```python
def test_patch_cannot_reactivate_cancelled_block(client: TestClient, auth_headers: dict):
    trip_id, block_id = make_trip_with_block()

    cancel_resp = client.patch(
        f"/api/trips/{trip_id}/itinerary/blocks/{block_id}",
        json={"status": "cancelled"}, headers=auth_headers,
    )
    assert cancel_resp.status_code == 200

    reactivate_resp = client.patch(
        f"/api/trips/{trip_id}/itinerary/blocks/{block_id}",
        json={"status": "tentative"}, headers=auth_headers,
    )
    assert reactivate_resp.status_code in (404, 409), (
        f"Expected 404/409 but got {reactivate_resp.status_code}"
    )
```

---

### 13. Trip Phase — Dead write state `planning`: proposal-overview and pre-trip-drip proactive features permanently silenced

**Severity:** High

**Location:** `backend/concierge/proactive.py:491` (proposal-overview gate); `backend/concierge/proactive.py:1051` (pre-trip drip gate)

**What breaks:** Two proactive notification producers gate exclusively on `trip_status == 'planning'`. No application code path ever writes `trips.status = 'planning'`. Every trip is born `'ideation'` (DB default) and transitions only to `'completed'` (lifecycle task) or `'archived'` (decommit). `PatchTripRequest` explicitly excludes `status`; the concierge agent's `_PATCH_TRIP_ALLOWED_FIELDS` omits it. Both features — the proposal-overview nudge ("3 open votes to resolve before your trip") and the destination-spotlight drip — are permanently unreachable dead code. The value `'planning'` appears only in read-side guards, display logic, and eval/seed fixtures, confirming it was never wired to a write path.

**Fix:** Implement the `ideation → planning` status transition. The natural trigger is when a trip has a confirmed itinerary (at least one day of `'confirmed'` blocks) or a booking proposal accepted. Add `update_trip(trip_id, status="planning")` in the appropriate post-commit hook and lift the CHECK constraint (which currently has no restriction on `status` values) if schema enforcement is desired. Both proactive features become live immediately. Alternatively, rewrite the gate to use `derive_trip_phase(trip)` (which correctly computes the phase from date arithmetic and booking data) instead of the raw DB status column — this avoids the missing write entirely.

```python
@pytest.mark.asyncio
async def test_trip_can_reach_planning_status(make_trip):
    today = date.today()
    trip = make_trip(
        status="ideation", place_id=1,
        start_date=today + timedelta(days=30),
        end_date=today + timedelta(days=37),
    )
    updated = update_trip(trip.id, status="planning")
    assert updated.status == "planning"

@pytest.mark.asyncio
async def test_proposal_overview_fires_for_planning_trip(make_world_model):
    from backend.concierge.proactive import produce_proposal_overview_notification
    world = make_world_model(
        trip_id=uuid4(), trip_status="planning",
        trip_start_date=date.today() + timedelta(days=14), open_proposals=3,
    )
    result = await produce_proposal_overview_notification(trip_id=world.core.trip_id, world=world)
    assert result is not None, "Gate at proactive.py:491 never fires in prod"
```

---

### 14. Trip Phase — Dead write states `active` and `in_progress`: local-events and leave-by push notification features permanently dead

**Severity:** High

**Location:** `backend/concierge/proactive.py:311`; `backend/notifications/leave_by.py:660`

**What breaks:** `proactive.py:311` gates the local-events-during-trip producer on `trip_status in ('active', 'in_progress')`. `leave_by.py:660` queries `WHERE trips.status == 'live'`. None of `'active'`, `'in_progress'`, or `'live'` is ever written to `trips.status` by any production code. `derive_trip_phase` correctly derives `TripPhase.LIVE` from date arithmetic, but this is a computed attribute — it is never written back to the DB column. `_load_active_trips()` is guaranteed to return `[]` in production; a user on an active trip (dates straddling today) will never receive a leave-by push ("time to leave for your 2pm reservation"). The local-events producer returns `None` for every evaluation.

**Fix:** Change the gates to use the derived phase rather than the raw DB column. In `proactive.py:311`, replace `if trip_status not in ('active', 'in_progress')` with `if world.core.phase not in (TripPhase.LIVE,)`. In `leave_by.py:660`, replace the `WHERE status == 'live'` filter with a date-range filter (`start_date <= today AND end_date >= today`) — consistent with how `derive_trip_phase` computes liveness. This eliminates the dependency on a write that was never implemented.

```python
@pytest.mark.asyncio
async def test_load_active_trips_returns_live_date_trip(db_session, make_trip):
    from backend.notifications.leave_by import _load_active_trips

    today = date.today()
    trip = create_trip(
        created_by=uuid4(),
        start_date=today - timedelta(days=1), end_date=today + timedelta(days=2), place_id=1,
    )
    # trip.status is 'ideation' — never transitioned to 'live'
    rows = _load_active_trips()
    assert trip.id in [r.id for r in rows], (
        f"Trip spanning today not returned; status={trip.status!r}. "
        "Gate must use date range, not raw status='live'."
    )
```

---

### 15. Stay Candidates — `cast_vote` has no DB-level status guard: vote succeeds after concurrent withdraw (TOCTOU)

**Severity:** High

**Location:** `backend/api/routes/stay_candidates.py:146-149`; `backend/core/db/trip_stay_candidates.py:244-258` (`cast_vote`)

**What breaks:** `vote_for_candidate` reads candidate status via a plain `SELECT` (no `FOR UPDATE`), checks `status != 'active'` in memory, then calls `cast_vote` — a separate `get_tx()`. `cast_vote` is a bare `pg_insert ... on_conflict_do_update` with no JOIN or filter on `trip_stay_candidates.status`. The FK only enforces row existence, not `status='active'`. Between the two async yields, another coroutine can withdraw the candidate. `cast_vote` INSERT succeeds; the route returns HTTP 200 with `my_candidate_id` set. But `resolve_stay_vote` silently drops the vote (`active_ids` filter excludes withdrawn candidates). The user receives a vote-confirmed response that has zero effect on the outcome.

**Fix:** Make `cast_vote` atomic: replace the bare `pg_insert` with an `INSERT INTO trip_stay_candidate_votes ... WHERE EXISTS (SELECT 1 FROM trip_stay_candidates WHERE id=:cid AND status='active')`. Treat `rowcount == 0` as a 409 condition at the route layer. This closes the TOCTOU window at the DB level regardless of concurrency.

```python
def test_vote_after_concurrent_withdraw_returns_409() -> None:
    actor = _user()
    trip = uuid4()
    cand = _candidate(trip)  # active at read time

    def _cast_vote_ignores_status(trip_id, candidate_id, user_id):
        # Simulates current behavior: INSERT succeeds even after concurrent withdraw
        return StayCandidateVote(id=uuid4(), trip_id=trip_id, candidate_id=candidate_id,
                                 user_id=user_id, created_at=datetime.now(UTC))

    withdrawn = cand.model_copy(update={"status": "withdrawn"})

    with (
        patch(f"{MODULE}.require_trip_member_async", new=AsyncMock(return_value=None)),
        patch(f"{MODULE}.get_candidate", return_value=cand),
        patch(f"{MODULE}.cast_vote", side_effect=_cast_vote_ignores_status),
        patch(f"{MODULE}.list_candidates", return_value=[withdrawn]),
        patch(f"{MODULE}.list_votes", return_value=[]),
        patch(f"{MODULE}.get_trip_members", return_value=_members(actor.id)),
    ):
        resp = TestClient(_app(actor)).post(f"/api/trips/{trip}/stay-candidates/{cand.id}/vote")

    # Today: 200 with vote silently dropped. After fix: 409.
    assert resp.status_code == 409
```

---

### 16. Booking Proposal — `mark_booking_proposal_confirmed` docstring claims idempotency but overwrites `confirmed_at` on every call

**Severity:** High

**Location:** `backend/core/db/booking_proposals.py:83-99`

**What breaks:** The docstring states "Idempotent — returns the current row if it's already confirmed." The implementation issues `UPDATE ... SET status='confirmed', confirmed_at=:now WHERE id=:id` — unconditional on every call. A client retry on `POST /proposals/{id}/confirm` replaces the original confirmation timestamp with the retry timestamp, corrupting audit logs, receipts, and time-to-confirm analytics. The REST path also passes no `session_id` kwarg (defaults to None), so the implementation does not write `NULL` over `session_id` on retries (the `if session_id is not None` guard at line 97 prevents that), but `confirmed_at` is still unconditionally overwritten.

**Fix:** Add `WHERE status='pending'` to the UPDATE predicate (making the write a no-op on already-confirmed rows), and change the function to read and return the current row on a zero-rowcount result. This matches the stated idempotency contract: first call writes, subsequent calls return the existing row unchanged. The `confirmed_at` on the first call is preserved for all retries.

```python
@pytest.mark.asyncio
async def test_confirm_proposal_endpoint_is_idempotent_on_already_confirmed(
    async_client, db_session, authenticated_user
):
    original_confirmed_at = datetime(2024, 1, 1, 12, 0, 0, tzinfo=UTC)
    proposal = insert_confirmed_proposal(
        db_session, proposal_id=uuid4(), trip_id=uuid4(),
        user_id=authenticated_user.id, confirmed_at=original_confirmed_at,
    )

    with freeze_time(original_confirmed_at + timedelta(seconds=30)):
        resp = await async_client.post(
            f"/trips/{proposal.trip_id}/booking/proposals/{proposal.id}/confirm",
            headers=auth_headers(authenticated_user),
        )

    assert resp.status_code == 200
    db_session.refresh(proposal)
    assert proposal.confirmed_at == original_confirmed_at, (
        f"confirmed_at was overwritten: got {proposal.confirmed_at}, expected {original_confirmed_at}"
    )
```

---

### 17. Change Proposal — Idempotency gap: `/revert` returns 409 on successful retry instead of 200

**Severity:** Medium

**Location:** `backend/api/routes/proposals.py:640-842`

**What breaks:** The `/withdraw` route has an explicit idempotent short-circuit: if `existing.status == 'withdrawn': return _to_detail`. The `/revert` route has no equivalent. A mobile client that times out on a successful revert and retries gets HTTP 409 "Cannot revert a proposal with status 'withdrawn'" — indistinguishable from a genuine failure. No data corruption results (the diff-safe conflict detection correctly prevents double mutation), but the client cannot determine whether the undo succeeded.

**Fix:** Add `if proposal.status == "withdrawn" and proposal.was_reverted: return _to_detail(existing, ...)` at the top of the revert route's proposal-state check, analogous to the `/withdraw` pattern at `proposals.py:623-625`.

```python
async def test_revert_retry_returns_200_not_409(client, organizer_auth_headers, accepted_proposal_fixture):
    r1 = client.post(f"/trips/{trip_id}/proposals/{proposal_id}/revert",
                     json={"mode": "diff_safe"}, headers=organizer_auth_headers)
    assert r1.status_code == 200
    assert r1.json()["status"] == "withdrawn"

    r2 = client.post(f"/trips/{trip_id}/proposals/{proposal_id}/revert",
                     json={"mode": "diff_safe"}, headers=organizer_auth_headers)
    assert r2.status_code == 200, f"Expected 200 on retry, got {r2.status_code}: {r2.text}"
    assert r2.json()["status"] == "withdrawn"
```

---

### 18. Booking Proposal — Dead state `superseded` in CHECK constraint but never assigned and has no reaper

**Severity:** Medium

**Location:** `backend/core/db/_tables/booking.py:235-238`; `alembic/versions/_archive/b00kpr0p001_booking_proposals.py:98-101`

**What breaks:** `'superseded'` is in the `ck_booking_proposals_status` CHECK constraint. No application code ever writes `status='superseded'` to a `booking_proposals` row — the four write functions hard-code only `confirmed`, `rejected`, or `expired`. `expire_stale_proposals` (line 187) only touches `pending` rows. `get_recent_booking_proposal_for_trip` and `list_held_booking_proposals_for_trips` would skip a `superseded` row. The value was copied from the `change_proposals` schema where it is actively used, without building a corresponding write path.

**Fix:** Either (A) remove `'superseded'` from the `ck_booking_proposals_status` constraint in a new Alembic migration (clean option, documents intent), or (B) implement a `mark_booking_proposal_superseded` function and call it when a new booking proposal replaces an in-flight pending one. Option A is the safe near-term change.

```python
def test_superseded_is_not_reachable_via_application_code():
    import ast, inspect
    import backend.core.db.booking_proposals as mod

    source = inspect.getsource(mod)
    tree = ast.parse(source)
    assigned = {
        node.value.value
        for node in ast.walk(tree)
        if isinstance(node, ast.keyword) and node.arg == "status"
        and isinstance(node.value, ast.Constant)
    }
    # Fails today: 'superseded' is in the constraint but never in assigned
    allowed = {"pending", "confirmed", "rejected", "expired", "superseded"}
    assert "superseded" not in (allowed - assigned), (
        "'superseded' is in the CHECK constraint but never assigned — remove it or add a write path"
    )
```

---

### 19. Trip Phase — FE `TripStatus` includes `live` and `booked` which backend never writes; history LIVE classification permanently empty

**Severity:** Medium

**Location:** `travel-app/utils/api/types.ts:82-89`; `travel-app/utils/helpers.ts:91-93`; `travel-app/app/(tabs)/concierge/history.tsx:152`

**What breaks:** `history.tsx:152` classifies a trip as LIVE when `status === 'live' || status === 'active' || status === 'in_progress'`. All three values are never written to `trips.status` by production code. Every user mid-trip has `status='ideation'`. The LIVE section of the conversation history ledger is permanently empty for all users. `computeTripPhase`'s `status === 'live'` branch at `helpers.ts:91` is also dead for the same reason.

**Fix:** In `history.tsx:152`, replace the raw-status check with `computeTripPhase(t.trip) === 'active'`. This uses the date-math derivation that correctly identifies active trips without requiring a DB write.

```typescript
// before (dead — backend never writes these values)
const status = String(t.trip.status ?? '').toLowerCase();
const live = status === 'live' || status === 'active' || status === 'in_progress';

// after (uses derived phase from date arithmetic)
import { computeTripPhase } from '../../../utils/helpers';
const live = computeTripPhase(t.trip) === 'active';
```

---

### 20. Stay Candidates — No vote-phase guard on cast_vote or choose: votes can reverse a `decided` outcome; organizer can book a losing candidate

**Severity:** Medium (two related gaps reported as one)

**Location:** `backend/api/routes/stay_candidates.py:138-150` (vote); `backend/api/routes/stay_candidates.py:200-286` (choose)

**What breaks:** `vote_for_candidate` checks only `candidate.status == 'active'`; it has no phase check. Because `resolve_stay_vote` is stateless and recomputed on every GET, any new vote immediately mutates the phase. After the organizer observes `phase='decided'` and prepares to `/choose`, a voter can retract or move their vote, reverting the phase to `open` or `tie`. The organizer's `/choose` succeeds anyway (`claim_candidate` only checks `status='active'`). Separately, `/choose` has no check that the candidate being booked is the vote leader — an organizer can book a zero-vote candidate at any time via direct API call, with the FE's `decided && isLeader` guard bypassed entirely.

**Fix:** In `choose_stay_candidate` (stay_candidates.py ~line 224), add a phase re-read immediately before the saga begins:

```python
decision = await _decision(trip_id, actor.id)
if decision.vote.phase != "decided" or decision.vote.leader_id != candidate_id:
    raise HTTPException(
        status_code=409,
        detail="The group vote is no longer decided in favour of this option.",
    )
```

This closes both gaps: non-leader booking and phase-regression between observe and choose. The vote-retraction TOCTOU is not separately closeable without freezing votes once `decided` — that is a product decision, but the choose guard is the minimum viable server enforcement.

```python
def test_choose_rejects_when_vote_not_decided() -> None:
    # 1-1 tie — no decided leader
    votes = [_vote(u1, cand.id), _vote(u2, other.id)]
    with (
        patch(f"{MODULE}.list_candidates", return_value=[cand, other]),
        patch(f"{MODULE}.list_votes", return_value=votes),
        patch(f"{MODULE}.get_trip_members", return_value=_members(u1, u2)),
        patch(f"{MODULE}.claim_candidate") as claim,
        # ... other patches ...
    ):
        resp = TestClient(_app(actor)).post(f"/api/trips/{trip}/stay-candidates/{cand.id}/choose")

    assert resp.status_code == 409
    claim.assert_not_called()
```

---

### 21. Plan Commitment — FE branches on `booking_ref.state` `held_for_payment` and `held` but BE never writes these to blocks

**Severity:** Medium

**Location:** `travel-app/components/trip-plan/PlanBlockRow.tsx:1048-1057`; `backend/booking_agent/holds.py:53-79`

**What breaks:** `PlanBlockRow.tsx` renders an oxblood halo for `bookingState === 'held_for_payment'` and a planning-ink dot for `bookingState === 'held'`. `place_hold()` updates `booking_offers.status` to `'held_for_payment'` but never stamps `booking_ref.state` on the associated `itinerary_blocks` row. `settle_hold` stamps `'confirmed'`, `release_hold` stamps `'released'`, `book_handoff` stamps `'handed_off'` — no path stamps `'held_for_payment'`. The plan-state read endpoint derives `booking_raw` from `block.booking_state` (the DB column), which never receives the held value. A user with a live Duffel hold on a block sees no visual indication of the hold or its deadline.

**Fix:** Add a block-stamp step inside `place_hold()` (holds.py), mirroring the existing pattern in `settle_hold()` (lines 134-156) and `release_hold()` (lines 193-208): after `record_offer_hold` succeeds, call `update_block(block_id, booking_ref={"state": "held_for_payment", "payment_required_by": hold_result["payment_required_by"], ...})`. This makes the `held_for_payment` FE branch reachable and surfaces the hold deadline in the plan view.

```python
def test_place_hold_stamps_held_for_payment_on_block():
    ctx_block_id = uuid4()
    update_block_calls = []

    async def fake_update_block(bid, **kwargs):
        update_block_calls.append((bid, kwargs))

    with (
        patch(f"{HOLDS}.get_offer", AsyncMock(return_value=_offer(block_id=ctx_block_id))),
        patch(f"{HOLDS}.create_providers", return_value={"duffel": _mock_provider()}),
        patch(f"{HOLDS}.record_offer_hold", AsyncMock(return_value=_held_offer(block_id=ctx_block_id))),
        patch("backend.core.db.trips.update_block", side_effect=fake_update_block),
    ):
        from backend.booking_agent.holds import place_hold
        await place_hold(offer_id, [{"id": "pas_1"}])

    assert update_block_calls, "place_hold() must call update_block() to stamp held_for_payment"
    _bid, call_kwargs = update_block_calls[0]
    assert _bid == ctx_block_id
    assert call_kwargs.get("booking_ref", {}).get("state") == "held_for_payment"
```

---

### 22. Plan Commitment — `mark-happened` endpoint allows `event_state='happened'` on a cancelled block

**Severity:** Medium

**Location:** `backend/api/routes/plan_mark_happened.py:45`

**What breaks:** `POST .../mark-happened` calls `get_block_for_trip` without `require_active=True`. Cancelled blocks are returned. `update_block` writes `event_state='happened'` unconditionally. `_load_confirmed_moments` in `trip_story.py:367-370` queries `WHERE event_state='happened'` with no `WHERE status != 'cancelled'` filter. A cancelled block marked as happened pollutes the trip story memory surface with explicitly removed stops.

**Fix:** Pass `require_active=True` to `get_block_for_trip` at `plan_mark_happened.py:45`, or add `if block.status == 'cancelled': raise HTTPException(409, ...)` after line 46. Additionally add `.where(itinerary_blocks.c.status != "cancelled")` to `_load_confirmed_moments` in `trip_story.py` as a belt-and-suspenders filter.

```python
def test_mark_happened_rejects_cancelled_block():
    actor = _make_user()
    block = _make_block(status="cancelled", event_state="planned")

    with (
        patch(_PATCH_MEMBER, return_value=True),
        patch(_PATCH_GET_BLOCK, return_value=block),
        patch(_PATCH_UPDATE_BLOCK) as mock_update,
        patch(_PATCH_INVALIDATE),
    ):
        resp = TestClient(_app(actor)).post(
            f"/api/trips/{uuid4()}/plan/blocks/{block.id}/mark-happened"
        )

    assert resp.status_code in (409, 422)
    mock_update.assert_not_called()
```

---

## Uncertain — Needs Manual Trace

| Machine | Title | Location | Why ambiguous |
|---|---|---|---|
| — | — | — | — |

No defects were left uncertain in this batch. Every candidate either confirmed or was refuted during the adversarial verification pass. The refuted count was 6 (not listed here per audit scope).

---

## Machines Clean In This Batch

No machine in this batch is verified clean. All five machines — Change proposal lifecycle, Booking proposal + booking agent, Trip phase + conversation→trip promotion, Stay candidates & votes, and Plan commitment + block state — produced at least one confirmed defect. This section intentionally empty.

---

## Recommended Fix Order (This Batch)

Ordered by blast radius × ease (highest priority first):

1. **Booking proposals: add `WHERE status='pending'` to `mark_booking_proposal_confirmed` and `mark_booking_proposal_rejected` + route guards** — two critical terminal-escape defects with zero guards at any layer; any trip member can corrupt terminal state; two-line fix per function, no migration.

2. **Stay candidates: add status guard to DELETE `/stay-candidates/{id}` for `chosen` candidates** — critical; corrupts the stay-booking saga and permanently orphans trip accommodations; one `if candidate.status in ("chosen", "withdrawn")` guard blocks it.

3. **Restaurant writeback: read block status before `_stamp_block`** — critical; delayed webhooks silently resurrect cancelled blocks; two-line guard in `restaurant_writeback.py`.

4. **Change proposals: fix `expire_open_proposals_for_trip` CHECK constraint mismatch** — high; root cause of the orphan-state defect and FE dead-branch defect; use `status='withdrawn'` (already in constraint) or add a migration for `'expired'`; remove the bare `except Exception` at `_plan.py:895`.

5. **Proposal revert: add `SELECT FOR UPDATE` covering the version-restore path** — critical but harder; concurrent version-restore silently undoes the revert; fix pattern already present in `vote_on_proposal`.

6. **Revert guard: reject `apply_status='failed'` proposals** — high; two-line addition at `proposals.py:665`; prevents unintended `version_restore` erasing prior legitimate changes.

7. **`PATCH /blocks/{id}`: pass `require_active=True` to `get_block_for_trip`** — high; one-character change per call site (also `move_block` at line 1961); blocks un-cancel via stale-client PATCH.

8. **Concurrent trip promotion: add `AND trip_id IS NULL` to conversations UPDATE** — high; prevents orphaned trips on client retry; atomic two-predicate WHERE change inside the existing transaction.

9. **`decommit_trip`: add status guard + conditional WHERE on conversations UPDATE** — high; prevents stale decommit from clobbering re-promoted trip's conversation link; two independent two-line changes.

10. **Trip status write path for `planning` / `active`/`live`**: — high; four proactive features permanently dead; cleanest fix is to change the gates in `proactive.py` and `leave_by.py` to use `derive_trip_phase` / date-range instead of raw DB column; implementing the write transition is a larger product decision.

11. **Stay candidates: add phase re-check in `choose_stay_candidate` before saga** — medium; prevents organizer from booking a losing candidate and from committing against a regressed vote; one block of four lines before `claim_candidate`.

12. **Booking proposal TOCTOU: add `WHERE status='pending'` to concierge confirm path** — high; concurrent L2+ confirms orphan a booking session; fix pattern already present in `change_proposals.py:527`.

13. **Saga compensation: extend `release_candidate` to delete orphaned `trip_accommodations` row** — high but structurally complex; requires understanding which accommodation rows were created by the saga; blocked on fixing finding 4 first.

14. **FE dead branches** (`history.tsx` live-classification, `PlanBlockRow` held states, `VoteWidgetCard` expired status) — medium; `history.tsx` fix is one line (`computeTripPhase(t.trip) === 'active'`); `PlanBlockRow` fix requires implementing the `place_hold` block-stamp (finding 21); `VoteWidgetCard` fix is contingent on fixing the CHECK constraint (finding 1).

15. **Remaining medium defects** (revert idempotency short-circuit, `superseded` dead state in booking CHECK constraint, `mark-happened` on cancelled blocks, `cast_vote` TOCTOU) — addressable independently in any order; no inter-dependencies.
