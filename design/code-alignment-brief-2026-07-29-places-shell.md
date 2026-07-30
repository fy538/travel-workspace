# Code Alignment Brief — Places Shell (2026-07-29)

**Status:** not started
**Scope:** `travel-app` — the Places tab's chrome. The surface below it is already aligned.
**Canon:** `PLACES - CORE.html` (Claude Design → Vesper, `project_id 551f400f-3da1-42ab-be7f-35f2d28e7c75`), §2 screens + the Pass 4 shell kit `places-foundation-kit.jsx`
**Plan:** `docs/working/places-build-plan-2026-07-28.md`
**Repo state:** work from `origin/main`; pathspec commits only (local trees carry concurrent WIP)

---

## Why this brief exists

Twelve `feat(places)` commits landed 07-28 → 07-29 and built the surface
**faithfully**: `components/places/core/` contains `PlaceRow`, `MapSummary`,
`RelationshipMarker`, `StatusText`, `AreaCard`, `SearchEscape`, `QueryRow`,
`RowSkeleton`, `GuidePreview`, `ExperienceRow`, `ReadingDoor`, `SaveControl`,
`PhotoThumb` and `VKicker` — every one a real counterpart to a canon component,
several of them ahead of the canvas.

The **shell** did not follow. `PlacesWorkspace` hand-rolled its own header
instead of porting the Pass 4 kit, and the result reads as a different product
at the top of the page:

| Canon (§2, measured on the artboard) | Shipped |
|---|---|
| Scope **is** the page title — 22px EB Garamond, inline ⇄, no wordmark | Centred `Places` wordmark + scope demoted to a card |
| — | `PLACES IN` caps eyebrow above the scope |
| Support line under the title (`Carroll Gardens`) | absent |
| Search field, always present; disabled state keeps the field | Field replaced by *"Search isn't available for this scope yet."* |
| `Search everywhere →` at y=165 on every scoped screen | absent everywhere |
| Saved = header bookmark + section action | third entry point as a `Saved` pill |
| First section names the place (`Near you`) | `PLACES FOR THIS SCOPE` generic fallback |

Canon reaches its first content row at y=403 having shown scope, search, escape
and a map. The shipped chrome reaches its first row around y=270 having shown a
wordmark, a card, an apology and a pill.

### The actual root cause — worth fixing, not just the symptom

**Every component that consumed a shared implementation stayed aligned. Every
component that was hand-rolled drifted.**

The header cluster is the proof in the other direction: `PlacesRootHeaderActions`
uses the shared `HeaderActionCapsule`, and it is **exactly right** — so right
that the canvas was the stale one and was updated to match it on 2026-07-29.

The shell drifted because the canon shell components had **no named code
counterpart**. Nobody was choosing to diverge; there was simply nothing to adopt,
and no check that would notice. PR-P4 fixes that; the rest is porting.

---

## Explicit OUT of scope

- **Track C projection work** — `GET /api/places` exists and is wired. Missing
  map/highlight/experiences/areas on the mock persona are *thin data*, not
  missing code, and are the plan's B1–B4 / C1–C6.
- **Been** — cut entirely (plan A4). Do not restore it here.
- **Highlight variants beyond `GuidePreview`** — v1 ruling stands.
- **The scope picker** — already faithful, including the ownership line
  *"This changes what Places reads. It never changes your active trip."*
- **`components/places/core/`** — aligned. Do not refactor it in this brief.

---

## PR-P1 — Canvas first (design-only, no code)

Ship this **before** any code lands, because "match the design" is currently
ambiguous in one place.

- Apply **D6** to CORE: `SectionHeading` → the mono eyebrow via `VKicker`. The
  canvas still renders 17px sans headings; the code already ships the eyebrow.
  The ruling was recorded in the plan and never applied to the canvas, so today
  the code is right and the canon is stale.
- Fold in the 2026-07-29 header-capsule update (already done) so §2's screens
  and the kit agree.

**Exit:** no rule in CORE that the code correctly implements is still drawn the
old way. A coder reading CORE and a coder reading `core/PlacesCore.tsx` reach the
same answer.

---

## PR-P2 — Port the shell

Three components, all mapped 1:1 onto canon. Prefer *adopting* the existing
shared primitives over new local ones wherever one exists.

| New / changed | Canon source | Notes |
|---|---|---|
| `components/places/core/PlacesScopeControl.tsx` | `ScopeControl` | 22px serif scope name as `<h1>`, inline change glyph, sans support line, `Suggested` badge, `unavailable` state. `compact` variant at 17.5px for the collapsed shell. Picker rows stay **sans** — they are radio options, not the page's identity. |
| `components/places/core/PlacesShell.tsx` | `ExpandedShell` + `CompactShell` | Expanded = scope row (with the capsule right-aligned) then search. 126px. Compact = one row at 54px. |
| search | `PFSearch` | Scope-aware placeholder map (`trip` / `around` / `home` / `anywhere`). **Keep the field in a disabled state** rather than replacing it with a sentence — canon's own offline copy is *"Search needs a connection."* |

**Deletions** — all in `PlacesWorkspace.tsx`:
- the centred `Places` nav title (the tab bar marks the destination)
- the `PLACES IN` scope card (lines ~404–422)
- the `Saved` pill
- the *"Search isn't available for this scope yet."* branch

**Keep unchanged:** `PlacesRootHeaderActions` — already canonical.

**Most visible consequence:** the app loses its "Places" nav title. That is the
canon rule, stated in `ScopeControl`'s own docstring: *"There is no separate
wordmark: the bottom nav already marks the destination, so the largest thing on
screen is the context the surface is computed in."*

---

## PR-P3 — Render `SearchEscape`

It is already built in `core/PlacesCore.tsx` and rendered nowhere on the root.
Canon puts it directly under the field on every scoped screen — it is the only
affordance that lets a traveler leave a scope. Absent when the scope is already
`anywhere` (nothing to escape from), matching the cold-root specimen.

Also: section titles should name the place. `Near you` / `Places in Lisbon` /
`Around Alfama`, with `Places for this scope` as a genuine last resort rather
than the common case.

---

## PR-P4 — Correspondence + the guard that stops this recurring

The mechanism, not another list.

1. **A correspondence table** — `components/places/core/CORRESPONDENCE.md`: one
   row per canon component → its code counterpart → the canon file it comes
   from. Every entry in `PLACES - COMPONENT MAP.html`'s 49 gets a row or an
   explicit "not ported, because —".
2. **A conventions test** — `__tests__/conventions/placesShellContract.test.ts`,
   in the ratchet style already used by `serifFloorContract.test.ts`:
   - `PlacesWorkspace` renders `PlacesShell`; it declares no local header
     `<View>` with a title
   - the string `PLACES IN` appears nowhere
   - no centred `Places` title is passed to `ScreenScaffold`
   - every name in `CORRESPONDENCE.md` resolves to a real export

The test is what makes the next session's hand-rolled header fail CI instead of
shipping.

---

## PR-P5 — Bookkeeping

- `design/surface-manifest.yaml` → **Places Tab (root browse surface)**: stamp
  `code_verified_at` with the squash SHA, move `status: gap` → `partial`, and
  rewrite `notes` (the current text describes the pre-build state and is now
  wrong on almost every point).
- Update `docs/working/places-build-plan-2026-07-28.md` §1 — its audit describes
  07-28 and is stale as of 07-29.

---

## Suggested sequencing

```
P1 (canvas)  →  P2 (shell)  →  P3 (escape + titles)  →  P4 (guard)  →  P5 (books)
                      └── P4's correspondence table can be drafted in parallel
```

P1 first and alone. P2 and P3 could merge, but keeping them apart makes the
escape's absence reviewable on its own — it is a behaviour gap, not a restyle.

---

## Verification (every PR)

```bash
cd ~/travel-workspace/travel-app
npx tsc --noEmit
npx jest __tests__/conventions __tests__/components/places
npx jest __tests__/hooks/useConciergeHomeState.test.ts
```

Device pass, using flows that already exist:

```
.maestro/polish/places-workspace-default.yaml
.maestro/polish/places-workspace-cold.yaml
.maestro/polish/places-projection-root.yaml
.maestro/polish/places-destinations.yaml
```

Those runs currently capture **zero** screenshots. Fix the capture step as part
of P2 — a visual brief with no visual evidence is how this drift survived a week.

---

## Success metric

Screenshot the running Home scope beside CORE §2 artboard `s4` at 1:1. The scope
name is the largest thing on both, at the same place, in the same face; the
search field is present in both; `Search everywhere →` is present in both. No
wordmark in either.
