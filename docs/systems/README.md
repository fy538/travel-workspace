# System Charters

A **System Charter** is a one-page, cross-repo contract for one product system. It
answers, at a glance: *what does this system promise the rest of the app, what does
it own, what must always be true, how does it fail, and is it ready for real users?*

## Why this exists (and how it differs from `FEATURE.md`)

We already have good per-module docs. This layer adds what they don't:

| Doc | Scope | Answers |
|---|---|---|
| `backend/<system>/FEATURE.md` | one backend module, **as-built** | "how is this built right now?" |
| `docs/architecture/*` | a design, **how** | "how should this work?" |
| `docs/product/*` | a thesis, **why** | "why does this exist?" |
| **System Charter (this)** | one system, **cross-repo + contract** | "what does it promise, own, guarantee, and how ready is it?" |

A charter is the **investigation and prioritization** surface. When we ask "are the
systems stable and correct?" we audit reality against the charter's **Invariants** and
**Public interface**. When we ask "what blocks first users?" we read the **Maturity**
column of the index below. Charters **link down** to the canonical `FEATURE.md` /
architecture / page-spec — they never restate them.

## Maturity tiers (the prioritization lens)

- **MVP-required** — a wedge journey cannot complete without it. Hardened to the
  Definition of Done before launch.
- **Should-have** — improves a journey; can be faked / manual-ed for the first ~10
  users.
- **Built-dark** — exists in code but flagged off in prod (our monetization /
  experience layer, validated later).
- **Future** — not started or no data model yet.

## Validation status (the stability lens)

- **wired+validated** — reachable on-device, walked end-to-end against live backend.
- **wired** — reachable, but not validated by a mock-walk / Maestro / live walk.
- **partial** — some paths wired, others stubbed.
- **dark** — built, flagged off.

---

## Master index

Surfaces follow `Feature-Map.md` (Vesper / Trips / Discover / Atlas / Cross-cutting).
Wedge journeys = the group-trip path (journeys 02 → 05). "Serves" cites
[`docs/journeys/`](../journeys/).

| System | Surface | Maturity (for MVP) | Status | Serves journeys | Charter |
|---|---|---|---|---|---|
| **Concierge (Vesper)** | Vesper | MVP-required | wired | 01,04,05,07,08 | [✎](concierge-vesper.md) |
| **Memory & Preference** | Vesper | MVP-required | wired | 04,11 | [✎](memory-preference.md) |
| **Trips / Folio** | Trips | MVP-required | wired | 03,06 | [✎](trips-folio.md) |
| **Planning / Itinerary** | Trips | MVP-required | wired | 05 | [✎](planning-itinerary.md) |
| **Proposals / Change Studio** | Trips | MVP-required | wired | 05 | [✎](proposals-change-studio.md) |
| **Group / Social state** | Trips | MVP-required | wired | 02,04,05 | [✎](group-social.md) |
| **Proactive / Notifications** | Vesper | Should-have | wired | 09 | [✎](proactive-notifications.md) |
| **Expenses / Settlement** | Trips | Should-have | wired (least hardened) | 10,12 | [✎](expenses-settlement.md) |
| **Discover** | Discover | Should-have | wired | 07 | [✎](discover.md) |
| **Atlas (memory & trust)** | Atlas | Should-have | wired | 11,12 | [✎](atlas.md) |
| **Places (hours/open)** | Trips | Should-have (support) | wired | 08 | [✎](places.md) |
| **Booking** | Trips | Built-dark | partial/dark | 10 | [✎](booking.md) |
| **Voice / Narration** | Vesper | Built-dark | dark | (deferred) | [✎](voice-narration.md) |
| **Postcard / Story** | Atlas | Built-dark | dark | 12 | [✎](postcard-story.md) |

> First users only require the **MVP-required** rows to be `wired+validated`.
> Everything else is `should`, `dark`, or `future` for launch.

---

## Release scope

The v1 flag manifest and DoD checklist live at
[`docs/working/mvp-scope-and-flag-manifest-2026-06-30.md`](../working/mvp-scope-and-flag-manifest-2026-06-30.md).
It is the authoritative record of what ships in v1, what is hidden, and
the remaining device-cert gates.

---

## Cross-cutting doctrines

Doctrines are not system charters — they own no tables, no routes, no UI component.
They answer one recurring judgment call that every charter faces, so individual
features don't re-derive the answer from scratch.

| Doctrine | Governs | Applies to |
|---|---|---|
| [Graph Legibility](graph-legibility-doctrine.md) | *"The model knows X — should we show that?"* Show vs. tell, keep-silent list, Atlas as the one mirror room, write-back tiers | Concierge, Memory & Preference, Planning, Proposals, Discover, Atlas — any surface that reads or writes the traveler/group world model |

---

## Charter template

Copy this for a new system. Keep it to one page; link, don't restate.

```markdown
# <System Name> — System Charter

> Surface: <Vesper|Trips|Discover|Atlas|Cross-cutting>
> Maturity (for MVP): <MVP-required|Should-have|Built-dark|Future>
> Status: <wired+validated|wired|partial|dark>
> Last updated: YYYY-MM-DD

## Purpose
One sentence. Link the thesis/belief it serves.

## Spans (cross-repo)
- Backend: `travel-agent/backend/<module>/` (+ FEATURE.md link)
- Frontend: `travel-app/app/...`, `components/...`
- Tables of record: <list>

## Public interface (what other systems may call / read)
- Inbound contract: endpoints + key entry-point functions others depend on.
- Consumes: what it reads from other systems.
- **Never**: things outside systems must not do (e.g. write its tables directly).

## Owns (source of truth)
The data/tables this system is the sole writer of.

## Invariants (must always be true)
The promises we audit against. Privacy, honesty, idempotency, ordering, etc.

## Failure modes
What it does when a dependency is down (degrade vs fail loud).

## Maturity & validation
- Serves journeys: <#s>
- DoD checklist state: <which of the 8 points are green>
- What's dark / flagged off.

## Canonical docs
- why → product/...   how → architecture/...   what(be) → FEATURE.md   what(fe) → page-spec
- Tests: <key test files>

## Open risks / known gaps
The audit-bait. Where this most likely breaks for a real user.
```
