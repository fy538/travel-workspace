# Spacing, Rhythm, Alignment Audit

## Summary

The spacing system has a strong doctrine but inconsistent enforcement. `constants/layout.ts` explicitly says every magic number in a StyleSheet should trace back to layout tokens, and the design docs call for generous whitespace, 8pt-ish rhythm, aligned relationships, and a 44pt touch floor. In the audited app surfaces, the biggest polish risk is not one broken layout; it is that high-traffic screens still compose local offsets, small controls, fixed chrome, and section spacing one screen at a time.

No P0 issues found. The highest dogfood risk is P1: spacing primitives do not consistently protect native-feeling touch rhythm, especially in pill/tab/filter rows and header icon controls.

## Findings

### P1 - Interactive spacing primitives do not enforce the documented 44pt floor

`Tap` is documented as the app-wide pressable wrapper, but it only forwards styles to `Pressable`; it does not apply `minHeight`, `minWidth`, `hitSlop`, or a target-size mode. Several controls therefore depend on caller padding and fall below Vesper's own 44pt doctrine: trip segmented cells are `minHeight: 36`, default nav pills have only vertical padding, Discover filter pills use `spacing.xs` vertical padding, and compact header actions rely on small visual padding or hit slop rather than a shared icon-button primitive.

Why it matters: dogfood users will hit these controls constantly in week one. Small, differently padded controls feel less native and less premium even when they technically work.

### P2 - Discover's first viewport is crowded and offset with one-off spacing

Discover defines six top-level pills, renders them directly under a fixed search header, then pushes scroll content down with `headerHeight + 8` in three branches. That puts search, six category controls, fade chrome, and the first content header into the same first-viewport stack. The local `+ 8` offset also bypasses the named spacing scale.

Why it matters: Discover should feel like an editorial index. The current header behaves more like a dense dashboard filter bar, weakening the "quiet hierarchy" and "place-aware" first impression.

### P2 - Trip workspace chrome compresses the Plan landing before content can breathe

`TripHeader` stacks safe-area chrome, a back button, trip switcher, avatar stack, settings icon, and phase-adaptive pills. The Plan landing itself notes that the header pills are redundant with the surface grid and should be stripped later. In practice, this means the first viewport spends too much vertical rhythm on navigation before the concierge attention and day content begin.

Why it matters: the trip workspace is a core dogfood surface. The app should feel like entering a trip, not a project workspace with nested navigation chrome.

### P2 - Plan timeline alignment relies on a fragile hard-coded keyline

The legacy Plan timeline aligns "Suggest a change" with the block content using `paddingLeft: 56`, manually matching `timeCol` width, `dotCol` width, and margin. If any of those values change for Dynamic Type, localization, or density tuning, the secondary action drifts off the timeline keyline.

Why it matters: visible keyline drift is one of the fastest ways for an itinerary to feel assembled rather than designed. This should be a timeline primitive, not arithmetic embedded in one row.

### P2 - Me tab has inconsistent section rhythm and alignment modes

The Me tab alternates a centered profile block, a full card, a bare insight module with only vertical padding, tappable section headers, horizontal scrollers, inline placeholders, plain cards, and bottom links. Individual modules are reasonable, but adjacent spacing is governed by local styles (`marginVertical`, `marginBottom`, `paddingVertical`, `marginTop`) rather than a shared `ProfileStack` or `SectionStack` rhythm.

Why it matters: Me is where trust and memory are inspected. Mixed alignment modes and uneven vertical cadence make the product feel more accumulated than authored.

### P3 - Local spacing bypasses tokens in enough places to justify new primitives

The most visible examples are not many pixels off, but they are repeated: Discover uses `headerHeight + 8` and inline `{ gap: 12 }`; Concierge chat uses raw `gap: 8` and `borderRadius: 12`; Trip Plan uses `paddingLeft: 56`; the Trips welcome card uses `marginTop: 1`; and `TripCard`-style editorial layouts use several raw 14/18/24 offsets outside the core token vocabulary. Some are legitimate optical adjustments, but the current system has no way to distinguish sanctioned optical spacing from drift.

Why it matters: Vesper's premium feel depends on consistent rhythm. If every screen solves "just 8 more points here" locally, polish will decay as features land.

## Evidence

Internal doctrine:

- `Travel App/constants/layout.ts:4` says every magic number in a StyleSheet should trace back to layout tokens; `Travel App/constants/layout.ts:9` defines the spacing scale; `Travel App/constants/layout.ts:57` defines the accessibility touch target; `Travel App/constants/layout.ts:108` defines standardized card/section/inline gaps.
- `Travel App/docs/Design Language.md:57` sets the "leather travel journal, not a SaaS dashboard" metaphor; `Travel App/docs/Design Language.md:62` calls for generous whitespace; `Travel App/docs/Design Language.md:139` defines the 8pt-ish spacing scale; `Travel App/docs/Design Language.md:153` sets the 44pt touch target floor.
- `Travel App/docs/Components.md:27` says UI primitives should be used before RN primitives; `Travel App/docs/Components.md:31` describes `Tap` as having a consistent hit area.

Implementation evidence:

- `Travel App/components/ui/Tap.tsx:55` returns a plain `Pressable` with caller styles and pressed opacity only.
- `Travel App/components/ui/NavPills.tsx:142` sets default pill-row padding; `Travel App/components/ui/NavPills.tsx:158` defines default pills without a minimum target; `Travel App/components/ui/NavPills.tsx:202` sets trip segmented cells to `minHeight: 36`; `Travel App/components/ui/ScreenHeader.tsx:130` defines icon buttons with padding but no shared min-target primitive.
- `Travel App/app/(tabs)/discover/index.tsx:56` defines six top-level pills; `Travel App/app/(tabs)/discover/index.tsx:675` renders the fixed header; `Travel App/app/(tabs)/discover/index.tsx:698` renders `NavPills`; `Travel App/app/(tabs)/discover/index.tsx:750`, `Travel App/app/(tabs)/discover/index.tsx:1058`, and `Travel App/app/(tabs)/discover/index.tsx:1117` use `headerHeight + 8`; `Travel App/app/(tabs)/discover/index.tsx:1450` uses inline `{ gap: 12 }`.
- `Travel App/app/(tabs)/discover/index.tsx:238` through `Travel App/app/(tabs)/discover/index.tsx:241` define compact filter pills with `spacing.xs` vertical padding; `Travel App/app/(tabs)/discover/index.tsx:1634` through `Travel App/app/(tabs)/discover/index.tsx:1640` do the same for Near Me.
- `Travel App/components/trip/TripHeader.tsx:97` renders the header stack; `Travel App/components/trip/TripHeader.tsx:100` and `Travel App/components/trip/TripHeader.tsx:125` render compact icon controls; `Travel App/components/trip/TripHeader.tsx:135` renders workspace pills; `Travel App/components/trip/TripHeader.tsx:157` sets header row padding.
- `Travel App/app/(tabs)/trips/[tripId]/index.tsx:14` through `Travel App/app/(tabs)/trips/[tripId]/index.tsx:19` documents that Plan should eventually remove redundant header chrome; `Travel App/app/(tabs)/trips/[tripId]/index.tsx:543` defines Plan landing content padding and `Travel App/app/(tabs)/trips/[tripId]/index.tsx:548` defines section spacing.
- `Travel App/app/(tabs)/trips/[tripId]/plan.tsx:485` sets the timeline time column, `Travel App/app/(tabs)/trips/[tripId]/plan.tsx:493` sets the dot column, and `Travel App/app/(tabs)/trips/[tripId]/plan.tsx:534` through `Travel App/app/(tabs)/trips/[tripId]/plan.tsx:540` hard-code the secondary action offset.
- `Travel App/app/(tabs)/me/index.tsx:145` starts the Me scroll stack; `Travel App/app/(tabs)/me/index.tsx:147` renders the centered profile card; `Travel App/app/(tabs)/me/index.tsx:215` renders the Travel DNA card; `Travel App/app/(tabs)/me/index.tsx:221` renders a bare insight module; `Travel App/app/(tabs)/me/index.tsx:240`, `Travel App/app/(tabs)/me/index.tsx:289`, and `Travel App/app/(tabs)/me/index.tsx:372` repeat section headers; `Travel App/app/(tabs)/me/index.tsx:540` through `Travel App/app/(tabs)/me/index.tsx:562` define the mixed local rhythm.
- `Travel App/app/(tabs)/trips/index.tsx:500` uses `marginTop: 1`; `Travel App/components/trip/TripCard.tsx:254` through `Travel App/components/trip/TripCard.tsx:290` use several raw editorial offsets; `Travel App/components/trip/TripCard.tsx:319` through `Travel App/components/trip/TripCard.tsx:323` do the same in compact cards.
- `Travel App/app/(tabs)/concierge/chat.tsx:970` uses raw `gap: 8`; `Travel App/app/(tabs)/concierge/chat.tsx:1019` uses raw `borderRadius: 12`.

External guidance baseline:

- [Apple HIG Layout](https://developer.apple.com/design/human-interface-guidelines/layout) emphasizes safe areas, margins, and familiar relationships between controls and content.
- [Material Design layout principles](https://m2.material.io/design/layout/understanding-layout.html) emphasize predictable layout regions, visual grouping, consistent padding/keylines, adaptive layout, and 8dp measurement rhythm.
- [WCAG 2.2 Target Size Minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum) sets a 24 by 24 CSS pixel minimum or sufficient spacing around pointer targets; Vesper's own mobile standard is stricter at 44pt.

## Suggested Fix Direction

- Promote `Tap` into a true spacing primitive: add `minTarget="default|compact|none"` or create `IconButton`, `PillButton`, and `SegmentedControl` wrappers that apply `a11y.minTouchTarget` by default.
- Add semantic layout tokens for recurring product rhythms: `chromeGap`, `headerContentOffset`, `sectionStackGap`, `timelineKeyline`, `horizontalScrollerGap`, and `emptyStateInset`.
- Replace Discover's six equal-width top pills with either a horizontally scrollable category rail or a two-level model: primary mode selector plus secondary filters inside the active mode.
- Collapse Trip workspace chrome on Plan landing: make Plan the default surface, keep Chat/Map/Photos as lower-density actions, and avoid repeating destinations already present in the Plan content grid.
- Build a `SectionStack` / `ProfileSection` primitive for Me so centered identity, cards, list sections, and bottom links share predictable spacing and aligned text edges.
- Convert the Plan timeline's `56` keyline into a named token or a `TimelineRow` layout component so secondary actions inherit the same content column.

## Verification Ideas

- Add a static check for raw spacing/layout numbers in audited directories, allowing explicit exceptions only with a comment such as `// optical`.
- Add a React Native visual debug mode that outlines touch targets and section gutters over the app.
- Capture screenshots at iPhone SE, iPhone 15, and a large Dynamic Type setting for Discover, Trips list, Trip Plan landing, Plan timeline, Me, and Concierge chat.
- In screenshot review, verify: all recurring gutters align to the same left edge, top chrome does not crowd first content, segmented controls meet the 44pt app standard, and section gaps are visibly larger than intra-card gaps.
