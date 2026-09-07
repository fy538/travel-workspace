---
doc_type: working
status: active
owner: founder / social experience / complete-system integration
created: 2026-09-07
last_verified: 2026-09-07
expires: 2026-10-07
why_new: Expands the complete-system roadmap's social package into reviewable cross-repo implementation packages; the design handoff owns experience intent and the capability map owns its earlier audit, neither owns engineering dependencies and acceptance.
supersedes: []
depends_on:
  - complete-system-integration-roadmap-2026-09-05.md
  - social-experience-capability-map-2026-09-07.md
  - claude-design-social-experience-project-handoff-2026-09-07.md
  - fixtures/shared-fixture-world-2026-09-07.md
  - ../systems/contribution-and-consequence.md
  - ../decisions/2026-09-05-amend-home-composition-canon.md
---

# Social implementation roadmap — a shared layer of the lived-world product

## 1. Recommendation and scope

**Build social as a connected capability of the existing product: deliberately
shared human material, easier participation, useful shared adaptation, and
continuity with people and places. Do not build another social application
inside Vesper.**

The design is sufficiently developed to begin engineering contract mapping and
bounded implementation planning. Its remaining semantic correction does not
justify another broad design round. Conversely, attractive screens do not adopt
the four outstanding permission/identity proposals or prove runtime support.

This plan elaborates package 5 of the
[complete-system roadmap, §9.8](complete-system-integration-roadmap-2026-09-05.md#98-connected-system-next-stage--september-7-holistic-rebaseline).
Integration retains responsibility for shared landing, generated contracts and
activation; Life, Content, Capture and Plan keep their existing ownership.
Package numbers below are local work boundaries, not a competing company roadmap.

The outcome is three independently worthwhile experiences:

1. **A little of your world:** Maya shares an ordinary photograph, place, map,
   recipe or note; Nora receives something enjoyable or useful without having
   to reply, contribute, create an Occasion or ask AI to unlock it.
2. **An easier way to get together:** Nora can invite; Sam can understand,
   answer and arrive; Dana can help without attending; changing circumstances
   are handled without turning everyone into project administrators.
3. **Something stays with us:** the right people can find the actual material
   later, retain different interpretations, and optionally do something again.
   Past participation does not become a future commitment.

These are an implementation portfolio, not an invitation funnel. Ordinary
sharing does not have to lead to dinner; dinner does not have to lead to a
connection; receiving is complete without reciprocation. The four value moves
remain **Make sense. Open possibility. Help it work. Carry forward.**

**Current execution recommendation:** §10 turns this portfolio into the next
reviewable implementation sequence. Complete ordinary selected sharing,
original receiving and basic Life refinding together; then extend the same
contracts into participation and practical adaptation. §9 is the corrected
branch-local implementation record, not completion of S0–S7. The sequence in
§10 refines the packages below rather than establishing another roadmap.

### Planning and execution authority

This plan itself does not authorize application edits, schema changes, new
provider integration, bulk migration, runtime flag activation, deployment,
message sending, or adoption of pending policies. The first bounded implementation
batch was subsequently requested and is recorded in §9. The later request to
plan the next work authorizes this documentation revision, not those additional
effects. Execution should obtain the required owner/product rulings where named
below; already authorized behavior can advance independently of those rulings.
No wholesale Chat, Life or four-root redesign is required by this plan.

## 2. Evidence and the current starting point

Inspected September 7: workspace `main` at `48de261`; backend `main` at
`1146ae041`; mobile `codex/entity-object-design-completion` at `f4401ef73`.
All have concurrent work or adjacent worktrees. These are reproducible planning
coordinates, not frozen execution bases. Recheck status, ancestry, files and flags
before each package.

The fresh pass read current domain/models/routes/readers, the capability map,
four decision proposals, contribution contract, social-placement decision,
latest design response, and recent Integration, Home, Life and Plan thread
handoffs. This is source-and-document evidence: **no application test suite,
provider run or native social journey was executed for this roadmap.** Lane test
reports are not a combined-system pass.

| Area | Verified reusable code / recent lane evidence | Remaining gap or limit |
| --- | --- | --- |
| Relationship identity | Pair circles have invited/active/declined/left membership, mutual confirmation, pair-key handling and a pair conversation | Consumer connection defaults and consistent contact controls need closure. Current circle creation requires a display name; do not expose that as a naming assignment for a two-person connection |
| Addressed sharing | UUID relationship handoffs have source references, prepared commands, recipient reads, revisions, expiry/revocation and an Occasion-opening bridge | The inspected writer is an exact pair-room, one-place, short-note path. A place is required and text is bounded to 280 characters. This is not complete multi-recipient or non-spatial sharing |
| Home receiving | Home receiving is merged into backend main (`1146ae041`) and mobile Entity (`f4401ef73`); Integration also reports a clean mobile-main merge (`8bed6ca82`). The Home adapter preserves the original note and its author | The broader original-object destination, media variants and casual friends field are not certified by the note adapter. Do not reimplement the merged receiving/navigation work |
| Contextual Ask | T0 admission and effective retention enforcement exist. A recipient-bound `concierge/handoff_entry.py` and mobile seed changes were uncommitted during this inspection | Treat that work as active Integration/Chat ownership, not a missing seam to rebuild. It concerns a bounded note, not arbitrary attachments or blanket friend-source permission; effective permission acquisition and write paths still need review |
| Occasion and invitations | `occasions`, `occasion_members`, `occasion_invitations` and graph invitation/read/response APIs exist | Current canonical membership/invitation foreign keys require account user IDs. Non-account guest capability, narrow remote contribution and sensitive disclosure are narrower unfinished questions |
| Invitation transport | Existing Trip invite tokens, public projection, landing page and delivery machinery provide reuse candidates | Public preview or authenticated Trip upgrade does not establish no-account dinner participation. Existing transports must not silently add full Trip membership |
| Live engine | `SharedPlanRepairAdapter` validates current constitution/roster/Plan references and consumes group-safe options; it can show/recommend/abstain without applying | This is not fresh option production, owner adoption, or truthful participant-specific readback by itself. Follow the existing gateways and practical-assessment owners |
| Life | Retained Source, Occasion, Plan and Outcome projections and owner-change delivery exist. Indexed organization has advanced on a separate lane | The latest Life review reported migration/exclusion, stale reconciliation, concurrency and reader defects; fixes are in progress. Do not merge that branch wholesale or add a second social archive |
| Trust and attention | Relationship/place-pull grants, membership removal and message-report submission exist | The inspected report route logs and optionally forwards to Slack. It is not evidence of complete abuse handling or block enforcement. No complete per-person mute/block path was established in this audit |

Runtime flags, reachability, test evidence and shipped behavior are different
columns. UUID handoffs and place-pull have separate flags; social circles have a
different default. Source workers and Life indexed serving also have independent
activation boundaries. A flag name or checked-in implementation is not a claim
about the deployed environment.

### Code navigation for implementers

Paths here are relative to the workspace; follow actual functions rather than
old architecture diagrams that list aspirational domain directories.

- Relationship source/authority: `travel-agent/backend/domains/relationships/{models,schema,repository,api}.py`, `backend/api/routes/relationship_handoffs.py` and `backend/application/relationship_openings.py` inside that repo.
- Connections: `travel-agent/backend/core/db/social_circles.py`, `backend/core/models/social_circles.py`, `backend/api/routes/social_circles.py`; mobile `travel-app/data/social.ts`.
- Source custody/admission: `travel-agent/backend/core/contribution_admission.py`, `backend/core/db/{intake_v2,intake_anchors,pending_chat_turns}.py`.
- Receiving: `travel-agent/backend/root_projection/v2/{home_portfolio,home_source_adapters,source_contribution_discovery}.py`; mobile `travel-app/components/root-projection/`, `utils/rootProjectionNavigation.ts`, `data/relationshipPlaceHandoffs.ts`.
- Places: `travel-agent/backend/places/relationships.py` and section/read owners; mobile `travel-app/components/places/renderers/socialCard.tsx`. The existing friend strip's legacy saved-place presentation is not the current full social design.
- Occasion: `travel-agent/backend/domains/experience_graph/{schema,repository,commands,invitation_commands}.py`, `backend/api/routes/experience_graph.py`.
- Guest reuse: `travel-agent/backend/core/db/trip_invites.py`, `backend/api/routes/{invites,invite_landing}.py`, `backend/invites/public_projection.py`, `backend/notifications/invite_delivery_tasks.py`.
- Shared action: `travel-agent/backend/lived_experience/engine.py`, `adapters/shared_plan_repair.py` under that package, existing prepared-consequence/owner gateways and graph Plan/Commitment commands.
- Life: `travel-agent/backend/life_projection/{retained_source_projector,occasion_projector,outcome_projector,owner_contracts,current_authority}.py`; the indexed organization work remains subject to the Life lane's tested cut.

## 3. Architecture to preserve—and what must become explicit

### 3.1 One source of truth per concern

| Concern | Owner | Consumers must not do |
| --- | --- | --- |
| Original bytes, literal authored material, source lifecycle | Existing Source/Intake or appropriate original-object owner | Copy the original into independent Home, Places and Life stores with divergent deletion behavior |
| A deliberate share, recipients and delivery rights | Relationships/share authority coordinated with the source owner | Treat a visible URL, card or friendship as permission to reuse the underlying source |
| Ongoing connection and person-level contact restrictions | Existing relationship/circle ownership plus its trust enforcement boundary | Build a parallel friendship graph from follows, co-presence or repeated invitations |
| Invitation, participation and bounded contribution | Canonical Occasion/invitation owners | Make the host author another person's answer or make a contributor an attendee |
| Arrangement and accepted obligations | Plan/Commitment owners | Let a root card or engine recommendation become a competing arrangement |
| Options, preparation and situated judgment | Existing live engine and specialist suppliers | Mutate an arrangement or send an invitation merely because an alternative is attractive |
| Indexed organization and later refinding | Life over current owner-authorized records | Become the owner of shared media or permanently preserve revoked source content |
| Reading, presentation and attention | Root/detail projections, existing navigation and notification gates | Widen audience, infer attendance or produce social obligations from viewing |

The likely extension is a **bounded, source-backed human-sharing contract in
the existing ownership structure**, not a universal SocialPost containing
conversation, media, attendance, memory and generated content. S0 must settle
its exact persistence mapping before S1 schema work. Existing PlaceHandoff can
remain a specialization; do not stretch a mandatory-place, pair-only record by
inventing fake places, group conversations or user accounts.

The integration contract needs stable original identity and author, selected
source/component references, effective recipients, purpose/use authority,
revision and lifecycle, canonical reader/action references and repair lineage.
These are requirements, **not a prescribed new table or client-carried permission
blob**. Resolve authority on the server; expose only safe, understandable scope.

### 3.2 Independent state dimensions

Do not collapse these into one `shared` or `accepted` state:

- Connection status versus permission for this particular object.
- Delivery/display permission versus private AI-use permission.
- Invitation response versus responder identity assurance.
- Arrangement revision versus each person's participation and arrival window.
- Attendance versus the right to contribute or edit.
- Author's original versus someone else's eligible projection or saved reference.
- A past Occasion versus a proposal to do something again.

For the design's remaining concrete error: if Nora changes dinner from seven to
eight and Sam has not answered, show **“Dinner now starts at eight”** without
asserting **“You're expected around eight.”** His previous arrival statement
remains historical context, not renewed agreement. Confirmed acceptance, an
unchanged personal window and a decline need their own truthful readbacks. Do
not make every arrangement change demand a response; request one only when an
actual participation/commitment conflict warrants it.

## 4. Four decisions to resolve at their first implementation boundary

Recommendations below are for adoption review, not silent changes to canon.
Do not stop all work until every future social policy is settled.

| Decision | Recommended starting position | What it gates | What can proceed without it |
| --- | --- | --- | --- |
| [Friends audience](friends-audience-decision-proposal-2026-09-07.md) | One mutual connection; deliberate sharing to selected eligible recipients. Resolve and bind the audience at Send; later connections do not gain old material. No second Friends-membership invitation | Wider Friends publishing and reusable selection defaults | Existing explicitly addressed/account-based authority and original-reader mapping |
| [Connection and controls](ongoing-connection-default-decision-proposal-2026-09-07.md) | Reuse pair circles; optional request/accept, no post-photo nag. Mute, disconnect, block and report are separate. Recommend disconnect ends future contact eligibility while previously valid shares follow their own grants; block closes prohibited Vesper access/contact immediately | Consumer connection exposure and consistent restrictions; exact old-share/block semantics still need ratification | Current membership/capability tests and a cross-entry-point enforcement map |
| [Guest identity](guest-identity-and-delivery-decision-proposal-2026-09-07.md) | Safe account-free preview; establish recipient identity at the first attributed/sensitive boundary. Prefer one reusable verification step for the bounded session, not a code for every action. Do not require full app adoption | Attributed non-account RSVP, private address/constraint, later delivery and eventual linking | Existing account-based Occasion path, safe preview design, transport and principal mapping |
| [Friend-source use](scoped-source-use-grant-decision-proposal-2026-09-07.md) | Separate original display, independent world help and permissioned composition. Prefer an explicitly understood reusable narrow agreement over a per-post questionnaire; do not infer it from friendship. Immediate use and automated later composition remain distinct scopes | New recipient-source AI use, source-dependent retention and proactive composition not already authorized | Original enjoyment and independently sourced world information; any existing genuinely authorized narrow path |

Also reconcile—but do not invent new policy for—affected people in photographs,
private-address precision, guest link forwarding, existing source retention and
the separate generated-piece Keep/history proposals. A social source cannot
bypass those contracts because it is useful. Saving generated pieces is not a
prerequisite for receiving or refinding an independently authorized original.

## 5. Work packages

### S0 — agree the concrete owner and state contracts

**Outcome:** implementation can proceed without duplicate owners or contradictory
guest, arrival and source-use promises. Relative size: small, investigative.

1. Rebase the capability map against the selected integrated HEADs, actual
   flags and active dirty work. Mark each route: landed, isolated, gated,
   missing, or end-to-end verified. Ask lane owners for a clean tested cut.
2. Map source-backed human sharing to existing Source and relationship writers:
   what the current handoff can carry unchanged, what needs a versioned extension,
   and whether a narrow companion record is justified. Compare migration and
   caller costs; name the chosen writer, reader and deletion owner.
3. Ratify the decisions needed for S1/S2. Specify grant acquisition—not only a
   permissive enum default—and supported object kinds, selected components,
   audience binding, current-reader checks and bounded fan-out.
4. Define the guest capability/principal mapping and the arrangement-versus-
   participation state matrix needed for S3/S4. A proposed shape may remain
   behind a decision gate while existing-account work proceeds.
5. Turn design A/B/C into executable scenario requirements, including sparse
   social supply, non-spatial sharing and the unresolved 03.7 arrival correction.
   Board 06's remaining “only Sam” note and inconsistent fixture clocks are
   editorial fixes, not another exploration assignment.

**Deliverable:** append a versioned execution matrix to this doc, with exact
owner paths, contracts, accepted/pending decisions and first commit boundaries.
Do not create a packet per noun. Schema/model changes still require the repo's
explicit approval boundary before implementation.

**Checkpoint 0:** no unresolved choice is hidden in code defaults; no route
depends on a fabricated Trip, account, place, read receipt or authority grant.

### S1 — trusted sharing and connection foundations

**Outcome:** people can deliberately make the selected material available to the
right people, with usable control afterward. Relative size: large; split into
source/audience, contact controls and cross-owner repair commits.

**Backend**

1. Reuse source custody and contribution admission. Add only the S0-approved
   sharing mapping. Cover a place note, selected photo, and non-photo object;
   place context is optional where the object has none. Sending a selection
   must not expose the whole conversation, album or private source container.
2. Preserve author, subject restrictions, object identity, effective audience,
   permitted use and lifecycle. Bind at authorized Send, make retries
   idempotent, and revalidate audience/source/control state at commit and read.
   Friends selection does not become a new relationship invitation.
3. Keep source-owner and share-owner changes coherent using existing transaction
   or outbox boundaries. Model pending/failed delivery truthfully; do not report
   “sent” merely because a preparation row exists. External delivery may fail
   per recipient without replaying successful deliveries.
4. Adapt pair request/accept/decline/leave to the agreed connection meaning.
   Avoid user-entered pair names, duplicate pair identities and follow-based
   substitutions. Make pending, ignored and disconnected states uneventful.
5. Enforce mute/notification choices separately from block. Apply the block
   contract across share creation, reads, invitations, pair messages, context
   resolution and known-identity capability access. Audit applicable legacy
   paths too; hiding the new card is not enforcement.
6. Give reporting an honest authorized payload, recipient and operational
   handling path. Reuse existing report transport where suitable; do not treat
   `accepted=True` plus best-effort forwarding as a reviewed abuse workflow.
   Add proportionate spam/rate/attachment limits before public exposure.
7. Propagate withdrawal/expiry through original readers, root candidates,
   source-dependent derivatives and Life projections. Preserve independent
   records; use owner revision fences to prevent resurrection by late work.

**Mobile / bounded web**

- Extend existing share/intake and object actions with one legible selection,
  audience and Send boundary. Keep Chat's shell/composer otherwise unchanged.
- Put Edit/Withdraw and the appropriate person controls on contextual menus;
  no social-maintenance dashboard and no per-share five-axis questionnaire.
- Ensure account switching and logout remove cached recipient content and
  pending commands. An interrupted send can recover without duplicate posting.

**Acceptance:** selected parts only; no inferred new audience; source-owner
withdrawal wins over delayed delivery; duplicate Send produces one effect;
block and mute differ; no passive view/Keep/dwell information is shown to the
author. Test preserved old grants and revoked grants as different cases under
the adopted policy. Include people pictured who are not the uploader.

**Gate:** new social exposure requires its applicable controls and repair path;
they are not deferred until after wider sharing ships. S2 development can run
against these agreed contracts before all S1 exposure gates are satisfied.

### S2 — deliver original human value through the four-root experience

**Outcome:** a share is worth receiving and opens the actual thing, not a generic
conversation or explanatory report. Relative size: medium–large.

**Backend**

1. Extend the merged Home/Places receiver path, not a new feed service. Produce
   safe viewer-relative projections from original/share owners, with semantic
   revision, authorship, exact destination and current eligibility.
2. Establish one canonical original-object read path across compact and full
   presentations. Revalidate source and grant on direct/deep-link reads; don't
   trust a root card cached before withdrawal.
3. Support selected photo, authored text, place, and non-photo object references
   using existing media readers where possible. A map can open the actual map;
   an article opens the eligible article or external original. Sharing a URL
   does not authorize copying a paywalled article or arbitrary remote content.
4. Wire human Reply and private Ask separately. Reply addresses a known person
   with explicit context; Ask stays private and consumes only effective sources.
   Receive the active `handoff_entry`/seed work from its owner after review;
   don't duplicate it or broaden it to attachments by implication.
5. Offer independent useful world depth immediately—venue context, a meaningful
   comparison, hours relevant to a contemplated visit—from Content/world owners.
   Clearly separate that material from the friend's voice and endorsement.

**Surface behavior**

| Surface | Concrete implementation responsibility |
| --- | --- |
| Home | Directed material and shared consequences inside the object they change; conditional `Addressed to you` region under the accepted timing/deduplication rules. No response demand on every share. Preserve substantial non-social value |
| Places | `From friends` over the same world map/field, using intentional authored sharing and author-chosen precision; generous but finite browsing, sparse/empty states and return to independent world value. Not a live friend tracker or saved-place exhaust feed |
| Chat | Two clear intentions: Reply to Maya versus Ask Vesper privately. Preserve exact subject, recipient and origin on entry/return without redesigning the clean Chat root |
| Life | Eligible original/share references, indexed by the proper person/object context; no extra save required merely to look. S5 adds the richer continuity/organization closure |

Casual non-spatial Status retains its accepted Home doorway while featured and
Life People context afterward. Ordinary casual spatial shares are not copied
into a second full social field on Home. Nor is “one social ask” a limit of one
piece of human material across the whole page.

**Mobile deliverables:** shared original-reader behavior, compact/full variants,
contextual Reply/Ask, real empty/unavailable/withdrawn states, exact return and
cross-account teardown. Reuse composition, entity and media primitives rather
than require a universal card or one new screen per content kind.

**Checkpoint 1 — everyday social value:** a sender and recipient can complete
A using original material, plus independently sourced help, with no Occasion,
generation requirement, reciprocal upload or connection nag. Verify from owner
rows through actual API and mobile consumers; presentation-only fixtures are
insufficient. An arrival confirmation, reaction or reply remains optional where
it is not genuinely needed for a real consequence.

### S3 — bounded participation, invitations and remote contributions

**Outcome:** organizing, attending and contributing can involve different people
with different effort and access. Relative size: large/high uncertainty for the
non-account path; existing-account behavior is not a blank slate.

**Backend**

1. Reuse canonical Occasion/invitation commands and current account-based reads.
   Preserve invitation, roster, contribution and arrangement ownership; do not
   fork a separate dinner/guest Occasion store.
2. Implement the adopted guest-principal/capability mapping. Reuse token,
   expiry, revocation and delivery foundations without forcing full Trip
   membership or faking a registered user. Keep delivery target separate from
   verified identity. Account linking, if included, must be explicit and safe
   against recycled/wrong contacts and history resurrection.
3. Serve host-approved safe preview separately from private address, named
   roster, private constraints and contributor actions. Prevent sensitive data
   in link previews, URLs, analytics, public caches and notification payloads.
4. If using the proposed verification design, one bounded session can confirm
   identity for its allowed actions. An unverified RSVP remains provisional;
   don't present it to the host as verified Sam. Test expired sessions, failed
   delivery, forwarded links and retries. No new verification vendor is assumed.
5. Make guest answers and constraints minimal owner-bound commands. A private
   timing constraint can affect feasibility without appearing in group text.
   Guests can correct their own contributions without arrangement-edit rights.
6. Give Dana a contributor-scoped entry and readback: she can send her own tip,
   photograph or recipe to the allowed audience, with no attendance, address or
   unrelated history access. Do not make Nora retype it on Dana's behalf.
7. Deliver later material under the author's separate grant. Closing dinner or
   revoking an invitation does not magically decide every photograph's rights.
   A revoked invitation token cannot serve as an otherwise-invalid media grant.

**Mobile/web deliverables:** one capability-aware guest destination with states
for preview, answer, relevant arrival facts and later authorized material; host
readback and contributor entry in the existing Occasion experience. These are
states of a bounded journey, not a separate onboarding product.

**Acceptance:** no-account value without account adoption; one effortful host
does not create homework for guests; remote contributor stays non-attending;
wrong recipient cannot obtain the home address; provisional, confirmed and
declined answers remain distinct; no automatic ongoing connection.

### S4 — connect the live engine to shared life, not just trip operations

**Outcome:** when something changes, Vesper helps preserve the purpose of getting
together and communicates only the useful consequences. Relative size: large;
coordinate with Integration's practical-judgment package rather than fork it.

1. Follow the [live-engine owner-path matrix](live-engine-owner-path-matrix-2026-09-05.md): current world facts, movement, explicit participant windows,
   Plan/Commitment state and valid private constraints feed bounded assessment.
   A private input may shape feasibility but is not a public explanation.
2. Complete fresh feasible option supply into existing shared Plan repair.
   Show concrete choices and relevant tradeoffs; do not require every member to
   poll, rate or resubmit preferences. No-change, let-someone-join-later and
   abandon-this-option are legitimate results.
3. Apply only through the canonical owner command under current authority.
   Recheck Plan, roster, grants and protected Commitments at execution. Use the
   accepted owner-controls-editing policy; scoped collaborative edits need no
   redundant owner approval, but cannot rewrite another person's acceptance.
4. Reproject authoritative changed state to everyone affected: Nora, Maya and
   Sam in the fixture. Tailor detail to permitted context. Dana's unrelated
   contribution does not require a notification simply because dinner changed.
5. Preserve current arrangement versus personal participation through preview,
   owner adoption, pending affected-person response and arrival. Reject the
   design's unconfirmed “expected around eight” claim (§3.2).
6. Use existing invalidation/recovery and attention gates. Push is an optional,
   justified interruption that points to current truth, not a second state store.
   Explicit refresh/current assessment does not authorize a general background
   watch or continuous location tracking.
7. Exercise the same architecture for a non-trip local outing and a travel
   specialization. Keep the examples as fixtures, not runtime founder-specific
   classes or separate engines.

**Checkpoint 2 — easier together:** the B experience works across host, attendee
and remote contributor, including a changed arrangement and an offline gap.
Participants know what matters without reading a workflow log. Missing practical
facts produce an honest limitation, not invented certainty or a new form.

### S5 — shared originals and plural continuity in Life

**Outcome:** “the photo Maya sent from dinner” and “something we'd like to do
again” reconnect to the actual eligible objects. Relative size: medium–large,
dependent on a tested Life owner/read contract rather than all Life cutover.

1. Provide Life with content-free owner-change events and an authorized exact
   reader for the selected social source/share owners. Preserve author,
   contributor, viewer, source/share revisions, purpose, represented time/place
   and containment. Do not smuggle content or wider authority through an index.
2. Reconcile with the Life lane's evidence envelope and organization invariants.
   A dinner photo can be contained in a record without proving that everyone in
   the picture attended, enjoyed dinner or acquired a shared preference.
   Private Outcomes remain private and may disagree.
3. Support exact original retrieval first through the appropriate current reader;
   add indexed Time/People/Place navigation on the Life lane's certified cut.
   Do not add a social-only media archive to bypass unresolved index work.
4. Preserve legitimate access without unnecessary re-saving, while distinguishing
   eligible refinding from a recipient-owned permanent copy. Guest display uses
   the currently valid author grant and verified session/capability, not an extra
   Keep or connection requirement.
5. Enforce correction and revocation across cached views, search results,
   organization, thumbnails and dependent prepared content. Withdraw a revoked
   Paris note without deleting an independent dinner photograph or boat record.
   Test delayed old events after revocation and after explicit restoration.
6. A later invitation is a new prospective action: preserve useful place/people
   context, check its current eligibility, but reset new participation and
   time-specific constraints. A prepared suggestion is not a persisted Plan
   or an invitation already sent. Apply the pre-Plan retention decision only if
   adopted; do not quietly save drafts under a social label.

**Checkpoint 3 — continuity without maintenance:** C works after restart and
after a material source change. The boat remains its own record, the next pasta
evening needs fresh acceptance, and nobody must file an album or complete a
reflection questionnaire. Organization exclusions survive migration and replay.

### S6 — permissioned social intelligence and meaningful openings

**Outcome:** another person's perspective makes the product more useful than
the same public recommendation with their avatar attached. Relative size: large
if new automated-use scope is needed; original and independent value are already
part of S2 and should not wait for this package.

1. Use the existing Content and live-engine owners. Share preparation, publishing
   originals and generating recipient-specific material are different jobs;
   do not make the private Source-contribution worker their universal writer.
2. For each composition name the actual added value: a friend's contrasting
   experience, a useful detail that changes the route, or an applicable idea for
   a future gathering. Preserve the source and author rather than paraphrase
   what the user already knows. No personality or friendship diagnosis.
3. Admit friend-owned sources only under current purpose, consumer, retention,
   inference and audience rights. Review whether any existing `contextual_only`
   value reflects effective author permission; a model/API default is not proof
   that a person knowingly granted a broader use.
4. Apply the adopted distinction between an immediate private question and
   later Home/Places composition. No hidden durable answer or quoted question
   under an immediate-only grant. Retention needs its own authority; independent
   recomputation is valid only when the result truly stops depending on the
   restricted source.
5. Recheck queued/in-flight context and publication/read eligibility after
   withdrawal, expiry, blocked contact or correction. Use exact dependency
   lineage to preserve independent value without leaking a paraphrase.
6. Keep common world supply reusable, originals inexpensive and personalized
   generation selective. Root reads do not call providers. Use bounded producers,
   deadlines, deduplication and semantic/source revisions; measure actual costs
   rather than impose a speculative per-person daily generation schedule.

**Checkpoint 4:** in the same product, someone can enjoy an original with no
model call, get useful independent world help, and receive a genuinely better
permissioned connection where supported. Demonstrate added substance, not only
successful grant validation. Broader automation can remain gated without
misrepresenting the first two experiences as unfinished.

### S7 — integrated evidence, exposure and selective pruning

**Outcome:** the portfolio works on a combined candidate and unsupported legacy
paths no longer contradict it. This work starts with S1 and closes the rollout;
it is not a testing phase deferred until everything is built.

- Maintain connected regression cases as each owner changes; test sender,
  recipient, host, non-account guest, remote contributor and uninvolved person.
- Reconcile flags by capability: sharing, original reading, friends field,
  bounded guest actions, Life reader and source-based AI composition. Avoid one
  giant “social enabled” switch, while also avoiding a permanent matrix of
  redundant flags. Record supported combinations and kill-switch behavior.
- Promote a combined local candidate before internal exposure; record native
  two-person/device and bounded-web evidence separately from API/Jest fixtures.
- Review existing follow/feed, integer-place handoff, group room and Trip invite
  consumers. Retire only paths actually superseded, with caller/data/contract
  evidence and rollback. Trip collaboration can remain a valid specialization.
- Recheck the working design against real media, sparse supply, text scaling,
  image loading, keyboard, back navigation and failed delivery. Design changes
  should be localized to an observed problem, not another root redesign.

**Release gate:** explicit exposure authorization, adopted relevant policies,
tested data/migration recovery, functional controls and support/report handling,
measured runtime bounds, and no known high-priority cross-user correctness bug.
“Merged,” “enabled,” “native-evidenced” and “released” must remain separate claims.

## 6. Dependency order and how to execute without bottlenecking

| Package | Hard dependencies | Work that can overlap |
| --- | --- | --- |
| S0 contracts | Current code/design/canon audit | Existing Integration, Content and Life work continues |
| S1 sharing/control | S0 owner mapping and the particular adopted audience/control decisions | S2 receiving fixtures and components against agreed interfaces |
| S2 original receiving | S1 readers/audience/repair for real exposure; merged Home baseline | S3 account-based participation and independent world supply |
| S3 guest/contributor | Canonical Occasion ownership; S1 applicable controls; adopted guest policy for non-account access | S4 practical option-supply work can use existing accounts |
| S4 live adaptation | Current Plan/Commitment authority, relevant S3 participation semantics, Integration practical suppliers | S5 Life owner-reader/event contract and retrieval work |
| S5 continuity | S1 source/share lifecycle; selected tested Life interfaces; S3 identity only for guest access | Basic account-based refinding belongs in the first connected sharing delivery alongside S2, not after all S3/S4 work |
| S6 source-based intelligence | Actual effective use grants, dependency repair, Content/Integration consumer contracts | Original and independent-world value already available through S2 |
| S7 portfolio and pruning | Each capability's closure, not a blanket prerequisite for all development | Continuous verification throughout S1–S6 |

**Recommended next implementation batch after S0:** S1's selected-source and
named-recipient owner mapping, corresponding controls/withdrawal, S2's original
reader and Home/Places receiving, and S5's basic account-based Life refinding.
Exercise photo, place note and one non-photo object together. §10 specifies
commit boundaries and acceptance. This establishes shared contracts used by
every subsequent experience; it is not “prove one behavior loop before designing
the system.” Guest/practical contract work can proceed independently once those
interfaces are stable; it need not delay ordinary account-based sharing.

Keep at most two substantive social implementation packets active at once:

- **Sharing/receiving:** S1/S2, later S5/S6 integrations.
- **Participation/practical:** S3/S4 against the same identity/source contracts.

These are suggested bounded packets inside existing ownership, not a request to
spawn two permanent agents or establish a new integration hierarchy. Integration
owns shared landing; lane owners can implement and test independently against a
versioned seam. Serialize changes to shared models, generated schemas and the
same owner files. Use isolated worktrees when overlap cannot be avoided.

Do not promise a calendar completion date from this planning pass. Guest identity,
multi-recipient sharing and effective cross-user grants have meaningful contract
uncertainty. Estimate reviewable commits after S0, then revise the remaining
effort at each checkpoint using actual rework and integration evidence.

### Review questions at every checkpoint

1. Does a person receive something useful without maintaining the system?
2. Is another participant quietly doing extra work to make that possible?
3. Is this still one four-root product, or have we created a social sub-app?
4. Did a new record duplicate an existing owner, or close a demonstrated gap?
5. Do original, independent and source-dependent value remain distinguishable?
6. Are we blocked on a true policy/owner dependency, or merely waiting for an
   unrelated lane to finish everything?
7. What can we remove now that the replacement actually works?

Revisit the approach if guest verification becomes repeated onboarding, casual
sharing requires an Occasion, source selection becomes filing homework, Home
becomes an inbox, or accurate shared state requires everyone to open the app.

## 7. Validation and evidence plan

### Required portfolio

| Case | Essential checks |
| --- | --- |
| Direct ordinary share | Select only intended material; exact author and recipient; real original reader; no automatic private Keep or AI prelude |
| Friends field | Rich, sparse and empty supply; author-selected precision; new connection excluded from old shares; no synthetic activity |
| Reply versus Ask | Correct recipient/channel; Ask unavailable or independently sourced when rights are absent; no source attachment escalation |
| Control changes | Ambient mute versus direct interruption; disconnect versus old grants; block at creation/read/action and known guest paths |
| Guest/remote contribution | Safe preview; wrong/forwarded contact; provisional versus verified answer; contributor not attendee; own-material correction |
| Shared change | No adoption, owner adoption, stale command, changed personal window, no response, decline; each relevant observer sees current permitted truth |
| Later retrieval | Same original after restart; guest access without forced contribution; independent dinner/boat records; no automatic future participation |
| Repair race | Withdrawal before worker start, during production, before publication, after delivery and against stale replay; no resurrection |
| Little/no social context | App is useful with zero friends, one contribution and no response; no invitation debt or fabricated personalization |

### Test layers

1. **Unit/contract:** contribution policy, social circles, relationship handoffs,
   graph invitations, live repair, reader/DTO and root-navigation suites. Existing
   tests are starting points, not proof of the whole portfolio.
2. **Connected PostgreSQL/API:** real owner rows, authenticated commands, outbox,
   readers and correction. Exercise migration on populated historical records.
   Synchronize actual races when claiming concurrency protection; a sequential
   stale replay is a different test.
3. **Cross-repo contract:** after backend API/model changes run workspace
   `./scripts/sync-types.sh`; review full OpenAPI, app projection and generated
   types, typecheck and method-aware operation coverage. No hand-maintained
   backend DTO copies or new dark operation exposed accidentally.
4. **Native and guest web:** use the app's registered surface QA and isolated
   design references; two-account/two-device walkthrough where relevant; phone
   browser for the bounded guest route. A mocked export is not native evidence.
5. **Operational:** measure fan-out, media access/caching, delivery retries,
   revocation propagation and provider/model calls. Never use generation on
   scroll or permanent location observation to make fixtures appear lively.

Every execution receipt names exact HEAD, flags, fixture or real-data boundary,
commands/results, failing or skipped checks, migrations and rollback. Keep test
counts from separate/overlapping lane runs separate. Protect raw contact data,
private constraints, source text and tokens in tests, logs and analytics.

### Product and cost evidence—not engagement targets

Measure task completion and friction for sending/receiving, successful retrieval,
understood audience, failed/duplicate deliveries, stale shared readback, repair
latency, native readability and bounded cost. Evaluate substantive usefulness
with occasional consented walkthroughs, not routine after-action questions.

Do not optimize equal posting, reply speed, daily activity, streaks, read ratios
or human-message volume. Private operational telemetry must not become a sender's
viewer list or relationship score. Offline gathering can be supported without
claiming attendance from a link tap or tracking where people went.

## 8. Next action and completion ledger

**Next: reconcile the reviewed branch-local batch, close the specific S0
decisions in §10.3, then authorize the connected S1/S2/basic-S5 packet.** Receive
Integration's existing note/seed work and Life's tested contract; don't rebuild
either. No further broad social design exploration is needed before mapping.

S0 is not marked complete merely because this roadmap exists: exact general
sharing persistence, effective grant acquisition and the policy rulings still
need owner review. Record rulings in the existing four proposals and promote
accepted durable semantics through the normal decision/contract path. Avoid
adding a second set of strategy documents.

| Package | Current planning status after the first bounded batch | Evidence needed to advance |
| --- | --- | --- |
| S0 | Planned; source/code mapping partially established above | Agreed owner/API/event mapping and scoped decision disposition |
| S1 | Pair/place dismissal and withdrawal improved on isolated branches; general sharing/control contract still planned | Connected selected-source/audience/control/withdrawal evidence |
| S2 | Home note receiving partly integrated; exact Places identity improved on isolated branches; broader original receiving planned | Actual multi-medium original-reader and four-root sender/recipient path |
| S3 | Existing account-based substrate; guest/contributor completion planned | Adopted guest mapping and bounded participation tests |
| S4 | Existing proposal-only engine substrate; connected behavior planned | Fresh options, canonical adoption and truthful affected-person readback |
| S5 | Existing owner projections plus unmerged Life work; social continuity planned | Tested Life interface, shared refinding and correction/replay evidence |
| S6 | Existing Content and scoped-use foundations; broader policy-gated work planned | Effective grants, substantive added value and all-consumer repair |
| S7 | Continuous obligation; not certified here | Combined candidate, native/web/operational evidence and authorized exposure |

## 9. Execution ledger — September 7, 2026

This ledger records the first implementation batch after the roadmap was
written. These commits are on isolated `codex/social-implementation-2026-09-07`
branches in the two child repositories; they have not been merged or pushed by
this planning thread. Contract snapshots are committed in the workspace root.

| Slice | Backend evidence | Mobile / contract evidence | State |
| --- | --- | --- | --- |
| Low-pressure recipient dismissal | `7159a74a4` adds `place_handoff.dismiss.v1`, binds it to the existing recipient-authorized terminal transition, and keeps legacy `Keep` action resolution compatible | `91995b4f8` adds the UUID action type, quiet terminal copy, cache invalidation and no receipt publication; workspace snapshots in `d3b6bc1` | Landed on isolated branches; focused backend 37 tests and mobile 14 tests passed |
| Exact friend-place doorway | `f9ce20f63` preserves bounded `venue_ids` aligned with friend place names and returns exact IDs from the existing Places query; snapshot `55f2bcb` | `894dfb6b8` makes only verified venue thumbnails open the canonical venue route and adds a profile doorway; legacy name-only rows remain informational | Landed on isolated branches; backend social-section tests (72) and mobile Places tests (47) passed |
| Sender withdrawal affordance | Existing sender-authorized `revoke` transition is reused; no new authority or route | `8cf8f82e9` adds local “Take it back”; `44e9d00e8` subsequently refreshes owner revision, bounds conflict retry and scopes the local control to its entity | Landed on isolated mobile branch; not a durable sender history/control surface |
| Revocation/expiry projection invariant | Existing Home adapter already rejects terminal and expired handoffs; no runtime change was needed | `4f4ed556c` makes the invariant explicit for Home projection tests (revoked and expired material both omitted) | Landed on isolated backend branch |
| Review corrections | `b7d98871c` filters unavailable legacy/UUID handoff messages from the recipient conversation-history route | `44e9d00e8` also repairs entity-people cache invalidation and generated enum ordering | Isolated tested cut; not certification of every original/context/search reader |

### What this batch establishes—and does not establish

The batch adds and tests bounded pair/place behavior: a recipient dismissal
without publishing a local consequence receipt, local sender withdrawal, and
profile/exact-venue doors where Places receives verified identity. Operational
action telemetry remains; “no social telemetry” was too broad a claim. The
Home terminal/expiry invariant and recipient Chat-history filtering have focused
coverage. The Places venue-save path is a separate Trip-peer reader, not proof
of a general authored-share lifecycle across Places.

The existing terminal `dismiss` also hides the addressed note from recipient
history. Do not equate that implementation with a future “clear from Home”
attention control; §10.3 calls for an explicit distinction before generalizing it.

It does **not** prove the full social portfolio. No multi-recipient audience,
selected-photo/non-spatial writer, non-account guest, remote contributor,
per-person mute/block policy, shared-object reader, scoped friend-source AI
composition, or live-engine participation path was introduced. Those remain
S0/S1–S6 work behind the decision and owner gates above. No Chat or Life root
redesign was made in this batch.

### Verification boundary

The final fix turn reported 218 backend tests (including four PostgreSQL tests),
78 mobile tests, TypeScript, generated-types checking and Ruff passing. These
are receipts for that isolated cut, not reruns during this planning pass, and
must not be added to the overlapping earlier slice counts. The new history-route
test uses mocked owner reads; existing database tests do not establish the entire
two-account journey. Backend commits required a size-budget hook skip; review
that debt, including added code in the large conversation route, before further
expansion. Native two-account, guest-web, full connected social-lifecycle and
operational fan-out evidence remain outstanding. “Committed on an isolated
branch” is not “merged,” “enabled,” or “released.”

The workspace `make contract-check` was also run after the snapshot commits.
Snapshot validation and the active mobile projection passed; the final compare
was intentionally against the separate dirty `travel-app` checkout on its
pre-social branch and therefore reported the two expected isolated-branch
differences (`handoff_action: dismiss` and `PlacesFriendActivity.venue_ids`).
That is the historical check context, not a current expected-failure waiver.
After receiving the reviewed branches, regenerate from the selected combined
backend and verify the matching mobile candidate. Other lanes have advanced
the workspace contract since these social commits; never overwrite their newer
operations with the old social snapshot.

Update this ledger as implementation lands; retain the design brief for intent
and the main roadmap for cross-system sequencing. Archive or renew this working
plan by October 7 rather than let it become another stale source of build truth.

## 10. Connected social execution plan — September 7 rebaseline

### 10.1 Outcome, scope and starting coordinates

**Next milestone: a person can share an existing piece of their world; another
person receives its actual value, can use it in the appropriate part of Vesper,
and can find it later while access remains valid. The sender can return and
control the share after the immediate sending session.**

This milestone includes the common contract, real mobile consumers, basic Life
continuity, contact controls and lifecycle repair. It is not a new social root,
an invitation-only product, or a temporary place-note experiment. Build against
all three A/B/C experiences; deliver the shared foundations before expanding
guest and practical capabilities that depend on them.

Planning inspection: workspace `80bf5c3`; backend primary main advanced through
`e65a06e01`; primary mobile `15b38e18f`. Social worktrees are clean at backend
`b7d98871c` and mobile `44e9d00e8`, both on
`codex/social-implementation-2026-09-07`, not merged into main at inspection.
Primary checkouts and workspace documents contain concurrent work. These are
inspection coordinates, not the next implementation's chosen merge base.

This revision inspected current code and documents. It did not rerun application
tests, launch a simulator, verify the design export visually, change code,
merge branches, or adopt the four policy proposals. Follow the current
[Integration roadmap](complete-system-integration-roadmap-2026-09-05.md),
especially its connected-value execution/receiving sections, for shared landing.

**Supported first portfolio:** a selected photograph, an authored place note,
and a non-spatial recipe represented by eligible text or an external-original
link. Include a send to one person and to several explicitly selected eligible
account recipients. These are coverage fixtures, not three new product modes.
A native map/collection can join when its existing owner supports an exact,
permissioned reader; do not claim arbitrary map sharing from the Trip-map URL
export. No public publishing or non-account delivery is included by implication.

### 10.2 Concrete owner mapping and architectural recommendation

Paths below are relative to a selected backend/mobile checkout. Reconcile
current primary and social-branch versions before editing shared files.

| Responsibility | Inspected reuse point | Next implementation responsibility |
| --- | --- | --- |
| Custody and selected material | Backend `core/db/intake_v2.py`, `core/db/intake_source_attachments.py`, `api/routes/intake.py`; existing `source_objects` | Retain only the selected material under the actual Share/Bring authority; resolve exact object/component identity. A private upload is not a recipient media grant. |
| Authored share and audience | Backend `domains/relationships/{models,schema,repository}.py`, `api/routes/relationship_handoffs.py` | Establish bounded general sharing within Relationships, coordinated with original custody; choose the schema at S0, not through client JSON defaults. |
| Connection and restrictions | Backend `core/db/social_circles.py`, social-circle models/routes; mobile `data/social.ts` | Reuse pair identity and current eligibility. Add only missing consumer controls/enforcement; no second Friends graph or mandatory pair name. |
| Current delivery and original destination | Backend `root_projection/v2/{home_portfolio,home_source_adapters}.py`; mobile `components/root-projection/`, `utils/rootProjectionNavigation.ts` | Extend the integrated exact-object receiving path to authorized human originals. Do not route every object to generic Chat or the generated-Source worker. |
| Places social supply | Backend `core/db/trip_save_suggestions.py::get_friend_shared_venue_activity`, `places/friends.py`; mobile `components/places/renderers/socialCard.tsx` | Preserve valid legacy specialization; add owner-authorized authored spatial supply independent of a Trip. Saving with explicit share opt-in is not the whole Friends experience. |
| Reply / private Ask | Backend `concierge/handoff_entry.py`; existing conversation routes; mobile `data/relationshipPlaceHandoffs.ts` and Chat entry/navigation | Receive Integration's revision-bound note resolver. Reply names a person; Ask names a private job. Neither expands attachment or source-use rights. |
| Durable retrieval | Backend `life_projection/{owner_contracts,owner_reads,current_authority,retained_source_projector}.py`; mobile `components/life/LifeRootV1Screen.tsx`, `app/you/life-record.tsx` | Supply a social owner adapter and exact reader to Life's tested path. On inspected main, `social_contribution` is explicitly `UNAVAILABLE`; changing that label alone cannot enable it. |
| Participation and adaptation | Backend `domains/experience_graph/`, invitation commands/routes, `lived_experience/adapters/shared_plan_repair.py` | Consume these same identities/material references, preserving canonical Occasion, Plan and Commitment mutations. No social-owned guest roster or second live engine. |

**Recommended persistence direction, subject to explicit schema review:** keep
original custody in Source or the existing original-object owner; place a
bounded share record and per-recipient delivery/access relations inside the
existing Relationships domain. A literal authored note may remain owned there;
do not duplicate it into Source and a message merely to satisfy a universal
shape. The share references the selected original/components and carries the
author's optional message, purpose and projection intent. It does not own the
underlying Place, Occasion, Plan, media library or human relationship.

Why prefer this direction:

- The current `PlaceHandoff` and prepared command require a world entity and
  conversation; the writer authorizes an exact pair. Adding nullable fields
  alone would leave pair, event, reader and action assumptions throughout it.
- A separate general SocialPost service would duplicate Source custody,
  audience checks, notification delivery and Life ownership.
- A narrow Relationships extension can reuse identity/authority and transport
  while keeping PlaceHandoff a supported specialization. Existing Trip story,
  map and Atlas public-share mechanisms are reuse candidates for rendering or
  delivery only; their public-link authority and statistics are not Friends
  semantics.

At S0, compare the actual migrations and callers for a versioned extension
versus a companion share/recipient representation. Record the chosen tables,
constraints, routes and owner transaction before code. Do not make legacy
PlaceHandoff records masquerade as the new type or perform dual canonical
writes. Any eventual migration needs an explicit compatibility adapter, history
mapping, rollback and consumer inventory; it is not prerequisite to replacing
new general-share creation.

**Required logical contract (field names are not an approved wire schema):**

| Dimension | Required semantics |
| --- | --- |
| Identity | Stable share ID; original owner/kind/ID; selected component IDs; author and relevant subjects; optional actual Place/Occasion context. No invented context to satisfy a schema. |
| Revision | Separate original content, share/audience and recipient-delivery/attention revisions as needed. Opening an item must not make its author's content edit inherently stale. |
| Scope | Effective audience bound at Send; permitted display/use; source custody and subject restrictions; projection intent such as addressed versus ambient. Equal recipients do not imply equal interruption. |
| Recipient relation | One bounded, idempotent delivery result per recipient; current access and reader reference. A multi-recipient share need not create a group conversation or reveal every recipient to the others. |
| Lifecycle | Current source and grant validity; semantic expiry; withdrawal and explicit restoration where supported. End of relevance is not necessarily end of original access. |
| Navigation | Exact authorized original/action reference; viewer/account scope; origin root and return context. Never send raw media bytes or bearer credentials in route parameters. |
| Events | Durable, content-free identity/revision/change envelopes; causal references; affected consumer/recipient scope, including former recipients for repair. Reuse existing outbox/delivery conventions. |

One server-owned reader policy must be used wherever original content is
exposed. The sender's control read and recipient's content read are different
views; a participant-only row lookup returning the whole object is not the
complete current-authority policy.

### 10.3 Decision register — resolve only what the next capability needs

The following are **recommendations for approval**, not amendments made by this
roadmap. Record adopted semantics in the existing proposals and owning contract;
do not create a second policy vocabulary in implementation comments.

| Decision | Recommended ruling | Required before / independent work |
| --- | --- | --- |
| General-share owner and supported kinds | Source/original custody plus bounded Relationships share/recipient records; first kinds in §10.1 | Shared model/table changes. Existing reader audit and fixture construction can proceed. |
| First audience | Explicitly selected eligible account recipients, one or several; freeze at Send; no automatic public/follower audience. Friends is an understandable selector, not a second invitation | New writer and audience projection. Do not require a global “all friends” default to begin. |
| End of connection versus old shares | Disconnect ends new contact eligibility; existing originals follow their own grants. Block closes the applicable contact/read paths without erasing independent originals | Wider social exposure and contact controls. Exact behavior across messages, invitations and known-identity links must be specified. |
| Clear versus release | Clearing a Home unit should change attention only; it should not destroy otherwise eligible Life retrieval. Giving up access, deleting one's reference and author withdrawal are separate effects | Generalizing `dismiss`. Preserve existing terminal note semantics until an approved migration; do not silently reinterpret old events. |
| Edit and recipient changes | Ordinary edits can update an author's message under content revision. Replacing selected originals or adding recipients is a fresh explicit audience consequence; no silent attachment substitution | Edit controls. Sender withdrawal remains independently useful and should not wait for rich editing. |
| Consumer source use | Original display first; independent world information available without using restricted human content. Use friend material in AI only under an effective, understood, purpose-specific grant | Broadening the existing note-only Ask or adding source-dependent composition. No blanket `contextual_only` default as consent. |
| Guest and non-attending contribution | Use canonical Occasion capabilities; recommend bounded identity verification at the first sensitive/attributed boundary with a reusable session | S3 non-account actions. Existing-account sharing and practical work continue without waiting for a verification vendor. |

The existing [audience](friends-audience-decision-proposal-2026-09-07.md),
[connection](ongoing-connection-default-decision-proposal-2026-09-07.md),
[source-use](scoped-source-use-grant-decision-proposal-2026-09-07.md) and
[guest](guest-identity-and-delivery-decision-proposal-2026-09-07.md) proposals
remain the decision locations. Include clear-versus-release in the attention/
connection and reader contract review. Reply-only versus a voluntary private
acknowledgment need not block this batch: keep Reply usable, do not build a
reaction/count service, and retain the acknowledgment choice as unresolved.

### 10.4 Implementation sequence and reviewable commit boundaries

These stages refine S0–S7; they are not independent services or new agent lanes.
Sizes are relative scope/risk, not calendar promises.

#### First — reconcile the existing cut (S0 / S7; small–medium)

1. Record the current social commits, actual Integration/Entity receiving
   base, Life contract cut and feature flags. Distinguish primary checkout
   state from main and from the combined candidate.
2. Audit read coverage before adopting the withdrawal claim: exact handoff
   GET, conversation history, conversation list/preview/search, contextual Ask,
   Home, entity people lines, Places and any cached media. The new history
   filter runs after message pagination; test a page filled by hidden notes
   followed by eligible older messages. This is a verification target, not a
   claim that the latest fixes establish all-reader repair.
   Put reusable read policy in its owning module rather than further growing
   the oversized conversation route. No blanket hook skip or unrelated cleanup
   is an accepted completion strategy.
3. Test current revision/retry/navigation fixes against real owner rows and
   mobile consumers. Inspect pending-state cleanup on navigation/account
   change and ambiguous network completion, not only successful responses.
4. Integration receives the tested cut in its candidate; run contract sync
   there, preserving newer Source operations. Do not overwrite the primary
   dirty mobile checkout or force a branch change underneath another session.

**Commit boundary:** targeted remaining defects/tests if established, then
updated branch/contract receipt. Merge/push/activation remain separately
authorized actions. **Exit:** one known baseline and honest remaining gaps,
not a repository-wide cleanup or a declaration that social is complete.

#### Second — settle the general sharing contract (S0; medium, decision-bearing)

1. Complete the §10.2 storage/caller comparison; settle the first five §10.3
   rulings and exact constraints/operations. Specify original read, sender
   enumeration, send/recovery, edit/withdraw, recipient clear and access checks.
2. Define fixture actors and data from the existing shared fixture world.
   Include excluded and later-connected people; preserve boat versus dinner
   separation. Add the three media cases to that fixture rather than inventing
   a second incompatible social world.
3. Agree the owner event/read interface with Life and the semantic destination
   interface with Integration. Specify failure, absent/tombstoned source,
   delayed delivery, cursor, account switch and revision behavior before APIs.
4. Obtain explicit approval for shared models/tables and pending policy changes
   under repo rules. No code default should make that decision on the user's
   behalf. Design only missing states in the existing project; no new round
   of full-scroll compositions.

**Commit boundary:** approved decision/contract updates plus schema/API/test
plan. **Checkpoint A:** photo, place note and recipe fit without mandatory
Trip, Place, group room, AI use or recipient maintenance. If not, revisit the
contract before building consumers.

#### Third — implement selected sending and current original reads (S1; large)

1. Implement approved persistence/migration through existing owners. Enforce
   unique author request identity, source selection, per-recipient eligibility,
   content/audience revisions and transactionally durable delivery intent.
   Bound fan-out and attachment sizes; record actual chosen limits in the
   execution receipt rather than deriving product limits from fixture counts.
2. Establish a canonical safe reader for the selected original and its media.
   Use current source/share/control state, including direct URL/thumbnail
   access. Preserve author and optional caption; do not substitute an AI
   synopsis. Scrub unintended EXIF/location and inherited album/private context
   from the recipient representation where applicable.
3. Support exact send-result recovery after an uncertain response/restart.
   Retry the same operation, not a fresh share; expose per-recipient failure
   without resending to successful recipients. “Sent” means owner-accepted
   recipient availability, not a preparation row or proof of reading. External
   channel delivery, when added, must have its own truthful status.
4. Implement durable sender enumeration and contextual withdrawal; add bounded
   edit under the adopted rule. The sender sees their material, selected
   audience and technical failure recovery, not recipient views/Keep/dwell or
   the recipient's private attention state.
5. Emit the source/share change contract at every relevant mutation. Recheck
   withdrawal before late delivery and fail closed at read even if projection
   cleanup is delayed. Independent custody follows its own owner.

**Commit boundaries:** persistence/migration tests → authorized original and
media readers → idempotent send/recovery/outbox → sender controls. Each API
change includes backend tests, workspace OpenAPI/projection and generated mobile
types; do not hand-maintain duplicate TypeScript models. Include migration on
populated legacy data, one Alembic head and rollback/recovery evidence.

#### Fourth — connect the native send/receive experience (S1 / S2; large)

1. Reuse existing object/share/intake entry points. One selection, understandable
   audience and Send boundary; sending an existing photo does not require an
   AI conversation. No public-looking composer or forced caption. Add missing
   server access through `data/`, with generated contracts and real/mock parity.
   An OS share into Vesper remains private Bring under the contribution contract;
   it must not publish to friends. Sharing outward is a separately intended
   audience consequence, even when the same component handles source selection.
2. Route compact presentations to one logical original destination with
   medium-specific rendering. Reuse entity, image, text and link primitives;
   shared reader behavior need not mean one universal visual card or a new
   screen family per type. Unavailable media must not fall back to stale bytes.
3. Make human Reply and private Ask separate, contextual continuations. Open a
   pair conversation only when an authorized reply/contact needs it. Do not
   create a group thread solely because several people received the same item.
   A private question may use independent place facts without loading the
   friend's restricted photo or text; explain unavailability briefly when needed.
4. Connect Home and Places with the exact placement rules in §10.5. The recipient
   can consume the original and leave without a task list, Keep, reply prompt,
   connection solicitation or generated interpretation. Preserve the sender's
   entry/return context and stable controls after reopening the item.

**Commit boundaries:** share entry and result recovery → original renderer and
navigation → contextual Reply/Ask → Home/Places adapters. Backend/API integration
and two-account tests accompany consumer work; mocked cards alone do not pass.

#### Fifth — close basic continuity and trust with that same delivery (S1 / S5 / S7; large)

This is part of the first connected milestone, not optional work deferred until
after guests, advanced AI or the whole Life redesign.

1. Social supplies original/share enumeration, current read authorization,
   semantic revisions and content-free events. Life owns its adapter, index,
   grouping, exclusion and rebuild behavior on the reviewed Life cut. Do not
   enable `social_contribution` by changing its capability declaration alone.
2. Refind by person and supported Time/Place lenses after restart without a
   second Save. A recent share can remain eligible in Life after leaving Home;
   sender withdrawal and recipient attention changes have different effects.
   A shared recipe needs no fake trip or map pin to be discoverable.
3. Implement the adopted mute/disconnect/block controls in existing person and
   conversation contexts, with server enforcement across relevant routes.
   Report remains an independent action with an operational owner and honest
   handling. Pair access must not leak through a known-identity guest link.
4. Reconcile source deletion, share withdrawal, recipient removal and control
   changes across projections, exact reads, search/context, thumbnails and
   in-flight work. Include former recipients in repair. Test stale replay and
   explicit restore; late events must not silently recreate withdrawn content.
5. Perform the registered native surface QA with real media, rich/sparse/empty
   supply, text scaling, keyboard, loading/failure states and account switching.
   Record exact surface registry IDs at implementation intake. Compare isolated
   design references, not entire boards. No screenshot claim from typecheck.

**Commit boundaries:** social owner events/enumeration → Life adapter/current
reader and refinding → contact enforcement and controls → connected lifecycle
and native receipts. Life can implement against an agreed versioned interface;
it need not finish Atlas migration first. If its tested reader is unavailable,
continue private integration work but do not call this milestone complete.

**Checkpoint B — connected everyday social value:** all three media work from
selection to another account's original, contextual optional use, restart and
refinding. Several selected recipients have independent access/attention;
the author can return and withdraw. This is the first complete-system delivery
boundary, not the limit of the product vision.

#### Sixth — extend into getting together (S3 / S4 / S5; large, guest risk high)

1. Exercise existing-account invitations, optional contributions and Plan
   changes through canonical owners using the same shared-original references.
   A recipe may inform dinner without automatically creating an Occasion.
2. Let an authorized remote contributor send and correct selected material
   without attendance, arrangement-editing or private-address rights. Reuse
   the common sharing reader where its scope fits; contribution commands still
   belong to the Occasion owner, not a new generic Share side effect.
3. Integrate fresh feasible options from the live-engine/Content owners. Show
   useful tradeoffs; adopt through current owner authority; reproject affected
   participants' permitted truth. Test no change, later arrival, decline and
   abandoning an option, not only everyone accepting the new time.
4. Resolve the guest proposal before non-account execution. Add bounded preview,
   verified/otherwise explicitly authorized answer, sensitive arrival facts,
   contribution and later media under their distinct capabilities. Reuse one
   suitable session, without forcing account adoption or repeated verification.
5. Reuse earlier material for another invitation with fresh participation and
   current constraints. Prior arrival/departure statements are not defaults for
   the next dinner. Sam's unanswered change cannot become “expected at eight.”

**Commit boundaries:** account contribution/invitation adapters → current shared
change/readback → approved guest principal/delivery → guest reader/answer/arrival
→ later material/continuation. **Checkpoint C:** host, attendee and non-attending
contributor benefit with unequal effort; original sharing still stands alone.
Coordinate with the existing Plan/Integration owners, not a second planning lane.

#### Seventh — add substantive social intelligence and widen exposure (S6 / S7)

Original enjoyment and independently sourced world depth already belong in
S2. This stage adds only the source-dependent intelligence that needs additional
effective permission, production and repair—not “AI on every share.”

- With the adopted source-use scope, select one concrete improvement such as a
  friend's route detail changing a useful afternoon option, or a contrasting
  perspective making a place newly understandable. Preserve independent world
  evidence versus the person's words; do not diagnose closeness or personality.
- Reuse existing bounded Content/Integration producers. No generation/provider
  call on scroll; cache authorized reusable world information and fence personal
  derivatives by source/grant revision. Measure actual production and media costs.
- Test source withdrawal during generation, before publication and at read;
  immediate-only Ask does not create retained derivative history by accident.
- Expand exposure only after the capability's controls, support path, native
  experience, runtime bounds and explicit release authorization are satisfied.
  Retire only superseded legacy callers and schemas with migration/rollback
  evidence. Useful Trip collaboration is not automatically obsolete.

**Checkpoint D:** the same product can deliver valuable human originals, useful
independent world help and meaningfully better permissioned connections. AI
availability never determines whether a friend's photograph is worth receiving.

### 10.5 Four-root acceptance: one material, different reasons to appear

| Root / destination | What the user gets | Required implementation behavior |
| --- | --- | --- |
| Home | Timely addressed material; shared consequences within the arrangement/possibility they affect; generous independent value | No notification transcript. Respect conditional `Addressed to you`, timeliness and deduplication. Clearing attention creates no access revocation. Ordinary ambient Friends publishing is not automatically an addressed Home item. |
| Places | Intentional spatial material in `From friends`, useful alongside the world | Independent of a Trip; author-chosen Place/neighborhood/city precision; finite pagination and substantive sparse/empty fallback. No live-person tracker or inferred visit. Exact venue identity alone does not authorize a more precise location. |
| Chat | Human conversation or a private useful question with the right context | Distinct Reply/Ask recipient and scope; no automatic attachments or retained third-party inference. Original content doesn't require entering Chat. Preserve return to the original root/object. |
| Life | What was shared, by whom, connected to legitimate time/place/people context | Same eligible original, not a permanent recipient copy. Basic refinding and sender control survive restart; reader authority remains current. No extra filing assignment. |
| Occasion / Plan | Contributions and useful practical state around doing something together | Existing detail destination and owners. Receiving a share does not enroll anyone; an arrangement edit does not answer for a participant. |

Casual non-spatial material follows accepted placement: a deliberately featured
Status can have its Home doorway, with Life People continuity; a specifically
addressed recipe may have timely Home delivery. Neither should acquire a fake
Place just to qualify for the friends map. Featured Status is a use of a share,
not a second profile system. No fifth tab or parallel social inbox is proposed.

### 10.6 Acceptance portfolio and evidence required

Use the [existing fixture world](fixtures/shared-fixture-world-2026-09-07.md)
and add compatible fixtures only where coverage is missing. Fixture statements
are not real source/provider facts or user observations.

| Scenario | Completion condition | Failure it must catch |
| --- | --- | --- |
| Photograph, no extra effort | Maya selects one image; Nora sees that image with attribution and can leave | Entire album/context disclosed; caption/AI/Keep/reply required |
| Place note with world value | Exact eligible place opens; independent useful context is separate from the friend's voice | Generic Chat destination, invented visit or friend endorsement |
| Non-spatial recipe | Actual text or eligible external original opens and can be found later | Mandatory Place, Occasion, ingestion questionnaire or copied restricted article |
| One send, several recipients | Each selected account receives once; failed delivery is recoverable individually | Duplicate shares, accidental group room, recipient-list leakage, future connections included |
| Original after restart | Refind through the supported Life lens; author can inspect/withdraw later | Component-local state is the only control; recipient forced to Keep |
| Clear, mute, withdraw | Attention changes preserve eligible refinding; author withdrawal closes applicable readers | “Leave it” unexpectedly erases access; Home-only hiding masquerades as revocation |
| Source/control race | Current rights win over old events, cached routes and in-flight work | Stale resurrection; stale thumbnail; raw message/search/context bypass |
| Sparse social supply | Zero or one friend still leaves useful Home/Places, with no invitation pressure | Fabricated friends activity or an empty app demanding recruitment |
| Dinner and changed timing | Current arrangement, personal answer and protected constraint remain separate | Silence treated as acceptance; old seven-thirty copied into next dinner |
| Asymmetric contribution | Dana contributes without attending; Sam receives without uploading anything | Membership/attendance/admin work used to unlock receiving |

Required evidence layers for the connected milestone:

1. Unit/route tests of each changed owner and consumer, including unauthorized
   readers and same-request retry. New canonical readers need real database
   tests, not only mocked repository return values.
2. Connected PostgreSQL/API scenarios from Source and share writes through
   outbox/delivery, reads and repair. Use synchronized races when claiming race
   protection; separately test ordinary stale replay and migration.
3. Cross-repo generated contracts on the same combined candidate: workspace
   `./scripts/sync-types.sh`, `make contract-check`, `make api-coverage-check`,
   plus mobile typecheck and real/mock consumer tests. Follow script-supported
   worktree selection; never regenerate into an unrelated dirty checkout.
4. Registered native two-account walkthrough and visual QA for affected roots
   and details. Add a third/excluded account for audience tests. Guest browser
   evidence belongs to S3 after its mechanism is adopted, not the first milestone.
5. Measured send/read/media/fan-out/recovery bounds, explicit original-only
   model-call count, and all known bypass/cleanup exceptions. No continuous
   location monitoring or generated filler to make the fixtures look alive.

Evaluate usefulness as well as correctness: can the recipient enjoy or use the
actual thing without work, can the sender understand the audience, can both
find what matters later, and does Vesper reduce coordination burden where it
participates? Use occasional consented walkthroughs; no per-share questionnaire,
reply-speed target, equal-contribution metric or passive consumption report to
the sender. Record friction observed, not an invented universal tap-count goal.

### 10.7 Ownership, checkpoints and stopping rules

- **Social owns:** selected-share semantics and approved writer, sender/recipient
  operations, contact policy enforcement and original/event interface. It fixes
  its branch-local defects before requesting shared adoption.
- **Source/Capture owns:** source custody, upload/selection and original lifecycle.
  Social obtains a tested narrow interface; it cannot bypass private custody.
- **Integration owns:** combined candidate, shared receiving/navigation contracts,
  generated snapshots and bounded production/practical coordination. Social
  supplies reviewed cuts rather than changing its roadmap underneath it.
- **Life owns:** social owner adapter, current-authority projection, indexing,
  exclusion and supported refinding. An interface review is sufficient to work
  independently; full Atlas cutover is not a blanket prerequisite.
- **Home/Places/Chat/Plan owners:** targeted consumer changes in their existing
  surfaces and owners. The approved social experience guides behavior; this lane
  does not reopen their shells or copy their implementation work.

Execute sequentially by default. If parallel agent work is separately requested,
the useful split is bounded owner/read work versus consumer/Life integration
after the interface is agreed. Serialize migrations, generated contracts and
same-file edits; no permanent agent per root or new orchestration hierarchy.
This plan does not dispatch or message another lane.

At Checkpoints A–D, or sooner after two substantive implementation packages,
reassess the remaining work using actual rework and integration receipts. Reopen
only the affected decision if sharing needs invented context, the sender gains
a maintenance dashboard, receiving becomes an AI task, Life duplicates custody,
or guests must administer the host's product. Don't restart philosophy/design
because one component needs a correction.

Treat unavailable adopted identity/policy, an incompatible owner interface, or
a cross-user correctness defect as a capability-specific stop. Work on independent
approved capabilities can continue. Do not turn a conditional launch gate into a
claim that every subsystem must be finished before implementation starts.

**Immediate next action on execution authorization:** finish the baseline reader
audit and the exact schema/audience/clear-versus-release contract review. Return
the proposed migration/API shape for the required approval, then execute selected
sending → original receiving → basic Life continuity and controls as one connected
delivery. No new research pack, broad design sprint or guest identity system is
needed to begin that work.
