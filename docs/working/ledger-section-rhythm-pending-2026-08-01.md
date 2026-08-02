# Pending: ledger section rhythm — re-apply after the SectionHeader migration

**Status:** written, verified by reading, then **reverted unapplied** on
2026-08-01 because a concurrent session was mid-refactor in the same two files.
Re-apply once that work lands and `tsc` is green.

## The finding

`docs/design-system/Row System.md` geometry lock:

> Section rhythm (ledger screens) — First section `marginTop: 0`; between
> sections **24**

Audited against the three Ledger-register archive screens. Each gets one half
of the rule right, and they are **opposite halves**:

| Screen | First section | Between sections |
|---|---|---|
| Conversations (`app/(tabs)/concierge/history.tsx`) | `spacing.none` = 0 ✓ | `spacing.lg` = **12** ✗ |
| Notifications (`app/notifications/index.tsx`) | `spacing.lg` = **12** ✗ | `spacing.xxxl` = 24 ✓ |
| Trip history (`app/(tabs)/trips/[tripId]/changes.tsx`) | — | `sectionRhythms.standard` = 24 ✓ |

Only Trip history — the one screen using the *named* recipe rather than raw
spacing tokens — is fully compliant. That is the argument for the fix below:
point the other two at the same named recipe rather than at literals.

## The change (2 files, 5 lines)

**`app/notifications/index.tsx`**

```diff
-import { spacing, layout } from '../../constants/layout';
+import { spacing, layout, sectionRhythms } from '../../constants/layout';

   sectionHeaderFirst: {
-    marginTop: spacing.lg,
+    marginTop: spacing.none,
   },
   sectionHeader: {
-    marginTop: spacing.xxxl,
+    marginTop: sectionRhythms.standard.betweenSections,
   },
```

**`app/(tabs)/concierge/history.tsx`**

```diff
-import { pageLayouts, spacing, radius } from '../../../constants/layout';
+import { pageLayouts, spacing, radius, sectionRhythms } from '../../../constants/layout';

   sectionHeader: {
-    marginTop: spacing.lg,
+    marginTop: sectionRhythms.standard.betweenSections,
     paddingHorizontal: spacing.xl,
   },
```

`sectionRhythms.standard.betweenSections` resolves to `layout.sectionGap` →
`spacing.xxxl` → **24**, so Notifications' value is unchanged in pixels; the
edit only moves it onto the named recipe. Conversations' 12 → 24 is the one
real visual change, plus Notifications' first header 12 → 0.

## Why the layer is right

Checked before reverting: `components/ui/SectionHeader.tsx` sets only
`marginBottom: spacing.md` (heading-to-content) and deliberately does **not**
own `marginTop`. So between-section spacing correctly belongs to the screen,
and this fix does not collide with the in-flight migration onto that component.

## Why it was reverted

The concurrent session had ~60 uncommitted files including both target screens,
`SectionHeader.tsx`, and `EditorialSectionHeader.tsx`. The tree was red with 6
`tsc` errors, none of them from this change — 5 were
`UniversalSearchOverlay.tsx` using `SectionHeader` without importing it, a
half-written edit. No clean verification signal was available, and committing
would have swept up their unfinished work.

## Open question to settle when re-applying

`sectionRhythms.editorial` is docstringed *"Ledger/archive sections with more
expressive typography"* but sets `betweenSections: spacing.xl` = **16**, which
contradicts Row System.md's 24 for ledger screens. `standard` (24) was chosen
here because it matches both the spec and the one already-compliant screen —
but the naming is genuinely misleading and someone should either rename
`editorial` or correct the doc.

## Also unresolved (separate, older)

Two `LedgerRow.test.tsx` failures predating all of this: `resolveSupport()`
disagrees with its tests about whether subtitle or destination wins the single
support line. Tests expect destination; the code prefers subtitle and
suppresses destination on tappable rows (`suppressDestination: Boolean(onPress)`)
with a reasoned comment. One side is stale; nobody has decided which.
