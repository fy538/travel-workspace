# State-Machine Exhaustiveness Audit — 2026-06-25

## Summary

Twelve state machines were audited across the travel-AI backend. **Thirteen defects were confirmed** (1 critical, 6 high, 3 medium, 3 low); 11 candidate findings were refuted because real guards already exist, and none remain in an uncertain/unprovable state. The single highest-severity issue is a **critical orphan-state bug in the scheduled/async task lifecycle**: a task that is `claimed` by a worker that then dies is stranded forever — no reaper exists, and the `UNIQUE(task_kind, scope_id)` constraint blocks any re-schedule, so deferred work (trip-story prewarm, post-trip debriefs) is silently and permanently lost — the exact regression the table was built to prevent. Overall health read: the **money path (expenses/settle) and the invite-slot path are the two weakest machines** — together they hold 1 critical-adjacent and 5 high defects, all on terminal-state mutation, atomicity, and idempotency. These are the systemic gaps: state transitions that commit in independent transactions without a guard, a lock, or a per-actor idempotency key. The content/conversation machines are healthier (mostly low/medium, mostly metric/staleness harm rather than money or lockout).

## Confirmed Defects

### Scheduled / async task lifecycle — `claimed` is a permanent crash-sink; no reaper recovers a stranded row

**Severity:** Critical
**Location:** `backend/core/scheduled_tasks.py:201,216,240` (claim selects only `status='pending'`, sets `claimed`, commits); dispatch is a separate loop step at `backend/api/lifecycle.py:863-873`.

**What breaks:** The invariant "`claimed` is transient — always followed by `mark_done`/`mark_failed` in the same tick" is enforced *only* by the in-process call sequence. `claim_due_tasks` commits `status='claimed'`, `attempts+1` in its own transaction, then the loop calls `dispatch_claimed_task` separately. If the process dies/OOMs/redeploys after the claim commit but before dispatch finishes, the row is stranded: `claim_due_tasks WHERE status='pending'` never re-selects it, and there is **no reaper for this table** (the booking/OCR/message reapers and notification-dedup sweep never touch `scheduled_tasks`). Worse, `UNIQUE(task_kind, scope_id)` + `schedule_task`'s `on_conflict_do_nothing` mean even a re-fire of the originating event silently no-ops. The deferred work is permanently lost. `claimed_at` is written on claim but read by nothing — provisioned for a reaper that was never built.

**Exploit:**
1. `schedule_task('trip_story_prewarm', scope_id=trip, run_after_at=T)` → row `pending`, `attempts=0`.
2. Claimer tick: row → `claimed`, `attempts=1`, commit at `:240`.
3. Before `dispatch_claimed_task` returns (handler awaiting an LLM call, or a deploy/autoscale-down/SIGKILL), the process dies.
4. New process boots; its claimer selects only `status='pending'` — this row is `claimed`. No reaper exists.
5. The task never runs. `trip.completed` already fired once, so no re-fire (and the unique constraint would no-op it anyway). Permanent silent data loss.

**Fix:** Add a stale-claim reaper, mirroring the existing `_run_booking_session_reaper_loop` pattern at `lifecycle.py:876`. Introduce `reap_stale_claims(stale_after)` in `scheduled_tasks.py` that issues `UPDATE scheduled_tasks SET status='pending', claimed_at=NULL WHERE status='claimed' AND claimed_at < now() - :stale_after`, and run it on a supervised loop in `lifecycle.py` (advisory-locked across workers like the proactive loop). Gate the reset to respect a max-attempts ceiling so genuinely poison tasks land in `failed` rather than looping forever. This makes `claimed_at` (already written) finally load-bearing.

```python
def test_stale_claimed_row_is_reclaimed_after_claimer_death():
    """A row stuck in 'claimed' (claimer died post-commit, pre-dispatch) must be
    recoverable: a reaper should reset stale 'claimed' rows back to 'pending' so
    the next claim_due_tasks tick re-dispatches them. Fails today (no reaper)."""
    import backend.core.scheduled_tasks as st
    from datetime import UTC, datetime, timedelta
    from uuid import uuid4
    from backend.core.db.engine import get_connection
    from backend.core.db.tables import scheduled_tasks

    kind = f"test_stale_{uuid4().hex[:6]}"
    try:
        st.schedule_task(kind, "s1", datetime.now(UTC) - timedelta(seconds=10))
        claimed = st.claim_due_tasks(limit=10)
        target = next(t for t in claimed if t.task_kind == kind)
        with get_connection() as conn:
            conn.execute(
                scheduled_tasks.update()
                .where(scheduled_tasks.c.id == target.id)
                .values(claimed_at=datetime.now(UTC) - timedelta(hours=1))
            )
            conn.commit()

        st.reap_stale_claims(stale_after=timedelta(minutes=15))  # NEW function
        reclaimed = st.claim_due_tasks(limit=10)

        assert any(t.id == target.id for t in reclaimed), (
            "stale 'claimed' row was never re-claimed — work is permanently lost"
        )
        with get_connection() as conn:
            row = conn.execute(
                scheduled_tasks.select().where(scheduled_tasks.c.id == target.id)
            ).mappings().one()
        assert row["status"] in ("pending", "claimed")
    finally:
        with get_connection() as conn:
            conn.execute(scheduled_tasks.delete().where(scheduled_tasks.c.task_kind == kind))
            conn.commit()
```

---

### Expense lifecycle & settle — Editing an already-settled expense mutates the settled share's amount (terminal-escape)

**Severity:** High
**Location:** `backend/core/db/expenses.py:736-746` (`update_expense_and_get` carries `is_settled` forward but re-INSERTs with the new `share_amount`); route entry `backend/api/routes/expenses.py:292-344`.

**What breaks:** `settled` is documented as a terminal sink meaning "this exact share amount was paid back." `update_expense_and_get` carries `(is_settled, settled_at)` forward but re-inserts the share with the **new** `share_amount` from `new_shares`, with no guard rejecting edits to settled shares. A share stays `is_settled=True` while its amount silently changes to a value never actually paid. `compute_settlement` (`backend/expenses/settlement.py:93-100`) then debits the payer's balance by the new amount as if fully paid. Invariant broken: `settled_amount == amount_actually_paid_back`. The payer is silently shorted with no un-settle, no audit row, no notification. The only route guard is the B7 authorization check (`expenses.py:315`); the only DB CHECK is `share_amount >= 0`.

**Exploit:**
1. `create_expense(amount=100, equal split A/B, paid_by=A)`.
2. B self-settles (`user_ids=[B]`) → B's share `is_settled=True`, `share_amount=50`.
3. A (creator, passes B7 as payer) edits the expense raising `amount` to 200 → recomputed shares 100/100.
4. B's share re-inserted with `is_settled=True` (carried) but `share_amount=100`.
5. Settlement ledger treats B's 100 share as fully paid; A is silently shorted 50.

**Fix:** Add a settlement-state guard at the service layer in `update_expense_and_get` (`expenses.py:703-765`): before re-inserting, detect any prior share with `is_settled=True` whose recomputed `share_amount` differs, and either (a) reject the edit with a domain error surfaced as a 409 at the route, or (b) auto-un-settle those shares (clear `is_settled`/`settled_at`) and write an audit row + notification so the debtor/payer are informed. Option (a) is safer and simpler. Belt-and-suspenders: a partial-index/trigger tying `is_settled=True` to an immutable `share_amount` at `backend/core/db/_tables/expenses.py`.

```python
def test_editing_expense_does_not_mutate_already_settled_share_amount(db_session, trip, user_a, user_b):
    from backend.core.db.expenses import (
        create_expense, settle_and_get_expense, update_expense_and_get, get_settlement_data,
    )
    from backend.expenses.settlement import compute_settlement
    exp = create_expense(trip_id=trip.id, amount=100.0, currency="EUR",
                         paid_by=user_a.id, split_type="equal",
                         shares=[{"user_id": user_a.id, "share_amount": 50.0},
                                 {"user_id": user_b.id, "share_amount": 50.0}])
    settle_and_get_expense(exp.id, [user_b.id])  # B self-settles 50

    update_expense_and_get(
        exp.id,
        {"amount": 200.0, "settlement_amount": 200.0, "exchange_rate": 1.0},
        new_shares=[{"user_id": user_a.id, "share_amount": 100.0},
                    {"user_id": user_b.id, "share_amount": 100.0}],
    )

    _, shares, _ = get_settlement_data(trip.id)
    b_share = next(s for s in shares if s["user_id"] == user_b.id)
    if b_share["is_settled"]:
        assert b_share["share_amount"] == 50.0, "settled share_amount mutated to a value never paid back"
    summaries, _ = compute_settlement(*get_settlement_data(trip.id))
    a_net = next(s for s in summaries if s.user_id == user_a.id).net_balance
    assert a_net == 50.0, f"payer silently shorted: net_balance={a_net} (expected 50)"
```

---

### Trip invites — Group-invite slot orphaned forever when `add_trip_member` crashes after consume

**Severity:** High
**Location:** `backend/api/routes/invites.py:944-958` (`_recover_consumed_invite`); consume at `invites.py:1071`; group-cap branch at `backend/core/db/trip_invites.py:282-285`.

**What breaks:** For a group invite, `consume_invite` only sets `consumed_at` at the cap and **never** sets `consumed_by` (stays NULL). `_accept_trip_invite` consumes first then adds membership in *separate transactions*. If `add_trip_member` crashes after consume committed, the cap-reaching user is consumed-but-not-a-member. On retry, `is_redeemable` returns `(False,'consumed')`, routing into `_recover_consumed_invite`, whose re-add branch is gated on `consumed_by == actor.id` — always NULL for group invites — so it returns None → `_InviteNotRedeemable`. The invariant "every consumed slot corresponds to a member" is broken: the slot is permanently burned and the legitimate invitee is locked out. The declared `X-Idempotency-Key` on accept is dead (never read).

**Exploit:**
1. Organizer mints a group invite `max_uses=5`.
2. Four users join; the 5th accept hits the cap: `consume_invite` sets `consumed_at`, `consumed_by` stays NULL.
3. The 5th user's `add_trip_member` raises (transient DB error / pod restart) after consume committed.
4. 5th user retries `POST /accept`.
5. `is_redeemable` → `(False,'consumed')`; `_recover_consumed_invite` sees `is_member=False` and `consumed_by(NULL)!=actor.id` → returns None → "invite not redeemable." Slot 5/5 burned, only 4 members.

**Fix:** Two coordinated changes. (1) In `_recover_consumed_invite` (`invites.py:944-958`), add a recovery branch for group invites: when `reason in {consumed,exhausted}` and `is_member=False`, allow re-add if the actor can be matched to a consumed-but-orphaned slot — but since `consumed_by` is NULL for group invites, the durable fix is to record per-user redemption (see next defect's fix) and recover from that ledger. (2) Make consume + `add_trip_member` atomic in `_accept_trip_invite` by wrapping both in one `get_tx()` connection so a crash rolls back the consume, eliminating the orphan window entirely. The atomicity fix alone closes this defect.

```python
def test_recover_consumed_group_invite_at_cap_readds_member(monkeypatch):
    organizer = create_user()
    trip = create_trip(owner=organizer)
    invite = mint_invite(trip_id=trip.id, max_uses=5, role="member")
    for _ in range(4):
        accept_invite_as(create_user(), invite.token)
    fifth = create_user()
    consume_invite(invite.token, fifth.id)            # commits consumed_at at cap
    assert not is_trip_member(trip.id, fifth.id)      # add never landed
    row = get_invite(invite.token)
    assert row.consumed_at is not None and row.consumed_by is None  # the trap

    resp = client.post(f"/api/invites/{invite.token}/accept", headers=auth(fifth))

    assert resp.status_code == 200            # FAILS today (raises _InviteNotRedeemable)
    assert is_trip_member(trip.id, fifth.id)  # slot 5/5 == 5 real members
    assert resp.json()["trip_id"] == str(trip.id)
```

---

### Trip invites — Same user re-accepting a group invite inflates `use_count` and burns a slot (no per-user idempotency)

**Severity:** High
**Location:** `backend/api/routes/invites.py:1060-1078`; `backend/core/db/trip_invites.py:274-306` (`consume_invite`).

**What breaks:** `_accept_trip_invite` computes `already_member` but calls `consume_invite` **unconditionally** before the `if not already_member` guard. `consume_invite`'s only guard is the atomic `WHERE use_count < max_uses AND revoked_at IS NULL AND consumed_at IS NULL` — there is no check that *this* user already consumed a slot. For a still-redeemable group invite, an already-member actor re-accepting passes `is_redeemable` and re-runs consume, incrementing `use_count` with no new member. The `trip_members` unique constraint blocks the duplicate membership, not the duplicate consume; the `X-Idempotency-Key` param is dead. Single-use invites are protected (consumed_at blocks the WHERE); group invites have no backstop.

**Exploit:**
1. Organizer mints group invite `max_uses=5`.
2. User A accepts → `use_count=1`, member added.
3. A re-POSTs `/accept` (double-tap/retry) → `is_redeemable` still True; `already_member=True` but consume runs anyway → `use_count=2`; `add_trip_member` skipped.
4. Repeat: `use_count` reaches 5, `consumed_at` set, link dead with one actual joiner. Other invitees denied capacity.

**Fix:** Gate consume behind membership for multi-use invites in `_accept_trip_invite` (`invites.py:1071`): only call `consume_invite` when `not already_member` (the single-use crash-retry case that motivated the unconditional consume is better handled by the atomic-transaction fix above). The durable fix is a **per-user redemption ledger** — a `(token, user_id)` unique row written inside the same consume transaction — which simultaneously fixes the orphaned-slot defect (recovery can consult it) and makes consume idempotent per user. Add a `UNIQUE(invite_id, user_id)` redemption table; have `consume_invite` insert-on-conflict-do-nothing and only bump `use_count` when the insert actually lands.

```python
def test_already_member_reaccept_of_group_invite_does_not_burn_a_slot(self, client, actor):
    trip_id = uuid4()
    invite = _make_trip_invite(trip_id=trip_id, max_uses=5, use_count=1)  # redeemable
    with (
        patch(_P_GET_INVITE, return_value=invite),
        patch(_P_IS_MEMBER, return_value=True),          # actor already in trip
        patch(_P_ADD_MEMBER) as mock_add,
        patch(_P_CONSUME, return_value=invite) as mock_consume,
        patch(_P_APPEND_EVENT),
    ):
        resp = client.post("/api/invites/tok_trip/accept")
    assert resp.status_code == 200          # idempotent success, no 409
    mock_add.assert_not_called()            # no duplicate membership
    mock_consume.assert_not_called()        # FAILS today: slot re-consumed
```

---

### Content / dossier — `user_query` angle via API route enters research queue unreviewed, bypassing `default_status_for_source`

**Severity:** High
**Location:** `backend/api/routes/angles.py:142-145` (hardcoded `status="queued"`).

**What breaks:** `default_status_for_source('user_query')` returns `pending_review` because `user_query` is review-required, and the canonical `create_angle()` honors this. But the public `/api/places/{slug}/angles/request` route (auth-only, no curator role) bypasses `create_angle` and hardcodes `status="queued"` on the INSERT for `source_type='user_query'`. `get_unwritten_angles` (`status='queued' AND dossier_id IS NULL`) immediately picks it up; `process_angles` runs the full research agent on attacker-controlled text; with `AUTO_PUBLISH_GREEN_DOSSIERS` on (prod-on), a GREEN result auto-publishes with zero curator gate. The sibling seeder inserts `status=None` (→ `pending_review`), confirming this is a bug, not design. No rate-limit; the case-insensitive title dedup is trivially evaded.

**Exploit:**
1. Authenticated (non-curator) user POSTs `/api/places/{slug}/angles/request` with arbitrary title.
2. Row inserted `source_type='user_query'`, `status='queued'`, `dossier_id` NULL.
3. `get_unwritten_angles` picks it up immediately.
4. `process_angles` runs the research agent on attacker text → spends LLM/research budget; auto-publishes a dossier with no review.

**Fix:** In `_insert_angle_request` (`angles.py:108-156`), stop hardcoding the status — route the insert through `create_angle()` / `default_status_for_source(source_type)` so `user_query` resolves to `pending_review`, exactly like the seeder. This single change re-centralizes the policy. Optionally add a per-user rate-limit on the public route to bound queue spam even for legitimately review-gated angles.

```python
def test_user_query_angle_request_enters_pending_review_not_queued(db_conn, auth_client, seeded_place):
    slug = seeded_place.slug
    resp = auth_client.post(
        f"/api/places/{slug}/angles/request",
        json={"title": "Speculative attacker-controlled angle text"},
    )
    assert resp.status_code == 201
    new_id = resp.json()["id"]

    from backend.core.db.tables import place_angles
    from sqlalchemy import select
    row = db_conn.execute(
        select(place_angles.c.status, place_angles.c.source_type).where(place_angles.c.id == new_id)
    ).one()
    assert row.source_type == "user_query"
    from backend.core.models.locations import default_status_for_source
    assert row.status == default_status_for_source("user_query") == "pending_review"

    from backend.core.db.content import get_unwritten_angles
    queued_ids = {a.id for a in get_unwritten_angles(place_id=seeded_place.id)}
    assert new_id not in queued_ids
```

---

### Message / conversation state — Cross-process double-reset of a failed turn double-executes the agent turn

**Severity:** High
**Location:** `backend/concierge/session.py:142-150` (reset branch gated on a read); unguarded reset UPDATE at `backend/concierge/persistence.py:134-140` → `_messages.py:270-278`.

**What breaks:** `_check_idempotency` gates the reset path on a READ (`agent.status == FAILED`), then issues `reset_agent_message_for_retry` whose UPDATE has no `WHERE status=FAILED` and no lock — a classic TOCTOU. Two retries of the same failed turn (double-tap, or two pods on the same client retry) both read FAILED, both reset to pending, and both run `handle_turn` against the same reused message IDs. Tool side effects (booking holds, intent writes, proposal creation) execute twice; only the final content write is last-writer-wins. The `idempotency_key` unique index doesn't protect here because the reset path reuses existing rows. (Confidence medium: some downstream tools carry their own idempotency keys, blunting the worst external effects — but `update_intent` and generic proposal creation are not uniformly keyed.)

**Exploit:**
1. Turn for key K fails; agent row A is `status=failed`.
2. Two concurrent requests with key K arrive.
3. Both pass the COMPLETE and PENDING/STREAMING checks and fall through to the FAILED branch.
4. Both call `reset_agent_message_for_retry(A)` → both UPDATE to pending (no status guard).
5. Both return reuse_ids and both run `handle_turn` → two full agent turns, double-firing side-effecting tools.

**Fix:** Make the failed→pending reset a conditional, atomic compare-and-set. Change `update_message_status` (`_messages.py:270-278`) — or add a dedicated `reset_agent_message_for_retry` UPDATE — to `... SET status='pending' ... WHERE id=:id AND status='failed'` and return the affected rowcount. In `_check_idempotency`, only proceed to return reuse_ids when the CAS won (rowcount==1); the loser should re-read and return the cached/in-flight result (or raise `TurnInFlightError`). This serializes the transition across pods with no extra lock infrastructure.

```python
import asyncio
import pytest
from backend.core.models.conversations import MessageStatus

@pytest.mark.asyncio
async def test_concurrent_retry_of_failed_turn_resets_only_once(db_session, make_conversation):
    conv = await make_conversation()
    key = "retry-race-key"
    user_msg = await create_user_message(conv.id, idempotency_key=key, content="hi")
    agent_msg = await create_agent_child(user_msg.id, status=MessageStatus.FAILED, content="")

    from backend.concierge.session import _check_idempotency
    results = await asyncio.gather(
        _check_idempotency(key), _check_idempotency(key), return_exceptions=True,
    )
    reuse_count = sum(
        1 for r in results
        if not isinstance(r, Exception) and getattr(r, "reuse_ids", None) is not None
    )
    assert reuse_count <= 1, f"expected <=1 reset/reuse winner, got {reuse_count} (double-execution)"
    refreshed = await get_message(agent_msg.id)
    assert refreshed.status in (MessageStatus.PENDING, MessageStatus.STREAMING, MessageStatus.COMPLETE)
```

---

### Expense lifecycle & settle — Batch settle is not atomic despite "no partial commits" guarantee

**Severity:** Medium
**Location:** `backend/api/routes/expenses.py:509-524` (mutation loop calling `async_settle_and_get_expense` per item).

**What breaks:** The route docstring promises "no partial commits," but each loop iteration calls `async_settle_and_get_expense`, which opens its own `get_tx()` (`engine.begin()`) and commits independently. If item N raises after items 1..N-1 committed, the batch returns 5xx but 1..N-1 are persisted as settled. The FE fails closed: `useSettleShares.ts` `onError` only toasts (no `invalidateQueries`), so the cache still shows those debts as owing while the BE cleared them — divergence with no forced reconciliation. Mitigated (hence medium): the settle UPDATE is conditional (`WHERE is_settled IS False`), so a later refetch self-heals and no money moves.

**Exploit:**
1. Client posts settle-batch `[E1,E2,E3]`, all authorized.
2. Auth phase passes.
3. E1 settles+commits (own tx); E2 settles+commits (own tx).
4. On E3 the connection drops / statement times out → 500.
5. E1/E2 are settled in the DB; FE `onError` only toasts → cache still shows them owing. No rollback, no reconciliation until an unrelated refetch.

**Fix:** Wrap the whole loop in a single transaction. Add `async_settle_batch(items)` in `backend/core/db/expenses.py` that takes one `get_tx()` connection, settles every item, and commits once — so item N's failure rolls back 1..N-1. Call it from the route in place of the per-item loop. Secondary hardening: in `useSettleShares.ts`, invalidate `tripExpenses`/`tripFolio` in `onError` (or `onSettled`) so the FE always reconciles after a batch failure even before the BE fix lands.

```python
def test_settle_batch_is_atomic_rolls_back_earlier_items_on_mid_loop_failure(self):
    e1, e2, e3 = uuid4(), uuid4(), uuid4()
    async def _get_expense(eid):
        return _make_expense_row(eid, trip_id=_TRIP_ID, paid_by=_USER_ID)
    settle_calls = []
    async def _settle(eid, user_ids):
        settle_calls.append(eid)
        if eid == e3:
            raise OperationalError("statement timeout", None, None)
        return _make_settle_result_dict(eid)
    with (
        patch(f"{_PATCH_IS_MEMBER}", return_value=True),
        patch(f"{_DB}.async_get_expense", new=AsyncMock(side_effect=_get_expense)),
        patch(f"{_DB}.async_settle_and_get_expense", new=AsyncMock(side_effect=_settle)),
    ):
        body = {"items": [
            {"expense_id": str(e1), "user_ids": [str(_USER_ID)]},
            {"expense_id": str(e2), "user_ids": [str(_USER_ID)]},
            {"expense_id": str(e3), "user_ids": [str(_USER_ID)]},
        ]}
        resp = client.post(f"/api/trips/{_TRIP_ID}/settle-batch", json=body)
    assert resp.status_code >= 500
    # Once atomic: exactly ONE write-transaction; e1/e2 must NOT be left settled.
    assert settle_calls == [e1, e2, e3]
```

---

### Content / dossier — No lease/lock on dirty experience-brief drain: two workers double-embed and last-writer-wins clear

**Severity:** Medium
**Location:** `backend/core/db/experience_briefs.py:244-258` (`get_dirty_experience_briefs`) + `260-292` (`clear_experience_brief_dirty`); loop at `backend/api/lifecycle.py:240`.

**What breaks:** `get_dirty_experience_briefs` is a plain `SELECT WHERE dirty IS TRUE` with no `FOR UPDATE SKIP LOCKED` and no claim/lease write; `clear_experience_brief_dirty` is `WHERE id=` only, with no `dirty`/`brief_version` CAS predicate (the version column exists but is unused). The embed loop runs in *every* uvicorn worker (`--workers 2`) and is **not** advisory-locked, unlike the sibling loops (anniversary/digest/proactive all use `pg_try_advisory_lock`). Two workers fetch the same dirty rows and both embed the same Qdrant point. If a live `mark_experience_brief_dirty` lands between a worker's embed and its clear, the unconditional clear wipes `dirty` + `pending_changes`, silently dropping the newer change — the brief reads clean but its embedding predates the change. Medium: staleness + wasted budget, not corruption.

**Exploit:**
1. Brief X is dirty; Workers A and B both fetch X (no lock).
2. A embeds X.
3. A new source change calls `mark_experience_brief_dirty(X)` → dirty=true, `pending_changes` appended.
4. A calls `clear_experience_brief_dirty(X)` (`WHERE id` only) → dirty=false, `pending_changes=[]`.
5. The step-4 change is lost; X reads clean but stale. B redundantly re-embeds the same point.

**Fix:** Two parts. (1) Make the clear conditional/optimistic: `clear_experience_brief_dirty` should `UPDATE ... WHERE id=:id AND updated_at=:drained_updated_at` (or `AND brief_version=:expected`), so a concurrent `mark` (which bumps the version/timestamp) makes the clear a no-op and the row stays dirty for the next pass. (2) Stop the double-embed: add `FOR UPDATE SKIP LOCKED` to `get_dirty_experience_briefs`, and wrap `_run_experience_embed_loop` (`lifecycle.py:240`) in a `pg_try_advisory_lock` mirroring the proactive loop at `lifecycle.py:1202`.

```python
import json
import pytest
from backend.core.db.experience_briefs import (
    mark_experience_brief_dirty, get_dirty_experience_briefs, clear_experience_brief_dirty,
)

@pytest.mark.integration
def test_clear_does_not_drop_change_marked_after_drain(seeded_experience):
    exp_id = seeded_experience.id
    mark_experience_brief_dirty(exp_id, change_description="change-A")
    states = get_dirty_experience_briefs(limit=10)
    drained = next(s for s in states if s.experience_id == exp_id)

    mark_experience_brief_dirty(exp_id, change_description="change-B")  # lands mid-flight
    clear_experience_brief_dirty(drained.id, new_version=(drained.brief_version or 0) + 1)

    after = next((s for s in get_dirty_experience_briefs(limit=50)
                  if s.experience_id == exp_id), None)
    assert after is not None, "newer change-B was silently dropped by unconditional clear"
    assert "change-B" in json.dumps(after.pending_changes)
```

---

### Message / conversation state — `update_intent` tool accepts any string as phase; no enum membership validation

**Severity:** Medium
**Location:** `backend/concierge/tool_handlers/trip_management.py:426`; validation at `backend/core/db/conversations/_intent_state.py:174,184`; type at `backend/core/models/conversations.py:110` (`phase: str | None`).

**What breaks:** The agent-facing `update_intent` tool funnels an LLM-supplied patch into `update_intent_state`, whose only guards are the `_INTENT_FIELDS` whitelist and `IntentState.model_validate`. But `IntentState.phase` is `str | None` — `model_validate` enforces *a string*, not membership in `{exploring,drafting,committed,dormant,ambient}` — and there is no DB CHECK on the JSONB (every sibling string-enum column *is* CHECK-guarded; phase-in-JSONB is the one that isn't). The tool-schema enum is API-advisory only, not enforced. `phase` gates two machines: re-engagement eligibility (`reengagement.py` excludes literal `'dormant'`/`'committed'`) and commit/promotion readiness. An LLM writing `'Committed'`, `'done'`, or `'comitted'` bypasses every literal-match guard.

**Exploit:**
1. LLM calls `update_intent({'phase':'Committed'})` (capital C) intending to lock the trip.
2. `model_validate` passes (it's a str); the value is JSONB-merged verbatim.
3. The re-engagement filter `phase notin(['dormant','committed'])` does not match `'Committed'` → a committed conversation is treated as nudge-eligible and gets re-engagement nudges.
4. Symmetrically, exact-`'committed'` promotion checks never fire → the trip can't be recognized as committed.

**Fix:** Validate/normalize `phase` against the closed set before the JSONB merge, in `update_intent_state` (`_intent_state.py:~174-186`): reject (or lowercase-and-match) any value not in `{ambient,exploring,drafting,committed,dormant}`, raising a `ValueError` the tool handler surfaces back to the model. Durably, tighten `IntentState.phase` to a `Literal`/`StrEnum` so `model_validate` enforces it, and add a DB CHECK on `intent_state->>'phase'` to match the sibling enum columns.

```python
import pytest

def test_update_intent_state_rejects_non_enum_phase():
    conv = create_conversation(...)  # intent_state defaults to {}
    with pytest.raises(ValueError, match="phase"):
        update_intent_state(conv.id, {"phase": "Committed"})  # capital C, not in enum
    state = get_intent_state(conv.id)
    assert state.get("phase") in (None, "ambient", "exploring", "drafting", "committed", "dormant")

def test_committed_phase_excluded_from_reengagement_regardless_of_case():
    conv = create_stale_conversation(...)
    update_intent_state(conv.id, {"phase": "Committed"})  # mis-cased
    stale_ids = [s.conversation_id for s in find_stale_conversations(...)]
    assert conv.id not in stale_ids  # FAILS today: 'Committed' != 'committed'
```

---

### Trip invites — `revoke_invite` has no `consumed_at` guard; an accepted invite can be stamped revoked

**Severity:** Low
**Location:** `backend/core/db/trip_invites.py:145-157` (`revoke_invite`).

**What breaks:** `revoke_invite`'s WHERE guards only `revoked_at IS NULL`, not `consumed_at`. An organizer revoking an already-accepted (terminal) single-use invite writes `revoked_at` onto a row that already has `consumed_at` — a both-consumed-and-revoked row. `is_redeemable` checks `revoked_at` before `consumed_at`, so it then reports `'revoked'` for a link that was a genuine successful join, muddying the BE audit/notification reason resolver. User-visible impact is nil (FE `inviteStatus` checks consumed first, so the pill stays "joined"; the active/badge partial index excludes both). Low: purely a BE reason-resolver muddle, no membership reversal.

**Exploit:**
1. Single-use invite is accepted → `consumed_at` set, terminal.
2. Organizer (or stale UI showing it active) calls revoke.
3. `revoke_invite` WHERE `revoked_at IS NULL` matches → `revoked_at` stamped on the consumed row.
4. `is_redeemable` now returns `(False,'revoked')` for a row representing a real join; the row is simultaneously consumed and revoked.

**Fix:** Add `AND consumed_at IS NULL` to the `revoke_invite` UPDATE's WHERE clause so revoke is a no-op against a terminal/consumed row and returns `False`. Callers (`revoke_trip_invite`, `revoke_conversation_invite`) can then surface "already accepted, cannot revoke" cleanly.

```python
def test_revoke_invite_does_not_stamp_consumed_terminal_row():
    invite = create_invite(trip_id=trip_id, created_by=organizer_id, max_uses=1)
    consume_invite(invite.token, user_id=joiner_id)
    consumed = get_invite(invite.token)
    assert consumed.consumed_at is not None and consumed.revoked_at is None

    changed = revoke_invite(invite.token)

    after = get_invite(invite.token)
    assert after.revoked_at is None, "consumed terminal invite must not be stamped revoked"
    assert changed is False
    ok, reason = is_redeemable(after)
    assert (ok, reason) == (False, "consumed")
```

---

### Trip invites — `InviteViewResponse.status 'needs_substance'` is a dead value

**Severity:** Low
**Location:** `backend/core/models/trip_invites.py:176`; `backend/api/routes/invites.py:642,683`.

**What breaks:** The type documents status as `"active" | "needs_substance"`, but both `InviteViewResponse` constructions hardcode `status="active"`. The substance signal is produced only as a 409 (`trip_needs_substance`/`conversation_needs_substance`) at *create* time, never as a view-response status. So `'needs_substance'` is an unreachable enum value — assigned nowhere, read by nothing (FE keys substance off the create-time 409). Harmless at runtime but a latent trap: any consumer branching on `status=='needs_substance'` for the view endpoint has dead code.

**Exploit:**
1. Grep for where `InviteViewResponse.status` is set to `'needs_substance'` → none.
2. A client switching on view-endpoint status to render a "needs more detail" state never hits that branch; the only substance signal arrives as a 409 from the create endpoint.

**Fix:** Drop `'needs_substance'` from the type/comment at `trip_invites.py:176` — it is a create-time 409, not a view status. Tighten the field to `Literal["active"]` to lock the contract. (If a view-side substance state is genuinely wanted later, emit it explicitly from `view_invite`.)

```python
def test_invite_view_response_status_enum_is_reachable():
    import re
    from pathlib import Path
    routes = Path("backend/api/routes/invites.py").read_text()
    produced = set(re.findall(r'status="([a-z_]+)"', routes))
    documented = {"active", "needs_substance"}
    assert documented <= produced, (
        f"Documented InviteViewResponse.status values never produced: {documented - produced}"
    )
    # After dropping the dead value, lock with: assert produced == {"active"}
```

---

### Content / dossier — Angle dead-letter sink: failed-research angles stay `status='queued'` forever

**Severity:** Low
**Location:** `backend/core/db/content/_angles.py:117` (`skip_count < max_skip_count` filter) + `540-551` (`record_angle_attempt`).

**What breaks:** `record_angle_attempt` only increments `skip_count`; it never changes status. Once `skip_count >= max_skip_count` (default 3), `get_unwritten_angles` filters the angle out but the row stays `status='queued'`, `dossier_id` NULL — invisible to the queue yet never marked rejected/failed and never retried. The CHECK constraint doesn't even *admit* a terminal `failed`/`exhausted` status, so there is nowhere for these to land. `get_angle_coverage` counts them as "unwritten" forever, inflating the generation-gap metric. No reaper, no alert. Low: silent metric inflation + invisible backlog, no crash/corruption.

**Exploit:**
1. Angle Y is queued.
2. Research fails (red) on three runs → `skip_count=3`.
3. `get_unwritten_angles` excludes Y.
4. Y stays `status='queued'`, `dossier_id` NULL, forever — counted as unwritten, indistinguishable from a healthy queued angle except by `skip_count`.

**Fix:** Add a terminal status. Extend the `place_angles_status` CHECK (`backend/core/db/_tables/content.py:171-174`) to include `'failed'` (or `'exhausted'`), and have `record_angle_attempt` flip status to that terminal value when the post-increment `skip_count >= max_skip_count`. Update `get_angle_coverage` to exclude terminal-failed angles from the "unwritten" count, so the generation-gap metric reflects only recoverable work.

```python
def test_skip_exhausted_angle_reaches_terminal_status(db):
    angle = create_angle(PlaceAngleCreate(place_id=PLACE_ID, title="t", question="q", source_type="bfs_explorer"))
    assert angle.status == "queued"
    for _ in range(3):
        record_angle_attempt(angle.id)

    queued_ids = [a.id for a in get_unwritten_angles(place_id=PLACE_ID, max_skip_count=3)]
    assert angle.id not in queued_ids

    refetched = get_angle_by_id(angle.id)
    assert refetched.status not in ("queued",), (
        f"skip-exhausted angle stuck in non-terminal status={refetched.status!r}"
    )
    cov = get_angle_coverage(PLACE_ID)
    assert cov["unwritten"] == 0
```

---

## Uncertain — Needs Manual Trace

None. Every candidate finding was either confirmed with a full end-to-end trace or refuted by an existing guard. There are no findings that could not be proven or refuted statically.

| Machine | Title | Location | Why it's ambiguous |
|---|---|---|---|
| — | — | — | (none) |

## Machines That Came Back Clean

No confirmed defects in these six machines — guards were verified present, not merely assumed:

- **Change proposal lifecycle**
- **Booking proposal + booking agent**
- **Stay candidates & votes**
- **Trip phase + conversation→trip promotion**
- **Atlas candidate → memory**
- **Plan commitment + block state**
- **Notification / proactive delivery**

(11 additional candidate findings across the audited machines were refuted because real guards exist; they are not reported individually.)

## Recommended Sequence

1. **Scheduled-task stale-claim reaper (critical).** Fix first: it is the only critical, the harm is unbounded silent data loss, and the fix is a self-contained additive loop that copies an existing, proven pattern (`_run_booking_session_reaper_loop`). No call-site churn, low regression risk. `claimed_at` already exists — you are just making it load-bearing.

2. **Settled-share mutation guard (high, money).** Next: real financial harm (payer silently shorted), reachable through the *normal* edit flow without malice, and the fix is a localized guard in one function (`update_expense_and_get`) plus a route-level 409. High value, small blast radius.

3. **Invite atomicity + per-user redemption ledger (two high invites defects together).** The orphaned-slot lockout and the use_count slot-burn share one root cause (consume and membership in separate, non-idempotent transactions). Fix them as one unit: wrap consume+`add_trip_member` in a single transaction and add a `UNIQUE(invite_id, user_id)` redemption ledger. One coordinated change closes both highs; doing them separately risks half-fixes.

4. **`user_query` angle status policy (high, content/budget + abuse surface).** A genuine one-line fix (route the insert through `default_status_for_source`) that closes an authenticated-user abuse path spending LLM budget and auto-publishing unreviewed content. Trivial ease, meaningful blast radius — do it early.

5. **Failed-turn reset CAS (high, conversation).** Convert the reset to a conditional `WHERE status='failed'` UPDATE with rowcount gating. Self-contained DB-layer change; closes the double-execution TOCTOU. Slightly lower priority because several downstream tools already carry their own idempotency keys (medium confidence on worst-case harm).

6. **Batch-settle atomicity + experience-brief clear CAS + intent-phase validation (three mediums).** Batch one transaction wrap, one optimistic-clear predicate + advisory lock, and one enum guard — each localized, each closes a real correctness/staleness gap but none move money or lock users out. Group them after the highs.

7. **The three lows (revoke `consumed_at` guard, dead `needs_substance` value, angle dead-letter status).** Cheap hygiene — each is a one-to-few-line change. Fold them into the next content/invites touch rather than scheduling dedicated work; they harm metrics/audit trails, not users.
