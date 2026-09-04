---
doc_type: working
status: active
owner: product / design / architecture / engineering
created: 2026-08-30
last_verified: 2026-09-01
expires: 2026-09-29
why_new: Preserves the detailed Life root anatomy, design evidence, and rejected alternatives while the compact v1 contract becomes the build-facing authority.
depends_on:
  - ../contracts/life-v1-experience.md
  - ../decisions/2026-09-01-adopt-life-v1-behavior-sequences.md
---

# Life Root — Production Spec

> Status: detailed design evidence. The compact build-facing authority is now
> `docs/contracts/life-v1-experience.md`; behavior-family rulings live in
> `docs/decisions/2026-09-01-adopt-life-v1-behavior-sequences.md`. This document
> remains the anatomy and rejected-alternative record.
> Date: 2026-08-30
> Sources: Claude Design project **"Vesper — Life & Anchors"** (`f524c7f0-0af3-46a9-8be8-a21ddbaaf4a8`), boards 00–04, 03A–03G3, 03E/03E2/03E3/03E8 (v8 = final), 03E4–03E9 (ruled exploration evidence), **01A6 · The Chip (ladder v3)**; board 05 (placement map) TABLED by founder — its contents are unruled
> Companions: `docs/working/design-kernel-extraction-2026-08-29.md` (kernel authority map), travel-app `docs/component-registry.json` (seven Life primitives registered 2026-08-30, provisional)

Every load-bearing decision below was ruled by the founder across 2026-08-29/30.
Where a rejected alternative shaped the ruling, the losing board is cited — the
"do not resurrect" list is as binding as the wins.

---

## 1. What Life is

Life is the governed record of lived experience — the fourth co-equal root
(Home · Chat · Places · Life). It is an **archive with intelligence in its
lower half**, not a feed:

- **Home** owns what is live and what rotates. Life never performs novelty.
- The loop, correctly phrased (brief §3.4): **Life holds governed
  evidence, lineage, and durable handles. Vesper recompiles them against
  the present. Home and Places deliver timely or spatial consequence;
  Chat, Plan, and Occasion help it work. Life preserves the resulting
  receipt.** Life is not an engine and does not "generate" openings.
- **Places** owns the world's objects. Life owns *your history with* them.
- Life's page may change **only when time, the record, or authority
  changes — never for engagement's sake** (founder ruling, "fixed
  windows"; amended 2026-08-30: "the record changes" explicitly includes
  revocation, blocking, grant narrowing, depicted-person removal, and
  suppression — these are authority mutations and must invalidate
  windows, reflections, cached reads, and counts exactly as record
  mutations do).

## 2. The four modes (lenses)

One corpus, four spines — never copies: **Time · Places · Threads · People**
(names founder-ruled). Each mode is a full page wearing the same anatomy (§3)
and the same speaking header (§4). People is first-class and equal; it is also
the one mode where a subject can object — see §8.

## 3. Page anatomy (founder-ruled, identical across modes)

```
1. Speaking header        (eyebrow LIFE · facet instrument · action capsule ·
                           generated read · mode sub-line)
2. DIGEST                 4–5 blocks, deterministic picks; the page is the
                           FRONT PAGE of the mode, never the archive
3. SCROLL DOOR            exactly one — into the mode's full history scroll,
                           with an honest right-hand count (`2019 — NOW`,
                           `14 PLACES`, `9 THREADS`, `31 PEOPLE`)
3b. RETURNS (0–3, EARNED) — ownership law (§18.4): Life delivers
                           RECORD-NATIVE understanding, reconstruction, and
                           re-entry; present-tense possibilities belong to
                           Home/Places (Life may hold a bounded door to what
                           the record enables, never the delivery itself).
                           Reasons render as the MATERIAL FACT ("Thursday's
                           forecast reached 34°C this morning"), category
                           in metadata. A receipt's result stays UNWRITTEN
                           until the experience is actually lived. A return
                           composed from another person's contribution
                           names them, is scoped by their full grant
                           (Use/Retention/Inference/Audience/Action), and
                           every dependent projection recompiles or falls
                           silent if the grant is withdrawn. The bounded return region (Option B):
                           each row = derived gold rule + serif title +
                           substance line (complete value BEFORE the tap) +
                           inline material reason + ≤1 door; suppressible as
                           a layer; absent when nothing qualifies; composed
                           only from Return-Anatomy-Lab-passed material
                           (boards 13/13A–13E, C1)
4. REFLECTIONS (0–2)      keepsake + specimen only (§6) — both conditional
5. WINDOWS (0–2, FIXED)   selected peeks into OTHER modes (§7); a window
                           into a mode that holds nothing does not render
6. Utilities              Everything kept (contextual maps live inside a
                           journey/place object when spatial structure helps)
7. Tab bar
```

`ACROSS TIME` and `RETURNS` (early Time-page sections) are retired **into**
slots 4–5; do not rebuild them as ad-hoc sections.

### Digest pick rules (deterministic, per mode)

- **Time**: current period expanded + most recent hosted + nearest upcoming +
  one more by weight; earlier periods compress to one dim summary row each.
- **Places**: strongest cluster expanded + its siblings collapsed, grouped
  under region bars (`BROOKLYN`, `ITALY`, `ELSEWHERE`).
- **Threads** (CORRECTED per brief §4.3): threads are **lines of
  attention**, never projects. `OPEN / RESTING / CLOSED` is demoted as
  the dominant user-facing lifecycle; no completion language, no
  progress-to-closure copy, no "next step," and a thread owes no
  action — it may end in better seeing, an explanation, or silence. A
  thread must pass the seven entrance gates and the evidence threshold
  (a single-context observation stays NESTED in its episode — the pasta
  fixture is `admitted_nested_not_thread` until a second supported
  cluster or authored attempt exists). Digest = qualifying lines
  (strongest expanded), with settled lines celebrated, not buried.
- **People** (CORRECTED per brief §4.4): organized around
  **viewer-relative shared records** — `Shared with Maya`, never a
  dossier *about* Maya. No inferred closeness ranking (`CLOSE/FURTHER`
  removed unless user-authored), no night/message counts as crowns,
  no implication that co-presence created friendship or contact
  permission. Conversations appear only when explicitly retained or
  linked. Groups (a hosted table) remain first-class entries; distant
  ties sit under a factual bar (`MET ALONG THE WAY`).

## 4. The speaking header

- Eyebrow `LIFE` (monoStampStrong) + **facet instrument** (four fanned panes;
  the front pane walks left→right by mode and carries the mode mark: clock /
  place / dashed thread / two heads) + `HeaderActionCapsule` (search ·
  Everything kept). Facet tap cycles modes via `organicPairMotion.halfTurn`.
- **Generated read** in the shipped `RootStandfirstVoice` register
  (serif_semibold roman 30/34, letterSpacing −0.7) obeying
  `rootMastCopy.ts` bands. Never italic. **The read is earned, not
  mandatory** (amended 2026-08-30 per constitution §2.1 and the
  artifact doctrine's silence family): when Vesper has nothing
  substantive, the mast falls back to the statline alone — silence is
  valid. The read is a **live projection, never persisted expression**
  (regeneration is therefore not an in-place rewrite of anything
  saved); it carries a whisper of source role (a long-press opens
  "Why this?" with its grounding); reads over *inferred* structure stay
  descriptive — no emotional or identity naming of episodes Vesper
  inferred; and no synthetic first-person speech ever renders for a
  deceased person. Examples (fixtures):
  Time "Seven years — this summer still settling." · Places "Mostly New
  York — lately, the coast." · Threads "Three pursuits open — one is
  tonight." · People "Mostly the two of you — nine, once."
- **Lens discoverability + mode switching (RULED 2026-08-31)**: the
  labeled choices (`TIME · PLACES · THREADS · PEOPLE`) are the switcher
  **at rest** (top of page, always); the facet is the switcher in the
  **condensed/scrolled header**. Rest-vs-condensed replaces any
  novice-vs-learned state machine — nothing is tracked, one labeled
  path is always visible from the top of any page, and accessibility
  never depends on the facet. Four companion rulings: (1) the landing
  lens is **last-used, persisted** — the user's own orientation,
  changed only by their hand; (2) the selector and facet are the ONLY
  two ways the lens ever changes — a window tap is **navigation to the
  item's dossier**, never a lens switch; (3) **no horizontal page-swipe
  between lenses** — it collides with the row-swipe grammar, and swipe
  adds verbs, never navigation; (4) facet motion (halfTurn 760ms)
  stays parked for build.
- **Read register** (brief §9.3): reads are grounded, descriptive
  orientation — never inner-state, intimacy, or identity implication
  ("still settling," "mostly the two of you" are out unless authored).
  Corrected fixtures: Time "Seven years, held — summer just added." ·
  People "Four shared records — one grows tonight."
- **Sub-line**: Time gets the years band — the ONLY instrument ("only time IS
  a line"); every other mode gets a mono stat line (`4 PLACES HELD · 2
  SHORES`, `3 OPEN · 2 RESTING`, `4 HELD CLOSE · 12 SHARED NIGHTS`).
- Combined/Mine/Together toggle: **removed** from chrome (governance lives in
  Together episodes + search filters).

## 5. The entry grammar (digest blocks)

Register ladder: read 30 → section bar mono 10 → object name serif semibold
(≈20 expanded / 16 row) → sans sub 12 → mono meta 10. All object names serif.

- **Section bar** (`LifeSectionBar`): the metronome. Regular hairline + mono
  kicker + optional right mono range/count. The page must scan by bars alone.
- **Expanded = `LifeEpisodeGroup`** — an uncarded paper group: serif head +
  children + at most one `Door`, closed by a hairThin rule. **No cards on
  Life pages** (founder-ruled; 03E4 all four alternative hierarchy paradigms
  also rejected — margin-rank, apparatus, object-rank, ink-rank).
- **Children = `LifeAnchorRow`** — serif body lines led by the anchor's
  **L5 kind mark** (`AnchorKindMark`: plane, wave, arch, plate, fork, book,
  pan, glass, table…). Never abstract dots/bullets/status LEDs — the dotted
  spine (v5), better-dot family (03E6), and list-alternative paradigms (03E5,
  03E7 prose/leaders/tally/marginalia) were ALL rejected. The one open item
  in a group is the only colored mark (goldDeep, full opacity) with a
  planning-ink stamp; held items are ink at 62%.
- **Collapsed = `LifeEpisodeRow`** — serif name + sans sub + hairThin bottom
  rule + canonical disclosure chevron. No leading marks. Adornments limited
  to a goldDeep caps stamp (`YOU HOSTED`, `HELD IN COMMON`) and, on window
  rows, a mono mode stamp.
- **The chip — the one miniature** (01A6 v3, founder-ruled after two
  rejected tile generations): below the pass, a kept object renders as ONE
  LINE — its L5 kind mark + its identity (mono route, or the serif name when
  the identity is a name) + **at most one state dot** — a 26pt pill, like a
  luggage tag. Variants: the **dark chip** (wristbands — the chip is a band
  segment, notches included) and the **thumb chip** (photos lead with a
  small riso thumb). Pass anatomy — perforations, wave tears, corner cuts,
  interior zones — NEVER shrinks below L2; it belongs to the object, not
  the shorthand. Tiles and plates are retired; the ladder below the pass is
  **CHIP → MARK**. An expanded journey's shelf and a cluster's wristband
  stack are both simply rows of chips (Bushwick's "twice at the same door"
  is two identical chips, visibly).
- **Identity follows what mattered** (founder-ruled 2026-08-30): a
  wristband's identity is the ACT — who you went to see (`FOUR TET`,
  `CARIBOU`) — the venue is containment, carried by the chain. Flights
  identify by route, dining by the name, admissions by the institution.
  The identity slot answers the question the person would actually ask
  of that artifact. (Bonus: two different acts at the same door makes
  "the record notices" an insight instead of a duplicate.)
- **State grammar of miniatures**: on Life everything shown is by
  definition held, so **held says nothing** — FLOWN/SAILED/RIDDEN are
  retired words. Dots mark only exceptions: upcoming = planning-ink ring,
  live = green, unused/lapsed = grey. Chip-interior lettering is object
  print (exempt from the UI mono floor).
- **The truth ladder survives the collapse** (amended 2026-08-30, per
  constitution §6.1 and C&C §5): "held" describes custody, never
  occurrence. Plan-only material renders quieter with a `PLANNED` stamp
  and never merges into occurred truth; `UNRESOLVED` and `DISPUTED` are
  renderable mono stamps wherever they apply; a source proves only what
  it proves (a menu is not a visit; a ticket proves purchase, not
  boarding). Dossiers owe a compact plan-vs-occurrence block whenever
  the two diverge (original plan, revision + author, miss/cancellation,
  final authoritative state).
- **Time-footprint law**: a footprint strip (span of day-dots / scatter /
  chain) is a *summary of the unseen* — it may appear only on **collapsed**
  renderings; an expanded entry never shows one (its rows are the footprint).
- **Voice lines**: EB Garamond italic ≥17px, at most one per group, always
  inside the group it comments on (e.g. Bushwick's "Twice at the same door…",
  People's governance whisper). Italic is voice-only, page-wide.
- **Doors**: `Door` primitive, gold text + the one arrow; group doors are
  group-final; section doors close sections; never mid-content.
- **The swipe grammar** (board 12): rows swipe everywhere in Life; bars,
  doors, and chips never do. Swipe LEFT = the stewardship tray, at most
  two paper verbs by surface (lens/dossier rows: SHARE · CORRECT; Vault
  rows: RELEASE · DELETE-oxblood; reflections/windows: SHARE · QUIET =
  suppress-this-item). Swipe RIGHT = one gold verb, ASK — the row's
  object to Chat inside its projection envelope. Trays are paper cells
  with hairlines, never colored slabs. A full swipe never commits a
  destructive verb (delete always taps + confirms in-flow); long-swipe
  may commit only a reversible lead verb. Swipe adds verbs, never
  navigation; every swipe verb also exists somewhere visible — the
  gesture is a shortcut, never the only path. No chore verbs exist.
  **Amendments (2026-08-30, per C&C §3.8 / constitution §5.4):**
  CORRECT opens the **stewardship sheet** — the full in-context repair
  set the contract requires (correct what happened · detach from
  episode · exclude from resurfacing · release an interpretation ·
  change audience or precision · delete via the owner) — so repair
  lives inside episodes, not exiled to the Vault. SHARE always opens a
  **destination + audience preview** (Send / Address / Share /
  Contribute-to-Occasion / Publish remain distinct commands there) and
  is never committed by long-swipe — audience change is a material
  boundary, not a reversible flick. Every stewardship action leaves a
  compact receipt (scope · owner · reason · undo).
- **Two child-row treatments, deliberately**: children *inside an expanded
  group* are airy (no separators — the group's structure holds them);
  page-level record rows (dossiers, digests) carry hairThin bottom rules.

## 5b. The dossier — held-thing pages (board 06 family)

Every click on a held thing (journey, chapter, cluster, thread, person,
hosted night) lands on ONE page grammar — the **dossier**: everything the
record holds about the thing. Self-similar law: **every organ shows a
taste, an honest count, and a door to all of it** (the root's digest
philosophy applied fractally).

Organs, ALL conditional (absence is air) — and the visible ORDER is
job-specific per object (C2): journey leads with what happened → what
Vesper reconstructed → WHAT THIS OPENS → record; place leads with held
episodes → distinction → Places handoff; thread with evidence → new
connection → optional return; shared-with with episodes → attributed
contributions → governance. `WHAT THIS OPENS` is the optional
near-the-top return organ (earned, complete-on-view, one continuation,
absent not empty). The organ set: masthead (back +
capsule + kind kicker + serif name 26 + a cached read at 19, grey — the
subordinate read register) · THE RECORD · THE DRAWER (all chips) · THE
CONTACT SHEET (all photos as uniform 62pt raw thumbs + an overflow count
tile) · THE CONVERSATIONS (the chat threads that made or carried it —
rows open them in Chat) · THE PEOPLE · THE PLACES (these two replace the
root's windows on dossiers — they ARE the doors out) · WHAT IT LEFT
(derived, gold-ruled — Returns lives here, not on the root) · THE LEDGER
(what it cost, from the expense system) · KEPT (keepsake) · THE SOURCES
(provenance, counted: `12 EMAILS · 3 BOOKINGS · 47 PHOTOS`) · Map/Share.
Person dossiers add HELD IN COMMON (governance) and their contact sheet
shows your camera + granted photos only. **Person-page guardrail**
(C&C §9 forbids the personality dossier): the person read and statline
must be source-bound counts and descriptive fact — never inferred
characterization — and every derived line on a person page carries the
"Why this?" grounding path. THE CONVERSATIONS organ admits only threads
whose retention/linkage was invoked or authored — chat content is not
durable evidence by default (graph-legibility keep-silent list).

**The taps (seven, total, everywhere in Life)**: serif row + chevron →
the held-thing page at that grain (fractal; a chapter opens this same
grammar at day grain; depth ends at objects; conversation rows → Chat) ·
chip → the object page (the pass at L1 with workflows — the one exit
from this grammar) · thumb → the photo full-screen as a single object
(there is no gallery mode) · gold door → where it names · caret → grows
in place, never navigates · keepsake → its moment · specimen → its page.

**NO HERO (founder-ruled)**: Life is a raw collection of artifacts, not
a polished Instagram account. No immersive/hero photography anywhere in
Life — imagery enters only as specimens (thumbs), one riso keepsake per
page, or a tapped photo as an object. Every page speaks once — a cached
statement-band read regenerated only when the record changes.

## 5c. The thin record — Life's degradation ladder (board 07 family)

Thin is a state of the SAME grammar, not a separate design — the organ
conditionality above IS the cold-start design. The ladder gates
**instruments, never content**, and is never announced: day 1 = one
dossier exists and Life opens on it; week 2 = lenses live, mast sub-line
is a statline (the years band must EARN its line — it appears only past
one year), 0–1 windows; season 1 = footprints and specimens become
possible; year 1 = years band, A YEAR AGO TODAY, keepsakes.

Laws: **the floor** = masthead + record + sources (everything held can
say where it came from) · **absence is never an ask** — no illustrated
placeholder for an empty lens or conditional organ, no add-prompt,
progress meter, or completeness score; the thin page is short, not
needy · **zero-record threshold, narrowly** — only when the entire
governed corpus is empty, the ordinary masthead and four lenses may be
followed by one frameless decorative illustration and one indicative
reassurance sentence; no CTA or example gallery appears, and the whole
treatment yields to the first real governed object · **one reassurance
at most** — where reflections would sit, the thin root may speak a
single voice line ("the record grows as you live it, not as you feed
it"), which disappears the day a real reflection exists · reads scale
down honestly (compact band).

## 5d. The full scroll (board 08 family)

Behind every scroll door: the complete corpus of that mode — collapsed,
dense, honest. **The root speaks and reflects; the scroll only keeps.**

- **Two-level metronome**: the scroll's one new mark is the **epoch rule**
  (a 1.5px ink rule carrying a serif marker — years on Time, regions on
  Places, `HELD / SETTLED` on Threads, `SHARED RECORDS /
  MET ALONG THE WAY` on People (post-correction vocabularies)) with standard mono section bars beneath. Two levels,
  never three.
- **Rows at scroll density** (52pt): collapsed episode rows with kind
  stamps (`JOURNEY`, `YOU HOSTED`, `THREAD`) where weight matters.
  Everything navigates; nothing expands in place on the scroll.
- **Pure archive**: no reflections, windows, keepsakes, or voice lines.
  The read is minimal ("Everything, newest to oldest."). The masthead
  count must reconcile with the scroll door that promised it — the count
  is a contract.
- **Closed things surface here**: settled threads, ended eras, lapsed
  places are visible on the scroll (the root shows the living record;
  the scroll shows all of it).
- The scroll ends with its own beginning: `THE RECORD BEGINS · SEP 2019`
  — the one place the archive states its age.

## 5e. The object page (board 09 family)

The chip's tap — the one exit from the dossier grammar — lands here:
**the object at L1, and almost nothing else.**

- **Pure object**: the pass renders with its complete anatomy (01A–01A4)
  — kind kicker, the route in display serif, the truths row, the
  perforation with real notches, the stub with barcode. This is the ONLY
  surface in Life where L1 appears.
- **Object print may speak — but only occurrence-supported print**
  (amended 2026-08-30): the pass says FLOWN on itself, like a used
  ticket's stamp, ONLY when an occurrence supports it (a scan, an
  arrival trace, an authored confirmation — the fixture's stamp cites
  its evidence: `FLOWN · AUG 15 · 09:41`). Without occurrence support
  the stub speaks purchase truth only (`KEPT`, `UNUSED`, `LAPSED`) —
  the canonical repair case is the ferry ticket bought but never
  sailed. The UI never repeats object print either way. **Print is
  fact-only** (brief §10.1): interpretation and voice ("the heat won,"
  "torn off at 4") belong to separately attributed notes or
  compositions, never to object print.
- **Truths are provenance-backed**: every truth traces to THE SOURCE
  (`1 EMAIL · DELTA · RECEIVED JUL 2 · PARSED, KEPT VERBATIM`) with a
  door to the original. The object page is where the record proves it
  invented nothing.
- **WHERE IT LIVES**: the containment chain upward (chapter → journey →
  lens) — the two-axes doctrine (identity vs containment) at object
  scale.
- **Workflows, minimal**: always `Share the pass` and `Correct a detail`
  (corrections are part of provenance). Live workflows (leave-by, gate,
  directions) appear here only while the object is live; otherwise they
  are Home's, not the archive's.

## 5f. The Vault — the custody surface (board 10 family)

The surface behind every "Everything kept" door — reached from every Life
page's capsule and utilities, **never in the facet**: the modes explore
the world; the Vault inspects the machine. A utility room, not a living
room — back-of-house register (denser rows, mono-forward labels, counts
everywhere), the same kernel worn like a storeroom ledger.

- **Everything accounted**: masthead total = total custody; kind counts
  (photographs, passes, emails, wristbands, menus, notes, saved
  compositions — marked generated) must sum to it; each opens a
  filtered list.
- **NOT YET PLACED**: loose artifacts as chips with one calm caption —
  "Vesper places these as episodes form; nothing here needs you." Loose
  is a fact, not a chore: no inbox, no badges, no counts nagging any
  other surface.
- **ARRIVALS**: recent ingestion as receipts — `SOURCE → WHAT IT BECAME`
  ("Delta email → the pass, parsed, kept verbatim") — the global twin of
  every dossier's SOURCES organ.
- **THE GRANTS LEDGER** (the destination of "Manage what's shared"):
  who holds what in common, on which of the five contract axes —
  **Use / Retention / Inference / Audience / Action** — with each
  grant's purpose, basis, and expiry visible (a grant never implies
  every purpose). Scope note: the Vault is *contextual custody
  inspection*; connectors, mandates, retention policy, and the full
  Source control plane remain Global settings' (C&C §3.8). **WITHDRAWN**:
  what left, by whom, and how many projections it revised — propagation
  visible, not asserted.
- **Custody verbs**: Export everything · Release a source · Delete —
  destructive verbs render in plain ink (RATIFIED 2026-08-31 in the
  design-kernel doc: oxblood = live-threshold register only, final). **Deletion speaks honestly** (brief §10.2): the confirmation
  states what leaves product read paths immediately, what expires
  within 24h (indexes, derivatives) and 30 days (backups), which
  managed exports recompile or close, and what cannot be remotely
  revoked (static downloads, screenshots).
- The Vault never recommends, resurfaces, or speaks editorially; its
  one read is an accounting ("Everything held, accounted for.").
- **User language, RULED 2026-08-31**: the surface is **"Everything
  kept"** in every user-facing label, title, and door; "The Vault" is
  retired to internal/board shorthand; "sources" survives only inside
  provenance strings ("parsed, kept verbatim"). A comprehension test
  may still validate; if it ever contradicts, the test wins.
- **Kind pages (10B–10D)**: one grammar, the unit changes by kind —
  photographs get the grid (uniform 65pt thumbs + overflow tile), emails
  get provenance rows (`SOURCE → WHAT IT BECAME`), passes/wristbands get
  chip rows, compositions get GENERATED-stamped rows. Vault masthead
  (kicker · name · accounting statline · SELECT), content under the
  scroll's two-level metronome, custody verbs scoped to the kind or the
  selection. Unplaced = a small planning ring on the item — a fact, never
  a badge that leaks elsewhere. Released sources stay listed honestly.
  Counts reconcile upward to the Vault's totals. A kind with sub-kinds
  earns MODE CHIPS under its masthead (passes: flights / rail / ferry /
  road / admissions) — scope filters, same pattern as search. Ticket rows are
  **L2 rows** — the ladder's row rung, used exactly here: stubbed
  mini-passes (mono ID over the containment chain, a perforated stub
  carrying date + state dot, the kind's signature varying the separator:
  dashed / wave / long-dash / corner-cut+violet; rail mirrors its stub
  left). Wristbands are full-width dark band rows, notched mid-row.
  The Vault stays a ledger — L1 never renders here; the full pass stays
  one tap away on the object page (10E/10F v2).

## 5g. Search the record (board 11 family)

Target-first retrieval over the whole corpus (11A: query "pasta"):
results grouped under the metronome with honest counts, each result a
kind-marked row whose sub-line is its **containment chain**; results are
doors, never in-place answers; the matched fragment washes gold. Scope
chips narrow by kind; search is also where Mine/Together scope filtering
lives pending the Together layer design. Per the Life continuity
decision §2: an optional `Around this` trail of **at most three**
landmarks expands only on request; raw queries and reformulations stay
session-local (≤24h encrypted recovery, never resurfacing/interest
evidence); durable state requires an explicit save, correction, or
consequential action. Search is not Chat — the page ends with the
Ask-Vesper handoff door, and zero results state the truth plus the same
door.

## 6. Reflections — "shown, never told"

Founder-ruled pairing (03E9; figures and instruments explicitly not chosen):

- **Keepsake** (`LifeKeepsake`) — a riso artifact postcard from the archive
  (photo, kept wristband, settled thread's trophy): cream mat, art in the
  riso duotone inks (teal `#4E7A6F` + coral `#C4604F` on cream), mono
  provenance stamp, riso corner mark. **Only when a real artifact exists; at
  most one per page.** No artifact → no slot → air extends (kernel
  degradation law). This is the page's only image.
- **Specimen** — a plain `LifeEpisodeRow` under the standardized bar
  **`FROM THE FULL RECORD`**, and it may only surface something that lives
  behind the scroll door and appears **nowhere else on the page**. It is the
  page's standing proof the archive is deeper than the digest.
- Prose reflections (gold-rule derived blurbs) are retired from these slots.

## 7. Windows — fixed, never rotating

Two rows peeking into two *other* modes, each carrying its mode stamp, under
a bar reading `WINDOWS · FIXED · <MODE> / <MODE>`. **A window changes only
when the underlying record changes** — opening the page twice in a day shows
the same page twice. Rotation is Home's job. Windows are also The Loop's
structural seats (Life → Places/Home openings live here, not in ad-hoc
sections). Suggested fixed pairs (fixtures): Time→(Places, Threads),
Places→(Time, People), Threads→(Places, People), People→(Places, Time).

## 8. People mode — governance contract

- The lens pivots **your record only**: your account of shared time. The
  Maya-group voice line is the doctrine: *"Your account of the time shared —
  hers stays hers."*
- Naming/reach defaults follow the contribution & consequence contract's
  five axes — **Use / Retention / Inference / Audience / Action**
  (CORRECTED 2026-08-30: an earlier draft used the four-root doc's
  informal may-use/name/contact/retain/show vocabulary; the adopted
  contract's axes govern). Default = names-without-reach; revocation
  must propagate across the whole lens; note that Life must also give
  the **Inference** axis a control surface (what may be learned from a
  contribution), not just Use/Audience.
- Jointly held episodes surface with the `HELD IN COMMON` stamp; each side
  keeps its own copy; either side can withdraw theirs.
- ⚠️ **Data gap**: no person or group entity exists in the backend today
  (north-star audit). This spec is the argument for building one; People
  ships last of the four lenses.

## 9. Registered components (travel-app, provisional, 2026-08-30)

| Component | Role |
| --- | --- |
| `LifeSectionBar` | Section metronome: mono kicker over hairline, optional right count |
| `LifeEpisodeGroup` | Expanded entry: uncarded paper group + closer rule |
| `LifeEpisodeRow` | Collapsed entry / specimen / fixed-window row |
| `LifeAnchorRow` | Serif child line led by its kind mark |
| `AnchorKindMark` | L5 ladder rung: 15pt ink kind glyph, gold when open |
| `LifeScrollDoor` | The one double-ruled archive entry with honest count |
| `LifeKeepsake` | Riso artifact postcard for the reflection slot |

Existing primitives composed, not duplicated: `Door`, `Tap`, `VText`,
`RowAccessory`, `RootStandfirstVoice` + `rootMastCopy` bands,
`HeaderActionCapsule`/`headerChrome`, `AuthoredVoiceTypeout`.

Still to build (not yet registered): `LifeChip` (the one-line miniature —
kind mark + identity + at most one exception dot; `dark` and `thumb`
variants; replaces the previously planned tile/plate primitives),
`LifeMasthead` (glue: eyebrow + facet + capsule + read + sub-line),
the dossier surface + organs (06), the thin ladder's instrument gates (07),
the full-scroll surfaces (08), the object page incl. the L1 pass
component (09), and the Vault custody surface (10) — designed, unbuilt,
`LensFacet` (the four-pane instrument), the years-band instrument,
footprint strip/mark (collapsed-only), and the
fractal episode page (one component every grain; a chapter is a
projection, not a new object).

### Mockup → token normalizations (deliberate)

- Mockup mono meta at 8.5/9px normalizes to `monoStamp` (10px) — the raised
  mono floor is canon; the mockups undershot it.
- Group title 21px normalizes to `serifTitleLg` (20); row title 16.5 →
  `serifTitle` (16); child 15.5 → `serifBody` (15, at the serif floor).
- Colors map 1:1 to `colors.surface.*` (paper/card/ink/mute/muteSoft/
  goldDeep/hairline/hairThin/planningInkDeep/confirmGreen/oxblood).

## 10. Data contracts the build owes

1. **Digest pickers** per mode (§3) — pure functions over the
   **viewer-authorized corpus** (inputs: viewer, epoch, grants,
   suppression state); no randomness, no recency-decay theater.
   Projection is viewer-relative by contract (C&C §5) — no picker may
   be viewer-independent.
2. **Keepsake availability** — an artifact index (photos, passes, wristbands,
   closed-thread trophies) with per-mode eligibility; empty ⇒ slot absent.
3. **Specimen picker** — from the full scroll minus everything already on the
   page; stable between record changes.
4. **Window selections** — persisted picks + an invalidation rule tied to
   record AND authority mutations (revocation, blocking, grant changes,
   suppression).
5. **Truthful counts** — every bar/door count (`3 THREADS`, `31 PEOPLE`)
   computed from the **viewer-authorized corpus** (tombstoned, deleted,
   blocked-dependency, and suppressed material excluded — the count
   reconciles to what THIS viewer's door can actually open);
   speakable-counts law: never say a number the scroll cannot
   substantiate.
6. **Person/group entity** (§8) — prerequisite for People.
7. **Chat-thread ↔ episode linkage** — THE CONVERSATIONS organ needs
   threads attributable to episodes/threads/people; does not exist yet.
8. **One counting service** — honest counts now appear on root bars,
   scroll doors, and every dossier organ; one shared implementation.

## 11. Do not resurrect (ruled out, with evidence boards)

- Cards as expansion surfaces (v2 → founder "no cards"); In Motion on Life
  (belongs to Home/Places); dots-on-spine timelines (v5); abstract dot
  families (03E6); list-alternative child paradigms — outline indents, dot
  leaders, tally ticks, marginalia, prose-composed children (03E5/03E7);
  figure & instrument reflection forms (03E9, not chosen); rotating windows;
  the standalone floating serif year; italic section labels; sans children
  inside groups; footprint strips on expanded entries; Combined/Mine/Together
  header toggle.
- **Miniature-scale pass anatomy** (01A6 v1–v2 — "dollhouse furniture"):
  uniform artifact tiles, plates, per-surface tile scales, interior
  zones/signature lines below L2, and miniature status words
  (FLOWN/SAILED/RIDDEN). The miniature is one line — the chip.
- **Staged, decorative, or generated-as-lived imagery anywhere in
  Life** (NARROWED AGAIN 2026-08-31 per §18.7, board 14): **a photograph may
  lead wherever it is the strongest evidence for the composition's
  job** — real, attributed, permission-safe, occurrence-grounded,
  visibly distinct from generated imagery. Typographic roots and
  mastheads remain the DEFAULT, not a prohibition; gallery modes,
  empty-state prompts, progress meters, and completeness scores remain
  banned; generated or decorative imagery never impersonates lived
  evidence.
- **Thread completion pressure** — closure language, next-step framing,
  progress-to-done copy, actions that exist merely to close a thread.
- **Intimacy ranking** — CLOSE/FURTHER groupings, night/message counts
  as crowns, inferred relationship characterization, person-dossiers
  about a person rather than shared-with records.
- **Editorial object print** — interpretation baked into an artifact's
  own stamp.
