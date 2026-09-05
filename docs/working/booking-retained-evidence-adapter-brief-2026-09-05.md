---
doc_type: working
status: active
owner: capability-retirement / Life / Home / Integration
created: 2026-09-05
last_verified: 2026-09-05
expires: 2026-10-05
why_new: Defines the smallest retained booking-evidence contract needed to remove Vesper-owned booking execution without losing useful tickets, reservations, provider facts, or exact recovery paths.
supersedes: []
depends_on:
  - product-surface-contraction-investigation-2026-09-04.md
  - capability-retirement-static-inventory-2026-09-05.md
  - capability-retirement-execution-receipt-2026-09-05.md
  - ../decisions/2026-09-05-home-borrows-life-pass-grammar.md
source_of_truth_for:
  - retained-booking-evidence-adapter
---

# Booking retained-evidence adapter

## Purpose and boundary

Vesper is retiring provider execution while keeping the useful relationship a
person has with a booking-shaped object. A ticket, confirmation, cancellation,
or external link can still help someone understand what is true, continue
elsewhere, find it later, or make the next part of the day work.

This is the handoff contract between capability retirement, Life, Home, and
Integration. It defines a **read adapter**, not a new booking system. Existing
booking session/offer identity remains authoritative for legacy records; Life
owns continuity; Home may deliver a timely consequence or live pass; the
external provider owns execution.

No provider call, reservation inference, migration, backfill, table deletion,
flag enablement, or route rewrite is authorized here.

| Vesper may own | Vesper does not claim |
| --- | --- |
| Explain available evidence and its provenance | Opening a provider link created a reservation |
| Preserve a private original and exact source/session/offer identity | A saved object or plan placement means attendance |
| Show supported status, timing, amount, and missing/unknown facts | Old provider data is current without a freshness owner |
| Open the canonical Life record or provider continuation | A provider page, refund, cancellation, or callback succeeded without owner truth |
| Present a current Home consequence when its fact and window are valid | Life or Home owns checkout, payment, cancellation, or reconciliation |

“We have the ticket” and “Open with the provider” are supported. “Booked for
you” is not.

## Existing identity and ownership

The adapter preserves the identity that disambiguates a record. It may normalize
the shape for a reader, but never collapses owners into a synthetic reservation
ID.

| Evidence kind | Identity to retain | Authority / reader |
| --- | --- | --- |
| Booking session | `trip_id` + `session_id` | Booking read API and its lifecycle |
| Booking offer | `trip_id` + `session_id` + `offer_id` | Offer read, provider status and cancellation truth |
| External confirmation or ticket | Source/submission ID plus provider reference | Intake/Source custody and Life exact-source reader |
| Trip block or arrangement | Trip/Plan owner + block/commitment ID | Plan/Occasion owner; evidence is a dependency |
| Accommodation row | Trip + accommodation row ID | Stay owner; linked expense remains its own ledger record |
| Expense/refund association | Expense ID and booking/offer reference | Expense owner and deterministic ledger |
| External continuation | Canonical URL or supported phone target + origin context | Places/entity or provider handoff; no session creation |

If a legacy session points to multiple offers, the reader shows unresolved
selection and lets the person choose or open the owning record. It never picks
the first offer. Withdrawn or revoked material produces the established
unavailable state while independent evidence follows its own retention rules.

## Reader vocabulary

These are semantic fields, not a new wire DTO. The first implementation derives
them from existing responses inside `bookingReads.ts` and Life/Home projections.
Add a contract field only after the owning API and generated-type review.

| Field | Required meaning | Missing/unknown behavior |
| --- | --- | --- |
| `evidence_ref` | Stable source/session/offer identity with kind | Never substitute a generic ID |
| `subject` | Provider, place, route, or arrangement name | Use canonical identity or label unknown |
| `status` | Supported `confirmed`, `cancelled`, `pending`, `unknown`, `expired`, or `unavailable` | Never upgrade from a link or stale cache |
| `occurred_or_scheduled_at` | Provider/arrangement time, separate from upload time | Preserve occurrence chronology |
| `amount` | Original amount and currency when supplied | Keep original denomination; no invented conversion |
| `provider_fact_at` | When a current provider fact was last known | Current claims require valid freshness |
| `source` | Original/evidence destination and access scope | Missing source remains missing |
| `external_continuation` | Supported URL/phone/action with exact target identity | Hide unsupported continuation |
| `linked_context` | Plan/Occasion, place, expense, people, or Life references | Show only authorized relationships; do not infer attendance |
| `return_context` | Origin root, result-set/unit/resource identity and revision when known | Recompose after stale or withdrawn state |

Historical, current, and unknown are distinct. A stale cached `confirmed` row
may remain dated evidence while current action advice is withheld.

## State and composition matrix

| State | Read result | Home / Places treatment | Allowed action |
| --- | --- | --- | --- |
| Confirmed, current | Exact owner fact with freshness | Life holds the record; Home may show a pass in its live window | Open evidence, provider continuation, linked context |
| Confirmed, dated/stale | Historical fact with timestamp | Life retrieval; no current live claim | Open source; owner-authorized revalidation |
| Cancelled | Cancellation and supported refund/manual-attention fact | Life record; Home consequence only if it changes today | Inspect evidence and manual recovery |
| Pending/processing | Current owner lifecycle and request identity | Never present as confirmed | Recheck existing owner status; no new execution from a read |
| Unknown/ambiguous | Last observed fact plus uncertainty | No success copy or false empty state | Open evidence/support; preserve unknown |
| Missing evidence | Valid relationship but no original | Explain what is missing; no generated substitute | Retry authorized source read or known external continuation |
| Revoked/unavailable | Access or withdrawal state | Remove private material from active projections | Exact owner repair or source controls |

The September 5 Home decision gives kept objects a shared pass/chip vocabulary.
The adapter supplies identity and facts; it does not implement a second card
renderer or decide prominence.

1. Before a live window, a ticket or booking-shaped object is a kept object or
   line in the relevant Home composition. No unsupported provider fact appears.
2. During a live window, a current owner-backed fact can become Home's crown or
   pass, with the last-known boundary and a door to exact evidence.
3. After occurrence, the pass leaves Home and Life retains the historical
   record. Later value is a grounded consequence or connection, never implied
   live reservation state.
4. Home's crown arbitration decides competition among objects; this adapter
   does not create a second demand budget.

Life can open the exact source/session/offer record and preserve chronology,
access, correction, and withdrawal. Home and Places consume owner reads and
return-context contracts. Neither root copies the whole booking object into an
independent store.

## Read/write boundary

The first app package extracted query hooks into `travel-app/data/bookingReads.ts`
while `data/booking.ts` keeps mutation hooks and compatibility exports. Query
keys, API methods, polling semantics, and mutation behavior remain unchanged.

Later presentation may reuse `BookingReceiptPrimitives`, but this adapter does
not own:

- session creation, offer selection, cart, hold, checkout, payment, or provider
  mutations;
- cancellation/rebooking or restaurant contact, except finite recovery for
  identified existing obligations;
- Chat tool discovery, share-capture ingestion, or memory admission;
- Plan/Occasion commands, participation, grants, attendance, or expense debt;
- Life indexing/grouping/migration, Atlas deletion, or Home arbitration.

## Consumer handoff

| Consumer | Needs | Remains owner-specific |
| --- | --- | --- |
| Life exact record/refind | Identity, chronology, source, access, correction | Corpus organization, episodes, grouping, synthesis, migration |
| Home pass/consequence | Current-window eligibility and dated fact | Ranking, crown, demand budget, copy, social placement |
| Places/entity | Canonical subject, URL/phone, result-set return context | Entity identity, public sharing, people, research |
| Plan/Occasion | Linked block/commitment and current evidence | Placement, participation, grants, mutation authority |
| Expense | Authoritative amount/currency and association | Allocation, rounding, ledger, payment, void, dispute |
| Chat | Source/reference and authored handoff context | Conversation, intake authority, memory and receipts |
| Export/deletion | Source and linked-record identifiers | Retention, deletion policy, redacted export |

## Implementation and exit criteria

1. Keep the read-facade extraction and compatibility tests green.
2. Inventory session-route, proposal, stay/coverage, expense, Life refind,
   export/deletion, and recovery callers as read, recovery, mutation, or
   compatibility. Preserve exact query identity.
3. Map fields to Life/Home's pass/chip family. Request new visual work only for
   an unsupported state; do not create an independent reservation composition.
4. Test confirmed, cancelled, unknown, multiple-offer, missing-source,
   revoked, stale/offline, and external-continuation cases. Assert reads never
   create a session/order/hold, call a provider, or claim a reservation.
5. Migrate one historical route and its exact return context through Integration;
   retain the compatibility URL until reachability is measured.
6. Remove presentation and execution families only after retained-consumer and
   environment-obligation gates are evidenced.

Exit requires exact identity reads, useful Life retrieval, valid Home
consequence/pass, named owners for all consumers, usable historical/recovery
links, and no production or migration claim from local code evidence.

## Open receiving-lane decisions

1. Life: exact reader route and which booking facts are first-class kept objects
   versus source-only entries.
2. Home: final pass/chip visual details and live-window freshness; written crown
   arbitration remains provisional where its design board says so.
3. Integration: canonical route/return payload and generated-contract ownership
   if a field is later required.
4. Expense: first assisted scope and association of externally purchased,
   non-Trip confirmations.
5. Operations: environment-specific obligation audit before runtime retirement
   or provider credential change.
