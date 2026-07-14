# Group / Social — System Charter

> Surface: Trips
> Maturity (for MVP): MVP-required
> Status: wired (membership golden-path; social dynamics beta)
> Last updated: 2026-07-13 (coordination-channel ruling added)

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
- **Vote privacy:** group surfaces show tallies and the viewer's own vote, never
  voter names; missing-voter identity is organizer/agent-side only.
- **Quiet propagation:** ordinary group-visible mutations converge on focus/refetch;
  only existing arbiter-gated event classes receive push.
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
