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
   *Correction entry (2026-08-30, code wins per §1):* the live radius
   scale is `layout.ts` — `card: 12` (compact/inner containers),
   `surfaceCard: 14` (the ordinary Quiet Paper card), `xl: 16` (the
   chat outer card and the well, as shipped). The prose range above is
   corrected to those three values; the real rule is the *semantic
   assignment* (outer chat card 16 · inner container/inset/plate 12),
   not a numeric band. Padding corrects to the spacing scale: `14×16`
   card padding (`lgl`×`xl`), `8` row rhythm (`md`).
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

**Amendment — RULED 2026-08-30 (founder): "Surfaces select; screens
adapt; content composes."** The 08-29 contract's language overstated
generation; corrected doctrine (boards of record: 07 amended in place,
09 "The Immersive Density" — renumbered from a colliding 08):

- **Scenario screens, not generated artifacts.** Each Wave-1 scenario
  (Invitation, Shape, Decision, Participation Brief, Live, Story) is a
  DESIGNED, stable screen — a slot system fed by a server envelope,
  exactly the workbench pattern. The five-part frame survives as the
  shared CHASSIS; the six media become the SECTION VOCABULARY scenario
  skeletons draw from. Skeletons adapt BY SCENARIO (designed,
  enumerated — one chassis, N scenario skeletons), never by render.
  Within-screen variation is enumerated state variation (the Shape's
  earned day-lens is a designed lens state, not a free medium choice).
  Rationale: the compilers already return typed anatomies — an
  invitation's form IS the invitation; §11.5's cost argument
  (legibility, spatial memory, auditability) applies one level down;
  the real variance the system serves is content variance, not form
  variance. People learn what an invitation looks like — that literacy
  is the product.
- **True medium choice survives in exactly one place: the chat
  answer** — ephemeral, in-thread, frame-governed. The resolver's
  legitimate scope shrinks from "within containers and chat turns" to
  chat turns plus enumerated lens states; job-taxonomy ratification
  exits the artifact critical path entirely.
- **The artifact runtime is first-class — an instrument, not a page:**
  (1) multiplayer state (votes, RSVPs, contributions land in the
  experience graph and re-project to every member); (2) viewer
  identity (My / Together / Whole natively); (3) live truth
  (refreshable bindings, in-place instrument values, the re-read
  band); (4) authorized action (only through the opaque re-auth
  path); (5) input collection (a screen may ask one question back;
  the answer becomes graph truth); (6) handoff (group threads,
  zero-install invitees, Life). Generation quality concentrates in
  DEEP SLOTS — the read as genuine interpretation, claim selection as
  judgment, the brief as personal, narrative under the grounding
  gate. The skeleton being boring is what lets intelligence
  concentrate where a person can feel it.
- **External placement (researched 2026-08-30, two passes, primary
  sources).** Industry taxonomy (OpenUI): static / declarative /
  open-ended generation. Our lanes: scenario screens = static;
  CardBlueprintV1 = declarative (the production-consensus bucket);
  open-ended refused for artifacts. Convergences: MCP Apps (shipped in
  Claude, ChatGPT, Goose, VS Code) is developer-authored, pre-declared
  UI in sandboxed iframes — zero model-generated layout in the
  standard; OpenAI Apps SDK's four display modes map onto our density
  ladder (inline=standard card, carousel=option sets,
  fullscreen=immersive, picture-in-picture=the live sliver) and its
  "keep tools useful without a component" is our durable message-body
  fallback; Google A2UI = catalog-only declarative JSON. The
  counter-example, honestly located: Gemini Dynamic View / AI Mode
  generates full per-prompt UI — explicitly experimental, minute-plus
  latency, acknowledged inaccuracies, and ANSWER-lane only. The
  frontier experiments exactly where this amendment reserves freedom;
  no one generates layout where it freezes form. Escape valve if ever
  needed: one sandboxed GeneratedView-style section kind inside the
  declarative frame (the documented hybrid), never a fork of the
  system. Wire-format economics favor lean blueprints (measured 2-3x
  token/latency spread among declarative formats). Strategic option
  unlocked by stable screens, parked not Wave 1: scenario screens port
  into MCP-Apps iframes — the Invitation/Decision rendering inside
  ChatGPT/Claude as wedge distribution.
- Boards 07 and 09 are read under this amendment: 07's "frame" = the
  chassis, its "six bodies" = the section vocabulary; 09's opened
  surface = the shared opened-screen chassis with a scenario-designed
  middle.

**Opened-screen laws — RULED 2026-08-30 (founder; board 09's four
proposals, all adopted, #3 amended):**

1. **The still-page law.** An open screen never reflows under a
   reading finger. Instruments update values in place (counts, timers);
   structural change (a person replied, a commitment moved, an option
   added) offers a quiet re-read band — coalesced to one — instead of
   mutating the page. Complement to §11.6: fresh on open, still after
   open.
2. **Instrument never opens immersive.** A live sliver tap hands off
   to the Live surface, which owns live UI. The composition system
   never builds a second live surface.
3. **Chrome = back + Keep, nothing else — with the Keep & send
   amendment.** No share sheet, no overflow; reading gets the whole
   width. Share rides behind Keep AND the two are one gesture: tapping
   Keep offers "Keep & send" in the same flow, so sharing costs one
   tap total and versioning comes free (shared ⇒ versioned is enforced
   mechanically, without taxing the re-invite loop).
4. **The colophon is required** on every opened screen: sources,
   freshness, unknowns, and a corrections door, in mono, at the end of
   the read. Trust Receipts generalized; the unknowns line enforces
   fabrication-closure per screen; the corrections door doubles as a
   standing outcome-capture inlet. Scales down to three mono lines on
   light screens; every line generated from actual provenance, never
   template copy.

**The family split — RULED 2026-08-30 (founder correction, second
weight pass): "Coordination objects are messages; editorial
compositions are pages."** The first Shape Screen draft rebuilt the
operating system at the render layer — seven anatomy parts, viewer
projections drawn as screens, a day-lens, and a single-trip-home mount
that quietly recreated the destination the itinerary demotion had just
killed. Founder ruled it too heavy. Corrected doctrine (board of
record: "10 Chat - The Shape Card", superseding the Shape Screen
draft; external ground: WhatsApp Events = a pinnable card in the chat,
Partiful = one page one link, TripIt = a time-ordered list of
confirmations — the winners at coordination are radically minimal, and
Product Model §2.2 already said structure only as consequence grows):

- **Two families, two weight budgets.** COORDINATION objects — Shape,
  Invitation, Decision, Live sliver, receipts — are CARDS: they live
  in the thread and the well, at message weight, with two zooms (well
  row ↔ card), and never grow a page. EDITORIAL compositions — Story,
  pre-trip Reading, journey reconstruction, guides — are PAGES: the
  full opened-screen chassis (cover, drop cap, colophon, immersive
  scroll). Board 09's chassis is hereby scoped to the editorial family
  only. Things you read get pages; things you coordinate through stay
  messages.
- **The weight law:** if it wouldn't fit in a message a friend would
  send, it's too heavy.
- **The Shape is a card: one read + at most four lines + a stamp.**
  No facepile section (people are a stamp), no next-action band (the
  promise shelf's lead IS the next action), no was/now cells (a change
  is a sentence or a sub-stamp), no lane headers, no door row. There
  is **no Shape destination screen and no single-trip-home mount** —
  the occasion lives in its thread; the card pins to the well.
- **Viewer-relativity survives with zero design:** my card in my
  thread, the group's card in the group thread — provenance decides,
  and there is nothing to switch between. The Whole (host coverage)
  view is CUT, undesigned, until a host actually needs it. The earned
  day-lens is DEFERRED to the trip case. A decision renders as one row
  that opens the Decision card; the Shape never hosts voting.
- **Coordination cards are never Kept** — Keep and the versioned
  manifest belong to the editorial family; a shape is never testimony,
  what happened is (the Story). Live yield, one-commitment collapse,
  recompute-on-read, and provenance-as-viewer all carry over from the
  superseded draft at card weight.

**The itinerary, decomposed — RULED 2026-08-30 (founder; the family
split's complexity stress test; board of record "12 Chat - The
Itinerary, Decomposed"):** "an itinerary" was never one thing — it was
three acts fused into one editable document, and the fusion was the
failure (hence 14 operation types and a 2,000-line screen). The split
assigns each act to the family that already handles it:

1. **"Where do things stand?" → the trip card** — a Shape-card variant
   holding AGGREGATES only, still ≤4 lines + a stamp ("Flights + stays
   hold · 12 reservations · 4 open evenings · Kyoto dinner deciding").
   The card never holds contents, only the shape. A dense day gets a
   **day card** — an outing-scale Shape for that day (the earned
   day-lens reborn at card weight).
2. **"What do we do about Tuesday?" → the thread** — the operational
   itinerary IS the trip's thread: time-ordered commitment, day,
   decision, and receipt cards, with the well pin holding what's
   current. Complexity is absorbed by decomposition in time, never by
   density in space; nobody coordinates twelve days at once — they
   coordinate the next thing. (TripIt's winning insight: an itinerary
   is a time-ordered list of confirmations — which is what a thread
   is.)
3. **"Show me the whole trip" → an editorial page** — the sequence
   body at full height on the board-09 chassis: viewer-relative,
   refreshable, KEEPABLE (reading is editorial, so the trip page is
   the legitimate Keep & send object — "send the trip to your mom").
   Read it; acting routes back through cards. The shipped pre-trip
   Reading is this object's first ancestor; the trip page is the
   editorial family's first citizen after the Story.

Bulk edits ("shift days 3–5") never earn surface ceremony: the agent
performs operations through the ledger that survives beneath; the
person sees a boundary-preview card and a receipt. Named bet,
concentrated not created here: retrieval by asking beats retrieval by
scrolling a grid — "what's Thursday?" returns the day card; if that
bet is wrong, the four-root pivot is wrong, so the itinerary case adds
no new risk. Net new design surface: trip/day cards are Shape-card
copy variants; the trip page is one editorial composition. Zero new
component systems.

**The left-edge ban + the detail mandate — RULED 2026-08-30 (founder,
clarified after a first misreading was briefly codified here; visual
polish is priority one).**

- **BANNED: the accent bar down a card's left edge** — the
  "highlighted card" treatment ("it's the card with the left edge
  highlighted that we are banning"; "reads as a PowerPoint
  component"). A card is bounded by its surface and hairline;
  emphasis comes from REGISTER — the gold wash, type weight, stamps,
  the one gold moment — never from an edge bar. Scope: card-level
  bars on chat/thread card renders. The §11.7 ticket-stub device and
  the well's receipt seam are separately named devices — REVIEWED AND
  KEPT (founder, 2026-08-30): both stand as small devices inside
  containers, distinct from card-level highlighting; do not extend
  them to new card-level uses while this ban stands.
- **The detail mandate** (from the same exchange: "I want it to be
  much more detailed — take a look at the current itinerary"): cards
  render their things with real detail — times, names, subtitles,
  states — in the shipping itinerary's row vocabulary, the polish
  authority: `TripEntry.tsx` (mono 10.5 right-aligned time gutter,
  gold-emphasized for now/held; **serif_medium 17.5/21 titles**; ONE
  arbitrated supporting caption — consequence > schedule > booking >
  place > participants > note; ONE colored state stamp — BOOKED
  planning ink, HELD/PROPOSED gold, CONFLICT oxblood, PICKED sage;
  hairline dividers; done 0.55, skipped strikethrough) +
  `ItineraryChapterHeader.tsx` (daypart mono gold-deep stamps with
  hairline rules + optional serif thesis) + travel connectors.
  Lightness is about structure, never about detail. Board 12 redrawn
  under both rulings same day.

**The zoom gestures — RULED 2026-08-30 (founder; board of record "13
Chat - Breathing"). Cards breathe in place; pages push; nothing
resizes.** Everything collapse/expand/fullscreen means elsewhere,
delivered as three enumerated transitions and zero persistent UI
state:

1. **Cards age into their compact form — collapse is time, not a
   gesture.** A card renders full while current; once superseded or
   the thread moves on, the same instance renders collapsed as its
   existing well-row form (kicker + one line + stamp — the two-zoom
   law reused, no third form). Scrollback becomes a scannable ledger.
   The current instance (the well pin's target) is always full.
2. **Expand is a tap, in place.** Tapping an aged card expands it
   where it stands — no navigation. Still-page compatible: expansion
   is person-initiated. Asymmetry is deliberate: expansion is a
   gesture, collapse is time; nobody manages card sizes. A full
   card's taps are its actions; it does not collapse by tap — aging
   does it.
3. **Fullscreen exists in exactly one form: the editorial page, by
   push (§11.4); back is its only exit, returning anchored.**
   Coordination cards never go fullscreen — "see this bigger" routes
   to asking (day card → the trip page), never a maximize control.
   No pinch, no grips, no user-resizing: density stays CHOSEN-tier.
   PiP already exists and is not draggable — the live sliver,
   system-owned.

- **Provenance-keyed default zoom in group threads:** the asker's
  card arrives full; the same card in the group thread arrives
  collapsed by default (tap to expand). The asker earned the detail;
  the group earned a glance. EXCEPTION: the Invitation always arrives
  full for everyone — its whole job is the first impression.
- **Receipts age fastest** — a receipt collapses on the next thread
  activity; shapes and decisions hold full until superseded or
  resolved.
- **Honesty on re-expansion:** an expanded old card renders ITS as-of
  stamp — history never masquerades as current truth; fresh truth is
  one ask away.
- Never: maximize controls, pinch-to-expand, drag handles, remembered
  sizes, collapse-all, a second minimized-window mechanic.

**The telescope — RULED 2026-08-30 (founder; board of record "14 Chat -
The Telescope"). Semantic zoom as the fifth axis of dynamism.**

- **Every aggregate line is a folded card.** Zoom in = tap a row and
  it unfolds into its child, in place, as a paperDeep inset with its
  own kicker: trip → segment → day → commitment — the experience
  graph's containment tree made touchable. Zoom out = tap the kicker:
  every unfolded child carries its parent's name, so the kicker is
  provenance AND the way home. No new gesture — board 13's
  tap-to-expand generalized from time to hierarchy; no navigation, no
  screens, no tabs; form stays FIXED-tier.
- **Cards arrive at message weight; depth is pulled, never pushed.**
  The weight law governs arrival; pulled depth is person-initiated,
  ephemeral, and folds back on aging. Nobody ever receives a
  twelve-day tree.
- **One unfolded child per level (the accordion rule).** Opening
  Kyoto folds Tokyo; opening Tuesday folds Monday. The kicker spine
  always shows where you are; "everything at once" stays the trip
  page's job. Three paths, one set of cards: the telescope WALKS, the
  page READS, asking JUMPS.
- **At live, time does the zooming:** the current day is the
  system-unfolded level.
- **Reading posture only:** actions stay on the card that owns them
  (vote on the Decision card, correct via the colophon). The
  telescope never becomes an editing tree — that would be the Change
  Studio reborn.
- Generalizes for free to any parent/child in the graph (occasion →
  commitments, settlement → lines): one mechanic for every hierarchy.
- Net: the system is dynamic along five axes — content, register,
  time, viewer, depth — and static along exactly one, form, which is
  what keeps the five legible.

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

### 11.10 Second aesthetic recovery batch — RULED 2026-08-30 (founder)

A close re-read of the pre-pivot project (including its unmined rhythm
study, "Places — Whole Pages": one page drawn eight ways, A–H) yielded a
second batch, all applied to the boards same-day:

1. **The header rule is chrome, everywhere**: `TITLE ——— count →` (mono
   label, trailing hairline, count/door carried in the header line).
   Shipped code (`headingRule`, PlacesAtoms.tsx:70 +
   ItineraryChapterHeader); now the 12th shared instrument. Fires at
   chapter/region openers only — inner-unit kickers stay bare.
2. **Rhythm is two-tier and per-root** (code-verified in layout.ts):
   Home regions run **variant B family rhythm, ruled in** — tight
   within a region (14–20), 44 between regions, header rules at region
   boundaries only. Places states run the **32 chapter beat** (their own
   shipped rhythm; the earlier flat 24 was under-canon for Places).
   Live Reduction deliberately keeps the compressed 24 — urgency
   compresses. `headingToContent` 8, `ledeToFirstSection` 12.
3. **The act break** (cardStackRhythms, locked 08-02): body→CTA is the
   intentional break and must outrank title→body — 12–16, never the
   in-card gap.
4. **Media texture split sharpened**: soft warm **blob** = the real,
   committed, photo-bearing thing (a booked occasion, a settling
   import); gold **hatch** = possibility/illustration; **grid** = map;
   **scrim cover** = editorial. One hatch for everything was texture
   monotony.
5. **Masthead at full scale**: the world read is serif 30/34 (−0.01em)
   with a 12.5/17 ghost condition sub at margin-top 7 — the pre-pivot
   mast spec. Both Home postures carry the sub.
6. **The rest register**: pages end, they don't stop — a centered serif
   close + ghost stamp (46px air) after the last section. On Home it
   closes the day honestly; on the World Field it states the
   count-toward law ("The field is finite. This is all of it today.").
7. **The compression law** (degradation compiler): compression shrinks
   media and drops the note; small plates stay — a row without its
   plate is a different composition, not a quieter one.
8. **Tally register** adopted as board furniture only; its product home
   is Life — rule it there. **Lens strip** consciously not recovered —
   superseded by the typed-edges ruling.

### 11.11 Component parameter consolidation + the board kit — 2026-08-30

Third same-day pass, component-level. Audit findings and fixes:

1. **Door-law sweep**: seven gold *chevrons* had crept onto the boards
   ("Open Red Hook ›", "Europe, in Life ›", "All plans and occasions ›"
   …) — a direct §11.1 violation the app already gates
   (`doorContract.test.ts`, GOLD_CHEVRON_COUNT=0). All seven now carry
   the arrow-forward. Boards and code agree again: gold + arrow = door;
   chevron is the ghost row affordance only.
2. **Identity ladder ruled**: facepile avatars **22 / tuck −7** (the
   codified 22 / tuck .34); single identity **32**; group-as-subject
   **40**; region plate **56**; the dashed chair matches its pile's
   size. Previously scattered across 24/26/28/30/34.
3. **One crown lift**: `0 6px 18px + 0 1px 3px` — the specimen sheets
   ran a second, lighter spec.
4. **The board kit exists**: `_kit/board-kit.css` in the Design project
   (mirrored beside the working boards) — the §3.1 ramp, §11 laws,
   containment physics, media textures, identity ladder, door SVGs, and
   the rest register as copyable classes with the rulings quoted in
   comments. New boards start from the kit; a value outside it is a
   defect unless ruled in. This is the anti-drift mechanism for board
   authoring, mirroring what the ratchet tests do for code.

### 11.12 The phase-2 composition amendments — RULED 2026-08-30 (founder)

The three proof compositions (C1 ordinary week · C2 multiplayer Occasion
· C3 longitudinal thread) closed with zero new kinds spent in
composition and R1–R7 confirmed; the founder then judged the sparse and
full Quiet boards side by side and ruled for fullness. The consolidated
amendments, landing here as the single canon-alignment pass:

1. **R1–R7 ratified as ruled** (people-as-reservoir; posture/modifier
   split; orientation contract; Quiet's returns; large-type-by-dominance,
   amending §11.7; the personalization split; the casual register).
2. **The orientation ladder** (C1-F3, final R3 text): Home opens with
   its most valuable true orientation; the serif read is the default
   expression, and *its scale tracks the evidence's scale* — the
   two-line mast (30) when interpretation converges, one line (22) when
   only world truth is known, direct state (17) when there is nothing
   to interpret. This supersedes any mandatory reading of §11.6.1;
   the read is never revoked, only scaled honestly.
3. **Demand and richness are different axes — the Quiet floor.** The
   demand laws (zero open decisions in Quiet, complete-on-view,
   scroll-past is an ending) constrain demand, not content. Quiet is
   the modal state of the primary interface; a page that proves
   "nothing here" teaches people not to open it. Ruled floor: the read
   at ladder scale + the week's shape + consumable returns
   (quality-gated, not count-capped — each must beat silence
   individually; none may be manufactured). Fullness comes from the
   world and the person's own held life — time-shape, texture,
   receipts, reading — never from Vesper performing its repertoire.
   R4's original "at most one return" wording is superseded.
4. **The admission question, broadened**: "materially worse without it"
   includes legibility and being-held, not only missed tasks.
5. **`week_shape` joins the Home union** (canon event, drawn on the
   Quiet-full board): the seven-day strip at containment step 3 — a
   diagram, not an object; zero demand. The old canon's day-strip
   primitive finally has a user.
6. **A Move always ships with its basis** (C3-F12): an unexplained Move
   is inadmissible; the why-this trail renders inline.
7. **The unwind doctrine** (C3-F14): contributions retract; occurrences
   don't. Artifacts unwind across every hop with their provenance;
   other people's own things — their photos, their evenings, their
   experience — are never taken back.
8. **The unattributed-aggregate law** (C2-F6): private constraints shape
   shared objects only in aggregate, and the aggregate never enumerates.
9. **Renamed for honesty**: `now_route_instrument` →
   `now_commitment_instrument` (C1-F1) — the subject is the owned
   commitment; a route is one form its preparation takes.
10. **The carried-forward receipt is promoted** into the receipt union
    (fourth independent derivation) and the **execution ledger** joins
    the shared instruments (C3-F11): the prepared → authorized →
    attempted → partial/failed/unknown → readback → repair → receipt
    chain as one renderable carrier.

### 11.13 The §7 close-out batch — RULED 2026-08-30 (founder)

The manifest's §7 queue is emptied. Six rulings:

1. **Two kinds in, one deferred**: `live_branch_field` (recovery
   register only — ordinary Live keeps exactly-one fallback, settling
   the singular/plural conflict) and `people_status_aperture` (already
   wave-0-accepted; a people-reservoir kind). The layered-Place-passage
   instrument is deferred until a composition demands it — three
   complete compositions never did.
2. **Vocabularies adopted, kinds refused**: focus_verdict carries the
   anatomy's six registers and the horizon doors the seven path types
   (type spaces, rendered by existence gate); `human_mode` folds into
   R2's modifier vocabulary. No Home social carrier (covered by R1);
   availability/reunion openings are Move content; **generated-vs-
   curated is a provenance label, never a union axis** — producer lanes
   do not earn kinds.
3. **`path_next_rows` ≤2** — the stricter number; widening later takes
   evidence, narrowing a shipped habit takes a fight.
4. **Urgent's suppressor semantics**: oxblood register; one recovery
   dominant; the read drops to direct state (the ladder's floor);
   everything below collapses to `week_shape` + critical in-motion rows;
   horizons and continuity yield entirely; the rest close is replaced by
   the **"what stays held" line** — suppression without reassurance
   reads as data loss. Drawn as the Home · Urgent board.
5. **R2 is ratified without the three-posture strip** — four postures
   have now rendered on one architecture; the escape clause stands: a
   posture demanding different architecture revisits clause 2
   explicitly, never quietly.
6. **Evidence-driven triggers replace dates**: tab-bar icons commission
   at the first device-visible shell increment; the Lamplight night
   register waits for real night usage in dogfood.

Score after this batch: 65 kinds + 13 instruments → 14 EXISTS ·
30 ADAPT · 33 BUILD. The open-questions ledger for Home & Places is,
for the first time, empty of ruling-shaped items.

### 11.14 The authority docket — RATIFIED 2026-08-30 (from response doc §11)

A post-alignment source audit found ten authority/epistemic boundary
violations in the phase-2 fixtures, all marked "pass" by their own
findings boards. All ten corrected on the source boards; ratified here
as surface laws (most restate the contribution contract; the boards
proved restating was necessary):

1. **Preparation is not execution; naming people does not contact
   them** (P1). One constitutive authorization sends, with the exact
   audience shown first.
2. **Unknown ≠ compatible** (P2). Nonresponse never becomes inferred
   agreement; shared objects say "every *known* limit."
3. **Human claims are claim-scoped** (P3, P10). Business relationships
   widen world facts, never a person's judgment; "the menu lists it" is
   Vesper's lane, "trust me on it" is only ever theirs.
4. **May-relay is its own grant axis** (P4). Attribution preserves
   provenance, not permission; a new audience needs the author's yes.
5. **Retention needs a keep** (P5). Bringing something into Chat grants
   immediate use, not durable residue; without a keep gesture it
   expires with the turn.
6. **Occurrence ≠ affinity** (P6). Behavior proves what happened; only
   the person authors preference, rotation, and meaning.
7. **No product self-narration** (P7). "It settled itself" is not a
   return; after a coordinated evening, silence is.
8. **Propagation-boundary honesty** (P8) — *precision amendment to
   §11.12.7*: withdrawal invalidates every governed artifact,
   projection, and learned signal and stops all future resurfacing; it
   cannot unread what was already read or erase external deliveries,
   and the receipt states that boundary instead of promising erasure.
9. **Availability is purpose-scoped** (P9). Another person's calendar
   or availability is usable only through the permission and purpose
   that supplied it.
10. **Implementation hold — LIFTED 2026-08-31 (founder re-review).** The
    corrected fixtures passed: C2/G8, C3/G9, and C3/G16 promoted to PASS;
    C3/G14 stays deliberately not-exercised and C3/G19 deliberately
    partial in their proper labs. The blanket hold is replaced by
    **contract-bounded implementation scope**: the grant store,
    retention, relay, Outcome inference, and projector invalidation may
    build strictly within the C&C five axes, the receipt union, the
    projection envelope, and the unwind doctrine as drawn — nothing
    beyond what the accepted boards and contracts specify. Semantic
    canvas work is closed; the next phase is native interaction and
    real-data validation.

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

5. **Oxblood single-meaning law — RULED 2026-08-31 (founder), from the
   Life program's interim ruling (production spec §5f / correction brief
   §10.3).** Oxblood means exactly one
   thing across every root: **a live threshold in the world** (urgency
   StatusMeta, map constraint, live-position rings). It never marks
   destruction: destructive verbs (delete, withdraw, revoke, leave)
   render in plain ink with a plain confirm — "one color must not mean
   both 'act now' and 'destroy.'" Boards audited 2026-08-31: no
   Home/Places board uses oxblood on a destructive control; the Vault's
   oxblood deletion door is the Life program's to correct.

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
Added 2026-08-30: the §11.8 amendment — "surfaces select; screens
adapt; content composes" (boards 07 amended, 09 "The Immersive
Density" renumbered from a colliding 08). Scenario screens replace
"generated artifacts"; the frame becomes the chassis, the six media
the section vocabulary; true medium choice confined to chat answers
(resolver ratification exits the artifact critical path — note this
narrows the taxonomy's "first concrete consumer" above to designed
slot selection, which needs no ratified resolver); the six-capability
artifact runtime made first-class; external placement recorded from
two primary-source research passes (industry static/declarative/
open-ended taxonomy; MCP Apps / Apps SDK / A2UI convergences; Gemini
Dynamic View located as answer-lane-only counter-example; sandboxed
GeneratedView hybrid as the sole escape valve).
Added 2026-08-30: opened-screen laws ruled (§11.8; board 09's four
proposals all adopted, chrome amended to Keep & send one-gesture) —
still-page, instrument-never-opens-immersive, back+Keep chrome,
required colophon. Board 09 no longer carries proposals; the Shape
screen board designs against settled chassis law.
Added 2026-08-30 (second weight pass): the family split (§11.8) —
coordination objects are messages (cards, two zooms, thread + well,
never Kept); editorial compositions are pages (the board-09 chassis,
now editorial-only). The Shape Screen draft superseded by "10 Chat -
The Shape Card"; no Shape destination screen, no single-trip-home
mount; Whole cut undesigned; day-lens deferred; weight law = "if it
wouldn't fit in a message a friend would send, it's too heavy."
Added 2026-08-30: the itinerary, decomposed (§11.8; board "12 Chat -
The Itinerary, Decomposed") — three acts, three homes: glance = the
trip card (aggregates, ≤4 lines), coordination = the thread as the
operational itinerary (day cards; decomposition in time), reading =
the trip page (editorial, Keepable). Bulk edits via ledger + boundary
preview + receipt; retrieval-by-asking named as the concentrated bet.
Added 2026-08-30: the zoom gestures (§11.8; board "13 Chat -
Breathing") — cards breathe in place (age-to-compact by time,
tap-to-expand in place), pages push (§11.4, the only fullscreen),
nothing user-resizes; provenance-keyed default zoom in group threads
(invitations exempt — always full); receipts age fastest; re-expanded
history renders its own as-of stamp.
Added 2026-08-30: the telescope (§11.8; board "14 Chat - The
Telescope") — semantic zoom as the fifth dynamism axis: every
aggregate line is a folded card (trip→segment→day→commitment, in-place
paperDeep insets, kicker = the way home); depth is pulled never
pushed; one unfolded child per level; at live, time does the zooming;
reading posture only. Five axes dynamic, one (form) static.
Added 2026-08-30 (polish audit): §11.7 card-physics correction entry
(code wins — radius semantics outer-16 / inner-12, padding 14×16 / row
8) and the BOARD RHYTHM KIT adopted for design boards: inside 1:1
mockups the app floors apply (mono ≥10 ls 1.3, serif ≥15 — sub-floor
serif triages to sans at the same px), hairlines only 0.10 / 0.06,
soft body ink = ink40 #3C352E (the #4A4339 that circulated on boards
was never a token), supporting captions 11.5, time gutters 36/30,
section gap 24. Board furniture (rail tags, fold markers, timestamps,
footers) is annotation and exempt. Boards 07 + 09–15 normalized
same day; the 00–06/08 set inherits the kit on the fork's next pass.
Added 2026-08-30 (closing pass, founder approvals): KEEP ELIGIBILITY
RULED — a composition may be Kept only on share-or-keep intent
(anything shared is automatically versioned; nothing self-saves);
scoped by the family split to editorial pages only (Reading, Story,
reconstruction, the trip page). This closes §11.8's last open call —
the workbook's "which generated compositions earn saved identity" is
now answered. Also ruled: the ticket-stub and receipt-seam edge
devices reviewed and KEPT (see the left-edge ban block); the Story
share-flag flip approved (the re-invite bet's live test, and the Keep
& send gesture's first carrier); Wave-1 coordination build
green-lit (OccasionCapsule writer → Brief producer → conformance
fixes). Resolver job-taxonomy ratification remains deliberately
parked (answer-lane only); PLAN_SHAPE flag mooted by the family
split.
Added 2026-08-30: THE VOICE SPLIT RULED (closes board 03's residual
open) — **Home states what matters; Chat states what it can do about
it.** The two reads never say the same thing twice: Home's Now read is
the world's sentence ("Storms this afternoon. Saturday opens
clearer."); Chat's read line is the agency sentence ("Maya moved
dinner. The rest can keep." / "Nothing needs you."). One voice, two
postures — witness vs workshop. Also: board 16 "The Editorial Family"
opened — the Story page + shipped-Reading conformance audit against
the opened-page laws, with two PROPOSED rulings pending founder pass:
(a) EDITIONS — a system-persisted composition (the T-7 Reading)
renders AS its dated edition with a see-it-fresh door, the
Kept-renders-as-kept rule extended to pushes; (b) FUTURE OPENINGS
belong to Home's Horizons, and appear in Chat only as promise-shelf
leads (an opening is an invitation to ask), never well rows or pushed
cards — consistent with the well's non-urgent-proactive exclusion.


## Palette ruling — oxblood scope (RATIFIED 2026-08-31, founder)

Oxblood `#7A2E2E` belongs to the **live-threshold / urgency register
only** ("act now in the world"). It is never a destructive-action color:
destructive verbs (delete, revoke) render in plain ink with their glyph,
and destruction's gravity is carried by the confirmation flow (friction +
honest disclosure of what leaves now, what expires later, and what cannot
be revoked). Rationale: one color, one meaning — "act now" (approach) and
"destroy" (avoid) are opposite postures and must not share a hue; the
non-color-state accessibility law already forbids destructive-by-color-
alone; and a second near-identical red is exactly the drift this kernel
exists to prevent. Origin: Life correction brief §10.3; interim applied
2026-08-31 across the Vault family and swipe grammar, now final.
