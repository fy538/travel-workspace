---
doc_type: working
status: active
owner: founder / Strategy task
created: 2026-09-07
last_verified: 2026-09-22
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

**September 22 rebaseline, after implementation and review:** Vesper has moved
from mostly subsystem and route work into connected feature implementation,
but remains a partially complete internal product candidate. Existing owner
material can now reach Home and Places as readings, comparisons, social
perspectives and practical options; selected material can be opened, acted on,
and returned to its exact owner-backed record. Life can refind retained
records and supported photo/text/audio originals, open an explicitly associated
Place, and restore its anchor on return. Intake v2 admits supported audio, and
Life's Intake original reader now plays verified retained MP3/M4A/WAV audio
after an explicit tap, using the existing authenticated GET and custody checks
(app commit `93a9090de`). Actual secured media bytes and native codec playback
remain unverified on device. PDF is not a missing reader path: Intake
intentionally rejects PDF uploads until its scanner/decoder lane exists. Named
database/API/native paths support parts of this
experience. They do not establish broad design coverage, worthwhile recurring
supply, general later-context benefit, production activation or release
readiness. The fixed fictional Home example is only a cold-start fallback; its
native presentation and live retirement have not been observed on a device.

The bounded Home → Places addressed-note continuity gap is now implemented in
the isolated candidate. Home passes the selected handoff ID/revision into the
canonical object route; the relationship owner reads that exact revision; and
the page opens only that line or reports it unavailable. It does not depend on
the entity page's incidental three-line list and never substitutes another
friend's note. The change completes the product path in code without adding a
social model or sharing surface.

The latest backend slice now admits the existing saved-Place change family
into Home: permanent closure, confirmed reopening, and a weather window.
Their source-owned label and explanation appear only when the notice resolves
to the exact canonical venue, as a private, read-only Place doorway. The Places
`CLEAR` action is never carried over, and unknown or mismatched notices are
withheld. This completes one existing receiving family, not Home's broader
content composition or coverage.

A further September 22 backend increment lets a recent explicit Place save
receive a current, accepted public reading in the same Home seat as its generic
save doorway. Home preserves the reviewed source and exact Places destination;
the ordinary save remains when no eligible reading is available, and an
already-present current-context reading is not repeated. A save is used only
as an explicit continuity signal, never as inferred taste. This adds one
source-backed Home value path, not broad composition, personalized taste, or
new generation infrastructure.

The September 22 Home → Places social continuation is now connected as well.
An existing `Addressed to you` Home region receives a final “From friends in
Places” door only when the same current Places read contains at least two
distinct trip-shared `friend-save` cards; addressed handoff notes already
represented on Home do not inflate that threshold. The typed destination
retains the resolved Places context and Home's semantic return token. Places
scrolls its existing Friends section into view without changing server section
order, and a fresh read with no such section simply remains an ordinary Places
feed. This reuses the existing Places/relationship owner and does not add a
social model, store, feed, or inference. Backend Home portfolio tests pass
**59**; the focused app route/workspace/feed packet passes **117** tests, source
and test TypeScript checks, targeted ESLint, and Places docs checks. No live
account read or device acceptance was run for this change.

The follow-on notification convergence gap is also closed in the app: a
foreground notification receipt or provider-drop recovery invalidates Home's
existing owner projection as well as Activity's notification cache. An active
Home can refresh in place; Home reached later can refresh on focus. This does
not record a read/seen action, navigate, or add a second banner. Focused
PushRegistrar (**15**) and Home root-invalidation (**3**) tests plus app
TypeScript pass. Native push delivery/device acceptance remains unverified.

The fixed Home ticket sample no longer sends its “Try it with your own ticket”
action to a blank Chat. That exact Home-owned sample source opens the existing
private Chat with an editable, unsent request and a seed that labels the Home
example fictional; another source or non-Home handoff cannot receive this
special treatment. The seed is attached only when the person submits, and the
one-shot draft/context is cleared only after transport acceptance, so a
declined send can be retried. Focused route/composer/seed tests pass (**73**),
as do the existing backend seed-context packet (**44**), app TypeScript and
app docs checks. App lint has no errors and one existing Chat-file max-lines
warning. Native screenshot acceptance remains unavailable: Metro is not
running on `:8081`, and Home still lacks a registered design-ref manifest. This
closes the sample's destination-and-context seam, not the user-provided ticket
interpretation or end-to-end device behavior.

**Home implementation map:** `build_home_portfolio` already reads ten bounded
sources (up to six concurrently, a 900 ms deadline per source, and up to 24
items per source),
and the ordinary Home composer can merge a current, private, prepared Source
contribution into those owner candidates without generating or enqueueing work
on the read. The candidate set then enters the existing posture/selection and
four-region presentation path; the app has 18 explicitly promoted semantic
Home renderers. This makes the next gap composition and worthwhile supply, not
a missing generic generation service or a renderer-per-section exercise. Trace
each intended design section to its existing owner, candidate, selected region,
rendered value and exact return; only build a new producer or semantic kind if
that trace demonstrates a real unsupported user outcome.

**Historical Home → Places friends-continuation tuple:** workspace `0138f2a`,
backend `60da1dcb9`, and app `d021488be`. Its 59 backend Home-portfolio and
117 app route/workspace/feed test results remain evidence for that earlier
slice, not the current checkout.

**Current isolated candidate tuple:** workspace `eea903b` (latest
roadmap-only checkpoint; product code is unchanged from `0fe8e88`), backend
`4357d1320`, and app `93a9090de`, all on
`codex/functional-implementation-2026-09-20`. The workspace, backend, and app
trees are clean. Backend
`4357d1320` adds real-Postgres Home HTTP acceptance for the saved-Place path;
its predecessor `18e1fb377` implements the bounded source-backed reading.
Backend `2d0721e67` scopes Home child-source fixture cleanup to the run that
owns the fixture, avoiding restoration of a profile snapshot by an absent or
concurrent run. The audio reader is committed in the app and adds no backend
operation. Offline OpenAPI export reflects the current backend source; app
projection remains blocked by 55 existing expired API-policy reviews. There is
no new `HEAD` operation or missing-consumer finding. Canonical main and its
unrelated working-tree changes remain untouched; see §2 for exact status and
evidence boundaries.
Prior focused evidence includes backend selector/portfolio **68 tests** and
backend seed context **44 tests**; Home renderer **12**, Home screen **17**,
PushRegistrar **15**, root-invalidation **3**, and route/composer/seed **73**
app tests; app TypeScript; app docs headers/links (**9 / 288**); and workspace
docs-link validation (**499** living Markdown files). Targeted ESLint reported
no errors and the existing Chat-file max-lines warning. No live-account read,
native push/device acceptance, or Home visual-parity acceptance ran. The latest
notification change only invalidates Home's existing owner projection after
foreground receipt/provider-drop recovery; it does not add a banner,
navigation, or a synthetic seen action.

Earlier acceptance remains useful but is not current-tuple evidence. On app
`9a4c029e3`, the exact Home → Place → Keep → Home route had native acceptance
on iPhone 16 Plus / iOS 18.2: it opened only the selected note, kept it,
observed the relationship owner's revision advance from 0 to 1 and an exact
reread at revision 1, returned to Home with the handled unit removed, and
cleaned its disposable fixture. That device receipt was not rerun on this
tuple. App `9a4c029e3` also added the negative sibling-note case: if the
selected handoff is absent but another person's line remains, the page reports
the selected note unavailable and does not substitute the other line. Its
`ObjectPageRebuild` suite passed **24 tests**, recipient owner-read invalidation
passed **4**, and TypeScript passed. The earlier app baseline `a4de82802` only
changed the Home sample caption to a readable Design Language token; its
focused Home renderer suite passed **12 tests**, TypeScript and targeted ESLint
passed. These remain regression/focused checks, not a new device rehearsal.
The registered Home-root native capture remains the earlier single mock-fixture
posture at app `6ae89c427`; it is not broad Home acceptance or design parity.
The current visual QA doctor could not run because Metro was unavailable at
`:8081`, so no current-tuple screenshot was captured. Withdrawal/expiry for the
selected note remain unproven. Workspace `2fe00cc` also corrects the Source workflow
recovery description: the existing worker sweep is scheduled, but process
restart and live transient-provider retry remain unproven. The [code review
ledger](functional-implementation-code-review-2026-09-21.md)'s **11 confirmed
findings are code-fixed**; remaining R05/R09 matrices and R02 cohort/release
and R06 deployed-scale evidence are acceptance gaps, not known uncorrected
defects.
On 2026-09-22, workspace `make docs-check` still fails on one unclassified
existing document (`docs/working/practical-judgment-producer-acceptance-brief-2026-09-09.md`)
and three expired compatibility entries (`discover-url-bridge`,
`atlas-tab-url-bridge`, `discover-map-api-bridge`); the status renderer also
cannot run while that inventory is invalid. Other listed docs checks passed.
This slice does not touch those owners. Standard pre-push findings were last
recorded as 55 expired API-policy
reviews, 59 expired schema-bridge exceptions, and 12 query-key ownership
findings; `make verify` has not been run against this exact tuple. These are
local candidate commits only—not merged, published, rollout-enabled, or
cleared through standard gates.

Backend commit `ee625b985` also closes a bounded Home projection defect:
long-authored Outcome meaning is now a compact excerpt, while the exact
revisioned Outcome and existing `life.read` requirement remain intact. Life
continues to own the complete authored meaning. This prevents a valid record
from overflowing Home's bounded candidate fields; it does not add a new source
reader, widen authority, or establish broader Home value coverage.

Backend `8ab3313b8` then corrected the Outcome door in both current and
compatibility Home projections: it now targets Life's exact
`/you/life-record?record=outcome.<id>` reader instead of Life's generic root or
the retired memories route. The existing Home-origin return token is preserved
by the app's route helper. App commit `a7f0083cc` adds a focused Life reader
regression confirming this exact key selects the Outcome row rather than the
missing-target state. Together, the route-helper and reader-component suites
pass **61 tests**. A later native receipt below closes the exact Home → Outcome
Life record → Home return path for the current candidate.

Use [§2](#2-inspected-baseline--september-22) for the current evidence boundary,
[§4](#4-current-package-register) for the sole current execution queue, and
[Integration §9](complete-system-integration-roadmap-2026-09-05.md#9-current-execution-ledger-and-next-batch)
for implementation scope and finish conditions. Older dated receipts preserve
their results, limitations and rationale; their embedded "next" instructions
are historical and do not form additional queues. Update these summaries when
a substantial package finishes instead of appending a competing next step.

**Next emphasis:** stop closing the same transport seams and build more of the
product people are meant to use. Home now receives all three currently
produced saved-Place change types through one exact, private Places continuation;
they are not city-scoped World Facts. Home already has a native, owner-backed
three-family full-scroll receipt (September 21); the Places World Field also
has an integrated native full-scroll receipt (September 22). The primary
package is therefore not “make the first Home full scroll.” It is to make Home
broader and more design-aligned: map the current Home composition contract and
design handoff to actual producers, projection kinds and renderers; identify
which useful sections are already supplied, which are not presented, and which
are genuinely unsupplied; then implement a coherent set of supported missing
composition and presentation together. Carry the received material through
source, exact depth/action destination, return, honest sparse/error behavior,
accessibility and polished native hierarchy. Do not reduce this to another
isolated card, repeated fixture scroll or acceptance-only increment. The fixed
Home example remains a cold-start fallback, not recurring supply or a varied
personal portfolio. A permissioned Life/social downstream result remains a
complementary package where structured inputs and authority already exist;
environment-dependent evidence does not serialize that product work. Do not
add a generator, feed or storage family to manufacture fullness. The exact
addressed-note withdrawal/expiry cases remain closeout for that route, not the
next product milestone. Focused tests and a real design-reference/polish check
are part of each build package, not a separate phase in place of
implementation.

**September 22 refinement:** the bounded Places World Field is now integrated
in the functional candidate, the server-elected ordering seam is fixed and
covered, and the combined native full-scroll passed on iPhone 16 Plus / iOS
18.2. The flow showed one Source-produced lead with public reading,
recipient-consented social input, a saved-place change, and a retained Place in
the same scroll; fixture cleanup and temporary-account erasure both verified.
This closes the Places candidate-adoption and named runtime acceptance step,
not comprehensive visual parity, recurring supply or release readiness. The
registered mock `places-search-loading` assertion still fails before
screenshot capture, and external design-canon comparison remains unverified.
Home's existing native three-family scroll does not yet establish the broader,
design-aligned Home composition or its cold-start sample presentation. The
next substantial build is that Home composition breadth; do not rebuild Places
or restart a two-surface redesign.

**September 22 Home presentation correction:** the native renderer now keeps
coherent secondary compositions—prepared possibilities and alternatives,
authored regions, and editorial reading previews—visually contained as
recognizable objects. Plain reading passages and findings remain uncontained.
This aligns card treatment with the accepted Home composition contract while
leaving selection, supply, owner authority and payload families unchanged. The
focused renderer suite passed **12 tests**, TypeScript passed, and the
registered polish-scenario inventory reported **31 scenarios**. App commit
`6ae89c427` was then captured by registered native flow
`20260922T095658Z-home-root` on iPhone 16 Plus / iOS 18.2; its manifest records
that exact revision. The screenshot review showed the reading preview as a
secondary contained object beneath the prepared route. This is evidence for
that fixture posture only—not a complete Home scroll, cross-posture acceptance
or Claude-design parity. Targeted ESLint reported **0 errors** and the existing
Home renderer max-lines warning. The broader design-aligned Home composition
remains the primary build.

The renderer ledger was rechecked against the current candidate: the Home
transport union is 36 kinds, with 18 explicit Home semantic renderers plus the
three chrome components; Places has 12 explicit semantic renderers. The
previous coverage audit's 17-kind count and its claim that several now-rendered
forms remain dark were stale. The combined
focused Home/Places packet preceding the latest recipient-action change passed
50 tests; the action follow-through adds its own 4/4 owner-action tests, 3/3
runner-contract tests and native/API acceptance. This closes documentation
drift that had called several already-renderable kinds "dark"; it does not
claim source admission, recurring content supply, broad runtime full-scroll
quality or design parity. See the [renderer coverage audit](home-places-renderer-coverage-audit-2026-09-05.md).

**Inspected product-code tuple before this documentation update:** workspace
`1d9264d`, backend `fd80c437e`, and app `a4de82802`. The documentation-only
workspace commit `8d9730c` records the preceding rebaseline; dated snapshots
below remain historical receipts, not the current product-code tuple.
The native Home-selected Place-note Keep path and Home Outcome → Life record →
Home return were proven on iPhone 16 Plus / iOS 18.2 on their named earlier
candidate revisions; neither was re-run on this tuple. The current focused
Home renderer and Source recovery tests, TypeScript and targeted ESLint passed;
the visual doctor was blocked by Metro not being available at `:8081`. Do not
inherit earlier device evidence as a fresh full-tuple run. The fixed Home
sample's live presentation/retirement, selected-note withdrawal/expiry,
comprehensive visual/device acceptance and exact-tuple `make verify` remain
unverified. None of these commits is merged to main, published, or
production-flag activated. Earlier receipts document the exact Outcome Life
door and excerpt bound, Home/Places scrolls, Life readers/refinding, and
explicit Life → Places return; retain their individual evidence boundaries.

### September 22 backend robustness receipt — bounded Home Outcome preview

Backend `ee625b985` bounds authored Outcome meaning before it enters Home's
`RootDirectState`: whitespace is normalized and the excerpt is capped at 220
characters. The candidate's internal `material_trigger` is now static rather
than duplicating unbounded authored prose. The exact revisioned Outcome ref
and existing `life.read` requirement remain the door to the complete record;
no route, schema, UI, source-inspection handle, or authority policy changed.

Focused backend evidence: the v2 contract plus semantic-composition packet
passed **46 tests**; the Home portfolio packet passed **51 tests**. Targeted
Ruff checks and formatting checks passed. No database, API server, native
device, or full `make verify` run was part of this slice. This is projection
robustness, not new Home content supply, visual acceptance, or design parity.

### September 22 implementation receipt — exact Home Outcome → Life record

Home's graph candidate, returned-state orientation, and compatibility Home
compiler now emit `/you/life-record?record=outcome.<id>` for an Outcome's
revisioned `ResourceRef`. This is the route Life already uses for the stable
`outcome.<id>` record key. The app's existing resource resolver recognizes it
as an exact Life destination, and Home's resource-open path adds its normal
origin/return token. The generic `/owners/outcome/{id}` and retired
`/you/memories` forms no longer strand this Home door at the Life root.

Evidence: the focused backend Home/composition/compiler packet passed **110
tests**; app commit `a7f0083cc` adds an exact Life reader target-selection
regression. The root-navigation and Life reader component suites pass **61
tests combined**, covering exact Outcome routing, return-token propagation,
and selection of the keyed row rather than a missing-target state. Ruff,
formatting, and backend commit hooks passed for the backend change. No
API/database/native tap-and-back rehearsal or full `make verify` was run. The
reference and local reader selection now agree; the runtime return experience
still relies on the existing root-navigation contract and remains unproven end
to end on device.

### September 22 native receipt — Home addressed note → exact Place → Keep

The exact addressed-note continuation is now exercised on a native iPhone 16
Plus / iOS 18.2 simulator. The flow opened the Home-selected handoff in its
canonical Place, showed only that exact note, performed Keep, observed the
relationship owner's revision advance from **0 to 1**, reread that exact note
at revision 1, then returned to Home where the handled inbox unit was gone.
The disposable fixture was cleaned after the run. The runner passed; the
focused `ObjectPageRebuild` suite passed **23 tests**, and the runner-contract
suite passed **4 tests**. App TypeScript and shell syntax passed; targeted ESLint
had **0 errors** and 14 warnings matching existing patterns. The earlier
disposable-Postgres owner-read test passed **1 test** and dropped its database.

This closes the named native Keep/owner-read/return path. It does not prove
withdrawal or expiry behavior on a Home-selected note, the fixed cold-start
sample's presentation or retirement, visual parity, broader design coverage,
standard gates, merge, publication or release readiness. The exact-note action
is a continuity capability—not evidence that the overall Home experience now
has sufficient value depth.

### September 21 current-candidate integrity pass

After the Life-roadmap alignment receipt, the same isolated tuple was checked
with the bounded offline backend packet (**129 passed**), the Home/Places native
packet (**45 passed**) and the Life native packet (**32 passed**). These runs
confirm that the documented tuple still preserves the existing projection,
renderer and Life-reader contracts; they do not replace `make verify`, prove
device acceptance, or widen the evidence for recurring supply, provider-backed
generation, visual parity, R05 process recovery or R09 persisted/native
timezone edges. No merge, activation or publication occurred.

### September 21 Home partial-read treatment

The backend already carries owner-level `RootDegradation` entries when an
optional Home owner is unavailable or partial. App `c37e85f83` now presents a
small, generic **A partial read** notice above the supplied Home content. It
does not expose owner names or diagnostic strings; retry appears only when at
least one degradation is explicitly retryable. Existing orientation, units,
exact destinations and return behavior remain unchanged. The focused Home
screen/experience packet passes **32 tests**, TypeScript and targeted lint pass,
and the polish scenario/design-reference checks are structurally green (the
Home contract still has no design-ref manifest). No backend, schema, route,
producer, storage, or policy surface changed; native screenshot/device
acceptance remains unrun.

### September 21 Places partial-read treatment

The governed Places runtime now presents the same generic **A partial read**
notice when its semantic envelope carries owner-level degradations and the
existing feed notice is not already describing the state. App `1ddb3a0ba`
keeps the supplied feed and semantic units on screen, hides backend owner,
code and effect strings, and offers Retry through the existing runtime refresh
path only when a degradation is explicitly retryable. The focused Home/Places
packet passes **50 tests**; TypeScript, targeted lint, polish-scenario
validation and structural design checks pass. No backend, schema, route,
producer, storage or policy surface changed, and native screenshot/device
acceptance remains unrun.

### September 21 canonical Home sequence readback

Backend `bdc05c02f` adds a production-composition test for the already supplied
same-Place sequence. It runs the real `compose_home_root_v2` pipeline with the
existing public-content adapter and verifies that two source revisions remain
substantive, preserve the Places context/place/source destination, and return
as one sequence. The same test also makes a source-owner read unavailable and
verifies that the sequence is omitted with an explicit retryable degradation
rather than shown as if it were current.

This is stronger than adapter-to-compiler evidence, but it is still a
controlled owner-read composition test, not a disposable-Postgres HTTP
readback, device acceptance run, recurring supply receipt, or visual parity
claim. The next runtime proof should use a safe supplied database/device when
available; otherwise preserve this boundary and select another supported
owner-backed value seam.

The child-code tuple after this proof is backend `bdc05c02f` and app
`242d309f0`. The earlier `306eb51a4` tuple remains the lease-repair baseline;
the new backend commit changes tests only.

A fresh, separately named disposable PostgreSQL was migrated to the current
head and the existing Save → Places → Home owner loop passed
`tests/integration/test_save_root_projection_loop_pg.py` (**1 passed**). This
confirms the current checkout still migrates and serves a real persisted owner
path; it does not turn the controlled same-Place sequence test into a
public-content HTTP readback or prove recurring supply.

### September 21 persisted public-Place HTTP readback

Backend `96d264c41` adds two integration cases on a fresh disposable PostgreSQL
database migrated to the current Alembic head. The real
`GET /api/root-projections/v2/home` route reads two accepted, evidence-linked
public Place primitives from the database, resolves the user's persisted Home
coordinates to the seeded test city, and composes one Home sequence. The
response preserves both immutable Source refs, the exact `place` entity ref,
and the Places context/entity destination. A second case retracts one source
observation and verifies that source disappears while the still-active source
remains readable.

The test keeps the actual HTTP route, Home composer, context resolver and
Places content reader live, while making unrelated Home owners empty so cold
database connection timing cannot decide this bounded owner proof. It is
therefore stronger than the controlled service-composition test but still not
a full default-portfolio performance run, recurring supply receipt, native
device acceptance, visual parity or provider-backed generation. The focused
HTTP cases and the existing Save → Places → Home persisted loop pass **3
tests** together; the broader Home/Places/content packet passes **106 tests**.
Fixtures are removed after each case. This closes the disposable-Postgres/API
boundary for the supplied public-Place sequence; the remaining gap is supply
breadth and full default-portfolio/native experience quality, not another
content storage or route abstraction.

### September 21 persisted Life graph HTTP readback

Backend `651628265` adds two fresh disposable-PostgreSQL integration proofs for
the existing Life graph owner. A Plan created through the real graph command
reaches both `/api/root-projections/v1/life` and
`/api/root-projections/v1/life/record`; the compact root preserves the Plan
title and exact `/you/life-record` destination, while the depth entry preserves
the viewer-owned Life ref and the same Plan identity. A second case creates an
explicitly accepted multi-person Occasion and shared Outcome, then verifies
that the People lens preserves the guest owner ref, Occasion grant and exact
Outcome destination in both root and depth reads. Intake and Atlas readers are
isolated as empty owners for this bounded test; graph projection, Life corpus
assembly, route fan-in and HTTP serialization remain real. Both cases pass on
a freshly migrated database, and the offline Life route packet passes **30
tests**.

This closes the persisted graph-to-Life HTTP boundary for one private Plan
family and one explicitly permissioned People Outcome. It does not establish
full corpus breadth, Threads serving, organization coverage, native/device
acceptance, visual parity, or later permitted context benefit. The next Life
package should therefore be a useful existing-authority downstream result or a
sparse/pending/failure treatment, not another route-only happy path.

### September 21 roadmap maintenance — post-review execution order

The code-review pass confirms that the roadmap is still directionally correct,
but it narrows the active queue. Receiving-boundary work is no longer the
default next milestone: the canonical Home/Places rail, full-scroll native
composition, Life source/original readers, bounded social receiving and the
People-bound anchor path have each reached their named candidate boundaries.
Repeating injected-unit, workspace-reachability or single happy-path tours
would add receipts without adding product value.

The Home/Places partial-read notices now close the generic owner-degradation
notice gap for the supplied roots. They do not close every empty, stale,
pending, or unavailable-owner case. Do not repeat notice work unless another
state produces a distinct user consequence. The next implementation package
must therefore satisfy all of the following:

1. Use an existing owner-backed payload with enough substance to deliver a
   useful result, rather than adding infrastructure to manufacture variety.
2. Preserve the exact source/depth/action destination, return state, expiry,
   and honest sparse/pending/failure treatment through the native surface.
3. Prefer one consequential value-depth seam in Home/Places or one
   permissioned Life/social downstream result whose authority already exists.
4. Include frontend hierarchy, accessibility and polish in the package's exit
   criteria; visual parity is not a separate excuse to reopen the shell.

R05 process-interruption/restart and live transient-provider failure/retry
evidence, plus R09 persisted/native timezone-edge evidence, remain open.
Attempt the remaining matrices only with a disposable queue/database/device
that can produce the named evidence; an
unavailable environment is unverified, not a reason to serialize independent
product work. The dedicated Integration/landing lane remains paused. This
maintenance note is a queue correction, not a new architecture program.

### September 21 Source worker lease-renewal repair

Backend `306eb51a4` now renews the existing durable Source workflow lease
while the bounded provider/readback executor is running, using the deployment
envelope's lease duration and renewal cadence. Renewal remains owner-fenced;
database renewal errors allow the existing completion/recovery fence to decide
the outcome rather than fabricating success. The focused Source worker,
workflow, contract, canonical-executor and runtime packet passes **79 tests**;
backend pre-commit checks pass.

This closes the code-level lease-renewal gap, but not the remaining R05
process-interruption/restart rehearsal or a live transient-provider retry
receipt. Those remain environment-dependent evidence tasks and do not justify
activating the worker or widening generation scope.

## September 21 post-execution rebaseline — after the 12-hour functional window

The window produced a coherent receiving/continuity increment rather than a
new subsystem. Home can now compare already-supplied experiences, compose
multiple addressed Place contributions, and keep admitted standalone Places
units visible through the canonical feed even when mature browse cards are
absent. Places can compare two privacy-eligible perspectives. Life now makes
the distinction between a retained source and an exact retained original
legible in both the digest and complete-record readers. These changes reuse
existing owner reads, composition kinds, renderer registration, exact
destinations, custody checks and return parameters. They add no generator,
feed, store, route family, booking flow, audience policy or notification
system.

This changes the product's implementation position in three specific ways:

1. **Receiving is no longer the principal unknown.** The backend selection
   rail, canonical Home/Places workspace, native semantic renderer gate and
   Life source/original readers are connected for the named cases. Repeating
   injected-unit, workspace-reachability or single-happy-path proofs is not a
   roadmap milestone.
2. **Value depth is now the principal product gap.** The candidate can deliver
   comparisons, social perspective and addressed material when structured
   inputs exist, but it still does not prove a worthwhile, varied full scroll
   or recurring prepared supply. A successful transport path is not evidence
   that the result is interesting, useful or worth returning for.
3. **Life continuity is clearer but not broad.** Source/original recognition,
   refinding and organization have a real native seam. Broader media/corpus
   coverage, later permitted reuse, useful Returns and People/Threads breadth
   remain M3/M4/M5 work; this receipt does not justify a new inference or
   storage architecture.

### Historical forward order at the September 21 checkpoint — superseded

The sequence below records the September 21 checkpoint only. It is not a
second active queue: use [§4 Current package register](#4-current-package-register)
for the September 22 order. In particular, Home composition breadth is now the
primary build; Life/social value and the R05/R09 evidence remain complementary
or non-blocking as stated there. Keep this historical reasoning for provenance,
but do not dispatch from it when it differs from §4.

1. **Close only consequential edge evidence** when its disposable database,
   queue or device is available: R05 process-restart and live
   transient-provider failure/retry, plus R09 persisted/native timezone edges.
   R04 native sender control is now verified; do not block independent product
   work on unavailable environments or rerun completed receiving tours.
2. **Completed bounded Home full-scroll package:** the receipt below proves
   one composed scroll from real, already supplied owner payloads, including
   exact source/depth doors and honest asynchronous material loading. This is
   a useful acceptance boundary, not proof of broad corpus fullness; choose
   the next value-depth package from another supported owner rather than
   adding infrastructure to manufacture variety.
3. **Advance Life/social downstream value** on independent files: extend
   bounded readers and permissioned later use beyond the exact-source seam,
   while keeping source authority, audience and custody explicit. The visible
   result must reduce user work rather than expose organization maintenance.
4. **Reassess the complete cut only after those outcomes.** Shared Integration,
   main landing, activation, release certification and any Atlas retirement
   remain separately authorized and paused. Frontend polish and accessibility
   are finish conditions for each selected surface package, not a reason to
   open a repository-wide visual rewrite.

This checkpoint is a progress rebaseline, not a feature-completion claim. No
overall percentage is meaningful until the Claude design inventory, supplied
content breadth and native acceptance are measured against the same candidate
and evidence boundary.

### September 21 verification receipt — latest candidate

After the People-bound anchor follow-through and Source lease-renewal repair,
the latest candidate was checked without changing production state or claiming
a full gate. Backend root projection regressions passed **443 tests**; the
focused Life route/projection/index-projector packet passed **60 tests**; the
focused Home/Places/Life native packet passed **54
tests**; and the persisted schedule-zone unit packet passed **36 tests**.
These packets overlap the broader historical receipts and prove only their
named contracts. They do not close R05's process-interruption/transient-failure
matrix, R09's persisted/native cross-device/DST matrix, provider-backed supply,
recurring generated content, full-scroll quality, design parity, or release
readiness. No `make verify`, full device acceptance campaign, merge, flag
activation, or publication was performed by this receipt.

The verification result reinforces the current execution order: keep the
candidate's receiving and continuity foundations, choose one existing
owner-backed value-depth or Life/social downstream slice, and reserve edge
evidence for an environment where its disposable queue/database/device is
available. Do not reopen a new generator, feed, storage, route, or universal
object architecture in response to these passing counts.

### September 21 Life · People receipt — shared outcomes reach the record

The Life adapter now admits a shared Outcome into the People lens when its
existing owner projection ties it to an Occasion with at least one other active
participant. It also admits a non-private shared Commitment with multiple
authorized participants even when no Occasion exists, using the existing
commitment-scoped grant. Entries retain their audience grant, attributed member
owner refs, exact Life-record destination and the copy `Shared with your
people`. Viewer-only material remains out of People rather than being
relabeled as social material. This is an additive read/return seam; it does not
create an Occasion producer, person dossier, activity feed, new audience
policy, or contribution inference.

Backend commits `ef4167163`, `e9ad26f7f` and `014313121` carry the adapter and route
regressions; app
commits `76af974a0` and `9a597abd4` prove the native entry restores the exact
Life reader with `lens=people` (while other owners retain `lifeLens` return
context). The latest backend root packet passes **442 tests**;
the Life anchor/projection/route/index packet passes **60 tests**; the combined
Home/Places/Life native packet passes **54 tests**; and TypeScript plus the
resource-destination packet pass. The result proves a bounded structured
People record, not broader media/contribution richness, names, social
juxtaposition, provider supply, design parity, or release readiness.

### September 21 Life · People follow-through — explicit person-bound originals remain findable

The Life owner already admitted an intake anchor with an explicit
`people=resolved` binding to the direct People read, but the shadow/index
projector wrote every anchor as Time-only. Backend `9d52e71b3` now preserves
the owner-declared lens set: Time always, Places only for an explicit place
binding, and People only for an explicit people binding. The anchor remains
private and opens its exact artifact owner; no audience, person dossier or
social inference is added.

The focused anchor/projection/route/index packet passes **60 tests**, including
the complete-record `lens=people` read, and the full root-projection packet
passes **442 tests** on this backend head. This closes a bounded Life
continuity gap between direct, shadow and depth reads; it does not claim
shared-media breadth, names, later permitted reuse or design parity.

The native Life root now has the matching private-anchor return regression in
app `242d309f0`: the People lens opens an `anchor` entry to its exact artifact
and preserves `lifeLens=people` without turning the private source into a
shared item. The focused `LifeRootV1Screen` suite passes **13 tests** and
TypeScript passes. The previously recorded 54-test combined native packet is
unchanged and remains scoped to the suites it actually ran.

### September 21 native receipt — honest semantic unit states

App commit `9b463726d` adds one shared `RootUnitStatusMeta` treatment for
non-current semantic units. Home and Places preserve substantive pending or
partial material and its exact doors while clearly saying that the result is
still taking shape or only partly available; stale and unconfirmed states have
explicit copy as well. Both native renderers fail closed for `revoked` units so
a cached envelope cannot keep withdrawn social or private material visible.
The backend contract, selection gates, schema and owner reads are unchanged.

The focused Home/Places packet passes **35 tests**; TypeScript and targeted
ESLint pass with only the existing renderer max-lines warnings. Polish scenario
IDs pass; the `vesper-home` design-reference check passes and the
`places-workspace` check passes with the expected operator-owned external-canon
warning. No device screenshot or full surface capture was run, so this is
native semantic-state evidence, not visual parity or release evidence.

### September 21 contract-hardening follow-through — sequence scale and practical catalog kinds

The sequence package received two bounded backend follow-through checks. The
expanded-place public-content reader now batches a nine-place scope as
eight-plus-one owner calls rather than dropping the entire Home reader; the
focused regression preserves all nine current records in backend commit
`7fc1858df`. The practical fit path now has a positive owner-adapter matrix for
every catalog kind the mobile surface exposes (`venue`, `site`,
`accommodation`, and `experience`) in backend commit `248237edd`, while
unsupported and stale evidence remain fail-closed. A stale Home assertion
about the intentional public-reading limit was corrected in `17f20921b`.

The combined backend packet for content-source, practical-catalog and Home
portfolio coverage passes **94 tests**. The native sequence/rendering and Home
smoke packet passes **20 tests**; TypeScript, Ruff, formatting and compile
checks pass. These are contract and focused-regression receipts, not deployed
scale measurements, provider-backed fit evidence, recurring generation,
canonical runtime readback or design parity. The next package remains a
substantive supplied Home/Places result or an independently authorized Life
downstream value seam; do not widen infrastructure to manufacture fullness.

## September 21 functional receipt — same-place public readings compose into a sequence

The public Place-content owner already supplied accepted, evidence-linked
interpretations to Home one at a time. Backend commits `7f7bc8e24` and the
defensive deduplication follow-up `27a6ea73d` add an
opt-in Home adapter mode used by the real `places_context` reader: when at
least two current records describe the same entity, Home emits one
`horizon_editorial_passage` whose lead medium is the existing `sequence`
anatomy. Each step preserves its source id and exact claim/interpretation;
the unit carries every source/entity/context reference, one provenance action,
and a Places destination. Unpaired entities retain the existing single-reading
path. The adapter does not merge records, generate a new claim, reorder beyond
the supplied owner order, or change Places serving.

The focused Home portfolio/projection packet passes **90 tests**; Ruff,
formatting, compile and diff checks pass. The existing native sequence anatomy
and Home smoke packet pass **24 tests**, TypeScript remains green, and no API
schema/types, generator, route, store, policy or rollout surface changed. This
is the first substantive value-depth package in the current window, not proof
of broad content supply, recurring generation, design parity or a complete
full-scroll runtime receipt. The next proof must use the canonical Home runtime
or move to another supplied value family; it must retain exact destinations,
expiry and sparse/pending/failure behavior.

### September 21 contract-hardening receipt — the sequence reaches the page and native anatomy

The same-place reading package now has regression evidence at both seams that
matter for delivery. Backend commit `7e7095f57` proves that the composed
candidate survives Home selection and `compile_home_v2` as one Horizons unit,
retaining its typed sequence anatomy and Places destination. App commit
`ac6e08235` proves that the existing native composition renderer presents the
ordered steps rather than reducing the payload to a generic editorial label.

The focused backend Home portfolio packet passes **47 tests** and the focused
native composition/Home smoke packet passes **20 tests**. This is contract
hardening for the previous receipt, not a new producer or a claim that the
canonical runtime has supplied multiple readings for a real account. The next
substantive slice remains a real sparse/pending/failure runtime readback or
another already-supplied owner-backed value family; no new generator, store,
route, or feed should be introduced to manufacture breadth.

## September 21 functional receipt — standalone Places rail survives an empty feed

The backend/runtime and canonical workspace forwarding seam could still be
hidden by the app's mature-feed state classifier: when `workspace_feed.sections`
was empty, Places became an empty/unavailable root before `field_units` reached
the feed renderer. App commit `66079f456` makes admitted, natively renderable
standalone semantic units count as received Places content even when there are
no mature browse cards. The client uses the existing semantic renderer registry
as the renderability gate, so an unsupported kind cannot make an empty page look
healthy.

The focused presentation/workspace packet passes **40 tests**, TypeScript and
targeted ESLint pass. This is a receiving-state correction, not new supply,
producer, route, storage, rollout or design-parity work. A populated standalone
unit now has a complete path to the canonical scroll; the next package still
needs substantive full-scroll value and exact destination/return evidence.

## September 21 functional receipt — addressed Place contributions compose on Home

Home already received one recipient-authorized Place contribution as a
`people_note_door`. Backend commit `953e2bc69` now composes two or more eligible
contributions into the admitted `people_authored_region` comparison form. Each
case keeps the sender's exact words and attribution, while each action carries
its own exact Place and handoff references. A single contribution retains the
existing note-door behavior; revoked, expired, misaddressed or malformed
material is excluded before composition.

App commit `4c507e1c4` promotes the existing Home renderer registry and adds a
native **Addressed to you** treatment using the shared composition renderer and
typed action callbacks. Backend root-projection tests pass **438 tests**;
focused Home renderer/smoke tests pass **32 tests**, TypeScript passes, and
targeted ESLint reports no errors (only the existing Home renderer max-lines
warning). This is a bounded social-receiving/value-depth improvement: no new
store, audience policy, notification, generator or route was introduced. A
real relationship-backed native/device receipt remains outside this change.

## September 21 functional receipt — Life distinguishes retained sources and originals

The existing Life root and complete-record readers already opened exact retained
source/original destinations, but their native rows looked identical to ordinary
Life records. App commit `b1f37eac4` adds the existing `LifeEpisodeRow` stamp
affordance: source submissions show **SOURCE** and exact retained originals show
**ORIGINAL** in both the root digest and paginated record. The destination,
current-custody checks, lens return parameters and owner contracts are unchanged.

The focused Life root/record/groups/primitives packet passes **34 tests**;
TypeScript and targeted ESLint pass, and `git diff --check` is clean. This is a
bounded native records/originals comprehension improvement, not a new corpus,
media reader, source type, organization rule, or visual-parity claim.

**September 21 afternoon execution rule:** the latest product behavior is the
supplied-reading `Why this?` slice, mechanism-row adaptation, explicit
selected-trip fit, attributed friend-place preview, public-reading limits, and
native social-evidence treatment, exact social venue doors, Home editorial/
aperture anatomy, Places editorial-cover anatomy, the native starter browse
shelf, native branch/continuity/returned-understanding treatments, the honest
balanced-field fallback, the native owner-backed evidence register, the
supplied-experience comparison, and the plural social perspective in backend
`c3f64589e` and app `ecdecaffe`.
The next
implementation should therefore be selected from an
existing owner-backed Home/Places payload and add substantive received value
(for example, a truthful comparison, sequence, evidence view or practical
consequence only when its structured inputs already exist). It must preserve an
exact destination, return state, expiry and empty/failure behavior, and ship
with focused regression evidence. Do not open a new generator, feed, store,
route family or broad visual-parity program to make this slice appear fuller.
If the payload cannot support a truthful result, keep the gap explicit and
move to the next supported owner/destination/return seam rather than inventing
content.

## September 21 functional receipt — compare supplied experience options

Places already supplies bounded experience previews with timing, duration and
price. Home previously flattened each experience into a separate aperture, so
the person had to open several doors before understanding how the options
differed. When one Places section contains at least two owner-backed
experiences, the backend now emits one `horizon_prepared_alternatives`
comparison composition with two to four cases and one exact Places action per
case. One-experience sections retain the existing aperture behavior.

Backend commit `7d036bb7c` adds the bounded comparison adapter, preserves the
existing owner/read requirements and expiry, and covers the multi-option and
single-option paths. App commits `b7d025044` and `4c53af70d` register the native
comparison treatment, its registry contract and exact action destinations. The focused backend
Home/contract/composition packet passes **80 tests**; the Home native smoke
packet passes **23 tests**; TypeScript, targeted ESLint and backend Ruff/
format checks pass (the existing Home renderer max-lines warning remains).
This is a value-depth improvement over already supplied data: it adds no
provider acquisition, ranking policy, generator, store, route family, booking
flow or design-parity claim.

## September 21 functional receipt — plural social perspective in Places

The relationship owner already supplies up to two privacy-eligible friends,
their bounded place names, and exact venue IDs for a Places context. Places now
keeps two such perspectives together as one `social_plural_comparison`
composition rather than rendering an activity-feed-like pair of rows. The
comparison preserves attribution, names each perspective, provides up to six
exact Place doors, carries one combined relationship read requirement, expires
with the current social projection, and explicitly says no response is owed.
Sections with fewer than two eligible friends retain the existing attributed
row behavior.

Backend commit `c3f64589e` adds the bounded producer and regression; app commit
`62c5982a8` adds the native plural-social treatment and exact-door regression.
The focused backend root packet passes **81 tests**; the combined app Home/
Places renderer packet passes **80 tests**; TypeScript, targeted ESLint and
backend Ruff/format checks pass (the existing Places renderer max-lines
warning remains). This extends the existing casual-sharing owner; it adds no
social feed, notification, friend-location inference, response obligation,
new store, audience policy or occasion model.

## September 21 functional receipt — standalone Places units reach production rail

The preceding workspace regression used an injected `field_units` value and
therefore proved only the native receiving boundary. Backend commits
`90fe88f88` (implementation) and `5cfcae1c4` (real plural-adapter regression)
close the upstream seam: the Places runtime adapter now forwards
all explicitly supported standalone kinds (including plural social perspective,
evidence, and the admitted field families) while excluding units already
represented by mature browse cards. The runtime model rejects unsupported
standalone kinds instead of exposing an unregistered renderer. The focused
Places-runtime suite passes **9 tests** and the combined root packet passes
**96 tests**, with Ruff, formatting and compilation clean. This changes no
producer, route, store, rollout flag or policy; provider-backed supply and
native full-scroll acceptance remain open.

## September 21 functional receipt — canonical Places workspace reachability

The plural-social and other semantic field units were already exercised by the
internal `PlacesRootV2Screen`, but the production `PlacesWorkspace` boundary
did not have a direct regression proving that the runtime envelope's standalone
units reached its `PlacesSectionFeed`. App commit `ecdecaffe` adds that
canonical-workspace test: a `social_plural_comparison` unit is supplied through
the real workspace prop and remains visible to the feed. The focused workspace
suite passes **16 tests**, the targeted ESLint check is clean, and the app
typecheck remains green. This closes a receiving-boundary evidence gap only; it
adds no producer, route, rollout flag, storage family or design-parity claim.

**Scope decision — Places group waiting remains deferred.** The legacy Places
`group_waiting` producer still reads itinerary proposals alongside booking
holds. The v2 adapter intentionally does not surface that section: canonical
open Plan proposals already have a Home-owned coordination candidate whose
destination is the supported Chat review route. Promoting the Places copy would
duplicate coordination, revive the operational urgency surface we are pruning,
and bypass the Home → Chat return contract. Revisit only if the Plan owner
supplies a distinct, permission-safe Place consequence with new value beyond
the existing proposal review; do not add a second proposal route to fill the
Places scroll.

## September 21 native receipt — mechanism-row anatomy

The accepted `horizon_mechanism_row` Home kind now has a distinct native
renderer instead of falling through to the generic reading treatment. The row
keeps the existing authored anchor, explanation, evidence basis, source
inspection action, exact Places destination, expiry and return registration,
while using the compact mechanism mark/copy anatomy appropriate to a cue or
approach instruction. No backend contract, source owner, generator or route
changed.

App commit `7b735a71e` adds the renderer and a regression covering its visible
anatomy and passive surface treatment. The focused Home renderer/smoke packet
passes **21 tests** and `npx tsc --noEmit` passes. This is a native treatment
improvement for an already supplied value family, not full Claude-design parity
or evidence that additional semantic kinds are supported.

## September 21 functional receipt — preserve attributed Place perspective

Places friend-activity cards already arrive from the relationship owner with
the names of the shared places. The root adapter previously discarded those
names and rendered only the friend plus a count/sentence. It now carries a
bounded preview of up to three names (with a `+N more` suffix when needed) in
the existing attributed social row. The exact person owner, privacy-scoped
relationship read, Places destination and no-response-debt behavior are
unchanged.

Backend commit `0dcc26db0` adds the adapter behavior and regression coverage.
The focused Places/Home contract packet passes **33 tests**; Ruff, formatting
and Python compile checks pass. This is a consumer-value improvement over an
existing social owner payload, not a new sharing model, audience policy or
group-occasion implementation.

## September 21 functional receipt — retain public-reading limits

The existing Home public-Place adapter now carries the accepted Source's
explicit `limits` into the bounded reading basis, alongside the observable
target and applicable conditions. This keeps a supplied cue or interpretation
from sounding like a route, hours or preference guarantee while preserving the
same authored claim, exact Source revision, Places destination, expiry and
return behavior. The field was already present in the owner contract; no new
schema, generator or storage path was added.

Backend commit `a5914bd82` adds the bounded projection and regression coverage.
The focused Home portfolio/composition packet passes **49 tests**; Ruff,
formatting and Python compile checks pass.

## September 21 functional receipt — render attributed social evidence

The Places native semantic-unit card now gives the existing
`social_attributed_evidence` kind a compact people-led treatment: a person mark,
the attributed friend's authored label, the bounded relation text (including
the shared Place names retained by the backend), and the same source,
destination and capability doors used by other admitted units. The practical
expiry fence still runs before the body, so an expired assessment cannot leave
stale fit prose visible. This is a native adaptation of an existing
relationship-owned payload; it does not add an audience policy, sharing model,
generator, store, or route.

App commit `6aedd2c00` adds the renderer and a regression in the Places root
screen. Focused Places root/expiry tests pass (**27 tests**), TypeScript and
targeted ESLint pass. The renderer is not full Claude-design parity and does
not prove broad social supply or general multiplayer behavior.

## September 21 native receipt — Home editorial and aperture anatomy

Home now gives two already-supplied value families their own native treatments:
`horizon_editorial_passage` uses an editorial reading rail with an explicit
reading label, authored substance and evidence basis; `horizon_aperture_row`
uses a compact compass-led opening with its relation and exact continuation.
Both preserve source doors, destination doors, practical assessment expiry and
capability actions. Composition payloads continue through the existing
RootComposition renderer rather than being flattened into another copy path.

App commit `fda51a42c` adds both treatments and regression coverage. The
focused Home renderer/smoke packet passes **22 tests**, TypeScript passes, and
targeted ESLint has no errors (the renderer's pre-existing max-lines warning
remains). This improves the native expression of supplied Home value; it does
not claim new content supply or full Claude-design parity.

## September 21 native receipt — Places editorial field anatomy

Places now gives the existing `field_editorial_cover` read/composition kind a
native field-reading rail, authored substance and an “A field reading” label,
while preserving source inspection, exact destination, actions and practical
expiry behavior. App commit `659f572ae` adds the treatment and regression.
Focused Places root/expiry tests pass **28 tests**; TypeScript and targeted
ESLint pass. This improves the native expression of supplied Places value; it
does not claim new content supply or full Claude-design parity.

## September 21 native receipt — Places starter browse shelf

The admitted `field_browse_shelf` starter kind now has a native way-in tile
instead of falling through to the generic field card. The treatment preserves
the existing source, exact destination, capability and practical-expiry seams;
it does not fabricate the riso/photo media that the design manifest still
requires from a future media-bearing payload. App commit `17c2c4472` adds the
native treatment and root regression. The focused Places root/expiry packet
passes **29 tests**, TypeScript passes, and targeted ESLint has no errors.

## September 21 native receipt — Places field-family treatments

The admitted `field_branch`, `field_returned_understanding`, and
`field_continuity_doors` kinds now have native row, gold-rule reading, and
carry-forward door treatments. Source inspection, exact destinations,
capability actions and practical expiry remain shared through the existing
follow-up seam. App commit `f4a190b56` adds these treatments, a small styles
module to keep the renderer under its size budget, and root regressions. The
focused Places root/expiry packet passes **30 tests**, TypeScript passes, and
targeted ESLint has no errors. This is native coverage of admitted payloads; it
does not claim returned-understanding supply or full Places design parity.

## September 21 functional receipt — Places balanced-field fallback

When the current scope has no eligible World Field lead (including a feed made
entirely of deferred encounter-state sections), the backend now emits the
admitted `field_balanced_fallback` kind with an explicit absence explanation
and the existing search/map actions. The native client renders that state as an
open-field orientation treatment and preserves exact expiry/source/action
behavior. Backend commit `a516ce26d` adds the producer contract and regression;
focused backend Places packets pass **39 tests**. App commit `34c3651c1` adds
the native treatment and regression; the focused Places root/expiry packet
passes **31 tests**, TypeScript passes, and targeted ESLint has no errors. This
closes an honest sparse-state seam; it does not add provider acquisition, media
supply or a recommendation.

## September 21 functional receipt — Places evidence register

The existing feature-flagged Places register producer now has a v2 receiving
path when it supplies an approved verdict, viewer-owned history log, or fresh
change register. The backend preserves the register lines and evidence
revision as a presentation-neutral `path_evidence_apparatus` composition; the
native client renders an evidence list with the existing exact Place source
door and expiry behavior. Backend commit `aa96caff7` adds the adapter
regression; focused backend Places packets pass **40 tests**. App commit
`e601a9dfd` adds the native evidence treatment and regression; the focused
Places root/expiry packet passes **32 tests**, TypeScript passes, and targeted
ESLint has no errors. This does not enable `PLACES_REGISTERS_ENABLED`, add a
new producer/store, or turn an unqualified register into a recommendation.

## September 21 functional receipt — preserve social Place destinations

The existing recipient-consented friend activity path now carries its bounded
owner-provided venue IDs through the Places v2 unit. The native social row can
therefore expose named **Open …** actions for up to three shared Places, each
with an exact venue destination and the normal root return token. Name-only
legacy rows retain their existing person/field door and never guess a venue
from display text. No new social store, audience policy, notification,
occasion model or route was added.

Backend commits `cee8a4474` and `f9fa3d82b` add bounded venue refs/actions,
legacy-row tolerance and contract coverage; app commit `6c8b0cd14` preserves duplicate-action test identity and
verifies both exact venue doors. Backend focused Places contract/runtime tests
pass (**39 tests**); app focused Places root/expiry tests pass (**27 tests**),
with TypeScript and targeted ESLint clean. This is a completion improvement for
an existing social receiving path, not general multiplayer coverage.

The dedicated shared Integration/landing lane remains **PAUSED by the founder**.
That pause does not cancel the subsequently authorized isolated implementation
and lane-local disposable-runtime work recorded here. This rebaseline does not
resume shared runtime, authorize landing/publishing, enable production flags or
adopt pending product agreements. Cross-run editorial reuse remains pending.
The [review ledger](functional-implementation-code-review-2026-09-21.md) is
**not closed**: the named native/database happy paths now pass and the R01/R03
authority matrices are verified. R04's real API sender-control boundary now
passes and its native UI runner is committed but unrun because no simulator is
available; R05's exhausted-lease code correction is committed with focused
tests, but disposable-Postgres/transient-restart evidence remains open; R09
timezone edge coverage remains open.

## September 21 functional receipt — honor explicit selected-trip fit

Home's bounded public-Place reader now carries through an existing
server-owned Places selection reason. When the automatic context is explicitly
`live_trip`, `imminent_trip`, or `recent_return`, accepted public readings for
that context are admitted with the higher current-fit relevance and the
grounded “already in motion” explanation. Home, area, anywhere, and ordinary
continuation contexts remain conservative; a rich scope alone does not create
personal relevance.

This uses `PlacesContextRef.selection_reason` already resolved by the Places
owner. It adds no sensor inference, profile field, notification, generator,
store, or new route. Backend commit `052284b33` adds the caller wiring and a
trip-selected regression case; **49** focused Home portfolio/composition tests
pass, with Ruff and formatting clean. The result is still a public reading,
not a claim about the viewer's taste or attendance.

## September 21 functional receipt — preserve supplied mechanism cues

The first substantive Home breadth slice after the receiving proofs is now
implemented. Accepted public Place primitives authored as `perceptual_cue` or
`approach_cue` retain their existing Source-backed `RootRead` payload but emit
the already-admitted `horizon_mechanism_row` anatomy. Interpretive lenses and
other primitive types remain editorial passages until their narrower owner
contracts are explicit. The native Home registry now renders the mechanism row
instead of dropping an otherwise valid unit as an unpromoted kind.

This is an adaptation of existing owner data, not a new generator, store,
route, or inference layer. Exact Source/Place destinations, `Why this?`, expiry,
and return behavior are unchanged. Backend commit `507cefd38` adds the typed
selection and regression coverage; app commit `df490cb56` promotes the native
registry entry. Evidence: **48** focused backend Home portfolio/composition
tests, **20** focused Home renderer/smoke tests, TypeScript, Ruff, formatting,
and Python compile checks passed. This does not establish `horizon_world_fact_row`,
prepared alternatives, broad source supply, or full Claude-design parity.

## September 21 functional receipt — Why-this on supplied Home readings

The first bounded breadth slice after the receiving proofs is now implemented
in backend commit `c4b4ff031`. Home's existing contextual Places angles and
accepted public Place interpretations now carry the typed `source.inspect`
navigation action, rendered by the existing Home V2 action/inspection path as
the optional **Why this?** affordance. It does not add a source store, a new
generator, or a new route: the candidate keeps its existing exact source and
Place destination, while the existing inspection hook explains the item's
grounding and preserves the owner-removal/request path for source attachments.

Evidence: the focused Home portfolio/composition packet passed **47 tests**;
Ruff, format and Python compile checks passed; the backend child is clean at
`c4b4ff031`. This is a small receiving/comprehension improvement, not proof of
full Claude-design parity or broad content supply. The next Home breadth slice
should add substantive supplied value or a supported consequence to the full
scroll, not another explanatory control.

## September 21 evidence closeout — current boundary

The isolated lane ran the exact candidate against disposable Postgres on
`localhost:61460`, API `http://127.0.0.1:61463`, and simulator
`D7C8FEF4-237B-4347-841C-6FE920BFABFA` (iOS 18.2). The persistence packet
passed **8 tests** with 22 deselected, and the relationship/content packet
passed **2 tests** with 47 deselected. The three existing native runners then
passed: Life retained-source return/withdrawal, Home Save → Places unsave and
readback, and Places recipient-consented social pull → venue → return. The
social runner required `PLACE_HANDOFF_PULL_ENABLED=true` in the disposable API
process; no production or shared runtime flag was changed.

This closes those named owner/readback boundaries, not the whole product. The
queue wrapper, sender-control and timezone edge matrices, broader supplied
Home/Places
coverage, later permitted Life/social value, Claude-design visual parity and
release/landing gates remain unfinished.

The existing `run-cross-root-home-places-life.sh` then passed as a combined
journey on the same simulator and lane runtime: Home's addressed social note
opened the exact Place and returned; the Places tab remained reachable; Life's
Places lens opened the exact retained original and returned to the same Life
entry. The runner verified both Home and Life no longer represented their
temporary fixtures after cleanup. This proves connected navigation and
withdrawal for these two supported fixtures, not shared Occasion semantics,
general media/group behavior, or full design parity.

## September 21 native/runtime receipt — Home Save → Places consequence and readback

The first real-owner native rehearsal for the current Home/Places receiving
surface now passes in the isolated functional lane. The lane used the running
local API, disposable Postgres fixture and iOS simulator rather than mocked
Home data. The existing rehearsal provisioned one private Save for the named
venue **Vesper Rehearsal Bookshop**, then exercised the real app:

- Home admitted the exact `save.<id>` destination and opened the canonical
  Places venue reader;
- the native save control exposed the actual accessibility contract,
  **Remove place from saved places**, and the tap completed the unsave;
- the runner read the canonical `/api/users/{user}/saves` owner state and
  Home projection, confirming the venue Save and its Home representation were
  absent after the action;
- the fixture was restored through the owner writer, and the readback flow
  reopened the restored venue from Home with the saved state and non-empty
  Places reading.

Evidence: `run-home-places-real-save-readback.sh` passed all three flows
(preflight, destructive unsave, restored readback) on simulator
`D7C8FEF4-237B-4347-841C-6FE920BFABFA`; the focused runner contract had
**3/3 tests passed** and `npm run typecheck` passed. App commit
`c05d0827b` makes the rehearsal lane-port aware, removes its implicit `.env`
requirement, prevents retries of the destructive step, and aligns both flows
with the native accessibility label. The canonical fixture was restored and
no production flag or dataset was changed.

This closes one native receiving/consequence boundary. It does not prove
visual parity with the Claude designs, broad Places/Home corpus coverage,
Life original-byte return, multiplayer media/group behavior, production flag
activation, merge/publication or release readiness. The next bounded work
should be another supported return/action seam (preferably Life's exact
source return/refind) or a real supplied Home/Places content variant; do not
respond by adding a new generator, social store or route family.

## September 21 native/runtime receipt — Life exact source return and withdrawal

The next unblocked boundary is now also proven with real owner data. A
disposable retained Intake source was created through the existing Capture
writer using inline text, projected through the canonical retained-source Life
owner, and exposed by the real Life v1 API. The native rehearsal then:

- rendered the retained `source_submission` in the Life Time lens;
- opened its exact `/you/intake-submissions/{submissionId}` destination;
- showed the retained note and `ORIGINAL MATERIAL` section;
- returned to the same Life root/lens through the native return control; and
- revoked the source through the owner delete path, withdrew its Life row, and
  verified the canonical Life API no longer represented it.

The reusable provisioner and runner are now committed: backend
`e752cdbd4`, app `5313f3b36`. The runner requires an explicit local database,
QA owner and API origin, uses a run-scoped idempotency key, and cleans up on
success or failure. Evidence: the complete `run-life-real-source-return.sh`
passed on simulator `D7C8FEF4-237B-4347-841C-6FE920BFABFA`; its six focused
runner-contract tests passed, the Life/Intake Jest packet passed **29 tests**,
and TypeScript, Python compile, Ruff and format checks passed. Existing
non-fatal React `act(...)` warnings remain in the original-source tests.

This closes the native Life exact-source return/readback boundary for one
owner-authorized retained text source. It does not establish full Life corpus
coverage, original binary media playback, multi-lens breadth, social/group
media, visual parity with Claude designs, production flag activation,
merge/publication or release readiness. The next useful work is another
supported supplied Home/Places variant or a practical/social action seam—not
another Life storage abstraction.

## September 21 native/runtime receipt — Places recipient-consented social read

The existing Places `From your people` section now has a real native receiving
and return rehearsal for the bounded `place_pull` contract. The provisioner
created a disposable sender, active pair room, recipient-owned pull grant,
accepted graph-to-venue binding, venue under the recipient's explicit New York
Place context, and one venue-bound handoff. With the existing pull flag enabled
only in the local process, the iOS simulator then:

- rendered the exact sender note in `From your people`;
- opened the handoff's canonical venue through the stable venue tile target;
- showed the venue reader and its exact generated fixture name;
- returned to the same Places context through the native back control; and
- verified the social card was still present before the runner removed the
  temporary handoff and re-read the canonical feed.

Evidence: `run-places-real-social-pull.sh` passed on simulator
`D7C8FEF4-237B-4347-841C-6FE920BFABFA` for run
`places-social-native-20260921-e`; the runner contract packet passed **9/9**
tests, and app TypeScript, backend compile, Ruff and format checks passed. The
fixture cleanup removed the sender, relationship, graph, venue and handoff;
the post-cleanup feed no longer contained the handoff. This is native proof of
one recipient-consented venue-bound pull, not general social-feed parity,
group/media sharing, Life adoption, production activation, visual parity,
merge/publication or release readiness. The next useful work is a supported
practical/social action or supplied Home/Places variant that reuses the same
owner and destination contracts; do not add a second social store or a new
generic feed architecture.

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

<a id="2-inspected-baseline--september-22"></a>

## 2. Inspected baseline — September 22

At the previous roadmap update, the isolated candidate was clean at
workspace `0138f2a`, backend `60da1dcb9`, and app `d021488be`, all on
`codex/functional-implementation-2026-09-20`. Backend `fd80c437e` admits the
existing saved-Place closure, reopening and weather-window notices into Home
as private, exact-venue Place continuations. The latest backend slice adds a
conditional Home door into Places' existing Friends section: it appears only
when the same current Places read contains at least two distinct trip-shared
`friend-save` cards, retains the selected Places context and Home return token,
and does not count addressed handoff notes already shown on Home. App
`d021488be` focuses that existing section without changing server ordering.
Focused evidence for this latest slice is 59 Home portfolio tests and 117 app
route/workspace/feed tests, plus source/test TypeScript, targeted ESLint and
Places docs checks. No live-account read or device acceptance was run for it.

The candidate also contains the integrated Places World Field and its combined
native full-scroll acceptance, exact Home Outcome → Life record return,
Home-selected Place-note ownership and Keep path, bounded Home renderer
correction for coherent secondary compositions, and a fail-closed regression
preventing substitution of another person's Place note. Earlier receipts remain
scoped: the registered Home-root capture is an available-state mock fixture,
not a full owner-backed Home scroll or a Claude-design parity verdict. A
separate three-family Home scroll has owner-backed native evidence, but neither
result establishes the broader design-aligned Home composition. The fixed
cold-start example still lacks current-tuple native presentation and
live-retirement evidence. The current visual doctor could not run without Metro
at `:8081`; no current-tuple screenshot was produced. Focused Source recovery
tests have passed, while process restart and live provider retry remain
explicitly open.
Since that baseline, Home no longer drops every In-motion candidate except
one. Distinct settled/current owner records can coexist in that region; the
existing one-unresolved-decision rule and posture-specific cumulative
attention budget still bound the page. The app already renders selected units
as a region list, so no new UI primitive, route, schema, producer, or owner was
added. Backend commit `7537ae042` and app commit `d9b3fd358` carry the change.
The focused backend selector/portfolio packet passed **68 tests**; the native
Home screen component packet passed **17 tests**; source TypeScript, targeted
ESLint, backend Ruff/format, and app documentation header/link checks passed.
No device capture or live account read was run. The app surface-contraction
check remains red on its stale route inventory plus unowned
`/you/intake-submissions/[submissionId]` and `/you/life-record`; the Home
surface-budget check remains red on pre-existing Places file-size overages.
Neither finding is in the changed files. Workspace `make docs-check` also
remains red on the unclassified
`docs/working/practical-judgment-producer-acceptance-brief-2026-09-09.md` and
expired compatibility entries `discover-url-bridge`, `atlas-tab-url-bridge`,
and `discover-map-api-bridge`; its current-state renderer cannot run with the
invalid inventory.

**Current isolated candidate after the Life audio slice.** Backend
`2d0721e67` adds the bounded Home child-source cleanup guard; app `93a9090de`
implements Life audio playback. All three isolated repositories were clean at
the start of this documentation correction. Intake v2 accepts server-decodable
audio; PDF/PKPass/HEIC/HEIF remain rejected pending scanner/decoder support, so
PDF preview is not a missing reader feature.

The canonical Life Intake reader now offers explicit-tap playback for retained
MP3/M4A/WAV through the existing authenticated, custody-checked GET media route.
There is no autoplay, transcript, AI use, export, share action, upload-format
expansion, new API operation, or policy expansion. Focused screen, original
boundary and shared audio-hook coverage passes **41 tests**; app TypeScript
passes. Targeted ESLint reports no errors and one existing max-lines warning in
the Intake screen. The **31** registered polish scenario IDs validate, and the
`life-root` design-reference check is structurally valid with its existing
HTML-reference warning. The visual QA command found no capture matching its
flow, so there is no screenshot or native/device verdict. Actual secured media
bytes, iOS/Android codec playback, expiry-specific playback, end-to-end owner
read, and accessibility/polish acceptance remain unproven.

The offline OpenAPI exporter regenerated the full snapshot from current backend
source. No API operation or generated mobile wire type changed. The governed
app projection still stops at the pre-existing **55 expired-policy findings**;
the earlier missing-consumer finding was caused by the abandoned `HEAD`
proposal and is no longer present. This is not a completed policy backlog or a
full type-sync gate. Native media/device proof remains a follow-up acceptance
item, not a reason to add a speculative API route or hold the Home composition
build.

Canonical main was not modified; its workspace checkout contains unrelated
user changes and remains untouched.

| Repository | Isolated candidate HEAD before this documentation update | Canonical `main` HEAD last inspected |
| --- | --- | --- |
| Workspace | `0f3caf4` | `70c4b4b` |
| Backend | `2d0721e67` | `a7c02cbe1` |
| App | `93a9090de` | `e2e792913` |

The canonical-main column is a comparison only: the workspace contains
unrelated uncommitted user changes, the backend contains an unrelated
untracked fixture, and the app checkout is clean. None was modified.

### September 22 follow-up — preserve Home saved-place closure context

The next isolated implementation used workspace parent `82d4304`, backend
baseline `8866f41a2`, and unchanged app `a4de82802`; backend commit
`95b0361ab` contains the source change. The Home adapter now carries the
producer's `CLOSED PERMANENTLY` label and exact explanation only when the
notice ID resolves to the canonical venue already represented by the Place
card. It remains the existing private, non-mutating Place doorway; the Places
`CLEAR` action is not copied. Mismatched identity fails closed, and reopened /
weather `NOTICE` rows remain unpromoted.

Evidence: `python3 -m pytest tests/root_projection/test_home_portfolio.py -q`
passed **55 tests**; `python3 -m pytest tests/root_projection
tests/places/test_return_sections.py -q` passed **491 tests**. Ruff,
formatting, `git diff --check`, and backend commit hooks passed. No OpenAPI,
mobile renderer, database, device, runtime service, standard gate, or rollout
flag changed. The workspace roadmap update is documentation-only. This is
copy fidelity for one existing Home path, not broad design coverage or a
decision to surface other notice kinds.

### September 22 implementation receipt — Home receives saved-Place changes

The follow-up used workspace parent `1d9264d`, backend `95b0361ab`, and
unchanged app `a4de82802`; backend commit `fd80c437e` extends the existing
contextual-Places adapter. Home now admits the current Places `CHANGED` feed's
closure, reopening, or weather-window notice only when its recognized notice
ID resolves to the exact venue ref. It carries the source's label and
explanation in the existing private `HORIZON_APERTURE_ROW`, with a typed exact
Places destination. It never copies the Places `CLEAR` action; malformed or
unknown notices and mismatched Place identities fail closed. The producer
still emits one changed item at a time. These viewer-owned notices are not
city-scoped facts and are not `horizon_world_fact_row`.

Evidence: the focused Home portfolio packet passed **57 tests**; root-projection
plus Places-return tests passed **493**. Existing mobile Home renderer, Home
screen smoke, and root-navigation suites passed **76 tests**; app TypeScript,
Ruff, formatting, `git diff --check`, and backend commit hooks passed. No app
code, OpenAPI, database, native-device/API rehearsal, or flag changed. The
mobile tests prove the existing aperture body and typed destination paths, not
a fresh native real-data capture. The V2 rollout remains unchanged.

The stronger Keep-after-reopen flow contract from app `e2c0bafb1` remains a
separate acceptance path: its 4-test flow contract and 33-test focused
owner/action/object-page packet pass, but it has not been exercised by the
`90-places-full-scroll` run and should not inherit that run's acceptance. The
registered native Home capture `20260922T095658Z-home-root` records app
`6ae89c427`; it covers only the available-state mock fixture, not current app
`a4de82802` or the full Home scroll. The exact-note non-substitution regression
passed on app `9a4c029e3`; app `a4de82802` subsequently changed only the sample
caption color and passed its focused renderer checks. No current-tuple visual
capture was possible because Metro was unavailable at `:8081`. The previously
observed `maestro:metadata:check` failure on untouched flow
`.maestro/76-places-public-reading.yaml` (`lane:
functional-implementation` is not an allowed metadata value) remains
unrechecked against this tuple; flow 75 itself normalized successfully.

At the previous inspected checkpoint, workspace `d076caa` was a
documentation-only rebaseline on top of functional workspace commit
`e7b872b`; backend and app code at that checkpoint were `8866f41a2` and
`9a4c029e3`.
Candidate checkout: `travel-workspace--functional-implementation-2026-09-20`,
branch `codex/functional-implementation-2026-09-20` in all three independent
repositories. Earlier workspace receipt `b127a54` records the initial exact
Home-selected Place continuity acceptance. The exact Home Outcome return
implementation is in app `0924ff1e5`; app `e2c0bafb1` adds the stronger
Keep-after-reopen flow contract and runner safeguards. The September 22 child
merges integrated sibling commits `d7d153810` and `cd70c7111`; the app merge
also contains the `dominant_unit_id` ordering fix and regression. The latest
app commit at that checkpoint, `9a4c029e3`, adds a selected-note fail-closed
regression only. The
workspace, backend and app candidate checkouts were clean at inspection; the
canonical workspace checkout has unrelated user changes and was not touched.
Canonical main and its concurrent work remain untouched. The candidate is
committed in its lane, not landed on main or released. Recheck Git and ownership
before execution; this is a dated observation, not a locked dispatch base.

### September 22 Places World Field — integrated candidate receipt

The World Field from the sibling lane has been merged into this candidate:
workspace source lane `58e45dc`, backend source commit `d7d153810`, app source
commit `cd70c7111`; resulting candidate merge commits are backend `8866f41a2`
and app `933f004f8`. The server elects one lead with bounded branches/doors;
the app respects that exact identity when kind-partitioning the semantic field.
The regression covers a returned-understanding unit elected as dominant so
mature browse cannot displace it.

On the merged tuple, backend `tests/root_projection` passed **454 tests** and a
focused Source/Places packet passed **81 tests** (overlapping scopes, not
additive). The app focus packet passed **25 suites / 314 tests**; TypeScript,
contract typecheck and the **31**-scenario registry passed; targeted ESLint
reported zero errors and one existing max-lines warning. The combined native
`90-places-full-scroll` passed on iPhone 16 Plus / iOS 18.2 with the isolated
lane API/Postgres and complete internal four-root gates. It presented the
server-elected Source lead, public Place reading, recipient-consented friend
note, reopened saved-place notice and retained Place in one scroll. All runner
fixtures were cleaned, and the exact temporary QA account was deleted with an
empty residual scan. The provider-free fixture was run with background work
disabled; a local sentinel satisfied the backend key-presence guard, and no
external model call was made.

The separate registered mock polish flow still fails its forced
`places-search-loading` assertion before screenshot capture; structural design
checks do not have the external canon attached. Therefore the integrated field
has named content/runtime acceptance, not comprehensive design parity,
recurring supply or release acceptance. Home's missing design-aligned full
scroll is the next substantial build.

| Capability | Implemented / recorded evidence | Remaining product or evidence boundary |
| --- | --- | --- |
| Home / Places | Owner-backed Save/readback, public Place and child-entity readings, consented place pulls, nearby open-now options, supplied experience comparisons, plural social perspectives, addressed Place contributions and recipient Keep/Leave-aside; exact Home-selected handoff ID/revision survives navigation into its canonical Place and is read from the relationship owner without fallback; native multi-source scrolls and partial-read treatment; fixed fictional Home sample behind existing delivery gates; Home Outcome excerpts capped at 220 characters with exact revisioned Life door; exact Outcome routing and Life-row selection covered by **61 app route/reader tests**; exact Home photo tap gated by current delivery revision and material authorization; persisted Home public-Place HTTP readback and named local API/iOS flows; secondary Home composition card-containment correction with **12** focused tests and one registered mock native capture | Exact Home Outcome → Life record → Home return passed on iPhone 16 Plus / iOS 18.2: the selected `outcome.<id>` opened and Back restored the same Home unit; the runner verified fixture withdrawal from Home and Life, with **4/4** runner-contract tests passed. The separate exact-note native Keep path also passed on iPhone 16 Plus / iOS 18.2: selected note opened, Keep advanced owner revision 0→1, exact owner reread confirmed revision 1, and Home return removed the handled inbox unit. The latest renderer capture is mock-only and one posture; it does not replace the earlier three-family owner-backed Home scroll or establish design parity. Addressed Place-note withdrawal/expiry remain unproven. Standard-gate inventory was last recorded as 55 expired API-policy reviews, 59 expired schema-bridge exceptions, and 12 query-key ownership findings; recheck before landing. **Next product build:** implement a substantially richer, design-aligned Home composition from currently supported owner material. First distinguish present-but-unrendered sections from genuine supply gaps; then connect useful variety, dynamic importance, and source/action/return coherently across the full scroll. Validate on the actual current Home design reference and representative Home postures as part of the build. No new generator/store to manufacture fullness. Still open: fixed sample native presentation/retirement, ordinary empty states, binary-media runtime proof, selected-note withdrawal/expiry, comprehensive native visual acceptance/parity |
| Life | Retained text originals, exact refinding/return, explicit place- and people-bound sources, organized period groups, and a canonical artifact reader that presents every available authorized photo whole with same-record return; metadata refinding continues past the newest 100 results with a versioned keyset cursor and rechecks current owner, retention, status and custody on each page; the continuation case passes on a fresh lane-local disposable PostgreSQL database; Life opens an explicitly linked Place from a retained source/original with anchored return; persisted private Plan and explicitly permissioned shared Outcome reach Life/People root and depth HTTP readers | Broader binary-media/corpus coverage and People/Threads experience, live original-byte/device acceptance, later permitted reuse that changes a subsequent result, indexed serving cutover and Atlas retirement |
| Social | Existing-owner venue-bound pulls and one-recipient original-text receiving through Life/Home; recipient Keep/Leave-aside; named local API/iOS flows; native sender withdrawal after recipient disconnect | Casual media/group/gathering breadth and useful juxtaposition; no new sharing or friend-source AI-use policy is adopted here; broader downstream use remains |
| Practical/live engine | Current open-now facts and saved-place changes affect surfaces; explicit fit contract and private stop-assistance/reviewed Send implemented | Provider-backed fit rehearsal, wider fresh-world coverage, purpose-preserving adaptation and accepted watching mandates; R09 code correction is complete, persisted/native timezone evidence remains |
| Preparation | Explicit Source work registered on the shared Arq rail behind production/worker/cohort gates; result serialization and bounded deterministic due-work recovery repaired | Real Arq/Redis wrapper and expired due-work recovery pass; a current disposable workflow also completed on the registered worker with `producer_silence`; exhausted final-attempt leases now close through the existing fence with 29 focused and 25 disposable-Postgres tests, including retry-budget recovery. Registration/recovery are not activation, and live output quality, cost and process-restart queue evidence remain unverified |
| Native / delivery | Specific real-owner happy paths now run through the internal four-root shell; Home v2 world-read timezone boundary is corrected and its focused screen suite passes; the fixed Home sample has not yet been observed on a native device | No comprehensive native/design acceptance, latest-tuple full gate, default-shell promotion, main landing or release |

No overall feature-completion percentage is asserted: these evidence scopes
are neither equally sized nor equivalent to design inventory coverage. The
review fixes have focused test receipts, but the ledger's remaining edge cases
and full contract gate must not be described as passed. A previous dependency
failure is not a standing tooling verdict: the inspected backend `.venv`
imports `openai`; the affected regression commands still need correct-environment
execution.

### Historical September 9 baseline

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
| Useful material with real depth and return | Home/Places now has owner-backed multi-source scrolls and a fixed low-context example; exact source/depth/return paths are established for named cases | Make the default portfolio genuinely varied and useful across sparse and richer situations; native-accept the cold-start example and widen only from measured owner-supply gaps |
| Recognizable, revisitable Life | Connect source evidence, organization and bounded readers; refind now paginates and a retained source can open its explicitly linked Place | Broaden supported media/corpus and People/Threads experience; demonstrate a permissioned later-use benefit before considering serving cutover or Atlas retirement |
| Enjoyable ordinary sharing | Complete durable sender controls and build on bounded original/pull receiving and refinding | Extend the same owners into supported media, gatherings and permissioned social intelligence; pending audience/use policies block only their dependent work; receiving never owes a reply or plan |
| Practical help within the same experience | Make supported facts change the appropriate offer while independent reading, saved and human value survives | Extend beyond opening status when a concrete timing/fit question requires it; accepted following and external changes need their own authority |
| Trustworthy combined delivery | Functional candidate committed in its isolated lane; preserve scoped receipts, open review items and explicit typing debt | Verify new product packages, cost, native/accessibility and rollout at their proper scope; main landing remains separate and paused; retire replacements only after obligation review |

These outcomes overlap. **On explicit dispatch, implement independent packages
without waiting for every design or policy.** An unavailable dependency blocks
its affected work, not the whole package. The emphasis is existing capabilities
becoming useful together, with consumer-path completion rather than more layers.
Reopen architecture when evidence exposes an owner or dependency contradiction.

## 4. Current package register

This register supersedes the September 9 dispatch as the forward queue. Its
technical work and exits live in
[Integration §9](complete-system-integration-roadmap-2026-09-05.md#9-current-execution-ledger-and-next-batch).
The earlier A/B handbacks remain supporting evidence, not active assignments.
These are work packages within I1–I5, not new subsystems or a redispatch of old
tasks. Lane-local implementation and verification do not resume shared
Integration/landing, publish code, or activate production flags.

| Package / role | Status and complete outcome | Dependency / handback |
| --- | --- | --- |
| **Primary build — Home design-aligned composition breadth** | Current isolated tuple is recorded in §2: workspace `0fe8e88`, backend `4357d1320`, app `93a9090de`. Home has ten bounded owner readers, a prepared private Source-contribution read, posture/region selection and 18 promoted semantic renderers. It receives exact saved-Place change notices, a conditional Home → Places Friends door, and now a bounded current public Place reading in the explicit-save seat. The latter preserves its accepted Source and exact Places destination; real HTTP/Postgres acceptance proves source retraction restores the save door and unsaving removes both. Focused source/portfolio tests passed **73**, offline root-projection tests **470**, bounded database query test **1**, and the saved-Place HTTP integration file **3**. Earlier evidence includes a three-family owner-backed Home scroll, exact Outcome/Place return paths, and the secondary-composition renderer correction. The audio-reader app change does not alter Home. These receipts establish connected slices, not a substantial, design-aligned Home composition, recurring supply, or visual parity; no Home design-ref manifest is registered in this lane. | **Build sequence:** **(1) Trace** substantial sections in the registered Home design authority (`docs/governance/home-surfaces-design-authority.json`) against real producers, candidate/read, selected region, renderer, destination/action and return. Verify the external canonical bundle and its hashes before visual acceptance; exploratory exports are not runtime contracts. The latest `vesper-home` proposal includes shared-photo-set and event concepts that current owners do not supply; do not infer shared-set identity from separate recipient grants or recast saved-venue notices as city events. Classify each remaining gap as already supplied but omitted, supplied but weak/repetitive in composition, or genuinely unsupplied; record owner and evidence for the last category. **(2) Compose** a coherent longer Home from supported material first, making importance, variety and hierarchy legible without turning it into an infinite feed or adding user homework. Extend a producer only where the trace proves a valuable missing outcome and its owner, evidence, privacy, freshness, lifecycle and return are already defined. No new generator/store, semantic kind or isolated card/route to simulate fullness. **(3) Accept** two materially different Home postures against a verified design reference and current code tuple: follow at least one exact source/depth/action destination and return; inspect whole-scroll hierarchy, sparse/pending/failure states, accessibility and polished native treatment. Do not count a fixture-only scroll, isolated card or transport seam as the outcome. **Closeout, not a competing milestone:** fixed Home-sample native presentation/retirement, selected-note withdrawal/expiry, ordinary empty states, binary-media runtime, comprehensive visual parity and standard landing gates remain separate. The registered Places mock `places-search-loading` assertion is a separate QA gap; its forced-state failure produced no screenshot. |
| **Complementary build — Life/social downstream value** | Persisted HTTP reads prove one private Plan and one explicitly permissioned shared Outcome through Life root and depth. The People-record seam preserves grant/member refs, exact destinations and explicit People-bound private anchors. Life's canonical artifact reader shows the authorized photo set and opens a selected original without cropping. Metadata refinding paginates beyond the former 100-result ceiling; Life's Places lens opens an explicitly linked Place from a retained source/original and returns to the anchored record. The canonical Intake reader now plays retained MP3/M4A/WAV after explicit tap through the existing authenticated GET; the slice is committed in app `93a9090de`, with 41 focused tests and TypeScript passing. Real media bytes, native codec/device playback, expiry-specific playback evidence, accessibility/polish and end-to-end owner read remain unproven. PDF/PKPass/HEIC/HEIF uploads are rejected pending scanner/decoder work, so PDF preview is not currently a valid feature gap. | Do not expand search into body semantics. Current recipient deliveries remain owned by Relationships and revalidated there; Life's root corpus does not read them, and its audience contract has only private/group/public. Do not encode a revocable one-to-one original as a durable Life record or mislabel it as group content. The Place door follows an owner-declared association; it does not prove attendance or later permitted reuse. Keep this audio work bounded to the authenticated original reader: no autoplay, transcription, AI interpretation, app-level export, share action, upload-format expansion, or later-use policy. Do not add a new operation or widen the image/text original-delivery MIME allowlist as part of this Life reader. Complete real-media, device, expiry, owner-read and accessibility/polish acceptance when the supported runtime is available. Keep Home's design-aligned composition breadth as the primary product build; Life acceptance follow-up must not turn into a new shared schema or policy lane. Defer policy-dependent social/media reuse. |
| **Non-blocking review closeout — R02/R05/R06/R09 evidence** | All 11 confirmed code findings in the September 21 review ledger have code-level fixes; this is not equivalent to closing every acceptance boundary. R01/R03 disposable-Postgres authority/revocation regressions pass. R04 sender withdrawal has API and native evidence at its named one-recipient text scope. R05 has lease/recovery code, a real Arq/Redis wrapper and expired due-work recovery evidence. R09's timezone propagation correction has focused regressions. | Still open are the governed outsider/cohort/release matrix for R02; a real process-kill/restart and live transient-provider failure/retry for R05; deployed expanded-place scale/cost evidence for R06; and persisted/native cross-device, date-boundary and DST evidence for R09. Run only in the correct disposable/runtime environments. These remain necessary for their named readiness/landing claims but do not gate independent Home implementation. See the [review ledger](functional-implementation-code-review-2026-09-21.md) for exact boundaries. |
| **Across both builds — native polish** | Required within each completed surface: design hierarchy, card/media treatment, interaction, accessibility and sparse/pending/failure states. Not accepted yet. | Use current inspected Claude exports and handoffs; record actual canvas/version. Unresolved visual choices do not block unrelated owner/supply work. |
| **Orchestration / this thread** | Own scope, current queue, cross-system decisions and package review; dispatch only when requested. | Review first working composition, consequential blocker and completed package. Judge delivered behavior and remaining user effort, not commit/test counts. |
| **Dedicated Integration / landing** | PAUSED; combined shared runtime, main landing and publishing are not enabled by this update. | Lane-local implementation/verification remains distinct. On explicit resume, receive selected clean cuts and run required gates without pretending candidate receipts certify production. |
| **Existing specialist lanes** | Reference suppliers, not automatically restarted or assumed merged. | Use immutable relevant cuts; independently assigned work needs file ownership and direct dependency exchange, not six standing lanes matching six design projects. |

**September 22 current-tuple clarification:** The Home selector/screen tests and
single mock native capture named in the detailed Home row are earlier receipts,
not fresh verification of the current code tuple. The current isolated tuple is
workspace `0fe8e88`, backend `4357d1320`, and app `93a9090de`. Backend
`18e1fb377` / `4357d1320` add a bounded source-backed reading for an explicit
saved Place and real-Postgres Home HTTP proof of source retraction and unsave;
the app has no corresponding Home renderer change, and no current-tuple Home
visual acceptance was run. This adds one useful owner-backed Home path but does
not change the next package: trace and build a substantially richer Home from
material its owners actually supply, including the still-open private,
cross-time returned-value contract, then accept that composition against a
verified design reference and representative postures.

The primary and complementary builds can advance together after file boundaries
are assigned. Share contract needs early; reserve one writer for schema sync,
root composition and device/runtime resources. Use longer outcome assignments
through implementation and focused review, escalating product/authority choices
or real dependencies rather than every ordinary repair. No fixed integration
ceremony is added. Required pre-push gates remain required.

**September 22 Home design/source boundary:** the latest `vesper-home` Claude
board is useful design input, but it is not among the seven files registered by
the active hashed Home/Places design authority. `HOME_SURFACES_CANON_DIR` is
unset in this lane, so no visual acceptance against that bundle was possible.
The current data model also cannot honestly render two attractive ideas from
the newer board as if they were already supplied: Relationship original
deliveries are individual grants with no shared photo-set/Occasion identity,
and the saved-Place closure/reopening/weather notices are exact saved-venue
changes—not city-scoped dated service notices. Do not group deliveries by
time/place, or promote those notices into `horizon_world_fact_row`. Keep Home
composition work moving with currently owner-backed material; any slice that
needs either missing identity/source must first establish that owner's contract
and evidence rather than infer it in the renderer.

At each substantial handback, update §2 and this register in place: what became
useful, what supplied it, how it behaves after action/correction/return, what
design coverage remains, and which evidence actually ran. Preserve underlying
receipts, but do not append another current execution queue.

### September 9 dispatch record

Historical dispatch only. The current package register above replaces its
assignments and "next" language; permissions and unresolved evidence are not
silently broadened.

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

Use the [current design handoff index](claude-design-integration-2026-09-04/00-handoff-index.md)
to identify the active project assignment and export. Design proposals do not
amend accepted product decisions. Only a specific dependent anatomy/Plan
continuation waits for its applicable human decision; present assessment and
supported receiving continue. Package handbacks are evidence at their stated
boundaries, not complete-system or native acceptance claims.

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
| [Cross-project design assignments](claude-design-integration-2026-09-04/00-handoff-index.md) | Design owners propose; founder resolves consequential product/authority choices | Final purpose-responsive anatomy and prepared-assistance exception remain subject to their applicable decision; exact identity/context transport, supported facts, readback and existing renderers continue |

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

## September 21 E2 follow-through — Home source-backed reading depth

The same identity seam existed in Home's contextual Places adapter. A
source-backed editorial card carried its immutable `place_content_primitive`
source into Home, but the adapter dropped the canonical Place subject before
constructing the Places destination. Backend commit `b2fcbdd90` now preserves
the source and Place together in Home represented/owner refs, value-contract
subjects, and the typed destination resource set. Legacy dossier cards remain
unchanged, and the change reuses the existing Places subject resolver rather
than adding another identity abstraction.

Evidence: the focused Home portfolio and v2 contract packet passes **73
tests**; the new regression proves a Home source-backed reading carries both
the immutable source revision and exact Place continuation. Ruff, formatting,
vulture, boundary, and repository hooks pass. This closes the analogous E2
Home receiving gap but does not claim full Home/Places corpus parity, social
delivery, native tap/back proof for this newly covered path, production flag
activation, or Claude-design visual parity. The next useful slice is therefore
another supported receiving/action connection or the bounded native proof, not
a new content generator, store, or route family.

## September 21 E2 follow-through — preserve Home Places scope

The public Place-interpretation adapter also dropped the originating Places
context from its typed destination, even though it retained that context in
provenance. Backend commit `4eba46bcf` now emits the context, exact Place, and
immutable source revision together. The existing native resolver can therefore
open the exact reading while retaining the originating Places scope and Home
return token. The focused Home/Places backend packet remains **73 tests**;
Ruff, formatting, vulture, boundary, and repository hooks pass.

This is a destination-context repair, not a new route or content model. It does
not claim native tap/back execution for this newly seeded path, broad corpus or
social parity, production activation, or visual parity with Claude designs.
The next unblocked work remains another supported receiving/action seam or a
bounded native return proof.

The destination contract was then checked through the broader composition
boundary: the practical/root delivery packet passes **36 tests**, including
Home composition with the new context → Place → immutable Source ordering.
Backend commit `fc443b21d` updates the stale contract assertion; this is
verification of the production adapter path, not fixture-only insertion.

## September 21 functional implementation receipt — preserve Places reader context

The Places section composer had one remaining continuation defect: its Reading
producer rebuilt the automatic Places context even when the root had already
resolved an explicit `place:*` handle. The reading collection could therefore
be sourced from a different scope than the visible Places root. Backend commit
`8a22bf36d` forwards the resolved context handle into the existing reader while
leaving the exact Place-owned Source contract intact. No child-owned material is
relabeled as a Place reading; Home remains the bounded parent→child consumer,
and Places keeps its current exact Place destination semantics.

Evidence: `tests/places/test_collections.py` and
`tests/places/test_sections_feed.py` pass **29 tests**; Ruff, format and the
repository pre-commit hooks pass. This is a read-path continuation repair, not
a new generator, store, provider call, schema, flag activation, native capture,
or production rollout. A populated native Places Reading tap/back proof remains
open and should be exercised only with an admitted exact Place Source.

## September 21 functional implementation receipt — native Place reading continuity

The bounded native proof for the remaining Places Reading seam is now complete.
Backend commit `93e7889b7` adds a disposable local-Postgres fixture that creates
two accepted, policy-bound, exact Place-owned `interpretive_lens` Sources. It
does not widen the Places collection to child-owned material: the fixture and
the production reader continue to require `entity_ref.type = place`.

App commit `ff06e6ff9` adds `.maestro/76-places-public-reading.yaml` and its
runner/static contract. With the real local API, the flow proves: the exact
Place Sources appear in the scoped `place:1` Places workspace; a reading card
opens the immutable Place reader with the expected claim and interpretation;
Back returns to the same Places workspace and preserves the same reading card;
the runner removes all fixture rows and verifies the canonical collection no
longer exposes the Source. The native simulator run passed end to end, and the
runner's three static contract tests passed. The focused backend Places packet
remains **29 passed**, with Ruff, format, py_compile and repository hooks
passing.

This closes the narrow native Places Source → exact Place reader → scoped return
boundary. It does not claim broad content-corpus parity, provider supply,
production flag activation, Claude-design visual parity, or child-owned Source
support in the Places collection. The next useful slice should therefore move
to another supported receiving/action connection rather than add a new content
store, generator, or route family.

## September 21 functional implementation receipt — native Home child-owned Source continuity

The next Home receiving seam is now proven with a real local-Postgres fixture.
Backend commit `9553d602f` adds a disposable New York City child venue and one
accepted, policy-bound public `interpretive_lens` Source owned by that venue. It
temporarily anchors the selected account to the NYC Home area and restores the
previous Home location during cleanup. The fixture authorizes both the Home
notice and the exact venue reader's bounded interpretation consequence; it does
not create a booking, save, provider result, or generated artifact.

The same backend commit fixes the production Home adapter identity seam: the
immutable Source now appears in the active unit's `represented_refs` as well as
the destination and owner/source refs. Without that identity, the native return
registry correctly rejected the destination as containing a resource absent from
the unit that opened it. The regression packet and the Home/Practical root
packet pass **76 tests** with Ruff and formatting clean.

App commit `de621f0c0` adds `.maestro/77-home-child-source.yaml`, its real-API
runner, and three static runner/flow contract tests. On the iOS simulator, the
flow proved: the child-owned Source appears as a substantive Home reading;
opening it reaches the exact venue object reader with the fixture claim and
interpretation; Back returns to the same Home unit; cleanup removes the fixture
and the temporary Home anchor. App typecheck and the static packet pass.

This closes the narrow Home child Source → exact venue reading → Home return
boundary. It does not claim broad Home/Places corpus parity, social delivery,
provider supply, production rollout, or Claude-design visual parity. The next
useful slice remains another supported receiving/action connection or a bounded
Life/native return seam, not a new content generator, store, or route family.

## September 21 functional implementation receipt — native Life Places source continuity

The next Life seam is now proven with a real local-Postgres fixture. Backend
script `provision_life_places_source_return_rehearsal.py` creates one
disposable venue and one retained inline source whose typed
`capture_context.subject_entity_ref` points to that venue. The fixture verifies
that the retained-source owner preserves the explicit venue association, then
withdraws both the source and venue during cleanup. It does not claim that the
owner visited the venue or create an occurrence, booking, provider result, or
new Life model.

App commit `de621f0c0`'s native Life root is exercised by the new
`.maestro/78-life-places-source-return.yaml` runner and its three static
contract tests. With the real local API and iOS simulator, the flow proves:
the source appears in Life's Places lens; its exact entry opens the canonical
Intake original-material reader; Back returns to the same Places lens and
entry; cleanup withdraws the source and the HTTP Places-lens projection no
longer exposes it. The run passed end to end, with the existing Life return
resolver preserving `lifeLens=places`.

This closes the narrow Life Places source → exact original → Places return
boundary. It does not claim broad Life corpus population, semantic place
attendance, social delivery, provider supply, production activation, or
Claude-design visual parity. The next slice should therefore move to another
supported receiving/action connection or a bounded practical/social seam,
not add another content store, generator, or route family.

## September 21 functional implementation receipt — recipient-consented Places social pull

The existing multiplayer seam is now re-run on the same real local API and
iOS simulator. Backend fixture `provision_places_social_pull_rehearsal.py`
creates a disposable sender, venue, accepted graph binding, recipient-consent
grant, and expiring `PLACE_PULL` handoff. It reads through the canonical
relationship repository and removes the sender, graph, venue, and handoff rows
on cleanup; it adds no social ranking, public feed, or second social store.

The existing `.maestro/75-places-real-social-pull.yaml` flow proves: a
recipient-consented note appears in the scoped Places workspace under “From
your people”; the friend contribution opens the exact canonical venue owner;
Back returns to the same Places context with the contribution still present;
cleanup withdraws the handoff and the canonical feed no longer exposes it.
The native run passed end to end, and the three static runner/flow contract
tests passed.

This closes the narrow social pull → exact Place → scoped return boundary. It
does not claim general social publishing, multiplayer occasion composition,
Home social delivery, notification cadence, production activation, or Claude
visual parity. The next slice should target another supported practical or
Home receiving connection, not add a second social model.

## September 21 functional implementation receipt — Home addressed social receiving

The companion Home multiplayer seam is now packaged and proven. The existing
Places social fixture accepts a `SEND_NOW` mode without changing its default
recipient-consented `PLACE_PULL` behavior. It creates the same disposable
sender, venue, graph binding, personal pair, and expiring handoff, then removes
the sender account and graph/venue rows during cleanup.

The new `.maestro/79-home-real-social-send.yaml` runner first verifies the
canonical `/api/root-projections/v2/home` response contains the exact
`home.place-handoff.<handoff>` unit, attributed read, and venue destination.
The native flow proves: the note appears on Home, the exact venue opens, Back
returns to the same Home unit, and cleanup withdraws it from the projection.
The iOS run passed end to end; the three static runner/flow tests and app
typecheck passed. The existing Places `PLACE_PULL` flow was re-run afterward
and also passed, confirming the mode extension did not regress Places social
receiving.

This closes the narrow addressed social note → Home → exact Place → Home return
boundary. It does not claim general social publishing, multiplayer occasion
composition, notifications, production activation, or Claude visual parity.
The next slice should target a supported practical/current-world action or a
different bounded receiving seam, not add a second social model.

## September 21 functional implementation receipt — Home practical/open-now possibility

The next functional slice is complete. The Places nearby producer is now
eligible in anchored `quiet` and `starter` contexts, so Home can surface a
bounded current-world possibility even when no trip is active. It reuses the
existing nearby corpus/taste floor, operational cache, common admission
contract, and Places destination; no provider call, booking flow, or new
recommendation store was introduced.

Backend commits `596bc9429` and `ade6d0e0a` add the serving correction, owner-doc
update, regression coverage, and a
disposable fixture that writes three verified NYC venues with ten-minute
`open_now` evidence into the existing cache. App commits `cbef1acaa` and
`13e981a20` add the real API/iOS Maestro flow and static runner contracts. The
native run passed: Home
showed the typed `place.open_now` assessment, opened the exact fixture venue,
and returned to the identical Home unit. Fixture cleanup withdrew all status,
venue, and temporary-home rows. Evidence: **69** focused backend tests, **3**
static app tests, TypeScript pass, and real simulator pass.

The receipt is bounded: it does not claim live provider acquisition, route or
fit-window evaluation, booking, notifications, production activation, or
Claude-design parity. Keep the next implementation wave on existing producer →
owner-read → native destination → return chains; reassess after each complete
loop before widening the grammar or adding infrastructure.

## September 21 functional implementation receipt — cross-root Home → Places → Life continuity

The current lane now has a combined native checkpoint across the four-root
shell's receiving and continuity seams. App commit `a9e466e61` adds the real
local-API Maestro flow and runner `81-cross-root-home-places-life`. It composes
two already-supported disposable fixtures: an addressed Home `SEND_NOW` venue
handoff and a place-bound retained Life source. No new store, provider,
generator, social model or route family was added.

The simulator run passed through Home social value → exact venue object → the
Places root → Life's explicit Places lens → the canonical original reader →
Life return. Cleanup removed both fixtures and HTTP checks confirmed their
withdrawal from Home and Life. The runner's **3 static contract tests**,
`bash -n`, and child-repository diff checks passed. This is stronger than the
individual flow receipts because it proves the same shell can leave one root,
enter another, and still preserve exact owner-backed return behavior.

The evidence remains bounded: it does not establish a shared occasion across
the fixtures, broad group/media sharing, binary-original playback, provider
acquisition, production activation, design parity or release readiness. Keep
the next slice on a remaining supported user-visible capability, preferably
Life organized-record native depth or another practical consequence, rather
than adding integration infrastructure.

## September 21 functional implementation receipt — native Life organized record

Life organization now has a real simulator proof, not only projection tests.
Backend commit `a397b94e5` makes the retained-source rehearsal call the
existing owner-maintenance boundary so its period-group materialization and
withdrawal callbacks are exercised. App commit `00e117c71` adds the real-API
Maestro runner and flow `82-life-organized-record`.

The run passed through Life Time → organized views → the current period group
→ the group-scoped record containing the exact retained source → Life return.
The runner withdrew the source and derived group afterward and verified both
were absent. Evidence: **315** focused backend Life/API tests, **3** static
mobile contracts, TypeScript, and a real iOS simulator pass. This is one
conservative period-group path; people/thread grouping, semantic attendance,
binary original playback, social adoption, production activation, design
parity and release readiness remain outside the claim.

## September 21 functional implementation receipt — saved-place closure consequence

Places now has a real-runtime proof for a current-world change to something the
traveler deliberately saved. Backend fixture
`provision_places_saved_closure_rehearsal.py` creates one disposable canonical
venue, one private Save through `create_save_with_effects`, and fresh
normalized `permanently_closed` evidence in the existing provider-status
cache. No provider call, booking, trip, or second notice store is introduced.

The new app flow `.maestro/83-places-saved-closure.yaml` and runner prove on
the local API and iOS simulator: the saved-place notice appears in the
canonical scoped Places feed; the user clears the exact notice; the notice is
absent on the subsequent feed read; and the underlying Save is still present.
Cleanup then removes the fixture venue, cache row, Save effects, and dismissal
event. The owner-level rehearsal also passed directly: `changed` emitted the
closure card, `clear_places_notice` recorded a neutral dismissal, the card
disappeared, and the Save remained.

Backend commit `5bbba47cc` and app commit `f06a309dc` carry the fixture and
native flow. Evidence: backend return/section tests passed **52**; the new
static mobile contract passed **3**; shell syntax, Python compilation, Ruff,
and formatting passed; and the real native flow passed end to end on simulator
`D7C8FEF4-237B-4347-841C-6FE920BFABFA`. This closes one practical consequence
loop (current-world evidence → user-controlled dismissal) without claiming
provider acquisition, alternative selection, notifications, or broad Places
parity. The next wave should continue the same bounded owner/destination/
return discipline, with the roadmap re-evaluated after another complete
user-visible loop rather than widening infrastructure.

## September 21 functional implementation receipt — saved-place reopening consequence

The positive counterpart to the saved-place closure path is now proven against
the same existing current-world owner path. Backend commit `908b0a600` adds a
disposable rehearsal that creates a private Save, writes fresh normalized
operating-status evidence showing a venue reopen, and emits the existing
`changed` notice with the exact `OPEN AGAIN` assessment. It does not add a
provider, scheduler, notification channel, or second notice store.

App commit `179235f76` adds `.maestro/84-places-saved-reopen.yaml`, its
run-scoped runner, and static contracts. The real local API/iOS simulator flow
passed: Places displayed the saved venue's reopening notice, the user cleared
that exact notice, the notice disappeared on the next feed read, and the Save
remained present. Cleanup removed the temporary venue, cache evidence, Save
effects, notice and claims. The direct owner rehearsal also passed before the
native run.

Evidence: **367** focused backend tests, **12** combined static mobile
contracts, TypeScript, shell/fixture checks, and the real native flow passed on
simulator `D7C8FEF4-237B-4347-841C-6FE920BFABFA`. This closes the bounded
current-world reopening consequence, not provider acquisition, scheduler
activation, notifications, alternative selection, broad Places parity,
production rollout, or Claude visual parity. Continue with the next supported
user-visible producer → owner read → destination → return seam and reassess
after another complete loop.

## September 21 functional implementation receipt — native Life original refinding

Life's bounded original-refinding path now has a real native proof. The
existing `provision_life_real_source_return_rehearsal.py` fixture admitted one
retained text source through Capture and the Life owner; no new index, corpus,
search owner or storage model was introduced. App commit `ac23512b9` adds
`.maestro/85-life-original-refind.yaml`, its real-API runner, and three static
contracts.

The local API/iOS simulator flow passed: `/api/life/originals/refind` returned
the exact source metadata, Life Search rendered the matching original, the
user opened the canonical Intake original reader, Back returned to the same
Life Search query, and cleanup withdrew the source. A post-cleanup refind read
confirmed the deleted source was no longer exposed. The default-off
`EXPO_PUBLIC_LIFE_REFIND_LANE` was enabled only in the local development build.

Evidence: **15** combined static mobile contracts, TypeScript, shell/fixture
checks, and the real native flow passed on simulator
`D7C8FEF4-237B-4347-841C-6FE920BFABFA`. This closes native refinding for one
owner-authorized retained source, not whole-history search, semantic body
indexing, shared-original breadth, production flag activation, visual parity,
or release readiness. Continue with another supported producer → owner read →
destination → return seam and keep the refinding bounds explicit.

## September 21 functional implementation receipt — native recipient original delivery

The approved one-recipient original-sharing seam now has a real native
recipient proof. Backend commit `212c185cb` adds a disposable fixture using
the existing Relationships owner: a temporary sender, active pair
conversation, verified inline text source, and exact one-recipient delivery
to the local QA account. It adds no audience model, copy store, notification
path, or new custody authority.

App commit `c3471c169` adds `.maestro/86-life-original-delivery.yaml`, its
real-API runner, and three static contracts. With the UUID relationship and
Life-refind gates enabled only in the local internal development build, the
iOS simulator flow passed: Life showed the current shared original, the
recipient opened the exact original-material reader, the text bytes rendered,
Back returned to the same Life results, and cleanup withdrew the delivery and
temporary sender/source rows. The post-cleanup recipient list no longer
contained the delivery.

Evidence: **18** combined static mobile contracts, TypeScript, Python
compile/Ruff/format checks, backend commit hooks, and the real native flow
passed on simulator `D7C8FEF4-237B-4347-841C-6FE920BFABFA`. This closes the
native recipient-side original-read/return boundary for one retained text
source, not binary-media breadth, guest/group audiences, onward sharing,
production flag activation, visual parity, or release readiness. Keep the
existing exact-source, current-custody and one-recipient bounds while moving
to the next supported producer or consequence seam.

## September 21 functional implementation receipt — native Home original delivery

The one-recipient original-sharing seam now reaches Home as well as Life.
Backend commit `b08f28bf1` maps `relationship.original_delivery` through the
shared owner-read compiler and canonical relationship reader, preserving
recipient, active-status, expiry, represented-at, and exact-source checks.
App commit `1142de74f` adds the real-API Maestro flow and runner
`87-home-original-delivery`; it introduces no new audience, copy, notification,
or custody system.

The local API/iOS simulator rehearsal passed after restarting Metro with a
clean governed-shell bundle: Home showed the current addressed original, the
recipient opened the exact material reader, the inline text rendered, Back
returned to the same Home unit, and cleanup withdrew the delivery and temporary
sender/source rows. Evidence: **67** focused backend owner-read/portfolio
tests, **6** static mobile contracts, TypeScript, Python compile/Ruff, and the
real native flow passed on simulator
`D7C8FEF4-237B-4347-841C-6FE920BFABFA`.

This closes Home placement and exact return for one retained text original,
not binary-media breadth, guest/group audiences, onward sharing, notification
delivery, production flag activation, visual parity, or release readiness.
Keep the exact-source, current-custody, one-recipient bounds and continue with
the next supported producer → owner read → destination → return seam.

## September 21 functional implementation receipt — controlled Source worker rail

The explicit Source preparation path now connects to the existing shared Arq
worker rail without changing the product surface. Backend commit `913f5a7ae`
adds `run_root_source_contribution`, which reuses the existing
workflow lease, canonical owner-read executor, retained-production readback,
telemetry and exact result reader. The request route dispatches only when the
existing producer gate and a separate worker gate are enabled with a named
cohort; `WorkerSettings` registers the job under the same condition, and the
shared queue refuses inline execution for it. No new queue, provider, result
store, or ordinary Home/Places production path was introduced.

Evidence: **31** focused backend tests passed across the deployment contract,
feature flags, request JSON/dispatch boundary and worker registration, plus
Ruff and Python compile checks. The default remains dark: without
`ROOT_SOURCE_CONTRIBUTION_PRODUCTION_ENABLED=1`,
`ROOT_SOURCE_CONTRIBUTION_WORKER_ENABLED=1`, and a non-`none`
`ROOT_SOURCE_CONTRIBUTION_WORKER_COHORT`, the worker is not registered and
submission only persists the existing content-free workflow. This is an
implementation/rail receipt, not controlled provider activation, cost
approval, production scheduling, or proof of a generated result. The next
checkpoint is a separately authorized local/dogfood Redis execution with a
real source/context fixture and native result readback; do not enable these
environment gates by default.

## September 21 checkpoint — practical fit is implemented; provider-backed rehearsal deferred

The explicit `place.fit_window` path was re-traced before selecting another
slice. The current branch already carries the complete bounded contract: the
object page captures a current opaque origin, Places resolves it under the
current account/session, the backend performs exact Place/route/commitment
owner reads, the composer binds a supported/unsupported/unknown assessment,
and the native semantic renderer preserves expiry, independent Place value and
the existing destination/return behavior. Focused backend and mobile coverage
is green.

The remaining gap is evidence, not missing product code: a real native run would
invoke request-only routing and therefore requires an explicitly authorized
routing credential and device-location setup. No fake route cache, duplicate
route owner, default provider call or fixture-only "fit" claim is added. Until
that authority exists, the honest unknown/fallback path remains the supported
behavior and the next implementation should be another existing
owner → destination → return seam or the separately authorized Source-worker
dogfood checkpoint.

## September 21 functional receipt — composed Home reading value admission and native continuity

The composed same-place sequence is now proven through the canonical value
admission path and native return, not merely candidate production. Backend
commit `8109a6ad6` fixes a low-context admission seam: `NOT_APPLICABLE`
personal novelty no longer collapses source-bound compositions to
`below_value_floor`; only explicit `KNOWN_TO_PERSON` repetition suppresses
them. Evidence and epistemic-yield checks remain in force, so this preserves
the low-context promise without inventing novelty. The commit also records the
two-reading fixture field (`reading_count`) for the existing run-scoped
rehearsal.

App commit `9f6126671` arms fixture cleanup before dynamic projection lookup,
so jq/API failures cannot orphan run-owned venues/source rows or the temporary
Home anchor. The existing `8cd899b6d` navigation contract and `c18470b4a`
two-reading fixture remain the underlying route/fixture commits.

With the local replay API (placeholder key `local-test`,
`DISABLE_LLM_BACKGROUND_LOOPS=true`), explicit lane database/account, governed
shell flags (`FOUR_ROOT_SHELL`, `ROOT_PROJECTION_V2`, Places/Life gates,
internal build) and `OBJECT_PAGE_REBUILD_ENABLED`, iOS flow
`78-home-public-reading-sequence` passed: canonical Home V2 emitted both
accepted readings as one `composition` unit; the exact venue/Object Page
opened; both reading texts rendered; Back restored the same Home unit; and
cleanup removed fixture rows and restored the Home location. Simulator UUID:
`D7C8FEF4-237B-4347-841C-6FE920BFABFA`.

Evidence: backend Home/value packet **82 passed**;
`rootProjectionNavigation` **45 passed**; static flow/runner contracts **3
passed**; TypeScript, shell syntax, Ruff, formatting and Python compilation
passed; and the real native flow passed. The first native attempt used the
legacy Expo bundle and is not counted; the corrected governed-bundle run is
the acceptance evidence above.

This closes the low-context Home source sequence → exact entity → Home return
boundary. It does not claim broad corpus parity, provider supply, production
flag activation, social breadth, visual parity with Claude designs, or release
readiness. Next work should select another supported producer/action seam, not
create another sequence architecture.

## September 21 functional implementation receipt — native Home full-scroll across three owner families

The next substantive Home/Places package is now proven as one composed native
scroll rather than three isolated happy paths. App commits `1b3396ebc` and
`7427b1833` add flow `89-home-full-scroll`, its static contract test and a
run-scoped runner with typed destination preflight.
The runner reuses the existing disposable owner writers—two accepted public
Place readings for one child venue, one addressed human Place contribution,
and one recipient-authorized text original. It adds no generator, provider,
feed, custody, audience or storage system.

With the local replay API (placeholder key `local-test`,
`DISABLE_LLM_BACKGROUND_LOOPS=true`,
`RELATIONSHIP_UUID_HANDOFFS_ENABLED=true`), explicit lane database/account,
and the governed four-root/Object Page bundle, the iOS simulator flow passed.
The canonical Home projection contained all three substantive families; the
flow scrolled to the addressed contribution, the public Place composition and
the original preview, rendering their attributed copy and waiting for the
authorized original material to arrive instead of accepting the loading
placeholder. Screenshot: `home-full-scroll`. The runner then removed every
fixture and restored the Home anchor. Simulator UUID:
`D7C8FEF4-237B-4347-841C-6FE920BFABFA`.

Evidence: the new static runner/flow packet **3 passed**; the flow passed
Maestro syntax validation; TypeScript passed; and the real native flow passed
end to end. The first exploratory pass correctly exposed that original
material is asynchronous; the final flow waits for the caption after the
loading state. This is a supplied local owner proof, not a production corpus,
provider-backed generation, recurring supply, social breadth, visual parity or
release-readiness claim. The next build should move to another substantive
owner/action seam or bounded Life downstream value, not duplicate this
full-scroll harness.

## September 21 functional implementation receipt — native Places full-scroll across reading, social, and change

The Places counterpart is now proven as one composed native scroll rather than
three isolated cards. Backend commit `35765fdb5` closes the admission seam that
was exposed by the governed runtime: a typed saved-place change notice now
resolves its exact venue owner through the reviewed notice grammar. Generic or
unrecognized notices remain ownerless and fail closed; the v2 adapter does not
invent a venue or add a second notice producer.

App commit `e4a4823d5` adds flow `90-places-full-scroll`, its static contract
test, and a run-scoped runner. The runner composes the existing disposable
owner writers for one accepted public Place reading, one recipient-consented
`place_pull` contribution, and one saved-place reopen notice in the same
`place:1` workspace. It preflights the canonical reading/feed responses,
scrolls through all three source families, and checks the saved-place notice's
user-controlled `OPEN AGAIN` action. Cleanup is armed before the first dynamic
projection lookup and verifies that the public reading and notice withdraw
after the run.

Using the local replay API (`AI_MODE=replay`, placeholder key `local-test`,
`DISABLE_LLM_BACKGROUND_LOOPS=true`) with
`RELATIONSHIP_UUID_HANDOFFS_ENABLED=true`, `PLACE_HANDOFF_PULL_ENABLED=true`,
`PLACE_CONTENT_PRIMITIVE_READS_ENABLED=true` and
`CONTENT_CONTROL_PLANE_PLACE_ENABLED=true`, the governed four-root/Object Page
bundle passed on simulator
`D7C8FEF4-237B-4347-841C-6FE920BFABFA`. The public reading claim, “From your
people” contribution, and saved-place reopen notice all appeared in one real
Places scroll. The existing standalone saved-reopen flow was rerun afterward
and passed through notice dismissal and retained-place return.

Evidence: the focused backend typed/generic notice packet **2 passed**;
backend commit hooks passed; the new mobile static packet **3 passed**;
Maestro syntax, shell syntax and TypeScript passed; the combined native
full-scroll flow passed; and the standalone saved-reopen native flow passed.
This is a local supplied-owner proof. It does not claim provider-backed
generation, production corpus breadth, recurring social supply, notifications,
alternative selection, broad visual parity, or release readiness. The next
useful slice is another supported producer/action seam or bounded Life
downstream value—not another parallel Places scroll harness.

## September 21 functional implementation receipt — native sender withdrawal after recipient disconnect

The remaining R04 native boundary is now proven. App commit 9452f09d9
corrects the existing sender-control flow to scroll to the real history row
before asserting its controls and to verify the post-withdrawal source state.
The runner now checks the authoritative sender-history response after the
gesture: the exact delivery is revoked at revision 1 before cleanup. It does
not broaden recipient eligibility or introduce another sharing owner.

With the local replay API (placeholder key local-test,
DISABLE_LLM_BACKGROUND_LOOPS=true), the governed internal bundle used
EXPO_PUBLIC_RELATIONSHIP_UUID_HANDOFFS_ENABLED=true and the existing
Life/Object Page flags on simulator
D7C8FEF4-237B-4347-841C-6FE920BFABFA. The disposable fixture used the
existing QA sender, created a temporary recipient and exact retained text
original, then disconnected that recipient after delivery creation. The native
flow showed the sender-owned history and Withdraw control, withdrew the
delivery, confirmed the control disappeared, and retained the original
material. The runner verified status=revoked/revision>=1, then removed the
temporary delivery and recipient while preserving the sender.

Evidence: the static sender-flow packet 3 passed; Maestro syntax and shell
syntax passed; and the real iOS native flow passed end to end. The initial
attempt exposed two honest harness issues—no scroll to the below-fold control
and an incorrect expectation that an empty post-withdrawal recipient state
would retain the send section—both were corrected without changing product
behavior. This closes native R04 sender control for the exact one-recipient
text-original scope. It does not claim group/media sharing, broader audience
policy, notifications, production activation, or visual parity. Remaining
review evidence is R05 process-restart/transient queue behavior and R09
persisted/native timezone edges.

## September 21 functional implementation receipt — recipient controls on the rebuilt Places reader

The exact-place friend line now completes its recipient-side lifecycle in the
rebuilt venue reader. App commit `072f56488` invalidates the Places feed after
the fresh owner read reports a terminal handoff and after recipient actions;
the existing owner action still refreshes Home projections and the exact
handoff query. This closes a stale-return case where the detail page hid a
Leave-aside line but the Places feed could briefly continue to show its card.

The real native rehearsal uses a run-scoped disposable PostgreSQL fixture and
proves the canonical Places feed and entity People-lines response before UI
automation. On simulator `D7C8FEF4-237B-4347-841C-6FE920BFABFA` (iOS 18.2),
the app showed the recipient-consented contribution, opened the exact venue
through `venue-detail-screen-rebuild`, displayed the authorized People-line
sheet, accepted Keep, then Leave aside, returned to the same Places context,
and no longer represented the dismissed friend card. The runner completed
owner cleanup and verified the post-cleanup Places projection. It now accepts
`VESPER_MAESTRO_UDID` so the selected simulator is explicit.

The lane used only local internal opt-ins
(`EXPO_PUBLIC_IS_INTERNAL_BUILD=true`,
`EXPO_PUBLIC_OBJECT_PAGE_REBUILD_ENABLED=true`,
`EXPO_PUBLIC_RELATIONSHIP_UUID_HANDOFFS_ENABLED=true`) and local API flags
(`SKIP_AUTH=true`, `RELATIONSHIP_UUID_HANDOFFS_ENABLED=true`,
`PLACE_HANDOFF_PULL_ENABLED=true`); AI/provider-backed generation and
background LLM loops were disabled. Evidence: the native
`run-places-real-social-pull.sh` passed end to end; the focused owner-action
Jest packet passed **4/4**, runner-contract tests **3/3**, targeted ESLint, app
TypeScript, shell syntax, and `git diff --check` passed. An initial rehearsal
exercised the compatibility renderer because the local rebuilt-page opt-in
was absent; that was not counted as acceptance. The corrected explicit-flag
run passed.

This closes one recipient-only Keep/Leave-aside and return boundary for a
venue-bound text contribution. It does not establish general multiplayer
parity, broader Places visual parity, production activation, group/media
sharing, or release readiness. Continue with the next substantive Home/Places
owner/value gap; do not infer a new social subsystem from this slice.

## September 21 functional implementation receipt — direct Home photo opening

Home's existing one-recipient original reader now lets the recipient open an
image original by tapping the image itself. The affordance is available only
when the exact projected delivery revision is confirmed active and the current
material authorization is ready. Authorization failure, material failure or a
stale delivery does not expose an interactive photo. Text originals retain the
explicit **Open original** action; an image also retains that fallback while it
is not currently eligible for direct opening. The tap reuses the existing
destination callback and original-reader/root-return path.

App commit `e7c3b0954` adds the accessible image action and Home gate. Evidence:
**52** focused tests across the original-material surface, Home original
delivery, Home renderer registry and adjacent Places expiry suites; app
TypeScript and targeted ESLint passed with zero errors (one pre-existing
max-lines warning in the Home renderer); `git diff --check` passed. This is
component/screen evidence only: no live image-byte/API fixture or simulator
run was performed. It does not prove binary-media reliability, the full
multi-photo composition, Reply/Ask/share behavior, production activation,
visual parity or release readiness. Keep broader media support as open work
and do not treat this affordance as an album or sharing-system implementation.

## September 21 functional implementation receipt — retryable Home image preview

Home now keeps a failed recipient-photo preview inside its original 4:3 media
frame and offers one accessible **Tap to retry** action there. Retry uses the
existing original-material retry path; it does not add another retry control
below the image. While the image is failed, the preview no longer offers the
separate **Open original** action. The existing delivery lifecycle gates still
remove revoked, expired, mismatched, or otherwise unavailable deliveries before
the preview is rendered. Text-original retry and the canonical original reader
are unchanged.

App commit `7f4afa2d6` implements the retry affordance and focused coverage.
Evidence: **53 tests** passed across the original-material surface, Home
original-delivery screen, Home renderer registry, and adjacent Places expiry
suites; TypeScript, accessibility governance, the 31 polish scenarios, the
Home design-contract check, targeted ESLint, and `git diff --check` passed.
ESLint retains one existing max-lines warning in the Home renderer. The
registered surface-budget check still fails on the untouched Places files
`PlacesWorkspace.tsx` (786/768 lines) and `editorialFeedCard.tsx` (114/87).
The QA doctor could not connect to Metro at the lane's assigned port 61464, so
no native screenshot/capture was produced; no S3-compatible service or
configured media credentials are available in this lane, so real binary-byte
delivery was not verified. This is focused retry interaction evidence, not
proof of live image delivery, visual parity, the full multi-photo composition,
Reply/Ask/share behavior, or release readiness. Keep those broader media and
design gaps open.

## September 21 functional implementation receipt — Life original photo set

The canonical artifact reader previously selected only the first available
owner-authorized image and displayed it in a fixed-height `cover` crop, even
though the existing Life projection can supply several exact media refs. The
reader now presents every available ref in supplied order as an aspect-shaped,
non-cropped photo strip. Selecting a photo opens that exact source in a focused
full-screen viewer; Previous, Next and Close stay inside the same source-bound
record. A failed preview offers **Tap to retry**; a failed full-size view has a
single retry control. The reader uses the existing authenticated media route
with `cachePolicy="none"`, and the route continues to recheck owner/source
authorization. No backend, projection, storage, sharing, export, deletion,
gesture-zoom or audience policy changed.

App commit `ff74def0b` implements the gallery/viewer and updates the
[Canonical Artifact Reader contract](../../travel-app/docs/surfaces/canonical-artifact-reader/contract.md)
with its whole-photo, order, return and authority boundaries. The six focused
`canonicalArtifactCard` tests pass, including multiple items, selected-photo
navigation/return and failed-preview retry. TypeScript, targeted ESLint,
Prettier, accessibility governance, the 31 polish scenarios, the doctrine-only
reader design check, and `git diff --check` pass. The `size-budgets` check still
fails on existing unrelated files (`VenueDetailScreen`, `ImportCaptureScreen`,
`TravelPlanScreen`, `PlaceHomeScreen`, `extendHttpMemoryEndpoints`, `http.ts`,
and `interface.ts`); `home-surface-budgets` still reports the pre-existing
Places workspace/card overages. The reader has no registered native capture;
the gallery doctor could not reach Metro on `:8081`, so no device screenshot
or visual verdict was produced. This also does not prove real original bytes:
the lane has no configured S3-compatible media service/credentials. This closes
the bounded reader implementation only; native device acceptance remains
unverified, as do wider Life media/corpus coverage, live media delivery,
People/Threads breadth, later permitted reuse, and release readiness.

## September 21 functional implementation receipt — Life refind continuation

Life Find no longer silently stops at the newest 100 retained source
descriptors. The existing owner-scoped metadata read now accepts a stable
`created_at`/source-ID keyset position and exposes a versioned opaque cursor;
the native screen offers an explicit **Search older originals** action and
appends results without turning Life into an automatically growing feed.
Every page repeats the existing owner, current-retention, source-status and
custody-receipt checks. The cursor contains ordering data only and cannot grant
access. Search remains literal metadata-only (note, filename, source label and
capture date); it does not search original bodies, unretained sources or the
whole of Life. Exact Source destinations and return context are unchanged.

Backend commit `031b821e` adds the bounded keyset read, cursor validation,
API continuation and regression coverage. App commit `17e9b3f5` wires the
cursor through the typed client, keeps account/query isolation and expiry
filtering across pages, and adds the user-directed continuation state. The Life
root contract records the pagination and authority boundary. Offline backend
tests pass **8 tests** with **3 database-backed cases deselected**; Ruff check
and format checks pass. App TypeScript, targeted ESLint, Prettier and the two
focused Jest suites pass (**13 tests**). The OpenAPI snapshot, app projection
and generated types are synchronized; projection check passes using the
roadmap's established temporary copy of the API policy with only expired review
dates advanced for projection. Canonical policy dates are unchanged. The
required API coverage audit still fails on **55 unrelated expired-policy
reviews**; the newly found existing intake-media consumer is now registered,
so no missing-consumer finding remains.

The Postgres continuation test is present but was not executed because this
lane has no `TEST_DATABASE_URL` with `TEST_DATABASE_DISPOSABLE=1`; the offline
suite deselected it. No full `make verify`, simulator/device acceptance, or
native screenshot was run. This closes the bounded implementation gap in Life
refinding, not a broad Life archive, semantic search, media-delivery, provider
generation, design-parity or release-readiness claim. Next work should return to
the roadmap's value-depth queue rather than expanding this lookup into a new
index or corpus.

### September 21 Home value-depth — fixed cold-start demonstration

Home now has a product-authored, explicitly fictional ticket example for cold
or quiet accounts when no substantive Home unit is available. The sample is
static (no model call and no personal-data inference), distinguishes itself as
a sample, and offers the existing Chat continuation as an optional next step.
It retires after a proof-backed open/action or two distinct proof-backed
presentations. Its exact receipt-history query is bounded and keeps a prior
explicit try visible even if later render telemetry accumulates. No new event
store or preference/knowledge inference was added.

Backend commit `ebaea7c80` and app commit `cb3bae7cb` contain the owner-read,
candidate, lifecycle, native treatment and focused regression coverage. The
focused backend packet passes **77 tests**; Ruff check/format pass. The Home
renderer suite passes **11 tests**; TypeScript and test-contract TypeScript
pass; targeted ESLint has no errors. Its pre-existing renderer max-lines
warning remains, with the changed renderer shortened from 1,173 to 1,145 lines.
The SQL query shape was compiled and checked offline; it was not executed
against PostgreSQL.

This package remains dark unless the existing root-delivery projection and
exposure flags plus a valid presentation secret are configured; no rollout
flag was changed. Native visual acceptance was not run: Metro/API services are
unavailable in this lane and its booted simulator is not assigned to the lane.
The sample's user-visible appearance and live proof-backed retirement therefore
remain unverified. This closes a bounded cold-start content path, not Home
design parity, full-scroll variety, generated supply or release readiness.

### September 21 Life refind continuation — disposable PostgreSQL follow-up

The previously unrun continuation case was executed against a new database
created only inside this lane's assigned Postgres service
(`vesper-functional-implementation-2026-09-20`, host port `61460`). The database
`vesper_functional_life_refind_test_20260921` was absent before creation,
migrated to the current Alembic head, and removed by the test command's cleanup
trap; a follow-up catalog query confirmed it was absent. The exact test
`tests/life/test_original_refind_postgres.py::test_owner_refind_continues_across_keyset_pages_without_duplicates`
passed (**1 passed**). It proves the real SQL keyset read returns all three
fixture sources across two pages without duplicates and ends with no cursor.
The existing offline continuation packet remains **8 passed, 3 deselected**;
this targeted run covers the formerly deselected Postgres case. It does not
certify the full Postgres suite, `make verify`, live original bytes, simulator
acceptance, or broader Life search and release readiness.

### September 21 Life → Places — explicit source association and anchored return

Life's complete Places record now offers **Open related place** beneath a
retained source/original only when its existing represented refs resolve to an
exact Places-owned destination. The source row remains the primary exact
source door. The secondary action carries the current Life lens, group and
entry anchor; Places uses that context for its cold/deep-link Back fallback,
while ordinary stack Back remains unchanged. This is an explicit owner-linked
association—not evidence of attendance, a new visit episode, or an inferred
relationship. No backend, schema, read owner, corpus, or authority changed.

App implementation and contract changes are in the current
`codex/functional-implementation-2026-09-20` candidate. The Life record and
Place-home focused suites pass **32 tests** together; TypeScript and targeted
ESLint pass with no errors (the Place screen retains its existing max-lines
warning), `git diff --check` passes, and all **31** polish scenario IDs
validate. The `life-root` design-reference check is structurally valid with
the existing HTML-reference warning. Native visual acceptance remains
unavailable: the registered `life-root` surface has no capture flows, and no
simulator/device capture was produced. This closes one explicit cross-root
destination/return seam, not broad design parity or later permitted context
reuse. The next queue remains a substantive Home/Places value result or a
distinct Life/social later-use result whose existing payload and authority can
support it.

## September 22 functional implementation receipt — Places Keep persistence flow contract

App commit `e2c0bafb1` strengthens the existing
`.maestro/75-places-real-social-pull.yaml` sequence. After Keep, the flow closes
the exact Place reader, returns to Places, reopens that same venue, and confirms
the same handoff remains kept before it explicitly selects Leave aside. The
runner now rejects non-loopback API origins and arms fixture cleanup before
provisioning, reducing the risk of leaving a rehearsal contribution behind if
setup or the UI flow fails. This changes no recipient-action semantics, API,
owner, policy or storage.

Evidence on the current app revision: the flow contract passes **4/4** tests;
the focused owner-action, handoff-adapter and rebuilt-object-page packet passes
**33 tests**; shell syntax and YAML parsing pass. The extended Keep → close →
Places → reopen → Leave-aside sequence was not natively accepted in this
refresh. Its local API startup stopped because `ANTHROPIC_API_KEY` was
unavailable; no substitute key or QA identity was supplied, and Maestro did
not execute the flow. `npm run maestro:metadata:check` reaches the next,
untouched flow and fails because `.maestro/76-places-public-reading.yaml`
still declares invalid `lane: functional-implementation`; flow 75 itself
passes normalization. This is strengthened acceptance scaffolding, not a new
user-visible capability or visual verdict. Preserve the earlier narrower
native Keep receipt, but require a valid local runtime before claiming the new
reopen-persistence sequence.

## September 22 Home producer/render coverage and returned-value gap

A producer-to-native crosswalk was run against the current backend and app
candidate. Every non-chrome Home kind emitted by the active projection sources
has a native renderer in `HOME_V2_RENDERERS`; `world_read` and `week_shape` are
handled by the Home screen chrome. `now_decision` and `people_waiting_row` are
currently selector/contract kinds rather than active source outputs, and
`horizon_world_fact_row` has no producer. There is therefore no current
producer-backed Home unit waiting for a missing native renderer. Do not spend
the next Home slice on another registry/treatment pass.

The selected Home export in `Downloads/vesper-home` sharpens the actual gap:
its returned posture asks for one useful travel-derived transfer alongside
forward-looking New York value, not a generic trip link or an inventory of
tickets/photos. The current `home_candidates_from_trips` adapter provides the
honest exact Life door (`Returned <date> · refind in Life`) but does not compose
the user's own retained trip evidence into a richer Home result. Other active
Home supply already includes accepted public Place readings, practical Place
facts, Social-owner contributions, Outcomes, and Places continuations; their
presence does not fill this private returned-value gap.

This is a source/use-contract gap, not permission to read the Atlas tables from
Home or to derive a new narrative on every open. The
[consumer-strategy reconciliation](../decisions/2026-09-06-reconcile-consumer-strategy.md#2-optional-conversational-continuity-belongs-in-the-intended-product)
accepts optional continuity as a product direction but leaves retention and
eligible later uses unresolved; the
[Home/Places/returned design matrix](home-places-life-productization-program-2026-09-04.md#44-design-to-runtime-acceptance-matrix)
also rejects a result that merely repeats tickets, routes, or photographs.
Before implementing a private artifact-derived return, define the specific
source set and purpose under the current Life owner, exact lineage and
destination, correction/withdrawal behavior, and truthful sparse/failure
fallback. Prefer a Life-owned bounded read; do not add a Home-side Atlas query,
generator, or new store. If the allowed sources cannot support a genuinely
useful transfer, keep the current exact Life door and the forward-looking
public/Place value rather than fabricate one.

Within the broader Home composition package, the next distinct user-value gap
is still a **returned-value contract and one source-backed composition**, not
a broad semantic expansion: use a confirmed Journey/Outcome and permitted
Sources to connect to a present Place, person, or commitment; keep it
complete-on-view with one exact Life depth door; and prove that correction or
withdrawal cannot leave dependent Home copy stale. The saved-Place reading
above is a completed complementary path from explicit saved intent to accepted
public Place material; it does not satisfy this private, cross-time use case.
Continue the remaining R05 process-interruption and R09 persisted/native
timezone evidence as bounded review closeout, but do not let those verification
cases replace the next user-visible value result.

## September 22 functional implementation receipt — private audio originals in Life

The canonical Intake original reader now offers explicit, owner-authenticated
foreground playback for verified retained MP3, MPEG-4 audio/M4A and WAV
sources. The existing GET media route remains the custody and owner authority;
the shared player verifies native readiness for this GET-only source rather
than introducing a `HEAD` endpoint or expanding API policy. Unsupported audio
containers stay unsupported. Failure produces a retry; leaving the reader,
changing source revision, withdrawal or retention expiry releases the player.
There is no autoplay, upload-policy change, transcript, AI use, export or send
action.

On the app candidate `93a9090de`, the focused Intake screen,
original-boundary and shared audio-hook packet passes **41 tests**, including
the readiness-timeout regression. `npm run typecheck` passes; targeted
ESLint reports no errors and one existing max-lines warning in the Intake
screen. The registered polish scenario IDs validate (**31**); the `life-root`
design-reference check is structurally valid with its existing HTML-reference
warning. Native polish QA found no capture for a flow and therefore did not
produce a visual/device verdict. Actual secured media bytes and codec playback
on iOS/Android remain unverified.

The offline OpenAPI exporter regenerated the stale full snapshot from the
current backend source, but projection stopped at the pre-existing expired
operation-governance queue (**55 expired-policy findings**). No new API
operation or generated mobile wire type is part of this slice. This does not
repair the broader API-governance backlog or constitute a full type-sync gate.

The primary next product build remains the Home design-aligned composition
package in §4: broaden useful value from supported owner material, trace exact
depth/action destinations and return, and assess whole-scroll hierarchy and
polish against the verified design reference. This audio reader is a complete
bounded implementation with native media/device acceptance still open; it does
not replace or serialize that Home work.

## September 22 functional implementation receipt — saved-Place reading in Home

Backend commit `18e1fb377` lets the exact saved-Place continuity door carry a
substantive accepted public reading when one is available. The bounded reader
checks only the four most recent place-like saves, requires exact entity
identity and the existing current/public/source-evidence gates, and reads a
limited number of candidates per entity. The reading shares the generic save's
Home seat, retains its immutable Source and exact Places destination, and
includes the explicit save as a represented owner reference. If no eligible
reading can be read, the ordinary save doorway is preserved. If the same Place
already has current-context public content in the portfolio, the saved-place
copy is suppressed to avoid a second presentation. A saved Place is not
interpreted as a taste profile; no API, schema, migration, generator, or app
screen was added.

Evidence on the isolated candidate: the focused source/portfolio packet passed
**73 tests**; the offline root-projection suite passed **470 tests**; Ruff and
format checks passed. `tests/db/test_place_content.py::test_bounded_entity_listing_returns_latest_reviewed_place_content`
passed **1 test** against a freshly migrated, uniquely named disposable
PostgreSQL database on the lane's isolated Postgres service. The HTTP follow-up
commit `4357d1320` adds a real owner-backed regression: the accepted reading
replaces the generic save in Home, source retraction restores the save doorway,
and unsaving removes both. Together with the two existing public-Place HTTP
readback cases, the integration file passes **3 tests** on a freshly migrated
disposable PostgreSQL database. Both test databases were dropped afterward and
the lane Postgres container stopped. Backend commit hooks also passed. No app
files changed. No live-account read, native Home render, screenshot,
design-reference comparison, or full `make verify` was run. The source/query
and HTTP projection behavior are verified; Home visual acceptance and the
complete end-to-end user experience are not.

This closes one source-backed value seam from explicit saved intent to the
existing Places owner. It does not change the program priority: the broader
Home composition package remains active, with the returned-value contract in
the previous section still the next distinct private, cross-time value gap.
