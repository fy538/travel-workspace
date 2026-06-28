# Group / Social — System Charter

> Surface: Trips
> Maturity (for MVP): MVP-required
> Status: wired (membership golden-path; social dynamics beta)
> Last updated: 2026-06-27

## Purpose
The group itself — **membership & invites** (who is in the trip, with what role) and
**social dynamics** (admin style, energy, engagement, fairness) that the concierge
reads to adapt tone and routing. Membership is the foundation everything group-shaped
stands on (privacy routing, booking, expenses, notifications). Serves belief #3
(*the agent never reveals individual constraints to the group*) and #14 (using the
product is the distribution — the invite is "join our trip").

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
