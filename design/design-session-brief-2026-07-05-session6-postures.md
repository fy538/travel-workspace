# Vesper Design Canon — Session 6 Brief: Postures, Lifecycle, Adjudications (2026-07-05)

Scope: five items — the last substantive design session before pure alignment work. Items 1–3 are drawing; items 4–5 are adjudications with small drawing tails. Two of the five require a product decision — recommendations are stated; override in-session if you disagree, but RECORD whichever way you rule.

Standing rules:
- Governance first (rows in 02d/06b of `Vesper Canon Consolidation & Ownership.html`, flip as landed) · 393×852 frames · `design-system.jsx` tokens — NO new local palettes (session 5's Global Chrome page forked a `GC` palette; do not repeat that) · State System components for states · stop after five and export.

---

## 1. Solo posture — one owning statement (owner: NEW section on Trip Document, cross-referenced from Chat, Itinerary, Notifications)

Solo trips are currently designed as scattered per-page variants (Costs has a solo split, Changes has a solo timeline state, Trust has role variants) but no page owns the posture end-to-end. Code reality: the folio cover already renders **"just you"** for a party of one; chat detects `isSoloOrganizer` (it gates the invite nudge); but **plan/vote affordances have zero solo handling** — vote chips would render for a party of one.

Draw one "Solo posture" board (owner: Trip Document, since the trip is the scope):
- **1a. Solo folio frame** — cover with "just you", no member roster row, needs-you hero without waiting-on-N framing.
- **1b. Solo plan rule** — one frame or annotated row: vote affordances SUPPRESSED for party of one; decisions are direct edits (Changes' solo state already establishes this — reference it, don't redraw).
- **1c. Solo chat rule (prose)** — a solo trip's chat is a private trip-linked Vesper thread wearing no group chrome (no member bubbles, no privacy seam), with the invite nudge as the only group-facing element. Record: joining of a second member PROMOTES the thread to the group room (one-line rule; the promotion moment itself can ride the existing invite-accept flow).
- **1d. Solo notifications rule (prose)** — no vote/consensus notification types for solo trips; list which of the 20 types are suppressed.

## 2. Account lifecycle cosmetics (owner: Trust & Controls)

Code is already App-Store-compliant (real cascading deletion, DSAR export, Clerk delete + sign-out). Three small canon gaps:
- **2a. Post-deletion goodbye state** — one frame: after delete completes, a calm terminal screen (account gone, what was removed in one line, door to sign-up). No error styling; this is a dignified exit. One italic voice line appropriate ("It was a pleasure traveling with you.").
- **2b. Sign-out confirm** — code has a confirm sheet; canon has only the row. Draw the confirm moment (Interaction Surfaces confirm pattern — NOT the destructive typed-confirm; signing out is routine).
- **2c. Export copy fix** — canon's Account screen says the data export is "emailed to you"; code actually produces a share-sheet JSON bundle on-device. Fix the canon copy to match reality ("Prepared on this device — save or share it wherever you like").

## 3. "Ask the organizer" — the 403 recovery pattern (owner: Interaction Surfaces)

Role matrices exist everywhere (who CAN'T do what) but there is no designed moment for the blocked attempt itself. Draw one pattern board:
- **3a. Inline blocked-action treatment** — a member taps an organizer-only control (e.g. changing trip dates): the control doesn't error; it explains ("Only Maya can change dates") with a one-tap **Ask** affordance that drops a pre-written request into the group chat ("Ben would like to move the dates — @Maya").
- **3b. The three intensities (prose rule)** — locked-invisible (member never sees the control: preferred for destructive actions) · locked-visible-explained (this pattern) · request-flow (Ask). Record which trip-settings controls use which intensity, referencing Trip Settings & Admin's role matrix.

## 4. ADJUDICATION — Quiet mode (canon has it, code deleted it)

Canon: full QuietModeBoard (vesper-home-quiet.jsx) + `whisper` voice register. Code: FocusHome.tsx documents the deliberate removal of the moon toggle and whisper branch; whisper is dead code in the type union.

**Recommendation: KILL from canon.** The code removal was a deliberate simplification; quiet mode is attention-pressure medicine for a product that doesn't yet have attention-pressure users. Archive the QuietModeBoard (appendix, do-not-implement note), remove `whisper` from the canonical register list (leaving 5), and record in governance: "Quiet mode removed from v1 canon 2026-07-05; revisit post-dogfood if home noise becomes real." If you rule the other way (rebuild in code), record it as an alignment build item instead — but do not leave the canon and code contradicting each other.

## 5. ADJUDICATION + small draw — Deck & home-state taxonomy reconciliation (owner: Home)

Two mismatches between the Home canon and code:
- **Deck faces**: canon has 11; code has 6 structured (vote/settle/pick/call/brief/readiness) — but code's `readiness` face isn't in the canon 11, and canon's Flight/Proposal/Comparison aren't in code (they fall back to prose — already logged as alignment build items).
- **Home states**: canon boards say Planning/Calm/Urgent/On-trip/Post-trip/Cold/Single/Juggling; code's FocusState kinds are urgent/dispatch/imminent/prepared/signal/capture/resume/starter.

Do:
- **5a. Draw the `readiness` deck face** — it ships today with no canon artboard. One dark deck frame in the existing 11-card board's style, making it the official 12th face.
- **5b. Taxonomy mapping board (prose)** — one table: each code FocusState kind → which canon home-state board governs its look. Where canon boards have no code branch (Calm, Single-item, Juggling), rule each one: keep-as-build-intent (add to alignment backlog) or trim from canon. Recommendation: keep **Single-item** (rail collapse is real polish, cheap), keep **Calm** (it's the queue-empty vibe — code's `starter`/`prepared` likely maps to it; verify in the table), trim **Juggling** to a note (cross-trip tagged rail is post-dogfood).
- Record the ruling for each in governance so the alignment pass has one authoritative list.

## Definition of done

Five governance rows landed · solo posture has one owning board · Trust & Controls gains goodbye/sign-out/export-copy · Interaction Surfaces gains the blocked-action pattern · quiet-mode contradiction resolved ONE way · deck is officially 12 faces with a state-mapping table · export a fresh handoff.
