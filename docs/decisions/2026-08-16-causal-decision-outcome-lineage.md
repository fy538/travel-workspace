---
doc_type: decision
status: accepted
owner: founder / engineering
created: 2026-08-16
decided: 2026-08-16
why_new: Give judgments, group decisions, domain actions, occurrences, outcomes, and later learning distinct references so every supported family can share proof without sharing private content or domain ownership.
supersedes: []
source_of_truth_for: [causal-decision-outcome-lineage]
---

# Use content-free causal lineage across decision families

## Context

The repository has decision records, action receipts, proposal decisions,
occurrence artifacts, outcomes, and learning admission contracts. Several use
the word `decision` for different events, while the learning registry has little
production adoption. Copying all of them into one universal event or agent
would erase authority and privacy boundaries.

## Decision

Every newly integrated consequential family uses distinct typed references:

```text
opening_id
judgment_id
domain_decision_ref
action_receipt_ref
occurrence_ref
outcome_ref
learning_application_ref
```

The content-free reference types extend `backend/core/decision/models.py` and
the existing action/learning contracts. Specialist domains retain their
writers, state machines, payloads, and transaction boundaries.

### Required semantics

- A `judgment_id` identifies Vesper's evaluated choice, including abstention.
- A `domain_decision_ref` identifies an accepted proposal, consent, or other
  authoritative human/domain decision.
- An `action_receipt_ref` identifies an attempted or applied domain command.
- An `occurrence_ref` identifies what is known to have happened.
- An `outcome_ref` identifies an evaluated consequence or reflection.
- A `learning_application_ref` identifies an admitted use of prior evidence in
  a later decision, including deliberate non-application.

No reference implies the state of another. Callback success is not domain
completion; proposal acceptance is not occurrence; occurrence is not a durable
preference; dismissal is not correction.

## Family adapters

Each registered decision family names:

- detector/opening producer;
- context compiler and privacy boundary;
- deterministic vetoes and authority class;
- judgment producer;
- treatment policy;
- canonical domain command and receipt reader;
- occurrence/outcome observer;
- learning admission store;
- kill switch and release posture.

The first registered portfolio is place interpretation, movement intervention,
ambient/Home attention, notification treatment, private disruption, shared Plan
repair, encounter confirmation, and later-occasion application.

## Migration

1. Wrap current `DecisionRecord` identifiers without rewriting history.
2. Add adapters for one family at a time and emit lineage in shadow.
3. Reconcile callbacks to canonical domain readback.
4. Admit learning only through existing governed store writers.
5. Remove overloaded identifiers only after historical readers and analytics
   have migrated.

## Rollback and compatibility

Family adapters and shadow lineage can be disabled independently. Historical
records keep their original IDs and gain only explicit compatibility wrappers;
the system must not infer missing occurrence or outcome edges.

## Proof gates

- every supported family passes ownership, contract, domain integration,
  adversarial lifecycle, and surface-readback levels;
- retries and duplicate callbacks produce one canonical action lineage;
- correction or revocation invalidates or annotates later applications;
- private evidence can change judgment without entering shared lineage;
- learning application records both use and deliberate non-use;
- no general coordinator receives domain mutation authority.

## Non-goals

- One event table for all domains.
- Replacing domain state machines.
- Learning from unconfirmed inference or interface dismissal.
- Requiring every family to share one model or release schedule.
