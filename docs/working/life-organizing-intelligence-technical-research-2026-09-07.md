---
doc_type: working
status: active
owner: founder / Life engineering / Capture integration
created: 2026-09-07
last_verified: 2026-09-07
expires: 2026-10-07
why_new: Separates a seven-area comparative literature review and experiment specification from the already substantial Life system design and execution roadmap; it supplies research evidence without becoming a second roadmap or product authority.
source_of_truth_for: []
supersedes: []
depends_on:
  - life-organization-and-composition-engine-system-design-2026-09-05.md
  - life-complete-system-and-atlas-replacement-roadmap-2026-09-05.md
  - ../contracts/life-v1-experience.md
  - ../systems/contribution-and-consequence.md
---

# Life organizing intelligence — technical research

## 1. Recommendation

Build Life's intelligence as **evidence-grounded organization with selective
model assistance**, not as a general autonomous memory writer. A useful Life
system needs to identify what material supports, distinguish one experience
from another, connect related experiences without merging them, preserve
recognizable organization over time, and show a useful selection of the record.
Answering questions from a memory store is only one of those responsibilities.

The research supports our existing separation between evidence, relationships,
organization, and presentation. It does **not** establish that our current
grouping is good, that a particular model is best, or that another memory
framework should replace the existing Life infrastructure.

The next substantial step is a connected experimental implementation of the
existing B0/B1/B2 comparison across **all five product worlds**, including
ordinary life, shared experience, and correction. This is a system-wide behavior
portfolio, not a proposal to narrow the product to one demonstration loop.

| Research area | Recommended first approach | What would justify more complexity? |
| --- | --- | --- |
| Evidence units and extraction | Literal, source-located evidence; metadata/text first, targeted vision where needed | Measured failures on tables, screenshots, image regions, or multi-event notes |
| Event identity and episodes | Typed relations plus bounded candidates and contradiction checks | B2 improves correct grouping beyond B1 without inventing attendance or merging unrelated events |
| Cross-experience continuity | Hybrid retrieval followed by relation-specific selection; keep analogy separate from membership | Needed links remain unretrievable after lexical, structured, and embedding candidates |
| Hierarchy and granularity | Stable owner/episode structure plus calendar navigation and multiple lenses | A deeper level measurably improves recognition or refinding |
| Incremental organization | Dependency-scoped recomputation, revision fences, durable controls, minimal justified change | A demonstrated affected scope cannot fit existing bounded maintenance |
| Presentation intelligence | Deterministic evidence coverage, recognition, diversity, and continuity under a budget | A model selector wins blinded judgments without losing exact access or increasing churn |
| Evaluation and economics | Stage-level metrics, sequence replay, human usefulness judgments, whole-lifecycle costs | Enough labeled errors exist to justify calibration, a trained classifier, or fine-tuning |

### Research status and limits

Research checked on September 7, 2026. Sources below are original papers,
official research publications, or implementation documentation. Peer-reviewed
work and recent preprints are distinguished. A recent preprint is a candidate
design pattern, not an independently replicated production result. No cited
benchmark directly validates Vesper's complete Life experience.

This investigation inspected local code and documents and ran one pure metric
diagnostic. It did **not** run paper implementations, buy model inference,
upload personal artifacts, collect participant data, benchmark models, modify
backend behavior, or authorize serving. Numerical experiment sizes and budgets
below are proposed starting points, not measured requirements.

## 2. What our code already provides—and what it does not

The implementation baseline inspected here is backend
`codex/life-shadow-rehearsal-2026-09-07` at `b1ab469f0`, in the isolated Life
worktree. The documentation baseline is
`codex/life-organization-value-research-2026-09-07` at `76de669` before this
report. Neither reference means the latest Life packages are merged into main
or active in production. Paths in this section are backend-repository-relative.

| Existing code | What is present | Research-bearing gap |
| --- | --- | --- |
| `backend/life_projection/evidence.py`, `source_evidence.py` | Typed evidence/time roles and a retained-source adapter with source revision and locator | Retained-source adapter is capture-time evidence, not inferred occurrence/place/people evidence; richer automatic extraction is not wired through it |
| `organization.py`, `organization_projector.py` | Stable group identity, typed relationships, Plan/Occasion containment, exclusions and scoped reconciliation | Automatic source-only episode discovery and semantic relationship classification are not implemented |
| `maintenance.py` and existing delivery/backfill machinery | Shared completion semantics, revision-aware maintenance, index/primary owner-group publication | Model preparation and richer organization must fit these seams, not bypass them |
| `organization_reader.py` and index readers | Bounded reads and scoped continuation foundations | Reader usefulness and grouping quality are not established by cursor correctness |
| `compiler.py` | Bounded deterministic digest selection, including owner-family representation | No measured recognizability/coverage selector or learned preview quality |
| `quality.py` | Deterministic fixture outcome counts and rates | No measured model quality; one rate currently conflates record recovery with relationship recovery |

`calendar_period_group_seed`, `evidence_membership_proposal`, and
`retained_source_evidence_unit` have test usage but no inspected production
caller composing them into the richer organizer. They are extension points,
not evidence that B1 or B2 has been completed. The Life package test receipts
in the roadmap demonstrate engineering behavior, not learned organization.

Two legacy areas require selective reuse rather than wholesale adoption:

- `backend/atlas/clustering.py` validates photo-oriented cluster inputs and
  uses photo/count/coverage thresholds. It is not a general semantic organizer;
  importing a five-photo minimum would exclude valuable text-only experiences.
- `backend/composition/FEATURE.md` describes the older Atlas board composer.
  Selection and fallback mechanics may be useful, but travel-specific affinity
  and significance assumptions should not become universal Life ranking.

### A concrete measurement correction

The following read-only call was executed against the pinned Life branch:

```python
measure_life_quality(
    required_record_ids=("dinner.receipt", "dinner.photo"),
    actual_record_ids=("dinner.receipt", "dinner.photo"),
    actual_joins=(),
    findable_record_ids=("dinner.receipt", "dinner.photo"),
)
```

It returns `required_link_recall=1.0` and `actual_join_count=0`.
That is valid **record** recovery, but cannot measure whether the receipt and
photo have the required relationship. The helper has no required-edge input.
Its undirected join pairs also cannot distinguish directed, typed relationships
or different evidence spans in the same source. Correct the measurement
contract before interpreting an organizer comparison; do not rewrite historical
results as if actual relationship recall had already been measured.

There are also two unrelated W1–W6 namespaces:

- Workspace `fixtures/life-engine/life-engine-replay-v0.1.json` describes
  product worlds and expected behavior, with some owner evidence unavailable.
- Backend `tests/life_projection/fixtures/shadow_rehearsal_v1.json` exercises
  delivery lifecycle scenarios such as update, withdrawal, and restore.

Report fixture namespace **and** scenario ID. Passing the second set does not
mean the first set's product organization has been implemented or evaluated.

## 3. Area one: multimodal evidence units and extraction

### The question

What is the smallest useful, attributable piece of evidence from a ticket,
photo, retained conversation, receipt, article, or note? How does it retain
enough context to be useful without turning an entire source into one event?

### What the research contributes

**MinerU2.5 — September 2025 preprint.** Its document parser separates coarse
layout analysis from detailed recognition of selected regions. The useful
pattern is handling layout and local content at different resolutions. Its
document benchmarks do not establish attendance, speaker attribution, or
ordinary-photo event understanding. [Paper](https://arxiv.org/html/2509.22186v1).

**ColPali — ICLR 2025.** It embeds document-page images with multiple vectors
and uses late interaction for retrieval. This is relevant when visual layout
contains retrieval cues lost by text extraction. It retrieves pages; it does
not by itself extract trustworthy event claims or organize personal photos.
[Paper](https://arxiv.org/abs/2407.01449).

**Late Chunking — 2024 preprint, revised 2025.** It contextualizes tokens over
a longer text before pooling representations for individual chunks. That can
preserve surrounding context while retaining passage-level retrieval. It does
not decide whether neighboring sentences describe the same event or which
person owns a claim. [Paper](https://arxiv.org/abs/2409.04701).

**EM²Mem — September 1, 2026 preprint.** It aligns captions, transcripts,
keyframes and structured fields into event-centered records before retrieval.
Its anchors use short temporal video segments, including 30-second segments;
they are not discovered sparse-life episodes. Its video QA setting is much
denser than occasional Vesper contributions. The useful hypothesis is retaining
cross-modal evidence together, not adopting its segmentation or semantic-profile
layer. [Paper](https://arxiv.org/html/2609.00551v1).

### Recommendation for Life

Start with source-located units that distinguish **literal content, extracted
claims, and organizational proposals**. One original can support several units
without becoming several independent witnesses. Preserve page/region/span
locators, owner/source revision, lineage, typed dates, attribution, and the
purpose for which a unit may be used.

Use metadata and existing text extraction first. A ticket's journey date is
planned travel, not proof the person took it. A file timestamp is not necessarily
the event date. Two paragraphs about different evenings need separate locators.
A screenshot of a message is not automatically a statement by the screenshot
owner. An image model may recognize visible objects without identifying people
or inferring their motives.

Use targeted vision only where a documented failure class requires it. Compare
page retrieval with extraction rather than assuming a single representation must
do both. Generated contextual text remains a derivative: it cannot become an
additional original source or silently supply missing occurrence evidence.

### Experiment E1: does richer evidence improve organization?

Compare (a) whole-source metadata/text, (b) source-located textual units, and
(c) targeted multimodal units. Include receipts, tickets, no-photo notes,
multi-event retained passages, derivative screenshots, and contradictory dates.

Measure exact field accuracy **by field type**, valid locator rate, missed
evidence, false attribution, planned-to-occurred mistakes, and downstream
required-edge recall. Run organization first with hand-checked units and then
with extracted units; that separates extraction errors from grouping errors.

Capture owns source extraction/lifecycle and the source-side envelope. Life can
define expected fixture units and consumer validation now. Do not add a second
source parser inside the Life worker to avoid that handoff.

## 4. Area two: event identity and episode grouping

### The question

Are these two records about the same dinner, separate visits to the same
restaurant, parts of one journey, or simply the same subject? This is not one
generic similarity score.

### What the research contributes

**MAVEN-ERE — EMNLP 2022.** Its event-relation work distinguishes coreference,
temporal, causal, and subevent relationships. That distinction is directly
useful to our task decomposition; its textual event datasets are not a
personal-life clustering benchmark. [Paper](https://aclanthology.org/2022.emnlp-main.60/).

**Cross-document event coreference using discourse coherence — ACL 2025.**
The method uses contextual connections across documents rather than isolated
event mentions. Its limitations include reliance on gold event mentions and
possible cascading errors in a real extraction pipeline. For Life, we should
test contextual support, but never supply invented connective narrative as
evidence. [Paper and limitations](https://aclanthology.org/2025.acl-long.1134.pdf).

**LLMERE — COLING 2025.** It asks about multiple relations for a focal event,
partitions the extraction workload, and uses rationales to improve relation
extraction. Its call-count improvement over pairwise processing is not a claim
that total tokens, checking work, or production latency are linear and cheap.
It suggests a bounded batch classifier worth comparing with pairwise calls.
[Paper](https://aclanthology.org/2025.coling-main.500/).

**HDBSCAN's implementation documentation** explains a useful limitation:
new data can change a transductive clustering, while `approximate_predict`
holds existing clusters fixed. Neither mode supplies durable product identity
or our merge/split/correction policy automatically. Use clustering as an
experimental candidate source, not the authority for Life handles.
[Official documentation](https://hdbscan.readthedocs.io/en/latest/prediction_tutorial.html).

### Recommendation for Life

Use bounded **candidate generation → typed relationship judgment → group-level
consistency checks → existing proposal/materialization**. Preserve direct
owner containment as the strongest baseline. Time/place/entity indexes and
lexical retrieval can cheaply propose candidates; semantic retrieval adds
recall when literal cues differ. None of these signals alone commits membership.

Distinguish these experiment labels before mapping to the existing enum:

- Same source or derivative: lineage, not another occurrence.
- Same occurrence: event-specific support, not common topic.
- Part of a larger episode: dinner within a journey, not dinner equals journey.
- Related place/person: a navigable association, not presence or attendance.
- Continued attention: a supported connection across experiences.
- Useful analogy: a proposed comparison, not biographical fact.
- Insufficient evidence or contradiction: legitimate outcomes.

Coreference and containment have different algebra. Pairwise similarity is
not transitive permission to merge a chain. Before admitting a proposed group,
check contradictory time/place/owner evidence and exclusions across its
boundary. Keep group proposals independent of generated names.

### Experiment E2: distinguish identity from resemblance

Run B0 owner containment; B1 structured evidence with deterministic checks;
B2 the same B1 inputs plus bounded semantic relation assistance. Include a
semantic-only clustering challenger so we can quantify the failure we expect,
rather than merely assert it.

Hard cases: the same restaurant on two dates, similar dishes in unrelated
cities, two differently worded accounts of one meal, an unused reservation,
an outing without a Plan, and one note about multiple outings. Compare
candidate recall separately from classification precision. Evaluate joins at
the evidence-unit level and resulting groups against acceptable partitions.

For B2, compare focal-item batch classification with pairwise classification
under the same candidate and token budgets. Require a typed result and bounded
source references or contradiction codes—not verbose private reasoning. A
retrieved candidate is never automatically an admitted relationship.

## 5. Area three: cross-experience continuity and associative retrieval

### The question

How do we connect an Italy pasta observation, a retained explanation, a friend's
contribution, and a later NYC cooking attempt without merging those experiences
or assigning the person an invented culinary identity?

### What the research contributes

**HippoRAG 2 — ICML 2025.** It combines graph structure, passage information,
query-oriented filtering and graph traversal to improve associative retrieval.
This is relevant when useful evidence requires more than one semantic hop.
Its QA results do not establish human-legible groups or beneficial everyday
resurfacing. [Paper](https://arxiv.org/html/2502.14802v2).

**Contextual Retrieval — Anthropic engineering, September 2024.** It adds
context to chunks before embedding and lexical indexing. This suggests a
controlled comparison against naked passage embeddings. Generated context has
construction cost and can add errors; it must remain derived and dependent on
the actual source, not be counted as independent evidence.
[Official research report](https://www.anthropic.com/engineering/contextual-retrieval).

**A-Mem — February 2025 preprint version inspected.** It generates structured
notes, finds related memories, and evolves contextual descriptions and links.
Neighbor-assisted discovery is a useful hypothesis. Automatically rewriting
past memory content is not a substitute for Life's original custody, explicit
controls, and revision-aware derived organization.
[Paper](https://arxiv.org/html/2502.12110v1).

### Recommendation for Life

Begin with a hybrid candidate union: exact owner/Place/People references,
lexical matches, compatible dates where relevant, and embedding neighbors.
Evaluate whether a bounded graph expansion adds useful links only after that
baseline. Existing relational edges may be sufficient; a graph algorithm does
not require a new graph database or another memory service.

Separate two products of retrieval:

1. **A durable relationship in Life:** supported continuity, with evidence and
   a stable route to the originals.
2. **An opening or comparison:** possibly useful generated content derived
   from that record, often more appropriate to Home or Places.

Life can hold the Italy observation; Home might compare Sorrento's cliffs with
another coast or offer a relevant NYC possibility. An externally sourced
geological comparison is not a new autobiographical fact. A friend's authorized
Paris contribution may be valuable without an AI essay explaining why it matters.
Life should not become a second infinite recommendation feed.

### Experiment E3: useful connection rather than repeated input

Create judgments for required known links, plausible but unsupported links,
useful optional analogies, and forbidden connections. Include paraphrases,
name collisions, highly generic food vocabulary, and links several months
apart. Compare hybrid retrieval; hybrid plus contextualized chunks; and hybrid
plus bounded graph expansion. Start with candidate budgets of 8, 16 and 32 as
an experimental sweep, not production defaults.

For exact refinding, measure whether the specific original is returned, not
just a broadly related group. For new value, separately judge added substance,
relevance, evidence sufficiency, attribution, and whether it repeats what the
person already supplied. Distinguish supplied/received information from merely
shown information. An LLM judge can triage; it cannot establish that the person
learned something or liked the result.

## 6. Area four: hierarchy and granularity

### The question

Which structure helps a person recognize and navigate their life without
requiring them to think in our data model? When is a day, episode, journey,
month, Place, or Thread useful—and when is it another unnecessary layer?

### What the research contributes

**RAPTOR — ICLR 2024.** It recursively clusters and summarizes information
at multiple levels for retrieval, with soft membership. A retrieval tree can
help answer broad and specific questions, but its generated summary structure
does not define stable user-facing episodes or exclusive source membership.
[Paper](https://arxiv.org/html/2401.18059v1).

**MemTree — ICLR 2025.** It incrementally builds a semantic hierarchy with
context aggregation at higher nodes. This supplies an alternative to a flat
memory collection, but its hierarchy is not evidence that users should browse
an equivalent tree or accept automatic title/structure changes.
[Paper](https://arxiv.org/html/2410.14052v3).

**TiMem — January 2026 preprint.** It consolidates memory across temporal
levels. Its own limitations include fixed temporal boundaries, additional
consolidation cost, and incomplete storage-time forgetting. Temporal
aggregation is worth studying; fixed daily/weekly/profile stages should not
become a mandatory Life experience. [Paper](https://arxiv.org/html/2601.02845v1).

**PhotoTOC — Microsoft Research, 2003.** It studied time/appearance-based
photo grouping with an overview linked to the original chronological collection.
Its browsing evaluation supports testing recognition and navigation, not just
cluster statistics. It does not establish the right hierarchy for sparse,
mixed-media Life records. [Research publication](https://www.microsoft.com/en-us/research/publication/phototoc-automatic-clustering-for-browsing-personal-photographs/).

### Recommendation for Life

Keep three structures distinct: retrieval summaries, durable organization,
and the currently visible navigation path. They can share evidence without
sharing one tree. Time/Places/People/Threads are views over relationships,
not four copies of the originals.

For the same corpus, an acceptable Time path might be month → two local
outings; a journey might have a few supported city segments. Do not insert a
week or a day solely because a hierarchical algorithm creates that node.
Place access may collect separate visits. A Thread may connect several episodes
without containing them as one event. Direct search must bypass all of these
levels to reach an exact original.

Period membership can use a declared time role without claiming an occurrence.
An undated reading remains available without forced chronology. Multiple
relationships must not multiply source counts or visitor counts. Later authored
compositions select and arrange existing evidence; they need not be the same
structure as the automatic organizer.

### Experiment E4: does an extra level earn its place?

Compare a flat dated record, a shallow owner/episode structure with calendar
navigation, and a model-proposed hierarchy. Give reviewers identical evidence
and refinding tasks: find the sauce note, distinguish two cafe mornings,
recover an unused ticket, understand a journey sequence, and locate a friend's
contribution.

Measure correct recognition, exact task success, navigation actions, wrong
turns, and disorientation after an update. Accept multiple valid structures;
do not reward the algorithm merely for matching one author's arbitrary tree.
Blinded content lists or low-fidelity artifacts are enough for early comparison;
this does not require another visual design sprint or app/device tests.

## 7. Area five: incremental organization, rewriting, and correction

### The question

How does Life improve when new material arrives without reorganizing everything,
overwriting a deliberate edit, preserving a false claim, or losing the history
needed to understand a change?

### What the research contributes

**Incremental constrained clustering with minimal weighted modification —
CP 2023.** It treats stability relative to prior clustering as an explicit
optimization concern while incorporating constraints. Its solver, domain, and
interactive labeling assumptions need not transfer. The useful idea is to
penalize unnecessary changes, not to relax explicit user corrections or ask
users to maintain training labels. [Paper](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CP.2023.10).

**MemForest — May 2026 preprint.** It separates extraction from updates to
scoped temporal structures and refreshes affected derived paths. Its logarithmic
dependency-depth argument assumes balanced structures and sufficient concurrency;
it is not a bound on total work, tokens, or end-to-end latency. The narrow
transfer is dependency-scoped maintenance, not adoption of its whole framework.
[Paper](https://arxiv.org/html/2605.23986v1).

**Zep/Graphiti — January 2025 preprint.** Its temporal graph distinguishes
event-valid time from knowledge/ingestion time. That distinction is useful for
late-arriving historical material. Its described conflict handling does not
replace current owner authority: a newly ingested old claim must not beat a
newer owner revision or explicit correction in Life.
[Paper](https://arxiv.org/html/2501.13956v1).

**TrustMem — June 2026 preprint.** It evaluates individual memory transitions
for coverage, preservation and faithfulness and uses those judgments in
training. Its verifier is itself a model, and the reported benchmarks are not
Life's multimodal browsing tasks. Borrow transition-level audit questions
before considering learned memory-editing policies or reinforcement learning.
[Paper](https://arxiv.org/html/2606.25161v1).

### Recommendation for Life

Treat organization as maintained derived state, not an ever-rewritten biography.
Preserve originals, supported historical states, durable exclusions, authored
labels and stable group identities. Recompute the affected evidence/relationship
scope; publish only after rechecking owner revision and relevant controls.
Never hold source/organization database locks during model inference.

The preparation result should identify its input revisions, proposed changes,
dependencies and method version. A stale result is rejected or re-prepared,
not allowed to write because its model score was high. Reuse the existing
maintainer, fences, shadow index and durable delivery. Local invalidation is
not a replacement for durable event delivery or continued pending work.

Stability is subordinate to correctness. A later nonattendance statement must
remove a visit claim even if the resulting preview changes. Conversely, a new
photo is not automatically a reason to rename a journey or replace an already
useful representative. Preserve valid user choices according to their actual
scope, not as global preference or identity inferences.

### Experiment E5: quality over an evolving sequence

For every product world, replay late imports, duplicates, out-of-order owner
revisions, corrections, rename/detach, withdrawal and explicit restoration.
Measure each state, not only the final snapshot. Include a crash/retry boundary
where relevant to an existing maintainer test.

Compare full recomputation with affected-scope recomputation. Require semantic
equivalence of eligible evidence and accepted relationships, while separately
checking prescribed identity/history behavior; byte-identical generated prose
is not a meaningful equivalence requirement. Test whether old routes and stable
reader anchors still resolve appropriately.

Report membership churn, title churn, preview churn, order churn, number of
unrelated scopes touched, stale results rejected, repair delay, and model work.
Calculate avoidable churn only among still-eligible unaffected material.
Required correction/withdrawal changes are separate. A system that never
updates is not successful merely because it has zero churn.

## 8. Area six: presentation intelligence and representative selection

### The question

Once the right material is organized, what small selection makes it useful
and recognizable? This is a different optimization problem from deciding
membership, and it materially affects whether Life feels like a personal
record or an empty database browser.

### What the research contributes

**Lin and Bilmes — ACL 2011.** Their summarization work combines coverage
and diversity through submodular objectives and budgeted selection. It offers
a principled alternative to taking the highest-scoring near-duplicate items.
Approximation guarantees depend on the objective and constraints; adding an
arbitrary negative churn penalty does not preserve them automatically.
[Paper](https://aclanthology.org/P11-1052/).

**Stuff I've Seen — SIGIR 2003.** This personal retrieval system used contextual
cues across previously seen material; its workplace deployment found time and
people useful for refinding. It supports testing those cues in Life rather than
assuming generated summaries are always the best preview. Its users and tasks
are not evidence of consumer retention for Vesper.
[Research publication](https://www.microsoft.com/en-us/research/publication/stuff-ive-seen-a-system-for-personal-information-retrieval-and-re-use/).

### Recommendation for Life

Begin with a deterministic selector whose inspectable features represent
recognition, distinguishing evidence, useful facet coverage, redundancy, exact
destination quality, and continuity with a still-useful previous selection.
Validity and current visibility are filters, not optional ranking bonuses.

A lens-specific preview might favor:

| Entrance | Useful distinguishing material | Unhelpful default |
| --- | --- | --- |
| Time | Which evening, a recognizable original, supported sequence | A title plus generic artifact count |
| Places | The specific venue and separate visits/keeps | Treating every place mention as a visit |
| People | An attributed contribution and its shared context | An inferred relationship score or blended group voice |
| Threads | What connected across contexts and what changed | All items sharing a broad keyword |

A receipt can be the right preview when someone wants the bottle name. A
friend's actual note can be the entire value. An image is not mandatory, and
text-only material should not be demoted merely because it is less decorative.
Reserve owner-family diversity only if it helps useful coverage; do not make
the product a catalog of backend object types.

Keep original access independent of preview selection. Summaries are optional
derived renditions with source dependencies, not the canonical record. A
material-improvement rule can preserve a valid preview until a new item adds a
missing facet or corrects a misleading one. Evaluate whether this is too static
as well as whether it prevents needless movement.

### Experiment E6: useful previews without more homework

Compare current compiler selection; deterministic coverage/diversity selection;
and a bounded model selector over the same eligible candidates. Separate
selection quality from copy quality by first holding the text fixed.

Ask internal reviewers which experience they recognize, what useful fact or
original they can get to, and whether a selection omits the distinguishing
detail. Include sparse weeks, text-only experiences, repeated photos,
multiplayer contributions, and a withdrawal after a preview has been generated.
Then compare concise copy variants using the winning evidence selections.

Track useful evidence coverage, redundancy, exact access, mistaken inference,
preview stability, and preference with reasons. Do not optimize time spent,
click volume, personality inference, or pressure to contribute more. These are
research tasks for reviewers—not questions Life should routinely put to users.

## 9. Area seven: evaluation, uncertainty, and model economics

### What the research contributes

**LongMemEval — ICLR 2025.** Its long-term conversational-memory benchmark
tests extraction, multi-session reasoning, temporal reasoning, updates and
abstention. These are useful regression dimensions, but QA accuracy is not
enough to certify Life organization, stable navigation, or meaningful previews.
[Paper](https://arxiv.org/abs/2410.10813).

**HaluMem — November 2025 preprint.** It evaluates extraction, updating and
memory-based answering separately, exposing failures that accumulate across
operations. Its constructed memory/dialogue setting is not an observed
consumer-life corpus. Borrow error attribution by stage rather than treating
one end-to-end answer score as a diagnosis.
[Paper](https://arxiv.org/html/2511.03506v2).

**H2HMem — 2026 preprint.** Its multimodal dyadic and multiparty benchmark
tests recall, reasoning and application, including speaker and modality
attribution challenges. Its human-in-the-loop generated material does not
establish the social acceptability or visibility policy of a consumer app.
It makes a useful counterweight to single-user text-only memory evaluations.
[Paper](https://arxiv.org/html/2606.09461v1).

**Calibration research — ICML 2017.** Guo and colleagues show why classifier
confidence and observed correctness can differ, and study calibration methods
including temperature scaling. That does not make an LLM's self-reported
“90% certain” a calibrated probability. Methods requiring logits cannot simply
be applied to arbitrary verbal scores. [Paper](https://proceedings.mlr.press/v70/guo17a.html).

### A common experiment corpus

Use the existing product worlds, not a new travel-only benchmark:

| Product world | Essential behavior |
| --- | --- |
| W1 Europe journey | Supported segments, mixed transport evidence, late correction, exact originals |
| W2 ordinary NYC life | Useful organization without Plan/Occasion or photos; distinct repeated visits |
| W3 continuing attention | Observation, retained explanation and later attempt connected without invented identity |
| W4 shared dinner | Common context with attributable, viewer-relative contributions and withdrawal |
| W5 ambiguous ticket | Kept source without assumed attendance; negative evidence survives replay |

W6 manual authorship remains a later-phase compatibility case: automatic work
must not preclude selecting, rearranging or titling a composition independently.
It is not permission to build a Life-owned authoring system now.

Start with roughly 30 calibration sequences and 30 separately authored holdout
sequences spread across W1–W5. This is a tractable development seed, not a
statistically sufficient launch sample. Expand coverage after inspecting error
classes. Holdouts must differ in structure, ambiguity and source arrangement,
not merely replace Nice with another city. Split by underlying story and source
lineage so crops, paraphrases and screenshots cannot cross the boundary.

Cover all twelve perturbations already specified in system-design §16: month
boundary; late import; derivative duplicate; repeated venue; timezone/midnight;
multi-event no-photo note; undated reading; transient Ask versus retention;
unrelated similar food; viewer differences; withdrawal after preview; stale
replay after negative attendance. Distribute them across worlds rather than
constructing a needlessly exhaustive Cartesian product.

Use synthetic or explicitly authorized, de-identified artifacts. No private
trip corpus should be sent to an external model merely because it is convenient.
Each experiment manifest records fixture version, owner-envelope version,
source revisions/locators, model/prompt versions, and method parameters.

### Separate measurements instead of one quality number

1. **Evidence:** exact field correctness by type, valid source locators,
   missed claims, fabricated/incorrectly attributed claims.
2. **Candidates:** required candidate recall at K before classification;
   an unreachable pair cannot be rescued by a better classifier.
3. **Relationships:** required typed-edge recall, admitted-edge precision,
   contradiction/forbidden-edge counts and rates, abstention coverage.
4. **Groups:** accepted membership/hierarchy, false merges/splits, unsupported
   occurrence claims, unplaced-but-findable evidence, useful group coverage.
5. **Reads:** exact-original task success, distinguishing-preview usefulness,
   navigation effort, and grounded new value where applicable.
6. **Evolution:** required repair, unjustified membership/title/preview/order
   churn, stale-state behavior, preserved controls, old-route resolution.
7. **Resources:** extraction/build/update/read work, affected-scope size,
   tokens, storage, latency, retries, and human correction burden.

For required-edge recall, match relation type, direction when relevant,
source-located endpoints, viewer/purpose scope, and tested revision state.
Only symmetric relations should normalize endpoint ordering. Keep record recall
as its own useful metric. Where grouping judgments are legitimately ambiguous,
record acceptable alternatives and reviewer disagreement rather than fabricate
one unquestionable gold tree.

Blinded review should compare identical evidence and budgets. Use at least a
second reviewer for ambiguous grouping/value judgments when feasible. Small
founder-led judgments can guide development; they cannot establish broad user
preference. Model judges should see source evidence, be checked against human
labels, and not be the sole assessor of their own model family's output.

### Uncertainty and acceptance

Plot precision versus admitted coverage per relationship type on calibration
data, choose thresholds there, and report untouched holdout performance with
raw denominators. If scores are only ordinal, present observed score bands;
do not imply calibrated probabilities. Repeat stochastic variants enough to
expose instability, with a small fixed repeat budget recorded in the manifest.

Every experiment must include a conservative no-new-link baseline. High
precision achieved by doing nothing is not progress; judge coverage and useful
findability alongside it. Conversely, higher recall does not compensate for
fabricated attendance, erased corrections, or leaked withdrawn material.

Known authority/correction/replay fixtures must pass completely before broader
promotion is considered. Zero failures in a finite fixture suite is necessary
test evidence, not a population-level safety guarantee. Product-quality and
cost thresholds remain decisions to set after calibration, before the final
holdout run—not numbers selected after seeing a favorable result.

### Cost: include work moved out of the query path

EM²Mem's Appendix C reports lower inference tokens but higher construction
tokens. In its 500-query comparison, total tokens are 104.50M versus 102.58M
for its baseline, with an unweighted token break-even near 536 queries. Those
numbers are not Vesper cost estimates; they illustrate why fast retrieval alone
does not establish lower total cost.
[Reported construction and amortization analysis, Appendix C](https://arxiv.org/html/2609.00551v1).

For Life, measure this workload explicitly:

```text
lifecycle cost = extraction + initial organization + incremental updates
               + retrieval/presentation + retries/repairs + retained storage
```

Track input/output/vision/embedding work separately and price it using actual
run-time provider rates when an experiment is authorized. Cache hits, reuse,
and invalidation matter. One retained article consulted once has different
economics from a frequently opened shared occasion. Use scenarios at roughly
100, 1,000 and 10,000 evidence units for boundedness tests, including a highly
skewed group; synthetic scaling results do not establish consumer performance.

Compare a small-corpus whole-context challenger where it fits the **same**
privacy and input budget. A sophisticated index should earn its cost. Compare
methods first with the same model where possible; swapping both architecture
and model prevents clear attribution. Model selection and later tuning follow
measured failures, not a benchmark leaderboard.

Use the existing model registry/gateway for any later inference harness.
Predeclare a run budget and stop conditions; record cache keys with source
revision, locator, purpose, prompt/model and extractor version. Do not cache
private generated context across visibility scopes. No model deployment or
new inference framework is selected by this report.

## 10. How this enters the existing engineering plan

The [Life roadmap](life-complete-system-and-atlas-replacement-roadmap-2026-09-05.md)
remains the sole sequence. These experiments refine M2/M3/M5 inside R0–R8;
they are not seven new delivery lanes or a prerequisite to finish every paper
before implementing useful behavior.

### Next connected checkpoint

1. **Correct and extend the measurement seam.** Preserve record recovery;
   add typed required-edge judgments, group expectations, and explicit fixture
   namespaces. Add regression cases in which all records exist but no required
   relationship does. Keep unmeasured denominators explicit.
2. **Turn the five product worlds into executable organization fixtures.**
   Include source-located units, owner states, updates and accepted read results.
   Keep oracle-evidence and raw-artifact runs separate. This work can proceed
   while Capture finalizes richer source evidence.
3. **Implement the B1 experimental consumer using existing proposal seams.**
   Exercise periods, source-only episodes, multi-event evidence, and negative
   evidence without introducing model calls or a second durable index.
4. **Add a bounded B2 offline comparison.** Use the same evidence/candidates,
   typed outputs, contradiction checks and existing model gateway. Run E1–E6
   selectively against the shared corpus; do not create six independent rigs.
5. **Evaluate the composed reader result.** Judge groups, exact retrieval,
   preview selections, and update stability together. Decide which expensive
   techniques earned a place; record failures and cheaper baselines as well
   as wins. Only then propose production wiring and serving criteria.

Steps 1–3 are available without a new design project or production activation.
Step 4 needs a bounded inference-run decision and eligible data; this research
request itself did not authorize spending or personal-data processing. No
blanket “everything else is blocked” conclusion follows from a pending producer.

### Exact interfaces needed from adjacent owners

| Owner | Needed interface or agreement | What Life can do meanwhile |
| --- | --- | --- |
| Capture | Current-authority source/evidence read: owner/source revision, typed date claims, source locator and repair behavior, supported place/participant attribution, permitted purpose/scope, negative/corrected claims | Fixture contract, consumer validation, replay, candidate/group experiments on explicit evidence |
| Integration | Confirm how extraction completion or revised evidence makes the existing durable delivery path reach Life; current-state read and revision fencing must agree | Exercise identifier-only consumer/replay; report unsupported richer evidence rather than invent a producer |
| Home/Places | Exact original/group destinations and eligible derived relationships/content, not a copy of Life's mutable inferred biography | Produce bounded shared fixtures with correct original routes and viewer-relative evidence |
| Later composition owner | Authored selection/title/order controls remain distinct from automatic membership and source custody | Test that automatic repair preserves supported controls; do not invent the writer |

Reuse existing owner revision semantics. If asynchronous extraction changes
evidence without changing the source revision, that needs an agreed version or
delivery contract—not a consumer assumption that cache refresh will discover it.
Do not independently modify Capture's transactions or compete for Intake's
single acknowledgement. The live engine continues to read canonical owners
directly, whether or not Life is ever opened.

### Deferred until evidence justifies them

- Custom-trained or reinforcement-learned memory writers.
- A universal latent personality/interest profile as the organizer.
- Whole-corpus reclustering on every import.
- A mandatory hierarchy, photo quota, or generated summary for every experience.
- A new graph database, memory framework, queue, or parallel source parser.
- A user-facing uncertainty-clearing inbox or ongoing filing/labeling work.
- Serving cutover, production activation, destructive migration, or Atlas deletion.

## 11. Bottom line

We have enough research to stop treating “organizing AI” as one unspecified
future component. The methods worth testing are concrete: source-located
multimodal evidence, typed event relations, hybrid associative retrieval,
shallow useful hierarchy, constrained incremental maintenance, and
coverage-oriented presentation.

The remaining uncertainty is primarily **which combination produces useful,
recognizable Life records from our sparse and evolving evidence at acceptable
cost**. Our next research output should therefore be a reproducible comparison
with real error cases and readable results—not another broad memory-framework
survey, and not a premature claim that the infrastructure already supplies
the intelligence.
