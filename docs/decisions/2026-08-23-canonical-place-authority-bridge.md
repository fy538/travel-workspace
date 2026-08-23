---
doc_type: decision
status: accepted
owner: founder / engineering
created: 2026-08-23
decided: 2026-08-23
why_new: Close the identity gap between the established Place/Entity authority and the clean Experience Graph world_entities tables before graph-backed surfaces expand.
supersedes: []
source_of_truth_for: [canonical-place-authority-bridge, graph-place-identity]
---

# Canonical Place authority and the Experience Graph bridge

## Context

The accepted [Place identity and provenance](2026-08-08-place-identity-and-provenance.md)
decision defines typed `EntityRef` values as the application-facing identity.
The later Experience Graph introduced a separate `world_entities` table and
graph-local identifiers. Those identifiers are useful for graph ingestion and
relationship reasoning, but they currently have no mounted resolver to the
existing Place, venue, site, or accommodation readers.

Leaving both systems addressable would make a graph summary look authoritative
while deep links, correction, privacy, export, and deletion still operate on a
different object. That is an authority failure, not a harmless migration detail.

## Decision

1. Existing Place/Entity identity remains the canonical product authority for
   any object a user can save, plan, navigate to, share, correct, or revisit.
   Public APIs and durable cross-domain records use the typed `EntityRef`
   contract from the August 8 decision.
2. `world_entities` is an internal graph representation until an explicit
   identity binding exists. It may not be emitted as a public place reference,
   used as a deep-link target, or treated as a second canonical entity.
3. Every graph entity that can reach a user-facing surface must resolve through
   an identity-binding ledger:

   ```text
   GraphIdentityBinding {
     graph_entity_id: UUID
     canonical_ref: EntityRef
     method: direct | provider_match | reviewed | redirected | merged
     evidence: object
     confidence: number
     status: pending | accepted | rejected | superseded
     created_at: timestamp
     updated_at: timestamp
   }
   ```

   A pending or rejected binding can remain useful for private graph reasoning,
   but cannot be promoted into a shared projection.
4. Graph reads return the canonical `EntityRef` and a binding status. They do
   not return a graph UUID as a substitute. If no accepted binding exists, the
   response is explicitly an unresolved graph candidate and has no place
   navigation, booking, or shared-save authority.
5. Redirects and merges follow the existing canonical resolution/receipt
   policy. Feature code must not copy graph ids into Place foreign keys or
   perform ad-hoc row rewrites.

## Migration seam

The bridge is delivered in this order:

1. Add the binding model, uniqueness constraints, and resolver contract.
2. Backfill only high-confidence direct/provider matches with evidence.
3. Make graph summaries and openings use the resolver; unresolved items remain
   visibly provisional.
4. Add deep-link, correction, export, deletion, and replay tests across both
   stores.
5. Deprecate graph-local public identifiers after all consumers read the
   canonical reference.

No graph surface is considered production-ready until steps 1–4 are verified.

## M0 implementation evidence (2026-08-23)

The first trust seam is now landed. `graph_identity_bindings` and the
`xgraph16` migration provide explicit global/owner-scoped accepted bindings,
conflict checks, and a resolver that passes through the existing canonical
redirect policy. Projection and owner-scoped anchor reads expose
`canonical_entity_ref` plus `entity_binding_status`; unresolved graph
candidates are public-but-provisional and graph UUIDs are redacted at the API
boundary. The graph evidence table is physically separated from the mature
Trip `occurrence_evidence` table so both metadata authorities cannot silently
read the wrong columns.

High-confidence backfill, canonical deep-link/correction parity, and replay
coverage remain follow-through work for M1. They are intentionally not
represented as complete by this ADR.

## Non-goals

- This decision does not merge the two SQLAlchemy metadata objects immediately.
- It does not require rewriting historical graph records.
- It does not decide provider matching policy beyond requiring evidence and an
  explicit binding status.

## Acceptance tests

- A graph summary with an accepted binding deep-links to the canonical Place.
- An unresolved graph entity cannot be saved to a shared Plan or Occasion.
- Correct, export, deletion, and residual-reference audits cover both ids.
- A redirect/merge returns the same canonical `EntityRef` on retry.
