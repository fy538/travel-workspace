---
doc_type: working
status: active
owner: founder / product
created: 2026-08-07
expires: 2026-08-21
why_new: Records the implementation and live validation gates for the smallest zero-install distribution handoff derived from the Product Model and multiplayer strategy.
---

# Shared Plan Handoff — execution ledger

## Decision held constant

This implements one narrow part of the Product Model's distribution loop:

```text
organizer's local Plan → existing group chat → closed RSVP → organizer's Plan decision
→ lived experience → personal residue → a later organizer
```

The shared object remains a useful projection of a durable local Plan. It is
not a new social object, chat, poll, availability grid, membership grant, or
anonymous group identity. This follows the Product Model and the settled
multiplayer strategy boundaries.

## Implemented code layer

| Handoff step | Result | Evidence |
|---|---|---|
| Organizer shares a local Plan | Local Plans use a group-first “Share this plan” entry and a response-first OS share message. Travel invite behavior is unchanged. | app `374de8a5` |
| Non-user sees value first | A group, multi-use local Plan gets an intentionally narrow public response: title/destination/snapshot and aggregate RSVP totals only. | backend `c97d2e4f` |
| Non-user can respond | The public web page and installed app offer only `in`, `maybe`, or `out`; the response is explicitly not membership. | backend `eb8cd257`; app `374de8a5` |
| Privacy boundary | The public model excludes names, chips, free text, constraints, costs, itinerary detail, conversation, and rich plan preview. The audit event records only the closed RSVP value. | public-projection tests; external-sharing contract |
| Organizer can read the signal | The existing authenticated pending-invites row presents only the three aggregate counts; a response marks the row as engaged. | backend `014414aa`; app `ae75b6e4` |
| Measurement | `invite_loop_funnel.py` reports P0 shared links, P1 links with an RSVP, P2 aggregate current responses. It deliberately does not claim attendees, installs, or identity. | backend `50fef957` |

## Checks actually run

- Backend focused invite/public-projection suite: 199 passed for the organizer
  aggregate change; earlier public RSVP suites: 185 passed.
- App focused suite: 62 passed for RSVP, organizer display, and existing invite
  behavior; TypeScript typecheck passed.
- Contract snapshots and generated app types were regenerated and committed.
- External-sharing scenario registration and device preflight passed. The actual
  simulator mock-ready subflow stalled, so there is **no device-validation
  claim** for this change.

## Explicit next gates — not code-complete claims

1. **M1 device-real Friday night.** The roadmap's acceptance remains a founder
   using a local Plan with real venues and times while out. Run the real local
   Plan → group link → at least two zero-install responses → organizer review
   route on a device. Capture the normal Plan state before and after; do not
   call RSVP a commitment or attendance.
2. **Organizer resolution decision.** The anonymous aggregate cannot safely
   decide a Plan. The organizer should use the existing canonical proposal /
   Plan mutation path once they make a judgment. Do not build a “resolve
   RSVPs” action until product specifies whether the aggregate changes time,
   venue, capacity, or merely informs the organizer; those have different
   authority and evidence requirements.
3. **Participant residue and return.** Validate first that a participant can
   leave with an appropriate personal occurrence/artifact and later create a
   separate Plan. Do not mint follows, group membership, CompanionScope, or
   social graph data from a bearer-link response. That would violate the
   consented-edge sequencing in multiplayer strategy §9.

## Pilot readout

After the M1 run, use a single reporting window beginning at the first shared
Plan mint:

```bash
cd /Users/feihuyan/travel-workspace/travel-agent
PYTHONPATH=. ./.venv/bin/python scripts/invite_loop_funnel.py --since YYYY-MM-DD --json
```

Read P0–P2 as handoff health, then collect qualitative evidence separately:

- Did the organizer make a better or faster decision without a poll?
- Did anyone read RSVP as enrollment or feel pressured to install?
- Was the Plan actually used during the occasion?
- Did a participant later return for a personal Plan or residue surface?

No aggregate may be used to infer who attended, private constraints, or a
relationship edge.
