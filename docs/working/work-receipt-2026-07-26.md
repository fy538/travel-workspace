---
doc_type: working
status: active
owner: founder / product
created: 2026-07-26
expires: 2026-08-25
why_new: No existing document owns the agent work-receipt content type. Trust receipts own the action ledger and reasoning traces own process transparency; neither makes a batch of agent work legible as an outcome.
promotes_to: a content contract in Content Contracts plus surface contract updates for concierge reply, plan-ready card, attention dropdown, and contextual itinerary change slot
supersedes: []
source_of_truth_for:
  - agent-work-receipt-content-type
---

# The Work Receipt

> **Working spec, not shipped canon.** Records what the work receipt is, why it
> exists, where it renders, what it must never say, and how to know if it worked.

## One sentence

**A work receipt is a short, grounded report the agent posts after doing a batch
of work — what it took in, what it did and why, what it protected, and what still
needs a person.**

## The problem it solves

The product's most differentiated machinery is invisible by design. The privacy
guard stack, group synthesis, feasibility repair, constraint honouring, and the
canonical mutation path all do their best work silently — and
[Surfacing Strategy](../../travel-agent/docs/product/Surfacing%20Strategy.md) §2
argues correctly that substrate *should* stay invisible.

But there is a difference between **substrate that shouldn't be narrated** and
**work that was never acknowledged.** Today, a user who triggers a plan waits
90–130 seconds (with a ~50-second silent stretch), comes back, and sees an
itinerary. Everything the agent reasoned about — the clustering, the constraint
that removed two options, the pace it protected, the decision it deliberately
left open — is gone. The itinerary is the artifact; the judgment is discarded.

The receipt is the smallest thing that makes the judgment legible without
narrating surveillance.

## The distinction that makes it safe

This is the load-bearing rule:

> **Report accomplishment, not knowledge.**

- *"I know you prefer slow mornings"* → surveillance-flavoured. Violates the
  [Graph Legibility doctrine](../systems/graph-legibility-doctrine.md).
- *"Kept two mornings slow"* → accomplishment-flavoured. Same intelligence,
  no surveillance affect.

The receipt describes **what the agent did with what it was given**. It never
describes what it has learned about a person, and never attributes a constraint
to a member (see Privacy rules below).

## Not the same as the receipts we already have

| Primitive | What it is | Scope | Lifetime |
|---|---|---|---|
| **Trust receipt** (`vesper_action_receipts`) | The ledger. "This mutation happened, here is the record." | Per action | Durable, auditable |
| **Proposal receipt** | The decision record. Who voted, what changed, what can be reverted. | Per proposal | Durable |
| **Reasoning trace / step timeline** | Process transparency. "Searched venues, checked distances." | Per turn | Ephemeral |
| **Work receipt** *(new)* | The batch-level outcome record. "Four cluster near your stay, so I drafted Saturday around them." | Per batch of work | Structured record is durable; individual renderings may be transient or compressed |

The reasoning trace answers *what steps did it take*. The work receipt answers
*what did that work mean for us*. The first is a progress bar with words; the
second is a conclusion a person can agree or disagree with.

The durable part is a structured, grounded batch record that relates inputs to
outcomes and cites any underlying trust or proposal receipts. A chat message,
completion card, itinerary summary, or push is a rendering of that record. The
rendering may disappear or compress; the batch record must remain available for
audit, correction, and source tracing.

## Anatomy — seven moves

1. **Input acknowledged** — proves it saw what it was given.
2. **Outcome stated** — says what it created, updated, merged, skipped, or failed
   to understand.
3. **Disposition made explicit** — distinguishes a suggestion from a committed
   change and says what it deliberately left unchanged.
4. **Reason given when it mattered** — exposes judgment only when the reason
   materially affected the outcome and is grounded in recorded evidence.
5. **Constraint honoured** — shows something was protected when it is safe to do
   so, without saying whose.
6. **What's outstanding** — hands the human decision back explicitly.
7. **Destination named** — says where the result now lives and links there.

Not every receipt needs all seven. Moves 2 and 3 are mandatory. A receipt may be
useful without a *because*; it must never invent a rationale merely to sound
intelligent.

### Reference examples

**Plan generation (personal thread)**
> Built Thursday–Sunday around your stay in Alfama. Kept two mornings slow
> because the group asked for a relaxed pace. One dinner is a hold, not a
> booking. Two things still need a decision.

**Ingestion (once "bring the mess in" exists)**
> Organised seven links. Added four new places to Paris, merged one duplicate,
> and couldn't identify two. Nothing was added to the itinerary. The two
> unresolved links need your attention.

**Repair / the Catch**
> Your 2pm and 4pm were 55 minutes apart on foot. Moved the second by half an
> hour; nothing after it shifted.

**Replan after a closure**
> The museum is closed Tuesday, so I moved it to Thursday and pulled the market
> forward. The rest of the week is unchanged.

**Vote resolution (group thread)**
> Saturday dinner was selected under the group's voting rule. Two people didn't
> vote. The itinerary now reflects the selected restaurant.

### Import disposition contract

An ingestion receipt derives its counts from the processing record, not from
free-form narration. When applicable it reports:

- received
- extracted
- created
- updated
- merged as duplicates
- failed
- needs review
- promoted to Places, a proposal, a booking, or the itinerary
- deliberately left uncommitted

The receipt must distinguish **source**, **candidate**, **proposal**, and
**committed canonical object**. "Found," "suggested," and "added to the
itinerary" are not interchangeable.

## Privacy rules (non-negotiable)

The receipt can render on a group-facing surface and therefore inherits every
existing group-composition and privacy rule.

- **Never name the member behind a constraint.** *"Two restaurants can't
  accommodate Maya's allergy"* is a violation and would be caught by the
  identity-leak guard. Even *"two options were ruled out on dietary grounds"*
  may be identifying in a small group. The group-safe form is the least specific
  truthful statement, such as *"two options didn't meet the trip
  requirements"* — or no constraint narration at all.
- **Group-channel receipts route through `group_compose`** like any other
  group-facing message. No bypass, no exception.
- **Private-thread receipts may be more specific to the person they belong to**,
  and only about that person.
- **Raw imports are private to the sender by default.** A group receipt may
  report explicitly promoted derived results; it may not expose the raw booking
  email, screenshot, document, private note, or inferred constraint.
- **Aggregate constraint language follows the existing small-group rules** —
  value-free topic counts where the current composer already collapses them.
- A group rendering that cannot be composed safely is **suppressed**, not
  softened. Any underlying mutation must still have used its canonical,
  ledgered path; only the unsafe narration is withheld.
- **Push is a lock-screen surface.** It uses the least sensitive completion
  language and deep-links to an authenticated in-app rendering.

## Grounding rules

Every clause must be traceable to something that actually happened in the batch.

- Sources: tool results, planning output, feasibility findings, constraint hits,
  vote state, workflow receipts.
- **No inferred flourishes.** If the agent did not actually rule an option out on
  a constraint, it may not say it did.
- Counts must be real ("seven links", "three people") and derived, never
  estimated.
- Mutation language must cite the canonical ledger entry that proves the change.
- "Unchanged," "nothing else moved," and equivalent negative claims require a
  computed diff; absence from a tool result is not proof.
- Retry and replay must be idempotent: one batch produces one structured receipt,
  not a new receipt each time a renderer or worker retries.
- This is a natural first surface for the facts primitive: a receipt is
  fact-dense, short, and entirely derivable — the ideal place to enforce
  `facts_policy` above `log`.
- If grounding fails, degrade to the shortest true statement rather than
  fabricating specificity.

## Where it renders

The receipt is a **content type, not a screen.** It occupies slots that exist.

| Slot | When | Form |
|---|---|---|
| **Agent reply in chat** | The turn that did the work | Full receipt, replaces the generic conversational close |
| **Plan-ready card body** | Async plan completion | Full receipt — replaces a bare "your plan is ready" |
| **"Things need your attention" dropdown** | Extraction, proposal, or work needs a person | Outstanding count plus deep-link to the existing review flow |
| **Contextual itinerary change slot** | Returning after a plan mutation or background repair | Compressed, attached to the affected day or item and links to detail |
| **History / receipt detail** | Someone revisits or audits the batch | Durable structured outcome with sources and cited mutations |
| **Push** | Async completion worth interrupting for | Privacy-safe one line, deep-links to the authenticated full receipt |

**The return moment is the highest-value placement.** Plan generation takes
90–130 seconds; people leave. Background work happens overnight. Other members
act while you're away. The receipt is the answer to *"what did I miss"* — which
is also, not incidentally, what makes re-entry rewarding rather than a chore.
See [Surfacing Strategy §2.5](../../travel-agent/docs/product/Surfacing%20Strategy.md)
on re-entry triggers.

## When it must NOT fire

Receipt spam kills the effect faster than absence does.

Threshold: **did the agent do something the user could not see happening?**

- ✅ Plan generation, replan, repair, ingestion batch, the Catch firing,
  multi-item resolution, a vote resolving, overnight background work.
- ❌ A single lookup, a weather answer, a one-line reply, a tool call the user
  watched complete, any turn where the step timeline already told the story.

Ship with the threshold conservative. It is easy to widen and hard to recover
from having trained people to skim.

## Implementation shape

- First produce a **deterministic structured receipt payload** from recorded
  inputs, processing dispositions, canonical mutations, and outstanding items.
- Treat natural-language composition as an optional rendering step. Counts,
  mutation claims, destinations, and reversibility are never generated from
  model memory.
- Give every batch a stable idempotency key and links to its source artifacts,
  canonical objects, and underlying trust/proposal receipts.
- Route every group-visible rendering through `group_compose`; do not reuse a
  private rendering in a group surface.
- The import-system research must determine whether the durable batch record can
  extend `vesper_action_receipts` or needs a small work-batch abstraction. Do not
  assume "no new data model" before that trace.
- Build order: structured contract → producer → grounding and privacy
  enforcement → durable detail → existing render slots → push.

### Phase 0 finding (2026-07-26) — schema decision

Traced `vesper_action_receipts` (`backend/core/db/_tables/action_receipts.py`)
before deciding. Conclusion: **no new ledger table for v1.** The existing
table already has the two primitives a batch needs — `correlation_id`
("ties receipt to the proactive event or turn that produced it") to group
multiple committed mutations under one batch, and `idempotency_key` for
exactly-once writes. It does not need to duplicate the batch envelope
(counts, disposition, outstanding items, rendered text) because those
belong to work that includes items which *never* become a mutation row
(skipped candidates, failures, needs-review) — that's new, and it's thin.

Also found a closer precedent than `vesper_action_receipts`:
`backend/concierge/receipt_composer.py` already implements exactly the
"deterministic composer, no LLM/DB, template-based text" pattern this doc
specifies — for single-proposal events. `receipt_composer._fmt_time`'s
docstring documents a real historical leak (agent-authored free text
"the early slot since Sarah needs step-free access" rendering raw into a
receipt) that is the concrete version of this doc's grounding rule. The
work receipt is the batch-level generalization of that same pattern, not a
new architecture.

**v1 shape shipped for plan generation / refine:**
- `backend/core/models/work_receipts.py` — the structured contract.
  `ReceiptReasonCategory` is a closed enum; there is no field anywhere on
  the payload that free text can flow into. This is stricter than the
  original "categorical labels, defaults to least-specific" language above
  — v1 has *no* free-text reason path at all, private or group, because a
  per-thread specificity distinction turned out to be more machinery than
  the first slice needed. Revisit if cohort feedback wants more detail in
  private threads.
- `backend/concierge/work_receipt_composer.py` — `compose_plan_generation_receipt`
  (structured, grounded to `PlanningOutput.itinerary` / `.changes_from_original`
  lengths, never estimated) + `render_work_receipt_text` (fixed-template
  rendering from a reviewed label map, `_CONSTRAINT_LABELS` — no interpolation
  of anything except counts).
- Durability: v1 stores the payload as `metadata.work_receipt` on the
  plan-ready card's message row (via `to_message_metadata`) — the "durable
  via the owning table" option named above. `action_receipt_ids`/
  `correlation_id` fields exist on the payload for future linking once a
  batch produces its own action_receipts to cite; not wired yet.
- Render slot: **plan-ready card body only** (`create_plan_ready_card` in
  `structured_messages.py`, wired from `post_plan_ready_card` in
  `_plan_runtime.py`). The free-form chat-reply slot (LLM-composed) is
  deliberately deferred — grounding an LLM's free-form turn from a
  structured payload is a different, riskier problem (prompt engineering,
  not template rendering) and doesn't block validating the payload/receipt
  concept itself.
- Privacy: the rendered group-channel text is folded into the *existing*
  `group_card_privacy_check_async` call already gating the plan-ready
  card — one privacy boundary, not a parallel one. On a block, the receipt
  text is dropped and the check retried without it (suppressed, not
  softened) — the card still ships with its pre-existing generic content
  rather than failing the whole card over a receipt-text issue.
- Tests: `tests/concierge/test_work_receipt_composer.py` (17 cases) —
  grounding (counts trace to real collection lengths, never guessed),
  disposition truthfulness (unrecognized operation degrades conservatively),
  the specific historical privacy leak reproduced as a regression test
  (`test_itinerary_change_reason_free_text_never_enters_payload`,
  `test_rendered_text_never_contains_planner_free_text`), fixed-vocabulary
  label map, and durable-metadata round-trip. Plus
  `tests/concierge/test_structured_messages.py::test_work_receipt_text_and_metadata_shape`
  / `test_no_work_receipt_falls_back_to_generic_content` (regression tests
  for a double-nesting bug in the metadata merge, caught before ship).
  `mypy`/`ruff` clean; zero regressions in `test_plan_runtime.py`,
  `test_structured_messages.py`, `test_planning_workflow.py`,
  `test_receipt_composer.py` (39 pre-existing tests, unchanged). Also
  smoke-tested against a real committed 6-day, 14-block Rome trip pulled
  read-only from local dev Postgres (not synthetic fixtures) — grounding
  and privacy held on real data; the private/group renderings came out
  identical for that trip because `constraint_categories_honoured` /
  `outstanding` aren't populated for plan-generation yet (expected, not a
  gap in this validation — see "Not yet built").

  **Idempotency fix (2026-07-26, same day):** the first version of this
  composer generated `batch_id = str(uuid4())` fresh on every call and
  derived `idempotency_key` from that random value — meaning the key was
  idempotent only with itself, never across a real retry, directly
  contradicting this doc's own grounding rule ("one batch produces one
  structured receipt, not a new receipt each time a renderer or worker
  retries"). Fixed: `compose_plan_generation_receipt` now takes an
  `operation_id` param and derives `batch_id`/`idempotency_key` from it
  when supplied. `post_plan_ready_card` passes
  `planning_commit.operation_id` — the same durable, retry-stable id
  `planning_workflow.py` already uses to resume a plan across a crash.
  Two calls with the same `operation_id` now produce byte-identical keys;
  see `test_same_operation_id_yields_identical_batch_and_idempotency_key`.
  **Known remaining gap, not yet fixed:** the key is deterministic now,
  but nothing dedupes on it — `create_plan_ready_card` still does a plain
  `create_message` INSERT with no check against an existing row for the
  same `idempotency_key`, unlike `vesper_action_receipts`'s
  `on_conflict_do_update`. A retry with a correct, matching key today
  still produces two message rows (two cards), just with identical
  metadata instead of divergent metadata. Closing that requires either a
  dedup check before `create_message` or a unique index + upsert — deferred,
  and should be closed before this is load-bearing for retry-heavy traffic.

**Not yet built:** ingestion receipts (blocked on the ingestion loop itself
existing), the Catch/repair receipt, replan-after-closure receipt, the
"attention dropdown" and "contextual itinerary change slot" render sites,
push, and the durable audit/history view. All are additive on top of the
same contract — a new `compose_*_receipt` function per `action_kind`, not
a new architecture.

## Why this is worth doing now

- It is the **cheapest way to make the invisible half of the product visible**,
  and the invisible half is the differentiated half.
- It makes **returning to the app rewarding**, which is the re-entry half of the
  frequency problem.
- It is the natural output surface for the **"bring the mess in" ingestion loop**
  — the two compound: ingestion creates material, the receipt reports it.
- It requires **no new screen, tab, or navigation**, which matters given current
  surface-area pressure.
- It exposes planning intelligence, group coordination, constraint handling, and
  agent work **in one paragraph** — the same paragraph that would demo well.

## Open decisions

- ~~Can the structured batch record extend `vesper_action_receipts`, or does
  aggregation require its own record?~~ **Resolved 2026-07-26** — see Phase 0
  finding above. No new table for v1; payload lives in the owning message's
  metadata, correlated to `vesper_action_receipts` rows when the batch has
  any.
- Does the receipt replace the agent's conversational close, or precede it?
  *(Deferred — v1 ships the card-body slot only; the free-form chat reply
  slot is unbuilt, see Phase 0 finding.)*
- Compressed form for the contextual itinerary slot: one line, or three?
  *(Deferred — slot not yet built.)*
- Does the private-thread variant name the *user's own* constraint back to them
  ("kept your budget in mind"), or is even that too knowledge-flavoured?
  *(Deferred — v1 has no free-text reason path in either channel; this
  becomes live only if a per-channel specificity tier is added later.)*
- Should receipts be suppressible per-user, and if so is that a preference or an
  autonomy setting?
- Does the group receipt appear as a normal agent message or as a distinct
  structured object with its own affordances? *(v1: reuses the existing
  `plan_ready` card type — no new affordance yet.)*

## How we know it worked

Qualitative first — this is a *felt* quality, and cohort 1 is the instrument:

- Does anyone quote it back, screenshot it, or react to it?
- Does anyone **correct** it? (Correction is the strongest signal — it means the
  reasoning was legible enough to disagree with.)
- Do members who did *not* trigger the work say they knew what happened?

Quantitative, if instrumented cheaply:

- Return-session engagement after a receipt vs. after a bare completion.
- Deep-link follow-through from plan-ready with a receipt body vs. without.
- Whether outstanding-decision counts in receipts correlate with decisions
  actually getting made.

## Correctness and validation gates

A receipt is not complete because its copy renders or its backend test passes.
The qualifying journey must be validated at the appropriate layers described in
`docs/journeys/README.md`, including a real-device check before any
"device-certified" claim.

- Every mutation claim resolves to an append-only ledger entry.
- Accepted, rejected, partially successful, and failed work are represented
  honestly.
- Plan and Map show the same resulting state after a mutation or revert.
- A receipt offers reversal only when the underlying mutation is actually
  diff-safe and reversible.
- Duplicate delivery, worker retry, and replay do not duplicate changes or
  receipts.
- Private raw artifacts and constraints stay out of group, push, export, and
  other multi-member renderings.
- Deep-links open the cited result for an authorized viewer and fail closed for
  everyone else.
- Group/private variants, partial failures, stale or out-of-order completion,
  cold start, push entry, and relevant real-device flows are exercised before
  shipping claims.

## Falsifiers

Reconsider or pull this if:

- People skim past it and go straight to the itinerary.
- It reads as bragging, or as the agent explaining itself too much.
- Grounding proves unreliable and receipts state things that didn't happen.
- The group-safe version is so redacted it becomes generic
  ("some options were considered").
- It increases perceived surveillance rather than perceived competence — the
  exact failure the accomplishment/knowledge distinction is meant to prevent.

## References

- [Surfacing Strategy](../../travel-agent/docs/product/Surfacing%20Strategy.md) — §2 invisible substrate, §2.5 re-entry triggers
- [What We Believe](../../travel-agent/docs/product/What%20We%20Believe.md) — #1 (act within earned authority), #3 (silent diplomacy), #8 (public outcomes, private inputs), #9.5 (coherent revision)
- [Graph Legibility doctrine](../systems/graph-legibility-doctrine.md)
- [Content Generation doctrine](../systems/content-generation.md)
- `backend/concierge/group_compose.py` — the composition and privacy gate this must route through
- `backend/core/db/_tables/action_receipts.py` — the trust-receipt ledger this may cite
