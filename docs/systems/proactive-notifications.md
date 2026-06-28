# Proactive / Notifications — System Charter

> Surface: Vesper
> Maturity (for MVP): Should-have
> Status: wired
> Last updated: 2026-06-27

## Purpose
Decides *when, whether, and how* to proactively message a traveler — and routes
each notification to the smallest useful, privacy-correct surface. Serves belief
#7 (Surfacing Strategy): proactive presence is **trust-calibration**, not
manufactured engagement — a nudge earns its interruption or it isn't sent.

## Spans (cross-repo)
- Backend: [`travel-agent/backend/notifications/`](../../travel-agent/backend/notifications/FEATURE.md) (`gates.py` → `triage.py` → `arbiter.py` → `state_updater.py` / `channel_dispatch.py`) + [`backend/tasks/`](../../travel-agent/backend/tasks/FEATURE.md) (daily lifecycle/character-read/story loops) + `concierge/triggers.py::run_proactive_turn` (Tier 3). Loops registered in `api/lifecycle.py`.
- Frontend: `app/notifications`, push routing (`utils/push`, `notificationOwnership`), bell/badge.
- Tables of record: `proactive_events` (append-only ledger), `notification_state`, `notification_outcomes`, `notification_deliveries`.

## Public interface (what other systems may call / read)
- **Entry points:** `arbiter.py::candidates_from_triage()` → `arbitrate()` is **the SINGLE EXIT** — need-floor → `rank()` → `pick()` → accept-gate → holdout → `dispatch_candidate()` (which calls `run_proactive_turn` *inside* the arbiter). Score = `urgency × source_prior × value_hint`.
- **Deterministic-event push:** `push.py::ExpoPushDispatcher` for product events ("your story is ready") — bypasses the 3-tier loop but still passes `_check_user_push_gates`.
- **Consumes:** trip/itinerary/proposal/expense state, `experience_opportunities` (supply side, injected into triage), traveler timezone + cadence prefs.
- **Never:** dispatch outside the arbiter exit (no Tier-3 turn from triage directly); write a notification without a `proactive_events` correlation chain.

## Owns (source of truth)
The proactive-decision ledger and notification lifecycle: `proactive_events`,
`notification_state`, `notification_outcomes`, `notification_deliveries`. It owns
*the decision to interrupt* — not the content systems it speaks about.

## Invariants (must always be true)
- **Private outcomes never route to group surfaces** (journey 09 / 10): private financial or concierge facts go to private chat; only group-visible outcomes reach group chat.
- **Quiet hours / cadence are binding** for non-critical nudges — Tier-1 gates run with **zero LLM** and use the user's timezone, not server TZ.
- **Single exit:** every composed/sent proactive turn passes through `arbitrate()`; dispatch lives inside the arbiter.
- **Best-effort, non-blocking:** ledger write failures and per-channel failures never block a turn or another channel; `status='skipped'` (user opted out) ≠ `status='failed'` (system error).
- **No stranded taps / no badge drift:** a push with a missing trip id falls back rather than dead-ends; badge counts agree with the feed the bell opens; read-state persists across refresh.

## Failure modes
- Triage (Haiku) or composition (Sonnet) down → no turn sent (silent, gated), no fabricated message.
- A channel (push/sms/email) fails → that delivery row is marked, siblings still fire; `pause_all` short-circuits everything.
- Fast-path story subscriber lost on restart → daily `trip_story_backfill` recomposes (LEFT-JOIN idempotent, batch cap 50).
- Stale `pending` outcomes → `cleanup.py` resolves to `no_response`/`expired` after 2h.

## Maturity & validation
- Serves journey: 09 (notifications & proactive routing).
- DoD state: routing/ownership/push unit tests ✅ (`__tests__/screens/notifications.routing.test.tsx`, `notificationOwnership.test.ts`, `push.test.ts`) · **live-walk / Maestro ❌** (high-drift domain).
- Dark/off: `learned_value_enabled=False` (Beta-Bernoulli value model), `holdout_fraction=0.0` (incrementality write-free), email/SMS log-only until credentials set.

## Canonical docs
- why → `product/Surfacing Strategy.md` · what(be) → `backend/notifications/FEATURE.md` · `backend/tasks/FEATURE.md` · trace → `docs/reliability/traces/notifications-and-proactive-help.md`.
- Tests: `__tests__/data/notifications.test.ts`, `notifications.routing.test.tsx`, `utils/notificationOwnership.test.ts`.

## Open risks / known gaps
- **Privacy routing is the headline risk** — a private outcome leaking to group chat is the journey-09 "must never happen". The route-priority matrix is the first thing to validate live, not just in mocks.
- Drift-prone surface: timing, read-state mutation, and push payloads diverge from mocks easily — no Maestro/live walk yet.
- Scoring is hand-tuned (value model + holdout both dark); incrementality is instrumented but not yet measured, so "is this nudge net-positive?" is unproven.
