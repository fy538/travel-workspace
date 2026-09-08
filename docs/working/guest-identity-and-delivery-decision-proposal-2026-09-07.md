---
doc_type: working
status: active
decision_status: proposed
owner: founder / invites and occasions / trust / social experience
created: 2026-09-07
last_verified: 2026-09-07
expires: 2026-10-07
why_new: Defines bounded non-account guest access against existing Occasion owners while keeping intended-recipient identity and sensitive delivery unresolved until verified.
supersedes: []
depends_on:
  - social-experience-capability-map-2026-09-07.md
  - ongoing-connection-default-decision-proposal-2026-09-07.md
  - ../journeys/18-signed-out-join-by-invite.md
---

# Decision proposal: a bounded guest without full app adoption

## 1. Status and corrected foundation

**Proposed, not adopted or implemented.** The September 7 cross-check found
canonical `occasions`, `occasion_members` and `occasion_invitations`, plus
creation/response/invitee-read APIs. Core tables date to August 21–22. They use
account identities; their existence does not supply the complete non-account
guest experience.

The earlier proposal incorrectly generalized legacy Trip invitation limitations
to all invitations and proposed a roster as though none existed. Inspect the
canonical Occasion owner first. Reuse token, expiry, landing and delivery
behaviors where appropriate; do not create a competing Occasion or invitation
authority merely to support dinner.

## 2. Desired experience

Sam can understand an invitation, answer, communicate a relevant constraint,
arrive comfortably and receive material deliberately shared with him without
adopting the host's full app workflow. Dana can contribute something helpful
without attending or seeing the private address. Unequal effort remains valid.

A bounded guest is not automatically a full Trip member, a mutual connection,
an audience for all history, or an editor. Prefer one understandable receiving
destination with capability-specific access, not a sequence of account screens.

## 3. Separate capability from identity

| Capability | Proposed experience | Boundary to resolve |
| --- | --- | --- |
| Safe preview | Understand host-authored invitation and non-sensitive practical information without account creation. | Host-approved preview scope and forwardability; private home address and guest list are not public preview defaults. |
| Attributed answer / private constraint | Answer once and optionally tell the host something relevant. | Establish whether the responder is the intended guest; an unverified bearer response cannot be treated as verified Sam. |
| Sensitive arrival information | Receive the exact details legitimately needed to attend. | Possession of a forwarded link or an unverified “yes” is not identity verification. Gate sensitive disclosure using the adopted access mechanism. |
| Arrival line / remote contribution | Send the narrow update or object to the intended people. | Effective contributor identity, audience and own-material correction; attendance and editing rights remain separate. |
| Later photograph or other object | Receive something worthwhile without contributing in return. | Author's delivery/custody scope, intended recipient, expiry and withdrawal; the invite's lifespan does not decide all later rights. |
| Continued contact / account linking | Optional deliberate continuation. | Verified principal and explicit linking; no automatic rebinding, connection or history access. |

The previous “exact address after answering; identity only when Keep/Connect”
rule is withdrawn as a settled recommendation. Compare a recipient-bound
verification step at the first sensitive boundary with any explicitly
authorized bearer-link design. Show the cost and forwarding implications
honestly. No mechanism is adopted by this doc.

## 4. Ownership, revocation and retained value

Invites and canonical Occasion owners govern participation and bounded access;
source authors govern their material; delivery/trust govern recipient assurance.
Life owns eligible record projections, not a second guest identity directory.

Revoking an invitation/access link stops use through that capability. It does
not make the host owner of Maya's private original or erase another person's
independent record. A separately valid author-delivery grant may remain; do not
claim the revoked link can still display it. Account linking must preserve these
separate authorities rather than resurrecting expired access.

A contact supplied by the host is a delivery target, not verified ownership of
that contact. Whether guest principals extend an existing owner or need a narrow
new representation is an engineering decision after owner-path inspection.

## 5. Acceptance cases

1. Safe preview works without adopting the app; sensitive information is not
   disclosed to someone who merely obtained a forwarded preview link.
2. Sam's attributed response/constraint uses the verified or explicitly adopted
   capability policy, without exposing his private line to other guests.
3. Dana contributes a tip without attendance, address access or host re-entry.
4. The day-of page reflects current accepted facts; an unadopted suggestion
   never becomes Sam's changed arrival instruction.
5. Later material has independent author/recipient/expiry checks; viewing does
   not require uploading or connecting in return.
6. Revocation, forwarding, a wrong contact and optional later account linking
   cannot silently widen access or misattribute a participant.

## 6. Open decisions and implementation handoff

Identity assurance by capability; sensitive-address access; later media custody;
guest contributions; cost of verification/delivery; and the supported principal
representation. Inspect current graph, invitation, contribution, Life and trust
owners and their tests first. Extend Journey 18 where suitable rather than
claiming its landing-page coverage proves this whole route. No new runtime
permission, schema, sender or activation follows from this proposal.
