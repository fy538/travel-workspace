# Code Alignment Brief — Motion + State + Notifications (2026-07-12)

**Status:** merged (travel-app #76–#79) · **Lane:** Motion / State System / Notifications  
**Repo:** `travel-app` from `origin/main` (`5fae4455`+) · isolated worktrees · pathspec commits  
**Prior:** Family polish closed (headers, buttons, sheets, StatusPill, muteSoft). This wave shifts to a11y motion, dual hard-failure kit, and Notifications wiring.

---

## TL;DR

Run four parallel PRs:

| PR | Focus | Target |
|---|---|---|
| **M1** | Reduce-motion gaps | Shared gate; migrate Animated/Reanimated loops that ignore reduced motion |
| **M2** | Press contract | Snap `pressScale` 0.97→0.98; press feedback timing (not spring) per canon |
| **S1** | Hard-failure kit | One blessed full-page failure (`ErrorState` vs `StateScreen tone=failure`); migrate + ratchet |
| **N1** | Notifications | Wire TODAY/YESTERDAY/EARLIER sectioning to all modes; kill NeedsEye bordered card regression |

---

## Explicit OUT of scope

- Atlas / Discover redesign (deferred).
- Deck content/substrate (separate fullstack plan).
- muteSoft UNCLEAR / sage / fsStamp.
- Backend Universal Search Actions route.
- Device dogfood of prior gap-close (separate).

---

## PR-M1 — Reduce motion

**Canon:** disables all nonessential animation app-wide when reduce-motion is on.  
**Existing:** `hooks/useMotionPreference.ts`, `utils/motion.ts` (`_reduceMotion`), `useAnimatedLoop`, Reanimated `useReducedMotion` in several cards.

**Audit list from open findings (re-verify — some may already gate):**  
`VoiceOrb`, `CardStates`, `CardLive`, `CardLift`, `Deck.tsx`, `OrganizerInviteNudge`, `ErrorBanner`, `AtlasMemoryReel`, `NavChromeContext`.

**Do:**
1. Inventory each: does it already call `useReducedMotion` / `useMotionPreference` / skip loops?
2. Migrate remaining: freeze loops at rest opacity/scale; skip `withRepeat` / `Animated.loop`.
3. Prefer existing helpers over new ones; extend `useAnimatedLoop` or `utils/motion.ts` if needed.
4. Optional: thin CI grep/ratchet for `Animated.loop` without a reduce-motion neighbor (keep simple).

**Branch:** `polish/m1-reduce-motion`

---

## PR-M2 — Press scale + timing

**Findings:** press-scale drifted 0.98 → 0.97; press uses spring where canon wants fixed-duration timing collapse.

**Do:**
1. Confirm canon value in motion docs / vesper tokens (expect **0.98**).
2. Change `constants/motion.ts` `pressScale` 0.97 → 0.98.
3. In `components/ui/Tap.tsx` (and any direct press springs): prefer `withTiming` + house easing over `withSpring(spring.press)` for the press-in/out collapse, matching canon.
4. Grep for hardcoded `0.97` / local press springs; align or leave documented exceptions.
5. Run `npm run motion-governance` if present.

**Branch:** `polish/m2-press-contract`  
**Conflict note:** may touch `constants/motion.ts` + `Tap.tsx` — coordinate with M1 if both edit motion utils; prefer M2 owns press tokens, M1 owns loop gating.

---

## PR-S1 — One hard-failure kit

**Problem:** `components/ui/state/ErrorState.tsx` and `StateScreen.tsx(tone='failure')` are two visually different full-page hard-failure UIs (oxblood badge pill CTA vs bare icon).

**Do:**
1. Read both + call-site counts; pick **one** as canonical (prefer the one closer to state-system canon / more call sites if canon unclear — document choice in PR).
2. Make the other a thin wrapper **or** migrate call sites and delete/deprecate the loser.
3. Add adoption ratchet (pattern like local-button budget): fail if new direct imports of the deprecated primitive appear (or if both remain without wrapper).
4. Do not redesign cold-start Discover chip-picker or InlineAbsence in this PR.

**Branch:** `polish/s1-hard-failure-kit`

---

## PR-N1 — Notifications sectioning + priority strip

**Findings:**
- `notificationSectionLabel()` (or equivalent) exists but only Trip-Updates mode sections rows; Global / Trip-Scoped / Personal stay flat.
- Priority/time-sensitive strip reverted to bordered tinted “NeedsEye card” — canon killed that pattern.

**Do:**
1. Find section helper + screen modes in `app/notifications` / `components/notifications*`.
2. Wire section headers for all four modes that canon sections.
3. Restyle priority strip: no card background / border wash — match notifications canon (hairline or bare row treatment).
4. Opportunistic small copy fixes only if trivial (push-denied CTA, etc.) — else leave listed.

**Branch:** `polish/n1-notifications-sections`

---

## Execution log (2026-07-12)

| PR | travel-app | Result |
|---|---|---|
| M2 | #76 `ba799d6f` | pressScale 0.98 + Tap timing |
| N1 | #77 `65847b3d` | time sections + bare priority strip |
| S1 | #78 `093107e3` | ErrorState→StateScreen wrapper + ratchet |
| M1 | #79 `71548c77` | SpotTake usePulse + motion-governance (rebased onto S1 CI) |

---

## Verification (every PR)

```bash
cd travel-app
npx tsc --noEmit -p .
npm run motion-governance   # M1/M2
# relevant Jest if touching notifications/state
```

---

## Success metric

| Metric | Before | After |
|---|---|---|
| Listed motion offenders without reduce-motion | several | 0 (or documented exception in motion-exceptions.md) |
| pressScale | 0.97 | 0.98 + timing press |
| Dual hard-failure kits | 2 live | 1 (+ wrapper or ratchet) |
| Notification modes with TODAY/YESTERDAY/EARLIER | 1/4 | 4/4 (or all modes that have dated rows) |
| NeedsEye bordered priority card | present | gone |

Campaign closes when all four PRs merge — not when every Notifications P2 nit is done.
