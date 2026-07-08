# Code Alignment — Batch J1: Header System (2026-07-06)

Canon: `Vesper Header Audit.html` + `header-audit-app.jsx` + `productive-header.jsx` (handoff 119). Repo: `~/travel-workspace/travel-app`.

## Read this first — the audit's premise doesn't match the code

The Header Audit's framing is *"4 surfaces each hand-roll the same productive-header shape → converge them into one shared `ProductiveHeader`."* **A source pass of the RN app shows that consolidation has already largely happened in code — under different names.** The app is in better shape than the audit assumed. Concretely:

| Surface | Canon says | Code reality | Verdict |
|---|---|---|---|
| Notifications | forked header → merge | already uses shared `EditorialMasthead` (`app/notifications/index.tsx:343`) | ✅ already shared |
| People & Collaboration | forked header → merge | already uses shared `CompactHeaderBar` via `AtlasNativeScaffold` (`app/atlas/companions.tsx:83`) | ✅ already shared |
| Chat | keep as-is (Family C) | already uses shared `FloatingChatHeader` (`chat.tsx:478`) | ✅ correct, leave alone |
| Places | "slim reader chrome" → merge | **no top bar at all** — hero-first with `FloatingGlassIconButton` glass overlays (`app/place/[placeSlug].tsx`) | ⚠️ design/code disagree — adjudicate |
| Itinerary | "most capable productive header" | `PlanSituationHeader` (`plan.tsx:1184`) — phase-adaptive, not a back/title/action row by design | ✅ deliberate specialist, not a target |
| **Trip Story** | forked header → merge | **hand-rolled `MemoryStoryHeader`** (`story.tsx:45-88`) | ❌ the ONE genuine fork |

So the design audit's own correction (it walked "8+ copies" down to 4 after spot-checking) needs to go one step further: **in code the true raw-fork count is 1 — Trip Story.** Everything else is already on a shared primitive, just decomposed by surface-lineage (`ScreenHeader` / `EditorialMasthead` / `CompactHeaderBar` / `FloatingChatHeader` / `PlanSituationHeader`) rather than by the canon's 4-family names.

## What this batch actually is

Given the above, J1 is small and mostly reconciliation, not migration. The one real fork lives inside a surface (Trip Story) that is getting a major rework in the same handoff (`trip-story-app-a/b/c`, ~1,180 lines — deferred to Batch J2). So:

### Task J1-1 — Taxonomy reconciliation (doc, do now)
The code decomposes headers differently from canon's 4 families. Record the mapping so the next header picks an existing primitive instead of adding a 6th — this is the actual anti-fork guard, and it's cheap.
- Add a short header-taxonomy note (in `components/ui/` alongside the primitives, or the app's design-system doc) mapping: **Family A Productive → `ScreenHeader`** (the plain back/title/action row) · **Family A "editorial" register → `EditorialMasthead`** (parchment/serif, archive & notifications) · **Family A "collapsing" register → `CompactHeaderBar`** (scroll-condensing, Atlas scaffold) · **Family B HeroChrome → `FloatingGlassIconButton` overlays** (Places/Trip-Doc cover — not yet extracted as a named component) · **Family C Chat → `FloatingChatHeader`** · **Family D TabRoot → the Trips-Home top bar / `EditorialMasthead` largeTitle**.
- State the standing rule (canon's own): a pushed screen with back + one task uses an existing shared header; **do not hand-roll a new one.** Trip Story is the cautionary example.
- Do NOT force-merge `ScreenHeader`/`EditorialMasthead`/`CompactHeaderBar` into one component — they encode real register differences (plain vs parchment-serif vs scroll-collapsing). Canon's "Family A" is one *shape*; the code's three are one shape in three *registers*, which is legitimate. Merging them would be churn that fights shipped, working code.

### Task J1-2 — Trip Story header: fold into J2, don't do standalone
`MemoryStoryHeader` (`story.tsx:45-88`) is the single genuine fork and the honest migration target — but Trip Story is being substantially redesigned in handoff 119 (Batch J2, currently deferred to the post-dogfood social-loop initiative). Migrating the header now risks throwing away work the rework replaces. **Recommendation: bundle the `MemoryStoryHeader` → `ScreenHeader` migration into Batch J2 when Trip Story is rebuilt for real.** If J2 slips indefinitely and the fork bothers you sooner, it's a standalone ~S task: verify `ScreenHeader` covers back+label + the "○ READY FOR ATLAS" status line + N icon actions (the recon says back+title+actions are supported; the status-line element may need a small `ScreenHeader` prop extension — verify before committing).

## Two adjudications to flag (design's call, not the implementer's)
1. **Places header divergence.** Canon draws Places with a slim productive reader-chrome header; code ships Places hero-first with glass-overlay chrome and no top bar — the recon reports this as deliberate (consistent with the Discover Detail lineage where Experience Detail is full-screen/hero-first). Someone should decide which is canon. **Recommend: code is right, the Places header mock is the stale side — but record it as a canon amendment rather than "fixing" code to match a mock the product already moved past.**
2. **The 3-way Family-A split.** Is canon OK with `ScreenHeader`/`EditorialMasthead`/`CompactHeaderBar` as three registers of one family, or does it want a single merged `ProductiveHeader`? **Recommend: accept the split, document it (J1-1), don't merge.**

## Done
Taxonomy note written + anti-fork rule recorded (J1-1) · Trip Story header migration explicitly parked on J2 with rationale · the two adjudications surfaced to the design owner · no header primitives merged or rebuilt (the code's decomposition is sound). Net: J1 is a paperwork/guard batch — the real header consolidation already exists in code; this stops it from re-fragmenting and hands two disagreements back to design.
