---
doc_type: working
status: active
owner: product / backend / frontend
created: 2026-09-04
last_verified: 2026-09-04
expires: 2026-10-04
why_new: Replans entity work from the implemented September 4 baseline into evidence-gated completion, integration, and separately approved expansion.
supersedes: []
---

# Entity roadmap: trustworthy objects, useful continuity

## 1. Outcome and scope

An entity should remain recognizable across Vesper while its facts, the
viewer’s relationship, and current circumstances change. The page is a reader
and doorway into those systems, not their replacement.

The next milestone is an internally usable, source-honest object experience
with demonstrated continuity and repair. It is not a larger directory.

This is a proposed roadmap, not authorization to implement, deploy, run paid
research, enable flags, schedule jobs, or backfill data. No catalog, narrative,
photo, hours, embedding, or identity backfill is included. Test-only fixtures
may be created in an isolated test database during later authorized execution;
they are not production seed data.

This roadmap sequences the remaining work in the [September 3 entity
program](entity-system-next-program-2026-09-03.md), rather than restarting its
already implemented phases. That program retains its detailed architectural
contracts; the [execution log](entity-system-execution-log-2026-09-03.md)
retains historical implementation evidence. Product decisions below remain
proposals until accepted. Conflicting historical statements must be reconciled
in Phase 0, not silently treated as superseded canon.

## 2. Baseline and evidence limits

Inspected local `main` on September 4 (after the continuation receipts below):

- Backend: `9f3d80959` — research gating, persistence hardening and the
  read-only entity health report.
- Mobile entity baseline: `d3b22275b` — canonical mock envelopes for all known experiences,
  guarded venue/site/experience journeys, focused shared-renderer
  state-contract coverage, and Dynamic Type/accessibility governance fixes
  (the preceding route/action implementation is `35c110f47`).
- Workspace: `61f46d4` — roadmap, runbook, native receipt and post-fix
  accessibility evidence are committed locally.

These are local source baselines, not deployment or public-release evidence.
No database job, provider call, canary, or backfill was run to write this
roadmap. Native captures are recorded in the linked receipt; earlier passing
checks remain in the execution log.

| Layer | Existing implementation to preserve | Remaining evidence or work |
| --- | --- | --- |
| Identity | Canonical refs, external identities, private provisional shells, redirects and alias-aware reads | Cross-entry and cross-owner identity/repair certification |
| Relationship | Save, Plan, personal attendance and private outcome projection; bounded page readback | Two-user later-read proof, correction and retraction across consumers |
| Situation | Separate no-store contextual read and expiry handling | Foreground/background, context-change and stale-action certification |
| Object UI | Guarded shared renderer on venue, site and experience routes; default venue route still retains its compatibility composition; mock and local-real-backend identity/verb slices are native-evidenced for all three kinds; all known mock experience envelopes are canonical; sparse/capability/stale unit cases are locked; post-fix iOS accessibility-medium pass and static governance are recorded | Full state-matrix acceptance, including auth diversity, write/readback, sparse/unavailable/photo/offline/process-restart, VoiceOver, Android and other platform evidence |
| Research | Read-only persisted brief; explicit gated queue request; idempotency and rate controls | End-to-end job state, artifact readiness, provenance, freshness and retry closure |
| People | Bounded authorized exact-place lines and gated addressed-handoff doorway | Grant/revocation and recipient experience proof; richer inline people citations remain separate |
| Operations | Read-only entity-health counts | Queue age, artifact mismatch, repair evidence, operational ownership and rollout receipt |

Accommodation has backend presentation/research support but is intentionally
outside the current rebuilt-page migration. Backend support does not imply
native route support. Neighbourhood and person-made spot design states likewise
must not be counted as shipped from fixture vocabulary alone.

## 3. Architectural and product constraints

1. `EntityRef` is app identity; provider IDs are mappings, not the authority for
   personal history. Do not introduce a universal entity/event table.
2. Public facts, authored research, private outcomes, addressed words and live
   context keep their respective owners, provenance, audience and lifecycle.
3. A base page read performs no model call, research enqueue, provider lookup,
   personal-memory write or automatic promotion of a provisional shell.
4. Keep, Plan, occurrence, liking and meaning never imply one another.
5. A shared occurrence can coexist with different private outcomes.
6. Missing or stale evidence yields absence, a qualified historical statement,
   or an honest unavailable state—not generated filler or an action promise.
7. Actions go through existing owners and read back their accepted result.
8. Correction, withdrawal and revocation invalidate dependent use, not just
   the currently visible card; independently supported facts remain intact.
9. Provider rights are field- and purpose-specific. This roadmap does not
   establish current Google or other provider licensing permissions. Verify
   applicable official terms before changing integrations or retention.
10. Internal page, research and relationship-handoff flags remain independent.

These constraints follow the [Product Model](../../travel-agent/docs/product/Product%20Model.md)
and [Contribution and Consequence contract](../systems/contribution-and-consequence.md).

## 4. Delivery map

| Phase | Outcome | Depends on | Relative effort | Exit evidence |
| --- | --- | --- | --- | --- |
| 0 | One current contract and evidence ledger | Baseline inspection | Small | Decisions and route/capability inventory |
| 1 | A working continuity and repair path | 0 | Large | PostgreSQL-backed two-user journey and consumer assertions |
| 2 | Honest asynchronous research | 0; existing queue | Medium–large | Request → artifact → page success/failure/recovery tests |
| 3 | Explicit freshness and bounded live context | 0; integrate with 1/2 | Medium | Clock-controlled lifecycle and provider-budget tests |
| 4 | Native object experience acceptance | 1 and core part of 3; 2 only if research is enabled | Medium | Current-SHA captures, real-backend journeys and accessibility verdict |
| 5 | Bounded internal operation | 1, 3, 4; each optional capability’s own gate | Medium | Release manifest, monitors, owner and rollback rehearsal |
| 6 | Useful later transfer into the app | 1; pilot after 5 | Large, owner-dependent | Later Occasion benefit and correct withholding proof |
| Later | Expand entity kinds, content and coverage | Explicit decisions after evidence | Unestimated | Separate approved scope and quality/cost gates |

Effort is comparative, not a calendar commitment. Phase 0 should convert the
remaining uncertainty into estimates. Phases 2 and 3 can proceed independently
of continuity work once interfaces and ownership are agreed; they need not
hold the core page hostage. A research-disabled internal page can pass Phase 4.

## 5. Phase 0 — Reconcile contracts and make readiness explicit

### Deliverables

- Add a concise current-state section to the entity program and handoff. Label
  every capability as implemented, tested, native-evidenced, enabled, or
  deferred; attach commit/test/run references separately.
- Resolve the handoff’s historical “opening queues research” statement against
  its later explicit `Read up` sequence. Recommendation: retain explicit
  request, no spend on GET, and no silent refresh on opening.
- Update the fixture-contract audit: some entries predate people-lines and
  addressed-handoff implementation. Preserve historical findings but distinguish
  now-supported wire fields from still-design-only concepts.
- Inventory actual entry points, route kinds, flags and action owners. Record
  accommodation’s intentional exclusion rather than filing it as a regression.
- Identify an existing venue, site and experience for internal read-only
  rehearsal; create independent equivalent fixtures only in the test lane.
- Inventory active work before editing shared surfaces. The entity lane owns
  entity adapters and object pages, not Home/Places contribution generation,
  universal memory admission, or relationship delivery infrastructure.

### Exit gate

There is one approved answer for research trigger, sparse-page behavior,
supported entity kinds, permitted verbs and each release gate. No document
claims native acceptance or lifecycle closure solely from code existence.

## 6. Phase 1 — Prove continuity and causal repair

### 1A. Identity across entry points

- Characterize Search, Map, Places, Chat artifact, Plan and saved-place opening
  through the existing resolution and routing helpers. Assert a canonical ref
  and exact return context, not equality of every surface’s wording.
- Cover public identity, owner-private shell, ambiguous provider match,
  alias chain, merge target, deleted/unavailable source and reverse merge.
- A second viewer must not discover or promote the first viewer’s private
  shell merely by requesting its identifier or provider mapping.

### 1B. One differentiated later read

Use the real owner APIs and PostgreSQL joins for this test sequence:

1. Two authorized test users open the same existing place from different roots.
2. A keeps it. B remains unsaved; neither is marked visited or affectionate.
3. A adds it through the existing Plan owner, not a new object-page trip ladder.
4. Record a supported shared occurrence with participant-specific attendance.
   First include a non-attendee case; then a case where both attended.
5. A and B voluntarily record different private outcomes through the existing
   owner. No mandatory review prompt or inferred outcome is introduced.
6. Reopen the object and the relevant Life/Plan/Places reads. Each outcome is
   visible only to its authorized viewer; public facts remain shared.
7. A corrects and retracts their outcome. B’s outcome and independently
   supported occurrence remain unchanged.

### 1C. Repair matrix

Build on existing identity, outcome, relationship and lived-experience tests;
do not invent a second lifecycle engine. For each event, identify actual active
consumers and their invalidation/recompute mechanism:

| Event | Must change | Must remain independent |
| --- | --- | --- |
| Unsave | Viewer save state and saved-place projections | Plan, occurrence and outcome |
| Correct/retract outcome | Viewer readback and eligible derived use | Another participant’s outcome and occurrence truth |
| Merge/reverse merge | Canonical routing and alias-aware evidence reads | Original authorship and historical subject records |
| Source deletion | Dependent claims and reusable content become unavailable | Independently owned identity and commitments |
| Handoff revocation | Recipient’s future display and cached projection | Sender’s private original under its custody policy |
| Situation expiry | Current advice and affected action capability | Durable place identity and personal history |

Test stale mounted screens, account switch, logout, backgrounding, process
restart, duplicate commands and intervening writes before reversal. Late
responses from a previous account/entity must not populate the current view.

### Exit gate

The complete deterministic journey passes against a disposable PostgreSQL
database. Receipts identify owner-accepted changes; dependent active
projections agree after repair. Tests include negative privacy assertions and
cache behavior, not only expected response shape. Any unsupported consumer is
explicitly excluded and gated, not counted as certified.

## 7. Phase 2 — Close research as an asynchronous product capability

The core implementation slice is now landed and locally tested: a viewer-safe
status read, explicit gated request, source-bearing brief artifact, expiry/
stale detection, idempotent replay, page-readable completion gate, atomic
claiming, abandoned-lease recovery, and fail-closed budget/concurrency
controls. The remaining work is certification against the full failure matrix
and an owner-approved canary; it is not permission to turn on paid research or
backfill entities.

### 2A. Status and request contract

- The public-facing state is implemented separately from internal queue
  statuses: absent, queued, running, ready, stale, failed, unavailable. Keep a
  client polling timeout as “status unknown/check again,” not proof of worker
  failure, and certify that mapping in the native matrix.
- The additive status read resolves the canonical ref and current viewer
  eligibility on every read. Certify that it never exposes another requester’s
  identity, raw prompts, queue metadata or provider errors.
- Stable job/result identity, safe failure classification and bounded timing
  are now part of the response; verify active-job discoverability and dedupe
  under concurrent authorized reads.
- Transport retry reuses the same idempotency key. A deliberate new attempt
  after terminal failure uses a new key and rechecks eligibility and budget.
  Scope client state to account plus canonical entity; reset it on changes.
- Use the existing queue. Any shared-model or schema change needs the
  repository-required approval before implementation; prefer derived status
  over a new job table.

### 2B. Artifact success and provenance

- The worker completion gate now traces request → queue claim → persistence →
  brief GET → mobile and requires the request’s valid readable artifact, not
  merely an older dossier. Certify this with an inspected end-to-end artifact.
- Certify text, generation/as-of time, source records and paragraph-source
  references as one consistent version. Never leave old citation mappings
  attached to new text or infer citations from paragraph position.
- Test venue, site and accommodation write targets independently. Experience
  and provisional-shell requests remain ineligible in this slice.
- Retain sparse legacy briefs without fabricated attribution. Define when a
  newly generated uncited or quality-held artifact is ineligible for serving.
- Audit the legacy writeback gate. Do not solve readiness by globally enabling
  a broad writer; use an approved narrow path or keep requests disabled.

### 2C. Mobile reconciliation

- The mobile reducer renders pending, ready, failed, unavailable and
  polling-paused states from one explicit model; certify pending-copy clearing
  when the artifact is ready.
- Resume status reads after foreground/remount without enqueueing new work.
  Stop timers on unmount/account change and ignore stale responses.
- Offer an explicit retry only for eligible terminal states; distinguish a
  status recheck from a new paid request. Offline attempts perform no mutation.
- Keep old usable content during refresh, labeled with its age; never replace
  it with blank content because a refresh failed.

### 2D. Cost, concurrency and failure tests

- PostgreSQL concurrency tests now cover at-most-one active job for a
  canonical entity; extend the evidence to different accounts/keys and merge
  aliases in the canary rehearsal.
- Test worker crash/retry, missing artifact, quality hold, provider failure,
  disabled persistence, rate-limit exhaustion and budget-store unavailability.
- Establish an explicit fail-closed posture for paid requests when budget
  enforcement cannot be trusted; do not assume an in-process limiter suffices
  across instances. Add a global cost/concurrency cap as well as per-user gates.
- Fake providers/models cover the ordinary test suite. A paid internal canary
  is a separate approved operation with a named budget and result inspection.

### Exit gate

A user can request, leave, return, see completion or honest failure, and retry
without duplicate spend. The displayed brief is the artifact the job produced,
with correct sources. No GET queues work. Research remains off until these
checks and the operational canary are accepted.

## 8. Phase 3 — Publish a freshness and retention matrix

Reuse `backend/places/cache.py`, `linker.py`, `proactive_refresh.py` and existing
refresh/purge scripts. The Known Gaps Register O-14 already describes this
substrate; verify scheduler deployment rather than treating documented scripts
as proof of running operations. Do not create an entity-specific competing
cache or activate schedules as part of planning.

| Data | Persistence and authority | Refresh/invalidation trigger | Stale/absent display |
| --- | --- | --- | --- |
| Identity and canonical redirects | Durable identity owner, provenance-bound mappings | Explicit resolution, correction and reviewed merge | Retain identity; qualify uncertainty; do not guess a match |
| Stable descriptive facts | Licensed catalog/source owner with observation metadata | Source change or that owner’s configured freshness policy | Show attributed historical fact only where appropriate |
| Hours, closure and operational status | Existing provider cache; rights-specific retention | Existing field TTL and approved relevant-Plan refresh | Remove unsupported “open now”/availability promises |
| Editorial research | Public-source brief artifact, separately versioned | Explicit request when absent/stale; approved future refresh policy | Dated content or absence; not an eternally fresh claim |
| Saved/planned/attended/outcome relationship | Existing private/domain owners | Owner mutation, audience change and alias revision | Authoritative readback; no new inference from interaction |
| Addressed words and people byline | Relationship owner and grant | Edit, expiry, block or revocation | Omit unauthorized material; do not serve stale private content |
| Route/current situation | Request-scoped, no-store for precise context | Origin/mode/Plan/Moment change, foreground and expiry | Silence or unavailable state; durable page remains usable |
| Photos | Source custody and licensed display capability | Source deletion, rights change or URL expiry | Photograph or nothing, with required attribution |

Tasks:

1. Inventory actual configured TTLs and distinguish content freshness from HTTP
   cache freshness. Preserve existing field defaults until evidence supports a
   change. Recompute time-derived predicates such as “open now” at boundaries.
2. The current descriptive-brief default is 30 days via
   `ENTITY_RESEARCH_BRIEF_TTL_SECONDS`; treat that as a pilot policy to inspect
   and revise, not as a universal freshness guarantee. Exclude volatile
   hours/availability from it.
3. Keep `already_fresh` bound to eligible artifact freshness, not row presence;
   retention may outlive eligibility to influence current advice.
4. Exercise expiry while mounted, offline, backgrounded and across local-day,
   timezone and DST changes. Invalidate changed origin/mode/Plan inputs.
5. Audit provider field storage, attribution and deletion against current
   official policies before rollout. Do not infer permissions from old comments.

Exit: every shown current claim has an owner, observation/as-of and an expiry
rule; expired claims lose their practical authority. Unknown freshness must
not produce confident “today” advice. Revoked private content has no stale
grace period.

## 9. Phase 4 — Certify the native object experience

Keep the current shared venue/site/experience scope. Use generated API models,
the `data/` bridge, real-shaped mocks and existing action owners.

Acceptance states:

- Known rich place; sparse identity-only place; owner-private provisional;
  ambiguous resolution; redirect; unavailable/deleted source.
- Photo present, absent, failed and unauthorized; correct attribution.
- Saved/unsaved, planned, personally attended, private verdict and retracted
  verdict; different authenticated viewers.
- Situation fresh/expired/absent and changed route context.
- Research absent/pending/ready/stale/failed when enabled; none of its verbs or
  promises when disabled.
- Authorized addressed line, revoked line, and relationship feature disabled.
- Exact return to each origin, nested sheets, Android back, offline/reconnect,
  account change, process death, large text and screen-reader navigation.

Use the registered `places` QA surface and extend its scenarios where needed.
Follow the app’s design-reference, doctor, capture, comparison and structured
verdict workflow. Capture the actual rebuilt route with flag values, current
source SHA, installed binary/build, data mode and scenario IDs in the manifest.
A legacy-page screenshot, design fixture, harness dry run or TypeScript pass
cannot substitute for native evidence. Record platform limitations explicitly.

Exit: accepted captures and functional journeys on the intended release
platforms, with accessibility checks and no unsupported verbs or fake content.
The venue/site/experience flag-on Keep/Ask slices and focused unit suite are
intermediate receipts, not this exit: real-backend, accessibility, platform,
and full state-matrix evidence remain open. The core page may pass with
research/handoff disabled; enabling either requires the corresponding states
to pass separately.

## 10. Phase 5 — Operate a bounded internal pilot

Deliver a release manifest, not merely another feature flag:

- Exact backend/mobile revisions and deployed build; enabled capabilities,
  allowed accounts, entity kinds and test sample.
- Worker/writeback/provider readiness, named operational owner and approved
  cost ceiling for any research canary.
- Content-free health signals: resolution errors, duplicate conflicts,
  projection latency/error, queue age, retries/failures, completed-job/missing-
  artifact mismatches, stale claims suppressed and invalid source references.
- Cost and cache hit/miss signals only through approved aggregate telemetry;
  do not log private outcomes, addressed prose, precise origin or credentials.
- Tested independent disable paths for research, handoffs and rebuilt pages.
  Disabling requests must stop new admission; document what happens to already
  running jobs. UI rollback does not imply destructive database rollback.

Proposed hard blockers: any unauthorized disclosure, wrong-person outcome,
false current claim, duplicate paid job for one active canonical request,
uncorrectable active projection, or completion without a readable artifact.
These require zero observed failures in the acceptance suite. Record sample
sizes; zero observed errors is not proof of zero production risk.

Set latency, queue-age and cost thresholds after baseline measurement, before
enabling the pilot. Use explicitly opted-in accounts and a small set of existing
places. No new recurring scheduler or public rollout is authorized here.

Exit: owner-reviewed pilot receipt with metrics, inspected examples, residual
risks and rehearsed rollback. Public expansion is a separate decision.

## 11. Phase 6 — Carry useful evidence into later experience

Begin with one named consumer and one later Occasion, not simultaneous root
redesigns. Phase 1 proves correct storage/readback; this phase proves useful
future application and appropriate non-application.

1. Reuse the lived-experience provider and governed outcome/source reads.
2. Agree with the receiving owner on evidence shape, allowed purpose, audience,
   contextual eligibility, revision dependencies and repair behavior.
3. Demonstrate a later choice improved by an explicit prior outcome, using a
   paired comparison without that evidence. A changed sentence alone is not
   proof of useful continuity.
4. Include changed circumstances, contrary newer evidence, weak relevance,
   revoked permission and another participant’s private outcome. Withhold
   evidence when it is not authorized or useful; do not freeze taste.
5. Provide inspectable evidence and an owner-routed correction path. Correcting
   the original must change the later recommendation/projection, not just the
   original object page.

Integration ownership:

| Receiver | Entity lane supplies | Receiver continues to own |
| --- | --- | --- |
| Search/Map/Places | Canonical ref, supported facts and authorized relationship read | Retrieval, map behavior and surface composition |
| Chat | Entity context and valid action doorway | Gesture resolution, answer/no-write behavior and conversational receipts |
| Plan/Occasion | Identity, relationship and bounded situation | Commitment, attendance and participant authority |
| Life | Evidence-linked place relationship and correction target | Durable navigation and source/outcome repair controls |
| Home | Authorized contextual evidence through an agreed adapter | Selection, urgency, contribution admission and rendering |
| Experience Graph | Canonical binding and governed evidence dependency | Graph admission and later use |
| Relationships | Exact entity reference and sender doorway | Consent, audience, recipient delivery and revocation |

Do not edit `backend/root_projection/v2/source_contribution_*`, Home/Places
unit unions or their contribution producer as an incidental entity change.
Confirm active ownership before touching any receiving system. If integration
needs broader owner work, make that dependency explicit instead of bypassing it.

Exit: a later experience benefits in a way a cold catalog cannot reproduce,
and the same mechanism correctly withholds or withdraws evidence in the
negative cases. Include an immediate-use/no-Plan case too: this lifecycle is a
proof, not a mandatory funnel for every person or place.

## 12. Later expansion — separate decisions, not hidden deliverables

### A. Complete additional kinds and design capabilities

- Accommodation migration only after its booking/Stay owner and object-page
  scope are approved; preserve kind-specific commitments and source policies.
- Person-made spots, neighbourhood entities and provisional promotion need
  explicit ownership, identity/dedupe and audience rules.
- Rich inline people citations, source/mark sheets and optional dossier
  composition need contract and design acceptance, not synthetic fixture fields.

### B. Improve useful context

- Extend live situation only for demonstrated user jobs; do not accumulate
  ambient location or build a generic real-time place database.
- Revisit descriptive research quality and refresh cadence using inspected
  outputs and measured cost. Do not increase generation to fill empty space.

### C. Coverage/identity seeding, only if later approved

Prepare a separate proposal for one bounded geography and selected kinds:
licensed source inventory, field allowlist, source provenance, candidate-only
dry run, dedupe quality sample, review thresholds, rollback and incremental
change policy. Keep identity seeding distinct from facts/photos/research
enrichment. Measure unresolved useful clicks and false merges before deciding
whether more rows are the best intervention. This roadmap runs no backfill.

## 13. Execution packages and validation

Suggested reviewable packages, not permission to execute:

| Package | Primary scope | Dependency / review condition |
| --- | --- | --- |
| E0 | Workspace contract reconciliation and readiness ledger | Product decisions recorded |
| E1 | Backend cross-owner journey/repair characterization | Isolated PostgreSQL fixture lane |
| E2 | Backend relationship/identity fixes exposed by E1 | No speculative owner rewrite |
| E3 | Mobile canonical routing/cache/receipt fixes | E1/E2 contracts stable |
| E4 | Backend research status and artifact-success contract | Shared-model approval if needed |
| E5 | Research provenance, persistence and concurrency tests | E4; legacy writer boundary approved |
| E6 | Mobile research state machine and recovery tests | E4/E5; generated types synchronized |
| E7 | Freshness matrix and existing-cache integration | Agreed field policy; no scheduler activation |
| E8 | Native state matrix, captures and verdict | E3/E7; E6 only if research enabled |
| E9 | Internal pilot runbook, health checks and rollback | E8 plus each enabled capability gate |
| E10 | One later-consumer integration and withholding eval | Owner agreement; E1/E3 continuity proof |

For each later implementation package:

1. Check branches/status and task-intake requirements in each affected repo.
   Use descriptive `codex/` branches/worktrees for isolation when appropriate.
2. Add focused regression tests, API/privacy tests and real PostgreSQL tests
   for DB-dependent behavior. Run repository-required backend validation;
   report environmental exclusions rather than calling mocks integration proof.
3. For backend route/model changes, run workspace `./scripts/sync-types.sh`,
   review both OpenAPI snapshots and mobile generated types, then run
   `make contract-check` and the API governance checks for operation changes.
4. Run mobile hook/component/route tests, typecheck and touched-file formatting.
   Require native evidence for surface acceptance using the existing QA lane.
5. Add one evidence receipt: exact revisions, commands/results, fixtures,
   flags, screenshots when applicable, known gaps and rollback.
6. When committing is authorized, stage explicit filenames separately in each
   repository. Never sweep concurrent work into a commit. Record the linked
   cross-repo commit group before declaring the package complete.

## 14. Immediate recommendation and decisions

E0/E1 and the first E4–E10 implementation slices are now landed and locally
validated. The next work should stay evidence-gated:

1. Extend E8 from the now-passed local-real-backend identity/verb slice into
   the complete auth and accessibility/platform state matrix across venue,
   site, and experience. Add sparse, unavailable, photo, account, offline,
   large-text, and process-restart cases before treating the shared renderer
   as release-ready. Keep research and addressed handoffs disabled in the
   core-page verdict until their own states are evidenced.
2. Prepare E9’s owner-reviewed pilot receipt: exact deployed revisions,
   enabled capabilities, thresholds, cost ceiling, health report and rollback.
   Do not enable a flag or scheduler as part of this documentation step.
3. Close the remaining E1/E2 repair inventory for stale mounted screens,
   account changes, merge/retraction/deletion and handoff revocation, then
   re-run the affected consumer proofs.
4. Only after those gates, choose one named E10 receiving experience for a
   second transfer proof. Treat accommodation, spots, neighbourhoods and any
   coverage/backfill as separate product decisions.

Decisions to accept before the relevant execution boundary:

- Explicit `Read up`, never research-on-open, for this release.
- Venue/site/experience as current rebuilt-page scope; accommodation and spots
  remain separate expansion decisions.
- Sparse internal page may advance with research and handoffs disabled.
- Artifact success, source completeness and proposed brief freshness policy.
- Any shared schema/model, prompt or provider integration changes required by
  implementation, per repository rules.
- Pilot audience, supported platforms, cost budget and operational owner.
- Which single later consumer owns the first transfer proof.

The roadmap is successful when an existing place supports immediate value,
truthful personal continuity, authorized multiplayer differences, live honesty
and causal repair—without needing a larger catalog to make the demo work.

## 15. Execution ledger — 2026-09-04 continuation

Completed implementation packages in this lane:

| Package | Evidence | Commit(s) |
| --- | --- | --- |
| E1 | PostgreSQL two-member continuity test: shared occurrence/identity remains equal while private verdicts differ by viewer | `travel-agent:b1f5a9fcf` |
| E4 | Viewer-safe lifecycle endpoint; completed status requires a readable brief; experience/provisional requests remain unavailable; expired artifacts report stale/retryable | `travel-agent:4f018f2f0`, `fb38e24f1` |
| E5 | Explicit source metadata write-back; stale idempotency replay refresh; page-artifact worker gate; fail-closed global budget, atomic queue claim and abandoned-lease recovery | `travel-agent:e9d89fc0d`, `350e5f931`, `5eee43f31`, `f2a6d846a`, `83583a42d`, `0bd02d8da`, `97ee0019f`, `ea940a044` |
| E6 | Generated mobile status contract; centralized research state reducer; stale content age label; status-error recovery copy and tests; stable locale metadata formatting; stale-age preservation during unknown status | `travel-app:9904f3411`, `9abfc997d`, `462d56a0d`, `ce504cfa9`, `71f154151`, `a3636e13c` |
| Contract | OpenAPI snapshots, active projection, generated schema, identity seams and schema bridge are synchronized | `workspace:93ea30e` |
| E8 (native default-route slice) | Current mobile build passes venue identity/save/private-handoff, registered Places capture, and explicit plan-placement review/commit on iPhone 16 Pro in the mock lane; the default venue route is flag-off, so shared `ObjectPageRebuild` acceptance remains open. The rebuild intentionally omits the legacy Add-to-trip ladder per the Places contract. | `travel-app:47735f406`, `travel-app:35c110f47`, [native QA receipt](entity-native-qa-receipt-2026-09-04.md) |
| E8 (native guarded-renderer slice) | Flag-on venue, site, and experience routes pass on the iPhone 16 Pro mock lane with canonical `Cervejaria Ramiro` / `Museu Nacional do Azulejo` / `LUX Fragil Closing Night`, `Keep place`, visible Ask handoffs, and explicit assertions that the legacy Add-to-trip ladder is absent. Focused renderer tests also lock sparse, owner-private capability denial, and stale research states; all known mock experience IDs resolve to canonical names. The three journeys pass at iOS `accessibility-medium` text size on the post-fix source, and static accessibility governance passes. This proves the intended shared renderer identity/verb contract and one enlarged-text check; full native state-matrix evidence remains open. | `travel-app:7b4d0601b`, `travel-app:6e3fe8545`, `travel-app:464e7da98`, `travel-app:377c8a4b5`, `travel-app:ea10e4482`, `travel-app:dba1e16e9`, `travel-app:d3b22275b`, [native QA receipt](entity-native-qa-receipt-2026-09-04.md) |
| E8 (native local-real read slice) | With all API background workers disabled, the guarded venue/site/experience routes also pass against a temporary FastAPI process backed by native PostgreSQL, using existing rows and real HTTP presentation reads. Each preserves canonical identity, `Keep place`, visible `Ask Vesper`, and absence of the legacy Add-to-trip ladder. This closes the real-read portion of E8 only; no auth diversity, mutation, research, or repair claim is implied. | `travel-app:89367c36e`, `travel-agent:e33dd4764`, [native QA receipt](entity-native-qa-receipt-2026-09-04.md) |
| E10 (later-consumer slice) | Real PostgreSQL second-occasion loop closure changes candidate choice from a prior explicit outcome, then reopens after correction and withholds on changed roster/occasion; chat attachment snapshots remain catalog-only | `travel-agent:18b71b9f7`, `422a5f6c8` |
| E9 (health receipt) | Read-only, content-free entity health report now includes queue age, retry/lease, duplicate-active, and completed-without-fresh-brief integrity metrics | `travel-agent:9f3d80959` |

Validation recorded for this continuation:

- `make contract-check` passes (577 snapshot paths, 442 active-mobile paths,
  367 facade exports classified).
- Backend focused entity/research suites pass, including the live PostgreSQL
  relationship continuity test and queue lifecycle tests.
- A second native-Postgres follow-up pass covering entity presentation,
  private-entity contracts, people-line gating, relationship handoffs and
  outcome feedback passed 66 tests. The current mobile entity
  screen/renderer/projection set passed 78 tests; these strengthen deterministic
  privacy/repair evidence but do not substitute for two-account device or
  platform acceptance.
- The complete entity-focused backend selection (API, Places, core/database
  identity, research queue and health report) passed 177 tests with 2 recorded
  dogfood-wedge skips requiring an explicitly seeded Lisbon corpus. This is a
  code-level gate, not evidence of a production catalog or rollout.
- The no-background local API returned honest `404` responses for an unknown
  site across public and authenticated presentation routes. The corresponding
  cleared-state Maestro flow remained at the Expo development-server picker,
  so native unavailable/process-restart acceptance is intentionally still open.
- The read-only health report at `2026-09-05T00:41:29Z` found zero stale
  claims, duplicate-active jobs, expired leases or completed-without-fresh-
  brief mismatches, alongside one old pending venue research row and one
  pending resolution review. Those rows were not changed; E9 must assign their
  disposition before any research canary.
- The real PostgreSQL second-occasion loop-closure proof passes independently
  with the repository virtualenv (`.venv/bin/pytest
  tests/scenarios/test_micro_journey_loop_closure.py -q`: 5 passed). It
  demonstrates a later decision changing from a prior `good_once` outcome,
  reopening after correction, and withholding under changed roster/occasion
  conditions. The ambient Homebrew pytest lacks the optional `openai` package
  needed only while constructing that full HTTP scenario harness, so that
  runner mismatch is recorded rather than treated as a product failure.
- Mobile TypeScript, schema bridge and object-page projection tests pass.
- The mobile test TypeScript project passes (`npm run
  test:typecheck:contracts`); API boundary and schema-bridge CI checks also
  pass (`npm run api-boundaries`, `npm run schema-bridge`).
- The focused mobile shared-renderer state suite passes
  (`__tests__/components/places/ObjectPageRebuild.test.tsx`: 3 tests),
  covering sparse body absence, capability/owner-private withholding, and
  stale research age plus explicit refresh. The four touched screen/mock
  suites pass 69 tests; TypeScript completes cleanly.
- `npm run accessibility-governance` passes after removing the rebuilt
  renderer’s Dynamic Type opt-outs; the three guarded journeys were rerun at
  iOS `accessibility-medium` on `travel-app:d3b22275b` and passed.
- The touched mobile files also pass the date-locale convention test after
  replacing implicit device-locale formatting with the app's stable `en-US`
  locale (`travel-app:71f154151`).
- The read-only entity health report regression passes and remains content-free
  (`travel-agent:9f3d80959`); it reports anomaly counts without repair,
  refresh, provider calls, or backfill.
- Full offline aggregate runs are not a release pass: the backend aggregate
  still reports the pre-existing refresh-memory/Postgres-leak and dead-Atlas-
  handler failures; the frontend aggregate still reports 24 unrelated
  convention/navigation/history fixture failures. These are recorded as
  validation exclusions, not silently attributed to the entity changes.
- Native Maestro runs initially found two QA-lane prerequisites (Metro
  reachability and a persisted real-API override). After those were corrected
  without changing product flags, the current mobile SHA passed
  `.maestro/54b-journey-07-venue-context.yaml` end-to-end in the mock lane
  with the object-page rebuild flag off (the default venue compatibility
  composition).
  The registered `polish/places.yaml` capture also passed after its stale
  Plans-shell assertion was corrected. The follow-up
  `.maestro/54c-journey-07-venue-plan-outcome.yaml` flow also passed through
  explicit trip/day selection, review, commit, and affected-plan return after
  sequencing the iOS modal transitions. The scoped result is recorded in the
  [native QA receipt](entity-native-qa-receipt-2026-09-04.md); it covers the
  mock-lane identity/save/private-handoff, Places default, and one explicit
  placement path, not the guarded flag-on `ObjectPageRebuild` path, complete
  real-backend, or accessibility state matrix.
  Production canary and any backfill remain intentionally outstanding; no
  flag was enabled and no catalog row was backfilled.
- The guarded venue/site/experience renderer was subsequently run twice
  against a temporary local FastAPI process backed by native PostgreSQL (not
  the mock adapter). The clean rerun disabled all API background workers; all
  three existing local rows passed the same identity/verb assertions. Exact
  IDs, revisions, screenshots and logs are recorded in the [native QA
  receipt](entity-native-qa-receipt-2026-09-04.md). This closes only the
  real-read portion of E8; auth diversity, mutations/readback, repair,
  offline/process restart, VoiceOver, Android and the full state matrix remain
  open.
- A bounded venue process-restart flow (stop, relaunch, and reopen the same
  deep link) passed against the same no-background local backend. Cleared-state
  cold start remains blocked by the Expo development-client picker, while the
  product-level restart path is now evidenced in the native receipt.

The next unclosed gates are the broader native state matrix (auth-diverse
real-backend journeys, sparse/unavailable/photo/account states, VoiceOver, Android and
platform verdict),
a reviewed pilot receipt, and explicit operational ownership. The
later-consumer benefit/withholding proof is now present in the real PostgreSQL
loop-closure scenario, but it is not a production rollout receipt. These remain
release gates, not reasons to enlarge the catalog now.
