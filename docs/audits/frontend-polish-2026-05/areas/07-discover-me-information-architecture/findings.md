# Discover + Me Information Architecture Polish Findings

## Summary

Discover today is trying to be the city index, global search, personalized feed, friend feed, event browser, editorial guide shelf, nearby-mode switcher, speculative query tool, and trip-creation funnel all at once. Its clearest one-sentence job should be: **help me understand what is worth noticing in this place.**

Me today is a profile, taste-memory surface, inbox, trip archive, people graph, saved-place shelf, voice-log shelf, privacy center, and settings menu. Its clearest one-sentence job should be: **show and tune what Vesper knows about me.**

No P0s. The dogfood risk is P1/P2 polish: both tabs feel more like accumulated dashboards than the restrained, opinionated, editorial companion described in Vesper's doctrine. This conflicts with the internal brief's "leather travel journal, not a SaaS dashboard" rule (`Travel App/docs/Design Language.md:55-64`) and with current platform guidance that prioritizes clear hierarchy, grouping, and simple primary task flows: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [Material accessibility](https://m2.material.io/design/usability/accessibility.html), [WCAG 2.2 target size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum), and [IBM progressive disclosure](https://www.ibm.com/docs/en/technical-content?topic=practices-progressive-disclosure).

## Findings

### P1 - Discover has too many equal first-order destinations

`PILLS` exposes six peer tabs: `Angles`, `Friends`, `For you`, `Events`, `Trending`, and `Guides`, even though the inline comment says Angles is the only tab backed by the content graph and the others are overlays (`Travel App/app/(tabs)/discover/index.tsx:53-56`). Those six pills sit directly under a sticky search field (`Travel App/app/(tabs)/discover/index.tsx:675-699`), before the actual place thesis appears (`Travel App/app/(tabs)/discover/index.tsx:754-805`).

This makes Discover's primary job ambiguous. Angles, For You, Events, and search each look like plausible main modes. Apple's HIG frames hierarchy as controls elevating and distinguishing content, while Material notes that every added button, image, and line of text increases UI complexity. Here, the top chrome is asking the user to choose an operating mode before Vesper has expressed an opinion.

### P1 - Discover's first viewport is control-led, not editorial-led

The default Angles branch opens with search, six nav pills, a small "The index for" caption, city picker, Near Me toggle, result count, an `All / By Lens` toggle, and only then the angle cards (`Travel App/app/(tabs)/discover/index.tsx:675-699`, `Travel App/app/(tabs)/discover/index.tsx:754-805`, `Travel App/app/(tabs)/discover/index.tsx:897-943`). The `AngleCard` component says it is "editorial, not functional" (`Travel App/components/angles/AngleCard.tsx:8-11`), but the surrounding hierarchy makes the page feel like a browse console.

The modules competing for primary attention are global search, tab pills, city switching, Near Me, the All/By Lens view toggle, the first AngleCard, and the sticky plan CTA for users without an active trip (`Travel App/app/(tabs)/discover/index.tsx:719-723`, `Travel App/app/(tabs)/discover/index.tsx:1001-1018`). This undercuts Vesper's doctrine to default to recommendations over option lists (`Travel App/docs/Design Language.md:17-20`).

### P1 - Events turns Discover into a filter-heavy database surface

The Events tab has an event search input, availability filters, type filters, and optional genre filters before users reach results (`Travel App/app/(tabs)/discover/index.tsx:1227-1347`). That is appropriate for a listings product, but Vesper's doctrine says to "default to recommendations, not option lists" (`Travel App/docs/Design Language.md:17-20`) and to "default to less" where possible (`Travel App/docs/Design Language.md:37-40`).

For dogfood, this is not broken, but it feels less premium and less native than a concierge app should. A user looking for "what should I do tonight?" is asked to operate a faceted search UI instead of being handed one or two opinionated moves.

### P1 - Me contradicts the brand by foregrounding profile completion

The profile block shows `Complete your profile` in the empty state and `Profile {profile.taste_completion}% complete` for incomplete profiles (`Travel App/app/(tabs)/me/index.tsx:151-163`, `Travel App/app/(tabs)/me/index.tsx:194-205`). The brand brief explicitly says Vesper is not gamified and calls out "complete your trip profile 80%" as an anti-pattern (`Travel App/docs/Brand Identity.md:48-55`).

This is a trust issue, not just copy. Me should make the user feel known and in control of memory, not scored by a setup checklist. It also competes with the better primary object on the screen: Travel DNA (`Travel App/app/(tabs)/me/index.tsx:215-218`, `Travel App/components/me/TravelDNACard.tsx:1-19`).

### P1 - Me mixes identity, inbox, archive, social, and settings in one linear wall

After the profile block, Me renders Travel DNA, a concierge insight CTA, pending votes, memory, trip highlights, people, social activity, saved venues, voice logs, and bottom settings links in one scroll (`Travel App/app/(tabs)/me/index.tsx:145-237`, `Travel App/app/(tabs)/me/index.tsx:239-523`). Pending votes are especially out of place: they are active trip work inside a profile tab (`Travel App/app/(tabs)/me/index.tsx:232-237`).

The competing primary modules are profile identity, Travel DNA, the insight card, pending votes, and memory. This turns Me into a home dashboard rather than the user's durable relationship with Vesper. It also blurs where the user should go for urgent work: Trips, Concierge, or Me.

### P2 - Several primary controls appear visually below native touch-target expectations

The doctrine makes `minTouchTarget 44pt` non-negotiable (`Travel App/docs/Design Language.md:153-154`). Material recommends 48x48dp touch targets and 8dp spacing for most platforms; WCAG 2.2 sets a lower 24x24 CSS-pixel floor. Discover has multiple compact controls in the first viewport and Events filter stack whose visual boxes are much smaller than 44pt: Near Me uses small text and `paddingVertical: spacing.xs` (`Travel App/app/(tabs)/discover/index.tsx:777-791`, `Travel App/app/(tabs)/discover/index.tsx:1633-1644`), the All/By Lens buttons use `paddingVertical: spacing.xs` (`Travel App/app/(tabs)/discover/index.tsx:897-919`, `Travel App/app/(tabs)/discover/index.tsx:1724-1728`), and filter pills use similarly compact padding (`Travel App/app/(tabs)/discover/index.tsx:1260-1345`, `Travel App/app/(tabs)/discover/index.tsx:238-258`).

This is secondary to the IA problem, but it worsens the same perception: the surface feels fiddly and tool-like instead of calm and native.

## Evidence

- Internal doctrine says Vesper is a place-aware concierge relationship, not a generic trip planner or group chat tool (`Travel App/docs/Design Language.md:7-9`).
- Internal doctrine says Vesper should be opinionated over options and default to recommendations (`Travel App/docs/Design Language.md:17-20`).
- Internal doctrine says the product should "default to less" and use minimal chrome in live travel moments (`Travel App/docs/Design Language.md:37-40`).
- Internal aesthetic guidance says the metaphor is "a leather travel journal, not a SaaS dashboard" with generous whitespace and quiet hierarchy (`Travel App/docs/Design Language.md:55-64`).
- Brand identity says Vesper is knowledgeable, restrained, warm, opinionated, and durable (`Travel App/docs/Brand Identity.md:39-46`), and explicitly not productivity-coded or gamified (`Travel App/docs/Brand Identity.md:48-55`).
- Apple HIG's current top-level principles include clear visual hierarchy and platform consistency: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/).
- Material accessibility recommends clear layouts with distinct calls to action, notes that every added element increases complexity, and recommends 48x48dp touch targets: [Material accessibility](https://m2.material.io/design/usability/accessibility.html).
- WCAG 2.2 SC 2.5.8 requires pointer targets of at least 24x24 CSS pixels unless an exception applies, and notes larger targets help many users: [WCAG 2.2 target size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum).
- Progressive disclosure guidance recommends showing essentials first and revealing complexity as users go deeper: [IBM progressive disclosure](https://www.ibm.com/docs/en/technical-content?topic=practices-progressive-disclosure).

## Suggested Fix Direction

For Discover, make the first viewport a place-led editorial surface:

- Lead with `Lisbon` and one opinionated module: "the thing worth noticing now" or one featured angle with 1-2 exemplar venues.
- Keep search as a compact affordance, not the first visual object.
- Reduce the first-order navigation to the primary mode plus one contextual mode, likely `Angles` and `Near me` or `For you`.
- Move `Friends`, `Trending`, and `Guides` below the fold as editorial/social shelves, or move Friends into Me/People.
- Move `Events` behind a "Tonight / dates" module or a deeper Events screen; avoid three filter rows at tab level.
- Move `SpeculativeQueryInput` below the first set of real angles or behind "Request an angle" so it feels like a power path, not the screen's thesis.
- Keep the trip-creation CTA contextual: after saving/opening an angle, in the angle detail, or as a single quiet prompt below the hero rather than a sticky bottom bar competing with browsing.

For Me, make the first viewport an identity-and-memory surface:

- Lead with the user, one Travel DNA reflection, and a single "What Vesper knows" action.
- Remove percentage-complete language from the top profile; if completion is needed, move it to Constraints/Privacy or render it as a quiet missing-memory prompt.
- Move `PendingVotesSection` out of Me and into Trips or Concierge pending prompts; at most show a small notification badge from Me.
- Group trip highlights, memory, saved venues, voice logs, and people under a lower "Library" section.
- Group privacy, account, delegation, angle review, and feedback under a lower "Settings & trust" section or route.
- Treat social activity as part of People, not as a top-level Me module.

## Verification Ideas

- Run a first-viewport screenshot review on iPhone SE, iPhone 15, and a large Dynamic Type setting. Pass condition: a reviewer can state each tab's primary job in five seconds.
- Instrument or manually dogfood first-week taps: if Discover opens mostly into search/events/filters, the tab is acting like a database; if it opens into angle detail or venue detail, the editorial job is landing.
- Add a checklist to design review: one primary module above the fold, one primary CTA, secondary modules behind disclosure or below the first content block.
- Use an accessibility overlay or RN inspector pass to confirm first-viewport controls meet at least 44pt on iOS and 48dp on Android where possible.
