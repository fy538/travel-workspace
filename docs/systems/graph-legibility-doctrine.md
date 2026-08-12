---
doc_type: contract
status: active
owner: founder / engineering
created: 2026-07-06
last_verified: 2026-07-10
why_new: Establish one cross-cutting boundary for when the world model may explain itself to users.
supersedes: []
source_of_truth_for: [graph-legibility-and-model-reveal-policy]
---

# Graph Legibility — Cross-Cutting Doctrine

> Status: ratified 2026-07-10
> Applies to: Vesper, You, Trips, Places, and any surface that reads or writes the traveler/group world model
> Consumed by: all system charters above should cite this doc when adding a "does the model know this" moment
> Last updated: 2026-07-06

## Purpose

Answers one question every future feature will ask: *"the model knows X about this user — should we show that?"* Without a standing answer, every surface re-litigates it from scratch, and the product drifts toward either (a) narrating its own intelligence until it feels surveilled, or (b) hiding it so completely that three months of substrate work (Personal Memory, place affinity, group synthesis) never reaches a user as felt value. This doctrine is the standing answer, so individual features don't have to re-derive it.

This is a **companion doctrine**, not a system charter — it owns no tables, no routes, no UI component. It governs a cross-cutting judgment call the same way the design canon's "State System" companion governs empty/loading/error language: apply it inside the relevant system's own surfaces, don't build a screen for it.

The retired Atlas design material remains historical reference only. This doctrine
follows the current three-root IA and the deliberate memory controls in You.

## The one-line rule

**The graph is felt as fit, not shown as a label.** A great human concierge doesn't say "I remembered you like window seats" — they book the window seat. The user should infer the intelligence from the quality of the outcome, not from the app announcing what it knows about them.

This is not a new principle invented for this doc — it follows the product's
silent-diplomacy principle. The same rule applies to taste, familiarity, history,
and group dynamics.

## The two tests

Run every candidate "does the model know this" moment through both before building it:

1. **Would a great human concierge say this out loud, or just do it?** If they'd just do it (book the table, skip the question, pick the neighborhood), it's *show* — change behavior, build no UI. If a concierge genuinely would say it out loud (offering a choice, checking in), it's *tell* — but keep it to dialogue, phrased as an offer, never a chrome element phrased as a verdict.
2. **Did the user deliberately author this signal, and would they be relaxed seeing it read back?** Saves, edits, explicit corrections, things typed into chat — pass. Dwell time, query content, which way someone voted in a group decision — fail, and stay invisible **always**, regardless of how useful the signal is internally.

## Where it is allowed to speak: deliberate You memory controls

Explicit personal-memory explanations live behind a deliberate action in **You**:
they are private, evidence-first, correctable, and reversible. Concentrating
these reveals in a control a person intentionally opens keeps personalization
from reading as surveillance in everyday planning.

**Every other surface — Trips, Vesper, Places, and everyday You screens —
expresses the graph through better-fitted output, never through a label, chip,
or badge that says "I know this about you."** If an explicit explanation is
needed, link to the intentional You control or drop the label and let the fit
speak.

## The keep-silent list

These signals may be computed and used internally, but must never be surfaced
back to the user, regardless of how compelling the insight:

- **Dwell / attention time** — surfacing "you lingered on Naples" exposes passive behavior the user never chose to broadcast. (The app barely captures this today — keep it that way unless there's a specific, consented use.)
- **Query / chat content as a read-back** — "you keep asking about safety" turns a private conversation into evidence used against the asker.
- **Individual votes in a group decision** — inferring personal taste from a coordination act ("you voted for the fado bar — you love live music?") violates the premise the vote was offered under. Coordination signals stay coordination signals; they don't get promoted to taste signals shown back to anyone.
- **Unrequested predictions** — "planning Rome next?" is predictive *and*
  unrequested, the exact intersection that reads as creepy: wrong and it's
  dumb, right and it's surveilled. Never show it proactively on Trips, Vesper,
  Places, or You.

## Show vs. tell — worked calibrations from this thread

| Candidate | Show (silent, behavior-only) | Tell (explicit, needs its own justification) | Verdict |
|---|---|---|---|
| Proposal rationale citing taste history | N/A — the *default* line stays neutral/logistics | Reveal on tap (existing "Why this?" affordance), never by default | Tell, but gated behind a deliberate ask |
| Home feed ranking from loved-categories | Feed is just better; no chip | A "you love X" chip on Home | Show only — cut the chip |
| Write-back on save / mark-happened | Silent; shapes future output | A receipt every time ("Remembered you prefer window seats") | Show by default; that pattern should be rare/earned, not standing |
| Familiarity deepening across trips | Fewer repeat questions, a first draft that already fits | A "familiarity: established" badge | Show only — the felt signal is *behavior*, never a score |
| `open_questions` ("still unsure if you like museums") | — | Vesper asks naturally in a chat turn when relevant | Tell, but as conversation, never as a standing panel |
| Cross-trip photo→taste loop | Keeping a photo quietly improves later suggestions | A "we learned this about you" toast | Show only |

The pattern across every row: **the same underlying signal can be show or tell
depending only on whether it's rendered as behavior or rendered as text.**
Default to behavior. Only promote to text in an intentional You memory control
or when the user's own tap requested the explanation.

## Tiered write-back guidance

Not every user action that teaches the model deserves the same treatment:

- **Deliberately authored, safe to acknowledge (rare, earned):** saves,
  mark-happened, corrections in a You memory control, choosing your own words
  over Vesper's in a story edit. These may occasionally get a light,
  evidence-first acknowledgment — but never a standing receipt on every
  instance. Frequency is the failure mode here, not the acknowledgment itself.
- **Deliberately authored, teach silently:** most saves, most edits, itinerary reverts. Record the signal, let it change future output, never mention it.
- **Never promote to a taste signal shown back to anyone:** votes, dwell, query content (see keep-silent list above) — these can still shape *internal* ranking/arbitration, but the write-back itself must stay invisible even in aggregate.

## Anti-patterns this doctrine rules out

- A "your taste profile" page that lists inferred traits as a dossier rather
  than discrete, evidence-backed, correctable controls in You.
- Standing badges/chips (familiarity level, loved-category tags) on daily-use
  surfaces (Trips, Vesper, Places).
- A receipt on every write-back action ("Remembered X") — the pattern is canon-legal but must stay rare or it curdles into "I'm recording you."
- Any surfaced content derived from dwell time, query text, or individual votes, anywhere.
- Predictive statements ("you'll probably want...") that weren't invited by a
  user action.

## Open risks / known gaps

- **"Rare/earned" is not yet a measurable rule.** The write-back acknowledgment tier (`ConsequenceBanner`'s "Remembered you prefer window seats") currently has no defined cadence — nothing stops an engineer from wiring it to fire on every save. Needs a concrete frequency cap (e.g., at most once per session, or only on the first instance of a new pattern) before it's actually enforceable.
- **A correction path for explicit memory claims is required.** The real
  safeguard against a wrong reveal is *upstream* — an evidence threshold before
  a claim appears — plus the existing You memory forget/reset controls. A plain
  dismiss may suppress a pattern, but it does not replace a durable correction
  or deletion control for a claim shown in You.
