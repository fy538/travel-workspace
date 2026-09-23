---
doc_type: working
status: active
owner: founder / engineering architecture
created: 2026-09-15
last_verified: 2026-09-15
expires: 2026-10-15
why_new: Maps live, indirect, compatibility and retiring consumers across Home, Chat, Places, Life, Capture, content, notifications and practical systems; the existing generation review covers model/content execution but not this cross-system consumer and cutover disposition.
supersedes: []
source_of_truth_for: []
---

# Service, consumer and retirement consolidation — September 15 investigation

## Decision this report enables

Choose a bounded cleanup or shared-mechanics package without disrupting the
selected Home/Places construction or confusing a retired *surface* with an
unneeded domain capability. This is a dated source inspection, not another
product authority, execution queue, production traffic audit, or authorization
to delete historical records. The [program roadmap](vesper-program-roadmap.md)
owns order; the [generation review](generation-infrastructure-and-consolidation-review-2026-09-14.md)
and [technical G packages](complete-system-integration-roadmap-2026-09-05.md#generation-consolidation)
own generation-lifecycle work. The [capability-retirement receipt](capability-retirement-execution-receipt-2026-09-05.md)
owns booking's local implementation and outstanding operational gates.

**Intended behavior of this documentation change:** preserve the current owner
seams while making actual producer-to-consumer paths and retirement preconditions
inspectable. The workspace owns this cross-repository map. Acceptance is valid
working-document metadata and links, no competing canonical wording, and a
source-supported disposition for each proposed cleanup.

## Inspection tuple and evidence limits

The primary code inspection used the coordinated receiving checkout, not the
canonical sibling `main` checkout:

| Repository | Branch / inspected HEAD | Working state during inspection |
| --- | --- | --- |
| Workspace | `codex/receiving-completion-2026-09-10` / `3465b83a8f5f1e4032b3cfbc05ebd83168650c41` | Four roadmap/capture/supply working docs modified by the active owner; not edited here. |
| Backend | same named child branch / `7c56b8fd7b8dd5be0fb9a5fbe0b2c0acf4fa4130` | Clean at inspection. |
| Mobile | same named child branch / `73e966e9ddb11ca98f33f5a565a0043048674256` | Active Home native/test/QA edits appeared after the first status read; not edited here. |

The separate situated-value coordinated lane was clean in all three repositories.
The canonical workspace `main` was dirty with Design-owned documentation, while
canonical child `main` checkouts were clean. Worktree inventories contained 39
workspace, 42 backend and 40 mobile worktrees at inspection. Counts alone do
not identify stale or removable worktrees; their owner, unique commits, dirty
state and runtime allocation require a separate audit before pruning.

This review read code, owner docs, route policy and registered callers. It did
not contact a deployed environment, provider, production database, live queue,
or paid model. Static reachability cannot establish zero supported-client or
deployed traffic. `make api-coverage-check` passed with 582 active, 15 dark and
62 retiring operations; the import-boundary check passed; the lazy-import check
reported 60 documented bridges and no new/stale entries. These checks prove
policy and import consistency at the inspected checkout, not product adoption,
runtime availability, provider costs or native quality. No full `make verify`,
disposable-DB concurrency test or native verdict was run for this investigation.

## Architecture in one view

The backend is a modular FastAPI application, not a collection of separately
deployed domain microservices. Ordinary model calls use the shared
[`core/llm.py`](../../travel-agent/backend/core/llm.py) gateway and registered
surface/model routing. Job categories use one Arq worker *entry-point type*,
[`WorkerSettings`](../../travel-agent/backend/workers/audio_jobs.py), despite
the historical `audio_jobs` name; deployed replica count was not inspected.
The newer Source workflow owns durable
request state; Redis/Arq transports its job UUID, not another copy of Source
truth. Distinct domain owners, result stores and rights remain necessary.

The durable [architecture principles](../../travel-agent/docs/product/Product%20Architecture%20Principles.md)
define Source, Person, Place, Occasion, Plan, Commitment, Moment, Occurrence and
Outcome as ownership contracts, not a mandate for one universal table. A
viewer-safe root projection may compile their outputs but cannot become their
mutation owner. The current code broadly follows this separation. Its most
significant debt is *generation-to-generation coexistence* and uneven
production/reuse/retirement mechanics above the shared model gateway.

## Consumer map: live, indirect, compatibility and candidate retirement

| Path / current owner | Actual source-to-consumer path | Current disposition and prerequisite |
| --- | --- | --- |
| **Legacy per-trip Home** — `backend/home/feed.py` | `GET /api/trips/{trip_id}/home_cards` → `data/home.ts::useTripHomeCards` → `TripsHomeController`. The route is mounted when the target shell is not enabled. | **Keep during legacy posture.** The new Home root does not call this assembler, but legacy Plans still does. Retire only after the shell's accepted cutover and old deep-link/feature obligations are checked. |
| **Cross-trip Concierge Home feed** — `backend/home/concierge_feed/` | Direct `GET /api/concierge/home` has a mobile facade, with no identified current mounted-screen caller in this static pass. **Indirectly live:** `vesper_workbench/assemble.py` defaults its feed loader to `assemble_concierge_home_feed`, and `seam.py` reduces ranked cards to an urgent Chat/Vesper door. That feed reuses helpers and `HomeCard` from per-trip Home. | **Separate route from package.** The direct route may be a later transport retirement candidate; the producer cannot be deleted while the workbench's urgent seam depends on it. First move that seam to a narrower canonical urgent/read model under Chat/workbench owner review. |
| **Current Chat/Vesper workbench** — `backend/home/vesper_workbench/` | `GET /api/concierge/home/workbench` → `useVesperWorkbench` → mounted `app/(tabs)/concierge/index.tsx`. Here/Season catalogs and urgent seam are different producer concerns. | **Keep.** Do not erase a current Chat root or useful catalogs by treating every `backend/home` subpackage as retired Home. Its redesign/cutover belongs to its owner, not this cleanup audit. |
| **Home root v1 and v2** — `root_projection` | v1 reads the Experience Graph and compiles temporal Home. v2 runs owner reads, value-over-silence judgment, root seat/exposure gates and root-native compilation. `HomeRootExperience` keeps v1 cold on a healthy v2 response and wakes it on transport/contract failure. | **Keep both during governed rehearsal.** v1 is an active fallback and the shell can also run in compatibility posture. A device-verified, coherent release cutover and fallback policy are required before retirement. |
| **Places feed, v1 root and governed runtime** — `places` + `root_projection` | The mature `PlacesWorkspace` consumes Places feed/map/search/save and a joined `/v2/places/runtime` semantic envelope. `PlacesRootExperience` wakes the v1 root after runtime failure/expiry. The standalone `/v2/places` route also exercises the semantic contract. | **Do not remove mature capabilities to make the root uniform.** The runtime intentionally joins governed admission to the existing map/workspace. Retire duplicate reads only after replacement/parity and error handling are proved. |
| **Legacy Discover sectioned feed** — `backend/discover/` | `GET /api/discover/feed` is deprecated and marked retiring. The mobile `getDiscoverFeed` transport has an unmounted `useDiscoverFeed` facade in this pass. The similarly named, mounted `useDiscoverFeeds` in legacy Trips Home instead calls For You, social feed and collections. `backend/discover/`'s sectioned composer is otherwise only imported by its own API route. | **Best bounded route/package retirement candidate after traffic proof.** Confirm supported-client and deployed zero traffic, then retire backend route/composer plus app facade/mock/tests/contracts together. Do not remove the distinct For You/social/collections path. |
| **Atlas-era board composition** — `backend/composition/` + `backend/atlas/` | `compose_board` has Atlas taste-board callers; Discover's board consumer was retired in July. The Atlas *tab* now redirects to Life, but old Atlas compose/reading deep routes and `useAtlasReading` still exist. | **Compatibility, not conclusively dead.** Do not build a new generic board engine or automatically perform G1b. Check deep-link/retained-reader traffic and Life replacement before retiring Atlas copy upgrades or the board path. |
| **Custody-first Intake v2 and legacy inbound** — `backend/inbound/` | New shares use `intake_submissions`; older inbound items remain for older callers/rollback and unsupported paths. Mobile `data/inboundItems.ts` contains both, while mounted share-capture and exact submission readers use v2. | **Converge by supported format and owner agreement.** Preserve accompanying authored intent, immediate result, safe leave, exact return and correction. Do not let legacy and v2 become two semantic truth owners or move intake into Life. |
| **External experience ingestion** — `backend/ingestion/` | Scoped provider/event ingestion writes the public experience corpus. It is not user-initiated Source custody. | **Keep distinct from inbound.** Similar folder names do not justify consolidation. |
| **Life projection** — `backend/life_projection/` | Derived records/index/organization consume owner changes and support viewer-relative Life navigation; the owner explicitly disclaims Source custody and Occurrence truth. | **Keep derived.** Indexed-serving cutover, free-text interpretation and Atlas retirement remain separately gated. |
| **Notifications** — `backend/notifications/` | Optional inferred-value arbitration and mandatory delivery policy are separate questions. Deterministic due/transactional events can bypass learned arbitration but not recipient delivery gates. Root semantic admission may cap interruptive treatment. | **No second notification service needed.** Reuse content-free admission/readout where warranted; do not collapse current owner facts, arbitration and delivery into one generic score. |
| **Booking and expense** — their domain owners | Booking new execution is guarded by the retirement flag; callbacks, obligations, recovery and evidence readers remain. Expense OCR may assist, but deterministic shares, money and payment state stay ledger-owned. | **Contract UI and execution footprint separately.** The [expense brief](assisted-expense-contraction-brief-2026-09-05.md) proposes compact result/inspection while preserving exact ledger. Booking route/table/provider deletion waits for deployed obligation audit, retained-reader migration and operator recovery. |

The key hidden dependency is:

```text
Mounted Chat/Vesper workbench
  → workbench urgent seam
  → cross-trip Concierge Home assembler
  → legacy per-trip HomeCard/helpers and other ranked producers
```

By contrast, governed Home v2 does **not** import the legacy Home assembler:
[`root_composition.py`](../../travel-agent/backend/api/services/root_composition.py)
reads domain/source candidates and the `root_projection/v2` compiler. This makes
legacy Home retirement possible eventually, but **not** until both Plans' old
read and Chat's hidden seam have a supported successor.

## Why similarly named admission layers should remain distinct

The [lived-experience judgment](../../travel-agent/backend/lived_experience/judgment_admission.py)
answers whether an evidence-bound candidate materially helps the current job
over silence and what treatment ceiling it earns. Root
[`gates.py`](../../travel-agent/backend/root_projection/v2/gates.py) then applies
root permission/currentness, exposure, cluster/seat and attention-budget rules.
[`compose_root_projection`](../../travel-agent/backend/api/services/root_composition.py)
executes owner reads and value assessment before root selection. Notification
delivery decides recipient/channel timing afterward. These are different
decisions with different authority; eliminating one to reduce module count
would blur meaning, surface capacity and interruption.

## Actual shared-mechanics opportunities

### Generation lifecycle — use existing G packages, not a new platform

The [September 14 review](generation-infrastructure-and-consolidation-review-2026-09-14.md)
found the shared model/provider gateway and accounting already substantial.
G1a repaired demonstrated Pick/Settle cache identity omissions; G3 connected
explicit, controlled Source requests through the existing durable workflow and
queue. Both are locally complete at their bounded receipts. G1b (Atlas copy
upgrade), G2 (lookup reuse), G4 (outbox mechanics) and G5 (resource controls)
remain conditional or unexecuted; none should be dispatched merely to fill a
checklist. Public preparation, private synthesis, human originals, current
owner facts and generated media have different output/rights contracts.

**G2 disposition before repair:** `lookup_agent/cache.py` filters a semantic
hit by city and freshness, not by `query_type` or resolved subject. The agent
returns cached prose before entity resolution and omits fresh-response citations
on the hit path. This is a genuine reuse defect if Lookup survives. But
[`api-operation-policy.json`](../governance/api-operation-policy.json) marks
`POST /api/lookup/` retiring, with no named consumer and a September 15 review
date; no mobile call was found in this static pass. First establish deployed
traffic and a selected future journey. Repair its exact-subject/citation
contract only if it remains supported. Otherwise retire route, cache, tests and
contract shadows through the API owner. Similarity may find evidence; it must
never authorize reuse of personal or operational final prose by itself.

### Projection outboxes — G4 is real duplication with non-identical semantics

[`memory_projection_outbox.py`](../../travel-agent/backend/core/db/memory_projection_outbox.py)
and [`life_projection_outbox.py`](../../travel-agent/backend/core/db/life_projection_outbox.py)
each implement transaction-bound enqueue, due-row selection with
`FOR UPDATE SKIP LOCKED`, lease-token claim, exact token read, acknowledgment,
exponential retry and seven-day published-row pruning. Together they are about
500 lines. This is a concrete extraction candidate, not evidence that their
tables or events should merge.

| Semantic difference | Memory projection | Life projection |
| --- | --- | --- |
| Enqueue identity | Coalesces a pending user correction event and replaces its `projection_version`/payload. | Inserts or deduplicates an explicit `event_key` carrying owner revision, change and policy coordinates. |
| Acknowledgment fence | Requires event ID, projection version and lease token; does not additionally test unexpired lease in the inspected update. | Requires event ID, lease token and unexpired lease. |
| Retry terminal state | Bounded exponential delay in this module; no local dead-letter marker in the inspected function. | Same general delay shape, with dead-letter at eight attempts. |
| Owner meaning | Invalidate/rebuild a memory-derived projection after correction. | Deliver an owner change into derived Life organization/index. |

The lease-expiry difference is an **unresolved contract distinction**, not a
declared defect. A common helper must preserve each owner's chosen fencing and
terminal policy until tests and owner review establish a justified unification.
G4's narrow first pair belongs in one backend writer after overlapping
Capture/Life writers hand off. Disposable-DB tests should cover concurrent
claim, stale-holder acknowledgment, version replacement, retry/terminal and
transaction rollback. No universal event table or cross-domain schema rewrite.

### Resource controls — share mechanics, not economic authority

`core/llm_accounting.py` observes provider usage after calls;
`commercial_access/` can atomically reserve customer allowance;
`research_agent` has per-job limits and a separate atomic city cap;
`places/budget.py` applies a daily soft provider-call gate. These are different
subjects and costs. G5 should reuse deadline/idempotency/reservation patterns
where two actual producers require them, while supplier exposure, customer
benefit and provider uncertainty retain separate owners. A usage ledger alone
is not pre-call spend admission. Paid/recurring production needs the existing
supply/commercial decisions and measured cost evidence.

### Import bridges and file hotspots — opportunistic debt, not a new migration

`check_imports.py` passed with no direct cross-agent violations;
`check_lazy_imports.py` reported 60 documented lazy bridges, including
`core → agent` cases. The architecture guidance explicitly calls that the
highest-priority category when its owner interface can stabilize. A wholesale
import migration would risk cycles and owner movement during active product
construction; reduce bridges when a surviving shared contract is already being
touched, and require the checker/owner rationale to shrink with the code.

Representative large files at this tuple are `home/concierge_feed/producers.py`
(2,171 lines), `api/routes/booking.py` (2,623), `api/routes/expenses.py`
(2,053), `api/routes/root_projections.py` (1,193) and mobile
`data/rootProjections.ts` (620). Line count is not a correctness metric. The
first two are especially poor targets for cosmetic modularization while their
presentation/execution dispositions remain unresolved. The root-projection
route repeats Places practical-request parsing across standalone v2 and joined
runtime endpoints, but that file is within the active Places owner seam; defer
a local extraction until a coherent receiving cut and preserve API parity.

## API-retirement queue: static eligibility is not deletion authority

The policy contains 62 `retiring` operations with no listed consumers; 52 have
`review_by: 2026-09-15`. Representative candidates include deprecated
`GET /api/discover/feed`, `GET /api/discover/trending`, and
`POST /api/lookup/`. The complete queue, lifecycle, owner and removal trigger
remain in [the operation policy](../governance/api-operation-policy.json), not
a second manually maintained list here. The passing API audit means operation
classification and trace rules are coherent; it does **not** prove an exported
data hook is mounted, a supported older client has stopped calling, or deployed
traffic is zero. `--list-transport-only` additionally identified 24 transport
methods without product callers; some retiring endpoints are absent from that
list because a facade exists without a mounted consumer.

For each proposed retirement, inspect four different consumers before a write:

1. current mounted native routes and conditional flags;
2. indirectly imported producer functions used by another live route;
3. historical/deep-link, export, deletion, privacy, recovery and operator
   obligations;
4. supported-client and deployed traffic over the policy's agreed window.

Then delete the backend operation, app facade/mock, generated projection inputs,
tests and governance entry coherently, using the workspace's API sync and
coverage checks. Backend route removal is contract-sensitive and requires the
child Task Intake, focused tests, offline OpenAPI/type sync and affected mobile
consumers. The traffic and obligation steps cannot be replaced by repository
search or a reviewer vote.

## Recommended sequence for this supplemental lane

**First: G0-style disposition of a bounded trio.** Review deprecated Discover
feed, retiring Lookup and the direct Concierge Home feed route **separately from
its live package**. Produce for each an exact caller/flag/indirect dependency,
traffic/obligation evidence boundary and keep/repair/retire choice. Do not
make zero traffic up. This is an audit that can proceed without touching the
active Home/Places native files; deletion waits on the named policy gate.

**Second: G4 only when its owner files are free.** If the first disposition
cannot yield a safe deletion because deployed evidence is unavailable, use the
backend slot for a narrow memory/Life outbox helper and paired concurrency
tests. Decide the lease/terminal distinction before implementation. This is a
bounded engineering-quality result, not a prerequisite for native content.

**Third: product-generation retirement at actual cutovers.** After Home/Places
and later Chat/Life replacements are owner-backed, visually accepted and
supported-client safe, retire old assemblers, routes and deep screens in
consumer order. Booking execution follows its deployed obligation and retained
evidence gates; expense surface contraction leaves deterministic money truth
intact. Avoid an all-repository screen purge, noun migration or generalized
generation service.

The next product-experience cut remains the program owner's first priority.
This supplemental cleanup lane should reduce code that has no surviving job or
share repeated mechanics where two surviving jobs prove the abstraction. It
should not force feature construction to wait for a cleanliness score.

## Open questions and exit

- Is there any supported/deployed traffic on the three proposed route
  candidates, and which historical links or operator readers still depend on
  them? **Unresolved;** no production inspection was performed.
- Should Memory's acknowledgment reject an expired, unreclaimed lease as Life
  does, or is its projection-version fence intentionally sufficient?
  **Unresolved;** require owner decision and disposable-DB evidence before G4.
- What exact successor will provide the workbench's urgent seam without
  assembling the full legacy Concierge Home feed? **Product/Chat owner handoff,**
  not a silent cleanup decision.
- When does the governed four-root rehearsal become a supported serving
  cutover, and what fallback/older-client window remains? **Release owner gate.**
- Which Atlas compose/reading deep links and retained board results need
  continuity after Life adoption? **Life/Atlas owner and traffic gate.**

Before this working report expires on October 15, either turn a verified
disposition into the existing program/G owner plan and archive this snapshot,
or reverify the tuple and remaining questions. Do not promote its point-in-time
counts into Product Thesis, Current State or an overlapping architecture canon.
