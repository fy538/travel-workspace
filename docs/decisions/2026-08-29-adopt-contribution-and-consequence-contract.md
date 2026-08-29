---
doc_type: decision
status: accepted
owner: founder / product / architecture
created: 2026-08-29
decided: 2026-08-29
last_verified: 2026-08-29
why_new: Establishes one cross-repository contract for interpreting Ask, Point, Bring, retention, inference, audience, action, receipt, and correction without turning contribution into homework or memory into hidden person-level inference.
supersedes: []
source_of_truth_for:
  - contribution-gesture-defaults
  - contribution-authority-axes
  - contribution-consequence-treatments
  - source-bound-retention-default
---

# Adopt one contribution and consequence contract

## Context

Vesper's current canon already says to accept attention before organizing it,
deliver value before extraction, preserve provenance, keep shared experience
plural, and ask only at a material consequence boundary. The implementation,
however, contains two incompatible input philosophies:

- Intake v2 separates custody, observations, semantic candidates, truth state,
  retention, audience, action authority, and correction; while
- legacy Concierge memory prompts encourage immediate storage of preferences,
  personality insight, emotional investment, behavioral patterns, and silence.

The inconsistency becomes architecture-bearing when Chat, Home, Places, Life,
Occasions, and proactive behavior all depend on what an input was allowed to
become. A separate policy for every input surface would reproduce the same
problem in several forms.

## Decision

Adopt the cross-repository [Contribution and Consequence
Contract](../systems/contribution-and-consequence.md).

The primary distinction is the human gesture and immediate job, not whether the
input arrived as text, image, file, link, voice, or message:

| Situation | Default |
| --- | --- |
| **Ask** with no retention request | Use authorized continuity, answer, and create no new durable personal state |
| Explicit **Point** or clearly owned **Bring** whose consequence is private and reversible | Create only source-bound private state, deliver value first, then show quiet scope plus Correct/Undo |
| Ambiguous Place, time, owner, Occurrence, or Occasion | Keep the source under its custody policy and hold interpretation provisionally; ask only when resolution changes truth or consequence |
| Audience, affected-person, provider, spend, public, sensitive-inference, or weak-reversal boundary | Prepare privately and preview the exact boundary before crossing it |

Every contribution resolves five independent authority axes: **Use, Retention,
Inference, Audience, and Action**. Confidence may narrow behavior but never
expands authority.

## Product law

> **Create the smallest truthful object whose future consequences justify its
> existence.**

An answer may be complete without a write. A private Source or authored
observation may persist without becoming an Occurrence, preference, identity,
meaning claim, shared projection, or action. A material consequence is applied
only through its owning domain and leaves authoritative readback and repair.

The visible treatment set is deliberately small:

1. **T0 — answer or prepare privately:** no new durable personal state;
2. **T1 — apply privately, then receipt:** source-bound, reversible, and
   correctable; and
3. **T2 — preview the material boundary:** one prepared effect and one decision.

The more granular M0–M6 authorization modes remain internal policy and continue
to govern explicit language, affected principals, bounded mandates, external
action, and public consequence.

## Memory consequences

- Conversation content is not automatically permission to create memory.
- A question, ignored suggestion, non-response, dwell event, read receipt,
  individual vote, or inferred emotion does not become durable person-level
  preference or identity evidence.
- An explicitly authored preference or constraint may persist only with source,
  scope, truth type, authority, correction, and an honest receipt treatment.
- Repeated behavior may support a bounded hypothesis or an offer of a mandate;
  it cannot silently create a durable trait or grant autonomy.
- Personal Memory and group profiles are derived projections, not the authority
  that upgrades raw interaction exhaust into truth.

## Multiplayer consequences

- Authored material retains author and channel audience.
- Private derivatives do not inherit a shared audience merely because the
  source was shared.
- Minimum-safe private constraints may shape a shared consequence without being
  disclosed and without authorizing the consequence.
- Invitation, contribution, Decision, and public Place effects use their own
  owners, affected principals, and receipts.

## Implementation consequences

- Ordinary Chat, inbound Intake, Occasion contribution, correction, and
  proactive input must compile into the same storage-neutral contribution
  envelope before retention or action.
- Intake interpreters may propose candidates but cannot grant themselves
  effective retention, audience, or action authority.
- Legacy `observe()` and synthesis paths require a policy gate; prompt judgment
  alone is not authority.
- Corrections must invalidate dependent claims, projections, and pending
  consequences while preserving independently valid Sources and evidence.
- No database migration is authorized by this decision. Existing owners must be
  mapped first; the shared envelope is a boundary contract, not automatically a
  new universal table.

## Why this is inferred rather than benchmarked

A point-in-time comparison with current ChatGPT would mostly measure model,
account, connector, and memory configuration. A comparison with current Vesper
would mostly measure implementation lag after the pivot. The architecture is
instead derived from the representative fixture portfolio and the structural
value that disappears when only response prose remains.

Later human research may refine receipt prominence, correction language, and
whether scope is understood. It does not reopen the authority model unless
people materially misunderstand audience or real-world consequence.

## Revisit trigger

Revisit if the complete portfolio cannot be expressed through one envelope and
the five authority axes; if a class of private reversible contribution still
creates material surprise despite truthful value and legible repair; or if a
domain owner cannot support causal correction without a new shared authority.
