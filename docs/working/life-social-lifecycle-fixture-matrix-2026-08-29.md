---
doc_type: working
status: active
owner: founder / product / architecture / design / trust / engineering
created: 2026-08-29
last_verified: 2026-08-29
expires: 2026-09-28
why_new: Makes multiplayer Life behavior deterministic across joining, leaving, withdrawal, revocation, blocking, reconciliation, account deletion, death, and export instead of relying on one visibility flag or generic privacy principles.
promotes_to: null
supersedes: []
source_of_truth_for: []
depends_on:
  - docs/working/life-object-and-lens-fixture-pack-2026-08-29.md
  - docs/working/life-behavior-research-round-3-2026-08-29.md
  - docs/working/contribution-authority-immediate-value-and-repair-research-2026-08-29.md
  - docs/working/contribution-contract-fixture-pack-2026-08-29.md
  - docs/systems/contribution-and-consequence.md
---

# Life Social-Lifecycle Fixture Matrix

## Question or outcome

When people contribute to a shared Occasion or juxtaposition, then leave,
withdraw, block, reconcile, delete an account, die, or export the result, what
does each participant still own, see, find, receive, and carry forward?

This document converts that question into deterministic fixtures. It does not
approve final controls, copy, screen composition, legal policy, or storage
schema. It defines the behavior that any later Life interface and read model
must make true.

## Executive decision

Multiplayer Life must preserve a **shared episode without creating shared
ownership of every consequence**.

```text
governed shared core
  + attributed contribution lanes
  + private or relationship-scoped Outcomes
  + viewer-relative audience and safety evaluation
  + independent return policy
```

The product must never treat “in the same Occasion” as permission to merge
private interpretations, expose adjacent personal history, infer consensus, or
restore a relationship after a later unblock.

Four planes are always evaluated independently:

1. **Record authority** — what may exist and under whose custody;
2. **Audience authority** — who may read or use it now;
3. **Relationship safety** — which social paths must not be rendered; and
4. **Return policy** — whether valid material may be searched, shown, surfaced,
   notified, or carried forward.

## 1. Evidence labels

| Label | Meaning |
| --- | --- |
| **DETERMINISTIC EXPECTATION** | A required result of the fixture transition |
| **POLICY VARIANT** | A non-default behavior remains testable for an explicitly different Occasion or audience policy |
| **HARD FAILURE** | A result that invalidates the architecture or treatment |
| **OUT OF SCOPE** | A legal, moderation, or visual-design question this pack does not settle |

## 2. Invariant object graph

Use the same named graph throughout so transition differences remain visible.

### Principals

- **Feihu** — host of L02 Brooklyn dinner; private Rome material in L05.
- **Maya** — invited participant in L02; author of Paris material in L05.
- **Alex** — invited participant in L02; contributor of a receipt after dinner.
- **Vesper** — system composer, never a participant or owner of human meaning.

### L02 Brooklyn dinner

| ID | Unit | Owner/author | Initial audience | Initial state |
| --- | --- | --- | --- | --- |
| `OCC-L02` | Occasion | Feihu as host/custodian | Feihu, Maya, Alex | Dinner occurred |
| `SRC-L02-F1` | Invitation and time change | Feihu | All participants | Shared-core evidence |
| `SRC-L02-M1` | “I’ll bring dessert” | Maya | All participants | Attributed contribution |
| `SRC-L02-M2` | Pasta-table photo | Maya | All participants | Attributed contribution |
| `SRC-L02-A1` | Restaurant receipt | Alex | All participants | Attributed contribution |
| `OUT-L02-F` | Feihu's private Outcome | Feihu | Feihu only | Private |
| `OUT-L02-M` | Maya's private Outcome | Maya | Maya only | Private |
| `CMP-L02-S` | Shared dinner reconstruction | Vesper composition | Current authorized participants | Derived from shared core only |
| `CMP-L02-F` | Feihu's personal dinner return | Vesper composition | Feihu only | May use shared core plus Feihu-private state |

### L05 Rome–Paris juxtaposition

| ID | Unit | Owner/author | Initial audience | Initial state |
| --- | --- | --- | --- | --- |
| `SRC-L05-F1` | Rome heat and transit note | Feihu | Feihu; later shared with Maya | Human-authored lane |
| `SRC-L05-M1` | Paris heat photo and note | Maya | Maya; explicitly shared with Feihu | Human-authored lane |
| `CMP-L05-B` | Rome–Paris comparison | Vesper composition | Feihu and Maya while grants remain valid | Bounded comparison, not consensus |
| `OUT-L05-F` | What comparison means to Feihu | Feihu | Feihu only | Private Outcome |
| `OUT-L05-M` | What comparison means to Maya | Maya | Maya only | Private Outcome |

## 3. Grant and epoch model

Every contribution-use grant in the fixtures must record:

- author and relevant data subjects;
- custodian;
- audience and purpose;
- precision, including Place precision;
- membership and relationship epoch;
- validity interval;
- reshare and managed-export rights;
- post-membership behavior;
- posthumous directive if one exists;
- revocation owner and scope; and
- dependency lineage into claims, relations, covers, compositions, snippets,
  indexes, caches, exports, and pending handoffs.

The read path evaluates the current epoch. Historical membership is evidence
that someone participated; it is not automatically a current audience grant.

## 4. Transition register

| ID | Transition | Record plane | Audience plane | Safety plane | Return and Continue plane |
| --- | --- | --- | --- | --- | --- |
| **S01** | Active participant, valid grants | Shared core and attributed lanes persist | Current audience may read granted material | No overlay | Search, stable/nested return, and permitted Continue are eligible |
| **S02** | Invitation declined | Invitation truth persists under authorized custody | Declinee sees only what invitation policy permits; no participant access | No overlay | No attendee return, participant projection, or social comparison |
| **S03** | Invitation deferred/no response | Invitation and uncertainty remain distinct | No inferred participant audience | No overlay | Coordination may remain prospective; no “you were there” or memory return |
| **S04** | Participant leaves | Episode and occurred participation remain governed | Frozen historical shared core remains by default; explicit ephemeral/access-terminating policy may close it | No automatic safety overlay | New shared return and later updates stop; private independent history remains |
| **S05** | Contribution withdrawn | Contribution becomes unavailable to former uses as scoped | Audience grant ends for withdrawn material | No automatic safety overlay | Dependents recompile, degrade, or disappear; no substitute paraphrase that leaks it |
| **S06** | Source deleted | Custody/existence changes per deletion contract | No audience may retrieve deleted content | No automatic safety overlay | Unsupported claims and pending handoffs invalidate causally |
| **S07** | Audience narrowed or Place precision reduced | Source may remain under author custody | Readers receive only new audience/precision | No automatic safety overlay | Search, Map, composition, snippets, and Continue re-render at permitted precision |
| **S08** | Block/no-contact | Independent records remain unless separately deleted | Grants may still exist but cannot be rendered through blocked relation | Direct and relevant social-periphery paths suppressed | Automatic social return and Continue stop; unblock restores no old grant |
| **S09** | Estrangement without block | Record and grants remain as authored | Audience remains technically valid unless changed | No hard block; optional scoped shield can be explicit | Default social resurfacing may be reduced only through return policy, never inferred emotion |
| **S10** | Later unblock | Records remain as before | No audience or membership restoration | Safety overlay removed | No automatic return; explicit retrieval may work only under still-valid authority |
| **S11** | Later reconciliation | Prior epoch remains historical | New grants begin in a new epoch | New safety state applies prospectively | New return policy is authored; old compositions do not silently reactivate |
| **S12** | Account deletion | Deleting person's governed state follows custody/deletion contract | Their grants and access cease; other people's independent state remains | Relationship rendering closes | Derivatives invalidate; retained legal state is product-inaccessible and never resurfaced |
| **S13** | Verified death | Record follows explicit directive or conservative default | Death never expands audience | No synthetic presence/personhood | No new first-person messages, inferred wishes, or proactive social revival |
| **S14** | Managed export vs screenshot | Managed export retains dependency identity; screenshot is an unmanaged copy | Managed export can recompile/close; screenshot cannot be remotely revoked | Current app suppresses unsafe rendering | Product never promises revocation of copies it cannot control |

## 5. Deterministic assertions by transition

### S01 — Active participant and valid grants

**Setup:** Feihu, Maya, and Alex are current L02 participants. All listed
shared Sources have valid Occasion-scoped grants.

**Expected:**

- `CMP-L02-S` contains the dinner time, Maya's dessert commitment, Maya's photo,
  and Alex's receipt with attribution.
- Feihu cannot see `OUT-L02-M`; Maya cannot see `OUT-L02-F`.
- Search for “What did Maya contribute?” returns Maya's granted lane, not a
  synthesized group statement.
- A shared recap may say “Maya brought dessert” only if occurrence evidence
  supports fulfillment; the commitment alone supports “Maya planned to bring
  dessert.”

**Hard failures:** private Outcome leakage, authorship loss, or commitment
reported as occurrence.

### S02–S03 — Declined, deferred, and uncertain invitations

**Expected:**

- Declined, deferred, invited, accepted, attended, and contributed remain
  distinct states.
- The attendee list contains only governed attendance evidence.
- A nonresponse never becomes a relationship interpretation.
- An invitation may be found by an authorized user without earning a Life
  memory entrance.

**Hard failures:** “Everyone came,” “Maya skipped,” or a shared-memory return
based only on invitation state.

### S04 — Participant leaves

The accepted default is:

- **S04-A compact historical access:** the former participant may retrieve a
  bounded shared core that existed during their membership epoch, excluding
  later contributions, current participant state, and revoked material.

Retain this explicitly configured variant for ephemeral or access-terminating
Occasions:

- **S04-B access termination:** the former participant loses the shared
  projection but retains their own Sources and independently owned Outcomes.

Both branches require:

- current membership to be false;
- no new shared contribution or generated social return;
- no withdrawal of the person's old contribution merely because they left;
- no deletion of other participants' independent episode history; and
- a new membership epoch if they later return.

S04-A is the ordinary occurred-social default. S04-B must be stated when the
Occasion is created or when the audience contract is granted; it cannot be
applied retroactively merely because a participant leaves.

### S05–S07 — Withdraw, delete, and narrow

When Maya withdraws `SRC-L02-M2`:

- the shared photo disappears from authorized source retrieval;
- `CMP-L02-S` recompiles without the photo and any claims supported only by it;
- a cover derived from the photo is replaced or removed;
- cached thumbnails, snippets, embeddings, and pending handoffs invalidate;
- the pasta event remains only if independent authorized evidence supports it;
- no generated description of the image survives as a leakage substitute; and
- Maya's dessert commitment remains because it is a different Source/grant.

When Maya reduces `SRC-L05-M1` from exact location to city:

- Feihu may retain “Paris,” not the precise Place;
- Map, search, comparison, export, and Continue use the reduced precision;
- historical generated text containing the precise Place is superseded or
  closed; and
- the system does not preserve precision in semantic indexes or snippets.

When a Source is deleted, every material dependent either retains sufficient
independent support, visibly degrades, or disappears. A previous generated
sentence is not independent support.

### S08–S11 — Block, estrangement, unblock, and reconciliation

When Feihu blocks Maya:

- `CMP-L05-B` and `CMP-L02-S` are suppressed for Feihu wherever they render
  the blocked relationship or its unsafe social periphery;
- Feihu's independent Rome and Red Hook history remains findable;
- Maya's current location, status, contributions, and relationship cues are
  not used to open possibilities for Feihu;
- no prompt recommends sharing, messaging, inviting, or revisiting together;
- explicit retrieval of a socially entangled item is handled by the safety
  contract, not by ordinary rank; and
- Maya's own record is not deleted.

Estrangement without a block produces no inferred safety state. The person may
explicitly choose “Less like this,” “Not now,” or a person/episode shield.
Inactivity alone does not authorize a grief, breakup, recovery, or personality
interpretation.

On unblock:

- only the block overlay is removed;
- prior audience grants, membership, follows, return rank, and pending Continue
  actions remain unrestored; and
- no “welcome back” memory is generated.

On reconciliation:

- new grants receive a new epoch;
- historical grants remain closed or historical according to their own policy;
- old compositions are regenerated only from currently valid inputs; and
- the system does not infer that reconciliation means the relationship is now
  public, close, or ready for proactive return.

### S12 — Account deletion

The fixture must verify:

- all deleting-user access tokens, active memberships, and use grants end;
- deleted Sources invalidate dependent claims and renderings;
- other participants keep independently owned Sources and Outcomes;
- the shared episode may degrade without inventing substitutes;
- legally retained data is excluded from product read paths, generation,
  search, resurfacing, and action; and
- no deleted account remains as an active participant, cold opener, or social
  possibility.

### S13 — Verified death

Run two branches:

- **S13-A explicit directive:** execute only the documented posthumous audience,
  custody, and use terms.
- **S13-B no directive:** preserve no new sharing rights, synthetic speech,
  inferred wishes, first-person messages, or proactive relationship revival.

Death does not convert private material into a memorial corpus. Verification,
legal requirements, executor roles, and minor/dependent policy remain outside
this fixture's product decision, but the conservative no-expansion invariant is
mandatory.

### S14 — Managed export and unmanaged screenshot

A managed Vesper export must retain a manifest of included Source revisions,
audience, precision, and dependency state. If a later revocation reaches it,
the product may close access or recompile it from remaining authorized inputs.

A screenshot or externally copied file is not remotely revocable. The product
must communicate this limitation before sharing when material sensitivity
warrants it. It must not claim that deleting or revoking inside Vesper erases
copies outside Vesper's control.

## 6. Derived composition rules

Every multiplayer composition must:

1. compile from currently authorized inputs at read/use time;
2. expose human lanes and Vesper operations separately;
3. retain plural Outcomes rather than choosing a majority interpretation;
4. never infer disclosure authority from several people mentioning the same
   fact;
5. degrade gracefully when one lane is withdrawn;
6. avoid leaking withdrawn content through title, cover, thumbnail, embedding,
   snippet, or generated paraphrase;
7. separate historical event truth from current relationship state; and
8. treat silence as correct when safe substance cannot be produced.

## 7. Return-policy precedence

Apply suppression in this order:

```text
hard block or safety boundary
  > source or audience revocation
  > person / relationship / social-periphery shield
  > episode / date / Place / Source exclusion
  > composition-class exclusion
  > snooze
  > editorial rank
```

A lower layer cannot outvote a higher one. High predicted relevance cannot
override a boundary. Suppression does not delete the record, and authorized
explicit retrieval after automatic suppression is a successful outcome when
the applicable safety policy permits it.

## 8. Test oracle

### Required zero counts

| Failure | Required result |
| --- | --- |
| Unauthorized audience exposure | **0** |
| Private Outcome leakage | **0** |
| Stale derivative after invalidation deadline | **0** |
| Old grant restored by unblock or reconciliation | **0** |
| Contribution with lost attribution | **0** |
| Synthetic group consensus | **0** |
| Unverified death treated as death | **0** |
| Retrospective push without prospective authority | **0** |

### Required coverage

- 100% of material claims have dependency lineage.
- 100% of social renderings evaluate current audience and safety state.
- 100% of transitions produce an inspectable before/after policy trace.
- 100% of Continue actions recheck authority at destination time.
- 100% of state-changing Continuations return a receipt; ignored or dismissed
  possibilities create no false receipt and mutate no Life record.

### Human evaluation questions

For each viewer and transition, ask:

1. Can I tell what happened versus what someone planned or privately felt?
2. Can I tell who contributed each material statement or Source?
3. Can I predict what leaving, withdrawing, blocking, or deleting will do?
4. Does the result preserve my own life without pulling an unsafe person back
   into it?
5. Can I retrieve what I am still allowed to retrieve without it returning
   automatically?
6. Did Vesper create any apparent group judgment that no person authored?
7. If nothing appears, is that legibly a correct outcome rather than a broken
   empty state?

## 9. Architecture requirements exposed

This matrix requires, without approving new durable owners:

- membership and relationship epochs;
- typed, scoped contribution-use grants;
- a relationship-safety overlay independent of ordinary audience;
- a return-policy compiler with deterministic precedence;
- claim- and Source-level dependency traversal;
- derivative invalidation across renderings and retrieval infrastructure;
- viewer-relative shared-core and attributed-lane projections;
- plural Outcome projections;
- managed-export identity and closure/recompilation behavior; and
- Continue envelopes that recheck current authority.

## 10. Acceptance gate

The multiplayer Life contract is ready for visual design only when all S01–S14
transitions can be instantiated against L02 and L05 with deterministic expected
results, all zero-count failures remain zero, and the S04-B access-terminating
variant can be explicitly scoped without changing the S04-A default.

The compact standard is:

> Together should make shared life richer without making anyone's life less
> theirs.
