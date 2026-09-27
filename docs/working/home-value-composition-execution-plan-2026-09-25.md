---
doc_type: working
status: active
owner: codex/home-value-delivery lane
created: 2026-09-25
last_verified: 2026-09-27
expires: 2026-10-25
why_new: Gives one complete Home implementation assignment after separating the program queue from historical receipts; existing design contracts define behavior but not this bounded delivery package.
depends_on:
  - vesper-program-roadmap.md
  - ../systems/contribution-and-consequence.md
  - ../../travel-app/docs/surfaces/home-root/contract.md
---

# H1 — Complete Home value delivery on the recovered system

Status: in progress in the coordinated `codex/home-value-delivery` lane. The
recovered workspace/backend/app baseline is merged as recorded in the
[program roadmap](vesper-program-roadmap.md). Current lane child heads are
backend `a38d5c7f3` and app `91c93cd6e`; the app includes cold Home code
`1408699e1`, its structured native verdict, and the corrected real-API native
rehearsal. The current Home implementation
includes the earlier exact share-time attribution and return, received-original
reader and lifecycle, source-bound Quiet geology comparison, Home Ask-to-Source
result, practical/open-now venue handoff and Home-to-Chat Plan/opening/recovery
doors. Those connected paths are documented in the dated receipts below; most
native evidence is still fixture-backed.

The latest bounded change gives Cold Home a substantive current-Places reading
before any request for contribution. The mock unit preserves source references
and the exact Places dossier destination, and its standalone Chat-seed fixture
remains separate. App commit `1408699e1` records that composition and renderer;
`d1f2111cf` records the reviewed native capture. The cold-specific review passes
its two expected assertions with two P2 findings. It is not a live-owner read.
The prior coordinated `make verify` was on an earlier tuple and has not been
rerun after current app/backend changes. The 12-state Home matrix remains
MIXED; accepted full-scroll design-reference alignment and production/recurring
editorial supply remain open.
September 27 Home polish commits align the four-root Home tab glyph with its
label while preserving the briefcase glyph in legacy Plans, then align region
headings to D-H10 and remove the prohibited gold edge from Home readings. The
same-day native review-first Chat capture now covers all three supported Home
resource doors: Plan, nearby opening and recovery. These are synthetic,
mock-only composer captures; they do not exercise Send or establish full-scroll
visual acceptance.

A later structured native review of the full Home-root matrix is recorded
below. It captures all 12 registered Home/Chat-receiving states on the lane
simulator and returns a **MIXED** product-quality verdict, not H1 completion or
design parity. A targeted follow-up now closes the Planning loose-end
composition mismatch for its registered native posture; bounded copy,
hierarchy and mobile-overlay issues elsewhere in the full matrix remain.

## Outcome and scope

Complete the path from supported input or existing material to a useful result,
Home composition, polished native presentation, meaningful depth/action and
exact return. A richer full scroll is an outcome, not the engineering unit or
a content quota. Home should deliver
value without requiring more capture, reflective homework or an action on every
card. Ordinary present/future life stays visible after a trip; retrospective
material earns space by its substance. This is functional implementation and
native presentation work, not another infrastructure or research-only round.

The backend's existing portfolio/application composer owns supply admission,
posture, semantic selection and degradation; the app owns native treatment,
navigation and restoration. Accepted product and surface contracts own meaning
and authority. Acceptance combines focused contract tests, real owner-path
readback where available, and native comparison to the accepted design reference.

Supply is part of this assignment: distinguish an absent producer, unavailable
prepared result, admission/selection failure and poor native presentation before
choosing a fix. Reuse existing generation/worker infrastructure. Ordinary Home
reads intentionally do not generate on a miss; the controlled worker's explicit
preparation support is not proof of recurring production or authorization to add
ambient triggers. Implement missing connections within accepted owner authority;
escalate a genuinely new trigger/use agreement rather than silently introducing it.

Implement the highest-value gaps in that existing path. Do not assume each item
below is absent just because a September 22 receipt says it was unfinished.

## Read before editing

1. Root and affected child `AGENTS.md`; backend
   [Task Intake](../../travel-agent/docs/operations/Task%20Intake.md) and app
   [Task Intake](../../travel-app/docs/Task%20Intake.md).
2. [Program](vesper-program-roadmap.md), [four-root ownership](../systems/four-root-loop-object-surface.md),
   [Contribution and Consequence](../systems/contribution-and-consequence.md).
3. [Home contract](../../travel-app/docs/surfaces/home-root/contract.md), its
   adopting decisions/kernel, and [surface quality baseline](../../travel-app/docs/surfaces/_quality-baseline.md).
   Read Places/Life owners only for touched destinations or contracts.
4. Relevant accepted design references and the [latest Home handoff](vesper-home-design-review-2026-09-08.md);
   its Live studies are design input, not automatically adopted service policy.
   Verify which board is adopted. The external [design registry](../governance/home-surfaces-design-authority.json)
   has a specific scope and hashes; it is not blanket adoption of every newer
   Downloads project. Record the actual Home comparison reference, its authority
   and availability. Do not silently replace accepted rules with an exploratory
   export or copy the external canonical bundle into the repo.

The current `home-root` entry in `travel-app/scripts/polish-qa/surfaces.mjs`
now registers selected 02/03 first-viewport image references while retaining
`judgeAgainst: 'doctrine'`. The pair manifest marks them `reference`, not full
visual canon: the native Available/Returned fixture captures have different
dates and content, and the comparisons cover only the first 874 logical pixels.
They establish a repeatable visual review input, not full-scroll parity or a
final design verdict. The full accepted Root Boards and surface contract remain
the authorities; a doctrine pass alone still cannot establish visual parity.
This bounded reference work does not require every pending design study to
finish before implementation.

## Starting implementation map

| Responsibility | Existing implementation / focused tests |
| --- | --- |
| Owner portfolio and mapping | `travel-agent/backend/root_projection/v2/home_portfolio.py`, `home_source_adapters.py`; `travel-agent/tests/root_projection/test_home_portfolio.py` |
| Recovered human/world composition | Candidate-only `travel-agent/backend/root_projection/v2/home_human_openings.py` and its portfolio tests; preserve attribution, canonical identity and independent fallback |
| Prepared value and production | `travel-agent/backend/application/root_composition.py`, `travel-agent/backend/root_projection/v2/source_contribution_serving.py`, `source_contribution_canonical_executor.py`, `travel-agent/backend/workers/source_contribution_jobs.py`; inspect preparation, readback, serving and expiry separately |
| Posture and composition | `travel-agent/backend/root_projection/v2/home_composition.py`, shared semantic selection, `travel-agent/backend/application/root_composition.py`; `test_home_composition.py`, `travel-agent/tests/api/test_root_composition_service.py` |
| Native composition/treatment | `travel-app/components/home-root/HomeRootExperience.tsx`, `HomeRootV2Screen.tsx`, `HomeRootV2UnitRenderer.tsx`, `travel-app/utils/homeRootV2RendererRegistry.ts` |
| Action, depth and exact return | Existing root projection navigation/return registry and owner-specific destinations; `travel-app/__tests__/components/home-root/HomeRootExperience.connected.test.tsx` |

Verify filenames and nearest tests at intake. Current main contains a 20-kind
Home renderer registry, bounded owner portfolio and return handling; reuse them.
Numbers are not an instruction to fill every slot or add every design kind.

## Complete assignment

### 1. Select the recovered baseline and trace actual remaining gaps

Start from the merged recovery revisions recorded in the program roadmap. The
current coordinated lane owns this package; do not branch from an older main or
edit the separate recovery/native worktrees. The original recovery PRs are
already merged; this package's new changes must use the normal current checks
and review, with no inherited protection bypass.

Trace three materially different supported situations on that baseline:

| Situation | Required value and continuation |
| --- | --- |
| Ordinary day / available time | Useful understanding or grounded possibility before rich history exists; Home to exact content/Place and back; include authorized post-return continuity without making the trip the whole page |
| An evening involving other people | An existing attributed note, original or supported shared arrangement contributes real value; optional continuation does not create response debt or imply new location-sharing rights |
| Healthy live/travel situation | Useful practical state coexists with independent possibilities; genuine urgency changes emphasis without making all Live situations operational dashboards |

These are system-coverage cases, not three parallel projects or a single-loop
launch gate. Sparse context, urgent compression, source expiry/unavailability
and exact return are relevant regression variants, not a combinatorial test
campaign. A pending study's unsupported service is not part of the required case.

### First trace — code path baseline, 2026-09-25; local API follow-up, 2026-09-26

This is a code-path trace, not production-supply or native-visual acceptance.

| Situation | Owner → Home → continuation | Current finding |
| --- | --- | --- |
| Ordinary day / available time | Experience Graph, saves, receipts, automatic Places context and current public Place Sources, plus an optional current prepared Source result → bounded Home portfolio and shared admission → exact Place/Source/owner door and semantic return token | The read path is implemented and bounded; a Home miss does not invoke a provider or enqueue generation. Deeper Source work requires the existing explicit “Ask Vesper” gesture. An eligible fixed cold/quiet demonstration may coexist with the automatic `places_context` navigation door; other owner content and contextual-Places value still take precedence, and existing retirement, feature, receipt, and signing-secret gates are unchanged. A deeper break was found: the sample had no shared value manifest and was withheld by common admission. Backend revision `bf1e5dadf` now gives this fictional, deterministic sample an explicit low-burden value contract, a bounded `moment.read` dependency (accepting partial availability), and a six-hour expiry. Its unit is covered through candidate construction, shared value admission, and Home selection. The lane-local API returned `home.sample-ticket-demo.v1` as `now_sample_demonstration`; `candidate_manifest_missing` disappeared. This used a synthetic development actor, not a real person or production data. Two bounded `conditions_unavailable` Moment degradations remained, and Home posture was `quiet`. This proves local API composition only—not recurring supply, production coverage, or design parity. |
| Evening with other people | Relationships supplies exact addressed Place notes and individually authorized original deliveries → Home composes a same-Place note with eligible world material, or an attributed multi-note region; original previews keep per-delivery grants → Place or original reader revalidates owner state and returns through Home | Recovered human/Place composition is present. Original media is projected as separate deliveries (maximum two candidates in the current Home adapter); the reader has no reply affordance. No event/photo-set grouping or reply policy is inferred. The newer Home 18 K/L scroll is useful design input for a lead photo and shape-preserving remainder, but cannot create a shared-set identity from individual grants. |
| Healthy live/travel situation | Experience Graph and Plan/proposal owners establish Live; Places current context can supply separately evidenced practical alternatives → Live Home selector keeps independent possibilities eligible; Urgent alone suppresses most support → owner-specific destination/action and exact return | Live is not treated as urgent, and functional selection is covered by the focused backend suite. A real-Postgres native rehearsal now opens a supported `place.open_now` Home possibility, the exact venue, and returns to the same Home unit. Provider-backed freshness, recurring generated supply, and native presentation against the selected design remain separate unproven claims. |

The ordinary Home Source read adapter is present: `compose_home_root_v2` reads
only an already-prepared result, and `read_prepared_source_contribution`
re-discovers the viewer-relative opportunity and reloads the exact current
Source and context refs through the governed material readers. Missing,
changed, expired, wrong-audience or incomplete material makes the prepared
contribution unavailable; an ordinary Home miss does not start generation.
The earlier H1 Source workflow and native continuation evidence used authored
owner/material fixtures. The September 27 receipt below now closes the
one-path integration gap with persisted Intake and editorial owner records:
canonical discovery, owner reads, material loading, explicit workflow,
production readback, and prepared Home all participate. It exercises the
registered structured producer with a deterministic injected caller; the
owner/data and proposal are synthetic, and no external model or paid provider
is used. This proves that the existing governed serving path can deliver one
canonical owner-backed composition through the production proposal/authority/
compiler boundary; it does not prove production content supply, real-user
quality, or recurring preparation.

The first H1 app slice adds the exact owner-read share time to a received
original's Home attribution line (`MAYA · SHARED SAT, 4:25 PM` in the
recipient's local timezone). It labels this as sharing time, not photo-capture
time; it adds no inference, persistence, API field, generation, or reply
obligation. This addresses the selected Home study's lightweight temporal
context while preserving the existing delivery grant and one-delivery rendering
boundary. If the device timezone is invalid, the visible fallback now labels
the time as UTC rather than implying it is local.

The next app slice (`8fc767355`) captures the opened Home unit's vertical
position in the viewport as ephemeral return context. After the destination
revalidates the same Home projection, the original item returns at that same
screen position instead of being pulled up to the top rail. The existing strict
recomposition path remains authoritative if the projection, viewer, audience,
unit or represented source changed while the person was away. This is local
navigation state only: no persistence, API change, new permission, or guarantee
that a changed Home page will jump to stale content.

The `home-root` QA surface now registers selected Home 02/03 first-viewport
references at L0/reference scope while retaining `judgeAgainst: 'doctrine'`;
these are not an accepted full-scroll visual canon. The newer `vesper-home`
Board 18 is an additive extension of the selected 02/03 scrolls; within that
assignment, K/L is the selected photo-integrated full scroll and D/E is a
narrower study. K/L keeps one lead original,
the remainder in a shape-preserving row, the rest of Home's city/future value,
and larger-text treatment. The fixture's album, Reply/Ask path, and actual-photo
assets are not supported by current production owners. Home now retains the
opened unit's viewport position when the same projection is revalidated, but
that behavior has focused projection/UI tests, not native-device observation.
Relationship currently supplies individual grants, not a shared-set identity;
the present Home/original-reader path has no Reply action.
Board 18 informs exploration, but absent the applicable owner contracts and an
accepted full-scroll visual scope, it establishes neither those behaviors nor
native parity. The Home 03
note-first opening is not an adopted placement decision: its screenshot remains
a comparison reference, not an implementation requirement or evidence of a
composition bug.

For each value unit record its actual source/preparation trigger, owner/read,
candidate, region/treatment, received benefit, depth/action and return. Classify
each break as supply, mapping/selection, renderer, destination or design/authority
decision. Keep one compact table here, not another report.

Do not alter the detached native checkout or assume its runtime is free.

### 2. Implement missing value-delivery connections and native treatment

- Use existing owner-backed explanation/reading, grounded possibility,
  practical state, authorized human material and continuity where each exists.
  No fixed content quota or fake richness; show the most useful true material.
- Include the recovered human/world juxtaposition and practical help where
  supported. Do not defer every social or live benefit until an editorial Home
  is finished, or add a separate social feed to demonstrate multiplayer.
- Verify how supported prepared results become available, remain current and
  reach the ordinary Home read. Repair an existing preparation/serving link when
  broken. A manually injected demonstration is not recurring supply; label it
  accurately and keep a specific unsupported trigger as a decision/dependency.
- Correct selection or treatment that needlessly hides useful supporting value.
  Preserve one dominant and the accepted demand budget; urgent compression is
  not the default for every live or quiet situation.
- Make hierarchy, media, spacing, object containment and section language read
  as one coherent Home. Avoid two competing metadata headings, repeated prose
  and generic fallbacks that erase semantic treatment. Follow accepted tokens
  and component conventions rather than inventing a parallel design system.
- Finish depth/action/return for the affected units. A preview must lead to the
  promised content or canonical object and restore the original context; a
  settled state must reflect owner readback rather than local success styling.
- Preserve value from independent sources when one source is unavailable.
  Do not launch expensive generation just to fill a viewport or make every
  Home read depend on model production.

Fix ordinary failures within this assignment, including review findings. A
missing provider blocks its dependent claim, not all renderer/navigation work.
If supported supply cannot sustain a useful composition, repair bounded existing
owner connections in this package. A new producer capability or authority choice
requires an explicit scope decision; finish independent work and report that exact
gap. Do not declare value delivery complete from fixtures or invent filler.

### 3. Verify, review and hand back a coherent package

Use nearest tests during iteration. Cover mixed-source selection, sparse/failed
source behavior, urgent versus ordinary attention, exact depth/return and any
changed action readback. Run app type checking and focused backend/app tests;
sync generated API contracts only if wire behavior changes. Complete relevant
Task Intake checks and the coordinated pre-push gate before publication.

Capture the three supported situations through the actual governed native Home
route, recording the complete product-system rollout posture and data source;
compare against the verified accepted reference for hierarchy, full-scroll
richness, interaction and accessibility. Include at least one exact depth/action
and return per situation. Identify frontend mocks, owner-real readback and
provider-backed execution separately. A missing device/reference may leave
implementation ready but visual acceptance open; it cannot be called complete
design parity. No release flag change or provider spending is implied.

Obtain code review at the coherent package boundary and correct actionable
findings. Report changed behavior, exact revisions, checks with their boundaries,
unresolved design/supply items and branch disposition. Do not repeatedly seek
founder approval for ordinary repairs already within scope.

## Authority and parallelism

One primary owner holds the package. Optional delegated work, when authorized:
backend selection/mapping, disjoint native treatment, and independent review.
The primary owner retains wire contracts and shared navigation; workers do not
edit those concurrently. Delegate an outcome through implementation and tests,
not a chain of micro-diagnoses. Do useful independent work while another worker
is running. Use the current requested model settings; this document imposes no
new permanent model policy or worker count.

Escalate only a material product/permission/architecture choice, conflicting
write ownership or unavoidable external dependency. No new semantic kind,
private-to-shared conversion, inferred authored photo set, durable watch,
booking service, Chat/Life redesign or generator/store is authorized just to
make Home fuller. Narrow destination fixes under existing contracts are in scope.

## Completion and latest receipt

Exit requires useful connected implementation for the three supported situations,
current owner-backed delivery evidence for the affected paths, regression coverage,
reviewed native presentation and honest supply/degradation. Repeated-use supply
and visual parity are separate claims, supported only by their actual evidence.
Remaining unsupported design concepts are explicitly
separated from defects in the delivered scope. A package is not finished merely
because its branch exists or its mocked screenshot is attractive.

Receipt log (chronological; most recent entry is at the end): **in progress**.
On the merged recovery baseline, the focused backend Home portfolio and
selection suite passed (86 tests). The first H1 app
slice is committed in app revision `66e2c3c`; its owner-read regression
coverage is committed in `122f4d2`. The following focused command passed
(3 suites, 25 tests); `npm run typecheck` passed as well:

```sh
npm test -- --runInBand --runTestsByPath __tests__/screens/original-delivery.test.tsx __tests__/components/ReceivedOriginalSurface.test.tsx __tests__/utils/originalDeliveryTime.test.ts
```

The renderer-level case verifies Home reads the
sender and shared-at time from the current `useOriginalDelivery` result; this
is mocked owner-read evidence, not a live backend readback. `python3
scripts/check_docs.py --all` passed. After installing the lane's ignored app
dependencies, the Home polish doctor passed against the lane Metro and its
assigned iPhone 16 Pro simulator. Run `20260926T143155Z-home-root` captured
all seven registered fixture postures (Available, Planning, Live, Returned,
Quiet, Cold, Urgent); their scripted visibility/assertion flows completed.
The screens were reviewed against the active Home contract, but the manifest
still has `designRefs: []`, so this is not Claude-design parity or final
product-quality acceptance. `npm run qa:design:check -- home-root` confirms
that Home remains doctrine-only, and `HOME_SURFACES_CANON_DIR` is unset in this
shell. These fixture postures do not contain the received original whose new
share-time line was changed; that behavior has focused
formatter/component/renderer coverage but no dedicated native capture or live
owner-data readback. The controlled real-owner original/full-scroll rehearsal
was not run: `QA_ALLOW_DATABASE`, `QA_USER_ID`, and `DATABASE_URL` were unset.
I installed the lane's ignored Python 3.13 dependencies and brought up its
isolated Postgres/Qdrant services; migrations completed, but API startup failed
because `ANTHROPIC_API_KEY` is required by the current startup contract. The
lane containers were stopped without deleting their named volumes. No QA
account or delivery fixture was created in that attempt. This is a dated
hold, not the current state; it is superseded by the owner-backed rehearsal
below.

The subsequent exact-return slice is committed in app revision `8fc767355`.
This focused command passed (4 suites, 53 tests):

```sh
npm test -- --runInBand --runTestsByPath __tests__/utils/rootProjectionReturnRegistry.test.ts __tests__/components/HomeRootV2Screen.smoke.test.tsx __tests__/components/home-root/HomeRootExperience.test.tsx __tests__/components/home-root/HomeRootExperience.connected.test.tsx
```

`npm run typecheck` and the following targeted ESLint command passed:

```sh
npx eslint components/home-root/HomeRootV2Screen.tsx components/home-root/HomeRootExperience.tsx utils/rootProjectionReturnRegistry.ts __tests__/utils/rootProjectionReturnRegistry.test.ts __tests__/components/HomeRootV2Screen.smoke.test.tsx __tests__/components/home-root/HomeRootExperience.test.tsx
```

The interaction test captures a unit at viewport y=160; the return registry
test verifies that anchor survives an exact projection return. This remains
mocked projection/navigation evidence, not device-level scroll observation or
live owner-data readback. The real-owner API rehearsal was still blocked by
the then-current provider-key startup contract; no key or substitute was
supplied at that point. Backend revision `6c792ed8b` later made explicit
`AI_MODE=off` startup valid, and the lane's local real-Postgres rehearsal below
ran without a provider call.

The latest native refinements are committed in app revisions `1b23ed891` and
`a963fa0b9`. Non-dominant Home editorial readings no longer repeat the region's
meaning with an extra “A closer reading” kicker; the kicker remains when the
reading is promoted to the standalone dominant. For outcome continuity, Home
no longer shows the generic “Canonical outcome” basis caption; it keeps the
record label, substantive value and Life door. Other direct-state bases remain
visible. Focused checks passed: 2 renderer/screen suites (36 tests), TypeScript,
and targeted ESLint (with the existing file-length warning). The Home scenario
registry check passed; the Returned posture capture at
`travel-app/.maestro/runs/20260926T153747Z-home-root` records the combined
screen at app revision `a963fa0b9`. It is fixture-backed (`dataContext: null`)
with no registered design refs: evidence of this native treatment only, not
real-owner supply, reference comparison, or Claude design parity.

The combined `make verify` gate remains unrun. Only the isolated lane database
schema was migrated; no product-data fixture, production data, release flag
change or publication was involved. The Expo
rehearsal flags were local to the lane; the native build required disabling the
local Sentry source-map upload because no Sentry organization was configured.
`npm ci` reported 20 audit vulnerabilities (1 low, 19 moderate); no dependency
remediation was attempted. This is implementation progress only, not H1
completion, recurring-supply evidence, accepted-reference parity or release
readiness. Preserve older detailed evidence in Git/history rather than
accumulating competing “latest” overrides.

### September 26 — Received-original path and Home scenario

App revision `2840a24204af777ebd0d2396a22ce973c365d288` adds one
opt-in `home-original-recipient` fixture to the existing Returned posture. It
contributes exactly one private, individually addressed original; it does not
invent a shared album or reply action. Exact-text reads now pass through the
original-delivery API owner for both HTTP and mock transports. The HTTP owner
preserves the prior bearer-token read, one retry after `401`, cancellation and
no-store behavior. The mock content is returned only to its recipient persona,
and mock metadata reads are constrained to sender or recipient. No backend
wire contract, generated types, release flag or production data changed.

The focused command below passed: 4 suites, 19 tests. `npm run typecheck` also
passed. Targeted ESLint had no errors; it reported two pre-existing
`array-type` warnings in `constants/personas/index.ts:352-353`. The scenario-ID
and surface-index checks passed. `npm run qa:design:check -- home-root` still
reports that Home is doctrine-only with no registered reference manifest.

```sh
npm test -- --runInBand --runTestsByPath \
  __tests__/utils/api/homeOriginalDelivery.mock.test.ts \
  __tests__/utils/homeRootV2PostureFixtures.test.ts \
  __tests__/data/originalDeliveries.test.tsx \
  __tests__/components/home-root/HomeRootExperience.connected.test.tsx
```

The new Maestro path is
`.maestro/polish/home-root-social-original.yaml`. Its first native attempt on
the lane-assigned iPhone 16 Pro reached the Home card, but failed the current-
owner attribution assertion: the pre-existing Metro bundle had the internal
`RELATIONSHIP_UUID_HANDOFFS_ENABLED` flag off, so it correctly remained in the
loading state. That Metro process was not restarted or changed. To finish the
device check, a separate temporary internal-only Metro server was started on
port `53178` with mock API, internal build, root-shell, projection, Places/Life
renderer and relationship-handoff flags enabled. The same Maestro flow then
passed on the lane-assigned iPhone 16 Pro
(`AF31B886-E837-4962-834A-5CBAD5C306DB`), including sender/time attribution,
caption, exact note text, opening the original, returning to Home and verifying
the card remained. Its debug output is under
`/tmp/vesper-home-social-original-internal-a11y/.maestro/tests/2026-09-26_121259/`;
a Home screenshot is at `/tmp/vesper-home-social-original-passed.png`. The
temporary server was stopped after the capture; this was an internal QA run,
not a release-flag change.

The first passing capture exposed a real accessibility defect: the note's
explicit accessibility label replaced its actual text, hiding it from VoiceOver
and the native test hierarchy. App revision
`7e7108d9e146af8b572d182696690dccb2775e02` removes that override and makes the
note selectable. The focused follow-up passed 5 suites / 39 tests, typecheck,
and targeted ESLint; the recipient Maestro flow passed again, and the ordinary
`home-root-returned` flow passed on the same simulator after restoring the
default persona.

```sh
npm test -- --runInBand --runTestsByPath \
  __tests__/components/ReceivedOriginalSurface.test.tsx \
  __tests__/screens/original-delivery.test.tsx \
  __tests__/data/originalDeliveries.test.tsx \
  __tests__/utils/api/homeOriginalDelivery.mock.test.ts \
  __tests__/utils/homeRootV2PostureFixtures.test.ts
npm run typecheck
npx eslint components/inbound/OriginalMaterialView.tsx \
  __tests__/components/ReceivedOriginalSurface.test.tsx
maestro test --udid AF31B886-E837-4962-834A-5CBAD5C306DB \
  --debug-output /tmp/vesper-home-social-original-internal-a11y \
  .maestro/polish/home-root-social-original.yaml
maestro test --udid AF31B886-E837-4962-834A-5CBAD5C306DB \
  --debug-output /tmp/vesper-home-social-original-default-restore \
  .maestro/polish/home-root-returned.yaml
```

That earlier capture was mock interaction/presentation evidence only. Its
real-owner hold was superseded by the controlled local rehearsal below. The
accepted Home design reference remains unresolved; `make verify` remains
unrun. H1 is not complete, and the mock capture does not establish recurring
social supply, photo presentation, production data, or design parity.

#### September 26 — Offline owner-backed original → Home return

Backend revision `6c792ed8b` now accepts explicitly configured `AI_MODE=off`
without an Anthropic key; `live` and `cheap` modes still require one. This
makes the declared offline rehearsal mode executable without weakening
provider-backed startup. The local rehearsal also enabled the existing
relationship-handoff route gate; no release flag, API schema or generated app
type changed.

The first local owner-backed native run reached the exact original reader but
failed on return: Home issued two root reads together (ordinary focus refresh
and semantic-return refresh), and competing compositions left the surface
partial. Home now coalesces those triggers onto one in-flight owner read. The
focused regression test verifies that focus and semantic restoration share the
same revalidation path. This fix and the strengthened runner are in app revision
`04d4ed85c`.

The final local owner-backed run passed on the lane-assigned iPhone 16 Pro
simulator (`AF31B886-E837-4962-834A-5CBAD5C306DB`): the app rendered the
synthetic recipient's original from the local backend, opened its exact text,
returned to Home with the same original visible, and the backend owner read
confirmed the delivery remained active until fixture cleanup. The runner then
removed the disposable sender/source/delivery and verified that neither the
recipient owner list nor Home projection retained it. The recipient was the
existing synthetic QA account Mara; no founder or production data was used.
`AI_MODE=off` and `WEB_SEARCH_MODE=off` meant there were no provider calls.

```sh
# From workspace root. Backend runtime contract; live and cheap remain strict.
(cd travel-agent && .venv/bin/python -m pytest --run-quarantined \
  tests/api/test_error_handlers.py::TestStartupValidation::test_fails_without_anthropic_key \
  tests/api/test_error_handlers.py::TestStartupValidation::test_passes_without_anthropic_key_when_ai_is_explicitly_off \
  tests/api/test_error_handlers.py::TestStartupValidation::test_still_fails_without_anthropic_key_when_ai_is_live -q)
(cd travel-agent && .venv/bin/ruff check backend/api/lifecycle.py tests/api/test_error_handlers.py)

# App return behavior, native runner contract, and local owner-backed device path.
(cd travel-app && npm test -- --runInBand --runTestsByPath \
  __tests__/components/home-root/HomeRootExperience.test.tsx \
  __tests__/components/home-root/HomeRootExperience.connected.test.tsx \
  __tests__/utils/rootProjectionReturnRegistry.test.ts)
(cd travel-app && npm run typecheck)
(cd travel-app && node --test scripts/maestro/home-original-delivery.test.mjs)
(cd travel-app && bash -n scripts/maestro/run-home-original-delivery.sh)
(cd travel-app && QA_ALLOW_DATABASE=vesper \
  QA_USER_ID=31ccbc41-123c-4fb3-b433-7be7f10f9bb2 \
  DATABASE_URL=postgresql://vesper:localdev@localhost:53173/vesper \
  EXPO_PUBLIC_API_URL=http://127.0.0.1:53176 \
  VESPER_MAESTRO_UDID=AF31B886-E837-4962-834A-5CBAD5C306DB \
  scripts/maestro/run-home-original-delivery.sh)
```

Backend focused tests passed (3), Ruff passed; app focused tests passed (3
suites, 31 tests), typecheck passed, runner contract tests passed (3), and the
native path passed with exact fixture cleanup. The combined `make verify` gate
is still unrun. This is local owner-backed integration evidence for one
recipient path—not recurring social supply, multi-recipient behavior, photo
presentation, production acceptance, or Home-design parity. Home has no
registered design refs, so no Claude-design parity claim is made.

#### September 26 — Original-reader and owner-poll lifecycle

The first post-return runtime observation showed periodic original-owner reads
continuing after the synthetic delivery was removed. Investigation separated
two callers that share the same owner endpoint: the depth reader, and Home's
still-rendered original card. The reader now supplies its 30-second revalidation
only while its route is focused. The shared material hook now cancels
revalidation when it no longer has a confirmed owner-backed delivery to protect;
this prevents a stale Home projection from retrying a missing/revoked owner
record indefinitely. The Home card retains its normal grant/expiry checks while
the delivery is confirmed.

The final native local-owner rehearsal passed again on the assigned iPhone 16
Pro simulator. After cleanup, Home performed one expected owner read, received
`404` at `2026-09-26T17:20:56Z`, then emitted no further original-delivery reads
in the following 35 seconds. This is distinct from the earlier repeated
30-second reads before the shared-hook guard. Focused screen/data tests passed
(2 suites, 28 tests), app typecheck and targeted ESLint passed, and the
owner-backed fixture was removed and absent from both the recipient owner list
and Home projection.

```sh
(cd travel-app && npm test -- --runInBand --runTestsByPath \
  __tests__/screens/original-delivery.test.tsx \
  __tests__/data/originalDeliveries.test.tsx)
(cd travel-app && npm run typecheck)
(cd travel-app && npx eslint 'app/original-delivery/[deliveryId].tsx' \
  data/originalDeliveries.ts \
  __tests__/screens/original-delivery.test.tsx \
  __tests__/data/originalDeliveries.test.tsx)
(cd travel-app && QA_ALLOW_DATABASE=vesper \
  QA_USER_ID=31ccbc41-123c-4fb3-b433-7be7f10f9bb2 \
  DATABASE_URL=postgresql://vesper:localdev@localhost:53173/vesper \
  EXPO_PUBLIC_API_URL=http://127.0.0.1:53176 \
  VESPER_MAESTRO_UDID=AF31B886-E837-4962-834A-5CBAD5C306DB \
  scripts/maestro/run-home-original-delivery.sh)
```

This closes the observed polling regression for the reader and its shared
material lifecycle. It is local synthetic-owner evidence only; it does not
change the separate Home supply, recurrence, visual-reference, or production
acceptance gaps. `make verify` remains unrun.

#### September 26 — Native received-photo presentation

App revision `957fddde2` adds a QA-only Home scenario for one individually
addressed photo original, backed by the repository's existing local dogfood
image. The registered native flow captures Home, opens that exact original,
and returns to the same Home context. The capture exposed and corrected a
presentation defect: previews had a fixed-height image frame that left blank
side gutters around landscape media. Image layout now uses the loaded image's
intrinsic aspect ratio; tall images are height-capped without cropping. The
fresh iPhone 16 Pro capture shows the landscape photo filling the Home content
width, the reader preserving its proportions, and the original remaining
visible after return.

This is presentation and navigation evidence for a mock persona using a local
dogfood-media route. The mock has no private owner token, so its native flow
uses the visible “Open original” action; it does not exercise authorized image
tap-through. This does not prove owner-backed S3/private-media reads, recurring
photo supply, album/set semantics, replies, production data, or Claude-design
parity. Home now has an L0 first-viewport reference manifest, not an accepted
complete visual reference; `make verify` remains unrun.

```sh
(cd travel-app && npm test -- --runInBand --runTestsByPath \
  __tests__/components/ReceivedOriginalSurface.test.tsx \
  __tests__/screens/original-delivery.test.tsx \
  __tests__/utils/api/homeOriginalDelivery.mock.test.ts \
  __tests__/conventions/cardContract.test.ts \
  __tests__/utils/homeRootV2PostureFixtures.test.ts)
(cd travel-app && npm run typecheck)
(cd travel-app && npx eslint \
  constants/personas/index.ts constants/mocks/rootProjectionV2.ts \
  utils/api/mock/originalDeliveries.ts scripts/polish-qa/surfaces.mjs \
  scripts/maestro/home-original-delivery-photo.test.mjs \
  __tests__/utils/api/homeOriginalDelivery.mock.test.ts \
  __tests__/utils/homeRootV2PostureFixtures.test.ts \
  __tests__/conventions/cardContract.test.ts \
  components/inbound/OriginalMaterialView.tsx \
  __tests__/components/ReceivedOriginalSurface.test.tsx)
(cd travel-app && node scripts/maestro/normalize-metadata.mjs)
(cd travel-app && node scripts/maestro/home-original-delivery-photo.test.mjs)
(cd travel-app && node scripts/polish-qa/validate-scenario-ids.mjs)
(cd travel-app && VESPER_METRO_URL=http://127.0.0.1:53177 \
  node scripts/polish-qa/run-polish-qa.mjs home-root \
  --flow=polish/home-root-social-photo)
```

The focused tests passed (5 suites, 155 tests), typecheck passed, Maestro
metadata validated (386 flows), the photo-flow contract test passed, and
scenario validation passed (`registered=31`). Targeted ESLint reported zero
errors and three warnings in the touched persona/card-contract files. The
native flow completed with all three captures (`home-root-social-photo`, its
reader, and its return) on the lane-assigned iPhone 16 Pro. `git diff --check`
passed before commit. These checks do not replace the full app suite or the
coordinated `make verify` gate.

#### September 26 — Cold-start sample admitted by shared composition

Backend revision `bf1e5dadf` fixes the second half of the cold-sample delivery
path. The already-approved fictional ticket demonstration was constructed by
the Home portfolio, but the common composer withheld it because it lacked a
`ValueCandidate` manifest. It now has a deterministic, low-burden value
contract, a bounded `moment.read` requirement that permits known partial
availability, and a six-hour expiry. The content remains explicitly
product-authored fiction; the Moment read establishes a current Home opening,
not ownership of the sample ticket or route. No API schema, producer,
generation trigger, or user-data write was added.

The regression now carries the candidate through manifest construction, shared
value admission, and cold Home selection. Backend portfolio tests passed (83),
and root-composition/value-composition tests passed (44). Ruff check, Ruff
format check, and `git diff --check` passed. Commit hooks also passed.

An HTTP `GET` against the isolated lane API returned 200 for
`/api/root-projections/v2/home?timezone=America%2FNew_York`. The sanitized
response included `home.sample-ticket-demo.v1` (`now_sample_demonstration`)
in `now`, alongside the `places-context.current` aperture in `horizons`; the
`candidate_manifest_missing` degradation was gone. Two bounded
`conditions_unavailable` Moment degradations remained. The response posture was
`quiet`. The local runtime used its synthetic development actor, not a real
person or production account; this proves HTTP composition wiring, not
real-user value, recurring supply, or visual parity. No full `make verify` was
run as part of this slice.

#### September 26 — Home 02/03 first-viewport reference comparison

The selected ordinary-day Home 02 and post-return Home 03 phone canvases from
the accepted 2026-09-09 direction are now exported into the app repository as
top-viewport references. The existing exporter gained an exact-match
Playwright-locator mode with a required single output name, static-page guard,
unique-match assertion, optional bounded viewport crop, and capture provenance.
The source Downloads project was not edited. The design crops are 393px wide,
874 logical pixels tall; their proportions are close to the iPhone 16 Pro
native viewport captures and make above-the-fold hierarchy reviewable.

The `home-root` comparison manifest pairs Home 02 with the native Available
fixture and Home 03 with the native Returned fixture. Both are registered as
`reference`/L0: native captures include system chrome, and the fixture dates,
postures, and content intentionally do not match the authored canvases. Review
is limited to hierarchy, visual treatment, and first-viewport density; neither
pair proves full-scroll parity, same-data state parity, real-owner value, or
product acceptance. The complete scroll remains a separate acceptance gap.
The surface registry now includes the two images in its visual review context,
while `judgeAgainst: 'doctrine'` remains unchanged until the full accepted
reference and its scope can be represented honestly.

Fresh native captures at app revision `957fddde2` now replace the historical
screenshots for this comparison: Available passed in
`20260926T185857Z-home-root`; Returned passed in
`20260926T185943Z-home-root` (including its close capture). Both ran on the
lane iPhone 16 Pro with mock data and no backend. The broad warm surface, serif
lead, section-label treatment, and spacing are directionally consistent. Home
02's timed `Today, in order` composition is not yet exercised by a matching
native state; the current Available fixture is a different Saturday
possibility, so this comparison cannot classify that difference as a defect.

The social-original native flow required both the app and API relationship
handoff flags. The two first attempts (`20260926T190143Z-home-root` and
`20260926T190801Z-home-root`) lacked the app flag and are setup failures, not
product evidence. With the flag enabled, the flow reached the recipient unit
and exposed two capture issues: `20260926T191126Z-home-root` asserted preview
copy that was below the opening viewport, and `20260926T191912Z-home-root`
passed the exact reader and return but its Home screenshot still showed the
opening. The flow now explicitly scrolls to show the received unit before
capturing it. At app revision `957fddde2`,
`20260926T192044Z-home-root` passed 1/1 with 2/2 extra captures: share-time
attribution and caption on Home, exact fixture text in the reader, and return
to the same Home context. Its Home screenshot shows the received note after
the week strip and Worth Knowing, followed by rest-close. This is mock fixture
evidence on the lane iPhone 16 Pro, with no backend or production data.

That proves the local recipient path, not Home 03 first-viewport parity. The
accepted product decision does not adopt the note-first opening as Home's
placement, so its difference from the current feed is not an implementation
defect absent a new decision. Keep the registered pair marked `reference`; do
not infer matching content, placement, real-owner value, or full-scroll
acceptance from it. Home 02's timed `Today, in order` composition remains
outside current owner-backed data: `RootCompositionSequenceStep` has no time
field or accepted producer contract for this timeline. Treat that as a
capability/contract dependency, not a renderer bug; do not invent times or
seed owner facts to match the canvas. Continue H1 on existing owner-backed
value and its real presentation/return gaps while those dependencies remain
unresolved.

#### September 26 — Home alternatives hierarchy and cold-start capture

App revision `6489ef4c4` removes the generic “A few ways in” kicker directly
above a supplied alternative's semantic title. The component regression test
asserts that the meaningful title remains and the duplicate generic label is
absent. This is a narrow hierarchy correction; the test fixture covers the
affected alternatives renderer.

The first cold-start polish attempt exposed a test-harness ordering issue: the
readiness flow launched the development client before connecting it to the
lane's Metro server. The simulator returned to SpringBoard and emitted a JSI
native crash during that disconnected startup. The readiness runner now passes
the encoded lane Metro URL and opens the Expo development-client link as the
first app command. With this ordering, the cold-start readiness assertion and
registered Home Available flow passed together: run
`20260926T195030Z-home-root`, 1/1 capture, on the lane iPhone 16 Pro. The
capture is fixture-backed. It does not include the alternatives unit changed
above, so it verifies cold-start and overall Home flow only; the renderer change
is supported by the component test, not a matching native alternatives
screenshot.

Checks for this slice: the Home smoke suite passed (22 tests); the readiness
contract tests passed (4); TypeScript passed; ESLint reported no errors and the
existing `HomeRootV2UnitRenderer.tsx` max-lines warning; `qa:polish:scenarios`
passed with 31 registered flows; `qa:design:check -- home-root` passed with one
manifest and two reference pairs. `git diff --check` passed. The full app suite,
`make verify`, accepted visual parity, real-owner readback and release readiness
remain unverified.

#### September 26 — Quiet Home: a sourced connection with actual explanatory value

App commit `42cba2d30` replaces the mock Quiet-state cliff card's relational
placeholder (“Sorrento's cliff has a New York counterpoint”) with a concrete
geological contrast. A follow-up copy correction in `7d7d5b762` makes the title
“The Palisades began as magma between older rock layers,” avoiding the
misleading implication that the cliffs themselves cooled underground. The comparison
explains that a CNR study examined a tuff cliff at one Sorrento Peninsula site,
while the Palisades expose a diabase sill formed by magma intruding between
older layers and cooling below the surface. The card states the limit of the
Sorrento evidence explicitly: one study site does not characterize every cliff
on the peninsula. Sources consulted: [CNR institutional study](https://iris.cnr.it/handle/20.500.14243/330594)
and [Palisades Interstate Park geology](https://njpalisades.org/nature/).

The fixture now carries comparison anatomy and a structured composition brief
with source-bound claims, an explicit uncertainty note, and a visible
source-owner trust line. It removes the second Quiet card that merely repeated
that Vesper had connected the two cliffs. Quiet now has two units—the
substantive geology composition and the existing recorded trip outcome—with no
input actions. This is a presentation/content fixture change; no API contract,
backend producer, or live content-generation behavior changed.

Verification on app commit `7d7d5b762`: the focused Home/projection suites
passed (3 suites, 38 tests); `npm run typecheck` passed; targeted ESLint passed;
`node scripts/polish-qa/validate-scenario-ids.mjs` passed (31 registered
flows); and `git diff --check` passed. The workspace `python3
scripts/check_docs.py --all` check passed before this receipt was added.

Native boundary: the Quiet flow passed 1/1 on the lane iPhone 16 Pro in run
`20260926T202128Z-home-root`; screenshot:
`travel-app/.maestro/runs/20260926T202128Z-home-root/screenshots/full/home-root-quiet.png`.
That capture was taken from the functional working-tree diff immediately
before it was committed as `42cba2d30`; its generated manifest therefore
records the preceding HEAD `6489ef4c4`, not the later commit. The only edit
between capture and that commit restored unrelated test formatting to its
original form. It shows the comparison body but is scrolled below the title, so
it does not visually prove the final headline in `7d7d5b762`. Do not treat the
manifest SHA as committed-revision evidence. An earlier
capture attempt (`20260926T201821Z-home-root`) was setup-only failure: Metro
was bound to localhost/IPv6 while the simulator tried `127.0.0.1`; restarting
Metro on the lane-reachable interface produced the passing capture. A later
post-commit repeat (`20260926T202325Z-home-root`) stalled in Maestro's iOS
XCTest driver during mock-readiness, before the product flow, and was
interrupted; it is not product-failure evidence and predates the headline
refinement.

#### September 26 — Post-commit Quiet Home native acceptance

The headline refinement now has native evidence on the committed app revision
`7d7d5b762`. Run `20260926T204547Z-home-root` passed the registered
`polish/home-root-quiet` flow 1/1 on the lane iPhone 16 Pro. The flow reached
the Home v2 screen, asserted the exact revised Palisades headline, confirmed
the Quiet state has no dominant demand card, and reached the honest
`NOTHING ELSE WAITS` close. Its final screenshot is
`travel-app/.maestro/runs/20260926T204547Z-home-root/screenshots/full/home-root-quiet.png`;
it shows the lower page at the close, while the preceding headline assertion
proves the copy was present before the flow scrolled down. This is fixture
rendering/interaction evidence, not production sourcing or recurring supply.

The first post-commit attempt (`20260926T204154Z-home-root`) opened the legacy
Plans screen because Metro was started without the internal four-root rollout
flags. It failed the expected `home-v2-screen` assertion before product
content was exercised. Restarting the lane Metro with the five local rehearsal
flags enabled and pointing Maestro to `http://192.168.86.189:53177` corrected
the setup; no app code or committed rollout default changed. The lane-specific
Home design check passed with two reference pairs, but the external canonical
bundle was not verified and the quiet screenshot does not include the
reference-matched first viewport.

Focused continuation checks on `7d7d5b762` passed 5 suites / 49 tests across
Home source inspection, source-result presentation, Home routing, return
tracking, and strict return resolution; `npm run typecheck` passed. These
checks establish the client-side contract, not a real owner-backed Source
contribution workflow. At that point in the September 26 sequence, no
disposable database had yet been configured; a later real-Postgres Home
rehearsal is recorded below.

This remains fixture-only evidence: it proves the composition can be rendered
and understood in the native Home surface, not that live owner data or a
production generation service will discover, source, refresh, or reliably
produce this kind of connection. At this point in the sequence it did not prove
the deeper Source contribution workflow or recurring content supply; the
separate Postgres workflow receipt below now establishes a bounded server-side
workflow result, not the native Home interaction or production supply.

#### September 26 — Real owner-backed Home full-scroll composition

App revision `48ee7ba88` makes the full-scroll runner read the exact simulator
assigned in the workspace `.workspace-lane.json`, verify it is booted before
any fixture write, and pass its UDID to Maestro. The previous runner could
silently pick among multiple booted simulators. The accompanying Home contract
records this boundary.

The guarded real-Postgres run `h1-home-scroll-20260926T205800Z` passed 1/1 on
the assigned iPhone 16 Pro (`AF31B886-E837-4962-834A-5CBAD5C306DB`) against
backend `bf1e5dadf` and Home implementation `7d7d5b762` (the later app commit
contains only the runner guard and its contract note). In one ordinary
Home-v2 scroll, the canonical owner read rendered two public Place
interpretations, a Place-addressed note from a friend, and an individually
authorized original. The flow asserted each exact unit and authored text; the
runner then confirmed that the fixture units no longer appeared in Home after
its cleanup trap completed. The local run used a newly created synthetic QA
account, a lane-only PostgreSQL database, `AI_MODE=off`, and no provider calls.
The screenshot is locally available at `travel-app/home-full-scroll.png`.

This closes the specific gap for a bounded synthetic social + editorial +
original-material composition through actual local owner reads, native
presentation, and fixture withdrawal. It does not establish production-data
quality, recurring/AI-generated supply, real photo rendering, design-reference
parity, or global four-root readiness. At this point the native Home
Ask-to-Source-result interaction was still open; it is covered by the later
native workflow receipt below.
The Home 02/03 references remain first-viewport aids; the external canonical
bundle was not verified. The runner does not open every destination in this
full-scroll flow; use the separate original-reader return receipt for that
behavior. `make verify` and release readiness remain unverified.

#### September 26 — Explicit Source workflow on disposable Postgres

The existing `tests/api/test_source_request_delivery_postgres.py` acceptance
was executed against this lane's isolated PostgreSQL service after upgrading
that database to the backend's current Alembic head. All three tests passed.
The main case submits an explicit request over HTTP, confirms idempotent replay,
observes the pending exact-result response, runs the canonical worker fence,
then reads the same persisted production through the exact-result endpoint and
the prepared-value reader for both Home and Places. It also checks reuse rather
than a second provider call, truthful unknown cost when no provider ledger row
exists, and owner revocation making the exact result unavailable. The adjacent
cases verify that a completed result can reach Places runtime and that a late
worker cannot publish after cancellation.

This is real workflow/storage/readback execution on disposable Postgres, but
the Source inventory, materials, owner-read portfolio, and producer output are
authored fixtures. This backend test alone does not exercise the native “Why
this?” → “Ask Vesper” → result-screen tap-through, read canonical user-owned
Source records, or make a paid model call. The bounded native flow is now
covered separately below; neither receipt establishes production-source
quality or recurring supply.

```sh
# Lane-only service and migration; use the exact assignments in
# .workspace-lane.json. Credentials are intentionally omitted here.
docker compose up -d --wait postgres
DATABASE_URL=<lane-local-postgres-url> PYTHONPATH=. \
  .venv/bin/python -m alembic upgrade head

# Executed with TEST_DATABASE_URL and DATABASE_URL both set to the isolated
# loopback database, plus TEST_DATABASE_DISPOSABLE=1.
AI_MODE=off WEB_SEARCH_MODE=off DISABLE_LLM_BACKGROUND_LOOPS=true \
  PYTHONPATH=. .venv/bin/python -m pytest \
  tests/api/test_source_request_delivery_postgres.py -q -x
```

Result: 3 passed on backend `bf1e5dadf`. Supporting same-lane evidence:
97 focused backend Source/workflow/API tests passed; 4 focused app suites / 36
tests passed across explicit request, Home route handoff, exact-result states,
and result destinations. These test boundaries do not replace native device
acceptance, `make verify`, production-source evaluation, or release readiness.

#### September 26 — Native Home Source request → exact result → return

App revision `aa3e235d6` completes the native continuation from a prepared
Home Source card: “Why this?” → “Ask Vesper” → the exact pending result → the
same Home contribution after the provider-free worker has produced or reused a
persisted result. The Home request now carries the visible contribution's full
governed `source_refs` set rather than only its private attachment. The runner
prepares the owner-backed fixture, submits the initial controlled production,
lets the registered Home action create its own workflow, runs the canonical
worker fence, verifies exact-result readback, and cleans up both workflows and
the fixture production.

`travel-app/scripts/maestro/run-home-source-result-real.sh` passed on the
assigned iPhone 16 Pro against the lane API and disposable Postgres database.
The synthetic QA owner and authored fixture are not production-user or
production-supply evidence; `AI_MODE=off` means no paid model call. The separate
backend workflow receipt above proves the API/storage boundary, while the
native run proves the Home gesture, pending/ready result, return and cleanup.
No release flag or API schema changed. This closes the bounded local
Home-to-Source-result path, not recurring editorial supply or production
quality.

#### September 26 — Home received original as one authored share

App revision `bf96a00f0` makes an individually addressed original a contained
Home share object: current sender/share-time attribution, the material preview,
and its exact “Open original” door sit together inside the existing quiet-object
card. Text previews no longer render a second inset panel inside that card.
This follows the Home contract's rule that authored shares are coherent carded
objects. It changes neither recipient authorization nor original-reader
revalidation; no album, inferred grouping, reply affordance, or audience change
was added.

Focused verification on the committed app revision:

```sh
npm test -- --runInBand --runTestsByPath \
  __tests__/utils/homeRootV2Renderer.test.ts \
  __tests__/components/ReceivedOriginalSurface.test.tsx \
  __tests__/components/home-root/HomeRootExperience.connected.test.tsx
npm run typecheck
npx eslint components/home-root/HomeRootV2UnitRenderer.tsx \
  components/inbound/OriginalMaterialView.tsx \
  __tests__/utils/homeRootV2Renderer.test.ts
```

Result: 3 suites / 26 tests passed; TypeScript passed; ESLint reported no errors
and the pre-existing `HomeRootV2UnitRenderer.tsx` max-lines warning. The
registered native flow
`polish/home-root-social-original` passed 1/1 on the lane's assigned iPhone 16
Pro. Capture:
`travel-app/.maestro/runs/20260926T221849Z-home-root/screenshots/full/home-root-social-original.png`.
That run rendered the working-tree change immediately before it was committed;
the manifest records prior HEAD `aa3e235d6`, so it is not represented as a
post-commit revision receipt. A repeat after commit stalled in Maestro's iOS
XCTest driver before the product flow and was stopped; it is a harness-startup
failure, not product-failure evidence. The passing capture is mock-fixture
presentation/interaction evidence, not real-owner readback, actual-photo
rendering, full-scroll parity, or production acceptance. The Home design check
has two first-viewport reference pairs but reports `externalCanonVerified=0`;
accepted full-scroll visual parity remains open.

#### September 26 — Practical Home possibility → exact venue → return

App revisions `c012b2724` and `758f15460` update the existing practical
rehearsal runner to
read its API port and reserved simulator from `.workspace-lane.json`, refuse an
unbooted assigned device, pass that exact UDID to Maestro, reject a different
API origin, and check that fixture cleanup reports both deletion and
restoration of the owner's prior Home location. A short runner-contract test
retains these requirements and the existing open-now/venue/return assertions.

On the lane's merged backend `debbf7b1e` and product app `bf96a00f0`, with the
runner changes later committed as `c012b2724` and `758f15460`, the native flow
`80-home-practical-open-now` passed 1/1 on its assigned iPhone 16 Pro (iOS
18.2; Xcode 26.5; Maestro 2.6.1). The first attempt used Metro without the
five governed-root flags from the Home-root contract and correctly opened the
legacy Plans shell; it failed before exercising the target behavior. Restarting
Metro with the documented internal rehearsal posture fixed the environment,
and the repeated runs passed: Home exposed the supported `place.open_now` unit,
its destination opened the exact provisioned venue, Back returned to the same
Home unit, and cleanup confirmed row deletion and Home-location restoration.
The runs used only lane Postgres and a synthetic QA actor; `AI_MODE=off` and
`WEB_SEARCH_MODE=off` prevented external generation/search. The runner test
(`node --test scripts/maestro/home-practical-open-now.test.mjs`), `bash -n` on
the runner, targeted ESLint, and `git diff --check` passed. The Maestro debug
record confirms both screenshot commands ran, but the successful debug folder
did not retain PNGs; this is functional integration evidence, not a reviewed
visual-design verdict, real-provider freshness, production venue coverage, or
recurring supply. Full-scroll design acceptance and `make verify` remain open.

#### September 26 — Private original-photo transport contract

App revision `6244103fe` adds a focused regression at the shared Home/reader
media boundary: an individually addressed photo passes its exact content URL
and recipient bearer token to `AppImage`, with client caching disabled. The
test protects the existing private-read design; it adds no media route and
does not broaden the grant.

Backend revision `e41ea8dcf` corrects the image branch of the original-content
route test to use PNG bytes rather than text bytes labelled `image/png`. The
test now asserts byte preservation, PNG signature and `image/png` media type,
while retaining the existing recipient recheck, private/no-store headers,
withdrawal-race, size/hash, and storage-failure assertions.

Focused evidence:

```sh
# travel-app
npm test -- --runInBand --runTestsByPath \
  __tests__/components/ReceivedOriginalSurface.test.tsx
npx eslint __tests__/components/ReceivedOriginalSurface.test.tsx
npm run typecheck

# travel-agent
.venv/bin/python -m pytest tests/api/test_original_delivery_content.py -q
.venv/bin/ruff check tests/api/test_original_delivery_content.py
.venv/bin/ruff format --check tests/api/test_original_delivery_content.py
```

Results: app 1 suite / 10 tests passed, ESLint clean, TypeScript passed;
backend 9 tests passed and Ruff checks passed. The backend route test still uses
mocked owner and storage functions.

#### September 26 — Owner-custodied photo grant through Home

Backend revision `4aba48201` extends the disposable-Postgres original-delivery
acceptance to a PNG source. It creates real Intake custody and relationship
rows, sends the exact original through the production repository/route
functions, reads the recipient-safe grant and content, and composes the actual
Home owner read/projection. Only `download_private_bytes` is stubbed to return
the exact PNG fixture; the test asserts the exact private storage key, PNG
signature, and MIME type. The existing text case remains in the same
parameterized acceptance.

Verification used the lane-assigned PostgreSQL service on port 53173 and its
disposable database. The whole
`tests/domains/relationships/test_original_deliveries_postgres.py` file passed
(4 tests); Ruff check/format and the commit hooks passed. The test directly
invokes the real route functions, not a running HTTP server. Since this lane
has no private S3-compatible media-store configuration, the actual private
object download and native image render remain open. No runtime permission,
storage adapter, or production behavior was changed. Full-scroll design
parity, recurring production supply and the coordinated `make verify` gate
also remain open.

#### September 26 — Source-backed World Catalog runway

Backend revision `3350cd3b4` refreshes the reviewed freshness metadata for
active seasonal and NYC `here` entries, adds two source-backed NYC exhibitions
that extend useful coverage beyond the current NYBG exhibition window, and
adds the Smokies monarch migration window through late October. New and
refreshed `expires_at` values are source-review deadlines, not event end dates;
the active entries retain explicit re-review rather than being given an
artificially long freshness window. The checker covers today plus the next 14
UTC calendar dates, including the whole final day. On September 27 UTC, an
October 11 00:00 expiry proved too early; active rows now expire at October 12
00:00 UTC and remain source-fresh through the full October 11 runway day. The
14-day runway is backed by 5 seasonal and 5 `here` entries, with no generic or
invented rows. The newly
curated exhibition sources are the [Met's Krasner and Pollock exhibition](https://www.metmuseum.org/exhibitions/krasner-and-pollock-past-continuous),
the [Brooklyn Museum's Iris van Herpen exhibition](https://opencollection.brooklynmuseum.org/exhibitions/3450),
and the [National Park Service's monarch migration guidance](https://www.nps.gov/articles/000/witness-a-migration-marvel-this-fall.htm).

The catalog checker passed with `--runway-days 14`. Focused tests passed:

```sh
.venv/bin/python -m pytest \
  tests/home/test_vesper_workbench.py \
  tests/home/test_vesper_workbench_treatment_contract.py \
  tests/home/test_vesper_workbench_voice.py \
  tests/scripts/test_check_vesper_world_catalogs.py \
  -m 'not requires_postgres and not requires_dogfood_wedge and not requires_api_keys' -q
```

Result: 71 passed, 1 deselected because it requires a service-gated
environment. The catalog checker passed 7 tests, including the boundary
regression that an October 11 00:00 expiry cannot cover the entire final day.
The coordinated `make verify` passed on workspace `510bb15`, the backend
working tree subsequently committed as `3350cd3b4` (same checked code/data),
and app `6244103fe`. Backend offline tests: 21,895 passed, 14 skipped, 1,493
deselected, 53 xpassed, one local-Qdrant warning. Tool/validator tests: 1,004
passed; eval replay verified 422 deterministic checks and skipped 14
LLM-backed checks; app journeys: 34 suites / 173 tests; mock/API seams: 6
suites / 185 tests; offline app: 8 suites / 126 tests. Workspace governance,
contract drift, generated types, and documentation gates passed. The doctor
reported `uvicorn` unavailable and service probes unrun by design; the gate did
not exercise a running API or private object store. This closes the immediate
date-sensitive runway gate, not recurring supply, future catalog review before
October 12 UTC, production freshness, full-scroll design parity, or H1's
broader Home value-delivery exit criteria.

#### September 27 — Local private-photo object → native Home → return

The optional photo mode in the existing original-delivery rehearsal now proves
the actual local object-store path rather than stopping at a mocked storage
read. It uploads the checked-in synthetic Rome-table JPG to an explicitly
loopback Moto S3-compatible service, records exact Intake custody, and reads
the recipient-authorized bytes through the running local API. Before launching
Maestro, the runner checks MIME type, byte count and SHA-256 against that
custody record. The assigned iPhone 16 Pro simulator then opened the same
photo from Home, rendered the exact-original reader, returned to the original
Home unit, and preserved the active owner delivery. Cleanup removed the exact
private object and disposable delivery/sender; the API then returned 404 for
the removed content. Database inspection confirmed no rehearsal delivery
remained. The separate lane-local QA recipient is retained for this lane's
remaining work.

The first native attempt correctly exposed that Maestro's accessibility
visibility check could consider “Open original” visible while its touch point
was underneath the floating tab bar. The flow now performs and captures an
actual upward Home scroll before tapping. This is test-flow correction only;
no production UI behavior or API contract changed.

The exact API body was `image/jpeg`, 368,414 bytes, SHA-256
`0f52adbee1d0275cef3c3904cbca0e01199cec98a1f45cda7dc9017a5e451f44`. Focused
checks passed:

```sh
# travel-agent
PYTHONPATH=. .venv/bin/python -m pytest -q tests/scripts/test_original_delivery_native_rehearsal.py
.venv/bin/ruff check scripts/provision_original_delivery_native_rehearsal.py tests/scripts/test_original_delivery_native_rehearsal.py
.venv/bin/ruff format --check scripts/provision_original_delivery_native_rehearsal.py tests/scripts/test_original_delivery_native_rehearsal.py

# travel-app
bash -n scripts/maestro/run-home-original-delivery.sh scripts/maestro/run-life-original-delivery.sh
node --test scripts/maestro/home-original-delivery.test.mjs scripts/maestro/home-original-delivery-photo.test.mjs scripts/maestro/home-original-delivery-real-photo.test.mjs
(cd travel-app && QA_ALLOW_DATABASE=vesper QA_USER_ID=4b7effb2-bafb-4fcc-8b6b-5ea0d55a09f1 \
  DATABASE_URL=postgresql://vesper:localdev@localhost:53173/vesper \
  EXPO_PUBLIC_API_URL=http://127.0.0.1:53176 \
  MEDIA_S3_BUCKET=vesper-qa-home-originals \
  MEDIA_S3_ENDPOINT_URL=http://127.0.0.1:5013 MEDIA_S3_REGION=us-east-1 \
  AWS_ACCESS_KEY_ID=vesper-qa AWS_SECRET_ACCESS_KEY=vesper-qa \
  VESPER_HOME_ORIGINAL_DELIVERY_MEDIA_KIND=photo \
  VESPER_MAESTRO_UDID=AF31B886-E837-4962-834A-5CBAD5C306DB \
  bash scripts/maestro/run-home-original-delivery.sh)
```

Backend guard tests passed (11), Ruff check/format passed, shell syntax passed,
and app runner contract tests passed (7). The owner-backed runner additionally
passed on the assigned simulator with its cleanup and post-cleanup API checks.
The run used local Postgres on port 53173, API port 53176 and Moto on port 5013;
AI and provider calls were not used. This closes the local private-object and
native photo-render gap for one synthetic owner-authorized delivery. It does
not verify AWS/R2 or production storage, recurring real-user supply, multiple
recipients, provider-generated Home value, accepted design-reference parity,
or H1 completion. The coordinated `make verify` gate remains unrun after this
slice.

#### September 27 — Selected Home viewport review and shell icon correction

The selected Home 02 ordinary-day and Home 03 post-return crops were captured
on the assigned iPhone 16 Pro against local app revision `43d4a7a95`. The QA
doctor passed with lane Metro on port 53177. Focused native captures passed:

```sh
VESPER_METRO_URL=http://127.0.0.1:53177 npm run qa:polish -- home-root --flow=home-root-available
VESPER_METRO_URL=http://127.0.0.1:53177 npm run qa:polish -- home-root --flow=home-root-returned
```

Artifacts: `.maestro/runs/20260927T012045Z-home-root` and
`.maestro/runs/20260927T012146Z-home-root`. The first attempt used a Metro
process without the internal four-root rehearsal flags and correctly exposed
the legacy Plans screen; this was an environment setup failure, not Home UI
evidence. Restarting lane-local Metro with the five governed-rehearsal flags
and mock API mode produced the current Home captures. Manual comparison found
the warm palette, Roman-first value hierarchy, prepared-possibility crown,
week shape and substantial source-bound reading coherent with the selected
02/03 reference direction. These remain L0, reference-only first-viewport
anchors with different fixture content and native status/tab chrome; this is
not full-scroll acceptance, same-content parity, or a claim that the Home 03
note-first example is a required placement.

The concrete visual defect was the four-root tab labeled Home retaining the
legacy briefcase glyph. App revision `43d4a7a95` makes the icon mode-aware:
home/home-outline in the four-root shell, briefcase/briefcase-outline in legacy
Plans. The shell regression suite passed (2 tests), `npm run typecheck`
passed, targeted ESLint passed, and the post-commit Available native capture
passed with the Home glyph visible. `npm run qa:design:check -- home-root`
reports two reference pairs and zero external canon verification. This small
polish fix does not close full-scroll design alignment, recurring or production
supply, or H1. The coordinated `make verify` gate remains unrun.

#### September 27 — Home region-heading and reading polish

A fresh review of the selected Home 02/03 references found that the v2 Home
renderer was reusing the archive's uppercase mono `SectionHeader`. D-H10 calls
for sentence-case sans 13/600 headings with a hairline. App revision
`383c226ac` adds a Home-only header and a named `sectionHeading` text role,
leaving the shared archive component unchanged. Direct native comparison then
found the heading ink was too muted; `4d2532bd8` aligns it to Home's primary
ink. The heading is also exposed to assistive navigation as a semantic header
in `6035e428d`.

That same visual review caught a gold vertical strip on the source-backed Home
reading. It violated kernel §12.6's left-edge accent ban. App revision
`624f5b114` removes that strip without changing the reading, its comparison,
source attribution, or the existing gold status/door roles. The focused Home
screen test now guards the no-left-border treatment and sentence-case region
labels.

The updated Available and Returned states were captured on the assigned iPhone
16 Pro after the visual changes:

- `.maestro/runs/20260927T014514Z-home-root` — Available, app `4d2532bd8`.
- `.maestro/runs/20260927T014612Z-home-root` — Returned top + close, app
  `4d2532bd8`.

Both were manually reviewed against the registered L0 references; the heading
register, contrast and hairline now align, and the Home reading no longer has
the banned colored edge. The accessibility-role commit followed those captures
and does not alter pixels; its behavior is covered by the focused component
test. `qa:design:check -- home-root` still reports one manifest/two reference
pairs and zero verified external canon. This is a targeted native polish
review—not all-seven-posture certification, full-scroll/same-content design
parity, recurring real-owner supply, or H1 completion.

Checks after these changes: `npm test -- --runInBand
__tests__/components/HomeRootV2Screen.smoke.test.tsx` passed (23 tests);
`npm run typecheck` passed; targeted ESLint passed (the renderer file reports
only its existing 1,408-line max-lines warning); and
`npm run design-tokens:check` passed. The coordinated `make verify` also
passed on this lane after the polish wave: backend offline suite 21,906 passed,
14 skipped, 1,493 deselected and 53 XPASS (one local-Qdrant warning); tool and
validator checks 1,004 passed; deterministic eval replay 422 checks with 14
LLM-backed checks skipped; 34 app journey suites / 173 tests and 126 app
offline tests passed; app typecheck, API snapshot/projection/generated-type
checks, API coverage, workspace/child governance, and 389 Maestro flow
structure plus serial syntax validation passed. This is local coordinated
verification only—not hosted CI, production-data acceptance, recurring supply,
or design parity. The first-viewport captures also show the floating root dock
over part of the long reading. At that point it remained an open review item;
the following investigation identified the actionable cause and corrected it
at the Home-to-shell interaction seam, without changing shell geometry.

#### September 27 — Canonical retained Source material read

The existing Postgres Intake projection test now passes a real canonical
`source_attachment_ref` from its retained Place-photo record through
`load_governed_source_materials`. With a synthetic owner and fixture photo
metadata in the lane's disposable PostgreSQL database, private loading returns
the exact current Source revision and preserves the limit that this gesture
does not establish a visit. Group loading returns an explicit
`AUDIENCE_UNAUTHORIZED` omission; after the Intake owner deletes the submission,
the same reference returns `SOURCE_UNAVAILABLE`. No private bytes were read,
no provider ran, and no Home production was generated by this test.

```sh
# travel-agent; TEST_DATABASE_URL names only this lane's disposable Postgres.
TEST_DATABASE_URL=postgresql://vesper:localdev@localhost:53173/vesper \
DATABASE_URL=postgresql://vesper:localdev@localhost:53173/vesper \
TEST_DATABASE_DISPOSABLE=1 AI_MODE=off WEB_SEARCH_MODE=off \
DISABLE_LLM_BACKGROUND_LOOPS=true PYTHONPATH=. .venv/bin/python -m pytest \
tests/inbound/test_intake_subject_postgres.py -q -x
PYTHONPATH=. .venv/bin/python -m pytest \
tests/root_projection/test_source_contribution_materials.py -q -x
.venv/bin/ruff check tests/inbound/test_intake_subject_postgres.py
.venv/bin/ruff format --check tests/inbound/test_intake_subject_postgres.py
```

Results: Postgres Intake module 5 passed; canonical Source-material suite 9
passed; Ruff check and format passed. The lane-local DB was started from the
workspace's isolated Compose project and migrated to the current backend head
before testing. This proves the owner-backed material adapter and its private
audience/deletion boundary against persisted Intake rows—not the complete
Source discovery → workflow → generated result → Home path, actual user
content, production supply, or design parity. H1 remains in progress.

#### September 27 — Canonical Source workflow reaches Home through structured producer

A new disposable-Postgres regression now sends an explicit OS-share text
submission through persisted Intake state, confirms its derived Experience
Anchor, and pairs it with an evidence-receipted approved Place dossier. It uses
the production Source discoverer, canonical owner-read registry and plan,
governed material loader, explicit workflow route/worker, canonical result
readback, and prepared Home reader. The registered `StructuredSourceContributionProducer`
receives both exact owner materials and decodes/hydrates a deterministic
proposal returned by an injected local caller; canonical authority, source
metadata, and Home/Places expressions are then compiled and retained through
the regular path. No external model or paid provider is involved. Deleting the
Intake submission makes the exact result unavailable and removes it from
prepared Home.

This exercise found and fixed a real authority seam: discovery provides a
revisionless canonical venue handle while the canonical Place owner read
returns the same venue at its current revision. Subject authorization now
matches kind/id/path for such handles, but continues to require exact equality
when the requested subject carries a revision. The unit regression proves both
cases; the Postgres workflow proves the real venue/Place owner-read path.

```sh
# travel-agent; TEST_DATABASE_URL names only this lane's disposable Postgres.
TEST_DATABASE_URL=postgresql://vesper:localdev@localhost:53173/vesper \
DATABASE_URL=postgresql://vesper:localdev@localhost:53173/vesper \
TEST_DATABASE_DISPOSABLE=1 AI_MODE=off WEB_SEARCH_MODE=off \
DISABLE_LLM_BACKGROUND_LOOPS=true PYTHONPATH=. .venv/bin/python -m pytest \
tests/api/test_source_request_delivery_postgres.py -q -x --tb=short
.venv/bin/python -m pytest \
tests/root_projection/test_source_contribution_producer.py \
tests/root_projection/test_source_contribution_runtime.py -q
.venv/bin/ruff check backend/root_projection/v2/source_contribution_runtime.py \
tests/root_projection/test_source_contribution_runtime.py \
tests/api/test_source_request_delivery_postgres.py
.venv/bin/ruff format --check backend/root_projection/v2/source_contribution_runtime.py \
tests/root_projection/test_source_contribution_runtime.py \
tests/api/test_source_request_delivery_postgres.py
```

Results: Postgres Source-delivery module 4 passed; structured-producer plus
Source-runtime suites 42 passed; Ruff check and format passed. The authority
fix is committed as `490d222ed`; the follow-on integration-test commit is
`bda484a37`. These checks establish one persisted, synthetic-owner Intake →
canonical discovery/reads → registered structured-producer contract → explicit
production → exact result → prepared Home → withdrawal path. The source, user,
dossier, and model proposal are fixtures; the caller is injected and local.
This is not evidence of real-world editorial quality, paid-provider behavior
or cost, recurring supply, all Home postures, mobile rendering, full-scroll
design parity, or H1 completion.

The full coordinated `make verify` passed on workspace `a765026`, backend
`490d222ed`, and app `6035e428d` before the test-only commit `bda484a37`. It
reported backend offline tests 21,907 passed / 14 skipped / 1,494 deselected /
53 xpassed (one local-Qdrant warning), 1,004 tool/validator tests passed, 422
deterministic eval checks verified with 14 LLM-backed checks skipped, API
projection/type/coverage checks green, app journeys 34 suites / 173 tests,
mock/API seams 6 suites / 185 tests, and offline app 8 suites / 126 tests.
Workspace governance and all 389 Maestro flow syntax checks passed. The
workspace doctor reported `uvicorn` unavailable and service probes unrun by
design; `make verify` did not exercise a running API or production data. The
latest test-only commit was separately re-run against the lane's disposable
Postgres (4 delivery tests) and the 42 producer/runtime tests. H1 remains in
progress.

#### September 27 — Expected Source rejections close as explicit outcomes

Review of the persisted worker path found that continuity classified normal
non-admission states, but then tried canonical readback for any non-`None`
production object. A compiler-rejected draft therefore raised lease loss after
its attempt had already been completed; a pipeline rejection completed storage
but surfaced to the worker as generic producer silence. Continuity now returns
a content-free terminal outcome and exposes a production only for admitted
output. Only `produced` is retained and read back; a canonical cache hit is
`reused`; silence, provider failure, compiler rejection and pipeline rejection
complete without output/readback. The exact-result route now reports those
no-output outcomes as `no_useful_result` with their precise reason. Rejected
drafts do not cross the worker receipt boundary.

The regressions cover all four non-production outcomes at the continuity seam.
The real disposable-Postgres workflow additionally exercises pipeline and
compiler rejection end to end: each attempt records the precise state, the
workflow reaches `completed`, the result contains no production, and the
retained-contribution table stays empty. The repeated worker run is
`not_claimed`, not stranded in `running`.

```sh
# travel-agent; offline tests do not probe or clean an ambient database.
PYTHONPATH=. .venv/bin/python -m pytest \
  -m "not requires_postgres and not requires_api_keys and not requires_dogfood_wedge" \
  tests/root_projection/test_source_contribution*.py \
  tests/api/test_root_source_contribution_wiring.py \
  tests/api/test_agent_workflows.py -q --tb=short

# These URLs identify only the lane's disposable Compose Postgres on port 53173.
TEST_DATABASE_URL=postgresql://vesper:localdev@localhost:53173/vesper \
TEST_DATABASE_DISPOSABLE=1 \
DATABASE_URL=postgresql://vesper:localdev@localhost:53173/vesper \
SKIP_AUTH=true PYTHONPATH=. .venv/bin/python -m pytest \
  tests/api/test_source_request_delivery_postgres.py -q --tb=short

.venv/bin/ruff check \
  backend/api/routes/agent_workflows.py \
  backend/application/root_composition.py \
  backend/root_projection/v2/source_contribution_canonical_executor.py \
  backend/root_projection/v2/source_contribution_continuity.py \
  tests/root_projection/test_source_contribution_continuity.py \
  tests/root_projection/test_source_contribution_canonical_executor.py \
  tests/api/test_root_source_contribution_wiring.py \
  tests/api/test_source_request_delivery_postgres.py
.venv/bin/ruff format --check \
  backend/api/routes/agent_workflows.py \
  backend/application/root_composition.py \
  backend/root_projection/v2/source_contribution_canonical_executor.py \
  backend/root_projection/v2/source_contribution_continuity.py \
  tests/root_projection/test_source_contribution_continuity.py \
  tests/root_projection/test_source_contribution_canonical_executor.py \
  tests/api/test_root_source_contribution_wiring.py \
  tests/api/test_source_request_delivery_postgres.py
.venv/bin/python -m mypy --config-file mypy.ini backend/
```

Results: offline Source/root/worker regressions 302 passed; the disposable-
Postgres Source-delivery module 6 passed; Ruff check and formatting passed;
backend mypy passed across 1,888 files with no issues.
The lane Postgres service was stopped after the tests. No API shape, database
schema, trigger policy or prompt changed. The coordinated `make verify` and
backend `make ci` gates were not rerun after this slice. This verifies expected
terminal handling and retained-output boundaries, not provider-backed quality,
production supply or H1 completion. The implementation is committed on the
backend lane as `a444db9fa`; it has not been published.

#### September 27 — Home reading now drives shared dock collapse

Investigation of the expanded dock over the long Home reading found that both
`HomeRootV2Screen` and its compatibility `HomeRootScreen` maintained their own
scroll behavior but did not forward the clamped vertical offset to the shared
`NavChromeContext.handleScroll`. The scroll callback now updates root reading /
exposure state and forwards that same offset to shared navigation. No new
navigation policy or inset was introduced: the existing contract collapses the
full pill on downward reading and expands it on upward movement or return to
the top. The registered Quiet flow leaves its terminal "rest close" read
uncentered, preventing an automatic centering correction from reversing scroll
direction, and asserts the accessible compact-nav action before capture.

Evidence on the lane's assigned iPhone 16 Pro simulator: mock-only
`home-root-quiet` passed, including the compact-navigation assertion. The
captured end-of-scroll frame shows the Home affordance collapsed to one icon
instead of covering the reading with the full four-tab dock. Run folder:
`travel-app/.maestro/runs/20260927T035625Z-home-root` (local QA artifact; not a
committed design reference). An initial run with `centerElement: true` did not
prove the scroll posture: centering introduces reverse movement and expanded
the dock. The registered flow now avoids that ambiguity.

Focused checks after the code change:

```sh
cd travel-app
npm test -- --runInBand \
  __tests__/components/HomeRootV2Screen.smoke.test.tsx \
  __tests__/components/HomeRootScreen.smoke.test.tsx
npm run typecheck
npx eslint \
  components/home-root/HomeRootV2Screen.tsx \
  components/home-root/HomeRootScreen.tsx \
  __tests__/components/HomeRootV2Screen.smoke.test.tsx \
  __tests__/components/HomeRootScreen.smoke.test.tsx
```

These checks establish scroll-signal wiring and one internal mock-device
interaction; they do not establish all-posture behavior, full-scroll design
parity, production data or H1 completion. The coordinated `make verify` was
not rerun after this slice.

#### September 27 — Coordinated local gate on the current lane tuple

The full workspace gate was run after the backend Source-outcome slice and the
Home scroll/dock change, against workspace `881a66a`, backend `a444db9fa`, and
app `670d49183`:

```sh
make verify
```

Result: passed. Backend CI reported 21,914 passed, 14 skipped, 1,496
deselected, and 53 xpassed in the offline suite; the local-Qdrant payload-index
warning remains expected. All 1,004 tool/validator tests passed, mypy passed on
1,888 source files, and 422 deterministic eval checks passed while 14
LLM-backed checks were skipped. OpenAPI snapshot/projection/type sync,
operation coverage, frontend typecheck, 34 journey suites / 173 tests, 6
mock/API seam suites / 185 tests, and 8 offline suites / 126 tests passed. The
Maestro syntax/governance checks covered 389 flows; the remaining workspace
registry, documentation, compatibility, and evidence-integrity checks passed.

The doctor reported `uvicorn` unavailable and intentionally did not probe or
start services. This gate does not run native simulator flows, a live API,
production data, or external providers. Its result establishes a current local
cross-repository code/contract baseline only—not recurring useful supply,
accepted full-scroll design parity, or H1 completion. No files were generated
or left dirty by the gate.

#### September 27 — Full native Home posture and social-receiving capture

The registered native Home matrix now captures all seven postures plus the
separate received-note and received-photo paths on the lane-assigned iPhone 16
Pro. Final run `20260927T050123Z-home-root` completed **9/9** captures, with
the photo flow also capturing its exact reader and return. The screenshots and
manifest are local QA artifacts under
`travel-app/.maestro/runs/20260927T050123Z-home-root/`; they are not committed
design references. App product code in the capture was `670d49183`; the
photo-flow selector/test correction was committed immediately after as
`1b6cfd127` (QA-only; no Home rendering code changed).

The photo flow had been targeting the generic text-original button. The
photo-specific reader is opened through
`home-v2-original-image-open:<delivery_id>`, so the Maestro selector and its
unit assertion now name that actual affordance. Initial photo retries also
showed the mock image as unavailable because the local dogfood-media API and
mock media authorization were not in the runtime. The passing capture used
this lane's API on port `53176` with LLM background loops disabled, Metro on
`53177`, the internal four-root flags, and a process-only local QA JWT. No
credential or environment file was changed. One earlier setup attempt used a
placeholder key before disabling background loops; a startup task received an
Anthropic 401, then the process was stopped and restarted with
`DISABLE_LLM_BACKGROUND_LOOPS=true`. No valid model call succeeded. Keep that
flag enabled for future local QA API sessions without real credentials.

Validation after the flow correction:

```sh
cd travel-app
npm run qa:polish:scenarios
node scripts/maestro/home-original-delivery-photo.test.mjs
VESPER_METRO_URL=http://192.168.86.189:53177 npm run qa:polish -- home-root
```

The first two checks passed (`31` registered scenario IDs; photo-flow test
passed). The full native run passed `9/9`. `qa:design:compare` generated both
registered first-viewport comparison sheets and they were visually reviewed.
These are L0 composition references, not full-scroll design acceptance.

Review notes that remain open rather than being hidden by the capture pass:

- The Returned native first viewport leads with the current-life read and
  recorded trip outcome; Maya's received original is proven only in a separate
  scrolled Home flow, not in the note-first position of the Home 03 reference.
  Decide whether the ordering is intentional before calling that composition
  aligned.
- The Cold fixture is truthful and gives one nearby opening, but its lower
  viewport has substantial whitespace after the week strip. Judge whether this
  reads as a deliberate low-pressure beginning or as insufficient first-use
  value; do not fill it with invented personalization.
- **Resolved:** in the September 1 Live fixture, Saturday dinner is upcoming.
  `current` is the owner-read validity state, not event timing; the old native
  renderer exposed that enum as `CURRENT`, which could misread as “happening
  now.” Home now leaves the valid state implicit and uses the existing
  human-readable owner-state treatment for non-current states. A focused test
  checks both cases. The dated dinner fixture remains accurate. The post-change
  iPhone 16 Pro Live capture passed and was visually reviewed. A broader native
  attempt passed Available, Planning, Live, and Returned, then failed the
  social-original flow after three retries: the original stayed at
  `Opening original…` with only the mock runtime active and the API stopped, so
  its sender/timestamp assertion could not pass. This attempt does not certify
  the full post-change matrix; the earlier 9/9 receipt is from the prior app
  revision.
- The seven posture screenshots are primarily viewport captures, not accepted
  full-scroll references. Production owner reads, recurring content supply,
  and matched full-scroll Claude-design evidence remain unproven.

This improves native implementation/interaction evidence and closes the
photo-flow harness mismatch. It does not promote Home to design parity or
complete H1. The coordinated workspace `make verify` result above predates this
QA-only app commit; the focused checks and the full native capture are the
post-change evidence.

#### September 27 — Post-fix native matrix and structured visual verdict

After the owner-validity wording correction, the registered Home matrix was
rerun against app rendering revision `cd8e8652e` and the lane-local API/Metro
runtime. The current run, `20260927T053220Z-home-root`, passed all **9/9**
native captures: Available, Planning, Live, Returned, received original,
received photo, Quiet, Cold, and Urgent. The API and Metro used this lane's
ports (`53176` and `53177`), internal four-root and relationship handoff flags,
and a process-only local QA identity. Background generation/provider loops
were disabled; this run did not validate paid providers or production data.

The two registered Home 02/03 pairs were opened and reviewed beside their
native captures. They are L0 first-viewport composition references, not
same-content comparisons or full-scroll canon. The verdict validated and was
committed at
`travel-app/docs/surfaces/home-root/verdicts/20260927T053220Z.json`, with its
manifest snapshot. It records all 23 expected assertions: 21 pass and two are
`na` because the returned four-region scroll and Quiet crown are outside the
captured frames. All four gates pass for the evidence captured; the verdict's
bounded `overall: pass` does **not** certify full-scroll parity. The run had no
prior dimension summary, so it establishes the first structured rubric
baseline rather than a before/after regression result.

The committed verdict records 18 p2 refinements across the captures, including
the long geology-reading stack, generic Ask Vesper doors, repeated urgent/live
copy, and the collapsed Home control overlapping a small part of the received
photo. The two already-open H1 composition questions remain unresolved:
whether Maya's note should lead the returned opening, and whether Cold's lower
whitespace feels like deliberate low pressure or insufficient first-use value.
Do not turn either into a code change without resolving the composition intent.
The regenerated app design status now places Home at **L4-doctrine** for this
capture matrix; this is not L5 or accepted Claude-design parity. App
`docs:check` passed after adding the verdict, and `npm run design:status`
refreshed the generated status projection.

This receipt strengthens native posture/social evidence and creates a
re-runnable visual review record. It does not establish full-scroll design
alignment, real-owner personalization, recurring editorial supply, cost, or
H1 completion.

#### September 27 — Current coordinated gate

`make verify` passed on the coordinated lane revisions at the time of the run:
workspace `8f2ecf0fcf03b0fbae8525d10e9cb3e4cd97df63`, backend
`a444db9fa82a6cd297c4078bc9e235c9bebbf35c`, app
`ccef6395382f650f97a1a7dea9aee28f8529cca2`. Backend offline tests reported
21,914 passed, 14 skipped, 1,496 deselected and 53 xpassed; the local-Qdrant
payload-index warning remains expected. The 1,004 workspace tool/validator
tests, backend mypy over 1,888 files, 422 deterministic eval checks, OpenAPI
snapshot/projection/generated-type checks, API coverage, app typecheck, 34
journey suites / 173 tests, 6 mock/API suites / 185 tests, 8 offline suites /
126 tests, and the 389-flow Maestro syntax/governance sweep passed. Fourteen
LLM-backed eval checks were skipped. The gate completed its World Catalog
runway, branch/flag, documentation, compatibility and evidence-integrity
checks. `uvicorn` was unavailable; services, native simulator flows, production
data, external providers and full-scroll design parity were not exercised.
This is current local integration evidence, not H1 completion or release
authorization.

#### September 27 — Comparison-led Home output avoids duplicate explanation

Home now omits the composition's prose `substance` only when the Home
projection is led by a native comparison. The comparison title and structured
facts, scope caveat, source provenance, and Life continuation remain visible;
standard/deeper projections and prose-led Home reads still show the substance.
This is a bounded presentation choice: let the comparison carry its own
meaning rather than explain the same contrast a second time. App change and
focused test are committed as `9a0b25e13`.

The photo-social native flow also now follows the affordance actually available
in the mock recipient session. Without an auth token, the preview deliberately
offers the explicit **Open original** action instead of making the image itself
a tappable button; the exact reader and return are unchanged. The old Maestro
selector expected the authenticated image-tap affordance. The test was updated
to assert the mock session's explicit button, not to alter product behavior.

Focused verification passed:

```sh
npm test -- --runInBand __tests__/components/RootCompositionRenderer.test.tsx __tests__/components/HomeRootV2Screen.smoke.test.tsx
npm run typecheck
npm run qa:polish:scenarios
npm run qa:design:check -- home-root
VESPER_METRO_URL=http://127.0.0.1:53177 npm run qa:surface -- home-root --after
```

The native matrix captured **9/9** states on the assigned iPhone 16 Pro,
including the exact photo reader/return and Returned full-scroll close. The
staged JPG was served read-only from the lane's existing dogfood-media file
through a temporary static bridge on assigned port `53176`; Metro used `53177`
and the internal four-root, mock and relationship-handoff flags. No database,
live API, LLM provider, production account, or persistent environment change
was used. The capture manifest records base HEAD `ccef63953`: capture happened
before commit, with exactly the three reviewed app files dirty; those exact
files were committed as `9a0b25e13` without subsequent content edits. Thus the
rendered tree matches this app commit, although the manifest itself names its
pre-commit HEAD.

The selected Home 02/03 references and the updated Available, Returned, Quiet,
and received-photo screenshots were visually reviewed. The comparison is
shorter and still retains its caveat and provenance; its detailed anatomy
remains scroll content, and the references are first-viewport composition aids
only. `qa:surface` generated a new pending verdict scaffold, not a completed
structured visual verdict. This is capture and focused-behavior evidence, not
accepted full-scroll design parity, recurring/production supply, or H1
completion. The coordinated workspace `make verify` has not been rerun after
this app slice.

#### September 27 — Home continuation doors name their subject

App commit `d1cea4334` gives three Home-to-Chat resource fallbacks contextual
labels from their already-rendered unit semantics: the planning loose end says
**Ask about the meeting point**, a cold nearby invitation says **Ask about this
walk**, and urgent recovery says **Ask about the alternative**. Unmatched
units retain their existing generic labels. This makes the action's subject
legible without changing Home selection, ownership, destination resolution,
permissions, or generation.

At that copy-only change, these resource fallbacks still opened the existing
Chat route with Home's return token; they did not seed context. The typed
`chat.continue` route already carried graph context. The follow-on below closes
the resource-fallback gap for three supported Home owner rows without changing
other resource kinds.

Focused verification after the commit passed: the connected Home suite (6
tests), app typecheck, Prettier, 31 registered polish scenario IDs, and the
Home design-reference check (1 manifest, 2 pairs; `externalCanonVerified=0`).
The Home Polish QA doctor passed. Three mock-only native captures on the
assigned iPhone 16 Pro rendered and were visually reviewed. Their manifests
record app base SHA `9a0b25e13` with this slice's two app files modified; only
Prettier formatting followed before those exact behavior changes were committed
as `d1cea4334`:

| Flow | Result |
| --- | --- |
| `polish/home-root-planning` | Captured; “Ask about the meeting point” — `.maestro/runs/20260927T144648Z-home-root/screenshots/full/home-root-planning.png` |
| `polish/home-root-cold` | Captured; “Ask about this walk” — `.maestro/runs/20260927T144742Z-home-root/screenshots/full/home-root-cold.png` |
| `polish/home-root-urgent` | Captured; “Ask about the alternative” — `.maestro/runs/20260927T144832Z-home-root/screenshots/full/home-root-urgent.png` |

Metro used the lane's assigned port `53177`; the app bundle used explicit
process-only four-root/internal and mock flags. These captures used no live API,
database, provider, or production account. They cover only the three changed
states; the nine-state matrix, structured visual verdict, full-scroll parity,
and coordinated `make verify` were not rerun for this copy-only slice.

#### September 27 — Home owner context reaches review-first Chat

The three subject-labeled Home resource fallbacks now enter the existing
private review-first composer with the exact current owner attached:

| Home door | Seed owner | Draft | Composer attachment |
| --- | --- | --- | --- |
| Planning loose end | `experience_graph/plan` | “Help me think through this open choice.” | The rendered loose-end label |
| Nearby invitation | `experience_graph/opening` | “Tell me more about this possibility.” | The rendered invitation title |
| Recovery instrument | `experience_graph/commitment` (the exact underlying Commitment id) | “Help me understand this change and what I can do next.” | The rendered recovery summary |

The app creates this route only when the owner ref is a UUID and exactly
matches the resource represented by that unit. Non-UUID fixture ids continue
to use the existing unseeded fallback. The user can inspect or remove the
attachment and edit the draft; no first turn is staged until they explicitly
send. Home's return token is preserved.

The backend now resolves `plan` in the authenticated viewer's personal or
together Experience Graph projection. The Plan block contains its current
title/type/lifecycle/revision/horizon plus only currently visible linked
Commitments and Occasions from that same projection. As with the existing graph
seed kinds, stale Home `clientContext` does not enter the prompt. This is
one-turn contextual grounding; it adds no memory write-back, group delivery,
provider call, autonomous action, or permission grant.

Focused verification passed:

```sh
cd travel-app
npm test -- --runInBand \
  __tests__/components/home-root/HomeRootExperience.connected.test.tsx \
  __tests__/utils/rootProjectionNavigation.test.ts \
  __tests__/screens/conversation-create.smoke.test.tsx
npm run typecheck
cd ../travel-agent
PYTHONPATH=. .venv/bin/python -m pytest -q \
  tests/concierge/test_conversation_seed.py
```

These changes are committed on the coordinated lane as app `af441e1e5`
(`Carry Home owner context into Chat`) and backend `f9fed77a3`
(`Resolve Home Plan context for Chat seeds`). The focused app run passed 96
tests across the three named suites; backend seed tests passed 46 cases. App
typecheck and focused Ruff checks passed. ESLint exited successfully with one
import-order warning in the existing conversation-create smoke test. The
31-scenario polish registry and Home design-reference governance check also
passed.

The connected Home tests cover all three owner paths and ensure mock IDs do not
become authoritative seeds. Composer tests cover visible context, editable
draft, explicit send, and private audience. Backend seed tests cover
viewer-scoped Plan re-resolution and exclusion of stale Home copy. These checks
do not establish generated-answer quality, live-service acceptance, group
behavior, a native screenshot of the composer, recurring production supply,
accepted full-scroll design parity, or H1 completion. The coordinated
`make verify` subsequently passed on workspace code HEAD `714f2724e`, backend
`f9fed77a3`, and app `af441e1e5`; the workspace contained only the two receipt
doc edits recorded here and in the program roadmap. Backend CI passed 21,916
tests (14 skipped, 1,496 deselected, 53 xpassed; one local-Qdrant warning),
tool-contract tests passed 1,004, eval replay verified 422 deterministic checks
with 14 LLM-backed checks skipped, app journeys passed 173, API seam tests
passed 185, and offline app tests passed 126. OpenAPI projection, API coverage,
workspace governance, and serial Maestro syntax checks for 389 flows all
passed. The doctor noted `uvicorn` unavailable and left service probes unrun;
this gate did not start live services. Separately, the native polish doctor
stopped before capture because Metro was not running at default `:8081` (the
assigned lane port is `53177`). No composer screenshot or visual acceptance is
claimed for this change.

H1's remaining high-level gaps are recurring/production supply and accepted
full-scroll design parity; the Home-to-Chat resource-fallback context break is
now closed locally for these three supported owners.

#### September 27 — focused native receiving and return capture

After the Home-to-Chat code and coordinated gate, a focused native capture
rechecked the pre-existing received-original continuation on app
`af441e1e5`. On the lane-assigned iPhone 16 Pro, the mock recipient opened the
attributed Home original, opened its exact reader, and returned to the same
Home unit. The Maestro result captured 1/1 persona and both extra screenshots;
the manifest records `dataContext: null`. Command:

```sh
VESPER_METRO_URL=http://192.168.86.189:53177 \
  node scripts/polish-qa/run-polish-qa.mjs home-root --after \
  --flow=polish/home-root-social-original
```

The server was started in Expo LAN mode on the assigned Metro port with
process-only internal, four-root, relationship-handoff and mock flags. This
used no live API, database, account, model or paid provider. The exact captured
screens and log are retained under
`travel-app/.maestro/runs/_pairs/home-root/after/` on the lane (ignored QA
output, not committed evidence). The first attempt with host-loopback Metro
passed the doctor but the simulator could not connect; the lane-reachable LAN
address made the actual flow pass. `travel-app/AGENTS.md` now records the
simulator-reachability check so a host-side doctor result is not mistaken for
capture evidence.

This capture does **not** exercise the new Home-to-Chat owner-seeded composer,
does not provide a structured visual verdict, and is not accepted full-scroll
design parity. The screen was opened to confirm the native path, but no
comparison against an adopted full-scroll canon was performed. The Home-to-Chat
context behavior remains covered by focused connected/component and backend
seed tests, not a native composer capture. The current `--after` run folder
contains only this targeted persona; it is not the previously captured 9-state
matrix. No H1 exit criterion is removed by this receipt.

#### September 27 — native Home Plan to private Chat composer

App commit `eb8429120` adds a registered native scenario for the just-implemented
Plan fallback. The mock-only Home row opens the review-first Chat composer; the
capture asserts the private audience, suggested draft, and full accessible
label of the removable Plan attachment. The draft was not sent. The dedicated
persona uses a UUID-shaped synthetic owner ref so it takes the guarded route;
it is isolated from normal Home mock personas and is **not** a persisted Plan,
backend-read evidence, or send authority.

The assigned iPhone 16 Pro captured 1/1 persona on iOS 18.2, with
`dataContext: null`. The screenshot is
`travel-app/.maestro/runs/_pairs/home-root/after/screenshots/full/home-root-chat-plan-composer.png`;
the exact capture command and attempt log are retained in the same ignored QA
run folder. The manifest records pre-commit app HEAD `7f96afa8a`; the four
captured fixture/registry/flow changes were committed as `eb8429120` without
subsequent edits. No live API, database, production account, provider or send
was involved. Metro and the app used the lane-assigned `53177` port and LAN
address.

The attachment appears as a compact, visually ellipsized chip in the composer;
the captured accessibility label retains its full title. The test verifies the
accessible attachment and screenshot only; no structured visual verdict or
design comparison was completed. This adds native evidence for the Plan owner
path, not native proof of backend Plan resolution, generated answer quality,
full-scroll parity, recurring supply, or H1 completion.

#### September 27 — native Home opening and recovery to private Chat composer

App commit `772bee902` adds isolated mock personas and registered native
scenarios for the two remaining supported Home resource doors. On the assigned
iPhone 16 Pro / iOS 18.2, both passed 1/1: nearby opening
(`20260927T162503Z-home-root`, scenario `M1-ana-cold-start`) and recovery
(`20260927T162550Z-home-root`, scenario `M6-urgent-open-decision`). Each flow
opens the private, editable composer, retains the exact resource attachment,
asserts the suggested prompt and full accessible attachment label, and stops
before Send. Both manifests have `dataContext: null`; the capture used mock
mode and the lane-reachable Metro server on port `53177`.

The manifest app SHA is `eb8429120`; the new fixture/flow changes were present
in the running app and committed afterward as `772bee902`, with no subsequent
app edits. Screenshots and attempt logs remain in the ignored, run-specific
folders under `travel-app/.maestro/runs/20260927T162503Z-home-root/` and
`travel-app/.maestro/runs/20260927T162550Z-home-root/`. No live API, database,
production account, provider, or send was involved. As on the Plan capture, the
attachment chip is visually ellipsized while its accessible label remains
complete. These captures prove client-side UI routing and review posture for
the three mock owner types; they do not prove backend resolution on-device,
answer quality, persisted real-owner data, a structured visual verdict,
full-scroll design parity, recurring supply, or H1 completion.

#### September 27 — preserve current commitment state in Home-to-Chat seeds

Backend commit `1a190224a` extends the existing viewer-scoped seed formatter
for direct Experience Graph Commitments and Plan-linked Commitments. A later
disposable-Postgres acceptance found that the initial revision `0` was dropped
by truthy-value filtering; follow-up commit `6d99a195c` now preserves revision
zero in graph seeds and plan-linked commitment summaries. The seed keeps owner
status, coordination state, provider state, revision, visibility, and an
optional current time window distinct. Both paths derive these values from the
same personal-then-together projection used to resolve the exact current owner;
stale Home `clientContext` remains excluded. The same follow-up closes a group
privacy gap: Experience Graph seeds are discarded before owner lookup on group
turns. No API shape, provider call, memory write-back, or action authority
changed.

The focused seed suite passed (47 tests):

```sh
PYTHONPATH=. .venv/bin/python -m pytest -q tests/concierge/test_conversation_seed.py
```

`PATH="$PWD/.venv/bin:$PATH" make lint` passed, including Ruff, import-boundary,
lazy-import, import-cycle, and route-shadowing checks. `make typecheck` passed
for 1,888 backend source files; `git diff --check` passed. The initial lint
invocation with the system Python could not import FastAPI; rerunning with the
repository virtual environment on `PATH` passed. This test uses synthetic
projection objects and proves formatter/owner-selection behavior only. It does
not exercise a live API/database, on-device backend resolution, generated
answer quality, provider cost, recurring supply, design parity, or H1 exit.

#### September 27 — database-backed Home seed assembly and group privacy

Backend commit `6d99a195c` adds a real-PostgreSQL acceptance test for the
production `_build_turn_prompt_kwargs` path. In a fresh lane-owned disposable
database migrated to Alembic head, the test creates a synthetic owner, Plan,
and changed Commitment through the canonical owner commands, then assembles
the prompt context from the real viewer-scoped Experience Graph projection.
It verifies the distinct current state fields and exact time window, preserves
initial Plan/Commitment revision `0`, excludes stale Home copy, and returns no
owner context for another viewer. The same real owner ref returns no context
on a group turn, proving that the seed is dropped before the owner read.

The combined disposable-Postgres and focused seed suite passed (49 tests):

```sh
TEST_DATABASE_URL=<lane-owned-disposable-postgres-url> \
  TEST_DATABASE_DISPOSABLE=1 PYTHONPATH=. .venv/bin/python -m pytest -q \
  tests/concierge/test_conversation_seed_postgres.py \
  tests/concierge/test_conversation_seed.py
```

The disposable database was unique to this run; no ambient/dev database was
used. Backend lint, typecheck (1,888 source files), formatting, import checks,
and route-shadowing checks passed. This reaches the real owner repository and
prompt-assembly boundary but is not an HTTP request, provider/model call,
generated-answer quality evaluation, on-device backend proof, recurring supply,
design parity, or H1 completion. The coordinated `make verify` has not been
rerun after these backend changes.

#### September 27 — private Home seed through the canonical Chat HTTP route

Backend commit `c50268c6e` adds a route-level disposable-Postgres acceptance
for the Home-to-Chat seed. The test creates a synthetic owner, personal
conversation, Plan and changed Commitment through canonical persistence
commands, then sends a request to
`POST /api/conversations/{conversation_id}/messages` with the Home seed. The
real conversation route and `ConciergeSession` create the `TurnContext`; the
production `_build_turn_prompt_kwargs` assembler then resolves the current
owner projection from Postgres. The test confirms the current Plan and
Commitment states, revision `0`, exact time window and owner-specific copy
reach the prompt, while stale Home prose does not.

Only the final `handle_turn` provider/model boundary is replaced: the capture
stub invokes the production prompt assembler and returns a fixed response.
This is an in-process FastAPI HTTP-boundary test, not a networked API server or
a model/provider call. It proves private request-to-session-to-owner-prompt
grounding with synthetic data; it does not establish answer quality, on-device
backend resolution, recurring/production supply, or accepted full-scroll
design parity.

The combined real-Postgres route, owner-assembly and focused seed suite passed
(50 tests):

```sh
TEST_DATABASE_URL=postgresql://vesper:localdev@localhost:53173/vesper_home_seed_http_20260927_a \
  TEST_DATABASE_DISPOSABLE=1 PYTHONPATH=. .venv/bin/python -m pytest -q \
  tests/integration/test_home_seed_chat_http_pg.py \
  tests/concierge/test_conversation_seed_postgres.py \
  tests/concierge/test_conversation_seed.py
```

`PATH="$PWD/.venv/bin:$PATH" make lint` passed, including Ruff, formatting,
import boundaries, lazy-import inventory, SCC ratchet and route-shadowing
checks. `PATH="$PWD/.venv/bin:$PATH" make typecheck` passed for 1,888 backend
source files; `git diff --check` passed. The uniquely named synthetic database
was confirmed to have zero connections, dropped, and its lane Postgres
container stopped without deleting the volume. The coordinated `make verify`
has not been rerun after this test-only slice. H1 remains in progress.

#### September 27 — full native Home-root acceptance review

Run `20260927T180109Z-home-root` captured all 12 registered Home-root and
Home-to-Chat states on the lane-assigned iPhone 16 Pro, using app revision
`f481d22c5`, mock mode and synthetic fixture content. The review completed
all 29 manifest assertions, all four gates and all ten rubric dimensions per
persona. Capture and visible-data correctness passed for every persona; one
Planning assertion failed, along with that persona's visual and intent gates.
The structured verdict is **MIXED**, with 24 evidence-linked findings (one
`p1`, 23 `p2`) and no blocker. It is committed at
`travel-app/docs/surfaces/home-root/verdicts/20260927T180109Z.json`.

The highest-priority finding is precise: the Planning manifest requires one
compact In-motion status row without an icon plate, but the native screen
renders the unresolved meeting point as a large crown card and adds a second
large Saturday route card. Other findings cover vague cold-start place detail,
generic unsent Chat drafts and visually truncated context chips, repeated Live
dinner copy, text-heavy Home readings, an unclear source-freshness word, and
the floating dock overlapping content at some reading positions. The returned
full-scroll close is separately visible above navigation. Home 03's note-first
crop remains reference-only: its order is not treated as an adopted rule or a
contract failure. The photo recipient capture uses a synthetic media fixture;
it does not establish an authorized private-media grant.

This run is native **mock presentation and interaction** evidence only. The
Home-to-Chat captures stop before Send. No backend, authenticated account,
provider, real owner data, recurring supply or production behavior was
exercised. The active comparison references remain first-viewport L0 aids;
full-scroll product design is not certified. This review also corrected three
older verdict roll-ups whose recorded 4–18 minor findings exceeded the shared
threshold: Home `20260927T053220Z`, Places Workspace
`places-workspace-after`, and Trip Itinerary `trip-itinerary-after` are now
MIXED rather than PASS. Against Home's prior dimension/gate snapshot, this run
records 17 newly judged fail states; those are newly surfaced review findings,
not proof that product code regressed between builds. Both Home runs now derive
MIXED under the same baseline.

Focused checks passed:

```sh
node scripts/polish-qa/verdict.mjs validate .maestro/runs/20260927T180109Z-home-root
node scripts/polish-qa/verdict-schema.test.mjs
node --test scripts/maestro/home-original-delivery-photo.test.mjs
npm run qa:polish:scenarios
npm run qa:design:health -- home-root .maestro/runs/20260927T180109Z-home-root
```

Results: verdict valid with derived `mixed`; 39 schema checks passed; photo
fixture contract test passed; 31 scenario IDs registered; capture-health
reported no visual-health assertions are configured for Home. The verdict
diff's 17 dimension/gate changes were recomputed against the previous Home
review after its overall roll-up was corrected; the filed regression list
matches that computed diff. The coordinated
`make verify` has not been rerun on this latest app/backend tuple.

#### September 27 follow-up — compact Planning loose end

App commit `fd765d1ba` keeps the unresolved Plan visible under **In motion** as
one compact, tappable status row, while preserving its exact Plan destination.
It no longer renders as a page-level crown or icon-plated card. The Home
renderer test explicitly guards this compact treatment even when the row is
the dominant semantic item. The focused component/renderer suites passed (42
tests), app typecheck passed, and ESLint reported zero errors plus its existing
`max-lines` warning for `HomeRootV2UnitRenderer.tsx`.

Native mock capture `20260927T185946Z-home-root` used app revision `fd765d1ba`,
branch `codex/home-value-delivery`, iPhone 16 Pro and Maestro 2.6.1. Its
Planning flow captured 1/1 state; `npm run qa:polish:scenarios` registered 31
flows. The structured one-state verdict is **PASS** and records no regressions,
with two bounded P2 findings still open: repeated meeting-point wording and
reduced pre-tap action discoverability after removing the explicit “Ask about”
label. This is a posture-specific result, not a new full-matrix verdict.

The flow-filtered run had no matching Available/Returned app screenshots for
the two Home design-reference comparisons, so those comparisons are not
certified by this capture. The prior 12-state Home matrix remains **MIXED**;
full-scroll design parity, backend/real-owner behavior, production supply, and
the coordinated `make verify` are not established here. An initial capture
attempt using simulator loopback could not load its bundle; restarting the
lane-owned Metro server on LAN resolved the environment issue, and the passing
capture used that corrected setup.

Next Home work should close the remaining connected-value gap using current
owner-backed evidence, not broaden the fixture matrix: verify that the
source-backed Place reading and exact destination survive the governed Home
owner path, then judge the delivered content with its real provenance. The cold
native review has two bounded P2 follow-ups—equal visual weight for `Why this?`
and `Open in Places`, and the cryptic newcomer close “The rest keeps.” The
12-state Home matrix remains MIXED, and the earlier two Planning-row clarity
findings remain open. Keep Chat and Life screen design outside this package;
mock-native success does not establish production/recurring supply or full
design parity.

#### September 27 — source-backed Cold Home opening

App commit `1408699e1` aligns the Cold Home fixture with the backend's existing
Places editorial promotion: one substantive Red Hook reading, preserved source
refs and an exact `/dossier/41` Places destination. The previous generic
waterfront-walk prompt now exists only in the separate Home-to-Chat seed
scenario, so Cold Home demonstrates delivered value instead of another input
request. The dominant read uses the registered serif reading role. The QA
manifest explicitly marks its home/route/dinner week-shape labels as synthetic
demo data rather than live calendar evidence.

On the lane-assigned iPhone 16 Pro, run
`20260927T193324Z-home-root` captured 1/1 Cold state. Structured verdict
`d1f2111cf` is **PASS** for that posture with two P2 findings: `Why this?` and
`Open in Places` have equal visual weight, and “The rest keeps” is cryptic for a
newcomer. The exact destination is separately verified by the connected route
test. The run is a mock-native presentation/interaction capture; it proves no
live owner read, production editorial quality, recurring supply, real calendar
context or full-scroll design parity. The focused Home suite passed 47 tests,
`npm run typecheck` passed, ESLint exited 0 with the existing renderer
`max-lines` warning, 31 polish flows registered, and the Home design-reference
check passed. The matching backend cold-promotion and fallback tests also
passed (2 passed, 81 deselected), proving the existing deterministic portfolio
selection boundary only. The lane-assigned PostgreSQL endpoint at
`127.0.0.1:53173` did not respond, so no database-backed owner acceptance was
attempted. `make verify` has not been rerun after this slice.

#### September 27 follow-up — persisted cold Home Place opening

Backend commit `a38d5c7f3` closes a real posture-boundary defect. When a
world-only Places reader had candidates, its helper attached a local `quiet`
signal. Home incorrectly treated that as the person's own Home lifecycle, so a
genuinely empty Experience Graph with useful Place material became `quiet`
before the cold promotion could run. Posture resolution now ignores signals
from `places_context` and `contextual_places`; owner-derived signals and
owned-content posture behavior remain intact. The unit regression supplies the
world-only `quiet` signal explicitly, and the HTTP acceptance reads a genuinely
cold Experience Graph plus accepted public Place Sources through the real Home
route and portfolio.

The route test verifies `home_posture=cold`, one substantive
`now_invitation`/composition, both persisted Place Source references, the exact
city Place destination, and the Places root/capability. Its unrelated owner
readers return empty results so this remains a focused source-to-Home contract,
not a timing benchmark or a synthetic outage simulation. The Place, Source
records, and owner are test fixtures; the route does not call a model or a
provider. This proves the local dark HTTP path can deliver existing accepted
world material before personal history exists. It does not prove real-source
quality or supply, authenticated app-to-backend behavior, recurring/production
content, or full design parity.

The focused Home portfolio plus persisted Place HTTP modules passed (87 tests)
against a newly created lane-owned disposable database. The named database was
confirmed absent before creation, migrated to head, had zero active connections
after the tests, and was dropped; the lane's normal `vesper` database and
Compose volume were untouched.

```sh
TEST_DATABASE_URL=postgresql://vesper:localdev@127.0.0.1:53173/vesper_home_cold_http_20260927 \
  TEST_DATABASE_DISPOSABLE=1 PYTHONPATH=. .venv/bin/python -m pytest -q \
  tests/root_projection/test_home_portfolio.py \
  tests/integration/test_public_place_content_home_http_pg.py
PATH="$PWD/.venv/bin:$PATH" make lint
make typecheck
git diff --check
```

Backend lint passed (including Ruff, formatting, import boundaries, lazy-import
inventory, import-cycle ratchet, and route ordering); backend mypy passed for
1,888 source files. A first bare `make lint` selected system Python and stopped
at the route checker because FastAPI was unavailable there; the documented
`.venv`-first invocation above passed. Coordinated workspace `make verify`,
backend `make ci`, on-device backend use, real/recurring editorial supply and
the full Home matrix were not established by this slice. H1 remains in
progress. The next decisive gap is substantive, authorized current Source
supply and its actual app-to-backend delivery; do not treat another synthetic
accepted row as evidence that this supply problem is solved.

#### September 27 — app delivery seam recheck

The app already has the semantic Home v2 network path; another API client or
parallel Home data service is not the next implementation. `HomeRootExperience`
consumes `useHomeRootProjectionV2`, which requests the typed backend operation
in real mode and uses the persona fixture in mock mode. The request is part of
the coherent product-system gate: shell, Home v2, Places governed runtime and
Life v1 must all be requested, and the build must have development/internal
authority. These flags default off. Thus the mock iPhone pass and the
disposable-Postgres HTTP proof establish adjacent boundaries, not the combined
authenticated app experience.

The next delivery acceptance should turn on that existing internal/dev gate,
point the real app at the lane API, and confirm the cold Place-backed unit
renders and opens its exact Places destination without using the fixture. Use
the same synthetic owner/source only for this local rehearsal; it would still
not validate real editorial quality or recurring source supply. If the existing
auth/dev rehearsal cannot supply a test identity safely, resolve that setup
separately rather than bypassing the authenticated route or broadening the
serving contract. The remaining cold-copy P2s and the MIXED full Home matrix
still need their own acceptance; they are not blockers to tracing the current
network seam.

#### September 27 — governed cold Home through API, native app, and return

The previous runner still searched for the retired `horizon_editorial_passage`
kind and could select any booted simulator. App commit `91c93cd6e` updates its
selection to the current `now_invitation` composition and requires the assigned
lane device to be booted before provisioning; it passes that device explicitly
to Maestro. The matching runner-contract test checks the selector, device
preflight, and exact-source assertions.

On the lane-assigned iPhone 16 Pro (iOS 18.2), the existing Home public-reading
sequence passed against the local API and a newly created, lane-owned disposable
Postgres database. The route returned Cold posture and one invitation with both
persisted accepted Place Source references. The real app displayed both
interpretations, opened the exact venue in the internal Object Page rebuild,
and Back returned to the same Home unit. The registered flow is
`travel-app/.maestro/78-home-public-reading-sequence.yaml`; its run log is in
`/tmp/vesper-home-cold-native-20260927b/.maestro/tests/2026-09-27_172310/`.
No model or external provider was called. This used a synthetic QA owner with
development `SKIP_AUTH=true`; it establishes viewer-scoped local delivery, not
Clerk JWT behavior, production data quality, or recurring editorial supply.

The rehearsal database was newly created, migrated, verified to have zero
remaining run-scoped observations and zero active connections, then dropped.
The lane's retained `vesper` database and Compose volume were not used for
fixture writes. Runner tests passed (4), shell syntax and `git diff --check`
passed, and the native run exercised the actual owner API in real API mode.
The coordinated `make verify` is still required after the final workspace and
backend revisions. The full Home matrix remains **MIXED**; this specific cold
delivery and return path passes, while full-scroll design parity, recurring
supply, and the remaining copy findings stay open.
