---
doc_type: working
status: active
owner: founder / product / engineering
created: 2026-08-23
last_verified: 2026-08-23
expires: 2026-09-22
why_new: Defines the final signed-in two-account evidence required before enabling the M3 UUID relationship handoff flag.
supersedes: []
promotes_to: null
source_of_truth_for: [m3-signed-in-two-account-device-cert]
---

# M3 signed-in two-account device certification

This is the release gate for the first addressed-place multiplayer loop. The
mock/device Maestro flow is necessary UI evidence, but it is not evidence that
two real accounts can cross the backend authority boundary. This runbook must
be executed against a dogfood deployment before the serving flag is enabled for
any cohort.

## Preconditions

- two physical devices (or two device-tier simulators with independent
  sessions) and two real Clerk identities;
- `USE_MOCK=false` and `EXPO_PUBLIC_SKIP_AUTH=false` in the app build;
- the backend is serving the current OpenAPI contract and Alembic head
  `xgraph17_identity_binding_null_uniqueness` or later;
- `RELATIONSHIP_UUID_HANDOFFS_ENABLED=true` only for the named dogfood cohort;
- one reviewed, active graph binding for the canonical venue used in the walk;
- one confirmed pair Circle containing the two identities; and
- a stable venue detail deep link and a stable pair conversation deep link.

The pair Circle is the audience authority. Do not use a follow, shared Trip,
co-location, or an arbitrary recipient UUID as a substitute.

## Walk

### A. Sender — canonical Place detail

1. Sign in as the sender on Device A and open the canonical venue detail.
2. Confirm `venue-relationship-handoff` is present only because the account has
   a confirmed pair Circle.
3. Tap **Leave this place for someone**, choose the intended pair member, and
   submit a short source-bound note.
4. Record the addressed message id, handoff id, canonical `EntityRef`, and the
   action receipt from the API. Do not record source bytes or bearer tokens.
5. Refresh the venue and the pair conversation. The note must remain one
   durable handoff, not a second local draft.

### B. Recipient — private Chat card and shared Occasion

1. Sign in as the recipient on Device B and open the same pair conversation.
2. Verify the private card names the place and note but contains no sender
   source-object id, graph-local UUID, or private source payload.
3. Tap **Open together** once. A second tap/retry must not create another
   Occasion. Record the returned `occasion_id` and receipt.
4. Refresh Home/Places/Chat. Both participants must see the same authorized
   shared Occasion, and neither participant may see an unrelated Trip link.

### C. Plural private Outcomes

1. Each participant records a different private Outcome after the Occasion is
   lived.
2. Switch accounts and verify each Outcome is visible only to its owner.
3. Correct one Outcome with its current revision. The owner sees the new
   revision; the other participant still sees the shared Occasion but not the
   private meaning.
4. Replay the correction with the stale revision. The API must reject it
   without changing either Outcome or the shared Occasion.

### D. Negative and recovery checks

- sender revocation removes the recipient's available card and leaves no
  actionable stale payload;
- a non-member cannot read the handoff, open the Occasion, or inspect either
  private Outcome;
- retrying the same create/open/correction idempotency key returns the original
  receipt rather than a second mutation; and
- disabling `RELATIONSHIP_UUID_HANDOFFS_ENABLED` makes the namespace
  unavailable without affecting legacy place readers or existing Trips.

## Evidence packet

Attach one redacted receipt containing:

- app build identifier and backend deploy digest;
- Alembic revision and OpenAPI snapshot hash;
- the two device descriptors and anonymized account labels;
- canonical venue `EntityRef` and handoff/Occasion/Outcome receipt ids;
- timestamps for sender, recipient, opening, each Outcome, correction, and
  negative-oracle checks; and
- screenshots or Maestro artifacts for sender, recipient, shared Occasion,
  owner-only Outcome, correction, and sender/recipient privacy boundaries.

The receipt must not contain source text beyond the intentionally synthetic
canary note, bearer tokens, Clerk identifiers, raw graph UUIDs, or private
Outcome meaning from the other participant.

## Current state

The sender doorway now exists on both graph summaries and canonical venue
detail. Backend persistence and mock/device evidence are green. This packet is
still **pending human execution** because the current session has no two real
dogfood identities, a production serving flag, or two independent signed-in
devices. Until the packet is attached, keep the flag off outside the named
local/demo environment.
