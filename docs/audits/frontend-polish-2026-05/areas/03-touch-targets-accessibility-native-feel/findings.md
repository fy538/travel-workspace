# Touch Targets, Accessibility, Native Feel

## Summary

Vesper's interaction doctrine is clear: `minTouchTarget 44pt` is "Non-negotiable" in `Travel App/docs/Design Language.md`, and `Tap` is documented as the app-wide replacement for raw `Pressable`. The implementation is directionally good, but too much of the standard is still left to individual call sites. The highest-leverage polish fix is to make touch target size, icon-button semantics, disabled/selected state, and press feedback mechanical.

Severity is mostly P2: these are not dogfood blockers, but they are exactly the kinds of small misses that make a premium native app feel slightly uncertain in week-one use.

External baseline:

- [Apple HIG, Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility): iOS/iPadOS controls should provide comfortable, reliably tappable targets; Vesper's own doctrine codifies this as 44x44 pt.
- [WCAG 2.2 Target Size Minimum](https://www.w3.org/TR/WCAG22/#target-size-minimum): 24x24 CSS px is the lower accessibility floor, not the native/premium target.
- [Material Design accessibility](https://m2.material.io/design/usability/accessibility.html): touch targets should generally be at least 48x48 dp, reinforcing that 44pt should be treated as Vesper's minimum, not an aspiration.
- [React Native accessibility props](https://reactnative.dev/docs/accessibility): roles and state should be exposed explicitly for controls such as buttons, switches, tabs, and radio-like choices.

## Findings

### P1 - `Tap` and `Button` do not enforce the 44pt standard mechanically

`Tap` wraps `Pressable` and adds opacity/haptics, but it passes caller styles through without any minimum target, default `hitSlop`, required label, or disabled/selected state policy (`Travel App/components/ui/Tap.tsx:55`-`Travel App/components/ui/Tap.tsx:64`). `Button` composes `Tap`, but neither `sm` nor `md` sets `minHeight`; `sm` is only text plus `spacing.md` vertical padding, and `md` is text plus `spacing.lg` vertical padding (`Travel App/components/ui/Button.tsx:113`-`Travel App/components/ui/Button.tsx:135`).

This means the canonical primitives can still produce targets below Vesper's own 44pt floor. It also explains why many screens locally add partial `hitSlop` or padding with inconsistent results.

### P2 - Trip workspace icon controls are likely below 44pt

`TripHeader` has icon-only back and settings controls rendered through `Tap`, but `styles.backBtn` only adds `marginRight` and no width, height, padding, or `hitSlop` (`Travel App/components/trip/TripHeader.tsx:100`-`Travel App/components/trip/TripHeader.tsx:107`, `Travel App/components/trip/TripHeader.tsx:125`-`Travel App/components/trip/TripHeader.tsx:132`, `Travel App/components/trip/TripHeader.tsx:163`-`Travel App/components/trip/TripHeader.tsx:165`). Their effective visual targets are roughly the 20-22pt icons.

The trip title switcher also toggles an expandable panel but exposes only `accessibilityRole="button"` and no expanded state (`Travel App/components/trip/TripHeader.tsx:109`-`Travel App/components/trip/TripHeader.tsx:121`). This is high-frequency chrome in the primary trip workspace, so small targets and incomplete state make the app feel less native.

### P2 - Segmented controls and pill filters often sit below native target height

`NavPills` uses correct tab roles and selected state, but the default pill style is 13pt text with `spacing.md` vertical padding, likely below 44pt (`Travel App/components/ui/NavPills.tsx:37`-`Travel App/components/ui/NavPills.tsx:45`, `Travel App/components/ui/NavPills.tsx:158`-`Travel App/components/ui/NavPills.tsx:164`). The trip segmented variant explicitly sets `minHeight: 36`, below Vesper's 44pt floor (`Travel App/components/ui/NavPills.tsx:91`-`Travel App/components/ui/NavPills.tsx:111`, `Travel App/components/ui/NavPills.tsx:202`-`Travel App/components/ui/NavPills.tsx:209`).

The Discover view toggle repeats the same pattern with button-like segmented choices, no selected state, and small vertical padding (`Travel App/app/(tabs)/discover/index.tsx:897`-`Travel App/app/(tabs)/discover/index.tsx:918`, `Travel App/app/(tabs)/discover/index.tsx:1714`-`Travel App/app/(tabs)/discover/index.tsx:1728`). These controls are scannable visually, but not consistently native-feeling or stateful to assistive tech.

### P2 - Close/remove controls for personal data and attachments are undersized

Several destructive or corrective icon-only controls are intentionally tiny and then patched with insufficient `hitSlop`:

- Composer image removal is 24x24 with 6pt hit slop, documented as a 36pt effective target (`Travel App/components/chat/ComposerBar.tsx:307`-`Travel App/components/chat/ComposerBar.tsx:315`, `Travel App/components/chat/ComposerBar.tsx:546`-`Travel App/components/chat/ComposerBar.tsx:558`).
- "What I know about you" dispute/remove buttons are 20-22pt controls with 6-8pt hit slop, topping out around 32-38pt (`Travel App/app/(tabs)/me/what-vesper-knows.tsx:182`-`Travel App/app/(tabs)/me/what-vesper-knows.tsx:190`, `Travel App/app/(tabs)/me/what-vesper-knows.tsx:205`-`Travel App/app/(tabs)/me/what-vesper-knows.tsx:213`, `Travel App/app/(tabs)/me/what-vesper-knows.tsx:260`-`Travel App/app/(tabs)/me/what-vesper-knows.tsx:270`, `Travel App/app/(tabs)/me/what-vesper-knows.tsx:394`-`Travel App/app/(tabs)/me/what-vesper-knows.tsx:433`).
- Constraints removal uses icon-only `Tap` controls with `hitSlop={8}` but no 44pt container, and the language add chip is fixed at 32x32 (`Travel App/app/(tabs)/me/constraints.tsx:190`-`Travel App/app/(tabs)/me/constraints.tsx:217`, `Travel App/app/(tabs)/me/constraints.tsx:235`-`Travel App/app/(tabs)/me/constraints.tsx:247`, `Travel App/app/(tabs)/me/constraints.tsx:381`-`Travel App/app/(tabs)/me/constraints.tsx:385`).

Because these actions edit allergies, accessibility needs, languages, learned facts, and photo attachments, missed taps or accidental taps feel trust-eroding rather than merely annoying.

### P2 - Accessibility state is missing or inconsistent on toggles, disabled buttons, and radio-like choices

`ComposerBar` disables camera/send affordances visually and functionally, but the `Tap` instances do not expose `accessibilityState={{ disabled: ... }}` (`Travel App/components/chat/ComposerBar.tsx:333`-`Travel App/components/chat/ComposerBar.tsx:349`, `Travel App/components/chat/ComposerBar.tsx:382`-`Travel App/components/chat/ComposerBar.tsx:409`). In contrast, `Button` does expose disabled state (`Travel App/components/ui/Button.tsx:75`-`Travel App/components/ui/Button.tsx:82`), so behavior is inconsistent across canonical action surfaces.

`constraints.tsx` marks privacy controls as switches but does not expose checked state (`Travel App/app/(tabs)/me/constraints.tsx:322`-`Travel App/app/(tabs)/me/constraints.tsx:328`). Radio-like code is also inconsistent: `RadioOption` uses `accessibilityState={{ selected, disabled }}` for `accessibilityRole="radio"` (`Travel App/components/ui/RadioOption.tsx:40`-`Travel App/components/ui/RadioOption.tsx:52`), while the delegation screen uses `checked` for the same role (`Travel App/app/(tabs)/me/delegation.tsx:92`-`Travel App/app/(tabs)/me/delegation.tsx:99`). The visual UI may be clear, but VoiceOver users get a less predictable contract.

### P3 - Press feedback is inconsistent where tab screens bypass `Tap`

`Tap`'s file header says to use it instead of `Pressable` throughout the app for consistent opacity and haptic feedback (`Travel App/components/ui/Tap.tsx:1`-`Travel App/components/ui/Tap.tsx:15`). The tab screens still bypass it in places:

- Memory uses raw `Pressable` for the group-and-learn consent banner (`Travel App/app/(tabs)/trips/[tripId]/memory.tsx:143`-`Travel App/app/(tabs)/trips/[tripId]/memory.tsx:154`).
- Photos uses raw `Pressable` for photo tiles with tap and long-press actions (`Travel App/app/(tabs)/trips/[tripId]/photos.tsx:470`-`Travel App/app/(tabs)/trips/[tripId]/photos.tsx:495`).

Photo tiles may reasonably avoid haptics because they are high-frequency, but they still need consistent pressed visuals. Today the user can tap important album/memory surfaces with less confirmation than nearby `Tap` controls.

## Evidence

Likely below-44pt icon-only or compact controls:

- `TripHeader` back/settings icons: `Travel App/components/trip/TripHeader.tsx:100`-`Travel App/components/trip/TripHeader.tsx:132`
- `NavPills` trip cells: `Travel App/components/ui/NavPills.tsx:202`-`Travel App/components/ui/NavPills.tsx:209`
- `ComposerBar` image remove: `Travel App/components/chat/ComposerBar.tsx:546`-`Travel App/components/chat/ComposerBar.tsx:558`
- `what-vesper-knows` chip closes: `Travel App/app/(tabs)/me/what-vesper-knows.tsx:394`-`Travel App/app/(tabs)/me/what-vesper-knows.tsx:433`
- `constraints` language add chip: `Travel App/app/(tabs)/me/constraints.tsx:381`-`Travel App/app/(tabs)/me/constraints.tsx:385`

Places where hit slop is missing or insufficient:

- Missing on `TripHeader` icon controls: `Travel App/components/trip/TripHeader.tsx:100`-`Travel App/components/trip/TripHeader.tsx:132`
- Insufficient on image remove: `Travel App/components/chat/ComposerBar.tsx:307`-`Travel App/components/chat/ComposerBar.tsx:315`
- Insufficient on learned-profile chip close controls: `Travel App/app/(tabs)/me/what-vesper-knows.tsx:205`-`Travel App/app/(tabs)/me/what-vesper-knows.tsx:308`
- Insufficient on constraints remove controls: `Travel App/app/(tabs)/me/constraints.tsx:190`-`Travel App/app/(tabs)/me/constraints.tsx:217`

Accessibility label/state/role gaps:

- Missing expanded state on trip switcher: `Travel App/components/trip/TripHeader.tsx:109`-`Travel App/components/trip/TripHeader.tsx:121`
- Missing disabled state on composer camera/send controls: `Travel App/components/chat/ComposerBar.tsx:333`-`Travel App/components/chat/ComposerBar.tsx:409`
- Missing checked state on privacy switches: `Travel App/app/(tabs)/me/constraints.tsx:322`-`Travel App/app/(tabs)/me/constraints.tsx:328`
- Inconsistent radio state convention: `Travel App/components/ui/RadioOption.tsx:40`-`Travel App/components/ui/RadioOption.tsx:52` vs. `Travel App/app/(tabs)/me/delegation.tsx:92`-`Travel App/app/(tabs)/me/delegation.tsx:99`
- Missing selected state on Discover view toggle: `Travel App/app/(tabs)/discover/index.tsx:897`-`Travel App/app/(tabs)/discover/index.tsx:918`

Press feedback inconsistencies:

- `Tap` sets pressed opacity and haptic globally: `Travel App/components/ui/Tap.tsx:42`-`Travel App/components/ui/Tap.tsx:64`
- Raw `Pressable` in Memory consent banner: `Travel App/app/(tabs)/trips/[tripId]/memory.tsx:143`-`Travel App/app/(tabs)/trips/[tripId]/memory.tsx:154`
- Raw `Pressable` in Photos tiles: `Travel App/app/(tabs)/trips/[tripId]/photos.tsx:470`-`Travel App/app/(tabs)/trips/[tripId]/photos.tsx:495`

## Suggested Fix Direction

1. Add mechanical target enforcement to `Tap`, probably behind props such as `minTarget="auto" | "none"` and `targetSize={44}`. For layout-sensitive cases, allow visual size to remain small while applying `hitSlop` to reach 44pt.
2. Add a canonical `IconButton` for all bare-icon controls. It should require `accessibilityLabel`, default to a 44x44 target, support `selected`, `expanded`, `disabled`, and `destructive`, and centralize haptic strength.
3. Give `Button` explicit `minHeight: layout.minTouchTarget` or equivalent for every size. If `sm` must remain visually compact, make the target area larger than the visible chrome.
4. Raise `NavPills` and segmented controls to a 44pt minimum. Keep the current visual density by using track padding and centered labels rather than shrinking the hit area.
5. Normalize accessibility states: switches should expose `checked`; disabled `Tap` controls should expose disabled state; selected filters/toggles should expose selected or use tab/radio semantics consistently.
6. Replace raw `Pressable` in tab screens with `Tap` or an explicit no-haptic variant that still provides pressed visuals.

## Verification Ideas

- Add unit tests for `Tap`, `Button`, `IconButton`, and `NavPills` asserting minimum target style or computed hit slop.
- Add an accessibility snapshot test for composer disabled send/camera states, trip switcher expanded state, privacy switch checked state, and selected segmented controls.
- Add a dev-only touch-target overlay that draws 44pt bounds around every `Tap`/`IconButton`.
- Run VoiceOver on the trip workspace, composer, Discover filters, and "What I know about you"; verify labels and states are understandable without seeing the screen.
- On a small iPhone viewport, dogfood the first-week loops: switch trip tabs, send/stop a message, remove a learned preference, add/remove a photo, and toggle a privacy control without mis-taps.
