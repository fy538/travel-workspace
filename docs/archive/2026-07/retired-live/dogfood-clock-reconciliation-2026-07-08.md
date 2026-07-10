---
doc_type: archive
status: archived
owner: founder / engineering
created: 2026-07-09
archived: 2026-07-09
why_new: Move reviewed completed evidence out of the living documentation tree without deleting its historical record.
---

# Dogfood Clock Reconciliation

> Archived from the living documentation tree on 2026-07-09 during Phase 5 cleanup.

> Status: FIXED 2026-07-08 — all 4 steps executed and verified (BE + FE agree)
> Owner: founder / engineering
> Created: 2026-07-08
> Relates to: [Persona cast consolidation](persona-cast-consolidation-2026-07-08.md) —
> this is the "3 clocks + date drift" hazard flagged in the dogfood-world audit,
> investigated concretely before the two-device wedge walk.

## Corrected diagnosis

The prior audit named this "3 clocks that need reconciling." Code investigation
shows something more specific and cheaper to fix: **a reconciliation mechanism
already exists — `backend/core/dogfood_dates.py` — built for exactly this
problem, but it is incompletely wired and not populated on the seeded wedge
trip.** This is a wiring gap, not a missing design.

```python
# backend/core/dogfood_dates.py
"""Canonical dogfood manifests can pin display time with
``trip_summary.dogfood_today`` so local/EAS QA keeps authored trips in the
intended product phase even after the real calendar moves on."""

def dogfood_today_override(trip: Any) -> date | None: ...
def is_dogfood_authored_trip(trip: Any) -> bool: ...
```

That is precisely a per-trip, backend-authoritative "pin the display date"
mechanism — the right shape of fix. It's just not finished.

## The four sources of truth (not three)

| # | Source | Mechanism | Reads |
|---|---|---|---|
| 1 | **FE dev time-travel clock** | `travel-app/utils/now.ts:20-48` — module var `_overrideMs`, persisted to AsyncStorage (`dev.mockNowMs`) | Global, per-device, manual |
| 2 | **FE trip-phase computation** | `travel-app/utils/helpers.ts:34-104` `computeTripPhase()` via `todayIsoLocal(date = now())` | Clock #1 |
| 3 | **Backend trip-phase computation** | `backend/core/trip_phase.py:26-89` `compute_trip_phase()` — `today = datetime.now(tz or _UTC).date()` | Real wall clock. **No override param.** Feeds voice quotas, notification triage, lifecycle (per its own docstring) |
| 4 | **Backend dogfood override** | `backend/core/dogfood_dates.py` `dogfood_today_override(trip)` reads `trip_summary.dogfood_today` | Per-trip authored field. **Wired into only 3 of the relevant consumers** (`trip_note.py`, `concierge_feed.py`, `plan_state.py`) — NOT into `trip_phase.py`, the chokepoint function |

The FE dev clock (#1) has **zero relationship** to the backend override (#4) —
grep for `dogfood_today` in `travel-app` returns nothing. A dev flipping the FE
time-travel clock changes what the FE renders but does not touch anything the
backend computes from real dates.

## The conflict is present-tense — no dev clock required

`mara-lisbon` (the wedge trip, `docs/working/persona-cast-consolidation-2026-07-08.md`'s
`S4-lisbon-group-planning`) is seeded with:

```yaml
# lisbon-phase1.yaml
start_date: 2026-10-03
end_date: 2026-10-06
status: live                    # <- hand-authored, never set by any override
trip_summary:
  state: group_live
  # no `dogfood_today` key
```

No `dogfood_today` is set. Today is 2026-07-08 — **87 days before `start_date`**.
Right now, with zero manual intervention, two backend surfaces already disagree:

- **`concierge_feed._phase()`** (home feed framing): `dogfood_today` is `None`,
  so its short-circuit `if trip.status == "live" and (dogfood_today is None or
  calendar_active)` is satisfied by the hardcoded status alone → returns **`"active"`**,
  regardless of dates.
- **`trip_phase.compute_trip_phase()`** (voice quotas, notification triage,
  lifecycle per its docstring): ignores `status` entirely, compares only dates
  to the real wall clock → returns **`"pre_trip"` / `"early_planning"`** (>14
  days out).

Same trip, same moment, two backend answers. Whichever surface the two-device
wedge walk happens to exercise determines which reality the walk observes —
silently, with no error and no log line calling it out.

## Why `status: live` is itself the deeper problem

`backend/notifications/leave_by.py:650` documents a **previously fixed defect**
in this exact family:

> "Defect #14 fix: the previous query filtered on `status == 'live'` which is
> **never written by any production code path** (trips are born 'ideation' and
> only transition to 'completed' or 'archived')."

`trips.status` has no DB `CheckConstraint` — it's free text, default `'ideation'`.
`'live'` is a value **only dogfood manifests ever write**; no real trip state
machine produces it. So `status: live` in the manifest isn't a snapshot of a
real trip state — it's authored narrative flavor that happens to collide with
a string some (but not all) backend code still branches on directly. That's
what made Defect #14 possible once already, and `concierge_feed.py`'s `_phase()`
still branches on the same literal today.

## Risk to the two-device wedge walk

The wedge walk exercises **create → invite → plan → propose** (J02→J05) — a
*planning*-phase interaction, not a live-trip one. But:

- If anything the walk touches routes through `trip_phase.compute_trip_phase()`
  (voice quotas, notification triage), it will see `pre_trip/early_planning`
  for a trip the manifest and home-feed framing insist is `"active"`/`live`.
  A proposal-notification test, or any copy that reads "days until departure,"
  could silently show 87-days-out framing during a walk meant to feel like an
  imminent group reunion.
- This is exactly the kind of bug that would make the wedge walk *look* broken
  for reasons that have nothing to do with the invite/proposal logic actually
  under test — burning the one real-device session on a date-math artifact.

## Recommended fix (small, follows the existing design)

1. **Wire `dogfood_today_override` into `trip_phase.compute_trip_phase()`.**
   Add an optional keyword-only param (consistent with the function's own
   "keyword-only so callers can adapt without contorting data" design):
   ```python
   def compute_trip_phase(*, title, status, start_date, end_date, tz=None,
                           dogfood_today: date | None = None) -> dict[str, Any]:
       ...
       today = dogfood_today or datetime.now(tz or _UTC).date()
   ```
   Non-breaking — existing callers omit the new param and get current behavior.
   Callers that have a `trip` object pass `dogfood_today_override(trip)`.

2. **Populate `trip_summary.dogfood_today` on `mara-lisbon`** (and any other
   wedge-relevant seeded trip) pinned to a date that keeps it inside its
   real `start_date`/`end_date` window relative to when the device walk
   actually happens — so `during_trip`/`live` is what a dogfooder sees on
   whichever surface they hit, consistently.

3. **Stop writing `status: live` as if it were a real trip state.** Use a
   real status (`planning`) + `dogfood_today` to pin phase. This removes the
   false signal Defect #14 already proved dangerous once, without waiting for
   a second defect to prove it again in `concierge_feed.py`.

4. **Give the FE a thin read of the same field**, so the FE's phase
   computation can prefer `trip.trip_summary.dogfood_today` over (or in
   addition to) the global manual time-travel clock. This means a dogfooder
   who logs into the seeded backend on a real device sees the *authored*
   phase automatically — no manual time-travel step required, and no way for
   FE and backend to derive different "today"s for the same trip.

Not proposed: reconciling the FE's global time-travel clock itself. It serves
a different job (arbitrary manual exploration of any phase, any trip, for
screenshots/demos) and should stay separate from the per-trip authored pin.

## Sequencing

This is small and touches phase-computation logic used by voice quotas and
notification triage — worth a narrow, reviewed patch rather than folding into
the persona-registry commits. Suggested order, ahead of the two-device walk:

1. Add the `dogfood_today` param to `compute_trip_phase()` (non-breaking).
2. Set `trip_summary.dogfood_today` on `mara-lisbon`; drop `status: live` in
   favor of `status: planning` + the pinned date.
3. Spot-check `concierge_feed._phase()` and `trip_phase.compute_trip_phase()`
   now agree on `mara-lisbon`'s phase.
4. (Fast-follow, not blocking) FE reads the same field.

## Executed 2026-07-08

**Steps 1-3 done, verified, not yet committed.** Also wired a third call site
(`backend/api/routes/voice.py`, the voice-quota path) that direct code
investigation found calling `compute_trip_phase()` raw with a column-projection
row — not covered by the `compute_trip_phase_from_obj()` wrapper, so it would
have stayed unfixed otherwise.

- `backend/core/dogfood_dates.py` — `dogfood_today_override()` now accepts a
  `Mapping` (SQLAlchemy `RowMapping`) in addition to attribute-style objects,
  needed for the voice.py call site.
- `backend/core/trip_phase.py` — `compute_trip_phase()` gets an optional
  keyword-only `dogfood_today: date | None = None` (non-breaking);
  `compute_trip_phase_from_obj()` now resolves and passes it automatically,
  so both existing callers (`backend/api/lifecycle.py`, `backend/discover/compose.py`)
  get the fix with no call-site change.
- `backend/api/routes/voice.py` — added `trips.c.trip_summary` to the
  column-projection select; passes `dogfood_today_override(row)` through.
- `lisbon-phase1.yaml` — `mara-lisbon`: `status: live` → `status: planning`
  (matches the original design intent already recorded in
  `persona-dossiers.md`, which says "status `planning`" — the manifest had
  drifted from its own design doc); added `trip_summary.dogfood_today:
  "2026-09-25"`.

**Pin choice, corrected mid-execution:** initially pinned to a during-trip date
(`2026-10-04`) per this doc's original step 2 wording ("keeps it inside its
real start/end window"). Caught before verifying: the wedge walk (J02-J05) is
entirely pre-trip planning behavior (create, invite, propose, mutate) — pinning
to during_trip would have introduced a *new* mismatch, putting the seeded world
in live-trip "what now" framing while the walk exercises planning surfaces.
Corrected to `2026-09-25` (8 days pre-departure → `pre_trip`/`active_planning`),
which also matches `persona-dossiers.md`'s original `status: planning` intent.
Also updated `trip_summary.state: group_live` → `group_planning` for the same
reason (unread by any code path, but would have been a fresh point of
confusion sitting next to the fix).

**Verified (before/after, real today = 2026-07-08):**

| | `trip_phase.py` | `concierge_feed._phase()` |
|---|---|---|
| **Before** (`status: live`, no `dogfood_today`) | `pre_trip` / `early_planning` (87 days out) | `active` |
| **After** (`status: planning`, `dogfood_today: 2026-09-25`) | `pre_trip` / `active_planning` (8 days out) | `imminent` |

Before: a direct contradiction (one surface says "happening now," the other
says "3 months away"). After: both surfaces agree the trip is imminent /
being actively planned — the correct phase for the wedge walk.

**Also verified:** manifest still validates against `DogfoodManifest` pydantic
schema; all 12 existing `tests/core/test_trip_phase_timezone.py` tests still
pass (non-breaking); ruff clean on all 3 edited files; mypy clean on all 3
(whole-repo `make typecheck` shows 2 pre-existing errors in
`backend/core/db/plan_similar.py`, last touched 2026-07-06, unrelated to this
change).

## Step 4 — FE reads the same field (executed)

**Turned out to matter more than "fast-follow."** Investigation surfaced that
the FE's own `computeTripPhase()` (`travel-app/utils/helpers.ts`) has the
*same* `status === 'live'` shortcut pattern Defect #14 already proved
dangerous on the backend — and the FE's own doc-comment lists valid statuses
as `ideation / planning / confirmed / archived`, `'live'` isn't among them
either. That meant fixing only the backend (steps 1-3) would have **replaced
one 3-way mismatch with a different one**: pre-fix, the FE's `status==='live'`
shortcut accidentally *agreed* with `concierge_feed._phase()`'s wrong answer
(`'active'`); post-fix (manifest now `status: planning`), the FE would fall
through to real wall time and compute `'pre'` — a *fourth* distinct answer,
disagreeing with both backend surfaces.

**Fix:** `travel-app/utils/helpers.ts` — added `dogfoodTodayOverride()`,
mirroring `backend/core/dogfood_dates.dogfood_today_override()` exactly
(reads `trip_summary.dogfood_today`, validates, returns `null` on
absent/malformed). `computeTripPhase()` takes an optional `trip_summary` field
and uses the override to compute `today` in place of real wall time, with the
same precedence as the backend. Purely additive: `trip_summary` was already
**required** on the FE's canonical `APITrip` type (used by `isBlankTrip()`
already), so all ~24 existing call sites needed zero changes.

**Verified:**
- All 6 pre-existing `computeTripPhase.test.ts` tests pass unchanged.
- 5 new tests added: pinned-date phase transitions (pre/active/completed), a
  direct mara-lisbon regression check, fallback-to-real-time when the field is
  absent or malformed, and a non-string-value doesn't-throw guard. 11/11 pass.
- `npx tsc --noEmit` — 0 errors across the whole app (confirms the optional
  field addition doesn't break any consumer).
- `eslint` clean on both changed files.
- 5 broader indirect test suites (journey-12 mock walk, trip-workspace smoke,
  trips-home smoke, Atlas starting-points, timezone consent-phase) — 35/35
  pass, zero regressions.

The FE's global manual time-travel clock (`utils/now.ts`) is intentionally
untouched — it remains a separate mechanism for a separate job (arbitrary
manual exploration for screenshots/demos), not reconciled with the per-trip
authored pin.

## Commits

- **travel-agent** `a651738b` (steps 1-3: BE wiring) — pushed to
  `persona-cast-consolidation`.
- **travel-app** `55ea65ee` (step 4: FE wiring) — pushed to
  `persona-cast-consolidation` (new branch, matching name).
- **workspace** — this doc — pushed to `persona-cast-consolidation`.

All three repos now have a matching `persona-cast-consolidation` branch
carrying both the persona-registry work and this clock-drift fix, ready for
review as one coherent change set ahead of the two-device wedge walk.
