---
doc_type: working
status: active
owner: founder / product / architecture
created: 2026-09-04
last_verified: 2026-09-05
expires: 2026-10-04
why_new: Investigates post-pivot surface contraction and plans bounded booking-execution retirement while preserving external reservation usefulness.
supersedes: []
source_of_truth_for: []
---

# Product surface contraction after the August pivot

## Status and recommendation

**Next execution sequence:** [§20](#20-next-execution-sequence--september-5-rebaseline)
extends this plan across booking presentation, arrangements/settings, assisted
expenses, Life's Atlas replacement, and reusable presentation. It maps those
changes to the active integration and Life roadmaps without reopening the
already-landed retirement guards. Start with the isolated SC-0 / SC-1a read
package described in [§20.12](#2012-active-lane-coordination-checkpoint).
Route, object-renderer and shared-contract changes have receiving owners; each
later cut depends on its named replacement, not a complete design freeze.

**Detailed implementation plan:** [§12–19](#12-capability-retirement-lane--detailed-plan)
turned the investigation into a bounded booking-retirement program. The first
implementation packages are now landed: scope adoption, static inventory,
server-side admission closure, shared Places resilience cleanup, and the
session-free venue continuation. The September 5 execution request authorizes
repository implementation and documentation, not production shutdown, external
actions, database deletion, or an unapproved shared-model change. The remaining
packages stay gated on the environment obligation audit and the explicit
Chat/Life lane boundary.

The subsequent [lightweight arrangements handoff](lightweight-arrangements-implementation-handoff-2026-09-04.md)
details the Plan/Occasion collaboration replacement, four complete situations,
inspected code seams, and keep/adapt/replace/retire sequence. Use it for that
lane; this investigation retains the wider booking and expense responsibility
analysis. Neither document authorizes deletion or claims runtime completion.

This is the research, recommendation, and bounded execution record for the
capability-retirement lane. It records the founder's September 4 direction and
a fresh inspection of the two repositories. It does not authorize production
shutdown, external provider actions, destructive data deletion, or claim that
the full replacement experience is complete. The exact landed revisions and
remaining gates are recorded in the [execution receipt](capability-retirement-execution-receipt-2026-09-05.md).

**Recommend retiring in-app booking execution, substantially reducing itinerary
and administrative presentation, and turning expenses into an assisted
capability with a small inspectable record.** Keep the four roots and invest
their design budget in delivering the differentiated product.

The August pivot broadened the human situations Vesper serves. It should also
reduce the number of separate software products Vesper attempts to operate.
Understanding someone's life, helping an evening work, and connecting people
and places do not require owning checkout, a travel editor suite, or a finance
application. Breadth of useful context does not require breadth of operational
responsibility.

There are three different decisions here:

| Decision | Meaning | Application |
| --- | --- | --- |
| Retire a responsibility | Stop promising and operating the capability; delete its dedicated implementation after obligations are accounted for | Provider checkout, holds, payment submission, automated reservation calls, cancellation/rebooking execution |
| Consolidate an interaction | Preserve the useful action with much less navigation, entry, and explanation | Expense capture/correction, changing dinner time, reviewing a shared decision |
| Retain dependable state | Keep records and calculations needed for the promised outcome even when they have no standalone screen | Commitment times, source evidence, membership, exact allocation, recorded repayment, local correction |

A smaller app cannot be achieved by moving every existing screen into a sheet.
Some responsibilities and branches must actually end. Conversely, replacing a
dependable calculation with generated prose would make the product less useful.

## 1. What the pivot established

The relevant evolution is visible in both documents and history:

1. **August 17:** backend commit `03f1053f6` explicitly made experience primary
   to itinerary. Its Product Model diff adds that planning is the commitment
   path through the model, not a prerequisite for participating in it.
2. **August 23:** the [lived-world identity decision](../decisions/2026-08-23-adopt-lived-world-product-identity.md)
   makes attention the doorway, people and the physical world the subject, and
   group travel the specialization. A useful response need not become a Plan.
3. **August 23:** the [surface contraction register](m1-surface-contraction-register-2026-08-23.md)
   classifies Booking as external handoff and Expenses as compatibility. It
   nevertheless explicitly preserves provider adapters, reconciliation, and
   domain writers. This was presentation contraction, not capability retirement.
4. **August 28:** the [four product moves](../decisions/2026-08-28-adopt-four-product-moves.md)
   establish Make sense, Open possibility, Help it work, Carry forward. Practical
   relief can be complete value; every feature does not earn its own product.
5. **August 29–September 1:** contribution, expression, and four-root contracts
   distribute value across Home, Chat, Places, and Life. The [August 31 editing research](ai-native-effortless-editing-and-composition-research-2026-08-31.md)
   specifically argues for touching the visible object, expressing a change
   naturally, and receiving a localized result without schema or form labor.

The current [Product Thesis](../../travel-agent/docs/product/Product%20Thesis.md)
says infrastructure providers supply coverage, routing, inventory, and execution.
The [Product Model](../../travel-agent/docs/product/Product%20Model.md) defines a
Plan as the minimum useful prospective structure and distinguishes a reservation
from occurrence and personal meaning. The [Architecture Principles](../../travel-agent/docs/product/Product%20Architecture%20Principles.md)
require deterministic arithmetic and state transitions beneath model judgment.

These support substantial contraction. They do not establish that every
existing domain implementation must survive indefinitely.

### Why the code still feels like the earlier product

The [Booking Product Strategy](../../travel-agent/docs/product/Booking%20Product%20Strategy.md)
already diagnosed overbuilt infrastructure in July and moved to capture first.
However, it says to freeze rather than demolish the infrastructure and keeps
flight transactions, hotel merchant operations, and automated calls as later
options. Those are future obligations that this new direction can explicitly
remove.

The current [HPL program](home-places-life-productization-program-2026-09-04.md)
puts compatibility retirement after internal cohort acceptance. That order is
appropriate when removing an old reader whose retained job still needs a
replacement. It should not prevent earlier retirement of a capability we decide
to stop offering. Otherwise we keep paying to polish, test, and maintain a
product we no longer intend to launch.

The [release manifest](../release/v1-scope.yaml) already excludes live booking
transactions from v1. Moving from dark/deferred to retired would be a stronger,
longer-term scope decision. The [generated release contract](../release/v1-scope.md)
must be regenerated from that manifest, not edited directly.

## 2. What exists in the code

Inspected root HEAD `6c53cc5`, backend HEAD `f7fb3ff71`, app HEAD `ff6d0e2b5`.
All three were on `main` and clean at the initial inspection. This investigation
did not start the API, contact booking providers, inspect production accounts,
or establish whether historical external obligations exist.

The following physical line counts come from tracked source files. They include
comments and blank lines, exclude tests, and measure selected families rather
than the full dependency graph. They are maintenance-footprint indicators,
**not deletion estimates or evidence of user adoption**.

| Selected family | Files | Lines | What the boundary includes |
| --- | ---: | ---: | --- |
| Backend booking | 58 | 15,305 | Python under `backend/booking_agent/` |
| App booking | 10 | 4,701 | `app/booking/` and `components/booking/` |
| Backend expense helpers | 6 | 1,214 | Python under `backend/expenses/`; excludes substantial API/DB code |
| App expenses | 16 | 4,876 | `app/trip-expenses/` and `components/expense/` |
| Backend itinerary core | 45 | 23,112 | Python under `backend/core/` with `itinerary` in the path |
| App itinerary components | 53 | 12,049 | `components/trip-itinerary/` and `components/trip-plan/`; excludes the main route and hooks |

Notable individual route files:

- [Booking session](../../travel-app/app/booking/[sessionId].tsx): 1,487 lines;
  offer comparison, selection, cart, checkout consent, held price, cancellation,
  reconciliation, group consent, recovery, and return navigation.
- [Trip plan](../../travel-app/app/%28tabs%29/trips/[tripId]/plan.tsx): 2,066 lines;
  multiple presentations, day navigation, review, movement, map face, operational
  changes, restoration, and connection to newer Plan/Occasion projections.
- [Changes](../../travel-app/app/%28tabs%29/trips/[tripId]/changes.tsx): 331 lines;
  canonical operation history, seen state, and recovery navigation.
- [Permissions](../../travel-app/app/trip-settings/permissions.tsx): 599 lines;
  shared editing, ownership, delegation, expense/booking initiation, voting,
  auto-resolution, booking autonomy, and group-room behavior controls.
- Expenses has **five routes**: list, add, detail, edit, balance. The add sheet
  still exposes title, amount, currency, category, date, payer, participants,
  split method, optional block association, note, and privacy.

The [surface registry](../../travel-app/scripts/polish-qa/surfaces.mjs) calls
Booking `external_handoff` and Costs `compatibility_redirect`, but still
registers extensive booking and expense design/capture obligations. The Costs
route is an actual interactive ledger, not an implemented redirect. Product
classification alone has not reduced the implementation.

## 3. Booking: end execution ownership, retain external reservation usefulness

### Recommended retained experience

Vesper should help select a suitable place, explain practical fit, provide a
useful external booking or contact link, understand a supplied confirmation,
and use that evidence to help the subsequent experience work.

Example target behavior:

> This restaurant fits the evening and has the access information you need.
> Open the restaurant's booking page. When you provide the confirmation,
> Vesper can connect its time and location to the evening and help you arrive.

An external link need not create a BookingSession, a Trip, an itinerary day,
a shopping cart, or a follow-up task. A chosen responsibility such as “I will
book for us” can be recorded when it helps the people involved; merely opening
a link should not assign responsibility or imply a reservation.

The source may support a scheduled reservation, amount, terms, or contact
information. It does not prove current provider status, attendance, refund, or
payment between friends. Read-only tracking can remain a separately justified
capability when a reliable source exists. Importing a flight ticket does not
by itself provide live flight status.

### Retire from the product direction

- Multi-provider booking sessions and cart/checkout presentation.
- In-app order creation, hold placement/settlement, and payment approval flows.
- Automated restaurant reservation calls and their normal launch roadmap.
- Vesper-operated cancellation/rebooking execution and manual operator queues
  once any actual outstanding obligations are resolved.
- Provider-specific traveler/passenger/payment forms and booking autonomy
  settings whose only purpose is this execution stack.
- Credential/readiness/canary and launch requirements for retired providers.
- Future merchant-of-record or booking-revenue assumptions that keep these
  systems on the product roadmap.

Retained commercial links can remain simple links where useful. They should
not cause a new comparison, attribution, insurance-upsell, or marketplace
project merely to justify the existing code.

### Dependencies that prevent a blind directory deletion

| Existing seam | Finding | Disposition |
| --- | --- | --- |
| Places HTTP resilience | `backend/places/base.py`, `google_places.py`, and `foursquare.py` import retry/circuit-breaker code through Booking; the primitives already live in `backend/core/resilience.py` | Redirect imports and relocate only any surviving generic wrapper; do not create another utility subsystem |
| API lifecycle | `backend/api/lifecycle.py` registers expiration, session dispatch, checkout reconciliation, and session reaping; normal startup starts these unless API background tasks are disabled | Remove retired runtime registrations as well as UI entry points |
| Worker runtime | `backend/workers/booking_jobs.py` and `audio_jobs.py` can recover pending sessions independently of the API dispatcher | Audit all schedulers, registered functions, and queued jobs |
| External capture | `backend/workers/inbound_jobs.py` calls booking attribution; link capture also uses booking event storage | Preserve useful import/provenance and disentangle it from session commerce |
| Reservation attestation | `backend/core/booking_attestation_gateway.py` records user-reported handoff completion with a block/actor boundary | Preserve the evidence distinction; simplify or replace the Trip requirement when an actual consumer needs it |
| Transport and older workbench | `concierge/tool_handlers/transport.py` and `home/vesper_workbench/route.py` import booking provider types/runtime | Decide which read-only capability survives; do not retain the graph just to preserve imports |
| Expense and accommodation | Expense API reads offers; stay/cost and cancellation projection link old booking records | Retain history or migrate references without requiring new BookingSessions |
| Navigation | Chat cards, notification routing, universal search, trip settings, details, and the legacy venue screen open the booking route | Replace destinations, tool results, and action descriptors together |

There is already a useful separation: [the itinerary-committed subscriber](../../travel-agent/backend/booking_agent/subscribers.py)
deliberately does not start booking. Retiring execution need not destroy planning.

However, the old venue screen's `startBooking` requires an itinerary ID and
creates a session even for `L1_links`. That is a concrete example of structure
required by the implementation rather than by the person. The entity lane
should receive this dependency finding; it does not need a redesign in this
research task.

“Dark” is not proof that no work remains. Before decommissioning, perform a
read-only inventory of nonterminal sessions, holds, checkout/cancellation
claims, restaurant attempts, queued jobs, and provider sagas in the relevant
environment. Distinguish fixtures from real obligations. If none exist, proceed
without inventing a production observation period. If some exist, support that
finite set through resolution rather than retaining a general booking product.

## 4. Itinerary: retain useful temporal structure, reduce the planning suite

The user still benefits from seeing when dinner is, what is fixed, what is
optional, how places connect, and who is joining. An itinerary can be an
excellent visual output. It should not become the required grammar for
participating in Vesper or a detailed workspace every user must manage.

### Target presentation

One focused Plan/Occasion view, composed from:

- fixed commitments and supplied reservation/ticket evidence;
- flexible intentions and a small useful sequence;
- the relevant people and shared expectations;
- practical movement and material dependencies; and
- contextual change and inspect actions.

“Dinner at 8, perhaps a walk beforehand” should be a complete useful Plan.
Empty hours are not missing work. A detailed multi-day schedule should remain
available when requested, without forcing the same editor density onto a
Saturday evening. This is a product recommendation, not a claim that these
postures are fully implemented today.

### Prune or consolidate

- Full block-entry and advanced edit workflows as the default route to change.
- Separate generic Changes destination as a normal navigation obligation;
  show a relevant delta and local Undo, with history available from its owner.
- Dedicated technical recovery/operation presentations for ordinary edits.
- Parallel-plan construction controls before a split/rejoin is actually useful.
- Repeated details, stay, people, and administration destinations that expose
  the same owner with slightly different forms.
- Booking-specific operation branches after booking execution is retired.

Keep direct manipulation where it is faster: tap a time to change it, inspect
the ticket, move a stop, compare two alternatives. Natural language handles
compound intent such as “make tomorrow lighter and keep the dinner.” Forcing
every simple correction through Chat would replace tap labor with prompt,
latency, and verification labor.

### Keep the authority that remaining behavior needs

The canonical operation/commit path, revision checks, participant ownership,
history, and exact repair still serve shared planning. They prevent one person's
private change from silently changing everybody's evening. A local schedule
change must not imply that an external reservation changed.

New architecture still relies on old itinerary truth:

- [Trip adapter](../../travel-agent/backend/domains/experience_graph/trip_adapter.py)
  explicitly preserves the Trip/block as execution authority and projects a
  linked Commitment into the newer graph.
- [Home source discovery](../../travel-agent/backend/root_projection/v2/source_contribution_trip_evidence.py)
  reads latest-revision blocks explicitly recorded as happened/skipped.
- [Situation envelope](../../travel-agent/backend/lived_experience/situation.py)
  permits a missing `plan_ref`, which is compatible with broader situated help;
  that type alone does not establish a complete non-Trip runtime.

Therefore reduce presentation first, then remove unreachable operation families
and migrate necessary authority deliberately. Do not build a second generic
Plan engine merely to rename the old one. Retaining today's itinerary owner
does not commit us to preserving all 23,112 lines of the audited core forever.

## 5. Permissions and change management: smaller visible choices

The permission page currently combines governance for several mini-products.
Deleting booking responsibility removes entire choices such as who may start
booking work and how much booking autonomy Vesper has.

For retained shared activity, show understandable controls near the effect:

- who is invited and who sees this;
- who is organizing or allowed to change shared arrangements;
- what Vesper is handling for this occasion; and
- how to stop, correct, leave, or revoke it.

Default policy should cover ordinary participation. A material change should
make its affected people and effect clear once. Detailed thresholds and generic
governance matrices do not belong in ordinary onboarding or a Plan's main view.
The [Contribution and Consequence contract](../systems/contribution-and-consequence.md)
already supports explicit language, narrow mandates, quiet reversible receipts,
and proportionate previews.

Private context, shared visibility, permission to change a plan, and permission
to incur cost remain distinct internally. Simplifying visible choices must not
make the model invent consent. Global account, privacy, deletion, and mandate
controls still merit discoverable durable access.

## 6. Expenses: AI can carry the work; a ledger carries the numbers

The opportunity is larger than a chat wrapper over Add Expense. Receipt
understanding can support several jobs without turning each receipt into a
shared debt:

| Job | Value | Minimum supporting state |
| --- | --- | --- |
| Understand a receipt | Explain the total, included service/tax, or a visible line item | Source plus extracted amounts and uncertainty; no ledger required |
| Remember practical facts | Re-find the restaurant, ticket, cost, or date inside an episode | Retained Source and allowed owner links |
| Understand spending | Summarize recorded costs or compare a stated budget with known commitments | Explicit coverage, currency basis, recorded facts versus estimates |
| Share a cost | Allocate a known payment among the right people | Authorized payer, participants, amount/currency, allocation and owner |
| Close out | Explain the remaining balance after recorded repayments/refunds | Deterministic ledger and inspectable payment/correction history |

This can work for dinners, shared groceries, weekends, hosting, and trips. It
does not require general personal finance, bank synchronization, categories the
person must maintain, or payment rails. The current implementation remains
Trip-scoped; a non-Trip expense owner is a design/engineering gap to resolve
through existing Occasion/Commitment boundaries, not a shipped capability.

### Current strengths

- [Receipt extraction](../../travel-agent/backend/expenses/receipt_ocr.py) already
  uses vision to extract merchant, date, currency, total, tax, tip, and items.
  It directs the parser to omit unreadable values.
- [Settlement](../../travel-agent/backend/expenses/settlement.py) is deterministic
  and accounts for shares and recorded payments. Existing corrections and
  voiding preserve history.
- [Conversational handlers](../../travel-agent/backend/concierge/tool_handlers/expenses.py)
  exist for log, summary, and settle, and are exposed as `expense_log`,
  `expense_summary`, and `expense_settle` through the tool dispatcher/catalog.
- Existing review/correction, membership, idempotency, and currency machinery
  can support a lighter product without being redesigned as prose.

### Current gaps that block simply deleting the forms

1. `expense_log` assumes the **caller paid**, accepts no participant selection,
   and splits among **all Trip members**. It rejects non-equal allocation.
2. The tool has no equivalent of the complete receipt/source attachment and
   payer/allocation control available to the form. The selected capability
   bundle is a linked-Trip ledger capability.
3. Existing Chat tools do not provide complete parity for exact correction,
   refunds, partial repayment recording, or voiding a mistaken payment.
4. The tool schema's top-level description still says exact/percentage splits
   are stored but not applied, while its enum and implementation now only
   support equal splits. The replacement needs one truthful capability contract.
5. [Accommodation auto-cost](../../travel-agent/backend/expenses/accommodation_cost.py)
   creates a settleable expense from a stated cost and payer, splitting a shared
   stay among all Trip members. That exception needs an explicit policy decision
   when distinguishing source capture from authority to allocate group debt.
6. [Currency conversion](../../travel-agent/backend/expenses/exchange_rates.py)
   retains a `1.0` sentinel when no rate is available. A streamlined experience
   must expose unresolved conversion and exclude unsupported converted totals
   from definitive settlement. Less visible UI makes reliable admission more
   important; it does not justify a confidently generated number.

### Recommended target interaction

For explicit input, such as “I paid $126 for dinner; split equally between me,
Maya, and Theo,” Vesper should resolve the people, use deterministic allocation,
and show one compact result with $42 each, payer and audience, plus correction.
Whether that result is applied or previewed follows the existing authority
boundary; the product should not ask the person to repeat already clear facts.

For a receipt alone, first deliver what can be understood. Retain it privately
when the Bring contract allows. Prepare a shared allocation only if requested
or covered by an explicit narrow standing instruction. A receipt cannot establish
who should pay, whether someone was a guest, or who attended.

If a useful statement would allocate debt but one material fact is missing, ask
that fact alone. Do not ask for merchant/category/date/Plan again when already
supported. Do not create a queue of speculative costs the person must clean up.

Correction should stay local: “Theo did not join dinner,” “that includes the tip,”
or “I sent Maya $20 back.” Show precisely what changed in the allocation or
recorded payment. An externally sent payment is a recorded report unless a
separate payment source verifies it; Vesper has not moved money.

### Target interface footprint

Use compact amount/allocation and balance compositions, a reusable focused
inspection/correction treatment, and deliberate historical retrieval. Retire
the five-route expense product after its promised common actions have a working
replacement. Dense groups may still warrant expanding the same balance
composition; a larger viewport does not require a second money workflow.

Home can show a useful completed answer or a material unresolved consequence;
Life can retrieve the supporting receipts in the occasion/journey; Chat can
take input and corrections; Places can use permitted cost/access information
where it helps a decision. None needs a permanent Expenses module.

## 7. How the four roots become more focused

| Root | What becomes stronger after contraction | What should not move there |
| --- | --- | --- |
| Home | Useful interpretation, possibility, and the next practical consequence; occasional concise cost or commitment readback | Booking dashboards, receipt-entry queues, every missing itinerary field |
| Chat | Natural requests, directed import, compound changes, exact corrections, compact results | All state hidden in transcript, a requirement to describe visible selections again |
| Places | Spatial context, fit, access, routing, useful external continuation | A universal booking marketplace or Trip/day selection before opening a provider |
| Life | Re-finding episodes, people, Plans, tickets, receipts, and supported history | An archive of every operational status or a finance administration center |

Plans and Occasions remain focused destinations when spatial or temporal
overview is useful. The separate entity lane owns its reader implementation.
This research proposes the integration boundary and does not modify Chat,
Life, or entity source code.

## 8. Scrutinize design burden with the right test

The need for good frontend design is intrinsic to this product: Home and Places
must make sophisticated intelligence understandable and worth attention. That
investment is valuable. The failure is requiring a new visual system and
lifecycle for every backend capability.

A new dedicated surface should earn its cost by doing a job that cannot be
handled well by an existing root, object, reader, or focused interaction:

1. Does the user need a stable spatial or temporal overview?
2. Are several items easier to compare or manipulate simultaneously?
3. Is a durable record necessary for independent inspection and correction?
4. Would conversation impose more expression, waiting, or verification work?
5. Is the underlying responsibility actually part of the product we want?

Evaluate total user work, reachable states, duplicate implementations, required
fields, navigation hops, and maintenance obligations. Route count alone is a
poor target: compatibility URLs may be cheap, while one enormous sheet can
hide several products' worth of complexity.

## 9. Recommended engineering sequence

### A. Make the scope decision concrete

Record retirement of provider transaction execution; identify retained
reservation evidence, external handoff, practical planning, and bounded expense
help. Update active strategy and release owners so new work does not rebuild
what this decision removes. Historical decisions remain historical.

Move capability retirement ahead of the HPL cohort dependency. Replacement
coverage still applies to useful actions we keep. Do not require every old
checkout or editor feature to reach parity in the new app.

### B. Decommission booking as a complete subsystem change

1. Inventory live obligations and all creation/dispatch paths read-only.
2. Redirect Places to existing core resilience and identify retained capture/read helpers.
3. Remove new provider execution entry points across API, tools, workers, and
   mobile actions; preserve finite recovery if actual obligations require it.
4. Replace session-shaped handoff with a useful direct external continuation
   and source-backed reservation reading.
5. Delete checkout/session UI and unused execution, saga, provider, scheduler,
   webhook, canary, configuration, and test branches once remaining consumers
   and obligations are accounted for.
6. Regenerate schemas, mobile types, operation policy, route/design registries,
   and release documentation. Retain necessary historical read/export access.

### C. Simplify the Plan experience over its existing authority

Design the compact Plan/Occasion composition, local changes, and inspect/history
access against ordinary evening, upcoming trip, live disruption, and shared
split/rejoin situations. Replace the main editor presentation and its common
entry paths. Then prune unused operation families, duplicated readers, and
provider-only branches. Keep Home/Places integration work moving against the
same owner contracts.

### D. Complete assisted expense behavior and remove the form suite

Unify receipt and language input into typed expense commands with exact payer,
participants, supported allocation, source identity, and correction. Keep
arithmetic, repayment, and refund truth deterministic. Add the compact result
and inspection treatment, then retire obsolete routes and dedicated component
flows. Resolve non-Trip scope deliberately; do not require a fake Trip for a
dinner simply to reuse the old tables.

### E. Reduce administration and the acceptance footprint

Delete controls belonging to retired capabilities. Consolidate remaining
occasion access and delegation; preserve account-level controls. Remove obsolete
QA/design obligations instead of merely reclassifying the screen. Verify
critical retained behavior in its new location, along with deep links, history,
correction, and multiplayer boundaries.

Packages C and D can proceed independently once retained ownership and action
boundaries are agreed. This is a system contraction program, not a requirement
to finish one behavioral proof before working on another root.

## 10. Documents to change if this recommendation is adopted

| Owner | Required change |
| --- | --- |
| Product Thesis / Model / Vision & Scope | Make provider execution boundary explicit; keep broad experience and practical assistance; distinguish retained itinerary authority from default editor UX |
| Booking Product Strategy | Replace freeze-and-eventual-launch with retirement, capture, handoff, and narrow read-only capabilities |
| Monetization Strategy | Remove dependence on future transaction execution/merchant operations; keep any useful external referral optional |
| Surfacing Strategy and August 23 contraction register | Separate responsibility retirement from presentation migration; remove blanket retention of every provider writer |
| Booking / Planning / Expenses system charters | Record retained owners, finite legacy obligations, simplified interactions, and the actual retired branches |
| HPL productization and broader system build plans | Front-load scope subtraction and remove obsolete delivery/acceptance work |
| Release manifest, API operation policy, mobile surface/route registry | Reflect real capability removal and surviving destinations mechanically |
| Trip itinerary, Costs, Booking, settings contracts | Replace old screen-level parity obligations with the intended retained experience |

## 11. Verification and limits

The investigation used source inspection, route/caller/import tracing, selected
tracked-source counts, current canonical documents, and relevant August Git
history. It did not perform visual QA or a full runtime walkthrough.

Ran the existing offline expense split-contract and settlement-property suites:
**71 tests passed**. This corroborates the current equal-only Chat contract and
the value of retaining tested deterministic computation. It does not establish
the proposed assisted expense experience, complete production money correctness,
or production booking retirement readiness.

The main unknowns for implementation are actual outstanding provider
obligations, the final minimal Plan composition, non-Trip cost ownership, and
the common expense actions that should remain supported. None requires
continuing to polish booking checkout while the product boundary is decided.

## 12. Capability retirement lane — detailed plan

### 12.1 Outcome and scope

**Vesper helps the experience work around a reservation; it does not operate the
reservation business.** The package removes transaction ownership and its
administrative burden while keeping external continuation, source-backed
understanding, practical assistance, correction, and historical access.

This is a finite cross-repository engineering program, not another product root
or permanent architecture lane. It is subordinate to existing Source, Place,
Plan, Occasion, Commitment, contribution, and privacy authorities.

| In this lane | Not independently owned here |
| --- | --- |
| Booking execution retirement across entry points, tools, jobs, providers, and mobile controls | Plan/Occasion structure, collaboration, participation, and general itinerary redesign |
| Replacement external continuation and reservation-evidence interface | Life corpus/lens/dossier design or a new reservation inbox |
| Booking-specific dependencies in receipt, stay, cost, history, and privacy paths | Expense product redesign, allocation policy, or ledger replacement |
| Bounded caller changes agreed with the affected surface owner | Broad Chat redesign or changes to entity-page composition |
| Removal of obsolete booking claims, QA, configuration, and operational requirements | Subscription billing/IAP, ordinary microphone/voice capabilities, map routing, general Source intake |

Expenses need an explicit implementation owner through the orchestrator. The
arrangements handoff itself excludes a broad expense redesign; do not interpret
adjacency as permission for either lane to change shared debt semantics.

### 12.2 Updated evidence from the fork investigation

The review recovered parent Strategy turns from September 4, approximately
16:10–23:57 UTC, including publication cleanup, HPL planning, the founder's
surface-contraction request, the five design handoffs, and parallel-lane scoping.
It also traced relevant document history from August 14 onward. This is not a
claim to have reread every document in the three repositories.

Fresh inspection adds these corrections to the earlier inventory:

- The selected `backend/booking_agent/` path's latest Git change was August 10;
  the three-week product pivot did not retire that package.
- A static scan of the committed full OpenAPI snapshot found **44 operations
  whose paths contain `booking` or `provider-sagas`**: 39 active, four retiring,
  one dark under the current API policy/defaults. This deliberately includes
  retained reads and one expense operation, excludes other differently named
  paths, and is neither a complete execution inventory nor a deletion count.
  Registry `active` is not evidence of live provider permission or adoption.
- API startup dispatch is not the only route: the independent worker resumes
  pending booking sessions at startup and every minute; itinerary held-order
  confirmation has a separate provider executor and scheduled-task handler.
- Places imports through a booking compatibility module, but retry and circuit
  breaker primitives are already core-owned. Fix the imports rather than
  duplicating the library.
- The legacy venue path creates an `L1_links` session and requires an itinerary.
  The concierge's ordinary L1 path avoids a session but can stamp a handoff
  actor and emit a receipt. These are distinct caller behaviors to replace.
- The global mobile return-catch prompt is actually mounted in `app/_layout.tsx`.
  Link taps can create device-persisted claims and a later “Did you get it?”
  sheet. This behavior must retire alongside execution-oriented navigation.
- Manual attestation currently requires a current Trip block already marked
  `handed_off` and an assigned actor/controller. It cannot unchanged serve an
  independently imported reservation with no Trip or prior Vesper handoff.
- Life refinding reads `booking_offers` joined to `booking_sessions`. Account
  deletion preserves/minimizes shared external obligations. Both are migration
  consumers, not evidence that execution must remain a product indefinitely.

The [V2.3 interaction report](claude-design-interaction-kernel-lab-v2-3-arrangements-execution-report-2026-09-04.md)
already explores F3, the external-reservation journey, and identifies non-Trip
attestation as an open interface question. Its scripted checks are design-time
evidence, not real extraction, participant validation, or native acceptance.
The [Home/Places response](claude-design-integration-2026-09-04/01-home-places-response.md)
also states that returning from a provider marks nothing. Use those proposals
as design input, not as production implementation or automatic canon adoption.

The fork investigation ran the following offline suites: **60 passed**.

```bash
cd travel-agent
./.venv/bin/pytest -q tests/core/test_resilience.py \
  tests/booking/test_provider_resilience.py \
  tests/booking/test_capability.py tests/life/test_refind_sources_unit.py
```

These validate existing reusable behavior only. No deployed-provider inventory,
live integration, retirement migration, or native acceptance was performed.

## 13. Experience decisions to settle before replacement implementation

The recommended decisions below define the intended behavior. CR-0 records
their adoption and exact contract mapping; this working plan does not silently
change canon or authorize a new table.

### D-1 — External continuation is navigation, not an assignment

Use the existing Place/object or answer to expose a supported provider URL,
website, or contact action. Prefer ordinary language such as “Reserve on their
site” or “Open airline.” Do not require Trip/day/participant/session selection.

Opening and returning must not create a Plan, booking claim, reservation,
shared responsibility, debt, or reminder. Preserve origin and return context.
Optional product telemetry must remain distinct from personal or shared truth.
Do not replace the retired return-catch sheet with another default completion
prompt. Existing device claims should be cleared by a narrowly targeted local
migration, not interpreted as current intent.

“I'll book dinner for us” is a separate explicit contribution. The Plan/Occasion
lane owns any useful responsibility it establishes; no provider executor follows
from that statement. A failed external link offers a supported website/contact
fallback, not an invented URL or a Vesper checkout fallback.

### D-2 — Understand reservations made anywhere

Support a confirmation brought independently of Vesper navigation. The minimum
experience is useful explanation and retrieval even without a Trip or Plan.

Reuse custody-first Intake, Source identity, exact subject resolution, and
owner-bound claims. Do not create a new universal reservation store, dual-write
legacy inbound rows, or manufacture a hidden Trip. Identify the current writer
for each retained fact before introducing any new record.

Keep these operations separate, even if they feel like one fluid interaction:

1. Receive and inspect the source under its permitted use.
2. Retain supported evidence when authorized.
3. Associate with a place and, optionally, a prospective owner.
4. Apply an arrangement/Commitment consequence only through its owner.
5. Share only the information authorized for that audience.

Clear existing context should avoid re-entry of facts. Ambiguous repeated
reservations, people, dates, or owners must not be guessed merely to eliminate
a question. Ask only the fact whose ambiguity would change a consequence.
The source can remain privately useful while that association is unresolved.

Audit actual supported input formats and forwarding behavior. A design that
shows a PDF, ticket pass, or email does not establish decoder/delivery support.
Do not make this retirement package implement every possible import format;
name the supported acceptance formats and preserve honest fallback behavior.

### D-3 — Evidence, intention, and current provider status remain distinct

| Material | What it can support | What it does not establish |
| --- | --- | --- |
| Provider link | A place to continue externally | Reservation, assigned booker, or availability |
| “I booked dinner at eight” | Attributed user-reported reservation facts | Independent provider confirmation |
| Supplied confirmation | Facts stated in that source, with its issue/observation time | Ongoing monitoring or guaranteed current provider status |
| Authorized supported provider read | Bounded current status at the checked time | Future status or permission to execute a transaction |
| Agreed meeting time | Human arrangement/Commitment truth | An externally changed reservation |
| Recorded reservation | A planned/provider dependency | Attendance, enjoyment, or shared expense liability |

Use plain source attribution and relevant uncertainty rather than a dashboard
of technical statuses. Preserve these distinctions in typed contracts and tests.
Receipt identifiers and private continuation URLs must not become ordinary
group-visible Place facts.

### D-4 — Reconcile changes without operating the merchant

Use F3 and [arrangement scenario S4](lightweight-arrangements-implementation-handoff-2026-09-04.md#s4--a-consequential-change-while-people-are-already-moving):
the provider's updated evidence says 8:30, while the shared arrangement still
says 8:00. Show the relevant mismatch, useful arrival/adaptation assistance,
and a narrow authorized way to coordinate. Vesper does not silently move the
shared time, cancel the earlier booking, contact the merchant, or claim a refund.

Correcting or withdrawing a Source invalidates dependent claims/projections;
it does not cancel an independent reservation or erase an accepted agreement.
Reversing a local association is not Undo for an external purchase or message.

### D-5 — Retain only justified provider reads

Treat live availability, transport inventory, and ongoing monitoring as separate
scope decisions. For each existing adapter, name an accepted consumer, supported
operation, data freshness, operational cost, and owner. Default this package to
external links and supplied evidence where that is enough; do not activate dark
providers, acquire credentials, or retain a multi-provider offer marketplace
to avoid making a decision.

An existing useful availability read can survive after being separated from
session/cart authority. Keep routing, reachability, practical transport advice,
and place intelligence on their own merits. Imported flight evidence alone
must never imply live flight tracking.

### D-6 — Preserve access, not the obsolete application

Old receipts and deep links should reach an authorized read-only record or an
honest explanation when the record is unavailable. Historical cards must not
invoke retired commands. Do not redirect every old URL to Home and call that
successful recovery; preserve exact subject and context where possible.

Legacy confirmed, cancelled, unknown, and user-reported states must not all
migrate to “booked.” Keep privacy, export/deletion, source lineage, and useful
history while retiring execution. Retention policy is separate from service
shutdown; no arbitrary permanent retention or bulk data deletion is implied.

## 14. Dependency-ordered engineering packages

| Package | Result | Depends on | Can proceed beside other lanes? |
| --- | --- | --- | --- |
| CR-0 | Adopt scope and owner/interface decisions | This investigation and current canon | Yes; short coordination points only |
| CR-1 | Reproducible dependency and obligation inventory | CR-0 scope; environment identified for runtime audit | Yes; source audit needs no design freeze |
| CR-2 | No new booking execution can enter or restart | CR-1; finite recovery policy if obligations exist | Yes; does not require complete Life/Plan redesign |
| CR-3 | External continuation and reservation evidence work coherently | CR-0 interface decisions; existing owner support | Yes; coordinate shared files and contracts |
| CR-4 | Retained readers and legacy links no longer need execution | CR-1 inventory and CR-3 required replacements | Yes; narrow Life/Plan/Entity integration |
| CR-5 | Delete obsolete execution, UI, jobs, and operations footprint | CR-2; CR-4 coverage; obligations resolved or safely isolated | Yes; serial landing for shared registries |
| CR-6 | Validate and release the contracted capability set | CR-2–CR-5; exact three-repo revision set | Separate from full HPL promotion |

After CR-0/CR-1, admission closure and replacement experience can advance in
parallel. Do not wait for a complete four-root launch to stop unwanted work.
Conversely, do not remove a retained reader before its replacement is usable.

### CR-0 — Scope adoption and contract alignment

Tasks:

- Record D-1–D-6 as accepted, amended, or unresolved with a named owner. Table
  design, shared model changes, and tuned prompt edits require the repository's
  explicit approval boundaries before implementation.
- Amend the existing strategy/system/release owners listed in §18. Distinguish
  permanent retirement from deferred or flag-gated exposure; do not infer
  retirement of every external action from retirement of booking execution.
- Separate HPL compatibility-reader retirement from this responsibility
  retirement. Retained HPL navigation/rollback requirements remain intact.
- Agree the minimal contract with Life and Components and Plan: source identity,
  optional owner association, authored/reported truth, relevant timestamps,
  visibility, correction, canonical readback, and destination. These are
  requirements on existing contracts, not authorization for a universal DTO.
- Agree a finite list of supported input formats and acceptance situations.

Exit: every retained responsibility has an owner; every removed promise has
an explicit disposition. No new screens or schema are justified solely by the
old implementation's existence.

Commit unit: shared scope/contract amendments. Avoid sweeping concurrent
arrangement or entity edits into that commit.

### CR-1 — Inventory before shutdown

Create a bounded retirement inventory in this document's execution ledger or
an attached machine-readable report if needed by tests. Reuse the method-aware
API policy and existing route/job inventories; do not build a general capability
management platform.

Inventory rows should name: entry point, caller, owner, side effect, retained
consumer, environment exposure, disposition, dependency, and deletion criterion.

Source inspection must cover:

- `backend/api/routes/booking.py`, `admin_booking.py`, `booking_webhooks.py`,
  `booking_confirmation_landing.py`, and `itinerary_operations.py`.
- Concierge schema/catalog/dispatcher/booking handlers and prompts that promise
  execution; `search_transport` and older Home/workbench consumers.
- API lifecycle, `core/event_subscribers.py`, independent worker functions and
  cron registrations, provider checkout tasks, itinerary provider outbox/sagas,
  cancellation/restaurant reconciliation, expiration, projection retries.
- Mobile booking route/components/data hooks, Chat card actions and ordinary
  link instrumentation, global return-catch, venue entry points, notifications,
  search destinations, permission controls, and route generators.
- Life refinding, booking coverage, captured costs, accommodation and expense
  joins, confirmation sharing/revocation, account export/deletion, membership
  transfer, and historical data constraints.
- Provider canaries, cancellation-review monitoring, deploy configuration,
  readiness gates, dependency manifests, fixtures, and QA design obligations.

For each relevant runtime environment, produce an **aggregate, read-only**
obligation report with counts and restricted identifiers for nonterminal
sessions, external order references, holds, ambiguous checkout/settlement,
cancellation claims, active restaurant attempts, provider sagas, queued tasks,
undelivered receipts/refund projections, and shared historical references.

Do not use mutation-oriented `claim_*`, reconciliation, recovery, or startup
functions for this audit. Use explicit read-only SQL/queue inspection, without
logging tokens, passenger details, payment payloads, or confirmation secrets.
Distinguish fixtures, sandbox orders, and real external obligations using
evidence; an empty local database does not certify production. Account for
in-flight work by rechecking after admission closes in CR-2.

Exit: no execution path or retained dependency is unclassified. Unknown external
obligations remain a concrete blocker to destructive shutdown, not a reason to
keep accepting new work. Source-only inventory can finish while environment
access remains unresolved.

Commit units: pure audit/tests; then the redacted inventory and dispositions.
Do not commit private runtime records.

### CR-2 — Close admission and preserve only required recovery

Tasks:

- Reject new session creation, checkout/holds/payments, restaurant contact and
  retry, and provider-changing itinerary commands. Remove agent discovery of
  retired tools/promises in the same package; guard stale/replayed calls too.
- Enforce retirement at server/domain dispatch boundaries, not only mobile
  flags. Any temporary transition control must fail closed and have a removal
  criterion; do not introduce a permanent matrix of booking rollout flags.
- Prevent queued-but-unsubmitted work and recovering workers from starting a
  new provider effect. Revalidate at dispatch immediately before any external
  effect. Recheck inventory after closure for requests already in flight.
- Distinguish definitely unsubmitted work from ambiguous submitted work. Never
  mark an unknown payment failed to make the queue empty. Never automatically
  cancel an existing reservation as part of cleanup.
- If obligations exist, bound recovery to that identified legacy set and retain
  necessary authenticated callbacks/read reconciliation/projection delivery.
  Isolate any operator-authorized liability-reducing action from new execution.
  If no obligations exist, omit the recovery tail rather than inventing one.
- Define old-client behavior: authenticated retired mutations return a stable
  unsupported-capability response with appropriate continuation guidance.
  Resolve exact HTTP/status mapping against existing error conventions. A
  retirement response must not leak another user's record existence.

Exit: direct HTTP, stale cards, tool invocation, worker restart, queue replay,
and itinerary commands cannot create new booking effects. Required legacy
recovery still works, or the zero-obligation report justifies removing it.

Commit units: admission and negative tests; worker/outbox closure; bounded
recovery handling only if necessary. Do not deploy a state where a worker can
still dispatch newly admitted work through an overlooked path.

### CR-3 — Build the small retained reservation experience

Tasks:

- Reuse existing supported URLs and external navigation, preserving canonical
  subject and exact return context. Do not persist a commercial session merely
  to render a link. Keep private provider/account links owner-scoped.
- Remove the default return-catch interaction and its link-tap claim producers;
  migrate only its exact local storage key. Other saved material stays untouched.
- Map ordinary supplied confirmation and explicit user-report cases through
  existing Intake/Source and typed owner commands. If a non-Trip owner seam is
  absent, specify and approve the narrow extension before building it.
- Provide compact evidence/readback and exact correction through existing
  artifact/object treatments. Private source retention, arrangement association,
  and telling other people remain separate effects.
- Handle independently purchased bookings, duplicate imports, corrections,
  insufficient evidence, and confirmations with no prospective container.
- Integrate a changed-source mismatch with the arrangement owner, without
  copying shared time into a second authority or executing a provider change.
- Selectively adapt accepted read-only capabilities under D-5. No dark provider
  activation, new integration, mailbox scanning, or generalized monitor work.

Exit: the complete external journey works without a booking session or fake
Trip; not supplying a confirmation creates no homework; supported evidence has
canonical readback and useful retrieval.

Commit units: backend contract/commands and tests; synchronized schema and app
data bridge; reusable rendering/navigation; bounded caller adoption. Detailed
visual composition stays with the dedicated design tool and relevant surface
owner; native QA remains required for changed UI.

### CR-4 — Migrate retained readers and compatibility paths

Tasks:

- Redirect Places to the existing core resilience primitives. Move only a
  surviving generic decorator if needed; retain appropriate retry semantics.
- Replace execution-package imports in retained Source/capture/availability
  helpers with their proper existing owners. Do not leave a new package that
  simply copies the booking subsystem under a different name.
- Decouple Life refinding and retained stay/cost/receipt views from execution.
  Initially use an explicit bounded legacy read adapter if data migration is
  unnecessary; require a removal/retention decision rather than indefinite
  compatibility by accident.
- Preserve source identities, record timestamps, actor/audience boundaries,
  cancellation/unknown distinctions, expense links, and correction lineage.
  No broad backfill or silent inference of attendance/payment is authorized.
- Route historical booking URLs/cards/notifications to the exact authorized
  evidence reader where possible. Missing/deleted records get honest recovery;
  unsupported actions must not bring back checkout.
- Preserve confirmation-share revocation and export/deletion behavior. If old
  public links exist, maintain their exact audience/expiry guarantees during
  migration or deliberately revoke under an approved transition policy.
- If a data migration is needed, specify a dry run, explicit target set,
  before/after counts, idempotency, transactional behavior, backup, rollback,
  and failure handling. Schema changes require approval and Alembic discipline.

Exit: every retained consumer has an implemented owner/read path, and historical
truth survives without general-purpose booking execution. Cross-lane owners
review their affected contracts before shared-file landing.

Commit units: shared import cleanup; bounded read adapters; consumer/deep-link
migration; approved data migration separately if necessary.

### CR-5 — Delete the obsolete footprint

Only after CR-2/CR-4 and the obligation decision:

- Delete unused session/cart/checkout/hold/restaurant-contact presentation and
  associated actions, mocks, hooks, and dedicated forms.
- Delete execution graph/provider mutation branches, unused provider adapters,
  expired transition guards, scheduled handlers, recovery consumers no longer
  needed, provider callbacks, and operator APIs/scripts for retired work.
- Remove booking-specific initiation/autonomy/consent settings while preserving
  ordinary Plan editing, privacy, sharing, and scoped AI authority.
- Remove obsolete canaries, SLA monitors, readiness requirements, credentials
  references, and dependency packages only after checking non-booking consumers.
  General API/worker/voice processes must remain intact.
- Update tests and QA registry to reflect the retained product. Delete tests
  whose sole subject is a retired behavior; preserve or move boundary tests that
  protect retained evidence, arithmetic, privacy, and history.
- Handle operational shutdown and provider-secret removal through an explicitly
  approved deployment step. Local code deletion does not certify external
  infrastructure has stopped.

Do not rewrite old Alembic history or drop historical tables just to achieve a
zero-match search. Any remaining compatibility storage/reader must be named,
non-executing, and governed. Commit history preserves removed source code;
there is no need to keep dead implementation under an archive module.

Exit: no live consumer, runtime registration, app control, launch gate, or future
roadmap promise depends on retired execution. All intentional historical
exceptions and remaining obligations are explicit.

Commit units: mobile removal; backend deletion; operations/dependencies; generated
registries/QA cleanup. Keep each repository's working state testable and stage
only named files.

### CR-6 — Verify, deploy, and record closure

Verification covers §16 plus API/type parity, privacy, account lifecycle,
retained source/cost reads, worker startup, and native visual/interaction QA.
Run broad local suites to distinguish existing baseline failures from changes;
no newly introduced failure is accepted as legacy debt without evidence.

Deploy order:

1. Ship backward-compatible retained reads and admission closure. Old clients
   cannot start retired work; required historical access stays usable.
2. Replace/remove affected mobile actions and verify old-client/stale-card
   responses alongside the new external journey.
3. Confirm closed admission and inventory again across deployed worker/API
   versions, in-flight work, queues, and callbacks.
4. Resolve or isolate the finite recovery tail; then remove no-longer-needed
   execution jobs, endpoints, provider secrets/config, and old code.
5. Perform approved historical-data migration/deletion separately if needed.
6. Record exact backend/app/workspace revisions, deployed versions, evidence,
   retained exceptions, and closure in §19.

Rollback restores necessary readers/presentation without reopening retired
execution. A general HPL flag rollback must not resurrect checkout or the
global return-catch behavior. Do not use a blind checkout of a pre-retirement
server revision as the operational rollback plan.

The three Git repositories cannot publish atomically. Keep the cross-repo
contract set coherent, update any revision lock only to verified child commits,
and distinguish local completion from deployed retirement. No push or deployment
is authorized by this planning document.

## 15. Cross-lane contracts and coordination

| Lane | Agreement needed | Work this lane must not duplicate |
| --- | --- | --- |
| Entities | Supported external action destination; private versus public URLs; exact origin/return; old venue booking caller replacement | Entity identity, full page composition, research pipeline |
| Components and Plan | Optional association; imported provider facts versus shared agreement; explicit booker contribution; changed-reservation mismatch; receipt/readback | New PlanItem model, editing grants, RSVP/attendance, general itinerary rewrite |
| Life | Source-backed reservation retrieval; exact legacy links; cancelled/unknown history; minimal legacy adapter if needed | Corpus architecture, lenses, dossier anatomy, Everything Kept |
| Contribution/Chat | Existing supported import/report/correction paths; stale tools/cards; no return-catch or automatic assignment | New Chat root or parallel intake implementation |
| Home/Places delivery | Useful practical readback and changed evidence; external continuation; no generic booking coverage homework | Generation/ranking system or root redesign |
| Expense owner via orchestrator | Preserve existing cost/refund evidence and unresolved legacy liability; agree replacement read contracts | Assisted-expense scope, new debt, allocation/settlement redesign |

Concurrent edits currently touch product/collaboration canon, root contracts,
and entity handoffs. Before each substantive package, refresh branch/status
and document revisions in all affected repositories. Coordinate exact files,
not merely broad lane names. Land generated schemas and shared registries
serially to avoid overwriting another lane's contract changes.

No full design freeze is required. CR-1 and shared import analysis can proceed
immediately after execution authorization; CR-2 depends on retirement scope and
obligations, not Life composition. Non-Trip association in CR-3 waits only for
its exact owner contract, not the entire Plan design.

## 16. Acceptance portfolio

The portfolio tests the whole retained responsibility across roots. It is not a
single-loop product gate. The rows below are planned tests, not passing receipts.

| Case | User-visible result | Required negative assertion |
| --- | --- | --- |
| R1 Ordinary dinner, no Plan | Open a supported restaurant link; return to the same Place/context | No session, Trip, assignment, confirmation, follow-up queue, or shared write |
| R2 Independent confirmation | Bring a supported confirmation made elsewhere; understand and refind it | No prior Vesper handoff or fake Trip required; no inferred attendance |
| R3 Explicit user report | “I booked for eight” stays attributed and correctable | No fabricated provider verification or payment evidence |
| R4 Shared change | Provider evidence moves to 8:30 while friends still have 8:00; show useful mismatch and authorized coordination | No silent shared-time overwrite, provider change, or read/silence-as-consent |
| R5 Missing or conflicting evidence | Useful partial readback; one consequential clarification if needed | No guessing repeated venue/date/owner; no mandatory filing wizard |
| R6 Trip ticket and stay | Existing confirmed/cancelled/unknown material remains readable in the right context | Import is not live tracking; historical reservation is not proof of occurrence |
| R7 Correction and withdrawal | Dependent views/readers update; independent arrangements survive | No deleted source resurrection, automatic external cancellation, or cross-viewer leak |
| R8 Legacy client/card/link | Authorized record opens or precise unsupported recovery appears | No stale action can recreate a session or reach provider execution |
| R9 Restart and queue replay | No new external effect; bounded known recovery only if needed | API, worker, saga, and callback paths cannot reopen admission |
| R10 Account/member lifecycle | Retained shared evidence remains safe; private data and revoked access disappear correctly | No orphan obligation, exposed passenger/confirmation data, or broken deletion/export |
| R11 Retained cost truth | Existing expense/refund links remain inspectable and deterministic | No fabricated repayment/refund or automatic shared debt from a new capture |
| R12 Sparse/offline/provider failure | Cached evidence is useful and dated; external failure has honest fallback | No synthetic availability, “done” before readback, or retry into retired execution |

Testing layers:

- Pure unit checks for evidence distinctions, resolver behavior, shared
  resilience, expired/unsupported actions, and deterministic mapping.
- Endpoint and command tests with provider-effect spies proving zero new
  create/pay/hold/cancel/contact calls across every retired entry point.
- Real-Postgres tests for retained history, account lifecycle, idempotency,
  correction, concurrent admission closure, and any approved data migration.
- Worker/scheduler registration and restart tests, including queued work from
  an older deployment and late callbacks where a recovery tail exists.
- Mobile interaction tests for link-only behavior, return context, no global
  follow-up prompt, stale cards, and old/new destination handling.
- Native QA through the existing registered-surface workflow for phone sizes,
  large text, loading/offline/error states, back navigation, and account switch.
- Controlled supported-format capture tests and any permitted read-only provider
  integration. Do not create a real order merely to test retirement.

Source inspection and Jest/pytest do not establish native acceptance or
production shutdown. Preserve that distinction in every execution receipt.

## 17. Validation and completion measures

For backend API/model changes, use the workspace workflow in the same logical
package:

```bash
./scripts/sync-types.sh
make contract-check
make typecheck
```

The default sync is offline. Do not start the API merely to generate a schema:
lifespan and worker startup can dispatch real work. Review full snapshot,
derived mobile snapshot, generated types, API-operation policy, and surviving
callers together. Never hand-edit the generated artifacts.

Documentation changes should run metadata, inventory, link, and relevant
release/canon checks. UI changes follow child-repo intake and registered native
QA. Implementation receipts record exact commands, revisions, failures, and
baseline distinctions; this plan is not a substitute for that evidence.

Measure contraction by responsibility and reachability, not only lines/routes:

- Zero new provider mutations/contact through retired entry points.
- Zero default link-tap assignments or return-catch prompts.
- Zero synthetic Trip/session requirement for the supported external journey.
- All retained history, source, privacy, and cost consumers mapped and tested.
- Zero unexplained queued or external obligations in certified environments.
- No retired execution capability in tool discovery, app controls, or release
  requirements; no rollback route that silently re-enables it.
- Removed code/jobs/dependencies and intentional historical exceptions listed.
- Exact distinction between locally built, locally tested, native accepted,
  deployed, and externally decommissioned.

Runtime retirement can complete while governed historical records still exist.
If recovery remains active, label the result “new execution closed; legacy
recovery remains,” not “fully retired.”

## 18. Documentation changes during implementation

| Authority | Planned treatment |
| --- | --- |
| This investigation/plan | Keep broad contraction research; own bounded retirement package status, references, and receipts |
| Product Thesis / Model / Vision & Scope | Narrow amendment making retired execution distinct from retained practical intelligence and external evidence |
| Booking Product Strategy and `docs/systems/booking.md` | Replace future checkout/MoR/contact roadmap with external usefulness and explicit finite legacy recovery; retain historical provenance |
| Monetization Strategy | Remove execution-dependent promises and launch requirements; optional referrals do not justify a marketplace or insurance project |
| Contribution and Consequence | Preserve generic authority model; amend only an actual retained reservation/report/association seam if needed |
| August 23 contraction register | Add a dated superseding disposition for booking, not rewrite the historical M1 decision |
| HPL program / product-system build program | Distinguish early capability retirement from later retained-reader cutover and full HPL promotion |
| Release manifest and generated release contract | Declare actual retained/retired scope, then regenerate; no “dark for later” claim after retirement |
| API operation policy, mobile route/surface registries | Classify actual operations and destinations; remove obsolete QA obligations with evidence |
| Backend FEATURE docs, configuration/runbooks | Describe surviving entry points and owners; remove obsolete provider setup/canary instructions |
| Existing journeys 10 and 22 | Reconcile retained external-reservation and historical-recovery cases with the new responsibility boundary |

## 19. Execution ledger and immediate next step

| Package | Status at planning close | Evidence / next dependency |
| --- | --- | --- |
| CR-0 | Complete in repository | Scope and owner/interface decisions were recorded in `eb032ca` and the booking/release canon amendments in `7b06de4`; no production shutdown or shared-model expansion was inferred |
| CR-1 | Source inventory complete; environment audit blocked | Static inventory committed in `0f534c6`; the required per-environment read-only obligation report has not been run and remains a destructive-shutdown gate |
| CR-2 | Admission implementation complete; discovery/rollout gated | REST/domain/worker admission and stale/replayed dispatch guards landed in backend `7fb582700`; follow-through `d10fafd86` also guards booking/restaurant writers and provider-saga starts/reapproval. The audit-repair follow-through adds state-conditional retirement cleanup/failure writes, worker/audit classifier parity, and narrowed exception handling, with 115 focused tests across the package. Concierge booking-tool discovery remains a deferred Chat-lane surface; `BOOKING_EXECUTION_RETIRED` remains opt-in (`false`) until environment obligations are audited and deployment is approved |
| CR-3 | Places continuation complete; generalized evidence seam open | Backend venue continuation facts landed in `5e40410f3`; app venue/experience handoff landed in `78a396b73`; no booking session, Trip, day, or return-catch is created by the Places path. Independent non-Trip confirmation association remains open and is not claimed here |
| CR-4 | Partial: shared resilience and Places complete; retained readers deferred | Generic resilience moved to `backend/core/resilience.py` in `e33dd4764`; Life/stay/cost/history/deep-link readers remain untouched because this lane explicitly does not change Life or Chat |
| CR-5 | Not started; gated | Deleting execution UI, jobs, provider mutation branches, credentials/config, and route obligations requires CR-1 environment evidence plus CR-4 retained-reader coverage |
| CR-6 | Not started; local package checks recorded | Contract, typecheck, focused tests, lint, and generated route inventory are clean for landed slices; the contraction guard still reports two unowned Life routes, which are intentionally deferred. This is not native QA, deployment acceptance, or proof of external decommissioning |

**Next safe step:** obtain the environment-specific, read-only obligation audit
for each deployed environment, then re-check after the admission closure is
deployed. In parallel, the Life/Chat owners can approve the narrow retained
evidence and return-context seams. Only after those dependencies are evidenced
should CR-4 migrate retained readers and CR-5 delete obsolete execution
footprint. Do not set the retirement control live, drop booking tables, remove
the compatibility route, or remove the return-catch behavior from Chat as part
of this repository pass.

## 20. Next execution sequence — September 5 rebaseline

### 20.1 Outcome, authority, and current evidence

**Outcome: four useful roots, a small set of readable objects and focused
interactions, and fewer independently maintained operational workflows.** Home
and Places retain generous value; Chat accepts natural input; Life organizes
continuity. Contraction removes work from the person and the implementation.
It must not make every useful capability available only through a transcript.

This section is the requested detailed plan. It extends the existing research
and CR packages rather than adding a competing strategy document. Runtime
implementation, deployment, provider shutdown, and data migration are not
claimed by this planning update. Earlier implementation receipts remain dated
evidence. The existing no-Chat/no-Life editing boundary remains in force for
this capability-retirement task; owner handoffs below are planned dependencies.

The [complete-system integration roadmap](complete-system-integration-roadmap-2026-09-05.md)
owns overall ordering (I0–I6). The [Life replacement roadmap](life-complete-system-and-atlas-replacement-roadmap-2026-09-05.md)
owns Life/Atlas work (R0–R8). SC packages below define contraction deliverables
inside those programs. They do not create seven new teams, services, or goals.

Inspection points: workspace `c27b70e`, backend `647950ede`, app `f267db979`.
All were on `main`; integration continued during the read-only investigation.
The Plan design report, handoff, kernel, decision index, and a new seven-sentence
Plan decision had concurrent uncommitted edits. Those files were read as current
design input and left to their owner. Pin the committed ruling before Plan
implementation; this section does not independently promote their draft state.

These are the original planning inspection points, not a frozen shared checkout.
The later [lane checkpoint](#2012-active-lane-coordination-checkpoint) records
newer commits, the Strategy/Integration task split, active Entity work, and
Home's newly committed borrowing from Life. It narrows the first batch below.

| Evidence at inspection | Meaning for the next work |
| --- | --- |
| Booking guards and recovery repair are committed; `BOOKING_EXECUTION_RETIRED` defaults to `false` | Reuse the implementation. Enabling retirement and retiring a client workflow are separate decisions; neither is proven by the other |
| Local audit previously reported 2,342 additive counts; no deployed/provider attestation is recorded here | These are not 2,342 distinct customer bookings. Do not use fixture counts as a production obligation estimate or delete rows to make the gate green |
| `app/booking/[sessionId].tsx` remains 1,487 lines | Receipt reading and provider execution still share a large route |
| Trip plan is 2,082 lines; permissions is 599 lines; expenses still has five routes | Much of the visible workflow reduction remains ahead |
| M-1 registry has 47 surface entries: 11 compatibility, 2 external-handoff, 3 retire, and 31 in other classes | This is a QA inventory, not a count of visible tabs or independently implemented screens; aliases and fixtures must be distinguished |
| At the initial inspection, `surface:contraction:check` reported stale generated routes and missing owners for `/you/intake-submissions/[submissionId]` and `/you/life-record` | Recheck before implementing: Integration owns the coordinated registry update, with Life confirming its readers; Retirement supplies the booking dispositions |
| Life root and exact readers have advanced; indexed corpus primitives are still dark | Consume its current contracts and wait only for the reader/migration needed by a particular deletion |
| Home canon admits 35 semantic kinds | Audit renderer reuse; this does not require 35 independent visual implementations, nor authorize deleting meaningful distinctions |

### 20.2 Retained experience and removal boundaries

| User job | Target experience | Implementation to shrink | Required authority retained |
| --- | --- | --- | --- |
| Find somewhere suitable and reserve externally | Place/Experience explains fit and opens the provider directly | Session creation, cart, checkout, contact automation, ordinary booking autonomy | External link identity and return context; no claim of a reservation from a click |
| Retrieve a ticket or past reservation | Exact evidence reader with original, supported facts, status and useful continuation | Checkout-specific receipt wrapper and booking dashboard navigation | Source/session/offer identity, viewer scope, cancellation/unknown distinctions |
| Understand and change an arrangement | Current readable Plan; contextual words, narrow real controls, local result | Default block-entry ladder, general Changes feed, repeated administration | Existing Plan/Trip owner, participant and grant scope, revision-aware commands |
| See who is joining or allowed to edit | People and permissions close to the arrangement | Booking controls, voting/autonomy matrices as default interaction | Invitations, membership, edit grants, protected commitments, leave/revoke |
| Explain or split a receipt | Immediate interpretation; explicit allocation becomes one compact result | Five-route ordinary expense workflow and repeated supported-field entry | Exact amount/currency, payer/shares, current authorization and payment ledger |
| Re-find a past year, place, person, or source | Life and its exact object destinations | Competing Atlas/Memory archive homes and dedicated legacy workflows | Custody, existing originals, chronological meaning and correction |
| Receive value and friends' material | Home/Places compositions over existing sources and shared objects | Separate content factories, an additional social destination, repeated copies | Authorship, audience, source identity, freshness and withdrawal |

Keep the useful calendar/date picker, map, dense balance expansion, original
document, and focused object reader when the job needs them. A screen earns
its place by reducing comprehension or action effort. Replacing five screens
with five equally elaborate sheets is not completion. Moving their logic into
one giant Chat tool or generic renderer is not architectural reduction either.

### 20.3 Ownership and dependency map

**Integration** now executes I0–I6. **Strategy** is the separately forked
positioning/product discussion; older roadmap references to “Strategy” describe
the pre-fork task. The table names existing ownership and proposed handoffs,
not new instructions delivered to those tasks. This task does not allocate
their queues or treat an idle task as relinquishing its surface.

| Package | Execution owner / existing program | Depends on | Concrete endpoint |
| --- | --- | --- | --- |
| SC-0 — accurate inventory and replacement contracts | Retirement inventories its targets; Integration I0/I6 coordinates shared registry/navigation changes; Life confirms its route ownership | Current HEADs and exact consumer contracts | Reviewed route/capability dispositions; fresh contraction check; next batch has named readers |
| SC-1 — booking evidence and presentation contraction | Retirement owns isolated booking reads/recovery; Integration coordinates caller migration; Life/Home own their pass/receipt presentation; CR-3/CR-4 | SC-0; existing owner APIs; agreed reader and presentation contracts | Minimal retained evidence path, session-free new journeys, old execution presentation removable |
| SC-2 — arrangement and settings contraction | Components and Plan owns design; Integration I3/I5 implements coordinated owner integration | Current Plan ruling and journey coverage; exact intent/contribution/grant decisions | Readable Plan with compact local change/people behavior; legacy editor and admin branches reduced |
| SC-3 — assisted expenses | Retirement can specify the bounded expense-owner/result contract; implementation allocation remains proposed; Contribution and Capture owns intake/Chat behavior; Integration coordinates I3/I5 | SC-0; accepted expense interaction and scope; explicit receiving-owner handoff | Complete capture/read/correct/payment-history behavior through small reusable treatments |
| SC-4 — continuity replacement | Life R0–R8 owns organization, readers and migration; Integration owns cross-root emitters | Life's own reader, maintenance and migration milestones | Life is the only continuity experience; required legacy links preserve exact jobs |
| SC-5 — presentation reuse and social containment | Home owns composition; Entities owns object depth; Life owns kept-object presentation; Integration I4 coordinates their shared code | Current renderer inventory and accepted compositions; each owner's active file boundary | Fewer duplicated rendering and production paths with the same useful variety |
| SC-6 — deletion and operational closure | Retirement owns CR-5/CR-6; Integration I6 coordinates the candidate | Per-family replacement evidence; runtime/provider disposition where relevant | Obsolete UI, execution paths, registrations and maintenance obligations removed |

SC-0 → SC-1a read separation can proceed without a finished Life composition or
generalized Occasion model. SC-1a visual delivery follows the Life/Home
kept-object boundary. SC-2 and Life continue in their owners. SC-3 experience/
owner mapping can proceed while booking work lands. SC-5 accompanies ordinary
I4 work; it is not an additional renderer program in Retirement. SC-6 runs per
completed family rather than as one repository-wide deletion at the end.

### 20.4 SC-0 — establish a truthful, small execution boundary

Deliverables:

1. Re-run the read-only contraction check at current HEAD and record drift.
   Supply exact booking dispositions to Integration's next registry batch.
   Integration refreshes `travel-app/docs/design-alignment/route-inventory.generated.json`
   with its generator after Life confirms its actual owner or justified
   exemption. Do not broadly exempt `/you/**`, and do not independently
   regenerate the shared inventory while other lanes are changing routes.
2. Extend the existing M-1 register/route policies with each next target's user
   job, actual renderer, callers, replacement, retained read/write behavior,
   deletion condition, owner, and evidence revision. Reuse the registry; no
   new policy service or universal capability database.
3. Trace actual reachability: menu, CTA, old chat card, notification, external
   link, settings recovery, mock route, and dev gallery. Distinguish a tiny
   redirect from a full renderer behind a compatibility label.
4. For booking and expenses, name which operations disappear and which remain
   for inspection, correction, history, or recovery. Reconcile the API policy
   with real callers; do not mark all booking paths inactive by name.
5. Add focused behavioral checks for selected replacements. A metadata class
   alone cannot certify that an external handoff avoids session creation or
   that an old expense link opens its exact retained record.

Commit units: isolated booking consumer/disposition record; coordinated
generator/ownership repair in the receiving lane; then the applicable caller
changes. Keep generated registries synchronized with the actual implementation
stage; do not claim a planned redirect already exists. Unrelated route drift
does not block read-facade extraction, but must be reconciled before publishing
a changed route inventory or accepting a route-removal package.

Exit: a current check result with named receiving owners, no unidentified
consumer in SC-1a, and a bounded next commit list. Shared inventory repair must
pass before caller/route cutover. Repository-wide route reduction targets are
not set from raw file counts. Track destinations and compatibility adapters
separately.

### 20.5 SC-1 — finish the booking replacement before removing its shell

**SC-1a: isolate retained reads, then compose the retained reader.** Only the
read separation and its focused regression tests are the first code package.

- Start at `travel-app/data/booking.ts`, which mixes session/offer/coverage
  reads with confirmation, consent, refresh and other mutations. Extract the
  needed read facade into a small `data/` module using existing generated API
  types and query identities. Keep screen data access behind that facade.
- Map the smallest retained reader onto Life's kept-object/pass family and
  Home's accepted use of that family before building another receipt surface.
  Existing booking receipt primitives are reuse candidates, not a competing
  design authority. The reader needs source/provider, supported time and amount,
  exact status, original/evidence when available, and external continuation.
  The facade and tests can land before that visual mapping; route replacement
  cannot. Missing evidence remains missing.
- First preserve the session/offer identity model for historical records.
  Do not introduce a universal reservation table/DTO or silently convert
  existing bookings to Source anchors to make the UI uniform.
- Keep selection of multiple offers explicit where the old session link does
  not identify one. Never choose the first offer and present it as the receipt.
- Separate ordinary historical reads from active recovery polling; viewing a
  settled record should not start a background recovery workflow. Revalidate
  current access and show stale cached status honestly when offline.

First-package seams: `data/booking.ts`, its small extracted read module, and
focused booking tests. Later seams: `app/booking/[sessionId].tsx`,
`components/booking/BookingReceiptPrimitives.tsx`, and current booking read APIs.
`utils/routes.ts` is an Integration handoff, not an independent first-package
edit. `backend/life/refind_sources.py` and
`backend/core/accommodation_booking_truth.py` are retained consumers to map,
not files to rewrite wholesale. Preserve existing imports with thin re-exports
where useful so read extraction does not force cross-lane caller edits. Keep
query identity and current read/poll behavior stable during that extraction;
change recovery behavior only in its separately verified package. A read facade
is not a second truth owner.

**SC-1b: switch callers and reduce presentation.**

- Preserve the already-landed session-free venue/experience continuation.
  Cover unavailable URL/phone, normal return, and failed external open.
- Route legacy links to the correct retained reader, preserving origin and
  identity. Keep the compatibility URL until external callers are accounted
  for; the old interactive renderer need not live as long as its URL.
- Coordinate `components/chat/BookingConfirmationCard.tsx`,
  `hooks/useConciergeBookingCardActions.ts`,
  `components/booking/HandoffReturnCatchPrompt.tsx`, and
  `backend/concierge/tool_handlers/booking_flow.py` through Integration and
  Contribution and Capture. These are deferred Chat edits in this task.
  Align tool discovery and promises, handle
  stale calls truthfully, and migrate local return-catch claims without
  treating them as proof of a reservation.
- Inspect `app/trip-settings/index.tsx` recovery links before removing the
  booking route. A membership/leave blocker must still have a usable supported
  recovery destination while an actual legacy obligation remains.
- Delete checkout/cart/hold/contact panels and exclusive hooks only after
  supported callers and finite recovery users no longer need them. Reuse
  retained receipt pieces; do not rename the whole booking tree as evidence.

**SC-1c: decouple retained backend readers.** Preserve bounded historical read
adapters where that is cheaper and clearer than migration. A table may remain
for evidence while its execution service disappears. Inventory Life, stays,
expense/refund, export/deletion, confirmation shares and account departure.
Separate required facts from provider execution dependencies. Remove each
adapter only when its consumers have an exact replacement.

Acceptance: old confirmed/cancelled/unknown/multiple-offer records; revoked
access; supported external continuation; no new session/order from new paths;
stale client/tool calls; correct readback after late callbacks; intact linked
stay/expense and account lifecycle behavior. The prior 115 tests are a starting
suite, not evidence for a new client replacement.

SC-1a can be implemented and reviewed locally before a deployed obligation
audit. Switching or deleting recovery-dependent presentation follows the
existing CR/runbook gates. No production flag is inferred from an app build.

### 20.6 SC-2 — arrangements absorb itinerary and administration

Use the current Plan design's seven-sentence direction in kernel §11.15:
a current readable page; say the change through the contextual pill/Chat/voice;
own material changes within authority, others receive an explicit contribution;
effects attach to their rows; at most one top-level needs-you sentence; bounded
assistance; and failure preserves the person's words. Finite direct choices
such as a set time or yes/no remain allowed by that design. The earlier §4
examples are not a mandate to build a broad direct-edit toolbar.

The seven sentences define presentation, not permission to simplify away
commitment authority. “Yours” cannot authorize changing another person's
participation, spending, provider reservation, or an out-of-scope grant.
Unknown execution must never look applied. Notification and live-engine policy
retain their upstream contracts until any required amendment is accepted;
do not apply a Plan design's notification wording as a global silent policy.

Implementation sequence:

1. Land the read composition over existing Trip/Plan truth. Reuse
   `components/trip-plan/LocalPlanScreen.tsx` and the current plan-state data
   seam where suitable; inspect rather than preserve their Trip assumptions
   for future local intentions. Do not create a pseudo-Trip for a loose Keep.
2. Connect contextual expression to existing canonical commands for supported
   owner edits. Use the I3 decisions only for genuinely missing prospective
   material, contributions, or grants. Do not implement a second planner.
3. Place the consequential result on the relevant object/row. Replace general
   Changes navigation in `components/trip/TripHeader.tsx` with local readback
   and a deliberately opened history path. Old `/changes` links must resolve
   to their relevant history before the full old screen is retired.
4. Reduce `app/trip-settings/permissions.tsx` to relevant people/edit access
   and viewer controls. Remove booking initiation/autonomy controls with SC-1;
   scope any changes to voting or collaboration policy through the Plan owner.
5. Consolidate repeated facts across `trip-info`, `trip-dates`, Trip details
   sections and stay pages only when they represent the same user job.
   Preserve a useful date picker, per-person stay needs and accountable leave/
   ownership transfer. Global privacy, account deletion and connectors remain
   discoverable without requiring an AI request.
6. Delete superseded editor-only components, operation chrome and route callers
   after the replacement supports their retained jobs. Keep canonical revision,
   participation, conflict and correction machinery underneath.

Acceptance spans solo afternoon, hosted dinner, overlapping journeys with split/
rejoin, and a change while someone is moving. Check distinct personal and shared
effects, stale grant/preview, failed mutation, local history and exact return.
These complete situations guide the system; none becomes a mandatory user loop.

### 20.7 SC-3 — assisted expenses with small inspectable results

**Recommended scope:** first replace interaction over the existing Trip expense
owner. Deliver receipt understanding without a Trip, but do not promise shared
non-Trip debt until its participant/owner contract is explicitly chosen through
I3. Never manufacture a Trip to satisfy today's `log_expense` requirement.

Three treatments cover ordinary usage:

| Input / job | Immediate result | Consequence |
| --- | --- | --- |
| Receipt alone | Supported merchant/amount/currency and useful explanation; missing information remains uncertain | Private custody follows Bring/Ask; no automatic shared allocation |
| Explicit supported-scope instruction: “I paid $126; split equally among us three” | Payer, named people, $42 each, source/context and exact scope | Apply only under current financial authority; clarify a missing material fact once |
| “What do we owe?” or a correction | Compact current balance or changed allocation with focused inspection | Read deterministic ledger; correction/payment commands retain their existing semantics |

Reuse `backend/expenses/receipt_ocr.py`, `settlement.py`, `money.py`,
`exchange_rates.py`, `backend/core/db/expenses.py`, and the API/concierge
expense owners. On mobile reuse `data/expenses.ts`, relevant mutation hooks,
`ExpenseDetail`, `CostsBalanceSheet`, and receipt/amount primitives. The current
`useCreateExpenseFromReceipt` still requires Trip context; extraction and shared
debt must not be conflated when removing that presentation requirement.

Commit sequence:

1. Specify the result and inspection contract against existing owners. Include
   loading, unresolved input, exact applied state, payment lock, review/dispute,
   private masking, currencies and original receipt. Inventory each current
   add/edit/detail/balance action before replacing it.
2. Make extraction and known-field reuse work through existing input owners.
   Remove repeated category/date/payer questions when already supported. Do
   not turn possible costs into a review queue. Required Chat wiring remains
   a scoped Contribution and Capture / Integration handoff, not a composer
   redesign or second receipt-intake pipeline in this task.
3. Reuse one focused expense reader and balance treatment across the arrangement,
   Home when useful, and exact Life retrieval. Dense history expands the same
   ledger view. Keep receipt scope and numerical provenance visible on demand.
4. Implement correction, payment-history inspection, payment recording and
   voiding, and dispute/review actions in that focused treatment. A plain-language
   correction calls the same deterministic owner; generated prose cannot clear
   debt. Existing split grammar is immutable: replacement must follow the
   current owner contract rather than silently editing history.
5. Replace the five expense route callers with the shared treatment. Retain
   exact-ID redirects for historical links; remove exclusive forms, route
   implementations and mocks after the common and exception jobs work.
6. Close numerical/source gaps before exposing a lighter confident result.
   Audit `sentinel` conversions and current consumers; unknown exchange rates
   cannot contribute to a definitive converted settle-up. Preserve original
   amounts. Review the existing `accommodation_auto` exception explicitly; do
   not expand it or change existing debts as a side effect of UI contraction.

Keep these guarantees: deterministic rounding and currency precision, stable
idempotency, participant validation, live payments included in net balances,
append-only payments with void correction, no debt from masked gifts, and no
automatic balance change from a provider cancellation/refund. Existing review
authority remains inspectable even when its dedicated screen disappears.

Acceptance: explicit split; receipt without allocation; an absent/ambiguous
participant; private gift; stale/missing rate; duplicate submission; correction
after payment; void and re-record; disputed cost; cancelled booking evidence;
and a departed participant's still-permitted historical balance. Exercise both
server and mobile behavior against the same financial outcomes.

### 20.8 SC-4 and SC-5 — consume Life replacement and contain presentation growth

**SC-4 is Life-owned, not another implementation lane here.** Its roadmap
already has the visible Life root and indexed-corpus foundations. Contraction
needs exact source/record readers, preserved year/city/other filter semantics,
current authorization, originals, correction, and every required legacy link.

- Integration maps incoming emitters in Home, Places, Chat, notifications and
  shared links to Life's accepted destination contract.
- Life removes old Atlas composition/readers and exclusive producers as their
  jobs migrate. A thin historical URL adapter may outlive the Atlas product.
- Source data is not a deletion candidate simply because its old UI disappears.
  Verify source withdrawal, counts, chronology and representative legacy records
  before backfill/serving changes; follow Life's own migration sequence.
- This task supplies the booking/expense retained-evidence boundary. It does
  not independently replace Life's index, organize the corpus, or redesign Life.
- Life's latest work also investigates organization, editorial synthesis and
  maintenance requirements. Index utilities alone do not replace Atlas's useful
  enrichment or establish the new experience. Preserve required producers until
  Life identifies which exact replacement is serving their retained jobs.

**SC-5 consolidates proven duplication during I4.** Map Home semantic kinds to
their actual renderers and value producers before extracting common code.
Prefer existing composition/receipt/reading/map primitives and native props.
Do not build a universal model-generated UI schema to reduce a component count.

Candidate shared families to inspect: short finding/readable prose, source or
authored contribution, prepared sequence/alternatives, practical state/receipt,
and navigation/expansion. These are implementation candidates, not five new
product grammars or a fixed limit. A spatial comparison and an authored friend
share may need different forms even when both use a card container.

Preserve the latest social split: addressed/shared-consequential material in
Home, casual spatial sharing in Places' friends scope, and durable history in
Life People. Reuse identity and authored material; do not add a social tab,
separate social content factory, or duplicate the same contribution in full
throughout Home. Follow the explicit exceptions and admission conditions in the
[Home amendment](../decisions/2026-09-05-amend-home-composition-canon.md).

The subsequent [Home/Life pass decision](../decisions/2026-09-05-home-borrows-life-pass-grammar.md)
also preserves tickets, flights, bookings and other kept objects as useful
material: Life holds the record; Home can present the timely consequence or
live pass. Removing Vesper-owned booking execution must not remove these
objects, their valid live facts, or their external continuation. Reuse the
accepted visual family without merging backend identities. Its crown-arbitration
clause is explicitly provisional; native accessibility and the unsettled visual
details still require the owning design/acceptance work.

Exit: an actual duplicate implementation or independent production path was
removed, its surviving consumers retain meaning and behavior, and native
composition remains useful. Reducing the semantic-kind count is not an outcome.

### 20.9 SC-6 — remove superseded code and finish operational closure

Treat each cut as a bounded change with a replacement record:

1. Identify the exact implementation and callers to remove, including old
   clients, background jobs, notifications, external links and test fixtures.
2. Establish the retained job's replacement or explicitly retired responsibility.
3. Update emitters and preserve exact compatibility handling where needed.
4. Remove exclusive UI, hooks, mocks and transports; prune unused imports and
   dependencies. Shared voice, subscription billing, routing, intake and source
   controls must be traced independently of booking naming.
5. Remove obsolete design/capture scenarios and launch obligations with the
   implementation. Transfer retained behavior tests to the replacement. Keep
   historical evidence as historical; a former screenshot baseline must not
   force a dead screen back into the product.
6. Reconcile the surface/route registries, API operation policy, generated
   contracts, release manifest and affected system/FEATURE documentation.
7. Record the surviving adapter, if any, with its owner, consumers and objective
   removal condition. Do not repeatedly extend a compatibility label without
   shrinking the old implementation.

Booking operation closure additionally follows the
[audit runbook](../../travel-agent/docs/operations/Booking%20Capability%20Retirement%20Audit.md):
verify the actual deployed database selected by configuration (`--environment`
is a label, not a selector), audit each environment, classify and attest provider
obligations, approve the applicable finite recovery/zero-obligation disposition,
then close admission under the operational procedure and re-audit in-flight work.
Retain required callbacks and liability-reducing recovery until resolved.
If obligations block enablement under the current runbook, record that block;
this plan does not silently relax it. UI/read separation may still progress.

Only then remove unused provider execution modules, jobs, startup registrations,
credentials/config requirements and launch canaries. Database/table removal is
a separate decision based on retained evidence, export and deletion consumers;
it is not a prerequisite for removing checkout. Rollback may restore a needed
reader without reopening new provider execution or resurrecting deleted sources.

### 20.10 Validation, measurements, and design handoffs

Validate by the changed responsibility, using existing suites and registered
native QA rather than building a new proof environment first.

| Change | Required evidence |
| --- | --- |
| Inventory / docs | Generator parity, M-1 contraction check, valid lifecycle/links, explicit retained adapter ownership |
| Booking read/presentation | Focused booking/read/retirement tests; historical/unknown/cancelled access; external open makes no booking write; exact caller return; registered native booking/entity scenarios |
| Arrangement/permissions | Canonical owner and participant tests; local/multi-day/split scenarios; scoped edit and failure readback; retained history and leave/revoke; registered Plan/settings captures |
| Expense replacement | Existing settlement property/e2e, expense API and concierge parity tests plus the changed focused mobile suites; dense, private, currency and payment-lock native cases |
| Life migration | Life-owned parity/index/source-custody/legacy-reader evidence and native acceptance; no second certification program here |
| Shared rendering | Exhaustive handling for admitted kinds, source/identity/action parity and native comparison for changed families |
| API/removal | `./scripts/sync-types.sh`, `make contract-check`, `make api-coverage-check`, app typecheck, relevant backend/frontend offline suites and import/architecture gates |

Re-run the full affected offline suite at an integrated candidate or when new
failures justify it. Attribute failures to inspected revisions; an untouched
file or large passing count alone does not prove a failure is baseline. Native
evidence is separate from code/contract checks. Deployment is separately recorded.

Measure each package's before/after using a small ledger in its receipt:

- independent user workflows removed, distinct from route aliases;
- required screens/questions to complete the representative job;
- repeated facts the person must supply;
- exclusive components/hooks/transports/jobs deleted;
- retained jobs with exact successful destinations and correction paths;
- actual native/usefulness result and unresolved integration dependencies.

Do not set a screen-count or LOC quota. Four roots stay; the useful full-scroll
richness of Home and Places is not the target of contraction. Source-code
reduction is meaningful only when supported behavior remains clear and dependable.

Claude design work, where needed, should refine the existing owners' outputs:

1. Life/Home kept-object family: verify normal, cancelled, unknown and missing
   evidence cases, original and external continuation. Request only uncovered
   booking-reader states; do not commission an independent reservation design
   while those owners are already composing passes and chips.
2. Expense result plus expanded inspection: explicit split, receipt-only,
   correction, payment lock and unresolved currency; reuse existing primitives.
3. The Plan owner's already-selected reduced composition and necessary people/
   settings treatment; do not commission another ninety-frame operational map.

Each handoff names the old UI it replaces and the interactions retained. It
does not request redesigns of all four roots. Visual exploration can follow the
owner/read contract; basic read-facade separation does not wait on final artwork.

### 20.11 First batch and explicit completion states

**Next batch in this task:** execute the isolated part of SC-0 and SC-1a:
inventory booking read consumers; record current route drift and its receiving
owners; separate the read facade behind existing imports; add focused regression
tests; publish the retained fields and caller migration table. No shared route
rewrite, new receipt composition, schema regeneration, extra retirement switch,
or size-ceiling increase belongs to this first package.

Then complete SC-1a presentation using the Life/Home family and migrate SC-1b
callers through Integration with Life and Contribution and Capture. SC-2 and
SC-4 proceed in their existing programs. Prepare SC-3's bounded interaction and
owner mapping, but do not assume ownership of intake/Chat or start a parallel
expense composer. Once allocated, it need not wait for all Home content or the
complete Life index rollout. Fold SC-5 into I4 where duplication is observed.
Apply SC-6 family by family as dependencies close.

| Completion state | Required result |
| --- | --- |
| Planned | Named retained jobs, inspected seams, owner, replacement and deletion conditions |
| Implemented locally | Replacement code and relevant local checks; no implied serving or release claim |
| Replaced in supported app | Normal and legacy entry points perform retained jobs through the new treatment; native/real-backend evidence recorded |
| Old implementation removed | Exclusive code, tests/fixtures, route/transport consumers and maintenance obligations deleted or deliberately retained as bounded adapters |
| Operationally retired | Deployed workers/providers/credentials and any remaining obligations have exact closure evidence; historical data remains governed |

At this planning close, SC-0–SC-6 are proposed execution packages with the
already-landed CR/Life/Places foundations listed above. None is marked complete
by writing this section. The next review should assess whole experiences across
the four roots and the maintenance burden actually removed, then adjust the
next dependency-bound batch.

### 20.12 Active-lane coordination checkpoint

**Observed September 5, approximately 15:20 EDT.** This checkpoint follows a
read of the latest Integration, Life, Home, Strategy, Contribution and Capture,
and Components and Plan task turns. The Entities task tool returned empty turn
items; its latest user/assistant messages were recovered from that exact local
task's transcript and checked against its new acceptance plan and commits.
Only user-visible messages were used. This is an observation, not a lock,
delivered assignment, or claim that another agent acknowledged a handoff.

| Task / stable ID | Latest observed work | Consequence for Retirement |
| --- | --- | --- |
| **Integration** — `01a030af-13a8-74e1-81be-7d526bec3045` | Executing I0–I6. Home transport union/prose handling, authority-safe owner-read coalescing, Places result identity and return propagation have landed; catalog-backed revision work is now committed. Places map/return work remains active | Consume those contracts. Leave shared routing, root queries, result-set identity, renderer unions and schema synchronization to the integration package |
| **Life** — `01a06ecc-1a79-74a1-9c47-9f24461313ea` | Latest request is research into design/docs and organizing-system requirements. Index/withdrawal primitives exist; serving cutover, incremental maintenance, grouping and editorial intelligence remain incomplete | Supply retained booking/expense evidence needs. Do not create Life groups, replace its source reader, cut Atlas producers or assume the four lenses are a complete replacement |
| **Entities** — `01a0649a-f267-7d31-a788-81669e1822a8` | User authorized execution of [C0–C8 acceptance work](entity-system-acceptance-plan-2026-09-05.md). C0 documentation and C1 public-share payload hardening have landed; canonical reads, freshness, research lifecycle, people privacy and native acceptance follow | Leave venue/site/experience routes, shared object renderer, `data/entities.ts`, research and people contracts with Entities. Its declared scope excludes accommodation frontend migration and root redesign |
| **Home** — `01a06f87-e648-74d2-a0ae-f0adb305e44c` | Latest task response recommends connected full-scroll implementation, exact Keep/arrangement destinations and return repair; task was idle when read. Separate current design changes have now committed Home's use of Life passes/chips and provisional crown arbitration | Preserve generous discovery/social/practical value. Reuse the new kept-object family; no separate booking-card redesign or blanket removal of reservation material |
| **Components and Plan** — `01a06e71-b35c-7ca0-8307-367db90a8a6a` | Latest completed work expands [handoff §0.6](claude-design-plans-in-real-life-handoff-2026-09-04.md#06-end-to-end-journeys-coverage-and-engineering-implications) with entry, contribution, disagreement, conditional-plan and later-return gaps. Plan decision/report/handoff work remains concurrent | Keep itinerary/settings contraction behind the accepted arrangement behavior and owner commands. Do not remove guest contribution, participation or recovery jobs because the new page looks simpler |
| **Contribution and Capture** — `01a06edc-801f-7683-b6b7-1611c483f0e1` | Latest repair batch separates authored authority from evidence, preserves Bring retention, bounds temporary custody, stabilizes Chat retry identity and fixes source-level Life counts. Task was idle when read | Reuse this intake/Chat path for receipts. Do not add a second OCR-to-memory or expense-ingestion path; preserve source custody separately from financial allocation |
| **Strategy** — `01a072c6-2735-7152-94ea-bb6958ead53d` | Separate fork discussing understandable promise, adoption and value. “More to discover. Less to figure out.” is a proposed positioning direction, not a newly implemented contract | Contraction should reduce effort while preserving discovery and practical care. Strategy discussion does not itself assign engineering work or change accepted runtime authority |

Useful source anchors at this checkpoint:

- Integration: backend `c57aef18c` / `407173860` (Places identity/catalog
  revision), app `f267db979` / `84ae8d379` (return propagation), and
  `615f42d93` (typed prose). Do not repeat already-landed packages.
- Entities: workspace `d3f82c8` (acceptance plan), app `7a783afae` (public
  share payloads); prior lifecycle/identity fixes remain part of the baseline.
- Home/Life design: workspace `c2cabef`, app `8b7d540bd`. Accepted document
  status does not imply every provisional clause or native visual detail is
  settled.
- Capture: backend `42964124e`, app `5a2b02ed4`; reuse the corrected contract
  rather than the earlier review's superseded failure descriptions.
- Life: backend `647950ede` is withdrawal/upsert hardening, not a backfill or
  serving cutover receipt.

#### Work that can proceed independently here

1. Booking read/write/recovery consumer inventory, including accommodation,
   expense/refund, Life refinding and settings departure dependencies.
2. Read-facade extraction in booking-owned modules with compatibility exports
   and tests preserving exact session/offer/query semantics.
3. A retained-evidence adapter specification: existing owner/reference, allowed
   facts, source/evidence link, status distinctions, access and recovery needs.
   Use it as input to the Life/Home reader; no universal new object is needed.
4. Expense interaction and deterministic-owner analysis. Capture implementation,
   arrangement placement and shared non-Trip debt remain receiving-owner seams.
5. Static obsolete-dependency analysis and operational audit preparation. No
   deployed access, flag enablement, provider action or data deletion is implied.

#### Work that requires a shared boundary before this task edits it

| Boundary | Receiving owner / required artifact | Our next permitted contribution |
| --- | --- | --- |
| Shared navigation and route registry | Integration, with Life/Entities confirming exact destinations; current [Places context contract](places-result-set-context-contract-2026-09-05.md) and [dependency matrix](cross-root-change-dependency-matrix-2026-09-05.md) | Submit caller/disposition rows and regression cases; do not rewrite `utils/routes.ts`, root navigation, Places return helpers or generated inventory independently |
| Booking evidence on Home and in Life | Life/Home field and reader mapping, preserving historical owner identity and supported recovery | Specify source/session/offer/status needs; re-use pass/chip/reader patterns once mapped rather than introduce a parallel artifact system |
| Shared entity components and accommodation | Entities' current acceptance boundary; Integration resolves any accommodation handoff | Trace booking dependencies in accommodation. Do not infer that its exclusion from Entities makes its screen available for unilateral redesign |
| Chat/receipt ingestion | Contribution and Capture contract plus Integration's consumer wiring | Supply retained read/correction operations and receipt-only versus allocation cases; no Chat or share-screen edits in this lane |
| Plan/permissions/expenses | Components and Plan journey coverage and Integration I3/I5 owner decisions | Identify obsolete booking controls and exact retained leave, grant, payment and recovery jobs; no parallel Plan or expense-input composer |
| OpenAPI/generated types | One bounded API-change package with named owner and isolated schema sync | Avoid contract changes in read extraction. If later necessary, reconcile overlapping model edits and regenerate after the owning source commit |

Handoffs stay small: current source SHA, exact files/consumers, retained user job,
needed contract or decision, regression cases, and a clear readiness condition.
For a cross-owner edit, first verify the current accepted contract and file
boundary; a missing agreement becomes a bounded question for that owner/user.
It must not stop unrelated booking read work or trigger a freeze across all lanes.

#### Shared-checkout discipline

The inspected repositories are shared `main` checkouts, not isolated lane
branches. The task histories already record mixed staging and temporarily lost
unstaged changes during concurrent commits/synchronization. Filename-scoped
staging alone does not prevent `git commit` from including somebody else's
already-staged files, nor does it protect overlapping generated output.

Before each package and commit, re-read HEAD, branches, worktrees, status, staged
paths and the intended files' diff. Never unstage, reset, stash, commit or restore
another task's work to obtain a clean tree. If the index contains another lane's
work or an overlapping edit is active, defer that commit or use an explicitly
isolated `codex/` worktree with a later scoped integration step. Do not run
concurrent schema syncs or route-generator rewrites over active source edits.

This planning update changes only this document. The next runtime package is
the independent read-separation package above; all broader contraction outcomes
remain planned, with their actual owning lanes and dependencies visible.
