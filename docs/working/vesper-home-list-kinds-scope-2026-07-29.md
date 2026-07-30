---
doc_type: working
status: active
owner: founder / eng
created: 2026-07-29
expires: 2026-08-28
why_new: Vesper Home's redesign settled on ONE list band with four kinds (sessions · route · here · season), sorted only by edge. The design is canon and verified in Claude Design, but three of the four kinds have no data source — they are eight hand-written rows in a fixture pool. No doc scopes what each kind would actually cost to implement, and the build order that falls out of that scoping is close to the inverse of the design's own emphasis. This doc owns exactly that scoping and the build order it implies.
promotes_to: an engine build plan once the sessions envelope ships
supersedes: []
depends_on:
  - docs/working/vesper-home-workbench-2026-07-28.md
  - docs/working/home-surfaces-program-2026-07-28.md
source_of_truth_for:
  - vesper-home-list-kind-sourcing
  - vesper-home-list-build-order
---

# Vesper Home — the list kinds, scoped

> **The design is settled; the data is not.** The canon lives in Claude
> Design (`vesper-list.jsx` for the model, `Vesper Home - Workbench.html`
> §05/§05b for the surface). This doc does not restate it. It answers one
> question: what would each kind cost to actually implement, and what
> order does that imply.

## The model, in one paragraph

Vesper Home has four slots — `voice · facts[2] · seam · list`. The list is
**one band, one kind at a time**, and the cap names the kind. Four kinds
exist: `sessions` (yours) and `route · here · season` (the world's). World
kinds compete **only on edge** — the nearest closing deadline wins the band,
and the rows are the rest of that kind. No backfill across kinds; a
one-row list is the correct answer to a quiet week. Sessions carry no
calendar edge, so they are a separate tier that wins whenever any are open —
the single opinion in the model, recorded as open in `vesper-list.jsx`.

**Every row must have an edge.** That is the eligibility rule, and it is
what keeps the surface off a feed. It also disqualifies more candidate data
than it first appears to — see `here` below.

## The scoping

| kind | source today | the gap | cost model | coverage |
|---|---|---|---|---|
| `sessions` | conversations + `concierge_feed` | serializer only | zero marginal | 100% |
| `route` | Amadeus/Duffel **pricing** | no **discovery** | per origin per day | global |
| `here` | events exist as a *lookup* category only | no maintained calendar | editorial + vendor | per city |
| `season` | nothing | a small curated table | ~zero after authoring | global |

### 1 · `sessions` — real today

On the wire now: `conversation_type`, `trip_id`, `title`,
`last_message_preview` / `sender`, `unread_count`. `concierge_feed` already
ranks cross-trip items, and F1 ratified adopting it (filtering, never
re-scoring).

**Missing, all in the DB and none on a read endpoint:**

- the facepile — `ParticipantResponse` is `{user_id, role, joined_at}`; no
  display name, no avatar
- running / waiting — `intent_state.phase`, `current_goal`,
  `open_questions[]`, `session_status`, `agent_workflows.status`
- **a session's edge** — who owes whom, and since when. This is what would
  retire the tier exception and let sessions compete honestly on edge
  instead of always winning.

Hours of work. No vendor, no marginal cost, no coverage question.

### 2 · `route` — one new call on a vendor already integrated

**Verified in `backend/booking_agent/providers/amadeus_flights.py`.** Its own
docstring lists three endpoints:

1. Flight Offers Search — `POST /v2/shopping/flight-offers`
2. Flight Offers Price — `POST /v1/shopping/flight-offers/pricing`
3. Flight Create Orders — out of scope

All three require **origin + destination + dates**. That is *pricing an
itinerary the traveller specified*. It is not discovery.

What the kind needs is **Flight Inspiration Search**
(`/v1/shopping/flight-destinations`) — origin only, returns destinations
with prices. Same vendor, same credentials, not integrated. So this is a
new provider method rather than a new commercial relationship.

**The economics are favourable and worth stating plainly:** results cache
per *origin per day*, so cost scales with the number of distinct home
cities, not with users. Ten thousand travellers in New York share one query.

Two risks:

- **origin inference.** Does the product reliably know a home airport?
  Unverified.
- **staleness.** Showing a fare that is gone is worse than showing nothing.
  Needs a freshness stamp and a short TTL, and the row should degrade to
  absent rather than to a stale price.

**One honest design note.** The canonical March specimen reads *"both end
with the month."* The API's real edge is the travel-date window that was
searched, not a price expiry. Those are different claims and the copy must
not imply the fare expires when it does not.

### 3 · `here` — the hard one, and it is a per-city pilot

**Verified:** `backend/lookup_agent/schemas.py` carries `"events"` as a
classifier category. That is *reactive* — a traveller asks what is on this
weekend and the agent searches. There is no maintained, dated, per-city
calendar, which is what a proactive list requires.

Three options, none clean:

- **Vendor** (Ticketmaster / Songkick / Eventbrite). Covers *ticketed*
  events. Does not cover "the Frick reopens after five years", Restaurant
  Week, or greenmarket citrus — which are precisely the three canonical
  rows in the design. The specimen was drawn from the category a ticketing
  API is worst at.
- **Editorial.** The Discover pipeline already generates dossiers and has a
  manual approval gate (F6 ruled `AUTO_PUBLISH_GREEN_DOSSIERS` stays off).
  Dated city windows could ride the same machinery and the same gate.
- **Hybrid** — vendor for ticketed, editorial for civic and seasonal-local.

**The edge is the binding constraint, not the events.** Most event data
carries a start date and no reliable *end*. This model sorts by the closing
edge, so the admissible subset is far smaller than "events near me"
suggests. Any vendor evaluation should test for end-dates first and
everything else second.

Scope as **one to three cities**, not a global feature.

### 4 · `season` — cheapest, widest coverage, no feed

**Verified:** nothing exists. `backend/core/recurring_patterns.py` is
weekly-schedule parsing (opening hours, market days), not annual seasons.
`temporal_resolution.py` and `loose_dates.py` are date parsing.

What is needed is small: a curated table of a few hundred rows. Northern
lights until March. Blossom forecast mid-February. Ferries restart in April.
Shoulder seasons, monsoons, harvests. These change **annually**, apply
**globally**, and need no API.

Edges are fuzzy — "until the sky stays light" — but honestly fuzzy, and the
design already accepts that.

## The build order, and why it is not obvious

```
sessions  →  season  →  route  →  here
```

This is close to the **inverse** of the design's own emphasis, where §05b's
canonical first launch is a `here` list of three local windows.

The reason is coverage, and the design already argued it for a different
purpose. §05b says `season` "needs no feed at all, which matters because a
cold account most often opens in a city Vesper has no coverage for." That
was written to justify `season` as the second-fact fallback. The
implementation scoping independently lands on the same kind as the cheapest
to build. Design reasoning and build cost agreeing is rare; take it.

**The consequence for §05b.** If `season` ships first, the realistic first
launch is a season row, and `here` becomes the upgrade for covered cities —
not the default. The hero specimen should eventually be re-shot against
whichever kind actually ships first, or it will teach the wrong expectation.

**The consequence for `nocoverage`.** That fixture — list empty, no well,
eyebrow absorbs the ambient — may be the *common* first launch rather than
the edge case, until `season` lands. It is worth knowing what fraction of
first launches would land there before deciding how much of §05b is the
real product.

## The engine, which is unblocked either way

Independent of the kinds above, and buildable on `sessions` alone:

- **One envelope, two waves.** Wave 1 is `facts · seam · list` — a cheap DB
  and cache round trip. Wave 2 is the generated voice. They must not be one
  payload, or the whole home page blocks on the slowest and most
  failure-prone slot.
- **The voice derives from the envelope**, not from a parallel query. The
  read line is a readout of the winning kind and its count, which is why
  `VList.read()` exists as a **deterministic floor**: when generation is
  slow or fails, the page says the plainer version of the same true thing
  and never blanks.
- **One kind per response, decided server-side.** A client handed all kinds
  will eventually render two.
- **Never pad across kinds.** A one-row list is the truth about a quiet week.

A Vesper Home showing only `sessions` is a legitimate product under the
model's own no-backfill rule, not a degraded one. So the engine should ship
before any world kind exists.

## Unverified, and worth ten minutes each

- That Flight Inspiration Search is genuinely not integrated. The evidence
  is the provider's own docstring listing three endpoints — strong, not
  exhaustive.
- Whether the product reliably knows a traveller's home airport.
- The Discover per-angle generation cost. The ~$0.14 figure is from an
  earlier research-pipeline note, not a fresh read.
- Whether any Discover content already carries end-dates. If it does, `here`
  is cheaper than scoped above.

## Open decisions

| # | decision | blocks |
|---|---|---|
| K1 | Does `season` ship before `here`, accepting that the §05b hero is then unrepresentative? | build order |
| K2 | Which cities for the `here` pilot, and vendor vs editorial vs hybrid? | `here` |
| K3 | Is the tier exception (sessions always win) permanent, or retired once a session edge exists? | `vesper-list.jsx` §OPEN |
| K4 | What fraction of first launches land in `nocoverage`? Needs a number before §05b's weight is settled. | §05b scope |
