---
doc_type: working
status: active
owner: founder / cross-repo architecture / program roadmap owner
created: 2026-09-29
last_verified: 2026-09-29
expires: 2026-10-13
why_new: The strategy handoff names three artifact workstreams but cannot hold their detailed contracts, dependencies, migration, evaluation and delivery sequence without becoming a second general roadmap. This bounded supporting plan expands that section for the existing program owner.
supersedes: []
source_of_truth_for: []
---

# Artifact experience engineering roadmap

Vesper should turn an ordinary contribution into a recognizable thing worth
keeping, opening and returning to. Around that stable object, the system can
offer worthwhile connections to personal material, collections, other people
and the changing world. Intelligence must add substance without requiring a
conversation, a rich history, or more documentation work.

This roadmap turns the September 29 artifact investigations into coordinated
engineering packages. Build on existing custody, owner references, composition,
retrieval, jobs and native readers. Add the missing identity, selected-part,
collection, saved-edition and discovery contracts deliberately. Do not create
another assistant or a universal artifact service.

**Execution status:** planning only. No package below is declared implemented,
scheduled or accepted by writing this document. The
[program roadmap](vesper-program-roadmap.md) retains the sole dispatch queue.
The [strategy handoff](roadmap-proposals-for-codex-2026-09-28.md#9-focused-artifact-engineering-proposals)
is the admission path into the active delivery lane. Preserve its unfinished
capture, signing, authenticated readback, Home and sharing work. The program
owner can absorb these packages into that work rather than restart it.

**In brief.**

- **What to build first:** the thing's identity (P1), catalog anchoring (PC)
  and native readers (P2), for the families already designed: tickets,
  venues, and books, films, shows and music.
- **What comes later:** discovery of additions (P3), exact kept editions (P4)
  and selective refresh (P5). P3 starts thin; saved editions and broader archive
  maintenance wait until additions have shown people value. Original-record
  correction belongs in P1; permission, publication and spending safeguards
  accompany the first live discovery, not a later hardening phase.
- **The object comes first.** Original access and an honest useful fallback
  must not wait for catalog resolution or generated enrichment. Recognition
  may use a model; its latency and failure must not block original access.
  The design reference is the Vesper — Artifacts Claude Design project
  (section 1A).
- **World things are anchors; the person's things attach to them.** A venue,
  film, book, show, album or course has one standard face; the ticket, dish,
  photograph, note or reading attaches to it.
- **Sharing originals is not downstream of generated editions.** Eligible
  attributed-original sharing and receiving advance with the relevant identity,
  reader and sharing contracts. Generated derivatives have later dependencies.
- **One open decision** gates real art and live venue facts: which catalog
  sources to license (section 6).

## 1 Product outcome and boundaries

The complete experience has several independently valuable outcomes:

1. A ticket, photograph, passage or practical record becomes recognizable,
   attractive and inspectable, preserving the original and personal details.
2. The person can open the thing or a meaningful part of it, without Chat as
   an admission fee or a generic subject page replacing their own material.
3. Vesper can present an actual useful addition: another original, a precise
   comparison, a sourced explanation, a map or an appropriate practical option.
4. An explanation deliberately kept can be reopened exactly. New context
   does not silently rewrite it.
5. Collections and the four roots expose the same identities. A related-object
   detour returns to what the person was reading.
6. Corrections, source loss and audience changes repair dependent results.
   Repeated unchanged opens do not require new generation.

These are capabilities, not a compulsory funnel. Original-only, retrieval,
enjoyable juxtaposition and practical relief can each complete the value.
The system should sometimes produce strong enrichment and sometimes add nothing.
It must not optimize for more captures, generated paragraphs or daily returns.

Plan against several artifact families from the start. The first implemented
family must not dictate all identities, media or evidence rules. A source-bound
fallback should remain useful when a specialized treatment is unsupported.

### Accepted direction

- [One composer](../decisions/2026-09-27-documenting-core-loop-and-one-composer.md)
  owns deliberate capture and sharing; Chat is one door. A deliberate composer
  share with a question is Bring plus Ask, with the named Ask-only escape.
- [Collections](../decisions/2026-09-28-collections-are-the-spine.md) have
  many-to-many membership. Remove from one collection is not Delete everywhere;
  deleting a collection does not delete its things.
- [Ingestion](../decisions/2026-09-28-ingestion-and-connected-inbox.md) requires
  the same ticket across email and screenshot to resolve to one thing retaining
  its sources. Separate contributions and occurrences remain separate.
- [Life](../decisions/2026-09-29-life-model-occasions-collections-and-sharing.md)
  treats occasions as things holding originals and spans as collections. A
  shared collection has no per-item private layer. A viewer's personal back
  must not leak into shared notes or synthesis. Leaving takes the contributor's
  things out; composite derivatives still require a precise policy.
- [Record value](../decisions/2026-09-29-record-as-first-class-value.md) is a
  first-class benefit. Every artifact need not produce a novel insight or action.

Older contracts remain authoritative except where those accepted amendments
explicitly change them. Do not reinstate an old Ask rule or reopen settled
collection behavior from an earlier research note.

### Not authorized by this roadmap

No booking execution, mailbox-wide retention, autonomous sharing, background
location tracking, automatic personality inference, new billing policy, or
launch exposure follows. Connected-inbox material remains private under the
accepted restriction until the relevant provider policy is resolved.

The open catalog mechanism, save-on-share proposal, automatic shared additions,
notification defaults, shared saved-derivative policy and offline retention
promise remain separate decisions. The plan does not adopt them implicitly.

## 1A Design alignment, September 29

Added after the evening design review in the Vesper — Artifacts Claude Design
project (`81acdbcf`). These boards are the visual and interaction reference for
P2 and the forms PC must supply data for. They are design direction, not
measured user preference.

| Board | What it settles |
| --- | --- |
| `A2 - Kinds, first pass` | Tickets, places, books, films, shows and music in one flat language |
| `A3 - More tickets, more places` | Fifteen ticket kinds in four groups (travel, events, entry, stays and tables) and eleven place kinds with kind-specific facts |
| `A4 - Books, films, shows, music` | Real catalog art first; a uniform house design per medium as the fallback |
| `A4b - Film, house design` | The film fallback: the billing-block design (1b), with aspect ratio, film strip and slate kept as alternates |

The Life project (`e72a2fd2`) boards T1 (the thing's page), K1 (the collection
page) and S1–S2 (sharing and receiving) draw the surrounding pages.

- **One visual language.** Everything follows the Life ticket component: a
  cream surface with a soft shadow, a mono kicker and date, one serif hero,
  mono labels over values, hairlines, one accent. It carries no ornament, 3D,
  texture or handwriting.
- **Each thing takes its own real-world form.** A ticket stays a ticket. The
  festival wristband, the hotel key card and the dinner reservation (with the
  time as its hero) get their own silhouettes. Place cards carry facts, not a
  map.
- **Anchors and attachments.**
  - A venue, film, book, show, album or course is a subject with one
    standard face. This is section 3's Subject.
  - The person's things attach to it: a ticket, a dish as a standard menu
    item, a photograph clipped to the dish rather than serving as its face, a
    friend's note beside it, a reading as progress.
  - P2 must open anchors as pages as well as things.
- **Media formats differ by medium.**
  - Books: 2:3 covers.
  - Films: 2:3 posters.
  - TV: 16:9 key art. This is the frame streaming apps use; square season art
    crops badly.
  - Music: square art, with the record sliding out of the sleeve.
- **The house fallback is uniform within each medium:**
  - books: a white, typeset edition;
  - films: the billing block;
  - TV: a 16:9 title card;
  - music: a plain sleeve.

  None of them uses generated imagery.
- **First families.** The designed families come first, and dish, recipe and
  scorecard follow:
  - tickets (admission and travel);
  - places (venue anchors);
  - works (books, films, shows, music).

  P0's fixtures should cover the designed families as well as the passage and
  practical-record cases.

## 2 Evidence baseline and current foundation

The detailed September 29 inspections used the active delivery checkout
`travel-workspace--home-value-delivery`, not the older canonical main checkout:

| Repository | Inspected revision | Later bounded delta check |
| --- | --- | --- |
| Workspace | `97fcfc101978e7ecfb399278f36afcb52b6d7652` | `55d83029821e80df8e27195913028fcd6fe0ddea` |
| Backend | `1c0b5da7e19fe59cafffc9309e7c8140ef9327d2` | `fead707fb16a42ca9295960566b62771a114f375` |
| App | `677dc378152850c2ff9cf6cd7530dd6c0d7e7f58` | `212b87a4137aaff1a95ae045c52e7157d229afa4` |

The committed delta was hook/CI tooling, not artifact runtime changes. The
backend also had concurrent fixture-map and retained-source-projector test
edits at the later check; neither was changed or tested by this investigation.
Recheck actual HEADs and dirty work before implementation. The newer strategy
decisions and notes include uncommitted work; they are not evidence of runtime
conformance or a landed migration.

A later verification-instruction check used backend `e8bbb03a769ffc7a0072d5153673a3867fb2caae`
and app `212b87a4`. It confirmed the newer child static/bounded-merge commands
recorded in section 9. This was a command-policy check, not another full product
audit or an executed merge gate.

| Area | Reusable implementation found | Remaining boundary |
| --- | --- | --- |
| Capture and originals | Intake custody, idempotent commands, provisional observations, original media access and artifact read projection | Cross-door thing identity, stable subparts and all-door authenticated native acceptance are not established by those primitives |
| Focused reading | Source result reader, original readers, exact result reference, related navigation infrastructure | User-owned kept editions and complete expiry/action behavior need work; exact workflow readback is not permanent saved-expression ownership |
| Retrieval | Atlas dense and lexical retrieval with rank fusion and user filtering | Indexed title, one-line summary and Place label do not cover every original, passage, detail or collection relation |
| Contextual selection | Governed bounded Source discovery and approved source-pair selection | Place-centric pairs and the current two-source Home requirement are not general artifact exploration |
| Production | Shared model wrappers, bounded attempts, leases, cooldowns, retained results and read-time eligibility | Selected-object entry, complete influence lineage, policy-authorized preparation and user-owned persistence need explicit integration |
| Change handling | Life transactional outbox, current-authority readers, owner fences, repair and publication patterns | Artifact candidate-set progress, negative selection invalidation and end-to-end lifecycle coverage need integration |
| Evaluation | Editorial judge/fixtures, retrieval metrics, lifecycle tests and registered native QA | No executed artifact-specific connection comparison, human preference study or cost/latency measurement was produced by this research |

Representative code and test locations are collected in section 12. A test
read during research is a defined check, not a passing result.

## 3 Shared architecture contract

The following are proposed mappings to resolve in package P0. They are not new
wire models or permission to create a table for every row.

| Responsibility | Minimum distinction | Owning boundary |
| --- | --- | --- |
| Original | Source ID, content/custody revision, author, received time and permitted uses | Intake and Source custody |
| Recognizable thing | Stable owner reference, provisional/corrected fields, reversible representation links | Existing domain owner plus a reviewed thin reconciliation mapping where needed |
| Selected component | Stable component ID and source-revision-bound locator | Source/Intake evidence adapter, shared with composition and readers |
| Subject | Film, book, dish or Place identity | Entity/domain owner; not an occasion or attendance claim |
| Occasion and occurrence | A bounded occasion, original contributions, separately supported event claims | Experience Graph and existing operational owners |
| Collection membership | Thing reference, contributor, revision, removal/exclusion and audience consequence | Consumer collection owner; not the editorial guide collection table |
| Contextual selection | Selected target, viewer/purpose, candidate scope, context revision and eligible result references | Existing context/discovery owner |
| Prepared result | Exact generated output, input manifest, method version and current eligibility | Existing production/composition lifecycle |
| Kept edition | Exact chosen expression, stable edition reference and governed availability | Explicit saved-composition persistence owner |

### Identity and selection

Retry identity, byte identity, thing identity, subject identity and occurrence
identity are different. Two admissions in one image need addressable parts;
two screenings of one film must not collapse. A photo, menu and receipt can
support one occasion without being duplicate sources.

Subjects retain stable application-owned references. Provider identifiers are
reversible mappings, not replacements for those references. P0 must specify how
cultural subjects fit the owner model, including a work versus a particular
edition or release. Work-level relationships can coexist with edition-specific
evidence; neither collapses a person's artifact or separate occurrence.

Selected parts need a bounded tagged contract: whole source, text range, image
region, and later timed media. Define text normalization, coordinate units,
image orientation and source representation revision. A locator is not the
component identity. Ambiguous or missing anchors become unavailable; they do
not silently select different material. Quote selectors themselves contain
source content and follow its custody and audience rules.

Reconciliation must be evidence-backed and reversible. Preserve distinct
source grants; merging identity does not union permission. Reference migration
must preserve old links through a reviewed alias or redirect, and reversible
split must leave each original addressable.

### Context and edition semantics

Use a selected-object context containing the owner reference, optional
component, originating collection, viewer/use scope, current purpose, and
relevant time/place. No fabricated Trip or chat session is required. Opening
establishes current attention, not a durable preference.

Keep three independent state axes:

- **Content validity:** supported, superseded, expired or currently inaccessible.
- **Selection freshness:** current, potentially outdated or discovery incomplete.
- **Preparation:** not requested, queued, running, ready, useful silence,
  rejected, failed or cancelled, mapped onto existing job states where possible.

These are semantic requirements, not instructions to invent three competing
state machines. A valid kept edition can coexist with a newer candidate. A
revoked result is not safe to show merely because regeneration is pending.

An edition's content does not silently change. Its availability can change
under correction and authority. Explicitly creating a replacement produces a
new version with lineage. Existing authorized preparation may run without a
Refresh tap; opening alone expands no audience, retention or action grant.

### Dependency and publication semantics

Record all supplied inference inputs with roles: factual support, selection
context, novelty history and policy. Displayed citations are only a subset.
Carry source/owner revisions, relevant grants, recipe/model/prompt versions,
candidate-scope revision, and relevant context/index progress.

A candidate-set dependency includes an empty selection. New relevant material
can invalidate that selection while its former winners remain unchanged.
Candidate arrival marks work eligible for reconsideration; it does not mandate
generation. Coalesce changes and reuse equivalent eligible results.

Keep model calls outside database locks. A short publication transaction must
check the current attempt, owner/grant revisions and expected selection
generation before publishing the result and pointer. Read-time authorization
remains necessary. Existing reader checks are protection, not a reason to
assume publication races are solved; absence of a fence is not by itself proof
of a user-visible leak.

## 4 Delivery sequence and package dependencies

Use one coordinated package owner with bounded subagent assignments. The waves
below describe dependencies, not calendar estimates or a standing set of
parallel lanes. All package statuses begin as **proposed**.

| Package | Outcome | Entry dependency | Primary responsibility |
| --- | --- | --- | --- |
| P0 | Agreed shared contracts and evidence portfolio | Program-owner admission and current baseline | Cross-repo architecture |
| P1 | Recognizable identity, correction, parts and collection continuity | P0; existing capture custody | Capture and Life owners |
| PC | Catalog anchoring and licensed media | P0; approved sources for live provider use, not fallback work | Entity/catalog owner with capture and existing Places owners |
| P2 | Immediate focused reader and exact return | P0 and usable source adapters; not all of P1 | Native reader owner |
| P3 | Substantive selected-object discovery | P0 and available owner reads; staged P1 collection integration | Context/retrieval and content owners |
| P4 | Kept editions and dependent correction | P0, P2 and a typed prepared-result seam; worthwhile additions to retain | Saved composition and correction owners |
| P5 | Selective refresh and accountable spend | Minimum safeguards accompany first P3; broader maintenance follows value, P4 for saved-edition replay | Maintenance/production owners |
| P6 | Shared value and cross-root continuity | Originals: relevant P1/P2 and existing sharing contracts; generated results: P3 and, when retained, P4/P5; grants for each behavior | Collection/social and root consumers |
| P7 | Whole-system hardening and controlled exposure | Evidence work starts in P0; completion follows selected product scope | Coordinated package owner |

**Wave A:** P0 plus P1 identity and original-record correction, PC subject
mapping and fallback contracts, and P2 foundation work. P2 can begin against
stable existing source references; attractive original reading must not wait
for provider selection, the entire collection system or intelligence.

**Wave B:** connect approved PC providers and continue P2 family coverage.
Start thin P3 discovery when its interfaces and eligible owner reads are stable,
with P5's minimum publication and cost safeguards. A usable reader and producer
meet at the first connected checkpoint while other families continue. P1
collection operations and eligible original portions of P6 proceed under their
existing owners; they do not wait for generated editions or enrichment value.

**Wave C:** once additions have shown people value, P4 adds exact retained
expressions and P5 expands selective maintenance. Extend P6 to the resulting
generated value only under its applicable grants and adopted derivative policy.
This deferral does not include original-record correctness, existing sharing,
or the safeguards required by an already running producer.

**Wave D:** complete the selected P6 root/social journeys and P7 hardening.
An original-focused scope can reach this checkpoint without all of Wave C.
Expand exposure according to evidence and existing release authority, not
merely because all package branches have commits.

## 5 Detailed engineering packages

### P0 Shared contracts and implementation admission

**Deliver:** one reviewed owner/interface map and a common lifecycle portfolio
that allows reader, retrieval and maintenance work to proceed independently.

- Recheck actual worktrees, runtime ownership, pending work and the program
  queue. Reuse the capture/share owner for overlapping files and outcomes.
- Map the responsibilities in section 3 to concrete existing types, services
  and mutation paths. Decide the thin identity/reconciliation mapping and
  consumer collection owner; do not rename editorial collections into it.
  Name the cultural-subject owner, stable local references, external mappings
  and work/edition distinctions before PC and P2 choose incompatible models.
- Specify selected component, selected-object context, prepared result and
  kept-edition references. Reuse owner revisions and existing action envelopes.
- Map representation, claim and context dependencies separately. Define what
  changes on correction, removal, deletion and access loss.
- Read the accepted amendments into the affected owner contracts without
  rewriting historical decisions or adopting pending catalog/grant proposals.
- Establish fixtures across the designed families (tickets, a venue anchor,
  a book, film, show and album) and the dish photo, passage and practical
  record, including sparse history and a permitted friend's contribution. Record
  allowed uncertainty and the original-only baseline.
- Establish the supported-family/mode matrix now: distinguish shared-contract
  coverage, first-delivery native coverage, honest fallback and deferred modes.
  Track original access, structured reading, catalog lookup, discovery and
  sharing separately. Designing the full portfolio does not require every
  provider and reader to finish before any supported family can be delivered.
- Agree on complete assignments and shared-file ownership. Any new schema or
  authority choice receives the required founder review before it is treated
  as settled; this is not repeated permission for ordinary implementation.

**Acceptance:** each scenario can be traced through a named owner, revision,
reader and repair route; backend/app share the same definitions. No owner is
invented by a mock adapter. Open decisions name only the work they actually block.

### P1 Recognizable objects and collection continuity

**Deliver:** a kept contribution becomes an inspectable thing with stable
identity and addressable originals, independent of its entry door.

- Reuse Intake and its immediate private Keep/Undo path. Preserve provisional
  extraction, source ordering, original access and unsupported-type fallback.
- Add source-bound components for multiple admissions or passages. Preserve
  originals through OCR correction, representation replacement and partial
  extraction failure. Never synthesize unreadable details to fill a template.
- Implement evidence-backed reconciliation of repeated captures. Persist the
  reason, supporting identifiers and reversible links. Ambiguous cases remain
  separate until evidence supports convergence; do not ask for classification
  before providing the original's value.
- Repair successive original-record corrections as distinct commands with
  expected revisions. Reassess the inspected candidate/action idempotency
  coupling and wrong-time clearing path; support typed replacements through
  the proper owner. These corrections do not depend on generated editions.
- Separate event/valid time, received time and freshness. Recheck the fact
  writer's validity-end default before reusing it for historical artifact data.
  Preserve captured facts and their provenance when current subject facts change.
- Establish consumer collection membership through its chosen owner, including
  explicit removal/exclusions, many-to-many membership and deletion semantics.
  Silent private filing is different from sharing or creating new structure.
- Represent one occasion holding multiple originals without creating the
  retired journey/chapter/day ownership hierarchy. Operational commitments
  stay with their domain owners.
- Keep artifact-family normalization bounded and versioned. Reuse semantic
  forms and client renderers; do not implement the pending self-promoting
  catalog, arbitrary model-authored schemas or a bespoke screen per interest.

**Acceptance:** email/screenshot of a proven same ticket converge without
losing sources; two screenings remain separate; a multi-admission image opens
the selected admission; complementary meal evidence stays attributed; removing
one membership and deleting the collection do not delete the thing. Source
deletion and Undo cannot resurrect through indexing or retry. Two legitimate
date corrections both apply, their retry applies once, and unrelated evidence
survives. Historical event time does not become upload time or catalog freshness.

**Dependency boundary:** connected-inbox OAuth, provider approval and every
capture door need not complete before the identity contract can be exercised
with existing eligible captures. Their shipping status remains explicit.

### PC Catalog anchoring and licensed media

**Deliver:** a capture can link to an evidenced subject and receive licensed
art and facts without making a successful external lookup necessary to keep
or open the person's object. Resolved subjects with missing art and unresolved
subjects have distinct, useful fallbacks.

- **Map subjects to provider identifiers,** per medium:
  - films and TV: a film/TV catalog such as TMDB;
  - books: ISBN-keyed sources;
  - music: a music catalog;
  - venues: a places provider.

  Keep the stable application-owned subject reference from P0 and record
  provider identifiers as reversible mappings with resolution evidence.
  Distinguish book works from ISBN-specific editions and relevant media
  releases or versions. Same-title candidates require discriminating evidence
  such as year, director or artist; missing evidence leaves resolution open.
  Provider replacement or a corrected match must not change the person's
  artifact identity, merge separate screenings or discard prior sources.
- **Handle unresolved subjects explicitly.** Matched, ambiguous, not found,
  and provider-unavailable outcomes are different. With an incomplete capture
  or no confident match, show supported captured details and the appropriate
  house treatment, or the original fallback if its family is unknown. Do not
  guess credits or require classification before reading. A correction or
  later successful match enriches the same thing rather than replacing it.
- **Fetch and cache the fields the forms use:**
  - covers, posters, 16:9 key art and album art;
  - runtime and credits (the film billing block);
  - episode counts and season structure;
  - venue address, category, hours and open status.

  Keep relatively stable catalog facts separate from live venue facts. Reuse
  the existing Places identity, live-status, cache and budget owners for
  venues; PC consumes them rather than creating another freshness service.
  Current fields carry observed time, expiry and honest stale/unknown states.
  Hours and current open status have different freshness requirements, with
  timezone and provider coverage accounted for. Catalog refresh changes the
  anchor's current facts, never the address, date or details on an old original.
- **Honor each source's terms:** attribution, caching limits and display rules.
  Record provenance per field. Choosing the sources is a founder decision
  (section 6), because it sets cost and what may be shown.
- **Bound provider work from the first connected lookup.** Reuse existing
  limits where applicable; declare call, concurrency, timeout, retry and spend
  budgets, with attempt accounting and permitted cache reuse. Repeated opens
  do not imply repeated paid lookups. Later model-generation budgets do not
  substitute for these provider limits.
- **Fall back when there is no licensed art:**
  - books: the white edition;
  - films: the billing block;
  - TV: the 16:9 title card;
  - music: the sleeve.

  Never generate imagery.
- **Own the latency of the recognizable object.**
  - Provide a fast recognition path: text reading for tickets and cached
    subject lookups.
  - Measure time to recognizable object (p50 and p95) separately from any
    model enrichment.
  - The ingestion decision's two-second goal remains a target until measured.

**Acceptance:**

- With adequate evidence and an approved available provider, a photographed
  cinema ticket resolves to the right film and cinema, with eligible poster,
  runtime and credits.
- Same-title cases disambiguate by supported identifiers or remain unresolved;
  two editions preserve both the shared work and edition-specific evidence.
- No match, ambiguity, unavailable provider and incomplete capture leave the
  original readable, without guessed metadata or forced classification.
- A corrected match preserves personal identity and original access.
- Venue status is current within its declared freshness boundary or explicitly
  stale/unknown; changing it does not rewrite historical source facts.
- Missing art falls back to the house design.
- Required attribution appears.
- Provider failure and repeated opens respect declared call/retry/spend limits.
- Original availability, structured recognition and catalog-enrichment latency
  are measured separately, including cold and unresolved cases.

### P2 Focused native reading

**Deliver:** an appealing, useful object opens immediately, supports inspection
and returns correctly from related material. It remains useful without AI.

- Extend the existing artifact/original/result routes through the app data
  facade. Retain generated wire types and existing mock/real selection.
- Define reusable family-level readers for appropriate inspection: an original
  photo, ticket details, a selected passage, and structured practical evidence.
  A single giant conditional ArtifactCard is not the abstraction.
- Open anchors as pages too: a venue, work or course in its standard face,
  with the person's attached things. Follow the Artifacts project boards
  (section 1A) for the forms: ticket kinds, place cards, media formats and
  house fallbacks.
- Preserve the selected personal target. Two tickets or contributions about
  one film open their own artifacts; visiting the common subject page is an
  explicit detour with a way back, not a silent replacement of either record.
- Keep original access, authorship, uncertain fields and selected component
  visible enough to understand. Standardized styling must not fabricate an
  official ticket, alter evidence, or imply validity or attendance.
- Read prepared eligible additions separately. No generation spinner replaces
  the whole object. Distinguish no addition from incomplete discovery/failure.
- Preserve originating root, collection, component, result edition and return
  position. Returning from another artifact should not rerank the reading.
- Recheck time-based expiry while mounted, app foregrounding, account change,
  grant loss and a late request response. Suppress stale payload/actions, not
  only change the heading. Respect adopted offline policy.
- Use existing semantic tokens, accessible native components and family-level
  fallbacks. Exercise large text, screen-reader order, long content and memory
  pressure. Do not choose new libraries or SDK upgrades in this roadmap.

**Acceptance:** original access and an honest fallback do not wait for model
recognition, catalog lookup or generated additions. Each supported family can
be inspected and its original reached; two personal artifacts sharing a subject
remain separately openable; a related detour restores exact context. Expiry and
authority changes affect actionable content; provider failure leaves
independently eligible value intact. Native QA must prove interaction and
visual fit beyond component tests.

Retain reviewed original-first specimens across the portfolio: readable
admission details, photograph inspection, a passage with its source context,
and usable structured record details. They must preserve personal specificity
and appropriate interaction rather than cosmetic variants of a generic information
card. Design review can identify weaknesses and select a treatment; desirability
to ordinary users remains a hypothesis until the human comparison.

**Design boundary:** exact density and aesthetic treatment need design review,
but source access, route continuity, eligibility and data contracts can advance
before final composition is frozen.

### P3 Contextual discovery and useful selection

**Deliver:** opening a thing can reveal a supported addition that the existing
Place-pair selector could not reliably discover, without requiring more input.

- Add a selected-object entry to existing context/retrieval, not a new agent.
  Begin with structured relationships, literal text/identifiers and semantic
  retrieval. Allocate bounded candidate space across these paths.
- Include a bounded public-world/nearby discovery route keyed by the selected
  subject and relevant circumstances. It can discover a newly announced
  screening, exhibition or local possibility, not just explain already known
  evidence. Use current authorized world/provider/research adapters and finite
  coverage; no continuous web search per artifact. Check present availability
  separately before expressing a practical option.
- Extend indexed representations only where they supply independent value:
  source text, passage/context, image OCR or identified detail, and relevant
  collection relationships. Indexes remain derived; hydrate current owners
  before inference. Group multiple representations back to the same evidence.
- Apply eligibility before selection. A similarity score never repairs the
  wrong entity, grants private context or proves occurrence.
- Include P5's minimum safeguards with the first live producer: current owner
  and grant checks before inference and at publication/readback, rejection of
  obsolete results, bounded calls/retries and reserved budgets, complete input
  dependencies, and actual-attempt accounting. Reuse existing mechanisms;
  this does not require the later archive-maintenance system.
- Separate candidate discovery from relationship/value judgment. Preserve
  original-only, attributed juxtaposition, single-source explanation, supported
  comparison and practical continuation as legitimate treatments.
- Keep the existing Home-specific two-source/cross-root producer contract for
  its own job. Create a reviewed focused-artifact policy at its owning seam;
  do not globally weaken existing gates or force a second source as padding.
- Distinguish user-supplied knowledge, kept explanations and passive exposure.
  Test semantic repeats and useful new mechanisms on familiar premises.
- Use bounded research only for a named missing public fact. Reuse governed
  public evidence across private matching where licenses and freshness allow;
  never share personalized synthesis through a public cache.
- Reuse existing editorial/retrieval evaluators with artifact-appropriate
  metrics. Extend the current Home/Places expression schema and mark treatment
  dimensions such as root distinctness applicable only to their real job.
  Adapt the venue-specific retrieval runner for artifact support sets and
  explicit valid-empty, incomplete/error and rejected-proposal outcomes.
  A new model provider or complex reranker must earn its place on identical
  candidates; neither is a prerequisite.

**Acceptance:** run the section 7 comparison with retrieval recall and selection
quality separated. Engineering evidence must include a supported additional
proposition or useful juxtaposition, plus a justified original-only case where
prose would repeat or distract. Preserve equally polished treatments for review.
A reviewer-selected enrichment winner is a hypothesis, not consumer superiority.
Wrong-entity, unauthorized and unsupported outputs fail independent of fluent
writing. The first live slice also exercises a changed-source/grant race and
its call/retry/spend bounds; broad P5 deferral does not waive those checks.
Human preference is a separate product-evidence checkpoint, not an
invented passing label or a prerequisite to all implementation.

### P4 Exact kept editions and dependent correction

**Deliver:** the person can retain a named explanation and reopen exactly what
they chose, with honest correction and availability over time.

- Implement the saved-composition persistence seam from the existing contract:
  ID/edition, exact content/media, selected target, complete dependencies,
  authorship, represented/generated times, retention trigger and eligibility.
  Do not turn the current six-hour production lifetime into permanent Keep.
- Make Keep idempotent for the same command/result; distinguish a second
  deliberate edition from a retry. Explicit replacement produces a new version.
- Preserve the original and kept edition when a better contextual selection
  appears. Do not silently rerun generation for an exact-result link.
- Consume P1's correction/revision events and repair affected edition
  dependencies without rewriting independent evidence. Ordinary source/date
  correction and its retry semantics are foundation work, not deferred here.
- Revalidate current permission on every served edition. Where policy is not
  settled, keep shared derivative retention gated; do not promise irrevocable
  copies or salvage uncited prose merely because another citation survives.

**Acceptance:** Day 2 edition is byte/content-exact after Day 5 context arrives;
successive P1 corrections repair the correct edition dependencies while
independent claims survive; withdrawn dependencies cannot appear through
old deep links or pending results. Retention/redaction semantics are separately
approved before the affected shared path ships.

### P5 Selective maintenance and bounded cost

**Deliver:** meaningful changes create timely new possibilities without
continuously regenerating the archive.

**Staging:** current owner/grant and publication checks, obsolete-result
rejection, input lineage, finite calls/retries and budget reservations, and
actual-attempt accounting accompany the first live P3 producer. They are not
postponed until enrichment proves valuable. Existing mechanisms can satisfy
them where verified. Broader dirty-selection tracking, archive-wide coalescing
and saved-edition maintenance can follow demonstrated value; no new cache may
suppress discovery of new material in the meantime. PC's provider budgets are
required by PC itself, not covered implicitly by generation accounting.

- Add bounded candidate-scope revisions and dirty selection tracking, including
  previous empty selections. Preserve current serving's ability to discover
  arrivals; a new cache must not remove that behavior.
- Use existing outbox/job patterns for durable source/index progress. Carry
  owner revision and indexing method version. Readiness advances only when all
  relevant preceding work is accounted for, not the highest finished event.
- Distinguish stale index hits from incomplete discovery. Reject stale or
  ineligible content before prompting; use bounded owner-query fallback where
  valid. An index failure is not a successful no-result judgment.
- Coalesce invalidations and deduplicate work across processes. Recompute cheap
  selection first; reuse equivalent eligible prepared content. Generate only
  under a supported request or adopted preparation policy.
- Extend short atomic publication fences using existing owner/grant patterns.
  Protect first-insert versus delete, takeover, concurrent edit and cancellation.
  Model calls never run inside those database locks.
- Record input influence beyond citations, including prior claims used for
  novelty suppression. Correcting that history can change future selection
  without rewriting unrelated saved evidence.
- Reserve finite generation budgets before work. Define cancellation/retry
  accounting and cost ceilings separately from commercial entitlements. A
  cooldown, cache hit or telemetry field is not a hard budget.
- Measure actual model attempts and workload cost using the shared accounting
  path. Preserve uncertainty when accounting fails. Do not equate wrapper-level
  producer invocations with billed model-call counts.

**Acceptance:** section 8 races and replay converge without stale publication;
unchanged warm reads need zero generation calls; burst imports stay bounded;
late evidence can change an empty selection; index lag is observable. Report
measured cold/warm latency, cost and fan-out before setting production defaults.

### P6 Shared value and cross root continuity

**Deliver:** artifacts become more valuable through authorized people and
different roots without duplicating material or inventing a second social feed.

**Staging:** preserve and extend eligible exact-original sharing and receiving
as soon as the relevant P1/P2 and existing sharing contracts support it.
Collection sharing additionally requires its membership and removal behavior.
Neither waits for P3, P4 or broad P5. Generated-result circulation needs P3's
safeguards; retained or shared derivatives add P4/P5 and the applicable policy.
Full cross-root acceptance is a later integration check, not permission to
delay original receiving or duplicate its implementation in a new service.

- Wire Life's collection/time/place/people readings to stable thing references.
  Add selected component and edition continuity where needed; do not redesign
  unrelated Chat, Life or Place surfaces as a side effect.
- Let Home receive a worthwhile compact return and open the exact thing/result.
  Places may situate the same material when spatial context is useful. Chat
  can continue from the selected context through an explicit private request.
- Opening in one root does not create another copy or grant action authority.
  Practical help uses existing owner commands and current provider truth;
  a generated option is not a booking, commitment or monitoring mandate.
- First support attributed human originals under current eligible grants.
  AI synthesis over a friend's contribution requires its own applicable use
  authority. Show different perspectives without generating a group consensus.
- Implement accepted shared collection add/remove/leave semantics with the
  actual collection owner. Keep private viewer context out of shared notes and
  captions. Explicit author sharing and any future automation are distinct.
- Route friends' changes and new organizing structure under the accepted
  notification placement; do not revive a parallel Updates feed, narrate silent
  filing, or select push cadence without its policy decision.
- After withdrawal, preserve independent contributions while repairing all
  dependent projections. Exercise saved editions only under an approved policy.

**Acceptance:** a recipient gains value without contributing or replying; a
friend's original stays attributed; a collection leave removes the correct
contributions; private backs do not leak; Home/Places/Life entry and Chat detour
preserve selection and return. Tests cannot substitute for real authenticated
multi-viewer readback and native interaction.

### P7 Hardening and controlled delivery

**Deliver:** the chosen scope works as one product under normal and adverse
conditions, with explicit limits on what is ready to expose.

- Start deterministic portfolio and telemetry work in P0; do not postpone all
  evaluation until this final package. Reuse the current test/eval/QA framework.
- Test migration, aliases, partial backfill, duplicate delivery, rollback and
  old-client fallback. Readers tolerate supported prior versions; no destructive
  source rewrite or indefinite dual truth owner is permitted.
- Run offline tests, disposable-Postgres races, generated API/type checks,
  authenticated API/native readback and registered visual/interaction QA at
  the appropriate boundary. Preserve exact revisions and named limitations.
- Compare treatment quality with real permitted model execution when authorized.
  Keep fixtures, live model output, native acceptance and voluntary preference
  as distinct evidence categories.
- Evaluate returning users and sparse-history users across ordinary material.
  Record benefit, attribution, unwanted work and optional continuation—not only
  clicks, capture counts or judge scores.
- Review model spend, storage/index growth, repair lag and prepared-but-unused
  work. Disable optional enrichment safely without breaking original access.
- Expand internal exposure under existing flags first. Deployment, publication,
  shared policy adoption and public release require their own authority.

**Acceptance:** the selected scope has an explicit supported-family/mode matrix,
known limitations, rollback path, current acceptance evidence and program-owner
checkpoint. Retire replaced adapters only after consumer/readback coverage.

## 6 Decisions and their actual blocking scope

| Decision | Recommendation or current boundary | Blocks | Does not block |
| --- | --- | --- | --- |
| Thing reconciliation and component ownership | Approve a thin mapping and shared selectors in P0; preserve domain truth | Incompatible identity/schema implementations | Original rendering against existing source references |
| Consumer collection owner | Map accepted many-to-many behavior explicitly; do not reuse editorial guide tables by name | Durable collection writes and corresponding sharing | Single-object private reader and owner-linked discovery |
| Kept edition after supporting withdrawal | Recommended default: withhold affected content, preserve only permitted metadata, offer a new independently supported version; exact policy unadopted | Shared derivative retention and partial salvage promises | Private originals and edition mechanics tested without disputed shared material |
| Offline retained material | Adopt what can be cached, for how long and how reconnect handles loss; no instant remote revocation promise | Persistent shared offline caches and their user promise | Online reader, locally available independently eligible originals under existing rules |
| Automatic preparation | Separate selection refresh from generation; define allowed triggers and budget owner | New proactive generation/background posture | Existing explicit requests, pure reads and cheap authorized selection |
| Initial families and reader density | Map designed families and comparison cases in P0; distinguish contract coverage, first-delivery modes, fallback and deferred coverage | Final family-specific visual acceptance and unsupported-format exposure | Shared reader/data/lifecycle foundations |
| Catalog and art sources | Choose per-medium sources for films/TV, books, music and venues, with their terms, costs and caching limits | Shipping real art, credits and live venue facts | House-design fallbacks, reader foundations, identity work |
| Open catalog and model vendor | Keep reviewed bounded families and current model infrastructure until a change earns adoption | Self-promoting type registry or new provider rollout | All baseline packages |
| Shared additions and notification cadence | Preserve accepted explicit sharing and placement; pending automation/push defaults stay pending | Those automatic or interruptive behaviors | Attributed originals, explicit add/remove and in-context receiving |

Do not convert these rows into a blanket prerequisite. Escalate only the
consequential decision needed by the next concrete behavior.

## 7 Connection quality portfolio

Use complete small corpora with distractors, exact identities/revisions,
eligible evidence sets and acceptable abstentions. These are planned synthetic
fixtures, not claims of facts about a real film, meal or friend.

| Case | Required distinction |
| --- | --- |
| Ticket plus one authoritative public note, then a newly announced related screening | Useful single-source explanation without attendance inference; discover the new public candidate after an empty selection, with availability checked separately |
| Dish photo, menu and home attempt | Observable contrast versus unsupported explanation of the restaurant's technique |
| Passage and museum photo across collections | Retrieve the specific span/detail; go beyond shared keywords |
| Scorecard or practical record | Correct arithmetic, units and comparable conditions; no personality judgment |
| Friend's perspective | Original/juxtaposition may suffice; visibility does not grant synthesis |
| First artifact with no history | Good public context or good original; no setup homework or invented preferences |
| Same name or title with different entities | Discriminating identifiers outrank plausible semantic similarity |
| Connection explicitly stated by user | Suppress paraphrase; permit a supported new mechanism or application |
| Previously displayed connection | Avoid repetition without claiming understanding; exact reopening stays available |
| Novel but irrelevant material | Purpose-fit relevance outranks obscurity or maximum diversity |
| Day 1 ticket, Day 2 edition, Day 5 photograph | New discovery and stable edition coexist through correction/withdrawal |
| No worthwhile addition | Distinguish true empty/rejected options from failed or incomplete retrieval |

Compare an original with essential context, attributed juxtaposition, and a
sourced explanation at matched presentation quality. Add a practical treatment
only where the situation calls for it. Counterbalance human comparisons so
showing one version does not manufacture familiarity in the next.

Measure separately:

- Candidate recall at a bounded budget, including complete support sets and
  wrong-entity/unauthorized retrieval. A judge cannot repair missing candidates.
- Selection quality on fixed candidates: relevance, redundancy, false novelty,
  false suppression and appropriate abstention.
- Claim grounding, attribution, uncertainty, current authority and repair.
- Human preference, identifiable benefit, later attribution, voluntary return
  and reduced unwanted work. Reviewer/model votes are not these outcomes.

Keep related versions and arrival sequences together when splitting development
and held-out sets. Do not leak the Day 5 answer into Day 1 evaluation. Run cheap
deterministic wiring first, bounded retrieval/model comparisons during the
build, and human comparison separately. No new evaluation platform is needed.
An empty expected set needs an explicit abstention verdict; the existing
venue-runner convention alone does not supply one. Focused-artifact treatments
must not inherit a universal Home/Places distinctness score.

## 8 Change and cost replay

Use a controlled clock and barriers at discovery, owner reads, model completion,
publication and readback. Inspect content/actions and owner state, not only
status labels. Persist evidence of the tested revision tuple.

| Event | Expected behavior |
| --- | --- |
| Late photo of an earlier event | New ingestion position triggers discovery; event time and existing edition stay unchanged |
| New useful source after empty selection | Candidate scope invalidates emptiness even if old sources never changed |
| Two corrections and one retry | Both new commands apply; the retry does not apply twice; unrelated evidence survives |
| Location or purpose changes | Select new context without moving the original or changing an active reading |
| Grant loss during generation | Current publication/read guards deny affected output; index cleanup is not the safety boundary |
| Concurrent edits and worker takeover | Older revisions/leases cannot publish over current state |
| Crash before call | Bounded recovery can resume without claiming a paid call occurred |
| Crash after provider response before commit | At most one current published result; duplicate provider spend remains possible |
| Database new, index old, then stale hit | Incomplete discovery or valid fallback; owner hydration rejects stale/ineligible content |
| Burst import and repeated opens | Bounded fan-out and coalesced work; unchanged opens require no generation |
| Source expiry while screen remains open | Stale content/actions become unavailable, with stable navigation and honest recovery |
| Withdrawal after Keep | Apply adopted derivative policy; preserve independent originals and no revoked content resurrection |
| Account switch and offline reconnect | No prior-account late response/cache leakage; current grants rechecked on reconnect |

Record time to recognizable object and time to useful extension separately,
including p50/p95, cold/warm state, queue and index lag, failures, cancellation,
reuse, stale-publication rejection, duplicate work and unused prepared content.
Cost includes extraction, embedding, public evidence preparation, generation,
retries, repair and storage/index growth. Tie each reported model call to the
shared accounting path; missing accounting is an error/unknown, not zero spend.

The approximate two-second arrival goal in the ingestion decision is an
unmeasured product target, not an achieved service level. Package P2 measures
original recognition separately from model enrichment. Set actual budgets and
freshness targets from representative workloads, not model-list pricing alone.

## 9 Integration migration and validation

### API and storage changes

The backend owns wire models; the workspace owns full/app OpenAPI projection;
the app consumes generated types. For changed routes/models, update backend and
focused tests, run `./scripts/sync-types.sh` from the actual coordinated lane,
review snapshots/types/consumers together, then `make api-coverage-check`.
Do not hand-edit generated models or duplicate them in a native-only interface.

Prefer additive, reversible schema changes and bounded backfill. Preserve old
source/reference identities with tested compatibility until readers migrate.
Do not backfill unsupported attendance, uncertain dates, inferred preferences
or broader grants. Mixed model/recipe versions must remain inspectable.

Contract tests and typed fixtures can let reader and backend work proceed
concurrently. Mock/real selection stays at the app data boundary. Mock progress
must not become a second production owner or count as authenticated readback.

### Verification boundaries

Backend packages follow [Backend Task Intake](../../travel-agent/docs/operations/Task%20Intake.md):
schema/API work is contract-sensitive, prompts/selection are prompt-sensitive,
and unapproved authority/core-schema choices retain founder review. Native
data, persistence and routing follow [Frontend Task Intake](../../travel-app/docs/Task%20Intake.md)
and are generally parity-sensitive, not visual-only work.

- Run focused offline tests during iteration; use existing selectors and name
  skips/quarantines. Source and lifecycle fixtures prove only their inputs.
- Database race tests require explicit `TEST_DATABASE_URL` and
  `TEST_DATABASE_DISPOSABLE=1`; never probe or clean ambient development data.
- Follow the implementing checkout's current child preflight: at the command
  review above, backend `make ci-static` plus
  `make merge-check BASE_REF=<explicit-base>`, and app `npm run verify:fast`
  plus `npm run verify:merge -- --base <explicit-base>`. Full regression suites
  are separate deliberate/main/nightly/release checks, not automatically
  repeated after every edit. Retain coordinated `make verify` under this
  workspace's delivery instruction and the currently required hosted checks.
  Resolve any staged-gate transition through the execution lane's CI Plan;
  this roadmap does not itself promote `verify-changed` to a replacement or
  waive required checks. A defined command is not evidence it ran.
- For visible changes, use registered surface contracts and the existing
  polish QA path: scenario/reference validation, doctor, capture, structured
  comparison and verdict. Establish the correct build, persona, data source
  and design reference before an expensive run. A dry run proves no pixels.
- Exercise authenticated original access, server persistence and multi-viewer
  repair separately from mock screenshots and model quality.
- Record commands, revisions, environment and pass/fail/blocked/unrun/stale
  states with the existing verification measurement tooling. Do not claim
  productivity gains from test counts or fewer instructions.

### Checkpoints

| Checkpoint | Review | Decision |
| --- | --- | --- |
| After P0 | Do owners, selectors, revisions and policy boundaries fit the family/mode matrix? | Approve interfaces and first-delivery coverage; resolve only actual blockers |
| First connected P1/PC/P2 result | Are originals desirable and correct, including no-match/provider failure and historical-versus-current facts? | Accept supported reader/catalog modes without requiring every family or P3 |
| First connected P2/P3 result | Is the addition substantive and low effort, with permission, publication and spend safeguards exercised? | Adjust reader/selection together; decide whether saved editions and broader maintenance now earn work |
| P4/P5 lifecycle replay | Do change, exact retention, revocation, index lag and spend behave coherently? | Harden affected seams or revise the abstraction before broadening |
| P6 receiving and P7 integration | Can a sparse-history person and a thin social participant receive complete value? | Review originals as soon as ready; add derivative cases only when supported, then choose exposure under existing authority |

Checkpoints guide direction; they are not a demand to pause after every small
technical obstacle. No single movie-ticket demo certifies the whole product.

## 10 Operational delegation

One owner carries the coherent package through implementation, review,
integration and handoff. Use in-session subagents for bounded parallel work;
do not create user-owned sessions unless requested. Reuse an appropriate
coordinated worktree and verify runtime/device ownership before work.

After P0, sensible parallel assignments are native focused reading and PC
provider integration, while capture/Life owns shared identity, correction and
membership. Thin discovery can join once its interfaces are stable; early
original sharing stays with its existing owner. Avoid turning every package
into a standing lane. P4 and broader P5 separate persistence from maintenance
only when value, contracts and file ownership permit it. One owner controls
shared models, migrations, generated contracts and navigation integration.

Each assignment includes outcome, relevant canon/code, exact write ownership,
allowed scope, acceptance evidence, dependency contracts, and escalation rules.
It should continue through ordinary diagnosis, implementation, local tests,
review fixes and a verified handoff. Report at first integrated result,
consequential blocker and completion—not every minor success.

Coordinate interfaces directly. Escalate product authority, incompatible owner
design, missing external access, or consequential scope changes. Do not broaden
policy, weaken checks, enable background work or switch another session's
checkout to clear a blocker.

Use focused checks continuously, integrate when an interface changes or a
complete outcome is ready, and run coordinated gates at landing/checkpoints.
Avoid requiring every small commit to wait for a full device matrix, while
preserving required delivery checks. Commit coherent changes with explicit
filenames when implementation is authorized; publishing and deployment retain
their separate authority.

## 11 Recommended first assignment

At the next program checkpoint, admit **P0 plus the necessary P1 foundation,
PC catalog anchoring for the first families, and P2 reader integration** as a
complete artifact-foundation assignment inside the current capture/Life work.
The first families are those already designed (section 1A): tickets, venue
anchors, and books, films, shows and music. P0 distinguishes their shared-contract
coverage from supported first-delivery modes and honest fallbacks; every family
and provider need not finish at once.

For a fast first release:

- Deliver ordinary source/date correction and Undo with the P1 foundation.
- Start P3 thin, with one or two kinds of addition, once its interfaces and
  eligible owner reads are stable. Connect to a usable P2 reader early.
- Include permission, publication, input-lineage and spend safeguards with
  the first live P3; include provider limits with PC.
- Defer saved editions and broader archive maintenance until additions show
  people value, not the safeguards required by already running work.
- Advance eligible original sharing and receiving with the relevant P1/P2 and
  sharing contracts; only generated derivatives wait for their later dependencies.

The finish condition is not a document alone:

- shared target/component/edition contracts are mapped and reviewed;
- eligible kept originals from existing supported doors open through the same
  references, with honest selected-part, unresolved-catalog and fallback behavior;
- distinct source/date corrections and retries behave correctly, and refreshed
  subject facts never overwrite historical captured facts;
- subject identity is application-owned, provider mappings are reversible,
  and work/edition distinctions preserve both shared and specific evidence;
- approved catalog integrations obey freshness, attribution and provider limits;
  unresolved provider decisions do not block the original/fallback reader;
- collection and reconciliation ownership are explicit, with the adopted
  portion connected rather than improvised in a screen;
- exact return and expiry/authority behavior have focused test coverage;
- original-first family specimens have concrete visual/interaction review,
  preserving the submitted material's specificity; do not postpone the whole
  desirability question as later polish or claim measured user preference;
- the P0 family/mode matrix, portfolio fixtures and lifecycle replay inputs
  are ready for P3 and the relevant P5 stages;
- unresolved shared policy remains isolated behind its explicit boundary.

Dispatch P3 as soon as its selected-object/context interfaces and eligible
owner reads are stable, while the remaining P1/P2 work continues. Do not wait
for every first-assignment finish condition, complete collection writes or
edition persistence. Review the first connected P1/PC/P2 foundation, then the
connected P2/P3 result; neither checkpoint waits for all families. Prepare P4
and broader P5 contract tests in parallel where files are independent, while
the minimum producer safeguards ship with P3.
Do not block on signing, a new model vendor, complete connected inbox delivery
or final visual polish when unrelated work can proceed.

This sequencing builds the shared system from the full behavior portfolio.
It does not turn one proof loop into the product's architecture or add another
mandatory planning phase before ordinary implementation can begin.

## 12 Implementation references and research provenance

Code links resolve against this checkout for navigation. Findings refer to the
delivery revisions in section 2; re-open the corresponding files in the actual
implementation lane before editing. Existing strategy and research details:

- [Focused artifact direction](product-direction-2026-09-28.md#14-september-29-focused-artifact-experience).
- [Artifact engineering and bounded model research](memory-as-product-direction-research-2026-09-28.md#17-september-29-artifact-engineering-investigation).
- [Contribution and consequence](../systems/contribution-and-consequence.md)
  and [artifact expression and persistence](../systems/artifact-expression-and-composition.md).
- [Resource references](../../travel-agent/backend/core/models/execution_contract.py),
  [artifact read projection](../../travel-agent/backend/core/models/canonical_artifact.py),
  [Intake locators](../../travel-agent/backend/core/intake_evidence.py),
  [correction handling](../../travel-agent/backend/core/db/intake_semantics.py),
  [time correction adapter](../../travel-agent/backend/inbound/anchor_runtime.py),
  [historical fact writer](../../travel-agent/backend/core/db/entity_facts.py).
- [Atlas retrieval](../../travel-agent/backend/core/vector/atlas.py),
  [Source discovery](../../travel-agent/backend/root_projection/v2/source_contribution_discovery.py),
  [selection](../../travel-agent/backend/root_projection/v2/source_contribution_opportunities.py),
  [known-to-person checks](../../travel-agent/backend/root_projection/v2/known_to_person.py).
- [Exact result references](../../travel-agent/backend/core/source_contribution_result.py),
  [serving](../../travel-agent/backend/root_projection/v2/source_contribution_serving.py),
  [producer](../../travel-agent/backend/root_projection/v2/source_contribution_producer.py),
  [publication and invalidation](../../travel-agent/backend/core/db/source_contributions.py),
  [Life fences](../../travel-agent/backend/life_projection/owner_fence.py),
  [LLM accounting](../../travel-agent/backend/core/llm_accounting.py).
- [Native result reader](../../travel-app/components/source/SourceContributionResultScreen.tsx),
  [saved-composition fixtures](../../travel-app/utils/compositionBrief.ts),
  [editorial evaluator](../../travel-agent/tools/eval/judges/source_contribution_editorial.py),
  [retrieval metrics](../../travel-agent/tools/eval/plugins/retrieval/metrics.py).

The parallel research used these primary technical precedents. The transfer to
Vesper is a design recommendation, not validation of Vesper's product advantage:

- [Embark](https://www.inkandswitch.com/embark/): separate data, computations
  and views; accepted concrete bindings need not follow every later context
  change. This prototype does not establish our retention or collaboration policy.
- [Web Annotation](https://www.w3.org/TR/annotation-model/): source, selector
  and representation state; locators need revision context. No JSON-LD or
  universal graph implementation is required.
- [Qdrant multi-representation retrieval](https://qdrant.tech/documentation/tutorials-search-engineering/multi-representation-search/)
  and [MMR](https://aclanthology.org/X98-1025.pdf): complementary retrieval
  representations and relevance-aware redundancy reduction. Neither establishes
  factual support, personal novelty or felt value.
- [Skyframe](https://bazel.build/reference/skyframe): explicit dependency and
  candidate-set tracking. Model generation is nondeterministic; retaining its
  result does not make a new call reproducible.
- [Convex queries](https://docs.convex.dev/functions/query-functions) and
  [Materialize subscriptions](https://materialize.com/docs/sql/subscribe/):
  separate deterministic reads from external actions, and distinguish progress
  from an empty result. Borrow the mechanisms, not new infrastructure.

## 13 Document completion record

This document records planning and inspection evidence only. Runtime tests,
native acceptance, model comparisons and economic measurements in the packages
are required future work, not completed results. On expiry, the program owner
should absorb useful package detail into the active execution plan, refresh this
supporting plan with an explicit reason, or archive it. Do not maintain a second
dispatch queue here after execution is admitted.
