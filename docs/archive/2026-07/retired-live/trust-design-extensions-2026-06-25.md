---
doc_type: archive
status: archived
owner: founder / engineering
created: 2026-07-09
archived: 2026-07-09
why_new: Move reviewed completed evidence out of the living documentation tree without deleting its historical record.
---

# Trust Design Extensions — Phase 2 Board Brief

> Archived from the living documentation tree on 2026-07-09 during Phase 5 cleanup.

**Date:** 2026-06-25
**Parent canon:** `design-trip4/project/Vesper Trust & Controls System.html` + `trust-kit.jsx`
**Status:** Phase 3 implemented in app (2026-06-25) — blocks 08–10 match `Downloads/vesper/project/Vesper Trust & Controls System.html`.

---

## Why this doc exists

The Trust & Controls HTML board covers blocks **01–07** (Profile, Account, Privacy, Notifications, Trip controls, Data receipt, Ledger language). Four live app surfaces sit **outside** that board and still use legacy register (Card, metrics, or split IA). This brief is the Claude Design / Figma extension spec.

**Out of scope here (separate boards):**

- Travel DNA portrait → `atlas-dna-final.jsx`
- Atlas archive (map, timeline, postcards) → `Atlas Home.html`
- Ledger tier polish (voice logs, narration history) → optional future **Ledger System** board

---

## Claude Design prompt (one board extension — copy this)

```
Extend design-trip4/project/Vesper Trust & Controls System.html (blocks 01–07 already shipped).
Build on trust-kit.jsx and trust-screens.jsx — same warm paper (#EAE3D5), Stamp/Zone/Row/Receipt/
ReceiptRow primitives, EB Garamond + DM Sans + JetBrains Mono. Add three new blocks below block 06:

08 · Memory receipt — What Vesper thinks it knows (distinct from block 06 Data receipt, which is
the audit log of data *uses*). Entry: Privacy → "Full memory receipt". NO metric strip (no
Artifacts/Signals/Hidden chips). POPULATED + EMPTY phone frames. POPULATED: stamped zones
CURRENT READ (2–3 serif quotes), TASTE MATERIAL (flat ReceiptRow lines with provenance, e.g.
"Slow mornings · From Lisbon week · high confidence"), LINKS (two chevron rows: Travel DNA,
Data receipt). EMPTY: honest cold-start prose, no fabricated signals.

09 · Declared constraints — Sacred hard prefs Vesper always respects. Entry: Travel DNA → EDIT.
Three stamped zones on paper (no white iOS cards): HARD CONSTRAINTS (allergies with alert glyph,
accessibility needs, language chips with add/remove), WHAT THE CONCIERGE LEARNED (namespace
groups, hairline rows, × to forget a fact, optional "low confidence"), CONCIERGE MEMORY (one
destructive row: reset learned prefs; footnote that full export lives on Account). POPULATED frame.

10 · Your people — Resolve companions vs following in one IA. Prefer Option A: single Companions
screen with COMPANIONS zone (TrustRow per co-traveler, trip frequency) + SOCIAL zone (Following
& activity — either chevron to sub-screen or inline expansion with quiet Follow/Following pills
and activity as small Receipt slips with olive dot). Also show EMPTY frame. No loud CTAs.

Do NOT redesign blocks 01–07. Do NOT touch Travel DNA portrait (atlas-dna-final.jsx is separate).
Output: append blocks 08–10 to the existing HTML board in the same visual language as 01–06.
```

The per-block notes below are reference detail for engineering after sign-off.

---

## Extension block 08 — Memory receipt

**App route:** `/atlas/receipt`
**Entry:** Privacy → THE RECORD → "Full memory receipt"
**Problem today:** Uses `AtlasNativeMetric` strip + chip pills. Trust canon says **prose and line rows, not metrics**.

### Frame variants to design

| Variant | Content |
|---------|---------|
| **POPULATED** | Current read (1–3 serif quotes), taste signals as `ReceiptRow`-style lines with provenance, forgotten/disputed counts in prose footer |
| **EMPTY** | Honest cold-start copy — no fabricated signals |
| **ERROR** | Already implemented; keep ErrorState pattern |

### Layout rules (match block 06 + kit)

- `AtlasNativeScaffold` eyebrow: `ATLAS · RECEIPT` / title: `Memory receipt.`
- **No metric chips** (Artifacts / Signals / Hidden)
- Sections: `Stamp` headers — `CURRENT READ` · `TASTE MATERIAL` · `LINKS`
- Rows: line-by-line, each with title + muted provenance (e.g. "From Lisbon week · high confidence")
- Footer rows (not cards): Travel DNA → `/atlas/dna`, Data receipt → `/atlas/data-receipt`
- Contest affordance: per-signal "Not quite" → concierge seed (lives on DNA dimension pages, not here)

---

## Extension block 09 — Declared constraints

**App route:** `/atlas/constraints`
**Entry:** Travel DNA → declared prefs line → EDIT
**Problem today:** `Card` + `SectionTitle` + chip pills + `SettingsList` — not trust ledger language.

### Sections to frame

1. **HARD CONSTRAINTS** — Allergies · Accessibility · Languages
   - Each: list of values with quiet remove (×), ghost "Add …" action
   - Footnote: "Sacred — never shared with your group"
2. **WHAT THE CONCIERGE LEARNED** — Namespace groups (Food, Travel, …)
   - Each fact: value + key + optional "low confidence"
   - Retire (×) per row — not a form editor
3. **CONCIERGE MEMORY** — Single destructive row: Reset what the Concierge knows
   - Copy points to Account for full data export (no duplicate download)

---

## Extension block 10 — Companions & following

**App routes:** `/atlas/companions` (read-only frequency) · `/atlas/following` (follow graph + activity)
**Problem today:** Two screens, one concept; Following still uses legacy Card rows internally.

### IA decision (pick one in design)

| Option | Description |
|--------|-------------|
| **A — Nested (recommended)** | Companions is canonical; "Following & activity" section expands inline or pushes a sheet with follow toggles + activity feed |
| **B — Tabbed** | Single screen, segments: Companions \| Following |
| **C — Keep split** | Two screens but both fully on Trust kit (TrustRow list + follow as value pill / toggle) |

### Frame variants

- **WITH COMPANIONS** — 3 people, trip counts, initials in profile style
- **WITH ACTIVITY** — "What's happening" receipt slips + Everyone list with Follow/Following pills
- **EMPTY** — matches EmptyStateArt people motif

---

## Extension block 11 — DNA dimension dispute (optional, separate board)

**App route:** `/atlas/dna-dimension/[key]`
**Status:** Engineering has "Sounds right" / "Not quite" → concierge seed. Visual is bespoke DNA register, not Trust kit.

### Design ask

- Confirm contest affordance matches `atlas-dna-final.jsx` dimension pages
- If not: add dispute chip row to dimension page frame (not full Trust migration)

---

## Implementation order (Phase 3 — after design sign-off)

1. Memory receipt — highest visibility from Privacy
2. Constraints editor — sacred prefs, blocks concierge safety
3. Companions/following — after IA decision
4. Trip settings shell — `AtlasNativeScaffold` or trip-scoped header variant (block 05 polish)
5. Ledger tier — only if product wants parity with Trust polish

---

## Engineering ↔ design checklist

| Surface | Engineering (done) | Design (pending) | Polish (pending) |
|---------|-------------------|------------------|------------------|
| Profile | ✅ Trust kit, live delegation | — | — |
| Account | ✅ + live delegation summary | — | — |
| Privacy | ✅ | — | — |
| Notifications | ✅ | Pause-all row style? | minor |
| Data receipt | ✅ | — | — |
| Delegation | ✅ TrustSegmented | — | — |
| Memory receipt | ✅ link fix only | **Block 08** | TrustReceiptRow |
| Constraints | ✅ scaffold, export deduped | **Block 09** | Trust kit interior |
| Following | ✅ scaffold | **Block 10** | Trust kit interior |
| Companions | ✅ partial | **Block 10** | merge IA |
| Trip settings | ✅ Trust kit + `AtlasNativeScaffold` | — | — |

---

## File references

```
design-trip4/project/Vesper Trust & Controls System.html  # parent board
design-trip4/project/trust-kit.jsx                        # tokens + primitives
design-trip4/project/trust-screens.jsx                    # blocks 01–06
design-trip4/project/atlas-dna-final.jsx                  # DNA (separate)

travel-app/app/atlas/receipt.tsx
travel-app/app/atlas/constraints.tsx
travel-app/app/atlas/companions.tsx
travel-app/app/atlas/following.tsx
travel-app/components/trust/TrustControlsKit.tsx
```
