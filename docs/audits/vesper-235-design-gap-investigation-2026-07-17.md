---
doc_type: working
status: active
owner: founder / design / engineering
created: 2026-07-17
last_verified: 2026-07-17
expires: 2026-08-16
why_new: Revalidates the next design iteration against the newer Vesper 235 bundle and current code after the Vesper 220 audit was partially remediated.
supersedes: []
source_of_truth_for: [vesper-235-design-code-gap-investigation]
---

# Vesper 235 Design ↔ Code Gap Investigation

> Date: 2026-07-17
> Verification status: revised after a claim-by-claim source pass on 2026-07-17.
> Design evidence: the `vesper 235` design bundle (Canon 130, exported 2026-07-17 16:07).
> Committed code evidence: `travel-app` `f74def2768db03e28ae3e85118c4a83d75d8926a` and `travel-agent` `7c75097b994f5b12bd8d9c0f200abcfe157b84a3`. These heads include work committed between 16:00 and 16:39, after the first draft's approximate snapshot.
> Scope: identify where the **design is behind the code** so the next Claude Design iteration works from real product behavior. Code-behind and stale-design findings are included only where they change that judgment.

## 0. How to read this audit

This revision uses four evidence labels:

- **VERIFIED** — directly supported by current design and source.
- **PARTIAL** — the core claim is real, but the original wording overstated absence, breadth, production exposure, or exact parity.
- **CHANGED AFTER INITIAL SNAPSHOT** — later commits changed the answer during the audit window.
- **NOT SUBSTANTIATED** — removed from the actionable tally because the source did not support the claim as written.

Two provenance statements from the first draft cannot be independently verified: that no prior audit documents were read and that five parallel investigations were used. They are not product findings and are omitted here.

The first draft's aggregate `~45 design behind / ~20 code behind / ~20 aligned / ~10 stale` tally is also removed. It had no reproducible finding ledger, allowed partial gaps to be counted as total absence, and mixed route rows, product behaviors, components, and editorial cleanup as equal units.

## 1. Snapshot relationship

- **VERIFIED:** Vesper 235 is current in visual-system terms. Its header, Chat Working States, Post-Trip Continuity, Object Inspection v2, and itinerary consolidation work run through July 17.
- **VERIFIED:** code intentionally cites numbered design exports; `travel-app` commit `b1bef1e7` is titled `feat: close Vesper 220 alignment gaps`.
- **PARTIAL:** saying code “trails design by 15 exports” is useful shorthand for that one alignment commit, not a general parity metric. Code and design advanced independently after Vesper 220.
- **VERIFIED:** the remaining gaps are concentrated in code-discovered durable states and governance: cancellation, settlement, operation-specific recovery, delivery failure, authority transfer, public projection, and route ownership.
- **CHANGED AFTER INITIAL SNAPSHOT:** archived-trip recovery landed in both repositories between roughly 16:25 and 16:39. Any earlier claim that recovery substrate was absent is now stale.

## 2. Corrected executive summary

The strongest design-behind themes are:

1. **Money truth and booking cancellation.** Code has durable cancellation reconciliation, completion receipts, participant consent, view-only controller states, expense review, recorded-payment voids, and cancelled-booking → Costs review. The design has good adjacent principles but not the complete user-facing lifecycle.
2. **Operation-specific itinerary coverage.** The Workflow Canon gives six detailed journey families; the engine exposes 14 operation types. Vesper 235 already covers more than the first draft credited—attendance, occurrence correction, split creation, provider separation, generic recovery, and archived recovery are present—but it does not provide a single operation-by-operation authority/receipt/recovery matrix for the shipped grammar.
3. **Home and Chat reliability language.** Deck uncertainty, the complete delivery/failure state machine, fail-closed roster authority, and general group-turn presence remain behind code. Chat card coverage itself is not nearly as sparse as first claimed.
4. **Public proposal projection.** An unauthenticated proposal landing derives a public status line from live vote data despite the External Sharing canon saying group decisions and vote counts are not public. This is an ungated backend path; current deployment and a user-facing mint affordance were not verified.
5. **Authority-transfer consequences.** Vesper 235 already draws basic organizer handoff. Code is ahead in shared-plan-owner transfer, departure preflight, atomic handoff-and-leave, booking-controller transfer, proposal expiry, and unsettled-balance blocking.
6. **Governance bookkeeping.** The route table contains exactly 62 rows while its heading still says 53. Fifteen current route files are absent from the table, and `/atlas/receipt` is a phantom route.

Important code-behind items remain: native LiveKit app wiring, removal of named voice personas, the Chat thinking ladder, full Document mode, several Atlas/Discover deferred loops, and portions of cancelled/archived trip UI.

## 3. Ranked design-iteration backlog

The order below is based on truth/privacy risk first, then centrality and leverage. “Present in source” does not mean production deployment was verified.

| # | Design work | Why it remains |
|---|---|---|
| 1 | **Booking cancellation lifecycle** — pending verification, manual review, not-cancelled resolution, completion receipt, cancelled booking → Costs review | Durable money truth exists in source; the drawn booking/cost system does not own the whole lifecycle |
| 2 | **Public proposal-share ruling** — prohibit/gate it or define a redacted projection; then align the four runtime OG-card types | Direct canon contradiction on an unauthenticated backend route |
| 3 | **Real itinerary operation matrix** — 14 operation types × preview, authority, receipt, recovery, provider effect | Vesper 235 has strong journeys but no exhaustive shipped-operation contract |
| 4 | **Consolidate Move** — anchor-relative Before/After is canonical; time selection survives only where time is the conflict | Newer itinerary boards and code agree; the Workflow Canon still contains an older time-picker journey |
| 5 | **Deck transaction lifecycle** — acting → reconciling → committed/superseded/uncertain/error | Flagship surface has a new honesty state with no dedicated board |
| 6 | **Chat delivery and room authority** — 11 phases, six failure classes, turn-vs-screen ownership, roster-unavailable, split outcome, repaired-arrival seam | Reliability behavior is real and only partly covered by Working States |
| 7 | **Consent and controller variants** — pending/approved/declined/remind/cooldown/narrow-to-self plus view-only attribution | Existing design sketches the concept; runtime state breadth is larger |
| 8 | **Observed-reality persistence** — distinguish attendance, occurrence, plan correction, and provider correction; add provenance/supersession/receipt rules | Correction UX exists in Vesper 235; durable writeback anatomy does not |
| 9 | **Parallel-plan lifecycle supplement** — update/dissolve/end/cancel-one-stop/absorb-back/split-origin | Split creation is designed; later lifecycle and recovery are incomplete |
| 10 | **Departure and succession consequences** — shared-plan owner, organizer, booking controller, proposals, and balances | Basic handoff exists; the atomic consequence model is missing |
| 11 | **Notification routing governance refresh** | Runtime destinations now exist, but the design routing matrix does not enumerate all intents |
| 12 | **Route-mapping refresh** — 62-row count, 15 missing route files, remove `/atlas/receipt` | Makes the Canon Index truthful on its own terms |
| 13 | **Atlas corrections** — remove the retired home-map assumption; reconcile render-control contradiction; remove archived Reading if it is not being built | Small changes that prevent implementation from following stale doctrine |
| 14 | **Discover cover contract** — document the shipped Plan-a-trip CTA, five context shapes, IssueFloor, and updating state | Wedge-facing behavior exists without a consolidated design contract |
| 15 | **Receipt editorial dictionary** — operation/recovery reason codes → approved human copy | Several surfaces still mechanically replace underscores with spaces |

## 4. Trip / Itinerary / Changes / Operations

The July 16 cutover is **VERIFIED**: frontend legacy readers and compatibility editors, backend legacy writers and rollout infrastructure, and retired Folio routes/references were removed or archived. This does not imply that every leftover lexical “Folio” reference is gone.

### DESIGN BEHIND — verified or corrected

1. **14 operation types, not 15.** `ItineraryOperationType` contains: `materialize_shape`, `add`, `move`, `reorder`, `replace`, `remove`, `restore`, `set_attendance`, `mark_occurrence`, `create_parallel_plan`, `update_parallel_plan`, `dissolve_parallel_plan`, `optimize_day`, and `replan`. The API module has 18 route decorators.
2. **Six detailed Workflow journey families versus 14 runtime types.** The Workflow Canon explicitly calls itself “the six typed operations” and gives detailed journeys for Move, Add, Optimize/Replan, Replace/Rebook, Split, and Remove. Authority is an ending, not a seventh operation.
3. **PARTIAL, not absent:** Vesper 235 already designs attendance and occurrence correction, generic revert/recovery, split creation, and provider-linked failure. The missing piece is exact type-level ownership for `reorder`, `restore`, `set_attendance`, `mark_occurrence`, `create/update/dissolve_parallel_plan`, `materialize_shape`, and a distinct `replan` contract rather than treating Optimize/Replan as one journey.
4. **Move has an internal design contradiction.** Newer itinerary redesign boards and code use candidate days plus Before/After anchors (`relativePlacement`) and separate reorder semantics. The Workflow Canon still shows a time-chip Move configuration. Consolidate around anchor-relative placement; use time controls only for genuine time conflict resolution.
5. **Parallel plans are partially designed.** Split initiation, member branches, authority, atomic commit, safe failure, and attendance are drawn. Code adds topology-owner versus decision-owner, update/dissolve, branch-stop cancellation, absorbed-stop restoration, split origin, and revert review. Those later lifecycle states need a supplement, not a ground-up redesign.
6. **Reversal is partially designed.** Canon establishes capability-authored recovery, exact versus non-exact reversal, “revert as a new operation,” and provider limits. Code adds lineage uniqueness, compound atomic inverses, stale reversal review, tombstones/successors, and `diff_safe`, `diff_safe_partial`, and `version_restore` modes. Those details lack a consolidated design matrix.
7. **Observed reality is partially designed, not “fully undesigned.”** Vesper 235 explicitly contains “Your attendance,” “Happened,” “Didn’t happen,” cancelled/locked personal correction, and planned-versus-happened doctrine. Missing: writeback provenance, confidence, visibility, supersession chains, provider corrections, and durable receipts.
8. **Provider sagas are partially designed.** Replace/Rebook includes provider pending, refund failure, retry, and partial success. Code is broader: continuation verbs, held-price reapproval/decline, expiry, and `manual_action_required`. Design should extend the existing saga language instead of inventing a second family.
9. **Authority taxonomy remains behind code.** Runtime confirmation reasons and proposal policy are more exact than the boards: meaningful/broad/protected change, provider fee/nonrefundability/changeability unknown, provider action, organizer review versus affected-member vote, voluntary propose, and unavailable owner health.
10. **Now Mode is partial.** The Trip canon contains live/completed posture and a Now-first weighting; code provides concrete Walk me there, Running late, and Mark done intents plus active/between/day-complete modes. Add an operational board rather than another header redesign.
11. **`materialize_shape` and chat → replan need an entrance/landing contract.** The accepted-shape-to-itinerary transition and Trip Details “Replan destination or dates” handoff exist in code but are not owned as a complete journey.
12. **Decision grammar still needs consolidation.** Chat vote cards, Changes, Proposal Detail, and Stay decisions expose related but non-identical approval language. The dated code comment is valid evidence of an unresolved cross-surface rule.
13. **Succession is partial, not absent.** Trip Settings already draws organizer handoff and leave guards. Missing: shared-plan ownership as a distinct authority, departure preflight consequences, atomic handoff-and-leave, booking control transfer, proposal expiry, and balance blocking.
14. **Receipt copy remains mechanical.** Changes, object detail, attention, and operation cards still use underscore replacement for several reason/summary codes. The substrate exists; the editorial dictionary does not.

### CODE BEHIND / changed during verification

- **CHANGED AFTER INITIAL SNAPSHOT:** the backend recover endpoint and app API client now exist for archived trips. The design already draws Recover and Reuse-as-template. Current route-level UI completion still needs a focused implementation audit; Reuse-as-template was not found.
- **DomainIndex family:** transport and bookings have the clearest IR-native index treatment; several other domains still hand off to older productive screens.
- **Hybrid plan shell:** `plan.tsx` combines the canonical Trip header/spine with additional situation, ticket, energy, and backbone bands. This needs an explicit keep/fold/remove decision.
- **Landing resolver:** implementation remains simpler than the full design edge-rule set.
- **Expired proposal wording must be scoped.** Canonical itinerary-operation proposals do not use `expired`; booking proposals legitimately do. Remove only expired specimens that claim to represent the itinerary-operation proposal state machine.

### ALIGNED OR CLOSE

- Trip entry, day chapters, gaps, travel connectors, and the exact-return registry are strongly aligned.
- Object Inspection v2 covers seven object kinds, shared contextual/comprehensive entry, typed states, personal/factual correction, provider truth, and owner-versus-destination distinctions.
- Replace versus Replace-and-rebook, capability-authored recovery, stale/concurrent review, and the Changes timeline are materially represented in both design and code.
- Residue remains: a few status-color/vocabulary differences, rebased-proposal receipt treatment, and the editorial receipt dictionary.

## 5. Costs / Booking / Stay

### DESIGN BEHIND

1. **Cancellation reconciliation — VERIFIED.** Internal/provider states include processing/refreshing/pending/cancelled/not-cancelled/manual-action-required. The bounded client projection primarily exposes pending/cancelled/manual-action-required. The UI says “Cancellation is still being verified” and blocks a second submission. Design should distinguish internal truth from user-facing states instead of presenting one flat enum.
2. **Cancellation completion receipt — VERIFIED.** A replay-safe receipt is emitted through the generic `notification` card type for cancelled, not-cancelled, and escalation outcomes. This deserves money-specific anatomy or an explicit ruling that the generic card is sufficient.
3. **Cancelled booking → Costs review — VERIFIED.** The app contains `BOOKING CANCELLED · REVIEW COST` and “Settlement is paused while this expense is under review.” Costs canon lacks this booking-linked review posture.
4. **Booking controller — VERIFIED.** Provider mutation is controller-gated and other viewers receive a view-only explanation. The original “every receipt needs a variant” wording was too broad; design needs viewer/controller variants for controller-owned actions and receipts.
5. **Participant consent — VERIFIED, partially designed.** Code supports per-person pending/approved/declined/excluded, confirmation blocking, narrow-to-self, and a four-hour reminder cooldown. Canon sketches the approval moment but not the full ledger lifecycle.
6. **Departure consequences — VERIFIED, partially designed elsewhere.** Basic handoff exists in Trip Settings. Booking controller transfer, proposal expiry, account-deletion preservation, and the exact consequences shown during departure are not consolidated there.
7. **Expense review governance — VERIFIED.** Eligible payers/share holders can open; only the opener can withdraw; payer/organizer resolution and settlement exclusion are enforced; live payments must be voided before review. Design needs the role-gated action and paused-settlement states.
8. **Recorded payments and void — VERIFIED.** The read-side ledger, visible voided rows, restricted void action, and exact transfer recording exist. Costs canon does not own the full history/void grammar.
9. **Currency truth — VERIFIED.** Settlement uses one settlement currency; unsupported legacy conversions are excluded rather than fabricated; `ESTIMATED RATE` exists.
10. **Masked expenses — VERIFIED.** Private payer display and hidden non-payer amounts exist; masked splitting is constrained and booking-derived expenses cannot be masked. No complete canon treatment was found.
11. **Split-type immutability — VERIFIED.** Edit keeps the established split type display-only, and equal-share language is derived from actual shares.
12. **Archived-trip booking closure — PARTIAL.** Archival guards provider work and recovery now exists; a compact design ruling for booking behavior on archived/recovered trips is still useful.

### ALIGNED / qualifications

- Stay’s core state model, candidate comparison, hold distinction, night coverage, gaps, split stays, check-in/out, and returned suppression are strongly aligned. This was a source inspection, not exhaustive device certification; “all gaps verified closed” was too absolute.
- Receipt/OCR intake follows confirm-before-add truth, but scan-state artboards remain a small gap.
- There is no set-budget flow; the read-only estimate framing is consistent.
- Repository surface contracts contain important implementation law, but calling them a “shadow canon” is an interpretation, not a verifiable defect. The actionable point is to fold durable money rules back into the drawn canon.
- No claim is made here that these provider paths are deployed or commercially launchable. The booking feature documentation itself says no provider category currently has a launchable, verified end-to-end live booking flow.

## 6. Vesper Home / Chat / Voice / Notifications / Search

### DESIGN BEHIND

1. **Deck transaction lifecycle — VERIFIED.** Runtime phases are `acting | reconciling | exiting | error | uncertain`, with committed/superseded/uncertain outcomes and a shielding overlay. The deck canon explains advancement but does not draw these transaction states.
2. **Chat delivery lifecycle — VERIFIED, partially designed.** Code has 11 phases and six failure classes with turn-versus-screen ownership. Working States covers important waiting and durable-work patterns, but not the complete delivery/failure mapping.
3. **Fail-closed roster authority — VERIFIED.** `loading | unavailable | solo | group` prevents an unverifiable shared room from mounting. No explicit “cannot verify this room” design state was found.
4. **Group observer presence — PARTIAL.** Vesper 235 has a plan-build group-observer specimen. Code generalizes presence to “{name} is asking Vesper…” plus an optional observer SSE that exposes activity but never reply prose. Design needs the general room-level privacy/observer rule, not a claim of zero coverage.
5. **Human-message versus AI-turn failure and repaired arrival — VERIFIED as reliability concerns.** The split outcome and late propagation need a clear transcript seam and retry ownership.
6. **Attachment coverage claim corrected.** Runtime has exactly 15 attachment types, not 16. Chat canon also contains 15 conceptual card sections, not five. The real gap is an exact runtime-type → canonical-family table, especially for `itinerary_operation`, `document_edit`, `plan_ready`, `trip_creation_proposal`, and `lazy_research` lifecycle semantics.
7. **Markdown substrate — VERIFIED.** Native markdown and streaming repair are current behavior. Canon needs a concise typography and partial-syntax rule, not a new card family.
8. **NarrationCard — PARTIAL, not absent.** Chat canon already draws Narration/Guide with prose, audio scrubber, duration, and continuation. Runtime adds depth, feedback, lazy audio, and a broader style/depth matrix; extend the existing card.
9. **Home cold/stale truth — VERIFIED.** The query cache can restore home data for up to 12 hours. Add skeleton and stale-verdict rules for the hero.
10. **Queued restored turn — VERIFIED.** Restored queued turns require an explicit Send now action. Add one ruling clarifying that restoration does not violate the no-concurrent-send rule.
11. **Bundle hygiene — VERIFIED as design-internal cleanup.** Superseded Quiet/Whisper voice directions need unmistakable archive/superseded marking wherever they remain loadable.

### ALIGNED / no longer design gaps

- **Notification preferences are designed.** Trust & Controls already draws cadence, quiet hours, Push/SMS/Email, Critical always on, Pause all, system-permission recovery, and trip overrides. The first draft incorrectly called this whole surface undesigned.
- **Notification destinations are implemented.** Current committed code routes `story_ready`, `on_this_day`, `unpacked_seasonal`, `map_view`, and invite-answer entries. The remaining issue is the stale design routing matrix and feed-sectioning documentation.
- **Universal Search action routes are implemented.** Backend action results now receive non-mutating route hints and the frontend parses them. Remove the earlier “D25 follow-up half-done” claim. `site` and `accommodation` still lack direct frontend result routes and remain a valid gap.
- Notifications inbox, durable-workflow strips, Deck reseeding, search chip limits, and Ask-Vesper handoff remain close to canon.

### CODE BEHIND

- **Native live voice:** `connectToLiveKitRoom` and an injectable connector seam exist, but no app startup wiring installs the connector. Mock mode stops at `ready_to_connect`; real mode without wiring surfaces an error. “Pure no-op stub” was too coarse.
- **Named personas:** ten city personas remain in `guide_voices.py`, conflicting with the explicit “Vesper, full stop” identity ruling. Narration-specific exceptions would need a new decision.
- **TTS configuration mismatch:** configuration names ElevenLabs for narration, while current guide narration uses Cartesia. Treat this as implementation/configuration drift, not a design gap.
- **Thinking ladder:** design’s escalating thinking treatment remains unbuilt; TypingIndicator still supplies the current waiting primitive.
- **Plan-build day identity:** backend progress does not carry enough day identity for the designed per-day fill behavior.
- **Document mode and conversation-create doorway:** meaningful substrate exists, but the complete designed takeover/naming/chooser flow is not wired.
- **Compare/Flight deck faces:** retain a parked/superseded annotation so deleted orphan faces are not reintroduced without a producer.

## 7. Atlas / Discover / Places / Story / Sharing / Invite / Onboarding / Trips Home

### DESIGN BEHIND OR INTERNALLY STALE

1. **Public proposal share contradiction — VERIFIED.** `/p/{trip_id}/{proposal_id}` is unauthenticated and derives its status line from proposal votes. External Sharing says group decisions and vote counts are not public. No route-level feature flag was found. The image is **cached for five minutes** (`Cache-Control: public, max-age=300`), not uncached. No in-app mint affordance was found, and production deployment was not verified.
2. **Four runtime OG-card types — VERIFIED.** Story, invite, proposal, and Unpacked use shared 1080×1920/9:16 rendering infrastructure. External Sharing has a broad object matrix, but it does not provide an exact projection/redaction contract for all four runtime card payloads.
3. **Atlas home map assumption — VERIFIED stale.** `/api/atlas/map` and `map_compose` were deleted; `/your-map` redirects to Long View. Atlas still draws home place-map modules. Decide whether they are decorative/local projections from accepted history or remove them; do not imply the deleted endpoint still exists.
4. **Readings semantics mostly align.** Both design and code say kept views recompose live and use live/updated/active/thin freshness. The remaining mismatch is `archived (re-addable)`: current kept-board behavior soft-deletes and has no Reading archive state. The first draft incorrectly described the whole Reading model as design-behind.
5. **Your Memory contains an internal design contradiction.** `trust-screens.jsx` draws a live render toggle; `atlas-memory-final.jsx` says rendering is “coming later.” Runtime exposes a gated capability. Reconcile the two design sources. Keep/restore/removed behavior is substantially designed; only exact runtime availability and correction actions need checking.
6. **Invitee Post-Join status is stale — VERIFIED.** The shipped payoff surface matches much of the exploration, while the page still says active exploration and references retired Folio framing. Graduate it and re-anchor it to the current Trip plan surface.
7. **Discover cover behavior — VERIFIED in code.** Plan a trip, the five read shapes (`dream | briefing | proximity | retrospective | dual`), IssueFloor, and Updating this edition exist. Consolidate them into the Discover contract.
8. **Succession depth — PARTIAL.** Basic organizer transfer is already designed. Shared-plan-owner transfer, preflight blockers, atomic departure, controller transfer, proposal expiry, and balance consequences remain missing.
9. **Invite substance gate — VERIFIED.** `trip_needs_substance`, quota failure, and organizer concierge recovery exist without a complete organizer-side design moment.

### CODE BEHIND / gated

- Story sharing and Unpacked minting are built but deliberately dark behind frontend and backend flags.
- Memory Inbox remains narrower than the five-kind canon.
- Discover Map’s full pin taxonomy is not implemented.
- Several anniversary/seasonal/auto-candidate/postcard loops remain flag-dark by design.
- “Plan Similar” and some public/deferred matrix rows remain unbuilt or gated.

### ALIGNED

- Atlas’s staged place-first home, Long View, current correction model, Trips Home hero cascade, Trip creation proposal flow, onboarding pipeline, and core Discover/Places reader ownership are materially represented in code.
- Post-Trip Continuity and Story/Memory ownership are substantially aligned.

## 8. Routes, components, and foundations

### Route diff

The governance table contains **exactly 62 rows**, while its heading and Canon Index description still say 53. Because some rows bundle multiple routes, this is a table-row count, not a count of every concrete Expo route.

Fifteen current route files are absent from the table:

1. `/(tabs)/trips/[tripId]/details`
2. `/(tabs)/trips/[tripId]/details/[section]`
3. `/(tabs)/trips/[tripId]/object/[kind]/[objectId]`
4. `/atlas/memory`
5. `/atlas/scan`
6. `/atlas/candidate/[id]`
7. `/atlas/delegation`
8. `/atlas/whole`
9. `/atlas/removed`
10. `/atlas/shared-links`
11. `/atlas/unpacked-card`
12. `/atlas/narration-history`
13. `/atlas/voice-logs`
14. `/atlas/feedback`
15. `/(auth)/goodbye`

`/atlas/receipt` appears in the design exception list but no corresponding route file exists; `/atlas/data-receipt` is the real route. `narration-history` and `voice-logs` both exist and need a keep/redirect/retire ruling.

### Component diff

**Converged:** Button, StatusPill, CardSurface, VesperMark/signature carve-outs, design tokens, State System, FloatingTabBar, header contracts, sheet primitives, Chat Working States, and the `{family, variant}` card taxonomy have strong cross-references between code and canon.

**Correction to the first draft:** `WorkerProgress`, `InlineAbsence`, and `ActionFailureInline` are explicitly canonical in the State System. `TravelerPicker` is explicitly adopted by Interaction Surfaces. They are not unowned components.

**Likely active component coverage gaps after exact-name search:** `StateTransition`, `ProgressGate`, the shared `Tap` primitive, `VesperDiagnosis`, `NavPills`, `DismissButton`, `ScreenScaffold`, `CardActionPill`, `CardStatusLabel`, and `QueuedTurnTray`. `CardLift` appears only in an archived design exploration, so current ownership is unclear rather than wholly absent.

**Code-behind rulings:** Trips Home still renders the create FAB despite the A8 kill ruling. The earlier Universal Search action-route gap is now closed. Header-family documentation and a few parchment/glass consumers still merit a smaller consistency audit.

### Governance and foundation cleanup

- The Canon Index open list still contains items that later Vesper 235 pages resolve, including the completed Trip → Memory → Story boundary.
- The itinerary parity matrix should be re-issued after the July 16 cutover rather than merely flipped from “code audit required” to “done.”
- Facts-Only implementation framing is stale: the wrapper substrate exists and enforcement remains flag-controlled.
- Content Contract FIX-NOW history should distinguish implemented source changes from flags still running in log/dark modes.

## 9. Recommended Claude Design sequence

### Round 1 — money and public truth

1. Cancellation lifecycle, completion receipt, and cancelled-booking → Costs review.
2. Public proposal-share ruling plus four-card projection/redaction table.
3. Consent ledger and controller/view-only booking variants.

### Round 2 — itinerary grammar

1. One 14-operation capability matrix; reuse the existing six journey families.
2. Resolve the Move time-picker versus anchor-relative contradiction.
3. Add observed-writeback persistence, parallel-plan later lifecycle, and editorial receipt mapping.

### Round 3 — reliability and authority

1. Deck action lifecycle.
2. Chat delivery/failure, roster-unavailable, general observer privacy, and repaired arrival.
3. Departure/succession consequences layered onto the existing Organizer Handoff design.

### Round 4 — governance polish

1. Route table refresh and `/atlas/receipt` removal.
2. Atlas map/Reading archive/render-toggle corrections.
3. Discover cover contract, notification routing matrix, and active component ownership gaps.

## 10. Code queue, not Claude Design work

- Install and verify native LiveKit application wiring.
- Execute the singular-Vesper persona ruling or explicitly approve a narration-only exception.
- Build the thinking ladder and Plan Build day-identity event.
- Complete Document mode.
- Remove the Trips Home create FAB if A8 still wins.
- Add frontend destinations or stop indexing unroutable `site` and `accommodation` Universal Search results.
- Finish archived-trip UI and Reuse-as-template only after the current recovery substrate is audited.
