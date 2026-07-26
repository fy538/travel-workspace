---
doc_type: working
status: active
owner: founder / engineering
created: 2026-07-25
last_verified: 2026-07-25
expires: 2026-08-24
why_new: The canonical proactive-notifications charter describes the current proactive pipeline, but this investigation spans notifications, activity rows, cards, chat, remote channels, and future live travel surfaces. It must remain a proposal until the target boundary and in-flight notification schema are adjudicated.
promotes_to: docs/systems/proactive-notifications.md plus an architecture decision record
supersedes: []
source_of_truth_for: [notification-attention-refactor-roadmap-2026-07]
---

# Notification and Attention Architecture — Consolidated Research and Roadmap

> [!IMPORTANT]
> **Phase 0 boundary adjudicated in the current uncommitted branch.**
> A local persistent database had already applied `notifrecord01`, so its
> revision identifier and original operations are retained as migration-history
> compatibility. Follow-on migrations rename and narrow that table to
> `notification_envelopes`, make learning outcomes optional correlation, and
> correct deletion semantics. Home cards do not create or link envelopes.
> This chain has been upgraded through `notifenv04` and checked against real
> Postgres locally; it still requires normal branch review before any shared
> environment rollout.

## Question and decision

How should the product evolve from its current collection of proactive candidates,
deterministic push senders, activity-feed rows, Home cards, conversations, and
background travel signals into a coherent attention system without putting
transactional truth behind a learned engagement model or forcing every surface
through a notification-shaped abstraction?

The recommended direction is:

1. Keep arbitration optional and restricted to inferred/proactive opportunities.
2. Give related user-visible projections a stable cross-surface attention identity
   and lifecycle.
3. Build one delivery spine for inbox and remote-provider delivery.
4. Keep Home cards, request-time ambient cards, conversations, and live travel
   surfaces as projections rather than pretending they are transport channels.
5. Migrate producer by producer, with shadow comparison and separate device proof.

This is a refinement of the earlier “one Notification type plus one delivery
spine” proposal. That proposal correctly separated the decision to speak from
delivery policy, but `Notification` is too narrow to be the root product object:
the product also exposes attention through cards, activity rows, chat, and
potentially bounded live sessions.

## Executive conclusion

The durable conceptual flow is:

```text
domain event or current truth
        ↓
user-relative attention case
        ↓
[arbitration — inferred opportunities only]
        ↓
projection decision
        ├── activity/feed row
        ├── actionable or ambient card
        ├── conversation
        ├── inbox/remote notification → delivery spine
        └── bounded live travel surface
        ↓
visibility, work, truth, projection, and delivery outcomes
```

The architecture must answer three questions:

1. **Does this deserve attention?**
   Deterministic product truth normally does. Inferred opportunities must earn
   exposure through arbitration.
2. **Which surface is appropriate?**
   The system chooses passive availability, an actionable surface, conversation,
   an interruption, or a bounded live surface.
3. **How is that projection delivered?**
   Inbox and remote delivery own preferences, quiet hours, caps, channel
   resolution, expiry, replacement, provider dispatch, receipts, and terminal
   outcomes.

Only the third question belongs to the remote delivery spine. Request-time Home
cards should not be routed through push/SMS mechanics merely to reuse policy.

## Reconciled vocabulary

### Domain event or current truth

The authoritative fact: a booking was confirmed, a proposal needs a vote, a gate
changed, a traveler left the group, or the current itinerary has a feasibility
problem.

This truth remains owned by the booking, proposal, membership, itinerary, expense,
or other domain system. Attention infrastructure never becomes the source of
trip truth.

### Attention case

The user-relative reason a fact or opportunity may deserve awareness or work.
Examples:

- “Fei’s booking is confirmed.”
- “Fei still needs to vote on proposal 123.”
- “This traveler’s route to the airport has entered the leave-now window.”
- “This nearby venue is a plausible ambient opportunity.”

An attention case has a stable key. Phase 1 includes a minimal
`attention_cases` table because the flagship Catch lifecycle crosses producers,
time, and surfaces. Short-lived request-time ambient opportunities may remain
ephemeral only when they cannot create a second projection and do not need
cross-surface cancellation, supersession, or recipient state.

### Arbitration

The decision about whether an inferred opportunity should be surfaced. It may
return:

- `send`
- `defer`
- `downgrade`
- `suppress`

Transactional facts, receipts, membership changes, and canonical booking truth
must not be engagement-suppressed.

### Intervention

An evaluation or exposure decision for an attention case. This is useful
telemetry terminology, but it should not be the universal persisted product
object.

### Projection

A concrete representation of an attention case:

- activity/feed row;
- durable actionable card;
- request-time ambient card;
- chat/conversation message;
- push, SMS, or email;
- live travel session.

Each projection owns its surface-specific rendering and interaction behavior
while sharing stable attention identity, truth state, expiry, and destination.

### Delivery attempt

One provider-specific attempt to deliver an inbox or remote projection. It owns
provider identifiers, timestamps, status, and error detail. A durable Home card is
not a provider delivery attempt.

## Classification axes

Avoid a single enum that attempts to encode every concern. Declare independent
axes on the type registry.

### Decision mode

- `deterministic`: product truth or a rule decided the case must exist.
- `inferred`: the product is guessing that an unsolicited opportunity is useful.

Only `inferred` enters learned arbitration.

### Attention class

- `ambient`: useful if discovered; should not wake the user.
- `ledger`: durable awareness/history without required work.
- `transactional`: user or group action caused a meaningful update.
- `time_critical`: delay materially reduces usefulness or safety.

### Lifecycle kind

- `update`: informational lifecycle, such as booking confirmation.
- `open_loop`: work remains, such as a vote or approval.
- `live_session`: bounded, evolving active travel state.
- `ambient_opportunity`: eligibility, exposure, dismissal, and expiry.

### Audience and privacy

- private traveler;
- selected recipients;
- group-safe audience.

Audience is an authority boundary, not a presentation preference. Private facts
must never be composed into group-visible text. Group-visible prose must use the
canonical group-safe composition/redaction path.

## State model

Do not collapse lifecycle into `is_read`.

| Dimension | Representative values | Meaning |
|---|---|---|
| Visibility | `unseen`, `seen`, `read` | Whether the user has encountered the projection |
| Work | `informational`, `open`, `snoozed`, `completed` | Whether user action remains |
| Truth | `current`, `stale`, `superseded`, `canceled` | Whether the underlying assertion is still valid |
| Projection | `active`, `transformed`, `superseded`, `canceled` | Envelope/surface-specific lifecycle; durable cards retain their richer presentation lifecycle |
| Delivery | `pending`, `sent`, `delivered`, `failed`, `skipped`, `canceled` | Provider attempt lifecycle; provider acceptance remains ticket metadata until receipt reconciliation |

Consequences:

- “Mark all read” changes visibility, not work.
- Voting completes the open loop and cancels pending reminders.
- A changed booking can supersede an old confirmation without erasing history.
- Dismissing an ambient card does not falsify its underlying venue or trip data.
- Provider acceptance is not proof that a device rendered the message.

GitHub provides one concrete product precedent for separating inbox visibility
from disposition through distinct read, done, saved, and unsubscribe operations:
[GitHub notifications](https://docs.github.com/en/subscriptions-and-notifications/concepts/about-notifications).
The separation in this proposal is primarily derived from this product's own
vote, booking, Catch, and read-state bugs; it does not depend on that precedent.

## Current implementation assessment

### Valuable correctness work already in flight

The current notification branch contains useful corrections:

- inbox and push booking destinations are converging on the same `booking_ref`;
- quiet-hours timezone fallback is more consistent;
- the cross-trip interruptive cap is reserved atomically;
- Expo ticket IDs are persisted and a receipt reaper polls terminal receipts;
- deterministic notifications no longer need a fabricated chat-message row;
- the activity feed can read from a durable notification parent;
- notification response states no longer leave some terminal outcomes unread.

These corrections should be completed before broad migration.

### Phase 0 resolution of the in-flight one-way-door boundary

The original uncommitted `notification_records` declaration on
`codex/notification-correctness-baseline` described itself as the
durable parent “for every class,” while `home_card` remains a
`notification_deliveries.channel`. It is already integrated into
`fan_out_to_channels()`, `on_notification_sent()`, delivery creation, and the
notification feed. The migration is forward-only after delivery records exist.

That risks codifying two structural errors:

1. A durable Home card is a projection with its own lifecycle, not a remote
   provider attempt.
2. `notification_records.content` can duplicate booking, proposal, message, or
   card truth and become stale independently.

Phase 0 resolves that boundary as follows:

- keep `notification_deliveries` as the provider-attempt ledger;
- keep `notification_outcomes` as optional response/learning telemetry;
- preserve `notifrecord01` because it had already reached a local persistent
  database, then rename and narrow its table in `notifenv02`;
- use `notification_envelopes` only for inbox/remote content and policy
  snapshots;
- let deterministic delivery proceed without a learning outcome;
- make outcome deletion clear optional correlation rather than erase an
  envelope-owned delivery;
- make envelope deletion own cleanup of its delivery ledger;
- keep `home_card` only as a temporary delivery-ledger compatibility value,
  never as an envelope-owned projection.

The minimal `attention_cases` row and Catch identity remain Phase 1 work. Adding
them during migration triage would mix the still-open cross-producer identity
design with a correctness repair.

### Existing activity aggregation

The current feed intentionally aggregates several sources:

- unread conversations;
- pending votes;
- proactive in-app deliveries;
- pending invite answers.

That is a useful product aggregation, but its rows do not yet share a complete
lifecycle vocabulary. Pending work and unread information are mixed into one
`total_unread`, and mobile mapping reconstructs several concepts client-side.

The target feed should expose explicit source, destination, attention identity,
visibility state, work state, truth state, expiry, and allowed actions.

## Target contracts

### Type registry

Establish one exhaustive product registry. Each attention type declares:

- stable `type` and contract version;
- subject type and subject identifier;
- decision mode;
- attention class;
- lifecycle kind;
- audience/privacy rule;
- allowed projections;
- default destination;
- urgency and interruption policy;
- expiry and replacement strategy;
- dedupe/cancellation-key strategy;
- whether group-safe composition is required;
- outcome semantics.

Remove `candidate_type`, structured `intent`, and `trigger_name` as competing
identifiers. Keep free-text intent only when it genuinely records model
reasoning.

### Derived interruption policy

`attention_class` is the source of the maximum interruption policy. A producer
does not independently choose OS interruption level, provider priority, sound,
or whether quiet hours may be bypassed.

The registry resolves policy through one exhaustive function:

```text
ambient
  → inbox/card only; remote interruption forbidden

ledger
  → passive/default delivery; quiet hours binding; no sound by default

transactional
  → active delivery allowed; quiet hours binding; no cadence suppression

time_critical
  → time-sensitive delivery allowed; quiet-hours bypass only under the
    separately declared and user-enabled critical policy
```

Type-specific configuration may only **downgrade** this derived ceiling. It
cannot escalate it. Registry validation must reject, at startup and in tests:

- `ambient` with an interruptive remote projection;
- `ambient` or `ledger` with `time_sensitive`;
- any class other than `time_critical` bypassing quiet hours or the interruptive
  cap;
- `critical` OS interruption without a separately reviewed entitlement and
  product policy.

Dynamic urgency is resolved by registered type policy from authoritative case
context; arbitrary producer strings do not become provider policy. This single
derivation replaces independently maintained urgency weights, channel
priorities, and database vocabulary.

### Cross-surface identity

Related projections should carry:

- `attention_key`;
- `subject_type` and `subject_id`;
- `projection_id`;
- `dedupe_key`;
- `supersedes_key`;
- `expires_at`;
- destination contract;
- trace/correlation ID.

For observability naming only, OpenTelemetry’s broker-oriented messaging
conventions are a useful analogy: they distinguish individual message identity
from conversation/correlation identity and propagate creation context across
producer and consumer boundaries. They are not authority for the product's
mobile-push data model:
[OpenTelemetry messaging spans](https://opentelemetry.io/docs/specs/semconv/messaging/messaging-spans/).

### Concrete Catch identity and projection ownership

The Catch is the Phase 1 proving case. Current code creates or reuses a canonical
reschedule `change_proposals` row before it creates the proactive candidate.
The cross-surface identity is therefore:

```text
attention_type = feasibility_catch
subject_type   = change_proposal
subject_id     = <change_proposals.id>
attention_key  = feasibility_catch:change_proposal:<change_proposals.id>
```

Assignment and discovery rules:

1. The existing canonical proposal gateway creates or reuses the
   `change_proposals` row.
2. In the same transaction, or through its transactional outbox before any
   projection is emitted, it upserts one `attention_cases` row per recipient.
   A unique constraint on
   `(attention_type, subject_type, subject_id, recipient_id)` arbitrates races.
3. The feasibility producer places `subject_type`, `subject_id`,
   `attention_case_id`, and `attention_key` on its candidate. It must not use
   the trip/day dedupe key as cross-surface identity.
4. The independent Home proposal scanner reads the proposal ID and resolves the
   same attention case by the unique subject tuple. It never computes a second
   identity.
5. The type registry declares one owner per projection role. For the Catch,
   `home.primary` is owned by the proposal read-model renderer because it has
   the structured one-tap fix. The arbiter announcement may project to activity
   or remote delivery, but cannot mint another `home.primary` card.
6. Durable projection tables carry `attention_case_id` and enforce at most one
   active primary projection for
   `(recipient_id, attention_case_id, surface, projection_role)`. Read-time
   aggregators also group by that tuple before ranking, so compatibility rows
   cannot render beside the canonical projection.
7. Proposal resolution, withdrawal, or supersession changes the attention
   case's work/truth state and cancels or transforms every linked projection.

This fixes the current split in which the proposal scanner identifies the
structured card as `proposal:{proposal.id}`, while the announcement path dedupes
by `feasibility_catch:<trip>` and its Home dispatcher derives a trip/day key.

### Table-count accounting

This proposal does **not** initially reduce the number of tables. It reduces
competing identities, writers, and policy implementations.

Phase 1 consolidation math:

- add `attention_cases`: **+1 table**;
- add foreign keys and unique indexes to existing projection tables: **no new
  table**;
- narrow or rename `notification_records`: **table retained**;
- retain `notification_deliveries`, `notification_outcomes`, `vesper_cards`,
  and domain tables: **tables retained**;
- no table deletion is claimed in the initial roadmap.

Later evidence may justify retiring compatibility counters, duplicate dismissal
storage, or legacy notification state, but those deletions are not prerequisites
and must not be counted as benefits before an explicit migration plan proves
them. The near-term value is preventing duplicate Catch projections and
eliminating divergent policy code, not reducing table count.

### Remote delivery spine

One remote/inbox entry point should own:

```text
delivery envelope
→ recipient and audience validation
→ preferences
→ quiet hours
→ interruptive cap
→ channel resolution
→ TTL and expiration
→ collapse/replacement keys
→ idempotent dispatch
→ provider ticket
→ provider receipt
→ terminal attempt state
```

Policy results should be explicit and observable:

- `send`;
- `defer`;
- `downgrade_to_in_app`;
- `suppress`;
- `replace_existing`;
- `cancel_pending`.

Expo already exposes `ttl`, `expiration`, `collapseId`, Android `tag`, Android
`channelId`, priority, and iOS interruption level. These values should be derived
centrally from type policy rather than chosen by individual producers:
[Expo push message contract](https://docs.expo.dev/push-notifications/sending-notifications/).

### Cancellation and supersession

When the intended action occurs:

- cancel delayed or queued reminders;
- complete the open loop;
- remove or transform its actionable card;
- clear actionable feed state;
- retain historical product truth where appropriate.

Notification workflow systems use explicit cancellation keys to stop delayed
work after the user acts, while persistent feed messages require a separate
archive/transform operation:
[Knock workflow cancellation](https://docs.knock.app/send-notifications/canceling-workflows).

## Surface-specific rules

### Activity center

Present two user concepts:

- **Needs you**: votes, approvals, booking decisions, unresolved catches.
- **Updates**: confirmations, replies, completed actions, informational changes.

One badge source should count the product’s declared unread concept. Reading an
update must not complete an open loop.

### Home and trip cards

Cards share attention identity and truth state with activity and remote
projections but keep card-specific ranking, rendering, impression, dismissal,
and expiry behavior.

- Actionable cards represent open loops.
- Ambient cards represent pull-based opportunities.
- Request-time cards need not become durable attention rows unless cross-surface
  lifecycle or measurement requires it.
- Durable `vesper_cards` remain a projection, not a delivery-provider record.

### Foreground behavior

When the app is already showing the affected surface, update it subtly rather
than displaying a duplicate banner. Apple recommends avoiding repeat
notifications, presenting foreground updates without unnecessary interruption,
and excluding sensitive information from lock-screen copy:
[Apple notification guidance](https://developer.apple.com/design/human-interface-guidelines/notifications).

### Live travel surfaces

Live Activities/Live Updates are appropriate for:

- an active leave-for-airport window;
- check-in or boarding progression;
- a gate change during an active airport session;
- an active transfer ETA.

They are inappropriate for:

- nearby ambient discovery;
- generic inspiration;
- chat;
- distant upcoming events;
- general shortcuts into the app.

Apple describes Live Activities as bounded, glanceable ongoing tasks and advises
against duplicate pushes for the same update:
[Apple Live Activities](https://developer.apple.com/design/human-interface-guidelines/live-activities).
Android requires an ongoing, normally user-initiated, time-sensitive activity
and explicitly excludes ambient information:
[Android Live Updates](https://developer.android.com/develop/ui/views/notifications/live-update).

Expo now provides an official iOS widgets and Live Activities path, but it
requires native target configuration and development builds:
[Expo widgets](https://docs.expo.dev/versions/latest/sdk/widgets/).

## Forward roadmap

### Phase 0 — Finish and harden correctness

**Estimate:** 2–4 engineering days.

- [x] Complete push receipt reconciliation and dead-token disabling. Expo states
  that a successful ticket is provisional, receipts should be checked later,
  and `DeviceNotRegistered` tokens must stop receiving sends:
  [Expo push receipts](https://docs.expo.dev/push-notifications/sending-notifications/).
- [x] Finish the known destination-parity gaps across inbox and push, including
  booking references and existing card identifiers.
- [x] Finish quiet-hours timezone consistency.
- [x] Retain the atomic interruptive cap.
- [x] Correct known badge/read-state behavior, including dismissed and
  no-response terminal states.
- [x] Correct known type-to-rendering and type-to-routing bugs. Full
  registry-backed exhaustiveness remains Phase 1.
- [x] Adjudicate the already-applied local `notifrecord01` boundary without
  rewriting migration history.
- [x] Revise dependent fan-out, persistence, feed, OpenAPI, and mobile mapping
  call sites.
- [x] Add old/new compatibility reads and real-Postgres ownership/lifecycle
  assertions.
- [ ] Prove send → receive → route → read/badge reconciliation on one real iOS
  and one real Android device. The current local environment has enabled iOS
  Expo registrations but no Android registration; Phase 0 must not be called
  device-certified until both traces are captured.

**Exit gate:** correctness tests pass, real Postgres behavior is verified, and at
least one real iOS and one real Android device prove send → receive → route →
read/badge reconciliation.

Implementation evidence on 2026-07-25:

- Alembic upgraded a local Postgres database from already-applied
  `notifrecord01` through `notifenv04`; `alembic check` reports no schema drift.
- 697 notification, producer, lifecycle, receipt, diary, and J09 backend tests
  pass.
- 203 focused feed, fan-out, and Postgres CRUD tests pass.
- OpenAPI projection and generated TypeScript contract checks pass.
- focused mobile notification-feed, destination, and push tests pass (43 tests).
- full-device certification remains open; this is a backend/contract-verified
  Phase 0 implementation, not a shipped or journey-certified claim.

### Phase 1 — Lock vocabulary and identity

**Estimate:** 3–5 days.

- [x] Add the exhaustive type registry.
- [x] Normalize decision mode, attention class, lifecycle kind, audience, urgency,
  expiry, dedupe, destination, and projection eligibility.
- [x] Add the minimal `attention_cases` table and `attention_key`.
- [x] Implement the Catch subject tuple, recipient uniqueness, and canonical
  `home.primary` projection owner described above.
- [x] Implement exhaustive interruption-policy derivation and reject invalid
  class/policy combinations in startup validation and tests.
- [x] Deprecate `candidate_type` as a persistence compatibility name;
  `notification_type` is the canonical product identifier and free-text
  `intent` no longer selects policy.
- [x] Keep ambient request-time opportunities ephemeral only when they cannot
  participate in cross-producer lifecycle or duplicate a durable projection.

**Exit gate:** every current producer and feed source maps to one registered
type; unregistered types fail tests; two independently invoked Catch producers
converge on the same recipient attention case; only one `home.primary`
projection renders; invalid class/interruption combinations fail closed.

Implementation evidence on 2026-07-25:

- `TYPE_REGISTRY` covers all 30 current structured types and owns axes,
  projection eligibility, Home rendering, expiry, dedupe, destination, and
  cancellation policy. Unregistered structured types fail closed; unknown
  free-text intent enters only through the explicit generic type.
- Alembic `notiftype01` adds recipient-relative `attention_cases`, envelope and
  durable-card links, and a partial unique constraint allowing only one active
  `home.primary` projection per case. `alembic check` reports no schema drift.
- The Catch and venue-disruption producers use
  `<type>:change_proposal:<proposal_id>` identity. The proposal read model
  upserts the same recipient case and owns `home.primary`; notification
  dispatch returns `home_primary_owned_elsewhere` instead of creating a twin.
- Home ranking collapses any duplicate projections by attention case and
  deterministically prefers `home.primary`. Proposal resolution completes the
  case and expires linked durable projections in the same database transaction.
- Inbox and Expo push payloads expose the same notification type, case, key,
  and subject identity. The generated mobile API contract and
  `AppNotification` mapper preserve those fields.
- Real-Postgres convergence and lifecycle canaries, registry validation, and
  projection-dedupe tests pass as part of a 731-test notification/feed/J09
  backend run; 18 Catch, venue-disruption, and proposal-producer tests also
  pass, including the end-to-end producer → proposal-read-model identity
  assertion. Ruff, Alembic drift checks, OpenAPI generation, contract
  projection, TypeScript checking, and 68 focused mobile notification/J09 tests
  pass. Device certification remains outside this phase and is not implied.

### Phase 2 — Build and migrate the remote delivery spine

**Estimate:** 1–2 weeks.

**Implementation status (2026-07-25): backend-complete; device proof pending.**

- [x] Introduce the single remote/inbox delivery entry point.
- [x] Centralize preferences, quiet hours, caps, channel resolution, TTL,
  replacement, provider dispatch, tickets, receipts, and terminal outcomes.
- [x] Add explicit send/defer/downgrade/suppress/cancel decisions.
- [x] Migrate producers through an adapter with policy shadow comparison.

Recommended migration order:

1. a low-risk deterministic update;
2. booking confirmation;
3. proposal/vote open loops;
4. leave-by/time-critical alerts;
5. proactive concierge producers.

Implemented in that order. `delivery_spine.Notification` is now the only
producer-facing inbox/remote contract. `channel_dispatch.fan_out_to_channels`
remains the internal per-recipient execution engine and has one production
caller: the spine. The former producer gate, outcome-minting, manual leave-by
cap, direct Expo path, and sync fan-out escape hatch were removed.

Every delivery records requested versus registry-resolved channels in its
metadata and emits a shadow-mismatch log when policy narrows the requested set.
This is a deterministic policy comparison, not a second provider send.
Registered time-critical policy now owns leave-by quiet-hours/cap bypasses.
Provider TTL/expiration, replacement/collapse key, and interruption level are
derived centrally. Existing Expo ticket persistence and receipt reaping remain
the terminal provider evidence path.

Verification: Ruff passes; 707 backend notification, concierge-session/proactive,
booking-hold, and planning-autopilot tests pass, including explicit decision,
type-policy bypass, dedupe-window, producer migration, provider payload, and
proactive identity coverage. This phase has not been proven on a physical
device and therefore is not device-certified.

Use an incremental strangler migration rather than a big-bang replacement:
[AWS strangler-fig guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/strangler-fig.html).

### Phase 3 — Unify cross-surface lifecycle

**Estimate:** 4–7 days.

- **Implementation status (2026-07-25): backend and client contract complete;
  physical-device proof pending.**

- [x] Propagate attention identity into feed, durable cards, push payloads, and
  destinations.
- [x] Implement cancellation and supersession.
- [x] Separate visibility, work, truth, projection, and delivery state.
- [x] Ensure one action updates all affected projections without destroying domain
  history.

Canonical change-proposal acceptance, rejection, withdrawal, replan withdrawal,
revert, overlap replacement, and rebase replacement now call one lifecycle
transition in the same database transaction as the domain mutation. Booking
confirmation and rejection use the same boundary. The transition completes the
recipient's work, records stale/superseded/canceled truth, transforms or cancels
the envelope projection, cancels only pending provider attempts, and expires
linked durable Home cards. Already-sent delivery rows and resolved inbox
envelopes remain as audit/history instead of being deleted.

`notiflife01` adds explicit envelope projection state, expiry, cancellation
metadata, replacement-subject linkage, and the `canceled` delivery outcome.
Delayed producers consult canonical proposal/booking truth when creating a case
and fail closed when the subject is already terminal; fan-out rechecks the case
after creating each delivery audit row and before invoking a surface/provider.
An already-accepted remote push cannot be recalled, so client rendering must
still use the latest case/truth state after a tap.

The inbox contract now returns attention identity plus visibility, work, truth,
projection, and delivery state. `is_read` is derived only from visibility.
`requires_action` is derived from open/current/active work and remains true
after a user reads an item; completed, superseded, and canceled history remains
visible but non-actionable. The mobile mapper preserves these axes and renders
terminal history as resolved.

**Exit gate:** canonical proposal and booking actions atomically converge linked
cases/cards/envelopes/pending deliveries; delayed sends cannot reopen terminal
work; feed and mobile tests prove read ≠ complete and history survives
supersession. Physical-device send → tap → refresh behavior remains part of the
open Phase 0 device-certification gate and is not implied here.

Implementation evidence on 2026-07-25:

- Alembic upgraded local Postgres to `notiflife01`; `alembic heads` reports one
  head and `alembic check` reports no schema drift.
- 774 notification, feed, proposal-gateway, and booking lifecycle backend tests
  pass. One unrelated proposal-vote race test is deliberately excluded because
  its fixture asks the human proposal author to vote on their own proposal,
  which the canonical eligibility invariant correctly rejects.
- 45 focused mobile feed, ownership, destination, and routing tests pass, and
  TypeScript checking passes.
- The complete OpenAPI snapshot, active-mobile projection, and generated
  TypeScript schema were regenerated after the feed-contract change.

### Phase 4 — Polish the Activity surface

**Estimate:** about one backend/mobile week.

- **Implementation status (2026-07-25): backend/client implemented; physical
  device and accessibility walk pending.**

- [x] Split “Needs you” from “Updates.”
- [x] Make mark-read visibility-only.
- [x] Make completion, snooze, dismissal, expiry, and supersession explicit.
- [x] Move route reconstruction into a shared API contract.
- [x] Establish one authoritative badge source.
- [x] Add reason/source labels where they improve trust.
- [x] Update foreground surfaces without duplicate interruption.

`notifact01` adds delivery-owned read/dismiss timestamps, attention snooze
expiry, and explicit dismissed/expired envelope projections. Recipient-owned
Activity endpoints support read, batch-read, snooze, resume, and dismiss.
They lock in the same case → delivery → envelope order as canonical lifecycle
resolution, change no proposal/booking/itinerary truth, and cannot generically
mark domain work complete. Completion still arrives only from the canonical
domain mutation.

The feed now provides `activity_section`, `activity_status`,
`supported_actions`, source/reason labels, snooze/expiry state, and one semantic
destination object. “Needs you” means open + current + active; reading does not
remove open work, while snoozed work moves to Updates until its deadline.
Completed, dismissed, expired, superseded, and canceled rows remain visible
with explicit status copy.

Inbox and push now receive the same `destination_kind` plus typed identifiers.
The mobile client prefers that contract and retains legacy reconstruction only
for old payloads. Private conversation destinations remain private by contract
and test.

`NotificationFeed.badge_count` is the source for the bell, cached optimistic
updates, and OS icon synchronization. Opening Activity or tapping one push no
longer blindly clears the icon badge. Foreground receipt invalidates Activity
quietly; the operating-system banner remains the only interruption.

**Exit gate:** backend and mobile tests prove sectioning, lifecycle actions,
route parity/privacy, badge ownership, optimistic rollback, and foreground
refresh. A VoiceOver/TalkBack pass plus physical iOS/Android send → receive →
route → lifecycle → badge reconciliation remains required before calling the
surface device-validated.

Implementation evidence on 2026-07-25:

- Alembic reports the single `notifact01` head and no schema drift against the
  upgraded local Postgres database.
- 784 backend notification/feed/lifecycle tests pass with one unrelated
  proposal-vote fixture deliberately deselected. The final focused Phase 4
  lifecycle, Activity API, feed, and destination-contract gate passes 37 tests.
- 104 mobile Activity, badge, foreground, destination, and routing tests pass
  across 12 suites. TypeScript checking passes; targeted lint has no errors.
- The complete OpenAPI snapshot, active-mobile projection, and generated
  TypeScript schema include the Activity action and feed-contract changes.
- No physical-device or accessibility validation is claimed.

### Phase 5 — Scope proactive arbitration

**Estimate:** 4–7 days for the initial safe version.

- **Implementation status (2026-07-25): backend shadow canary complete;
  enforcement, calibrated experiment launch, and device/dogfood proof pending.**

- [x] Restrict arbitration to inferred cases.
- [x] Apply deterministic privacy, eligibility, and truth gates first.
- [x] Support send, defer, downgrade, and suppress.
- [x] Run shadow mode before suppression controls production delivery.
- [x] Add stable send/no-send holdout cohort machinery, dark by default.
- [x] Measure passive awareness, action completion, dismissal, notification opt-out,
  and app abandonment separately.

Do not train or tune against click-through alone, and never place transactional
truth behind the model.

`arbitration_policy.py` is now the sole owner of the inferred interrupt
decision. It stores requested versus effective action, reason, version,
need/receptivity inputs, causal experiment arm, and propensity separately.
Shadow mode is the default and always sends after hard gates; changing
production behavior requires both `mode=enforce` and an independent enforcement
switch. Holdouts require the same two keys and use a stable recipient/type
(private) or trip/type (group) assignment rather than a fresh correlation id.
A minimum-delivery floor remains available during enforcement.

Hard gates fail closed on audience/privacy policy, trip membership,
conversation/source provenance, and stale proposal truth. Those gates do not
replace composition privacy: every group candidate still enters the canonical
strict group-safe proactive-turn path. Inferred generic urgency is clamped below
time-critical, so only registered deterministic truth can claim quiet-hours or
cap exemptions.

`notifarb01` extends durable decision evidence and source-labels suppression
windows so user “Not now,” policy deferral, experiment protection, and dispatch
dedupe cannot be confused in analysis. The operations readout keeps exposure,
passive awareness, action completion, dismissal, explicit opt-out, app return,
and no-return proxy separate; no-return is explicitly not treated as definitive
abandonment.

**Exit gate for production enforcement:** collect representative shadow data;
choose and review thresholds from that distribution; pre-register the holdout
unit, fraction, window, and success/harm measures; confirm privacy traces and
real iOS/Android delivery behavior; then canary the independent enforcement
switch with an immediate rollback path. Backend completion does not satisfy
this gate.

### Phase 6 — Platform polish

**Estimate:** 3–6 days, excluding live surfaces.

- **Implementation status (2026-07-25): backend/client/native configuration
  implemented; physical iOS/Android proof pending.**

- [x] Create stable Android channels “Trip updates,” “Needs your action,”
  and “Time-critical travel.” Android users control channel importance after a
  channel is created, so identifiers must be durable:
  [Android notification channels](https://developer.android.com/develop/ui/compose/notifications/channels).
- [x] Map policy to iOS passive, active, and time-sensitive interruption levels.
- [x] Add and verify TTL, APNs/FCM collapse, and Android replacement tags.
- [x] Preserve contextual permission requests after a visible value moment. Both
  platforms recommend asking in context rather than automatically at launch:
  [Apple permission guidance](https://developer.apple.com/documentation/UserNotifications/asking-permission-to-use-notifications) and
  [Android permission guidance](https://developer.android.com/develop/ui/compose/notifications/notification-permission).
- [x] Audit lock-screen privacy, notification actions, accessibility text, deep
  links, and foreground behavior.

The Android channel IDs are intentionally versioned:
`trip_updates_v1` is low/quiet, `needs_action_v1` is default importance, and
`time_critical_travel_v1` is high importance with sound/vibration. Because
Android freezes behavioral channel settings after first creation, any future
importance/sound change must mint a v2 ID rather than rewrite user-controlled
behavior. Updated Android clients advertise `vesper_channels_v1` during device
registration. The server omits `channelId` for older clients—Expo then uses its
Default channel—because targeting a channel the installed app has not created
can silently discard the notification.

The backend derives actual interruption from normalized urgency capped by the
registered type policy, then derives the Android channel from that same value.
It no longer trusts loose provider metadata to escalate a notification.
Passive traffic uses normal provider priority; active/time-sensitive traffic
uses high provider priority; only time-sensitive traffic requests iOS sound.
The Expo payload retains TTL/expiration and uses one normalized replacement key
for FCM/APNs collapse plus Android displayed-notification replacement.

Private noncritical push bodies now show generic lock-screen copy while the full
content remains behind authentication in Activity or its destination.
Group-visible text still comes from the canonical group-safe composition path.
Leave-by is the sole registered time-critical type and keeps its bounded
operational departure instruction. No custom OS mutation actions ship in this
phase: default tap routes through the shared destination contract, while
snooze/dismiss/complete stay inside authenticated Activity where current domain
truth can be checked.

Opening Activity no longer requests notification permission. Passive launch and
foreground paths only re-register an already-granted token; the primed OS ask is
owned by save/keep and first-message value moments. The iOS native configuration
declares Time Sensitive Notifications capability. The entitlement and Android
channel contract both require rebuilt native binaries; an OTA JavaScript update
alone is not a valid Phase 6 rollout.

**Exit gate:** physical iOS and Android traces must demonstrate all three
presentation classes, user channel controls, Focus/summary and Doze behavior,
lock-screen redaction, cold/background/foreground routing, expiry/replacement,
badge reconciliation, and VoiceOver/TalkBack labels. Static, backend, and mock
proof do not satisfy this gate.

### Phase 7 — Live travel experiment

Start only after the shared lifecycle and delivery spine are proven.

- Choose one bounded journey, preferably airport departure/boarding.
- Start, update, and end the live session from authoritative trip/provider state.
- Avoid duplicate push for routine live-session updates.
- Redact sensitive lock-screen content.
- Require explicit user control and immediate end when the activity ends.

### Phase 8 — Learned optimization

Start only when the system produces trustworthy exposure and outcome data.

- Establish causal holdouts.
- Model separate objectives and negative outcomes.
- Learn ranking/timing for inferred cases only.
- Keep hard privacy, truth, and transactional rules outside the learned model.

## Recommended sequence

1. Finish correctness and revise the unlanded schema.
2. Establish the registry and stable attention identity.
3. Migrate remote delivery producer by producer.
4. Unify activity/card lifecycle.
5. Introduce proactive arbitration.
6. Polish platform behavior and permissions.
7. Experiment with an active-trip live surface.
8. Add learned optimization after sufficient trustworthy data exists.

The first six steps are approximately four to six focused engineering weeks for
one backend/mobile lane, excluding major product redesign and the optional live
surface.

## Proof and safety gates

Every phase that changes a user-visible journey must prove four separate things:

1. **Static contract:** types, policy registry, routing, and lifecycle tests.
2. **Backend reality:** real Postgres migration/integration and concurrency
   behavior.
3. **Privacy trace:** private inputs cannot enter group-visible text; group
   composition uses the canonical safe path.
4. **Device reality:** a real iOS and Android device demonstrate receive,
   presentation, route, action, badge, and reconciliation behavior.

For booking, proposal, itinerary, expense, and membership changes:

- domain truth has one canonical writer;
- mutation receipts remain visible on the owning surface;
- stale or mocked provider truth is visibly labeled and cannot silently replace
  canonical state;
- background notification failure never rolls back the successful domain
  mutation;
- delivery success is not claimed solely from provider acceptance or green
  backend tests.

## Remaining decisions

For later delivery and badge phases:

1. Exact product definition of the app badge count.
2. Whether email is interruptive for policy purposes or a separate asynchronous
   delivery class.
3. Which deterministic producer becomes the first shadow-migration slice.
4. Whether the first live-travel experiment belongs inside the MVP horizon.

## Exit

Before 2026-08-24:

- adjudicate the five remaining decisions;
- promote durable vocabulary, ownership, and invariants into
  `docs/systems/proactive-notifications.md`;
- record the schema and projection boundary as a decision under
  `docs/decisions/`;
- convert accepted phases into implementation work;
- archive this note as the point-in-time research record.
