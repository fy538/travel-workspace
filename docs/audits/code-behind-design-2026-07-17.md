---
doc_type: working
status: active
owner: engineering / design
created: 2026-07-17
last_verified: 2026-07-17
expires: 2026-08-16
why_new: Reconciles the reverse design/code audit after remediation and provides the authoritative compact residual implementation-gap list.
reference_material: docs/audits/design-behind-code-2026-07-17.md
design_target: Vesper 220 / Canon 130
code_target:
  travel_app: 95b1c2fa
  travel_agent: 8526bc37
source_of_truth_for: [code-behind-design-gap-inventory-2026-07-17]
---

# Where the Code Is Behind the Design — Vesper 220 vs repos @ 2026-07-17

## Purpose and verdict

This is the reverse companion to `design-behind-code-2026-07-17.md`: it records only places where the current design remains a valid product target and the implementation does not yet reach it.

The source audit compared the JSX behind Vesper 220—not screenshots—with the current React Native app, generated API types, backend routes, and relevant tests. The existing design-behind-code audit was then used to adjudicate direction. A literal visual difference was not counted when newer code has already invalidated the older board.

## Post-remediation reconciliation

The first engineering remediation wave landed in `travel-app@b1bef1e7` and
`travel-agent@eefed571`. Source and regression checks were rerun after the
changes. The original detailed findings remain below as the historical audit;
this section is now the authoritative residual list.

A second durable-agency increment is committed at app `8f506f70` and backend
`c57f6036`. It adds an enforced
`organizers` editing mode; granular, persisted Vesper suggestion/minor/major
delegation; and viewer-owned quiet-trip plus proactive notification-family
controls. Notification policy is applied before proactive arbitration, and
partial family updates preserve earlier choices.

The next increment now includes organizer-managed policies that durably
control who may add expenses and who may start booking work. Final provider
confirmation remains the stricter organizer-plus-session-controller action.
Booking sessions opened from explicitly scoped plan blocks now persist each
included traveler as pending/approved/declined, block confirmation on holdouts,
and support a durable self-only fallback. Controllers can now remind named
pending travelers through the shared notification pipeline; each accepted send
has a durable participant receipt, a four-hour anti-spam claim, and a direct
booking-session destination. Shared confirmation receipts are now durable:
provider-confirmed checkout, reconciliation, restaurant, and paid-hold paths
post one replay-safe receipt to the shared trip room,
including proposal-less plan and venue sessions. The Costs half is now durable
too: affected travelers can open one expense dispute, the opener can withdraw,
and the payer or an organizer can resolve it. An open dispute is excluded from
settlement, blocks settle/delete, cannot be opened over live payments, retains
history, and posts an exact-expense receipt to the trip room.

Archived-trip recovery is now durable at app `f74def27`, backend `7c75097b`,
and workspace contract `afedb59`. Organizer recovery restores the preserved
trip shell and its exact pre-archive lifecycle phase, reopens only group rooms
archived by that transition, and deliberately leaves proposals, searches,
workflows, notification outcomes, and invites closed. The app normalizes the
backend's legacy `active` phase to the traveler-facing `live` phase.

Trip cancellation and reuse are now full-stack. Cancellation has an
organizer-only preflight, refuses unresolved booking/provider truth, states
that cancelling a trip never cancels a reservation, preserves confirmed
booking and unsettled Costs truth, retains a readable cancelled record, and is
durably idempotent. Reuse creates a clean, undated solo draft and copies only
reusable itinerary shape; members, invitations, conversations, bookings,
expenses, proposals, votes, workflows, event outcomes, and provider state stay
with the source trip. The mobile entrance, generated contract, duplicate-call
guards, and return routing are covered.

The terminal-lifecycle hardening through backend `eea2c245` closes the
remaining cancellation races. Central write gates now reject late booking,
proposal, workflow, planning, and message persistence. Notification creation,
channel fan-out, invite delivery, scheduled active-trip work, recurring
pre-trip preparation, and calendar completion all recheck durable lifecycle
truth. Post-trip story/memory work and money/reconciliation notices remain
available by explicit policy rather than accidental exception.

Optimize Route consequence truth is typed at backend `8526bc37` and app
`95b1c2fa`. Replan previews now also project every atomic child as an added,
moved, removed, or replaced stop and state how many existing stops stay
unchanged and how many protected provider dependencies remain explicit. The
landed receipt preserves that same structural evidence from the revalidated
preview. Each changed stop now also carries destination-local prior/proposed
day and time plus grounded outbound travel mode/minutes; absent route truth is
left absent. Initial Split construction now selects any active same-day place,
keeps the full interval explicit, supports multiple travelers on either named
branch, and requires an owner drawn from each branch.

The private-handoff finding is also closed after re-adjudicating the production
path. A strict group-compose failure already persists a replay-safe, hidden
system seed in the requesting traveler's existing personal trip conversation;
group history maps that failed row to the canonical privacy divider and
`PrivateHandoffSeamCard`, whose action opens the exact seeded conversation.
The public projection is now intentionally narrower than the private seed: it
carries only conversation/trip routing truth and seed status. Suppressed draft
content and presentation summaries never enter group history, SSE metadata,
mock payloads, or route params. The similarly named gallery privacy-boundary
specimen is not the group private-handoff contract and does not need a second
producer.

Chat Comparison is now grounded in the existing shared Stay decision model.
`post_stay_comparison` requires at least two active persisted candidates,
projects only saved price/area/cancellation/source/note fields plus the canonical
vote resolver's counts and phase, and persists an idempotent
`notification/comparison_card`. The card previews two options, states when more
exist, and opens the canonical Stay comparison/vote surface for the complete
durable action. It does not infer pros/cons, claim live inventory, or revive the
separate producer-gated Home Comparison face.

### Resolved in the first wave

- **Truth and governance:** Stay's internal soft hold is now framed as a group
  decision marker; Vesper 220 is fingerprinted; broken route-owner references
  fail the design gate; typography is green at 52/52.
- **Trip and workflow:** existing operation previews now show Was/Now,
  protections, recovery and revalidation; replace-only versus replace-and-book
  is explicit; stale recovery preserves previous/current/draft truth; traveler
  object/history surfaces no longer expose raw IDs, confidence or internal
  canonical/ledger language; completed trips point to unresolved Costs.
- **Product surfaces:** connected systems, inline OAuth retry, Atlas rotating
  seed entrances, Chat depth for booking/vote/research, trip-creation anchors,
  and cross-device workflow adoption are implemented.
- **Discover:** scope and layer controls, denied/offline postures, exact-trip
  context, in-plan membership, venue/detail context and grounded Ask Vesper
  handoffs are implemented end to end.
- **Search and state:** Universal Search action receipts have stable,
  non-mutating destinations; Atlas Unpacked and stale profile state use the
  shared state doctrine; the privacy seam uses an attached explanation.

### Resolved in the durable-agency and lifecycle waves

- **Booking lifecycle authority:** entry authority, participant consent,
  named holdouts and cooldown-governed reminders, organizer-plus-controller
  confirmation, provider cancellation/reconciliation, shared replay-safe
  receipts, and expense disputes are durable.
- **Trip retirement:** archive/recovery, guarded cancellation, readable
  cancelled records, and sanitized reuse-as-template are implemented across
  backend, generated client contract, app state, settings entrances, and
  regression tests.
- **Cancellation races:** terminal status now wins against in-flight writers,
  queued notifications and invites, scheduled coordination work, recurring
  pre-trip workers, and automatic calendar completion.

### Compact residual backlog

| Priority | Residual capability | Direction |
|---|---|---|
| P1 | Missing Chat object producers | Atlas draft still needs a typed producer plus durable action; itinerary contributor attribution remains ungrounded. |
| P1 | Heterogeneous Discover pins | Venue pins are complete; friend, experience and place payloads still need accessible rendering and grounded handoffs. |
| P2 | Bounded product/interaction polish | Trip Info hero/description, Skip vote, trip-creation correction, booking recovery and share-owner sheets. |

Deferred and therefore excluded from the active residual list: Home
Flight/Comparison without producers, per-trip privacy/learning, voice takeover,
native blur material, and Atlas deferred facets.

The overall verdict after remediation is:

- The central Trip/Itinerary shell is substantially aligned. It does not need another structural rewrite.
- There are no remaining P0 findings from this audit.
- Durable trip agency now covers plan governance, Costs/Booking entry authority,
  booking participant consent and reminders, shared booking receipts, the
  expense-dispute lifecycle, guarded trip cancellation, archive recovery, and
  sanitized reuse. Remaining P1s are grounded object producers rather than
  lifecycle, authority, consequence, or shell redesign.
- The central Trip/Itinerary shell, alignment gate, typography ratchet and
  bounded Discover/Atlas/Chat seams are green.

## Direction and severity rules

**Direction**

- **Active gap:** the design is still the intended target; implementation is missing, narrower, or misleading.
- **Partial / full-stack seam:** UI or primitives exist, but the producer, durable contract, action, or state family is incomplete.
- **Backend-gated:** the target is valid, but exposing the control without persistence or authority would be dishonest.
- **Deliberately deferred:** recorded for planning but not an active release regression.
- **Excluded:** the design board is behind newer product truth; implementation must not be changed to imitate it.

**Severity**

- **P0:** enabled behavior misstates truth, privacy, money, or authority.
- **P1:** material canonical behavior is absent or non-functional.
- **P2:** polish, recovery, state application, or governance debt that does not falsify the primary action.

---

## 0. Cross-cutting design-system and enforcement gaps

### 0.1 The alignment system is certifying Vesper 216, not Vesper 220 — P1

`travel-app/docs/design-alignment/canon.fingerprint.json` and `STATUS.md` identify **Vesper 216** as the captured canon. This audit's actual target is Vesper 220. A passing design gate therefore cannot establish alignment to the current design file.

There is a second blind spot:

- `single-trip-home` was correctly removed from the active polish surface registry when the legacy Folio surface was deleted.
- Five routes in `docs/design-alignment/route-owners.yaml` still point to that removed owner: Trip root, Details, Details section, Memory, and Story.
- `generate-status.mjs` labels these `owned (BROKEN REF)` but increments `ownedCount` anyway.
- `check-design-gate.mjs` fails only on `L0 GAP`; broken owner references do not fail the gate.
- `Vesper Trip Visual Canon.html` remains an L1 canon gap with no owning surface.

**Required:** fingerprint Vesper 220, replace the retired owner with current canonical Trip/Details/Memory/Story owners, and make any `owned (BROKEN REF)` route a gate failure. Until then, the most important product spine is outside meaningful alignment certification.

### 0.2 Typography adoption is over budget — P1

`node scripts/check-typography-budget.mjs` currently fails:

> 65 raw `fontSize` literals; baseline 63.

Largest concentrations:

| File | Raw sizes |
|---|---:|
| `components/trips/TemptHero.tsx` | 13 |
| `components/trip/MemoryModeSections.tsx` | 8 |
| `app/atlas/long-view.tsx` | 7 |
| `components/trips/StoryReadyEntry.tsx` | 6 |
| `components/trip-plan/TicketBand.tsx` | 5 |
| `components/voice/MicPrivacyDisclosure.tsx` | 5 |

This does not prove that all 65 rendered sizes are visually wrong. It proves the semantic-role migration has regressed and the CI ratchet is red. Audit these files against `constants/typography.ts`, create a role only when a real missing role is repeated, and lower the baseline after conversion.

The underlying families are correct: EB Garamond, DM Sans, and JetBrains Mono are registered, and the shared Button, color, radius, shadow, and sheet budgets remain structurally healthy.

### 0.3 State System application is incomplete — P2

The shared state primitives are broadly implemented, but real routes still bypass the doctrine:

- `app/atlas/unpacked.tsx` uses a full-screen spinner instead of a content-shaped skeleton.
- `app/(tabs)/_layout.tsx` uses a red profile-fetch banner for stale/missing data. The canon reserves danger/red for a failed user action; stale data should use the quieter ink/steel posture.
- Discover Map has generic loading/error/empty/unavailable states but lacks its designed location-denied and offline-cached variants; see §4.4.

This is migration debt, not a reason to redesign the state kit.

### 0.4 Interaction-surface migration has two residual seams — P2

- `components/chat/group/PrivacySeamDivider.tsx` still uses `Alert.alert` for an informational explanation; the design calls for a Toast or attached sheet.
- The canonical `ReceiptConfirmSheet` has not been extracted; booking and expense confirmation remain domain-specific.

`TextInputModal` is not a current gap: despite the old name, its implementation already uses the shared sheet/field/action-bar primitives.

### 0.5 Floating-tab blur is a technical deferral — deferred

The floating tab bar's geometry, inset contract, active state, hiding, and collapse behavior align. It uses parchment RGBA rather than the specified 12px blur because `expo-blur` is not in the build. Treat this as material polish after a native-dependency decision, not a functional blocker.

---

## 1. Trip, Itinerary, Changes, People, and Trip Settings

### 1.1 Operation previews and receipts are not consequence-rich enough — P1

The typed operation machinery is real and should be preserved. The gap is its traveler-facing consequence layer:

- `LowRiskOperationSheet` configures Move/Reorder through the newer relative Before/After placement model.
- Its preview largely humanizes `summary_code`, authority reason, and a generic provider note.
- It does not consistently show the design's useful `WAS / NOW` comparison, what changed, what stayed protected, travel/evening/provider consequences, and revalidation outcome.
- The landed state still exposes an operation-ID prefix and generic reason text.

**Required:** enrich the preview/receipt payload and presentation around the existing typed operation. Do **not** restore the obsolete absolute time-slot Move picker; relative placement is newer product truth.

### 1.2 Replace-and-rebook is not an explicit, informed choice — P1

The design separates “Replace itinerary only” from “Replace and rebook,” then previews provider availability, price, fee, refund, and refundability. Current code automatically builds replace-and-rebook whenever a protected item has a provider revision; otherwise it performs an ordinary replace.

Provider saga handling after commit is strong. What is missing is the pre-commit choice and its concrete provider/money consequences. This is a high-trust seam: automatic selection should not stand in for traveler consent.

### 1.3 Stale/concurrent recovery lacks the three-truth decision surface — P1

The backend and sheet can refresh/rebase a stale preview, but the UI collapses recovery to “Preview out of date / Review again.” The canonical recovery model preserves:

- prior truth,
- current truth,
- the traveler's draft,
- explicit rebase, discard, or leave-open decisions.

Implement this as a recovery state of the existing operation flow, not a second mutation system.

### 1.4 Optimize and Replan consequence depth — resolved 2026-07-17

`OptimizeRouteSheet` now shows distance saved plus a typed per-stop
classification and destination-local current/proposed position and time. Kept,
moved, retimed, and moved-plus-retimed stops therefore have explicit WAS/NOW
evidence before the canonical compound operation is committed. Map drag
remains an explicit deferral rather than an incomplete promise.

Replan now uses the generic operation preview contract to expose every atomic
child as added, moved, removed, or replaced, plus the count of unchanged stops
and protected provider dependencies. The review sheet renders those exact
server-authored consequences before its one atomic commit, and the landed
receipt persists and renders the revalidated structural delta. The residual is
also closed: every affected stop carries its grounded prior/proposed day and
local time plus outbound travel mode/minutes when known. Preview and landed
receipt render the same evidence; missing travel remains absent rather than
estimated. Route geometry and private planner rationale are deliberately
excluded from this group-safe contract.

### 1.5 Initial Split/Rejoin construction — resolved 2026-07-17

Production supports atomic parallel-plan operations, traveler assignment,
branch movement/expansion, detachment, rejoin, and recovery. Initial creation
now lets the traveler select any active same-day place for the other branch,
assigns every intervening stop explicitly so topology remains contiguous,
supports multiple travelers on either named branch, and chooses each decision
owner from that branch. The resulting preview remains one canonical
`create_parallel_plan` operation with one split, both branches, and one rejoin;
the UI does not sequence per-row mutations.

### 1.6 Trip cancellation and reuse — resolved 2026-07-17

Production supports organizer-only archive recovery, guarded trip
cancellation, and private reuse-as-template through the backend, generated
mobile contract, Trip context, and Trip Settings. Cancellation first exposes
provider/booking blockers, performs no provider cancellation itself, preserves
confirmed reservations and unsettled shares, retires forward coordination,
and leaves a readable cancelled record. Creation and queued-delivery paths
recheck terminal status so late work cannot quietly resurrect the trip.

Reuse is not recovery and does not copy live truth. It creates an undated solo
ideation draft from reusable day/block structure while stripping travelers,
bookings, Costs, votes, conversations, workflows, provider state, dates,
times, commitments, and prices. New provider work therefore requires fresh
selection and validation in the new trip.

### 1.7 Object Detail and Changes still leak engineering artifacts — P1

The object route has a useful typed anatomy, but traveler-facing output still includes phrases and values such as:

- “canonical operation,” “canonical sources,” and “ledger record,”
- raw reason codes,
- numeric model confidence,
- truncated linked target IDs,
- a “CANONICAL REFERENCE” block,
- operation-ID prefixes in Changes.

These violate the reference audit's binding doctrine: retain truth/provenance, but translate it into human relationships and recovery language. This is cleanup of a functioning page, not a call to remove object inspection.

The Changes screen also retains a double-header/blank-band seam. Do not copy the older mixed votes/history board or restore in-row Undo; the newer applied-history model and operation-detail recovery are the right architecture.

### 1.8 Trip-specific Notifications and Permissions are only partial — P1

**Notifications:** the design calls for Quiet this trip and per-family controls for live-trip, booking/stay, decisions, suggestions, story/memory, and emergency alerts. Frontend and backend currently store only `inherit | eager | minimal` cadence.

**Permissions:** the design distinguishes three editing modes, Costs/Booking authority, big-change voting, and separate Vesper draft/minor-fix/major-approval controls. Production has `open | review` plus one “Prepare itinerary changes” toggle; enabled operations all map to `prepare_preview`.

Both need durable backend policy and capability-aware UI. They are not just missing switches.

### 1.9 Trip Privacy remains backend-gated — deliberate deferral

The design includes story visibility, shared-link posture, Atlas saves, per-trip learning, learned-memory review, and profile inclusion. Production intentionally presents information and links to account-wide controls, explicitly deferring per-trip learning controls until they can be persisted.

Keep that honesty. Build durable per-trip fields before exposing the designed toggles.

### 1.10 Connected systems and Trip Info are incomplete — P2

- Trip Settings exposes Stay, Costs, and Story, but not the designed Bookings, Photos, and Atlas connections.
- Trip Info supports name, destination, dates, and travelers, but not optional description or Illustration/Photo/Minimal hero style.
- Proposal Detail supports neutral tallies and lazy-consensus behavior, but has no neutral “Skip vote” action.
- Date-change review covers substantive impacts in copy, but flattens them into a generic confirmation instead of grouped impact rows and conflicts.

Do not restore the design's obsolete queued date-change state; keep the newer preview → atomic replan model and improve only its information hierarchy.

### 1.11 Trip-creation proposal is missing editable evidence — P2

`TripCreationProposalCard` now has a safe in-card ambiguous-outcome error, so the old audit claim that failure is absent is stale. It still omits two designed behaviors:

- the anchors row carried by the evidence contract,
- row-level “Change” actions that seed a correction into the composer and refresh the same proposal.

### 1.12 Completed trips do not point to unresolved settlement — P1

Post-Trip Continuity assigns the factual completed Trip one responsibility that Memory must not absorb: if costs remain unsettled, show a quiet “ONE THING UNRESOLVED” pointer back to Costs/Trip Details. Neither the itinerary root nor the completed-trip shell currently renders that settlement query/pointer.

Memory correctly owns retrospective/story/feedback material. Add the unresolved factual pointer to the completed Trip, not to Memory.

### 1.13 Cross-device workflow adoption lacks the designed choice — P2

Durable workflows re-poll and render `PendingWorkflowStrip`; completed work gets a finished-while-away notice. What is absent is the distinct cross-device adoption state: explain that a build already running elsewhere was adopted, with “Watch it finish” and “Start fresh instead.”

This is a presentation/control gap on an existing durable workflow, not missing workflow persistence.

---

## 2. Stay, Booking, Costs, Auth, and External Sharing

### 2.1 Stay “Hold” overstates provider truth — P0

This is the audit's sole P0.

The enabled UI says “Held — confirm before it lifts” and renders `ON HOLD · LIFTS …`. The backend route writes only a `held_until` timestamp to the stay candidate and explicitly describes it as a **soft hold**. It creates neither a Booking object nor a provider operation.

The design expects the held room to be the same live transaction in Stay and Booking before becoming a confirmed Stay. Current code therefore presents internal decision-state as inventory truth.

**Required resolution—choose one:**

1. Connect Hold to a real provider/Booking hold with authoritative expiry and recovery; or
2. Rename/reframe it as an internal group decision reservation with no implication that inventory is protected.

Do not preserve the current wording while leaving the backend unchanged.

### 2.2 Stay comparison lacks decisive group context — P1

`StayCompare` renders price, terms, and votes. It does not render who saved each option or a concise differentiator. It accepts a recommendation prop, but the route never supplies it; the schema has `added_by` and `note` but no typed recommendation/reasoning contract.

Add saved-by identity and a typed differentiator/recommendation layer. Do not generate unsupported certainty from price/vote counts alone.

### 2.3 Booking group-consent states — resolved 2026-07-17

Production now persists included participants and their pending, approved,
declined, or excluded state; blocks provider confirmation while any included
traveler has not approved; names holdouts from the trip roster; lets the
controller remind only pending participants; records accepted nudge delivery;
and offers the explicit self-only scope reduction. Push and shared-chat cards
both deep-link to the booking session, while the existing durable four-hour
claim prevents repeated delivery.

### 2.4 Booking recovery coverage is partial — P2

Production strongly covers price change, ambiguous provider outcome, cancellation, multi-traveler fallback, handoff, and checkout recovery. The designed provider-down, missing-dates, dedicated missing-traveler, and “Notify me” states are not represented as a coherent family. Some belong before a booking session exists, so route ownership should be settled before building them.

### 2.5 Expense dispute lifecycle — resolved 2026-07-17

Production now persists dispute reason, note, state, resolution and actor history.
Only the payer or an assigned-share traveler may open; only the opener may
withdraw; the payer or a trip organizer may resolve. One open dispute suspends
the expense from settlement and blocks settle/delete, while existing live
payments must be voided before a dispute can open. Ledger/detail projection is
server-backed, and every transition posts an exact-expense trip-room receipt.
No money is silently edited by a dispute transition.

The older reimbursement row is not part of this gap. Recorded settlement payments and voiding are newer, more durable code truth and belong in the design-behind-code audit.

### 2.6 Place and venue share controls are absent — P2

The design specifies an owner-control sheet with copy, preview, native share, personal-note exclusion, and privacy posture. Place and Venue currently invoke native sharing immediately with a public URL. Add the owner-control surface and link state when these design-ready patterns move into the active release scope.

### 2.7 OAuth failure lacks its inline provider state — P2

The auth design keeps the selected provider in context, disables peers while loading, and turns a failed provider button into an inline retry state. `AuthProviderStack` accepts only a global loading flag; OAuth failures become transient toasts. Track the selected provider and render its failure/retry state inline.

---

## 3. Vesper Home, Chat, Voice, Search, and Notifications

### 3.1 Home Flight and Comparison families have no grounded producers — P1 / backend-gated

The canonical Home Deck includes:

- a Flight face with replacement options and “Send to group,”
- a two-column Comparison face with direct choice.

Frontend and backend registries currently support Pick, Call, Brief, Near You, Vote, Settle, and Readiness, but not Flight or Comparison. The canon itself says these await backend producers.

Build grounded producer/action contracts first. Do not add static front-end faces that imply live schedule or inventory knowledge.

### 3.2 The canonical Chat card catalog is only partial — P1

The attachment union and renderer cover many designed cards, but these remain absent or incomplete in production:

- contributor attribution on the persisted Itinerary/Day Plan stop grid,
- Memory/Atlas Draft,
- explicit consent path for sending a voice segment to the group.

`PlanReadyCard` now persists and renders the committed itinerary's complete
day/stop grid, including themes, stable block identity, wall-clock labels and
grounded outbound travel mode/minutes. Its compact state previews two days and
two stops per day; the in-card depth action reveals the complete snapshot, and
the primary action opens the canonical Plan surface. The remaining itinerary
gap is contributor attribution: the durable block model does not yet record a
reliable author, so the producer intentionally omits it rather than presenting
planner inference as fact. Memory/Atlas Draft still requires an attachment
schema, producer, persistence, renderer states, and actions—not just card
styling. Voice-segment sharing remains a separate consent-gated voice scope.

Chat Comparison is closed through the durable Stay candidate/vote substrate.
The persisted card carries every active candidate as factual data, orders its
preview by vote count with stable creation order as the tie-breaker, and exposes
the resolved vote phase without naming holdouts. The compact renderer shows two
options and routes to the complete Stay comparison for voting. This does not
close §3.1's Home Deck Comparison family, which remains correctly gated on a
separate Home producer contract.

The production Map/Route path is also closed. `post_map_route` answers explicit
map, connection and day-route questions with a typed, persisted route object
from the canonical `TripMapState` builder. It carries stable block identity,
coordinates, saved segment mode/minutes/distance, route-quality evidence, and
an explicit `routed` versus `straight_line` geometry source. The handler
refuses days with fewer than two placed stops, is retry-idempotent by tool-call
identity, and passes all visible route copy through the group privacy guard.
The renderer never presents a straight connector as routed truth, reports
omitted unplaced stops, and opens the canonical Map face focused on the first
stop. Keeping this as an explicit on-demand producer also preserves the card
catalog's one-object-per-conversational-moment rule.

Canonical Error/Recovery is now closed for the durable planning workflow.
Retryable workflow failures persist a `retrying` object that states no plan was
committed, explains that the background worker owns the retry, and deliberately
offers no competing Retry action. Terminal failures persist a distinct
`failed` object with a server-authored revised-request prompt; only that
explicitly retry-safe state exposes the composer action. Recovery cards are
deduplicated by workflow and terminal state, retain the internal error code for
diagnostics without displaying it as user copy, and are followed by the normal
`plan_ready` artifact when background recovery succeeds. Generic connection
and history-loading failures remain transient `ErrorBanner` UI rather than
durable artifacts, preserving the distinction between screen chrome and an
in-thread execution receipt.

### 3.3 Chat's depth law is not applied — P1

The design distinguishes object depth from destination navigation:

- Booking proposal → Full terms,
- Comparison → See all the differences,
- Vote → Who's voted,
- Research → How I chose,
- depth opens a centered `CardLift`; a destination pushes normally.

`CardLift` exists, but its only production consumer is `ConciergeCardDecisionSheet`. Wire the shared depth behavior into Chat's booking, vote, research, and future comparison objects.

### 3.4 Universal Search action receipts are inert — P1

Frontend routing already follows the canon's D25 ruling: an action receipt should navigate to its proposal, expense, booking, Changes context, or Ask Vesper, never replay the mutation. Backend search results still emit `route=None` with `is_action=True`; the overlay correctly disables rows with no destination.

This is a bounded backend fix: populate stable destinations and test each action family end to end.

### 3.5 Suggested follow-ups are not durable turn metadata — P2

Private-thread follow-ups are derived from a recommendation object. They disappear when that metadata is absent and are not part of the persisted terminal turn contract. Add typed `suggested_actions` to durable terminal metadata before expanding the pattern.

### 3.6 Voice has one residual identity artifact — P2 / flag-dark

The active overlay correctly removed named personas but still displays `Vesper · {city}`. The final voice canon uses only “Vesper” as session identity. Remove the contextual persona subtitle when the live-mic path is intentionally reopened.

Mic permission request/denied/limited screens are already implemented. Full-screen takeover and hold-to-talk remain canon-declared flag-dark and are not active regressions.

### 3.7 Notifications are substantially aligned — no active gap

Global, Trip Updates, Trip Scoped, and Personal modes; loading/empty/push-denied/stale-cache states; priority strip; routing; and mark-read behavior are implemented. Trip-specific alert-category preferences remain a Trip Settings contract gap in §1.8, not a missing Notifications center.

---

## 4. Atlas, Discover, Places, and Post-trip

### 4.1 Atlas cold start is a static subset of the designed seed system — P1

The design specifies a rotating, state-driven seed pool across:

- place seeds: Known Around, Everyday, Cities Been, Dreaming, Set Home,
- taste seeds: Food, Pace, Pulls,
- home unset → lead with Set Home,
- taste skipped → lead with a taste seed,
- home + taste present → lead with place seeds,
- one or two cards at a time, with lightweight first-tap progression.

Production has a static “Start with a place” entrance/search/home row plus one permanently retiring two-choice teaching prompt. It does not rotate families or select seeds from user state.

Implement a small deterministic seed selector and progression contract before adding more card variants.

### 4.2 Discover Map lacks the canonical scope/layer system — P1 / backend-gated

The map design owns a tappable scope pill, layer button, scope chooser, filter chips, and “Show pins.” Current code renders a non-interactive title pill and explicitly documents layer/filter controls as an extension point because the endpoint only supports city or coordinates.

Add the scope/filter contract and `MapLayerSheet` together. A decorative filter sheet with no query semantics would be false parity.

### 4.3 Discover Map is not trip-aware enough — P1

The design includes an active-trip context strip, in-plan markers, and a trip-aware Ask Vesper handoff. Current pins can render an `in_trip` inner dot, but the route accepts no `tripId`, shows no trip context strip, uses generic Ask copy, and opens venue detail without preserving trip context.

The marker primitive is partial implementation; context propagation and handoff are missing.

### 4.4 Discover Map pin and state taxonomies are incomplete — P1

The design uses shape as well as color: friend square, experience open ring, place/area, suggested dashed ring, in-trip dot, and saved ring. The current payload/canvas explicitly supports current venue pins only; friend and heterogeneous object types are deferred until the payload expands.

State gaps are also explicit:

- no location-denied state with “Use city scope,”
- no offline-cached posture that clearly limits the map to cached saved/trip pins,
- generic loading uses an activity indicator rather than the richer map-state treatment.

This needs backend object/type expansion, accessible shape encoding, and route-level state selection. Current cluster and pin accessibility labels are useful foundations.

### 4.5 Places and core Atlas reading surfaces are aligned — no active gap

Verified aligned or intentionally deferred:

- city/neighborhood share one Place route,
- Venue and Experience detail/action structures are implemented,
- Take states exist,
- Atlas Read/Time/Places and Readings shelf exist,
- `/your-map` now redirects rather than rendering a second Atlas map,
- riso/postcard generation infrastructure exists but remains flag-dark,
- People/Theme facets and Reel are explicit future scope.

The Atlas place-first home composition and editorial budget are newer than portions of the design; do not rewrite them back to the older order.

---

## 5. Corrections to the reverse one-line list in the reference audit

The reference document intentionally treated code-behind-design as a brief appendix. Several entries changed or needed finer direction judgment:

| Reference item | Current adjudication |
|---|---|
| Universal Search action rows `route=None` | **Still true**; §3.4. |
| Trip-creation anchors/correction/failure | **Partly true**: anchors and correction remain; safe in-card failure now exists; §1.11. |
| Home Flight/Vote/Comparison/Settle/Readiness | **Only Flight and Comparison remain**; Vote, Settle, and Readiness are implemented; §3.1. |
| Voice permission screens + takeover | Permission screens are **implemented**; takeover remains intentionally flag-dark; city subtitle remains; §3.6. |
| Costs disputed/reimbursement | **Dispute resolved** as a durable lifecycle; reimbursement was superseded by the recorded-payments ledger; §2.5. |
| `/your-map` should redirect | **Resolved**; it is now a redirect stub. |
| Adopted-workflow recovery band | Persistence/polling exist; the explicit adopted-running choice remains; §1.13. |
| Completed-trip settlement pointer | **Still true**; §1.12. |
| Atlas rotating seed pool | **Still true**; §4.1. |
| Atlas riso/render pipeline | Infrastructure exists and is flag-dark; not an active parity gap. |

Items not independently revalidated were not promoted into this audit merely because they appeared in the older one-line list.

---

## 6. Explicit exclusions: do not “fix” code toward stale boards

These visual differences are design-behind-code or intentional deferrals:

- Do not replace relative Move/Reorder placement with the old absolute time-slot picker.
- Do not merge open decisions and applied history back into one Changes timeline or restore in-row Undo.
- Do not restore the queued date-change model; keep preview → atomic typed Replan.
- Do not expose fourteen backend operation identifiers as fourteen top-level traveler actions.
- Do not add hard Delete without durable deletion/privacy semantics; Archive is the honest current action.
- Do not add per-trip privacy/learning switches before their values can be saved and enforced.
- Do not fake a Stay provider hold, Home Flight alert, or Home Comparison from ungrounded local data.
- Do not implement the obsolete reimbursement row over the recorded settlement-payment ledger.
- Do not reopen voice takeover, Atlas Reel, or People/Theme facets as release gaps while their flags/decisions remain deferred.
- Do not remove code-ahead reliability features such as operation authority, proposal saga recovery, group read sync, or roster gates just because Vesper 220 does not draw them.

---

## 7. Recommended engineering waves

### Wave 0 — restore truth and trustworthy enforcement

1. Resolve Stay “Hold”: real provider/Booking hold or honest internal-reservation wording.
2. Fingerprint Vesper 220; repair the five broken route owners; fail the gate on broken references.
3. Return the typography budget to baseline or lower, starting with the six highest-count files.

### Wave 1 — bounded, high-value seams

1. Populate Universal Search action destinations backend-side.
2. Add the completed-trip unresolved-settlement pointer.
3. Remove object-detail/Changes raw IDs, reason codes, confidence, and canonical-system language.
4. Apply correct State System postures to Atlas Unpacked and the global profile-fetch notice.
5. Add inline OAuth provider failure/retry.

### Wave 2 — full-stack canonical capabilities

1. Chat Map/Route, Comparison, Error/Recovery, Itinerary, Atlas Draft, and production Privacy Handoff; then CardLift depth behavior.
2. Discover Map scope/layer contract, trip context, heterogeneous pin types, denied/offline states.
3. Atlas state-driven seed selector and progression.
4. Stay comparison attribution/differentiators/recommendation.

### Wave 3 — workflow depth and lifecycle

1. Structured operation consequences and receipts.
2. Replace-only vs replace-and-rebook consent.
3. Three-truth stale recovery.
4. Replan typed delta and richer initial parallel-plan construction.

### Deferred activation work

Home Flight/Comparison producers, live checkout, per-trip privacy/learning, voice takeover, blur material, external-share owner controls, and Atlas deferred facets should advance only with their required contracts and product gates.

---

## 8. Evidence and validation

The audit used source code and contracts rather than screenshot comparison. Parallel investigations covered:

- Trip/Itinerary/Changes/People/Settings,
- Costs/Stay/Booking/Auth/Trust/Sharing,
- Home/Chat/Voice/Search/Notifications,
- a local pass over Atlas/Discover/Places/Post-trip and alignment tooling.

Focused suites reported by the domain passes:

- 81 Trip workflow tests passed across ChangeStudio, Parallel Plan, Proposal Detail, Changes, and Privacy.
- 32 Booking tests passed.
- 190 notification/cancellation tests passed after terminal delivery fencing.
- 148 scheduled-task/subscriber tests passed with one infrastructure-dependent skip.
- 87 lifecycle, pre-trip, and worker tests passed after recurring-job fencing.

Lifecycle claims were additionally checked against the cancellation preflight
and cancel routes, sanitized template-reuse route and copier, generated mobile
contract, Trip context actions, Trip Settings entrances, retained cancelled
record routing, Postgres cancellation race coverage, and template-reuse
copy/strip assertions.

Passing tests do not invalidate these findings; most gaps are accepted target omissions or unmodeled contracts rather than regressions against current assertions.

Direct checks:

- `node scripts/check-typography-budget.mjs` — **failed**, 65 vs baseline 63.
- Button, color, radius, shadow, and sheet primitives were inspected as source systems; no global font-family or Button-system fork was found.
- The design-alignment gate logic was inspected directly: `owned (BROKEN REF)` is not included in the failure set.

No implementation code was changed by this audit.
