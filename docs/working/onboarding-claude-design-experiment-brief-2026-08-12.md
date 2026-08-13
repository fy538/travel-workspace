---
doc_type: working
status: active
owner: founder / product / design / engineering
created: 2026-08-12
expires: 2026-09-11
why_new: Converts the August onboarding investigation into bounded Claude Design experiments with fixed fixtures, required states, current Vesper design-language constraints, and explicit evaluation criteria.
promotes_to: null
supersedes: []
related:
  - onboarding-and-entry-point-product-investigation-2026-08-12.md
  - product-loop-coherence-maestro-and-environment-strategy-2026-08-12.md
  - ../../travel-app/docs/surfaces/onboarding/contract.md
  - ../../travel-app/docs/Design Language.md
  - ../../travel-app/docs/Brand Identity.md
---

# Claude Design brief: onboarding and first-value experiments

> **Experiment brief, not implementation authority.** This document constrains
> Claude Design exploration around the August product pivot. Source code,
> surface contracts, design tokens, and the hash-pinned Home-surface bundle own
> current implementation and visual facts. An attractive board does not
> authorize a route, data source, inference, or feature flag.

## 1. Assignment

Design four bounded mobile experiments that test how a new or invited person
first understands Vesper and reaches durable value:

1. **Organic install — fragment first**: a person gives Vesper one real travel
   fragment, sees one useful judgment, steers it once, and authenticates only
   to save it.
2. **Share into Places**: a shared external place becomes a reviewed Place,
   receives a bounded Vesper judgment, and can be saved or handed to Trips
   without losing the original payload.
3. **Invite post-join payoff**: the current privacy-safe invite remains thin,
   but joining produces an immediate personal benefit rather than merely
   access to group state.
4. **Home city — chat to Move to local occasion**: the same Vesper composer
   accepts an ordinary local-life fragment, grounds one timely Move, and turns
   it into a local Plan only after explicit acceptance. A later frame proves
   that Vesper can earn a relationship between trips without becoming a
   generic nearby feed or an endless chat transcript.

This is not a request to redesign the whole application, invent a new design
system, or render every possible acquisition path. The research and entry-point
audit are in [the companion investigation](onboarding-and-entry-point-product-investigation-2026-08-12.md).

## 2. Product hypothesis

The experiments test one common product claim:

> Bring Vesper a real fragment of intent. Vesper interprets it with available
> place and people context, lets the person steer the judgment, turns the
> accepted result into durable private or shared state, and leaves a credible
> reason to return.

The three mobile roots are learned through artifact ownership, not a tab tour:

| Root | Owns in these experiments |
| --- | --- |
| **Places** | Place identity, source evidence, editorial context, save state, and place relationship. |
| **Vesper** | Interpretation, opinion, clarification, correction, and private work. |
| **Trips** | Accepted Plan state, group-visible commitments, execution, and durable trip ownership. |

Do not force a user through all three roots. Cross a boundary only when the
artifact changes owner. A Place can remain a Place. A Vesper exploration can
remain private. A chosen plan becomes a Trip; an accepted home-city occasion
becomes the same underlying container with `trip_kind='local'`, while an
unaccepted Move expires without creating durable clutter.

## 3. Method and iteration budget

Follow [Design Workflow](../../travel-app/docs/Design%20Workflow.md): use the
screen as a substrate diagnostic, not as permission to invent substrate.

### Round 1 — render the constrained thesis

- Produce the required frames and failure states below.
- Use the fixed fixtures and copy budgets.
- Explore only the named open design dimension for each experiment.
- Report visual friction as one of:
  - **A — UI:** hierarchy, layout, copy fit, or interaction treatment;
  - **B — content:** the available content has the right shape but weak quality;
  - **C — substrate:** the design needs data, continuity, privacy, or mutation
    behavior the product does not currently provide.

### Round 2 — repair the right layer

Re-render only after A/B/C findings have owners. Do not visually conceal a
Category C gap—for example, do not draw a signed-out shared Place surviving
auth as if the code already guarantees it.

### Round 3 — expand one resolved dimension

Only after Round 1 is coherent may the board explore a stronger alternate
paradigm. Budget at most three to four iterations per experiment. Start with
organic onboarding; home city should follow as the counter-fixture for the same
aperture. Invite and share may remain one constrained pass until the organic
first-value model is accepted.

## 4. Locked Vesper design language

These are pass/fail constraints distilled from the active
[Design Language](../../travel-app/docs/Design%20Language.md),
[Brand Identity](../../travel-app/docs/Brand%20Identity.md), and
[Type & Material Doctrine](../../travel-app/docs/design/type-material-doctrine.md).
Where an older board or brand example conflicts with the current specialized
surface or type/material contract, the current contract and source win.

### 4.1 Character and composition

- The metaphor is a **leather travel journal and a good host's desk**, not a
  SaaS dashboard, travel marketplace, or generic AI chat product.
- The emotional register is knowledgeable, restrained, warm, opinionated, and
  durable. It is not playful, gamified, productivity-coded, or aspirational
  luxury.
- Use generous whitespace and quiet hierarchy. One important idea should own
  the first viewport.
- **Opinionated over options:** give one recommendation with accept, tweak, or
  reject. If alternatives are truly required, show no more than two and make
  the recommended one clear.
- **Show, do not ask:** concrete proposals and corrections outrank preference
  questionnaires. The initial composer may offer up to three contextual prompt
  examples, but not a quiz wall.
- Auth, consent, correction, and recovery are productive trust surfaces—not
  expressive marketing interludes.

### 4.2 Color

Use semantic roles from `travel-app/constants/colors.ts`; do not create a new
onboarding palette.

- Warm paper/page: `bg.secondary` (`#F5F4EF`) or the owning surface's existing
  paper recipe.
- Primary ink: `text.primary` (`#2C2C28`).
- Primary action: warm umber `action.primary` (`#4A3428`).
- Vesper-authored attribution and selected warmth: `vesper.gold`
  (`#B0853A`) / `vesper.goldDeep` (`#8A6628`). Gold is sparse; it is not generic
  active chrome.
- Olive means successful/live/connected; slate means planning or neutral
  information; terracotta/oxblood means warning, conflict, or attention.
- Do **not** use violet for general Vesper presence. In these boards it is
  permitted only for an explicit privacy-handoff treatment already sanctioned
  by the app.
- No gradients, glassmorphism, or saturated “AI” color field as category
  shorthand.

### 4.3 Typography

- **EB Garamond Roman**: editorial title, substantial Vesper-authored
  judgment, or one bounded expressive line.
- **System Sans**: composer, auth, permissions, buttons, chips, labels,
  instructions, corrections, errors, and dense operational content.
- **JetBrains Mono**: dates, time, duration, small source stamps, or compact
  factual metadata only.
- Roman-first. No italic face and no synthetic slant. Distinguish Vesper through
  copy, placement, spacing, ochre attribution, and a restrained Roman serif
  role.
- One authored voice treatment per frame. Do not solve weak hierarchy by
  adding more serif styles.
- Use semantic roles from `constants/typography.ts`; if a board needs a new
  role, name its purpose and flag it as a token request.

### 4.4 Material and imagery

- **Paper is the room, not every object.** Prefer open sections and rows. Use
  the existing Quiet Paper/card recipes only when a bounded object earns
  containment: an interpretation, selected Place, receipt, or trip artifact.
- Do not put every prompt, fact, and CTA in a separate card.
- Do not invent full-bleed material or negative-margin sections. Current Home
  surface source explicitly has no shipping bleed treatment.
- Use existing radii, spacing, shadows, and component recipes. Do not infer
  geometry from an old board when production tokens exist.
- Real place photography must be editorial, warm, and evidence-bearing. When
  evidence is absent, use an honest code-native illustration treatment or no
  image—never invented personal photos, gray skeleton art, generic stock
  travelers, or an image that implies the wrong venue.
- The Organic Pair is the only Vesper identity mark. Use the production SVG
  geometry through its semantic wrapper; never substitute an emoji, generic
  sparkle, orb, compass, or repeated decorative motif.

### 4.5 Interaction and motion

- Minimum touch target: 44pt. Design for Dynamic Type reflow, VoiceOver order,
  keyboard presentation, Reduce Motion, and 320pt fallback—not only a pristine
  390pt frame.
- No “Welcome to Vesper” splash. The first useful interaction is the welcome.
- No blank chat canvas. Use a situated opener, a real incoming object, or
  concrete prompt ghosts.
- One low-stakes response should take under five seconds. Use at most three
  response actions.
- Primary buttons use warm umber. Status is typographic, not a pill. Chips are
  for choices or short responses, not permanent state decoration.
- Motion is restrained: native transitions, quiet state changes, no spring
  overshoot, parallax spectacle, confetti, progress celebrations, or counting
  animation.
- Normal latency uses reserved geometry and quiet operational feedback. Do not
  expose tool names. Only genuinely long work may use the product's bounded
  ambient concern line.

### 4.6 Voice, privacy, and truth

- Vesper sounds like a knowledgeable local friend with taste: specific,
  concise, and willing to say “skip it.” Avoid “AI-powered,” “personalized for
  you,” “optimize,” and other category or workflow language.
- Show visible care without attributing a private constraint to a person.
- Public and signed-out surfaces render projected, default-deny context only.
  Costs, private notes, votes, full itinerary, and booking detail never leak.
- A first-session answer can be a provisional input, not a permanent identity
  claim.
- Never fabricate current weather, availability, distance, visit history,
  group sentiment, or a reason “for you” when the fixture does not supply it.
- Every consequential action needs a clear owner and consequence receipt.

## 5. Current visual and interaction reference packet

Claude Design should receive the canonical files below as project context, not
only this brief.

### Required doctrine

1. [`travel-app/docs/Design Language.md`](../../travel-app/docs/Design%20Language.md)
2. [`travel-app/docs/Brand Identity.md`](../../travel-app/docs/Brand%20Identity.md)
3. [`travel-app/docs/design/claude-type-material-appendix.md`](../../travel-app/docs/design/claude-type-material-appendix.md)
4. [`travel-app/docs/surfaces/onboarding/contract.md`](../../travel-app/docs/surfaces/onboarding/contract.md)
5. [`travel-app/docs/surfaces/auth-invite/contract.md`](../../travel-app/docs/surfaces/auth-invite/contract.md)
6. [`travel-app/docs/surfaces/external-sharing/contract.md`](../../travel-app/docs/surfaces/external-sharing/contract.md)
7. [`travel-app/docs/surfaces/vesper-home/contract.md`](../../travel-app/docs/surfaces/vesper-home/contract.md)
8. [`travel-app/docs/surfaces/places-workspace/contract.md`](../../travel-app/docs/surfaces/places-workspace/contract.md)
9. [`travel-app/docs/surfaces/trips-home/contract.md`](../../travel-app/docs/surfaces/trips-home/contract.md)
10. [`travel-agent/docs/product/Product Thesis.md`](../../travel-agent/docs/product/Product%20Thesis.md)
11. [`travel-agent/docs/product/Product Model.md`](../../travel-agent/docs/product/Product%20Model.md)
12. [`travel-agent/docs/product/Growth Strategy.md`](../../travel-agent/docs/product/Growth%20Strategy.md)
13. [`travel-agent/docs/product/Occasion Object Decision Note.md`](../../travel-agent/docs/product/Occasion%20Object%20Decision%20Note.md)

### Visual references to attach

- Opening art/material family:
  `travel-app/assets/illustrations/begin-orient-cover.jpg` and the manifest at
  `travel-app/docs/surfaces/onboarding/design-refs/manifest.json`.
- Vesper cold/workbench grammar:
  `travel-app/docs/surfaces/vesper-home/design-refs/workbench-cold.png` and
  `workbench-home.png`.
- Existing invite landing, as structural runtime evidence only:
  `travel-app/.maestro/runs/_pairs/auth-invite/after/screenshots/full/auth-invite-landing.png`.
  Do not copy the mock-data banner into the design.
- External sharing privacy grammar:
  `travel-app/docs/surfaces/external-sharing/design-refs/external-sharing-canon-board.png`
  and `public-projection-contract-board.png`.
- Trips and Places root composition: the external hash-pinned bundle at
  `/Users/feihuyan/Downloads/vesper-home-surfaces/`, especially `HANDOFF.md`,
  `Canon - Home Surfaces`, `Trips - The Page`, and `Places - The Page`.
  Its identity was successfully verified for both registered surfaces on
  August 12, 2026. The bundle's boards are arguments; source remains fact.

The checked-in Vesper 401/405 Trips and Places images are historical
implementation evidence, not post-pivot composition authority. They may help
with vocabulary but must not silently replace the external August bundle.

## 6. Output contract for every Claude Design board

- iOS mobile, 390pt design width, with a 320pt stress specimen and one large
  Dynamic Type specimen for the densest frame.
- HTML/CSS output that can be exported and inspected; React Native fidelity is
  the goal, not literal web component reuse.
- One isolated root per frame with a stable `data-screen-id`.
- Support `?screen=<id>&mode=capture&capture=1` so QA can export phone frames
  rather than screenshotting a full board.
- Include a small, clearly separated board index for navigation; it must not
  appear inside isolated capture frames.
- Show happy path plus the explicitly required empty, working, error, auth
  cancel/recovery, and privacy states.
- Annotate every interactive control with destination and consequence.
- Add three notes at the end of the board:
  1. **Type/material compliance** — expressive vs productive regions, font
     roles, image bridge, and any proposed new token.
  2. **Substrate gaps** — every element requiring behavior not verified in the
     current code, marked Category B or C.
  3. **Decision log** — the one open dimension explored, what stayed locked,
     and the recommended variant.

Do not produce a mood board, a collection of unrelated hero screens, or a
single happy-path storyboard with no executable states.

## 7. Experiment 1 — organic install, fragment first

### Hypothesis

A new user can understand Vesper more quickly from one concrete, steerable
judgment than from the current trip-versus-dreaming questionnaire.

### Fixed fixture

Incoming text:

> Five days in Lisbon with my parents. Beautiful, but not exhausting.

First judgment fixture:

> Make Lisbon small enough to feel. Keep arrival day open, stay central, and
> give Sintra its own day rather than squeezing it between city plans.

Correction:

> My dad can't do steep walks.

Corrected consequence fixture:

> Then Alfama becomes optional, not a spine. Keep the first two mornings flat
> and central, and treat hillier stops as short, deliberate outings.

These lines are design fixtures, not approved production generation copy. The
board must present the first answer as a bounded judgment from the information
provided, not as evidence that Vesper knows this family already.

### Required frames

| ID | State | Required content and behavior |
| --- | --- | --- |
| `organic-01-first-contact-a` | Composer-led start | Situated Vesper opener, one generous composer, and up to three contextual examples. No onboarding progress bar, feature tour, tab explanation, or permission request. |
| `organic-01-first-contact-b` | Alternate start | Same composer and value promise with a quieter workbench-style opener. This is the only visual paradigm comparison in Round 1. |
| `organic-02-fragment-ready` | Input ready | Exact fixture in the composer; keyboard-safe layout; clear send action; no derived taste labels. |
| `organic-03-working` | Interpreting | Reserved result geometry and restrained operational feedback. No spinner, tool names, fake citations, or second Vesper thought. |
| `organic-04-first-judgment` | Pre-auth value | One authored judgment plus a compact, inspectable trip-shape artifact. Actions: `Keep this`, `Tweak`, and a quiet exit. |
| `organic-05-correction` | Steering | The original judgment remains intelligible while the correction enters through composer/prefilled context. Do not turn correction into a permanent accessibility profile. |
| `organic-06-corrected` | Consequence | The revised judgment visibly reflects the hill constraint without diagnostic or overly medical language. Provide a concise change receipt. |
| `organic-07-auth-to-save` | Commitment boundary | Reuse contextual auth grammar. State exactly what will be saved: a private Lisbon draft and its correction. Preserve a back path to the result. |
| `organic-08-saved-trip` | Durable owner | Lisbon Trip exists. Show one calm receipt, the next useful action, and Trips ownership. This is the first frame where authenticated three-root chrome may appear. |
| `organic-09-return-trigger` | Future value | One credible reason to return—such as an open planning question or chosen monitoring request. Do not manufacture urgency or ask for push before the user selects a notification-worthy job. |

### Required adverse states

- vague input (“Europe, maybe?”): Vesper offers at most two useful directions;
- temporary network failure: preserve the exact fragment locally and offer
  retry without returning to the first screen;
- auth cancel: return to the corrected pre-auth artifact;
- local persistence failure: do not promise the draft was saved;
- large text and keyboard: primary action and correction remain reachable;
- safety/access follow-up: appears after preview and before consequential Plan
  commitment, not as the opening question.

### Open design dimension

Compare only the first-contact composition:

- **A:** direct, composer-led “bring me a fragment” aperture;
- **B:** quieter Vesper workbench invitation with prompt ghosts feeding the
  same composer.

Everything after submission stays structurally identical so the test isolates
category comprehension rather than comparing two unrelated funnels.

### Stop condition

The experiment is ready for founder review when both variants:

- communicate that Vesper interprets and shapes, not merely chats;
- show useful value before auth;
- make correction legible and consequential;
- land in one owned durable Trip;
- render all adverse states without violating design doctrine; and
- identify any required pre-auth compute or intent-continuity work as Category
  C rather than hiding it in the prototype.

## 8. Experiment 2 — share into Places

### Hypothesis

Share capture can become the clearest Places acquisition wedge because it
starts from an existing behavior and makes the Places → Vesper → Trips
relationship visible through one real object.

### Fixed fixture

- Source: a shared restaurant URL.
- Recognized object: **A Cevicheria · Lisbon**.
- Initial source-bounded judgment: **“A lively dinner, not the quiet night
  after arrival.”**
- User correction/context: **“This is for the trip with my parents.”**
- Intended result: saved Place first; optional Trips-owned preview/commit
  second.

The fixture may use a deterministic illustration unless approved, correctly
attributed place media is supplied. Do not invent a photograph of the venue.

### Required frames

| ID | State | Required content and behavior |
| --- | --- | --- |
| `share-01-received` | Payload received | Show that the exact URL/text is retained. This is productive, compact, and cancelable. |
| `share-02-recognized` | Extraction preview | Place identity, source domain, qualitative ambiguity if any, and `This one` / `Not quite`. No numeric confidence score. |
| `share-03-public-judgment` | First value | One clearly source-bounded Vesper opinion. Do not claim personal fit before the user supplies context. |
| `share-04-context-correction` | Steering | Add the parents context and show how the judgment changes. Keep it provisional. |
| `share-05-auth-to-save` | Commitment boundary | Preserve URL, recognized entity, and correction; explain that auth saves the Place and private note. |
| `share-06-place-owned` | Places destination | Hero-first exact Place with save state, source, bounded “why,” and Ask Vesper. Authenticated root chrome is allowed. |
| `share-07-trip-preview` | Ownership handoff | `Add to trip` opens a Trips-owned preview/commit surface. Places does not mutate the Plan inline. |
| `share-08-trip-receipt` | Consequence | Exact Trip/Plan change receipt, with one path back to the Place. |

### Required adverse states

- URL resolves to more than one candidate;
- no recognizable Place, preserving the original text for Vesper;
- network unavailable, with locally retained payload and TTL disclosure;
- already-saved Place;
- expired local payload;
- auth cancel and resume;
- public source lacks enough evidence for a judgment, in which case Vesper
  says less rather than manufacturing fit.

### Open design dimension

Compare only when Vesper asks for context:

- **A:** give a small public-evidence judgment immediately, then invite context;
- **B:** ask one concrete context question before giving the first judgment.

Both variants must recognize and preview the Place before auth. Neither may
turn into a taste survey.

### Stop condition

The original payload, recognized entity, user correction, saved Place, and
optional Trip handoff remain traceable on every frame. The board clearly marks
signed-out share persistence and post-auth resumption as a current Category C
continuity gap until implementation proves otherwise.

## 9. Experiment 3 — invite post-join personal payoff

### Hypothesis

The invite already explains why the recipient is here. Removing generic
onboarding and showing one personal consequence immediately after join will
increase perceived value without exposing private group state.

### Fixed fixture

- Organizer: **Sarah**.
- Trip: **Lisbon, Portugal · Jun 4–Jun 10**.
- Safe public shape: destination, dates, organizer, and privacy boundary only.
- Recipient's optional private signal: **“Quiet mornings.”**
- Post-join payoff: **“Thursday is still open, so Vesper kept the morning
  loose.”**

The payoff must not say Sarah or another member required it, and it must not
imply the Plan was mutated unless the fixture explicitly supplies that fact.

### Required frames

| ID | State | Required content and behavior |
| --- | --- | --- |
| `invite-01-safe-preview` | Public landing | Preserve the existing calm hierarchy: organizer, destination, dates, privacy boundary, optional private signal, and one Join CTA. No bottom tabs. |
| `invite-02-auth-context` | Identity boundary | Contextual auth says the user is joining Sarah's Lisbon trip. Token and private signal are visibly preserved. |
| `invite-03-joining` | Idempotent progress | Quiet productive state; no celebration, duplicate CTA, or claim of membership before success. |
| `invite-04-joined-receipt` | Consequence | Membership and attendance state are clear. The receipt is compact and does not expose private itinerary detail. |
| `invite-05-payoff-a` | Trip-owned payoff | Personal consequence appears within the joined Trip, with `Open the plan` and `Ask Vesper privately`. |
| `invite-05-payoff-b` | Vesper-owned payoff | Same consequence begins a private Vesper thread with a clear door back to the Trip. This is the only Round 1 comparison. |
| `invite-06-notification-choice` | Return trigger | Ask for push only after the recipient chooses a reason to hear back: Plan changes, attendance decisions, or Vesper follow-up. |

### Required adverse states

- invalid, expired, revoked, and already-joined invite;
- auth cancel and later resumption;
- join retry after an ambiguous network result, without duplicate membership;
- no private signal supplied;
- safe payoff unavailable, in which case the Trip opens without a fabricated
  personal sentence;
- large group/date/title text and 320pt width.

### Open design dimension

Compare the owner of the first payoff:

- **A:** inside Trips, showing that Vesper shaped the shared artifact;
- **B:** inside a private Vesper thread, showing a personal relationship before
  the user enters group state.

Do not otherwise redesign the invite landing. It is the strongest current
onboarding path and serves as a reference/control.

### Stop condition

The chosen variant makes personal value legible within one screen after join,
keeps private inputs private, preserves Trip ownership, and creates one
permission-worthy return trigger.

## 10. Experiment 4 — home city, chat to Move to local occasion

### Why this experiment exists

The first three experiments all begin with travel-shaped demand: a trip
fragment, a Lisbon Place, or a Lisbon invite. They can prove that Vesper is a
better way to plan travel without proving the broader August thesis: Vesper
should earn trust in familiar places and remain useful between trips.

This experiment keeps conversation as the flexible intake and steering layer,
but refuses to make chat the whole product. The intended loop is:

```text
ordinary local fragment
  -> private Vesper judgment
  -> source-grounded, expiring Move
  -> accept / tweak / decline
  -> accepted local Plan
  -> timely guidance or deliberate silence
  -> lightweight outcome
  -> a better-grounded next occasion
```

The roots retain distinct jobs:

| Moment | Owner | What it proves |
| --- | --- | --- |
| Interpret and correct the fragment | **Vesper** | Conversation can absorb incomplete intent and change its judgment. |
| Inspect the public-world evidence | **Places** | A recommendation has a real place/source boundary rather than invented local omniscience. |
| Hold a low-commitment possibility | **Move** | Vesper can propose one timely action without polluting durable state. |
| Keep the accepted occasion | **Trips** | Commitment, companion coordination, and execution have an owner. The user-facing object may be titled “Saturday outside”; do not force travel vocabulary onto it. |
| Learn from what happened | **Vesper + private memory** | A later suggestion can cite an explicit outcome, not pretend one click established a permanent taste profile. |

### Hypothesis

A person can understand within one local-life task that Vesper is useful in
their familiar city, not only when they have a destination and dates. Chat
should make the product steerable; the grounded Move, accepted local Plan,
outcome, and credible next occasion should make it feel larger than chat.

### Fixed fixture

The profile begins with **no saved home city** and no location permission.
The user supplies the geography in the fragment:

> My sister is in Harlem Saturday morning. We want to be outside, and not just
> go to brunch.

Reviewed public-world opening:

- **From Root to Bloom · Marcus Garvey Park**
- **Through Aug 22**
- source label: **NYC Department of Cultural Affairs 2026 release**

First judgment fixture:

> There’s a stronger anchor than brunch: From Root to Bloom is outdoors at
> Marcus Garvey Park through Aug 22. I’d build a loose morning around that.

Correction:

> She has to leave by one.

Corrected Move fixture:

> Keep the artwork as the one anchor and finish by one. Don’t turn it into a
> cross-town itinerary.

Move actions are **Keep this Saturday**, **Tweak**, and **Not this**. Keeping it
creates a user-facing local Plan titled **Saturday with my sister**. The
underlying implementation may use `trip_kind='local'`; the interface must not
ask for lodging, a destination, a date range, or other travel-only fields.

After value—not before—the product may ask:

> Keep New York as where you’re usually around?

The answer is explicit and editable. Declining it does not discard the Move or
block the local Plan. The prototype must not imply that GPS, IP address, or the
one fragment silently established a home city.

For the second-occasion frame, use this reviewed catalog fixture only after an
explicit positive outcome:

- **Late-summer parks calendar · Aug 14–Sep 1**
- **Free talks, walks, and outdoor programs continue across the city**
- source label: **NYC Parks Events Calendar — August 2026**

Vesper may say:

> The late-summer parks calendar has more free outdoor programs through Sep 1.
> Want one that fits another two-hour Saturday morning?

These are deterministic design fixtures based on the checked-in reviewed Here
catalog. They do not authorize production copy, claim live availability, or
supply venue details beyond the cited evidence.

### Required frames

| ID | State | Required content and behavior |
| --- | --- | --- |
| `local-01-first-contact` | Universal composer | Use the same fragment aperture as organic onboarding. One local example may sit beside travel examples, but do not add a “Travel or local?” branch, location request, tab tour, or separate local onboarding. |
| `local-02-fragment-ready` | Local intent ready | Exact fixture in the composer. Make the user-supplied Harlem context visible; do not imply a saved home city. |
| `local-03-grounded-opening` | Evidence-bearing judgment | Render the first judgment with compact source and freshness evidence. A path to the Place/source exists, but the screen is not a nearby feed. |
| `local-04-chat-steering` | Correction | The user adds the one-o’clock constraint in conversation. Preserve the original intent and make the changed consequence legible. |
| `local-05-move-preview-a` | Chat-forward Move | One Move attachment follows the judgment inside the Vesper thread. It is visibly provisional and expiring, with Keep/Tweak/Not this. |
| `local-05-move-preview-b` | Artifact-forward Move | The same Move becomes the primary compact surface; conversation recedes into Tweak. Content, actions, and ownership stay identical to variant A. |
| `local-06-auth-to-keep` | Commitment boundary | If signed out, explain that auth keeps this Saturday plan and correction. Cancel returns to the intact Move. Signed-in users skip this frame. |
| `local-07-home-confirmation` | Profile invitation | Ask the exact, editable New York question only after value. Show both save and not-now continuations; location permission is unnecessary. |
| `local-08-local-plan` | Durable occasion | “Saturday with my sister” is now owned by Trips, with its bounded time, one anchor, source, and companion action. No travel-only chrome or claims that unchosen details are settled. |
| `local-09-invite` | Social handoff | Invite the sister using the existing privacy-safe invite grammar. The local Plan remains useful solo if the invite is skipped or declined. |
| `local-10-live-or-silent` | Execution posture | Show what deserves a timely update and, alongside it, an explicit quiet-state specimen where Vesper sends nothing because there is no material change. Do not fabricate live conditions. |
| `local-11-outcome` | Lightweight reflection | Ask one low-effort question such as “Worth doing again?” with at most three responses. State what the response will help with; do not turn it into a review, streak, or permanent identity label. |
| `local-12-second-occasion` | Compounding proof | In a later-session specimen, use the fixed parks-calendar fixture and the explicit two-hour/positive outcome. Explain “why now,” offer one pull-forward action, and preserve a quiet dismissal. |

### Required adverse states

- the city is unknown or absent from the reviewed Here catalog: ask for an
  explicit area or say there is not enough grounded evidence; never synthesize
  a local feed;
- the public opening is expired, stale, or cannot be revalidated: withdraw it
  and preserve the original fragment for a new answer;
- location permission is declined or unavailable: the flow still works from
  typed geography and never nags before value;
- the person declines to save New York as home: keep the accepted local Plan,
  but do not claim ambient personalization later;
- the Move is ignored or declined: it expires and creates no Trip, Plan, task,
  or notification residue;
- auth is canceled or fails: return to the intact pre-auth Move;
- the invite is skipped, declined, or unresolved: the occasion remains valid
  for the initiating person;
- no trustworthy second opening exists: render deliberate silence, not generic
  recommendations;
- no explicit outcome exists: do not claim that Vesper “learned” whether the
  occasion worked;
- 320pt width, large text, keyboard, and source expansion all retain the main
  action and evidence boundary.

### Open design dimension

Compare only **how quickly chat recedes after it has done its job**:

- **A — chat-forward:** the sourced judgment and Move stay in a compact Vesper
  thread, with the Move as a bounded attachment;
- **B — artifact-forward:** the sourced judgment resolves into a primary Move
  surface, while `Tweak` reopens conversational steering.

Both variants must begin with the same composer, accept the same correction,
show the same source, and create the same local Plan only after acceptance.
This is not a comparison of chat versus no chat. It tests whether chat is best
understood as the whole interface or as connective tissue around owned
artifacts.

### Current implementation posture — annotate on the board

| Posture | Verified boundary |
| --- | --- |
| **Present substrate** | Vesper conversation/Home, the `CITY · WEEKDAY` everyday-context grammar, a reviewed NYC Here catalog, `home_city` persistence from the profile area, and a local-Plan path backed by `trip_kind='local'` exist in code. |
| **Dark or internal** | `AMBIENT_ENABLED` is false. Local Plan and foreground Near You surfaces require internal-build dogfood flags. Outcome and related encounter work also remain gated. Treat every such frame as experimental, not shipped. |
| **Category C until proven end to end** | Active-onboarding home-city confirmation, pre-auth fragment continuity, source-to-Move acceptance, complete Move-to-local-Plan graduation, companion handoff for this local path, and second-occasion retrieval/notification policy must be visibly marked as substrate gaps wherever the prototype depends on them. |

### Stop condition

The experiment is ready for founder review when a new person can distinguish:

- **pull:** “I can tell Vesper an ordinary local situation”;
- **judgment:** “Vesper gives one sourced opinion and lets me correct it”;
- **Move:** “this is a low-commitment possibility, not saved clutter”;
- **Plan:** “only what I accepted became a shared, executable occasion”;
- **ambient return:** “Vesper may bring back a timely, explainable opening—or
  stay quiet”; and
- **compounding:** “the later suggestion uses an outcome I explicitly gave.”

Reject the experiment if users describe it as an events feed, a chatbot that
never produces an owned object, or a travel planner awkwardly relabeled for
Saturday morning.

## 11. Evaluation rubric

Score each criterion `0 = fails`, `1 = ambiguous`, or `2 = clear`. A variant
cannot advance with a zero in truth/privacy, intent continuity, accessibility,
or implementation honesty.

| Criterion | A score of 2 means |
| --- | --- |
| **Product comprehension** | Within the first value frame, a new user can explain what Vesper did beyond “chat.” |
| **Between-trip comprehension** | The local variant makes familiar-city value legible without resembling an events/nearby feed or requiring a fabricated travel container. |
| **Time to credible value** | A useful interpretation, recognized Place, or joined Trip appears before unnecessary setup. |
| **Steerability** | One correction visibly changes the judgment or owned artifact. |
| **Intent continuity** | The incoming text, URL, invite, and correction survive auth and materialization. |
| **Ownership clarity** | The user can tell whether Places, Vesper, or Trips owns the result and next action. |
| **Trust and privacy** | Evidence boundaries, private context, auth, and consequences are understandable without anxiety-producing chrome. |
| **Return value** | The flow ends with a credible open loop or explicitly chosen notification reason. |
| **Vesper fidelity** | The surface feels restrained, warm, editorial, opinionated, and materially native—not like a generic travel-AI app. |
| **Accessibility** | Touch, type, contrast, keyboard, motion, and recovery constraints survive the stress frames. |
| **Implementation honesty** | Dark features and missing continuity are labeled; no prototype-only behavior masquerades as shipped substrate. |

### Automatic rejection conditions

- auth precedes all value on organic or share entry;
- a feature tour or tab tutorial replaces the real task;
- the first session becomes a preference questionnaire;
- the result is an empty generic chat;
- incoming context disappears after auth;
- public or group UI reveals private constraints;
- the board invents weather, availability, visit history, sentiment, or current
  implementation;
- violet or generic sparkle/gradient language stands in for Vesper;
- serif, paper cards, or illustration are applied everywhere;
- pre-auth/public frames show authenticated tab chrome;
- a Place mutates the Plan without a Trips-owned preview;
- the local flow requests location permission or permanent profile facts before
  showing value;
- the local flow presents a scrollable nearby/events feed instead of one
  situated judgment;
- the Move creates durable state before explicit acceptance, or an ignored Move
  leaves notification/task residue;
- local value remains only in chat bubbles with no inspectable evidence, Move,
  Plan, outcome, or owned consequence;
- a local Plan asks for lodging, date ranges, destination setup, or other
  travel-only requirements;
- a proactive return lacks a source boundary, “why now,” user-granted reason to
  notify, or credible silent alternative;
- UI cannot survive 320pt or large text.

## 12. Paste-ready Claude Design master prompt

Use this after attaching the reference packet:

```text
Design Round 1 of Vesper's onboarding and first-value experiments from the
attached brief. Begin with Experiment 1, Organic Install — Fragment First.

Vesper is proactive, multiplayer, place-aware AI for real-world experiences.
It feels like a knowledgeable, restrained host and a durable travel journal,
not a generic AI assistant, travel marketplace, productivity dashboard, or
gamified onboarding flow.

Render the exact fixed fixture and every required happy/adverse frame. Explore
only the named first-contact dimension A vs B; keep the remainder structurally
identical. Do not invent backend behavior, private knowledge, current
conditions, or dark features. Mark any missing continuity or substrate as a
Category C gap on the board.

Use iOS mobile at 390pt, 44pt minimum targets, Dynamic Type-safe layout, warm
paper, System Sans for productive UI, EB Garamond Roman for bounded authored
judgment, and JetBrains Mono only for factual stamps. No italics, generic
sparkles, violet agent chrome, card wall, status pills, preference quiz,
spinners, or “Welcome to Vesper” splash. Use Vesper's production Organic Pair
only in sanctioned identity/attribution placement.

Output isolated HTML/CSS frames with stable data-screen-id roots and support
?screen=<id>&mode=capture&capture=1. Include Type/material compliance,
Substrate gaps, and Decision log notes. Recommend one variant using the brief's
evaluation rubric; do not recommend on aesthetics alone.
```

After Organic Round 1 is reviewed, start fresh Claude Design chats in the same
project for Share, Invite, and Home City so prompt context does not drift.

For Experiment 4, begin the fresh chat with:

```text
Design Round 1 of Experiment 4 — Home City, Chat to Move to Local Occasion —
from the attached brief. This is the missing between-trips proof of Vesper's
August thesis.

Use the fixed Harlem / From Root to Bloom fixture and every required happy and
adverse frame. Compare only how quickly chat recedes: A keeps a compact Move
attachment in the Vesper thread; B makes the Move primary and lets Tweak reopen
conversation. Both variants use the same universal composer, source evidence,
correction, acceptance boundary, local Plan, outcome, and second-occasion
fixture.

Conversation is the intake and steering substrate, not the entire product.
Show the ownership transition from private Vesper judgment to an expiring Move
to an accepted Trips-owned local Plan. Do not create durable state before Keep,
do not ask for location permission or permanent preferences before value, and
do not turn familiar-city value into an events or nearby feed. Include a quiet
state where Vesper correctly sends nothing.

Treat all ambient, local-Plan, outcome, and end-to-end continuity behavior as
dark/internal or Category C exactly as specified in the brief. The board must
not present prototype behavior as shipped. Follow the locked Vesper design
language and output contract, then recommend A or B using the full evaluation
rubric rather than aesthetics alone.
```

## 13. Handoff and evidence

For a selected board:

1. export isolated frames with
   `npm run qa:design:export -- --html="<Claude Design HTML>" --surface=onboarding`;
2. validate refs with `npm run qa:design:check -- onboarding`;
3. record the product decision separately from the prototype;
4. classify each discrepancy as UI, content, or substrate before implementation;
5. update the owning surface contract if the accepted product behavior changes;
6. implement through existing onboarding, handoff, auth, and route owners rather
   than creating a parallel framework; and
7. certify visible implementation through the registered surface-QA flow. A
   design board, Jest suite, or static HTML export alone is not a device receipt.

The first founder review should decide the organic first-contact composition
and whether the pre-auth judgment is strong enough to justify replacing the
current dreaming branch. Share, invite, and home city should then inherit that
accepted judgment/correction grammar rather than each inventing a new
onboarding system. The home-city review has one additional burden: it must prove
that conversation can resolve into a Move, a real local occasion, and an honest
reason to return without making Vesper noisy.
