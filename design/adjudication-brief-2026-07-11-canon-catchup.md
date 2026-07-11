# Claude Design Adjudication Brief — Canon Catch-Up (2026-07-11)

**For:** the human, working in Claude Design (claude.ai/design), canon project `Vesper` @ handoff 131.
**Source:** the "close all action items" campaign (Batches A–H, 2026-07-10) that closed out `code-alignment-brief-CC1..CC4` plus a fresh chat-surface audit backend fix (the message Report action). Confirmed against handoff 131 (2026-07-10 17:21) that none of the six items below are already addressed — 131 is a different, unrelated initiative (BackboneBand + PlanReadyReceipt, "canon 130").

**How to use this:** each item is a decision, not a task. Several are cases where **code made a deliberate, reasoned, already-shipped choice that canon doesn't reflect** — these aren't code bugs waiting on a canon ruling to fix, they're canon that's stale against a real product decision. Where that's the case it's called out explicitly so you're not re-litigating something already settled, just recording it. Others are genuine open questions. As always: when you adjudicate a page, regenerate its specimen `.jsx` in the same session — a ruling that isn't mirrored in the specimen is how canon drifts again.

**Not in this brief:** the group-thread privacy-seam divider (`people-collab-app.jsx:213-220` `PrivateSeam`) has a clear, small, already-correct canon spec — it just needs building in code, no decision required. Left off this list on purpose.

---

## D17 — Offline chat send: canon's queue vs. code's shipped "refuse with notice"

**Conflict:** canon specifies queue-and-send-later for offline composer sends — `vesper-chat-canon.jsx:1727` ("Offline: save draft locally, queue send, show QUEUED badge in composer"), `:1555-1560` (loading/failed/offline board: "message will send when connected"), `:1086-1094` (thread state: "showing cached thread / changes will send when reconnected"). Code does none of this — `ComposerBar.tsx:336-341` hard-refuses the send with an error toast the instant the device is offline, and there's no local draft persistence, no queue, no badge.

**This isn't a gap code owes canon — it's the opposite.** The refuse-immediately shape is a deliberate, already-audited, **app-wide** architecture (`hooks/useNetworkState.ts`'s `useOfflineGate`/`useGatedMutation`), adopted after a real "bad-network audit" found that firing requests while offline left users watching a full ~30s fetch timeout before failing. Every mutation surface in the app — Save, Follow, Vote, comments, chat send — uses this same gate. Building canon's queue behavior just for chat would require new infrastructure (local draft store, send queue, reconnect-triggered flush, a QUEUED badge, and reconciling all of that with chat replies being a live SSE stream, not a fire-and-forget POST) **and** would leave the app with two contradictory offline behaviors.

**Decide:** adopt "block with notice" as canon's chat-offline behavior, matching what's already shipped everywhere else in the app. (Canon's own audit trail for this finding already names this as a valid resolution — "adjudicate canon down... if queueing is out of MVP scope.")

**Regenerate:** `vesper-chat-canon.jsx`'s offline states (:1086-1094, :1555-1560, :1727) to the immediate-refusal shape; delete the QUEUED badge concept from the composer board unless a future session wants to revisit it as a real roadmap item.

---

## D18 — PlanBlockRow's rail-node overlays that canon's 7-state grammar doesn't cover

**Gap:** canon's `row-system.jsx` `TimelineRow` defines exactly 7 node states (`planned · booked · held · proposed · now · done · skipped`) plus the `conflict` overlay. Code's `PlanBlockRow.tsx` (the golden-path day-view row, freshly migrated onto this exact grammar) layers three more real signals on top that canon doesn't model: `held_for_payment` (urgent — oxblood fill + halo, a booking-payment-deadline signal distinct from a plain `held`), `expired` and `failed` booking outcomes (oxblood / amber, no halo), and an `isExperience` gold tint carved out of the `planned` state's default look. These aren't invented — they're real, pre-existing product signals (payment urgency, terminal booking failures, experience-type tagging) that predate this session's grammar migration and were deliberately kept as overlays rather than dropped, since removing them would be a real loss of information for the user.

**Decide:** should canon formally document these three overlays (with their exact tone/halo treatment) as sanctioned additions to the TimelineRow spec — not as new base states, but as a documented second layer alongside `conflict` — so a future audit doesn't re-discover them as "undocumented drift"? Alternative: rule that these signals should be dropped/simplified to fit inside the clean 7-state model exactly, and code follows up to remove them.

**Regenerate:** `row-system.jsx` `TimelineRow`'s node-state table, adding a short "overlays" note alongside the state table (mirroring how `conflict` is already documented as an overlay, not an 8th state).

---

## D19 — The `proposed` state now covers two different signals

**Context:** code had two separate "something's being decided" signals for a block — `commitment_state==='proposed'` (Vesper suggested this) and a separate `hasOpenProposal` flag (an open group vote on a change to this block). During the grammar migration this session, product decided to collapse both onto canon's single `proposed` state, trading away the visual distinction between "Vesper's own suggestion" and "the group is actively voting on a change" in favor of matching canon's clean 7-state model exactly.

**Decide:** ratify the collapse (simplest — ships as-is, no further action) — or, if that visual distinction matters enough to bring back, canon should define what the group-vote-in-progress case looks like (a variant of `proposed`, e.g. a different node fill/border, or a genuinely new 8th state) and code adds it back as a follow-up.

**Regenerate:** none needed if ratifying the collapse — just note in `row-system.jsx`'s spec comment that `proposed` is deliberately the merge point for both cases. If restoring the distinction, add the new treatment to the node-state table.

---

## D20 — The message action sheet has no canon spec at all

**Gap:** canon's only long-press ruling anywhere in the chat surface is header-title reveal (`vesper-chat-canon.jsx:1803`) — there's no spec for a per-message action sheet. Code invented one from scratch: long-press on any chat message (user or Vesper) opens a shared action sheet with **Share** (always) and **Report** (Vesper turns only, now backed by a real endpoint — `POST /api/messages/report`, shipped this session). It doesn't offer **Copy** — a real gap, since AI-authored markdown text isn't selectable in the bubble at all (a `react-native-markdown-display` limitation), so there's currently no way to copy a Vesper reply's text.

**Decide:** ratify a canon board for this action sheet — Share/Report (and ideally Copy) grammar, icon choices, destructive styling for Report, and whether user-authored turns should ever get Report too (currently: no). This is a real, live, now-fully-wired pattern (Report has a working backend behind it) that deserves a spec rather than staying an unratified invention.

**Regenerate:** a new specimen in `vesper-chat-canon.jsx` or a small standalone board — action-sheet anatomy (icon + label + subtitle per row, destructive treatment for Report), matching the shared `ActionListSheet` primitive's actual shape so the spec and the shipped component agree from day one.

---

## D21 — Sheet title size: code's 20pt vs. canon's ~16.5–17pt

**Conflict:** canon's `sheet-header.jsx` specimen and related boards spec bottom-sheet titles at roughly 16.5–17pt, weight 600–700. Code's `ui/SheetHeader.tsx` `large` size (the default, used by the majority of sheets) maps to `typography.h1` — 20pt DM Sans medium. This has been flagged at least twice this session (once during the Costs sheet-header migration, once during the row-grammar work) as a likely artifact of the app's fontSize-ratchet role ladder simply not having an exact token at canon's size, rather than a deliberate choice — but it's never been adjudicated, so every future sheet-related pass re-discovers it as an open question instead of a settled fact.

**Decide:** does 20pt get blessed as the actual shipped size (canon's title-size language updates to match), or does code need a new `typography` role at ~16.5–17pt for sheet titles specifically (and `ui/SheetHeader.tsx`'s `large`/`compact`/`display`/`displaySmall` ladder gets a token that actually hits canon's number)? This blocked at least one real migration this session (`CostsBalanceSheet`'s title+Done row couldn't cleanly adopt `SheetHeader` because no existing size variant matched its serif_semibold/17px title without a visible regression) — resolving it unblocks that and any future sheet-title consolidation.

**Regenerate:** `sheet-header.jsx` — either confirm 20pt in the title-size language, or add the missing size to the anatomy table with an exact px/weight so code has a real target.

---

## D22 — Onboarding's Fleuron marks vs. D8's "one glyph" ruling

**Context:** D8 (resolved, canon 129) picked the two-point `VesperMark` spark as the one true Vesper glyph everywhere, with all other sparkle variants retiring/aliasing to it — CC3.5 executed this across the app (19 genuine-attribution sites across 14 files converted). D8's ruling made no carve-out for onboarding. Code's `app/onboarding.tsx` still uses the separate `Fleuron` mark six times, and `components/onboarding/SeamDecline.tsx` once more — two of those seven are genuine attribution-eyebrow uses (same job VesperMark now does everywhere else), the rest are more decorative/scene-setting uses within the onboarding flow's own bespoke visual identity.

**Decide:** does onboarding get a documented, deliberate exception to D8 (its own distinct decorative register, given it's a uniquely crafted first-impression flow — not more sparkle variants accumulating by accident), or does D8's "one glyph, no exceptions" ruling stand and onboarding converts its two attribution-eyebrow uses to VesperMark like everywhere else (the four purely decorative Fleuron uses would be a separate, lower-stakes question either way)?

**Regenerate:** if blessing an exception, add a short note to `vesper-shared.jsx`'s VesperMark section naming onboarding as a documented carve-out and why. If not, no canon change needed — just flag that CC3.5 left this specific conversion undone pending this call.

---

## Priority for the design session

Recommend this order: **D17** (offline chat) and **D20** (message action sheet) first — both are code that's already shipped and stable, so canon just needs to catch up to reality, lowest risk, highest "why doesn't the spec match what's live" payoff. **D21** (sheet title size) next — it's blocking a concrete pending migration. **D18/D19** (PlanBlockRow overlays + the proposed collapse) together, since they're both about the same file/grammar and a single session can resolve both in one pass. **D22** (onboarding Fleuron) last — lowest urgency, isolated to one flow, no code is currently "wrong" either way since nothing's forcing a conversion.

---

## After you re-export
Run `python3 scripts/canon-drift-check.py` — it will flag every surface whose canon files you touched as stale, which is the signal for which code batch(es) to re-verify against the new handoff.
