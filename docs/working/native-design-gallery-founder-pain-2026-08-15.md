---
doc_type: working
status: active
owner: founder / product / design / frontend
created: 2026-08-15
last_updated: 2026-08-15
last_verified: 2026-08-15
expires: 2026-09-14
why_new: Founder-pain calibration of the August 14 native gallery research, revised after a second-pass check against the original plan. The first version of this note oversold a table of contents as a design scroll and treated Storybook as the enemy. This revision keeps only the first increment that is actually better.
promotes_to: a complete native gallery table of contents, optional M1 signature scroll, and the original hybrid architecture thereafter
supersedes: []
related:
  - native-design-gallery-research-and-direction-2026-08-14.md
  - home-kit-galleries-plan-2026-08-15.md
  - visual-polish-evaluation-and-design-workflow-2026-08-13.md
  - ../../travel-app/docs/Frontend Engineering Loop.md
  - ../../travel-app/docs/design-consolidation/Plan.md
  - ../release/m1-plan-repair.md
  - ../../travel-agent/docs/product/Demo Journey Canon.md
---

# Native gallery, founder pain, and demo polish

> **Working follow-up, not an implementation claim.** Route classifications
> were re-verified against the travel-app checkout on 2026-08-15, then checked
> again against the August 14 memo. Durable rules still belong in the frontend
> contract, not here.

## Direct answer

The August 14 document is the better **architecture**. The first version of
this follow-up was not a better plan. It was Phase 0 of that memo, plus a
menu, plus several classification errors, framed as a replacement.

A plan that is actually better for the founder pain is narrower:

> Finish the existing hub as a complete table of contents of true visual
> galleries, wrap `app/dev` in `Stack.Protected`, and only then — if sitting
> with fourteen separate scrolls is still too slow — add one M1 signature
> scroll that reuses existing fixtures. Do not invent a specimen registry.
> Do not spike Storybook until the next step would be search, deep links, or
> agent discovery.

That is original Phase 0 made immediately usable, with original Phase 3's
composition idea pulled forward only if the menu is not enough. It keeps
original Phase 0.5 (Storybook) as the gate before custom catalog
infrastructure. It does not replace the destination.

## 1. Second-pass check: where the first follow-up lost

The August 14 one-line direction was:

> Protect and classify the existing native composition galleries, then run a
> tiny Storybook spike **before building custom catalog infrastructure**.

The first follow-up treated that as "go spike Storybook instead of letting
the founder sit." That was a misread. Original Phase 0 already *is* classify
and protect. Storybook is Phase 0.5 so that Phase 1 does not rebuild
Storybook's discovery, tags, and deep links by hand.

| Claim in the first follow-up | Verdict |
| --- | --- |
| Original's next action is an engineering-platform bundle that delays sitting | **Overstated.** Classify-and-link is Phase 0. The delay is coupling Phase 0.5 to that first sitting. |
| A `NativeGalleryEntry` index is the smallest fix | **Worse than original.** That typed record (`tags`, `componentIds`, `captureTier`, `storyIds`) is the custom catalog original told us not to build first. Extending the existing `GALLERIES` array is the thin move. |
| Hub + DevFab = "all components in one place" | **False.** That is a better menu. The founder still taps through ~14 screens. Original's browse-versus-capture split is the actual "one place" idea. |
| Map every visual kit onto an M1 act | **Completeness theater.** Demo Journey Canon says do not start with onboarding; alpha-critical objects are trip crown, decision receipt, group room, privacy-safe rationale, live repair, one Places claim. Stay kit, photo intake, profile, and experience anatomy are not the flagship demo. |
| `/dev/onboarding` belongs on the design hub | **Wrong.** It is a redirect into the real onboarding flow, the same kind of QA bridge as `force-state`. |
| `/dev/interpretation-dossier` is a deterministic specimen | **Wrong.** It calls live `useDossier` / `useVenueDetail` hooks. Original gallery rules forbid query dependencies. |
| "Unflattering twins" is a new rule | **Already in original §8.** Representative plus one extreme fixture per Tier A family. |
| Frontend Engineering Loop Phase 5 kills a Storybook spike | **Category error.** Phase 5 says do not polish whole surfaces in Storybook. Original already agreed: native compositions stay native; spike Storybook only for isolated leaf states. |
| Do not block hub expansion on a bundle audit | **Half right.** Adding links to files that already exist does not change the leak surface. Adding new `app/dev` files, or shipping TestFlight, still needs original's fail-closed bar. `Stack.Protected` is the cheap guard for the menu slice. There is no `Stack.Protected` in the root layout today. |

The original is stronger on: not recreating Storybook, isolated specimen
identity, not dumping every route into one scroll, and treating agent
duplication as a real cost if coding agents keep inventing near-copies.

The first follow-up was stronger on only one sequencing point: **do not make
the founder wait for a 3–5 component Storybook/MCP/Maestro-deep-link spike
before the existing galleries are findable.**

## 2. What the founder pain actually requires

"Look at all the components in code in one place and polish them until they
are acceptable for a demo" is not one screen of 89 primitives. It is also
not fourteen disconnected `/dev/*` routes.

It needs two layers, which original §1 already named:

1. **A complete menu** so you do not have to remember filenames.
2. **A browse scroll** of the demo-visible families so rhythm, radius, type,
   and empty-state voice can be judged in one sitting.

Layer 1 is missing (hub still lists 5 of the true galleries). Layer 2 exists
per family and does not exist across families. Original Phase 3 put the
cross-family composition last. For a solo founder polishing M1, that is the
part that is late. Storybook does not provide layer 2 at all — isolated
stories cannot prove Trips, Vesper, and Places feel like one product. Original
said that, and it remains correct.

## 3. Corrected inventory (2026-08-15)

27 files under `app/dev`. They are not 19 galleries. Original's "~14 visual,
rest QA" was closer than the first follow-up's hub-everything table.

**True visual galleries — put these on the hub and DevFab**

Already linked from the hub: `/dev/gallery`, `/dev/header-gallery`,
`/dev/control-gallery`, `/dev/composer-gallery`, `/dev/deck-gallery`.

Missing from the hub, should be linked:

| Route | Why | In DevFab | In `Stack.Screen` |
| --- | --- | --- | --- |
| `/dev/chat-artifact-gallery` | Vesper conversation objects | no | yes |
| `/dev/proposal-receipt-family` | Act 3 decision receipt | no | **no** |
| `/dev/trip-crown-gallery` | alpha-critical trip mark | yes | yes |
| `/dev/trip-shape-mood-gallery` | trip object on home | no | yes |
| `/dev/trip-creation-card` | trip object | no | yes |
| `/dev/booking-confirmation-card` | booking object | no | yes |
| `/dev/stay-kit` | lodging family; supporting, not flagship | no | **no** |
| `/dev/occasion-crown-gallery` | later-occasion mark | no | **no** |
| `/dev/experience-anatomy-gallery` | shared anatomy; not flagship | no | **no** |
| `/dev/profile-system` | people fixtures | no | yes |
| `/dev/photo-intake-action-states` | media kit; not flagship | no | **no** |
| `/dev/native-markdown` | foundation | no | **no** |
| `/dev/discover-cold-start` | Places empty composition | no | yes |

**QA bridges — keep off the design scroll**

`/dev/force-state`, `/dev/screenshot-mode`, `/dev/persona-switcher`,
`/dev/membership-epoch`, `/dev/deck-qa`, `/dev/billing-sandbox`,
`/dev/onboarding` (redirect into the real flow).

**Sandbox, not a specimen**

`/dev/interpretation-dossier` — live data, prototype reading surface. Link
from a QA/sandbox group if at all, never as a deterministic gallery.

The hub itself (`/dev/design-system`) is the index, not a specimen.

Component registry remains 89 (62 stable / 24 provisional / 3 internal),
`lastUpdated` 2026-07-31, catalog check still failing on `LedgerRow` path
drift plus 20 unregistered `components/ui` files. Repair that as hygiene. It
still cannot be the workbench: receipts and chat artifacts are feature
components.

## 4. The plan that is actually better

Keep August 14's hybrid end-state. Change only the first increment.

```text
Phase 0, made usable
  classify (this memo) + complete the hub menu + DevFab + Stack.Protected
        ↓
sit and polish the families that are already on device
        ↓
if fourteen scrolls are still too slow:
  one M1 signature scroll that reuses existing fixtures
  (original Phase 3, scoped to alpha-critical objects, pulled forward)
        ↓
when the next need is search, deep links, or agent discovery:
  original Phase 0.5 Storybook spike
  (do not hand-build NativeGalleryEntry / manifests first)
        ↓
original Phases 1–4 unchanged
```

### Slice A — complete the menu (the actual first increment)

This is original Phase 0 without waiting on a Storybook spike or an IPA
bundle audit.

1. Extend the existing `GALLERIES` array in `app/dev/design-system.tsx`.
   Group as Foundations / Demo signatures / Other kits / QA tools.
   Hard-coded links, no new schema, no tags, no capture tiers.
2. Mirror those groups in `DevFab`. One incomplete menu is the current bug;
   two incomplete menus is worse.
3. Wrap the `dev` screens in `Stack.Protected` with
   `__DEV__ || IS_INTERNAL_BUILD`. This is the fail-closed guard original
   asked for. It is not a bundle-exclusion proof.
4. Do not add new `app/dev` files. The seven routes missing from
   `Stack.Screen` are already routes because they live under `app/`. Linking
   them does not enlarge the leak surface. Creating new gallery files would.

Exit: DevFab → Design system reaches every true visual gallery without a
filename.

This is **not** "all components in one place." It is the missing table of
contents. Say that out loud so it does not get sold as the design scroll.

### Slice B — only if Slice A is not enough

Original was right that one giant mount-everything scroll is unreadable.
The founder-pain version of browse mode is smaller: **one scroll of
alpha-critical objects**, not all 27 routes.

Demo Journey Canon §15 names those objects: trip crown, decision receipt,
group room / chat artifacts, privacy-safe rationale, composer, controls,
headers. Pull existing production components and fixtures from the galleries
that already exist. Do not rewrite them. Do not include stay kit, photo
intake, profile, experience anatomy, or onboarding in this scroll.

Each family on that scroll gets the original's matrix, not a new one:
representative, one extreme, one absence or failure.

Exit: one sitting can judge whether the M1 objects look like one product.

### What remains original, on purpose

- Do not build `NativeGalleryEntry`, search, agent manifests, or generated
  Maestro catalogs before the Storybook spike.
- Spike Storybook on 3–5 components only when isolated discovery is the
  next bottleneck (leaf controls, provider-wrapped patterns). Keep native
  compositions native.
- Catalog broadly, baseline selectively. Do not screenshot 89 modules.
- Visual diffs are not taste. Maestro `assertScreenshot` stays the capture
  tool; it does not certify polish.
- Hosted Chromatic / App Percy / Sherlo wait for a measured review bottleneck.
- Before TestFlight or any new `app/dev` file, verify external-build
  exclusion. Conditional `Stack.Screen` is still not exclusion.

## 5. Why this beats both the original first action and the first follow-up

| Need | Original Phase 0+0.5 as one breath | First follow-up | This revision |
| --- | --- | --- | --- |
| Stop hunting filenames | After Storybook decision | Yes, but via a custom registry | Yes, extend `GALLERIES` |
| See M1 objects in one sitting | Phase 3 | Claimed a menu would do it | Slice B, only if needed |
| Avoid recreating Storybook | Strong | Contradicted itself | Strong |
| Route safety | IPA audit before any hub growth | Too casual | Protected for the menu; audit before new files / TestFlight |
| Agent duplicate-prevention | Storybook/MCP early | Deferred too hard | Same trigger as original: spike when discovery is the pain |
| Time-to-founder-sitting | Slowed by 0.5 | Fast, but wrong object | Fast, honest object |

The original's fear is still the right one: a beautiful custom workbench that
is a second Storybook. The first follow-up's fear is also real: a four-phase
platform plan that never becomes a sitting. The better plan is the original
with a usable Phase 0 and with Phase 3 available early, scoped to M1, if the
menu is not enough.

## 6. Decision

| Question | Answer |
| --- | --- |
| Is the August 14 memo useful? | **Yes. It is the architecture.** |
| Was the first follow-up a better plan? | **No.** Better sequencing instinct, worse object, worse classification. |
| What is better than original's bundled 0+0.5? | **Slice A now. Slice B only if sitting still requires fourteen taps.** |
| When does Storybook come back? | When the next step would be search, deep links, portable stories, or agent discovery — original's trigger, unchanged. |
| What must not be built in Slice A? | `NativeGalleryEntry`, a mega-scroll of all 27 routes, new `app/dev` files, a Storybook install, registry-as-workbench. |

## 7. Home kits (2026-08-15)

Hub + M1 signatures still do not show the recently revamped **Trips Home** and
**Places Workspace** card families. Those surfaces are existence-gated, so
one mock persona never reveals the kit. The next increment is two labeled
family scrolls (`/dev/trips-home-kit`, `/dev/places-workspace-kit`), not a
fake fully-loaded home. Plan:
[home-kit-galleries-plan-2026-08-15.md](./home-kit-galleries-plan-2026-08-15.md).
