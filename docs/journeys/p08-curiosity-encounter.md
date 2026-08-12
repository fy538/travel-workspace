---
doc_type: contract
status: active
owner: product / engineering
created: 2026-08-11
last_verified: 2026-08-11
why_new: Defines the smallest proof that Vesper helps a person experience a place more deeply, without expanding the product into a broad ambient feed.
related:
  - product-proofs.yaml
  - ../release/m1-plan-repair.md
  - ../../travel-agent/docs/product/Product%20Thesis.md
---

# P08 — Curiosity becomes a grounded encounter

## Claim

When a person expresses a curiosity, Vesper can select a sourced perspective
on a place, turn it into one feasible real-world Move, preserve that intent as
conditions change, and use the person's private reflection to improve a later
occasion.

This proves **interpretation joined to hospitality**. It does not prove
notification-led discovery, broad city coverage, a contributor marketplace, or
general-purpose learning.

## Canonical first run

One person opens Lisbon with the explicit curiosity:

> How do cities adapt to difficult terrain?

They select the approved lens on movement across Lisbon's hills. The resulting
Move contains at most three canonical anchors, one observation prompt per
anchor, current route/time/availability evidence, and enough buffer to remain
credible. If a relevant anchor becomes infeasible, the repair preserves the
terrain-and-movement inquiry rather than substituting a popular attraction.

After the person confirms the occurrence, they may privately record what they
noticed and the thread they would follow next. The next occasion can use that
private receipt only within its permission, freshness, and applicability
boundaries.

## Product rules

1. The first surface is pull-first: a dossier or explicit Vesper request.
   P08 does not permit notification delivery.
2. The lens, dossier, place identity, and curiosity reference travel as typed
   context. The server resolves all meaningful content from canonical ids.
3. A Move must be spatially feasible and evidence-backed. Unknown operational
   facts remain unknown; the product must not invent a route or opening.
4. The observation prompt invites attention; it is never presented as a fact
   about the user's experience.
5. Free-text reflection is private by default. It is not public place truth,
   group truth, or telemetry content.
6. A later occasion must explain its use of a reflection without quoting or
   exposing it outside the owner-scoped context.

## Acceptance evidence

| Layer | What it proves |
| --- | --- |
| contract | Lens identity survives the mobile handoff and canonical Move composition; privacy and repair invariants fail closed. |
| database | One confirmed personal outcome has a correct, retractable private reflection and can influence only a permitted second occasion. |
| device_mock | A person can complete Place → Dossier → Vesper → Plan/Map → reflection in one internal build. |
| human_outcome | The person can name something specific they noticed or learned that they would otherwise have missed; qualitative feedback does not describe the experience as intrusive homework. |

## Explicit non-goals

- No new top-level navigation, Curiosity feed, or universal place ontology.
- No autonomous generation or auto-publication of interpretations.
- No open contributor or local-expert network.
- No inferred curiosity written durably without an explicit user action.
- No ambient notification or geofence interruption.

## Promotion gate

P08 remains dark until all required layers contain revision-bound receipts. A
passing fixture, seeded replay, or hand-authored reflection is not human-outcome
evidence.
