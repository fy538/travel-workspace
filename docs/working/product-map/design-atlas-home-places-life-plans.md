---
doc_type: working
status: active
owner: Claude orchestrator (product map)
created: 2026-09-26
expires: 2026-10-26
why_new: No single document lists every board in the five Home/Places/Entity/Life/Plans Claude Design projects with its disposition, its evidence and the build surface it targets, so progress cannot be measured and designRefs cannot be populated.
promotes_to: null
supersedes: []
---

# Design Atlas: Home · Places · Place/Entity page · Life · Plans

This is the design half of the Design Atlas × Build Map. It covers five Claude Design projects:

| Project | ID | Boards (non-component, excluding before-copies) |
|---|---|---|
| Vesper — Home | `42876b8c` | 38 (00–24, 08b, 08c, 09b, R1–R4, Z1–Z4) |
| Vesper — Places | `516a3ea4` | 11 (00–10) |
| Vesper — Entity Object Handoff Lab | `dd48304b` | 23 (00–16, 06B, Z1–Z5) |
| Life | `e72a2fd2` | 21 (00–09, 03b, 04b, 04c, P1–P4, R0) |
| Vesper — Plans in Real Life | `cd2e1f82` | 17 (00–09, 11–13, 90–92) |

The document gives, for each project, every board with a disposition. It then sets a canonical target set for each build surface and lists contradictions, founder questions, design debt and completeness.

## 0. Method, evidence boundary and vocabulary

**Sources, all read-only.**

- **Board lists.** `list_files` (depth −1) on all five projects on 2026-09-26. This listing is complete and gives every file with its etag.
- **Board text.** Board text had already been extracted on 2026-09-25 into the prior-research scratchpad (`…/7e6d4384…/scratchpad/{home,places,lifeplans,catalog/txt}`). Reused from that research: the catalogs `home.md`, `places-entity.md` and `life-plans.md`.
- **Re-extracted today** from the live project with `render_preview`, because their etags are newer than the prior capture could guarantee: Home 00, 19, 20, 21, 22, 23.
  - 20–23 are byte-identical to the prior extraction.
  - **00 and 19 had changed.** 00 now lists board 24. Board 19 was rebuilt on 24.4's place card, and the live dark map is gone. The prior catalog's H-150 ("a live dark map" on 19.1) is therefore **stale**.
  - The uncommitted §30 of `docs/working/claude-design-home-artifact-led-visual-value-response-2026-09-05.md` records the same change. §30 is headed "September 26", but the board etags read 09-23 23:10–23:15. Treat the etag as the board state and §30's date as the write-up date.
- **Shared-component state.** Read directly from each project's manifest: `vdl-consumed.json` in Home and Life, `vdl-package.json` in Places and Entity.
- **Authority documents.** Everything under `docs/decisions/` from 2026-08-29 to 2026-09-09. The working reviews and handoffs, including the uncommitted Sep 23 Live section of `vesper-home-design-review-2026-09-08.md` and response §28–§30. The four surface contracts in `travel-app/docs/surfaces/*`, `docs/governance/home-surfaces-design-authority.json`, `travel-app/scripts/polish-qa/surfaces.mjs` (travel-app `23cff76f4`), and `docs/design-archive/*`.

**Dates.** "Modified" is the etag, a microsecond Unix timestamp shown as a local date.

- Several bulk stamps are shared-package adoption rewrites, not design changes:
  - Home 09-11 13:08–13:26
  - Places 09-11 13:04–13:13
  - Life 09-11 13:22–13:27
  - Plans 09-11 13:16
  - Entity 09-11 00:19–01:19
- For those boards the last *design* change is older. The board's own header says when it was last designed.

**Evidence boundary.**

- Every board is a static fixture mockup.
- "Adopted" means an accepted decision record or founder ruling. It never means built, natively verified or participant-tested.
- 09-09 selections are **founder-delegated** (`2026-09-09-select-design-convergence…`: "not a claim that the founder separately inspected each resulting frame").
- No board was rendered at pixel level for this atlas, and no native app was run.

**Disposition vocabulary (as requested).**

| Disposition | Meaning |
|---|---|
| **ADOPTED TARGET** | Founder-ruled, or backed by an accepted decision record |
| **SELECTED** | The chosen direction on the board or in a response or review doc, not yet in canon |
| **EXPLORATORY-KEEP** | Proposed, review or coverage work worth keeping |
| **REFERENCE** | Index, ledger, as-built, baseline, before-copy or reference-canon copy |
| **SUPERSEDED/REJECTED** | Archive |

**Build-surface keys used below.**

| Key | What it covers | Flag |
|---|---|---|
| `home-root` | `components/home-root/*`, v2 `HomeRootV2Screen` | `EXPO_PUBLIC_FOUR_ROOT_SHELL` and the v2 flags |
| `places-root` | Governed `PlacesSemanticField` (10 kinds); legacy `places-workspace` still ships | — |
| `entity-object` | `ObjectPageRebuild` | `EXPO_PUBLIC_OBJECT_PAGE_REBUILD_ENABLED`; routes `/venue`, `/site` |
| `life-root` | `LifeRootV1Screen`, `GET /v1/life` | — |
| `trip-itinerary` / Plans | `TravelPlanScreen` (shipped); `LocalPlanScreen` (`LOCAL_PLAN_DOGFOOD_ENABLED`); `PlanStopInspectSheet` / `PlanStopAssistance` | — |

---

## 1. Authority map: what actually governs these boards today

| Layer | Artifact | State on 2026-09-26 |
|---|---|---|
| Home anatomy | Decision 2026-08-30 (Home & Places anatomy), amended 2026-09-05 (composition canon; pass grammar and crown arbitration) | Accepted. Crown order is still **provisional**: "to be confirmed on board 08 row three", and never confirmed |
| Life anatomy | Decisions 2026-08-30 (Life anatomy) and 2026-09-01 (Life v1 behaviours, delegated) | Accepted |
| Entity page | Rulings 2026-09-03 (in the Entity spec §0) and decision 2026-09-04 (rollout) | Accepted |
| Plans | Decision 2026-09-05 (Plan in seven sentences); 2026-09-09 amends sentence 6 | Accepted |
| Cross-project selection | Decision 2026-09-09 (select design convergence and prepared continuations) | Accepted (delegated). **The last decision record.** Nothing after 09-09 (the 09-21 photos, 09-23 Live lane D, the coupon, the 09-23/26 place card) has a decision record |
| Contract render authority (Home, Places) | `home-root/contract.md` and `places-root/contract.md` cite the **"Vesper Root Boards" canvas**, committed as `docs/design-archive/root-boards-2026-08-31-accepted/` | **Stale.** They do not cite the Home or Places projects or the 09-09 selections |
| Contract render authority (Entity) | `entity-object/contract.md` | Cites the handoff and build brief. Says a design export "should be promoted into `design-refs/`", which has not happened |
| Contract render authority (Life) | `life-root/contract.md` | One promoted ref: archive board 25 of **Vesper — Life & Anchors** (`f524c7f0`), not the current Life project |
| Registry | `docs/governance/home-surfaces-design-authority.json` | Authority `vesper-home-surfaces-2026-08-09`, scope `trips-home` and `places-workspace` (pre-pivot bundle). **None of the five projects is registered.** Its copy policy forbids canonical HTML in repos, yet two committed snapshots exist: `docs/design-archive/design-language-2026-09-11/` (404 tracked files, Home 00–16 only) and `root-boards-2026-08-31-accepted/` |
| QA design refs | `surfaces.mjs` | See table below |

`surfaces.mjs` design references (travel-app `23cff76f4`):

| Surface | `designRefs` | `judgeAgainst` | Flag |
|---|---|---|---|
| `home-root` | `[]` | `doctrine` | `EXPO_PUBLIC_FOUR_ROOT_SHELL` |
| `places-workspace` | `[]` (v405 PNGs listed separately are historical) | `external-canon` | — |
| `entity-object` | `['docs/surfaces/entity-object/contract.md']` | `doctrine` | — |
| `life-root` | `life-v1-production-time-rich.html` (archive 25) | `external-canon` | — |
| `trip-itinerary` | `'Vesper Itinerary.html'` (pre-pivot Discover/Search design) | `canon` | — |

**Implication.** The Build Map cannot yet measure "design parity" for any of these surfaces against the current projects: every QA reference predates them or is empty. §3 proposes the target sets to register.

---

## 2. Board tables by project

### 2.1 Vesper — Home (`42876b8c`)

Shared components live in the project (not boards): `InviteCard` (09-23), `Ticket` (09-23), `OriginalReader` (0.4.1, 09-11) and `Notice` (09-11). The manifest `vdl-consumed.json` (09-23) records `vdl-stage1 0.4.1`.

| Board | Modified | Purpose | Disposition | Evidence | Build target |
|---|---|---|---|---|---|
| 00 Index | 09-23 | Reading order, statuses, fixture world, rulings and open items. Now lists 24 | REFERENCE | Live read 09-26; response §30 | — |
| 01 Parts | 09-10 | Every kind drawn: the 35 admitted plus 3 proposed (temporal strip, work receipt, money row) | REFERENCE | Decision 09-05 §4 (35 kinds); 09-09 "does not admit proposed new kinds" | `home-root` registry (20 of 35 kinds native) |
| **02 Persona A**, top three frames: SELECTED ORDINARY (Sun Sep 6), SELECTED QUIET (Thu Sep 3), SELECTED unit study (thin context) | 09-11 | The generous ordinary and quiet scrolls; the unit study is not a full scroll | **ADOPTED TARGET** (delegated) | Decision 09-09 §3: "retain the generous ordinary/post-return 02/03 compositions"; benefit-led read (14.1 B); 09-12 routing: "accepted as design references" | `home-root` Available/Quiet |
| 02, below the HISTORY divider | 09-11 | How the scrolls were reached: Sunday/Monday before and after forms, floor, sparse Monday, Thursday, record | REFERENCE | 00 index | — |
| **03 Persona B**, top three frames: SELECTED POST-RETURN (day zero Aug 28), SELECTED RETURN AFTER ABSENCE, SELECTED TRIP DAY | 09-10 | Post-return and trip-day scrolls on one Life-record fixture | **ADOPTED TARGET** (delegated), with a caveat: the trip day uses 3 unadmitted kinds (C-05) | Decision 09-09 §3; 00 index "new 09-08" for trip day | `home-root` Returned/Live |
| 03, history | 09-10 | Day zero before and after; temporal posture; dish redraw | REFERENCE | 00 index | — |
| 04 Persona C · New User | 09-11 | First open before and after (sample = Life's signature), sample opened, one contribution, chip receipt, next open | SELECTED (cold/thin reference) | 00 index "thin-context check"; 09-09 §3: sample is "optional bounded demonstration, not an input tax" (15.3 over 15.2) | `home-root` Cold; `now_sample_demonstration` (built; backend-flag dark) |
| 05 Wedge · Trip Forming | 09-09 | Group travel: organizer, joiner, live day under change (rev 4) | EXPLORATORY-KEEP | "Launch wedge" framing must be reconciled with the everyday-first strategy (decision 2026-09-06, reconcile consumer strategy) | Plans/Occasion ↔ `home-root` |
| 06 Places · From Friends | 09-08 | Friends scope and Place Focus; two continuations (06.3 route, 06.4 cold map) | ADOPTED TARGET (social split); continuations are EXPLORATORY | Decision 09-05 §2, "the social split" (D-H4 closed) | Home pull door → `places-root` friends scope |
| 07 Ledger and Decisions | 09-11 | Rulings vs history, per-form ledger, deletion test, 15 questions, HL ledger | REFERENCE | 00 index | — |
| **08 Seam with Life** | 09-11 | Pass at L1 in the live window, kind mark, chip, flight ladder, collision; row 3 crown ranking; row 4 Rule A vs Rule B | **ADOPTED TARGET** (pass grammar) · crown order provisional · Rule B not promoted | Decision 09-05 (pass grammar) §§1–6; 09-09 "does not amend commitment/crown arbitration"; 00 index "DECISION NEEDED" | `home-root` crown / `now_commitment_instrument` |
| 08b Home to Life | 09-11 | Four whole encounters, HL-1 to HL-4 (coastline, afternoon route, ferry day corrected, a friend's photo); sparse and no-Return checks | EXPLORATORY-KEEP (PROPOSED). Carries the destinations of the adopted 02/03 scrolls | 00 index "Continuity pass 09-07 · PROPOSED"; HR-1/HR-3 corrections applied | `home-root` → Life doors |
| 08c The Trip Day | 09-10 | Trip-day scroll, boat moved, Life day page, pass, claim; what Home does not do | SELECTED | 00 index "New · 09-08"; the trip-day scroll is selected on 03 | `home-root` Live; Life P3.4 |
| 09 Forms | 09-11 | Selected-form sheet, bare control, 1.3× reflows, reading order, chip study | EXPLORATORY-KEEP (held-object instrument is ADOPTED) | 00 index "Everything on 09 is proposed, not ruled" | Renderer anatomy |
| 09b Forms · Large Text | 09-10 | Temporal strip across the day, photo rules, the six selected scrolls at 1.3× | SELECTED (large-text reference, unruled) | 00 index "New · 09-08"; response doc | `home-root` Dynamic Type QA |
| 10 States | 09-09 | Withdrawal, narrowing, block; occasion lived through; kept intention returning; attributed friends | EXPLORATORY-KEEP | 00 index "Added 09-06 · PROPOSED" | `home-root` social degradations |
| 11 Return and Continuity | 09-08 | Nine undrawn kinds on a return-after-absence page; region-to-heading mapping | EXPLORATORY-KEEP | "Added 09-06 · PROPOSED" | `home-root` continuity kinds; headings (see C-12) |
| 12 Why This, Chat, Degraded | 09-11 | Why-this sheet, the one Chat aperture, stale / provider-unknown / import-pending states | EXPLORATORY-KEEP | "PROPOSED"; the secondary-question route was corrected by 15.4 | `home-root` degradation, Chat seed |
| 13 Photograph Treatments | 09-09 | 8 treatments × 3 handlings; warm paper for reference images; own photos untreated | SELECTED (founder-chosen 09-08, no decision record); riso REJECTED | 00 index "warm paper chosen"; review H7 | Photo rendering (no approved assets) |
| 14 Three Ordinary Opens | 09-10 | A newcomer across three opens on the bounded supply set (pair with Places 03.3) | EXPLORATORY-KEEP (stress case). 14.1 B read is ADOPTED | Decision 09-09 §3: "14 remains the bounded-supply stress case"; benefit-led read selected | `home-root` supply / world read |
| 15 Learning and Steering | 09-10 | Demonstration vs ordinary control; secondary question; spoken steering | 15.3–15.4 and 15.5–15.7 ADOPTED (local shortening only); rest EXPLORATORY | Decision 09-09 §3 (15.3; 15.5–15.7 accepted "without adopting persistent preference"). The index under-labels 15.5–15.7 (C-14) | Chat ↔ Home steering |
| 16 Shared Language Adoption | 09-11 | vdl 0.4.1 consumption, before/after crops, missing variants reported | REFERENCE | Response §22–23; snapshot README 09-11 | vdl → native component map |
| 17 Delivery and Return | 09-15 | Away results: requested result, friend's offering, consequential change; withdrawn, cancelled, signed out | EXPLORATORY-KEEP (coverage; donors reused) | 00 index "Coverage · 09-12"; review §Sep 12 | Notifications contract; `home-root` return |
| **18 Ordinary Photographs**, K (full scroll) and L (K at 1.3×) | 09-21 | Sunday Home with Maya's pictures, In motion (refund), Saved this week (recipe as retrieval), city week, friends door | **SELECTED** | Review "Export review Sep 21": "Keep 18 K/L as the selected photo-integrated scroll"; response §27 applied the 09-22 refinements | `home-root` people_original_delivery + Life viewer |
| 18 A/B/C, D/E, J, path frames | 09-21 | Treatments (C = "retrieval dressed as enrichment", not selected); D/E narrow study; J region failure; viewer path | A/B EXPLORATORY-KEEP; C REJECTED; D/E REFERENCE (study); path SELECTED | Response §26–27 | Life 04b/04c viewer; Social 10P |
| 19 Live · A New City | 09-23 | Unfamiliar city, no plan: **place card** (24.4) + IN REACH coupon vs a timed afternoon (19.2, not chosen); Places and back; "only here an hour"; no location; 1.3×; healthy hour | SELECTED (design) study; 19.2 REJECTED | Response §28 and §30; live board text 09-26 | `home-root` Live (nothing built) |
| 20 Live · An Evening Together | 09-23 | Pasta night: host, late joiner, guest; Dana contributes once; "Keep seven / Move to eight"; nothing to resolve; the show with a moved meeting point | EXPLORATORY-KEEP (proposed studies) | 00 index "proposed studies"; §29 applied lane D | `home-root` + Plans + Social |
| 21 Live · A Travel Day | 09-23 | TAP 214: preparation (cream pass), rush (oxblood), gate (live pass + coupon), skip Sintra, landing offline item by item, arrival | EXPLORATORY-KEEP (proposed studies) | Same as 20; 21.1's "accepted responsibility" is unadopted (C-07) | `home-root` Live/Urgent |
| 22 Live · Making Live Visible | 09-23 | Lanes A (instrument crown), B (band), B+ (band holds object), C (live field), **D (the object itself goes live)** | **D SELECTED** (founder-chosen 09-23, no decision record); A/B/B+/C REJECTED | Response §29; review §Live. The board still prints the old B/A recommendation, and D1 still shows a live map (C-02) | Requested shared `Ticket` live variant (not built) |
| 23 Live · The Companion Tray | 09-23 | Trays T1–T5; T2 coupon in seven colourways | **T2 ink/cream SELECTED** (founder-chosen 09-23); others REJECTED | Response §29; 00 index. The board itself does not mark the choice | Same |
| 24 Live · Where You Are | 09-23 | Familiar or unfamiliar × plan or no plan; 24.4 place card, "Maps stay in Places" | SELECTED (design): 24.4 applied to 19. Index label still reads "Exploration" | Response §30 (founder question, agent resolution; no founder ruling recorded) | `home-root` Live |
| Before VDL 0.3 − 02, 04, 08, 08b, 09, 12 | 09-11 | Frozen pre-adoption copies used by 16's crops | REFERENCE (before-copies; archive candidate) | `vdl-consumed.json` "before_references" | — |
| R1 Home Posture Matrix | 09-06 | 7 postures × 4 regions (08-31 canon copy) | REFERENCE (copy of ADOPTED canon) | Decision 08-30; contract "Posture acceptance" | `home-root` postures |
| R2 Home Admission Compiler | 09-06 | 11 gates and precedence | REFERENCE (copy of ADOPTED law) | Decision 08-30; manifest §3 (gates "pending adoption" in ranker) | Backend `concierge_feed` / v2 selectors |
| R3 Instruments | 09-06 | Instrument sheet (08-31) | REFERENCE. May be superseded by workbench Stage 2 (brief 09-13) | 00 index "unrevised" | `components/instruments` (dev gallery only) |
| R4 The Grant Moment | 09-06 | T2 grant as one human choice | REFERENCE | 08-31 canon | Social/Life grants |
| Z1–Z4 Baseline 09-04 | 09-06 | The 09-04 study (inventory; three personas × five opens) | SUPERSEDED (archive; cited by 07) | 00 index "Archive" | — |

### 2.2 Vesper — Places (`516a3ea4`)

Components live in the project: `ActionGroup`, `FactPair`, `InviteCard`, `LocationFooter`, `Notice`, `OriginalReader` (0.4.1), `PlaceHead`, `PlaceIdentity`, `SourceList` and `Ticket`, all 09-11. Manifest `vdl-package.json`: "0.4.1, prepared for review; not published to the Production Kernel".

| Board | Modified | Purpose | Disposition | Evidence | Build target |
|---|---|---|---|---|---|
| 00 Index | 09-21 | Project in miniature; board table; "Selected versions only" | REFERENCE | Board text | — |
| **01 The Field** (01.1 populated, 01.2 cold) | 09-11 | The chosen field scroll: anchor and sentence, lead composition with day-line, From friends row, Any day shelf, Red Hook pocket, evening, two ways in and reading, Sunday, tail doors | **ADOPTED TARGET** for the substantial field (delegated); expression SELECTED 09-07 | Decision 09-09 §3 "preserve the substantial field"; response §20 (founder chose the expression). The five ordering decisions on 05 remain **unaccepted** | `places-root` (lead_composition, browse_shelf, branch, continuity_doors, … render; most instruments are design-only) |
| 02 The Journeys | 09-11 | E: exploration; H: receiving in three branches (read / reply / private Ask / "Make it Saturday"); P: the practical chain on one clock (check, prepared proposal, answer, move, change, return) | ADOPTED TARGET for behaviours (check = one look; prepared-message door); frames SELECTED | Decision 09-09 §2 (sentence-6 exception) and §4 ("current check… not an implicit watch") | `places-root` + Social sender + Plans organizer command (none built) |
| 03 The Situations | 09-11 | 03.1 missing history; 03.2 missing friends; 03.3 pair with Home 14; 03.4 unavailable; 03.5 and 03.6 unhurried vs constrained; 03.7–03.9 correction | 03.7–03.9 ADOPTED (delegated); the rest SELECTED | Decision 09-09 §3 "Keep the explicit mistake/correction/later-use comparison" | `places-root` degradations; Life inference owner |
| 04 The Checks and the Opening | 09-11 | Long names; 1.3× (04.7–04.12); the opening door, destination and return | REFERENCE (acceptance checks), SELECTED opening sequence | 06 Log | Places QA matrix |
| 05 Decisions | 09-11 | Five ordering, map, arrangement, friends and proposal decisions | EXPLORATORY-KEEP: "PROPOSED, NOT ACCEPTED" | Board header | Needs a founder ruling (Q-P1) |
| 06 Log | 09-21 | One row per pass through the "Sep 12 coverage, closed against its own bar" pass | REFERENCE | Board | — |
| 07 Components | 09-11 | The Places kit at phone width; exclusions narrowed 09-09; older sheets marked historical | REFERENCE (kit spec) | 06 Log (09-11) | `places-root` renderer and instrument mapping |
| **08 The Page** | 09-11 | 08.1–08.6 six states (normal, cold, material change, pending, listing unreachable, closed for good); 08.7–08.9 three purposes vs Entity 09/11/12; 08.10–08.13 reading → pier → ending → unvisited | 08.1–08.6 SELECTED; **08.7–08.9 ADOPTED direction**; **08.12 and 08.13 ADOPTED** (08.13 with the diagram corrected) | Decision 09-09 §1 and §3 | `entity-object` (Places register form not built) |
| 09 Purposes | 09-11 | Field for four purposes: a little context, accumulated context, a friend's contribution, history irrelevant | SELECTED (design; replaces the withdrawn fixed-stage rule; unruled) | Review P1; 06 Log | `places-root` admission |
| 10 Scope and Selection | 09-21 | A1–A6 scope chooser, remote scope, refine, no match, clear; B1–B9 marker ↔ row, entity, private question, provider handoff, return, 1.3×, 320 px, back-after-change | EXPLORATORY-KEEP ("Proposed for review"); B4 destination ADOPTED direction | Board's own table: "Implemented No, Verified No" | `places-root` map/list; `PlacesMapCanvas`; return tokens |
| before/00–09 + `support.js` | 09-11 | Pre-0.3 originals | REFERENCE (before-copies; archive candidate) | 00 index | — |

The Places archive (Z01–Z20) lives in the repository under `docs/working/design-gen/places/archive`, not in the project.

### 2.3 Vesper — Entity Object Handoff Lab (`dd48304b`)

Components live in the project (all 09-11): `ActionGroup`, `FactPair`, `InviteCard`, `LocationFooter`, `Notice`, `OriginalReader` (**0.3, 11,643 B**), `PlaceHead`, `PlaceIdentity`, `SourceList`, `Ticket`, plus `entity-lab.css`. Manifest `vdl-package.json` records **vdl-stage1 0.3** (09-10).

| Board | Modified | Purpose | Disposition | Evidence | Build target |
|---|---|---|---|---|---|
| 00 Read Me | 09-15 | Working set, statuses, locked Part I, 09-03 rulings | REFERENCE (describes 09 with the rejected rule, see C-01) | Board | — |
| 01 Audit | 09-04 | The venue page as it ships (mock vs real), catalog coverage (photos 0 %, hours 17 %) | REFERENCE (as-built 08-13; re-measure against prod) | Board | `/venue/[venueId]` legacy |
| 02 The Law | 09-04 | Seven inputs, twelve rules, tests | ADOPTED TARGET (acceptance criteria; amended by 06) | 09-03 rulings; E08 T1–T14 | `entity-object` tests |
| 03 Three Kinds One Family | 09-11 | Entity / container / spot on one shell | SELECTED ("Current"); spot admission UNRESOLVED | Read Me "Current"; roadmap Later | `entity-object` (container is the named exception) |
| 04 The People Slot | 09-04 | Byline, face sheet, ten states | SELECTED ("Current") | Read Me; form from the Places Social Anatomy canon (08-30) | `people-lines` byline (built behind a flag); sheet actions design-only |
| 05 The Five Paths | 09-11 | Origin → resolving → known / matched / made → two stops | SELECTED ("Current") | Read Me | Entity resolution routes (harness not built) |
| **06 The Page** | 09-11 | Chosen page: square plate (photo or nothing), kicker, byline, pair, cited body, verbs, closing row, where row | **ADOPTED TARGET** (shell, plate, verbs, pair); body partly superseded by 14 | Rulings 09-03; decision 09-04 (verbs; no Add-to-trip) | `ObjectPageRebuild` (most of it on main behind a flag) |
| 06B Arrival and Large Text | 09-11 | Café Aurora arrival (nothing above the body moves); Hortus at accessibility size | SELECTED ("Current") | Read Me; app `2377099e9` large-text stacking | `entity-object` |
| 07 Implementation Handoff | 09-04 | Mirror of the rev-3 spec | REFERENCE ("workspace file wins") | Board | — |
| 08 Build Brief | 09-04 | Mirror of the build brief (tests, token map, ranker, state machines) | REFERENCE | Board | — |
| 09 One Place, Five Doors | 09-11 | Five entry contexts; context matrix | **SUPERSEDED in its body rule** ("the context adds one line and never a fact" = invariant body); the context/Back/"opening implies nothing" matrix is EXPLORATORY-KEEP | Decision 09-09 §1 rejects the invariant-body rule and orders the lab to reconcile 09/11/12 with 14 | Context line (design-only) |
| 10 Intent Beyond Tonight | 09-11 | Keep receipt with when-chips; keep loosely; "Would this work for Maya's dinner?" | EXPLORATORY-KEEP (non-canonical; owner unresolved; corrected 09-11) | Read Me; E13 | Keep (built); chips unresolved |
| 11 Places and Life | 09-11 | Focus lanes become inputs; relationship line; Life door pair | EXPLORATORY-KEEP; the door pair is SELECTED | Places 08 table "Selected: Entity 11's pair of doors" | Relationship line (built); Life door design-only |
| 12 Useful Edges | 09-11 | Directions and Reserve interstitials; return is not booking; confirmation projection; three effects behind a face | SELECTED (via Places 08 table: "Entity 12 as drawn"); lab label non-canonical | Places 08; decision 09-04 non-goals | Interstitials design-only |
| 13 Status and Deltas | 09-09 | Capability ledger against main 09-04; decision/delta log | REFERENCE (stale: 09-04 ledger) | Board | Build Map input |
| **14 Received from Places** | 09-11 | R1 discover, **R2 for Saturday (protected destination reference)**, R3 from the reservation, R4 friend's original direct, R5 unvisited | **ADOPTED TARGET** (delegated) | Decision 09-09 §1; Read Me "Selected"; 09-12 routing "preserve Entity 14 R2" | `entity-object` purpose-responsive body (context line not built) |
| 15 Shared Adoption | 09-11 | vdl 0.3 adoption, what is shared, missing variants | REFERENCE | Board | — |
| 16 Requested Work and Return | 09-15 | Candidate with purpose; explicit check: running / result / failed / unknown / stale; exact original; provider door | EXPLORATORY-KEEP (non-canonical coverage; donors Plans 90) | Board header | Check service (does not exist) |
| Z1–Z5 Archive | 09-04 | Four languages, the blob, typeset, element order, the pair | SUPERSEDED | Read Me "Archive" | — |
| before/03, 05, 06, 06B, 09, 10, 11, 12, 14 + `support.js` | 09-11 | Pre-0.3 originals | REFERENCE (archive candidate) | Read Me | — |

### 2.4 Life (`e72a2fd2`)

Components live in the project (09-11): `Notice`, `OriginalReader` (**0.3**, 11,643 B) and `Ticket`. Manifest `vdl-consumed.json` records **vdl-stage1 0.3** (09-11). Fixtures: `life-composition-fixtures-v0.1/v0.2.json` (09-06).

| Board | Modified | Purpose | Disposition | Evidence | Build target |
|---|---|---|---|---|---|
| 00 Start here | 09-21 | Walkthrough index, statuses | REFERENCE. Header is stale: "SEP 6 · EIGHTEEN BOARDS" while 21 exist | Board | — |
| **01 My life, four ways** | 09-11 | Masthead, lens selector (Time · Places · Threads · People), Returns, reflections, windows | **ADOPTED TARGET** | Decision 08-30 (Life anatomy); archive 25/26 "composition verbatim"; 09-09 "preserve four lenses" | `life-root` (Time served; People partial; Places shadow; Threads not served; Returns never produced) |
| **02 An ordinary beginning** | 09-11 | Ordinary week, thin record, zero record, Ask vs Keep, ongoing interest | **ADOPTED TARGET** (delegated) | 09-09 §3 "ordinary formation… quiet non-use"; C3 consumer-proven 09-01 | `life-root` thin/zero; Chat Ask no-write (not true in code) |
| **03 Open something in my life** | 09-11 | One page grammar: journey, place relation, shared record, one evening | **ADOPTED TARGET** (dossier canon) | Decision 08-30; archive 06 family | Dossiers unbuilt |
| 03b Inside a record | 09-11 | Fractal drill-down; "where it lives" | EXPLORATORY-KEEP ("Review", with a recommendation) | 00 | Unbuilt |
| **04 My original things** | 09-11 | Pass family full size; non-pass kinds; Everything kept; kind drawers | **ADOPTED TARGET** | Direction A ruled 08-29; "Everything kept" ruled 08-31 | Everything control exists; ledgers and custody verbs not built |
| 04b Ordinary photographs | 09-21 | Evening pictures uncropped; viewer; Bring vs Ask; mixed selection; image failure | SELECTED (Review label; shared viewer donor for Home 18 and Social 10) | Life handoff "Export review Sep 21: preserve the progress" | Unbuilt |
| 04c One photo path | 09-21 | Scripted prototype of the Life and Home paths; Social 10P outcomes (partial retry only the late table; unknown = check) | SELECTED (prototype donor). **The partial-send disagreement is resolved in Life** and now flags Social 10P's "Share 1" | 04c text (live); Life handoff item 2 | Unbuilt |
| **05 Find it again** | 09-11 | Target-first search, honest limits, imperfect cues, full record by time | **ADOPTED TARGET** (consumer-proven 09-01) | Decision 09-01 | Refind lane behind `EXPO_PUBLIC_LIFE_REFIND_LANE` (dark); full record `/you/life-record` built |
| **06 Give once, get value back** | 09-11 | Value-first contribution, held question, Returns, context used vs unused | **ADOPTED TARGET** | Decision 09-01; 09-09 (equal present info in comparisons) | Unbuilt (Returns slot has no producer) |
| **07 The people in my life** | 09-11 | Addressed arrival stamp, hosted dinner lanes, optional reply, withdrawal, three note choices | **ADOPTED TARGET** (Together arc 09-01); the "Keep a copy" door is agreement-dependent | Decision 09-01 | `social_contribution` owner UNAVAILABLE in Life |
| 08 The actual source | 09-21 | Original email/document/photo reader; loading, offline, won't open | SELECTED ("Current"; Sep 12 coverage) | 00; Life handoff §Sep 12 | Partly built (`/you/intake-submissions/[id]`, proven 09-21) |
| 09 Finishing a local action | 09-21 | Scoped export/delete, partial failure, four verbs | SELECTED ("Current"; 09.3 Review) | 00 | Not evidenced |
| P1 What I keep ahead of me | 09-11 | AHEAD (arranged vs kept softly), kept-intention lifecycle, kept place before a visit | EXPLORATORY-KEEP (pending R1–R6 and intention owner since 09-04) | 00; `life-unfolding-decision-docket-2026-09-04.md` | Blocked: runtime needs a Trip |
| P2 Life changes without management | 09-11 | Late material, sentence correction, stability laws | EXPLORATORY-KEEP | 00 "Review" | Org engine shadow; no correction UI |
| P3 Something I deliberately saved | 09-11 | Saved composition vs living record; captured day (P3.4/P3.5, Home 08c) | EXPLORATORY-KEEP | 00 "Review" | Unbuilt |
| P4 A map inside a record | 09-11 | Map as a conditional organ; kept path | EXPLORATORY-KEEP (kept path = contract amendment) | 00 "Review" | Unbuilt |
| R0 Reference | 09-11 | Kernel, chip at 32 pt, pass, lens switching, optional swipe | REFERENCE (chip 32 pt ADOPTED in Life; swipe demoted) | 00 "Current" | Chip not built |
| before-shared-package/ (14 boards + `support.js`) | 09-11 | Pre-0.3 originals | REFERENCE (archive candidate) | `vdl-consumed.json` | — |

The Life archive, Vesper — Life & Anchors (`f524c7f0`, 121 canvases), is outside this atlas's scope. It still holds the promoted `life-root` designRef (board 25).

### 2.5 Vesper — Plans in Real Life (`cd2e1f82`)

Every board is stamped "EXPLORATION · NOT CANON · NOT PRODUCTION". Components: `Notice` only (09-11). There is no vdl manifest; the kit is `kit/plans.css` plus `kit/plans.before-vdl.css`. Other files: `kit/proto.js` (09-05) and `evidence/plan-day-{top,scrolled}.jpg` (09-04).

| Board | Modified | Purpose | Disposition | Evidence | Build target |
|---|---|---|---|---|---|
| 00 Start Here | 09-15 | Recommendation, board map (design = 01–09, 11, 12, 13; 90–92 appendix) | REFERENCE | Board | — |
| 01 Baseline | 09-11 | Native captures (main `47735f406`, Ready-Kyoto mock); the redrawn control | REFERENCE (as-built) | Board | `TravelPlanScreen` |
| 02 A · A Loose Saturday | 09-11 | Loose intention (A2), exploratory alternative (A4), receipt (A5), release timing keep place (A7), rejected skeleton (A8), order-less list (A9), conditional pair (A10) | A9 and A10 ADOPTED; A8 REJECTED; A2 SELECTED (storage model proposed) | Decision 09-05 (§11.8 amendment); board 07 | `LocalPlanScreen` (internal flag; needs a Trip) |
| 03 B · A Planned Trip, Kyoto | 09-11 | Arrival day; loose day beside a reservation; list ↔ map; ticket stub; compact header; 135 % | SELECTED (itinerary = default projection is ADOPTED; type-role tokens PROPOSED) | Decision 09-05; 07 Q10/Q11 | `TravelPlanScreen` refinements |
| 04 C · Shared Afternoon and Dinner | 09-11 | Invitation as guests see it, guest link, suggestion under a row, contributor not coming, scoped grant, dinner only, return / end grant | EXPLORATORY-KEEP (guest delivery Q9/Q16 open) | Board labels "illustrated" | Social/multiplayer (unbuilt) |
| 05 D · The Day Changes | 09-11 | Rain on an optional stop; "Update & send" (D3); the one mismatch; Sam on the train | D3 ADOPTED (09-09 table); others EXPLORATORY-KEEP | Decision 09-09 §2 table | Unbuilt |
| 06 E · Overlap and the Four Doors | 09-11 | Two travellers overlapping; Home, Chat, Places and Life point at the same page | SELECTED ("card is a pointer"; PCA-3 pending) | Board 07 | Cross-root doors (unbuilt) |
| **07 Decisions, Mapping, Reuse** | 09-15 | The seven sentences, composition answers, token mapping, Q-list | **ADOPTED TARGET** (sentences FR 09-05 + 09-09 amendment); token changes PROPOSED | Decisions 09-05 and 09-09 | All Plans work |
| **08 Contextual Request** | 09-11 | One Ask pill; value-first stop sheet (P2); resolution shapes; "More room in Chat" | **ADOPTED TARGET** (sentence 2 drawn); P2 SELECTED | Decision 09-05; board 07 | `PlanStopAssistance` built (`131171f26`), native unverified |
| 09 Journeys | 09-11 | Value without doing; ask/correct/change; J2f "Ask Ben about 10:15" | J2f ADOPTED (09-09); rest SELECTED | Decision 09-09 §2 | Partly built (Send proposal) |
| **11 Continuations** | 09-11 | I1–I1c prepared proposal; guest reply; incompatible; morning after | **I1–I1c ADOPTED** (09-09); G1 and F1 EXPLORATORY-KEEP | Decision 09-09 §2 | "Send proposal" built |
| 12 Brought In and Followed | 09-15 | X1–X4b brought-in schedule; W1 current check; W2–W5 following (PROPOSED); C1–C2 captured day | X and W1 SELECTED; **W2–W5 EXPLORATORY-KEEP (needs founder decision Q23)**; C1–C2 EXPLORATORY | Board 00 "W1–W5, PROPOSED"; 09-09 §4 (W2 window corrected, service not adopted) | Unbuilt |
| 13 Scoped Actions, Drafts, Requested Work | 09-15 | "···" per stop type (S1–S3); drafts through interruption (D1–D3); finite requested work (R1–R5) | EXPLORATORY-KEEP (Sep 12 coverage; draft retention Q14 proposed) | Plans handoff §Sep 12 | Unbuilt |
| 90 Appendix · Change States | 09-11 | Pending / failed / unknown, safe retry, stale alternative, return ≠ booking | REFERENCE (behaviour donors for Entity 16 and Places) | Board 00 | Engineering truths |
| 91 Appendix · Coverage, Arrival, Peers | 09-11 | Conditional (W1/W2), arrival cues, peers (P1 DEFERRED, P2 WITHDRAWN), outcome carry-forward | REFERENCE | Decision 09-05 (PR-1 deferred, PR-2 withdrawn) | — |
| 92 Appendix · Interactive Prototype | 09-11 | Scripted regex prototype with failure injection | REFERENCE (research chrome) | Board: "not evidence for… natural-language flexibility" | — |
| "Before shared package" ×13 | 09-11 | Pre-adoption originals | REFERENCE (archive candidate) | 00 | — |

There is no board 10 in this project.

---

## 3. Canonical target set per surface (the implementation reference now)

Principle: register only frames whose status is ADOPTED or SELECTED **and** whose contents do not depend on an unadmitted kind or an unadopted service. Anything else becomes a caveat or a follow-up.

The committed 09-11 snapshot (`docs/design-archive/design-language-2026-09-11/`) already holds Home 00–16, Places 00–09, Entity, Life and Plans. **Home 17–24, Places 10 (09-21 state), Life 04b/04c/08/09 (09-21 state) and Plans 12/13 (09-15 state) need a new dated snapshot** before they can be registered by path.

### 3.1 Home (`home-root`, the H1 lane with `designRefs: []`)

**Recommend registering now:**

| Situation / posture | Board · frame | Why |
|---|---|---|
| Available / ordinary | **02 · SELECTED ORDINARY (Sun Sep 6)** | 09-09 adopted; benefit-led read; the sequence ("Today, in order" = `horizon_prepared_alternatives`, admitted 09-05); Maya's note received directly |
| Quiet (after a trip) | **02 · SELECTED QUIET (Thu Sep 3)** | 09-09 adopted; paired evidence |
| Returned day 0 | **03 · SELECTED POST-RETURN (Aug 28)** | 09-09 adopted |
| Return after absence | **03 · SELECTED RETURN AFTER ABSENCE** | 09-09 adopted; pairs with 11 (proposed) for the continuity kinds |
| Ordinary with a friend's originals (H1 "evening involving other people" / receiving) | **18 K**, with **18 L** for 1.3× | Selected 09-21. Scope: register K for composition and hierarchy only. The pictures are stand-ins (no approved PH set), and the In-motion refund row is the unadmitted money row (C-05) |
| Cold / thin | **04 "after" first open** + 02 thin unit study | Reference for invitation/sample; apply 15.3 (sample optional, not an input tax) |
| Healthy live / trip day | **03 · SELECTED TRIP DAY**, as composition and breadth reference only | Adopted 09-09. It uses the temporal strip, work receipt and money row (unadmitted), so register with the caveat "kinds pending C-05" |
| Crown arbitration / recovery | **08 row three** | Pass grammar adopted; the order is provisional (Q-H1) |
| Large text | **09b** (six selected scrolls at 1.3×) | Selected; unruled |
| Away result → destination → return | **17** (H-130 to H-138) | Coverage reference. Destinations are owned by Plans, Entity and Social |

**Recommend *not* registering yet (adopt by decision first):**

- **Live lane D (22 D) + coupon T2 ink/cream (23) + place card (24.4 / 19).** The founder chose these 09-23, and 24.4 is the design agent's resolution of a founder question. They are coherent and consistent with the 09-05 pass grammar ("the L1 pass renders on Home only inside its live window, and there it is the crown").
- They still conflict with three written rules (C-03, C-04, C-06):
  - the kernel oxblood law (oxblood = live threshold / live position; lane D uses green for live and oxblood only for urgent);
  - the contract's Live posture ("route instrument, compact field");
  - "Home owns no objects" (the place card).
- The shared `Ticket` live variant is only *requested*.
- **Recommendation:** a short decision record, "Live = the situation's own object goes live (dark stock, torn stub, pulse); an optional coupon of one to four fitting items; no live object without evidence; unfamiliar/no-plan uses a Places-owned place projection", amending kernel §oxblood and contract "Posture acceptance". Then register 21.1 (cream pass), 21.2 (urgent), 21.3 (gate with coupon), 20.1/20.2 (evening decision) and 19.1 (place card) as Live and Urgent references.
- Until then, **Live stays designed-but-unadopted**. H1's "healthy live/travel" case should be judged against 03 TRIP DAY plus the contract's "Live is not attention protection".
- **20 and 21 in full** are proposed studies. Keep them as coverage donors. Do not use them as parity targets, because 21.1 depicts an unadopted monitoring responsibility (C-07).

### 3.2 Places field (`places-root`; legacy `places-workspace`)

- **Register:**
  - **P01.1** (populated field) and **P01.2** (cold)
  - **P03.1–03.4** (the four absences told apart: missing history, missing friends, bounded supply, unavailable information)
  - **P03.7–03.9** (correction; adopted)
  - **P04.7–04.12** (1.3× checks)
  - **P07** (kit)
- **Register behaviour references for the chain:** **P02 E1–E5** (exploration and return) and **P02 P1–P6** (practical chain; adopted behaviours).
- **Hold:**
  - **P10** (scope and map/list return). Proposed; register after a ruling.
  - **P05's five ordering decisions.** The field composition itself is "an adaptable composition, not a permanent section order" (P05 decision 1). Build should treat 01.1 as an **example** layout, not a fixed section order, until P05 is accepted.
- **Places root contract:** replace the "Vesper Root Boards" Places pages with P01/P03/P07 as render authority, and keep 08-30 anatomy as rule authority.

### 3.3 Place / entity page (`entity-object`)

- **Register:**
  - **E06** (shell: plate, kicker, byline, pair, verbs, closing row, where row)
  - **E14 R1–R5**, with **E14 R2 as the protected destination reference**
  - **E06B** (arrival and large text)
  - **E04** people-slot states (form only; sheet actions are design-only)
  - **P08.1–08.6** state readings: material change, pending, listing unreachable, closed for good
- **Reconcile first:** P08 draws the Places "register" form (HOURS / THE ROOMS / TICKETS) and an anchor head. E06 draws the FactPair and closing row. The 09-09 decision selected "stable identity and shell", and P08's own table selects "Entity's invariant shell". **Use E06 chrome and P08 reading logic** (C-10).
- **Hold:** E09–E12 (non-canonical; E09 conflicts with 09-09) and E16 (proposed coverage).
- **Promote:** E06 + E14 into `docs/surfaces/entity-object/design-refs/`, as the contract already asks.

### 3.4 Life (`life-root`)

- **Keep** the promoted archive-25 reference.
- **Add from the current project:**
  - **Life 01** (four lenses at rest, current wording)
  - **02** (ordinary / thin / zero; zero-record illustration missing)
  - **03** (dossier grammar)
  - **04** (pass family; Everything kept)
  - **05** (refind; behind a flag)
  - **07** (people)
  - **08** (source reader; partly built)
  - **R0** (chip 32 pt, pass)
- **Hold:** P1–P4 (pending R1–R6 and owners) and 04b/04c (Review; shared-photo-asset gap).
- Build-truth note for the Map: Threads is not served, Returns have no producer, and friends' notes are not in the Life corpus. The adopted design is far ahead of the build.

### 3.5 Plans page (`trip-itinerary` / Plans)

- **Replace** `'Vesper Itinerary.html'` (pre-pivot) with:
  - **07** (the seven sentences as rule authority)
  - **03 B1–B7** (Kyoto: the readable arrangement over the native itinerary)
  - **02 A2 / A9 / A10** (loose and order-less)
  - **08 P1–P11** (one Ask pill and value-first stop sheet; P2 matches the built `PlanStopAssistance`)
  - **11 I1–I1c** and **09 J2f** (prepared proposal; built)
  - **05 D3** (Update & send)
  - **13 S1–S3** as the "···" reference (proposed)
- **Hold:** 04 (guest), 12 W2–W5 (following) and 91/92.
- **01** stays the as-built comparison.

---

## 4. Contradictions

Severity: **H** = blocks correct implementation or misleads a build lane · **M** = must resolve before adoption of the affected area · **L** = labelling or cleanup.

| # | Statement | Boards / docs | Sev | Recommended resolution |
|---|---|---|---|---|
| C-01 | Entity 09 (and its Read Me description) still states the invariant-body rule ("the context adds one line and never a fact"). The 09-09 decision rejected it and ordered the lab to "reconcile active 09/11/12 and its indexes with 14 rather than leaving two competing specs". Not done: 09/11/12 are unchanged since the 09-11 vdl rewrite. Places 08's table still says the amendment is "proposed, not adopted" | Entity 00, 09, 11, 12; Places 08 (row "Where the exchange stands"); decision 09-09 §1 | **H** | Mark E09's body rule SUPERSEDED in-board; keep only the context/Back matrix; relabel the P08 row "accepted 09-09"; make E14 the Entity index's current page body |
| C-02 | Home 22 still prints its original recommendation ("B for the travel day and the evening… A for the new city") and draws D1 as "the map, live". The founder selected D (response §29), and 24.4 / §30 replaced the Home live map with a place card ("Maps stay in Places") | Home 22, 19, 24; response §29–§30 | **M** | Add a "Selected: D (09-23); D1 superseded by 24.4" stamp on 22; retire the D1 frame or mark it historical |
| C-03 | The kernel says oxblood means exactly one thing: "a live threshold in the world" (urgency StatusMeta, live-position rings; ratified 08-29/08-31). The 09-05 pass-grammar decision gives the live pass an "oxblood threshold". Lane D instead uses a **green** pulse (`state.live #6B8F5E`, "new to Home's paper" per 22's own risk note) for live, and oxblood only for urgent | `design-kernel-extraction-2026-08-29.md` palette ruling; decision 09-05 pass grammar §3; Home 22 D, 23, 21.2 | **H** (for Live adoption) | Founder ruling: either (a) green = healthy live, oxblood = urgent/threshold (amend the kernel and §3 of the pass-grammar decision), or (b) keep oxblood for live and drop green. Record it in a decision before any native Live treatment |
| C-04 | The Home contract's "Posture acceptance" defines Live as "route instrument, compact field" (from R1). The same contract says "Live posture is not an attention-protection fact". The 09-23 Live studies restore breadth (21.3) and replace the route instrument with the situation's object (lane D) | `home-root/contract.md`; R1; Home 19–24 | **M** | Amend the contract posture line when lane D is adopted; R1 becomes REFERENCE-historical for Live |
| C-05 | The adopted 03 TRIP DAY scroll and the selected 18 K contain the three **unadmitted** kinds (temporal strip, work receipt, money row: "Rome refund" in In motion). 09-09 says the selection "does not… admit proposed new kinds", and the contract says "a new kind requires a canon event" | Home 01, 03, 08c, 18 K; decision 09-05 §4; 09-09 §3; contract rule 4 | **H** (for H1 parity) | Founder canon event: admit the three kinds (the union becomes 38), or rule them compositions of existing kinds. Until then, register 03 TRIP DAY and 18 K with a "kinds pending" caveat |
| C-06 | Home 24.4 / 19 draw a Home-owned "WHERE YOU ARE · Red Hook" place card (neighbourhood identity, facts that end, the way back). Canon says "Home owns no objects; every door lands on an owner", and the neighbourhood is an Entity container (E03) and a Places pocket (P01 "Red Hook, by ferry") | Home 19, 24; Entity 03; Places 01; Home 08 door map | **M** | Define the card as a **projection of the Places/Entity container** with a door to it (no Home copy). Places owns the neighbourhood facts |
| C-07 | Home 21.1 draws an accepted monitoring responsibility ("Gate and delay changes · told to you here and by notification, until you board · YOU ASKED · ENDS AT BOARDING"). Decision 09-09 "accepts no… watch service"; Places D2 and Plans W1 say "a check is one look, not a watch"; Plans W2–W5 following is PROPOSED pending founder Q23 | Home 21.1, 21.3; decision 09-09 §4; Places 02 P2; Plans 12 W | **M** | Keep 21.1 labelled "depends on Q23 following service". Rule Q23 once for Plans and Home |
| C-08 | Home 20.1 offers "Keep seven / Move to eight" as two buttons after a friend's ask. The 09-09 decision chose the proposal route over an ambiguous "Move to eight…" for Social 03.5 and requires exact effect labels ("Send proposal is never an update alias"). Nora is the host, so a direct owner change is legitimate only as the D3 "Update & send" | Home 20.1–20.2; Social 03.5; decision 09-09 §2 | **M** | Relabel 20.1's action with its exact effect ("Move to eight and tell everyone" = D3 preview), or route it through a proposal |
| C-09 | The design references in contracts and QA predate the projects. The Home and Places contracts cite the Aug 30/31 Root Boards. The governance registry covers the pre-pivot `trips-home` / `places-workspace` bundle. `home-root` has `designRefs: []`, and `trip-itinerary` refs a pre-pivot Discover design. The registry's copy policy forbids repo HTML, while two HTML snapshots are committed and `life-root` has a promoted HTML ref | Contracts; `home-surfaces-design-authority.json`; `surfaces.mjs`; `docs/design-archive/*` | **H** (measurement) | Create one registry entry per surface pointing at the §3 frames, via the dated snapshot mechanism the 09-11 archive established. Amend the registry's copy policy to "dated archive snapshots allowed; no copies in product code" |
| C-10 | Two place-page chromes. Places 08 uses anchor + sentence + plate + a "register" (HOURS / THE ROOMS / TICKETS). Entity 06/14 uses kicker + name + FactPair + closing row. Both claim the "invariant shell" | Places 07, 08; Entity 06, 14, 15 (missing variants) | **M** | Adopt E06 chrome (built on main) and P08 reading logic; add the register as a FactPair / closing-row variant request to the workbench |
| C-11 | Shared package drift. Home and Places are on vdl-stage1 **0.4.1** (OriginalReader 13,559 B). **Entity and Life are on 0.3** (11,643 B). Plans has no manifest. The 0.4 consumer list named Entity, but Entity never took it. `vdl.css` reads "0.3" in every project | `vdl-consumed.json` (Home, Life); `vdl-package.json` (Places 0.4.1, Entity 0.3) | **M** (Entity: reader instances; E14 R4 "direct original" is a missing variant) / L (Life: retrieval only, per its note) | One-file copy of OriginalReader 0.4.1 into Entity and Life; add `vdl-consumed.json` to Plans and Entity; bump the `--vdl-version` string at the workbench |
| C-12 | Region headings: design vs build. Home 11 maps Now = no heading; Horizons = "Today / This week / Worth knowing / The city this week"; Continuity = "Since you last looked / From the trip / Continuity". Native v2 renders "Needs you now" / "Coming up" / "Now", "From the trip" / "Carried forward", and v1 "Ways the world can open". Everyday Outcomes are mislabelled "From the trip" (CR24-06) | Home 11; `HomeRootV2Screen.tsx:66-107` (per the 09-25 code inventory) | **M** | Rule 11's mapping (proposed since 09-06) and align the renderer labels |
| C-13 | Life photographs are "riso placeholders" (Life 00), and Life keeps "one riso keepsake per page" and a riso zero-record illustration. The kernel says "illustration renders possibility / photography renders evidence". Entity ruled "photo or nothing — no riso" (09-03), and the founder rejected riso processing for photos (Home 13, 09-08) | Life 00, 01, 02, 04; Entity 06; Home 13 | **M** | Replace riso photo placeholders with the shared PH stand-ins (as 04b already does). Keep riso only for non-evidence illustration (the zero record), and state that rule once |
| C-14 | Home 00 marks 15 "15.3–15.4 selected (09-09 decision); the rest proposed", but decision 09-09 also accepted "15.5–15.7's local shortening treatment" | Home 00, 15; decision 09-09 §3 | L | Relabel 15.5–15.7 "accepted (local shortening only)" |
| C-15 | Chip size: the pass-grammar decision specifies the Home chip at **h26**; Life R0 adopted **32 pt**; a shared **30** is proposed (Home 09 chip study); the vdl Ticket has no 32 pt chip variant | Decision 09-05 §2; Life R0, `vdl-consumed.json` "missing variants"; Home 09 | M | One ruling (26/30/32) and a Ticket chip variant at the workbench |
| C-16 | Places 05's five decisions are "PROPOSED, NOT ACCEPTED", while P01 (their expression) is the adopted field (09-09) | Places 01, 05; decision 09-09 §3 | M | Rule P05 1–5 (or explicitly adopt 1–4 and let decision 5 be replaced by 09-09 §2's wording, "the person sends") |
| C-17 | Both Home 20 (evening: "one shared decision") and Places 02 P1–P6 (practical chain around the same kind of dinner: check → proposal → move) put a "move dinner" consequence in front of the person. The social split sends shared consequences to Home, and the seat law allows one present-delivery seat | Home 20; Places 02 P4–P5; decision 09-05 §2; Life 19 seat law | M | Rule: Places carries the consequence only inside an exploration the person started. Home carries it when it arrives unasked. Never both on one open |
| C-18 | Life 04c starts its Home path from **Home 18 D** ("Last night" region), which Home marks "a study, not the selection" (K is selected) | Life 04c B1; Home 18 D/K | L | Re-point 04c B1 to 18 K's region |
| C-19 | Life 00 header "SEP 6 · EIGHTEEN BOARDS" (21 exist). Home 24 is labelled "Exploration" although it drove 19's rebuild. Plans 00 cites the kernel projection "@ e4eff7ca, 07-25" while its `styles.css` matches the shared kernel copy (29,657 B) | Life 00; Home 00; Plans 00 | L | Label refresh |
| C-20 | Plans stamps "EXPLORATION · NOT CANON" on every board, including 07, which carries the founder-ruled seven sentences and 09-09 amendment, and 08/11, whose frames are adopted | Plans 07, 08, 11 | L/M | Add an "ADOPTED" band to 07, 08 P1–P2 and 11 I1–I1c |
| C-21 | Build vs design: flagged `CurrentShapeSurface` renders SETTLED / FLEXIBLE / OPEN / CHANGED / UNKNOWN sections, though the 09-05 ruling prohibits status buckets. `m1-plan-repair.md` ("group accepts one governed mutation") conflicts with sentences 3 and 6 | Plans 07; `travel-app` `CurrentShapeSurface`; `docs/release/m1-plan-repair.md` | M | Retire the flagged composition; mark the M1 doc historical |
| C-22 | Home contract rule 1 gates the pull door on "at least two distinct **trip-shared friend-save** contributions". The design's friends scope is casual shares of any kind (06; decision 09-05 §2) | `home-root/contract.md`; Home 06 | M | Rebase the contract condition on the friends-scope read, not trip-scoped saves |
| C-23 | Home 05 frames group travel as the "launch wedge", while the accepted strategy is everyday-first ("travel is a specialization", 09-06) | Home 05; decision 2026-09-06 | L | Relabel 05 as the group-travel specialization |
| C-24 | "T2" means two things: tray T2 (coupon, board 23) and grant tier T2 (R4, C&C T0/T1/T2) | Home 23, R4 | L | Rename the tray "coupon" everywhere in specs |

---

## 5. Open design questions for the founder

1. **Crown order (Q-H1).** Confirm or change recovery > live commitment > decision with a deadline > forming arrangement, on Home 08 row three. Provisional since 09-05.
2. **Live grammar (Q-H2).** Adopt lane D + coupon + the no-evidence-no-live rule (22 D, 23 T2 ink/cream, 21.1–21.3) as canon? Rule the colour (C-03) and the posture wording (C-04).
3. **New city (Q-H3).** Place card (24.4 / 19.1) versus live map (22 D1). And who owns the card (C-06)?
4. **Three proposed kinds (Q-H4).** Admit temporal strip, work receipt and money row (Home 01, 03 TRIP DAY, 08c, 18 K), or treat them as compositions (C-05)? Also: generalize the strip and receipt beyond trips (review H10)?
5. **Following / monitoring (Q-X1).** What service promise exists? Home 21.1 "ends at boarding", Plans 12 W2–W5 (Q23), Home 17 H-133 "checked once · not watched".
6. **Home 11 region headings (Q-H5)** and the 12/15.4 secondary-question route: adopt 11's mapping (C-12)?
7. **Home social states (Q-H6).** Adopt 10 (withdrawal, narrowing, block, occasion lived through, kept intention, attributed friends)? Also the block frame 4→3 attendance inconsistency (10.3).
8. **"Where my friends are" (Q-H7).** Confirm the semantic, never-biometric reading. Open on Home 00.
9. **Places field order (Q-P1).** Accept P05 decisions 1–5, and decide whether a kept possibility or the day's best world offering leads (P01).
10. **Places scope and map (Q-P2).** Accept P10 A (scope never implies presence) and B (marker ↔ row, provider return)?
11. **Places end (Q-P3).** Does Places want Home's week seam, or the three tail doors (P01)?
12. **Kept intention owner (Q-X2).** Owner and storage for "an intention without a named Plan". This blocks Places C7, Entity 10, Life P1 (R1–R6, pending since 09-04) and Plans 02 A2/A7 (runtime needs a Trip).
13. **Place-page chrome (Q-E1).** E06 FactPair / closing row vs P08 register (C-10). Also: container page (town as door) and spot admission (E03)?
14. **Entity face sheet (Q-E2).** "Keep her words" as a distinct permitted copy (E12.4 / Life 07.7), and the confirmation projection owner (E12, Plans Q5).
15. **Life P-boards (Q-L1).** R1–R6 (AHEAD, three keeps); P2 stability laws; P3 saved-piece custody; P4 kept-path contract amendment.
16. **Photos (Q-X3).** Approve one real or licensed PH-01..07 set (ledger §10). Home 18, Life 04b/04c and Social 10 cannot be judged without it.
17. **Chip size (Q-X4).** 26 / 30 / 32 (C-15).
18. **Guest without account (Q-X5).** Home 20.5, Plans 04 C2 (Q9/Q16); 09-09 accepted no broader guest audience.
19. **Plans type roles (Q-PL1).** The four proposed token changes (12 pt times, 15 pt Roman opener, 11 pt stamps, 13 pt support) and the preview-card material (07).

---

## 6. Design debt and cleanup

**Before-copies (safe to archive once the 09-11 snapshot is confirmed complete).** The committed snapshot already preserves the originals.

| Project | Before-copies |
|---|---|
| Home | 6 "Before VDL 0.3" boards |
| Places | 10 `before/` boards + `support.js` |
| Entity | 9 `before/` boards + `support.js` |
| Life | 14 `before-shared-package/` boards + `support.js` |
| Plans | 13 "Before shared package" boards + `kit/plans.before-vdl.css` |

That is 52 duplicate boards. Before deleting any of them, the owner should check `docs/design-archive/design-language-2026-09-11/manifest.json` for each file. This atlas deletes nothing.

**Stale or superseded boards to archive or stamp.**

- Entity Z1–Z5 and Home Z1–Z4 (already archive; keep while Home 07 cites them).
- Entity 09 body rule (C-01).
- Home 22 D1 and its printed recommendation (C-02).
- Home 18 D/E (study).
- Places P08 "where the exchange stands" row (C-01).

**Stale indexes and ledgers.**

- Life 00 header (C-19).
- Entity 00's E09 description.
- Entity 13's capability ledger (09-04). Refresh from the 09-25 code inventory: for example, the Tonight? verb is still unwired and the context line is design-only.
- Home 00 "OPEN" block. It still says "Large-text renders have not been run", but 09b exists.

**Shared-component drift.**

- OriginalReader 0.3 in Entity and Life vs 0.4.1 elsewhere (C-11).
- `Ticket` has no live variant, road mode, wristband, leading-edge stub or 32 pt chip (Home and Life requests).
- The OriginalReader direct-entrance / nonspatial / sender-owned variants are queued (Places `vdl-package.json` extension_queue).
- PlaceHead needs no-plate / map-plate and provider credit.
- LocationFooter needs a per-place map.
- The FactPair link position.
- The `vdl.css` version string.
- The Home "dark live object" is drawn locally on 19–23; that is a fork risk until the workbench owns it.
- Plans and Entity lack a `vdl-consumed.json`.

**Supporting-file drift.**

- `support.js` exists in two sizes: 66,404 B (Home, Entity, Plans) and 69,150 B (Places, Life).
- Plans `kit/proto.js` (09-05) predates the 09-09 amendment. Its I1 behaviour should be re-checked before anyone cites 92.

**Registration debt.**

- There is no dated snapshot after 09-11. Home 17–24, Places 10, Life 04b/04c/08/09 and Plans 12/13 in their current state exist only in Claude Design, the Downloads exports and the uncommitted generators (`docs/working/design-gen/home/gen_live*.py`, untracked).

**Fixture debt.**

- Places 03/06/09/11/12 and Entity boards still show street addresses that are not on the wire.
- Home 21's airport noodle counter is invented.
- The Rome refund is a claim, not confirmed money owed (review).

---

## 7. Design completeness by surface

Legend: **F** = fully drawn with a selected or adopted frame · **P** = drawn but proposed or thin · **—** = not drawn.

| State / flow | Home | Places field | Place page | Life | Plans page |
|---|---|---|---|---|---|
| Ordinary rich | F (02, 18 K) | F (01.1) | F (08.1, E14 R1–R3) | F (01) | F (03 B) |
| Empty / cold / first use | F (04; 02 thin) · P (14) | F (01.2, 03.1) | F (08.2; E06B sparse) | F (02 zero, but the illustration asset is missing) | P (02 A2 loose; no "no plans" page is drawn) |
| Thin / week two | P (02 unit study, 04 next open) | F (03.2) | F (sparse page) | F (02) | F (02 A9 order-less) |
| Degraded / error / stale | P (12: stale, provider unknown, import pending; 17: cancelled, signed out; 18 J image failure) | F (03.4; map unavailable on 07) | F (08.3–08.6; E16 failed / unknown / stale, proposed) | P (08.8–08.9 source won't open; 04b image failure) | P (90; 13 D3 Notice) |
| Large text / narrow | P (09b, 18 L, 19.7, 21.8; native Dynamic Type unverified) | F (04.7–04.12; 10 B7/B8) | F (E06B) | — (no Life board at 1.3×) | P (03 B7, 12 X4b) |
| Live (healthy) | P (03 TRIP DAY adopted; 19–21, 24 proposed; lane D selected, not adopted) | P (02 P1–P6 around a dinner; 08.11 "at the pier") | P (Tonight? verb design-only) | — (Life stands down; P3.4 captured day) | P (05 D) |
| Urgent | P (08 row 3; 21.2) | — | — | — | P (05 D4 mismatch) |
| Offline | P (21.6 item by item; 12 stale) | — | — | P (08 offline source) | — |
| Social: receive | F (02 note; 18 K; 06) · P (10) | F (02 H1–H4) | F (E14 R4; E04) | F (07) | P (04 C3, C4) |
| Social: coordinate | P (20; 05) | F (02 P2–P4; adopted behaviour) | P (E10 "consider for Maya's dinner") | P (P1 together-ahead) | F (11 I1, 05 D3 adopted) · P (04 guests) |
| Correction / wrong inference | P (15 steering adopted locally; 19.4–19.5; 21.4) | F (03.7–03.9 adopted) | — | P (P2) | F (09 J2b) |
| Return / exact scroll | P (17; 18 path pictured; scroll retention unverified) | P (02 E5; 10 B6/B9) | P (E09 Back matrix; E12 return ≠ booking) | P (04c; 05 Back to query) | P (06 doors; 08 P11) |
| Away delivery | P (17) | — | P (E16) | — | P (13 R1–R5) |

**Per-surface notes.**

- **Home.**
  - Richest coverage. The adopted core (02/03, 08 pass grammar) is sound.
  - The gaps are formal rather than visual: three unadmitted kinds; a provisional crown order; Live selected but unadopted; ten proposed boards (08b–12, 14, 17) never ruled.
  - The empty and first-use story rests on a sample demonstration whose backend is flag-dark, and on world supply that does not exist for NYC (no weather or notice source). Design is complete; supply is not.
- **Places field.**
  - Complete as a static experience, and its absences are unusually well drawn (03.1–03.4).
  - It is almost entirely fixture-driven: dated occurrences, transit headways, tides, photos (0 %) and seat inventory have no supply.
  - Interaction (P10) is proposed. The ordering decisions are unaccepted.
- **Place / entity page.**
  - The most build-ready of the five (E06 largely on main behind a flag).
  - What remains: the purpose-responsive body (E14; the context line is not built); reconciling the Places register with E06 chrome; face-sheet actions; interstitials. Entity 16's check service does not exist.
- **Life.**
  - The adopted design (01–07) is complete for ordinary, thin and zero states, but there are no large-text boards.
  - The whole payoff layer is drawn but unbuilt: Returns, Carried forward, Threads, custody verbs.
  - The future half (P1 AHEAD, kept intention) is blocked on one owner decision.
- **Plans page.**
  - Rules are adopted (07). Composition refinements are illustrated on the native itinerary baseline (01). Contextual Ask and Send proposal are built.
  - Multiplayer (04), following (12 W) and requested work (13) are proposed.
  - No "no plans yet / cold" Plans page is drawn: by design, a loose intention lives on its owner (A9).
  - No participant walkthrough exists. Board 07's revisit trigger depends on one.

---

## 8. What this atlas did not verify

- Pixel-level rendering of every board. Only the Home 00/19–23 text was re-read live.
- Native behaviour and any participant evidence.
- Whether the Social project's 10P "Share 1" frame (flagged by Life 04c) has since changed.
- The Life & Anchors archive (`f524c7f0`) and the Home & Places canon project (`a26e3228`), except where the decisions cite them.
- Etag timestamps are the design server's write stamps. One case (response §30 dated September 26 against 09-23 etags) shows write-up dates can trail board dates.
