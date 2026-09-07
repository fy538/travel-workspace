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
| SP-1b exact result binding | Canonical Source execution computes a deterministic production digest; the completion receipt can carry a typed versioned result reference; an owner-only result route reopens the retained version without current Home/Places ranking or acquisition. Replaced/expired results return unavailable. Exact reads now revalidate a referenced Places context before serving, validate digest shape, fail closed on owner-read/storage errors, and canonicalize unordered fields before hashing; worker regressions prove the digest is carried into the receipt. | `381bbba29` — `feat: bind exact source result identities`; `7d8552f29` — `fix: revalidate source context on exact reads`; `35c1b203f` — `fix: harden exact source result reads`; `90955883f` — `test: prove exact source result receipt binding`; `1961eebff` — `fix: canonicalize source result identities` |
| SP-1c exact-result independence and fail-closed context handling | Exact requester readback now uses the retained production seed's source/context coordinates instead of re-running current opportunity discovery or ranking. Its shared validation still rechecks owner custody, audience, expiry, represented time, current Opening state, and deterministic candidate expiry. The API route maps both Places-context and retained-result storage failures to the existing unavailable state rather than leaking a server error. Regressions prove discovery is not called and both read boundaries fail closed. | `fd08f68f4` — `fix(source): keep exact result readback independent`; `fb521f38d` — `fix(source): fail closed on context read errors`; `f2bf741a1` — `fix(source): fail closed on result read errors` |
| SP-2b effective stop | Source-only cancellation uses a transaction-time actor/type/revision fence, records the applied command, cancels the workflow atomically, and remains behind the existing shared workflow-control flag. Generic steer/pause/resume/handoff semantics remain intent-only. | `1447eeccd` — `feat: apply source workflow cancellation` |
| SP-2c terminal result semantics | The exact-result reader now distinguishes a completed `producer_silence` ending (`no_useful_result`) from a malformed or missing result identity (`unavailable`), and maps superseded workflows to an unavailable result without attempting regeneration. | `9c1eda6e9` — `fix(source): report terminal silence and supersession` |
| SP-2d bounded request admission | Authenticated clients can submit a strict, private, content-free request with a named purpose, subjects, Sources, root scope, represented clock and bounded expiry. The request is persisted through the existing workflow fence; malformed exact comparisons are rejected and disabled production returns a truthful unavailable response. | Backend `bc012aca2` — `feat(source): accept bounded preparation requests`; `40eb81b2a` — `fix(source): gate preparation on production rollout` |
| Contract publication and mobile recovery | The full OpenAPI snapshot and active projection include the request and owner-only exact result routes. Generated mobile types, HTTP methods, mock parity and focused transport tests consume both routes; the result read remains available for already-retained output while new production is separately gated. The shared result hook is root-scoped, does not read without a workflow identity, treats unavailable/failed outcomes as terminal, and polls only a pending result. The request hook submits the bounded body and invalidates only that exact root/result key; it never retries by creating a new request. | Workspace `f60f2e6`, `1434694`, `20d833a`; app `c9d208632`, `66d61f59c`, `15b38e18f`, `d874bb778`, `90b8ba7b5`, `c201457d3`, `c6300cc1e`, `b479c3289` |
| CV-3 Home/Places receiving | The tested receiving adapter is landed on backend `main` and the app's Entity checkout and clean app-`main` integration worktree. It preserves owner-backed composition, exact continuations, practical delivery, and return-token behavior without adding a new producer or screen family. | Backend `1146ae041`; app `f4401ef73` (Entity checkout) and `8bed6ca82` (clean `main` worktree) |

## Existing receiving evidence consumed

No new Home/Places producer or store was introduced. The existing prepared
read path already composes eligible retained Source value into both Home v2 and
Places v2/runtime through `root_composition._prepared_source_contribution`.
The parallel Content lane also landed an exact public Place-content source
handoff in `b0d5a80ca`; this is an owner/ref/revision receiving boundary, not a
broad public recommendation publisher:

* `59f323b31` provides provider-free prepared Source admission;
* `ea816526d` carries verified Place facts through root delivery;
* `tests/api/test_root_composition_service.py` and
  `tests/api/test_practical_root_delivery.py` cover bounded, read-only
  composition; and
* `backend/core/place_content_sources.py` plus its tests provide the public
  content owner/ref/revision/current-state receiving boundary (`b0d5a80ca`).

The integration implication is deliberate: private exact requester recovery,
ordinary Home/Places ranking, and public Content supply remain distinct owners
that can converge at the existing typed receiving boundary. A private Source
result is not automatically public content, a Life artifact, a notification,
or an action.

## Validation

Focused local suites passed during this batch:

* 114 tests across workflow API/DB, Source continuity, canonical executor,
  worker, serving, workflow, and Source storage;
* 304 tests across the integrated Home/Places composition, practical delivery,
  workflow API, Source projection, and Source storage packet;
* 69 focused backend tests across the merged Home/Places receiving and workflow
  packet;
* 46 focused mobile Home/Places/navigation tests plus TypeScript typecheck on
  the merged Entity checkout. The clean app-`main` integration worktree has no
  installed dependencies, so it was not re-run independently there;
* 6 public Place-content owner/receiving tests, including the exact handoff
  added by `b0d5a80ca`;
* the route pre-commit gates including route-auth, response-model, import-cycle,
  and status-guard checks;
* 22 focused backend workflow API tests, including request admission, strict
  exact scope validation and the production rollout gate;
* 85 focused mobile HTTP tests, including content-free request submission and
  owner-scoped exact result recovery;
* 2 focused mobile result-hook tests, including no-read-without-identity and
  explicit terminal recovery after a pending result;
* 1 focused mobile request-hook test, including exact-body submission and
  root-scoped result invalidation;
* `make contract-check` passed with the request/result routes in the active
  mobile projection, generated types synchronized, 370 facade entries
  classified, and the canonical place/Occasion checks green.

## Still gated / not claimed

1. The request owner now expresses an exact commissioned subject/Source set,
   but the production worker is still dark; acceptance is not evidence that a
   provider-backed result will arrive.
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
