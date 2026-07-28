---
doc_type: working
status: active
owner: frontend
created: 2026-07-28
expires: 2026-08-27
why_new: Durable device evidence for Home Surfaces program step 3.
promotes_to: nothing
supersedes: []
source_of_truth_for: [home-surfaces-step3-device-evidence]
---

# Home Surfaces step 3 — device evidence

Captured 2026-07-28 on iPhone 16 Pro, iOS 18.2
(`AF31B886-E837-4962-834A-5CBAD5C306DB`), app
`com.fyan.vesper`.

## Evidence

- `vesper-home.png` — normal Dynamic Type. The Home composer has a real
  leading `+`, a readable 17px placeholder, and no decorative sparkle.
- `vesper-history.png` — normal Dynamic Type. Shows the state-first
  sections, unread treatment, three-line rows, hairlines, group mark,
  and fixed new-conversation action.
- `vesper-history-axxxl.png` — iOS
  `accessibility-extra-extra-extra-large`. The row grows, the title
  remains clamped to two lines, and the page header and fixed action
  remain usable.

## Automated device checks

The focused normal-size History flow passed:

- conversation list visible
- `Still open`, `Earlier this week`, and `July 2026` visible
- unread dot visible

The focused maximum-Dynamic-Type flow passed:

- conversation list and `Still open` visible
- unread dot visible
- fixed `Start a new conversation` action visible

The Home flow reached the screen, composer, and attachment assertions.
Its only selector failure was the dissolve test id: the dissolve is
deliberately hidden from accessibility and pointer-transparent, so
Maestro cannot select it. Component coverage asserts its 64px geometry
and `pointerEvents="none"`; the Home capture supplies the visual check.

## Code checks

- TypeScript typecheck passed.
- Focused History, sectioning, Composer, pending-turn, stream-isolation,
  and Vesper Home suites passed.
- Targeted ESLint completed with no errors.
- The full Jest run retains two pre-existing unrelated failures:
  `plan.smoke.test.tsx` cannot find `plan-move-mode`, and
  `trip-settings.group-agency.test.tsx` finds multiple `Where to?`
  labels. Both reproduce independently of step 3.
