---
doc_type: working
status: active
owner: founder / engineering
created: 2026-08-10
last_verified: 2026-08-10
expires: 2026-09-09
why_new: Audits every coexisting definition of done (J registry, P spine, v1 scope, alpha scope, demo canon, M1, MVP skill), dates each one, names which are current and which are stale, and defines the consolidation that makes the demo journey the single spine.
source_of_truth_for: [definition-of-done-consolidation]
related:
  - ../release/m1-plan-repair.md
  - ../journeys/PRODUCT_PROOF_SPINE.md
  - ../release/v1-scope.md
---

# Definition-of-done consolidation audit

## 1. Executive verdict

There are **seven coexisting definitions of done**. Five are load-bearing, two
are stale. The confusion is not from having several registries — it is from
three specific defects:

1. **The V1 release contract certifies against journeys the journey registry
   itself now classifies as historical.** Five of its IN capabilities anchor
   physical certification on J01/J02/J03/J11/J12 — all `historical` in the
   08-07 taxonomy.
2. **The 08-07 J-taxonomy re-classification was never propagated.** The
   redesign of the J-tests around the pivot already happened
   (`69d8ae5`, "define pivot product proof spine") — but v1-scope, the MVP
   skill, the journeys README's layer model, and the working plans never
   absorbed it.
3. **Three demo-critical flags exist in no contract at all**
   (`WEATHER_RESCUE_PROPOSALS_ENABLED`, `GROUP_TRIP_MICRO_JOURNEY_ENABLED`,
   `LOCAL_PLAN_DOGFOOD_ENABLED`).

**Ruling this document proposes:** consolidate against the demo journey — but
do **not** rewrite the 28 J-tests. They were already demoted to a regression
floor on 08-07 and they are cheap (28/28 seeded replay, ~37s). Redesigning
them would spend weeks destroying regression value to produce what P01–P07
already is. The demo-shaped layer already exists; the work is repointing the
**certification burden** and retiring the stale documents.

## 2. Full inventory — every definition of done, dated

| # | Artifact | Created | Last touched | Question it answers | State |
|---|---|---|---|---|---|
| 1 | J registry (`journeys.yaml`, 28 journeys) | 2026-06-30 | 08-07 | Does anything that used to work still work? | **CURRENT** as regression floor; taxonomy added 08-07 |
| 2 | Journey `STATUS.md` | 2026-06-06 | **08-10** | Current per-journey evidence | **CURRENT** — 28/28 seeded replay recorded 08-10; J08 repaired `2b61d7980` (08-08) |
| 3 | `EVIDENCE_MODEL.md` (7 layers) | 2026-08-07 | 08-10 | What does each kind of evidence prove? | **CURRENT** — backed by `journey_evidence.py` + promotion tooling |
| 4 | `PRODUCT_PROOF_SPINE.md` + `product-proofs.yaml` (P01–P07) | 2026-08-07 | 08-10 | What would prove the pivot thesis? | **CURRENT** — the demo-shaped layer; P05/P06/P07 dark |
| 5 | V1 release contract (`v1-scope.yaml`) | scope decided 06-30; YAML 08-09 | 08-10 | What may ship lit vs dark? | **SPLIT** — dark-surface boundary current; promise + J anchors + coverage stale |
| 6 | Demo Journey Canon (incl. alpha scope §14) | 2026-08-09 | 08-10 | What story do we tell, in what order? | **CURRENT** — narrative authority |
| 7 | M1 — Plan Repair (`m1-plan-repair.md`) | 2026-08-10 | 08-10 | The one primary milestone | **CURRENT** — new spine |
| 8 | MVP skill (`mvp-invariants`, ×2 copies) | 2026-07-08 | untouched | House rules fired on every edit | **STALE** — 2 dead file refs, 1 dead symbol, 4-layer model, J01–J19 |
| 9 | Journeys `README.md` 4-layer model | 2026-06-10 | 08-07 | (superseded layer model) | **STALE** — lines 144–183 conflict with EVIDENCE_MODEL |
| 10 | Owner Action Items | 2026-05-15 | 08-10 | Human/console blockers | **CURRENT** for TestFlight; predates M1 |
| 11 | Application Readiness Plan | 2026-08-09 | 08-09 | Accelerator submission gates | **STALE DATE** — drives to 08-15 early deadline the founder dropped; PearX regular is 10-04 |

Working plans (all `docs/working/`, all dated, all expiring — not registries):
thesis-to-experience audit (08-09), intentional convergence plan (08-10),
convergence-and-AI next round (08-10), canonical demo closure plan (08-10),
Lisbon runbook (08-10). These are execution documents downstream of M1, not
competing definitions of done. No action needed beyond their own expiry dates.

## 3. How we got here — the timeline

```text
06-06/06-10  STATUS.md + journeys README (4-layer model born)
06-30        journeys.yaml created · V1 scope DECIDED (pre-pivot promise)
07-08        mvp-invariants skill written (J01–J19, 4 layers)
08-06        PIVOT — lived-experiences model adopted
08-07        Pivot reaches the evidence layer:
               · P01–P07 proof spine created
               · 7-layer EVIDENCE_MODEL created
               · J registry re-classified: 9 customer_regression /
                 8 assurance_pack / 11 historical
               · registry header: "J identifiers... are not the current
                 product-thesis spine"
08-09        Pivot reaches strategy + release tooling:
               · Demo Journey Canon (flagship 4-act demo, alpha scope)
               · v1-scope.yaml made machine-readable (scope NOT re-decided)
               · consolidation decision (10-doc authority table —
                 omits Demo Canon and Proof Spine)
08-10        M1 — Plan Repair written; STATUS.md refreshed to 28/28
```

The pattern: the pivot propagated **downward** (thesis → evidence tooling) and
**upward** (thesis → narrative), but never **sideways** into the June
artifacts — the V1 scope decision, the skill, the old layer model.

## 4. The collisions, precisely

### 4.1 V1 contract certifies historical journeys

08-07 taxonomy vs v1-scope `journey_ids` + `required_layers: [physical]`:

| V1 capability (IN) | Anchored on | Taxonomy says |
|---|---|---|
| Auth and onboarding | J01, J02 | **both historical** |
| Trip create/invite/roles | J02, J03, J04 | J02, J03 **historical** |
| Planning/proposals/revert | J01, J05, J06 | J01 **historical** |
| Post-trip Story + photos | J11 | **historical** |
| Expenses and settlement | J10, J12 | J12 **historical** |

The contract demands physical-device certification of journeys the registry
says exist to "preserve historical customer and regression coverage." That
certification effort is the single largest misdirected line item in the
current plan.

### 4.2 Demo-critical mechanisms have no contract

- `WEATHER_RESCUE_PROPOSALS_ENABLED` (M1 Act 1) — absent from v1-scope
- `GROUP_TRIP_MICRO_JOURNEY_ENABLED` (60-second cold demo) — absent
- `LOCAL_PLAN_DOGFOOD_ENABLED` (M1 Act 4) — absent
- `ambient` capability is OUT while M1 Act 4 needs
  `AMBIENT_COINCIDENCE_CANDIDATES_ENABLED` (listed under it)
- Act 1's producer `_produce_weather_rescue` lives in
  `backend/concierge/proactive.py`, an evidence path of the OUT
  `proactive-disruption` capability

### 4.3 Two layer models coexist

- journeys README lines 144–183: static trace / mock walk / backend canary /
  live dogfood (June, tooling-free)
- `EVIDENCE_MODEL.md`: contract / database / device_mock / persona_replay /
  staging / physical / ai_eval (August, backed by `journey_evidence.py`,
  receipts, and the promoted attestation index)

Only the second is executable. The first survives as prose and inside the MVP
skill.

### 4.4 Governance registry can't see the evidence layer

The 08-09 consolidation decision's authority table omits Demo Journey Canon
and the Product Proof Spine; `PRODUCT_PROOF_SPINE.md` and `EVIDENCE_MODEL.md`
declare no `source_of_truth_for`. The two documents that own "what proves the
thesis" are invisible to the mechanism built to prevent exactly this drift.

### 4.5 Corrections recorded this session

- "J08 currently fails" — **stale since 08-08** (`2b61d7980`); STATUS.md now
  records 28/28 (observed 08-10, `travel-agent b56b38823`).
- "Semantic privacy guard fails open" (`Group Chat Facilitator.md` §3/§5 W2)
  — **stale since 06-22** (`aee4c6dc0`); guard fails closed on all four paths.
- "Do not build group chat (§7.1)" (`multiplayer-strategy` §8) — cites an
  archived section that says something different; no canonical doc prohibits
  the decision room.

## 5. The target architecture — one spine, three supports

```text
                    M1 — Plan Repair  (docs/release/m1-plan-repair.md)
                    the ONE milestone: 4 demo acts + exit criteria
                          │
        ┌─────────────────┼──────────────────────┐
        │                 │                      │
  Demo Journey Canon   P01–P07 spine        EVIDENCE_MODEL (7 layers)
  what story + what    what proves the      what each receipt proves;
  it must communicate  thesis; per-act      evidence-attestations.json
                       proof mapping        is the only "done" ledger
                          │
        ┌─────────────────┴──────────────────────┐
        │                                        │
  J registry (28)                         v1-scope.yaml
  REGRESSION FLOOR — seeded replay        DARK-SURFACE BOUNDARY —
  only; taxonomy governs; physical        which flags stay off; no
  cert NOT required on historical Js      roadmap or promise semantics
```

Roles after consolidation:

| Artifact | Sole role | Stops being |
|---|---|---|
| M1 | The milestone. All prioritization questions resolve here | — |
| Demo Canon | Narrative + alpha scope | an implicit second milestone |
| P01–P07 | Thesis evidence contract | — |
| EVIDENCE_MODEL | The only layer vocabulary | — |
| J registry | Regression floor, replay-level | a certification target |
| v1-scope | Dark-surface guarantee for store release | a roadmap, a promise, a cert driver |
| MVP skill | House rules, rewritten to the above | a stale 4-layer J01–J19 artifact |

## 6. Execution plan

### Phase A — rulings (founder, ~1.5h, blocks everything)

1. **A1.** Adopt the 7-layer EVIDENCE_MODEL as the only layer model; retire
   the README 4-layer prose (replace lines 144–183 with a pointer).
2. **A2.** Rule the three unclassified flags into v1-scope (proposal:
   weather-rescue PARTIAL/allowlisted; micro-journey PARTIAL/internal;
   local-plan PARTIAL/dogfood).
3. **A3.** Split `ambient` into `ambient-broad` (stays OUT) and
   `relationship-opening` (M1-scoped, dark until P06 anchors exist).
4. **A4.** Drop `required_layers: [physical]` from v1 capabilities anchored on
   `historical` journeys; physical certification moves to M1 acts (P-proofs).
   J04/J05/J10 two-device lane stays (they are assurance/customer tiers).
5. **A5.** Replace the v1 `promise:` field with a pointer to Product Thesis.

### Phase B — mechanical edits (~2h, delegable)

6. **B1.** Add M1, Demo Canon, and Proof Spine to the consolidation decision's
   authority table; add `source_of_truth_for` to PRODUCT_PROOF_SPINE.md and
   EVIDENCE_MODEL.md.
7. **B2.** Add the J↔P join table (capability → J ids → P ids) to the proof
   spine, promoting the existing prose mapping.
8. **B3.** Rewrite `mvp-invariants` skill: 7 layers, J01–J28 + P01–P07 + M1
   triggers, live canonical-writer paths (replace
   `build_and_persist_proposal` / `change_proposals.py` /
   `plan_edit_commit.py` with current gateway symbols), Experience/Plan/Move
   language. Delete or symlink the `.agents` copy.
9. **B4.** Fix the two remaining stale claims: `Group Chat Facilitator.md`
   fail-open lines (§3, gap C, W2) and `multiplayer-strategy` §8 group-chat
   line.
10. **B5.** Update `pearx-w27/application-draft.md` `target_submission` to the
    regular-deadline plan; annotate the Application Readiness Plan's 7-day
    schedule as superseded by M1's dates.

### Phase C — the only new engineering commitment

11. **C1.** Nothing new. M1's act table already owns the build order
    (F1–F5 doorway closure → flag flips → device receipts → P06 anchors).
    Working plans in `docs/working/` execute under M1 and expire on their own.

### What is explicitly NOT done

- No rewrite of the 28 J-tests or their fixtures.
- No new milestone documents beyond M1.
- No renaming of J ids or Maestro flows (107 flows keep their anchors).
- No v1-scope deletion — it remains the store-release dark-surface contract.

## 7. Success test

After Phases A+B, these questions must each have exactly one answer and one
authority:

| Question | Answer lives in |
|---|---|
| What is the milestone? | M1 — Plan Repair |
| Is X done? | evidence-attestations.json (promoted receipts only) |
| What story do we demo? | Demo Journey Canon §13 |
| What proves the thesis? | P01–P07 |
| What layer is this evidence? | EVIDENCE_MODEL (7 layers) |
| Can this flag be lit? | v1-scope.yaml (post-A2/A3/A4) |
| Did we break something old? | J seeded replay (28/28 floor) |

If any question has two answers after this pass, the consolidation failed and
the second answer should be deleted, not reconciled.
