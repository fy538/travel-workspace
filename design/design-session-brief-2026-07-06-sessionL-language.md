# Vesper Design Canon — Session L: Language Canon (2026-07-06)

Scope: the words layer. A fresh-eyes language audit found the visual canon strong but four naming/verb families unruled and the voice rule unwritten. Five items — mostly rulings + targeted copy edits, minimal drawing. Every ruling gets recorded on the owning page (Operations System for verbs, Canon Consolidation for names) so future copy has one source of truth.

Standing rules: governance/Ops rulings FIRST, then apply the copy edits · no visual redesign · flip a 02d row per ruling.

---

## 1. Name the trip surface once (the worst drift in the bundle)

Four names coexist: "Trip Document" (75×/20 files), "Folio" (71×/17), "trip home" (61×/20), "Single Trip Home" (19×/5) — `universal-search-app.jsx` uses two in one file (~705 vs ~756), `notifications-app.jsx` (~849) hedges "route to Trip Document / Single Trip Home."
**Ruling to record:** user-facing word = **"Trip"** (as in "Back to the trip"); canon/spec name = **"Trip Document"**; "Folio" = component-name register only (SoloFolioFrame etc. stay); retire "Single Trip Home" and "Trip Home" from all prose. Apply: fix universal-search ~705/756, notifications ~849, itinerary-canon "Back returns to Single Trip Home" lines (~1582–1867), stay/costs `<Node label="Trip Home">` (costs-screens ~318). Also record the second name pair while here: user-facing label for the itinerary surface = **"Plan"** (it's what the tab says); "Itinerary" = canon/spec name — one line in Canon Consolidation.

## 2. Verb rulings on the Operations System page (the four families it never claimed)

Add a short "Verb Canon — additions" board to the Ops page recording:
- **Add-to-trip verb = "Add to trip"** everywhere. Fix: places-canon ×7 "Add to plan", discover-detail ~325 (file has both variants), chat-canon "Add to itinerary", booking-screens-2 ~94 "Save to the plan". ("Save" stays reserved for the Saved system — its language is exemplary; don't touch.)
- **Proposal voting pair = Approve / Decline**; **"Accepted/Applied" = outcome states, never button labels.** Fix: proposal-detail ~410 ("Approve" stays) vs ~418 ("Accept & apply to Plan" → "Approve & apply to Plan"), trip-document-canon Changes card "Reject" ×6 → "Decline".
- **Undo vs Revert, one sentence:** Undo = your own immediate action (toast-scale); Revert = unwinding an applied group change (record-scale). Current usage already conforms — just write the rule.
- **Release** family: already sanctioned with conversational alternates — no change, note as settled.

## 3. Write the voice rule + fix the leaks

**Ruling (record on the Ops page and in Canon Consolidation register rules):** "The italic voice speaks as I — first person, never 'Vesper will…'. Third person is spec-register only."
Apply to the five known leaks: action-grammar-rows ~90 ("Vesper will add it" → "I'll add it" — this one is on the Ops page itself), universal-search ~554 ("Vesper will search and compare options" → first person), auth-invite ~710 ("Sign in and Vesper will begin." → e.g. "Sign in — I'll take it from here."), trip-settings ~400 (attributed or roman per Session P treatment — verify it was caught), plus kill the bundle's only exclamation: people-collab ~637/1256 "Welcome to Lisbon!" → promote its existing sub-line "You're in. Ana and Theo can see you joined." And rewrite the service-desk register at trip-document-canon ~1774/1903: "Everyone approved — you're all set for Wednesday." → "Everyone approved — Wednesday's settled."

## 4. Record the two taxonomies (one line each, Canon Consolidation)

- **People-words:** member = current trip role · traveler = headcount/party context · companion = past co-traveler (Atlas/People register). All three stay; the rule just says which register uses which. (Optional consistency fix: pick "travelers" for all count strings — "4 travelers" — since Trip Settings and Costs already use it.)
- **Reader-objects:** Dossier = single deep-read · Guide = curated picks list · retire bare "READ" as a third user-facing kicker noun (keep "8 min read" duration strings — different sense). Fix the "READ · FOR YOU" kickers to "DOSSIER · FOR YOU" or the guide equivalent.

## 5. Canonize the duplicated voice lines (drift already happening)

Three copy families exist in multiple wordings; pick one wording each, mark the owning page, and align the copies:
- **"I'll keep the tab"** — 7 instances, 4 wordings, 6 files (costs-screens ~99 is the natural owner; align trip-edge-states ~199, trip-document-canon ~241, trip-live ~101, trip-record-sheet ~138/144, trip-imminent ~162).
- **"Nothing needs you"** — 6 files, 4 endings; suggest the strongest: "Nothing needs you — the trip's just unfolding." (owner: Home quiet/calm board).
- **Ryokan exemplar** — 5 files; fine as a recurring exemplar, but align the wording exactly so it reads as THE canonical example, not five drafts. (Stay's "You're covered for all five nights" ×2 internal: align.)

## Definition of done

Verb-canon board exists on Ops page · trip-surface + Plan naming rulings recorded and applied (zero remaining "Single Trip Home"/"Trip Home" in prose) · first-person rule recorded, five leaks + two service-desk lines fixed · both taxonomies recorded · three copy families each have one wording · 02d rows flipped · export a fresh handoff.
