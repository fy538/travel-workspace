# Proactive / Notifications — System Charter

> Surface: Vesper
> Maturity (for MVP): Should-have
> Status: wired
> Last updated: 2026-07-25

## Purpose
Decides whether Vesper should intervene, what useful outcome it can carry toward
resolution, when the traveler is receptive, and which privacy-correct surface is
smallest. A push notification is only one delivery mechanism. The product unit is
the complete intervention:

```text
notice a consequential gap
→ understand its impact on these travelers and this itinerary
→ find a workable response
→ ask only when judgment or permission is required
→ update the itinerary and relevant people
```

Serves belief #9.75: proactivity is **judgment and trust-calibration**, not
manufactured engagement. An intervention earns its interruption or Vesper uses a
quieter surface, defers, or stays silent.

## Spans (cross-repo)
- Backend: [`travel-agent/backend/notifications/`](../../travel-agent/backend/notifications/FEATURE.md) (`gates.py` → `triage.py` → `arbiter.py` → `state_updater.py` / `channel_dispatch.py`) + [`backend/tasks/`](../../travel-agent/backend/tasks/FEATURE.md) (daily lifecycle/character-read/story loops) + `concierge/triggers.py::run_proactive_turn` (Tier 3). Loops registered in `api/lifecycle.py`.
- Frontend: `app/notifications`, push routing (`utils/push`, `notificationOwnership`), bell/badge.
- Tables of record: `proactive_events` (append-only arbitration ledger),
  `attention_cases` (recipient-relative cross-surface identity),
  `notification_envelopes` (delivery snapshot), `notification_state`,
  optional `notification_outcomes`, and `notification_deliveries`.

## Public interface (what other systems may call / read)
- **Inferred-attention entry:** `arbiter.py::candidates_from_triage()` →
  `arbitrate()` is the single learned-arbitration exit. Hard privacy,
  eligibility, provenance, and current-truth gates run first. Deterministic
  candidates dispatch without ranking; inferred candidates alone run rank →
  versioned `send | defer | downgrade | suppress` policy → optional holdout →
  compose. Default policy mode is shadow.
- **Delivery entry:** inferred and deterministic notifications both construct
  `delivery_spine.py::Notification` and call `deliver()` (or the synchronous
  adapter for the legacy state updater). Only the spine may call
  `channel_dispatch.py::fan_out_to_channels`; producers never call a gate,
  delivery table, or provider directly.
- **Vocabulary and identity:** `notifications/type_registry.py` is the
  exhaustive structured vocabulary. `notification_type` chooses policy;
  free-text `intent` is telemetry only. Projections that share a subject use
  `attention_cases` keyed by
  `(notification_type, subject_type, subject_id, recipient_id)`.
- **Activity contract:** feed rows expose explicit Needs-you/Updates placement,
  lifecycle status, supported projection actions, trust labels, and a semantic
  destination. Activity read/snooze/resume/dismiss endpoints never complete or
  mutate the underlying proposal, booking, or itinerary.
- **Consumes:** trip/itinerary/proposal/expense state, `experience_opportunities` (supply side, injected into triage), traveler timezone + cadence prefs.
- **Never:** let a free-text intent choose delivery or rendering policy; create
  a second active `home.primary` projection for one attention case; require an
  optional learning outcome for deterministic product delivery.
- **Authority boundary:** notification, home card, chat, voice, and email may
  propose or announce a trip action, but material plan outcomes land through the
  canonical itinerary operation; delivery state never becomes trip truth.

## Owns (source of truth)
The proactive-decision ledger, recipient-relative attention lifecycle, and
delivery evidence: `proactive_events`, `attention_cases`,
`notification_envelopes`, optional `notification_outcomes`, and
`notification_deliveries`. It owns *the inferred decision to interrupt* and the
cross-surface identity of that work — never the booking, proposal, itinerary,
expense, or membership truth it speaks about.

## Invariants (must always be true)
- **Private outcomes never route to group surfaces** (journey 09 / 10): private financial or concierge facts go to private chat; only group-visible outcomes reach group chat.
- **Quiet hours / cadence are binding** for non-critical nudges — Tier-1 gates run with **zero LLM** and use the user's timezone, not server TZ.
- **Scoped arbitration:** every inferred proactive turn passes through
  `arbitrate()`; deterministic facts do not. Every remote/inbox send traverses
  the delivery spine and its registered type policy, preference, membership,
  quiet-hours, cap, expiry, replacement, dedupe, persistence, provider-ticket,
  receipt, and outcome handling.
- **No learned escalation into truth lanes:** generic model-authored
  `time_sensitive`/`high` urgency is capped at `action_needed`. Only a
  registered deterministic time-critical type may bypass quiet hours or
  interruptive caps.
- **Enforcement is a two-key change:** requested arbitration actions are
  durable evidence in shadow mode, but effective delivery remains send.
  Production gating requires mode `enforce` plus a separate rollback switch;
  randomized holdouts remain disabled until those same controls are active.
- **One platform derivation:** registered type policy plus normalized urgency
  derives iOS interruption level, Android channel, provider priority, sound,
  TTL, and replacement identity. Producers cannot select a more interruptive
  channel by passing loose metadata. Android channel IDs are capability-gated
  by the device's registered `vesper_channels_v1` contract; legacy installs
  omit the ID and fall back to Expo Default.
- **Private lock-screen minimization:** private noncritical copy is redacted in
  the remote alert while authenticated Activity/destination content remains
  complete. Deterministic leave-by is the sole registered time-critical type
  and may retain the bounded operational instruction.
- **Policy is data:** quiet-hours and interruptive-cap exemptions are legal only
  on registered time-critical types. `leave_by` declares both exemptions; no
  producer implements a bypass branch.
- **Explicit delivery result:** every spine call resolves to send, defer,
  downgrade, suppress, cancel, or failed. A non-interruptive projection that
  succeeds while push is held is a downgrade, not a full send.
- **One structured vocabulary:** every policy-bearing type is registered.
  Unknown structured types fail closed. Model-authored intent may only enter as
  the explicit generic `notification` type.
- **One case, one Home primary:** all projections of a durable subject carry the
  same recipient attention identity. The type registry declares the
  `home.primary` owner.
- **Domain truth closes attention atomically:** proposal and booking terminal
  transitions update linked cases, envelopes, pending delivery attempts, and
  durable cards in the same transaction. Already-sent delivery evidence and
  resolved inbox history are retained.
- **Read is not done:** visibility (`unseen`/`seen`/`read`), work
  (`informational`/`open`/`snoozed`/`completed`), truth
  (`current`/`stale`/`superseded`/`canceled`), projection, and delivery state
  are independent. Reading open/current work never completes it.
- **One badge source:** `NotificationFeed.badge_count` owns the bell, cached
  optimistic count, and OS icon synchronization. Opening Activity or tapping
  one push never zeros an independent counter.
- **One route meaning:** inbox and remote payloads carry the same semantic
  destination kind and identifiers. Legacy intent reconstruction is fallback
  compatibility only; private-chat destinations cannot fall through to a group
  route.
- **Best-effort, non-blocking:** ledger write failures and per-channel failures never block a turn or another channel; `status='skipped'` (user opted out) ≠ `status='failed'` (system error).
- **No stranded taps / no badge drift:** a push with a missing trip id falls back rather than dead-ends; badge counts agree with the feed the bell opens; read-state persists across refresh.
- **Outcome over information:** an advisory intervention identifies the impact,
  offers the best next action or prepared revision, and lands in relevant trip
  context. A generic fact such as weather without its trip consequence is not a
  successful proactive turn.
- **Smallest useful surface:** interruptive push is reserved for urgency or
  time-sensitive value; quieter home/itinerary treatment is preferred when the
  user can discover it safely.
- **Silence is first-class:** uncertainty, weak grounding, low receptivity, low
  incremental value, or lack of a useful continuation can all produce no send.
- **Coherent action:** when an intervention recommends an itinerary change, the
  proposal includes downstream timing/logistics/provider consequences rather
  than changing one isolated stop.

## Failure modes
- Triage (Haiku) or composition (Sonnet) down → no turn sent (silent, gated), no fabricated message.
- A channel (push/sms/email) fails → that delivery row is marked, siblings still fire; `pause_all` short-circuits everything.
- A delayed producer races a terminal proposal/booking mutation → canonical
  truth initializes or returns a completed case and delivery fails closed. A
  provider-accepted push cannot be recalled; tap/refresh must render current
  truth rather than trust the stale payload.
- A foreground push arrives while the relevant surface is mounted → invalidate
  server-backed Activity state without creating an additional app toast; the OS
  banner/list presentation remains the single interruption.
- Fast-path story subscriber lost on restart → daily `trip_story_backfill` recomposes (LEFT-JOIN idempotent, batch cap 50).
- Stale `pending` outcomes → `cleanup.py` resolves to `no_response`/`expired` after 2h.

## Maturity & validation
- Serves journey: 09 (notifications & proactive routing).
- DoD state: routing/ownership/push unit tests ✅ (`__tests__/screens/notifications.routing.test.tsx`, `notificationOwnership.test.ts`, `push.test.ts`) · **live-walk / Maestro ❌** (high-drift domain).
- Code defaults remain dark for learned-value and holdout behavior; deployed
  overrides are environment state and must be verified through the operational
  notification diary/readout rather than copied into this charter. Phase 5
  arbitration defaults to counterfactual shadow measurement; effective
  suppression and holdout exposure remain off. Email/SMS remain
  credential-dependent.

### Accepted policy boundaries

- The Activity/app badge counts feed entries that are unread or still require
  action. Reading an open-loop item changes visibility but does not remove its
  badge contribution.
- Email is asynchronous rather than interruptive: it keeps preference,
  membership/truth, dedupe, expiry, and outcome gates, but does not consume the
  push/SMS interruptive cap or use mobile quiet hours.
- A bounded live-travel experiment is deferred until physical iOS/Android and
  accessibility certification passes. Learned optimization remains deferred
  beyond that until causal exposure/outcome evidence is trustworthy.

## Canonical docs
- why → `product/Surfacing Strategy.md` · what(be) → `backend/notifications/FEATURE.md` · `backend/tasks/FEATURE.md` · trace → `docs/reliability/traces/notifications-and-proactive-help.md`.
- Tests: `__tests__/data/notifications.test.ts`, `notifications.routing.test.tsx`, `utils/notificationOwnership.test.ts`.

## Open risks / known gaps
- **Privacy routing is the headline risk** — a private outcome leaking to group chat is the journey-09 "must never happen". The route-priority matrix is the first thing to validate live, not just in mocks.
- Drift-prone surface: timing, read-state mutation, and push payloads diverge from mocks easily — no Maestro/live walk yet.
- Scoring still depends materially on authored priors. Learning and holdout
  infrastructure exists, but deployed overrides and statistical power must be
  verified through the operational readout; "is this intervention net-positive?"
  remains unproven.
- Product-quality proof is still missing: a real on-device intervention must show
  that Vesper noticed something consequential, proposed the right coherent
  response, reached the right person at the right time, and reduced work rather
  than merely sending information.
- Phase 2 backend proof: 707 notification, concierge-session/proactive,
  booking-hold, and planning-autopilot tests pass. Production searches show one execution call to
  `fan_out_to_channels`, owned by `delivery_spine`; deterministic producers,
  booking confirmation, proposal open/resolved events, leave-by, nudges, and
  proactive concierge dispatch all enter through `Notification`. Provider
  expiry, replacement/collapse, interruption policy, tickets, receipts, and
  explicit decision tests pass. This is backend proof only; no real-device
  delivery is certified.
- Phase 3 backend/client contract: `notiflife01` introduces explicit
  projection/cancellation/replacement fields and canceled pending deliveries.
  Canonical proposal and booking mutations converge attention cases, inbox
  envelopes, Home cards, and pending delivery attempts without deleting audit
  history. The feed and mobile mapper preserve separate lifecycle axes; read
  visibility does not clear open work. Physical-device tap/refresh proof remains
  open and no device certification is claimed.
- Phase 4 backend/client implementation: `notifact01` adds Activity visibility,
  snooze, dismissal, and expiry persistence. The feed owns Needs-you/Updates
  placement, lifecycle copy, supported actions, semantic destinations, and the
  authoritative badge count. Mobile optimistic actions roll back on failure and
  foreground receipt refreshes existing surfaces without an extra toast.
  Physical iOS/Android and accessibility validation remain open.
- Phase 5 backend canary: hard candidate gates precede the inferred-only
  versioned policy; requested/effective actions and causal experiment arms are
  stored separately. The operational readout reports exposure, passive
  awareness, action completion, dismissal, explicit opt-out, return, and
  no-return proxy as distinct measures. Defaults preserve existing delivery
  behavior. Production enforcement, causal calibration, and device/dogfood
  validation remain open.
- Phase 6 platform implementation: three versioned Android channels are
  registered before token enrollment; the iOS build declares Time Sensitive
  capability; payload interruption/channel/priority derives from registry
  policy; long replacement IDs are provider-safe; passive foreground updates
  refresh/list without a banner; and private noncritical lock-screen bodies are
  minimized. Activity no longer triggers permission on mount—save/keep and
  first-message value moments own the ask. Physical iOS/Android presentation,
  settings, Focus/Doze, lock-screen, and accessibility proof remains open.
