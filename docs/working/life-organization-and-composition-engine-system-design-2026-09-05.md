---
doc_type: working
status: active
owner: founder / Life engineering / product / cross-repository architecture
created: 2026-09-05
last_verified: 2026-09-05
expires: 2026-10-05
why_new: Converts the Life requirements, AI/ML research, and later manual-authorship direction into evolving examples, engineering decisions, contracts, evaluation cases, and implementation units within the existing Life replacement roadmap.
source_of_truth_for: []
supersedes: []
depends_on:
  - ../contracts/life-v1-experience.md
  - ../systems/contribution-and-consequence.md
  - life-complete-system-and-atlas-replacement-roadmap-2026-09-05.md
  - life-unfolding-decision-docket-2026-09-04.md
  - ../../travel-agent/docs/product/Product%20Model.md
  - ../../travel-agent/docs/product/Vesper%20Editorial%20and%20Content%20Canon.md
  - ../../travel-agent/docs/product/Vesper%20Expression%2C%20Medium%2C%20and%20Projection%20Canon.md
---

# Life Organization and Composition Engine — System Design

## 1. Outcome, scope, and reading order

**Life should make the record useful without filing work, remain recognizable
as new material arrives, and let people later make something of their own from
what it holds.**

The next engineering problem is not selecting a memory framework. It is joining
source custody, organization, retrieval, synthesis, human authorship, and repair
into one dependable experience. The system must work for an ordinary week as
well as a rich journey, and for plural shared perspectives as well as a private
record. It must not require a new trip, ongoing capture, or a completed story.

This document specifies the proposed engineering baseline. It does not claim
implementation, approve migrations or model calls, or redefine product canon.
The [existing roadmap](life-complete-system-and-atlas-replacement-roadmap-2026-09-05.md)
still owns package sequence and completion; this is its detailed design for
R1/R2 and the organization-bearing portions of R3–R7. Execution receipts stay
in [Life execution status](life-v1-execution-status-2026-09-01.md).

Read sections 2–4 for product behavior, 5–10 for engineering, and 11–13 for
evaluation, implementation, and unresolved choices. Section 14 records the
research patterns being borrowed and their limits.

### 1.1 Authority and phase boundaries

- The [Life experience contract](../contracts/life-v1-experience.md) owns the
  four lenses, finite root, full-record access, no-homework rule, and Returns.
- [Contribution and Consequence](../systems/contribution-and-consequence.md)
  owns admission, five independent authority axes, owner mutations, and repair.
- The [Editorial Canon](../../travel-agent/docs/product/Vesper%20Editorial%20and%20Content%20Canon.md)
  owns claim scope, human authorship, factual versus editorial value, and
  novelty. Section 3.1 already exempts attributed human contribution from the
  requirement to invent a new AI interpretation.
- The [Expression Canon](../../travel-agent/docs/product/Vesper%20Expression%2C%20Medium%2C%20and%20Projection%20Canon.md)
  owns medium semantics. Native code owns geometry and interaction; this design
  does not introduce server-authored screens or a universal card.
- The [Unfolding docket](life-unfolding-decision-docket-2026-09-04.md) contains
  pending prospective rulings. This document does not silently adopt AHEAD,
  settle the owner of an object-less intention, or create a default Plan.
- Manual-first composition is a **later phase**. Preserve its architectural
  requirements now; do not build its complete editor as a prerequisite for Life.

No new root, ambient chat scan, camera-roll mandate, identity profile, booking
system, graph database, or independently deployed memory microservice follows.

## 2. Current implementation: retain foundations, do not confuse them with the engine

Read-only inspection on September 5 covered the files below and the replacement
roadmap's implementation receipts. The workspace is concurrently active; this
is a scoped code baseline, not production certification or a full regression run.

| Existing seam | What exists | What this design still requires |
| --- | --- | --- |
| [Corpus assembly](../../travel-agent/backend/life_projection/corpus_query.py) and [root routes](../../travel-agent/backend/api/routes/root_projections.py) | Root/depth normalize owner projections and expose corpus revision/cursor semantics | Owner-backed incremental serving; complete typed time roles and source coverage |
| [Life table](../../travel-agent/backend/core/db/_tables/life.py) and [write contract](../../travel-agent/backend/life_projection/index_contract.py) | Viewer/version/record identity, time roles, references, lineage fields, and derived payload | Populated ownership/revision mappings, typed dependency edges, organization identities and maintenance |
| [Index projector](../../travel-agent/backend/life_projection/index_projector.py), [reader](../../travel-agent/backend/life_projection/index_records.py), [comparator](../../travel-agent/backend/life_projection/index_compare.py) | Pure all-lens batch construction, typed bounded reads, anchor lookup and parity helpers | Backfill, shadow runtime, runtime authorization, and serving cutover; parity helpers do not validate every grant or claim |
| [Index writer](../../travel-agent/backend/life_projection/index_writer.py) | Atomic batches and rejection of ordinary upserts over withdrawn/revoked rows | General revision ordering, stale-first-insert protection, and explicit authorized restoration |
| [Root compiler](../../travel-agent/backend/life_projection/compiler.py) | Deterministic priority ordering, lens sections, eight-entry cap, optional Return slot | Period/episode digest, differentiated lens grouping and whole-page usefulness |
| [Life refinding](../../travel-agent/backend/life/refind_sources.py) | Target-first retrieval over itinerary/booking evidence with negative occurrence truth | Whole-corpus source, episode, thread and saved-composition retrieval |
| [Canonical artifact projection](../../travel-agent/backend/core/models/canonical_artifact.py) | Viewer-safe facts, media, provenance, actions and owner handles | A saved editable composition owner; this read model is explicitly not one |
| [Intake outbox](../../travel-agent/backend/core/db/intake_outbox.py) and [anchor worker](../../travel-agent/backend/workers/intake_anchor_jobs.py) | Leased events with a single publication acknowledgement; graph bridge receipt before ack | A durable downstream delivery path, not a competing Life consumer of those same events |
| [Legacy clustering](../../travel-agent/backend/atlas/clustering.py) and [composition engine](../../travel-agent/backend/composition/FEATURE.md) | Photo-candidate validation and affinity-board assembly | Sparse multimodal grouping, source-aware interpretation and native Life anatomy |

Important implementation distinctions:

1. The index fields are available, but the snapshot adapter does not populate
   all time/lineage fields or derive trustworthy owner revisions by itself.
2. Refusing to overwrite a tombstone is not complete concurrency control. An
   old job can also attempt a first insert, or overwrite a newer non-revoked row.
3. The existing comparator proves selected row/order/lens/continuation parity,
   not permission, payload, authorship, or synthesis equivalence.
4. A legacy photo-count confidence tier is not confidence that something was
   lived or meaningful. Do not port its thresholds into Life organization.
5. The legacy board engine's assumption that a person's past is inherently
   trusted is not valid for attributed, late, disputed, or imported evidence.

Keep reusable readers, owner adapters, routes, tests and native primitives.
Do not rebuild them merely to introduce the word memory. Audit and replace
legacy assumptions at their actual boundaries.

## 3. The decisions this design makes

| ID | Recommended baseline | Reason and rejected alternative |
| --- | --- | --- |
| D1 | Existing domains retain source, occurrence, Plan, Occasion and claim authority; Life owns derived organization and reads | A universal Memory/Experience owner would duplicate truth and correction |
| D2 | One item can have several typed relationships, but a default human-readable containment path | One exclusive cluster cannot express a dish inside a dinner, at a place, and in a cooking thread |
| D3 | Explicit links and compatible time/place evidence precede semantic grouping | Embedding similarity is a candidate signal, not evidence of the same event |
| D4 | Unplaced retained material is a valid result | Forced grouping creates false history and filing obligations |
| D5 | Stable identity, user controls and accepted relationship decisions survive rebuilds | Hashing the current member set or regenerating labels must not recreate every object |
| D6 | Immediate safety invalidation; asynchronous bounded enrichment | Slow models must not block browsing or let revoked evidence remain visible |
| D7 | Record organization, synthesis and human composition have distinct revision behavior | New evidence should not silently rewrite a chosen keepsake |
| D8 | Deterministic grouping/selection baseline, bounded model assistance, explicit fallbacks | No custom training or framework adoption before a measured need |
| D9 | Four lenses share authority and identities, not identical grouping/ranking | A common corpus is not four copies of the same list |
| D10 | Attributed human expression and factual records do not pass the AI novelty gate | Maintenance effort is avoidable; voluntary creative effort can itself deliver value |
| D11 | Generation and present-delivery allocation are separate | Finishing a draft does not give it a Home or Life slot |
| D12 | Retained composition structure is renderer-neutral, with native presentation | Do not revive the legacy server-selected visual-slot model or add arbitrary generated UI |

These are engineering recommendations for the current program, not evidence
that numeric thresholds, schemas, or future authoring UX have been validated.

## 4. Six evolving experience specifications

The following are **constructed evaluation scenarios**, informed by the founder's
Europe/NYC stories and existing fixture worlds. Added names, sources, dates and
transitions are test inputs, not recovered facts about the founder. A supplied
item is durable only when its fixture explicitly grants retention.

For each transition assert source custody, eligible relationships, stable
identity, visible output, forbidden output, and affected dependencies. These
specifications should become executable replay cases before model tuning.

### W1 — A rich Europe journey, assembled gradually

Initial state: an existing journey/Trip handle, an explicitly supplied travel
window beginning August 14, retained flight/train/ferry tickets, selected photos,
and separately authored visit statements. Tickets alone establish arrangements.

| Step | Change | Expected record and visible value | What must remain stable or absent |
| --- | --- | --- | --- |
| W1.1 | Initial sources admitted with journey context | One journey door with nested source-backed segments; originals available immediately; intended and supported actual movement distinguished | No invented boarding, meals consumed, overnight stays or filled route gaps |
| W1.2 | Older Sorrento photos imported after return | Place them by supported capture/occurrence context, not today's import time; enrich the relevant nested segment | Journey ID, authored title, unrelated Rome segment and reader anchor remain stable |
| W1.3 | A photo derivative and duplicate ticket arrive | Record source lineage; deduplicate display of equivalent evidence within the permitted scope | No extra visit, independent witness, or increased confidence from the derivative |
| W1.4 | The person reports taking a train instead of one booked ferry | Retain the unused ferry ticket; update the occurrence relation and transport reconstruction | Independently supported later hotel evidence survives; old ferry claim cannot return on reimport |
| W1.5 | A reconstruction earns admission | A compact intended-versus-supported-actual sequence supplies useful structure; dossier opens all sources | No psychological interpretation; sparse legs remain gaps; no reflection prompt |

Lens effect: Time shows journey/segments; Places accumulates supported relations
without equating kept tickets with visits; People shows only authorized shared
material; Threads need separate supported continuity. A journey can cross month
boundaries without becoming two journeys; periods reference the same identity.

### W2 — An ordinary NYC week, without a major occasion

Initial state: a small existing local record, two explicitly reported outings,
a retained restaurant note, and an undated article. No active Trip is required.

| Step | Change | Expected record and visible value | What must remain stable or absent |
| --- | --- | --- | --- |
| W2.1 | A few independent local items arrive | A factual local period with supported episode doors; the undated article remains in custody/search | No invented week theme or demand to supply more material |
| W2.2 | A second visit to the same cafe is explicitly reported | A second occurrence linked to the same Place; its relationship dossier can show both | Do not merge two mornings into one event or infer a ritual, preference or companion |
| W2.3 | Nothing new arrives for several days | The record remains recognizable and useful for refinding | No streak, empty task, routine rewrite, or prompt to finish the week |
| W2.4 | An old Italy source is imported | Update its historical context and custody; leave this week's chronology intact | Dense travel evidence does not take ownership of the current week or Home |
| W2.5 | A relevant current opportunity becomes available | Home/Places may use eligible prior context with fresh world evidence; Life preserves the supporting relation | No promise that the memory engine alone verifies hours, availability or live feasibility |

Ordinary value can be finding the restaurant note or recognizing the week's
shape. It need not be an AI insight. Do not manufacture an episode merely to
fill the four-to-five-block rich-root target; thin states are legitimate.

### W3 — A pasta observation becomes reusable understanding

Initial state: a retained source-bound observation about a dish in Sorrento,
with its photo and an existing conversation/episode relation. No global food
preference or permanent project has been authorized.

| Step | Change | Expected record and visible value | What must remain stable or absent |
| --- | --- | --- | --- |
| W3.1 | First observation admitted | Nest it under the relevant episode or question; preserve the person's wording | A single observation does not become a cross-time thread |
| W3.2 | Weeks later, the person keeps a cooking attempt and explicitly connects it to that dish | Two distinct contexts gain an evidenced continuity relation; a modest thread door can be justified | NYC cooking remains its own episode; no task list or inferred new identity |
| W3.3 | A recipe and explanation are retrieved for the current Ask | Answer immediately; persist only material separately admitted under the contribution contract | Query text and transient sources are not silently added to Life |
| W3.4 | A permitted explanation contributes a mechanism beyond the person's note | Show the distinction with sources, limits and reusable cooking guidance; use comparison/evidence if clearer than prose | Do not repeat “you noticed the pasta was different” as new value |
| W3.5 | The person corrects the proposed mechanism | Supersede that interpretation and repair dependent outputs; retain the original observation and attempt | Rejecting an explanation does not erase the episode or human meaning |

If the later connection is only model-proposed, require the evidence and scope
gate in section 6; no user-facing approval queue. Insufficient support means
retain the separate records, not interrogate the person.

### W4 — Shared dinner, plural perspectives, later withdrawal

Initial state: a real Occasion handle with scoped participation; Maya contributes
a dish photo for that Occasion; the viewer contributes a separate note. Private
messages and other participants' personal meanings are outside shared scope.

| Step | Change | Expected record and visible value | What must remain stable or absent |
| --- | --- | --- | --- |
| W4.1 | Occasion and contributions become available | One bounded shared core plus visibly attributed contribution lanes | Named person or photographed face is not proof of participation |
| W4.2 | The viewer adds a private reflection | It appears only in that viewer's permitted private read | No fictional group voice, shared preference, or intimacy ranking |
| W4.3 | An authorized composition juxtaposes perspectives | Each perspective remains attributable; the juxtaposition must add value if Vesper presents it as synthesis | No widening audience because both sources are individually accessible to the viewer |
| W4.4 | Maya withdraws her contribution while synthesis runs | Block dependent serving and publication, invalidate media/excerpts/derived claims, and rebuild from eligible evidence | Source removal cannot be delayed until the model job completes |
| W4.5 | The viewer later revisits the dinner | Their independent note and supported shared core remain; unavailable material is omitted or boundedly explained | Do not delete independent history, reveal the withdrawn payload in a tooltip, or restore it from a saved draft |

People is a lens into shared records, not a computed relationship dossier.
The Occasion owner keeps participation and arrangement authority. Life owns
neither invitation acceptance nor a universal narrative of the gathering.

### W5 — Ambiguous evidence and correction across time

Initial state: a retained museum ticket, an undated screenshot of that museum,
and a friend's separately scoped photo. There is no supported attendance claim.

| Step | Change | Expected record and visible value | What must remain stable or absent |
| --- | --- | --- | --- |
| W5.1 | Ticket admitted | Search can find the exact ticket; scheduled date is labeled as planned, not occurred | No visit count, attended episode or invented screenshot date |
| W5.2 | The person says they did not go | An attributed negative occurrence claim is owner-accepted; ticket stays findable as unused | Unknown and explicitly did-not-happen remain different |
| W5.3 | Old extraction retries after the correction | Ignore the superseded attendance inference; current owner state wins | Arrival time is not authority; revision strings are not compared lexicographically |
| W5.4 | Place identity is corrected | Repair place associations, counts, search, maps and dependent synthesis | Independent items at the original Place stay there |
| W5.5 | Full rebuild and event replay run in different orders | Equivalent eligible facts, corrected relationships, stable links and controls result | No stale first insert, resurrected claim, or count inflation |

An unresolved retained source is a complete custody outcome, not a processing
task for the user. Chronology may expose an undated group rather than assert
false precision. A clarifying question is warranted only when a chosen current
consequence depends on the answer.

### W6 — Later manual composition over a changing Life record

Initial state: the person deliberately selects several photos, place notes and
recipes, spanning Italy and NYC, to make a small food guide. This phase is later
than the automatic organization baseline.

| Step | Change | Expected record and visible value | What must remain stable or absent |
| --- | --- | --- | --- |
| W6.1 | The person selects material and starts composing | A private authored draft records exact selections; manual ordering/captions work without AI | No new episode, merged trip, audience, or required AI transformation |
| W6.2 | They ask AI to shorten one section, preserving captions | A preview changes only the delegated content; protected blocks and decisions remain intact | No whole-document regeneration or inferred preference from a local edit |
| W6.3 | They save version 1 | Life can reopen that chosen version; other surfaces reference it | Root refresh and background regrouping do not rewrite it |
| W6.4 | Another relevant photo arrives | It may improve the automatic record; an explicit refresh can offer a scoped diff for a new draft | No unsolicited insertion into version 1 or repeated “finish your story” prompt |
| W6.5 | A source is corrected or withdrawn | Corrected facts get an honest validity treatment; unauthorized content stops serving even inside the saved version | Version stability does not authorize preserving disclosure; independent authored text is not silently rewritten |
| W6.6 | The person shares their chosen version | The composition owner checks the actual recipients, source reuse rights and current validity | Selecting material is not permission to publish; exports have explicit correction/revocation limits |

The user's chosen selection can be valuable without any new discovery. A title
such as “My favorite meals” is their expression, not Vesper's inferred verdict.
Generated factual additions still need support and attribution. This is
authorship, not a workaround for missing automatic organization.

## 5. System boundaries and proposed data contracts

### 5.1 One backend, several clear responsibilities

```text
Existing canonical owners + durable human controls
           │ authorized change + owner revision + policy state
           ▼
Owner adapters → derived corpus index → typed grouping/membership
           │                              │
           ├───────── exact sources ───────┤
           ▼                              ▼
     refinding/dossiers            stable lens digest
           │                              │
           └──── evidence bundle ──────────┘
                         │
               bounded synthesis proposals
                         │ validation + dependencies
                         ▼
                eligible generated version
                         │
           shared allocation / native projection

Later: selected sources or generated version → authored draft → kept version
       User choices do not mutate the source record through this path.
```

These are logical responsibilities in the existing backend and worker system,
not seven services. Keep canonical owner contracts in shared core; implement
Life organization policy as a domain module, and keep HTTP routes thin. Search
and other agents consume core contracts rather than importing another agent's
private runtime. Reuse current Postgres, vector and model-call infrastructure.

### 5.2 Logical types to define before migrations

Names below are proposed internal contracts, not existing API types. Each
field must map to an existing owner field or an explicitly reviewed addition.

| Contract | Minimum information | Authority/persistence |
| --- | --- | --- |
| `OwnerEvidenceRef` | Typed owner/record ID, exact revision, source locator, author, purpose/grant references, time roles, truth state | Reference to owner truth; never an authority grant itself |
| `LifeGroup` | Stable ID, kind, optional canonical anchor, display-title basis, supported time extent, member references, organization revision | Viewer-scoped derived organization; a group is not a Plan or attendance claim |
| `LifeMembership` | Member/group IDs, typed relation, source basis, authored/derived origin, validity, rejected/superseded state | Explicit corrections persist separately; accepted derived decisions are reproducible inputs |
| `LifeControl` | Actor, target relation/field, rename/detach/suppress/release command, scope, revision and Undo basis | Durable human instruction, not model output; use existing owner controls where applicable |
| `DependencyManifest` | Typed dependency ID and revision, source span, policy revision, semantic role, derived consumer, fingerprint | Reverse-indexable lineage for repair; JSON blobs alone are insufficient for efficient fan-out |
| `LifeSynthesisSpec` | Job/operation, bounded claim set, supporting references, known/supplied context, exposure basis, generation/policy version | Replaceable generated work under permitted retention; no independent factual authority |
| `AuthoredCompositionSpec` | Creator, selected references, stable block IDs, section order, captions, exclusions/locks, base version, purpose/audience | Later dedicated composition custody; separate from source and occurrence ownership |
| `LifeProjectionRead` | Record/group IDs, count units, coverage, eligible version, source availability, stable cursor/anchor, allowed actions | Rebuildable viewer-relative read; native client determines geometry |

Do not put all raw chats, source media, graph facts and prose into
`life_corpus_entries.payload`. That table remains the serving projection.
Large member/source lists need paged relation readers; current bounded
`source_refs` fields are previews, not an exhaustive dependency inventory.

### 5.3 Persistence choices

Recommended implementation direction:

1. Reuse `life_corpus_entries` for normalized serving records. Add owner adapter
   coverage rather than inventing a second corpus.
2. Store derived groups, memberships and dependency edges relationally in
   Postgres, indexed by viewer, member, owner and consumer. Final table names
   and consolidation into existing tables belong to the migration review.
3. Keep an identity/lineage registry and durable human controls independent of
   disposable summaries. A private Life-only grouping instruction may need a
   narrow control repository; it must not mutate another owner's Occasion.
4. Retain accepted model-assisted relation decisions with evidence/policy/model
   versions where their reuse is authorized. They are derived proposals, not
   self-validating claims or independent witnesses.
5. Treat embeddings, search documents, summaries and generated variants as
   derivatives with deletion and rebuild registration. No new graph database
   or opaque managed-memory store is selected.
6. Do not persist manually authored drafts in `CanonicalArtifactProjectionV1`.
   It is a read contract. Select/reuse the composition custody owner in R7
   before any saved-composition API or schema migration.

### 5.4 Time, authority, counting and identity

Time roles remain distinct: scheduled/planned, occurred interval, captured,
authored, imported, generated, and represented-at. Preserve timezone, precision,
uncertainty and source basis. An ordering fallback is internal and must not
become an asserted event date. Future material cannot count as lived because
its scheduled date passed.

Authority is claim- and purpose-specific, not a global source ranking. A
provider owns booking status; a person may author that they did not attend.
These can coexist. An owner-accepted correction to a particular assertion
supersedes its earlier derivation. Model confidence and later ingestion do not
override it. Conflicting participant perspectives remain attributed/plural.

Counts name their unit: retained originals, distinct occurrences, Places,
episodes, or kept compositions. One source can support several relations
without creating several visits. Deduplication is scoped to lawful access;
matching private hashes must not reveal another person's material.

Canonical-owner groups derive stable identity from the owner's typed handle.
Derived episodes use an identity registry, not their current label, member-set
hash or model summary. Persist identity reconciliation and redirect decisions.
Calendar period IDs include the calendar/timezone policy, separate from their
rendered label. No global mutable display rank becomes part of identity.

## 6. Organization baseline and model boundary

### 6.1 Distinguish the relations before computing similarity

| Relation | What it says | What it must not imply |
| --- | --- | --- |
| Same source / derivative | Two files or excerpts share evidence lineage | Two independent observations |
| Supports occurrence | A source or admitted claim supports what happened | Purchase, possession or mention alone proves presence |
| Belongs to episode | Material is contextual evidence within a bounded episode | Every source records a separate event |
| Related Place / person | Canonical entity association or authorized attribution | Visit, participation, liking or intimacy |
| Continues attention | Supported relation across contexts | A project, obligation or permanent preference |
| Useful analogy / contrast | A bounded explanatory relation | Same event, same mechanism without verification, or identity |
| Selected for composition | A human or delegated choice of material | Canonical episode membership or wider sharing rights |

A system can propose a useful contrast between distant cliffs without merging
their Places or creating a durable “cliff enthusiast” profile.

### 6.2 Baseline algorithm

1. **Read authorized deltas.** Resolve owner state, versions, controls and
   permitted evidence. A source used only for Ask never enters the durable
   candidate pool just because extraction completed.
2. **Normalize without strengthening truth.** Extract literal metadata and
   references; resolve entities through canonical services. Preserve uncertain
   or contradictory evidence instead of filling missing fields.
3. **Apply explicit containment and exclusions.** A named journey, Occasion,
   episode, or authored connection is the strongest local organizational cue,
   subject to authority. Detach/reject overrides are applied before proposals.
4. **Generate bounded candidates.** Use linked owner IDs, compatible event-time
   ranges, canonical place hierarchy and permitted contextual evidence. Exact
   links are never discarded because a semantic candidate cap was reached.
   Lexical/dense neighbors supplement, not replace, these paths.
5. **Classify the relationship.** Exact compatible cases use deterministic
   rules. Ambiguous or cross-context candidates may receive bounded model
   review returning a relation type, supporting source locators, contradictions,
   uncertainty and a no-link option. No arbitrary SQL or mutation plan.
6. **Admit through policy.** Accept only supported, in-scope relations. Defer or
   reject uncertain joins without a user queue. A shared Place and nearby date
   are not enough when evidence conflicts or different occasions are known.
7. **Reconcile identity and materialize.** Update affected memberships and
   group spans; preserve human titles and identity; emit versioned dependencies.
8. **Project separately.** Build stable lens reads; queue eligible synthesis
   only where the change can add value. Browsing never waits for that queue.

The model proposes relation evidence, not authority, custody, attendance,
participation, preference, spending, audience, or the end of an intention.

### 6.3 Grouping and granularity defaults

- Existing owner-bounded journeys and Occasions remain useful anchors, not
  prerequisites for every retained item.
- Derive a new episode only when there is a supported bounded context that
  gives useful containment; one source may remain a source door. Do not require
  a minimum number of photos or a multi-day trip.
- Use month/year periods as deterministic navigation scaffolding; local week
  sections may summarize ordinary records. Calendar boundaries do not split an
  event, and an event spanning periods keeps one identity with references.
- Preserve sub-episodes when they help refinding: a day/meal/transfer may be
  nested under a journey without becoming a Plan or a separate root-level card.
- Repeated visits to one Place remain distinct occurrences. Accumulated Place
  relations can include kept-not-visited, planned, occurred and authored notes,
  with explicit distinctions rather than one affinity score.
- A model-proposed thread needs at least two distinct evidence-bearing contexts
  plus a defensible continuity relation and appropriate inference scope.
  Two similar words, derivative sources, or repeated unanswered questions do
  not suffice. This is an initial conservative policy, not a scientific threshold.
- A person can deliberately name a thread or collection sooner; it stays
  human-authored, not presented as a system-discovered pattern. A later editor
  must not be gated by the automatic thread policy.

### 6.4 Stable updates, merges and splits

Adding evidence normally updates membership and a factual description, not
identity. A rename changes the rendered title, not the object. Harmless new
material should not reorder unaffected groups or reset a reader's position.

For a merge: prefer an existing canonical owner identity; otherwise retain an
established derived identity under a deterministic reconciliation rule and
record aliases. Never merge incompatible owner worlds or access scopes merely
to simplify display. Human grouping controls constrain the operation.

For a split: retain the old handle as a bounded resolution entry pointing to
the legitimate descendants. Preserve a unique canonical-anchored descendant
where one exists. Do not arbitrarily send every old link to the first child.
The client can open a small disambiguation view when no exact descendant is
recoverable. Never reveal private child titles through lineage.

Evaluation penalizes false merges more heavily than harmless separation. Exact
numeric thresholds and permissible churn are calibrated on section 11's cases;
they are not LLM self-reported probabilities.

## 7. Incremental maintenance, repair and rebuild

### 7.1 Chosen delivery pattern

Use a **durable downstream Life change journal/work queue** with independent
acknowledgement, implemented through existing worker/database conventions.
Do not let Life claim the same intake events that the normalization or graph
bridge worker must consume.

For a source/claim transition, the canonical owner's transaction (or the
existing bridge's committed downstream transaction) records the state change
and an idempotent Life change notification together. The existing upstream
event is acknowledged only after that durable handoff exists. If an owner
cannot participate in this transaction, explicitly design an owner outbox or
checkpointed reconciliation adapter; do not rely on a best-effort callback.

Source custody and graph admission are separate events. Source-only material
must become findable even when it never becomes an accepted graph anchor.
Every owner adapter declares event coverage, revisions, deletion and grant
change semantics; periodic reconciliation repairs missed delivery, not authority.

Proposed event information: event ID, owner kind/ID, owner revision or ordered
sequence, change kind, affected fields/relation IDs, policy revision, occurred
time if known, and cursor/checkpoint. Carry references rather than raw private
payload through logs or queue metrics.

### 7.2 Worker behavior and concurrency

1. Claim a leased bounded batch; load current owner state and policy.
2. Resolve affected viewers from current authorized projections in paged batches.
3. Re-read the relevant controls and dependency revisions.
4. Compute normalized rows and affected organization proposals.
5. Publish with compare-and-swap against the owner/control/authorization revisions
   read. Opaque revision strings require equality checks or owner-provided
   ordering; never lexical or import-time ordering.
6. Commit rows, dependency changes and downstream dirty markers atomically within
   the chosen transaction boundary; acknowledge only after durable completion.
7. If versions changed, discard/retry against fresh state. Preserve safe reads
   and let queued newer work coalesce; do not publish a stale draft first.

The publication guard must cover inserts as well as updates. Tombstone-only
guards cannot stop an old job inserting a never-materialized row after deletion.
Explicit restore requires current owner authority and a new authorization
generation; it is not achieved by clearing flags in an ordinary upsert.

Do expensive extraction/generation outside database transactions. At publication,
use a short transaction with owner/policy locks or a verified conditional write
that closes the check-to-write race; a Python check immediately before an
unconditional upsert is insufficient. Readers also require current owner/policy
eligibility, not only the index row's cached `audience` or `status`. A narrow
authorization-generation check can block stale derived reads while large
recipient/dependency fan-out finishes asynchronously. The owner adapter must
provide that check or fail closed; the index cannot manufacture it.

### 7.3 Different triggers, different work

| Trigger | Immediate behavior | Deferred work |
| --- | --- | --- |
| New admitted source | Original/receipt remains accessible through owner; expose index coverage honestly | Normalize, index, local grouping, optional synthesis |
| Late import or duplicate | Preserve time roles and lineage | Update affected historical groups, not all recent periods |
| Accepted correction | Block contradicted claims and dependent outputs; preserve still-valid originals | Recompute membership, counts, retrieval documents and generated versions |
| Delete or narrowed grant | Reauthorize reads; suppress dependent content/media immediately at the server boundary | Purge/rebuild derivatives and recipient-specific projections |
| Rename or detach | Apply control readback and preserve it against future inference | Reproject affected groups; invalidate only dependent descriptions |
| Suppress resurfacing | Remove from relevant delivery candidacy | Keep custody/refinding unless separately changed |
| World fact changes | Invalidate the affected current explanation/instrument | Recheck eligible Returns; do not rewrite historical occurrence |
| Page refresh | Read permitted stable state | No generation or re-clustering merely because GET happened |

### 7.4 Bounded work and failure posture

Candidate lookup, group membership, dependency fan-out and viewer fan-out all
need independent cursors. Never cap correctness work and mark it complete.
Partition large groups and resumably queue remaining work. Safety-invalid
derivatives stay blocked until dependencies are repaired; harmless enrichment
can continue serving the last valid version.

Initial experiment configuration: at most 50 semantic neighbor candidates per
changed source, one bounded relation-classification batch, and at most two hops
for optional associative retrieval. These are starting resource budgets, not
quality thresholds or shipped settings. Exact links and invalidation traverse
their full paged sets. Do not make model tokens proportional to lifetime history.

Coalesce repeated dirty notifications per object/version. Use bounded retries,
leases, dead-letter diagnostics and operator recovery. Never surface the worker
queue as a user's unfinished Life. Stop model work on quota exhaustion while
keeping deterministic custody, correction and read paths operational.

### 7.5 Rebuild and serving migration

Backfill from authorized owners plus durable human controls and the identity
registry into a separate projection version. Establish per-owner high-water
marks, page through history, then replay subsequent changes with the same
idempotent logic. A wall-clock timestamp is not a complete cross-owner snapshot.

Distinguish two tests:

- **Projection rebuild:** same owner/control state, identity registry and accepted
  proposal inputs yield equivalent facts, memberships and eligible reads.
- **Algorithm re-derivation:** a new model/policy can propose different links;
  compare material differences in shadow. It is not byte-identical replay and
  must not silently replace authored choices or established identity.

Raw sources alone cannot recreate an author's title, detach instruction or
saved composition. Those are durable inputs with their own retention policy.
Generated prose may vary when deliberately regenerated; support, authority and
protected edits must not. Cache/replay versioned outputs for exact regression.

Shadow compare old/new reads for identity, time, count unit, membership, payload,
sources, current authority, continuation and exact destination. Keep the existing
parity helpers, extending their scope rather than treating them as sufficient.
Cut over behind the existing rollout mechanism after owner coverage and race
tests pass. Rollback changes the reader version, never resurrects revoked data.

### 7.6 Honest limits for caches and exports

“Immediate withdrawal” means no further authorized server response may disclose
the material once the owner change is effective; it is not a promise to erase
pixels already seen or an exported file on another device. Online client caches
must react to owner invalidation and recheck on foreground/open. Shared sensitive
derivatives need short validity leases and an unavailable state when offline
authorization cannot be established. Expired signed media access cannot be
replaced with an ungoverned cached copy.

Define offline eligibility explicitly during reader integration. Exported copies
need an honest boundary; hosted shares can be revoked, downloaded copies cannot
be remotely guaranteed erased. The later authoring phase cannot bypass this.

### 7.7 Untrusted source content and retention

Text inside an imported article, ticket, image, transcript or friend's artifact
is evidence to interpret, not an instruction that can grant retention, change
audience, invoke tools or supersede a correction. Resolve commands from the
authenticated gesture/channel and canonical owner, never from embedded prose.
Model outputs are schema-validated proposals and cannot self-authorize writes.

Source spans, extracted text, thumbnails, embeddings, candidate explanations,
prompts and job caches all inherit applicable retention/deletion constraints.
Operational journals and telemetry retain only the minimum content-free
identifiers needed for recovery; a tombstone must not retain enough text to
reconstruct a deleted source. Do not retain whole prompts as a workaround for
source deletion. Add a malicious instruction inside W3's recipe or W5's document
to the replay variants; it must not widen scope or erase an accepted correction.

## 8. From organized evidence to a useful Life page

### 8.1 Four distinct lenses over the same record

| Lens | Organizes around | Default value | Avoid |
| --- | --- | --- | --- |
| Time | Supported periods, journeys, occasions and episodes | Recognize when things happened and recover nested evidence | Upload feed, invented life chapters, future dates treated as occurrence |
| Places | Canonical Place relationships and their distinct states | Revisit what is held, known, experienced or personally contributed there | “Visited” from a save; ranked taste profile; second nearby feed |
| Threads | Explicit or sufficiently supported continuity across contexts | Recover how a question, practice or idea developed | Topic extraction as a project or completion obligation |
| People | Viewer-authorized shared records and attributed material | Recover what was shared or lived together without merging meaning | Intimacy ranking, contact surveillance, inferred participation |

Each reader uses the same eligibility, source/control revisions and identity,
but can use different grouping and retrieval order. Root, full-record and
Everything kept counts must reconcile by declared unit, not forced equality
between source count and episode count.

### 8.2 Digest selection

Honor the current Life root anatomy: speaking header, finite digest, one
full-record door, optional Returns/Reflections/Windows, and custody access.
Use four-to-five meaningful blocks when the record supports them; thin states
remain thin. Preserve all four labeled lenses and accessible alternatives.

For Time, start with supported periods and stable nested episode previews.
For other lenses, use canonical associations and bounded supported groups.
Choose representative evidence by direct relevance, coverage, non-duplication,
source availability and explicit user choices, not photo volume or aesthetics
alone. A representative image is a lead example, not evidence of importance.

Prefer stable ordering and minimal change between reads. Digest selection can
omit an item without deleting it or hiding its full-record path. Track root
selection separately from group membership. Display no processing or evidence
quality score as a request for the user to improve their Life.

### 8.3 Dossiers and truthful depth

A group door opens a bounded dossier with identity, supported chronology,
planned-versus-occurred distinctions, people/attribution, nested evidence and
appropriate correction. Originals remain accessible independently. An exact
source search opens the source, not a generic dossier that happens to mention it.

Keep five doors distinct around one place: world entity, original source,
personal relationship record, current arrangement, and saved composition. Reuse
the existing object-page kernel and owner destinations; do not replace all of
them with a new Life mega-screen.

### 8.4 Synthesis and editorial admission

First producers: (a) reconstruction that makes fragmented chronology or
intended-versus-actual movement legible, and (b) a grounded cross-source
explanation or contrast. Design both against W1–W5; do not make one the universal
template. An attributed human contribution can be shown without generated prose.

Generation sequence:

1. Resolve authorized evidence and the present job.
2. Identify the proposed added value and check supplied/previously delivered
   claims separately from exposure history.
3. Retrieve missing support within purpose and budget, retaining source spans.
4. Generate a bounded claim set and a renderer-neutral expression proposal.
5. Validate support and uncertainty per claim; compute counts/quantities in
   code; reject identity overreach, parroting and unsupported analogies.
6. Recheck dependency/authority revisions at publication, then store an eligible
   replaceable version only under its retention policy.
7. Let shared allocation determine whether/where it appears. No slot entitlement.

For an analogy, require the shared mechanism, a material difference and a
bounded use. A superficial resemblance can remain a clearly labeled comparison
of evidence; it must not be sold as a causal explanation. Model-generated text
cannot become a new independent source for its own conclusion.

Factual summaries belong where they help. They need not pass novelty merely to
exist in a dossier. Proactive editorial Returns still need new substance and a
material trigger. Human-created selections are not subject to that same AI gate.

### 8.5 Cross-root circulation

Home consumes current-life value; Places consumes spatial/world value; Chat
receives or transforms with context; Life preserves record and reusable depth.
Transfer source/record/composition handles and revisions, not copied facts into
four private memories. Home/Places still require their own current-world checks.

Use the existing shared Return allocation policy over evidence/intent identity
and version. Equivalent candidates cannot race for independent delivery on GET.
When current value is allocated to Home/Places, Life yields that optional Return,
but keeps source/dossier/search access. A saved composition does not disappear
from custody just because its proactive delivery recedes.

## 9. Human correction and later authorship

### 9.1 Editing commands do different things

| Human action | Target owner/effect | Must not do |
| --- | --- | --- |
| “I did not go” | Occurrence/claim correction and causal repair | Delete the purchased ticket |
| “This belongs to that dinner” | Authorized membership correction | Change another person's participation or create an Occasion |
| Rename a Life grouping | Canonical owner's title where applicable, otherwise scoped Life display control | Change factual dates or infer personal meaning |
| Detach from an episode | Specific membership plus anti-rejoin control | Delete the original or unrelated memberships |
| Do not resurface this | Delivery suppression within stated scope | Remove custody or teach a global dislike |
| Release this interpretation | Invalidate the named derived relation/claim | Erase independently authored observations |
| Change my composition caption/order | Authored draft/version | Rewrite occurrence or other surfaces' canonical facts |
| Remove from composition | That selection/block | Delete the source from Life |
| Delete/withdraw original or share | Source/audience owner, with dependency repair | Preserve prohibited excerpts in a generated snapshot |

Natural language may resolve an exact bounded edit. Ask only if ambiguity changes
its scope or consequence. Direct controls and language use the same commands;
Undo uses the owner's valid inverse, not a guessed reconstruction of old truth.

### 9.2 Three entrances, one later authoring capability

- **Use these:** manually select materials and compose without AI.
- **Make something about this:** delegate a draft from a named scope.
- **Make my version:** branch from an existing generated or saved composition.

Begin with evidence, short authored text, ordered sections and place/sequence
references using existing renderers. The user can select, replace, reorder,
change a cover/title, caption and undo directly. Language handles broader
transformations over a selected scope. Do not require a video timeline editor,
infinite canvas, new tab, or a separate feature for every format.

### 9.3 Authored composition contract

Proposed logical shape, not a production payload:

```yaml
composition:
  identity: composition_handle
  version: immutable_version_handle
  based_on: optional_source_composition_version
  author: person_handle
  mode: authored_snapshot
  source_selection: [typed_source_ref_with_revision]
  sections:
    - id: stable_section_id
      blocks:
        - id: stable_block_id
          role: human_contribution
          content_ref: authored_caption_or_selected_source
          protected_fields: [wording, selection]
  order: [stable_section_id]
  excluded_sources: [typed_source_ref]
  dependencies: dependency_manifest_ref
  authority: current_owner_and_grant_refs
```

This is not a generic server-driven UI tree: blocks carry allowed semantic
content and references, not coordinates, colors, typography or executable code.
AI can propose patches to delegated fields; it cannot modify protected selections
or wording. Validate patches against the base version, show the material diff,
and require conflict resolution if that base changed. A lock never protects
unauthorized content from withdrawal.

Saving freezes the user's chosen version, not the validity of every fact. New
evidence can offer a new draft or explicit refresh. Material factual corrections
must prevent the old claim being presented as current truth: contextualize,
redact or make the affected block unavailable without silently rewriting the
person's words. Source/grant withdrawal blocks disclosure, including cached media,
captions or derived claims dependent on that access. Preserve independent authored
content under its own authority.

Default to saved snapshots. An explicitly live collection is a distinct later
mode with visible update behavior, not the default for personal keepsakes.
Sharing creates a separately governed projection; it does not widen the rights
on every selected source. Hosted-share withdrawal and file-export limits must
be stated plainly.

### 9.4 Required future canon alignment

Product Model §1.2 and Expression Canon §6.2 currently describe compositions as
Vesper-generated/assembled. Before shipping manual-first creation, extend that
wording to include deliberate human assembly with optional AI. Preserve the
same source, author, audience, version and correction distinctions. No new
universal object model or fifth product move is needed. The automatic Life
engine may proceed without opening this later editor to users.

## 10. Technical contracts and mobile integration

Recommended contract boundaries:

- Owner adapter: authorized bounded reads, exact revision, changed-since cursor,
  deletion/grant-change coverage and source/claim availability.
- Organization command: input owner/control versions, eligible candidates,
  accepted/rejected typed relations, identity reconciliation and affected groups.
- Synthesis command: job, bounded evidence, dependency versions, allowed claims,
  protected authored material and retention/cost policy.
- Serving read: viewer/lens/filter, corpus/group revision, count unit/quality,
  dependency validity, stable destination and cursor/anchor recovery.
- Human command: actor, exact target, base revision, operation, scope and
  authoritative readback. Different effects do not share a generic “update memory.”

These may be in-process interfaces first; do not add an HTTP endpoint for every
box. Preserve the current Life transport until a real contract change warrants
versioning. Backend models remain schema source; use the workspace type-sync
workflow for API changes, then update root/depth/search/dossier consumers together.

Cursor rules continue to bind viewer, lens, filters, ordering and corpus revision.
Prefer a conflict/restart around stable identity over silently skipping or
duplicating rows. Separate index coverage from a usable next cursor. New safety
restrictions override any older cursor or cached view. Group navigation must
preserve origin and stable row/block identity without replaying all prior pages.

Client integration should reuse [LifeRootV1Screen](../../travel-app/components/life/LifeRootV1Screen.tsx),
[reading-position storage](../../travel-app/utils/lifeReadingPositionStorage.ts),
[refinding](../../travel-app/components/search/LifeRefindLane.tsx), and existing
object readers. These are integration targets, not an instruction to redesign
Chat or Life visuals in this document. Detailed composition stays with the
dedicated design tools; behavior, data and accessible fallbacks are specified here.

## 11. Evaluation: decide with evolving records, not benchmark headlines

### 11.1 Fixture contract

Convert W1–W6 into deterministic event manifests with fixture-only IDs:

```yaml
scenario: W5
initial_owners: []
events:
  - id: W5.2
    actor: fixture_person
    owner_command: report_did_not_attend
    expected_base_revision: fixture_revision_1
expectations:
  custody: [ticket_remains]
  claims: [attendance_negative]
  forbidden: [visit_increment, stale_reimport_restores_attendance]
  stable_ids: [ticket_handle]
  repaired_consumers: [life, search, dossier, home, places, saved_derivatives]
```

The executable format should reference existing fixture owners and assertions;
it is not a new general workflow language. Do not upload real private artifacts
or call paid models during fixture construction without appropriate authority.

Run each event sequence normally, with duplicate delivery, delayed old events,
worker restart, partial owner outage, source deletion during synthesis, and
viewer/grant changes between query and publication. Include year/month/timezone
boundaries, ambiguous dates, two visits to the same place, and large sparse
authorized histories. W6 can remain a contract test until its phase is built.

### 11.2 Baselines and bounded experiments

| Experiment | Baseline | Addition to compare | Decision it informs |
| --- | --- | --- | --- |
| E1 episode membership | Explicit links + structured time/place rules | Bounded semantic retrieval + relation classifier | Whether model assistance improves recall without harmful false merging |
| E2 cross-time continuity | Explicit authored links | Supported model-proposed thread relations | Whether new relationships are useful, not merely similar |
| E3 refinding | Exact/lexical/structured retrieval; dense baseline where available | Hybrid reranking, then limited graph or hierarchy expansion | Whether additional retrieval infrastructure earns its maintenance cost |
| E4 maintenance | Full deterministic projection rebuild | Incremental affected-set updates | Equivalent truth/control state with less recomputation and stable identity |
| E5 synthesis | Factual record and silence | Grounded reconstruction and explanation/contrast | Added substance, comprehension, non-invasiveness and whole-page value |
| E6 later authoring | Manual selection/editing | Optional scoped AI edits | Control, edit survival and satisfactory output without prompt gymnastics |

Pin model, prompt, extraction/index versions, context budget and fixture revision.
Keep held-out scenario variants; do not tune and judge on identical examples.
Human grouping labels can include several acceptable partitions: the system
must preserve hard facts and forbidden joins, not imitate one subjective filing
scheme. Model judges assist triage; humans judge novelty, usefulness and ownership.

### 11.3 Acceptance measures

Hard automated requirements across the covered owner portfolio:

- No unauthorized derivative served after effective revocation at server checks.
- No correction or rejected membership restored by replay/backfill.
- No authored field changed by an undelegated model patch.
- No duplicate logical identity, derivative-as-independent-witness, or false
  count caused by multi-lens membership.
- Exact source/dossier destinations and bounded continuation/restoration work.
- Rebuild preserves human controls and identity registry; incomplete coverage
  cannot be reported as complete.

Quality measures: false merges/splits, unsupported memberships, proportion
unplaced but findable, exact-item retrieval success, unnecessary identity/title/
membership churn, claim support/coverage, redundant Returns, subjective intrusion,
value before a tap, and coherence of the entire page over repeated visits.

Efficiency measures: affected records per event, dependency/viewer fan-out,
index lag, p50/p95 read and repair latency, model calls/tokens/cost per admitted
source and per **published useful** synthesis, cancellation and dead-letter rate.
Measure actual query plans at 10,000+ records and skewed shared histories.

Do not invent release latency or quality numbers from paper scores. Establish
measured baselines in the replay harness, then record tolerances and service
budgets before cutover. Permission and authored-control failures cannot be
averaged away by good prose. Full product acceptance still includes ordinary,
shared, current-consequence and no-value/silence cases, not just W1.

## 12. Implementation units inside the existing roadmap

The units below refine R1–R7; they do not replace R0/R8, create another roadmap,
or require waiting for every adjacent visual lane. They are not implemented by
this documentation change. Schema/owner choices receive review before code.

| Unit | Existing package | Concrete work and likely home | Exit evidence |
| --- | --- | --- | --- |
| U1 owner contracts and replay fixtures | R1/R2 | Explicit owner/revision/authority adapter matrix; typed time and dependency contracts in shared core/Life; W1–W6 manifests in existing test/eval homes | No guessed owner revision; retained source-only and negative-occurrence paths accounted for; proposed schema diff reviewed |
| U2 connected corpus maintenance | R1/R2 | Durable downstream change delivery, owner-backed projector callers, revision/insert/restore guards, paged backfill, shadow reads, existing index modules and worker patterns | Actual populated reads match owner truth; restart/revocation races pass; shadow comparison includes payload/authority; no silent serving switch |
| U3 organization and repair | R2 | Typed groups/memberships, identity registry, controls, baseline grouping and affected-set dependency rebuild | W1–W5 transitions coherent across replay/rebuild; no model requirement for core custody and correction |
| U4 useful lens reads and refinding | R3/R4/R5 | Native digest/dossier data, complete custody, indexed anchor recovery, exact/structured whole-corpus search, cross-root handles | Ordinary and rich records useful; all lenses have truthful depth; no classification burden or source loss |
| U5 supported synthesis and kept versions | R7 with R4/R5 | Bounded reconstruction and contrast producers, claim/dependency checks, existing shared Return allocator, exact keep/reopen owner | Complementary useful outputs, correction/withdrawal propagation and cross-root delivery coherence |
| U6 manual-first authoring | Later extension of R7 | Canon wording update, manual selection, stable blocks, scoped AI patches, save/share/version behaviors | W6 plus authorship testing; no silent edits or source mutation; explicit hosted-share/export boundary |

Design U3–U6 contracts during U1 so early storage does not preclude them. Build
connected packages sequentially as a solo founder, integrating representative
outcomes rather than accumulating disconnected helpers. U5's contract and value
examples must exist early; U5 delivery is not indefinitely deferred until every
record detail is polished. U6 remains a deliberate later feature.

### 12.1 The immediate next coding batch

After review of this design, implement **U1 plus the first connected portion of
U2**, not another standalone index helper:

1. Add the six replay manifests and expected outcomes; reuse existing Life
   fixture worlds and label new synthetic evidence explicitly.
2. Define the owner adapter matrix for retained originals, admitted anchors,
   existing graph objects, historical Atlas material, shared contributions and
   kept compositions. Mark unavailable owners explicitly rather than stubbing
   them as successful. Review time roles and multi-owner dependency handling.
3. Propose the minimal schema/transaction diff for independent Life change
   delivery, publication guards, and checkpoints; include the control/identity
   seams U3 needs. Do not deploy it from this design task.
4. Connect admitted source custody and its anchor changes through the same
   tested path into a shadow index. This is the first adapter, not the product's
   architectural limit; extend the matrix across owners before serving cutover.
5. Exercise duplicate events, late imports, source-only items, correction,
   withdrawal during work, reauthorization and first-insert races against
   Postgres. Demonstrate real incremental population and indexed reads.
6. Record code/test/coverage receipts in the existing status document and
   roadmap. Update OpenAPI/mobile types only when a transport changes.

The batch should end with observable data flow from an authorized owner change
to a correct shadow Life record, plus explicit remaining owner coverage. A
passing helper suite alone does not complete it. This is an engineering
dependency sequence within a whole-system design, not a demand to prove one
behavior loop or freeze the philosophy first.

### 12.2 Adjacent lanes

- **Entity:** supply canonical place/person/source handles and exact read/action
  destinations. Life does not own entity resolution or redesign entity pages.
- **Chat/Intake:** supply admitted evidence and correction events under the
  contribution contract. Life must not compensate by scanning all chat history.
- **Plan/Occasion:** supply arrangements, participation and occurrence truth.
  Unresolved retained-intention ownership blocks those writes only, not existing
  source/episode organization. Do not settle that lane by inference here.
- **Home/Places/live engine:** consume evidence-backed handles and supply current
  conditions and delivery allocation. Life does not independently choose a route
  or prove a current opening feasible from old memory.
- **Native design:** can refine visual composition against stable semantic
  fixtures while backend contracts proceed. No fifth tab or editor-driven shell
  redesign is required.

## 13. Open choices and stopping rules for further research

| Question | Current recommendation | What must happen before changing it |
| --- | --- | --- |
| Exact derived-group and control storage | Relational Postgres alongside existing owners and Life read index | Review existing controls/identity coverage and a minimal migration diff in U1 |
| Saved-composition custody owner | Reuse a suitable versioned owner if audit proves one; otherwise a narrow authored-composition owner | Inspect existing persistence, rights and command semantics before R7 writes; current artifact projection is not enough |
| Episode window and semantic thresholds | Conservative explicit-evidence baseline; no fixed universal hours/radius rule | E1 held-out false-merge and retrieval evidence |
| Summary hierarchy or graph expansion | Exact/structured/hybrid baseline and bounded expansion | E3 shows a recurring miss worth the extra latency, indexing and repair burden |
| Visual document retrieval | Preserve originals plus ordinary extraction first | Layout-dependent retrieval failures justify a ColPali-style experiment; do not assume it handles personal photos |
| Serving/repair budgets | Bound every operation and instrument actual costs | Measured baseline before release; no borrowing vendor latency claims |
| Object-less kept intention | Preserve owner seam and no-auto-Plan rule | Explicit ruling from the existing Plan/Occasion lane |
| Manual composition UX | Manual selection + optional AI; saved snapshot default | U6 interaction design and authorship tests, not an automatic-memory benchmark |

More research should answer one of these named uncertainties. Do not reopen
the broad memory-framework search merely because implementation is substantial.
No custom training, RL memory controller, engagement ranking, or always-on
lifelogging is selected. These require a specific observed failure and an
evaluation advantage over the simpler system.

## 14. Research provenance and transfer limits

The September 5 research round evaluated source-preserving memory, organization,
retrieval, consolidation and repair. The follow-up examined Apple Photos and
human/AI authorship. The links below preserve the primary basis for this design;
the recommendations above are Vesper-specific engineering judgments, not claims
that these papers validate Life end to end. Sources accessed September 5, 2026.

| Source | Pattern used | Limit retained in this design |
| --- | --- | --- |
| [Zep / Graphiti, January 2025](https://arxiv.org/html/2501.13956v1) | Source-linked assertions and separate validity/ingestion time | Newest ingestion must not defeat an explicit correction; provenance links were not experimentally evaluated |
| [RAPTOR, ICLR 2024](https://arxiv.org/html/2401.18059v1) | Overlapping multiscale retrieval with raw leaves retained | Retrieval clusters do not establish stable lived-event identity |
| [TiMem, January 2026 preprint](https://arxiv.org/html/2601.02845v1) | Incremental hierarchical consolidation with fine evidence | Calendar summaries are derivatives, not canonical biography or event boundaries |
| [A-Mem, consulted revised paper](https://arxiv.org/html/2502.12110v11) | Link proposals across related notes | Automatic note evolution cannot overwrite authored meaning |
| [HippoRAG 2, ICML 2025](https://arxiv.org/html/2502.14802v2) | Source-anchored associative retrieval with dense fallback | Graph QA results do not establish deletion, permission or Life usefulness |
| [StateAuditor, August 2026 preprint](https://arxiv.org/html/2608.01619v1) | Check stale assumptions after memory correction | Bounded repair aid, not replacement for dependencies or a reason to ask routine verification questions |
| [ColPali, ICLR 2025](https://arxiv.org/abs/2407.01449) | Visually rich document-page retrieval | Conditional experiment, not evidence of attendance or a general personal-photo organizer |
| [RHELM, May 2026 preprint](https://arxiv.org/html/2605.31086v1) | Evolving heterogeneous-source evaluation | Borrow change sequences, not synthetic personas or benchmark scores as product validation |
| [Apple Photos album-to-memory creation](https://support.apple.com/guide/iphone/play-memory-movies-iphee2ee53fe/ios) | Start from manually chosen material | A product interaction precedent, not evidence of Vesper user demand |
| [Apple Photos memory personalization](https://support.apple.com/guide/iphone/personalize-your-memory-movies-iph1a5832438/ios) | Add/remove/reorder items and edit presentation choices | Do not infer Apple's proprietary memory architecture from its user controls |
| [Apple Intelligence memory creation](https://support.apple.com/guide/iphone/use-apple-intelligence-in-photos-iphf7de217f0/ios) | Description-directed draft alongside manual entry | Do not assume all precise edits are supported through natural language |
| [DirectGPT, CHI 2024](https://arxiv.org/abs/2310.03691) | Visible objects, scoped manipulation and undo with LLM assistance | Editing study, not evidence that a mobile personal-memory editor is validated |
| [Co-Writing with AI, on Human Terms, 2025](https://arxiv.org/html/2504.12488v1) | Selective delegation and preservation of author-valued decisions | Writing research with a limited interview sample; transfer to keepsakes remains a hypothesis |

The design is ready to guide contracts and a connected implementation batch.
It is not evidence of shipped grouping quality, model reliability, scale,
manual editing, or a complete Atlas replacement. Those require the package
receipts and evolving-record evaluations above.

## 15. Verification of this documentation delivery

This pass changed this design, its roadmap references/next batch, and inventory
classification only. It ran no application tests, model experiments, migrations,
backfills or deployments and did not modify either child repository.

Scoped lifecycle metadata validation passed for the design and roadmap;
whitespace validation passed. The global link check reports only its pre-existing
unrelated `state` target in the arrangements execution report. The inventory
check had 23 pre-existing unclassified documents before this pass and 22 after
classifying the touched Life roadmap; the new design is classified. These
remaining workspace issues are not claimed as fixed or as Life runtime failures.
