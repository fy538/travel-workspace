# Proposals / Change Studio — System Charter

> Surface: Trips
> Maturity (for MVP): MVP-required
> Status: wired (the central Advise→Propose→Act loop; a known drift hotspot)
> Last updated: 2026-06-27

## Purpose
The controlled mutation gateway for a trip plan — the two ways the itinerary changes:
(A) an exact **proposal** resolved by the named decision owner (or by an explicitly
enabled vote), and (B) a **direct edit** by an authorized actor — each producing a
visible receipt with only server-proven recovery actions. Serves belief #9
(planning and experiencing are one continuous activity) and the trust loop.

## Spans (cross-repo)
- Backend: `api/routes/proposals.py`, `plan_edit_preview.py`, `plan_edit_commit.py`, `plan_mark_happened.py`, `plan_state.py`; `core/db/change_proposals.py::build_and_persist_proposal`, `core/db/plan_events.py` (append-only ledger), `core/edit_policy.py` (`resolve_edit_mode_for_trip`), the conflict engine, `concierge/tool_handlers/planning/_propose_present.py`.
- Frontend: `app/trip-proposal/[proposalId]`, `(tabs)/trips/[tripId]/changes`, Change Studio sheets on Plan rows, Now Mode, `components/plan/*`, `data/proposals.ts`.
- Tables of record: `change_proposals` (+ votes), `plan_events` (append-only ledger).

## Public interface (what other systems may call / read)
- **Proposal lifecycle:** `GET /api/trips/{trip_id}/proposals`, `GET /api/trips/{trip_id}/proposals/{proposal_id}`, `POST /api/trips/{trip_id}/proposals/{proposal_id}/vote`, and canonical mobile `POST /api/trips/{trip_id}/proposals/{proposal_id}/resolve`.
- **Retired split authority:** `/api/trips/{trip_id}/itinerary/operations/proposals/{proposal_id}/accept` and `/apply` are not public lifecycle steps. They had no adopted consumer and must remain absent from OpenAPI; proposal resolution and application are one server-owned canonical resolve flow.
- **Direct edit:** `POST /plan/edit-preview` → returns an `idempotency_token`; `POST /plan/edit-commit` (replays the token) → `direct` (atomic write + ledger entry) or `propose` (creates a proposal, no mutation until accepted), chosen by `edit_policy`. `POST /plan/mark-happened`.
- **Inbound:** Concierge creates proposals **only** via the shared `build_and_persist_proposal` (chat-created proposals must not bypass it).
- **Consumes:** Planning/Itinerary (the blocks it mutates), Group/Social (edit-mode/role), Places (conflict: closed-hours).

## Owns (source of truth)
The proposal lifecycle and the **`plan_events` append-only ledger** (the before/after
that makes Undo/revert truthful). The itinerary blocks themselves are owned by
Planning/Itinerary — this system is their only sanctioned mutation path.

## Invariants (must always be true)
*(These are journey 05's "Must Never Happen", inverted.)*

These are accepted target invariants. Current implementation satisfies them
path-by-path, not universally: direct future-unbooked Remove has atomic
fault-injection proof; proposal apply, ordinary Add/Move/Replace, Optimize,
Replan, provider sagas, proposal creation convergence, and canonical receipts
remain migration/evidence work. No client may promise a target invariant merely
because it is listed here.
- **Every accepted change emits a visible receipt** — no silent mutation.
- **Rejected proposal confirms the original remains** — it never just disappears.
- **Optimistic concurrency:** commit must surface conflict or a stale `expected_updated_at` rather than clobber.
- **Idempotency:** the preview `idempotency_token` is replayed (5-min TTL); retries never create duplicate votes or duplicate applied changes.
- **Revert truthfulness:** if revert says success, Plan **and** Map reflect it (no ghost state) — the ledger makes this deterministic and diff-safe.
- **No private source leak:** proposal detail shows a public-safe reason; never the private constraint behind it.
- **One creation path:** chat-created and UI-created proposals both go through `build_and_persist_proposal`.
- **No silent voting:** voting is explicit trip/action policy; adding a member
  never enables it and silence never counts as consent.
- **Frozen authorship, current safety:** a submitted proposal's normalized
  operation and attribution are immutable, while acceptance revalidates current
  authority, protection/provider state, trip phase, and preconditions.
- **Receipts separate public reason from private influence:** group-visible copy may
  explain the decision but must never identify who supplied a private constraint.
- **Receipts carry stable source references:** the visible result must be traceable
  to proposal, plan-event, or provider identifiers without exposing raw prompts.
- **Correction propagates:** reverting or disputing the source invalidates every
  derived receipt/read model; a green toast over stale state is a contract failure.

## Failure modes
- Commit conflict / stale timestamp → 409-style surface to the UI (recovery banner), never a silent overwrite.
- Target: source-system error before a structural commit rolls back mutation and
  canonical operation evidence together. Current ordinary writers and proposal
  compensation do not yet prove this universally.

## Maturity & validation
- Serves journey: 05 (Track A proposal loop + Track B direct edit).
- DoD state: backend proposal/apply + idempotency tests ✅ · canary passes ✅ · **mock-walk ❌ · on-device Maestro ❌ · live group walk ❌**.
- Conflict engine: closed-hours type + soft-conflict "keep as is" shipped; scan TTL-cached.

## Canonical docs
- why → `product/Interaction Design and Social Dynamics.md` · how → `architecture/Trip State Architecture.md` · `architecture/deck-faces/Card-Deck-Action-Audit-2026-06.md` · what(fe) → `page-specs/change-proposals.md`.
- Tests: `tests/api/test_proposals*`, `__tests__/data/proposals.test.ts`, `__tests__/components/plan/ProposalReviewSheet.test.tsx`.

## Cross-cutting constraints
- **Graph legibility**: proposal rationale that cites taste history must follow [graph-legibility-doctrine.md](graph-legibility-doctrine.md) — reveal on tap ("Why this?") only, never by default in the proposal card.

## Open risks / known gaps
- This is the **#1 named drift hotspot** for the wedge ("real acceptance/apply behavior is a known drift hotspot"). The revert-truthfulness and cross-surface-coherence invariants must be proven by a live walk + a Journey-06 parity pass after every mutation.
- Two edit-preview implementations were reconciled into one spine (06-19) — verify nothing still calls the retired path.
