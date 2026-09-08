---
doc_type: working
status: active
decision_status: implemented
owner: Content / Home / Integration
created: 2026-09-08
last_verified: 2026-09-08
expires: 2026-10-08
why_new: Records the bounded Content-to-Home receiving slice, conservative editorial value calibration, sourced review specimens, and the landed Capture anchor shadow contract.
supersedes: []
depends_on:
  - vesper-program-roadmap.md
  - recommendation-world-supply-architecture-and-roadmap-2026-09-07.md
  - source-connected-value-execution-receipt-2026-09-07.md
---

# Content → Home supply and Capture anchor lifecycle — execution receipt (2026-09-08)

This is a bounded implementation receipt, not a claim of complete world
supply, provider coverage, or Capture support. Content owns the admitted public
material; Home consumes it through the existing root-candidate contract;
Integration owns shared contract/schema and landing. The slice deliberately
does not add a provider, index, generator, store, API route, mobile screen, or
new Home renderer.

## 1. What landed

Backend child commits `3cce198dd` (`home: surface bounded public place
content`), `472250bd2` (`content: calibrate Home editorial value signals`),
and `7e72194b3` (`fix(content): allow bounded non-trip purpose fit`) add. The
latter two are landed on canonical `travel-agent/main` as `8a092de39` and
`a7c02cbe1`:

| Layer | Change | Boundary preserved |
| --- | --- | --- |
| Content → Home adapter | `home_candidates_from_public_place_content(...)` converts already accepted, grounded, public `PlaceContentPrimitiveRecord` rows into substantive `HORIZON_EDITORIAL_PASSAGE` candidates | The Content owner remains authoritative for lifecycle, evidence, policy and public eligibility; Home does not generate or reinterpret a raw provider result |
| Home Places-context reader | The existing `places_context` reader resolves its current editorial subtree, asks the existing public-content owner for at most six current records, and appends those candidates | No GET-time acquisition, model call, universal index, private history read, or new reader budget |
| Exact continuation | Each candidate carries the immutable `place_content_primitive` source ref (including revision) and a Places entity continuation | A stale, withdrawn or expired source is not silently treated as current |
| Value contract | The result is a complete-on-view `READ` with a claim, interpretation and evidence basis; `source.inspect` remains the optional exact read | The card is not a questionnaire, status door or required Keep/follow-up |

The adapter deduplicates primitive/version identity, bounds copy and result
count, preserves source freshness, and uses the existing six-hour read window
only as a delivery deadline. Public acceptance remains a source-quality and
eligibility signal, not proof of personal novelty or high explanatory yield.
Without an authorized known-claim window, novelty is `not_applicable`; an
explicit matching claim becomes `known_to_person`. Evidence strength derives
from required observation states. Epistemic yield is high only for a distinct
interpretive lens with at least two source observations, medium for a distinct
single-source interpretation, and low for a repeated/weak cue.

An explicit richer context changes ranking and present relevance only when the
caller names a concrete current-purpose fit (`context_adds_value=True`) and
provides an authorized context reference. A Trip-shaped scope by itself does
not earn the `+8` ranking or a personalized explanation; the fit also works
for a bounded city, area or continuation context.

## 2. Actual checkpoint output

The following is a **synthetic authored fixture passed through deterministic
production code**, not populated production data or a live provider result. It
is included to show the exact receiving payload and depth that Content must
eventually supply:

```text
candidate_id: home.public-content.<fixture-record-id>
anchor: New York's waterfront is still shaping how neighborhoods meet the city.
voice: The old industrial edge remains part of the neighborhood's social shape.
basis: working piers beside newer public paths; when walking the waterfront between neighborhoods
source_ref: place_content_primitive/<fixture-record-id>@aaaaaaaa…aaaaaaaa
destination: Places / places.open_entity(place/7, exact source ref)
why_this: A reviewed reading makes one current Place more legible.
value: world_opening → make_sense → read; high evidence; medium epistemic yield;
       not_applicable novelty; medium present relevance; low burden; complete on view
```

This is substantive enough to be worth receiving without asking the person to
add an artifact, answer a question, or open a second flow. It also exposes the
source identity needed for correction, expiry and inspection.

## 3. Sparse versus richer authorized context

| Situation | What the implementation does | What it does not claim |
| --- | --- | --- |
| Sparse Home, no current Trip | Uses the automatic Places context and its resolved editorial place subtree; emits the same accepted public reading with `present_relevance=medium`, priority `70`, and “A reviewed reading makes one current Place more legible.” | No personal taste, past attendance, trip, or private-history inference. If there is no resolved context or no eligible public source, it stays silent rather than inventing a card. |
| Richer authorized context, but no demonstrated current-purpose fit | Reuses the same exact public source with the same `present_relevance=medium`, priority `70`, and copy as sparse Home. | A Trip or rich scope alone does not make a public interpretation more relevant. |
| Richer authorized context with an explicit current-purpose fit | May use `present_relevance=high`, priority `78`, and “This adds a grounded reading to a Place already in motion for you.” The fit does not require a Trip; a bounded Places context reference is sufficient. | The fit must be named by the producer; it still does not claim attendance, taste, or private meaning. |

The difference is therefore useful but narrow: an authorized current-purpose
fit may change why the item is timely, while Content still supplies the same
evidence-backed substance. This avoids both flat repetition and creepy
personalization.

## 4. Sourced local review specimens

The following are **authored review specimens**, not populated production rows,
provider calls, or permission to republish source prose. They were checked
read-only on 2026-09-08 against the public operator/park pages:

- [Hudson River Park — Pier 57](https://hudsonriverpark.org/locations/pier-57/)
  states that the nearly two-acre rooftop park and perimeter walkway are open
  daily 6:00 a.m.–1:00 a.m.; it also describes a 7,400-square-foot indoor
  “Living Room” with seating and views.
- [Pier 57 — Rooftop Park](https://pier57nyc.com/rooftop/) repeats the daily
  hours, gives the south-gate access route, and identifies the rooftop as a
  public place for picnics and gatherings.
- [Pier 57 — About](https://pier57nyc.com/about/) describes the original
  maritime terminal and its use of three hollow concrete caissons to support
  the main structure.

The resulting candidate copy is deliberately bounded:

```text
Pier 57 offers two public settings for a waterfront catch-up: a nearly
two-acre rooftop park and an indoor Living Room.

The same address can support two kinds of catch-up: open-air views on the roof,
or seated indoor gathering in the Living Room.

Basis: rooftop hours and indoor seating/views are source-stated; check current
access and hours. Crowd levels, weather, seating availability and a friend's
preference remain unknown.
```

The companion historical specimen is:

```text
Three hollow concrete caissons support Pier 57’s main structure.

The pier’s engineering is part of its identity: a reused maritime terminal
whose structure remains part of what you are standing on.
```

The first combines two source observations into a practical alternative without
claiming that the roof is calmer, that an indoor move is guaranteed, or that a
specific friend will prefer it. The second is a single-source interpretation;
its evidence is high when the required observation is active, but its
epistemic yield remains medium. Source URLs and research time are retained in
the authored fixture; no source-rights or current-availability claim follows.

## 5. Freshness, no-results and cost behavior

- The source owner admits only accepted, active, grounded, public,
  policy-bound records valid at the represented clock and explicitly eligible
  for Home/Places. The exact source revision remains in the candidate.
- The Home reader bounds the request to six records. It uses no provider,
  model, background worker, index write, or private-history query. A source's
  own `valid_until` wins over the six-hour read window; a failed owner lookup,
  unsupported context, or empty result returns the existing Places-context
  candidates only.
- No-result behavior is honest absence, not a generic “ask Vesper” door and
  not a claim that the world has nothing worthwhile. Populated production
  supply still requires Content evidence and a supported area/subject.
- No service price or production cost was measured in this slice. The bounded
  read adds a source-list operation to an already existing Home reader; any
  provider/model acquisition cost belongs to Content's producer and remains
  outside this commit.

## 6. Capture anchor lifecycle and Life shadow status

The candidate-owned Capture contract is now landed. Integration's producer
commit `cd0e28f35` adds the monotonic candidate revision and atomic Intake/Life
outbox handoff. Life's consumer `ac54cefc9` and revision-alignment follow-up
`9b1009a6a` are also landed on canonical `travel-agent/main`.

The Life adapter remains shadow/read-only: it re-reads the authoritative
candidate and source custody, fences candidate revisions, writes only the
existing private Life Time row, and supports withdrawal, explicit newer
restore, stale replay, source-access loss, bounded enumeration/backfill and
user-control preservation. This does not make serving ready, populate
production candidates, infer attendance/people, activate Source, retire Atlas,
or add a new event bus.

The remaining gate is therefore serving and broader evidence—not the owner
identity/revision contract. Capture's current explicit-subject shadow and this
receipt remain implementation evidence, not proof of production continuity.

## 7. Verification boundary

Executed in the dedicated backend lane:

```text
ruff check backend/root_projection/v2/home_portfolio.py \
  backend/root_projection/v2/home_source_adapters.py \
  tests/root_projection/test_home_portfolio.py       # passed
python -m compileall -q <two changed backend modules> # passed
pytest -q tests/root_projection/test_home_portfolio.py \
  tests/root_projection/test_source_contribution_discovery.py \
  tests/root_projection/test_source_contribution_materials.py \
  tests/api/test_root_composition_service.py \
  tests/api/test_practical_root_delivery.py \
  tests/core/test_place_content_sources.py             # 97 passed
```

The test packet includes direct sparse/rich adapter tests, a reader test with
no Trip, conservative known/repeated/weak-yield cases, the non-Trip
current-purpose fit regression, and the two Pier 57 review specimens. The
fixtures are authored and deterministic; no live provider, production
database, model, mobile renderer or native Home screenshot was exercised.
Backend commit hooks passed Ruff formatting, vulture, secret checks,
import/cycle/async-call ratchets, contract-key coverage and related backend
parity checks.

## 8. Next owner actions

1. **Content:** provide a reviewed populated record for one supported area and
   one richer context, including source provenance, freshness, allowed roots,
   and exact expected copy; state unsupported coverage if no row exists.
2. **Home:** retain the existing receiving lane and exact entity/source
   destination; no new card family or generator is required for this package.
   Native visual acceptance and populated production supply remain unrun.
3. **Integration:** preserve the landed candidate producer/consumer boundary;
   any future serving cutover or broader evidence packet is a separate,
   founder-approved gate.
