# Path to First Dogfood-Ready Journey — Wedge (02 → 05)

> Status: in-flight plan
> Owner: founder
> Last updated: 2026-06-27
> Goal: take ONE journey from "passes static trace" to "a real user completes it on a
> phone, against the live backend" — then repeat.

## Why this slice

The product's wedge is **group trip planning** (belief #14: the invite *is* the
distribution). The thinnest end-to-end slice that proves the wedge is the chain of two
journeys:

- **[Journey 02](../journeys/02-concrete-trip-creation-and-invite.md)** — organizer creates a trip, invites a friend, both land in one shared workspace with correct membership.
- **[Journey 05](../journeys/05-group-planning-to-proposal-to-plan-mutation.md)** — the group asks Vesper for a change, reviews a proposal, votes/applies it, and sees the plan update clearly (plus direct Change Studio edits).

Together: **create → invite → plan → propose → mutate → see-it-everywhere.** That is the
smallest thing a real group can actually *do* and feel value from. Everything else is
secondary for first users.

Current scorecard: both journeys are **static-trace ready**, **2/2 mock-walked** (data
layer, 2026-06-27), **0/2 dogfood-ready**. The remaining work is *validation*, not
construction — the build is largely done. The mock-walks proved every invariant the
mock layer can express; the live walk (DoD 5/6) covers the rest (see gaps below).

## Scope split (for THIS slice only)

Classify ruthlessly. The rule: a thing is **must** only if the slice can't complete
without it.

**MUST (block launch of this slice)**
- Trip create + invite + accept + membership coherence — [Group / Social](../systems/group-social.md)
- Concierge group chat (ask for a change) — [Concierge](../systems/concierge-vesper.md)
- A plan to mutate (generate or seed) — [Planning / Itinerary](../systems/planning-itinerary.md)
- Proposal lifecycle + direct edit + revert + receipts — [Proposals / Change Studio](../systems/proposals-change-studio.md)
- Trip Home / Plan / Changes coherence after mutation — [Trips / Folio](../systems/trips-folio.md)
- Group-safe routing of any private input — [Memory & Preference](../systems/memory-preference.md) + Concierge

**SHOULD (fake or manual for first ~10 users)**
- Push notifications for proposal events → start with in-app activity only; deliver pushes later.
- Map surface parity → verify it doesn't *lie*, but Map polish is not blocking.
- Onboarding polish → a rough but honest intake is fine.

**DARK (flag off, confirm invisible)**
- Booking transactions (Duffel), pay-later holds, Voice/narration mic, Postcards, Atlas Unpacked share, cross-trip "Vesper knew." All exist; none gate this slice. **DoD point 7 requires confirming they're invisible, not removed.**

## Invariants to verify (the correctness checklist)

Pulled from each charter's **Invariants** + each journey's *Must Never Happen*. These are
what a live walk must actively try to break:

| # | Invariant | System | How it breaks |
|---|---|---|---|
| I1 | Invite maps to exactly one trip; accept lands in the correct workspace | Group/Social | stale `currentTripId` sends invitee to wrong trip |
| I2 | Auth detour preserves the invite token | Group/Social | sign-in mid-invite drops context |
| I3 | Non-member sees no private trip data pre-accept | Group/Social | invite landing over-fetches |
| I4 | Private constraint never reaches the group | Memory+Concierge | free-text reply bypasses `group_compose.py` |
| I5 | Accepted change emits a visible receipt; rejected confirms original remains | Proposals | silent mutation / silent disappearance |
| I6 | Revert truthfulness — Plan **and** Map reflect it | Proposals+Folio | ghost state after revert |
| I7 | Optimistic concurrency — commit surfaces stale `expected_updated_at` | Proposals | clobbered concurrent edit |
| I8 | Idempotency — retries never duplicate votes/applied changes | Proposals | double-apply on retry |
| I9 | Cross-surface coherence after any mutation (Home/Plan/Changes/Map/Notif agree) | Folio | journey 06 parity — no unified block-id test today |
| I10 | One proposal-creation path (`build_and_persist_proposal`) | Proposals | chat-created proposal drifts |

I4, I5, I6, I9 are the highest-value — a privacy leak (I4) is the unrecoverable trust
event; coherence (I9) is the named drift hotspot.

## Definition of Done (8 points) — current state

| # | Gate | State | Work |
|---|---|---|---|
| 1 | Charters current for every system in the slice | ✅ done | all 6 written |
| 2 | Backend deterministic/replay tests green | ✅ **307 green** | full wedge suite vs live Postgres (invites/members/plan-edit/proposals/apply/folio/trips), 2026-06-27 — **certifies I5/I7/I8 server-side**; fixed 3 stale invite-accept tests left behind by the J1 atomic-consume refactor |
| 3 | **Frontend mock-walk passes** | ✅ **02 + 05 + 06 green** | `journey-02-mock-walk.smoke.test.tsx` (9) + `05-group-planning-proposal-mutation.test.ts` (11) + `06-cross-surface-coherence.test.ts` (8) |
| 4 | **Maestro flow green on-device** | 🔶 **authored, run pending** | `.maestro/24-journey-02-create-invite.yaml` + `25-journey-05-proposal-mutation.yaml` written, all selectors source-verified, harness confirmed working — needs Metro/dev-client running to boot JS and go green (your machine) |
| 5 | **Walked once by you on a real phone vs live backend + real Clerk** | ❌ | the two-account invite walk (needs 2 devices/accounts) |
| 6 | Invariants I1–I10 spot-checked on the live walk | ❌ | run the AI trace prompts in each journey doc, then verify live |
| 7 | Dark features confirmed invisible | ⬜ | flip through the slice confirming no booking/voice/postcard leaks in |
| 8 | One real external user completes it | ❌ | TestFlight invite to one friend |

## Work sequence (do in order)

1. ✅ **Mock-walk 02** (DoD 3) — `journey-02-mock-walk.smoke.test.tsx` (contracts + invite landing surface).
2. ✅ **Mock-walk 05 both tracks** (DoD 3) — `05-group-planning-proposal-mutation.test.ts` (11) + `journey-05-mock-walk.smoke.test.tsx` (Changes UI).
3. ✅ **Coherence test for I9** — `06-cross-surface-coherence.test.ts` (8). J06 smoke duplicate retired (merged into this file).
4. 🔶 **Maestro flows** (DoD 4) — authored: `.maestro/24-journey-02-create-invite.yaml`, `25-journey-05-proposal-mutation.yaml` (selectors source-verified, appended to `config.yaml` order). **To run green on your sim** (harness confirmed working; just needs JS loaded):
   ```
   export JAVA_HOME=/opt/homebrew/opt/openjdk && export PATH="$JAVA_HOME/bin:$HOME/.maestro/bin:$PATH"
   npx expo start --dev-client          # leave running; reload the app once
   maestro test .maestro/24-journey-02-create-invite.yaml
   maestro test .maestro/25-journey-05-proposal-mutation.yaml
   ```
   4 missing-testID gaps were marked `# GAP` with `optional` text fallbacks (PlanBlockRow, ChangeStudioSheet, Changes screen, Button testID forwarding) — flows run without them but hardening them removes text-selector fragility (spawned a task).
5. **Live two-account walk** (DoD 5/6) — organizer + invitee, two devices, live Fly backend + real Clerk. Actively try to break I1–I10. Use the AI-trace prompts in the journey docs first to find suspects, then verify on-device.
6. **Dark sweep** (DoD 7) — confirm booking/voice/postcard surfaces are invisible across the slice.
7. **One friend on TestFlight** (DoD 8) — the real validation. Watch them, don't coach.

Then: pick the next journey (likely **10/12** booking+expense trust loop, or **08** live companion) and repeat. **Do not start new substrate until this slice is genuinely dogfood-ready.**

### Mock-layer fidelity gaps (updated 2026-06-28, post Stream D)

**Closed in code (2026-06-27/28):**
- `getTripMembers` layers runtime `_addedTripMembers`
- `viewInvite` resolves through `_createdTrips`
- Folio spine composes over `_getMockItinerarySync` (shared read model with Plan/Map)
- **`getActionReceipt`** — derives a real receipt from `recent_changes` (`utils/api/mock/trips.ts`; journey-05 asserts I5 via the endpoint)
- **`postEditCommit` 409 + idempotency cache** — stale `expected_updated_at` throws 409; token replay returns cached body (`utils/api/mock/profile.ts`; journey-05 asserts I7/I8)

**All mock-layer fidelity gaps from the original wedge pass are closed in code** (2026-06-28), including per-trip proposal ledger (`_ledgerProposalIdForTrip` in `utils/api/mock/trips.ts`).

> **Consequence for the live walk (DoD 5/6):** **I5, I7, I8-applied** are now mock-certified (journey-05). **I6 (revert truthfulness)** remains backend-certified only until a live revert walk. Cross-surface **Folio-spine parity (I9)** is mock-certified via the shared itinerary read model.
>
> **Backend logic for I5/I6/I7/I8 is certified by automated tests:** `tests/scenarios/test_j05_proposal_plan_mutation.py` + `test_j05_plan_edit_commit.py` (retired `test_wedge_journey_e2e.py`, 2026-06-28). The live walk verifies **FE wiring/surfacing**.
>
> **Operational note (RESOLVED 2026-06-27):** the shared dev `vesper` DB was initially migration-drifted — stamped at the phantom pre-squash revision `000422aac133`, missing recent `itinerary_blocks` columns — so the E2E's block-touching cases skipped (2 passed / 4 skipped). **Running the backend test suite migrated it to a current head (`sma26expimmut`); the columns are now present and the E2E passes 6/6 even in isolation.** The test harness applies migrations to the DB it connects to, so the drift self-healed. No manual action needed.

## Validation tooling (already built — use it)

- **Personas + time-travel clock + force-state** (`app/dev/persona-switcher.tsx`, `utils/now.ts`) — reach any trip lifecycle state without a backend.
- **Maestro** (`.maestro/`, 61 flows) — DevFab deep-links (`guide://dev/persona-switcher`) drive setup.
- **Offline golden-path suite** (`npm run test:offline`) — the mock-walk home.
- **AI trace prompts** — each journey doc ships one; run it as the first pass of step 5.
- **Backend replay/eval gate** — keeps the backend honest offline (zero-API).
