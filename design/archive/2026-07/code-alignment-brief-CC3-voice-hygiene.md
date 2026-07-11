# Code Alignment — Batch CC3: Voice-Register Hygiene (2026-07-09)

Repo: `~/travel-workspace/travel-app`. Canon mirror: `~/travel-workspace/design/vesper-canon-anchor/project/` (handoff 125, read-only). Ledger: `design/component-consistency-audit-2026-07-09.md`, family **voice-registers**. Core is healthy (5 registers, Whisper killed, `VesperSignature` shared). This batch enforces the **law: italic serif = Vesper voice ONLY.** The frays are faux-italic sans leaking onto UI status text, and Vesper's genuine voice losing its serif face.

## Blocked-until
- **Tasks CC3.3 (dismissal register) depends on D9; CC3.4 (costs voice lines) depends on D10; the glyph pick in CC3.5 depends on D8.** Everything else is unblocked. Start CC3.1/CC3.2.

## Standing rules
Same as CC1. Extra: when you touch a text style, confirm the target token is the real Vesper-voice serif-italic token (not a faux-`fontStyle: 'italic'` on DM Sans, which doesn't even have an italic cut — it renders as synthetic slant).

## Task CC3.1 — Purge faux-italic sans from status text  ·  severity HIGH
Canon: italic = Vesper voice only; status/UI text is DM Sans roman. Code applies `fontStyle: 'italic'` to DM Sans (no italic cut → ugly synthetic slant) on non-voice status text across chat, proposals, changes, plan. Grep `fontStyle: 'italic'` app-wide; for each hit decide: is this Vesper *speaking* (→ convert to the serif-italic voice token) or is it UI status (→ drop italic, use roman). The E5 ruling (TrustControlsKit `TrustContract`) is the precedent; generalize it. Report the full list with your roman/serif call per site.

## Task CC3.2 — Markdown `*em*` must keep the serif face inside Vesper prose  ·  severity HIGH
Canon: within Vesper's serif chat prose, emphasis stays in-face (serif italic), not sans. Code: the serif markdown variant is correct in some places but the em maps to DM Sans in others. **Careful — the audit overstated this:** `GroupVesperNote.tsx:187-189` is the *compact* (DM Sans body) variant and is correct as-is; its serif variant at `:152-154` already maps em right. Fix only the genuine serif-prose paths where em drops to sans. Verify against `chat-narration-band.jsx` / `vesper-chat-canon.jsx`.

## Task CC3.3 — Changes masthead voice line  ·  severity MEDIUM  ·  partial-blocked D9
Canon: the Changes masthead's Vesper-voice line renders in the serif voice token. Code (`app/.../changes.tsx:116-126`): `summaryLine` is mostly mechanical count chrome ("3 changes recently · 1 needs your vote") set in faux-italic sans — only the **empty-state string** is genuine Vesper voice. Split them: count chrome → roman sans; empty-state voice line → serif voice token. (The dismissal-vs-navigational register question is D9 — if D9 lands first, apply it here too.)

## Task CC3.4 — VesperSignature adoption  ·  severity MEDIUM
Canon: one shared attribution primitive. Code: `VesperSignature` has 13 adopters but 5 surfaces hand-roll attribution eyebrows. Migrate the genuine drift sites onto `VesperSignature`. **Exception the audit confirmed:** `TripHeroCard`'s eyebrow faithfully implements its OWN canon board (`far-hero-kit.jsx:86-97` `VesperEyebrow`) — leave it. Fix the other four; list them in your report.

## Task CC3.5 — One Vesper glyph  ·  severity MEDIUM  ·  BLOCKED on D8
Once D8 picks the one true mark: port canon's chosen glyph (spark SVG or plus) into `components/brand/`, replace the ~four code variants (custom SVG + Ionicons `sparkles`/`sparkles-outline` across ~36 files) with it. Until D8 lands, do NOT touch glyphs — you'd just create a fifth variant.

## Task CC3.6 — Costs populated-state voice lines  ·  severity — · BLOCKED on D10
Once D10 answers whether the ≤1-voice-line budget applies to populated costs states: either bless the three code sites or convert them to roman. No action until the ruling.

## Done
No faux-italic sans on status text · em keeps serif in Vesper prose · Changes masthead splits chrome from voice · attribution on VesperSignature (TripHeroCard exempt) · (post-handoff) one glyph, costs voice resolved · report lists every `fontStyle: italic` site with its roman/serif disposition.
