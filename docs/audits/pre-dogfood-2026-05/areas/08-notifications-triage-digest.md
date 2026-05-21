# Area 08 — Notifications, Triage, Digest

Date: 2026-05-20
Scope: Pre-dogfood read-only audit of the notification intelligence pipeline
(gates → triage → triggers → channel dispatch), the daily digest engine, the
bell/feed, push delivery + deregister, and the React Native consumers.
Mode: read-only; no product code, tests, or config changed.

## Summary

The notification fabric has good bones — Tier 1 gates honour cadence, quiet
hours, pause-all, and active-conversation suppression; the triage prompt
defaults to silence; per-channel dispatch is best-effort; the bell feed
sanitises pre-auth invite answers to a privacy-preserving "Answered privately"
constant; logout properly deregisters the push token; account deletion
cascades `user_devices`, `notification_state`, `notification_outcomes`, and
`notification_deliveries`.

Three things are still genuinely scary for a first-week tester, and they all
sit on the **target-routing seam** between triage's intent and where the
agent's composed reply actually lands:

1. The triage system tells the model "this is a **private** fyi for Sam
   because the taste matches" — but `run_proactive_turn` always writes to
   the **group conversation**, so the agent's body is visible to every
   member when they open the trip chat. The "private" label only gates the
   push fan-out, not the underlying `messages` row. This is the single
   biggest privacy hazard in the area.
2. The `events_tonight` proactive trigger injects up to 400 raw chars of
   the creator's Personal Memory directly into the agent prompt, with no
   group-safe synthesis, and the resulting compose lands in the group
   conversation via the same bug as #1.
3. Quiet hours are honoured at the *gate* (per-user evaluation) but **not
   at the per-recipient fan-out** for group dispatches. A user who turned
   on quiet hours still gets pushed at 2am whenever any *other* member of
   their trip passes the gates and triage decides to send a group
   notification.

Beyond those, the per-day cap is keyed `(user_id, trip_id)` rather than per
user, so a member of five active trips can take 20+ notifications/day before
any cap fires; and several deterministic product pushes (booking proposal
status, story_ready, shares_settled) reuse the same `run_proactive_turn`
plumbing that has the routing bug from #1, so booking detail / story title
also lands in the group thread regardless of `target_kind="private"`.

Everything else (digest cadence, bell badge math, mark-read flow, invite
intake summary, deregister on logout/delete) is in good shape.

---

## Findings

### [P0] — "Private" proactive notifications land verbatim in the group conversation

**References:**
- `Travel Agent/backend/concierge/triggers.py:48-95` (`run_proactive_turn` always opens the trip's *group* session)
- `Travel Agent/backend/concierge/session.py:1390-1417` (`get_or_create_session_for_trip` returns the group conversation)
- `Travel Agent/backend/concierge/session.py:707-755` (`_record_turn_side_effects` is the *only* code that consumes `triage_metadata.target_audience` / `target_user_id`; both are passed straight to `record_notification_dispatch`, never to session routing)
- `Travel Agent/backend/notifications/state_updater.py:118-176` (`record_notification_dispatch` honours target by per-user outcome creation, but the reply has already been persisted as a row in the group `messages` table)
- `Travel Agent/backend/notifications/prompts.py:49-53, 102-107` (triage prompt explicitly mints private taste-based nudges and stuffs the matching reason into `prompt_for_agent`)
- `Travel Agent/backend/api/lifecycle.py:901-914` (loop dispatches the chosen `notif.prompt_for_agent` with `target_audience` flowing only to the metadata, not to session selection)

**Why it matters to a real tester:**
The triage prompt is explicitly designed to recommend *private* fyi messages
"because taste is personal" (a one-off concert that matches Sam's genre
profile, a quiet venue for Lilia, etc.). The Haiku assembles a
`prompt_for_agent` that names the experience and the reason it fits *that
traveler*. The Sonnet turn is then run inside the trip's group conversation
session — so the reply ("Sam — there's a Floating Points set at Lux on the
20th, your kind of techno…") is persisted into the group `messages` row.
Other members see it the next time they open the trip chat or pull the bell
feed (it shows up in `unread_conversations` for everyone). Push only fires
to Sam, but the message itself is no longer private. This is precisely the
launch-blocking failure mode the product promises not to commit.

**Repro / deterministic test idea:**
1. Create a 2-member trip with members Alex (creator) and Sam.
2. Seed Sam's Personal Memory `Who They Are` with a constraint such as
   "Sam is in recovery and avoids alcohol-forward venues."
3. Hand-build a `TriageNotification(decision="send", target="private",
   target_user_id=str(sam.id), prompt_for_agent="Sam asked us to flag
   alcohol-free Friday nights — there's a sober rave Friday at 10pm.",
   intent="sober_friday", urgency="fyi")` and call `run_proactive_turn`
   directly with the matching triage_metadata.
4. Query Alex's bell feed (`GET /api/users/{alex_id}/notifications`) and
   the messages of the trip's group conversation. Assert neither contains
   the literal phrase "sober" / "alcohol" / "in recovery" or any
   paraphrase. Today both surfaces leak the body.
5. Confirm the bug also reproduces when triage runs end-to-end against a
   real fixture trip with a member taste snippet referencing dietary
   constraints.

**Suggested fix direction:**
Make `target_audience` actually route at the session layer. When
`triage_metadata["target_audience"] == "private"` and `target_user_id` is
set, resolve a per-user *personal* conversation for that user
(`get_or_create_session_for_personal_trip` already exists at
`session.py:1420`) and persist the agent reply there instead of the group
session. Update `triggers.py::run_proactive_turn` to branch on
`target_audience`. Add a regression test that asserts a private notification
never produces a row in the trip's group conversation. As a defence-in-depth
companion, run the agent's composed reply through a group-safe synthesis
gate when the session *is* the group conversation but the originating
intent was private — refusing to ship if the body still names another
member's constraint.

**Confidence:** High.

---

### [P0] — `events_tonight` trigger pastes raw Personal Memory into the agent prompt and into the group chat

**References:**
- `Travel Agent/backend/concierge/proactive.py:338-359` (raw PM slice `markdown_content[:400]` injected as "Traveler context")
- `Travel Agent/backend/concierge/proactive.py:355-359` (resulting prompt fed straight to `run_proactive_turn` with `trigger_name="events_tonight"`)
- `Travel Agent/backend/concierge/triggers.py:64-95` (run_proactive_turn opens the group session)
- `Travel Agent/backend/api/routes/_notifications_feed.py:298-301` (the agent reply body, up to 300 chars, is stored verbatim in `notification_deliveries.metadata_['body']` and surfaced in the bell)

**Why it matters to a real tester:**
The PM document is the densest concentration of private constraints we have
(dietary, accessibility, sober/recovery flags, anxieties, sometimes income
information). Slicing 400 chars of `markdown_content` is essentially "take
whatever happens to be near the top of the file." The agent is then told
"mention the most relevant one in a brief, natural message" — and the reply
lands in the group conversation because of the P0 above. Tonight's events
fire daily during a trip, so this is a high-frequency leak channel.

**Repro / deterministic test idea:**
1. Seed a creator's `personal_memories.markdown_content` with a known
   private sentence in the first 400 chars (e.g. "Fei takes anxiolytics
   and prefers quiet venues after 9pm.").
2. Seed at least one matching active `experiences` row for the trip's
   `place_id` with `availability='one_off'` and `starts_at` later today.
3. Invoke `_check_events_tonight(trip_id, loop)` directly.
4. Read the trip's group conversation messages — assert no agent reply
   contains the substring "anxiolytics" / "anxiety" / "quiet venues" or a
   close paraphrase. Today the trigger has no group-safe filter on the
   reply.

**Suggested fix direction:**
Either (a) stop injecting raw PM into this trigger — replace with a
group-safe taste snippet derived through the existing
`backend.synthesis.group_synthesizer` pathway or the
`extract_taste_snippet("Who They Are")` helper that
`lifecycle._evaluate_trip_notifications` already uses, with a guarantee
that constraint sentences never appear; or (b) route the dispatch as a
real private notification (per the P0 above) to the user whose PM was
read, so it lands in their personal conversation, never the group chat;
or both. Add a unit test that drives a PM containing a known leak phrase
through the trigger and asserts the resulting agent reply (or the
inserted message row) does not contain it.

**Confidence:** High.

---

### [P0] — Quiet hours bypassed for per-recipient push when a group notification fans out

**References:**
- `Travel Agent/backend/notifications/gates.py:113-154` (`check_quiet_hours` gates only at the per-user *evaluation* stage)
- `Travel Agent/backend/api/lifecycle.py:833-846` (gates are applied to `members_passing`; users in quiet hours are excluded from the set fed to triage, but)
- `Travel Agent/backend/notifications/state_updater.py:156-176` (`record_notification_dispatch` for `target_audience="group"` fans out to *every* trip member's `notification_state` via `get_notification_states_for_trip`)
- `Travel Agent/backend/notifications/state_updater.py:90-115` (each per-user `on_notification_sent` calls `fan_out_to_channels_sync`)
- `Travel Agent/backend/notifications/channel_dispatch.py:121-129` (fan-out checks `prefs.pause_all` but never re-runs `check_quiet_hours`)
- `Travel Agent/backend/notifications/push.py:35-74` (the *deterministic* push helpers DO consult `check_quiet_hours` — the asymmetry is the smoking gun: the team thought to honour quiet hours for product pushes but forgot to do so on the triage fan-out path)

**Why it matters to a real tester:**
A user who sets quiet hours (10pm–8am) and is in a group trip with even
one member outside that window will get woken up. The proactive loop runs
on cadence, the gate filters that user out of the triage *context*, triage
decides to send a "group" nudge, and `record_notification_dispatch` blasts
push to every member regardless of their individual quiet-hours setting.
The user did exactly what the product asked them to do — set quiet hours —
and the product still pushed at 2am. Trust break.

**Repro / deterministic test idea:**
1. Trip with Alex (no quiet hours) and Sam (quiet hours 22:00–07:00 in
   `America/New_York`).
2. Local clock 02:30 in `America/New_York`.
3. Have triage emit a `TriageNotification(decision="send", target="group",
   urgency="fyi", channels=["push"])`.
4. Assert no `notification_deliveries` row with `channel='push'` and
   `status='sent'` is created for Sam — current code records one with the
   push body actually fired.

**Suggested fix direction:**
Re-check `check_pause_all` *and* `check_quiet_hours` per recipient inside
`fan_out_to_channels`, with `urgency='time_sensitive'` allowed to bypass
quiet hours only when `prefs.critical_always` is true (matching the
existing gate-prompt comment at `gates.py:120-122`, which currently has
no enforcement counterpart). Skipped deliveries should land with
`status='skipped'` and `error_detail='quiet_hours_active'` so the
asymmetry shows up in analytics. Add tests parallel to the existing
`tests/notifications/test_push_gates.py` (which covers the deterministic
helpers) for the triage-driven fan-out path.

**Confidence:** High.

---

### [P1] — Booking-proposal status pushes inherit the same group-conversation routing bug

**References:**
- `Travel Agent/backend/notifications/home_event_bridge.py:130-187` (`notify_booking_proposal_change` builds `target_kind="private"` notifications carrying booking detail)
- `Travel Agent/backend/concierge/tool_handlers/booking_flow.py:375-419` (dispatches via the same `run_proactive_turn` path)
- inherits the P0 above: the agent reply lands in the group conversation

**Why it matters to a real tester:**
The booking-proposal bridge composes prompts like "Booking confirmed for
Ramiro at Tue 8pm. Send a tight one-line push so the traveler knows." The
Sonnet reply (confirmation number, time, price, sometimes the cabin
class) is private to the traveler who booked, but it appears in the group
chat. For a launch focused on the booking moat this is exactly the wrong
detail to leak.

**Repro / deterministic test idea:**
1. Two-member trip. User A initiates a booking proposal, the booking
   agent transitions it to `confirmed`.
2. Observe the group conversation for User A's trip — assert no message
   row containing the confirmation phrase ("Booking confirmed",
   "Ramiro", or whatever the cap.venue_name returns).

**Suggested fix direction:**
Same root cause as Finding 1 — once `run_proactive_turn` routes
`target_audience="private"` to a personal conversation, this regression
class disappears. Regression test fixture: confirm that a booking-event
push dispatched via `notify_booking_proposal_change` writes a `messages`
row only inside the personal-trip conversation, not the group
conversation.

**Confidence:** High.

---

### [P1] — Daily notification cap is per-(user, trip) not per-user — multi-trip members can be spammed

**References:**
- `Travel Agent/backend/notifications/config.py:13` (`max_notifications_per_day: int = 4`)
- `Travel Agent/backend/notifications/gates.py:56-75` (`check_daily_limit` reads `state.notifications_today`, which lives on `notification_state` — keyed `(user_id, trip_id)`)
- `Travel Agent/backend/core/db/_tables/notifications.py:41-79` (`notification_state` unique constraint is on `(user_id, trip_id)`, so the counter resets per trip)

**Why it matters to a real tester:**
Cap is documented as "4/day". For a user planning one trip, it works. For
a dogfooder who is in five active trips (the dogfood loop is "plan a real
trip" — at scale these compound), the actual max is 4 × 5 = 20 per day,
1.5× of that on `eager` cadence. The dogfooder will perceive this as
spam and turn the product off. Worse, deterministic product pushes
(stories, shares_settled, booking_event) bypass `check_daily_limit`
entirely (see `backend/notifications/push.py:35-74` — only checks
`pause_all` and `quiet_hours`).

**Repro / deterministic test idea:**
1. Create one user in 4 active trips.
2. For each trip, force the proactive loop to send 4 group notifications
   (simulate by stubbing triage or by direct calls to
   `record_notification_dispatch`).
3. Count `notification_deliveries` rows with `channel='push'` and
   `status='sent'` for that user in the last 24h — expect ≤4 (the
   documented cap), observe 16.

**Suggested fix direction:**
Add a per-user daily counter (`user_notification_state` or extend
`user_notification_preferences` with a daily tally + reset window —
mirrors the `chat_token_counters` / `voice_quota_counters` /
`invite_dispatch_counters` pattern). Check it inside
`fan_out_to_channels` *and* honour it from the deterministic push
helpers. Pre-launch: at minimum set the per-trip cap lower (2/day) given
that real dogfooders will be in 2–3 trips at once.

**Confidence:** High.

---

### [P1] — Triage prompt assembles per-member taste snippets with names, which the agent then carries into a group reply

**References:**
- `Travel Agent/backend/api/lifecycle.py:860-876` (per-member taste snippet via `extract_taste_snippet(pm.markdown_content)`, formatted as `"{name}: {snippet}"`)
- `Travel Agent/backend/notifications/experience_opportunities.py:168-194` (snippet is 300 chars; falls back to first 300 chars of raw PM when "Who They Are" header is absent)
- `Travel Agent/backend/notifications/triage.py:271-298` (taste_summaries handed to Haiku triage prompt)
- `Travel Agent/backend/notifications/prompts.py:49-53` (triage prompt explicitly authorises the LLM to put the constraint reason into `prompt_for_agent`, then Sonnet composes a group-bound reply through Finding 1's bug)

**Why it matters to a real tester:**
"Who They Are" is the most identity-laden section of the PM — it's the
free-form prose Vesper synthesises from observations including hard
constraints. Even when the agent's reply *intends* to be neutral, the
LLM is being primed with "Sam: vegetarian, anxious in crowds, prefers
matcha lattes; Lilia: gluten-free, mobility-limited" and asked to choose
the best per-traveler nudge. The reply path (group conversation, per
Finding 1) means any leak in the model's compose is group-visible. When
the fallback path triggers (no `Who They Are` header), 300 raw chars of
markdown are pasted in — same hazard as the events_tonight trigger.

**Repro / deterministic test idea:**
Seed a PM where the `Who They Are` section contains a known constraint
phrase, fire one triage cycle with an upcoming experience that matches
that constraint, capture (a) the Haiku prompt sent to triage and (b) the
resulting Sonnet group-conversation reply. Assert (a) does not include
constraint-language for users not addressed by the nudge, and assert (b)
does not include any constraint phrase verbatim regardless of who's
addressed.

**Suggested fix direction:**
1. Route private notifications to personal conversations (Finding 1) so
   the blast radius is bounded.
2. Replace `extract_taste_snippet` with a *group-safe* synthesiser that
   strips constraint sentences before they enter the triage prompt (the
   existing `backend/synthesis/group_synthesizer.py` machinery is the
   right home).
3. When the fallback path fires (no header found), refuse to send rather
   than dump raw PM into the prompt.

**Confidence:** High.

---

### [P2] — Triage runs even when zero members pass gates if any outcome is pending; dispatches still slip out

**References:**
- `Travel Agent/backend/api/lifecycle.py:842-846, 883-892` (early-return only when *both* `members_passing` is empty *and* `pending_outcomes` is empty; otherwise triage runs with `members_passing or notif_states` → falls back to all members)

**Why it matters to a real tester:**
Late at night when everyone in the trip is in quiet hours and there
happens to be a pending outcome (a notification fired earlier that
hasn't been responded to), the loop will still call Haiku with the full
member list and may decide to send a *new* notification — and because
of the quiet-hours-bypass-at-fan-out bug (Finding 3), that notification
actually lands as a push. Compounding two soft bugs.

**Repro / deterministic test idea:**
Trip with one member, quiet hours 22–8. Inject a `pending` outcome.
Run `_evaluate_trip_notifications` at 03:00 local. Observe Haiku call
and ensuing dispatch.

**Suggested fix direction:**
Tighten the early-return: if `members_passing` is empty, run only
outcome *evaluation* on existing pending rows, never send fresh
notifications. Even simpler — skip the cycle entirely; the next tick
will pick up the work once any member exits quiet hours.

**Confidence:** Medium.

---

### [P2] — Invite-intake dispatch path skips the per-user daily limit and per-trip group interval

**References:**
- `Travel Agent/backend/api/routes/invites.py:801-851` (`_dispatch_intake_notification` jumps straight to `record_notification_dispatch` with no gate check)
- `Travel Agent/backend/notifications/state_updater.py:138-155` (`record_notification_dispatch` for `target_audience="private"` simply increments the counter and fans out)

**Why it matters to a real tester:**
An organizer running a 50-person invite blast will receive 50 push
notifications, even though their nominal daily limit is 4. The bell pip
is already correct (one badge counter), but pushes are not capped or
coalesced. Mitigated for typical 4-6 person trips; concerning for
power users or accidental loops.

**Repro / deterministic test idea:**
Mint 10 invites on a trip, have each invitee submit_intake. Count push
deliveries to the organizer; expect ≤ 4 (daily cap), observe 10.

**Suggested fix direction:**
Either (a) coalesce intakes into "3 new invite answers" when more than
N land within a window, or (b) hard-cap to the daily limit by passing
the intake-dispatch path through `check_daily_limit` before calling
`record_notification_dispatch`.

**Confidence:** Medium.

---

### [P2] — `critical_always` user preference has no enforcement counterpart

**References:**
- `Travel Agent/backend/core/db/_tables/notifications.py:103` (column exists, defaults true)
- `Travel Agent/backend/notifications/gates.py:113-154` (`check_quiet_hours` returns hard fail; never reads `prefs.critical_always`)
- `Travel Agent/backend/notifications/gates.py:120-122` (comment promises "the triage layer is told about critical_always and decides whether a time-sensitive notification is worth violating the policy" — neither the triage assembly nor the prompt mentions `critical_always`)

**Why it matters to a real tester:**
The DB column suggests a contract: time-sensitive items can pierce
quiet hours when the user opted in. The contract isn't implemented —
quiet hours always win, regardless of urgency. Pre-launch this only
matters if someone advertises "we'll wake you for a flight gate change."
If we *don't* want that, drop the column; if we do, the gate needs to
short-circuit on `(urgency == 'time_sensitive') and prefs.critical_always`.

**Suggested fix direction:**
Either remove `critical_always` from the schema + prefs Pydantic model,
or wire it into `check_quiet_hours`/`fan_out_to_channels` with explicit
tests covering both branches.

**Confidence:** Medium.

---

### [TECH-DEBT] — `triggers.py` docstring promises session-layer routing that does not exist

**References:**
- `Travel Agent/backend/concierge/triggers.py:32-43` (docstring claims "target_audience" and "target_user_id" are "session-layer routing only" and "The routing fields stay out of the LLM context by design — the agent decides what to say; the session decides where to send it.")
- `Travel Agent/backend/concierge/triggers.py:48-95` (session selection is hard-coded to the trip's group conversation; nothing reads `triage_metadata['target_audience']` for routing)

The docstring is the strongest hint that someone intended Finding 1's
fix but it never landed. Once Finding 1 is fixed the docstring becomes
accurate; until then it actively misleads readers of the code.

**Confidence:** High.

---

### [TECH-DEBT] — `_filter_unknown_channels` validator on `TriageNotification` returns the raw value when shape is wrong

**References:**
- `Travel Agent/backend/notifications/triage.py:73-94` (`if not isinstance(v, list): return v  # type: ignore[return-value]`)

If the LLM returns `"channels": "push"` (string, not list) the validator
hands the string back to Pydantic, which will then raise. That works, but
the docstring claims "filter here so the valid entries still land". A
slightly safer default is `return None` on shape error so the legacy
"dispatch to everything the user allows" path takes over rather than
breaking the whole notification.

**Confidence:** Medium.

---

### [TECH-DEBT] — `_PROACTIVE_FEED_LIMIT = 50` paired with `notification_outcomes`/`notification_deliveries` cascades works, but bell badge can stall when a heavy user has >50 unread proactives plus unrelated conversations

**References:**
- `Travel Agent/backend/api/routes/_notifications_feed.py:257-318`
- `Travel App/components/ui/NotificationBell.tsx:25-29` (`unreadCount = notifications.filter((n) => !n.is_read).length`)

If a user accumulates 51+ unread proactives, the 51st (oldest) silently
falls out of the feed and the bell count under-reads. Dogfood will
probably never hit this, but worth flagging.

**Confidence:** Low.

---

## Known / Accepted

These are explicitly out of scope for this audit — either prior P0s now
closed, deferred-by-design items in the Known Gaps Register, or behaviours
the product has decided to live with.

- **`PendingInviteAnswer.answer_summary` is collapsed to the literal
  "Answered privately" by `summarize_pending_intake`**
  (`backend/core/models/trip_invites.py:206-222`). This was a P0 in the
  prior audit and is now closed; verified that the bell, the trip-info
  pending-invites surface, and the React Native renderer
  (`Travel App/data/notifications.ts:83-98`) all flow this constant only.
  The body string `"${a.answer_summary}"` in the RN renderer reads
  slightly awkwardly ("Answered privately" wrapped in curly quotes), but
  it does not leak.

- **G-7 per-recipient intake dedupe**
  (`backend/api/routes/invites.py:727-786`). Captures the BEFORE state
  and skips dispatch when an unacknowledged intake is just being revised.
  Tested behaviour, kept.

- **G-3 dedicated per-conversation interjection cooldown**
  (`conversations.last_interjection_at` + 30-minute cooldown, gates +
  cooldown in `group_interjection.py`). Working as designed.

- **G-2 — synchronous interjection deferred** (Known Gaps Register §
  Group Dynamics). The 5-minute scan window is the documented worst-case
  latency; not a privacy bug.

- **G-10 — Transport Nudge 2 dormant** (Known Gaps Register § Group
  Dynamics). Predicate hardcoded to `False`; not a regression source.

- **Logout deregisters the push token before sign-out**
  (`Travel App/app/(tabs)/me/account.tsx:178-205` calls
  `unregisterPushNotifications` while still authenticated; in-memory id
  + AsyncStorage fallback in `utils/push.ts:212-247`). Verified end to
  end.

- **Account deletion cascades push devices and notification state**
  (`backend/core/db/account_deletion.py:227-241` generic sweep + FK
  CASCADE on `user_devices`, `notification_state`,
  `notification_outcomes`, `notification_deliveries`). Frontend doesn't
  re-call `unregisterPushNotifications` on the delete path, but the
  server-side cascade plus the residual-reference scan covers the data;
  the Expo-side subscription becomes inert once our token row is gone.
  Acceptable.

- **Deterministic product pushes (`send_shares_settled_push`,
  `send_story_ready_push`) bypass cadence + daily limits but honour
  `pause_all` and `quiet_hours`** (`backend/notifications/push.py:35-74`).
  Explicitly documented design tradeoff for events the product deems
  always-worth-it. Worth revisiting once the per-user daily cap from
  Finding 5 lands so that a runaway loop in either helper can't
  bypass it.

- **Digest engine has no push surface and is gated by
  `DISABLE_LLM_BACKGROUND_LOOPS`** (`backend/digest/engine/daily.py`,
  `backend/api/lifecycle.py:728-752`). Quiet hours don't apply because
  the digest never wakes a phone. The `_gather_day_inputs` query at
  `_shared.py:243-259` does pull all-member observations without per-
  visibility filtering, but the digest's downstream consumers are the
  planner + admin UI today; if a future surface ever renders the digest
  text back to the group, the observation visibility filter (mirroring
  M-2 in the Known Gaps Register) becomes a real concern.

- **`EXPO_PUSH_ENABLED=false` falls back to log-only push, recording
  `status='sent'`** (`channel_dispatch.py:414-427`). Documented design;
  prevents accidental sends in dev/eval; analytics intentionally treat
  log-only as "operator's choice, not a failure".

- **`O-15` (durable per-call LLM cost log) and `O-16` (alerting on
  background loop fire-rate) are still deferred** per the Known Gaps
  Register. The notification triage loop benefits indirectly when both
  ship, but neither blocks dogfood.

- **`max_notifications_per_cycle=2` in `NotificationSettings`** caps a
  single triage cycle but is per-trip; combines with the per-trip daily
  cap noted in Finding 5.
