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
> Applies to: Concierge, Memory & Preference, Trips/Folio, Proposals/Change Studio, Discover, Atlas — any surface that reads or writes the traveler/group world model
> Consumed by: all system charters above should cite this doc when adding a "does the model know this" moment
> Last updated: 2026-07-06

## Purpose

Answers one question every future feature will ask: *"the model knows X about this user — should we show that?"* Without a standing answer, every surface re-litigates it from scratch, and the product drifts toward either (a) narrating its own intelligence until it feels surveilled, or (b) hiding it so completely that three months of substrate work (Personal Memory, place affinity, group synthesis) never reaches a user as felt value. This doctrine is the standing answer, so individual features don't have to re-derive it.

This is a **companion doctrine**, not a system charter — it owns no tables, no routes, no UI component. It governs a cross-cutting judgment call the same way the design canon's "State System" companion governs empty/loading/error language: apply it inside the relevant system's own surfaces, don't build a screen for it.

*(Note: the design canon referenced throughout this doc — "Vesper Design Canon" and the separate "Atlas memory composition vision" bundle — currently lives outside this repo as Claude Design exports, not under version control here. See the open risk below about linking this doctrine into that canon once it has a stable, committed home.)*

## The one-line rule

**The graph is felt as fit, not shown as a label.** A great human concierge doesn't say "I remembered you like window seats" — they book the window seat. The user should infer the intelligence from the quality of the outcome, not from the app announcing what it knows about them.

This is not a new principle invented for this doc — it's belief #3 (*"the diplomacy is silent, the intelligence is invisible"*) and the Atlas Vision Board's own thesis (*"Atlas opens with meaning, not input"*) generalized from privacy-specifically to graph-legibility-generally. Silent diplomacy is a special case of this rule where the hidden signal happens to be a private constraint; this doc is the general case for any hidden signal — taste, familiarity, history, group dynamics.

## The two tests

Run every candidate "does the model know this" moment through both before building it:

1. **Would a great human concierge say this out loud, or just do it?** If they'd just do it (book the table, skip the question, pick the neighborhood), it's *show* — change behavior, build no UI. If a concierge genuinely would say it out loud (offering a choice, checking in), it's *tell* — but keep it to dialogue, phrased as an offer, never a chrome element phrased as a verdict.
2. **Did the user deliberately author this signal, and would they be relaxed seeing it read back?** Saves, edits, explicit corrections, things typed into chat — pass. Dwell time, query content, which way someone voted in a group decision — fail, and stay invisible **always**, regardless of how useful the signal is internally.

## Where it's allowed to speak: Atlas is the one mirror room

There should be exactly one place in the product where the graph explicitly reflects itself back to the user: **Atlas.** Its whole design (see `atlas-memory-composition-vision` bundle, Canonical Experience Board §2/§8, Vision Board's "trust, made editable") is built for this — retrospective, opt-in, entered on purpose, evidence-first, correctable. Concentrating every explicit "here's what I know about you" reveal into a room the user chooses to enter is what keeps it from reading as surveillance elsewhere, and it's what makes those reveals land as a gift instead of a notification (the postcard-scarcity principle: emotional weight comes from constraint, not abundance — the same logic applies to self-knowledge reveals as to photo caps).

**Every other surface — Home, Chat, Proposals, Itinerary, Discover — expresses the graph only through better-fitted output, never through a label, chip, or badge that says "I know this about you."** If a feature idea wants to add a "based on your history" chip anywhere outside Atlas, that's the signal to route it into Atlas instead, or drop the chip and let the fit speak.

## The keep-silent list

These signals may be computed and used internally, but must never be surfaced back to the user, in Atlas or anywhere else, regardless of how compelling the insight:

- **Dwell / attention time** — surfacing "you lingered on Naples" exposes passive behavior the user never chose to broadcast. (The app barely captures this today — keep it that way unless there's a specific, consented use.)
- **Query / chat content as a read-back** — "you keep asking about safety" turns a private conversation into evidence used against the asker.
- **Individual votes in a group decision** — inferring personal taste from a coordination act ("you voted for the fado bar — you love live music?") violates the premise the vote was offered under. Coordination signals stay coordination signals; they don't get promoted to taste signals shown back to anyone.
- **Unrequested predictions** — "planning Rome next?" is predictive *and* unrequested, the exact intersection that reads as creepy: wrong and it's dumb, right and it's surveilled. (`get_intended_destination` should stay inside Atlas at most, never on Home/Trips unprompted.)

## Show vs. tell — worked calibrations from this thread

| Candidate | Show (silent, behavior-only) | Tell (explicit, needs its own justification) | Verdict |
|---|---|---|---|
| Proposal rationale citing taste history | N/A — the *default* line stays neutral/logistics | Reveal on tap (existing "Why this?" affordance), never by default | Tell, but gated behind a deliberate ask |
| Home feed ranking from loved-categories | Feed is just better; no chip | A "you love X" chip on Home | Show only — cut the chip |
| Write-back on save / mark-happened | Silent; shapes future output | A receipt every time ("Remembered you prefer window seats") | Show by default; that pattern should be rare/earned, not standing |
| Familiarity deepening across trips | Fewer repeat questions, a first draft that already fits | A "familiarity: established" badge | Show only — the felt signal is *behavior*, never a score |
| `open_questions` ("still unsure if you like museums") | — | Vesper asks naturally in a chat turn when relevant | Tell, but as conversation, never as a standing panel |
| Cross-trip photo→taste loop (`ATLAS_SIGNALS_TO_MEMORY`) | Keeping a photo quietly improves later suggestions | An "Atlas taught me this" toast | Show only |

The pattern across every row: **the same underlying signal can be show or tell depending only on whether it's rendered as behavior or rendered as text.** Default to behavior. Only promote to text when the moment is Atlas, or when the user's own tap requested the explanation.

## Tiered write-back guidance

Not every user action that teaches the model deserves the same treatment:

- **Deliberately authored, safe to acknowledge (rare, earned):** saves, mark-happened, corrections in Atlas's "is this right?" pattern, choosing your own words over Vesper's in a story edit. These may occasionally get a light, evidence-first acknowledgment — but as an occasional moment, not a standing receipt on every instance. Frequency is the failure mode here, not the acknowledgment itself.
- **Deliberately authored, teach silently:** most saves, most edits, itinerary reverts. Record the signal, let it change future output, never mention it.
- **Never promote to a taste signal shown back to anyone:** votes, dwell, query content (see keep-silent list above) — these can still shape *internal* ranking/arbitration, but the write-back itself must stay invisible even in aggregate.

## Anti-patterns this doctrine rules out

- A "your taste profile" settings page that lists inferred traits as a dossier (outside Atlas).
- Standing badges/chips (familiarity level, loved-category tags) on daily-use surfaces (Home, Discover cards, Trips).
- A receipt on every write-back action ("Remembered X") — the pattern is canon-legal but must stay rare or it curdles into "I'm recording you."
- Any surfaced content derived from dwell time, query text, or individual votes, anywhere.
- Predictive statements ("you'll probably want...") that weren't invited by a user action or an Atlas-context query.

## Open risks / known gaps

- **"Rare/earned" is not yet a measurable rule.** The write-back acknowledgment tier (`ConsequenceBanner`'s "Remembered you prefer window seats") currently has no defined cadence — nothing stops an engineer from wiring it to fire on every save. Needs a concrete frequency cap (e.g., at most once per session, or only on the first instance of a new pattern) before it's actually enforceable.
- **A correction path for Atlas reveals is needed, but a dedicated confirm/dispute chip is not the requirement.** The real safeguard against a wrong reveal is *upstream* — the evidence threshold that gates whether a reveal fires at all (recurrence across trips/contexts), plus the existing Trust & Controls "× forget" / "reset learned preferences" front door. The minimum viable correction for a reveal is a plain dismiss (swipe/X) that quietly suppresses that pattern, not a bespoke "Is this right? — yes/no" interaction. The heavier chip is optional polish, justified only if Atlas reveals ship frequently enough that dismiss-and-forget proves too blunt — it is **not** a dependency for this doctrine or for Atlas shipping.
