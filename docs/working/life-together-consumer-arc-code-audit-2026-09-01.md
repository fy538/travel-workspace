---
doc_type: working
status: active
owner: engineering (Claude Code) / founder review
created: 2026-08-31
last_verified: 2026-08-31
expires: 2026-09-30
why_new: Workstream A ("Together as a complete consumer experience") requires a
  code audit of what the current backend and mobile app can and cannot represent
  against the Life social-lifecycle fixture matrix before the design prototype
  commits to behavior the substrate cannot honor. Audit only — no migration, no
  refactor, no noun changes.
promotes_to: null
supersedes: []
source_of_truth_for: []
depends_on:
  - docs/systems/contribution-and-consequence.md
  - docs/working/life-social-lifecycle-fixture-matrix-2026-08-29.md
  - docs/working/life-next-behavior-prototype-handoff-2026-08-31.md
---

# Life "Together" Consumer Arc — Code Audit

Repositories audited (all paths below are absolute):

- Backend: `/Users/feihuyan/travel-workspace/travel-agent/backend`
- Mobile: `/Users/feihuyan/travel-workspace/travel-app`

Evidence labels used throughout: **CODE-EVIDENCED** (file:line), **DOCUMENTED
TARGET** (contract/fixture language, no code), **ABSENT** (searched, not
found; searches named). Read capability and durable authority are recorded
separately. Status vocabulary follows the handoff §3 ladder; nothing here is
"done."

---

## 0. Executive summary

### What exists

1. **The five authority axes exist as a storage-neutral contract** —
   `ContributionAxes` composes independent Use / Retention / Inference /
   Audience / Action sub-models with cross-axis validators
   (`backend/core/models/contribution.py:211-216`, treatment coherence at
   `:295-312`). CODE-EVIDENCED. Status: **Architecture resolved**. It is a
   turn-time decision shape only: `resolve_contribution`
   (`backend/core/contribution_policy.py:134`) has exactly one caller, inside
   the agentic facade compiler
   (`backend/concierge/agentic_facade/compiler.py:287`), reachable only when
   `agentic_facade_mode == "shadow"` — and the default is `"off"`
   (`backend/concierge/config.py:172-175`). **No production write path is
   gated by it.**

2. **A viewer-relative "together" projection contract exists and is
   deliberately fused shut.** `CanonicalArtifactProjectionV1` carries
   `scope.mode: mine|together`, `viewer_role`, per-fact and per-media
   `audience` (`backend/core/models/canonical_artifact.py:33-37,85,92`), and
   the pure compiler filters shared facts to an explicit
   `shared_fact_keys` allowlist ("a shared Occasion alone is not that grant,"
   `backend/core/canonical_artifact_projection.py:427-431`). But the only
   transport rejects `mode=together` with HTTP 403: "Together projections
   require graph-owned sharing authorization"
   (`backend/api/routes/artifact_projections.py:51-55`). Status:
   **Projection modules composed**; the sharing authority it waits for is
   ABSENT.

3. **Two genuinely read-time, fail-closed grant systems exist — both for
   location/presence only.** Directional relationship-visibility grants with
   `granted_at`/`revoked_at`/`revision` and read-time mutuality
   (`backend/core/models/relationship_visibility.py:19-28`,
   `backend/core/db/relationship_visibility.py:167-231`) and trip location
   sharing with read-time mode resolution and coarsening
   (`backend/core/db/trips/members.py:361-385`). These are the correct
   substrate pattern (revoke-and-re-grant, never a toggle over a live grant).

4. **The experience graph already separates shared occurrence from private
   Outcome.** Durable `occasions` / `occasion_members` /
   `occasion_invitations` (pending/accepted/declined/deferred/expired/revoked)
   and `personal_outcomes` with `owner_id` and `visibility IN
   ('private','shared')`
   (`backend/domains/experience_graph/schema.py:329-351,353-378,380-404,720-763`).
   Plural Outcomes are structurally supported.

### What's missing (the load-bearing absences)

1. **No durable grant object anywhere.** Of the fixture matrix §3's thirteen
   grant fields, nine have **zero occurrences in the backend** (custodian,
   plural subjects, epoch, reshare, post-membership, posthumous,
   revocation-scope, dependency-lineage as fields; grant-level author), and
   the three present ones (audience, purpose, weak validity) exist only in
   the unpersisted `ContributionAxes` contract (§1.11 census). Shared trip
   content is governed by membership plus, at best, a 2-3 value visibility
   flag. The only durable sharing grants are two location tables and one
   billing-entitlement table.
2. **No block / no-contact / relationship-safety overlay at all** — backend or
   mobile (§6). Transitions S08/S10 cannot be represented today.
3. **No membership epochs, no historical audience.** `trip_members` rows are
   hard-deleted on departure (`backend/core/db/trips/members.py:818-822`);
   nothing can distinguish "was a member when this was shared" from "never
   was." S04-A (compact historical access) is unimplementable as stored.
4. **No revocation bus.** Exactly one deletion path fully fans out (Atlas
   artifact cascade). Trip-photo withdrawal — the closest analogue to Maya
   withdrawing `SRC-L02-M2` — is a single `deleted_at` UPDATE with zero
   downstream calls (§4).
5. **Memory synthesis still launders**: the `observe()` prompt mandates
   same-turn preference/personality/mood/silence writes, the tool has a live
   cross-user write hole, observations carry no author column, and group trip
   digests feed individual Personal Memory narrative (§7).

### Top feasibility risks that should change the design

1. **R1 — Withdrawal cannot be demonstrated honestly on the current
   substrate.** The design prototype's S05 moment ("every dependent projection
   reconciles") has no backend counterpart: occurrence-reconciliation evidence
   is append-only with no retraction API
   (`backend/core/db/occurrence_reconciliation.py` — only `record_*`
   functions), chat history has no redaction primitive
   (`backend/concierge/persistence.py`), and mobile image/query caches are
   never cleared on revocation. The fixture contract in §8 should therefore be
   the design's source of truth, and any wired demo must scope withdrawal to
   surfaces that recompute at read (canonical projections, Atlas boards).
2. **R2 — "Shared with Maya" has no addressable unit.** Person-to-person
   addressed contribution (F3/L05) has no model: audience recipients exist
   only in the in-flight `ContributionAudience` (`contribution.py:174-189`),
   never on a durable row. The nearest durable precedent is the place-handoff
   flow (revocable, cross-root — `backend/core/db/place_handoffs.py:579-663`),
   which is single-purpose. Design should assume the grant record in §8 is
   new construction, not a projection over something that exists.
3. **R3 — Block/unblock (S08/S10) is greenfield.** There is nothing to
   suppress with and nothing that unblock could accidentally restore — but
   also no overlay layer for the return-policy precedence stack (fixture
   matrix §7). The good news: the existing grant substrate's
   revoke-and-re-grant semantics mean the S10 invariant ("unblock restores no
   grant") is the natural shape of the codebase, not a fight against it.
4. **R4 — Historical epochs contradict the current hard-delete posture.**
   S04-A requires keeping what today is deliberately destroyed in one
   transaction (conversation participation, membership rows, notification
   state). Adopting epochs is a schema-level decision, not a read-model
   patch.
5. **R5 — Personal Memory is a single narrative document rendered into both
   1:1 and group contexts** (`backend/concierge/refresh_memory.py:408-415`),
   with audience enforced by LLM instruction rather than structural exclusion.
   Any Together design that lets shared evidence near Personal Memory
   inherits this laundering surface until migration step §13.5-6 of the
   contract lands.

---

## 1. Model inventory

For each concept: where it lives, what exists, what's missing vs the fixture
matrix grant model.

### 1.1 Person

- Durable: `users` table (`backend/core/db/_tables/users.py:42`); graph-local
  `users` (`backend/domains/experience_graph/schema.py:48-56`: auth_subject,
  email, display_name).
- API read model: `UserMeResponse`
  (`backend/core/models/users.py:32-64`) — identity plus taste projection
  (`taste_dna`, `interests`), `followers_see_stories: bool`,
  `public_profile_enabled: bool` (two account-level audience booleans).
- Personal Memory: `personal_memories` table
  (`backend/core/db/_tables/memory.py:44-54`) — versioned markdown narrative,
  `signal_count`, `taste_dimensions`. No audience column; see §7.

### 1.2 Relationship

- `follows`: bare directional edge — follower_id, followed_id, created_at
  (`backend/core/db/_tables/social.py:47-53`). Unfollow is a hard row delete
  (`backend/core/db/follows.py:56-58`). No state machine.
- `relationship_visibility_grants`
  (`backend/core/db/_tables/social.py:68-91`; model
  `backend/core/models/relationship_visibility.py:19-28`): grantor, grantee,
  granularity `none|coarse|precise`, granted_at, revoked_at, revision.
  Directional, self-managed, fail-closed at read
  (`backend/core/db/relationship_visibility.py:167-180`), mutuality derived
  at read time, never stored (`:183-227`). **The one real precision concept
  in the codebase.**
- `SocialCircle` / `SocialCircleMember`
  (`backend/core/models/social_circles.py:32-58`): kind pair/group/household,
  member status `invited|active|declined|left` with `left_at`,
  `source_trip_id`. Membership states exist; epochs do not.
- `RelationshipMemoryClaim`
  (`backend/core/models/relationship_memory.py:23-48`; table
  `core/db/_tables/relationship_memory.py:21-95`): the most governed claim
  shape in the codebase — subject_user_id, scope kind
  (personal/circle/trip_roster), claim_type, source_type/source_id,
  supersedes_claim_id, visibility `private|circle`, state
  `active|superseded|retracted`, confidence, evidence_refs. Promotion to
  shared requires an explicit member action
  (`ShareRelationshipMemoryClaimRequest`, `:17-20`).
- Relationship handoffs domain (own MetaData,
  `backend/domains/relationships/schema.py`): `relationship_handoffs`
  (`:26-87`) with sender/recipient, `permissions` JSONB, status
  `available|kept|dismissed|revoked|expired`, expiry, revision; append-only
  `relationship_handoff_events` (`:96-114`); boolean
  `relationship_place_pull_grants` keyed (recipient, sender) (`:149-170`).
  The one durable person-to-person addressed-contribution precedent — single
  purpose (place handoff), but it carries a permission envelope, revocation,
  and an event ledger.
- ABSENT: any relationship-state model (friend/estranged/blocked), any
  relationship epoch.

### 1.3 Occasion

- New graph, durable: `occasions`
  (`backend/domains/experience_graph/schema.py:329-351`) — created_by, kind,
  lifecycle `opening|planned|active|lived|closed|unknown`, purpose,
  lived_at/closed_at, revision. Contract twin: `Occasion`
  (`backend/core/models/experience_graph.py:201-214`).
- Read-model capsule: `OccasionCapsule`
  (`backend/core/models/plan_topology.py:201-226`) with `visibility:
  private|participants|shared` and `authority: "compiled_read_model"` —
  explicitly a compiled projection, not persistence.
- Legacy: most production "occasion" behavior is still Trip-based — the
  17-table `trips`/`trip_members`/`trip_invites` stack, plus an `occasion`
  Text column on `trips` itself (`core/db/_tables/trips.py:62`).
  `domains/experience_graph/trip_adapter.py` exists specifically to project
  Trips into the graph model. Note the structural split: the experience-graph
  and relationships domains each declare their **own SQLAlchemy MetaData**
  separate from the main registry (`domains/experience_graph/schema.py`,
  `domains/relationships/schema.py:22` vs `core/db/_tables/_meta.py`). The
  graph model — with lifecycles, revisions, soft-leave members, and full RSVP
  vocabulary — is the better substrate for Together; the Trip stack is the
  one production uses.

### 1.4 Invitation

- Occasion lane: `occasion_invitations`
  (`backend/domains/experience_graph/schema.py:380-404`) — inviter_id,
  invitee_id, message, status constrained to
  `pending|accepted|declined|deferred|expired|revoked` (`:400`), revision,
  expires_at, not-self check; response validation at
  `domains/experience_graph/commands.py:1075-1148`. This matches the fixture
  matrix S02/S03 state vocabulary exactly. CODE-EVIDENCED.
- Trip lane: `TripInvite` (`backend/core/models/trip_invites.py:77-135`;
  table `core/db/_tables/trips.py:522-669`) — token-PK link invite:
  created_by, target_user_id, contact channel, max_uses/use_count,
  expires_at, revoked_at, consumed_by/consumed_at, snapshot fields.
  **ABSENT: no status column** — pending/accepted/declined/deferred does not
  exist on trip invites; state is inferred from
  revoked_at/consumed_at/use_count. The RSVP-adjacent axis is separate:
  `ParticipationStatus = in|maybe|out` (`trip_invites.py:68`).
- Third shape: `social_circle_members.status = invited|active|declined|left`
  (`core/db/_tables/social_circles.py:66-131`) — no `deferred`.
- Being invited ≠ participating is honored: membership and invitation are
  separate rows in both graph lanes.

### 1.5 Participant / membership

- `occasion_members` (`backend/domains/experience_graph/schema.py:353-378`):
  status CHECK `('active','left')` with `left_at`, role, visibility (default
  `participant`), window JSONB, revision, joined_at — a soft-leave model,
  unlike trips. But `UniqueConstraint(occasion_id, user_id)` (`:373`) means a
  rejoin reuses the same logical slot: no membership history.
- `trip_members` (`core/db/_tables/trips.py:198-221`,
  `UniqueConstraint(trip_id, user_id)` at `:216`): current-membership only;
  departure **hard-deletes the row** inside a cascade that also deletes
  conversation participation, notification state, proposal votes, and bearer
  share links (`backend/core/db/trips/members.py:672-892`, delete at
  `:818-822`).
- `conversation_membership_events`
  (`core/db/_tables/conversations.py:280-304`): **append-only**
  join/leave/removed ledger — "a prior invite redemption cannot silently
  resurrect someone who chose to leave" (`:277-279`). The one durable
  severance receipt in the system, and the natural precedent for epochs.
- **Epoch: ABSENT as a durable record.** The concept exists three times, all
  read-side: the departure comment "Social signals belong to one current
  membership epoch" (`core/db/trips/members.py:859-861`); a structural
  `MembershipEpoch(Protocol)` over `trip_members` rows used for content-free
  context fingerprints (`core/context_compiler/provenance.py:20-31`); and
  `membership_join_outbox.py:33`, which uses `trip_members.id` as
  `membership_epoch_id` — an id that does not survive leave/rejoin because
  the row is deleted. No `epoch` column or `membership_epochs` table exists
  anywhere (grep over backend + alembic's 454 revisions).

### 1.6 Audience

No single audience system; three mechanisms (full read-path analysis in §2):

- Per-item stored flags, re-read each request: trip photos
  `private|group|group_and_learn`
  (`backend/core/models/trip_photos.py:11,21`), accommodations
  `group|private` (`trip_accommodations.py:40`), personal_outcomes
  `private|shared` (schema `:754`), observations `shared: bool`
  (`backend/core/db/_tables/memory.py:380`), entity saves
  `share_with_friends: bool` (`backend/core/db/_tables/social.py:255`),
  story shares `visibility` + `redaction_policy`
  (`backend/core/db/trip_story_shares.py:186,328`).
- Directional per-person grants: relationship visibility and trip location
  sharing only (§1.2).
- Membership-only: everything else trip-scoped — 252 call sites of
  `require_trip_member` (`backend/api/auth.py:224-238`).
- Surface-local audience literals, mutually incompatible: `AdmissionAudience
  = personal|group|public` (`core/models/admission.py:30`),
  `EditorialMapAudience = trip_group|private_user|public_redacted`
  (`core/models/editorial_map.py:18`), `PendingChatTurnAudience =
  personal|group` (`core/models/pending_chat_turns.py:20`), receipt
  `visibility = private|group|public|system`
  (`core/db/_tables/action_receipts.py:74`) — at least nine audience
  representations exist, none shared.
- In-flight only: `ContributionAudience` with mode
  `private|named_people|occasion|public` and `recipient_ids`
  (`backend/core/models/contribution.py:97-101,174-189`) — the only
  representation combining an enum, a recipient list, and an occasion scope.
  **Named-recipient audience exists nowhere durably.**

### 1.7 Grant

- In-flight: `ContributionAxes` / `ContributionDecision` /
  `ContributionReceipt` (`backend/core/models/contribution.py:211-216,
  283-312,315-324`). Storage-neutral, frozen, validator-enforced. Not
  persisted; not consulted by any live writer (§0.1).
- Durable grants that exist: `relationship_visibility_grants` (location),
  `trip_member_location_sharing` (location), place handoffs
  (`backend/core/db/place_handoffs.py` — status ladder with REVOKED,
  recipient-side withdrawal of proposed occasions `:645-657`), story shares
  (revocable slugs, `backend/core/db/trip_story_shares.py:198-243`).
- ABSENT: any durable contribution-use grant on shared content.

### 1.8 Source

- Intake v2: `IntakeSourceObject` / `IntakeSubmission`
  (`backend/core/models/intake.py:123-171`) — custody_verified_at,
  custody_receipt_sha256, custody_status, retention_mode (default
  `ephemeral_processing`), retention_expires_at. Custody and retention are
  real here. CODE-EVIDENCED.
- Graph: `source_objects` (`backend/domains/experience_graph/schema.py:89-104`)
  — owner_id, source_kind, content_hash, payload_ref, `privacy` (default
  `private`), metadata.
- ABSENT on both: audience beyond owner, purpose, reshare, dependency
  lineage pointers (lineage lives, partially, on consumers — §4).

### 1.9 Receipt

- Persisted: `vesper_action_receipts`
  (`backend/core/db/_tables/action_receipts.py:18-90`) — visibility
  `private|group|public|system`, status `active|superseded|revoked|errored`,
  undo refs; model `ActionReceiptRow` / `SerializedActionReceipt` with
  `SourceRef.degraded` ("Set when the referenced source has been deleted or
  revoked", `backend/core/models/action_receipts.py:37-45,50+`) and the
  `PublicReason` / `PrivateInfluence` split where the private value can never
  be stored, only a safe label (`:14-34`). Deletion-aware receipts exist. A
  separate graph-side `experience_action_receipts` table exists
  (`domains/experience_graph/schema.py:786`).
- Transient/piggybacked: `AttentionReceipt` is written into
  `proactive_events` rows (`core/db/proactive_events.py:30-49`), and
  `WorkReceipt` is flattened into chat-message metadata
  (`concierge/structured_messages.py:963-1001`) — neither has its own table.
- Contribution receipts (invalidated_projection_refs, audience_effects,
  undo_available) exist only in the storage-neutral contract
  (`backend/core/models/contribution.py:315-324`).

### 1.10 Block state

**ABSENT** — backend and mobile. See §6 for searches and the adjacent
mechanisms that are *not* blocks.

### 1.11 Grant-field census vs fixture matrix §3

| Fixture §3 field | Current state | Evidence |
| --- | --- | --- |
| author | PARTIAL — `uploaded_by_user_id` on photos (`trip_photos.py:20`); `edited_by` per shared-memory *version*, not per item (`trip_shared_memories.py:44`); **no author column on observations** (`_tables/memory.py:359-388`); no grant-level author (`ContributionScope.actor_id` is in-memory, `contribution.py:220`) | CODE-EVIDENCED |
| data subjects | ABSENT as a plural field anywhere; singular analogues only (`relationship_memory_claims.subject_user_id`, `_tables/relationship_memory.py:26`) | |
| custodian | ABSENT — grep `custodian` across backend: **zero hits**; custody exists as *status* on sources (§1.8), never as a named party; `occasions.created_by` is the nearest proxy | |
| audience | PARTIAL — flags/enums (§1.6); named recipients in-flight only | |
| purpose | ABSENT durably; `ContributionUse.purposes` in-flight (`contribution.py:118-129`); photo `group_and_learn` is the one purpose-bearing stored value | |
| precision (incl. Place) | PARTIAL — `none|coarse|precise` for location grants (`relationship_visibility.py:16`), read-time blur (`members.py:385`), `geometry_precision` on world entities (schema `:70`); **no precision on any shared-content grant** | |
| membership/relationship epoch | ABSENT durably — read-side Protocol + row-id token only (§1.5) | |
| validity interval | PARTIAL — granted_at/revoked_at on the two location-grant tables; expires_at on invites, observations, takes; `ContributionDecision.expires_at` (`contribution.py:293`) is never written anywhere. The only grant in the codebase with an event ledger, policy version, and validity window is `commercial_benefit_grants` (`_tables/commercial_access.py:123-186`) — billing, not sharing | |
| reshare / managed export | ABSENT — grep `reshare`: **zero hits** (story-share slugs are revocable but reshare rights are not modeled) | |
| post-membership behavior | ABSENT — grep `post_membership`: **zero hits**; hard-delete means the only behavior is S04-B-always (`members.py:818-822`) | |
| posthumous directive | ABSENT — grep `posthumous`: **zero hits** | |
| revocation owner + scope | PARTIAL — every revocation in the system is a flat timestamp or status flip (`revoked_at` + `granularity='none'` on visibility grants, `social.py:83-87`; `intake_source_objects.revoked_at`/`revocation_reason`, `_tables/intake_v2.py:113-114`; handoff `status='revoked'`); grep `revocation_scope`: **zero hits** — nothing records what a revocation reaches | |
| dependency lineage | PARTIAL — `atlas_derived_signals`, `SourceRef.degraded`, `dependency_manifest` on decisions (`_tables/memory.py:94`), V0 `source_artifact_*` columns Atlas-only with "~20 call sites will be migrated" (`backend/core/db/atlas.py:1276-1279`); grep `dependency_lineage`: **zero hits** as a field | |

---

## 2. Viewer-relative read paths

Which read models evaluate the viewer at read time vs bake audience at write
time. (Classification below is CODE-EVIDENCED at the cited lines.)

### Viewer-evaluated at read (fail-closed)

| Path | Evidence |
| --- | --- |
| Relationship-visibility mutuality — "Nothing stores a symmetric 'friend' flag, so either party's revocation takes effect on the very next read" | `backend/core/db/relationship_visibility.py:183-227` |
| Location disclosure — mode resolved against grant, revoked_at, expires_at, trip-terminal state per read; blur applied centrally | `backend/core/db/trips/members.py:361-385` |
| Story-share access — viewer access `open|members_only|unavailable` computed per read, member check at `:77`; photo allowlist re-derived per read so flipping a photo private retroactively removes it from a published story; revocation also deletes the `story_published` feed event | `backend/core/db/trip_story_shares.py:60-78,714-752,198-243` |
| Trip photo list — `(uploader == viewer) OR visibility IN ('group','group_and_learn')` | `backend/api/routes/trip_photos.py:449-450` |
| Public profile — target's `public_profile_enabled` checked per read | `backend/api/routes/profiles.py:92-94` |
| Canonical artifact projection — compiled per viewer; together-mode fact allowlist | `backend/core/canonical_artifact_projection.py:356-431` (transport rejects together: `api/routes/artifact_projections.py:51-55`) |

### Write-time baked

| Path | Evidence |
| --- | --- |
| Group profile synthesis — privacy applied once at synthesis, persisted to `trip_group_profiles`, served to all members; mitigated by event-driven invalidation (`privacy.preference.changed` → invalidate), whose emission is best-effort and swallows failures, so an outage leaves a stale over-disclosing profile | `backend/preference_engine/synthesis/group_synthesizer.py:240-274`; `backend/core/db/privacy.py:85-96`; `backend/core/memory_subscribers.py:66-69,87-93` |
| Personal Memory narrative — synthesized once into markdown rendered into both 1:1 and group contexts; group-audience filter applied to inputs at synthesis time (`get_active_facts(user_id, visibility="group")`) | `backend/concierge/refresh_memory.py:405-415` |
| Chat composed cards — `CardBlueprintV1` snapshots persisted into `messages.metadata_`; revalidated only at action-tap time | `backend/concierge/composed_cards.py:236,297,346,891,1049-1050` |

### Membership-only (no per-item audience)

| Path | Evidence |
| --- | --- |
| Trip shared memories — no audience field on row; GET gated solely by membership; `"visibility": "group_safe"` is a hard-coded label in a legacy mirror, not a gate | `backend/core/models/trip_shared_memories.py:36-47`; `backend/api/routes/trip_group_memory.py:264,283-288` |
| Map photo layer — no viewer param; caller responsible for membership | `backend/core/db/photos.py:14-24` |
| The bulk of 252 `require_trip_member` call sites | `backend/api/auth.py:224-238` |

### Search / embeddings

Qdrant collections are shared; isolation is a **mandatory query-time owner
filter** ("enforced here — never delegated to the caller,"
`backend/core/vector/atlas.py:184-194,211-218`). **No audience metadata exists
in any vector payload** — shared content is simply not cross-searchable, which
is fail-safe but also means a co-participant can never find shared items by
search (missing READ capability, not just missing durable authority).

### Historical vs current membership

Current-only, aggressively: `is_trip_member` is a plain EXISTS with no
`left_at` (`backend/core/db/trips/members.py:392-405`); departure hard-deletes
membership and conversation participation in one transaction (`:818-857`).
Leaving revokes all read access instantly (S04-B behavior), and departed
members' contributions remain visible to remaining members. One deliberate
exception: member-edited group-memory generations survive departure as
"cooperatively owned trip history" (`:879-887`).

### lived_experience is owner-only by assertion

`surface_projection.py:55-56` raises unless `owner_only is True`;
`exposure.py:114-115` rejects recipient drift. The `visibility` field there is
treatment visibility, not audience. Any viewer/audience parameter: ABSENT.

---

## 3. Can author / subject / custodian / audience / purpose / expiry / use / inference / action be represented independently today?

**As a read/coordination contract: yes.** `ContributionAxes`
(`backend/core/models/contribution.py:211-216`) holds the five axes
independently, with validators preventing incoherent combinations
(T1-cannot-widen-audience at `:305-309`, T0-cannot-retain at `:297-304`,
admitted-learning-requires-L3/L4 at `:166-170`). Author-vs-subject-vs-custodian
distinctions appear in the contract vocabulary (`ContributionScope.actor_id`,
audience recipients, owner_kind) and in `RelationshipMemoryClaim`
(subject ≠ sharer). Status: **Architecture resolved**.

**As durable authority: no.** On every durable shared-content row the answer
collapses to one visibility flag plus implicit ownership:

- `personal_outcomes.visibility IN ('private','shared')` (schema `:754`) — no
  audience list, no purpose, no expiry.
- `trip_photos.visibility` 3-valued; the third value (`group_and_learn`) is
  the **only stored value in the codebase that binds audience and
  inference-purpose together** — and it binds them into one enum rather than
  representing them independently
  (`backend/api/routes/trip_photos.py:341-356`).
- `observations.shared` boolean + `context_scope`; author ABSENT; purpose
  ABSENT; inference authority is implicit in existence (`_tables/memory.py:
  359-388`).
- Expiry exists independently where it exists (`expires_at` on observations,
  invitations, takes); use/inference/action never do.

Conclusion: independent representation is **Projection modules composed** at
the contract layer and ABSENT at the storage layer. The fixture matrix's grant
model (§3) requires new durable construction; nothing needs to be *undone*
first, because nothing durable contradicts it — the flags can be read as
degenerate grants during migration.

---

## 4. How withdrawal/revocation would propagate today

Traced against Maya withdrawing `SRC-L02-M2` (shared photo) and narrowing
`SRC-L05-M1`. There is **no revocation bus**: no content-deletion event topic
exists (the full `emit()` literal set is 10 event names, none
deletion/revocation; subscriber registry at
`backend/core/event_subscribers.py:45-66` and
`backend/core/memory_subscribers.py:87-93`).

| Target | Verdict | Evidence |
| --- | --- | --- |
| Life surfaces | **SILENT FAILURE** | `lived_experience/lineage.py` is a forward-only decision audit trail — `link()` rejects re-linking (`:176`), `close()` is terminal (`:229`); 16 importers all construct/advance arcs, none invalidates. No deletion subscriber. |
| Home | **SILENT FAILURE (bounded)** | `invalidate_home_feed_cache` (`backend/home/feed.py:138`) has ~14 callers — booking/proposal/invite/membership — and **zero from any content-deletion route**; bounded by the 60s feed TTL (`feed.py:99`). |
| Chat | **PARTIAL** | Composed-card actions revalidate at tap and reject `revoked` (`composed_cards.py:891,1049-1050`) — pending-action side is sound. But `concierge/persistence.py` has **no delete/redact/supersede function**; `load_conversation_history` (`:240`) replays withdrawn content, including baked vision summaries (`:343`), to the model indefinitely. |
| Places | **SILENT FAILURE** | Photo upload writes occurrence evidence (`record_photo_evidence`, `backend/api/routes/trip_photos.py:411-421` → `core/db/occurrence_reconciliation.py:150-171`); the module is append-only — **no retraction function exists**. Deleted photos keep supporting occurrence conclusions for every member. |
| Saved compositions | **PROPAGATES (by recomputation)** | Canonical projection is a pure compiler (`canonical_artifact_projection.py:1-6`); Atlas boards store facets and recompose live on open (`api/routes/atlas.py:577-590`). Caveat: `composition/copy_cache.py` copy has a 1h TTL and no invalidation hook. |
| Search / embeddings | **PARTIAL** | Atlas artifact delete removes its vector (`core/db/atlas.py:495`, gated on `ATLAS_SEMANTIC_WRITE:490`). Observation vectors survive the artifact cascade but hydrate through `get_active_observations_by_ids`, so deactivated rows can't leak content — they only dilute retrieval (`concierge/memory_tools.py:1011-1024`). `core/vector/briefs.py:557 delete_brief` has **zero callers**. Most collections rely on `REBUILD_RECONCILIATION`, not event cascade (`core/derived_artifacts.py:34-38,120,218`). Trip photos/notes are never embedded — nothing to go stale. |
| Caches | **SILENT FAILURE** | Only 5 registered caches (`register_cache` hits: home_feed, plan_state, conflict_scan, narration_stops, TTLCache); no content-scoped cache; zero `publish_invalidation` calls from deletion routes; cross-worker invalidation silently degrades to local-only without `REDIS_URL` (`core/cache_invalidation.py:66-82`). Mobile: React Query persistence has a 12h maxAge cleared only at sign-out (`travel-app/utils/queryPersistence.ts:20-40`, `utils/accountTeardown.ts:60`); expo-image `memory-disk` cache is never cleared (`components/ui/AppImage.tsx:114`; no `clearDiskCache` callers). Revoked photo bytes persist on-device. |
| Pending actions | **PROPAGATES** | Pending chat turns re-resolve sources at send and 409 on missing custody (`api/routes/pending_chat_turns.py:231-276`; custody+storage must both be `verified`, `core/db/pending_chat_turns.py:344-346`). |

### The one complete cascade, and the one bare tombstone

- **Atlas artifact delete** (`backend/core/db/atlas.py:1104-1144` +
  `api/routes/atlas.py:1589-1613`): deactivates derived observations via
  `atlas_derived_signals`, drops the vector, forgets kept-place affinity,
  archives timeline entries, then refreshes Personal Memory. Two honest gaps
  in its own comments: observations lack queryable `source_artifact_*`
  columns outside the Atlas flow ("the other ~20 call sites will be migrated,"
  `:1276-1279`), and "the LLM aggregate may preserve a signal it can no
  longer justify" (`api/routes/atlas.py:1600-1603`).
- **Trip photo delete** (`api/routes/trip_photos.py:531-548`): one UPDATE
  setting `deleted_at`. No event, no cache call, no evidence retraction, no
  lineage. Retention later purges bytes (`core/db/retention.py:140-173`).
  Direct reads filter `deleted_at IS NULL`, and public story pages re-derive
  their photo allowlist at read — so *first-party* rendering heals, while
  every derivative listed above silently does not.

### Cross-root revocation precedent

Place handoffs are the one genuine cross-root revocation implementation:
revoke valid even from KEPT (`place_handoffs.py:579-583`), recipient's
proposed occasions withdrawn (`:645-657`), audit event written (`:663`),
recipient's chat card action dies at tap (`composed_cards.py:1049-1050`).
This is the pattern §8's `withdraw_grant` transition should generalize.

---

## 5. Who owns the shared core vs each person's private Outcome

- **Private Outcome ownership is clean and plural.** `personal_outcomes` is
  `owner_id`-scoped with visibility defaulting private
  (`domains/experience_graph/schema.py:720-763`); contract twin `Outcome`
  (`core/models/experience_graph.py:309-329`). The legacy lane
  `ExperienceOutcomeFeedback` is per-user, retractable, with a fail-closed
  exact-roster resolver so a companion verdict never transfers to a different
  roster and free text is "never copied into group composition or telemetry"
  (`backend/core/models/experience_outcomes.py:41-72,154-204`; prompt
  rendering marks it "private; do not quote to a group," `:377`). Plural
  Outcomes: **Architecture resolved** and partially **Implemented**.
- **Shared-core custody is host-implicit, not modeled.** `occasions.created_by`
  is the only custodian-like field (schema `:333-335`). On account deletion,
  custody of a shared occasion is reassigned to the longest-standing organizer
  (`backend/core/db/account_deletion.py:625-672`) — custodianship exists
  behaviorally but has no named field or grant.
- **Shared reconstruction (`CMP-L02-S` analogue) is not persisted** — the
  canonical projection compiler is read-time and the transport's together lane
  is 403 (§0.2). Whoever eventually owns "graph-owned sharing authorization"
  owns the shared core; today no one does. DOCUMENTED TARGET
  (`canonical_artifact.py:1-6` — "deliberately do not introduce a durable
  artifact owner").
- **Attribution risk in the group-memory document**: `TripSharedMemory` items
  carry no per-item author — only whole-document `edited_by` per version
  (`core/models/trip_shared_memories.py:36-47`). Fixture-matrix zero-count
  "contribution with lost attribution = 0" cannot be proven on this shape.
- **Post-trip exit artifacts are actor-scoped** (all `record_place_affinity`
  paths — with a fourth, group-derived path deliberately held at weight 0.0
  and `signal_source="trip_attendance"`,
  `backend/tasks/trip_attendance_affinity.py:65-73,202-209`; readers gate on
  `weight >= 1.0`, `core/context_compiler/source_loader.py:546-549`). The
  memory-bank note "all three paths actor-scoped" is stale: there are four,
  and the fourth is safe only via the weight convention.

---

## 6. Does unblock restore any grant implicitly?

**There is no block to audit — the entire block/no-contact/mute-person layer
is ABSENT** in both repos.

Searches run (backend `--include='*.py'`, mobile `*.ts/tsx`):
`blocked_user|block_user|user_block|blocked_by|blocklist|is_blocked|unblock|
blocked_at|muted_user|mute_user|no_contact|do_not_contact|hide_person|
hidden_from|shielded`, plus person-filtered `suppress`, plus every table and
constraint name containing block/mute, plus SQL migrations. Every hit is
unrelated: `itinerary_blocks` (the plan primitive,
`core/db/_tables/itinerary.py:140`), UI `BlockedActionRow`, photo-permission
`blocked`, Metro `resolver.blockList`, palette token `surface.mute`.

Adjacent mechanisms that are *not* person-blocks: per-conversation Vesper mute
(`core/group_agency.py:43-48` — mutes the agent, not a person), leave-by
day-mute (`notifications/leave_by.py:184-200`), arbiter notification
suppressions keyed on dedup content (`core/db/arbiter_suppressions.py:27-78`),
memory-correction suppression (content-scoped,
`core/db/memory_corrections.py:93`).

**The substrate's semantics already match S10.** The grant system that would
host block is revoke-and-re-grant, not toggle-over-grants: revocation stamps
`granted_at=None, revoked_at=now`, and "re-granting stamps a fresh
`granted_at` rather than reviving the old grant"
(`backend/core/db/relationship_visibility.py:66-83`); unfollow hard-deletes
the edge (`core/db/follows.py:56-58`). No code path stores a suppression flag
*over* a live grant — the shape that would make unblock silently restore
audience does not exist. So S10's "unblock restores no old grant" is the
natural consequence of building block as an independent safety overlay (fixture
matrix plane 3) rather than as grant mutation — which is also what the matrix
requires. Record separately: the safety overlay itself (S08 suppression of
compositions/periphery/prompts) is ABSENT and is new construction.

---

## 7. Does memory synthesis launder shared evidence into person-level narrative?

The contract §12 flags are **verified and current**, with two additional
findings the contract does not list (the cross-user write hole and the group
digest inlet). Verdict per path:

### 7.1 `concierge/_prompts_skills.py` — NON-CONFORMING

- Same-turn `observe()` for preference/personality/mood: SKILL_MEMORY block
  at `:1518-1598`; "personality insight, trip-specific wish, energy/mood
  context" (`:1535-1537`); emotional-investment trigger (`:1549-1551`);
  "Call observe() in the same turn as the signal — no delay, no batching"
  (`:1553-1557`); observe MANDATORY on booking turns (`:1563-1568`).
- Patterns of silence instructed as observations: "Notice what people DON'T
  do… notice who hasn't spoken recently… if you see a pattern (someone
  consistently ignores food suggestions, or stops participating after a
  certain decision), that's worth an observation" (`:1590-1597`). This
  directly contradicts contract §11 ("ignored options, silence… not allowed
  as durable person inference by default").
- Third-party relational claim exemplar in the post-trip debrief skill:
  "Sam mentioned he wished there'd been more just-the-two-of-them time with
  Maya. File for future trip design." (`:2353-2361`) — records a claim naming
  another person from one speaker's utterance.
- Mitigation present but rhetorical only: "Use context_scope honestly… must
  not become universal personality" (`:1560-1561`).

### 7.2 `concierge/memory_tools.py` — NON-CONFORMING

- Writes to `observations` (`core/db/_tables/memory.py:359-388`) via
  `create_observation`. Recorded: subject (user_id), `shared` bool,
  provenance JSONB (evidence_origin + source_message_id), context_scope,
  supersedes, expiry. **No author column** — the author trace is a message
  UUID inside JSONB.
- Real guards exist: legacy `target_user_id` rejected
  (`cross_user_observation_forbidden`, `:617-624`), group visibility only
  from a group trip conversation (`:625-636`), recall blocked in group rooms
  (`:679-685`), constraint mutation self-bound (`:666-677`).
- **Live cross-user write hole**: the actor-binding equality check at
  `:651-664` excludes `observe` from its tool set and provides no replacement
  check; `_normalize_user_ids` → `_resolve_user_id` resolves display names
  against trip members (`:42-102`), so `observe(user_id="maya", …)` on a trip
  turn writes into Maya's personal memory. `observe` is in `_ALWAYS_TOOLS`
  (`concierge/_tools_select.py:64`), loaded every turn including group rooms
  (call site `concierge/agent.py:1851-1864`). The postcondition
  (`concierge/postconditions.py:602-617`) detects the mismatch but only
  stamps a failed receipt — the row is not deleted (`:848-857`), and
  auto-synthesis has already been scheduled (`memory_tools.py:698-699`).
- **No admission gate**: `validate_contract_context` is a no-op for
  unregistered tools and `observe` is not in the contract registry
  (`concierge/tool_contracts.py:316-381`); classified
  `AGENT_MAINTAINED_STATE`, not `USER_AUTHORIZED`
  (`concierge/tool_registry.py:518`). The contribution-policy path exists
  only in default-off shadow mode (§0.1).

### 7.3 `concierge/refresh_memory.py` — NON-CONFORMING (audience-aware, authorship-blind)

- Inputs: `get_all_active_observations(user_id)` — filters only user/active/
  expiry; no author filter (structurally impossible), no shared filter, no
  grant check (`:392-415`; `core/db/observations.py:539-569`). The one real
  audience filter is `get_active_facts(user_id, visibility="group")` with the
  honest rationale that PM markdown "is rendered into BOTH 1:1 and
  group-channel context (no separate render path)" (`:408-415`).
- The synthesis prompt writes personality narrative by design — "Who They
  Are," "Social & Group Dynamics," "Energy & Rhythm" (`:61-83`).
- `[private]` observations are not excluded from group-reachable narrative;
  the prompt instructs abstraction instead: "let the signal inform your
  understanding but render it abstractly… NOT a named-person callout"
  (`:123-135`; tagging at `:768-775`, where the fallback
  `getattr(obs, "shared", True)` defaults permissive, though the DB default
  is false). Prompt-level mitigation of a storage-level gap.
- **Group digest inlet**: `_get_prior_trip_summaries` folds group trip digests
  — `what_worked`, `what_didnt`, and `group_dynamics_learned.energy_pattern`
  — into one person's narrative with no audience or grant check
  (`:479-482,829-877`). Multi-author trip evidence → person-level narrative:
  the cleanest laundering instance found.

### 7.4 `concierge/reflection.py` — NON-CONFORMING

- Group-level agent events folded into one person's reflection:
  `events += [e for e in agent_evts if e.user_id == user_id or e.user_id is
  None]` (`:247-249`).
- Silence-to-observation instruction: "Notice absence patterns… Proposal
  non-votes (silence_observed signals) tell you who isn't participating"
  (`:111-116`).
- Up to 8000 chars of the group trip digest injected into the reflection
  prompt (`:598-603`). Reflection's `observe` schema is a stripped variant
  (no visibility/context_scope/confidence) with `user_id` required
  (`:158-173`); `trip_id=None` at `:725-731` disables name resolution, but a
  literal UUID still passes the §7.2 hole.

### 7.5 Conforming neighbors

- `post_trip_memory_refresh.py`: fan-out per member to their own refresh; its
  only direct write is a factual trip-completed observation with operational
  provenance (`:72-127,196-199`). CONFORMING in itself — but it is the
  trigger that guarantees the group digest exists before each member's
  post-trip refresh, i.e. it arms §7.3's inlet.
- `preference_engine/edit_inference.py`: trip-scoped input, actor-scoped
  output, provenance carried (`:149-238`). CONFORMING.
- Group activity → individual affinity is deliberate and weight-0 with
  distinguishing `signal_source` (§5). CONFORMING but convention-held.

---

## 8. Smallest renderer-neutral fixture contract for the design prototype

The prototype needs deterministic viewer-relative outputs for S01, S05, S07,
S08, S10, S11 over the L02 + L05 graphs — independent of any current API,
since §§2-6 show the substrate cannot yet produce them. Proposed shape
(YAML; JSON-equivalent): one **world file** (objects + grants + transitions)
and one **expectation file per (transition, viewer)** so design and any later
projection module test against identical fixtures.

### 8.1 World file — `together-fixture.v1`

```yaml
fixture_contract: together-fixture.v1
principals:
  - {id: "person:feihu", display: "Feihu"}
  - {id: "person:maya", display: "Maya"}
  - {id: "person:alex", display: "Alex"}
  # Vesper is an operator, never a principal.

epochs:
  - {id: "epoch:OCC-L02:1", scope: "occasion:OCC-L02", opened: "2026-08-20"}
  - {id: "epoch:rel:feihu-maya:1", scope: "relationship:feihu-maya", opened: "2026-06-01"}

occasions:
  - id: "occasion:OCC-L02"
    kind: dinner
    custodian: "person:feihu"
    members:
      - {person: "person:feihu", role: host, status: active, epoch: "epoch:OCC-L02:1"}
      - {person: "person:maya", role: member, status: active, epoch: "epoch:OCC-L02:1"}
      - {person: "person:alex", role: member, status: active, epoch: "epoch:OCC-L02:1"}
    lifecycle: lived

sources:
  - id: "SRC-L02-F1"   # invitation + time change
    author: "person:feihu"
    lane: shared_core
  - id: "SRC-L02-M1"   # "I'll bring dessert" — commitment, not occurrence
    author: "person:maya"
    lane: attributed
    truth: {kind: commitment}
  - id: "SRC-L02-M2"   # pasta-table photo
    author: "person:maya"
    lane: attributed
    media: {kind: photo, place_precision: exact}
  - id: "SRC-L02-A1"   # receipt
    author: "person:alex"
    lane: attributed
  - id: "SRC-L05-F1"   # Rome heat/transit note
    author: "person:feihu"
    lane: human_authored
  - id: "SRC-L05-M1"   # Paris heat photo + note
    author: "person:maya"
    lane: human_authored
    media: {kind: photo_note, place_precision: exact}

outcomes:  # never enter any shared projection
  - {id: "OUT-L02-F", owner: "person:feihu", scope: "occasion:OCC-L02"}
  - {id: "OUT-L02-M", owner: "person:maya",  scope: "occasion:OCC-L02"}
  - {id: "OUT-L05-F", owner: "person:feihu", scope: "cmp:CMP-L05-B"}
  - {id: "OUT-L05-M", owner: "person:maya",  scope: "cmp:CMP-L05-B"}

grants:  # the 13-field record from the fixture matrix §3, one per shared use
  - id: "grant:L02-M2"
    author: "person:maya"
    subjects: ["person:maya", "person:feihu", "person:alex"]  # people in frame
    custodian: "person:maya"
    audience: {mode: occasion, occasion: "occasion:OCC-L02", epoch: "epoch:OCC-L02:1"}
    purpose: [occasion_memory, shared_reconstruction]
    precision: {place: exact}
    validity: {from: "2026-08-20", until: null}
    reshare: none
    post_membership: compact_historical_access   # S04-A default
    posthumous: null
    revocation: {owner: "person:maya", scope: [source, derived, projections]}
    dependency_lineage: ["cmp:CMP-L02-S", "cover:CMP-L02-S",
                         "snippet:CMP-L02-S:photo", "idx:emb:SRC-L02-M2"]
  - id: "grant:L05-M1"
    author: "person:maya"
    subjects: ["person:maya"]
    custodian: "person:maya"
    audience: {mode: named_people, recipients: ["person:feihu"],
               epoch: "epoch:rel:feihu-maya:1"}
    purpose: [comparison, private_return]        # NOT person_inference
    precision: {place: exact}
    validity: {from: "2026-08-25", until: null}
    reshare: none
    post_membership: n/a
    posthumous: null
    revocation: {owner: "person:maya", scope: [source, derived, projections]}
    dependency_lineage: ["cmp:CMP-L05-B", "idx:emb:SRC-L05-M1"]
  # grant:L02-M1 (dessert commitment), grant:L02-A1 (receipt),
  # grant:L02-F1 (shared-core invitation) follow the same shape.

compositions:  # always recompiled from currently-valid inputs; never inputs themselves
  - id: "cmp:CMP-L02-S"
    audience_rule: current_authorized_participants
    inputs: [shared_core, "grant:L02-F1", "grant:L02-M1", "grant:L02-M2", "grant:L02-A1"]
  - id: "cmp:CMP-L02-F"
    audience_rule: owner_only   # Feihu; may add Feihu-private state
    inputs: ["cmp:CMP-L02-S", "OUT-L02-F"]
  - id: "cmp:CMP-L05-B"
    audience_rule: grant_intersection   # both lanes' grants must be valid
    inputs: ["SRC-L05-F1", "grant:L05-M1"]

transitions:
  S01: {op: none}
  S05: {op: withdraw_grant, grant: "grant:L02-M2"}
  S07: {op: narrow_grant, grant: "grant:L05-M1",
        change: {precision: {place: city}}}
  S08: {op: block, actor: "person:feihu", target: "person:maya"}
  S10: {op: unblock, actor: "person:feihu", target: "person:maya"}
  S11: {op: reconcile, parties: ["person:feihu", "person:maya"],
        new_epoch: "epoch:rel:feihu-maya:2",
        new_grants: []}   # reconciliation authors new grants explicitly
```

### 8.2 Viewer projection output — the renderer-neutral unit

Each expectation is a list of projection units. A renderer (design board,
mobile screen, test) consumes only this shape:

```yaml
projection:
  transition: S05
  viewer: "person:feihu"
  units:
    - ref: "cmp:CMP-L02-S"
      lane: vesper_composition
      state: recompiled            # visible | recompiled | degraded | suppressed | absent
      attribution: preserved
      must_contain: ["SRC-L02-F1", "SRC-L02-M1", "SRC-L02-A1"]
      must_not_contain: ["SRC-L02-M2", "paraphrase:SRC-L02-M2",
                         "cover:from:SRC-L02-M2", "snippet:from:SRC-L02-M2"]
      degrade_note: silent          # no substitute paraphrase; absence unexplained content-wise
    - ref: "SRC-L02-M1"
      lane: "attributed:person:maya"
      state: visible               # different Source/grant — survives
    - ref: "OUT-L02-F"
      lane: "private:person:feihu"
      state: visible
    - ref: "OUT-L02-M"
      lane: "private:person:maya"
      state: absent                # never renderable to Feihu in any transition
  receipts:
    - {to: "person:maya", kind: revocation_readback,
       affected: ["cmp:CMP-L02-S", "idx:emb:SRC-L02-M2"]}
```

Unit vocabulary (closed sets, renderer-neutral):

- `lane`: `shared_core | attributed:<person> | private:<owner> |
  vesper_composition`
- `state`: `visible | recompiled | degraded | suppressed:<reason> | absent`
  — `suppressed` carries `safety_overlay | revoked | precision` and must
  never leak why in rendered content, only in the policy trace.
- `attribution`: `preserved | n/a` (no third value; lost attribution is a
  zero-count failure).
- `precision`: optional, e.g. `{place: city}` — the max renderable precision.

### 8.3 Required expectations per transition (both graphs, all viewers)

| Transition | Deterministic expectations (from the fixture matrix §5, restated as unit assertions) |
| --- | --- |
| **S01** | Feihu/Maya/Alex each see `cmp:CMP-L02-S` `visible` with all four lanes attributed; each sees own Outcome `visible`, others' `absent`; dessert renders as commitment ("planned to bring"), not occurrence. |
| **S05** | As in §8.2. Alex's view identical to Feihu's for the shared units. Maya retains her own original (`SRC-L02-M2` `private:person:maya` `visible`) — withdrawal of the grant is not deletion of her Source. |
| **S07** | Feihu: `cmp:CMP-L05-B` `recompiled` with `precision: {place: city}`; `must_not_contain: ["place:exact:SRC-L05-M1"]` across text, map pins, snippets, and search index entries; prior generated text containing the precise Place `absent` or superseded. |
| **S08** | Feihu: `cmp:CMP-L05-B` and `cmp:CMP-L02-S` `suppressed:safety_overlay`; his independent lanes (`SRC-L05-F1`, Rome/Red Hook history) `visible`; zero units may open a social path to Maya (no prompts, no status, no location). Maya: her own record unchanged; no notification of the block. Grants: unchanged rows — suppression is an overlay, not grant mutation. |
| **S10** | Only the overlay lifts: units return to the state their **grants** currently justify — for L02 that is `visible` (grants intact); for anything revoked meanwhile, still `absent`. `must_not` assertions: no proactive return unit, no "welcome back" composition, no restored follows/rank. |
| **S11** | New-epoch grants only: old `grant:L05-M1` stays historical; `cmp:CMP-L05-B` renders only if re-authorized by a new grant in `epoch:rel:feihu-maya:2`; no composition reactivates without one. |

### 8.4 Why this is the *smallest* contract

- It adds exactly the objects the code lacks (grant record, epoch, overlay,
  lineage list) and reuses what exists (occasion members
  `schema.py:353-378`, invitation vocabulary `:380-404`, plural outcomes
  `:720-763`, lane attribution from `RelationshipMemoryClaim`).
- Every §8.3 assertion maps 1:1 to a fixture-matrix zero-count, so the design
  prototype and any later projection module share one oracle.
- It is renderer-neutral: units carry no layout, copy, or component names —
  the design board decides how `suppressed:safety_overlay` *feels*; the
  contract only fixes what may and may not exist on screen.

---

## 9. Non-conforming seams (verifying and extending contract §12)

Contract §12's five bullets, verified, plus seams this audit adds. "Seam"
means: a place where the contract's authority model and the code diverge
today.

| # | Seam | Status | Evidence |
| --- | --- | --- | --- |
| 12.1 | `_prompts_skills.py` / `memory_tools.py` same-turn observe for preference/personality/mood/emotional investment/silence | **VERIFIED, current** | §7.1-7.2; `_prompts_skills.py:1518-1598,2353-2361` |
| 12.2 | `refresh_memory.py` / reflection / PM synthesis promote observations into higher-authority narrative without the shared gate | **VERIFIED, current** | §7.3-7.4 |
| 12.3 | Ordinary conversation lacks an enforceable continuity-read/no-write (T0) posture | **VERIFIED** — `observe` has no contract entry, no admission, `AGENT_MAINTAINED_STATE` class (`tool_contracts.py:316-381`, `tool_registry.py:518`); contribution policy shadow-only (`config.py:172-175`) | |
| 12.4 | Share capture review-first vs value-first | NOT RE-AUDITED here (out of Together scope) | |
| 12.5 | Causal correction across every consumer not certified | **VERIFIED and sharpened** — see §4 verdict table | |
| A1 | `observe` cross-user write hole: excluded from actor-binding, display-name resolution to trip members, detection-only postcondition | NEW | `memory_tools.py:651-664,42-102`; `postconditions.py:602-617,848-857` |
| A2 | No author column on `observations`; provenance-only trace, unindexed | NEW | `core/db/_tables/memory.py:359-388`; `core/db/atlas.py:1276-1291` |
| A3 | Group trip digest (incl. `group_dynamics_learned`) → individual PM narrative | NEW | `refresh_memory.py:479-482,869-877` |
| A4 | Reflection folds `user_id is None` group agent events into one person | NEW | `reflection.py:247-249` |
| A5 | Trip-photo withdrawal is a bare tombstone; upload writes cross-member occurrence evidence with no retraction counterpart | NEW | `trip_photos.py:411-421,531-548`; `occurrence_reconciliation.py` (append-only) |
| A6 | Chat persistence has no redact/supersede primitive; withdrawn content replays to the model | NEW | `concierge/persistence.py:19,118,240,343` |
| A7 | `trip_members` hard-delete forecloses historical epochs / S04-A | NEW | `core/db/trips/members.py:818-822` |
| A8 | Shared-memory items lack per-item attribution | NEW | `core/models/trip_shared_memories.py:36-47` |
| A9 | Group profile bake mitigated by best-effort event emission that swallows failures (stale = over-disclosure) | NEW | `core/db/privacy.py:85-96` |
| A10 | Mobile caches (React Query 12h persist; expo-image disk) cleared only at sign-out; never on revocation | NEW | `travel-app/utils/queryPersistence.ts:20-40`; `utils/accountTeardown.ts:60`; `components/ui/AppImage.tsx:114` |
| A11 | `core/vector/briefs.py:557 delete_brief` has zero callers — brief index removal never wired | NEW | verified against registries/dispatch |
| A12 | Together projection lane rejected at transport pending a sharing authority no module owns | NEW (also the correct current behavior) | `api/routes/artifact_projections.py:51-55` |
| A13 | Stale memory-bank claim: `record_place_affinity` "all paths actor-scoped" — a fourth, group-derived path exists, safe only by weight-0 convention | NEW | `tasks/trip_attendance_affinity.py:65-73,202-209` |

---

## 10. Open questions for the founder

1. **Epochs vs hard delete (R4).** S04-A requires historical membership
   evidence that the current departure cascade destroys by design (including
   deliberate privacy rationale — bearer-link revocation, conversation
   purge). Should epochs be introduced as new append-only tables beside the
   hard-delete behavior (preserving the current privacy posture as the
   S04-B variant), or does S04-A's "compact historical access" get scoped
   down for v1? The existing precedent to generalize is
   `conversation_membership_events` — the codebase's one append-only
   severance ledger, built precisely so "a prior invite redemption cannot
   silently resurrect someone who chose to leave"
   (`core/db/_tables/conversations.py:277-304`). (The mobile QA fixtures
   `62-02-j24-membership-ended.png` / `62-04-j24-history-after-rejoin.png`
   in `travel-app/` suggest the product already intends epoch semantics the
   schema does not provide.)
2. **Who owns the "graph-owned sharing authority"** that
   `artifact_projections.py` is waiting for? The grant record in §8.1 is the
   obvious candidate shape; its owner (experience-graph domain vs a new
   grants domain) determines where S05/S07 revocation starts.
3. **Is the §8 grant record the durable promotion of `ContributionAxes`,** or
   a separate object that references a ContributionDecision? The contract
   says envelope shapes are storage-neutral "unless a later implementation
   decision promotes a durable shape" — this audit's evidence says Together
   cannot ship without that promotion happening for audience grants
   specifically.
4. **Blast-radius decision for withdrawal (R1).** Given §4, an honest v1
   demo can only wire withdrawal through recompute-at-read surfaces. Is a
   fixture-scale demonstration (Consumer flow proven at fixture scale)
   acceptable for the Together gate, with the revocation bus
   (deletion event topic + lineage columns) as its own workstream?
5. **The two smallest memory fixes** — removing `observe` from the
   actor-binding exclusion (`memory_tools.py:653`) and stripping
   `group_dynamics_learned` from PM synthesis input
   (`refresh_memory.py:875-877`) — are one-line-scale and close live
   laundering paths flagged by contract §12. This audit made no changes;
   should these be authorized ahead of the broader migration order?
6. **Shared-memory item attribution (A8).** The fixture matrix's
   lost-attribution zero-count cannot hold on the current whole-document
   shape. Migrate items to carry authors, or exclude the group-memory
   document from the Together shared-core story?

## Applied safety fixes — 2026-08-31

Narrow fixes applied against this audit's findings (uncommitted, in
`travel-agent/backend`); tests: `tests/concierge/test_memory_tools.py`,
`test_refresh_memory.py`, `test_memory_workflow.py`, `test_prompt_golden.py`
(goldens regenerated via `UPDATE_GOLDEN=1`), `test_prompt_budget.py` — all green.

- **A1 / §7.2 cross-user `observe` write hole — FIXED.**
  `concierge/memory_tools.py:651-658`: `observe` removed from the
  actor-binding exclusion set, so any observe whose resolved `user_id`
  differs from the authenticated speaker is refused
  (`cross_user_memory_access_forbidden`) before execution. Display-name
  resolution against trip members still runs, but can no longer become a
  cross-custody write. The detection-only postcondition was left in place
  (defense in depth); no subject-reference storage was built.
- **§7.1 / 12.1 same-turn psychological observation instructions — FIXED
  (narrowed, not deleted wholesale).** `concierge/_prompts_skills.py`
  SKILL_MEMORY: "personality" removed from the observe tool description
  (~:1523); "personality insight" and "energy/mood context" triggers replaced
  with an explicit prohibition on inferred personality/mood/psychological
  characterization (~:1534-1539); the emotional-investment trigger bullet
  removed (~:1546); the "Notice what people DON'T do" silence-pattern
  paragraph replaced with an explicit silence-is-not-durable-signal rule
  (~:1589-1591). Post-trip debrief skill: "Energy revelations" (slow-start
  person) and "Social dynamics" (Sam/Maya third-party relational) exemplar
  bullets removed (~:2350). Explicitly-authored preference/constraint capture
  (allowed by contract §11) was preserved, as were the same-turn mechanics for
  those.
- **A3 / open question 5 (`refresh_memory.py:875-877`) — FIXED as the audit
  specified, not as loosely re-described elsewhere.** The lines at 875-877
  are the `group_dynamics_learned.energy_pattern` inlet from group trip
  digests into individual Personal Memory synthesis (not literal observe()
  instructions). That inlet is now stripped: `refresh_memory.py:872-877`
  no longer folds `group_dynamics_learned` into `_get_prior_trip_summaries`
  output; `what_worked`/`what_didnt` remain (per the audit's scoped
  recommendation).
- Left as-is (out of this pass's scope): `reflection.py:111-116` silence
  instruction and `:247-249` group agent-event folding (A4), the group digest
  `what_worked`/`what_didnt` inlet, A2 author column, A5 photo withdrawal,
  observe contract-registry entry (12.3).
