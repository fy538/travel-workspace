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

This is a **research-backed implementation roadmap**, with the bounded code receipts in §10. The detailed Content-lane execution plan is in [§11](#11-content-infrastructure-execution-plan). It does not establish provider procurement, legal clearance, deployment approval or complete supply. No paid API batch, account inspection, production DB query, subscription, provider contact, worker registration or app change was performed in this lane. Public documentation describes capabilities, not measured NYC coverage.

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
  World Foundry and web-search policy tests is **268 passed, 9 skipped, 16
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

Planning recheck: workspace `c0b3e12`, backend `5421c66b7`, mobile `17eea1980`.
The Place canon has uncommitted strategy amendments; they are working context.
This pass inspected code and documents, not production configuration or data.
The earlier 210-test receipt is historical verification of the implemented
repairs, not a test of the plan below.

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
| [Experience ingestion](../../travel-agent/backend/ingestion/base.py) | Conditional upserts and changed-ID invalidation are landed; `raw_data`, schedule, status and prose still share the material-change predicate | Split observation refresh, practical repair, text regeneration and vector payload updates. Dirty marking currently occurs in a later transaction and catches failures; retry-safe downstream repair remains work. |
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
- Replace the post-commit best-effort dirty handoff with an existing durable
  transaction/outbox mechanism or a reviewed narrow extension. An unchanged
  retry after a crash must still recover missed downstream work.
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

**Immediate first execution round:** C0's concrete owner-binding gaps and
routing-boundary repair, then C1's bounded evidence result with C2's explicit
disposition mapping. Exercise restaurant, event, recurring activity and
cross-place explanation shapes from the start. Deliver code and readback
evidence, not only another generalized architecture document. Supplier rights
work proceeds alongside this; it blocks the affected live provider path, not
the independent adapter, persistence and retrieval work.

Relative sizes above express uncertainty and review burden, not calendar
estimates. Estimate elapsed time after Wave A identifies the writer cutover
and the scope of any event-model change. Track completion with commit IDs,
test receipts, remaining gaps and actual producer/readback bindings in this
document.

**Execution status, September 7:** the provider-independent part of Wave A is
now landed: C0's nearby discovery/routing read boundary, C1's typed bounded
result, explicit search-depth policy and traceable-source handling, and C2's
write-free disposition mapper. The next work is intentionally gated rather
than implied by these commits: canonical observation/primitive promotion,
unknown-time event representation and field-specific repair, active retrieval
readback, public preparation, and consumer activation still need their owner,
schema/rights, or supplier decisions. No provider was activated and no root
read was changed into a production research trigger.

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
