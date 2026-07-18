---
doc_type: working
status: active
owner: engineering
created: 2026-07-18
last_verified: 2026-07-18
expires: 2026-08-17
why_new: Records the Wave 6 signed-out projection privacy cutover and its verification evidence.
supersedes: []
source_of_truth_for: [wave-6-public-projection-parity]
---

# Wave 6 Public Projection Parity — 2026-07-18

Wave 6 hardened the four canonical signed-out projection paths: Story, Invite,
Proposal, and Unpacked. The implementation now has one default-deny registry
that freezes allowed/prohibited categories, actor controls, runtime posture,
expiry, and stale behavior.

Invite was the material privacy cutover. Its public JSON no longer exposes trip
or conversation IDs, companion counts, or full organizer display names. The
snapshot generator no longer reads trip briefs or itinerary block titles; it
uses only trip title, destination, dates, and inviter first name. Cached invite
copy was bumped to privacy version 3. The app no longer renders companion-count
UI or a date-derived pseudo-itinerary, and an authenticated recovery endpoint
now handles already-accepted links without public IDs.

Story shares now support actor-selected photo exclusion and an explicit
per-share expiry. Rotation preserves that expiry. Unpacked shares now persist
the actor-selected recap card kinds and optional expiry in the durable share
row; both HTML and preview-image rendering read the same controls after an
authoritative revocation/expiry check. Proposal remains a generic authenticated
handoff and deliberately resolves no proposal data until a durable revocable
public proposal projection exists.

All four HTML surfaces use the same non-diagnostic unavailable copy. Public
preview cards use the same cache policy and carry neutral `og:image:alt`
metadata. Unknown, expired, revoked, and exhausted states therefore do not act
as existence or lifecycle oracles for signed-out viewers.

Verification:

- 215 backend projection, Invite, Story, Unpacked, and registry tests passed.
- 39 app Invite screen and journey tests passed.
- Regenerated `docs/openapi.json`, `docs/openapi.app.json`, and app API types.
- TypeScript `tsc --noEmit` passed.
- Ruff lint passed; Alembic reports one head: `wave6unpacked01`.

Deployment requires applying the `wave6unpacked01` migration before enabling
new Unpacked share creation against the updated runtime.
