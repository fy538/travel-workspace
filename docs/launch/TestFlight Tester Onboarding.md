# TestFlight Tester Onboarding

Two paste-targets in one doc:

1. **What to Test** — pastes into TestFlight's "What to Test" field
   per build. Testers see this in the TestFlight app before they
   download.
2. **Tester welcome email** — manual send when you invite each tester.
   Sets expectations the TestFlight UI can't.

---

## A) "What to Test" field (TestFlight, per build)

≤ 4000 chars; markdown rendering is partial — keep formatting plain.

```
Thanks for taking Vesper for a real trip.

Vesper is a travel concierge — it plans the trip with you, talks to
your group on your behalf, and remembers the place so the next trip
is sharper than the last. The most useful thing you can do is plan a
real trip you'd actually take in the next 6-8 weeks.

WHAT TO DO

1. Tell Vesper what trip you're thinking about — destination, dates,
   who's coming. Stay in the 1:1 thread for the first 5-10 minutes.
2. Add your friends. Vesper will mint an invite link for each person —
   send them via iMessage. They'll land in the group chat after they
   sign in.
3. Let Vesper run the group conversation for a day or two. It will
   surface proposals as cards — approve, ask for an alternative, or
   skip.
4. When the trip starts, open the trip-home tab. Try "Hear about this
   place" on a venue you arrive at. Or don't — silence is a feature.
5. After the trip, the Memory tab will compose a Trip Story. Read it,
   edit any section, add photos. This is the artifact that proves
   Vesper was worth using.

WHAT TO SEND FEEDBACK ON

What we most want to hear:

• Moments when Vesper said something specific to your group that no
  generic travel app could have said. (This is the moat. We need to
  know it lands.)
• Moments when Vesper said something obviously wrong, dumb, or
  generic. (Show us where the model is still thin.)
• Anything that broke or hung for more than 15 seconds.
• Anything in the post-trip Memory artifact that surprised you —
  good or bad.

What you don't need to send feedback on:

• Polish-level UI issues — we know about most of them.
• "It would be cool if Vesper could also do X" — feature requests
  are welcome but the immediate bar is "does the current product
  feel worth using."
• Performance on cold start. First reply after the app has been
  closed for a while will be slow. That's the dyno waking up.

HOW TO SEND FEEDBACK

• In-app: Me tab → Send Feedback. This includes the trip context
  automatically.
• Bugs that crash the app: TestFlight's built-in screenshot →
  feedback path also works.
• Direct: text or email Tiger anything urgent.

KNOWN ROUGH EDGES IN THIS BUILD

• First message in a fresh trip can take 10-20s while the agent loads
  the trip context. Subsequent messages are fast.
• The voice companion is best on a real trip in a real place — it
  uses geofencing to choose what to say. Standing in your kitchen
  won't give you a representative experience.
• If a group member doesn't accept the invite within 7 days, the link
  expires. We'll let you re-mint without losing the group state.
• The booking flow currently routes you out to the provider's site
  (Viator, Booking.com) for the final step. In-app booking lands in
  a later build.

Privacy: what you say to Vesper in the 1:1 thread stays in the 1:1
thread. Vesper synthesizes a group plan from everyone's private
input but never exposes individual preferences to the shared chat.
You can delete your account from Me → Account at any time and all
of your data goes with it.

— Tiger
```

---

## B) Tester welcome email / message (send manually when you invite)

≤ 600 words. iMessage / email friendly. The TestFlight invite alone
doesn't carry tone; this does.

**Subject:** Vesper — the early invite

```
Hi {first_name},

You're one of the first 10 people I'm putting Vesper in front of.

The pitch in one line: Vesper plans the trip, talks to your group on
your behalf, and remembers the place so the next trip is sharper than
the last. It's the concierge relationship a great travel writer has —
the one who knows your taste, your dynamics, and the third-best
restaurant in the neighborhood.

What I'm actually asking of you: pick a real trip. Something you'd
take in the next 6-8 weeks with at least two other people. Walk
Vesper through it. Pull your group in once you've spent 5-10 minutes
in the 1:1 thread getting comfortable.

The trip can be small. A weekend in Asbury Park is fine. A week in
Tokyo is fine. The point is that it's real — Vesper's whole thesis
is that the product compounds over real trips, not over trying-it-out
sessions.

What I'd love to hear about:

1. When did Vesper say something that felt like it actually knew your
   group? That's the moment we built the whole thing for. If it
   happens, tell me which message.

2. When did Vesper say something obviously wrong or generic? Those
   are the moments I need to fix next. Quote the message.

3. Did the post-trip Memory artifact feel worth keeping? Or did it
   feel like a template?

Send feedback in-app (Me → Send Feedback) — it auto-attaches the
trip context, so I don't have to ask "which trip?" Send anything
urgent direct to me.

Two things to expect:

• First message can be slow if the app has been backgrounded a while
  — the agent is cold-starting.
• The voice companion is calibrated for real trips, real arrivals.
  Trying it from your couch won't be representative.

Privacy: what you tell Vesper privately stays private. The agent
synthesizes a group plan from everyone's inputs without exposing
individuals' constraints to the group. You can wipe everything from
Me → Account → Delete Account if you change your mind.

Thanks for the time. I'll listen to whatever you send me.

— Tiger
```

---

## C) The first 10 testers — who and why

This isn't paste-content; it's planning. The first 10 invites are the
single most important growth decision before public launch.

**Selection criteria** (any 2 of 3 qualifies):

- **Real Organizer**: actually plans 4+ trips/year, including at least
  one group trip in the next 8 weeks
- **Will give honest critical feedback**, not just "looks great"
- **Has the iOS device** (TestFlight is iOS-only for this build)

**The wedge cohort to aim for**:

| Slot | Profile | Why |
|---|---|---|
| 1-3 | Organizers in your direct network with trips already booked or planning | Fastest signal — the trip exists, not a hypothetical |
| 4-6 | Friends of friends who fit Organizer archetype, intro'd via Slot 1-3 | Tests the cold-invite UX |
| 7-9 | Existing travel/design/product peers who'll tear it apart | Critique signal — different from user signal |
| 10 | One "neutral" tester — neither in your network nor a peer | Sanity check on what's obvious vs. learned |

**What NOT to do**:
- Don't invite 25 people. The eval substrate isn't deep enough to
  digest 25 simultaneous trip streams.
- Don't invite anyone who's still in "would love to try it" mode but
  doesn't have a real trip coming up. Wasted slot.
- Don't ship the invite at end of week without a Sunday-night
  check-in pattern. First 72 hours of feedback are the most useful;
  you have to be reachable.

---

## D) The 7-day signal you're looking for

After the first 10 testers have had the app for a week, the question
is whether the wedge is real. Specifically:

| Signal | Threshold | What it means if you hit it |
|---|---|---|
| ≥3 testers sent a message specific to "Vesper said something my group needed to hear" | The compounding-memory thesis has surface-level evidence |
| ≥1 tester reached the post-trip Memory artifact and kept it | The artifact is doing the come-back-for-Trip-2 work |
| <5 P0/P1 bugs reported across all 10 testers | The substrate is launch-worthy |
| ≥1 tester invited a friend to their group who signed up | The invite UX works end-to-end on cold users |

Less than 2 of those: hold launch, fix the gap.
3 of 4: cautious go on a wider TestFlight (50 users).
4 of 4: open the public TestFlight link.
