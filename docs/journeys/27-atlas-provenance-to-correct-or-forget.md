---
doc_type: canon
status: active
owner: founder / engineering
created: 2026-07-18
last_verified: 2026-07-18
why_new: Memory provenance and correction are a primary trust journey rather than a secondary candidate-review step.
source_of_truth_for: [journey-J27]
---

# 27 — Atlas Provenance to Correct or Forget

## Product Promise

A traveler can trace a learned claim to evidence and correct, soften, forget, or
disable it without deleting the underlying travel record.

## Canonical User Story

As a traveler, I want to understand and change what Vesper learned, so that
personalization remains accountable to me.

## Starting State and Surfaces

- Any Atlas stage: learned facts, nothing learned, or learning disabled.
- Routes: `/atlas/memory`, data receipt, artifact learning, privacy/signal controls.
- Source contract: Atlas `J-A4`; J16 owns account-wide deletion/export.

## Canonical Steps

1. Open Your Memory and inspect synthesis/evidence.
2. Open the complete receipt and originating source.
3. Correct, soften, forget, or change the learning control.
4. Return to Memory, artifact, and Home; all reflect the same decision.
5. Confirm the underlying travel record remains unless separately deleted.

## Required Branches

| Branch | Path | Required evidence |
|---|---|---|
| `J27.B01` | Nothing learned versus learning disabled | `FE`, `BE`, `VIS` |
| `J27.B02` | Evidence and receipt provenance | `FE`, `BE`, `VIS`, `LIVE` |
| `J27.B03` | Correct/soften learned claim | `FE`, `BE`, `VIS`, `LIVE` |
| `J27.B04` | Forget claim but retain source record | `FE`, `BE`, `VIS`, `LIVE` |
| `J27.B05` | Originating artifact/Home reconcile | `FE`, `BE`, `VIS` |
| `J27.B06` | Learning/photo controls and failed retry | `FE`, `BE`, `VIS` |

## Must Never Happen

- A forgotten fact remains active elsewhere.
- Correction deletes trip history or source media.
- Confidence scores replace evidence.
- Nothing learned is mislabeled as learning disabled.

## First Automation Target

Promote `atlas-journey-memory-forget-return.yaml`; add correction parity across
Memory, receipt, originating artifact, and Home against an ephemeral persona.

## Certification

- The canonical `journey-27-mock-walk.smoke.test.tsx` follows one sourced claim from active to disputed
  to forgotten and proves the artifact is unchanged and still listed.
- Mature receipts prioritize artifact-backed signals ahead of synthesized DNA,
  so a full five-line DNA summary cannot hide the claims with source-specific
  Soften, Correct, and Forget controls.
- The Postgres scenario exercises the real receipt, signal mutation, artifact,
  and artifact-signal routes. It also verifies the observation is inactive and
  the durable correction exclusion is `forgotten`.
- Maestro flow `65-journey-27-memory-provenance-correct-forget.yaml` covers the
  honest cold start, receipt evidence, artifact soften/forget, retained-source
  reopen, photo controls, cached failure, and healthy retry.
- `persona-cert:J27` creates a disposable traveler, source artifact, signal, and
  observation; it performs correction and forgetting through real routes, then
  removes the entire fixture without touching Mara or Elif's durable memory.
