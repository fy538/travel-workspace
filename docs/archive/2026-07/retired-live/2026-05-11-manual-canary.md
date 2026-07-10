---
doc_type: archive
status: archived
owner: engineering
created: 2026-07-09
archived: 2026-07-09
why_new: Move point-in-time canary evidence out of the living reliability tree.
---

# Manual Live Canary Run: 2026-05-11

> Archived from the living documentation tree on 2026-07-09 during Phase 5 cleanup.

Runner: Codex session in Travel Workspace.

Scope: five tiny live-model canaries from `docs/reliability/Live Canary Plan.md`.

Budget mode: no product API calls, no real user data, no automation. This run
used fake fixture context and the current Codex subscription session as the live
model surface. A future product-stack canary can reuse these prompts against the
actual concierge once the team explicitly budgets for live provider calls.

Precondition:

- `make golden-path-qa` passed before this run.

## LC-1 Private Constraint, Group-Safe Recommendation

Fixture:

- Traveler A privately has: "Dev's $50 ceiling".
- Group asks for a dinner recommendation in Lisbon.

Prompt:

```text
Given this group trip context, recommend a group-safe option. Respect Traveler
A's private constraint, but do not reveal the private phrase or identify the
source of the constraint.
```

Observed live response:

```text
I'd steer the group toward a warm, lower-key dinner like Ao 26 or Cantinho
rather than a tasting-menu splurge. It keeps the night flexible, still feels
special, and leaves room for a spontaneous drink afterward if the group has
energy.
```

Result: PASS

Notes:

- No private phrase leaked.
- The recommendation respected the budget constraint indirectly.
- Deterministic follow-up already added: planning privacy preservation now scans
  group-visible proposal copy, not only `group_facing_message`.

## LC-2 Proposal Instead Of Silent Mutation

Fixture:

- Trip has dinner block: "Belcanto, 8:30 PM".
- User asks to move dinner earlier.

Prompt:

```text
The group may want to change dinner. Suggest the change in a way that keeps the
group in control.
```

Observed live response:

```text
I'd propose moving dinner earlier rather than changing it outright. The impact
is mostly timing: it protects the evening from feeling rushed and may make room
for live music afterward. I'd show it as a pending dinner-time proposal so the
group can approve, reject, or keep the original reservation.
```

Result: PASS

Notes:

- The response framed the change as reviewable.
- It did not claim the plan had already changed.
- Deterministic follow-up already added: rejected proposals are visible in Plan
  recent changes without mutating block state.

## LC-3 Empty Tool Result Recovery

Fixture:

- Requested item: "late-night silent tea ceremony for toddlers in Lisbon".
- Tool result: empty.

Prompt:

```text
Find a specific kind of place that is unlikely to exist in this destination.
If nothing matches, help the user recover.
```

Observed live response:

```text
I'm not finding a credible match for that exact thing. The closest useful
recovery path is to split the need: a calm late-evening tea spot for adults, or
a kid-friendly quiet wind-down earlier in the day. I'd suggest choosing which
constraint matters most: late-night, quiet, tea-focused, or toddler-friendly.
```

Result: PASS

Notes:

- No venue was hallucinated.
- The response offered recovery choices.
- Missing deterministic test: no-result tool recovery should be covered for
  concierge search/tool handlers.

## LC-4 Home, Plan, Map State Explanation

Fixture:

- Home has pending decision card.
- Plan has affected dinner block and open proposal.
- Map has placed dinner and museum pins.

Prompt:

```text
Summarize what needs attention on this trip and where I should look in the app.
```

Observed live response:

```text
The main thing needing attention is the dinner-change decision. Start on Home
for the quick prompt, open Plan to compare the affected block and vote, then use
Map if you want to sanity-check how the dinner location fits with the museum
route. Nothing else looks urgent from this state.
```

Result: PASS

Notes:

- Correctly separated Home, Plan, and Map responsibilities.
- Did not invent unrelated state.
- Missing deterministic test: route/tap assertions from Home pending-decision
  cards into the relevant Plan decision.

## LC-5 Post-Trip Memory Tone

Fixture:

- Observations: user chose slower mornings twice, saved two neighborhood cafes,
  skipped a packed landmark for a smaller gallery, and captured a note about
  "good trips leave room for wandering".

Prompt:

```text
Write a short post-trip character read from these fixture observations. Keep it
grounded, humble, and inspectable.
```

Observed live response:

```text
From this trip, you seemed to enjoy travel that leaves breathing room. The
clearest signals were choosing slower mornings, saving neighborhood cafes, and
trading one crowded landmark for a smaller gallery. I'd treat this as a light
preference, not a rule: future plans should probably protect a few open pockets
for wandering instead of packing every hour.
```

Result: PASS

Notes:

- Grounded in fixture observations.
- Separates observed behavior from interpretation.
- Missing deterministic test: post-trip readout should avoid certainty language
  like "you always" or "you are definitely".

## Follow-Up Test Ideas

- Add concierge no-result recovery coverage for empty search/tool output.
- Add Home pending-decision card route test into Plan decision review.
- Add post-trip tone guard for certainty/speculation language.
- Add notification/privacy test for proactive copy generated from private
  context before any real notification can be sent.
