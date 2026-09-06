---
doc_type: working
status: active
decision_status: proposed
owner: founder / Components and Plan / Integration
created: 2026-09-06
last_verified: 2026-09-06
expires: 2026-10-06
why_new: Gives the unresolved pre-Plan owner choice one reviewable proposal with commands and receiving-lane contracts instead of competing Home, Life and Capture substitutes.
supersedes: []
---

# Decision proposal: retain intention without requiring a Plan

## Status and decision requested

**Proposed, not adopted or implemented.** The founder authorized preparation
of this decision document, not a particular schema or a new runtime writer.
Accepted Contribution and Consequence rules remain in force. On approval,
promote the agreed choice into an immutable decision record and update the
owning contract before schema implementation. This proposal is the shared
review location for Integration D1, arrangement A0 and Life R6.

**Recommendation:** a narrowly typed, person-owned retained intention in the
existing experience-graph domain, with no required Plan, Occasion, place or
exact time. Life indexes it; Home and Places project eligible value; Chat and
direct controls invoke its owner commands. None of those surfaces stores an
independent copy of intent.

## Why the existing types are insufficient unchanged

The [graph models](../../travel-agent/backend/core/models/experience_graph.py)
already contain Plan, Commitment, ExperienceAnchor and OpeningCandidate.
A Plan can be open and untitled, but creating one merely to satisfy Keep
would still silently create a container. An anchor represents source-bound
evidence and currently lacks the revision contract needed here. A generated
OpeningCandidate's shown/dismissed/expiry lifecycle is not authored intent.
A Commitment overstates an optional desire. A generic memory observation does
not by itself provide prospective lifecycle, exact commands and adoption links.

Reuse existing custody, typed references, revision/idempotency conventions and
graph infrastructure. Prefer a small explicit owner over stretching one of
these meanings. Physical table names, endpoint names and generated schema are
not selected by this proposal. The implementation review must demonstrate why
any reused record can enforce the same semantics before avoiding a new table.

## Proposed semantic contract

Retain only deliberately authored intent, such as “Keep the bookstore in mind
for Saturday; leave the rest open.” Asking about the bookstore, reading an
Opening or importing a ticket does not create this record.

The owner must preserve:

- Stable identity, person owner, monotonic revision and authority basis.
- The authored intention, optional target/source refs and dependency lineage.
- Optional temporal wording, timezone when known and resolved bounds only when
  justified. “Sometime” is valid; do not invent a deadline.
- Optional Plan/Occasion association through an explicit relation, not a
  required parent or transfer of ownership.
- Separate custody, present eligibility and optional adoption state. A passed
  Saturday stops that cue; it does not prove completion, disinterest or deletion.
- Scoped correction/release and inspectable owner readback.

Semantic operations are retain, revise, release a cue/relation, release the
intention, and explicitly adopt/link through an existing Plan/Commitment owner.
These are not a mandate for five endpoints. Commands bind actor, target,
expected revision, exact effect and a retry-stable idempotency key. Later new
intent about the same place is not deduplicated solely by entity identity.

“Forget Saturday, keep the place” removes the temporal intent and preserves an
independently saved place. If no separate save exists, the explicit instruction
must invoke the Save owner and report its actual result; it cannot claim a
place was kept merely by deleting intent. Partial effects remain legible.

Adoption preserves lineage and records the receiving owner's actual reference
and revision. It does not automatically retire the original, invite anyone,
create a reservation or enroll another person. Revoking a source removes its
dependent use; independently authored intent survives only where it remains
meaningful and authorized without that source.

## Consumer promises and implementation ownership

| Owner / lane | Supplies or consumes | Must not infer |
| --- | --- | --- |
| Components and Plan | Owner commands, revisioned exact read, explicit adoption relation | Keep means Plan creation or attendance |
| Contribution and Capture | Resolved authored gesture and permitted source refs; invokes owner | Ask or model interpretation grants retention |
| Life | Derived indexing, refinding and prospective presentation | Life is the intent writer or every intent must fill an Ahead section |
| Home / Places | Eligible current value, exact destination and correction-aware return | Keeping starts a watch, push subscription or bespoke generation |
| Integration / live engine | Authorized reads and change/expiry dependencies | Intent alone grants location monitoring or autonomous action |

Private intent stays private. Sharing a suggestion, adopting it into common
material and accepting participation remain separate existing boundaries.
The user need not learn a new noun, fill a form or manage a queue.

## Acceptance and implementation sequence after adoption

1. Specify the minimal generated contract and exact reader/command path; review
   identity, concurrency, retention and migration before adding storage.
2. Implement owner transactions and authoritative readback, then downstream
   change delivery using the agreed cross-root contract.
3. Integrate Chat/direct Keep, Life retrieval and Home/Places projection against
   the same identities. No simulated success in a surface-owned store.
4. Verify Ask→Keep, repeated transport retry versus new intention, change of
   date, release-date/keep-place, adoption, concurrent correction, withdrawal
   and expired cues. Preserve unrelated sources and shared commitments.

Existing material is not retroactively classified from chat logs, saves,
anchors or generated content. Any migration needs its own explicit mapping.
Owner implementation does not authorize watches, public rollout or paid work.

## Tradeoff and approval boundary

This adds a small lifecycle-bearing domain concept. It avoids pseudo-Plans and
surface-local substitutes, at the cost of one owner/reader/repair integration.
Reject a universal item table or generalized document editor. Revisit if a
current governed owner can satisfy all the above without changing its meaning.

Approval must settle the owner choice and lifecycle; the subsequent schema
review settles persistence and commands. Until then, read-only exploration,
existing saves, Life's other owners and Home value remain executable. Do not
claim durable loose Keep is complete.

References: [arrangement handoff §4](lightweight-arrangements-implementation-handoff-2026-09-04.md#4-recommended-architecture-decisions-before-implementation),
[contribution contract](../systems/contribution-and-consequence.md),
[integration coordination](complete-system-integration-roadmap-2026-09-05.md#2-current-coordination-register--september-6).
