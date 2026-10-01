---
doc_type: working
status: active
owner: Claude orchestrator (product map)
created: 2026-09-26
expires: 2026-10-26
why_new: Inventories every Vesper Claude Design project, classifies which are current or superseded, maps how they succeeded one another, and records which legacy ideas survived, were rejected, or were orphaned, so the founder can clean up the project list and recover lost ideas.
promotes_to: null
supersedes: []
---

# Design atlas: legacy and superseded Claude Design projects

Read-only inventory, 2026-09-26. Nothing in Claude Design or in any repository
was changed. Every cleanup item below is a recommendation.

## 0. Scope, method and evidence limits

**What was listed.** `list_projects` returned exactly 20 projects. It does not
return everything. The July living-canon project **Vesper** (`551f400f`) opens
through `get_project` and `list_files` but is missing from the list. Three
further projects exist only as local exports in `~/Downloads`, and their live
IDs are not recorded anywhere in the repositories. The count of 20 is either a
cap or an ownership filter. Treat the register in §1 as "at least 24 projects".

**Dates.** File etags are microsecond Unix timestamps. I converted them to New
York time (EDT). "First" is the earliest surviving file etag, not a true
creation date, because files are rewritten. "Last" is the latest file etag.
Project type and sharing come from `get_project`.

**What I read.**

- Prior catalogs in the 7e6d4384 scratchpad:
  - `foundations.md` for the Kernel Lab and Home & Places
  - `life-plans.md` and `notes-docs.md` for Life & Anchors
  - `chat-you.md` for the August Chat and You history
  - `social.md` for Social Aperture
  - `home.md` and `places-entity.md` as a proxy for current project contents
- Text I extracted myself:
  - Home Surfaces: the local Aug 9 export, plus live fetches of Build Manifest, Trips — Prototypes and Receipt Gaps
  - You & Trust: the local Aug 12 export, which is current
  - Old Home `03538beb`: the live 00 Index
  - The Social Aperture stub `739de9aa`: the live 00 Read Me
- Downloaded HTML was stripped to text in memory. No HTML was saved. No serve
  URL was written to any file.
- Repository documents are cited by path.

**Evidence limits.**

- Boards are static fixture compositions. No project holds participant
  evidence.
- Some August boards are templated (`{{ }}`), so text extraction loses their
  data.
- I rendered no boards.
- "Survived" means the idea appears in a current project or in canon. It does
  not mean it is built.
- For the 11 active projects I relied on other researchers' catalogs rather
  than re-reading every board.

---

## 1. Project register

Legend:

- **Role:** active target · reference (live dependency) · superseded predecessor · archive · accidental duplicate
- **Recommendation:** keep active · freeze as reference · archive · delete-candidate

### 1a. Active set (one line each; covered in depth by other researchers)

| Project | ID | Type, sharing | First → last | Boards | Role | Predecessor | Recommendation |
|---|---|---|---|---|---|---|---|
| Vesper — Home | `42876b8c` | project, private | 09-06 → 09-26 | 28 current (00–24, 08b, 08c, 09b); 6 "Before VDL 0.3"; R1–R4 references (same-size copies of Home & Places canon boards); Z1–Z4 baselines; 4 components | active target (Home) | `03538beb` ← Home & Places ← Home Surfaces | keep active |
| Vesper — Places | `516a3ea4` | project, private | 09-07 → 09-21 | 11 boards, 10 components, `before/` | active target (Places) | Home & Places Places boards; Home Surfaces "Places — The Page" | keep active |
| Vesper — Entity Object Handoff Lab | `dd48304b` | project, private | 09-02 → 09-15 | 18 boards, Z1–Z5 archive, 10 components | active target (place and object page) | Home & Places "Place Focus" | keep active |
| Life | `e72a2fd2` | project, **org/team, comment** | 09-06 → 09-21 | 18 boards, 3 components | active target (Life) | Life & Anchors | keep active; rename to "Vesper — Life" for consistency |
| Vesper — Plans in Real Life | `cd2e1f82` | project, private | 09-04 → 09-15 | 16 boards, 13 "Before shared package" copies | active target (Plans) | Home Surfaces Trips; Kernel Lab F1–F4; Home & Places C2 | keep active |
| Vesper — Multiplayer Shapes | `caf916f9` | project, private | 09-20 → 09-26 | 12 boards | active target (social) | Social Experience ← Social Aperture | keep active |
| Vesper — Social Experience | `3ef10868` | project, private | 09-07 → 09-21 | 12 boards, 3 before-copies, R1–R12 references | active, and partly superseded by Multiplayer Shapes rulings (Sep 20–23) | Social Aperture | keep. Add a note that Multiplayer Shapes wins where they conflict |
| Vesper — Chat (September 2026 Exploration) | `096be8ed` | project, private | 09-12 → 09-14 | 10 boards, plus `record/` and `kernel/` | active target (Chat; "Chat, decided" 09-14) | Chat (Aug) `a06d5cb9` | keep active; consider dropping "Exploration" from the title now that it is decided |
| Vesper — You, Identity & Trust (Sept 2026 exploration) | `b66c82a5` | project, private | 09-12 → 09-14 | 6 current (0-0 to 0-5), 35 history, 9 components | active target (You) | You & Trust (Aug) `78e0a36c` | keep active; same title note |
| Vesper — Design Language Workbench (Stage 1) | `c13ae951` | project, private | 09-10 → 09-14 | 17 boards, 25 S2 instrument specimens, 9 components | active (shared visual language, Stage 1 and 2) | Kernel Lab (behaviour); Home & Places instruments | keep active |
| Vesper · Production Kernel | `fc85e38a` | **design system, org default, org edit** | 07-25 → 09-10 | 9 cards, guide, tokens | active (primitives only) | — | keep active. Last re-sync was 09-10, and its component layer is still empty (VDL §15.3) |

### 1b. Legacy set (my scope)

| Project | ID | Type, sharing | First → last | Boards | Role | Successor | Recommendation, with reason |
|---|---|---|---|---|---|---|---|
| **Vesper** (July living canon) — *not returned by list_projects* | `551f400f` | project, **org/team, comment** | 07-08 → 08-12 (oldest uploaded module 06-05) | about 89 root pages and 200+ `.jsx` modules, plus `archive/`, `scraps/`, `uploads/` (66 pages and 215 modules on 07-29) | archive: the pre-pivot root of every lineage | Home Surfaces, You & Trust, Chat Aug, Life & Anchors, CAL, Onboarding | **Archive and freeze.** The VDL (09-10 §15.2) calls it "now historical". Its `CLAUDE.md` Home rules "predate current direction and are not authority". Its web components (`buttons.jsx`, `row-system.jsx`, `vesper-tokens.jsx`…) could seed the empty kernel component layer. Do not delete. |
| Vesper — Home Surfaces | `f4eee076` | project, private | 08-05 → 08-13 | 13 (the 12 in the Aug 9 export plus "Receipt Gaps — Cross-Surface", 08-11/13) | **reference with a live dependency.** It is the hash-pinned "August composition authority" for the shipped legacy Trips home and Places workspace. It is design history for post-pivot work. | kernel extraction (08-29); Home & Places; Plans; Places | **Freeze as reference.** Do not archive while `docs/governance/home-surfaces-design-authority.json` is `active` and `scripts/check_home_surfaces_governance.py` enforces it. The production build still ships these legacy surfaces. |
| Vesper — You & Trust | `78e0a36c` | project, private | 08-10 → 08-12 | 9 | **reference with a live dependency.** `Profile System — Canonical Screens` is the "approved artboard" for the shipped `/you` portrait (`travel-app/docs/surfaces/profile-system/contract.md:53`) | You Sept `b66c82a5` | **Freeze as reference** until a You decision supersedes the 2026-08-10 profile decision; then archive |
| Vesper - Home & Places | `a26e3228` | project, **org/team, comment** | 08-29 → 09-04 | 66 | superseded predecessor that also holds the accepted-canon record. Its "Vesper Root Boards" canvas is still cited as the semantic render authority by the `home-root` and `places-root` contracts. | Home `42876b8c`; Places `516a3ea4`; Entity `dd48304b`; Workbench (instruments) | **Freeze as reference.** Do not delete. MP0–MP6, both 09-02 critiques, the Brainstorm and HP 09-04 exist only here: the repo archive of 08-31 predates them |
| Vesper — Life & Anchors | `f524c7f0` | project, **org/team, comment** | 08-29 → 09-06 | 120 boards plus a `Canvas` stub and `fixtures/` | superseded predecessor and archive. Its own 00A front door classifies every board; the successor manifest lists roughly 60 boards as "archive-only (never transferred)" | Life `e72a2fd2` | **Archive (freeze).** Add a successor banner. Do not delete: archive-only boards, decisions (08-30, 09-05) and active working docs cite it as evidence |
| Vesper — Chat (August) | `a06d5cb9` | project, private | 08-29 → 08-30 | 17 | superseded predecessor. The 09-12 brief declared its composition doctrine superseded | Chat Sept `096be8ed` | **Archive.** Rename to show the date. It is a behaviour and idea donor only |
| Vesper — Interaction Kernel Lab | `6dd8b450` | project, private | 08-31 → 09-04 | 23, plus README and an executable runtime (`lab-state.js`, `fixtures.js`, `derive-f.js`, 60 replay scenarios) | reference: "behavior donor only, not canon" (VDL 09-10 §15.2) | kernel §11.15; Plans; Workbench | **Freeze as reference.** Its runtime is the only executable behaviour oracle in the design corpus (see §4) |
| Vesper - Social Aperture | `fac2051b` | project, private | 09-02 (18:26 → 21:37) | 13 | superseded exploration ("provenance… not a reason to reopen the accepted root split", SE brief 09-07) | Social Experience → Multiplayer Shapes | **Freeze as reference.** Its pin decision record still disagrees with later rulings (§5.2) |
| Vesper Social Aperture (no hyphen) | `739de9aa` | **design system (mistake), org/team, comment** | 09-02 18:05 only | 2: an early Read Me and a same-size copy of Brainstorm | accidental false start, created 21 minutes before `fac2051b` | `fac2051b` | **Delete-candidate.** Its only unique content is an earlier Read Me draft, and the design-system type may confuse design-system pickers |
| Vesper — Home (old) | `03538beb` | **design system (mistake), org/team, comment** | 09-04 → 09-05 | 14 (00–09, Z1–Z4) | retired. "created as a design-system project by mistake and is retired" (`decisions/2026-09-05-home-borrows-life-pass-grammar.md:21`). Moved to `42876b8c` on 09-06. **Its own 00 Index still presents itself as current** and has no retirement banner | Home `42876b8c` | **Delete-candidate after a snapshot.** Z1–Z4 have identical file sizes in `42876b8c`. Boards 00–09 are the 09-05 intermediate state, superseded by later revisions and by the ledger on `42876b8c` 07. Until deletion, rename it and remove org sharing. Two projects in the org already share the title "Vesper — Home" |

### 1c. Export-only projects (live project not found; IDs unrecorded)

| Export (in `~/Downloads`) | Export date | Boards | Role | Recommendation |
|---|---|---|---|---|
| Vesper · Conversational Artifact Language (v2–v2.1.1) | Aug 13–14 | 17 (00 Overview … 16 Decision Log) | superseded Chat-transcript artifact language. A copy is checked in at `travel-app/docs/surfaces/vesper-chat/design-refs/artifact-language-v2.1.1/`. The Kernel Lab handoff says "do not import" it as interaction authority | Find the live project, then archive it. Chat Sept's CardBlueprintV1 (record/26) is the current card grammar |
| Vesper — Onboarding & First-Value Experiments | Aug 12 | 5 (Organic fragment-first; Share into Places; Invite post-join payoff; Home City local first value; Universal mixed-initiative aperture) | **orphaned lineage.** No live successor project exists. `claude-design-onboarding-reconciliation-handoff-2026-09-12.md:18` still says "Continue in `~/Downloads/vesper-onboarding-first-value-experiments-aug-2026`" | Decide the onboarding owner (§4, item 11) |
| Evening star design exploration | Jul 25 | 2 (identity mark, symbol category) | brand identity, outside the product lineage | Keep with brand material |

---

## 2. Design lineage

### 2a. Lineage by root

```
PRE-PIVOT                                PIVOT FOUNDATION (08-29 → 09-04)          CURRENT (09-04 →)
Vesper 551f400f (Jul 8–Aug 12)
 ├─ Trips Home, Stack Model ─┐
 ├─ Places Core/Feed ────────┼─► Home Surfaces f4eee076 ─► [kernel extraction 08-29]
 │                           │    (Aug 5–13)                   │
 │                           │                                  ├─► Home & Places a26e3228 ─► Home 03538beb ─► HOME 42876b8c
 │                           │                                  │    (08-29–09-04)             (09-04–05, retired)   (09-06→)
 │                           │                                  │     ├─ Places boards ───────────────────────► PLACES 516a3ea4 (09-07→)
 │                           │                                  │     ├─ Place Focus ─────────────────────────► ENTITY dd48304b (09-02→)
 │                           │                                  │     └─ MP0–MP6 + Brainstorm ─┐
 │                           └─ Trips Prototypes ──────────────►│──────── Kernel Lab 6dd8b450 F1–F4 ──► PLANS cd2e1f82 (09-04→)
 ├─ Atlas / Post-Trip ───────────────────────────────────────► Life & Anchors f524c7f0 ────────────► LIFE e72a2fd2 (09-06→)
 │                                                               (08-29–09-06)   └ 17-family ─┐
 ├─ Vesper Home Workbench / Chat ─► CAL (Aug 13–14, export) ─► Chat a06d5cb9 (08-29–30) ─────► CHAT 096be8ed (09-12→)
 ├─ Profile / Trust & Controls ──► You & Trust 78e0a36c (Aug 10–12) ─────────────────────────► YOU b66c82a5 (09-12→)
 ├─ Vesper Onboarding ───────────► Onboarding experiments (Aug 12, export) ─────────────────► (no successor project)
 └─ (social: follow graph, stories)            Social Aperture 739de9aa→fac2051b (09-02) ◄──────┘
                                                  └─► SOCIAL EXPERIENCE 3ef10868 (09-07) ─► MULTIPLAYER SHAPES caf916f9 (09-20→)
Production Kernel fc85e38a (07-25 →, design system) ◄── kernel extraction; VDL 09-10 ─► WORKBENCH c13ae951 (09-10→)
```

### 2b. Dated steps and the rulings that moved each one

| Date | Step | Ruling or event that governs it (source) |
|---|---|---|
| 07-08 → 08-12 | **Vesper** `551f400f` is the single living-canon file for Trips, Places, Vesper Home, Atlas, Profile, Onboarding and Chat | 07-29 consolidation found 66 pages and 215 modules, 214/215 reachable, with the three audit scripts RED (`docs/working/design-file-consolidation-2026-07-29.md`) |
| 07-25 | Production Kernel created (design system, org default) | — |
| 08-05 → 08-13 | **Home Surfaces** splits Trips and Places into "One vocabulary, three tabs" (the containment scale, the evidence union, the role split) | 08-06 shared model; 08-07 canon "still canon for vocabulary · not for state"; **08-09 authority record** (`docs/governance/home-surfaces-design-authority.json`); 08-11 manifest re-verified; 08-11/13 Receipt Gaps audit |
| 08-10 → 08-12 | **You & Trust** (portrait and settings hybrid) | 08-10 profile decision; 08-11 canonical screens approved, and screen 01 shipped to `/you`; 08-12 "What Vesper reads" removed; the Projections board stamped SUPERSEDED |
| 08-12 / 08-13–14 | Onboarding experiments; Conversational Artifact Language v2.1.1 | Onboarding brief 08-12; CAL briefs 08-13/14 in `travel-app/docs/working/` |
| 08-27 | Pre-pivot recovery: "calm is not absence" | `home-surfaces-pre-pivot-recovery-and-post-pivot-direction-2026-08-27.md` §11 (recover, revise, retire) |
| 08-28 | The pivot: four product moves | `decisions/2026-08-28-adopt-four-product-moves.md` |
| 08-29 | Kernel extraction turns the Home Surfaces vocabulary into the root-agnostic kernel. The bundle becomes "design history, not authority". **Home & Places, Life & Anchors and Chat (Aug) are all created that evening** (19:06, 19:09, 21:22). Life & Anchors picks the Pass anchor: "A is what I was looking for" | `design-kernel-extraction-2026-08-29.md` §1 and §11.10; Life & Anchors 01A/01B/01C |
| 08-30 | Home and Places consumer anatomy adopted. Life anatomy adopted. Home & Places pruned (deleted boards survive only in `docs/design-archive/root-boards-2026-08-30/`). Chat rulings: family split, Shape card, Telescope, Breathing | decisions 08-30; Chat 00 State of Play |
| 08-31 | Home & Places semantic phase closed; accepted bundle archived. Kernel Lab V1 → V2 | `design-archive/root-boards-2026-08-31-accepted/` |
| 09-01 | Kernel Lab zoomed-out review: "keep the kernel, narrow its authority, put value return before it". D-47–D-49 delegated. Life behaviour sequences ruled | IKL 91; `interaction-kernel-lab-zoomed-out-…-2026-09-01.md` |
| 09-02 | Home & Places critiques (Cards and Instruments; Aesthetic Pass); MP0–MP6; Brainstorm. **Social Aperture**: false start `739de9aa` at 18:05, real project `fac2051b` at 18:26; pin working decision. Entity Lab created | `pin-as-ambient-unit-working-decision-2026-09-02.md` |
| 09-04 | HP 09-04 value pass; Kernel Lab V2.3 F1–F4; **Plans** created; **Home `03538beb`** created (design-system type by mistake) | integration brief 09-04 |
| 09-05 | Amend Home canon (containment means a coherent object; a conditional people region; four type roles). The Plan in seven sentences. Home borrows Life's pass grammar. Crown arbitration | decisions 09-05; kernel §11.15–11.16 |
| 09-06 | Consumer strategy reconciled (booking and provider execution retired). **Home moved to `42876b8c`. Life `e72a2fd2` distilled from Life & Anchors** (00A verified 09-06) | decisions 09-06; Life manifest 09-06 |
| 09-07 | **Places** and **Social Experience** created. The Places response marks the Home & Places specimen sheets and Home Surfaces' "The Page" (Aug 8) as "Historical, not current" | `places-complete-experience-design-response-2026-09-07.md:475` |
| 09-08 / 09-09 | Five-project consolidation. Home compared against Home Surfaces "Trips — The Page", which added three kinds (trip-day strip, work receipt, money row). Design convergence selected | `claude-design-home-artifact-led-visual-value-response-2026-09-05.md` §12; decision 09-09 |
| 09-10 / 09-11 | VDL: Kernel Lab is a behaviour donor only; July Vesper is historical. **Workbench** created. The repo snapshot `design-language-2026-09-11` holds 6 products and the workbench, **but no legacy projects** | `vesper-shared-design-language-consolidation-2026-09-10.md` §15.2 |
| 09-12 → 09-14 | **Chat Sept** and **You Sept** created ("explore a new experience, not an old portrait patch"). Chat decided 09-14; You r2/r3 rulings 09-13/14 | `claude-design-you-trust-new-project-exploration-handoff-2026-09-12.md` §1, §8 |
| 09-20 → 09-26 | **Multiplayer Shapes**. Its Sep 20–23 rulings supersede Social Aperture's comment kill and its "This was useful" receipt | `social.md` B1–B2 |

---

## 3. Legacy projects: what survived, what was rejected, what was orphaned

For each project, **Survived** names where the idea lives now. **Rejected**
gives the reason. **Orphaned** lists good ideas that were neither carried nor
explicitly rejected. Board references are `Project:board`.

### 3.1 Vesper (July living canon, `551f400f`)

This project is outside the brief's named list but is the ancestor of all of
them, so it gets a summary.

- **Survived.**
  - Its tokens and type contract became `travel-app/constants/*`, which feeds the Production Kernel through `scripts/design_kernel_export.mjs`.
  - Its Trips Home Stack Model's six-part temporal argument (Stack · Companion · The Table · Your People · Connect · Trail) was recovered on 08-27 as "present → future → past" and "stable anatomy, variable existence".
  - The Vesper Home Workbench's "Trips owns objects; Vesper owns sessions" became Chat's ownership line.
  - The Places card-family work (uncarded candidate, verb as a control) became `cardSurface.ts`.
- **Rejected.**
  - The trip-centric ranked queue as the universal Home model. The 08-27 recovery says "The transferable asset is the compositional grammar, not the old domain ownership."
  - Atlas as a root: it now redirects to Life.
  - The follow graph and public profile as a distribution surface (multiplayer digest, Doc 5 → Doc 4).
- **Orphaned.** The VDL names prototype web components that "can seed a later component bundle": `buttons.jsx`, `field.jsx`, `sheet-header.jsx`, `productive-header.jsx`, `row-system.jsx`, `vesper-tokens.jsx`, `vesper-typography-contract.jsx`. The kernel's component layer is still empty. No lane has picked this up.

### 3.2 Vesper — Home Surfaces (`f4eee076`, Aug 5–13)

**What it was.** The last pre-pivot design of the shipped Trips (Plans) tab and
Places tab, held by one owner so the two surfaces "stopped producing each
other's answers".

- *Trips — The Page*: 56 frames in 11 groups:
  - A crown · B time · C room · D evidence · E stack
  - F what counts as a plan · G approach · H return · I voice · J maps · K trip feel
- *Places — The Page*: 42 frames in 7 groups:
  - A one place, six registers
  - B several places · C composed plan · D reading · E memory · F people
- *Trips — Prototypes*: "One anatomy, four amounts of structure".
- *Canon*, *Build Manifest* and *Receipt Gaps*.

**Survived.**

| Idea (board) | Where it lives now |
|---|---|
| Containment scale: "A card marks something you can complete here. A row takes you somewhere else." (Canon §1) | Kernel §5 and `cardSurface.ts` CONTAINMENT. Amended 09-05 to "containment marks a coherent object". |
| Evidence union: 10–11 receipt shapes, "finish once, not build twice" (Canon §3) | Kernel §6 "grain-agnostic"; Home's work receipt and receipt chip |
| One crown per surface: "exactly one per surface, or the top of the scale means nothing" (Trips — The Page A) | Home crown; VDL audit "Home has exactly one crown and Places has none" |
| Eight postures shared by both surfaces | Home posture matrix (seven postures), copied into Home R1 |
| Header rule, two-tier rhythm, act break, blob/hatch/grid media split, rest register (Places — Whole Pages A–H rhythm study) | Kernel §11.10, ruled 08-30 |
| Mast and "the page's own voice" (Trips group I) | Home's "the read", serif 30/34 |
| Group H "The return — after it ends · no shipping section" | Became the case for Life as a full continuity root, and Home "Since you last looked" |
| Trips — Prototypes: trip / night / wander / return; "the Plan should preserve the character of each experience rather than render all of them as ordered timelines"; the 96pt slot holds "the most specific true thing" (where / who / area / place) | Plans in Real Life A–C (loose Saturday, planned trip, shared afternoon) |
| "Trips · The Page" priorities (compared 09-08) | Home added `now_temporal_strip`, `now_work_receipt` and `motion_money_row` |
| Receipt Gaps D, "What the trip became" | Life journey reconstruction (LF-12) |

**Rejected.**

- **The co-sign, "Three of you have saved this"** (Places — The Page F·16), and
  "Again? You and Mira · four trips together". Rejected by the 08-30 Places
  anatomy: "Mara saved this" is a rejected social form, and popularity is not
  authority. The Life do-not-resurrect list also rules out intimacy ranking.
- **Trip feel** (Trips K, "Pick a rhythm before a destination", 40 authored
  feels). Rejected in spirit by the 08-27 recovery: "Future ideas should not
  become engagement bait or unsupported inspiration." The flag is still on in
  dogfood (`TRIP_FEEL_STATIC`).
- **The lens strip and overlay-lens card** (Places — Proposed, Places D).
  "Consciously not recovered — superseded by the typed-edges ruling" (kernel
  §11.10.8).
- **A trip-centric ranked queue and equal-weight section feeds** (08-27 §11,
  "Retire").

**Orphaned.**

1. **A shared settle primitive.** Receipt Gaps B: "The settle ledger renders four ways… no shared primitive." Chat has no settle card. Home's money row is proposed only for refunds. See §4, item 1.
2. **"The world changed toward you"** (Receipt Gaps C: a saved cabin drops $40, a table opens). This was **partly resolved by rejection**: the 09-06 booking retirement forbids implied watching. Plans "Brought In and Followed" is the bounded, mandated form. Price changes still have no shape anywhere.
3. **The Trip feel illustration corpus** (40 matched `.webp` illustrations). This is an asset orphan, not an idea orphan. It could supply the missing "riso" plates (§4, item 14).

### 3.3 Vesper — You & Trust (`78e0a36c`, Aug 10–12)

**What it was.**

- Canon — You & Trust: the verified substrate, with four row registers.
- Visual Directions, and Portrait A/B (both superseded).
- Profile System — Canonical Screens (approved 08-11).
- Projections — Public, Co-traveler, Together (superseded 08-12).
- The Connection Loop — Save to Ask to Overlap.
- Axis Studies — The Present Marker.
- Route Map, and As Built.

**Survived.**

- **The approved screens are shipped.** Screen 01 became `YouPortraitScreen.tsx` on `/you`.
- **The header settings gear plus an explained footer door** (Canonical Screens 00B). This is a "solved human need", preserved by the 09-12 brief.
- **Authored words and deliberately chosen places make a page someone's own** (01 Private · Mature, 03 Public). These became You Sept's "the line" (Y-03) and "Places she keeps up" (Y-08).
- **"Seeing yourself vs seeing another person are different experiences"** (Projections). This became You Sept 0-2 "Who sees what", "Viewing as anyone", and "unavailable reveals no private reason" (Y-B12).
- **Time expressed visually** (Axis Studies; B+F "the baseline changes, and today is named"). This became You Sept 0-4 "Her time here". The present-marker thinking fed "never the full empty year".
- **The Connection Loop's steps 02–03**: "Ask someone: a place plus a time… Nobody is added to anything. This sends a question"; respond with no account ("I'm in / Maybe / Can't make it"). These became the Social Experience and Multiplayer Shapes gathering attachment and the no-app guest link page.

**Rejected.**

- Portrait-first as the dominant destination ("inert dashboard").
- "What Vesper reads" and inferred taste on a person's own page (ruling 08-12).
- The follower count in the hero ("A count is not an identity").
- The creator "published lens" variant (01b). The board itself says: "Do not select this… unless the founder rules that creators are the target." The 09-06 vision parks creator lenses as "later".
- The long portrait's repeated "Is this you?" calibration (09-12 brief §8).
- Follow as the relationship primitive (You Sept board 30). Note that shipped code still uses Follow.

**Orphaned.**

1. **The data-use ledger line.** Canon §07 `TrustReceiptRow`: "09:24 · Coarse location read · To rank places near Alfama" and "Voice note · Dropped · Redacted before it reached the model". The same idea recurs on You Sept board 18 ("Kept · used to suggest things… Not kept · Today's rule"). **That trust half is absent from the current You canon 0-0** (`chat-you.md` Part VI). It lives only in shipped `/you/settings` code. This is the most concrete "why you can see this / what Vesper used" affordance in the corpus. See §4, item 3.
2. **Overlap** (Connection Loop 05): "Only inside a granted relationship. Only as an intersection. Always mutual… Both of you saved Casa do Frango. Neither of you has been. Ask about Thursday." The backend reader exists (`GET /api/social-circles/{id}/together`). No current board draws it. It sits close to the rejected "X saved this", but differs because it is mutual, actionable and pair-scoped. **It needs an explicit ruling** rather than silent loss.
3. **The per-save consent bit** (Connection Loop 01): "Share with my circle… Turn this on for one save at a time — never for all of them at once." Multiplayer Shapes chooses audience at share time, not per save. This is compatible, but the "save is intent, not taste" framing was not carried forward.

### 3.4 Vesper - Home & Places (`a26e3228`, Aug 29 – Sep 4)

The full catalog is in `foundations.md` §3–§9. This summary shows fates only.

**Survived.**

- The four moves, the four roots, one dominant thing, and the demand budget.
- Push-not-tab and exact return.
- A crown only for finishable things, with arbitration ruled 09-05.
- The quiet floor.
- The admission gates ("silence is better", "synthesis handed back").
- The T0/T1/T2 treatment ladder and the Grant Moment (Home R4).
- The posture matrix, admission compiler and instruments. These were copied into Home R1–R3 (identical file sizes). The instruments were reworked in the Workbench Stage 2.
- The Places four states: World Field, Place Focus, Place Path, Live Reduction. These went to Places and Entity.
- The 09-02 Aesthetic Pass: one serif voice, three radii, and "people = ink, you = umber". Carried into the VDL.
- Brainstorm shape #3, the From-people Places scope, adopted as "From friends".
- MP5 withdrawal and clean ending, now in Life 17F, You Y-B6/B7 and Multiplayer Shapes.

**Rejected or superseded.**

- "Two kicker registers", replaced by four type roles (09-05).
- "People as reservoir, no people region", replaced by a conditional "Addressed to you" region (09-05).
- Chat "coordination objects are messages, never a page", reversed by "The plan is a page you read" (§11.15).
- The execution ledger and per-owner provider truth (Home Urgent v2, F5, C3). Dormant since the 09-06 booking retirement; "pending is silent".
- F2 temporal posture "I'm watching the noon forecast": implied monitoring is forbidden without a mandate.
- The fifth tab, the table, rollcall and the OS widget from the Brainstorm, all not adopted.

**Orphaned.** Most of these are from the MP boards, which exist only in this
project.

1. **Contributor efficacy** (MP1): the giver sees what their contribution changed, "without public engagement metrics". The Social Experience brief bars automatic usage reports. The tension was never ruled (multiplayer digest §G.23). See §4, item 4.
2. **Relationship scopes wider than the pair** (MP3: `From people I trust`). Dropped by the 09-07 Social Experience brief without a stated rejection (digest §G.18).
3. **Causal prominence** (MP2: a person can own Home's crown, with the metadata → supporting → causal ladder). Only partly absorbed. The 09-05 "Addressed to you" region is conditional. Whether a *person's* act can take the crown is not stated in current Home canon.
4. **Shared agency beyond making a plan** (MP4 Occasion through Places: private caucus, subgroup split and reconvergence). Plans draws "The day changes while people move" (05 D), but not caucus or split (digest §G.25).
5. **Retained intention without a Plan** (HP 09-04 C3, and Kernel Lab F1). This is not orphaned but **unresolved**: the proposal is still `decision_status: proposed` (09-06). It appears in Life P1 and You Y-06 "Looking for", and both say "a want has no owner".

### 3.5 Vesper — Life & Anchors (`f524c7f0`, Aug 29 – Sep 6)

The full tables are in `life-plans.md` §4. The archive's 00A front door and the
Life manifest (`claude-design-life-current-product-manifest-2026-09-06.md`)
classify every board. This is the best-governed legacy project.

**Survived.** Everything below went into Life `e72a2fd2`:

- Four lenses of one corpus.
- The production root (25 and 26).
- The thin-record degradation ladder.
- The dossier and its twelve conditional organs.
- The pass family and the chip (ladder v3).
- The Vault, renamed "Everything kept".
- Target-first search and human refinding.
- The contribution lifecycle.
- The Together arc, "her words first".
- Causal repair.
- The Unfolding arc, as P1–P3 (still proposed).
- Mode switching.
- "Life holds; Vesper recompiles; surfaces deliver".

Home also borrows the pass grammar (decision 09-05). The four return families
(13A–13D) survive as LF-38. Fractal drill-down (06 family) survives as LF-16.

**Rejected** (with reasons in `life-plans.md` §4B and the binding
do-not-resurrect list in `life-root-production-spec-2026-08-30.md` §11):

- The Ledger Line and Specimen anchors.
- The Ledger of Years, The Shelf and Atlas of Time.
- Hierarchy, row and dot paradigms, and figure/instrument reflection forms, which "score the person".
- "Life generates; Home and Places deliver".
- In Motion on Life.
- The Combined/Mine/Together toggle.
- Rotating windows.
- Thread completion pressure.
- Intimacy ranking.
- The relational comparison Return ("no generated comparison beside a friend's words").
- The Red Hook possibility-transfer fixture.
- Per-lens riso empty strips.
- The V2 serif chip.
- FLOWN/SAILED chip stamps.

**Orphaned or tabled.** These are neither carried nor rejected.

1. **Where Objects Live** (05). The Life-as-drawer / Home-as-wallet matrix, the footprint morph and the tap law were "TABLED by founder; contents unruled". Only the rule that L1 appears in Home only while live survived, informally via 09B. This is directly relevant to the product map's "one identity, many views" question.
2. **The resurfacing control center** (00A: "semantics ruled, undesigned"). The controls exist as contract features (LF-68: "Useful · Not now · Keep searchable · Less like this · Never surface this"). Current Life has no board for where a person reviews and undoes them.
3. **The Return Arbitration Lab** (19–19D, 23). Kept "internal by design". Its tuning questions are still open: a global 3-seat cap, partial-overlap suppression, and whether losers are inspectable (`notes-docs.md` #15).
4. **Custody, permitted use and deletion** (39/31 vs 10B). The "release" wording conflict was routed to a contract owner and is **not canonized**.
5. **Deferred items (not orphans).** Lamplight night theme; swipe as an accelerator; "Make my version" (P3.3); photographic composition; the dark-chip scale (D8).

### 3.6 Vesper — Chat, August (`a06d5cb9`, Aug 29–30)

The full table is in `chat-you.md` Part III.

**Survived.**

- The Material Trade: "Chat slims as Home fattens".
- The Entry Envelope mast: world stamp, 30/34 read line, capsule, "chrome speaks the world not the brand".
- The Composition: "surfaces select; screens adapt; content composes", which became CardBlueprintV1.
- Shape-card weight law: "if it wouldn't fit in a message a friend would send, it's too heavy".
- Breathing, as the superseded card.
- The Participation Brief: the guest's "one question back, max", which became G5.
- The Well's "every kind names how it ends", which became card lifecycle.

**Rejected.**

- The Promise Shelf: "a standing advertisement".
- The monitoring tile: "a running job is not a watch".
- The live sliver.
- Gold-wash urgency.
- The decision mandate "execute / stage / escalate".
- Weather in the eyebrow.

**Orphaned.**

1. **The Telescope** (14): semantic zoom through trip › segment › day › commitment. "Depth is pulled, never pushed." An accordion keeps one child per level, and "the telescope ends where ownership begins". It survives for the past in Life LF-16 fractal drill-down. **No forward-looking equivalent exists in Plans or Chat.** Plans in Real Life draws day pages and "Ask Vesper", not a pulled-depth grammar for a multi-day trip.
2. **The Editorial Family** (09, 16): Reading and Story pages with a colophon ("FROM · AS OF · UNKNOWN · Something wrong? Correct it") and "Keep & send". Serif-for-artifact-bodies survived, but the **colophon as a provenance-and-correction foot** did not become a shared component. The nearest current relatives are Home's "Why this" (board 12) and Places' SourceList.
3. **Decision conformance** (11): "a decision must say when it resolves and what happens then". Home's `now_decision` has a deadline. The "what happens then" clause is not drawn anywhere current.

### 3.7 Vesper — Interaction Kernel Lab (`6dd8b450`, Aug 31 – Sep 4)

The full catalog is in `foundations.md` §1, §8 and §9.

**Survived** (as law, not as lab UI):

- The four truth planes.
- The boundary ladder with exactly one preview per real boundary.
- "Undo ends at the boundary".
- Fail closed.
- "Code owns every number".
- World events are not user actions.
- One semantic identity projected natively by each root.
- Generated means ephemeral unless kept.
- The modality allocation (D-48). It was partly revised by §11.15's "one way to change anything: say it".
- The relay door ("prepare, human sends"), which became the 09-09 prepared-message door.

The F-journeys are named behaviour donors for the Workbench and Plans.

**Rejected or overridden.**

- The kernel as the product's opening philosophy (09-01 review: "not the right center of gravity").
- Rigor from the comparison matrix, now closed.
- The provider execution ledger (09-06).

**Orphaned.**

1. **Expense help without a mini-app** (F4). A receipt photo does three jobs resolved from wording:
   - a question gets an answer with no ledger;
   - a split with names creates a private split record;
   - "split it" with no names makes Vesper ask who, and never assume all members.

   Every figure is computed by `derive-f.js`, and "Vesper hasn't moved any money." **No decision adopted or rejected it** (PCA-1 is open). Money between people appears in no current project, although the M1 and v1 scope include expenses (`vision.md` §6). See §4, item 1.
2. **The executable behaviour oracle.** `lab-state.js`, `fixtures.js`, `derive-f.js` and **60 deterministic replay scenarios** encode the kernel laws above as runnable cases. D-47 (the offline authorship eval) and D-49 (the native D2 harness) were delegated rulings that no later document records as started.
3. **E1 value-first protocol** (95): a two-altitude protocol for testing value before collaboration. Nobody ran it. There is still no participant evidence.

### 3.8 Vesper - Social Aperture (`fac2051b`) and its stub (`739de9aa`), Sep 2

**What it was.** A one-day exploration asking whether social needs "an
intentional, present-tense way to enter… their permissioned social world". It
produced:

- the **pin as ambient unit** working decision (01);
- ten Ambient boards;
- the ten-shape Brainstorm. Same-size copies exist in Home & Places and in the stub.

**Survived.**

- The directed case "leave it for someone at a place" (Ambient 2C). It is built dark as the addressed place handoff.
- Kills that still hold: no social room or fifth tab; no counts, upvotes, follower graph or public pins; no arrival push or inferred presence.
- The friend's words changing a decision ("go before nine"). This is the value claim behind Places "From friends" and Multiplayer Shapes place shares.
- Ambient 8, "The Map as the Invite", copied into Social Experience R9.
- Bounded status sentences ("until Sunday night"), in Multiplayer Shapes 06.

**Rejected or superseded.**

- "Comments under pins" (killed here) was **re-admitted** as a ruled verb by Multiplayer Shapes (Sep 20–23).
- "This was useful" (an author-only receipt) was superseded by the ruled single like.
- "Reply opens a Chat, not a comment" was superseded.
- The journey-scale "where I have been" map (Ambient 1) was killed: its value is at city zoom.
- Bearer-link rebinding on join (Ambient 8) is cautioned against by Social Experience R9.
- "Universal-pin ambitions" were retired by the 09-07 brief.

**Orphaned** (see `social.md` gap 5 and the multiplayer digest §G):

1. **By-product production and the self-first default** (01 §1, Ambient 5). A pin exists at zero audience as private place memory. It is produced from moments that already happen (keeping a place, a photo at a kept place, an occasion ending). "Vesper never asks anyone to go pin something." The default audience is "just me". **This is the only supply and cold-start mechanism in the social corpus. It did not carry into Multiplayer Shapes.** See §4, item 2.
2. **The value test.** "A pin works when it changes a decision"; dogfood metrics are "useful" taps, pins opened while planning, and replies. Not pins created. No current social board states a success test.
3. **Map layers and trust order** (Ambient 10, 01 §8): "YOUR KEEP → A FRIEND'S LINE → A DOSSIER → THE LISTING · A DOSSIER NEVER OUTRANKS A FRIEND". Also **reach and time** (Ambient 7): radius not isochrone, "order = distance, never popularity", "fade, never hide". Also the **three-detent map sheet** (Ambient 9). None of these appears in the current Places catalog. They are the most developed social-map thinking in the corpus.
4. **Outward-sharing inspection**: "What have I made visible, to whom, and for how long?" (handoff S7). You Sept has per-entry audience and a window row, but no whole-account view (digest §G.19).
5. **Density as the design test** (01 §4): judge at 3 pins and at 28 pins, "one object in two postures". Multiplayer Shapes admits "how many" is unknown.

### 3.9 Vesper — Home, old (`03538beb`, Sep 4–5)

It was created as a design-system project by mistake. It holds the 09-05 merge
of the 09-04 generous-value pass (H0–H6 folded into 00–09) and the Z1–Z4
baseline.

- **Survived.** All of it, in `42876b8c`. Z1–Z4 have identical file sizes. Boards 00–09 continued to be revised there. Its 07 ledger keeps the replaced phones.
- **Rejected.** D-H1, "crown only when operational", was withdrawn by the founder (00 Index, 09-04).
- **Orphaned.** None found. The only risk is that its 00 Index calls itself current, is org-shared, and has the same title as the live project.

### 3.10 Export-only projects

- **Conversational Artifact Language** (Aug 13–14). Chat Sept carried one card per turn, card lifecycle and no stacking. **Unverified**: whether CAL's motion and streaming (11) and edge-state (12) specifications reached Chat Sept; the Chat owner should check once.
- **Onboarding & First-Value Experiments** (Aug 12). The five entrances stay an active input to the 09-12 reconciliation brief, but no live project was opened. Chat Sept board 9 (O1, proposed) covers only the Chat entrance, and the code has "no home-city or taste step in the normal path" (`crosscutting.md` §4).

---

## 4. Orphaned good ideas: consolidated shortlist

Ranked by product value against the current plan. Each item names the owner who
should receive it and the move needed. "Ruling" means the idea conflicts with a
later rule and needs a founder decision. "Re-home" means it fits current canon
and only lacks an owner.

| # | Idea | Where it lives now | Why it matters | Receiving owner | Move |
|---|---|---|---|---|---|
| 1 | **Money between people.** Expense help without a mini-app, plus one shared settle primitive | Kernel Lab F4; Home Surfaces Receipt Gaps B; Home `motion_money_row` (refunds only) | M1 and v1 scope include expenses. Settle renders four ways in code. No current project draws a split | Plans (`cd2e1f82`), with Home for the row | Re-home: one Plans board built from F4's wording rules and `derive-f.js` |
| 2 | **By-product social supply with a self-first default** | Social Aperture 01 §1, Ambient 5 | The only answer in the corpus to the cold-start and supply bet. Multiplayer Shapes admits "how many" is unknown | Multiplayer Shapes (`caf916f9`) | Ruling: does keeping a place or ending an occasion offer one optional line, defaulting to "just me"? |
| 3 | **"What Vesper used" data ledger**, and the You trust half | You & Trust Canon §07 `TrustReceiptRow`; You Sept board 18 | A concrete answer to "why can you see this?" Shipped in settings code, absent from the You design canon | You (`b66c82a5`), with the C&C contract | Re-home: add the trust half to You 0-0, or state where it lives |
| 4 | **Contributor efficacy** (giver sees the consequence without metrics) | Home & Places MP1 | The social motive to keep contributing. It conflicts with the Social Experience bar on usage reports | Social, with the founder | Ruling |
| 5 | **Social map grammar**: trust order, radius and time, fade-never-hide, three detents | Social Aperture Ambient 7, 9, 10 | Places "From friends" needs ordering and density rules. These are drawn and unused | Places (`516a3ea4`) | Re-home as a Places reference board. The trust-order lineage test is still open |
| 6 | **Overlap** (mutual, pair-scoped "both saved, neither has been") | You & Trust Connection Loop 05; backend Together projection | A pull reason to ask again, without a feed | Social | Ruling: it is adjacent to the rejected "X saved this" |
| 7 | **Where Objects Live** (drawer vs wallet, footprint morph, tap law) | Life & Anchors 05 (tabled) | The object-model question the product map is asking now | Life and Home | Ruling: un-table or formally close |
| 8 | **The Telescope for forward plans** ("depth is pulled, never pushed") | Chat Aug 14 | Multi-day trips have no pulled-depth grammar. Life has one only for the past | Plans | Re-home |
| 9 | **Executable behaviour oracle** (60 replays, state machine, `derive-f.js`) and the D-47/D-49 evals | Kernel Lab runtime | The only runnable encoding of the kernel laws. It could become native acceptance cases | Engineering verification | Re-home as test fixtures, or record that it is closed |
| 10 | **Colophon** (FROM · AS OF · UNKNOWN · Correct it) as a shared provenance foot | Chat Aug 09 and 16 | Provenance and correction are scattered across "Why this", SourceList and notices | Workbench (`c13ae951`) | Re-home as a component candidate |
| 11 | **Onboarding entrances** (share into Places; home-city first value; invite payoff) | Onboarding export (Aug 12) | New-user reality is thin. No project owns onboarding | Founder: choose an owner (Chat or a new project) | Ruling on ownership |
| 12 | **Resurfacing control center** | Life & Anchors 00A; LF-68 controls | Controls without a place to review them | Life | Re-home |
| 13 | **Wider relationship scopes** (`From people I trust`), outward-sharing inspection, density as a test | Home & Places MP3; Social Aperture S7 and 01 §4 | Dropped between 09-02 and 09-07 without a stated rejection | Social | Ruling: confirm dropped, or restore |
| 14 | **Unused assets**: the July web components, and the Trip feel illustration set (40 files) | Vesper `551f400f`; `TripFeelSection` corpus | The kernel component layer is empty, and photo plates are still placeholders | Workbench | Evaluate |

Items were checked against the current-project catalogs (`home.md`,
`places-entity.md`, `life-plans.md`, `chat-you.md`, `social.md`). An item is
listed only if those catalogs neither carry it nor record a rejection. The
check is only as complete as those catalogs.

---

## 5. Cleanup recommendations

These are recommendations only. Nothing was changed.

### 5.1 In Claude Design

1. **Put the status in the title.** Two projects are both named "Vesper — Home" (`42876b8c`, `03538beb`). Two differ only by a hyphen ("Vesper - Social Aperture", "Vesper Social Aperture"). Suggested scheme:
   - superseded: `ARCHIVE · <name> · →<successor>`
   - live dependency: `REFERENCE · <name>`
   - apply to:
     - `ARCHIVE · Vesper — Home (retired 09-06) · → 42876b8c`
     - `ARCHIVE · Vesper — Chat (Aug 2026) · → 096be8ed`
     - `ARCHIVE · Vesper — Life & Anchors · → Life e72a2fd2`
     - `ARCHIVE · Vesper (July canon)`
     - `REFERENCE · Vesper — Home Surfaces (legacy build authority)`
     - `REFERENCE · Vesper — You & Trust (Aug, shipped portrait)`
     - `REFERENCE · Vesper - Home & Places (accepted canon 08-31, MP boards)`
     - `REFERENCE · Vesper — Interaction Kernel Lab (behaviour donor)`
     - `REFERENCE · Vesper - Social Aperture (pin provenance)`
2. **Add a one-line successor banner** to each legacy front door. None of them points to its successor today:
   - Life & Anchors 00A
   - Home & Places Overview
   - Kernel Lab 00
   - Chat 00
   - Social Aperture 00
   - Home Surfaces Canon
   - You & Trust Canon
   - old Home 00 Index

   The 00 Index of old Home `03538beb` still reads as current.
3. **Delete-candidates**, only after a snapshot to `docs/design-archive/` and the founder's confirmation:
   - `739de9aa`, the 2-board stub. Its only unique content is an earlier Read Me.
   - `03538beb`. Its only unique content is the 09-05 intermediate board state.

   Both are **design-system type** by mistake and **org-shared**.
4. **Reduce accidental audience.** Legacy projects with org/team sharing:
   - Life & Anchors
   - Home & Places
   - old Home
   - the Social Aperture stub
   - July Vesper

   A teammate opening them has no signal that they are superseded. Either add banners (item 2) or narrow sharing to invited people.
5. **Snapshot before any archive or delete.** The 09-11 repo snapshot covers the six active products and the workbench only. **No repo snapshot exists** for:
   - Home Surfaces live (after 08-09)
   - You & Trust
   - Life & Anchors
   - Chat Aug
   - Kernel Lab
   - Social Aperture
   - the post-08-31 Home & Places boards: MP0–MP6, critiques, Brainstorm, HP 09-04

   Local Downloads exports exist for only some of these, and Downloads is mutable.
6. **Find the three export-only projects** (CAL, Onboarding, Evening Star) and the unlisted July project in the Claude Design UI. Then record their IDs here.

### 5.2 Repository documents that still point at superseded projects as authority

| File | What it says | Why it is stale | Suggested change |
|---|---|---|---|
| `docs/governance/home-surfaces-design-authority.json` (`status: active`, 08-09); `scripts/check_home_surfaces_governance.py`; `travel-app/Makefile` `home-surfaces-canon-check` | "The external Page boards govern adopted design intent, grouping, composition, and visual direction" for `trips-home` and `places-workspace` | Right as the as-built reference for the legacy default build (production posture is still legacy). Wrong as *design intent*: the direction now lives in Home `42876b8c`, Plans `cd2e1f82` and Places `516a3ea4`. The pinned hashes match the **08-09 Downloads export**, while the live project has a newer Build Manifest (08-11) and a Receipt Gaps board (08-11/13) the bundle lacks | Narrow the `design_intent` rule to "as-built and regression reference". Add a `superseded_for_direction_by` list naming the three successors. Owner: governance |
| `travel-app/docs/surfaces/trips-home/contract.md:13-20`; `travel-app/docs/surfaces/places-workspace/contract.md:20-27` (verified 09-22) | "The August composition authority is the external, hash-pinned `vesper-home-surfaces` bundle" | Same as above | Add one sentence naming the post-pivot successor boards and saying these contracts govern the legacy surfaces only |
| `travel-app/docs/surfaces/profile-system/contract.md:53` | "The approved artboard is `Profile System - Canonical Screens.dc.html` in the `Vesper — You & Trust` project" | Right for the shipped portrait. The Sept You canon (0-0 to 0-5, ruled 09-13/14) is a different page and is not referenced | Add a note pointing to `b66c82a5` as the adopted direction pending build, and keep the August board as as-built |
| `travel-app/docs/surfaces/home-root/contract.md:29-38`; `travel-app/docs/surfaces/places-root/contract.md:21-33` (verified 09-22) | Semantic renders: "the 'Vesper Root Boards' canvas" (Home & Places). Authority: the 08-29 kernel extraction and the 08-30 build manifest | Current Home and Places compositions live in `42876b8c` and `516a3ea4`. The cited kernel doc expires 09-28 and the build manifest expires 09-29 | Name the current projects as the render authority, and renew or retire the two working docs before they expire |
| `docs/working/claude-design-social-experience-project-handoff-2026-09-07.md:741` | Lists "Life `f524c7f0`" as the Life project | Life `e72a2fd2` existed from 09-06 | Correct the ID, or mark the line historical |
| `docs/working/pin-as-ambient-unit-working-decision-2026-09-02.md` (active to 10-02) and its mirror on Social Aperture 01 | "Reply opens a Chat, not a comment"; "This was useful" | Superseded by the Multiplayer Shapes rulings of Sep 20–23 (comment is a verb; one like) | Add a superseded-in-part note. Keep the by-product and self-first sections open (§4, item 2) |
| `docs/working/claude-design-onboarding-reconciliation-handoff-2026-09-12.md:18` | "Continue in `~/Downloads/vesper-onboarding-first-value-experiments-aug-2026`" | It points work at a mutable local export of a project with no live ID | Decide the owner (§4, item 11), then repoint |
| `docs/working/life-root-production-spec-2026-08-30.md:21` (expires 09-29); `life-unfolding-decision-docket-2026-09-04.md`; `life-over-time-walkthroughs-2026-09-06.md` | Cite Life & Anchors boards as sources | Fine as evidence, since the spec itself says it is "detailed design evidence". Readers may still take the archive as current | Add a header line: "boards cited here are in the archive; the current project is Life `e72a2fd2`" |

### 5.3 Expired or expiring working documents still marked `active`

Already past expiry: `design-file-consolidation-2026-07-29.md` (08-28),
`home-surfaces-post-consolidation-engineering-plan-2026-08-09.md` and
`docs/home-surfaces-audit-2026-08-09.md` (09-08), and
`home-surfaces-pre-pivot-recovery-and-post-pivot-direction-2026-08-27.md`
(09-26, today). Expiring by 09-30: the kernel extraction and Places anatomy
(09-28); the Home and Places build manifest, the Life root production spec, the
Life & Anchors correction brief and the critique response (09-29); the Kernel Lab
MCP handoff (09-30). Contracts still cite the kernel extraction and the build
manifest as live authority (§5.2), so renew, promote or archive each one under
`docs/governance/README.md` rather than letting it lapse.

---

## 6. Open questions and unverified points

- Why `list_projects` stops at 20, and whether more unlisted Vesper projects exist beyond `551f400f`. **Unresolved.**
- The live IDs of the CAL, Onboarding and Evening Star projects. **Unknown.**
- Whether the live Home Surfaces files differ materially from the hash-pinned 08-09 bundle. **Unverified.** File sizes differ throughout, and etags show edits on 08-11 and 08-13, but live hashes were not computed.
- Whether CAL's streaming, motion and edge-state specifications reached Chat Sept. **Unverified.**
- Whether any orphan in §4 was rejected in a founder conversation that no document records. **Possible.** The list is doc- and board-based.
