---
doc_type: working
status: active
decision_status: proposed
owner: founder / Experience Graph / Life / Integration
created: 2026-09-06
last_verified: 2026-09-06
expires: 2026-10-06
why_new: Resolves the missing shared-audience and revocation contract for Outcome before Life receives an Outcome producer.
supersedes: []
---

# Decision proposal: Outcome shared audience and revocation

## Status and recommendation

**Proposed, not adopted or implemented.** This document is the review boundary
for the next Life owner-family package. It does not authorize an Outcome
producer, a schema migration, a Life serving cutover, or a new social feed. The
accepted [Contribution and Consequence Contract](../systems/contribution-and-consequence.md),
[Life v1 behavior sequences](../decisions/2026-09-01-adopt-life-v1-behavior-sequences.md),
and current owner matrix remain authoritative until this proposal is accepted
or replaced.

**Recommendation:** keep Outcome shadow-only until one canonical, viewer-relative
audience resolver and its revocation events are specified and tested. Treat
`personal_outcomes.visibility = 'shared'` as an authorization result, not as a
complete audience definition. Preserve the two existing domain shapes, but do
not let the Life projector infer a broad audience from a presentation surface.

The proposed canonical rules are:

1. **Private Outcome:** effective audience is only `{owner_id}`. It never enters
   a shared Life projection.
2. **Shared encounter Outcome:** effective audience is the active members of
   the Outcome's explicit `occasion_id`. A shared encounter still requires an
   Occasion; an anchor or Place alone never grants social visibility.
3. **Shared Commitment Outcome:** effective audience is the active
   `commitment_participants` set. A linked Occasion is an authorization
   prerequisite for a participant where the existing graph rules require it;
   the link does not silently widen a participant-scoped Outcome to every
   Occasion member.
4. **No public or relationship-wide audience exists for this package.** A
   future addressed handoff or relationship grant is a different owner and
   delivery contract, not an Outcome shortcut.

This deliberately narrows the current reader's implicit behavior. The current
Together query can include a shared Commitment Outcome for every member of a
linked Occasion. That may be a valid future explicit `occasion` audience, but
it must not be treated as the canonical rule without an authored grant and a
separate decision.

## What the repository establishes today

The code already exposes two distinct Outcome writers:

| Shape | Current owner command | Current authority | Current revision |
| --- | --- | --- | --- |
| Commitment Outcome | `record_outcome` / `update_outcome` in `experience_graph/commands.py` | Caller must be a Commitment participant; shared requires a shared Commitment | Integer CAS |
| Encounter Outcome | `record_encounter_outcome` / `update_encounter_outcome` in `experience_graph/outcome_commands.py` | Caller must be an active Occasion member when an Occasion is present; shared requires an Occasion | Integer CAS |

`personal_outcomes` has an owner, optional Commitment/Occasion/Anchor/Place
context, `visibility`, and an integer `revision`. Owner deletion cascades the
Outcome row. Occasion membership and Commitment participant rows also have
their own status/identity lifecycles. These facts are useful foundations, but
they do not by themselves say which viewers must receive a Life delta.

`get_experience_projection(..., mode=together)` is intentionally a surface
read. It currently filters shared Outcomes by the viewer's active Occasion
membership and by Commitment links visible through those Occasions. That query
must remain a consumer of authorization, not become the source of truth for a
Life event payload. A projector needs a stable audience contract even when the
destination surface changes.

## Effective audience contract

Define the following pure, reviewable operation before wiring a producer:

```text
outcome_audience(outcome, graph_state) -> set[viewer_id]
```

The operation is evaluated from current authoritative rows, not from generated
copy, prose, or a prior Life index row:

| Outcome state | Audience | Exclusions |
| --- | --- | --- |
| private | owner only | every other viewer, including Occasion members and Commitment participants |
| shared encounter | active members of `occasion_id` | no Occasion; inactive/left members; blocked or otherwise ineligible viewers under the existing contribution policy |
| shared Commitment | active `commitment_participants` | non-participants, including linked Occasion members who were not named participants |
| missing owner/source or invalid context | empty set; withdraw derived rows | never guess a replacement owner or widen from a surviving presentation record |

The resolver returns identifiers and a policy version, not Outcome meaning,
source text, or private fields. It should be deterministic for a transaction's
authoritative snapshot and should be usable by both a future producer and a
shadow projector.

### Occasion membership is not the same as participant membership

An Encounter Outcome is explicitly about a shared Occasion, so all active
members are the natural audience unless the product later adds a narrower
grant. A Commitment Outcome is participant-scoped: the Commitment's
participant set is the authored boundary. Merely attaching that Commitment to
an Occasion must not expand the Outcome's audience. If the product wants an
Occasion-wide Commitment outcome, add an explicit audience/grant operation and
test its withdrawal separately; do not overload `visibility='shared'`.

## Revocation and re-evaluation semantics

Outcome delivery is a delta over the **before/after audience union**. Whenever
an owner, context, visibility, or membership changes, every viewer in
`before ∪ after` must be considered. The event remains content-free and carries
opaque identifiers, revisions, and policy metadata only.

Required re-evaluation triggers:

1. Outcome create and integer-revision update.
2. Private ↔ shared visibility change.
3. Occasion member accept, leave, block, restore, organizer transfer, or
   Occasion closure/erasure.
4. Commitment participant add, removal, transfer, or Commitment deletion.
5. Outcome context correction that changes its Occasion or Commitment binding,
   if such a command is introduced.
6. Owner account erasure and any source/grant revocation that removes the
   Outcome's authorized context.

The projector then re-reads the current graph and applies this rule:

```text
current audience contains viewer -> revision-CAS upsert/restore
current audience excludes viewer -> withdraw
current row is absent or invalid -> withdraw for every prior viewer
```

An old event may not resurrect a row after a newer revision or withdrawal. An
explicit, authoritative reauthorization may restore a withdrawn row at the
current revision; replay alone may not.

### Owner departure is not silent ownership transfer

Leaving an Occasion removes that person from the effective reader audience and
from future Occasion-scoped mutations. It does not silently transfer their
authorship to another person or rewrite the remaining members' independent
history. Existing shared material may remain available to the other currently
authorized members until the author explicitly releases it or the owning
Occasion/Commitment is revoked. If product requirements instead demand that
owner departure retracts the material for everyone, that is a separate product
decision and command; it must not be inferred by the Life projector.

### Account erasure

Account erasure is stronger than ordinary membership departure. With the
current schema, Outcomes owned by the departing account are deleted by the
owner foreign-key cascade; they are not transferred to a surviving Occasion
member. The producer/erasure path must therefore emit a content-free
withdrawal for every previously effective viewer before or atomically with the
delete. Surviving participants' independent Outcomes remain independent. A
future attribution-preserving shared record would require a new custody and
authorship contract, not a special case in Life.

## Required event envelope

An eventual Outcome Life event should include only what the projector needs to
re-evaluate:

- stable Outcome id and owner id;
- source family (`commitment` or `encounter`);
- change kind and current integer revision;
- opaque Occasion/Commitment/Anchor/Place refs as applicable;
- `viewer_ids` for `before ∪ after`, or an equivalent authoritative audience
  snapshot reference;
- policy/contract version and causation id; and
- no meaning, source object contents, private notes, or generated prose.

The owner transaction must enqueue the event with the graph mutation. Audience
membership changes must enqueue their own identifiers so a worker can repair
all affected Outcome rows without scanning every user's Life corpus.

## Acceptance fixtures before a producer

The contract is ready for implementation only when the following fixtures are
green against the canonical graph and the shadow projector:

1. Private create/update projects only to the owner.
2. Shared encounter create projects to all active Occasion members and to no
   inactive/left member.
3. Shared Commitment create projects only to active Commitment participants,
   even when the Commitment is attached to an Occasion with other members.
4. Shared → private withdraws all non-owner rows and retains the owner's row.
5. An Occasion member leaving withdraws that viewer's encounter projection but
   does not transfer authorship or rewrite the remaining viewers' records.
6. A Commitment participant leaving withdraws only that participant's
   projection; a surviving participant's independent Outcome remains.
7. An Occasion/Commitment deletion or invalid binding withdraws every affected
   viewer and cannot be undone by a stale event.
8. Owner account erasure withdraws all derived rows for the deleted Outcome;
   no Outcome is reassigned to a survivor.
9. A newer revision wins over an out-of-order event; explicit reauthorization
   is the only restore path.

## Sequencing and ownership

1. **Experience Graph:** implement and test the pure audience resolver and
   enumerate every membership/visibility change that can alter its result.
2. **Integration:** define the content-free event keys and before/after viewer
   union; ensure account erasure and relationship changes can publish them
   transactionally or through an identifier-only repair path.
3. **Life:** add the Outcome owner contract only after the fixtures above pass;
   then add a shadow projector with integer CAS, withdrawal, stale replay, and
   explicit restore proof.
4. **Serving:** keep `supports_delta_delivery=False` and Life serving gated
   until cross-viewer shadow comparison is clean. Do not treat the existing
   Together query as proof of a complete Outcome audience contract.

Related sequencing records:

- [Life next owner-family decision](life-next-owner-family-decision-2026-09-06.md)
- [Complete Life system roadmap](life-complete-system-and-atlas-replacement-roadmap-2026-09-05.md)
- [Contribution and Consequence Contract](../systems/contribution-and-consequence.md)
- [Contribution use grants decision](../decisions/2026-08-29-adopt-contribution-use-grants.md)

