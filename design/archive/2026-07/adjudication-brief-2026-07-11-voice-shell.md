# Claude Design Adjudication Brief — Voice live-mic shell (2026-07-11)

**For:** the human, working in Claude Design (claude.ai/design), canon project `Vesper` @ handoff 134.
**Source:** zero-trust re-audit Wave 2 (`design/reaudit-2026-07-open-findings.md`, Voice row) — spot-verified against `vesper-home-voice.jsx`, `VoiceOverlay.tsx`, `useVoiceSession.ts`, `MicPrivacyDisclosure.tsx`.
**How to use this:** one decision, not a task list. Pick one direction; don't split the difference. If canon changes, regenerate the specimen in the same session.

---

## D24 — Full-screen "Calm Listening" vs shipped bottom-sheet voice shell

**Conflict:** canon (`vesper-home-voice.jsx`) specifies a full-screen dark takeover — tap/hold gesture split, amber/gold accents, three entry points via `vesper-modes.jsx`. Code ships `VoiceOverlay.tsx`: a slide-up bottom-sheet LiveKit modal, no hold-to-talk, **purple** on `VoiceOrb` / sheet chrome (violates the app's own color doctrine: purple = legacy agent-presence only).

**This isn't drift from neglect.** `VoiceOverlay` documents an explicit H2-5 "sanctioned bespoke" rationale in-file. `VOICE_ENABLED` defaults off; narration text path ships; live mic stays dark behind credential + process gates. The sheet is a deliberate MVP shell that was never reconciled with the Calm Listening specimen.

**Evidence (code, 2026-07-11):**
- `travel-app/components/voice/VoiceOverlay.tsx` — Modal + bottom sheet, not full-screen takeover
- `travel-app/components/voice/VoiceOrb.tsx` — `colors.purple[200/400]`
- `travel-app/hooks/useVoiceSession.ts` — throws when real API has no native connector (no longer a silent no-op); mock stays at `ready_to_connect`
- `travel-app/hooks/useNarrationWithInterruption.ts` — ~1000-line-tested hook, **zero production callers**
- `travel-app/components/voice/MicPrivacyDisclosure.tsx` — copy promises interruption flow + status indicator for unwired behavior
- `MicStatusIndicator` — **deleted** (was dead code); disclosure still references the affordance class

**Decide:** one of two directions —

1. **Canon owes code (carve-out).** Bless the bottom-sheet shell as v1 live-mic chrome. Mandate **amber/gold only** (retire purple on voice surfaces). Narrow `MicPrivacyDisclosure` to what ships today (no interruption / no status-indicator promise until wired). Hold-to-talk and full-screen takeover explicitly deferred — document in `vesper-home-voice.jsx` as post-v1. Regenerate specimen with a "shipped shell" panel showing the sheet, not the takeover.
2. **Code owes canon.** Full-screen Calm Listening becomes the v1 target before further LiveKit investment. Bottom sheet is throwaway — migrate `VoiceOverlay` to takeover layout, implement tap/hold gesture split, amber register, and wire `useNarrationWithInterruption` end-to-end (or cut interruption from v1 scope explicitly in canon). This is the larger lift.

**Regenerate:** if (1), add a **VOICE SHELL CARVE-OUT (D24)** paragraph to `vesper-home-voice.jsx` naming the bottom sheet, deferring takeover + hold-to-talk, and banning purple on voice chrome. If (2), mark the bottom-sheet panels in the specimen as **SUPERSEDED — convert to takeover** and add a comment block listing the code files that must migrate.

---

## Smaller, related — no design decision needed (blocked or mechanical)

- **LiveKit wiring:** `docs/VOICE_NATIVE_WIRING.md` + `configureVoiceRoomConnector()` — execution gap, not a shell question. Un-darking live mic can proceed under either D24 ruling once color + disclosure honesty are settled.
- **Interruption stack:** if ruling (1), either narrow disclosure copy **or** wire `useNarrationWithInterruption` — product chooses depth, not glyph shape.
- **Entry points:** canon lists three (`vesper-modes.jsx`); code gates composer mic only behind `VOICE_ENABLED`. Mechanical follow-up once shell is ruled.

---

## After you re-export

Run `python3 scripts/canon-drift-check.py`; update `design/surface-manifest.yaml` Voice row status/notes with the ruling.
