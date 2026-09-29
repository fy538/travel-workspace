---
doc_type: working
status: active
owner: founder / product strategy
created: 2026-09-28
last_verified: 2026-09-28
expires: 2026-10-28
why_new: A bounded six-question research synthesis is needed to test the memory-as-consumer-surface direction against primary research, adjacent products and inspected implementation. The product-direction note preserves the chronological discussion; this companion owns the dated evidence and proposed research decisions, not another product canon or implementation queue.
promotes_to: Existing Product Thesis, Product Model, Life, contribution and editorial owners after explicit decisions; implementation sequencing remains in the program roadmap.
supersedes: []
source_of_truth_for: []
---

# Memory as product: six-question direction review

Research date: September 28, 2026. Three parallel research agents covered
collections/capture, connections/multiplayer, and architecture/commercial choice.
The coordinating review reconciled their findings and checked selected sources
and code directly. Recommendations below are proposals, not adopted policy.

## 1. Executive judgment

**The direction is plausible and more concrete, but not an empty market.**
Research supports treating personal material as something people can recover,
enjoy, understand and share—not merely context for an assistant. It does not
establish that people want another destination for that material, or that more
automatic organization will make them return.

The proposed center is coherent:

> Ordinary contributions become a connected record worth having in its own
> right, with understanding, possibilities and practical help growing from it.

Three benefits should be unmistakable in the experience:

1. **Worth keeping now:** the contribution becomes recognizable and useful
   without classification homework or a large historical import.
2. **Worth returning to:** the person can recover, revisit and explore it,
   including for pleasure rather than a new task.
3. **Richer together:** another person's material or perspective adds something
   neither person supplied alone, without equal-effort participation.

This is not a proposal for three product modules or a compulsory progression.
Practical help remains important. It should be a natural consequence of the
record and present circumstances, not the required justification for every
kept item.

| Research question | Assessment | Most consequential next question |
| --- | --- | --- |
| Why revisit a collection? | Strong supporting research; much is already in Life doctrine | What makes the actual object worth opening again? |
| Why contribute here? | Low friction is necessary but insufficient | What advantage beats leaving the same material in Photos, messages or email? |
| Which connections deserve attention? | Strong existing editorial doctrine and useful code safeguards | Does the output add substance beyond a capable baseline? |
| What does multiplayer add? | Plausible benefit, with persistence/audience tensions | Does each participant benefit without obligation or loss of their own voice? |
| Does the architecture fit? | Several inspected mechanisms fit well | Do ingestion, identity, collections and repair preserve those guarantees end to end? |
| Why choose and pay? | An occupied adjacent market, not evidence of Vesper demand | Which recurring benefit earns preference and can be served sustainably? |

**Recommendation:** strengthen contribution-to-collection quality and its
downstream uses; do not restart the architecture or add a broad feature list.
Research and system implementation can proceed together. No single experiment
should define the whole product or block unrelated engineering progress.

## 2. Authority and evidence boundaries

Read this beside the [product-direction trace and follow-up](product-direction-2026-09-28.md).
The accepted [documenting/composer decision](../decisions/2026-09-27-documenting-core-loop-and-one-composer.md),
[collections decision](../decisions/2026-09-28-collections-are-the-spine.md),
[ingestion decision](../decisions/2026-09-28-ingestion-and-connected-inbox.md)
and [multiplayer decision](../decisions/2026-09-26-multiplayer-direction.md)
retain authority. Pending friction defaults, catalog mechanism R3, notification
policy and friend-content use grants remain pending where their owners say so.

### Repository snapshot

| Repository | Inspected revision | Boundary |
| --- | --- | --- |
| Workspace research lane | `5dda28b645204cb973a53c4611df6560e835b3fe`, `codex/product-direction-2026-09-28` | Included the existing uncommitted §1.1 follow-up; this report is additive |
| Backend | `fdf789d06e8b889ac9882072e595e2d7cea02f21`, `main` | Lane child resolves to the canonical child checkout; read-only, clean at inspection |
| Mobile | `23cff76f41fddc931a20db8b2016b131bb70d329`, `main` | Same boundary; not a claim about another active implementation lane |

The primary workspace had concurrent design/document edits. They were not
changed or used to infer implementation status. File locations and line numbers
below refer to this snapshot; later revisions may move them.

This is a targeted investigation, not an exhaustive code review or a hands-on
review of all design canvases. No app/backend tests, device sessions, paid model
runs or database operations were executed. Test assertions were inspected; they
are not new passing receipts. Product pages establish advertised capabilities,
not actual usability, adoption or comparative superiority.

Online sources were accessed September 28. Foundational work keeps its original
date; newly retrieved does not mean newly published. Qualitative studies,
controlled experiments, technical benchmarks and vendor documentation are
distinguished below. No user interviews were conducted in this research.

## 3. What makes a personal collection worth returning to?

### Evidence

- **Mixed material can matter more than a photo archive alone.** Petrelli and
  Whittaker's 2010 home memory tours/interviews involved 17 people from 13
  families and 169 objects. The objects' significance was often relational and
  idiosyncratic. That supports keeping heterogeneous material recognizable;
  recognizing its type cannot establish why it matters. This is qualitative,
  culturally bounded evidence from an earlier technology era, not a population
  estimate. [Family memories in the home](https://shura.shu.ac.uk/2907/1/PUC-journal-digitalVSphysical.pdf)
- **Stored does not mean findable.** A 2010 study of 18 professional parents
  used interviews and retrieval tasks for significant family events over a
  year old; participants failed to find almost 40% of requested pictures.
  This motivates delayed retrieval tests, not a claim about today's Photos
  apps. The sample was narrow and the study predates current search features.
  [Easy on that trigger dad](https://eprints.whiterose.ac.uk/id/eprint/10334/1/Clough_10334.pdf)
- **Remembering has several purposes.** Sellen and Whittaker's 2010 constructive
  critique distinguishes retrieval, recollection, pleasurable reminiscing,
  reflection and remembering intentions. Its lesson is to evaluate the intended
  benefit rather than total capture. It is a synthesis/critique, not a trial
  establishing consumer retention. [Beyond Total Capture](https://hci.stanford.edu/courses/cs247/2011/readings/sellen.pdf)
- **Others' contributions can change the value of the object.** Odom and
  colleagues' 2012 interviews with 13 people examined physical, local-digital
  and online possessions. Social context, control and boundaries complicated
  what possession meant. This supports preserving comments and authorship,
  not replacing them with one machine narrator. The study is exploratory,
  small and from an earlier cloud-service era. [Lost in Translation](https://www.microsoft.com/en-us/research/wp-content/uploads/2012/05/odom2012.pdf)
- **Accumulation has a maintenance cost.** A 2025 qualitative study of 12
  participants' deletion practices found effort, fear of loss and a range of
  emotions around reviewing/discarding personal photographs. It supports
  reversible control and evaluating clutter, not automatic deletion or a
  recurring cleanup assignment. [Challenging but satisfying](https://www.sciencedirect.com/org/science/article/pii/S0022041825000359)

### What the repository already answers

The [Life v1 contract](../contracts/life-v1-experience.md), lines 21–32, already
promises finding, understanding and using held material again without filing
work. Its thin/zero-record states at lines 161–174 reject prompts to enrich the
record. The collections decision already specifies many-to-many membership and
time-agnostic kept things. These are foundations to implement, not newly
discovered principles to duplicate in another canon.

### Recommendation

Distinguish four reasons to revisit in evaluation: **recover a particular thing,
enjoy re-encountering it, understand something new, and receive another person's
perspective**. They are not four required outputs or tabs.

The important nuance is that editorial novelty and personal value are different
tests. A new AI explanation should add something. A familiar photograph, a
friend's exact words, or an organized record can be valuable without a new
claim. Do not make collection browsing pass the same novelty gate as generated
editorial content.

Design the collection as an object with recognizable contents, navigable time,
people and place, clear provenance and stable ways back in. Test whether this
is worth possessing before assuming that a generated narrative is needed.
Beauty can improve recognition and enjoyment; visual polish alone does not
establish an advantage over the original apps.

**Disconfirming evidence:** people enjoy a demonstration but never return;
they cannot find a specific item later; or they prefer the original album or
message because Vesper obscures its context or adds maintenance.

## 4. Why contribute here rather than leave it where it already lives?

### The counterargument deserves equal weight

In the 2004 Keeping Found Things Found study, participants successfully returned
to at least 95% of sites when cued with descriptions they had made months
earlier; two-thirds of refinding methods required no explicit keeping.
Workplace web behavior and researcher-provided cues limit generalization, but
the result directly challenges the assumption that fragmentation always creates
pain. [Keeping and Re-Finding Information on the Web](https://www.microsoft.com/en-us/research/publication/keeping-and-re-finding-information-on-the-web-what-do-people-do-and-what-do-they-need-to-do/)

The earlier observational work also found that keeping methods differ in
whether they preserve relevance and remind people at an appropriate moment.
The opportunity is not simply to store in one place, but to preserve useful
context that the existing behavior loses. [Keeping Found Things Found, 2001](https://www.microsoft.com/en-us/research/publication/keeping-found-things-found-web/)

**Inference for Vesper:** an additional contribution has to earn its effort,
uncertainty and future maintenance cost. Easier ingestion improves that tradeoff
but does not establish desire. Connected inboxes can lower repeated effort while
also filling the product with irrelevant or incorrectly grouped material.

### Existing decision versus implementation

The September 27 decision already mandates private defaults, keep-first,
correction afterward, author payoff and in-place share-sheet completion. The
September 28 ingestion record explicitly calls its roughly two-second payoff
target unmeasured; its minutes-long pipeline description is a dated observation,
not a measurement rerun here.

At the inspected mobile revision,
[share-capture](../../travel-app/app/share-capture/index.tsx), around lines
402/435, contains `answer_only` handoffs, and around line 961 retains a
needs-review candidate branch. That is evidence of paths requiring alignment,
not proof that every active configuration follows them. The accepted composer
amendment—not an older blanket Ask rule—governs deliberate shares with questions.

### Recommended first-contribution comparisons

| Input | Benefit worth testing | Insufficient substitute |
| --- | --- | --- |
| A menu or dish photograph | Recognizable original plus supported useful details, easy to find again | Merely announcing that it is a photograph of food |
| A friend's recommendation | Recoverable place/link with the permitted original context | A second generic place bookmark stripped of the friend's contribution |
| A ticket screenshot | Readable practical information and a stable return path | A receipt saying only that upload succeeded |
| A few mixed items from an evening | A coherent bounded collection with recognizable relationships | An import count or request to write a reflection |
| A contribution to a shared collection | Visible placement and preserved authorship | Requiring another participant to reply or contribute before value appears |

These are proposed treatments, not claims of current recognition accuracy.
Show the same input in the participant's existing tool and in Vesper; do not
compare a carefully prepared Vesper result against an intentionally poor control.

The 2019 Human-AI Interaction guidelines support legible capabilities,
uncertainty handling and easy correction. Their validation included 49 design
practitioners evaluating 20 products; they are design guidance, not evidence
that an extra confirmation or its removal universally improves conversion.
[Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/research/wp-content/uploads/2019/01/Guidelines-for-Human-AI-Interaction-camera-ready.pdf)

**Open decision:** the minimum satisfying transformation differs by input.
Measure it rather than requiring a generated insight for everything. A receipt
establishes trust in persistence; it does not by itself prove consumer value.
Likewise, “documenting” may be the internal behavior model without being the
phrase that makes a newcomer want to participate.

## 5. Which connections are worth receiving?

### Research suggests separating novelty, substance and timing

A three-case sensemaking analysis distinguishes finding evidence from
reorganizing it and choosing representations. Applied to Vesper, a reconstructed
sequence or well-chosen comparison can contribute more than a retrieved
paragraph. The original work concerns expert information tasks, so the consumer
application remains an inference. [Russell and Stefik, 1993](https://www.markstefik.com/wp-content/uploads/2014/04/1993-Sensemaking-long-Stefik-Russell.pdf)

A study using 2,300 judgments across 92 queries from 36 Microsoft employees
found that some results were interesting despite weak query relevance. That
supports distinguishing material worth exploring from material worth showing
now; it does not prove that unsolicited interruption is helpful.
[André, Teevan and Dumais, CHI 2009](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/chi09-serendip.pdf)

There is a countervailing risk: a preregistered 2025 experiment with 180
participants compared honest/misleading summaries and chatbot discussion after
reading articles. Misleading chat increased false recollection. This does not
estimate the risk of an ordinary Vesper deployment, but warns against treating
a persuasive explanation as proof of accurate remembering.
[Slip Through the Chat, IUI 2025](https://dam-prod.media.mit.edu/x/2025/08/25/IUI-2025-Slip%20Through%20the%20Chat.pdf)

### The repo is already specific here

The [August 29 contribution briefs](life-editorial-contribution-briefs-and-treatment-evaluation-2026-08-29.md),
around line 103, reject merely returning the founder's Colosseum/Troy connection.
Their proposed addition is the Iulus–Julian/Augustan lineage mechanism, with
the original observation credited separately from researched explanation. This
report evaluates that specimen's structure; it does not freshly certify its
historical claims.

The [post-return manuscript](life-canonical-post-return-new-york-experience-manuscript-2026-08-29.md),
around lines 407–459, develops the cultural and Rome–Paris treatments. Crucially,
the Paris/Maya branch is explicitly synthetic. The contribution brief withholds
real-world promotion without authorized friend evidence and bounded dates.
It is not evidence that a real recipient enjoyed this comparison.

The [September 7 organizing research](life-organizing-intelligence-technical-research-2026-09-07.md),
around lines 332–338, already separates exact retrieval from added substance and
proposes known-link, useful-analogy, unsupported-link and forbidden-link cases.
Reuse this work rather than create another parallel evaluation philosophy.

Actual backend safeguards include:

- [known_to_person.py](../../travel-agent/backend/root_projection/v2/known_to_person.py):
  bounded exact/near-lexical checks against authorized known claims, not a model
  of everything the person knows;
- [source_contribution.py](../../travel-agent/backend/root_projection/v2/source_contribution.py),
  lines 387–425: rejects known claims relabeled as new and unsupported personal
  inference, and requires an additional Vesper claim for generated contributions;
- [known-claim tests](../../travel-agent/tests/root_projection/test_known_to_person.py),
  around lines 38/65: distinguish additional predicates and changes to negation,
  amounts, time and direction. These tests were read, not executed here.

This is real architectural progress. Lexical novelty still cannot establish
intellectual novelty, relevance or truth. A distant paraphrase can be empty;
a new predicate can be wrong. Conversely, human-authored material need not
pass the generated-content novelty requirement.

### Recommendation

For the same authorized material, compare three versions: **the original,
attributed juxtaposition, and juxtaposition plus Vesper's explanation**.
The third should earn its additional space. Sometimes the friend’s exact
contribution is the best result.

Ask what was genuinely added, what was already known, whether the evidence
supports the comparison, and whether the result belongs here now. Do this in
research sessions, not as routine homework inside the app. Include ordinary
food, hobbies and daily life—not only the founder's unusually rich travel corpus.

## 6. What does multiplayer add beyond private memory?

**The strongest hypothesis is additional substance, not additional distribution.**
A photograph someone else took, a recipe they brought, or their different
account of the evening can change what the collection lets people revisit.
Forwarding a generated answer distributes an output; it does not necessarily
create this continuing shared object.

### Supporting evidence and tensions

Broekhuijsen's 2018 thesis combines three qualitative design studies of photo
practices and shared remembering. It argues for curation within the social
practices that motivate it, rather than organization as separate preparatory
work. Remote, mixed-media AI collections are an extrapolation beyond its photo
and co-located emphasis. [Curation-in-Action](https://opus.lib.uts.edu.au/handle/10453/129375)

Grudin's historical groupware analysis highlights mismatches between who does
the work and who gets the benefit. Asymmetric contribution can be healthy, but
the organizer's effort must be counted rather than made invisible. This is
workplace-system analysis, not a consumer social experiment.
[Groupware and Social Dynamics](https://bpb-us-e1.wpmucdn.com/blogs.cornell.edu/dist/4/2619/files/2016/07/grudin_EightChallengesForDevelopers-1nwclfd.pdf)

Lobinger and colleagues' qualitative research comprised 34 interviews, including
eight paired interviews, concerning friendships and romantic relationships.
Trust and assumptions about redistribution mattered to photo sharing. Its
purposive German sample does not establish prevalence, but motivates an important
Vesper test: casual sharing may become less comfortable when people expect
lasting organization or reinterpretation. [Photo-sharing boundaries, 2017](https://firstmonday.org/ojs/index.php/fm/article/download/7860/6327)

Thus persistence can increase the value of remembering while reducing the ease
of contributing. Removing public metrics does not automatically remove pressure.
People may still feel obliged to reply, appear interesting or match a friend's
effort. These are hypotheses to test, not diagnosed behavior in Vesper users.

### Existing direction and actual implementation

The accepted multiplayer decision already preserves people's words, private
Keep, no public like counts, bounded audience and contributor withdrawal. The
collections decision makes adding an act of sharing and shared collections
whole-visible. These are not blank-sheet questions.

[The Places social adapter](../../travel-agent/backend/root_projection/v2/adapters.py),
around lines 1247–1314, builds two attributed perspectives and explicitly avoids
claiming consensus. However, [its contract fixture](../../travel-agent/tests/root_projection/test_v2_contracts.py),
around line 1509, uses “Mara shared 1 place” and “Jon shared 1 place.” That can
prove structure and destinations; it cannot prove a meaningful juxtaposition.
High evidence/yield signals assigned by the adapter are not human evaluation.

[Relationship models](../../travel-agent/backend/domains/relationships/models.py),
around lines 110/153, provide exact-original recipient grants and place-based
handoffs. They are useful primitives, not proof that the newer general
share/audience/collection model is fully delivered. Visibility also does not
automatically authorize AI synthesis of a friend's words; the decision's
use-grant amendment remains a separate implementation prerequisite.

### Recommendation

Study real pairs or small groups with a frequent contributor, an occasional
contributor and a mostly receiving participant. Assess each separately:

- Is it easy and worthwhile to offer one thing?
- Can someone enjoy receiving without building a history or reciprocating?
- Does the collection preserve recognizable authorship and disagreement?
- Does it create an opening for human contact or an offline experience when
  appropriate, without prescribing contact as the required outcome?

Do not require a social graph before solo value exists, or equal effort before
social value exists. Preserve friends' actual voices; don't make AI commentary
the price of seeing them.

## 7. Can the architecture preserve meaning as memory changes?

**The inspected architecture is compatible with this direction.** It already
separates sources, occurrences, outcomes and projections. The main research
implication is to verify connected guarantees, not replace those owners with
a universal memory table.

W3C PROV offers a useful technical precedent for distinguishing entity,
activity, agent, attribution, derivation, revision and invalidation. It is a
vocabulary, not an implementation of Vesper's permissions or repair behavior.
[PROV-DM](https://www.w3.org/TR/prov-dm/)

### Identity: preserve existing distinctions

[The intake writer](../../travel-agent/backend/core/db/intake_v2.py), lines
530–545, explicitly uses `(owner_id, idempotency_key)` for retry identity and
rejects content hashes as a substitute because identical bytes can represent
different intentions. The replay branch checks the request before returning
the original submission. [Entity identity](../../travel-agent/backend/core/db/entity_identity.py),
lines 41–91, separates verified global mappings from owner mappings and disallows
last-writer-wins remapping.

These are safeguards to retain. They do not yet prove that an email and a
screenshot of one ticket converge into one artifact with two sources. Retry,
source, subject, occurrence and contribution identities need explicit relations;
“same thing” is not precise enough as an engineering merge rule.

### Five change cases

| Case | Inspected support | What still needs connected evidence |
| --- | --- | --- |
| Same restaurant twice | `life_projection/evidence_organization.py:149–164` preserves separate evidence identities; lines 249–270 refuse to treat a ticket alone as occurrence | Real recognition and display from ambiguous photographs/notes, not only pre-labelled events |
| Conflicting friends' accounts | `core/models/experience_graph.py:316–327` gives Outcomes authors, sources, visibility and revision; original delivery preserves sender and exact source selection | Two opinions remain attributed; factual disagreement does not silently become last-writer-wins truth |
| Explanation five days later | `lived_experience/lineage.py:32–66` carries causal identifiers; `life_projection/current_authority.py` rehydrates owner truth | The earlier basis, current correction and unavailable-source state remain intelligible without retaining unauthorized material |
| A ticket changes | `domains/experience_graph/occurrence_commands.py:45–118` supports grounded evidence and checked supersession | Operational change reaches the correct reservation owner and dependent views; purchase/schedule never becomes attendance by implication |
| A shared contribution is deleted | `core/db/intake_v2.py:903–1043` scrubs source data, invalidates dependents and revokes handoffs; original delivery rechecks current eligibility | Relevant caches, screens and pending outputs converge while independent material remains intact |

All paths in the table are under `travel-agent/backend/`. These are static
observations, not newly executed end-to-end proofs.

The [organization holdout fixture](../../travel-agent/tests/life_projection/fixtures/organization_holdouts_v1.json),
around lines 103–122, explicitly exercises two meals at the same restaurant.
[Its test](../../travel-agent/tests/life_projection/test_life_organization_holdouts.py),
lines 85–126, checks required/forbidden relations and labels the evidence as
oracle-based rather than human-value or serving evidence. This is a particularly
good foundation: the missing question is whether the input producer supplies
reliable distinctions, not whether the compiler has any such concept.

[Original-delivery repository](../../travel-agent/backend/domains/relationships/original_delivery_repository.py),
lines 399–435 and 459–528, contains current-authority checks and withdrawal /
revocation paths. [Postgres tests](../../travel-agent/tests/domains/relationships/test_original_deliveries_postgres.py),
around lines 69/361, define recipient/revision and API/Home coverage; they were
not run. The [repair gateway builder](../../travel-agent/backend/lived_experience/repair_gateways.py),
lines 52–70, names bounded repair families, not proof of universal repair.

Vesper can control governed pointers and future derived views, not erase
screenshots or external copies. Apple's Shared Albums similarly distinguishes
album deletion from copies already saved to another library. This is a practical
limit to explain, not a reason to abandon in-product withdrawal.
[Apple Shared Albums](https://support.apple.com/en-us/108314)

### Collections are the key mapping task

The existing [collections CRUD](../../travel-agent/backend/core/db/collections.py),
lines 1–10, explicitly serves editorial Discover/Guides collections. Its name is
not evidence that it implements the September 28 personal/shared collection.
Life organization has separate derived grouping and current-owner read paths.
Map the consumer object onto these owners deliberately; do not simply rename
an editorial collection or turn a read projection into mutation authority.

The [root-projection feature contract](../../travel-agent/backend/root_projection/FEATURE.md)
marks the pipeline experimental/rollout-gated. Mobile
[product-system rollout](../../travel-app/utils/productSystemRollout.ts),
lines 36–69, retains local/internal restrictions and `releaseEligible: false`;
[Life refinding](../../travel-app/utils/lifeRefindFlag.ts), lines 7–23, is also
opt-in. These observations preclude claiming this research demonstrated the
experience in an installed production app.

## 8. Why choose—and pay for—Vesper in ordinary life?

### The competitive baseline is stronger than an empty chatbot

Official pages checked September 28 show substantial overlap. Prices below are
published offers in USD, not observed transaction prices, retention, revenue
or willingness to pay for Vesper.

| Alternative | Documented offer | Implication |
| --- | --- | --- |
| [mymind](https://mymind.com/) | AI-assisted organization, type-aware presentation, Smart Spaces and rediscovery | Automatic organization and beautiful saving are not a unique position |
| [Are.na](https://www.are.na/about) | Mixed-media channels, reconnecting content, private/shared collections and export; Premium $70/year or $7/month | Connected collections and collaborative knowledge are already a product category |
| [Fabric](https://fabric.so/pricing-and-plans-for-individuals) | Notes/files/bookmarks, intelligent memory and collaboration; annual-billed Plus $96/year, Pro $216/year | Broad information plus AI is not by itself a distinct consumer promise |
| [Day One pricing](https://dayoneapp.com/guides/premium-subscription/day-one-pricing-features-guide/) | Silver $49.99/year; Gold $74.99/year adds AI features; basic export remains available | Personal record and AI enhancement already coexist in paid offers |
| [Day One Shared Journals](https://dayoneapp.com/guides/shared-journals/shared-journals/) | Current guide says free users can create shared journals with attributed contributions | Multiplayer memory alone is neither an empty category nor automatically a paid advantage |
| [Apple Shared Photo Library](https://support.apple.com/en-au/118229) | Shared photographic library for up to six people | Combining a group's pictures must beat familiar existing behavior |

These are documentation comparisons, not hands-on product rankings. Day One has
changed pricing and editing rules; do not reuse older premium-host assumptions
or generalize a permission detail across platforms without checking it.

### Proposed advantage to establish

The opportunity is a particular combination: ordinary mixed material becomes
recognizable, related to lived time/place and other people's contributions,
revisitable without filing, and useful when circumstances change. The experience
must demonstrate this combination without asking newcomers to understand the
whole underlying system.

The best initial audience hypothesis is behavioral, not universal: people
already collecting or sharing fragments across formats who experience a real
gap when returning to them. Compare them with people satisfied by Photos,
messages or notes. Do not assume all travelers, all AI users, or all people
with large libraries share the need.

The personal archive is not a new technical invention. Microsoft's
[Stuff I've Seen](https://www.microsoft.com/en-us/research/publication/stuff-ive-seen-a-system-for-personal-information-retrieval-and-re-use/)
evaluated unified refinding among more than 230 employees and highlighted time
and people as useful cues. It supports testing those access paths, not consumer
demand for Vesper. [MyLifeBits](https://www.microsoft.com/en-us/research/publication/mylifebits-a-personal-database-for-everything/)
explored heterogeneous personal material and links much earlier; Vesper's
selective, consumer-facing experience has to earn its own advantage.

### Commercial and cost research still needed

Test payment after a participant has received a complete benefit and can name
what they would miss. Compare willingness to continue using the experience
with willingness to pay; neither follows from admiration for a mockup.
Membership for additional capacity, depth and assistance remains a hypothesis,
not a price selected by this report. Include the economics of thin recipients:
social value should not require every invited person to become a paying power
user, but who funds their service remains a packaging question.

Measure full workload cost: recognition, retries, storage, indexing, research,
generation, revisions, repair and later reads. The shared
[LLM wrapper](../../travel-agent/backend/core/llm.py), around lines 728–765,
records usage/cost, and [contribution telemetry](../../travel-agent/backend/root_projection/v2/source_contribution_telemetry.py),
around line 114, includes a cost class. Instrumentation is not a measured
cost per satisfied or retained user. No margin estimate was produced here.

**Proposed operating principle:** invest generation where it adds value;
reuse stable extraction, render originals and deterministic organization when
sufficient, and invalidate only affected derivatives. A rich product need not
generate a new essay for every item or every visit. This should be tested for
quality and measured cost, not adopted as an unexamined cost-cutting rule.

## 9. What recent 2026 literature adds—and does not

These additions prevent the review from relying only on older HCI work, while
preserving the distinction between a research prototype and a viable product.

- **MemoryDiorama, April 2026 preprint:** an 18-person within-subject study
  compared photographs, static dioramas and dynamic mixed-reality dioramas.
  Richer cues increased reported/detail measures, but the authors did not assess
  memory accuracy or false-memory formation, and different events introduce
  confounds. Lesson: richer presentation is worth exploring, but vividness is
  not truth or evidence of retention. No 3D-generation feature is recommended
  by this result. [Paper and limitations](https://arxiv.org/html/2604.06773v1)
- **Mi-Memory, July 2026 technical report:** treats memory as a lifecycle with
  provenance, diagnosis, update/forgetting and deployment constraints. It
  explicitly separates controlled benchmark results from preliminary and
  design-only components. Lesson: trace where useful evidence is lost between
  ingestion and receiving; do not infer complete user-facing memory from a
  retrieval score. This is not proof that Vesper should adopt its framework.
  [Technical report](https://arxiv.org/html/2607.18975v1)
- **ReaLMem, September 2026 preprint:** uses multi-year personal visual archives
  from seven participants, with owner annotations, to evaluate recall and
  personalization. It exposes limitations beyond factual retrieval but has a
  small, unusually rich-history sample. Lesson: evaluate temporally related
  material, while separately testing sparse first use. Its persona-inference
  tasks do not authorize Vesper to infer personality or preference against its
  own rules. [Paper and limitations](https://arxiv.org/html/2609.19167v1)

Collectively, these papers support better multimodal and longitudinal evaluation.
They do not remove the need to observe whether people want Vesper's specific
experience, or establish that a model's interpretation should become personal
truth.

## 10. How this fits the whole product

Making memory first-class must not mean hiding it in Life while Home and Places
remain unrelated assistant feeds. The same recognizable material should support
different reasons for entering the product.

| Surface | Recommended expression of the shared center | Avoid |
| --- | --- | --- |
| Chat and other input doors | Ask, contribute, correct and work with a thing; immediate useful response | Mandatory chat before every capture, or a classification conversation |
| Life | Stable collections, original material and paths through time, people and place | Filing dashboard or AI personality biography |
| Home | Valuable contributions and warranted returns connected to present life; timely practical help | Obligatory reflection, an endless recent-trip recap, or novelty manufactured on refresh |
| Places | The spatial reading of personal/shared material alongside relevant world information | A disconnected generic recommendation directory |

These are orientations, not one product move per tab. A collection can be
encountered through Home or Places and explored in Life without becoming
three copies. The live engine continues to help when time, availability,
commitments or conditions change; it does not need to manufacture a Plan from
every contribution to justify its existence.

The system can remain broad while the interaction becomes simpler:
**bring something; receive something worthwhile; return or continue when useful.**
The user need not know which service produced the benefit.

## 11. A bounded research and implementation portfolio

This is a proposed portfolio for the existing roadmap owner, not a new dispatch
queue. Use a small set of complete experiences to exercise the shared system;
do not mistake them for the limits of the product.

### A. First-object and revisit study

Compare the same newly encountered material in the person's existing app and
in a Vesper treatment. Include a photograph, practical screenshot and friend
recommendation. Use their own material with permission; require no backfill,
tags or journaling. Distinguish:

- time until the person can explain what useful thing they received;
- understanding of what was kept and who can see it;
- prompted delayed refinding versus spontaneous returning;
- voluntary second contribution versus research-requested capture;
- pleasure, understanding and practical usefulness as separate outcomes.

Include thin records, richer records, people satisfied with current tools and
people who abandon the prototype. Do not generalize founder enthusiasm or
survivor interviews into demand. A prototype study evaluates the presented
experience; it does not certify production extraction accuracy or latency.

### B. Connection and social comparison study

Use originals alone, attributed juxtaposition and juxtaposition plus explanation.
Include useful, merely coincidental, already-known and unsupported connections.
For social cases use real consenting pairs/groups, with a mostly receiving
participant. Record contributor effort separately from recipient benefit.

Success need not be a message, a plan or a booking. Recognition, enjoyment and
refinding can finish the experience. Still record whether an optional opening
actually helps people reconnect or do something together; do not count opening
an invitation as attendance.

### C. System cases to run as the implementation matures

| Case | What it tests | Evidence boundary |
| --- | --- | --- |
| One menu/photo, almost no history | Immediate useful representation without identity inference | Real extraction plus participant comprehension |
| Same subject, two separate visits | Subject identity does not collapse occurrences | Ingestion → persisted evidence → Life/Places rendering |
| Same ticket through two doors | Cross-door convergence preserves both sources without replay duplication | Backend identity assertions plus consumer readback |
| Day 1 photo, day 2 explanation, day 5 related material | Later evidence changes the right relation without rewriting original authorship | Delayed read, updated view and inspectable provenance |
| Two people, different accounts of an evening | Plural meaning and exact human voice survive composition | Pair comprehension plus source/authority checks |
| Quiet week and a sparse record | Value without trip density, a social graph or daily prompts | Unprompted behavior, with prompted tasks reported separately |
| Changed reservation | Live practical help remains part of the same experience | Operational-owner truth and relevant surface changes |
| Wrong grouping, removed item, withdrawn friend contribution | Correction changes dependent views without erasing independent material | Owner mutation, caches, pending outputs and real readback |

Reuse existing fixtures and novelty/repair suites where possible. Add missing
cases at the relevant owners; avoid creating a new evaluation service solely
for this research. Human comprehension, deterministic correctness and installed
experience are different evidence layers and should remain distinguishable.

### D. Commercial and service study

After complete benefits exist, ask participants to choose between continuing
with Vesper and their current behavior, then evaluate a clearly specified paid
offer. Report actual payment separately from hypothetical willingness. Track
service costs across thin recipients, regular contributors and burst importers.

Do not use daily active usage, number of stored artifacts, generated words or
clicks as a substitute for value. A low-frequency product can still be valuable;
its costs and willingness to pay have to support that cadence.

### Decision ledger

| Hypothesis | Evidence that would strengthen it | Evidence that should change our approach |
| --- | --- | --- |
| Collections are an intrinsic reward | People choose to keep/revisit them without being asked to act | Attractive screenshots but no later preference over existing tools |
| Contribution earns its effort | Voluntary second contributions after a thin first payoff | Dependence on repeated capture prompts or heavy initial imports |
| Connections add substance | People identify a supported distinction not present in the originals | Generic prose, obvious callbacks, or better results without the AI paragraph |
| Multiplayer improves the experience | Contributors and mostly receiving participants each report concrete benefit | Organizer-only benefit, reciprocity pressure or discomfort with persistence |
| Existing architecture can support the center | Mutation cases pass from real input through all affected reads | Recurring identity loss, stale projections or authority workarounds |
| Membership can fund the service | Repeat choice, paid uptake and measured sustainable workloads | Payment depends on promises not delivered, or frequent generation costs exceed viable revenue |

These are directional criteria, not fabricated numerical thresholds. Set actual
study sizes and acceptance thresholds before collecting results, using the
available service and the decision each study must support.

## 12. What should change in our documents next?

This report changes no product policy or runtime behavior. It identifies the
following bounded reconciliation work rather than recommending another canon.

1. **Product Thesis and Product Model:** deliberately reconcile first-class
   visible memory with older language such as “not … memory collection” and
   “Memory is substrate, not the endpoint” (Thesis lines 25–28 and 64–67).
   Preserve their strong authority, plural-outcome and non-mandatory-loop rules.
   Do not replace them silently through this working research.
2. **Contribution and Life owners:** incorporate explicitly accepted September
   27–28 amendments where older entrance/Threads wording remains. Keep unruled
   friction presets, zero-touch type promotion, notification defaults and
   friend-content AI use separate. Accepted amendments apply only to their
   named scope, not all casual questions.
3. **Editorial/experience evaluation:** retain the high bar for generated
   additions while explicitly protecting familiar-original, retrieval and
   shared-human value. The Editorial Canon already distinguishes those lanes;
   correct misapplied tests rather than invent a weaker novelty standard.
4. **Existing implementation packages:** add owner mapping for the new
   collection promise, cross-door identity cases and delayed correction/readback
   where missing. Preserve tested distinctions instead of rebuilding them.
5. **Commercial research:** replace generic-agent comparison alone with the
   actual alternatives—Photos, messaging, connected collections, journals and
   AI organizers. A differentiated combination remains a hypothesis until
   people prefer the delivered experience.

## 13. Closeout and promotion

Documentation verification in the recorded workspace lane:

- `git diff --check`: passed.
- `python3 scripts/check_doc_governance.py docs/working/memory-as-product-direction-research-2026-09-28.md docs/working/product-direction-2026-09-28.md`:
  passed for both named documents.
- `python3 scripts/check_docs.py --inventory --links`: inventory passed;
  repository-wide links failed on the same 22 previously observed missing
  targets in other documents. No findings named this report or its parent note.
- No application/runtime tests were run; this is a documentation/research change.

Before October 28, promote only explicit decisions into their existing owners,
attach newly collected evidence to the relevant package, and archive or renew
this research with a concrete remaining question. The
[program roadmap](vesper-program-roadmap.md) remains the implementation queue.

Bottom line: the evidence favors making the connected record tangible and useful,
not expanding the list of agent capabilities. The largest uncertainty is no
longer whether the philosophy can be stated coherently. It is whether ordinary
contributions reliably become something a person prefers to have, return to,
and sometimes share with others.
