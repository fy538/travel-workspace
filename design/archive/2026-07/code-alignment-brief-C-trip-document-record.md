# Code Alignment — Batch C: Trip Document Record Layer + Plan States (2026-07-05)

Repo: `~/travel-workspace/travel-app`. Canon: `~/travel-workspace/design/vesper-canon-anchor/project/` (read-only). Same standing rules (git status, snap rule, commit-per-task, tests, no push). This batch restores the "record" half of the Trip Document thesis — the biggest structural fidelity gap found in the module audit.

## Task C1 — Margin stream: facet stream → chronological change ledger
Canon: `trip-document-canon.jsx` → `MItem`/`MVItem` (~1135-1372): the margin stream is a chronological record of changes — swap, vote, conflict, booking, lazy-consensus, ready, reaction, applied — each a dated margin entry. Code: `TripFolioHome.tsx` → `AlsoMovingStream` (~1568) is facet-based (topical), with no applied/revert entries. Build: convert (or augment) the margin stream into the change ledger per canon — entries sourced from the same plan_events data that powers the Changes timeline (the append-only ledger exists backend-side; this is a read-model + rendering task). Keep it subordinate to the document (margin register, not a second Changes screen).

## Task C2 — Three missing attention-card faces
Canon: `trip-document-canon.jsx` → `ATTN_CARDS` (~1785): 8 card types, one card grammar. Code covers swap/vote/clash/booking via hero evidence + ReadinessRows; **LAZY-CONSENSUS, REACTION (pulse), APPLIED (record)** fall through `TripActiveFeedStrip` (~3332) as generic title/subtitle rows. Build the three faces per the canon card grammar.

## Task C3 — ReviewStack group-decision variant
Canon: `itinerary-canon.jsx` → `ReviewStackGroupDecision` (~1731). Code: `components/trip-plan/ReviewStackSheet.tsx` has only in-progress + done (~81-117). Build the group-decision variant (members' votes visible in the stack resolution flow).

## Task C4 — ChangeStudio loading + no-suggestions states
Canon: `itinerary-canon.jsx` (~1643, 1670) draws explicit loading and no-suggestions states for Change Studio. Code: `ChangeStudioSheet.tsx` has no distinct designed states for these. Build both per canon (compose from the app's existing state components — they mirror State System).

## Task C5 — Dead art-direction variant cleanup
Code keeps two art directions live in `TripFolioHome.tsx` (~770-864): `Dir6LiveFacets` vs `Dir7Stamp`/`Dir7LiveFacets`. The canon unified document picked one. Determine which direction the canon lifecycle phones match, delete the dead variant, and note the choice in the commit message.

## Done
Five commits · margin stream reads as a dated change ledger · all 8 attention faces render · group-decision review + ChangeStudio states exist · one art direction remains · report token mismatches + any backend read-model work flagged.
