# Visual-QA Screenshot Lane — Runbook

Resolves punch-list **P1-9** ("No visual QA gate exists"). See the area
report for the full rationale and scenario rationale:
[`areas/10-visual-qa-regression-gates/findings.md`](areas/10-visual-qa-regression-gates/findings.md).

The lane drives the **iOS simulator development build** (mock API + skip
auth) with [Maestro](https://maestro.dev) and captures PNG screenshots of
the dogfood-critical screens. "The screen is the eval": these stills are the
regression evidence for typography, spacing, touch targets, and the private/
group chat substrate.

> **Status:** the flow scaffolding (`Travel App/.maestro/`) and npm scripts
> are committed, but the flows have **not been run** in this environment (no
> simulator / Maestro CLI available here). The first human to run this lane
> should expect to tune selectors — see *Selector notes* below.

---

## Why native first (not Expo web)

The area report recommends a native Maestro lane as the first gate, with
Expo web as a *secondary* review accelerator that is **not yet wired**:
Expo web currently can't boot because `react-native-web` and
`@expo/metro-runtime` are not installed (only `react-dom` is present in
`Travel App/package.json`), and native-only modules (maps, media, secure
store, notifications, Clerk) need explicit web fallbacks first. To enable
web later: `npx expo install react-dom react-native-web @expo/metro-runtime`
then `npx expo start --web` — track that as separate work.

---

## Prerequisites

1. **Install Maestro** (a standalone CLI — *not* an npm dependency):
   ```bash
   curl -fsSL "https://get.maestro.mobile.dev" | bash
   # then add ~/.maestro/bin to PATH (the installer prints the line)
   maestro --version
   ```
2. **Xcode + an iOS Simulator** (Maestro drives the booted simulator).
3. **A mock-mode simulator build** of the app. The `development` EAS profile
   already compiles an iOS simulator app with
   `EXPO_PUBLIC_USE_MOCK_API=true` + `EXPO_PUBLIC_SKIP_AUTH=true` +
   `EXPO_PUBLIC_IS_INTERNAL_BUILD=true` (see `Travel App/eas.json`). Build and
   install it onto the booted simulator:
   ```bash
   cd "Travel App"
   eas build --profile development --platform ios   # produces a simulator .app/.tar.gz
   # download + drag onto the simulator, or:
   # xcrun simctl install booted <path-to-app>
   ```
   Mock + skip-auth boots **straight to the Trips tab** (`app/index.tsx`), so
   no sign-in step is needed in any flow.

   *Local alternative (no EAS):* run a dev client / `npx expo run:ios` with
   the same two env vars exported, then point Maestro at the running app
   (`appId: com.fyan.vesper`).

---

## How to run

```bash
cd "Travel App"

# Full screenshot lane (all flows, alphabetical / configured order):
npm run visual-qa

# Single high-impact smoke (private Vesper chat) — good for CI:
npm run visual-qa:smoke
```

Both wrap the Maestro CLI (`maestro test .maestro` / a single flow file).
The app bundle id targeted by every flow is **`com.fyan.vesper`** (iOS).

### Where screenshots land

Maestro's `takeScreenshot: <name>` writes `<name>.png`. Point the lane at a
git-ignored output dir so artifacts are never committed:

```bash
mkdir -p .maestro/screenshots
cd .maestro/screenshots && maestro test ../   # PNGs land here
```

`.maestro/screenshots/` is already in `Travel App/.gitignore`. In CI, upload
that directory as a build artifact and (once the UI stabilizes) diff against
an approved baseline set.

---

## What the committed flows cover

| Flow file | Screens captured |
|-----------|------------------|
| `01-trips.yaml` | Trips list (top + scrolled) — live/planning/completed cards |
| `02-trip-home.yaml` | Trip workspace home (Plan), Map (fallback), group Chat |
| `03-concierge-private-chat.yaml` | Concierge home + private Vesper chat thread |
| `04-plan.yaml` | Plan itinerary (top + scrolled) — block-state hierarchy |
| `05-discover.yaml` | Discover feed (top + scrolled) |
| `06-me.yaml` | Me profile (top + scrolled) + "What Vesper knows" |

### Selector notes (debt to clean up)

The app exposes only ~3 `testID`s today, so flows lean on **visible tab
labels** ("Trips", "Concierge", "Discover", "Me"), **ScreenHeader titles**,
and **trip-workspace pill text** ("Chat", "Plan", "Map", "Photos",
"Memory"). Two soft spots a future change should harden:

- **Trip cards** are matched by seeded city name (`.*Lisbon.*`). If dogfood
  fixtures change, update the regex — or add a `testID` to the first
  `TripCard` so flows can target it by role instead of copy.
- **Discover** has no stable post-navigation header to `assertVisible` on;
  consider a `testID` on the screen root.

Prefer extending existing **accessibility labels** over adding `testID`s —
keep `testID`s for non-copy automation anchors only.

---

## Scenario pack (target coverage)

The committed flows are a first slice. The full dogfood-critical state pack
(from the area report) the lane should grow to cover — seeded with a **fixed
clock and fixed IDs** so snapshots stay stable (two mock openers currently
use `new Date()` in `constants/mocks/chat.ts` and should move to a QA clock):

**Trips**
- Live trip, planning trip, completed trip
- No-trip / empty welcome state

**Concierge (private Vesper)**
- First-contact thread
- Long Vesper note (multi-paragraph reply)
- Streaming / loading state
- Failed send / offline composer

**Trip workspace**
- Trip home, group chat
- Plan day with confirmed / tentative / cancelled / **conflict** blocks
- Map with route **and** map-unavailable fallback
- Group **vote / proposal pending**
- Photos, expenses (form + error), settings

**Discover / Me**
- Discover feed: sparse vs rich items; place / venue / angle detail
- Me: profile, "What Vesper knows", constraints / privacy, account, feedback
- Memory story with **missing photos**

**System states**
- Notification permission rationale
- Location / microphone / photo permission prompts
- Offline / error banners
- Small-device keyboard composer state

---

## Recommended viewport matrix

Capture before each dogfood release (CI runs one size; full matrix is a local
pre-release pass):

| Viewport | Why |
|----------|-----|
| iPhone SE width (~320pt) | Smallest supported — cramped-layout regressions |
| 390pt iPhone (e.g. 14/15) | The common case |
| Large iPhone (Pro Max) | Wide-layout / safe-area check |
| **Large Dynamic Type** (XL / Accessibility) | Text overflow, badge growth, touch targets — run on private chat, Plan, trip home, settings, composer |
| One Android emulator (optional) | 48dp target baseline |

Set Dynamic Type via the simulator's **Settings → Accessibility → Display &
Text Size → Larger Text** before re-running the lane, and pair the screenshot
gallery with a manual **Accessibility Inspector** pass for touch-target and
contrast checks (Vesper's 44pt minimum is non-negotiable).
