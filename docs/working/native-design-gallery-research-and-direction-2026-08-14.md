---
doc_type: working
status: active
owner: founder / product / design / frontend
created: 2026-08-14
last_updated: 2026-08-15
expires: 2026-09-13
why_new: Two-pass research and product-engineering direction for turning the app's existing development galleries into a coherent native design workbench, while deciding with evidence whether React Native Storybook should own isolated component stories and agent discovery.
promotes_to: the frontend engineering loop, a protected native composition workbench, and an isolated-component story contract if the proposed pilots prove useful
supersedes: []
related:
  - native-design-gallery-founder-pain-2026-08-15.md
  - visual-polish-evaluation-and-design-workflow-2026-08-13.md
  - product-loop-coherence-maestro-and-environment-strategy-2026-08-12.md
  - ../../travel-app/docs/Frontend Engineering Loop.md
  - ../../travel-app/docs/Design Workflow.md
  - ../../travel-app/docs/design-consolidation/Plan.md
  - ../../travel-app/docs/research/Product-Quality AI Design QA Loop.md
---

# Native design gallery research and direction

> **Working research and direction, not an implementation claim.** This document
> records the August 14 follow-up to the visual-polish discussion and the idea of
> a centralized "design scroll." Counts, routes, dependencies, and vendor
> capabilities are a snapshot as of 2026-08-14. Durable rules should be promoted
> into the frontend contract rather than leaving this note as a second source of
> truth.
>
> **2026-08-15 founder-pain follow-up (revised):** this memo remains the
> architecture. A second-pass check found the first founder-pain note was not
> a better plan — it oversold a menu as a design scroll. The surviving
> change is narrower: make Phase 0 immediately usable (complete hub + DevFab +
> `Stack.Protected`) before coupling it to the Storybook spike. See
> [native-design-gallery-founder-pain-2026-08-15.md](./native-design-gallery-founder-pain-2026-08-15.md).

## Second-pass verdict

The second research pass deliberately searched for evidence against the first
recommendation. It found enough to **revise the sequence, but not the overall
architecture**.

### What remains correct

- Vesper needs a deterministic native visual workbench between design and full
  product journeys.
- Real production components, named fixtures, isolated states, canonical
  compositions, and selected baselines are the right ingredients.
- Whole-surface native galleries remain necessary because isolated component
  stories cannot prove Trips, Vesper, and Places feel coherent together.
- Maestro remains the correct device-level executor. It already owns 12
  baseline flows and 25 `assertScreenshot` checks in this repository.
- Visual change detection and product-quality judgment must remain separate.

### What changes

1. **Do not build a rich custom specimen registry before testing Storybook.**
   Storybook now supplies standard story discovery, tags, deep links, portable
   stories, manifests, and an experimental native MCP endpoint. Recreating all
   of that first would be premature engineering.
2. **Run the Storybook technical spike earlier.** A 3–5 component spike should
   follow the route/gallery audit, before search, custom manifests, or generated
   Maestro catalogs are built.
3. **Use a hybrid ownership model if the spike works.** Storybook owns isolated
   component/pattern states. Native `app/dev` compositions own full surfaces and
   QA-only state bridges. Maestro captures both.
4. **Keep the existing component lifecycle registry narrow.** It intentionally
   governs `components/ui`; it should not be stretched to own every feature
   component and executable specimen. Join lifecycle metadata to stories where
   useful, but do not make one overloaded schema.
5. **Audit dev-route protection before expanding the native hub.** Expo Router's
   official documentation says route files are automatically included and that
   all routes are accessible unless explicitly protected. Conditional
   `<Stack.Screen>` declarations configure routes; they are not, by themselves,
   proof that `app/dev` files are absent or unreachable in an external build.
6. **Use Maestro's native screenshot assertion instead of adding another local
   diff engine.** Its experimental AI defect commands are useful as advisory
   smoke checks, not as polish acceptance.

### Revised one-line direction

> Protect and classify the existing native composition galleries, then run a
> tiny Storybook spike before building custom catalog infrastructure; keep the
> result hybrid unless evidence strongly favors one lane.

### Decision check

| Question | Evidence | Direction |
| --- | --- | --- |
| Do we need a native composition lane? | Existing product galleries, forced-state bridges, and surface contracts depend on app/native context. RNTester and Microsoft Gallery show this pattern remains legitimate. | **Yes; retain and protect it.** |
| Should we build our own isolated-story discovery system first? | Storybook already provides CSF, tags, story indexing, deep links, portable stories, and experimental MCP/manifests. | **No; spike Storybook first.** |
| Is Storybook ready for a wholesale migration? | Strong adoption and better v10 setup, but native MCP is experimental, visual tests remain external, and current 10.5 peers conflict with two app versions. | **No; bounded technical spike.** |
| Do we need another local screenshot engine? | Maestro 2.x has `assertScreenshot`; the repo already has 25 assertions. | **No.** |
| Should Maestro AI be a release gate? | Commands are experimental, cloud-routed, generic, and optional by default. | **Advisory only.** |
| Should we add a hosted review service now? | App Percy is credible and integrates with Maestro/Storybook, but adds account, build, signing, device, and sometimes beta SDK complexity. Chromatic native remains early access. | **Only when review/device operations are measured bottlenecks.** |
| Is the current dev-route boundary proven safe? | Expo Router auto-includes route files; conditional screen declarations are configuration, not demonstrated exclusion. | **No; verify before expansion.** |

## 1. The idea in plain language

The proposed idea makes sense:

> Put the app's real visual language in one development-only place, fill it with
> deterministic mock content, and make it easy to scroll through components,
> cards, patterns, page compositions, and important states as they are supposed
> to look.

This is commonly described as a component workbench, specimen catalog, UI
gallery, preview catalog, or living style guide. "Design scroll" is a useful
product name for its human-review mode, but the implementation should support
both:

1. a **scroll/browse mode** for judging gestalt, rhythm, repetition, and family
   resemblance; and
2. an **isolated specimen mode** for deterministic deep links, screenshots,
   diffs, and agent inspection.

Those modes solve related but different problems. A long scroll is excellent
for noticing that six cards have subtly different radii or that typography has
lost its rhythm. A stable isolated specimen is excellent for automation and
precise review. Trying to make one screenshot do both produces a brittle,
unreadable artifact.

## 2. Executive conclusion

Vesper should build this as a **hybrid workbench**, not as a single giant custom
gallery and not as a wholesale Storybook migration.

The app already has most of the substrate:

- 27 React Native files under `app/dev`, of which roughly 14 are gallery- or
  specimen-like and the rest include state bridges, QA harnesses, and developer
  controls;
- a central design-system hub;
- production-backed token, state, header, control, composer, deck, receipt,
  artifact, onboarding, and product-state galleries;
- a checked-in registry nominally containing 89 components, though its current
  coverage and generated-catalog checks fail on this branch;
- component lifecycle and catalog checks;
- Maestro capture lanes, surface scenarios, baseline checks, perceptual hashing,
  comparison sheets, and structured visual verdicts.

The missing product is not "a gallery." It is **coherence and clear ownership
across the visual-development lanes**:

- one inventory instead of a hard-coded hub plus many unlinked routes;
- one stable specimen identity and deep-link convention;
- named production-relevant states instead of ad hoc mock snippets;
- risk-tiered capture rather than baselining everything;
- whole-surface compositions alongside isolated components;
- an agent-readable manifest that says what exists and when to reuse it; and
- an explicit bridge from specimen to Maestro evidence and accepted design
  intent.

The revised direction is therefore:

```text
real production components + tokens
                ↓
deterministic named fixtures
                ↓
    ┌───────────────┴────────────────┐
    ↓                                ↓
Storybook spike / stories     native compositions
(isolated components)         (surfaces + QA bridges)
    ↓                                ↓
story or route deep links → Maestro assertScreenshot
                    ↓
      calibrated AI + human visual verdict
```

Do not migrate all existing galleries to Storybook. After auditing the current
routes, run a 3–5 component technical spike before building custom search,
manifest, or story-discovery infrastructure. If Storybook works cleanly with
Expo 55, the native renderer, Codex, and Maestro, let it own isolated component
states going forward. Keep canonical surface compositions and operational state
bridges in the app's native development lane.

## 3. What is already in the repository

This was the most important research finding. The question is not greenfield.

### 3.1 Existing native workbench

[`app/dev/design-system.tsx`](../../travel-app/app/dev/design-system.tsx) is a
central production-backed hub. It currently links five galleries:

- state and token gallery;
- header gallery;
- control gallery;
- composer lab; and
- deck gallery.

[`app/dev/gallery.tsx`](../../travel-app/app/dev/gallery.tsx) already calls
itself a scrollable specimen sheet. Its comments capture the right invariants:
use real tokens, render real shared primitives, remain presentational and
self-contained, and avoid query/navigation/data dependencies.

There are 27 `app/dev/*.tsx` files in total, but they should not all enter the
design workbench. A filename-based and source-header audit found approximately:

- 14 gallery/specimen/visual-kit routes;
- 6 clear operational or control routes such as force-state, screenshot-mode,
  persona switching, membership transitions, onboarding access, and billing;
  and
- several focused QA screens that need explicit classification.

Beyond the five galleries linked from the hub, the repository contains focused
visual work for chat artifacts, experience anatomy, crowns, proposal receipts,
trip creation, photo intake, profiles, stay kits, native Markdown, and other
product families. Some should be indexed; operational bridges should remain in
a separate QA/dev-tools section. "Put all 27 in one scroll" would make the
workbench less coherent, not more.

### 3.2 Existing component inventory

[`docs/component-registry.json`](../../travel-app/docs/component-registry.json)
currently registers 89 components:

| Lifecycle status | Count |
| --- | ---: |
| Stable | 62 |
| Provisional | 24 |
| Internal | 3 |

The design-system hub already reads this registry to show lifecycle counts by
category. The repository also has generated component-catalog and lifecycle
checks. That is a much stronger starting point than a hand-maintained showcase.

However, the registry is not currently green on the checked-out clean
`feat/receipt-wave2` branch. Read-only runs of
`npm run components:catalog:check` and `components:catalog:test` fail because:

- the `LedgerRow` record still points at `components/ui/LedgerRow.tsx` while the
  source now lives under `components/ui/rows/`; and
- 20 current `components/ui` source files are unregistered, including new root
  voice/chrome, motion, row, and state modules.

The generated `docs/Components.md` is also stale relative to the registry. This
may be normal in-flight work on the feature branch, but it means the headline
"89 components" is a nominal snapshot, not a complete current inventory. Phase
0 must restore the catalog checks or explicitly reclassify the omitted modules
before the registry can anchor workbench discovery.

The generator also makes an important boundary explicit: the registry is
intentionally limited to shared `components/ui` modules. Feature components
remain owned by their feature directories. A specimen system spanning headers,
chat artifacts, receipts, stays, and home surfaces therefore should **join to**
this registry where applicable, not expand it into a universal executable
catalog.

### 3.3 Existing visual-evaluation substrate

The mobile package already exposes scripts for:

- PR, nightly, Android, live, baseline, stability, and polish Maestro lanes;
- deterministic surface and polish scenarios;
- accepted-baseline artifact checks;
- typography, composer, receipt, narrow-layout, and accessibility captures;
- animation checks;
- perceptual hashes;
- structured visual-verdict scaffolding and validation;
- design-reference health and comparison sheets; and
- design-alignment, invariant, staleness, and production-evidence checks.

The current checkout contains 12 Maestro baseline flows and 25
`assertScreenshot` commands. This is not merely planned infrastructure; native
visual regression is already active on selected surfaces and components.

This changes the build-versus-buy calculation. Storybook, Loki, or another
service would not arrive in an empty repo. It would overlap with a substantial
native system and would need a clear incremental job.

### 3.4 Existing documented intent

[`docs/design-consolidation/Plan.md`](../../travel-app/docs/design-consolidation/Plan.md)
already describes `app/dev/gallery.tsx` as the **living catalog** and asks that
it grow. Conversely,
[`docs/Frontend Engineering Loop.md`](../../travel-app/docs/Frontend%20Engineering%20Loop.md)
says the Storybook lane should come later because the then-current bottleneck
was whole-surface closure against dogfood state.

Both can remain true:

- consolidate the already-built native catalog now because it is a small
  extension of current infrastructure; and
- defer a second framework until it solves a measured problem the native
  catalog does not.

### 3.5 Dev-route protection needs verification

The source comments state that dev routes are gated by
`__DEV__ || IS_INTERNAL_BUILD`, and the root layout conditionally renders 20
`<Stack.Screen name="dev/..." />` declarations. Seven other files under
`app/dev` are not explicitly listed there.

This is not sufficient evidence of exclusion. Expo Router documents that files
inside `app` automatically become routes, that screens do not need explicit
`Stack.Screen` declarations, and that all routes are included by default unless
protected. See [Expo Router navigation layouts](https://docs.expo.dev/router/basics/navigation-layouts/)
and [protected routes](https://docs.expo.dev/router/advanced/protected/).

This does not prove an exploitable production route without building and
deep-linking the external binary, but it invalidates the assumption that a
conditional `Stack.Screen` alone is a production leak guard. Before expanding
the native gallery, verify one of these stronger boundaries:

- development tooling is removed from the external bundle by build-time route
  generation or entry-point separation;
- the entire `dev` group is inside a `Stack.Protected` guard and every dev screen
  also fails closed when opened directly; or
- gallery code moves outside the production `app` route tree.

Storybook's recommended entry-point swapping is attractive partly because it
provides a clean standalone workbench entry and zero Storybook code in the
normal bundle.

## 4. What the industry patterns say

The strongest pattern across current tools is not a specific vendor. It is a
separation of concerns:

1. production UI remains the source of truth;
2. previews provide named, deterministic inputs;
3. the catalog makes those previews discoverable;
4. a selected subset becomes screenshot tests;
5. journeys prove navigation and integrated state; and
6. humans still approve meaning and taste.

### 4.1 Native preview systems validate state matrices

Apple's current Xcode preview system supports named, parameterized previews and
variants for devices, orientation, color scheme, and Dynamic Type. The point is
not merely to render one happy-path component; it is to make configuration
changes visible side by side. See [Apple's Xcode preview documentation](https://developer.apple.com/documentation/xcode/previewing-your-apps-interface-in-xcode).

Android's Compose previews similarly support device, locale, UI mode, and font
scale variants. Its screenshot-testing tool converts selected previews—not
every preview—into approved reference images with an actual/reference/diff
report. The tool remains experimental in 2026, but the architecture is useful:
catalog broadly, snapshot selectively. See [Compose Preview Screenshot Testing](https://developer.android.com/studio/preview/compose-screenshot-testing).

Airbnb's [Showkase](https://github.com/airbnb/Showkase) demonstrates the same
idea at design-system scale for Jetpack Compose: annotation-driven discovery,
search, grouped components and tokens, and generated permutations such as dark
mode, RTL, and font scaling. Its relevance to Vesper is conceptual rather than
technical: metadata should generate the browser and state matrix, rather than a
developer maintaining both manually.

### 4.2 React Native Storybook is substantially better in 2026

React Native Storybook v10 supports Expo and Expo Router, native rendering,
Component Story Format, controls, actions, notes, backgrounds, deep links, and
portable stories. Version 10.4 recommends **entry-point swapping**: when
`STORYBOOK_ENABLED=true`, Storybook replaces the app entry point, and Storybook
code does not ship in the normal bundle. Embedding it as an Expo Router route is
supported but not recommended. See the [React Native Storybook setup guide](https://storybookjs.github.io/react-native/docs/intro/getting-started/).

Its useful ideas map cleanly to the proposed workbench:

- colocated stories capture named rendered states;
- arguments are structured component inputs;
- decorators provide safe-area, theme, provider, or layout harnesses;
- deep links identify one stable specimen; and
- portable stories can be reused in tests.

However, native Storybook still has less isolation and a smaller addon ecosystem
than web Storybook because it renders inside a native runtime rather than an
iframe. Its documentation also states that there is currently no built-in
React Native visual-testing path; it recommends using Maestro, Detox, or an
external visual service against story deep links. See the [native comparison](https://storybookjs.github.io/react-native/docs/intro/)
and [native testing guidance](https://storybookjs.github.io/react-native/docs/intro/testing/).

That is important: adopting Storybook would organize specimens, but it would
not replace the current Maestro/device evidence loop.

The ecosystem is no longer obviously niche. As of this research pass, npm lists
`@storybook/react-native` 10.5.4 as current with roughly 707,000 weekly
downloads. That is strong enough to justify a real spike, not a theoretical
dismissal. See the [npm package](https://www.npmjs.com/package/@storybook/react-native).

It is still not a zero-risk install in this exact app. The 10.5.4 package
declares exact peers for `react-native-reanimated` 4.5.1 and
`react-native-safe-area-context` 5.8.0, while the app currently uses Reanimated
4.5.3 and safe-area-context 5.6.x. Version 10.4.4 used broader peer ranges. The
spike must test dependency resolution and native rendering without changing
production dependency versions merely to satisfy the workbench.

### 4.3 The most interesting incremental benefit is agent context

Storybook 10.3 introduced an MCP server for React that gives coding agents
component metadata, documentation, stories, previews, and focused test tools.
The stated goal is directly relevant to our failure mode: agents should reuse
real components instead of inventing plausible but inconsistent new ones. See
[Storybook MCP for React](https://storybook.js.org/blog/storybook-mcp-for-react/).

Storybook 10.4 added agent-assisted setup and richer experimental React
component metadata, while React Native Storybook added agent skills and an
experimental MCP endpoint. See [Storybook 10.4](https://storybook.js.org/blog/storybook-10-4/)
and the [React Native configuration docs](https://storybookjs.github.io/react-native/docs/intro/configuration/).

The caveat is material: Storybook's manifest and general MCP documentation says
the capability is in preview and React-only, while React Native Storybook has a
separate explicitly **experimental** MCP endpoint. The native endpoint can
expose documentation/query tools and, with WebSockets, select stories on a
device. We should not assume the full React web agent workflow—including
docgen, manifests, test tooling, and live previews—is equally reliable for the
React Native renderer. See the [native MCP configuration](https://storybookjs.github.io/react-native/docs/intro/configuration/mcp-configuration/)
and [Storybook manifests](https://storybook.js.org/docs/ai/manifests).

The underlying principle does not require Storybook, however. A filtered JSON
or generated Markdown specimen manifest can immediately tell Codex:

- which production component exists;
- its maturity and intended use;
- its canonical states and fixture IDs;
- the galleries and screens where it appears;
- the design reference and screenshot evidence; and
- which similar-looking component is retired or prohibited.

This remains the highest-potential agent-facing part of the proposal, but the
new conclusion is to test Storybook's generated context before hand-building a
parallel manifest.

### 4.4 Hosted native visual testing is promising but still moving

Chromatic announced React Native visual testing as a **sneak peek** on May 13,
2026. It promises hosted iOS and Android simulators, parallel runs,
stabilization, baseline diffs, PR checks, and collaborative approval on top of
React Native Storybook. See [Chromatic's announcement](https://www.chromatic.com/blog/react-native-visual-testing-sneak-peek/).

That is directionally attractive because it outsources simulator stability and
adds a mature review UI, but "sneak peek" is not the right maturity level for a
foundational migration. It should be monitored or piloted later.

[Sherlo](https://sherlo.io/) currently offers cloud React Native Storybook
screenshots and collaborative review. It is listed by React Native Storybook as
an external visual-testing option. It may be worth evaluating if hosted device
maintenance or reviewer collaboration becomes the bottleneck, but its benefits
should be verified against this app rather than accepted from vendor claims.

[Loki](https://github.com/oblador/loki) can run Storybook visual regression on
Chrome, iOS simulators, and Android emulators with explicit reference approval.
It is credible, but it would leave Vesper responsible for the same native
environment stabilization and review plumbing already handled by the current
Maestro/polish substrate. It is not an obvious near-term upgrade.

BrowserStack's App Percy now has direct official integrations for both
[React Native Storybook](https://www.browserstack.com/docs/app-percy/integrate/storybook-react-native)
and [Maestro mobile flows](https://www.browserstack.com/docs/app-percy/integrate/maestro).
This is stronger counterevidence than the first pass captured:

- Storybook stories can be discovered and captured locally or on real
  BrowserStack devices;
- Maestro flows can upload visual checkpoints without abandoning the current
  journey runner; and
- App Percy supplies baseline management, PR review, ignore/consider regions,
  collaboration, and a device grid.

The integration cost remains meaningful. The Storybook path adds Appium and a
Storybook-enabled native build; cloud iOS requires a distribution-signed IPA.
The self-hosted Maestro SDK and CLI versions documented by BrowserStack are
currently beta. App Percy also cannot pause animations automatically and asks
teams to stabilize or ignore dynamic regions. It is therefore a credible
future review layer, not a prerequisite for the workbench.

### 4.5 Maestro itself has moved forward

Maestro 2.x now includes [`assertScreenshot`](https://docs.maestro.dev/reference/commands-available/assertscreenshot),
which compares the current view or a selected crop to a reference image with a
configurable match percentage. The app already uses it. This removes the need
to select a new open-source diff runner merely to obtain baseline assertions.

Maestro also offers experimental [`assertNoDefectsWithAI`](https://docs.maestro.dev/api-reference/commands/assertnodefectswithai)
and [`assertWithAI`](https://docs.maestro.dev/api-reference/commands/assertwithai)
commands plus an AI analysis report. These can inspect screenshots for cutoff,
overlap, centering, spelling, or a natural-language condition. They are
processed through Maestro Cloud, require authentication, and default to
optional because responses remain experimental. See [Maestro AI test analysis](https://docs.maestro.dev/maestro-flows/workspace-management/ai-test-analysis).

Their appropriate role is advisory smoke detection. They do not have Vesper's
accepted design reference, product hierarchy, or founder taste, and should not
be allowed to transform "no generic defect detected" into "product-quality
pass."

### 4.6 A native gallery is not inherently an anti-pattern

React Native itself still uses RNTester as a native component/example and
integration-test application. Its contributor documentation describes native
snapshot tests that render components and compare them with reference images,
while warning that OS/architecture differences require a controlled
configuration and mocked network dependencies. See [React Native's testing
guide](https://reactnative.dev/contributing/how-to-run-and-write-tests).

Microsoft similarly maintains a React Native Gallery as a proving ground and
showcase for native and JavaScript components. See the [React Native Windows
Gallery description](https://microsoft.github.io/react-native-windows/blog/2021/03/16/64updates).

These examples validate retaining native composition and integration galleries.
They do not justify recreating Storybook's isolated-story discovery, tagging,
and agent metadata. The dividing line is responsibility, not ideology:

- native gallery for platform behavior, surface composition, and app-context
  harnesses;
- Storybook candidate for isolated component states, discoverability, and
  portable metadata.

## 5. The role of mock data

The design workbench should use mock data, but "mock" should not mean fake
components, toy markup, or an alternate UI implementation.

### 5.1 What should be real

- the production React Native component;
- typography, spacing, color, material, and motion tokens;
- production formatting and layout logic;
- production icon and media-fallback behavior;
- the real provider wrapper when a provider affects rendering; and
- production accessibility labels and semantics.

### 5.2 What should be deterministic

- component props and view models;
- clocks, dates, time zones, currencies, and locale;
- names, trip titles, location labels, and body copy;
- image identities and dimensions;
- request results, delays, and errors when a component owns async display; and
- experiment flags and platform traits.

Storybook's current guidance uses arguments for inputs, decorators for rendering
contexts, and request mocks for success and failure cases. The transferable
lesson is that fixtures should sit at the component boundary and stay
repeatable. See [Storybook decorators](https://storybook.js.org/docs/writing-stories/decorators)
and [network request mocking](https://storybook.js.org/docs/writing-stories/mocking-data-and-modules/mocking-network-requests).

### 5.3 What should not enter this lane

- a live cloud database;
- mutable shared test accounts;
- production APIs;
- random fixture generators without fixed seeds;
- remote image URLs with uncontrolled crops or availability;
- background agent responses that can change wording or timing; or
- a second implementation built only to resemble the production component.

The workbench's job is reproducible visual inspection. Local integration and
cloud dogfood remain necessary elsewhere to prove wiring and real behavior.

## 6. Recommended hybrid Vesper workbench

### 6.1 Four lenses, at most two hosts

The system should expose four coherent lenses. They do not all need to live in
one renderer:

- **If the Storybook spike passes:** isolated foundations/components/patterns
  live in Storybook; native surface compositions and operational QA bridges
  remain under the app's protected development lane.
- **If the spike fails:** the protected native `/dev/design-system` hub hosts
  all four lenses using a thin generated index.

The user experience may still offer one developer entry point linking both
hosts. The architectural objective is single ownership per specimen, not a
single enormous scroll.

#### A. Foundations

- typography roles and font-loading evidence;
- semantic color and material roles;
- spacing, radius, border, elevation, and safe-area primitives;
- icons, imagery, gradients, and media fallbacks; and
- motion primitives with a static capture state.

#### B. Components and patterns

- headers and navigation chrome;
- buttons, chips, filters, segments, and passive status;
- composer states;
- cards, receipts, decks, and artifacts;
- rows, lists, sheets, notices, and empty/error/loading states; and
- cross-surface primitives used by Trips, Vesper, and Places.

#### C. Canonical compositions

These are not full journeys. They are deterministic surface slices that expose
how components compose:

- Trips home first viewport and representative trip states;
- Vesper conversation start, streaming, artifact, proposal, and return states;
- Places empty, saved, dense, and decision-support states; and
- onboarding's first-value path.

This lens prevents the classic failure where every component looks acceptable
alone but the product still feels like a pile of components.

#### D. Stress matrix

The useful matrix is small and risk-driven, not combinatorial:

- short, representative, and extreme content;
- empty, loading, partial, error, stale, disabled, selected, and streaming;
- narrow phone width and the canonical phone width;
- default and large accessibility text;
- missing or awkward media; and
- iOS/Android only where platform rendering materially differs.

Long multilingual strings, RTL, landscape, tablet, dark mode, and every Dynamic
Type size should be added when product scope or observed defects justify them,
not because the matrix can theoretically grow forever.

### 6.2 One stable identity, not one universal registry

The second pass rejects the idea of designing a large custom specimen registry
up front.

Keep the existing authorities separate:

- `component-registry.json` owns shared `components/ui` lifecycle, imports,
  ownership, and retirement;
- Storybook CSF owns isolated component stories if the spike passes;
- a small native route index owns composition galleries and QA bridges; and
- the existing polish surface registry owns whole-surface capture contracts.

Join them with stable IDs and optional references. Do not duplicate their full
schemas. A minimal native route record might be:

```ts
type NativeGalleryEntry = {
  id: string;
  title: string;
  kind: 'foundation' | 'composition' | 'qa-bridge' | 'sandbox';
  route: string;
  tags: string[];
  componentIds?: string[];
  surfaceId?: string;
  storyIds?: string[];
  captureTier?: 'blocking' | 'advisory' | 'none';
};
```

If Storybook passes, its existing tags can express stable/provisional,
component/pattern, owner, and capture eligibility; its story index supplies
discovery and deep links; and its preview manifests may supply agent context.
Only add a custom field when neither Storybook nor the existing repository
registries can express a real need.

Across the two hosts, stable identity should drive:

- navigation and filters;
- stable deep links;
- screenshot filenames and capture manifests;
- Maestro specimen flows;
- joins to component lifecycle and surface evidence;
- agent-readable component discovery;
- accepted/provisional/exploration labels.

No index record should duplicate JSX or fixture payloads. It points to a real
production render and deterministic fixture owned beside the component or
feature.

### 6.3 Named states before arbitrary knobs

Controls are useful for exploration, but acceptance should center on named,
product-relevant states:

- `default`;
- `long-title`;
- `missing-image`;
- `loading`;
- `error-retryable`;
- `selected`;
- `streaming`; and
- `large-text`.

Named states communicate intent and remain stable in screenshots. Arbitrary
prop knobs can hide invalid combinations and make visual evidence impossible to
reproduce.

### 6.4 Browse mode and capture mode

Each gallery family should be reachable in two forms:

```text
/dev/design-system?section=receipts
/dev/design-system/specimen?id=proposal-receipt--accepted-long-copy
```

The exact route is an implementation detail. The contract is not:

- browse mode may include labels, notes, grouped states, and scrolling;
- capture mode renders one specimen with fixed chrome and dimensions;
- the specimen ID is stable across local runs and CI;
- missing fixture or component IDs fail loudly; and
- the capture route can render without mutable cloud state.

## 7. How this fits with Maestro and visual evaluation

The workbench does not replace Maestro. It gives Maestro a cheaper and more
deterministic target.

| Layer | Question answered | Recommended instrument |
| --- | --- | --- |
| Static/type checks | Is the specimen registered and valid? | TypeScript and registry validation |
| Isolated rendering | Can this production UI render each named state? | Native workbench |
| Visual change | Did accepted pixels/structure change? | Selected screenshots and diff/hash |
| Visual quality | Is hierarchy, rhythm, fit, and product feel good? | Calibrated vision critique plus human review |
| Integrated surface | Do components compose in the right app state? | Canonical surface specimen and surface capture |
| User journey | Can the user traverse and mutate real product state? | Maestro against local integration/dogfood |

Maestro can open a specimen deep link, wait for a stable test ID, hide or freeze
known animation, capture the screen, and record the specimen ID. The same tool
can separately execute Trips/Vesper/Places journeys. These results must not be
collapsed into one `passed` label.

### 7.1 Do not baseline every specimen

Use three evidence tiers:

| Tier | Purpose | Suggested initial size | Gate |
| --- | --- | ---: | --- |
| A: canonical | High-value product signatures and first-value compositions | 15–25 | Blocking after baseline approval |
| B: stress | Long copy, narrow width, large text, missing media, key error states | 20–40 | Advisory until stable |
| C: exploration | Knobs, alternatives, provisional experiments | Unbounded but pruned | No baseline |

The exact counts are adjustable. The important constraint is that screenshot
maintenance grows with environment permutations, not merely with the number of
components.

### 7.2 AI critique should be structured and skeptical

An AI reviewer should receive:

- current isolated or surface screenshot;
- accepted reference when one exists;
- product intent and the component/surface contract;
- device, font-scale, fixture, and specimen metadata;
- a rubric for hierarchy, typography, spacing, component fit, native integrity,
  and product character; and
- founder-labeled examples of blocker, major, minor, and acceptable variance.

It should return localized findings with severity and confidence, not a general
"looks good." Visual diffs detect change; they do not establish taste. AI review
increases coverage, but final baseline approval remains a calibrated human act.

## 8. Failure modes and efficient countermeasures

| Failure mode | Why it happens | Efficient countermeasure |
| --- | --- | --- |
| Gallery drifts from production | Showcase-specific JSX is easier than extracting the real component. | Gallery may compose only real production components and tokens; registry check requires a production owner. |
| Mock data is too flattering | Designers choose short names, perfect photos, and fully loaded states. | Every Tier A family gets representative plus one extreme fixture; observed production failures become fixtures. |
| Every possible combination explodes | Width × platform × text size × state × theme grows multiplicatively. | Risk-tier the matrix; add a dimension only when scope or defect history justifies it. |
| One giant scroll becomes slow and unreadable | All components, images, animations, and states mount at once. | Categorize, lazy-render sections, and keep a separate one-specimen capture route. |
| Snapshot churn destroys trust | Fonts, clocks, remote media, animations, and OS changes create noise. | Pin device/runtime, bundle media, freeze time, settle motion, record metadata, and approve baseline updates explicitly. |
| A green diff means "beautiful" | Snapshot tools only know whether the image changed. | Separate visual integrity from product-quality verdict; use a rubric, independent critique, and human calibration. |
| Components pass but screens feel incoherent | Isolation hides density, rhythm, and hierarchy between components. | Include canonical first-viewport and surface compositions in Tier A. |
| Journeys are too slow for local iteration | Reaching a deep state repeatedly wastes time and adds network variance. | Use the workbench for component/surface iteration; reserve journeys for connectivity and mutation claims. |
| Catalog becomes another source of truth | Routes, fixtures, docs, and screenshots are hand-maintained separately. | Keep lifecycle, stories, native compositions, and surface contracts in their existing authorities; join with IDs and generate derived indexes. |
| Agent sees too much context | Dumping all 89 components and every state wastes tokens and lowers relevance. | Query/filter the manifest by family, status, surface, and tags; show stable options first. |
| Agent invents a near-duplicate anyway | Existence alone does not communicate the approved choice. | Include preferred uses, prohibited substitutes, status, and real consumer examples; add duplicate review to frontend receipt. |
| Dev tooling enters production | File-based routes are assumed absent because their `Stack.Screen` declaration is conditional. | Audit an external build and deep links; use `Stack.Protected`/fail-closed guards or move the workbench out of the production route tree. Use Storybook entry-point swapping for the isolated lane. |
| Dual Storybook/native fixtures diverge | A migration adds `.stories` without retiring or generating the old catalog. | Pilot from the same fixture model; do not maintain two independent state definitions. |
| Hosted visual vendor becomes infrastructure before proving value | Review UI is attractive, so switching costs are ignored. | Time-box against concrete metrics: setup hours, capture time, flake, reviewer time, and defects caught. |

## 9. Storybook decision

### 9.1 What Storybook would add

- a widely understood Component Story Format;
- automatic story discovery and browsing;
- mature args, decorators, documentation, and controls concepts;
- stable story deep links;
- portable stories;
- a growing React Native setup path; and
- potentially valuable MCP/agent metadata and collaboration workflows.

### 9.2 What it would not solve by itself

- native visual polish judgment;
- full-screen product coherence;
- actual user journeys and backend mutations;
- accepted Vesper design intent;
- deterministic devices and fonts;
- React Native screenshot baselines without Maestro/Detox/external service; or
- fixture quality.

### 9.3 Current recommendation

**Do not migrate wholesale. Spike it now, before building its substitutes.**

First classify and protect the existing native routes. Then pilot Storybook with
3–5 stable components that already have clean fixtures and high reuse: one leaf
control, one provider-wrapped pattern, one feature component, and one
composition-like component. Do this before implementing a custom manifest,
search UI, or generated story index.

The pilot should use the recommended standalone entry-point swap and answer:

1. Can 10.4.x or 10.5.x install without forcing unsafe production dependency
   changes?
2. Do the real Vesper fonts, safe areas, Reanimated components, images,
   gestures, sheets, and providers render correctly?
3. Can Codex query native stories and component intent through the experimental
   MCP endpoint, with acceptable metadata quality and token use?
4. Can current Maestro open story deep links and capture them with no more flake
   than equivalent native routes?
5. Does one fixture definition serve Storybook, Jest where useful, and native
   capture rather than creating a duplicate mock layer?
6. Does entry-point swapping keep Storybook absent from the production bundle?
7. Is the review experience materially better than a generated native index?

If the renderer, dependency, and deep-link checks pass but MCP does not, use
Storybook for humans and expose a thin generated manifest later. If the native
renderer itself is brittle, stop the spike and keep the native catalog. Do not
let the allure of agent tooling override incorrect native rendering.

### 9.4 Revised ownership decision

| Surface | Default owner after a successful spike | Why |
| --- | --- | --- |
| Shared leaf components | Storybook story beside component | Standard discovery, args, tags, portable states |
| Reusable feature patterns | Storybook when provider harness stays small | Agent context and isolated stress states |
| Foundation/token scroll | Native gallery initially; migrate only if Storybook improves it | Already data-driven from real tokens |
| Trips/Vesper/Places compositions | Protected native gallery | Needs native layout, app-level composition, and product gestalt |
| Forced state and membership transitions | Native QA bridge | They mutate or route app context; not component stories |
| Full journeys | Maestro against app | Proves connectivity and user loop |
| Selected visual baselines | Maestro `assertScreenshot` | Already installed and in use |
| Generic AI defect smoke | Maestro AI, advisory | Experimental and not design-aware |
| Product-quality acceptance | Structured independent review plus founder calibration | Requires intent and taste |

## 10. Minimal implementation direction

This should be a consolidation project measured in small slices, not a new
platform initiative.

### Phase 0 — inventory, classification, and route safety

**Goal:** know what already exists before adding abstractions.

- enumerate all `app/dev` routes and their rendered production components;
- join them to the 89-component registry where possible;
- label each route as foundation, component, pattern, surface, sandbox, or
  obsolete;
- identify duplicates and screens that render hand-built showcase copies;
- verify external-build bundling and direct deep-link behavior for `app/dev`;
- establish a fail-closed route boundary before expanding the native lane;
- keep the shared component registry, surface registry, and fixture ownership
  boundaries explicit; and
- select the first 15–25 Tier A specimens from the Trips/Vesper/Places core
  loops and product signatures.

**Exit:** one reviewed inventory and no ambiguity about source of truth.

### Phase 0.5 — Storybook technical spike

**Goal:** learn whether the standard tool removes enough custom work to justify
its dependency and runtime cost.

- test 3–5 representative components using shared deterministic fixtures;
- prefer 10.5.x, but compare 10.4.4 if exact peer dependencies conflict;
- use entry-point swapping rather than an Expo Router story route;
- exercise real fonts, images, Reanimated, gestures, sheets, and providers;
- connect the experimental native MCP endpoint to Codex and inspect actual
  responses;
- open stories by deep link and capture through Maestro; and
- record setup time, dependency changes, render failures, capture time, and
  agent usefulness.

**Exit:** explicit adopt-for-isolated-stories or reject-for-now decision. Delete
the spike if it fails; do not leave a third half-owned lane.

### Phase 1 — coherent ownership and entry points

**Goal:** make existing work discoverable to people and agents.

- if Storybook passes, add isolated stories incrementally and use its hierarchy,
  tags, story index, and deep links rather than rebuilding them;
- keep native foundations/compositions/QA bridges in a small classified route
  index;
- if Storybook fails, replace the five-item hard-coded native list with that
  generated index and add only the minimum filtering needed;
- generate custom agent Markdown/JSON only if measured MCP/index output is
  insufficient;
- validate stable IDs, dead routes, stale component joins, and duplicate fixture
  ownership; and
- enforce the verified external-build boundary.

**Exit:** a human or Codex can find the preferred component/state without
knowing a filename.

### Phase 2 — stable specimen deep links and captures

**Goal:** create the fast visual loop.

- add one-specimen rendering with stable IDs;
- normalize deterministic fixtures, time, images, and static motion states;
- generate a Maestro capture manifest for Tier A;
- record screenshot metadata and enforce explicit baseline approval; and
- keep Tier B advisory until its environment is stable.

**Exit:** one command can render and capture the canonical set without walking
full app journeys.

### Phase 3 — compositions and calibrated review

**Goal:** catch the "components are fine, product still looks wrong" class.

- add first-viewport/canonical compositions for Trips, Vesper, Places, and
  onboarding;
- add the smallest high-risk stress matrix;
- run deterministic health checks before AI review;
- calibrate AI severity against founder-labeled examples; and
- keep surface and journey evidence distinct in reports.

**Exit:** visual findings are localized, reproducible, and harder to pass
leniently.

### Phase 4 — optional hosted review pilot

**Goal:** test whether outsourced devices and collaborative review solve a
measured bottleneck.

- trial App Percy through the existing Maestro lane first if journey/surface
  review is the bottleneck;
- trial App Percy Storybook, Chromatic early access, or Sherlo only if isolated
  story review is the bottleneck;
- keep the lane non-blocking until its flake and baseline workflow are trusted;
  and
- compare cost, signing/build complexity, capture latency, review latency, and
  defects caught with the local path.

**Exit:** adopt, defer, or reject based on evidence, and remove the losing
duplicate path.

## 11. What not to build yet

- a custom drag-and-drop design editor;
- a general-purpose replacement for Figma or Claude Design;
- a bespoke MCP server before the static manifest proves insufficient;
- automatic screenshots for all 89 components and every permutation;
- a cloud fixture service;
- a second set of gallery-only primitives;
- an elaborate visual-quality scalar score;
- cross-platform parity for states the product does not support; or
- a Storybook/Chromatic migration framed as modernization rather than a measured
  response to a bottleneck.

## 12. Success metrics and decision gates

Track a few operational measures for four weeks:

- percentage of stable components with at least one discoverable real specimen;
- percentage of Tier A specimens reachable by stable deep link;
- time from component edit to comparable screenshot;
- capture flake/noise rate;
- number of duplicate or near-duplicate components added;
- number of visual defects caught in workbench versus full journey versus human
  dogfood;
- median human review time for a frontend change;
- number of stale specimens or broken component joins; and
- whether coding agents cite/reuse registered components in their frontend task
  receipts.

The direction is working if it shortens the visual feedback loop, catches issues
before manual journey dogfood, and increases reuse without creating a large
maintenance stream.

## 13. Proposed durable rules

If the pilot succeeds, promote these rules:

1. Every broadly reusable production component has a lifecycle registry entry.
2. Every Tier A product signature has a named deterministic specimen.
3. Galleries render production components and tokens, never visual copies.
4. One specimen ID joins route, fixture, screenshot, component, and design
   evidence.
5. Browse mode is for system coherence; capture mode is for deterministic
   evaluation.
6. Catalog broadly, baseline selectively.
7. Component evidence, surface evidence, and journey evidence make different
   claims and report separately.
8. A visual change detector cannot award product-quality acceptance.
9. Agent manifests prioritize stable components and communicate intended use,
   not just props.
10. New frameworks or hosted services enter only through a bounded comparison
    against the current native lane.
11. File-based dev routes require a verified fail-closed external-build
    boundary; conditional screen configuration is not treated as exclusion.

## 14. Final direction

The design scroll is not a side project. Properly scoped, it is the missing
middle of the frontend loop:

```text
Claude Design / accepted intent
              ↓
     deterministic production fixtures
          ↙                         ↘
Storybook isolated states     native compositions
     (if spike passes)         and QA bridges
          ↘                         ↙
         Maestro native capture / assertions
              ↓
calibrated product-quality review
              ↓
local integration and cloud dogfood journeys
```

Today, the app jumps too easily from design artifact or code change to a full
device journey, while its many existing galleries remain fragmented. Closing
that gap should make visual iteration faster, give agents better component
context, and make it much harder for a technically passing screen to masquerade
as a polished one.

The highest-ROI next action is therefore **Phase 0 plus the Phase 0.5 spike**:

1. classify the 27 `app/dev` files and separate about 14 visual galleries from
   operational QA routes;
2. verify that external builds cannot directly open dev routes;
3. choose the first 15–25 Tier A visual specimens from the core product loops;
   and
4. test Storybook on only 3–5 representative components, including native
   rendering, dependency compatibility, Maestro deep-link capture, and Codex
   MCP usefulness.

Only then choose the Phase 1 implementation. This prevents two opposite kinds
of premature engineering: a custom catalog that recreates Storybook, or a
Storybook migration that duplicates a strong native surface/evaluation system.

## Sources reviewed

Primary and official sources were preferred:

- [React Native Storybook introduction and native/web comparison](https://storybookjs.github.io/react-native/docs/intro/)
- [React Native Storybook v10 setup and Expo entry-point swapping](https://storybookjs.github.io/react-native/docs/intro/getting-started/)
- [React Native Storybook stories and CSF](https://storybookjs.github.io/react-native/docs/intro/writing-stories/)
- [React Native Storybook testing and Maestro guidance](https://storybookjs.github.io/react-native/docs/intro/testing/)
- [React Native Storybook development workflows and story deep links](https://storybookjs.github.io/react-native/docs/intro/development-workflows/)
- [React Native Storybook experimental MCP configuration](https://storybookjs.github.io/react-native/docs/intro/configuration/mcp-configuration/)
- [React Native Storybook npm package and current adoption signal](https://www.npmjs.com/package/@storybook/react-native)
- [Storybook MCP for React](https://storybook.js.org/blog/storybook-mcp-for-react/)
- [Storybook AI manifests and lifecycle caveats](https://storybook.js.org/docs/ai/manifests)
- [Storybook tags and filtering](https://storybook.js.org/docs/writing-stories/tags)
- [Storybook 10.4 release](https://storybook.js.org/blog/storybook-10-4/)
- [Storybook decorators](https://storybook.js.org/docs/writing-stories/decorators)
- [Storybook network-request mocking](https://storybook.js.org/docs/writing-stories/mocking-data-and-modules/mocking-network-requests)
- [Chromatic React Native visual-testing sneak peek](https://www.chromatic.com/blog/react-native-visual-testing-sneak-peek/)
- [App Percy integration with React Native Storybook](https://www.browserstack.com/docs/app-percy/integrate/storybook-react-native)
- [App Percy integration with Maestro](https://www.browserstack.com/docs/app-percy/integrate/maestro)
- [App Percy native screenshot stabilization limits](https://www.browserstack.com/docs/app-percy/stabilize-screenshots/ss-native-apps)
- [Maestro screenshot assertions](https://docs.maestro.dev/reference/commands-available/assertscreenshot)
- [Maestro AI test analysis](https://docs.maestro.dev/maestro-flows/workspace-management/ai-test-analysis)
- [Expo Router automatic route inclusion](https://docs.expo.dev/router/basics/navigation-layouts/)
- [Expo Router protected routes](https://docs.expo.dev/router/advanced/protected/)
- [React Native contributor snapshot-testing guidance](https://reactnative.dev/contributing/how-to-run-and-write-tests)
- [Microsoft React Native Gallery](https://microsoft.github.io/react-native-windows/blog/2021/03/16/64updates)
- [Loki](https://github.com/oblador/loki)
- [Sherlo](https://sherlo.io/)
- [Apple Xcode previews](https://developer.apple.com/documentation/xcode/previewing-your-apps-interface-in-xcode)
- [Android Compose Preview Screenshot Testing](https://developer.android.com/studio/preview/compose-screenshot-testing)
- [Airbnb Showkase](https://github.com/airbnb/Showkase)
