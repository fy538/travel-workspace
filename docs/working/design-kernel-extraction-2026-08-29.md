---
doc_type: working
status: active
owner: founder / design
created: 2026-08-29
last_verified: 2026-08-29
expires: 2026-09-28
why_new: Extracts the root-agnostic layers of the pre-pivot design system into one citable kernel so all four root boards (Home, Chat, Places, Life) build on the same substrate instead of re-deriving it — the structural defense against the sparseness over-correction recurring per root.
promotes_to: null
supersedes: []
source_of_truth_for:
  - the root-agnostic design kernel vocabulary and its authority map
depends_on:
  - docs/decisions/2026-08-28-adopt-four-product-moves.md
  - docs/decisions/2026-08-29-close-whole-product-v1-wave-0.md
  - docs/working/home-surfaces-pre-pivot-recovery-and-post-pivot-direction-2026-08-27.md
  - docs/working/places-four-state-design-fixture-brief-2026-08-29.md
---

# Design Kernel Extraction

## Decision

The pre-pivot design system's **root-agnostic layers** — tokens, type roles,
geometry, composition grammar, evidence union, identity anatomy, registers —
are the shared foundation for all four root boards (Home, Chat, Places,
Life). Trip-coupled layers (composition plans, producers, section unions, the
8-posture Trips page model) are **not** extracted and must not be cited as
kernel.

Validation: the kernel passed its worst-case register test on 2026-08-29 —
the Places **Live Reduction** operational instrument rendered strictly inside
kernel language (HOLD + ACT NOW postures), founder-reviewed and approved.
Board: `claude.ai/code/artifact/41450961-6c8c-43d4-8a6c-87842f6cd40c`.

This is the recovery doc's §7 direction made citable: *recover the pre-pivot
compositional grammar without recovering trip-centric ownership.* A rule no
implementer sees is not a rule — root briefs and roadmaps should cite this
page, and this page cites code.

## 1. Authority map — where each layer's truth lives

The single most important finding of the extraction: **most of the kernel is
already codified.** Where code and any board disagree, code wins; where this
doc and code disagree, code wins and this doc needs a correction entry.

| Layer | Authority | Verified |
| --- | --- | --- |
| Palette tokens | `travel-app/constants/colors.ts` | 2026-08-29 |
| Type roles | `travel-app/constants/typography.ts` + `constants/textVariants.ts` | 2026-08-29 |
| Font families | `travel-app/constants/fonts.ts` | 2026-08-29 |
| Containment scale + materials | `travel-app/constants/cardSurface.ts` | 2026-08-29 |
| Radius / elevation | `travel-app/constants/layout.ts` (via cardSurface) | 2026-08-29 |
| Receipt union | `travel-agent/backend/home/trips_stack_models.py` | 2026-08-29 |
| Component catalog + lifecycle | `travel-app/docs/Components.md` | 2026-08-29 |
| Card treatments | `travel-agent/backend/core/models/places_sections.py` | 2026-08-29 |
| Content contract (copy budgets) | `travel-agent/backend/core/content_contract.py` → generated `travel-app/constants/contentContract.generated.ts` | 2026-08-29 |
| Interaction motion | `docs/systems/motion-language.md` (ratified contract, CI-enforced via `npm run motion-governance`; tokens in `travel-app/constants/motion.ts`) | 2026-08-29 |
| Continuity motion (proposed) | `docs/working/four-root-continuity-motion-2026-08-29.md` — patterns 9–12 for cross-state/posture transitions | 2026-08-29 |
| Composition grammar (prose rules) | this doc §5 | 2026-08-29 |
| Identity anatomy | this doc §7 (board-carried) | board 08-11 |
| Registers incl. urgency ruling | this doc §11 | 2026-08-29 |

The Claude Design bundle (`~/Downloads/vesper-home-surfaces 2/`, exported
08-27, last verified 08-11 against since-moved commits) is **design history,
not authority**. Re-copy, never fork, when a board needs its drawings.

Provenance labels used below: `verified` = read from source 2026-08-29 with
file named; `board` = carried from the 08-11 board verification and NOT
re-read — quote with that caveat or re-verify before building against it.

## 2. Palette — verified, with live token names

All hex values confirmed byte-identical between the boards and
`constants/colors.ts`:

| Role | Token | Value | Line |
| --- | --- | --- | --- |
| Paper (page) | `paper20` | `#EFEAE0` | colors.ts:63 |
| Card | `paper00` | `#FBF7EC` | colors.ts:60 |
| Ink | `ink00` | `#1B1714` | colors.ts:66 |
| Mute | `ink60` | `#6E6862` | colors.ts:69 |
| Mute light | `ink80` | `#B5AFA5` | colors.ts:70 |
| Gold | `gold60` | `#B0853A` | colors.ts:72 |
| Gold deep | `gold80` | `#8A6628` | colors.ts:73 |
| Gold light | `goldLight` | `#F2E6CC` | colors.ts:201 |
| Oxblood | `ox60` / `oxblood` | `#7A2E2E` | colors.ts:74/207 |
| Green | `confirmGreen` | `#3D7050` | colors.ts:216 |
| Planning ink | `blue60` | `#3D5066` | colors.ts:79 |
| Planning ink deep | `planningInkDeep` | `#2A384B` | colors.ts:189 |
| CTA primary | `primary` | `#4A3428` (umber — the only solid CTA fill; never gold) | colors.ts:153 |
| CTA tint | `tint` | `rgba(27,23,20,0.06)` | colors.ts:156 |
| Hairline | `borderHairline` | `rgba(27,23,20,0.10)` | colors.ts:96 |
| Hair-thin | `borderHairlineSoft` | `rgba(27,23,20,0.06)` | colors.ts:97 |

Color laws: planning ink is **the page's only non-warm element** and belongs
to StatusMeta. `danger` (colors.ts:444) resolves to oxblood — see §11 for the
urgency ruling that governs its visible use.

## 3. Type — three voices and their laws

The type system is three *voices*, not three fonts (`fonts.ts`, whose
header comments are themselves doctrine — read them before any type work):

- **Serif — EB Garamond** (`serif` 400 / `serif_medium` 500 /
  `serif_semibold` 600 / `serif_bold` 700; no 300 weight exists): editorial
  titles, reading moments, and Vesper's voice. History (Fraunces →
  Cormorant → Newsreader → EB Garamond) is settled; do not reopen — the
  Newsreader swap was already tried and reversed.
- **System sans**: UI surfaces, chrome, captions, body copy — the workhorse.
- **JetBrains Mono** (`mono` 500 / `mono_bold` 700): stamps, dates,
  timestamps, evidence labels — the "this is a fact" voice.

Laws (verified in fonts.ts, ratchet-enforced by
`__tests__/conventions/serifFloorContract.test.ts`):

1. **Size floors**: serif never below 15px; the italic register never below
   17px. Rationale is codified: EB Garamond's small x-height reads ~20%
   smaller than sans at equal px — above 15 that difference *is the point*
   (a legible second voice); below it, the pairing looks like a mistake.
2. **The ×1.2 ratio**: serif replacing sans at the same hierarchy level
   needs ~1.2× the size (reference pair: 18px sans ≈ 22px serif). Never
   eyeball this per call site.
3. **Violations are a triage, not a bump**: sub-floor serif is usually body
   or UI text and the fix is moving it to sans (same px, larger apparent
   size, no reflow) — raise to 15 only for genuinely editorial or voice
   moments.
4. **Italic is a register, not a style**: one approved italic
   (`serif_italic` 500), used only through `textVariants.vesperVoiceItalic`
   — Vesper speaking. Never synthesize slant at a call site.
5. **Weight ladder for serif titles**: `serif_semibold` at 24–29px,
   `serif_bold` at ≥30px.
6. **Caps need tracking**: system-sans uppercase requires positive
   letter-spacing 1.4–2.0 (`letterSpacing.caps…capsWidest`); display
   tightens as size grows (−0.6 / −1.0).

| Role | Spec | Source |
| --- | --- | --- |
| `cardTitle` | sans 600 16.5/20/−0.3 | typography.ts:407 |
| `cardTitleLg` | sans 600 19.5/22/−0.3 (crown/sketch titles) | typography.ts:412 |
| Object-page title | sans 600 24 (one rung above cardTitleLg) | typography.ts:413 |
| `serifTitleLg` | serif_medium 20/25 | textVariants.ts:114 |
| `serifProseHeading` | serif_semibold 20/28 (crown read) | textVariants.ts:131 |
| `monoStampStrong` | mono bold 9, ls 1.15, caps (eyebrow) | textVariants.ts:156 |
| Mast | serif 600 30/34 · sub sans 12.5/17 | board 08-11 |
| StatusMeta | 6pt dot + sans 600 11, ls 0.8, caps | board 08-11 |

### 3.1 The board rhythm ramp — CONSOLIDATED 2026-08-30 (founder correction)

The founder reviewed the compositions and called the micro-rhythm off.
Audit confirmed it: 33 distinct font sizes, mono kickers at 9px/1.15
against the ruled 10px floor (which `textVariants.monoStamp` already
enforces at 10/1.3), italic quotes below the 17px italic floor, seven
section padding values, radii 9–18. All 27 boards were normalized onto
one ramp, anchored to the code tokens (code wins):

**Mono** — kicker/stamp 10px·700·ls 1.3 (gold-deep, mute, or ghost);
data/footnote 10px·ls 0.9 ghost; numeral/time and world-read anchor
11px·700·ls 1.15; chips 10px·700 in the pill. Floor 10px everywhere in
HTML text; SVG diagram labels (map annotations, 7.5–9) are exempt as
artwork.

**Sans** — meta 12.5/17 · controls (doors, secondary buttons, dense
cells) 13/18 · body + primary CTA 14/19 · row title 15/19·600·−0.2 ·
cardTitle 16.5/20·600·−0.3 · crown title 19.5/22·600·−0.3 ·
StatusMeta 11/600·ls 0.8.

**Serif** — compact prose 15.5–16 · voice italic 17/24 (floor 17,
ruled) · prose read 18/25 · crown read 20/28 · editorial title 18.5 ·
relation title 22/27 · world read 26/33. Serif floor 15 stands.

**Geometry** — dots 3–4 · receipt/CTA 11 · media & 56pt+ thumbs 13
(44pt → 9, 56pt → 10, 72pt → 12) · card 15 · frame 16 · crown 18 ·
pill 999. Row heights quantized to 34 (spine) / 36 (door) / 44
(compact) / 52 (standard) / 56–68 (plated). Section rhythm: one beat —
`padding-top: 24` between sections (16 only directly under the world
read). Page gutter 22, card padding 15–16.

Any new board value outside this ramp is a defect unless ruled in.

## 4. Geometry

| Constant | Value | Provenance |
| --- | --- | --- |
| Crown radius | 18 (`cardSurfaceRadius.tonal`; the crown's own literal is independent but equal) | verified cardSurface.ts:170 |
| Card radius | 14 (`radius.surfaceCard`) | verified layout.ts:71 |
| Receipt box | r11, pad 8/12, gold@22% border on gold@7% fill | board 08-11 |
| Row floor | 60 · pv 8 (44/56 image plates fit; 92 does not) | board 08-11 |
| Page gutter | 22 → content 349 at 393pt (receipt caps 3 chips / 2 rows measured at this width) | board 08-11 |
| Facepile | 22pt discs, tuck 0.34, plate 24.4 | board 08-11 |
| Button sm | minHeight 36, ph 20, label 12/16, r11 | board 08-11 |
| Consequence rule | 2pt gold LEFT rule on transparent | verified cardSurface.ts:144 (named in doc comment) |

## 5. Composition grammar — the rules that make it one product

1. **Containment = completion.** "A card marks something you can complete
   here. A row takes you somewhere else." Codified with the scale itself in
   `cardSurface.ts` (`CONTAINMENT`: 0 uncardedSection · 2 groupBanded ·
   3 groupOutlined · 3.5 flatObject · 4 quietPanel · 5 crown). Operates on
   objects, not sections; a preview inherits the object's containment.
2. **The second axis.** "Set apart" ≠ "finishable" — the 4− paperFlat and
   the 2pt gold left rule both say *set apart* without claiming completion.
   The middle of the scale (2–3) is where editorial lives. (Named in the
   cardSurface.ts doc comment; the left rule still has no rung — deliberate.)
3. **Presence.** Uncarded + imagery = editorial; uncarded + no imagery =
   admin form. One illustration family everywhere; every media slot passes
   `media={null}` today — but see §12.2 for the Life-driven media extension.
4. **One solid CTA.** `action.primary` umber is the page's only solid fill;
   everything else is tint or a row. Urgency never changes this (proven by
   the ACT NOW frame: pressure lives in status and content, not a red
   button).
5. **Evidence discipline.** Receipts render only from real data, never as
   decoration or a second action. A solo return carries **no** receipt — a
   reason is not proof. Count toward, never count missing.
6. **Register diversity beats quantity.** Fullness comes from different
   registers, not more examples. "One dominant thing does not mean one
   visible thing" — the anti-sparseness law from the recovery doc, now a
   kernel rule so no root re-learns it.
7. **Standing trap.** Read the render path, not the stylesheet; resolve
   every variant to a number.
8. **Surfaces select; containers compose** (the locus-of-generation law
   — RULED 2026-08-29, founder; see §11.5). Root surfaces are designed:
   stable anatomies whose slots fill from bounded, kind-keyed unions and
   whose only dynamism is *selection among designed states* (posture,
   dominance, rotation, register — enumerated variation). Generated,
   viewer-relative composition belongs to **object containers** — the
   Occasion container (the Occasion capsule + its five compilers) and
   the Trip/Plan container (My Shape / Together / Whole Shape) — which
   render *inside* stable slots at the slot's density. A root whose
   layout is composed per-moment violates the stable-skeleton law
   ("roots should not shapeshift… every time the resolver changes its
   mind"); a container rendered from a static template violates the
   reason the itinerary was demoted.

## 6. Evidence union — verified grain-agnostic

Eleven receipt kinds live in `backend/home/trips_stack_models.py` (`spine`
:430, `ledger` :147, `candidates` :275, `checklist` :182, `conditions` :500,
`people` :455, `diff` :203, `call` :221, `shape`, `waveform` :483, `near_you`
:301). **No payload carries a trip reference** — the 08-06 canon resolution
holds. Coupling lives in exactly two places, neither of them the types: the
producer (`_receipt_for_card`) and the carrier field. Adoption by any root =
one carrier field + one producer; no union edits. The spine shape's
`label · title · is_open` mapped onto the Live Reduction sequence
(time · step · fixed/flexible) with zero generalization — third grain it has
carried unchanged.

## 7. Identity anatomy — board-carried

One crown anatomy; **the biggest slot holds the most specific true thing
about the object**: Trip → where · Night → who · Wander → the area ·
Return → the place itself · **Live → the route/map** (extended by the
stress test). Scale is a separate instrument from containment — a lead can
lead by size on bare paper. The four-grain framing ("one occasion object,
four grains") predates and survives the pivot; it is the kernel's cleanest
bridge to the Occasion model. RULED 2026-08-30: both gradients
(identity — the biggest slot holds the most specific true thing;
structure — a dominant never carries more structure than its subject
truly has) govern the Home Now union; see the build manifest §1.1 laws. Anatomy values (art 96/94 optical, StatusMeta,
facepile-on-dates-row) are board-carried — re-verify at build time.

## 8. Component layer — build with the catalog, not beside it

The canonical component inventory is **`travel-app/docs/Components.md`**
(Actions, Selection, Forms, Headers, Layout, Rows, Surfaces, Status, Media,
Sheets, States, Typography, Identity — plus a lifecycle, a retired list, and
a maintenance contract). The kernel rule is about *how* it is used:

1. **Every surface composes from catalog components.** A new board draws
   with the existing anatomy first; a genuinely new component is a catalog
   addition (with lifecycle entry), never a one-off in a screen file.
2. **Containment is chosen by recipe, not by hand.** `CardSurface` recipes
   (`crown`, `quietPanel`, `flatObject`, `quietReceipt`, `tonalGroup`,
   `groupOutlined`, `groupBanded`, `urgentState`, `calmState`, `uncarded…`,
   16 total in cardSurface.ts) map to the containment scale — pick the
   step, take its recipe, never hand-roll fill/border/shadow.
3. **Two row grammars exist; know which you are in.** `TripsStackRows`
   (tier glyph + mono kicker + fact, no heading role) vs `ListRow` (38pt
   monogram/30pt icon slot + h2 title). Neither has an image path today —
   adding one is the drawn-but-unbuilt C6 fix (44/56pt plates), not a new
   grammar.
4. **Small primitives carry the identity** — reuse, never redraw:
   `StatusMeta` (the 6pt-dot status line), `ConsequenceBanner` (the 2pt
   gold left rule), the receipt dispatcher (renders all 11 shapes inside
   the caller's box), the facepile (22pt/tuck 0.34), `Button`
   (`variant="tint"` default; solid = umber primary only).
5. **Retired stays retired.** Components.md's retired list is a boundary —
   a board that redraws a retired component is proposing its revival and
   must say so.

## 9. Treatments — how a card presents a judgment

Server-owned presentation vocabulary, verified in
`backend/core/models/places_sections.py:101-139`
(`PlacesSectionTreatment`). The client renders; the producer decides:

- **`single`** — one confident reading of one thing.
- **`fork`** — two readings, deliberately **without** a confidence claim
  between them.
- **`choice`** — a real decision offered to the person.
- **`conviction`** — the raised-material "we are sure" register.
  **Deliberately producer-less (dark) by ruling**: the code comment is the
  law — without a non-proximity confidence signal, "an emitted conviction
  would be fabricated certainty." Do not wire a producer to it; earning
  conviction is a data problem, not a UI one.

Kernel reading: treatments are the *epistemic honesty layer* — the visual
system distinguishes "here is one thing" / "we genuinely don't know which" /
"you decide" / "we are sure," and the rarest register is intentionally
unreachable until the evidence exists. Any new root surface presenting
judgments adopts this vocabulary rather than inventing adjacent ones.

## 10. Content contract — copy has budgets, not vibes

Per-field character budgets are generated from the backend
(`backend/core/content_contract.py` →
`travel-app/constants/contentContract.generated.ts`), kept in FE/BE
lockstep, and test-enforced (`cardContract.test.ts` — every persona's mock
copy must fit). The home-card instance:

| Field | Target | Max | Prompt hint |
| --- | --- | --- | --- |
| eyebrow | 24 | 40 | 2–3 word category label |
| title | 48 | 80 | one punchy line, ~6 words, no trailing punctuation |
| body | 84 | 160 | one sentence in Vesper's voice — fits 2 lines on the hero |
| cta_label | — | — | governed, see generated file |

Contracts also carry `grounding` ("only the card's supplied … facts") and
`adjacentOverlap` rules ("do not repeat adjacent labels or receipts").
Kernel rule: **a new surface's copy slots get a contract instance before
they get mock copy** — budgets are how boards, generation, and backend stay
honest about the same rectangle.

## 11. Registers

- **Editorial** (serif read, illustration, uncarded-with-imagery) — the
  default register for possibility.
- **Admin** (uncarded, typographic, rows) — logistics and settings.
- **Voice** (serif italic ≥17px) — Vesper speaking; the temporal-posture
  line ("The route is viable. Nothing needs booking yet.") lives here.
- **Urgency** — **RULED 2026-08-29 (founder): oxblood `#7A2E2E` is admitted
  as the urgency StatusMeta color.** Scope: a live threshold that is real
  and close — never decoration, never emphasis. The planning-ink reservation
  is untouched (oxblood is warm). Urgency composes as: oxblood StatusMeta +
  countdown in the meta row + compressed content + (optionally) the
  consequence rule promoted — the CTA law (§5.4) and the calm ground do not
  change. A release path ("Let it pass") must always exist; HOLD is never a
  task.

### 11.1 Gold register and the Door law — RULED 2026-08-29 (founder)

Gold was carrying seven roles (993 call sites; census 2026-08-29). The
ruling splits affordance out of voice:

- **Gold text is tappable if and only if it carries the canonical trailing
  arrow.** One arrow idiom (the `arrow-forward` glyph at 13pt, gold-deep) —
  the literal `→`-in-string and ad-hoc chevron variants migrate to it.
- **Gold never appears on non-tappable body text.** Inert statuses move to
  mute/ink; deadlines and live thresholds move to the oxblood urgency
  register (§11). Gold stamps (mono eyebrows) remain — the mono voice, not
  body text, is what disambiguates them.
- **Three-class signifier law** (extends §5): arrow = door (navigates);
  a distinct edit affordance = correctable record; nothing = read-only.
  Grounding: WCAG 1.4.1 (color alone cannot mark interactivity; warm gold
  on warm paper fails the 3:1 luminance test), Apple HIG (one tint color,
  interactive-only), NN/g flat-design research (+22% task time under weak
  signifiers).
- **Build target:** one `Door` primitive (uncarded tappable line: gold text
  + trailing arrow + 44pt target) replacing ~21 hand-assembled sites; a
  conventions ratchet (gold body text inside `Tap` must carry the arrow;
  outside `Tap` must not) once the primitive lands.
- Fixed same day: `components/stay/stayTokens.tsx` had gold/goldDeep
  aliases SWAPPED relative to the canonical palette; renamed with rendered
  colors preserved (consumer references flipped, tests green).

### 11.2 Micro-type floor — RULED 2026-08-29 (founder)

**No text role below 10px.** The 9px mono eyebrow sat below every shipped
floor (Apple HIG 11pt minimum / Caption 2 floors at 11; M3 label-small
11sp; M2's 10sp overline — the historical minimum — was dropped from M3).
Applied same day: `monoStamp`/`monoStampStrong` raised 9 → 10 with
tracking rescaled 1.15 → 1.3 (~0.13em ratio preserved); ~405 call sites
restyle via the token; three pinning tests updated, all green.
Remaining 9px roles to migrate when next touched: `capsMicro`,
`atlasGoldMark` (textVariants/typography), `discoverMeta`, `kicker`,
`kickerWide` (typography.ts), one raw literal in
`components/voice/MicPrivacyDisclosure.tsx:310`, and the sub-9 "micro tag"
(8pt) needs its own exception review. Dynamic Type stays uncapped (CI
enforces via `scripts/check-accessibility-contracts.mjs`); note the
Design Language's "reviewed exception" mechanism has no implementation —
build the allowlist when the first real exception appears. FontScale
adaptation thresholds are scattered (1.2 / 1.3 / 1.35 / 1.4 / 1.75) —
name them as shared constants when next touched.

### 11.3 Night register — DIRECTION RULED 2026-08-29 (founder), build deferred

**"Lamplight"**: the warm inversion, not a neutral dark theme. Model is
Apple Books — theme identity persists, brightness is an orthogonal axis.
When built: ground = warm near-black (the ink family, never pure #000 —
halation), cards one lightness step up, text = paper tones, gold
desaturated ~10–25% and lightened ~5–15%, oxblood lightened; riso
illustrations keep their paper plate on the dark ground (art is not
re-authored). Current state is hard-locked light (`app.json`
`userInterfaceStyle: "light"`, flat palette, zero scheme detection) —
the semantic-alias structure (`surfacePage`/`surfaceCard`) makes
theme-keying structurally cheap later. First scope when built: the Live
register (the evening use case). Until then this stays parked per Brand
Identity's expiring-plan note; this section exists so the *direction* is
no longer an open question.

### 11.4 Cross-root projection contract — RULED 2026-08-29 (founder)

**Push, not tab-switch.** Tapping an origin-root proposition (Home's
Saturday route, a change claim, a Life return) opens the owning root's
projection **inside the origin root's stack** — it never auto-switches
tabs. Grounding: the four-product-moves decision's own line that focused
owner views "do not require additional root tabs" — *owner* and *tab* are
different things; task continuation is not a change of posture. The rules:

- One typed context envelope travels with any cross-owner tap (the
  twelve-field contract from places-consumer-experience-anatomy §6,
  generalized — it is not Places-specific; the same law governs
  Chat→Plan and Life→Places).
- The reason for the tap leads the destination; provenance renders as one
  quiet label; back restores the origin's exact scroll; the claim
  refreshes from canonical readback (seen is a state, not a badge).
- **The only tab crossing is the in-view door** ("Open Red Hook in
  Places") — the person's own act of converting a task into an
  exploration. The accepted cost: a pushed instrument is a deliberate
  dead end that cannot widen to World Field except through that door.
- **The projection push is the minority case.** Origin-root units
  complete on view; scroll-past is a complete ending; only a genuine
  instrument earns depth.
- Motion is the ordinary Workspace Transition within the stack;
  continuity-motion L5 (no cross-root shared-element animation) stands
  with nothing left to design against it.

### 11.5 Locus of generation — RULED 2026-08-29 (founder)

**Surfaces select; containers compose.** The generated-composition
system's authority is scoped to *objects*, not *pages*:

- **Roots stay designed.** Home's five regions, Places' four states, the
  Chat workbench's slot system, Life's period-and-episode spine — stable
  anatomies. What varies at a root is which content fills its slots
  (server-chosen from bounded kind-unions — the well-section union,
  Home's region kinds, Places' section reasons) and which designed state
  dominates (posture, rotation, register). Enumerated variation, never
  composed layout.
- **Containers are the generated things.** The Occasion container
  (`occasion capsule` + the five compilers in
  `backend/core/occasion_product_projections.py`) and the Trip/Plan
  container (My Shape / Together / Whole Shape) are compositions:
  viewer-relative, evidence-bound, assembled at read time from the
  object's actual commitments, decisions, people, and unknowns. They
  render inside stable slots at the slot's density — compact in the
  well, standard in a chat card (`CardBlueprintV1`), immersive when
  opened.
- **The adaptive resolver's legitimate scope is *within* containers and
  chat turns** — choosing a composed artifact's lead medium (sequence vs
  map vs comparison vs prose vs silence) per the seven-job taxonomy.
  Root-surface composition is outside its authority. Any future
  ratification of the resolver's job taxonomy is to be read with this
  scope constraint attached.
- Rationale: real variance lives in the object (every occasion differs
  in people, commitments, unknowns — the reason the static itinerary
  died); root cards are typed and slot-governed, where a per-moment
  composer buys little and costs legibility, spatial memory, and
  auditability ("why am I seeing this" multiplies at card granularity).

### 11.6 The compositional batch — RULED 2026-08-30 (founder)

Eight board-level questions closed in one sitting (board: "Canon · The
Eight Rulings" on the root-boards canvas). Seven adopted as recommended;
**#1 amended by the founder**:

1. **The world read is two-tier on Home.** The mono anchor (place-day
   stamp + freshness) plus a **two-line serif read at mast scale** in the
   standfirst voice — a read, never a greeting: something true about
   today ("Storms this afternoon. Saturday opens clearer."). Uses the
   registered mast role (`RootStandfirstVoice`, serif 600 30/34); no new
   type. **One voice moment per page**: when a posture's dominant moment
   is itself a voice statement (Quiet, Returned · Day 0), it promotes
   into the read and the Now region yields. Places keeps the compact
   band except at genuine cold start — the anatomy doc's §3.2 mast
   demotion stands, since its objection was masts that describe the
   product, not reads that say something true. Boards drawn before this
   ruling show the compact band; the canon pair and full-fidelity Home
   boards are the reference renders.
2. **Crownless Quiet is required, not merely admissible** — a card
   promises completion and a calm statement is not finishable; Quiet
   keeps the Now region, drops only the container.
3. **Evidence objects: object carded, door rowed** — where a human note
   itself renders (author, quote, audience, inspectable) it earns its
   container (Places, Life); where a region merely references it, that
   is a door, and doors are rows.
4. **Verdict registers render uncarded** until conviction is genuinely
   earned (which the treatment doctrine keeps producer-less — no
   board-level exception).
5. **Envelope staleness**: the destination always re-reads world truth
   on open; the envelope carries intent and evidence, never cached facts
   presented as current.
6. **Seen is canonical**, not per-device.
7. **Tab-bar icon language deferred, with an owner** — the dedicated
   design environment during production design; today's icons remain
   placeholders.
8. **56pt illustration plates on Home ratified** — the 44/56 row-plate
   gradient extended to Home (the C6 fix); 56 fits the row floor, 92
   never will.

### 11.7 The physical grammar survives the pivot — RULED 2026-08-30 (founder correction)

The founder reviewed the first specimen sheets against the pre-pivot
boards and ruled the comparison against the new work: "we deviated from
a more excellent visual grammar … visually it looks less clean." The
deviation, measured: **zero riso media plates** in the new sheets versus
one on nearly every pre-pivot unit; form variety collapsed to a uniform
labeled rectangle; the one-large-type-moment-per-unit rhythm lost; mono
promoted from kicker/footnote voice to body voice. Ruling:

1. **The pre-pivot physical grammar is kernel, not era styling.** The
   riso hatch plate (possibility), the polaroid with tilt and serif
   caption (evidence — photography only here, per the media doctrine),
   the was/now paired cells, the ticket stub, the tally, the editorial
   cover with scrim, the facepile with the dashed empty chair, the gold
   drop cap — these carry into the four-root era as the component
   wardrobe. New surfaces are clothed in them, not in bare rectangles.
2. **Every unit earns one large type moment** (≥17px serif or
   semibold sans); mono returns to kicker/footnote duty only.
3. **Card physics are uniform**: 13–18px radii, hairline + quiet lift,
   15–16px padding. No 9–11px-radius drift.
4. **Places carries browse texture again** — `field_browse_shelf` and
   `field_editorial_cover` join the World Field union (manifest §2.1),
   admitted by the same compiler, below the lead. Browse is a texture
   the field can hold, never the field's organizing principle.

Specimen sheets re-clothed same day; composition boards re-clothed the
same day (Home Saturday: map object in the crown, occasion plate +
facepile, editorial cover; World Field: hatch branch thumbs + the browse
shelf and editorial cover in composition; Focus/Path/fixtures: plates
hatched, Path title to serif). Quiet posture deliberately stays sparse —
sparseness there is the design, not the failure. Live Reduction stands
as founder-approved. Remaining un-re-clothed: none.

### 11.8 The Composition contract + the Shape default — RULED 2026-08-29 (founder)

Extends §11.5 from *containers compose* to what composing IS, and
demotes the itinerary surface. Board of record: "07 Chat - The
Composition" in the Vesper — Chat Design project. Vocabulary per canon:
a **Composition** is generated; an **Artifact** is brought or kept —
saving is the act that turns one into the other.

- **One frame, six bodies, three zooms.** Every composition renders in
  a fixed five-part frame: provenance kicker (mono — the promise-shelf
  result-family vocabulary; the shelf promises a family, the
  composition opens with the same family's name) · the read (serif, one
  interpretive line — the only genuinely generated language) · the body
  (exactly ONE lead medium of the canon's six + at most one supporting
  instrument) · the ground (mono stamps: sources, freshness, unknowns —
  unknowns render, never hide) · one continuation (door or prefill,
  never a button row). The same composition exists at three densities —
  compact (a well section, per the well composition rules), standard
  (`CardBlueprintV1`; its 8-block grammar IS this frame at card scale),
  immersive (opened, editorial family; the one unbuilt density) — as
  one object at three zooms, never three artifacts (the Card↔Deck
  fidelity law generalized).
- **Freedom ladder.** FIXED (client-owned, invariant): frame anatomy,
  type, color, spacing, skins, density geometry, action mechanics.
  CHOSEN (server, per render, from enumerated sets): job, lead medium +
  support, claim selection and order, read-line copy, modifiers,
  audience projection, the one continuation. NEVER (nobody, including
  the model): layout, novel components, coordinates, colors, gestures,
  persistent identity without a save event. Dynamic in selection and
  language, static in form — dynamic the way a newspaper is dynamic.
  Viewer-relativity is a law, not a style: My / Together never merge
  into one synthetic read.
- **Laws:** one job per composition (a second job = a second
  composition or the continuation); smallest medium that makes the
  contribution perceptible; evidence-bound and fabrication-closed
  (silence is a first-class render); three zooms one object; the
  composition owns nothing (actions opaque + re-authorized; consequence
  returns as a receipt); every composition names how it ends;
  duplicate-family suppression across well / shelf / open thread.
- **Design language:** no new dialect — the §11.7 physical grammar
  assigned per medium (sequence: timeline rows + ticket stubs + was/now
  cells + the §12.1 dot encoding; comparison: paired cells + tally +
  serif verdict, diagram only per the §12.1 boundary; spatial: the map
  plate; evidence: quote plates + polaroid/riso + facepile; prose:
  serif + gold drop cap at immersive + editorial cover; instrument: the
  Instrument Hold strip = the well's live sliver). Mono = provenance,
  serif = interpretation, sans = data; at most one gold moment per
  composition.
- **Persistence — four endings, declared in the brief, stamped in the
  ground:** ephemeral (default; durable residue = the message's plain
  text; the graph is the truth, the composition never is), refreshable
  (recomputed at read; staleness renders), **saved** (a deliberate
  human act mints a versioned manifest — id, brief, claims, viewer,
  timestamp — and the Composition becomes an Artifact in Life;
  corrections regenerate versions, never mutate; anything shared is
  automatically versioned; nothing self-saves), live (instrument UI
  never persists; the receipt does).
- **The Shape default — the itinerary demoted.** The default
  projection of any occasion is its **Shape**: a few settled things, a
  few open things, who's in, what's unknown (the OccasionCapsule
  fields / PlanShape lanes). Time enters as stamps on commitments,
  never as a grid everything must inhabit. The day-by-day timeline
  survives only as an **earned lens**: sequence leads for a day only
  when that day holds enough timed commitments that sequence is
  genuinely the smallest medium. Use-case ground: one moment / an
  outing / a gathering / live / after never touch an itinerary; only
  the dense trip day earns one. Dies at the surface: the day grid as
  single-trip home, block-editing ceremony as primary UI, day-placement
  as the price of being real. Survives beneath, unchanged: commitments,
  booking/provider sagas, the operation ledger as audit spine,
  feasibility as a quiet check on timed conflicts. Guard: if the Shape
  ever grows tabs, the itinerary has been rebuilt under another name.

### 11.9 The Chat entry — RULED 2026-08-29 (founder, seven passes)

Boards of record: Vesper — Chat project, 02 (target entry), 04 (well
vocabulary + composition), 05 (promise shelf), 06 (entry states),
08 (the entry envelope — the typed build contract). Trigger remains the
four-root migration (board 03); the shipping workbench changes nothing
until then.

- **One skeleton, state-invariant:** chrome → read line → well → air →
  prompt shelf at the composer → composer → dock. States differ by what
  fills the slots and in what register, never by layout. Slots empty;
  they are not rearranged.
- **The chrome speaks the world, not the brand.** The header eyebrow is
  a server context slot: at rest the world line (LOCATION · WEATHER,
  "BROOKLYN · 72° CLEAR" — live weather service, never seeded-world),
  during a live occasion the mode line ("LIVE · RED HOOK · 72°"),
  silent pre-permission. "With Vesper" is deleted. Actions live in ONE
  warm-glass capsule (Search · History/chatbubbles · You); the compact
  "Vesper" title morphs into the capsule on scroll only.
- **Well composition:** at most three kind-keyed sections; ONE loud
  (gold wash — nearest deadline wins), ONE full-anatomy (rest compact
  rows), fixed order demanding → live → reporting → quiet; overflow
  collapses to a roll-up row. **Durable truth never earns a row** — the
  as-built facts band is retired; facts annotate sections as context
  stamps. The well persists wherever anything honest fills it; the
  honest empty (well absent, air extends) is a designed outcome.
- **All prompting gathers at the composer.** Below the well is air —
  load-bearing, no producer may claim it. The shelf = worked lead
  {family kicker + provenance, serif ask, one substance line} + ONE
  row of two named-return tiles; two rows only leadless (Live, where
  the live moment is the lead). Zero CTAs: no doors, no buttons —
  every element is tappable whole and prefills the composer, editable.
  No duplicate family between lead and tiles; fewer honest asks →
  fewer tiles, never filler. Cold takes the bring→get conditional form
  (scaffolding grows as ground shrinks).
- **Family vocabulary (closed set):** A CATCH-UP · A COMPARISON ·
  A ROUTE · A SHAPE · A KEEPING · A WATCH · A SETTLING · A FINDING
  (cold lead may take A FIRST SHAPE). GHOST_COPY generalizes to
  {family, ask, substance?} tuples, server-owned.
- **Owed before ship** (board 08): content-contract instances for the
  new copy surfaces; the world-line producer (device + weather via the
  envelope, with staleness rule); resolver job-taxonomy ratification
  (scoped by §11.5) before selection goes live.

## 12. Adjacent system rulings

<!-- Header restored 2026-08-29: a prior edit dropped the "## 12" line;
     the §12.1–§12.4 numbering below is load-bearing (cited by §11.8,
     §14, §15). -->

1. **Map grammar — RULED 2026-08-29 (founder); honesty contract added
   2026-08-30.** Segment source (routed / estimated / unknown) is a
   channel orthogonal to user commitment; minutes render only off a fresh
   fact; a crossing draws a bare arc, never invented geometry; hollow
   pin = unrouted endpoint. One encoding, many media:
   ink coastline on paper wash, **gold = scheduled/fixed, dashed ink =
   flexible, oxblood = constraint**, mono labels, no photography — the same
   sentence across city field, peninsula map, difference diagram, route
   strip, and sequence dots (solid gold dot = scheduled, hollow = open,
   dashed = flexible). Two additions ratified with it: a fourth encoding
   slot — **oxblood concentric rings = live position** (as rendered on the
   ACT NOW frame, no longer improvised); and the diagram boundary — a
   comparison earns a *diagram* only when the difference is
   spatial/structural, otherwise it stays prose (closes the
   difference-diagram question from the Places board).
2. **Media doctrine — RULED 2026-08-29 (founder), amended same day to
   three registers after reconciling with the ingestion canon.**
   (a) **Illustration renders possibility** — suggestion surfaces keep
   `media={null}` and the illustration family.
   (b) **Document-like captures canonize into typed anchors** — a ticket,
   reservation, or receipt (however ingested: email, photo, share sheet)
   becomes an Experience Anchor (Movement/Base/Attendance/Dining/Attention
   — `docs/working/artifact-and-experience-anchor-grammar-v1-2026-08-21.md`)
   whose canonical rendering carries the product behavior, with the raw
   source kept inspectable underneath — "the original is evidence, not the
   hero," displayed per the Expression canon's layered-source rule
   ("original, derived fact, and uncertainty remain distinct"; the typed
   rendering accompanies, never replaces).
   (c) **Substance photographs stay photographs** — people, scenery,
   moments render as photographs (Attention traces / Occasion evidence),
   never auto-canonized, no inference from faces or co-presence; presented
   with respect (no aggressive crops, no filters, warm cast fine).
   Generated compositions never impersonate either register ("generated
   imagery never presents invention as lived evidence").
   **This unblocks the Life board.**
   Intake-side flags surfaced by the 08-29 investigation, owned by the
   intake-v2 track, not this doc: the 24h `ephemeral_processing` raw-byte
   TTL is correct for documents but destroys substance photos — retention
   choice must surface at capture for register (c); HEIC (the default
   iPhone camera format) currently fails closed (no decoder lane); EXIF
   location use/stripping is unspecified anywhere in the intake docs.
3. **Dense retrieval register**: Life's multi-year index may need a row
   grammar denser than floor-60. Unexplored; flag at Life board time.
4. **ACT NOW anatomy inversion — RULED 2026-08-29 (founder).** The
   consequence rule may promote above the crown, with three constraints:
   Live register only; only when facts justify ACT NOW (never
   HOLD/MONITOR/WAIT FOR SIGNAL); reverts the moment the posture drops.
   This is the visual analog of the existing posture law ("Urgent is the
   only posture allowed to suppress most of the supporting field").

## 13. Not kernel — do not cite as kernel

- The 24-kind Trips section union, its ANCILLARY/POST_HERO orders, and the
  8-posture Trips page model (trip-lifecycle-keyed).
- All producers and gating (`stackCrown`, `showCountdownSection`,
  `committedTripIds`, `_receipt_for_card`).
- Trip-entity-bound sections: companion reading, today-mapped, trip feel,
  dreams-in-taste, the group section, expense-ledger receipt semantics.
- The Places ranked-feed page skeleton (the reasons/cards survive as
  content units inside the four-state encounter; the feed as page does not).
- The three-tab role split ("Trips/Places/Vesper") — superseded by the
  four-root ownership matrix in `travel-agent/docs/product/Surfacing
  Strategy.md`.

## 14. Per-root application

| Root | Kernel posture |
| --- | --- |
| Home | Near-pure reuse: five regions re-edit existing anatomies (crown→Now, open-loops→In motion, trail→Horizons, group→With people, memory family→Continuity); the work is register diversity, not new parts |
| Chat | Entry CONVERGED 08-29 (§11.9, seven founder passes): world-line chrome, well composition laws, prompt shelf at the composer, typed envelope contract (board 08); kernel governs cards/receipts that land in chat; the artifact-language track keeps its own conversational chrome — boundary doc needed if conflict appears |
| Places | Kernel governs everything around and on the canvas; the canvas grammar itself is §12.1 — new work in kernel clothes |
| Life | Greenfield on kernel substrate; blocked on §12.2 media ruling; watch §12.3 density |

## 15. Open rulings queue (founder)

Empty. All nine 2026-08-29 rulings closed: oxblood urgency StatusMeta
(§11); gold register + Door law (§11.1); micro-type floor 10px (§11.2,
applied); Lamplight night direction (§11.3, build deferred); map grammar
incl. live-position rings + diagram boundary (§12.1); two-register media
doctrine (§12.2 — Life board unblocked); ACT NOW inversion, scoped
(§12.4); cross-root projection contract — push, not tab-switch (§11.4);
locus of generation — surfaces select, containers compose (§11.5, and
§5.8; scopes any future resolver job-taxonomy ratification).
Plus the 2026-08-30 compositional batch of eight (§11.6; #1 amended by
the founder: Home opens with the two-line serif read at mast scale, one
voice moment per page) — which also closes the projection-contract
board's two former opens (envelope staleness, canonical seen).
Remaining watch item, not a ruling: dense retrieval register (§12.3, at
Life board time).
Added late 2026-08-29: the Composition contract + the Shape default
(§11.8; board of record "07 Chat - The Composition") — one frame / six
bodies / three zooms, the freedom ladder, seven laws, four persistence
endings, and the itinerary demoted to an earned per-day lens beneath
the Shape. One open call flagged inside it, deliberately left with the
workbook: which compositions may earn saved identity (recommendation
on the board: share-or-keep intent only; nothing self-saves).
Added late 2026-08-29: the Chat entry batch (§11.9, seven founder
passes) — one state-invariant skeleton, world-line chrome ("With
Vesper" deleted), well composition (3 max / one loud / one full /
fixed order; durable truth never earns a row), the prompt shelf at the
composer (lead + one row, zero CTAs), and the typed entry envelope
(board 08). No new opens beyond what it restates: the resolver
job-taxonomy ratification (already scoped by §11.5) now has its first
concrete consumer — entry-slot selection — plus content-contract
instances owed before ship (listed on board 08).
