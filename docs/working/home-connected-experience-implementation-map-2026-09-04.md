---
doc_type: working
status: active
owner: founder / Home engineering
created: 2026-09-04
last_verified: 2026-09-04
expires: 2026-10-04
why_new: Converts the connected Home journey plan into an evidence-linked code map and production-feasibility work package without authorizing a repository-wide rewrite or a second owner system.
supersedes: []
---

# Home — connected-experience implementation map

## 1. Purpose and decision boundary

This document is the engineering companion to the [connected Home plan](home-connected-experience-plan-2026-09-04.md). It maps the four journeys in that plan onto the code that already exists in the backend and mobile app.

It is an implementation-readiness map, not a claim that the Claude composition is shipped. The inspected repositories have active concurrent work; branch, status, and commit must be rechecked before modifying a file. This map deliberately does not authorize a new navigation framework, a generalized Occasion store, a booking surface, or a Home-owned copy/content factory.

### Baseline observed during the September 4 inspection

| Repository | Observed ref | Interpretation |
| --- | --- | --- |
| `travel-agent` | `d10fafd86` on `main` | Existing root-projection and adjacent backend work is a reuse baseline only; the working tree is dirty. |
| `travel-app` | `ec09c0f41` on `main` | Existing Home v2/navigation/return seams are a reuse baseline only; the working tree is dirty. |
| workspace docs | current working documents | The Home Revision 3 design and connected journey plan remain working references, not promoted product canon. |

Do not reset or sweep concurrent changes into a Home commit. Re-run the checks above and inspect ownership at the start of every package.

## 2. Current seams: what exists and what it means

| Seam | Current evidence | Disposition for the connected prototype |
| --- | --- | --- |
| Home projection consumption | `travel-app/components/home-root/HomeRootExperience.tsx`: `useHomeRootProjectionV2`, expiry observation, consequence confirmation, compatibility fallback | **Keep.** Adapt composition data and event wiring; do not add a second Home state machine. |
| Home v2 presentation | `HomeRootV2Screen.tsx` and `HomeRootV2UnitRenderer.tsx`: typed regions, units, exposure, scroll restoration | **Keep/adapt.** Map Revision 3 units to existing renderer families. Keep ranking and domain data outside layout components. |
| Home interaction orchestration | `HomeRootExperience.tsx`: `openV2Destination`, `openV2Action`, `openV2Resource` | **Keep/adapt.** Every prominent control needs an explicit destination/action disposition and a return token. |
| Owner-root destination mapping | `travel-app/utils/rootProjectionNavigation.ts`: `hrefForRootResource`, `hrefForRootDestination`, `hrefForRootCapability` | **Adapt narrowly.** Entity and Places-context paths are real; plan/occasion/commitment/opening/action resources often fall back to Chat or Life root. Add only exact owner routes proven by the owning lane. |
| Canonical resource routing | `travel-app/utils/resourceDestination.ts`: allowlisted paths, exact entity routes, Life/source fallback, honest unsupported result | **Keep.** Prefer this seam for ResourceRef opening rather than arbitrary router pushes. |
| Return context | `travel-app/utils/rootProjectionReturnRegistry.ts`: typed selected refs, viewer, region/unit, exact-or-recomposed resolution, 30-minute in-memory TTL | **Keep/adapt.** Test exact restoration, recomposition after revision, and a graceful root fallback after restart/expiry. Do not mistake it for durable product memory. |
| Places family | `travel-app/utils/placesRouteFamily.ts` and `usePlacesSemanticNavigation.ts` | **Keep.** Preserve Home-depth versus Places-root semantics and context handles. |
| Consequence boundary | `travel-app/hooks/useRootConsequenceConfirmation.ts` | **Keep/adapt.** Use previews only for writes with real external/audience effects; read-only exploration must remain immediate. |
| Projection reads | `travel-app/data/rootProjections.ts` | **Keep.** Separate HTTP refresh/revalidation from model/provider generation in measurements and tests. |
| Backend root composition | `travel-agent/backend/root_projection/FEATURE.md` and `backend/root_projection/v2/*` | **Keep.** Reuse bounded owner reads, candidate admission, value portfolio, root-native compilation, grants, and exposure. The root projection must not become a domain owner. |
| Source contribution validation | `source_contribution_pipeline.py` and `source_contribution_runtime.py` | **Keep/adapt.** Preserve source/material/audience/grant checks and revision binding for Home-derived contributions. |
| Source contribution production | `source_contribution_producer.py`: `SourceContributionProducerBudgetV1` (`max_sources=3`, bounded input/output, timeout, retry) | **Keep, instrument.** These are per-call limits, not an account-level cost model or proof of reuse. Add result reuse and refresh measurements before broadening generation. |
| Life record opening | `travel-agent/backend/life_projection/record.py` and `api/routes/root_projections.py`; mobile generated schema includes `/api/root-projections/v1/life/record` | **Keep/adapt.** Use canonical artifact/intake/trip record refs. Do not route every Life resource to an undifferentiated root if an exact record ref exists. |
| Shared contribution contract | `docs/systems/contribution-and-consequence.md` | **Keep as cross-repo contract.** Ask/Bring, T0/T1/T2, owner readback, audience, correction, and withdrawal govern J2–J4. |

The principal gap is not “we need more infrastructure.” It is destination and owner precision: several typed Home resources can currently land in generic Chat or the Life root, which is insufficient for a connected prototype that promises recognizable continuity.

### Scoped progress since the initial map

The first implementation slice landed in mobile commit `dd313abd8`:
`hrefForRootResource` now opens `memory_candidate`, `intake_submission`, and
`reading` through their exact Life routes, and `artifact` through the
source-bound canonical artifact reader (`/you/memories/artifacts/[id]`). The
older memory/Atlas aliases remain unchanged for existing callers. This closes
the J4 exact-record opening seam; it does not prove the intake write/readback
journey or resolve the remaining arrangement and loose-Keep contracts.

Mobile commit `e98985c30` extends the same seam for an explicitly allowlisted
non-Chat owner path: a Plan/Occasion/opening resource can now honor its declared
Home, Places, or Life route (with the short return token) when one is supplied.
Legacy owner-only paths and Chat paths still use the existing Chat handoff. This
is route precision, not a new arrangement surface; the owning lane still has to
publish and test the canonical destination before a projection can use it.

Mobile commit `f5ef99df1` completes the Life-side continuation of that seam:
when a `life` destination includes an explicitly allowlisted exact Life resource,
Home opens that resource (including the short return token) instead of dropping
the user at the Life root. Trip and source-bound Life readers now preserve the
same return context. A Life destination with no exact Life ref still lands at
the Life root, so this does not invent a new Life surface or change Chat/Life
ownership.

Mobile commit `00d2dd892` adds return-registry coverage for audience changes and
selected-resource revision changes. The restoration contract now has executable
proof that those changes recomposes Home rather than restoring a stale unit;
restart behavior remains intentionally represented by the missing-token fallback.

Mobile commit `bf879c7f8` narrows exact Life continuation to Life-record resource
kinds. Incidental people or place refs carried for context cannot silently
redirect a Life destination to the wrong owner route. The follow-on mobile
commit `b80626984` includes graph-owned `plan`, `occasion`, `commitment`,
`opening`, `outcome`, and `recovery_instrument` refs when their owner publishes
the canonical `/you/history` path, while keeping a generic `trip` ref on the
Home/Plan owner. This matches the current Life adapter's route contract rather
than guessing from resource kind alone.

## 3. Journey-to-code matrix

Status vocabulary: **present and verified** means the seam is visible in code but still needs a journey test; **present but unverified** means a similar path exists but its exact semantics are not proven; **adapt** means a small owner-specific change is likely; **missing** means no honest implementation path was found; **blocked on owner decision** means engineering should not invent the contract.

### J1 — possibility → inspect → optional keep → Home

| Step | Current path | Status | Keep/adapt/add decision | Required verification |
| --- | --- | --- | --- | --- |
| Open a Home option | `HomeRootV2UnitRenderer` → `HomeRootExperience.openV2Destination` or `openV2Resource` | present and verified | Keep typed event flow; assign a stable fixture ref to the option and represented resources | Render and tap each R3 option; prove no implicit save/plan write |
| Open Place/entity depth | `hrefForRootDestination` / `hrefForRootResource`; `places.open_entity`, entity route allowlist | present and verified | Keep exact entity route; preserve `originRoot=home` and return token | Entity opens with expected context and source refs; back returns to the originating unit |
| Ask a contextual question | destination target `chat` → `conversationSeedForRootDestination` / `destToHref` | present but unverified | Keep new seeded conversation policy; verify target identity and no accidental reuse of unrelated chat history | Private contextual question opens with the correct refs and return context |
| Keep without adopting | no confirmed generic loose-possibility owner route in current mapping | blocked on owner decision | Decide whether Keep is an existing Life/Plan operation; do not create a Home store or silently create a Plan | Accept, cancel, duplicate, and stale revision cases; read back exact retained ref |
| Return/recompose | `rootProjectionReturnRegistry` exact-or-recomposed resolver | present but unverified | Keep; add changed/withdrawn/thin-state fixture | Exact return while valid; honest recomposition after revision/expiry |

**J1 owner dependencies:** Places/entity owns depth; Plan/Life/Capture must define loose retention; Home only projects the resulting state.

### J2 — social contribution → consume → inspect context → optional response/use

| Step | Current path | Status | Keep/adapt/add decision | Required verification |
| --- | --- | --- | --- | --- |
| Read addressed contribution | Home resource/action path plus source-backed projection refs | present but unverified | Keep original attribution and audience metadata; do not synthesize a generic social feed | Viewer sees a complete share without responding; private/group scopes remain distinct |
| Inspect original and Place | `hrefForRootResource` for artifact/entity/place plus Places context route | present and verified | Keep canonical ResourceRef opening; adapt only missing source/original route | Original, source scope, and place context agree |
| Browse more shared material | No confirmed present-tense browse owner was found in the Home navigation map | blocked on owner decision | Decide whether Life People or a separate explicitly scoped destination serves this intent; no silent new social root | Authorized-only list; withdrawn/expired material disappears from derivatives |
| Respond or use in arrangement | `openV2Action` → source inspection and consequence confirmation where declared | present but unverified | Keep source inspect first; route arrangement use to Plan owner, not generic Chat | Audience preview, explicit send, duplicate submission, and withdrawal/repair |
| Return | return registry keyed by source refs/viewer/unit | present but unverified | Keep/revalidate; preserve orientation without resurrecting stale content | Back after withdrawal and after private-save-only path |

**J2 owner dependencies:** source/share authority, Life People browsing decision, and Plan contribution semantics. Social consumption must be valuable before any reply is requested.

### J3 — arrangement → inspect → contribute/edit → owner readback → Home

| Step | Current path | Status | Keep/adapt/add decision | Required verification |
| --- | --- | --- | --- | --- |
| Open arrangement | `hrefForRootResource` currently maps `plan`, `occasion`, `commitment`, `opening`, and `recovery_instrument` to `routes.conciergeChat()` | adapt | Add an exact owner destination only after the Plan/Occasion lane names its canonical route; remove generic Chat fallback for that typed case | Arrangement opens in the Plans-in-Real-Life owner with same refs and audience |
| Ask before edit | Adjacent Plans design reports contextual Ask Vesper; Chat seed seam exists | present but unverified | Reuse target-preserving assistant entry; do not create a Home composer or second chat history | Contextual question does not mutate arrangement; answer retains target |
| Contribute suggestion | source contribution pipeline/runtime validates refs, grants, material, and audience | present but unverified | Keep contribution distinct from accepted edit; use existing receipt/owner handoff | Contributor receipt, owner visibility, no false accepted state |
| Authorized bounded edit | consequence confirmation hook exists; exact Plan command contract not proven here | blocked on owner decision | Plan lane defines command, authority, idempotency, and affected commitments; Home consumes readback | Accept/reject/stale/offline/double-submit; only affected participants see change |
| Owner readback and Home refresh | projection hooks support refresh; no journey proof | adapt | Bind Home refresh to accepted owner revision, not optimistic local text | Accepted state appears consistently for owner and participant views |

**J3 owner dependencies:** Plan/Occasion command contract and route; Home must not implement booking/rebooking or an alternate arrangement store.

### J4 — sample/onboarding → bring/ask → immediate value → exact Life continuity

| Step | Current path | Status | Keep/adapt/add decision | Required verification |
| --- | --- | --- | --- | --- |
| Inspect sample | Home v2 projection/mocks can supply a labeled demonstration | present but unverified | Keep sample as structured/nonpersonal fixture; never write personal memory on inspection | New account has no invented location, person, or preference |
| Try with yours | Home action/destination can seed Chat; capture boundary lives outside Home | present but unverified | Keep existing Chat/Capture entry and carry origin/target; do not add a new Home composer | Attachment enters the correct intake flow and can return |
| Ask versus Bring | `docs/systems/contribution-and-consequence.md` defines distinction; capture implementation is adjacent | present but unverified | Keep explicit gesture semantics; attachment alone is not durable retention | Cancel, ambiguous date/venue, extraction pending, answer-only, authorized Bring |
| Useful result and receipt | Life/intake routes and consequence contracts exist; exact mobile journey not proven | adapt | Show useful result first; then scoped receipt/Undo only when a write occurred | Undo and correction target exact source/record; no “all done” fiction |
| Exact Life opening | `life_projection/record.py` canonical refs; mobile `resourceDestination` supports Life/source fallback | present but unverified | Prefer exact artifact/intake/trip record; fallback honestly to archive only when unsupported | Life opens the retained original/record, not just the Life root |
| Later re-open | projection refresh and retained refs exist; restart/ready timing unproven | adapt | Preserve useful output and source status; no inference of attendance/enjoyment/preference | Pending/failed/withdrawn/reopened states; no new input required |

**J4 owner dependencies:** Capture/Chat owns intake and channel semantics; Life owns retained record; Home owns only the value projection.

## 4. First implementation packages

These are dependency-ordered packages, not permission to edit every listed file in one branch.

### Package A — fixture and contract harness (lowest risk)

- Define one shared New York fixture manifest for J1–J4: stable IDs for viewer, person, source, place/entity, possibility, arrangement, commitment, contribution, result, and retained record.
- Record which values are structured, human-authored, reusable research, personal adaptation, or bespoke; label simulated sources.
- Add or extend pure fixture tests for Home projection shape, destination mapping, and return-token composition. Avoid changing production routes in this package.
- Completion: a test can name the same object before and after a cross-root transition; no new database table or client store.

### Package B — exact destination seam

- In `rootProjectionNavigation.ts` / `resourceDestination.ts`, add only owner routes that Plan/Life/Entity explicitly declare and that can be covered by tests.
- Preserve the current safe-path allowlist and unsupported fallback. Do not convert every typed kind into a new screen.
- Completion: J1 entity, J3 arrangement, and J4 retained-record openings have exact or explicitly labeled fallback dispositions.

### Package C — return and readback verification

- Extend `rootProjectionReturnRegistry` and Home experience tests for exact restoration, revision mismatch/recomposition, 30-minute expiry, restart fallback, and viewer/audience changes.
- Add owner-revision-triggered refresh for accepted arrangement/contribution results; do not mark optimistic local state as accepted.
- Completion: all four journeys return to an honest state under changed, withdrawn, offline, and thin-data fixtures.

### Package D — bounded owner integrations

- Plan lane: canonical arrangement destination and contribution/edit command contract.
- Capture/Chat lane: target-preserving Ask/Bring entry and scoped receipt/Undo.
- Life lane: exact retained original/record ref and readback status.
- Home lane: consume these contracts through existing projection/actions; no domain writes in Home components.
- Completion: each owner has one request/read path, one result/receipt shape, and one accountable test owner.

### Package E — production economics and rollout evidence

- Measure cold result creation, unchanged reuse, and incremental refresh separately. Count root reads, provider/model calls, retries, cache hits, and media delivery.
- Reuse existing bounded producer budgets; add aggregate reuse/invalidation instrumentation before widening generation.
- Keep v2 flag-gated and compatibility fallback until native and journey acceptance passes.
- Completion: measured/estimated/unknown labels, latency/useful-result yield, and rollback scope are recorded; no paid experiment is implied.

## 5. Cross-journey test matrix

| Concern | J1 | J2 | J3 | J4 |
| --- | --- | --- | --- | --- |
| No implicit write on open | ✓ | ✓ | ✓ | ✓ |
| Exact source/object identity | place/possibility | original/share | arrangement/contribution | source/record |
| Audience and viewer scope | private | addressed/private/group | participant/editor | private/authorized |
| Return after unchanged read | ✓ | ✓ | ✓ | ✓ |
| Return after revision/withdrawal | ✓ | ✓ | ✓ | ✓ |
| Offline/pending/duplicate handling | optional keep | response/use | command | intake/receipt |
| Owner readback | retained possibility | source authority | accepted arrangement | Life record |

Minimum automated coverage should extend existing tests in:

- `travel-app/__tests__/components/home-root/HomeRootExperience.test.tsx`
- `travel-app/__tests__/utils/rootProjectionNavigation.test.ts`
- `travel-app/__tests__/utils/rootProjectionReturnRegistry.test.ts`
- `travel-app/__tests__/utils/resourceDestination.test.ts`
- backend root-projection, source-contribution, Life-record, and owning Plan/Capture tests identified by each lane

Run local tests in proportion to each package. Backend API changes require the workspace contract workflow (`scripts/sync-types.sh`, snapshot review, generated mobile types, and frontend typecheck); do not hand-maintain schema copies.

## 6. Production classification and generation policy

| Value type | Default treatment | Refresh trigger | Degraded fallback |
| --- | --- | --- | --- |
| Structured projection/layout | deterministic render | source/revision change | omit unit or use known prior projection |
| Human-authored contribution | retrieve with audience check | source correction/withdrawal | hide or show honest unavailable state |
| Reusable world research | cache/version by evidence | stale fact or explicit exploration | cite last known result or omit |
| Personal adaptation | bounded synthesis from authorized refs | relevant source/consequence change | structured recommendation without bespoke prose |
| Bespoke composition | generate only when it creates new value | meaningful input change | template/known result, never a hollow prompt |

Opening Home must not silently trigger a new model call for every card. A network refetch is not a generation event; an unchanged generated result is not free unless its upstream reuse is measured.

## 7. Non-goals and handback questions

Non-goals for this phase: booking or rebooking UI, a generic social feed, a second Chat system, an all-city content factory, generalized Occasion architecture, a repository-wide noun migration, and a permanent Home task queue.

Before implementation, return with answers to these bounded questions:

1. What exact existing owner stores a loose “Keep” possibility, and how is it distinct from Adopt/Plan?
2. What is the canonical route/ref for an arrangement and for a retained intake record?
3. Does Life People already satisfy “browse shared with you,” or is that a separately scoped extension?
4. Which command is an accepted edit versus a contribution, and what owner revision does Home read back?
5. Which source changes invalidate a Home result, and which can reuse it unchanged?

The next founder review should inspect one connected artifact and this map together. A polished Home scroll without exact owner destinations is not connected; a set of routes without a satisfying value-first composition is not the product.
