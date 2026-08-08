---
doc_type: contract
status: active
owner: product-engineering
created: 2026-08-07
last_verified: 2026-08-07
why_new: Defines the small product-thesis proof spine independently from the historical J regression registry.
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

- J04 protects the privacy boundary used by P01/P03/P04.
- J05 and J06 protect mutation and cross-surface coherence used by P01/P03.
- J13, J15, and J16 protect failure, reversal, and data-lifecycle boundaries.
- J08 and J22 are retained regressions relevant to future P07 rescue work.

No P proof is physical-device certified by this document. Consult run receipts
for revision-specific execution evidence.
