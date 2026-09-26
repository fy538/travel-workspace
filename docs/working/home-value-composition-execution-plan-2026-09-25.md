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
Home implementation. Home content and renderer refinements are committed
locally through `7d7d5b762`: exact share-time attribution (`66e2c3c`,
`122f4d2`, `e0bf0a7`),
exact Home return (`8fc767355`), reduced repeated section/canonical-outcome
copy (`1b23ed891`, `a963fa0b9`), a recipient-only original-material mock
transport plus a dedicated Home scenario (`2840a2420`), an accessibility fix
for the original note (`7e7108d9e`), original-owner polling lifecycle
handling (`58f53d3fb`), a source-bound geological comparison in Quiet Home
with its duplicate connection card removed (`42cba2d30`), and the more precise
headline “The Palisades began as magma between older rock layers”
(`7d7d5b762`). Focused checks and fixture-backed native captures pass for the
affected content path; the post-commit Quiet capture now asserts the revised
headline. A later local real-Postgres full-scroll rehearsal also passes for a
bounded set of social/editorial/original owners (recorded below). The full app
suite, accepted design-reference alignment, production/recurring editorial
supply, and combined verification remain open.

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
produce this kind of connection. It does not prove the deeper owner-backed
Source contribution workflow or recurring content supply.

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
quality, recurring/AI-generated supply, the prepared Source-result workflow,
real photo rendering, design-reference parity, or global four-root readiness.
The Home 02/03 references remain first-viewport aids; the external canonical
bundle was not verified. The runner does not open every destination in this
full-scroll flow; use the separate original-reader return receipt for that
behavior. `make verify` and release readiness remain unverified.
