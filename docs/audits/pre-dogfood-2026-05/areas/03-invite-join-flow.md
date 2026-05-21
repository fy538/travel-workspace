# Pre-Dogfood Area Audit 03 — Invite → Join Flow

Date: 2026-05-21
Scope: invite mint → dispatch → landing → intake → accept, idempotency &
race semantics, per-user dispatch quota, public landing/AASA/Universal
Links, deep-link token survival across auth, SendGrid/Twilio graceful
degradation, mock-vs-real parity for the invite client surface.
Mode: read-only; no product code, test, or config was modified.

## Summary

| Severity | Count |
|---|---:|
| P0 | 4 |
| P1 | 3 |
| P2 | 3 |
| TECH-DEBT | 2 |

**Status of the prior `dogfood-readiness.md` invite findings.** I confirmed
both invite P0s and the idempotency P1 from 2026-05-21 are *largely* closed:
`pending_intake_summary` now collapses to the neutral `"Answered privately"`
literal (`backend/core/models/trip_invites.py:206-222`); the
`invite.intake_received` and `invite.consumed` `trip_events` payloads carry
`token_fp` instead of the raw token (`backend/api/routes/invites.py:757`,
`:977`); `PendingInviteAnswer.invite_token` is hashed at the feed boundary
(`backend/api/routes/_notifications_feed.py:22-26, :206`); and a consumed
single-use invite retried by the same authenticated user now resolves to
200 via `_recover_consumed_invite` (`backend/api/routes/invites.py:881-928`),
with a passing test at `tests/api/test_invites_api.py:739-760`.

**The catastrophic-failure framing still has open holes.** Four raw-token
egress paths slipped through the prior P0 sweep: `_accept_trip_invite`'s
exception log still formats `token` (`invites.py:952-957`), the
conversation-scope twin does the same (`:1080-1085`), the
post-accept observation seeded for Personal Memory persists the raw token
in `provenance.token` (`:1018`), and — most operationally dangerous for
dogfood — the **`LogOnlyDispatcher` fallbacks** (the default with no
Twilio/SendGrid creds) log the SMS/email body which contains the full
share URL `…/invite/{token}` (`backend/notifications/invite_dispatch.py:114`,
`backend/notifications/email_dispatch.py:74-79`). A fifth, separate path:
the Home feed renders three `group_state` cards whose `ref_id = inv.token`
(`backend/home/feed.py:431, 449, 461`), so every organizer's home payload
ships their own join credentials in JSON. None of these are guarded by a
regression test.

On the **first-impressions** side: iOS Universal Links will silently fail
to deep-link the app because `INVITE_APPLE_TEAM_ID` defaults to
`REPLACE_ME` (`invite_landing.py:60`) and no preflight surfaces the
mis-rendered AASA file. And the **mock client** still surfaces verbatim
chip text as `pending_intake_summary` (`Travel App/utils/api/mock.ts:2699`),
which means UI tests against the mock encode the unsafe behaviour that the
real backend just stopped doing — the privacy primitive has no parity
guard.

Everything else found is in-scope tightening: the accept handler accepts
`X-Idempotency-Key` and silently ignores it; the public intake POST has no
abuse rate-limit; a now-dead `status === 409` branch on the FE; trip
`/api/invites/{token}/intake` events still journal the full chip text
server-side (intentionally, but worth marking).

## Findings

### [P0] — Raw invite token persisted to `observations.provenance` at accept time
**References:** `Travel Agent/backend/api/routes/invites.py:1003-1020`
**Why it matters to a real tester:** The post-accept background task
seeds the new member's Personal Memory with their pre-auth chip/free-text
answers — fine on its own — but writes `provenance={"source":
"invite_intake", "token": tok}` into the observation row. `observations`
is the most-read DB surface in the product: reflection, Personal Memory
synthesis, the `/debug/cost` cycle, support exports, every `make pm-diff`
run, and the `personal_memories` text rendered back to the user all touch
it. The raw token sits there forever (no TTL on observations) and is
trivially `SELECT`-able. It is the join credential for whichever trip the
user joined; anyone with read access to observations can join that trip
silently. The prior P0 fix explicitly said *use a token fingerprint or
invite id in any artifact outside the trip_invites row itself* — this
call site was missed.
**Repro / deterministic test idea:**
1. `POST /api/invites/tok_secret/intake` with `{"chip_answer": "I'm in"}`.
2. Sign in as a fresh user, `POST /api/invites/tok_secret/accept`.
3. Wait for the `_persist_intake_and_synthesize` background task.
4. `SELECT provenance FROM observations WHERE user_id = <new user>` and
   assert `'token'` does **not** appear; only `'token_fp'` or invite row
   identity does.
**Suggested fix direction:** swap `"token": tok` for
`"token_fp": _token_fp(tok)`. Observations only need correlation, not
the bearer secret; the trip_id is already inferable from the user's
membership added moments earlier.
**Confidence:** High.

### [P0] — `LogOnlyDispatcher` (default when no Twilio/SendGrid creds) logs the share URL with the raw token
**References:** `Travel Agent/backend/notifications/invite_dispatch.py:104-116`,
`Travel Agent/backend/notifications/email_dispatch.py:58-85`,
`Travel Agent/backend/notifications/invite_dispatch.py:229-246` (body
composition includes `\n{url}` where `url = PUBLIC_INVITE_BASE_URL/{token}`)
**Why it matters to a real tester:** `LogOnlyDispatcher` is what the
factory returns when `TWILIO_*` or `SENDGRID_*` env vars are unset
(`invite_dispatch.py:204-210`, `email_dispatch.py:151-166`). That is the
default for every dogfood environment until the operator wires provider
credentials — the Owner Action Items doc and the existing readiness P0
both note that hosting/credentials are still pending. So during exactly
the window the audit is sizing for, **every minted dispatch-bearing
invite emits the join credential at INFO level** via lines like
`LogOnlyDispatcher.send channel=sms to=+1555... body='Alice is planning
a trip — Berlin. Tap to see what it\\'s becoming:\\nhttps://travelagent.app/invite/<TOKEN>'`.
INFO-level logs are universally collected by `make logs`, support
screenshots, structured-log aggregators, error trackers (Sentry breadcrumbs
on a later failure attach them), and TestFlight diagnostic dumps. The
local rule documented at `invites.py:66-78` ("raw invite tokens are
bearer credentials and must never be written to logs") is broken at the
exact moment dispatch fan-out actually runs.
**Repro / deterministic test idea:** with `TWILIO_*` and `SENDGRID_*`
unset, `POST /api/trips/{trip_id}/invites` with
`{"contact_channel":"sms","contact_value":"+15551234567","contact_hint":"Sam"}`.
Capture the application log and assert the minted invite's `token` value
(or anything beyond the `_token_fp(...)` 10-char hash) does not appear
in any record at any level.
**Suggested fix direction:** in `LogOnlyDispatcher.send` and
`LogOnlyEmailDispatcher.send`, redact the URL before logging — e.g.
replace any substring matching `/invite/(\S+)` with `/invite/<token_fp>`,
or strip the body entirely and log only `len(body)`, `to`, and `channel`.
Add a unit test that captures `caplog` and asserts the token does not
appear in any record.
**Confidence:** High.

### [P0] — Home feed `group_state` cards ship the raw invite token as `ref_id`
**References:** `Travel Agent/backend/home/feed.py:423-466`
(three sites: `ref_id=inv.token` on the just-accepted, pending-too-long,
and unread-intake archetypes), `Travel Agent/backend/home/cards.py:53-85`
(`HomeCard.ref_id`)
**Why it matters to a real tester:** `HomeCard` is part of the public
home-cards response (`GET /api/users/{id}/home/cards`). Every organizer
who has a trip with any active or recently-consumed invite gets their
own join credentials echoed back in the JSON body of their home feed —
beyond the existing organizer-only invite-management surface, where the
URL belongs. Anyone with read access to a captured home response
(analytics breadcrumb on a 5xx, Chrome network panel screenshot during a
dogfood bug report, log of the response body in any HTTP middleware,
client-side React Query devtools) holds the token and can immediately
join the trip — or, for a multi-use group-share invite, can quietly add
themselves and look like one of the invitees. This is the same class as
the previously-fixed `PendingInviteAnswer.invite_token` leak; the home
card pathway was not part of that sweep.
**Repro / deterministic test idea:**
1. Create a trip; mint a `max_uses=5` invite (so `consumed_at` stays
   null, hitting the "pending too long" branch after 3 days, or directly
   stub `created_at` to push into the window).
2. `GET /api/users/{organizer}/home/cards` (or invoke
   `_build_group_state_card` directly in a unit test).
3. Assert that no card's `ref_id` matches the actual invite token. The
   ref_id should be `_token_fp(inv.token)` or the trip_id; dismissal
   key shape can keep its uniqueness via the fingerprint.
**Suggested fix direction:** replace `ref_id=inv.token` with
`ref_id=_token_fp(inv.token)` at all three sites. Tap-target on the
client routes by trip, not by token (the cards already render via
`archetype` + trip context), so a fingerprint is sufficient as the
dismissal correlator. If the client today reads `ref_id` to construct a
deep link, route to `/trips/{trip_id}/invites` instead — the organizer
can find the same invite by `contact_hint`/created-at on that surface.
**Confidence:** High.

### [P0] — Raw invite token logged when `add_trip_member` / `add_participant` raises a non-duplicate error
**References:** `Travel Agent/backend/api/routes/invites.py:946-958`
(trip path), `:1075-1086` (conversation path). Compare to the
fingerprinted siblings at `:318`, `:339`, `:341`, `:499`, `:578`, `:635`,
`:649`, `:769`, `:849`, `:984`.
**Why it matters to a real tester:** Both paths catch `Exception` from
the membership insert, branch on duplicate-string heuristic, and on the
non-duplicate branch `logger.exception("... via invite %s", ..., token)`.
That fires whenever the underlying DB write fails for any reason that
isn't a unique-constraint match — connection blip, FK timing, advisory-
lock contention, schema drift — and writes the raw token plus full
stack trace to ERROR-level logs. ERROR is what aggregators alert on and
what gets pasted into Slack and tickets when a tester reports "I tried
to join and it failed." Every recipient of that paste then holds the
join credential. The same `_token_fp` helper sits two lines away in the
journal write below it; the formatter just wasn't updated.
**Repro / deterministic test idea:** patch `add_trip_member` to raise
`OperationalError("connection lost")` (anything that doesn't match
`unique`/`duplicate` substring). `POST /api/invites/tok_secret/accept`.
Capture logs; assert `tok_secret` never appears, only
`_token_fp("tok_secret")`. Repeat against `_accept_conversation_invite`
via `add_participant`.
**Suggested fix direction:** change both `logger.exception` format-args
from `token` to `_token_fp(token)`. While there, the wrapped
`AgentError(str(e))` re-raises into the global `_agent_handler`, which
correctly redacts the inner detail before responding (audit B10) — but
the contained 500 still includes the raw token in the server-side
exc_info chain via the `str(exc)` repr. Same fix applies.
**Confidence:** High.

### [P1] — Mock invite client surfaces verbatim chip text as `pending_intake_summary`, contradicting the just-fixed real-backend privacy primitive
**References:** `Travel App/utils/api/mock.ts:2669-2710` (the
`pending_intake_summary: "I'm in"` literal at `:2699`), versus
`Travel Agent/backend/core/models/trip_invites.py:203` (real backend
emits the constant `"Answered privately"`)
**Why it matters to a real tester:** The prior P0 — "intake answers
exposed to organizer despite privacy promise" — was closed by collapsing
the real-backend summary to the neutral string `"Answered privately"`.
The mock surface still returns the chip's literal text. So any UI
snapshot test, jest assertion, or visual-regression run against
`EXPO_PUBLIC_USE_MOCK_API=true` will encode the unsafe rendering as the
expected behavior. If a future refactor regresses the real backend back
toward leaking chip content, the mock-vs-real parity suite (`make
mock-real-parity`, the rationale for which is the *whole point* of this
seam — see workspace `AGENTS.md` cross-repo contract) will not catch it,
because the mock asserts the leaky shape is "fine." This is a paper-thin
parity drift on the most privacy-sensitive primitive in the area.
**Repro / deterministic test idea:** add an assertion to
`__tests__/data/notifications.test.ts` (or a new mock-parity test) that
the mock's `listTripInvites` and any `pending_invite_answers` surface
returns *only* `null` or the literal string `"Answered privately"` for
`pending_intake_summary` / `answer_summary`. The current mock fixture
fails it. Optionally extend `Travel Agent/scripts/api-coverage-check.py`
to also walk the mock module for hardcoded chip text in invite-summary
positions.
**Suggested fix direction:** replace the mock's `"I'm in"` /
`"Need dates first"` literals with the same `PRIVATE_INTAKE_SUMMARY`
constant the backend uses (or re-export it from the generated schema
when the constant lands in the OpenAPI examples). Add a comment at the
mock site that points back to `summarize_pending_intake` so the next
mock-fixture editor doesn't reintroduce content.
**Confidence:** High.

### [P1] — iOS Universal Links silently fail because the AASA file ships with `REPLACE_ME` as the Apple Team ID
**References:** `Travel Agent/backend/api/routes/invite_landing.py:56-66`
(`APPLE_TEAM_ID = "REPLACE_ME"` default), `:287-319`
(`apple_app_site_association` returns `appIDs: ["REPLACE_ME.com.travelagent.app"]`),
`Travel App/app.json:19-22` (`associatedDomains: ["applinks:travelagent.app"]`),
`Travel App/eas.json:18-35` (TestFlight builds point at
`travelagent.app` / `travel-agent.fly.dev`)
**Why it matters to a real tester:** The invite → join loop **is** the
acquisition path. A tester taps an SMS/email invite, lands on
`https://travelagent.app/invite/<token>`, and expects the app to take
over. iOS fetches the AASA file, sees `REPLACE_ME.com.travelagent.app`
as the only claiming `appID`, doesn't match the installed bundle, and
silently falls back to Safari. The user sees the HTML landing, taps
"Open in the app" which goes to `guide://invite/<token>` — that works
*only if* the custom URL scheme is registered (it is, via
`expo.scheme: "guide"`), but it bypasses Universal Links entirely, so
deferred deep linking (tap-then-install-then-open) is broken. Two
secondary effects: (a) the `apple-itunes-app` Smart App Banner relies
on the same AASA claim to surface the "Open" affordance, so the
top-of-Safari banner is degraded; (b) the existing readiness P0 about
unreachable hosts (`travelagent.app` returns 000) means the AASA file
isn't even fetchable today, so this issue compounds: when the host
finally comes up, deep-linking will still be broken until the team-id
env var is set. **There is no preflight or runtime guard.**
**Repro / deterministic test idea:** in `scripts/preflight-eas-build.sh`,
fetch `https://<EXPO_PUBLIC_API_URL>/.well-known/apple-app-site-association`
and assert `payload.applinks.details[0].appIDs[0]` does not contain
`REPLACE_ME`. Locally: `curl -s http://localhost:8000/.well-known/apple-app-site-association
| jq -r '.applinks.details[0].appIDs[0]' | grep -v REPLACE_ME`. Today
that grep returns empty.
**Suggested fix direction:** add the team-id check to the preflight
script (cheap; doesn't need EAS or network). At deploy time, require
`INVITE_APPLE_TEAM_ID` to be set; refuse to serve the AASA file with
the placeholder (return 503 with an explicit "AASA misconfigured" log)
rather than silently shipping a broken manifest. Document the env var
in `docs/Owner Action Items.md` alongside the existing release-host
checklist.
**Confidence:** High.

### [P1] — `POST /accept` accepts `X-Idempotency-Key` and then ignores it; recovery relies entirely on a same-user membership probe
**References:** `Travel Agent/backend/api/routes/invites.py:861-890`
(signature parses `X-Idempotency-Key`, never reads it),
`:893-928` (`_recover_consumed_invite` is the only safety net),
`Travel Agent/backend/api/routes/invites.py:242-254` (mint shows the
pattern — `get_cached_response` / `register_in_flight` /
`record_response` — that accept does not follow),
`Travel App/app/invite/[slug].tsx:122-149` (FE generates and sends a
stable key)
**Why it matters to a real tester:** the FE sends the header; the API
parses it; nothing uses it. The membership-probe recovery the prior P1
fix added does work for the dominant single-use-trip case, but it has
three sharp edges that an `X-Idempotency-Key` cache would cover
cleanly: (1) **bystander false-positive** — if any other code path
makes the actor a member of that trip (organizer added them directly,
they accepted a different invite first), a replay of a now-consumed
unrelated token returns 200 with `trip_id` of the consumed invite,
which is misleading data the FE will use to navigate; (2)
**conversation-scope multi-use ambiguity** — same shape for
`is_participant`; (3) **background-task duplication** — the recovery
path skips `consume_invite`/`add_trip_member`/`append_trip_event` (good)
but also skips the genesis-social-state background task scheduling
(`:1041-1049`) — which is correct for replays but means the FIRST
successful 200 must always be the one that schedules it. If the
membership write succeeded but the response was lost *before*
`background_tasks.add_task` ran (the request was killed mid-handler),
genesis never fires for that trip; the next retry can't re-schedule it
because the recovery path returns early. A real idempotency cache that
remembered "this key produced this response and these side-effects ran"
would not have this hole.
**Repro / deterministic test idea:**
1. Add `actor` to trip via the organizer-add path (not via invite).
2. Replay `POST /api/invites/<consumed-token-from-different-flow>/accept`
   with the actor's auth and any `X-Idempotency-Key`.
3. Today: 200 with the foreign invite's `trip_id`. Expected with
   idempotency: a fresh request returns 410 (not redeemable, never
   redeemed by you) unless the key matches a prior success in the
   cache.
**Suggested fix direction:** either (a) wire the same
`get_cached_response/register_in_flight/record_response` pattern used
in `mint_invite` around `accept_invite` keyed on
`("accept_invite", token, actor.id, x_idempotency_key)` — short doc on
why we cache by (token, actor) and not by key alone, so a
multi-tab/multi-device retry with different keys still converges; or
(b) explicitly drop the header from the signature and document that
the membership probe is the only retry safety net, with a same-user
`consumed_by` assertion inside `_recover_consumed_invite` so the
bystander false-positive can't fire. Either is acceptable; the current
half-state (parse-then-ignore) is the worst of both.
**Confidence:** Medium-high.

### [P2] — Public `/api/invites/{token}/intake` has no rate limit; a token holder can spam organizer notifications
**References:** `Travel Agent/backend/api/routes/invites.py:703-786`
(no quota check, no token-bucket, no IP throttle),
`Travel Agent/backend/core/db/trip_invites.py:179-205`
(`record_pending_intake` resets `intake_seen_at = NULL` on every write
and merges JSONB on every call),
`Travel Agent/backend/api/routes/invites.py:785-786` (G-7 dedupe gate
suppresses repeat push only while `was_unacknowledged_before=True`)
**Why it matters to a real tester:** any holder of an invite token —
the recipient, anyone they forwarded the SMS to, anyone who captured
the token from the URL bar — can fire `POST /intake` in a loop. Each
call resets the bell badge, re-arms the dedupe window (after the
organizer next opens `GET /trips/{id}/invites` to clear
`intake_seen_at`), and on the cleared-then-write transition fires a
fresh push + (if the organizer hasn't muted SMS for trip channel) a
real Twilio SMS to the organizer. The dispatch cap is on the **mint**
side (`invite_dispatch_counters`), not on intake-triggered pings, so
the organizer's phone becomes a free abuse channel. The blast radius
is bounded by the token-holder population and the organizer's
ack-cadence, but during dogfood with a small group it is more than
enough to break trust in the bell. Lower priority than the P0/P1
egress paths because the attacker needs the bearer token, but worth
adding the lightest rate limit before live testers arrive.
**Repro / deterministic test idea:** in a loop, alternate
`POST /api/invites/<token>/intake` and (as the organizer)
`GET /api/trips/<trip_id>/invites` to clear `intake_seen_at`. Count
`record_notification_dispatch` invocations and Twilio API calls
attempted; assert the count is bounded per (token, day) to a small N.
Today it is unbounded.
**Suggested fix direction:** add a small per-token-per-hour counter
(reuse the `invite_dispatch_counters` pattern keyed on `(token,
hour_utc)` or a new table) that gates only the *push/SMS dispatch*
side, not the pending_intake write — so the recipient can still revise
their answer in-app, but the organizer is rate-limited to e.g. 3 push
+ 1 SMS per token per hour regardless of intake churn. Bell + in-app
list stay accurate.
**Confidence:** Medium.

### [P2] — Frontend's `if (status !== 409)` accept-error branch is now dead; the "treat 409 as already-joined" affordance silently never fires
**References:** `Travel App/app/invite/[slug].tsx:152-164`
**Why it matters to a real tester:** the FE was written when the
backend distinguished "already a member" (409) from "consumed" (410)
from "expired" (410). After the prior P1 fix, the backend never
returns 409 from `accept_invite`: `_recover_consumed_invite` returns
200 with the existing membership for the same-user retry, the
duplicate-insert path is caught inside `_accept_trip_invite` and also
returns 200, and unrecoverable cases return 410. The
`status === 409` fallback that "uses the known IDs from the invite
view" is unreachable. It is harmless — the recovery path now produces
the same outcome via 200 — but it is brittle: a future backend tweak
that *does* re-introduce 409 (e.g. an idempotency-key conflict for the
P1 above) would suddenly cause a silent navigation via stale invite
data instead of an alert. Either delete the branch or back-fill the
backend behavior the FE still asks for.
**Repro / deterministic test idea:** assert in a unit test that
`backend/api/routes/invites.py::accept_invite` never returns 409 for
any input matrix; or delete lines 154-164 and run the
`__tests__/screens/invite-landing.smoke.test.tsx` to confirm no path
relies on it.
**Suggested fix direction:** delete the 409 branch and the comment;
let the catch-all alert path handle any non-recoverable error. If P1
above is fixed by introducing an idempotency-key 409, restore the
branch consciously then.
**Confidence:** High.

### [P2] — Trip-scoped `invite.intake_received` event still journals the full chip + free-text payload in `trip_events.payload.intake`
**References:** `Travel Agent/backend/api/routes/invites.py:750-764`
(`payload={..., "intake": payload}` where `payload` is the full
`{chip_answer, free_text}` dict)
**Why it matters to a real tester:** unlike the **API-facing**
neutrality that `summarize_pending_intake` provides, the
**`trip_events` journal** stores the raw chip + free-text per invite
event. The journal is not currently exposed in any
organizer-readable route (I checked `grep -r trip_events
Travel\ Agent/backend/api/routes/` — only invites.py writes and
nothing reads), so this is not a present-day leak. It is a latent one:
the next surface that exposes the audit journal (e.g. an admin
viewer, a debug endpoint, an export script) will silently echo the
"I cannot afford expensive dinners" string into a place organizers can
read. The journal already preserves *who answered and when* via
`token_fp` + `created_at`; the substance is what should drop out.
**Repro / deterministic test idea:** add a regression test that
asserts `trip_events.payload` for `event_type='invite.intake_received'`
contains only `{token_fp, contact_hint}` (or, if intake substance
must persist for debugging, that the substance is moved to a
separately-scoped journal table that is *not* trip_id-keyed).
**Suggested fix direction:** drop `"intake": payload` from the
`append_trip_event` call. The invitee's substance is already
authoritatively stored in `trip_invites.pending_intake` (with proper
access controls) and in their own `observations`; the journal only
needs the event-happened signal. If retention is genuinely required
for ops, gate the field on a `JOURNAL_INCLUDE_INTAKE_CONTENT` env var
default-off.
**Confidence:** High.

### [TECH-DEBT] — `mint_invite` idempotency cache is in-process; cross-pod retries mint fresh tokens and re-fire dispatch
**References:** `Travel Agent/backend/api/routes/invites.py:240-254,
:345-354` (uses `backend.core.idempotency.get_cached_response /
record_response` — in-memory),
`Travel Agent/backend/core/idempotency.py` (implementation)
**Why it matters to a real tester:** if dogfood ever runs on more than
one backend pod (which the current Fly config does not yet — single
instance assumed — but is the natural growth path), the FE's
`X-Idempotency-Key` on mint stops being honored across pod boundaries.
A retry that lands on a different pod mints a fresh token, fires a
fresh SMS, and counts a fresh row against `invite_dispatch_counters`.
This is fine at single-pod dogfood scale but should be flagged before
any horizontal scaling.
**Suggested fix direction:** move the idempotency cache to Postgres
(small TTL'd table keyed on the same tuple) when the deployment
shape changes; gate behind an env var so single-pod stays fast.
**Confidence:** Medium.

### [TECH-DEBT] — `Travel Agent/docs/openapi.json` drift vs the workspace snapshot is a latent contract risk for the invite surface
**References:** `CLAUDE.md` "Single source of truth: docs/openapi.json
in THIS workspace repo"; current `docs/openapi.json` shows
modification in `git status`. Invite endpoints (`view_invite`,
`accept_invite`, `submit_intake`) and their response models are all
in scope.
**Why it matters to a real tester:** if the workspace snapshot
captures something different from the Travel Agent local snapshot
(e.g. a `pending_intake_summary` description that still hints at
content, or an `InviteAcceptResponse` shape used by the FE), the
generated TS types in `Travel App/utils/api/schema.gen.ts` lock in
the wrong contract and the FE renders the wrong fields.
`make api-coverage-check` only verifies URL coverage, not field
semantics.
**Suggested fix direction:** run `./scripts/sync-types.sh` and inspect
the diff in `docs/openapi.json`. If the diff is invite-related,
regenerate and commit; if it's unrelated noise, document in the
commit. Add a CI assertion that the workspace snapshot's invite
schemas carry no chip-content strings in `example` blocks.
**Confidence:** Medium-low (verified the diff exists in `git status`
but did not inspect it as part of this read-only audit).

## Known / Accepted

Items previously filed in `dogfood-readiness.md` (2026-05-21) that this
audit re-verified as **closed** and is *not* re-filing:

- **Organizer-visible chip text leak via `pending_intake_summary`** —
  fixed. `summarize_pending_intake` now collapses both `chip_answer`
  and `free_text` to the single literal `"Answered privately"`
  (`Travel Agent/backend/core/models/trip_invites.py:203-222`); the
  notification-feed renderer carries the neutral string through
  unchanged (`Travel App/data/notifications.ts:90-92`). Test coverage
  is at `tests/api/test_invites_api.py:872+` and the model unit tests.
- **Raw `token` in `trip_events.payload` for `invite.intake_received`
  and `invite.consumed`** — fixed. Both call sites now use
  `_token_fp(token)` (`invites.py:757`, `:977`); test coverage at
  `tests/api/test_invites_api.py:437` (intake) and
  `tests/api/test_invites_api.py:721+` (accept). The full chip
  *payload* is still journaled — see the P2 above for that residual.
- **Raw token in dispatch failure logs in `mint_invite` / `_safe_dispatch`** —
  fixed. `logger.exception("Invite dispatch task failed for %s",
  _token_fp(invite.token))` at `:318` and `:499`.
- **`PendingInviteAnswer.invite_token` exposing raw token in the
  notification feed** — fixed. `_invite_token_fp(token)` is applied at
  `_notifications_feed.py:206`; the FE-generated AppNotification id
  uses the hashed form (`Travel App/data/notifications.ts:85`).
- **Accept-after-consumed retry returning 410 to the same user** —
  fixed via `_recover_consumed_invite` (`invites.py:881-928`); test
  at `tests/api/test_invites_api.py:739-760` asserts the same-user
  retry returns 200 with the existing membership.
- **Pending-invite-token persistence across the auth bounce** —
  verified working. `setPendingInviteToken` (called on 401 in
  `[slug].tsx:354`) stashes the token with a 30-minute TTL in
  SecureStore (`utils/invitePending.ts`); `AuthRedirect` reads and
  clears it post-sign-in, then redirects to `/invite/{token}`
  (`components/auth/AuthRedirect.tsx:31-50`). The TTL and
  clear-on-resolution behavior are correct guards against the prior
  cross-account leak the file docstring describes.
- **Per-user daily dispatch cap** — verified active. `invite_quota.py`
  gates `(user_id, day_utc)` at default cap 20 (`notification_settings
  .invite_dispatch_daily_cap_default = 20`), with the pre-mint check
  + atomic commit pattern. The fail-open behavior on DB failure is
  consistent with the documented pattern for adjacent counters
  (`chat_token_counters`, `voice_quota_counters`).
- **Conversation-scoped invite gating** — `mint_conversation_invite`
  applies the same quota and `conversation_has_substance` gate
  (`invites.py:444-460`) as the trip variant; `_require_conversation_owner`
  correctly returns 403 (not 404) on a mismatch
  (`invites.py:99-112`). Phase-4 acknowledged gap: conversation
  invites don't log `invite.consumed` to `trip_events` (no such
  table) and don't fire the intake notification — documented at
  `invites.py:748-750, :869-875`, accepted.
- **`is_redeemable` race semantics for multi-use invites** —
  `consume_invite`'s UPDATE WHERE re-evaluates `use_count < max_uses
  AND revoked_at IS NULL AND consumed_at IS NULL` under
  READ COMMITTED, so concurrent accepts either succeed-once /
  raise-once or fall through to the recovery branch
  (`backend/core/db/trip_invites.py:234+`, B12 audit note in the
  docstring); test coverage at `tests/api/test_invites_api.py:768+`.
- **HTML landing page does not expose trip internals pre-auth** —
  `invite_landing.py:128-224` renders only `og_title`, `og_description`,
  `snapshot_text` (Haiku-generated under the trip-snapshot pipeline),
  plus the deep-link CTA. No member names, no constraint content, no
  itinerary. Note: Audit 01 already filed a separate P0 about the
  *snapshot text generation* potentially inheriting PM constraints
  via `invite_snapshot.py`; that finding stays with Audit 01.
- **Universal-Links AASA component shape and Android intent-filter
  config** — verified consistent across `invite_landing.py:301-316`,
  `Travel App/app.json:19-22, :31-47`. Only the Team-ID placeholder
  (P1 above) blocks activation; structure is right.
- **`Travel App/utils/api/http.ts` invite client surface coverage** —
  all four invite endpoints (`viewInvite`, `submitInviteIntake`,
  `acceptInvite`, `revokeTripInvite`) are present in both
  `interface.ts` and `mock.ts`. Mock substance for `viewInvite`,
  `acceptInvite`, `submitInviteIntake` is faithful enough for the
  happy path; the substantive parity gap is the `pending_intake_summary`
  content (P1 above).
