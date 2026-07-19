---
doc_type: working
status: active
owner: engineering / design
created: 2026-07-18
last_verified: 2026-07-19
expires: 2026-08-17
why_new: Records Wave 8 deterministic Receipt/OCR and archive/recovery device evidence, the QA-runner device-targeting repair, and the remaining parity gates.
supersedes: []
source_of_truth_for: [wave-8-missing-state-evidence]
---

# Wave 8 missing-state evidence — 2026-07-18

## Outcome

Wave 8 closes the missing mock-device specimen gap for the Receipt/OCR state
machine and the trip archive/recovery journey. Both are now registered surfaces,
run on an explicitly selected iPhone 16 Pro Max, captured in one complete run,
and visually inspected after route transitions settled.

The 2026-07-19 completion pass closes the locally verifiable interaction,
aggregate, authorization, and large-text gates. It does **not** claim hosted
Clerk two-account parity or real vendor OCR/provider execution: those require
external credentials/services. The accepted result is therefore specific:
durable product states, local real-backend policy, and mock-device interaction
are verified; hosted identity and vendor transport remain external gates.

## What changed

### Receipt/OCR durable-state entrance

The existing Add Expense screen now accepts a development-only state selector;
it does not create a parallel product page. The registered flow covers:

- uploading;
- reading;
- long scan;
- complete extraction;
- partial extraction;
- unreadable receipt;
- manual supersession;
- save failure with the receipt and edits retained.

The actual submit path now preserves the form and shows an inline retry message
when expense creation fails. Device inspection also found a real contradiction:
the recognized amount displayed `MXN 615`, but MXN was absent from the fixed
currency chips, so no currency appeared selected. A recognized currency that is
not in the default shortlist is now inserted at the front and visibly selected.

### Archive and recovery durable-state entrance

Trip Settings now accepts a development-only archive state selector and composes
the existing blocked sheet, archived settings shell, recovery sheet, and real
recovery action. The registered flow proves:

- provider work blocks archive and retains an exact continuation action;
- archived status is visible on the canonical settings screen;
- recovery names what returns and what remains closed;
- successful recovery returns to the canonical itinerary rather than a second
  recovery-only page.

### Capture-harness correctness

The polish runner previously displayed the requested `--device` name while
seeding, terminating, driving, and capturing the first booted simulator. With
two booted devices this silently attached to a concurrently controlled iPhone
16 Pro. Device-name resolution now tolerates `simctl` trailing whitespace and
passes the resolved UDID through storage seeding, app termination, readiness,
Maestro, and hierarchy inspection.

The two new flows also relaunch the app between durable states and wait for
navigation animation completion before capture. This removed intermittent home
screen failures and the visible sliver of the prior route that initially
appeared in screenshots.

### Design-reference honesty

Trip Settings lacked a registered reference manifest. Wave 8 adds an L0 family
marker exported from the current Trip Settings/Admin canon. It proves surface
identity and direction only; it is explicitly not pixel-parity evidence.

## Verification evidence

Static and unit evidence:

- TypeScript passed with `npx tsc --noEmit`.
- Focused Add Expense and Trip Settings suites passed: 40 tests.
- The broader focused pass, including the receipt long-scan hook, passed 43 tests
  before final capture polish.
- Polish scenario validation passed with 27 registered scenarios.
- Trip Costs and Trip Settings design-reference validation passed.
- QA runner files pass Node syntax checks.
- Targeted diff whitespace validation passed.

Device evidence, iPhone 16 Pro Max / iOS 18.2:

- Receipt/OCR final run:
  `travel-app/.maestro/runs/20260719T045833Z-trip-costs`
  — 1/1 capture, 7/7 extras, 2/2 crops, PASS verdict.
- Archive/recovery final run:
  `travel-app/.maestro/runs/20260719T045954Z-trip-settings-admin`
  — 1/1 capture, 3/3 extras, 2/2 crops, PASS verdict.

Completion-pass evidence:

- Receipt/OCR interaction run:
  `travel-app/.maestro/runs/20260719T053855Z-trip-costs`
  — 1/1 capture, 9/9 extras, 2/2 crops; includes typed correction and exact
  production back-return to Costs.
- Booking aggregate:
  `travel-app/.maestro/runs/20260719T054037Z-booking`
  — 11/11 captures with every declared crop present.
- Largest Dynamic Type, Booking consent:
  `travel-app/.maestro/runs/20260719T054609Z-booking`
  — 1/1 capture, 1/1 crop after making tall ledgers partially-visible rather
  than requiring an impossible 100% in one viewport.
- Largest Dynamic Type, archive/recovery:
  `travel-app/.maestro/runs/20260719T055331Z-trip-settings-admin`
  — 1/1 capture, 3/3 extras, 2/2 crops; the confirmation action is reachable
  through the new scrollable BottomSheet body.
- External Sharing recipient breadth:
  `travel-app/.maestro/runs/20260719T061253Z-external-sharing`
  — 6/6 captures: public story, disclosure-safe terminal state, retryable
  network state, valid Invite, generic Proposal handoff, and generic Unpacked
  authentication handoff.
- External Sharing owner controls:
  `travel-app/.maestro/runs/20260719T061947Z-external-sharing`
  — 1/1 primary capture, 2/2 focused action screenshots, and 2/2 crops after
  creating a real mock link through the production mutation.

Backend and static evidence:

- `make dogfood-journey-live-api`: 16/16 against real FastAPI/Postgres
  transport. The invite assertion now certifies the public projection itself
  and explicitly rejects leaked `id`, `trip_id`, and `created_by` fields.
- 14/14 focused controller/observer/provider and masked-expense authorization
  tests passed.
- Accessibility governance passed; no Dynamic Type disabling, text shrinking,
  or legacy Touchable regressions were found, and modal accessibility contracts
  remain present.
- Six focused frontend suites passed: 91/91 tests.
- Full polish/design-alignment test chain passed.

The run identifiers use UTC and therefore carry the following calendar date.

## Promotion decision

| Row | Newly accepted evidence | Still required before parity promotion |
|---|---|---|
| M11 | Archive/recovery interaction, 11/11 Booking aggregate, largest-text Booking/archive runs, real Postgres journey cert, and focused controller/viewer policy tests | Hosted two-account Clerk device walk and live provider execution |
| M12 | Full Receipt/OCR state machine, typed correction, exact return, static accessibility governance, and largest-text upload/read/review rendering | Live receipt upload/OCR vendor transport; hands-on VoiceOver rotor/navigation pass |

No other M01–M10 or S01–S02 row is promoted by this wave.

## Remaining external-only work

1. Run the hosted Clerk journey with two real accounts. Local TestClient and
   Postgres actor switching prove policy, but they do not prove JWT/OTP/session
   plumbing on Fly.
2. Execute a real provider booking and a real receipt upload/OCR response. Mock
   state breadth must not be relabeled vendor truth.
3. Perform a hands-on VoiceOver rotor/navigation pass. Static accessibility
   contracts and Maestro accessibility-tree selectors are useful evidence, but
   are not a substitute for operating VoiceOver.
4. Add the backend actor-permitted tokenized Unpacked projection. The new route
   is intentionally an authentication-only doorway and exposes no recap data.

Everything else in the prior local Wave 8 list is closed. The correct status is:
local product and policy evidence complete; hosted identity, vendor transport,
and manual assistive-technology validation remain external gates.
