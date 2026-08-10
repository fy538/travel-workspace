---
doc_type: working
status: active
owner: founder / product / engineering
created: 2026-08-10
expires: 2026-09-09
why_new: Keeps unresolved canonical home-surface compositions from becoming silent frontend or schema commitments before product adoption, privacy, and evidence conditions are explicit.
source_of_truth_for: [home-surfaces-unresolved-composition-adoption-gates]
supersedes: []
---

# Home surfaces — adoption decision docket

This is the execution gate for compositions that are present in the canonical
external design bundle but not yet adopted in the product inventory. It does
not adopt any item. A component or a partial backend substrate is not evidence
that the composition is approved to ship.

The implementation inventory remains
[`docs/status/home-surfaces-composition-inventory.json`](../status/home-surfaces-composition-inventory.json).
This docket separates decisions from their later engineering work so that an
agent never silently turns a board option into a wire contract, a mutation, or
a shared read model.

## Required verdict for every row

Before any non-dark implementation begins, the named product owner records:

1. **Verdict:** `adopt`, `explore behind an explicit flag`, `defer`, `reject`,
   or `relocate`.
2. **Surface and order:** Places feed reason/arrangement or exact Trips page-plan
   position. Neither client-side ranking nor body-local membership is allowed.
3. **Evidence predicate:** the real facts that permit the composition and the
   honest absent/unavailable state.
4. **Canonical action:** existing destination/writer, or an explicitly approved
   new owner. No decorative action.
5. **Privacy and authority:** whether information is private, shared, member
   scoped, consented, or location/photo sensitive.
6. **Acceptance scenario:** fixture, backend-real canary, and physical-device
   path required before `F`, `B`, or `V` evidence may be recorded.

Any row that writes a Plan, proposal, booking, expense, or shared message must
use the existing canonical writer, ledgered receipt, and privacy boundary. A
private member signal never becomes group-visible source text.

## Packet A — Places registers and arrangements

| Composition | Current usable substrate | Required decision before implementation |
|---|---|---|
| `places-a-register-anatomy` | candidate rows plus `reason`, `note`, `count` | Select allowed register kinds. Recommendation stays dark until a real confidence signal exists. |
| `places-b-door` | count door and typed list destinations | Decide whether the quiet-panel grouping is a distinct arrangement or only the current count door is adopted. |
| `places-b-comparison-stack-stub` | partial time/price/set facts | Adopt one arrangement first; define comparable facts and destination. |
| `places-d-new-reading-registers` | reading/lens substrate | Name one reading arrangement and its attributable evidence. Overlay lens is not implied. |

Engineering after adoption: additive discriminated backend arrangement/register
contract → producer eligibility/provenance tests → generated types → Places
render-plan execution → responsive renderer → fixture/canary/device evidence.

## Packet B — Places maps, return, people, and personal history

| Composition | Missing product/domain truth | Required decision before implementation |
|---|---|---|
| `places-c-root-map` | no feed projection or ownership | Decide Places versus Trips ownership before adding a root map. |
| `places-e-postcard-return` | return selection and final read destination | Define grounded selection and an honest artifact/trip route. |
| `places-f-cosign-again-marker` | consented recurrence and people-to-place aggregate | Approve privacy policy and aggregation semantics. |
| `places-g-personal-record` | visit/return history and page-length semantics | Define the visit signal; saves alone cannot impersonate return history. |

No location, social, or historical aggregation may be inferred merely because a
place is nearby, saved, or associated with a trip.

## Packet C — Trips immediate attention and people

| Composition | Current usable substrate | Required decision before implementation |
|---|---|---|
| `trips-a-near-you` | generic crown card + typed nearby destination | Approve dedicated receipt, location freshness policy, and permission states. |
| `trips-b-temporal-strip` | none | Define a day-receipt contract and its no-data state. |
| `trips-c-invite-people` | invite card, People destination, roster route | Select crown/section placement and approve the member-visible read model. |

Near You must disclose foreground location and never present a previous location
as current. Invite/People content may expose only authorized membership facts;
it must not compose from private traveler inputs.

## Packet D — Trips decisions, plans, approach, and return

| Composition | Current usable substrate | Required decision before implementation |
|---|---|---|
| `trips-d-evidence-decision` | generic Crown receipts | Adopt one standalone module and specify its canonical resolution route. |
| `trips-e-draft-shelf` | none | Define a real draft entity/lifecycle before a shelf exists. |
| `trips-f-hosting` | none | Define hosting as a domain entity and its lifecycle. |
| `trips-g-pretrip-approach` | partial temporal/save substrate | Choose This Week, This Weekend, or Saved Unplaced individually. |
| `trips-h-return` | retrospective cards and compatibility routes | Define a real Story/read destination; Plan is not a plausible substitute. |

Any resolution action must call the existing proposal/Plan path. It cannot create
a parallel writer or an unledgered mutation.

## Packet E — Maps and Trip Feel

| Composition | Current usable substrate | Required decision before implementation |
|---|---|---|
| `trips-j-today-mapped` | selector, endpoint, typed model, dark renderer | Decide dark/dogfood/production posture and explicit build profile. |
| `trips-j-map-expansion` | partial vocabulary only | Define coherent route/member/photo truth and privacy policy before selectors. |
| `trips-k-trip-feel-static` | private local prompt | Decide whether to retain it; acknowledgement must be honest about `recorded`. |
| `trips-k-trip-feel-stateful` | none | Define private persistence, canonical writer, resumption, revision, and receipt. |

Today Mapped is the only map candidate eligible for a narrow evidence-first
release train. Expansion concepts require separate privacy and coherence review;
member locations and photos are not safe generic map inputs.

## Engineering dispatch rule after a verdict

For one adopted family, use three isolated lanes:

1. **Backend:** model/producer/route tests and additive OpenAPI contract.
2. **Frontend:** generated type consumer, Places feed or Trips page-plan entry,
   renderer, canonical action, and telemetry identity.
3. **QA:** exact-state fixtures, mock walk, backend-real canary, and paired iOS/
   Android physical-device evidence.

The integration owner alone synchronizes `docs/openapi.json`,
`docs/openapi.app.json`, and `travel-app/utils/api/schema.gen.ts`. Backend
compatibility deploys before app reliance; removal waits for client/cache expiry
and device proof.

## Current stop conditions

- There are 19 unresolved and one exploratory composition rows. They are not
  coding debt until a verdict exists.
- Physical-device evidence remains unavailable while the connected iPhones are
  offline; simulator/mock evidence must not be promoted to `V=verified`.
- A backend-real canary is required before any named family is called
  backend-validated; generated fixtures are not a substitute.
