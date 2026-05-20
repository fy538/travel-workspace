# App Store Connect Copy — Vesper

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

> Six characters. The product is the concierge relationship and shares
> the agent's name — single noun, single mental object (Brand Identity §1).

---

## Subtitle (30 chars max)

```
The trip, before the asking
```

> 27 chars. Brand-voice example pattern from §10 ("Your trip, before
> everyone starts asking for the itinerary"). Avoids the generic "AI
> travel planner" register that places Vesper in the wrong category.

**Alternates if the first reads wrong on the listing card:**
- `Plans the trip. You enjoy it.` (29)
- `Group trips, without the chase` (29)
- `A trip your group already loves` (30)

---

## Promotional text (170 chars max — editable without re-review)

```
For the friend who plans everything. Vesper handles the group ask, the
booking, the day-of nudge — and remembers the place so the next trip is
sharper than the last.
```

> 168 chars. Speaks directly to the Organizer archetype (the launch
> wedge). Mentions the compounding memory thesis without naming the
> mechanism. Stays specific.

---

## Description (4000 chars max)

```
Vesper is a place-aware travel concierge for the friend who plans
everything.

You name the trip. Vesper handles the rest — quietly working the group,
holding the calendar, learning what each person actually wants without
exposing anyone's constraints to the chat. The plan that comes back is
specific to who you are, who you're going with, and where you're going.

Vesper isn't another AI assistant. It's a concierge relationship that
gets sharper every trip.


WHAT VESPER DOES

• Plans the trip with you, in a 1:1 thread the group never sees. Your
  preferences, your budget, your group dynamics — never leaked to the
  shared chat.

• Talks to your group on your behalf. Vesper sits in the group thread
  and surfaces a plan everyone can live with, without anyone having to
  spell out what they don't want to do.

• Books restaurants, hotels, activities. Sends a brief to the venue
  about your group so the host knows you're a birthday or that two
  guests don't eat shellfish — without you having to explain it.

• Narrates the place as you arrive. Optional voice companion that knows
  what's worth saying about the bairro you just walked into — and when
  to stay silent.

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

Most travel apps end where Vesper begins. Booking sites take your
money. Planning tools make a checklist. Group apps trade messages.
None of them know you. None of them remember what mattered. None of
them work the room.

Vesper builds a relationship across trips. Trip 1 is the introduction.
By Trip 3 it knows you better than your group does — which restaurant
you'll skip, which neighborhood you'll lose an afternoon in, which
constraint you don't want to repeat out loud.


PRIVACY

What you tell Vesper privately stays private. Group plans are derived
from your inputs without exposing them — the agent does the diplomacy
so you don't have to. We never sell data, never train on your
conversations, and you can delete everything from the app.

For the full picture: settings.travelagent.app/privacy.


REQUIREMENTS

iOS 17 or later. iPhone. A real trip — Vesper is meaningless without
one.


Vesper plans the trip. You enjoy it.
```

> 2780 chars. Headlines and section breaks follow Apple's plain-text
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
