---
name: mvp-invariants
description: This project's own house rules for shipping MVP-relevant code — apply this whenever touching a canonical journey (J01-J19), any code that sends text or data to a group/notification/booking surface, any proposal/booking/expense/itinerary mutation, or when about to say a journey/feature/DoD item is "done," "shipped," "complete," or "certified." Also use this when writing or reviewing code that composes a message visible to more than one trip member. This project has a real history of two recurring failure modes — private data leaking to a group, and "done" being claimed on the strength of green backend tests alone without a device ever confirming it — so treat this skill as required reading before any of the triggers above, not optional background.
version: 1.0.0
---

# MVP Invariants — Travel Workspace

Five rules this codebase has learned the hard way, each with a documented incident
or repeated audit finding behind it. Full charters live in `docs/systems/`; full
journey specs in `docs/journeys/`. This file is the checklist that sits in front
of them — read the linked doc when a rule needs more than one line of context.

## 1. "Done" requires a device, not just green tests

This project defines four validation layers (`docs/journeys/README.md`):

1. **Static trace** — read the journey doc, trace it through both repos, no live LLM calls.
2. **Mock walk** — Jest smoke / scripted navigation against mock data.
3. **Backend canary** — real Postgres, no LLM where possible.
4. **Live dogfood** — Maestro or a human, on a real device, real providers.

The default verdict for any journey is **REFUTE — broken until proven**, not the
other way around. A journey only becomes a live-dogfood canary *after* layers 1–3
are green (`docs/journeys/README.md`).

**Why this matters here specifically:** this project's own `STATUS.md` shows
journeys sitting at "logic 12/12" while device-cert sits at 0/12 — backend/replay
green is real progress, but it is not the same claim as "a user can do this on
their phone." Conflating the two is the single most common overclaim in this
project's history.

**Apply it:** if you or a subagent are about to say a journey/feature is "done,"
"shipped," "complete," or "certified," name which layer that claim is actually
resting on. "Backend canary passes" and "device-validated" are different
sentences — don't let one stand in for the other. Check `docs/journeys/STATUS.md`
and `docs/journeys/STATIC_TRACE_PUNCH_LIST.md` for the current per-journey layer
before asserting anything about its state.

## 2. A private constraint never reaches the group

Anything one trip member told Vesper privately — a dietary restriction, a budget
constraint, an accessibility need, anything said in a 1:1 thread — must never
surface in a group-visible place: group chat, a notification, a booking brief,
a shared read model, an export.

**The one sanctioned path:** all group-bound text is composed through
`travel-agent/backend/concierge/group_compose.py`. A free-text reply that
bypasses this and writes straight to a group thread is exactly how this leaks.
This project's docs call a leak here **"the unrecoverable-trust-event risk"** —
unlike almost every other bug class, a user who catches Vesper leaking their
private constraint to friends doesn't file a bug report, they stop trusting the
product.

**Apply it:** any new code path that produces text destined for a group thread,
a push notification, a booking confirmation, or any multi-member surface must be
traced back to `group_compose.py` (or an equivalent explicit redaction step) —
not assumed safe because it "just formats a message." When reviewing such a
change, ask specifically: *what happens if the input here contains something one
member said privately?*

## 3. Never let a stub or a stale read stand in for the real thing

Do not ship a UI or backend response that presents a fabricated, mocked, or
stale result as if it were live and current. This project has shipped and later
had to unwind exactly this pattern more than once — fake personalization, a fake
"auto-book" tier that didn't book anything, a dead read-model quietly showing
stale state as current truth.

**Apply it:** if a surface can't yet do the real thing, show that honestly
(an explicit "not yet" / disabled / pending state) rather than a plausible-looking
fake. If you're building on a `Built-dark` system (see `docs/systems/README.md`'s
maturity tiers), keep it unreachable behind its flag rather than half-wiring it
into a surface where a user would read it as real.

## 4. Mutations are ledgered, reversible, and honest about which one won

Any change to a plan, proposal, booking, or expense must be append-only-ledgered
(this project's `plan_events` pattern) and truthfully reversible:

- An accepted change emits a visible receipt.
- A rejected change confirms the original state remains, visibly.
- A revert must be diff-safe and must show correctly on **every** surface that
  displayed the mutation — Plan and Map both, not just one (`docs/journeys/`
  invariant I6, the named "coherence" drift hotspot in this project).

**Apply it:** if you're writing code that mutates a plan/proposal/booking/expense
and it doesn't produce a ledger entry + a receipt the user can see, it's
incomplete — not a smaller version of the feature, a missing invariant.

## 5. One canonical path per mutation type — no parallel writer

If a mutation type already has a builder (e.g. all proposals go through
`build_and_persist_proposal`), a new feature must call that path, not add a
second way to produce the same row. A second writer is how the drift bugs in
this project's own state-machine audit happened — two paths disagreeing about
what state a thing is in.

**Apply it:** before writing a new INSERT/UPDATE for a proposal, booking,
itinerary block, or expense, grep for the existing canonical builder first
(`build_and_persist_proposal` and siblings in
`travel-agent/backend/core/db/change_proposals.py` and
`travel-agent/backend/api/routes/plan_edit_commit.py` are the known ones).
Extend it if it's missing a case; don't route around it.

---

**When in doubt**, the fuller version of each of these lives in
`docs/systems/README.md` (maturity/validation tiers) and the per-system charters
it indexes, and in `docs/journeys/README.md` + `docs/journeys/STATUS.md` for the
journey-specific invariants (I1–I10 in
`docs/working/wedge-journey-02-05-path-to-dogfood.md`). This skill is the
five-minute version, not a replacement for those.
