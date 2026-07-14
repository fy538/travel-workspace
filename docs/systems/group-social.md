# Group / Social — System Charter

> Surface: Trips
> Maturity (for MVP): MVP-required
> Status: wired (membership golden-path; social dynamics beta)
> Last updated: 2026-07-14 (chat transport, roster routing, and durable propagation added)

## Purpose
The group itself — **membership & invites** (who is in the trip, with what role) and
**social dynamics** (admin style, energy, engagement, fairness) that the concierge
reads to adapt tone and routing. Membership is the foundation everything group-shaped
stands on (privacy routing, booking, expenses, notifications). Serves belief #3
(*the agent never reveals individual constraints to the group*) and #14 (using the
product is the distribution — the invite is "join our trip").

## Coordination-channel ruling (2026-07-13)

**The pre-cohort strategy is the shared-object path, not chat replacement.** The trip
is the shared social object; the group's existing thread (iMessage/WhatsApp) remains
their talk channel; every decision artifact (invite, proposal, trip page) must preview
beautifully and land deep when pasted into it. The in-app group room's job is **"the
trip's room"** — where Vesper, decisions, and the operational record live — judged
against Partiful's bar, not iMessage's. We do not compete on messaging.

- **Dogfood metric:** links created and pasted out (invite / proposal / trip-page
  shares) and taps back in (link-landing opens → deep-link arrivals). **Not** in-app
  group-message volume — low chat volume is *expected and fine* under this ruling.
- **Chat replacement is a hypothesis the cohort may promote, not a plan.** Promotion
  trigger: observed *organic* member-to-member banter in trip rooms (unprompted
  human-to-human messages, not Vesper-addressed). Until that trigger fires, no
  engineering hours go to messaging table stakes (per-message push, reactions,
  reply-to, in-thread photo sharing, human presence/typing/read receipts).
- **Supersession:** this overrides `travel-agent/docs/product/Strategic
  Implications.md` §14 ("replaces WhatsApp as the trip's communication hub", "move
  their trip conversation into your app") — annotated in place. It is consistent with
  `Growth Strategy.md` §"Don't compete with WhatsApp on messaging" and with this
  charter's existing "Quiet propagation" invariant, which is a deliberate consequence
  of this ruling, not an anti-spam accident.

## Group-decision rulings (2026-07-13)

Four founder rulings on how group decisions should *feel*. The through-line: the
privacy load belongs on the **input layer** (private chat, constraint synthesis,
compose redaction) — which stays sacred — not on the **decision layer**, where
anonymity reads as bureaucracy to a friend group. Constraint privacy ≠ preference
privacy.

1. **Social votes — supersedes the D1 secret ballot.** Names on choices, holdouts
   visible to the group. By the time something is up for a vote, the options were
   already filtered group-safe by the synthesis layer, so a public vote leaks no
   constraints; visible preference among friends is ordinary social life and is
   what creates momentum and peer accountability. A *sensitive* objection belongs
   in the private channel (Ask Vesper), not an anonymous ballot — the vote is the
   public instrument, the private channel is the constraint instrument.
   *Status: implemented* (`proposals.py`'s `_to_detail`/`list_proposals`,
   `users/trips_board.py`, `conversations.py`'s vote_widget rehydration; FE
   avatar-stack vote rows from the 07-06 batches lit up with zero FE-side
   logic changes — purely gated on the now-always-true
   `can_view_individual_votes` field). Per-vote free-text comments are a
   narrower, still-restricted exception: visible only to the comment's own
   author and the organizer — free text can carry more than a preference,
   closer to a private objection than "I approve".
2. **Attribution follows the visibility of the initiating intent.** An ask made in
   front of the group ("hey Vesper, propose swapping Tuesday") is the member's own
   proposal, prepared by Vesper — human credit. An ask made privately stays
   "Vesper proposed" — deliberately, as the diplomacy shield (a private "somewhere
   cheaper tonight" must never leak its asker through attribution). Unknown
   provenance fails private. `proposed_by_agent` now means "autonomous, or
   shielding a private ask." *Status: implemented* (`_propose_present.py`;
   Change-Studio proposals already carried human credit).
3. **Visible care: show the work, never the accommodation.** Constraint-neutral
   diligence (hours checked for the actual day, walking time from the stay,
   cross-checks against saved places) is group-visible by design — discretion
   felt as competence (belief #31). Accommodation visibility ("works for
   everyone") stays banned for cohort 1 — the asymmetry implies someone needed
   accommodating; revisit with real cohort transcripts. *Status: implemented*
   (invisible-scaffolding prompt).
4. **Voting visible by default; automation opt-in.** The old `voting_enabled`
   conflated (a) members expressing an opinion with (b) timers converting silence
   into plan mutations. Split them: visible voting defaults ON for trips with ≥2
   members; consensus automation (deadlines, lazy-consensus auto-apply) defaults
   OFF, organizer opt-in. Explicit-unanimity auto-accept stays (it only fires on
   explicit votes). This honors "membership does not imply a governance
   preference" — that principle was always about automation, never expression.
   *Status: implemented* (`consensus_automation_enabled` column + migration;
   `change_proposals.py`'s deadline sweep/reminder re-keyed to it;
   `trips/members.py::add_trip_member` reinstates auto-enable for visible
   voting only, on the trip's first non-organizer member; `_propose_present.py`
   only sets a proposal deadline when automation is on, so a lazy_consensus/
   active_approval countdown never shows without a sweep to honor it; FE
   trip-settings gets a second toggle for automation, gated on visible voting
   being on first).

## Spans (cross-repo)
- Backend: membership/invites in `core/` + `api/routes/trips.py`, `members`, `invites`; social dynamics in [`travel-agent/backend/social_state/`](../../travel-agent/backend/social_state/FEATURE.md) (6).
- Frontend: `app/trip-begin`, `app/invite/[slug]`, `app/invite-code`, `(tabs)/trips/[tripId]/chat` (group room), `components/trips/*`, `data/trips.ts`, `useCreateInvite`/`useTripInvites` hooks.
- Tables of record: `trips`, `trip_members`, `trip_invites`; `trip_social_state` / synthesized social markdown, `trip_group_profiles` (merged — written by Memory & Preference).

## Public interface (what other systems may call / read)
- **Membership (FE → BE):** create trip; create invite link; `GET /invite/{token}`; accept invite (→ `trip_members` row). Auth-detour safe (token survives sign-in).
- **Membership guards:** `require_trip_member` / `require_trip_organizer` (the row-level access gate every trip-scoped endpoint depends on).
- **Social dynamics:** `social_state/retriever.py::get_social_state()` (read by `concierge/turn_context.py`), `record_interaction()` (reached via `concierge/signal_capture.py`, proposal automation, group interjection), `genesis.py` (cold-start doc at trip creation).
- **Never:** non-members must not read trip data; invite links must not expose private member data.

## Owns (source of truth)
Trip membership, invite tokens, and social-state signals. (The merged `trip_group_profiles`
is owned by [Memory & Preference](memory-preference.md); this system supplies the social-dynamics layer.)

## Invariants (must always be true)
*(Membership invariants are journey 02's "Must Never Happen", inverted.)*
- **Invite → exactly one trip:** a token maps to one trip; accept lands in the *correct* workspace.
- **Auth detour preserves the token** — sign-in mid-invite never loses context.
- **Consumed/expired invites render as such** — never as active.
- **No pre-accept leakage:** non-members can't see private trip data before accepting.
- **No fake success:** a failed invite-create never shows success.
- **Membership coherence:** Trips list, Trip Info, Group Chat, and Notifications agree on who's in.
- **Social state is rebuilt from signals**, not stored as a static doc; extraction is Haiku.
- **Fairness:** equity-imbalance signals feed the concierge (vote-absence friction, quiet-member detection).
- **Vote privacy (superseded 2026-07-13 by group-decision ruling 1, above):**
  vote choice + identity — names on choices, holdouts — is group-visible to
  every trip member. Per-vote free-text comments remain restricted to the
  comment's own author and the organizer. (Was: group surfaces show tallies
  and the viewer's own vote, never voter names; missing-voter identity was
  organizer/agent-side only — the old D1 rule this replaces.)
- **Quiet propagation:** ordinary group-visible mutations converge on focus/refetch;
  only existing arbiter-gated event classes receive push.
- **Human delivery is independent of AI participation:** ordinary reactive-room
  messages use an idempotent non-streaming write, consume no concierge-turn quota,
  and render no Vesper placeholder. Explicit Vesper address and opted-in proactive
  candidates alone enter the AI participation transport.
- **Committed chat history cannot depend on one Redis publish:** human-message and
  Vesper-message lifecycle writes enqueue an identifier-only propagation event in
  the same Postgres transaction. Successful publish acknowledges it; a periodic
  repair sweep retries missed signals. The client poll remains the final fallback.
- **Shared-room routing fails closed on roster uncertainty:** group-chat hooks mount
  only after an authoritative roster verifies at least two members. A verified solo
  roster redirects privately; an unavailable or empty roster exposes retry without
  creating or subscribing to the shared room.
- **Wiki-mode V1:** committed plan state is shared immediately; curator/selective
  draft propagation is deferred.
- **Organizer authority is explicit:** the organizer resolves proposals in V1;
  unanimous yes among at least two voters may auto-accept, with no timeout automation.
- **Membership dignity:** join gets a group line and organizer notice; leave is a
  quiet line; removal and role change update the roster without group announcement.
- **Room mute honesty:** any member may mute Vesper for the room, but the change
  requires an unattributed group line plus organizer-visible who/when audit data.

## Failure modes
- Stale social state → background re-synthesis on staleness threshold; last good doc served meanwhile.
- Invite/membership write failure → surfaces loudly (never silent success).

## Maturity & validation
- Serves journeys: 02 (create + invite — already a reliability golden path), 04 (group-safe routing), 05 (role gates edit-mode).
- DoD state: offline golden-path + invite hooks tests ✅ (`useCreateInvite`, `useTripInvites`, `invite-landing.smoke`) · **screen-level mock walk-through ❌ · live two-account invite walk ❌**.

## Canonical docs
- why → `product/Interaction Design and Social Dynamics.md` · how → `working/Group Interjection Sync Design.md` · what(be) → `backend/social_state/FEATURE.md` · what(fe) → `page-specs/trip-group-chat.md` · `trip-page.md`.
- Tests: `__tests__/offline/goldenPath.test.ts`, `__tests__/hooks/useCreateInvite.test.ts`, `__tests__/screens/invite-landing.smoke.test.tsx`.

## Open risks / known gaps
- Invite flows are "easy to break with auth detours, stale tokens, and current-user assumptions" — the **stale `currentTripId`** assumption is the classic failure (sends an invitee to the wrong workspace). Trace it explicitly.
- This is the only MVP-required system needing a genuine **two-account, two-device** live walk (everything else can be walked solo).
- Remaining propagation backlog is honest-but-quiet rather than a privacy blocker:
  vote history, direct-edit receipts, stay decision events, booking path symmetry,
  mark-booked chat bridge, trip-genesis audit, room-mute audit, and pin idempotency.
  Extend the second-observer certifier as each lands.
