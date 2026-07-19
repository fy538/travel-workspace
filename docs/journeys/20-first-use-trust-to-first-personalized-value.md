---
doc_type: canon
status: active
owner: founder / engineering
created: 2026-07-18
last_verified: 2026-07-19
why_new: First-session consent, safety, and value are now a durable product lifecycle rather than incidental checks inside trip ideation.
source_of_truth_for: [journey-J20]
---

# 20 — First-Use Trust to First Personalized Value

## Product Promise

A new traveler can share only the context they choose, defer optional permissions,
and reach one grounded useful result without completing a personality quiz.

## Canonical User Story

As a new traveler, I want to understand and control what Vesper learns before I
see it personalize anything, so that the first useful moment feels earned.

## Starting State and Surfaces

- Signed-in first session; no committed trip or durable Atlas value.
- Routes: `/onboarding`, `/onboarding-safety`, Vesper Home, Trips Home, Atlas Home.
- J18 owns a signed-out invite detour; J01 owns trip ideation after first-use trust.

## Canonical Steps

1. Enter first-use setup and provide or defer optional profile context.
2. Set a private safety constraint and choose photo/location/push permissions.
3. Approve one grounded diary/photo recovery action, save a place, or begin a trip seed.
4. Reach the appropriate Home with that value visible and provenance intact.
5. Leave and return; choices and the value moment persist without duplicated prompts.

## Required Branches

| Branch | Path | Required evidence |
|---|---|---|
| `J20.B01` | Minimal setup with all optional fields deferred | `FE`, `VIS` |
| `J20.B02` | Private safety constraint persists without group leakage | `FE`, `BE`, `VIS`, `LIVE` |
| `J20.B03` | Photo/location/push denied without blocking value | `FE`, `VIS` |
| `J20.B04` | Recovery intake requires approval and records provenance | `FE`, `BE`, `VIS`, `LIVE` |
| `J20.B05` | Interrupted setup resumes exactly once | `FE`, `VIS` |
| `J20.B06` | First useful result returns on the correct Home | `FE`, `BE`, `VIS`, `LIVE` |

## Must Never Happen

- Optional permissions become mandatory.
- Raw photos or private constraints upload/share before approval.
- A skipped answer is presented as a learned preference.
- Resume creates duplicate prompts, trips, saves, or memories.

## First Automation Target

Ephemeral first-session fixture: deny every optional permission, save one grounded
place, restart, and prove Home shows the save while private/safety state remains private.

## Certification

J20 is certified across four independent layers:

- The frontend now stores a versioned 24-hour onboarding draft, restores the
  exact step and partial answers, serializes clear-after-save handoffs, and
  clears the draft when the traveler deliberately exits onboarding.
- Connected mock contracts prove optional fields stay absent, safety constraints
  persist privately, photo-derived recovery remains pending until approval, and
  one explicit venue save returns on Atlas Home without invented Travel DNA.
- The PostgreSQL scenario and `persona-cert:J20` repeat the private intake,
  approval provenance, and first grounded result against disposable users and
  clean up every fixture, so shared dogfood identities are never mutated.
- Maestro flow `67-journey-20-first-use-trust-value.yaml` visibly certifies exact
  resume, minimal deferral, photo/location denial, private safety persistence,
  recovery approval, and the first useful Atlas result. Push denial is covered
  headlessly because the OS prompt is session/device state rather than a stable
  screenshot fixture.
