---
doc_type: decision
status: accepted
owner: founder / engineering
created: 2026-08-08
decided: 2026-08-08
why_new: Establish one cross-repo identity, resolution, correction, and provenance contract for geographic places and place-like entities.
supersedes: []
source_of_truth_for: [place-identity, entity-resolution, place-fact-provenance]
---

# Place identity and provenance

## Context

Vesper currently has strong identity inside individual domains but incompatible
references at their boundaries. Geographic places use integer ids and slug
aliases; venues, sites, and accommodations use independent integer spaces;
experiences use UUIDs; provider discovery uses namespaced strings; Saves uses a
typed string id; and planning has an internal `venue_<id>` / `site_<id>`
grammar. Atlas and a Map adapter still use bare ids in places where venue/site
collisions are possible.

This is a product-trust issue, not only a schema issue. A place must remain the
same object across discovery, saving, planning, Map, Atlas, booking, and future
correction. Facts attached to that object must retain their source, freshness,
confidence, and spatial precision. A private imported candidate must not become
another traveler's attributed or group-visible fact.

## Decision

### 1. Use typed internal references at every public boundary

The canonical application reference is an object:

```text
EntityRef {
  type: place | venue | site | accommodation | experience | custom
  id: string
}
```

`type` and `id` are one identity. A numeric id without its type is never a
valid cross-domain reference. Persistence may continue to use type-specific
foreign keys where that is the natural domain model; the public and shared-core
boundary is the typed reference.

The planning-only `venue_<id>` / `site_<id>` grammar may remain inside the
planning tool protocol. It must be parsed into `EntityRef` before persistence,
telemetry, or a public read model. `site:<id>`, `venue:<id>`, and bare numeric
compatibility forms are transitional inputs, not canonical outputs.

### 2. Keep provider identity separate from application identity

An external identity is:

```text
ExternalRef {
  provider: string
  external_id: string
}
```

Provider results may be shown without a database write. An explicit mutation
may resolve an `ExternalRef` to an `EntityRef`, but the provider id never
becomes the durable id of a Save, itinerary block, Atlas affinity, booking
attribution, or Map stop.

A globally verified `(provider, external_id)` resolves to one active canonical
entity. Unverified candidate mappings may be owner-scoped. Competing candidates
must be resolved before global promotion; uniqueness must not silently pick the
last writer.

### 3. Every identity-changing mutation returns a durable resolution receipt

Materialization, redirect following, and merge operations return:

```text
ResolutionReceipt {
  requested_ref: EntityRef | ExternalRef
  canonical_ref: EntityRef
  method: direct | materialized | provider_match | redirected | merged
  evidence: object
  resolved_at: timestamp
}
```

Mobile retries use a durable idempotency key and receive the same canonical
receipt. A `409`, a cache refetch, or a provider-wire id comparison is not an
adequate substitute because none proves which canonical entity won.

### 4. Redirects are canonical; physical row rewrites are an implementation detail

Resolution may redirect across entity kinds, including `site` to `venue`, when
the two rows represent the same real-world object. Same-table row consolidation
may additionally rewrite current foreign keys, but historical receipts and
source evidence retain their original reference and resolve through the
redirect ledger.

There is one canonical merge service. It records source, target, evidence,
actor, policy version, timestamp, and reversal. Feature code must not set
`merged_into_venue_id` / `merged_into_site_id` or bulk-rewrite dependent rows
directly.

Merge policy is domain-specific:

- Saves become one canonical save without escalating sharing consent.
- Affinity is recomputed from deduplicated evidence, never blindly summed.
- Itinerary block ids and history remain stable while the subject redirects.
- Conflicting verified booking or provider identities require review.
- Status, media, and fact observations retain their original provider and time.
- Search and vector projections tombstone the old active identity after the
  canonical projection is ready.

### 5. Facts retain provenance independently of the entity

Canonical entity columns remain fast read projections. Consequential facts also
carry a provenance record:

```text
FactProvenance {
  entity_ref: EntityRef
  field: string
  source: string
  source_record_id: string | null
  observed_at: timestamp | null
  expires_at: timestamp | null
  confidence: number | null
  precision: string | null
  status: candidate | verified | disputed | stale
}
```

The active value is selected deterministically from claims. A default entity
status is not evidence that every field has been verified. Raw prompts and
model chain-of-thought are not provenance.

Coordinates are governed by the same rule. Supported precision values are:

```text
exact | rooftop | entrance | interpolated | area | unknown
```

`area` and `unknown` geometry may establish broad scope but may not produce an
exact-looking pin or an enforceable route, travel-time, detour, or feasibility
claim. Existing geometry without evidence backfills to `unknown`, not `exact`.

### 6. Private provisional identity stays private

An owner-scoped provisional entity is eligible for matching only when the
reader is its owner, it has been explicitly shared into the relevant group, or
it has been promoted to a verified global entity. Nearby/fuzzy matching must
not attach one traveler to another traveler's private provisional row.

Named group attribution from a Save requires explicit, current sharing consent.
Private saves may influence group reasoning only through the privacy-safe group
composition boundary; the group sees a useful consequence, not the private
source or member identity.

Merging duplicate saves is conservative: the target remains private unless the
current canonical save has an explicit share grant. A merge never creates or
widens consent.

### 7. Atlas keeps raw evidence and adds canonical geography

Atlas retains the original place label and extraction source. It may add a
nullable canonical geographic `place` reference with match method and
confidence. Automatic resolution is allowed only for unambiguous,
high-confidence matches; otherwise the canonical reference remains null.

Clustering and future-trip joins prefer canonical place identity when present
and use normalized text only as a fallback. Correcting the canonical
association does not delete the original artifact, media, or raw label.

## Validation and rollout

Changes are additive first: dual-write, shadow-read, compare, backfill, then
switch consumers. Compatibility parsers emit telemetry and are removed only
after no production caller depends on them.

The protected journeys are J04, J06, J07, J08, J13, J19, J20, and J25-J28.
Each affected increment needs static trace, mock/client coverage, and a real
Postgres scenario. User-facing completion additionally requires on-device
evidence. Green backend tests alone do not certify the journey.

## Non-goals

- Replacing all entity tables with one universal entity table.
- Making model output an authority for identity, geometry, or freshness.
- Automatically merging ambiguous candidates.
- Exposing internal provider identifiers as product-facing ids.
- Mounting the built-dark trip save-suggestions route before its consent
  projection is proven.

## Consequences

- API changes that introduce `EntityRef` are contract-sensitive and require
  OpenAPI regeneration and frontend parity checks.
- Resolution, merge, and provenance require migrations and backfills.
- Existing feature-local identity strings remain temporarily readable but stop
  being emitted from shared contracts.
- Place identity becomes a shared substrate whose correction propagates to
  Plan, Map, Places, Atlas, booking, and search rather than a per-surface fix.

