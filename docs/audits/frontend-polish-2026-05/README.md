# Frontend Polish Audit - May 2026

Status: initial research memo  
Scope: `Travel App` frontend design implementation, engineering architecture, and dogfood polish readiness  
Created: 2026-05-24

## Executive Summary

The frontend has a stronger design vision than its current implementation expresses.

The canonical docs describe Vesper as a warm, editorial, place-aware travel companion: "a leather travel journal, not a SaaS dashboard." The codebase contains good brand primitives that can support this vision, including `LetterpressCard`, `VesperNote`, `Fleuron`, `HonestIllustration`, and `Status`. But many high-traffic screens still rely on generic white cards, locally authored styles, oversized screen files, chat-bubble conventions, and dashboard-like modules.

The result is not a broken app. It is a product with a clear soul that is still being obscured by ordinary mobile UI defaults.

For dogfooding, the highest-leverage polish work is not a broad redesign. It is an alignment pass across the most-used surfaces:

1. Make private Vesper chat feel like the product's signature experience.
2. Reduce trip workspace chrome and visual noise.
3. Consolidate cards, spacing, typography, and touch targets behind stricter primitives.
4. Replace repeated placeholder imagery with destination-aware visual treatment.
5. Add a screenshot-based visual QA workflow so polish regressions become observable.

## Sources Reviewed

Internal docs and implementation:

- `Travel App/docs/Design Language.md`
- `Travel App/docs/Brand Identity.md`
- `Travel App/docs/Components.md`
- `Travel App/docs/Design Workflow.md`
- `Travel App/docs/Review Rubric.md`
- `Travel App/docs/design-decisions/agent-chat.md`
- `Travel App/docs/design-decisions/trip-card.md`
- `Travel App/docs/page-specs/*`
- `Travel App/constants/colors.ts`
- `Travel App/constants/layout.ts`
- `Travel App/constants/typography.ts`
- `Travel App/components/ui/*`
- `Travel App/components/brand/*`
- High-traffic screens under `Travel App/app/(tabs)/*`

External benchmark references:

- [Apple Human Interface Guidelines - Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
- [Apple Human Interface Guidelines - Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)
- [Apple Human Interface Guidelines - Typography](https://developer.apple.com/design/human-interface-guidelines/typography)
- [Material Design - Accessibility](https://m2.material.io/design/usability/accessibility.html)
- [WCAG 2.2 Target Size Minimum](https://www.w3.org/TR/WCAG22/#target-size-minimum)

Note: I attempted to boot the Expo web app for screenshots with mock API and skipped auth, but web support is not currently installed. Expo reported that `react-native-web` is missing. This memo is therefore based on code and docs, not rendered screenshot QA.

## What Is Working

### 1. The product design doctrine is unusually strong

`Travel App/docs/Design Language.md` gives the frontend a real north star:

- The product is a concierge relationship, not a trip planner or group chat tool.
- Purple is reserved for AI/concierge presence.
- The app should feel like a leather travel journal, not a SaaS dashboard.
- Long-form reading should use article scale; utility surfaces should use dense UI scale.
- Minimum touch target is documented as 44pt.

This is exactly the kind of doctrine a polish effort needs. The issue is execution drift, not lack of taste.

Relevant anchors:

- `Travel App/docs/Design Language.md:57` defines the leather travel journal metaphor.
- `Travel App/docs/Design Language.md:61` reserves purple for AI/concierge.
- `Travel App/docs/Design Language.md:120` through `Travel App/docs/Design Language.md:131` defines UI vs article typography.
- `Travel App/docs/Design Language.md:153` through `Travel App/docs/Design Language.md:154` defines the 44pt touch target floor.

### 2. Good brand primitives already exist

The app is not missing all the right abstractions. It already has:

- `LetterpressCard`
- `VesperNote`
- `Fleuron`
- `HonestIllustration`
- `Status`
- `Tap`
- `Button`
- `ScreenHeader`
- `NavPills`
- `TripCard`

This means a polish pass can be incremental. We do not need to invent a new design system from scratch; we need to make the existing one harder to bypass.

### 3. Trip cards show the right direction

`TripCard` is one of the clearest examples of the intended product feel. It uses the locked trip-card design direction, letterpress treatment, typographic status, and honest illustration fallback.

Relevant anchors:

- `Travel App/components/trip/TripCard.tsx:4` through `Travel App/components/trip/TripCard.tsx:7` documents the locked design direction.
- `Travel App/components/trip/TripCard.tsx:54` and `Travel App/components/trip/TripCard.tsx:128` use `LetterpressCard`.
- `Travel App/components/trip/TripCard.tsx:151` uses typographic status rather than a generic pill.

The problem is that other surfaces do not consistently inherit this same level of taste.

## Main Findings

### Finding 1 - Generic cards are still winning too often

The app's default `Card` primitive is a plain white rounded rectangle with a hairline border:

- `Travel App/components/ui/Card.tsx:15` through `Travel App/components/ui/Card.tsx:21`

That is a reasonable utility primitive, but it does not express the product's leather-journal metaphor. Since many screen-level modules use white cards and local styling, the experience can feel closer to a normal mobile dashboard than an editorial travel companion.

Recommended direction:

- Split cards into explicit roles: `EditorialCard`, `UtilityCard`, `ActionCard`, and possibly `AgentCard`.
- Make product surfaces default to editorial/letterpress treatment.
- Keep plain white cards for forms, settings, and dense utility views only.
- Add lint or review rules against new local white-card styles outside approved primitives.

### Finding 2 - Private Vesper chat contradicts the app's own anti-pattern

The design docs say private 1:1 Vesper should not feel like a generic chat bubble. But `MessageBubble` still renders AI messages as purple bubbles, including the private case:

- `Travel App/components/chat/MessageBubble.tsx:84` through `Travel App/components/chat/MessageBubble.tsx:92`
- `Travel App/components/chat/MessageBubble.tsx:99` through `Travel App/components/chat/MessageBubble.tsx:127`
- `Travel App/components/chat/MessageBubble.tsx:263` through `Travel App/components/chat/MessageBubble.tsx:266`

This is probably the single biggest perceived-polish issue because the concierge is the core product relationship. A private Vesper reply should feel more like a composed note, field dispatch, or envelope on parchment than a team-chat bubble.

Recommended direction:

- Create a distinct private-message renderer, for example `PrivateVesperMessage`.
- Use article typography for substantial Vesper prose.
- Preserve bubbles for group chat, user messages, and compact operational updates.
- Treat attachments and recommendation blocks as composed editorial modules, not decorations under a bubble.

### Finding 3 - Large screen files are allowing visual decisions to spread locally

Several high-traffic files are very large:

- `Travel App/app/(tabs)/discover/index.tsx` - 1824 lines
- `Travel App/app/(tabs)/concierge/chat.tsx` - 1042 lines
- `Travel App/components/trip/ProposalReviewSheet.tsx` - 1049 lines
- `Travel App/components/expense/AddExpenseSheet.tsx` - 885 lines
- `Travel App/app/(tabs)/me/index.tsx` - 632 lines

Large files are not automatically bad, but in frontend polish work they usually correlate with local layout/style decisions, hard-coded spacing, and unclear visual hierarchy.

Recommended direction:

- Refactor large screens into screen shell + named sections + focused hooks.
- Move repeated style patterns into primitives.
- Add a "no new 800+ line screen file" review norm unless explicitly justified.

### Finding 4 - Token usage is not strict enough

The design system has tokens for colors, layout, spacing, typography, and radii, but local styles still dominate. A static scan found:

- 206 `StyleSheet.create` occurrences across 191 files
- 96 inline object style usages across 41 files
- 439 raw `fontSize` numbers across 149 files
- 96 raw `borderRadius` numbers across 68 files
- 48 raw hex color usages across 10 files

Some exceptions are legitimate, especially illustrations and one-off rendering details. But the volume suggests visual polish is being decided too far away from the design system.

Recommended direction:

- Add lint rules or a custom static check for raw `fontSize`, `borderRadius`, and hex colors outside approved token files.
- Allow exceptions with named comments or local allowlists for illustrations.
- Add semantic type aliases such as `typography.actionLabel`, `typography.metadata`, `typography.timestamp`, and `typography.editorialBody`.

### Finding 5 - The trip workspace has too much layered chrome

The trip workspace header stacks:

- global bottom tabs
- sticky trip header
- back/settings controls
- trip title switcher
- avatar stack
- phase-adaptive horizontal pills

Relevant anchors:

- `Travel App/components/trip/TripHeader.tsx:1` through `Travel App/components/trip/TripHeader.tsx:12`
- `Travel App/components/trip/TripHeader.tsx:97` through `Travel App/components/trip/TripHeader.tsx:147`

The individual pieces are reasonable, but together they risk making the main trip area feel like a project-management tool. For dogfooding, the trip workspace should feel calmer and more inevitable.

Recommended direction:

- Audit the first viewport of trip home on small iPhones.
- Decide which controls must be persistent and which can collapse.
- Consider making `Plan` the dominant workspace and moving secondary modes into contextual actions.
- Reduce repeated navigation language when the user is already inside a trip.

### Finding 6 - Touch target compliance needs to be enforced mechanically

`Tap` is a good abstraction, but not every caller gives it a large enough hit area. For example, `TripHeader` icon controls use small icons with margin but no explicit hit slop or minimum target:

- `Travel App/components/trip/TripHeader.tsx:100` through `Travel App/components/trip/TripHeader.tsx:107`
- `Travel App/components/trip/TripHeader.tsx:125` through `Travel App/components/trip/TripHeader.tsx:132`
- `Travel App/components/trip/TripHeader.tsx:163` through `Travel App/components/trip/TripHeader.tsx:165`

Apple's HIG lists 44x44 pt as the minimum interactive target for iOS/iPadOS, and also emphasizes spacing between controls. WCAG 2.2 defines a lower web minimum of 24x24 CSS px with exceptions, but this is an accessibility floor, not a premium mobile target.

Recommended direction:

- Give `Tap` a `minTarget` mode or default minimum target behavior.
- Create `IconButton` as the only approved bare-icon control.
- Add a visual debug mode that overlays touch target bounds.
- Add accessibility labels and states to every interactive icon.

### Finding 7 - The image strategy is not strong enough for dogfooding

The repo has only app-level image assets such as icons and splash images. Trip cards use `HonestIllustration` with the same `lisbon-dusk` variant in both compact and full postcard states:

- `Travel App/components/trip/TripCard.tsx:101`
- `Travel App/components/trip/TripCard.tsx:131`

The illustration is brand-aligned, but repeated default imagery makes the app feel mock-like. Travel products need visual specificity: real place, actual state, concrete moment.

Recommended direction:

- Add destination-aware illustration variants or curated fallback photography.
- Make trip imagery deterministic per destination/status.
- Add a "no repeated hero image across adjacent trip cards" rule.
- For dogfood, prioritize imagery for the first seeded/live trips rather than all possible destinations.

### Finding 8 - Discover and Me read like accumulation surfaces

`Discover` and `Me` appear to have grown by accretion:

- `Discover` includes angles, friends, for-you, events, trending, guides, search, nearby context, and plan actions.
- `Me` includes profile, Travel DNA, insights, pending votes, memory, trips, social activity, saved venues, voice, and account links.

These ideas may all be useful, but polished apps usually make one primary job obvious per screen. The current structure risks making both tabs feel like dashboards.

Recommended direction:

- Define the one-sentence job of each tab.
- Restrict the first viewport to that job.
- Move secondary modules below the fold or behind progressive disclosure.
- Establish a module hierarchy: hero, primary loop, secondary utility, archival links.

### Finding 9 - Purple usage should be re-audited

The doctrine says purple is sacred and reserved for AI/concierge. Some surfaces use purple-adjacent treatment outside obvious agent presence. This may be defensible in specific cases, but the product should actively protect purple's meaning.

Recommended direction:

- Run a purple usage audit.
- Categorize every use as agent-presence, memory-of-agent, decorative, profile, status, or unknown.
- Replace decorative/profile purple with earth-tone alternatives unless it directly signals Vesper.

### Finding 10 - Visual QA is missing as a repeatable engineering gate

The app has strong type/test posture, but visual polish cannot be protected by typecheck alone. Since web support is currently unavailable, there is no cheap screenshot loop from this workspace.

Recommended direction:

- Either install and support Expo web for internal visual QA, or create an iOS simulator screenshot harness.
- Capture at least these dogfood screens:
  - Trips list
  - Trip home
  - Private Vesper chat
  - Group trip chat
  - Plan timeline
  - Discover
  - Me
- Review across small iPhone, large iPhone, and dynamic type/accessibility text settings.

## Suggested Dogfood Polish Priorities

### P0 - Core identity polish

1. Replace private Vesper bubbles with a signature editorial note renderer.
2. Standardize card roles and move high-traffic modules away from generic white cards.
3. Add minimum target enforcement through `Tap` and `IconButton`.

### P1 - Main journey polish

4. Simplify trip workspace chrome and first viewport hierarchy.
5. Make trip imagery destination-aware.
6. Refactor `Discover`, `ConciergeChat`, `ProposalReviewSheet`, `AddExpenseSheet`, and `Me` into smaller sections.

### P2 - Regression prevention

7. Add static checks for raw colors, font sizes, and radii.
8. Add screenshot QA on web or simulator.
9. Add a frontend polish review checklist to PR review.

## Parallel Research Prompt Pack

Use these prompts in separate agents. Each prompt is self-contained and includes its own output path, so it can be copied directly into a fresh agent.

Output folders:

- `docs/audits/frontend-polish-2026-05/areas/01-spacing-rhythm-alignment/findings.md`
- `docs/audits/frontend-polish-2026-05/areas/02-typography-text-hierarchy/findings.md`
- `docs/audits/frontend-polish-2026-05/areas/03-touch-targets-accessibility-native-feel/findings.md`
- `docs/audits/frontend-polish-2026-05/areas/04-private-vesper-chat-polish/findings.md`
- `docs/audits/frontend-polish-2026-05/areas/05-trip-workspace-plan-hierarchy/findings.md`
- `docs/audits/frontend-polish-2026-05/areas/06-card-system-surface-taxonomy/findings.md`
- `docs/audits/frontend-polish-2026-05/areas/07-discover-me-information-architecture/findings.md`
- `docs/audits/frontend-polish-2026-05/areas/08-imagery-empty-states-placeholder-honesty/findings.md`
- `docs/audits/frontend-polish-2026-05/areas/09-color-purple-discipline-semantic-state/findings.md`
- `docs/audits/frontend-polish-2026-05/areas/10-visual-qa-regression-gates/findings.md`
- Synthesis output: `docs/audits/frontend-polish-2026-05/MASTER-PUNCH-LIST.md`

### Prompt 1 - Spacing, Rhythm, And Alignment

```text
You are a frontend polish researcher auditing the Travel App inside Travel Workspace.

Workspace root:
/Users/feihuyan/Documents/Claude/Travel Workspace

Primary repo:
/Users/feihuyan/Documents/Claude/Travel Workspace/Travel App

Read first:
- AGENTS.md
- Travel App/CLAUDE.md
- Travel App/docs/Design Language.md
- Travel App/docs/Brand Identity.md
- Travel App/docs/Components.md
- Travel App/docs/Design Workflow.md
- Travel App/docs/Review Rubric.md
- docs/audits/frontend-polish-2026-05/README.md

Rules:
- Audit only. Do not edit product code.
- You may create or update only this report file:
  docs/audits/frontend-polish-2026-05/areas/01-spacing-rhythm-alignment/findings.md
- Prefer rg over grep.
- Do not read .env files or secrets.
- Use file and line references for every concrete finding.
- Compare the implementation against Vesper's own design doctrine and against current platform guidance such as Apple HIG, Material accessibility guidance, and WCAG 2.2 target-size guidance.
- Where you cite external guidance, link the source.
- Focus on dogfood polish: what would make the app feel less trustworthy, less premium, less native, or harder to use in the first week of internal use?
- Do not inflate severity. P0 means a concrete dogfood-blocking or core-identity-blocking issue.

Output:
- Write a concise markdown report to:
  docs/audits/frontend-polish-2026-05/areas/01-spacing-rhythm-alignment/findings.md
- Use sections: Summary, Findings, Evidence, Suggested Fix Direction, Verification Ideas.

Audit spacing, rhythm, alignment, and layout consistency across the Travel App.

Focus files:
- Travel App/constants/layout.ts
- Travel App/components/ui/*
- Travel App/components/brand/*
- Travel App/app/(tabs)/trips/**
- Travel App/app/(tabs)/discover/index.tsx
- Travel App/app/(tabs)/me/index.tsx
- Travel App/app/(tabs)/concierge/chat.tsx

Research baseline:
- Apple HIG layout: safe areas, margins, readable content width, familiar relationships between controls and content.
- Material layout principles: consistent spacing, adaptive layout, clear grouping.
- Common premium mobile practice: 8pt rhythm, consistent section spacing, aligned text edges, predictable gutters, clear first viewport hierarchy.

Questions:
1. Where do local spacing values bypass tokens?
2. Where do adjacent modules have inconsistent vertical rhythm?
3. Where are text edges, cards, headers, and controls visually misaligned?
4. Which first-viewport layouts feel crowded or under-composed?
5. Which spacing fixes should become primitives/tokens rather than one-off edits?
```

### Prompt 2 - Typography And Text Hierarchy

```text
You are a frontend polish researcher auditing the Travel App inside Travel Workspace.

Workspace root:
/Users/feihuyan/Documents/Claude/Travel Workspace

Primary repo:
/Users/feihuyan/Documents/Claude/Travel Workspace/Travel App

Read first:
- AGENTS.md
- Travel App/CLAUDE.md
- Travel App/docs/Design Language.md
- Travel App/docs/Brand Identity.md
- Travel App/docs/Components.md
- Travel App/docs/Design Workflow.md
- Travel App/docs/Review Rubric.md
- docs/audits/frontend-polish-2026-05/README.md

Rules:
- Audit only. Do not edit product code.
- You may create or update only this report file:
  docs/audits/frontend-polish-2026-05/areas/02-typography-text-hierarchy/findings.md
- Prefer rg over grep.
- Do not read .env files or secrets.
- Use file and line references for every concrete finding.
- Compare the implementation against Vesper's own design doctrine and against current platform guidance such as Apple HIG, Material accessibility guidance, and WCAG 2.2 target-size guidance.
- Where you cite external guidance, link the source.
- Focus on dogfood polish: what would make the app feel less trustworthy, less premium, less native, or harder to use in the first week of internal use?
- Do not inflate severity. P0 means a concrete dogfood-blocking or core-identity-blocking issue.

Output:
- Write a concise markdown report to:
  docs/audits/frontend-polish-2026-05/areas/02-typography-text-hierarchy/findings.md
- Use sections: Summary, Findings, Evidence, Suggested Fix Direction, Verification Ideas.

Audit typography and text hierarchy.

Focus files:
- Travel App/constants/typography.ts
- Travel App/constants/fonts.ts
- Travel App/components/chat/MessageBubble.tsx
- Travel App/components/trip/TripCard.tsx
- Travel App/components/trip-home/*
- Travel App/app/(tabs)/discover/index.tsx
- Travel App/app/(tabs)/me/index.tsx

Research baseline:
- Apple HIG typography and Dynamic Type.
- Material type scale and readable hierarchy.
- Editorial app practice: clear distinction between content worth reading and UI labels for action.

Questions:
1. Where are raw font sizes used instead of typography tokens?
2. Where does copy that should feel editorial use dense UI styling?
3. Where do compact controls use oversized or inconsistent type?
4. Where might text truncate, overlap, or fail under larger accessibility text?
5. What missing typography tokens would reduce local style drift?
```

### Prompt 3 - Touch Targets, Accessibility, And Native Feel

```text
You are a frontend polish researcher auditing the Travel App inside Travel Workspace.

Workspace root:
/Users/feihuyan/Documents/Claude/Travel Workspace

Primary repo:
/Users/feihuyan/Documents/Claude/Travel Workspace/Travel App

Read first:
- AGENTS.md
- Travel App/CLAUDE.md
- Travel App/docs/Design Language.md
- Travel App/docs/Brand Identity.md
- Travel App/docs/Components.md
- Travel App/docs/Design Workflow.md
- Travel App/docs/Review Rubric.md
- docs/audits/frontend-polish-2026-05/README.md

Rules:
- Audit only. Do not edit product code.
- You may create or update only this report file:
  docs/audits/frontend-polish-2026-05/areas/03-touch-targets-accessibility-native-feel/findings.md
- Prefer rg over grep.
- Do not read .env files or secrets.
- Use file and line references for every concrete finding.
- Compare the implementation against Vesper's own design doctrine and against current platform guidance such as Apple HIG, Material accessibility guidance, and WCAG 2.2 target-size guidance.
- Where you cite external guidance, link the source.
- Focus on dogfood polish: what would make the app feel less trustworthy, less premium, less native, or harder to use in the first week of internal use?
- Do not inflate severity. P0 means a concrete dogfood-blocking or core-identity-blocking issue.

Output:
- Write a concise markdown report to:
  docs/audits/frontend-polish-2026-05/areas/03-touch-targets-accessibility-native-feel/findings.md
- Use sections: Summary, Findings, Evidence, Suggested Fix Direction, Verification Ideas.

Audit touch targets, accessibility labels/states, hit slop, and native interaction feel.

Focus files:
- Travel App/components/ui/Tap.tsx
- Travel App/components/ui/Button.tsx
- Travel App/components/ui/NavPills.tsx
- Travel App/components/ui/ScreenHeader.tsx
- Travel App/components/trip/TripHeader.tsx
- Travel App/components/chat/ComposerBar.tsx
- Travel App/app/(tabs)/**

Research baseline:
- Apple HIG accessibility target guidance, especially 44x44 pt iOS/iPadOS target size.
- WCAG 2.2 target-size minimum as a lower accessibility floor.
- Common mobile practice for icon buttons, bottom bars, segmented controls, and destructive actions.

Questions:
1. Which icon-only controls are likely below 44pt?
2. Where is hit slop missing?
3. Where are accessibility labels, roles, states, or hints missing?
4. Where does press feedback feel inconsistent?
5. Should `Tap`, `Button`, or a new `IconButton` enforce the standard mechanically?
```

### Prompt 4 - Private Vesper Chat Polish

```text
You are a frontend polish researcher auditing the Travel App inside Travel Workspace.

Workspace root:
/Users/feihuyan/Documents/Claude/Travel Workspace

Primary repo:
/Users/feihuyan/Documents/Claude/Travel Workspace/Travel App

Read first:
- AGENTS.md
- Travel App/CLAUDE.md
- Travel App/docs/Design Language.md
- Travel App/docs/Brand Identity.md
- Travel App/docs/Components.md
- Travel App/docs/Design Workflow.md
- Travel App/docs/Review Rubric.md
- docs/audits/frontend-polish-2026-05/README.md

Rules:
- Audit only. Do not edit product code.
- You may create or update only this report file:
  docs/audits/frontend-polish-2026-05/areas/04-private-vesper-chat-polish/findings.md
- Prefer rg over grep.
- Do not read .env files or secrets.
- Use file and line references for every concrete finding.
- Compare the implementation against Vesper's own design doctrine and against current platform guidance such as Apple HIG, Material accessibility guidance, and WCAG 2.2 target-size guidance.
- Where you cite external guidance, link the source.
- Focus on dogfood polish: what would make the app feel less trustworthy, less premium, less native, or harder to use in the first week of internal use?
- Do not inflate severity. P0 means a concrete dogfood-blocking or core-identity-blocking issue.

Output:
- Write a concise markdown report to:
  docs/audits/frontend-polish-2026-05/areas/04-private-vesper-chat-polish/findings.md
- Use sections: Summary, Findings, Evidence, Suggested Fix Direction, Verification Ideas.

Audit the private Vesper chat experience as the core product relationship.

Focus files:
- Travel App/docs/design-decisions/agent-chat.md
- Travel App/docs/page-specs/agent-chat.md
- Travel App/app/(tabs)/concierge/chat.tsx
- Travel App/components/chat/MessageBubble.tsx
- Travel App/components/chat/ComposerBar.tsx
- Travel App/components/chat/RecommendationBlock.tsx
- Travel App/hooks/useConciergeChat.ts

Research baseline:
- Best-in-class assistant/chat UX patterns from native mobile apps.
- Apple HIG guidance on hierarchy, controls, and accessibility.
- Vesper's own doctrine: private AI should feel like a composed concierge relationship, not generic group chat.

Questions:
1. Where does private chat reuse group chat metaphors in ways that hurt product identity?
2. What should render as prose, note, card, inline action, or operational status?
3. How should streaming, retry, privacy simplification, and attachments look without clutter?
4. Which states are missing or visually weak: loading, empty, error, offline, reconnecting?
5. What component split would let private and group chat diverge cleanly?
```

### Prompt 5 - Trip Workspace And Plan Hierarchy

```text
You are a frontend polish researcher auditing the Travel App inside Travel Workspace.

Workspace root:
/Users/feihuyan/Documents/Claude/Travel Workspace

Primary repo:
/Users/feihuyan/Documents/Claude/Travel Workspace/Travel App

Read first:
- AGENTS.md
- Travel App/CLAUDE.md
- Travel App/docs/Design Language.md
- Travel App/docs/Brand Identity.md
- Travel App/docs/Components.md
- Travel App/docs/Design Workflow.md
- Travel App/docs/Review Rubric.md
- docs/audits/frontend-polish-2026-05/README.md

Rules:
- Audit only. Do not edit product code.
- You may create or update only this report file:
  docs/audits/frontend-polish-2026-05/areas/05-trip-workspace-plan-hierarchy/findings.md
- Prefer rg over grep.
- Do not read .env files or secrets.
- Use file and line references for every concrete finding.
- Compare the implementation against Vesper's own design doctrine and against current platform guidance such as Apple HIG, Material accessibility guidance, and WCAG 2.2 target-size guidance.
- Where you cite external guidance, link the source.
- Focus on dogfood polish: what would make the app feel less trustworthy, less premium, less native, or harder to use in the first week of internal use?
- Do not inflate severity. P0 means a concrete dogfood-blocking or core-identity-blocking issue.

Output:
- Write a concise markdown report to:
  docs/audits/frontend-polish-2026-05/areas/05-trip-workspace-plan-hierarchy/findings.md
- Use sections: Summary, Findings, Evidence, Suggested Fix Direction, Verification Ideas.

Audit the trip workspace, including trip home, plan, map, photos, and memory navigation.

Focus files:
- Travel App/app/(tabs)/trips/[tripId]/_layout.tsx
- Travel App/components/trip/TripHeader.tsx
- Travel App/app/(tabs)/trips/[tripId]/index.tsx
- Travel App/app/(tabs)/trips/[tripId]/plan.tsx
- Travel App/app/(tabs)/trips/[tripId]/map.tsx
- Travel App/app/(tabs)/trips/[tripId]/photos.tsx
- Travel App/app/(tabs)/trips/[tripId]/memory.tsx
- Travel App/components/trip-home/*

Research baseline:
- Native travel/productivity apps with clear workspace hierarchy.
- Apple HIG layout and tab/navigation guidance.
- Common practice for nested navigation: avoid redundant persistent chrome, keep context but reduce controls.

Questions:
1. Is the trip workspace first viewport calm and legible?
2. Which controls are persistent but low-frequency?
3. Where do bottom tabs, trip header, nav pills, and section modules compete?
4. Does Plan feel like the primary trip surface or one of many equal tabs?
5. What should be collapsed, moved, or converted to contextual action?
```

### Prompt 6 - Card System And Surface Taxonomy

```text
You are a frontend polish researcher auditing the Travel App inside Travel Workspace.

Workspace root:
/Users/feihuyan/Documents/Claude/Travel Workspace

Primary repo:
/Users/feihuyan/Documents/Claude/Travel Workspace/Travel App

Read first:
- AGENTS.md
- Travel App/CLAUDE.md
- Travel App/docs/Design Language.md
- Travel App/docs/Brand Identity.md
- Travel App/docs/Components.md
- Travel App/docs/Design Workflow.md
- Travel App/docs/Review Rubric.md
- docs/audits/frontend-polish-2026-05/README.md

Rules:
- Audit only. Do not edit product code.
- You may create or update only this report file:
  docs/audits/frontend-polish-2026-05/areas/06-card-system-surface-taxonomy/findings.md
- Prefer rg over grep.
- Do not read .env files or secrets.
- Use file and line references for every concrete finding.
- Compare the implementation against Vesper's own design doctrine and against current platform guidance such as Apple HIG, Material accessibility guidance, and WCAG 2.2 target-size guidance.
- Where you cite external guidance, link the source.
- Focus on dogfood polish: what would make the app feel less trustworthy, less premium, less native, or harder to use in the first week of internal use?
- Do not inflate severity. P0 means a concrete dogfood-blocking or core-identity-blocking issue.

Output:
- Write a concise markdown report to:
  docs/audits/frontend-polish-2026-05/areas/06-card-system-surface-taxonomy/findings.md
- Use sections: Summary, Findings, Evidence, Suggested Fix Direction, Verification Ideas.

Audit every card-like surface and propose a stricter card taxonomy.

Focus files:
- Travel App/components/ui/Card.tsx
- Travel App/components/brand/LetterpressCard.tsx
- Travel App/components/trip/TripCard.tsx
- Travel App/components/trip-home/*
- Travel App/components/chat/*
- Travel App/components/discover/*
- Travel App/components/angles/*
- Travel App/components/me/*
- Travel App/app/(tabs)/**

Research baseline:
- Premium mobile apps that distinguish editorial cards, utility panels, forms, list rows, and action modules.
- Apple HIG hierarchy/grouping guidance.
- Vesper Design Language rules on parchment, earth tones, purple, and tactile radii.

Questions:
1. How many different card styles exist today?
2. Which styles are product-defining vs generic utility?
3. Where are cards nested inside cards or visually over-framed?
4. Which modules should use `LetterpressCard` or a new editorial primitive?
5. What card taxonomy should be enforced before dogfooding?
```

### Prompt 7 - Discover And Me Information Architecture

```text
You are a frontend polish researcher auditing the Travel App inside Travel Workspace.

Workspace root:
/Users/feihuyan/Documents/Claude/Travel Workspace

Primary repo:
/Users/feihuyan/Documents/Claude/Travel Workspace/Travel App

Read first:
- AGENTS.md
- Travel App/CLAUDE.md
- Travel App/docs/Design Language.md
- Travel App/docs/Brand Identity.md
- Travel App/docs/Components.md
- Travel App/docs/Design Workflow.md
- Travel App/docs/Review Rubric.md
- docs/audits/frontend-polish-2026-05/README.md

Rules:
- Audit only. Do not edit product code.
- You may create or update only this report file:
  docs/audits/frontend-polish-2026-05/areas/07-discover-me-information-architecture/findings.md
- Prefer rg over grep.
- Do not read .env files or secrets.
- Use file and line references for every concrete finding.
- Compare the implementation against Vesper's own design doctrine and against current platform guidance such as Apple HIG, Material accessibility guidance, and WCAG 2.2 target-size guidance.
- Where you cite external guidance, link the source.
- Focus on dogfood polish: what would make the app feel less trustworthy, less premium, less native, or harder to use in the first week of internal use?
- Do not inflate severity. P0 means a concrete dogfood-blocking or core-identity-blocking issue.

Output:
- Write a concise markdown report to:
  docs/audits/frontend-polish-2026-05/areas/07-discover-me-information-architecture/findings.md
- Use sections: Summary, Findings, Evidence, Suggested Fix Direction, Verification Ideas.

Audit Discover and Me as information-architecture and visual-hierarchy surfaces.

Focus files:
- Travel App/app/(tabs)/discover/index.tsx
- Travel App/components/angles/*
- Travel App/components/discover/*
- Travel App/components/venue/*
- Travel App/app/(tabs)/me/index.tsx
- Travel App/components/me/*

Research baseline:
- Best practices from consumer apps where discovery/profile pages have one obvious primary job.
- Apple HIG guidance on hierarchy and grouping.
- Common practice for progressive disclosure and reducing dashboard-like widget walls.

Questions:
1. What is the one-sentence job of Discover today?
2. What is the one-sentence job of Me today?
3. Which modules compete for primary attention?
4. Which modules should move below the fold, behind disclosure, or out of the tab?
5. What first-viewport composition would feel more polished?
```

### Prompt 8 - Imagery, Empty States, And Placeholder Honesty

```text
You are a frontend polish researcher auditing the Travel App inside Travel Workspace.

Workspace root:
/Users/feihuyan/Documents/Claude/Travel Workspace

Primary repo:
/Users/feihuyan/Documents/Claude/Travel Workspace/Travel App

Read first:
- AGENTS.md
- Travel App/CLAUDE.md
- Travel App/docs/Design Language.md
- Travel App/docs/Brand Identity.md
- Travel App/docs/Components.md
- Travel App/docs/Design Workflow.md
- Travel App/docs/Review Rubric.md
- docs/audits/frontend-polish-2026-05/README.md

Rules:
- Audit only. Do not edit product code.
- You may create or update only this report file:
  docs/audits/frontend-polish-2026-05/areas/08-imagery-empty-states-placeholder-honesty/findings.md
- Prefer rg over grep.
- Do not read .env files or secrets.
- Use file and line references for every concrete finding.
- Compare the implementation against Vesper's own design doctrine and against current platform guidance such as Apple HIG, Material accessibility guidance, and WCAG 2.2 target-size guidance.
- Where you cite external guidance, link the source.
- Focus on dogfood polish: what would make the app feel less trustworthy, less premium, less native, or harder to use in the first week of internal use?
- Do not inflate severity. P0 means a concrete dogfood-blocking or core-identity-blocking issue.

Output:
- Write a concise markdown report to:
  docs/audits/frontend-polish-2026-05/areas/08-imagery-empty-states-placeholder-honesty/findings.md
- Use sections: Summary, Findings, Evidence, Suggested Fix Direction, Verification Ideas.

Audit imagery, empty states, skeletons, placeholders, and visual specificity.

Focus files:
- Travel App/assets/*
- Travel App/components/brand/HonestIllustration.tsx
- Travel App/components/ui/EmptyState.tsx
- Travel App/components/ui/Skeleton.tsx
- Travel App/components/trip/TripCard.tsx
- Travel App/components/trip-home/*
- Travel App/app/(tabs)/trips/**
- Travel App/app/(tabs)/discover/**

Research baseline:
- Premium travel apps and editorial products that use imagery to make place and state concrete.
- Vesper's doctrine: no generic placeholders, empty states should teach or delight, real destination specificity matters.

Questions:
1. Where does repeated placeholder imagery make the app feel fake?
2. Where do empty states use generic copy or generic visuals?
3. Which dogfood flows need seeded real imagery first?
4. Should destination fallback art be generated, curated, or algorithmic?
5. What rules prevent placeholder visuals from leaking into dogfood builds?
```

### Prompt 9 - Color, Purple Discipline, And Semantic State

```text
You are a frontend polish researcher auditing the Travel App inside Travel Workspace.

Workspace root:
/Users/feihuyan/Documents/Claude/Travel Workspace

Primary repo:
/Users/feihuyan/Documents/Claude/Travel Workspace/Travel App

Read first:
- AGENTS.md
- Travel App/CLAUDE.md
- Travel App/docs/Design Language.md
- Travel App/docs/Brand Identity.md
- Travel App/docs/Components.md
- Travel App/docs/Design Workflow.md
- Travel App/docs/Review Rubric.md
- docs/audits/frontend-polish-2026-05/README.md

Rules:
- Audit only. Do not edit product code.
- You may create or update only this report file:
  docs/audits/frontend-polish-2026-05/areas/09-color-purple-discipline-semantic-state/findings.md
- Prefer rg over grep.
- Do not read .env files or secrets.
- Use file and line references for every concrete finding.
- Compare the implementation against Vesper's own design doctrine and against current platform guidance such as Apple HIG, Material accessibility guidance, and WCAG 2.2 target-size guidance.
- Where you cite external guidance, link the source.
- Focus on dogfood polish: what would make the app feel less trustworthy, less premium, less native, or harder to use in the first week of internal use?
- Do not inflate severity. P0 means a concrete dogfood-blocking or core-identity-blocking issue.

Output:
- Write a concise markdown report to:
  docs/audits/frontend-polish-2026-05/areas/09-color-purple-discipline-semantic-state/findings.md
- Use sections: Summary, Findings, Evidence, Suggested Fix Direction, Verification Ideas.

Audit color usage, semantic state, and purple discipline.

Focus files:
- Travel App/constants/colors.ts
- Travel App/components/**
- Travel App/app/**

Research baseline:
- Apple HIG color/accessibility guidance.
- Material accessibility and contrast guidance.
- Vesper doctrine: purple is agent presence only; earth tones are semantic; status labels should be typographic.

Questions:
1. Where are raw hex values used?
2. Where is purple used outside AI/concierge presence?
3. Where do colors communicate state inconsistently?
4. Where might contrast fail in disabled, tertiary, timestamp, or badge text?
5. Which color usages need semantic tokens?
```

### Prompt 10 - Visual QA And Regression Gates

```text
You are a frontend polish researcher auditing the Travel App inside Travel Workspace.

Workspace root:
/Users/feihuyan/Documents/Claude/Travel Workspace

Primary repo:
/Users/feihuyan/Documents/Claude/Travel Workspace/Travel App

Read first:
- AGENTS.md
- Travel App/CLAUDE.md
- Travel App/docs/Design Language.md
- Travel App/docs/Brand Identity.md
- Travel App/docs/Components.md
- Travel App/docs/Design Workflow.md
- Travel App/docs/Review Rubric.md
- docs/audits/frontend-polish-2026-05/README.md

Rules:
- Audit only. Do not edit product code.
- You may create or update only this report file:
  docs/audits/frontend-polish-2026-05/areas/10-visual-qa-regression-gates/findings.md
- Prefer rg over grep.
- Do not read .env files or secrets.
- Use file and line references for every concrete finding.
- Compare the implementation against Vesper's own design doctrine and against current platform guidance such as Apple HIG, Material accessibility guidance, and WCAG 2.2 target-size guidance.
- Where you cite external guidance, link the source.
- Focus on dogfood polish: what would make the app feel less trustworthy, less premium, less native, or harder to use in the first week of internal use?
- Do not inflate severity. P0 means a concrete dogfood-blocking or core-identity-blocking issue.

Output:
- Write a concise markdown report to:
  docs/audits/frontend-polish-2026-05/areas/10-visual-qa-regression-gates/findings.md
- Use sections: Summary, Findings, Evidence, Suggested Fix Direction, Verification Ideas.

Design a practical visual QA and regression workflow for Travel App.

Focus files:
- Travel App/package.json
- Travel App/app.json
- Travel App/eas.json
- Travel App/app/**
- Travel App/components/**
- workspace Makefile and scripts

Research baseline:
- Common React Native/Expo visual QA practices.
- Screenshot testing with simulator/device automation.
- Expo web as a low-cost internal visual review target when feasible.
- Accessibility text-size review and small-device viewport review.

Questions:
1. What is the lowest-friction way to capture repeatable screenshots for dogfood-critical screens?
2. Should this repo add Expo web support, simulator screenshot scripts, Storybook, or a custom screenshot route?
3. What seeded data is needed for useful screenshots?
4. Which screens and states must be captured before dogfooding?
5. What should run in CI vs locally before release?
```

## Suggested Synthesis Prompt

Run this after the parallel reports land.

```text
You are a frontend polish synthesis researcher auditing the Travel App inside Travel Workspace.

Workspace root:
/Users/feihuyan/Documents/Claude/Travel Workspace

Primary repo:
/Users/feihuyan/Documents/Claude/Travel Workspace/Travel App

Read first:
- AGENTS.md
- Travel App/CLAUDE.md
- Travel App/docs/Design Language.md
- Travel App/docs/Brand Identity.md
- Travel App/docs/Components.md
- Travel App/docs/Design Workflow.md
- Travel App/docs/Review Rubric.md
- docs/audits/frontend-polish-2026-05/README.md
- all findings.md files under docs/audits/frontend-polish-2026-05/areas/

Rules:
- Synthesis only. Do not edit product code.
- You may create or update only this report file:
  docs/audits/frontend-polish-2026-05/MASTER-PUNCH-LIST.md
- Prefer rg over grep.
- Do not read .env files or secrets.
- Use file and line references for every concrete finding.
- Preserve links to external guidance where the area reports cite them.
- Focus on dogfood polish: what would make the app feel less trustworthy, less premium, less native, or harder to use in the first week of internal use?
- Do not inflate severity. P0 means a concrete dogfood-blocking or core-identity-blocking issue.

Output:
- Write the final markdown synthesis to:
  docs/audits/frontend-polish-2026-05/MASTER-PUNCH-LIST.md

Synthesize the frontend polish research reports under docs/audits/frontend-polish-2026-05.

Create a prioritized dogfood polish punch list with:
- P0/P1/P2 severity
- affected surface
- concrete user impact
- file references
- recommended implementation direction
- verification plan
- whether the fix is design-system, screen-specific, or QA-process work

Keep the output practical. The goal is not a redesign manifesto; the goal is to make the app polished enough for dogfooding.
```
