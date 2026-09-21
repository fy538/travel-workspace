---
doc_type: working
status: active
owner: founder / Strategy task
created: 2026-09-07
last_verified: 2026-09-21
expires: 2026-10-07
why_new: Extracts the present-tense cross-lane program map from a long Integration plan and its historical receipts so independent owners can coordinate without competing execution queues.
supersedes:
  - cross-lane priorities and lane allocation in complete-system-integration-roadmap-2026-09-05.md section 2
source_of_truth_for:
  - cross-lane program priorities and accountable assignments
  - cross-lane dependency routing and system reassessment
depends_on:
  - ../decisions/2026-09-06-reconcile-consumer-strategy.md
  - ../systems/four-root-loop-object-surface.md
  - ../systems/contribution-and-consequence.md
  - complete-system-integration-roadmap-2026-09-05.md
---

# Vesper program roadmap

**September 21 current posture:** the received-material, practical-route,
Content consumer/hydration and temporal-map packages have verified isolated
results at the boundaries recorded below. The latest Content and Places turns
are complete, not waiting for a design canvas. Meaning-based discovery,
bounded exact-original social receiving, and a feature-flagged recipient-consented
Home/Places social read now have committed isolated implementations and focused
verification below. This is not whole-roadmap or
native acceptance: broader semantic/time retrieval, supply activation,
Social/Life adoption and combined delivery remain unfinished. The proposed
cross-run editorial reuse policy has been presented to the founder and is
not yet approved. Integration remains **PAUSED by the founder**; no shared
runtime, landing, publishing or pending product agreement is activated.
Earlier dispatch and review entries below preserve the execution history.
Section 7 preserves the older acceptance scope as history.

## September 21 functional implementation receipt — consented Places social read

The next bounded social seam is now implemented in the same isolated lane. The
existing Places `From your people` section can consume recipient-consented
`place_pull` handoffs without introducing a feed, social post store, or new
audience model:

- **Authority:** the relationship repository now exposes a strict readable
  place-pull reader that rechecks the active pair room, relationship record,
  recipient grant, expiry/status and linked Source custody before any Places
  projection sees the handoff. Place-pull is deliberately not a chat send and
  therefore does not require a `message_id` receipt.
- **Scope:** Places resolves the current editorial subtree first, maps accepted
  graph identities to canonical venue owners, and keeps only venue-bound notes
  inside that visible scope. `Anywhere`/`Saved` contexts without a proven
  editorial subtree remain empty rather than leaking a global recipient queue.
- **Presentation:** the existing friend row carries the sender, exact note,
  canonical venue name and venue id, so the mobile renderer can open the
  existing venue destination. It is dark behind the existing
  `PLACE_HANDOFF_PULL_ENABLED` flag; no new UI or generated schema is required.

Evidence: Places suite **710 passed, 3 skipped** (seven pre-existing leak
warnings); the combined social/relationship/root packet **61 passed**; the
relationship Postgres persistence packet **4 passed**; Ruff, format, compile
and diff checks passed. The feature remains candidate-level: flag activation,
populated accepted handoffs, native capture, merge/publication and rollout are
unverified. This slice deliberately supports only venue-bound recipient pulls;
broader casual media, group audiences, person ranking, and Life adoption remain
separate decisions. A follow-up backend fix in `travel-agent` commit
`76e0ea9e2` removes the accidental chat-receipt filter and adds a Postgres
regression assertion for a pull with no message row. The workspace receipt is
still candidate-only and must not be read as flag activation or publication.

## September 21 runtime supply probe — consented Places social read

The newly adopted social seam was exercised end to end against the isolated
lane database and API, rather than only through patched producer tests. The
probe created a disposable sender, active pair circle and personal room,
recipient-owned pull grant, accepted graph→venue binding, venue under the
resolved New York Home subtree, and a venue-bound `place_pull` handoff. It then
read the real `/api/places/feed?context_handle=home` response with the existing
flag enabled locally. The exact note, sender, venue identity and handoff id
were present in the existing `From your people` section; the direct owner
reader returned one eligible handoff. Every temporary user, relationship,
graph, venue and Home-location row was removed in `finally`.

Evidence: `DIRECT_READABLE_COUNT 1`, `PLACES_FEED_STATUS 200`,
`PLACES_FEED_NOTE_SEEN True`, `PLACES_FEED_SENDER_SEEN True`,
`PLACES_FEED_VENUE_SEEN True`, `PLACES_FEED_HANDOFF_ID_SEEN True`, with one
`friend_activity` section. This proves the local persistence→owner read→Places
feed boundary for a venue-bound pull. It does not prove native visual behavior,
production flag activation, broader media/group sharing, Life adoption, or
publication. The manual API was stopped after the probe; no provider or
background loop was enabled.

## September 21 functional implementation receipt — Home social receiving

Home now consumes the same recipient-consented, venue-bound `place_pull`
records through its existing addressed Place-note adapter when
`PLACE_HANDOFF_PULL_ENABLED` is enabled. It does not add a Home-specific social
store, ranking path, or copy transformation: the relationship owner remains
responsible for pair/grant/expiry/custody checks, and Home preserves the
sender's note, exact venue identity and existing Places destination. The flag
keeps the new read dark by default.

Evidence: the focused Home/Places/relationship packet passed **48 tests**, and
the real disposable runtime returned HTTP 200 from
`/api/root-projections/v2/home?timezone=UTC` with the exact pull note, sender,
venue and handoff id present. Temporary users, relationship rows, graph
identity, venue and Home context were cleaned up. No mobile schema change was
needed because the existing Home destination contract already handles the
typed Place door. This remains local candidate evidence: native capture,
production activation, broader group/media sharing, Life adoption and
publication remain open.

## September 21 runtime supply probe — Life original refinding

The exact-original continuity boundary now also has a real HTTP receipt. A
temporary retained, confirmed Intake source owned by the lane's default user
was inserted with a valid custody receipt and one-hour retention. The running
API answered `POST /api/life/originals/refind` with HTTP 200 and returned one
metadata match containing the exact source identity for the query. The
submission and source rows were removed immediately after the request.

Evidence: `LIFE_ORIGINAL_STATUS 200`, `LIFE_ORIGINAL_MARKER_SEEN True`,
`LIFE_ORIGINAL_SOURCE_ID_SEEN True`, `LIFE_ORIGINAL_ENTRY_COUNT 1`, followed
by `LIFE_ORIGINAL_CLEANUP_DONE True`. The relationship original-delivery
Postgres packet also passes **3 tests**. This proves owner-authorized metadata
refinding and its typed Life destination, not full Life corpus organization,
native original rendering/return, or indexed serving adoption.

## September 21 runtime continuation — Life organized record and group

The organized Life read now has a real API receipt in addition to its offline
route and Postgres projector coverage. A temporary canonical retained-source
submission was admitted through `create_submission`, promoted to confirmed
`source_and_derived` custody, and propagated through the existing Life outbox
projector. With the local API running against the disposable lane database,
`GET /api/root-projections/v1/life?lens=time` returned the exact retained
record, its owner/source refs and the typed Intake destination; the paired
`GET /api/root-projections/v1/life/organization/groups?lens=time&limit=10`
returned the current September period group with matching revisions. The
submission, source, corpus, organization and temporary user rows were removed
after the read.

Evidence: both routes returned **HTTP 200**; the Life root carried one
`source_submission` entry with `source.<submission_id>` identity and the group
page carried `derived:period:2026-09:iana.utc`, `content_revision=2`; API
background loops were disabled and no provider was used. This proves
persistence → Life owner projector → organized API read for one retained
record. It does not prove full multi-lens corpus coverage, indexed serving
adoption, native visual capture, original-byte return or rollout activation.

## September 21 runtime supply probe — child-owned public Source

The promised persistence boundary was exercised against the isolated lane's
disposable Postgres, not only mocks. A temporary accepted, grounded public
Source owned by a canonical venue under Place `1` was inserted with its active
observation and consequence-policy binding. The real owner readers returned it
both by exact `venue` identity and through the bounded parent→child Place read;
the Source adapter then revalidated it at the current represented clock and
returned the exact immutable handoff. The temporary venue, primitive,
observation and lifecycle rows were removed in the same probe.

Evidence: `CHILD_SOURCE_RUNTIME_OK venue_id=22 exact=1 scoped=1 sources=1
handoff_entity=venue:22`, using the lane database on port `61460`. This proves
the persistence/owner-reader seam only. It does **not** prove populated Home
composition, Places native rendering, feature-flag activation, merge or
publication; the public consumer remains candidate-level until those boundaries
are exercised with an approved dataset. The next useful package is therefore a
small populated Home/Places composition check or the next supported receiving
gap, not another rewrite of the Source contract.

## September 21 populated composition probe — Home to exact entity destination

The next boundary was exercised through the actual lane API with a temporary
Home context. A disposable user was given an authoritative New York Home
coordinate, and a temporary accepted, grounded public primitive was attached to
a venue beneath Place `1`. With the existing primitive-read and Places detail
control-plane flags enabled **only for this local probe**:

- `GET /api/root-projections/v2/home?timezone=UTC` returned **200** and the
  serialized response contained the exact Source revision, venue identity and
  claim from the temporary record.
- The existing exact destination,
  `GET /api/me/entities/venue/{id}/presentation-v2` with the Source id and
  revision, returned **200**, `reading_selection_state=available`, and the
  Source-backed claim/body.
- The temporary Home location, venue, primitive, policy binding, observation and
  lifecycle rows were removed after the request. No production flag or dataset
  was changed.

The matching mobile destination/return packet is also green: **87 Jest tests**
across Home root rendering, root-projection navigation, Places home receiving
and entity-route construction, with TypeScript `tsc --noEmit` passing. These
are focused contract and renderer checks; no simulator capture or native
visual verdict is implied.

This proves the populated Home → exact entity destination/reader boundary, not
native rendering, a production rollout, or an independent child-Source card in
the Places collection. The latter remains intentionally scoped to exact Place
owners by the current collection contract. The next work should consume this
destination on the mobile surface or close another supported receiving gap;
there is no evidence for widening the Source model.

## September 20 functional implementation receipt — Life continuity slice

The first execution slice under the functional-implementation goal is complete
in the isolated coordinated lane `codex/functional-implementation-2026-09-20`.
It integrates the already-reviewed Life/original continuity branch across the
three repositories without changing the four-root rollout gate:

- **Backend:** exact retained-original refinding by metadata, one-recipient
  original delivery with sender readback/withdrawal, custody/authority checks,
  and bounded practical visit judgment. Migrations, owner repositories and
  route contracts are included.
- **Mobile:** Life Find and exact original readers, sender controls, Home
  original/practical receiving, account/expiry handling and exact return
  routing. The sender-screen test harness now supplies its required user
  context; no runtime behavior was weakened.
- **Workspace contract:** the Life refinding and original-delivery operations
  are registered in the API policy and generated snapshots. Projection matches
  under a temporary policy containing only the pre-existing expired-route
  review-date repair; the expired-policy backlog itself remains unresolved and
  is not hidden by this receipt.

Evidence on the lane: backend focused Life/original/practical **170 passed**;
backend root/Life regression **715 passed, 43 deselected**; mobile focused
continuity/original/Home **78 passed**; broader Home/Places/Life/original
coverage **332 passed**; TypeScript and Python compilation passed. This is a
committed candidate, not a merge, publication, production activation or native
visual acceptance. Next execution should consume this candidate through the
combined receiving/runtime check, then take the next highest-value Home/Places
receiving gap rather than reopening the completed Life slice.

## September 20 functional implementation receipt — Home/Places and practical depth

The second execution slice is complete in the same isolated lane. It adopts only
the bounded commits from the existing native-receiving work; the much larger
candidate branch remains unmerged. The slice now carries a real result through
the Home/Places destinations and one supported practical/social action:

- **Places:** purpose and visit context survive root → search/reading → entity
  depth; retained readings have explicit lifecycle/owner gates, exact-selection
  navigation, expiry behavior and fail-closed handling. Practical visit checks
  preserve the evidence-backed origin and current-purpose boundary.
- **Home and plans:** exact Places visits lead with value, and a private stop
  question can receive a bounded answer or send a reviewed human message into
  an eligible existing room. The assistance routes now expose explicit trip
  membership checks before service work and their content contract has a named
  enforcement site.
- **Mobile receiving:** practical checks, retained-reading destinations,
  graph/context doors, exact return state and native receiving controls are
  connected without changing Chat or the four-root rollout gate. Life row
  wrappers now use the shared row primitives rather than creating a new shell.

Evidence on the lane: backend focused Places/root/practical/plan/Life coverage
**1,208 passed, 43 deselected**; mobile focused Home/Places/Life/plan receiving
**462 passed**; mobile typecheck passed; package auth and content-contract
regressions **23 passed**. A full offline backend sweep reached **21,526 passed**
before the package repairs; after those repairs, the only remaining full-sweep
compatibility failure is the pre-existing expired-deadline check for two legacy
AI bridges. The standard API audit still reports the pre-existing 55 expired
policy review dates plus one unrelated missing-consumer entry for the intake
media read. Native device acceptance, disposable-Postgres execution,
merge/publication and rollout activation remain unproven.

The implementation commits are backend `5dd8e6938` and mobile `9fee2d46c`, in
the isolated branch `codex/functional-implementation-2026-09-20`. The next
package is the combined receiving/runtime check followed by the next uncovered
Home or Places supply gap; do not merge the broad 181/204-commit candidate
wholesale.

## September 20 functional implementation receipt — Life organized records

The third execution slice completes the missing organization layer of Life. The
backend now serves owner-backed, bounded group reads with eligibility binding,
pagination metadata and focus-safe refresh. The mobile Life record can open
the organized groups surface for its time/places/people/threads lenses, preserve
exact destinations and return context, and refresh without turning a stale
cursor into an implicit new record. The matching OpenAPI snapshot and generated
mobile types are committed.

Evidence on the lane: backend Life/root projection package **731 passed, 48
deselected**; mobile organized-record/refinding/row package **49 passed**;
mobile typecheck passed; the row ratchet remains green. This is still offline
and candidate-level evidence: the disposable-Postgres organization test is
present but not executed here, native visual acceptance and rollout activation
remain unproven.

The implementation commits are backend `7471c597c` (with `c73732aa8` and
`aceba2193`) and mobile `19c53b42a` (with `8c5efbe32`, `d7c8ba697` and
`c253e15bb`), with contract refresh `34e2c1b`. The next execution should run
the combined receiving/runtime check across all three slices, then return to the
highest-value uncovered Home/Places supply or social receiving gap.

## September 20 functional implementation receipt — cold-world Home opening

The fourth execution slice closes a different Home gap: a genuinely cold user
with only world-facing Places context can receive one substantive invitation,
rather than a flat empty-state report or an input request. The projection now
keeps owner-backed material distinct from contextual world supply, preserves the
cold posture when no owned history exists, and promotes at most one admitted
world-opening passage into the existing `NOW` invitation contract. It does not
invent history, generate content on read, add a provider, or turn a context-only
source into personal evidence; the existing source, provenance, destination and
why-this payload remain intact.

Evidence on the lane: backend Home portfolio/composition **40 passed**;
mobile Home root **30 passed**; mobile typecheck passed. The implementation is
backend `40e90210f` in `codex/functional-implementation-2026-09-20`. This is a
candidate-level, render-independent result: native visual acceptance, combined
runtime delivery, disposable-Postgres execution, merge/publication and rollout
activation remain unproven. The next execution should exercise the combined
receiving/runtime path across the Life, Home/Places and cold-world slices, then
take the next uncovered Home/Places supply or social receiving gap. The standard
API audit remains bounded by the pre-existing 55 expired policy dates and one
unrelated intake-media missing-consumer finding.

## September 20 combined receiving/runtime rehearsal

The four slices were exercised together through the existing offline owner and
consumer boundaries after the Plan Assistance auth repair. Backend Home/Places,
practical assistance, original receiving, root composition and Life organization
tests passed **152/152**. The corresponding mobile Home, Places, Plan Assistance,
original receiving, Life organization/refinding and return suites passed
**407/407** with `TZ=UTC`, the explicit boundary used by the arrangement-time
fixtures. A default New York shell exposes one pre-existing timezone-sensitive
expectation in the object-page projection; it is not a functional failure of
these slices, but native/device timezone acceptance remains open.

The repair is backend `9e8214eb5` and is test-only: offline response-mode tests
stub the new DB-backed membership boundary while a separate denial test proves
membership is checked before assistance context. This rehearsal still does not
prove a disposable-Postgres run, populated provider supply, native visual
quality, merge/publication or rollout activation. The next build target is a
real Home/Places supply or social-receiving seam, selected from an existing owner
contract rather than a new generator or store.

The broader backend offline sweep then reached **21,546 passed, 14 skipped and
53 xpassed**, with one failure in the pre-existing expired AI-compatibility
registry for `concierge_home_card_metadata` and `sse_tool_calls_made`. That
failure is unchanged from the baseline and is not hidden by this receipt; the
full API audit and expiry cleanup remain separate work.

## Current round — meaning-based discovery and exact-original receiving

**Authorized September 9 following the lexical increment:** complete two
consumer capabilities with local Luna xhigh subagents, keeping Strategy focused
on architecture/authority and review. The bounded
[one-recipient original-display rule](../decisions/2026-09-09-exact-original-recipient-display.md)
is adopted; broader AI use, audience and general-share decisions are not.

- **Discovery — implemented locally:** Content lane `65193c1` / `a49068dad` /
  `dfe84b3c4`; connects the existing derived semantic index through actual Places search
  and exact reading destinations. Rehydrate candidates from current owners;
  preserve geographic scope, source/revision, rights, surface/release admission,
  independent catalog results and bounded lexical fallback. No new supply,
  generated-on-read content, provider spend or serving activation. Future-event
  applicability remains separate from freshness. Compare paraphrase retrieval
  against the lexical baseline with geography controlled; fake vectors do not
  establish semantic quality.
- **Original receiving — implemented locally:**
  received-value lane `c4a4296` / `de76cf417` /
  `930ecee68`; exact selected-source Send, sender readback/control, currently
  authorized recipient original, Home entry/return and lifecycle repair. Follow
  Social §10.4 and the adopted contract. No invented Place for non-spatial
  material, generalized social owner by accident, new AI-use grant or Chat/Life
  redesign. The implemented scope is retained plain text and JPEG/PNG/GIF/WebP
  originals, one existing eligible account per send, not the whole Social roadmap.
- **Orchestration:** a second local spawn was refused by the session's retained
  agent limit. The existing Luna xhigh worker completed discovery, then
  original receiving; Strategy handled the contract, independent review and
  regression follow-ups in parallel. No second session or model substitution was dispatched. Local
  implementation, focused verification and explicit commits are authorized;
  Integration, landing, publishing and activation remain paused/separate.

Each assignment owns diagnosis through implementation, self-review, tests and
coherent commits. Checkpoints are the first substantial architecture boundary,
a consequential blocker, and final verified handback—not routine step approvals.
These two bounded implementations are complete locally; broader execution scope
and whole-product acceptance are not complete.

**Discovery architecture checkpoint:** keep embedding/vector lookup in the
existing vector owner, and its optional execution/budget in Places. The
provider-free lived-experience reader owns authoritative candidate admission
and ranking, not model/network invocation. Reuse the configured embedding and
collection contract behind a separate default-off serving gate; do not invent
a local-only runtime. Preserve the total 350 ms optional-reading envelope,
finished lexical results and catalog independence, with bounded physical work
and no database connection held across provider work. The committed implementation
incorporates this reorganization. Tests use fake providers;
no production provider or collection is activated by implementation.

**Discovery completion:** backend `6c808727c` adds the contract-aware vector
adapter, bounded optional Places execution and provider-free exact-version
rehydration. A separate default-off gate protects serving. Lexical reads retain
their full 350 ms budget; semantic work uses only remaining time, capped at
120 ms, with isolated bounded physical work so timeout/cancellation does not
accumulate an unbounded queue or starve catalog/lexical work. Current owner
membership, accepted version, rights, evidence, lifecycle and release checks
remain authoritative. The bounded global vector shortlist is post-filtered by
requested place: it can miss eligible local matches below that shortlist.
Complete geographic recall needs reviewed place-filter metadata and a fresh
derived build; neither semantic quality nor event-time applicability is claimed.

Review follow-up `a49068dad` preserves lexical fallback for provider HTTP
status failures as well as transport failures; 401/429/503 regressions failed
before the fix and passed afterward. Strategy independently verified the clean
`65193c1` / `a49068dad` / `dfe84b3c4` tuple: 139 offline tests passed in
4.928s and one disposable PostgreSQL search/receiving regression passed in
4.305s. Measured commands,
revisions and outputs are in
`/tmp/vesper-semantic-discovery-20260909/semantic-discovery-hardened-final-20260910T023646Z.log`
and `semantic-discovery-db-hardened-final-20260910T023648Z.log` in that directory.
The DB test uses fake vector hits; no live-provider quality, native acceptance,
full `make verify`, combined delivery or activation is established.

**Original receiving architecture decision:** the existing `PlaceHandoff`
requires a Place and conversation; keep that specialization intact. A narrow
one-recipient exact-original delivery component and companion operation belong
to the existing Relationships owner, with Source/Intake retaining custody.
This implements the adopted display rule for spatial and non-spatial originals;
it does not adopt a general sharing owner, broader audience, AI permission or
independent recipient copy. Existing current account/relationship eligibility
must hold; do not invent a Place, connection or conversation to satisfy it.
The worker reported this schema boundary before implementation and Strategy
approved the bounded owner-preserving extension. Any genuinely new eligibility
policy remains a founder decision. Caption is optional; receiving/return is
complete without Ask, Keep, reply or sender-visible consumption metrics.

**Original receiving completion — September 10:** clean coordinated candidate
`c4a4296` / `de76cf417` / `930ecee68` (workspace/backend/app). Relationships
owns a narrow delivery repository and a shared eligibility-policy module;
Source/Intake owns exact custody, supported original roles, MIME, size and
revision validation. Reads enforce current grant/source/linked-pair access and
effective expiry, including reauthorization after a private download. Dismissal
is not withdrawal. Recipient status/expiry filtering precedes the list limit.
The real Home v2 server portfolio supplies the typed unit without displacing
urgent work; mobile supplies a bounded 280-character preview, original depth
reader/root return, account/expiry handling, sender history, retry reconciliation
and withdrawal. Sender and read hooks preserve the existing default-off gate.

Strategy independently ran **120 offline backend tests** (5.611s), **two real
PostgreSQL scenarios** (6.091s, isolated disposable port 55566), and **55 mobile
tests across seven suites** (2.959s), all passing with zero skips. The original
broader mobile run found a stale renderer-registry assertion; `930ecee68`
corrects it and adds mounted denial coverage with previously cached text.
Measured commands, revisions and results are under
`/tmp/vesper-social-original-20260909/`: `social-original-final-offline-20260910T043237Z.log`,
`social-original-final-postgres-20260910T043258Z.log`, and
`social-original-final-mobile-hardened-20260910T043517Z.log`. Backend tests run
with the existing Python 3.13 environment, not the measurement wrapper's 3.14.
Backend commit hooks passed; the independent size check passed. Offline export
from actual backend code, generated-contract sync/typecheck, API boundaries,
schema bridge, Home surface budgets and API coverage passed (574 active,
15 dark/zero unflagged, 62 retiring). Default export initially used an environment
without FastAPI; selecting the installed Python 3.13 environment resolved that
tooling failure without changing the exporter or weakening a check.

**Remaining boundaries:** these are lane commits, not merged or serving. Full
`make verify`, ASGI authentication acceptance, native/visual acceptance and live
semantic-provider quality remain unrun. Mocked route functions and mounted React
tests are not native/HTTP evidence; the React tests still emit act warnings.
Mobile global size/query-key checks retain inherited violations; the new API
family is extracted rather than added inline to the oversized implementations.
Original lists remain bounded (including the sender's latest 50 sends); do not
promise exhaustive history or complete source/pair-filtered recall. Broader
recipient refinding, guests, Reply/Ask and onward/AI-use rights are not delivered
by this package. Integration, merge/push, provider activation and deployment
remain paused or separately authorized.

## Previous round — contextual discovery and exact human receiving

**Authorized September 9 after the six-finding repair:** use local Luna xhigh
subagents under Strategy rather than dispatching separate execution chats.
Integration stays paused. This is implementation plus one bounded authority
investigation, not supply activation, a new design sprint, or a global merge.

- **Contextual discovery — implementation:** continue in the clean Content
  coordinated lane, workspace `65193c1`, backend `26c2d6244`, app `dfe84b3c4`.
  Trace the current question/context path and implement a bounded improvement
  through actual Places retained-reading search and its existing destination.
  Preserve current flags, exact source/revision, geographic scope, consequence
  and release admission, independent catalog results and optional-read budgets.
  Do not describe lexical improvements as semantic understanding or use source
  freshness as event applicability. The non-runtime semantic index, external
  acquisition, generated-on-read content and new serving activation stay gated.
  Finish independent supported work and name precise remaining dependencies.
- **Exact human-original receiving — read-only investigation:** inspect current
  Relationship grants, source custody, recipient reads and mobile entry/return
  against the existing Social plan. Establish whether an exact selected original
  is already authorized, and which source-to-share binding or permission decision
  is actually missing. No new audience, media exposure, AI-use permission, source
  retention or Chat/Life redesign follows from this investigation.
- **Strategy:** owns the canonical roadmap, architecture review and final
  verification. Agents own explicit files and lane-local commits; no overlapping
  writer, automatic sibling merge or shared-runtime restart is authorized.

The first Luna worker started successfully; a second spawn and an old-worker
resume were rejected by the session's agent limit. The available worker is
assigned the implementation after its short initial social read; Strategy
completes social investigation concurrently. This is one worker plus the parent,
not a claim of two concurrent Luna execution agents. Existing completed workers
are not reconfigured silently. Report one substantive boundary proposal, genuine
authority/dependency changes and the verified handback—not each ordinary step.

### Current-round completion — bounded search improvement, not full C4b

Content backend `5ffded6c5` completes the first contextual-discovery increment
at clean workspace `65193c1` and unchanged app `dfe84b3c4`. Actual Places
retained-reading search now normalizes supported Latin case/diacritics, scores
query-term presence once per authored field, and rewards contiguous normalized
query phrases without dropping short words or repeated query tokens. Verbose
repetition cannot inflate a field's score. Existing owner identities, anchor
coverage, admission and optional-read budgets remain in force; no API or mobile
contract changed. This is lexical ranking, not semantic understanding,
translation, future-event applicability, or activation of the derived index.

Strategy independently reran 112 backend tests at that clean tuple in 4.295s,
plus Ruff and revision diff checks. The tests cover the retained reader, actual
Places search consumer, source contracts, Home portfolio and entity presentation.
Search context/catalog and per-place selections are stubbed in the new consumer
regressions; this is not a database-to-native or consumer-quality acceptance
claim. The measured command and output are recorded in
`/tmp/vesper-contextual-discovery-20260909/contextual-discovery-final-20260910T012522Z.log`.
Full `make verify`, native, provider and combined-lane checks were not run.

The parallel social investigation is recorded in the
[Social roadmap, section 10.4](social-experience-implementation-roadmap-2026-09-07.md).
Existing recipient display intent does not yet establish an exact selected
source/object binding and current original-byte authorization. The proposed
extension binds that selection to the existing handoff and delegates reads to
the custody owner; it does not broaden audiences, imply AI-use permission, or
backfill ambiguous historical shares. Its 54 passing baseline contract tests
do not prove a new recipient-media path. This remains an explicit decision and
implementation boundary, not an activated capability.

Both outcomes are local. Integration stays paused; no landing, publishing,
provider work, Chat/Life redesign or product-policy change occurred. Broader
semantic/event-time retrieval and social-original receiving remain separately
scoped follow-on work, not hidden completion claims for this package.

### Completed search package and repair history

**Earlier consumer package — September 9: retained readings in Places search.**
The C4b audit found that the actual authenticated Places search response carries
catalog rows, while the retained-content reader has no corresponding typed
search-result destination. This is an implementation gap, not a reason to
reopen the existing Places direction: the four-root contract permits spatially
anchored Sources/compositions, and the Places handoff's exploration contract
already includes explanations, reading destinations and search continuation.
Content owns an isolated cross-repository package connecting eligible retained
readings to that actual search route and the existing mobile Source/detail
destination, preserving catalog search and context on return. Reuse current
renderers; do not settle new visual composition or create another detail system.

Use the existing bounded structured/lexical owner reader and current public,
review, evidence, rights, freshness and release gates. Preserve their default
posture: this assignment does not activate supply or semantic serving. The
response must distinguish a reading from a catalog entity, carry exact owner
identity/revision, and support an honest empty or independently failed reading
branch without losing valid catalog results. Verify real route-to-owner reads,
correction/withdrawal exclusion, schema generation, mobile selection and return;
record native evidence separately if unavailable. No Chat/Life changes, new
permissions, retention, editorial reuse, provider work, landing or publishing.

This completes the receiving contract needed by broader C4b; lexical matching
is not a substitute for semantic retrieval or evidence that C4b is finished.
The semantic index remains non-runtime pending its separately reviewed reader
and activation boundary. The audit used an older lane roadmap copy for part of
its recommendation; current program/policy instructions must be read from this
canonical workspace, while implementation stays in the isolated lane.

**Search-consumer review checkpoint, not acceptance:** Content returned backend
`b681845a2`, app `3b79e5579` and workspace `f35dfe0`. The implementation adds
metadata-only reading results, exact Source/version query parameters and
source-keyed mobile caches. Strategy independently ran 28 database-free
presentation/compiler/search tests at clean backend `578d44311` in 4.007s;
the app/workspace were still dirty, so this is only that backend boundary.
The first handback remains incomplete: rows lack canonical subject labels,
successful detail responses with a missing selected reading lack an explicit
receiving state, new mobile tests prove navigation rather than selected-content
render/return, and the final search filter drops accommodation/experience
readings instead of establishing their receiving path. Content is assigned one
consolidated completion pass, including real search-to-detail lifecycle
readback and consistent reader/control-plane/release eligibility. Existing
commits are preserved; no whole-package, native or activation acceptance follows.

**Independent follow-up verification:** at clean workspace `65193c1`, backend
`1ba22dcdd` and app `c9f9533d5`, Strategy passed 81 backend tests in 6.961s
(including real PostgreSQL search/detail lifecycle reads), 89 mobile tests in
7.011s, app and test-contract typechecks in 11.175s, and API coverage (566 active,
15 dark, 62 retiring). Logs are under
`/tmp/vesper-places-search-review-20260909/`. The control-plane bypass was first
reproduced at `5f9f2b80a` with primitive reads enabled; the independent four-case
gate matrix now passes. Canonical subject labels, real accepted version-2
replacement and all four entity-route transports are present. Correction,
evidence withdrawal and release-scope exclusion are separate evidence boundaries.
Search context/catalog collaborators remain stubbed in the connected database
test; this is not live-provider, native, latency or release certification.

**Receiving renderer follow-up completed:** app `b5d10917f` exercises the actual
renderer/projection for selected, unavailable and malformed readings, including
accommodation/experience. An unavailable selection does not become a generic
Take. Strategy independently passed 91 focused app tests across seven suites.
This closes that renderer gap, not native or whole-package acceptance.

**September 9 deep-review repair round — local fixes verified; Integration paused.** Independent
review found six remaining cross-consumer defects despite the earlier focused
checks. Repair existing owners in their isolated lanes; do not start a new
architecture or wait for another design canvas.

| Repair | Owning implementation lane | Required evidence |
|---|---|---|
| Apply receiving-surface/release eligibility to direct Home/Places content, not only search | Content + Places backend | Denied surface and disabled/restricted delivery remain excluded through actual composition; valid delivery survives. |
| Remove an already-mounted private original at its authority deadline | Home app | Fake-clock mounted expiry, resumed/focused revalidation and revoked/expired source handling; no generic private-image caching. |
| Return useful negative/unknown answers to explicit practical-fit questions | Home + Places backend | Real explicit-request path returns honest supported/unsupported/unknown assessments without promoting infeasible unsolicited recommendations or action authority. |
| Preserve exact reading identity/revision through root doors | Content app's complete selected-reading receiver | All supported entity destinations keep selection and return context; incomplete selection fails closed. |
| Carry and enforce the selected Take's authorized deadline | Content backend + app | Deadline survives projection and an already-mounted selection becomes unavailable without substituting another Take. |
| Bound optional content retrieval so it cannot hold base results hostage | Content + Places backend | Bounded scan plus success, failure and slow-producer tests; catalog/base results remain independently available. |

The founder requested local Luna xhigh subagents, not separate execution
threads. One worker started; the session refused additional agents because its
retained-agent limit was reached. Luna implemented content admission/budgets;
Strategy completed receiver and candidate-scoped practical-answer repairs
and independently reviewed and verified. Strategy coordinated shared schemas
and commits. No parallel owner may overwrite another bundle's
changes, and unrelated canonical design edits remain untouched.

Review evidence before repair: 151 Content backend tests, 146 Places backend
tests (13 deselected), 108 Home backend tests, 53 canonical Life/capture tests,
91 Content app tests and 51 Home app tests passed in their stated isolated
environments. A new mounted-original expiry regression failed as expected;
these prior passes do not refute the six findings. Commands, revisions and
measurements are under `/tmp/vesper-review-20260909/`. Connected PostgreSQL
evidence uses only Content's explicitly disposable lane database on port 60716.
Native acceptance, full `make verify`, combined delivery and production latency
remain unverified. Integration is still **PAUSED**: no landing, publishing,
shared-runtime restart, supply activation or new product-policy authorization.

Receiver repair checkpoint: Content app `ea8888f4e` preserves exact root
reading selection; Content backend `250a3810c` and app `dfe84b3c4` preserve and
enforce the selected Take's validity deadline. Home app `4424d8d59` and
`04d12c754` enforce original-source custody while mounted and across suspended
foreground return. Independent combined checks passed 139 Content app tests
and 61 Home app tests, both app/test-contract typechecks, and Content's surface
size gate. The Take backend test file passed 19 tests. Evidence is under
`/tmp/vesper-fixes-20260909/`. Home's verification borrowed Content's installed
dependencies only after both package manifests and lockfiles compared
byte-identical. Existing Object-page lint warnings remain; no native evidence
was collected. The older Home/Places mobile branches still require Content's
complete selected-reading receiver at eventual integration; query parameters
alone are not a receiving implementation. These isolated commits do not
resume Integration.

Backend repair checkpoint: Home backend `5922f9a3e` preserves a directly
requested assessment as a read-only answer, including a useful unsupported or
unknown result. Activity feasibility stays false; unsolicited recommendations,
stale/unauthorized owner reads and action authority do not inherit the exception.
Places backend `027786a43` carries the shared answer contract while preserving
its newer route-fact evaluator, and gates/budgets public-content delivery.
The explicit request-to-answer route is verified in the Home lane; eventual
integration must retain that request binding alongside Places' newer evaluator.
Do not replace either branch's entire evaluator/adapter with the other.

Content backend `26c2d6244` closes receiving admission and optional search
budget/hydration gaps. Producer regressions cover disabled flags, incompatible
surfaces, disallowed consequences, absent release authority and valid delivery.
Slow/failed optional readers preserve base results; the existing bounded pool
continues observing workers after request timeout.

Independent measured checks passed 95 Home practical tests, 97 Places
admission/practical tests, 107 adjacent Places tests, and 91 Content
admission/reading tests. Some packets overlap; these are not unique-test totals.
Five Content database tests also passed against its explicitly disposable
PostgreSQL on port 60716. SQL-limit regression checks the constructed query
before hydration; the database packet is not a production latency measurement.
Offline OpenAPI export, app projection, generated types, TypeScript and API
coverage passed in Home and Places. Home schema commits are workspace
`2bf01ac` / app `ddf9866f9`; Places are workspace `8a17eca` / app `ca8860966`.
Places regeneration also reconciles already-implemented PracticalVisitIntent,
revision and time fields absent from its older snapshot; none is a new API
promise introduced by this repair. No generated file was hand-edited.

The expanded Home packet initially failed seven tests because its MagicMock
clock replaced a datetime query annotation during FastAPI app construction.
A test-only concrete clock repair restores the real datetime schema. The final
combined Home packet passed **151 tests** (root service/routes, Home portfolio,
practical route delivery, value composition and v2 contracts). No tests were
quarantined. Backend Ruff and applicable local commit hooks passed; formatting
hooks required a reviewed formatting-only retry in Content and Places.
This closes all six reviewed defects at the isolated implementation/test
boundary, not combined integration or native acceptance. Full `make verify`
and native device tests remain **unrun**. Existing Object-page lint warnings
remain. Canonical child repos were not changed; concurrent canonical design
documents remain outside this repair. The roadmap's local pre-commit checks
are invoked explicitly before its scoped commit to avoid auto-stashing those
concurrent edits; repository hook configuration is unchanged.

**Latest September 9 continuation:** isolated Content PostgreSQL is now
provisioned and the existing Foundry transaction guarantees have connected
evidence. Backend `bcafb2146` adds same-run replay, immutable evidence conflict,
editorial rollback and projection-failure/retry tests; the owner reports
14 connected Foundry/source/ledger/content/projection tests and 9 entity
fact/identity tests passed. Workspace receipt `1b4b419` holds the detailed
commands and environment. Strategy inspected the test implementation and
receipt; that initial packet was not a process-kill or concurrent-Foundry proof. Earlier
statements that the test database was unavailable are historical. The lane's
Compose project owns PostgreSQL on port 60716; this does not resume Integration.

**Content lifecycle continuation reviewed:** backend `6c060a36a` and lane
workspace receipt `9de0d55` extend that packet with barrier-started concurrent
same-plan promotion and reviewed public Source readback through correction,
validity-window exclusion and withdrawal. Strategy inspected the committed
tests: both workers must converge on the same observation, claim, primitive and
projection identities; old and withdrawn content must fail the exact reader as
well as disappear from enumeration. The barrier coordinates worker starts, not
a prescribed database-lock interleaving. The owner reports 10 focused tests and
25 adjacent connected tests passed, plus formatting and documentation checks;
Strategy subsequently reran this test file within the C4b packet below, not the
entire 25-test adjacent selection. No production code changed
in this increment. Process-kill recovery, cross-run editorial reuse policy,
provider activation and user-facing acceptance remain outside this evidence.
These commits remain isolated and unmerged.

**C4b structured/lexical slice reviewed:** Content backend `53879cbe4` adds
bounded multi-place retrieval through existing place-membership and content
readers; `284312179` repairs represented-clock eligibility and distinguishes an
unmatchable explicit question from no-query browsing. It searches up to eight
caller-resolved places, scans beyond a nonmatching initial page within an explicit
budget, preserves supported anchor representation, and returns current eligible
material or an honest empty result. Strategy inspected both commits and ran the
full focused packet against the lane-owned disposable PostgreSQL on port 60716:
**38 passed**, zero skipped, 3.989s, at clean backend `284312179`, workspace
`9de0d55`, app `12cc59a51`. Command and measurement are in
`/tmp/vesper-c4b-review-20260909/`. The owner subsequently stopped PostgreSQL and
retained its volume.

This is not all of C4b: `now` governs freshness, not future event-window search;
anchors are supplied, not geocoded; matching is bounded ASCII lexical matching,
not semantic retrieval. Mocked stale records prove eligibility filtering, not a
live stale-vector path. No new runtime vector consumer, provider/model call,
root producer, UI, source activation or Integration landing follows. These are
explicit remaining consumer/supply seams, not reasons to rebuild the owners.

E2's previously unrun mobile destination suite has also been executed by
Strategy against clean app `500aa7299`: 4/4 Jest cases passed, followed by a
passing TypeScript check. The lane and installed canonical dependency lockfiles
match; an ignored dependency symlink supplied the existing installation without
a package install. Measurements and full logs are in
`/tmp/vesper-e2-mobile-depth-20260909/` (6.499s Jest, 12.952s typecheck).
The backend was concurrently edited by its owner and is outside this app-only
evidence. Native presentation and combined release verification remain unrun.

The [remaining Content policy recommendations](recommendation-world-supply-architecture-and-roadmap-2026-09-07.md#127-september-9-recommendations-for-the-remaining-policy-choices)
now specify the choices for cross-run editorial reuse and acquisition cost
accounting. They are proposals; fixes to existing transaction or parser
semantics do not wait on them.

**E3 blocker correction:** Places' reassessment `484280c` identifies a missing
request-scoped route adapter, not a required new durable route owner or product
policy. Existing RouteFact, Entity situation and foreground movement contracts
supply the semantics. Implementation is continued in the same lane: bind exact
viewer/request, origin, destination, mode, departure applicability and expiry;
consume authorized route evidence through the existing owner family; keep
ordinary root reads provider-free. The earlier
blanket statement that no code change was safe is superseded by this reassessment.
Implementation review additionally requires private route inputs to remain out
of serializable value candidates, hashable exact request binding, and no invented
expiry or unsupported departure-time applicability. Provider isolation must be
tested through the actual root composition path, not only the generic compiler.

**E3 adapter and practical-consumer slice reviewed:** backend `edc91997a` adds
the request-local route adapter and fit assessment; `ad992f0da` repairs the exact
canonical-ref assertion and proves a positive compiler → registered executor →
value-judgment path. A longer duration changes the admission result. Strategy's
first run at `edc91997a` found 135 passed / 1 failed; the repaired four-suite
packet passed **137**, zero skipped, in 4.305s at clean backend `ad992f0da`,
workspace `afceb11`, app `500aa7299`. Logs and measurements are in
`/tmp/vesper-e3-route-review-20260909/`. Provider and entity boundaries in this
packet are stubbed; this is not a live-provider, HTTP-caller or native proof.
Route-only acquired observations may follow request start; ordinary historical
owner-read clocks remain constrained. The route input is kept out of serialized
value candidates and owner requests.

**Next implementation boundary:** connect these tested capabilities through
real, explicitly authorized consumers. Neither the new multi-place retrieval
helper nor the route-input mapping currently has a new production caller. Trace
existing producer/foreground paths before choosing the adapter; preserve no
acquisition on ordinary root reads, exact request context, useful delivered
content, and current eligibility. Do not call these helpers a complete system,
restart Integration, or wait for a visual canvas to investigate this wiring.

**Caller-connection round dispatched — September 9:** both existing sessions
continue in their isolated lanes with Luna xhigh requested, owning complete
implementation/test handbacks rather than another helper-only audit:

- **Content:** connect current place scope to admitted child-entity material
  through `home_portfolio.py` and `source_contribution_discovery.py`. Exact
  place-only enumeration currently misses site/venue-owned primitives. Preserve
  canonical child subjects, exact Source versions, release/eligibility gates,
  bounded work and honest geographic versus personal relevance; prove the real
  sparse-history producer path and correction/withdrawal behavior. Content owns
  these discovery/producer files and necessary content-reader adapters.
- **Places:** connect shared route evidence semantics to the existing
  authenticated entity-situation POST/service. Reconcile its separate route
  expiry/origin handling with the new adapter under an existing neutral owner,
  preserving import boundaries, useful existing response semantics and Plan
  information. Prove the actual foreground caller and retain route-backed fit
  tests. Places owns entity-situation and route/owner-read files; it must not
  introduce a Places-to-agent dependency or a second routing engine.

These are scoped consumer implementation assignments, not Integration activation.
No new source/provider activation, location collection, background work, shared
runtime, Chat/Life/UI redesign, canonical landing or publishing is authorized.
Necessary wire changes, if justified, retain normal contract synchronization and
consumer verification. Owners coordinate specific overlaps directly.

**Foreground route consumer verified — September 9:** Places backend
`9d8183513` connects the existing authenticated entity-situation POST/service
and canonical route reader through `core.distance.request`, with no
Places-to-agent dependency or new wire shape. Strategy's five-suite packet
passed 159 tests, but an additional executed advancing-time reproduction showed
that a route expiring between request start and completion was still accepted.
Backend `27f4d7420` repairs that boundary for both route and origin validity.
Strategy reran the same packet: **159 passed**, zero skipped, 4.615s; the three
new clock regressions also passed (1.554s). The original reproduction now yields
`route_expired`. Logs/measurement are in
`/tmp/vesper-foreground-route-review-20260909/`; backend was clean at that
revision, app unchanged at `500aa7299`. Workspace `72857a1` was clean for the
five-suite run and had owner documentation edits during the separate clock run.
The HTTP test executes the actual service/shared validation with stubbed entity,
relationship and route-provider boundaries. It is not live-provider, native,
route geometry, deployment or combined-system evidence. Content's producer
package was still in progress at this route review; neither lane is merged or activated.

**Content caller package verified — September 9:** backend `709e27466` connects
current place scope to admitted child-entity Sources in Home and Source discovery.
`12d30676e` adds short-circuitable hydration and local omission when a child's
canonical identity cannot be resolved; `e6d0edd10` adds real SQL scan measurement.
Strategy inspected these changes and independently ran the seven-suite
core/root/Foundry/side-build packet against the lane-owned disposable PostgreSQL
on port 60716: **112 passed**, zero skipped, 9.479s, at clean backend
`e6d0edd10`, workspace `9de0d55`, app `12cc59a51`. Full command, output and
revision measurement are in `/tmp/vesper-content-root-review-20260909/`.
The actual discovery producer uses the real Source reader and canonical child
resolution in its connected test; external/context branches are stubbed and
dogfood activation is disabled. Exact parent/child release composition retains
focused unit evidence, not a new production activation claim.

**Next design-independent package: bounded set-based Source hydration.** The
owner measured 49 SQL executions for eight hydrated records on early success,
and 242 for forty records when the first 32 are stale. Strategy's rerun verifies
the committed real-reader regression's relative-query and exact-row assertions;
the exact SQL totals are owner-reported. Source inspection confirms repeated
policy/evidence/disagreement/lifecycle reads inside `_load_record`, including
duplicate required-evidence lifecycle work. Content is dispatched to eliminate
this per-record amplification through the existing canonical reader, retaining
bounded early termination, complete record semantics, correction/withdrawal,
expiry, evidence/policy and release eligibility. Compare actual SQL counts,
hydrated records and useful output before/after; do not introduce a cache,
alternate owner or eligibility shortcut. This is an implementation package,
not another helper-only audit. The private database remains available for this
work; no provider, UI, source activation, main landing or Integration restart
follows. Semantic/time retrieval and the broader C4b/C5a/C6a boundaries remain
unfinished.

**Independent temporal-consumer repair dispatched — September 9:** Places
continues in its existing practical-judgment lane. The current
`/api/places/map` already accepts explicit dates without a Trip, but
`get_discover_map_experiences` compares `starts_at <= date_to` directly against
a date. This inspected boundary can omit later events on the final requested
day; existing connected cases do not test that edge. The owner must reproduce
it, repair complete calendar-window handling through the actual map reader,
and verify authoritative timezone/default-day semantics, spatial scope,
historical requests and unchanged recurring/on-demand browse behavior. Reuse
existing time owners; do not invent a timezone, occurrence or second event
engine. `load_place_experience_previews` already supplies a local-window helper
but has no production caller; its existence is neither a complete temporal
consumer nor permission to widen the API. Places owns the map/entity query
and temporal tests, disjoint from Content's Source hydration files. Use its
own manifest/runtime and finish the implementation plus connected evidence in
one handback. No design, Trip creation, UI change, provider acquisition or
Integration restart is required or authorized by this repair.

**Source hydration package verified — September 9:** Content backend
`60029f1ba` replaces per-record auxiliary reads with set-based hydration and
SQL latest-per-observation lifecycle selection; `e5fe426e8` bounds all affected
readers to eight-record hydration batches, including entity/no-callback reads.
The real scan regression now enforces SQL budgets, not merely a relative
query-count assertion, and exercises stored policy/disagreement preservation.
Another connected case preserves the full ordered entity output through
`[8, 8, 2]` batches. Strategy inspected both commits and independently ran the
expanded twelve-suite root/content/DB-owner packet: **130 passed**, zero
skipped, 9.213s, at clean backend `e5fe426e8`, workspace `9de0d55`, app
`12cc59a51`, using the isolated disposable PostgreSQL on port 60716.
Full command and measurement: `/tmp/vesper-content-batching-review-20260909/`.
The owner reports actual scan costs of five SQL executions/eight hydrated
records and 22/forty, versus the previous 49/eight and 242/forty. Strategy's
rerun verifies the enforced budget and row-count assertions; those precise
SQL totals are owner measurements. This proves bounded roundtrip work for
the tested readers, not production latency, active-release throughput,
live supply breadth or native acceptance. Content's assigned hydration
package is complete at this boundary; temporal map repair remains active.
No merge, publishing, source activation or Integration resume follows.

**Temporal map package verified — September 9:** Places backend `50763e5b5`
repairs inclusive final-day filtering through the existing authenticated map
endpoint and spatial reader. Application-validated timezone data compiles exact
UTC window predicates before the database LIMIT; this avoids both first-page
loss and an unbounded application pagination loop. The result shape, historical
requests, recurring/on-demand browse semantics and explicit invalid/missing
timezone fallback remain intact. Earlier reviewed revisions passed the original
40-test packet but were not sufficient: Strategy reproduced omissions for a
tab-padded New York timezone and `America/Coyhaique`, which the application
recognizes but this PostgreSQL image does not. Both actual-reader reproductions
now return the expected event; only their test-owned rows were created/deleted.

Strategy independently reran the four-suite temporal/Places/map endpoint packet
against lane-owned disposable PostgreSQL on port 55572: **42 passed**, zero
skipped, 8.385s, at clean backend `50763e5b5`, workspace `5efb55c`, app
`500aa7299`. Full command and measurement are in
`/tmp/vesper-places-temporal-review-20260909/`. The real endpoint case overrides
authentication but executes the map service/readers; the many-adjacent-events
case enforces one experience query with the correct later result. This proves
the tested predicate/result and roundtrip boundary, not a production query-plan
or latency budget, all temporal discovery, provider freshness, or native UI.
The Places assignment is complete at this boundary. Both execution lanes are
idle; their temporary PostgreSQL services are stopped after Strategy's checks,
with volumes retained. No main landing or Integration restart follows.

**C3a parser completion:** Strategy found that Ticketmaster normalization still
converted raw status omission into `onsale`, bypassing the earlier writer-only
repair. Backend `7802fe99d` preserves that omission through normalization and
the SQL update while retaining explicit `onsale`. Strategy inspected the patch
and ran both affected ingestion suites: 34 passed against that clean backend
revision (1.301s). Full output/measurement is in
`/tmp/vesper-event-omission-20260909/`; an earlier invocation ran from the wrong
directory and collected no tests, then was corrected. This establishes the
raw-response-to-generated-update boundary with a mocked database, not provider
conformance or a live ingestion deployment.

**Velocity refinement, September 9:** keep implementation autonomous and
compatibility continuous, but make coordinated integration demand-driven.
Reviews below are triggers, not a fixed sequence of stop gates. Package readiness,
landing and whole-product acceptance are distinct; no per-commit, per-day or
three-package integration ceremony is required. Required delivery gates remain.

### Design independence rule — September 9

A Claude canvas, screenshot, or other design export is a reference consumer,
hypothesis set, and validation target—not an engineering gate. When a design is
unavailable, changing, or unresolved, continue render-independent work against
the accepted product grammar and system contracts: domain truth, read models,
state transitions, authority, provenance, privacy, evidence and affordance
intents. Keep those seams stable and adaptable; do not encode disputed card
anatomy, navigation, visual hierarchy or copy into the substrate merely to make
progress visible.

The arrival of a design should cause a bounded presentation validation and any
necessary adapter work, not a repository-wide restart. The design-dependent
parts are the final composition, visual treatment, interaction details and
native acceptance evidence. A missing design can block only work whose meaning,
policy or contract genuinely depends on that choice. It must not block
independent capability implementation, focused tests, fixtures, telemetry or
owner-backed read/write paths. Conversely, design-independent tests do not
claim visual or product acceptance.

## 1. Purpose and authority

Make Vesper's capabilities work together as a useful everyday product: immediate
help, worthwhile discovery, human connection, practical assistance and continuity,
without extensive setup or continual contribution. Travel is a demanding
specialization, not a required entrance. **Make sense. Open possibility. Help it
work. Carry forward.** These are a repertoire, not stages, tabs or services.

This is the short current coordination map, approved by the founder in Strategy
on September 7. It replaces older lane-allocation instructions, not unfinished
acceptance requirements. [Product Thesis](../../travel-agent/docs/product/Product%20Thesis.md),
[Product Model](../../travel-agent/docs/product/Product%20Model.md), accepted
decisions and system contracts retain product/authority ownership. The
[Integration plan](complete-system-integration-roadmap-2026-09-05.md) owns shared
technical sequencing and landing; lane plans own implementation detail;
[journey evidence](../journeys/EVIDENCE_MODEL.md) and release owners determine
certification. This is not an eleventh canonical-spine entry or a release scope.

No universal-object rewrite, mandatory Plan, booking-execution expansion, or
single-loop prerequisite. The live engine participates in selection, fit,
reevaluation and permitted consequences throughout; it does not depend on a
Life page opening. Chat layout redesign remains outside these assignments.
Pending policies, paid/provider runs, deployment, activation and destructive
retirement require their existing approvals. Assignment does not dispatch a task.

## 2. Inspected baseline — September 9

Read-only recheck: workspace `1cc28e26cfa8bb2f575718177718854a086bb68a`, backend
`a7c02cbe15940d13303ae98ada8d6e8192fc85a4`, app
`e2e792913b1902007ad237b05a3a58784a80332c`, all on main. Children are clean;
workspace has concurrent design reviews, handoffs, delivery records and generators.
There are 16/18/17 worktrees respectively; no other checkout was adopted or
fast-forwarded. These are observations, not locked dispatch bases.

Source inspection confirms a shared Home/Places composition pipeline, additive
current-job owner-read compilation, exact Source result retrieval, delivery
exposure/known-claim checks, object-page projection and internal Life organization
readers. Do not rebuild these. In the inspected shared value-composition path,
the only admitted practical question is `place.open_now`; other questions are
explicitly unknown. This is not a claim that the wider live engine lacks movement
or other specialists. Entity viewer context ranks facts but does not currently
enter `composeObjectBodyBlocks`; Life's internal organization reader remains
distinct from serving adoption. These observations motivate the next packages.

No fresh product tests or native certification were run for this rebaseline.
The documentation-only check found an unrelated `design-gen/social/README.md`
missing metadata/inventory registration; do not carry September 8's docs pass
onto today's dirty tree or silently repair another lane's generator output.

### Historical September 8 reliability and acceptance evidence

**Acceptance-planning recheck:** workspace `33cceef`, backend `a7c02cbe1`,
mobile `e2e792913`, all on canonical main. The child trees were clean; root
has concurrent Places generator edits in `docs/working/design-gen/places/`,
which this plan leaves untouched. These observations are dated, not locks.

| Layer | Landed / recorded evidence | Remaining boundary |
| --- | --- | --- |
| Engineering baseline | Earlier backend `78ea8a05f`: 21,322 offline and 1,369 serial connected tests passed with documented skips/exclusions | Not a full-suite result on today's HEAD; mypy's last measured 262 errors/62 files remains unresolved |
| Home / Places | Exact requested-result states and return; attributed human/public-content receiving; exact Place-depth fix `e2e792913` | Native acceptance and populated coverage unrun; Source production remains dark |
| Content | Public owner-to-Home adapter; conservative quality labels `8a092de39`; bounded non-Trip purpose fit `a7c02cbe1` | Researched Pier 57 records are local authored review fixtures, not production coverage or measured enjoyment |
| Capture / Life | Candidate lifecycle option A producer `cd0e28f35`, shadow consumer `ac54cefc9`, revision alignment and fixtures | No indexed serving cutover, general occurrence/people inference or Atlas retirement |
| Latest focused evidence | Content/Home 98 backend tests, 45 app tests and typecheck; Life 271 offline and 43 connected tests; documentation and API coverage checks passed in owner receipts | Overlapping selections, not additive journeys, native proof or complete release verification |
| Social | Ordinary-sharing decision packet prepared on isolated branch; existing bounded addressed receiving tested | Generic sharing policy, friend-source AI use and general Life refinding remain unadopted/unimplemented |

The previous rounds are closed at their stated boundaries. Their detailed
history, commands and failures remain in the [Integration checkpoint](integration-execution-checkpoint-2026-09-07.md)
and [Content receipt](content-home-supply-execution-receipt-2026-09-08.md).
Do not restart repaired documentation gates, reimplement connected hooks or
describe the adopted anchor contract as a current decision blocker.

Native feasibility was inspected read-only: Xcode 26.5 build 17F42, Maestro on
PATH, available iOS 18.2/26.5 simulators, none booted; no listener found on default
Metro port 8081. Runtime printout reports canonical ports, not a reserved lane.
App build installation/compatibility, design-reference hashes, Maestro health
and isolated runtime readiness remain unverified. No device or service was
started by this planning pass.

## 3. Whole-product outcomes and sequence

| Outcome | Now | Next / later, without dropping the broader scope |
| --- | --- | --- |
| Useful material with real depth and return | Connect prepared public/personal material to varied Home/Places output and exact destinations | Complete requested-work UI, sparse/failure states, useful depth and reuse; widen supply based on measured gaps |
| Recognizable, revisitable Life | Connect source evidence, organization and bounded readers; inspect evolving groups and previews | Compare bounded model assistance on identified misses; broaden coverage, then separately accept serving cutover and Atlas retirement |
| Enjoyable ordinary sharing | Settle the next source/audience contract; connect original receiving, durable controls and refinding | Extend the same owners into guests, gatherings and permissioned social intelligence; receiving never owes a reply or plan |
| Practical help within the same experience | Make supported facts change the appropriate offer while independent reading, saved and human value survives | Extend beyond opening status when a concrete timing/fit question requires it; accepted following and external changes need their own authority |
| Trustworthy combined delivery | Receiving/reliability round locally landed; preserve its passing test selections and explicit typing debt | Verify new connected product packages, cost, native/accessibility and rollout at their proper scope; retire replacements only after obligation review |

These outcomes overlap. **On explicit dispatch, implement independent packages
without waiting for every design or policy.** An unavailable dependency blocks
its affected work, not the whole package. The emphasis is existing capabilities
becoming useful together, with consumer-path completion rather than more layers.
Reopen architecture when evidence exposes an owner or dependency contradiction.

## 4. Current package register

The prior isolated receipt `f3bd44b` retains its evidence and gaps, not a current
execution instruction. The detailed implementation scope is the leading
[September 9 tranche in the technical plan](complete-system-integration-roadmap-2026-09-05.md#current-engineering-tranche--september-9).
Use two substantial packages, not six engineering lanes mirroring design projects.

| Package / role | Status and complete outcome | Dependency / handback |
| --- | --- | --- |
| **A — Received material and continuity** | Dispatched to **Home**; implementation slice complete at its supported boundary. Luna xhigh requested. Retained-image and exact text-original receiving/return, existing human/text receiving and the explicit practical-assessment consumer binding are delivered; exact recipient-side human media remains an unimplemented dependency. | Uses existing content/source/social owners; owns shared root/consumer seams. No new source store or Life serving cutover. Final handback records commits/evidence and precise relationship-media/practical receiver boundaries. |
| **B — Practical judgment and contextual projection** | Dispatched to **Places**; backend contract and self-review complete at its supported boundary. Luna xhigh requested. `place.fit_window` now handles exact place/commitment evidence, closure, expiry and viewer binding; its first root consumer is delivered through the bounded Home-owned explicit Places v2 request seam. | Uses existing place/route/commitment owners. The delivered seam proves one explicit request end to end without changing Chat or ordinary cards. Future producers, route-owner coverage and adaptive Entity/recommendation-policy exceptions remain separate decisions. |
| **Strategy / this thread** | Own priorities, consequential decisions, package boundaries and whole-product review. | Resolve only the few choices that block named capabilities; inspect evidence rather than require approval after each step. |
| **Integration** | PAUSED. Retains combined candidate, shared runtime and landing ownership; not the approval desk for local implementation. | A future explicit resume names a bounded landing or combined acceptance task, not necessarily both. Receive relevant ready cuts without waiting for unrelated packages; existing gates and publication authority remain. |
| **Existing Content, Life, Social, Entity and Plan lanes** | References/suppliers, not automatically restarted. Their branch-local work is not assumed merged. | Reuse owner plans and tested cuts. Assign a separate supplier only for independent work that reduces blocking, with one file owner. |

### September 9 dispatch record

| Package | Existing session / isolated coordinated checkout | Initial isolated ports / progress owner |
| --- | --- | --- |
| A | Home `01a06f87-e648-74d2-a0ae-f0adb305e44c`; `/Users/feihuyan/travel-workspace--received-value-2026-09-09`; branch `codex/received-value-2026-09-09` in all three repos | Postgres 55566, Qdrant 55567/55568, API 55569, Expo 55570; lane-local `home-connected-experience-implementation-map-2026-09-04.md` |
| B | Places `01a07c7f-871a-70b0-840e-95a0db1e9351`; `/Users/feihuyan/travel-workspace--practical-judgment-2026-09-09`; branch `codex/practical-judgment-2026-09-09` in all three repos | Postgres 55572, Qdrant 55573/55574, API 55575, Expo 55576; dated progress section in its lane-local technical roadmap |

Both coordinated lanes were created from §2's complete September 9 tuple and
checked clean before dispatch. The tool accepted one consolidated assignment
per existing session with explicit `gpt-5.6-luna` / `xhigh`; both turns completed
without a reported tool error. The response does not expose effective model/
effort or Fast readback: requested settings are recorded, Fast and effective-
setting verification remain unavailable. No model defaults, global configuration,
extra task or monitoring automation changed. The OpenAI Docs check supports
explicit model selection, not a claim of verified runtime settings from a title
or prompt.

The latest canonical roadmaps/design reviews are uncommitted and therefore not
in these new worktrees. Both assignments explicitly require read-only intake of
the canonical September 9 versions, recording inspected versions/hashes, while
all implementation and progress edits stay in the owner's lane. Strategy owns
canonical roadmap/recommendation updates; do not import all canonical dirty work.

A writes root composition/selectors, receiving/navigation/Life consumer changes
and final generated contract synchronization. B writes practical assessment and
necessary assessment model fields, coordinating exact shared files before edits.
A receives an immutable B cut and verifies the real consumer. Existing domain
truth/grants remain with their owners. Both can perform necessary local tests,
bounded repairs and explicit-file local commits; no publishing/main landing,
paid/provider work, flag activation or broad retirement. Local disposable runtime
requires manifest/port recheck and explicit DB safety; neither lane starts with
an allocated device. Integration is not a dependency for ordinary file work.

Strategy's [two concrete design recommendations](vesper-five-project-design-consolidation-2026-09-08.md#september-9-implementation-round-recommendations--two-narrow-choices)
remain ready for founder selection. They do not amend accepted decisions. Only
the dependent new anatomy/Plan continuation waits; present assessment and
supported receiving continue. The completed package handbacks are evidence at
their stated boundaries, not a complete-system or native acceptance claim.

**A first handback — September 9, returned for receiving repair:** isolated app
`90da37e83` and workspace `c5f5836` add a separate Source-original door and route
`source_attachment` to its Intake submission. The owner reports 73 focused Jest
tests, typecheck/lint and 99 offline backend tests passed; Strategy inspected the
diff/receipt but did not rerun them. The actual destination currently shows
notes/count/lifecycle rather than the original attachment, and ignores the passed
`rootReturnToken`. Producer code confirms attachment identity currently equals
submission identity, but route identity alone does not prove useful consumption
or return. Package A remains incomplete: the owner has one consolidated repair
instruction covering actual source receiving, destination/return tests and the
remaining originally assigned material families. No Integration restart, landing
or new acceptance campaign follows. B was still active at this receipt check.

**A second handback — September 9, repair still required:** backend `250e4cd3a`,
app `9a8ecbc9c`, workspace `016c652` add authenticated Intake media and an image
reader with root return. Owner-reported evidence is 77 app and 127 offline backend
tests plus typecheck/lint/API/docs checks, not independently rerun or native
acceptance. Source review found same-object custody-loss display handling missing,
a duplicate API-origin resolver bypassing the shared runtime override, uncaught
storage SDK failures, and unavailable-screen return gaps. One consolidated repair
request also retains the originally assigned directed human-original path, which
the handback leaves venue-only. The slice is improved, but Package A is not yet
complete or ready for landing; no integration ceremony was started.

**Latest partial cuts — September 9:** A backend `95f5e201c`, app `cbcf98f53`,
workspace `1f88e98` address the named custody-display, API-origin, SDK-error and
state-return defects at source-review level. A reports 79 app/128 offline backend
tests; real disposable-DB owner authorization and native/private-cache behavior
remain unverified. This is a delivered retained-image slice, not all of A.
B backend `311c4b995`/`e40c09e25`, workspace `f8ccc84`/`f6e8b45` supply bounded
window arithmetic and viewer checks; the receipt still leaves producer/consumer
wiring outstanding. Strategy requested precise claim/operational boundaries,
exact commitment filtering and waiting-versus-overlap correction before binding.
Both owners were continued under their original assignments to reconcile that
dependency directly and finish permitted human-original receiving or name a
specific genuine blocker. Their final handbacks now identify the supported
consumer outcomes and precise remaining seams. Neither package is a complete
system acceptance; no extra lane, main landing or shared acceptance round
follows. The next dependent implementation requires an explicitly assigned
landing/consumer task after B's backend contract is adopted, not a recurring
Integration ceremony.

**Final package handbacks — September 9:** Home workspace `490b6dc`, backend
`95f5e201c`, app `cbcf98f53`; Places workspace `d8b2c42` (with backend
`e67b84e1a`). Home reports 79 focused app and 128 focused offline backend tests,
typecheck/lint/Ruff/hooks and API/docs checks at their stated boundaries; Places
reports value 28/28 and graph/owner-read 34/34 plus Ruff/hooks. These are owner
receipts, not rerun by Strategy. Home's retained-image media reader and exact
Home/Places-origin return are now a useful supported result. Its directed human
path is honestly complete only as attributed words plus the canonical venue door;
an exact recipient-readable original-media seam would require a new relationship
authority/API and remains deferred. Non-image source objects, populated producer
supply, disposable-DB authorization and native/cache evidence remain unverified.

Places' `place.fit_window` is a bounded, read-only assessment from explicit
visit window/duration, exact `place.read` and optional exact `commitment.read`.
It rejects current closure/permanent closure, filters exact commitment refs,
preserves evidence expiry/viewer binding and keeps route origin unknown without
an admitted `route.evaluate` owner. It deliberately does not judge hospitality
or waiting cost. Ordinary Home/Places cards do not emit this intent; the bounded
Places v2 caller seam now carries the exact fields and a root-visible receiving
fixture is proven. No API/provider/booking expansion, new policy, Chat redesign
or Integration wake followed this round.

**Consumer-bound follow-up — September 9, completed:** the remaining dependency
was one bounded Home-lane assignment, not a new parallel lane. In
`/Users/feihuyan/travel-workspace--received-value-2026-09-09`
(`codex/received-value-2026-09-09`), Home adopted the complete Places backend
range `311c4b995^..e67b84e1a`, added an explicit target/window/duration request
seam, and proved one truthful `place.fit_window` result through root selection,
OpenAPI serialization and the existing Home/Places semantic renderers. The
assignment forbade ordinary-card inference, Chat/Life changes,
route/booking/provider expansion and fabricated fields; those boundaries held.
Workspace `81df98a`, backend `a5326eec0`, and app `954a43c1e` are clean lane
handbacks. Owner evidence: backend focused packet 127 passed; app renderer
suites 9/9, TypeScript/schema bridge, changed-file lint and full lint error
count passed; API-coverage, docs-links and governance passed. This remains
focused synthetic/owner-read evidence: no native/device, populated production
provider, route-owner, or UI request-control acceptance is claimed. Integration
remains paused; no shared runtime, landing or publication is implied.

The producer decision and user-facing acceptance bar are captured in the
[practical-judgment producer brief](practical-judgment-producer-acceptance-brief-2026-09-09.md).

The subsequent Places hardening pass is recorded in the [technical roadmap's
E3 receipt](complete-system-integration-roadmap-2026-09-05.md#e3-follow-up--deterministic-matrix-request-telemetry-and-local-rehearsal--september-9):
the judgment matrix now rejects ambiguous or stale evidence and the existing
root-composition measurement carries privacy-safe aggregate practical fields.
This improves readiness without creating a producer, changing ordinary cards or
claiming populated/native acceptance.

**A exact-original follow-up — September 9, completed:** the Home lane continued
the same isolated package to close the remaining text-original gap. Travel App
`e274d22aa` renders an eligible exact `text/*` original from verified inline
source material, keeps the existing authenticated retained-image reader, and
labels pending, expired, revoked, missing, unsupported and unknown custody
states without substituting a note, count or lifecycle report. The existing
`rootReturnToken` is read and returns directly to the originating Home or Places
root. Travel Agent `250e4cd3a`/`95f5e201c` remain the owner-scoped media/custody
foundation already present in this lane; no new producer, store or policy was
added. Workspace receipt `10a70ce` records the implementation map update.
The follow-up's focused app suites (3 suites / 15 tests), TypeScript and lint
passed; the earlier package's 127 focused backend tests remain the applicable
backend evidence. The exact recipient-side original for directed human handoffs,
native/device behavior, disposable-DB authorization and populated producer
supply remain unverified or separately scoped. Integration remains paused; no
merge or publication is implied.

**B cross-root replay follow-up — September 9, completed:** the Places lane added
an isolated deterministic replay contract rather than waiting for final Home or
Places composition. Backend `0b7fa0107` composes one bounded Source world twice,
proves a stable production digest, preserves the same represented/owner/subject/
source/evidence refs and supported value facts across Home and Places, and keeps
root-specific candidate IDs, seats, payloads, states and revisions distinct.
The selectors independently suppress an unchanged repeat as
`repeated_exposure`; the practical matrix also proves unknown, stale and closed
evidence cannot erase an independent ordinary value. Workspace receipt
`2cf651b` records the test-only handback. Focused value/replay evidence is 40
tests, with Ruff/format/compile and hooks passing; optional `openai` (and broader
`shapely`/`redis`) imports leave root-projection/API rehearsal unverified. No
production schema, UI, provider, Chat/Life, route or persistence behavior
changed, and Integration remains paused.

**E1 current-job read follow-up — September 9, completed:** in the existing
Places lane, backend `9ca596a89` makes current-job owner reads authoritative at
the root-composition execution boundary. `PortfolioSituation` remains available
for fixtures, legacy callers, Source continuity and telemetry, but no longer
selects runtime capabilities when exact value/current-job requests exist.
Explicit practical origin refs are included as request-local Place subjects;
this does not schedule unsupported routing. Evidence is 24 focused owner-read
tests and 74 combined owner/value/portfolio tests, with compile, Ruff/format and
diff checks passing. The root-composition service test remains unverified in the
lane because optional `openai` (and broader `shapely`/`redis`) imports are absent;
no workaround was used. Workspace receipt `6cc9f00` records the technical
roadmap update. No API/schema/mobile/UI/provider/booking/DB/Chat/Life change or
Integration wake was made.

Strategy then reran the lane's current-job, root-composition and public
Place-to-depth tests from the dependency-complete canonical Python 3.13
environment: **32 tests passed in 4.88s**. This closes the optional-import
collection limit for that focused boundary without changing the lane's broader
provider, native, production or Integration evidence limits.

**Canonical frontend baseline — September 9:** the clean `travel-app` main
checkout at `e2e792913` was exercised with `make test-frontend`. It produced
**1,201 passing suites / 8,187 passing tests**, but failed **13 suites / 16
tests** (8,203 total); the failures include existing conversation/card
contract, navigation, dev-gallery and mock-walk expectations. This is a
current baseline, not a regression attribution to the A/B slices and not native
acceptance. Chat and Life remain out of scope here; the failures are recorded
for their owning lanes rather than repaired opportunistically. The command
completed in 283.121s with its warnings/log output retained outside the repo.

**E2 public Place-to-depth follow-up — September 9, completed:** the Places
lane wired one existing public Place-content Source family through the real
owner boundary, shared judgment and the existing Places semantic renderer.
Backend `5700c4207` derives bounded Place subjects from current Places context
and feed cards, reads current public Sources without provider calls, and emits a
Places-native `FIELD_EDITORIAL_COVER` with the exact
`place_content_primitive` revision, evidence-bound `source.inspect` and typed
`places.open_entity` destination carrying Place and Source refs. App
`500aa7299` exposes that already-declared destination through the existing Door
primitive; no route, taxonomy, schema, provider or visual-composition change
was introduced. Workspace receipt `5567119` records the lane handback. Evidence
is 20 content/lived-experience plus 74 owner/value/read tests, with
Ruff/format/compile/diff and backend hooks passing. The new root-projection test
is unverified because optional `openai` (and broader `shapely`/`redis`) imports
are absent; app Jest/typecheck were unrun in that checkout because
`node_modules` is unavailable. This proves code-path wiring, not live provider
supply or native rendering. No Chat/Life/Integration wake followed.

The focused owner-to-depth, current-job and root-composition boundary was then
rerun from the dependency-complete canonical Python 3.13 environment: **32
tests passed in 4.88s**. This supplements, but does not replace, the lane's
unverified broader root-projection, provider-supply and native-rendering
boundaries.

**E3 route-owner seam audit — September 9, bounded stop:** the Places lane
confirmed that `place.fit_window` is the complete supported route-free
assessment (exact Place evidence, stated window/duration and optional exact
Commitment windows). Origin-dependent fit remains honestly `unknown` because
there is no canonical route owner: `route.evaluate` fails closed as
`canonical_route_reader_not_available`, `PlaceOwnerRead.route_refs` is only an
empty extension point, and `OwnerReadPayload` has no typed RouteFact payload
with origin/destination, mode, time, provider/use policy, revision, expiry and
degradation. The existing `RouteFact` gateway and foreground movement service
are specialized/request-scoped, not owner-bound readback. Workspace receipt
`88c43dd` records the audit; 34 route/movement/value/owner tests plus
Ruff/format/compile/diff passed. No code or schema change was safe, and no
provider, API, UI, Chat, Life, Social or Integration work was started. A future
route package first needs an adopted owner contract and refresh/readback
authority; until then origin-dependent claims stay unknown while ordinary Place
value survives.

**C1a Content accounting follow-up — September 9, completed:** the Content
lane closed measured research-usage accounting across executor/thread
boundaries. Backend implementation `10ecea2c4` snapshots usage before terminal
DB writes, keeps uncached/cache-read/cache-creation/output classes distinct
(including a valid zero uncached count), and scopes the direct
`scripts/run_research.py` caller alongside queue, angle and quick-research
paths. Test commits `25c132fc8` and `d5ee6c38a` cover executor-boundary discard
and success, multiple calls, cache variants, absent usage, concurrent isolation,
an async provider-error-to-discard fallback and metadata-only discard without
private draft/source leakage. Evidence is 42 accounting tests, 5 async error
tests and 78 adjacent regression tests;
Ruff/format/compile, hooks and workspace docs checks passed. Experience-table
token persistence, hard monetary reservation/settlement, paid/provider runs,
production writes and Postgres crash/concurrency evidence remain deferred to
C1b/C2b. No UI, Chat, Life, Social, route, schema or Integration changes were
made; workspace receipts are `1c485df` and `8a16d54`.

**C2b evidence-admission checkpoint — September 9, bounded:** the Content lane
exercised the existing reviewed World Foundry/source-owner handoff without
adding a schema, owner, route, caller, provider, vector index, public
publication path, or consumer surface. Backend test commit `e41efb43b`
(`test(content): exercise foundry evidence admission`) proves that a typed,
source-bound observation and fact claim use deterministic Foundry-scoped keys,
one transaction connection and stable result identities when the same
`PromotionPlan` is replayed. It also proves that a volatile operating-status
fact backed only by `research_aggregate` is rejected before transaction start,
accepted editorial remains `PROPOSED`, and owner `ConflictError` propagates.
Workspace receipt `dd93657` records the evidence and boundaries. Focused
provider-free evidence was `27 passed, 1 deselected` (the guarded Postgres
test); Ruff, format, compile, hooks and docs checks passed. Live Postgres
transaction/idempotency, rollback, crash recovery and provider execution
remain unverified. The current owner key includes `run_id` and
`assignment_id`, so equivalent re-acquisition under a new run receives new
observation/claim/editorial identities; no approved policy yet decides when
that is a new observation versus the same useful version. No reachable C2a
caller currently constructs typed Foundry drafts automatically. This is a
contract checkpoint, not cross-run deduplication or automatic publication;
the isolated child/workspace commits remain unmerged while Integration is
paused.

**C1b acquisition-envelope checkpoint — September 9, bounded:** the Content
lane audited actual research/Places callers and characterized the existing
reservation mechanisms without activating providers or repurposing customer
entitlement accounting. Backend test commit `0bbd18340` covers known-unit
partial settlement, typed `CommercialAccessUnavailable` on settlement
failure, and best-effort release failure; workspace receipts are `3cd1039`
and `614d237`. The offline packet was `45 passed`; Ruff/format/compile, hooks
and docs checks passed. The audit confirms that quick-research operation
counts, provider fan-out/retries, Places' precheck-plus-audit, the LLM job
budget, and the commercial usage ledger have different semantics. Real
Postgres atomic last-allowance/rollback/reconciliation/expiry evidence was
guarded and unrun because the disposable test environment was absent. No
approved policy yet defines provider operation units, retry/page/detail/index
accounting, sponsor/scope, replay identity, or unknown-charge settlement, so
no acquisition reservation was wired and no hard COGS cap is claimed. No UI,
Chat, Life, Social, route, schema, provider or Integration change was made.

**C3a event-lifecycle omission repair — September 9, bounded:** the Places
lane fixed one concrete refresh defect in backend commit `16858e745`
(`fix(events): preserve lifecycle status on omission`), with workspace receipt
`7794848`. A partial provider refresh that omits `status` no longer compares
against or writes the insert default `active`; an existing cancelled or
postponed lifecycle value is preserved while other supplied fields may update.
The focused regression proves the generated upsert contains no status write.
This is a narrow omission repair, not a date-only/TBA schema, full
field-specific operational/semantic split, provider conformance claim, or
complete event supply path. The isolated Places child/workspace commits remain
unmerged while Integration is paused.

<a id="sequence-and-system-checkpoints"></a>

### Execution order and event-triggered reviews

1. **Dispatch preparation, not a housekeeping project:** verify current relevant
   branches/cuts, exact owned files and settled contracts; choose isolated
   coordinated checkouts. Record existing code versus the actual missing consumer
   behaviors. Do not merge every branch or recreate a runtime just to begin.
2. **A and B implement concurrently on explicit assignment.** Each owns several
   dependent substeps through tests and self-review. A does not wait on B to fix
   exact-source receiving; B does not wait on final card design to calculate
   supported fit. Shared schema/root files have one writer and an exact handoff.
3. **Exchange a dependency when it is usable.** Owners agree ordinary interfaces
   and run affected producer/consumer checks directly in their isolated lanes.
   Only a consequential architecture, authority or priority conflict returns to
   Strategy. A tested B assessment can reach A before either package is finished;
   no coordinated runtime or central approval is needed for that exchange.
4. **Finish and report independently.** Each owner self-reviews code, real owner
   paths, change/loss behavior, remaining human work and serving characteristics.
   A DTO without its intended consumer does not finish the outcome. Record
   unsupported parts and readiness precisely; one package does not wait for the
   other's final report. Continue already assigned independent work without
   waiting for Strategy to acknowledge the handback; new scope needs assignment.
5. **Review when the decision becomes useful.** A meaningful connected capability,
   material contract risk, observed costly branch divergence, or a consequential
   product conflict triggers the relevant review—not elapsed time or commit
   count. Strategy can review capability evidence asynchronously without a
   shared build. Combined runtime/acceptance work requires explicit Integration
   resume and a named implemented experience, affected surfaces and current tuple.
   No proof of one loop is required before whole-system design.

### Compatibility, landing and acceptance are different work

| Work | Trigger and owner | What it does not require |
| --- | --- | --- |
| Local implementation and verification | Package owner, throughout the assigned outcome; focused tests plus applicable owner/Task Intake evidence | Waiting for other packages, shared device access or a Strategy review after each commit |
| Interface compatibility | Changed producer/consumer contract or a usable dependency; the two owners plus the assigned shared-file writer | Restarting Integration, synchronizing all branches, or retesting unrelated surfaces |
| Ready for landing | A coherent tested cut with receiving coverage, exact revisions and remaining evidence limits | Both A/B being finished or a new whole-product design review; readiness is not permission to merge |
| Bounded landing | Explicit assignment to the landing owner; required coordinated `make verify` and applicable delivery gates | Automatically replaying the September 8 acceptance campaign; no tests required by an owner/release contract are waived |
| Combined product acceptance | A meaningful implemented cross-lane experience or identified system risk, with explicitly resumed Integration | Every historical branch or all six design projects being complete; unrelated engineering continues |

Avoid both extremes: constant assembly ceremonies and weeks of unexamined drift.
At a real shared change/handoff, check relevant ancestry, interface compatibility
and migration/generated-consumer effects; adopt only needed immutable cuts in
the lane's own checkout. Rising conflicts, mutually incompatible consumers or
blocked downstream work justify a **bounded** integration request. Do not turn
that risk check into a recurring all-repository cleanup or full acceptance run.
While Integration is paused, owners can establish readiness and exchange cuts;
this roadmap does not reassign landing, authorize merges or resume the lane.

Success is fewer broken consumer paths, stronger supported judgment, less
re-explanation/checking, and usable outputs—not commits, agents, tests or new
schemas counted. Measure cost/latency through existing telemetry. Do not add a
third package just to coordinate the two or restart all historical roadmaps.

### Design coverage without six implementation queues

The technical plan's [six-project design-to-capability map](complete-system-integration-roadmap-2026-09-05.md#six-project-design-to-capability-map)
connects the latest handoffs to A/B and named later work. Preserve substantial
Home/Places receiving, original-first social value, purposeful Life retrieval,
restrained Entity depth and practical care before disruption. Do not defer all
surface work because final layout details remain open, or interpret A/B as the
complete product. Select the next missing capability from that map when its
dependencies are usable; completing a central acceptance round is not a blanket
prerequisite. Pending policies still block their dependent implementation.

## 5. Consequential decisions and narrow dependencies

| Decision | Accountable proposer / decision | Work that waits; work that continues |
| --- | --- | --- |
| [Conversational continuity](conversation-history-source-expiry-decision-proposal-2026-09-06.md) | Strategy + Capture; founder adopts | New history-specific retention/later use waits; present help and already authorized retained-source use continue |
| [Pre-Plan intention](retained-intention-before-plan-decision-proposal-2026-09-06.md) | Components and Plan, reviewed by Life/Capture/Integration; founder adopts | New durable loose-intention writes wait; existing Plan, Source and read-only exploration continue |
| [Sharing source/audience contract](social-experience-implementation-roadmap-2026-09-07.md#103-decision-register--resolve-only-what-the-next-capability-needs) | Social with source owners/Life/Integration; founder adopts permission changes | Wider audiences, guests and new friend-source AI uses wait on their respective decisions, not all authenticated original receiving |
| Practical responsibility / live-family activation | Integration + existing action owners; Strategy/founder for promise or authority changes | New accepted watches/provider actions wait on signal, freshness, reevaluation, expiry/cancel and consequence contracts; supported current assessment continues |
| Capture → Life evidence | Candidate lifecycle option A is accepted and landed; Capture owns truth, Life consumes projections | Broader semantics and serving remain separate gates; the revision/delivery decision is no longer a blocker |
| Offer, coverage and payment | Strategy; founder adopts | New geographic/service promises, prices and allowances wait; cost instrumentation and useful free receiving continue |
| [Six-project design decisions](vesper-five-project-design-consolidation-2026-09-08.md#strategy-alignment-and-consequential-choices) | Entity/Places and Plans propose; founder resolves | Final purpose-responsive anatomy and seven-sentences assistance exception wait; exact identity/context transport, supported facts, readback and existing renderers continue |

Keep detailed alternatives and evidence in the linked proposal. This register
does not adopt them. A dependency request names missing fields/behavior,
receiving test and affected package—not “blocked on Life/Content/Social.”

## 6. Coordination, completion and next system review

### September 9 operating rule — longer slices, quieter coordination

One assignment is a **bounded product outcome**, carried through investigation,
implementation, consumer wiring, focused tests, self-review, repair and handback.
It is not “research first, then ask whether to implement,” one file, one commit
or one green test. Longer slices can span multiple coherent commits and context
compactions, but do not grant unlimited time, new product policy or new scope.
Package A/B each has its own outcome owner; neither wakes paused Integration to
obtain permission for ordinary local implementation.

**Dispatch mechanics:** set the destination explicitly to `gpt-5.6-luna` with
`xhigh` reasoning for each execution start/resume/steering call that supports those
fields. Do not trust the title or prompt text to configure the model. Record the
requested settings and observed effective settings if available; unavailable
readback remains unverified, never “confirmed.” Reports that start a turn in this
Strategy session use `gpt-6-astra` / `high`, not `minimal` or `none`. Those are
destination settings, not the sender's settings. If the selected API cannot set
them, choose a supported mechanism or surface that limitation—do not silently
fall back to medium. Model settings are independent of Fast service tier; current
thread-dispatch tools expose no Fast field. No global settings are changed here.
Official [Codex command guidance](https://learn.chatgpt.com/docs/developer-commands#built-in-slash-commands)
separates model/effort selection from Fast, whose availability depends on the
catalog. This document records our operating policy, not a runtime configuration.

**Give permission to finish ordinary work inside the package:** reproduce causes,
read adjacent owners, implement the bounded fix, update affected docs/tests,
regenerate contracts where required, repair regressions introduced by the change,
and self-review the complete diff. Commit coherent changes when the assignment
authorizes it. Do not stop at a normal technical obstacle to request the same
authority again. Exhaust relevant safe alternatives, then report the exact
dependency; continue independent in-scope work while it is unresolved. Do not
rewrite unrelated infrastructure or weaken checks to avoid a blocker.

**Contact another owner directly for a material dependency:** name the exact
field/behavior, proposed contract, receiving test, owned files and immutable
revision needed. Send one coherent request, not a sequence of corrections as
each thought occurs. A handoff is available evidence, not a new assignment.
Only the assigned writer changes shared files; agreement does not permit editing
someone else's checkout. Escalate incompatible contracts or competing priorities
here; do not route every technical question through Strategy.

**Cross-session messages are event-driven:**

- A usable interface/cut another active owner needs; keep working afterward.
- A consequential blocker requiring authority or a material scope decision.
- One implementation-complete or genuinely blocked final handback.

No acknowledgement-only turns, “tests passed, what next?” messages, per-commit
reports, repeated unchanged blockers or automatic ping-pong replies. The
orchestrator does not send “continue” merely because a substep finished; the
original assignment already authorizes the remaining named work. Batch review
feedback into one prioritized correction assignment. Necessary user-facing
progress updates within the execution session still follow its host instructions;
less cross-session chatter is not permission to hide failures or ignore questions.

**Long-run continuity:** keep the current state in one existing owner receipt or
the assigned package section: decisions, exact revisions, work completed, next
in-scope action, pending command/session and blockers. Update at meaningful
boundaries and before compaction/handoff, not after every command. On resume,
read it and verify Git; do not reconstruct the entire strategy history or restart
completed work. If usage limits or interruption end the run, report incomplete
work truthfully with a resumable next action; never claim completion to fit a budget.

**Stop for:** an unresolved authority/policy or consequential architecture choice;
overlapping file ownership that cannot be resolved; destructive changes outside
the assignment; paid/external activation without approval; or exhausted safe
technical alternatives. Stop only the dependent work unless the whole package
truly depends on it. No unsolicited nested lane expansion; any delegated helper
needs explicit authorization, independent useful work and the same model/effort
and ownership rules. Existing seeded-world model policy is a separate exception;
seeded-world acquisition is outside A/B.

### Reusable long-slice dispatch brief

Fill this into **one message**, with exact paths/revisions instead of placeholders.
Do not paste the entire multi-week thread or dispatch the template unfilled.

> Own package [A/B] through implementation, receiving-side tests, self-review,
> repairs and one final handback. Execution: Luna xhigh, explicitly configured
> by the dispatch call. Outcome: [person-visible capability and supported scope].
> Work in [isolated coordinated checkout], from [three repo revisions]; own
> [files/subsystems]. Read AGENTS, Task Intake, the program's §4/§6, the technical
> tranche's relevant package, and [specific owner/design contracts]. Preserve
> [already complete code]; implement [ordered missing behaviors]. [Other owner]
> owns [shared files/interface]; coordinate directly on [exact dependency].
> You may implement, repair, test, update affected owner docs and commit coherent
> local changes inside this package without another approval after each step.
> Do not change [pending policy/layout], start paused Integration, publish,
> activate production/provider work, retire broad legacy paths or weaken gates.
> Required evidence: [commands, real-owner scope, receiving and failure cases];
> local runtime/device ownership: [explicit allocation or unavailable]. Continue
> independent work if a dependency blocks. Communicate only actionable handoffs,
> consequential blockers and final completion; keep normal progress local.
> Review triggers: [specific shared contract/product risk or meaningful connected
> capability]. Do not pause for commit-count checkpoints, routine acknowledgement
> or another package's final report. Landing: [named owner and authorization or
> deferred]; combined acceptance: [separate scope or deferred]. Keep required
> compatibility and delivery checks; do not resume Integration by implication.
> Finish with [capability result, revisions, commands/results, evidence limits,
> unresolved decisions and precise receiving instructions]. A DTO, receipt or
> passing unit test alone does not finish the package. If interrupted, leave one
> resumable state record and report what remains rather than ask to start over.

### Outcome ownership and assignment

Standing lanes supply expertise; a package has one accountable **outcome owner**
who follows it through receiving-side verification, even when another lane owns
a dependency. Strategy owns priority, product coherence and consequential
decisions. Integration owns an explicitly assigned combined candidate, shared
runtime and landing; it need not implement every supplier fix. Crossing repository
or surface boundaries does not automatically transfer a package to Integration:
A/B retain their named outcome owners through consumer wiring and local evidence.

Use one consolidated assignment per round, recorded in the existing lane plan
or Integration receipt, with this compact agreement:

> Outcome and accountable owner; receiving owner and dependencies; exact repo
> bases and owned files; authority and exclusions; required behavior/tests and
> evidence level; handoff/checkpoint; escalation conditions.

The owner carries authorized work through diagnosis, implementation, focused
tests, dependency handoff and receiving feedback. Ordinary fixture/harness
repairs and bounded documented recovery do not require a new Strategy prompt.
Escalate new authority/product decisions, incompatible shared contracts,
destructive or external actions, or an exhausted technical alternative with
evidence and a proposed next option. Do not repeat an unchanged failing retry.
These permissions do not expand the package, weaken gates or authorize release.

### Independent files, serialized shared resources

Implement and test in isolated checkouts; simulator availability does not block
independent file work. Agree overlapping files, shared APIs/navigation/models
and receiving tests directly with the affected owners. Involve Integration only
for assigned landing/shared-runtime work or a risk requiring its decision. Only
Integration assembles supplier changes into the shared acceptance checkout;
this does not prevent an owner adopting an agreed dependency in its own lane.
An explicit bounded file handoff is possible when no inspection is running; a clean Git
status alone is not permission to edit another owner's checkout.

Before a resumed shared inspection, Integration records a **candidate tuple**
in its existing receipt: workspace/backend/app revisions, harness revision, dirty diff if any,
build, effective flags, dataset/identity and mock-versus-owner mode, API/Metro
origins, simulator, current operator and next recipient. Confirm the intended
surface and data path before a long run. Treat source, harness, flags and data
as stable for that inspection. A required change ends that candidate's run;
record the new tuple and rerun affected checks. Preserve earlier results at
their original scope; never silently carry a pass onto changed behavior.

Device release and result acceptance are different. The operator hands over
the tuple, evidence location and unfinished actions directly to Integration and
the next recipient. Integration schedules use or shutdown after confirming no
owner still relies on the runtime; emergency cleanup remains permitted with an
explicit interruption record. This is a small handoff, not a new lock service.

### Messages, evidence and reconciled closeout

Keep progress and raw attempts in existing receipts. Send messages for a usable
handoff, a material dependency change or a consequential blocker; do not start
turns for acknowledgement-only/status-only traffic. Strategy receives actionable
interface/decision requests and one reconciled closeout, not an obligatory report
for every substep or first green test. Necessary corrections may still be sent
mid-round. Destination model/effort follows this section; never infer it from how
short the message is. This policy creates no polling loop or automation.

For a resumed combined round only, Integration verifies before closeout:

1. Every participating owner has completed its handoff or is explicitly deferred;
   no late supplier change is being mistaken for the inspected candidate.
2. Final repo/harness revisions, staged/unlanded patches and relevant dirty state
   are recorded, with release and publication status separate.
3. Required checks are passed, failed, blocked, unrun or stale against that tuple.
   Tool crashes prove no app assertion. Fixture, owner-backed HTTP, native and
   reviewer evidence remain distinct; unsupported carry-forward is not a pass.
4. Each unresolved defect has an owner, next action and restart condition. A
   paused or failed round can close administratively without claiming acceptance.
5. Runtime/device ownership is released or explicitly transferred. Strategy
   synthesizes the combined result and the few decisions needed from the founder.

Keep proportionate tests and the existing coordinated delivery gates; do not
rerun every broad suite in every supplier lane or waive failures. Update one
existing package receipt at meaningful checkpoints, preserving necessary raw
evidence without creating a new document/commit for every message. Product
commits remain small and coherent. No new task board or meta roadmap is needed.

Use the next completed capability's existing handback to assess time from
assignment to working consumer, dependency waiting, avoidable redispatches,
integration/rework effort, invalidated runs and founder interventions. Do not
require a new tracking system or a synchronous meeting to record these. Use
actual timestamps/receipts (and the existing measurement tool for command timing);
do not claim faster delivery from fewer messages, tests or commits. Strategy
maintains this overview; owners maintain their detailed queues. Reassess product
direction when new capability evidence can change the next scope, or a material
conflict appears. The previous “at most three integrated packages” cadence is
superseded; no automatic pause or scheduled monitoring follows.

### September 9 offline baseline — completed

After the independent Home exact-original and Places cross-root replay slices,
the canonical backend's intended Python 3.13 environment completed the
repository-wide offline suite. From `travel-agent/`, `make test-offline`
selected **21,425 tests** after deselecting 1,427 cases; **21,358 passed, 14
skipped, 53 xpassed and 6 warnings** in 196.73s. Its follow-up concierge
offline subset passed **76 tests** in 2.84s. The command and environment are
valid baseline evidence for the canonical backend checkout, not a claim about
native/device, live-provider, production-database, Chat/Life serving or the
paused Integration candidate. The six warnings are retained as warnings; no
gate was weakened and no unrelated dirty workspace files were staged.

<a id="7-current-acceptance-round--dispatched-september-8"></a>

## 7. Historical acceptance round — dispatched September 8, now paused

**Superseded as an execution queue by September 9 §4.** The founder paused
Integration after this assignment. The scope and unfinished evidence below are
preserved, not waived; imperative “next” and “dispatched” language in this dated
record does not restart it. A future explicit resume must name a current tuple
and the implemented package being accepted, not blindly replay this whole round.

**Reconciled closeout and next outcome:** the inspected isolated tuple is clean
workspace `f3bd44b`, backend `4b30edeb2`, app `8c9422342`; the Life target repair
is `99daf978e`. Receipt `f3bd44b` reconciles the later Home report with Integration's
earlier closeout. Home reports a later 6/7 capture
with a quiet assertion failure; the earlier 7/7 pass is historical fixture
evidence. Places repairs advanced the flows but the final assertion revision
has no native pass. Life's 18 focused tests pass; XCTest failed before native
assertions after bounded recovery. Content is owner-backed at the HTTP boundary,
not native receiving. Runtime is reported stopped. These are execution/evidence
boundaries, not production acceptance. The newly dispatched package first fixes
candidate-generated status drift and genuinely stale test expectations, then
performs supported native or documented manual inspection on a stable tuple.
It must include actual owner-backed receiving (not just HTTP or mock postures),
fair same-area context comparisons, exact depth/original return and supported
Life valid/missing-target behavior. Integration may request bounded supplier
help without restarting whole lane roadmaps; one closeout returns to Strategy.

**First inspection is complete, not product acceptance.** Isolated receipt
`309b65e` records Home's 7/7 mock posture pass, Places' three failed paths plus
a Search-cancel shell anomaly, and Life's failed flow with a stale return
selector and a direct-row unavailable-record mismatch. The runtime was shut
down after inspection. Owner-backed corpus receiving is still unperformed.
Canonical children remain backend `a7c02cbe1` / app `e2e792913`; new supplier
patches and receipts remain isolated. This dated recheck found workspace
`118723b` with concurrent Home-design edits, which this round preserves.

The founder has now authorized repairs and combined acceptance. The header QA
pair `3c0ea94af` + `768f8bc5a` requires Integration review together, including
pending-versus-conformant audit summaries; three Life chrome decisions remain
pending, not waived. Home harness `2060afa31` and the prepared Content packet
are candidates, not evidence that current main passed native acceptance.
Social decisions remain here for founder review.

### Order and shared environment

1. **Integration restores the existing inspection tuple:** isolated coordinated
   workspace/children, exact commits, disposable local dataset, Compose/Expo
   ports, one exclusively assigned simulator, installed development build and
   registered design references. Read `--print-runtime` before startup.
   Document startup failures and disable unintended provider/background execution
   in the inspection environment through existing supported controls. Do not
   point tests or cleanup at the ambient development database.
2. **Home and Life implement the observed bounded repairs in parallel.** Home
   scopes search force-state, pins the supported urgency context, corrects the
   cold scroll/tap sequence and investigates missing navigation. Life repairs
   direct-row identity/return while retaining real missing-record warnings.
   Integration reviews/adopts the existing Content corpus through owner paths;
   no new Content research round is dispatched. Legacy booking/reflective
   fixture expectations must be reconciled with current authority, not restored
   indiscriminately or silently removed to make tests pass.
3. **Home inspects the combined candidate first, then Life uses the reserved device.**
   Use current supported serving for each; shadow results must be compared
   explicitly, not secretly substituted into product reads.
   Record mock-mode and actual owner-backed HTTP receiving separately. Device
   order may change by explicit Integration handoff if repair readiness differs.
4. **Stop for system review at corrected native flows plus first owner-backed
   receiving.** Review useful full-scroll material, exact depth/original return
   and supported Life continuity. Do not invent a persistence mapping merely
   to join the evidence. Verify and land reviewed small packages under existing
   gates; report blocked seams explicitly and reassess after at most three
   integrated subpackages. No deadline or daily-use target is implied.

### A. Home and Places: worthwhile populated receiving

**Person's outcome:** open the app without a new question and receive useful
understanding, possibility, practical help or an authorized human contribution;
open appropriate depth and return without reconstructing context.

**Data and acceptance portfolio:** use the same bounded supported area and local
corpus for three situations: sparse/no Trip; richer authorized context without
a Trip; and a changed practical condition or purpose. Include an eligible
original human contribution under the existing adopted sharing contract.
Use enough materially different material to assess the whole scroll, not a
fixed card count or one mandatory unit per product move.

Content supplies provenance, retrieval time, claim-level evidence, permitted
use, canonical identities, revisions and freshness to existing owner admission.
Use reviewed public sources and deliberately authored test-person context;
do not reuse real private histories without authority. A locally populated
record based on real research is still local evidence, not production coverage.
Public web research/local deterministic admission is in scope; paid API/model
generation, ambient ingestion, broad seeded-world batches and production writes
require their separate approval. Missing coverage becomes a named supply gap,
not filler or another input prompt.

**App inspection:** Home and Places full scroll, first viewport, exact content
and source depth, Back/return, long copy/text sizing, stale/withdrawn content,
empty supply and unavailable requests. Compare registered current design
references, not a screenshot of a whole Claude board. Explain differences
between the latest design export and registered authority before an intent
verdict; do not silently bless an old bundle or promote a new export.

**Pass / revise / stop:** the received contribution is specific and supported;
the page offers materially different value without redundant prose or chores;
current purpose can matter without a Trip; independent value survives expired
practical claims; exact identity and return are maintained. Equal sparse/rich
answers are acceptable when context adds nothing. Reviewer judgment is recorded
as judgment, not measured consumer enjoyment. If data never reaches the app,
the package remains incomplete even when its adapters pass.

No root redesign, new card taxonomy, Home generator, mandatory Keep/Plan, booking
execution or Chat redesign follows. `open_now` is not arrival feasibility:
existing live-engine owners must supply any stronger practical conclusion.

### B. Life: recognizable continuity and exact originals

**Person's outcome:** locate an entrusted item naturally through relevant
time/place/group views, recognize why it is there, open its original and correct
it without maintaining an inferred biography.

Use existing supported Sources and confirmed candidates with an original,
explicit Place relation, uncertain/late capture time, neighboring records and
a deliberate exclusion. Exercise correction, withdrawal and explicit restoration.
Include Plan/Occasion/shared records only where their current owner supports
them; do not fabricate social refinding or occurrence/people evidence.

Compare three stages: authoritative record, maintained shadow organization and
current app reader. Name exactly what the user can and cannot currently see.
Inspect whether labels, ordering, grouping, previews and original-return paths
help recognition; count/replay correctness alone is not acceptance. Preserve
unknowns and distinguish capture time from occurrence time.

Life owns consumer/organization improvements justified by the comparison;
Integration owns shared reader contracts and schema synchronization. First
checkpoint is a record-to-reader trace plus actual-app inspection of supported
reads, and a concrete gap list for shadow-only outputs. If visibility requires
a serving change, prepare a bounded cohort/parity/rollback/repair plan for
founder review. Do not activate indexed serving or retire Atlas merely to get a
screenshot. An explicitly labelled internal comparison is not shipped Life.

### C. Social: decision review, not another implementation round

Use the existing isolated packet `43ae39a` + `bb23e89`, not another research
document. Strategy presents consequences and recommendations for five decisions:
recipient snapshot, disconnect/block old access, clear/release/withdraw,
caption edit versus replacement/new audience, and friend-source AI
purpose/retention. Original-first receiving remains complete without AI or reply.

Keep distinct internal controls without making three equal removal choices a
routine user task. A recipient's Ask cannot grant the sender's source-use rights.
Founder adoption must name the permitted consumer/purpose/retention boundary.
The candidate lifecycle ADR does not approve any of these choices.
After adoption, Social receives one original-receive → optional continuation →
authorized refind → sender-control package. Until then current bounded human
receiving can be inspected independently.

### Native evidence and closeout

Use the app's existing surface QA registry, contracts and verdict protocol:
scenario validation, canonical design check, surface doctor, capture,
comparison and structured verdict. Resolve actual Home/Places/Life surface IDs
from current contracts; compatibility Trip/Atlas captures are not substitutes.
Reserve one simulator; record build, environment, dataset, route, reference
hashes, screenshots and executed navigation. A doctor failure gets a concrete
repair or exact blocker, not permanent native deferral. Dry runs produce no
native evidence; manual fallback needs the documented screenshot receipt.

Report separately: implemented, locally integrated, owner-connected,
native-observed, reviewer-assessed and release-approved. Retain focused tests,
real-backend parity where affected, schema/API checks and current delivery
gates. Known failures stay explicit; do not bypass a gate or sum overlapping
tests into a journey claim. Record timing with the existing measurement tool;
include known/unknown source and generation costs.

The next shared review asks: what was worth receiving; what context actually
improved; how much input/navigation/reconstruction remains; what did correction
change; and which owner must fix the limiting gap? Choose continue, revise or
retire per package. No automatic monitoring, paid execution, deployment,
publication, production Source activation or Social policy expansion is
authorized by this plan. Historical dispatches and receipts stay in Git and
existing lane records; this overview owns only the current sequence.

## September 20 functional implementation receipt — Places public Source readings

The next Home/Places supply seam is now implemented in the isolated functional
lane. Places Reading doors can carry either the retained dossier identity or an
exact accepted public `place_content_primitive` Source plus its canonical Place
subject. When the existing primitive-read and `app.place.detail` control-plane
flags are enabled, the Reading producer reads bounded current public Sources
through `list_current_public_place_content_sources`, projects only claim and
interpretation metadata into the existing reading card, and sends selection to
the already-supported exact Place owner read. No generator, provider, second
content store, personal-history inference or new card family was added. Legacy
dossier reading behavior remains compatible and the default-off gates remain
unchanged.

The mobile root card and Reading collection preserve the Source revision/entity
identity and open `/place/[placeSlug]` through the existing exact-reader route;
stale or malformed selections still fail closed. `places_card_resource_ref` and
the shared value requirements recognize the Source owner rather than treating it
as a dossier. Focused backend Places/Home coverage is **66 passed**; the focused
mobile Places/route/object suite is **397 passed** and TypeScript passes. The
standard projection command remains blocked by the repository's pre-existing
expired API-policy entries and one unrelated intake-media missing-consumer
finding; derived snapshots were refreshed for this additive schema change using
an explicitly temporary local policy copy, with the committed policy untouched.

This is a committed candidate, not live populated supply, native visual
acceptance, disposable-Postgres evidence, merge/publication or rollout
activation. The next package should exercise this Source-backed reading with a
real accepted record in the combined runtime, then choose the next uncovered
Home/Places or bounded social-receiving seam. Do not widen the primitive feature
flags or add a new generator/store as part of this package.

## September 21 functional implementation receipt — Home child-entity public supply

The next narrow supply gap is now closed in the same isolated functional lane.
Home's sparse public-content reader previously asked the Source adapter for
exact `place` rows only, even though the canonical place-content owner already
supports bounded parent→venue/site/accommodation/experience membership. The new
`list_current_public_place_content_sources_for_places` adapter uses that
existing structured owner read, then re-applies represented-clock eligibility,
public/root admission, version deduplication and the existing Home candidate
adapter. Child-owned readings therefore retain their exact child EntityRef and
Places continuation instead of being dropped or relabeled as a container.

No provider, generator, semantic index, new store, schema, card family or
personal-history inference was added. The exact-entity Source listing remains
unchanged for callers that intentionally ask for one owner. Focused backend
Source/Home coverage is **65 passed** (including the child-source continuation
regression); Ruff, format and backend hooks pass. The implementation is backend
commit `1de6fa954`, with test follow-up `2fbf828e6`; app behavior and the
existing generated contract are unchanged.

This remains local candidate evidence: the accepted database rows, combined
runtime, native visual receiving, merge/publication and rollout flags are not
proven. The next useful check is a real admitted child-owned Source through
Home → exact Places reader → return, followed by reassessment of the bounded
social-receiving seam. Do not broaden the child enumeration beyond the existing
eight-anchor/owner-read bounds or turn it into acquisition.

## September 21 functional implementation receipt — native shell checkpoint

The lane completed a bounded native checkpoint against the current four-root
shell. The installed simulator build initially crashed before rendering because
its local `node_modules` contained `react-native-worklets` **0.11.4** and
`react-native-reanimated` **4.5.3**, while the committed lockfile requires
Worklets **0.12.1** and Reanimated **4.6.0**. Running the lockfile-preserving
`npm ci` in `travel-app/` repaired the local dependency/build mismatch; no
source or dependency manifest change was needed. A second launch reached the
native app without the Worklets crash.

With the existing opt-in flags enabled locally (`FOUR_ROOT_SHELL`, root
projection v2, Places renderer v2 and Life root/refind flags), the simulator
opened the current Home root against the lane API. The screen rendered the
owned-state admission result — “No owned current state clears Home's admission
threshold” — and the Home/Chat/Places/Life navigation shell. This is real native
reachability and empty-account behavior, not a fixture screenshot. A direct
deep link with the runtime mock override disabled also reached the real API.

The same checkpoint exposed and repaired a route-registration defect: without a
nested Life stack, Expo Router surfaced the tab as `life/index`, ignored the
configured Life title/icon and logged that no `life` route existed. App commit
`3c23c2116` adds the minimal `life/_layout.tsx` stack, after which the native
tab renders as **Life** with the configured icon. The route contract tests
(three suites, 10 tests) and TypeScript check pass.

This receipt does **not** claim populated native receiving, production flag
activation, Home→Places→Life return, visual parity with the Claude references,
or release readiness. The temporary API user and local services are disposable
and must be cleaned up after the checkpoint. The next useful native package is
one admitted, bounded dataset that visibly exercises a populated Home item,
its exact Places destination and a Life refind/return path; do not alter the
production defaults or add another shell to obtain that evidence.

## September 21 populated Home → Places → Life native checkpoint

The bounded follow-up dataset was exercised through the real lane API and the
opt-in native shell. It included one recipient-consented venue-bound
`place_pull`, its canonical New York venue destination, and one retained Life
source with a confirmed current owner revision. The first Life replay correctly
failed closed on a stale revision; a fresh `source_verified` event and the
existing outbox repair path then produced the September organization group.

The API returned **200** for Home v2, the exact venue reader, Life v1, and Life
organization groups. Home contained the exact `people_note_door` note from Maya,
venue id `35` and the Places destination ref. Life contained the retained
`source_submission` and `derived:period:2026-09:iana.utc` group with matching
source revisions.

With `EXPO_PUBLIC_IS_INTERNAL_BUILD=true` and the existing opt-in flags, the
simulator rendered the populated Home note and **Open in Places →**, the exact
`Runtime Garden Table` destination reader, and the populated Life Time lens with
one retained record. This is the first connected native receiving receipt for a
real accepted bounded dataset. It is not a tap/back return proof, full corpus or
multi-lens proof, broader social/group-media support, production activation,
Claude-design parity, or release acceptance. The temporary data and API/Expo
processes must be cleaned up after the capture. The next useful work is the
native return/refind interaction or another supported receiving gap; do not
widen the content model or add a second generator/store.

## September 21 functional implementation receipt — explicit place-bound Life sources

Life's Places lens now admits a retained source only when Capture supplies an
explicit, currently resolved place-like subject (`place`, `venue`, `site`,
`accommodation`, `experience`, or `transport_hub`). The canonical Life adapter,
the compatibility intake page, and the retained-source shadow projector share
one subject policy. The source remains a private `source_submission` door and
opens the exact Intake submission; its place reference is carried as
represented lineage, but the read does not claim attendance, occurrence, or a
semantic interpretation. Sources without an explicit place subject remain
Time-only. This makes the product's combination of time + place concrete
without inventing a visit from a photo, note, or capture context.

Backend commit `b3c832c40` adds the behavior and regression coverage. Focused
Life projection tests pass (**41 passed**), and the adjacent corpus/index
regressions pass (**25 passed**); Ruff, format, vulture and repository hooks
pass at commit time. No schema, API wire contract, or mobile production surface,
generator, provider, or new store was added; app commit `81e876156` adds the
focused Life-root Places-source handoff regression. The broader Life route suite remains bounded
by the existing local environment: its Postgres/API collection requires
`TEST_DATABASE_URL` and the optional `openai` dependency, so this receipt is
unit/contract evidence rather than populated database or native Places proof.

This is intentionally a narrow adoption seam, not generalized place
inference. The next verification should seed one accepted place-bound retained
source and prove Life Places → exact Intake source navigation in the combined
runtime; only then should we choose the next receiving/action seam. Do not
promote capture-time subject association to occurrence evidence or widen the
supported place taxonomy without an owner contract.

## September 21 functional implementation receipt — retained-source revision repair

The first disposable-runtime replay of the new Places adoption exposed a
cross-timezone CAS defect: Postgres returned an owner timestamp with the local
session offset while the evidence adapter serialized the same owner revision in
UTC. The retained source was therefore rejected as `source_revision_mismatch`
before either its period or explicit-place organization could materialize.
Backend commit `d46b5150c` centralizes retained-source owner revision
serialization in UTC and uses that token consistently in the source record,
Life adapter, shadow index, and evidence handoff.

After the repair, a current-authority read of the disposable place-bound source
compiled both `derived:period:2026-09:iana.utc` and `owner:venue:22942` groups
with no rejected evidence, and the worker published the retained-source event.
Focused Life coverage is **42 passed**, the Postgres projector packet is **4
passed**, and the earlier corpus/index packet remains **25 passed**; Ruff,
format and repository hooks pass. App commit `81e876156` covers the native
Life-root handoff to `/you/intake-submissions/[submissionId]?lifeLens=places`.

The full HTTP/native route proof remains open: this disposable API request
entered the existing Atlas timeline reader and hit a pre-existing fallback-user
projection failure, so no route or simulator parity is claimed. All temporary
users, venue, submission, source and outbox rows were removed and the API was
stopped. The next package should repair or explicitly bypass that unrelated
Atlas fixture boundary for a clean Life Places → exact Intake → return proof;
do not weaken Atlas authority or widen the new source policy.

## September 21 correction — combined Life Places route proof

The earlier HTTP boundary was a dev setup error, not a Life or Atlas behavior
failure: the probe process used a configured user id that was absent from the
disposable Postgres database, so auth fell back to the synthetic
`00000000-0000-0000-0000-000000000005` identity and Atlas correctly rejected its
foreign-key write. A clean retry created the configured temporary user in the
same database, seeded one verified `photo_library` source with an explicit
venue subject, registered the existing retained-source projector, and repaired
the outbox event.

The real `GET /api/root-projections/v1/life?lens=places` returned **200** with
one private durable `source_submission`, the explicit venue in
`represented_refs`, and the exact `/you/intake-submissions/[submissionId]`
destination. The entry remained `pending` (the existing custody state); no
attendance or occurrence claim was added. This closes the combined backend
route boundary for this narrow source case. It does not prove a physical
native tap/back return, populated multi-lens corpus behavior, production
activation, or visual parity. Temporary users, venue, source, outbox rows and
API process were removed; no advisory locks remain. The next package is the
native return/refind proof or another supported receiving/action seam, not an
Atlas workaround.

App commit `60da1cbe0` now covers the corresponding native return contract:
when the source is opened with the Life origin and `lifeLens=places`, its
return action dismisses to the exact Places-lens Life record rather than a
generic Life surface. The focused Intake/Life packet passes **29 tests** (with
the existing non-fatal `act(...)` warnings from the original-preview async
fixture).

Backend commit `f518d6e22` adds the route-level regression for the same
contract: a retained source with an explicit venue subject is emitted in the
Places lens as a private `source_submission`, includes the venue in
`represented_refs`, and points to the exact Intake submission. The focused Life
route suite passes **26 tests**.

## September 21 E2 repair — source-backed Places reading depth

The Places adapter had a narrower exact-depth gap: a source-backed editorial
card preserved its immutable `place_content_primitive` ref but dropped the
reading's canonical Place subject. Its native destination could therefore
fall back to the generic Places root even though the Home/Places contract had
promised an exact reading. Backend commit `fbc1fa018` preserves that subject in
represented refs, value-contract subjects, and the typed destination resource
set. Legacy dossier cards remain unchanged.

Evidence: the focused Home/Places backend packet passes **72 tests** and the
native root-navigation packet passes **44 tests**. The existing client resolver
now receives both the exact immutable reading and its Place area, so it can
open the Place reader with the reading source and preserve the originating
return token. This is a bounded receiving repair; it does not add a content
store, provider, generator, or new route family.
