# Summary

Vesper has the right color doctrine in place, but implementation drift is weakening it. The app's own design language says purple is reserved for AI/concierge presence, earth tones carry semantic state, raw hex should not be used outside tokens, and status should read typographically rather than as generic pills. The current code mostly follows the palette, but purple is also used for profile identity, selected expense chips, generic empty states, map/activity dots, "today/live" indicators, and several non-agent operational accents.

The dogfood risk is trust and signal clarity, not functional breakage. In the first week of internal use, users will learn that purple sometimes means "Vesper is speaking," sometimes "selected," sometimes "live," sometimes "activity," and sometimes "profile decoration." That makes the concierge presence feel less sacred and the app less premium.

External baseline: [Apple HIG Color](https://developer.apple.com/design/human-interface-guidelines/color) recommends consistent color use for status/interactivity; [Apple HIG Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) emphasizes perceivable interfaces and adequately sized controls; [Material accessibility guidance](https://m2.material.io/design/usability/accessibility.html) uses 4.5:1 contrast for small text and multiple cues for states; [WCAG 2.2](https://www.w3.org/TR/WCAG22/#target-size-minimum) sets a 24x24 CSS px pointer target minimum and 44x44 as enhanced target size.

# Findings

## P1 - Purple is no longer exclusive to Vesper/concierge presence

Purple is used as a generic accent for empty states, profile identity, selected form chips, expense categories, activity dots, map markers, and temporal state. This conflicts with the doctrine that "Seeing purple = the AI is doing something" and weakens the product's signature signal.

Examples:
- Generic `EmptyState` always renders a purple icon and purple-tinted icon well, regardless of whether the empty state is agent-related: `Travel App/components/ui/EmptyState.tsx:23`, `Travel App/components/ui/EmptyState.tsx:27`, `Travel App/components/ui/EmptyState.tsx:51`.
- The Me profile avatar and archetype use purple as profile decoration: `Travel App/app/(tabs)/me/index.tsx:148`, `Travel App/app/(tabs)/me/index.tsx:549`.
- Expense category selection uses purple for selected chip border, icon, and text even though selection is generic form state: `Travel App/components/expense/AddExpenseSheet.tsx:542`, `Travel App/components/expense/AddExpenseSheet.tsx:555`, `Travel App/components/expense/AddExpenseSheet.tsx:817`; same pattern in edit: `Travel App/components/expense/EditExpenseSheet.tsx:123`, `Travel App/components/expense/EditExpenseSheet.tsx:135`, `Travel App/components/expense/EditExpenseSheet.tsx:255`.
- Expense "activity" category is purple in rows/details, making an expense taxonomy look AI-coded: `Travel App/components/expense/ExpenseRow.tsx:28`, `Travel App/components/expense/ExpenseRow.tsx:31`.
- Plan and map activity dots use purple for non-experience blocks/stops: `Travel App/components/trip-plan/PlanBlockRow.tsx:158`, `Travel App/components/trip-map/mapStopDisplay.ts:27`, `Travel App/components/trip-map/tripMapStateAdapter.ts:321`.

## P1 - Semantic state colors contradict the documented status mapping

The design language maps `live` to olive and reserves purple for agent presence, but some implementation paths use purple for live/today/highlight state. This makes color state less predictable and chips/badges feel more like generic dashboard UI.

Examples:
- The canonical mapping says `live` should be olive and status should be typographic, not pill/badge/chip: `Travel App/docs/Design Language.md:110`, `Travel App/docs/Design Language.md:268`.
- `statusColors` correctly maps `live` to olive in the token file: `Travel App/constants/colors.ts:99`, `Travel App/constants/colors.ts:104`.
- `TripLogCard` overrides live status to purple: `Travel App/components/memory/TripLogCard.tsx:45`, `Travel App/components/memory/TripLogCard.tsx:47`.
- `PlanDaySection` maps `today` to purple and uses it as an outlined badge color: `Travel App/components/trip-plan/PlanDaySection.tsx:27`, `Travel App/components/trip-plan/PlanDaySection.tsx:38`, `Travel App/components/trip-plan/PlanDaySection.tsx:115`.
- The day deep-link highlight uses a purple border, which reads agent-coded rather than navigation focus/selection: `Travel App/components/trip-plan/PlanDaySection.tsx:222`, `Travel App/components/trip-plan/PlanDaySection.tsx:224`.
- `PlanCommitmentBadge` maps `proposed` to purple; this is defensible when explicitly Vesper-proposed, but the token is state-based rather than source-based: `Travel App/components/trip-plan/PlanCommitmentBadge.tsx:20`, `Travel App/components/trip-plan/PlanCommitmentBadge.tsx:22`.

## P2 - Low-contrast tertiary text is carrying real content

`colors.text.tertiary` is `#9C9A90`, which is about 2.82:1 on white, 2.56:1 on `#F5F4EF`, and 2.39:1 on `#EDECE6`. That is below Material/WCAG's 4.5:1 small-text guidance. It is acceptable for decorative separators, but it is currently used for timestamps, disabled labels, metadata, empty-state details, photo/privacy captions, and badge-like cues.

Examples:
- Token definition: `Travel App/constants/colors.ts:49`, `Travel App/constants/colors.ts:52`.
- Message timestamps are 10px tertiary text: `Travel App/components/chat/MessageBubble.tsx:336`, `Travel App/components/chat/MessageBubble.tsx:338`.
- Trip log dates and "No story yet" are tertiary text at 12px/11px: `Travel App/components/memory/TripLogCard.tsx:116`, `Travel App/components/memory/TripLogCard.tsx:118`, `Travel App/components/memory/TripLogCard.tsx:145`.
- Lazy research failed/ok badges use tertiary text on tertiary background, making an important verification cue visually weak: `Travel App/components/chat/LazyResearchBadge.tsx:52`, `Travel App/components/chat/LazyResearchBadge.tsx:61`, `Travel App/components/chat/LazyResearchBadge.tsx:63`.
- Discover snippets/loading/stat text use tertiary for readable content, not decoration: `Travel App/app/(tabs)/discover/index.tsx:1587`, `Travel App/app/(tabs)/discover/index.tsx:1661`, `Travel App/app/(tabs)/discover/index.tsx:1663`, `Travel App/app/(tabs)/discover/index.tsx:1818`.
- Disabled button state applies global 0.5 opacity; a primary disabled button blends to roughly 2.89:1 on the parchment canvas, which is low even if inactive controls have legal exceptions: `Travel App/components/ui/Button.tsx:62`, `Travel App/components/ui/Button.tsx:67`, `Travel App/components/ui/Button.tsx:108`.
- Muted privacy copy in the consent sheet uses tertiary for contract-level information: `Travel App/components/trip/GroupAndLearnConsentSheet.tsx:263`, `Travel App/components/trip/GroupAndLearnConsentSheet.tsx:272`.

## P2 - Raw color literals bypass semantic tokens

Most colors are tokenized, but raw hex/rgba still appears in product files, including duplicated sacred-purple backgrounds, image text colors, illustration palettes, dev/internal crash surfaces, and local fallback colors. Some are legitimate illustration/photo exceptions, but several should become named semantic tokens so they can be audited.

Examples:
- `PendingPromptCard` hard-codes the sacred-purple background `#F1EFFB` instead of using a shared agent surface token: `Travel App/components/plan/PendingPromptCard.tsx:64`, `Travel App/components/plan/PendingPromptCard.tsx:66`.
- `CardShell` duplicates the same `#F1EFFB` as `SACRED_BG`: `Travel App/components/trip-home/CardShell.tsx:49`, `Travel App/components/trip-home/CardShell.tsx:61`.
- Me highlights define a local palette with multiple raw hex values plus `colors.purple[200]`: `Travel App/app/(tabs)/me/index.tsx:38`.
- ErrorBoundary internal diagnostic UI uses raw red/black/blue grays: `Travel App/components/ErrorBoundary.tsx:127`, `Travel App/components/ErrorBoundary.tsx:128`, `Travel App/components/ErrorBoundary.tsx:129`, `Travel App/components/ErrorBoundary.tsx:130`, `Travel App/components/ErrorBoundary.tsx:131`.
- TripCard uses raw overlay text and hairline colors that look like reusable photo/editorial tokens: `Travel App/components/trip/TripCard.tsx:81`, `Travel App/components/trip/TripCard.tsx:265`, `Travel App/components/trip/TripCard.tsx:294`, `Travel App/components/trip/TripCard.tsx:396`.
- HonestIllustration uses many raw colors. This is probably an acceptable asset-level exception, but it should be explicitly allowlisted: `Travel App/components/brand/HonestIllustration.tsx:83`, `Travel App/components/brand/HonestIllustration.tsx:87`, `Travel App/components/brand/HonestIllustration.tsx:133`, `Travel App/components/brand/HonestIllustration.tsx:164`.
- `TextInputModal` keeps a raw terracotta fallback that should be unnecessary if tokens are guaranteed: `Travel App/components/ui/TextInputModal.tsx:265`, `Travel App/components/ui/TextInputModal.tsx:267`.

# Evidence

Internal doctrine anchors:
- Purple is sacred and reserved for AI/concierge surfaces: `Travel App/docs/Design Language.md:57`, `Travel App/docs/Design Language.md:61`, `Travel App/docs/Design Language.md:84`.
- Earth tones are semantic, including olive for success/live, terracotta for planning/warnings, slate for info/booked, and gold for curator/premium: `Travel App/docs/Design Language.md:90`.
- All colors should live in `constants/colors.ts` and use semantic roles, not raw hex: `Travel App/docs/Design Language.md:80`, `Travel App/docs/Design Language.md:82`.
- Status should be typographic and semantic, not generic pills/badges/chips: `Travel App/docs/Design Language.md:268`, `Travel App/docs/Design Language.md:274`.
- Fleuron purple is allowed when paired with Vesper attribution; structural dividers should use ink-soft: `Travel App/docs/Brand Identity.md:138`, `Travel App/docs/Brand Identity.md:145`.

Raw color scan highlights:
- Token source correctly centralizes the main palette: `Travel App/constants/colors.ts:10`.
- Raw color literals outside tokens were found in product files including `ErrorBoundary`, `PendingPromptCard`, `CardShell`, `TripCard`, `HonestIllustration`, `TextInputModal`, and `Me`.
- Some raw rgba calls are probably intentional overlays (`PhotoLightbox`, photo captions, modal veils), but there is no allowlist separating asset/photo exceptions from product UI exceptions.

Contrast spot checks:
- `text.tertiary` `#9C9A90` on white: about 2.82:1.
- `text.tertiary` `#9C9A90` on `background.secondary` `#F5F4EF`: about 2.56:1.
- `text.tertiary` `#9C9A90` on `screen.canvas` `#EDECE6`: about 2.39:1.
- `purple[400]` `#7F77DD` on white: about 3.76:1, fine for icons/large accents but not small text.
- `gold[400]` `#C4A055` on white: about 2.47:1, unsafe for small text if used directly.

# Suggested Fix Direction

Create stricter semantic color roles rather than adding more palette colors:
- `agent.surface`, `agent.surfaceStrong`, `agent.accent`, `agent.action`, `agent.attribution`.
- `state.live`, `state.planning`, `state.booked`, `state.completed`, `state.focus`, `state.selected`, `state.disabledText`.
- `metadata.default`, `metadata.subtle`, `metadata.onPhoto`, `timestamp.default`.
- `category.food`, `category.transport`, `category.activity`, `category.stay`, `category.shopping`, `category.other`, using earth tones only.
- `surface.photoText`, `surface.photoSubtext`, `surface.hairlineInk`, `surface.sacredWash`.

Then make purple usage source-aware:
- Keep purple for Vesper attribution, Vesper asks, private/agent conversation substrate, voice/concierge presence, and agent-generated pending work.
- Replace generic selection purple with espresso/action tokens.
- Replace `live`/`today` purple with olive or an ink focus treatment.
- Replace expense/activity/map purple with earth-tone category colors.
- Make generic `EmptyState` neutral by default and allow `tone="agent"` only at agent-owned call sites.

For contrast:
- Treat `text.tertiary` as decorative-only.
- Introduce a stronger `metadata.default` that passes 4.5:1 on parchment/white for timestamps and badges that carry meaning.
- Avoid global opacity for disabled buttons; use explicit disabled foreground/background tokens with readable labels where the reason matters.

For raw colors:
- Move `#F1EFFB`, photo overlay ink, hairline ink, diagnostic colors, and local highlight palettes into named tokens or approved asset palettes.
- Add a static check that fails raw hex/rgba in `app/**` and `components/**` except allowlisted asset/photo files.

# Verification Ideas

- Run a purple audit script that lists every `colors.purple`, `tone="purple"`, and purple raw literal call site, then classify each as `agent-presence`, `agent-memory`, `generic-selection`, `category`, `temporal-state`, `profile`, or `unknown`.
- Add contrast tests for every text token on `background.primary`, `background.secondary`, and `screen.canvas`, with a separate allowlist for decorative captions.
- Add visual review scenarios for the Me tab, expense sheets, plan day list, trip log, concierge list, and generic empty states with the question: "Does purple only mean Vesper is present?"
- Add a token-lint rule for raw colors in `Travel App/app/**` and `Travel App/components/**`, with explicit exceptions for SVG illustration palettes and photo/lightbox overlays.
- Snapshot or screenshot-check disabled buttons, timestamps, badges, and tertiary metadata in light mode and Increased Contrast mode.
