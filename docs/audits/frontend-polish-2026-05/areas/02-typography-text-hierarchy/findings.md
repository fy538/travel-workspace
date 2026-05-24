# Summary

Typography is not broken, but the implementation is drifting away from Vesper's own doctrine in the highest-signal reading surfaces. The token file correctly defines a two-scale system: dense Inter UI text for action surfaces and Fraunces article text for content worth reading. The problem is local usage: private Vesper prose, curator takes, trip-home signals, CTAs, and metadata often fall back to raw sizes or compact caption/body styles.

No P0s found. The main dogfood risk is P1/P2 polish: Vesper can feel more like a generic utility app than a premium editorial concierge, and several fixed text treatments are likely to truncate or crowd under larger accessibility text.

# Findings

## P1 - Private Vesper prose still renders as compact chat UI

`MessageBubble` receives `isPrivate`, but AI text always uses the same purple bubble and Markdown body style. The renderer applies `styles.bubbleAI` and `markdownStyles.body`/`paragraph` based on `isAI`, not on private-vs-group context. That contradicts the product doctrine that private 1:1 Vesper should read like prose on parchment, not a bubble.

- `Travel App/components/chat/MessageBubble.tsx:84` renders the Vesper tag for AI messages, including private.
- `Travel App/components/chat/MessageBubble.tsx:99` wraps AI text in the same bubble container.
- `Travel App/components/chat/MessageBubble.tsx:263` applies the purple AI bubble treatment.
- `Travel App/components/chat/MessageBubble.tsx:352` uses `typography.body` for AI Markdown, not article-scale Fraunces.

Dogfood impact: the core concierge relationship feels less premium and less like Vesper's "writes on the page" signature experience.

## P2 - Editorial content is compressed into caption-scale UI text

Several content surfaces that should reward reading are styled as dense utility labels. This is most visible in Discover and trip-home cards, where curator takes and generated rationales become 12-13pt snippets rather than editorial content.

- `Travel App/components/trip-home/HomeCardBody.tsx:76` caps card titles at two lines and styles them as 14/18 Inter at `Travel App/components/trip-home/HomeCardBody.tsx:114`.
- `Travel App/components/trip-home/HomeCardBody.tsx:148` styles editorial subtitles as 12/16 Fraunces italic; `editorial-lg` is only 13/18 at `Travel App/components/trip-home/HomeCardBody.tsx:155`.
- `Travel App/components/trip-home/HappeningCard.tsx:29` routes `why_for_you`-style content through that compact `editorial` subtitle.
- `Travel App/components/trip-home/ConstraintMealCard.tsx:31` does the same for care/diplomacy copy.
- `Travel App/app/(tabs)/discover/index.tsx:1195` renders search-result curator headlines as `typography.caption`.
- `Travel App/app/(tabs)/discover/index.tsx:1689` renders Near Me curator takes as caption italic with local 17 line height.
- `Travel App/app/(tabs)/discover/index.tsx:1816` renders masonry hooks as caption copy.

Dogfood impact: content that should feel specific, trusted, and worth reading can read like metadata. This weakens the editorial travel-journal identity.

## P2 - Local font values are replacing semantic type roles

The token file asks callers to "use semantic roles, not raw values," but focused files contain many local type definitions. Some values reference token font sizes without adopting the full style object, which preserves the number while dropping font family, line height, color, or semantic meaning.

- `Travel App/components/chat/MessageBubble.tsx:305` through `Travel App/components/chat/MessageBubble.tsx:337` defines failed/sending/privacy/retry/timestamp text with raw 10-11pt sizes.
- `Travel App/components/chat/MessageBubble.tsx:374` and `Travel App/components/chat/MessageBubble.tsx:381` define Markdown headings as raw 16/15pt weights.
- `Travel App/components/chat/MessageBubble.tsx:400` uses raw `Courier` 13pt for inline code.
- `Travel App/components/trip/TripCard.tsx:261` defines a raw hero display style instead of reusing `typography.displayLarge`.
- `Travel App/components/trip/TripCard.tsx:337`, `Travel App/components/trip/TripCard.tsx:366`, and `Travel App/components/trip/TripCard.tsx:403` locally recreate metadata/caps roles.
- `Travel App/app/(tabs)/me/index.tsx:547`, `Travel App/app/(tabs)/me/index.tsx:549`, `Travel App/app/(tabs)/me/index.tsx:553`, `Travel App/app/(tabs)/me/index.tsx:560`, and `Travel App/app/(tabs)/me/index.tsx:576` define local action/archetype text.
- `Travel App/app/(tabs)/discover/index.tsx:172`, `Travel App/app/(tabs)/discover/index.tsx:252`, `Travel App/app/(tabs)/discover/index.tsx:1737`, and `Travel App/app/(tabs)/discover/index.tsx:1799` define local card/control text variants.

Dogfood impact: the app can look assembled from adjacent but not identical surfaces. Premium typography needs fewer local one-offs.

## P2 - Text is likely to truncate or crowd under larger accessibility text

The highest-risk layouts combine fixed card dimensions, fixed line heights, `numberOfLines`, and row layouts with non-shrinking CTA text. Apple HIG encourages Dynamic Type support, and WCAG 2.2 expects text to resize up to 200% without loss of content or functionality. These areas should be screenshot-tested at large accessibility sizes.

- `Travel App/components/trip/TripCard.tsx:105` caps compact trip titles to one line inside a row with a fixed 92pt photo.
- `Travel App/components/trip/TripCard.tsx:130` through `Travel App/components/trip/TripCard.tsx:145` places hero title/date text absolutely over the image; the style uses fixed 30/32 display type at `Travel App/components/trip/TripCard.tsx:261`.
- `Travel App/components/trip/TripCard.tsx:62` caps memory titles to two lines while using display-hero scale.
- `Travel App/components/trip-home/HomeCardBody.tsx:75` through `Travel App/components/trip-home/HomeCardBody.tsx:82` puts a capped title beside a non-shrinking CTA; the CTA has `flexShrink: 0` at `Travel App/components/trip-home/HomeCardBody.tsx:122`.
- `Travel App/components/trip-home/CardShell.tsx:133` sets the dismiss target to 32x32, below the app's own 44pt accessibility floor.
- `Travel App/app/(tabs)/discover/index.tsx:900` through `Travel App/app/(tabs)/discover/index.tsx:917` renders compact segmented controls with small vertical padding and 13pt local text.
- `Travel App/app/(tabs)/discover/index.tsx:1411`, `Travel App/app/(tabs)/discover/index.tsx:1494`, and `Travel App/app/(tabs)/discover/index.tsx:1812` put masonry text inside fixed-height image blocks without visible large-text strategy.
- `Travel App/app/(tabs)/me/index.tsx:409` caps saved venue names to one line in a fixed-width 160pt chip defined at `Travel App/app/(tabs)/me/index.tsx:616`.

Dogfood impact: first-week testers using larger text may see clipped destination names, cramped controls, or lost editorial hooks. Even for default-size users, aggressive truncation can make the product feel less trustworthy because the app appears to be hiding useful specifics.

## P3 - Compact control labels are inconsistent across surfaces

Controls use a mix of 10pt caps, 11pt lowercase CTA hints, 12pt captions, 13pt medium labels, 14pt body labels, and 15pt button labels. Some of this is legitimate hierarchy, but the lack of named roles makes it hard to tell intentional contrast from drift.

- `Travel App/components/trip-home/HomeCardBody.tsx:122` uses 11pt lowercase CTA text.
- `Travel App/components/trip-home/UndoToast.tsx:84` uses 11pt uppercase undo text.
- `Travel App/app/(tabs)/discover/index.tsx:1571` uses 14pt search cancel text.
- `Travel App/app/(tabs)/discover/index.tsx:1634` and `Travel App/app/(tabs)/discover/index.tsx:1649` define the Near Me pill with small padding and caps-small-derived text.
- `Travel App/app/(tabs)/discover/index.tsx:1724` and `Travel App/app/(tabs)/discover/index.tsx:1737` define the view-mode segmented control locally.
- `Travel App/app/(tabs)/discover/index.tsx:1790` and `Travel App/app/(tabs)/discover/index.tsx:1799` define the bottom CTA locally at 15pt.

Dogfood impact: controls are understandable, but the interface may feel less native and less deliberate because similar actions do not share a consistent typographic voice.

# Evidence

Internal doctrine:

- `Travel App/constants/typography.ts:8` through `Travel App/constants/typography.ts:15` documents the two-scale rule and asks callers to use semantic roles instead of raw values.
- `Travel App/constants/typography.ts:112` through `Travel App/constants/typography.ts:145` defines the article scale: 17/27 body and 17-20pt headings.
- `Travel App/constants/fonts.ts:37` through `Travel App/constants/fonts.ts:48` defines shared letter-spacing values, but callers still define local caps/metadata roles.
- `Travel App/docs/Design Language.md:120` through `Travel App/docs/Design Language.md:131` defines UI scale vs article scale and says reading surfaces should use article scale.
- `Travel App/docs/Design Language.md:153` through `Travel App/docs/Design Language.md:154` defines a 44pt touch-target floor.

External baseline:

- Apple HIG Typography: https://developer.apple.com/design/human-interface-guidelines/typography
- Apple HIG Accessibility recommends supporting font-size enlargement through Dynamic Type and gives iOS/iPadOS control-size guidance: https://developer.apple.com/design/human-interface-guidelines/accessibility
- Apple HIG Buttons says buttons generally need at least a 44x44pt hit region: https://developer.apple.com/design/human-interface-guidelines/buttons
- Android Developers' Material 3 overview describes a type scale grouped into display, headline, title, body, and label roles: https://developer.android.google.cn/develop/ui/compose/designsystems/material3?hl=en
- Material accessibility guidance recommends scalable text, space for large fonts, clear hierarchy, and 48x48dp touch targets on most platforms: https://m2.material.io/design/usability/accessibility.html
- WCAG 2.2 Resize Text requires text to resize up to 200% without loss of content/functionality: https://www.w3.org/TR/WCAG22/#resize-text
- WCAG 2.2 Target Size Minimum sets a 24x24 CSS px minimum pointer target with exceptions; this is a web floor, not the app's premium mobile target: https://www.w3.org/TR/WCAG22/#target-size-minimum

# Suggested Fix Direction

1. Add missing semantic typography tokens before touching screens: `metadata`, `timestamp`, `inlineError`, `actionLabel`, `compactControlLabel`, `sectionLabel`, `homeCardTitle`, `homeCardCta`, `homeCardSubtitle`, `editorialSnippet`, `photoMeta`, `markdownHeading`, and `inlineCode`.
2. Split Vesper message rendering by substrate: keep `MessageBubble` for group chat and user messages; add a private Vesper prose renderer that uses article-scale Fraunces on parchment with attribution outside the bubble.
3. Promote readable travel content out of caption scale: curator takes, `why_for_you`, brief signals, and search snippets should use at least a named editorial snippet style, with article scale for longer prose.
4. Make compact controls use named text roles and named minimum target behavior. `CardShell` dismiss, view toggles, retry buttons, guide prompts, and bottom CTAs should converge on shared `IconButton`, `SegmentedControl`, or `actionLabel` roles.
5. Replace hard line caps with responsive behavior where the content carries trust: destination names, Vesper/curator hooks, trip titles, and personal memory captions should wrap gracefully or expose the full text in the next tap surface.

# Verification Ideas

- Run a static check over focused files for raw `fontSize`, `fontFamily`, `fontWeight`, `lineHeight`, `letterSpacing`, and `numberOfLines`.
- Screenshot the focused screens at default, Large, and Accessibility Large text sizes on a narrow iPhone viewport.
- Add a small fixture set with long city names, long trip titles, long venue names, long CTA labels, and 3-4 line curator takes.
- In visual QA, specifically inspect: private Vesper chat, trip card compact/full/memory variants, trip-home attention cards, Discover search/Near Me/masonry, and Me saved venues/highlights.
- Validate touch target overlays for dismiss buttons, segmented controls, retry buttons, saved-venue chips, and CTA rows against the 44pt app target.
