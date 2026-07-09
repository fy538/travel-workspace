# Code Alignment — Chat: Composer Shape Divergence (2026-07-08)

Repo: `~/travel-workspace/travel-app`. Canon: `~/travel-workspace/design/vesper-canon-anchor/project/vesper-composer.jsx` + `chat-narration-band.jsx` (read-only). This is a narrow, single-issue brief — the Chat surface overall is faithfully aligned: `resolveNarrationBandStack` (`utils/narrationBandStack.ts`) reproduces canon's exact priority order (companion > lease conflict > geofence > permission), 2-band cap, and collapse-into-subtitle rule; `ComposerBar.tsx` already consolidated the two historical near-identical pills (`Composer` + `ChatComposer`) into one component per canon's stated goal, and reuses the exact `VCspark` SVG path. The one concrete miss is the shape half of canon's own thesis.

Standing rules: git status first (branch from main) · snap rule (app tokens are value truth) · one commit per task · typecheck+tests green · no push without approval · **flag backend-gated items, do not fake data** (none of the items below are backend-gated — this is a pure FE styling/token fix).

## Task 1 — Thread composer renders as a full pill, not canon's squared/soft shape

Canon `vesper-composer.jsx:24-58` (`VComposer`) and its board (`vesper-composer.jsx:77-84`) make "one composer, two shapes" the explicit spec: `shape='pill'` (borderRadius 999) at home, `shape='soft'` (borderRadius **17**) in the thread — the code comment even says "The softer bar holds a growing, multi-line reply and reads more editorial in the thread." This is not a cosmetic nuance; it's the named thesis of the whole file.

Current code collapses both contexts onto the same fully-rounded pill:
- `components/chat/ComposerBar.tsx:704-713` (`inputPill`, home/`inlineMode`) — `borderRadius: radius.full` (9999).
- `components/chat/ComposerBar.tsx:714-724` (`inputFloatingThread`, thread/`floatingThreadMode`) — **also** `borderRadius: radius.full` (9999).

Both call sites confirm the intended split is context-driven, not accidental:
- `app/(tabs)/concierge/index.tsx:1030-1031` — home composer passes `inlineMode`.
- `app/(tabs)/concierge/chat.tsx:1350,1380` — thread composer passes `floatingThreadMode`.

Fix: give `inputFloatingThread` its own radius token distinct from `radius.full`, matching canon's `shape='soft'` (17). `constants/layout.ts:37-56` already defines a `radius` scale (`md: 6`, `pill: 10`, `chip: 16`, `input: 20`, `full: 9999`) — none of these is exactly 17; either add a `soft`/`composerThread` token at 17 (matching canon literally) or reuse the closest existing scale value if the design system has since standardized a different soft-radius constant (check `constants/layout.ts` for any newer token before adding one — don't duplicate). Apply it to `inputFloatingThread` only; leave `inputPill` (home) at `radius.full`.

## Task 2 — Verify no other floatingThreadMode consumers assume the pill radius

`floatingThreadMode` is used in `app/(tabs)/concierge/chat.tsx` and possibly `app/(tabs)/trips/[tripId]/chat.tsx` (grep `ComposerBar` call sites first — 6 files import `ComposerBar` total). Confirm the radius change doesn't clip or visually break the leading sparkle/attach icon or the trailing send/mic/stop icon circles, which are sized independently (`sendIconWrapFloating`, `leadingAttachButton`) and were tuned against the old fully-round shell. Adjust icon insets only if the new corner radius creates visible clipping at the pill's ends — do not change icon sizes without a visual check.

## Done
`inputFloatingThread` (thread-context composer) renders with a distinct squared/soft radius (~17, or the nearest canon-matching token) instead of `radius.full` · `inputPill` (home-context composer) is unchanged at `radius.full` · both composer contexts checked on-device (or via polish-QA capture) for icon clipping/alignment at the new radius · typecheck + tests green.
