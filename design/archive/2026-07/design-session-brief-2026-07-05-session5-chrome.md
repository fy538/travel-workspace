# Vesper Design Canon — Session 5 Brief: The Between-Pages Layer (2026-07-05)

Scope: five items, all in the layer the canon never claimed — global chrome and cross-surface bands. A post-anchor audit found every *page* has an owner but nothing *between* pages does. All five surfaces ALREADY EXIST in production code; content models below are extracted from the live components and are constraints, not suggestions.

Standing rules:
- Governance first: add a row to 06b (or 02d where it's an ownership call) in `Vesper Canon Consolidation & Ownership.html` for each item, flip to DRAWN as it lands.
- 393×852 phone frames · `design-system.jsx` tokens · State System components for states · Interaction Surfaces primitives for sheet/dialog chrome.
- Stop after these five and export.

---

## 1. OrganizerInviteNudge (owner: Chat — cross-referenced from People & Collaboration)

The in-chat invite moment — the code's own header calls it "the second half of the wedge." Real behavior: when a trip has enough substance to invite around but the organizer is still its only member, a **slim dismissable banner** appears at the top of trip chat offering **one-tap share** (mints the invite link and opens the OS share sheet). Dismiss is session-scoped per trip (it can return next session). Visibility gate: solo organizer + a real exchange has happened.

Draw (3 frames on one board):
- **1a. The nudge in place** — group-chat-shaped thread with only the organizer + Vesper, nudge banner at top. This is a warm invitation moment, not a growth-hack toast — one italic Vesper-voice line is appropriate here (this is THE wedge moment; give it the voice).
- **1b. Pending state** — after tap, while the link mints ("one-tap share" in flight).
- **1c. The moment it should NOT appear** — same thread with 2+ members (banner absent), as a suppression frame so implementers see the gate.

## 2. Global Chrome — FloatingTabBar (owner: NEW small companion page, "Vesper Global Chrome")

The floating bottom nav is real, distinctive, and unowned. Real behavior from `components/nav/FloatingTabBar.tsx`: a floating parchment pill, 14px from screen edges, that **collapses to a single circular icon showing the active tab on scroll down, and expands back to the full pill on tap** (Reddit-style). Expanded: all 4 tabs, icon + label. Every scroll screen reserves bottom inset via a shared contract (`useFloatingNavInset`).

Draw:
- **2a. Expanded pill** — 4 tabs (Trips · Vesper · Discover · Atlas), active state treatment.
- **2b. Collapsed circle** — single active-tab icon, mid-scroll context.
- **2c. The transition** — a 3-step strip (expanded → collapsing → collapsed) so motion intent is explicit.
- **2d. Rules board (prose)** — show/hide matrix: which routes hide the bar entirely (Itinerary canon already rules no-tab-bar on the plan workspace — consolidate that ruling here), inset contract note, badge/unread policy (decide: does the pill ever carry a badge? recommend NO — Notifications owns unread awareness; record the decision either way).

## 3. ConsequenceBanner — the cross-surface "Vesper acted" class (owner: Interaction Surfaces)

Code reality: a persistent, dismissable banner (sparkles icon + title + close) that a context can address to any of six surfaces (`atlas / discover / plan / trip_memory / trips_home / vesper_home`) with kinds including `atlas_memory / capture / plan / trust / proposal / save`. It is the visible face of plan-audit/undo — how the user learns Vesper did something while they were elsewhere. The canon currently designs only the itinerary-scoped **fading receipt toast**; this is the persistent sibling.

Draw:
- **3a. The banner anatomy** — one canonical form: sparkles glyph, one-line title, optional Undo action, dismiss. Two kind examples with real flavor (e.g. plan: "Moved dinner to 8:00 — the museum ran long" with Undo; trust/memory: "Remembered you prefer window seats" with See why).
- **3b. In-context trio** — the same banner sitting on Trips Home, Discover, and Vesper Home (three mini-frames), showing placement (below header, above content) per surface.
- **3c. Two-tier rule (prose)** — define the system: **fading receipt toast** = you watched it happen (itinerary, already canon); **persistent ConsequenceBanner** = it happened while you were away; banner clears on dismiss or on visiting the acted-on surface. Record which kinds may carry Undo.

## 4. Narration arrival band (owner: Chat — new "chat chrome band" section)

Four real banners stack above the concierge chat list today, with no design governing them. Real components + copy:
- **GeofenceBanner** — "You're near {entityName}" + Hear action (pending state: "Hearing…"), dismissable. Fires from geofence context when narration has something nearby.
- **LiveCompanionBanner** — active voice-guide arc: title + subtitle (stop count), **End** action ("Ending…" pending).
- **NarrationLeaseConflict** — narration is claimed by another device/member (display-name lookup with generic fallback copy).
- **Inline location-permission strip** — Enable / Dismiss, when geofencing lacks permission.

Draw:
- **4a. Each banner** as a component row (4 rows, one board) — canonical form for each, DM Sans productive register (these are operational, not editorial).
- **4b. Stack discipline** — one frame showing the worst case (companion active + geofence hit simultaneously) and the rule: **max 2 visible, priority order companion > lease conflict > geofence > permission**; excess collapses into the top banner's subtitle or is deferred. (Recommended rule — adjust if you disagree, but record whatever you choose.)
- **4c. Placement** — where the band sits relative to chat header and thread (one context frame). Note: narration SHIPS in v1 (only live-mic is voice-flagged), so this band is v1-real, not dark.

## 5. Session-expiry recovery (owner: State System — new SessionRecovery component)

Code reality: the token layer already does silent single-flight refresh with retry-once — the soft path is invisible by design and needs NO artboard. The gap is the **hard lapse**: refresh fails and the user is bounced to sign-in with no designed moment. Requirements: it must feel like a pause, not an ejection.

Draw:
- **5a. SessionRecovery interstitial** — full-screen State System treatment: calm statement ("You've been signed out — sign back in and you'll be right where you were"), single sign-in CTA, no error-red (this is routine, not a failure). One italic voice line permitted.
- **5b. Post-recovery return** — small frame or prose rule: after sign-in, return to the interrupted screen (not home), with a StaleNotice if content refreshed underneath; if edits were queued offline, the existing queued-edits pattern applies (reference State System's offline/sync board, don't redraw).
- Record in governance: soft path (silent refresh) intentionally has no surface; SessionRecovery is the only designed moment.

## Definition of done

Five governance rows added + flipped · new "Vesper Global Chrome" companion page exists and is listed in the Canon Index · Chat page gains the nudge + chrome band sections · Interaction Surfaces gains the banner class · State System gains SessionRecovery · export a fresh handoff.
