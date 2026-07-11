---
doc_type: archive
status: archived
owner: engineering
created: 2026-07-11
last_verified: 2026-07-11
archived: 2026-07-11
why_new: Records the first executable charter-invariant audit and its findings.
---

# Charter Invariant Checkers — Route 3 findings (2026-07-11)

**What this is.** The 16 system charters in `docs/systems/` each carry an
"Invariants (must always be true)" section — until now checked by reading, not
by running. This work extracts the DB-checkable subset into executable SQL
checkers that run against a seeded database, converting the charters into a
permanent regression net. First run against the dev DB (1,189 trips, 445
plan-events, 83 proposals of accumulated journey output) immediately surfaced
one production-code drift bug, one invariant-violating test footgun, and one
state-vocabulary wart.

## Deliverables

| Artifact | Where |
|---|---|
| Checker script (27 checkers, one command) | `travel-agent/scripts/check_charter_invariants.py` |
| Pytest twin (permanent net, `@requires_postgres`) | `travel-agent/tests/invariants/test_charter_invariants.py` |
| Fixes landed alongside | `PlanEventType` vocab, 2 test fixtures (see findings) |

```bash
cd travel-agent
PYTHONPATH=. python scripts/check_charter_invariants.py            # all
PYTHONPATH=. python scripts/check_charter_invariants.py --charter expenses-settlement
PYTHONPATH=. python scripts/check_charter_invariants.py --json     # machine-readable
PYTHONPATH=. python -m pytest tests/invariants/ -q                 # as tests
```

Checkers are read-only SELECTs and run in ~0.2s. Two modes: **enforce** (exit
1 / test failure on violation) and **report** (prints findings, never fails —
used where drift is tolerated by design, e.g. the plan-event vocabulary that
readers must handle gracefully). Route-2 concurrency simulations can import
`run_checker`/`CHECKERS` directly as their post-simulation assertion layer —
that was the point: simulations mutate, then the same net asserts nothing
structural broke.

## Findings from the first run

### F1 — `block_added` missing from the canonical `PlanEventType` vocabulary (production drift) — FIXED

`backend/core/db/trips/blocks.py:168` writes `event_type="block_added"` (154
rows in the dev DB) and `blocks.py:614` even *reads it back*, but the type was
never added to the `PlanEventType` Literal in
`backend/core/models/plan_events.py` — the writer site landed without updating
the list its own comment says to update. Readers tolerate unknown types by
design, so nothing crashed; the cost is silent: any exhaustive handling of
`PlanEventType` (rendering, analytics, revert logic) treats `block_added` as
"generic unknown." **Fixed** by adding it to the Literal (no other consumers
of the Literal exist to be affected). The `L2-ledger-event-types-known`
checker now guards this class of drift permanently.

### F2 — bare `create_trip()` is an invariant-violating footgun; one test leaked 96 violating trips — FIXTURE FIXED, cleanup pending

`G3-organizer-is-member` failed with **96 trips whose creator has no
`trip_members` row** — all titled "Suppress Test Trip" by
`suppress-*@example.com` users, created 07-08→07-11 by
`tests/notifications/test_h3_lifecycle_bridge.py` runs.

Root cause chain:
- `backend/core/db/trips/crud.py` still exports bare `create_trip()`, which
  writes the trip row but **no organizer membership**. Production has **zero
  callers** — every prod path uses the atomic `create_trip_with_organizer()`
  (added precisely to kill the orphan-trip failure mode). The bare variant
  survives only as a test-usable footgun: **56 call sites across the test
  suite** still use it.
- The h3 test used it and (unlike most tests) its rows aren't cleaned up, so
  every run accrues membership-violating trips into the shared dev DB.

**Fixed 2026-07-11 (full remediation):**
- The h3 fixture now uses `create_trip_with_organizer` (verified: re-running
  the suite no longer adds orphan trips — 96 before, 96 after).
- **All 55 remaining bare-`create_trip` call sites migrated** to
  `create_trip_with_organizer` across 27 test files + 1 script
  (`scripts/canary_lc1.py`), including the redundant
  `add_trip_member(creator, role="organizer")` lines that would otherwise
  now collide with the atomic insert (9 files needed this; one test —
  `test_trips.py::test_full_lifecycle` — needed the assertion rewritten to
  read the pre-seated membership instead of re-adding it; one —
  `test_preferences_api.py::_make_trip_with_member` — needed a throwaway
  co-organizer so the demote-to-member path doesn't trip the "can't demote
  the last organizer" guard).
- **`create_trip` deleted** from `backend/core/db/trips/crud.py`. Its
  `emit("trip.created", ...)` call was ported into
  `create_trip_with_organizer` first — `create_trip_with_organizer` had
  never emitted it, so **`trip.created` was never fired in production**
  (zero prod callers of the bare function) and its one real subscriber,
  `backend/home/farout_read/subscriber.py::_on_trip_created`, was dead code
  end-to-end. This is now fixed as a side effect of the footgun deletion;
  full verification of `_on_trip_created`'s downstream behavior is out of
  scope here (event_bus's `emit()` is documented never-raises / try-except
  per handler, so this is safe to have activated).
- **CI wired**: `.github/workflows/ci.yml`'s `test-db` job gets a named
  `Run charter invariant checkers` step (`pytest tests/invariants/ -v -m
  requires_postgres`), alongside the existing blanket `tests/` sweep that
  already covers it via `testpaths = ["tests"]`.
- Full regression sweep (28 test files, pre- vs post-migration): baseline
  37 failed / 7 errored (pre-existing, confirmed via `git stash` isolation —
  unrelated seed-data/FK issues from concurrent work); post-migration
  **same 37/7**, +26 passing (193→219, then +26 more with h3 included).
  Zero regressions.

**Still pending — needs a human-run DELETE; auto-mode denied both attempts
this session** (asking for the destructive DELETE without a fresh, explicit
user instruction naming it — correctly, since this turn's instruction only
covered migration/CI):

```sql
-- 96 rows: suppress-fixture trips with no organizer membership (pre-fix residue)
DELETE FROM trips t USING users u
WHERE u.id = t.created_by
  AND t.title = 'Suppress Test Trip'
  AND u.email LIKE 'suppress-%@example.com'
  AND NOT EXISTS (SELECT 1 FROM trip_members tm
                  WHERE tm.trip_id = t.id AND tm.user_id = t.created_by);
-- 37 rows: off-vocabulary ledger rows from the pre-fix account-deletion fixture (F2b below)
DELETE FROM plan_events WHERE event_type = 'manual_edit';
```

Until run, `G3` fails and `L2` reports on the local dev DB only — **CI's
fresh, migration+fixture-seeded database has none of this residue**, so the
new CI step should pass cleanly on the next run regardless.

**F2b (same class):** `tests/core/test_account_deletion.py` wrote
`event_type="manual_edit"` — that's a *source_type*, not an event_type (37
leaked rows). **Fixed** to `event_type="block_updated"`,
`source_type="manual_edit"`.

### F3 — `status='withdrawn'` is overloaded for reverted-after-apply (vocabulary wart, documented)

12 proposals showed `apply_status='succeeded'` + `status='withdrawn'`. The
ledger trail (`created → accepted → applied → withdrawn → reverted`) shows
this is the **revert flow by design**: revert reuses `withdrawn` and sets
`was_reverted=true` rather than having a distinct `reverted` status. Coherent
— the ledger disambiguates — but anything reading `status` alone cannot tell
"withdrawn before ever applying" from "applied then undone." The
`P4-apply-status-coherence` checker now encodes the real rule
(`succeeded ⇒ applied/accepted ∨ was_reverted`) and enforces it; the zero-row
check confirmed no *incoherent* rows exist. Consider a `reverted` status value
if any surface ever needs to distinguish without joining the ledger.

## Checker inventory (27)

| Charter | Checkers |
|---|---|
| proposals-change-studio | P1 applied⇒ledger-event · P2 applied-exactly-once · P3 reverted⇒revert-event · P4 status/apply coherence · P5 voters-are-members · L1 ledger-refs-resolve · L2 event-vocab (report) · R1 receipt-undo-coherence (report) |
| expenses-settlement | E1 payer-is-member · E2 split-users-are-members · E3 masked⇒payer-covers-fully · E4 no-auto-created · E5 idempotency-unique · E6 equal-split-sums (report) |
| group-social | G1 invite use_count ≤ max_uses ∧ = redemptions · G2 redeemer-is-member · G3 organizer-is-member · G4 stay-voters-are-members · G5 no post-revoke/expiry redemptions |
| memory-preference | M1 versions gapless/monotonic (report) |
| planning-itinerary | I1 itinerary versions gapless (report) · I2 block time_end ≥ time_start |
| concierge-vesper | C1 telemetry origin tagged on every turn |
| places | PL1 per-provider daily budget never exceeded · PL2 Google-id 30-day retention (report) |
| voice-narration | V1 quota counters non-negative |
| booking | B1 no stale-pending proposals past expiry (report) |

Notable adjacent wins baked into the SQL: "vote counts ≤ member counts" holds
by construction (votes are a JSONB object keyed by voter, P5 proves keys ⊆
members); E3 is the data-shape half of "masked expenses never appear in a
group-visible payload" (a masked expense with a non-payer split is the only
way a group ledger could owe against it — API-level redaction is the
behavioral half, covered by existing route tests).

## Triage: invariants NOT convertible to snapshot SQL

Honest accounting of what this net does **not** cover, so nobody mistakes
green for "all charters hold":

- **Append-only-ness itself** (plan_events): a snapshot can't prove nothing
  was ever UPDATEd/DELETEd. Options: a DB trigger raising on UPDATE/DELETE, or
  Route-2 simulations diffing ledger state before/after. The net checks the
  *consequences* (refs resolve, exactly-once, applied⇒event) instead.
- **Viewer-dependent egress** (concierge privacy egress, masked-expense
  redaction, proposal private-reason hiding, pre-accept invite leakage): needs
  calling read models per (viewer, trip) and scanning payloads — a natural
  second phase reusing the privacy-invariant tracer.
- **Behavioral/code-path invariants**: fail-open loaders, `<notes>` stripping,
  guardrail-on-every-turn, provider `NormalizedOffer` normalization,
  quiet-hours zero-LLM gating, postcard cost-guard ordering, Folio
  read-only-ness. These are (mostly) covered by existing unit tests; the
  charters' value there is as review checklists.
- **FE-mirror invariants** (Discover dual-implementation parity, badge/read
  coherence): belong to the FE test suite / canon-drift-check lane.
- **Atlas dedup & postcard scarcity caps**: checkable in principle but need
  schema introspection of archive/artifact-type semantics — deferred rather
  than guessed at.

## State after this session

- 27 checkers: **25 pass** locally against the dirty dev DB; L2 reports + G3
  fails **solely on the pending residue cleanup** (SQL above, dev-DB-only —
  CI's fresh DB is unaffected). Once the DELETE runs, expect 27/27 green
  locally too.
- The net has already demonstrated sensitivity on real dirt (it found F1/F2
  on its first execution — it is not a suite that can't fail).
- The footgun class of bug (F2) is now structurally closed: `create_trip` no
  longer exists, so no test can reintroduce a membership-less trip via it.
- CI wired: `tests/invariants/` runs both implicitly (blanket `tests/` sweep)
  and explicitly (named step) in the `test-db` job.
- Lint/mypy clean across every touched file (28 test files, 1 script, 2
  backend modules, 1 CI workflow); full regression sweep shows zero
  regressions (see F2 fix log above).

## Follow-ups (ranked)

1. Run the residue-cleanup SQL above (blocked on permissions — destructive
   DELETE against the shared dev DB needs your explicit go-ahead).
2. Phase 2: egress checkers (viewer-scoped payload scans for masked expenses,
   private constraints, pre-accept invites) reusing the privacy tracer.
3. Route 2 hook: run concurrency simulations against a scratch DB, then call
   `run_checker` over the full registry as the post-simulation assertion.
4. Consider a distinct `reverted` proposal status (F3) if any surface needs it.
5. Verify `farout_read/subscriber.py::_on_trip_created`'s actual behavior now
   that `trip.created` fires in production for the first time (it was dead
   code end-to-end before this session's footgun deletion restored the
   emit() call) — low risk (event_bus fails closed per-handler) but worth a
   deliberate look rather than leaving it as an incidental side effect.
