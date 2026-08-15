---
doc_type: working
status: active
owner: founder / product / design / frontend
created: 2026-08-15
last_updated: 2026-08-15
last_verified: 2026-08-15
expires: 2026-09-14
why_new: Founder-pain calibration of the August 14 native gallery research. The original memo is a strong architecture map; this note answers whether it is useful for a solo founder who needs to see production components in one place and polish them until they are acceptable for the M1 demo.
promotes_to: a classified native gallery index and a demo-signature scroll if the recommended slice is implemented
supersedes: []
related:
  - native-design-gallery-research-and-direction-2026-08-14.md
  - visual-polish-evaluation-and-design-workflow-2026-08-13.md
  - ../../travel-app/docs/Frontend Engineering Loop.md
  - ../../travel-app/docs/design-consolidation/Plan.md
  - ../release/m1-plan-repair.md
---

# Native gallery, founder pain, and demo polish

> **Working follow-up, not an implementation claim.** Counts and route
> classifications were re-verified against the travel-app checkout on
> 2026-08-15. Durable rules still belong in the frontend contract, not here.

## Direct answer

The August 14 document is **useful as a map and as a set of "do not build"
rules**. It is **not the right execution plan** for the highest founder pain:

> I need to look at the components in code in one place and polish them until
> they are acceptable for a demo.

That pain is already half-solved in the repository and half-hidden by
fragmentation. The missing product is not Storybook, Chromatic, MCP, or a
custom specimen registry. It is a **single native index plus a short
demo-signature scroll** of production components with honest fixtures.

Keep the August 14 architecture. Do not start its Phase 0.5 Storybook spike
until the existing galleries are actually findable.

## 1. Is the August 14 doc useful?

### Yes — keep these conclusions

- The idea of a "design scroll" is right. A long native scroll is how a
  founder notices that six cards have different radii. Isolated stories cannot
  prove Trips, Vesper, and Places feel like one product.
- This is not greenfield. `app/dev` already has 27 routes; about 19 of them
  are visual. The hub currently advertises five.
- Production components + deterministic fixtures, never gallery-only copies.
- Catalog broadly, baseline selectively. Do not screenshot every permutation.
- Visual change detection is not product-quality judgment.
- Do not build a custom Storybook clone (search, tags, manifests, deep-link
  catalog) before testing whether Storybook itself is worth the dependency.
- Conditional `<Stack.Screen>` is not a production leak guard. Expo Router
  still auto-includes files under `app/`.
- Hosted native visual testing is still too early to bet the loop on.

### No — do not execute it as written this week

The memo's highest-ROI next action is:

1. classify 27 routes,
2. verify external-build exclusion,
3. pick 15–25 Tier A specimens,
4. spike Storybook on 3–5 components.

That sequence solves an **engineering-platform** problem. The founder pain is
a **review-surface** problem. A Storybook spike, MCP evaluation, and Maestro
capture-manifest work will delay the thing that actually shortens demo polish:
opening one screen and seeing the visual language.

Industry evidence in 2026 agrees with that split. Storybook pays off for
multi-developer design systems and async review. For a solo founder with a
tight feedback loop, it is usually overhead unless agents are already
inventing duplicate components faster than they can be caught. Vesper has that
agent failure mode later. It does not have it as the demo bottleneck today.

The frontend loop already said this. Phase 5 of
[`docs/Frontend Engineering Loop.md`](../../travel-app/docs/Frontend%20Engineering%20Loop.md)
is explicit: do not start the Storybook lane yet; the bottleneck is closing
whole surfaces against dogfood state.

## 2. What the founder pain actually is

There are two jobs that the August 14 memo correctly separated, then buried
under a four-phase platform plan.

| Job | Question | Tool |
| --- | --- | --- |
| **A. Founder taste, demo week** | Do these production pieces look like one product, and are the demo-visible states acceptable? | One native hub + a short scroll of named demo signatures |
| **B. Engineering / agents / CI** | Can a component state be discovered, deep-linked, captured, and reused without inventing a duplicate? | Stories or a generated index, later |

Job A is the pain. Job B is real, but it is not what makes a demo look
unfinished tonight.

"Look at **all** the components" is also the wrong literal goal. The registry
nominally lists 89 shared `components/ui` modules; `components/ui` currently
has far more source files than that; feature components (chat artifacts,
receipts, stay kit, crowns) live outside the registry. A complete catalog of
every module and state is how a solo founder never ships the demo.

The useful definition of "all" is:

- every **demo-visible family**, in one index;
- each family showing **default, one extreme, and one failure/absence** state;
- production components, not flattering toys;
- enough juxtaposition that rhythm, radius, type, and empty-state voice can
  be judged in a single sitting.

That is 15–25 specimens, not 89 × N permutations.

## 3. Verified current state (2026-08-15)

The August 14 snapshot is still directionally right. A few counts moved.

| Claim | 2026-08-14 | 2026-08-15 verification |
| --- | --- | --- |
| `app/dev/*.tsx` files | 27 | **27, unchanged** |
| Hub-linked galleries | 5 | **5, unchanged** — state, header, control, composer, deck |
| Unlisted in root `Stack.Screen` | 7 | **7, unchanged** (see table below) |
| Component registry | 89 (62/24/3) | **89, same split**; `lastUpdated` still `2026-07-31` |
| Catalog checks | failing | **still failing** — `LedgerRow` path drift plus 20 unregistered `components/ui` files |
| Maestro baseline flows | 12 | **12** |
| `assertScreenshot` commands | 25 | **27** (two more than the memo) |
| Storybook in the app | none | **none** |
| Expo | 55 | **`expo ~55.0.28`** |
| Reanimated / safe-area | 4.5.3 / 5.6.x | **unchanged**; Storybook 10.5.4 still peers `reanimated 4.5.1` and `safe-area-context 5.8.0` |

### 3.1 Route classification

These labels are for the native hub. They are not a new ID series.

**Foundations / tokens**

| Route | In hub | In DevFab | In `Stack.Screen` |
| --- | --- | --- | --- |
| `/dev/gallery` | yes | yes ("State gallery") | yes |
| `/dev/design-system` | — (is the hub) | yes | yes |
| `/dev/native-markdown` | no | no | **no** |

**Product-signature galleries (should be in the hub)**

| Route | Why it matters for demo polish | Hub | DevFab | `Stack.Screen` |
| --- | --- | --- | --- | --- |
| `/dev/header-gallery` | chrome family | yes | yes | yes |
| `/dev/control-gallery` | buttons, chips, status | yes | yes | yes |
| `/dev/composer-gallery` | Vesper input states | yes | yes | yes |
| `/dev/deck-gallery` | decision faces | yes | yes | yes |
| `/dev/chat-artifact-gallery` | Act 1–2 conversation objects | no | no | yes |
| `/dev/proposal-receipt-family` | Act 3 receipt | no | no | **no** |
| `/dev/trip-creation-card` | trip object | no | no | yes |
| `/dev/trip-shape-mood-gallery` | trip shape / mood cards | no | no | yes |
| `/dev/booking-confirmation-card` | booking object | no | no | yes |
| `/dev/stay-kit` | lodging cards and plates | no | no | **no** |
| `/dev/trip-crown-gallery` | trip identity mark | no | yes | yes |
| `/dev/occasion-crown-gallery` | Act 4 later-occasion mark | no | no | **no** |
| `/dev/experience-anatomy-gallery` | shared experience anatomy | no | no | **no** |
| `/dev/profile-system` | people / identity | no | no | yes |
| `/dev/photo-intake-action-states` | media intake | no | no | **no** |
| `/dev/onboarding` | first-value path | no | no | yes |
| `/dev/discover-cold-start` | Places empty | no | no | yes |
| `/dev/interpretation-dossier` | Act 2 explanation | no | no | yes |

**QA / operational bridges (keep out of the design scroll)**

| Route | Kind |
| --- | --- |
| `/dev/force-state` | state injection |
| `/dev/screenshot-mode` | capture chrome killer |
| `/dev/persona-switcher` | persona / time travel |
| `/dev/membership-epoch` | Maestro-only membership transition |
| `/dev/deck-qa` | operational deck harness |
| `/dev/billing-sandbox` | purchases, not visual language |

The founder pain is visible in that table. Chat artifacts, proposal receipts,
stay kit, occasion crowns, trip-shape moods, and experience anatomy already
exist as production specimen screens. None of them appear on the design-system
hub. DevFab adds only trip crowns and billing on top of the five hub galleries
(`screenshot-mode` is mentioned in a comment, not linked). To review the rest,
someone has to know the filename.

### 3.2 Why the registry cannot be the workbench

`docs/component-registry.json` is a lifecycle document for shared
`components/ui`. It is the right owner for "is this primitive stable, and what
is the public import?" It is the wrong owner for "show me the demo."

Re-running `npm run components:catalog:check` on 2026-08-15 still fails:

- `LedgerRow` is registered at `components/ui/LedgerRow.tsx` and now lives at
  `components/ui/rows/LedgerRow.tsx`;
- 20 current `components/ui` files are unregistered, including voice/chrome,
  motion, row, and state modules.

Fixing that catalog is worth doing, but it will not let a founder scroll
receipts or chat artifacts. Those are feature components by design.

## 4. Research around the topic

### 4.1 Native in-app catalogs are the standard for this pain

Apple Xcode Previews, Android Compose previews, Airbnb Showkase, React Native's
own RNTester, and Microsoft's React Native Gallery all share one idea: render
the **real** component with **named** configurations, in the **native**
runtime, and browse them as a catalog.

Showkase is the closest cousin to the founder request. Annotation-driven
discovery, grouped components and tokens, and generated permutations (dark
mode, RTL, font scale). The transferable lesson is not "adopt Showkase." It is
**metadata should generate the browser**. Vesper already has the specimens;
it is missing the generated index.

Compose screenshot testing and Apple previews also agree with August 14's
best rule: catalog broadly, snapshot selectively. That rule is even more
important for a solo founder. Screenshot maintenance grows with environment
permutations, not with how many components exist.

### 4.2 Storybook in 2026 is better, and still the wrong first move here

Current facts:

- `@storybook/react-native` **10.5.4** is current (published 2026-07-27).
- Weekly downloads are still strong (~659k on this pass; the August 14 memo
  saw ~707k — same order of magnitude, not a collapse).
- v10.4+ recommends **entry-point swapping** so Storybook is absent from the
  normal bundle when `STORYBOOK_ENABLED` is unset. That remains the only
  clean way to keep workbench code out of an external binary.
- Native MCP is still **experimental**. It can expose docs/query tools and,
  with WebSockets, select stories on a device. It is not the web Storybook
  agent workflow.
- Native Storybook still has **no built-in visual test path**. Official
  guidance is Maestro, Detox, or an external service against story deep links.
- Peer conflict is unchanged: 10.5.4 wants `react-native-reanimated` **4.5.1**
  and `react-native-safe-area-context` **5.8.0**. This app is on Reanimated
  **4.5.3** and safe-area **~5.6.2**. A spike still cannot "just npm install."
- Chromatic React Native visual testing remains **early access / sneak peek**
  (May 2026 announcement, still not GA on this pass).

Independent 2026 practitioner guidance is blunt: Storybook is a multiplier
when several people maintain a shared library across apps. For one person,
one product, and a page-or-surface review loop, the ROI is often negative.
Vesper is more component-dense than a marketing site, so the answer is not
"never Storybook." The answer is "not before the native index exists."

If agents later keep inventing near-duplicate primitives, that is the measured
bottleneck that would justify the spike. Existence of an experimental MCP
endpoint is not that bottleneck.

### 4.3 Expo route protection is still the real leak question

Expo's protected-route docs (updated May 2026) are explicit:

- files in `app/` become routes;
- `Stack.Protected` creates exceptions for client-side navigation;
- protected routes are **not** a substitute for keeping files out of the
  bundle;
- people who know a URL can still request the corresponding JS.

So August 14 was right to distrust conditional `Stack.Screen`. It was also
right that expanding the gallery without a fail-closed boundary is a product
risk. For a demo-polish slice, the proportionate guard is:

1. wrap the whole `dev` group in `Stack.Protected` with
   `__DEV__ || IS_INTERNAL_BUILD`;
2. make every listed *and currently unlisted* gallery fail closed if opened
   when the guard is false;
3. defer moving galleries out of `app/` or introducing a Storybook entry-point
   swap until an external binary is actually being cut.

Do not block the hub index on a full production-bundle audit. Do not pretend
the current comments already prove exclusion.

### 4.4 Mock data is the other half of polish

The August 14 "what should be real / deterministic / forbidden" split is the
best section in that memo. For demo polish it needs one extra rule:

**Every demo-signature specimen needs an unflattering twin.**

Founders lose trust in galleries that only show short names, perfect photos,
and fully loaded states. The demo will not look like that. The minimum matrix
per family is:

- representative (the demo beat);
- extreme (long title, missing image, dense roster);
- failure or absence (error, empty, stale, unavailable provider).

That is how a gallery becomes a polish instrument instead of a mood board.

## 5. Recalibrated direction

```text
existing production galleries
        ↓
one classified native hub          ← do this now (Job A)
        ↓
demo-signature scroll
(Trips / Vesper / Places / receipt / onboarding)
        ↓
founder sitting, scrolling, fixing
        ↓
selected Maestro captures of those signatures
        ↓
Storybook spike only if isolated discovery
or agent reuse is the measured bottleneck   ← Job B, later
```

This is compatible with August 14's hybrid end-state. It changes the order
so the founder pain is relieved first, and custom catalog infrastructure is
still not built.

### 5.1 What "acceptable for a demo" means

M1 is four acts, not a design-system certification. The gallery should be
able to show, in one sitting, the objects a viewer will actually see:

| Demo act | Gallery families to put on the hub |
| --- | --- |
| Act 1 — rescue | composer, chat artifacts, trip home chrome, trip-shape mood, proposal object |
| Act 2 — judgment | interpretation/dossier, experience anatomy, place/stay cards |
| Act 3 — action | proposal receipt family, booking confirmation, controls, headers |
| Act 4 — later occasion | occasion crown, trip crown, profile/people |

If those families look like one product — type, radius, paper, empty-state
voice, receipt geometry — the demo can be visually acceptable even while
dozens of unused primitives stay provisional.

### 5.2 Smallest implementation that solves the pain

One slice, no new platform:

1. **Classify the 27 routes in a small native index** (the August 14
   `NativeGalleryEntry` shape is fine: `foundation | composition | qa-bridge |
   sandbox`).
2. **Replace the five-item hard-coded hub list** in
   `app/dev/design-system.tsx` with that index, grouped for humans:
   Foundations · Demo signatures · Other compositions · QA tools.
3. **Add the same groups to DevFab**, so the floating button is not a second
   incomplete menu.
4. **Declare the seven unlisted visual routes** in the root stack, inside
   `Stack.Protected`.
5. **Do not merge 19 galleries into one giant mount-everything scroll.** One
   hub plus per-family scrolls is the right browse mode. A later
   `?specimen=` capture route is optional and should wait until a family is
   actually being baselined.
6. **Pick ~20 demo-signature states** and give each an unflattering twin.
   Start from galleries that already exist; do not rewrite them.
7. **Repair the component registry** as a separate hygiene commit (`LedgerRow`
   path + unregistered files). Useful, not blocking for the hub.

Exit: a founder can open DevFab → Design system, scroll the index, and reach
every visual family without knowing a filename.

### 5.3 Explicitly defer

- Storybook install and MCP evaluation
- custom search UI
- generated Maestro catalogs for all specimens
- hosted App Percy / Chromatic / Sherlo
- screenshotting every `components/ui` module
- a second set of gallery-only primitives
- moving the workbench out of `app/` before an external-build audit is
  actually scheduled

## 6. Failure modes specific to solo-founder polish

| Failure | Why it happens here | Countermeasure |
| --- | --- | --- |
| Platform instead of sitting | Research memos make the next action "spike Storybook" | Hub index first; Storybook only after a measured discovery bottleneck |
| Completeness theater | 89 components feels like the real inventory | Demo-signature families, not registry coverage percentage |
| Flattering fixtures | Galleries are easier to love than the demo | Representative + extreme + absence for each family |
| Hunting filenames | Hub and DevFab are partial menus | One generated or checked-in index, two entry points |
| Mixing QA bridges into the scroll | Force-state and billing sit next to type specimens | Separate "QA tools" section, never in the design scroll |
| Green Maestro, unfinished demo | Assertions prove change, not taste | Founder sitting with the scroll is the polish loop; Maestro is the later net |
| Dual catalogs | Adding `.stories` without retiring native specimens | Do not introduce Storybook until a family is ready to move, then move it |

## 7. Decision

| Question | Answer |
| --- | --- |
| Keep the August 14 memo? | **Yes.** It is the architecture map and the "do not overbuild" list. |
| Execute Phase 0.5 Storybook spike now? | **No.** Peer conflicts and experimental MCP do not unlock demo polish. |
| Build a custom specimen platform? | **No.** Index what exists. |
| Is a native composition lane needed? | **Yes, and it already exists.** Make it findable. |
| What is the founder-pain slice? | Classified hub + DevFab + protected unlisted visual routes + demo-signature states with unflattering twins. |
| When does Storybook come back? | When isolated discovery or agent duplication is the measured bottleneck, or when an external bundle must contain zero `app/dev` files. |

The August 14 document was right about the destination. This note is about
not walking the long way there while the demo still requires a filename to
review a receipt.
