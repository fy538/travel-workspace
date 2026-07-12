---
doc_type: working
status: active
owner: frontend / design
created: 2026-07-11
expires: 2026-08-10
why_new: Consolidate page-level header chrome onto the established shared primitives.
supersedes: []
---

# Header chrome consolidation plan

Date: 2026-07-11  
Repo: `travel-app` (work from `main`)  
Related: Cursor canvas `header-chrome-icon-audit.canvas.tsx` (local IDE artifact, not in-repo), `docs/audits/header-chrome-audit-20260617.md`, `design/archive/2026-07/code-alignment-brief-J1-header-consolidation.md`, `docs/design-alignment/HEADER-SYSTEMS.md`

## Goal

Every top-left / top-right **page** control uses a shared primitive. No route-level raw `Ionicons chevron-back`. No bespoke circle fills outside `FloatingGlassIconButton`. Keep the six families — do not merge them into one mega-header.

## Locked decisions (proposed defaults)

Confirm or override before Phase 1:

| Decision | Proposed default | Why |
|---|---|---|
| Pushed parchment lists opened from glass (Notifications, voice logs, narration history) | **`EditorialMasthead floating` → paper glass** | Matches Conversations history / All Trips; fixes glass-entry → bare-destination |
| `FloatingChatHeader` | **Thin pass** — keep API, swap internals to `FloatingGlassIconButton` + `HeroChrome` | Removes 4th circle style without rewriting chat screens |
| `ReaderChrome` | **Leave bare** | Explicit doctrine; not an offender |
| Trip folio dark glass / place / venue heroes | **Leave** | Correct immersive register |
| Productive `ScreenHeader` / costs / trip-info | **Leave bare** | Correct parchment task register |
| Trip Story `MemoryStoryHeader` | **Park on J2** unless J2 is still deferred — then do as Phase 4 standalone | Matches existing J1 brief |

If you prefer Notifications stay bare instead, the alternate is: strip glass from Trips-home `NotificationBell` so entry/destination both bare. Default below assumes **paper glass**.

---

## Family map (do not collapse)

| Family | Canonical primitive | Icon treatment |
|---|---|---|
| A productive | `ScreenHeader` / `ProductiveHeader` | Bare `PageChromeIconButton` |
| A editorial | `EditorialMasthead` | `floating` → paper glass; else bare (setup-only) |
| A collapsing | `AtlasCompactHeader` / `CompactHeaderBar` | Paper (or dark) glass |
| B hero | `HeroChrome` + `FloatingGlassIconButton` | `dark` over photo; `canvas` on plan map |
| C chat | `FloatingChatHeader` | Must compose glass primitives (after Phase 2) |
| D tab-root | Right-cluster glass on Trips/Atlas/Discover homes | Paper glass |
| E sheet | `SheetHeader` | Bare close (unchanged) |
| F reader | `ReaderChrome` | Bare by doctrine (unchanged) |

**Anti-fork rule:** a pushed screen with back + one task picks an existing family. No new header components.

---

## Offender backlog → target

### Phase 0 — Guard (cheap, do first)

1. Add a Jest convention test: fail if `app/**/*.tsx` contains route-level `Ionicons` / `name="chevron-back"` outside an allowlist (inline row chevrons, year steppers, list-row affordances).
2. Short taxonomy note next to primitives (or amend `HEADER-SYSTEMS.md`) with the family map above + glass variant matrix (`dark` / `paper` / `canvas` / `bare`).
3. Fix `NotificationBell` Trips-home hack: use real glass `PageChromeIconButton` (or first-class glass support on the bell) instead of wrapping with `floatingGlassIconButtonStyle`.

### Phase 1 — Glass-entry destinations (highest visual risk)

| Offender | File | Change |
|---|---|---|
| Notifications | `app/notifications/index.tsx` | `EditorialMasthead floating` (+ floating title treatment; keep “Mark read” via floating `rightLabel`) |
| Voice logs | `app/atlas/voice-logs.tsx` | same |
| Narration history | `app/atlas/narration-history.tsx` | same |

**Done when:** back matches Conversations history paper glass; opened-from-bell / Atlas archive flows no longer flash bare chevron.

### Phase 2 — Kill the fourth circle style

| Offender | File | Change |
|---|---|---|
| Chat header internals | `components/chat/FloatingChatHeader.tsx` | Rebuild chrome buttons on `FloatingGlassIconButton` (`paper`) + layout via `HeroChrome` (or equivalent). Preserve public props so `concierge/chat`, `trips/.../chat`, `ConversationCreateHeader` stay call-site stable. |
| Call-site smoke | those 3 consumers | Visual/device check only if API unchanged |

**Done when:** chat circles share the same fill/hairline/size tokens as paper glass elsewhere.

### Phase 3 — Raw chevron P0 setup / misc routes

Replace page-level raw `chevron-back` with the correct family:

| Offender | Likely target |
|---|---|
| `app/onboarding.tsx` | Bare `PageChromeIconButton` (or explicit onboarding exemption documented in allowlist) |
| `app/trip-dates/index.tsx` | `ScreenHeader` |
| `app/trip-begin.tsx` | `ScreenHeader` or bare `PageChromeIconButton` |
| `app/invite-code.tsx` | `ScreenHeader` or bare `PageChromeIconButton` |
| Re-check stale audit hits | `dossier` (should already be `ReaderChrome`), `trip-place`, `your-map` if still present |

**Done when:** convention test is green with only intentional allowlist entries.

### Phase 4 — Hand-rolled trip specialists

| Offender | Change |
|---|---|
| `PlanFocusedHeader` in `plan.tsx` | Migrate list face → `ProductiveHeader` (back + “Trip” + right actions). Map face already uses canvas glass — keep. |
| `TripHeader.tsx` | If still used by secondary trip faces: either adopt glass when over hero, or bare `PageChromeIconButton` consistently — no raw `IconButton` one-offs. |
| Atlas `boards.tsx` / `shared-links.tsx` | Route through `AtlasCompactHeader` instead of one-off header rows. |
| Experience full-screen (`ExperienceDetailSheet` screen mode) | If hero-first full screen: dark glass back like Place/Venue; if parchment: `ScreenHeader`. Pick one register. |
| `MemoryStoryHeader` | Prefer park until Trip Story J2; if J2 still deferred, migrate to `ScreenHeader` (+ small prop if status line needs it). |

### Phase 5 — Harden

1. Expand convention test to flag bespoke `borderRadius: radius.full` + back icon outside `FloatingGlassIconButton` / allowlist.
2. Update `HEADER-SYSTEMS.md` / regenerate `npm run design:headers` after migrations.
3. Device dogfood checklist: Notifications, Conversations history, Trip folio, Concierge chat, Plan list+map, All Trips, Atlas voice logs, onboarding back.

---

## Explicit non-goals

- Do **not** merge `ScreenHeader` + `EditorialMasthead` + `CompactHeaderBar`.
- Do **not** put dark glass on parchment task screens.
- Do **not** put bare chevrons on photo heroes.
- Do **not** change ReaderChrome to glass.
- Do **not** invent a 7th header component.

---

## Suggested PR slices (landable)

1. **PR-A** — Phase 0 guard + taxonomy note + NotificationBell fix  
2. **PR-B** — Phase 1 floating mastheads (notifications + voice logs + narration)  
3. **PR-C** — Phase 2 FloatingChatHeader internals  
4. **PR-D** — Phase 3 raw chevrons  
5. **PR-E** — Phase 4 plan / TripHeader / Atlas boards / experience (Story optional / parked)

Each PR: typecheck + convention test + visual check of touched surfaces on device (layer-4 claim only after device).

---

## Effort sketch

| Phase | Size | Risk |
|---|---|---|
| 0 Guard | S | Low |
| 1 Floating lists | S | Low (prop flip + spacing/insets) |
| 2 Chat internals | M | Medium (chat layout/safe-area) |
| 3 Raw chevrons | S–M | Low |
| 4 Specialists | M | Medium (plan header behavior) |
| 5 Harden | S | Low |

---

## Decisions locked (2026-07-11 implementation)

1. Paper glass for Notifications / voice logs / narration (`floating` + `titleSurface="plain"`).
2. Thin chat pass — `FloatingChatHeader` internals on shared glass primitives.
3. Trip Story `MemoryStoryHeader` remains parked on J2.

## Implementation status

- Phase 0–3 + Experience / PlanFocusedHeader chrome: done in travel-app working tree.
- Atlas boards / shared-links already on `FloatingGlassIconButton` (kept).
- Story header: still parked.
