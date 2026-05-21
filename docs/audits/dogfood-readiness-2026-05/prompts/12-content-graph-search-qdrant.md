# Prompt 12 — Content Graph, Search, Qdrant/Postgres Drift

```text
You are a Cursor Cloud agent auditing Travel Workspace for dogfood readiness.

Use the common rules in:
docs/audits/dogfood-readiness-2026-05/prompts/00-common-instructions.md

Area:
Location/content graph, search/retrieval, Qdrant/Postgres consistency, city seeding pipeline.

Output:
docs/audits/dogfood-readiness-2026-05/areas/12-content-graph-search-qdrant.md

Product promise:
The concierge and discovery surfaces should retrieve grounded, place-aware recommendations from the content graph without empty results caused by drift, type mismatch, stale embeddings, or thin coverage.

Inspect:
- Travel Agent places/content import pipeline, dossier import, seed_place scripts, Qdrant clients, vector payload builders, filters.
- Search pipeline, hybrid retrieval, fan-out search, venue/site/accommodation/experience payload consistency.
- Travel App Discover, For This Trip, place/angle/venue detail error states.

Start with:
- Travel Agent/docs/product/Content as Infrastructure.md
- Travel Agent/docs/architecture/Content Strategy and Architecture.md
- Travel Agent/docs/architecture/Location Context Model Data Architecture.md
- Travel Agent/docs/operations/Content Research Pipeline.md
- Travel Agent/docs/operations/Vector Store Operations.md
- Travel Agent/docs/operations/Content Pipeline Audit.md

Audit questions:
1. Are Postgres IDs/types and Qdrant payload IDs/types consistent across entity types?
2. Do filters handle nulls, bools, ranges, city slugs, parent place hierarchy, and accents consistently?
3. Can transient embedding or import failures wipe valid data or leave dirty rows unmarked?
4. Do search tools explain empty results without hallucinating?
5. Are seeded content files importable and deduped?
6. Does app UI surface content gaps with retry/empty states instead of blank rails?
7. Are retrieval evals covering the current city set and high-risk filters?

Run if cheap:
- targeted retrieval/vector tests
- content pipeline static checks
- make contract-check

Deliver:
Prioritize failures that make Lisbon or other dogfood cities feel empty, generic, or hallucinated.
```

