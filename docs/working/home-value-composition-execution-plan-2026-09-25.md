---
doc_type: working
status: active
owner: codex/home-value-delivery lane
created: 2026-09-25
last_verified: 2026-09-26
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
[program roadmap](vesper-program-roadmap.md). This package owns the current
Home implementation. App refinements are committed locally through
`7e7108d9e`: exact share-time attribution (`66e2c3c`, `122f4d2`, `e0bf0a7`),
exact Home return (`8fc767355`), reduced repeated section/canonical-outcome
copy (`1b23ed891`, `a963fa0b9`), and a recipient-only original-material mock
transport plus a dedicated Home scenario (`2840a2420`), and an accessibility
fix for the original note (`7e7108d9e`). Focused tests, typecheck, lint, the
seven-posture native fixture capture, and the recipient/default native Home
flows pass. The full app suite, design-reference acceptance and combined
verification remain open.

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
has `designRefs: []` and `judgeAgainst: 'doctrine'`. Establish specific accepted
screen references through the existing export/registration workflow as part of
H1. A doctrine pass cannot establish visual parity. This bounded reference task
does not require every pending design study to finish before implementation.

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

### First trace — current baseline, 2026-09-25 local

This is a code-path trace, not production-supply or native-visual acceptance.

| Situation | Owner → Home → continuation | Current finding |
| --- | --- | --- |
| Ordinary day / available time | Experience Graph, saves, receipts, automatic Places context and current public Place Sources, plus an optional current prepared Source result → bounded Home portfolio and shared admission → exact Place/Source/owner door and semantic return token | The read path is implemented and bounded; a Home miss does not invoke a provider or enqueue generation. Deeper Source work requires the existing explicit “Ask Vesper” gesture. Existing portfolio/composition tests pass. Ordinary production coverage is not established. |
| Evening with other people | Relationships supplies exact addressed Place notes and individually authorized original deliveries → Home composes a same-Place note with eligible world material, or an attributed multi-note region; original previews keep per-delivery grants → Place or original reader revalidates owner state and returns through Home | Recovered human/Place composition is present. Original media is projected as separate deliveries (maximum two candidates in the current Home adapter); the reader has no reply affordance. No event/photo-set grouping or reply policy is inferred. The newer Home 18 K/L scroll is useful design input for a lead photo and shape-preserving remainder, but cannot create a shared-set identity from individual grants. |
| Healthy live/travel situation | Experience Graph and Plan/proposal owners establish Live; Places current context can supply separately evidenced practical alternatives → Live Home selector keeps independent possibilities eligible; Urgent alone suppresses most support → owner-specific destination/action and exact return | Live is not treated as urgent, and functional selection is covered by the focused backend suite. Provider-backed freshness, recurring generated supply, and native presentation against the selected design remain separate unproven claims. |

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

The `home-root` QA surface still has no registered screenshot/design-reference
manifest. The newer `vesper-home` Board 18 is an additive extension of the
selected 02/03 scrolls; within that assignment, K/L is the selected photo-
integrated full scroll and D/E is a narrower study. K/L keeps one lead original,
the remainder in a shape-preserving row, the rest of Home's city/future value,
and larger-text treatment. The fixture's album, Reply/Ask path, and actual-photo
assets are not supported by current production owners. Home now retains the
opened unit's viewport position when the same projection is revalidated, but
that behavior has focused projection/UI tests, not native-device observation.
Relationship currently supplies individual grants, not a shared-set identity;
the present Home/original-reader path has no Reply action.
Until the applicable owner contracts and a specific isolated reference are
registered through the app's design workflow, this board informs implementation
but establishes neither those behaviors nor native parity.

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

Latest receipt: **in progress**. On the merged recovery baseline, the focused
backend Home portfolio and selection suite passed (86 tests). The first H1 app
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
account or delivery fixture was created.

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
live owner-data readback. The real-owner API rehearsal remains blocked by its
current provider-key startup contract; no key or substitute was supplied.

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

This fixture is only mock interaction/presentation evidence. The real-owner
original rehearsal remains blocked by missing local QA database/account/
provider configuration, and the accepted Home design reference is still
unresolved.
`make verify` remains unrun. H1 is not complete, and this mock does not establish
recurring social supply, photo presentation, production owner readback, or
design parity.
