---
doc_type: working
status: active
owner: founder / product / design
created: 2026-07-13
expires: 2026-08-12
why_new: No existing design brief owns the missing invitee post-join payoff moment identified by the first-five-minutes audit.
supersedes: []
source_of_truth_for: [invitee-post-join-design-prompt]
---

# Claude Design prompt — Vesper invitee post-join moment

Use this prompt inside the Claude Design project that contains the existing
Vesper auth/invite, onboarding, chat, and Trip Home/Folio design canon.

---

This is a small, targeted addition — one missing moment — not a redesign of
the invite flow, the auth flow, chat, or Trip Home. Those are already
well-designed and should not change.

## Start from the actual current design

Read these files and their local imports before changing the canvas:

- `Vesper Auth and Invite.html` + `auth-invite-app.jsx` — the invite landing
  and signal-chip intake canon (already strong; do not restyle).
- `Vesper Onboarding.html` + `onboarding-canon-invite.jsx` — the `InvInvite` /
  `InvAuth` / `InvGift` invite-door sequence.
- `Vesper Chat.html` + `chat-invite-nudge.jsx` — note this file is the
  **organizer's** view of someone joining ("Ana and Theo joined the trip" —
  `ScreenNudgeSuppressed`). It is not the gap this prompt closes.
- `Vesper Home.html` / `Vesper Trips Home.html` + `trips-home-canon.jsx`,
  `folio-integration-canon.jsx` — whatever the invitee actually lands on.
- `Vesper People and Collaboration.html` + `people-collab-app.jsx` —
  `ScreenInviteSignedIn`, `InviteEdgeBoard` (accept success state).

Create a new Claude Design tab named exactly **`Vesper Invitee Post-Join.html`**.
Do not edit any of the files above. Build the new work in the new tab,
importing the existing shared design-system and design-canvas files.

## The gap this closes

The invite door (landing → signal chips → auth) is well designed and ends
at one micro-state: "You're in." (`InviteEdgeBoard`, accept success).
Nothing after that has ever been designed. Specifically:

- No artboard shows the trip **as first seen by a just-joined member**.
  "Land straight in the existing shared-trip home… Vesper greets you
  in-context there" is asserted in the onboarding canon notes and never
  drawn.
- The invite door's own hook — the open day marked "yours to shape," the
  signal chips promising "used to shape your join experience" — has no
  designed payoff. The promise is made and then never visibly kept.
- The organizer's view of a join (`chat-invite-nudge.jsx`'s "Ana and Theo
  joined the trip") is designed. The **invitee's own** view of landing,
  with their own signal reflected back, is not.

This is not a cosmetic gap. It is the literal mechanism of the product's
core distribution belief: an invited person gives lightweight signal and
should feel, concretely, that it did something. Right now the flow gives
them a toast and a generic trip screen.

## Product goal

Design the first thirty to sixty seconds inside the trip for someone who
just joined via invite — solo or group-share — so that what they told
Vesper on the invite screen is visibly, specifically reflected back,
without narrating it as data collection ("we noticed you selected...").
This is a **felt** acknowledgment, not a receipt.

The test: could a first-time invitee, without instruction, point at
something on screen and say "that's because I said I wanted slow
mornings"? If the only evidence is a toast that already vanished, this
has not succeeded.

## Preserve from existing canon

- Warm productive material: `#EFEAE0` background, `#F9F5ED` sheet,
  `#1B1714` ink, DM Sans / JetBrains Mono / EB Garamond italic (Vesper's
  voice only — never for actions or receipts).
- The accept-success micro-state already designed
  (`InviteEdgeBoard`: "You're in. Ana and Theo can see you joined." → "Open
  Lisbon"). This prompt's work begins the moment AFTER that tap.
- Whatever the current Trip Home / Folio canon renders for an ordinary
  returning member — this is an overlay/inflection on top of it, not a
  replacement screen.
- The signal-chip privacy line ("Not posted to the group") — the payoff
  design must not contradict it. Reflecting the invitee's own answer back
  to *them* is fine; surfacing it to the *group* is not, unless belief
  #14's diplomacy rules are explicitly re-examined (they are not in scope
  here).

## Explicitly retire these assumptions

- Do not design a second onboarding sequence, tour, or checklist for
  invitees. This is one felt beat, not a flow.
- Do not have Vesper recite the chip answer back verbatim as a fact
  ("You said you wanted slow mornings") — belief #31's discretion doctrine
  treats narrated personalization as a design smell (graph-legibility
  doctrine: fit, not surveillance). The acknowledgment should be *shown*
  through something concrete changing (a plan beat, a highlighted open
  day, a Vesper aside), not *told* as a summary of inputs.
- Do not invent a group-share notification that exposes one invitee's
  answer to another. Multi-use links have no attributable identity by
  design (see backend `record_pending_intake` — group-share submissions
  are anonymous and appended, never attributed to a specific accepter).
- Do not silently drop the group-share case as "can't be helped." Design
  it as its own honest variant — see the open decision below.

## Domain truths the UI must express

- **Single-use invite** (`max_uses == 1`): the accepting user IS the
  answerer. Their signal can be attributed to them specifically. Design
  the direct case first — this is the common path.
- **Group-share invite** (`max_uses > 1`): submissions are anonymous by
  construction (see D10 in the audit below) — the backend cannot say
  "this specific person answered this." Do not design a payoff that
  implies otherwise.
- **The open day / "yours to shape" hook** (from `InvInvite`, Onboarding
  canon): if the invite promised this, the post-join moment is where it
  either pays off or is honestly absent (undated trip, no open slot).
- Personal attendance, group signal, and organizer visibility remain
  distinct concepts — do not let this design accidentally leak an
  individual's chip answer into a shared/group-visible surface.

## The one open product decision this design must resolve

**D10 (from invitee-first-five-minutes-audit-2026-07-13):** group-share
link answers are currently anonymous — never attributed, never seeded
into memory, never acknowledged to the specific person who answered, even
though the web/app copy promises "saved for when you join."

Two live options; the design should pick one and make it visible in the
artboards (not just decide it in prose):

1. **Attribute at accept** — when a group-share invitee accepts, offer
   them the chance to claim/re-confirm their earlier pre-auth answer
   (e.g. "You told me: slow mornings, fado night — still sound right?"),
   converting anonymous submission → attributed signal at the moment
   identity becomes known. Warmer, more plumbing.
2. **Post-join chips** — skip pre-auth signal capture for group-share
   links entirely; ask the same chip question again, now attributed,
   immediately after join. Simpler, no anonymous-submission handling,
   but the invitee answers twice if they already answered pre-auth.

Recommendation carried into this prompt as the default premise: **option
1 (attribute at accept)** — it keeps the existing pre-auth chip moment's
promise true rather than replacing it. Design both if time allows; if
not, design option 1 and note option 2 as the fallback.

## Required canvas sections

Build real screen sequences with transition captions, not isolated
specimens.

### 1. Solo / single-use payoff (the common path)

Sequence: accept success (existing canon, unchanged) → land in Trip
Home/Folio → the one moment their signal shows up. Candidates to
storyboard and choose from (pick the one that reads as felt, not told):

- A Vesper aside inline in the itinerary/chat, in the italic voice
  register, that acts on the signal rather than describing it — e.g. if
  they chipped "slow mornings," a morning slot in the visible plan
  reflects that pacing, with a short italic Vesper line naming *why*
  briefly, not as a data dump.
- The open day (if one exists) visibly marked as theirs to shape, with a
  direct, low-friction entry point into shaping it — the payoff of the
  `InvInvite` hook.
- A quiet, dismissible surface — not a modal, not a tour step — that
  disappears once seen and never reappears.

Show the state where **no signal was given** (they tapped "Not now" on
the chips) — the trip should not feel emptier for it; there is simply no
extra beat, not an apology or a placeholder.

### 2. Group-share payoff (the D10 decision made visible)

Sequence: a group-share accept → the attribute-at-accept moment (or
chosen alternative) → landing in Trip Home with the SAME quality of
payoff as the solo case, once attribution succeeds. Show what happens if
the invitee declines to confirm/re-state their answer (their prior
anonymous submission stays anonymous; no broken state, no re-ask
loop).

### 3. Failure / absence states

- Chip answer existed but converting it into anything visible failed
  server-side (e.g. no matching plan slot to act on) — the moment should
  degrade to *nothing shown*, never a broken or generic placeholder.
- Returning to the trip a second time — the payoff beat must not
  reappear on every visit. Show the "already seen, now just an ordinary
  trip" state.

### 4. Organizer-side non-change (confirm, don't redesign)

One artboard confirming `chat-invite-nudge.jsx`'s existing "Ana and Theo
joined the trip" line is untouched and sufficient — this prompt does not
add new organizer-facing surface for the join itself.

## Annotation and fidelity requirements

- Label every artboard with: invite path (solo/group-share), whether
  signal was given, and whether this state is shipped or
  implementation-required.
- Add transition captions: trigger, what carries over from the invite
  screen (which chip, which day), what's shown, how it resolves/dismisses.
- Use realistic content — a real destination, a real chip selection, a
  real organizer name — consistently across one journey.
- Every dismiss/continue target ≥44pt.
- No screenshot may include global bottom navigation unless the target
  screen genuinely has it (Trip Home does; a transient overlay should
  not add its own).

## Definition of done

The design is ready for review when, without instruction, a first-time
invitee looking at the artboards could:

1. See where their pre-auth signal visibly went — not told about it,
   shown something built from it.
2. Understand the group-share case is handled honestly, not silently
   dropped.
3. Confirm the moment appears once and never nags on return visits.
4. Confirm nothing here leaks one member's private signal into a
   group-visible surface.
5. Distinguish this from a tour, checklist, or onboarding sequence — it
   reads as "the trip already knows me a little," not "here's how to use
   the app."

## Handoff

On completion, this feeds an implementation slice analogous to Slice C's
`DeferredSafetyChipsSheet` pattern: a scoped, testable addition wired into
the existing post-join landing path (trip Home/Folio + chat), not a new
onboarding route. Cite artboard IDs in the implementation plan the way
`itinerary-redesign-implementation-plan-2026-07-13.md` cites its design
source.
