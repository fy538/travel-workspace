# App Store Connect Copy — Vesper

> **Release scope, not company category (revised 2026-08-24):** This copy describes the
> current trip-centered first release. The company model is personal and
> multiplayer intelligence for the lived world; group travel is the launch
> wedge and first demanding specialization. Keep App Store claims constrained to behavior the submitted
> build actually demonstrates. The external messaging hierarchy is recorded in
> the [experiential-responsibility messaging decision](../decisions/2026-08-24-adopt-experiential-responsibility-messaging.md);
> this release copy remains deliberately narrower.

Paste targets for App Store Connect → App Information / App Store / iOS App.
Voice is locked in `Travel App/docs/Brand Identity.md` §10 — confident,
specific, restrained. Not aspirational-luxe, not productivity-coded, not
gamified.

When the App Store Connect listing is created (OAI #2), copy each block
below into the matching field. The character counts are the App Store
2026 limits.

---

## App name (30 chars max)

```
Vesper
```

> Six characters. The product and its intelligence share one name—single noun,
> single mental object (Brand Identity §1).

---

## Subtitle (30 chars max)

```
Better trips for the group
```

> 26 chars. States the experienced outcome rather than the planning feature and
> keeps the multiplayer wedge legible.

**Alternates if the first reads wrong on the listing card:**
- `Better trips, not just plans` (28)
- `Group trips, without the chase` (29)
- `A trip your group will love` (27)

---

## Promotional text (170 chars max — editable without re-review)

```
Vesper helps your group decide and adapt together, keeps one shared plan
coherent as reality changes, and carries forward what actually mattered.
```

> Speaks to the whole group while preserving organizer relief. Mentions the
> continuity thesis without claiming that external learning is already proven.

---

## Description (4000 chars max)

```
Vesper helps groups have better trips—not just plan them.

It understands each person privately, grounds decisions in the places and
conditions involved, and helps the group decide and adapt together in the real
world. The shared result can reflect private needs without exposing who needed
what.

Vesper stays oriented to the people, place, and shared Plan, and learns from
what actually mattered so the next experience needs less explanation.


WHAT VESPER DOES

• Plans the trip with you, in a 1:1 thread the group never sees. Your
  preferences, your budget, your group dynamics — never leaked to the
  shared chat.

• Helps the group decide without exposing private constraints. Vesper can show
  the relevant tradeoffs and a group-safe proposal; people still choose what
  the decision means and how to talk to one another.

• Keeps plans and booking details together. Add an existing reservation
  or follow an external provider link, then keep the shared itinerary
  current for everyone. Vesper does not make booking commitments.

• Helps when the plan changes. Proposed itinerary edits remain reviewable,
  and accepted changes update the shared plan instead of creating another
  competing version in chat.

• Renders the trip back as a memory artifact. After you come home,
  Vesper writes the trip up in your voice with your photos slotted in.
  A keepsake that doubles as input for the next trip.


WHO VESPER IS FOR

• The Organizer. The one in every friend group who plans everything.
  Vesper makes you dramatically better at this — and gives you relief
  from the coordination burden.

• Groups planning a multi-day trip together. Vesper synthesizes
  individual preferences privately so the group conversation stays
  about the trip, not about logistics.

• Travelers who care about the place. Not the most photogenic
  itinerary — the one that fits who you actually are.


WHY VESPER IS DIFFERENT

Maps are excellent at places, routes, and current world truth. Booking products
provide inventory and transactions. Assistants explain and synthesize. Group
chats and planners hold discussion and artifacts. Vesper can connect those
parts around a different responsibility: helping this experience work for the
people actually living it.

Vesper can carry forward what mattered across trips: which places fit,
what the group changed, and which constraints should not need repeating.
That evidence is useful only when it makes the next decision better.


PRIVACY

What you tell Vesper privately stays private. Group plans can reflect your
inputs without attributing them. Vesper reduces coordination friction; it does
not replace human care, conversation, or expression. We never sell data, never train on your
conversations, and you can delete everything from the app.

For the full picture: settings.travelagent.app/privacy.


REQUIREMENTS

iOS 17 or later. iPhone. The current release is designed around a real
group trip.


One group. One shared trip that stays coherent.
```

> Character count verified below the 4000-character limit. Headlines and section breaks follow Apple's plain-text
> formatting (newlines render as paragraph breaks). Pulls language
> verbatim from Brand Identity §2 (essence) and §10 (voice samples).

---

## Keywords (100 chars max, comma-separated)

```
trip planner,group travel,concierge,itinerary,booking,vacation,memory,journal,travel ai,organizer
```

> 99 chars. No spaces between keywords (Apple counts spaces). Avoids
> brand names of competitors (Apple may reject). "organizer" mirrors
> the launch wedge. "memory" + "journal" anchor the post-trip artifact
> for searches outside the typical travel-planner lane.

---

## Support URL

```
https://travelagent.app/support
```

> Defer the actual `/support` route until the first beta tester ships a
> bug report. For TestFlight review, a plain text page at this URL
> with the in-app feedback path + email fallback is enough.

---

## Marketing URL (optional — only set when there's a real landing page)

```
https://travelagent.app
```

> If the root `travelagent.app` redirects to App Store or shows a
> minimal "Vesper" splash, set this. If it returns 404, leave blank —
> Apple flags marketing URLs that 404.

---

## Privacy policy URL

```
https://travelagent.app/privacy
```

> Already served by the backend at `GET /privacy` per the May 13
> commit. Verify with `curl -fsS https://travelagent.app/privacy` once
> deployed.

---

## Copyright (one line)

```
© 2026 Vesper
```

> No incorporation suffix until there's one to write. Apple accepts a
> plain brand name.

---

## Category

**Primary:** Travel
**Secondary:** Lifestyle

> Don't pick "Productivity." Brand Identity §3 anti-list rules out the
> productivity-coded register; the category should match.

---

## Age rating

| Question | Answer |
|---|---|
| Cartoon or fantasy violence | None |
| Realistic violence | None |
| Sexual content / nudity | None |
| Profanity / crude humor | None |
| Alcohol, tobacco, drug references | Infrequent / Mild — Vesper references bars and wine when relevant |
| Mature themes | None |
| Gambling | None |
| Horror / fear | None |
| Medical / treatment info | None |
| Unrestricted web access | No |
| User-generated content / social networking | **Yes** — group chat |

> Resulting rating: **4+** in most stores; **12+** if Apple weights the
> alcohol mention. Either is fine for the audience.

---

## Screenshots

Required sizes (iOS 17+):
- 6.7" (iPhone 15 Pro Max, 1290×2796)
- 6.5" (iPhone 11 Pro Max, fallback — 1284×2778)

Capture from a real device on a real trip session. Avoid:
- Lorem-ipsum placeholders (Apple rejects on sight)
- Screenshots of the dev SKIP_AUTH user
- Screenshots that show another product's content

**Suggested order (5 screenshots):**

1. **Trip card hero.** A real trip card (Brand Identity §11 wordmark
   visible). The single most-shared surface.
2. **1:1 with Vesper.** A planning thread where Vesper has asked a
   specific question — "8 or 8:30 for Wednesday?" type prompt.
3. **Group chat with a proposal.** Shows the privacy-mediated synthesis
   — Vesper proposed a restaurant the group can react to with one tap.
4. **Memory surface.** The Trip Story rendered as an artifact. Photo
   slots filled in.
5. **Voice / narration card.** The dark immersive narration screen
   while in-trip.

**What we don't ship as screenshots:** the Me tab, the settings
screens, the dev privacy-audit screen, the discover feed without
content.

---

## What's New (per build, ≤4000 chars)

Use the same brand voice. Example for the first TestFlight build:

```
First TestFlight. The plan is to keep this small until the basics work:
the 1:1 thread, the group surface, the memory artifact.

Known rough edges: occasional slow first reply when the agent is cold;
the voice companion is opt-in and best on a real trip.

Send feedback through the Me tab. Thank you for testing.
```

---

## Last review

Each field above is committed in this doc as the source of truth. When
something changes, edit here first and copy to App Store Connect.
Never edit in App Store Connect without backporting — the next reviewer
prompts come from this file.
