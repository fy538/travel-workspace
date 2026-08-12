---
doc_type: contract
status: active
owner: product / engineering
created: 2026-08-11
last_verified: 2026-08-11
why_new: Defines the smallest proof that Vesper helps a person experience a place more deeply, without expanding the product into a broad ambient feed.
related:
  - product-proofs.yaml
  - ../release/m1-plan-repair.md
  - ../../travel-agent/docs/product/Product%20Thesis.md
---

# P08 — Curiosity becomes a grounded encounter

## Claim

When a person expresses a curiosity from a Trip-scoped Dossier, Vesper can use
one sourced perspective to prepare a feasible real-world Move, preserve the
private causal record, and use the person's private reflection to improve a
later occasion.

This proves **interpretation joined to hospitality**. It does not prove
notification-led discovery, broad city coverage, a contributor marketplace, or
general-purpose learning.

## Canonical first run

One person opens Lisbon with the explicit curiosity:

> How do cities adapt to difficult terrain?

They select the approved lens on movement across Lisbon's hills. The resulting
Move contains one canonical anchor, its two route legs, current
route/time/availability evidence, weather suitability when it is material, and
enough buffer to remain credible. The selected 45, 75, or 120-minute duration
is an upper bound for the whole journey, including both legs and buffer—not a
request the model may silently overrun. Any observation invitation is
conversational: it is not a persisted place fact, route, or claim about what
the person experienced.

A canonical rebase retains the private Dossier/lens record, but is not a claim
of semantic repair. If the opening or evidence no longer supports the
encounter, the person must request a fresh grounded Move; Vesper must retain
the original lens or say that no grounded encounter is available. It must not
silently substitute a popular but unrelated attraction.

After the person confirms the occurrence, they may privately record what they
noticed and the thread they would follow next. The next occasion can use that
private receipt only within its permission, freshness, and applicability
boundaries.

## Product rules

1. The first surface is pull-first and Trip-scoped: an approved Dossier opened
   in a Trip, or an explicit Vesper request that has an active Plan context.
   P08 does not permit notification delivery.
2. The lens, dossier, place identity, and curiosity reference travel as typed
   context. The server resolves all meaningful content from canonical ids.
3. A Move must be spatially feasible, evidence-backed, and no longer than the
   selected encounter budget. Unknown operational facts remain unknown; the
   product must not invent a route, opening, or favorable weather claim.
4. An observation invitation invites attention; it is never persisted or
   presented as a fact about the person's experience.
5. Free-text reflection is private by default. It is not public place truth,
   group truth, or telemetry content.
6. A later occasion may retain the private Dossier lens alongside its outcome,
   but must explain its use without quoting raw reflection text or exposing any
   owner-scoped context.

## Acceptance evidence

| Layer | What it proves |
| --- | --- |
| contract | A Trip-scoped lens identity survives the mobile handoff; the complete Move budget, route, hours, and material weather facts fail closed or remain explicit. |
| database | One confirmed personal outcome has a correctable, removable private reflection and private Dossier causal join that can influence only a permitted second occasion. |
| device_mock | A person can complete Trip Places → Dossier → Vesper → applied Plan/Map → reflection in one internal build. |
| human_outcome | The person can name something specific they noticed or learned that they would otherwise have missed; qualitative feedback does not describe the experience as intrusive homework. |

## Dogfood protocol

Run this with two real internal accounts and one Lisbon lens. The facilitator
records receipts and counts, not the person's private question or reflection.

1. **Intent.** Account A opens an authored Dossier, enters an optional question
   in their own words, chooses 45, 75, or 120 minutes, and opens the
   review-first Vesper thread. Confirm this doorway is absent outside a Trip;
   in a Trip, confirm the thread shows the correct bounded request and does not
   treat their words as a sourced place fact.
2. **Move.** Vesper prepares one proposal. Account A opens its **This Move**
   receipt; after the Move is applied to the Plan, they can open the focused
   map doorway. Record whether the total route + anchor + buffer duration stays
   within the selected budget, every displayed route duration was fresh,
   operating/availability claims had an authority, weather-sensitive anchors
   reacted honestly to forecast evidence, and unknown conditions stayed
   unknown. Do not mark the run successful merely because prose sounds
   plausible.
3. **Repair.** Change one relevant condition (hours, route freshness, weather,
   or the open window) in the seeded world. Verify that a canonical rebase
   retains the private Dossier/lens intent. Then start a fresh bounded P08
   request: its replacement must retain the original lens or explicitly say
   that no grounded encounter is available. A popular but unrelated substitute
   fails. This does not yet prove autonomous semantic repair.
4. **Private outcome.** After a confirmed moment, Account A records a verdict,
   optional observation, and optional next thread from the travel Plan. Verify
   that the Plan has not silently changed and that the free text is not shown
   in a group surface.
5. **Second occasion.** Start a related private planning turn. Verify that the
   bounded prior-outcome and Dossier-lens context can shape the choice, while
   raw observation text remains absent and a mismatched companion roster
   withholds companion fit.
6. **Multiplayer boundary.** Account B joins the same trip and reviews the
   canonical proposal. Verify that B can make a group decision on the Plan but
   cannot see A's question, lens interpretation, depth verdict, observation,
   or next thread.
7. **Silence.** With no explicit P08 request, location/geofence event, or
   weather change, verify that no P08 notification or ambient card appears.
   P08 has no autonomous delivery authority in this phase.

The facilitator records only: start, review, proposal-ready, proposal-applied,
confirmed, reflection-saved, later-occasion-used, and a one-sentence voluntary
answer to “what did you notice that you might otherwise have missed?” Capture
the answer only with explicit research consent; it is not product telemetry.

## Systems boundary

The existing systems contribute distinct evidence rather than one blended
“smart” claim:

| System | Permitted role in P08 | Must not do |
| --- | --- | --- |
| Dossier / provenance | Supply an authored, attributed lens | Claim it is personally true because it was clicked |
| Plan + route + Mapbox | Bound the Move and expose its route receipt once applied | Invent travel time, show an un-applied proposal as a map stop, or hide stale legs |
| Availability + weather | Constrain a bounded addition; rain can exclude a weather-sensitive anchor, while unavailable coverage stays explicit | Turn a stale or unavailable condition into a current recommendation |
| Location / proximity | Existing consented context may help establish feasibility | Trigger a P08 interruption or continuous tracking |
| Concierge AI | Synthesize, abstain, and prepare a reviewable proposal | Mutate Plan or manufacture source authority |
| Multiplayer | Let a group decide a canonical Plan change | Share a person's curiosity, interpretation, or reflection |
| Outcomes | Privately thicken a later occasion and retain the source lens | Become public place truth or a profile fact by default |

## Explicit non-goals

- No new top-level navigation, Curiosity feed, or universal place ontology.
- No autonomous generation or auto-publication of interpretations.
- No open contributor or local-expert network.
- No inferred curiosity written durably without an explicit user action.
- No ambient notification or geofence interruption.

## Promotion gate

P08 remains dark until all required layers contain revision-bound receipts. A
passing fixture, seeded replay, or hand-authored reflection is not human-outcome
evidence.

### Known boundary

The current contract records and reuses the causal lens, but it does not yet
have a deterministic lens-to-candidate matching model or autonomous semantic
repair after a condition change. Treat interpretation fit as a human-outcome
and evaluation criterion, never as an already-proven routing fact.
