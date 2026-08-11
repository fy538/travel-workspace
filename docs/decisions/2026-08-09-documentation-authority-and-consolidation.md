---
doc_type: decision
status: accepted
owner: founder / product / engineering
created: 2026-08-09
decided: 2026-08-09
why_new: Records the authority boundaries required to consolidate the product canon without erasing the company's thesis evolution or creating new competing summaries.
supersedes: []
source_of_truth_for: [product-documentation-authority-boundaries]
---

# Decision: consolidate the product canon by authority, not by deletion

## Context

Vesper's company thesis evolved quickly from AI travel planning toward a
proactive, multiplayer, place-aware intelligence for real-world experiences.
The writing preserved that evolution, but the living canon accumulated the same
core argument in Product Thesis, Product Model, Product Vision & Scope, What We
Believe, architecture documents, and mobile doctrine. A new reader had to read
roughly 40,000 words to orient, while current implementation status remained
mixed with release intent in a dated working document.

The problem is not exact duplicate prose. It is overlapping authority: several
documents answer the same question with different levels of detail and decay.
Deleting the older reasoning would lose the journey that made the current thesis
credible; leaving it all living makes the current position hard to explain.

## Decision

The product documentation is consolidated around explicit ownership:

| Document | Sole authority |
|---|---|
| Product Thesis | Core promise, problem, wedge, moat, proof, and company direction |
| Product Model | Experience, Plan, Trip, Move; context objects; operating loop; settled hypotheses |
| Product Vision & Scope | Full product expression, horizons, and scope boundaries |
| What We Believe | Stable numbered principles used as decision anchors |
| Product Architecture Principles | Durable architecture invariants and rationale |
| Unified Context Graph | Current Trip-centered as-built context mapping and flow |
| Demo Journey Canon | Which story is demonstrated first and what it must communicate |
| M1 — Plan Repair | The single primary milestone, its four acts, and its exit criteria |
| Product Proof Spine | P01–P07 thesis proofs and their required initial evidence |
| Journey Evidence Model | Evidence layers, receipt contract, and promotion into the attestation index |
| V1 release contract | Machine-readable release intent and production posture |
| Current State | Generated comparison of release intent with executable evidence |
| Design Language | Mobile visual, interaction, accessibility, and receipt doctrine |
| Brand Identity | Name, personality, emotional register, brand voice, and marketing expression |

The canonical spine remains an authority registry, not a required cover-to-cover
reading list. The default company-orientation path becomes Product Thesis →
Product Model → Current State; the default *execution* path becomes M1 →
Product Proof Spine → Journey Evidence Model. Historical pre-consolidation
sources are preserved as non-authoritative snapshots with their originating
commit IDs.

**Amendment 2026-08-10.** The original ten-entry table omitted every document
that owns demo narrative and thesis evidence — two of which were created within
48 hours of this decision. The four rows added above close that gap. Any
document claiming `source_of_truth_for` must appear here; a document that owns
truth but is absent from this table is the failure mode this decision exists to
prevent.

Concepts are moved to their owner before redundant prose is removed. Stable
belief numbers and live anchor URLs are preserved during the first pass. Current
status must be generated from registries; canon must not manually claim what is
shipped.

## Consequences

The current thesis becomes faster to learn and harder to contradict. Supporting
documents may link to canon, but may not restate its entire argument. Product
Model stops serving as history, strategy memo, roadmap, IA brief, and business
plan simultaneously. Release scope moves out of `working/` and gains a
machine-readable contract.

Some useful narrative detail moves to historical snapshots or specialized
documents. This is intentional preservation, not repudiation: the travel-planner
origin remains part of the founder and product journey, while current documents
state which framing supersedes it.

## Revisit trigger

Supersede this decision if the company model changes enough that Experience,
Plan, Trip, and Move no longer organize the product, or if usage shows that the
three-document orientation path cannot explain the product and its current proof
without relying on unstated context.
