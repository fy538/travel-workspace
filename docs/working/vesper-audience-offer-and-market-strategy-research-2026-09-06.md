---
doc_type: working
status: active
owner: founder / product / research
created: 2026-09-06
last_verified: 2026-09-07
expires: 2026-10-06
why_new: Investigates six connected market-facing choices following the consumer strategy research, covering audience, complete release offer, ownership boundaries, distribution, paid packaging and competitive advantage.
supersedes: []
source_of_truth_for: []
---

# Bringing the complete Vesper product to market

## 1. Conclusion and status

**Focus the initial audience and supported service, not the product philosophy into one feature.** The strongest current hypothesis is a person who already asks questions, saves places or exchanges recommendations, but must repeatedly reconnect those fragments to what they can do, whom they might do it with and what is happening now. One current need is enough; none of these behaviors is an admission requirement.

For that person, Vesper should offer two things together: **more worthwhile understanding and possibilities, and less work making them useful in real life.** Less copying between apps is part of the benefit, not the whole value proposition. Sometimes the result should be a surprising explanation or a friend's perspective worth enjoying without further action.

This memo investigates six questions requested in the strategy task:

1. Who has the strongest reason to choose Vesper first?
2. What is the complete first-release offer?
3. What should Vesper own versus hand off?
4. What makes someone recommend it, and when does receiving become adoption?
5. What is worth paying for?
6. Why choose it over a strong combination of existing products?

These are recommendations and research hypotheses, **not adopted geography,
public copy, entitlements, retention policy or launch readiness**. No user study,
purchase test, competitor hands-on benchmark or production cost measurement was
conducted. Product documentation establishes advertised capability, not
independently verified quality. Initial research was checked September 6; later
rounds are dated September 7 with source and access limits beside the findings.

### Current reading map

| Question | Read this | Status |
| --- | --- | --- |
| What is accepted? | [Consumer-strategy decision §5](../decisions/2026-09-06-reconcile-consumer-strategy.md#5-september-7-refinement-complete-benefits-selective-context-and-voluntary-choice), then Product Thesis / Model | Accepted product and evaluation refinement; not a shipped-service claim |
| What would the complete first offer include? | [Supported-offer candidate](vesper-v1-supported-offer-2026-09-07.md) | Proposed service boundaries and three entrances; coverage, availability and payment unresolved |
| What is the latest memory recommendation? | [Continuity proposal §4](conversation-history-source-expiry-decision-proposal-2026-09-06.md#4-simple-controls-with-exact-consequences) and [§10](conversation-history-source-expiry-decision-proposal-2026-09-06.md#10-selective-long-range-continuity-four-complete-experiences) | Selective long-range use and scoped controls, still unadopted; current Ask/T0 binds |
| What should a finished encounter feel like? | [§15](#15-complete-encounter-comparison-and-recommended-defaults--september-7), [§16](#16-received-value-against-capable-alternatives--september-7), and [situated-value §11.9](situated-value-decision-matrix-2026-09-06.md#119-whole-experience-review-received-value-context-and-human-work) | Authored comparisons, including capable alternatives; not consumer results |
| What was actually exercised here? | [§17](#17-executed-receiving-capture-and-remaining-encounter-gaps--september-7) and [§18](#18-addressed-note-to-private-help-implementation--september-7) | Dated local receipts and a bounded note-to-private-help implementation; not live consumer delivery |
| What governs engineering handoff? | [Integration roadmap](complete-system-integration-roadmap-2026-09-05.md) | Existing owners, dependencies and checkpoints; its current execution status outranks this memo's historical lane snapshots |
| Why these recommendations? | [§19](#19-four-consequential-strategy-questions--september-7), then the relevant earlier research section | Research synthesis; no independent policy or release authority |

The [accepted consumer-strategy decision](../decisions/2026-09-06-reconcile-consumer-strategy.md) remains authoritative. Everyday usefulness is the product; travel is a demanding specialization and acquisition candidate. Consumer-funded assistance is the economic direction. Provider transaction execution remains retired. The four moves remain **Make sense. Open possibility. Help it work. Carry forward.** No person must traverse all four.

### September 7 audit: chronological trace and fresh-eye assessment

Scope: the Strategy task `01a072c6-2735-7152-94ea-bb6958ead53d`, from
06:24 to 18:24 EDT on September 7. The 40 completed turns in that window run
from approximately 10:51 to 18:17 EDT. This traces task messages, findings,
document changes and recorded execution receipts; it is not a new code audit
of every parallel lane or a rerun of their tests.

| Time, EDT | How the thinking progressed | Where the reasoning lives |
| --- | --- | --- |
| 10:51–11:23 | Specify optional recent continuity, then insist context earn influence; repo review separates foundational progress from consumer-value evidence | Continuity proposal §§2, 7; historical 90-day comparison in §9 |
| 12:50–13:21 | Separate audience, entrance, payoff, return and payment; treat the exhibition demo as a controlled example, not a universal entrance, and specify three credible first encounters | §§12–13 |
| 13:43–14:37 | Follow accepted work through delivery/refinding and corrections through day 1, day 2 and day 5; a four-month return exposes the cost of a universal 90-day ceiling | Continuity §§8–9; integration §9.6.8; situated-value §11.9 |
| 14:54–15:05 | Prefer selective older context over a universal cutoff; preserve temporary circumstances, attribution, source expiry and capable fresh answers | Continuity §10; §19.3 |
| 15:30–15:54 | Compare orientation, payoff-only and payoff-plus-bridge; revise the broad bridge hypothesis into mixed defaults with genuinely finished endings | §§14–15 |
| 16:12–16:56 | Compare substance against strong alternatives, inspect synthetic receiving captures, then implement the bounded addressed-note/private-Ask handoff | §§16–18; stronger local integration evidence, not demonstrated consumer preference |
| 17:15–17:53 | Synthesize complete service, continuity, whole-page value and market/economics; align canon and write the supported-offer candidate | §19; accepted decision §5; supported-offer candidate |
| 18:06–18:17 | Refine controls by requested/on-visit/interrupting/external use; early explanation is not blocking configuration; do not turn a proposed pause into an ambiguous destructive control | Continuity §§4–6 and the §10 branches |

**The direction is refinement, not another pivot.** Immediate help, independent
world receiving and a friend's offering can each be complete. Authorized context
may improve later selection, understanding or feasibility without compulsory
callbacks. The live engine supplies current judgment and explicitly accepted
responsibility, not a separate operations product or an ambient watch. The four
moves remain a repertoire across roots, never a mandatory sequence.

Three earlier recommendations must not be read as current defaults:

- The **90-day ceiling** is an earlier comparison, not the latest proposal;
  removing it does not remove source expiry or adopt a new retention agreement.
- **Payoff plus bridge** is not the universal ending. §15 supersedes that broad
  preference with encounter-specific defaults; available capability need not
  become another visible task.
- A separate **pause** was explored, not selected. The latest proposal favors
  legible off-with-clearing; a request to pause must not silently erase material.
  Nonblocking explanation can come early without turning first value into setup.

#### Research and evidence audit

The research supports design risks and plausible mechanisms more strongly than
it selects Vesper's exact defaults. The memory interview work is exploratory;
reminiscence and social-agent studies are not evidence for daily Vesper use;
vendor documentation is not a hands-on competitive benchmark. Abstract-only
and preprint limits remain beside the underlying claims.

This audit rechecked the [serendipity paper](https://arxiv.org/abs/2507.17290):
its best reported Pearson correlation is 0.215, not 21.5% accuracy. It does not
certify Vesper delight. The [OP-Bench paper](https://arxiv.org/html/2601.13722v1)
uses constructed cases selected for inappropriate memory use; its failure rates
must not become estimates of ordinary consumers' experience. Neither source
selects a retention duration or a product policy. Other sources retain their
recorded verification dates; this is not a claim to have newly reread every paper.

Keep four evidence classes distinct: authored targets; synthetic/controlled
fixtures; actual generated and delivered app results; human benefit, voluntary
choice and paid-service evidence. The classes answer different questions.
§17 records 73 backend checks, 34 mobile checks and twelve synthetic captures;
§18 records a subsequent note-only implementation with local checks. Their
counts overlap and must not be summed into unique coverage or consumers tested.
Attachments, retained adapted answers, full generated-encounter quality and
production availability do not follow from those receipts.

The strongest remaining risk is **documentary confidence outrunning delivered
value**. These examples increasingly clarify the target, but we still lack
evidence that the whole offer wins voluntary choice at sustainable cost. Repeated
research summaries cannot close that gap. Conversely, a fresh answer tying a
capable alternative is not failure; consistent ties without later contextual,
practical or social advantage would weaken the differentiated-product thesis.

#### What remains consequential

1. Resolve the existing history/use agreement and its concrete control effects;
   do not let an attractive walkthrough count as adoption.
2. Resolve the first supported service's real materials, coverage, completion
   and return paths using the offer candidate and existing engineering owners.
   Inspect actual outcomes across the portfolio, not a single showcase loop.
3. Learn whether the intended audience chooses and later pays for that service,
   separating comprehension, benefit, opportunity, voluntary return and cost.
   No recruitment, purchase or release is authorized by this audit.

No new grammar, architecture lane or research queue is needed to organize these
decisions. Amend the owning document when a choice changes; keep earlier
comparisons as dated provenance rather than adding another competing conclusion.

## 2. Documentary baseline and reconciliation

This builds on, rather than replaces, the [consumer-promise research](vesper-consumer-promise-and-adaptive-value-research-2026-09-05.md), [ordinary-value research](vesper-ordinary-value-and-relationship-strategy-research-2026-09-06.md), [useful-preparation research](vesper-useful-preparation-and-initiative-research-2026-09-06.md) and [situated-value manuscript](situated-value-decision-matrix-2026-09-06.md). Those documents examine how assistance should behave; this memo asks what recognizable offer that behavior creates.

Reviewed authorities include [Product Thesis](../../travel-agent/docs/product/Product%20Thesis.md), [Growth Strategy](../../travel-agent/docs/product/Growth%20Strategy.md), [Monetization Strategy](../../travel-agent/docs/product/Monetization%20Strategy.md), [Venture Path](../../travel-agent/docs/product/Venture%20Path.md), [Content as Infrastructure](../../travel-agent/docs/product/Content%20as%20Infrastructure.md) and the complete [contribution contract](../systems/contribution-and-consequence.md). The [Home implementation map](home-connected-experience-implementation-map-2026-09-04.md) supplies point-in-time delivery boundaries, not a new code audit.

The current strategy already distinguishes audience, entrance, first payoff, return and payment. It also rejects equating recipient participation with acquisition, memory with advantage, or a complete free experience with unlimited service. The missing work is choosing among coherent alternatives and specifying the service each would actually receive.

The original inspection found an August 16 header, trip-first readiness and an
obsolete heritage-partnership pointer in **Content as Infrastructure** despite
an earlier follow-through claim. The September 7 audit corrected the actual
file: everyday and sparse-context receiving now sit beside demanding travel;
understanding/enjoyment need not cause a decision; behavioral signals do not
establish satisfaction or identity; shared world supply stays permission-bound;
partnerships and defensibility remain conditional. The current Monetization
Strategy is linked directly. This reconciles doctrine, not runtime behavior.

The same audit corrected the consumer-promise brief's stale “now recommends
90 days” statement and connected the latest scoped-control proposal to the
existing receiving ledger and roadmap. No accepted authority, launch geography,
price, source eligibility or current Ask/T0 policy changed.

Two narrower Editorial Canon conflicts were also reconciled with its existing
doctrine: a social return can supply enjoyable familiarity without new knowledge,
and opening an article, map or audio work for depth is legitimate. The rejected
pattern is an empty teaser or another input demand, not media that needs more
room than a Home preview. No new medium or social audience was introduced.

**Commit-boundary note:** some dated lane observations below consulted concurrent
local drafts. References marked **local WIP** are provenance, not documents or
sections landed by this strategy commit. Their owners retain publication and
implementation responsibility; the relevant accepted canon still governs.

## 3. Initial audience: choose a recurring situation, not an aspirational identity

### Evidence and interpretation

The 2025 NBER working paper *How People Use ChatGPT* identifies practical guidance, information seeking and writing as dominant consumer uses. That supports the existence of ordinary question-and-help behavior. It does **not** establish demand for Vesper, dissatisfaction with assistants or willingness to switch. This pass used the indexed publisher abstract; direct full-paper retrieval was blocked. No numerical market estimate is derived from it. [NBER working paper](https://www.nber.org/papers/w34255).

Beli explicitly presents restaurant tracking and sharing with friends as its product entrance. It illustrates how a recognizable activity can explain a product; it does not establish that Vesper should require restaurant logging or copy its scope. [Beli](https://beliapp.com/beli-home).

The strategic implication is to enter through an existing action while earning an additional benefit. “Document your life so we can eventually understand you” requires a new habit before repayment. “Bring this question or recommendation because we can help now” can meet an existing need. That is a hypothesis about adoption friction, not a result from either source.

### Three viable audience/entrance combinations

| Candidate | Immediate reason to try | How the complete product can become relevant | Main strategic risk |
| --- | --- | --- | --- |
| People already exploring ordinary life through questions, saved places and recommendations | A question, an open afternoon, a friend's tip or something noticed becomes immediately useful | Understanding, local possibilities, casual sharing, practical preparation and later retrieval | Weak local supply or a generic answer loses to existing assistants and maps |
| People who often bring friends together | Reduce the reconstruction and coordination needed to make a small gathering work | Shared suggestions, human contributions, individual constraints, live adaptation and shared history | Becomes organizer software; friends receive chores and the host becomes an unpaid operator |
| Travelers who also want continuity at home | Make unfamiliar circumstances understandable and manageable | Travel evidence, relationships with places, practical help and later local openings | Episodic demand, heavy reliability expectations and an enduring travel-planner first impression |

**My recommendation is the first as the leading audience hypothesis, the second as an embedded distribution opportunity, and the third as a demanding comparison and seasonal entrance.** This preserves everyday strategy without pretending that local discovery is easy or that travel has ceased to matter.

Recruitment should look for recent behavior, not ask people whether they are curious: a saved recommendation they could not refind; a question whose answer they wanted to use; an outing requiring several searches; a friend message that could have become a shared experience. Do not require all those behaviors, a rich archive or an active friend graph. Include people who dislike planning and people who enjoy choosing or researching; they may want different parts of the work removed.

NYC is a reasonable founder-accessible candidate **if** the actual world supply can support the selected situations. Access to residents is not evidence of neighborhood readiness. “New Yorkers” is too broad an audience, and “cultured travelers” risks confusing the founder's tastes with a market.

### What would change this recommendation?

Favor social-led acquisition if both organizers and lightly involved recipients experience markedly better outcomes, while individual use remains useful. Favor travel-led acquisition if acute value creates substantially stronger voluntary choice and people later use Vesper outside trips without prompting. Reconsider all three if the best cases require the founder's unusually rich history or constant bespoke attention from the team.

The audience must have a reason to choose Vesper **before** its continuity advantage compounds. Later context cannot rescue an uncompetitive first encounter.

[Section 12](#12-audienceentrance-recommendation-and-acquisition-packet--september-7)
makes this recommendation recruitable: a leading audience and moment, matched
message comparison, supported-payoff requirements and voluntary distribution.
It does not select launch geography or change the canonical product boundary.

## 4. First-release offer: a complete service with declared limits

### Breadth of capability is different from breadth of user work

Thompson, Hamilton and Rust's three studies found that consumers weighted capability more before use and usability more after use, sometimes selecting products that disappointed in practice. The accessible publisher abstract supports that distinction; it does not prove a universal maximum feature count or that a coherent multi-purpose AI product must be split apart. [Feature Fatigue, 2005](https://journals.sagepub.com/doi/full/10.1509/jmkr.2005.42.4.431).

For Vesper, the implication is **do not make people learn a separate workflow for every capability**. Keep a small number of recognizable actions and stable destinations. The four moves describe delivered value, not four onboarding choices or one move per tab.

Granola offers a useful adjacent example: its pre-meeting briefs prepare from existing notes and other permitted sources around a concrete upcoming meeting. Its current documentation limits eligibility and omits a brief when useful material is insufficient. This illustrates a service whose scope and delivery moment are intelligible; it does not validate transplanting workplace monitoring into private life. [Granola pre-meeting briefs](https://docs.granola.ai/help-center/taking-notes/pre-meeting-briefs).

### Proposed complete-release requirements

These are experience requirements for planning, not a list of shipped features:

| User expectation | Complete value required | Honest boundary |
| --- | --- | --- |
| “Help me with this.” | A useful answer, explanation, comparison or practical interpretation from one question or item | No profile, friends or Trip required; source uncertainty remains visible |
| “Show me something worthwhile.” | Home has substantive on-view value; Places supports spatial exploration and depth | Selected supported coverage; no promise of a wholly new bespoke feed every day |
| “Can this work for us?” | Bounded feasibility, alternatives and a clear next step around an actual intention | Advice is not an accepted watch; provider execution stays external |
| “I want you to have this.” | A friend's original material is understandable and usable with little recipient effort | Audience and authorship survive; no automatic enrollment in a project |
| “Where is the thing I gave you?” | Entrusted material can be refound and understood in Life and appropriate context | A question alone does not currently authorize lasting memory |
| “Something changed.” | Accepted state and dependent help remain coherent, with correction or an explicit limitation | No promise of detecting everything or silently performing external actions |

Each root has a role within that offer. **Chat** is the easy way to ask, bring and steer. **Home** delivers relevant value now and ahead, including enjoyable material that needs no action. **Places** makes the world spatially, practically and socially legible. **Life** gives continuity and access to the person's retained material and experiences. A user need not visit every root to receive complete value.

Home richness should come from complementary contributions: a useful current fact, an interesting comparison, an attributed friend note, a possible next experience, or something already entrusted that matters now. It must not turn into a catalog of capabilities, a recap dashboard or a set of prompts requesting more input. A prepared possibility should contain enough substance to consider; opening it should deepen value, not reveal that the card was only a question.

### State the release boundary on three axes

1. **World coverage:** where and for which conditions are recommendations and practical claims adequately supported?
2. **Responsibility:** can this request be answered now, prepared as finite work, or explicitly followed over a supported period?
3. **Continuity:** what material is retained, what may later use it, and how does correction travel?

These axes are more informative than “v1 has Home, Places and AI.” An app can have all four roots and still fail the service. Conversely, constrained geography need not constrain cultural comparisons or source-based understanding to that geography.

### Actual implementation boundary

The September 6 Home map records an owner-backed portfolio spanning practical context, a substantive Places angle, an addressed human note and an ordinary Places opening, with renderer/destination/return tests. It also explicitly leaves richer prepared-result kinds, generalized casual sharing, retained intentions and full live reevaluation dependency-bound. These are **documented local integration checkpoints, not production activation or user-value evidence**. A canonical shared owner route cannot be advertised merely because the card leading toward it exists.

Optional conversational continuity, pre-Plan intention and assistance-instruction scope still have separate unadopted packets. Do not sell “everything you ask follows you through life” under the current Ask contract. Architecture can proceed systematically while those decisions are resolved; marketing must follow the effective contract and working delivery.

## 5. Own versus hand off: preserve the experience, not every operation

The decision is not “native good, external bad” or the reverse. Ask: **If we hand this off, does the person lose the context, judgment or continuity they came to Vesper for?** Then ask whether owning it creates an operational business we have intentionally declined.

| Capability | Vesper should own | Use providers / external continuation |
| --- | --- | --- |
| Place exploration | Relevant selection, interpretations, friend provenance, comparison and the person's context | Licensed facts, basemap infrastructure, directions and navigation |
| Bookable possibility | Fit, necessary caveats, exact destination, retained confirmation if supplied | Inventory, checkout, payment, cancellation and rebooking execution |
| Practical preparation | What changed, why it matters to this intention, viable alternatives and accepted bounded work | Specialized status feeds and provider-authoritative facts |
| Explanation / article / audio | The useful result, source context, appropriate lightweight presentation and continuity | Source publication or specialist playback where native duplication adds little |
| Social contribution | Audience-specific original, relationship to place/occasion, current shared state and useful receiving | Existing messenger as transport; do not build a replacement social messenger |
| Life continuity | Retained evidence, exact identity, refinding, correction and authorized later use | File providers as appropriate; not a forced full-life migration |

Google provides cross-platform Maps URLs for search, directions and navigation without an API key. That makes a scoped navigation handoff technically plausible. It does not supply Vesper with live place facts or prove the destination workflow is complete. [Maps URLs](https://developers.google.com/maps/documentation/urls/get-started).

Separately, Places API content has storage, display and attribution restrictions, with specific exceptions such as place IDs. Thus “use big-tech infrastructure” is not a license to build an unrestricted permanent world corpus from provider responses. Review the applicable agreement, region and service before choosing a supply pipeline; this is dependency identification, not legal advice. [Places API policies](https://developers.google.com/maps/documentation/places/web-service/policies).

### A handoff still needs a designed return

Before leaving, preserve the selected place, intended time/party where supported, reason for choosing it and unresolved questions. Explain whether the link checks availability, opens directions or merely opens a provider page. After return, do not infer a purchase, RSVP or attendance from the click. Accept a supplied confirmation through the existing source owner; avoid making confirmation upload a prerequisite for enjoying other value.

If the link fails, the original useful result should remain accessible with another supported continuation. Do not solve broken handoffs by quietly rebuilding booking execution. Some provider workflows will lose context; count the resulting user effort honestly.

### How this keeps the live engine central

The live engine's distinctive contribution should be **what a real-world fact means for this person's or group's intention**, including before anything goes wrong. A delay feed reports a delay; Vesper may establish that a proposed stop no longer fits, preserve the worthwhile part and offer an alternative. This requires reliable facts and authorized state; “we integrate a feed” is insufficient.

The engine must also help ordinary situations: whether a short outing fits the available window, whether a venue works for the group, what preparation is still missing. It should not become a universal background watch or dominate every Home item. A photo comparison and a friend note do not need an operational incident to justify their existence.

Minimize screens, not correctness. For example, moving expense interaction into Chat may reduce input burden, but extracted receipts, arithmetic and shared balances still need deterministic computation and inspectable state if supported. A model's fluent answer cannot replace those mechanisms. This is a boundary example, not a proposal to expand expense scope.

## 6. Distribution: deliver a gift before asking for adoption

### What the evidence supports

Apple Invites separates the paying creator from the receiver: iCloud+ is required to create invitations, while people can RSVP without an Apple account or device. This demonstrates a recipient-light product boundary inside a larger bundle, not willingness to pay for standalone Vesper. [Apple announcement, February 2025](https://www.apple.com/newsroom/2025/02/introducing-apple-invites-a-new-app-that-brings-people-together/).

Partiful provides browser invitation creation and link-based RSVP without requiring guests to download its app; its help center describes the core platform as free. That is a strong friction baseline, not evidence that no identity check is ever needed or that its economics transfer. [Partiful invitations](https://partiful.com/invitations/invitation-apps), [cost FAQ](https://help.partiful.com/en-us/articles/15525599-does-partiful-cost-money).

Aral and Walker's 2011 randomized Facebook field experiment separated targeted messages from broadcast mechanisms. Targeted messages were stronger per message while broadcast generated more total adoption through greater use. The accessible abstract supports measuring mechanism and denominator separately. The old platform setting does not justify copying unsolicited broadcast into Vesper. [Original study](https://pubsonline.informs.org/doi/abs/10.1287/mnsc.1110.1421).

Berger and Milkman's study of New York Times sharing linked practical usefulness, interest and surprise with transmission; separate experiments examined emotional arousal. Sharing an article is not adopting a subscription, and arousal is not Vesper's objective. The transferable hypothesis is that useful or interesting substance can give people a reason to share without engagement machinery. [Original paper, 2012](https://cssh.northeastern.edu/pandemic-teaching-initiative/wp-content/uploads/sites/43/2020/09/What-Makes-Online-Content-Viral.pdf).

### Three distinct mechanisms

1. **A personal offering:** a friend sends a place, observation, photo or comparison. Receiving it is complete value; the recipient owes no reaction. Vesper helps it remain understandable and usable later.
2. **A shared experience that works better:** a person contributes one suggestion or availability response without becoming a planner. The group benefits; organizer effort must actually fall, not move into follow-up outside the app.
3. **A result worth wanting for oneself:** a recipient sees a useful transformation and independently thinks of something they would bring. This is the adoption bridge, not the same event as opening a link.

The first is especially aligned with the founder's low-pressure social vision. Do not let the convenience of measuring RSVPs quietly turn every social interaction into occasion management.

An illustrative contrast: “Here is the place I mentioned, and my photo of the courtyard” is already a good human gift. A useful addition might clarify where it is or help a recipient assess an explicitly requested visit. An AI personality interpretation, invented comparison between friends or demand to add their own memory degrades it. Human authorship is not raw material awaiting mandatory AI improvement.

### Recipient experience and measurement

Recommend useful receiving before installation where technically and policy-feasible. Private material may still need proportionate identity verification. “No install” must not become “anyone with the link may see it.” General external receiving remains a design/implementation question, not certified current behavior.

Measure separately: unique recipients reached; successful permitted access; useful receipt; voluntary response; independent first personal use; later voluntary use; and, where applicable, purchase. Record organizer work, support and delivery costs too. Do not infer friendship quality from views, silence or response speed, or expose surveillance metrics to create pressure.

A recipient who never adopts can still be a product success and a legitimate service cost. Distribution succeeds only if enough people voluntarily become users relative to that cost—not because we redefine every invited person as acquired.

## 7. Payment: sell useful depth and capacity, not a busier AI

RevenueCat's 2026 report covers over 115,000 integrated subscription apps, primarily 2025 metrics, with eligibility thresholds. It reports higher median annual realized revenue per payer for AI apps but lower 12-month subscription retention across durations. These are observational subscription-level benchmarks, not Vesper forecasts or proof that AI causes churn. The page has inconsistent weekly figures in different sections; this memo uses no weekly number. [Report and methodology](https://www.revenuecat.com/state-of-subscription-apps).

Flighty's current pricing page packages practical depth around a familiar job and offers Pro on the first flight. This illustrates how a bounded experience can reveal a paid benefit; it does not establish Vesper's price, desired features or entitlement policy. [Flighty pricing](https://flighty.com/pricing).

### Recommended packaging hypothesis

Keep **one consumer membership** as the leading hypothesis. Its benefit is access to more substantial supported assistance: deeper research, richer requested preparation, higher capacity and explicitly bounded continuing help. Do not make “more content in Home” the main paid promise. Some people will pay for insight, others for practical relief or coordination; all should still recognize the same product.

The free experience needs useful immediate help, legible limits, basic receiving and meaningful access to entrusted material. It need not include unlimited generation, imports, media or monitoring. Paid expansion should not make shared truth tier-dependent, require friends to buy seats, or take correction and retrieval hostage. A larger capacity tier is not a larger permission grant.

A time-bounded occasion/travel offer remains a real alternative if benefits cluster into rare periods. Do not implement both billing models now. Compare them against actual recurrence and costs; an annual subscription is not validated merely because the philosophy spans a lifetime.

An understandable paid offer might describe the work available and limits before acceptance, rather than exposing tokens. However, “we will take care of your weekend” is too broad: identify the supported research/preparation and what remains with the user or provider. An accepted task should not stop halfway behind an unexpected upgrade demand. Define cancellation, service-period end and failure treatment before selling continuing responsibility.

### Economic evidence needed

Calculate cohort contribution from **net collected revenue minus attributable service cost**, including:

- inference, tools and research retries;
- licensed world supply and refresh;
- media/storage/delivery;
- accepted monitoring and failure recovery;
- free-user and recipient service; and
- variable support.

Keep fixed engineering and acquisition spending separate but visible. Allocate reusable world work without double-counting it; do not call it free. Measure both typical workloads and costly tails: broad research, repeated revisions, group-size fan-out, weak-source retries and a long accepted watch. Entitlement limits must be sustainable at the tail as well as attractive at the median.

A rich Home can reuse eligible world interpretation, owner facts and original human material. Bounded personal composition is not synonymous with generating a magazine per visit. The accepted [source-production worker decision](../decisions/2026-09-06-bound-source-production-worker.md) already separates ordinary serving from optional production; this memo does not activate the worker or add a scheduler.

No defensible price follows from the research alone. First compare comprehensible offers; then, when supported delivery exists, observe real purchase and renewal alongside actual costs. Survey willingness, initial payment and durable willingness are different evidence. Affiliate revenue remains supplementary and contingent, not the mechanism that makes an otherwise unviable membership work on paper.

## 8. Differentiation: compete against a capable stack

### The baseline has advanced

Google's March 2026 Ask Maps announcement describes conversational recommendations personalized from Maps activity. Its August Australian rollout describes live transit information, optional Gmail-based reservation context and resuming prior conversations; Calendar was still described as forthcoming there. Region, eligibility and real quality need hands-on verification. It is no longer credible to frame Maps simply as a static directory with an AI garnish. [March announcement](https://blog.google/products-and-platforms/products/maps/ask-maps-immersive-navigation/), [August announcement](https://blog.google/intl/en-au/products/explore-get-answers/ask-maps-australia/).

Gemini's January 2026 Personal Intelligence announcement explicitly describes combining retrieval and reasoning across connected personal sources. “An assistant that knows your history” is therefore not an exclusive category claim. This is an announced capability baseline, not a claim that every user has it or that it works perfectly. [Gemini announcement](https://blog.google/innovation-and-ai/products/gemini-app/personal-intelligence/).

Compare Vesper with **a capable personal assistant plus maps, messenger, calendar and existing saved material**, not with each competitor artificially isolated. Let participants use their familiar tools well. Also run an equal-evidence comparison to isolate whether Vesper's judgment and presentation add value rather than merely being given more context.

### Candidate advantages, not established moats

| Potential advantage | What a person would notice | What would fail to establish it |
| --- | --- | --- |
| More worthwhile understanding and discovery | A source-grounded connection, perspective or practical possibility they would not readily have obtained | A callback to what they already said, or merely longer prose |
| Less reconstruction across time | Prior permitted material changes today's help without repeated explanation | A generic memory mention, or an app that requires continual correction |
| Coherent personal and shared experience | Friends' contributions and actual shared state remain useful while private context stays private | A group chat wrapper or an extra planning obligation |
| Better situated help | Current facts change the recommendation or preparation in a useful way | A status alert detached from the person's intention |
| Lower total interaction burden | Asking, using, sharing and refinding work together with less effort | Fewer screens but more prompting, checking, copying and recovery |

**Integration is valuable only when these combinations change the experience.** A shared database or elaborate ontology is not a consumer advantage by itself. Likewise, good correction is a necessary service quality, but an entire pitch about governance will not explain why the product is desirable.

The compounding hypothesis has several parts: better reusable world judgment, permitted personal continuity, useful relationship context, and an increasingly well-designed service. Only some are network effects. More registered friends does not guarantee more value, and private history is not an asset available for unrestricted reuse. Do not label all accumulated data a moat.

### A fair comparative portfolio

Use the existing manuscript rather than inventing another showcase world:

- One question or photograph, no history: can Vesper offer useful substance at competitive effort and latency?
- An open local window with one anchor: are possibilities genuinely worthwhile and feasible?
- A friend's place contribution: is the original useful on receipt, with optional help that adds rather than replaces human meaning?
- A changed shared arrangement: does the system reduce the whole group's checking and reconciliation work?
- A later return after silence: can entrusted material improve help without being re-entered or inaccurately generalized?

Compare natural-use effort and equal-evidence quality separately. Track useful result, novelty that matters, checking burden, total user/recipient effort, latency, return after absence and service cost. Do not penalize the alternative merely for using several apps; count switching only where it creates real work or lost value. Counterbalance order and use different but comparable cases to reduce learning effects. Research participation is separate from the production experience; do not turn Home into a daily questionnaire.

If Vesper wins only when other apps are denied context, that is a weak differentiation case. If it wins only through hidden manual founder work, that is a delivery gap. If it performs well but people still choose their existing stack, investigate whether the benefit matters enough to justify another app before expanding features.

## 9. Three launch propositions for the same system

These are comparison drafts, not canonical copy. All three must show the **same honest examples and boundaries**: a useful first question, a local possibility, a human contribution and practical adaptation with later retrieval. An example dependent on unfinished capability must be labeled as a design concept, not demonstrated as working.

### A — Everyday-led: recommended first hypothesis

> Bring Vesper something you're wondering about, somewhere you want to go, or something a friend sent. Get useful answers and possibilities that fit your life—with less work connecting the pieces.

Best fit: people with recurring questions and scattered real-world interests. Strength: a familiar low-setup entrance into the whole product. Risk: still sounds like an assistant unless the examples demonstrate new substance and useful continuity. Avoid making “connecting pieces” a requirement to bring many pieces first.

### B — Social-led

> Good things from your friends, easier to enjoy together. Vesper makes the places, suggestions and moments you share useful—without turning everyone into a planner.

Best fit: people already exchanging suggestions and initiating small gatherings. Strength: visible human benefit and a natural receiving experience. Risk: narrows perceived scope to invitations, excludes someone with no active friends and creates organizer expectations. Keep solo value in the same demonstration.

### C — Experience/travel-led

> Get more from where you are, with less to figure out. Vesper helps you understand what catches your attention, find worthwhile possibilities and make the day work—away or at home.

Best fit: unfamiliar places or people actively seeking an outing. Strength: concrete circumstances make the benefit legible. Risk: “away or at home” may not overcome the first impression of a travel guide. Everyday examples must be real value, not promises of post-trip recaps.

These are audience propositions, distinct from the prior balanced/discovery/practical headline experiment. Do not combine every variation into a large factorial study before learning whether newcomers understand the basic offer.

## 10. Recommended decisions and sequence

| Decision | Recommendation now | Evidence that should change it | Where it belongs after approval |
| --- | --- | --- | --- |
| First audience | Existing question/save/share behavior around ordinary life | Stronger independent choice and sustained benefit in a social or travel cohort | Growth Strategy |
| First offer | Complete personal, spatial, social and practical value within explicit coverage | A promised family cannot deliver useful value without disproportionate work | Existing integration and surface plans, plus launch service description |
| Ownership | Own interpretation, continuity, shared state and situated judgment; use provider execution | A handoff destroys the core payoff, or native work duplicates a specialist without benefit | Product Vision and Scope and existing owner contracts |
| Distribution | Recipient-complete value with voluntary independent adoption | Organizer costs rise, recipients feel recruited, or access friction blocks the gift | Multiplayer/Growth and existing receiving design |
| Packaging | One membership hypothesis; episodic alternative for comparison | Observed demand is episodic, renewal is weak or supported costs do not fit | Monetization Strategy |
| Differentiation | Better combined outcomes and lower total work against a capable stack | Equal-evidence quality or natural repeat choice is not better | Venture Path and comparative research |

Proceed in this order without freezing independent integration work:

1. **Describe the supported service.** Use the existing owner/readiness inventory to label available, gated, proposal-dependent and unsupported behavior. Include world supply, meaningful handoffs and recovery, not only feature existence.
2. **Compare the three audience propositions.** Use the prior four comprehension questions, recent real behavior and the same examples. A small exploratory set can expose misunderstandings; it cannot estimate market size or conversion.
3. **Exercise the complete portfolio against alternatives.** Include sparse context, absence and lightly participating recipients. Revisit the affected surface or owner when a failure is operational; revisit the proposition when the value itself does not matter.
4. **Characterize the cost of that same service.** Do not run economics on a cheaper, emptier product than the one shown in design. Reusable supply, personal preparation and recipient costs all count.
5. **Choose one initial commercial offer when it can be delivered.** Observe purchase and subsequent benefit/renewal before expanding claims. Do not implement competing billing systems as a substitute for deciding.
6. **Amend canon selectively.** Reconcile the Content as Infrastructure drift; change Growth, Scope, Multiplayer, Monetization or Venture documents only for actual founder decisions. Keep hypotheses and research evidence here.

Review direction at these decision boundaries rather than after arbitrary feature counts. The key question is not whether every subsystem is complete. It is whether the system, within declared scope, creates a recognizable and worthwhile experience that people can choose without inheriting its complexity.

**Bottom line:** Vesper can remain ambitious while being easier to understand. The strongest focus is a stable responsibility to the person—not a long capability list and not one narrow loop. Bring something because the app helps now; receive worthwhile value; carry it into actual life with less unwanted work; benefit later where continuity is wanted and authorized.

## 11. Consumer-experience follow-through: independent entrances

The subsequent consumer-experience research sharpened the next deliverable:
**three independent entrances and a return after absence**, rather than a
scheduled first-week curriculum. The founder approved applying that direction.
The concrete specimens now live in [the existing situated-value manuscript
§14](situated-value-decision-matrix-2026-09-06.md#14-three-independent-entrances-and-a-return-after-absence),
not in a second product manuscript or an app implementation.

### Evidence that shaped the pass

- **Initial categorization matters.** Moreau, Markman and Lehmann's two
  experiments found that the first plausible category cue influenced
  expectations about unfamiliar products. Applying this to a chat box, trip
  dashboard or editorial feed is our design inference; their 2001 product study
  did not test AI apps. It supports checking what each entrance teaches, not
  asserting a permanent first-impression law. [Original paper](https://business.columbia.edu/sites/default/files-efs/pubfiles/963/963.pdf).
- **Capability should become legible through relevant use.** Google's PAIR
  guide recommends staged introduction, concrete benefits and low-risk
  experimentation. It also warns against assuming that experimentation should
  shape future personalization. This is practitioner guidance, not retention
  evidence. Our application preserves accessible capabilities without a
  required feature tour or new inference permission. [Mental models](https://pair.withgoogle.com/guidebook-v2/chapter/mental-models/).
- **Situation can supply first-use context.** Google's April 2025 multimodal
  AI Mode announcement describes answering questions about supplied images.
  This establishes a competitive interaction baseline: one item can support
  immediate help without a life archive. It does not establish Vesper's
  superiority or any provider's actual result quality. [Announcement](https://blog.google/products-and-platforms/products/search/ai-mode-multimodal-search/).
- **Enjoyment and valued outcomes both matter.** The 497-person survey in
  *Beyond Intrinsic Motivation* explored different motivational patterns in
  reported technology experiences. Enjoying use and valuing what it enables
  need not be identical. These are exploratory associations, not proof that a
  feature causes return. We therefore allow reading, practical relief and
  enjoyable receiving to be complete outcomes. [Research version](https://arxiv.org/html/2410.12991v1).
- **Stable use can accommodate changing content.** Spotify describes daylist
  as an adapting playlist. Our inference is to make the kind of Home value
  recognizable even as its contents vary—not to copy music-refresh cadence,
  infer mood or guarantee an endless supply of personalized novelty.
  [Spotify discovery guidance](https://newsroom.spotify.com/2025-01-22/4-tips-to-supercharge-your-discovery-on-spotify-in-2025/).
- **Absence has more than one meaning.** Epstein and colleagues surveyed 193
  former self-trackers and interviewed 12, finding varied reasons for stopping
  and varied experiences afterward. The domain is self-tracking, not Vesper;
  it supports designing return and access without assuming failure or guilt,
  not dismissing evidence of abandonment. [Original paper](https://homes.cs.washington.edu/~jfogarty/publications/chi2016-abandonment.pdf).
- **Small social contributions can be the value.** Snapchat research with 154
  college students and 28 interviews associated mundane sharing with enjoyment
  and reduced self-presentational concern, but not equivalent social support.
  The sample and observational design limit generalization. We preserve original
  human expression without demanding AI novelty or reciprocal effort.
  [Original paper](https://www.yardi.people.si.umich.edu/pubs/Schoenebeck_Snapchat16.pdf).

Sources were reviewed September 6, 2026. Academic findings, practitioner advice,
advertised product behavior and Vesper-specific recommendations remain distinct.
No newcomer study or hands-on competitor comparison was conducted.

### What the manuscript now decides for design review

N1 applies an explanation to two supplied photographs; N2 offers a concrete
local possibility and a substantive world comparison without personal history;
N3 delivers a friend's original recommendation with useful place context. R
tests a return after two questions, one deliberately kept place and little other
participation, with a separate no-retention variant. The existing fictional
venues and stipulated image geometry remain clearly labeled; no live listings
or image-analysis results were manufactured.

Each specimen identifies received value, optional continuation, work removed,
what remains human, cross-root effects, implementation dependencies and the
expectation it should establish. Each also includes a critique: a capable
assistant may match N1; N2 depends heavily on world supply; N3 does not by itself
prove adoption; R must work without unauthorized memory or fabricated freshness.

The working recommendation is **N2 as the strongest composition hypothesis for
revealing breadth**, while N1 and N3 remain independent legitimate entrances.
This is not an adopted launch route or an onboarding experiment result. The
four product moves remain a repertoire. The next review should establish
whether newcomers can accurately predict a useful next encounter without
expecting unsupported retention, background responsibility or provider action.

### September 7: real-source follow-through

The [NYC newcomer companion](nyc-newcomer-connected-home-specimen-2026-09-07.md)
now replaces fictional supply for one complete encounter with primary-source
material. It follows Home into Places and Chat, separates exact retention from
mere interest, specifies a later low-participation return, and changes one fact
to add an addressed friend recommendation. Its code evidence identifies
continuation and supply gaps; passing focused tests does not certify the
complete experience. No launch promise, runtime policy or production activation
changes through this specimen.

## 12. Audience–entrance recommendation and acquisition packet — September 7

### Recommendation and status

**Lead with people who already save or send real-world possibilities, at the
moment they want help understanding or using one of them.** Recruit from that
behavior, not an identity such as cultured traveler, busy professional or power
planner. Someone can want a better explanation without wanting an outing.

The founder requested this concrete follow-through. It is a recommended
recruitment and experience-review packet, not permission to contact people,
spend on acquisition, publish promises or launch an unfinished service. NYC
remains a coverage-dependent candidate; no new audience or geography is adopted
into canon here. Existing engineering lanes continue against the whole product.

### The audience and the moment

Look for a recent example of a person saving a place/event, sending a friend a
recommendation, or asking a question sparked by something encountered. The
relevant friction is that the fragment did not yet become useful understanding
or a possibility they could judge—not that the person failed to complete a plan.
Do not require all three behaviors, an upcoming trip, friends on Vesper or a
rich archive. Include people who enjoy choosing and researching.

The leading entrance is **one thing already in front of the person**: a question,
link, photograph or recommendation. They need not fetch a document to qualify;
ordinary language is sufficient. No initial library import, contact sync,
calendar access or memory opt-in should be needed for the immediate payoff.

| Entrance | Why someone would try it | Principal weakness to investigate |
| --- | --- | --- |
| **Leading: help with something that caught my attention** | Existing attention supplies a reason to ask now; useful help needs little setup | Could be indistinguishable from a good general-assistant answer |
| **Independent alternative: show me something worthwhile** | Home demonstrates breadth without requiring a question or capture | Depends on adequate current world supply; easily becomes a generic city guide |
| **Distribution entrance: receive something from a friend** | The human contribution provides immediate context and motivation | Enjoying the contribution does not necessarily create a reason to adopt Vesper |

This sharpens §9's everyday-led proposition, rather than replacing it. N2/Home
remains the strongest *composition hypothesis for showing breadth* in §11.
Recruitment moment, first destination and breadth demonstration are different
choices. Do not route every incoming question or shared object through Home.
Travel remains a seasonal acquisition comparison, not a fourth required test
arm or a mandatory bridge to everyday use.

### Proposed message and honest first payoff

Message draft for review, not approved public copy:

> Something caught your attention? Bring it to Vesper. Understand it better,
> discover what else it opens up, and get help taking it further if you want.

It must earn specificity through an example, not rely on this wording alone.
The exhibition is a controlled demonstration candidate, not universal onboarding.
“What makes it worth seeing, and could it fit into Saturday afternoon?” is a
well-specified benchmark request, not language a newcomer should have to supply.
Also exercise a bare link or “What do you think of this?” without first teaching
the four product moves. [Section 13](#13-first-encounter-experience-specifications--september-7)
specifies concrete first responses, optional continuations and legitimate endings.

The complete first payoff should include a substantive explanation or judgment
from actual evidence; relevant practical bounds where supported; and optional
depth or continuation. A worthwhile answer can end there. Do not require an
itinerary, a save, a social invitation or a trip through all four roots.

Use one fixed evidence packet to compare three introductions:

- **Balanced:** “Understand what caught your attention, and see what you can do with it.”
- **Discovery-led:** “Find a worthwhile way into somewhere or something new.”
- **Practical-help-led:** “Work out whether this idea fits your afternoon, with less to figure out.”

Show the same explanation, possibility, practical limits and optional human
continuation at comparable fidelity. Change the opening message, not source
quality or feature availability. Rotate presentation order in a qualitative
review; repeated exposure and small samples cannot establish conversion lift.
Observe whether people can name a use and its limits before explaining the
philosophy to them. None of these messages settles the company category.

Before showing a working demo, pin its build and label each promised outcome:
working, gated, prototype-only or unsupported. Content must establish usable
supply for the example; Integration must establish its actual receiving path.
Dates and access conditions in old specimens need rechecking for a live claim.
Use labeled prototypes when necessary, but do not count their reactions as app
activation. No promise of automatic memory, accepted monitoring, private guest
access or provider execution follows from a compelling demonstration.

### Proposed first recruitment batch

Start with a **small qualitative batch of approximately twelve adults**, a
practical founder workload rather than a statistically powered sample. Include
people outside the founder's close circle and a few independently consenting
friend pairs. At least some people must encounter Vesper with no participating
friends. Differences between these groups are descriptive, not causal evidence
that a social entrance performs better.

Ask for recent behavior: “Was there something you saved, sent or wondered about
recently that you wanted to do more with?” They may describe it or use a supplied
public example; do not require private screenshots or third-party conversations.
Recruitment draft: “I'm building Vesper and would like feedback on whether it
helps with something like that. It isn't necessary to import your history or
invite friends.” Disclose prototype and working-app boundaries accurately.

First observe the unaided attempt, then offer help. Record founder assistance
separately so manual explanations, research or fixes do not masquerade as
product capability. A scheduled research debrief is not a natural return.
Compensation, if later approved, should not depend on praise, sharing or adoption.
No participant outreach, recording or recruitment spending is authorized here.

### Distribution: let the value travel before the installation request

The sender should have a reason to share independent of helping Vesper grow.
Examples include their own photograph and note, a useful comparison, or an
actual invitation. Make the intended recipient's permitted value available
before an install request where feasible; proportionate identity verification
may still be necessary for private material. Public links are not a substitute
for private receiving. Do not broaden an audience to remove onboarding friction.

After receipt, a contextual invitation to personal use can be appropriate:
“Have something of your own you want to explore?” It should never block reading,
pressure a reply or require reciprocal posting. Sharing a link, receiving value,
creating an account and initiating a personal use remain different events.
A satisfied non-adopting recipient is legitimate, including their service cost.

Prioritize founder recruitment first, then voluntary product sharing. Consider
small matched creator/community demonstrations after the shown service works.
Defer broad paid acquisition and mass public-content production until repeated
usefulness and cost are understood. These are priorities, not a campaign launch
or a forecast that sharing will produce self-sustaining growth.

Research checked September 7: [Granola's launch](https://www.granola.ai/blog/announcement)
illustrates a familiar entrance into a broader ambition; its
[sharing documentation](https://docs.granola.ai/help-center/sharing/sharing-notes)
separates receiving a note from workspace membership and paid seats.
[Partiful](https://partiful.com/invitations/make-invitations) advertises
browser-based invitations without guest app installation. These are product
patterns, not measured Vesper acquisition effects. [Paul Graham's early-recruitment
essay](https://paulgraham.com/ds.html) supplies practitioner reasoning for direct
founder recruitment, not controlled evidence or permission to conceal manual work.

### Evidence to collect and decisions it changes

Keep a consented research record separate from product personalization. Do not
add passive social-view reporting or a new tracking SDK for this packet.

| Question | Evidence | Consequence for the recommendation |
| --- | --- | --- |
| Does the offer make sense? | What someone would use it for, expects before setup, sees as different, and would not expect it to do | Rewrite the entrance if it implies a travel planner, generic chat or unsupported concierge responsibility |
| Does first value repay the effort? | Actual help received, time/setup, mistakes and founder assistance | Repair delivery if the problem is substance or reconstruction; do not solve it with a stronger claim |
| Is there a reason to choose it again? | Independent later use versus prompted research participation; what triggered the return | Distinguish a good one-off answer from a repeatable service; low frequency alone is not failure |
| Does sharing distribute the product? | Permitted access, recipient benefit, then voluntary first personal use and later use where observable | Improve receiving or the adoption bridge; never count every guest or link open as acquired |
| Can the offer be supported? | World-data/model/recipient costs and founder/support effort for that same experience | Bound coverage or costly work; do not extrapolate cheap fixtures into acquisition economics |

Review the batch for recurring patterns, counterexamples and severity, not a
fabricated success percentage. Understanding with no useful payoff calls for
product work; usefulness with no repeat choice calls for examining recurrence
and alternatives; useful sharing with no adoption calls for examining the
recipient's own need. Favor another entrance if it earns clearer independent
choice without increasing burden or making unsupported promises. A small
founder-recruited sample cannot establish market size, CAC, retention or pricing.

### Receiving lanes and next decision

- **Strategy here:** owns audience/message comparisons and a concise findings
  record in this section; founder decides any launch exposure or canon change.
- **Content:** supplies coverage, permitted evidence and costs through the
  [existing world-supply roadmap](recommendation-world-supply-architecture-and-roadmap-2026-09-07.md).
- **Integration:** identifies working build paths and missing consumer connections
  in its existing roadmap; no separate acquisition architecture.
- **Social:** owns sender/recipient friction and optional continuation through the
  social design brief, `vesper-social-experience-design-brief-2026-09-07.md`
  (**local WIP** at the strategy commit boundary).
- **Life:** supplies authorized retrieval and continuity; it is not an onboarding
  prerequisite or a requirement to retain each question.

Before deciding whether to authorize the research batch, review the concrete
encounters in §13 for actual payoff and honest capability boundaries. This packet
supports preparation only. No new engineering lane, outreach, paid channel,
runtime permission, public promise or scheduled follow-up is created by this update.

## 13. First-encounter experience specifications — September 7

### 13.1 What this pass specifies

**Earn a first use through a complete small benefit; make further capability
available without making continuation the price of that benefit.** These are
experience and content specifications, not rendered designs, working app output,
research results or a narrowed implementation roadmap. The whole-system work
continues; the encounters make its intended consumer payoff inspectable.

Three entrances receive the same review structure below: curiosity, practical
help and a human offering. They are not three modes, onboarding tracks or new
objects. Two evidence worlds prevent the exhibition from defining the product:

- **E — public cultural material:** MoMA's *Frida and Diego: The Last Dream*,
  plus its collection and curatorial material. Primary sources were checked
  September 7. This is a real-source content specimen, not a verified visit.
- **D — ordinary dinner at home:** a deliberately fictional recipe, a supplied
  kitchen constraint and a friend's authored contribution. These are synthetic
  interaction fixtures, not actual user history or a tested cooking recommendation.

For comparison, hold the evidence, fidelity and access constant *within* a
world. E-curiosity versus D-practical cannot isolate the effect of an entrance:
topic, motivation and evidence differ. Nor should readers mistake all the
designer notes below for text that appears on a phone.

### 13.2 Curiosity — one detail changes what the person can see

**Arrival:** In Chat, a newcomer pastes the exhibition link and asks, “Anything
interesting here?” No prior interests, trip history or visit are assumed. If
they send the link alone, useful interpretation still comes first; its custody
follows the actual Bring/Ask affordance rather than this example inventing a
new retention rule.

**First response draft — the useful substance is already visible:**

> **A self-portrait with room for a friend.**
>
> Kahlo paired *Fulang-Chang and I* with a mirror when she gave it to her friend
> Mary Sklar. MoMA's curator explains that the mirror let Sklar see herself
> beside Kahlo. It changes the work from a picture of one person into a way for
> two people to appear together—even when they're apart.

The gift and mirror account comes from [MoMA's curatorial essay](https://www.moma.org/explore/inside_out/2009/12/03/a-close-look-frida-kahlo-s-fulang-chang-and-i/);
the last sentence is our interpretive framing of that account, not an invented
quote or claim about the user's relationships. The [collection record](https://www.moma.org/collection/works/79374)
identifies the two-part work; the [exhibition materials](https://press.moma.org/exhibition/frida-and-diego-the-last-dream/)
include it. A source affordance belongs beside the response, without requiring
the person to open it to discover the substance.

**What has been delivered:** a specific, grounded way of reading one work,
beyond the exhibition title and dates. It is not necessarily new to this person.
If they already know it, a longer retelling is not improvement: another supported
angle or an honest stop is preferable. Do not claim “you never noticed this.”

**Optional continuation:** “See the work” opens the exact authoritative artwork
page, retaining the surrounding answer on return. No illustration or press
image is reproduced in this packet. Native image use requires its own rights
check; a compelling mockup must not assume licensed media exists.

If the person instead asks “Could I go Saturday?”, shift to their practical
question with the same exhibition identity. MoMA lists the exhibition through
September 12; this alone does not establish ticket availability or fit in an
afternoon. The related opera ran May 14–June 5, so it is not a simultaneous
September option. Ask for a time constraint only if needed to judge fit; do not
request a full itinerary. Recheck dates and admission before any live demo.
[MoMA exhibition announcement](https://press.moma.org/exhibition/frida-and-diego-the-last-dream/).

**Comfortable ending:** they understand the work differently and leave. No
reflection question, museum checklist, taste inference or automatic Home
callback. Not visiting is not failed conversion.

**Hard critique:** a capable assistant with these sources can produce this
answer. This earns a content-quality benchmark, not a moat. Vesper must establish
that it finds and presents worthwhile substance reliably, at competitive effort
and cost; later coherence cannot excuse a generic first response.

### 13.3 Practical help — adapt the thing, not the person to a workflow

**Arrival:** A newcomer brings recipe D to Chat: “Could I make this for six
tonight? I've only got one big pot.” Nothing about their pantry, guests' needs,
available time or pot capacity is known beyond that sentence.

**Declared synthetic evidence:** D serves four and specifies 400 g dry pasta,
600 g tomatoes and 120 g cheese. Its method combines the uncooked tomatoes and
cheese in a large bowl, boils pasta in one pot, then tosses them together. Those
are stipulated recipe facts for this comparison, not inferred from a photograph.
No preparation time, actual stock, dietary suitability or culinary success has
been verified. The fixture is intentionally simple enough to audit.

**First response draft:**

> **One pot works for the method—the sauce isn't cooked separately.**
>
> For six recipe-sized portions: **600 g pasta · 900 g tomatoes · 180 g cheese.**
> Mix the sauce in a large bowl while the pasta cooks, then toss together.
>
> The remaining question is capacity: if 600 g of pasta crowds your pot, use
> two batches. The quantities scale by 1.5; the cooking time doesn't.

**What has been delivered:** scaled quantities and the resolution of the actual
equipment concern, without “tell me your cooking profile,” a shopping project,
an Occasion or six guest accounts. The capacity caveat is specific enough to
use; “Can you tell me more?” would send the work back to the person. If the
question were only “Can I do this tonight?”, give the supported method facts
first and ask about time only if it changes the requested judgment.

**Optional continuation:** the exact method remains accessible as “Method for
six,” preserving steps as well as quantities. Do not add a shopping-list action
by default. If the person says “I have 700 g tomatoes,” respond to that actual
constraint; do not treat it as evidence of enduring pantry contents. A requested
method view is a normal result, not a new recipe-management product.

**Comfortable ending:** they know whether the equipment is the problem and can
use the adjusted recipe. A follow-up need not be solicited. They may choose a
different dinner. Vesper has not checked guests' restrictions, bought ingredients,
accepted a timer or promised to follow tonight's meal.

**Hard critique:** scaling and equipment reading are table stakes. Do not sell
them as novel intelligence. The potential advantage is that a person can move
from a friend's exact recipe to their own constraint without re-finding,
re-pasting or inheriting the friend's settings—and later refind it if deliberately
kept. That receiving-to-help transition is a design target to verify, not a
shipped result or permission for automatic cross-context memory.

### 13.4 Social — a small human offering, already worth receiving

**Sender gesture:** Fictional friend Maya selects her own dinner photograph,
attaches recipe D and sends it to one friend with her words:

> Made this with the last tomatoes from the market. The sauce never touches
> the stove. Thought you'd like it.

The photograph and note are synthetic placeholders described here, not assets
we have inspected or a claim about a real friend. Sending this is not inviting
the recipient to dinner, requesting a reaction or granting public Place use.

**First receiving composition:** show **Maya**, her photograph, her unchanged
note and the attached recipe. Show the core quantities and method from D beside
the attachment when permitted, so the recipient can understand the idea without
opening a second site. Do not insert “Maya knows how much you love effortless
Italian cooking,” an AI paraphrase of her note or a relationship interpretation.
There is no necessary AI-written response before the human offering.

**What has been delivered:** a glimpse of a friend's evening and something
specific the recipient can try. Recipe extraction can remove work, but the
photograph does not need an invented insight to justify its place. Compare
original-only with original-plus-method; remove the addition if it merely
lengthens receiving. This follows the original-first direction in
`vesper-social-experience-design-brief-2026-09-07.md` (**local WIP**).

**Optional continuation:** keep a normal private Reply available. A secondary
“Ask about this” starts with the exact recipe attached; if the recipient asks
the six-person question in §13.3, the app should provide that help without
making them supply the recipe again. Their kitchen constraint and private
answer do not go to Maya. These are alternatives, not two tasks to complete.

If the recipient writes “Want to make this together Friday?”, help send that
bounded invitation to the chosen friend. Do not create an accepted gathering
or infer either person's availability. Shared preparation becomes relevant only
after an actual shared intention; casual receiving must not become a setup flow.

**Comfortable ending:** enjoy the photo, read the note, close it. No reply debt,
viewed/used report, automatic appreciation or request to contribute an equivalent
artifact. If external private receiving is not implemented, label its mockup as
a target. No-install receiving does not mean anonymous access to private material;
necessary access checks may precede private content, but an app-growth request
must not block an otherwise authorized recipient's value.

**Hard critique:** messenger plus a recipe link already delivers much of this.
Vesper earns extra value only where exact attached context, useful adaptation,
permitted refinding or later coordination genuinely reduce effort. Let a
recipient use their familiar messenger/assistant well in the comparison.
Receiving happily without adopting remains success for the offering, not
evidence of acquisition.

### 13.5 One system, not a tour through four roots

| Surface | What these encounters can require | What they do not authorize |
| --- | --- | --- |
| **Chat** | Direct questions and private help on the exact received item; no re-pasting within the supported continuation | Mandatory chat before receiving value, automatic durable taste learning |
| **Home** | The permitted friend offering can be useful on view; eligible world material can supply an independent substantive unit | Repeating every answer as a card, turning the dinner question into a tonight reminder, gating all Home value behind capture |
| **Places** | Exact exhibition/place context when spatial exploration or a visit becomes relevant | Inventing a restaurant or current friend location from a home-cooked dish photo |
| **Life** | Refind an explicitly kept recipe or other admitted Source with its identity and repair path | Inferring that dinner happened, that a museum was visited, or that every Ask was kept |

Not every encounter uses every root. Home's independent, no-question entrance
remains covered by the [NYC newcomer specimen](nyc-newcomer-connected-home-specimen-2026-09-07.md).
These three encounters do not demote it or prescribe the whole Home feed.
The practical engine is expressed in situated judgment and correction, not an
extra engine card. None of these small requests accepts background monitoring.
Existing [contribution authority](../systems/contribution-and-consequence.md)
and unresolved continuity proposals still govern; this section changes neither.

### 13.6 Comparison and evidence plan

**Keep four questions separate:**

1. **Comprehension:** show one fixed encounter at the same fidelity under the
   balanced, discovery-led and practical-led openings in §12. Ask what the
   product is for, what arrives before setup, what differs and what it does not
   do. Don't change the underlying answer to favor a message.
2. **Immediate usefulness:** use something personally relevant where the
   participant is comfortable, or a public substitute. Observe an unaided
   attempt before founder help. Personal relevance is not a controlled message
   comparison, and sensitive material is not the price of participation.
3. **Transfer:** before showing another example, ask “Is there another situation
   of your own where this might help?” Record their answer or lack of one before
   explaining capabilities. Then optionally show the other evidence world;
   recognition after teaching is different from spontaneous understanding.
4. **Independent choice:** observe a later self-initiated use only when an
   appropriate functioning service and consented research arrangement exist.
   A suggested second task, scheduled debrief or statement of intent is not
   evidence of natural return. No follow-up automation is created here.

Cross the entrances within the same world when investigating a suspected topic
bias: E can support curiosity, a supplied Saturday constraint, or a friend's
authored perspective; D can support understanding the method, equipment/quantity
help, or Maya's offering. Keep friends fictional in fixtures, and do not fabricate
their experience from public material. Not every participant needs all six
combinations: that would itself become a curriculum and introduce learning effects.

Research rationale, checked September 7: [NN/G's task-scenario guidance](https://www.nngroup.com/articles/task-scenarios-usability-testing/)
supports realistic goals without teaching the route to the answer. Its [real-data
guidance](https://www.nngroup.com/articles/users-real-data/) distinguishes the
qualitative value of personal relevance from the variability it introduces into
quantitative comparisons. These are practice recommendations, not evidence that
our particular encounters work. [Webb and Sheeran's 2006 meta-analysis](https://pubmed.ncbi.nlm.nih.gov/16536643/)
found that experimental changes in intention translated into smaller changes in
behavior; it supports separating stated interest from action, not forecasting
Vesper retention from an unrelated effect size.

For every comparison, record what helped, what was already known, unnecessary
reading/taps, missing facts, checking/reconstruction effort, latency and manual
founder work. An equal-evidence assistant comparison tests judgment; a familiar-
tools comparison tests total effort. Neither has been run for these specimens.
Recipe arithmetic should be computed deterministically; world facts should be
source-bound and refreshed where relevant. Human material should retain its
author. Don't assume each small response needs fresh deep research or a bespoke
article: cost the actual supply, reuse, private adaptation and receiving path.

### 13.7 Review recommendation and next handoff

My recommendation is **keep all three as a compact review portfolio**, with
curiosity showing depth, dinner showing ordinary practical range, and receiving
showing human value. This is not a choice to launch three separate products.
The mirror example now supplies real substance; the dinner example is deliberately
mundane; the social example succeeds without compulsory AI prose. Their weakness
is equally explicit: none alone establishes switching or retention.

Before a design or engineering handoff, review whether each first response is
worth receiving with every continuation removed. Then review the optional exact-
context transition for genuine work removed. If those fail, revise the payoff,
not the headline or the number of actions. If they pass, the existing lanes can
mark the named paths working, gated, prototype-only or unsupported against a
pinned build before any newcomer session. This update itself implements no app
path and authorizes no outreach, spending, policy change or canonical rewrite.

## 14. Learnable breadth, judgment, dependable value and voluntary preference — September 7

### 14.1 Recommendation and what this round adds

**Make the breadth discoverable through valuable encounters; make the service
dependable by being precise about what each encounter delivers.** We should not
choose between a feature catalog and a single-purpose app. A person can understand
an increasingly broad Vesper through recognizable situations: a question about
something, an appealing possibility, help making something work, something from
a friend, and something worth finding again.

The working proposition is not “Vesper does everything.” It is: **something you
ask, encounter or receive can become more understandable, more useful, or an
opening into real life—with less rebuilding of context when you continue.**
This is an internal explanation to examine, not a replacement public headline.
Current usefulness must stand on its own; continuity is an additional benefit,
not a mandatory demonstration in every response.

The existing docs already establish much of the foundation:

- The [matrix](situated-value-decision-matrix-2026-09-06.md)'s §15 draft (**local WIP**)
  distinguishes character, situational fit and feasibility, and already rejects
  a universal option count or novelty quota.
- [The NYC newcomer specimen](nyc-newcomer-connected-home-specimen-2026-09-07.md)
  makes Home an independent entrance before rich history or active friends.
- `nyc-recommendation-judgment-specimen-pack-2026-09-07.md` (**local WIP**)
  supplies source-backed candidates and contrasting selection approaches.
- [The world-supply roadmap](recommendation-world-supply-architecture-and-roadmap-2026-09-07.md)
  owns the implementation of bounded investigation, selective retention and
  receiving. This round does not create a competing engineering lane.
- Sections 12–13 here separate first payoff, comprehension, transfer, return and
  payment. The new work is choosing how those encounters reveal the product,
  and examining evidence that could overturn our preferred choices.

This is targeted desk research, not a systematic review, usability study or new
code-readiness audit. Primary 2025–2026 research is supplemented by older choice
and habit research where it addresses the mechanism. Access and domain limits
are stated below. Publication recency does not make a study directly transferable
to Vesper. No participant behavior, switching advantage or price is established.

### 14.2 Learnable breadth: demonstrate nearby usefulness, without making a curriculum

**Evidence complicates “no onboarding.”** Asisof, Nißen and von Wangenheim's
AMCIS 2025 work reports two studies of conversational-agent onboarding. Their
framework includes capabilities and limitations, disclosures and validation,
and guidance and contestability. The abstract reports relationships between
onboarding breadth/depth and user perceptions. This pass could read the official
abstract, not verify the full methods or sample. It supports investigating what
orientation people need, not a claim that a long onboarding flow improves Vesper
adoption. [Official proceedings record](https://aisel.aisnet.org/amcis2025/sig_hci/sig_hci/4/).

**Understanding the machinery is not the same as using it well.** Rismani and
colleagues' CHI 2026 study primed 48 people with functional or structural
descriptions of a writing assistant, then used a cover-letter task with some
deliberately ungrammatical suggestions. Structural explanations improved system
understanding and perceived usability, but that condition produced more errors.
This finding comes from the institutional abstract; it does not establish the
best onboarding for everyday discovery. Our inference is to teach supported
uses and material limits, not assume an explanation of the memory or agent
architecture will calibrate reliance. [Study record](https://www.microsoft.com/en-us/research/publication/from-use-to-oversight-how-mental-models-influence-user-behavior-and-output-in-ai-writing-assistants/).

There is a useful product precedent in Google's source-based notebook: its
documentation puts source questions and several generated media around the same
notebook. Different outputs need not imply unrelated products. This is a
documented interaction structure, not a hands-on usability result. Vesper should
borrow the continuity of subject, not the need to build a notebook or inspect a
large format menu before receiving help. [Google's notebook guide](https://support.google.com/gemininotebook/answer/16206563?hl=en).

**Recommended design hypothesis: complete payoff, then an earned bridge.** An
earned bridge exposes a relevant supported continuation of the exact thing in
front of the person. It is not an extra card asking them to feed the system.

| Encounter from the existing portfolio | Value before any next action | A possible earned bridge; what it teaches |
| --- | --- | --- |
| A question about the exhibition | The source-backed painting-and-mirror explanation in §13.2, not just an exhibition summary | Exact exhibition information when visiting becomes relevant: understanding can connect to a real place without starting a trip |
| Six people, one pot, recipe D | The adjusted quantities and workable method in §13.3 | An optional explicit keep/refind path: practical help can remain accessible without the person filing a transcript |
| Home without a question | The concrete possibility and substantive world explanation in the NYC specimen | Open the exact session or spatial subject; ask privately about it without re-pasting: Home gives value and Chat can work with what was received |
| Maya's recipe and original note | The friend's authored offering and usable recipe in §13.4 | Private help on that recipe, or a supported human reply: receiving does not require logging, matching effort or becoming an organizer |

These are alternatives available when useful, not a requirement to put a button
after every answer. Some encounters should simply end. A person who reads the
explanation, enjoys the photo or makes dinner has already received value.
Comprehension should not depend on touring Home, Chat, Places and Life.

Compare three whole-encounter treatments with the **same content, availability
and visual fidelity**:

1. **Orientation-led:** a concise, dismissible account of the supported range
   accompanies the encounter. It may explain more accurately; it also adds
   reading before the product has earned attention.
2. **Payoff-only:** the complete result, with ordinary source/object access and
   no capability teaching. It may be the clearest experience; it may also look
   like a one-off answer or a narrow content app.
3. **Payoff plus an earned bridge:** the same result, with a contextually useful
   continuation where warranted and brief optional orientation elsewhere. It
   may teach breadth through use; it can fail if every result feels like an
   upsell into another task.

At this research stage, Treatment 3 was the leading hypothesis, **not an
empirical winner**. The subsequent [§15 comparison](#151-result-a-useful-continuation-is-not-always-a-visible-next-step)
revises that broad preference into mixed encounter defaults; do not apply it as
a universal bridge requirement. The deciding
question is whether someone independently recognizes another appropriate use
and avoids unsupported expectations. Remembering a tab name or repeating our
four moves is not the goal. Measure spontaneous transfer before explaining the
other portfolio examples; otherwise we measure what the session taught them.

Do not solve poor transfer by automatically producing more follow-ups. First
distinguish an unclear promise, a weak payoff, an invisible useful continuation
and a capability that simply is not relevant to this person.

### 14.3 Judgment: opinionated enough to help, open enough to explore

The evidence already considered in matrix §15 withstands this pass. Chernev,
Böckenholt and Goodman's 2015 meta-analysis covers 99 observations and 7,202
participants; choice complexity, task difficulty, preference uncertainty and
the decision goal moderate overload. It does not justify a fixed top-three
rule. Our inference is to reduce comparison burden for a constrained decision
while preserving meaningful breadth for exploration. [Publisher abstract](https://myscp.onlinelibrary.wiley.com/doi/10.1016/j.jcps.2014.08.002),
[author-hosted paper](https://chernev.com/wp-content/uploads/2017/02/ChoiceOverload_JCP_2015.pdf).

Binst, Michiels and Smets' accessible UMAP 2025 interview paper describes
fortuitous, refreshing and enriching recommendation encounters. Its 17
interviewees in Belgium described broadening, deepening and reviving interests,
as well as restrictive topic fixation. These qualitative accounts support
multiple forms of discovery, not a ranking formula or evidence that novelty
causes retention. For Vesper, an unfamiliar mechanism or a useful rediscovery
can matter more than categorical distance from prior interests. [Author paper](https://arxiv.org/html/2505.15440v1).

**The additional warning is that convincing explanations can conceal poor
selection.** Rahman, Siemon and Ruotsalo's 2026 IJHCS article reports a study of
231 people over three tasks in which persuasive explanations influenced choices,
including selection of lower-utility options. This pass accessed the indexed
publisher abstract; direct full-text access was blocked. Task-defined utility
is not a measure of someone's whole life. The result nevertheless argues
against treating recommendation acceptance as proof of better judgment.
[Publisher record](https://www.sciencedirect.com/science/article/pii/S1071581925002757).

My recommendation is **a supported point of view with visible material
tradeoffs**, not a popularity list and not a confident personality reading.
The result should communicate what is rewarding about the option and what
could make it wrong here. Avoid flattery, fabricated urgency or social proof
substituting for those reasons. A popular option can legitimately win.

Apply this to complete compositions, not just individual cards:

- **Open afternoon:** when the person has actually supplied that purpose, lead
  with a compelling shape of experience and let different possibilities remain
  browseable. The Governors Island case in the judgment specimen is useful
  because the way of experiencing the place can be the contribution; a novel
  destination is not required. The island, a local park and a ticketed evening
  are not equivalent options just because all are “things to do.”
- **A catch-up with a departure deadline:** promote the option whose practical
  terms support conversation and the stated window. A materially different
  alternative is useful if it changes the real tradeoff. Do not require the
  person to compare six superficially similar venue descriptions.
- **Home with no declared decision:** deliver a generous field of worthwhile
  material. Do not manufacture a free afternoon, a task to choose something,
  or a scarce-time crown from the absence of recorded plans. A friend offering,
  a complete explanation and a practical possibility can coexist without all
  demanding decisions.

The named candidates remain dated research fixtures from the linked specimens,
not fresh availability claims here. Exact operational facts must be rechecked
when a real recommendation depends on them.

Extend the existing comparison in three separable ways:

1. Hold world evidence and wording style constant; compare category/popularity,
   eligible-history and current-purpose selection. Examine discriminating
   reasons and rejected alternatives, not just how appealing the winner sounds.
2. Hold the selected option and facts constant; compare compact factual reasons
   with more persuasive prose. If selection rises without better understanding
   of tradeoffs, do not record that as improved recommendation quality.
3. Review the whole receiving surface, including repeated visits. Several good
   cards can still create a repetitive page or an exhausting set of decisions.

Judgment is not successful because it changes the recommendation every time
history is added. Sometimes the same option remains best, with a better way to
experience it or less checking left to do. Sometimes irrelevant history should
change nothing. Newness, confidence, clicks and explanation length are not
substitutes for that distinction.

### 14.4 Dependable ordinary value: bound the claim, not the whole product to one topic

**Sparse context and sparse world supply are different problems.** A recipe
question may be fully answerable from the supplied recipe. A local opening
needs worthwhile current supply even if no personal history is needed. A
friend's offering needs authorized access and legible original material, not
an AI interpretation. A retained object needs dependable retrieval, not a
freshly generated insight. No one mechanism supplies all four.

Nadalic Sotic and Kamps' SIGIR 2026 perspectives paper uses mixed-method
qualitative work with nine people querying document collections. It reports
expectations of exhaustive analysis and persistent memory, limited source
inspection, and interpretations of “not found” as nonexistence. This pass read
the indexed primary abstract; full-text access was blocked. The small,
document-search setting does not establish prevalence in Vesper. Our inference:
coverage gaps must not become negative claims about the world.
[Publication record](https://doi.org/10.1145/3805712.3808537).

Flighty's documentation offers a concrete adjacent pattern: predicted times
remain distinct from official times, and its help page names supported and
unsupported delay causes and regional differences. We have not independently
verified its accuracy claims. The useful lesson is that practical depth can
coexist with specific boundaries; it is not a reason for Vesper to rebuild
Flighty's tracking infrastructure. [Flighty coverage and predictions](https://flighty.com/help/delay-predictions).

For the shared portfolio, specify the service this way:

| Encounter | Minimum sufficient basis | Complete value that can be offered | Missing-basis behavior that still helps |
| --- | --- | --- | --- |
| Exhibition curiosity | Inspectable public curatorial/source material | A substantive explanation with exact source access | If current admission is unknown, keep the supported explanation; do not imply an available visit. If the source itself is inaccessible, do not pretend to have read it |
| Recipe D for six | The actual recipe, requested serving count and equipment constraint | Correct quantities and a feasible method; arithmetic need not be generative | Preserve a supported method while stating a material equipment uncertainty; do not invent pantry contents or turn the question into a cooking profile |
| Independent Home | A bounded supply of worthwhile world material, with current evidence for claims that need it | Complete explanations and concrete possibilities without history or friends | Remove an expired occurrence claim; retain independently useful material or substitute a genuinely supported option. “Not verified” is not “sold out,” and thin coverage is not “nothing to do” |
| Maya's offering | Original content available to this recipient for this use | The note/photo/recipe as authored, with an exact continuation when supported | If optional AI adaptation fails, retain the original offering. If access is withdrawn, explain unavailability without reconstructing private content from a derivative |
| Finding something explicitly kept | Exact admitted object, current access and a working retrieval path | Open the kept thing without transcript archaeology | Identify the specific unavailable source or broken handoff; do not replace it with a plausible generated substitute |

This is a **proposed service envelope**, not certification that every path works
today. It also does not make a disclaimer-only response successful. If the
remaining supported content is not worth receiving, record an unmet service
need rather than decorate the limitation.

The practical engine belongs inside these experiences: adjusting quantities,
noticing that a departure deadline changes the choice, or distinguishing a
place's character from today's access. Its visibility should come from useful
judgment and relief, not from a separate “live engine” product. Answering now,
finite preparation and continuing monitoring remain different services; an
answer does not silently accept responsibility to keep watching.

**Cost the complete useful encounter.** Compare permitted reusable public
material, claim-specific refresh, private adaptation, exact retrieval and
original human contributions before assuming each Home item needs a fresh
article. Record acquisition, model/tool calls, retries, reuse rights, refresh,
latency and human repair alongside what the person actually receives. Low model
cost is not success if assembly work has merely moved back to the person.

This aligns with the active world-supply roadmap rather than introducing a
universal context store, a comprehensive place index or generation on every
root read. Do not leak private context into public preparation or provider
queries. A richer feed should come from supported breadth, reuse and worthwhile
selection—not obligatory production to fill an arbitrary card count.

### 14.5 Voluntary preference: attach to recurring situations, not a daily obligation

My leading hypothesis is that Vesper earns a place in someone's repertoire:
**“When this kind of thing comes up, Vesper is a good place to turn.”** That can
be a casual question, an available window, a friend's offering, a practical
change or a need to retrieve something. These are different entry cues, not
five habits we should demand each person acquire.

Enjoying an explanation or casually browsing worthwhile possibilities can itself
be the benefit; a subsequent plan or practical action is not required. Hsiao,
Lin and Chuang's June 2026 accepted article reports an online survey of 330
Taiwanese students using conversational AI. Enjoyment was associated with use
intentions, but not payment intentions; other relationships differed across the
two tools. The publisher's abstract and disclosures were accessible, not the
full analysis. Crucially, data collection was in 2023–2024, and these are
intentions in a student sample, not observed 2026 retention or purchasing.
Our inference is to count enjoyable receiving as genuine potential value while
keeping use, preference and payment distinct. [Primary article](https://www.nature.com/articles/s41599-026-08154-3).

Lally and colleagues' real-world habit study followed 96 people choosing daily
health-related behaviors in a consistent context over 12 weeks; sufficient
data and successful model fits covered smaller subsets. It found substantial
variation in automaticity trajectories, and a missed opportunity did not
materially disrupt the modeled process. This is not an app-retention trial or
a basis for a “66-day Vesper habit.” Our inference is to investigate recurrence
of useful situations, not prescribe streaks or treat occasional absence as
relationship failure. [Primary publication](https://doi.org/10.1002/ejsp.674).

Verplanken and Roy's 2016 field experiment included 800 participants and found
a sustainability intervention more effective among recently relocated
households; behaviors were self-reported over eight weeks. This institutional
abstract supports investigating context changes as possible entry moments.
It does not establish that returning from vacation resembles moving home,
or validate a post-trip acquisition strategy. Compare people settling into a
new place with people in established routines rather than generalizing from
the founder's Europe trip. [University of Bath study record](https://researchportal.bath.ac.uk/en/publications/empowering-interventions-to-promote-sustainable-lifestyles-testin/).

Readwise's documentation separates reviewing retained highlights from email
delivery: people can disable review emails and still use the review in the app.
It also exposes frequency tuning, including cases where source volume affects
resurfacing. The precedent is useful retrieval without mandatory push, not
proof of retention. Vesper should avoid importing a review regimen or making
people manually tune their lives to prevent repetitive output.
[Readwise review documentation](https://docs.readwise.io/readwise/docs/faqs/reviewing-highlights).

Keep the following evidence distinct:

| Observation | What it can support | What it does not establish |
| --- | --- | --- |
| “That helped” after one encounter | Immediate perceived benefit, with the person's explanation | Recall when another need arises, switching or payment |
| An unprompted plausible next-use example | Some transfer of the product's range | Actual independent return or belief in unsupported services |
| Choosing Vesper when a relevant situation recurs and alternatives are available | Voluntary preference in that situation | A universal daily habit, a durable preference profile or broad market demand |
| A friend enjoys receiving an offering | Recipient value, including asymmetric participation | Acquisition, permission to contact them or obligation to contribute |
| Someone independently brings their own question after receiving | A possible transition from receiving to personal use | Subscription demand or retention beyond that observed behavior |
| Actual willingness to buy a clearly bounded offer, later renewal if observed | Evidence about that offer under those conditions | A price justified by compliments, theoretical time savings or engagement alone |

No such Vesper study was run in this research round. A future consented study
can examine relevant opportunities and chosen tools, with access to familiar
alternatives. Do not infer those opportunities from hidden tracking or label
all non-return as rejection. A person may have no need, may forget, may expect
Vesper cannot help, may encounter friction, or may prefer another product.
Those explanations require different product changes.

An equal-information comparison tests contribution quality; an end-to-end
comparison tests whether context transfer and receiving actually save effort.
A capable assistant may match the answer. Familiar messaging may already make
sharing effortless. The comparison should let those alternatives work well.
Vesper's proposed advantage must survive without an artificially weak baseline
or founder assembly hidden behind the interface.

### 14.6 One portfolio, four investigations—not four new product lanes

Use the four entrances in §14.2 throughout, retaining the exact evidence and
fictional-person labels from their existing source packets. Do not manufacture
a single person's week in which all four needs conveniently occur. They are
comparable encounters through one system, not a mandatory funnel.

Review each encounter under these changes where applicable:

- Remove personal history. Does useful value remain, and is it still honestly
  described? Removing irrelevant context can correctly leave the answer intact.
- Add one relevant, permitted fact. Does it improve substance, feasibility,
  confidence in a justified choice, or work avoided—not merely personalized copy?
- Change a decisive condition or remove one supply dependency. Does the system
  adapt the actual contribution without turning a limitation into homework?
- Remove friends from the base experience. Does the individual product remain
  useful? Then add one original offering and assess the recipient's gain without
  requiring equivalent effort or a new social identity.
- Return after a gap where a subsequent encounter is appropriate. Is the exact
  kept object or current opportunity accessible without a catch-up queue? Any
  later use of conversation must respect the effective agreement; the pending
  continuity proposal is not runtime authority.

For reviews, use the existing [received-value and human-work ledger](situated-value-decision-matrix-2026-09-06.md#119-whole-experience-review-received-value-context-and-human-work).
Add explicit observations for **next-use understanding**, **material choice
tradeoffs**, **useful fallback**, and **independent preference**; these need not
be new production events or permanent user records. Do not collapse factual
correctness, appeal, effort, comprehension and later outcomes into one score.

### 14.7 Decisions, disconfirmation and next handoff

The recommended next step is to make and review **competing complete encounters
from this portfolio**, not expand the canon again before seeing their effects.
This is a way to choose defaults for the complete system, not a “prove one loop
before designing the architecture” restriction.

| Decision | Leading recommendation | Evidence that would change it |
| --- | --- | --- |
| How to reveal breadth | Complete payoff with a relevant earned bridge; optional concise orientation | Newcomers remain narrowly calibrated, or perceive constant follow-up pressure; clearer orientation or payoff-only treatment performs better |
| How to recommend | A supported point of view with material tradeoffs; wider browsing when wanted | People consistently prefer selection work themselves, or the recommendation does not improve on capable equal-evidence alternatives |
| What service to promise | A complete bounded offer across understanding, world possibilities, practical help, original social receiving and explicit refinding | Ordinary supply/latency/repair costs make one promise unreliable; narrow that claim or its supported conditions rather than silently lower the payoff |
| What earns return | Useful recurrence and easy exact continuation, without mandatory daily cadence | People value individual answers but neither recall nor choose Vesper again under relevant conditions; reconsider the entrance, distinctive benefit or service, not just notification volume |

Concrete handoff order:

1. **Product/design:** use the current four source packets to compare the three
   breadth treatments. Keep the core results equally good; include an independent
   no-input Home composition and an original social offering. Leave detailed
   visual composition to the dedicated design lane.
2. **Recommendation/supply:** reuse the existing NYC candidates to separate
   discovery, selection and explanatory copy; attach the service-envelope
   conditions to the same encounters. Do not start another supply architecture.
3. **Integration:** identify a pinned build and label each receiving, continuation,
   correction and refinding path working, gated, prototype-only or unsupported.
   Record real latency, supply and remaining human work. This document does not
   replace that engineering check or claim its completion.
4. **Research, when authorized:** examine comprehension and immediate benefit
   first; examine later independent choice only with a functioning service and
   an appropriate consented arrangement. Avoid forcing everyone through the
   portfolio, and do not turn study questions into routine product homework.

The resulting decision should say what the person reliably receives, how they
discover another useful application, and what we still cannot promise. Until
then, the launch audience, canonical wording, membership offer and unresolved
continuity policy remain at their existing status. This pass changes research
and handoff recommendations only; it initiates no outreach, purchase, monitoring,
app implementation or external task.

## 15. Complete encounter comparison and recommended defaults — September 7

### 15.1 Result: a useful continuation is not always a visible next step

**The best starting point is not treatment C everywhere.** Writing out the
encounters exposes a weakness in that interpretation of §14: even a relevant
continuation can make an already complete answer feel unfinished, or make a
friend's gesture feel like an advertisement for AI.

My recommendation after this authored comparison:

- **Curiosity about an exhibition:** complete explanation, exact work access,
  and a subdued path to the exhibition. Make another direction available without
  suggesting the person ought to visit.
- **A direct practical question:** the usable answer, then stop. Keeping or
  adapting remains available, but do not promote a new task merely to demonstrate
  range.
- **Independent Home:** a varied, finite receiving experience with exact object
  continuations and an easy way into broader exploration. Do not append a
  capability lesson or make every contribution a question.
- **A friend's offering:** the original person and material lead. Private help
  is accessible, but becomes prominent when the recipient asks for it.

These defaults follow the **current encounter**, not a permanent user type or
one grammar per root. A practical answer can appear inside a Home object; an
exploratory question can happen in Chat; a shared recipe can become practical
help without changing ownership of the friend's words.

This section contains twelve comparable written treatments: three treatments
for each of four encounters. Each encounter has one complete common payload
and an exact composition recipe for A/B/C, avoiding twelve slightly different
answers that would confound the comparison. It is not rendered UI, a working
app demo, a participant study, a complete Home content inventory or a new launch
restriction. Quoted blocks and labeled controls are proposed user-facing content;
the surrounding explanations are reviewer notes, not phone copy.

### 15.2 Comparison controls and common behavior

Use the same evidence, answer, source access, available actions and destination
contents within each encounter. Change only the orientation and prominence of
the continuation. **B must not be a deliberately crippled product.** Its ordinary
object controls still work; C promotes an existing relevant path rather than
secretly receiving better research, retention or practical assistance.

| Treatment | Exact construction | Fair comparison boundary |
| --- | --- | --- |
| **A — orientation-led** | A dismissible first-encounter strip, then the common payload and ordinary controls. Strip copy: “Ask, explore, get practical help, share with friends, or keep something.” | No setup fields, modal tutorial or delayed answer. This is the strongest concise orientation alternative, not a straw-man onboarding ordeal |
| **B — payoff-only** | The common payload with ordinary source, object and conversation controls; no added capability copy or promoted follow-up | Do not hide provenance, human Reply, essential method steps or exact subject context to make C win |
| **C — payoff plus an earned bridge** | The same payload, with the one case-specific continuation below promoted; no generic orientation strip | No newly generated benefit withheld from A/B, automatic save, suggested-task queue or requirement to continue |

The orientation strip is comparison copy, not a canonical product promise.
Apply it once at the tested first encounter, not on every subsequent screen.
For C, moving an action into prominence is itself the intervention; record that
difference rather than pretending the interfaces are identical.

All variants preserve an easy Back/close, normal access to the four roots and
the originating subject when a person actually continues. Nobody must pass
through all four roots. A permission, failure or material uncertainty remains
equally legible across treatments. Do not make an unsupported route appear live
in one variant or silently use the pending conversational-continuity proposal.

### 15.3 Curiosity: a work becomes worth looking at

**Starting evidence:** E from §13. A newcomer asks about the supplied MoMA
exhibition link, “Anything interesting here?” The date is September 7, 2026.
No personal history, interest profile or intended visit is assumed.

**Common first response, complete before tapping:**

> **A self-portrait with room for a friend.**
>
> Kahlo gave *Fulang-Chang and I* to her friend Mary Sklar with a mirror beside
> it, so Sklar could see herself next to Kahlo. The gift lets its recipient
> appear in the work, rather than only look at it.

Ordinary source access: **MoMA's account**. Ordinary work access: **See the
painting and mirror**, opening the [exact collection record](https://www.moma.org/collection/works/79374), not image search.
The originally supplied exhibition link opens its own details in every variant;
C additionally exposes that route beside the answer.
The final sentence is our interpretive framing, not a quotation or a claim
about this user's friendships. The gift account was rechecked against
[MoMA's curatorial essay](https://www.moma.org/explore/inside_out/2009/12/03/a-close-look-frida-kahlo-s-fulang-chang-and-i/).
No artwork reproduction is licensed or supplied by this document.

| Version | Full first encounter after the common payload is inserted | Likely strength / weakness, as design judgment |
| --- | --- | --- |
| **A** | Orientation strip → response → work/source access → normal Chat composer | Names the range clearly, but the abstract capabilities compete with the very small interesting detail |
| **B** | Response → work/source access → normal Chat composer | A clean, satisfying answer. Broader practical capability may remain invisible, but that is not necessarily a failure of this encounter |
| **C** | Response → work/source access → subdued **Exhibition details** continuation → normal Chat composer | Gives a concrete route from understanding to a real place without a “Plan your visit?” question; risks nudging a reading-only encounter toward going somewhere |

**The shared destination when Exhibition details is chosen:**

> **Frida and Diego: The Last Dream**
>
> MoMA · March 21–September 12, 2026
>
> Saturday, September 12 is the final listed exhibition day.
>
> Admission availability has not been checked.

Destination actions: **MoMA visitor information** and a normal contextual Ask
whose subject is this exhibition. The dates were rechecked against the
[exhibition announcement](https://press.moma.org/exhibition/frida-and-diego-the-last-dream/).
This is published visit context, not an assessed outing, ticket inventory or
promise to monitor the closing date. C does not automatically open this depth;
A/B can reach the same information through ordinary object access or a question.

**Recommendation:** C, lightly expressed, for this exhibition-level question.
B remains appropriate when the question is only about interpreting the painting.
Do not turn that distinction into a durable “reader versus doer” preference.
The source/work route already does much of the work: adding another explanatory
sentence about Vesper's capabilities would probably weaken this small result.

**Completed ending:** the person understands the gesture and leaves. Nothing is
kept or promoted to Home by the Ask alone. If the answer was already familiar,
another supported angle can be offered in response to that correction; repeating
the same story more fluently does not earn value.

### 15.4 Practical help: make the answer usable without opening another task

**Starting evidence:** synthetic recipe D from §13, serving four with 400 g dry
pasta, 600 g tomatoes and 120 g cheese; uncooked sauce mixed in a bowl. The person
asks, “Could I make this for six tonight? I've only got one big pot.” This is a
method-and-quantity fixture, not a verified dietary or cooking recommendation.

**Common first response:**

> **One pot works—the sauce stays off the stove.**
>
> For six recipe-sized portions:
> **600 g pasta · 900 g tomatoes · 180 g cheese**
>
> Mix the tomatoes and cheese in a large bowl. Cook the pasta in your pot,
> then toss together. You'll still need that mixing bowl.
>
> If 600 g crowds your pot, cook in two batches. Scale the quantities, not the
> cooking time.

All necessary stipulated method steps are visible here. **Do not hide them
behind “Method for six” and then count opening it as engagement.** The original
recipe and ordinary exact-result Keep remain accessible. There is no shopping
list, timer, guest setup or dinner plan in the common result.

| Version | Full first encounter | Likely strength / weakness, as design judgment |
| --- | --- | --- |
| **A** | Orientation strip → complete response → ordinary source/result controls and Chat composer | May teach range, but it precedes a practical answer with unrelated capability reading |
| **B** | Complete response → ordinary source/result controls and Chat composer | Resolves the asked job. There is no implied second step; this is my preferred default |
| **C** | Complete response → promoted **Keep this version** → ordinary controls and composer | Exact preservation can be useful, but promoting it implies filing is part of finishing dinner help |

**A later action, available in every variant:** if the person deliberately says
“Keep this version,” retain the exact six-person method through the appropriate
supported owner. After authoritative success, proposed receipt:

> Kept privately: **Pasta for six**. **Open in Life** · **Undo**

That link opens the retained method, not a generic Life root or a transcript
requiring the person to reconstruct the quantities. Do not save only the
four-person original while claiming to have kept the adjusted version. Source
and derivation identity remain inspectable; Maya's original recipe, if it was
the entrance, has not been rewritten.

On failure, no success receipt: **“Couldn't keep this version. The method is
still here in this conversation.”** That describes the current encounter, not
a promise of indefinite chat retention. The same failure applies to A/B/C.

**Recommendation:** B. Contextual continuation should work exceptionally well
when invoked, without being promoted after every adequate answer. If a person
asks to preserve, compare or adapt something, that becomes the current job;
do not keep the interface artificially quiet when it would obscure that job.

**Completed ending:** read the quantities, cook or choose something else,
leave. No “Did you make it?” request, inferred attendance, pantry profile or
automatic later Home callback. Later refinding is promised only for what was
actually retained under its agreement.

### 15.5 Independent Home: value in the scroll, not a menu of possible AI jobs

**Starting evidence:** the exact thin-history NYC world in the
[newcomer specimen](nyc-newcomer-connected-home-specimen-2026-09-07.md#2-exact-starting-conditions):
selected NYC, explicitly kept SNFL, no eligible old Ask content, no active
friends, no known origin, free time or intended outing. Hold those facts and
the September 7 date constant. The four units below are a finite comparison
page, not a production ceiling or a claim that this is Home's final inventory.

**Common full-scroll content, in reading order:**

**H1 — a concrete possibility**

> **Twenty minutes on the water.**
>
> Pier 2, Brooklyn Bridge Park · Sat, September 12 · Free
>
> A short paddle in the protected embayment. Equipment and instruction provided.
>
> Weather-dependent. Reservation availability not checked.

Ordinary exact object access: **See the session**. This is a 20-minute paddle,
not an asserted total outing duration. The dated park listing specifies
10 a.m.–3 p.m.; the operator specifies Saturdays only in September. Both were
rechecked for this manuscript. No reservation inventory was inspected.
[Dated park listing](https://brooklynbridgepark.org/event/kayaking-saturdays-september-12/),
[operator's seasonal notice](https://www.bbpboathouse.org/).

**H2 — a useful comparison, not another essay**

> **One market, different days.**
>
> Union Square Greenmarket
>
> Monday: Mushroom Queens · cultivated mushrooms
> Wednesday: Bear Creek Farm · dahlias
>
> Examples from GrowNYC's published rosters. Attendance can change.

Ordinary object access: the exact market/day comparison. These examples do not
claim exclusive days, available stock or that either vendor is absent on other
days. The comparison itself is visible; opening should deepen it, not force the
person to assemble it from long lists. [GrowNYC rosters](https://grownyc.org/locations/union-square-greenmarket/).

**H3 — complete understanding, no outing required**

> **Those Hudson cliffs cooled underground.**
>
> Magma pushed between older rock layers and hardened into diabase. Erosion
> later exposed its edge as the Palisades. You're looking at what used to be
> inside the landscape.

Ordinary source/spatial subject access: **The Palisades**. This addresses a
regional landform, not the person's present location or inferred geology taste.
The final sentence is explanatory framing of the supported process, not a
claim that the person is standing there. [Park geology](https://njpalisades.org/nature/).

**H4 — compact access to something entrusted**

> **Kept: Stavros Niarchos Foundation Library**
>
> Fifth Avenue at 40th Street · Public rooftop terrace
> NYPL's holiday closure: September 5–7.

Ordinary object access: the exact kept library. The rooftop need not be news to
someone who saved it. This unit supplies refinding and context, not a declaration
that their visit is affected. NYPL's indexed official material supports the
terrace and holiday schedule; that is not a live check of today's entrance or
terrace condition. [NYPL library description](https://www.nypl.org/about/locations/schwarzman),
[holiday schedule](https://www.nypl.org/help/closings/).

The common page has no onboarding questionnaire, empty people section,
capability cards between these units, review queue, or “choose something for
this week” request. Its values have unequal expression: an activity, a compact
day comparison, a causal explanation and a kept-object door. These are content
roles, not instructions to introduce four new renderer families.

| Version | Complete composition | Likely strength / weakness, as design judgment |
| --- | --- | --- |
| **A** | Orientation strip → H1 → H2 → H3 → H4 → ordinary root navigation | Explains the range beyond a city guide, but begins the receiving surface with a product description |
| **B** | H1 → H2 → H3 → H4 → ordinary root navigation | Clean and useful without new input. Exact object taps already reveal considerable depth; the broader exploration path relies on recognizing Places |
| **C** | H1 → H2 → H3 → H4 → **Explore NYC** → ordinary root navigation | The additional path broadens exploration without asking for a prompt or more personal data. It risks duplicating an already clear Places tab; this is a deliberately small difference |

**C's exact continuation:** Explore NYC opens Places in the selected NYC scope,
with map/field exploration and current supported material—not the four Home
units copied onto another page, a blank map, or an inferred live-location search.
Existing place exploration should supply this; the comparison does not invent
new facts or promise an unbuilt feed. B can reach the same scope through the
ordinary Places control. No content is withheld from B to manufacture C's value.

**An object can also become practical without that detour.** Opening H1 in any
variant gives the date, 10 a.m.–3 p.m. published window, the approximately
20-minute paddle, north Pier 2 entrance/floating dock, equipment, waiver and
registration terms. **Operator registration** is an external handoff, not Vesper
checkout. A contextual question is grounded in this session. The person need
not go through Places before asking from the Home object.

If they ask, “Could I do this before lunch?”, a supported thin-evidence response
is: **“The paddle is about 20 minutes; the journey and any wait are additional.
Where would you start, and what time and place is lunch?”** These missing anchors
matter to the volunteered question. They are not required to read Home. The
continuation has not finished assessing feasibility until the necessary route
and slot evidence are resolved; do not call the published activity a prepared
before-lunch plan.

**Recommendation:** C as a modest candidate, not a new feature or a universal
footer requirement. The stronger commitment is to the complete content and
exact object routes shared by B and C. If the ordinary Places navigation already
makes exploration obvious, choose B and remove the redundant door. Neither a
footer nor this useful NYC supply alone establishes differentiated personal value.

**Completed ending:** receive something interesting or useful and leave. After
September 12, the dated paddle offer loses current prominence; do not roll its
date forward. Expired holiday wording recedes independently of the library save.
These are conditional transformations, not a fabricated September 14 feed.

### 15.6 Social: the friend is not a preamble to Vesper

**Starting evidence:** the fictional Maya and recipe D from §13.4. This is an
authenticated, authorized addressed offering, not public posting or a new guest
access policy. Its people and meal are independent fixtures; do not merge them
into the adjacent social project's shared history or invent matching attendance.

**Common receiving content:**

> **Maya**
>
> Made this with the last tomatoes from the market. The sauce never touches
> the stove. Thought you'd like it.

Maya's own dinner photograph accompanies her words. The photograph is a labeled
fixture placeholder here, not a generated or inspected asset. An attached recipe
preview supplies this compact, separately sourced material:

> **Tomato pasta · Recipe for four**
>
> 400 g pasta · 600 g tomatoes · 120 g cheese
> Mix the tomatoes and cheese in a bowl; cook the pasta, then toss together.

The preview is the attached recipe's method, not a claim inferred from pixels
or AI speech attributed to Maya. In this comparison, original and recipe preview
are held constant. The separate original-only versus enrichment decision remains
with the social design brief's section E,
`vesper-social-experience-design-brief-2026-09-07.md` (**local WIP**).

| Version | Complete receiving composition | Likely strength / weakness, as design judgment |
| --- | --- | --- |
| **A** | Orientation strip → Maya/photo/note → recipe preview → **Reply to Maya** and ordinary object controls | The product's range is explicit, but it takes the first word in someone else's gesture |
| **B** | Maya/photo/note → recipe preview → **Reply to Maya**; **Ask Vesper privately** available as a secondary object action | The human gesture remains the point. Private usefulness is accessible without competing for a response |
| **C** | Maya/photo/note → recipe preview → **Reply to Maya** plus promoted **Ask Vesper privately** | Makes adaptation easier to discover; risks two competing invitations beneath a gesture that asks for nothing |

There is no automatic reply, reaction tally, read receipt, “your turn” label or
system question. The human Reply composer and private Ask composer remain
visibly distinct in every variant. Prominence may vary; audience legibility may
not. Recipe previews are visible only where their custody/use permits it.

**Private continuation, available in all variants:** the recipient selects
Ask Vesper privately and types, “Could I make this for six? One big pot.” The
exact attached D is already present as context. Deliver the complete answer
from §15.4; do not ask the recipient to upload the recipe again. Maya receives
neither this question nor the answer. There is no new recipe-manager onboarding.

**Human continuation, also optional:** if the recipient chooses Reply to Maya
and sends “Want to make this together Friday?”, send that exact addressed
question through the supported path. This is not an accepted gathering or a
claim that either person is free. A subsequent actual shared intention can
use the existing arrangement/Occasion experience; casual sharing need not
create one in advance. The comparison sends no real message.

**Recommendation:** B. Promote assistance after the recipient expresses a
practical question, rather than putting Vesper in competition with Maya at first
receipt. This is not a rule to hide useful AI enrichment: if it supplies a
substantive missing benefit, assess that separately against the original-only
baseline, as the social lane already requires.

**Completed ending:** enjoy Maya's glimpse and close it. Receiving without reply
or adoption is valid. If optional AI is unavailable, the authorized original and
recipe still provide value. If access is withdrawn, do not preserve the offering
by reconstructing it from an unauthorized derivative.

### 15.7 Cross-encounter review and the decisions this actually makes

This is my comparative inspection of authored specimens. “Preferred” below does
not mean consumers preferred it, a variant won an experiment, or runtime paths
were certified. No numerical quality or retention scores are invented.

Because the answer and candidate selection are held constant, A/B/C cannot
establish better recommendation judgment or better content. They isolate how
the same value and range are presented. The separate candidate-selection and
discovery comparisons in §14.3 remain necessary to evaluate those contributions.

| Encounter | Recommended first presentation | What should be exceptionally good when invoked | What would change the recommendation |
| --- | --- | --- | --- |
| Exhibition curiosity | **C**, with a subdued exact exhibition path; B for a narrowly interpretive question | Artwork/source depth, accurate exhibition context and a grounded practical question | Readers experience an outing nudge, or normal object access already makes the continuation clear |
| Direct practical help | **B**, complete answer and ordinary controls | Correct adaptation; retaining and reopening the exact requested version | People explicitly want preservation but cannot discover it, or a genuinely complex requested job needs clearer next steps |
| Independent Home | **C**, lightly; B if the exploration door duplicates clear navigation | Useful full scroll, exact object depth, practical help and wider spatial exploration | Added navigation does not improve comprehension or discovery; the content itself remains too weak or repetitive |
| Original social offering | **B**, human-first and privately helpable | Reply/Ask distinction, no re-pasting, optional shared preparation | A concrete substantive addition is wanted at receipt and improves it without displacing the friend |

**The more precise default is therefore: finish the current contribution; make
its useful depth accessible; promote another job only when that promotion earns
its attention.** Neither maximum silence nor maximum continuation is the target.
This qualifies §14's leading C hypothesis rather than replacing the four moves.

The common architecture-bearing requirement is continuity of the actual subject
and result—not a larger number of buttons. Reading → exact work; paddle → exact
session; private Ask → the received recipe; Keep → the chosen method version;
Back → still-valid originating context. Same-subject continuation alone does
not authorize cross-session history reuse, a new audience or an external action.

### 15.8 Stress review, remaining limits and handoff

| Change applied equally across treatments | Required visible behavior | Why it matters to the comparison |
| --- | --- | --- |
| No personal history and no friends | E and D answers and the base Home retain their useful substance; no empty social placeholder | The system cannot use rich context to conceal weak first value |
| A relevant fact is supplied now | The recipe serving count or practical outing constraint changes the actual answer, not just its greeting | Tests adaptation within the encounter without assuming an unadopted memory grant |
| An answer is already familiar | Accept the correction; another supported angle or a clean ending, not an insistence that the person should find it interesting | Novelty cannot be established by our copy alone |
| A volatile fact is unavailable | Supported explanation/method survives; unverified feasibility is not promoted as solved | A persuasive version cannot win by hiding unfinished checking |
| An exact Keep fails | No successful save claim or later retrieval promise; retain immediate usefulness within actual custody | Authority and the usefulness of the answer are different questions |
| A friend offering is withdrawn | Remove its permission-dependent material; preserve only independently authorized content | A contextual bridge cannot become a back door to private material |
| A person returns after absence | No attendance inference, catch-up debt or stale current offer; exact kept material remains accessible where supported | A return is another useful encounter, not completion of our preferred funnel |

For human-work review, distinguish **work already removed** (scaling, reading
the source, comparing rosters, carrying the recipe), **wanted human choice**
(whether to cook, read, paddle or reply), and **unresolved service work** (a
route/slot assessment not yet performed, a failed retained-object write).
Do not count the third as completed value or call the second friction to erase.

The manuscript still has limits. The cultural explanation and recipe arithmetic
can be matched by a capable assistant; a good city guide can supply much of H1–H3;
messaging already makes a photo enjoyable. Our proposed differentiation remains
dependable selection, substantive connection when earned, exact continuation,
practical judgment and reduced reconstruction across these encounters. This
comparison makes those demands concrete; it does not establish a moat or demand.

**Ready for design review now:** render A/B/C from the shared payloads and action
destinations, at equal fidelity, in the dedicated tool. Do not add richer images,
better facts or hidden concierge work to one treatment. Start with the mixed
recommendations, but keep the alternatives available for direct comparison.
For the Home case, compare the entire scroll and return, not just its first unit.

**Next integration handback:** mark each exact route and result working, gated,
prototype-only or unsupported against a pinned build. Older code-readiness
tables in the source specimens are historical inspections, not current blockers
or proof. Existing integration and world-supply lanes own implementation;
this document dispatches no lane or work item.

**Later newcomer evaluation, if authorized:** show one first-encounter treatment
before explaining other uses; record immediate benefit, unsupported expectations
and spontaneous next-use understanding. Use different participants or explicitly
account for learning/carryover when comparing variants. Showing A and then asking
whether C teaches the range is not an independent test. Actual return, referral
and payment require their own observed evidence; this manuscript supplies none.

Public source checks for this section were made September 7, 2026. Listings,
indexed NYPL material, synthetic recipe/people and unverified availability remain
distinguished. No app, design export, canonical promise, permission agreement,
background watch, social message or purchase was changed by this pass.

## 16. Received value against capable alternatives — September 7

### 16.1 Finding and comparison discipline

**The four experiences are worth supporting, but the manuscripts do not yet
establish a differentiated complete service.** Curiosity and practical answers
can be good without being exclusive. Original social receiving can be complete
without AI. Independent Home carries the largest unresolved editorial burden:
it must select and deliver worthwhile things before the person commissions them.
Continuity can improve all four, but a connected destination is not itself a
better result.

This pass follows §15 without repeating its A/B/C presentation exercise. It asks
what is actually received. The comparisons below are **authored familiar-tool
comparators and authored Vesper targets**, not outputs captured from competing
products or the Vesper production model. Equal information access includes the
same sources, current question and additional context. A tie is allowed. We do
not handicap the comparator by removing its conversation, search, attachments,
saved lists or legitimate connected sources.

The comparison has two distinct lenses:

- **Result quality with matched information:** would Vesper supply a better
  explanation, choice or completed piece of work? These examples often tie.
- **Complete service as actually available:** who must locate, assemble, check,
  retain and reconnect that information? Potential savings here need real
  encounter evidence; they cannot be awarded automatically to Vesper.

One contextual item is supplied explicitly within each encounter. This does not
assume that an earlier private Ask became reusable history. For a later-session
comparison, record the actual permitted source and retrieval path separately.
No new continuity agreement is adopted by these specimens.

#### The competitive baseline has moved

Google's March 12, 2026 Ask Maps announcement describes conversational local
questions, recommendations informed by searched/saved places, friend-meeting
suggestions, saving, sharing and directions. Its initial rollout was US/India
mobile; this page is not a current account-level availability check. We should
not compare Vesper with an intentionally nonconversational, nonpersonal map.
[Google's announcement](https://blog.google/products-and-platforms/products/maps/ask-maps-immersive-navigation/).

Google's January 14 Personal Intelligence announcement also describes reasoning
across connected email/photos and retrieving details for practical help. It
acknowledges mistaken connections and over-personalization. This is a vendor's
capability account, not independent evidence of reliability or a benchmark we
ran. Nevertheless, “other assistants only recollect; we connect” is too broad a
competitive claim. Our claim needs a demonstrably better experience in the
situations we support. [Google's account](https://blog.google/innovation-and-ai/products/gemini-app/personal-intelligence/).

### 16.2 What current lane evidence actually establishes

Inspected recent completed responses in **Content**, **Integration**, **Home**,
**Life** and **Social**, their linked receipts, and relevant backend code. This
was a focused receiving-value pass, not a reread of every task or a new full
architectural audit. Backend inspection was pinned to `9efb3d9d9`; the mobile
checkout history was at `c3feb89f0` on `codex/entity-object-design-completion`.
Home also reports isolated-branch work; do not silently count it as merged.
Content was actively fixing review findings during this pass.

| Evidence | What it supports | What it does not support |
| --- | --- | --- |
| [Integration's connected Source receipt](source-connected-value-execution-receipt-2026-09-07.md) | Exact Source identity/version, prepared-result receiving and bounded cancellation have concrete implementation/test evidence | Its commissioned worker remains dark; this is not a live commissioned example of any of the four finished experiences below |
| [Home implementation map](home-connected-experience-implementation-map-2026-09-04.md) and the Home task's latest report | Owner-backed receiving and exact return/context work are progressing, including isolated-branch tests | Native populated experience, breadth of supply and consumer preference are not established by the reported test counts |
| [Practical root-delivery test](../../travel-agent/tests/api/test_practical_root_delivery.py) | Real root composition is exercised with synthetic owners; volatile open-now information can expire without discarding independent place substance | The fixture's authored bookshop/reading text is not evidence of research or generation quality. This pass read the test; it did not rerun its suite |
| [Home portfolio fixtures](../../travel-agent/tests/root_projection/test_home_portfolio.py) | Concrete reading and addressed friend-note payloads can be tested as retained contributions | Preserving a supplied sentence does not establish that the system can discover or author it well |
| Content task's completed review, followed by active fixes | Source research, bounded retrieval and event/content lifecycle are substantial real work; the review also identified disconnected or defective seams | An active correction effort is not a completed consumer-quality run. Its reported defects are a dated review, not a claim they remain unfixed after this snapshot |
| [Social handoff](claude-design-social-experience-project-handoff-2026-09-07.md), especially its latest ordinary-sharing revision | Human-first sharing, lightweight participation and contextual assistance have concrete design requirements | Design manuscripts are not runtime evidence that a recipient can use this end to end |
| Life task's current organization/reader work | Exact refinding and richer source-backed organization have distinct implementation work underway | A retained source does not by itself establish a reconstructed dinner, journey or social history |

**A diagnostic actually executed here:** imported
`root_rehearsal_cases` and `compile_root_rehearsal` from the existing
[deterministic root rehearsal](../../travel-agent/tools/dogfood/content/root_rehearsal.py)
using the backend virtual environment and serialized each compiled root unit's
payload. All four synthetic situations compiled successfully. No external model,
database seed, authenticated user journey or mobile render was run.

Selected literal payloads from that run:

| Situation / root | Compiled fixture output | Received-value assessment |
| --- | --- | --- |
| Ordinary NYC / Home | “A first weekend back in New York” / “The Saturday horizon is open and the recent journey supplies useful context.” | Describes why a possibility could exist; does not supply one |
| Ordinary NYC / Places | “An open Saturday near home” / “A bounded local field connected to the coming week.” | A valid contextual door, not a substantive local experience |
| Shared Saturday / Places | “Two useful views of Brooklyn” / “Lena's open evening and Mara's contributed place evidence remain attributable.” | Describes preservation of perspectives without showing either perspective |
| Disruption / Home | Recovery instrument with fallback “The source owner can provide the latest state.” | Establishes a typed recovery destination; the serialized fallback alone does not solve the disruption |

These are **structural fixtures**, not alleged bad answers produced for customers.
Other portfolio fixtures already contain more concrete copy. The important gap is
evidentiary: a successful compilation cannot certify the usefulness of the
content supplied to it. Do not repair that gap by merely substituting impressive
prose into a wiring fixture and calling the content engine validated.

### 16.3 Curiosity: something worth understanding, even if the answer ties

**Input E0:** the exhibition link from §15.3 and “Anything interesting here?”
No supplied personal history. The same exhibition/collection/curatorial source
packet is available to both treatments.

**Authored familiar-tool comparator:**

> Kahlo gave *Fulang-Chang and I* to Mary Sklar with an accompanying mirror,
> letting her friend appear beside the self-portrait. The gift made looking at
> the painting a way of joining it.

**Authored Vesper target:**

> **A portrait its recipient could enter.**
>
> Kahlo paired *Fulang-Chang and I* with a mirror when she gave it to Mary Sklar.
> Her friend could appear beside her: the gift made their relationship part of
> the viewing experience.

Both supply essentially the same contribution. The interpretation is our
framing of the documented gift, not a quotation from Kahlo. **Verdict: tie in
substance; keep the useful answer, but do not sell its headline as differentiation.**

**One new context item E1:** “I already know the mirror story.” Both treatments
receive it. A complete replacement, equally available to either, is:

> **A familiar composition, an unexpected companion.**
>
> MoMA curator Veronica Roberts reads the portrait against Renaissance Madonna
> and Child paintings: the companion here is a pet monkey. That comparison
> offers another way to look at the pose—not just the story of the gift.

This changes the interpretive substance instead of praising the person's
knowledge or restating the connection. Roberts offers the comparison; it is not
proof of Kahlo's deliberate intention. [MoMA curatorial essay, December 3,
2009](https://www.moma.org/explore/inside_out/2009/12/03/a-close-look-frida-kahlo-s-fulang-chang-and-i/).

**Work removed:** reading and selecting a supported angle from a longer source.
**Work remaining:** none required to finish understanding this contribution;
looking more closely is the person's optional enjoyment. Arranging a museum
visit is a separate job, not a hidden step needed to complete this answer.

**Sharpen:** explicit corrections should change the next explanation. If the
person later permits retaining a useful explanation, reopening that exact work
and carrying the correction may reduce repetition. That requires a real path;
an unspecified memory promise earns no advantage here. **Remove:** an obligatory
“How does this connect to your life?” or outing prompt. Novelty is not known until
we have relevant evidence about this person's knowledge.

### 16.4 Practical help: complete the small job, do not build a recipe chore

**Input D0:** synthetic recipe D serves four: 400 g pasta, 600 g tomatoes,
120 g cheese. Combine uncooked tomatoes and cheese in a large bowl, cook pasta
in one pot, then toss. Question: “Can I make this for six tonight? One big pot.”
This is a controlled recipe fixture, not dietary advice or a verified culinary
recipe. Both treatments receive the exact method.

**Authored familiar-tool comparator:**

> Yes. For six: 600 g pasta, 900 g tomatoes and 180 g cheese. Mix the tomatoes
> and cheese in a large bowl while the pasta cooks; drain and toss. One cooking
> pot is enough, provided it can comfortably cook that quantity. If not, cook
> the pasta in batches. Follow its usual cooking time, not 1.5 times as long.

**Authored Vesper target:**

> **For six:** 600 g pasta · 900 g tomatoes · 180 g cheese.
>
> Mix the tomatoes and cheese in a large bowl. Cook the pasta in your pot,
> drain, then toss together. If the pasta is crowded, use batches; keep the
> packet's cooking time. You need only one cooking pot, plus the mixing bowl.

**Verdict: tie in practical substance.** Correct arithmetic and a usable method
are real first-encounter value. No biography or personal graph is necessary.
Neither treatment has verified the pot's capacity; conditional guidance is more
useful here than interrupting for a kitchen inventory.

**One new context item D1:** “There will be eight now.” A complete replacement
for either treatment is:

> **For eight:** 800 g pasta · 1.2 kg tomatoes · 240 g cheese.
>
> Mix the tomatoes and cheese in a large bowl. Cook the pasta in batches if it
> crowds your pot, keeping its packet cooking time; drain and toss with the
> mixture. The sauce still needs no second cooking pot.

The change affects quantities and the practical pressure on the pot, not just a
serving-count label. The original friend's four-person recipe remains unchanged.
There is no inferred dinner event, invitation, shopping order or automatic save.

**Work removed:** multiplication and reconstructing how the method scales.
**Wanted human work:** choosing whether to cook and actually cooking.
**Unresolved work:** obtaining ingredients if needed; we have not inspected the
cupboard or fulfilled a purchase. Do not call that completed assistance.

**Sharpen the proposed Vesper benefit:** if the person explicitly keeps the
eight-person version, reopen that exact method from Life or its related context,
not the original four-person attachment or a freshly regenerated approximation.
A strong comparator may also preserve the response or original thread. Vesper
must demonstrate less refinding/reassembly, not presume competitors cannot save.
**Remove:** mandatory recipe naming, categorization, a meal-planning screen or
post-answer journaling. A failed Keep cannot turn a correct answer into a false
claim that the later-use problem was solved.

### 16.5 Independent Home: a useful selection before another request

**Input H0:** the controlled September 7 NYC world from §15.5: chosen city,
one explicitly kept SNFL place, no usable old Ask history, no active friends and
no inferred availability. The candidate packet includes the four items below
and Art Cart. Public detail is source-bound; no live inventory, route or weather
checks are represented as completed.

**Authored familiar-tool comparator:** a capable city guide/assistant supplied
the same packet can give this entire selection, with source links. A comparison
against a blank map or an unsourced generic “visit a museum” list would be unfair.

**Authored Vesper target, complete scroll at content level:**

| Unit | Finished value received without opening another screen | Optional depth |
| --- | --- | --- |
| **Twenty minutes on the water** | Pier 2's published Saturday, September 12 kayaking program offers a short paddle with equipment and instruction. Advance registration is recommended; weather and available places still need checking. | Exact session and operator information, not a general kayaking search |
| **Same market, different days** | Union Square's roster includes Mushroom Queens' cultivated mushrooms on Monday and Bear Creek Farm's dahlias on Wednesday. Different visits can mean different growers, not merely different queues. These are examples, not exclusive attendance or stock promises. | Compare the relevant day rosters |
| **The cliffs cooled underground** | The Palisades' diabase formed when magma cooled within older rock. Erosion later exposed the resistant rock as the Hudson's edge: the cliff is not simply a lava flow frozen on the surface. | Source-backed geological explanation, without prescribing a hike |
| **Your kept library** | SNFL's public roof terrace remains a concrete place to refind. The indexed NYPL holiday notice lists September 5–7 closures; this is a kept-place note, not a suggestion to visit today. | The exact kept place and current operator information |

The underlying public sources and September 7 checks are recorded in
[§15.5](#155-independent-home-value-in-the-scroll-not-a-menu-of-possible-ai-jobs) and the
[connected Home specimen](nyc-newcomer-connected-home-specimen-2026-09-07.md).
In particular, twenty minutes is paddle duration, not the whole outing; an
indexed closure notice is not a live terrace check. The geological explanation
is supported by the [Palisades park's nature account](https://njpalisades.org/nature/).

**Verdict:** this is already a more credible opening than an empty personalized
dashboard. It offers an activity, a useful comparison, understanding and
refinding. However, equal-access familiar tools can supply the same facts and
good selection. Vesper's extra hypothesis is that an appropriately composed
selection arrives here without requiring another research brief, and remains
connected when something becomes useful. We have not measured that advantage.

**One new context item H1:** within the current encounter the person says,
“I'd like something hands-on, but not a class or course.” This is an immediate
purpose, not a durable identity or evidence of free time today.

Give that fact to both treatments. Replace the kayaking lead with:

> **Make something without signing up for a course.**
>
> Bryant Park's Art Cart provides free drawing and craft supplies. Check in
> with the host on the north end of the Upper Terrace and make something for
> a while. The published April–September hours are daily, 11 a.m.–7 p.m.
>
> [Art Cart details](https://bryantpark.org/activities/art-cart)

The park distinguishes the general supplies offer from separately registered
workshops. This suggestion is for the former; it does not claim every workshop
is drop-in or that supplies/current conditions have been checked on site.
[Operator page, checked September 7](https://bryantpark.org/activities/art-cart).

**Changed complete composition:** Art Cart → market-day comparison → Palisades
explanation → kept library. Kayaking leaves this Home selection; it can remain
discoverable in Places without being falsely classified as a rejected interest.
We have changed the candidate and the proposed experience, not added “because
you like making things” to the old lead. The other three units preserve breadth;
one practical purpose need not make the whole page a single-topic feed.

**Work removed:** source discovery, a bounded candidate comparison and
distinguishing casual use from a course commitment. **Wanted human choice:**
whether any of these possibilities appeals. **Unresolved service work:** route,
live disruption and conditions if the person now wants to go. A source link is
an honest next door but not the same as having checked the trip for them.

**Sharpen:** Home must earn its selection as a whole. Dropping the private library
save should still leave a useful newcomer page. Dropping a redundant unit should
improve it. The four-unit manuscript is a matched comparison, not a canonical
feed-length cap. A longer Home must keep adding distinct value, not stretch these
four items into more cards. **Remove:** more input prompts, memory commentary,
duplicated explanations of personal fit and a compulsory action under every read.

### 16.6 Social: preserve the human gift; add help when it helps

**Input S0:** Maya's fictional addressed photograph, exact note and attached
recipe D. The recipient already has permission to receive it. No active social
graph, Occasion or reciprocal contribution is required.

**Authored familiar-tool comparator:** an ordinary direct message can provide
the photograph, this full note, a readable attachment and a human reply:

> Made this with the last tomatoes from the market. The sauce never touches
> the stove. Thought you'd like it.

**Authored Vesper target:** the same photograph and Maya's words, followed by a
compact faithful preview of the attached recipe:

> **Tomato pasta · for four**
> 400 g pasta · 600 g tomatoes · 120 g cheese.
> Mix the tomatoes and cheese in a bowl, cook the pasta, then toss together.

Reply to Maya is the ordinary human continuation. Private Ask is separately
available. No AI paragraph explains what this gesture means about their friendship.
The recipe preview counts as convenience only if the original attachment was
harder to use; it is not automatically a substantive improvement over messaging.

**Verdict:** tie in the core social benefit. Maya adds the relationship and the
pleasure of receiving something chosen for the person. Preserve that value.
Removing Maya would leave a different, less personal encounter even if the
recipe were identical. Removing unnecessary Vesper interpretation improves it.

**One new context item S1:** the recipient privately asks, “How much for six?”
Both treatments receive the exact recipe and question. The finished answer is:

> **600 g pasta · 900 g tomatoes · 180 g cheese.**
> Keep Maya's method: mix the tomatoes and cheese in a bowl, cook the pasta,
> then toss together. Use batches if your pot is crowded.

An assistant with the attachment can match this. Vesper's intended advantage is
asking directly on the received object, privately, without re-uploading or
reconstructing it. Whether a familiar-tool workflow already makes that easy is
part of the comparison, not a pre-decided Vesper win. This private adaptation
does not change Maya's attachment or send her the question.

**Work removed if the path works:** finding, copying and restating the original
for assistance. **Wanted human choice:** enjoy, reply, cook, share onward where
allowed, or do nothing. There is no outstanding work just because no reply was
sent. The recipient may later write “Want to make this together Friday?”; that
is an optional human opening, not permission to generate an accepted plan.

**Sharpen:** retain ordinary non-photo contributions, exact source help and an
easy path from an actual shared intention into arrangements. **Remove:** requiring
an Occasion before sharing, AI-authored intimacy, response debt and pretending
that every friend artifact needs a synthesized juxtaposition. A Rome–Paris
comparison still earns a place when it supplies an actual useful contrast; this
recipe encounter does not need one to qualify as social value.

### 16.7 Decisions from the comparison

| Keep | Sharpen | Remove from these encounters |
| --- | --- | --- |
| Good ordinary answers, even where familiar tools can match them | The actual contribution made by eligible context: changed interpretation, candidate, quantity or next usable result | Differentiation claims based solely on personalization, memory, extra buttons or prettier copy |
| Generous independent Home value | Whole-page selection and prepared supply; a fresh encounter must remain useful without a rich archive | Placeholder prose describing what an opening or perspective could do |
| Original human sharing as complete value | Optional help that inherits the exact authorized subject and leaves authorship intact | AI enrichment as an admission fee for social content |
| Practical instruments and source-bound checks | A usable current judgment when requested, with exact unresolved work made legible | Calling a provider link, typed instrument or generic fallback a completed practical service |
| Exact retained-result access and continuity | Observe how much re-explanation, searching and reassembly the person actually avoids | A compulsory capture-organize-return funnel appended to every payoff |

**The proposed advantage is a better complete experience, not four individually
unmatchable answers.** That is also the burden of the strategy: the result must
be worth receiving now, and the person should not become the integration layer
when its significance changes. Home, Chat, Places and Life are complementary
ways to receive, work with, explore and retain those results—not four extra jobs.

The live engine belongs inside this promise. Stable explanation or a recipe can
remain useful without live data. A question about going, meeting or adapting
should invoke the relevant current judgment; the engine's value is the workable
answer, not merely the instrument's presence. The review does not retire live
help because its source/feasibility work is harder, nor reinstate booking execution.

### 16.8 Handback to existing lanes: finished results, not another framework

Use these as four parallel receiving requirements within the existing roadmap,
not a single-loop launch restriction or a reason to stop system integration.
No new lane, runtime job or policy change is dispatched here.

1. **Curiosity / Content:** supply a captured source-backed answer and its
   corrected-known-fact continuation. Inspect whether the second genuinely adds
   another supported angle. Do not substitute an authored fixture for generation.
2. **Practical / Integration:** carry exact D through assistance, a serving-count
   change and an explicitly requested retained-version reopening. Show the
   actual quantities/method received and which steps still require reconstruction.
3. **Home + Places / receiving and supply:** capture the complete sparse-context
   selection and its changed-purpose composition. Open the exact suggested
   activity, ask for practical help, and return without losing the subject.
   Review the selection and unresolved real-world work, not just routing success.
4. **Social + Life / existing object paths:** receive the original, ask privately
   on its exact attachment and optionally retain the permitted result. Show that
   original-only receiving remains complete. Do not require a new social system
   to demonstrate ordinary private help on an authorized object.

For each capture, attach: pinned build/branch; supplied and permitted inputs;
actual visible result; source freshness; hidden human preparation; work left to
the recipient; destination/result continuity; failures; and any measured cost
or latency. **Unmeasured stays unmeasured.** Do not label an authored target a
production result, or report an integration test as evidence of consumer demand.

Keep content production proportional to the job. The recipe arithmetic can be
checked deterministically; original sharing does not need a synthesis pass;
source-grounded public explanations can be reused where terms and freshness
allow; private selection and current feasibility have separate costs. This is
a cost-conscious design recommendation, not a measured unit-economics result or
authorization to generate an entire feed on each root read.

The next review should put these actual results beside the authored comparators
and accept **better, equivalent, worse or not yet demonstrated**, with reasons.
Do not average a failed practical outcome away with an excellent essay. Conversely,
do not reject a useful plain answer because it fails to exhibit every product move.
If the response is equivalent but the complete workflow is materially easier,
that is a legitimate result—provided the reduced work was actually observed.

This pass changed working research only. It did not change application code,
design exports, canonical product wording, feature flags, audiences, retained
memory, background workers or external actions. The deterministic rehearsal is
the only runtime diagnostic executed here; lane-reported tests remain attributed.

## 17. Executed receiving capture and remaining encounter gaps — September 7

### 17.1 Outcome: stronger delivery evidence, not four completed consumer runs

**The receiving system can preserve useful material, separate changing practical
facts, and recover exact prepared content. The complete four encounters are
still not demonstrated end to end.** This pass captured existing implementation
outputs instead of writing another set of ideal answers.

- **73 backend tests passed** across practical root delivery, Home portfolio,
  prepared Source serving and public Place-content handoff.
- **34 mobile utility tests passed** across root navigation and return-context
  restoration. No UI render or native interaction was tested.
- **Twelve result records were captured** from existing test functions: selected
  compiled root fields, candidate payloads, retained-result reads and one public
  content handoff. All corresponding test calls passed.

The [capture JSON](evidence/received-value-2026-09-07/receiving-capture.json)
preserves the selected payload fields without editorial rewriting. The
[capture command](evidence/received-value-2026-09-07/capture-command.txt)
reproduces the observation of existing tests. It is an inspection aid, not a new
product evaluator, service, registry or production capture endpoint.

**Pinned implementation:** backend `9d3127084d128fec33bb610dba17094ff3d3fea6`
on `main`; mobile `c3feb89f05a5761c14985c9e0cea709afdf8f114` on
`codex/entity-object-design-completion`; workspace
`382d369a9f30722562e01d974f6409d0793863a7` plus existing working documents.
Backend and mobile source were unchanged during the capture; the pre-existing
backend product-document edit was not touched. Home/Life isolated-branch work
was not silently substituted into this checkout.

Database engine factories and Python socket connection calls were blocked for
the backend capture process. The tests supplied synthetic owner reads, records,
sources and producer responses. Existing pytest configuration prevented durable
observability writes. No database cleanup, provider acquisition, real-person
message, new retained user object or paid model job was performed. Pytest's
5.76 seconds and Jest's 1.182 seconds are test-run timings, **not product latency**.

The Content task has now committed its research/publication repairs in
`9d3127084`; §16.2's active-fix status is historical. Its completed report also
says two live-key synthesis tests encountered an exhausted Anthropic credit
balance. That is attributed lane evidence, not an independent billing check.
This pass did not retry paid calls, switch providers or change model settings.

### 17.2 What was actually received at each inspected boundary

#### A. Root delivery preserves substance when a practical fact disappears

The existing [practical-delivery test](../../travel-agent/tests/api/test_practical_root_delivery.py)
runs real adapters, owner-read handling, judgment and root composition over a
synthetic feed. Its treatment/delivery persistence bindings and several owners
are substituted. It is not a full authenticated HTTP or native journey.

The captured Home output with a current observation includes:

> **Bookshop**
> Open now · Independent publishers upstairs

Beside it, the reading survives intact:

> **The working waterfront is still shaping dinner**
> Red Hook's newer kitchens occupy the same industrial edge that once kept the
> neighborhood apart from the subway city.

When the opening observation is missing, or expires while composition is
finishing, the bookshop relation becomes:

> Independent publishers upstairs

The independent reading remains. Places runtime produces the same substantive
separation in its own unit kinds; the captured workspace feed also removes the
unusable `open_now` claim. All 21 condition/surface combinations in that test
passed; the JSON retains six selected Home/runtime cases rather than pretending
to capture all 21.

**What this demonstrates:** volatile conditions do not have to erase all the
value or leave a stale operational claim behind. The system can preserve a
reason to be interested while declining to say a place is open.

**What it does not finish:** “Can I go now?” still needs the current evidence
relevant to the person's actual situation. An omitted opening claim is not a
completed feasibility check, route, substitute destination or verification of
inventory. The bookshop and waterfront sentences were authored by the fixture;
this is no evidence that Vesper researched them or that the reading adds enough
substance for a person who already knows that neighborhood.

#### B. Prepared value survives root changes and exact refinding

The existing [Source-serving tests](../../travel-agent/tests/root_projection/test_source_contribution_serving.py)
invoke real orchestration and serving with a deterministic authored producer,
synthetic source inventory, and in-memory record loaders. They capture the same
prepared production for both roots and reopen it by its digest independently
of current discovery ranking.

One production yields these different root expressions:

| Home | Places |
| --- | --- |
| Title: “The route was tracing an older public boundary” | Title: “Where the working edge still divides the waterfront” |
| Comparison: “The lived trace” beside “The wider context” | Spatial anatomy identifying “The working edge” |
| Shared substance: “The evening route was crossing a working-waterfront boundary that still shapes how public life reaches the water.” | The same shared substance |

**What this demonstrates:** Home and Places can express one prepared contribution
differently without requiring separate meanings or independently regenerated
answers. The exact serving test returned the original prepared object.

**What remains:** this fixture's prose and `new_to_person` label come from
[`_draft`](../../travel-agent/tests/root_projection/test_source_contribution_runtime.py),
not from an evaluated model or a reader's response. The comparison is still
abstract: neither concrete access geometry nor a fully developed explanatory
mechanism appears in these short labels. Treat it as a valid typed example,
not as a consumer-quality win over §16's familiar-tool comparator.

The record loader here is in memory. A successful digest read is not a demonstrated
database write → mobile Keep → Life rediscovery journey. The exact workflow-result
route remains dark under the [Integration receipt](source-connected-value-execution-receipt-2026-09-07.md).
Do not present this as proof that a person can already save and reopen the
eight-person recipe version from §16.4.

#### C. The Home portfolio combines families; that is not yet a rich newcomer Home

The [four-family Home test](../../travel-agent/tests/root_projection/test_home_portfolio.py)
captures an assembled candidate portfolio containing:

- the waterfront reading;
- Maya's actual note, “Try the back room after seven; it changes the whole place.”;
- a Brooklyn context door whose relation is simply “Home”; and
- a “Move dinner later” proposal whose relation is “A reviewed Plan change is
  ready for the group.”

Its existing assertions verify that all four survive selection with typed
destinations. The captured list is the **candidate stage**, including orientation
and week chrome—not a screenshot or the final governed full-scroll root.

The two door labels provide navigation but do not deliver a concrete afternoon
or a reviewable before/after dinner change on their own. More importantly, these
particular proposal and context inputs do not contain all the detail needed to
do that. Do not infer from this test alone that the real owner or detail screen
lacks it. The open requirement is to show the complete selected experience with
realistically complete owner material.

A separate graph-unavailable fixture yields “Start anywhere” and an unmarked
week. **That is a failure/degradation scenario, not evidence that every healthy
newcomer receives an empty Home.** It also cannot substantiate the independent
NYC selection from §16.5. That selection and its changed-purpose replacement
remain authored targets, not executed supply outputs in this capture.

There is a placement distinction to preserve: the current
[Home design handoff](claude-design-home-artifact-led-visual-value-handoff-2026-09-05.md)
(September 7 section 13, **local WIP** at this capture)
keeps casual friends' place-sharing in Places and studies a contribution to a
shared evening in Home. The backend addressed-note adapter establishes a
capability, not a decision to place every casual note on Home. Align actual
candidate selection with the agreed experience rather than letting a test
fixture decide the design by accident.

#### D. Social attribution works at the adapter; exact private assistance has a seam

**Historical pre-fix capture:** [§18](#18-addressed-note-to-private-help-implementation--september-7)
subsequently closes the exact-note/private-Ask gap described here. The attached
material, retained adaptation and full generated receiving experience remain
separate boundaries; the table below is not the latest note-only route status.

The addressed-note adapter preserves Maya's original sentence, associates it
with the venue and rejects a different recipient. This is useful evidence that
the friend need not be replaced by Vesper-authored social prose. It is an
adapter-level capture, not a complete share → receive → reply session.

The mobile [navigation implementation](../../travel-app/utils/rootProjectionNavigation.ts)
and its passing [tests](../../travel-app/__tests__/utils/rootProjectionNavigation.test.ts)
show a precise limitation:

- Supported venue/site/accommodation/experience/dossier subjects can create a
  private seeded conversation. A dossier takes priority over an incidental venue.
- A destination containing **only a `place_handoff` reference** returns
  `/(tabs)/concierge/chat`, not a conversation seeded with that note.
- Adding a venue can supply a venue seed; that is not equivalent to passing
  the friend's exact note or attached recipe.

This is a deliberately bounded fallback, not a newly introduced regression or
evidence that every source-entry path in the app is broken. But it means this
root-navigation path cannot yet demonstrate S1's promised reduction in re-pasting.
Adopt an appropriate existing source-context path where available, or resolve
the missing subject contract, before calling this encounter connected. A generic
Chat door must not be counted as exact-object assistance.

The [return registry's tests](../../travel-app/__tests__/utils/rootProjectionReturnRegistry.test.ts)
also passed: supported paths preserve origin, selected references and one-time
restoration, while changed identity/audience leads to recomposition. These are
valuable navigation guarantees, but they cannot restore subject context that
was never supplied to the conversation.

### 17.3 Comparison against the promised four encounters

| Intended encounter | Current evidence captured | Complete-experience verdict | What still sits with the person or is unobserved |
| --- | --- | --- | --- |
| E: explanation, then an already-known correction | A supplied reading survives composition; a prepared comparison has root-specific expressions | **Not yet demonstrated** for the actual explanation/correction pair | Research quality, a genuinely different supported angle, and whether the person must repeat the correction |
| D: usable recipe adaptation, changed count, selected-version reopening | Exact prepared-object serving and mobile owner navigation work in separate tests | **Not yet demonstrated** for recipe D | No captured cooking answer, authoritative retained adaptation or mobile-to-Life reopening; existing Source serving does not substitute for these |
| H: worthwhile independent Home, then changed-purpose selection | Concrete supplied content and practical expiry survive root delivery; multiple families survive candidate selection | **Partly demonstrated mechanically; selection value unobserved** | Candidate research/selection, complete sparse-context scroll, exact practical continuation and wanted human choice remain separate questions |
| S: original receiving, then private help on the attached object | Attribution and recipient filtering at the adapter; supported contextual routes and safe fallback at mobile navigation | **Original-note mechanism demonstrated; full private-help encounter not yet** | Addressed-note-only navigation does not supply the exact subject; full receipt, optional assistance and permitted retained result are not captured |

None of these verdicts is a consumer preference result. The actual generated
answers needed to rate **better/equivalent/worse** against the authored comparators
were not available in this pass. The integration checks are a meaningful advance
in evidence, but are not a substitute for those answers.

### 17.4 Consequence for the roadmap

**Continue the system work, but make three concrete connections the next receiving
checkpoint.** This is a refinement of existing lane deliverables, not a new
parallel framework or authorization to edit their code here.

1. **A real result on a real supported entry path.** Content should supply
   source-backed output through the application's producer once its execution
   prerequisite is available; Integration should capture the exact result
   returned. Start from the E/H packets already written, retaining sparse and
   changed-context cases. Restoring model credits alone does not finish owner,
   supply or navigation work.
2. **Exact subject into private help.** Resolve the addressed-note/attached-source
   handoff without losing author, source identity or permitted use. Check any
   existing source-entry implementation before introducing a new seed kind.
   Capture what reaches the assistant, not merely that Chat opens.
3. **Exact useful result into deliberate retention and refinding.** Home's latest
   handoff explicitly leaves the saved-piece owner and P3 behavior unresolved
   with Life. Resolve that small ownership seam before advertising the selected
   recipe/explanation as saved. Do not multiply artifact stores or make a generic
   Source result route stand in for the consumer's retained object.

Practical current-state work remains embedded in these encounters. If a person
asks whether the proposed activity works now, show the bounded assessment and
what it leaves unresolved. Preserve the independent explanation or original
human contribution when an operational check fails. This is where the live
engine supports the whole product rather than becoming a separate dashboard.

Keep the handoff distinction explicit: the supplied manuscripts tell the lanes
what a worthwhile result might look like; these captures show what selected
mechanisms currently do; subsequent live output must establish the quality of
the actual result. No new wording, notification, history agreement, worker
activation, model purchase or design export was changed by this execution pass.

## 18. Addressed note to private help implementation — September 7

**The next step is partly implemented, not merely specified.** Root navigation
can carry a versioned relationship note into the existing private composer;
the server can resolve its actual text for the recipient's explicit question.
This closes the note-only subject gap recorded in §17.2.D. That section remains
a historical capture, not the current behavior for a valid versioned note.

### 18.1 What changed

- The client carries only `place_handoff` ID and revision. The friend note
  takes precedence over an incidental venue. Missing or malformed revision
  does not become a guessed note or a venue substitute.
- The private composer displays a removable **Friend's note** attachment and
  waits for the person's question. Removing it retains the draft while dropping
  the note reference from the pending turn. Opening does not send, Keep, reply
  to the sender, create an Occasion or ask for another upload.
- The server reads `domains.relationships.repository.get_place_handoff`, not
  the separate legacy integer-place store. It requires an exact current
  revision, the intended recipient, pair/send-now scope, active status,
  valid expiry and contextual inference permission. A sender's participation
  is not the recipient's inference authority.
- Group turns drop the entire note seed before owner access. Owner failure,
  revoked access or changed state cannot be replaced by client-supplied prose,
  incidental Trip context or a location packet. The existing UUID namespace
  flag remains in force; this pass does not enable it.
- The supplied text remains an attributed human contribution, not a Vesper
  rewrite or a claim about the recipient's personality. No attachment contents
  or private sender profile are fetched.

Implementation: note reader `travel-agent/backend/concierge/handoff_entry.py`
(**local WIP**, not committed with this documentation),
[entry boundary](../../travel-agent/backend/concierge/entry_context.py),
[private/group assembly](../../travel-agent/backend/concierge/agent.py),
[root navigation](../../travel-app/utils/rootProjectionNavigation.ts), and
[existing composer](../../travel-app/app/conversations/create.tsx). The bounded
cross-repo contract is documented in the
[Conversation Seed standard](../../travel-app/docs/conversation-seed/Standard.md)
(September 7 addressed-friend-note section, **local WIP** at this receipt).

### 18.2 What this does not finish

**S1's attached-recipe encounter is still incomplete.** The current reader
supplies only the authored note, explicitly marking attachments as not loaded.
Knowing that a photo or recipe was attached is not access to its contents.
Neither a model response based on that recipe nor a complete receive/help/save
journey was generated in this pass. This is not an account-wide memory feature
or a guarantee that previous answers are causally repaired after withdrawal.

Three dependencies remain with existing owners rather than new stores:

1. **Source/Integration:** authorized attachment content and a complete request
   → runnable producer → exact result path. The updated
   [Source control mapping](source-request-result-control-mapping-2026-09-07.md)
   still distinguishes request purpose, workflow state and readable result.
   A terminal-state improvement does not settle request semantics or produce
   the actual explanation/recipe used in the encounter.
2. **Life with Home:** choose the supported owner and reopen semantics for the
   exact deliberately saved adaptation. The
   [Home-to-Life handoff](claude-design-home-artifact-led-visual-value-handoff-2026-09-05.md)
   (September 7 section 13, **local WIP** at this receipt)
   is still the seam to resolve. Saving the original note or an expiring Source
   production cannot silently stand in for saving the adapted result.
3. **Content with Integration:** collect actual supported producer output for
   the E/D/H/S comparisons once execution prerequisites are met. No model credit
   purchase, provider substitution, worker activation or real generation was
   performed here. Authored examples and test assertions remain labeled as such.

This preserves the strategic test: does received value improve, and does less
reconstruction remain with the person? Connecting one missing owner is useful
system progress, not a decision to narrow the whole product to this encounter.

### 18.3 Verification and integration receipt

- **77 backend tests passed:** the new note-reader cases plus the existing
  conversation-seed suite. Owner calls were mocked; database connection factories
  and network sockets were blocked. This verifies the receiving boundary, not
  a production database round trip or a generated answer.
- **75 mobile tests passed:** root navigation, root return registry, conversation
  seed serialization and composer rendering/handoff. The new cases include
  explicit send and removal-with-draft-preservation. Typecheck passed; scoped
  ESLint had zero errors and one existing import-order warning in the smoke test.
- Ruff and cross-agent import checks passed. No API route or generated schema
  changed. No database migration, model invocation or flag activation ran.
- The broad offline backend run was attempted but stopped during collection
  on an in-progress indentation error in Content's
  `tests/research_agent/test_experience_research.py`. That owner was notified;
  its file was left untouched. This is not a whole-suite pass.
- Chat scenario and design-reference checks passed. After starting a temporary
  offline Metro server, the registered `vesper-chat` doctor passed. No native
  screenshots were captured or judged; the new attachment is not device-certified.
- Workspace document governance reported an unrelated expiry violation in
  `fixtures/shared-fixture-world-2026-09-07.md`; this pass did not edit that file.
- A concurrent Integration merge (`f4401ef73` in mobile) absorbed the in-progress
  navigation/test portion. Integration was notified that the remaining seed
  type, composer, backend and documentation changes still require integration
  together. This task did not create a commit, push or claim a clean checkout.

## 19. Four consequential strategy questions — September 7

### 19.1 Conclusion, method and decision status

**Subsequent founder-requested follow-through:** the product and evaluation
direction from this round is now recorded in the dated
[September 7 strategy refinement](../decisions/2026-09-06-reconcile-consumer-strategy.md#5-september-7-refinement-complete-benefits-selective-context-and-voluntary-choice),
with acceptance mapped into
[roadmap §9.8.11](complete-system-integration-roadmap-2026-09-05.md#9811-supported-service-and-received-value-acceptance--september-7).
Product Thesis, Product Model, Editorial Canon, Growth and Monetization were
aligned. The research findings below retain their evidence status: no consumer
study was run and no runtime capability was added. History/material/use policy,
launch coverage, paid packaging and rollout remain separate unresolved decisions.

**Offer follow-through:** the [v1 service candidate](vesper-v1-supported-offer-2026-09-07.md)
now makes the recommended audience, situation range, coverage and responsibility
boundaries concrete. Its three-entrance review uses §§17–18 and newer lane
receipts; it does not replace those receipts with a second readiness ledger.

**Keep the broad product, but make its promises much more concrete.** The
remaining uncertainty is not best resolved by another grammar, another tab or
a single launch loop. It concerns what reliably reaches a person, which context
improves it, how the whole experience earns attention, and what makes someone
choose and fund it again.

| Area | Recommendation from this round | Still a decision or evidence gap |
| --- | --- | --- |
| Complete supported service | Bound world coverage and responsibility while completing the user's benefit across the existing repertoire | Exact supported jobs, material types, geography and degraded-service behavior |
| Ongoing relationship | Selective long-range continuity, with present circumstances and corrections outranking stale assumptions | Actual history/use agreement, eligible material, lifecycle and effective implementation |
| Judgment and received value | Judge substantive results and the whole receiving experience, including when context should not influence it | Actual producer quality, useful supply and human preference beyond authored specimens |
| Audience, distribution and payment | Start with existing question/save/share behavior; let recipients benefit lightly; investigate payment for dependable assistance | Voluntary choice, natural return, renewal and whole-cohort economics |

This is a targeted synthesis of primary research, official product descriptions
and current repository evidence, checked September 7, 2026. It is not a systematic
literature review, hands-on competitor benchmark, participant study or production
cost audit. Source findings and Vesper-specific recommendations are separated
below. Older research is included where its question is more relevant than its
publication year; 2026 preprints are not treated as settled consumer evidence.

The main internal baseline is the accepted
[consumer-strategy decision](../decisions/2026-09-06-reconcile-consumer-strategy.md),
the [contribution contract](../systems/contribution-and-consequence.md),
[Product Thesis](../../travel-agent/docs/product/Product%20Thesis.md),
[Growth Strategy](../../travel-agent/docs/product/Growth%20Strategy.md) and
[Monetization Strategy](../../travel-agent/docs/product/Monetization%20Strategy.md).
The newest continuity recommendation is explicitly **proposed**, while the
receiving implementations in §§17–18 are bounded engineering evidence. Neither
turns the authored E/D/H/S encounters into observed consumer outcomes.

### 19.2 Complete service: finish a benefit, not every downstream operation

#### Research findings

Amershi and colleagues' CHI 2019 human–AI guidelines were evaluated with 49
design practitioners across 20 AI-infused products. They support making
capabilities and limits understandable and supporting correction across an
interaction. They are design guidance, not evidence that users want Vesper or
that a particular launch scope will succeed.
[Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/).

Granola's documented enhanced-notes flow combines a transcript, the person's
notes and meeting context into a finished result; the person can inspect its
source material. This is a useful precedent for attention guiding a richer
output. It does not establish that Vesper should copy workplace capture,
retention or pricing, or require people to record everything.
[Granola enhanced notes](https://docs.granola.ai/help-center/taking-notes/ai-enhanced-notes).

The NBER working paper on ChatGPT use identifies ordinary information seeking
and practical guidance among major uses. That supports meeting an existing
question/help behavior, not assuming demand for a new life-documentation habit.
It does not demonstrate switching intent or a Vesper advantage. This inference
uses the publisher abstract, not a new analysis of its underlying conversations.
[How People Use ChatGPT](https://www.nber.org/papers/w34255).

#### Recommendation for Vesper

Specify a complete offer through recognizable received benefits, not the list
of services we have implemented:

- **Ask about something:** receive a substantive explanation, comparison or
  adaptation from the question or material currently available. A direct answer
  can finish without a suggested project, Keep prompt or reflection exercise.
- **Open Home or Places:** receive worthwhile world material and possibilities
  without first supplying a rich biography. Curiosity, enjoyment and orientation
  count; not everything must become an outing.
- **Get practical help:** receive a grounded assessment or preparation for a
  supported situation, including what remains uncertain and what the person or
  provider still needs to do.
- **Receive something from a person:** enjoy the actual contribution or offer
  without equivalent effort. Optional private assistance must preserve its
  subject, attribution and permitted uses.
- **Return to something entrusted:** reopen the exact deliberately retained
  result or source with its meaning and ownership intact, not merely a related
  chat, venue or reconstruction prompt.

These are service acceptance descriptions, not five new product nouns, five
paywall tiers or a mandatory sequence. The four existing moves can combine
differently in each. The release need not support every conceivable attachment,
city, provider or background condition to support these benefits honestly.

**Define the boundary along three dimensions:** the situations/materials we can
handle well, the world coverage we can substantiate, and the responsibility we
actually accept. This is more useful than either “we do everything” or “we only
do one loop.” Broad input does not mean equal specialist competence everywhere.

The live engine belongs inside that offer. It can assess whether something
works now and protect its purpose when circumstances change; it should not
appear only during a trip emergency. But current assessment is different from
an accepted watch. Keep, payment and a suggested next step do not imply future
checking. A bounded watch needs sources, duration, permitted treatment and
failure/stop behavior before anyone relies on it.

External handoff can be a complete **Vesper** service without pretending to be
a completed real-world transaction. Preparing the right option and preserving
context for the provider is legitimate. Claiming a reservation is made, or
leaving the person to redo all the research, is not. We should retire unnecessary
operational UI without making the remaining assistance vague.

#### What the repository still needs to resolve

The [Source request/result mapping](source-request-result-control-mapping-2026-09-07.md)
distinguishes a contextual warm request from an exact commissioned explanation
or comparison. Its recorded next steps include request semantics, executable
ingress and an exact consumer result. Terminal-state support alone does not
finish that service. Similarly, §18's recipient-note reader is not access to an
attached recipe, and saving the original contribution is not saving the adapted
answer. These are connected completion gaps, not reasons to redesign the system
around one social case.

The acceptance review should include sparse context, no friends, an ordinary
week, unavailable fresh generation and changing world conditions. A fallback
must be judged on what it actually delivers: a generic answer is not made useful
by calling it graceful degradation. With insufficient evidence, narrow the
claim or stop before reliance rather than silently replacing the requested job.

**Decision to make:** name the first supported offer and its limits in the
existing integration roadmap. Keep the representative portfolio broad. Do not
wait for universal coverage, and do not advertise unfinished service transitions.

### 19.3 Continuity: long memory, short-lived assumptions

#### Research findings

Jones and colleagues' CHI EA 2025 study combined six regular-user interviews
with 54 Reddit threads. Participants struggled to understand what memory stored
and influenced; task and context boundaries mattered, and users developed
workarounds for them. This preliminary qualitative sample is not population
evidence or a basis for a particular retention duration.
[Users' Expectations and Practices with Agent Memory](https://younghokim.net/files/papers/jones-agent-memory-chi25lbw.pdf).

The January 2026 OP-Bench preprint usefully separates irrelevant personalization,
repetition and sycophancy. Importantly, its dataset was deliberately filtered
for cases where memory-conditioned responses were inappropriate. Its reported
failure rates therefore cannot estimate how often ordinary consumers experience
those problems. Use it to broaden failure cases, not to select a memory system
or claim that more memory generally harms users.
[OP-Bench](https://arxiv.org/abs/2601.13722),
[dataset construction, Appendix A.2](https://arxiv.org/html/2601.13722v1).

#### Recommendation for Vesper

I favor the latest proposal's **selective long-range continuity**, rather than
a universal 90-day automatic-use cutoff, because the product intentionally
connects life across months and years. That is a strategic judgment, not an
empirical finding that a particular duration is optimal. The old Sorrento
question can remain relevant to a new landscape; the old rental-kitchen
constraint should not define today's kitchen.

The distinction we need is:

- A historical exchange may remain available under its agreement.
- Its relevance to today's question must be earned again.
- A circumstance described then does not remain current merely because it is
  stored or mentioned in a newer answer.
- Its source, subject, corrections and allowed uses survive retrieval.

This is not a choice between forgetting everything and maintaining a global
personality profile. The [latest proposal, §10](conversation-history-source-expiry-decision-proposal-2026-09-06.md#10-selective-long-range-continuity-four-complete-experiences)
already moves in the right direction. It is still unadopted: the existing
Ask/T0 and expiry contract remains binding, with no historical backfill.

The subsequent [control refinement, §4](conversation-history-source-expiry-decision-proposal-2026-09-06.md#4-simple-controls-with-exact-consequences)
is the latest recommendation for explaining and limiting that use. It separates
requested help, on-visit discovery, interruption and external/shared consequence;
an early explanation is not blocking configuration. It recommends scoped effects
and off-with-clearing, not a newly selected pause mode. These remain proposals.

**Memory should compete for influence, not demand visible credit.** The answer
need not begin “because you asked about this in September.” Sometimes context
improves selection, excludes a wrong assumption or reduces re-explanation.
Sometimes it adds nothing, and a fresh answer is just as good. An original
friend invitation does not need a manufactured callback to prove intelligence.

The day-one/day-two/day-five problem illustrates the deeper requirement. A
first discussion may mention a stairs constraint; a later explanation attributes
the difficulty to a lift's closing time; a still later correction says it was
for the person's parents on that outing. Useful continuity preserves all three
relations without making the constraint permanent, deleting independent history
or transferring a parent's circumstances into the user's profile. The latest
proposal's access specimen makes that distinction explicit; it is synthetic,
not a claim about the founder or their family.

For consumer comprehension, favor one legible optional agreement for eligible
ordinary private conversations, with clear exclusions and controls at the point
of use. Do not require per-turn classification or a weekly memory-cleanup queue.
However, “one legible agreement” cannot erase the distinction between readable
history and permitted later use, nor attachment lifecycles, sensitive material
or another person's permissions. The scoped
social source-use proposal, `scoped-source-use-grant-decision-proposal-2026-09-07.md`
(**local WIP**),
correctly keeps original receiving separate from model use and retained
derivatives; its agreement mechanism remains unresolved.

Useful correction should match what the person means: “that was for my parents”
changes attribution; “not tonight” changes a situation; “don't use this again”
changes eligibility. These are proposed experience requirements, not a request
for three more settings screens. Deletion and revocation must also reach
dependent future outputs and in-flight work; a prettier memory panel cannot
substitute for that behavior.

#### How to evaluate the decision

Compare the same current question and available world evidence with no history,
indiscriminate history, and selectively eligible history. Count appropriate
non-use, correction survival and reduced reconstruction alongside useful recall.
Include an old curiosity, a temporary constraint, an unrelated new purpose,
a return after months, withdrawn material and an original social contribution.
Keep the no-history alternative capable; ties are legitimate.

**Decision to make:** settle the actual material/history/use agreement and
repair behavior in the existing proposal before activation. Research supports
clear boundaries and evaluating misuse; it does not authorize retention or
determine the policy on behalf of users.

### 19.4 Judgment: diverse reasons to receive value, not merely diverse cards

#### Research findings

Wang and colleagues studied whole-page recommendation diversity by user intent,
rather than item dissimilarity alone. Their YouTube experiments reported improved
enjoyment and daily activity. The transferable idea is that different-looking
items can still serve the same narrow purpose. YouTube's scale, behavioral
inference and engagement objective are not Vesper's product or permission model.
[Beyond Item Dissimilarities](https://arxiv.org/abs/2405.12327).

A RecSys 2025 paper compared LLM serendipity judgments with two existing
human-study datasets in movies and e-commerce. Its best reported Pearson
correlation was 0.215—not 21.5% accuracy. Although the authors see promise in
LLM evaluation, my inference is that we should not let model reviewers certify
consumer delight. These domains and datasets also do not directly establish
quality in Vesper's lived-world situations.
[Exploring the Potential of LLMs for Serendipity Evaluation](https://arxiv.org/abs/2507.17290).

#### Recommendation for Vesper

Home can contain history, food, local places and social material and still feel
repetitive if every unit says “here is another interesting fact related to your
trip.” Diversity has to include **why this is worth receiving**: understanding,
enjoyment, practical relief, a human perspective, or a possibility that makes
the coming week feel more open. These are examples, not five fixed sections or
quotas. The four moves remain an uneven repertoire across roots.

This is also why a rich Home should not be reduced to a tiny dashboard, while a
long scroll should not become a personalized magazine assembled on every visit.
The person can browse without having an urgent task. We still owe each item
substance and the whole page a reason for its composition. Quiet aesthetics
must not mean an empty life; forward value must not exclude an interesting recap.

Review at two levels:

1. **The result itself:** what new understanding, enjoyment, practical relief
   or human connection is actually supplied? Is its subject distinctive, its
   claim supported and its form usable? Repeating the person's observation with
   a clever title does not pass.
2. **The whole encounter:** why this selection here, what else does the page
   crowd out, and how much work remains if the person wants to use it? Does an
   excellent explanation become the fifth unwanted trip callback? Can a social
   offering remain complete without mandatory Chat, planning or saving?

The live engine contributes feasibility when the item implies an actual outing,
time, condition or commitment. It should not operationalize every curiosity.
A landscape explanation can be complete without a route; a recommended outing
cannot rely on that explanation as evidence that access is currently safe or
open. Historical personal context chooses a relevant subject; independent world
evidence supports the facts and present practical claims.

For production, the existing
[world-supply roadmap, §12](recommendation-world-supply-architecture-and-roadmap-2026-09-07.md#12-next-execution-batch-connected-content-lifecycle)
offers a compatible direction: separately governed reusable public material,
private selection/composition, and current validation where required. It records
useful lifecycle work but also remaining supply/activation dependencies. It does
not establish consumer-quality output or final cost. Do not add a second content
store or research-on-GET architecture to answer this strategy question.

The economic and editorial implications align. Reuse a well-supported public
explanation when appropriate; use context to select or adapt it; spend on fresh
work where it changes the answer. Reuse is not permission to copy another
person's private composition, and a cache hit is not evidence of usefulness.
Some answers should remain answer-only rather than becoming durable feed supply.

#### What should count as evidence

Continue the existing E/D/H/S comparisons—curiosity, practical adaptation,
sparse-context Home and social receiving—but now distinguish authored targets
from actual produced and received results. Use the same sources and current
constraints for strong alternatives. Assess full scrolls and continuations,
not merely isolated card screenshots or whether every schema field is filled.

Automated checks can catch repetition, missing grounding, stale conditions,
wrong subjects and unauthorized dependencies. Human evaluation must still ask
whether a result was worth receiving and how it compared with what the person
would otherwise do. Do not substitute dwell time for liking, a link tap for an
outing, or an LLM score for enjoyment. Nor should evaluation become a permanent
rating/reflection chore inside the consumer product.

**Decision to make:** adopt no new grammar. Clarify the editorial selection and
whole-experience quality bar in the existing Content/Home work, then inspect
actual output. If personal context repeatedly supplies only decorative callbacks,
improve or omit its influence rather than displaying more evidence of memory.

### 19.5 Market: existing intent before rich data; received value before acquisition

#### Research findings

Partiful's official help describes shareable invitations, phone-number RSVP
and lightweight event participation. It illustrates a recipient job that can
travel through existing social channels before deeper participation. It does
not mean all receiving is anonymous or frictionless, nor that Vesper should copy
automatic reminders or event-management scope.
[Why use Partiful?](https://help.partiful.com/en-us/articles/15525594-why-use-partiful).

RevenueCat's 2026 report finds stronger early monetization but weaker subscriber
retention for AI apps in its dataset. Annual-plan retention after 12 months was
21.1% for AI apps versus 30.7% for non-AI apps. These are observational benchmarks
from RevenueCat apps meeting inclusion thresholds, not a causal AI effect,
Vesper forecast or profit measure. Category and cohort composition matter.
The report's weekly-retention summaries conflict, so this synthesis does not
use those numbers.
[State of Subscription Apps 2026](https://www.revenuecat.com/state-of-subscription-apps).

Schmidt and Bijmolt's meta-analysis covered 77 consumer-goods studies and found
average hypothetical willingness to pay above real willingness to pay. Its
reported average bias of 21% is not a universal correction factor for an AI
subscription survey. The practical lesson is to distinguish stated enthusiasm
from a consequential buying choice.
[Willingness-to-pay meta-analysis](https://link.springer.com/article/10.1007/s11747-019-00666-6).

#### Recommendation for Vesper

The strongest initial audience hypothesis remains **intent-rich, not necessarily
data-rich**: people already asking questions, saving possibilities or sending
recommendations, when they want help understanding or using one. Someone with
one real question is more relevant to first value than someone who likes the
idea of an AI life companion but has no present reason to use it.

Recruit against recent behavior, not the founder's travel intensity, cultural
interests or willingness to document. Include people with little history, no
friends on Vesper and limited patience for planning. Also include people who
enjoy choosing and researching; less work should not mean removing the part
they like. NYC remains a candidate whose supply must be checked, not an adopted
market simply because the founder can recruit there.

Keep three independent entrances: bring a current thing/question, open Home for
worthwhile value, or receive something from a person. The same complete product
can explain itself differently at each entrance. Receiving an invitation or
note does not require committing to the whole app, and a sender's delight is
not evidence that their friend wants another social platform.

Distribution should follow the value's natural shape: an original contribution,
a useful explanation, an invitation or a contextual recommendation worth sending.
Preserve attribution, chosen audience and the original material. Then offer an
optional continuation with a clear personal benefit. Do not make account setup,
reciprocal contribution, public performance or recruiting friends the price of
understanding what was sent. The exact guest and identity mechanism remains a
separate policy/design decision, not an authorization for public links here.

Return has several legitimate cadences: a casual question, an open afternoon,
something unfolding, a friend's offer, or something entrusted that is needed
again. Ask whether Vesper is chosen when the situation recurs, rather than
manufacturing situations through daily prompts. A week without use can be
compatible with a good relationship; repeated opportunities lost to existing
apps despite access to Vesper are more informative.

For payment, retain membership as the leading hypothesis for repeated everyday
assistance and an episodic pass as an alternative if value clusters around
occasions. Do not implement both now. A membership may be justified by recurring
use or dependable availability, but availability must be real and bounded—not
an implied watch on everything in someone's life. People do not owe daily use
to justify the subscription.

The free experience should contain finished benefits and basic social
participation, while expensive depth/capacity can be limited intelligibly. Avoid
charging separately for each product move or making retained material,
correction and basic shared truth hostage to payment. Do not position “more
memory” as a sufficient paid benefit; charge for an actual improvement in help.

Model contribution at the whole service/cohort level: collected revenue after
platform fees and refunds, less variable inference/tool/data costs, acquisition
and refresh of world supply, delivery/storage, free-participant usage and support.
Include rejected generations, retries and abandoned research. Keep fixed
engineering and customer acquisition visible separately. Cheap final tokens or
high revenue per payer alone do not establish a viable business.

#### Recommended learning sequence, not another product restriction

First use a small, behaviorally selected qualitative group to check that people
understand the same honest offer and receive a complete supported result. A
practical initial proposal is 12–16 people across the entrances, including lightly
involved recipients; this is a founder-manageable exploratory sample, not a
powered experiment or a validated sample-size prescription.

Then observe voluntary access over several ordinary weeks, including weekends
and periods without pressing plans. Do not assign daily sessions or require a
diary. Optional follow-up interviews can reconstruct actual opportunities and
alternative-app choices. Any assisted/manual delivery must be labeled and its
labor counted; authored specimens must not be presented as runtime capability.

Finally, investigate paid packaging once the described service can actually be
provided. Price comparisons can reveal tradeoffs and objections, but only an
honest consequential purchase and later renewal can establish those behaviors.
No recruiting, charging, messaging or deployment is authorized by this research
note. This learning can accompany the whole-system roadmap; it does not require
freezing architecture around one observed loop.

**Decision to make:** choose an initial audience/offer experiment and a cost
envelope before a price. If travel produces stronger voluntary preference than
ordinary local use, reconsider acquisition emphasis without automatically
restoring the travel-only identity or booking infrastructure.

### 19.6 What this changes about our next work

The four areas reinforce each other, but must not become a circular promise:
we cannot require a rich history to supply value, daily engagement to build that
history, social density to make Home interesting, and payment to finance an
unproven bespoke feed. Each entrance needs a credible benefit on its own;
continuity and relationships can then compound it.

The opinionated sequence is:

1. **Settle the consequential service and continuity boundaries in their existing
   decision locations.** Write what is supported, what is not, what finishes,
   and what needs separate authority. Keep engineering progressing within the
   current contracts; do not activate proposals by implication.
2. **Complete and inspect the connected portfolio through existing owners.**
   Integration/Source owns exact request-to-result completion; Content owns
   substantive supply; Home/Places owns receiving composition; Life owns the
   retained-result/refinding seam; Social preserves original receiving and
   authorized optional help. These are dependencies, not a dispatch of new tasks.
3. **Learn from voluntary consumer choice as the supported experiences become
   available.** Comprehension, actual received quality, return opportunities,
   recipient value and payment are separate observations. Do not roll them into
   one engagement score or treat contract tests as market evidence.

| Observation that would challenge us | Strategic response |
| --- | --- |
| Good first value requires the founder's archive | Strengthen immediate and public-world value; do not demand more onboarding input |
| Long-range context creates stale assumptions or repetitive callbacks | Narrow/select its influence and repair dependencies; do not equate recall with success |
| A rich Home still feels like the same offer repeated | Recompose around different reasons to receive value, not more media or section labels |
| Users understand the breadth but must redo the work elsewhere | Fix exact subject/result and provider handoff completion before expanding the promise |
| Senders like sharing but recipients receive pressure or little benefit | Improve original receiving and optional continuation; do not add growth prompts |
| People like examples but do not choose Vesper when relevant situations recur | Revisit audience, comparative value and service quality before treating it as a notification problem |
| People pay once but costs or renewal fail | Revisit the service/allowance and membership-versus-episodic hypothesis; do not resurrect booking revenue by default |

**Overall judgment:** the strategy is coherent enough to support the system we
are building, but coherence is not yet evidence that people will prefer or pay
for it. The next advance is making its broad usefulness reliably receivable,
with selective continuity and boundaries a newcomer can understand. This round
adds research and recommendations only; it changes no canonical agreement,
application code, runtime flag, billing policy or release claim.
