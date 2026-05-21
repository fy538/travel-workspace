# Area 06 — Propose / Apply / Revert Trust Loop

**Auditor:** Cursor cloud agent (Opus 4.7), read-only.
**Scope:** backend `propose_change` → ledger → apply → diff-safe revert,
plan-state read-model, concurrency on votes/resolves/reverts, and the
`Travel App/components/trip-plan/*` + `ProposalReviewSheet` UX that
exposes "honest apply state" and "force full revert" to the group.

---

## Summary

The Phase 3 trust loop is *mostly* well thought through — the append-only
`plan_events` ledger, per-field `BlockDiff` capture, forward-chain block-ID
translation, and the `apply_status` first-class column on `change_proposals`
are real and load-bearing. But there is one **system-breaking bug at the
core of revert** and several smaller bugs that all sit on the same trust
seam: the headline status the user sees can diverge from what actually
happened to the itinerary.

The two highest-stakes findings:

1. **P0-1 (Revert never flips status to `withdrawn`)** — the
   `resolve_proposal` DB call used by the revert endpoint is guarded on
   `WHERE status='open'`, so an `accepted` → `withdrawn` transition is
   a no-op. The itinerary blocks ARE reverted, the ledger event is
   written, the receipt is posted — but `change_proposals.status` stays
   `accepted`, `apply_status` stays `succeeded`, and the proposal looks
   to every reader (Plan v2, Changes screen, ProposalReviewSheet) like
   it was just accepted. The Revert button on `ProposalReviewSheet`
   stays live, so users can "revert" the same proposal repeatedly,
   piling up `diff_safe_partial` conflicts each time. Every test in
   `tests/api/test_proposals_api.py` mocks `db_resolve`, so this is
   invisible to CI.

2. **P0-2 ("Force full revert" is a silent no-op)** — the frontend
   `RevertConflictSheet` "Force full revert" button calls
   `revertProposal(..., { mode: 'version_restore' })`, but the backend
   `RevertRequest` model has no `mode` field. The body field is
   discarded by Pydantic; the backend re-runs the same `diff_safe` path
   which still finds the `proposal_applied` event and re-runs the same
   partial revert. The "later changes will be lost" warning copy is a
   promise the backend cannot keep — there is **no version-restore
   trigger reachable from the UI at all** for a proposal whose ledger
   event exists.

Three more material findings sit in the same trust-loop neighborhood:

3. **P0-3 (Auto-approve bypasses delegation entirely)** — the agent
   alone decides `approval_mode='auto_approve'` and immediately
   mutates the plan; `DelegationLevel.ask` on `group_proposals` /
   `venue_swaps` is never consulted, and the `trips.voting_enabled`
   gate explicitly only covers the voting modes. Members who said
   "ask me first" can wake up to a changed itinerary.

4. **P1-4 (Double-accept race re-forks the itinerary)** — two
   organizers tapping "Accept" simultaneously without `X-Idempotency-Key`
   both pass the route guard; the second call sees `proposal.status=='accepted'`
   from the read-after-write fallback and re-enters `apply_accepted_proposal`,
   which has no `apply_status`-idempotency check and re-forks.

5. **P1-5 (Diff shown to user can drift from what applied)** — the
   `before_snapshot`/`after_snapshot` on `impact_analysis` are frozen
   at *proposal-creation* time. The apply helpers capture the real
   `BlockDiff` against current block values, which can be different
   if the block was edited between propose and apply. The
   `BlockDiffChip` and `DiffRow` keep showing the stale text.

Several P2 UX issues compound the bugs (Undo button on rejected /
already-reverted proposals; delete-on-revert losing later edits to
added blocks; vote-loss race at deadline; etc.).

The good news: the ledger itself is honest and append-only, the
`BlockDiff` capture is well-structured, and the forward chain is the
right shape. Most of the bugs above are localized to one or two
functions.

---

## Findings

### [P0] — Revert never flips proposal status to `withdrawn`; UI still reads "Accepted" + Revert button stays live

**References:**
- `Travel Agent/backend/core/db/change_proposals.py:253-308` (`resolve_proposal` guarded on `WHERE status='open'`)
- `Travel Agent/backend/api/routes/proposals.py:495-526` (revert route calls `db_resolve(status="withdrawn", ...)` on a proposal whose status is `accepted`)
- `Travel Agent/backend/core/db/plan_state.py:445-471` (`_build_recent_changes` only emits `proposal_reverted` when `status=='withdrawn' AND was_reverted`)
- `Travel App/components/trip/ProposalReviewSheet.tsx:772-786` (Revert button is gated on `proposalStatus === 'accepted'`)
- `Travel Agent/tests/api/test_proposals_api.py:737-744` (every test mocks `_PATCH_RESOLVE` to return a synthetic `withdrawn_proposal`, so the bug is invisible)

**Why it matters to a real tester:**
The whole Phase 3 trust loop pivots on the user being able to undo
an accepted change. Today the revert endpoint runs the diff-safe
reverse-patch, writes the ledger event, posts the chat receipt — and
then tries to flip `change_proposals.status` from `accepted` to
`withdrawn` via a function that only updates rows where
`status='open'`. The UPDATE matches 0 rows; the function falls back
to `return get_change_proposal(...)` which returns the still-accepted
proposal; the route happily writes that back to the client. Net
result:
- `change_proposals.status` stays `accepted` forever (`resolution_note`,
  `resolved_by`, `resolved_at` are not overwritten either).
- `apply_status` stays `succeeded`.
- `metadata_.was_reverted=True` is the **only** durable signal that
  a revert ever happened — and the plan-state aggregator's
  `_build_recent_changes` only consults `was_reverted` inside the
  `elif proposal.status == "withdrawn"` branch, so the change shows
  up as `proposal_accepted` ("Proposal accepted") in Plan v2 +
  Changes screen, not `proposal_reverted`.
- `ProposalReviewSheet` reads `proposal.status==='accepted'` and
  keeps rendering the Revert button. A tester who clicks Revert a
  second time triggers another diff-safe attempt; this time every
  field's *current* value matches `old` (not `new`), so every field
  is marked as a conflict — the `diff_safe_partial` banner appears
  with the entire proposal as "later changes kept". The Revert
  button still stays live. They can do this indefinitely.
- The block-level `BlockChangedBanner` reads
  `recent_change_ids → 'proposal_accepted'` and keeps rendering
  "Vesper changed this · Undo", even though the block values are
  back to pre-apply.
- The Plan Change Strip / chat receipts say "Accepted" while the
  itinerary actually shows the pre-accept state. Two surfaces
  contradict each other — exactly the trust violation the audit
  prompt asked us to hunt for ("an apply that reports success but
  didn't mutate (or vice-versa)").

Tests don't catch this because every assertion in
`tests/api/test_proposals_api.py::test_revert_*` mocks
`backend.core.db.change_proposals.resolve_proposal` and forces it to
return a hand-built `withdrawn_proposal`. The real DB function is
never exercised in the revert-path tests.

**Repro / deterministic test idea:**
Integration test against real Postgres (the existing
`@requires_postgres` lane):

```python
# Seed: open proposal → resolve as accepted → apply succeeds.
p = create_change_proposal(...)
resolve_proposal(p.id, "accepted", resolved_by=u, ...)
apply_accepted_proposal(p.id)
assert get_change_proposal(p.id).status == "accepted"

# Now revert via the route.
client.post(f"/api/trips/{trip}/proposals/{p.id}/revert", json={})

# This is the assertion that currently fails.
final = get_change_proposal(p.id)
assert final.status == "withdrawn", f"status stuck at {final.status}"
assert final.was_reverted is True
```

Or, simpler unit-level: call
`resolve_proposal(p.id, "withdrawn", resolved_by=u)` directly on a
proposal whose current status is `accepted`. Today it returns the
unchanged accepted proposal and writes nothing. It must transition
to `withdrawn` (or raise) for the revert flow to work.

**Suggested fix direction:**
Two options, pick one:
1. Relax `resolve_proposal`'s guard so revert can pass an allow-list:
   add an optional `from_status: tuple[str, ...] = ("open",)` parameter
   and call from the revert endpoint with `from_status=("accepted",)`.
   This keeps the optimistic-concurrency contract (still rejects the
   double-revert race if a sibling beat us to `withdrawn`).
2. Or: introduce a dedicated `mark_proposal_reverted(proposal_id, ...)`
   DB helper that does `UPDATE … SET status='withdrawn',
   resolved_at=now(), resolution_note=… WHERE id=… AND status='accepted'`,
   and have the revert endpoint call it instead of `db_resolve`. This
   has the bonus of writing an explicit `proposal_reverted` event type
   from the helper, so the route doesn't need its separate `write_event`
   call.

Also: backfill a `@requires_postgres` test for the route that calls
the **real** `resolve_proposal` end-to-end so this bug class can't
sneak back. The existing tests over-mock the DB layer.

**Confidence:** High. The code path is short and the bug is mechanical
— I traced it from the route into `db_resolve`, the WHERE-clause guard
is unambiguous, and no other writer touches `change_proposals.status`
(verified with `grep withdrawn backend/`).

---

### [P0] — "Force full revert" button is silently a no-op; users cannot escape `diff_safe_partial`

**References:**
- `Travel App/components/trip-plan/RevertConflictSheet.tsx:83-95` (button copy promises "This will restore the plan to before this proposal. Later changes listed above will be lost.")
- `Travel App/components/trip/ProposalReviewSheet.tsx:241-249` (`forceRevertMutation` sends `{ mode: 'version_restore' }`)
- `Travel App/utils/api/types.ts:916-924` (TS type already flags this drift: "UI-ONLY: backend ``RevertRequest`` does not currently carry ``mode``")
- `Travel App/utils/api/http.ts:779-784` (request body forwarded as-is)
- `Travel Agent/backend/api/routes/proposals.py:59-67` (`RevertRequest` only has `resolution_note`; FastAPI silently drops the extra `mode` field)
- `Travel Agent/backend/core/db/proposal_apply.py:679-792` (`_try_diff_safe_revert` always wins when the `proposal_applied` event exists; `version_restore` is unreachable from a v2 proposal)

**Why it matters to a real tester:**
A real failure mode for the "revert" trust loop is exactly the one
the conflict sheet is built for: organizer reverts; some blocks were
edited since the apply; the user is told "I kept these later changes
to be safe, force a full revert if you want them gone." They tap
"Force full revert" expecting the plan to snap back to pre-accept
state — and absolutely nothing changes. The same partial result
reappears. There is no error toast (HTTP returns 200), no console
warning, no telemetry signal. The user concludes that the agent is
either lying or fundamentally broken; either way the trust loop is
gone for that trip.

The drift is also called out in a code comment on the frontend
(`types.ts:916`) — it's known but not closed. Because the field is
on a Pydantic model with no `extra="allow"`, the extra key is
discarded with no log line either side, so this drift is invisible
in production.

The downstream effect is worse than just "the button doesn't work":
once you're in `diff_safe_partial` mode, the **only** way to reach
`version_restore` is for the `proposal_applied` event to be missing
— which is only true for proposals accepted before Phase 2 shipped.
For any modern proposal, the version-restore fallback is dead code
behind the UI.

**Repro / deterministic test idea:**
1. Accept a proposal. Apply succeeds.
2. Manually edit one of the affected blocks (e.g. PATCH the block
   `notes` field through any other path, or via a second proposal).
3. Tap Revert. Backend returns `revert_mode='diff_safe_partial'`
   with a non-empty `revert_conflicts`.
4. Open the conflict sheet, tap "Force full revert".
5. Observe network: `POST /revert {"mode": "version_restore"}` → 200.
6. Re-fetch `/plan-state` and `/proposals/{id}` — itinerary still has
   the later edits; conflict count unchanged. Assert that this is
   wrong.

Or pure unit: assert FastAPI raises on `RevertRequest(mode="version_restore")`
(it currently does not, because the field is silently dropped) — or
add an end-to-end test that POSTs `{"mode": "version_restore"}` and
asserts the revert result has `mode='version_restore'`.

**Suggested fix direction:**
Add `mode: Literal["diff_safe", "version_restore"] | None = None`
to `RevertRequest`. When `mode='version_restore'`, branch in
`revert_accepted_proposal_v2` to skip `_try_diff_safe_revert` and
go straight to the full-version restore path. Make sure the new
write path also clears the `proposal_applied` event's effect on
future revert attempts (e.g. write a `proposal_force_restored`
event so a subsequent diff-safe lookup knows the field-level
diff is no longer authoritative).

Sync `Travel App/utils/api/types.ts` to import `mode` from the
generated schema rather than carrying a hand-maintained
`RevertProposalRequest` — once the backend has the field, drop the
UI-only interface.

Until the fix lands, hide the "Force full revert" button or
swap it for "Restore the original plan (admin only)" and route to a
support flow — anything is better than a button that lies.

**Confidence:** High. The frontend type file itself documents the
gap; I confirmed the round trip by reading the FastAPI route model.

---

### [P0] — `auto_approve` proposals bypass delegation preferences and `trips.voting_enabled`; agent can mutate plan without consent

**References:**
- `Travel Agent/backend/concierge/tool_handlers/planning/_propose_present.py:124-141` (`voting_enabled` gate explicitly only covers `lazy_consensus` / `active_approval` — `auto_approve` falls through)
- `Travel Agent/backend/concierge/tool_handlers/planning/_propose_present.py:247-254` (`approval_mode == "auto_approve"` immediately runs `_do_resolve(..., "accepted", ...)`)
- `Travel Agent/backend/concierge/proposal_automation.py:281-345` (`_do_resolve` calls `apply_accepted_proposal` directly)
- `Travel Agent/backend/core/models/delegation.py:11-14` (`DelegationLevel ∈ {ask, suggest_confirm, auto}`; `CATEGORY_IDS` includes `group_proposals` and `venue_swaps`)
- `Travel Agent/backend/api/routes/delegation.py` (registry exists, but **no caller** in `_propose_present.py` or `proposal_automation.py` reads from it)

**Why it matters to a real tester:**
The product narrative is "the agent edits the shared itinerary as
reviewable diffs the group can approve/revert." A member who has
explicitly set their `group_proposals` delegation to `ask` (the
strictest level) reasonably expects the plan never to change
silently. Today the agent has full unilateral authority to set
`approval_mode='auto_approve'` and immediately mutate the plan; the
delegation tier is never consulted. The only gate is a per-trip
`voting_enabled` boolean, which by design only governs the voting
modes — `auto_approve` is by-design *outside* the voting system,
which means it's also outside the consent system.

This is the launchpad for the Act stage: if delegation isn't load-
bearing for Propose, it won't be load-bearing for Act either, and
the first time a member finds their booked dinner swapped without
their vote, the social contract collapses.

A pre-dogfood tester is likely to discover this the first time
they ask the agent for a "tiny tweak" — the agent picks
`auto_approve`, applies, posts a `change_applied` receipt, and the
tester sees the plan mutate in a group chat that they assumed
would just float a proposal.

The current `should_require_hotel_booking_vote` triage exists for
bookings (`proposal_automation.py:47-106`) and reads delegation
levels correctly. There's no analogous gate for
`approval_mode='auto_approve'` on change proposals.

**Repro / deterministic test idea:**
1. Set User B's `group_proposals` delegation to `ask` via
   `PUT /api/me/delegation-preferences`.
2. As User A (organizer), ask the agent to propose a "low-stakes
   swap" of a block. Confirm the agent's tool call uses
   `approval_mode='auto_approve'`.
3. Observe: proposal is applied immediately. User B's chat shows a
   `change_applied` card with no chance to react. Assert this is wrong.

Or unit-level: extend `_execute_propose_change` test to assert that
when ANY non-organizer member has `group_proposals=ask`, the
`approval_mode` is forced to `lazy_consensus` (or to error out and
return an `error_category='delegation_requires_vote'` so the agent
re-drafts with a vote widget).

**Suggested fix direction:**
At the top of `_execute_propose_change` after the
`voting_enabled` check, add a delegation triage:

```python
from backend.core.db.delegation import get_delegation_levels_for_trip
levels = get_delegation_levels_for_trip(trip_id, category="group_proposals")
if approval_mode == "auto_approve" and any(l == "ask" for l in levels.values()):
    approval_mode = "lazy_consensus"
    # Or: return an error_category='delegation_requires_vote' envelope
    # so the agent re-drafts with a deadline and we don't override the
    # agent's choice silently.
```

Long-term: factor a `should_require_vote_for_proposal(trip_id,
proposal_category)` mirror of the hotel triage so flight + dining
+ activity proposals all use the same delegation logic.

**Confidence:** Medium. The bypass is real and grep-confirmed; the
exact "right" fallback (downgrade to `lazy_consensus` vs error out)
is a product call.

---

### [P1] — Double-accept race re-forks the itinerary and produces a phantom version

**References:**
- `Travel Agent/backend/api/routes/proposals.py:319-394` (`resolve_proposal` endpoint)
- `Travel Agent/backend/api/routes/proposals.py:342-349` (idempotency only fires when the caller sends `X-Idempotency-Key`)
- `Travel Agent/backend/core/db/change_proposals.py:253-308` (`db_resolve` returns the post-update row OR falls back to `get_change_proposal` on 0-row update)
- `Travel Agent/backend/core/db/proposal_apply.py:136-156` (`apply_accepted_proposal` only checks `if proposal.status != "accepted"`; no `apply_status='succeeded'` short-circuit)

**Why it matters to a real tester:**
Two organizers tapping "Accept" on the same proposal at the same
moment (extremely plausible — the proposal sits in the group chat,
both see it, both tap because they want to "be helpful"):

1. Both pass `is_trip_organizer`.
2. Both fall through the idempotency guard (mobile doesn't send
   `X-Idempotency-Key` on resolve — I checked
   `Travel App/utils/api/http.ts:772` and there's no header).
3. Both call `db_resolve(status='accepted')`. Only one wins the
   `WHERE status='open'` UPDATE; the other gets the now-accepted
   row from the fall-through `return get_change_proposal(...)`.
4. Both routes see `body.status == 'accepted'` and call
   `apply_accepted_proposal(proposal_id)`.
5. The second `apply_accepted_proposal` has no apply-idempotency
   guard. It loads the (now post-first-fork) itinerary as
   "original", forks AGAIN (version N+2), tries to map old block
   IDs (which are from pre-first-fork) against the new fork's
   positions, fails most lookups, fires the title-match fallback,
   and either applies to wrong blocks or no-ops while still
   creating a useless N+2 version with `apply_status='succeeded'`.
6. Two `proposal_applied` events for the same proposal end up in
   the ledger with different `applied_block_map`s. The forward
   chain in `_build_block_forward_chain` is built from
   `resolved-at`-sorted accepted proposals; with two applies
   sharing one `resolved_at` (or differing by microseconds), the
   chain becomes unstable.

The user-facing damage:
- Itinerary version count silently doubles for every contested
  accept.
- Plan v2 may show "changed_recently" on the wrong blocks after
  the second apply's title-match fallback.
- Diff-safe revert later reads the ledger and tries to reverse
  two diffs over each other — produces nonsense conflicts.

**Repro / deterministic test idea:**
```python
# Two threads/connections, same proposal.
p = create_change_proposal(...)
def accept():
    requests.post(f".../proposals/{p.id}/resolve", json={"status":"accepted"})
threads = [threading.Thread(target=accept) for _ in range(2)]
[t.start() for t in threads]; [t.join() for t in threads]

# After both: assert exactly ONE itinerary version was created post-accept.
hist = get_itinerary_history(p.trip_id)
assert len(hist) == initial_history_len + 1
# And only one proposal_applied event.
events = get_events_for_source("proposal", str(p.id))
assert sum(1 for e in events if e.event_type == "proposal_applied") == 1
```

**Suggested fix direction:**
Two layers:
1. In `apply_accepted_proposal`, short-circuit on
   `proposal.apply_status == "succeeded"` (now a first-class
   column) — log and return the existing itinerary version. This
   makes apply idempotent regardless of caller.
2. Make the route's idempotency guard automatic. Either always
   require `X-Idempotency-Key` for `/resolve` and `/revert` (and
   add it on the frontend mutation hook), or hash
   `(trip_id, proposal_id, body.status)` and de-dupe within a 5s
   window. The mobile mutation already retries on network blips,
   so the header is cheap.
3. Add an `apply_attempts` counter to the
   `proposal_applied` event payload or a sibling
   `proposal_apply_skipped` event so the audit trail records the
   contention rather than hiding it.

**Confidence:** High on the mechanism, Medium on observed impact
without contention testing. The repro is purely deterministic.

---

### [P1] — Diff shown to the user can drift from what the apply actually mutated

**References:**
- `Travel Agent/backend/concierge/tool_handlers/planning/_propose_present.py:148-178` (`before_snapshot`/`after_snapshot` are captured at *proposal-creation* time from `get_block_for_trip`)
- `Travel Agent/backend/core/db/proposal_apply.py:346-486` (apply helpers capture `_capture_block_diff` against the *forked* block's current values, not against the snapshots)
- `Travel App/components/trip-plan/BlockDiffChip.tsx:22-44` (renders the stale `impact_analysis.before_snapshot.title → after_snapshot.title`)
- `Travel App/components/trip/ProposalReviewSheet.tsx:453-478` (`DiffRow` reads the same stale snapshots, never the ledger `block_diffs`)
- `Travel Agent/backend/core/db/_tables/itinerary.py:269-279` (apply ledger has the real diffs, no API exposes them yet)

**Why it matters to a real tester:**
The diff is the user's primary signal for what they're approving.
If a block is edited between propose and apply — by a parallel
manual edit, a competing proposal accepted first, or a forked-then-
edited version — the `before_snapshot` written into
`impact_analysis` at proposal-creation is stale. The user sees
"Belcanto → Taberna," approves it, and the apply silently mutates
"Cervejaria Ramiro" (the block's actual current title) → "Taberna."
The chat receipt still says "Belcanto → Taberna." Anyone reading
the proposal detail later sees a diff that bears no resemblance to
what landed.

This is the exact "a diff shown to the user that doesn't match what
applied" failure mode the audit prompt asked us to hunt for. The
ledger DOES capture the honest diff in
`plan_events.payload.block_diffs`, but no API exposes it and no UI
component reads from it.

The risk is amplified by the forward-chain machinery: the
proposal's `affected_block_ids` are translated through
`applied_block_map` for plan-state attachment, but the impact
snapshots are not re-resolved. So even the "Touches on your plan"
section in `ProposalReviewSheet` shows the current block via
forward-chain translation while the diff text shows a different
block from proposal-creation time.

**Repro / deterministic test idea:**
1. Create a proposal `P1` against block `B1` (title "Belcanto"),
   `proposal_type='swap'`, alternative_options[0].venue_name="Taberna".
2. Before resolving `P1`, accept-and-apply a sibling proposal `P0`
   that renames `B1` to "Cervejaria Ramiro".
3. Resolve `P1` as accepted. Apply runs `_apply_swap` which sets
   title to "Taberna" against current title "Cervejaria Ramiro".
4. Assert: ledger event `proposal_applied.payload.block_diffs[0].fields.title`
   is `{"old": "Cervejaria Ramiro", "new": "Taberna"}`.
5. Assert: `GET /proposals/{P1}.impact_analysis.before_snapshot.title`
   is "Belcanto" (proves drift).
6. Assert (the fix): `ProposalReviewSheet` `DiffRow` shows the
   ledger value, not the impact_analysis value. This currently
   fails — the component reads `impact_analysis` only.

**Suggested fix direction:**
1. Expose the ledger's `block_diffs` on the `ProposalDetail`
   response (or as a sibling `GET /proposals/{id}/applied-diff`
   endpoint that returns `[{block_id, before: {...}, after: {...}}]`).
2. Update `BlockDiffChip` and `DiffRow` to prefer the ledger payload
   when `apply_status='succeeded'`; fall back to
   `impact_analysis.before/after_snapshot` only for `status='open'`
   proposals (where there's no applied diff yet — the snapshot is
   the agent's plan, not the truth).
3. Rename the `impact_analysis` snapshot keys to make the difference
   explicit (`proposed_before` / `proposed_after`) so future readers
   understand the snapshot is a forecast, not a record.

**Confidence:** High on the divergence path, Medium on real
incidence rate at dogfood scale (depends on how often parallel
edits happen on the same block).

---

### [P1] — `apply_accepted_proposal` title-match fallback can apply to the wrong block

**References:**
- `Travel Agent/backend/core/db/proposal_apply.py:200-229` (fallback scan when `affected_block_ids` all fail to map; matches by substring of `block.title` in `proposal.title + description`)
- `Travel Agent/backend/core/db/proposal_apply.py:213` (`if len(title_key) < 4: continue` — guard, but "Café" or "Park" still pass)

**Why it matters to a real tester:**
When `apply_accepted_proposal` can't position-map the proposal's
old block IDs into the freshly-forked itinerary (e.g. an
intervening fork changed positions / removed days), it falls back
to scanning every block and substring-matching the block's title
into the proposal title + description. A proposal titled "Swap
out the bar tonight for something quieter" against an itinerary
containing both "Park Bar" and "Lounge Bar" matches BOTH (title
keys "park bar" and "lounge bar" each appear in
`proposal_text.lower()` because of the literal word "bar"... wait,
actually the substring goes the OTHER way: `title_key in
proposal_text`. Still: any block whose title appears anywhere in
the proposal copy is included. A proposal that mentions "the park"
in the description (a totally normal sentence) would match a "Park
Walk" block on day 4 that has nothing to do with the swap.

This is "an apply that reports success but didn't mutate the right
thing" — the mutation is real, but it hits the wrong blocks. The
ledger `block_diffs` would still be honest, but the user reads the
proposal and sees a description that mentions "the park" as
background context, not as the swap target, and discovers later
that an unrelated block was rescheduled / re-titled.

**Repro / deterministic test idea:**
Seed an itinerary with two blocks: "Park Bar" on day 1, "Park
Walk" on day 4. Create a proposal:
- `title="Swap Park Bar for Lounge Bar"`
- `description="Better atmosphere; the park is too cold tonight"`
- `affected_block_ids=[stale_uuid_not_in_new_version]`

Apply it. Today: both "Park Bar" AND "Park Walk" get matched by
the fallback (`"park bar" in "swap park bar for lounge bar better
atmosphere; the park is too cold tonight"` → True; `"park walk"
in ...` → False, but `"the park"` substring math is fragile).
Even if the example doesn't trip, the *shape* is wrong — title
substring matching against the description is a class of bug.

**Suggested fix direction:**
Drop the title-match fallback entirely; if `affected_new_ids` is
empty after the position-map AND the proposal isn't `add`-type,
record `apply_status='failed'` with `apply_error='block_position_lost'`
and surface the existing "Needs organizer review" trust-loop banner.
The forward-chain in plan-state already handles open proposals
across forks correctly — the apply path doesn't need a fallback
for accepted proposals because by definition the apply runs
immediately after `db_resolve` and the position map should still
be valid.

If a fallback is truly needed for legacy proposals, restrict it
to **exact** title equality, not substring, and only when exactly
one block matches.

**Confidence:** Medium — I haven't observed a real misfire, but
the substring direction is reversed in a way that scales badly
with proposal description length.

---

### [P1] — Vote-loss race at the deadline between cron auto-resolve and a late vote

**References:**
- `Travel Agent/backend/core/db/change_proposals.py:197-232` (`vote_on_proposal` uses `SELECT FOR UPDATE` on the proposal row, and rejects votes when `row["status"] != "open"`)
- `Travel Agent/backend/core/db/change_proposals.py:215-218` (silent rejection: returns the existing proposal with no error)
- `Travel Agent/backend/concierge/proposal_automation.py:109-152` (cron path reads votes then resolves)
- `Travel Agent/backend/api/routes/proposals.py:237-316` (route returns the proposal after vote attempt; an aborted vote returns the resolved proposal indistinguishably from a successful vote against an open proposal)

**Why it matters to a real tester:**
The voting widget has a deadline. The cron loop
(`evaluate_and_resolve_proposals`) reads `_analyze_votes(proposal)`
then calls `_do_resolve` (which uses `db_resolve`'s
`WHERE status='open'` guard). Between the cron's
`_analyze_votes` and `_do_resolve`, the user can submit a final
"reject" vote that the cron didn't see. The user's vote
function acquires `SELECT FOR UPDATE`, sees `status='accepted'`,
silently rolls back, and returns `get_change_proposal(...)` — the
already-accepted proposal — with no error or warning.

The mobile client's optimistic update in
`ProposalReviewSheet.tsx:189-211` overwrites the cached proposal
with the optimistic vote, then on success invalidates the query
and re-fetches. The re-fetch returns `proposal.status=='accepted'`,
the optimistic vote is silently dropped (the user's vote isn't in
`proposal.votes` because the merge never committed), and the user
sees their vote "stuck" or invisible. They retry; same result. No
toast tells them the vote was rejected because the deadline
passed.

This is dogfood-blocking on any vote-driven decision: it punishes
exactly the user behavior the vote widget is designed to invite
(deliberate, last-minute consideration).

**Repro / deterministic test idea:**
Lazy-consensus proposal with a deadline 100ms in the future and
no votes. Concurrently trigger `evaluate_and_resolve_proposals`
and submit a `reject` vote. Assert: either the vote is counted
(and the resolution is "rejected"), or the API returns a 409 with
a "deadline passed" message — the silent drop currently observed
is the bug.

**Suggested fix direction:**
1. `vote_on_proposal` returns a sentinel (`None` for "row missing,
   404") and `("rejected", "proposal_already_resolved")` for the
   already-resolved case. The route translates this to HTTP 409
   with a clear `error_category`.
2. Frontend mutation handles the 409: roll back the optimistic
   update and toast "Voting closed — the proposal was resolved."
3. Optionally: the cron `_resolve_single_proposal` takes a
   `SELECT FOR UPDATE` on the proposal before computing votes, so
   the lock chain is consistent (vote waits for cron OR cron waits
   for vote — whoever holds the row decides).

**Confidence:** High on the silent-drop mechanism; Medium on the
fix surface (409 + UX copy is one cut, locking the cron is another).

---

### [P2] — Background auto-resolver `_do_resolve` skip-detection is wrong; reruns can re-apply the same proposal

**References:**
- `Travel Agent/backend/concierge/proposal_automation.py:292-312` (skip logic uses `result.auto_resolved` as the proxy for "we resolved it")

**Why it matters to a real tester:**
The skip path is:

```python
result = resolve_proposal(...)
if result and not result.auto_resolved:
    # "Someone else resolved it" → return False
    return False
```

This logic works when a *human* resolved first (the existing row
has `auto_resolved=False`), so the function correctly skips.
But if THIS background loop fired earlier with
`auto_resolved=True` (e.g. a missed cron tick, a doubled scheduler,
a restart-replay window), the existing row has `auto_resolved=True`,
the condition `not result.auto_resolved` is False, the function
does NOT skip, and proceeds to call `apply_accepted_proposal`
again. That re-fork-and-re-apply chain is the same as the
double-accept race above.

The DB-layer guard `WHERE status='open'` does prevent a second
*resolve*, so `db_resolve` returns the previously-resolved row
unchanged. But `_do_resolve` reads the unchanged row, fails to
notice "I didn't resolve this just now", and goes on to apply.

**Repro / deterministic test idea:**
1. Create an open proposal `P` with a past deadline.
2. Call `evaluate_and_resolve_proposals(trip_id)` once — `P`
   resolves and applies (`apply_status='succeeded'`, version N+1).
3. Call it AGAIN immediately. Today: it calls
   `apply_accepted_proposal` a second time and creates version N+2.
4. Assert: `len(get_itinerary_history(trip_id)) == initial+1`.

**Suggested fix direction:**
Replace the `auto_resolved` heuristic with a true "did this call
just transition the row" check. Either:
- Have `resolve_proposal` return a tuple `(proposal, was_updated:
  bool)` — `_do_resolve` uses `was_updated` directly.
- Or check `result.resolved_at` against a captured `now()` snapshot.
- Or, more cleanly, fold the apply step into the same DB
  transaction as the resolve (a single function "resolve and
  apply" that holds a row lock for the whole sequence).

Also pair with the apply-idempotency fix from the double-accept
finding above.

**Confidence:** Medium — requires a doubled cron tick or
proactive trigger to fire; haven't observed in production but
verified the logic is wrong.

---

### [P2] — Diff-safe revert can DELETE an `add`-proposal block that members later annotated

**References:**
- `Travel Agent/backend/core/db/proposal_apply.py:756-782` (delete safety check is `if status == "tentative" and not booking_ref:` then `_delete_block`)
- `Travel Agent/backend/core/db/proposal_apply.py:668-676` (raw `_delete_block` — no cascade check on participants/notes/etc.)

**Why it matters to a real tester:**
The block created by an `add`-proposal starts at `status='tentative'`
with `booking_ref=None`. If a member adds notes ("Let's bring
Maya"), tags participants, or edits the title (without booking),
the safety check still passes and the block is deleted on revert.
Member work silently vanishes — exactly the "a conflict path that
loses a user's change" failure mode the audit prompt named.

The diff-safe revert for modify/swap/reschedule on EXISTING blocks
correctly checks per-field divergence. The `add`-revert path uses
a much coarser safety net.

**Repro / deterministic test idea:**
1. Agent proposes `add` for a new dinner block → accepted → applied.
2. Member edits the new block: `update_block(block_id, notes="reservation under Pat")`.
3. Organizer reverts. Assert: block is NOT deleted (member's edit
   should turn it into a conflict). Today: block is silently
   deleted.

**Suggested fix direction:**
Compare current `updated_at` against the proposal's
`resolved_at` (or against the `proposal_applied` event's
`created_at`). If `updated_at > applied_at`, treat the added block
as a conflict — keep it, list it in `field_conflicts` as
`{block_id}:added_block_edited_since`, return
`mode='diff_safe_partial'`. The version-restore fallback can then
do the destructive cleanup if the user truly wants it.

**Confidence:** Medium — requires a member to edit an
agent-created block, which is plausible but not the default flow.

---

### [P2] — `BlockChangedBanner` shows Undo for any change with a `proposal` source, including rejected/reverted/failed proposals → 409 on tap

**References:**
- `Travel App/components/trip-plan/BlockChangedBanner.tsx:45` (`const hasProposal = change.source?.kind === 'proposal' && change.source.id;` — no filter on `change.type`)
- `Travel App/components/trip-plan/ChangeTimelineRow.tsx:71` (`canUndo = change.type === 'proposal_accepted'` — correct filter, but only used on Changes screen)
- `Travel Agent/backend/api/routes/proposals.py:489-493` (route returns 409 for non-accepted proposals)
- Compounds with **P0-1** above: since revert never flips status, even reverted-blocks keep showing the Undo affordance forever.

**Why it matters to a real tester:**
The Plan tab and the Changes tab disagree on which proposals offer
Undo. A rejected swap proposal generates a `proposal_rejected` row
in `recent_changes`; on Plan tab, the corresponding block still
gets a "Vesper changed this · View diff · Undo" banner. Tapping
Undo throws a 409 ("only accepted proposals can be reverted") and
the user sees the generic "Couldn't revert change. Try again?"
toast (`plan.tsx:91-94`). No information about *why*.

For `proposal_apply_failed` the situation is worse — the banner
implies a change happened and offers Undo, but in fact nothing
mutated and the proposal is in a "needs organizer review" state.

Plan tab and Changes tab should behave identically.

**Repro / deterministic test idea:**
1. Create a swap proposal against block `B1`. Reject it.
2. Open `/trips/{tripId}/plan`. Block `B1` shows
   "Vesper changed this · View diff · Undo".
3. Tap Undo → 409 error → vague toast.
4. Assert: the Undo button should not have rendered.

**Suggested fix direction:**
Mirror the `ChangeTimelineRow` filter:
```ts
const canUndo = change.type === 'proposal_accepted' && proposalId != null;
```
And don't render the banner at all for `proposal_rejected` /
`proposal_apply_failed` / `proposal_reverted` if it's not adding
information beyond what the Plan Change Strip already covers — for
those, the strip is the right surface.

**Confidence:** High.

---

### [P2] — `revert_conflicts` payload uses `block_id:field` strings instead of structured records; the conflict sheet shows raw UUIDs to the user

**References:**
- `Travel Agent/backend/core/db/proposal_apply.py:732-754` (`field_conflicts.append(f"{block_id_str}:{field}")`)
- `Travel App/components/trip-plan/RevertConflictSheet.tsx:69-80` (renders each conflict string verbatim)

**Why it matters to a real tester:**
The conflict list rendered in `RevertConflictSheet` shows literal
strings like
`"a8f1c2e3-...-...:title, a8f1c2e3-...-...:notes, ..."`. To a non-
technical tester, this is unintelligible — the very moment they
need clarity about *which* later change they're being asked to
override, the UI hands them raw UUIDs. The sheet then asks them
to make a destructive decision based on that text.

**Repro / deterministic test idea:**
Trigger a `diff_safe_partial` revert. Open the conflict sheet.
Assert the rendered text refers to block titles ("Dinner at
Belcanto: title kept" or similar), not raw IDs.

**Suggested fix direction:**
Change the ledger payload shape (additive — keep `field_conflicts`
for backwards-compat, add a new `field_conflicts_detail: list[{block_id,
block_title, field, current_value, kept_reason}]`). The frontend
renders `block_title · field` instead of the UUID string. Backend
fetches `block.title` while writing the conflict record (already
loaded via `_fetch_block_fields`).

**Confidence:** High on the UX gap; the rendering literally passes
the string straight through.

---

## TECH-DEBT

### Tests over-mock the proposal-resolution DB layer, hiding real failures

**References:**
- `Travel Agent/tests/api/test_proposals_api.py:671-869` (every revert test patches `backend.core.db.change_proposals.resolve_proposal` and `revert_accepted_proposal_v2`)
- `Travel Agent/tests/api/test_proposal_apply.py:9-15` (apply tests patch every collaborator including `get_full_itinerary`, `create_block`, `merge_proposal_metadata`)

**Why it matters:**
The P0 revert bug (status never flips to `withdrawn`) and the
P1 double-accept bug are both invisible to CI because no test
exercises the real `db_resolve` against a Postgres row whose
status is `accepted`. The test suite proves "the route passes its
mocked collaborators the right arguments" but not "the data layer
actually transitions state." The `tests/api/test_plan_state.py`
suite does seed `ChangeProposal` instances directly with
`status='withdrawn'` + `was_reverted=True` — which gives a false
sense of coverage because the only way to reach that state in
production is via the broken `db_resolve` call.

**Suggested fix direction:**
Add `@requires_postgres` end-to-end tests for the resolve+apply+
revert chain that exercise the real DB. Keep the mocked unit tests
for input validation / authz logic; move the state-transition
contract to integration tests.

---

### `proposal_applied` ledger event isn't surfaced anywhere structured for clients

**References:**
- `Travel Agent/backend/core/db/plan_events.py:115-136` (`get_events_for_source`)
- `Travel Agent/backend/api/routes/proposals.py:587-638` (`_to_detail` doesn't include any ledger payload)

**Why it matters:**
The ledger holds the authoritative `block_diffs` and `applied_block_map`
but no API exposes them. The `ProposalDetail` response leaks selected
fields (`apply_status`, `revert_mode`, `revert_conflicts`) but the
diffs themselves — the most valuable artifact for debugging trust
issues — are server-only. Until those are exposed, the diff drift
(P1-5) can't be fixed cleanly on the client.

**Suggested fix direction:**
Add `applied_diff: list[BlockDiff] | None = None` to
`ProposalDetail`; populate it from `get_events_for_source` for
`apply_status='succeeded'` proposals. Or expose a
`GET /api/trips/{trip}/plan-events?source_type=proposal&source_id=…`
endpoint for the broader ledger.

---

### `recent_changes` and block decoration are 72h hardcoded; long-trip dogfood will hit the edge

**References:**
- `Travel Agent/backend/core/db/plan_state.py:53` (`RECENT_CHANGE_WINDOW = timedelta(hours=72)`)
- `Travel Agent/backend/core/db/plan_state.py:514-515` (cap at 50 rows after the window filter)

**Why it matters:**
A dogfood trip lasting more than 3 days will silently lose
visibility into proposals from before the window. The Changes
screen ("a timeline of what the agent did") will be empty for
older churn even though the data exists in the ledger. The cap
at 50 protects against unbounded responses but isn't surfaced to
the client as `has_more`.

**Suggested fix direction:**
Parameterize the window on the request (e.g. `?since=…`); add a
`has_more` flag when truncating; on the Changes screen offer a
"Load older" affordance backed by the ledger directly.

---

## Known / Accepted

These are confirmed deferred-by-design from the Known Gaps Register
and CLAUDE notes — flagged here so they aren't re-litigated:

- **O-9 — Tier 3 eval mocks DB writes including `propose_change`** (Known
  Gaps Register). The eval suite doesn't regression-gate the
  proposal-persistence layer. Out of scope for this audit; the
  bugs above sit BELOW the eval seam in the real DB code.
- **Concurrency on `vote_on_proposal` (B8 audit)** — addressed by
  `SELECT FOR UPDATE` (`change_proposals.py:197-232`); not a new
  finding. The deadline race in P1-7 is a different surface
  (vote vs cron, not vote vs vote).
- **Idempotency-key check on `/vote` and `/resolve`** — present but
  optional, by design. The mobile client doesn't currently send it
  (see double-accept finding); recommending to make it automatic
  rather than mandatory.
- **`auto_approve`'s `_do_resolve` chain is intentional** — the
  agent is *allowed* to auto-act on low-stakes changes; the gap
  flagged in P0-3 is that delegation preferences should override
  this, not that the path itself shouldn't exist.
- **`compose_revert_receipt` covers all three modes** (verified at
  `tests/concierge/test_receipt_composer.py:173-211`). Receipt
  copy is honest; the gap is the upstream `status` bug, not the
  composer.
- **TR-1 / G-10 / O-13** etc. — unrelated subsystems flagged in
  the Known Gaps Register; out of scope.
