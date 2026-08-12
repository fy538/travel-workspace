# Personal memory and trust — compatibility charter

> Product status: Atlas retired; personal memory remains
> Canonical owners: You (controls), Vesper (governed use), Trips (history/story), Places (saves)
> Last updated: 2026-08-12

## Purpose

Personal memory is a private substrate, not a separate product destination.
People can inspect and correct the memory Vesper uses through deliberate **You**
controls. Trips owns trip history and story; Places owns saved places. Vesper
uses the resulting context to make the product feel coherent without narrating
surveillance back to the traveler.

The legacy `atlas` backend and mobile namespaces may remain only while data,
deep links, and individual controls are moved or retired. They must not regain a
home screen, a tab, proactive prompts, or a new product loop under a renamed
shell.

## Invariants

- Personal-memory claims are evidence-backed, inspectable, correctable, and
  reversible from a user-chosen control.
- Passive signals (dwell, private query content, and individual group votes)
  are never surfaced as personal claims.
- Memory improves Vesper's fit by default; explicit explanations appear only
  after a user action that asks for them.
- No new UI, journey, notification, background producer, or API is owned by
  “Atlas.”

## Preserved technical substrate invariants

Retiring the destination does not relax the data and control contracts below.
They remain owned by the memory/preference system; this charter names them so a
surface migration cannot silently discard them.

- Candidate fingerprints are deduplicated per traveler. A private candidate
  resolution is owner-checked and applied exactly once, including under
  concurrent retries.
- Forgetting a derived signal or deleting its source artifact revokes the
  linked observation and triggers memory re-synthesis. UI retirement must not
  leave a revoked signal eligible for Vesper context.
- Personal Memory remains versioned, append-only synthesis; hard constraints
  remain separately stored and binding. No surface writes the synthesized
  document directly.
- Hiding or restoring a timeline projection changes its visibility, not the
  underlying trip or kept-memory record. A removed-moments control must keep
  this distinction legible.

## Compatibility boundary

- Legacy Atlas URLs remain temporary deep-link bridges and need an explicit
  canonical destination plus a removal condition.
- Legacy Atlas read models may serve neutral You memory controls while they are
  being migrated. New app code must use the `you` route family and product copy.
- Data retention and deletion behavior remain intact; removing a surface never
  authorizes deleting a traveler's stored memory.

## Validation

The product proof is an intentional control loop: a person opens You, sees what
Vesper may use, corrects or forgets a claim, and receives behavior consistent
with that correction. This is a trust control, not a retention feed.

## References

- Product decision: [retire Discover and Atlas product surfaces](../decisions/2026-08-12-retire-discover-and-atlas-product-surfaces.md)
- Memory substrate: `travel-agent/backend/atlas/` and `travel-agent/backend/memory/`
- Technical owner: [Memory & Preference system charter](memory-preference.md)
- Mobile control entry: `travel-app/app/you/memory.tsx`
