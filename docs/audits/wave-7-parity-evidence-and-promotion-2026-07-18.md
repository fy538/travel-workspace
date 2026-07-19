---
doc_type: working
status: active
owner: engineering / design
created: 2026-07-18
last_verified: 2026-07-18
expires: 2026-08-17
why_new: Records the post-implementation evidence pass across Vesper 255 Round 1 and names the remaining promotion gates precisely.
supersedes: []
source_of_truth_for: [wave-7-parity-evidence-and-promotion]
---

# Wave 7 parity evidence and promotion — 2026-07-18

## Outcome

Wave 7 converted several broad “device/accessibility evidence pending” notes into
repeatable registered evidence, repaired the capture harness that had made whole
surface runs unreliable, and found one real Booking truth-copy defect plus one
Costs persona-fixture defect. Both product defects are fixed.

No M01–M12 or S01–S02 row is promoted to `PARITY VALIDATED` in this pass. That
is deliberate, not a failure of the wave. The evidence now distinguishes what
is proven from the remaining real-backend, provider, accessibility, and
state-breadth work instead of treating all rows as generically open.

## What changed

### Current design evidence

- Booking now has current isolated Vesper 255 references for cancellation
  pending verification and unresolved participant consent. The older Booking
  family marker remains only as an L0 identity receipt.
- Trip Costs now points at a fresh capture of the current Costs canon rather
  than the older Vesper 155 fallback.
- External Sharing now has a registered design-reference manifest for both its
  owning canon and the Public Projection Contract companion.
- Design-reference validation passes for Booking (three pairs), Trip Costs
  (one pair), and External Sharing (two pairs).

### Booking durable-state evidence

- Added deterministic mock sessions and registered Maestro flows for:
  - cancellation pending provider verification;
  - unresolved participant consent with approved, pending, declined, reminder,
    requester, and blocked-confirmation truth.
- Both flows pass independently on iPhone 16 Pro / iOS 18.2.
- Device inspection found that a provider-confirmed booking undergoing
  cancellation verification still used pre-confirmation hero copy: “you’ll
  still confirm” and “handoff ready.” The hero now preserves original provider
  confirmation while explicitly naming pending cancellation verification.
- The cancellation recovery continues to state what changed, what did not, and
  exposes refresh only as a provider-status check.

### Costs evidence and fixture integrity

- The full registered Trip Costs surface run passes: five of five scenarios,
  including every declared crop.
- Captured states are return-planning estimates and ledger, live dense MXN
  ledger, empty planning ledger, completed settled ledger, and expense detail.
- The completed Elif Rome fixture previously carried expenses and memory but no
  formal trip/roster entry. The new trip-membership gate therefore rejected its
  device route even though unit-level expense derivation was coherent. The
  completed trip is now a first-class persona trip with Elif, Sarah, and Mike;
  a regression test locks Elif into its roster.

### External Sharing evidence

- Added and registered the terminal-unavailable public-story state.
- The full registered External Sharing run passes two of two scenarios:
  default public story and generic terminal-unavailable link.
- Unknown and terminal links visibly converge on the non-oracular generic copy.
  The forced network-error state remains explicitly open.

### Capture-harness repair

The runner’s direct AsyncStorage seed was not sufficient proof that the running
app had adopted a requested persona and frozen time. The readiness route now
applies both values through the app’s internal screenshot-mode path and verifies
the effective state before product capture. The runner also terminates the app
before writing its snapshot so shutdown cannot overwrite the new seed with the
previous run’s in-memory values.

This repair changed the Trip Costs result from zero of five captures to five of
five without weakening assertions or removing product states.

## Verification evidence

Backend:

- 182 Story, Invite, Proposal, Unpacked, projection-registry, and privacy tests
  passed.
- 158 Booking consent, trip archival, expense dispute, recorded payment,
  expense API, Receipt/OCR, masked-search, and masked-summary tests passed.
- The explicit PostgreSQL lifecycle subset passed 19 of 19 with no skips.

App and contracts:

- 17 focused Booking fixture, Booking composition, and persona-Costs tests
  passed.
- TypeScript passed with `tsc --noEmit`.
- Targeted lint passed; the only Booking warning is the existing file-size
  warning on `BookingSessionSurfaces.tsx`.
- Surface and scenario registries validate.
- Booking, Trip Costs, and External Sharing design-reference manifests validate.

Device:

- Booking cancellation pending: passed.
- Booking participant consent: passed.
- Trip Costs registered surface: five of five passed with all crops.
- External Sharing registered surface: two of two passed.

## Promotion decision by row family

| Rows | Evidence closed in Wave 7 | Still required before parity promotion |
|---|---|---|
| M01–M03 | Cancellation pending device composition; PostgreSQL/backend transition coverage retained; contradictory hero copy fixed | Real-provider cancellation walk; full cancellation state breadth; restart/replay device walk; large text and VoiceOver |
| M04–M05 | Complete mixed consent ledger fixture and device capture; PostgreSQL consent lifecycle | Full controller / organizer-non-controller / included / excluded / viewer device matrix; large text and VoiceOver; real-backend network-payload inspection |
| M06–M10 | Full current Costs surface capture; 158-test backend family includes disputes, payments, expense API, masking, and OCR | Explicit real-backend mixed-currency and payer/non-payer masked-view walks; accessibility matrix; payment-history/void device continuation |
| M11 | PostgreSQL archive lifecycle remains green | Registered blocked, archived, provider-recovery, and recovered device states plus accessibility walk |
| M12 | Backend OCR/privacy family remains green; current Costs baseline is stable | Registered upload, reading, long-scan, complete, partial, unreadable, manual-supersession, correction, save-failure/retry, and exact-return device states; large text and VoiceOver |
| S01–S02 | 182 projection/privacy tests; default and generic terminal-unavailable public-story captures | Forced network error; Invite and Unpacked device/card states; generic Proposal handoff device state; actor-selected Story/Unpacked controls; large text and screen-reader checks |

## Next wave

Wave 8 should be a narrow missing-state wave, not another broad refactor:

1. register and capture the Receipt/OCR state machine;
2. register and capture archive-blocked, archived-booking, and recovery states;
3. run real-backend actor walks for Booking controller/viewer and Costs
   mixed-currency/masking;
4. run large-text and VoiceOver checks on the durable-state specimens;
5. rerun the complete Booking aggregate surface after the repaired readiness
   harness, then promote only rows whose full matrix is attached and accepted.
