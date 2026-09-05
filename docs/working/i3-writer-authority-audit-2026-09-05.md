---
doc_type: working
status: active
owner: strategy integration / contribution and consequence
created: 2026-09-05
last_verified: 2026-09-05
expires: 2026-10-05
why_new: Maps the remaining background and reflection writers to the contribution authority contract before changing retention or inference behavior.
source_of_truth_for:
  - I3 writer-authority inventory and decision queue
depends_on:
  - complete-system-integration-roadmap-2026-09-05.md
  - i3-intake-format-and-custody-audit-2026-09-05.md
  - ../systems/contribution-and-consequence.md
---

# I3 writer-authority audit

This pass audits writers that can turn a conversation, source, behavior, or
generated synthesis into a durable observation or derived profile. It does not
delete writers or change retention semantics. The important distinction is
between a factual processing receipt, a low-weight derived signal, a personal
meaning claim, and an authored intention; the current code contains all four.

## Inventory

| Writer / path | Current input and write | What is sound | Decision or repair still needed |
| --- | --- | --- | --- |
| Explicit `observe()` / memory tool | Authenticated Chat tool path writes an observation when the user explicitly asks to remember/save; prompt rules now reject inferred personality, mood, silence, and unrequested booking preference writes | Explicit gesture, actor, source conversation, and existing observation owner are the strongest current retention path | Verify every non-Chat caller uses the same contribution decision; the model must not promote its own candidate or bypass correction/readback |
| Intake v2 contribution adapter | Custody-first source admission resolves an Ask/Point/Bring decision before source/derived work; unresolved shares can remain answer-only | Source custody and retained originals are separated from interpretation; unsupported formats fail closed | Finish native/relaunch evidence and keep source-only Life readback distinct from semantic interpretation |
| `preference_engine.edit_inference` | Committed catalog replacement evidence becomes a low-importance `source_mode="inferred"` observation with operation/transition provenance; ambiguous moves, titles, timing, and notes are excluded | Uses exact before/after catalog snapshots, idempotent receipts, a cap, and factual “swapped/added/removed” wording | Decide whether this is a processing signal only or may enter longitudinal Personal Memory; if it remains durable, expose source lineage, correction, expiry, and owner readback rather than treating it as stated taste |
| `core.personalization.discover_synthesizer` | LLM turns saves, dismissals, votes, and plan additions into 1–3 first-person observations (`source_mode="inferred"`) | Minimum signal count, category/importance validation, bounded output, and origin/session provenance exist; passive views are not included | A save/dismissal pattern is not an authored preference. Gate durable promotion behind an explicit policy/mandate or keep it session/Occasion-scoped; never let first-person generated prose masquerade as user-authored wording |
| `core.memory_signal` | Deliberate save/share/regenerate of a trip story writes a low-weight reflection observation; view/dwell is excluded | Deliberate engagement and low importance reduce noise; the write is best-effort and cannot break the primary action | “Shared” or “regenerated” is evidence of engagement, not necessarily that the trip’s experiences resonated. Reclassify as a derived interaction receipt or require a named interpretation policy before Personal Memory synthesis |
| Accommodation / planning reflection hooks | Tool and post-trip paths may create observations or synthesis input around supplied reservation/plan facts | Some paths are explicitly tied to a user action and preserve trip scope | Audit each call against booking-retirement and C&C ownership; a provider fact is not attendance, preference, or personal meaning |
| `refresh_memory` / Personal Memory synthesis | LLM composes a versioned personal narrative from observations | Existing source retrieval, versioning, and post-trip model policy provide a bounded derived projection | Treat output as generated projection, never canonical claim; ensure inferred observations retain labels and can be corrected/withdrawn without resurrecting stale prose |
| Group synthesis | LLM composes group material from scoped individual inputs and privacy gates | Group privacy omission and roster/source freshness checks exist | Keep authored social material and independent participation separate from generated group prose; no group profile should grant a writer authority over a person’s memory |

## Findings

1. **The repository has a real distinction, but not one universal writer gate.**
   Explicit Chat observation, source custody, inference workers, engagement
   signals, and generated profiles use related provenance vocabulary but do not
   all return the same Contribution Receipt or affected-projection list.
2. **The highest-risk path is first-person behavioral synthesis.**
   `discover_synthesizer` deliberately labels its writes as inferred, but the
   generated text is phrased as “I …”. That is useful for a provisional
   session overlay and unsafe as an unqualified personal truth.
3. **Factual edit inference is narrower than its destination.** Committed
   catalog replacement evidence is factual and bounded, but writing it into
   the same observation stream as explicit memory means downstream synthesis
   must preserve the source mode and importance or it can be over-read.
4. **Interaction telemetry is not meaning.** A trip-story save/share/regenerate
   is valuable product signal, but “this resonated” is an interpretation that
   should not be silently promoted to Personal Memory.
5. **The repair is not a new universal table.** Reuse the existing
   ContributionDecision/Receipt, source custody, observation provenance,
   learning-promotion gate, and canonical owner readback. Add a durable field
   only when a writer cannot satisfy correction, expiry, audience, or source
   lineage from those seams.

## Recommended implementation order

1. Add a writer inventory check to the contribution lane so every observation
   producer names gesture/input, source mode, canonical owner, audience, and
   correction path.
2. Keep `discover_synthesizer` and `memory_signal` derived and low-authority
   until the founder rules whether behavioral evidence may enter longitudinal
   Personal Memory. Do not rewrite their prompts in the held Chat lane.
3. Preserve `edit_inference` as a factual, low-weight processing signal while
   exposing its operation/transition lineage to readback and correction.
4. Audit accommodation/planning and post-trip reflection writers against the
   booking-retirement boundary and the distinction between provider fact,
   occurrence, intention, and meaning.
5. Add one cross-writer acceptance portfolio: explicit Keep, source-only Bring,
   behavioral signal, correction/release, group privacy, and generated
   synthesis. The expected result must identify the canonical owner and every
   invalidated projection without exposing private content.

## Current evidence state

This document is **implemented as an audit and decision queue**, not a claim
that every writer is conformant. The format/custody boundary is separately
locally tested in `i3-intake-format-and-custody-audit-2026-09-05.md`. The
remaining writer changes are decision-bound and should not be bundled into
Home/Places renderer promotion, Life internals, or Chat redesign.
