---
doc_type: working
status: active
owner: founder / frontend / design
created: 2026-07-12
last_verified: 2026-07-12
expires: 2026-08-11
why_new: Turn the Motion Language migration into a repeatable release and review practice.
supersedes: []
source_of_truth_for: [motion-rollout, motion-release-review]
---

# Motion Rollout and Review

The motion canon is ready for normal feature work. It is not a one-time visual
cleanup: it remains a release concern wherever a person taps, enters a workspace,
opens a bounded presentation, waits for real work, or completes a consequential
action.

## What is already gated

- `npm run motion-governance` freezes the approved direct-Reanimated ownership,
  rejects raw ordinary timing literals, and requires the four bespoke sequences
  to declare Reduced Motion behavior.
- The normal app CI runs this guard alongside the sheet and local-button
  ratchets.
- The manual macOS `Mobile Stability Device` workflow can record the
  `decision-seal` ceremony and upload the frame/video artifacts.
- The pull-request template prompts for pattern, origin/dismissal, Reduced
  Motion, and composer/keyboard review when an interaction changes.

## Release gate for a motion-affecting build

1. `npm run motion-governance`, typecheck, and the relevant unit/smoke tests are
   green.
2. Normal and Reduced Motion are checked on a current iPhone simulator for the
   affected surface. For chat, this includes the keyboard-open state.
3. An interaction that presents a sheet, lift, or deck has a clear source and
   return path; no generic card occupies composer chrome.
4. Completion animation follows a real success boundary. A routine save, send,
   or navigation does not gain ceremony.
5. At least one physical device pass happens before external release for changed
   high-traffic surfaces or any keyboard/gesture-intensive behavior.

## Cadence

- **Every motion-affecting pull request:** complete the Motion & Presentation
  section in the PR template and run the smallest relevant simulator flow.
- **Before an internal dogfood build:** run the device workflow with completion
  motion QA enabled; inspect keyboard, Reduced Motion, and any changed overlay.
- **Before an external release:** repeat the affected flows on a physical phone,
  including interruption and low-connectivity behavior where relevant.
- **Monthly or after a major shared-primitive change:** review the four entries
  in `docs/systems/motion-exceptions.md`; absorb a routine exception into a
  shared primitive or remove it.

## Current rollout status

The Trips-between hero hold found during Phase 9 was resolved in the final
review: the surface canon is `TemptHeroFromSaves`, not `TripHeroCard`, and its
saved-destination extraction now uses the same city-or-name fallback as the
secondary taste rail. The full gate must remain green before declaring a build
release-ready.
