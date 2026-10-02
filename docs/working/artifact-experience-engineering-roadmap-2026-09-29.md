---
doc_type: working
status: active
owner: founder / Strategy lane
created: 2026-09-29
last_verified: 2026-10-02
expires: 2026-10-13
why_new: The strategy handoff names three artifact workstreams but cannot hold their detailed contracts, dependencies, migration, evaluation and delivery sequence without becoming a second general roadmap. This bounded supporting plan expands that section for the existing program owner.
supersedes: []
source_of_truth_for: []
---

# Artifact experience engineering roadmap

**Current lane state — October 2:** A1 in [section 0](#a1-private-reader-and-collection-data-coherence)
is implemented and verified in the frozen candidate tuple: workspace
`f77e055045562d04774a447b45150c6eb8e01d32`, backend
`3e66aed35856c8963220cf211ecceacd54859c84`, and app
`8bf11fb84a60455bfabf47a08b546d28d856603e`. Central integration has now landed
these candidates through backend [PR #247](https://github.com/fy538/travel-agent/pull/247),
app [PR #216](https://github.com/fy538/travel-app/pull/216), and workspace
[PR #61](https://github.com/fy538/travel-workspace/pull/61), with required checks
passing. The accepted merge tuple is recorded in the
[program checkpoint](vesper-program-roadmap.md). Do not repeat A1. One separately bounded Clerk-authenticated mobile acceptance
gate remains open below. No new chat Goal is active; model evaluation remains
excluded.

Vesper should make an original worth keeping, opening and returning to, with
optional intelligence that adds substance. A1 hardens existing private data and
reader continuity while product design continues; it does not authorize a new
Collection member experience. Earlier local/unmerged and quality-pilot wording
is retained as dated history, not a competing execution queue.

## 0 Strategy lane execution boundary

### A1 Private reader and Collection data coherence

**Goal:** complete the P1/P2 private data-continuity slice so existing reads stay
coherent after owner correction, merge/reversal, source removal and account
change. Carry reproduction, necessary implementation, focused cross-layer
verification and a clean integration candidate through one assignment. Read-only
Collection data composition remains headless; no new member UI is part of A1.

**Starting evidence, October 2:** `data/canonicalArtifacts.ts` already has expiry
and foreground refresh; `__tests__/data/canonicalArtifacts.test.tsx` covers late
prior-account responses. `data/selectedSourceResearch.ts` already binds work,
original, revision and account, with original-only fallback. Private Collection
pagination already pins revisions and restarts stale continuation. Backend
`tests/inbound/test_kept_things_postgres.py` covers alias/reversal races and
source revocation; `test_candidate_owner_lifecycle_postgres.py` covers correction,
Undo, retry and persisted reader behavior. Preserve this coverage instead of
rebuilding those owners or assigning every listed scenario as absent.

**Reproduced investigation seam — October 2:** composed Collection member pages
have a separate query key from singular/batch Thing projections. A mounted
Collection member read remained stale after a successful merge: its Thing
projection stayed at revision 1 when authoritative readback had advanced to
revision 2. The fix centralizes owner-session-scoped private Thing, index and
composed-member refresh after merge/reversal; verified source revocation also
prunes only the exact revoked submission from cached projections before refresh.
Cancellation guards prevent an older in-flight composition from writing back
after a source or account transition. Focused app regressions cover merge,
reversal, cross-account isolation and delayed detail/batch responses.

| Milestone | Implementation and completion evidence |
| --- | --- |
| A1.1 Mutation-to-read coherence | Mount an existing composed member read, perform owner merge then reversal through the real mutation facade, and inspect refreshed membership-to-Thing/source identity. Reproduce any stale cache, repair through existing query ownership, and prove unrelated account data stays isolated. A bounded no-defect result is acceptable if the existing path demonstrably refreshes. Do not replace the data layer. |
| A1.2 Source and correction lifecycle | Connect current private Collection membership/Thing batch reads with source revocation and alias reversal through real owner routes/disposable Postgres. Keep independent originals eligible; removal from a Collection must not delete a Thing. Combine existing correction Save/refetch/Undo route evidence with current app invalidation; add only missing cross-boundary cases. Preserve exact source identity, expected revisions, safe retries and denial. |
| A1.3 Delayed reads and owner transitions | Exercise a pending member-batch/reader response across account or session changes, and across a source/revision change followed by authoritative readback. Prove cached old content/actions cannot be reinstated by late responses once invalidation/current authority is known. Respect existing refresh/offline semantics; do not promise instantaneous remote revocation or invent push infrastructure. |
| A1.4 Reviewable candidate | Verify changed app behavior and real backend parity at their stated boundaries; regenerate contracts only if actual wire changes require it. Run the explicit-base preflight once the coherent candidate is stable. When visible existing reader behavior changes, retain its required scoped native evidence or clearly leave that acceptance blocked. Hand off fixed revisions and a concise case/evidence matrix. |

**A1 evidence — October 2:** app regression suites passed (3 suites / 24 tests)
for composed-member merge/reversal refresh, account isolation, delayed reads,
and exact source-revocation pruning. Disposable-Postgres owner-route coverage
passed with the existing correction/Undo, merge/reversal, revocation and
Collection lifecycle suites (20 tests total). No API wire shape changed, so
generated contract synchronization was not needed. The app changes only query
coherence/cancellation and have no visible presentation effect; no native
visual capture was triggered.

**Separate authenticated acceptance gate — OPEN / NOT RUN:** signed-in
Clerk-backed mobile Save → canonical readback → Undo → readback has not been
established by this A1 work. The backend route tests used the lane's disposable
local database and `SKIP_AUTH`; they prove their route/persistence boundary,
not authenticated app-to-service behavior. No approved Clerk session or device
was assigned to this lane. Keep this gate open until that evidence is available;
do not infer closure from the route tests, mock app tests, or prior synthetic
native runs.

**Provider-free API and Metro readiness — October 2:** the lane-local Postgres and Qdrant
were healthy. The API started with the locally configured real Clerk issuer/JWKS,
`SKIP_AUTH=false`, `AI_MODE=off`, `WEB_SEARCH_MODE=off`,
`DISABLE_API_BACKGROUND_TASKS=true`, `DISABLE_LLM_BACKGROUND_LOOPS=true`, and
`EMBEDDING_PREWARM_ENABLED=false`; read-only `/health` and `/ready` both returned
HTTP 200, with Postgres and Qdrant ready. The `/ready` response reports the
local service checks as healthy.
The first startup omitted the prewarm override and contacted Hugging Face Hub
for the local embedding-model prewarm; it was stopped immediately. A corrected
startup with prewarm explicitly disabled produced no prewarm activity. No
LLM/search-provider call, protected-route request, or user-data mutation was
made. The API remains running on the lane's port 64746. The app lane's ignored
`travel-app/.env.local` now contains only the matching test Clerk publishable
key, lane-local API URL, real-backend mode and auth-bypass-disabled settings;
the ignored backend `.env` contains only the matching issuer/JWKS plus the
provider-off controls listed above. Both files were created with private file
permissions; the canonical env files were not changed and no values were
printed. Metro is running offline and localhost-only on lane port 64747. Its
first attempt correctly failed the app's loopback guard; the successful retry
used the app's explicit `ALLOW_LOCAL_ENV_OVERRIDE=1`. The Mapbox build-token
warning remains; no map/build behavior was exercised. No approved signed-in
session or device is assigned to this lane, so this is service/bundle readiness,
not authenticated mobile acceptance. The shared simulator remains unavailable
to this lane until central releases it.

This investigation also found a registry mismatch: implementation and tests
prewarm when `EMBEDDING_PREWARM_ENABLED` is unset, while the flag registry says
the default is false. The registry is corrected to match the verified behavior;
the provider-free command above must continue setting the kill switch explicitly.

**Finite remaining acceptance objective:** when an approved Clerk app key,
signed-in QA session, and assigned device are available, perform one real
owner-scoped replacement-time Save → canonical readback/cold reopen → Undo →
canonical readback/cold reopen against a non-sensitive test artifact. Record
the authenticated session-to-owner mapping and app/backend revisions; verify
the explicit offsets and expected revision progression, and that the original
source evidence is unchanged. Stop after this one round trip. The matching test
Clerk app/backend configuration is now present in this lane's ignored files;
the remaining blocker is an approved signed-in QA session and central release
of an assigned device—not another implementation package. Backend denial and
persistence tests remain separate evidence and are not substitutes for this
acceptance.

**Normal sign-in when the device is released:** open the installed Vesper
development build against this lane's Metro server. On the welcome screen tap
“I already have an account”; on the sign-in screen choose “Continue with email”
and complete Clerk's ordinary email-code flow with the approved QA account.
Keep the email and one-time code out of chat and logs. Before Save, confirm the
signed-in session resolves to the expected owner. This sign-in step has not yet
been exercised on a device.

**Goal completion boundary:** A1's mandatory outcome is verified private
implementation/data coherence plus the reviewable candidate; it does not certify
Clerk-authenticated mobile/service behavior or production use. The existing
signed-in Save/readback/Undo acceptance remains a separately named open gate.
Attempt it only when an approved session and assigned device exist; mock or
identity-override results must not be promoted to authenticated acceptance.
If required evidence for changed visible behavior is unavailable, that candidate
boundary remains blocked rather than silently waived. Once the declared work is
complete, stop; do not reactivate model evaluation to extend the goal.

**Ownership / independence:** own kept-Thing/Collection query caches and reader
internals. Connectivity owns root/capture callers; coordinate a concrete shared
query-key change once rather than concurrently editing their routes. Prefer no
API changes; if necessary, own the coordinated generated-contract slice and
notify central before another lane touches snapshots. Reuse existing private
owner contracts, generated types, mock/real API boundary and mutation gating.
No model/provider, catalog license or final screen design is needed for A1.

**Out of scope:** shared membership/audience changes, new retention, Collection
labels/previews/hierarchy/detail route, saved AI editions, prompt/model quality,
automatic generation and new backend identity owners. Reproduce the concrete
seam first; if all cases already have sufficient evidence, a short verified
closure is better than speculative code or more tests for activity's sake.

**Continuation and consolidation:** progress through A1.1–A1.4 without requesting
a new task at each checkpoint. Update this block with the current milestone,
base/candidate tuple, evidence, blocker and next independent step. Central may
land a ready independent slice without ending A1. Stop at the finish boundary or
an unresolved authority decision; wider P0–P7 packages are not automatically
assigned. [Program operating rules](vesper-program-roadmap.md#next-activation-round--october-2-roadmap-goals)
own watcher, device, integration and goal-state behavior.

**Execution ownership — October 1:** the Strategy artifact lane owns this
outcome end to end in one coordinated workspace/backend/app worktree tuple; do
not open a second lane for the same identity slice. The workspace repository
owns this cross-repo roadmap, contract alignment and evidence receipt.
`travel-agent` owns the persisted `ThingRef`, reconciliation commands,
source-preserving authorization checks, and the backend read contract.
`travel-app` consumes that stable contract through generated API types and a
native reader; it owns presentation, navigation and query-cache behavior, but
must not invent a parallel identity, reconciliation or source-authorization
authority. Keep the three Git histories independent.
Strategy Technical supplies reusable context/research primitives, while
Orchestration owns capture transport and Home/Places delivery; neither lane
owns the kept-Thing identity write. The artifact lane carries its slice through
focused verification and committed handoff to central integration, escalating
only a changed authority boundary
or a real cross-lane conflict.

**Product decision ownership — October 1:** the founder retains authority over
unresolved user-facing composition choices, including what a Life Collection
member view should make meaningful and how that value is presented. The
artifact lane owns advancing the bounded, current-authority data contract and
its implementation within the accepted Collection semantics; it must not
mistake an API payload or the legacy Threads design reference for approval of
the final member experience. Backend owns canonical Collection data and
authorization, the app owns its presentation and interaction, and this
workspace records the cross-repo contract and evidence. Escalate when a choice
changes product meaning, privacy/audience behavior, or visible claims; routine
contract, query, cache and verification work remains with the accountable lane.

**Ownership decision — October 1:** keep the artifact-roadmap outcome in the
existing `codex/artifact-foundation` coordinated tuple; do not create another
branch or worktree merely to begin its next package. This tuple is the single
accountable execution lane for the outcome and carries each bounded slice
through implementation, cross-repo verification, review and committed handoff
to central integration for safe landing. “Single lane” does not collapse
the three repositories into one history or transfer ownership of their layers;
each repository's changes are committed in that repository, under the
ownership split above. Open a separate lane only for a genuinely independent
outcome with explicit file/runtime ownership, not for another step in this same
artifact sequence. Technical owns the landed selected-source producer and its
remaining quality and spending gates. Consume the accepted interface, not a sibling branch.
Artifact owns its future reader adoption; do not rebuild the producer. Escalate
only when the work
requires a new product/authority decision, changes the agreed ownership
boundary, or encounters a real cross-lane conflict; ordinary implementation
and verification obstacles stay with the accountable lane.

**P1 replacement-time editor ownership — completed October 1:** this bounded
slice is implemented in the existing coordinated lane; no second branch is
needed. `travel-agent` owns which revision-bound correction is authorized, its
persistence/replay semantics and canonical readback. `travel-app` owns the
owner-only editor, interaction and validation, command/retry behavior, Undo
affordance, and refresh of the canonical reader. The workspace owns this
roadmap receipt and any cross-repo contract synchronization; generated API
snapshots and app types continue through the documented sync flow. The app's
native Save/refetch/Undo evidence is synthetic mock state only; authenticated
live app/backend readback remains unproven. Time authoring remains
explicit-offset only: the lane must not infer a zone from the device or place,
alter an explicitly supplied offset, or present an unverified time as
corrected. This slice is independent of research activation or consumer adoption.

**Write ownership:** thing/component and cultural-subject identity, reconciliation,
typed readings, focused reader internals, consumer collections and Life, approved
catalog/media adapters, exact kept editions and original-sharing semantics.
Do not infer cultural-subject capabilities from place-only entity enums.
Orchestration owns raw capture transport, native extension/session behavior,
Home/Places feeds and caller-side navigation. Strategy Technical owns the
general context/research/preparation machinery.

**Package split, not duplicate implementation:**

- P3 and shared P5 runtime/maintenance requirements are implemented by Technical
  R1–R5. Strategy owns their reader adapters and experience acceptance, not a
  second retrieval/generation/refresh engine.
- P0/P1 publish source/thing/subject/component references, revisions, typed
  readings and correction/withdrawal behavior. P4 owns exact retained editions;
  Technical owns prepared-result validity/reselection and consumes P4.
- P6 owns consumer collection membership, sharing/receiving and Life. Its
  Home/Places requirements are delivered by Orchestration. Publish the eligible
  projection/open target; do not edit their roots in parallel.
- PC owns approved subject/catalog matching and media-use decisions; it reuses
  shared acquisition/budget utilities where landed. Catalog facts do not grant
  permission for general research or establish present practical availability.

**Dependencies and useful fallback:** consume Technical's landed prepared-result
contract when available; meanwhile originals, catalog fallbacks, corrections,
collection organization and eligible original sharing remain complete work.
Provider approval gates that provider/use, not all reader development. P0's
unresolved owner/schema choices gate only dependent writes; inspect existing
owners and original renderers without inventing an unapproved schema.

**Operating agreement:** start from the program's common three-repository tuple
in a complete coordinated worktree. Keep one current assignment and its receipts
here. At start and meaningful landing checkpoints, inspect landed dependencies;
no routine inter-chat dispatch or waiting for the other roadmaps to finish.
Record an unavailable interface here and continue the independent work above.
Preserve original caller routes until their owning lane adopts replacements.
Follow the program's generated-file, migration, runtime and landing rules.

The latest source Strategy draft's design, research and six refinements are
preserved below. This ownership pass does not change pending provider, sharing,
retention or generation policy.

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

### Current merged execution baseline

The October 1 central integration landed the committed artifact-foundation
increments and adjacent dependencies with required hosted checks passing.
The inspected canonical main tuple for the next intake is:

| Repository | Accepted main revision |
| --- | --- |
| Workspace | `0b8792793fc25eceb8967edf7b832fe0f0194934` — PRs #41/#42/#43 |
| Backend | `0a1fdf224aaf59ca713eec5eba79a34321f038a9` — PR #241 |
| App | `acf5bd837fe3725b00d9744727f513a601fb2498` — PR #212 |

The retained artifact owner checkout still has older heads; this roadmap pass
does not rebase or move it. Refresh that existing coordinated lane at intake,
preserving any owner edits and checking the actual current main tuple.

This is the starting tuple for the next slice, not a new runtime test receipt.
Section 13 preserves earlier acceptance at its recorded revisions; the
[program baseline](vesper-program-roadmap.md#inspected-baseline-and-publication-state)
records the landing and immutable CI-pin distinction. Recheck status at intake;
another checkout's local `main` or uncommitted work is not this lane's baseline.

### Historical investigation baseline

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
Recheck actual HEADs and dirty work before implementation. At those inspections,
the newer strategy decisions and notes included uncommitted work; they were not
evidence of runtime conformance or a landed migration.

A later verification-instruction check used backend `e8bbb03a769ffc7a0072d5153673a3867fb2caae`
and app `212b87a4`. It confirmed the newer child static/bounded-merge commands
recorded in section 9. This was a command-policy check, not another full product
audit or an executed merge gate.

A further September 29 repository and primary-source review used backend
`3c170d21fc0ca9231b956f2b9de7f9f195231768` and app
`87eceee24512d9086962eea5b844cef9d7bffbeb` in the delivery checkout. Workspace
documentation advanced concurrently from `50e92512` to `7a5d434e`; the child
revisions stayed unchanged. This read-only review sharpened source-to-artifact
continuity, typed reading, input-format coverage, result reuse and provider-use
boundaries below. It ran no runtime/device tests or paid provider/model calls.

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

The following responsibilities guide package P0. The kept-thing identity
direction is accepted by the September 30 decision below; exact schemas and
the remaining mappings still need design. These are not shipped wire models
or an instruction to create a table for every row.

| Responsibility | Minimum distinction | Owning boundary |
| --- | --- | --- |
| Original | Source ID, content/custody revision, author, received time and permitted uses | Intake and Source custody |
| Recognizable thing | Stable owner reference and reversible source/recognition links; fields read from their existing authorities | Implemented initial `kept_things` owner in the existing backend/Postgres; the row is content-free and submission-backed. Cross-submission links/aliases and consumer reads remain unfinished. |
| Selected component | Stable component ID and source-revision-bound locator | Source/Intake evidence adapter, shared with composition and readers |
| Subject | Film, book, dish or Place identity | Entity/domain owner; not an occasion or attendance claim |
| Occasion and occurrence | A bounded occasion, original contributions, separately supported event claims | Experience Graph and existing operational owners |
| Collection membership | Thing reference, contributor, revision, removal/exclusion and audience consequence | Consumer collection owner; not the editorial guide collection table |
| Contextual selection | Selected target, viewer/purpose, candidate scope, context revision and eligible result references | Existing context/discovery owner |
| Prepared result | Exact generated output, input manifest, method version and current eligibility | Existing production/composition lifecycle |
| Kept edition | Exact chosen expression, stable edition reference and governed availability | Explicit saved-composition persistence owner |

#### P0 accepted kept thing identity boundary

The accepted [September 30 decision](../decisions/2026-09-30-kept-thing-identity.md)
establishes a thin, user-owned **Thing identity** (`ThingRef`) that
names what the person keeps, with original Sources, source-local recognition,
world Subjects, selected Components, and generated/kept expressions remaining
separate authorities. This is a narrow domain inside the existing backend,
not a new microservice or a completed cross-source migration. Once
reconciliation is implemented, it can satisfy the accepted ingestion rule:
two copies of the same ticket resolve to one kept thing while retaining both
Sources. The first persisted slice still leaves separate submissions distinct;
it does not turn every downstream concept into a generic Artifact row.

The table separates the accepted identity responsibilities from remaining
implementation recommendations: cultural-work schemas and stable Component
ownership are not approved merely by accepting the kept-thing boundary.

| Concept | Owner/reference boundary | Keep distinct from |
| --- | --- | --- |
| Original Source | Existing Intake/source-custody identity plus exact content revision and grants | Thing identity and extracted claims |
| Kept Thing | Stable owner-scoped `ThingRef`; the durable consumer target for Collections, readers, sharing, and cross-door reconciliation | Source bytes, ExperienceAnchor occurrence semantics, world-subject identity, and generated prose |
| Recognition | Existing submission-scoped candidate/observations, linked reversibly to a Thing when admitted or explicitly reconciled | Cross-submission identity: current `(submission_id, candidate_key)` is idempotency inside one submission, not the global identity |
| World Subject | Existing Place identity for physical places; a bounded cultural-work subject reference with work/edition distinctions remains the recommended design, not a selected schema | A person's ticket, copy, note, dish, or separate attendance contribution |
| Component | Proposed: a Thing-associated stable component reference only when a selected part must survive; its typed selector remains bound to exact Source/content revision | Raw coordinates/offsets as identity, or a new universal media-annotation platform |
| Experience / Occasion | Existing Experience Graph and operational owners; can relate Things and Subjects using supported evidence | A replacement identity for everything the person keeps |
| Reader descriptor | Optional, versioned `ArtifactReadingDescriptor` used to choose a renderer | Stable identity, catalog resolution, attendance, or permission |
| `ResourceRef` | Existing navigation/command address to an owner projection | The identity registry or data owner itself |

This means **do not** expand the current place-like `EntityRef` into a universal
personal Thing, and do not put source payloads, claims, collection membership,
Subjects, or generated editions into a universal Artifact table. The existing
EntityRef capability sets and persistence paths encode physical Place behavior;
World Foundry promotion rebuilds Place projections. Reusing those tables for
cultural works is a capability/owner migration, not a safe enum addition. On
the other side, keeping only submission-local Intake candidates cannot satisfy
cross-door identity or canonical Collection membership. A narrow Thing owner
is the accepted middle boundary. Its content-free owner, evidence-backed
reversible alias commands, owner read API and first native reader are now
implemented. Compatibility from existing candidate IDs into that stable owner
and downstream Collection consumption remain. Capture still owns candidate
truth under the September 8 lifecycle decision; a candidate is not silently
migrated or reclassified by this approval.

Before this identity slice can be considered integrated:

1. Preserve the delivered submission-backed row as the initial idempotent
   identity. Define how source and recognition references attach to it, how
   existing reader IDs remain compatible, and which future consumers resolve
   `ThingRef` rather than an Intake candidate.
2. Implement and verify evidence-backed reversible link/merge/split, retries,
   concurrency, migration and rollback. Preserve independent Source custody;
   never union grants when Things reconcile.
3. Keep cultural-work schema/capability changes explicit; they are not an enum
   addition to the existing physical Place owner. That separate design remains
   open and must not block source-backed kept-item identity unnecessarily.
4. Reuse the landed source-revision-bound text selection adapter. Stable
   cross-representation Component identity still needs a concrete retaining
   consumer and its own design; do not build a universal annotation platform.

These are implementation design obligations, not another founder approval gate
for the same kept-thing direction. Escalate changes that would alter the accepted
authority boundary; keep unrelated policy decisions separate.

The initial persistence slice materializes one content-free, owner-scoped
identity in the same Intake transaction that establishes verified private
retention; the unique owner/submission origin makes that write idempotent. The
new read API resolves an owner-scoped Thing and independently authorizes its
original Sources. The app can open a native Thing reader and return to the exact
Source. The existing candidate-backed reader target is unchanged, so ordinary
candidate IDs do not yet route through the stable identity. Separately retained
submissions can be reconciled only through the backend domain command today;
there is no merge/reversal HTTP route or user-facing control.

The bounded identity tests verify owner-confirmed evidence-backed linking,
retry safety, stale-revision conflicts, reversible aliases, and independently
authorized Sources. They do not establish automatic catalog matching, every
old candidate reference redirect, a user-facing merge/reversal flow, or
downstream Collection behavior. Each original remains separately addressable;
merging identity never copies a Source's permission to another Source.

**P1 initial identity grain:** the verified private Keep submission is the
idempotent origin and grouping boundary for one `ThingRef` contribution bundle.
This preserves the user's deliberate grouping before extraction; it does not
claim every source in the envelope is one semantic item. Keep the row
content-free and resolve eligible Sources and Capture candidates from their
current owners. Different submissions remain separate until evidenced,
revisioned reconciliation; reversible aliases preserve old references through
merge/split. Place this owner in the existing backend/Postgres system, in a
narrow `kept_things` SQLAlchemy Core table/repository, and create it in the
Intake transaction that establishes private retention. Do not reuse EntityRef,
ExperienceAnchor, the graph projection or editorial Collections as the Thing
owner. The first delivery is implemented in backend commit `0911ad063`: the
SQLAlchemy Core table/repository, Alembic backfill, and transactionally created
identity on verified private retention. Backend commit `cb7defc86` adds
owner-confirmed reversible alias commands and the owner read projection; app
commit `eb515f055` adds generated API consumption and a native original-first
Thing reader. Existing candidate-backed artifact IDs remain a separate read
target, the merge/reversal domain commands do not yet have HTTP write routes or
user-facing controls, and downstream Collection integration remains separate.

Code basis for this boundary: `travel-agent/backend/core/models/entity_identity.py`
and `backend/core/entity_types.py` define place-like `EntityRef` values and
capability subsets; `backend/core/db/entity_identity.py` resolves namespaced
external IDs only to those references. `backend/core/db/intake_semantics.py`
keys candidate replay by submission and candidate key, while
`backend/core/db/intake_anchors.py` projects confirmed candidates as
`ExperienceAnchorProjection`. `backend/core/models/execution_contract.py`
defines `ResourceRef` as a typed reopenable owner address, not a durable owner.
`backend/world_foundry/persist.py` promotes accepted facts through entity and
Place-content owners. These are implementation observations, not permission to
reuse or migrate those schemas.

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

The current entity capability sets describe place-like things, including
physical visit/page behavior. Do not add cultural subjects to those sets or
route them through `custom` without reviewing the inherited capabilities and
owner hydration. P0 chooses a bounded cultural owner exposed through existing
references, or a reviewed extension of the identity substrate. Namespace
external identifiers by provider and resource kind where needed; bare film,
TV or release IDs are not assumed globally interchangeable.

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

### Code-backed owner map and present reader boundary — October 1 update to the September 30 baseline

The following is an implementation inventory, not a decision to promote any
projection into a new canonical owner.

| Concern | Existing implementation and authority | What this establishes—and what it does not |
| --- | --- | --- |
| Source custody | Intake submissions, source objects, and retained-source lifecycle in `travel-agent/backend/core/db/intake_v2.py`; HTTP commands in `travel-agent/backend/api/routes/intake.py` | Source ownership and revocation exist. `DELETE /api/intake/submissions/{id}` revokes/scrubs the source; it is not a reversible artifact Undo. |
| Kept Thing identity | `travel-agent/backend/core/db/_tables/kept_things.py`, `travel-agent/backend/core/db/kept_things.py`, Alembic revisions `keptthing01`/`keptthing02`, and `travel-agent/backend/api/routes/artifact_projections.py`; app consumer in `travel-app/data/keptThings.ts` | Verified private Keeps create an idempotent content-free owner Thing. Evidence-backed, revisioned aliases now have authenticated merge/reversal routes and deliberate app controls; the ordinary candidate-to-bundle entry is connected. Every original is separately reauthorized; aliasing does not copy grants or claim semantic sameness. The reader still exposes originals, not a composed Thing title/summary. |
| Private consumer Collection | `travel-agent/backend/core/db/consumer_collections.py`, `travel-agent/backend/core/models/consumer_collection.py`, its authenticated route and `travel-app/data/consumerCollections.ts` | A private canonical Collection owns many-to-many stable ThingRefs. Index/detail and revision-bound lifecycle commands are consumed through generated types and session-scoped queries. Detail pagination carries the first page revision and rejects stale continuation. The app pairs each page with one bounded owner-authorized Thing batch, preserving membership order and identity; this is data composition, not an authorized member presentation. There is no native Life Collection detail. Shared membership and receiving remain unimplemented. |
| Confirmed thing/read target | Confirmed Intake candidates are projected by `travel-agent/backend/core/db/intake_anchors.py` as `ExperienceAnchorProjection`; the existing route remains `ResourceRef(kind="experience_anchor")` at `/you/memories/artifacts/{id}`. The stable kept-Thing route is `GET /api/artifact-projections/things/{thing_id}` and the app reader is `/you/memories/things/[id]`. | Candidate rows retain UUIDs across replay/status changes and use `(submission_id, candidate_key)` as their idempotent key. Existing IDs still open the candidate-backed reader; they are not automatically redirected or migrated to Thing. The current normal entry path can now open the Thing identity from an eligible candidate; the identities remain distinct and separately addressable. |
| Claims and correction | Intake observations/candidate revisions in `travel-agent/backend/core/db/intake_semantics.py`; source-bound projection in `travel-agent/backend/core/canonical_artifact_projection.py` | The owner reader exposes gated `wrong_time`, `separate_from_occasion`, `keep_occurrence_forget_interpretation`, and (when an explicit private target/revision is present) `replace_time`. The replacement editor preserves each aware instant's wall-clock date/time and explicit UTC offset, does not infer from device/place, binds Save and Undo to the current numeric revision, and refreshes the artifact after a successful command. Backend persistence and projection replay are already covered separately. Native keyboard/cancel and synthetic-mock Save/refetch/Undo evidence are recorded; authenticated live app/backend readback remains unproven. The form also has recorded UX follow-ups for raw UTC-offset entry and start/end place context. |
| Place and occurrence context | Physical `EntityRef` vocabulary in `travel-agent/backend/core/entity_types.py`; owner-scoped Experience Graph rows bridged by the artifact projection route | Place/time/Occasion/Plan context can be read from its existing owners. The place-like entity capability sets are not a cultural-work identity registry. |
| Selected component | Intake observations and `evidence_locator` validation in `travel-agent/backend/core/intake_evidence.py`; Technical's `read_selected_text_component_for_owner` in `travel-agent/backend/inbound/original_source_reader.py` (backend `63ac861ef`) | A backend-only adapter now refinds strict UTF-8 `text/plain` character spans against the selected Source ID and full source digest, with current custody checks and a 20,000-character cap. It is not stable cross-representation Component identity, PDF/OCR/image selection, or a mobile selection API. The current artifact reader still opens the whole source. |
| Life organization | Rebuildable viewer-specific groups and membership controls in `travel-agent/backend/life_projection/organization.py`, `travel-agent/backend/core/db/_tables/life_organization.py`, and `travel-agent/backend/core/db/life_organization.py` | Groups, memberships and controls are keyed by `viewer_id` and `projection_version`; memberships record evidence-backed derived relations to owner records. Durable controls rename a derived group, detach one derived membership, or undo that control. They provide useful revision/CAS and reversible-control patterns, but do not create or own a user's canonical Collection or its shared audience. |
| Existing editorial collections | Public `/api/collections` reads in `travel-agent/backend/api/routes/collections.py`, backed by editorial guide bundles in `travel-agent/backend/core/models/collections.py` and `travel-agent/backend/core/db/collections.py` | This is content for Discover, with typed editorial member entity references and published/draft state. Its API is not the accepted personal/shared Collection owner, and its member schema does not point to stable consumer Thing references. |
| Contextual selection and prepared additions | Strategy Technical's existing Source Contribution discovery, work, result, serving, and publication path (section 12); mobile adapters in `travel-app/hooks/` and request/read routes in `travel-agent/backend/api/routes/agent_workflows.py` | The producer/result path is reusable, but current app integration is Home/Places-rooted, not artifact-bound. See the request-boundary note below. |
| Kept edition | No kept-edition target or exact-snapshot action is exposed by the current canonical artifact projection/reader route | The current reader can reopen its original owner projection; it does not establish user-owned persistence of a generated explanation or a stable edition reference. P4 remains separate. |

#### Artifact-specific discovery request boundary — September 30

The Source Contribution producer and exact-result reader already exist; the
missing piece is not another research provider. The app's
`SourceContributionRoot` in
`travel-app/hooks/useSourceContributionResult.ts` is limited to
`home | places`; `useSubmitSourceContributionRequest.ts` and
`useRootSourceInspection.ts` submit and consume root jobs. The backend
contract in `travel-agent/backend/api/routes/agent_workflows.py` likewise
accepts only Home/Places in `allowed_roots` and requires any `context_ref` to be a
`places_context`. The request names subject/source/context refs and
`represented_at`, but has no selected artifact target, target revision, or
component locator. Consequently the current artifact reader cannot ask for and
reopen a prepared result bound to the exact item being viewed. P0 must settle
that target/revision/component contract before P3 adds an artifact adapter; do
not pass a submission-local `experience_anchor` through `context_ref` or label
a root-wide result as artifact-specific value. Exact kept-edition persistence
remains the separate P4 owner.

The merged Technical increments provide exact-original revision binding,
bounded public acquisition and the plain-text refind primitive above. Reuse
those owners; their presence does not extend this Home/Places request contract.
The first artifact-bound adapter needs an explicitly supported selected target,
revision, optional component and eligible result/readback contract from
Technical, plus current-authority and first-producer spend safeguards. Current
research telemetry is not complete provider-spend enforcement. Technical's
[execution state and receipts](product-map/adaptive-context-and-research-roadmap-2026-09-29.md#6-implementation-packages-and-execution-state)
own those producer limits; this lane owns reader adoption and acceptance.

#### Consumer Collection ownership decision — October 1

**Decision:** Strategy owns one bounded, canonical consumer-Collection domain
in the existing backend/Postgres system. It is the source of truth for
consumer-Collection identity and metadata, many-to-many membership by stable
`ThingRef`, collection-level audience, and owner-authorized membership and
lifecycle mutations under the accepted Collection decisions. Keep this a
domain in the existing service, not a new microservice or a universal content
store. It references kept Things; it does not copy Source payloads, take Source
custody, or become the owner of Thing identity.

**Presentation and projection:** Life owns the Life surface and its read
presentation/projection, not canonical Collection state. Home and Places may
present Collection-backed value through Orchestration-owned compositions. Any
mutation initiated from those roots must resolve back to the Strategy-owned
Collection owner; a Life group or root projection is not a write-through
authority. Strategy Technical supplies supported contextual results and
readback, not a competing Collection owner.

**Existing systems keep their present roles:** `life_organization` is a
viewer-specific, evidence-backed derived grouping/projection with reversible
local controls; it is not the canonical shared Collection owner. The public
editorial `/api/collections` domain is Discover guide content with catalog
entity members; it is not the user-owned Collection owner. Their revision,
idempotency, detach, and Undo patterns may inform the new domain, but neither
model is to be renamed, widened, or repurposed for consumer membership.

**Implementation status and limits:** the artifact lane now implements the
private canonical backend owner over stable kept Things: schema/migration,
owner-scoped index/detail reads, and revision-bound create, rename, add, remove
and soft-delete commands. Membership stores Thing references rather than Source
payloads; adding a Thing is currently limited to its owner, and deleting a
Collection preserves the Things. The authenticated operations are included in
the generated mobile contract, with typed app HTTP/API methods and mock parity
covered by focused lifecycle tests, along with session-scoped paginated React
Query data hooks. Life presentation and device acceptance remain unfinished.
This is not shared-Collection support:
other-owner contributions, recipient grants, whole-collection serving,
leave/withdrawal repair, and sharing UI remain unimplemented. Automatic
filing/default Collection behavior and Vesper-initiated shared additions remain
unresolved. The implementation does not settle notification batching or quiet
hours, or the exact recipient-grant implementation. It does not change the
accepted rule that a shared Collection is visible as a whole to its members.

The first delivered reader-mode matrix is deliberately narrow:

| Mode | Current behavior | Not implied |
| --- | --- | --- |
| Mine, confirmed `ExperienceAnchor`, recognized ticket/place/work with family-relevant source facts | Versioned descriptor may select the corresponding native reader; original-first fallback remains for missing facts, unknown types, or unsupported descriptor versions | Catalog match, validity, visit/attendance, external media, selected-part identity, or general input-format support |
| Mine, sparse/unrecognized anchor or recognized passage/dish/practical record | Recognized passages require a non-empty source-backed `excerpt`; practical records require supplied identity/place/provider/time/status details. Dish, sparse records/passages and unrecognized anchors use the source-fact/original fallback. | Author/work identity, calculated receipt or payment claims, a new family-specific schema, or generated interpretation |
| Together | Canonical artifact projection route rejects the request until graph-owned sharing authorization exists; private reader-family metadata is withheld | That an Occasion link or source-level sharing elsewhere grants this reader access |
| Catalog lookup, selected-part reading, contextual discovery, exact saved edition | Not connected by this reader increment | Any provider rights, answer generation, durable retention, or permission to share generated material |

### Supported source and artifact-mode crosswalk — September 30

Admission, interpretation, reader mode, and audience are separate gates. An
Intake submission reaching verified custody does not prove that its contents
were understood as an artifact, that a family reader is available, or that the
artifact can be shared.

| Door or representation | Custody and reader evidence | Limit that remains |
| --- | --- | --- |
| App text, camera/photo library, and OS share capture | Intake v2 accepts inline text and supported selected/captured sources. Exact image, text, audio, and calendar representations have owner-reader coverage in the app; image inspection uses the shared zoom surface. | This proves supported bytes and the source reader, not that every source yields a recognized artifact family. App preflight and backend byte validation reject PDF, Apple Wallet (`.pkpass`), and HEIC/HEIF today. |
| Forwarded email | Subject/body enters as private inline text; numbered admitted attachments reuse Intake custody. `tests/inbound/test_email_forward_v2.py::test_v2_email_rejects_valid_sibling_with_scanner_gated_attachment` proves the entire unsupported bundle is rejected before Intake state or uploaded bytes are created. | All-or-nothing at 15 files / 8 MiB aggregate, within the 10 MB webhook cap; no sender-facing failure notice. No external mail delivery or sender readback is proven. |
| Explicit original delivery | A specific received original is inspectable only while the selected delivery is active, unexpired, and currently authorized for that recipient. The image reader uses that exact authorized URI/token and resets when eligibility changes. | This is not Together access to the sender's canonical artifact, its other sources, or collections. No grant is inferred from a shared Occasion or fixture. |
| PDF, PKPass, HEIC/HEIF, or unsupported audio representation | No admitted Intake-v2 source reader is promised for rejected bytes. | A registered normalizer, upstream file picker, or ticket-like appearance does not override the scanner/decoder gate. |

| Artifact reader mode | Current app behavior | Not connected / not implied |
| --- | --- | --- |
| Mine · transport/admission ticket | Versioned ticket reader only when the owner projection has a supported descriptor and family facts; otherwise source-fact/original fallback. | Valid ticket, attendance, catalog identity, stable selected admission, or PDF/Wallet support. |
| Mine · place anchor | Source-backed place treatment when place/time facts qualify; otherwise source-fact/original fallback. | Resolved venue, visit claim, map, catalog details, or availability. |
| Mine · book/film/show/music | Medium-specific text-built face when recognized with family facts; the submitted source remains reachable and no catalog art is assumed. | Work/edition identity resolution, licensed media, or a general subject page. |
| Mine · passage | Text-built “as kept” treatment only with a recognized descriptor and non-empty source-backed excerpt; other supplied facts remain bounded details. | Author/book/edition identity, surrounding context, or generated interpretation. |
| Mine · practical record | Neutral “as kept” sheet when a recognized descriptor and supplied identity/place/provider/time/status detail are present; otherwise generic source-fact/original fallback. | Totals, payment state, validity, or other calculated/inferred facts. |
| Mine · dish; sparse or unknown format | Generic source-fact/original reader, including when a descriptor is recognized but lacks the fields required for a designed reader. | A specialized dish face, inferred meaning, or completion of missing facts. |
| Together · canonical artifact | Not served by this private owner projection until the graph-owned sharing authorization path exists. Static shared fixtures test presentation/redaction only. | Production multiplayer artifact reading, membership authority, or publication. |
| Selected component, catalog, contextual discovery, kept edition | No stable selected-part reference or artifact-bound prepared-result/saved-edition handoff in this reader. | OCR region identity, external provider rights, generated context, or silent persistence. |

The format-reader tests, owner-original checks, email bundle rejection,
private/Together fixtures, and September 30 disposable-Postgres artifact-route
replay give bounded evidence for these stated behaviors. The route replay
proves persisted owner readback, non-owner denial, withdrawal, and explicit
submission deletion for one confirmed Intake candidate. This crosswalk does
not prove that every door recognizes every family; that claim remains
unsupported until cross-door identity and owner readback are implemented and
tested.

Descriptor support proves only the confirmed-reader route. It does not establish
which source doors or representations reach that route. The current door and
format boundary is:

| Door or layer | Current path and admitted scope | Failure/evidence boundary |
| --- | --- | --- |
| App text and file capture | `travel-app/utils/intakeCaptureService.ts` and `travel-app/hooks/useCaptureDraftController.ts` submit inline text or 1–16 selected/captured sources through Intake v2. Origins include Chat, camera/photo library, and iOS/Android share capture. The app preflight rejects PDF, Apple Wallet (`.pkpass`), and HEIC/HEIF; the backend still validates actual bytes. | This is an app preflight plus owner upload/finalize contract, not a guarantee that every OS-shared representation can be decoded or semantically read. An unsupported item blocks the selected app bundle before its V2 submission. |
| Forwarded email | The SendGrid route supplies message text plus numbered attachments to `travel-agent/backend/inbound/email_forward.py`. The current limit is 15 attachments and 8 MiB aggregate; every attachment is validated before the Intake row, private attachment upload, or raw archive is written. | Unsupported content rejects the whole email, including otherwise-valid text/siblings; there is no sender-facing failure notice. `tests/inbound/test_email_forward_v2.py::test_v2_email_rejects_valid_sibling_with_scanner_gated_attachment` now proves a valid PNG before a scanner-gated PDF creates no submission, archive, or uploaded bytes. It does not prove sender-visible delivery/readback. |
| Backend byte admission and normalization | The active Intake v2 boundary supports server-decodable image, audio, text, and calendar sources. The normalizer registry includes JPEG/PNG/GIF/WebP, text/calendar, and audio metadata normalization; the audio normalizer still requires a separate transcription adapter. PDF and PKPass normalizers exist but V2 rejects them until the scanner lane is enabled; HEIC/HEIF is rejected. | A registered parser is not permission to admit a format; a MIME normalizer is not proof of semantic extraction or a family reader. PDF/Wallet support, HEIC conversion, mixed-bundle partial success, and every email combination remain unsupported. |

The reader-mode matrix now has code-backed boundaries for its first app doors,
including the all-or-nothing email case and one database-backed confirmed-
artifact lifecycle through the canonical reader route. A separate sparse-
history fixture in `travel-app/constants/mocks/artifactPortfolioFixtures.ts`
admits a private Sorrento opening from only one viewer observation and one
public research source. Its test retains the observation and sourced geology,
and excludes the later lift/ferry movement synthesis because those personal
sources are absent. This proves the existing composition compiler accepts that
bounded shape; it does not prove live model generation, current-source
verification, successful native rendering, or human desirability. P0 still
needs selected-part representation fixtures and a clearer caller-visible
rejection/receipt for unsupported email content. Exercise those against the
owner routes; do not change Orchestration's transport or enable a scanner from
this artifact lane.

### Typed reading contract

Experience semantics and reader formats are separate dimensions: existing
semantic families such as `attendance` and `attention` do not become the UI
family enum for tickets, books or albums. The first runtime increment is the
optional `ArtifactReadingDescriptor` on `CanonicalArtifactProjectionV1`,
version `artifact-reading.v1`. A maintained backend registry maps known source
artifact types to a bounded presentation family/format and reports whether
family-relevant facts survived owner projection. The app dispatches known
travel/admission tickets to a native ticket reader; unknown types, unsupported
versions and recognized records without family facts retain the original-first
source-fact reader. This descriptor does not resolve a cultural subject, imply
ticket validity/attendance, or author UI geometry. It is an adapter milestone,
not the complete typed-field contract. It is emitted only for the owner's Mine
view; Together stays generic until the sharing owner explicitly authorizes the
family metadata. P0 still needs to specify each reader's
required/optional fields, uncertainty, units, timezones, selected components
and unknown-version behavior. A maintained registry is sufficient; no
arbitrary model-authored schema or new UI framework is required. Backend wire
models and generated app types remain authoritative.

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

Define that equivalence explicitly, separately from retry tokens and exact
edition identity. The reuse fingerprint or reviewed compatibility rule covers
selected target/component and representation revision, job/purpose, materially
relevant context, eligible input manifest, and method/policy versions. A new
work-item key cannot compensate for an inner cache that ignores those inputs.
Existing Home/Places grouping retains its own contract; extending it for P3
does not establish that current Home serving is defective. Reuse still requires
current eligibility and sufficiently current discovery, including empty results.

Keep model calls outside database locks. A short publication transaction must
check the current attempt, owner/grant revisions and expected selection
generation before publishing the result and pointer. Read-time authorization
remains necessary. Existing reader checks are protection, not a reason to
assume publication races are solved; absence of a fence is not by itself proof
of a user-visible leak.

## 4 Delivery sequence and package dependencies

Use one Strategy owner with bounded internal subagents only when authorized.
The waves describe experience dependencies across the three assigned lanes,
not calendar estimates or additional permanent lanes. Execution is active in
this coordinated Strategy lane; section 0 records landed slices, while each
package's remaining gates stay open until their stated evidence exists.

| Package | Outcome | Entry dependency | Primary responsibility |
| --- | --- | --- | --- |
| P0 | Agreed shared contracts and evidence portfolio | Common baseline; program's assigned boundaries | Strategy-owned identity/reading seams; Technical owns producer contracts |
| P1 | Recognizable identity, correction, parts and collection continuity | P0; existing capture custody | Strategy |
| PC | Catalog anchoring and licensed media | P0; approved sources for live provider use, not fallback work | Strategy catalog owner, retaining existing Places domain authority |
| P2 | Immediate focused reader and exact return | P0 and usable source adapters; not all of P1 | Strategy |
| P3 | Substantive selected-object discovery | P0 and available owner reads; staged P1 collection integration | Technical R1/R2 with first-producer safeguards; Strategy reader adapter |
| P4 | Kept editions and dependent correction | P0, P2 and a typed prepared-result seam; minimum snapshot at the first adopted retention trigger, broader UX after worthwhile additions | Strategy |
| P5 | Selective refresh and accountable spend | Minimum safeguards accompany first P3; broader maintenance follows value, P4 for saved-edition replay | Technical R3/R4/R5; Strategy retains P1/P4 repair |
| P6 | Shared value and cross-root continuity | Originals: relevant P1/P2 and existing sharing contracts; generated results: P3 and, when retained, P4/P5; grants for each behavior | Strategy collections/receiving/Life; Orchestration Home/Places |
| P7 | Whole-system hardening and controlled exposure | Evidence work starts in P0; completion follows selected product scope | Each lane validates its boundary; program checkpoint assesses combined experience |

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
or the safeguards required by an already running producer. If an adopted
retention trigger applies earlier, ship P4's minimum exact snapshot and
dependency seam with that behavior; broader saved-edition UX can still wait.

**Wave D:** complete the selected P6 root/social journeys and P7 hardening.
An original-focused scope can reach this checkpoint without all of Wave C.
Expand exposure according to evidence and existing release authority, not
merely because all package branches have commits.

## 5 Detailed engineering packages

### P0 Shared contracts and implementation admission

**Deliver:** one reviewed owner/interface map and a common lifecycle portfolio
that allows reader, retrieval and maintenance work to proceed independently.

- Recheck actual worktrees, runtime ownership, pending work and the program's
  lane boundaries. Consume Orchestration's existing capture path; do not take
  over its transport files when implementing identity or sharing semantics.
- The September 30 code-backed map in section 3 now ties existing owners to
  concrete types, routes, and mutation paths. Carry the accepted September
  28 Collections and September 29 Life semantics into owner contracts; do not
  reopen them while deciding their implementation. Review the remaining thin
  identity/reconciliation mapping and where consumer collection persistence
  belongs. The accepted Life organization projection and editorial guide
  collections are not the consumer Collection owner by implication.
  Name the cultural-subject owner, stable local references, external mappings
  and work/edition distinctions before PC and P2 choose incompatible models.
  Review the physical capability assumptions and external ID namespaces in
  section 3 instead of treating this as an enum-only extension.
- Specify selected component, selected-object context, prepared result and
  kept-edition references. Reuse owner revisions and existing action envelopes.
  Define the typed reading adapter and semantic reuse contract in section 3;
  independently authored native fixtures do not establish backend compatibility.
  Strategy owns target/component/reading and kept-edition references; Technical
  owns prepared-result execution and reuse. Declare the consumer's required
  target/purpose/revision semantics without independently implementing that cache.
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
  sharing separately, with the supported entry doors and file representations
  for each first-delivery path. Ticket-family support does not imply PDF,
  Wallet or every email attachment works. The inspected intake blocks PDF and
  Wallet pending a document scanner and rejects HEIC/HEIF unless an upstream
  path converts it to a supported format. Exercise the actual door and the
  rejection/receipt when an unsupported attachment rejects an email bundle;
  do not assume supported siblings were retained. Enabling a scanner or changing
  partial-bundle admission is explicit scoped work, never a security bypass.
  Every provider, format and reader need not finish before delivery can begin.
- Agree on complete assignments and shared-file ownership. Any new schema or
  authority choice receives the required founder review before it is treated
  as settled; this is not repeated permission for ordinary implementation.

**Acceptance:** each scenario can be traced through a named owner, revision,
reader and repair route; backend/app share the same definitions. No owner is
invented by a mock adapter. Open decisions name only the work they actually block.

### P1 Recognizable objects and collection continuity

**Deliver:** a kept contribution becomes an inspectable thing with stable
identity and addressable originals, independent of its entry door.

- Reuse Intake and its immediate private Keep/Undo path as the source-retention
  trigger for Thing creation/attachment. Upload, extraction, and the UI's
  “Keep this interpretation”/candidate-confirmation action do not themselves
  grant raw-source retention; Capture accepts the interpretation, while Intake
  owns whether the original remains retained. Preserve provisional extraction,
  source ordering, original access and unsupported-type fallback.
- Bridge kept-source and confirmed-artifact readers through a stable consumer
  open target. Recognition may improve a provisional reading without requiring
  candidate confirmation. Through confirmation, correction and candidate
  withdrawal while Source custody remains eligible, preserve selected sources/
  components, attached originals and collection references using existing
  custody/owner identities and a thin resolver.
  Source revocation still removes access. Do not create duplicate durable
  artifacts merely to switch readers.
  **Delivered boundary:** an eligible original now links back to its existing
  confirmed candidate/anchor only when active evidence names the exact source
  object and custody-bound content digest. The private interpretation read is
  owner-session scoped and rechecked on return. This does not establish durable
  component identity across OCR or representation replacement.
- Add source-bound components for multiple admissions or passages. Preserve
  originals through OCR correction, representation replacement and partial
  extraction failure. Never synthesize unreadable details to fill a template.
- Implement evidence-backed reconciliation of repeated captures. Persist the
  reason, supporting identifiers and reversible links. Ambiguous cases remain
  separate until evidence supports convergence; do not ask for classification
  before providing the original's value.
  - Repair successive original-record corrections as distinct commands with
  expected revisions. Reassess the inspected candidate/action idempotency
  coupling. The revisioned time path now replaces source-extracted time claims
  in both compiler and owner-scoped artifact reads, with the correction record
  as provenance; a later `wrong_time` correction removes that time from the
  canonical artifact projection. The persisted lifecycle test now also exercises
  all four revisioned semantic correction actions in sequence, including exact
  retry, changed-payload conflict, stale-revision conflict, latest-correction
  readback, and preservation of the original extracted observation. Concurrent
  different commands at one revision now prove a single winner and stale loser;
  concurrent retries of one command prove one persisted effect. Sequential
  owner corrections now traverse the authenticated Intake route and verify the
  canonical artifact readback. The mobile replacement-time editor and Undo are
  implemented; its registered native Save/refetch/Undo exercise is synthetic
  mock state, while authenticated live app/backend readback remains open. These
  corrections do not depend on generated editions.
- Separate event/valid time, received time and freshness. The entity-fact
  writer now derives `valid_to` only from an explicit asserted end; freshness
  `expires_at` remains separate and current selectors still enforce it. Its
  `valid_from` convenience default remains `observed_at` for current-state
  claims, so historical producers must provide event-time bounds explicitly.
  Preserve captured facts and their provenance when current subject facts change.
- Establish consumer collection membership through its chosen owner, including
  explicit removal/exclusions, many-to-many membership and deletion semantics.
  Silent private filing is different from sharing or creating new structure.
- Represent one occasion holding multiple originals without creating the
  retired journey/chapter/day ownership hierarchy. Operational commitments
  stay with their domain owners.
- Keep artifact-family normalization bounded and versioned. Reuse semantic
  forms through section 3's typed reading adapter, distinct from semantic-family
  classification; do not implement the pending self-promoting catalog,
  arbitrary model-authored schemas or a bespoke screen per interest.

**Acceptance:** email/screenshot of a proven same ticket converge without
losing sources; two screenings remain separate; a multi-admission image opens
the selected admission; complementary meal evidence stays attributed; removing
one membership and deleting the collection do not delete the thing. Source
deletion and Undo cannot resurrect through indexing or retry. Two legitimate
date corrections both apply, their retry applies once, and unrelated evidence
survives. Historical event time does not become upload time or catalog freshness.
Keep an unclassified supported image, open it immediately, finish recognition
while it is open, confirm/correct it, and reopen the same selection. The original,
collection references and return context survive without false confirmation.

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
- **Minimize public lookup inputs.** Extend the existing typed public-request
  pattern with approved title/year/artist/ISBN or canonical venue discriminators.
  Keep raw OCR, private attendee/traveler/recipient names, admission barcodes,
  booking references, credential-bearing URLs, private constraints and friends'
  notes out of catalog/discovery requests and their logs/shared cache keys.
  Public artist/author/director identifiers can remain approved discriminators.
  Private matching stays inside its authorized boundary; custody alone does not
  authorize external disclosure. P3 reuses this rule rather than sending
  free-form private context to public search.
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
- **Approve particular source uses:** display/attribution, storage and delivery,
  inference/indexing, sharing/export and retained-edition eligibility. Record
  field/media provenance, applicable policy version and expiry where relevant.
  Metadata access does not establish artwork rights or every downstream use;
  training and inference permissions are not interchangeable. Extend existing
  media policy and delivery contracts, not a parallel rights service or blanket
  immutable image cache. Source selection and its permitted uses remain the
  founder decision in section 6; unsupported uses stay disabled.
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
    subject lookups. The inspected image normalizer does not already perform
    OCR; interpretation currently uses a model. Measure that path before
    introducing a separate extraction stack or claiming a fast path exists.
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
- Missing or withdrawn art falls back according to its use policy, including
  provider-specific blank-image responses, not only network errors. The original
  survives; an exact kept edition never silently substitutes different artwork.
- Required attribution appears; display-only or non-retainable material cannot
  enter an unapproved inference, index, shared or retained-edition path.
- A private-ticket fixture containing names, barcodes and booking references
  produces an actual outgoing request containing only approved discriminators.
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
  **Delivered increment:** a passage's source-backed `excerpt` is now emitted
  by the owner projection and shown in a restrained “as kept” reader when the
  recognized descriptor and excerpt are both present. This does not select a
  part inside a longer original or identify its author/work; dish and practical
  records were subsequently given a source-only “as kept” sheet. It requires
  supplied structured details and calculates no amount/payment state. Dish
  records still use honest source-fact/original fallback.
- Reuse a common original-inspection interaction across Intake, confirmed
  artifacts and received originals, retaining each owner's authorization adapter.
  Test dense print, zoom/pan, selected parts, supported text copying and dismissal
  back to the reading. Evaluate existing image/gallery and platform text-selection
  capabilities before adding a native OCR dependency; inspection is not durable
  extraction or a source selector.
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
  Reserve known media geometry; late recognition, artwork or additions must not
  move controls under a finger, reset accessibility focus, or insert content
  above the active reading position. Preserve selection as the object improves.
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
Actual semantic output must reach the family renderer through the generated
contract, including uncertainty and unknown-version fallback. Exercise the
kept-to-recognized transition and inspect the same small-print original after
Keep, confirmation and authorized receiving, including multiple large images.

Retain reviewed original-first specimens across the portfolio: readable
admission details, photograph inspection, a passage with its supplied source
context, and usable structured record details. They must preserve personal specificity
and appropriate interaction rather than cosmetic variants of a generic information
card. Design review can identify weaknesses and select a treatment; desirability
to ordinary users remains a hypothesis until the human comparison.

**Design boundary:** exact density and aesthetic treatment need design review,
but source access, route continuity, eligibility and data contracts can advance
before final composition is frozen.

**Implementation increments:** travel and admission ticket formats have a
typed dispatch path; place records receive a compact source-backed place,
neighborhood and time treatment without a map or resolved-venue claim; and
book/film/show/music records use text-built medium-specific house forms without
catalog or generated art. Other reading formats still use the generic
source-fact/original reader; this does not imply that PDF, Wallet, every email
attachment or complete native acceptance is available. The canonical reader
exposes owner correction for time, Occasion separation and interpretation
hiding, plus the replacement-time editor and Undo. That replacement-time path
has a registered native mock-state Save/refetch/Undo flow, not authenticated
live-service readback. Source deletion remains with Intake/Source custody;
deleting a Source is not a reversible correction or a promise that revoked
material can be restored. Reliable photo pinch/pan, actual VoiceOver
traversal/actions, loading/error coverage, Android/physical-device behavior and
wider native acceptance remain open.

### P3 Contextual discovery and useful selection

**Implementation owner:** Strategy Technical R1/R2 with required R3–R5 safeguards.
The requirements below remain part of this experience; Strategy implements the
P2 receiving adapter, not the shared producer.

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
  separately before expressing a practical option. Apply PC's typed public-query
  and source-use boundaries before external requests, indexing or synthesis.
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
- Extend production reuse with section 3's semantic equivalence contract.
  Changing selected component, purpose or materially relevant context must not
  reuse incompatible output merely because source bytes or group IDs match.
  Keep command retries and exact-result reopening separate from this decision.
- Separate candidate discovery from relationship/value judgment. Preserve
  original-only, attributed juxtaposition, single-source explanation, supported
  comparison and practical continuation as legitimate treatments.
- Keep the existing Home-specific two-source/cross-root producer contract for
  its own job. Create a reviewed focused-artifact policy at its owning seam;
  do not globally weaken existing gates or force a second source as padding.
- Distinguish user-supplied knowledge, kept explanations and passive exposure.
  Test semantic repeats and useful new mechanisms on familiar premises.
- Use bounded research to resolve a specified public uncertainty **or discover
  candidates for a named purpose**, anchored to the selected object and relevant
  circumstances. This matches the public-world discovery requirement above and
  [Technical R1](product-map/adaptive-context-and-research-roadmap-2026-09-29.md#r1-generalize-bounded-acquisition).
  Discovery proposes candidates; verification must support any presented claim.
  Both paths require permitted public terms, source-use rights, finite limits
  and applicable spend admission. This planning clarification enables no new
  live/paid caller, ambient research or disclosure policy. Reuse governed public
  evidence across private matching where licenses and freshness allow; never
  share personalized synthesis through a public cache.
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

**Retention boundary:** P3 can remain ephemeral only while no adopted retention
trigger applies. Explicit Keep/share, an exact governed reference, or citation,
action, repair or collaboration requiring a stable expression invokes the
existing persistence policy. Ship P4's minimum exact snapshot and dependency
seam with the first such behavior, or keep that behavior unavailable. This is
not permission to adopt unresolved shared-derivative policy or retain every Ask.

### P4 Exact kept editions and dependent correction

**Deliver:** the person can retain a named explanation and reopen exactly what
they chose, with honest correction and availability over time.

**Staging:** broader saved-edition UX follows worthwhile additions. Minimum
retention support follows the actual trigger, including those beyond Keep/share
listed in the [owner policy](../systems/artifact-expression-and-composition.md#persistence-policy).
Current production-cache readback is not an immutable edition store.

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

**Implementation owner:** Strategy Technical R3/R4 and related R5 applicability.
Strategy retains P1 original repair and P4 exact-edition storage/repair; catalog
PC retains its own approved-use obligations. No second maintenance queue here.

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
  selection first; reuse equivalent eligible prepared content under section 3's
  fingerprint/compatibility rule. Generate only under a supported request or
  adopted preparation policy. Broader P5 deferral does not defer correct P3 reuse.
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

**Implementation split:** Strategy owns collection/social operations, recipient
readers and Life. Orchestration owns Home/Places placements and caller return.
Technical supplies only the permitted generated-result/readback capability.

**Deliver:** artifacts become more valuable through authorized people and
different roots without duplicating material or inventing a second social feed.

**Staging:** preserve and extend eligible exact-original sharing and receiving
as soon as the relevant P1/P2 and existing sharing contracts support it.
The private owner-only Collection backend foundation exists; shared Collection
serving additionally requires owner-to-owner membership, audience grants,
recipient readback, removal/leave repair and native acceptance. Neither waits
for P3, P4 or broad P5. Generated-result circulation needs P3's
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
| Kept Thing identity and reconciliation | Accepted September 30: a narrow stable kept-thing domain, separate from Sources, candidates, Subjects and generated editions, inside the existing backend. Initial submission-backed storage and migration are implemented; cross-source compatibility and reversible reconciliation remain. | Unsafe or unspecified migration/alias compatibility and downstream reads, not another approval of the identity direction | Existing readers and the delivered private-Keep identity writer |
| Components and cultural subjects | Stable cross-representation Component identity and cultural-work schemas remain design recommendations; review physical capabilities, external ID namespaces and typed readings | Dependent component/catalog schema changes | Existing source-bound selectors and kept-thing identity work |
| Consumer collection owner | Product semantics are accepted: user-owned collections, many-to-many membership, whole-collection visibility, and explicit Remove/Delete. The viewer-scoped derived Life organization and public editorial guide collections remain separate read/projection and editorial owners. A distinct canonical owner over stable kept-Thing references now has private backend schema and owner-only operations; Vesper-initiated additions to shared collections remain a separate pending policy choice. | Shared audience/receiving semantics and their recipient read/withdrawal repair; native Life integration | Implemented private Collection persistence and management API; single-object private reader and owner-linked discovery |
| Kept edition after supporting withdrawal | Recommended default: withhold affected content, preserve only permitted metadata, offer a new independently supported version; exact policy unadopted | Shared derivative retention and partial salvage promises | Private originals and edition mechanics tested without disputed shared material |
| Offline retained material | Adopt what can be cached, for how long and how reconnect handles loss; no instant remote revocation promise | Persistent shared offline caches and their user promise | Online reader, locally available independently eligible originals under existing rules |
| Automatic preparation | Separate selection refresh from generation; define allowed triggers and budget owner | New proactive generation/background posture | Existing explicit requests, pure reads and cheap authorized selection |
| Initial families, input paths and reader density | Map designed families in P0 by supported door, representation and mode; explicitly scope scanner or partial-email admission work | Final family-specific visual acceptance and exposure of unsupported input paths | Shared reader/data/lifecycle foundations and supported photo/text paths |
| Catalog sources and permitted uses | Choose per-medium sources and approve display, storage/delivery, inference/indexing, sharing/export and retention uses, with terms and costs | Each unapproved use of provider art/data, not every integration at once | House-design fallbacks, reader foundations, identity work |
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
| Recognition completes during reading, then confirmation/correction | Same selected thing, original and collection reference remain openable; no forced confirmation, shifted controls or lost return position |
| Same source, different admission or explanation versus practical purpose | Incompatible output is not reused; unchanged eligible scope reuses without generation |
| Same retry token with changed parameters | Reject the parameter mismatch rather than returning a result for a different request |
| Location or purpose changes | Select new context without moving the original or changing an active reading |
| Grant loss during generation | Current publication/read guards deny affected output; index cleanup is not the safety boundary |
| Concurrent edits and worker takeover | Older revisions/leases cannot publish over current state |
| Crash before call | Bounded recovery can resume without claiming a paid call occurred |
| Crash after provider response before commit | At most one current published result; duplicate provider spend remains possible |
| Database new, index old, then stale hit | Incomplete discovery or valid fallback; owner hydration rejects stale/ineligible content |
| Burst import and repeated opens | Bounded fan-out and coalesced work; unchanged opens require no generation |
| Source expiry while screen remains open | Stale content/actions become unavailable, with stable navigation and honest recovery |
| Withdrawal after Keep | Apply adopted derivative policy; preserve independent originals and no revoked content resurrection |
| Exact expression cited or acted through under a retention trigger | Retain the required snapshot/dependencies before that behavior is supported; later context does not rewrite the referenced result |
| Catalog art removed or not retainable | Preserve personal original and subject identity; block unapproved reuse and do not replace media inside an exact edition silently |
| Unsupported file in a mixed email bundle | Exercise actual admission/rejection and sender-facing receipt or its documented absence; do not imply supported siblings were kept |
| Account switch and offline reconnect | No prior-account late response/cache leakage; current grants rechecked on reconnect |

Record time to original access, recognizable object and useful extension separately,
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
- Follow current root/child AGENTS and the [CI Plan](../reliability/CI%20Plan.md).
  Use `make verify-changed WORKSPACE_BASE_REF=<base> AGENT_BASE_REF=<base> APP_BASE_REF=<base>`
  as local merge preflight in the actual coordinated lane. Full `make verify`
  is diagnostic/release coverage, not a mandatory rerun on every push. Required
  hosted checks remain authoritative. A defined command is not evidence it ran.
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
| After P0 | Do owners, typed readings, selectors, reuse semantics and policy boundaries fit supported families, input paths and modes? | Approve interfaces and first-delivery coverage; resolve only actual blockers |
| First connected P1/PC/P2 result | Do real supported inputs stay inspectable and recognizable through recognition/correction, including no-match/provider failure and historical-versus-current facts? | Accept supported reader/catalog modes without requiring every family or P3 |
| First connected P2/P3 result | Does a worthwhile addition meet the usable reader, with changed-scope reuse, permission, publication and spend safeguards exercised? | Adjust reader/selection together; supply minimum retention for any triggered behavior and decide whether broader P4/P5 now earn work |
| P4/P5 lifecycle replay | Do change, exact retention, revocation, index lag and spend behave coherently? | Harden affected seams or revise the abstraction before broadening |
| P6 receiving and P7 integration | Can a sparse-history person and a thin social participant receive complete value? | Review originals as soon as ready; add derivative cases only when supported, then choose exposure under existing authority |

Checkpoints guide direction; they are not a demand to pause after every small
technical obstacle. No single movie-ticket demo certifies the whole product.
Original-only value is the immediate foundation, not a substitute for the
connected P2/P3 checkpoint demonstrating a substantive addition. Neither that
addition nor human preference is required for every original or sharing path.

## 10 Operational delegation

One Strategy owner carries its assignment through implementation, focused
verification, review corrections and landing in its own coordinated worktree.
Use bounded in-session subagents only when delegation is authorized and writes
are disjoint; P0–P7 are packages, not additional permanent lanes.

Within this lane, reader work and approved catalog adapters can proceed
independently once their owned interfaces are settled. Shared identity,
collection writes and migration ownership stay explicit. General research and
runtime implementation belongs to Strategy Technical; root composition and
entry transport belong to Orchestration.

Follow the [program operating agreement](vesper-program-roadmap.md#6-autonomous-execution-and-landing).
Consume landed contracts, not a changing sibling checkout. Publish additive
P0/interface work before holding it behind every renderer. No direct owner-to-owner
chat relay is required. Escalate unresolved product/authority choices or a genuinely
incompatible interface; ordinary debugging continues in this lane. Land coherent
increments, not every small commit or one branch after the entire roadmap ends.
Update only this roadmap's current assignment and evidence, leaving the other
lanes' queues and checkouts untouched.

<a id="11-recommended-first-assignment"></a>

## 11 Historical first assignment and completed foundation receipts

Continue **P0 plus the necessary P1 foundation, PC catalog anchoring for the
first families, and P2 reader integration** from the merged baseline in section
2. The original-first reader and correction increments are landed; do not
restart baseline preparation or treat the whole assignment as complete. Existing custody
is its input; raw capture transport remains Orchestration's work.
The first families are those already designed (section 1A): tickets, venue
anchors, and books, films, shows and music. P0 distinguishes their shared-contract
coverage from supported first-delivery modes and honest fallbacks; every family
and provider need not finish at once.

### Completed connected slice — owner-controlled reconciliation, October 1

**Outcome:** an owner can connect two stable saved-bundle identities from an
occurrence-specific reader without changing candidate identity, claiming the
bundles are semantically the same object, or weakening exact-Source
permissions. The user controls the connection; Vesper cannot infer or apply it.

1. **Authenticated reconciliation transport — implemented and verified.** The
   revision-bound route requires owner identity, current source/target
   revisions, one exact currently retained Source from each bundle, a command
   ID and explicit `keep_bundles_together` confirmation. Exact retry resolves
   idempotently; a route test verifies a stale-revision conflict is returned as
   409, while PostgreSQL tests cover persisted exact retry and command reuse.
   Intake remains the authority for Source access.
2. **Deliberate owner interaction — implemented and verified.** The app shows
   eligible saved bundles, preselects one currently readable original from
   each, allows inspection or changing the evidence, and asks for explicit
   confirmation. It never merges from model confidence, shared Subject
   identity or byte similarity. A target-source read failure is shown as an
   error with retry and disables confirmation rather than looking empty.
   `Separate` reverses the connection directly, without free-text rationale.
   Candidate/anchor IDs remain occurrence-specific; Life and Collection
   consume Thing references without owning or copying identity.
3. **Persisted behavior — bounded local evidence.** Tests cover one
   owner-confirmed connection and exact retry, distinct save identities,
   independent Source revocation, and reversal that restores both original
   references. Separate Postgres concurrency acceptance now covers concurrent
   exact merge/reversal retries and competing opposite-direction merges; see
   section 13. These tests do not establish semantic sameness, production
   authentication or cross-client acceptance.
4. **Reader acceptance remains independent.** Loading/error component behavior
   has focused tests. Reliable photo pan/pinch and actual VoiceOver cases remain
   open until a device runtime is available. Retain Android/physical-device and
   authenticated live-service readback as explicit boundaries; do not claim
   every reader state is accepted or repeat captures without a concrete defect
   hypothesis.

### Implemented editor and next connected acceptance — October 1

**Outcome:** an owner can explicitly correct an artifact's private event-time
interpretation from the canonical reader without changing the submitted
original or guessing the event timezone from the device's current location.

1. **Backend authority — already implemented and separately verified.** The
   typed `replace_time` command is revision-bound, idempotent for an exact
   retry, replayed through the canonical anchor and reversible through the
   existing owner correction/Undo contract. The October 1 backend increment
   exposes its action only when the projection has an explicit private target
   and current revision; no database migration was needed.
2. **Native owner editor — implemented.** `Mine` exposes `Replace the time` only
   for that explicit correction target. The sheet edits separate start/end
   calendar date, wall-clock time and numeric UTC offset; it preserves the
   captured offsets, uses UTC only as the neutral picker coordinate, does not
   derive a timezone, and explains that the original remains untouched. Save
   binds the current revision and payload-specific command identity, keeps the
   draft after failure, refetches the artifact on success, and exposes existing
   owner-only Undo when the refreshed projection allows it.
3. **Focused proof — passed with a bounded native claim.** Four app test suites
   (51 tests) and the app typecheck passed; targeted ESLint had no warnings or
   errors. The backend projection suite (27 tests), Ruff check/format and
   workspace contract audit passed. A fresh native iOS 18.2 build on the exact
   `iPhone SE (3rd generation)` used for capture resolved the stale installed
   Worklets binary. Registered run `20261001T153024Z-canonical-artifact-reader`,
   recaptured against the finalized acceptance wording, captured the software
   keyboard while the focused offset/helper remain
   visible, then used Enter to dismiss it and scrolled to reachable Save/Cancel
   controls; the flow cancelled back to the same artifact (1/1). The fresh
   capture and structured verdict are recorded in the app as
   `20261001T153024Z`. A manual synthetic-field check entered
   `-04:00` with on-screen keys; because that makes the end precede the start,
   the editor showed its validation message and disabled Save, and Cancel
returned to the unchanged artifact.
The later five-flow portfolio captured on the lane's `Vesper QA SE` simulator
at app revision `3c2bf4b71` does **not** repeat that keyboard proof: its focused
offset screenshot has no visible software keyboard. The editor, shared
`FormField`, and `BottomSheet` code are unchanged between `51d275d11` and
`3c2bf4b71`; the cause is therefore not established as an app regression. Keep
the earlier iPhone SE proof bounded to that simulator/run and leave current
assigned-device keyboard acceptance open pending a correctly configured
recapture.
4. **Boundary of this keyboard/validation/cancel capture:** no correction was
   submitted in this scenario; backend readback, deployed authentication,
   Android/physical-device behavior, or user preference was not proven by this
   capture. The later mock-mode round-trip below is a separate synthetic-state
   proof, not service persistence. The verdict retains two minor UX follow-ups:
   raw UTC notation is technical for ordinary owners, and Start/End lack
   associated place labels when the artifact contains distinct event locations.
   Address those without weakening the rule that Vesper never silently infers
   the event timezone.

#### Mock-mode correction parity checkpoint — completed October 1

The dedicated synthetic QA artifact (`qa-replacement-time-editor`) now has an
in-memory, revision-bound correction projection behind the existing app
API/data seam. Save updates the effective event time without rewriting the
original submitted evidence; a fresh canonical-artifact read shows the
replacement and owner-only Undo; Undo restores the prior effective time,
including across successive corrections. Exact retries are idempotent, stale
revisions conflict, invalid explicit offsets are rejected, and resetting mock
state restores the original fixture. An unrelated mock candidate retains its
existing behavior. No backend schema, OpenAPI, generated wire types,
real-service behavior, or ordinary mock candidate was changed.

Focused tests cover initial direct-save resolution, replacement/readback,
exact retry, stale-revision rejection, invalid input, successive corrections,
Undo/readback and reset. A separate registered native iOS 18.2 mock-mode
Save/refetch/Undo scenario passed while the existing keyboard/validation/cancel
capture remains intact. The native evidence is explicitly synthetic mock-state
evidence—not backend persistence, deployed authentication, or service
readback. The displayed time-window projection now preserves both dates and
explicit offsets across a day boundary; this improves legibility but does not
resolve the recorded UTC-notation or start/end place-label UX follow-ups. No
user preference or product-policy decision is implied.

**Connected receiving checkpoint — completed October 2:** the focused Life
artifact reader adopts Technical's exact-result contract through the generated
mobile API projection, typed transport and session/account-scoped data facade.
It is gated to an explicit result reference and exact eligible original; no
screen triggers producer work. This does not require Thing migration or imply
broader P1/PC/P2 completion. The next open gate is comparative evidence of
supported addition quality, usefulness and remaining effort. Broader P3
generation remains behind its authority, lineage, publication and spend
boundaries, not unrelated visual polish.

### Foundation completion criteria

For a fast first release:

- Preserve landed revision-bound corrections and Undo. The mobile
  replacement-time editor has bounded native keyboard, validation and cancel
  evidence, plus a native synthetic-mock Save/refetch/Undo round-trip. The
  authenticated live app/backend persistence and readback acceptance remains
  open; do not infer an event timezone or overstate the synthetic capture.
- The thin P3 read-only receiver is connected in the existing Life/artifact
  reader behind an internal default-off flag. Keep it there until the existing
  quality, authority and spend gates are met; do not treat a synthetic fixture
  or a successful read as evidence that additions are useful.
- Include permission, publication, input-lineage and spend safeguards with
  the first live P3; include provider limits with PC.
- Defer saved editions and broader archive maintenance until additions show
  people value, except for minimum exact-snapshot support at any adopted
  retention trigger. Do not defer safeguards required by already running work.
- Advance eligible original sharing and receiving with the relevant P1/P2 and
  sharing contracts; only generated derivatives wait for their later dependencies.

The finish condition is not a document alone:

- shared target/component/edition, typed reading and semantic reuse contracts
  are mapped and reviewed, without conflating semantic and presentation families;
- eligible kept originals from existing supported doors open through the same
  references before and after recognition/confirmation/correction, with honest
  selected-part, unresolved-catalog and fallback behavior;
- actual first-delivery file formats and mixed-bundle failure behavior are
  exercised; no unsupported scanner path is implied by ticket-family coverage;
- distinct source/date corrections and retries behave correctly, and refreshed
  subject facts never overwrite historical captured facts;
- subject identity is application-owned, provider mappings are reversible,
  and work/edition distinctions preserve both shared and specific evidence;
- approved catalog integrations obey use-specific rights, public-query limits,
  freshness, attribution and provider budgets; unresolved provider decisions
  do not block the original/fallback reader;
- collection and reconciliation ownership are explicit, with the adopted
  portion connected rather than improvised in a screen;
- exact return, common original inspection, stable progressive reading and
  expiry/authority behavior have focused test coverage;
- original-first family specimens have concrete visual/interaction review,
  preserving the submitted material's specificity; do not postpone the whole
  desirability question as later polish or claim measured user preference;
- the P0 family/mode matrix, portfolio fixtures and lifecycle replay inputs
  are ready for P3 and the relevant P5 stages;
- unresolved shared policy remains isolated behind its explicit boundary.

Adopt the Technical lane's P3 output as soon as its selected-object/context
interfaces and eligible owner reads are landed, while P1/P2 work continues. Do not wait
for every first-assignment finish condition, complete collection writes or
broader edition persistence beyond any triggered minimum. Review the first
connected P1/PC/P2 foundation, then the connected P2/P3 result; neither checkpoint
waits for all families. Prepare P4
and broader P5 contract tests in parallel where files are independent, while
the minimum producer safeguards and any triggered retention support ship with P3.
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
- [Confirmed artifact route](../../travel-agent/backend/api/routes/artifact_projections.py),
  [retained-source projection](../../travel-agent/backend/core/db/intake_anchors.py),
  [semantic families](../../travel-agent/backend/inbound/semantic_contract.py),
  [native reading adapter](../../travel-app/utils/canonicalArtifactView.ts),
  [entity capabilities](../../travel-agent/backend/core/entity_types.py),
  [intake format boundary](../../travel-agent/backend/inbound/v2_security.py)
  and [email admission](../../travel-agent/backend/inbound/email_forward.py).
- [Media policy](../../travel-agent/backend/media/policy.py),
  [public Places query boundary](../../travel-agent/backend/places/FEATURE.md),
  [source inspection](../../travel-app/components/inbound/OriginalMaterialView.tsx)
  and [artifact gallery](../../travel-app/components/artifacts/ArtifactMediaPreview.tsx).
- [Atlas retrieval](../../travel-agent/backend/core/vector/atlas.py),
  [Source discovery](../../travel-agent/backend/root_projection/v2/source_contribution_discovery.py),
  [selection](../../travel-agent/backend/root_projection/v2/source_contribution_opportunities.py),
  [known-to-person checks](../../travel-agent/backend/root_projection/v2/known_to_person.py).
- [Exact result references](../../travel-agent/backend/core/source_contribution_result.py),
  [serving](../../travel-agent/backend/root_projection/v2/source_contribution_serving.py),
  [producer](../../travel-agent/backend/root_projection/v2/source_contribution_producer.py),
  [publication and invalidation](../../travel-agent/backend/core/db/source_contributions.py),
  [work-item identity](../../travel-agent/backend/core/models/source_contribution_work.py),
  [continuity handoff](../../travel-agent/backend/root_projection/v2/source_contribution_canonical_executor.py),
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
- [IIIF Presentation](https://iiif.io/api/presentation/3.0/): distinguish compound
  objects, representations, annotations and rights. Borrow those distinctions,
  not a new IIIF/JSON-LD platform or a substitute for semantic retrieval.
- [AWS idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/):
  retry identity follows intent; changed parameters under one token are rejected.
  Artifact result reuse still needs its own explicit equivalence contract.
- [TMDB licensing FAQ](https://developer.themoviedb.org/docs/faq) and
  [Places policies](https://developers.google.com/maps/documentation/places/web-service/policies):
  access, commercial licensing, attribution and storage are bounded by source
  terms. They do not establish Vesper's negotiated rights or blanket permission
  for downstream inference, sharing or retention; approve those uses explicitly.
- [Expo SDK 55 Image](https://docs.expo.dev/versions/v55.0.0/sdk/image/): existing
  iOS Live Text interaction is an inspection option to evaluate, not backend OCR,
  a durable selector, or a cross-platform capability promise.
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

The dated receipts below preserve their original publication states and evidence
boundaries. October 1 central integration landed their committed increments;
section 2 and the current assignment supersede historical “local/unmerged” and
“next” wording. Landing does not broaden a receipt into product acceptance.

This document records planning, code-backed owner mapping, and bounded local
implementation receipts. The September 30 follow-on checkpoint started from
workspace HEAD `61486071`, backend `d6730f6d6`, and app `d7401a2ec` in the
coordinated `codex/artifact-foundation` worktree. Subsequent commits added
backend correction-replay coverage (`3cecd34f6`), an owner-scoped exact-original
projection (`0cbd4b6a7`), the app's exact inspect route (`14b40fea6`), and
generated API snapshots (`f3b693890`), and a registered exact-original reader
QA scenario (`f84ea3419`). The September 30 continuation added an app-side
original-to-record link (`fa07c85c4`) and disposable-Postgres owner-readback
coverage through the authenticated Intake route (`5dbc29353`, extended by
`ac946ba0b`), followed by canonical artifact-reader lifecycle coverage
(`9c775cd03`). The October 1 continuation added app mock correction parity
(`de36dcd86`) and committed the registered native verdict/manifest
(`51d275d11`). Focused evidence:

| Boundary | Command | Result and limit |
| --- | --- | --- |
| P1 initial Thing persistence | Backend `0911ad063`; `DATABASE_URL=postgresql://vesper:localdev@localhost:64743/vesper_artifact_backfill_test .venv/bin/alembic upgrade head`; `TEST_DATABASE_URL=postgresql://vesper:localdev@localhost:64743/vesper_artifact_test TEST_DATABASE_DISPOSABLE=1 .venv/bin/python -B -m pytest -p no:cacheprovider tests/inbound/test_kept_things_postgres.py tests/inbound/test_chat_keep_handoff_postgres.py tests/inbound/test_intake_subject_postgres.py -q`; `make verify-changed WORKSPACE_BASE_REF=38a2388aaa6c79c7a8e16149beabbc935f4b86b9 AGENT_BASE_REF=0911ad0639b8b9cfa3ae48e9740e6e5432106685 APP_BASE_REF=e7bdc660501eaa19234e6b45bda033658edaa2d4` with temporary Ruff/mypy caches and `PYTEST_ADDOPTS='-p no:cacheprovider'` | Nine disposable-Postgres tests passed. A synthetic retained submission seeded before `keptthing01` upgraded was backfilled as exactly one owner-matching identity row. `verify-changed` passed: static gates, 22,082 passed / 14 skipped / 1 xfailed / 52 xpassed offline tests, OpenAPI/app-projection/generated-type and cross-repo contracts, and docs links/spine/canon checks. Two Qdrant local-mode warnings; no failed tests. This proves only local submission-backed identity persistence and backfill. No Thing API/client reader, cross-submission merge/split, Collection integration, deployed-service, or user-value evidence. |
| Backend email admission | `PYTHONPATH=. .venv/bin/python -m pytest -p no:cacheprovider tests/inbound/test_email_forward_v2.py -q` | 17 passed at backend `d6730f6d6`; mock-based owner-boundary behavior, no DB/provider delivery evidence. Includes valid-PNG + scanner-gated-PDF whole-bundle rejection. |
| Backend test quality | `ruff check --cache-dir /private/tmp/vesper-artifact-ruff tests/inbound/test_email_forward_v2.py` and `ruff format --check --cache-dir /private/tmp/vesper-artifact-ruff tests/inbound/test_email_forward_v2.py` | Both passed; backend commit hooks also passed Ruff, formatting, Vulture, and secret checks. |
| Backend correction replay | `PYTHONPATH=. .venv/bin/python -m pytest -p no:cacheprovider tests/inbound/test_anchor_runtime.py tests/inbound/test_intake_anchor_projection.py tests/core/test_canonical_artifact_projection.py tests/api/test_artifact_projections.py -q` | 49 passed at backend `3cecd34f6`; replay selects the newest semantic correction while ignoring a confirmation audit row, is deterministic, and preserves original source lineage/hash as interpretation claims change. Fixture-level evidence only; no database concurrency or persisted replay proof. |
| P1 successive typed-time correction foundation | Backend `df3fa9ec8`; app `9aee57049` (implementation `804e9ede1`). `ruff check --no-cache …` and `ruff format --check --no-cache …`; focused backend suite (`tests/inbound/test_intake_semantics_contract.py`, `tests/inbound/test_anchor_runtime.py`, `tests/core/test_canonical_artifact_projection.py`, `tests/api/test_intake_route.py`, `tests/inbound/test_candidate_owner_lifecycle_postgres.py`, excluding guarded DB/API-key/dogfood markers); disposable-Postgres case `test_revisioned_time_corrections_apply_successively_and_dedupe_exact_retry`; app `npx tsc --noEmit --pretty false`, `npm run test:typecheck:contracts`; targeted reader/action Jest tests; `./scripts/sync-types.sh` and `npm run generate-api-types:check` | Backend lint/format passed; 78 focused offline tests passed (2 deselected); the explicitly disposable lane-Postgres case passed, proving two successive typed replacements, exact retry deduplication, stale-revision and changed-payload conflicts, separate persisted corrections, and unchanged original evidence. OpenAPI snapshot, app projection and generated types synced offline and generation check passed; app typecheck, test contract typecheck, and 18 targeted tests passed. The UI regression proves the same command ID is reused after an ambiguous failure. Existing reader corrections now submit command ID + current numeric revision. No live API or native UI proof. This completes only the command/owner foundation: no mobile replacement-time editor is exposed until time-zone authoring can preserve the original zone or require an explicit choice; other P1 identity, component, collection and reconciliation work remains open. |
| P1 post-keep artifact handoff | App `debc65b1c`; `npm test -- --runInBand __tests__/screens/share-capture-intake-v2.test.tsx`; `npx tsc --noEmit --pretty false`; `npm run test:typecheck:contracts` | 28 screen tests passed; the new case proves “Open artifact” is available only after the owner keeps an interpretation and routes the candidate/anchor ID into the existing canonical reader while “Forget” and “Done” remain. This is mocked navigation, not a live API or native simulator result. It closes the immediate capture-to-reader door only; the reverse original-to-record link was still open at this checkpoint and is covered by the following receipt. Stable source/component identity remains open P1 work. |
| P1 original-to-record continuity | App `da5c6b8fa` plus lineage hardening `fa07c85c4`; `npm test -- --runInBand __tests__/utils/intakeArtifactContinuity.test.ts __tests__/screens/intake-submission.test.tsx __tests__/data/intake-source-removal-lifetime.test.tsx __tests__/data/intakeReadAuthority.test.tsx __tests__/utils/queryKeys.test.ts`; `npm run typecheck`; `npm run test:typecheck:contracts`; targeted `npx eslint …`; `npm run qa:polish:scenarios`; `npm run qa:design:check -- canonical-artifact-reader`; `npm run qa:polish -- canonical-artifact-reader --doctor` | 65 tests passed; typecheck, test-contract typecheck, scenario IDs (31), design-ref check, and whitespace checks passed. The link uses confirmed candidate/anchor identity only when active observation lineage matches the exact submission, source ID, and custody-bound digest, with owner-session scoped interpretation cache, entry/return revalidation, withdrawal/revocation/expiry guards, and no duplicate artifact. Targeted ESLint had zero errors; the existing original-reader max-lines warning remains (850 baseline code lines; 889 after this change). No live API evidence. Design-ref check is doctrine-only with no pinned design reference. Native QA preflight was blocked because Metro was not reachable on `:8081`; no screenshot or native visual acceptance. |
| P1 exact original-to-record backend readback | Backend `5dbc29353`, extended by route-level coverage `ac946ba0b`; `TEST_DATABASE_DISPOSABLE=1` against a newly created lane-local disposable DB; `PYTHONPATH=. .venv/bin/python -m pytest -p no:cacheprovider tests/inbound/test_candidate_owner_lifecycle_postgres.py -q`; offline `PYTHONPATH=. .venv/bin/python -m pytest -p no:cacheprovider tests/inbound/test_intake_semantics_contract.py -q`; `ruff check --no-cache tests/inbound/test_candidate_owner_lifecycle_postgres.py`; `ruff format --check --no-cache tests/inbound/test_candidate_owner_lifecycle_postgres.py` | Both Postgres lifecycle tests passed and 17 offline semantic-contract tests passed. The DB-backed authenticated-route assertion proves the actual `GET /api/intake/submissions/{id}/interpretations` response returns the confirmed active observation with its exact source ID, source-content digest and custody receipt; another owner receives 404, and withdrawal is reflected in the same route’s readback. Ruff and formatting passed, as did backend commit hooks. The task-specific database was dropped and only the Postgres service started for this run was stopped; the lane’s default database and volume were preserved. This is real route + persisted-DB evidence with a test dependency override for identity, not deployed-service or native/mobile acceptance; no schema or API contract changed. |
| Backend exact-original projection | `PYTHONPATH=. .venv/bin/python -m pytest -p no:cacheprovider tests/core/test_canonical_artifact_projection.py tests/core/test_intake_anchor_originals.py tests/api/test_artifact_projections.py tests/inbound/test_anchor_runtime.py tests/inbound/test_intake_anchor_projection.py -q` | 59 passed at backend `0cbd4b6a7`; private owner projection includes up to 16 supported exact source/revision references, excludes them from Together, and withholds inspection for unsupported, revoked or unverified originals. Fixture/unit/API-route evidence; no disposable-Postgres readback or concurrency proof. |
| App exact-original inspection | `npm test -- --runInBand __tests__/utils/canonicalArtifactActions.test.ts __tests__/screens/canonical-artifact-reader.test.tsx __tests__/components/canonicalArtifactCard.test.tsx __tests__/screens/intake-submission.test.tsx`; `npm run typecheck`; targeted `npx eslint …` | 65 passed; exact source ID and revision reach the existing Intake reader, with a chooser for multiple originals. Typecheck and targeted lint passed at app `14b40fea6`; screen mocks exercise routing, not native bytes, image zoom or device interaction. |
| P2 exact-original photo inspection | App `c4b287de0`, transform-test follow-up `1da37e6c2`; manual QA fallback `72a4b8f41`; `npx jest --runInBand __tests__/utils/artifactPhotoZoom.test.ts __tests__/components/canonicalArtifactCard.test.tsx __tests__/components/photo-intake/PhotoViewerSurface.test.tsx`; `npm run typecheck`; `npm run test:typecheck:contracts`; targeted `npx eslint …`; `npm run size-budgets`; `npm run qa:polish:scenarios`; `npm run qa:design:check -- canonical-artifact-reader`; `VESPER_METRO_URL=http://127.0.0.1:64747 npm run qa:polish -- canonical-artifact-reader --doctor`; `npm run docs:check` | 26 focused tests passed; typecheck, test-contract typecheck, targeted lint, size budget, 31 scenario IDs, docs checks and whitespace check passed. The exact selected private original supports pinch zoom, bounded pan, double-tap zoom and screen-reader zoom actions; geometry and gesture-transition tests cover fit, stationary/moving focal points, bounds and recentering. It remains memory-only (`cachePolicy="none"`). Design refs are doctrine-only. The lane-configured QA attempt was blocked before capture: CoreSimulator was unavailable, then the runner could not create its temporary lock directory in the managed checkout (`EPERM`). The reader contract now defines a manual device/VoiceOver checklist, but that checklist was not run; physical gesture, screen-reader and screenshot acceptance remain open. |
| P2 shared exact-photo inspection across Life readers | App `cde109f78`; `npx jest --runInBand __tests__/utils/photoZoom.test.ts __tests__/components/canonicalArtifactCard.test.tsx __tests__/components/photo-intake/PhotoViewerSurface.test.tsx __tests__/screens/intake-submission.test.tsx __tests__/screens/original-delivery.test.tsx`; `npx jest --runInBand __tests__/screens/original-sender.test.tsx __tests__/screens/intake-submission.test.tsx __tests__/screens/original-delivery.test.tsx`; `npm run verify:merge -- --base main`; `npm run qa:polish:test`; `npm run typecheck`; `npm run test:typecheck:contracts`; `npm run qa:polish:scenarios`; `npm run docs:check`; `npm run size-budgets`; `npm run api-boundaries`; `npm run schema-bridge`; `npm run home-surface-budgets`; cacheless `npx eslint --no-cache app components` | Focused reader tests passed (77), then 55 sender/intake/recipient tests passed after updating the existing sender screen's mock for the newly consumed interpretation-poll hook. Full merge scope passed: 1,285 suites, 9,075 tests, 1 snapshot. The polish harness, typechecks, docs, size, API-boundary, schema-bridge, Home budget, polish scenario-ID checks and `git diff --check` passed. Direct cacheless ESLint passed with 0 errors and 169 warnings; the `verify:fast` Expo lint wrapper could not write `.expo/cache/eslint` (`EPERM`). The Life native doctor and dry-run did not reach capture because CoreSimulator was unavailable and the runner could not create its temporary lock/screenshot paths (`EPERM`). The shared zoom component now serves the same exact image source in private Intake, current received-original authorization, and canonical artifact readers; loss of custody/authorization, image failure, delivery change or expiry closes/resets the viewer. No original bytes are disk-cached. No device gesture, VoiceOver, or screenshot acceptance is claimed. |
| P0 first artifact-family fixture portfolio | App `c154e5826`; `npx jest --runInBand __tests__/components/canonicalArtifactCard.test.tsx __tests__/utils/canonicalArtifactPortfolio.test.ts __tests__/utils/canonicalArtifactActions.test.ts __tests__/utils/canonicalArtifactRenderProfile.test.ts __tests__/utils/canonicalArtifactRelationships.test.ts`; `npm run typecheck`; `npm run test:typecheck:contracts`; targeted `npx eslint --no-cache constants/mocks/canonicalArtifactFixtures.ts __tests__/components/canonicalArtifactCard.test.tsx __tests__/utils/canonicalArtifactPortfolio.test.ts`; `npm run verify:merge -- --base main` | Focused portfolio/render/action tests passed: 5 suites, 47 tests; both TypeScript checks and targeted lint passed. Full app merge scope passed: 1,286 suites, 9,089 tests, 1 snapshot. Reusable development/test specimens now cover all four designed work formats plus passage, dish and practical-record fallbacks, a sparse recognized film, and a bounded friend contribution. Tests verify renderer fallback, no catalog/generated art assumption, private-to-Together fixture redaction and no private-original access in the friend fixture. These are static mock projections only: they do not prove backend reader coverage, actual sharing authorization/publication, catalog identity, or persisted owner behavior. |
| P0 supported source and artifact-mode crosswalk | Backend `PYTHONPATH=. .venv/bin/python -m pytest -p no:cacheprovider -m "not requires_postgres and not requires_api_keys and not requires_dogfood_wedge" tests/inbound/test_intake_semantics_contract.py tests/core/test_intake_anchor_originals.py tests/core/test_canonical_artifact_projection.py tests/inbound/test_anchor_runtime.py tests/inbound/test_intake_v2_replay_identity.py tests/inbound/test_email_forward_v2.py -q`; app `npx jest --runInBand __tests__/screens/intake-submission.test.tsx __tests__/utils/intakeSourceOriginal.test.ts __tests__/utils/api/mockIntakeV2.test.ts __tests__/utils/api/captureIntakeApi.test.ts __tests__/screens/original-delivery.test.tsx __tests__/utils/canonicalArtifactPortfolio.test.ts`; workspace `make docs-check` | 79 backend offline tests and 100 app tests across 6 suites passed; workspace documentation checks passed with the crosswalk. Tests cover source custody/admission, supported original representations, private original projection, supported reader/fallback modes, fixture redaction, recipient authorization, and fail-closed email attachment rejection. These are bounded unit/route/mock checks; no external email delivery, production file decoder, cross-door identity reconciliation, production Together artifact authorization, or disposable-Postgres run is claimed. |
| App registered QA and native attempt | `npm run qa:polish:scenarios`; `npm run qa:polish:surfaces`; `npm run qa:polish:test`; `VESPER_METRO_URL=http://192.168.1.153:64747 npm run qa:polish -- canonical-artifact-reader --device='Vesper QA SE' --flow=polish/canonical-artifact-reader` | Scenario/surface registries passed (31/47); the harness suite passed. App `f84ea3419` registers an exact calendar-original open/return flow with a fixture bound to the existing mock source and Together redaction. The native attempt reached the assigned iOS 18.2 simulator but stopped at the runner's readiness gate: its installed dev app crashed with Reanimated/Worklets JS/native mismatch (0.7.4 vs 0.11.3). `npx expo run:ios --device 51A7A2C0-49CB-487E-A056-A771361EFA9B --no-bundler --no-build-cache` could not produce a replacement: Xcode 26.5 failed to load the generated CocoaPods project containing the RaTeX Swift-package product (`_setSavedArchiveVersion` selector error), followed by missing module-map errors. Only the redbox was captured; no product screenshots exist. Native visual acceptance remains pending. |
| Generated API contract | `./scripts/sync-types.sh` | Offline export, app projection and generated TypeScript completed after adding `ArtifactOriginalReference` and revisioned typed correction fields; the static fixture was updated before sync passed. Generated snapshot commit `f3b693890` predates the September 30 correction contract update in this lane. |
| App reader fallbacks | `npm test -- --runInBand __tests__/components/canonicalArtifactCard.test.tsx` | 18 passed at app `d7401a2ec`, covering ticket/place/work readers and generic fallback for passage/dish/practical-record descriptors. |
| App static/registered inventory | `npm run typecheck`; targeted `npm run lint -- __tests__/components/canonicalArtifactCard.test.tsx`; `npm run qa:polish:scenarios` | Passed; scenario inventory is 31 registered IDs. No screenshot was captured and this is not native visual acceptance. |
| Workspace documentation | `make docs-check` (after `make docs-status-sync`) | Passed on workspace `f3b693890` plus this roadmap and generated-current-state edits in the working tree; both receipts landed together as workspace `ab0a3522`. Includes governance, child governance, inventory, spine, canon, release, generated status, links, compatibility and Home-surface checks. |

### September 30 lifecycle extension

| Boundary | Command | Result and limit |
| --- | --- | --- |
| P2 source-bound passage reader | Backend `4b29a3125` and lineage assertion `48ca8c790`; `PYTHONPATH=. .venv/bin/python -m pytest -p no:cacheprovider tests/core/test_canonical_artifact_projection.py -q`; targeted `ruff check --no-cache …` and `ruff format --check --no-cache …`; app `8df9bf93e`; `npm test -- --runInBand --no-cache __tests__/components/canonicalArtifactCard.test.tsx`; `npm run typecheck`; targeted `npx eslint --no-cache …`; app contract `3c87bbef3`; app `npm run docs:check` | 23 backend projection tests and 21 app component tests passed. The backend now returns a source-backed `excerpt` fact and marks it family-relevant; the regression proves exact excerpt value and active observation source lineage. The app renders “PASSAGE · AS KEPT” only with a recognized descriptor and non-empty excerpt, shows supplied place/source-note facts, and falls back when the excerpt is missing. TypeScript, targeted lint/format, commit hooks and app docs checks passed. Generated wire shape is unchanged; no catalog/author/work inference, selected part within a longer original, live backend, native screenshot, or visual-preference claim. A standalone Metro server did start on the assigned lane port, but registered `--doctor` still stopped before capture: CoreSimulatorService was unavailable and the harness could not create its run lock under the managed checkout (`EPERM`). A full `dev.sh` attempt also could not start the API because `ANTHROPIC_API_KEY` is absent; the exact lane Postgres/Qdrant containers were stopped afterward without deleting their volumes. No successful native capture is claimed. |
| P2 source-only practical-record reader | App `cb82e8abe`; `npm test -- --runInBand --no-cache __tests__/components/canonicalArtifactCard.test.tsx`; `npm run typecheck`; `npm run test:typecheck:contracts`; `npm run generate-api-types:check`; `npx eslint --no-cache components/artifacts/ArtifactFamilyReader.tsx components/artifacts/PracticalRecordArtifactReader.tsx __tests__/components/canonicalArtifactCard.test.tsx`; app contract `04394b889`; `npm run docs:check` | 22 reader tests passed. A recognized practical-record descriptor uses a neutral structured sheet only when supplied identity/place/provider/time/status details exist; sparse cases stay generic. Tests prove source facts are shown and no total/payment assertion is introduced. TypeScript, test-contract typecheck, generated API snapshot check, targeted lint, app docs headers/links and hooks passed. No backend schema/API change, receipt arithmetic, live backend, native screenshot, or visual-preference claim. Native acceptance is blocked by CoreSimulatorService and managed-checkout lock-path failures recorded in the passage-reader row above. |
| Backend source/reader regression after P2 changes | `PYTHONPATH=. .venv/bin/python -m pytest -p no:cacheprovider -m 'not requires_postgres and not requires_api_keys and not requires_dogfood_wedge' tests/inbound/test_intake_semantics_contract.py tests/core/test_intake_anchor_originals.py tests/core/test_canonical_artifact_projection.py tests/api/test_artifact_projections.py tests/inbound/test_anchor_runtime.py -q` | 67 offline tests passed at backend `48ca8c790`; covers Intake semantics, exact-original projection, canonical reader family facts, API projection and anchor replay. No database, API key, or dogfood evidence. |
| P1 canonical artifact reader lifecycle | Backend commit `9c775cd03`; `DATABASE_URL=postgresql://vesper:localdev@127.0.0.1:64743/artifact_lifecycle_20260930_01 PYTHONPATH=. .venv/bin/python -m alembic upgrade head`; `TEST_DATABASE_URL=postgresql://vesper:localdev@127.0.0.1:64743/artifact_lifecycle_20260930_01 TEST_DATABASE_DISPOSABLE=1 TRAVEL_APP_ROOT=../travel-app SKIP_AUTH=true PYTHONPATH=. .venv/bin/python -m pytest -p no:cacheprovider tests/inbound/test_candidate_owner_lifecycle_postgres.py -q`; offline `PYTHONPATH=. .venv/bin/python -m pytest -p no:cacheprovider -m 'not requires_postgres and not requires_api_keys and not requires_dogfood_wedge' tests/inbound/test_intake_semantics_contract.py tests/core/test_intake_anchor_originals.py tests/core/test_canonical_artifact_projection.py tests/api/test_artifact_projections.py tests/inbound/test_anchor_runtime.py -q`; `ruff check --no-cache tests/inbound/test_candidate_owner_lifecycle_postgres.py`; `ruff format --check --no-cache tests/inbound/test_candidate_owner_lifecycle_postgres.py` | Three Postgres lifecycle tests passed. The authenticated canonical artifact route proves persisted readback of a confirmed source-bound candidate, non-owner denial (404), candidate withdrawal (404), and 404 after actual `delete_submission`; source-loss restore remains fenced. The new database was migrated and dropped inside this lane's PostGIS service, then the service was returned to its prior stopped state; the lane's default database and volume were preserved. The 66-test offline source/reader suite, Ruff, formatting, and backend commit hooks passed. TestClient uses an identity dependency override; this is not deployed-service or native/mobile acceptance, and no schema/API contract changed. |
| P1 validity and freshness separation | Backend `cfdbae9da`; `DATABASE_URL=postgresql://vesper:localdev@127.0.0.1:64743/artifact_validity_20260930_01 PYTHONPATH=. .venv/bin/python -m alembic upgrade head`; `TEST_DATABASE_URL=postgresql://vesper:localdev@127.0.0.1:64743/artifact_validity_20260930_01 TEST_DATABASE_DISPOSABLE=1 TRAVEL_APP_ROOT=../travel-app SKIP_AUTH=true PYTHONPATH=. .venv/bin/python -m pytest -p no:cacheprovider tests/db/test_entity_facts.py tests/db/test_place_projections.py tests/places/test_status_evidence.py -q`; targeted Ruff check/format; `RUFF_CACHE_DIR=/private/tmp/vesper-artifact-ruff PYTEST_ADDOPTS='-p no:cacheprovider' TEST_DATABASE_URL=postgresql://vesper:localdev@127.0.0.1:64743/artifact_validity_20260930_01 TEST_DATABASE_DISPOSABLE=1 TRAVEL_APP_ROOT=../travel-app SKIP_AUTH=true make merge-check BASE_REF=origin/main` | 15 PostgreSQL tests passed against the newly created lane-local disposable database. A claim with an expired freshness deadline remains in history with no inferred `valid_to` and is excluded from current selection; an explicitly bounded historical claim remains selectable only inside its validity interval. Place projections still exclude stale evidence. No API or database schema changed. Backend commit hooks passed. The full merge check remains red: 21,962 passed, 14 failed, 14 skipped, 1 xfailed, 52 xpassed, with 2 collection errors. The failures are in `tests/core/vector/` CLI suites (not changed by this slice); collection errors in `tests/scripts/test_audit_prompt_tokens.py` require unavailable network access to fetch tokenizer data. Root causes of the vector failures were not established here. This full-suite result does not negate the focused fact/projection tests, but broader backend verification remains open. |
| P1 corrected time in canonical artifact readback | Backend `555f52ac7`; `TEST_DATABASE_URL=postgresql://vesper:localdev@127.0.0.1:64743/artifact_validity_20260930_01 TEST_DATABASE_DISPOSABLE=1 TRAVEL_APP_ROOT=../travel-app SKIP_AUTH=true PYTHONPATH=. .venv/bin/python -m pytest -p no:cacheprovider tests/inbound/test_candidate_owner_lifecycle_postgres.py -q`; offline `PYTHONPATH=. .venv/bin/python -m pytest -p no:cacheprovider tests/inbound/test_anchor_runtime.py tests/inbound/test_intake_anchor_projection.py tests/inbound/test_intake_semantics_contract.py tests/core/test_canonical_artifact_projection.py -q`; targeted Ruff check/format; targeted mypy | Three Postgres lifecycle tests and 64 offline reader/semantic tests passed. A revisioned owner time replacement now supersedes source-extracted time facts in the persisted anchor and canonical artifact projection, is represented as a user-confirmed fact with a non-degraded correction-observation reference, and is removed when a later `wrong_time` command is applied. Exact retry preserves the revision. Ruff, format, targeted mypy and backend commit hooks passed. No API or database schema changed. |
| P1 semantic correction replay breadth | Backend test commits `25a7ac228`, `f74516894`, and `81812dca5`; lane-local Postgres on `64743`; fresh disposable DB `artifact_route_corrections_20260930_01`. `DATABASE_URL=postgresql://vesper:localdev@127.0.0.1:64743/artifact_route_corrections_20260930_01 PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=. .venv/bin/python -m alembic upgrade head`; `DATABASE_URL=postgresql://vesper:localdev@127.0.0.1:64743/artifact_route_corrections_20260930_01 TEST_DATABASE_URL=postgresql://vesper:localdev@127.0.0.1:64743/artifact_route_corrections_20260930_01 TEST_DATABASE_DISPOSABLE=1 TRAVEL_APP_ROOT=../travel-app SKIP_AUTH=true PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=. .venv/bin/python -m pytest -p no:cacheprovider tests/inbound/test_candidate_owner_lifecycle_postgres.py -q`; `/opt/homebrew/bin/ruff check --no-cache tests/inbound/test_candidate_owner_lifecycle_postgres.py`; `/opt/homebrew/bin/ruff format --check --no-cache tests/inbound/test_candidate_owner_lifecycle_postgres.py` | All 3 candidate-owner lifecycle tests passed. Sequential `replace_time`, `wrong_time`, `separate_from_occasion`, and `keep_occurrence_forget_interpretation` commands now run through the Intake HTTP route; each is verified against persisted revisions and the canonical artifact projection. Exact retries preserve revision, changed payload under the same command ID and stale expected revisions return 409, the latest correction is selected, hiding interpretation clears projected facts, and original extracted evidence remains unchanged. Two different commands racing at one revision produced one write and one stale-revision conflict; simultaneous retries of one command returned the same revision and persisted one effect. Ruff and formatting passed; commit hooks passed Ruff, formatting, Vulture, secret and key-prefix checks. TestClient uses a dependency override for owner identity; this is route/DB evidence, not deployed authentication or service evidence. No API/schema changed. The exact disposable database was dropped and lane Postgres returned to stopped; the named volume was preserved. Native acceptance and mobile replacement-time editor/user-facing Undo remain open. |

The September 30 practical-reader review at app `70707614c` found and fixed a
content-loss edge case: a distinct supplied `identity` was being hidden when a
separate `title` already served as the artifact heading. The new regression
passed with 23 focused reader tests; `npm run typecheck`,
`npm run test:typecheck:contracts`, targeted ESLint, and
`npm run verify:merge -- --base main` passed (1,286 suites, 9,092 tests, 1
snapshot). This is mock/component and app-suite evidence, not live API or native
visual acceptance.

Native acceptance, model comparisons, human preference and economic measurements
remain future evidence—not completed results. On September 30 the assigned
`Vesper QA SE` simulator was available, but the installed development binary
crashed before the product route: the JS bundle used `react-native-worklets`
`0.7.4` while that binary contained native Worklets `0.11.3`. The registered
`canonical-artifact-reader` flow therefore captured 0/1 scenarios and no
screenshots. A lockfile-pinned `pod install --deployment` completed without
changing tracked files, but rebuilding with Xcode 26.5 (build `17F42`) still
failed: Xcode reported the generated `Pods.xcodeproj` damaged while decoding
`XCSwiftPackageProductDependency` (`_setSavedArchiveVersion` selector missing),
then Swift compilation could not import `Expo`. CocoaPods was `1.16.2`; the
checked-out app locks `react-native-worklets` `0.7.4`. This is an environment /
generated-project build blocker, not reader-flow acceptance or evidence of a
reader defect. No native visual judgment is claimed; resume capture only with a
working, checkout-matched dev build and a Pods project the selected Xcode can
load. This file owns Strategy's package progress under the program boundaries,
not the other lanes' queues. On expiry, refresh unfinished work with an
explicit reason, promote durable contracts or archive completed planning and
research.

### September 30 native reader recovery and bounded acceptance

The earlier failed native attempt above is retained as historical evidence. The
build blocker was resolved in the same coordinated lane: app commit
`5c102849c` backports collision-safe UUID allocation for React Native's
CocoaPods-generated Xcode project, with a regression that reproduces the
SPM-project reload collision (Ruby/Xcodeproj: 2 tests, 6 assertions passed).
After `pod install --deployment`, Xcode 26.5 could load the workspace and the
checkout-matched development app rebuilt and installed on `Vesper QA SE` with
`SENTRY_DISABLE_AUTO_UPLOAD=true npx expo run:ios --no-bundler --device "Vesper QA SE"`.
This was a narrow patch to the pinned React Native version, not a dependency
upgrade.

At app `a611cba69`, the native `canonical-artifact-reader` scenario completed
on simulator UDID `51A7A2C0-49CB-487E-A056-A771361EFA9B`: `VESPER_METRO_URL=http://127.0.0.1:64747 npm run qa:polish -- canonical-artifact-reader --device="Vesper QA SE" --flow=polish/canonical-artifact-reader` captured 1/1 scenario and 2/2 extras under `.maestro/runs/20260930T140955Z-canonical-artifact-reader`. Opened screenshots confirmed the source-inspection and return path, legible artifact hierarchy, non-overlapping metadata, and independently traversable title/facts/action. The UI/accessibility changes are in `a611cba69`; the app surface contract's corrected evidence boundary is in `28f701c54`.

Focused reader tests passed (3 suites, 38 tests); targeted ESLint and app
typecheck passed. `npm run verify:fast` passed, followed by
`npm run verify:merge -- --base main` (1,286 suites, 9,094 tests, 1 snapshot).
The structured native verdict at
`travel-app/docs/surfaces/canonical-artifact-reader/verdicts/20260930T140955Z.json`
is `pass` for this bounded fixture scenario, with two minor P2 observations:
the `ENCOUNTER ATTENTION` kicker pair is taxonomy-forward, and the footer
repeats the “Inspect source” action. `qa:polish:scenarios` passed with 31
registered scenarios. The design-reference check is doctrine-only because this
surface has no pinned design-reference manifest; no Claude-design comparison or
design-intent verdict is claimed.

This closes the registered exact-original inspection/return native scenario,
not the larger artifact-reader acceptance. The run used a fixture-bound
calendar original and does not establish production persistence or live API
readback. Photo panning/pinch, VoiceOver traversal, physical-device behavior, a
multi-family native matrix, real-world artifact usefulness, model quality, and
the P3 discovery experience remain unverified/open. Direct simulator input did
verify double-tap fit → zoom → fit on the seeded owner-photo fixture. The
subsequent registered Maestro run completed but the four gesture-state captures
had identical SHA-256
`242e12a3edaa8a4c5a96d9dabfcc34dd9db5ee86d2a2bbe144e71379c6057f8f`; its gesture
commands are not acceptance evidence and were removed from that flow. A
follow-up visual check exposed a viewport bug: the transformed clipping frame
could expand over the fixed photo-viewer title and close control. The shared
component now keeps the clipping viewport fixed and transforms only its inner
photo layer; simulator retest confirms the controls stay stationary through
fit → zoom → fit. Pan, pinch, VoiceOver, physical-device behavior, and broader
acceptance remain open. Continue with those narrower acceptance and
product-value gates before treating the artifact reader as broadly native-
accepted or moving to an unscoped generalized dynamic-content implementation.

The adjacent registered Life continuity flow was also run after this recovery:
`VESPER_METRO_URL=http://127.0.0.1:64747 npm run qa:polish -- life-root --device="Vesper QA SE" --flow=polish/life-intake-source-continuity`
captured 1/1 scenario and 3/3 extras in
`.maestro/runs/20260930T142555Z-life-root`. Reviewed screenshots show the exact
mock owner-held photo from the Life source row, the focused viewer displaying
that same uncropped photo, and the source absent from Life after owner-authorized
Undo. This is fixture-backed route/entry/exit evidence; Maestro did not exercise
pinch, pan, double-tap, or VoiceOver. It does not prove live-source persistence,
and it is not a broader Life-root design verdict. Photo gesture and assistive
acceptance therefore remain open. A September 30 attempt expanded the flow
with coordinate double-tap and swipe commands, but the captured fit, zoom, pan
and restored PNGs had identical SHA-256
`242e12a3edaa8a4c5a96d9dabfcc34dd9db5ee86d2a2bbe144e71379c6057f8f`. Those
automation commands are not evidence of visible interaction and were removed
from the registered route-continuity flow. Separately, direct simulator input
on the same seeded owner photo visibly toggled fit → zoom → fit. That supports
only the double-tap path on this simulator/build; a direct CUA drag produced no
visible pan, so pan remains unresolved rather than failed or passed. The
simulator check also exposed that the animated transform was applied to the
clipping viewport, allowing the image to overlap its fixed title/close header.
The shared component now leaves that viewport fixed and clipped, with the
transform on an inner image layer. A post-change simulator double-tap again
showed fit → zoom → fit while the header stayed stationary and the image
remained inside the viewport. A focused component-structure regression test
guards that separation; simulator drag still did not establish panning.

The bounded JavaScript follow-up verifies that the photo viewer's declared
Zoom in and Zoom out accessibility actions dispatch through the existing
bounded transform and return to fit. App commit `8914469b3` adds this focused
component test. The focused reader/zoom test command passed (3 suites, 42
tests), as did app typecheck and targeted ESLint. `npm run verify:fast` passed
(lint: 0 errors, 169 existing warnings; typecheck, API boundaries, schema
bridge, Home budgets, and test-typecheck contracts passed). The main-based
merge gate passed against the same tree before the test-only commit:
`npm run verify:merge -- --base main` (1,286 suites, 9,095 tests, 1 snapshot).
These are callback-wiring and repository-gate results, not device VoiceOver
activation or native gesture acceptance.

During a separate simulator follow-up, opening the Vesper tab displayed a
“Maximum update depth exceeded” error while its root remained in a loading
state; the simulator accessibility tree then became unavailable. A subsequent
CoreSimulator log query could not connect, so this observation has no diagnosed
cause and is not attributed to the artifact reader. It prevented interactive
VoiceOver/gesture follow-through and should be triaged independently of this
roadmap slice; no Vesper/Home code was changed here.

### September 30 photo viewport correction

App commit `82353cccf` fixes the shared photo viewer geometry found above:
`ZoomableOriginalPhoto` keeps its overflow-hidden viewport fixed and applies
the animated transform only to the inner photo layer. The new component test
guards that boundary. After hot reload on `Vesper QA SE` (iOS 18.2), direct
simulator double-tap showed fit → zoom → fit while the title and close control
stayed stationary and the enlarged photo remained clipped to the viewport.
Direct CUA drag still did not visibly establish pan. A later attempt to invoke
the image's accessibility increment action was blocked because the Mac UI was
locked; this is not VoiceOver evidence. Pan, pinch, VoiceOver traversal,
physical-device behavior, and a native recipient-reader capture remain open.

Validation on the corrected app tree: the focused command
`npm test -- --runInBand __tests__/components/zoomableOriginalPhoto.test.tsx __tests__/components/canonicalArtifactCard.test.tsx __tests__/utils/photoZoom.test.ts`
passed (3 suites, 32 tests); `npm run typecheck`,
`npm run test:typecheck:contracts`, `npm run qa:polish:scenarios`, targeted
ESLint, `npm run docs:check`, `make docs-check`, and `git diff --check` passed.
`npm run verify:merge -- --base main` passed (1,287 suites, 9,096 tests, one
snapshot). The `npm run verify:fast` wrapper stopped at Expo ESLint because its
managed-checkout cache write returned `EPERM`; equivalent cacheless full lint
over `app`, `components`, and the new test passed with zero errors and 169
warnings. App evidence was committed separately as `1e82b3e55`. No backend,
live-service, VoiceOver, or physical-device evidence is implied.

### September 30 sparse-history composition fixture

App commit `b212de7fa` adds a separate sparse-context variant of the Sorrento
opening without changing the six-entry executable portfolio. It contains only
the person's cliff observation and one cited public geology source; the
existing lift and ferry evidence, and the synthesis that depends on them, are
absent. The focused test confirms the compiler admits the two-source brief,
preserves the source authors, excludes the unsupported movement claim, and
leaves owner state unchanged under its ephemeral lifecycle.

Validation: `npm test -- --runInBand __tests__/utils/artifactPortfolio.test.ts`
(1 suite, 9 tests), targeted ESLint on the fixture and test, `npm run typecheck`,
and `git diff --check` passed. This is deterministic fixture/compiler evidence
only; it does not establish a live generation path, research freshness, a
user-facing native rendering, or preference/desirability. Selected-part
representation remains open pending the P0 reference decision.

### September 30 relationship-label safety

App commit `fd1353a7b` prevents the optional connected-neighborhood reader
from exposing internal `ResourceRef`/`EntityRef` IDs as user-facing text. It
uses a matching projection-supplied source/provenance label when that value is
not identifier-shaped; otherwise it renders a safe target-kind label. The
underlying relation references and IDs remain unchanged, and a fallback does
not claim subject resolution.

Validation: `npm test -- --runInBand
__tests__/utils/canonicalArtifactRelationships.test.ts
__tests__/components/canonicalArtifactCard.test.tsx` passed (2 suites, 32
tests); `npm run typecheck`, targeted ESLint, `npm run qa:polish:scenarios`
(31 registered IDs), `npm run docs:check`, and `git diff --check` passed. Jest
printed a React `act(...)` warning from `VirtualizedList`, but the suites passed.
The full app merge-scope run also passed at app `fd1353a7b`:
`npm run verify:merge -- --base main` (1,287 suites, 9,100 tests, one
snapshot). The runner force-exited one worker after the suites completed; no
test failure was reported.
Native visual acceptance was not run because the Mac UI was locked; these
checks prove fixture/component behavior only, not native rendering or live
projection behavior. No backend, API schema, or identity change was made.

### September 30 photo-selection zoom reset regression

App commit `5b6a4e2c7` adds a regression proving that after the first original
is zoomed, selecting the next original begins from fit rather than carrying
over the previous photo's transform. The production reader already remounts
the zoom surface using the selected source identity; this test protects that
P2 contract without changing runtime behavior.

Validation on app `5b6a4e2c7`: `npm test -- --runInBand --no-cache
__tests__/components/canonicalArtifactCard.test.tsx` passed (1 suite, 27
tests), targeted ESLint passed, `npm run typecheck` passed, and
`npm run verify:merge -- --base main` passed (1,287 suites, 9,101 tests, one
snapshot). The focused Jest run printed the existing asynchronous
`VirtualizedList` `act(...)` warning; the suite passed. The 31 registered QA
scenario IDs validated. A native QA retry was unavailable: CoreSimulatorService
returned a connection error, and the runner's doctor stopped before device
preflight because it could not create its lane-local QA lock (`EPERM`). No
native flow or screenshot was produced. Pinch/pan, VoiceOver, physical-device,
and wider reader acceptance remain open; no backend/API or identity change was
made.

### September 30 revision-bound correction Undo

Backend `d3730a8c4` adds `undo_correction` to the existing authenticated Intake
owner command. Undo requires a command ID and expected owner revision, appends a
new correction-history observation naming the exact latest effective semantic
correction, and replays the remaining correction history. It restores the
preceding effective correction or the source-derived interpretation; it never
edits or recreates the Source. The owner projection reports Undo only for an
eligible Mine reading with an effective semantic correction. JSON
`owner_revision` ordering, then creation time and observation ID, keeps anchor
compilation and canonical projection selection deterministic across independent
reads; legacy observations without that field sort after revisioned owner
events. No database migration was needed.

Workspace OpenAPI snapshots are committed at `7ff1eb2c`; app reader, fixture,
generated TypeScript and contract are committed at `14693c6d0`. The native
reader offers `Undo correction` only when Mine supplies the current revision
and correction target, sends the existing owner command, and refetches the
exact artifact projection. Together never receives the control. The app change
does not add a second correction owner or mutate the original.

Validation: the backend focused offline suite
(`tests/inbound/test_anchor_runtime.py`,
`tests/core/test_canonical_artifact_projection.py`,
`tests/inbound/test_intake_semantics_contract.py`, and
`tests/api/test_intake_route.py`) passed (83 tests); the three disposable-Postgres
candidate-owner lifecycle tests passed, including correction sequence/Undo,
retry deduplication, stale and changed-payload conflicts, concurrency, and
Source-deletion blocking. `make ci-static` passed with lane cache directories
under `/private/tmp`; mypy checked all 1,890 backend source files. The app
`npm run verify:merge -- --base 87eceee24512d9086962eea5b844cef9d7bffbeb`
passed (1,287 suites, 9,103 tests, one snapshot). App typecheck, test-contract
typecheck, generated-type check, targeted ESLint, QA scenario registry (31 IDs),
app docs check, workspace `make docs-check`, and `git diff --check` passed.
Local API startup was not available because `ANTHROPIC_API_KEY` was absent;
database coverage used the isolated Postgres service and TestClient identity
override. The service was stopped afterward and its named volume preserved.
Native/device acceptance was not run, so no live API or native UI behavior is
claimed. P1 identity, component, collection and reconciliation work, and the
timezone-gated replacement-time editor, remain open.

### September 30 artifact-to-original return continuity

App commit `18ad70bfa` preserves route ownership through exact-original
inspection. The canonical artifact reader now passes its immediate artifact
ID, exact source identity, ephemeral root token, and Life lens/group/record
context into the existing Intake source reader. Its Back action targets that
artifact as the semantic parent even if unrelated navigation history exists;
the cold-link fallback rebuilds the artifact route with the same token/context.
Leaving the artifact
then follows its exact Life return or registered root when available, allowing
the existing root tracker to complete restoration only after the artifact is
left. Source custody revalidation and original authorization stay in their
existing owners; no backend, API, durable identity, or source-custody behavior
changed.

Validation on app `18ad70bfa`: the focused screen command
`npm test -- --runInBand --no-cache
__tests__/screens/canonical-artifact-reader.test.tsx
__tests__/screens/intake-submission.test.tsx` passed (2 suites, 48 tests);
`npm run typecheck`, `npm run test:typecheck:contracts`, targeted ESLint,
`npm run docs:check`, `npm run qa:polish:scenarios` (31 registered IDs), and
`git diff --check` passed. One full merge run first lost an unrelated Discover
test worker to SIGSEGV after 1,286 of 1,287 suites; that suite passed alone,
and the full rerun passed: `npm run verify:merge -- --base
87eceee24512d9086962eea5b844cef9d7bffbeb` (1,287 suites, 9,106 tests, one
snapshot). Native QA was attempted with the lane-assigned Metro port and Vesper
QA SE device, but CoreSimulatorService became unavailable and the runner could
not create its lock directory (`EPERM`); no native flow or screenshot was
produced. Thus navigation is verified at route/screen-test level only, not on
device. Selected-part interaction, native visual/gesture acceptance, and the
P0-gated identity/component/collection/reconciliation decisions remain open.

### September 30 artifact reader copy polish

App commit `6364cbf95` responds to the P2 findings in the September 30 native
reader verdict: attention-family artifacts now lead with the title instead of
the internal `ENCOUNTER · ATTENTION` taxonomy, and a live `Inspect source`
action replaces—not repeats—the adjacent availability sentence. When the
reader has no source-opening callback, the factual availability copy remains.
No data contract or authorization behavior changed.

The focused canonical artifact reader component suite passed (28 tests), along
with app typecheck, test-contract typecheck, targeted ESLint, API-boundary,
schema-bridge, surface-budget, docs and scenario-registry checks. The full app
merge check passed on `main` (1,287 suites, 9,107 tests, one snapshot). The
composite `npm run verify:fast` stopped at ESLint because the managed checkout
denied a write to `.expo/cache/eslint`; the same lint completed with
`npm run lint -- --no-cache` (0 errors; 169 existing warnings), and its later
fast-gate constituents passed individually. `qa:design:check` confirmed this
surface has no pinned design-reference manifest. With Metro correctly running
on lane port 64747, the first registered device attempt exposed a capture
setup error: the simulator was given a loopback Metro URL (`127.0.0.1`), which
points back to the simulator rather than the Mac. Restarting Metro with LAN
host mode and passing the reachable host URL allowed the registered scenario
to complete on `Vesper QA SE` (iOS 18.2):
`VESPER_METRO_URL=http://192.168.1.153:64747 npm run qa:polish --
canonical-artifact-reader --device="Vesper QA SE"
--flow=polish/canonical-artifact-reader` captured the artifact, exact original,
and return state (1/1 scenario, 2/2 extras). The committed native verdict at
`travel-app/docs/surfaces/canonical-artifact-reader/verdicts/20260930T191307Z.json`
is `pass` for this bounded mock-fixture scenario. It confirms the private,
tentative record, exact `.ics` event/location, explicit no-calendar-import
message, and return to the same artifact/action after the copy polish. This
does not establish live backend delivery, persisted production state, design
reference parity, photo gestures, VoiceOver, physical-device behavior, or the
broader artifact-family matrix. Those native/product acceptance items remain
open.

### September 30 registered artifact-reader family matrix

App commit `eb5209447` expands the registered `canonical-artifact-reader`
Maestro flow through the production reader route to include a source-backed
book, a kept passage, a structured practical record, and a sparse work record
that must remain on the generic source-fact fallback. The flow waits for the
family-reader test IDs where relevant, so a screenshot alone cannot silently
stand in for reader dispatch. The fixtures remain mock-only; this adds no
catalog, backend, persistence, or product-capability claim. The existing
calendar → exact original → return path is retained.

Validation: app `npm run qa:polish:test` passed (including committed-verdict,
surface-index, scenario, and design-gate checks); `git diff --check` passed;
`npm run qa:polish -- canonical-artifact-reader --dry-run
--flow=polish/canonical-artifact-reader` generated the expected seven-screenshot
manifest without captures. The live capture was **not run**: `xcrun simctl list
devices booted` returned `CoreSimulatorService connection became invalid`, so
there was no available simulator target. The dry-run is registry evidence only,
not native acceptance. This closes a coverage-definition gap, not the open P2
native visual/interaction acceptance. Resume with the registered device flow
on a working simulator, inspect the family screenshots, and judge each
fallback/authority claim before marking any matrix state accepted.

### September 30 source-to-reader contract verification

On app `eb5209447`, the focused component and route tests
`npm test -- --runInBand --no-cache
__tests__/components/canonicalArtifactCard.test.tsx
__tests__/screens/canonical-artifact-reader.test.tsx` passed (2 suites, 42
tests). On backend `d3730a8c4`,
`pytest -q -p no:cacheprovider tests/core/test_canonical_artifact_projection.py
tests/inbound/test_anchor_runtime.py` passed (38 tests). The first pytest
invocation ran the same tests but exited during cache writing because the
managed worktree denies `.pytest_cache` writes; disabling that cache provider
produced the clean result above. These tests prove projection/dispatch and
route behavior at unit/component level, not simulator or authenticated live
service behavior.

### September 30 photo-reader bounds after layout change

App commit `6dd9816f1` closes a P2 transform edge case in the shared
`ZoomableOriginalPhoto`: after viewport layout or decoded source dimensions
change, the current scale/translation is re-clamped against the new contained
image bounds. This prevents stale pan offsets from exposing blank space after
rotation, window/safe-area resizing, or a source-size update. Returning to fit
still recenters. Intake, received-original Life, and canonical-artifact viewers
all inherit the shared behavior; their source custody and authorization owners
remain independent.

Validation on app `6dd9816f1`: the focused component and route command
`npm test -- --runInBand --no-cache
__tests__/components/canonicalArtifactCard.test.tsx
__tests__/components/zoomableOriginalPhoto.test.tsx
__tests__/screens/canonical-artifact-reader.test.tsx` passed (3 suites, 44
tests). The added regression changes from portrait to landscape bounds and
asserts the corrected transform is used by the next zoom action. `npm run
typecheck`, targeted ESLint for the changed component/test, and `git diff
--check` passed. Native capture/gesture acceptance was not re-run because
CoreSimulatorService remains unavailable in this environment; this closes a
JS geometry regression only, not native pan/pinch, VoiceOver or physical-device
acceptance.

### September 30 full app merge-scope verification

After the photo-viewer bounds change, app command `npm run verify:merge --
--base main` completed in full mode on `6dd9816f1`: 1,287 suites and 9,108
tests passed, with one snapshot. The changed photo/artifact suites were included
in that run. Existing asynchronous React test warnings appeared in unrelated
suites, but the aggregate command exited successfully. This is broad app
regression evidence, not native device acceptance or a backend integration
claim.

### September 30 expiry-aware cached reader facts

App commit `bc71bf128` closes the mounted-reader gap for owner facts that carry
`valid_until`. The backend already excludes expired facts when it serves a
fresh projection, but a cached mobile projection could keep displaying one
past its deadline. The existing expiry-tick hook now removes expired or
malformed-deadline facts from the rendered projection immediately, then asks
the owner for a fresh read; the canonical artifact query also opts into stale
refetch when the app returns to the foreground. When no current family-specific
facts remain, the projection no longer advertises a specialized family reading.
Unrelated source-backed facts, the exact original, and independent owner
actions remain available. The query cache is not mutated by the display filter.

The new data-hook tests cover the exact deadline, suppression while refresh is
still pending, family-reader fallback after its qualifying facts expire, and
foreground refetch. The focused artifact reader set passed (3 suites, 47 tests),
as did app typecheck, test-contract typecheck, targeted ESLint, and the polish-QA
registry. The registered canonical-reader QA dry-run created no screenshots;
`xcrun simctl list devices booted` still fails because CoreSimulatorService is
unavailable. Thus no native visual or live-service claim is made. A full app
merge-scope check on `bc71bf128` passed with
`npm run verify:merge -- --base main`: 1,288 suites, 9,112 tests and one
snapshot. Existing unrelated React/API diagnostic warnings appeared during the
suite, but the aggregate command exited successfully. This is broad app
regression evidence, not native device or authenticated live-service evidence.

### September 30 account-session-scoped artifact reads

App commit `5d1a9a5b4` partitions canonical artifact projection queries by the
authenticated session key and does not enable the owner read until the active
session and profile are ready. The reader suppresses cached projection data
while that owner context is unresolved; changing accounts selects a distinct
cache key, so a late response from the previous account cannot become the
current account's visible artifact. Intake correction success now invalidates
the exact account-scoped projection key. This is a client cache/read boundary,
not a replacement for backend authorization.

The focused session/expiry suite passed (`canonicalArtifacts.test.tsx` and
`queryKeys.test.ts`: 2 suites, 16 tests), including signed-out suppression,
account-key separation, and the late-response account-switch race. App
typecheck, test-contract typecheck, targeted ESLint, `npm run docs:check`,
`npm run qa:parity` (6 suites, 185 tests), `npm run qa:polish:test`, and
`git diff --check` passed. The full app merge check passed on this commit:
`npm run verify:merge -- --base main` (1,288 suites, 9,114 tests, one
snapshot). No authenticated live-service or native-device test was run; this
slice changes session-scoped data access rather than layout, and simulator
availability remains a separate acceptance constraint.

### September 30 native artifact-reader family matrix

App commit `bf5f2deae` records the first completed registered simulator matrix
for the artifact reader: calendar artifact, exact `.ics` original, return to
the same artifact, source-backed book, kept passage, practical record, and
sparse-work fallback (seven screenshots total). It ran on Vesper QA SE / iOS
18.2 through the production reader route with deterministic mock fixtures. The
calendar remains explicitly tentative; the source preview says no event is
added to the device calendar; the sparse work stays unresolved; supplied
passage and practical facts render without inferring surrounding meaning,
payment, or validity. The committed structured verdict is
`travel-app/docs/surfaces/canonical-artifact-reader/verdicts/20260930T204016Z.json`
with its manifest snapshot. It passes the four capture/correctness/visual/intent
gates against the surface contract and doctrine; no Claude Design reference is
pinned for this reader.

The initial run exposed a test-selector mismatch, not a rendering defect: the
excerpt was visible in the screenshot, while the flow expected its bare text
instead of the accessible label `Kept passage: …`. The registered assertion
now checks that label, and the complete rerun captured 1/1 flow and 6/6 extra
screenshots. `npm run qa:polish:test` passed, including 73 committed verdicts;
`npm run qa:polish:scenarios` validated all 31 IDs; `npm run docs:check` passed
for 312 app Markdown files; `git diff --check` passed. These captures prove
fixture-backed native rendering/navigation, not authenticated API, production
persistence, or user desirability. Photo pinch/pan/double-tap, VoiceOver
activation/traversal, Dynamic Type, ticket/place/show/music/dish family
coverage, and live-service readback remain open. The earlier registered dry-run
receipt records the simulator outage before this subsequent successful run.

### September 30 expanded native reader-family matrix

App commit `05d81a9df` expands the production-route capture matrix to 14
screenshots on the lane-assigned `Vesper QA SE` simulator (UDID
`51A7A2C0-49CB-487E-A056-A771361EFA9B`, iOS 18.2): the tentative calendar
artifact, exact `.ics` original, return to that artifact, and native reader
states for book, transport ticket, admission ticket, place, film, show, music,
kept passage, practical record, dish fallback, and sparse-work fallback. The
final structured verdict and manifest are
`travel-app/docs/surfaces/canonical-artifact-reader/verdicts/20260930T211642Z.json`
and `.manifest.json`; it passes capture, correctness, visual, and doctrine
intent for this bounded fixture matrix. The place fixture is explicitly
`noticed`; the reader now leads with `Da Enzo`, omits the misleading
experience-family eyebrow, and avoids repeating the place name as a fact.

Validation on the final app commit: focused reader/portfolio tests passed (2
suites, 44 tests); `npm run typecheck`, `npm run test:typecheck:contracts`,
targeted ESLint, `npm run qa:polish:test` (74 committed verdicts),
`npm run qa:polish:scenarios` (31 registered IDs), `npm run docs:check` (318
Markdown files), and `git diff --check` passed. The full app merge-scope check
passed: `npm run verify:merge -- --base main` (1,288 suites, 9,117 tests, one
snapshot). The successful capture command targeted the lane-assigned simulator
and produced 1/1 flow plus 13/13 extra screenshots. No authenticated service,
persisted-production, or user-preference evidence is claimed. Dynamic Type,
loading/error states, photo gestures, VoiceOver activation/traversal, and live
service readback remain open. The committed verdict records two P2 observations:
the text-only show face still reads as a restrained metadata panel, and the
reader matrix does not yet demonstrate the context-dependent artifact value
planned for a later slice. This completes family-rendering coverage, not the
artifact experience roadmap or the contextual-discovery phase.

### September 30 largest-text artifact-reader reflow

App commit `c704fc997` adds content-driven reflow for the canonical artifact
reader and its exact-source screen at the system's largest accessibility text
sizes. At the shared `fontScale >= 1.35` threshold, fact rows stack labels and
values, title/status/fact copy is no longer line-capped, ticket routes become
vertical, and book/place/music/passage/practical faces relinquish fixed
geometry. Redundant floating-reader and private-source titles are hidden at
that size; the floating reader chrome becomes opaque so content cannot bleed
behind the control. The implementation does not reduce the person's selected
text size.

The registered `polish/canonical-artifact-reader-accessibility` capture
(`20260930T222931Z-canonical-artifact-reader`) contains ten fixture-backed iOS
18.2 screenshots on Vesper QA SE at
`accessibility-extra-extra-extra-large`, including source-action scrolling,
opening the exact calendar original, returning to the same artifact, and the
ticket/book/place/music/passage/practical family faces. Its structured `pass`
verdict and manifest are
`travel-app/docs/surfaces/canonical-artifact-reader/verdicts/20260930T222931Z.json`
and `.manifest.json`. The capture occurred immediately before the app commit;
the manifest therefore records parent HEAD `05d81a9df`. No reader UI source
changed between capture and `c704fc997`; the later row-guard correction is
test-only. This is native layout/scroll evidence for the captured fixture on
one iOS simulator, not VoiceOver activation, Android/physical-device coverage,
live-service readback, or user desirability. Two accepted P2 observations note
the long first-viewport title and tall source action at maximum text size; both
remain legible and reachable, and neither justifies capping user-selected text.

Focused reader/source tests passed (3 suites, 82 tests), app TypeScript and test
contract typechecks passed, targeted ESLint reported zero errors with two
warnings, and `git diff --check` passed. The row-system ratchet initially
classified the new static `ArtifactFactRow` as an interactive/list row; its
existing `isOutOfScope` classifier now documents this exact static document
fact-pair exception, with a test ensuring the general ratchet still applies to
artifact reader components. The focused ratchet test passed (10 tests).

`make verify-changed WORKSPACE_BASE_REF=main AGENT_BASE_REF=main
APP_BASE_REF=main` passed across the coordinated lane. This included the full
app suite (1,288 suites, 9,123 tests, one snapshot), backend static checks and
full tests (21,993 passed, 14 skipped, 53 xpassed; two warnings), workspace
tooling tests, and cross-repository API/compatibility/documentation contracts.
After the app commit, `npm run qa:polish:scenarios` validated 31 registered
IDs, `npm run qa:polish:test` validated 75 committed verdicts, and
`npm run docs:check` passed for 327 app Markdown files. Pinch/pan, actual
VoiceOver traversal/actions, loading/error states, physical-device/Android
behavior, live-service readback, and value/desirability remain open; this
closes only the largest-text iOS reflow slice, not P2 as a whole.

### September 30 Home dock stability prerequisite

App commit `5d56ef5ff` stabilizes the private-capture handler registered by the
Vesper Home dock. The Home hook had passed a newly allocated capture-entry
object on every render; that recreated the dock accessory and fed registration
updates back through `NavChromeContext`. The app now memoizes the navigation
adapter and entry, with a regression test that equivalent Home renders retain
the same capture handler. This was an adjacent defect surfaced while preparing
native artifact QA; it is not an artifact feature increment or a Home visual
acceptance claim.

Focused evidence: the Home capture/private-capture/dock suites passed (3 suites,
23 tests); the Home smoke suite passed (18 tests); `npm run typecheck`, targeted
ESLint and `git diff --check` passed. On the assigned Vesper QA SE simulator,
the registered `polish/life-intake-source-continuity` flow completed (1/1
scenario, 3/3 extras) and proved the fixture-backed source → exact-photo viewer
→ source → removal path. That flow does not exercise photo gestures, VoiceOver,
or the Home surface's design. `npm run verify:merge -- --base main` passed on
app commit `5d56ef5ff` (1,288 suites, 9,124 tests, one snapshot); the runner
reported one worker forced exit after the suite completed, with no failed
tests. Native photo pan/pinch and assistive-action acceptance therefore remain
open as recorded above.

### October 1 cross-submission Thing identity and native read target

This increment completes the bounded backend identity/read and app-consumer
slice, but not its ordinary entry-path integration. Workspace commit
`3a0ec826` records the ownership split: backend owns identity, reconciliation,
Source authorization and the read contract; the app owns presentation,
navigation and query cache, without a second identity authority. Backend commit
`cb7defc86` adds the owner-scoped alias table, evidence-backed reversible merge
and exact reversal commands, alias resolution, independently reauthorized
Source reads, and `GET /api/artifact-projections/things/{thing_id}`. App commit
`eb515f055` consumes the generated contract and adds a native Thing reader that
lists originals and returns to the exact Source. The merge/reversal operations
remain backend domain commands: no HTTP write route or user-facing controls
were added. Existing candidate IDs still open the prior `ExperienceAnchor`
reader; there is not yet a normal product entry path to the new Thing reader.

Backend migration and database evidence used the lane-local Postgres service on
port `64743` and fresh disposable database `artifact_alias_20261001_02`:

- `DATABASE_URL=postgresql://vesper:localdev@127.0.0.1:64743/artifact_alias_20261001_02 PYTHONPATH=. .venv/bin/python -B -m alembic upgrade head` passed from an empty database; `alembic check` reported no new operations.
- `TEST_DATABASE_URL=postgresql://vesper:localdev@127.0.0.1:64743/artifact_alias_20261001_02 TEST_DATABASE_DISPOSABLE=1 PYTHONPATH=. .venv/bin/python -B -m pytest -p no:cacheprovider tests/api/test_artifact_projections.py tests/inbound/test_kept_things_postgres.py -q` passed (15 tests). These are real PostgreSQL tests, not mocked repository checks.
- Targeted Ruff check and formatting passed; backend commit hooks passed when run with the lane `.venv` on `PATH`. Targeted mypy passed earlier in the slice; the full `make ci-static` invocation reproducibly ends in a mypy 2.3.1 internal error after its preceding static gates pass.

App evidence: `npm run typecheck` and `npm run test:typecheck:contracts` passed;
the focused reader/intake/typography run passed (3 suites, 46 tests); changed-file
ESLint passed with 0 errors and 3 warnings (the existing Intake line-count and
two API array-type warnings). `npm run verify:merge -- --base
e7bdc660501eaa19234e6b45bda033658edaa2d4` passed standalone (1,290 suites,
9,185 tests, one snapshot). A later combined `make verify-changed` run was not a
passing receipt: its app worker for `ChatScrollEdge.test.tsx` terminated with
SIGSEGV, then that suite passed alone (1 suite, 3 tests); cached Expo ESLint
failed to write `.expo/cache/eslint` with `EPERM`; and workspace runtime tests
could not bind temporary localhost ports in the sandbox. The combined backend
static gate independently reproduced the mypy internal error. Do not describe
the combined preflight as green. API generation and `make api-coverage-check`
passed; the full/app-generated contract files are recorded in the workspace
snapshot update.

The assigned simulator was unavailable (`CoreSimulatorService` failure), so
there is no native screenshot, VoiceOver, Android, physical-device, or
authenticated live-service acceptance for the initial Thing route. The
following candidate-to-bundle entry integration is separately recorded below.
Collection and Life remain consumers, not identity owners.

### October 1 candidate-to-bundle entry integration

This implementation records the ownership decision in product behavior without
changing the accepted identity model. Strategy continues to own the outcome
end-to-end. Backend owns the persisted Thing reference, source-eligibility check,
owner-scoped projection and action contract; the app owns the separate button,
navigation and bundle-reader language. The workspace owns this cross-repo
roadmap and evidence receipt. No repository copies identity or source
authorization from another owner.

Backend commit `f1ae16096` links a candidate to the Thing for its verified
private-Keep submission only when its supporting Source is available, content
is available, private source retention is active and unexpired. The projection
preserves the candidate/anchor ID and exposes a distinct `Open saved bundle`
action; it does not claim that the submission's multiple sources or candidates
are one semantic object. Existing primary occurrence actions remain in place.
App commit `9a1c96292` opens that bundle separately and describes it as kept
together originals, not as a single semantic item. The existing source-to-
candidate path remains unchanged; each original is still authorized separately
when the user opens it. The app surface contract defines the exact return and
legacy/unretained fallback.

| Boundary | Command | Result and limit |
| --- | --- | --- |
| Backend projection | `PYTHONPATH=. .venv/bin/python -B -m pytest -p no:cacheprovider tests/api/test_artifact_projections.py tests/core/test_canonical_artifact_projection.py -q`; targeted Ruff check and format check on the four changed Python files | 37 tests passed; Ruff check and formatting passed. Covers eligible and missing Thing references, derived-only/expired retention exclusion, stable Thing path, action ordering and preserved primary action. No live-service or database acceptance was added in this increment. |
| App reader and action | `npm test -- --runInBand __tests__/screens/canonical-artifact-reader.test.tsx __tests__/screens/kept-thing-reader.test.tsx __tests__/utils/canonicalArtifactActions.test.ts __tests__/components/canonicalArtifactCard.test.tsx`; `npm run test:typecheck:contracts`; targeted `npm exec eslint -- --no-cache …`; `npm run docs:check` | Four suites / 62 tests passed; contract typecheck, changed-file ESLint and docs checks passed. Screen tests establish the conditional action and route/return behavior, not native rendering or live authorization. |
| Native QA readiness | `npm run qa:polish:scenarios`; `npm run qa:design:check -- canonical-artifact-reader`; `node scripts/polish-qa/run-polish-qa.mjs canonical-artifact-reader --doctor` | 31 registered scenario IDs passed. Design-reference check returned success with a warning: the doctrine-only surface has no design-ref manifest. Doctor/preflight was blocked because Metro was not reachable on `:8081`; no screenshot, simulator, VoiceOver, or native visual acceptance is claimed. |

At this checkpoint, the increment completed only candidate-to-bundle read
integration. It added no schema, write endpoint, automatic reconciliation,
Collection membership, public sharing or new source-retention behavior.
Owner-confirmed merge/reversal transport and UI, Collection continuity and
native QA were still open then; the following receipt records the reconciliation
implementation. The backend/app commits for this earlier increment were
lane-local and not merged to `main`.

### October 1 owner-confirmed bundle reconciliation

This implements the already accepted
[kept-Thing identity decision](../decisions/2026-09-30-kept-thing-identity.md);
it does not create a new identity decision or assert that two bundles represent
the same real-world object. One verified private Keep still creates one
owner-scoped identity for that contribution bundle. When deciding whether two
separately kept bundles should stay connected, the owner—not Vesper or a model—
makes that choice after seeing currently readable originals from both. The app
preselects one exact source from each bundle to reduce work and permits
inspection or source substitution before confirmation. `Keep these bundles
together` records a revision-bound, reversible owner connection; `Separate`
undoes that connection without a free-text explanation. Stable bundle/source
references survive. Intake retains Source custody and access decisions,
`kept_things` owns Thing identity/reconciliation, the app owns presentation and
navigation, and Life/Collections remain consumers. The connection does not
combine permissions or prove semantic sameness.

Backend commit `53d90e9eb` and app commit `38757f485` are committed on the
coordinated local lane; neither is merged to `main`. Workspace API policy,
OpenAPI snapshots, generated Current State, roadmap and reader contract are
maintained in the independent workspace repository. No database migration was
needed; the OpenAPI snapshots and generated app types changed for the new
authenticated read/index and explicit merge/reversal operations.

| Boundary | Command | Result and limit |
| --- | --- | --- |
| Persisted owner behavior | `DATABASE_URL=postgresql://vesper:localdev@127.0.0.1:64743/artifact_reconcile_20261001_01 PYTHONPATH=. .venv/bin/python -B -m alembic upgrade head`; `TEST_DATABASE_URL=postgresql://vesper:localdev@127.0.0.1:64743/artifact_reconcile_20261001_01 TEST_DATABASE_DISPOSABLE=1 PYTHONPATH=. .venv/bin/python -B -m pytest -p no:cacheprovider tests/inbound/test_kept_things_postgres.py tests/api/test_kept_things.py tests/api/test_artifact_projections.py -q`; `DATABASE_URL=postgresql://vesper:localdev@127.0.0.1:64743/artifact_reconcile_20261001_01 PYTHONPATH=. .venv/bin/python -B -m alembic check` | Fresh disposable DB migrated from empty; 25 tests passed; Alembic found no new upgrade operations. Proves owner scoping, exact-source checks, persisted owner-confirmed alias and retry, independent Source revocation, reversal and stable original references. Does not prove production authentication, semantic identity, concurrent merge races, or deployed service behavior. Exact test DB was dropped and the PostgreSQL container started for this run was stopped; the lane volume was preserved. |
| Backend static/API coverage | `ruff check --no-cache backend/api/routes/kept_things.py backend/api/routes/artifact_projections.py backend/core/db/kept_things.py backend/core/models/kept_thing.py backend/api/router_registry.py tests/api/test_kept_things.py tests/api/test_artifact_projections.py`; `ruff format --check --no-cache` on those seven files; `make api-coverage-check` | Ruff and formatting passed; API coverage passed: 583 active, 15 dark (0 unflagged), 62 retiring operations. Targeted mypy terminated with an internal error in mypy 2.3.1; no mypy result is claimed. Backend commit hooks passed Ruff, formatting, Vulture, secret/key checks, import boundaries, route auth, and related policy checks. |
| App and generated contracts | `npm run typecheck`; `npm run test:typecheck:contracts`; `npm run generate-api-types:check`; `npm run docs:check`; `npx jest --runInBand __tests__/utils/api/mock/experienceGraph.test.ts __tests__/screens/kept-thing-reader.test.tsx __tests__/screens/kept-thing-reconcile.test.tsx` | Typecheck, generated API check, app docs check passed; three suites / 12 tests passed, including explicit confirmation, reversal-capable reader action, exact-source navigation/return, mock parity, and target-source read failure/retry with confirmation blocked. These are local TypeScript/Jest checks, not native or live-service UI evidence. |
| Workspace docs and native QA readiness | `make docs-check`; `npm run qa:polish:scenarios`; `npm run qa:design:check -- canonical-artifact-reader` | Workspace docs checks passed after refreshing the generated API counts; 31 scenario IDs passed. Design-ref check succeeded with its existing warning that the doctrine-only surface has no pinned design manifest. No simulator screenshot, VoiceOver, Android/physical-device, or authenticated mobile-to-service acceptance was run. |

The owner-controlled reconciliation contract is now explicit in the canonical
artifact-reader surface contract and this roadmap. Private canonical Collection
membership now has backend persistence and owner commands; shared membership,
audience/receiving, Life integration, broader source/audience lifecycle replay,
and native acceptance remain open. None is implied by the reconciliation
receipt above.

### October 1 private consumer-Collection backend foundation

This slice makes Strategy the canonical owner for user Collections over stable
kept-Thing references in the existing Postgres service. It does not repurpose
editorial `/api/collections` or viewer-specific derived `life_organization`,
and adds no service. Collections own names, revisions, status and many-to-many
membership; they do not copy Source payloads or take over Source permissions.
Authenticated owner commands create, list, open, rename, add/remove the owner's
kept Things, and soft-delete a Collection without deleting those Things.
Commands are revision-bound and replay-safe; adds/removals require exact owner
confirmation. Cross-owner membership, shared recipients, audience grants,
whole-collection serving, auto-filing and Life UI are not implemented.

Backend commit `4b419349b` is committed on the local `codex/artifact-foundation`
lane. The workspace records the seven new backend operations in its canonical
OpenAPI snapshot and marks them `retiring` in operation policy until a reviewed
Life consumer and device evidence justify mobile activation. The active mobile
projection and generated TypeScript remain unchanged; no app files were changed.

| Boundary | Command | Result and limit |
| --- | --- | --- |
| Persisted owner lifecycle | `DATABASE_URL=postgresql://vesper:localdev@localhost:64743/consumer_collection_20261001_a7f3 ./.venv/bin/python -m alembic upgrade head`; `TEST_DATABASE_URL=postgresql://vesper:localdev@localhost:64743/consumer_collection_20261001_a7f3 TEST_DATABASE_DISPOSABLE=1 SKIP_AUTH=true PYTHONPATH=. ./.venv/bin/python -m pytest -p no:cacheprovider tests/api/test_consumer_collections.py tests/inbound/test_consumer_collections_postgres.py -q`; `DATABASE_URL=postgresql://vesper:localdev@localhost:64743/consumer_collection_20261001_a7f3 ./.venv/bin/python -m alembic check` | The dedicated disposable DB is at `consumercol01`; seven focused API/Postgres tests passed; Alembic found no schema drift. Covers private owner scope, stable Thing references, remove versus soft-delete, stale revisions, replay without resurrecting removed membership, and preserved Things after Collection deletion. No production auth, shared-recipient or deployed-service acceptance. |
| Backend static/governance | `ruff check --no-cache` and `ruff format --check --no-cache` on the seven changed Python source/test files; `./.venv/bin/python scripts/check_alembic_single_head.py`; `make api-coverage-check` | Ruff and formatting passed; 1 Alembic head across 481 migrations; API coverage passed with 583 active, 15 dark, 0 unflagged, and 69 retiring operations. Commit hooks passed after running with the lane's `.venv` on PATH; static CI-parity guards including route auth and status-write safety passed. |
| Cross-repo API contract | `./scripts/sync-types.sh` | Offline OpenAPI export and projection succeeded; generated types passed `tsc --noEmit`. Full backend snapshot added the seven endpoints. App projection remained 461 paths / 508 operations and generated app types were unchanged because the routes are not yet mobile consumers. No device or Life-screen acceptance. |

The test database was created solely for this slice and dropped after
verification; the artifact lane's Postgres service and volume remain available
for the next implementation slice. This receipt is backend/database evidence
only: the Collection root has not yet become a user-facing mobile experience.

### October 1 private consumer-Collection app data facade

This follow-on consumes the generated authenticated Collection operations
without introducing a second Collection or identity owner. Workspace commit
`2c93873c` activates the reviewed app projection and records its ownership
policy; app commit `1241835ba` adds `data/consumerCollections.ts` with
session-scoped paginated index/detail queries and gated create, rename, add,
remove and soft-delete mutations. Successful writes invalidate only that
account's Collection index/detail cache. Both real and stateful mock modes use
the shared API boundary. This is a data-layer contract, not a Life screen,
navigation path, native acceptance, shared membership, or recipient-grant
implementation.

Focused app evidence: TypeScript typecheck, generated-contract typecheck, the
Collection/query-key Jest suites (3 suites, 18 tests), targeted ESLint, mock/real
parity QA (6 suites, 185 tests), and API-boundary checks passed. Workspace API
coverage passed with 590 active, 15 dark, 0 unflagged, and 62 retiring
operations. App documentation checks passed for headers and links (330
Markdown files). These checks establish API/data-facade behavior and mock/real
selection boundaries; they do not establish a rendered Life experience or
device/service acceptance.

### October 1 Life Collections contract reconciliation

The accepted September 29 Life decision replaces the Threads reading with
Collections and sets the entry rule: Time for a new or collection-sparse
record, Collections once collections exist, then resume the last selected
reading. Workspace commit `9a49c480` updates the canonical Life experience
contract to this target. App commit `fd62ded2d` keeps the native contract
truthful by distinguishing the accepted target from the current Time/Places/
Threads/People runtime and by marking its exported design as legacy evidence,
not approval for the Collections composition. These are contract updates, not
runtime or visual implementation.

The read-side seam is now explicit: Consumer Collection detail supplies
Collection metadata and stable member `ThingRef`s; the Thing projection
supplies currently authorized original references, but neither supplies a
user-facing Thing title/summary. Life may own a read composition, but must
resolve presentation through current Thing/Source authority rather than
copying claims or inventing a semantic label. The next Life-facing member
implementation therefore needs that bounded composition contract and its
authorization, pagination and stale-cache behavior before a Collection member
UI is credible. `make docs-check` passed after the contract changes. No API,
model, screen, navigation, native screenshot or device acceptance changed in
this increment.

### October 1 owner-backed Life Collections root read

Backend `LifeRootLens` now separates root readings from the existing four-value
`LifeLens` used by the complete corpus, record and organization readers. The
Life root endpoint accepts Collections and reads the authenticated owner's
canonical Collection rows through one bounded query. It returns at most eight
owner summaries, each with its exact Collection revision and current member
count, plus exact total count; it does not hydrate Things or make an N+1 call.
The Collection's own ResourceRef is the authority and destination, so the root
does not invent Source provenance. An empty Collection root remains genuinely
empty. Existing Time/Places/People/Threads corpus behavior is unchanged.

The workspace Life contract, roadmap and Current State record this increment.
Backend commit `3f67aa32c` adds the owner-backed root read; app commit
`4532fd497` mirrors the root/corpus lens split and deliberately keeps
Collections out of native controls until a real detail route and member
composition exist. Both commits remain local to `codex/artifact-foundation`,
not merged or published. The app preflight also exposed existing raw-touchable
and ambient-date-locale violations in the reconciliation reader; the app
commit adopts the existing `Tap` primitive and pins the locale, with the full
app suite passing afterward. The generated OpenAPI snapshots and app types
are synchronized. Focused backend unit/API tests passed (65); the owner-scoped Collection/Postgres
integration tests passed (3) against a temporary, non-volume disposable
PostGIS database; the container was removed. App typecheck passed; five
focused Life/root-mock Jest suites passed (56 tests); backend Ruff check/format,
API coverage, and workspace `make docs-check` passed.

The final change-aware cross-repo preflight also passed against the explicit
starting revisions recorded in the command below. It ran the complete app
suite (1,292 suites / 9,198 tests), backend suite (22,104 passed, 14 skipped,
53 xpassed), 118 contract tests, full backend static checks, OpenAPI snapshot
and app-projection checks, generated-type parity, schema bridge, API coverage
(590 active, 15 dark, 0 unflagged, 62 retiring), and documentation links/spine/
canon checks. Jest reported one worker that did not exit gracefully and had
to be force-exited after the passing suite; this is a test teardown warning,
not a failed suite. An earlier full preflight had one intermittent
`consumerCollections.test.tsx` failure; its isolated rerun and this full run
passed. The cause of that earlier failure was not established.

| Boundary | Exact verification | Result and limit |
| --- | --- | --- |
| Cross-repo preflight | `WORKSPACE_BASE_REF=1132952be2106483dde0eebdc5f0bc4a7a9828af AGENT_BASE_REF=4b419349bc4410e92f62a2c35815d814a434afa5 APP_BASE_REF=fd62ded2d0a0a492e9758af1bd77ac8759b6f1e2 RUFF_CACHE_DIR=/private/tmp/vesper-artifact-foundation-ruff-cache PYTEST_ADDOPTS='-p no:cacheprovider' make verify-changed` | Exit 0. Covers local code, contracts, OpenAPI, generated types and documentation at those exact lane bases. Does not establish native Collections UI, visual/device acceptance, deployed auth, or production-service behavior. |

This is backend/API foundation evidence, not a native Collections experience,
member reader, visual, device, or production-service acceptance. The next
independent Life slice is the bounded current-authority member composition
contract; do not expose a dead-end Collections row or implement member UI
before that contract and the corresponding design are ready.

### October 1 revision-bound Collection detail pagination

Backend `Consumer Collection` detail pagination now returns a Collection
revision on the first page and accepts that revision on continuation requests.
The owner Collection row is read under a shared lock for each bounded detail
query, so canonical writes cannot interleave with the page read; if the
revision has changed since page one, the route returns `409 Conflict` and the
client must restart at page one. The app pins continuation pages to the first
page revision, sends `expected_revision`, and the stateful mock enforces the
same stale-page behavior. This makes count, membership and pagination
consistency explicit without deciding how a member should be rendered.

Backend commit `ebe90232b` and app commit `43c4b3b51` implement the slice on
`codex/artifact-foundation`. Workspace commit `b9dcc369` immediately precedes
this cross-repo increment; the receipt commit records the updated contract,
OpenAPI snapshots and this roadmap. All commits are local to the lane and are
not merged or published.

| Boundary | Exact verification | Result and limit |
| --- | --- | --- |
| Database contract | `DATABASE_URL=postgresql://vesper:localdev@127.0.0.1:64743/artifact_collection_paging_20261001_01 PYTHONPATH=. .venv/bin/python -B -m alembic upgrade head`; `TEST_DATABASE_URL=postgresql://vesper:localdev@127.0.0.1:64743/artifact_collection_paging_20261001_01 TEST_DATABASE_DISPOSABLE=1 SKIP_AUTH=true PYTHONPATH=. .venv/bin/python -B -m pytest -p no:cacheprovider tests/api/test_consumer_collections.py tests/inbound/test_consumer_collections_postgres.py -q`; `DATABASE_URL=postgresql://vesper:localdev@127.0.0.1:64743/artifact_collection_paging_20261001_01 .venv/bin/python -B -m alembic check` | Empty disposable DB migrated successfully; 10 focused API/Postgres tests passed; Alembic found no new operations. The Postgres case proves stale continuation rejection after a persisted revision change in the lane DB, not production concurrency or deployed-service behavior. |
| Backend checks | `/opt/homebrew/bin/ruff check --no-cache` and `/opt/homebrew/bin/ruff format --check --no-cache` on changed backend files; backend hooks during commit | Ruff, format and commit hooks passed. |
| App contract and behavior | `npm exec jest -- --runInBand __tests__/data/consumerCollections.test.tsx __tests__/utils/api/http.test.ts __tests__/utils/api/mock/experienceGraph.test.ts`; `npx tsc --noEmit`; `npm run schema-bridge` | 3 suites / 107 tests passed; typecheck passed; schema bridge passed (376 facade exports, 1,372 generated models). No rendered screen or device acceptance. |
| Cross-repo preflight | `WORKSPACE_BASE_REF=b9dcc36979806bbee5f8b46acb6b590aaba4dd84 AGENT_BASE_REF=3f67aa32c609b6ba613bca0ebf9e8d8b4e2f2a27 APP_BASE_REF=4532fd497e477ba9d343cbe860e6a8df1c8889a1 RUFF_CACHE_DIR=/private/tmp/vesper-artifact-foundation-ruff-cache PYTEST_ADDOPTS='-p no:cacheprovider' TEST_DATABASE_URL=postgresql://vesper:localdev@127.0.0.1:64743/artifact_collection_paging_20261001_01 TEST_DATABASE_DISPOSABLE=1 SKIP_AUTH=true make verify-changed` | Exit 0. Full app merge suite passed (1,292 suites / 9,199 tests); full backend suite passed (22,105 passed, 14 skipped, 1 xfailed, 52 xpassed); 118 contract tests passed; OpenAPI/projection/generated-type, API coverage, docs links/spine/canon and static checks passed. App lint retained 169 existing warnings; backend reported existing warnings. No visual/device, deployed auth or production-service acceptance. |

The temporary database `artifact_collection_paging_20261001_01` was created
after confirming that exact name was absent from the isolated
`vesper-artifact-foundation` Postgres service. It was dropped after successful
verification; the lane service and volume were preserved. This increment is
not a UI member-composition decision: founder approval remains necessary for
product meaning, labels and user-visible hierarchy, while routine pagination,
cache invalidation and contract implementation remain lane-owned.

### October 1 stale Collection continuation recovery

The app data facade now recognizes only the Collection reader's explicit
revision-change `409` (not every `409`) and resets that exact account- and
Collection-scoped infinite query. TanStack then reloads page one and derives
new continuation parameters from the returned revision. This closes the
consumer-side half of the stale-page contract without a stale-offset retry or
UI-specific recovery code. It does not add a Collection screen or solve the
member-presentation boundary.

App commit `833a0bb38` is local on `codex/artifact-foundation`. The exact
cross-repo preflight bases were workspace `6570c29333641c3a261146472d0357dad633ec8b`,
backend `ebe90232b4daa4a9c09a0780f1bffb9366176fa9`, and app
`43c4b3b51cb933610745fc526335264b1af27680`; no backend or wire schema changed.

| Boundary | Exact verification | Result and limit |
| --- | --- | --- |
| Stale continuation recovery | `npm exec jest -- --runInBand __tests__/data/consumerCollections.test.tsx` | 1 suite / 4 tests passed, including a persisted revision change and a restart at offset zero using the new revision. |
| App fast gate | `npm run verify:fast` | Passed: native compatibility, icon generation check, lint (0 errors / 169 existing warnings), typecheck, API boundaries, schema bridge, Home budgets and contract typecheck. |
| App merge scope | `npm run verify:merge -- --base 43c4b3b51cb933610745fc526335264b1af27680` | Passed: 98 suites / 725 tests over the two changed files and related smoke/convention tests. |
| Cross-repo preflight | `WORKSPACE_BASE_REF=6570c29333641c3a261146472d0357dad633ec8b AGENT_BASE_REF=ebe90232b4daa4a9c09a0780f1bffb9366176fa9 APP_BASE_REF=43c4b3b51cb933610745fc526335264b1af27680 RUFF_CACHE_DIR=/private/tmp/vesper-artifact-foundation-ruff-cache PYTEST_ADDOPTS='-p no:cacheprovider' make verify-changed` | Exit 0 after the sandbox denied one initial ESLint cache write; rerunning the exact gate with the lane-local cache write permitted passed both `verify:fast` and the 98-suite merge scope. No API/schema/database/native-device boundary changed. |

### October 1 repeatable Artifact Reader accessibility capture

The ownership decision in section 0 remains in force: `codex/artifact-foundation`
is the single accountable lane for this artifact-roadmap outcome, with
workspace/backend/app ownership kept in their independent Git histories. No
duplicate branch or worktree was opened. The app's assigned-simulator QA runner
now applies a capture's declared `systemContentSize`, records it in the run
manifest, and restores the simulator's previous setting. The artifact-reader
accessibility flow also now asserts the source screen's actual `Original`
heading instead of a stale test ID. App commit `be51135e3` contains these QA
and operating-guidance corrections; it does not change product behavior. App
commit `3aaceef88` adds the validated verdict/manifest snapshot and updates the
reader contract with the exact evidence boundary and unresolved canon issue.

The post-commit run used Vesper QA SE / iOS 18.2 at app revision `be51135e3`.
It captured 14 standard artifact-reader screenshots and 10 screenshots at
`accessibility-extra-extra-extra-large`, including the exact calendar original
and return, the ticket's vertical route reflow, and scroll access to the source
action. All captures are deterministic mock fixtures. The repeatable setting
and actual source heading are now part of the evidence contract, rather than
assumptions about simulator state.

| Boundary | Exact verification | Result and limit |
| --- | --- | --- |
| QA harness | `npm run qa:polish:test` | Passed all constituent polish-QA checks, including the device-forwarding regression. This validates the harness, not the reader's live-service behavior. |
| Native reader capture | `VESPER_METRO_URL=http://192.168.1.153:64747 npm run qa:surface -- canonical-artifact-reader --after --device="Vesper QA SE"` | Device doctor passed; both registered captures completed (14 standard screenshots, 10 maximum-text screenshots). Design-reference comparison was skipped because this doctrine-only surface has no comparison manifest. The fixture run does not prove live backend readback, persistence, or authenticated data. |
| Structured review | `node scripts/polish-qa/verdict.mjs validate .maestro/runs/_pairs/canonical-artifact-reader/after`; `node scripts/polish-qa/verdict.mjs diff .maestro/runs/_pairs/canonical-artifact-reader/after` | Verdict validates as `mixed`. The diff reports three explicitly recorded pass-to-fail review changes (designLanguage, intent, overall); its exit 1 is the expected signal for those review regressions, not an unrecorded capture failure. The committed verdict and manifest are under the app's `docs/surfaces/canonical-artifact-reader/verdicts/` history. |

The one P2 is a canon-alignment issue, not an instruction to recolor the app:
the QA doctrine reserves gold for curator/editorial use, while `Design
Language.md` also names gold as Vesper voice/kicker/attribution; artifact-family
labels use the same gold token. No pinned surface reference resolves that
boundary, so visual intent is not certified until the founder/design authority
chooses or sharpens the rule. Layout, source authority, and all 17 behavioral
assertions passed. VoiceOver activation, physical-device/Android behavior,
gestures, user preference, loading/error states, and live-service acceptance
remain open.

### October 1 bounded owner-authorized Thing projection batch

The backend now serves up to 50 unique owner `ThingRef`s in one bounded batch
request. It resolves active aliases in sets, reads each canonical Thing/group
and its retained-source references without a per-Thing query pattern, then
reauthorizes the retained Sources against the owner's current Intake authority.
The existing single-Thing projection delegates to the same reader with a
one-item batch, preserving one authorization/projection path. The reconciliation
screen now requests its source and selected target together. This is a useful
read primitive for future Collection composition, but is not that composition:
the result still carries authorized original references rather than user-facing
Thing titles/summaries, and no Life Collection detail UI is added.

Backend commit `2e2ee4d6aa8b79bc71976b7946369d3bb72f2f74` and app commit
`eb14a00fa4750c2bba524753ad16376d3094d3a0` are local on
`codex/artifact-foundation`. Workspace commit `f6efac21` is the pre-receipt
base; this workspace change synchronizes the full/app OpenAPI snapshots and
Current State and records the clarified ownership decision. The three histories
remain independent; none of these follow-on changes is merged or published.

Ownership is explicit: Strategy is the product/domain owner for artifact and
Collection semantics; the existing coordinated artifact-foundation tuple is
the single accountable execution lane for this roadmap outcome. Within that
tuple, backend owns canonical persistence and owner-scoped authorization, app
owns presentation/navigation/cache behavior, Strategy Technical owns its
reusable producer request/result and research runtime, and Orchestration owns
capture transport plus Home/Places delivery. This batch projection belongs to
the artifact lane; it is not a new Life-screen or Orchestration assignment.
Founder review remains reserved for choices that change product meaning,
authority, privacy/audience behavior, or visible claims.

| Boundary | Exact verification | Result and limit |
| --- | --- | --- |
| Backend owner read (from `travel-agent/`) | `TEST_DATABASE_URL=postgresql://vesper:localdev@127.0.0.1:64743/artifact_batch_20261001_02 TEST_DATABASE_DISPOSABLE=1 SKIP_AUTH=true PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=. .venv/bin/python -B -m pytest -p no:cacheprovider tests/api/test_artifact_projections.py tests/inbound/test_original_source_reader.py tests/inbound/test_kept_things_postgres.py -q` | 38 tests passed against an isolated disposable PostgreSQL database. Covers bounded batch validation, owner scoping, alias resolution, current-source reauthorization, single-reader parity and app-facing route behavior. The exact database was dropped after verification; the lane service and volume were preserved. |
| Backend static and API contract | `make ci-static`; `./scripts/sync-types.sh`; `make api-coverage-check` | Static checks passed, including mypy (1,902 source files). Offline snapshot, app projection and generated types synchronized; typecheck passed. API coverage: 591 active, 15 dark (0 unflagged), 62 retiring. |
| App reader | `npm exec jest -- --runInBand __tests__/screens/kept-thing-reconcile.test.tsx __tests__/utils/api/mock/experienceGraph.test.ts`; `npm run typecheck -- --pretty false` | Two suites / seven tests passed; typecheck passed. `verify:fast` later reported zero lint errors and 167 existing warnings. No Collection screen or device acceptance. |
| Workspace docs | `make docs-check` | Passed after synchronizing generated API counts in Current State. |
| Cross-repo change-aware preflight | `WORKSPACE_BASE_REF=f6efac21e77d8802a816e5a457bb2ef03647439c AGENT_BASE_REF=ebe90232b4daa4a9c09a0780f1bffb9366176fa9 APP_BASE_REF=3aaceef880ff6b8ffaf2859c06aaa3d92d7a96c9 RUFF_CACHE_DIR=/private/tmp/vesper-artifact-foundation-ruff-cache PYTEST_ADDOPTS='-p no:cacheprovider' TEST_DATABASE_URL=postgresql://vesper:localdev@127.0.0.1:64743/artifact_batch_20261001_02 TEST_DATABASE_DISPOSABLE=1 SKIP_AUTH=true make verify-changed` | Exit 0. App: 1,292 suites / 9,200 tests. Backend: 22,110 passed, 14 skipped, 53 xpassed. Workspace scripts: 118 passed; static, OpenAPI/projection/generated-type parity, API coverage, schema bridge, and docs links/spine/canon passed. An earlier full attempt had one isolated worker SIGSEGV in unrelated `PlacesEntityOpening`; its isolated rerun and the final full suite passed; cause was not established. No device, live-auth or production-service acceptance. |

### October 1 concurrent owner-confirmed reconciliation acceptance

The earlier persisted reconciliation receipt explicitly left concurrent merge
races unproven. Backend commit `10c5877d8b14663e40d3a6a508b8f40a7fd8dcb1`
adds three independent-connection Postgres cases: the same exact merge command
submitted concurrently creates one active alias and one revision transition;
opposite-direction merges at the same starting revisions have one winner and a
stale-revision loser without an alias cycle; and concurrent exact reversal
retries reverse one alias once while restoring both original ThingRefs. These
tests exercise the existing canonical lock order, revision checks, command
idempotency and reversible alias owner. No runtime code, schema, API or product
behavior changed.

| Boundary | Exact verification | Result and limit |
| --- | --- | --- |
| Fresh-database readiness | `docker exec vesper-artifact-foundation-postgres-1 createdb -U vesper thing_races_20261001_01`; `DATABASE_URL=postgresql://vesper:localdev@127.0.0.1:64743/thing_races_20261001_01 PYTHONPATH=. .venv/bin/python -B -m alembic upgrade head`; `DATABASE_URL=postgresql://vesper:localdev@127.0.0.1:64743/thing_races_20261001_01 PYTHONPATH=. .venv/bin/python -B -m alembic check` | Disposable DB migrated from an empty schema; Alembic reported no new upgrade operations. The named database was dropped after verification; the lane service and volume were preserved. |
| Owner reconciliation lifecycle | `TEST_DATABASE_URL=postgresql://vesper:localdev@127.0.0.1:64743/thing_races_20261001_01 TEST_DATABASE_DISPOSABLE=1 SKIP_AUTH=true PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=. .venv/bin/python -B -m pytest -p no:cacheprovider tests/inbound/test_kept_things_postgres.py -q` (from `travel-agent/`) | 12 tests passed, including all three new barrier-synchronized concurrency cases against real PostgreSQL. This establishes repository transaction behavior in the isolated lane DB, not production database settings or fleet-level deployed behavior. |
| Change-aware preflight | `WORKSPACE_BASE_REF=bb5e20e700c5ab393eb3d045c8290d13a8290871 AGENT_BASE_REF=2e2ee4d6aa8b79bc71976b7946369d3bb72f2f74 APP_BASE_REF=eb14a00fa4750c2bba524753ad16376d3094d3a0 RUFF_CACHE_DIR=/private/tmp/vesper-artifact-foundation-ruff-cache PYTEST_ADDOPTS='-p no:cacheprovider' TEST_DATABASE_URL=postgresql://vesper:localdev@127.0.0.1:64743/thing_races_20261001_01 TEST_DATABASE_DISPOSABLE=1 SKIP_AUTH=true make verify-changed` | Exit 0. Backend static checks, route/import guards and mypy passed; selected merge scope passed 82 tests, including the changed Postgres file. Workspace and app had no changed files relative to these bases. No API/schema/app, native, authenticated-device or production-service behavior changed. |

### October 1 bounded Life Collection member data composition

The app data facade now composes a canonical Collection membership page with
one bounded batch of current owner-authorized Thing projections. It is
session-scoped, paginated, pins continuation to the Collection revision,
preserves each membership's Thing identity and ordering, and fails closed if a
projection is missing, duplicated or unexpected. Empty pages skip the batch.
Collection writes invalidate only the current account's member-page cache.
The reader carries authorized original references only: it does not copy
Source content, synthesize claims, or infer titles, previews or hierarchy.
This completes data composition for the current read contract, not a native
Life Collection detail screen or approval of the member presentation.

Ownership remains the one-lane decision in section 0: Strategy owns the
artifact/Collection outcome and this coordinated lane carries it across the
independent workspace/backend/app repositories. Backend remains authority for
canonical Collection membership, Thing identity and current-source
authorization; the app owns the page-to-projection join, pagination/cache
behavior and eventual presentation; workspace owns the shared roadmap,
contract alignment and evidence. Founder approval is still required for
user-facing member labels, previews, grouping/hierarchy or claims that change
product meaning. No separate Life implementation lane is needed for this data
composition, and no Collection UI is exposed by it.

App commit `b94a50ccf2b37a777048de067cba0cd09b5dcd8f` is local on
`codex/artifact-foundation`; it follows app base `eb14a00fa4750c2bba524753ad16376d3094d3a0`.
No backend API, OpenAPI snapshot, generated type or database change was
required. Workspace base before this receipt is `53909466f00b695bf66dde9604b97534169453aa`;
backend stayed at `10c5877d8b14663e40d3a6a508b8f40a7fd8dcb1`. Histories remain
independent; this receipt does not merge or publish any lane.

| Boundary | Exact verification | Result and limit |
| --- | --- | --- |
| App focused composition | `npm exec jest -- --runInBand __tests__/data/consumerCollections.test.tsx` | 1 suite / 9 tests passed: bounded batch composition, ordering, empty page, account/session isolation, missing projection failure, stale-revision page-one recovery, and scoped mutation invalidation. |
| App data/API parity | `npm exec jest -- --runInBand __tests__/data/consumerCollections.test.tsx __tests__/utils/api/http.test.ts __tests__/utils/api/mock/experienceGraph.test.ts` | 3 suites / 114 tests passed, including the HTTP batched query shape and stateful mock member-to-projection behavior. Targeted ESLint had 0 errors and 3 existing `import/first` warnings in `http.test.ts`; no warning was suppressed. |
| App merge scope | `npm run verify:merge -- --base eb14a00fa4750c2bba524753ad16376d3094d3a0` | Passed: 616 suites / 4,951 tests. Jest reported one worker teardown warning and forced exit after the passing run; it is recorded as a teardown warning, not a failed suite. |
| Backend contract regression | `TEST_DATABASE_URL=postgresql://vesper:localdev@127.0.0.1:64743/collection_members_20261001_01 TEST_DATABASE_DISPOSABLE=1 SKIP_AUTH=true PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=. .venv/bin/python -B -m pytest -p no:cacheprovider tests/api/test_consumer_collections.py tests/api/test_artifact_projections.py tests/inbound/test_kept_things_postgres.py -q` (from `travel-agent/`) | 33 tests passed against the exact disposable lane database after a full migration from empty; Alembic check reported no model drift. The exact database was dropped after verification. This rechecks the existing backend contracts used by the app composition; no backend code changed in this slice. |
| Cross-repo change-aware preflight | `WORKSPACE_BASE_REF=53909466f00b695bf66dde9604b97534169453aa AGENT_BASE_REF=10c5877d8b14663e40d3a6a508b8f40a7fd8dcb1 APP_BASE_REF=eb14a00fa4750c2bba524753ad16376d3094d3a0 RUFF_CACHE_DIR=/private/tmp/vesper-artifact-foundation-ruff-cache PYTEST_ADDOPTS='-p no:cacheprovider' make verify-changed` | The first sandboxed attempt stopped at an Expo ESLint-cache permission error; with the lane cache write allowed, `verify:fast` passed (0 lint errors / 167 warnings), the scoped merge suite passed (616 suites / 4,951 tests), and docs links/spine/canon checks passed. Native Life detail rendering, actual member labels/previews, VoiceOver/device acceptance, authenticated mobile-to-service readback and production-service behavior remain outside this data-facade verification. |

### October 1 owner replacement-time editor

Backend commit `11fe148fe` and app commit `fac17ba97` add the private,
revision-bound `replace_time` affordance and native owner editor. The backend
projection offers the action only with an explicit private target and current
revision. The app preserves each captured aware instant's wall-clock date/time
and UTC offset, uses UTC only as a neutral picker coordinate, does not infer an
event zone, retains the draft after a failed write, binds exact retry identity
to the correction payload, refetches after success, and offers existing
revision-bound Undo only when authorized by the refreshed private projection.
No API/database migration was needed. OpenAPI snapshot, mobile projection and
generated app types were regenerated offline; the cross-repo sync completed
with no TypeScript errors.

| Boundary | Exact verification | Result and limit |
| --- | --- | --- |
| Backend projection | `PYTHONPATH=. .venv/bin/python -m pytest -p no:cacheprovider tests/core/test_canonical_artifact_projection.py -q` (from `travel-agent/`) | 27 tests passed. The replacement action's explicit owner target/revision gate and projection shape are fixture/projection evidence, not deployed-service evidence. |
| Backend lint/format | `/opt/homebrew/bin/ruff check --no-cache backend/core/canonical_artifact_projection.py backend/core/models/canonical_artifact.py backend/inbound/anchor_compiler.py tests/core/test_canonical_artifact_projection.py`; `/opt/homebrew/bin/ruff format --check --no-cache` on the same files | Both passed. Backend commit hooks also passed Ruff, formatting, Vulture, secret/prefix and repository architecture checks. |
| App behavior | `npm exec jest -- --runInBand __tests__/utils/canonicalArtifactTime.test.ts __tests__/utils/canonicalArtifactActions.test.ts __tests__/screens/canonical-artifact-reader.test.tsx __tests__/utils/api/mockIntakeV2.test.ts`; `npm run typecheck -- --pretty false`; targeted `npx eslint --no-cache` over the editor, reader, fixtures, helpers and focused tests | Four suites / 51 tests passed; TypeScript passed; targeted ESLint reported no warnings/errors. Tests cover explicit-offset preservation, date/time validation, neutral picker coordinate, action privacy, payload-bound idempotency/retry, draft retention, revision use, success receipt/refetch and owner-only Undo. Mock/service boundaries remain. |
| App mock correction parity and native Save/Undo | App `de36dcd86`; `npm test -- --runInBand __tests__/utils/api/mockIntakeV2.test.ts __tests__/utils/canonicalArtifactView.test.ts`; `npm run typecheck -- --pretty false`; `npm run verify:merge -- --base e7bdc660501eaa19234e6b45bda033658edaa2d4`; `env VESPER_METRO_URL=http://192.168.1.153:64747 node scripts/polish-qa/run-polish-qa.mjs canonical-artifact-reader --flow=polish/canonical-artifact-replacement-time-save-undo --device='Vesper QA SE'`; verdict and manifest committed as app `51d275d11` | Focused mock/reader tests passed (25); typecheck, changed-file ESLint, `docs:check` (349 Markdown links), `qa:polish:scenarios` (31), `qa:design:check -- canonical-artifact-reader`, verdict validation/committed checks and `qa:polish:test` passed. `verify:merge` passed 1,293 suites / 9,222 tests / 1 snapshot. Registered run `20261001T163935Z-canonical-artifact-reader` passed 1/1 on iOS 18.2 (`Vesper QA SE`), with the app implementation at `de36dcd86`; the screenshot shows the corrected dated time range and Undo, and the Undo view restores source-derived Starts/Ends. This is synthetic in-memory mock state only: it does not establish backend persistence, authenticated live-service readback, or production behavior. |
| Historical native editor capture | `VESPER_METRO_URL=http://192.168.1.153:64747 node scripts/polish-qa/run-polish-qa.mjs canonical-artifact-reader --flow=polish/canonical-artifact-replacement-time-editor --device="Vesper QA SE"`; verdict validate/commit for `.maestro/runs/20261001T141548Z-canonical-artifact-reader` | iOS 18.2 simulator captured 1/1 scenario: start, distinct `+02:00`/`+01:00` end fields, focused offset, reachable Save/Cancel and cancellation. Its keyboard configuration suppressed the software keyboard; it remains form-presentation evidence only. Its structured `pass` and two P2 usability observations are retained historically in `travel-app/docs/surfaces/canonical-artifact-reader/verdicts/20261001T141548Z.json`; do not use it to claim keyboard behavior. |
| Native keyboard, validation and return capture | `env SENTRY_DISABLE_AUTO_UPLOAD=true npm run ios -- --device "iPhone SE (3rd generation)" --port 64747`; `env VESPER_METRO_URL=http://192.168.1.153:64747 node scripts/polish-qa/run-polish-qa.mjs canonical-artifact-reader --flow=polish/canonical-artifact-replacement-time-editor --device="iPhone SE (3rd generation)"`; verdict validate/commit for `.maestro/runs/20261001T153024Z-canonical-artifact-reader` | Native iOS 18.2 build succeeded with 0 errors/4 warnings; Sentry auto-upload was disabled. The fresh registered flow, captured after finalizing its acceptance wording, shows the software keyboard with the focused start offset and helper visible, presses Enter, scrolls to Save/Cancel, then cancels and returns to the same synthetic artifact (1/1). Separately, on-screen key entry of `-04:00` surfaced “The end time must be after the start time” and disabled Save; Cancel left the original time unchanged. The validated verdict and matching manifest snapshot are `travel-app/docs/surfaces/canonical-artifact-reader/verdicts/20261001T153024Z.json` and `.manifest.json`. Evidence is limited to synthetic native form/validation behavior; no correction was submitted and no service persistence/readback/Undo or production authentication is established. |
| Contract regeneration and registry | `./scripts/sync-types.sh`; `make api-coverage-check`; `npm run qa:polish:scenarios`; `npm run qa:design:check -- canonical-artifact-reader` | Sync and typecheck passed; API audit passed (591 active, 15 dark, 0 unflagged, 62 retiring); all 31 polish scenario IDs passed. Design check remains doctrine-only with no pinned design-reference manifest. |
| Cross-repo change-aware preflight | `env -u DRY_RUN WORKSPACE_BASE_REF=7e007e46 AGENT_BASE_REF=10c5877d8 APP_BASE_REF=b94a50ccf RUFF_CACHE_DIR=/private/tmp/vesper-artifact-foundation-ruff-cache PYTEST_ADDOPTS='-p no:cacheprovider' make verify-changed`; `make docs-check` | Passed. App `verify:fast` had 0 lint errors / 167 warnings; app merge scope passed 1,293 suites / 9,216 tests / 1 snapshot. Backend static checks and mypy passed; selected backend tests passed (22,112 passed, 14 skipped, 1 xfailed, 52 xpassed, 8 warnings); 118 workspace script tests passed. Cross-repo contract, API coverage, compatibility, links/spine/canon and full workspace doc-governance checks passed. This is local preflight, not hosted CI. At this preflight the native Save/refetch/Undo mock round-trip had not yet run; the later mock-only proof is recorded above. Authenticated live mobile/API readback, deployed service, production credentials, Android/physical device and user preference remain unproven. |

### October 1 expanded canonical artifact reader portfolio

The October 1 iOS 18.2 Vesper QA SE run expands the prior single-flow mock
Save/Undo receipt to the full reader portfolio. It captured 30 screenshots
across four registered flows: 14 standard family/source/return captures, 10
captures at `accessibility-extra-extra-extra-large`, four replacement-time
editor/keyboard captures, and two synthetic Save/Undo captures. All four flows
and their Maestro assertions completed. The run used app implementation
revision `51d275d11`; app evidence commit `0a166e950622dafb221250f1a1a62b83cdf690d7`
updates the stable verdict and manifest.

| Boundary | Exact verification | Result and limit |
| --- | --- | --- |
| Registered scenario set | `npm run qa:polish:scenarios` | Passed; 31 scenario IDs registered. |
| Native portfolio capture | `VESPER_METRO_URL=http://127.0.0.1:64747 npm run qa:polish -- canonical-artifact-reader --after --device="Vesper QA SE"` | Four of four flows captured on iOS 18.2. The screenshots cover the standard reader families/fallbacks, exact calendar source and return, largest-text reflow/source access, keyboard/editor reachability, and mock correction readback/Undo. Deterministic fixtures and in-memory mock state only; no authenticated service readback or persistence. |
| Structured verdict | `npm run qa:verdict:validate -- .maestro/runs/_pairs/canonical-artifact-reader/after`; `npm run qa:verdict:diff -- .maestro/runs/_pairs/canonical-artifact-reader/after`; `npm run qa:verdict:committed` | Validation passed; the committed-verdict check passed for 79 receipts. The verdict is `mixed`: capture, correctness and visual gates pass, while intent fails on two reader captures because artifact-family gold labels conflict with the currently assigned gold role in QA doctrine. The diff exits 1 for the explicitly recorded scope-expanded overall change (`pass` to `mixed`); it is not evidence of an app-code regression. |
| Review follow-ups and unproven scope | Screenshot review and flow logs in `.maestro/runs/_pairs/canonical-artifact-reader/after` | P2 clarity observations include duplicated tentative status, technical raw UTC offsets, and absent endpoint-place labels. The gold-role finding is a canon question, not an instruction to recolor. VoiceOver activation, pinch/pan, loading/error states, Android/physical-device behavior, user preference, and authenticated live-service correction/readback remain unproven. |

The expanded evidence does not close the native acceptance package. The
reader's fixture-backed rendering and registered flows are better evidenced;
resolution of design authority and the unproven native/service boundaries
remain separate work.

### October 1 recipient-original reader continuity

The existing Home original card already identifies its sender, the explicit
recipient boundary, and the time the original was shared. Opening it used to
drop that full attribution in the Life-owned detail reader, which showed only
the sender. App commit `5bc3fe752` now derives the same recipient-safe line from
the selected current-authorized delivery and carries it into the exact-original
reader. The reader remains read-only: it neither turns opening into a reply,
retained copy, nor wider audience. Home and Life surface contracts now state the
cross-root continuity requirement. If sender or received time is unavailable,
the existing sender-only fallback remains; no timestamp is inferred from the
original's capture time.

The deterministic Home fixture was moved to May 30, 2026, before the registered
June 3 mock clock; a focused assertion prevents this "shared Saturday" receipt
from becoming future-dated. No backend/API schema, owner, or authorization
changed. App evidence commit `ed0cf8d1a` replaces the pre-commit screenshot
receipt with the repeat captured against app revision `5bc3fe752`.

| Boundary | Exact verification | Result and limit |
| --- | --- | --- |
| Recipient attribution and fixture | `npx jest --runInBand --no-cache __tests__/screens/original-delivery.test.tsx __tests__/utils/api/homeOriginalDelivery.mock.test.ts` | 2 suites / 26 tests passed, covering attributed detail rendering through success and transient material failure, plus the non-future fixture timestamp. |
| App fast gate | `npm run verify:fast` | Passed on app revision `5bc3fe752`: native compatibility, icon check, typecheck, API boundaries, schema bridge (376 facade exports / 1,373 generated models), Home budgets and contract typecheck. Lint had 0 errors and 167 existing warnings. |
| Registered native flow | `env VESPER_METRO_URL=http://127.0.0.1:64748 npm run qa:polish -- home-root --flow=polish/home-root-social-original --device='Vesper QA SE'` | Run `20261001T182244Z-home-root` captured 1/1 flow and 2/2 extra screenshots on Vesper QA SE / iOS 18.2, with manifest `gitSha` `5bc3fe752`; flow log confirms mock readiness (`home-original-recipient`, fixed clock `1780502400000`). Home displays Maya + **TO YOU** + received time, opens her exact words, and returns to the same Home context without a reply task. This is deterministic mock/native evidence, not authenticated relationship-service readback or real-recipient preference. |
| Structured visual review | `npm run qa:verdict:validate -- .maestro/runs/20261001T182244Z-home-root`; `npm run qa:verdict:diff -- .maestro/runs/20261001T182244Z-home-root`; `npm run qa:verdict:committed` | Validated `pass`, with two retained P2 observations: the note is below a longer geology reading in this scrolled capture, and the reader's compact `SHARED SAT, 4:25 PM` stamp omits month/day. Both registered design refs were opened; generated first-viewport comparison pairs have no matching screenshot in this component-interaction flow, so the verdict explicitly does not certify Home 03's note-first root opening. The receipt is recorded in `travel-app/docs/surfaces/home-root/verdicts/20261001T182244Z.json` and its manifest snapshot. |
| App changed-scope merge suite | `npm run verify:merge -- --base 0a166e950622dafb221250f1a1a62b83cdf690d7` | Jest completed 1,293 suites / 9,222 tests / 1 snapshot, all passed. This is local app evidence; the cross-repository `make verify-changed` checkpoint is recorded after this workspace receipt. |

The received-original flow advances the original-focused P6 slice only. It does
not settle Home's return-state ordering (Orchestration owns that placement),
recipient grants or withdrawal beyond the current Relationships authority,
Life Collection presentation, shared collection membership, or live-service
acceptance. The next independent artifact work can continue under section 0;
this flow adds no dependency on the unmerged Technical P3 producer.

### October 1 full date at received-original reader depth

The October 1 verdict's remaining timestamp ambiguity was specific to the
opened reader: `SHARED SAT, 4:25 PM` could become unclear when the original is
reopened much later. App commit `16d5fbc88` keeps Home's compact weekday stamp,
but the Life-owned received-original reader now shows the full recipient-local
calendar date and time from the same current-authorized delivery timestamp.
The original capture time is not substituted. The exact sender and **TO YOU**
boundary remain intact, and opening remains read-only. The date now fits on one
line at the captured iPhone SE width.

This closes the reader-date P2 observation from verdict
`20261001T182244Z`. It does not fix Home's post-return ordering or change the
text-only sender treatment in the Home preview; the committed follow-up verdict
records those two bounded P2 observations. That sender-presentation follow-up
belongs to Orchestration under the program roadmap's Home/Places ownership
boundary. Strategy retains the received-original semantics and Life reader
attribution/date; this artifact lane should not change Home composition or
presentation to address the finding. Home 03's note-first first viewport is
not established by this scrolled component/interaction flow.

| Boundary | Exact verification | Result and limit |
| --- | --- | --- |
| Reader-date and Home-compact formatter | `npx jest --runInBand --no-cache __tests__/utils/originalDeliveryTime.test.ts __tests__/screens/original-delivery.test.tsx` | 2 suites / 31 tests passed: full local date/time and explicit UTC fallback at reader depth, compact Home formatting, exact reader attribution, and Home→reader recipient continuity. |
| App fast gate and docs | `npm run verify:fast`; `npm run docs:check`; targeted `npx eslint --no-cache utils/originalDeliveryTime.ts app/original-delivery/'[deliveryId].tsx' __tests__/utils/originalDeliveryTime.test.ts __tests__/screens/original-delivery.test.tsx`; `npm run qa:polish:scenarios` | Fast gate passed on app `16d5fbc88`: 0 lint errors / 167 existing warnings, typecheck, API boundaries, schema bridge (376 facade exports / 1,373 generated models), Home budgets and test-contract typecheck. Docs headers passed for 9 files and links for 357 Markdown files; 31 polish scenario IDs passed; targeted ESLint emitted no diagnostics. |
| Registered native flow | `env VESPER_METRO_URL=http://127.0.0.1:64748 npm run qa:polish -- home-root --flow=polish/home-root-social-original --device='Vesper QA SE'` | Run `20261001T184311Z-home-root`, manifest `gitSha` `16d5fbc88`, captured 1/1 flow plus 2/2 extra screenshots on Vesper QA SE / iOS 18.2. Home retains `SHARED SAT, 4:25 PM`; the Life reader shows `SHARED MAY 30, 2026 · 4:25 PM`; return lands on the same Home content. Deterministic mock/native only. |
| Structured visual review | `npm run qa:verdict:validate -- .maestro/runs/20261001T184311Z-home-root`; `npm run qa:verdict:diff -- .maestro/runs/20261001T184311Z-home-root`; `npm run qa:verdict:commit -- .maestro/runs/20261001T184311Z-home-root home-root`; `npm run qa:verdict:committed` | Validated `pass`; committed as `e8b9be9e6`; all 81 committed verdicts validate. The reader-date P2 is closed. Current bounded findings are Home feed ordering below a long geology reading and the preview's text-only sender header versus the Home 03 reference avatar/name treatment. Both Home presentation findings route to Orchestration; this scrolled interaction flow does not certify Home 03's first viewport. |
| Local service startup boundary | `make dev-backend`; `SKIP_AUTH=true DEFAULT_DEV_USER_ID=00000000-0000-0000-0000-000000000005 ANTHROPIC_API_KEY=local-no-ai-calls make dev-backend` | First startup stopped at missing local provider configuration. With process-only placeholder and synthetic development identity, the local API started and `/health` returned 200; no AI provider call was made. The lane database had zero user rows and no correction record was provisioned, so no app-to-backend correction write/readback was exercised. This is startup evidence only, not authenticated persistence. API process was stopped; no account or artifact fixture was created. |
| Cross-repository change-aware preflight | `WORKSPACE_BASE_REF=7a95a8ee7886a0c79bf5b155867d4cad3c87e3d7 AGENT_BASE_REF=11fe148fee184c6219be2d9368f5f02419d96680 APP_BASE_REF=0a166e950622dafb221250f1a1a62b83cdf690d7 RUFF_CACHE_DIR=/private/tmp/vesper-artifact-foundation-ruff-cache PYTEST_ADDOPTS='-p no:cacheprovider' make verify-changed` | Passed with exit 0 on workspace `8b0ff6fc`, backend `11fe148f` (unchanged), and app `e8b9be9e6`. The app fast gate and full selected merge-scope suite passed; workspace docs links, spine and canon checks passed. This is local evidence, not hosted CI. |

### October 1 current-revision artifact portfolio capture

App commit `3c2bf4b71` changed mock owner-Thing reads to use the same
API-backed query path as live mode, added mock readback/session partition tests,
fixed original numbering to follow the displayed bundle order, and registered
the owner-confirmed reconciliation interaction. The read parity and source
numbering changes do not modify the replacement-time editor or its shared form
controls.

| Boundary | Exact verification | Result and limit |
| --- | --- | --- |
| App-focused checks before commit | Focused Jest, `npm run typecheck`, targeted ESLint and `npm run qa:polish:scenarios` | Four focused suites / 18 tests passed; typecheck passed; targeted ESLint emitted no diagnostics; 31 registered scenario IDs passed. See app commit `3c2bf4b71`. |
| Full registered native portfolio | `VESPER_METRO_URL=http://localhost:64747 npm run qa:surface -- canonical-artifact-reader --after --device="Vesper QA SE"` | Run `canonical-artifact-reader-after`, manifest revision `3c2bf4b71`: five flows captured, 33 screenshots total (14 standard reader/source/return, 10 largest-text, 4 replacement-time editor, 2 mock Save/Undo, 3 reconciliation). Maestro flow assertions completed 5/5. This is evidence capture, not a committed visual-reference verdict. |
| Software-keyboard acceptance | Opened `canonical-artifact-reader-replacement-time-editor-keyboard.png` from the full run and two focused reruns, `20261001T202156Z-canonical-artifact-reader` and `20261001T202335Z-canonical-artifact-reader` | The start-offset field is focused, but no software keyboard is visible in the assigned `Vesper QA SE` captures. A previous dedicated native run `20261001T153024Z` on `iPhone SE (3rd generation)` does show the keyboard; it remains evidence for that run only. Current-device cause is unresolved and the full portfolio must not be described as passing this assertion. |
| Reconciliation visual review | Selected, connected and separated screenshots in the full run | Owner control, two retained originals, connection, and separation state are visible. The sticky translucent header overlaps underlying page headings in the selected and connected states; record this as a P2 component-fit finding in the pending structured visual review. |
| Current acceptance boundary | Manifest, flow log and screenshot review | No authenticated backend persistence/readback, Android/physical-device, VoiceOver, or user-preference claim is established. The current full portfolio's structured visual verdict remains pending; preserve the keyboard discrepancy and header observation when judging it. |

### October 1 focused reconciliation-label polish

App commit `033bd608f` removes the internal `CONNECTION 01` ordinal from the
owner-confirmed bundle-connection card. The dated evidence and direct accessible
Separate action remain. A focused reader regression test protects the consumer
copy from reintroducing the ordinal. This is presentation-only: it changes no
identity, authorization, reconciliation, or source-retention semantics.

The post-commit iOS 18.2 Vesper QA SE capture is run
`20261001T203947Z-canonical-artifact-reader`, at app revision `033bd608f`. Its
selected, connected, and separated states were visually inspected; the
structured verdict is committed in app commit `827d26c8f` as
`travel-app/docs/surfaces/canonical-artifact-reader/verdicts/20261001T203947Z.json`
and its manifest snapshot. The verdict passes this focused interaction with
two P2 follow-ups: underlying title text bleeds through the translucent sticky
header, and the connected-bundle saved-date sentence is mechanically phrased.
The capture is deterministic app mock state only, and it does not claim the
route-entry first viewport.

This focused receipt does not replace or upgrade the separate five-flow
portfolio at app revision `3c2bf4b71`: its structured visual verdict remains
pending, and its assigned-device editor capture still lacks the software
keyboard. The reason for the ownership choice remains recorded in section 0;
the UI/test/verdict work stayed in the existing coordinated
`codex/artifact-foundation` tuple, with no duplicate lane or worktree.

### October 1 explicit correction rehearsal: startup disclosure and live native flow

The focused Save → canonical readback → Undo → canonical readback rehearsal
uses only synthetic owner, submission, candidate, and source records in the
lane's disposable local PostgreSQL database. The first local backend startup
attempt also made an outbound request to public Hugging Face model-host
metadata while resolving the configured local model assets. No user content,
account data, credentials, or artifact/source payload was sent in that
metadata lookup. The backend was restarted with Hugging Face offline flags for
the rehearsal; this disclosure is separate from the app's local API traffic.

An early native attempt exposed an important acceptance gap: the editor showed
“Correction saved” even though the submitted offset remained `-04:00`. The
canonical projection exposed that false-green. The live flow now verifies the
entered `+01:00` value before Save, then checks the full persisted time window
after Save and the source-extracted original after Undo. This is the first
evidence here for a correction through the native app transport, not a mock
mutation or a UI-only confirmation.

The changes are committed independently in the two child repositories:
backend 7c8da9dd4 and app 9164f9750. No branch was pushed or merged.

| Boundary | Exact verification | Result and limit |
| --- | --- | --- |
| Startup/network disclosure | First local backend startup attempt; final API process started with `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1` | The initial startup attempted a public Hugging Face model-host metadata lookup before offline mode was enabled. No user/account data, credentials, or app/artifact payload was sent. The final rehearsal backend was launched with both offline flags. This is a bounded disclosure about that startup path, not a claim that all local tooling or telemetry is network-silent. |
| Backend invariants | `env QA_ALLOW_DATABASE=vesper_artifact_correction_20261001a32cabd9d TEST_DATABASE_URL=postgresql://vesper:localdev@127.0.0.1:64743/vesper_artifact_correction_20261001a32cabd9d TEST_DATABASE_DISPOSABLE=1 PYTEST_ADDOPTS='-p no:cacheprovider' ./.venv/bin/python -m pytest tests/inbound/test_candidate_owner_lifecycle_postgres.py -q -k revisioned_time_corrections_apply_successively_and_dedupe_exact_retry -rs` | 1 passed / 2 deselected. Covers wrong-owner denial, exact idempotent retry, changed-payload and stale-revision conflicts, successive correction revisions, and unchanged original source bytes. Run against the explicitly disposable lane database. |
| Native Save/readback/source/Undo | `bash scripts/maestro/run-canonical-artifact-replacement-time-live.sh` with the lane API `http://127.0.0.1:64746`, Metro `http://192.168.1.153:64747`, and fixture `20261001finalb`; Vesper QA SE, iOS 18.2 | Passed. Maestro runs `2026-10-01_233524` (Save + cold reopen), `2026-10-01_233601` (exact original source reader), and `2026-10-01_233614` (Undo + cold reopen) all completed. The script verified persisted correction revision 6 with start `2026-10-07T18:00:00+01:00` and end `2026-10-07T20:00:00-04:00`; after Undo it verified revision 7 restored source-extracted start/end at `-04:00`. Exact original source bytes matched before Save, after Save, and after Undo. Debug output is retained at `/tmp/vesper-artifact-correction-20261001finalb`. |
| App-focused checks | `npx jest --runInBand --no-cache __tests__/utils/api/httpIntakeEndpoints.test.ts __tests__/data/intakeCorrectionSession.test.tsx __tests__/screens/canonical-artifact-reader.test.tsx __tests__/utils/api/http.test.ts`; `npm run typecheck`; `npm run lint -- --no-cache`; `npm run api-boundaries`; `npm run schema-bridge`; `npm run home-surface-budgets`; `npm run test:typecheck:contracts`; `npm run native-compatibility`; `npm run brand:icons:check`; Maestro flow guard test and runner `bash -n` | 4 suites / 135 tests passed. All listed checks passed; lint reported 0 errors / 167 existing warnings. The normal `verify:fast` lint invocation could not write Expo's ignored `.expo/cache/eslint` file in this sandbox (`EPERM`), so the same Expo lint command was rerun with `--no-cache`. |
| App changed-scope merge suite | `npm run verify:merge -- --base acf5bd837fe3725b00d9744727f513a601fb2498` | Passed after correcting the transport test to assert the account-session revision fence: 1,297 suites / 9,270 tests / 1 snapshot. This was the full-suite fallback because new Maestro YAML/scripts and shared API adapters are outside the narrow local-source selector. |
| Cross-repository and documentation checks | `make ci-static`; backend `scripts/merge_scope.py --base 0a1fdf224aaf59ca713eec5eba79a34321f038a9`; `make contract-check api-coverage-check compatibility-check card-arrival-check chat-card-types-check`; `make docs-links-check docs-spine-check docs-canon-check` | Backend static checks and selected offline suite passed (22,294 passed, 14 skipped, 1 xfailed, 52 xpassed); API projection/type parity and compatibility checks passed; docs checks passed (555 living Markdown files, 10 canonical entry points, 8 authorities within budget). The first composite `make verify-changed` attempt exited nonzero on the stale app expectation and Expo cache `EPERM`; after the test correction, the full app suite, app fast-gate subcommands, cross-contract checks, and docs checks passed. The backend checks had passed during the initial composite run; the composite command itself was not rerun end-to-end. |
| Auth and persistence boundary | Synthetic rehearsal fixture and local `SKIP_AUTH` backend | The device used the app's real local HTTP client and a disposable local PostgreSQL database, with a synthetic development owner. This establishes native local persistence and canonical readback, but not Clerk-authenticated user behavior, remote service acceptance, Android/physical-device, or VoiceOver behavior. |

Commit-hook boundary: app secret-prefix and untracked-import hooks passed.
Backend hooks passed with RUFF_CACHE_DIR=/private/tmp/vesper-artifact-foundation-ruff-cache;
the formatter's write-mode hook was skipped because the sandbox denied writes
to the checkout, after explicit ruff format --check and ruff check both passed
on the committed backend files. All other applicable backend hooks passed.

The previous app-native startup failure is treated separately from the
metadata disclosure: opening the embedded app and then replacing its JavaScript
runtime reproduced an iOS ExpoModulesJSI teardown crash. The current rehearsal
flows now cold-open the Expo development-client URL directly before deep-linking
to the reader. Initial attempts also used a stale Metro bundle or a synthetic
API actor that did not match the fixture owner; the fail-closed runner rejected
the actor mismatch before running a flow. The final run used the refreshed
lane-local bundle and matching API owner. The earlier crash's upstream
similarity is not treated as proof of root cause or of a general Expo defect.

### October 2 exact selected-source result receiving

The app's existing canonical artifact reader can now receive an exact
selected-source research result without owning or starting its producer. The
workspace activates only the authenticated owner-authorized GET in the mobile
operation projection. The app adds a typed transport, explicit work-ID route
parameters, a session/account-scoped query facade, and a concise inline result
card. The facade requires the expected viewer, `life` consumer, exact retained
`text/plain` original and revision, canonical source identity, source-span
digest, unexpired result, and valid addition/no-addition shape. A missing result
is an ordinary original-only state. Cache identity includes the account session,
viewer, work ID, source ID and revision; leaving the reader removes the query
cache. The native route stays internal-only and default-off. No GET, retry,
rerender, refetch or opening of the original can dispatch or repeat generation.
The producer POST remains dark and unallocated.

Validation and limits:

- Focused app tests passed: three suites, **129 tests**. Command from
  `travel-app/`: `npm test -- --runInBand --no-cache
  __tests__/data/selectedSourceResearch.test.tsx
  __tests__/screens/canonical-artifact-reader.test.tsx
  __tests__/utils/api/http.test.ts`. App typecheck passed. Targeted ESLint
  reported **0 errors and 7 warnings** (existing warning classes).
- API governance, generated projection/types, and compatibility checks passed:
  `make contract-check api-coverage-check compatibility-check`. The audit
  reported **592 active, 16 dark (0 unflagged), and 62 retiring operations**.
- The real-backend owner-read/denial lifecycle ran against the explicitly
  disposable database `artifact_result_reader_20261002`: **13 passed** across
  the authenticated exact-read and result lifecycle tests. The synthesis
  provider was mocked; no external provider was called.
- Registered native fixture flow
  `.maestro/polish/selected-source-result-reader.yaml` passed **1/1** on the
  dedicated iOS 18.2 `Vesper QA SE` simulator. It demonstrated both a synthetic
  addition and original-only fallback through the actual reader. This is local
  fixture evidence, not a live produced result, production authentication,
  Android/physical-device acceptance, or user-value evidence.
- The app implementation is committed on `codex/artifact-foundation` as
  `76cfc1443`. The workspace operation policy, generated projection,
  this receipt and the adaptive-context receipt are committed separately in
  the workspace repository; no backend implementation changed in this slice.

This closes only thin receiving integration for one existing reader. R2
candidate relevance, semantic support, model quality, matched comparative
usefulness, intent fit, remaining user effort, broader consumers and R0–R7
package acceptance remain open. The feature remains internal/default-off; this
receipt neither activates generation nor releases provider allocation.

## Historical planning and integration checkpoints — through October 2

The following text preserves the earlier introduction, scope and receipts.
Statements about “current”, “next”, open PRs or a frozen quality pilot describe
those checkpoints. A1 and the accepted program baseline supersede them; model
evaluation is deferred and these paragraphs do not activate another assignment.

**Current acceptance — October 2:** combined central app [PR #214](https://github.com/fy538/travel-app/pull/214) landed at `e715953796ff7c3b09b82444aa5d68f85f697f52` with required hosted checks passing. P3's exact-result transport, session-scoped reader and original-only fallback are accepted implementation; matching governance/projection/types accompany the workspace update. Presentation stays internal/default-off, reads never dispatch generation, and producer POST remains dark. Combined local preflight passed 9,289 app tests and 186 workspace tests. Native fixture evidence remains mock evidence. The frozen live-model/usefulness evaluation now has a configured local credential, but Anthropic token counting was rejected for insufficient credit; generated outputs and independent human judgments remain absent. Authenticated production use is not certified. Do not reimplement P3 or widen presentation. Earlier local-handoff receipts below are historical.

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

**Current continuation — October 2:** P1 native correction/readback has its
bounded local real-HTTP/disposable-Postgres receipt. Backend PR #243 and workspace
PR #48 are merged; app PR #214 has since landed as recorded in the current
acceptance above. The receipt uses synthetic data and SKIP_AUTH, so authenticated
production behavior remains open. Do not repeat the completed happy-path goal or
represent the app candidate as accepted main.

**P3 local implementation handoff — October 2:** app `76cfc1443` and workspace
`5c17d29a` implement the exact-result consumer described below. The owner lane
reports 129 focused app tests, 1,298 suites / 9,279 tests on the final broad
rerun, 176 workspace tooling tests, 13 disposable-Postgres owner-read/lifecycle
tests, and the registered native fixture flow passing 1/1. The original
aggregate preflight had an Expo cache-permission failure and a Jest worker
crash; focused lint, the crashed suite alone, and the full app rerun passed.
These carried receipts do not convert that failed aggregate into a pass.

Central preparation reconciles this handoff with the newer roadmaps and passes
the generated-contract, API-governance, compatibility and docs checks. The app
candidate was blocked by Security audit at this historical preparation checkpoint;
the current acceptance above records its approved, checked landing. The API
GET adoption and generated types are one coordinated candidate: the projection
cannot land against accepted app `acf5bd837` without its matching generated
schema. Keep the original-only fallback, internal/default-off presentation,
zero generation on reads, and separate dark/unallocated POST. This does not
establish live-model quality, authenticated production use or useful output.
Do not repeat completed local receiving work; central owns protected landing,
then the frozen quality/usefulness gates and their remaining access/human-review
requirements are the next substantive evidence.

**Implemented handoff scope — P3 exact-result consumer foundation:** adopt the existing
selected-source result read into the focused-reader data path, preserving
immediate original-only value. The backend GET exists, but the inspected app
has no selected-source result transport/data consumer and its generated mobile
schema does not expose that route. Both GET and producer POST are dark with no
declared consumers in `docs/governance/api-operation-policy.json`.

1. Implement read-only GET adoption through the operation-governance owner,
   mobile projection and generated types, typed transport and session-scoped
   data facade. Use `scripts/sync-types.sh` and `make api-coverage-check`; do not
   hand-copy backend models. Declare the actual gated consumer honestly while
   preserving the producer POST's disabled/unallocated status. Lifecycle labels
   must follow the governance checker; adoption is not feature activation.
2. Bind a supplied exact work ID to the expected original/revision and current
   account. Exercise addition, content-free no-addition, missing/expired result,
   revoked dependency, source revision change and account change. GET, rerender,
   retry and original opening must make zero producer POST/model calls. An old
   result cannot flash from a prior account cache or replace a different source.
3. Use controlled results through the real local result owner/API to connect
   the seam to the existing reader under its disabled feature boundary. A local
   fixture may provide the exact work ID for this proof. Production discovery
   of that ID and new generation controls are not invented to complete a demo.
   Preserve exact-original access and return context; use an existing compatible
   composition treatment or stop at the verified data seam if presentation
   requires a design decision.

**Completion and handoff:** a clean committed slice with generated contract
parity, meaningful data/transport tests, real owner-read/denial evidence and a
registered native receipt if visible reader behavior changes. Original-only
remains useful for no-addition and unavailable assistance. Controlled content
proves integration, not semantic support or model usefulness. Preserve P1
correction coverage; record PR #214 as a prerequisite wherever it is actually
needed. Central integration owns shared pins and protected landing.

**Longer-term continuation:** after that seam, reviewed useful outputs and
explicit spending admission can justify an explicit request-to-read experience.
Exact saved editions follow demonstrated useful additions and approved retention
semantics. Final Collection presentation, shared derivative retention, catalog
rights and automatic generation remain outside this unattended milestone.

**Local receiving handoff — October 2:** app `76cfc1443` and workspace
`5c17d29a` implement and locally verify the thin read-only result consumer.
They remain unmerged candidates; the app's required Security audit still
blocks acceptance. The API GET adoption and generated projection below
belong to this candidate, not the accepted main tuple. The original stays
available, presentation is internal/default-off, and reads never generate.
Central integration owns protected acceptance and the coordinated pin update.

**Historical implementation receipt — October 1 before central integration:**
the following checkpoint used the earlier September 30 merged baseline. Its
local/unmerged statements describe that date; section 2 now records the newer
accepted tuple. The `codex/artifact-foundation` lane has implemented the initial
submission-backed Thing owner, evidence-backed reversible cross-submission
aliases, an owner-scoped Thing read API, an app reader that opens original
Sources without transferring their permissions, and the first ordinary
candidate-to-bundle entry path. The owner-confirmed reconciliation transport
and app controls are now implemented and locally verified. Backend commit
`53d90e9eb` and app commit `38757f485`, like earlier lane commits `cb7defc86`,
`f1ae16096`, `eb515f055`, and `9a1c96292`, are local and not merged to remote
`main`. Workspace commit `549cf42a` records the earlier generated API
snapshot/projection and ownership boundary. The current operation policy,
OpenAPI snapshots, generated Current State and this roadmap now record the new
reconciliation contract in the independent workspace repository. The new entry preserves candidate/anchor occurrence
identity and opens a contribution bundle only for a verified private Keep with
a currently available, unexpired retained Source. This closes the bounded
candidate-to-bundle read path and the first explicit bundle-reconciliation
path. A first private consumer-Collection backend slice is now implemented in
the local artifact lane: canonical metadata, many-to-many kept-Thing references,
owner-scoped reads and revision-bound create/rename/add/remove/soft-delete
commands. The operations are now in the generated mobile projection and have
typed API, mock-parity, and session-scoped paginated data-facade coverage. The
backend now also serves a bounded, owner-authorized Collections root reading
through the Life projection contract; it returns Collection metadata and exact
owner total, not member Thing content. Collections are not yet consumed by the
native Life presentation or device-validated. Shared membership,
audience/receiving, automated filing and native collection management remain
open, along with broader P0/P1/PC/P2 acceptance. The root-read implementation
is committed locally as backend `3f67aa32c` and app `4532fd497`; neither commit
is merged or published. The detail continuation now pins to the first page's
Collection revision, holds a shared owner-row lock while reading each bounded
page, and returns a conflict for stale continuation. Backend commit
`ebe90232b` and app commit `43c4b3b51` implement this read-consistency seam;
neither is merged or published. The app now recovers from that exact stale-page
conflict by resetting the active account's detail query and loading page one
again; app commit `833a0bb38` adds the recovery. No stale offset is retried and
other 409 errors do not trigger this reset. These commits are local and not
merged or published. Most recently, backend commit `2e2ee4d6a` adds a bounded
owner-authorized Thing-projection batch (maximum 50) with set-based alias and
current-source authorization reads; app commit `eb14a00fa` switches
reconciliation to fetch its source and selected target together. This remains
read infrastructure: it returns original-source references, not user-facing
member labels or a finished Life composition. These commits are local and not
merged or published. Most recently, backend commit `10c5877d8` adds real
Postgres acceptance for simultaneous exact-command merge/reversal retries and
opposite-direction merge races; it changes tests only, not runtime behavior.
Most recently, app commit `b94a50ccf` adds a session-scoped, paginated Life
Collection member data composition: each revision-pinned membership page is
paired with one bounded batch of owner-authorized Thing projections. It
preserves membership order and identity and carries authorized original
references only; it does not invent member titles or build a Life detail
screen. App commit `de36dcd86` gives the dedicated synthetic replacement-time
fixture revision-bound in-memory mock correction/readback and Undo semantics
and registers a native Save/refetch/Undo scenario. App commit `51d275d11` is
the implementation revision used for the October 1 iOS 18.2 capture; evidence
commit `0a166e950` records the expanded four-flow verdict. The native run
proves the round-trip only against synthetic mock state, not backend
persistence, deployed authentication, or a live service. The mock-parity
checkpoint below is closed within that bounded scope; the next connected
checkpoint remains Technical's artifact-target request/result contract, which
is on a separate unmerged branch and is not available to this lane. Do not
consume it until it is landed and its contract verified. Exact commands and
evidence limits are in section 13.

Most recently, app commit `3c2bf4b71` aligned mock and live owner-Thing reads
with the same API-backed query path, added session/readback coverage, assigned
source ordinals from the visible bundle order, and registered the native
owner-confirmed reconciliation flow. Focused app checks passed before commit.
The current-revision five-flow capture is recorded in section 13; it is not yet
a fully accepted portfolio because the assigned `Vesper QA SE` screenshot for
the replacement-time keyboard state shows a focused field but no software
keyboard. Do not infer that missing state from the earlier iPhone SE capture.

| Area | Implemented and evidenced | Remaining boundary |
| --- | --- | --- |
| P0 contracts and portfolio | Accepted kept-thing identity direction; code-backed owner map, supported-door/mode crosswalk, versioned reading descriptor, family/fallback fixtures and sparse-history examples; initial Thing storage/migration design is implemented under P1 | Subject/Component and edition mappings, selected-part representation cases and broader lifecycle portfolio; fixtures are not live generation or desirability evidence |
| P1 correction and continuity | Revision-bound corrections and append-only Undo; backend typed-time replacement; native owner-only replacement-time editor with separate explicit start/end offsets and revision-bound Save/Undo; capture-to-reader and exact-source-to-confirmed-record links with source/digest checks; owner-scoped Thing row on verified private Keep; evidence-backed reversible cross-submission aliases; owner-scoped Thing API/native reader; candidate-to-bundle entry from a qualifying occurrence reader; owner-confirmed reversible reconciliation transport/app controls; Postgres coverage for concurrent merge/reversal retries and competing merge directions | Synthetic mock-mode Save/refetch/Undo has registered native iOS 18.2 evidence. The five-flow current-revision portfolio includes reconciliation capture, but its structured visual verdict is still pending. The current assigned-device keyboard screenshot does not show the software keyboard, so that assertion is not accepted from this portfolio. Authenticated app-to-backend persistence/readback remains open; raw UTC-offset entry and absent start/end place labels remain UX follow-ups; wider migration/rollback and lifecycle acceptance remain separate |
| P2 original-first readers | Ticket, source-backed place, text-built book/film/show/music, supplied passage and practical-record treatments; exact-original chooser/return; shared photo viewer | Catalog identity/art, selected-part UI and later dish/recipe/scorecard treatments; source facts do not establish attendance, author identity or payment state |
| Reader lifetime | Account-session-scoped reads, expiry-aware displayed facts and foreground refresh, exact-source authorization and revision checks | Full source/audience/collection lifecycle replay and authenticated mobile-to-service acceptance |
| Native acceptance | October 1 iOS 18.2 Vesper QA SE capture at app revision `3c2bf4b71`: 33 screenshots across five registered flows (14 standard reader/source/return, 10 largest-text, 4 replacement-time editor, 2 synthetic mock Save/Undo, 3 owner-confirmed reconciliation). The October 2 registered result-reader flow also passed on the dedicated simulator with synthetic addition and original-only fallback. | The October 1 portfolio's structured visual verdict remains pending; its keyboard screenshot shows focus without the expected software keyboard. The October 2 result-reader flow is fixture-only, not a live produced result. Full visual judgment, live authenticated save/refetch/Undo, reliable pinch/pan, actual VoiceOver traversal/actions, loading/error states, Android/physical devices and user preference remain open |
| Landed Technical dependencies | Exact-original revision binding and backend-only refinding of a bounded UTF-8 `text/plain` span; bounded public-acquisition primitives; exact-result GET now adopted in the existing Life/artifact reader through a default-off internal gate | Stable cross-representation Component identity, useful-addition acceptance and released research-spend allocation remain open |
| PC and later packages | House-design fallbacks and existing eligible original receiving remain usable; canonical private consumer-Collection owner, generated mobile contract/client, session-scoped paginated data facade with revision-bound continuation, bounded owner-backed Life Collections root API, batch owner-authorized Thing projection, and app-side Collection-page-to-Thing batch composition are implemented. The accepted Collections reading remains the product target. | Shared membership/audience/receiving, native Life Collections lens/detail route and device acceptance, founder-approved member labels/previews/hierarchy, approved catalog mappings/uses, exact kept editions and connected contextual additions remain unfinished |

Section 13 retains the exact revisions, commands and limits of each receipt.
Earlier simulator/build failures are historical attempts, not the current
status of the subsequently captured family and largest-text matrix. Direct
simulator double-tap has bounded fixture evidence; the automated gesture run's
unchanged screenshots did not establish pan/pinch. Do not turn either result
into a broader gesture, accessibility or live-service claim. The Home dock
stability repair was a QA prerequisite, not another artifact feature.

**P1 correction acceptance — completed October 1, with an explicit auth limit:**
the native app transport and disposable PostgreSQL rehearsal exercised Save →
canonical readback → Undo → canonical readback, including persisted state and
unchanged submitted original. It used a synthetic development owner and local
`SKIP_AUTH`; it does not prove Clerk-authenticated behavior or remote-service
acceptance. The exact commands and limits remain in section 13. Do not repeat
the local rehearsal; a real-auth run is a separate acceptance target.

**P3 receiving checkpoint — completed October 2:** the exact selected-source
result GET is connected to the existing focused artifact reader behind a
default-off internal presentation flag. The reader uses the explicit work ID,
exact original/revision, current viewer/account and `life` consumer; addition
and no-addition preserve original access. Reads, retries, rerenders and opening
the original never invoke generation. The POST producer remains dark and has
no released allocation. This is receiving integration, not relevance, model
quality, comparative usefulness or product-value acceptance; see section 13.

The next substantive gate is evidence of result quality and usefulness using
the existing frozen evaluation proposal and independent human review. Keep
producer dispatch disabled; representative output collection and any paid call
remain separately gated. Final Collection presentation and wider reader design
remain independent work.

After this bounded slice, preserve section 11's P3 quality checkpoint: evaluate
the landed exact-Source request/result under its existing authority, evidence
and spend gates, with original-only value and exact return. Inspect the landed exact Source-based
scope and quality/spend gates before consumer adoption. The bounded Life/Collection
data composition is now implemented in the app data facade: it reads canonical
Collection membership at its pinned revision and resolves each page through
one current owner-authorized Thing batch, preserving the exact
membership/Thing association without copying Source content or claims. Do not
add member labels, previews, hierarchy or a native detail route until the
founder-approved display contract exists; the current design reference is
legacy Threads evidence and does not certify that composition. Keep Strategy
as the Collection owner and Life as presentation/projection owner. The first
read-side gate is implemented: root and corpus lenses are separate contracts, and the
Collections root index reads only the authenticated owner's bounded canonical
Collection name/count summaries plus exact total in one owner query. Collection
rows carry the canonical owner reference and do not fabricate Source lineage.
The `consumer_collection` path still has no native detail route; no Collections
tab or row is exposed in the app. Its bounded detail reader now carries the
first page's Collection revision into continuation requests, reads each page
under a shared owner-row lock, and rejects stale continuations with a conflict
that the app handles by restarting at page one. The new composition is a data
contract, not a user-facing member display or approval of final screen
hierarchy.
Owner-confirmed reconciliation
is implemented and reversible; it does not claim semantic sameness. Collection
continuity, native
acceptance, timezone-authoring for typed-time replacement, and wider
P0/P1/PC/P2 outcomes remain open. Do not build a second research engine; adopt
Technical's landed interface and first-producer safeguards.

The accepted
[Collections](../decisions/2026-09-28-collections-are-the-spine.md) and
[Life](../decisions/2026-09-29-life-model-occasions-collections-and-sharing.md)
decisions settle many-to-many membership, time-agnostic things, Remove versus
Delete, whole-collection sharing and Life's four readings. The
[September 30 kept-thing identity decision](../decisions/2026-09-30-kept-thing-identity.md)
now settles the narrow consumer identity boundary without reopening those
product semantics. It does not claim an implemented migration or adopt broader
retention, sharing or catalog policy.
Door-to-family recognition and sender-visible unsupported-email rejection
remain separate capture acceptance work owned by Orchestration.

This roadmap owns Strategy's package sequence and receipts. The program owns
cross-lane boundaries, not a permission queue for ordinary implementation. The
earlier [strategy handoff](roadmap-proposals-for-codex-2026-09-28.md#9-focused-artifact-engineering-proposals)
is proposal provenance. Capture transport, signing and Home/Places delivery
remain with Orchestration; shared context/research/runtime work remains with
Strategy Technical.

**In brief.**

- **What to build first:** the thing's identity (P1), catalog anchoring (PC)
  and native readers (P2), for the families already designed: tickets,
  venues, and books, films, shows and music.
- **What comes later:** discovery of additions (P3), exact kept editions (P4)
  and selective refresh (P5). P3 starts thin; saved editions and broader archive
  maintenance wait until additions have shown people value, except that any
  adopted retention trigger requires P4's minimum exact-snapshot support when
  that behavior first ships. Original-record correction belongs in P1;
  permission, publication and spending safeguards accompany the first live
  discovery, not a later hardening phase.
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
- **Provider approval is use-specific:** which catalog sources to license and
  which display, storage, inference/indexing, sharing and retained-edition uses
  they permit (section 6). Unapproved uses stay gated, not the original reader.


### Historical section 0 assignment — completed P3 foundation

**Current assignment:** the October 2 read-only P3 result-consumer milestone
is implemented and locally evidenced in the handoff above. Preserve P1 and P3
app candidates while central integration resolves the shared security blocker
and verifies the coordinated contract. Do not repeat their completed local
rehearsals or claim accepted-main adoption. After landing, continue the stated
quality and usefulness gates using the frozen evaluation proposal. The approved
finite provider pilot still requires credentials and later independent human
review. Production allocation, automatic generation, broader P0/P1/PC/P2/P6
work and unresolved design decisions keep their separate gates.

The October 1 batch-read increment now resolves up to 50 owner-authorized
Thing projections in bounded set-based reads, and reconciliation requests its
source and selected target together. This removes per-Thing network reads for
that flow and provides a reusable member-read primitive; it does not yet return
user-facing member titles or summaries. App commit `b94a50ccf` now composes
each revision-pinned Collection page with one such batch and preserves member
order and identity without an N+1 pattern. This closes the read-side
data-composition gate, but does not decide labels, summaries, previews or final
Life member presentation. The founder-approved member-display contract
remains a prerequisite to exposing a Collection detail experience.
