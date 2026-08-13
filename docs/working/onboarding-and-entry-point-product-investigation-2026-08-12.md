---
doc_type: working
status: active
owner: founder / product / engineering
created: 2026-08-12
expires: 2026-09-11
why_new: Records the August 12 onboarding and acquisition-entry investigation after the product pivot; the broader product-loop synthesis does not own detailed first-value flows, entry continuity, or onboarding priorities.
promotes_to: null
supersedes: []
related:
  - onboarding-claude-design-experiment-brief-2026-08-12.md
  - product-loop-coherence-maestro-and-environment-strategy-2026-08-12.md
  - thesis-to-experience-convergence-audit-2026-08-09.md
  - ../decisions/2026-08-12-retire-discover-and-atlas-product-surfaces.md
  - ../../travel-app/docs/surfaces/onboarding/contract.md
---

# Onboarding and entry-point product investigation

> **Working product investigation, not canon or current-status authority.** This
> note captures the onboarding discussion and a source-level audit performed on
> August 12, 2026. Re-verify implementation claims before acting on them.
> Product canon owns the durable thesis, code and generated registries own
> current behavior, and accepted product choices should be promoted into a
> decision or surface contract before this document expires.

## 1. The question we are trying to answer

The August product pivot has made Vesper's center clearer: the mobile product
now has three visible roots—**Trips, Vesper, and Places**—while Discover and
Atlas are retired as active product surfaces. The open onboarding question is
not merely how to make account creation shorter. It is:

> How can every plausible entry into Vesper make the new product thesis
> understandable, deliver credible value early, preserve the user's original
> intent, and create a reason to return?

That framing matters because Vesper is not an obvious single-purpose utility.
It combines place discovery, AI judgment, durable trip state, coordination,
execution, and learning. A conventional tour or taste questionnaire can name
those parts without showing why they form one product.

This investigation therefore covers:

1. the product premise onboarding should teach;
2. what the current generic onboarding actually does;
3. all meaningful acquisition and re-entry paths found in the codebase;
4. capabilities added or consolidated during the last ten days that onboarding
   can now expose;
5. a target flow for each entry type; and
6. the smallest sequence of product and engineering work that closes the
   highest-value seams.

The bounded fixtures, required frames, Vesper design-language constraints, and
evaluation rubric for visual exploration live in the companion
[Claude Design experiment brief](onboarding-claude-design-experiment-brief-2026-08-12.md).

## 2. Evidence labels and scope

The document uses three kinds of statements:

- **Verified** — observed in source, configuration, tests, flags, or dated Git
  history on August 12, 2026.
- **Inference** — a product interpretation of multiple verified facts.
- **Proposal** — a recommended future behavior, not a statement of current
  implementation.

The audit covers `travel-app`, `travel-agent`, and the workspace documentation.
Commit traffic is grouped into capability families, not counted as independent
features: the recent history contains merges, duplicate commits, cherry-picks,
and hardening commits, so raw commit volume would overstate product breadth.

## 3. Product premise onboarding must make felt

The canonical [Product Thesis](../../travel-agent/docs/product/Product%20Thesis.md)
and [Product Model](../../travel-agent/docs/product/Product%20Model.md) describe
Vesper as proactive, multiplayer, place-aware AI for real-world experiences.
Travel is the wedge; the broader human promise is a richer relationship with
places. The August 12 IA decision makes that thesis visible through three roots:

| Root | Question in the user's head | Product responsibility |
| --- | --- | --- |
| **Places** | What is here, and what might matter to me? | Search, map, editorial evidence, context, saves, and place relationships. |
| **Vesper** | What should I make of this or do next? | Interpretation, judgment, proposals, coordination, and governed action. |
| **Trips** | What are we actually doing? | Durable Plans, commitments, execution, coordination, and outcomes. |

**You** remains important but secondary: identity, preferences, memory,
privacy, and controls support the three-root loop rather than competing with it
as a fourth primary destination.

The product is most coherent when one job crosses the roots naturally:

```text
a place, link, need, invitation, or constraint
        ↓
Vesper interprets it in the person's and trip's context
        ↓
the person accepts, corrects, rejects, or shares that judgment
        ↓
a durable Trip, Plan, Place relationship, or private thread changes
        ↓
the product creates a credible reason to return
```

This does **not** mean onboarding should explain three tabs. It means the first
real task should let users experience the division of labor. For example:

> Places supplied the evidence; Vesper explained why it fit; Trips now owns
> the accepted plan.

The product should route to the owner of the resulting artifact. It should not
force a ceremonial visit to all three roots merely to increase cross-tab usage.

## 4. First-principles onboarding orientation

The external research and the code audit point to the following principles.

### 4.1 Optimize progress and trust, not the number of screens

Minimum friction is useful only if it preserves the context needed for a good
result. The more useful objective is:

> Maximize meaningful progress, product understanding, and earned trust per
> unit of user effort.

A two-screen flow that produces a generic answer can be worse than a four-step
flow that preserves a shared link, makes one specific judgment, lets the user
correct it, and saves the result.

### 4.2 Demonstrate the category through a real task

The product is easier to understand by seeing Vesper reason over a real trip,
place, link, or constraint than by reading a feature tour. Onboarding should use
the user's incoming fragment as the curriculum.

### 4.3 Prefer concrete evidence to abstract profiling

“Which pace are you?” is weak evidence in isolation. “Keep Thursday slow; my
parents will be tired after the flight” is immediately actionable. Taste and
relationship knowledge should accumulate from concrete choices, corrections,
and outcomes, with transparent controls in You.

### 4.4 A correction is an early value moment

An AI answer is not sufficient proof of personalization. The first correction
shows that Vesper can be steered and that the product will carry the correction
into durable state. “Slower,” “not with kids,” “lower budget,” or “step-free”
can be more revealing than a long preference survey.

### 4.5 Start before authentication; finish after a return trigger

Authentication is not the beginning of onboarding, and completing profile
fields is not the end. A good entry flow safely previews value before auth,
asks for identity at a commitment boundary, creates a durable artifact, and
leaves a clear future event or open loop worth returning for.

### 4.6 Ask for permissions at the moment they unlock value

- Ask for **push** after a user joins a trip, accepts a proposal, or requests
  monitoring.
- Ask for **location** after an explicit nearby or live-navigation request.
- Ask for **Photos** when importing a memory, receipt, or story—not to prove the
  app is personalized before its core value is clear.
- Ask for **Contacts** while inviting collaborators, with a manual path.
- Ask for **safety/access constraints** before consequential planning or
  booking, but after enough preview for the request to make sense.

### 4.7 Distinguish immediate and compounding value

Immediate value is a useful interpretation, joined Trip, extracted Place, or
saved decision. Compounding value is better future judgment because Vesper has
seen corrections, outcomes, and relationships. Onboarding must deliver the
first without pretending the second already exists.

## 5. Current generic onboarding: verified flow

The generic route is implemented primarily in
[`travel-app/app/onboarding.tsx`](../../travel-app/app/onboarding.tsx), with
persisted progress, contextual authentication, intent materialization, and a
deferred safety step.

The current sequence is:

1. a brand cover—“Every place you have loved,” “Place-aware,” and “Built for
   your people”;
2. a fork between having a trip and still dreaming;
3. on the trip branch: destination, duration, companions, authentication,
   safety, then either a created Trip or a Vesper conversation seeded with the
   partial answers;
4. on the dreaming branch: interest, pace, a diary/memory gift, Photos
   permission or decline, authentication, safety, then You/Memory.

### 5.1 What is already strong

- Progress survives interruption.
- Authentication is presented in context rather than as an unexplained wall.
- Trip creation is designed to be durable and idempotent.
- Partial trip answers can become a real Vesper thread instead of being lost.
- Safety constraints have a deferred but explicit place in the flow.
- Error recovery retains context and offers a useful alternate path.
- The trip branch ends in an owned artifact rather than an onboarding success
  screen.

### 5.2 Where it diverges from the August thesis

- The user supplies data before receiving a meaningful Vesper interpretation.
- The trip branch's product value arrives late, after a questionnaire and auth.
- The dreaming branch is the strongest remnant of the Atlas-era mental model:
  abstract taste choices, early Photos permission, and a landing in You/Memory
  rather than a first loop among Places, Vesper, and Trips.
- The flow demonstrates neither multiplayer nor proactivity.
- Abstract interest and pace selections look more personalized than the
  available evidence justifies.
- Analytics emphasize steps viewed, completed, and permissions, not whether
  entry context survived or a useful artifact caused a return.

**Inference:** the generic onboarding is operationally mature but
product-conceptually behind the pivot. The answer is not a cosmetic rewrite.
The flow needs a value event before auth and a more coherent destination after
auth.

## 6. Entry-point inventory

The app has several materially different beginnings. They should share
continuity and trust rules, but they should not all pass through the generic
questionnaire.

| Entry | Verified current behavior | Product assessment |
| --- | --- | --- |
| **Direct install / cold launch** | Signed-out users enter generic onboarding. Signed-in users resolve pending work and otherwise fall back to Trips. | Important but context-poor. It needs a fragment-first value path rather than a longer profile funnel. |
| **Trip invite link** | Verified app link. Shows a privacy-safe preview, retains the token across auth, joins idempotently, records attendance, then enters the Trip. Manual code and clipboard recovery cover some install gaps. | The strongest acquisition loop and closest to the target philosophy. Optimize the invitee's personal payoff after join. |
| **Public Trip Story** | Public reading, plan seed, “plan similar,” auth continuation, and Trip/Vesper creation paths exist. Public sharing is hard-disabled by `STORY_SHARE_ENABLED = false`. | Strong future social proof, but dark. Do not make it a primary onboarding dependency until it is certified and intentionally enabled. |
| **OS share sheet** | Accepts URL/text/image and an audio path; extraction can produce a Place or review screen. A durable signed-out auth handoff was not found. Audio was built but remains parked. | Potentially the best Places-first wedge. The signed-out seam is currently the blocker, not extraction UI. |
| **Public place / venue page** | Editorial web shares exist with “Open in Vesper.” Generated URLs use a marketing host that is not the associated app-link host. Exact object and question continuity through auth is incomplete. | Useful acquisition surface, but web-to-app and auth continuity need one explicit contract. |
| **Proposal link** | Web landing under `/p/...` can open a custom-scheme route. The path is not in the verified app-link allowlist, and durable post-auth continuation was not found. | A high-intent decision entry with a fragile transport seam. |
| **Guest proposal capability** | Backend landing and post-auth resolver concepts exist, but no matching native `app/guest/[capabilityToken].tsx` route was found. | Appears incomplete. Fix as a bounded capability flow or retire the advertised path. |
| **Booking confirmation** | Backend `/c/{token}` landing can emit a custom-scheme link. No matching native route or app-link claim was found. | Prefer a useful web receipt unless the recipient already has a Trip relationship; do not force signup for a passive confirmation. |
| **Unpacked** | Public web artifact and a native token route exist, but the native screen ignores the token and asks for sign-in without preserving a clear continuation. | Atlas-era distribution. Keep as web proof, reframe its CTA as a fresh Vesper seed, or retire it; do not invest in a separate native onboarding funnel. |
| **Push notification** | Signed-out taps stage a delivery ID; after auth the backend re-resolves the current destination. Cold launch and stale fallback behavior are covered. | Strong re-entry infrastructure. Resume exact work; never send a returning user through a tour. |
| **Session recovery** | Hard auth lapses can preserve and later restore the interrupted route ahead of generic onboarding. | Correct philosophy: continuity is onboarding for returning users. |
| **Custom `guide://` scheme** | Can route local paths, with sanitization in native-intent handling. | A transport mechanism, not a reliable public acquisition strategy. |

No product implementation was found for App Clips, widgets, home-screen quick
actions, Spotlight, or a general deferred deep-link/attribution SDK. This is
not itself a gap to fill. The current invite fallback plus a robust entry
envelope may be enough for the near term.

## 7. The central continuity seam

The post-auth resolver in
[`travel-app/utils/postAuthHandoff.ts`](../../travel-app/utils/postAuthHandoff.ts)
already establishes an important precedence model. In simplified form:

```text
invite or guest capability
  > pending notification, re-resolved by the backend
  > interrupted route
  > public-story “plan similar”
  > signup safety
  > generic onboarding intent
  > Trips fallback
```

This is good architecture: one coordinator decides which interrupted job owns
the next screen. The larger problem is that several acquisition intents are
not first-class members of that model. Share payloads, place/venue intent,
proposal links, booking confirmation, and Unpacked continuity either bypass it
or are incomplete.

**Primary conclusion:** the highest-leverage onboarding work is preserving the
user's exact incoming job across transport, authentication, safety, and
materialization. Building more introduction screens before repairing this seam
would polish the wrong layer.

### 7.1 Proposed common entry envelope

Refactor the existing stores and resolver toward a small typed envelope rather
than introducing a new general framework:

```ts
type EntryEnvelope = {
  source: 'organic' | 'invite' | 'share' | 'story' | 'place' |
    'proposal' | 'booking' | 'notification' | 'recovery';
  objectRef?: { type: string; id?: string; token?: string; url?: string };
  intendedAction: string;
  safePreview?: Record<string, unknown>;
  authClass: 'public' | 'auth_to_commit' | 'private';
  privacyClass: 'public' | 'personal' | 'trip_private';
  createdAt: string;
  expiresAt: string;
};
```

The exact type should remain smaller than this sketch if possible. Its durable
invariants matter more than its fields:

1. preserve enough context to resume the original job;
2. store only a privacy-safe preview before authentication;
3. give tokens and payloads explicit TTLs;
4. consume commitment-bearing intents idempotently;
5. choose one destination owner after materialization; and
6. measure whether the context survived end to end.

## 8. Recent capabilities onboarding can now reveal

The August 2–12 history shows that the product substrate is much richer than
the current onboarding demonstrates. The useful product families are:

- **A clearer shell:** three roots, canonical Places map, retired Discover and
  Atlas entry points, and a secondary You portrait/settings/memory family.
- **A broader Vesper input and judgment surface:** “Ask, paste, or drop
  anything,” durable pending turns, structured/composed cards, contextual
  handoffs, workbench behavior, and map-viewport context.
- **Places as evidence rather than a feed:** canonical entity routing, richer
  venue/site pages, editorial registers, saved-unplaced concepts, map search,
  date and reachability context, comparisons, provenance, and relationship
  signals.
- **Trips as a living state surface:** open loops, Today Mapped, Near You, Trip
  Feel, “Take us somewhere,” group-trip entry, route facts, and Plan readiness.
- **Multiplayer and decisions:** richer invite previews, attendance, guest
  capabilities, proposals, corrections, private constraints, and group
  application receipts.
- **Live execution:** route, matrix, isochrone, booking-ledger, webhook,
  cancellation, refund, notification, and current-truth infrastructure.
- **Outcome learning:** private reflections, proposal corrections, visit
  affinity, relationship claims/outcomes, exposure/fatigue history, and AI run
  identity.
- **Distribution:** Trip Stories, plan-similar, postcards, Unpacked, and shared
  editorial pages—several of which remain dark or legacy.

Many recent home capabilities are internal opt-in rather than production
defaults, and several distribution surfaces are hard-disabled. The product
should not make its onboarding promise depend on dark features. The immediate
opportunity is to use already-active primitives—Vesper interpretation, Places
evidence, durable Trips, and invites—to produce one legible loop.

## 9. Target onboarding by entry

Every entry should use the same basic recipe:

```text
preserve incoming intent
  → show a privacy-safe preview
  → perform the smallest useful action
  → invite one acceptance or correction
  → authenticate at commitment
  → create or update one durable artifact
  → expose ownership across the three roots
  → create a return trigger
```

### 9.1 Organic install: fragment first

**Proposal:** replace the “trip or dreaming” fork with a single generous
prompt: **“What are you trying to make happen?”**

Offer examples without turning them into a taxonomy:

- plan a trip;
- paste a place, link, or half-formed idea;
- help me find a starting point; or
- join someone else's trip.

The composer can accept a short sentence, link, or image. Vesper should return
one concrete and inspectable interpretation before authentication—for example,
a trip shape, a place fit judgment, or two plausible starting directions. Ask
for one correction. Authenticate when the user chooses to save, continue,
share, or turn the judgment into a Trip.

The result should be a durable Trip, saved Place relationship, or private
Vesper thread with an explicit next event. A blank Vesper conversation is not
enough; a generic diary/profile destination is no longer the right default.

### 9.2 Invite: preserve the thin contextual path

Do not add generic onboarding before or after join. The invite already provides
the missing cold-start priors: people, destination, dates, and a reason the user
is present.

After join, reveal one piece of **personal** value, not merely group state:

> “You said quiet mornings. Thursday is still open, so Vesper kept it loose.”

Then offer the smallest useful action: confirm attendance, add a private
constraint, inspect the Plan, or ask Vesper a private question. Ask for push
only when the user chooses a reason to be notified.

### 9.3 Share sheet: turn external fragments into Places value

Persist the share payload locally with a TTL before making network calls. Show
a safe extraction preview: what Place or idea was recognized, confidence, and
anything that remains ambiguous. Let the user correct it. Ask for auth to save
or attach it, then land on the exact Place with “why it fits” and an optional
Trip attachment.

This is a particularly coherent wedge because it starts with behavior users
already have—sending themselves travel fragments—and connects all three roots
without requiring a new content habit.

### 9.4 Public story: proof before personalization

When certified and enabled, let the public story demonstrate product quality.
Then ask what the new user wants to carry forward or change. Vesper should turn
that selection into a private seed before authentication; auth saves the seed
as a Trip or private thread. Avoid a generic “make one like this” copy flow
that ignores the person's constraints.

### 9.5 Place or venue page: one contextual question

Allow the editorial object to stand on its own publicly. Invite one question:
“Would this work with my parents?”, “Is this worth crossing town for?”, or
“Could this fit Saturday?” Vesper can answer from public evidence, clearly
bounded by what it does not know. Authentication saves the exact Place,
question, and answer; it must not return the user to an empty root.

### 9.6 Proposal or guest capability: resume the decision

Show only privacy-safe context before auth. After auth, open the exact proposal,
allow one decision or response, and show a receipt explaining what changed and
who can see it. Offer a private Vesper question as a secondary path. This flow
is about governed participation, not learning the whole app.

### 9.7 Booking confirmation: default to useful web receipt

A passive recipient should not need an account merely to confirm that a
booking exists. Keep the receipt useful on the web. Offer app entry only when
there is a real action—join the associated Trip, manage the booking, receive
updates, or coordinate with the group—and preserve that action through auth.

### 9.8 Unpacked: social proof or retirement

Do not rebuild an Atlas-specific native funnel. Preserve Unpacked as a public
artifact if it earns distribution, but direct its CTA toward a new Vesper seed
or relevant Place relationship. Otherwise retire the native route cleanly.

### 9.9 Push and session recovery: no onboarding detour

Resume the exact current object. If it is stale, explain that fact and offer
the nearest safe owner surface. Returning users experience continuity as
product quality; a tour would be a regression.

## 10. What should be learned when

The onboarding knowledge model should be progressive:

| Moment | Appropriate knowledge | Avoid |
| --- | --- | --- |
| Before auth | Incoming fragment, public object, temporary correction, privacy-safe preview | Durable sensitive profile claims or invisible inference |
| At first commitment | Identity, necessary safety/access constraint, target Trip or private artifact | Broad lifestyle questionnaire |
| During real use | Concrete place choices, proposal corrections, companions, budget/pacing constraints | Pretending one action is a stable taste law |
| After an outcome | What happened, whether it fit, what should change next time | Automatic memory promotion without consent or evidence |
| In You | Review, correct, delete, explain, and govern accumulated knowledge | Making You the main first-value destination |

The first session should ask only for the information required to make the next
judgment safer or materially better. Everything else can be learned from use.

## 11. Activation and measurement

“Completed onboarding” is an implementation event, not the product outcome.
The core activation model should measure:

1. **entry-context survival** — did the original token, place, payload,
   question, or interrupted object survive to the destination?
2. **time to useful interpretation** — how quickly did Vesper produce a
   concrete, inspectable result?
3. **first steering event** — did the user accept, reject, or correct it?
4. **time to durable artifact** — when did a Trip, Place relationship,
   proposal response, or private thread become real?
5. **return-trigger creation** — did the session establish an invite response,
   pending decision, live event, monitoring request, or explicit next step?
6. **artifact return** — did the user return to the same job at D1 and D7?
7. **compounding quality** — did the next occasion require less restatement or
   produce a better accepted judgment?

Entry-specific funnels should remain visible:

- invite: preview → private signal → auth → join → attendance or private ask;
- share: received → parsed → reviewed/corrected → saved → attached to Trip;
- story: read → personalized seed → auth → Trip/thread;
- organic: fragment → interpretation → correction → artifact;
- proposal: safe preview → auth → exact proposal → decision → receipt.

Cross-root usage is useful only when it reflects one coherent job. “Visited two
tabs” is not an activation metric by itself.

## 12. Recommended execution sequence

### P0 — Repair entry continuity

1. Inventory every public path, native route, custom-scheme path, and auth
   continuation in one executable matrix.
2. Add the smallest common `EntryEnvelope` semantics to the existing handoff
   coordinator and intent stores.
3. Cover share, public place/venue, proposal, booking, and Unpacked decisions.
4. Align iOS associated domains, Android intent filters, AASA paths, native
   routes, backend landing-page comments, and tests.
5. Either complete or explicitly retire the missing guest and booking native
   routes.
6. Instrument context survival and idempotent consumption.

### P1 — Reframe organic onboarding around first judgment

1. Replace the dreaming/diary branch with fragment-first intake.
2. Produce one bounded Vesper interpretation before auth.
3. Capture one correction and carry it into the created artifact.
4. Move Photos and memory-building prompts to the relevant use moment.
5. End in the artifact owner, with a visible next step.

### P2 — Perfect the two strongest wedges

1. Preserve and polish the invite flow, especially the post-join personal
   payoff.
2. Make signed-out share capture durable end to end.
3. Certify both paths with deterministic contract tests plus real-device
   evidence at the transport and permission boundaries.

### P3 — Enable public proof selectively

Enable Trip Story and public Place acquisition only after privacy, link routing,
auth continuation, and artifact creation are certified. Do not light all dark
distribution features together.

### P4 — Retire or reframe legacy distribution

Resolve Unpacked, postcards, legacy Atlas routes, and misleading landing pages
so every advertised doorway belongs to the current thesis.

## 13. What not to build yet

- A long explanatory tour of Trips, Vesper, and Places.
- A new onboarding platform beside the existing progress and handoff systems.
- A large stable taste profile based on first-session quiz answers.
- New acquisition surfaces such as App Clips or widgets before current links
  and share capture preserve intent reliably.
- A requirement that every user touch all three roots in session one.
- Activation dashboards built around signup or screen completion alone.
- Onboarding promises that depend on internal-only or hard-dark features.

The product already has enough substrate. The near-term work is to make one
incoming intention travel coherently through it.

## 14. Decisions to make

The investigation leaves a short founder/product docket:

1. **Organic first input:** should the default be a universal Vesper composer,
   or a small set of job-oriented starts feeding the same composer?
2. **Pre-auth compute boundary:** what useful judgment can be produced safely
   and economically before identity?
3. **First durable object:** under which conditions should the result become a
   Trip, Place relationship, or private Vesper thread?
4. **Dreaming branch:** retire it outright, or preserve only its strongest
   language as examples in fragment-first intake?
5. **Share wedge:** is share capture the primary Places acquisition experiment
   after invites?
6. **Public link ownership:** should marketing-host place URLs become verified
   app links, or should the web intentionally remain the public first surface?
7. **Legacy paths:** complete, web-only, or retire proposal guest, booking
   confirmation, and Unpacked native routes?
8. **Activation:** which single artifact-and-return event becomes the company
   definition of activated for each entry class?

## 15. Research and implementation source map

### Product and workspace context

- [Product Thesis](../../travel-agent/docs/product/Product%20Thesis.md)
- [Product Model](../../travel-agent/docs/product/Product%20Model.md)
- [What We Believe](../../travel-agent/docs/product/What%20We%20Believe.md)
- [Discover and Atlas retirement decision](../decisions/2026-08-12-retire-discover-and-atlas-product-surfaces.md)
- [Broader product-loop and test strategy](product-loop-coherence-maestro-and-environment-strategy-2026-08-12.md)
- [Current State](../status/current-state.md)

### Primary implementation surfaces reviewed

- [`travel-app/app/onboarding.tsx`](../../travel-app/app/onboarding.tsx)
- [`travel-app/app/onboarding-safety.tsx`](../../travel-app/app/onboarding-safety.tsx)
- [`travel-app/utils/onboardingIntent.ts`](../../travel-app/utils/onboardingIntent.ts)
- [`travel-app/utils/onboardingProgress.ts`](../../travel-app/utils/onboardingProgress.ts)
- [`travel-app/utils/onboardingAnalytics.ts`](../../travel-app/utils/onboardingAnalytics.ts)
- [`travel-app/utils/postAuthHandoff.ts`](../../travel-app/utils/postAuthHandoff.ts)
- [`travel-app/app/+native-intent.ts`](../../travel-app/app/+native-intent.ts)
- [`travel-app/app/invite/[slug].tsx`](../../travel-app/app/invite/%5Bslug%5D.tsx)
- [`travel-app/app/share-capture/index.tsx`](../../travel-app/app/share-capture/index.tsx)
- [`travel-app/app/unpacked/[token].tsx`](../../travel-app/app/unpacked/%5Btoken%5D.tsx)
- [`travel-app/app.json`](../../travel-app/app.json)
- [`travel-app/constants/featureFlags.ts`](../../travel-app/constants/featureFlags.ts)
- [`travel-agent/backend/api/routes/invite_landing.py`](../../travel-agent/backend/api/routes/invite_landing.py)
- [`travel-agent/backend/api/routes/proposal_landing.py`](../../travel-agent/backend/api/routes/proposal_landing.py)
- [`travel-agent/backend/api/routes/booking_confirmation_landing.py`](../../travel-agent/backend/api/routes/booking_confirmation_landing.py)
- [`travel-agent/backend/api/routes/atlas_unpacked_landing.py`](../../travel-agent/backend/api/routes/atlas_unpacked_landing.py)

### External design research

- [Microsoft Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/research/project/guidelines-for-human-ai-interaction/)
- [Google PAIR Guidebook](https://pair.withgoogle.com/guidebook/)
- [Apple Human Interface Guidelines: Onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding)
- [Android permission request guidance](https://developer.android.com/training/permissions/usage-notes)

## 16. Working synthesis

The August pivot gives onboarding a simpler job. It does not need to explain an
expanding feature portfolio. It needs to prove one product proposition:

> Bring Vesper a real fragment of intent; it will interpret that fragment with
> place and people context, let you steer the judgment, turn the accepted result
> into durable shared or private state, and get better as reality supplies
> outcomes.

The current app has much of the necessary substrate. The generic flow, however,
still teaches a pre-pivot category, and several high-intent entry paths lose
their context at authentication or link boundaries. Repairing that continuity,
then giving organic users one pre-auth judgment and one steering moment, is the
most direct path to earlier perceived value, clearer product identity, and
higher stickiness.
