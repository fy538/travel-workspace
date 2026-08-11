---
doc_type: contract
status: active
owner: product-engineering
created: 2026-08-07
last_verified: 2026-08-10
why_new: Defines the small product-thesis proof spine independently from the historical J regression registry.
source_of_truth_for: [product-proof-spine, p-series-evidence-requirements]
---

# Product proof spine

The current product model is **Experience → Plan → Trip**, with a Move as the
smallest useful unit. The product proof is not that every historical trip
workflow remains available. It is that a real occasion becomes a viable shape
that happens, and that the next similar occasion takes less work or leads to a
better-grounded decision.

The P registry is deliberately separate from J01–J28. A J test protects a
regression or an assurance boundary; a P test proves the present thesis.

| Proof | Promise | Required initial evidence | Current state |
|---|---|---|---|
| P01 | A real occasion becomes an accepted Move or local Plan. | Contract, database, device-mock | Active; device flow not yet recorded. |
| P02 | The decision is spatially and operationally credible. | Contract, database | Active. |
| P03 | A lived experience can be confirmed or corrected accurately. | Contract, database, device-mock | Active; device flow not yet recorded. |
| P04 | A second similar occasion uses permitted prior evidence. | Contract, database, AI evaluation | Active; AI evaluation not yet recorded. |
| P05 | A participant can contribute through a thin, zero-install handoff. | Contract, database, device-mock | Dark: product surface is not offered. |
| P06 | Consent, privacy, and deliberate silence are respected. | Contract, database, device-mock, AI evaluation | Dark: dedicated product proof is not yet offered. |
| P07 | The product can rescue a plan after a real disruption. | Contract, database, device-mock, staging | Dark: dedicated product proof is not yet offered. |

## P01 — occasion to accepted Move or Plan

Starting from a concrete local occasion, the user enters through the real
product entry point, sees a viable local shape, and accepts or changes it. The
result must be idempotent, must not invent travel/lodging semantics, and must
return on the appropriate Plan surface.

Negative oracle: confirmation cannot create duplicate moves or expose a
private input in a shared surface.

## P02 — spatially credible decision

The product must not present an impossible sequence as a viable plan. Routing,
time, place, provider freshness, fallback behavior, and visible rationale are
part of the oracle.

Negative oracle: unavailable provider facts must become an honest fallback,
not plausible fabricated certainty.

## P03 — Plan to lived outcome

The product proposes outcome evidence privately. The user can confirm, correct,
or reject it. A correction replaces or invalidates the prior interpretation,
and any later learning remains traceable to the evidence that justified it.

Negative oracle: an outcome cannot silently become a shared group claim.

## P04 — second occasion compounds

Run two related occasions for the same seeded persona. After a confirmed first
outcome, the second occasion may use permitted evidence from the first. Tests
assert provenance, privacy, and reduced required input—not the subjective claim
that a recommendation is universally “better.” Agent-quality judgment belongs
in repeated AI evaluations.

## Dark proof policy

P05–P07 are visible debt, not implied coverage. A dark proof may become active
only when its product surface is reachable and its contract, fixture, and
evidence requirements are added to `product-proofs.yaml`.

## Relationship to J assurance packs

The J and P registries answer different questions and are deliberately not
renumbered onto each other. J asks *did we break something that used to work*;
P asks *does the current thesis hold*. The join below exists so the two can be
read together — it is a coverage map, not an equivalence.

| Proof | M1 act | J journeys that protect its boundaries | J tier |
|---|---|---|---|
| P01 | secondary cold demo | J05, J06 (mutation, cross-surface coherence) · J07, J14 | assurance · customer/historical |
| P02 | Act 2 | J07 (place-to-action) · J08 (live plan/map agreement) | customer_regression |
| P03 | Act 4 | J04 (privacy boundary) · J05, J06 (mutation) · J11 (memory control) | assurance · historical |
| P04 | Act 4 | J04 (privacy boundary) · J17 (cross-trip recall) | assurance · holistic |
| P05 | Act 3 | J02, J03 (invite, membership) · J18 (signed-out join) · J24 (agency governance) | historical · customer |
| P06 | cross-cutting | J04 (privacy) · J09 (proactive routing) · J15, J16 (reversal, data lifecycle) | assurance |
| P07 | Act 1 | J08, J22 (retained rescue regressions) · J05, J06 (proposal path) | customer · assurance |

Reading rules:

1. A green J does **not** advance a P. J evidence is seeded replay at contract
   and database layers; P evidence requires the layers named in
   `product-proofs.yaml`.
2. A red J **does** block the P rows that depend on it — a broken mutation path
   invalidates any proof asserting a governed change.
3. J journeys with no P column entry (J01, J10, J12, J13, J19, J20, J21, J23,
   J25–J28) are pure regression floor. They are not certification targets for
   M1 and should not accrue device evidence on M1's account.

Milestone authority for the act column is
[M1 — Plan Repair](../release/m1-plan-repair.md).

No P proof is physical-device certified by this document. Consult run receipts
for revision-specific execution evidence.

## AI evaluation task bank

The backend owns 24 replay-safe tasks across P01–P04 and the future P06
consent/silence risk. Each task grades observed effects, terminal state,
evidence references, and shared text; it does not grade fluent prose alone.
Privacy and silence tasks require three independent observed trials. The runner
accepts adapter-produced trial JSON and never calls a model or provider itself:

```bash
cd travel-agent
.venv/bin/python -m eval.product_proofs.run_eval --trials /path/to/observed-trials.json
```

An absent trial is a failed evaluation task, not a pass. The task bank is not
itself a claim that an agent was evaluated; record an `ai_eval` receipt only
after a real adapter has produced and graded observed trials.
