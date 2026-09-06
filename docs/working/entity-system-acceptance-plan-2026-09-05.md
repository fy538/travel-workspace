---
doc_type: working
status: active
owner: product / backend / mobile
created: 2026-09-05
last_verified: 2026-09-06
expires: 2026-10-05
why_new: Converts the implemented entity roadmap into bounded correctness, native acceptance, and independently gated pilot packages without restarting the architecture or authorizing backfill.
supersedes: []
depends_on:
  - docs/working/entity-roadmap-2026-09-04.md
  - docs/working/entity-pilot-release-manifest-2026-09-05.md
  - docs/systems/contribution-and-consequence.md
---

# Entity system: implementation closure and acceptance plan

## September 6 current assignment

This remains the scoped C0–C8 execution detail; the September 4 entity roadmap
is background direction, not a second pending repair queue. The latest landed
app/backend fixes (`fce56e1cb`, `dda170a09`, represented in current main history)
address public-share lifetime, canonical cross-kind actions, research request
correlation/retries, readable-generation refresh, people expiry/custody/grants
and duplicate legacy reads. Do not repeat those fixes from an older checklist.
The later venue hook-order repair also landed in the shared app history.

**Next work is targeted receiving-lane closure, not entity expansion.** Accept
an exact Home/Places/Life entry, return, research-generation or withdrawal case;
reproduce it on current code; fix only the owning entity boundary; hand back
the typed ref/readback and regression. The existing focused tests are evidence,
not a new run or an enabled-capability verdict.

Core pages, research and people retain separate acceptance/activation gates.
Full native/platform and operational acceptance remain future work; the founder
has deferred app/device tests for current engineering. Preserve those gates,
but do not make them block disjoint code work or start a new native session by
default. No additional entity kinds, catalog backfill, paid research, queue
activation or Home/Places root redesign is included.

The [coordination register](complete-system-integration-roadmap-2026-09-05.md#2-current-coordination-register--september-6)
names current receiving owners. Older environment/test failures in receipts are
dated evidence and must be reproduced before becoming a current blocker. Core
data coverage or private-social availability cannot be inferred from a flag-off
smoke run or a passing transport-envelope test.

## 1. Outcome and authority

Finish a dependable entity experience for **venue, site, and experience** using
existing entities: open the correct object, understand what is known, take an
explicit action, see its authoritative result later, and correct or withdraw
the relevant evidence without corrupting another person's view.

This is the execution detail for the existing [entity roadmap](entity-roadmap-2026-09-04.md),
not a replacement architecture. The earlier execution log and receipts remain
historical evidence; their test counts and SHAs are not current-build approval.

The planning turn itself authorized no implementation, deployment, flag
enablement, research spend, provider calls, scheduled work, production writes,
or backfill. The later user instruction to execute this plan authorized the
scoped implementation and isolated verification packages below. Operational
enablement still stops at the explicit owner/budget/build gates in section 10.

### Three independently accepted capabilities

| Gate | What must work | What may stay disabled |
| --- | --- | --- |
| Core page | Canonical reads, sparse/rich pages, safe public sharing, Keep/Ask, authorized relationship readback, freshness, navigation and repair | Research requests and addressed people features |
| Research | Explicit request through worker to sourced readable artifact, correct retry/recovery and bounded operation | People features; no automatic refresh scheduler |
| People | Exact-place recipient projection, current authorization, expiry, withdrawal and two-account device behavior | Richer social actions and people cited inside prose |

All scoped code packages can be completed while capabilities remain off by
default. Native tests may enable the relevant flag only in their isolated test
build and must record and restore that configuration. Core acceptance does not
implicitly approve either optional capability.

### Non-goals

- No catalog, identity, opinion, photo, hours, embedding, or narrative backfill.
- No new entity taxonomy, universal table, identity provider, or cache system.
- No accommodation frontend migration, neighborhood/container page, person-made
  spot admission, shell promotion, or additional entity-family expansion.
- No generic Add-to-trip ladder on the rebuilt page; no new Tonight? workflow.
- No generated prose on page open, autonomous research, provider booking, or
  live-data scheduler activation.
- No new USEFUL/KEEP/REPLY social actions, inferred attendance, or inferred taste.
- No Home, Places root, Life, Chat, or Plan redesign as an incidental entity fix.

## 2. Verified starting point and work ownership

Inspected local `main` during planning:

| Repository | Source baseline | Relevant changes already included |
| --- | --- | --- |
| `travel-app` | `bbb597442` | C1–C5 route/share/freshness/research/people implementation and lifecycle/cache guards; concurrent Places/booking work remains separate |
| `travel-agent` | `120c34b31` | C5 people validity/custody read path and PostgreSQL owner-continuity proof; concurrent Life/Places work remains separate |
| workspace | `4b3705c` | Existing roadmap/runbook/pilot records plus the execution receipt and synchronized API snapshots |

Both child working trees were clean at this inspection. The workspace had
unrelated Plan/design decision and handoff edits; preserve them. These are
source baselines, not pushed/deployed/configuration claims. Re-read status and
branches immediately before implementation and before every commit.

The Places result-set integration has now landed. Preserve
`result_set_id`/revision and the existing return-context helpers in all three
detail routes; do not implement a second return-state mechanism.

### Ownership fence

| Surface | Entity package may do | Separate owner retains |
| --- | --- | --- |
| Identity | Use canonical refs and test redirects/visibility | Resolution, dedupe, merge and promotion decisions |
| Places/Map/Search | Verify canonical opening and exact return | Result-set scope, search, map composition and root navigation |
| Chat | Preserve typed entity context and test Ask boundary | Conversation authority, streaming, memory admission and receipts |
| Plan/Occasion | Read/verify relationship and explicit context | Placement, commitments, attendance and participant authority |
| Life | Verify reads and repair of linked evidence | Source/outcome mutation, indexing and continuity surfaces |
| Relationships | Consume/test bounded people projection | Pair membership, custody, permissions and withdrawal transitions |
| Provider/research | Verify existing field/artifact contracts | Licensing, provider execution, budgets and worker operation |

Do not edit `backend/root_projection/v2/source_contribution_*`, root unit
unions, Life indexing, or arrangement authorities without a specific receiving
owner agreement. Cross-owner failures become narrow owner tickets with a
reproduction; they are not permission to rewrite those systems.

## 3. Package C0 — Reconcile acceptance authority and baseline

**Risk:** documentation and verification planning. **Dependency:** none.

1. Reconcile the older build brief with the current surface contract. It still
   contains a proposed enqueue-on-open endpoint despite the explicit-tap ruling,
   broader entity families, fixed tiny-label scaling instructions, and actions
   that remain intentionally gated. Mark those passages historical/proposed;
   do not treat them as implementation instructions.
2. Record a capability/evidence matrix with source SHA, installed build, flags,
   backend/data mode, account class, test commands, result and exclusions.
3. Confirm the existing isolated PostgreSQL and native test lanes before any
   writes. Test fixtures belong only in a disposable test database. Existing
   development or production catalog rows must not be mutated to fabricate states.
4. Classify mobile lifecycle/data work as `parity-sensitive`; response changes
   as backend `contract-sensitive`. No prompt or model-registry change is planned.
5. Find the canonical design export. The historical
   `/Users/feihuyan/Downloads/vesper-entity-object-handoff-lab` path is currently
   absent, and `travel-app/docs/surfaces/entity-object/` has only the contract.
   Request the approved export if necessary. Behavioral work can continue;
   pixel-level acceptance cannot be claimed without references or an explicit
   design-owner decision adopting a new reference baseline.

**Exit:** one current scope/evidence ledger; no stale document can silently
expand research triggers, family scope, accessibility exceptions or rollout.

## 4. Core correctness packages

### C1 — Make public sharing public by construction

**Risk:** privacy-sensitive frontend parity. **Dependency:** C0.

The current venue route constructs its public share message from
`entityPresentationV2.take.headline`. The backend can return a personal Take;
governed private content can also carry a `curator` tier. A tier label is not
proof of public reuse permission.

Implementation:

- Introduce a small pure public-share payload builder, initially allowlisting
  only public canonical identity/name and its canonical public URL. Do not
  feed authenticated Take text, private relationship, trip labels or people
  notes into the external share path. A richer blurb needs an explicitly public
  projection, not a tier check or string scrubber.
- Audit venue, site and experience sharing for the same boundary. Preserve the
  correct kind-specific supported public destination; do not invent URLs.
- Check public eligibility both when opening the sheet and when executing its
  action. Close/reset a pending share sheet on viewer/entity/capability change.
- Keep owner-private shells unshareable; no empty public preview masquerading
  as a supported action. Copy link, native Share and preview must describe the
  same public object, without implying that displayed private prose is included.

Likely files: `travel-app/app/venue/[venueId]/index.tsx`, the site/experience
routes, `components/external-share/PlaceShareOwnerSheet.tsx`, and a pure helper
under `utils/`. Inspect existing public-preview APIs before adding any contract.

Tests: a recognizable secret in personal and private-governed Take headlines
never reaches `Share.share`; absent public metadata; provisional shell;
same-kind alias; route/account replacement with a sheet open; loss of share
eligibility before tap; Copy/Share/Preview parity. Assert payloads, not only
that a button is hidden.

**Exit:** external payloads contain only explicitly public material in every
tested rebuilt and compatibility route.

### C2 — Make the canonical v2 read own the rebuilt route

**Risk:** frontend parity and integration. **Dependency:** C0; coordinate with C1.

- Inventory every request fired by each route when rebuild is on/off. The
  venue currently still asks for legacy presentation/detail and exact-photo
  data alongside v2. Disable unnecessary legacy-only queries with explicit
  hook inputs; preserve React hook ordering and the flag-off behavior.
- Use the returned **full `{type, id}`** for Keep, Ask, photo contribution,
  research and people reads. Do not combine a canonical id with a hardcoded
  route kind or coerce an unsupported id into a number. If cross-kind redirects
  are supported, use the existing canonical route dispatcher; otherwise return
  the established explicit unsupported/unavailable result.
- Keep sparse/owner-private v2 success independent of public legacy 404s.
  Distinguish missing objects from transport/authentication failures.
- Audit page-open network effects, including auxiliary media/map hooks. The
  current contract forbids provider lookup on ordinary open. Retain permitted
  existing media reads where allowed; move lookup behind the approved explicit
  action or omit it. Do not build a generalized photo service in this package.
- Preserve the newly landed Places result-set identity, map position and
  return context through these changes. No root navigation refactor.

Likely files: all three detail routes; `data/entities.ts`; existing venue/media
data bridge; `utils/routes.ts` and `utils/placesMapReturn.ts` only for a verified
integration defect; existing typed Ask/photo helpers.

Tests: flag-on route tests with actual v2 data for all three kinds; rich/sparse;
private shell with legacy 404; retryable v2 failure; alias then Keep/Ask; invalid
id; account/route replacement; precise return identity; flag-off regressions.
Spy on network/command boundaries to prove no read-triggered research, model,
provider lookup or personal-memory mutation.

**Exit:** v2 governs the rebuilt page and its actions, without duplicate legacy
authority, wrong-target actions, hidden generation or return-context loss.

### C3 — Enforce freshness while the page remains open

**Risk:** frontend parity; backend only if a demonstrated contract gap requires it.
**Dependency:** C2.

- Reuse/extend the existing expiry pattern in `hooks/useUnexpiredValue.ts`.
  Expiry must re-evaluate while mounted and on foreground, not only when an
  unrelated render happens. Research currently checks its expiry at render time.
- Separate retained historical content from permission to claim something is
  current. Expired descriptive research may remain dated; expired route,
  open-now, availability or time-sensitive action advice loses current authority.
- Keep dated stale research legible even when the request flag is off. Only a
  known active request may say it is refreshing. Missing/invalid freshness
  evidence must not produce a confident current claim.
- Scope revalidation to the entity hooks/screen. Do not flip the application's
  global `refetchOnWindowFocus` policy to solve one page.
- Refresh or withhold affected viewer state on foreground, account change,
  Plan/context change and owner mutation. Distinguish public offline reading
  from private projection eligibility; C5 owns the stricter people rules.
- Reuse existing provider cache/field policy. Inventory actual configured TTLs,
  source attribution and precedence when `status.hours` and legacy tail fields
  disagree; do not invent a universal entity TTL or activate a scheduler.

Likely files: `components/places/ObjectPageRebuild.tsx`,
`components/places/objectPageProjection.ts`, `data/entities.ts`, expiry hooks,
`backend/places/entity_situation.py` and existing fact mappers if a test exposes
an incorrect read. No provider policy change by inference from an old comment.

Tests: fake-clock expiry without network traffic; background past expiry then
resume; offline/reconnect; clock/time-zone boundaries; stale brief with research
flag off; route/Plan replacement; invalid timestamps; dated content retained
while current advice and dependent actions disappear.

**Exit:** each current claim has an owner and effective validity rule, and
expiry changes the visible page without requiring navigation away.

## 5. C4 — Close research request-to-artifact lifecycle

**Risk:** mobile parity; existing backend contract/worker correctness.
**Dependencies:** C0 and C3 before final integration acceptance.

Preserve the recent backend fix: pending/running jobs remain authoritative even
when an older brief exists or a new brief is written before worker completion.
Do not reimplement a queue or infer completion from an HTTP success alone.

Implementation:

1. Correlate a POST receipt to GET status using the existing `entity_ref` and
   `request_id`, plus client request lifetime and observation ordering. The
   current projector receives only the POST status string, so it cannot prove
   that cached terminal status has observed the new request. Do not assume
   numeric IDs are ordered without the backend contract establishing that.
2. Keep an old ready/stale/absent snapshot from dismissing a newly queued
   request. Accept terminal state only for the relevant request or a confirmed
   superseding observation. Refetch the artifact on relevant ready transition
   and verify the displayed generation matches the server's ready metadata.
3. Distinguish transport retry of the same attempt from an explicit retry after
   server-confirmed failure. The former keeps its idempotency key; the latter
   rotates on the first deliberate retry, including failure learned by polling
   rather than an `already_failed` POST response.
4. Keep polling bounded and pause on inactive/offline screens. Exhaustion is
   unknown/last-observed status, not invented failure or eternal refreshing.
   Offer a status recheck without creating another job. Remount/restart reads
   existing state; it does not resubmit automatically.
5. Preserve account/entity/sequence guards, including A→B→A transitions and
   overlapping responses. Scope all invalidations to the original owner/ref.
6. Exercise worker claim, retry, quality hold and readable-artifact validation
   with fake provider/model adapters and isolated PostgreSQL fixtures.

Files: mobile research hooks in `data/entities.ts`, `ObjectPageRebuild.tsx`,
`objectPageProjection.ts`; backend `api/routes/entities.py`,
`core/db/entity_research.py`, `core/db/content/_review_queue.py`, and
`research_agent/tasks/process_research_queue.py` only as needed by failures.
The existing request/status wire fields should be sufficient initially; any
necessary new shared field requires the contract review/sync workflow.

Required cases: absent→queued→running→ready; stale brief during refresh; brief
written before job completion; old ready response racing a new queued receipt;
failed job then one-tap deliberate retry; transport timeout after admission;
duplicate taps; two viewers requesting the same public canonical object; alias;
missing or older artifact; source mappings; poll exhaustion/reconnect/restart;
flag-off, rate-limit and ineligible experience/private-shell requests.

**Exit:** a fake-worker end-to-end journey proves one admitted active job,
correct sourced artifact and honest lifecycle/recovery. A paid quality/cost
canary remains a separate operational approval.

## 6. C5 — Make people visibility expire and withdraw safely

**Risk:** privacy and shared response contract. **Dependency:** C0; integrate C2/C3.

Current response lines have `made_at` but no visibility deadline. The client
refetches every 60 seconds and on entry/reconnect. That is useful revalidation,
not strict expiry or immediate remote withdrawal. Durable handoff events exist;
that alone does not prove a client invalidation transport exists.

### Implemented contract; enablement still requires owner decision

- Add server-evaluated projection validity metadata (for example `evaluated_at`
  and `valid_until`) and effective line expiry where needed to
  `EntityPeopleLinesResponse` / `EntityPeopleLine`. Use existing handoff/grant
  truth; no new durable permission table is proposed.
- Derive validity from the earliest applicable permission/source deadline and
  a short revalidation lease. **Proposed maximum lease: 60 seconds**, subject
  to relationship/privacy-owner acceptance; it must not extend an earlier
  expiry. Do not call the lease proof that permission cannot change meanwhile.
- Recheck current recipient, pair/source eligibility, handoff status, naming
  precision and canonical binding under the relationship owner's rules. Reuse
  its authorization helpers; do not authorize solely from a cached graph link.
- Never expose raw conversation/source identifiers, hidden counts, rejected
  text or other recipients through the projection or its errors.

### Client behavior

- Gate display on viewer, canonical ref, successful validation and unexpired
  validity metadata. Missing/invalid validity metadata fails closed for this
  gated client. Handle delayed responses and clock skew conservatively.
- Remove visible lines on expiry, offline transition, background/route blur,
  authorization error, account change or an observed owner withdrawal. On
  foreground/reconnect, validate before showing private text again.
- Invalidate through existing relationship mutation/event integration when
  available. Remove the active sheet and any avatar/citation when its line loses
  eligibility. Old responses cannot resurrect a revoked or replaced projection.
- Ensure query persistence/rehydration cannot restore unvalidated private
  text; evict affected viewer caches on logout. Keep this scoped to these data.

### Remote revocation is an explicit release decision

Local/observed revocation can hide content immediately. Scheduled expiry can
be enforced locally. Unobserved cross-device revocation cannot be instantaneous
under polling. Before enabling people features, either prove an existing owner
invalidation channel and its reconnect behavior or have the privacy owner
explicitly approve the bounded visibility lease. If neither is acceptable,
keep the people capability off; core-page acceptance can still finish.

Files: `backend/core/models/entity_people.py`, `backend/api/routes/entities.py`,
`backend/domains/relationships/repository.py`; generated OpenAPI/app types;
`travel-app/data/entities.ts`, relevant relationship mutation bridge,
`components/places/PeopleLineSheet.tsx` and `ObjectPageRebuild.tsx`.

Tests: true PostgreSQL read before/after revoke, block, source withdrawal,
pair/recipient ineligibility, precision narrowing and expiry; fake-clock
mounted expiry; A→B and A→B→A; selected sheet revocation; stale response arrival;
offline/background/reconnect/process rehydration; old server response without
validity fields; two authenticated devices/accounts with recorded timing.

**Exit:** contract and client behavior match a documented privacy consistency
bound, with negative tests and two-account evidence. No immediate-revocation
claim is made from a polling-only implementation.

## 7. C6 — Prove continuity across the actual owning systems

**Risk:** cross-repo parity/integration. **Dependencies:** C1–C3; C4/C5 only for
the corresponding optional journey.

Extend existing relationship/repair and
`tests/scenarios/test_micro_journey_loop_closure.py` coverage. Do not build a
second continuity harness or merely repeat its already-passing assertions.

| Journey | Required evidence |
| --- | --- |
| Immediate value, no Plan | Open known/sparse place from a supported entry, read, Ask and return; no save/attendance/personal-memory write implied by reading or asking |
| Keep and release | Keep once, read back on page and the existing Saved/Places consumer, remount/restart, then Unsave; attendance/outcomes remain unchanged |
| Plan boundary | From the existing Plan-owned workflow, place the exact entity; entity reads planned state; cancel/remove via the owner and watch dependent reads repair |
| Plural outcomes | Isolated supported occurrence with two participants; same place/occurrence, independently authored outcomes; neither viewer sees the other's private verdict |
| Correction and later use | A prior outcome changes an existing later-decision test; correction/withdrawal removes only its dependent influence, preserving independent evidence |
| Entry/return parity | Search, Places list/map, Saved and supported Plan/Chat/Life entry routes retain canonical identity and their established return context |

Use a minimal fixture set: rich venue, sparse site, supported experience,
same-kind alias, owner-private provisional shell, missing entity, and two test
accounts. Cross-kind alias gets a fixture only if it is a supported contract.
Do not insert those states into a live catalog. Real-account native proof must
use actual authenticated principals; `SKIP_AUTH=true` is not auth-diversity proof.

For mounted stale views, test mutation→owner read→dependent query invalidation
→render, not only the database row. A typed Chat seed is not proof of the
downstream no-write behavior; exercise it in the existing cheap integration
lane. If current owner code fails, isolate and coordinate its bounded fix.

**Exit:** both positive and withholding/repair paths work across the chosen
existing consumers. Record unsupported entry routes as gaps rather than
building new root destinations or claiming all app consumers are certified.

## 8. C7 — Finish design and native acceptance

**Risk:** parity-sensitive visible UI. **Dependencies:** C0 design authority,
C1–C3; C6 for functional acceptance. Optional matrices depend on C4/C5.

Use the registered **`entity-object`** surface, not a legacy `places` screenshot
as a substitute. The old roadmap's generic Places QA instruction needs updating.

1. Promote approved isolated design screens into a governed reference location;
   record source/revision and map them to supported states. Do not use the
   implementation screenshot as its own design authority.
2. Compare plate/no-plate geometry, kicker/name/byline order, fact value/label
   hierarchy, source affordances, short reading body, closing facts and location
   handoff. Fix only accepted scope and supported data. No fabricated facts or
   social statements to reproduce a rich fixture.
3. Exercise square permitted media, no-photo/error/rights-denied states,
   long names, dense sources, maximum permitted people text and sheet overflow.
4. Honor current accessibility governance and dynamic text. Do not reintroduce
   fixed tiny labels from an older specimen. Check screen-reader order, focus
   return from sheets, labels, target sizes, Android back, safe areas and scroll.
5. Capture flags-on rebuilt routes on intended iOS/Android release platforms.
   Capture exact binary/build, backend SHA, JS SHA, data mode and scenario.
   Keep private raw evidence in access-appropriate test artifacts; published
   receipts contain no production private prose or identifiers.

### Minimum matrix (pairwise where safe, not an unbounded Cartesian product)

| Dimension | Coverage |
| --- | --- |
| Kind | Venue, site, experience; each gets canonical read, Keep, Ask, error and return checks |
| Object/data | Rich, sparse, no media, alias, provisional owner/non-owner, unavailable |
| Lifecycle | Loading, retryable failure, offline, reconnect, warm restart, cleared-state start, route/account replacement |
| Relationship | Unsaved/saved, planned, supported occurrence, private outcome, correction/retraction |
| Time | Fresh→expired while mounted and while backgrounded, changed Plan/origin |
| Optional research | Absent, queued, running, ready, stale, failed, unavailable, uncertain/exhausted polling; core flag-off absence |
| Optional people | Allowed, expired, withdrawn, denied precision, feature off, sheet open at withdrawal |
| Accessibility/platform | Default/enlarged text, narrow device, VoiceOver, TalkBack, iOS/Android back/focus behavior |

Follow the repository runner: scenario/design checks, doctor, capture,
comparison/material-health, structured verdict scaffold, manual inspection,
validation and verdict commit. Read the verdict protocol during execution.
Dry runs produce harness evidence only; unavailable platform/design/auth lanes
remain explicitly blocked gates, not converted into unit-test passes.

**Exit:** a current-build behavioral and design verdict for the core page,
plus separate optional capability verdicts. Fixes receive recaptures.

## 9. C8 — Reconcile operations and prepare an approvable release packet

**Risk:** operational planning; no enablement included. **Dependency:** C6/C7
for core approval; C4/C5 and their native evidence for optional approval.

- Update the existing roadmap, surface contract, native receipt, runbook and
  pilot manifest with current evidence and scoped residual gaps. Do not create
  another overlapping runbook or quietly rewrite historical test results.
- Refresh the content-free read-only health baseline. The old pending research
  row and resolution-review counts are historical; re-read before assigning
  disposition. Route any action to the existing owner, without deleting,
  requeueing or mutating rows as part of this package.
- Record backend/mobile deployed identifiers separately from reviewed source.
  Keep core, research and people flags/cohorts independently accountable.
- Name operational owner/backup; baseline latency/error/queue-age and inspection
  signals; set an explicit cost ceiling before research. Existing configured
  limits are not owner approval or proof of adequate monitoring.
- Rehearse rollback in the isolated lane: stop new admission, remove cohort,
  stop approved worker invocation, preserve dated readable artifacts and audit
  rows, then verify affected clients recover. Document already-running jobs;
  do not claim an admission flag cancels in-flight external work.

**Exit:** an honest release packet whose remaining approvals are visible.
Preparing it is not evidence that any pilot is approved or enabled.

## 10. Execution order, commit boundaries and decisions

Suggested sequence:

1. C0 baseline/authority reconciliation.
2. C1 public sharing; C2 canonical route/read boundary; C3 time/lifecycle.
3. C4 research lifecycle and C5 approved people contract/client changes.
4. C6 real-owner journey/repair integration.
5. C7 current-build visual/native acceptance and scoped fixes.
6. C8 evidence/operations reconciliation; stop before operational enablement.

If the people contract or remote-revocation decision is blocked, finish the
other packages and record C5 as blocked with people off. If reference export
is unavailable, finish behavior tests while leaving design acceptance open.
Neither condition authorizes expansion to compensate for the missing gate.

### Reviewable commit plan

| Commit/package | Repository | Intended boundary |
| --- | --- | --- |
| C0 | workspace / app docs as applicable | Scope reconciliation and acceptance ledger |
| C1 | app | Public-share allowlist, sheet lifetime and regressions |
| C2 | app | Canonical route/action ownership, dependency gating and route tests |
| C3 | app; backend only if needed | Mounted expiry, lifecycle revalidation and focused tests |
| C4a | app | Request identity, deliberate retry, bounded polling and race tests |
| C4b | backend | Worker/status regressions and only fixes exposed by them |
| C5a | backend | Approved projection-validity fields and owner authorization tests |
| C5b | workspace + app | Generated contract synchronization, fail-closed client and lifecycle tests |
| C6 | respective owning repo | Cross-owner fixtures/proofs; one narrow owner fix per commit if required |
| C7 | app | Approved reference registration, scoped polish, native flows and verdicts |
| C8 | workspace | Updated readiness/runbook/native/pilot receipts |

These are review boundaries, not a quota: split a package if it mixes concerns;
do not make an empty production change when characterization already passes.
Keep every repository independently understandable, and identify related
contract commits across repositories in the receipt.

Use descriptive `codex/entity-*` branches/worktrees if implementing in parallel
with other sessions. No automatic subagent delegation is assumed. Recheck the
checked-out branch before committing, explicitly stage only owned filenames,
preserve unrelated changes, and never bypass hooks to manufacture a green
receipt. Report pre-existing gate failures separately. Do not push or merge
without the applicable user instruction.

### Explicit decisions before crossing their boundary

| Decision | Proposed default | Blocking scope |
| --- | --- | --- |
| Public share content | Canonical public name + public link; no authenticated prose | C1 can proceed with this narrow behavior after execution authorization |
| People contract | Additive validity metadata from existing owner truth | Obtain approval for shared response-model changes before C5a |
| Remote withdrawal | Proven owner invalidation, or an explicitly accepted ≤60s visibility lease | People enablement; never silently weaken the privacy promise |
| Design source | Approved isolated export; otherwise documented owner-approved reference baseline | Pixel-level/design acceptance |
| Platform/account evidence | Intended release platforms and two real authenticated test principals | Corresponding native/auth approval; no silent iOS-only waiver |
| Paid research canary | Off until named owner, inspected output plan and explicit budget | Any model/provider-backed operational run |
| Deployment/cohort | Explicit reviewed builds and opt-in audience | Pilot enablement; never implied by an implementation instruction |
| Backfill | None | Remains outside every package |

## 11. Validation commands and reporting

During execution, use the repositories' configured environments. Verify paths
and test registrations at the implementation SHA rather than copying an old
passing count. These are starting selections, not commands run in planning.

Backend focused selection:

```bash
cd travel-agent
PYTHONPATH=. .venv/bin/pytest \
  tests/api/test_entity_research_requests.py \
  tests/api/test_entity_people_lines.py \
  tests/places/test_entity_presentation_read.py \
  tests/places/test_entity_relationship_reads.py \
  tests/places/test_private_entity_contracts.py \
  tests/places/test_entity_situation.py \
  tests/research_agent/test_research_queue.py \
  tests/domains/relationships/test_persistence_postgres.py \
  tests/scenarios/test_micro_journey_loop_closure.py -q
```

PostgreSQL-marked tests require the isolated test database. Do not aim their
transactional fixtures at an ordinary local or production database. Add new
focused tests for each new failure; run the broader required backend selection
and lint/format gates per repo guidance before completion.

Mobile focused selection:

```bash
cd travel-app
npm test -- --runInBand \
  __tests__/components/places/ObjectPageRebuild.test.tsx \
  __tests__/components/places/objectPageProjection.test.ts \
  __tests__/components/places/ObjectPageShell.test.tsx \
  __tests__/components/places/ObjectPageStateShell.test.tsx \
  __tests__/components/external-share/PlaceShareOwnerSheet.test.tsx \
  __tests__/data/entityResearchRequest.test.tsx \
  __tests__/data/entityForceState.test.tsx \
  __tests__/hooks/useUnexpiredValue.test.ts \
  __tests__/hooks/useSaveEntity.test.ts \
  __tests__/screens/venue-detail.smoke.test.tsx \
  __tests__/screens/experience-detail.smoke.test.tsx
npx tsc --noEmit
npm run test:typecheck:contracts
npm run api-boundaries
npm run schema-bridge
npm run accessibility-governance
```

Add the new people lifecycle, public-share payload, and flag-on site/venue/
experience route suites to this selection. Existing flag-off route mocks do
not prove rebuilt-route behavior. Run touched-file lint and relevant navigation,
query-key ownership and convention suites as well.

For approved backend response changes, run `./scripts/sync-types.sh` from the
workspace, review `docs/openapi.json`, `docs/openapi.app.json`, and
`travel-app/utils/api/schema.gen.ts`, then `make contract-check` and applicable
API-operation governance. Never hand-maintain mirrored TypeScript models.

Native entry commands, from `travel-app`:

```bash
npm run qa:polish:scenarios
npm run qa:design:check -- entity-object
node scripts/polish-qa/run-polish-qa.mjs entity-object --doctor
npm run qa:surface -- entity-object --after
```

Complete comparison and structured verdict review using the repository's
`AGENTS.md` workflow. Then run aggregate gates appropriate to the touched
surfaces and report existing failures with exact scope. Focused green tests
must never be reported as a green whole-repository or deployed release gate.

Each completion receipt distinguishes **implemented**, **deterministically
tested**, **real-backend tested**, **native/design accepted**, and **enabled**.
It records sample sizes, skips, source/build revisions, flags, data/auth mode,
failed/blocked cases, and next owner action. A screenshot proves only what is
visible; a mocked test proves only its controlled contract.

## 12. Definition of completion

Core implementation closure requires C1–C3 and the applicable C6 proofs. Core
product acceptance additionally requires C7 on the intended release platforms
and an owner-reviewed C8 packet. Research and people each need their own
completed code, negative tests, real-backend/native evidence and operational
approval before enablement.

The resulting milestone is a trustworthy first entity-page family, not a
larger place directory. Any later coverage proposal should be justified by
measured useful clicks that cannot resolve—not by a desire to fill sparse UI.
