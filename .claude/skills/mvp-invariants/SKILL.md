---
name: mvp-invariants
description: This project's house rules for shipping milestone-relevant code — apply this whenever touching an M1 demo act, a P-series proof (P01-P07), a canonical journey (J01-J28), any code that sends text or data to a group/notification/booking surface, any Plan/proposal/booking/expense/itinerary mutation, or when about to say something is "done," "shipped," "complete," or "certified." Also use when writing or reviewing code that composes a message visible to more than one Plan member, or when lighting a feature flag. This project has a real history of three recurring failure modes — private data leaking to a group, "done" claimed on green backend tests without a device receipt, and documents citing files or symbols that no longer exist — so treat this as required reading before any of the triggers above.
version: 2.0.0
---

# MVP Invariants — Travel Workspace

Six rules, each with a documented incident or repeated audit finding behind it.
This is the five-minute version; the linked authority owns the detail.

**Orientation:** the milestone is
[M1 — Plan Repair](../../../docs/release/m1-plan-repair.md). If work does not
serve one of its four demo acts, it is not this milestone.

## 1. "Done" requires a receipt at the right layer

There are **seven** evidence layers, defined by
[`docs/journeys/EVIDENCE_MODEL.md`](../../../docs/journeys/EVIDENCE_MODEL.md):
`contract` · `database` · `device_mock` · `persona_replay` · `staging` ·
`physical` · `ai_eval`.

A journey file or test name proves coverage is **defined**, never executed.
Execution claims come only from immutable receipts, and only promoted receipts
in `docs/journeys/evidence-attestations.json` count as current. A receipt is
`STALE` the moment any recorded revision differs from the checkout.

The only execution states are `PASS`, `FAIL`, `BLOCKED`, `UNRUN`, `STALE`.

**Why this project specifically:** at the last audit the attestation index was
empty while multiple documents described capabilities as shipped. "Backend
tests pass" and "device-validated" are different sentences.

**Apply it:** before saying done/shipped/complete/certified, name the layer the
claim rests on. Do not use retired vocabulary ("static trace", "mock walk",
"backend canary", "live dogfood") to describe evidence — those are agent
working modes, not layers.

## 2. A private constraint never reaches the group

Anything one member told Vesper privately — dietary, budget, accessibility,
anything in a 1:1 thread — must never surface in a group-visible place: group
thread, notification, booking brief, shared read model, export.

**The one sanctioned path:** all group-bound text goes through
`travel-agent/backend/concierge/group_compose.py`. It reasons with identity and
composes without it, so the composing model cannot know who said what. Lexical
guards fail closed; the semantic implication guard fails closed on all four
uncertainty paths and hands off to a dignified private card.

A leak here is this project's named **"unrecoverable-trust-event risk"** — the
user does not file a bug, they stop trusting the product.

**Apply it:** any new path producing text for a group thread, push
notification, booking confirmation, or multi-member surface must trace back to
`group_compose.py` or an equivalent explicit redaction step. Ask specifically:
*what happens if the input contains something one member said privately?*

## 3. Never let a stub or a stale read stand in for the real thing

Do not ship a UI or backend response presenting a fabricated, mocked, or stale
result as if it were live. This project has shipped and unwound this pattern
more than once — fake personalization, an "auto-book" tier that booked nothing,
a dead read model showing stale state as current truth.

**Apply it:** if a surface cannot do the real thing yet, show that honestly
(explicit not-yet / disabled / pending) rather than a plausible fake. A
backend failure must never render as an authoritative empty state.

## 4. Mutations are ledgered, reversible, and honest about which one won

Any change to a Plan, proposal, booking, or expense must be append-only
ledgered and truthfully reversible:

- an accepted change emits a visible receipt;
- a rejected change visibly confirms the original state stands;
- a revert must show correctly on **every** surface that displayed the
  mutation — Plan and Map both, not just one.

**Apply it:** if your mutation does not produce a ledger entry plus a
user-visible receipt, it is incomplete — a missing invariant, not a smaller
feature.

## 5. One canonical path per mutation type — no parallel writer

Itinerary and Plan mutations commit through
`travel-agent/backend/core/itinerary_commit_gateway.py`
(`commit_itinerary_operation`, with
`load_idempotent_itinerary_operation_result` for replay). Proposals flow
through `travel-agent/backend/core/itinerary_proposal_gateway.py` and the
`backend/api/routes/proposals.py` / `itinerary_operations.py` surfaces.

A second writer is how this project's state-machine audit bugs happened — two
paths disagreeing about what state a thing is in. The guest-participation
audit explicitly **forbade** a bearer-token endpoint writing votes directly,
because it would bypass membership checks, receipt provenance, and the
canonical path.

**Apply it:** before writing a new INSERT/UPDATE for a proposal, booking,
itinerary block, or expense, find the existing gateway and extend it. Do not
route around it. If you cannot find it, that is a question, not a licence.

## 6. Verify every path you cite, in the same pass

This skill's own v1 shipped with two dead file paths and a deleted symbol,
and stayed wrong for a month. Canonical docs have carried stale claims for
weeks after the code was fixed (a privacy guard described as fail-open three
weeks after it went fail-closed; a journey described as failing two days after
repair).

**Apply it:** when you write or update a document, skill, or comment that names
a file, symbol, flag, or test — open it or grep it in the same pass. A
`last_verified` date that was stamped without re-reading the code is worse than
no date, because it launders staleness as freshness.

---

## Flag discipline

A flag may only be lit when the release manifest says so. An **IN** capability
carrying a dark flag must declare a `gate:` in
[`docs/release/v1-scope.yaml`](../../../docs/release/v1-scope.yaml) naming the
condition under which it lights; `scripts/render_release_scope.py` enforces
this. Lighting a flag outside its stated gate is a scope change, not a config
change.

## Where the fuller versions live

- [M1 — Plan Repair](../../../docs/release/m1-plan-repair.md) — the milestone,
  its four acts, and exit criteria
- [Product Proof Spine](../../../docs/journeys/PRODUCT_PROOF_SPINE.md) —
  P01–P07 and the J↔P coverage join
- [Journey Evidence Model](../../../docs/journeys/EVIDENCE_MODEL.md) — layers,
  receipts, promotion
- [V1 release contract](../../../docs/release/v1-scope.md) — what ships lit vs
  dark
- [`docs/systems/README.md`](../../../docs/systems/README.md) — system charters
  and maturity tiers
- [Journey Status](../../../docs/journeys/STATUS.md) — the promotion board
