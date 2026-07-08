# Code Alignment — Batch G Backend: Stay-Vote Blocking · Nudge Endpoint · Masked Expenses (2026-07-06)

Repo: `~/travel-workspace/travel-agent` (Python / FastAPI / SQLAlchemy / Alembic). These are the three backend-gated items surfaced by the G1/G2 frontend audits — the FE renderers/affordances are prepped and dormant, waiting on these schema/endpoint changes. Land these **ahead of** the FE tasks that consume them (G1-5, G2-4, G2-5).

Standing rules: branch from main · mypy 0 + tests green · **import-test every touched module + scan for untracked `.py` before any deploy** (per the 2026-06-15 prod incident) · Alembic migration only where a real column is added (Task 3) · one commit per task · no push/deploy without approval.

Priority order: **Task 1 (blocking) + Task 2 (nudge) are wedge-relevant — do now.** Task 3 (masked) is deferred per adjudication B — include only if capacity allows, otherwise ticket and skip.

---

## Task 1 — Stay-vote `blocking` phase + holdout identity (NO migration — pure read-model logic)
The FE needs a `'blocking'` vote phase (one holdout preventing consensus) and the holdout's identity. All required data is already computed in `resolve_stay_vote`.

**File:** `backend/core/models/trip_stay_candidates.py`
1. **Enum** (line 22): `StayVotePhase = Literal["not_started", "open", "tie", "decided"]` → add `"blocking"`. This is a Python `Literal`, not a DB enum — **no migration**.
2. **Read model** `StayVoteState` (lines 95-109): add `blocking_member_ids: list[UUID] = Field(default_factory=list)`.
3. **Phase logic** `resolve_stay_vote` (lines 147-163): between the `decided` and `tie` branches, detect the blocking case. The data is already local: `tallies` (sorted desc, each with `voter_ids`), `total_voters`, `missing_voter_ids`, `everyone_voted`.
   - Blocking condition (recommended): `everyone_voted == True` AND the top candidate's `count == total_voters - 1` AND it's a single leader (would win outright if the one dissenter switched). The holdout = the voter(s) not in `tallies[0].voter_ids`. Populate `blocking_member_ids` with them.
   - Keep `tie` for the genuine multi-way-tied case (≥2 leaders at max). `blocking` is specifically "one person from consensus," which is the actionable "nudge them" state — that's why canon separates it.
   - Decide and **document in a comment** the boundary between `blocking` and `open` for larger groups (e.g. is "2 short of majority" blocking or still open? recommend: blocking only when exactly 1 vote from a locked majority, else `open`).

**FE consumer:** `StayDecisionResponse.vote` (`backend/api/routes/stay_candidates.py:85-92`) already serializes `StayVoteState` — no route change needed; the new field flows automatically. Mirror the FE type (`travel-app/utils/api/types.ts:1491`) in the same PR or flag it for the G1-5 implementer.

## Task 2 — Nudge endpoint (new route; reuse deterministic notification path, NOT the triage arbiter)
A user-initiated nudge is deterministic — it must **not** go through the Tier-2 Haiku triage/arbiter (that's for the proactive engine deciding what to send). Reuse the leave-by-style direct path: gate → create notification → push → mint outcome row.

**New route:** `POST /api/trips/{trip_id}/nudge` (put it in `backend/api/routes/trips.py` or a new `nudges.py`, following the router conventions at `expenses.py:121`).
- **Body:** `target_user_ids: list[UUID]`, `reason: Literal["stay_vote", "settle_up"]`, optional `reference_id` (candidate_id or expense/settlement context).
- **Auth:** `require_trip_member(trip_id, actor)` for send-rights. Both reasons are member-initiated (anyone owed can nudge a debtor; anyone can nudge a stay-vote holdout) — do NOT gate to organizer.
- **Reuse:**
  - `create_notification()` (`backend/concierge/structured_messages.py:222-257`) for the in-app message — author the copy per reason ("Ana nudged you — the group's waiting on your vote for where to stay" / "Ana sent a reminder about settling up").
  - `_check_user_push_gates()` (`backend/notifications/push.py:52-110`) before pushing — respect `pause_all`/`quiet_hours`/`allow_push`.
  - Mint an outcome row (`backend/core/db/notification_outcomes.py`) so nudges are tracked like every other send.
- **Taxonomy:** add `VOTE_NUDGE` and `SETTLE_NUDGE` to `CandidateType` (`backend/notifications/arbiter.py:42-70`). Verify the arbiter/triage don't choke on types they never rank (these bypass triage — confirm the enum addition alone doesn't break arbiter weight lookups; add weights if the arbiter requires an entry for every member).
- **Abuse floor (required):** enforce a per-(actor, target, reason) cooldown so a holdout can't be nudged repeatedly — reuse the gates/cadence infra (`run_all_gates` or a simple interval check). Recommend ≥ a few hours between nudges to the same person for the same reason. Return a clear "already nudged recently" response rather than silently sending.

**FE consumers:** G2-4 (cost-settle nudge, `travel-app app/trip-expenses/index.tsx:188`) and G1-5 (stay-vote "Nudge {name}", `StayCompare.tsx`). One endpoint serves both.

## Task 3 — Expense `masked` field [DEFERRED per adjudication B — include only if capacity allows]
A masked expense = a surprise/gift whose amount is hidden from the group. **Requires an Alembic migration** (new column) — handle with migration discipline (the prod incident memory: migrations run even on failed deploys; blue-green).

**Semantics call first (recommend, then confirm):** masked = **payer covers it fully, amount hidden from other members, excluded from their balances.** (The alternative — amount hidden but others still owe an unknown share — is nonsensical UX; don't build it.) So masked expenses drop out of the settlement graph for everyone except the payer.

1. **Column:** add `masked: bool` (default `False`) to the expenses table (`backend/core/db/_tables/expenses.py:70-126`) + Alembic migration. Mirror the existing `trip_photos.visibility` privacy precedent for naming/constraint style if a richer visibility enum is preferred over a bare bool (recommend bare bool — masked is binary).
2. **Models:** add `masked: bool = False` to `Expense` (`backend/core/models/expenses.py:41-62`), `ExpenseCreate` (65-79), `ExpenseUpdate` (82-92).
3. **Endpoints:** thread the flag through create (`routes/expenses.py:121-195`) and update (292-344).
4. **Settlement exclusion (the load-bearing part):** in `compute_settlement` (`backend/expenses/settlement.py:84-103`), filter masked expenses' shares out of every non-payer's balance so hidden amounts never leak via a computed balance or transfer instruction. Verify the settlement fetch query (`backend/core/db/expenses.py:949-1024`) carries the `masked` flag so the filter has it. Add a test proving a masked expense is invisible in a non-payer's `BalanceSummary` and `SettlementTransfer`.
5. **Response privacy:** confirm the expense list/detail endpoints don't return the masked amount to non-payer members (per-viewer filtering or amount-nulling). A masked expense that hides from balances but shows its amount in the ledger defeats the purpose.

## Done
`blocking` phase + `blocking_member_ids` computed and serialized (no migration; FE type mirrored/flagged) · `POST /nudge` endpoint live, deterministic path, both reasons, cooldown enforced, outcome rows minted · [if included] `masked` column migrated + threaded + excluded from others' settlement with a test proving no leak · report any FE type mirrors the app repo still needs (StayVotePhase `blocking`, nudge request/response shape, expense `masked`) so G1/G2 implementers wire against the real contract.
