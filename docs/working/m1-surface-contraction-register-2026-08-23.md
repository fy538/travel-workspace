---
doc_type: working
status: active
owner: founder / product / architecture / engineering
created: 2026-08-23
last_verified: 2026-08-23
expires: 2026-09-22
why_new: Records the M-1 product-surface classification, safe presentation retirements, replacements, retained capabilities, and reintroduction gates after the August product pivot.
supersedes: []
promotes_to: null
source_of_truth_for: [m1-surface-contraction]
---

# M-1 surface contraction register

This register is the execution receipt for M-1. It classifies presentation
surfaces without confusing a route with a durable authority. Removing a screen
does not remove the domain writer, provider adapter, command, receipt, export,
or correction path that a retained journey still needs.

## Classification vocabulary

| Class | Meaning |
|---|---|
| `root` | Approved product doorway with viewer-relative entry and navigation. |
| `focused_workspace` | A durable job that needs sustained spatial or operational work. |
| `artifact_or_sheet` | A bounded, inspectable treatment rendered in context or expanded in place. |
| `external_handoff` | A provider, OS, or governed-link handoff whose truth returns through a receipt/status artifact. |
| `compatibility_redirect` | A safe deep-link/bookmark/recovery surface with no new product investment. |
| `retire` | Removed from active routes, QA, and design obligations; retained primitives must have another consumer. |

## Surface vocabulary state

Current runtime, compatibility ownership, and the shell hypothesis are distinct
claims:

| Layer | Current truth | Product rule |
|---|---|---|
| Visible runtime roots | **Plans**, **Vesper**, **Places** | Preserve current reachability and travel-wedge guarantees while broader composition is tested. |
| Pushed private owner | **You** | Owns portrait, people, privacy, correction, forgetting, account, and delegated-authority controls without pretending to be a fourth visible tab. |
| Compatibility vocabulary | **Trips**, **Discover**, **Atlas**, and historical deep links | May recover into Plans, Places, You, or another canonical reader; compatibility does not authorize renewed product investment. |
| Shell hypothesis | **Home**, **Vesper**, **Places**, **Life** | Home/Life remain separately testable hypotheses. Grammar or visual approval does not approve navigation cutover. |
| Focused workspaces | **Plan**, **Occasion**, **Map**, and structured provider/action flows | A durable or consequential job may expand without becoming another root. |

User-facing copy may call the current Trips route **Plans**, because a Trip is
the travel specialization of Plan. **Home** is reserved for the proposed
current-attention composition and must not silently become an alias for Plans.
**Life** is reserved for a Mine/Together continuity hypothesis; until approved,
You remains the production owner. An Occasion is a bounded shared world, not an
automatic destination or fifth root.

Home may replace the current Plans root only after active and upcoming Plan
reachability, deep-link recovery, offline behavior, and first-viewport clarity
are at least equivalent. Life may replace or evolve You only after Mine/Together
proves clearer than the existing portrait and controls without becoming an
archive, graph dashboard, or content feed.

## Disposition register

| Family / route | Product class | Replacement | Retained capability | Deletion / reintroduction gate |
|---|---|---|---|---|
| Plans, Vesper, Places | `root` | Current visible runtime roots | Viewer-relative projections, active-Plan reachability, and universal entry | Home-shell review plus active-Plan, offline, and deep-link parity |
| You | `focused_workspace` | Current pushed private owner; possible Life evolution | Portrait, privacy, people, correction, forgetting, account, and authority controls | Mine/Together review plus privacy/export/deep-link parity |
| Trip / Plan / Map | `focused_workspace` | Plan/Occasion workspace and spatial Plan face | Itinerary authority, revisioned mutations, route/transport truth | Projection parity and recovery/readback coverage |
| Proposal Detail (`/trip-proposal/[proposalId]`) | `compatibility_redirect` | Group-chat decision artifact | Proposal policy, voting, mutation, receipts | Chat focus, inspect fallback, and receipt readback coverage |
| Decision Deck gallery | `retire` | Typed chat/workbench artifact primitives and focused component tests | Deck primitives still used by Vesper workbench/chat contexts | Archive tag `m1-pre-contraction-2026-08-23`; zero route/QA/design references; reintroduce only for a retained artifact family that cannot be covered in context |
| Booking (`/booking/[sessionId]`) | `external_handoff` | Provider handoff/status artifact and external checkout | Provider adapters, task-scoped authority, reconciliation, ambiguous outcomes, receipts | Handoff return, ambiguous outcome, and receipt readback coverage |
| Expenses (`/trip-expenses/**`) | `compatibility_redirect` | Receipt/source-evidence artifact, or explicit founder-approved utility | Expense evidence, settlement authority, correction, export/deletion | Artifact replacement/readback or founder decision before further route work |
| Stay (`/trip-accommodations/**`) | `focused_workspace` | Plan-owned stay sheet | Lodging facts and provider return state | Stay-to-Plan projection parity |
| External sharing / public entries | `external_handoff` | Governed link/share handoff | Audience, custody, expiry, revocation, and recovery | Privacy, expiry, and deep-link recovery coverage |
| Atlas/Discover and other historical aliases | `compatibility_redirect` | Places, You, or the owning canonical reader | Bookmark recovery and canonical identity | Telemetry or explicit route-retirement decision |

## Execution status — 2026-08-23

- The app archive tag `m1-pre-contraction-2026-08-23` points to the
  pre-contraction app state and is published on `fy538/travel-app`.
- Product disposition fields now live beside the executable polish registry and
  the canonical entry-point inventory. Critical Booking, Expenses, and
  Proposal routes declare their replacement explicitly in route ownership.
- The Decision Deck gallery route, fixture, screen-specific QA flows, baselines,
  and gallery-only test were removed. The Deck component family and headless
  action tests remain because Vesper contexts still consume them.
- Proposal Detail remains a compatibility route and normal deep links already
  focus group Chat; inspect mode is a bounded recovery path.
- Booking remains a bounded utility during cutover, classified as an external
  handoff. Expense screens remain compatibility surfaces until an artifact
  replacement or founder-approved money-management decision exists.
- M-1 is closed. The route/classification guard is part of the reliability
  workflow, and the next milestone is the minimum command/receipt/delivery
  seam rather than another presentation-surface expansion.

## Safety rules

1. No M-1 presentation deletion removes a durable domain writer.
2. A retired class may not own a non-development production route.
3. Every retired family has a tombstone, replacement, retained capability, and
   reintroduction criterion.
4. New routes must name their product class before implementation and must not
   bypass the canonical command/receipt boundary.
5. The surface-contraction CI guard and generated route/design registries are
   the mechanical reintroduction check.
