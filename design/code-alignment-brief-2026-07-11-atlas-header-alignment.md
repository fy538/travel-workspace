# Code Alignment — Atlas / Trip-Settings Header Geometry (2026-07-11)

**Status:** ready to execute · **Created:** 2026-07-11 · **Scope:** `travel-app` frontend only (+ one `design/surface-manifest.yaml` bookkeeping edit)
**Repo:** `~/travel-workspace/travel-app` · **Canon mirror:** `~/travel-workspace/design/vesper-canon-anchor/project/`

> **Read the whole "Orientation" section before touching code.** You (a fresh agent) have none of the audit that produced this brief. Everything you need is here or cited to a file you can open. Do not re-run the audit; do trust the file:line citations but re-open each file before editing since code keeps moving under concurrent sessions.

---

## TL;DR — what you're doing

A page-header shape used across **26 Atlas + Trip-Settings screens** places a large serif page title cramped directly under a floating back button, mis-indented relative to that button. This is a real geometry bug with **zero basis in canon** (canon's header board literally says *"Don't left-align the title — it's always centered, back and action both minWidth 52"* — see citation below). The fix is **narrow and mechanical**: two spacing constants + consolidating a duplicated title block onto an existing shared component. You are **not** redesigning anything and **not** ripping out the scroll-collapse animation (it's correct and canon-sanctioned).

Three edits + a manifest note:
1. **One line** in `components/ui/CollapsingHeader.tsx` — fixes the cramped vertical gap on all 26 screens at once.
2. **`components/atlas/AtlasNativeScaffold.tsx`** (18 screens) — fix a 4px horizontal mis-indent + swap its hand-rolled title block onto the shared `AtlasScreenHeader`.
3. **7 `AtlasCompactHeader` consumer screens** — swap each screen's hand-rolled title block onto `AtlasScreenHeader`; fix 3 of them that also have the 4px mis-indent.
4. **`design/surface-manifest.yaml`** — record the fix + correct one false-positive from the earlier audit.

---

## Orientation

### What prompted this
A user looked at the "Memory receipt" and "Elif" (profile) Atlas screens and said the page title, left-aligned just below the back button, "looks strange." Investigation confirmed the cramped/awkward look is a genuine geometry defect, not a taste disagreement.

### The two header primitives in play
This app has two independent page-header systems:
- **`ProductiveHeader.tsx`** (`components/ui/ProductiveHeader.tsx`) — the canonical "Family A" primitive. Back button + kicker + title are **siblings in one flex row**. Everything that delegates to it (`ScreenHeader`, `CostsTopBar`, `EditorialMasthead` in `inlineTitle` mode, etc.) is canon-correct. **You are not touching any of these.**
- **`CollapsingHeader.tsx`'s `CompactHeaderBar`** (`components/ui/CollapsingHeader.tsx`) — an iOS-style scroll-collapsing bar: a `position:'absolute'` overlay holding just the back button (+ optional right action), where the large page title lives separately down in the scroll body and a compact centered title fades into the bar on scroll. **This is the one you're fixing.** It is consumed by exactly two wrapper components:
  - **`AtlasNativeScaffold.tsx`** — 18 screens (list below)
  - **`AtlasCompactHeader.tsx`** — 8 screens (list below)

### Is the scroll-collapse pattern itself illegal? No — keep it.
Canon **does** sanction a "title fades in only on scroll" register. `header-audit-app.jsx` line ~298 calls it *"the reader variant of Family A"* (register A3). The one place canon actually builds a **large body title under such a fade-bar** is `vesper-discover-detail-app.jsx`'s `ReaderChrome` (which wraps `ProductiveHeader` with `fadeTitle`), used by the Dossier and Angle reader screens. So the *mechanism* is fine. Only the *geometry constants* are wrong. **Do not migrate these 26 screens onto `ProductiveHeader`** — that would mean rebuilding smooth animated interpolation for no benefit and a larger blast radius. Fix the constants in place.

### What canon actually specifies (the numbers you're matching)
From `vesper-discover-detail-app.jsx`, `ScreenAngle` (the clean no-hero reader case, ~lines 357–366) and `ScreenDossier` (~lines 325–334), plus `header-audit-app.jsx` rules block (~lines 500–523):

- **Vertical rhythm (Angle Detail):** bar bottom → **16px** padding → kicker label → **6px** gap → serif title.
- **Alignment:** canon's body title is **left-aligned** in both Dossier and Angle (no `textAlign` set). So a left-aligned large Atlas title is **not itself wrong** — canon's own precedent does the same. **Do not change alignment.**
- **Horizontal inset:** canon's mandated header rule is **16px** (`productive-header.jsx`: `padding: '8px 16px 10px'`, back/action `minWidth 52`; rule text: *"Don't left-align the title — it's always centered, back and action both minWidth 52."*). Canon's *own* Dossier/Angle body title uses 20px (`padding:'0 20px'`) — a 4px inconsistency canon never reconciles. **We normalize to 16px everywhere**, matching the one inset rule canon states explicitly, rather than copying its unremarked blind spot.

### Root cause, precisely
`CollapsingHeader.tsx`'s body-content offset helper adds only **6px** (`spacing.sm`) between the bar and the title where canon uses 16px — that's the "crammed right under the button" look, and it hits **all 26 screens** because both wrappers call the same helper. Separately, `AtlasNativeScaffold` (and 3 of the `AtlasCompactHeader` detail screens) indent the body **20px** (`spacing.xxl`) while their bar sits at **16px** (`pageChrome.sideInset`) — the 4px mis-indent. And the eyebrow+title+meta block is hand-rolled ~8 separate times when a correct shared version (`AtlasScreenHeader`) already exists and is used by one screen (`search.tsx`).

---

## The edits

> **Spacing scale** (`constants/layout.ts`): `spacing.sm = 6`, `spacing.xl = 16`, `spacing.xxl = 20`. `pageChrome.sideInset = spacing.xl = 16`. `COMPACT_BAR_H = 48` (exported from `CollapsingHeader.tsx`).

### Edit 1 — `components/ui/CollapsingHeader.tsx` (fixes vertical gap on all 26 screens)

`useHeaderContentTop()` (currently lines 62–65):

```ts
export function useHeaderContentTop(): number {
  const insets = useSafeAreaInsets();
  return insets.top + COMPACT_BAR_H + spacing.sm;   // ← change spacing.sm to spacing.xl
}
```

Change `spacing.sm` → `spacing.xl`. That is the only change in this file. Leave the absolute bar, the Reanimated fade/translate, the centered compact title, and everything else exactly as-is.

### Edit 2 — `components/atlas/AtlasScreenChrome.tsx` (add a `dark` prop to the shared component)

`AtlasScreenHeader` currently hardcodes light colors. One `AtlasNativeScaffold` screen (`app/atlas/compose.tsx`) renders `variant="dark"`, so before you can route all 18 screens through `AtlasScreenHeader` you must let it render dark. Add an optional `dark?: boolean` prop mirroring `AtlasNativeScaffold`'s existing `titleDark` / `metaDark` styles:

- Current dark values in `AtlasNativeScaffold.tsx` to mirror: title → `colors.atlas.paper`; meta → `'rgba(239,234,224,0.70)'`.
- In `AtlasScreenChrome.tsx`, add `dark?: boolean` to `AtlasScreenHeaderProps`, thread it into the title and meta `<Text>` color (e.g. `[styles.title, dark && styles.titleDark]`, `[styles.meta, dark && styles.metaDark]`), and add the two `titleDark` / `metaDark` style entries.

### Edit 3 — `components/atlas/AtlasNativeScaffold.tsx` (18 screens)

Two changes:

**(a) Fix the 4px horizontal mis-indent.** In its `styles`, `content.paddingHorizontal` (currently line ~167) is `spacing.xxl` (20px). Change to `pageChrome.sideInset` (16px) so the body lines up with the bar. (`pageChrome` is already imported from `../../constants/layout`.)

**(b) Replace the hand-rolled title block with `AtlasScreenHeader`.** The current inline block (lines ~68–77):

```tsx
{showIntro ? (
  <View style={styles.header}>
    <AtlasEyebrow tone="gold">{eyebrow}</AtlasEyebrow>
    <Text style={[styles.title, dark && styles.titleDark]}>
      {title}
      {italicTitle ? <Text style={styles.italic}>{'\n'}{italicTitle}</Text> : null}
    </Text>
    {meta ? <Text style={[styles.meta, dark && styles.metaDark]}>{meta}</Text> : null}
  </View>
) : null}
```

Replace with a call to `AtlasScreenHeader` (import from `./AtlasScreenChrome`), passing `eyebrow`, `title`, `titleItalic={italicTitle}`, `meta`, and `dark`. Prop parity is direct: `AtlasScreenHeader`'s `titleItalic` renders exactly the "second line in italic" shape that `italicTitle` produces here. After the swap, `AtlasEyebrow`, `styles.header`, `styles.title`, `styles.titleDark`, `styles.italic`, `styles.meta`, `styles.metaDark` in this file become unused — delete the now-dead styles/imports (let `tsc`/lint guide you).

**⚠️ Two cosmetic deltas to eyeball in visual QA** (both make the 18 screens match `search.tsx`, which already ships `AtlasScreenHeader`):
- **Meta line:** `AtlasNativeScaffold` styled meta as `typography.readingItalicMd` with `maxWidth: 336`; `AtlasScreenHeader` styles meta as `typography.readingItalicXs` with no max-width. So the concept/meta line becomes slightly smaller and full-width. Acceptable (more consistent app-wide), but confirm it reads well on a screen that has a `meta` (e.g. `receipt.tsx`).
- **Italic second line:** `AtlasNativeScaffold` used `typography.articleBodyItalic.fontFamily`; `AtlasScreenHeader` uses `fontFamily.serif_bold_italic`. Confirm the italic second line on `receipt.tsx` ("receipt.") still looks right. If the bolder italic is a visible regression, prefer changing `AtlasScreenHeader`'s `italic` style to `articleBodyItalic.fontFamily` (it has only 2 consumers total after this pass, so it's a safe shared change) rather than special-casing.

### Edit 4 — the 8 `AtlasCompactHeader` consumer screens

These each hand-roll their own `<AtlasEyebrow …/> + <Text style={styles.title}>…` block (title styled `typography.displayHero`). Route them all through `AtlasScreenHeader` and fix inset stragglers.

| Screen | Title-block lines (approx) | Horizontal inset now | Action |
|---|---|---|---|
| `app/atlas/search.tsx` | already uses `AtlasScreenHeader` | `spacing.xl` (16) ✓ | **no change** |
| `app/atlas/inbox.tsx` | ~174–175, styles ~400 | `spacing.xl` (16) ✓ | swap block → `AtlasScreenHeader` |
| `app/atlas/postcards.tsx` | ~96–97, styles ~327 | `spacing.xl` (16) ✓ | swap block → `AtlasScreenHeader` |
| `app/atlas/removed.tsx` | ~127–128 | `spacing.xl` (16) ✓ | swap block → `AtlasScreenHeader` |
| `app/atlas/long-view.tsx` | header block in sub-components | `spacing.xl` (16, line ~528) ✓ | swap block → `AtlasScreenHeader` |
| `app/atlas/candidate/[id].tsx` | ~160–161 | **`spacing.xxl` (20, line ~414)** ✗ | swap block **+ inset → `spacing.xl`** |
| `app/atlas/artifact/[id].tsx` | ~218–219 | **`spacing.xxl` (20, line ~587)** ✗ | swap block **+ inset → `spacing.xl`** |
| `app/atlas/learned/[id].tsx` | ~83–84 | **`spacing.xxl` (20, lines ~237/240)** ✗ | swap block **+ inset → `spacing.xl`** |

For each swap: replace the inline `AtlasEyebrow` + `Text` title (+ meta, where present) with an `AtlasScreenHeader` call (`eyebrow` / `title` / `titleItalic` / `meta` as the screen currently supplies them — some use `titleLead`+`titleInlineItalic` inline-italic form; `AtlasScreenHeader` already supports those exact props, so map 1:1). Watch for screens that render their eyebrow/title as **two separate sibling blocks** vs. one — preserve whatever content they show, just move it into the shared component. Remove now-dead `styles.title` etc. as `tsc`/lint flags them.

> Note: several of these screens reference `contentTop` (from `useHeaderContentTop()`) in multiple render branches (loading / error / empty / list). Edit 1 fixes the gap for all of those branches automatically — you don't need to touch them.

### Edit 5 — `design/surface-manifest.yaml` bookkeeping

Find the **"Header system"** row (`grep -n "Header system" design/surface-manifest.yaml`). In its `notes:`:
- Record this fix (Atlas/Trip-Settings collapsing-header geometry aligned to canon's reader precedent: bar→title gap 6→16px, body inset normalized to 16px, title block consolidated onto `AtlasScreenHeader`).
- **Correct one false positive:** an earlier code-side audit flagged `TripFolioFloatingChrome` in `app/(tabs)/trips/[tripId]/index.tsx` (Trip Home) as the same violation. It is **not** — it legitimately floats over a real full-bleed cover hero (`components/trip/TripFolioHome.tsx:360`, `testID="trip-home-image-hero"`) with a bottom identity block (pill · title · travelers, ~line 379). That's canon's **Family B (HeroChrome)** pattern, explicitly scoped to full-bleed hero/media surfaces. No fix needed there.
- Bump `code_verified_at` for the row to the current `travel-app` HEAD short-sha after you commit.

---

## Explicitly OUT of scope (do not touch)

- **Trip Home** (`app/(tabs)/trips/[tripId]/index.tsx`, `TripFolioFloatingChrome`) — legitimate Family B hero chrome, see Edit 5. Not a bug.
- **`app/atlas/scan.tsx`** — a multi-step wizard where each step owns its own title (same shape as `onboarding.tsx`). Not the "disconnected title halves" bug.
- **Family reassignment for `trip-settings/*`** — canon has *no* board for Atlas at all (an "Atlas Home.html" canon file was explicitly deleted as "unrelated product"), and Trip Settings' own canon (`vesper-trip-settings-app.jsx`) uses a *different, simpler* static centered-title `NavBar` with no scroll-collapse and no large body title. Under a strict reading, the 4 `trip-settings/*` screens currently on `AtlasNativeScaffold` might belong on a plain `ProductiveHeader`/`ScreenHeader` instead. **That is a design decision, not part of this pass** — this brief only fixes the geometry of the pattern they're on today. Flag it to the user separately if you want; don't resolve it silently here.

### The 18 `AtlasNativeScaffold` screens (for reference)
`app/atlas/`: `account.tsx`, `data-receipt.tsx`, `compose.tsx` (dark), `receipt.tsx`, `phone.tsx`, `notifications.tsx`, `profile.tsx`, `saved-places.tsx`, `constraints.tsx`, `privacy.tsx`, `board.tsx`, `companions.tsx`, `feedback.tsx`, `delegation.tsx` + `app/trip-settings/`: `notifications.tsx`, `index.tsx`, `permissions.tsx`, `privacy.tsx`. (You don't edit these individually — they all inherit Edits 1 & 3 through the shared components.)

---

## Verification

1. **Typecheck:** `cd ~/travel-workspace/travel-app && npx tsc --noEmit -p .` — clean, after the `AtlasScreenHeader` prop addition and every swap. Run it incrementally; dead-style/import removal will surface here.
2. **Visual (Browser preview tool, not manual):** check one screen per wrapper and per variant —
   - `app/atlas/receipt.tsx` (AtlasNativeScaffold, light, has `meta` + italic second line)
   - `app/atlas/compose.tsx` (AtlasNativeScaffold, **dark** — confirms the new `dark` prop)
   - `app/atlas/profile.tsx` (AtlasNativeScaffold, the "Elif" screen the user flagged)
   - `app/atlas/inbox.tsx` (AtlasCompactHeader)
   
   Confirm on each: title now has clear breathing room under the back button (not crammed), its left edge aligns with the back button's inset (no 4px step), and — **critically** — on scroll the compact centered title still fades into the bar correctly (you didn't break the animation). Screenshot `profile.tsx` before/after for the user.
3. **Grep guard:** after the pass, confirm no `AtlasCompactHeader` consumer still hand-rolls the block — e.g. `grep -rn "styles.title" app/atlas/*.tsx app/atlas/**/*.tsx` should show only styles that aren't the page-title `displayHero` block, and every eyebrow+title now flows through `AtlasScreenHeader`.

## Commit discipline (important — concurrent sessions)

Another session commits unrelated work in this repo continuously, with files often left staged. **Always commit with an explicit pathspec** — `git commit -m "…" -- <exact paths>` — never a bare `git add -A && git commit`, which would sweep their staged changes under your message. Group logically: the shared-component edits (`CollapsingHeader.tsx`, `AtlasScreenChrome.tsx`, `AtlasNativeScaffold.tsx`) and the 7 screen swaps can be one commit in `travel-app`; the manifest note is a separate commit in `~/travel-workspace`. Run `git status` before each commit to see exactly what you're including. Only commit/push when the user asks; if you're on `main`, branch first.
