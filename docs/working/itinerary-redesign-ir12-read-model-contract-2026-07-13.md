---
doc_type: working
status: active
owner: backend / product
created: 2026-07-13
last_verified: 2026-07-13
expires: 2026-08-12
why_new: Record the IR-12 target read-model authority, Folio compatibility boundary, and governing-document synchronization gate.
source_of_truth_for: [itinerary-redesign-ir12-read-model-contract]
---

# IR-12 — Coherent read-model contract

IR-12 is backend read-model work only. The itinerary remains the canonical
single-trip home before and during travel. The future Ledger/compact chrome and
full-screen Trip Details are IR-13 consumers; they are not implemented here.

The target authority is one versioned typed trip graph shared by Plan, Map,
Details State, Bookings, Needs attention, and canonical history. Event, stay,
transport leg, provider booking, expense, place, and history records retain
separate stable identities. Contextual and comprehensive destinations point to
the same object identity and differ only in entry and exact-return requirements.

Trip Details has a fixed factual order: Identity, People, Stay, Transport,
Costs, Bookings, Changes/History, Settings. Rows carry explicit calm,
attention, or absence state; viewer visibility; typed destinations; and
server-authored capabilities.

Folio remains `compatibility_only`. Its lifecycle, urgency, facets,
source-status, partial-data, and Memory handoff are measured independently.
Folio is not an input to the target graph and cannot become the new shell's
underlying authority merely by reaching field parity.

## IR-13 synchronization gate

The following older governing language is stale under the later 2026-07-13
Trip-shell convergence amendment:

- `travel-app/docs/surfaces/trip-itinerary/contract.md:178` and
  `travel-app/docs/audits/itinerary-interaction-ux-audit-2026-07-12.md:599`
  prescribe a medium-sheet Trip Details presentation. The accepted target is a
  full-screen, scrollable push.
- `docs/working/itinerary-interaction-business-logic-audit-2026-07-12.md:104`,
  `travel-app/docs/surfaces/trip-itinerary/contract.md:130`, and the UX audit's
  completed-trip rules prescribe an unconditional Memory default. The accepted
  target is hybrid: the completed record remains the fresh-entry face until
  meaningful Memory is ready; cancelled trips always retain the record.

Those documents must be synchronized before IR-13 exposes the target shell.
IR-12 may emit server-authored entry readiness and a recommendation, but routing
remains disabled until IR-16.

## Initial contract slice

The first implementation slice establishes:

- strict typed object/link/destination contracts and exact-return requirements;
- version and per-source partial-data envelopes;
- fixed Details State row contracts and Calm, Needs-attention, and Sparse
  fixtures;
- server-authored active/completed/cancelled entry readiness with routing fixed
  off; and
- explicit Folio field-parity/degradation reporting.

Database projection integration, List/Map parity, privacy proofs, provider and
compound/branch propagation, and route exposure remain subsequent IR-12 slices.
