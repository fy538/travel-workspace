---
doc_type: contract
status: active
owner: engineering
created: 2026-07-09
last_verified: 2026-08-28
why_new: Consolidate cross-repo generation and rendering rules that previously existed only in a point-in-time audit.
supersedes: []
source_of_truth_for: [generated-content-boundaries]
---

# Content Generation — System Charter

## Purpose

Keep model-authored language useful without allowing it to become an unverified
operational fact, money amount, provider confirmation, public claim, invented
memory, repeated user observation, unsolicited identity judgment, or synthetic
group meaning. This charter implements the product-level
[Vesper Editorial and Content Canon](../../travel-agent/docs/product/Vesper%20Editorial%20and%20Content%20Canon.md).
Evidence and human contributions reach generation only under the
[Contribution and Consequence Contract](contribution-and-consequence.md); an
editorially useful input is not automatically authorized for retention or
later inference.

## Owns

The cross-repo boundary between retrieved facts, known-to-person context, model
reconstruction and interpretation, rendering, and correction. Domain systems
still own their records and provider contracts; people remain authoritative
about personal meaning, and groups retain plural authored Outcomes.

## Invariants
- Ask, Point, Bring, audience, and action authority are resolved before
  generation. A composing model cannot grant retention, inference, audience,
  or action authority to its own output.

- Facts come from typed records or cited retrieval. Generation may explain or
  interpolate them but must not mint availability, price, hours, confirmation IDs,
  weather, or transaction state.
- Vesper-authored editorial generation starts from a contribution brief rather
  than directly from prose. At minimum, the composing path can identify evidence,
  what the person already supplied or received, prior exposure, the new claim,
  editorial operation, claim authority, audience, uncertainty, why now, visible
  grounding, expiry, and correction dependencies.
- Canonical state, operational instruments, and attributed human contributions
  are not automatically editorial content. Render each through its native owner
  and form; require an editorial contribution brief only when Vesper adds
  synthesis. Generated prose around another lane still inherits the canon.
- A paraphrase of the person's statement or prior Vesper output is not rendered
  as a new connection. Candidate selection must account for known-to-person
  claims without treating passive telemetry as proof of knowledge.
- Semantic receipt and exposure history remain distinct. Exposure may suppress
  an identical repeat but must not become evidence that the person understood,
  believed, valued, or remembers a claim.
- Generated content distinguishes occurrence record, model reconstruction,
  model interpretation, human-authored meaning, and operational consequence.
  The renderer may compress those labels; provenance may not collapse them.
- Unsolicited generated copy makes claims about evidence, events, Places,
  situations, mechanisms, and bounded relationships—not stable identity,
  emotional state, or what an experience meant to a person.
- Social synthesis preserves attribution and plural perspectives. A private
  signal may improve a minimum-safe group consequence but may not appear in its
  explanation; model prose must not impersonate human relational effort.
- Money and public-share paths require explicit user or provider confirmation.
- Confidence changes presentation and actionability; low-confidence text cannot use
  the visual authority of a confirmed provider fact.
- Generated output has a surface-specific hard budget and a safe fallback.
- Unit eligibility does not guarantee page admission. Composition accounts for
  marginal value, cumulative attention burden, and redundancy across subject,
  source, time horizon, operation, and expressive form; product moves are not
  content quotas.
- Value-bearing proactive content must be useful before requesting input. Chat
  may invite exploration; Home and Push must not use a reflection prompt to
  substitute for a missing contribution.
- Generated claims expose a proportionate trust footprint in the product while
  retaining full provenance for inspection and correction.
- Generated copy does not narrate that Vesper remembers, understands, is being
  restrained, or has kept a situation coherent. It renders the underlying state,
  effect, or contribution.
- Social projection must materially change understanding, possibility,
  coordination, or consequence. Otherwise omit it; when it changes another
  object, integrate attribution inside that object rather than creating a
  decorative social card.
- A user can correct or remove owned generated content, and the correction
  invalidates derived cards, stories, notifications, and shares.
- Public and group renderers receive only their privacy-safe projection.

## Failure posture

Missing grounding generalizes or omits the claim. Missing epistemic contribution
omits the editorial unit or falls back to an honestly labeled factual record;
it does not generate a question or personality read to fill the space. Guard
failure blocks or regenerates according to the calibrated surface policy;
logging alone is measurement, not proof of safety. Provider uncertainty renders
as pending, never confirmed.

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
- Trip Story Letter, Trip Story narrative prompts, `personal_insight`, and
  profile-insight extraction still encode a legacy character-read model. They
  are non-conforming migration surfaces under the Editorial and Content Canon;
  current existence is not approval for reuse.
- No shared runtime contract yet enforces the known-to-person check or the full
  editorial contribution brief. Until it does, prompt-level claims of novelty
  are not sufficient evidence of conformance.
- No shared composer yet enforces value-lane separation, marginal page
  admission, exposure lifecycle, or user-visible trust footprints. Individually
  grounded cards therefore remain insufficient evidence of a coherent Home.

The planning invariant is that a model estimate cannot populate quoted/provider
pricing without clear typing and rendering; point-in-time implementation findings
belong in archived evidence, not this contract.
