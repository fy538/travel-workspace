---
doc_type: working
status: active
owner: founder / engineering
created: 2026-07-18
last_verified: 2026-07-18
expires: 2026-08-17
why_new: Propose the smallest evidence-backed expansion after decomposing overloaded J06, J10, and J11 coverage.
supersedes: []
source_of_truth_for: [customer-journey-expansion-proposal-2026-07]
---

# Customer Journey Expansion Proposal

## Accepted recommendation

Nine customer-outcome journeys were added as J20–J28 after the evidence namespace
was reconciled. Four existing journeys will be strengthened instead of creating
separate top-level entries for every mature surface.

This yields a projected registry of 28 stable entries while making its internal
types honest: customer outcomes versus cross-cutting assurance packs.

## Approved new customer outcomes

### `J20` — First-use trust setup to first personalized value

**Promise:** A new traveler can establish only the context they choose, defer
optional permissions, and reach one useful personalized result without being
forced through a personality quiz.

- Starting state: signed-in first session, no trips or durable Atlas value.
- Transition: onboarding/safety/privacy choices persist; one trip seed, saved
  place, or grounded Vesper response becomes available.
- Return point: Vesper Home, Trips Home, or Atlas Home with the value visible.
- Primary persona: new traveler; signed-out/auth-return is an J18 branch.
- Required branches: skip optional profile fields; deny photo/location/push;
  private safety constraint; diary/photo recovery approval; interrupted resume;
  first useful result without a committed trip.
- Likely surfaces: `/onboarding`, `/onboarding-safety`, Atlas controls, Trips and
  Vesper Home.
- Priority: **P0** — privacy and activation risk.

### `J21` — Collaborative stay and traveler ownership lifecycle

**Promise:** The group can establish where the trip is based while each
traveler retains control over personal lodging details.

- Starting state: planning trip with no stay or mixed shared/personal stays.
- Transition: create, assign, edit, replace, or remove a stay with correct scope.
- Return point: Trip Details Stay and the matching itinerary object.
- Primary personas: organizer, personal-stay owner, unrelated member.
- Required branches: shared-base organizer mutation; personal self-mutation;
  organizer assistance; unrelated-member denial; candidate/manual stay; date
  mismatch; replace/remove; plan/details reconciliation.
- Likely surfaces: `/trip-accommodations/*`, `/accommodation/[id]`, Trip Details.
- Priority: **P0** — current J10 ownership is too broad.

### `J22` — Booking exception and provider handoff lifecycle

**Promise:** The traveler always knows what Vesper, the provider, and the human
have actually completed—and how to recover when those states diverge.

- Starting state: selected, held, provider-confirming, confirmed, expired, or
  provider-unknown offer.
- Transition: decide, settle, release, retry, cancel, or continue externally.
- Return point: canonical booking receipt or originating itinerary object.
- Primary personas: assigned booker and read-only observer.
- Required branches: owner/observer authority; unpaid hold settle/release;
  expiry; stale price refresh; provider unknown; checkout failure; external
  handoff; confirmed receipt; cancellation boundary; exact return.
- Likely surfaces: `/booking/[sessionId]`, chat booking cards, itinerary object.
- Priority: **P0** — provider and payment truth.

### `J23` — Group costs through correction, dispute, and settlement

**Promise:** A group can turn a real cost into an understandable split, correct
or dispute it, and record settlement without duplicating or misdirecting money.

- Starting state: manual, receipt-derived, or booking-linked cost.
- Transition: create/edit/split/dispute/settle/payment-record persists exactly once.
- Return point: Costs ledger and balance direction agree.
- Primary personas: payer, owing member, organizer, nonparticipant.
- Required branches: manual and receipt intake; payer/member validation;
  equal/exact/itemized split; edit/delete authority; dispute; currency/direction;
  partial and full settlement; payment retry; booking opt-in dedupe.
- Likely surfaces: `/trip-expenses/*`, booking share-to-Costs.
- Priority: **P0** — direct financial trust.

### `J24` — Group membership, organizer handoff, and agency

**Promise:** Joining, leaving, rejoining, changing roles, and changing Vesper's
room authority update current access without rewriting shared history.

- Starting state: solo or group trip with one current organizer.
- Transition: membership epoch, role, owner, room authority, and audit state change atomically.
- Return point: Trip Info/Settings and group room show the same current roster.
- Primary personas: current organizer, successor, member, removed/rejoining traveler.
- Required branches: solo→group→solo→group; leave/rejoin history; promote/demote;
  organizer/shared-plan-owner handoff; last-organizer guard; pending-work fencing;
  room versus personal mute; invite/intake authority transfer.
- Likely surfaces: `/trip-info`, `/trip-settings/permissions`, group chat.
- Priority: **P0** — existing deep backend evidence has no customer owner.

### `J25` — Empty Atlas to first useful Atlas

**Promise:** Atlas becomes useful from one grounded action without inventing a
  strong taste claim or requiring a completed trip.

- Source contract: Atlas `J-A1`; current trial branch `J11.B01`.
- Transition: saved-place relationship or attributed weak prior persists.
- Required branches: save place; optional concrete answer; permission denial;
  no-result; failed save; prompt dismissal; offline cached Home.
- Priority: **P1** — activation depth after trust-critical work.

### `J26` — Shape and keep a grounded Reading

**Promise:** A traveler can understand the evidence behind an interpretation,
steer it, keep it, and reliably find it again.

- Source contract: Atlas `J-A3`; current trial branch `J11.B03`.
- Transition: composed/steered Reading becomes one durable shelf item.
- Required branches: existing versus compose; thin result; generation retry;
  provenance; steer; keep idempotency; offline cached Reading; deleted source.
- Priority: **P1**.

### `J27` — Understand and correct what Vesper learned

**Promise:** A traveler can trace a learned claim to evidence and correct,
soften, forget, or disable it without deleting the underlying travel record.

- Source contract: Atlas `J-A4`; current trial branch `J11.B04`.
- Transition: one correction model updates Memory and originating surfaces.
- Required branches: nothing learned; learning off; provenance receipt; correct;
  soften; forget; originating-artifact parity; retry; source retention.
- Priority: **P0** — memory/privacy trust.

### `J28` — Browse, hide, and recover Atlas history

**Promise:** A traveler can browse the durable record by time/place, hide an
entry, understand why it is removed, and restore it to the right chapter.

- Source contract: Atlas `J-A5`; current trial branch `J11.B05`.
- Transition: visible→user-hidden→restored preserves archive reason and chapter.
- Required branches: time/place browse; rename/pin; user hide; system/dedup
  archive distinction; Removed; restore; pagination/cache; failed restore.
- Priority: **P1**.

## Strengthen existing journeys instead of adding new IDs

| Existing journey | Add branches for | Reason not to add another global journey |
|---|---|---|
| J07 | Universal search → evaluate place/venue/dossier → save/share/add/ask | Same motivation and trip-action outcome as contextual Discover |
| J12 | Photo intake → Memory → Story → share; recipient receipt | Media is a closeout input/continuation, not a separate lifecycle yet |
| J17 | Atlas timely return, expiry/dismissal, cross-trip re-entry | Timely return is the repeat-traveler activation face of cross-trip recall |
| J18/J19 | Public story/place/profile recipient → auth/save/follow/join | Distribution and social conversion already own the recipient outcome |

## Cross-cutting packs retained during migration

| Pack | Role |
|---|---|
| J06 | Read-model reconciliation invoked by every mutation journey |
| J13 | Failure/retry branch index across customer journeys |
| J14 | Solo/cardinality branch index across creation, chat, booking, and closeout |
| J15 | Confirmation/cascade/reversal index across destructive actions |

Retaining their IDs protects historical links. Their eventual registry tier
should become `assurance-pack`, not `holistic-extension`.

## ID collision resolution — complete

The adjacent backend J22–J27 scenario labels were resolved on 2026-07-18:

1. All six files and test functions now use descriptive scenario names.
2. The old labels remain discoverable in commit history and this migration note.
3. The scenarios will map to J24, J14, or J15 branches.
4. Global J20+ numbers may now be allocated only from `journeys.yaml`.

Promoting those six backend file numbers directly is not recommended: they are
implementation scenarios, overlap one customer motivation, and would reserve
six global journeys for one governance family.

## Red-team results

| Challenge | Resolution |
|---|---|
| “First value duplicates J01.” | J01 starts with trip ideation; the new outcome owns consent, defer/deny, and value before any committed trip. |
| “Stay and booking are one commercial loop.” | Their actors and truth boundaries differ: stay scope/ownership versus provider/payment state. |
| “Costs belongs inside booking.” | Most costs are manual/receipt-derived; correction, disputes, and settlement outlive booking. |
| “Governance is just J15 destructive actions.” | Joining, role transfer, mutes, and authority fencing are not destructive-only and form a continuous group lifecycle. |
| “Atlas should remain one journey.” | Atlas already has six motivations, persisted transitions, and return points with separate native flows. |
| “Search needs a new journey.” | Not yet; its outcome already terminates in J07/J19 actions. Add branches first. |
| “Photo/story sharing needs a new journey.” | Not yet; J12 owns the returned-trip narrative and J18/J19 own recipient conversion. |
| “Failure and solo should become more journeys.” | They are assurance dimensions and should attach to every relevant customer outcome. |

## Approval gate — passed 2026-07-18

The registry allocation proceeded after confirming:

- each candidate has a non-overlapping boundary against J01–J19;
- J06/J10/J11 evidence is mapped to branch IDs;
- the renamed governance scenarios have a recorded branch destination;
- the status generator can display branch fractions without turning partial
  journeys green;
- dark versus missing capability is represented explicitly.
