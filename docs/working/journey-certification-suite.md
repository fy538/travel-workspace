# Journey Certification Suite — Full Specification

> Status: MVP built — 12 deterministic journey slices running
> Owner: founder / engineering
> Created: 2026-06-28
> Last updated: 2026-06-28
> Purpose: implementation spec and operating guide for deterministic journey certification

---

## What This Is

A business logic QA layer that mirrors the existing Maestro visual QA system. Maestro answers "does the UI look right?" This system answers "did the right thing actually happen in the backend?"

The two systems together produce a per-journey verdict:

```
logic: PASS + visual: PASS = journey CERTIFIED
```

The MVP infrastructure now exists. All 12 canonical journeys have deterministic backend scenario coverage wired through `travel-app/scripts/logic-qa/run-logic-qa.mjs`. All 12 journeys are mock-walk green and static-trace ready (as of 2026-06-27), but zero are fully dogfood-ready until visual QA and live-device gates also pass.

Current MVP coverage:

| Journey | Backend scenario | Logic status | Notes |
|---|---|---|---|
| `J01` | `tests/scenarios/test_j01_vague_idea_to_trip.py` | PASS | Blank draft dedupe, planning-intent bootstrap, explicit promotion, no fake itinerary |
| `J02` | `tests/scenarios/test_j02_invite_acceptance.py` | PASS | Invite acceptance, membership, consumed-token behavior |
| `J03` | `tests/scenarios/test_j03_cold_trip_setup.py` | PASS | Blank setup honesty, place/date/title PATCH hydration, cold→pre Folio coherence, non-organizer setup guard |
| `J04` | `tests/scenarios/test_j04_private_constraint.py` | PASS | Private phrase redaction and audit event |
| `J05` | `tests/scenarios/test_j05_proposal_plan_mutation.py` | PASS | Proposal accept/apply/revert, reject preservation, vote idempotency |
| `J06` | `tests/scenarios/test_j06_home_plan_map_changes_coherence.py` | PASS | Cross-surface block-id parity, unplaced map visibility, home dismissal safety, proposal apply invalidation |
| `J07` | `tests/scenarios/test_j07_discover_context_to_trip_action.py` | PASS | Discover context → Vesper seed → private save / trip venue commit |
| `J08` | `tests/scenarios/test_j08_live_trip_what_now.py` | PASS | Live trip phase, active day, map/Folio parity, grounded Vesper seed |
| `J09` | `tests/scenarios/test_j09_notifications_proactive_routing.py` | PASS | Proactive feed payloads, read state, ownership, quiet-hours channel gating |
| `J10` | `tests/scenarios/test_j10_booking_stay_expense_trust_loop.py` | PASS | Stay privacy, explicit expense opt-in, booking approval boundaries, no fabricated checkout success |
| `J11` | `tests/scenarios/test_j11_atlas_candidate_memory_control.py` | PASS | Candidate approval, artifact provenance, timeline/almanac projection, hide/restore, signal controls |
| `J12` | `tests/scenarios/test_j12_returned_trip_closeout.py` | PASS | Cached story, settlement transfer, returned-trip home cards |

---

## Industry Precedent

This system is not invented from scratch. It combines several established QA and design-system practices into one product-specific certification layer.

### Journey-based end-to-end testing

The core idea is closest to **journey-based E2E testing**: drive a real user sequence across API, database, and product state, then assert that the whole workflow ended correctly. Traditional E2E testing validates that complete workflows work across system boundaries; this suite makes that idea more explicit by naming each workflow as a canonical product journey (`J01` through `J12`) and certifying it against the journey docs.

In this repo, that means:

```
journey doc → real backend scenario test → state/invariant assertions → verdict
```

### Business process testing

Enterprise QA often calls the same shape **business process testing**: rather than testing isolated endpoints, it tests meaningful business outcomes. For Vesper, the business outcomes are things like:

- a private constraint changes the plan without leaking to the group
- an invite produces the correct member state and permissions
- a proposal vote mutates the plan only when it should
- a returned trip becomes memory/story/settle-up state without keeping live-trip affordances

This is why each scenario should assert product meaning, not only HTTP status codes.

### Model-based and stateful testing

The suite also borrows from **model-based testing** and **stateful property testing**. Those disciplines define expected states, allowed transitions, and invariants, then check that real execution never violates them.

For Vesper, useful state transitions include:

```
draft → planned → live → returned
invited → accepted → active member
proposal created → voted → resolved → plan mutation
private input → redacted group output → safe plan state
```

The `## Must Never Happen` sections in `docs/journeys/` are effectively invariant specs. Treat them as first-class test assertions.

### Visual regression and design-system QA

This suite intentionally parallels the existing Maestro polish QA system. Maestro and screenshot review are the visual-regression side of the house: they answer whether the interface still looks aligned with the design contract. Journey Certification answers whether the underlying behavior still matches the product contract.

Together:

```
Maestro visual QA      → surface fidelity
Journey logic QA       → backend/product truth
Both PASS              → journey certified
```

### Canonical design source of truth

The canonical Claude design file currently being consolidated in parallel should be treated as **design intent**, not as the only source of truth. The durable stack should be:

1. Claude design board — screen families, visual intent, edge states, examples
2. Design tokens in code — type, spacing, color, radius, shadows, surfaces
3. Implemented component primitives — cards, rows, chrome buttons, receipt blocks
4. Maestro visual QA — screenshots prove the implementation still matches intent
5. Journey Certification — scenario tests prove the product state still behaves correctly

The key idea: design artifacts and journey artifacts should both be canonical, but they certify different dimensions of product quality.

---

## Why This Exists

The current test pyramid has a gap:

| Layer | What it checks | What it misses |
|---|---|---|
| Maestro polish flows (61 flows) | Does the UI render correctly? | Is the data real? Did the right DB state result? |
| Backend API tests (84 files) | Do individual endpoints return correct responses? | Does a full multi-step user scenario produce the right state? |
| FE mock-walk tests (97 tests) | Does the UI behave correctly against mocked data? | Does real backend data match the mock's assumptions? |
| `tests/scenarios/test_j*.py` (12 journeys + J05 plan-edit) | Full journey slices incl. I5/I6/I7/I8 | Visual/live-device gates still need promotion-level certification |

The gap: no layer says "given this user sequence, is the entire system — data + state + presentation — correct?"

This system closes that gap with **backend scenario tests** for all 12 journeys, using the same real-DB + TestClient approach as `tests/scenarios/conftest.py` and the J05 suite (`test_j05_proposal_plan_mutation.py`, `test_j05_plan_edit_commit.py`).

---

## Relationship to the Maestro System

This system is deliberately parallel to Maestro. Learn the Maestro pattern first — the new system is the same shape.

### Maestro visual QA (existing)

```
docs/surfaces/<surface>/contract.md      ← what the surface must look like
scripts/polish-qa/surfaces.mjs           ← registry of surfaces + flows + scenarios
.maestro/polish/<flow>.yaml              ← generated by agents from the contract
scripts/polish-qa/run-polish-qa.mjs      ← orchestrator
docs/surfaces/<surface>/accepted/*.png   ← accepted screenshots
verdict.md per run                       ← PASS / MIXED / FAIL
```

### Journey Certification (MVP built)

```
docs/journeys/<id>-<name>.md             ← behavioral spec
travel-app/scripts/logic-qa/scenarios.mjs
travel-app/scripts/logic-qa/run-logic-qa.mjs
travel-app/docs/logic-qa/visual-certification-matrix.md
travel-app/docs/logic-qa/runs/<date>/verdict.json
travel-agent/tests/scenarios/test_j<id>_<name>.py
```

The **journey docs** (`docs/journeys/`) already contain everything the agent needs to generate the test:
- `## Expected Outcome` → the state assertions to write
- `## Must Never Happen` → the invariant checks (these are the most important)
- `## Canonical Steps` → the HTTP sequence to drive
- `## Starting State` → the persona + fixture to seed

---

## Repo Layout

### Where things live

```
travel-workspace/              (workspace docs repo — git@github.com:fy538/travel-workspace.git)
├── docs/
│   ├── journeys/              ← 12 journey specs — the behavioral contracts (READ THESE)
│   │   ├── 01-vague-idea-to-vesper-shaped-trip.md
│   │   ├── 02-concrete-trip-creation-and-invite.md
│   │   ├── 03-cold-trip-setup-to-useful-workspace.md
│   │   ├── 04-private-constraint-to-group-safe-plan.md
│   │   ├── 05-group-planning-to-proposal-to-plan-mutation.md
│   │   ├── 06-home-plan-map-changes-coherence.md
│   │   ├── 07-discover-to-contextual-vesper-to-trip-action.md
│   │   ├── 08-live-trip-what-now-companion.md
│   │   ├── 09-notifications-and-proactive-routing.md
│   │   ├── 10-booking-stay-expense-trust-loop.md
│   │   ├── 11-atlas-candidate-to-memory-control.md
│   │   └── 12-returned-trip-to-story-memory-settle-up.md
│   ├── systems/               ← 14 system charters (invariants, failure modes)
│   └── working/
│       └── journey-certification-suite.md  ← THIS FILE
│
travel-agent/                  (backend repo — git@github.com:fy538/travel-agent.git)
├── backend/                   ← Python/FastAPI source
│   ├── api/routes/            ← HTTP route handlers
│   ├── core/db/               ← DB helpers (SQLAlchemy Core, no ORM)
│   ├── concierge/             ← chat agent, group_compose.py, privacy redactor
│   ├── planning_agent/        ← itinerary generation
│   ├── preference_engine/     ← personal memory, group synthesis
│   └── notifications/         ← proactive system
├── tests/
│   ├── conftest.py            ← shared fixtures, requires_postgres marker
│   └── scenarios/             ← deterministic journey scenario tests (THE PATTERN)
│       ├── conftest.py        ← persona fixtures, scenario_client (read this first)
│       ├── test_j05_proposal_plan_mutation.py  ← proposal lifecycle (I5/I6)
│       └── test_j05_plan_edit_commit.py          ← plan-edit I7/I8 (ported from retired wedge E2E)
│
travel-app/                    (frontend repo — git@github.com:fy538/travel-app.git)
├── scripts/
│   ├── polish-qa/             ← existing Maestro orchestration (study this pattern)
│   │   ├── surfaces.mjs       ← surface registry
│   │   └── run-polish-qa.mjs  ← orchestrator
│   └── logic-qa/              ← mirrors polish-qa for backend scenario verdicts
│       ├── scenarios.mjs
│       ├── run-logic-qa.mjs
│       └── verdict.mjs
└── docs/
    ├── surfaces/              ← visual contracts (study for the pattern)
    └── logic-qa/              ← verdict outputs
        └── runs/
```

---

## The Test Pattern

**Read `travel-agent/tests/scenarios/conftest.py` and an existing `test_j*.py` before writing any scenario test.** Every new test must follow this pattern exactly.

### Key conventions from the scenario tests

```python
# 1. Module docstring explains the journey and which invariants are certified
"""End-to-end [journey name] invariants against the REAL DB + routes.
...
"""

# 2. Data is uniquely namespaced per test — uuid4 emails, fresh trips
#    NEVER depend on global seeds; tests must not collide

# 3. Schema guard for DB migration drift
requires_current_block_schema = pytest.mark.skipif(
    not _schema_is_current(),
    reason="DB behind migrations — run `make migrate`"
)

# 4. Minimal app: only mount the routers under test
def _app(actor):
    app = FastAPI()
    app.include_router(proposals_router)
    register_exception_handlers(app)
    app.dependency_overrides[get_current_user] = lambda: actor
    return app

# 5. Test names encode the invariant: test_i6_revert_restores_exact_pre_proposal_state
# 6. Each test is self-contained: seeds → drives → asserts → no shared state
# 7. DB assertions go deeper than HTTP status codes:
#    check actual rows, check counts, check that prohibited data does NOT exist
```

### Shared conftest to build

`tests/scenarios/conftest.py` needs persona fixtures matching the 5 dev personas. These make every scenario test start from a realistic named state rather than anonymous uuids:

```python
# tests/scenarios/conftest.py

@pytest.fixture
def persona_elif(db_conn):
    """Frequent traveler. Has Rome trip history. Used for planning + proposal scenarios."""
    user = create_user(db_conn, email=f"elif-{uuid4()}@test.vesper",
                       display_name="Elif", ...)
    trip = create_trip_with_organizer(db_conn, user_id=user.id,
                                     title="Rome November", ...)
    # seed itinerary, blocks, existing proposals as needed per scenario
    return SimpleNamespace(user=user, trip=trip, ...)

@pytest.fixture
def persona_ben(db_conn):
    """Loose planner. Has Copenhagen trip. Used for cold-start + expense scenarios."""
    ...

@pytest.fixture
def persona_carmen(db_conn):
    """Budget-conscious. Has Mexico trip. Used for expense + settlement scenarios."""
    ...

@pytest.fixture
def persona_ana(db_conn):
    """First-time user. No trips. Used for cold-start + onboarding scenarios."""
    ...

@pytest.fixture
def two_persona_trip(db_conn, persona_elif, persona_ben):
    """Elif as organizer, Ben as invited member. Pre-accepted membership.
    Used for group scenarios (proposals, invite, privacy)."""
    add_trip_member(db_conn, trip_id=persona_elif.trip.id,
                    user_id=persona_ben.user.id, role="member")
    return SimpleNamespace(organizer=persona_elif, member=persona_ben,
                           trip=persona_elif.trip)
```

---

## Acceptance Ladder

Mirrors `docs/surfaces/_quality-baseline.md` for the logic layer.

| Gate | Passes when |
|---|---|
| **Scenario gate** | Test completes without exception; persona fixtures seed and route correctly |
| **State gate** | DB rows after the scenario match the journey doc `## Expected Outcome` |
| **Invariant gate** | Every `## Must Never Happen` condition is checked and none fire |
| **Certified** | All three gates pass across every scenario variant defined for the journey |

### Severity taxonomy (same as visual QA)

| Severity | Meaning | Examples |
|---|---|---|
| **Blocker** | An invariant is violated — the user can observe a wrong/dangerous outcome | Privacy leak to group; invite accepts into wrong trip; duplicate applied change; ghost block after revert |
| **Major** | State is wrong but not dangerous | Wrong member count; missing receipt event; stale timestamp not surfaced as 409 |
| **Minor** | Edge case misbehaves | Expired invite returns 200 instead of 410; optional field missing from response |
| **Nit** | Cosmetic data issue | Field populated with default instead of computed value |

### Verdict rules

- **PASS**: zero blockers, zero majors, ≤ two minors
- **MIXED**: no blockers, one or two majors or > two minors
- **FAIL**: any blocker

---

## Journey Scenario Specs

For each journey: what the scenario test must seed, drive, and assert. These are derived from the existing journey docs and system charter invariants — read the full journey doc before writing the test.

---

### J01 — Vague Idea to Vesper-Shaped Trip

**Journey doc**: `docs/journeys/01-vague-idea-to-vesper-shaped-trip.md`
**System charter**: `docs/systems/concierge-vesper.md`, `docs/systems/trips-folio.md`
**Test file**: `tests/scenarios/test_j01_shape_trip.py`
**Persona fixture**: `persona_ana` (first-time user, no trips)
**Key risk**: cold start, Trips Home phases, first-session concierge handoff

**Scenario to certify:**
1. Ana POSTs a vague intent message to the concierge (no active trip)
2. Vesper responds with a shaped trip suggestion
3. Ana accepts → trip row created, organizer membership created
4. Trip lands in the correct lifecycle phase (`planning`)

**State assertions:**
- `trips` table: one new row with `status='planning'`, `organizer_id=ana.id`
- `trip_members` table: one row with `user_id=ana.id`, `role='organizer'`
- `conversations` table: at least one concierge turn recorded
- `concierge_turns` table: `origin='test'`, not null response

**Must Never Happen checks:**
- Vesper reply contains fabricated place names not in the knowledge base
- Trip is created with `status=NULL` or an undefined status value
- `promoted_trip_id` in the concierge response references a non-existent trip

---

### J02 — Concrete Trip Creation and Invite

**Journey doc**: `docs/journeys/02-concrete-trip-creation-and-invite.md`
**System charter**: `docs/systems/group-social.md`
**Test file**: `tests/scenarios/test_j02_invite_acceptance.py`
**Existing coverage**: `tests/api/test_invites_api.py`
**Persona fixtures**: `persona_elif` (organizer), `persona_ben` (invitee)
**Key risk**: invite token maps to exactly one trip; auth detour preserves token; consumed invite is not reusable

**Scenarios to certify:**

*Scenario A — happy path:*
1. Elif creates a trip → trip row exists
2. Elif creates invite → `trip_invites` row, token returned
3. Ben hits `POST /api/invites/{token}/accept` → atomic `consume_and_add_trip_member`
4. Ben is now a member; invite is consumed

*Scenario B — auth detour (token survival):*
1. Invite token created for Elif's trip
2. Unauthenticated user hits accept endpoint → 401
3. Same token hits accept endpoint with Ben's auth → succeeds
4. Token is now consumed; third attempt → 410

*Scenario C — invalid tokens:*
- Consumed token → 410
- Expired token → 410
- Unknown token → 404
- Token for wrong trip → cannot be created (one token = one trip invariant)

**State assertions:**
- After accept: `trip_members` has Ben with `role='member'`, `trip_id=elif.trip.id`
- After accept: `trip_invites.consumed_at` is not null
- Non-member cannot fetch trip details (403 on `GET /api/trips/{id}`)

**Must Never Happen checks:**
- Accept lands Ben in a different trip than Elif's
- Consumed invite returns 200 on retry
- Non-member can see private trip data pre-accept (fetch trip → 403)

---

### J04 — Private Constraint to Group-Safe Plan

**Journey doc**: `docs/journeys/04-private-constraint-to-group-safe-plan.md`
**System charter**: `docs/systems/concierge-vesper.md`, `docs/systems/memory-preference.md`
**Test file**: `tests/scenarios/test_j04_private_constraint.py`
**Persona fixtures**: `two_persona_trip` (elif=organizer, ben=member)
**Key risk**: **unrecoverable trust event** — highest priority test in the suite

**What this tests:** The privacy egress invariant. `group_compose.py` is the only sanctioned path for group-bound text. Every path that can route private signal to the group must be tested.

**Leak phrases to inject and then search for:**
```python
PRIVATE_CONSTRAINT_PHRASES = [
    "ankle injury",
    "budget is $500",
    "gluten intolerant",
    "low energy",
    "secret anniversary",
]
```

**Scenarios to certify:**

*Scenario A — private concierge intake:*
1. Ben sends private constraint to private concierge channel (`POST /api/trips/{id}/messages` with `channel='private'`)
2. Vesper acknowledges privately
3. Assert: Ben's private message is NOT in the group conversation thread
4. Assert: No `PRIVATE_CONSTRAINT_PHRASES` appear in any `messages` row where `scope='group'`

*Scenario B — group-safe proposal generation:*
1. Ben has a private constraint stored in Personal Memory
2. Vesper generates a proposal for the group
3. Assert: proposal `summary` and `rationale` contain no leak phrases
4. Assert: proposal was routed through `group_compose.py` (check `composition_method` field if present)

*Scenario C — notification body check:*
1. Trigger a notification for the trip (proposal created, etc.)
2. Fetch the notification row
3. Assert: notification `title` and `body` contain no leak phrases

*Scenario D — booking copy check:*
1. Trigger a booking proposal summary for the trip
2. Assert: booking summary contains no leak phrases referencing financial constraints, accessibility, or dietary needs

**State assertions for all scenarios:**
- `messages` with `scope='group'`: zero rows containing any leak phrase
- `change_proposals`: `summary` and `rationale` columns contain no leak phrases
- `notifications` or equivalent: `title`/`body` contain no leak phrases

**Must Never Happen checks:**
- Any group-bound text contains a leak phrase → **Blocker**
- Private message appears in group conversation thread → **Blocker**
- `composition_skipped=True` message delivered to group without redaction → **Blocker**

---

### J05 — Group Planning to Proposal to Plan Mutation

**Journey doc**: `docs/journeys/05-group-planning-to-proposal-to-plan-mutation.md`
**System charter**: `docs/systems/proposals-change-studio.md`
**Test file**: `tests/scenarios/test_j05_proposal_plan_mutation.py`, `tests/scenarios/test_j05_plan_edit_commit.py`
**Existing coverage**: `tests/api/test_proposals_api.py`, `tests/api/test_plan_edit_commit.py`
**Persona fixtures**: `two_persona_trip`
**Key risk**: state machine completeness, idempotency, revert truthfulness

**J05 is the most-tested journey.** Scenario tests cover I5/I6 (proposals) and I7/I8 (plan-edit commit). Expand only where gaps remain:

*Scenario A — full proposal lifecycle:*
- Verify: rejected proposal leaves plan unchanged, receipt event emitted for rejection (extend `test_j05_proposal_plan_mutation.py` if not already asserted)

*Scenario B — direct Change Studio edit (Track B):*
1. Ben previews a direct edit (`POST /api/trips/{id}/plan-edit-preview`)
2. Token returned; Ben commits (`POST /api/trips/{id}/plan-edit-commit`)
3. Assert: block updated, `plan_events` ledger has the edit recorded
4. Ben replays same commit token → idempotent (same result, not duplicate)

*Scenario C — concurrent edit conflict (I7):*
1. Elif and Ben both fetch the same block with `updated_at=T`
2. Elif commits first → succeeds
3. Ben commits with stale `expected_updated_at=T` → 409
4. Assert: block has Elif's edit, not Ben's; `plan_events` has one entry

(`test_j05_plan_edit_commit.py` certifies B and C today.)

**State assertions:**
- Accepted proposal: `change_proposals.status='accepted'`, block mutation applied, `plan_events` entry
- Rejected proposal: `change_proposals.status='rejected'`, block unchanged, receipt event present
- Reverted proposal: `change_proposals.status='reverted'`, block restored to pre-proposal state, no ghost blocks

---

### J06 — Home/Plan/Map/Changes Coherence

**Journey doc**: `docs/journeys/06-home-plan-map-changes-coherence.md`
**System charter**: `docs/systems/trips-folio.md`
**Test file**: `tests/scenarios/test_j06_home_plan_map_changes_coherence.py`
**Persona fixtures**: `scenario_user`, `scenario_trip`, `scenario_client`
**Key risk**: after any mutation, all read models agree on block IDs and state

**Implemented scenario:**
1. Seed trip with one mapped block and one unplaced block
2. Create an open proposal affecting the unplaced block
3. Fetch Plan and Map → verify block-id parity and unplaced map visibility
4. Fetch Folio read model → verify the spine points at the same block
5. Dismiss an unrelated ambient Home key → verify the open decision still appears in Home and Plan
6. Accept/apply the proposal through the real route
7. Fetch Plan, Map, Folio, and recent Changes → verify the current block id, updated time, and source proposal all agree

**State assertions:**
- Plan and Map return the same canonical block IDs before mutation
- Map keeps unplaced blocks visible as `point: null` plus a day-level spatial note
- After mutation, Plan/Map/Folio point at the forked-forward current block id
- Folio spine day count matches Plan day count
- Plan recent_changes routes back to the source proposal and the current affected block

**Must Never Happen checks:**
- Stale block ID appears in any read model after proposal accept → **Blocker**
- Changes feed references a block ID that no longer exists → **Major**
- Folio spine day count diverges from Plan day count → **Major**

---

### J08 — Live Trip What-Now Companion

**Journey doc**: `docs/journeys/08-live-trip-what-now-companion.md`
**System charter**: `docs/systems/concierge-vesper.md`
**Test file**: `tests/scenarios/test_j08_live_trip.py`
**Persona fixtures**: `persona_elif` with trip in `live` status
**Key risk**: Vesper Home live mode, situation read model, context freshness

**Scenario to certify:**
1. Seed a trip with `status='live'` and a realistic day's itinerary
2. Elif sends "what should I do now?" to concierge
3. Assert: Vesper accesses situation context (not just planning context)
4. Assert: response references the current day's blocks, not future planning
5. Assert: response does not reference blocks from other trips (isolation)

**State assertions:**
- `concierge_turns`: turn recorded, `trip_id` matches live trip
- Response does not contain names of other trips or their blocks

**Must Never Happen checks:**
- Concierge routes a live-trip message into planning mode → **Major**
- Vesper references blocks from another trip in the response → **Blocker** (cross-trip data leak)
- Response fabricates venue details not in the knowledge base → **Major**

---

### J12 — Returned Trip to Story, Memory, Settle-Up

**Journey doc**: `docs/journeys/12-returned-trip-to-story-memory-settle-up.md`
**System charter**: `docs/systems/expenses-settlement.md`, `docs/systems/memory-preference.md`
**Test file**: `tests/scenarios/test_j12_returned_trip_closeout.py`
**Persona fixtures**: `two_persona_trip` with trip transitioned to `returned` status
**Key risk**: post-trip closure loop, settlement computation, memory promotion

**Scenario to certify:**
1. Trip transitions from `live` to `returned`
2. Assert: home feed card for "returned" state generated
3. Settle-up: seed expense ledger (Ben paid 100, Carmen paid 0 toward shared expense)
4. Compute settlement → assert correct owed amounts
5. Mark settled → assert `settlement_status='settled'` on expense
6. Story generation triggered → assert `trip_stories` row created with correct `trip_id`

**State assertions:**
- `trips.status='returned'` after transition
- Settlement: debt direction correct (Carmen owes Ben, not vice versa)
- After settle: no open balances
- `trip_stories` row exists, not null content

**Must Never Happen checks:**
- Settlement computation reverses debtor/creditor → **Blocker**
- Story generation references another user's private memories → **Blocker**
- Settlement marks all expenses paid when some are still open → **Blocker**

---

### Canonical scenario set complete

The second-pass gaps are now covered:

- `J01` certifies blank draft → private planning intent → promotion into a structured draft trip.
- `J07` certifies Discover context grounding, private saves, trip venue commits, and membership enforcement.
- `J08` certifies live trip plan/map/Folio/seed parity.
- `J11` certifies Atlas candidate approval, artifact provenance, timeline/almanac projection, hide/restore, signal-state control, and ownership isolation.

---

## The Registry and Orchestrator

### `scripts/logic-qa/scenarios.mjs`

Mirrors `scripts/polish-qa/surfaces.mjs`. The source of truth is
`travel-app/scripts/logic-qa/scenarios.mjs`, which now lists all 12 journeys
in canonical order (`J01` through `J12`) with their pytest targets and journey
docs.

### `scripts/logic-qa/run-logic-qa.mjs`

```js
// Usage:
//   node scripts/logic-qa/run-logic-qa.mjs              # run all
//   node scripts/logic-qa/run-logic-qa.mjs J04          # run one
//   node scripts/logic-qa/run-logic-qa.mjs --list       # list registered journeys
//   node scripts/logic-qa/run-logic-qa.mjs --no-write   # CI-style, no artifacts
//
// Outputs:
//   docs/logic-qa/runs/<date>/<journey-id>.json
//   docs/logic-qa/runs/<date>/verdict.json
```

The orchestrator:
1. Runs `python -m pytest <pytestTarget> -q -p no:cacheprovider`
2. Captures stdout/stderr and exit code per journey
3. Writes per-journey JSON plus a run-level `verdict.json`
4. Exits non-zero if any selected journey fails

### `docs/logic-qa/runs/<date>/verdict.json` structure

```json
{
  "startedAt": "2026-06-28T17:20:57.393Z",
  "finishedAt": "2026-06-28T17:21:09.359Z",
  "agentRoot": "/Users/feihuyan/travel-workspace/travel-agent",
  "status": "FAIL",
  "results": [
    {
      "id": "J04",
      "name": "Private Constraint to Group-Safe Plan",
      "status": "FAIL",
      "exitCode": 1,
      "durationMs": 1420,
      "pytestTarget": "tests/scenarios/test_j04_private_constraint.py",
      "doc": "../docs/journeys/04-private-constraint-to-group-safe-plan.md"
    }
  ]
}
```

---

## Build Sequence

### Phase 0 — Infrastructure (complete)

Built:

- `travel-agent/tests/scenarios/__init__.py`
- `travel-agent/tests/scenarios/conftest.py`
- `travel-app/scripts/logic-qa/scenarios.mjs`
- `travel-app/scripts/logic-qa/run-logic-qa.mjs`
- `travel-app/docs/logic-qa/README.md`
- ignored verdict output under `travel-app/docs/logic-qa/runs/`

The current `tests/scenarios/conftest.py` intentionally starts with generic `scenario_user`, `scenario_trip`, and `scenario_client` helpers instead of named persona fixtures. Keep using uuid4-backed fresh DB rows so tests never collide; add named persona fixtures only when a journey genuinely needs richer reusable dogfood state.

### Phase 1 — First deterministic scenarios (complete)

Built and green through `npm run qa:logic`:

- `J02` invite acceptance and consumed-token behavior
- `J03` blank setup, place/date/title hydration, cold→pre Folio coherence, and non-organizer setup guard
- `J04` private phrase redaction and audit event
- `J05` proposal apply/revert/reject/vote idempotency
- `J12` returned trip story, memory, and settlement closeout
- `J06` Home/Plan/Map/Folio/Changes coherence after proposal apply

### Phase 2 — Remaining deterministic journeys (complete)

Added and wired:

- `J01` Vague Idea to Vesper-Shaped Trip
- `J07` Discover to Contextual Vesper to Trip Action
- `J08` Live Trip What-Now Companion
- `J11` Atlas Candidate to Memory Control

Agent prompt template:

```
Build a backend scenario test for Journey XX following this exact pattern:
  - Pattern files: tests/scenarios/conftest.py, tests/scenarios/test_j05_proposal_plan_mutation.py
  - Persona fixtures: tests/scenarios/conftest.py
  - Journey spec: docs/journeys/XX-<name>.md  ← READ THIS FULLY
  - System charter: docs/systems/<relevant>.md  ← READ THE INVARIANTS SECTION

The test must:
1. Follow the naming convention: test_j<id>_<what>_<result>
2. Use real DB (requires_postgres mark)
3. Seed persona fixtures from conftest.py
4. Drive the HTTP sequence from the journey's Canonical Steps
5. Assert DB state from the journey's Expected Outcome
6. Assert every Must Never Happen as an explicit check with a clear failure message
7. Be self-contained: no shared state between tests, uuid4 namespacing
```

### Phase 3 — Runner hardening + richer verdict integration

Completed runner hardening:

- `--help` / `-h`
- `--list`
- `--json`
- `--no-write`
- clean unknown-option / unknown-journey exit code 2
- app-side CI job that checks out `travel-agent`, migrates Postgres, and runs `npm run qa:logic -- --no-write`

Optional future hardening:

- add `scripts/logic-qa/verdict.mjs` if the JSON summary needs richer severity aggregation
- add per-invariant severity aggregation once the scenario tests expose named invariant metadata

Update `docs/journeys/STATUS.md` after each journey is certified.

---

## How to Run

```bash
# Run all scenario tests (requires Postgres running)
cd ~/travel-workspace/travel-agent
PYTHONPATH=. pytest tests/scenarios/ -q

# Run a single journey
PYTHONPATH=. pytest tests/scenarios/test_j04_private_constraint.py -q -p no:cacheprovider

# Run with verbose output for debugging
PYTHONPATH=. pytest tests/scenarios/test_j04_private_constraint.py -v

# Run logic QA orchestrator
cd ~/travel-workspace/travel-app
npm run qa:logic
npm run qa:logic:ci

# Run for a single journey
npm run qa:logic -- J04

# List registered journeys
npm run qa:logic:list
```

**Prerequisites:**
- Docker running with `research-agent-postgres` container (local dev DB — user/db `vesper`)
- Canonical DSN: `postgresql://vesper:localdev@localhost:5432/vesper` (see `travel-agent/.env.example`)
- `PYTHONPATH=.` from `travel-agent/` root
- DB at head: `cd travel-agent && alembic upgrade head`
- Node/npm dependencies installed in `travel-app`

---

## Key Files to Read Before Starting

In order of importance:

1. **`tests/scenarios/conftest.py`** — persona fixtures and `scenario_client` helper
2. **`tests/scenarios/test_j05_proposal_plan_mutation.py`** — reference scenario for multi-step HTTP + DB asserts
3. **`tests/conftest.py`** — shared infrastructure, `requires_postgres` marker
4. **`docs/journeys/04-private-constraint-to-group-safe-plan.md`** — privacy journey spec
5. **`docs/systems/concierge-vesper.md`** — privacy egress invariant
6. **`backend/concierge/group_compose.py`** — the only sanctioned group text path
7. **`scripts/polish-qa/surfaces.mjs`** — the registry pattern to mirror
8. **`scripts/polish-qa/run-polish-qa.mjs`** — the orchestrator pattern to mirror
9. **`docs/surfaces/_quality-baseline.md`** — the quality framework to mirror for logic
10. **`docs/journeys/STATUS.md`** — current certification status across all 12 journeys
11. **`docs/working/wedge-journey-02-05-path-to-dogfood.md`** — the wedge plan context

---

## What Already Exists (Do Not Duplicate)

These are already built and passing — new scenario tests should ADD coverage, not reimplement:

| Existing test | What it covers | Journal |
|---|---|---|
| `tests/scenarios/test_j01_vague_idea_to_trip.py` | Blank draft dedupe, planning-intent bootstrap, explicit promotion, no fake itinerary | J01 MVP |
| `tests/scenarios/test_j02_invite_acceptance.py` | Invite acceptance, member creation, consumed-token behavior | J02 MVP |
| `tests/scenarios/test_j03_cold_trip_setup.py` | Blank setup honesty, place/date/title hydration, cold→pre Folio coherence | J03 MVP |
| `tests/scenarios/test_j04_private_constraint.py` | Group-safe proposal copy and privacy audit | J04 MVP |
| `tests/scenarios/test_j05_proposal_plan_mutation.py` | Proposal apply/revert/reject/vote idempotency (I5/I6) | J05 MVP |
| `tests/scenarios/test_j05_plan_edit_commit.py` | Plan-edit commit I7 409 + I8 idempotency | J05 MVP |
| `tests/scenarios/test_j06_home_plan_map_changes_coherence.py` | Cross-surface block-id parity and proposal apply invalidation | J06 MVP |
| `tests/scenarios/test_j07_discover_context_to_trip_action.py` | Discover context grounding, private saves, trip venue commits | J07 MVP |
| `tests/scenarios/test_j08_live_trip_what_now.py` | Live trip phase, active day, map/Folio parity, grounded seed | J08 MVP |
| `tests/scenarios/test_j09_notifications_proactive_routing.py` | Proactive payloads, read state, ownership, cadence, quiet-hours gating | J09 MVP |
| `tests/scenarios/test_j10_booking_stay_expense_trust_loop.py` | Stay privacy, expense opt-in, booking approval boundaries | J10 MVP |
| `tests/scenarios/test_j11_atlas_candidate_memory_control.py` | Atlas candidate approval, artifact provenance, hide/restore, signal controls | J11 MVP |
| `tests/scenarios/test_j12_returned_trip_closeout.py` | Returned-trip cached story, settlement, memory/home-card closeout | J12 MVP |
| `tests/api/test_invites_api.py` | Invite CRUD, accept/reject/expire | J02 partial |
| `tests/api/test_proposals_api.py` | Proposal lifecycle unit tests | J05 partial |
| `tests/api/test_plan_edit_commit.py` | Plan edit commit unit tests | J05 partial |
| `tests/api/test_expenses_api.py` | Expense CRUD | J12 partial |
| `tests/concierge/` | LLM eval baselines (35 concierge scenarios) | J01/J04 partial |
| `travel-app/__tests__/journeys/` | FE mock-walk tests for J02/J05/J06 (27 tests) | J02/J05/J06 FE only |

The scenario tests are the **backend integration layer** that certifies the server-side invariants these unit tests and FE mock-walks cannot reach.

---

## Codebase Quick Reference

### Backend: how to create a trip with members

```python
from backend.core.db.trips import (
    create_trip_with_organizer, add_trip_member,
    create_itinerary_version, create_itinerary_day, create_block,
    get_full_itinerary,
)
from backend.core.db.traveler import create_user
from backend.core.db.engine import get_connection
from uuid import uuid4

with get_connection() as conn:
    user = create_user(conn, email=f"test-{uuid4()}@vesper.test", ...)
    trip = create_trip_with_organizer(conn, user_id=user.id, title="Test Trip")
    member = create_user(conn, email=f"member-{uuid4()}@vesper.test", ...)
    add_trip_member(conn, trip_id=trip.id, user_id=member.id, role="member")
```

### Backend: how to mount a minimal test app

```python
from fastapi import FastAPI
from fastapi.testclient import TestClient
from backend.api.auth import get_current_user
from tests.conftest import register_exception_handlers

def _make_app(actor, *routers):
    app = FastAPI()
    for router in routers:
        app.include_router(router)
    register_exception_handlers(app)
    app.dependency_overrides[get_current_user] = lambda: actor
    return app

client = TestClient(_make_app(user, some_router))
```

### Backend: key routes for scenario tests

| Route | Purpose |
|---|---|
| `POST /api/trips` | Create trip |
| `POST /api/trips/{id}/members/invite` | Create invite |
| `POST /api/invites/{token}/accept` | Accept invite (atomic `consume_and_add_trip_member`) |
| `GET /api/trips/{id}` | Fetch trip (403 for non-members) |
| `POST /api/trips/{id}/messages` | Send concierge message |
| `POST /api/trips/{id}/proposals` | Create proposal |
| `POST /api/trips/{id}/proposals/{pid}/vote` | Vote on proposal |
| `POST /api/trips/{id}/proposals/{pid}/apply` | Apply/accept proposal |
| `POST /api/trips/{id}/plan-edit-preview` | Preview direct edit |
| `POST /api/trips/{id}/plan-edit-commit` | Commit direct edit |
| `GET /api/trips/{id}/folio` | Folio read model |
| `GET /api/trips/{id}/changes` | Changes feed |

### Privacy: how to check for leaks

```python
from sqlalchemy import text
from backend.core.db.engine import get_connection

PRIVATE_PHRASES = ["ankle injury", "budget is $500", "gluten intolerant"]

def assert_no_leak_in_group_messages(trip_id, phrases):
    with get_connection() as conn:
        rows = conn.execute(
            text("SELECT content FROM messages WHERE trip_id=:tid AND scope='group'"),
            {"tid": trip_id}
        ).fetchall()
    for row in rows:
        for phrase in phrases:
            assert phrase.lower() not in (row.content or "").lower(), \
                f"Privacy leak: '{phrase}' found in group message"
```

### DB: how to assert itinerary state

```python
from backend.core.db.trips import get_full_itinerary

with get_connection() as conn:
    itin = get_full_itinerary(conn, trip_id=trip.id)

block_ids = {b.id for day in itin.days for b in day.blocks}
assert expected_block_id in block_ids
assert ghost_block_id not in block_ids
```

---

## Connection to Dogfood Readiness

Each journey moves from `partial` to `deterministic tests: PASS` in `docs/journeys/STATUS.md` when its scenario test is green. The promotion rules (from `docs/journeys/README.md`) require deterministic tests to pass before a live device canary is meaningful.

Current status of all 12 journeys: `static trace: ready` + `mock walk: ready` + deterministic backend slices green.

The scenario tests close the `deterministic tests` column. Once the wedge journeys are green, the live two-account walk (DoD 5/6 from `docs/working/wedge-journey-02-05-path-to-dogfood.md`) becomes the final gate before first real users.

Pair backend Logic QA with `travel-app/docs/logic-qa/visual-certification-matrix.md`.
The matrix defines the screenshot/device checks for each journey; dogfood-ready
requires both rails to pass.

**The order that matters most for dogfood:**
1. J04 privacy — ship safety gate; must pass before any external user
2. J02 invite — first thing every user does; must be deterministically correct
3. J05 proposals — the core group planning loop
4. J12 settle-up — required before any multi-user trip ends
