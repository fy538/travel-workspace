---
doc_type: working
status: active
owner: engineering / search / architecture
created: 2026-08-31
last_verified: 2026-08-31
expires: 2026-09-30
why_new: Workstream B (human refinding) requires a code-only audit of current retrieval, truth, and authority capability against the fifty-query Life re-finding benchmark before any native prototype or index design is authorized.
depends_on:
  - docs/working/life-refinding-query-benchmark-2026-08-29.md
  - docs/working/life-next-behavior-prototype-handoff-2026-08-31.md
  - docs/working/life-object-and-lens-fixture-pack-2026-08-29.md
---

# Life Human Refinding — Code Audit (Q01–Q50)

Audit only. Nothing here authorizes implementation, noun migration, or
refactoring. Six-tier status vocabulary applies throughout; no capability
below is described as done.

## 1. Executive summary

**Coverage headline: 0/50 COVERED, 28/50 PARTIAL, 22/50 ABSENT** against the
fifty-query benchmark. No query passes today with target rank, truth, and
authority all at 2 — and two failures are global: the served Universal Search
envelope discards truth/authority columns its own SQL already selects, and a
durable per-user `query_hash` (32-bit FNV, reversible for short queries)
violates the benchmark §8 retention constraint on every query before scoring
begins.

The shape of the gap is consistent and, on balance, encouraging: **the truth
substrate is much stronger than the retrieval layer.** Planned-vs-occurred,
per-person occurrence with a first-class "no evidence" state, plan-revision
lineage with authorship, source custody with revocation columns, claim-local
source roles, directional visibility grants, and a rigorous stale-hours guard
all exist as CODE-EVIDENCED models — but almost none of them is reachable
from any search or query path, and the one personal search surface projects
them away. The dominant missing artifact is a **refinding read model**, not a
new truth store.

Top feasibility risks that should change the design:

1. **The search layer actively hides negative truth.** Cancelled/skipped
   itinerary items are filtered out of search (`core/db/search.py:1398-1399`)
   — the benchmark's "unused ticket" queries (Q01/Q08/Q20) hard-fail by
   *omission*, the exact oracle the benchmark names. Target-first refinding
   inverts this: unused/missed items must be included and truth-labeled.
2. **"I never went there" has no write path.** Rejecting an occurrence
   proposal strands canonical state at `planned` forever
   (`core/db/occurrence_reconciliation.py:604-628`); the §9
   correction-rerun-verify loop cannot close until it exists.
3. **No person entity, no person shields.** Non-user persons are
   unrepresentable; no block/mute table exists; person-scoped exclusion
   (Q42/Q50) and person-cue retrieval ("after meeting Teodora") are
   architecturally out of reach without a decision that touches the "no new
   owners" doctrine.
4. **Two parallel truth lanes.** The legacy itinerary lane and the
   clean-break experience graph both model plan/occurrence with different
   vocabularies and asymmetric capabilities (revision lineage exists only in
   the legacy lane). Building refinding read models before ruling which lane
   is the substrate builds them twice.
5. **Corrections do not reach derived state broadly.** Only *memory*
   corrections have a transactional propagation chain; occurrence/affinity/
   outcome corrections have none, no correction touches Qdrant vectors, and
   there is no reverse index from a withdrawn claim to its downstream uses —
   so benchmark §10's "every correction updates affected results" is
   currently unachievable for most correction kinds.
6. **Compositions are ephemeral.** Q29–Q33 presuppose persisted generated
   compositions with manifests; nothing persists them. The proven manifest
   pattern (`ContentDecisionReceipt`, complete selected/rejected partition)
   lives in the place-content lane and could be promoted.
7. **Photos have no retrieval identity** despite stored capture time, GPS,
   and place binding — three benchmark queries and much of "Around this"
   orientation depend on one.

Positive findings worth building on: the Places search projection already
carries a real per-viewer truth envelope (`PlacesRelationshipTruth` +
explicit `UNKNOWN`); `CanonicalArtifactProjectionV1` + the intake semantic
contract already define most of the §2 result-contract vocabulary; the chat
lane's `recall` demonstrates correct read-time authority (vector IDs only,
Postgres re-authorizes); and a deterministic, model-free, multi-user fixture
harness (dogfood manifests + `AI_MODE=replay`) already exists to host the
fifty-query runner.

## 2. Retrieval-path inventory (current code)

All paths below are CODE-EVIDENCED unless labeled otherwise. Backend root:
`/Users/feihuyan/travel-workspace/travel-agent/backend`; mobile root:
`/Users/feihuyan/travel-workspace/travel-app`.

### 2.1 Universal Search (personal, grouped)

- Route: `POST /api/universal-search` — `backend/api/routes/universal_search.py:44-134`
  (rate limit 60/min `backend/api/rate_limits.py:43`; trip IDOR guard
  `universal_search.py:80` via `core/db/trips/members.py:392-405`).
- Engine: `backend/search/dispatch.py` (1072 lines). Scope groups at
  `dispatch.py:78-106`, builders `dispatch.py:412-790`, concurrent per-group
  execution with graceful degradation `dispatch.py:879-892, 1033-1044`.
- Searchable identities (entity_type emitted): `trip`, `itinerary_block`,
  `venue`, `atlas_artifact`, `conversation`, `dossier`, `angle`, `person`
  (mutual-trip companions only), `booking`, `receipt`, `expense`,
  `settlement`, `action`.
- Retrieval technology: pg_trgm SQL for most groups (`core/db/search.py`),
  Qdrant BM25/hybrid for venues and Atlas artifacts (`core/vector/atlas.py:190`
  enforces the `user_id` filter inside the vector layer), PostGIS for NEARBY
  (venues only, `dispatch.py:319`).
- Ranking: per-group scores only; **no cross-group ranking by design**
  (`dispatch.py:19-28`, `core/models/universal_search.py:171-180`). No
  ambiguity handling — N rows per group (default 5, cap 20), no
  disambiguation, no cross-group dedup of the same real-world object.
- Envelope: `UniversalSearchItem` (`core/models/universal_search.py:101-131`)
  = title/subtitle/meta strings + `provenance{label, privacy}` + `route` +
  `score`. It carries **none** of: why-it-matched, truth state, author,
  source refs, structured time roles, correction affordances. Truth columns
  are selected then discarded (e.g. itinerary `status`/`booking_state`
  selected at `core/db/search.py:1379-1399`, dropped at
  `dispatch.py:602-616`).
- Dead/stale surfaces inside the module: `backend/search/interpreter.py`
  (LLM query interpreter — zero production callers; route hardcodes
  `interpretation = None` at `api/routes/search.py:419`) and
  `backend/search/venues.py` (zero importers, drops `score`).
  `backend/search/FEATURE.md:11-26` documents interpreter behavior that does
  not exist — stale doc. `backend/search/fusion.py` (RRF) is used only by
  Discover search (`api/routes/search.py:341,444`), not Universal Search.

### 2.2 Discover search (public catalog, flat)

- Route: `POST /api/search` — `backend/api/routes/search.py:301`; RRF fusion
  via `backend/search/fusion.py`; result model carries `match_sources` and
  `snippet` (`core/models/search.py:64,77`) — the only "why it matched"
  signal in any served envelope today, but only for public editorial/venue
  content. Suggest and nearby endpoints are unauthenticated
  (`search.py:519,668`).

### 2.3 Places search (relationship-truth-bearing)

- Route: `GET /api/places/search` — `backend/api/routes/places.py:247` →
  `backend/places/search.py:31`. `PlacesRankedItem` carries a real truth
  envelope: `PlacesRelationshipTruth{saved, taste_match, in_trip, loved,
  from_trip, from_guide, saved_by_friend, encounter}` with
  `PlacesEncounterTruth{count, last_date, trip_id, source}` and an explicit
  `UNKNOWN` marker-knowledge state
  (`core/models/places_projection.py:96-137`). The same underlying retrieval
  (`search_place_rows`) feeds Universal Search, which projects this truth
  away (`backend/places/search.py:24` vs `backend/search/dispatch.py:154`).
  This is the strongest existing precedent for the benchmark §2 contract.

### 2.4 Atlas search

- `GET /api/atlas/search` (`backend/api/routes/atlas.py:741-800`): kept
  memories (Qdrant dense/hybrid with pg_trgm fallback,
  `core/db/atlas.py:645-650, 839-840`), pending candidates, Travel-DNA
  phrases. Owner-scoped only.

### 2.5 Experience-graph read models (not yet searchable)

- Experience-graph reads (`backend/api/routes/experience_graph.py`) serve
  viewer-scoped projections over the clean-break graph
  (`backend/core/experience_graph_projection.py`,
  `backend/domains/experience_graph/repository.py:546`), with an explicit
  guard that viewer scope "must never fall through to a whole-table evidence
  read" (`repository.py:743`).
- `GET /api/artifact-projections/intake/{anchor_id}`
  (`backend/api/routes/artifact_projections.py:40-75`) serves
  `CanonicalArtifactProjectionV1` — mine-only; `together` mode returns 403
  until a graph-owned sharing authority exists
  (`artifact_projections.py:28-56`).
- Neither is reachable from any search path: no text or semantic index
  exists over anchors, occasions, occurrence evidence, or outcomes (see
  coverage matrix).

### 2.6 Mobile consumers

- `app/search.tsx:35-92` hosts
  `components/search/UniversalSearchOverlay.tsx` (sole consumer of
  `hooks/useUniversalSearch.ts:43-113`). Rows render glyph + title +
  subtitle + provenance label + meta string
  (`UniversalSearchOverlay.tsx:859-892`). `provenance.privacy` is
  transmitted but never read by any component (sole FE occurrence is the
  type declaration, `utils/api/universalSearch.ts:50`); no truth state, no
  authority, no correction affordance is rendered. The Ask-Vesper handoff is
  a client-side regex heuristic (`UniversalSearchOverlay.tsx:131-136`).
- The Life dev lab (`app/dev/canonical-artifact-life.tsx`) runs entirely on
  frontend mock fixtures (`constants/mocks/canonicalArtifactFixtures.ts`) —
  no search affordance, no backend read.

### 2.7 Raw-query telemetry and retention (benchmark §8)

- Server logs store `query_len` only, never raw text
  (`api/routes/universal_search.py:114-127`, `api/routes/search.py:284-293`).
  The only raw-query log lines are in the dead interpreter
  (`backend/search/interpreter.py:74,78,94` — currently unreachable).
- Client telemetry durably stores a **32-bit FNV-1a `query_hash`** per user in
  Postgres `user_events.context`
  (`travel-app/utils/universalSearchTelemetry.ts:38-45`,
  `travel-app/utils/stableHash.ts:7-14`, `backend/core/db/events.py:27-54`,
  table `core/db/_tables/conversations.py:480-506`). A 32-bit
  non-cryptographic hash over short queries is reversible by enumeration —
  a re-identifiable fingerprint, not redaction; it would FAIL benchmark §8
  as durable query-derived state.
- On-device: last 5 raw query strings persist in AsyncStorage
  (`travel-app/utils/universalSearchRecents.ts:65-74`), plus an
  opened-entity ledger storing titles of opened private objects
  (`utils/universalSearchOpened.ts:11-23`).
- Ask-Vesper persists the raw query server-side as a chat message
  (`UniversalSearchOverlay.tsx:469` → `app/conversations/create.tsx:561-575`)
  — user-initiated, but a durable raw-query path.
- No search-history table exists (zero hits for
  `search_history`/`search_queries`/`query_log` in backend). PostHog carries
  no search events (`backend/core/telemetry.py` Event enum).

### 2.8 Viewer-relative authority at read time

- Read-time filtering exists but is **membership-binary ownership**, not an
  audience/grant model: per-retriever guards at
  `core/db/search.py:1321-1322` (trips), `:2002-2013` (conversations),
  `:2131-2139` (people, requires `public_profile_enabled`),
  `:1545-1548`/`:1759-1762` (actions, `visibility != 'private'`),
  `:1640` (masked expenses), `:1904-1908` (receipts).
- ABSENT after checking `core/db/_tables/*.py`, `core/db/search.py`,
  `search/dispatch.py`: any `audience` column, any `user_blocks`/`mutes`
  table, any `can_view` helper, membership epochs (membership revocation is
  a row delete; "was a member during the trip" is inexpressible), any role
  distinction in read paths (`trip_members.role` exists at
  `core/db/_tables/trips.py:208-220`, but no search reader consults it).
- Known read-side authority hole: `_search_trip_settlement_shares`
  (`core/db/search.py:1698-1703`) exposes settlement rows joined to
  `expenses.title` without the masked-expense guard its sibling readers
  apply — a masked gift expense's title can leak through COSTS settlements.

### 2.9 Embedding and semantic-index coverage

Vector store is Qdrant only (no pgvector anywhere; every collection is a
registered derived artifact, `core/derived_artifacts.py:66-236`). Exactly six
write paths produce vectors (`core/vector/embed_brief.py:123,295`,
`core/vector/angle_embeddings.py:60`, `core/db/atlas.py:455`,
`core/vector/traveler_observations.py:18`, `core/vector/trip_similarity.py:130`,
`lookup_agent/cache.py`). Per object type:

| Object type | Semantic index | Query path today |
| --- | --- | --- |
| Venues / sites / experiences / accommodations / places (public catalog) | YES — `venue_briefs`, `site_briefs`, `experience_briefs`, `accommodation_briefs`, `place_briefs` (dense 768 + BM25 hybrid, `core/vector/collections.py:268-681`) | Discover + Universal Search PLACES + planning fan-out |
| Editorial narration chunks | YES — `narration_fragments`, read path hard-filters `review_status == "approved"` (`core/vector/narration_fragments.py:146-148`) | narration/guide retrieval |
| Atlas memories (user's own) | YES but **double-flag-gated, default off** (`ATLAS_SEMANTIC_WRITE`/`ATLAS_SEMANTIC_READ`, `core/db/atlas.py:437,878`); only `title + one_line_read + place_label` is embedded — the body is never embedded (`core/vector/atlas.py:75-77`) | Atlas + Universal Search ATLAS (pg_trgm fallback) |
| Agent memory observations | YES, always on — IDs-only from Qdrant, Postgres re-authorizes (`core/vector/traveler_observations.py:68`, `concierge/memory_tools.py:701-1018`) | chat `recall` tool only |
| Whole trips | YES — `trip_similarity` retrieval documents with mandatory caller-supplied authorized-trip allow-list (`core/vector/trip_similarity.py:213-285`) | chat trip-management tools |
| Photos / media | NO — reachable only by trip, block, GPS, time (`core/db/photos.py:14-49`, `core/db/photo_auto_tag.py:38-144`); EXIF capture time + GPS→block binding exist; `alt_text` written, read by nothing; no people tagging anywhere | none |
| Tickets / bookings / reservations | NO — pg_trgm over booking rows only (`core/db/search.py:1427-1447`) | Universal Search RECEIPTS |
| Ingested email/share sources | NO — `inbound_items.raw_text` has no vector, tsvector, or trigram index (`core/db/_tables/inbound_items.py:104-110`) | status/owner lookups only |
| Occasions / occurrence evidence / place affinity | NO — structural indexes only (`core/db/_tables/outcomes.py:28-79`, `_tables/place_affinity.py:32`) | none |
| Persons / contacts | NO — `display_name` ILIKE within shared trips (`core/db/search.py:2105-2139`) | Universal Search PEOPLE |
| `user_facts` / personal memories / hard constraints | NO — exact namespaced-key lookup only (`core/db/user_facts.py:211,247`) | chat memory handlers |
| Generated compositions | NO — **not durably persisted at all**; assembled per request, Redis-cached ephemerally (`composition/copy_cache.py:1-22`) | none |

Reranker: Cohere `rerank-v3.5`, off unless `COHERE_API_KEY` present
(`core/vector/rerank.py:52-98`); sole caller is planning fan-out with 3×
over-fetch (`planning_agent/fan_out_search.py:510-535`). No user-facing search
reranks.

Latent finds: three `markdown_tsv` TSVECTOR GIN indexes are maintained on
every write and read by nothing (`core/db/_tables/itinerary.py:66-79`,
`_tables/users.py:215-229`, `_tables/trips.py:261-278`); the
`place_content_primitives` vector corpus has no query path (side-build only,
`core/vector/place_content_sidebuild.py:382`).

Source custody (intake v2): `intake_submissions` + `intake_source_objects`
carry custody/processing/admission status, retention mode,
`content_sha256`, `custody_receipt_sha256`, and `revoked_at`
(`core/db/_tables/intake_v2.py:40-117`) — real custody, CODE-EVIDENCED.
Sender/author of a forwarded email is deliberately NOT a column — only a
`message_identity_sha256` digest survives structured capture
(`inbound/email_forward.py:109-129, 200-204`); attribution is unqueryable
without parsing the archived S3 blob.

### 2.10 Chat-side retrieval tools and direct-answer safety

- Model-visible read tools over personal history
  (`concierge/tool_registry.py:574` `_EXPLICIT_READ_NAMES`): `recall`
  (observations — the one always-on semantic personal lane;
  `concierge/memory_tools.py:283, 985`), `trip_find` / `trip_read_snapshot`
  / `trip_find_similar` (`concierge/tool_handlers/trip_management.py:114-331`),
  `conversation_search` / `conversation_read_window` (pg_trgm with
  participant-join authorization, `core/db/conversations/_search.py:80-119`;
  structured citations `conversation_history.py:178-183`),
  `itinerary_read*`, `expense_summary`, `whereabouts`. User facts reach the
  model only by prompt injection, never as a searchable read
  (`concierge/turn_context.py:1289`).
- **Atlas is not chat-readable**: no tool reads the user's Atlas
  timeline/candidates (only `post_atlas_draft`, a write —
  `concierge/tool_handlers/atlas.py:18`).
- `recall` is hard-blocked in group conversations
  (`memory_tools.py:679-686`) and rejects cross-user access
  (`memory_tools.py:651-664`) — read-time authority done right in this lane.
- Direct-answer safety is layered but asymmetric:
  - Venue-name grounding is deterministically enforced
    (`concierge/output_guards.py:1341` `_check_grounding`; anti-pattern
    documented in `_prompts_skills.py:203-227`).
  - Negative claims require `grounded_empty == (total_count == 0)`
    (`concierge/_output_validators.py:233, 384`;
    `trip_discovery_prompt.py:8-13`).
  - Operational-fact backing ships log-only by design
    (`output_guards.py:1392-1401, 1528`).
  - **No guard joins occurrence assertions to `event_state`** — nothing
    prevents a planned block being narrated as occurred; past days are
    collapsed to "(completed, N blocks)" from the date alone
    (`concierge/turn_context.py:793-798, 812-814`), and
    `_effective_blocks` returns all non-cancelled blocks as trip content
    when none is marked (`core/trip_retrieval_document.py:344-358`). This
    is the single highest-value new oracle a fixture runner should add.
- `lookup_agent` is a live venue lookup (route-only,
  `api/routes/lookup.py:10`; not in the concierge loop) with a semantic
  answer cache (cosine ≥ 0.90, per-type TTLs,
  `lookup_agent/cache.py:34-63`, `config/settings.py:8-17`). It has no
  access to personal history at all (`schemas.py:10-19`) — so it cannot
  conflate lanes, but its responses carry no as-of timestamp
  (`schemas.py:87-96`), weakening HC role separation.

## 3. Query-to-current-code coverage matrix (Q01–Q50)

Rating convention:

- **COVERED** — a served read path could answer the query with target rank,
  truth, and authority mostly intact today.
- **PARTIAL** — retrieval exists without the required contract, or the data
  model can represent the answer but no query path serves it. The split
  (read capability vs durable authority) is noted per row.
- **ABSENT** — neither a query path nor a representing model exists.

Scoring dimensions (benchmark §5): T=Target rank, Tr=Truth, Au=Authority,
O=Orientation, S=Source identity, R=Repair, C=Continue, St=State restraint.
"Fails" lists dimensions that would score 0–1 today. "Oracle" names any hard
failure oracle current code would trigger. Backend paths are relative to
`/Users/feihuyan/travel-workspace/travel-agent/backend`.

**Headline: 0 COVERED / 24 PARTIAL / 26 ABSENT.**

One systemic finding colors nearly every row: the benchmark's telemetry
oracle (St) fails globally today — `query_hash` is durably stored per user
(§2.7) — and the truth/authority dimensions fail globally in the served
Universal Search envelope even where retrieval succeeds, because the envelope
discards truth and authority columns it already selects (§2.1).

### L01 — Europe Journey

| ID | Rating | Current code path / missing capability | Fails | Oracle triggered today |
| --- | --- | --- | --- | --- |
| Q01 ferry booked-not-taken | PARTIAL | Booking rows searchable (`core/db/search.py:1427-1447` via RECEIPTS). "Booked but not occurred" IS representable as a conjunction: `commitment_state='booked'` × `event_state='planned'/'skipped'` (`core/db/_tables/itinerary.py:187-194, 234-236, 257-273`) — but no named `unused` state exists and **no code queries the conjunction**. Read gap only. | Tr, S, R | **YES — "hiding it because unused":** itinerary search hard-filters `status='cancelled'` and `event_state='skipped'` (`core/db/search.py:1398-1399`), so the not-taken segment is excluded from ITINERARY results. |
| Q02 pasta photo after Amalfi | ABSENT | No photo search path exists at all (§2.9; `core/db/photos.py:14-49` is list/geo only). EXIF time + GPS→block binding exist (`media/photo_metadata.py:28-108`, `core/db/photo_auto_tag.py:38-144`) — the *data* for "after Amalfi" adjacency is stored, unqueryable. | T, O, S | Photo simply not returned (target absent). |
| Q03 hotel before Rome | ABSENT | Keyword search would match "Rome" — journey-order-relative queries ("before X") are inexpressible. The only temporal-adjacency primitive is an in-memory `pairwise` walk over one day's loaded blocks (`core/itinerary_open_windows.py:35-88`) that fails strictly on untimed/overlapping blocks; no SQL predicate or index for "block before/after X". | T, Tr, O | **YES — returning a Rome hotel** (keyword match on "Rome"). |
| Q04 what changed after Nice | PARTIAL | A plan-revision chain WITH author exists on the itinerary lane: `itinerary_operations` (14 op types, `initiator ∈ human/vesper/system/provider`, `human_principal_id`, parent/inverse links — `core/db/_tables/itinerary_v2.py:62-142`) with before/after deltas projected by `core/itinerary_history_gateway.py:2081-2107`. Missing: any MR composer or query path over it. (Graph-lane `commitments.revision` bumps in place with no history, `domains/experience_graph/schema.py:475-506`.) | T, O | Exhaustive-recap risk only via chat; deterministic answer unreachable, not unrepresentable. |
| Q05 which train got us to Rome | PARTIAL | Block keyword search can hit the train (`core/db/search.py:1346`); occurrence evidence could confirm taken (`schema.py:690`) but is never joined. | Tr, S | **YES — ticket alone asserted as taken** (no occurrence join; UI shows the block as fact). |
| Q06 place in Rome where Aeneas came up | PARTIAL | A kept Atlas memory mentioning Aeneas is reachable via pg_trgm/semantic Atlas search (`core/db/atlas.py:839`, flag-gated semantic §2.9); chat `recall` reaches observations (`concierge/memory_tools.py:701`). Place binding exists on artifacts; film Source linkage absent. | O, S, C | Broad-results risk; no authorship split (S). |
| Q07 plan for the hottest day | ABSENT | No historical weather datum store; no plan-by-date query semantics; no separation of current-at-the-time external evidence. | T, Tr, O | **YES — current weather substitution** would be the only available path (chat live lookup). |
| Q08 tickets I sent during the trip | PARTIAL | RECEIPTS/bookings pg_trgm exists; intake v2 custody is real (`core/db/_tables/intake_v2.py:40-117`) — but forwarded-source text is unindexed (`_tables/inbound_items.py:104-110`), used/unused never surfaced, custody never rendered. | Tr, S, R | **YES — unused ticket omitted** (same filter as Q01) **and source custody hidden.** |
| Q09 why did the route change | PARTIAL | The revision chain itself is recoverable (`itinerary_operations` + `itinerary_operation_transitions.evidence` before/after, `itinerary_v2.py:62-158`; proposal rebasing `:183-244`). The causal *reason* exists only if authored; no authored-explanation link, no MR composer, no query path. | T, Tr (cause), S | **RISK if chat answers — fabricated cause from timing**; no guard joins "reason" claims to operation evidence. |
| Q10 Italy → NYC this weekend | ABSENT | Opening candidates exist but are producer-driven, not query-driven (`core/models/experience_graph.py:258-277`, `lived_experience/*`); no HC handoff joins historical thread + refreshed NYC truth on demand. | T, Tr, C | Recommendation-from-inferred-identity risk via concierge feed rather than evidence-grounded possibility. |

### L02 — Brooklyn dinner Occasion

| ID | Rating | Current code path / missing capability | Fails | Oracle triggered today |
| --- | --- | --- | --- | --- |
| Q11 who was bringing dessert | PARTIAL | The graph represents it: `commitments.subject` + `commitment_participants.attendance_intention` (`schema.py:475-524`); read via experience-graph projection (`api/routes/experience_graph.py`). Read gap: no NL query path; no GA composer. | T (not reachable by query), O | Commitment vs fulfillment IS separable (CommitmentStatus vs occurrence evidence) — oracle avoidable in data, not in any served answer. |
| Q12 what time did we move dinner to | PARTIAL | Depends on lane. Graph lane (chat-created Occasions): revised time = current `commitments.time_window` with an in-place `revision` counter — prior time and revision author unrecorded (`schema.py:475-506`). Itinerary lane: full lineage exists (`itinerary_operations` `move`/`replan` deltas with `current_time_start`/`proposed_time_start`, `core/models/itinerary_operations.py:1195-1212, 1356-1358`). No query path over either. | Tr, S (graph lane) | **YES on the graph lane — hiding revision lineage** (original time unrecoverable). Avoidable on the itinerary lane. |
| Q13 receipt Alex added | PARTIAL | Receipts searchable per trip (`core/db/search.py:1904-1908` guard); contributed time = row `created_at`; attribution flattened into prose strings (`search/dispatch.py:704-716`), author never a field. | S, Tr | Attribution loss in the served envelope (payer name embedded in subtitle text only). |
| Q14 photo of the pasta on the table | ABSENT | No photo search (as Q02); `visibility ∈ {private, group, group_and_learn}` exists on `trip_photos` (`_tables/trip_photos.py`) but no withdrawn-contributor concept. | T, Au | Target absent. |
| Q15 what did Maya contribute | ABSENT | No contribution-lane read model; the 5-axis grant taxonomy is DOCUMENTED TARGET only (contribution contract docs); no `audience`/grant tables exist (§2.8). | T, Au, S | Risk of unqualified group summary via chat. |
| Q16 who actually came | PARTIAL | Strong substrate on BOTH lanes: `itinerary_block_participation` separates `attendance_intention` from per-person `occurrence_state ∈ planned/happened/did_not_happen` (`itinerary_v2.py:259-298`), and `occurrence_artifact.py:93-98` yields exactly `confirmed/proposed/unmarked` — "no evidence ≠ absent" is first-class. Graph lane: `occasion_members` + `occasion_invitations` + `graph_occurrence_evidence` (`schema.py:353-431,690`). No GA composer; no query path. | T, O | RSVP-vs-attendance separation exists in the model — no served answer keeps them separate. |
| Q17 invitation → dinner changes | PARTIAL | Invitations, decisions, votes are durable (`schema.py:380-451`); a state-transition MR read model is absent. | T, O, S | Full-transcript risk only via chat. |
| Q18 only what was shared with everyone | PARTIAL | Per-item audience DOES exist across ≥6 vocabularies (writeback `visibility private/group/system` `core/db/_tables/itinerary_history_v2.py:173-176`; `participation_scope` `itinerary.py:154`; relationship-memory `visibility` `_tables/relationship_memory.py:62-83`; content `VisibilityScope` `core/models/content_contracts.py:40-44`; attention `audience_rule` `_tables/notifications.py:243-244`), and membership-epoch machinery exists (`api/routes/_membership_events.py:50-74`; member removal transactionally retires shares/votes/signals, `core/db/trips/members.py:820-892`). Missing: a composed shared-core projection under the viewer's epoch — the "Together" projection 403s (`api/routes/artifact_projections.py:50-56`); Universal Search consults none of these vocabularies. | T, Au (legibility) | Epoch/majority-disclosure violations preventable in principle but unenforced in any search read. |
| Q19 could we do this again next month | ABSENT | No pattern-plus-current-calendar HC path; calendars not integrated; possibility generation is producer-side only. | T, C | Auto-plan oracle avoided today only because nothing answers at all. |

### L03 — Museum ticket not attended

| ID | Rating | Current code path / missing capability | Fails | Oracle triggered today |
| --- | --- | --- | --- | --- |
| Q20 museum ticket never used | PARTIAL | Ticket row searchable via RECEIPTS; `missed` state representable (graph) and `SKIPPED` exists in `PlaceRelationshipState` (`lived_experience/place_relationship.py:14-19`); never joined to search. | Tr, R | **YES — omitted-because-unused** in ITINERARY scope (`core/db/search.py:1398-1399`). |
| Q21 Tuesday plan in Rome | PARTIAL | Blocks carry day + date (`search/dispatch.py:602-616`); text-only matching — no by-date/by-weekday query. Plan-vs-occurred separation not in envelope. | T, Tr | Plan rewritten oracle avoided (blocks immutable-ish), generic-itinerary risk via chat. |
| Q22 which booked places did we skip | PARTIAL | `event_state='skipped'` exists on blocks and `SKIPPED` in Places relationship truth; PlacesRelationshipTruth is served in Places search (`core/models/places_projection.py:96-137`). No booked-minus-occurred set query. | T, Tr | **YES — reservations treated as visits** wherever only booking rows exist (no occurrence join in any list). |
| Q23 did I go to that museum | PARTIAL | Calibrated substrate exists: per-person `occurrence_state` + `unmarked` (`core/db/occurrence_artifact.py:93-98` — "another participant may have marked the shared event as happened without proving that this person attended"), `PlacesEncounterTruth` + `UNKNOWN` marker knowledge (`places_projection.py:96-137`); the reconciler never infers `skipped` (`core/db/occurrence_reconciliation.py:6-7`). But the likely responder is chat, and **no output guard joins occurrence-assertions to `event_state`** — grounding guards cover venue names (`concierge/output_guards.py:1341`) and zero-claims (`grounded_empty`, `concierge/_output_validators.py:233`), not planned-vs-occurred (verified absent by sweep of `output_guards.py` + prompts + eval checks). Worse: rejecting an occurrence proposal writes only `state='rejected'` — **"I never went there" has no write path** to `did_not_happen` (`occurrence_reconciliation.py:604-628`). | Tr (calibration), R | **RISK — confident yes from possession** if chat reads booking/itinerary rows; no guard exists. |
| Q24 why wasn't it in visited places | ABSENT | No rule-explanation read model; Plan-vs-Occurrence eligibility logic exists implicitly in Places layers but is not introspectable. | T, O, R | Consent-free auto-correction risk low (no correction path from search at all). |
| Q25 exhibition near me now (HC) | PARTIAL | Current-world truth machinery is genuinely strong: per-field freshness TTLs (`places/cache.py:37-40`), a first-class `HOURS_STALE` reason that degrades to `NEEDS_VERIFICATION` and never softens to yes (`places/actionability.py:48,111-117,155-207`), stale-while-revalidate on Places reads (`places/linker.py:324-331`), durable refresh queue (`places/refresh_queue.py:29-45`). The HC join is absent: historical-result read paths never trigger a refresh (`places/returns.py` reads cache only), and `lookup_agent` responses carry no `fetched_at`/as-of timestamp (`lookup_agent/schemas.py:87-96`). | Tr (role separation), C | Stale-exhibition risk on the historical path; historical/current separation unexpressed in any envelope. |
| Q26 keep, but don't bring it up | PARTIAL | Entity-scoped suppression exists in several places: opening snooze/mute (`lived_experience/opening_contract.py:47-63`), treatment suppression with reasons (`lived_experience/treatment.py:51-122`), `user_not_now` arbiter suppressions (`core/db/arbiter_suppressions.py:19-40`), home dismissals, and place-level `not_for_me`/`user_state` shields that all read paths honor (`core/db/place_affinity.py:1033-1087, :395-1021`). None is scoped to search returns; no scope preview; no general return-policy compiler. | R (narrowness), Au | **RISK — "keep" treated as resurfacing consent** cannot be evaluated; no shared vocabulary between search and suppression. |

### L04 — Film/book becomes relevant in Rome

| ID | Rating | Current code path / missing capability | Fails | Oracle triggered today |
| --- | --- | --- | --- | --- |
| Q27 movie I saw before Italy | PARTIAL | `AnchorKind.attention` + attention artifact family exist (`core/models/experience_graph.py:217-224`, `inbound/semantic_contract.py:36`) so a watched-film anchor is representable with `captured_at`. Anchors are not text-searchable. | T, Tr | Watched-vs-release confusion unguarded (no media metadata model). |
| Q28 Colosseum → Troy observation | PARTIAL | If authored as an observation: semantic recall reaches it (`concierge/memory_tools.py:701-704`, always-on) with Postgres re-authorization. Atlas artifact alternative reachable by search. Claim provenance (founder's authored claim vs Vesper) not represented. | S, O | **RISK — crediting Vesper**: recall output enters chat prose with no authorship contract. |
| Q29 Rome article with manifest | ABSENT | Generated compositions are not persisted (`composition/copy_cache.py:1-22` — explicitly ephemeral); no manifest, no revision. | T, S, R | Target cannot exist to be re-found. |
| Q30 where else did that film come up | ABSENT | No cross-reference/occurrence graph for media Sources; semantic similarity would be the only path — exactly the forbidden substitute. | T, Tr, S | **YES if answered — semantic similarity presented as historical occurrence** is the only available mechanism. |
| Q31 my observation vs Vesper's | ABSENT (for personal compositions) | Claim-local roles DO exist — in the place-content lane: `AuthorityRole` (11 roles incl. `system`) × `TruthMode` × `EvidenceMaturity` with hard invariants, `ClaimEnvelope.evidence_refs` min 1 (`core/models/content_contracts.py:29-177`). Nothing applies this to personal compositions (which are not persisted, Q29); viewer-relative authorship exists for proposals (`core/proposal_eligibility.py:21-81`) but not for prose claims. | S, T | **YES — whole-output-labeled-only** is the best any personal surface could do. |
| Q32 sources for the Augustus connection | ABSENT (for personal compositions) | The claim→source pattern exists in place content: `SourceLineage` per evidence ref + `ContentDecisionReceipt` with a complete selected/rejected partition (`content_contracts.py:82-268`, persisted `core/db/_tables/place_content.py:177-205`). No personal-article claim carries citation spans. | S, Tr | **YES — citation list for whole article** is the only representable form. |
| Q33 remove note from articles, keep movie | ABSENT | No downstream-use reverse index: `place_content_decision_receipts.selected_claim_ids`/`evidence_refs` are un-indexed arrays — no code queries receipts by claim id; `ClaimEnvelope.correction_refs` is declared and never read; `CompositionReason.CORRECTION_INVALIDATED` is hard-scoped to one family (`lived_experience/composition.py:138-139`). `core/derived_artifacts.py` is corpus-level (rebuild policies), not claim-level. | R, S | **RISK — paraphrase leakage** unpreventable; dependents unenumerable. |
| Q34 follow this thread in NYC | ABSENT | As Q10. | T, C | — |

### L05 — Rome–Paris social comparison

| ID | Rating | Current code path / missing capability | Fails | Oracle triggered today |
| --- | --- | --- | --- | --- |
| Q35 Maya's Paris photo about the heat | ABSENT | No photo search + no cross-user contribution lanes + no precision-reduction model. | T, Au | Target absent; precision violation impossible to commit only because nothing returns. |
| Q36 Rome and Paris that same week | ABSENT | No attributed two-lane comparison read model; no authorized-lane join. | T, Au, S | Synthetic-shared-feeling risk via chat. |
| Q37 transit note Maya shared with me | PARTIAL | Two real person→person grant lanes exist: place handoffs (`domains/relationships/repository.py:433-747` — viewer-scoped get/list, pull grants `:651`) and directional relationship-visibility grants with precision tiers (`core/db/relationship_visibility.py:167-227`). Both cover places/location, not notes; neither is text-searchable. | T (scope), S | Stale-audience risk low (grants checked at read); note-shaped shares unrepresentable. |
| Q38 restaurant we compared afterward | ABSENT | No comparison object; no governed compared-place pair. | T, S | Joint-visit claim risk via chat. |
| Q39 only what Maya explicitly shared | PARTIAL | Place-handoff list is exactly "explicitly shared, viewer-authorized" for its narrow domain (`repository.py:554`). Everything else (photos, notes, routes) has no share lane. | T (scope), Au | Derived-guess leakage risk only via chat. |
| Q40 why can't I see her route anymore | PARTIAL | Revocation state exists and is well-built: directional `relationship_visibility_grants` with `granularity ∈ none/coarse/precise`, fail-closed resolution, read-time mutuality (revocation effective next read), `privacy_events` audit (`core/db/_tables/social.py:68-101`, `core/db/relationship_visibility.py:152-227`). Missing: any safe-abstraction *explanation* read model over that state. | T (explanation), Au | **RISK — leaking revoked detail in an explanation** if chat improvises; the deterministic policy answer is derivable but uncomposed. |
| Q41 send the heat comparison to Maya | ABSENT | The composition doesn't exist (Q29); no action-preview envelope for shares; chat share requires confirmation but has no authorized-content diff. | T, Au, C | **RISK — stale/over-scoped content in a share**; nothing computes "claims excluded by current grants". |
| Q42 don't show me anything involving Maya | ABSENT | No person-scoped return shield: no `user_blocks`/mute table anywhere in `core/db/_tables/` (verified independently twice); existing shields are entity-scoped only (place `not_for_me`/`user_state`, card dismissals) — never person-scoped. | Au, R | **YES — future leakage guaranteed**: nothing can enforce the request. |

### L06 — Longitudinal Red Hook Place relationship

| ID | Rating | Current code path / missing capability | Fails | Oracle triggered today |
| --- | --- | --- | --- | --- |
| Q43 Red Hook restaurant Maya and I went to | PARTIAL | The occurred-shared-visit join largely exists: `load_confirmed_encounters` joins itinerary → participation → `event_state='happened'` and excludes `occurrence_state='did_not_happen'` (`places/relationships.py:110-190`); companion×place affinity exists (`traveler_place_companion_affinity`, `_tables/place_affinity.py:112-160`, write-authorized to same-trip only). Missing: a person-cue query path composing them; person-level safety shields (no block table). | T, Au (safety) | **RISK — saved-returned-as-visited** in any keyword path that hits saved entities; **unsafe-Maya-rendering unpreventable** (no person shield). |
| Q44 ferry route I saved but never used | PARTIAL | Saved state exists (`traveler_place_affinity`, `_tables/place_affinity.py:32`; SAVED in `place_relationship.py:15`); routes are weakly represented; not-occurred contrast never surfaced. | Tr, T | **YES — omitted or shown without unused state** (no not-occurred rendering anywhere). |
| Q45 what did I do in Red Hook last spring | PARTIAL | Closest real capability: Atlas geo search (`geo_search_artifacts`, 50 km GEO index, `core/vector/collections.py:786-850`, `core/vector/atlas.py:197`) + `captured_at` — occurred episodes by place+period partially reachable for *kept memories only*. Honest-gap rendering absent. | Tr (plans/saves mixing), O | Mixing risk when keyword search unions saved + visited rows. |
| Q46 waterfront place I said I'd repeat | PARTIAL | Authored repeat intention storable as observation/outcome (`personal_outcomes.meaning`, `schema.py:720-760`); semantic recall could find it (chat lane only). | T, S | Inferred-preference oracle avoidable — explicit authored statement is a first-class object. |
| Q47 which Red Hook visits actually happened | PARTIAL | The truth substrate is the strongest here: `PlacesEncounterTruth` + occurrence evidence (7 evidence types with strengths, `_tables/outcomes.py:28-57`) + `LIVED` vs `SAVED`/`PLANNED` states; attendance-affinity seeding already honors `did_not_happen` (`tasks/trip_attendance_affinity.py:145-150`). Caveats: `RelationshipState.SKIPPED`/`CORRECTED` are dead enum members — the composer can never emit them (`lived_experience/place_relationship.py:83-150`, sole caller `canonical_providers.py:304-326`); no enumeration query with excluded-contrast rendering. | T, O | **YES today — reservations/saves counted as visits** in any current list that doesn't consult encounter truth (Universal Search PLACES shows "SAVED BY YOU" but no visited state). |
| Q48 why did Red Hook feel easier the second time | ABSENT | No longitudinal route/time comparison; `spatial_situation` is trip-bound; no familiarity model (correctly — but no evidenced MR either). | T, O | **RISK — psychographic/fabricated cause** if chat answers. |
| Q49 what can Red Hook make possible this weekend | ABSENT | As Q10/Q34 — possibility generation is producer-push (openings), not query-pull; no refreshed-world join on demand. | T, C | Stale-hours risk in any improvised answer. |
| Q50 hide dinner with Maya, keep Red Hook | ABSENT | No episode/person-scoped return exclusion; no scoped-hide vocabulary anywhere in read paths. | R, Au | **YES — unenforceable**; either nothing hides or everything would. |

### Matrix summary

| World | COVERED | PARTIAL | ABSENT |
| --- | ---: | ---: | ---: |
| L01 Europe Journey | 0 | 6 | 4 |
| L02 Brooklyn dinner | 0 | 6 | 3 |
| L03 Museum not attended | 0 | 6 | 1 |
| L04 Film/book bridge | 0 | 2 | 6 |
| L05 Rome–Paris social | 0 | 3 | 5 |
| L06 Red Hook | 0 | 5 | 3 |
| **Total** | **0** | **28** | **22** |

Missing READ capability vs missing DURABLE AUTHORITY, rolled up:

- **Missing read capability only** (the data or authority model exists;
  no query/projection serves it): Q01, Q04, Q05, Q08, Q09 (chain, not
  cause), Q11, Q13, Q16, Q17, Q18, Q20, Q21, Q22, Q23 (plus one missing
  write path — reject never writes `did_not_happen`), Q25 (plus the
  historical→refresh join), Q26, Q27, Q37, Q39, Q40, Q43, Q44, Q45, Q46,
  Q47.
- **Missing durable authority** (no model can represent the answer or the
  permission): Q07 (historical external evidence), Q12 on the graph lane
  (commitment revision history), Q15 (contribution lanes/grants beyond
  places), Q24, Q29–Q34 (persisted compositions + personal claim-local
  roles + downstream-use reverse index), Q35, Q36, Q38, Q41, Q42 + Q50
  (person-scoped shields — no block/mute table exists), Q48, Q49, plus
  Q02/Q14 (photo content identity stored, no photo retrieval identity) and
  Q03 (journey-order adjacency as a queryable relation).
- **Global St (state restraint) failure**: `query_hash` durable per user
  (§2.7) — every query starts at St ≤ 1 until removed.
- **Cross-cutting correction gaps** (hit R on many rows): corrections
  propagate transactionally for *memory* only (`core/db/memory_corrections.py:22-90`
  outbox + subscribers); occurrence/affinity/outcome corrections have no
  outbox (`memory_projection_outbox` accepts exactly one event type,
  `core/db/_tables/memory.py:324`); **no correction path touches Qdrant**
  (verified — corrected facts persist indefinitely in
  `traveler_observations`/`trip_similarity` vectors).

## 4. Renderer-neutral result envelope proposal

DOCUMENTED TARGET (proposal; nothing below exists as one served payload today).
The envelope deliberately extends two existing contracts instead of inventing a
third vocabulary:

- `CanonicalArtifactProjectionV1`
  (`/Users/feihuyan/travel-workspace/travel-agent/backend/core/models/canonical_artifact.py:126`)
  already carries viewer scope, truth-moded facts, provenance, unknowns,
  allowed actions, correction summary, and owner destinations — CODE-EVIDENCED.
- The intake semantic contract
  (`/Users/feihuyan/travel-workspace/travel-agent/backend/inbound/semantic_contract.py:23-58`)
  already defines `TruthMode`, `OccurrenceState` (including `artifact_only`,
  `contradicted`), and the Retention/Audience/Action authority tiers —
  CODE-EVIDENCED.

What neither contract has: query echo, why-it-matched, candidate sets with
bounded ambiguity, time-role separation as first-class fields, Around-this
landmarks, or a current-world refresh lane. The proposal:

```jsonc
{
  "schema_version": "life-refind-result.v1",
  "query": {
    "query_id": "anon-uuid",            // anonymized; raw text NOT persisted (benchmark §8)
    "session_ref": "ephemeral",
    "asked_at": "2026-09-01T14:03:00Z"
  },
  "viewer": {
    "viewer_id": "uuid",
    "scope": "mine | together",
    "membership_epoch": "opaque-rev",    // audience re-evaluated at read time (§2)
    "safety_overlays": ["person_shield:…"]  // opaque ids only; never explains a hidden relation
  },
  "form": "SF | GA | EP | MR | RP | HC",
  "confidence": {
    "kind": "single | bounded_candidates | none",
    "abstain_reason": null                // set when governed refusal/silence is the answer
  },
  "results": [
    {
      "rank": 1,
      "resource": { "kind": "experience_anchor", "id": "…", "canonical_path": "…" },
      "identity": { "semantic_type": "ferry_ticket", "title_key": "…" },
      "why_matched": [
        { "cue": "time_adjacency", "detail_key": "after_amalfi_departure" },
        { "cue": "media_kind", "detail_key": "photo" }
      ],                                   // machine cues + i18n keys; never free prose
      "time_roles": {
        "planned": "…", "occurred": null, "captured": "…",
        "authored": null, "generated": null, "current_world_checked": "…"
      },                                    // roles never collapsed (§2)
      "truth": {
        "occurrence_state": "planned | happened | missed | changed | unknown",  // ExperienceOccurrenceState
        "truth_mode": "source_extracted | user_confirmed | …",                  // TruthMode
        "confidence": 0.92,
        "conflicts": [ { "claim": "…", "sources": ["src-ref"] } ],
        "missing_evidence": ["attendance"]
      },
      "authorship": {
        "author_ref": "user-uuid | vesper | external:…",
        "claim_roles": [ { "span": "…", "role": "human | system | external", "source_ref": "…" } ]
      },
      "sources": [
        { "ref": "SourceRef", "custody": "original | derived", "status": "available|degraded|deleted",
          "used_state": "used | unused | unknown" }
      ],
      "parent": { "episode_ref": "occasion|journey ref", "relationship_ref": null },
      "around_this": [                      // max 3; expanded only on request (handoff §6.4)
        { "resource": "…", "relation": "preceding_movement", "time_role": "occurred" }
      ],
      "audience": { "visibility": "private | bounded_shared", "grant_basis": "opaque-grant-id" },
      "repair": {
        "operations": ["correct_occurrence", "detach", "exclude_return", "release_downstream", "delete_source"],
        "scope_preview_required": true      // action-preview queries (Q26/Q33/Q41/Q42/Q50) never auto-apply
      },
      "continue": [
        { "destination": "chat | places | owner_object", "authority_tier": "advise_only | propose_reversible",
          "context_envelope_ref": "cross-root continue envelope id" }
      ],
      "current_world": {                    // HC lane; null for purely historical results
        "refreshed_at": "…", "provider_truth_ref": "…", "staleness": "fresh | stale | unavailable"
      }
    }
  ],
  "candidate_note": {                       // present only when confidence.kind == bounded_candidates
    "distinguishing_cues": ["date", "city"],
    "max_candidates": 3
  },
  "retention": {
    "durable_state_created": false,         // hard invariant for scoring dim 8
    "telemetry": ["query_id", "result_ids", "form", "latency_ms"]  // never raw text
  }
}
```

Design notes:

- Every enum above already exists in code except `used_state`, `claim_roles`,
  `why_matched`, `time_roles`, and the `current_world` lane — those are the
  genuinely new obligations.
- `why_matched` is structured cues, not generated prose, so the deterministic
  phase (benchmark §6) can emit it without a model call.
- `results` is ordered; form `GA` may put a `governed_answer` object in place
  of `resource` but must still carry `truth`, `sources`, and `repair`.
- Suppression is expressed only as absence plus `safety_overlays` opacity —
  the envelope never explains *why* a hidden item is hidden (handoff §6.7).


Two refinements the coverage matrix forces on the envelope:

- `time_roles.occurred` must admit a fourth value beyond datetime/null:
  `"no_evidence"` distinct from `"did_not_happen"` — the codebase already
  makes this distinction (`occurrence_artifact.py:93-98` `unmarked` vs
  `itinerary_block_participation.occurrence_state='did_not_happen'`) and
  collapsing it would fail Q16/Q23/Q47.
- `sources[].used_state` should be derived from the existing conjunction
  (`commitment_state`/`booking_state` × `event_state`/`occurrence_state`)
  rather than a new column — the audit found the states present and only the
  join missing (Q01/Q20/Q44).

## 5. Deterministic fixture runner proposal

Status vocabulary target for this deliverable: **Architecture resolved** is
achievable now; nothing below is implemented.

### 5.1 What already exists to reuse (CODE-EVIDENCED)

The backend has a purpose-built offline, model-free, multi-user fixture
harness — the dogfood manifest lane — plus a scoring/replay lane:

- **World instantiation**: `tools/dogfood/content/seed.py` ("offline seeders…
  never call LLMs, web search, or product HTTP APIs"; dry-run by default,
  `--apply` gated, ops-guarded). Deterministic ids by construction:
  `uuid5(DOGFOOD_NAMESPACE, "{manifest_id}:{entity}:{key}")`
  (`tools/dogfood/content/schemas.py:76-111`); both seeder and verifiers
  re-derive ids through `dogfood_key` so they cannot drift.
- **Manifest shape**: `DogfoodManifest` (`schemas.py:1620-1650`) already
  declares 26 seedable collections — personas, trips, group profiles,
  itineraries, personal memories, observations, hard constraints, saves,
  affinity, conversations, atlas artifacts, expenses, booking sessions,
  trip photos, proposals, pending invites, trip stories, etc. — with a
  referential-integrity validator (`_refs_resolve`, `schemas.py:1657`).
  14 manifests exist to copy from (`tools/dogfood/content/manifests/`).
- **Model-call fail-closed**: `AI_MODE=replay` + `LLM_VCR_MODE=replay`
  (`backend/core/ai_mode.py:20-95, 237`; `backend/core/llm_vcr.py` — replay
  never falls back to a live call; a miss raises `VCRReplayMiss`). The
  journey certifier already runs token-free this way
  (`scripts/journey_cert/persona.py:42-44`).
- **Scoring vocabulary**: `tools/eval/core/models.py:12-88`
  (`CheckStatus{pass,fail,warn,error,skip}`, `CheckResult`), check
  registration decorators (`tools/eval/plugins/concierge/checks.py:30, 98`),
  config lint that hard-errors on stale check/tool names
  (`tools/eval/scripts/check_eval_configs.py`), the zero-LLM CI replay gate
  (`tools/eval/core/replay.py` — deterministic checks re-run against stored
  turn records, >5pp regression fails `--strict`), and baseline promotion
  (`tools/eval/cli.py:1587`).
- **State-transition grading**: `tools/eval/core/trajectory.py` grades
  whether a trajectory left correct canonical state behind; a YAML-mock
  world deliberately FAILS `stateful_trajectory`
  (`tools/eval/plugins/concierge/checks.py:190`) — an argument for seeding
  real Postgres via `seed.py` rather than the pure-YAML
  `tools/eval/core/fixtures.py` lane (which has venues/trips but no user
  graph).
- **Two correction memories to honor**: eval seed scripts rewrite YAML
  fixtures in place (always `git diff` after a run), and persona/baseline
  counts drift — current truth is **7 canonical identities** (not 6;
  `nadia` added 07-10, `tools/dogfood/content/scenarios.yaml:17-78`) and
  **41/41 concierge baselines** (not 35/36; `tools/eval/configs/concierge/`
  vs `tools/eval/baselines/`).

### 5.2 Proposed shape

1. **Fixtures**: one manifest per evidence world —
   `tools/dogfood/content/manifests/life-l01-europe.yaml` …
   `life-l06-redhook.yaml` — authored to the benchmark's §9 execution
   protocol. L02/L05 exercise multi-user seeding (already native: shared
   trips span personas in `frontend_mock_allowlist.yaml:11-25`). Gaps the
   manifest schema must grow before L-worlds are expressible (all named in
   §3): forwarded-source custody rows (intake v2), per-person
   `itinerary_block_participation` occurrence states, relationship
   visibility grants, place handoffs, and experience-graph occasions /
   commitments / occurrence evidence (`domains/experience_graph/schema.py`
   tables are not among the 26 seedable collections today).
2. **Runner**: a new `tools/eval/plugins/life_refinding/` plugin. Each of
   the fifty queries becomes one scenario config with: fixture world ref,
   viewer id, the query string, expected form (SF/GA/EP/MR/RP/HC), expected
   target id (re-derived via `dogfood_key`, never hardcoded), required
   truth/authority fields, and the hard-failure oracle expressed as a
   deterministic check. Phase 1 (deterministic) calls the retrieval read
   model directly — no model calls, `AI_MODE=replay` exported before any
   backend import. Phase 2 (optional augmentation, benchmark §6) records
   VCR cassettes separately and is excluded from the CI gate.
3. **Scoring**: implement the 8 benchmark dimensions as check functions
   registered through `_register_turn`-style decorators so the existing
   lint + replay gates recognize them; map dimension scores 0–2 into
   `CheckResult.details`; hard-failure oracles are `fail`-status checks.
   The §9 protocol steps 6–7 (apply correction → rerun → verify
   invalidation) become paired scenarios sharing one world with a mutation
   step between — `stateful_trajectory`-style before/after canonical
   snapshots make this gradeable.
4. **Telemetry constraint as a check**: assert after each run that no new
   durable row contains the raw query or a reversible digest of it —
   codifying benchmark §8 and catching regressions of the `query_hash`
   finding (§2.7).

### 5.3 What the runner cannot do until read models exist

The runner can instantiate all six worlds and *score* today's paths, but
§3 predicts the outcome: 0/50 pass. Its immediate value is (a) freezing the
worlds and oracles before design work, (b) regression-guarding each new
read model as it lands, (c) making the §9 correction/rerun loop executable.
Build it before, not after, the retrieval work.

## 6. Smallest-native-prototype recommendation

Goal: prove target-first refinding on device with the least new authority.
Everything below composes EXISTING truth substrate behind ONE new read
model and reuses the existing mobile search surface.

**Slice: L03 + the L01 transport/stay subset — queries Q01, Q05, Q08, Q20,
Q21, Q22, Q23 (7 queries, all SF/GA).**

Why this slice:

- It is the highest ratio of "data present, join missing" in the matrix:
  every required truth state already exists on itinerary/booking/
  participation rows (§3 L01/L03 rows); no new durable authority, no
  social/authority model, no photo index, no composition manifest needed.
- It directly kills the two most damaging live oracles: the
  cancelled/skipped exclusion filter (Q01/Q08/Q20 — `core/db/search.py:1398-1399`)
  and booked-treated-as-occurred (Q05/Q22 — the benchmark's central truth
  failure), plus it exercises calibrated negatives (Q23 `unmarked`).
- It fits the existing envelope precedent: extend the Places-style truth
  projection (`core/models/places_projection.py:96-137`) rather than
  inventing the full §4 envelope in one step.

Concrete minimal build (four pieces):

1. **One read model**: `refind_sources(viewer, q)` over bookings + itinerary
   blocks + participation + occurrence evidence, returning §4 envelopes with
   `used_state` derived from the `commitment_state × event_state ×
   occurrence_state` conjunction, `unmarked` preserved, and the
   cancelled/skipped filter REMOVED in favor of truth-labeled inclusion.
   pg_trgm retrieval is sufficient — no new index, no embeddings.
2. **One write path fix** (2-line class): make occurrence-proposal `reject`
   record a viewer-scoped `did_not_happen` (today it strands the canonical
   state at `planned` forever — `core/db/occurrence_reconciliation.py:604-628`);
   without it Q23's correction loop cannot close.
3. **Mobile**: render truth chips (planned / happened / skipped / booked-
   unused / no-evidence) + one "Around this" adjacent block in
   `UniversalSearchOverlay` rows for this result lane only — the overlay
   already has the row slots (§2.6).
4. **Telemetry**: drop `query_hash` from `universalSearchTelemetry.ts` in
   the same change (benchmark §8; §2.7).

Explicitly out of scope for the first slice: person cues (needs the person
entity + shields — L05/L06), photo queries (needs a photo retrieval
identity), compositions (needs persistence + manifest), HC handoff (needs
the historical→refresh join), and any NL query interpretation (the slice's
queries succeed with keyword + filter semantics; resurrecting the dead
`search/interpreter.py` lane is a later decision).

Fixture-scale proof: run the L01/L03 manifests + the seven scenario configs
from §5; the slice is done when those seven score ≥13/16 with zero hard
failures under the deterministic runner — "Consumer flow proven at fixture
scale" in the six-tier vocabulary, nothing more.

## 7. Open questions

1. **Which lane is the Life substrate?** The clean-break experience graph
   (`domains/experience_graph/`) duplicates the legacy itinerary lane's
   truth axes with different vocabularies (e.g. commitment revision has
   lineage in the itinerary lane, none in the graph lane — Q12). The
   benchmark can be passed on either, not on both at once. A ruling is
   needed before read models are built twice.
2. **Person entity**: L05/L06 and the handoff's own prototype queries ("the
   bar after meeting Teodora") are unrepresentable without a non-user
   person identity. Is that a new durable authority (contradicting the
   fixture pack's "no new owners yet") or a projection over
   `users`/`social_circles` plus authored mentions?
3. **Composition persistence**: benchmark Q29–Q33 requires persisted
   compositions with manifests; fixture-pack O2 says persist only on
   save/share/cite. The place-content lane's `ContentDecisionReceipt` is
   the proven pattern — does it get promoted to personal compositions, and
   does its missing claim-id reverse index get built there first?
4. **Query understanding**: the deterministic phase can pass SF/GA slices
   on keyword+filter semantics, but relative cues (Q03 "before Rome") need
   either structured query grammar or a model in the loop — which
   contradicts nothing in benchmark §6 (deterministic first, augmentation
   second) but needs an explicit latency/abstention contract.
5. **`query_hash` removal vs product analytics**: dropping it satisfies §8;
   does product analytics need a privacy-preserving replacement (e.g.
   k-anonymous query-length buckets), or nothing?
6. **Settlement masking hole** (§2.8): fix in place or fold into the
   refinding read-model work? It is a live read-side authority leak today,
   independent of this workstream.

## 8. Evidence discipline note

Every claim above is labeled or cited: CODE-EVIDENCED claims carry
file:line against the repo roots named in §2; DOCUMENTED TARGET marks
proposal content (§4–§6); ABSENT claims name the locations checked.
Dead-code identifications (interpreter, venues.py, SKIPPED/CORRECTED enum
members, markdown_tsv indexes, place_content_primitives corpus) were
verified by caller sweeps, not by absence of a single grep. Zero callers
was not treated as dead where a registry or mobile consumer could bind at
runtime (checked: tool registries, capability catalog, mobile API mirror).

## Applied safety fixes — 2026-08-31

Narrow fixes applied against this audit's findings (uncommitted, in
`travel-agent/backend`); tests: `tests/search/` (incl.
`test_masked_expense_search_leak.py`), `tests/api/test_events_api.py`,
`tests/api/test_search_api.py` — all green.

- **§2.8 settlement masking hole — FIXED.**
  `core/db/search.py`: `_search_trip_settlement_shares` now takes `actor_id`
  and applies the same guard as its siblings —
  `or_(expenses.masked.is_(False), expenses.paid_by == actor_id)` in its
  WHERE (`:1700-1709`); caller updated (`:1478`). A masked gift expense's
  title/amount can no longer leak through COSTS settlement rows to
  non-payers.
- **§2.7 durable per-user `query_hash` — FIXED at the ingest boundary.**
  The backend never names `query_hash`; it arrives inside the opaque
  telemetry `context` from `travel-app/utils/universalSearchTelemetry.ts:42`.
  `api/routes/events.py:71-83` adds `_scrub_durable_query_state`, applied in
  both the single (`:400`) and batch (`:511`) event endpoints, so the
  `query_hash` key is dropped before `user_events.context` is written —
  regardless of client version. `query_len` and other content-free metrics
  pass through unchanged. No migration was run; historical rows retain the
  field (retention/backfill is a separate decision, per open question 5).
  The client emitter still computes and sends the hash in transit — dropping
  it from `universalSearchTelemetry.ts` (§6 item 4) remains open in the
  app repo; the durable-state failure of benchmark §8 is closed server-side.

## Round 4 slice — build record — 2026-08-31

The §6 smallest-native-prototype BACKEND slice is built and fixture-proven.
All paths relative to `travel-agent/` unless noted. Uncommitted; additive to
the 08-31 safety batches.

### What was built

**Piece 1 — deterministic fixture runner (§5.2, built first per §5.3):**

- `tools/dogfood/content/manifests/life-l01-europe.yaml` — L01
  transport/stay subset (used flight, unused ferry + evidenced bus
  replacement, person-scope-confirmed train, Rome arrival landmark; booking
  sessions carry the ticket sources; second persona `noah` is the
  non-member authority probe).
- `tools/dogfood/content/manifests/life-l03-museum.yaml` — L03 (booked
  museum morning with a person-scoped did-not-attend correction, unticketed
  Pantheon stop with NO occurrence evidence, occurred forum walk and booked
  occurred trattoria dinner, plus a pending occurrence-reconciliation
  proposal as the Q23 correction fixture).
- `DogfoodManifest` grown minimally (`tools/dogfood/content/schemas.py`):
  two new collections, `occurrence_marks` (post-birth occurrence truth
  applied through the canonical `mark_occurrence` command, person- or
  group-scoped) and `occurrence_proposals` (pending reconciliation rows);
  both wired into `_refs_resolve` referential integrity.
  `tools/dogfood/content/seed.py`: `seed_occurrence_marks`,
  `seed_occurrence_proposals` (+ reset, `--kind` choices, plan counts).
  Registry allowlist: `tools/dogfood/content/check_manifest_registry.py`.
- `tools/eval/plugins/life_refinding/` — `runner.py`
  (`LifeRefindingEvalRunner`: seeds worlds idempotently through the dogfood
  seeder behind the ops-guard, re-derives every expected id via
  `dogfood_key`/uuid5, runs `refind_sources` directly, runs a non-member
  control query, snapshots durable state before/after), `checks.py` (the 8
  benchmark dimensions as 0–2-scored checks via the decorator registry;
  hard oracles as fail-status checks: `oracle_unused_included`,
  `oracle_not_reported_taken`, `oracle_no_possession_inference`,
  `oracle_plan_not_rewritten`, `oracle_reservations_not_visits`,
  `oracle_no_confident_yes`, `telemetry_no_durable_query`;
  `benchmark_total` enforces ≥13/16 + target/truth/authority=2 + zero hard
  failures). Seven configs: `tools/eval/configs/life_refinding/q0{1,5}_*`,
  `q08_*`, `q2{0,1,2,3}_*.yaml`. Registered in `tools/eval/cli.py` and
  `tools/eval/core/lint.py`. `AI_MODE=replay` exported in runner setup —
  phase 1 is fully deterministic, zero model calls.
- Telemetry check per §5.2 item 4: after each run the runner scans new
  `user_events` rows for the raw query and its 32-bit FNV-1a digest (the
  exact §2.7 finding); a hit is a hard failure.

**Piece 2 — the read model (§6 item 1):**

- `backend/core/models/life_refind.py` — `life-refind-result.v1` envelope
  (§4): anonymized query echo, form, structured `why_matched` cues (never
  prose), `time_roles.occurred` admitting `"no_evidence"` DISTINCT from
  `"did_not_happen"`, truth block reusing `ExperienceOccurrenceState` +
  intake `TruthMode`, `sources[].used_state` DERIVED from the
  commitment×event×occurrence conjunction (no new column), parent episode
  ref, `around_this` max 3, narrow repair operations with
  `scope_preview_required`, continue destinations with authority tiers,
  `retention.durable_state_created: false` as a hard invariant.
- `backend/life/refind_sources.py` — the read model: viewer-scoped
  membership join over legacy itinerary blocks + per-person participation +
  booking offers; deterministic cue grammar (unused/skipped-set/weekday/
  plan/attendance/kind cues) + keyword scoring; the cancelled/skipped
  exclusion filter does NOT apply (truth-labeled inclusion); zero writes.
  Lane ruling recorded in the module docstring: the CONTRACT is stable, the
  substrate is legacy rows today and swaps to the experience graph later.
  `backend/life/FEATURE.md` added (coverage guard).
- Served: `POST /api/life/refind` (`backend/api/routes/life_refind.py`,
  registered in `backend/api/router_registry.py`) — viewer-scoped via
  `get_current_user`, optional trip scope behind the membership guard,
  query_len-only logging.

**Piece 3 — the did_not_happen write fix (§6 item 2):**

- `backend/core/db/occurrence_reconciliation.py`
  `resolve_occurrence_proposal`: `reject` now commits a person-scoped
  `mark_occurrence(did_not_happen)` through
  `commit_occurrence_operation` before recording `state='rejected'` —
  canonical state no longer strands at `planned`. Person-scoped: only the
  rejecting viewer's participation row moves; shared `event_state` and
  other participants are untouched. (Deviation from the audit's "2-line"
  estimate: a raw column write would have bypassed the operation ledger,
  so the fix routes through the canonical command — ~20 lines.)
  Downstream consumers verified: attendance-affinity seeding and
  Places confirmed-encounters already honor `did_not_happen`.

### Scenario scores (final run, seeded `vesper_life_refind` DB)

All seven scenarios: **16/16, zero hard failures, target/truth/authority
all 2** — gate is ≥13/16.

| Scenario | Total | Hard failures |
| --- | --- | --- |
| Q01 ferry booked-not-taken | 16/16 | none |
| Q05 which train got us to Rome | 16/16 | none |
| Q08 tickets sent during the trip | 16/16 | none |
| Q20 museum ticket never used | 16/16 | none |
| Q21 Tuesday plan in Rome | 16/16 | none |
| Q22 booked places we skipped | 16/16 | none |
| Q23 did I go to that museum | 16/16 | none |

Q23's correction loop verified end-to-end through the REAL resolution
path: pre-correction envelope answers `unknown` / `occurred="no_evidence"`
(never a confident yes from possession); rejecting the pending proposal via
`resolve_occurrence_proposal` writes participation `did_not_happen`; the
rerun answers `missed` / `occurred="did_not_happen"`. Rerun-deterministic
(the runner rotates the pending proposal per run).

Honest caveat on the 2s: repair/continue/orientation score the envelope's
structural affordances (the slice emits fixed narrow operations and
advise-only destinations), so those dimensions certify contract presence at
fixture scale, not interaction quality — that is the mobile half's job.

Runner invocation (documented in the runner module):

```
createdb -U vesper vesper_life_refind
POSTGRES_DB=vesper_life_refind PYTHONPATH=. alembic upgrade head
POSTGRES_DB=vesper_life_refind AI_MODE=replay PYTHONPATH=. \
  python -m tools.eval.cli run --config tools/eval/configs/life_refinding/<scenario>.yaml
```

### Verification

- Offline suites: `tests/life/` (new, 20 tests), `tests/eval/` (955 incl.
  new check tests), `tests/dogfood/` (532) — all green.
- Postgres: `tests/scenarios/test_outcome_closure.py` green against the
  seeded DB (reject change does not regress the closure flow).
- Config lint `scripts/check_eval_configs.py`: 0 errors (7 pre-existing
  concierge warnings untouched). `python -m tools.eval.cli lint --agent
  life_refinding`: clean. Manifest validation + registry gate: clean.
- `mypy backend/life backend/core/models/life_refind.py
  backend/api/routes/life_refind.py backend/core/db/occurrence_reconciliation.py`:
  clean. `ruff check`/`format` on all new/touched files: clean.
- Import-boundary gates (`check_imports.py`, `check_lazy_imports.py`):
  clean. Feature-coverage guard: `backend/life` covered; the three
  pre-existing uncovered dirs (`application`, `domains`,
  `lived_experience`) are unchanged from the pre-session baseline.
- No eval-data fixture rewrites occurred (`git status` audited after runs).

### Pending (not this slice)

- **Mobile** (§6 item 3): truth chips + one Around-this row in
  `UniversalSearchOverlay` consuming `POST /api/life/refind`; type sync via
  `./scripts/sync-types.sh` (openapi snapshot deliberately NOT refreshed —
  known drift hazard).
- **Client `query_hash` removal** (§6 item 4): `travel-app/utils/
  universalSearchTelemetry.ts` still computes/sends the hash; server-side
  scrub from the safety batch already drops it durably.
- Baseline promotion + CI replay branches for the new agent
  (`cli.py` promote patterns, `core/baseline_integrity.py`,
  `core/replay.py`, a ci.yml step) — deferred until scores should ratchet.

### Spec deviations (with reasons)

1. Audit §5.2 named the lint at `tools/eval/scripts/check_eval_configs.py`
   — the real path is `scripts/check_eval_configs.py` (plus
   `tools.eval.cli lint`); both run clean.
2. Occurrence truth is seeded via the new `occurrence_marks` collection
   through the canonical `mark_occurrence` command rather than authored
   `event_state`/`status` on blocks — the replay compiler deliberately
   fails closed on any non-`planned`/non-`tentative` birth, and the
   command lane keeps the operation ledger truthful.
3. Fixture blocks cannot carry `commitment_state='booked'` pre-birth
   (compiler vocabulary), so "booked" is evidenced by `booking_sessions`/
   `booking_offers` rows — consistent with the envelope's rule that
   `used_state` derives from evidence, not assertion.
4. Envelope deltas vs the §4 sketch: field named `continues` (reserved
   word), `governed_answer` sits at envelope level for GA forms (results
   still carry full truth/sources/repair), and `session_ref`/
   `membership_epoch`/`safety_overlays` are omitted — mine-scope,
   single-viewer slice; they enter with the Together/shield work.
5. The telemetry oracle audits `user_events` (the §2.7 risk surface) plus
   the envelope retention invariant; a whole-database diff was judged out
   of proportion for the deterministic phase.
6. Two counted-boundary test literals were bumped for the new manifests
   (`tests/dogfood/test_itinerary_seed_replay.py`: 15→17 itineraries,
   109→118 blocks) and `canonical-personas.json` regenerated
   (source_hash only; the travel-app mirror got the same one-line change).

### Mobile half — 2026-08-31

Round 4 mobile slice (audit §6 items 3–4), travel-app repo. Additive only;
nothing existing was restyled or re-behaved.

**Built (files):**

- `types/lifeRefind.ts` — NEW. Hand-written mirror of the
  `life-refind-result.v1` envelope + request
  (`travel-agent/backend/core/models/life_refind.py`,
  `backend/api/routes/life_refind.py`). Deliberately NOT generated from the
  OpenAPI snapshot (known drift hazard, per this build record and the
  standing memory); follows the `utils/api/universalSearch.ts`
  manual-mirror convention, decision noted in the file header.
- `utils/lifeRefindFlag.ts` — NEW. `EXPO_PUBLIC_LIFE_REFIND_LANE`, default
  OFF, additionally fenced to dev/internal builds (the `fourRootShell.ts`
  dark-lane convention). Enable:
  `EXPO_PUBLIC_LIFE_REFIND_LANE=true` in a dev or internal build.
- `utils/lifeRefindPresentation.ts` — NEW. Pure truth-label mapping:
  primary chip Planned / In progress / Happened / "Didn't happen" /
  "No evidence either way" (sentinels in `time_roles.occurred` win, then
  `truth.occurrence_state`), plus a second "Booked, unused" chip when any
  source's `used_state='unused'`. no_evidence differs from did_not_happen
  in words, tone AND Badge variant; unit-tested as an invariant.
- `components/search/LifeRefindLane.tsx` — NEW. "From your life" lane:
  target-first `UtilityRow` (identity title leading, built on the
  `ui/rows` bones — the row ratchet enforces this), truth chips via the
  registered `Badge` primitive (no new design system), why-matched as one
  quiet caption from the machine cues, ONE Around-this block (≤3 rows),
  collapsed by default, expanded only on tap; display-only rows
  (envelope `continues` are advise_only in this slice). Renders after the
  existing grouped lanes; quiet (renders nothing) on loading/error/empty.
- `hooks/useLifeRefind.ts` — NEW debounced hook (mirrors
  `useUniversalSearch`); `utils/queryKeys.ts` +`lifeRefind` key.
- `utils/api/interface.ts` / `http.ts` — `lifeRefind()` →
  `POST /api/life/refind`; `utils/api/mock/discover.ts` — small fixture
  impl so mock/persona builds render the lane.
- `components/search/UniversalSearchOverlay.tsx` — lane mounted behind
  `LIFE_REFIND_LANE_ENABLED && hasQuery`; no other overlay change.
- `utils/universalSearchTelemetry.ts` — `query_hash` emission REMOVED
  (client now sends `query_len` only; §2.7 rationale left in a comment).
  Repo-wide grep confirms no other `query_hash` emitter remains.
- Tests: `__tests__/utils/lifeRefindPresentation.test.ts` (NEW — the two
  truth invariants + cue line + around clamp),
  `__tests__/components/LifeRefindLane.test.tsx` (NEW — chips render,
  unused item never hidden, no-evidence ≠ didn't-happen, around-this
  collapsed→expand), `__tests__/utils/universalSearchTelemetry.test.ts`
  (updated: asserts query_hash is ABSENT).

**Verified:** `npx tsc --noEmit` clean; new/touched files eslint-clean;
targeted jest suites green (63 tests across telemetry/presentation/lane/
overlay/hook + 28 across routing/recents/routes); rowRatchetContract no
longer flags the lane after the UtilityRow refactor; API-boundary gate
clean; catalog lifecycle gate passes. No component registered → no
`component-registry.json` / `Components.md` change.

**Pre-existing failures NOT from this slice** (verified by file lists —
none reference these changes; all trace to committed code or the
concurrent session's uncommitted Life* portfolio work):
`components:catalog:check` (MediaPlate/RestClose/RouteStrip unregistered),
rowRatchet (LifeAnchorRow/LifeEpisodeRow), 13 other conventions suites,
and the test-typecheck ratchet (477 vs baseline 406 — zero errors in this
slice's files).

**Deviations from spec, with reasons:** (1) Around-this rows are
display-only (no `canonical_path` navigation) — the slice's continues are
advise_only and legacy-substrate paths aren't guaranteed routable; the
required interaction is the expansion, which is implemented. (2)
`governed_answer` is not yet rendered — the supporting targets appear as
full result rows per the GA contract; a GA summary line is deferred to the
interaction-quality pass. (3) `atlasTelemetry.ts` still emits a separate
`raw_text_hash` on its own surface — out of this item's scope
(`query_hash` only), flagged here for a follow-up ruling.

### Atlas raw_text_hash — same-class fix — 2026-08-31

The mobile build flagged `utils/atlasTelemetry.ts` emitting a `stableHash`
of the user's raw Atlas query text into durable telemetry — the same
defect class as the universal-search `query_hash` (benchmark §8). Removed
under the same ruled precedent: `raw_text_hash` dropped (with an in-code
comment), `raw_text_length` and the structured `query_key` retained,
unused import cleaned. tsc + eslint clean. Uncommitted.
