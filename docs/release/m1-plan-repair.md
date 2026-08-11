---
doc_type: contract
status: active
owner: founder / engineering
created: 2026-08-10
last_verified: 2026-08-10
why_new: Replaces three competing definitions of "done" with one milestone derived directly from the canonical demo journey.
supersedes: []
source_of_truth_for: [primary-milestone, m1-scope, m1-exit-criteria]
---

# M1 — Plan Repair

**The primary objective. If work does not serve M1, it is not this milestone.**

M1 is defined by the canonical demo journey, not by a capability list. The
milestone is complete when the flagship demo can be performed end to end, on
devices, with revision-bound evidence for every claim it makes.

## The one sentence

> Four friends have a Plan. Reality breaks it. Vesper proposes one grounded
> repair, the group accepts it through one governed mutation, every surface
> agrees, and a later occasion is measurably easier because of what happened.

Narrative authority: [Demo Journey Canon §13](../../travel-agent/docs/product/Demo%20Journey%20Canon.md).
Thesis authority: [Product Thesis](../../travel-agent/docs/product/Product%20Thesis.md).
This document owns only **what must be true for M1 to be called done**.

## Target

| Field | Value |
|---|---|
| Milestone | M1 — Plan Repair |
| Primary artifact | One uninterrupted recording of the four-act demo |
| Evidence bar | `device_mock` for every act; `staging` for Act 1 |
| External date | PearX W27 regular deadline, 2026-10-04 23:59 PT |
| Internal target | Demo recorded and certified by 2026-09-28 |

M1 is **not** a store release. TestFlight submission is governed separately by
[Owner Action Items](../Owner%20Action%20Items.md).

## Scope — the four acts

Each act is one row. An act is done when its proof carries the required
evidence layers at a clean revision.

### Act 1 — Immediate rescue

Open on an existing shared Plan made incoherent by a real change. Vesper
proactively proposes one concrete repair.

- **Proof:** P07 (live rescue) — currently `dark`
- **Required layers:** contract, database, device_mock, staging
- **Flags to light:** `WEATHER_RESCUE_PROPOSALS_ENABLED` scoped by
  `WEATHER_RESCUE_TRIP_IDS`
- **Known gaps:** group-safe composition of the proposal; two-observer device
  certification; Postgres Lisbon replay is time-of-day dependent
- **Rollback:** all-off — flag false returns the surface to silence

### Act 2 — Grounded judgment

Open the explanation far enough to show why the alternative fits these people,
this place, this time, these conditions. Provenance and uncertainty visible.

- **Proof:** P02 (spatially credible decision) — `active`
- **Required layers:** contract, database
- **Flags to light:** none
- **Known gaps:** no `device_mock` receipt recorded
- **Negative oracle:** an unavailable provider fact must render as honest
  fallback, never as fabricated certainty

### Act 3 — Multiplayer action

Accept the repair. Plan, route, timeline, and participant state reconcile
through one canonical mutation. A concise receipt and reversible history remain.

- **Proof:** P05 (thin participant handoff) — currently `dark`
- **Required layers:** contract, database, device_mock
- **Flags to light:** `GUEST_PROPOSAL_CAPABILITIES_ENABLED`
- **Known gaps:** mobile capability handoff; private-constraint capture prompt;
  two-observer vote recovery
- **Invariant:** no path may write a vote outside the canonical
  itinerary-proposal gateway

### Act 4 — Compounding relationship

A later local occasion. A confirmed outcome from Act 3 helps Vesper notice a
relevant opening. Ends on a mutually accepted local Plan, not a chat response.

- **Proof:** P03 (plan to lived outcome) + P04 (second occasion compounds)
- **Required layers:** contract, database, device_mock, ai_eval
- **Flags to light:** `LOCAL_PLAN_DOGFOOD_ENABLED`
- **Known gaps:** no `device_mock` for P03; no `ai_eval` receipt for P04;
  companion-scope applicability is exact-roster equality, so evidence from a
  four-person occasion cannot inform the same three people
- **Open ruling required:** whether exact-roster equality is the intended
  permanent boundary or a temporary conservative default

### Cross-cutting — consent and silence

Applies to all four acts and is not a fifth act.

- **Proof:** P06 (consent and silence) — `dark`, **zero anchors**
- **Required layers:** contract, database, device_mock, ai_eval
- **Known gaps:** no anchors exist; this is the largest undefined risk in M1
- **Bar:** no private input may become a shared claim; deliberate silence must
  be demonstrable, not merely possible

## Secondary — the sixty-second cold demo

Retained because it is the nearest-to-active proof and its source work is
already open.

> Open interval + next commitment → **Take me somewhere** → one feasible
> micro-journey → begin.

- **Proof:** P01 (occasion to accepted Move or Plan) — `active`
- **Flags to light:** `GROUP_TRIP_MICRO_JOURNEY_ENABLED`
- **Known gaps:** the CTA renders only while a block is active, not in the
  between-block opening the demo requires; the seed binds a block rather than a
  bounded open window; create-conversation drops supplied spatial context;
  `propose_change` is unavailable to private turns

Source closure order:
[canonical demo convergence closure plan](../working/canonical-demo-convergence-closure-plan-2026-08-10.md).

## Exit criteria

M1 is done when **all** of the following hold at one clean revision:

1. `evidence-attestations.json` contains promoted receipts for P01–P05 and P07
   at the layers named above.
2. P06 has anchors, and its consent/silence oracles pass.
3. One uninterrupted recording satisfies the acceptance test in
   [Demo Evidence Matrix](../../travel-agent/docs/fundraising/Demo%20Evidence%20Matrix.md).
4. A cold reader unfamiliar with Vesper repeats what it does, for whom, and why
   now — **without** summarizing it as an AI trip planner.
5. Every lit flag has a named rollback and a recorded off-state.

Criterion 4 is a real gate. `Demo Journey Canon` §17 names category collapse as
the leading qualitative failure.

## Explicitly out of M1

Named so they stop competing for the same weeks:

- broad ambient dispatch and any nearby feed;
- live booking transaction execution;
- live voice, narration, and microphone entry points;
- rendered postcards and public story distribution;
- Riviera / Giulia world expansion;
- AI decision-and-learning phases beyond R2;
- store submission and App Store asset production.

Dark-surface governance for these remains owned by
[the v1 release contract](v1-scope.md), which is a **shipping boundary, not a
roadmap**. M1 does not supersede its OUT rulings; where M1 needs a capability
that contract marks OUT or leaves unclassified, that requires an explicit scope
revision decision before the flag is lit.

## Known contract collisions to resolve

These are open and block nothing today, but must be ruled before Act 1 or Act 4
ships:

| Collision | Detail |
|---|---|
| `ambient` marked OUT | Act 4's opening uses `AMBIENT_COINCIDENCE_CANDIDATES_ENABLED`, listed under an OUT capability |
| `proactive-disruption` marked OUT | Act 1's producer, `_produce_weather_rescue`, lives in `backend/concierge/proactive.py`, an evidence path for that OUT capability |
| Three flags unclassified | `WEATHER_RESCUE_PROPOSALS_ENABLED`, `GROUP_TRIP_MICRO_JOURNEY_ENABLED`, `LOCAL_PLAN_DOGFOOD_ENABLED` appear nowhere in `v1-scope.yaml` |

## Relationship to existing authorities

| Document | Still owns | No longer owns |
|---|---|---|
| Demo Journey Canon | Which story we tell and what it must communicate | — |
| Product Proof Spine | P01–P07 definitions and evidence requirements | — |
| Journey Evidence Model | What each evidence layer proves | — |
| v1 release contract | Which surfaces must stay dark; production posture | Any implication of a roadmap or product promise |
| Current State | Generated implementation truth | — |

If this document conflicts with Product Thesis or Product Model, those win. If
it conflicts with an implementation claim, Current State and revision-specific
receipts win.
