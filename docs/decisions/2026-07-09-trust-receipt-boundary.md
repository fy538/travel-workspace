---
doc_type: decision
status: accepted
owner: founder / engineering
created: 2026-07-09
decided: 2026-07-09
why_new: Preserve the consequential privacy and provenance boundary from the completed trust-receipts plan.
supersedes: []
---

# Decision: Separate public reasons from private influences in receipts

## Context

Vesper changes shared artifacts using personal, group, provider, and model-derived
inputs. A receipt must explain an action without leaking the private constraint or
person that influenced it.

## Decision

Receipts expose a privacy-safe public reason, stable references to the changed
artifact/event, and a correction or reversal path. Private influences remain in an
access-controlled projection and are never serialized into group-visible receipt
copy. Raw prompts and chain-of-thought are not provenance.

## Consequences

Receipt schemas and renderers must preserve the projection boundary. Debugging may
require privileged tooling, while ordinary users receive less granular attribution.
Corrections must propagate through derived read models.

## Revisit trigger

Supersede this decision only if a reviewed privacy model introduces explicit,
revocable consent for a different attribution boundary.
