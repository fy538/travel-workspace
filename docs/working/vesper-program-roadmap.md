---
doc_type: current_status
status: active
owner: founder / coordination task
created: 2026-09-07
last_verified: 2026-09-29
why_new: Owns the single live cross-lane execution queue, accountable package assignments, and system reassessment without duplicating product or implementation contracts.
supersedes:
  - current assignments and sequencing in the historical program and Integration roadmaps
source_of_truth_for:
  - cross-lane program priorities and accountable assignments
  - cross-lane dependency routing and system reassessment
depends_on:
  - ../decisions/2026-09-06-reconcile-consumer-strategy.md
  - ../decisions/2026-09-26-multiplayer-direction.md
  - ../decisions/2026-09-27-documenting-core-loop-and-one-composer.md
  - ../systems/four-root-loop-object-surface.md
  - ../systems/contribution-and-consequence.md
---

# Vesper program roadmap

## Direction and immediate priority — September 29

Build the complete product on the connected system already implemented.
**Implement the accepted horizontal capture/share experience from the connected
Home checkpoint, retaining the specific Home quality/supply gaps below.**
Home is not fully accepted: recovery still lacks a useful option comparison.
Landing the published Home package is a separate delivery task, not a reason to
redispatch its completed connections or
wait on every unfinished design.

The four moves remain **Make sense. Open possibility. Help it work. Carry
forward.** Home returns value for now and the anticipated future; Places opens
the situated world; Chat supports conversation; Life organizes what can be
revisited. Multiplayer and practical adaptation run through these experiences.

The [September 26 multiplayer direction](../decisions/2026-09-26-multiplayer-direction.md)
and [September 27 core-loop/composer decision](../decisions/2026-09-27-documenting-core-loop-and-one-composer.md)
now sharpen the entrance: documenting for oneself or others, through one
composer with many doors. Chat is a door, not a compulsory gateway. Immediate
benefit, private Keep with Undo, explicit audience and provisional interpretation
must coexist. This is not diary homework or a return to booking execution.

Those two decision files are unchanged snapshots brought from the concurrent
design checkout into this execution lane on September 27. Their accepted
rulings constrain the next implementation; their presence does **not** mean the
owner contracts, schema, runtime or all design boards have been updated.
Their pending recommendations remain pending.

This file owns the only current dispatch queue. The
[H1 package](home-value-composition-execution-plan-2026-09-25.md) owns implementation
detail and current evidence; the
[integration reference](complete-system-integration-roadmap-2026-09-05.md)
owns supporting technical guidance, not another schedule.

## Inspected baseline and publication state

The recovery work is merged on remote main; the subsequent Home package is
published but **not merged**. Remote branch heads and all three PR states were
rechecked on September 28; the table below is the published baseline, not a
claim that the local follow-up has shipped.

| Repository | Merged recovery baseline | Published Home candidate | Open PR |
| --- | --- | --- | --- |
| Workspace | `6ef3dca09be2b4ea40c83ae21d8cbf112ee17f24` (#36) | `a73e9d2348c07b398a91a4aee3733cfca4485252` | [#37](https://github.com/fy538/travel-workspace/pull/37) |
| Backend | `c8c9f578594a98beb41300c1a780f86ebb30eca4` (#233) | `c50b2286e9fcb477d015d7df20bcfdcce791f8b6` | [#234](https://github.com/fy538/travel-agent/pull/234) |
| App | `43225df35a01295993def384b5958c53ab8f1c8b` (#201) | `551e2a94b1ef58137a2fa7b3e309b245571e7e17` | [#202](https://github.com/fy538/travel-app/pull/202) |

### Live lane/PR reconciliation — September 29

A fresh read-only GitHub check confirms PRs #37, #202, and #234 are still open
and report `BLOCKED`; their published heads remain the revisions in the table.
The workspace PR's `Contract and golden paths` check is failed because the
private child checkout cannot authenticate; its Maestro configuration check
passed and the smoke was skipped. App and backend checks passed on their
published heads. Those results do **not** cover the current local follow-ups.

The coordinated product-code lane was at workspace `598422eb`, app `d7b640824`,
and backend `b4f49810e` during this refresh; relative to the published lane
branches it stood **49 / 60 / 8 commits ahead** before this workspace-only
roadmap update. The three PRs remain open and blocked at the published heads in
the table above. Current `origin/main` is an ancestor of all three product-code
heads, so no rebase is needed. The local follow-ups remain unpublished; do not
merge the older PR heads and describe later lane work as included. Before
closeout, run the coordinated gate on the intended tuple, resolve or record its
exact blocking boundary, then publish the current heads and refresh their
checks. The founder's previously recorded publication/merge authority remains
in force; it does not turn failed or skipped checks green.

**Coordinated local gate — September 29:** `make verify` ran on workspace
`322c08b0`, app `d7b640824`, and backend `b4f49810e`. Workspace doctor passed;
the backend structural checks reached the catalog gate, which failed because
the 14-day runway requires at least three active rows per band on 2026-10-12
and the reviewed catalog currently has `season=0, here=0` for that date. Backend
tests and app checks were not reached. This is a real data-gate failure, not a
green or an infrastructure crash. Do not weaken the checker or invent
seasonal/local entries to unblock integration; refresh those bands from
reviewable sources under the World Foundry operating contract, or retain the
failed boundary and continue independent work. No publication or merge follows
from this run.

The coordinated `codex/home-value-delivery` lane owns the Home candidate in all
three independent repositories. Workspace `1f4a9e5` contains the local roadmap
and accepted-decision rebaseline beyond the published tuple. App `332e77523`
adds reading clearance, quieter provenance, readable comparison rows and a
lighter original-reader door. App `64961a9cf` completes the next H1-A patch:
useful editable Home-to-Chat questions, readable/removable source context and
draft preservation without starter prompts reappearing. Its 102 focused tests,
app gate, 48 backend owner-grounding tests and three targeted native reviews
passed. These bounded reviews retain content/hierarchy residuals; the full
matrix remains MIXED. Backend `a8e87e64c` and app `97e0d0ac9` add current commitment
facts without booking inference, productive state typography, explicit compact-row
continuation and quieter provenance. They passed 140 backend and 48 focused app
tests, the app gate, and four bounded native self-reviews including Live XXXL.
Minor content/hierarchy findings remain. All these follow-ups are local, not
published or merged, and need the coordinated gate before publishing. H1 records
exact evidence and remaining findings; do not inherit full acceptance from a
targeted native pass.

Backend `539edb00d` bounds long owner text at the Home projection boundary without
changing canonical records. App `af8a126af` clarifies Returned/recovery fixtures
and fixes the native draft-replacement test. 143 backend tests, 70 focused app
tests and the app gate passed. Returned and recovery-to-Chat native reviews
passed their bounded assertions; Urgent is **MIXED**, with a P1 for missing
owner-backed alternative trade-offs. The latest Chat PASS does not supersede
that different capture's open P1. These follow-ups remain local and need the
coordinated gate before publication.

Local canonical `main` checkouts are not identical to remote main: workspace
`8a14d87` also contains separate design commits and dirty design work; backend
`fdf789d06` and app `23cff76f4` predate the merged recovery baseline. Do not derive
completion from the local branch name. Re-inspect heads, dirty changes and PR
state before execution; a dated table is not current Git state.

App `9640fef0b` adds common private text/photo authoring and add controls on the
four normal roots, building on `d07190235`'s immediate private receipt/Undo and
account-bound custody. Keyboard-pinned Keep, immutable retries and draft-lifetime
guards are implemented. Backend `d71d723df` adds verified-origin and real-DB
retention/removal regressions; `dca7c1be6` aligns the canon entrance without a
runtime change. Contribution and Chat rulings are reconciled here. Focused app
tests, the final app gate (185 seam tests), 13 backend checks including four
real-DB cases, and a nine-PNG native text flow passed their bounded checks.
Native intent remains MIXED because the registered reference is unavailable;
app `c27923302` now adds a six-frame iPhone 16 Pro native Photos-library
selection → editable draft → mock private Keep/exact-original receipt →
same-owner Undo path through Home root add. Its capture/correctness/visual gates
pass; the structured verdict remains MIXED because exact companion-reference
parity is unavailable and it records two small composer visual refinements.
App `33791bc00` adds a separately registered and captured two-photo variant:
native iOS Photos multi-selection → two editable/removable draft tiles → mock
private Keep with lead-original readback and `+ 1 more` → same-owner Undo.
The five-screenshot run `20260928T202625Z-photo-media-intake` completed on iPhone 16
Pro / iOS 18.2 / Maestro 2.6.1; all four functional assertions and verdict
validation passed. Its structured verdict is also MIXED: the companion design
reference remains unavailable (intent P1), and it carries the same two P2
composer refinements. App `8fce18ca1` adds the third native path: select a photo,
reopen the Photos picker, Cancel, then verify the unchanged draft still supports
Keep and same-owner Undo. Its five-screenshot run
`20260928T203504Z-photo-media-intake` completed on the same iPhone/iOS/Maestro
configuration; all four functional assertions passed, with no dimensional or
gate regressions against the two-photo run. The verdict remains MIXED for the
missing companion reference and the same two P2 composer refinements. Combined,
these captures establish one- and two-photo native iOS library happy paths plus
draft-preserving cancellation only. Camera, permission-denial recovery,
selections above two, individual readback of each selected original, real
authenticated readback, accessibility sizing, all root states and the six-door
composer remain uncertified. The newer Chat checkpoints below add Keep/Ask only
across private entrances; broader Send/Share remains incomplete.
The [capture checkpoint and door map](home-value-composition-execution-plan-2026-09-25.md#captureshare-continuation--private-custody-checkpoint-september-28)
record exact evidence, residuals and implementation order. These commits remain
local and need the coordinated gate before publication.

The later two-photo refinement supersedes that earlier visual verdict's two P2
findings. App `6eff90e82` compacted the note and reduced remove-chrome weight;
`8cc9f8c6f` put selected media before the optional note; `abadbe457` preserved
the full frame of text-bearing images; `8f0649bf0` compacted the empty note to
52 pt while keeping it multiline. The iPhone 16 Pro / iOS 18.2 / Maestro 2.6.1
run `20260928T222054Z-photo-media-intake` captured the final layout and passed
all four registered interaction assertions. The app `verify:pr` gate passed on
that code revision, including 185 parity tests across six suites. Its tracked
verdict at app `a5fc8ae00` is still **MIXED**: the registered design reference
is absent (intent P1, `fix-canon`), and one P2 remains because text-bearing
images cannot be opened full-size before Keep. The two former P2s—note
preceding media and oversized remove overlays—are no longer open. The receipt
shows the lead original and `+ 1 more`, not independent readback of every source.
This lane remains local/unpublished; this narrow mock-transport capture does not
close successful Camera capture, retryable native OS prompting, large-text,
other-root, live-authenticated, extension or whole-product acceptance. App
`d8a133677` preserves the draft after Camera denial, allows retry when
`canAskAgain` is true, and offers Settings only when the OS cannot prompt again.
Its denial-to-Settings handoff passed a targeted iPhone 16 Pro / iOS 18.2 /
Maestro 2.6.1 flow; the retryable native prompt and successful Camera shutter
remain unproven.

App `17db598c9` closes the remaining pre-Keep **open-image** behavior for the
two-photo draft: each selected original opens in the existing dark full-screen
viewer, then closes back to the unchanged editable draft. A post-commit iPhone
16 Pro / iOS 18.2 / Maestro 2.6.1 capture (`20260929T025713Z-photo-media-intake`)
passed the targeted native multi-photo flow and its bounded structured verdict
is **PASS** (`travel-app/docs/surfaces/photo-media-intake/verdicts/20260929T025713Z.json`);
`npm run verify:pr` also passed on the same code content (168 lint warnings
under a 169 ratchet, test-typecheck debt unchanged at 406, parity 185/185 across
six suites). The older checkpoint
above is historical evidence: its “cannot be opened” P2 is now closed. Two
small refinements remain (no pinch-to-zoom and no visible cue that a photo tile
opens). The actual 2026-07 intake canon exists in the primary workspace at
`design/vesper-canon-anchor/project/Vesper Photo & Media Intake.html`, but its
Artboard L depicts a trip-owned lightbox, not this newer private draft state;
the targeted result therefore does not claim full composition parity. The
previous seven-capture surface attempt remains non-green (only one capture
completed); only the registered two-photo flow was rerun here. This does not
close successful Camera capture, retryable native prompting, larger selections,
accessibility sizing, other roots, real-authenticated readback, extension, or
whole-surface acceptance. The separate `d8a133677` denial-to-Settings handoff
is now covered by its own targeted native flow.

The September 28 private-thread continuation connects newly selected Chat photos
to the same Intake owner, with visible Keep/Ask only and a current-owner
Open/Undo receipt. The question remains a separate answer-only pending turn.
Group/unresolved audience, carried references and ordinary questions do not
receive a new retention default. Scope, retry, source removal and typed owner
checks are recorded in the [Chat checkpoint](home-value-composition-execution-plan-2026-09-25.md#private-chat-bring--ask-checkpoint--september-28).
The new private-photo flow now has bounded native mock-transport acceptance and
shows the exact original before Undo; real authenticated mobile readback and
the complete six-door composer remain unverified. App `8a1337d62` connects the
Chat landing dock (legacy Vesper Home) and private/private-trip create through
the same source owner and durable pending-turn path, including idempotent room
creation, context preservation and destination Open/Undo. App `8fd994143` now
closes the specific native private-new-chat Keep → question → receipt → Undo
case and fixes the handed-off receipt state so Undo clears the exact owner
receipt while preserving the question. Two strict iPhone 16 Pro / iOS 18.2 /
Maestro 2.6.1 runs passed with the handoff-failure warning absent. This remains
mock-transport evidence; live authenticated readback, dock-fit, large-type and
full six-door acceptance remain open. Simulated room-create and bind retries
are now exercised together, but the expanded native scenario completed only
after runner retries; first-pass reliability remains unresolved. See the [entrance
checkpoint](home-value-composition-execution-plan-2026-09-25.md#private-chat-entrances-checkpoint--september-28)
and [September 29 follow-up](home-value-composition-execution-plan-2026-09-25.md#private-new-conversation-bring--ask-native-follow-up--september-29).

The [email checkpoint](home-value-composition-execution-plan-2026-09-25.md#forwarded-email-private-keep-checkpoint--september-28)
connects forwarded message text to private Keep, current-owner receipt/Undo and
Life metadata refinding. Historical replay preserves its retention policy and
cannot restore released originals. Raw provider envelopes are not additional
visible artifacts. Supported email attachment bytes now use the same Intake
source owner, receipts, Life projection and Undo; focused tests and disposable
Postgres acceptance passed. Real provider delivery and native acceptance remain
open; scanner-gated formats and the current no-notice rejection behavior remain
product limitations. The latest
coordinated gate **failed** at the world-catalog runway: no Season/Here rows
cover October 12. Its earlier pass does not certify this tuple; repair the
catalog through its existing owner before publication, without weakening gates.

App `a11d1a061` connects a newly retained private Intake source to the existing
Life owner projection: unresolved sources appear in Time, and in Places only
with an explicit Capture place subject; opening a row returns to its exact
Intake source. Keep/resolve/Undo refresh the projection without a parallel
artifact store or backend contract. Focused app tests, typecheck and
`verify:pr` passed. A registered standalone iPhone mock flow now passes private
Keep → Life row → exact original → existing owner receipt → Undo → row absent.
It deliberately does not claim return-to-Chat continuity, live authenticated
mobile readback, or Life composition/design acceptance. See the [continuity
checkpoint](home-value-composition-execution-plan-2026-09-25.md#private-intake-to-life-continuity--september-28).

App `fd6418e13` connects OS text/link/file handoff to the common private composer:
account-bound draft, explicit Keep, preserved originals/captions and existing
receipt/Undo. [Its checkpoint](home-value-composition-execution-plan-2026-09-25.md#os-common-composer-host-adapter--september-28)
records 94 focused app tests, the app gate and owner regressions. This remains
a **host-app adapter**, not the accepted in-place OS experience. The next native
package must own reproducible extension generation, current-session delivery,
host-closed operation, retry/readback/Undo and dismissal; do not redispatch the
finished host composer or add another capture/auth service.

App `bc0adbac5` makes the common capture UI finish in place using the same
current-owner receipt and Undo, with receipt-ID resumption and explicit optional
depth. [The session checkpoint](home-value-composition-execution-plan-2026-09-25.md#shared-in-place-capture-session--september-28)
records 123 focused app tests, the app gate, 39 owner regressions and the refined
native implementation sequence. This is now used in the main app, not an iOS
extension completion claim. The native host and shared authoring are implemented;
its account snapshot is an experimental follow-up below. Neither host-free UI nor
a simulator compile proves signed-device authentication or complete delivery.

App `95bc70d14` advances `6243f85f5`'s opt-in native host to the **same editable
composer**, with bounded Expo/native providers and accessible text-scaling props.
`fb559640a` repairs duplicate generated source references. App `9424daf82`
connects an app-owned Clerk session snapshot and read-only extension restore,
including generation fencing on account changes and teardown. The opt-in
simulator build, app gate (185 seam tests), 44 focused session/host regressions,
10 native configuration tests and inspected real-mode dependency bundle passed
their measured scopes. The
[native and account checkpoints](home-value-composition-execution-plan-2026-09-25.md#development-only-clerk-account-handoff--september-28)
record exact commands and limits. At that revision this remained an experimental
account bootstrap with no delivery. The current lane advances it: the extension
now invokes the existing custody service/client with a protected retry journal,
submission-ID persistence, current-owner readback and Undo behind a
development-only opt-in. Keep is still off by default. The latest opt-in
simulator build compiles, but both app and extension are ad-hoc signed with no
signed entitlements, even with an explicit local identity override. The project
team (`QNZ5K23A74`) does not match the only valid local Apple Development
identity (`J6ZKHAT2H7`), so this is not signed-device acceptance. The ordinary
build is restored, and production-profile enablement remains rejected. See the
[native capture checkpoint](home-value-composition-execution-plan-2026-09-25.md#in-place-extension-delivery-and-protected-retry-journal--local-implementation-september-28)
and [signing boundary](home-value-composition-execution-plan-2026-09-25.md#signed-simulator-build-and-entitlement-boundary--september-28).

App `e5788100f` extracts the resumable binary Source-custody sequence from the
React data module into one injected-client service, while keeping the app
facade stable. The focused suite (12/12) and app gate (185 seam tests) pass.
This removes the service's React/data dependency; it does **not** connect that
service to the native extension or prove authenticated HTTP. Before journaling,
App `67c33c8f3` adds the extension-safe authenticated transport and shared Intake
v2 route owner; their focused tests and app gate passed. App `f850dc0e2` connects
that owner through a protected pre-dispatch journal and in-place
resume/readback/Undo path. Follow-up `6005dd39b` fixes the two test-type errors
introduced with that slice; the final app gate passes, with the existing
406-error test-type debt unchanged. Exact local evidence and the still
unverified device boundary are in the linked native capture checkpoint.
Do not copy endpoint paths or import the app-wide HTTP facade. Keep stays
disabled by default until signed-device acceptance is proven.

App `ce8649e68` closes the private image-readback gap in the in-app capture
path: verified Chat Keep now previews the exact selected photo, and Life's
original reader shares the same owner-scoped media resolver. Mock readback
checks current persona custody and clears the local URI on Undo; both readers
fence account/source-stale results, including A → signed out → A. Seven focused
suites (112 tests), app `verify:pr` (185 parity tests), four backend media-route
tests and the registered native mock Chat flow passed. The native flow used a
real simulator library selection but not the live mobile/API transport. The
[H1 receipt](home-value-composition-execution-plan-2026-09-25.md#private-photo-original-readback--september-28)
has exact commands and limits. This does not resolve extension signing, real
Clerk/mobile media readback, all six doors or broader sharing policy.

The current lane follow-up extends the confirmed canonical artifact projection
from eight to the full 16-image Intake limit, preserving source ordinal order;
the existing Life-linked reader can open each projected original and virtualizes
offscreen full-size photo reads. Backend projection and app gallery tests cover
the 16-item boundary, but native runs still stop at two selected images and
mobile authenticated readback remains unverified. Continue within the same
capture/share owner package; do not treat this as a separate media subsystem or
as completion of the six-door outcome.

The separate canonical checkout contains concurrent design work and is not the
execution target. Do not switch it, advance its children, or bring unrelated
uncommitted design changes into this lane.

| Evidence at the published tuple | State and boundary |
| --- | --- |
| Coordinated local verification | `scripts/land-worktree.sh home-value-delivery --publish` completed `make verify` and published the three branches. This evidence predates the docs-only rebaseline; detailed counts and exclusions are in H1. |
| Backend CI | [Passed](https://github.com/fy538/travel-agent/actions/runs/36355954051), including DB and migration checks. |
| App CI | [Passed on the final app head](https://github.com/fy538/travel-app/actions/runs/36358544184), including tests, types, design/governance and contracts. |
| Workspace CI | [Failed before product tests](https://github.com/fy538/travel-workspace/actions/runs/36355993401/job/108723720414): private child checkout could not authenticate. Renew/fix `TRAVEL_WORKSPACE_CI_TOKEN` access, then rerun. A configured secret is not proof of usable access. |
| Merge | All three PRs remain open and review-required; no merge conflict was reported. User authorization to publish/merge is already recorded in the task. Any owner-approved one-off override must be reported with the failed/unrun boundary intact; do not silently change standing protections or label an override a passing check. |
| Native product quality | Full Home matrix remains MIXED. Targeted Planning and Cold follow-ups passed their bounded assertions, not full-scroll design parity. The newer local H1-A patch does not inherit a full PASS from these older captures or from its passing component checks. |

## What is already delivered in the candidate

| Capability | Established progress | Still not established |
| --- | --- | --- |
| Supported Source value | Canonical owner discovery/read, explicit Home `Ask Vesper` request, governed preparation, saved result, exact readback, native result/return and withdrawal connected; rejected outputs preserve their true terminal outcome. The September 26 synthetic, provider-free native rehearsal already covers this bounded connection. | Model-authored editorial quality and recurring useful supply remain unverified; do not repeat the same fixture flow as a quality test or add a new trigger to compensate |
| Contextual Home continuation | Exact Plan/opening/recovery context reaches a private editable Chat draft and supported backend prompt assembly | Quality of a real model answer or authority to send automatically |
| Received original | Exact authorized private photo through local DB, object storage, API and native reader/return | Production media service, album/grouped-photo identity, Reply or broader audience model |
| Practical value | Supported open-now possibility reaches the exact venue and returns | Provider-backed freshness or a generalized live service |
| Cold Home | Source-backed current-Places reading before an input request; owner-backed local API to native depth and return | Real recurring editorial supply, full design parity |
| Native composition | Compact planning motion, corrected Home glyph/region treatment, removed gold reading edge, exact return position and selected first-viewport references | All remaining matrix findings resolved or full-scroll reference acceptance |

Do not repeat these connection projects under new names. The
[H1 completion map](home-value-composition-execution-plan-2026-09-25.md#delivered-connections)
records their limits. More tests or fixture screenshots of the same paths alone
are not the next product increment.

## Current dispatch queue

| Order | Outcome / accountable owner | Finish condition and next decision |
| --- | --- | --- |
| 0 — delivery closeout | Reconcile the three open PRs with the current local lane before closing anything. The PRs still point at the published baseline; the local follow-ups are not included. Fix the workspace checkout credential through the repository owner, and run the coordinated gate on the intended current tuple. | Record actual merged heads and branch/worktree disposition. Reuse the lane for follow-on Home work if it remains suitable; do not archive it merely because a PR merged. This administrative gap does not block independent local building. |
| 1 — H1 checkpoint / retained gaps | Connected implementation and bounded-preview/copy follow-ups are committed. App `932abe25a` closes the Urgent action's divergent Chat route. App `53699858c` and `acf0c7203` remove unsupported “new route” / “already being repaired” claims and align the mock Chat handoff with its actual owner facts; post-commit urgent and Chat native captures pass. The source trace found reachability but no authorized route-options source: `route.evaluate` does not provide alternatives, and the itinerary alternative operation is venue-only. The [assignment](home-value-composition-execution-plan-2026-09-25.md#next-complete-assignment) retains the missing owner-backed option comparison, social hierarchy and real recurring-supply uncertainty. | Do not call Home fully accepted. First identify the canonical owner for current, authorized recovery options and unknowns—or refine the comparison promise if no such owner exists. Truthful fixture copy is not recovery value. These named residuals do not block independent capture/share foundations. |
| 2 — active capture/share package | Same coordinated owner continues from private Keep/Undo, root-add authoring, private Chat, local email and OS host-composer handoff. App `ce8649e68` adds exact private-photo readback on the Chat receipt and through Life's shared owner-scoped resolver; native mock-flow and owner-route tests pass, but mobile live-route/Clerk readback is not proven. The in-place native extension implements the existing Intake path, protected retry journal and owner receipt/Undo behind a development-only opt-in; simulator compilation passes, but signature inspection found ad-hoc app/extension bundles with no signed entitlements. The Xcode project team (`QNZ5K23A74`) differs from the only valid local development identity (`J6ZKHAT2H7`). Do not repeat simulator builds with the same identity mismatch. Resolve matching signing/provisioning with App Group/Keychain entitlements before signed-device acceptance. The H1-B Source trace is now complete at the connection boundary: Home's explicit `Ask Vesper` request and the synthetic provider-free native path already pass; keep model quality/recurring supply as unverified, and do not add another trigger or rerun the fixture as a substitute. The lane API starts with model/search disabled, LLM background loops disabled, and Clerk JWKS/issuer verification configured; health 200 is startup evidence only. Email v2 now captures supported attachment bytes through Intake; focused unit and disposable-Postgres acceptance passed, while real SendGrid delivery remains unverified. PDF/PKPass/HEIC and other scanner-gated types stay unsupported; any unsupported file can drop the whole email. The Import-by-email setup discloses this boundary, but there is no per-message or sender-facing failure notice. The eight stale-consumer findings caused by the Intake custody-client extraction are resolved by correcting the policy and schema-bridge source pointers; the current API audit, contract check, type sync and schema-bridge all pass without a wire-shape change. Broader Send/Share still needs its relationship/audience owner amendment. | A complete authored item can enter, return immediate value, reach its selected authorized audience, be refound and be corrected/withdrawn. Host-app redirection is not in-place OS completion. Authoring, simulator compilation and API health alone do not complete sharing, all six doors, full Life continuity or later value. Pending policies remain excluded. |
| 3 — reassess receiving and later value | At the capture/share checkpoint, choose the next whole-product package against the actual retained/shared material: richer Home/Places receiving, Life continuity, or an accepted preparation gap. | Select from observed code/design gaps and received benefit, not a standing parallel backlog. Do not launch all three automatically. |

**New bounded capture evidence (September 28):** app `d8a133677` preserves
the draft after Camera denial, offers retry only while the OS can prompt again,
and otherwise exposes Settings. A targeted iPhone 16 Pro / iOS 18.2 / Maestro
2.6.1 denial-to-Settings flow passed. The retryable native prompt and successful
Camera capture remain open; exact receipt and checks are in the [active Home
execution package](home-value-composition-execution-plan-2026-09-25.md#camera-permission-recovery--september-28).

**Camera failure-path follow-up (September 29):** app `de02ae042` now reports
native camera-launch failure accurately, preserves the editable draft, and
keeps Photos available as fallback. Its registered iPhone 16 Pro / iOS 18.2 /
Maestro 2.6.1 mock-transport flow passed through private Keep, image receipt and
Undo. This is not successful shutter or real custody evidence: the assigned
simulator has no camera source. The same app pre-PR gate passed (168 lint
warnings under a 169 ratchet; test-typecheck debt remains 406; parity 185/185
across six suites). The design-alignment test suite also passes with generated
`.tmp` caches excluded from source discovery and symlinks skipped. See the
[camera-unavailable evidence](home-value-composition-execution-plan-2026-09-25.md#camera-unavailable-recovery--september-29).

**Home root-add recovery follow-up (September 29):** app `55022182e` keeps the
shared private composer reachable on Home v2, compatibility, loading and
recoverable-error states; focused tests cover the loading/error route and
compatibility header clearance. Typecheck, 33 focused tests, the targeted flow
contract, polish QA tests and scenario registration passed. The app `verify:pr`
gate passed on this code content (185/185 parity; existing lint/test-typecheck
ratchets unchanged). The first combined native Home run captured **11/12**; the
photo case was invalid because the lane media endpoint was stopped and the flow
also targeted direct-image opening for a fixture without that authorization.
After starting this lane's API, the image loaded and showed the expected explicit
“Open original” source door; the corrected targeted flow captured the card,
reader and return (**1/1**). This is not a complete Home matrix or live custody
acceptance. Exact evidence and limits are in the [H1 execution record](home-value-composition-execution-plan-2026-09-25.md#home-root-add-during-loading-and-recovery--september-29).

App `baeb7a2d9` then adds an explicit `TO YOU` cue to the individually addressed
Home original stamp, using the existing current recipient-safe delivery read.
Four focused suites passed (70 tests), the app `verify:pr` gate passed
(185/185 parity), and post-commit native run `20260929T052518Z-home-root`
captured the addressed photo, exact original reader and Home return (1/1) on
iPhone 16 Pro / iOS 18.2 / Maestro 2.6.1. This closes only the copy detail;
full Home visual acceptance and live authenticated media custody remain open.
The H1 record carries exact commands, the 168/169 lint warning ratchet, the
existing 406 test-typecheck-error baseline, and the evidence boundary.

**Three-photo iOS capture checkpoint (September 29):** app `ddde3259c` adds a
registered Home-root Photos flow selecting three images, opening the third as
3/3, returning to the editable draft, mock Keep with `+ 2 more`, and same-owner
Undo. The committed iPhone 16 Pro / iOS 18.2 / Maestro 2.6.1 run passed **1/1**
with all six extra screenshots. This closes the native selection-above-two gap
for a three-image example only—not authenticated per-image readback, all 16
items, real custody, or the unavailable Claude-reference comparison. The
immediate next device milestone remains matching signed app/extension
provisioning, then real Clerk and owner-backed readback. Detailed assertions,
two non-blocking image-viewer refinements, the mock evidence boundary and exact
commands live in the [H1 execution package](home-value-composition-execution-plan-2026-09-25.md#native-selection-beyond-two--september-29).

**Private new-conversation Bring + Ask follow-up (September 29):** app
`8fd994143` fixes a receipt handoff defect: the destination composer now adopts
the owner-authorized receipt ID passed from the pending turn, and matching Undo
clears that receipt without dropping the authored question. A regression test
also proves a stale prior-source removal cannot clear a newer receipt. The
registered `polish/vesper-chat-private-create-capture` flow selects a native
Photos-library image, keeps it privately, creates the private conversation,
verifies the exact receipt and Undo, and confirms the question remains. Strict
native runs `20260929T152015Z-vesper-chat` and
`20260929T152544Z-vesper-chat` passed **1/1**, each with five extra captures, on
iPhone 16 Pro / iOS 18.2 / Maestro 2.6.1. Both assert the pending-turn failure
warning is absent. An earlier intermediate run displayed that warning once; it
did not recur in the next three runs, so its cause remains unconfirmed rather
than being presented as a proven fix. Focused tests passed **37/37** across
three suites; `npm run typecheck`, scenario registration (**31**), Chat design
reference validation (one manifest, 30 pairs, zero verified external canon
references), `git diff --check`, and workspace `make docs-check` passed. The
native flow uses mock transport: it does not prove authenticated upload,
server-backed receipt persistence, or model answer quality, and it has no
matching image-state design reference. The dock, failed-room/bind, large-type,
full Chat visual and complete six-door gaps remain. The matching handoff defect
and command evidence are recorded in the linked checkpoint.

**Private retry-path expansion (September 29):** app `d41237757` adds an
explicit same-attempt retry after private photo Keep succeeds but conversation
creation or pending-turn binding fails. The registered native scenario injects
both one-shot mock faults, keeps the create surface and authored question
available between them, then completes Chat receipt/Undo. The bind-only rerun
`20260929T183101Z-vesper-chat` passed on runner attempt 1/3 after changing the
Maestro selector to the button's stable test ID. The expanded two-fault run
`20260929T184142Z-vesper-chat` completed 1/1 on attempt 3/3; attempts 1 and 2
failed waiting for the destination composer, with the create surface still
visible. This is bounded simulated retry evidence, not a root-caused first-pass
reliability result or a real-server idempotency claim. Exact diagnostics and
remaining limits are in the [H1 checkpoint](home-value-composition-execution-plan-2026-09-25.md#private-capture-bind-retry-recovery--september-29).

The retry audit then corrected a separate mock/backend mismatch in app
`2644f51e2`: the mock stage owner now replays an identical client turn without
resetting bound state, rejects changed payload under the same idempotency key,
and clears turn state on mock reset. The backend still validates source custody
on every stage request, so the client deliberately restages with its stable key
after Undo rather than caching an ID. The follow-up run
`20260929T192147Z-vesper-chat` failed on runner attempt 1 at the destination
composer (create screen remained visible) and completed on attempt 2, including
receipt/Undo. The mismatch is fixed, but it did not remove the intermittent
native failure; the cause remains open in H1. App `npm run verify:pr` passes on
the corrected source (168 lint warnings; 403 test-typecheck errors; parity
185/185, zero skips). This remains simulated transport evidence, not live
authenticated custody, first-pass stability, or real-server delivery.

**Next execution checkpoint:** first resolve the signing prerequisite for app
`6005dd39b`'s journal-backed in-place path, then verify on an isolated signed
device: host closed, share payload preserved, explicit Keep, same-attempt
recovery after interruption, current-owner receipt, Undo, dismissal and repeated
invocation; include account expiry/switching. The latest code passed 41 focused
Jest tests, seven Swift journal scenarios, typecheck, ten native-configuration
tests and opt-in ShareExtension simulator compilation. However, both app and
extension signatures were ad hoc and contained no signed entitlements even when
an identity override was requested; the configured Xcode team
`QNZ5K23A74` differs from the only valid local identity team `J6ZKHAT2H7`.
Therefore no build was installed and this is **not** signed-device acceptance.
The exact evidence and prerequisite are recorded in the [H1 native checkpoint](home-value-composition-execution-plan-2026-09-25.md#signed-simulator-build-and-entitlement-boundary--september-28).
The ordinary configuration was restored, Pods installed, and the native
configuration suite passed 10/10. The first app gate found two new test-type
errors in this slice; both were fixed. Final `verify:pr` passed, including
185/185 `qa:parity` tests with zero skips; the full-suite test-type ratchet
remains at its existing 406-error baseline. Both already-booted simulators and
the paired iPhone were left untouched. The lane API's `/health` returned 200,
but no Clerk session or authenticated Intake call was exercised. Do not infer
acceptance from store-reopen harness tests, signature-integrity verification or
simulator compilation. If matching signing credentials are unavailable, record
the device acceptance boundary as externally blocked and proceed with an
independent roadmap slice. Do not reopen connected private Chat entrances.
Keep the unresolved broader-audience owner amendment, email provider/attachment
gaps, October 12 catalog failure and Home recovery comparison visible; none is
fixed by this capture checkpoint.
A locked Mac blocked the
new visual review, not the independent owner/code work. In-app text/photo
authoring, Just me, root add and private receipt/Undo are implemented locally;
the six-door map records their verification boundaries. Wider audience ownership
is not implemented. Source preparation/serving is
implemented but real recurring value is unverified; Home recovery has an actual
presentation/preparation gap, not a missing second generator. Retain those
distinctions. No new ambient trigger, audience policy or pending R1–R5 rule is
adopted to make this checkpoint easier.

### Capture/share package boundaries

The next owner should produce one compact implementation map in the active
package, using existing canonical owners and generated contracts. It must cover:

- **Owner reconciliation before affected runtime changes:** contribution §3.2,
  §9 and §12; Product Thesis/Model entrance wording; Chat ruling 04; group/social
  optional polls and occasion rooms; relationship audience and use-grant rules.
  Amend only accepted rulings, retain rationale, and identify remaining conflicts.
- **Shared path:** just-me default, Keep/Send/Share labels, immediate private
  custody with Undo, provisional recognition and truthful send-time payoff.
  Remove review-first capture without replacing it with invisible personal claims.
- **Doors:** OS share sheet finishing in place; camera/photo picker; global add;
  Chat attachments with visible keep state and Ask only; existing-object Keep/Send;
  email forwarding. Audit existing adapters, share one contract, and identify
  native/server delivery constraints rather than pretending every door is a
  React component.
- **Receiving and repair:** existing selected-original and place/link ownership,
  authorship, permitted audience, forward-only Friends eligibility, withdrawal
  and independent kept place survival. The newer audience model is accepted
  direction but its schema is not designed; do not force it through the old
  place-required one-recipient note or silently widen an existing grant.
- **Separate policy dependencies:** friend's words used for an explicit question
  require the named use-grant amendment. Guest identity, notifications, retention
  periods and export are not settled by the decisions; they need a ruling only
  where the selected implementation depends on them.

The September 27 R1–R5 recommendations are **not adopted by this roadmap**:
thread-intersection mechanics, the new voice register, autonomous artifact-type
evolution, status-triggered offers and the proposed intersection-offer sequence.
The accepted one-composer work can proceed without them. Selecting capture/share
as the next package does not approve an offer that depends on those pending rules.
Casual-question continuity remains unadopted; deliberate share-plus-question is
the separate accepted amendment.

## Execution and reassessment

Use the existing [lane lifecycle](../Workspace%20Repo%20Setup.md) and root AGENTS.
One owner keeps responsibility through landing or an explicitly held disposition;
temporary workers require authorized delegation and disjoint write ownership.
Keep at most one or two active implementation packages, not a new tracking system.

- **One complete assignment per round.** The owner carries diagnosis, implementation,
  focused tests, review corrections and landing. Ordinary debugging needs no
  founder round trip.
- **Parallelize only independent outcomes.** A bounded worker can handle Home
  presentation while another inspects existing preparation/serving, with one
  owner for shared wire contracts and navigation. Contract mapping for the next
  package can run independently; no competing runtime owner or permanent
  integration lane is needed.
- **Check in at the first working result, a consequential decision/blocker, and
  the reviewed finish.** Coordinate shared files, runtime and devices directly;
  escalate changed product/authority/architecture choices.
- **Verify proportionately.** Focused checks during implementation; affected
  contract/behavior/native evidence at package completion; required coordinated
  `make verify` before publication. Do not repeat the full matrix for every copy
  change or replace the required gate with a weaker one.
- **Maintain this roadmap in place.** Replace the baseline and queue; do not
  prepend dated overrides. H1 holds one current evidence summary; large receipts
  remain historical. Retire or replace its active assignment when done, not by
  accumulating another endless log.

At each package checkpoint ask: what is now worth receiving; does context improve
it; how much effort remains with the person; did we reuse the right owners; and
what exact evidence supports the result? Judge progress by finished outcomes,
rework, blocked time and founder intervention—not agents, commits or doc volume.

Documentation validation: the September 27 rebaseline refreshed the generated
inventory with `make docs-status-sync`. September 28 owner alignment changes no
registry or word-budget policy; measured `capture-roadmap-docs` passed
`make docs-check` in 6.103s.
The shared-composer checkpoint also passed measured `capture-shared-composer-docs`,
`make docs-check`, in 7.882s. Its runtime and exact evidence are bounded in H1.
A docs check does not refresh the full coordinated product gate.

## History, not another queue

The [September 27 program snapshot](../archive/vesper-program-roadmap-history-through-2026-09-27.md)
and [H1 receipts](../archive/home-value-composition-history-through-2026-09-27.md)
preserve the full prior bodies at workspace `a73e9d2`. Older strategy and
integration history remain linked below. No historical “current” statement
overrides the baseline above.

## Historical link compatibility

These anchors preserve older references. They do not reactivate old queues.

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
