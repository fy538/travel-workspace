---
doc_type: working
status: active
decision_status: implemented
owner: Integration
created: 2026-09-07
last_verified: 2026-09-07
expires: 2026-10-07
why_new: Records the September 7 execution receipts for the connected Source request, exact result, stop, and Home/Places receiving batch.
supersedes: []
depends_on:
  - complete-system-integration-roadmap-2026-09-05.md
  - source-request-result-control-mapping-2026-09-07.md
---

# Connected Source value — execution receipt (2026-09-07)

This receipt is the implementation companion to the [complete-system
integration roadmap](complete-system-integration-roadmap-2026-09-05.md). It
records what landed, what was verified locally, and what remains gated. It does
not activate the worker or claim native evidence.

## Landed packages

| Package | Receipt | Commit |
| --- | --- | --- |
| SP-2a callback repair | The resolver's workflow-fenced completer accepts the orchestration deadline, verifies it is unchanged, and forwards the authoritative value. A regression exercises the workflow wrapper and canonical readback; focused continuity/canonical/worker/Postgres tests: 54 passed. | `86f04589` — `fix: forward source work deadline through fenced completion` |
| SP-0a request/result/control mapping | Existing Source work-item fields, missing exact-commission fields, request/reuse/result identity distinctions, and truthful lifecycle states are documented without inventing a second store. | `51fc6c9` — `docs: map source request result and control boundaries` |
| SP-1b exact result binding | Canonical Source execution computes a deterministic production digest; the completion receipt can carry a typed versioned result reference; an owner-only result route reopens the retained version without current Home/Places ranking or acquisition. Replaced/expired results return unavailable. Exact reads now revalidate a referenced Places context before serving. | `381bbba29` — `feat: bind exact source result identities`; `7d8552f29` — `fix: revalidate source context on exact reads` |
| SP-2b effective stop | Source-only cancellation uses a transaction-time actor/type/revision fence, records the applied command, cancels the workflow atomically, and remains behind the existing shared workflow-control flag. Generic steer/pause/resume/handoff semantics remain intent-only. | `1447eeccd` — `feat: apply source workflow cancellation` |
| Contract publication | The full OpenAPI snapshot and active projection include the dark owner-only result route; the operation policy declares it dark with no mobile consumer. | `cf4ee23` — `chore: publish exact source result contract` |

## Existing receiving evidence consumed

No new Home/Places producer or store was introduced. The existing prepared
read path already composes eligible retained Source value into both Home v2 and
Places v2/runtime through `root_composition._prepared_source_contribution`:

* `59f323b31` provides provider-free prepared Source admission;
* `ea816526d` carries verified Place facts through root delivery;
* `tests/api/test_root_composition_service.py` and
  `tests/api/test_practical_root_delivery.py` cover bounded, read-only
  composition; and
* `backend/core/place_content_sources.py` plus its tests provide the public
  content owner/ref/revision/current-state receiving boundary.

The integration implication is deliberate: private exact requester recovery,
ordinary Home/Places ranking, and public Content supply remain distinct owners
that can converge at the existing typed receiving boundary. A private Source
result is not automatically public content, a Life artifact, a notification,
or an action.

## Validation

Focused local suites passed during this batch:

* 114 tests across workflow API/DB, Source continuity, canonical executor,
  worker, serving, workflow, and Source storage;
* the route pre-commit gates including route-auth, response-model, import-cycle,
  and status-guard checks;
* `make contract-check` confirmed the OpenAPI snapshots and active projection,
  but reports one inherited generated-TypeScript enum-order mismatch in
  `travel-app/utils/api/schema.gen.ts` (`low | medium | high` versus
  `high | medium | low`). The new dark result route is not in the active mobile
  projection, so no mobile consumer was added.

## Still gated / not claimed

1. The current Source request owner still cannot express an exact commissioned
   subject set without a real authenticated request owner; the mapping document
   intentionally leaves that contract-sensitive extension proposed.
2. The worker remains dark. No queue registration, provider activation, paid
   call, or ordinary GET acquisition was added.
3. Exact result lookup still requires the retained row and current Source/
   context custody; replacement or expiry is truthfully unavailable rather
   than an archival promise.
4. Public Content receiving exists as a canonical owner boundary, but a broad
   public recommendation supply job and its coverage/evidence portfolio are
   not implemented by this batch.
5. Native Home/Places rendering and consumer value are not evidenced here, per
   the current engineering instruction.

## Next checkpoint

Run one real local end-to-end fixture through explicit request → canonical
Source executor → durable production/readback → exact result route → Home and
Places receiving, then exercise cancellation against the same workflow. Keep
the worker dark and use fixture provider/owner material. This checkpoint should
be followed by a reassessment before any public preparation or mobile consumer
activation.
