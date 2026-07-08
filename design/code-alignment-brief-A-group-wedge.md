# Code Alignment — Batch A: Group-Wedge Surfaces (2026-07-05)

Repo: `~/travel-workspace/travel-app`. Design canon: `~/travel-workspace/design/vesper-canon-anchor/project/` (read-only mirror of handoff 97 — implement FROM it, never edit it). This batch closes every design-ahead gap on the group/invite wedge path — the product's load-bearing bet.

## Standing rules (all batches)
1. `git status` first; other sessions may have WIP — branch from main, don't touch unrelated WIP.
2. **Snap rule:** match the canon's layout/structure/copy intent exactly, but snap every color/size/font value to the app's existing tokens (26 font roles, color budget). Never copy raw hex/px from canon jsx. If a canon value has no token, flag it in your report instead of inventing one.
3. One commit per task; typecheck + tests green after each; grep for dangling references; update FEATURE.md docs touched (pre-push doc-sync guards). Do NOT push without user approval.

## Task A1 — Trips Home: planning-SHARED group posture
Canon: `trips-home-canon-screens.jsx` → `V2Group` (~line 164): the group-trip hero variant — "Lisbon table" overlay with member avatars and a DECISIONS vote hero. Code: `components/trips/TripsHomeModel.ts` has one `'planning'` HeroKind; no member-avatar group variant exists in TripsHomeCards/TripHeroCard. Build: when the highest-ranked planning trip has ≥2 members, the hero renders the group variant (avatar stack + open-decision framing). Reuse the existing `AvatarStack`.

## Task A2 — Trips Home: "See all N trips →" footer
Canon: `trips-home-canon.jsx` → `TripsFooter` (~line 127). Code: `/trips/all` route exists but is not linked from the home scroll. Build: the footer door at the end of the trips home scroll, count-aware, navigating to `/trips/all`.

## Task A3 — GroupAgencySheet: member view + dirty-dismiss
Canon: `group-agency-board.jsx` — 5 artboards; code (`components/chat/GroupAgencySheet.tsx`) implements only the organizer sheet. Build per canon 1c + 1e: (a) member (non-organizer) view — "Mute Vesper for me" active; mode/threshold read-only with "ask the organizer" affordance; memory rows show Forget only for items about the viewing member; (b) dirty-dismiss confirm on unsaved memory edits (canon frame exists; verify code's "Discard memory edits?" flow matches its layout). Recorded default for new groups: Proactive · Medium — verify code's default matches; fix if not.

## Task A4 — Solo suppression (plan + notifications)
Canon: `solo-posture.jsx` on Trip Document — "SUPPRESSED — PARTY OF 1". Code: `components/trip-plan/*` has zero solo handling. Build: (a) vote affordances suppressed when `trip.travelers.length <= 1` (decisions become direct edits, matching the Changes solo state); (b) backend/FE notification suppression for the vote/consensus types the canon board enumerates (check `solo-posture.jsx` for the exact list) — if suppression belongs backend-side, flag it for the travel-agent repo in your report rather than hacking it FE-side.

## Task A5 — OrganizerInviteNudge: voice-line alignment
Canon: `chat-invite-nudge.jsx` — the nudge carries one italic Vesper-voice line (this is the wedge moment; hospitality register, not growth-hack). Code: `components/chat/OrganizerInviteNudge.tsx`. Align copy/typography to the canon frame (italic serif = the app's Vesper-voice text style token).

## Done
Five commits · group hero renders for ≥2-member trips · footer wired · agency sheet has both role views + dirty-dismiss · party-of-one shows no vote chrome · nudge reads in Vesper's voice · report lists any canon values that had no token match and any backend work flagged.
