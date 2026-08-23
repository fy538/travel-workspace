---
doc_type: working
status: active
owner: founder / product / engineering
created: 2026-08-23
last_verified: 2026-08-23
expires: 2026-09-22
why_new: Make the durable writer, readers, lifecycle owner, and migration seam explicit for every canonical product noun before the multi-journey engine work expands.
supersedes: []
source_of_truth_for: [canonical-authority-register]
---

# Canonical authority register

This is the M0 working register for durable product nouns. A noun has one
durable writer even when it has many read projections. Adapters may temporarily
write legacy stores, but the adapter and its deprecation condition must be
named here. A UI, cache, vector index, or graph summary is never an authority.

The register is intentionally honest about current seams. “Target authority”
is the destination for M1–M5 convergence; “current authority” describes what
the code actually writes today.

| Noun | Current authority | Current readers/projections | Target authority | Lifecycle owner | Seam / risk | Status |
|---|---|---|---|---|---|---|
| World / Place | Existing Place, venue, site, accommodation identity tables | Places, Plans, Trip blocks, Map/deep links, saved entities | Canonical typed `EntityRef` plus resolution/redirect ledger | Place identity service | Graph `world_entities` binds through `graph_identity_bindings`; unresolved graph candidates remain provisional; see [ADR](../decisions/2026-08-23-canonical-place-authority-bridge.md) | M0 bridge landed; backfill/deep-link parity remains |
| Source / Artifact | Source objects, uploads, artifact interpretation records | Home intake, Vesper context, receipts, memories | Admission/source authority with immutable artifact and interpretation lineage | Admission engine | Ingestion paths still vary by surface | M1 contract |
| Relationship | Social circles, memberships, handoffs, invitations, conversations | Social surfaces, occasions, shared plans, notifications | Relationship kernel with explicit participant/authority edges | Relationship engine | Legacy circles and new handoffs coexist; flag must be real | M0/M3 |
| Plan | Legacy Trip/Plan models and graph Plans | Home, Vesper, booking, itinerary, shared planning | Plan authority with revisioned commands and projections | Planning engine | Trip-specific readers and graph Plans are not yet unified | M1/M5 |
| Occasion | Occasion/occasion_members plus Trip event slices | Life, invitations, attendance, shared context | Occasion authority with organizer/delegation and lifecycle policy | Occasion engine | Graph transfer is DB-tested; Trip/Occasion parity and full correction semantics remain | M0/M3 |
| Commitment | Bookings, holds, proposals, commitment tables | Plan, Occasion, notifications, receipts | Commitment authority with explicit capability/expiry | Commitment engine | Several provider and Trip-specific paths | M1/M5 |
| Lived Reality | Events, outcomes, memories, consequence records | Life, Home return, relationship history, place context | Outcome/occurrence authority with correction and provenance | Reality engine | Graph and legacy event stores need lifecycle parity | M0/M5 |
| Attention | Opening requests, attention projections, notification deliveries | Home, Vesper, Places, notification surfaces | Opening/attention authority with expiry and delivery receipts | Attention engine | Graph→Lived `CanonicalOpening` adapter and typed destinations landed; one persisted authority, cross-surface controls, telemetry, and flag coverage remain | M0/M4 |
| Receipt | Action receipts plus domain-specific booking/ingestion receipts | Confirmation, retry, audit, privacy/export surfaces | Shared receipt envelope with domain payload and viewer policy | Command/receipt spine | Legacy Trip receipt reads needed owner filtering | M0/M1 |
| Projection | Mobile read models, clean graph summaries, caches, vectors | Four roots and contextual cards | Rebuildable projections keyed to the authorities above | Projection/replay system | Projections can currently imply authority when source is unresolved | M1/M6 |

## Rules for using this register

1. A new durable table or route must name its noun and writer before merge.
2. A read model must carry source authority, revision/version, and freshness;
   it cannot silently become a second writer.
3. Cross-domain account export, deletion, residual scans, and correction tests
   must include every table that stores a user id or a graph/relationship
   reference. The M0 lifecycle registry is the current implementation seam.
4. A migration is complete only when old readers are removed or proven to read
   the target authority through an adapter.
5. “Not yet verified” is a valid status. It is safer than declaring a surface
   coherent because its route or card exists.

## M0 verification checklist

- [x] Legacy private Trip receipts filter by viewer.
- [x] Graph/relationship tables are included in lifecycle enumeration.
- [x] Social Circle kill switch exists, is registered, and is enforced.
- [x] Graph/Place identity conflict is recorded as an accepted ADR.
- [x] Identity-binding ledger and graph-to-Place resolver implemented (`graph_identity_bindings`, `xgraph16`, projection/anchor fail-closed public reads).
- [x] Postgres export/deletion/residual tests cover the current graph and
  relationship user-owned records.
- [x] Machine-readable reachability report runs in the five contract gates
  (`make m0-reachability-report`).
