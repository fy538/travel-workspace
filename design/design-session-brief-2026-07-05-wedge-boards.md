# Vesper Design Canon — Session 3 Brief: Three Wedge Boards Only (2026-07-05)

Scope: draw exactly THREE boards — group agency controls, full-screen profile, all-trips list — then flip their governance rows and stop. Do not proceed to other open items this session; a fresh handoff gets exported after these three so the wedge-critical designs are banked.

Standing rules:
- Frame width **393×852** (per the hygiene rule recorded last session).
- Snap to `design-system.jsx` tokens — no local palette forks.
- PRODUCTIVE register for all three (DM Sans-led; at most one italic Vesper-voice line per screen).
- Consume existing companions — Interaction Surfaces for sheet chrome/toggles/dialogs, People & Collaboration for avatar/people tokens, Row System for list rows, State System for any state treatment. Do not invent new primitives.
- Flip the matching 06b rows in `Vesper Canon Consolidation & Ownership.html` to DRAWN as each board lands.

Important: all three surfaces ALREADY EXIST in the production codebase. These boards canonize and elevate real screens — the content models below are extracted from the live code and are constraints, not suggestions. Design the best version of THIS model; do not substitute a different control vocabulary.

---

## BOARD 1 — Group Agency Controls (Chat page)

Owner: **Vesper Chat.html**. The codebase component is `GroupAgencySheet` (bottom sheet in the group room). Its real control model, which the design must cover:

1. **Agency mode — two-way selector: Reactive / Proactive.**
   - Reactive: Vesper only responds when spoken to in the group room.
   - Proactive: Vesper may interject on its own.
2. **Proactivity threshold (visible only when Proactive)** — three levels, real copy from code:
   - **Low** — "Vesper can help with ordinary coordination questions"
   - **Medium** — "Vesper waits for clear planning decisions or tradeoffs"
   - **High** — "Vesper only jumps in when timing looks costly"
   (Note the semantics: higher = quieter. The design should make this legible at a glance — consider a restraint scale, not a "power" scale.)
3. **Two mute switches, deliberately distinct:**
   - **"Mute Vesper for me"** — personal; the room still hears Vesper.
   - **"Mute Vesper for the room"** — affects everyone.
   The design must make the blast-radius difference unmistakable (this is a trust surface).
4. **Group memory section** — a list of things Vesper has learned that are visible to this group, each row with label + detail and a **Forget** affordance; edits are staged and there is a **"Discard memory edits?"** confirmation on dismiss with unsaved changes (Interaction Surfaces dirty-dismiss pattern).

Artboards to draw (5):
- **1a. The sheet, organizer view, Proactive selected** — full control set visible: mode selector, threshold at Medium, both mutes, group memory list (3–4 example rows with one staged forget).
- **1b. The sheet, Reactive selected** — threshold hidden/collapsed; show the collapse behavior.
- **1c. Member (non-organizer) view** — decide and draw the permission split: recommended split per trust doctrine: members get "Mute Vesper for me" + read-only view of mode/threshold + memory list with forget for items ABOUT THEM only; "Mute for the room" and mode/threshold changes are organizer-only with an "ask the organizer" affordance. If you choose a different split, record it in governance.
- **1d. Entry point** — the group chat header with the agency affordance visible (where a member finds this sheet).
- **1e. Dirty-dismiss confirm** — the "Discard memory edits?" moment, using the Interaction Surfaces destructive-confirm pattern.

Default state note for governance: new groups start **Proactive · Medium** (matches the wedge bet — Vesper demonstrating value in the group room — while Medium keeps it from being noisy).

## BOARD 2 — Full-screen `/profile/[userId]` (People & Collaboration page)

Owner: **Vesper People and Collaboration.html** (in-app screen; External Sharing keeps the signed-out shell and references this). The live screen's real content model:

- Display name + avatar token (People & Collaboration tokens).
- **Follower/following counts** ("N followers · N following").
- **FollowPill** — shown only when viewing someone else; toggles follow/unfollow.
- **"Travel taste" section** — public taste phrases (short prose lines, not chips).
- **Privacy line (real copy from code, keep it or improve it, don't drop it):** "Only public taste and shared stories appear here. Private trips, saves, and notes stay in Vesper."
- **"Shared trips" section** — ONLY trips shared with the viewer (never their full history — privacy seam doctrine); empty copy: "No shared trips yet."

Artboards to draw (4):
- **2a. Viewing another user, not following** — follow affordance prominent; rich taste + one shared trip.
- **2b. Viewing another user, following** — following state, unfollow path visible on tap/press treatment.
- **2c. Viewing self** — no FollowPill; "what others see" framing; the privacy line does double duty here as reassurance.
- **2d. Sparse/new profile** — few or no taste phrases, no shared trips: use State System InlineAbsence treatments inside the layout; do not draw a custom empty screen.

## BOARD 3 — `/trips/all` list (Trips Home page)

Owner: **Vesper Trips Home.html**, reached from the "See all N trips →" footer door. The live screen's real model (this settles the past-trips question from the session-2 brief):

- Title block: **"All trips."** + a generated subhead (e.g. "3 planning, 2 dreaming — and 4 kept behind you").
- **Planning section** — dated trips, sorted by start date. Rows from Row System shapes.
- **Dreaming section** — undated drafts.
- **Past trips are NOT listed** — they hand off to Atlas via a closing card: "Lisbon & 3 more live in [Atlas]" (the code calls this the TripsIndex past-trips card and already cites design canon for it — this board makes that citation true).
- Empty state exists in code when everything is zero, but per the recorded suppression rule a zero-trip user lands on cold Trips Home instead — draw NO empty artboard; add the suppression note to the board.

Artboards to draw (3):
- **3a. Default** — title block + Planning (3 rows, dated) + Dreaming (2 rows) + the Atlas past-trips handoff card closing the list.
- **3b. Planning-only / Dreaming-only variant** — one section absent; show how the list breathes without it (section simply omitted, no placeholder).
- **3c. Loading** — State System LoadingSkeleton in this layout.

## Definition of done

Three boards drawn on 393×852 frames · 06b rows for all three flipped to DRAWN (with the organizer/member split and Proactive·Medium default recorded under Board 1, and the Atlas past-trips handoff recorded under Board 3) · export a fresh handoff.
