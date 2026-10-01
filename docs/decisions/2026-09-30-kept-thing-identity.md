---
doc_type: decision
status: accepted
owner: founder / Strategy / architecture
created: 2026-09-30
decided: 2026-09-30
why_new: Records founder approval of a stable kept-thing identity distinct from source custody, recognition and world subjects; the expiring artifact roadmap cannot own this durable cross-repository architecture decision.
supersedes: []
source_of_truth_for:
  - kept-thing-identity-boundary
---

# Stable identity for the things people keep

## Decision and provenance

On September 30, the founder approved the explanation of the kept-thing
ownership boundary in the artifact Strategy thread and requested that it be
documented. Adopt a lightweight, stable, user-owned identity for the thing a
person keeps, provisionally called `ThingRef`. Implement it as a narrow domain
inside the existing backend, not another microservice or universal artifact
database. The name is a design label, not an already shipped wire contract.

This settles the identity direction proposed in the
[artifact roadmap](../working/artifact-experience-engineering-roadmap-2026-09-29.md#3-shared-architecture-contract).
Exact storage placement, schema and migration mechanics remain engineering
design work. Approval is not evidence that these have been implemented.

## Why the existing references are not sufficient

Current confirmed Intake candidates can supply an artifact reader through an
experience-anchor projection. Their recognition identity is scoped to a
submission; it does not establish that a photograph uploaded today and a
confirmation forwarded tomorrow describe the same kept ticket.

The [ingestion decision](2026-09-28-ingestion-and-connected-inbox.md) requires
one recognizable thing across doors while retaining its sources. The
[collections decision](2026-09-28-collections-are-the-spine.md) requires stable
many-to-many membership. Neither is satisfied by using an upload, a generated
description or a world catalog entry as the person's kept-item identity.

## Ownership boundaries

| Concept | Example | Owns |
| --- | --- | --- |
| Original Source | Ticket photograph and confirmation email | Existing Intake/source custody owns bytes, source revision, provenance, retention and access |
| Kept Thing | My ticket for Tuesday's screening | A narrow kept-thing domain owns stable consumer identity and reversible links/reconciliation across supporting sources |
| Recognition and claims | Provisional ticket details, confirmed candidate, corrected time | Existing Capture and domain owners retain recognition, lifecycle and fact/correction authority |
| World Subject | The film itself | Subject/domain owners supply shared facts without asserting the person's attendance or experience |
| Occasion | The evening at the cinema | Existing Occasion/experience owners connect supported context, people and contributions |
| Collection | Films, or an upcoming weekend | The collection owner holds membership references, not duplicate copies of the Thing or its originals |

Readers address the same Thing as supporting material changes. Research can
produce additions around it without becoming its identity or overwriting its
original evidence. The Thing domain must not absorb source payloads, canonical
claims, subject facts, collection membership or generated editions into one
universal record.

The [September 8 candidate-lifecycle decision](2026-09-08-capture-candidate-lifecycle.md)
continues to govern candidates and their graph/Life projections. This decision
adds the cross-submission kept-item identity; it does not transfer candidate
truth to the graph or reinterpret every existing anchor as a migrated Thing.
Under the accepted [Life model](2026-09-29-life-model-occasions-collections-and-sharing.md),
an Occasion can have a consumer Thing reference while its domain still owns
Occasion truth. There is no new competing Occasion hierarchy.

## Required behavior

0. Materialize or attach a `ThingRef` only through the existing owner-verified
   private Keep/retention path. A submitted source, extracted candidate, or
   candidate confirmation alone does not grant raw-source retention. Even where
   the UI says “Keep this interpretation,” Capture's command accepts the
   interpretation; Intake's separate custody/retention decision still governs
   whether its original may persist. A confirmed candidate may enrich/link to a
   Thing only while its supporting source is currently eligible. Do not let
   either owner decision imply the other.
1. Two sources for the same ticket may support one kept Thing, with both
   originals independently addressable. Two tickets for different screenings
   remain distinct Things even when they reference the same film Subject.
2. Reconciliation must be evidence-backed and reversible. A mistaken match
   needs a safe split/undo path. Preserve source provenance and existing reader
   references through explicitly designed compatibility or redirects.
3. Combining identity never combines permissions. Each source retains its own
   custody, audience, allowed uses and revocation checks. Revoking one source
   neither revokes an independently eligible source nor grants access to the
   revoked material through the surviving one. Dependent claims and projections
   still follow their actual evidence and current authority.
4. Collections and readers reference the kept identity rather than creating
   their own copies of truth. Subject matching does not collapse different
   people's kept records, occurrences or independently authored contributions.
5. Keeping an object does not establish attendance, preference or personal
   meaning. The [Contribution and Consequence contract](../systems/contribution-and-consequence.md)
   continues to govern use, retention, inference, audience, action and repair.

## Remaining design and implementation work

Strategy owns the kept-thing identity/reconciliation design and its reader/Life
adoption. Map Capture, collection and research consumers before selecting the
smallest storage/module boundary, required fields and command/revision contract.
Specify candidate-to-Thing mapping, old-link compatibility, mistaken-match
reversal, retry/concurrency behavior and incremental migration/rollback.

These are implementation choices within the approved direction, not reasons to
ask again whether kept Things should have a stable identity. Escalate a proposed
change that would alter the approved owner or authority boundaries. Exact
cultural-work schemas, cross-representation Component identity, catalog rights,
saved-edition retention and broader sharing policy are not settled here.

The next slice must demonstrate same-ticket/two-source reconciliation,
different-screening separation, independent source revocation, correction,
retries and reversible mistaken matches through persisted owner reads and
compatible reader reopening. Fixtures alone do not prove external email
delivery, OCR accuracy or native acceptance. Detailed execution and evidence
remain in the artifact roadmap.

The entry trigger is deliberately narrower than artifact recognition: use the
existing private Keep receipt as the source-retention boundary, then resolve an
eligible interpretation to the stable Thing identity without treating
candidate confirmation as the source-retention grant. The source-only state
remains immediately inspectable while recognition is incomplete. The roadmap
owns the exact transaction/API shape and how later confirmed candidates
converge on that identity.

For implementation, use the verified retained submission as the initial
idempotency and grouping boundary: one private Keep submission materializes one
owner-scoped Thing identity for the contribution bundle. This preserves the
person's deliberate grouping before recognition and gives retries a stable
origin. A Thing may include multiple independently addressable sources; it is
not a promise that those sources describe one semantic object. Later
evidence-backed reconciliation may merge identities across submissions, and
an evidenced split may separate distinct items without deleting the original
references. Do not infer components from byte equality or create one Thing per
extracted claim.

Implement persistence as a narrow `kept_things` owner in the existing
Postgres/backend system: SQLAlchemy Core table definitions under
`backend/core/db/_tables/`, an owner repository under `backend/core/db/`, and an
Alembic migration. The identity row contains only owner, stable ID, origin
submission, revision/lifecycle and timestamps. Readable sources and candidate
references are resolved through their existing owners at request time. Merge
aliases are owner-scoped, revisioned and idempotent; a split reverses the
recorded alias rather than rewriting consumer references. This is the selected
first-delivery design, not a claim that the schema or migration has shipped.

This record changes no code, schema, deployed flag or audience grant. It does
not authorize global deduplication, autonomous sharing, broader retention,
remote publication or a repository-wide identity rewrite.

## Revisit trigger

Revisit if implementation shows that an existing durable owner can satisfy
cross-submission identity and independent source authority without conflicting
lifecycle semantics, or if the new boundary duplicates truth rather than
referencing its owners. Record a superseding decision instead of silently
changing this accepted boundary.
