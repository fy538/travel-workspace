# No-Claude-Design Tightening Sprint

> Status: operating spec
> Owner: founder / engineering
> Created: 2026-06-10
> Scope: product tightening that should happen directly in app/backend/docs before another Claude Design pass

This doc turns the current glue substrate into implementation contracts. Use it
for surfaces where the visual direction is already good enough, but the product
still needs state coverage, copy discipline, event wiring, and dogfood proof.

Claude Design is useful when we need new visual language or competing layout
directions. These items mostly do not need that. They need exact semantics.

## Product Bet

The recent substrate work has made Vesper more than a set of screens:

- cards can carry durable lifecycle and outcome context,
- `ConversationSeed` can carry entry-point context into chat,
- proposal receipts can make plan mutation inspectable,
- privacy redaction can prove private facts were used safely,
- notifications can route to outcomes instead of generic screens.

The next tightening pass should make these systems feel inevitable to the user.
Every proactive surface should answer:

1. Why is Vesper showing this now?
2. What can I safely do next?
3. Who can see this?
4. What happened after I acted, ignored, dismissed, or asked?
5. Can Vesper explain or undo the result?

## Non-Design Surfaces To Tighten First

| Priority | Surface | Why this can skip Claude Design | First artifact |
| --- | --- | --- | --- |
| P0 | Home card lifecycle | Visual language exists; missing part is state/event semantics. | Lifecycle matrix + event tests |
| P0 | First-contact Vesper seeds | The substrate exists; most work is caller migration and prefill discipline. | Entry-point seed matrix |
| P0 | Privacy and group-boundary copy | Trust depends on exact wording and defensive rendering. | Copy rules + leak fixture |
| P1 | Proposal receipts | Existing proposal UI can carry better structured receipt fields. | Receipt checklist + Changes walk |
| P1 | Notification -> card -> action routing | Push/feed routing needs shared priority and attribution rules. | Routing matrix |
| P1 | Empty/loading/failure states | No new visual system required; define state contracts per surface. | State matrix |
| P2 | Booking/stay/expense trust loop | Needs honesty and visibility rules before a bigger design pass. | Trust checklist |
| P2 | Atlas provenance/correction | Needs metadata and control rules before alternate visuals. | Provenance checklist |

## 1. Home Card Lifecycle Contract

Existing substrate:

- Backend `ConciergeHomeCard.lifecycle_state`: `preparing`, `ready`, `seen`,
  `dismissed`, `acted_on`, `expired`.
- Backend `ConciergeHomeCard.state`: `present`, `preparing`, `loading`,
  `absent`.
- Backend fields already include `authorship`, `open_behavior`,
  `dismissible`, `feedback_enabled`, `reason`, `reason_signals`, `agent_read`.
- Notification delivery can carry `outcome_id`; durable cards can carry stable
  card identity.

### Canonical Lifecycle Semantics

| Lifecycle | User meaning | UI obligation | Backend/event obligation |
| --- | --- | --- | --- |
| `preparing` | Vesper knows something is forming but it is not actionable yet. | Render as non-actionable or quiet loading; no fake CTA. | Do not mark seen or acted. Promote to `ready` or expire. |
| `ready` | This is actionable now. | Show primary CTA and optional why/tune/dismiss controls. | Impression can mark `seen` after visible dwell. |
| `seen` | User has had a fair chance to notice it. | Keep visible unless lower priority than a newer card. | Write `card_seen` or equivalent outcome once. |
| `acted_on` | User completed the intended next step. | Replace CTA with receipt or remove from attention slot. | Link action event to `card_id` and `outcome_id` when present. |
| `dismissed` | User said this is not useful now. | Hide optimistically; provide undo when local. | Persist suppression unless card class forbids dismissal. |
| `expired` | The moment passed. | Remove or show stale explanation only from history. | Stop ranking; keep audit if tied to notification/outcome. |

### Card Action Vocabulary

Use these same actions across cards before inventing new labels.

| Action | Meaning | Copy | Event |
| --- | --- | --- | --- |
| Primary CTA | Vesper's recommended next move. | Surface-specific verb, never generic `Open`. | `card_primary_action` |
| Ask Vesper | Start contextual private chat. | `Ask Vesper` or `Ask Vesper about this`. | `card_ask_vesper` with `conversation_seed` |
| Why this | Explain why Vesper surfaced it. | `Why this` | `card_explain` |
| Not now | Suppress for this context/window. | `Not now` | `card_dismissed` with reason `not_now` |
| Already handled | User says the real-world task is done. | `Already handled` | `card_resolved_by_user` |
| Undo | Restore an optimistic dismissal. | `Undo` | `card_dismiss_undone` |
| Tune | Change future card preferences. | `Tune` | `card_feedback_opened` |

### Copy Rules

- `reason` should answer "why now" in one sentence.
- `reason_signals` should be evidence, not marketing copy.
- `agent_read` should be Vesper's judgment, not a restatement of the title.
- A card with private influence must not expose the private fact in `title`,
  `body`, push copy, or group-visible receipt.
- Do not use `urgent` language for ambient or exploratory cards.
- If a card is stale, say why it is stale instead of pretending it is current.

### Engineering Slice

1. [x] Add a shared frontend card lifecycle helper that maps lifecycle/state
   into render affordances: actionable, muted, dismissible, show receipt, show
   stale.
2. [x] Add unit tests for each lifecycle/action pair.
3. [x] Add one screen test where dismiss hides a noncritical card and undo
   restores it.
4. [x] Add one test where `Already handled` produces an outcome and suppresses
   the card without deleting the underlying trip truth.
5. [x] Make push-focused cards open the exact card by `card_id` or fall back to
   the relevant trip/outcome with visible stale copy.

### Landed 2026-06-10

- Frontend card lifecycle affordances now gate deck actions, impressions,
  decision sheets, primary actions, `Not now`, `Already handled`, and inactive
  states.
- Backend lifecycle writes now preserve a rolling audit in
  `vesper_cards.source.lifecycle_events`, including UI metadata when present.
- Restore/Undo now records an append-only `undo_dismiss` feedback marker and
  invalidates feedback-derived tuning, so restored cards do not disappear again
  after refetch.
- Card UI events now use the canonical vocabulary above in lifecycle metadata
  and telemetry contexts for primary, ask, explain, dismiss, undo, tune, and
  already-handled paths.
- Push-focused cards render a visible stale-card notice when the target card is
  no longer active.
- `seen` now records only after an 800ms focused Home dwell, with timers
  cancelled when cards leave view or Home loses focus.
- Home now shows small lifecycle receipts for primary action, Undo restore, and
  `Already handled` outcomes.
- Backend lifecycle has a Postgres canary covering durable card creation,
  active-feed listing, seen audit metadata, dismissal removal, restore, and
  audit preservation.

## 2. First-Contact Vesper Seed Matrix

Existing substrate:

- `ConversationSeed` standard exists in `travel-app/docs/conversation-seed/Standard.md`.
- Backend prompt assembly can resolve server entities or client-provided context.
- The bug class is mostly unmigrated entry points that still pass only a prefill
  string.

### Seed Requirements

Every Vesper entry point must choose one of these shapes:

| Entry point | Required seed | Prompt behavior | Privacy |
| --- | --- | --- | --- |
| Home card | `surface: home_card`, `clientContext`, optional `tripId` and entity | Prompt may auto-send if the user tapped a clear CTA. | Private by default unless card is explicitly group-visible. |
| Discover dossier | `surface: dossier`, `entity: dossier`, optional `tripId` | Prompt should be short: `Help me use this`. | Do not send personalized rationale to group. |
| Venue/place/accommodation | `surface` + server entity id | Prefer server resolution over URL blob. | Group handoff strips private `why_for_person`. |
| Invite | `surface: notification` or `generic`, `tripId` | Do not auto-send. Let user ask candidly first. | Private first impression. |
| Blank trip idea | `surface: generic`, optional prompt | Auto-send only if user typed text. | Private until promotion. |
| Proposal receipt | `surface: plan`, `tripId`, proposal id when available | Ask should include "why this changed" or "what changed". | Use group-safe receipt fields. |
| Atlas artifact | `surface: atlas_search` or `me`, entity/artifact id | Prompt should ask how to use/correct memory. | Private memory controls. |
| Push/deep link | `surface: notification`, `tripId`, `outcome_id`, optional `card_id` | Do not invent context if ids are missing. | Route private outcomes to private chat. |

### First-Contact Copy Standard

Avoid cold chatbot copy:

- Do not use: `How can I help?`
- Prefer: `I have the context. What do you want to do with it?`
- For a vague idea: `Tell me what kind of trip this wants to become.`
- For a place: `Want my read on whether this belongs in your trip?`
- For an invite: `Want to think through whether this trip fits you?`
- For a proposal: `Want the plain-English version of what changed?`

### Engineering Slice

1. Inventory all callers of `routes.conciergeChat` and classify them as migrated
   seed, legacy metadata, or bare prefill.
2. Migrate the top five visible call sites first: Home card, Discover dossier,
   venue detail, accommodation detail, proposal receipt.
3. Add a route/seed snapshot test for each migrated call site.
4. Add a backend dispatcher test for each entity type used by the migrated
   call sites.

## 3. Privacy And Group-Boundary Copy

Privacy is not just redaction. It must be legible without becoming scary.

### Copy Primitives

Use these exact meanings consistently:

| Situation | Preferred copy | Avoid |
| --- | --- | --- |
| Private intake | `Only you can see this.` | `This is confidential` |
| Private signal used safely | `I used this privately to shape the recommendation.` | `Based on your private note...` |
| Public redaction | `I kept the reason group-safe.` | `I hid the details.` |
| Group-safe proposal | `The group sees the plan impact, not the private source.` | Naming the protected user or fact |
| Private-to-group handoff | `I can turn this into a group-safe proposal.` | `Share this with the group` |
| Better as private | `This should stay between us unless you choose otherwise.` | Generic warnings |
| Audit receipt | `What Vesper used` / `What stayed private` | Security jargon |

### Defensive Rendering Rules

- Group surfaces must drop private rationale fields even if the backend
  accidentally sends them.
- Push, SMS, email, and notification list copy must use the strictest privacy
  copy, because they can appear outside the app.
- Booking notes and provider handoff copy must never contain raw private
  constraints unless the user explicitly typed them into a provider-facing form.
- Privacy audit should show categories and redaction proofs, not raw protected
  text.

### Engineering Slice

1. Add a deterministic fixture with one private constraint flowing through
   private chat, group proposal, notification, booking note, plan badge, and
   privacy audit.
2. Assert the raw private value never appears on group, notification, booking,
   or provider surfaces.
3. Assert the owner can inspect an audit receipt that explains safe use without
   echoing the raw private value.
4. Add a UI-side guard for any `why_for_person` or personalized rationale field
   rendered in group context.

## 4. Proposal Receipt Checklist

Existing direction is strong: proposals bridge Vesper's judgment, group
alignment, and plan truth. The next pass should make every applied change leave
a small, inspectable receipt.

### Receipt Must Answer

| Question | Field / surface |
| --- | --- |
| What changed? | human summary + affected block ids |
| Why did it change? | group-safe reason |
| Who can see this? | visibility label |
| What did Vesper skip? | skipped/conflict notes when relevant |
| Is the plan now updated? | Plan/Changes source read model |
| Can it be undone? | revert eligibility + disabled reason |
| Where else should this appear? | Home, Map, Chat, notification routing |

### Receipt Copy Rules

- Use "changed", "kept", "declined", and "restored" consistently.
- For accepted proposals, say what is true now, not just that a vote passed.
- For rejected proposals, reassure that the original plan remains intentional.
- For reverted proposals, name what was restored and what cannot be restored.
- When private signal informed the change, the receipt says `group-safe reason`,
  not `private reason`.

### Engineering Slice

1. Promote the existing proposal canary into a standing CI/dogfood gate.
2. Add an app-level Changes surface walk on top of the backend canary fixture.
3. Assert chat receipt, proposal detail, Plan recent changes, Home, Map, and
   notification all agree on the same proposal id and applied state.

## 5. Notification To Card To Action Routing

Notifications should not be a separate product. They are the interruptive edge
of the same card/outcome system.

### Routing Priority

When a push/feed item is tapped, choose destination in this order:

1. `card_id` present and active -> focused Home card.
2. `outcome_id` + `private` -> private Concierge chat or private outcome detail.
3. `proposal_id` -> proposal review sheet/detail.
4. `trip_id` + known action type -> exact trip subroute.
5. `conversation_id` -> conversation.
6. Fallback -> notifications feed with stale/missing-context explanation.

### Attribution Rules

- Tap records `engaged`, not merely `seen`.
- Opening the app from a push must preserve `outcome_id` and `card_id`.
- If the target is expired, record engagement and show stale copy.
- If the target is private and the user is not the owner, route to a safe
  fallback, not group chat.
- Feed routing and push routing must share the same resolver.

### Engineering Slice

1. [x] Add a shared notification target resolver used by feed taps and push
   taps.
2. [x] Add a PushRegistrar routing matrix test for `card_id`, private
   `outcome_id`, proposal, trip action, conversation, expired, and missing ids.
3. [x] Add one integration test that push tap opens the exact card and marks
   the outcome engaged.

### Landed 2026-06-10

- `utils/notificationDestination.ts` is the shared resolver for OS push payloads
  and in-app notification rows.
- `card_id` now has priority over generic proactive chat/outcome routing and
  routes to focused Concierge Home.
- Map-view push routing keeps the leave-by dismissal side effect while using
  the shared destination contract.
- Proactive notification rows can carry `card_id` through `AppNotification`.
- PushRegistrar now has a component-level OS-push matrix covering live tap,
  cold-launch tap recovery, foreground seen events, outcome engagement dedupe,
  exact-card Home routing, private outcomes, proposals, trip actions, map
  focus, conversations, stale-card ids, and missing-target no-ops.

## 6. Empty, Loading, Failure, And Silence States

These states need one shared rubric. The app should never fill uncertainty with
fake confidence.

| Surface | Loading | Empty | Failure | Silence / privacy |
| --- | --- | --- | --- | --- |
| Home cards | `preparing` card or quiet lead note | starter only if useful | stale/fallback card with no fake CTA | explain when Vesper is staying quiet |
| Vesper chat | streaming status and tool-status copy | seeded first-contact prompt | retry + preserved draft | private/group boundary explanation |
| Discover | skeleton rows tied to feed sections | one useful search/ask action | cached content + retry | no private why in group context |
| Atlas | scan/provenance progress | explain what is needed to learn | retry scan or privacy settings path | controls remain private |
| Proposal receipt | resolving/applied state | no open decisions | show not-applied/conflict state | group-safe reason only |
| Booking/stay | provider refresh in progress | no stay yet, add or ask Vesper | availability stale / provider unavailable | private stay notes hidden |
| Trip story | generating story | no moments captured yet | story not ready, preserve photos | memory write-back preview |

### Engineering Slice

1. [x] Make Concierge Home distinguish first-load loading, hard refresh
   failure, and stale cached data.
2. [x] Make Plan empty days distinguish suggestion loading, true empty, and
   retryable suggestion failure while preserving manual add actions.
3. [x] Add a compact state contract helper/copy map for repeated loading,
   empty, stale, and failure language.
4. [x] Audit Map, Atlas, Booking/stay, and Story for fake-empty states.
   - Booking session hard-failure state is landed.
   - Trip Story composing now renders as progress, not true empty.
   - Trip Map and Atlas Map already had hard-failure guards; tests now pin
     those branches so they do not regress into empty guidance.
5. [x] Add screen tests for one empty, one loading, one stale, and one hard
   failure path per promoted journey.

### Promoted Journey State Matrix

| Journey | Loading / progress | Empty | Stale / preserved | Soft failure | Hard failure | Test anchor |
| --- | --- | --- | --- | --- | --- | --- |
| Concierge Home | `Refreshing Home` skeleton | local starter only on success | `Home may be out of date` keeps cached queue visible | stale/missing target card notice | `Couldn't refresh Home` | `concierge-home.smoke` |
| Vesper chat | `Opening Vesper` history skeleton + editorial streaming copy | first-contact composer suggestions | failed user turn remains retryable; draft/text preserved | stream/tool error banner retry | `Couldn't load messages` | `concierge-chat.smoke` |
| Trip Plan | `Opening the itinerary` skeleton | `No plan sketched yet` cold-start card | `Plan may be out of date` keeps cached plan/legacy days visible | Morning briefings compact retry | `Couldn't load your plan` when both plan-state and itinerary fallback fail empty | `plan.smoke`, `surfaceStateCopy.test` |
| Plan empty day | `Finding nearby venues...` | `Nothing seeded yet` with Add / Free time | N/A: seeded suggestions are not cached as stale data | suggestion retry while manual add remains available | `Couldn't load suggestions` | `PlanEmptyDay.test` |
| Dossier reader | `Opening the read` skeleton | `This read needs more material` for partial body payloads | `This read may be out of date` keeps cached editorial copy open | image/related-content fallback without blocking the read | `Couldn't load this read` | `dossier-detail.smoke`, `surfaceStateCopy.test` |
| Expenses | `Balancing costs` skeleton | `No shared costs yet` with Add expense | `Costs may be out of date` keeps cached ledger visible | filtered category empty / settle mutation toast | `Couldn't load expenses` | `surfaceStateCopy.test` |
| Booking session | offer/session skeleton | `No offers yet` only after successful read | out-of-date booking banner when cached data refresh fails | provider receipt pending/unavailable copy | `Couldn't load booking options` | `booking-confirm.test` |
| Trip Story | `Loading story` / `Composing your story` | `No story yet` only when not composing | N/A: composed story stays visible on cached refetch failure | missing media stays non-blocking | `Couldn't load your story` | `story.smoke` |
| Trip Map | map-state fetch guard | live map fallback with itinerary guidance | N/A: map state does not show stale markers after hard failure | marker/detail fallback while map remains usable | `Couldn't load map` | `map.smoke` |
| Atlas Map | year/map read model progress via existing chrome | private-geography empty copy | N/A: private geography does not render stale nodes on hard failure | per-place media/provenance fallback | `Couldn’t load your map` | `atlas-map.smoke` |

### Landed 2026-06-12

- Expanded the shared promoted-journey copy contract so Home, Vesper chat,
  Dossier, Trip Plan, Expenses, Booking/stays, Trip Story, Trip Map, and
  Atlas Map each explicitly carry
  loading, empty, stale, soft-failure, and hard-failure semantics.
- Concierge Home now has literal screen coverage for empty, loading, stale,
  soft-failure, hard-failure, current CTA routing, decision-sheet paths, and
  Deck utility actions.
- Trip Story now shows a stale refresh banner while keeping a cached composed
  story visible; Trip Map has visible loading copy; Atlas Map now routes empty
  and failure copy through the shared state contract.
- Added literal screen coverage for the previously under-pinned Dossier, Trip
  Plan, Expenses, and Booking/stays branches. Chat now asserts the blank-thread
  composer suggestions as its empty path.
- Booking/stays now has visible loading copy (`Loading booking options`) and
  routes the successful empty-offers copy through the shared matrix.
- Expenses routes its filtered-category soft-empty state through the shared
  matrix, preserving the full ledger while making the scoped empty state clear.

### Landed 2026-06-11

- Trip Plan now keeps cached plan-state or legacy itinerary days visible when a
  refresh fails, with `Plan may be out of date` retry copy. The hard failure
  path now only wins when both plan-state and itinerary fallback leave the
  surface empty.
- Dossier reader now preserves cached editorial content through refetch errors,
  marks it stale, and renders a partial-payload empty body instead of a silent
  blank read.
- Expenses now separates first-load loading, true empty ledger, stale cached
  ledger, category soft-empty, and hard failure states.
- `surfaceStateCopy.test` pins the promoted journey copy matrix for Home, chat,
  Trip Plan, Dossier, Expenses, and Booking so the sprint contract stays
  explicit.

### Landed 2026-06-10

- Concierge Home no longer falls through to local fallback cards when the
  backend Home feed fails before data exists. It now shows a retryable
  `Couldn't refresh Home` state.
- First-load Home feed loading renders explicit skeleton content labelled
  `Refreshing Home`, instead of presenting generated relevance while the real
  queue is unknown.
- If Home has cached backend data but refresh fails, the last Vesper queue stays
  visible with an explicit `Home may be out of date` retry banner.
- Concierge Home smoke tests cover first-load loading, hard failure/no fake
  fallback cards, and stale-data refresh failure.
- Plan empty days now preserve the Add / Free time actions when seeded venue
  suggestions fail, show an explicit retryable `Couldn't load suggestions`
  state, and keep the existing `Finding nearby venues...` and true-empty copy
  distinct.
- PlanEmptyDay tests now cover phase copy plus suggestion loading, retryable
  failure, and successful empty results.
- `utils/surfaceStateCopy.ts` now holds the shared state-copy contract used by
  Concierge Home and Plan empty-day suggestion states, so these copies are
  asserted as product semantics rather than one-off string literals.
- Booking sessions now distinguish failed offer/session reads from "agent is
  searching" emptiness. Hard failures show a retryable
  `Couldn't load booking options` state, while cached data can remain visible
  behind an out-of-date refresh banner.
- Booking screen tests now assert the hard-failure path does not fall through to
  the searching-empty copy and that retry reissues the offers request.
- Trip Story now treats backend `composing` as an explicit progress state with
  story-shaped skeleton content, instead of showing `No story yet` while the
  background composition job is active.
- Story tests now cover loading, composing, true empty, retryable hard failure,
  and populated story rendering.
- Trip Map and Atlas Map tests now assert hard failures render retryable
  `ErrorState` branches instead of their itinerary/private-geography empty
  guidance.
- Vesper chat now uses the shared state-copy contract for history loading and
  history failure. Initial thread load shows `Opening Vesper`; failed history
  shows retryable `Couldn't load messages`.
- Chat-level stream errors now keep the failed user turn visible and wire the
  top error banner's `Retry` action to the latest failed user message, falling
  back to history refetch when there is no failed draft to retry.
- Concierge chat smoke tests now cover opening/loading, hard history failure,
  editorial streaming copy that hides raw tool labels, and retrying the latest
  preserved failed turn from the banner.

## 7. Booking, Stay, Expense Trust Rules

Before a new visual pass, lock these rules:

- Vesper can recommend, compare, prepare, and hand off.
- Vesper must not imply a booking happened unless a confirmation exists.
- Price and availability must have a timestamp or stale label.
- Provider handoff is explicit: "Book with provider", not "Book now" unless
  first-party booking is real.
- Shared lodging and private lodging need explicit visibility labels.
- Confirmed booking does not auto-create a shared expense.
- Expense creation should be opt-in and explain who can see it.
- `Ask Vesper` from booking/stay must carry trip, stay, provider, and visibility
  context.

### Landed 2026-06-10

- Booking offers now show a visible freshness line. When the backend does not
  provide provider-specific checked timestamps, the UI uses the successful
  offers-read time (`Checked just now`, `Checked 12m ago`) rather than leaving
  price/availability trust implicit.
- Expired or stale offers now show `Price or availability may have changed` or
  `Refresh before confirming`, and the booking screen keeps the stale-data
  warning visible when dependent reads fail after cached data exists.
- The booking session footer no longer uses one generic `Confirm selections`
  verb. In dogfood/non-live booking mode it says `Prepare handoff`; selected
  provider-link offers say `Open provider to book`; true direct booking copy is
  reserved for live-booking-enabled `L3_cart` sessions.
- Provider-link handoffs open the provider instead of calling the in-app
  confirm mutation, and the alert explicitly says Vesper will not mark the
  booking confirmed until the provider step is done.
- Successful non-live cart confirmation now toasts `Booking handoff prepared`
  instead of `Booking confirmed!`.
- Booking offers now render a compact terms strip before confirmation: price,
  taxes/fees, cancellation, payment timing when present, checkout path, and a
  receipt-boundary footnote. Missing taxes/fees are explicit
  `Provider confirms at checkout`, not silent.
- The terms resolver is intentionally narrow and fact-based. It reads current
  `BookingOffer.normalized`, `provider_response`, and top-level price fields;
  it does not create a checkout surface or invent provider guarantees.
- Booking confirmation cards now resolve state from provider proof, not booking
  method names. `Booked` only renders when a provider confirmation/reference is
  present; API sessions without proof render `In progress`, deep links render
  `Handoff ready`, and voice paths render `Call to confirm`.
- Backend booking-confirmation fallback copy follows the same boundary, so
  older clients and unstructured fallbacks do not claim `Booking confirmed`
  for provider handoffs.
- Travel Agent now persists a canonical offer-facts contract into
  `BookingOffer.normalized`: `checked_at`, `total_price`, canonical
  `price_breakdown.taxes_and_fees`, `provider_terms_url` for deep links, and
  existing `booking_method` / cancellation fields. Seed offers no longer invent
  a zero-price payload.
- The app terms/freshness resolver now understands the new normalized
  `total_price` and `checked_at` fields while remaining tolerant of older
  payloads.

### Close-the-gap posture

- First close visible trust gaps: terms, total-price/fee transparency, receipt
  boundary, and stale-provider language.
- Then light up one live-booking provider behind a hard-off flag.
- Do not build a universal checkout, payment vault, or provider-management
  system until one provider proves the full confirmation loop.

## 8. Atlas Provenance And Correction Rules

Before another Atlas visual pass, lock:

- Every memory/signal says whether it is confirmed, inferred, imported, or
  suggested.
- Every learned signal has a source/provenance route.
- User can keep, dispute, forget, or restore when supported.
- Removing a signal explains whether it deletes the artifact, hides the signal,
  or stops future recommendation influence.
- Privacy audit and Atlas receipt should agree on what was used.
- Travel DNA changes should produce a small receipt: what changed, from what,
  and where it may influence Vesper.

## Sprint Plan

### Slice A - Home Card Lifecycle

Outcome: every visible card action has a lifecycle meaning, event name, and
state transition.

Checklist:

- [x] Add lifecycle rendering helper in app.
- [x] Add lifecycle/action unit tests.
- [x] Add dismiss + undo screen test.
- [x] Add `Already handled` outcome test.
- [x] Add push-focused-card stale/fallback behavior.
- [x] Make `seen` dwell-based.
- [x] Add small lifecycle receipts for acted/restored/handled outcomes.
- [x] Add durable-card DB lifecycle canary.

2026-06-10 note: first app slice added `lifecycleAffordanceForCard`,
canonical card UI event names, non-actionable rendering for inactive lifecycle
states, Deck action gating, and focused utility coverage. Concierge Home smoke
coverage now protects dwell-based seen, dismiss/undo, primary-action receipt,
and handled receipt paths.

2026-06-10 note: second app slice added the Deck `Already handled` action for
task-like cards, records it as `acted_on` with explicit
`card_resolved_by_user` metadata, hides optimistically with Undo, and covers
eligibility + Deck emission in tests.

2026-06-10 note: third app slice made push-targeted `card_id` links explicit:
the targeted card bypasses local tuning/suppression when it is still active,
and missing/expired targets show stale-card copy after Home refreshes instead
of silently landing on the default queue.

2026-06-10 note: fourth app slice added explicit screen coverage for the
era-2 FocusHome Deck `Not now` path: long-press opens the Deck, `Not now`
hides the card, feedback persists as `not_now`, and Undo restores the card.

### Slice B - Conversation Seed Migration

Outcome: the most visible Vesper entry points stop arriving cold.

Checklist:

- [ ] Inventory all `conciergeChat` callers.
- [ ] Migrate Home card, Discover dossier, venue, accommodation, proposal.
- [ ] Add seed snapshot tests.
- [ ] Add backend resolver tests for migrated entity types.

### Slice C - Privacy Proof Fixture

Outcome: Journey 04 can move from "fixture gap" to deterministic proof.

Checklist:

- [ ] Create one private constraint fixture.
- [ ] Trace through private chat, group proposal, notification, booking, plan
      badge, Atlas/privacy receipt.
- [ ] Assert raw private value is absent from group-visible/output surfaces.
- [ ] Assert owner audit explains safe use.

### Slice D - Proposal Receipt Walk

Outcome: Journey 05 becomes app-visible, not just backend-canary strong.

Checklist:

- [ ] Promote proposal canary to standing gate.
- [ ] Add Changes surface walk.
- [ ] Assert receipt id/state agreement across Chat, Plan, Home, Map,
      Notifications.

### Slice E - Notification Resolver

Outcome: push and feed taps share exact routing semantics.

Checklist:

- [ ] Extract shared target resolver.
- [ ] Add routing matrix tests.
- [ ] Preserve `card_id` and `outcome_id` through app launch.
- [ ] Record tap as engagement.

## Definition Of Tightened

A surface is tightened when:

- happy path works,
- loading/empty/failure/stale/private states are named,
- every CTA has a state transition or is disabled,
- every proactive item has a why-this explanation,
- every notification/card action writes an outcome,
- private fields are defensively suppressed on group surfaces,
- mock mode does not hide a real-backend contract,
- at least one deterministic test protects the highest-risk path.

This is the bridge between substrate and dogfood. The goal is not to make more
features. The goal is to make the existing intelligence feel coherent, honest,
and safe.
