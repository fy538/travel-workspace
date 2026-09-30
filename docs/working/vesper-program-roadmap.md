---
doc_type: current_status
status: active
owner: founder / Orchestration lane
created: 2026-09-07
last_verified: 2026-09-30
why_new: Owns the existing program's lane boundaries and the Orchestration execution plan; specialist roadmaps own their own packages and receipts.
supersedes:
  - single-lane dispatch and current assignments in earlier versions of this roadmap
source_of_truth_for:
  - cross-lane implementation ownership and dependency boundaries
  - Orchestration lane execution order and system reassessment
depends_on:
  - ../decisions/2026-09-27-documenting-core-loop-and-one-composer.md
  - ../decisions/2026-09-28-collections-are-the-spine.md
  - ../decisions/2026-09-29-record-as-first-class-value.md
  - ../decisions/2026-09-29-life-model-occasions-collections-and-sharing.md
  - ../systems/contribution-and-consequence.md
---

# Vesper program roadmap

## Direction and current assignment

Build the complete product on the connected system already implemented.
The next execution model is **three autonomous implementation lanes in three
coordinated worktrees**, each containing the workspace and both independent
children. This file owns the boundaries between them and the work of
**Orchestration**, not a queue through which every other lane must ask permission.

The four moves remain **Make sense. Open possibility. Help it work. Carry
forward.** Keeping, enjoying and refinding a recognizable original are complete
value in their own right. Optional intelligence must add substance. Home returns
value for now and the anticipated future; Places opens the situated world;
Chat supports conversation and contribution; Life organizes the record through
Collections, Time, Places and People. Social participation and practical help
run through those experiences.

The accepted September 27–29 decisions amend older contracts where explicit;
they do not declare their runtime migration complete. No new booking execution,
automatic sharing, connected-inbox sharing, background-generation posture,
notification policy or deployment is authorized by this roadmap.

**Planning status:** the three lanes are scoped below, not started by this edit.
First establish the common committed baseline in section 3. Then each lane can
execute its own first assignment without waiting for the other two to finish.
No new coordination service, fourth integration lane or routine inter-chat
messaging is required.

## 1 Inspected baseline and unfinished product work

<a id="inspected-baseline-and-publication-state"></a>

September 30 inspection distinguishes implementation from publication and
acceptance:

| Repository | Observed revision | Meaning |
| --- | --- | --- |
| Canonical workspace | `7a5d434eb6025e792c0e1dd930d7d295a46f5304` | Includes prior consolidated decisions and roadmaps; current roadmap drafts are additional working changes |
| Existing delivery workspace | `73d9679409793f337be120bf9d6e39e27c966677` | Includes the subsequent integrated documentation-link repair |
| Backend main | `3c170d21fc0ca9231b956f2b9de7f9f195231768` | Home/capture follow-up and CI changes merged through PR #237 |
| App main | `87eceee24512d9086962eea5b844cef9d7bffbeb` | Home/capture follow-up and CI changes merged through PR #202 |

Workspace [PR #37](https://github.com/fy538/travel-workspace/pull/37) was still
open at the preceding publication check. The fresh GitHub request during this
rebaseline could not connect; its current status is **unverified**, not assumed
merged. Recheck it before choosing the launch baseline. Do not rerun old
credential repairs or reopen already merged child packages merely because
historical receipts describe those blockers.

The latest completed Strategy roadmap draft was inspected in its existing
product-direction checkout; the latest Technical draft was in the canonical
workspace. This rebaseline consolidates those roadmap contents here without
changing the source Strategy checkout. Reconcile their pending documentation
changes once before branching, rather than launching lanes from different
draft generations. Strategy-child Thesis/Model edits remain separate owned work.

| Area | Implemented foundation | Remaining work and owner |
| --- | --- | --- |
| Capture | Shared private composer, native extension host, retry/session custody, supported email attachment intake, original access | Supported-door delivery, failure/retry clarity and authenticated handoff: Orchestration D1 |
| Home | Source discovery/request/worker/readback connections, contextual continuation, current commitment facts, native hierarchy improvements | Useful recurring supply, complete receiving, full-scroll quality and recovery options: D2/D3 |
| Artifacts and Life | Source custody, original readers, owner references, Life projections and original receiving | Stable thing/component identity, typed family readers, catalog anchors, consumer collections and accepted Life model: Strategy |
| Context and research | Existing retrieval, bounded research pieces, jobs, generation infrastructure and publication fences | General selected-object capability, evidence fidelity, correct reuse and bounded maintenance: Strategy Technical |
| Places and practical help | Situated projections, entity pages, current place facts and owner-backed actions | Consume richer results coherently; useful current options and exact return: D2/D3 |

These are code/evidence boundaries, not design-completion percentages.
[H1](home-value-composition-execution-plan-2026-09-25.md) preserves the detailed
implementation receipts. Its complete native matrix remains MIXED; targeted
passes are not full acceptance. Real recurring supply, all-door authenticated
readback, signed extension behavior and some provider paths remain unverified.
Do not reconstruct completed Source/Home connections or build another generator.

## 2 Three lane ownership

| Lane and its execution roadmap | Owns | Does not own |
| --- | --- | --- |
| **Orchestration — this file** | Entry transport/custody integration; Home/Places composition and native presentation; practical live-engine adapters; caller-side navigation/return | Artifact identity, focused reader internals, Life/collection schema, public research or shared generation engine |
| **Strategy — [Artifact roadmap](artifact-experience-engineering-roadmap-2026-09-29.md)** | P0/P1 identity, components, typed readings, consumer collections; PC subject/catalog anchoring; P2 focused readers; P4 exact kept editions; Life and original-sharing/collection semantics in P6 | A second P3/P5 research/runtime implementation; root-feed composition; native capture transport |
| **Strategy Technical — [Adaptive context roadmap](product-map/adaptive-context-and-research-roadmap-2026-09-29.md)** | R0–R7 context/retrieval, bounded acquisition, evidence fidelity, prepared-result execution/reuse, budget/publication safeguards, relevance maintenance and evaluations | A second artifact store, collection owner, focused reader, Home/Places screen or notification policy |

**One implementation, several experience requirements.** Artifact P3 and the
shared research/runtime portion of P5 are fulfilled by Technical R1–R5; they
remain useful requirements in the Artifact plan, not competing work orders.
Artifact P4 owns durable kept editions; Technical R4 owns changing candidate
selection and prepared-result validity, consuming P4 when retention is required.
P6 is split: Strategy owns collections, original sharing/receiving and Life;
Orchestration owns their Home/Places placements. Technical R6 provides result
readback and consumer-conformance evidence, not its own mobile redesign.

### Code boundaries and shared files

Choose exact files at each lane's intake from these existing owner areas.
A directory is a starting point, not permission to rewrite every file in it.

| Boundary | Initial writer |
| --- | --- |
| App `native-capture/`, capture plugin/session modules, `components/inbound/`; backend inbound transport/security/email handling | Orchestration; artifact reconciliation and durable collection membership stay with Strategy |
| App `components/home-root/`, Places feed/map/root composition, `data/home.ts`, `data/placesProjection.ts`; backend Home/root/Places projections | Orchestration |
| Artifact/source open-target resolution, family renderer/reader, consumer collection and Life organization, subject/catalog identity | Strategy; place pages/facts remain existing domain owners, not automatically cultural-object capabilities |
| Backend `research_agent/`, selected-evidence adapters, shared preparation/job execution and reuse | Strategy Technical; a root composer consumes their output rather than implementing research |
| Lived-experience admission, surface treatment and practical owner adapters | Orchestration; shared research execution, retry/budget and result-publication changes stay Technical |
| App navigation infrastructure, shared design tokens, dependency manifests, global CI/governance tooling | Preserve by default; assign a bounded owner before a change spanning lanes |

Transport idempotency is not thing reconciliation. Catalog lookup is not general
research. Research recommendations are not current operational facts or
authorized commands. A shared UI component is not a new domain owner.

**Shared-file rule:** only the owning lane changes a semantic contract or its
implementation. Other lanes consume the landed version or keep an explicit
unsupported state. Avoid opportunistic moves/renames and cross-cutting cleanup.
If a task reveals a necessary change outside its owner, record the exact missing
interface in that lane's roadmap and continue its independent fallback work;
resolve a consequential boundary change at the next program checkpoint.
Do not edit the other lane's checkout or send it routine instructions.

Generated OpenAPI/type files are an exception to exclusive physical-file
ownership: every lane changing an owned API regenerates and reviews the complete
snapshot/projection/types in its own coordinated checkout. At landing, regenerate
against the combined backend and resolve consumers; never hand-merge generated
models. Separate domain migrations may proceed independently. The later landing
owner reconciles migration heads/order and validates the combined migration;
do not rename or rewrite another lane's already landed migration.

## 3 Prepare the common baseline once

Before implementation starts:

1. Preserve and reconcile the three latest roadmap drafts, accepted decisions
   and relevant pending owner-contract edits. Resolve workspace PR #37's actual
   state and the delivery-only link repair; do not assume local main equals
   remote main. Commit/land the intended shared starting tuple under the current
   publication authority.
2. Inspect `make worktrees`, branches, HEADs and dirty files in all three repos.
   Reuse suitable free coordinated lanes. Do not repurpose a read-only inventory
   checkout or another session's unfinished checkout by assumption.
3. Provision each execution checkout under the existing
   [workspace setup](../Workspace%20Repo%20Setup.md) and root AGENTS. A root-only
   app worktree is not sufficient: verify its own `travel-agent/` and
   `travel-app/` checkouts, matching intended bases, before any cross-repo command.
   Keep three independent Git histories; no submodules or canonical-child fallback.
4. Record the same starting workspace/backend/app SHA tuple in each lane's
   existing assignment. Select a descriptive `codex/` branch per lane. Reuse the
   worktree for follow-on packages rather than retaining a new branch per helper.
5. Check each lane's runtime manifest and `scripts/dev.sh --print-runtime`.
   Use isolated API/Expo ports, Compose projects, disposable test databases and
   caches. Reserve distinct simulator/device instances where capacity permits;
   otherwise only the device-dependent check waits. Do not restart another lane's
   services or repoint its app to a different backend.

After this one-time setup, lanes are autonomous. Each keeps current progress
in its own roadmap, not in all three. This file changes when priority or ownership
changes, not whenever another lane passes a test.

## 4 Interfaces and dependency order

The following are semantic seams to map onto existing contracts, not four new
services or an instruction to invent new wire schemas before inspecting owners.

| Producer | Minimum shared seam | Consumer behavior while unavailable |
| --- | --- | --- |
| Strategy P0/P1 | Stable source/thing/subject reference; selected component plus representation revision; typed reading and correction/withdrawal semantics | D1 uses existing supported custody/source references; Technical uses an existing-original adapter, with new identity modes disabled |
| Technical R1/R2 plus required safeguards | Prepared result and state; selected target; eligible input/dependency revisions; evidence fidelity; error/empty/stale treatment; supported action references | Strategy shows a useful original; D2 uses existing authorized supply. No generated placeholders presented as product value |
| Strategy P4/P6 | Exact retained-edition behavior and collection/audience operations, when adopted and implemented | Keep original-only and existing eligible receiving; disable unsupported retention/shared derivatives |
| Orchestration D2/D3 | Root caller context and return behavior; invocation of existing practical owner commands and current facts | Other lanes preserve existing navigation/actions; do not emulate a provider result or successful mutation |

**First parallel wave:**

- Strategy maps P0 early, then delivers the P1/PC/P2 foundation with original-first
  value and honest catalog fallbacks.
- Technical starts R0/R1 and an existing-original R2 path with first-producer
  safeguards. It can improve evidence fidelity and public-acquisition boundaries
  before new artifact identities land.
- Orchestration starts D1 against existing custody and proceeds with independent
  Home/Places improvements. It does not wait for catalog licensing, a new reader
  or broad research infrastructure.

Land the small additive P0/interface portion once ready; do not hold shared
interfaces until every family renderer is complete. Consumers adopt **landed
revisions**, not copied uncommitted code or a sibling branch that may change
under them. Typed fixtures can unblock presentation and adapter work but do not
prove the producer connection. Recheck owner state at receipt, publication and
readback where the existing contract requires it.

The next connected checkpoint combines a real supported input, Strategy's
reader and Technical's useful addition, with Orchestration's appropriate root
preview and exact return. This is a system connection checkpoint across several
representative families, not a decision to narrow Vesper to one behavior loop.

## 5 Orchestration execution plan

### D0 Rebaseline and prepare execution

**Current task:** reconcile these roadmaps, ownership, evidence and start order.
**Finish:** the three documents agree; each lane has a first assignment,
exclusions, dependency fallback and acceptance boundary. Execution preparation
in section 3 remains a separate step until actually performed.

Do not turn D0 into another architecture inventory or recurring acceptance-only
lane. The existing system and unfinished product work are sufficiently concrete
to begin bounded implementation after baseline preparation.

### D1 Finish supported capture delivery

**Outcome:** a supported contribution reaches durable custody with a clear
receipt and opens the same eligible original. Failure and retry do not require
the person to reconstruct their effort.

Work from H1's remaining capture evidence and current inbound/native code:

- Inventory actual door × file-format support, using existing contracts:
  in-app text/link/photo, external share, forwarded email and already supported
  structured attachments. Do not infer PDF/Wallet/HEIC support from “ticket.”
- Finish transport failure, account/session changes, duplicate attempts,
  cancellation and retry behavior. Preserve input and idempotency through the
  established custody path; do not introduce new cross-door thing identity here.
- Make rejected email bundles and unsupported files explicit. The inspected
  email path rejects the bundle on an unsupported attachment; partial admission
  is a separate reviewed behavior change, not a silent fix. Preserve scanner/
  security requirements and clearly bound any unsupported format.
- Connect receipts and open actions through the current source resolver,
  adopting Strategy's stable target when landed. Ordinary capture must work
  before model recognition or catalog lookup finishes.
- Resolve native extension signing/entitlements when the required access is
  available. The last device blocker was a team/provisioning mismatch; verify
  credentials before another expensive build. Real email-provider configuration
  and authenticated mobile readback need their own evidence.

**Acceptance:** current supported paths survive retry and account changes; a
real authorized backend read returns the retained original; unsupported paths
show honest failure and recovery. Separate in-app, extension, email-provider
and signed-device results. Mock/DB-only checks do not establish all-door delivery.

**Implementation checkpoint — September 30:** app `1f041a30a` adds durable
recovery for ordinary iOS in-app private Keeps. It journals text/photo bytes in
the app-private protected store before Intake dispatch, binds the record to the
backend owner plus the Clerk session generation, replays the same key when the
common composer is reopened, and clears local bytes only after terminal
current-owner readback. This reuses Intake v2 and the existing capture journal;
it does not cover a seeded OS-share handoff, Android, a Home-level resume
indicator, or signed/live backend acceptance. Focused app suites passed **51/51**,
production/test TypeScript checks passed, and nine Foundation journal-harness
scenarios passed. Native iOS build/device behavior remains **unverified**.

**OS-share identity correction — September 30:** app `bc1b54fac` fixes a
Clerk-subject versus backend-owner UUID mismatch in the opted-in native host.
It preserves the existing Clerk-keyed extension journal (so pending local
records remain discoverable), resolves the internal owner through authenticated
`GET /api/me`, and validates Intake receipts against that UUID. Six focused
Jest suites now pass **65/65**, including the external-to-internal owner mapping
and fail-closed resolution path. App `0ff582abf` adds an in-place retry after
transient profile/journal-read failure while the same Clerk lease remains
current, preserving the incoming draft and preventing duplicate retry dispatch.
Native/device and live-backend acceptance remain unverified.

**Host Keep → exact original — September 30:** app commit `495955944` connects
the in-app private Keep receipt to the existing owner-verified Intake/Life
reader. “Open original” appears only when the lead source is currently eligible
and has a stable content revision; navigation carries the submission, exact
source ID/revision, and ephemeral Home/Places return token. The reader rechecks
current ownership, custody, expiry and the requested revision, and the route
never receives a storage reference. This closes the host-app original-open
connection only: the native extension still has no host-app navigation, and
signed-device/authenticated live readback remain unverified. Apple documents
`NSExtensionContext.open` for Today and iMessage extensions, not the Share
extension point ([Apple API](https://developer.apple.com/documentation/foundation/nsextensioncontext/open%28_%3Acompletionhandler%3A%29)); keep the extension receipt in-place rather than adding a private-API launch workaround. Focused coverage
passed **40/40** across the receipt, route and share-capture suites; production
and test TypeScript checks and app docs checks passed. Targeted ESLint had zero
errors and six existing warnings; native visual/device acceptance was not run.

**Unsupported archive preflight — September 30:** app commits `89f60c55b` and
`0b6a01d02` reject generic ZIP before creating custody, including common
`application/zip`, `application/x-zip` and `application/x-zip-compressed`
declarations when the OS omits a filename. In the shared composer, an
unsupported archive remains visible for explicit removal; supported text can
still be kept afterward. The backend remains the byte-level admission
authority. App `2d4aec6be` also translates its raw server-side ZIP refusal into
the same actionable recovery guidance in the compatibility share route.
Focused intake, receipt, extension-host and route suites passed **75/75**;
production/test TypeScript, surface docs and targeted lint passed (six existing
warnings). This closes one unsupported-file feedback gap only; it does not
establish every door's format coverage, email sender recovery, or signed-device
acceptance.

**Multi-photo Keep receipt — September 30:** app commit `3d866cd03` replaces
the immediate receipt's lead-photo-only preview with a sequential viewer over
the selected images in Intake source-ordinal order. It requests only the
currently selected original through the existing owner media reader; the host
app's **Open original** carries that exact source and revision, and the share
extension previews the same selection without claiming it can open Vesper.
Focused receipt/session/native-host coverage passed **45/45**, including all
16 supported images, one-at-a-time reads, exact selected-original routing,
revoked-source refusal and owner-session fencing. Production/test TypeScript,
surface docs and targeted lint passed (two existing test-mock warnings). A
native visual capture was not run: Metro's lane port `53177` had a listener but
did not answer its status endpoint, so the registered runner correctly stopped
at preflight. Signed-device authenticated readback remains unverified; this is
not an excuse to block subsequent code work.

**Private audio Keep receipt — September 30:** app commit `911f1aa79` reuses
the authenticated foreground audio player in both in-app private-receipt paths.
Supported retained recordings appear in source order; playback is available
only for the focused in-app route and releases on blur, app background,
owner-session loss, removal, expiry, or unmount. Unsupported/missing originals
remain non-playable, and the native Share Extension still does not gain audio
playback or a broader input contract. No backend/API change was needed.
Focused receipt, composer/session and source-reader/share-route coverage passed
**112/112**; production/test TypeScript, surface docs, `git diff --check`, and
targeted ESLint (zero errors; six existing warnings) passed. The component
catalog check failed on the unrelated unregistered
`components/ui/authored-note-quote.tsx`. Native visual QA stopped in preflight:
CoreSimulatorService failed and the Maestro lock directory returned `EPERM`;
real authenticated playback and device/visual acceptance therefore remain
unverified.

**Independent work when blocked:** in-app authenticated/native acceptance,
email transport failure semantics and D2's existing-supply composition. The
native share receipt stays in-extension; do not add unsupported host-launch
workarounds.
Do not block the whole lane on signing, an unavailable provider or an unapproved
sharing policy. No Chat redesign or Life implementation belongs to D1.

### D2 Make Home and Places complete receiving surfaces

**Outcome:** both roots deliver substantial, navigable value from current
authorized supply, with the polish of the adopted design references.

- Compare the current registered Home/Places designs and latest adopted handoffs
  with actual section/row coverage. Implement missing supported sections and
  interactions, not just another screenshot or first-viewport crown.
- Home balances what matters now with immediately engageable possibilities,
  useful records and eligible human contributions. A return from a trip does
  not make the feed exclusively retrospective. No generated-card quota, routine
  input prompt or speculative personality interpretation.
- Places prioritizes situated discovery, spatial context and practical relevance.
  Consume the same underlying objects/results through a place-appropriate view;
  do not copy Home or create a second research pipeline.
- Consume Technical's prepared results and Strategy's reader/collection seams as
  they land. Keep originals recognizable; navigate to the exact object/component
  and restore root position on return. Show useful original/current-owner
  fallbacks for no result, failure, staleness or changed access.
- Add social placements from existing permitted originals and later P6 contracts.
  Preserve authorship, intended audience and distinct perspectives. No automatic
  shared filing, equal-effort requirement or unsupported shared synthesis.
- Complete hierarchy, density, image treatment, component spacing, large type,
  touch behavior, loading/empty/error states and full-scroll continuity. Frontend
  polish is part of completion, not a later optional pass.

**Acceptance:** representative sparse, ordinary, social, returned and live states
have useful real-owner content and working actions. Review full-scroll native
output against the correct adopted reference/build/data source. Name unavailable
supply and unsupported components; fixture parity alone does not establish
backend delivery or recurring value.

**Current lane increment — 2026-09-30:** app commit `d8e30d7c2`
(`codex/home-value-delivery`; based on workspace `f6ebfacb`, backend
`3c170d21`, app `87eceee`) applies the root contract's demoted Places
standfirst to the four-root renderer only. Ordinary root browsing keeps the
compact scope identity and begins with the admitted field; a cold start or an
explicitly entered scope may retain the standfirst. Home-depth and the legacy
workspace keep their prior behavior. Focused Places tests passed **32/32**,
app typecheck passed, the registered scenario check passed (**31 IDs**), and
the external Places design-reference hashes verified. Focused lint had no
errors and one existing unused-`spacing` warning in `PlacesWorkspace.tsx`.
Native capture remains **unverified**: CoreSimulatorService was unavailable
(`xcrun simctl list devices booted` could not connect), so the showcase surface
has not received a visual verdict. This closes only the scoped composition
change; D2 remains active. **Next:** capture the registered Places surface when
the simulator is available, then continue the full-scroll and real-owner D2
gaps without changing the compatibility workspace.

**Additional current lane increment — 2026-09-30:** backend commit
`0caed6e1a` and app commit `998afc80f` remove the redundant generic Occasion
row only when the selected Home commitment is canonically linked to that
Occasion. The distinct participant/social row remains visible and leads with
the group context; copy-similar but unlinked owner objects remain independent.
Backend focused composition/root-projection coverage passed **122 tests**;
Home UI coverage passed **62 tests**, app typecheck and test-contract typecheck
passed, Ruff and `make docs-check` passed. Targeted ESLint had no errors and
retained one existing `HomeRootV2UnitRenderer.tsx` max-lines warning. Native
visual acceptance remains **unverified**: Expo Metro started on the assigned
lane port, but the polish doctor could not initialize CoreSimulatorService and
could not create its run lock in the sandboxed worktree. No device screenshot
or visual verdict is claimed. This closes only the linked-duplicate composition
defect; D2 remains active.

**Independent work when blocked:** use existing Source/Place/commitment/authorized
social supply; finish root layout, navigation and failure treatment. Do not
rewrite P2's reader or generate pretend enrichment to fill a design.

**Additional current lane increment — 2026-09-30:** app commit `b233cb013`
(`codex/home-value-delivery`; workspace baseline `eea30b6c`, backend
`ea8515849`, app base `e8ad47537`) replaces the grounded-empty Places dead end
with a direct **Search Places** entrance. It opens the current supported scope,
or the existing anywhere-search mode when no supported scope is available; it
does not ask for an upload, wait for travel, request location, or create a
capture. Focused Places state tests passed **25/25** (including both scope
cases), app typecheck and targeted ESLint passed, the registered scenario check
passed (**31 IDs**), and `make docs-check` passed. Native validation then
completed through the documented local development setup: the opt-in iOS
prebuild generated the extension pod target, `pod install` succeeded, and the
iPhone 16 Pro simulator build/install passed with Sentry source-map auto-upload
disabled locally. The default capture-host-off project was restored and pods
reinstalled afterward; release capture delivery remains disabled. The
registered `places-workspace` capture produced **7/8** screenshots. The one
failed flow completed its Places search/readback checks, then failed a
`home-v2-screen` assertion immediately after a forced navigation to Plans; its
failure snapshot showed the Plans surface onscreen, so the remaining evidence
is a scenario timing/selector issue to investigate separately, not a Places
failure. The cold screenshot showed ready Lisbon/Rome guides and therefore did
not exercise this new zero-content CTA. The CTA itself is functionally covered
by the two focused tests; no screenshot of that exact state is claimed. The
external canonical design bundle was not supplied (`externalCanonVerified=0`),
so no strict design-intent verdict is claimed. This closes only the empty-state
entrance defect; D2 remains active. **Next:** continue D2's real-supply and
full-scroll implementation independently; keep the Plans post-navigation
capture issue bounded and do not wait on it to continue supported Home/Places
work.

**Additional current lane increment — 2026-09-30:** backend commit
`51d8f7334` and app commit `44f65c39a` carry the existing approved starter
guide into the ranked Places feed when the user is in the `starter`/Anywhere
posture and no scoped guide is available. It appears as “A guide to start
with,” opens its exact dossier, and is omitted when the approved corpus has no
display-ready guide. The app mock uses that same dossier rather than invented
content; no new generator, endpoint, schema, permission path, or parallel
content store was added. Backend feed tests passed **20/20**; focused app
component/mock-feed tests passed **55/55**, app typecheck passed, and local
pre-commit checks passed in both child repos. A registered cold-start iPhone
capture completed **1/1** and opened the exact Lisbon guide; its screenshot is
the initial starter-city viewport, so it does not independently establish the
new section's below-fold visual placement. The external canonical design bundle
was unavailable, so no strict design-intent verdict is claimed. This closes a
real receiving gap in the starter feed, not D2 as a whole; continue with the
next independently useful Home/Places slice rather than reopening planning.

**Additional current lane increment — 2026-09-30:** app commit `862934e2d`
distinguishes a friend-authored Place note from a composed editorial reading.
The exact human-authored words now appear as a short quoted Roman body, with
attribution, Place context and the precise Place Door preserved. It does not
rewrite source text, alter audience/authorization, change feed admission or add
a new content system. The full Home root screen suite passed **33/33**, app
production typecheck and the 31 registered polish-scenario ID check passed;
targeted lint had no errors and retained the existing renderer max-lines
warning. A native screenshot of this precise owner-note state was not captured,
so visual acceptance for that state remains unverified. This closes a known
Home hierarchy defect without closing D2.

**Additional current lane increment — 2026-09-30:** app commit `b2d52f5a3`
uses one shared authored-note treatment across Home and Places. The same
recipient-consented Place message is now legible as attributed, quoted Roman
body text in the scoped Friends section, rather than muted mono metadata; the
exact venue door and relationship-owner audience gate are preserved. The
Places `PlacesSectionFeed` suite passed **52/52**, Home root screen suite passed
**33/33**, app production typecheck and the registered polish-scenario check
(**31 IDs**) passed. Targeted lint had no errors and retained the existing
Home renderer max-lines warning. Native visual acceptance is unverified:
`xcrun simctl list devices booted` could not connect to CoreSimulatorService, so
no screenshot of either exact note state is claimed. This closes a cross-root
receiving inconsistency, not D2.

**Additional current lane increment — 2026-09-30:** app commit `c6e6ae49c`
names Home's Life receiving doors by record family (“Open the reading in Life,”
“Open the moment in Life,” “Open the record in Life,” and corresponding
original/capture/attachment/receipt labels) instead of presenting one generic
“Open in Life” action for every record. The existing canonical resource
resolution, exact resource argument and Home return token remain unchanged; no
backend, wire or authorization behavior changed. The focused Home root renderer
and screen suites passed **50/50**, app production typecheck passed, registered
design-reference and polish-scenario checks passed (**31 IDs**), and targeted
lint had no errors with the existing renderer max-lines warning. The registered
native Home quiet flow retried without producing screenshots and was stopped;
native visual acceptance remains **unverified**. This closes one Home
continuation-clarity refinement, not full-scroll D2 acceptance. Continue with
supported Home/Places supply and full-scroll behavior independently.

**Additional current lane increment — 2026-09-30:** app commit `d06dc229f`
keeps Home composition provenance to one visible line, so a long source label
does not push its reading into report-like density. The complete source names
and live/uncertain/stale qualification remain in the accessible label, and
freshness remains separately visible; the existing source-inspection action is
unchanged. Places and non-Home compositions keep their previous presentation.
The composition-renderer and Home-root suites passed **46/46**, app production
typecheck passed, targeted lint passed without new warnings, and registered
surface scenario IDs passed (**31**). The native quiet-flow attempt did not
produce screenshots, so this has no visual acceptance claim. This closes the
long-Home-provenance-line refinement, not D2 full-scroll acceptance.

**Additional current lane increment — 2026-09-30:** app commit `bde5eb165`
labels a Home `life.open` bridge that still carries a legacy Trip reference as
“Open trip details,” matching the exact Trip detail route selected by the
existing navigation resolver. It no longer promises to open the Life root
while sending the person to Trips. The capability, exact Trip reference and
Home return context are unchanged. Home renderer and route-resolution suites
passed **82/82**, app production typecheck and registered surface checks passed
(**31 IDs**), and targeted lint had no errors with the existing Home-renderer
max-lines warning. Native capture for this copy change was not completed; no
visual verdict is claimed. This closes one false-root-label mismatch, not the
remaining D2 receiving and full-scroll work.

**Additional current lane increment — 2026-09-30:** app commits `3409399e1`
and `d47a8be1c` extend the same Trip-door correction to direct Home resource
doors. A legacy owner path now says “Open trip details,” and an otherwise
allowlisted generic Trips path cannot be mistaken for a Home-root destination:
the renderer follows the concrete `trip` owner and agrees with
`hrefForRootResource`, which routes to Trip details. The Home renderer and
route-resolution suites passed **84/84**, app production typecheck passed, and
targeted lint had no errors; it retains the existing renderer max-lines
warning. No native visual verdict is claimed for this copy/door correction.
This closes a route-label consistency defect only; D2 receiving and full-scroll
acceptance remain active.

**Additional current lane increment — 2026-09-30:** app commit `0eb31d483`
removes a false exactness claim from the Home action-receipt door. The current
resource resolver opens the Life root for `action_receipt`; Home now says
“Open in Life” rather than promising a receipt-specific reader that does not
exist. The focused Home renderer suite passed **21/21**, app production
typecheck passed, and targeted lint had no errors with the existing
renderer-size warning. This is a truthful-door correction, not an exact
receipt-reader implementation or D2 completion.

**Additional current lane increment — 2026-09-30:** app commit `5bb78d2de`
aligns a Home Person resource door with its actual destination. Older Person
refs may carry `/you` as their canonical path, but Home's resource route opens
that exact person's profile; the door now says “Open profile” and preserves the
existing Home return token. The Home renderer and root-navigation suites passed
**87/87**, app production typecheck passed, registered Home design references
and scenario IDs passed, and targeted lint had no errors with the existing
renderer-size warning. App commit `0894cc819` also names the destination of a
saved-place resource door as “Open saved places,” matching its actual
Places-owned collection route and preserving the Home return token. After that
change, the renderer and root-navigation suites passed **89/89**, app typecheck
passed, and targeted lint had no errors with the existing renderer-size
warning. No native visual verdict is claimed for these copy and route-label
corrections. D2's broader receiving and full-scroll acceptance remain open.

**Additional current lane increment — 2026-09-30:** backend commit
`fd0013758` and app commit `c97db7847` make a fresh Anywhere Home read use the
existing approved Places starter guide when it has a readable preview. Home
shows the guide's own title and preview, verifies the exact dossier through
`source.inspect`, opens that dossier in Places, and suppresses the redundant
generic Anywhere row. If no display-ready guide exists, the fallback remains a
simple “Explore Places” door. No user-interest claim, generation, endpoint or
new content store was added. Places' no-lead state now gives a direct
search/map starting point and does not render the owner diagnostic. Focused
backend coverage passed **7/7**, Ruff check/format passed, the Places root
component suite passed **10/10**, and focused Home-renderer/exact-dossier-route
coverage passed **2/2**; both child-repo pre-commit hooks passed. Native visual
acceptance remains **unverified**: CoreSimulatorService again refused the
registered-device query, so no screenshot or design-parity verdict is claimed.
This closes a cold-start receiving and empty-state clarity gap only; D2 remains
active. Continue with existing-supply coverage and full-scroll/real-owner
acceptance independently of the simulator blocker.

**Follow-up correction — 2026-09-30:** backend commit `c32baddc9` removes the
separate Home starter-guide query from that increment. The canonical Places
feed already selects and carries the approved Anywhere guide; Home now consumes
that owner once through its existing contextual-Places adapter. The generic
“Explore Places” row is removed only when that same context has a source-backed
dossier reading, and remains when it does not. The exact `source.inspect`
evidence requirement and Places dossier destination remain intact. The
combined Home portfolio regression passes as part of **87/87** tests in
`test_home_portfolio.py`; Ruff, formatting, backend pre-commit hooks and
`make docs-check` passed. This is a consolidation correction, not a second
starter-content implementation; native and authenticated owner-readback
acceptance remain unverified. Detailed evidence is in the [H1 execution
plan](home-value-composition-execution-plan-2026-09-25.md).

### D3 Make practical help part of the same system

**Outcome:** what is happening now changes the useful options and actions across
the same Home/Places experience, without reviving the legacy booking product.

- Trace current plans/commitments, place constraints and situational changes
  through existing domain producers, lived-experience admission, projection,
  native action and owner readback.
- Fill missing useful option evidence where a current authorized provider/domain
  path exists. A renamed CTA or an alternative's name does not resolve H1's
  recovery-quality gap. The inspected venue-alternative tool is not a transport
  rerouting capability; scope such gaps honestly.
- Keep public researched possibilities distinct from current availability, cost,
  hours, commitment state and executable changes. Technical supplies bounded
  research; the operational owner remains responsible for practical truth.
- Connect permitted review/confirm/act/return behavior through existing commands.
  An outbound booking link is allowed only as a link, not an executed booking.
  Preserve the person's choice and do not infer obligations or attendance.
- Reassess generation supply and surface behavior together: appropriate later
  evidence may improve an option, but should not rewrite the original or silently
  create monitoring. Existing initiative/notification authority still applies.

**Acceptance:** a useful ordinary near-term situation and a material change
reach current owner-backed options, correct action outcomes and exact return.
Expired/unavailable facts stay distinguishable. Cover the meaningful changed
contract and failure path; do not treat one synthetic ferry story as the product.

**Independent work when blocked:** improve supported current-place/commitment
paths and disclose unsupported provider capabilities. Record the exact external
gap without building a parallel operational subsystem or pretending completion.

## 6 Autonomous execution and landing

Each lane starts by reading its roadmap, the ownership section above, root and
affected child AGENTS, Task Intake and relevant owner contracts. It then owns
diagnosis, implementation, focused verification, review corrections and delivery
of its selected outcome. Ordinary debugging does not need an orchestrator reply.

- Keep **one active coherent assignment per lane**, with bounded internal
  subagents only when delegation is authorized and writes are disjoint. Three
  lanes is a capacity limit, not a reason to invent work or run three native
  builds simultaneously.
- The owner updates only its own roadmap's current assignment: exact base tuple,
  owned files/interfaces, finished behavior, remaining gaps and next action.
  Use existing PRs and receipts; no new daily report files or duplicate trackers.
- At assignment start and a meaningful interface/landing checkpoint, inspect
  landed main and the required dependency. No constant polling or direct chat
  relay. If absent, take the named independent work; escalate only a genuine
  product/authority choice or incompatible boundary.
- Complete long slices without status chatter. Checkpoints are a working result,
  a consequential blocker and a reviewed finish. A helper's completion is not
  automatically a reason to redispatch or stop the owning lane.
- Integrate additive interfaces and complete useful increments while the next
  part proceeds. Do not merge every tiny commit, but do not keep completed work
  for weeks until all three roadmaps finish. If a dependency cannot land, name
  the specific blocker and stop adding dependent branch-only work.
- Each owner lands its own slice; Orchestration is not a required manual relay
  for ordinary merges. Serialize actual landings onto shared main, recheck the
  current base and affected compatibility, and follow the existing lane/CI policy.
  Land required child changes and then the workspace's matching contract/lock
  tuple. Never advance another session's checkout or overwrite its lock blindly.
- Publishing, merging and deployment use their actual authorization. Passing a
  local subset does not waive required hosted checks. A complete worktree can be
  reused after landing; retiring it follows the existing recovery-safe lifecycle.

### Proportionate verification

Use focused checks during iteration. For a landing candidate use
`make verify-changed WORKSPACE_BASE_REF=<base> AGENT_BASE_REF=<base> APP_BASE_REF=<base>`
with explicit bases in that coordinated lane. API changes require
`./scripts/sync-types.sh`, review of snapshots/generated consumers, and
`make api-coverage-check`. Current root/child AGENTS and the
[CI Plan](../reliability/CI%20Plan.md) govern actual required checks.

`make verify` is the full diagnostic/release suite, not a mandatory rerun after
every push. Native acceptance follows visible behavior changes; confirm runtime,
persona, data source and reference before capture. Disposable DB tests require
explicit opt-in. Keep exact commands, revisions and passed/failed/blocked/unrun/
stale boundaries; use existing measurement tooling. Never claim a five-minute
merge guarantee from this workflow or erase tests just to meet a slogan.

## 7 Reassessment and scope control

Reassess after the first shared interfaces, the first connected useful result,
and each complete D/P/R outcome—not every ordinary code change.

Ask: is the received result worth opening; is the original useful without AI;
does context improve it; how much effort remains; does social participation
benefit a thin recipient; are current practical claims dependable; and did we
reuse the correct owners? Review original-only and enriched experiences as
different valid modes. Track finished outcomes, rework, blocked time, generation
cost/latency and founder intervention, not commits or agent utilization.

Catalog rights, unresolved cultural/collection owner choices, shared derivative
retention, connected-inbox policy, automatic preparation and notification cadence
retain their explicit decision boundaries. Record which behavior is blocked and
continue independent supported work. These are not blanket reasons to stop all
three lanes or permission for an agent to decide new product policy.

## 8 Research basis and history

The worktree recommendation follows official [Codex worktree guidance](https://developers.openai.com/codex/app/worktrees/)
and [Git's worktree documentation](https://git-scm.com/docs/git-worktree):
separate checkouts permit parallel branches; they do not settle application
ownership or isolate external runtimes. Our three-repository setup therefore
needs coordinated child checkouts and separate runtime assignments.

[Fowler's integration guidance](https://www.martinfowler.com/articles/continuousIntegration.html)
distinguishes textual from semantic conflicts and warns that pulling main without
landing one's own work does not prevent divergence. Our application is a
bounded-slice landing practice, not a claim of strict continuous integration or
evidence that exactly three agents is optimal. The lane count is the founder's
chosen capacity. Explicit owners, additive interfaces and timely landing should
reduce coordination; measure the result rather than assume a speedup.

H1 remains the detailed implementation/evidence reference, not a fourth active
queue. Earlier program wording is preserved in
[the pre-rebaseline version](https://github.com/fy538/travel-workspace/blob/73d9679409793f337be120bf9d6e39e27c966677/docs/working/vesper-program-roadmap.md)
and the [September 27 archive](../archive/vesper-program-roadmap-history-through-2026-09-27.md).
The [integration roadmap](complete-system-integration-roadmap-2026-09-05.md)
is technical reference, not another schedule. This update changes planning and
ownership only; it is not new runtime, device, provider or consumer evidence.

## Historical link compatibility

These anchors preserve older references, not old queues.

<a id="2-inspected-baseline--september-22"></a>
<a id="2-inspected-baseline--september-8-after-reliability-landing"></a>
Historical baselines: [September 22](../archive/vesper-program-roadmap-history-through-2026-09-25.md#2-inspected-baseline--september-22)
and [September 8](../archive/vesper-program-roadmap-history-through-2026-09-25.md#historical-september-8-reliability-and-acceptance-evidence).

<a id="4-current-package-register"></a>
<a id="6-coordination-completion-and-next-system-review"></a>
<a id="7-current-acceptance-round--dispatched-september-8"></a>
Historical [package register](../archive/vesper-program-roadmap-history-through-2026-09-25.md#4-current-package-register),
[system review](../archive/vesper-program-roadmap-history-through-2026-09-25.md#6-coordination-completion-and-next-system-review)
and [acceptance round](../archive/vesper-program-roadmap-history-through-2026-09-25.md#7-current-acceptance-round--dispatched-september-8).

<a id="connected-dogfood-experience"></a>
<a id="current-round--meaning-based-discovery-and-exact-original-receiving"></a>
<a id="execution-order-and-event-triggered-reviews"></a>
Historical [connected experience record](../archive/vesper-program-roadmap-history-through-2026-09-25.md),
[discovery/receiving round](../archive/vesper-program-roadmap-history-through-2026-09-25.md#current-round--meaning-based-discovery-and-exact-original-receiving)
and [execution order](../archive/vesper-program-roadmap-history-through-2026-09-25.md#execution-order-and-event-triggered-reviews).
