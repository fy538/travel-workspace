---
doc_type: decision
status: accepted
owner: founder / engineering
created: 2026-08-16
decided: 2026-08-16
why_new: Separate why Vesper considered intervening, what it judged, and how it chose to express or suppress that judgment across Home, Chat, Place, Plan, and push.
supersedes: []
source_of_truth_for: [opening-request-contract, treatment-decision-contract]
---

# Separate openings, judgments, treatment, and recipient lifecycle

## Context

Current producers can independently create Home cards, chat artifacts,
notifications, movement guidance, proposal nudges, and ambient opportunities.
`AttentionCase` is a credible recipient lifecycle, but it often begins after a
producer has already chosen a surface. That makes silence, suppression,
cross-surface deduplication, and causal comparison difficult to prove.

## Decision

Converge on this content-free causal boundary:

```text
OpeningRequest -> ContextManifest -> JudgmentRecord -> TreatmentDecision
                 -> optional AttentionCase -> domain action or projection
```

These contracts extend `backend/core/decision`; they do not move detection
logic out of specialist domains and do not make every answer a notification.

### `OpeningRequest` v1

Required fields:

- stable `opening_id` and idempotency key;
- trigger family, source reference, observed time, and expiry;
- actor, intended audience classification, and subject references;
- optional `PlanRevisionRef` and `EntityRef` values;
- requested decision family;
- `initiation="asked"|"system"`.

An opening asserts only that evaluation is warranted.

### `ContextManifest` v1

Contains admitted source references, revisions, freshness and precision
classes, unknowns, authority snapshots, audience, and privacy class. Private
values remain in an ephemeral family-specific frame and never enter the
manifest.

### `TreatmentDecision` v1

Required fields:

- the judgment reference and recipient;
- exactly one selected treatment from `silence`, `in_context`, `home`, `place`,
  `plan`, `chat`, `shared_proposal`, or `push`;
- suppressed alternatives with reason codes;
- interruption eligibility and budget decision;
- projection reference, presentation expiry, and policy version;
- optional `attention_case_id` when lifecycle coordination is required.

The types belong in `backend/core/decision/models.py` until package size forces
a dedicated `backend/core/treatment` package. Attention policy remains owned by
the notification/attention subsystem.

## Migration

1. Register all current producer families without changing dispatch.
2. Emit shadow openings and treatments beside existing results.
3. Require shared causal identity before a family can project to more than one
   surface.
4. Move selection into treatment policy one family at a time.
5. Remove producer-owned surface selection only after parity, silence, expiry,
   and dedupe evidence passes.

## Rollback and compatibility

Shadow emission is independently disableable by family. Existing delivery and
Home paths remain canonical until their family passes release gates. Legacy
records may be observed but cannot be fabricated into causal lineage after the
fact.

## Proof gates

- one opening cannot produce duplicate active Home and push treatments;
- silence and every suppressed alternative are observable without private
  context;
- expiry cancels stale projections coherently;
- an already-visible owner surface lowers interruption eligibility;
- asked responses are not accidentally treated as proactive interruptions;
- treatment dismissal remains distinct from domain completion and learning.

## Non-goals

- A global background agent.
- Moving domain detection or mutation into the treatment layer.
- Sending new push behavior in the first migration slice.
- Persisting private decision frames.
