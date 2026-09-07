---
doc_type: working
status: active
owner: founder / content research / integration
created: 2026-09-07
last_verified: 2026-09-07
expires: 2026-10-07
why_new: Grounds recommendation supply in current adapters and delivery code, current provider documentation, retention constraints and a checkpointed implementation handoff for the NYC specimen portfolio.
supersedes: []
---

# Recommendation world supply: architecture and implementation roadmap

## 1. Recommendation

**Borrow broad discovery coverage; own selective, well-supported understanding and personal judgment. Do not build a comprehensive world index, but do not interpret that as storing nothing.**

Use existing canonical identities and evidence owners, bounded provider/web acquisition, selectively retained public material, and private current-purpose composition. Dossiers are optional depth. Home and Places consume eligible prepared material; an explicit investigation can discover something outside our corpus without first manufacturing a dossier, Trip or Plan.

The inspected foundation is reusable. The main gaps are candidate acquisition/admission, temporal fidelity, commercial source policies and the connection from acquisition to delivery—not the absence of another engine.

This is a **research-backed implementation roadmap**, with the bounded code receipts in §10. The detailed Content-lane execution plan is in [§11](#11-content-infrastructure-execution-plan); the next implementation batch, dependencies and completion checks are in [§12](#12-next-execution-batch-connected-content-lifecycle). It does not establish provider procurement, legal clearance, deployment approval or complete supply. No paid API batch, account inspection, production DB query, subscription, provider contact, worker registration or app change was performed in this lane. Public documentation describes capabilities, not measured NYC coverage.

### Authority and inspected state

- [Product Thesis](../../travel-agent/docs/product/Product%20Thesis.md) and [Product Model](../../travel-agent/docs/product/Product%20Model.md): everyday usefulness; current purpose over historical resemblance; four product moves, not a travel-only funnel.
- [Place canon §6](../../travel-agent/docs/product/Place%20Interpretation%20and%20Content%20Intelligence.md#6-pre-research-live-retrieval-and-runtime-composition): bounded investigation, thin serving, selective reuse, dossier-independent recommendations.
- [Situated-value matrix §15](situated-value-decision-matrix-2026-09-06.md#15-recommendation-judgment-from-context-to-worthwhile-possibilities) and [NYC specimens](nyc-recommendation-judgment-specimen-pack-2026-09-07.md): character, situational fit and feasibility as separate judgments.
- [Integration roadmap §2 / CV-3](complete-system-integration-roadmap-2026-09-05.md): Content supplies this handoff; Integration owns shared implementation and landing. Life remains a separate continuity owner.
- [Bounded production decision](../decisions/2026-09-06-bound-source-production-worker.md): no optional provider/model production or enqueue on ordinary root reads; activation remains separately gated.

Snapshot: workspace `ffcb533`, backend main `ea816526d`, mobile branch `codex/entity-object-design-completion` at `6296287ef`. Working-tree strategy edits were present. The matrix and Place canon include this lane's prior uncommitted amendments; treat them as inspected working state, not proof of deployment. This is a targeted code/doc audit, not a claim to have reread every recent document or tested all app routes.

September 7 review amendment: the follow-up review observed backend `778494b62` and mobile `3f199d470` and rechecked acquisition, ingestion and receiving boundaries. It retains the architecture, brings supplier feasibility and portfolio receiving checks forward, adds ready-supply and event-lifecycle requirements, and makes S0–S4 overlapping integration packages rather than a waterfall. The original test receipt in §10 was not a fresh test run against those later heads; the follow-up execution receipts below now record bounded repairs landed after that review. No provider, worker or production activation was performed.

## 2. What exists, and what it does not yet establish

| Boundary | Concrete implementation inspected | Reuse and limitation |
| --- | --- | --- |
| Broad POI acquisition | [Places factory](../../travel-agent/backend/places/factory.py), [service](../../travel-agent/backend/places/service.py), [metered linker](../../travel-agent/backend/places/linker.py) | Foursquare primary and Google fallback when keys exist; nearby/text discovery and known-place status. Not a general event or experiential-quality supplier. Configured credentials and live health were not checked. |
| Nearby candidate acquisition | [discovery.py](../../travel-agent/backend/places/discovery.py), `discover_nearby` | Corpus-first; default `min_corpus=3` prevents provider expansion once enough nearby rows exist. Count is not evidence that the current purpose has been served. |
| Nearby ranking | [taste.py](../../travel-agent/backend/places/taste.py), `_score_row` | Distance, corpus trust, saved/affinity/stated-category signals. Non-corpus candidates without a taste match are dropped. This blocks an unseeded cold start and some world-first possibilities by policy. It is not the only recommendation path in the app. |
| Places text search | [search.py](../../travel-agent/backend/places/search.py), [search dispatch](../../travel-agent/backend/search/dispatch.py) | Context-safe search over local retrieval; venue BM25/hybrid discovery is not internet search. General catalog search and external candidate discovery are distinct capabilities. |
| Canonical identity | [entity resolution](../../travel-agent/backend/core/entity_resolution.py), [existing-ref enrichment](../../travel-agent/backend/places/canonical_opening.py) | Existing external mappings, redirects, viewer-safe reads and explicit owner-shell resolution. Reuse this owner. Candidate discovery must not silently materialize global catalog rows. |
| Source policy and operational evidence | [source_policy.py](../../travel-agent/backend/places/source_policy.py), [cache.py](../../travel-agent/backend/places/cache.py) | Provider-specific map policy, raw-payload exclusion and per-field expiry exist. Current policy is not sufficient evidence of lawful retention of every normalized field; see §3. |
| Dated experiences | [Ticketmaster ingester](../../travel-agent/backend/ingestion/ticketmaster.py), [ingestion base](../../travel-agent/backend/ingestion/base.py), [occurrence helpers](../../travel-agent/backend/core/db/experiences.py) | Source/source-ID upsert and one-off/recurring experience support already exist. Ingestion stores raw payloads and marks experiences for embedding; it is not a selective, rights-cleared recommendation admission path by default. |
| Event lookup | [Ticketmaster tool](../../travel-agent/backend/core/tools/ticketmaster.py) | A separate query tool exists. It loses timezone/performer-slot detail in its output and defaults to Lisbon/PT when location is not supplied. Do not describe its presence as a general NYC supply path. |
| Local event delivery | [Places experience previews](../../travel-agent/backend/places/experiences.py) | This particular producer requires a membership-checked dated Trip. It returns nothing for an ordinary city scope. Other readers, including the map, have date filters; do not claim all event access is Trip-only. |
| Web research | [WebSearchTool](../../travel-agent/backend/core/tools/web_search.py) | Tavily, domain filtering, circuit breaking and live-mode guards exist. Output includes snippets and an optional provider answer, not a complete claim-grounding/extraction protocol. Depth currently changes with `max_results > 5`, conflating recall count and research cost. |
| Practical judgment | [canonical owner reads](../../travel-agent/backend/concierge/agentic_facade/canonical_owner_reads.py), [value composition](../../travel-agent/backend/lived_experience/value_composition.py) | Current cached venue facts feed explicit `place.open_now` assessment with identity, audience and per-field deadlines. This is useful progress, not validation of a future ferry, ticket window, accessibility route or performer set. |
| Prepared value and root delivery | [prepared Source serving](../../travel-agent/backend/root_projection/v2/source_contribution_serving.py), [canonical executor](../../travel-agent/backend/root_projection/v2/source_contribution_canonical_executor.py), [root composition](../../travel-agent/backend/api/services/root_composition.py) | Read-only private prepared-result admission and separately bound production exist. The private Source worker is not automatically a public city-content publisher or a broad external discovery agent. |
| Mobile receiving surface | [root data bridge](../../travel-app/data/rootProjections.ts), [Places root](../../travel-app/components/places/PlacesRootExperience.tsx), [workspace](../../travel-app/components/places/PlacesWorkspace.tsx) | Governed runtime/compatibility paths and a mature renderer exist. Extend their supported candidate/destination contracts only where necessary; no new recommendation screen or fifth root. Native rendering was not exercised. |

## 3. Initial audit findings and remaining work

The findings below describe the initial audit snapshot. §10 records subsequent
repairs; §11.1 records the latest code recheck and remaining limitations. In
particular, the POI fallback, source-wide invalidation and pagination findings
have bounded repairs, while complete root network isolation, event fidelity
and selective regeneration remain unfinished.

### A. Legacy Foursquare integration and obsolete cost assumptions

Both the [operational adapter](../../travel-agent/backend/places/foursquare.py) and the [research helper](../../travel-agent/backend/research_agent/tools/foursquare.py) target `/v3`. Foursquare documents May 15, 2026 deprecation for that family. Its current search endpoint uses `places-api.foursquare.com/places/search`, bearer authentication and an explicit API-version header. This is a documented migration mismatch; no live outage was reproduced. [Deprecation notice](https://docs.foursquare.com/developer/reference/upcoming-changes), [current search reference](https://docs.foursquare.com/fsq-developers-places/reference/place-search).

The [settings comments](../../travel-agent/backend/places/settings.py) still reason from roughly 2,000 free Foursquare calls/day and $17/1,000 Google Details calls. Those assumptions cannot price the present implementation: Foursquare's published Pro allowance is now 500 calls/month; Google's requested opening-hours fields belong to the Enterprise Details SKU. Update estimates from the actual field masks, account terms and operations. [Foursquare pricing](https://foursquare.com/pricing/), [Google field-to-SKU mapping](https://developers.google.com/maps/documentation/places/web-service/data-fields).

### B. A real root-read acquisition path remains

The inspected call chain is:

```text
Places feed / v2 Places / v2 Places runtime GET
  -> build_places_feed
  -> quiet-posture build_nearby_set
  -> discover_nearby_ranked (cache miss)
  -> discover_nearby (thin corpus)
  -> metered provider discovery (if configured)
```

Evidence: [routes](../../travel-agent/backend/api/routes/root_projections.py), [feed builder](../../travel-agent/backend/places/sections.py), [nearby producer](../../travel-agent/backend/places/nearby.py), and discovery/taste files above. Home's [portfolio adapter](../../travel-agent/backend/root_projection/v2/home_portfolio.py) also has a Places-feed reader; inspect enabled callers when closing the boundary.

The newly implemented **prepared Source read** is provider-free; that does not prove the entire root request is provider-free. This legacy branch contradicts the newer ordinary-read contract under the named conditions. Do not add more provider work to it. Separate acquisition from root serving, while preserving corpus and valid prepared value on a miss. No runtime network call was made in this audit.

### C. Private or normalized data is not automatically persistence-safe

`normalized_owner_shell` retains name, coordinates and categories. The cache strips raw payloads but still writes normalized provider fields. The boolean provider policy does not express field-level retention permission or deletion deadlines for shell values.

Google's policies distinguish indefinitely retainable Place IDs from restricted content; its current non-EEA service terms allow Places coordinates to be cached for up to 30 days and prohibit Places API content in conjunction with non-Google maps. That does **not** grant blanket 30-day retention for all fields, or indefinite retention because a shell is private. Review the applicable account agreement and product-specific exceptions before changing policy; this report is not legal clearance. [Places policies](https://developers.google.com/maps/documentation/places/web-service/policies), [service terms §14](https://cloud.google.com/maps-platform/terms/maps-service-terms).

Preserve the existing provider-map distinction, but audit names, categories, coordinates, normalized operating facts and derived representations separately. A test proving raw reviews are excluded is not proof that retained fields are licensed. Do not delete current records as part of this research handoff.

### D. Event normalization needs repair, not a new universal event model

The Ticketmaster ingester currently:

- applies `+00:00` to `localDate + localTime` when `dateTime` is absent;
- substitutes a 2099 date/midnight for missing start fields;
- builds city-date search bounds in UTC rather than resolving the requested local window;
- permits 25 pages of 200, although documented deep paging requires `size * page < 1000`;
- defaults missing currency to EUR and does not preserve a separate performer-slot identity.

The first four can change which event is offered or when someone attends. Repair unknown/timezone semantics and page bounds before widening ingestion. Preserve rescheduled, postponed, cancelled and unknown-time distinctions rather than treating any active record as operationally ready. [Current code](../../travel-agent/backend/ingestion/ticketmaster.py), [Discovery API reference](https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/).

### E. Quality admission is using the wrong proxies

Corpus membership and a taste match are useful signals, but neither establishes a worthwhile experience for today's purpose. Replace the exclusive taste prerequisite with evidence-backed admission, then rank by purpose and conditions. This does **not** mean admitting every generic provider result. Sparse/no-history cases still need a concrete reason to consider the option; unfamiliarity is neither a defect nor automatic serendipity.

### F. Ingestion invalidation is broader than the changed batch

After any nonempty batch, [ingestion base](../../travel-agent/backend/ingestion/base.py) calls `_mark_experiences_dirty`. Its query selects **all active experiences from that source**, not just the batch's affected IDs or materially changed records. Its conflict update sets `dirty=True` even for previously clean rows. The docstring's suggestion that only non-clean records are marked is not enforced by the query.

This establishes unnecessary embedding-work eligibility, not a measured production bill. Track affected identities and material field changes; invalidate only dependent brief/vector work. An unchanged refresh must not dirty the catalog, and a schedule/status correction must repair practical claims even when it does not require rebuilding descriptive content. Close this before expanding ingestion volume; test a one-record update alongside unrelated clean records, including another destination from the same source.

## 4. Source strategy, by job

All provider facts below were checked against public primary documentation on September 7, 2026. Commercial suitability remains account- and use-specific. None of the providers was queried through a paid Vesper integration in this round.

| Source path | Recommended job | Important limit / decision |
| --- | --- | --- |
| Current Foursquare Places API | Early POI comparison candidate; existing adapter knowledge helps investigate location/category/text discovery and exact status where supported | Existing code is not a supplier-selection decision. Compare migration effort, useful coverage, current fields, account-specific caching and attribution before choosing migration over replacement. Being powered by open-source POIs does not make the API's entire response freely reusable. [PAYG license](https://foursquare.com/legal/terms/apilicenseagreement/). |
| Google Places New | Compare exact identity and operational-field support; use selectively where its result materially helps | Field masks affect cost; attribution, retention and map restrictions constrain reuse. Not a default source for populating our permanent world database. See §3C. |
| Ticketmaster Discovery | Evaluate mainstream dated music, theater and similar inventory using the existing integration | Venue/attraction/event search is useful, but not proof of independent-nightlife or community-program coverage. Published default quota: 5,000 calls/day and 5/second. [API](https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/). |
| Organizer/institution pages via bounded research | Fill decisive gaps: Art Cart versus workshop, ferry fare rule, exact music date/set, exhibition character | Search discovers a source; exact-source evidence supports the claim. Page access, robots/terms, extraction reliability and permitted reuse need domain-specific handling. No bypassing access failures or treating snippets as current inventory. |
| Tavily, already integrated | First web supplier to measure; public search queries and targeted source discovery | Separate search depth from result count; validate source passages rather than treating the generated answer as another independent authority. |
| Exa | Benchmark challenger for search plus targeted page content if Tavily misses the job or costs more per resolved question | Do not integrate both by default or presume the lower search price means a better completed recommendation. [Endpoint pricing](https://exa.ai/pricing). |
| RA / specialist partnerships | Potentially important for independent electronic music beyond mainstream ticketing | RA publicly describes an events-API partnership with SoundCloud. That establishes an API exists, not open access or permission for Vesper. Treat access as a partnership question, not an undocumented endpoint to scrape. [RA announcement](https://ra.co/news/80904). |
| Eventbrite | Known-event/organizer continuation where access is supported | The official public event-search endpoint is deprecated and documented as shut down since 2019. Do not plan against marketing language implying an unrestricted citywide search API. [API reference](https://www.eventbrite.com/platform/new/api). |
| PredictHQ | Possible later licensed event-supply comparison if coverage gaps justify procurement | Its event-search API exists, but public API documentation alone does not establish consumer redistribution rights, price or detailed participation evidence. Not the first new dependency. [Official API specification](https://api.predicthq.com/docs/). |
| FSQ Open Source Places | Optional regional identity substrate if measured repeated demand makes local lookup worthwhile | Apache-licensed dataset access is distinct from PAYG API terms. Current delivery uses a Places Portal/Iceberg catalog. Import only a justified region/field subset; monthly/batch identity data is not open-now truth. [Access and license](https://docs.foursquare.com/data-products/docs/access-fsq-os-places), [dataset announcement](https://foursquare.com/resources/blog/products/foursquare-open-source-places-a-new-foundational-dataset-for-the-geospatial-community/). |

**Ticketmaster commercial checkpoint:** its general terms limit content caching to reasonable service periods, reserve restrictions on large non-user-driven call volumes, and contain a restriction concerning revenue derived from API use. Obtain applicability/permission for our paid and proactive product before treating the public quota as production authorization. Do not infer that a free key settles those questions. [General terms](https://developer.ticketmaster.com/support/terms-of-use/).

### Matched requests to evaluate

Use the existing four specimens as known-answer probes, plus open discovery tasks where the target name is withheld. A provider finding a named venue is not evidence it would discover the best experience independently.

| Specimen | Structured path | Distinctive/decisive evidence path | Deliverable and pass condition |
| --- | --- | --- | --- |
| Governors Island | Match island/site and departure geography using supported POI sources | Park material plus ferry operator | Distinguish destination, way to explore and transport condition; do not promise an afternoon fare using a morning exception. |
| Friend lunch | Nearby/text search in the stated meeting area | Food-counter/operator evidence; qualified experience observations when relevant | A flexible catch-up option without inventing quiet, seats or a shared food preference. |
| Saturday electronic music | Date/location/category event query, then exact occurrence lookup | Organizer/ticketing page and performer timetable | Correct local date, event/slot distinction, known/unknown admission and exact external continuation; cover a specialist alternative as well as a mainstream one. |
| Art Cart / museum | POI search can find the host, but may not identify the offering | Activity/calendar/exhibition pages | Resource versus registered workshop versus exhibition is explicit; an editorial preview can survive an unresolved admission check. |

Run structured-only, web-only and hybrid conditions on the same requests. Record missing candidates and decisive missing fields—not just result count. Supplement these well-documented examples with a neighborhood event and a low-documentation venue before making market-coverage claims.

## 5. The smallest coherent supply contract

This is a proposed **logical handoff**, not approval for a new schema, store or service. Map it onto current typed references, observations, research primitives and root candidates first; request model/API changes only for demonstrated gaps.

| Information | Meaning and existing owner direction |
| --- | --- |
| Request purpose and scope | Current job, spatial boundary, local time window, wanted participation and hard constraints; private context stays with the request/context owner. |
| Candidate reference | Canonical entity when resolved; otherwise exact provider identity or public source reference. No false canonical ID and no automatic save/materialization. |
| What is being recommended | Place, recurring resource, dated event, particular performance/admission window, or a way to experience one. Reuse experience/occurrence facilities before adding structures. |
| Evidence | Source, exact supported claim/passage, observation time, applicable time, uncertainty and contradiction. Private user evidence remains separate from public-world evidence. |
| Rights and expiry | Field-specific storage, reuse, display and attribution policy with version; validity expiry and legal retention deadline are different clocks. |
| Judgment | Distinctive reward, situational rationale, tradeoff, missing evidence and why an alternative loses. Not a universal quality score. |
| Practical dependency | Exact question/subject whose answer can change this claim. Current `place.open_now` support must not be relabeled as ticket or future-hours verification. |
| Continuation | Existing entity depth, supported medium, canonical action owner or exact source/provider link. “See tickets” is not “tickets available,” and creates no Vesper booking obligation. |
| Cost and repair | Work/request identity, operation/field tier, calls including retries, elapsed time, tokens, cache eligibility, supersession dependencies and invalidation owner. |

The live engine consumes this grounded candidate and current owner evidence; it does not become the crawler. It can downgrade an open-now claim when evidence expires without deleting a still-useful explanation. A future set-time or admission assessor should extend the existing claim-specific assessment boundary, with its own evidence contract.

### Three acquisition modes, one receiving system

1. **Explicit investigation:** a user asks for help; bounded discovery happens within that request's authority. Return ready value without waiting to enrich a Home card.
2. **Public editorial preparation:** a selected city/topic/time window supplies reusable world material when source rights and an execution budget permit. Public queries must not contain private context. Existing content/research owners are the destination; do not repurpose a private Source-contribution record as a global publication.
3. **Permitted personal preparation:** an accepted trigger may combine eligible private context with available world evidence. It uses existing authorized work/lease/readback boundaries; opening Home is not the trigger and Keep is not a watch.

In every mode, ready results enter the current root/owner contracts. No universal recommendation service should take over identity, personal memory, Life organization, provider transactions or shared arrangements.

### Ready value before personal history

Provider-free root reads must not become value-free reads. Before activating a supported-market Home/Places supply path, Integration and Content must name the existing public-content producer/readback owner and record:

- the initial location, topic and time-window coverage and the ready material a newcomer can actually receive;
- the permitted material store, independently of private Source preparation, and its read-only receiving path;
- the accepted preparation/refresh trigger, execution budget, deduplication key, freshness deadline and expiry owner;
- the fallback when supply is empty, expired or unavailable, preserving useful current material and distinguishing those states from "nothing worthwhile exists."

Use a bounded, rights-compatible initial collection and existing content/research ownership, not city completeness or a new publication service by default. Its exact producer/storage binding is an implementation checkpoint, not an already implemented capability. An explicit request may separately acquire new options without a dossier or save. A request affordance can supplement a sparse surface, but "ask us to generate something" cannot be the entire default value proposition for a supported newcomer. Outside supported coverage, be honest about the limit; do not manufacture local readiness.

The no-production-on-GET boundary is unconditional: it must not be left open while supply is built. Test the cutover with preserved valid material and the bounded fallback; do not describe an empty safe surface as completed consumer supply. Wider rollout waits for the ready-value checkpoint.

## 6. What to retain and index

| Data class | Proposed disposition | What not to do |
| --- | --- | --- |
| Independently supported canonical identity and permitted external IDs | Durable identity owner with corrections/redirects and field provenance | Treat a provider match as permission to retain every attribute forever. |
| Provider name/location/category/status fields | Only the provider/account's allowed fields and duration; preserve attribution and deletion obligations | Assume JSON normalization, a private shell or a short freshness TTL makes retention lawful. |
| Promising retrieved candidates | Request-local by default; short reusable batches only where allowed and useful | Persist every search result or every rejected option into the canonical catalog/Qdrant. |
| Durable public interpretation | Selectively retain source-supported, rights-compatible research primitives; version and derive retrieval indexes when useful | Require a long dossier or publish model knowledge without evidence. |
| Dated events and schedules | Retain justified current windows with revision, cancellation and expiry; preserve exact occurrence references | Embed every event by default or confuse a series/venue with this performance. |
| Images, reviews, audio and source text | Separate content/license policy; prefer authorized media or supported external continuation | Infer redistribution, embedding or permanent storage rights from discoverability. |
| Private recommendation and relationship context | Existing viewer/scope-specific, revision-bound owner rules | Cross-user cache a rationale or leak a friend's private preference into a public query. |
| User-authored keeps, tickets and actual outcomes | Existing Source/Life/consequence ownership, independently of the discovery cache | Delete a user's own ticket because a provider observation expired, or keep an unlicensed provider description because the user saved its ID. |

The initial ready-value path in §5 needs bounded permitted material, not a comprehensive index. Beyond that minimum, we may expand a **small hot working set** of frequently useful places, source endpoints and upcoming offerings in supported markets. Expansion is driven by permitted reuse, measured demand and distinctive value—not city completeness. Source catalog entries can record where and how to look without mirroring all the source's content.

An index pays for itself only when permitted avoided retrieval and better retrieval utility exceed refresh, reconciliation, hosting and editorial costs. Do not re-acquire restricted content solely to disguise prohibited retention. A switch to licensed or independently gathered data needs recorded lineage, not a silent provenance replacement.

## 7. Economics: price the completed useful answer

Published first paid-tier reference prices, not contracted rates or measured bills:

| Operation | Reference price | Consequence |
| --- | --- | --- |
| Foursquare Pro | $15 per 1,000 after the published 500-call monthly allowance | A 500/day code limit is not a free allowance; premium fields have separate pricing. [Pricing](https://foursquare.com/pricing/). |
| Google Text/Nearby Search Pro | $32 per 1,000; published monthly free cap 5,000 per SKU | Avoid expanding fields or repeating unchanged acquisition through root reads. |
| Google Details Enterprise | $20 per 1,000; published monthly free cap 1,000 | Relevant to the current opening-hours field mask, not the cheaper Essentials price. [Google prices](https://developers.google.com/maps/billing-and-pricing/pricing). |
| Tavily Search | Basic 1 credit, advanced 2; PAYG $0.008/credit | $0.008/$0.016 per search before other costs. Extract is separately priced. [Credit rules](https://docs.tavily.com/documentation/api-credits). |
| Exa Search / Contents | Standard search $7/1,000 up to 10 results; separate contents $1/1,000 pages | Additional results, summaries and deeper modes change the bill. [Prices](https://exa.ai/pricing). |

**Illustrative arithmetic:** two Google Pro searches, three Enterprise detail lookups and two Tavily basic searches cost approximately **$0.14 in these acquisition operations**, before free allowances, volume discounts, model tokens, extraction, routing, infrastructure or retries. Ten thousand such investigations would be approximately **$1,400 before those other costs**. This is a scenario, not a measured Vesper recommendation cost or an assertion that every question needs that work.

Budget for:

```text
completed-answer cost = discovery + detail/verification + extraction
                      + model input/output + retries + refresh + serving

cost per useful result = total acquisition/production spend
                        / results meeting the reviewed evidence-and-value bar
```

Useful controls: public-query deduplication where permitted; exact-ID detail retrieval; narrow field masks; a shortlist before expensive verification; extract the passages that settle a question; reuse current admissible work; bound retries; stop with a useful qualified answer. Restrict only costly optional enrichment when its budget is exhausted—do not unnecessarily remove already available practical help or editorial value.

The existing [daily budget gate](../../travel-agent/backend/places/budget.py) is a read-count precheck followed by later audit writes, not an atomic multi-worker reservation. Unknown providers default to unlimited there. Extend existing budget infrastructure for operation-aware reservation/accounting before relying on it as a strict spend cap. Do not create another uncoordinated billing ledger.

### Bounded measurement proposal

Run initial feasibility comparison during S0, before supplier-dependent migration or integration decisions; S4 repeats and extends it for operating economics. Before any paid run, approve the provider accounts, terms, exact request set and total dollar cap. Initial comparison proposal: the four cases plus two coverage-gap cases, structured-only/web-only/hybrid, at most two discovery requests and three detail/extraction requests per case-condition run, summed across suppliers. Retries and pagination consume those operation ceilings rather than adding free attempts; multi-page/extraction billing also counts toward the dollar cap. A hybrid path shares the budget rather than receiving each provider's full allowance. The illustrative $0.14 scenario above is separate from this smaller experimental envelope. Use fake or permitted recorded responses first; no proposed numeric batch limit grants execution authority.

Measure usable-candidate yield, decisive-field completeness, exact identity/time accuracy, cost per usable result, p50/p95 completed-answer latency, retry/unknown rate and rights-compatible reuse. Small batches expose failures; they do not establish market recall or statistically reliable tail latency. Compare at equal ceilings without requiring every path to waste the full budget.

Review usefulness as well as field completeness: does the option offer a concrete reward, fit the actual purpose, differ meaningfully from its alternatives and permit a low-friction next step? At the portfolio checkpoint, inspect repetition and variety across Home/Places without equating clicks, saves or attendance with enjoyment. An accurately identified but uninteresting list is not a passing recommendation.

## 8. Implementation sequence and checkpoints

These are packages within Integration's CV-2/CV-3/CV-4 program, not a replacement roadmap or a demand to prove one loop before building the system. **Package numbers express responsibilities, not a strict waterfall.** No calendar estimate is asserted before the first checkpoint.

| Execution stage | Packages that contribute | Checkpoint before widening |
| --- | --- | --- |
| Contract and feasibility | S0A receiving fixtures and S0B supplier evaluation; S3 contract mapping starts here | All four value families have a concrete receiving/continuation mapping; external dependencies and coverage limits are recorded before supplier-specific commitments. |
| Targeted foundation repairs | S0A read/budget boundaries, S2 normalization/invalidation, S3 ready-value design | Safe reads preserve valid value; ingestion changes do not dirty unrelated records; supported-market fallback and supply ownership are explicit. |
| Connected supply | S1 purpose-aware discovery, S2 event lifecycle, S3 production/readback/delivery | Explicit discovery and scoped prepared supply reach actual consumers, with refresh, expiry and exact continuation. |
| Expansion review | S4 repeated-use economics and coverage evaluation | Expand a supplier, time window or region only when useful yield, rights, consumer quality and refresh cost support it. |

Fixture and provider-independent work can overlap supplier research. Paid comparison, supplier activation and shared-contract changes retain their existing approvals; this table neither dispatches agents nor creates a new lane. Integration lands common composition changes serially.

### S0 — Establish receiving contracts, supplier feasibility and safe reads

**Owner:** Integration, with Content supplying provider decisions and Entity owner consultation on shell fields.

**S0A — repository-safe contract and boundary work:**

- Map the §5 handoff onto existing typed references, owner evidence, root candidates and mobile destinations before choosing new structures. Exercise the four specimens end-to-end with fixtures, including an unfamiliar place without a dossier, an unresolved exact provider/source reference, a recurring offering versus a workshop, and external continuation without automatic save/catalog materialization. Record unsupported mappings rather than inventing canonical identities.
- Trace every active root caller to network-capable Places functions; add boundary tests that use sparse corpus, empty ranked cache and fake configured providers.
- Split root-serving reads from explicit acquisition. A root miss preserves current useful material or uses the explicit sparse/unavailable fallback; it never enqueues enrichment. Carry the §5 ready-value requirements into S3 before calling the supported-market cutover complete.
- Identify the existing shared budget reservation/accounting path, including nested requests, retries and pagination, and test bounded failure behavior. Do not claim strict multi-worker spend enforcement from the current precheck alone.

**S0B — early supplier feasibility, with separate external gates:**

- Inventory field-level rights, expiry and attribution for cache, shell, media and derived evidence. Confirm the actual Foursquare account/version and Google agreement. Do not migrate or delete retained data without an exact disposition plan.
- Price actual field masks and operations and conduct the §7 bounded comparison once its account/terms/budget approvals exist. Establish initial per-family source, coverage and reuse limits before committing supplier-specific integrations. An existing adapter alone does not justify migration.

**Exit/checkpoint:** S0A has mapped portfolio receiving paths, zero provider/model/enqueue calls from ordinary Home/Places reads under cold-cache fixtures, and a concrete S3 ready-value/fallback handoff. S0B has the reviewed field-disposition matrix and an evidence-backed supplier/migration decision for each activated family, or an explicit unresolved dependency. Do not label S0B complete from fixtures alone; independent S1/S2/S3 contract work need not wait for it. Do not confuse S0A boundary safety with populated consumer supply.

### S1 — Build purpose-aware discovery over the existing boundaries

**Owner:** Integration; Content reviews outputs.

Start against S0A contracts and fixtures; connect a supplier only within S0B's cleared scope. Feed real integration findings back into S3 continuously rather than waiting for S1 and S2 to finish.

- Replace count-only search stopping with a bounded assessment of whether available candidates cover the request. Keep cheap corpus reuse; avoid automatic full fan-out.
- Extend candidate admission beyond required taste matches. Test independently worthwhile unknown options, strong generic cold-start value, relevant history and history that should be ignored.
- Use reviewed public place/category queries through the existing metered linker; private reasons remain internal. For general research, use a purpose-appropriate public query without raw conversation or private friend constraints.
- Separate Tavily depth/field needs from number of results. Add exact-source investigation only for claims that change selection.

**Exit/checkpoint:** offline matched fixtures produce substantive options without a dossier/Trip prerequisite, maintain hard constraints and never manufacture a personal bridge. Review all four specimens together, including the cases where generic and personalized choices should agree.

### S2 — Make offerings and local event windows first-class in discovery

**Owner:** existing experience ingestion/query owners, landed through Integration.

- Repair Ticketmaster local-time, unknown-time, paging and currency handling. Preserve provider status distinctions; do not invent confirmed times from missing values.
- Accept explicit local date windows for ordinary city discovery without inventing a Trip. Reuse current occurrence helpers and map/date semantics.
- Identify the minimum addition, if any, for performer slots and admission-window evidence. A proposal may be source-bound before a schema extension; exact operational claims require structured support.
- Keep provider inventory and organizer evidence separate. Retain only justified admitted observations; do not automatically mark every retrieved event for embedding.
- Repair the source-wide dirtying in §3F before expanding ingestion: retain affected IDs, compare meaningful field changes and invalidate only dependent work. Cover unchanged refresh, one changed record, unrelated clean records and schedule-only changes.
- Name the existing owner and accepted trigger for exact-ID refresh, reschedule, cancellation and expiry. Specify which public observations and private projections depend on each revision, and how late/out-of-order updates are rejected. Search omission is not cancellation; a failed refresh does not renew freshness. Never imply a personal watch merely because an option was shown or kept.
- Follow the [contribution/repair contract](../systems/contribution-and-consequence.md#8-receipt-and-causal-repair): provider expiry or cancellation repairs dependent practical claims, not independently retained user tickets, authored contributions or still-supported interpretation. Map this onto existing owners/outboxes before proposing new lifecycle machinery.

**Exit/checkpoint:** Saturday-to-Sunday performer case, event reschedule/cancellation, search omission, failed/late refresh, recurring resource versus workshop, and date-only/TBA fixtures preserve uncertainty and exact continuation. Changes reach dependent consumer claims without deleting independent user material or dirtying the provider's unrelated catalog. Before advertising specialist coverage, obtain actual source-access and coverage evidence.

### S3 — Connect selected supply to current judgment and delivery

**Owner:** Integration; Entity and Life receive narrowly scoped contracts.

**Begin receiving-contract fixtures alongside S0A.** S3 owns production completion, but is not the first point at which S1/S2 outputs encounter Home/Places or exact continuations.

- Bind approved acquisition triggers through the existing execution/lease/readback framework without treating the private Source producer as a universal public supplier.
- Complete the §5 ready-value record: concrete existing public producer and stored-result owner, initial market/time/topic scope, bounded admitted material, permitted refresh trigger/budget and empty/expired/unavailable fallback. Public preparation and private composition remain separate. Do not defer all newcomer supply to S4 or require a rich personal history to populate supported surfaces.
- Carry evidence refs, field validity, rights and exact continuations into existing candidate/root contracts. Use current practical assessment only for the questions it actually supports.
- Verify Home/Places receive the same authoritative result with different appropriate composition; source changes or expiry repair only dependent claims. Preserve an interesting explanation when a practical option becomes unavailable.
- Keep optional saves and shared consequences with their existing owners. Do not expand Chat or Life design in this package.

**Exit/checkpoint:** complete source→judgment→Home/Places→exact-depth/provider-link paths for the four value cases, with expired/conflicting/missing evidence variants. A supported newcomer receives substantive ready value without a dossier, save, extra questionnaire or generation on GET; explicit investigation can reach beyond the prepared set. Confirm actual producer/readback binding, not just a renderable fixture. No new screen family, booking infrastructure or global recommendation truth store. Native QA, real-supply acceptance and production activation remain separate gates.

### S4 — Measure repeated use and selectively expand

**Owner:** Content/Integration with founder budget approval.

- Repeat and extend the §7 comparison under the relevant provider/rights/budget gates. Initial supplier selection belongs in S0B, not here after supplier-dependent implementation.
- Revisit the primary POI supplier and specialist/web gaps from measured consumer yield; add Exa, specialist access or an aggregator only for a demonstrated shortfall.
- Measure repeated questions, refresh overhead, portfolio variety and allowed reuse before expanding S3's initial public preparation, adding targeted source subscriptions or importing an open-data identity subset.
- Stop expanding a source family if useful yield is poor, rights defeat the intended experience or refresh cost consumes its value. Preserve supported adjacent capabilities.

**Exit/checkpoint:** a per-family source/coverage/cost contract and explicit activation scope, not “world coverage complete.” Revise budgets and supported promises from the results.

## 9. What AI changes—and what it does not

AI can translate present purpose into different retrieval directions, interpret heterogeneous evidence, identify a missing decisive question and assemble a compact experience from a small candidate set. That reduces the need to pre-author every possible query/category combination. Our existing general web tool is a useful starting point, not proof that this judgment is implemented.

AI does not provide authoritative schedules, licensed data, exhaustive recall or identity simply by writing confidently. New search/grounding products should be swappable acquisition adapters, not the owners of personal context or canonical state. Preserve inspectable evidence and evaluation cases so a better supplier/model can replace the current one without rewriting Home, Places or Life.

The defensible work is **what we ask, what we verify, how we judge it for this moment, and what authorized continuity improves next time**. A proprietary copy of every venue/event is neither necessary nor sufficient.

## 10. Verification and open decisions

### September 7 execution receipts

- **S0A / targeted invalidation — landed in backend `90da623d3`:** the
  experience ingester now uses a NULL-safe material-change predicate on its
  existing `(source, source_id)` upsert. Unchanged provider refreshes do not
  advance `updated_at`, count as updates, or enter brief regeneration. Only
  returned changed IDs are sent to `experience_brief_state`; the previous
  source-wide active-row sweep is gone. This changes invalidation scope, not
  the storage schema or embedding worker.
- **S0A / POI discovery boundary — landed in backend `6130da1d3`:** nearby discovery
  accepts an explicit `allow_provider` boundary. Home, the ordinary Places
  projection/feed, and the nearby Places section pass `False`; the existing
  member-checked map discovery remains the explicit provider-capable path.
  Cache keys include this boundary. Thin-corpus root reads therefore return
  corpus material or a sparse result without invoking the POI fallback. The
  follow-up C0 receipt below closes the same boundary for optional reachability
  and travel-time ranking. This still does not provide the §5 ready-value pool
  for newcomers.
- **S0A / routing refinement boundary — landed in backend `0cb5e9325` and
  documented in `f3531bb05`:** `allow_provider=False` now gates both the
  isochrone/reachability canary and Matrix travel-time ranking. With routing
  flags enabled, ordinary Home/Places reads stay corpus-only or honestly sparse;
  explicit provider-capable map/discovery calls retain their prior behavior.
  New regressions exercise cold-cache root calls and assert neither routing
  helper is invoked. This is a nearby serving-boundary receipt, not a claim of
  complete provider isolation or newcomer ready supply.
- **S1 / bounded evidence handoff — landed in backend `8cd543260`:** the quick
  research path now preserves its legacy graph-state keys while attaching a
  typed `bounded-research-result-v1`. The result keeps request purpose/scope,
  source evidence, supported material, unresolved gaps, stop reason and
  measured usage together. It intentionally marks no source reusable and does
  not create a catalog row, dossier, vector or review write. Focused research
  coverage is **30 passed**; this is a consumer handoff receipt, not proof of
  supplier quality, identity resolution or canonical promotion.
- **S3 / explicit private-preparation handoff and first publication fence —
  landed in backend `4ec001ab7` with the bounded lease repair in `6a502fae2`,
  exact readback receipt in `e944ac954`, request-ref hardening in `72775a5bf`,
  and the inner-write fence in `872e92691`:** an explicit Source request now
  carries a content-free `ResourceRef` plus optional conversation/message
  provenance into the durable workflow, accepts only the
  `source_preparation_request` reference kind, rejects non-explicit or
  mismatched trigger references, uses the deployment lease rather than a
  historical default, and returns an actor-scoped workflow/result locator
  after successful readback. The inner Source publication path locks and
  verifies the claimed outer workflow in the same transaction, so a
  cancellation or lease takeover that wins the row lock cannot publish stale
  output. The submission adapter still does not enqueue, claim or produce
  work; public preparation remains a separate owner and activation decision.
  Focused workflow/worker/continuity/database coverage is **61 passed**;
  broader PostgreSQL interleaving proof remains open.
- **S1 / search-policy separation — landed in backend `84a650829`:** Tavily
  search depth is now an explicit tool/profile setting independent of result
  count. Direct legacy callers retain the prior fallback; current quick/deep
  research profiles explicitly remain `basic` pending a supplier-cost
  decision. Focused tool/handler coverage is **37 passed**. This changes
  configuration clarity and spend control, not provider activation or source
  quality.
- **S1/S3 / explicit disposition mapping — landed in backend `22fd90497`:** a
  write-free mapper now classifies a bounded result as `current_answer`,
  `reusable_observation`, `proposed_primitive`, or `deep_compilation`. Missing
  canonical identity or retention permission always caps the result at a
  current answer; editorial and deep paths require explicit requests, and
  unresolved gaps keep proposed primitives in review. Four focused regressions
  pass. This is a deterministic handoff seam, not canonical write-back or a
  source-rights grant.
- **S1 / source metadata and summary boundary — landed in backend `76e9dc41c`:**
  normalized sources now retain page title/publication metadata, while a
  provider-generated synthesis is marked `provider_summary` and excluded from
  canonical observations unless a traceable page supports the claim. This
  removes a provenance ambiguity without discarding useful graph context.
  Focused converter/Foundry coverage is **12 passed**.
- **S2 / event paging guard — landed in backend `5421c66b7`:** the existing
  Ticketmaster fetch keeps its 200-item page size but caps a refresh at five
  pages (the documented first-1,000-result window). A regression fixture proves
  a larger provider-reported `totalPages` value cannot extend the request beyond
  pages 0–4. This is a request-safety bound, not evidence of event coverage or
  permission for proactive refresh.
- **S2 / on-sale temporal guard — landed in backend `ba4b893a0`:** Ticketmaster
  normalization now preserves an on-sale timestamp only when it is parseable
  and timezone-aware; malformed or timezone-less values remain unknown. Two
  regression cases pass in the event normalizer suite. This improves temporal
  fidelity without choosing an unknown-time schema or enabling refresh.
- The focused combined receipt across ingestion/Ticketmaster, Places discovery/
  taste/projection/feed, Home and root-projection suites is **210 passed, 9
  skipped, 16 warnings**. The skips and warnings are the existing Postgres
  leak-baseline cases. The full offline suite was attempted but interrupted
  after a local embedding-model initialization stalled; it is not reported as
  a green full-suite receipt.
- **Follow-up provider-independent receipt:** the expanded regression command
  covering those suites plus bounded-result, disposition, source-metadata,
  World Foundry and web-search policy tests is **270 passed, 9 skipped, 16
  warnings**. The skips/warnings remain the existing Postgres leak baseline.
  Two separately selected API-marked synthesis tests reached the Anthropic
  client but could not execute assertions because the configured account has
  no credit; they are not included in the offline green receipt.
- The Ticketmaster normalization portion of `90da623d3` also stops fabricating
  a `2099-01-01T00:00Z` start or a default `EUR` currency. Payload-declared
  timezone pairs are converted; unknown start times are rejected for now,
  leaving the schema decision for an explicit unknown-time representation.

These are bounded implementation receipts, not provider coverage, rights,
production activation, native QA or a claim that the ready-value checkpoint is
complete. The original audit receipt below remains historical context.

Original audit receipt, executed locally without live provider calls (not rerun for the roadmap-only review amendment):

```text
PYTHONPATH=. .venv/bin/python -m pytest
  tests/places/test_taste.py tests/places/test_discovery.py
  tests/places/test_source_policy.py tests/ingestion/test_ticketmaster_ingestion.py
  tests/core/test_value_composition.py
  -q -m 'not requires_postgres and not requires_api_keys'

98 passed in 2.04s
```

These tests corroborate existing behavior, including some policies this report recommends changing. They do not validate contracts, live endpoint support, full root network isolation, source coverage or human recommendation quality. No code was changed or fixes claimed.

Review-amendment documentation validation: metadata, relative-link targets,
code fences, whitespace and inventory classification passed for this handoff
and the integration-roadmap receiving note. The original full workspace inventory
check reported 33 unclassified documents outside this handoff's new entry;
that repository-wide check was not rerun for this amendment and unrelated
classifications were left untouched. This is not a claim that repository-wide
documentation gates pass. No backend/mobile tests were rerun for these doc-only edits.

Decisions remaining: provider/account permission and field retention; Foursquare migration versus replacement; specialist event access; unresolved-reference receiving/continuation gaps; local event/slot and refresh-owner scope; concrete initial public ready-supply owner and market coverage; accepted public/personal preparation triggers; measured budget and activation envelope. The architecture direction need not wait for all of them: extend the existing ownership model and design acquisition/serving separation now, using the complete bounded specimen portfolio until external prerequisites are resolved. Re-evaluate at the §8 checkpoints; do not add a new engine or index simply because a particular supplier or receiving mapping fails.

## 11. Content infrastructure execution plan

### 11.1 Objective, scope and fresh implementation baseline

**Build the machinery that finds useful world material, establishes what it
supports, retains the reusable portion, and refreshes only what changed.** It
must serve both practical discovery and substantive understanding: restaurants,
events, ordinary activities, cultural interpretation, cross-place comparisons
and attributed human perspectives.

This is the Content implementation detail beneath S0–S4. It does not replace
the integration roadmap or change the four product moves. Home, Places, Chat,
entity readers and the live engine are consumers. This lane owns supply and
its contracts; Integration owns shared root composition and execution wiring.
Source/Intake owns personal source custody; Life owns its continuity indexes
and projections. The work is organized around the
whole content lifecycle, with the portfolio in §11.4 exposing different needs
throughout implementation.

Latest planning recheck: workspace `8cbdc02`, backend `86f04589d`, mobile
`17eea1980` on `codex/entity-object-design-completion`. Backend `96cadfada`
contains this lane's latest content-hardening repairs; `86f04589d` is the
adjacent Integration deadline-forwarding repair. Concurrent strategy,
Integration and Home work is present and remains owned by those lanes. These
are inspection baselines, not a cross-repository release or deployed state.
The earlier planning baseline (`c0b3e12` / `5421c66b7`) and test receipts remain
historical. This pass inspects code and documents, not production configuration
or data, and does not rerun runtime tests for a documentation-only plan.

| Existing owner / path | What the code establishes | Implication for this plan |
| --- | --- | --- |
| [Source observations](../../travel-agent/backend/core/db/source_observations.py) | Immutable observation keys, source identity, content hash, retrieved time, policy version, payload reference and request context; initial lifecycle event | Reuse as public evidence provenance where retention is allowed. It is not itself a full page archive or a private Source-custody agreement. |
| [Entity facts](../../travel-agent/backend/core/db/entity_facts.py) and [place projections](../../travel-agent/backend/core/db/place_projections.py) | Evidence-linked facts, current adjudicated projections and projection outbox support | Stable identity and factual truth remain here; acquisition does not overwrite canonical entity rows as a side effect of finding a candidate. |
| [Place content models](../../travel-agent/backend/core/models/place_content.py), [persistence](../../travel-agent/backend/core/db/place_content.py) and [delta application](../../travel-agent/backend/core/db/place_content_delta.py) | Versioned lenses, cues and conditional judgments; required/contextual evidence, disagreement edges, review, lifecycle, validity and policy bindings | Smaller-than-dossier content already has an owner. Extend its adapters and query paths before proposing another content store. |
| [World Foundry promotion](../../travel-agent/backend/world_foundry/promotion.py), [persistence](../../travel-agent/backend/world_foundry/persist.py) and [editorial bridge](../../travel-agent/backend/world_foundry/editorial_bridge.py) | Reviewed facts can persist; selected editorial becomes a **proposed** primitive with narrow interpretation authority | Foundry review, runtime acceptance, surface eligibility and public reuse are different steps. A persisted primitive is not automatically a Home candidate. Some Foundry docs still describe older writer limitations; code capability also does not establish deployed activation. |
| [Research graph persistence](../../travel-agent/backend/research_agent/agents/persist.py), [legacy write-back](../../travel-agent/backend/research_agent/db/write_back.py), [Foundry adapter](../../travel-agent/backend/research_agent/pipeline/world_foundry_adapter.py) | Legacy briefs/structured fields/dossiers, optional hold-for-review, and a research-to-Foundry adapter coexist | Trace and migrate the actual callers. `LEGACY_RESEARCH_WRITEBACK_ENABLED` defaults to true in code; the deployed value was not checked. A shadow artifact is not a completed migration. |
| [Quick research](../../travel-agent/backend/research_agent/agents/quick_research.py) and [bounded-result adapter](../../travel-agent/backend/research_agent/pipeline/bounded_result.py) | Uses the same research graph with a quick profile and known target slug/type; now exposes a typed evidence handoff alongside legacy state | Route bounded results to existing identity/observation/primitive owners; fewer graph iterations alone do not provide independent discovery or selective persistence. |
| [Public content source reads](../../travel-agent/backend/core/place_content_sources.py) and [content compilation](../../travel-agent/backend/lived_experience/content_compiler.py) | Exact accepted public primitive versions can be read and checked; current enumeration starts from bounded known entity refs | Reuse these consumer contracts. Discovering useful public material by region, time or theme still needs a concrete read path; the reader is not a public producer. |
| [Primitive vector projection](../../travel-agent/backend/core/vector/place_content_sidebuild.py) | Derived projection machinery already exists for place briefs, angles and primitives | Extend and validate the active retrieval path. Source observations, event changes and every discovered entity do not each need an embedding. |
| [Experience ingestion](../../travel-agent/backend/ingestion/base.py) | Conditional upserts and same-transaction changed-ID invalidation are landed in `96cadfada`; `raw_data`, schedule, status and prose still share the material-change predicate | Preserve the transactional repair. Split observation refresh, practical repair, text regeneration and vector payload updates; verify recovery for any additional downstream consumers. |
| [Event preview reader](../../travel-agent/backend/places/experiences.py) | This producer accepts a dated, membership-checked Trip | Give the content query owner an explicit place plus local-window path; preserve the Trip wrapper and its access checks. |
| [Places budget](../../travel-agent/backend/places/budget.py), [commercial usage ledger](../../travel-agent/backend/core/commercial_access/usage_ledger.py) | Provider call counting exists; separate commercial quota reservations are atomic and billing-subject scoped | Provider COGS enforcement cannot be claimed from the count check. Reuse reservation mechanics where suitable, while keeping internal acquisition spend distinct from customer entitlements. |
| [Discovery](../../travel-agent/backend/places/discovery.py), [taste](../../travel-agent/backend/places/taste.py), [reachability](../../travel-agent/backend/core/reachability.py) | `allow_provider=False` now gates POI fallback, reachability/isochrone and Matrix ranking; explicit map/discovery calls remain provider-capable | C0 has a focused receipt for this nearby call path. Reconfirm any additional root producers before broader rollout and preserve valid cached evidence and honest distance semantics. |

### 11.2 Architecture and ownership decisions

Use one logical evidence contract across acquisition paths, with existing
domain owners retaining persistence authority:

```text
explicit question                 bounded public preparation
         \                         /
          purpose + scope + evidence needs + work budget
                              |
             reuse current material / discover candidates
                              |
           verify only the questions that change the result
                              |
                  supported result + unresolved gaps
                   /                         \
        return current answer         permitted reusable portion
                                               |
                       observations / facts / primitives / events
                                               |
                          accepted current reads + derived indexes
                                               |
                         consumer judgment and final expression

new observation / correction / expiry
  -> owning record revision -> affected claims -> affected projections/indexes
```

Recommended decisions for implementation:

1. **Providers and source discovery supply breadth.** Reuse admitted local
   material first when it serves the question; expand retrieval when the
   available set lacks a decisive field, a suitable activity or a meaningful
   alternative. Three nearby rows do not establish adequate coverage.
2. **Retain selectively.** Public acquisition may yield reusable world
   evidence when source policy permits. The question, private rationale,
   friend constraint and user's identity stay with their authorized owner.
   Public evidence reuse never establishes personal-memory permission.
3. **Keep different kinds of knowledge separate.** Factual claims, attributed
   judgments, interpretation, event occurrence and private relevance require
   distinct provenance and lifecycles even when one response combines them.
4. **Use smaller outputs.** A useful result can be one supported fact,
   conditional judgment, comparison or event observation. A dossier is an
   optional deeper compilation; routine factual extraction does not require
   long prose or a founder reviewing every row.
5. **Choose depth by benefit and consequence.** Exact lookup, candidate search,
   targeted verification and deep interpretation share source tools but have
   different stopping rules. High-impact practical claims need their decisive
   evidence; an engaging explanation need not invent a next action.
6. **Preserve the public/private boundary across reuse.** A friend's private
   photograph or perspective can enrich an authorized composition; it cannot
   become public place research by stripping the author's name.
7. **Keep content independent of medium.** Retain supported meaning and refs;
   consumer composition can express it as a comparison, map, short explanation,
   article or audio. Media rights and generation costs remain separate.
8. **Public preparation has its own operating scope.** Existing research and
   content owners should produce bounded reusable supply. The private
   Source-contribution worker is not a global editorial publisher.

These choices operationalize the [Place canon §6](../../travel-agent/docs/product/Place%20Interpretation%20and%20Content%20Intelligence.md#6-pre-research-live-retrieval-and-runtime-composition)
and [Contribution contract](../systems/contribution-and-consequence.md).
They do not adopt a new canonical noun or schema. A demonstrated inability of
an existing owner to represent a required case should produce a narrow model
proposal with migration and consumer impact attached.

### 11.3 Logical contract and storage disposition

Map these fields into existing request, evidence, owner and execution models
in C0/C1. They are a review checklist, not a proposal to persist the same large
JSON object in every subsystem.

| Contract part | Required information and behavior |
| --- | --- |
| Work request | Job, public spatial/topic scope, local window/timezone when relevant, exact subjects if known, missing evidence, accepted trigger, deadline and operation budget. Public query is separate from private context. |
| Candidate | Canonical ref, external ref or exact source URL; what the offer actually is; source coverage limits; supported character; uncertain fields. Deduplicate by justified identity, not name alone. |
| Observation | Source record, observed/retrieved time, effective time, minimal supporting passage/field, content hash, rights-policy version, retained-payload location if permitted, and retention deadline. A URL alone is not a durable copy of the evidence. |
| Supported claim | Subject and assertion, supporting observations, fact/interpretation/judgment distinction, conditions, confidence or unknown, contrary evidence and validity. Generated prose is not an independent source. |
| Research result | Supported material, omitted/unknown claims, reasons for stopping, exact continuation, acquisition cost and optional reusable subset. A useful qualified answer can finish without canonical publication. |
| Change | Owner revision, affected fields and dependencies, operation identity, effective time and retry identity. A refresh that failed cannot renew validity. |

| Material | Recommended owner/disposition | Initial limit |
| --- | --- | --- |
| Search candidates with no canonical entity | Current investigation; allowed cache only under explicit source policy | No automatic catalog row, dossier, embedding or private save. Durable unresolved storage is an open C1 decision only if required. |
| Accepted identity and factual evidence | Existing external-identity, observation and entity-fact owners | Resolve exact subject and source rights before promotion. Keep an original external ref for reconciliation. |
| Evidence-backed lens or conditional judgment | Versioned place-content primitive and evidence links | Existing model requires an entity anchor. Use a real relevant anchor where it fits; do not invent a Place for an abstract topic. |
| Cross-place explanation | Join supported anchored material for the current answer | Retain constituent knowledge independently. A repeatedly useful multi-anchor relation needs an explicit owner mapping before durable storage; no generic knowledge graph is assumed. |
| Dated event or recurring offering | Existing experiences/occurrence machinery plus source observations | Venue, series, occurrence, performer slot and admission window remain distinguishable. Unsupported timing stays unknown. |
| Brief, dossier or selected semantic text | Existing content owner; derived index only after admission | Update only if supported meaning changed or a consumer needs the new projection. |
| Personal/social reason | Existing private request, Source or relationship owner | Never cache across users or turn an Ask into new durable person evidence. |
| Image, article text, audio or extracted page | Existing media/source mechanism where its license and custody apply | Prefer minimal permitted evidence and source links. Stored interpretation does not imply rights to redistribute its source media. |

### 11.4 Representative portfolio

Use the current [NYC judgment specimens](nyc-recommendation-judgment-specimen-pack-2026-09-07.md)
as inputs, plus the user's cliff-comparison story. These are implementation
cases, not assertions that any event, fare or opening is currently available.
Hold the target name out in discovery variants so exact lookup cannot masquerade
as candidate-finding ability.

| Case | Infrastructure requirement | Required change/failure variant |
| --- | --- | --- |
| An unfamiliar restaurant for a specific evening | Discover outside local corpus; distinguish character, current purpose and operational facts | Missing hours, conflicting identity, no taste history, source terms permitting only transient use |
| A rave or named performance across Saturday/Sunday | Local occurrence date, venue versus performer slot, exact continuation | Reschedule, cancellation, date-only/TBA, after-midnight slot, failed refresh and old response arriving late |
| Museum resource versus scheduled workshop | Explain what participation entails and whether a specific session is required | Recurring resource exists but no workshop is supported; time window changes |
| Sorrento cliffs compared with other landscapes | Find and substantiate a new relationship; retrieve across places and disciplines | Superficial resemblance, missing evidence for causation, user already made the proposed connection |
| A ferry or practical access question | Acquire the exact fact that changes the decision without deep editorial work | Price/admission/route evidence expires while historical explanation remains useful |
| A friend's perspective alongside public material | Reuse the public explanation while preserving the private author's audience | Contribution withdrawn; public knowledge survives while the private juxtaposition disappears |

For each case include fresh/reused material, no useful source, partial answer,
budget exhaustion, duplicate retry and correction. Review the portfolio as a
whole: interestingness, practical utility and social perspective are equal
pressures on the model. No single case defines the architecture or blocks
unrelated implementation work.

### 11.5 Work packages and acceptance criteria

#### C0 — Bind owners and finish the acquisition/serving boundary

**Maps to:** S0A and S3 receiving design. **Owner:** Content for the owner map;
Integration for shared serving behavior. **Size:** small audit/contract slice
plus a bounded backend repair. No provider activation is needed.

Deliverables:

- Fill the §11.3 owner map with exact model/function bindings, unsupported
  fields and consumer destinations for all six cases. Trace request entry,
  research completion, persistence, retrieval and repair; flag dormant or
  shadow-only paths separately from active callers.
- Record the legacy-writeback setting's code default and transition choices.
  Deployed configuration stays unknown until inspected in its own environment.
- Extend the root read boundary through isochrone and Matrix helpers. Allow
  current cached evidence; on a cache miss use an explicitly supported distance
  fallback or unknown. Do not label straight-line proximity as walking time.
- Test ordinary root paths with both spatial flags on, cold caches and
  configured fake providers; assert no provider/model/enqueue call. Separately
  preserve the explicit discovery path.

**Checkpoint:** known owners and actual call chains are recorded; all six
result shapes have an owner or a precise gap; the POI-only boundary claim has
been replaced by a demonstrated nearby discovery/routing call-path receipt.
This is safety and contract progress; substantive content production continues
in C1/C2.

#### C1 — Implement bounded acquisition and normalized evidence results

**Maps to:** S0B and S1. **Owner:** Content/research with existing Places and
web-tool owners. **Size:** medium. Contract/prompt-sensitive where behavior
changes; new provider integration remains an explicit source decision.

Implementation:

1. Add the smallest typed request/result adapters needed by §11.3 inside the
   existing research/tool boundaries. The first bounded-result adapter is
   landed in backend `8cd543260`; keep source acquisition independent from
   whether a canonical entity or dossier already exists.
2. Reuse exact IDs and current evidence before broad search. Let an initial
   candidate pass ask for specific missing evidence; do not fan out to every
   provider or require deep research for each result. Route the normalized
   result through the explicit disposition mapper (`22fd90497`) before any
   existing owner is asked to retain or promote material.
3. Separate Tavily search depth from result count in the existing tool/profile
   configuration. This is landed in backend `84a650829`; keep the current
   profiles on `basic` until a supplier-cost decision. Return source results as discovery material; extract or open
   the source that actually supports a consequential claim. Preserve source
   dates, status, attribution and gaps rather than treating the provider's
   generated answer as independent evidence.
4. Define source capabilities for geography/category/time coverage, exact-ID
   details, claim types, retention/display and refresh. Use a small versioned
   configuration over existing adapters first. The old seed-source registry
   and Places policy are inputs, not verified account permission.
5. Add per-investigation operation/time ceilings and attributable usage. Trace
   nested detail calls, fallback, pagination and retries against one envelope.
   Reconcile actual provider/model usage with the existing ledgers. Decide how
   internal spend reservations reuse existing atomic machinery without making
   a customer entitlement the supplier budget.
6. Prepare the matched supplier comparison from §7 with fake/permitted recorded
   responses. Run live measurement only with the exact account, terms and total
   spend envelope established. Keep supplier replacement behind adapters.

**Acceptance:** an unknown restaurant or event can produce a source-bound
candidate without a catalog insert; known identity avoids redundant search;
incomplete coverage is explicit; private context does not enter public queries;
provider failure or budget exhaustion preserves the useful supported subset.
Before concurrent metered production, demonstrate atomic reservation, replay,
settlement/release and accounting for nested work. A fixture result does not
select a commercial provider or establish NYC recall.

#### C2 — Connect small research outputs to selective canonical write-back

**Maps to:** S1 and S3. **Owner:** Content/research and the existing observation,
fact and place-content owners. Entity owner reviews identity effects.
**Size:** large; split into several reviewable commits.

Implementation:

1. Extend the existing research-to-Foundry adapter and evidence conversion so
   research can finish with a fact, a supported judgment or an interpretation.
   A complete dossier must not be the prerequisite for a usable result.
2. Classify each result as current-answer-only, reusable observation/fact,
   proposed editorial primitive, or optional deep compilation. Keep source
   permission, canonical admission and immediate-answer quality independent.
3. Bind accepted facts to observations and their real entity. Use the existing
   place-content draft/version/acceptance machinery for smaller editorial
   outputs. Preserve disagreement and required/contextual evidence roles.
4. Resolve an external candidate through existing identity owners only when
   persistence is justified. Until then return its exact external/source ref.
   If repeated unresolved reuse needs durability, write a concrete storage
   decision; do not silently put external IDs in canonical-ID fields.
5. Wire the complete editorial transition: proposed primitive, review receipt,
   accepted version, applicable consequence policy and eligible consumer read.
   Foundry's current narrow `on_request`/interpretation defaults must not be
   globally widened merely to fill Home. Supported factual responses can be
   returned while publication remains pending.
6. Build the legacy-writer cutover around matching inputs and consumers. Run
   write-free comparison first; select one canonical writer for each output;
   preserve current approved reads; then retire overlapping legacy writes.
   A hold queue is temporary staging with an owner and disposition, not the
   final production pipeline. Detect direct callers that bypass the flag.
7. Keep promotion transactions short and deterministic: network/model work
   finishes before the transaction; enforce idempotency, evidence refs and
   optimistic version checks; record indexing/repair work durably.

**Acceptance:** a useful conditional judgment is retained and read without a
dossier; factual output can succeed while editorial remains proposed; rejected
or transient material does not publish; retries do not duplicate claims; an
old result cannot replace a newer accepted revision; no source observation or
private context acquires broader rights through normalization.

**First architectural review:** test cross-place comparison with existing real
anchors. If the current model cannot represent a useful reusable relation,
propose the minimum multi-subject extension with consumer and repair examples.
Avoid building a general topic taxonomy or knowledge graph ahead of this need.

#### C3 — Complete event fidelity and field-specific repair

**Maps to:** S2. **Owner:** experience ingestion/query owners, with Content
evidence and Integration repair consumers. **Size:** medium/large; event
schema changes, if needed, are a separate contract-sensitive decision.

Implementation:

- Accept explicit place and local date-window inputs for content queries and
  acquisition. Convert using an established timezone; retain the existing
  membership-checked Trip wrapper. Do not infer a timezone from a city name
  when ambiguity would alter a date or attendance.
- Close the remaining Ticketmaster gaps: local query bounds, explicit TBA/TBD
  flags, rescheduled/postponed/cancelled distinctions, exact performer/admission
  evidence and unknown-start handling. Review ambiguous/nonexistent DST times
  as well as ordinary timezone conversion.
- Decide how date-only/TBA observations survive without fabricating an instant.
  The current normalizer rejects unknown starts. Preserve permitted uncertainty
  in evidence/staging and qualified answers while a schema proposal resolves
  whether an operational event record can represent it. Do not count rejected
  normalization as successful coverage.
- Split **observation refresh**, **operational change**, **semantic content
  change**, and **derived index payload change**. `raw_data` currently shares
  the brief-dirty predicate; timestamps or irrelevant payload metadata should
  not regenerate prose. A changed artist or activity description may justify
  text work; cancellation must immediately affect eligibility even if the
  embedding stays unchanged.
- Preserve the same-transaction dirty handoff landed in `96cadfada`. Verify
  durable delivery/replay for each additional dependency introduced by the
  field-specific split; do not repeat the already-landed dirty-marking repair.
  An unchanged retry after a crash must still recover missed downstream work.
- Bind refresh to exact source IDs and scope. Establish provider revision or
  retrieval ordering, cancellation/expiry semantics, backoff, retry ceiling and
  refresh budget. Search omission is not deletion or cancellation.
- Use source lifecycle, fact projection and content dependencies for repair.
  Old responses cannot revive a superseded event; unsuccessful refresh cannot
  advance freshness. Preserve unrelated descriptions, user tickets and authored
  memories under their independent owners.

**Acceptance:** the event variants in §11.4 survive normalization, query,
selection and repair; a schedule-only update changes practical truth without
rewriting unrelated content; a no-op refresh records freshness only where a
successful observation supports it; a simulated crash between commit and
downstream work is recoverable.

#### C4 — Make retained knowledge retrievable and reusable across questions

**Maps to:** S1 and S3. **Owner:** Content with existing search/vector and
place-content owners. **Size:** medium. Start alongside C2 using admitted
fixtures and real receiving contracts.

Implementation:

1. Support exact entity/version reads, geographic plus local-window queries,
   and semantic question/theme retrieval. Identify which existing query path
   serves each job and which needs a bounded extension.
2. Use Postgres/PostGIS and event indexes for exact identity, dates and location.
   Use the existing primitive side-build for selected semantic content. Fetch
   current canonical content after retrieval; stale vector text cannot restore
   expired or withdrawn evidence.
3. Select brief/primitive text only when useful for retrieval. Keep operational
   fields as structured state or index filters. Verify update/delete/retraction
   propagation and active collection identity before claiming cutover.
4. Assemble comparative knowledge from separately supported subjects. The
   cliff example must add a supported relationship the user did not already
   supply; a shared visual feature alone cannot establish common geology.
5. Keep character, applicability and current feasibility distinct through the
   result contract. Remove mandatory taste resemblance as the sole admission
   route; equally supported unfamiliar and generic options can be valuable.
6. Rank for the request's reward, constraints, alternatives and evidence.
   Separate retrieval relevance from editorial worth and private fit. Review
   variety and duplication across results rather than imposing novelty quotas.

**Acceptance:** the same admitted material supports multiple useful questions
without repeated research; exact reads work without vector search; thematic
retrieval can reach another place; expired operational evidence changes the
practical result while independent interpretation remains available. No new
worldwide index or embedding of every provider row is required.

#### C5 — Establish bounded public preparation and content economics

**Maps to:** S0B, S3 and S4. **Owner:** Content for source scope, preparation and
review; Integration for accepted execution binding. **Size:** medium; starts
as a scoped operator path and expands only after measured yield.

Deliver a preparation specification using existing research/content mechanisms:

- **Scope:** explicit region, topics/activity families, local time horizon and
  known exclusions. NYC is the evaluation portfolio, not an automatically
  adopted launch geography or a claim of city completeness.
- **Supply mix:** reusable durable interpretation, practical conditional
  knowledge, and a rolling current event/offer window. Background preparation
  should not spend equal effort on every entity.
- **Selection:** prefer demonstrated demand, useful coverage gaps, recurring
  questions and distinctive value. A source can be worth knowing how to query
  without mirroring its inventory. Use one small source-capability configuration
  before creating a source-management product.
- **Triggers:** explicit approved batch; source revision/expiry; a reviewed gap
  from permitted aggregate telemetry; or accepted preparation scope. Root GET,
  tab focus, Keep and unanswered prompts are not production triggers.
- **Execution:** choose the existing queue/worker/lease mechanism appropriate
  to the actual producer. Specify deduplication keys, overlap handling, retries,
  model/provider budget, review throughput, freshness deadlines and fallback.
- **Admission and readback:** public facts/primitives/events enter their current
  owners; consumer reads receive accepted eligible versions. A private producer
  record must not stand in for reusable public content.
- **Economics:** report cost per supported answer, per useful reusable unit,
  reuse count, refresh cost, duplicate work and human review time. Separate
  public acquisition, private composition, embeddings and media production.
  Subscription-backed Foundry work also has labor and usage costs; it is not
  an unmetered substitute for application runtime generation.

The two operating modes stay explicit: application research uses its model
registry and metered tools; subscription-backed seeded-world batches use the
[World Foundry operating contract](../../travel-agent/docs/operations/World%20Foundry.md),
including its model, independent review and target-specific promotion rules.
This planning task does not launch such a batch or dispatch agents.

**Acceptance:** a bounded collection is produced, admitted, retrieved and
refreshed through named owners, with cost and current coverage reported.
Supported consumers receive useful ready material. An empty or expired scope
is reported honestly while still-valid adjacent material remains available.
First live supplier measurement can occur as soon as its C1 prerequisites are
met; repeated-use economics then determine whether to expand the collection.

#### C6 — Complete consumer handoff and retire overlapping paths

**Maps to:** S3 and S4. **Owner:** Integration lands shared execution/composition;
Content supplies the accepted evidence contract and reviews substantive output.
Entity and Life own their exact destinations and private continuity effects.
**Size:** medium, with tests beginning during C0 rather than after production.

Deliverables:

- Source→evidence→result→current-owner read→consumer traces for the whole
  portfolio, including unresolved external continuation and no-save cases.
- The live engine receives exact fact subjects, validity, uncertainty and
  dependencies. Current `place.open_now` support stays limited to that claim;
  set-time, future availability and admission need their own supported evidence.
- Home/Places use substantive prepared value with appropriate composition;
  Chat can answer an explicit investigation immediately; entity readers use
  exact owner versions. Source/Intake retains personal material under the
  user's gesture and custody contract; Life indexes and projects permitted
  continuity from that owner. No new screen family is implied.
- Fix incompatible reader eligibility, owner revision and continuation gaps
  with narrowly scoped contract changes. Follow OpenAPI/type generation when
  public models change; internal research adapters need no automatic mobile API.
- Retire duplicated legacy writers/index paths only after their consumers have
  migrated. Record remaining intentional compatibility reads with an owner and
  retirement condition. Keep accepted existing material available during rollout.

**Acceptance:** consumer output reflects source correction, preserves useful
independent material, supplies a concrete next step when appropriate, and does
not reintroduce work on ordinary reads. Passing contracts is distinct from
native UX review and human evaluation of interestingness/usefulness.

### 11.6 Sequence, checkpoints and solo-founder work order

The C numbers describe packages, not a strict waterfall. Recommended execution:

| Wave | Work to advance together | Exit review |
| --- | --- | --- |
| **A — contract and acquisition** | Finish C0 owner bindings and routing boundary; implement C1 bounded request/result adapters; design C2 selective disposition against all six cases; prepare supplier comparison | Can the acquisition result preserve useful evidence without requiring a dossier/catalog insert? Are source dependencies and unsupported mappings explicit? |
| **B — persistence and temporal truth** | C2 canonical write-back and legacy transition; C3 event/field repair; C4 retrieval fixtures; first permitted supplier measurement | Can a small useful unit survive, be retrieved and be corrected? Are facts, interpretation and events retaining distinct meaning and lifecycles? |
| **C — reusable supply** | C4 active retrieval; C5 scoped public preparation; C6 real owner/readback handoff | Does reuse reduce cost while preserving interestingness and practical correctness? Can supported consumers receive ready value? |
| **D — expansion and retirement** | Repeated-use/economics evaluation; remove migrated duplicate paths; expand only valuable, supported source families | Does another source, region or index pay for its operating burden? What should stay deliberately outside current coverage? |

For a solo founder, keep one main landing sequence. Independently bounded
provider research, event normalization or fixture work can overlap when
delegation is requested; shared schemas, public contracts, activation and root
composition should be reviewed and landed serially by their owner. Parallel
work must have explicit file ownership and a common commit baseline.

Review at the end of each wave and whenever a package introduces a new durable
owner, external provider, shared contract, model behavior or source retention
decision. The review asks whether the design still supports all six cases,
what actual consumers use, what duplicates an existing owner, and what work
can be removed. Do not wait for one behavioral experiment to define the system.

**Next execution round:** C1a accounting closure, C2a write-free completion,
C2b selective owner persistence, and C4a exact readback, detailed in §12.
The earlier C0 routing repair and initial bounded-result/disposition adapters
are landed; they are regression boundaries, not tasks to restart. Keep the
whole six-case portfolio in view. Supplier rights work proceeds alongside
implementation; it blocks affected live use and retention, not independent
adapter, owner and query work using permitted fixtures.

Relative sizes above express uncertainty and review burden, not calendar
estimates. Estimate elapsed time after Wave A identifies the writer cutover
and the scope of any event-model change. Track completion with commit IDs,
test receipts, remaining gaps and actual producer/readback bindings in this
document.

**Execution status, September 7:** C0's nearby discovery/routing boundary,
C1's bounded-result adapter and explicit search-depth policy, and C2's pure
disposition mapper are landed. `96cadfada` subsequently tightened citation
association, cumulative subquery bounds, research response metering and event
invalidation. These repairs do not connect selective canonical publication:
the production graph still reaches legacy writers before quick research
normalizes its result, and the disposition mapper has no production caller.
Citation association does not establish claim entailment; subquery counting
does not establish a nested-call or monetary ceiling. §12 records two further
metering gaps found by inspection.

Adjacent Integration has advanced workflow authorization, lease/publication
fencing and deadline forwarding. Its active source-result/readback work stays
with that lane. Real PostgreSQL interleaving evidence, public content admission,
event uncertainty/field repair, active retrieval, public preparation and actual
consumer activation must each have their own receipt. The preceding content
review reported focused passing suites, but the full offline backend run was
not clean; this planning pass does not claim to repair or rerun that baseline.
No provider was activated and no root read became a production research trigger.

### 11.7 Validation, migration and decision record

Use the cheapest meaningful validation for each change:

| Change | Required evidence |
| --- | --- |
| Acquisition adapters and limits | Offline recorded/fake provider cases, wrong/ambiguous identity, incomplete evidence, timeout, capped retries and explicit call counts |
| Source/claim/primitive persistence | Existing observation/place-content/Foundry tests plus real local Postgres checks for transactional idempotency, version conflicts and crash recovery where SQL behavior matters |
| Prompt/research behavior | Side-by-side supported answers for the portfolio; inspect substantive additions, misleading certainty, needless research and unwanted homework; deterministic tests alone cannot establish quality |
| Events | Local midnight/DST/TBA, reschedule, cancellation, recurrence, source omission and late-response tests across normalization and query/repair consumers |
| Retrieval | Exact-owner read tests, primitive side-build/parity and stale-vector exclusion; actual query retrieval rather than only embedding generation |
| Public budget/preparation | Concurrency/reservation/replay, partial failure, refresh ceilings and readback; separate approved live sample for useful yield and actual cost |
| Consumer/API changes | Focused Home/Places/entity/Chat contracts as affected, workspace schema sync and generated mobile types when needed; native QA separately |

Existing starting suites include `tests/db/test_source_observations.py`,
`tests/db/test_place_content.py`, `tests/research_agent/test_world_foundry_adapter.py`,
`tests/research_agent/test_persist_results.py`,
`tests/world_foundry/test_editorial_bridge.py`,
`tests/core/test_place_content_sources.py`,
`tests/core/vector/test_place_content_sidebuild.py`, the ingestion suites and
the Places discovery/taste suites. Select tests by touched behavior rather
than repeatedly running the entire suite. The earlier embedding-startup stall
is not evidence of failure or success for these new changes.

Migration discipline:

- Inventory readers and writers before changing an owner. Compare legacy and
  new results without duplicating canonical writes. Keep legacy approved reads
  until the replacement can read the same supported material.
- Change the legacy-writeback default/activation only as part of a documented
  caller migration. Turning it off without a usable promotion path would make
  a review backlog, not working infrastructure.
- Schedule/index changes require scoped backfill and no-op receipts. Preserve
  user-created records and retained sources independently of provider cache
  expiry. No destructive catalog cleanup is implied by this plan.
- Roll back optional acquisition or publication through the owning execution
  controls; continue valid reads. Do not recover by allowing stale evidence,
  reviving superseded versions or re-enabling research on GET.

| Decision | Recommended direction | Evidence needed before affected implementation/activation |
| --- | --- | --- |
| Storage for unresolved candidates | Request-scoped first; exact external continuation | A repeated-use case that needs durable unresolved evidence and cannot map safely to existing owners |
| Reusable cross-place relationships | Compose supported anchored units first | A concrete reusable relation, its subjects, query consumer and repair requirements before a model extension |
| Editorial acceptance throughput | Reuse existing review/policy transitions; automate repeatable checks and reserve human review for judgment-heavy material | Source-family/output policy that explains which review establishes which claim and surface use; no universal founder queue |
| Unknown-time events and slots | Preserve uncertainty; reuse experience/occurrence owners | Exact date-only/TBA/series/slot cases, schema impact and matching readers before migration |
| Provider choice and retention | Compare by useful yield, current evidence and permitted reuse | Reviewed account/operation policy, coverage results and bounded costs; adapter existence alone is insufficient |
| Public production owner | Existing research/content production into public observation/fact/primitive/event owners | Exact trigger, queue/lease, budget, acceptance and current-read binding; private Source worker cannot fill the gap by renaming it |
| Spend enforcement | Reuse atomic mechanisms where suitable, preserve distinct provider COGS and entitlement scopes | Concurrency and nested-call accounting design; existing call counts do not certify a hard cap |

Documentation follow-through belongs to the corresponding implementation:
update Content as Infrastructure for the current everyday scope; Content
Research Pipeline for the new completion/write-back paths; World Foundry and
its FEATURE for the actual promotion boundaries; Events Strategy for timing
and refresh; and affected research/Places/ingestion FEATURE notes. The Place
canon §6 remains the product direction. This plan updates no deployment,
provider agreement, runtime prompt or personal-retention contract.

Planning-pass verification: governance metadata, scoped relative links, code
fences and whitespace checked for this roadmap and the Integration receiving
note. No runtime tests were rerun for these documentation-only changes.

## 12. Next execution batch: connected content lifecycle

### 12.1 Outcome and scope

The next milestone is a working connection from bounded research to selectively
retained knowledge, current consumer reads and correction. A small useful
answer must be able to finish immediately. Its permitted reusable portion can
subsequently help another question or person without repeating the research.
The six cases in §11.4 exercise the system together; none is the sole launch
loop or a prerequisite for unrelated architecture work.

Preserve three independent decisions:

- **What would help now:** the request's purpose, appropriate depth, supported
  answer and remaining uncertainty.
- **What work may run:** accepted trigger, source operations, execution budget,
  deadline and cancellation authority.
- **What may survive or be shown elsewhere:** source rights, exact subject,
  evidence, review, retention and consumer eligibility.

An LLM can propose a claim or editorial treatment. It cannot grant a source
license, approve canonical identity, widen an audience or mark its own draft
accepted. A public evidence write never means the user saved, followed, planned
or attended something. The
[contribution contract](../systems/contribution-and-consequence.md) continues
to govern those personal consequences.

This batch uses the existing observation, entity-fact, experience and
place-content owners. No universal content table, worldwide venue/event index,
new queue framework, new screen family or redesign of Chat/Life is authorized.
Source/account policy is a prerequisite for affected live operations, not a
reason to postpone provider-independent implementation.

### 12.2 Code findings that determine the work order

| Finding at the inspected baseline | Consequence |
| --- | --- |
| `quick_research` awaits the full graph before creating its bounded result. Green graph output flows through dossier generation/validation and persistence; yellow/red paths also have durable review/metadata effects. | Add an explicit acquisition/completion path whose disposition is chosen before any domain writer. Post-hoc normalization cannot provide a write boundary. |
| `map_research_disposition` has no production caller. `compile_graph` is called directly by the queue, angle task and research script as well as quick research. | Migrate actual callers with explicit modes and compatibility behavior. Testing only the mapper or quick wrapper misses bypasses. |
| `research_experience` can persist a metadata-only fallback with research status `complete`; its helper is a separate writer. | Separate useful fallback from researched/admitted material, and include this caller in the cutover. A disabled legacy graph writer is insufficient. |
| The new usage accumulator is a `ContextVar`, while the research DB executor does not propagate context. Some terminal writers calculate measured tokens inside that executor. | Capture an immutable usage snapshot before thread dispatch, or deliberately propagate context with isolation tests. Existing same-thread mocks do not cover this boundary. |
| Response accounting uses `uncached_input_tokens or input_tokens`. Zero uncached tokens is valid for fully cached input. | Reconcile with canonical provider-usage semantics; avoid adding cached input twice. Keep token classes separate for cost calculation. |
| Foundry persistence shares one transaction for observations, identities, claims and proposed primitives, then rebuilds the place projection after commit. | Reuse the transactional writer. Verify durable recovery across the fact-commit → projection-rebuild gap; a projection outbox created only during rebuild cannot by itself cover that earlier gap. |
| Accepted public primitive readers already enforce exact version and current eligibility. Enumeration begins from a bounded set of known entity refs. | Connect exact readback first, then add bounded geographic/window/theme candidate lookup. A working side-build is not evidence of working semantic retrieval. |
| Event dirty marking is now in the upsert transaction. An unknown-start cancellation/postponement can update an existing row using its stored start; new unknown-start records are still skipped. | Preserve the repair and distinguish carried historical time from a newly confirmed schedule. Temporal representation and field-specific refresh remain separate work. |

Primary implementation files are linked in §11.1. Additional seams are
[research graph](../../travel-agent/backend/research_agent/agents/deep_research.py),
[experience research](../../travel-agent/backend/research_agent/agents/experience_research.py),
[research DB executor](../../travel-agent/backend/research_agent/db/connection.py),
[research LLM accounting](../../travel-agent/backend/research_agent/pipeline/llm.py),
[disposition mapper](../../travel-agent/backend/research_agent/pipeline/disposition.py)
and [bounded schemas](../../travel-agent/backend/research_agent/pipeline/schemas.py).
These are code-inspection findings, not newly executed failure reproductions.
Recheck the active branch and caller inventory before editing: Integration is
changing nearby Source/workflow code concurrently.

### 12.3 Commit-sized execution sequence

The suffixes refine the existing C packages. Each row is a landing unit; split
a unit further when an owner/schema migration needs independent review. Do
not bundle a new source, shared schema and consumer activation into one commit.

| Unit | Depends on | Deliverable | Required completion evidence |
| --- | --- | --- | --- |
| **C1a — accounting closure** | Current baseline | Reliable run-usage snapshot across terminal/thread boundaries; correct cached-token accounting | Real executor-boundary test, concurrent-run isolation, success/review/discard/fallback paths and fully/partially cached responses |
| **C2a — write-free completion** | Existing bounded-result/disposition contracts | Small-result completion before persistence; explicit caller mode and legacy compatibility | Green/yellow/red, failure and exhausted-budget cases cannot reach domain writers in this mode; useful supported answers survive |
| **C2b — owner admission and publication** | C2a; source/subject policy for retained fixtures | Source-bound facts and proposed primitives using existing owners; explicit review → accepted current read | Real Postgres idempotency, rollback/version conflict and interrupted projection recovery; transient/private material cannot broaden rights |
| **C4a — exact reuse and handoff** | C2b; existing reader contracts | Current retained units can answer another request; machine-readable owner/version/validity result | Fresh → retained → reused → corrected traces; exact lookup needs no vector search or provider call |
| **C3a — local events and field repair** | Existing ingestion; shared result contract from C2a | Place/local-window queries, uncertainty handling and targeted operational/semantic repair | Trip wrapper parity, DST/midnight/TBA/cancel/late-response cases, schedule-only update without unnecessary prose regeneration |
| **C4b — geographic and thematic retrieval** | C4a; C3a for temporal candidates | Bounded active retrieval from admitted material and purpose-led candidate expansion | Actual query/readback and stale-index exclusion; unfamiliar no-history option and cross-place comparison supported |
| **C1b — enforceable acquisition envelope** | C1a; adapter inventory from C2a | Nested operation/deadline accounting and shared atomic spend reservations with replay/settlement | Concurrency, fallback/retry/pagination, unknown-charge timeout, crash and exhaustion cases; explicit source policy |
| **C5a — bounded public preparation** | C2b/C4a/C1b; C3a/C4b for affected coverage | Operator-scoped collection prepared through existing production and read owners | Admitted current collection, attributable cost, refresh/expiry and useful-empty-scope behavior; no work on GET |
| **C6a — consumer activation and retirement** | C4a contract handoff; relevant supply units | Integration-owned receipt in actual consumers and removal of migrated duplicate writers | Committed source/consumer SHAs, current-read and correction tests; separate native/content-quality review |

**First implementation round:** C1a → C2a → C2b → C4a. Its deliverable is
connected small-unit publication and readback, including correction, with
provider-free fixtures across all six cases. C2b can expose and test fact reads
while the editorial acceptance transition is being completed; neither requires
turning every answer into a publication. Event query work and budget design
can be prepared independently; their shared changes land after contract review.

#### C1a: close measured-usage correctness before expanding production

Capture run-local usage once at the terminal boundary and pass ordinary values
to persistence, or use a reviewed context-propagating executor. The preferred
minimal change is explicit snapshots where only accounting is needed; do not
change a shared executor's authority behavior accidentally. Verify the actual
executor path rather than replacing it with a same-thread passthrough.

Use canonical uncached/cache-read/cache-write/output semantics from the core
provider adapters. Test a genuinely zero uncached-input response, absent usage,
multiple model calls, exceptions and concurrent investigations. Keep measured
usage separate from estimated/pre-authorized cost. This closes accounting
correctness; it does not yet establish C1b's hard monetary ceiling.

#### C2a: make completion independent of a dossier and a writer

1. Inventory `compile_graph`, `quick_research`, `research_experience`, direct
   queue/angle jobs, research CLI and their persistence helpers. Record which
   callers migrate now and which intentionally retain compatibility behavior.
2. Select an explicit acquisition-only completion mode before execution.
   Reuse gathering/reflection where useful, but let small factual/interpretive
   results stop without dossier writing or the dossier-specific quality gate.
3. Normalize supported results and resolve disposition before observation,
   fact, primitive, brief, dossier or review-queue persistence. Apply this to
   failure/partial branches too. Execution telemetry may persist under its
   policy; it must not smuggle retained source bodies/private prompts into a
   supposedly transient run through metadata or graph checkpoints.
4. Bind proposed claims to specific source records and supporting passages or
   structured fields. Domain/index association is only source matching: reject
   ambiguous same-domain matches and a source that does not support the claim.
   Keep title, actual retrieval/publication time, contrary evidence and missing
   fields. A provider summary can guide research, not authenticate itself.
5. Call the disposition mapper using caller-owned purpose and policy inputs.
   Return partial value and exact external continuation without canonical
   insertion when identity, support or retention is insufficient.

Acceptance tests spy on **every reachable writer**, including fallback and
review paths. An exhausted budget must stop additional acquisition and finish
with the supported subset, rather than replan indefinitely. An explicit deep
compilation can retain its dedicated workflow; it is not the default cost of a
restaurant fact. Prompt/graph changes require side-by-side portfolio review in
addition to deterministic tests.

#### C2b: admit the reusable portion through existing owners

Use the research-to-Foundry adapter for typed observations, claims, judgments
and editorial proposals. Its required field mappings must come from supported
material; do not mine a polished answer into supposedly verified facts. Reuse
the entity owner only when persistence warrants canonical resolution. The
shared `EntityRef` already includes `experience`; inspect each downstream
owner's actual supported fields rather than inventing an event identity type.

Split implementation into two reviewable commits if needed:

- **Evidence/fact admission:** minimal permitted observation, exact subject,
  claim validity and independent source policy; existing atomic persistence,
  deterministic retry identity and a recoverable projection obligation.
- **Editorial transition:** proposed primitive, durable review receipt,
  accepted version and explicit action/surface policy. Retain the existing
  Foundry bridge's narrow `on_request` interpretation default. Home eligibility
  needs its own policy, not a global widening of every primitive.

Keep model/network work outside transactions. The current Foundry writer
already passes one connection to observation/fact/primitive gateways; preserve
that property. Close the after-commit projection gap with existing durable
repair machinery where it fits. Test both same-run retry and equivalent
re-acquisition: a new run ID must not automatically mean a new useful version.
Define change identity from subject, claim/content and supporting evidence,
while retaining each legitimate new observation's time and provenance.

Routine factual checks should be automated under a specific source/field
policy; judgment-heavy publication needs an appropriate review policy. A
universal founder approval queue is not the operating model. Until eligibility
is granted, an immediate supported answer can still succeed and a proposed
primitive must remain absent from public feeds.

#### C4a: retrieve a current unit and use it again

Bind the retained result to actual fact and primitive reader functions, not a
payload copied from the writer. Return exact subject, observation/claim or
primitive-version refs, support, validity, missing fields and permitted uses.
This is a content handoff, not a new personal-memory artifact.

Exercise the whole chain: initial answer → permitted retention → second
question/current read → changed observation → revised answer. The second
question should be able to use a smaller fact without loading a dossier.
Same-user and cross-user tests must separate public reuse from private
question/rationale. Withdrawal of a friend's contribution removes the private
juxtaposition while independent public knowledge remains available.

Use exact version checks already present in `place_content_sources.py`.
Return explicit stale/unavailable for an exact-version request that is no
longer eligible; do not silently substitute latest content. A caller asking
for current material may receive the current accepted revision through the
owner's current-read path. Both paths must recheck source lifecycle and policy.

#### C3a: make events useful outside a dated Trip

Expose a lower-level content query taking explicit place/geometry, local start
and end dates, timezone and relevant filters. Declare inclusive local date
semantics and convert once to half-open instants for query execution; apply
overlap/occurrence rules after retrieval. Keep the membership-checked Trip
producer as an adapter so private scope is never treated as public city scope.

Before a schema change, settle venue versus recurring offering, actual
occurrence and performer/admission slot using existing experience owners.
Preserve date-only, TBA/TBD and postponed observations without inventing a
timestamp. If an operational row cannot represent them, retain only permitted
uncertain evidence and report the limitation; skipping normalization is not
successful ingestion. A cancellation carrying an old stored start must not
suggest that this time was reconfirmed.

Classify changes separately: observation/freshness, practical eligibility,
semantic content and derived payload. A cancelled occurrence disappears from
current feasible suggestions immediately through owner checks; a new raw fetch
timestamp does not force a new brief or embedding. Preserve same-transaction
dirty marking and add durable obligations only for genuinely separate repair
consumers. Test provider revision/retrieval ordering, replay and successful
freshness updates so a late response cannot revive cancellation.

#### C4b: find retained material by place, time and question

Use structured Postgres/PostGIS/event predicates for geography and time, and
the existing derived content index for bounded semantic candidates. Confirm
the actual active collection and reader; then fetch authoritative current
records before composition. Expired evidence cannot return through stale
vector text. Index selected admitted semantic content, not every provider
result or every operational refresh.

Replace corpus-count/taste-match sufficiency only on the affected discovery
path: evaluate missing evidence, current purpose and useful alternatives.
Preserve explicit provider permission and budgets. Ordinary Home/Places reads
consume available material and declare gaps; they cannot acquire more by
silently invoking this expansion policy.

For the cliff comparison, compose from independently supported anchors first.
Only propose a multi-subject model extension if a real consumer cannot reuse
or repair the relation correctly with current owners. Assess whether the
answer adds substance the user did not supply, not simply whether search found
two similar embeddings.

#### C1b: make bounded work genuinely bounded

Inventory every metered search, extraction/detail call, provider fallback,
page, retry and model call. The existing `max_operations` subquery ceiling is
useful but is not that inventory's enforceable budget. Apply the accepted
deadline at dispatch and completion, and stop fan-out when no reservation
remains. Account for a timed-out operation that may already have been charged.

Use an acquisition-run envelope plus shared provider/time-window reservations.
Reuse atomic reservation/replay/settlement mechanics where appropriate; the
commercial ledger's customer billing subject is not automatically a provider
COGS subject. Reserve before dispatch, settle known usage, retain/reconcile
uncertain charges and release only known unused reservations. Unknown cost
must be explicit, not zero. Estimate conservatively under a configured source
policy, with a separate emergency stop and bounded retries.

Tests need concurrent contenders for the last allowance, nested fallback,
worker crash, duplicate settlement, cancellation and partial success. This
gates automated/live metered production. Offline adapter/readback work does
not wait for procurement, and a measured small supplier sample still needs an
explicit total spend/operation envelope and authorized account.

#### C5a: create a bounded collection of ready value

Choose an explicit public scope, such as NYC with one rolling weekend window
plus a small set of durable explanations useful beyond that weekend. Set a
target collection size, refresh ceilings, supported source families, review
capacity and total spend before a run. Selection should cover practical
possibilities, substantive understanding and a few reusable relationships.
Use the six cases for coverage, not a rigid six-section Home composition.

Bind an operator-authorized preparation request to the existing research
production owner and C2/C4 write/read paths. Record run identity, lease,
deadline, deduplication, budget and readback. The private Source-contribution
worker is not the default owner of public world preparation. An offline fixture
or a queue definition alone does not demonstrate a running public producer.

Start with explicit runs. Add recurring refresh only after freshness classes,
cost, repair and stop behavior have receipts. Report admitted useful units per
operation/cost, rejection reasons, repeat-query reuse, coverage gaps and stale
exclusions. Do not use pages scraped or words generated as success metrics.
Visual composition and new rendering formats remain outside this batch.

#### C6a: integrate without creating another product lane

Hand the Integration roadmap's **SP-4a public-content receive** package a
committed source SHA, exact typed result, owner reader, eligibility/validity
rules, correction behavior and test receipts. Supply public-only orientation,
small interpretation, event and mixed-public/private examples without assuming
a rich personal history. Integration owns workflow/result delivery and shared
composition; Home owns receiving composition; Life owns permitted continuity.
Content supplies the material and its lifecycle, not parallel implementations
of those responsibilities.

For the live engine, deliver structured subjects, conditions, operational
deadlines and dependencies. A useful interpretation can coexist with unknown
current feasibility. A schedule update affects practical judgment without
rewriting unrelated history. Ranking, action authority, live watch subscriptions
and actual booking remain with their established owners; content publication
does not create any of them.

Migrate one canonical writer per output kind after write-free comparison.
Include `research_experience` and direct graph callers; preserve current
approved legacy reads until replacements serve their consumers. Turning off
the legacy flag into a growing hold queue is not a completed cutover. Record
remaining intentional compatibility paths with an owner and removal condition;
do not delete old catalogs or user records as cleanup.

### 12.4 Review points and evidence

| Review point | When | Question that can change the next work |
| --- | --- | --- |
| **Completion boundary** | After C1a/C2a | Can small useful answers finish without domain writes or dossier work? Are evidence support and actual run accounting preserved? If not, repair this boundary before caller migration. |
| **Owner and reuse** | After C2b/C4a | Can admitted facts/interpretation be reread, reused and corrected through existing owners? Does a new schema solve a demonstrated problem, or duplicate an existing owner? |
| **Temporal and retrieval** | After C3a/C4b | Do ordinary local requests, scheduled events and cross-place questions all work with independent clocks and no taste-history prerequisite? Does semantic retrieval add useful reach beyond structured/exact reads? |
| **Supply and economics** | Before/after the bounded C5a run | Do source rights, useful yield, refresh burden, review and costs support expansion? Which material should remain transient or explicitly requested? |
| **Consumer integration** | At C4a handoff and C6a activation | Can real consumers use exact current material and respond to correction? Which remaining failures belong to supply, composition, rendering or native UX? |

At each review, update this roadmap with committed SHAs, tests actually run,
remaining gaps and the next bounded work. Recheck concurrent branches/status
before shared edits. Land explicit filenames; do not sweep other lanes' work.
If delegation is later requested, event fixtures/query work and provider
budget tests can run independently with named file ownership. Shared contracts
and activation retain a single landing owner.

Validation proceeds from pure adapter tests to owner integration tests to
actual receiving paths. Use real local Postgres for transaction/retry/conflict
claims; mocked sessions cannot establish lock ordering or crash recovery.
Keep optional provider/model dependencies out of ordinary-root tests, including
cold-cache and empty-result variants. If an API contract changes, run workspace
schema sync, inspect both OpenAPI snapshots and generated mobile types, then
check affected mobile consumers. Pure internal adapters do not need a new API.

Separately review consumer output for useful new substance, modest reading
burden, concrete possibilities, practical uncertainty and absence of unwanted
input homework. Offline fixtures establish mechanics, not live coverage,
human-perceived quality or measured provider economics. Native app QA is a
separate receipt when receiving UI changes.

### 12.5 Stop conditions and completion definition

Pause the affected path for a concrete decision when it needs a new durable
owner, changed private/public authority, a commercial source policy, an
unknown-time schema or a new review/activation policy. Record the narrow choice
and continue independent work. Do not declare the whole architecture blocked
by an unavailable provider or one ambiguous specimen.

**The first round is complete when** C1a/C2a/C2b/C4a have landed and retained
small outputs are demonstrably used and repaired through current readers.
It does not claim city-wide supply, deployed public preparation or finished
Home UX. **The connected content milestone is complete when** the relevant
event/retrieval paths, enforceable production budget, bounded public producer
and actual consumer handoff also have evidence, with overlapping writers
migrated or explicitly documented as compatibility paths.

Rollback disables new acquisition/publication through the owning controls
while preserving valid reads. It never re-enables implicit research on GET,
revives a withdrawn version or converts an unknown fact into a promise.
No calendar estimate is assigned before the first owner/transaction review;
the order and exit conditions above are the execution commitment.

### 12.6 September 7 execution receipts

The provider-independent portion of the batch is now implemented on the active
backend branch, in isolated commits:

| Unit | Receipt | What is now true |
| --- | --- | --- |
| C1a | `10ecea2c4` | Usage is snapshotted before executor-bound persistence, and zero uncached input is counted as zero rather than falling back to a legacy total. |
| C2a | `516c89596`, `dd1890eb6` | Answer-only completion is a graph terminal and the experience caller can return its bounded result without a brief/dossier write. Existing legacy callers remain explicitly compatible. |
| C4a | `b0d5a80ca`, `0cd27bdee` | Exact source handoff and bounded multi-anchor composition read current owner records with version, lifecycle, privacy, evidence and consequence checks. |
| C3a | `5a6bc740a`, `5a9daed12`, `af9dc4ae3` | Local event windows, explicit event search scope, provider metadata preservation and the lookup consumer's `results`/`events` compatibility boundary are covered. |
| C1b (first slice) | `8926cb497`, plus `2a102c599` | Caller deadlines are enforced around the full quick graph and before subquery dispatch; remaining chain time is capped and deadline exhaustion returns an explicit bounded stop. |
| C4b (structured first slice) | `4efe7aa1a` | A bounded place-scope reader discovers only admitted primitives attached to the place's canonical child entities; it does not invoke research, providers or a global index. |

Focused receipts run during this pass: `12` accounting, `48` content/graph,
`25` Places/event, `6` exact handoff, `10` multi-anchor composition, `13`
experience, `16` event-tool, `20` lookup, `5` quick-research, and `11`
place-scope tests. Deadline dispatch is covered inside the graph/quick suites;
the combined content-lane regression command ran `153` tests. These are
scoped receipts, not a branch-wide green claim.

The existing World Foundry promotion/persistence owner remains the C2b
boundary; this pass did not silently mark it complete. Real local Postgres
tests are still required for idempotency, rollback/version conflict and
interrupted projection recovery. C1b still lacks provider-COGS reservations,
unknown-charge settlement and crash/concurrency receipts. C5a public
preparation and C6a Integration consumer activation remain unlanded. No
semantic vector expansion, provider activation, Home/Life/Chat redesign or
GET-triggered research was introduced.

Roadmap-document verification after this receipt update: governance metadata,
relative links, same-document anchors, code-fence pairing and whitespace
remain to be rerun at commit time; the earlier planning-pass counts are not
reused as current verification claims.
