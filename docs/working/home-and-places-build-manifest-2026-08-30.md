---
doc_type: working
status: active
owner: founder / design / frontend / backend
created: 2026-08-30
last_verified: 2026-08-30
expires: 2026-09-29
why_new: The canon boards render compositions but nothing enumerates the unit taxonomy behind them or maps it to build status — and the §11.5 locus-of-generation ruling requires bounded kind-unions per root, which makes the taxonomy itself the contract. This is the post-pivot successor to the old canvas's "Build Manifest — Both Surfaces."
promotes_to: null
supersedes: []
source_of_truth_for:
  - the Home and Places unit taxonomy and its build ledger
depends_on:
  - docs/working/design-kernel-extraction-2026-08-29.md
  - docs/working/home-surfaces-pre-pivot-recovery-and-post-pivot-direction-2026-08-27.md
  - docs/working/places-consumer-experience-anatomy-2026-08-29.md
  - docs/working/post-return-new-york-home-possible-worlds-gallery-2026-08-28.md
  - docs/working/home-and-places-five-world-fixture-pack-2026-08-29.md
---

# Home and Places — Build Manifest

## Decision

Enumerate every unit kind that appears on the canon, fixture, handoff, and
stress boards for the new Home and Places roots; give each a stable kind
name, its containment posture, its evidence gate, and a build grade against
the code that exists today. Per kernel §11.5, roots render from **bounded
kind-unions, server-chosen** — so these tables are not documentation of the
design; they are the first draft of the unions the resolvers will be typed
against.

Build grades: **EXISTS** (substrate and renderer live today, possibly under
old names) · **ADAPT** (real substrate exists; carrier, projector, or
renderer work needed) · **BUILD** (net-new). Grades were checked against
source on 2026-08-30 (`places_sections.py` reasons, `trips_stack_models.py`
receipt kinds, the component catalog, and the kernel doc's authority map);
unverified claims say so.

## 1. Home — the region-kind union

### 1.0 Chrome and read

| Kind | What it is | Containment | Evidence gate | Grade |
| --- | --- | --- | --- | --- |
| `world_read` | Two-tier read (§11.6.1): mono anchor + two-line serif read in standfirst voice; merge rule for voiced dominants | chrome, never a card | location scope + one true condition; read must beat silence | **BUILD** — producer + voice contract are new; mast type role exists |
| `root_shell` | Four-root tab bar | chrome | — | EXISTS dark (`fourRootShell.ts`, flag-gated; icons placeholder per ruling 7) |
| `week_shape` | The seven-day strip: the week's held form (today, marks, one avatar day) | containment step 3 — a diagram, not an object; zero demand | occasions/commitments from canonical state only | **BUILD** — ruled in 2026-08-30 with the Quiet floor (kernel §11.12.5); the old canon's day-strip primitive, finally used |

### 1.1 Now — the dominant union (exactly one renders)

| Kind | Seen on | Containment | Grade | Substrate notes |
| --- | --- | --- | --- | --- |
| `now_commitment_instrument` *(renamed from `now_route_instrument`, kernel §11.12.9)* | Live posture; Live Reduction compact; C1 ticket dominant | crown (step 5) | **ADAPT** | crown anatomy shipped; map-grammar renderer is BUILD (see §3) |
| `now_prepared_possibility` | Available; World F Saturday | crown | **ADAPT** | crown + spine receipt exist; composer selection is new |
| `now_decision` | Planning ("two decisions open") | crown | **ADAPT** | proposal/decision substrate live (`proposal_approval`, `call` receipt) |
| `now_recovery_instrument` | F5 disruption | crown, oxblood register | **BUILD** | provider-state + prepared-work + honesty band; movement domain partial |
| `now_temporal_posture` | F2 ("Wait until noon") — CTA-less crown | crown, no CTA | **BUILD** | monitor authority, threshold, expiry — new semantics |
| `now_annotated_evidence` | F3 (dish photo) | crown | **BUILD** | photo-as-evidence per media ruling; annotation callouts new |
| `now_attributed_comparison` | F4 (two lanes) | crown | **BUILD** | grant-gated lanes; depends on contribution-&-consequence grants |
| `now_invitation` | Cold posture | crown | **ADAPT** | cold-start loop shipped previously; recompose |
| `now_merged_into_read` | Quiet, Returned·Day-0 | none — promotes into `world_read` | covered by `world_read` | ruling §11.6.1 |

**Now-union laws (adopted 2026-08-30, from the pre-pivot crown prototypes):**
1. **The identity gradient** — every Now dominant's biggest slot holds the
   most specific true thing about its subject (route → the path; decision →
   the open question; recovery → the provider offer; evidence → the
   photograph; comparison → the two lanes). This, not shared chrome, is
   what keeps nine dominants reading as one anatomy.
2. **The structure gradient** — receipt and structure fall off with the
   subject's own structure: a full instrument carries a sequence and a
   burden receipt; a prepared possibility carries a read and a door; a
   voiced moment carries nothing and merges into the read. A dominant may
   never carry more structure than its subject truly has.
3. **The Move (adopted as object model):** a prepared possibility that is
   offered, ignorable, and expiring — no row, no task, no trace on expiry
   ("Expires at 23:00 · nothing is saved"). `now_prepared_possibility` and
   Home openings render Moves, never durable objects; acting converts a
   Move into a real Plan/Occasion through the owning capability. This is
   the gallery F8 law ("understood and ignored; never an automatic save")
   given its substrate. **Amendment (kernel §11.12.6): a Move always
   ships with its basis — the why-this trail renders inline; an
   unexplained Move is inadmissible.**

### 1.2 In motion

| Kind | Containment | Grade | Notes |
| --- | --- | --- | --- |
| `motion_occasion_row` | uncarded row | **ADAPT** | ListRow anatomy exists; Occasion substrate is the pivot's own object |
| `motion_loose_end_row` | uncarded row | **ADAPT** | watched-claim semantics; `call`/agent-work substrate |
| `motion_all_plans_door` | Door | EXISTS | `Door.tsx` shipped |

### 1.3 Horizons

| Kind | Containment | Grade | Notes |
| --- | --- | --- | --- |
| `horizon_editorial_passage` | uncarded + 56pt plate | **ADAPT** | ruling 8 ratified the plate; the C6 image slot on rows is drawn-never-built — cheapest build in the ledger |
| `horizon_mechanism_row` | uncarded + plate | **ADAPT** | same anatomy, mechanism content |
| `horizon_aperture_row` | uncarded row | EXISTS-ish | `saved_unplaced` kind is live in both unions today |
| `horizon_hidden_system` | uncarded + mini diagram | **BUILD** | bounded-mechanism content + diagram unit |

### 1.4 With people

| Kind | Containment | Grade | Notes |
| --- | --- | --- | --- |
| `people_note_door` | uncarded row (door — ruling 3) | **ADAPT** | facepile + `people` receipt exist; grant checks BUILD |
| `people_participants_row` | uncarded row | EXISTS | `people` receipt (seats/facepile) |
| `people_waiting_row` | uncarded row | EXISTS-ish | `group_waiting` reason live in Places union; re-home |
| `people_authorized_door` | Door | **BUILD** | renders only under may-use; silent-yield otherwise |
| `people_gathering` | quietPanel — the group as subject | **ADAPT** | the pre-pivot "room" restored (regression fix, 2026-08-30): facepile at weight, the gathering itself carded as the thing that matters now; facepile + seats substrate exist |
| `people_status_aperture` | uncarded row/aperture — a person's returned/available status as a doorway ("JUST BACK · 10 DAYS") | **ADAPT** | ruled in 2026-08-30 (§7 resolution; already accepted wave-0 §1 A15); featured-Status substrate; renders in any region per R1 |

### 1.5 Continuity

| Kind | Containment | Grade | Notes |
| --- | --- | --- | --- |
| `continuity_capability_field` | 2pt gold left rule | **BUILD** | reusable-distinction ledger; feeds from lived-experience engine |
| `continuity_since_you_looked` | gold rule @45% | **ADAPT** | `diff`/`changed` substrate exists |
| `continuity_life_door` | Door | EXISTS | door to Life root |
| `continuity_settling` | crown (Returned·Day-0 dominant) | **BUILD** | import/settling status from Life ingestion |
| `continuity_voice_horizon` | voice italic, uncarded | **BUILD** | no-deadline thread; never auto-saves (gallery F8 law) |
| `continuity_reconstruction` | evidence-first paired timeline | **BUILD** | adopted 2026-08-30 (gallery §10 / worlds E3–E4/F7): the intended/actual sequence from receipts and movement rows — "what actually happened," never a trip report |

**Home union: 31 kinds** *(week_shape + people_status_aperture ruled in 2026-08-30)* (2 chrome + 9 Now, of which one folds into
`world_read` + 3 Motion + 4 Horizons + 5 People + 6 Continuity — 28
renderable). The union is the type the Home resolver emits; adding a kind
is a canon event, not a feature PR. *(Counts corrected 2026-08-30 after
the coverage audit; `people_gathering` and `continuity_reconstruction`
adopted the same day.)*

## 2. Places — the state-unit unions

### 2.0 Chrome (all states)

| Kind | Grade | Notes |
| --- | --- | --- |
| `scope_handle` (narrowing NEW YORK → RED HOOK → RED HOOK·ACCESS) | **BUILD** | the state machine + persistence contract (fixture brief §3) |
| `provenance_label` ("FROM HOME · …") | **BUILD** | rendered from the projection envelope |
| search / map-composition affordances | EXISTS | current search overlay + map routes; must adopt the typed context envelope |

### 2.1 World Field

| Kind | Containment | Grade | Notes |
| --- | --- | --- | --- |
| `field_lead_composition` | leads by size on bare paper | **BUILD** | map field + proposition + interval; the composer is the admission compiler's first client |
| `field_branch_lead` (56pt) / `field_branch` (44pt) | uncarded rows | **ADAPT** | `nearby_set`/`candidates` substrate; the *different-access-structure* selection rule is new |
| `field_returned_understanding` | gold left rule | **BUILD** | the one-Europe-unit; needs the lived-experience transfer substrate |
| `field_continuity_doors` | uncarded rows | EXISTS | saved (`saved`, count-toward law), map door, plans door |
| `field_balanced_fallback` | orientation state | **BUILD** | the no-strong-lead degradation (ordinary-open board) |
| `field_browse_shelf` | kicker + 2-up gallery cards w/ riso media | **ADAPT** | ruled in 2026-08-30 (founder: Places "can benefit from a little browse"); the old Places feed's gallery grammar (`g2`/`gmedia`), admitted by the same compiler — every item keeps one reason + one burden; below the lead, never leading |
| `field_editorial_cover` | full-bleed illustrated cover + scrim | **ADAPT** | ruled in 2026-08-30; the old `ov`/`ovscrim` editorial cover; media doctrine: illustration = possibility; at most one per field |

### 2.2 Place Focus

| Kind | Containment | Grade | Notes |
| --- | --- | --- | --- |
| `focus_identity_map` | media/map is the object | **ADAPT** | mapSurface/mapTokens exist; place-scale framing new |
| `focus_verdict` | uncarded serif + mono basis line | **ADAPT** | Take/dossier thesis substrate exists; conviction stays producer-less (ruling 4) |
| `focus_relationship_trace` | uncarded, descriptive | **ADAPT** | `traveler_place_affinity` + saves live; no stage language |
| `focus_human_note` | carded evidence object (ruling 3) | **ADAPT** | attribution anatomy exists; may-use/may-name gating BUILD |
| `focus_horizon_doors` (ACCESS/TRANSFER/ALTERNATIVE) | typed door rows | **BUILD** | typed edges with stated relation + difference |
| `focus_possibility_row` | uncarded row, reason + burden | **ADAPT** | `candidates`; the one-reason-one-burden contract is new copy law |
| `focus_action_seam` | umber primary + quiet doors | EXISTS | Button + Door |

### 2.3 Place Path

| Kind | Containment | Grade | Notes |
| --- | --- | --- | --- |
| `path_relation_statement` | uncarded title + serif | EXISTS (type roles) | copy law: never "Places like X" |
| `path_difference_diagram` | diagram, border-only | **BUILD** | new instrument family (diagram-only-when-spatial, map-grammar ruling) |
| `path_distinction_rows` | mono kicker + sans, ≤3 | **ADAPT** | render exists; evidence-count gate new |
| `path_evidence_apparatus` | uncarded numbered trail + italic analogy limit | **ADAPT** | the C2 citation contract — receipt union carries it; apparatus renderer new |
| `path_consequence` | gold rule + Door | **ADAPT** | ConsequenceBanner family |
| `path_next_rows` | uncarded rows, **≤2 (conflict settled 2026-08-30 — the brief's stricter number wins)**, typed | **ADAPT** | remove-rather-than-generic rule |

### 2.4 Live Reduction

| Kind | Containment | Grade | Notes |
| --- | --- | --- | --- |
| `live_instrument` | crown; map + sequence as one path | **ADAPT** | spine receipt EXISTS and carries it unchanged; synchronized map renderer BUILD |
| `live_burden_receipt` | receipt box r11 | EXISTS | receipt union verbatim |
| `live_fallback` | gold left rule, exactly one | **ADAPT** | conditions/diff substrate |
| `live_temporal_posture` | StatusMeta (oxblood ruled) | **BUILD** | ACT NOW / HOLD / WAIT / MONITOR / RELEASE semantics + reversion |
| `live_action_seam` | umber w/ creation preview | **ADAPT** | Door + plan-capability preview line |
| `live_branch_field` | two-branch consequence tree — **recovery register only** | **BUILD** | ruled in 2026-08-30: ordinary Live keeps `live_fallback`'s exactly-one; the oxblood recovery register may render the branch field (F5-P2). This also settles the singular/plural conflict: fallback stays singular |

### 2.5 Social forms (any state, grant-gated)

`social_attributed_evidence` (ADAPT) · `social_relational_relevance`
(**BUILD** — the why-it-matters sentence is generated, contract-bound) ·
`social_plural_comparison` (**BUILD**) · `social_participation_consequence`
(**BUILD** — the she-can-see-and-withdraw receipt; depends on the
contribution-&-consequence contract's grant store).

**Places unions: 34 kinds** across chrome (3) + World Field (8) + Focus
(7) + Path (6) + Live (6 — `live_branch_field` ruled in 2026-08-30) + social (4). *(Corrected 2026-08-30 — the
original "26" was arithmetic error. Grew 31 → 33 the same day: the
browse pair `field_browse_shelf` + `field_editorial_cover` ruled in.)*

## 3. Shared instruments (cross-root, build once)

| Instrument | Needed by | Grade |
| --- | --- | --- |
| Map-grammar renderer — one encoding (gold/dashed/oxblood/rings), three scales, **plus the map honesty contract** (adopted 2026-08-30 from the pre-pivot map group): segment source routed/estimated/unknown as a channel orthogonal to user commitment; minutes render only off a fresh fact; a crossing draws a bare arc, never invented geometry; hollow pin = unrouted endpoint | Home Now, all Places states | **BUILD** (stay on Mapbox per maps canon; stylized layer over camera) |
| Section header — `TITLE ——— count →`: mono label + trailing hairline rule, count/door carried in the header line; fires at chapter/region openers only | every sectioned surface, both roots | EXISTS (`headingRule` — PlacesAtoms.tsx:70, ItineraryChapterHeader.tsx; recovered onto the boards 2026-08-30) |
| "Why this?" provenance inspector — one inspectable source trail on every consequential projection, both roots (contribution-and-consequence §3.8; generalizes `path_evidence_apparatus`) | all consequential units | **BUILD** (adopted 2026-08-30) |
| Route strip (linear register of the same encoding) | Home, handoff, Live | **BUILD** (small) |
| Projection envelope (12 fields) + push-not-tab navigation + readback refresh + canonical seen | every cross-root tap | **BUILD** — the §11.4 contract |
| Admission & hierarchy compiler (§9 brief, hard gates, ranking, density taper) | both roots | **ADAPT** — 🔑 the `concierge_feed` ranker already exists and was ruled ADOPT-not-build; the gates and density taper wrap it |
| Degradation compiler (§10 rules) | both roots | **BUILD** — **compression law (ruled 2026-08-30, recovered from the pre-pivot rhythm study): compression shrinks media and drops the note; small plates stay — a row without its plate is a different composition, not a quieter one** |

| Two-tier read producer (anchor + grounded voice line + merge rule) | Home; Places cold start | **BUILD** |
| Receipt union + dispatcher | everywhere | EXISTS (12 kinds, grain-agnostic) — **`carried_forward` promoted 2026-08-30** after four independent derivations (§7 candidate, C1-F2, C2-F7, C3-F13): a standing consequence with causal lineage and an owner |
| Execution ledger — the prepared → authorized → attempted → partial/failed/unknown → readback → repair → receipt chain as one renderable carrier (C3-F11) | Home recovery, Live Reduction, Chat execution | **BUILD** — booking/hold receipt substrate EXISTS; the chain carrier is new |
| `Door`, CardSurface recipes, StatusMeta, ConsequenceBanner, facepile | everywhere | EXISTS |
| C6 row image slot (44/56 plates) | Home Horizons, Places branches | **BUILD** (one prop; drawn since old canon) |
| Photo-evidence annotation unit | F3-class content, Life | **BUILD** (media ruling) |

## 4. Migration ledger — the old inventory's disposition

**Old Places reasons (live enum, 15+):** `nearby_set`, `neighbourhood`,
`starter`, `guide`, `experiences`, `saved`, `saved_unplaced`, `changed` →
**survive as World Field / Focus selection inputs** (reasons become
admission-compiler candidates, not page sections). `anniversary`, `harvest`
→ **migrate to Life** (return/continuity layer). `friend_activity` →
**replaced** by the four social forms (the activity-feed shape is a rejected
pattern). `gap`, `expiry`, `group_waiting`, `urgency` → **re-home to Home**
(they are person-situation claims, not world claims). `reading`/`register`
→ fold into Path media (an article is a medium, not a shelf).

**Old Trips section kinds (24, by family — exhaustive rows live on the old
Build Manifest board, which remains the historical reference):** the crown
family → the Now union (§1.1); open-loops/countdown → In motion; trail/
near-you → Horizons (`near_you` receipt kind is live); group/connect → With
people; companion-reading/memory/anniversary family → Life + Continuity
doors; trip-feel/table → retired with the trip-lifecycle page model;
expense-ledger receipts → unchanged receipt union, surfaced by owner views.

## 5. The build ledger — what we actually need to build

Net-new (BUILD), roughly ordered by unblocking power:

1. **Admission compiler + degradation compiler** — every page composes
   through them; wraps the existing `concierge_feed` ranker.
2. **Projection envelope + push navigation + provenance label** — the
   §11.4 contract; unblocks every cross-root tap.
3. **Map-grammar renderer + route strip + difference diagram** — the one
   encoding at three scales; unblocks `now_route_instrument`,
   `field_lead_composition`, `live_instrument`, Path.
4. **Two-tier read producer** (+ merge rule) — Home's opening. *(Renderer half ✅ 2026-08-30: `home-root/WorldRead.tsx` implements the §11.12.2 ladder; `home-root/WeekShape.tsx` ships the week strip; the `carried_forward` receipt kind landed in the backend union, dark. The producer/selection half remains BUILD.)*
5. **Temporal-posture engine** (WAIT/HOLD/ACT NOW/MONITOR/RELEASE, monitor
   authority, expiry, reversion).
6. **Grant-gated social projector** (may-use/may-name checks,
   recompile-on-revoke, the relevance sentence, the consequence receipt) —
   lands with the contribution-&-consequence contract.
7. **Recovery instrument** (provider state, prepared-work list, honesty
   band, causal-ladder receipts).
8. **Scope-handle state machine** + typed horizon edges.
9. **C6 row image slot** — ✅ SHIPPED 2026-08-30 as `components/ui/MediaPlate.tsx` (media-doctrine textures + plate ladder); the route strip half of item 3 shipped alongside as `RouteStrip.tsx`, and the rest register as `RestClose.tsx`. First fixture screen: `components/home-root/HomeRootScreen.tsx` (Returned·Saturday) behind the dev route, smoke-tested.
10. **Photo-evidence annotation unit**; **capability field**;
    **settling/import status**; **voice horizon**.

Score, recounted 2026-08-30 (after same-day adoptions and the browse
pair): **65 kinds + 13 shared instruments → 14 EXISTS · 30 ADAPT · 33
BUILD** (one Now kind folds into chrome). More than half of both pages stands on shipped
substrate; the genuinely new engineering concentrates in five systems
(compilers, envelope, map grammar, read producer, grants) — everything else
is carriers and renderers over live data.

**§7 IS FULLY RESOLVED (2026-08-30, kernel §11.12–§11.13).** Every
candidate now has a disposition: promoted (carried-forward receipt,
why-this, `week_shape`, `continuity_reconstruction`,
`people_status_aperture`, `live_branch_field`), adopted-as-vocabulary
(focus_verdict's six registers, the seven horizon-door types,
`human_mode` folded into R2's modifiers), covered-by-existing-law
(Home social carrier → R1; availability/reunion openings → Move
content; generated compositions → provenance is a label, not a union
axis), deferred-with-trigger (layered-Place-passage — until a
composition demands it; composed-way — inside the §5.7 recovery build),
or settled (`path_next_rows` ≤2; fallback stays singular). The queue
below is retained as the historical record only.

## 7. Audit addendum — 2026-08-30 coverage findings (pending ruling)

A systematic audit of these unions against every 08-16→08-30 canon doc
found six specified-but-unrendered use cases and seven partials.
**Ruled 2026-08-30 (founder): adopted — the identity + structure
gradients and the Move (now §1.1 laws), the map honesty contract (§3),
`continuity_reconstruction`, the "Why this?" instrument, and
`people_gathering` (the group-at-weight regression fixed).** The rest
remain candidates awaiting ruling:

**Gap candidates still open:** a **layered-Place-passage** shared
instrument (source-bound timeline + live access in one unit — gallery
§10, B2); a `people_status_aperture` (the "JUST BACK · 10 DAYS"
return-Status preview — gallery D5, already accepted in wave-0 §1 A15);
a `live_branch_field` for the recovery register (F5-P2's two-branch
consequence tree — `live_fallback`'s "exactly one" holds for ordinary
Live only). *(Resolved from the original list: `continuity_reconstruction`
adopted same day; the carried-forward receipt promoted §3; the why-this
instrument adopted §3.)*

**Partials to widen:** `focus_verdict` must carry all six current-read
registers incl. the then/now diff medium (anatomy §4.2.2, §7);
`focus_horizon_doors`' type space is the anatomy's seven path types, not
the three fixture labels; Home needs a non-dominant grant-gated social
carrier (gallery D4/D6/F5 supporting positions); the possibility
small-multiple needs the `human_mode` vocabulary in the admission
compiler; an availability/reunion opening (gallery A6/C6); a
branch-level composed-way kind (recovery §8.4 walks/sequences); a Home
carrier for timely generated compositions (four-root §5.1).

**Doc conflicts to settle:** `path_next_rows` ≤2 (brief) vs ≤3
(anatomy) — pick one; `live_fallback` singular vs plural in the recovery
register (resolved if `live_branch_field` is adopted).

**From the pre-pivot boards** (mining audit, same date) — strongest
pull-forwards, pending ruling: the **identity + structure gradients** as
Now-union law (the biggest slot holds the most specific true thing;
structure falls off with grain — the cheapest coherence guarantee across
nine dominants); the **Move** as the non-durable expiring-offer object
under `now_prepared_possibility` (offered, ignored, expires — no row);
the **map honesty contract** folded into the renderer spec
(routed/estimated/unknown orthogonal to commitment; minutes only off
fresh facts; crossings as arcs); the **dissent register** ("everyone
will send you here; don't" — uncarded, lens-labeled, never oxblood); the
**lens/angle switcher** as one field on the Place projection. Also
flagged: the group-at-weight regression (With-people is all rows — the
multiplayer wedge's subject never gets the 46pt treatment), the
countdown's scale contrast, the never-built spine day-strip, and the
unresolved settle primitive.

**Deferred with an owner (2026-08-30):** the pre-pivot tally register
(26–30px mono numerals in bordered cells) is adopted as board furniture
(Build Manifest header) but has no product home in Home/Places — its
natural home is the Life root's governed history. Rule it there.

## 8. Not covered here

Per-slot copy budgets (each kind gets a content-contract instance before
mock copy — kernel §10 law); production geometry (the dedicated design
pass); Life's unit union (its own project); Chat's well union (owned by the
Chat canvas, per its founder ruling).

**Status disposition (ruled 2026-08-31, response doc §15.2-R3):** the
Product Model's Status object (one human-authored, audience-scoped
featured share) is a Life/People-program object — authoring and custody
live there. Home receives it only as a people-reservoir line under an
explicit grant, which `people_status_aperture` already covers. No
`status_*` kind is to be added to these unions.

**Relay disposition (ruled 2026-08-31, §15.2-R2):** a relay is a Share to
a new audience under the author's Audience grant — a named mechanic of
Share, not a sixth social verb. The verb set (Send · Address · Share ·
Contribute · Publish) stays closed.
