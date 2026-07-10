---
doc_type: contract
status: active
owner: engineering
created: 2026-07-09
last_verified: 2026-07-09
why_new: Consolidate cross-repo generation and rendering rules that previously existed only in a point-in-time audit.
supersedes: []
source_of_truth_for: [generated-content-boundaries]
---

# Content Generation — System Charter

## Purpose

Keep model-authored language useful without allowing it to become an unverified
operational fact, money amount, provider confirmation, or public claim.

## Owns

The cross-repo boundary between retrieved facts, model interpretation, rendering,
and correction. Domain systems still own their records and provider contracts.

## Invariants

- Facts come from typed records or cited retrieval. Generation may explain or
  interpolate them but must not mint availability, price, hours, confirmation IDs,
  weather, or transaction state.
- Money and public-share paths require explicit user or provider confirmation.
- Confidence changes presentation and actionability; low-confidence text cannot use
  the visual authority of a confirmed provider fact.
- Generated output has a surface-specific hard budget and a safe fallback.
- A user can correct or remove owned generated content, and the correction
  invalidates derived cards, stories, notifications, and shares.
- Public and group renderers receive only their privacy-safe projection.

## Failure posture

Missing grounding generalizes or omits the claim. Guard failure blocks or regenerates
according to the calibrated surface policy; logging alone is measurement, not proof
of safety. Provider uncertainty renders as pending, never confirmed.

## High-risk boundaries

Receipt OCR must not silently set a real expense; public stories must not publish
model-minted numeric facts; restaurant transcripts cannot manufacture confirmation;
narration and notifications inherit the same grounding constraints as visible cards;
cached lookup synthesis retains citations and expiry.

## Evidence and open decisions

The originating audit and its code-grounded follow-up are retained in the dated
archive. Unsettled policy questions remain classified `investigate`; this charter
records only durable constraints supported by the current product principles.

## Current risk register

- Output-guard escalation from measurement/log mode requires false-positive
  calibration; it is not a blind configuration flip.
- Curator and personal takes must receive the same place-fact grounding rule.
- Digest weather must join a real source or be omitted.
- Narration needs a documented spoken-length exception or a hard output clamp.
- Atlas LLM prose is a live surface and must satisfy grounding, correction, and
  restraint even when its authorship badge is honest.

The planning invariant is that a model estimate cannot populate quoted/provider
pricing without clear typing and rendering; point-in-time implementation findings
belong in archived evidence, not this contract.
