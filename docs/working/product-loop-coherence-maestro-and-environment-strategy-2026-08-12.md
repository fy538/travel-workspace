---
doc_type: working
status: active
owner: founder / product / engineering
created: 2026-08-12
expires: 2026-09-11
why_new: Consolidates the product-loop, onboarding, Maestro, automated-judgment, and test-environment conclusions developed in the August 12 architecture discussion; existing convergence plans do not own this end-to-end product-and-certification operating model.
promotes_to: null
supersedes: []
related:
  - thesis-to-experience-convergence-audit-2026-08-09.md
  - intentional-convergence-engineering-plan-2026-08-10.md
  - definition-of-done-consolidation-2026-08-10.md
  - ../reliability/Agent Reliability Playbook.md
---

# Product-loop coherence, Maestro, and environment strategy

> **Working synthesis, not product canon or current-status authority.** This
> document records the conclusions and proposed operating model from the
> August 12 product/architecture discussion. Dated implementation observations
> must be re-verified before action. Durable product decisions belong in canon
> or a decision record; durable testing requirements belong in contracts and
> runbooks; current execution state belongs in generated status and evidence.

## 1. Question and intended outcome

The discussion began with a broad concern: Vesper has accumulated many shipped,
dark, internal, and legacy capabilities, but the experienced product can still
read as a group of features rather than one coherent system. The product has
recently pivoted toward three visible mobile roots—**Trips, Vesper, and
Places**—and the team wants to know:

1. whether the product thesis and implementation are coherent as a whole;
2. whether the three-tab home redesign improved that coherence;
3. what it means to “close the loop” across features, AI, state, and pages;
4. how code tracing and automated certification can replace repetitive manual
   build-and-dogfood cycles;
5. where Maestro fits, what it can and cannot prove, and what the current
   Maestro estate actually certifies;
6. how to prevent screenshots and AI judges from producing lenient or stale
   confidence; and
7. which environments—mock, local real stack, ephemeral cloud, shared dogfood,
   or production—should execute each class of test.

The intended outcome is one actionable model connecting product strategy,
architecture, onboarding, instrumentation, automated testing, visual review,
and environment isolation.

## 2. Executive synthesis

The product thesis is coherent, and the three-tab redesign materially improves
its legibility. The remaining gap is not primarily a lack of features or a need
for another broad architecture wave. It is the absence of a sufficiently
canonical, executable expression of the thesis.

The product should be understood as one accumulating travel system:

> Vesper turns a traveler’s evolving taste, intent, relationships, and
> circumstances into a living trip—and remembers what happened so the next
> judgment is better.

The three roots are not independent feature containers. They are three views
into the same evolving state:

| Surface | User question | Product responsibility |
| --- | --- | --- |
| **Places** | What might I care about? | Attention, discovery, place evidence, taste signals, and later memory. |
| **Vesper** | What should I do with it? | Interpretation, judgment, coordination, proposals, and governed action. |
| **Trips** | What is actually happening? | Durable commitments, Plan state, status, execution, and outcomes. |

The next phase is therefore **loop completion**:

```text
place, idea, need, or constraint
        ↓
Vesper interprets it in context
        ↓
user accepts, corrects, or rejects a proposal
        ↓
canonical trip or personal state changes exactly once
        ↓
all relevant surfaces reconcile to the same revision
        ↓
the lived outcome becomes governed evidence for later judgment
        ↺
```

The implementation substrate is broad and often sophisticated. The observed
weakness is that product vocabulary, tests, docs, evidence, and some navigation
assumptions still contain pre-pivot Discover/Atlas and feature-centric history.
The authored verification system is stronger than its continuously trustworthy
device execution. That makes the next priority hierarchy and operational
closure, not more raw test or feature volume.

## 3. Product coherence after the three-tab redesign

### 3.1 What the redesign fixed

Reducing the visible roots to Trips, Vesper, and Places creates a comprehensible
product grammar:

- **Places gathers and interprets possibility.**
- **Vesper converts possibility and need into judgment or action.**
- **Trips makes accepted decisions durable and operational.**

That is more coherent than asking users to understand multiple overlapping
roots for discovery, archive, assistant, personal state, and trips. It also
gives the AI a clearer role: Vesper is not another content tab; it is the
reasoning and action surface between evidence and durable travel state.

The current mobile tab layout supports this direction. Trips leads, Vesper is
the center action surface, and Places is the third visible root. Discover and
Atlas remain registered as legacy deep-link owners rather than visible tabs.
See
[`travel-app/app/(tabs)/_layout.tsx`](../../travel-app/app/%28tabs%29/_layout.tsx).

### 3.2 What the redesign did not fix by itself

Changing navigation cannot guarantee:

- that a place opened in Vesper carries stable identity and useful context;
- that an accepted Vesper action commits to the canonical Plan exactly once;
- that Trips, Vesper, Places, notifications, maps, and caches show the same
  revision;
- that a user correction changes later assistance rather than disappearing;
- that privacy and audience boundaries survive cross-surface context assembly;
- that dark and legacy features stop competing in product language and tests;
  or
- that the team can certify the above without re-dogfooding every seam.

The redesign is a necessary product simplification. Loop closure is the
architectural and operational work that makes the simplification true.

## 4. What “closing the loop” means

Closing the loop is not merely adding navigation links, and it is not simply
giving an LLM access to every feature. It requires five kinds of continuity.

### 4.1 Navigation continuity

The user can move naturally among the surfaces involved in one job. Back,
resume, deep links, notifications, and app restart preserve an understandable
place in the journey.

### 4.2 Context continuity

The system retains the relevant place, trip, person, audience, decision, and
revision identity. The user should not need to restate which restaurant, which
Lisbon plan, or which collaborator they meant after crossing a surface.

### 4.3 State continuity

An accepted action mutates one canonical authority exactly once. Optimistic UI,
query caches, projections, notifications, chat receipts, Trips, and Places must
reconcile to that authority. A UI success message without the corresponding
canonical mutation is an open loop.

### 4.4 Learning continuity

Acceptances, corrections, rejections, occurrences, and outcomes can affect
future judgment only when their evidence is applicable, privacy-safe, and
correctable. Save is weak attention, not declared intent; attendance is not
delight; a dismissed notification is not a place dislike. Domain evidence
should remain distinct even when later judgment can combine it.

### 4.5 Verification continuity

The team can prove the loop at the appropriate layers, with evidence bound to
the code, fixture, product contract, device, and environment that produced it.
A July visual pass cannot certify an August redesign. A retry pass is not the
same observation as a first-attempt pass.

### 4.6 Connective tissue versus AI connectivity

The answer is “both, plus canonical state.”

| Intervention | What it solves | What it does not solve |
| --- | --- | --- |
| Links, handoffs, and consistent navigation | Reachability and orientation. | Whether context and state remain the same. |
| AI access to Places, Trips, and actions | Interpretation and action breadth. | Whether the action is governed, idempotent, private, and durable. |
| Shared identifiers, revisions, receipts, and domain commands | State and causal continuity. | Whether the experience feels useful and legible. |
| Outcome and applicability policy | Compounding future usefulness. | Whether current UI paths actually work. |
| Layered certification | Repeatable confidence. | Novel product taste and emergent user needs. |

The product needs all five. “AI connected to everything” without governed
commands and receipts creates an agent-shaped source of inconsistency. “Pages
linked together” without context identity creates a navigable but forgetful
product.

## 5. Core user loops

The product should document and certify a small number of loops rather than a
large flat list of pages and features.

### 5.1 Loop A — Taste to trip

```text
notice/search/save a place
        ↓
ask Vesper about it or invoke Vesper in context
        ↓
Vesper relates it to the person, companions, moment, and possible trip
        ↓
create or enrich a trip through a governed proposal
        ↓
the accepted result is visible and durable in Trips
```

Key proof points:

- place identity survives the handoff;
- Vesper cites or explains the relevant evidence honestly;
- the user can correct or decline the interpretation;
- an accepted proposal changes the intended trip revision once;
- Trips and Places show coherent post-mutation state; and
- restart preserves the result.

### 5.2 Loop B — Trip judgment and change

```text
trip need, disruption, conflict, or opportunity
        ↓
Vesper assembles current Plan + people + place + route + time context
        ↓
one bounded proposal with audience and authority
        ↓
accept, correct, reject, or group decision
        ↓
canonical Plan revision
        ↓
Trips / map / Now / notifications / Vesper reconcile
```

Key proof points:

- stale revisions produce an explicit conflict/rebase path;
- retries or duplicate taps do not double-apply;
- private evidence is not leaked into group-facing explanation;
- notification and deep-link routing land at the correct scope; and
- the receipt identifies what changed without overstating why.

### 5.3 Loop C — Experience to future judgment

```text
trip or local occasion happens
        ↓
occurrence and lightweight reflection/outcome
        ↓
domain-specific evidence remains private, correctable, and scoped
        ↓
later applicability evaluation
        ↓
future Places/Vesper/Trips judgment is materially better
```

Key proof points:

- occurrence is separated from preference inference;
- “unknown” remains possible;
- correction and deletion propagate;
- relationship evidence uses the exact applicable roster and audience;
- later influence is explainable without revealing private source material.

### 5.4 Why these loops create stickiness

The desired stickiness is accumulated usefulness, not generic engagement:

- the product remembers stable preferences and hard constraints;
- it preserves the state of current decisions;
- it understands recurring companions and relationship-specific fit;
- it can resume unfinished work;
- accepted and corrected judgments improve subsequent suggestions; and
- Trips becomes a trustworthy operational record rather than a disposable AI
  answer.

Switching cost should emerge because the system has earned context and trust,
not because it manufactures notifications or friction.

## 6. Onboarding as one complete learning loop

Onboarding should not principally teach three tabs. It should deliver the first
closed-loop outcome quickly enough that the user learns the product model by
experience. This is a first-session design requirement, not the architecture's
first or controlling behavior loop.

A candidate first session:

1. Ask for one concrete seed: an upcoming trip, a saved place, or a travel idea.
2. Let Vesper interpret the seed rather than merely store it.
3. Produce one meaningful, inspectable artifact in Trips within minutes.
4. Make clear how Places supplied evidence and how Trips now owns the durable
   result.
5. Ask for one correction or constraint and visibly improve the result.
6. Establish a credible return trigger: a collaborator response, pending
   decision, status change, next planning step, or post-experience reflection.

The user should leave with this learned model:

> I give Vesper fragments; it turns them into a trip; accepted changes persist;
> my corrections and outcomes can make later judgment better.

Candidate onboarding measures:

- time to first useful Vesper interpretation;
- time to first durable Trips artifact;
- proportion of users who make or accept one correction;
- proportion who cross at least two roots as part of one job;
- proportion returning to an unresolved or newly advanced trip state;
- proposal acceptance/rejection/correction distribution; and
- whether the second occasion requires less restatement than the first.

## 7. From repetitive dogfood to loop engineering

Manual dogfood should remain, but its function should change.

### 7.1 Questions automation should absorb

- Can the user reach the flow?
- Did the expected UI state appear?
- Did the mutation persist?
- Did another surface reconcile?
- Did restart preserve it?
- Did auth, permission, keyboard, safe area, or deep linking break?
- Did the correct deterministic fixture load?
- Did the canonical database state change exactly once?

### 7.2 Questions manual dogfood should retain

- Was the interpretation surprisingly useful?
- Was Vesper’s intervention well timed?
- Did the product make the user feel understood without becoming invasive?
- Did the explanation create trust?
- Did the three surfaces feel like one product despite technical correctness?
- Would the user naturally return, and for what unresolved value?
- What new expectation should become a contract or test?

### 7.3 The desired learning cycle

```text
manual exploration finds a failure or opportunity
        ↓
classify objective and subjective components
        ↓
encode each objective component at the lowest suitable layer
        ↓
add or refine a canonical loop contract
        ↓
retain only the subjective or novel residue for later dogfood
```

This prevents the team from repeatedly spending human attention on known
reachability, persistence, or reconciliation failures.

## 8. Maestro explained as a data-science system

Maestro is black-box mobile UI automation. It drives a built application through
the operating system’s input and accessibility interfaces. It can tap, type,
swipe, scroll, follow deep links, handle some system UI, assert observable
states, and capture screenshots or recordings.

For a data scientist:

| Data-science concept | Maestro equivalent |
| --- | --- |
| Experimental protocol | YAML flow. |
| Controlled covariates | Seeded persona, fixture, frozen clock, device, OS, locale. |
| Intervention | Tap, type, swipe, deep link, permission choice. |
| Measurement instrument | Accessibility tree, visible text, stable `testID`. |
| Observable/test statistic | `assertVisible`, `assertNotVisible`, selected/enabled state, screenshot similarity. |
| Raw evidence | Screenshot, recording, hierarchy, command log, JUnit report. |
| Cohort/stratum | Flow tags such as `pr-smoke`, `journey-nightly`, `native-live`. |
| Synthetic evaluation | Mock adapter and seeded personas. |
| External validity | Backend-connected preview or dogfood lane. |
| Repeated trial | Retry—with the first-attempt result retained as a separate outcome. |

Maestro observes the presentation layer, not latent system truth.

### 8.1 What Maestro can prove

- a real app binary launches on a supported simulator/emulator;
- a user-visible path is reachable;
- controls can be operated through native input;
- expected visible state appears;
- navigation, keyboard, permissions, safe areas, scrolling, and modal behavior
  work on the tested runtime;
- a value is visibly consistent across screens when explicitly compared; and
- a screen is sufficiently similar to a reviewed baseline under controlled
  conditions.

### 8.2 What Maestro cannot prove by itself

- canonical Plan or database truth;
- idempotency, concurrency, or exact mutation semantics;
- privacy of hidden backend context;
- correctness of analytics or event delivery;
- whether an AI response used the right evidence;
- whether an answer is genuinely useful rather than merely visible;
- long-horizon learning applicability; or
- correctness across untested devices, accounts, locales, and backend states.

The appropriate evidence chain is:

```text
fixture/API setup
        ↓
Maestro device journey
        ↓
deterministic UI assertions
        ↓
API/database invariant verification
        ↓
Maestro cross-surface and restart verification
        ↓
pixel and calibrated product-quality review
```

Maestro owns the automated hands-and-eyes portion. It is not the system oracle
and should not be the primary AI judge.

## 9. Dated audit of the current Maestro estate

### 9.1 Audit boundary

The following is a point-in-time read-only audit performed on August 12, 2026.
The app repository was structurally inspected and non-mutating validation was
run. No product flow was executed during the audit because the local polish
doctor and flows can modify simulator storage and application state.

At the audit point:

- the workspace and both child repositories were initially clean and on their
  respective `main` branches;
- local Maestro `2.6.1`, Java 17, a booted iOS simulator, Metro, and the app were
  present;
- Maestro metadata validation passed for **320 flows**;
- structural validation passed for **320 flows, 8 configs, 320 unique names,
  and 10 package references**;
- semantic Maestro syntax validation passed; and
- the polish registry resolved **31 scenarios**.

These checks prove authoring and configuration integrity. They do not prove
that the app passed those flows on a device.

### 9.2 Inventory

The tags overlap; counts are not mutually exclusive.

| Lane/tag | Audited count | Intended role |
| --- | ---: | --- |
| `pr-smoke` | 10 | Fast deterministic pull-request surface. |
| `journey-nightly` | 59 | Broader journey regression. |
| `android-smoke` | 5 | Android-specific smoke. |
| `native-live` | 13 | Signed-in backend-connected device certification. |
| `polish-capture` | 173 | Deterministic surface capture and review inputs. |
| `visual-baseline` | 11 | Pixel-regression baselines. |
| `stability` | 29 | Route/state and continuity coverage. |
| `legacy-visual` | 24 | Historical/legacy surface evidence. |
| `quarantine` | 0 | Explicitly excluded known-unreliable flows. |

Command usage in the audited flows:

| Command | Flows using it | Total uses |
| --- | ---: | ---: |
| `takeScreenshot` | 289 | 773 |
| `assertScreenshot` | 11 | 21 |
| `assertVisible` | 130 | 444 |
| `assertNotVisible` | 84 | 164 |
| `tapOn` | 135 | 449 |
| `openLink` | 295 | 742 |
| `runFlow` | 65 | 85 |

No Maestro AI assertions or `--analyze` use were found. Most screenshots are
therefore evidence for a later review process, not automatic visual verdicts.

### 9.3 What is strong

- Separate PR, nightly, Android, live, polish, baseline, and stability configs
  are already exposed through
  [`travel-app/package.json`](../../travel-app/package.json).
- The direct runner standardizes Java resolution, disables analytics, emits
  JUnit and debug output, and stores run artifacts. See
  [`run-maestro.mjs`](../../travel-app/scripts/mobile-stability/run-maestro.mjs).
- The polish runner preflights the environment, seeds persona and frozen time,
  uses locks, runs single-persona flows independently, verifies declared
  screenshots, and produces manifests/verdict scaffolds and before/after
  receipts. See
  [`run-polish-qa.mjs`](../../travel-app/scripts/polish-qa/run-polish-qa.mjs).
- Flow metadata includes owner, lane, isolation, fixture, journey, and area,
  making the suite more governable than a typical flat E2E directory.
- Mock/live separation is explicit, and the live config is not included in PR
  smoke by default.

### 9.4 What is weak or stale

#### The blocking ontology does not fully match the current product

The app exposes Trips, Vesper, and Places, but the PR lane still includes a
flow that taps the visible **Discover** tab:

- [`05-discover.yaml`](../../travel-app/.maestro/05-discover.yaml)

Other PR-tagged flows still wait for Discover copy or use Atlas-era routes:

- [`24-journey-02-create-invite.yaml`](../../travel-app/.maestro/24-journey-02-create-invite.yaml)
- [`45-navigation-continuity.yaml`](../../travel-app/.maestro/45-navigation-continuity.yaml)
- [`68-journey-16-account-data-lifecycle.yaml`](../../travel-app/.maestro/68-journey-16-account-data-lifecycle.yaml)

Legacy compatibility deserves coverage, but it should not define the primary
three-tab certification lane.

#### Continuous device evidence is not operationally closed

The workspace contains a scheduled/manual local-simulator workflow and a
conditional Maestro Cloud PR workflow:

- [`visual-qa.yml`](../../.github/workflows/visual-qa.yml)
- [`visual-qa-cloud.yml`](../../.github/workflows/visual-qa-cloud.yml)

The Cloud job skips when its API key, project ID, or Expo token is absent. The
EAS PR workflow is still manual-only pending activation:

- [`maestro-pr.yml`](../../travel-app/.eas/workflows/maestro-pr.yml)

Recent run history examined during the audit contained build, Metro, driver,
and pre-Maestro failures. Local targeted device evidence existed, but there was
not a uniformly green, current, continuously executing critical lane. The
precise run state is time-sensitive and must be re-queried before planning.

#### Visual verdicts can become stale

Trips, Vesper, and Places had structured July verdicts, but the accepted design
authority and implementation continued changing in August. An old pass is not
evidence for a new surface. Verdict freshness must be derived from hashes and
contract/canon dependencies rather than from the presence of a committed pass
file.

#### Runtime artifacts need lifecycle management

The local `.maestro/runs` and mobile-stability audit directories had grown to
roughly 1.5 GB combined during inspection. These runtime artifacts were ignored
rather than tracked, which protects Git, but retention, indexing, and promotion
rules remain necessary so accepted evidence is preserved while disposable
captures are pruned.

## 10. Common failure modes and efficient countermeasures

### 10.1 A screenshot exists, therefore the feature passed

**Failure:** `takeScreenshot` proves only that a PNG was written.

**Countermeasure:** Separate capture, correctness, visual, and intent gates.
Require declared captures, deterministic state assertions, and current evidence
metadata before any qualitative judgment begins.

### 10.2 Visible success, incorrect backend state

**Failure:** The UI displays “applied” while the canonical Plan is unchanged,
double-mutated, stale, or private evidence was mishandled.

**Countermeasure:** Pair the Maestro action with a backend verifier keyed by
`loop_run_id`, expected revision, idempotency key, actor, audience, and command
receipt. Then make Maestro revisit Trips/Vesper/Places after reconciliation.

### 10.3 Mock confidence mistaken for system confidence

**Failure:** The mock adapter renders a complete state that the real HTTP,
loading, auth, SSE, cache, migration, or persistence path cannot produce.

**Countermeasure:** Run the same outcome contract in a mock UI lane and a small
real-stack lane. Treat their evidence as complementary, never interchangeable.

### 10.4 Retry converts flakiness into a pass

The polish runner retries a capture up to three times and retains attempt logs,
but its downstream result primarily records eventual capture success. A
fail/fail/pass sequence can therefore become `ok: true` without first-attempt
health being a first-class field.

**Countermeasure:** Use a three-state result:

```json
{
  "status": "flaky",
  "attempts": 3,
  "first_attempt_passed": false,
  "eventual_passed": true
}
```

Blocking certification should require first-attempt success over the selected
window. Retried success should help triage, not erase the signal.

### 10.5 Optional actions bypass the behavior under test

**Failure:** An optional tap fails, but a later generic screen assertion still
passes.

**Countermeasure:** Disallow `optional: true` in critical loops unless the
branch has an explicit compensating assertion proving which path occurred.

### 10.6 Brittle or semantically weak selectors

**Failure:** Coordinates, ambiguous text, or overly broad regular expressions
interact with the wrong element. Conversely, a stable ID can continue passing
even if user-facing language is misleading.

**Countermeasure:**

- use user-visible text when the language itself is contractual;
- use stable accessibility IDs for icons, dynamic/localized content, and
  disambiguation;
- use relational selectors when several elements share text;
- verify state such as `enabled`, `selected`, or `checked` before action; and
- reserve coordinates for unavoidable platform controls with a narrow owner.

### 10.7 Stale fixtures and concept drift

**Failure:** Tests faithfully certify Discover/Atlas-era behavior after product
navigation has moved to Places/You, or accepted screenshots predate a redesign.

**Countermeasure:** Bind flows and baselines to a product-contract version.
Changes to visible roots, canonical vocabulary, fixtures, or accepted design
authority invalidate dependent evidence automatically.

### 10.8 Shared database pollution and cross-test dependence

**Failure:** A previous run leaves rows, vectors, auth sessions, jobs, or cache
state that influence the next run. Cleanup scripts grow increasingly complex.

**Countermeasure:** Prefer create-and-destroy isolation over cleanup. Every
stateful suite gets a unique database or branch, test-run namespace, synthetic
identities, and TTL. Every flow remains independently runnable.

### 10.9 Infrastructure failure misclassified as product failure

**Failure:** Build, simulator boot, driver connection, Metro, seed, auth, API,
or assertion failures collapse into one red status.

**Countermeasure:** Record a stage taxonomy:

```text
build → device → install → driver → seed → auth → API readiness
      → navigation → product assertion → backend postcondition → visual review
```

Report rates and latency per stage. Product pass rate should not silently absorb
“test never reached the product.” Infrastructure health must still block a
claim of certification; it is not permission to mark the product green.

### 10.10 AI judge leniency and bias

**Failure:** An AI reviewer produces a generous holistic pass, overweights polish
or fluency, misses small but consequential defects, or rationalizes stale or
incomplete evidence.

**Countermeasure:** Treat the judge as a noisy annotator:

- deterministic gates run first and cannot be overridden;
- use a small human-labeled calibration set;
- measure false negatives, especially AI-pass/human-fail cases;
- randomize before/after ordering for comparative review;
- withhold release-stakes framing from the judge;
- require localized findings and evidence, not only a score;
- permit `uncertain` rather than forcing pass/fail;
- human-review every proposed P0/P1 and a stratified sample of passes; and
- recalibrate after model, prompt, rubric, or visual-canon changes.

### 10.11 Multi-user flows simulated as sequential single-user flows

**Failure:** Two roles are exercised sequentially in one account/device world,
so notification delivery, concurrent revision behavior, auth boundaries, and
true participant state are not tested.

**Countermeasure:** Reserve a small credentialed two-identity/two-device lane,
or combine one Maestro device with a controlled API actor. Do not label a
sequential persona switch as multi-device certification.

## 11. AI visual review: appropriate role and calibration

Visual automation has three distinct instruments:

1. **Capture:** evidence exists; no judgment.
2. **Pixel/perceptual comparison:** controlled change detection against a
   reviewed reference.
3. **AI critique:** probabilistic judgment of hierarchy, clarity, defects, or
   intent from screenshots and context.

The correct ordering is:

```text
capture completeness
        ↓
deterministic correctness
        ↓
pixel/perceptual regression where stable
        ↓
AI visual and product critique
        ↓
human calibration and escalation
```

Maestro’s own `assertWithAI` capability is documented as experimental and is
optional by default. The absence of Maestro AI assertions in the current suite
is therefore not a gap that needs immediate correction. The existing external
verdict protocol can remain the qualitative layer if it becomes freshness-bound
and calibrated.

Suggested calibration metrics:

- human/AI agreement by criterion and surface;
- AI false-negative rate;
- AI false-positive rate;
- disagreement severity distribution;
- repeated-judgment stability;
- pair-order consistency;
- calibration-set drift after model/prompt changes; and
- time and cost per reviewed capture.

The AI layer should initially be non-blocking. Blocking use should be limited
to narrow criteria that have demonstrated acceptable error rates against the
human gold set.

## 12. Environment strategy

“Maestro Cloud,” “cloud backend,” and “cloud database” are separate choices.
The execution environment should be selected according to the uncertainty a
test is meant to remove.

### 12.1 Three independent axes

| Axis | Choices |
| --- | --- |
| Device executor | Local simulator/emulator, CI-hosted simulator, EAS Maestro job, Maestro Cloud. |
| Application backend | In-app mock, local FastAPI, ephemeral preview FastAPI, shared dogfood, production. |
| Persistence/dependencies | Fixture memory/storage, disposable local Postgres/Qdrant, ephemeral cloud branch/namespace, shared cloud production. |

### 12.2 Recommended environment ladder

| Lane | Backend and data | Auth | AI/providers | Cadence | Gate |
| --- | --- | --- | --- | --- | --- |
| **PR UI smoke** | In-app mock and frozen fixtures. | Bypassed. | Fixed outputs. | Every relevant PR. | Blocking. |
| **Local real-stack integration** | Local FastAPI + disposable local Postgres + disposable/namespaced Qdrant. | Bypassed or controlled dev identity. | Stubbed/recorded. | Developer loop and relevant CI. | Blocking for touched contracts. |
| **Cloud loop certification** | Ephemeral preview API + isolated Neon branch + isolated Qdrant test namespace. | Clerk development/test instance. | Mostly stubbed/recorded. | Main/nightly; later selected PRs. | Blocking after reliability target. |
| **Real-AI canary** | Preview/staging isolated state. | Real test auth. | Real model and selected providers. | Nightly/pre-release. | Non-blocking until calibrated. |
| **Shared dogfood** | Existing Fly backend + shared cloud data. | Real auth. | Real. | Manual product use. | Informative, not CI write gate. |
| **Production smoke** | Production. | Dedicated synthetic identity. | Real only when tightly bounded. | Post-deploy. | Read-only/idempotent health gate. |

### 12.3 PR mock lane

The existing `e2e-test` build in
[`travel-app/eas.json`](../../travel-app/eas.json) correctly uses mock API and
skip-auth flags. This lane should prove UI reachability, edge-state rendering,
native behavior, and deterministic cross-surface presentation quickly.

It should contain only the current product-critical loops. Mock fixtures should
explicitly model delayed, error, unauthorized, stale-revision, and optimistic
reconciliation states instead of attempting to cause those conditions through
unreliable timing.

### 12.4 Local real-stack lane

The local substrate already includes Postgres/PostGIS and Qdrant through
[`travel-agent/docker-compose.yml`](../../travel-agent/docker-compose.yml), and
the workspace’s dogfood environment helper keeps local Postgres and local
Qdrant paired:

- [`scripts/dogfood-env.sh`](../../scripts/dogfood-env.sh)

The current Docker services use persistent volumes, and backend tests contain
substantial self-healing cleanup for leaked test records. For multi-request
Maestro flows, transaction rollback alone is insufficient because requests,
connections, and background work span transaction boundaries.

Preferred lifecycle:

1. create `vesper_e2e_<run_id>` in the local Postgres service;
2. apply Alembic migrations;
3. seed one versioned canonical scenario;
4. start FastAPI with that `DATABASE_URL` and a test-run identity;
5. run Maestro;
6. verify API/database postconditions;
7. delete the database; and
8. delete the matching Qdrant namespace/collection or tenant partition.

Use one database per suite, or per shard when flows run concurrently. This
keeps the process fast while making state disposal explicit.

### 12.5 Ephemeral cloud preview lane

This is the principal missing environment.

```text
managed simulator
        ↓
unique preview FastAPI deployment
        ↓
unique Neon branch derived from sanitized e2e-golden
        ↓
isolated Qdrant test namespace
        ↓
Clerk test identities
```

Recommended run lifecycle:

1. Create `test/<commit>-<run_id>` from a sanitized `e2e-golden` parent branch.
2. Apply the candidate migrations.
3. Seed synthetic users, trips, places, conversations, and expected revisions.
4. Allocate a Qdrant `test_run_id` partition or bounded test collection.
5. Deploy the exact backend commit against those dependencies.
6. build/configure the app against the preview HTTPS URL;
7. execute Maestro on the managed device;
8. run postcondition verification;
9. retain JUnit, logs, screenshots, hashes, and state receipts;
10. destroy the backend, DB branch, and vector namespace; and
11. apply a TTL so leaked resources self-expire.

The golden parent should contain only synthetic or sanitized data. It should
not be an unreviewed clone of production PII.

### 12.6 Authentication strategy

Use two explicit questions:

- **Does data/API behavior work?** Local `SKIP_AUTH=true` can answer this
  efficiently.
- **Does the real authenticated mobile boundary work?** A cloud lane must run
  with `SKIP_AUTH=false` and Clerk test identities.

At least one loop should exercise organizer, member, invitee, and privacy roles
with dedicated synthetic accounts. Do not reuse personal dogfood identities or
depend on a human’s cached device session.

### 12.7 AI/provider strategy

“Real backend” and “real AI” are separate treatment variables.

The blocking real-stack test should use real FastAPI, SSE, tool orchestration,
commands, Postgres, and receipts while replacing LLM/search/provider calls at
their adapter boundary with deterministic outputs. This isolates system wiring
and state correctness.

A smaller real-AI lane should measure:

- task completion and structural outcome;
- tool selection and grounded evidence use;
- latency and cost;
- refusal/failure modes;
- proposal acceptance/correction rubric; and
- semantic quality distribution.

It should not assert exact prose. Until enough observations exist, model/provider
variance should not turn every release into a flaky system test.

### 12.8 Shared dogfood and production

The existing remote profile explicitly targets shared production Postgres and
cloud Qdrant, with guarded write operations. It should remain a deliberate
manual dogfood environment, not a concurrent automated mutation target.

Do not run destructive account, membership, invitation, or trip-reset flows
against shared production data. Production automation should be read-only or
strictly idempotent, use a dedicated synthetic tenant, and have bounded cleanup
and alerting.

## 13. Proposed certification architecture

### 13.1 One outcome contract, several implementations

Each canonical loop should define:

- fixture version and initial state;
- actor, audience, auth, and privacy boundary;
- user action sequence;
- visible UI expectations;
- canonical backend postconditions;
- idempotency and stale-revision expectations;
- cross-surface reconciliation expectations;
- restart/persistence expectation;
- analytics/receipt expectations;
- qualitative review dimensions; and
- environment applicability.

The same outcome contract can then produce:

- unit and property tests for domain rules;
- Postgres/Qdrant integration tests;
- API scenario tests;
- mock Maestro UI flows;
- preview Maestro full-loop flows; and
- visual-review capture scenarios.

This is the connective tissue between product management and engineering: the
user loop becomes an executable, layered contract rather than prose detached
from tests.

### 13.2 Evidence hierarchy

| Evidence | Can certify |
| --- | --- |
| Static/type/unit | Local logic, types, invariants. |
| Integration/contract | Real schema, API, DB, command, privacy, and projection behavior. |
| Maestro mock | Device-level UI behavior under controlled synthetic state. |
| Maestro preview + postcondition | Real mobile/network/auth/state loop. |
| Pixel/perceptual baseline | Controlled visual regression. |
| AI critique | Probable clarity, hierarchy, polish, and intent defects. |
| Manual dogfood | Novelty, timing, usefulness, trust, and taste. |

No higher layer should be used as a substitute for a cheaper, more deterministic
lower-layer assertion.

### 13.3 Evidence receipt schema

Every promoted run should bind at least:

```yaml
loop_id: taste-to-trip
contract_version: 3
workspace_sha: ...
app_sha: ...
backend_sha: ...
flow_sha: ...
fixture_version: ...
design_canon_hash: ...
environment: e2e-preview
backend_url_identity: ...
database_branch_id: ...
qdrant_namespace: ...
device_model: ...
device_os: ...
maestro_version: ...
first_attempt_passed: true
attempts: 1
ui_assertions_passed: true
backend_postconditions_passed: true
cross_surface_reconciliation_passed: true
visual_review_status: pass | fail | uncertain | not_run
generated_at: ...
```

A result becomes stale when any declared dependency changes. “Passed once” is
not a timeless property of a surface.

## 14. Product and engineering documentation model

The workspace should avoid replacing scattered feature docs with one new
permanent monolith. Instead, this working note should seed four bounded durable
artifacts if the recommendations are accepted.

### 14.1 Product object model

Define canonical nouns and their authority:

- Person and identity;
- Relationship and travel party;
- Place and place signal;
- Trip;
- Plan and revision;
- Proposal and command;
- commitment/booking;
- Conversation;
- Memory/preference evidence;
- Moment/occurrence; and
- Outcome.

For each: canonical owner, derived projections, identifiers, audience rules,
and reconciliation precedence.

### 14.2 Feature registry

Every substantial feature should record:

- user job;
- owning root or secondary surface;
- loop contribution;
- lifecycle: shipped, dark, internal, legacy, retiring, or retired;
- governing flag and owner;
- backend/frontend implementation references;
- entry and exit seams;
- current certification and evidence freshness; and
- criterion for promotion or removal.

Dark features should be documented without becoming visible product vocabulary.

### 14.3 Canonical loop registry

Start with Taste-to-Trip, Trip Judgment/Change, and Experience-to-Future-
Judgment. Give each one owner, contract version, supported environments,
required evidence, and current status.

### 14.4 Environment and evidence contract

Promote the accepted environment ladder, isolation rules, result taxonomy, and
receipt schema into a durable reliability contract/runbook. This working note
should then expire rather than compete with it.

## 15. Prioritized execution plan

### Phase 0 — Decide and reduce

1. Accept or revise the one-sentence thesis and three-root responsibilities.
2. Declare the current visible vocabulary and classify Discover/Atlas as legacy
   navigation owners where appropriate.
3. Select the first canonical loop to certify. Recommended: **Places → Vesper
   proposal → Trips durable result**.
4. Freeze expansion of the blocking Maestro lane until its purpose is current.

### Phase 1 — Make the mock lane honest

1. Replace stale Discover/Atlas assumptions in `pr-smoke` with 4–6 current
   three-root loop flows.
2. Move legacy deep-link checks to a compatibility/nightly lane.
3. Remove or justify optional commands and coordinate selectors in the critical
   subset.
4. Add first-attempt/flaky/failed result semantics to the runner and manifest.
5. Bind visual verdicts to current contract and canon hashes.
6. Restore one continuously green device executor before expanding flow count.

### Phase 2 — Add deterministic state truth

1. Define the first loop outcome contract.
2. Add `loop_run_id`, expected revision, actor, audience, and command receipt.
3. Implement the backend postcondition verifier.
4. Add cross-tab reconciliation and app-restart assertions.
5. Create disposable local Postgres database and Qdrant namespace orchestration.
6. Run the same contract through mock UI and local real stack.

### Phase 3 — Add production-like isolated execution

1. Create sanitized `e2e-golden` Postgres data.
2. Provision per-run Neon branches with TTL.
3. Add an isolated Qdrant test namespace strategy.
4. Deploy an ephemeral preview backend for the exact candidate commit.
5. Add Clerk test identities and session automation.
6. Execute the selected Maestro loop on a managed simulator.
7. Promote only complete, hash-bound evidence receipts.

### Phase 4 — Calibrate qualitative automation

1. Build a small human-labeled screenshot and response corpus.
2. Score current AI verdict behavior for false negatives and instability.
3. Narrow rubrics to criteria the judge can reliably observe.
4. Add `uncertain` and escalation paths.
5. Keep AI review non-blocking until the measured error profile warrants a
   narrow gate.

### Phase 5 — Redesign onboarding and measure stickiness

1. Make onboarding execute Loop A once.
2. Instrument first durable value and cross-root progression.
3. Measure correction, proposal, reconciliation, and return behavior.
4. Use failure distributions to simplify copy, surface ownership, and handoffs.
5. Add new features only when they strengthen context acquisition, durable
   conversion, or compounding future usefulness.

## 16. Proposed operating metrics

### Product loop metrics

- time to first useful interpretation;
- time to first durable value;
- percentage completing a cross-root loop;
- proposal accept/correct/reject rates;
- loop abandonment stage;
- successful resume after interruption/restart;
- second-occasion reduction in user restatement;
- return driven by an unresolved or advanced trip state; and
- correction/deletion propagation success.

### Certification health metrics

- first-attempt pass rate;
- eventual pass rate;
- flake rate;
- P50/P90 duration;
- infrastructure-versus-product failure distribution;
- stale-evidence count;
- optional and coordinate selector count in critical flows;
- percentage of critical mutations with backend postconditions;
- percentage of promoted receipts with complete hashes; and
- artifact storage and retention by lane.

### AI judge metrics

- human/AI agreement;
- false-negative and false-positive rates;
- uncertainty/escalation rate;
- repeated-judgment stability;
- pair-order consistency;
- disagreement by criterion and surface; and
- review time/cost saved after human calibration overhead.

## 17. Decisions still required

This document recommends but does not decide:

1. the exact one-sentence product thesis to promote into canon;
2. whether the three proposed loops are the canonical v1 loop registry;
3. which feature-registry owner adjudicates shipped/dark/legacy/retired status;
4. whether EAS managed Maestro or Maestro Cloud should be the primary managed
   device executor;
5. whether Neon branching should be adopted for ephemeral E2E state;
6. the isolation scheme for Qdrant test data;
7. the first-attempt reliability threshold required before a device lane blocks;
8. the human gold-set size and AI-judge error threshold; and
9. the initial onboarding value and return-trigger experiment.

## 18. Research basis

The research reviewed for this synthesis supports the following conclusions:

- Maestro is an arm’s-length, accessibility-driven black-box device automation
  framework with declarative flows and automatic settling:
  [How Maestro works](https://docs.maestro.dev/get-started/how-maestro-works).
- Flows should be independent and runnable from reset state:
  [Sequential execution](https://docs.maestro.dev/maestro-flows/workspace-management/sequential-execution).
- Visible text, stable IDs, relational selectors, and state-aware selectors have
  different measurement roles:
  [Maestro selector guidance](https://docs.maestro.dev/api-reference/selectors).
- Broad retries can hide real application flakiness:
  [Maestro retry guidance](https://docs.maestro.dev/reference/commands-available/retry).
- Expo distinguishes first-attempt passes, flaky retry passes, and failures and
  reports flow-level flake rate and P90 duration:
  [Expo Maestro Insights](https://docs.expo.dev/eas-insights/maestro/).
- EAS supports built mobile artifacts, tags, sharding, retries, recording, and
  PR-triggered Maestro workflows:
  [EAS E2E with Maestro](https://docs.expo.dev/eas/workflows/examples/e2e-tests/)
  and
  [EAS workflow syntax](https://docs.expo.dev/eas/workflows/syntax/).
- Maestro AI assertions are experimental and optional by default:
  [assertWithAI](https://docs.maestro.dev/api-reference/commands/assertwithai).
- End-to-end tests offer high user-level confidence but are slower and more
  failure-prone, so vital paths should be selected deliberately:
  [React Native testing overview](https://reactnative.dev/docs/0.73/testing-overview).
- Hermetic environments reduce common sources of test flakiness:
  [Google testing flakiness analysis](https://testing.googleblog.com/2020/12/test-flakiness-one-of-main-challenges.html).
- Neon supports isolated, copy-on-write database branches for CI/test runs,
  including branch lifecycle automation:
  [Neon branching workflow](https://neon.com/docs/get-started-with-neon/workflow-primer).
- Schema-only branches can avoid copying sensitive production data into test
  environments:
  [Neon schema-only branches](https://neon.com/blog/instant-branches-schema-only-or-with-data-the-choice-is-yours).
- Qdrant recommends payload-based tenant separation rather than unbounded
  collection proliferation:
  [Qdrant multitenancy](https://qdrant.tech/documentation/tutorials/multiple-partitions/).
- Clerk documents test identities, sessions, fixed OTP strategies, and Testing
  Tokens for automated E2E:
  [Clerk testing](https://clerk.com/docs/guides/development/testing/overview).
- LLM judges exhibit systematic biases and require calibration against human
  judgments rather than uncritical use:
  [Position-bias study](https://arxiv.org/abs/2406.07791) and
  [human–LLM judgment calibration](https://openreview.net/forum?id=bEP87LNTfX).

## 19. Exit and promotion plan

Before the expiration date, choose exactly one disposition for each durable
conclusion:

1. **Product thesis and three-root responsibilities:** promote into the existing
   product canon or record a superseding product decision.
2. **Feature lifecycle inventory:** merge into the governed feature registry,
   not a new hand-maintained duplicate list.
3. **Canonical loops and outcome contracts:** register in the journey/loop
   system and make their status executable.
4. **Maestro lane roles and result taxonomy:** promote into the mobile
   reliability contract and runner schema.
5. **Environment ladder and isolation:** promote into a cross-repo E2E runbook
   after one local-disposable and one ephemeral-preview proof.
6. **AI judge calibration:** promote only the measured protocol and thresholds;
   archive speculative recommendations.
7. **Point-in-time audit details:** archive as dated evidence or delete after
   generated current status supersedes them.

If none of these promotions are accepted, archive this note as a historical
discussion synthesis. Do not leave it active as a competing permanent source
of product or reliability truth.
