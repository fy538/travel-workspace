---
doc_type: working
status: active
owner: founder / product
created: 2026-07-26
expires: 2026-08-25
why_new: No existing document owns the agent work-receipt content type. Trust receipts own the action ledger and reasoning traces own process transparency; neither makes a batch of agent work legible as an outcome.
promotes_to: a content contract in Content Contracts plus surface contract updates for concierge reply, plan-ready card, and trip-home change slot
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
| **Work receipt** *(new)* | The report. "Four cluster near your stay, so I made Saturday work." | Per batch of work | Ephemeral; may cite the others |

The reasoning trace answers *what steps did it take*. The work receipt answers
*what did that work mean for us*. The first is a progress bar with words; the
second is a conclusion a person can agree or disagree with.

## Anatomy — four moves

1. **Input acknowledged** — proves it saw what it was given.
2. **Work done, with the reason** — the *because* is the whole point; it exposes
   judgment rather than output.
3. **Constraint honoured** — shows something was protected, without saying whose.
4. **What's outstanding** — hands the human decision back explicitly.

Not every receipt needs all four. Move 2 is mandatory; a receipt without a
*because* is a status line.

### Reference examples

**Plan generation (personal thread)**
> Built Thursday–Sunday around your stay in Alfama. Kept two mornings slow
> because the group asked for a relaxed pace. One dinner is a hold, not a
> booking. Two things still need a decision.

**Ingestion (once "bring the mess in" exists)**
> Organised the seven links your group shared. Four cluster around Testaccio, so
> I drafted a Saturday around them. Two were ruled out on dietary grounds. Three
> people still need to vote.

**Repair / the Catch**
> Your 2pm and 4pm were 55 minutes apart on foot. Moved the second by half an
> hour; nothing after it shifted.

**Replan after a closure**
> The museum is closed Tuesday, so I moved it to Thursday and pulled the market
> forward. The rest of the week is unchanged.

**Vote resolution (group thread)**
> Saturday dinner is settled. Two people didn't weigh in; the choice fits what
> they'd already said they needed.

## Privacy rules (non-negotiable)

The receipt is a group-facing content type and inherits every existing rule.

- **Never name the member behind a constraint.** *"Two restaurants can't
  accommodate Maya's allergy"* is a violation and would be caught by the
  identity-leak guard. The group-safe form is *"two options were ruled out on
  dietary grounds."*
- **Group-channel receipts route through `group_compose`** like any other
  group-facing message. No bypass, no exception.
- **Private-thread receipts may be more specific to the person they belong to**,
  and only about that person.
- **Aggregate constraint language follows the existing small-group rules** —
  value-free topic counts where the current composer already collapses them.
- A receipt that cannot be composed safely is **suppressed**, not softened. The
  itinerary still ships; only the narration is withheld.

## Grounding rules

Every clause must be traceable to something that actually happened in the batch.

- Sources: tool results, planning output, feasibility findings, constraint hits,
  vote state, workflow receipts.
- **No inferred flourishes.** If the agent did not actually rule an option out on
  a constraint, it may not say it did.
- Counts must be real ("seven links", "three people") and derived, never
  estimated.
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
| **Trip room (group)** | Work affecting the group | `group_compose`-composed, non-attributed |
| **Plan-ready card body** | Async plan completion | Full receipt — replaces a bare "your plan is ready" |
| **Trip home, "what changed"** | Returning after someone else acted, or background repair | Compressed, links to detail |
| **Push** | Async completion worth interrupting for | One line, deep-links to the full receipt |

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

## Cost and implementation shape

- **One composition call** at the end of qualifying turns — Haiku-tier, a few
  hundred tokens, on the order of **$0.001**.
- Inputs already exist in the turn; no new retrieval, no new data model.
- Group variant adds one existing `group_compose` pass.
- Build order: content contract → producer → three render sites → group routing
  → grounding enforcement.

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

- Does the receipt replace the agent's conversational close, or precede it?
- Compressed form for the trip-home slot: one line, or three?
- Should a receipt ever be durable (revisitable) rather than ephemeral, or does
  the trust-receipt ledger already cover that need?
- Does the private-thread variant name the *user's own* constraint back to them
  ("kept your budget in mind"), or is even that too knowledge-flavoured?
- Should receipts be suppressible per-user, and if so is that a preference or an
  autonomy setting?
- Does the group receipt appear as a normal agent message or as a distinct
  structured object with its own affordances?

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
