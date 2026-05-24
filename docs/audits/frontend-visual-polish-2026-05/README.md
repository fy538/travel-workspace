# Frontend Visual Polish Audit - May 2026

Status: fresh audit round  
Scope: rendered visual polish, native feel, interaction quality, copy, state coverage, and dogfood journey perception  
Created: 2026-05-24

## Purpose

This is a separate audit round from `docs/audits/frontend-polish-2026-05`.

The earlier round focuses on frontend implementation polish: design-system drift, spacing tokens, typography tokens, card taxonomy, touch targets, information architecture, color discipline, and visual QA process.

This round focuses on perceived product quality: what the app looks and feels like when a human actually uses it. The goal is to answer whether Vesper feels finished, native, calm, premium, and dogfoodable.

In short:

- `frontend-polish-2026-05` asks: is the frontend implementation aligned with the design system?
- `frontend-visual-polish-2026-05` asks: does the app feel visually and experientially polished on real screens?

## How To Run

Run the prompts below in parallel where possible. Each prompt is self-contained and includes its own output path.

Recommended workspace root:

`/Users/feihuyan/Documents/Claude/Travel Workspace`

Each researcher should:

1. Read the required docs.
2. Inspect the relevant code.
3. Use screenshots, simulator, TestFlight, or local device output if available.
4. If screenshots are not available, say so explicitly and perform a static/perceptual risk audit from code.
5. Write exactly one markdown report to the assigned folder.

Do not edit product code in this audit round.

## Output Folders

- `docs/audits/frontend-visual-polish-2026-05/areas/01-rendered-composition-first-viewports/findings.md`
- `docs/audits/frontend-visual-polish-2026-05/areas/02-motion-transitions-feedback/findings.md`
- `docs/audits/frontend-visual-polish-2026-05/areas/03-ios-native-conventions/findings.md`
- `docs/audits/frontend-visual-polish-2026-05/areas/04-copy-microcopy-tone/findings.md`
- `docs/audits/frontend-visual-polish-2026-05/areas/05-state-polish-empty-loading-error-offline/findings.md`
- `docs/audits/frontend-visual-polish-2026-05/areas/06-performance-perception-jank/findings.md`
- `docs/audits/frontend-visual-polish-2026-05/areas/07-dogfood-journey-walkthrough/findings.md`
- `docs/audits/frontend-visual-polish-2026-05/areas/08-visual-brand-specificity/findings.md`
- `docs/audits/frontend-visual-polish-2026-05/areas/09-modal-sheet-keyboard-polish/findings.md`
- `docs/audits/frontend-visual-polish-2026-05/areas/10-accessibility-visual-resilience/findings.md`
- Synthesis output: `docs/audits/frontend-visual-polish-2026-05/MASTER-PUNCH-LIST.md`

## Prompt 1 - Rendered Composition And First Viewports

```text
You are a frontend visual-polish researcher auditing the Travel App inside Travel Workspace.

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
- docs/audits/frontend-visual-polish-2026-05/README.md

Rules:
- Audit only. Do not edit product code.
- You may create or update only this report file:
  docs/audits/frontend-visual-polish-2026-05/areas/01-rendered-composition-first-viewports/findings.md
- Prefer rg over grep.
- Do not read .env files or secrets.
- Use file and line references for every concrete implementation finding.
- Use screenshots, simulator, TestFlight, or device output if available.
- If rendered screenshots are unavailable, state that clearly and perform a static composition-risk audit from code.
- Compare against Vesper's own design doctrine and current platform guidance such as Apple HIG layout, typography, accessibility, and WCAG target-size guidance where relevant.
- Where you cite external guidance, link the source.
- Focus on dogfood polish: what would make the app feel less finished, less native, less premium, or harder to trust in the first week of internal use?
- Do not inflate severity. P0 means a concrete dogfood-blocking or core-identity-blocking issue.

Output:
- Write a concise markdown report to:
  docs/audits/frontend-visual-polish-2026-05/areas/01-rendered-composition-first-viewports/findings.md
- Use sections: Summary, Screens/Surfaces Reviewed, Findings, Evidence, Suggested Fix Direction, Verification Ideas.

Audit rendered screen composition and first viewport quality.

Focus surfaces:
- Trips list
- Trip home / plan landing
- Private Vesper chat
- Group trip chat
- Plan timeline
- Discover
- Me

Questions:
1. Does each first viewport have a clear focal point?
2. Are gutters, card edges, text blocks, section headers, and controls optically aligned?
3. Does the screen feel composed, or like stacked modules?
4. Is there too much chrome above the useful content?
5. Which screens look most unfinished or generic?
6. Which fixes would most improve perceived polish before dogfooding?
```

## Prompt 2 - Motion, Transitions, And Feedback

```text
You are a frontend visual-polish researcher auditing the Travel App inside Travel Workspace.

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
- docs/audits/frontend-visual-polish-2026-05/README.md

Rules:
- Audit only. Do not edit product code.
- You may create or update only this report file:
  docs/audits/frontend-visual-polish-2026-05/areas/02-motion-transitions-feedback/findings.md
- Prefer rg over grep.
- Do not read .env files or secrets.
- Use file and line references for every concrete implementation finding.
- Use screenshots/video/simulator/device output if available.
- If runtime inspection is unavailable, state that clearly and perform a static interaction-risk audit from code.
- Compare against Vesper's design doctrine and current platform guidance where relevant.
- Where you cite external guidance, link the source.
- Focus on dogfood polish: does the app feel responsive, calm, native, and deliberate?
- Do not inflate severity. P0 means a concrete dogfood-blocking or core-identity-blocking issue.

Output:
- Write a concise markdown report to:
  docs/audits/frontend-visual-polish-2026-05/areas/02-motion-transitions-feedback/findings.md
- Use sections: Summary, Interactions Reviewed, Findings, Evidence, Suggested Fix Direction, Verification Ideas.

Audit motion, transitions, haptics, press feedback, loading movement, and perceived responsiveness.

Focus files:
- Travel App/components/ui/Tap.tsx
- Travel App/components/ui/Button.tsx
- Travel App/components/ui/NavPills.tsx
- Travel App/components/chat/ComposerBar.tsx
- Travel App/components/voice/*
- Travel App/components/trip/ProposalReviewSheet.tsx
- Travel App/components/expense/AddExpenseSheet.tsx
- Travel App/app/(tabs)/**

Questions:
1. Do taps, long presses, disabled states, loading states, and retries provide clear feedback?
2. Do sheets and modals enter/exit in a way that feels native and intentional?
3. Are there missing haptics on meaningful actions?
4. Does streaming chat feel alive without being noisy?
5. Are there abrupt transitions that make the app feel unfinished?
6. Which interactions need motion specs before implementation work continues?
```

## Prompt 3 - iOS Native Conventions

```text
You are a frontend visual-polish researcher auditing the Travel App inside Travel Workspace.

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
- docs/audits/frontend-visual-polish-2026-05/README.md

Rules:
- Audit only. Do not edit product code.
- You may create or update only this report file:
  docs/audits/frontend-visual-polish-2026-05/areas/03-ios-native-conventions/findings.md
- Prefer rg over grep.
- Do not read .env files or secrets.
- Use file and line references for every concrete implementation finding.
- Use simulator/device output if available.
- If runtime inspection is unavailable, state that clearly and perform a static native-convention audit from code.
- Compare against Apple HIG navigation, layout, inputs, sheets, tab bars, safe areas, keyboard, accessibility, and typography.
- Where you cite external guidance, link the source.
- Focus on dogfood polish: where does the app feel less iOS-native than it should?
- Do not inflate severity. P0 means a concrete dogfood-blocking or core-identity-blocking issue.

Output:
- Write a concise markdown report to:
  docs/audits/frontend-visual-polish-2026-05/areas/03-ios-native-conventions/findings.md
- Use sections: Summary, Native Conventions Reviewed, Findings, Evidence, Suggested Fix Direction, Verification Ideas.

Audit iOS-native conventions and platform fit.

Focus files:
- Travel App/app/_layout.tsx
- Travel App/app/(tabs)/_layout.tsx
- Travel App/app/(tabs)/**
- Travel App/components/ui/ScreenHeader.tsx
- Travel App/components/ui/NavPills.tsx
- Travel App/components/trip/TripHeader.tsx
- Travel App/components/chat/ComposerBar.tsx
- Travel App/components/**/*Sheet.tsx

Questions:
1. Do tab bars, headers, back behavior, and nested navigation feel native?
2. Are safe areas and status bar areas handled consistently?
3. Are sheets, modals, menus, and pickers platform-appropriate?
4. Does keyboard avoidance feel correct in chat, forms, and sheets?
5. Are destructive and confirmation actions presented in familiar ways?
6. Which conventions should Vesper intentionally break, and which should it follow?
```

## Prompt 4 - Copy, Microcopy, And Tone

```text
You are a frontend visual-polish researcher auditing the Travel App inside Travel Workspace.

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
- docs/audits/frontend-visual-polish-2026-05/README.md

Rules:
- Audit only. Do not edit product code.
- You may create or update only this report file:
  docs/audits/frontend-visual-polish-2026-05/areas/04-copy-microcopy-tone/findings.md
- Prefer rg over grep.
- Do not read .env files or secrets.
- Use file and line references for every concrete copy finding.
- Compare against Vesper's design doctrine: interesting, specific, quietly diplomatic, not generic, not overexplaining private constraints.
- Focus on dogfood polish: what copy feels placeholder, generic, robotic, too SaaS-like, too cute, too verbose, or not trustworthy?
- Do not inflate severity. P0 means a concrete dogfood-blocking or core-identity-blocking issue.

Output:
- Write a concise markdown report to:
  docs/audits/frontend-visual-polish-2026-05/areas/04-copy-microcopy-tone/findings.md
- Use sections: Summary, Copy Surfaces Reviewed, Findings, Evidence, Suggested Fix Direction, Verification Ideas.

Audit copy and microcopy polish.

Focus surfaces:
- Empty states
- Error messages
- Loading messages
- CTA labels
- Chat composer placeholders
- Permission prompts
- Proposal/review language
- Trip status and phase labels
- Discover and Me copy

Focus files:
- Travel App/app/**
- Travel App/components/**
- Travel App/constants/**

Questions:
1. Which strings feel generic or placeholder?
2. Which strings sound like software instead of a concierge?
3. Which strings overexplain privacy, constraints, or internal mechanics?
4. Which CTA labels are unclear or low-confidence?
5. Where should copy become more concrete to this trip, this place, or this user?
6. What microcopy changes are highest leverage before dogfooding?
```

## Prompt 5 - State Polish: Empty, Loading, Error, Offline

```text
You are a frontend visual-polish researcher auditing the Travel App inside Travel Workspace.

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
- docs/audits/frontend-visual-polish-2026-05/README.md

Rules:
- Audit only. Do not edit product code.
- You may create or update only this report file:
  docs/audits/frontend-visual-polish-2026-05/areas/05-state-polish-empty-loading-error-offline/findings.md
- Prefer rg over grep.
- Do not read .env files or secrets.
- Use file and line references for every concrete implementation finding.
- Use screenshots/simulator/device output if available.
- If runtime inspection is unavailable, state that clearly and perform a static state-coverage audit from code.
- Compare against Vesper's doctrine: empty states teach or delight; loading states evoke anticipation; errors are calm and recoverable.
- Focus on dogfood polish: what states will users hit in early dogfooding that currently feel broken or unfinished?
- Do not inflate severity. P0 means a concrete dogfood-blocking or core-identity-blocking issue.

Output:
- Write a concise markdown report to:
  docs/audits/frontend-visual-polish-2026-05/areas/05-state-polish-empty-loading-error-offline/findings.md
- Use sections: Summary, States Reviewed, Findings, Evidence, Suggested Fix Direction, Verification Ideas.

Audit empty, loading, error, offline, permission-denied, partial-data, stale-data, disabled, and retry states.

Focus files:
- Travel App/components/ui/EmptyState.tsx
- Travel App/components/ui/Skeleton.tsx
- Travel App/components/chat/*
- Travel App/hooks/*
- Travel App/app/(tabs)/**
- Travel App/app/notifications*
- Travel App/app/invite/**
- Travel App/app/trip-*

Questions:
1. Which important screens lack explicit empty/loading/error/offline states?
2. Which states exist but feel generic or visually weak?
3. Which retry flows are unclear?
4. Which permission-denied states need better recovery paths?
5. Which dogfood scenarios are most likely to expose unfinished states?
6. What state matrix should be required for dogfood-critical screens?
```

## Prompt 6 - Performance Perception And Jank

```text
You are a frontend visual-polish researcher auditing the Travel App inside Travel Workspace.

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
- docs/audits/frontend-visual-polish-2026-05/README.md

Rules:
- Audit only. Do not edit product code.
- You may create or update only this report file:
  docs/audits/frontend-visual-polish-2026-05/areas/06-performance-perception-jank/findings.md
- Prefer rg over grep.
- Do not read .env files or secrets.
- Use file and line references for every concrete implementation finding.
- Use runtime profiling/simulator/device observation if available.
- If runtime profiling is unavailable, state that clearly and perform a static performance-risk audit from code.
- Focus on perceived performance: jank, layout shifts, slow first paint, expensive rerenders, list performance, image loading, chat streaming smoothness.
- Do not inflate severity. P0 means a concrete dogfood-blocking issue.

Output:
- Write a concise markdown report to:
  docs/audits/frontend-visual-polish-2026-05/areas/06-performance-perception-jank/findings.md
- Use sections: Summary, Performance Surfaces Reviewed, Findings, Evidence, Suggested Fix Direction, Verification Ideas.

Audit perceived performance and jank risk.

Focus files:
- Travel App/app/(tabs)/discover/index.tsx
- Travel App/app/(tabs)/concierge/chat.tsx
- Travel App/app/(tabs)/trips/[tripId]/index.tsx
- Travel App/app/(tabs)/trips/[tripId]/photos.tsx
- Travel App/app/(tabs)/me/index.tsx
- Travel App/hooks/useConciergeChat.ts
- Travel App/hooks/useGroupChat.ts
- Travel App/components/**/*Sheet.tsx
- Travel App/components/**/*List*.tsx

Questions:
1. Which screens are likely to jank because of large render trees or local state?
2. Which lists need stronger virtualization or memoization?
3. Which image paths risk slow loads, layout shifts, or blank states?
4. Does chat streaming risk excessive rerendering?
5. Which bottom sheets or overlays are heavy enough to feel sluggish?
6. What cheap measurements should be added before dogfooding?
```

## Prompt 7 - Dogfood Journey Walkthrough

```text
You are a frontend visual-polish researcher auditing the Travel App inside Travel Workspace.

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
- docs/reliability/Golden Paths.md
- docs/audits/frontend-polish-2026-05/README.md
- docs/audits/frontend-visual-polish-2026-05/README.md

Rules:
- Audit only. Do not edit product code.
- You may create or update only this report file:
  docs/audits/frontend-visual-polish-2026-05/areas/07-dogfood-journey-walkthrough/findings.md
- Prefer rg over grep.
- Do not read .env files or secrets.
- Use file and line references for every concrete implementation finding.
- Use screenshots/simulator/device output if available.
- If runtime walkthrough is unavailable, state that clearly and perform a static journey-risk audit from code and docs.
- Focus on lived product quality across a complete dogfood journey, not isolated components.
- Do not inflate severity. P0 means a concrete dogfood-blocking journey issue.

Output:
- Write a concise markdown report to:
  docs/audits/frontend-visual-polish-2026-05/areas/07-dogfood-journey-walkthrough/findings.md
- Use sections: Summary, Journey Reviewed, Findings, Evidence, Suggested Fix Direction, Verification Ideas.

Audit a complete dogfood journey end to end.

Journey:
1. Open app as a dogfood user.
2. See trips list.
3. Create or open a planning trip.
4. Invite people or inspect group state.
5. Ask Vesper privately for help.
6. Review a proposal or recommendation.
7. Inspect the plan/map.
8. Use group chat.
9. Encounter at least one loading/error/empty state.
10. Check Me/profile context.

Questions:
1. Where does the experience stop feeling like one coherent product?
2. Where does the user lose confidence or context?
3. Which transitions between surfaces feel awkward?
4. Which step has the weakest visual polish?
5. Which top 5 changes would make the app feel dogfoodable fastest?
```

## Prompt 8 - Visual Brand Specificity

```text
You are a frontend visual-polish researcher auditing the Travel App inside Travel Workspace.

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
- docs/audits/frontend-visual-polish-2026-05/README.md

Rules:
- Audit only. Do not edit product code.
- You may create or update only this report file:
  docs/audits/frontend-visual-polish-2026-05/areas/08-visual-brand-specificity/findings.md
- Prefer rg over grep.
- Do not read .env files or secrets.
- Use file and line references for every concrete implementation finding.
- Use screenshots/simulator/device output if available.
- If rendered screenshots are unavailable, state that clearly and perform a static brand-risk audit from code.
- Compare against Vesper's own brand doctrine: leather travel journal, editorial, place-aware, purple as agent presence, specific over generic.
- Focus on whether the app looks like Vesper specifically, not merely a competent React Native app.
- Do not inflate severity. P0 means a concrete core-identity-blocking issue.

Output:
- Write a concise markdown report to:
  docs/audits/frontend-visual-polish-2026-05/areas/08-visual-brand-specificity/findings.md
- Use sections: Summary, Brand Surfaces Reviewed, Findings, Evidence, Suggested Fix Direction, Verification Ideas.

Audit visual brand specificity.

Focus files:
- Travel App/docs/Design Language.md
- Travel App/docs/Brand Identity.md
- Travel App/constants/colors.ts
- Travel App/constants/typography.ts
- Travel App/components/brand/*
- Travel App/components/trip/TripCard.tsx
- Travel App/components/chat/*
- Travel App/app/(tabs)/**

Questions:
1. Which screens unmistakably feel like Vesper?
2. Which screens could belong to any travel/planning app?
3. Where is the leather-journal/editorial metaphor strongest and weakest?
4. Where do generic cards, placeholder visuals, or utilitarian layout dilute the brand?
5. Is purple still meaningful as agent presence?
6. What reusable brand primitives are missing?
```

## Prompt 9 - Modal, Sheet, And Keyboard Polish

```text
You are a frontend visual-polish researcher auditing the Travel App inside Travel Workspace.

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
- docs/audits/frontend-visual-polish-2026-05/README.md

Rules:
- Audit only. Do not edit product code.
- You may create or update only this report file:
  docs/audits/frontend-visual-polish-2026-05/areas/09-modal-sheet-keyboard-polish/findings.md
- Prefer rg over grep.
- Do not read .env files or secrets.
- Use file and line references for every concrete implementation finding.
- Use simulator/device output if available.
- If runtime inspection is unavailable, state that clearly and perform a static sheet/keyboard-risk audit from code.
- Compare against Apple HIG sheet, modal, keyboard, and form behavior where relevant.
- Focus on dogfood polish: do overlays, forms, and text entry feel stable and native?
- Do not inflate severity. P0 means a concrete dogfood-blocking issue.

Output:
- Write a concise markdown report to:
  docs/audits/frontend-visual-polish-2026-05/areas/09-modal-sheet-keyboard-polish/findings.md
- Use sections: Summary, Overlays Reviewed, Findings, Evidence, Suggested Fix Direction, Verification Ideas.

Audit modal, bottom sheet, form, and keyboard behavior.

Focus files:
- Travel App/components/trip/ProposalReviewSheet.tsx
- Travel App/components/expense/AddExpenseSheet.tsx
- Travel App/components/memory/ShareStorySheet.tsx
- Travel App/components/trip/FindPhotosSheet.tsx
- Travel App/components/discover/ExperienceDetailSheet.tsx
- Travel App/components/chat/ComposerBar.tsx
- Travel App/app/trip-*/**
- Travel App/app/venue/**

Questions:
1. Do sheets have consistent height, drag behavior, close affordances, and safe-area handling?
2. Does keyboard avoidance work for chat and forms?
3. Are form fields, labels, validation, and submit buttons visually stable?
4. Are destructive/cancel actions placed safely?
5. Are nested sheets or overlays possible, and do they create confusion?
6. Which sheet should be polished first for dogfooding?
```

## Prompt 10 - Accessibility Visual Resilience

```text
You are a frontend visual-polish researcher auditing the Travel App inside Travel Workspace.

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
- docs/audits/frontend-visual-polish-2026-05/README.md

Rules:
- Audit only. Do not edit product code.
- You may create or update only this report file:
  docs/audits/frontend-visual-polish-2026-05/areas/10-accessibility-visual-resilience/findings.md
- Prefer rg over grep.
- Do not read .env files or secrets.
- Use file and line references for every concrete implementation finding.
- Use simulator/device output with larger text sizes if available.
- If runtime inspection is unavailable, state that clearly and perform a static accessibility-resilience audit from code.
- Compare against Apple HIG accessibility, Dynamic Type expectations, contrast guidance, and WCAG where relevant.
- Focus on whether layouts remain polished under real accessibility conditions.
- Do not inflate severity. P0 means a concrete dogfood-blocking or access-blocking issue.

Output:
- Write a concise markdown report to:
  docs/audits/frontend-visual-polish-2026-05/areas/10-accessibility-visual-resilience/findings.md
- Use sections: Summary, Accessibility Conditions Reviewed, Findings, Evidence, Suggested Fix Direction, Verification Ideas.

Audit visual resilience under accessibility settings.

Focus files:
- Travel App/constants/typography.ts
- Travel App/components/ui/*
- Travel App/components/chat/*
- Travel App/components/trip/*
- Travel App/app/(tabs)/**

Questions:
1. Which layouts are likely to break under larger text?
2. Where do fixed heights, absolute positioning, or small controls create risk?
3. Where do contrast, disabled states, timestamps, badges, or tertiary text look too faint?
4. Are icons and color-only state indicators understandable without color?
5. Which screens need large-text screenshot review before dogfooding?
6. What primitive changes would improve accessibility resilience globally?
```

## Synthesis Prompt

Run this after all area reports land.

```text
You are a frontend visual-polish synthesis researcher auditing the Travel App inside Travel Workspace.

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
- docs/audits/frontend-visual-polish-2026-05/README.md
- all findings.md files under docs/audits/frontend-visual-polish-2026-05/areas/

Rules:
- Synthesis only. Do not edit product code.
- You may create or update only this report file:
  docs/audits/frontend-visual-polish-2026-05/MASTER-PUNCH-LIST.md
- Prefer rg over grep.
- Do not read .env files or secrets.
- Use file and line references for every concrete finding.
- Preserve links to external guidance where the area reports cite them.
- Focus on dogfood polish: what would make the app feel less finished, less native, less premium, less trustworthy, or harder to use in the first week of internal use?
- Do not inflate severity. P0 means a concrete dogfood-blocking or core-identity-blocking issue.

Output:
- Write the final markdown synthesis to:
  docs/audits/frontend-visual-polish-2026-05/MASTER-PUNCH-LIST.md

Synthesize the visual polish research reports under docs/audits/frontend-visual-polish-2026-05.

Create a prioritized dogfood visual-polish punch list with:
- P0/P1/P2 severity
- affected surface
- concrete user impact
- file references
- whether the evidence was rendered/runtime or static/code-based
- recommended implementation direction
- verification plan
- whether the fix is visual design, native behavior, copy, state coverage, performance, or QA-process work

Keep the output practical. The goal is to make the app feel polished enough for dogfooding, not to produce a redesign manifesto.
```
