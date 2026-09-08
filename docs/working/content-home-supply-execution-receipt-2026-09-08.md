---
doc_type: working
status: active
decision_status: implemented
owner: Content / Home / Integration
created: 2026-09-08
last_verified: 2026-09-08
expires: 2026-10-08
why_new: Records the bounded Content-to-Home receiving slice, its sparse/rich evidence, honest absence behavior, and the still-gated Capture anchor contract.
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

Backend child commit `3cce198dd` (`home: surface bounded public place content`)
adds:

| Layer | Change | Boundary preserved |
| --- | --- | --- |
| Content → Home adapter | `home_candidates_from_public_place_content(...)` converts already accepted, grounded, public `PlaceContentPrimitiveRecord` rows into substantive `HORIZON_EDITORIAL_PASSAGE` candidates | The Content owner remains authoritative for lifecycle, evidence, policy and public eligibility; Home does not generate or reinterpret a raw provider result |
| Home Places-context reader | The existing `places_context` reader resolves its current editorial subtree, asks the existing public-content owner for at most six current records, and appends those candidates | No GET-time acquisition, model call, universal index, private history read, or new reader budget |
| Exact continuation | Each candidate carries the immutable `place_content_primitive` source ref (including revision) and a Places entity continuation | A stale, withdrawn or expired source is not silently treated as current |
| Value contract | The result is a complete-on-view `READ` with a claim, interpretation and evidence basis; `source.inspect` remains the optional exact read | The card is not a questionnaire, status door or required Keep/follow-up |

The adapter deduplicates primitive/version identity, bounds copy and result
count, preserves source freshness, and uses the existing six-hour read window
only as a delivery deadline. The richer-context signal changes ranking and
present relevance; it never invents a personal inference or claims attendance.

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
value: world_opening → make_sense → read; high evidence; high epistemic yield;
       medium present relevance; low burden; complete on view
```

This is substantive enough to be worth receiving without asking the person to
add an artifact, answer a question, or open a second flow. It also exposes the
source identity needed for correction, expiry and inspection.

## 3. Sparse versus richer authorized context

| Situation | What the implementation does | What it does not claim |
| --- | --- | --- |
| Sparse Home, no current Trip | Uses the automatic Places context and its resolved editorial place subtree; emits the same accepted public reading with `present_relevance=medium`, priority `70`, and “A reviewed reading makes one current Place more legible.” | No personal taste, past attendance, trip, or private-history inference. If there is no resolved context or no eligible public source, it stays silent rather than inventing a card. |
| Richer authorized context, current Trip scope | Reuses the same exact public source under the explicit context, with `present_relevance=high`, priority `78`, and “This adds a grounded reading to a Place already in motion for you.” | It does not claim the person visited the entity, liked the reading, or that the source was produced for them. |

The difference is therefore useful but narrow: authorized context changes why
the item is timely, while Content still supplies the same evidence-backed
substance. This avoids both flat repetition and creepy personalization.

## 4. Freshness, no-results and cost behavior

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

## 5. Capture anchor lifecycle remains a shared-contract gate

The current Capture/Life data is not sufficient to publish a reliable anchor
event: the existing outbox owner is `retained_source`/submission, while graph
anchors do not yet carry the revision/sequence needed for replay, correction,
withdrawal and idempotent consumer behavior. This lane therefore did **not**
invent an anchor event family, schema, or lifecycle.

Integration must first publish the shared contract (event identity, source
revision, occurrence/capture time, correction/withdrawal semantics and owner
read). Life can then consume it in its bounded organization/read path. Until
that contract lands, Capture's current explicit-subject shadow and the
documentation checkpoint remain valid but are not evidence of production anchor
continuity.

## 6. Verification boundary

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
  tests/core/test_place_content_sources.py             # 91 passed
```

The test packet includes direct sparse/rich adapter tests and a reader test
with no Trip. The fixture is authored and deterministic; no live provider,
production database, model, mobile renderer or native Home screenshot was
exercised. Backend commit hooks also passed Ruff formatting, vulture, secret
checks, import/cycle/async-call ratchets, contract-key coverage and related
backend parity checks.

## 7. Next owner actions

1. **Content:** provide a reviewed populated record for one supported area and
   one richer context, including source provenance, freshness, allowed roots,
   and exact expected copy; state unsupported coverage if no row exists.
2. **Home:** consume the candidate through the existing receiving lane and
   return the exact entity/source destination; do not add a new card family or
   generator for this package.
3. **Integration:** publish the Capture anchor event contract before any Life
   production consumer is wired; land this backend commit only after the
   shared receiving review.

