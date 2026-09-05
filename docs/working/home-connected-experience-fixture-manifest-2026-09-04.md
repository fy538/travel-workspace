---
doc_type: working
status: active
owner: founder / Home orchestration
created: 2026-09-04
last_verified: 2026-09-04
expires: 2026-10-04
why_new: Provides one deterministic New York specimen shared by the Home connected prototype, mobile journey tests, and owner-lane handoffs; identifiers are test fixtures and do not authorize a production schema or personal-data import.
supersedes: []
---

# Home connected-experience fixture manifest

## 1. How to use this manifest

This is the shared specimen for J1–J4 in the [implementation map](home-connected-experience-implementation-map-2026-09-04.md). A design artifact, unit test, or owner handoff may use these identifiers to demonstrate continuity across Home, Chat, Places, and Life.

The fixture is intentionally ordinary: a New York weekend after returning from travel. It is not a real user account, real friendship graph, or production content feed. Every item below is either structured demonstration data, supplied human-authored copy, or a clearly labeled simulated source. Do not infer attendance, preference, permission, or emotional state from it.

### Fixture state labels

- `cold`: new-account or first projection; no durable write has occurred.
- `active`: a source or arrangement is visible with its current revision.
- `pending`: a request was accepted for processing, but its result is not ready.
- `withdrawn`: the source or permission was removed; derivatives must not remain visible.
- `changed`: the owner revision changed while a destination was open; return must revalidate and recompose honestly.
- `undone`: a durable write was reversed; the original source may remain available if its audience still permits it.

## 2. Stable identity manifest

The IDs are opaque on purpose. They are suitable for mocks and contract tests; they are not a proposal to rename domain nouns or create new tables.

| Fixture ID | Kind / owner | Human-facing role | Audience | Initial state | Source / claim boundary |
| --- | --- | --- | --- | --- | --- |
| `fixture-viewer-maya` | `person` / viewer | Maya, the account owner | private | active | Demonstration persona only; no inferred biography. |
| `fixture-person-dana` | `person` / Life People | Dana, a friend who addressed one contribution to Maya | addressed/private | active | Supplied human-authored fixture copy; not a real person. |
| `fixture-place-red-hook` | `place` / Places | Red Hook waterfront context for a loose Saturday possibility | public world context | active | Structured place fixture; exact opening hours are intentionally unknown. |
| `fixture-entity-jane-carousel` | `venue` / Places | A place/entity opened from the possibility | public world context | active | Demonstration entity; factual claims must be marked simulated unless sourced. |
| `fixture-source-saturday-note` | `source` / Capture/Life | Maya’s supplied note/photo bundle for the possibility | private | active | Simulated supplied artifact; no automatic retention on inspection. |
| `fixture-possibility-waterfront` | `opening` / Plan or Life decision | “A Saturday around Red Hook” as an unadopted possibility | private | active | Projection of the source and place; not a Plan or commitment. |
| `fixture-share-dana-picnic` | `artifact` / source authority | Dana’s short contribution about a picnic nearby | addressed/private | active | Supplied human-authored fixture copy/media placeholder; no group widening. |
| `fixture-arrangement-saturday` | `occasion` / Plan owner | Existing shared Saturday arrangement | invited participants | active | Structured arrangement fixture; no booking or reservation authority. |
| `fixture-commitment-gallery` | `commitment` / Plan owner | One accepted gallery time inside the arrangement | invited participants | active | Structured commitment fixture; owner revision is `r3`. |
| `fixture-contribution-dana` | `source` / Plan handoff | Dana’s suggestion attached to the arrangement | invited participants | active | Contribution, not an accepted edit; owner decision is pending. |
| `fixture-sample-ticket` | `artifact` / Capture/Life | Labeled demonstration ticket used by a new account | private/sample | cold | Demonstration-only; never implies attendance or travel history. |
| `fixture-retained-ticket-record` | `artifact` / Life record | Exact retained record after an authorized Bring | private | pending | Exists only after the Bring branch succeeds; record ref is returned by Life. |
| `fixture-home-result-red-hook` | `outcome` / Home projection | Useful result that connects the possibility to a concrete next opening | private | active | Generated/adapted result must cite the refs that support it; no hidden write. |

### Revision and permission values

| Ref | Revision | Permission / audience rule |
| --- | --- | --- |
| `fixture-possibility-waterfront` | `r1` | Maya can inspect; Keep is a separate explicit decision. |
| `fixture-share-dana-picnic` | `r2` | Dana addressed Maya; reading is not permission to share onward. |
| `fixture-arrangement-saturday` | `r3` | Participants can contribute; only the owner/editor may accept a change. |
| `fixture-commitment-gallery` | `r3` | Accepted state is readable by invited participants; external booking authority is out of scope. |
| `fixture-sample-ticket` | `r1` | Sample inspection never creates a Life record. |
| `fixture-retained-ticket-record` | `r1` | Private record exists only after the authorized Bring result. |

## 3. Journey seed states

### J1 — possibility becomes inspectable

**Seed:** Home contains `fixture-possibility-waterfront` represented by `fixture-place-red-hook` and `fixture-entity-jane-carousel`.

**Expected path:** inspect option → open Place/entity → optionally ask a contextual question → return to the same Home unit → optionally Keep the exact possibility → later distinguish Keep from Adopt.

**Must not happen:** opening creates `fixture-arrangement-saturday`; a read silently adds a Plan; a missing fact is rendered as exact operating detail.

**Mutation cases:**

- leave without keeping: no durable write;
- Keep accepted: one explicit retained reference, no adoption;
- source withdrawn: recomposition hides unsupported claims;
- revision mismatch: return preserves orientation but not stale content.

### J2 — social contribution delivers value first

**Seed:** Home contains `fixture-share-dana-picnic`, with Dana attribution and addressed audience.

**Expected path:** read the contribution → open the original/context Place → optionally browse an authorized shared destination → optionally respond or use in `fixture-arrangement-saturday` → return with the original scope intact.

**Must not happen:** reply is required to receive value; a private save widens the audience; an expired or withdrawn original remains in a derivative Home card.

**Mutation cases:**

- ignore: no social debt or task;
- private save: Maya’s private reference only;
- explicit response: audience shown before send;
- withdrawal: original and derived share disappear or show honest unavailable state.

### J3 — arrangement shares one accepted truth

**Seed:** Home contains `fixture-arrangement-saturday` and `fixture-commitment-gallery` at owner revision `r3`; `fixture-contribution-dana` is not accepted.

**Expected path:** open the canonical arrangement destination → inspect context → contribute suggestion → separately exercise owner/editor acceptance → read back accepted revision → return to Home → reopen as participant.

**Must not happen:** Home becomes an editor; contribution is rendered as accepted; every read invokes a confirmation dialog; a booking or rebooking action appears.

**Mutation cases:**

- contribution pending: visible to the owner, not accepted;
- owner accepts: arrangement revision increments and Home refreshes from owner readback;
- concurrent edit: stale command is rejected or re-previewed;
- offline submission: no optimistic accepted state;
- participant leaves: their view changes without cancelling others.

### J4 — sample leads to immediate value and exact continuity

**Seed:** cold Home contains `fixture-sample-ticket`; no personal place, person, trip, or preference is assumed.

**Expected path:** inspect sample → choose Try with yours → existing Chat/Capture boundary → choose Ask or authorized Bring → immediate useful result → scoped receipt/Undo only if a write occurred → exact Life record opening after retention.

**Must not happen:** sample inspection writes memory; attachment alone means Bring; answer-only path shows a fake retained record; a ticket proves attendance or enjoyment.

**Mutation cases:**

- cancel intake: no source or Life record;
- Ask only: answer may be useful; no durable record;
- Bring accepted: `fixture-retained-ticket-record` becomes ready and is linked to the original;
- extraction pending: show pending status without “all done” language;
- Undo: record write is reversed and Home removes the durable consequence;
- correction/withdrawal: exact source and derivatives repair together.

## 4. Cross-root reference table

| Fixture object | Home | Chat | Places | Life |
| --- | --- | --- | --- | --- |
| `fixture-possibility-waterfront` | option/result unit | contextual question target if asked | Red Hook/entity context | retained only if Keep is explicitly defined by owner lane |
| `fixture-share-dana-picnic` | addressed value card | response target only after explicit intent | place context | original/source and relationship record if authorized |
| `fixture-arrangement-saturday` | arrangement/result card | contextual assistance, not owner | place context as needed | durable occasion/record only through owner contract |
| `fixture-sample-ticket` | labeled onboarding sample | Try with yours entry | none | no record until Bring succeeds |
| `fixture-retained-ticket-record` | continuity/result reference | source context if asked | extracted place only if supported | exact retained artifact/intake record |

The same opaque ref must remain recognizable across roots. A root may render a projection of it, but it must not silently fork the object or change its audience.

## 5. Content and provenance ledger

| Content | Treatment | Allowed claim | Required label |
| --- | --- | --- | --- |
| Home option copy | human-authored demonstration | what the option offers and which refs support it | `demonstration` |
| Dana contribution | human-authored supplied fixture | Dana’s supplied words/media only | `shared by Dana · addressed to you` |
| Red Hook/Jane’s Carousel facts | structured or reusable research | only sourced facts available to the fixture | `source` or `fact unavailable` |
| Home result | personal adaptation/bespoke composition | bounded connection grounded in listed refs | `based on …` / citations |
| sample ticket | structured demonstration | how Ask/Bring could work | `sample · not your history` |
| retained ticket | Life record | extracted fields accepted by the user | `saved to Life` plus source link |

No stock image, placeholder name, or simulated social message may be presented as a real user’s actual memory. If a prototype uses a visual placeholder, preserve the semantic label in the surrounding UI or research chrome.

## 6. Fixture completion checklist

- [ ] Every J1–J4 control points to one ID in this manifest or is labeled an unsupported stub.
- [ ] A return test can compare the same ref, revision, viewer, and audience before and after navigation.
- [ ] Keep, Adopt, Contribute, Accept, Ask, Bring, Undo, and Withdraw have distinct expected states.
- [ ] No fixture requires booking authority, a new generic social feed, or a second Chat/Life store.
- [ ] Generated/adapted values have an evidence list and a measured/estimated/unknown cost label.
- [ ] Pending, changed, withdrawn, and thin-data states are represented in at least one journey.
- [ ] When production contracts are known, replace only the fixture adapters—not the journey semantics.

## 7. Handback to implementation and design lanes

Use the following compact handback with each connected artifact or test PR:

```text
journey: J1 | J2 | J3 | J4
origin_ref: <fixture id>
intent: <inspect | ask | keep | contribute | accept | bring | undo | withdraw>
target_owner: <Home | Chat/Capture | Places/Entity | Plan/Occasion | Life>
target_ref: <fixture id or explicit unsupported>
expected_result: <what the user receives immediately>
persistence: <none | private | addressed | invited participants | owner accepted>
return: <exact unit | recomposed unit | root fallback>
failure: <changed | withdrawn | pending | offline | unsupported>
```

The manifest is complete when the prototype and tests can use this handback without inventing a new object or audience rule mid-journey.
