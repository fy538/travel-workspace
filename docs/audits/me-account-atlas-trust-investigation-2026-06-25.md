# Me / Account → Atlas Profile & Trust Investigation

**Date:** 2026-06-25
**Repo:** `travel-app`
**Scope:** Legacy `app/(tabs)/me/*` vs newer `app/atlas/*` trust surfaces
**Status:** **Phase 1 engineering complete** (2026-06-25). Phase 2 design extensions: see [`trust-design-extensions-2026-06-25.md`](trust-design-extensions-2026-06-25.md).

### Implementation snapshot (2026-06-25)

| Item | Status |
|------|--------|
| Me tab + `app/(tabs)/me/*` deleted | ✅ |
| `routes.constraints()` → `/atlas/constraints` | ✅ |
| `routes.people()` → `/atlas/following` | ✅ |
| `routes.privacyAudit()` → `/atlas/data-receipt` | ✅ |
| Trust surfaces on TrustControlsKit + AtlasNativeScaffold | ✅ (constraints/following interiors pending design) |
| Profile + Account live delegation summary | ✅ |
| Export deduped (Account only) | ✅ |
| Memory receipt link → data receipt | ✅ |
| Design extensions (memory receipt, constraints, people IA) | 📋 Phase 2 |

---

## Executive summary (original investigation)

The **Me tab is dead** (removed from the tab bar on 2026-06-05; Atlas supersedes it). Four tabs remain: **Trips · Vesper · Discover · Atlas**. Profile and trust controls now enter through **Atlas home → monogram → `/atlas/profile`**.

Most `routes.*` helpers already redirect Me paths to Atlas equivalents, but **~4,000 lines of Me screens remain on disk**. Two Me routes are still **live user paths**:

| Live Me route | Why it survives |
|---|---|
| `/(tabs)/me/people` | `routes.people()` — follow graph + social activity (Trips home, notification routing) |
| `/(tabs)/me/constraints` | `routes.constraints()` — hard-constraint editor linked from Atlas DNA |

Everything else under `me/` is **orphaned**: reachable only via deep URL or dead `me/index.tsx` links. The biggest product gap is a **semantic routing bug**: `routes.privacyAudit()` points to `/atlas/privacy` (visibility ledger), while the actual **data receipt** UI lives in orphaned `me/privacy-audit.tsx` and matches design block **06 · Data receipt**.

**Recommended direction:** No Me tab. Atlas tab = memory archive; monogram profile = trust hub. Consolidate remaining Me functionality into Atlas routes, delete Me files, and unify on **TrustControlsKit + AtlasNativeScaffold** as the canonical settings register (ledger/archive screens use **EditorialMasthead + LedgerRow** as a sibling tier).

---

## 1. Route inventory

### Navigation context

```
Tab bar (live)
├── Trips
├── Vesper (concierge)
├── Discover
└── Atlas  ← replaces Me tab

Atlas home (/(tabs)/atlas)
└── Monogram tap → /atlas/profile  (trust table of contents)

Me stack (/(tabs)/me) — NOT in tab bar
└── expo-router still indexes files; _layout registers 9 of 14 screens
```

### Per-route findings

| Route | File | User problem | Reachable? | Atlas duplicate? | Classification |
|---|---|---|---|---|---|
| `/(tabs)/me` | `index.tsx` | Personal hub: identity, library (memory, trips, people, saves, voice), settings/trust links | **No** — tab removed | `/(tabs)/atlas` home | **Dead** — keep file until router audit, then delete |
| `/(tabs)/me/account` | `account.tsx` | Full account: name edit, notification cadence/quiet hours/channels, sharing toggles, OAuth, export, sign-out, delete | **No** — `routes.account()` → `/atlas/account` | `/atlas/account` (slimmer) + `/atlas/notifications` | **Orphaned legacy** — richer than Atlas account; features split across Atlas |
| `/(tabs)/me/constraints` | `constraints.tsx` | Sacred hard constraints (allergies, a11y, languages), learned-fact retirement, per-dimension privacy toggles, DSAR export, reset memory | **Yes** — DNA "EDIT", `routes.constraints()` | Partial: `/atlas/privacy` (sharing only), `/atlas/dna` (read) | **Live legacy** — merge into Atlas trust |
| `/(tabs)/me/delegation` | `delegation.tsx` | Per-category Vesper autonomy (schedule, bookings, venues, group, logistics) | **No** — `routes.delegation()` → `/atlas/delegation` | `/atlas/delegation` | **Orphaned duplicate** |
| `/(tabs)/me/feedback` | `feedback.tsx` | TestFlight / in-app feedback to founder | **No** — `routes.feedback()` → `/atlas/feedback` | `/atlas/feedback` | **Orphaned duplicate** — not in `_layout` |
| `/(tabs)/me/log` | `log.tsx` | Cross-trip chronological log → trip story/detail | **No** — `routes.tripLog()` → Atlas tab | `/atlas/timeline` (conceptual) | **Orphaned** — not in `_layout` |
| `/(tabs)/me/memory` | `memory.tsx` | "Your Memory" home: DNA strip, recent story, map/log links | **No** — `routes.memoryHome()` → Atlas tab | Atlas home + `/atlas/dna` | **Orphaned** — not in `_layout` |
| `/(tabs)/me/people` | `people.tsx` | Co-travelers + **follow/unfollow** + social activity | **Yes** — Trips home, social notifications | `/atlas/companions` (read-only, different job) | **Live legacy** — needs IA decision |
| `/(tabs)/me/personal-memory` | `personal-memory.tsx` | Raw markdown "what Vesper reads before every conversation" | **No** — `routes.personalMemory()` → `/atlas/dna` | `/atlas/dna` + `/atlas/receipt` | **Orphaned** |
| `/(tabs)/me/phone` | `phone.tsx` | E.164 + SMS OTP verification | **No** — `routes.phone()` → `/atlas/phone` | `/atlas/phone` | **Orphaned duplicate** |
| `/(tabs)/me/privacy-audit` | `privacy-audit.tsx` | **Data receipt** — audit log of personal-data uses (geofence, voice, redactions) | **No** — `routes.privacyAudit()` → `/atlas/privacy` (**wrong target**) | `/atlas/receipt` is a *different* concept (memory receipt) | **Orphaned + misrouted** — should become `/atlas/data-receipt` |
| `/(tabs)/me/stories` | `stories.tsx` | Trip story archive with save toggles | **No** — `routes.storyArchive()` → Atlas tab | Atlas shelf / timeline | **Orphaned** — not in `_layout` |
| `/(tabs)/me/voice-logs` | `voice-logs.tsx` | Voice conversation archive + transcripts | **No** — `routes.voiceLogs()` → `/atlas/voice-logs` | `/atlas/voice-logs` | **Orphaned duplicate** — decorative search bar |
| `/(tabs)/me/what-vesper-knows` | `what-vesper-knows.tsx` | Transparency + **dispute** surface (DNA phrases, taste dims, interests, constraints) | **No** — `routes.whatVesperKnows()` → `/atlas/dna` (portrait, no dispute chips) | `/atlas/dna` + `/atlas/dna-dimension/[key]` | **Orphaned** — dispute UX needs a home |

### `_layout.tsx` registration gap

Registered (9): `index`, `people`, `voice-logs`, `constraints`, `account`, `phone`, `privacy-audit`, `personal-memory`, `delegation`

**Not registered** (5): `feedback`, `log`, `memory`, `stories`, `what-vesper-knows` — still routable by expo-router file convention.

### `routes.ts` redirect map

| Helper | Resolves to | Notes |
|---|---|---|
| `atlasProfile()` | `/atlas/profile` | Canonical trust hub |
| `account()` | `/atlas/account` | |
| `people()` | **`/(tabs)/me/people`** | Still Me |
| `constraints()` | **`/(tabs)/me/constraints`** | Still Me |
| `delegation()` | `/atlas/delegation` | |
| `feedback()` | `/atlas/feedback` | |
| `phone()` | `/atlas/phone` | |
| `privacyAudit()` | `/atlas/privacy` | **Bug:** should be data receipt, not privacy ledger |
| `whatVesperKnows()` / `personalMemory()` | `/atlas/dna` | Dispute UI lost on redirect |
| `memoryHome()` / `storyArchive()` / `tripLog()` | `/(tabs)/atlas` | |
| `voiceLogs()` | `/atlas/voice-logs` | |
| `atlasReceipt()` | `/atlas/receipt` | Memory receipt (signals/artifacts) |
| `savedVenues()` | `/atlas/saved-places` | |

---

## 2. Duplication map

```
LEGACY ME                          ATLAS / TRUST                         RELATIONSHIP
─────────────────────────────────────────────────────────────────────────────────────
me/index (dead hub)          →     atlas tab home                        FULL REPLACE
me/account                   →     atlas/account + atlas/notifications     SPLIT (Me richer)
me/constraints               →     atlas/privacy + atlas/dna + NEW editor  PARTIAL (constraints unique)
me/delegation                ≈     atlas/delegation                        DUPLICATE (use Atlas)
me/feedback                  ≈     atlas/feedback                          DUPLICATE
me/phone                     ≈     atlas/phone                             DUPLICATE
me/voice-logs                →     atlas/voice-logs                        SUPERSEDED (Atlas better)
me/privacy-audit             ✗     atlas/privacy (misrouted)               WRONG LINK
                             ?     atlas/receipt                           DIFFERENT (memory vs audit)
me/what-vesper-knows         →     atlas/dna (+ dimension pages)           DISPUTE UX GAP
me/personal-memory           →     atlas/dna / atlas/receipt               SUPERSEDED
me/memory / log / stories    →     atlas home / timeline / postcards     SUPERSEDED
me/people                    ≠     atlas/companions                        DIFFERENT JOB (follow vs co-travel)
```

### Three "receipt" concepts (currently conflated)

| Concept | Design name | Implementation | Content |
|---|---|---|---|
| **Visibility ledger** | Privacy | `/atlas/privacy` | Sharing dimensions, public profile toggles |
| **Memory receipt** | Full memory receipt (linked from Privacy) | `/atlas/receipt` | Artifacts, signals, taste material, DNA read |
| **Data receipt** | Data receipt · privacy audit (design §06) | `me/privacy-audit.tsx` only | Timestamped audit events: location, voice, redactions |

`routes.privacyAudit()` and Privacy's "Full memory receipt" row both confuse **data audit** vs **memory receipt**. Design artifact keeps them separate.

---

## 3. Visual audit

### Design canon reference

`Vesper Trust & Controls System.html` + `trust-screens.jsx` define:

- **Profile** — monogram masthead, standing prose, stamped zones, flat hairline rows (not nested iOS cards)
- **Account** — YOU / ACCESS / YOUR RECORDS / ACCOUNT zones
- **Privacy** — contract + `PrivRow` with state pill before toggle
- **Notifications** — posture summary receipt, segmented cadence, quiet hours
- **Trip controls** — scoped trust (see `app/trip-settings`)
- **Data receipt** — TODAY / YESTERDAY / OLDER groups, `ReceiptRow` with DROPPED badge
- **Ledger language** — bare 23px icons, 58–68px rows, mono stamped headers, paper surfaces

`Vesper Row System.html` defines generic row primitives later mirrored in `ListRow` / `SettingsList`.

### Screen-by-screen visual assessment

| Screen | Matches Vesper language? | Centralized primitives? | Polish (1–5) | Issues |
|---|---|---|---|---|
| **atlas/profile** | ✅ Yes | TrustControlsKit, AtlasNativeScaffold | **5** | Canonical reference |
| **atlas/account** | ✅ Yes | TrustControlsKit | **4** | Hardcoded conversation/narration counts (`148`, `32`) |
| **atlas/privacy** | ✅ Yes | TrustPrivacyRow, TrustContract | **5** | |
| **atlas/notifications** | ✅ Yes | TrustSegmented, TrustReceipt | **4** | Quiet hours display-only (no inline picker) |
| **atlas/delegation** | ◐ Partial | AtlasNativeScaffold; custom chip picker | **3** | Should use TrustSegmented per canon |
| **atlas/receipt** | ◐ Partial | AtlasNativeCard/Metric (not Trust receipt rows) | **3** | Metric strip conflicts with "prose not metrics" canon |
| **atlas/companions** | ◐ Partial | Bespoke rows, not TrustRow | **3** | |
| **atlas/dna** | ✅ Intentional break | Custom portrait layout | **4** | Content register, not settings — correct |
| **atlas/voice-logs** | ✅ Ledger tier | EditorialMasthead, LedgerRow | **4** | |
| **atlas/narration-history** | ✅ Ledger tier | EditorialMasthead, LedgerRow | **4** | |
| **atlas/feedback** | ❌ Legacy | ScreenHeader, Card, Button | **2** | Visual downgrade from profile |
| **atlas/phone** | ❌ Legacy | ScreenHeader, Card, Button | **2** | Downgrade from account TrustFieldRow entry |
| **me/index** | ◐ Pre-Atlas | CompactHeaderBar, Card, custom bottom links | **3** | Dead; mixed row styles |
| **me/account** | ◐ Transitional | SettingsList + ScreenHeader | **4** | Most complete notification editor in codebase |
| **me/constraints** | ◐ Mixed | SettingsList + custom constraint chips | **3** | Circular chip pills, Card-heavy |
| **me/people** | ❌ Legacy | ScreenHeader, Card, custom FollowButton | **3** | Generic list rows |
| **me/privacy-audit** | ✅ Trust kit | TrustReceiptRow — **best Me screen** | **4** | Uses ScreenHeader not AtlasNativeScaffold |
| **me/what-vesper-knows** | ◐ Custom | letterpress cards, chip dispute UI | **3** | Bespoke header; rich interactions orphaned |
| **me/voice-logs** | ❌ Legacy | Circular mic icon container, Card | **2** | Non-functional SearchBar |

### Recurring visual debt

1. **Circular icon containers** — `me/voice-logs`, older Card rows (Atlas voice-logs fixed with LedgerRow)
2. **ScreenHeader + Card form pattern** — feedback, phone (both Me and Atlas copies)
3. **SettingsList vs TrustControlsKit split** — SettingsList documented for trust pages but migrated screens use TrustControlsKit instead
4. **One-off bottom link rows** — `me/index` hairline + Ionicons (predates row system)
5. **Hardcoded metadata** — atlas/account record counts undermine trust posture

---

## 4. Product architecture — keep / merge / redesign / delete

| Screen | Recommendation | Rationale |
|---|---|---|
| `me/index` | **Delete** (after router confirm) | Dead tab; Atlas home replaces |
| `me/account` | **Delete** after porting gaps | Notification quiet-hours picker lives here only — belongs in `/atlas/notifications` |
| `me/constraints` | **Merge → `/atlas/constraints`** (new) or split: hard constraints → DNA editor sheet; privacy dims → already in privacy; reset/export → account | Single sacred editor; retire ScreenHeader pattern |
| `me/delegation` | **Delete** | Duplicate of atlas/delegation |
| `me/feedback` | **Delete** | Duplicate; **redesign** atlas/feedback to Trust kit |
| `me/log`, `memory`, `stories` | **Delete** | Superseded by Atlas timeline / home |
| `me/people` | **Redesign + merge partially** | Split: co-travelers → companions; following graph → new `/atlas/following` or Discover social |
| `me/personal-memory` | **Delete** | Superseded by dna + receipt |
| `me/phone` | **Delete** | Duplicate; **redesign** atlas/phone as Trust form |
| `me/privacy-audit` | **Move → `/atlas/data-receipt`** | Wire `routes.privacyAudit()` correctly; adopt AtlasNativeScaffold |
| `me/voice-logs` | **Delete** | Superseded |
| `me/what-vesper-knows` | **Merge dispute UX → atlas/dna-dimension + receipt** | Portrait stays; contestability on dimension pages |

### Global vs trip-scoped controls

| Global (Profile / Trust) | Trip-scoped (`/trip-settings`) |
|---|---|
| Travel DNA, companions, sharing dimensions | Per-trip notification cadence override |
| Notification cadence, quiet hours, channels | Vesper autonomy for *this trip* (organizer) |
| Global delegation categories | Group voting, plan editing policy |
| Account, phone, export, delete | Budget band, leave trip |
| Voice logs, narration history | — |
| Data receipt (audit log) | Trip activity (`routes.tripActivity`) |
| Memory receipt | — |

Trip settings (`app/trip-settings/index.tsx`) already uses **TrustControlsKit** — aligned with design §05.

### Normal users vs power users

| Surface | Audience |
|---|---|
| Atlas home, DNA portrait, companions | **All users** |
| Profile hub, privacy, notifications | **All users** (trust is default onboarding) |
| Account (sign-in, phone, sign-out) | **All users** |
| Delegation, data receipt | **Power / trust-curious** — linked from profile, not marketed |
| Memory receipt, dimension dispute, constraints editor | **Power users** correcting the model |
| Following graph (`me/people`) | **Social power users** |
| Feedback | **All users** (TestFlight path) |
| `dev/persona-switcher` | **Internal only** |

---

## 5. Target information architecture

### Should there still be a "Me" tab?

**No.** The decided architecture is:

- **Atlas tab** = living archive (memory, places, timeline, boards)
- **Profile** (monogram on Atlas home) = trust & identity controls
- **Account** = credentials, records, destructive actions (linked from Profile)

Me tab removal is already shipped; finish the migration by deleting orphaned files and fixing the two live Me routes.

### Concept glossary

| Term | What it is | Where it lives |
|---|---|---|
| **Profile** | Trust table of contents — "what Vesper knows" + "how it behaves" + account links | `/atlas/profile` |
| **Account** | Legal identity, access (phone/OAuth), records, sign-out/delete | `/atlas/account` |
| **Privacy** | Visibility ledger — what categories are private / group / shareable | `/atlas/privacy` |
| **What Vesper knows** | User mental model for taste + memory transparency | **`/atlas/dna`** (portrait) + **`/atlas/receipt`** (structured) + dimension pages |
| **Travel DNA** | Archetype + learned dimensions (reading, not form) | `/atlas/dna`, `/atlas/dna-dimension/[key]` |
| **Companions** | Who you *travel with* (frequency-derived) | `/atlas/companions` |
| **People / Following** | Social graph — who you *follow* (different data) | Today: `me/people` → should leave Me stack |
| **Delegation / Vesper autonomy** | Global decision categories (ask / suggest / auto) | `/atlas/delegation` |
| **Notifications** | Global cadence, quiet hours, channels | `/atlas/notifications` |
| **Voice logs** | Conversation transcript archive | `/atlas/voice-logs` |
| **Narration history** | Place narration replay cache | `/atlas/narration-history` |
| **Memory receipt** | What Vesper remembers — artifacts, signals, taste material | `/atlas/receipt` |
| **Data receipt** | Audit log of data *uses* (location, voice, redactions) | **Missing live route** — implement `/atlas/data-receipt` from `me/privacy-audit` |
| **Constraints** | Sacred declared prefs (allergies, a11y, languages) | **`me/constraints`** today → `/atlas/constraints` |
| **Trip controls** | Scoped settings for one trip | `/trip-settings?tripId=` |

### Proposed navigation tree

```
Atlas (tab)
├── [Home archive — desk, reel, shelf rooms]
├── Monogram → Profile
│   ├── Travel DNA ──────────────→ /atlas/dna
│   │   └── [dimension] ─────────→ /atlas/dna-dimension/:key
│   ├── Companions ──────────────→ /atlas/companions
│   ├── What you share ──────────→ /atlas/privacy
│   │   ├── Memory receipt ──────→ /atlas/receipt
│   │   ├── Data receipt ────────→ /atlas/data-receipt  [NEW]
│   │   └── Removed moments ─────→ /atlas/removed
│   ├── Quiet by default ────────→ /atlas/notifications
│   ├── Vesper autonomy ─────────→ /atlas/delegation
│   ├── Account & sign-in ───────→ /atlas/account
│   │   ├── Phone verify ────────→ /atlas/phone
│   │   ├── Voice logs ──────────→ /atlas/voice-logs
│   │   ├── Narrations ──────────→ /atlas/narration-history
│   │   └── Declared constraints → /atlas/constraints  [NEW]
│   └── Send feedback ───────────→ /atlas/feedback

Trips → Trip detail → Trip settings (/trip-settings)
Discover → "Tune Discover" → /atlas/dna (today via whatVesperKnows())
Social notifications → /atlas/following [NEW] or companions (TBD)
```

---

## 6. Implementation readiness

### Available primitives

| Component | Path | Role | Canon status |
|---|---|---|---|
| **TrustControlsKit** | `components/trust/TrustControlsKit.tsx` | TrustZone, TrustRow, TrustPrivacyRow, TrustFieldRow, TrustReceiptRow, TrustSegmented, TrustContract, TrustMonogram, state pills | **Canonical for trust/settings** |
| **AtlasNativeScaffold** | `components/atlas/AtlasNativeScaffold.tsx` | Collapsing header, eyebrow, display title, meta | **Canonical shell for trust screens** |
| **EditorialMasthead + LedgerRow** | `components/ui/rows/*` (ledger tier) | Archive/history screens (voice, narrations) | **Canonical for ledger tier** |
| **SettingsList** | `components/ui/SettingsList.tsx` | SettingsGroup + SettingsRow over CardSurface | **Secondary** — row-system compat; superseded by TrustRow for trust pages |
| **ListRow** | `components/ui/ListRow.tsx` | Generic list primitive | **General purpose** — not used in trust surfaces yet |
| **CardSurface** | `components/ui/CardSurface.tsx` + `constants/cardSurface.ts` | Material taxonomy for cards | Powers SettingsList; trust uses flat paper zones instead |
| **ScreenHeader** | `components/ui/ScreenHeader.tsx` | Legacy back + title | **Deprecate for trust** — keep for non-trust modals only |
| **ScreenScaffold** | (if present elsewhere) | — | Prefer AtlasNativeScaffold in Atlas/trust context |

### Recommended canonical stack

```
Trust / profile / account / privacy / notifications / delegation / trip-settings
  → AtlasNativeScaffold + TrustControlsKit

Archive / history (voice logs, narrations, data receipt timeline)
  → EditorialMasthead + LedgerRow (+ TrustReceiptRow for data receipt)

Content portrait (Travel DNA)
  → Custom layout (intentional — not a settings screen)

Forms needing keyboard (feedback, phone OTP)
  → AtlasNativeScaffold + TrustFieldRow/TrustRow OR redesigned trust form kit
    (NOT legacy ScreenHeader + Card)
```

### Feature parity gaps (Me → Atlas)

| Feature | Me has it | Atlas has it |
|---|---|---|
| Display name edit inline | ✅ `me/account` | ❌ read-only TrustFieldRow |
| Notification cadence + quiet hours picker | ✅ `me/account` | ◐ `/atlas/notifications` (cadence yes; quiet hours display-only) |
| Push channel toggles | ✅ `me/account` | ✅ notifications |
| Public profile / followers toggles | ✅ `me/account` | ✅ privacy |
| Hard constraint chip editor | ✅ `me/constraints` | ❌ (link only from DNA) |
| Learned-fact retirement | ✅ `me/constraints` | ❌ |
| Reset concierge memory | ✅ `me/constraints` | ❌ |
| Per-item dispute (taste, interests) | ✅ `what-vesper-knows` | ◐ dimension pages only |
| Follow / unfollow | ✅ `me/people` | ❌ |
| Data receipt audit log | ✅ `me/privacy-audit` | ❌ (mislinked) |
| Support links (help, terms) | ✅ `me/account` | ❌ |

---

## 7. Implementation plan (phased)

### Phase 0 — Routing hygiene (low risk)

1. Add `routes.atlasDataReceipt()` → `/atlas/data-receipt` (move `me/privacy-audit.tsx`)
2. Fix `routes.privacyAudit()` to point to data receipt, not privacy
3. Update Privacy "Full memory receipt" copy if needed to disambiguate memory vs data receipt
4. Point `routes.constraints()` → `/atlas/constraints` once screen exists
5. Decide `routes.people()` target (companions vs new following screen)

### Phase 1 — Close feature parity

1. Port quiet-hours **picker** from `me/account` → `atlas/notifications`
2. Create `/atlas/constraints` with TrustControlsKit (hard constraints + learned facts + reset)
3. Remove privacy-dimension toggles from constraints screen (already in `/atlas/privacy`) to avoid duplication
4. Wire real conversation/narration counts in `atlas/account` (remove `148` / `32`)
5. Add name edit to account (TrustFieldRow action → modal)

### Phase 2 — Visual unification

1. Migrate `atlas/delegation` chips → `TrustSegmented`
2. Migrate `atlas/receipt` metrics → prose + `TrustReceiptRow` list (per design)
3. Redesign `atlas/feedback` + `atlas/phone` on Trust kit
4. Migrate `atlas/companions` rows → `TrustRow`
5. Port dispute affordances from `what-vesper-knows` into DNA dimension pages or receipt

### Phase 3 — Social IA

1. Split `me/people`: co-traveler detail → companions; following → `/atlas/following` or Discover
2. Update `notificationDestination.ts` + Trips home `onOpenPeople`
3. Delete `me/people.tsx`

### Phase 4 — Delete Me stack

1. Remove `app/(tabs)/me/` directory (or leave stub redirect layout during transition)
2. Remove dead components only used by Me (`components/me/*` audit first)
3. Update tests (`privacy-audit.smoke.test.tsx`, notification routing tests)
4. Confirm expo-router does not register ghost routes

### Phase 5 — Design validation

Run Claude Design board (prompt below) for screens still visually ambiguous: constraints editor, following vs companions, feedback/phone trust forms, data receipt empty states.

---

## 8. Claude Design follow-up prompt

The existing **Vesper Trust & Controls System** artifact covers Profile, Account, Privacy, Notifications, Trip Controls, Data receipt, and row tokens. It does **not** fully specify: Travel DNA portrait, Companions vs Following, Memory receipt (signal-based), Constraints editor, Feedback/phone trust forms, or Atlas-profile entry from the monogram.

Use this prompt for a **"Vesper Profile, Account & Trust System"** full-screen board:

---

**Claude Design prompt:**

> Design a complete **Vesper Profile, Account & Trust System** for a travel app. Full-screen iPhone frames only (not isolated components). Use the existing Vesper trust ledger language: warm paper (`#E7E0D2`), EB Garamond display, DM Sans UI, mono stamped zone headers with gold diamond, flat hairline rows on paper (no nested iOS cards), state pills (PRIVATE / GROUP / SHAREABLE / VERIFIED / MINIMAL / ASK FIRST), receipt slips for summaries, oxblood for destructive actions only.
>
> **Context:** Atlas is the tab for memory archive. Profile opens from a monogram on Atlas home — it is the **trust table of contents**, not another dashboard. There is no "Me" tab.
>
> **Deliver full screens for:**
>
> 1. **Profile home** — monogram masthead, member-since prose (not a metric strip), zones: WHAT VESPER KNOWS (Travel DNA, Companions, What you share), HOW VESPER BEHAVES (Quiet by default, Vesper autonomy), ACCOUNT (Account & sign-in, Send feedback). Show quiet-state pill in masthead.
>
> 2. **Account & sign-in** — variants: phone verified, phone missing, demo mode (delete disabled). Zones: YOU (name, email), ACCESS (phone, Apple, Google), YOUR RECORDS (conversations count, narrations count, How Vesper decides, Download my data), ACCOUNT (feedback, sign out, delete). Use field rows (mono label + serif value).
>
> 3. **Privacy** — visibility contract, five sharing dimensions with pill-before-toggle rows, public profile toggles, THE RECORD section linking to Memory receipt and Removed moments.
>
> 4. **What Vesper knows / Travel DNA portrait** — full-bleed **portrait** (minimal scroll): archetype nameplate, Vesper pull-quote, four dimension doors as hairline rows, declared constraints line, floating "Talk to Vesper". This is a *reading*, not settings.
>
> 5. **Travel DNA dimension detail** — one dimension (e.g. Energy): learned read, evidence count, trips behind it, contest/dispute affordance, link to memory receipt.
>
> 6. **Companions** — frequency-ranked co-travelers, invite-to-trip CTA, honest empty state. Not an address book.
>
> 7. **Following** (separate from Companions) — social follow graph with follow/unfollow, friend activity feed. Clarify visual distinction from Companions.
>
> 8. **Declared constraints editor** — allergies, accessibility, languages as sacred chips; learned facts with retire action; reset memory (destructive, guarded).
>
> 9. **Vesper autonomy / delegation** — five categories with segmented control (Ask first / Suggest & confirm / Handle it) using trust segmented, not bubbly chips.
>
> 10. **Notification cadence** — posture summary receipt, Eager/Default/Minimal segmented, quiet hours with time picker affordance, channel toggles, Critical always on, Pause all, iOS push-off warning state.
>
> 11. **Voice & narration history** — ledger-style archive with search, expandable transcript row (voice) and replay row (narration). Distinct from settings register — editorial masthead.
>
> 12. **Memory receipt** — what Vesper remembers: current DNA read as quotes, taste material chips, links to correct DNA and privacy. Prose-first, not a dashboard metric strip.
>
> 13. **Data receipt** — audit log of data uses grouped TODAY/YESTERDAY/OLDER; redacted events show DROPPED badge. Empty state with example rows. Dev/stub data banner variant.
>
> 14. **Feedback / contact** — trust-styled form (not generic Card), attaches version/build context, success state.
>
> 15. **Phone verification** — OTP flow on trust paper, E.164 field, verify CTA, return-to-account success.
>
> 16. **Destructive account actions** — delete confirmation sheet, demo-mode disabled state.
>
> 17. **Empty / loading / error states** for: Profile (new user), DNA (insufficient signal), Companions empty, Data receipt empty, Voice logs empty, Memory receipt cold start, network error on Account.
>
> **Explicitly show:** entry from Atlas monogram → Profile; Profile → each child screen; Privacy → Memory receipt vs Data receipt (two different receipts). Include one **Trip controls** frame scoped to a single trip (organizer vs guest) for contrast with global trust.
>
> Match the tone: calm, grown-up, trustworthy — not generic iOS Settings.

---

## 9. Appendix — inbound link index

| Caller | Target route helper |
|---|---|
| Atlas home monogram | `routes.atlasProfile()` |
| Atlas profile | delegation, account, feedback, dna, companions, privacy, notifications |
| Atlas account | phone, voiceLogs, narrationHistory, delegation, feedback |
| Atlas privacy | atlasReceipt, atlasTimelineRemoved |
| Atlas dna | `routes.constraints()` |
| Discover "Tune" | `routes.whatVesperKnows()` → dna |
| Trips home | `routes.people()` |
| Social notifications | `routes.people()` |
| Trip detail | `routes.tripSettings()` |
| Dead me/index | account, constraints, privacyAudit, delegation, feedback, people, memory, voiceLogs, whatVesperKnows |

---

## 10. Summary decision table

| Item | Decision |
|---|---|
| Me tab | **Gone** — do not restore |
| Profile home | **Keep** `/atlas/profile` as trust hub |
| Me index, memory, log, stories | **Delete** |
| Me account, delegation, feedback, phone, voice-logs | **Delete** (Atlas copies win after parity) |
| Me constraints | **Migrate** → `/atlas/constraints` |
| Me privacy-audit | **Migrate** → `/atlas/data-receipt`; fix routing |
| Me what-vesper-knows | **Delete**; port dispute UX to DNA/receipt |
| Me people | **Split** — companions vs following; then delete |
| Atlas receipt | **Redesign** to Trust receipt rows (less metrics) |
| Atlas delegation | **Redesign** to TrustSegmented |
| Atlas feedback + phone | **Redesign** to trust forms |
| SettingsList | **Keep** for non-trust settings; not canonical for trust |
| TrustControlsKit + AtlasNativeScaffold | **Canonical** for trust/profile/account |
