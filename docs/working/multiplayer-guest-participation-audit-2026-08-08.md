---
doc_type: working
status: active
owner: founder / engineering
created: 2026-08-08
updated: 2026-08-08
why_new: Record the low-friction guest-participation audit before adding a new capability-link mutation path.
expires: 2026-09-07
---

# Multiplayer guest participation audit

## Finding

The RSVP side of the low-friction guest experience already exists as a scoped,
expiring capability link. The proposal side does not, by design: proposal
details and votes are member-private and all votes enter the canonical
itinerary-proposal gateway. These are two different authorization surfaces and
should not be collapsed into one bearer-token mutation endpoint.

## Existing guest path (implemented)

Trip invite tokens are the current capability links:

- tokens are time-bounded, revocable, and bounded by `max_uses`;
- the public projection can show a safe trip/invite snapshot without exposing
  member IDs, raw private answers, or internal identifiers;
- a signed-out recipient can submit bounded chip/free-text intake before
  account creation;
- shared local Plans can collect only the closed RSVP vocabulary (`in`,
  `maybe`, `out`), with aggregate counts shown to the organizer;
- a recipient can authenticate and accept the same invite, optionally claim
  their matching anonymous intake, and become a trip member without losing
  attribution;
- attendance prompts created from an invite are answered through the canonical
  itinerary operation writer and return an action receipt;
- retries are idempotent and expired/revoked/terminal-trip links fail closed.

The raw free-text answer remains owner-scoped invite state. The append-only
trip journal stores only a digest (presence/length and the closed RSVP value),
not the answer itself.

## Existing proposal path (implemented)

`GET /p/{trip_id}/{proposal_id}` is a generic authentication handoff. The raw
IDs are navigation coordinates only; the public route never resolves the
private proposal and renders no title, description, status, or vote tally.
After authentication, the app opens the member-gated proposal route.

Authenticated proposal voting already has the important mutation protections:

- trip-membership and eligible-voter checks;
- self-vote prevention;
- canonical operation-proposal gateway writes;
- same-vote idempotent replay;
- resolved-proposal conflict handling;
- aggregate-only public copy on the handoff/card surface.

## Deliberate gap

There is no proposal-specific capability link that lets a signed-out person
vote, provide one private constraint, or receive a decision receipt. Adding a
public `POST` that writes directly to `change_proposals.votes` would bypass
the member foreign-key/eligibility model, receipt provenance, and the existing
canonical mutation path.

The next implementation slice must therefore introduce a separate,
purpose-bound capability record (token hash, proposal/trip scope, expiry,
revocation, redemption state, and idempotency) plus an explicit post-auth
claim/upgrade flow. A guest vote must either become an authenticated member
before entering the canonical vote gateway or be represented by a first-class
guest participant model with equivalent authorization, attribution, and
receipt semantics. Until that design is implemented and device-tested, the
proposal handoff remains authentication-only.

## Evidence

- `tests/api/test_invites_api.py` and `tests/api/test_invite_landing.py` cover
  pre-auth intake, closed RSVP vocabulary, aggregate-only rendering, and
  public projection hygiene.
- `tests/core/test_trip_invites_bounds.py`,
  `tests/core/test_trip_invites_lifecycle_gate.py`, and
  `tests/core/test_trip_invites_redemptions.py` cover expiry, revocation,
  bounds, retry, and redemption behavior.
- `tests/api/test_proposal_landing.py` and
  `tests/api/test_public_projection_shapes.py` cover the generic proposal
  handoff and its no-private-data guarantee.
- `tests/api/test_proposals_api.py` and
  `tests/core/test_itinerary_proposal_gateway.py` cover member-gated,
  idempotent canonical voting.

## Exit decision for this sequence step

Guest RSVP is sufficiently implemented to carry forward. Guest proposal
voting is an explicit follow-on slice; it is not certified or implied by the
existing public handoff. No new guest mutation endpoint is shipped in this
audit commit.
