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

## Database authority slice

The second slice replaces the contract-only seam with a database-backed
canonical authority assembled from normalized itinerary, participation,
policy, branch, protection, provider-saga, booking, expense, stay, history,
place, people, lifecycle, and Memory-readiness facts. It does not read Folio.

The authority now:

- hydrates day/block revisions, subject lineage, participation scope,
  ownership, structural role, branch topology/participants/revisions,
  protection, and fail-closed server capabilities;
- retains the complete IR-10 provider-saga projection and IR-11 history page
  instead of rebuilding either from client-facing summaries;
- emits one deduplicated Needs-attention projection consumed by Details and
  available unchanged to later Bookings and shell consumers;
- preserves distinct event, stay, transport-leg, provider-booking, expense,
  place, and history identities with contextual/comprehensive exact-return
  links;
- hashes viewer, lifecycle-affecting projections, objects, links, people,
  Memory readiness, provider/history facts, and source states into a stable
  projection version; and
- degrades provider/history sources behind transaction savepoints, while
  incomplete policy facts produce denied capabilities and an explicit
  degraded capability source instead of permissive guesses.

`TripPlanState` and `TripMapState` expose the same additive authority behind
`ITINERARY_READ_MODELS_V2`; neither was replaced with another Plan/Map model.
`GET /api/trips/{trip_id}/details-state` is separately gated by
`TRIP_DETAILS_STATE_V2` and composes the fixed factual index from that
authority. Routing recommendations remain disabled.

Database evidence covers stable repeated projection versions, event↔expense
and stay↔expense identity/link paths, transport lineage, Details row counts,
and exact Plan/Map authority equality. Provider attention and canonical history
also prove one shared operation identity. This slice originally closed with 97
targeted tests passing.

## Final exit-gate closure

IR-12 is complete on 2026-07-13. The final slice adds:

- viewer-scoped authority access, current-member filtering for block and branch
  participation, departed-viewer denial, and account-deletion absence;
- privacy-safe limited Details rows for private stays, masked expenses, and
  provider details, with provider references/revisions restricted to the
  authorized controller;
- optional-source transaction savepoints for stays, expenses, bookings,
  provider truth, history, and Memory, so Sparse/partial reads preserve the
  plan and report explicit degraded source status;
- first-class generic and saga-backed booking projections, including event and
  lineage identity, Bookings group, itinerary commitment metadata, expense,
  provider-detail permission, continuation/attention, history operation, and
  saga identity;
- block-level booking identities/groups sourced from those same booking
  projections rather than reconstructed by Plan or Map;
- comparable List, Map, Details, Chat-attachment, Changes, and Bookings
  observer snapshots carrying one projection version, object identities,
  attention IDs, and history operation IDs;
- live Folio compatibility measurement against the canonical projection
  version plus a compatibility-only entry-readiness handoff; legacy facets
  remain explicitly degraded and Folio is still not an authority;
- backend-real completed-record, meaningful-Memory, and cancelled-record
  fixtures with routing still fixed off; and
- the independently gated, membership-scoped Details State route.

Exit evidence proves:

- stable event↔expense, stay↔expense, event↔booking, transport-lineage, and
  contextual/comprehensive identity paths;
- exact Plan/Map canonical equality and one-version agreement across all six
  IR-12 observer surfaces after a canonical operation;
- IR-11 branch group/branch revisions, owner, participants, and block branch ID
  survive as explicit projection facts;
- a real Replace-and-rebook pending state supplies one booking/history/
  attention operation identity, then its settled provider transition advances
  itinerary and Bookings metadata and clears attention without duplicating
  history;
- organizer/member projections differ only where privacy or capability facts
  require it, and a departed/deleted member is absent; and
- a failed optional expense source produces a partial Sparse Details response
  without losing the canonical plan.

Final regression evidence is 345 passing itinerary, provider, history,
compound, Plan, Map, Details, Folio, and route tests. Ruff and diff checks pass;
targeted mypy reports no IR-12-file errors (the repository retains 13 unrelated
baseline errors in six existing files).

No frontend shell, `TripFolioHome` expansion, alternate Plan/Map model,
post-trip routing, or IR-13/IR-16 UI behavior is included. The stale
medium-sheet Trip Details and unconditional Memory-default language identified
above remains a synchronization gate before IR-13 exposure.
