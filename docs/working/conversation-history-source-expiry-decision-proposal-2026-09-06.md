---
doc_type: working
status: active
decision_status: proposed
owner: founder / Contribution and Capture / Integration
created: 2026-09-06
last_verified: 2026-09-07
expires: 2026-10-06
why_new: Resolves one review boundary for conversation history, transient source derivatives and optional later reuse without silently expanding the accepted Ask contract.
supersedes: []
---

# Decision proposal: conversation history, source expiry and optional continuity

## Status and recommendation

**Proposed, not adopted or implemented.** Creating this document does not
authorize new retention, retrospective reuse, deletion or a migration. The
[contribution contract](../systems/contribution-and-consequence.md) remains
authoritative: Ask creates no new durable personal state; raw Ask processing
sources expire after processing, with at most 24 hours of technical retry
custody; session working context expires after 24 hours of inactivity.

**Recommend separating three permissions:** conversation-history display,
source/derivative custody, and use in a later context. A record stored for one
does not acquire the other two. The September 7 revision recommends a
prospective opt-in for **selective long-range continuity**, with
no universal age cutoff while eligible history and its use grant remain valid.
This replaces the earlier 90-day recommendation, not any effective policy. It
remains
**unadopted**, not something enabled by continued use or inferred interest.
The existing implementation batch does not gain new retention authority.

[Section 8](#8-continuity-lifecycle-clarification-expiry-and-a-long-return)
makes the proposal reviewable across clarification, changed circumstances,
source expiry and a return months later. It separates readable history,
automatic reuse and present applicability; none receives a new grant here.
[Section 9](#9-four-month-return-a-proposed-history-agreement-and-complete-walkthrough)
preserves the earlier 90-day comparison, using a return with no manual Keep and
no intervening participation. [Section 10](#10-selective-long-range-continuity-four-complete-experiences)
is the latest recommendation: four written experiences, capable no-history
comparisons, and an existing-owner integration map. History duration and wider
automatic use remain proposals, not an effective account agreement.
[Section 4](#4-simple-controls-with-exact-consequences) now distinguishes
requested help, on-visit discovery, interruption and external consequence;
early mode explanation versus later opt-in; and resurfacing exclusion versus
use exclusion and off-with-clearing. Section 10 applies those refinements to
the same four experiences, including correction and a return months later.

This document supplies the missing CC-2 decision packet and refines Integration
D4's implementation dependency. D4's five-axis policy is settled; the treatment
of history copies and their derivatives still needs this explicit resolution.

## Proposed treatment by material

| Material | Proposed history/custody treatment | Later use and repair |
| --- | --- | --- |
| Person-authored text | Ordinary conversation history only under its actual explicit account/history policy; §9 proposes until-deletion text history, not an effective new duration | History storage is not automatic memory admission. Deletion and context exclusion remain effective; explicit historical lookup needs the separately described use scope |
| Independent assistant explanation | May remain readable under that same history policy if it does not reconstruct expired/released source content | History alone grants no Life indexing, preference synthesis or Home production; separately authorized use preserves AI authorship and world-source dependencies |
| Raw Ask attachment and processing copies | Transient, including copied Chat images, OCR/extracted text and transcripts when source-derived | Enforce processing-end/expiry at read and prompt assembly before eventual cleanup; retries never renew authority |
| Source-dependent generated answer | Dependency-aware treatment; no blanket exemption for prose | Redact/withhold source-dependent portions when eligibility ends; retain only independently supportable explanation and a minimal unavailable-source marker |
| Deliberately retained Bring/Keep original | Its own custody policy; history holds an authorized ref rather than an independent permanent copy | Source controls govern derivatives and eligible reuse; conversation deletion is not automatically deletion of an independently retained original |
| Human-authored claim independently retained under explicit authority | Its named owner and scope, distinct from the original attachment | Repair causal dependencies without deleting independent claims or widening purpose |
| Minimal tombstone/receipt | Content-free identity/status needed to explain unavailability and prevent replay | Cannot preserve enough text, embeddings or media to reconstruct released content |

Do not infer the gesture from MIME type or the presence of `chat_images`.
“What does this ticket say?” and “Keep this ticket” use different authority.
An authored message that deliberately contains quoted material requires its own
custody classification; do not blindly delete all user-authored text or retain
all copied source text under a history label.

An expired attachment should not make unrelated conversation vanish. Conversely,
keeping a generated transcription in history must not defeat source expiry.
Where existing storage cannot distinguish answer spans, withhold the whole
source-dependent answer from future model use and use a minimal display marker
until an approved representation can safely separate it. Do not run a model
over released material to reconstruct a replacement.

## Existing implementation gap

[`chat_images.py`](../../travel-agent/backend/core/db/chat_images.py) stores
images for conversation use and now cleans up files on row-write failure.
Its [model](../../travel-agent/backend/core/models/chat_images.py) has no
explicit custody-purpose or expiry field. Transactional cleanup is therefore
not complete lifecycle enforcement. The [CC execution receipt](contribution-contract-and-legacy-memory-migration-plan-2026-08-29.md#116-execution-receipt--september-5)
also records intake deadline preservation and useful-first facts, not a fully
implemented history/source distinction.

Implementation must inventory every copy and consumer: original, thumbnail,
extracted text, transcript, message metadata, summaries, caches, pending jobs,
generated results and future prompt assembly. Reuse existing source identity and
policy fields where possible; do not introduce a second source-custody owner.

## Optional continuity: policy not adopted

The [September 6 strategy decision](../decisions/2026-09-06-reconcile-consumer-strategy.md)
accepts optional ordinary-conversation continuity as intended product behavior,
not this proposal's material, duration, migration or source-expiry choices.
Manual Keep should not be the only eventual continuity path. Current Ask/T0
rules remain in force until a separate policy amendment is accepted.

Evaluate history readability explicitly: independent explanations should remain
available where permitted; source-dependent answers must not reconstruct
released material; unrelated conversation should not disappear. User testing
must include returning to an answer after attachment expiry, not only whether
a source can enter a future prompt. None of this authorizes new custody or
retroactive reuse.

Ordinary questions must still be useful on their own. Already authorized
context may improve an answer within its scope. Neither requires retaining
every new question or turning a topic into a person claim.

A future opt-in must explicitly settle all of the following before adoption:

- What is retained and for how long; whether selection is prospective only.
- Which later answers, Home/Places contributions or retrieval may use it.
- Sensitive and third-party exclusions, inference limits and subject scope.
- Inspection, correction, exclusion, opt-out and deletion behavior.
- Treatment of previously produced derivatives and running jobs on revocation.
- A comprehensible agreement without per-question memory-management homework.

Do not preselect an opt-in, backfill from historical Chat, equate enabling
history with continuity, or broaden audience/action permissions. The September 7
extension proposes history duration and selective later use for review; it does
not establish an effective retention period or deploy a continuity preference.

## Delivery ownership after adoption

| Lane | Responsibility |
| --- | --- |
| Contribution and Capture | Lifecycle classification, copy inventory, read rejection, prompt-use filtering, cleanup and exact receipts |
| Integration | Shared dependency events, late-production suppression and cross-consumer verification |
| Life | Only eligible retained sources/claims; withdrawal in index and exact readers; no ambient history scan |
| Home / Places / Entities | Revalidate source-dependent results and cached material; preserve independent owner truth |
| Strategy / founder | Approve the policy and any later continuity agreement; do not mark implementation shipped |

Recommended execution: define the minimal lifecycle binding; implement request-
time denial and worker revalidation; then bounded cleanup with audit and retry.
Do not start by deleting historical files. Existing rows with unknown authority
need a non-destructive classification/inventory and a separately reviewed
migration. Unknown reuse eligibility must not silently become a grant.

Verify Ask/Bring differences, processing completion, expiry, retries, revocation
mid-job, no reconstruction from derivatives, exact source deletion versus
conversation deletion, preserved independent history and account isolation.
No UI redesign, native test session or production cleanup is authorized here.

## Approval and tradeoff

Approve or revise the material-by-material policy before implementing CC-2's
history-specific migration. The recommended separation preserves useful history
without turning it into hidden long-term memory; dependency-aware answer repair
is extra implementation work, not a promise the current model already fulfills.
On approval, publish an accepted decision and update the owning contribution
contract. Until then, this remains one bounded proposal, not a new roadmap.

## September 7 recommendation: remember the exploration, not a verdict on the person

This extension responds to the [newcomer encounter's unresolved memory
promise](nyc-newcomer-connected-home-specimen-2026-09-07.md#94-two-strategic-limits-remain-visible).
It recommends actual product behavior rather than another open-ended list of
research questions. **Every new permission and duration below is proposed.**
The earlier material treatment, current Ask contract and existing grants retain
their authority until an explicit amendment is accepted and implemented.

### 1. The experience to aim for

An ordinary question should help now. Under the optional agreement, later help
can build on what was discussed without the person organizing it first.

The retained basis is something like **“we explored this question, with these
stated circumstances and this provisional explanation”**, not “this is the kind
of person you are.” These are conceptual distinctions, not new app objects.

Useful continuity can produce:

- a better answer that skips already-established setup;
- a new explanation that builds on a distinction previously discussed;
- a worthwhile Home contribution that develops an exploration rather than
  paraphrasing it;
- a Places comparison informed by relevant, still-applicable context; or
- retrieval of an eligible earlier exchange when the person asks for it.

It need not produce an artifact, permanent preference, generated article, plan,
push or action. It need not make the earlier conversation visible every time.
The person should feel less need to start over, not more need to maintain a
memory collection.

### 2. Recommended agreement and defaults

| Decision | Recommended product behavior | Reason and cost |
| --- | --- | --- |
| Entry | Explain the actual default before contribution without blocking the first answer; offer one affirmative, prospective opt-in after value or in settings | Early understanding is not compulsory early configuration. Avoid hidden reuse, per-question Save chores and repeated opt-in solicitation after refusal. |
| Material | Eligible non-sensitive text from new private conversations, including enough surrounding context to preserve subject, purpose, uncertainty and authorship; independently supportable assistant explanations remain attributed | A bag of extracted facts loses why the person asked. Retain only what can be grounded and inspected; model summaries never become independent evidence. |
| Source custody | Attachment, OCR, copied document and transcript material retain their own existing custody rules | A continuity toggle must not silently make every supporting image permanent. A source-dependent answer cannot become a retained proxy for an expired attachment. |
| History duration | Eligible private text remains available until conversation/account deletion under the proposed history agreement, subject to disclosed service/account-closure and deletion handling | No automatic age expiry or unannounced inactivity purge; not eternal storage. Source-dependent material keeps its own earlier lifecycle. |
| Automatic-use duration | No universal age cutoff for contributions originally admitted under this prospective long-range agreement; eligibility ends on source/history loss, exclusion, grant withdrawal or a narrower purpose limit | Older context is selectively retrieved, not present in every prompt. Readable history alone grants no automatic use. The earlier 90-day option remains a comparison in §9, not the latest recommendation. |
| Later private use | Eligible retrieval and adaptation in Chat, Home and Places, all named in the agreement; distinguish requested assistance from on-visit discovery and honor narrower resurfacing/use exclusions | This is the intended cross-root value, not merely transcript search or a separate permission per tab. Personal context must materially help the selected contribution. |
| Automatic inference | Preserve an inquiry as inquiry, an authored circumstance as scoped evidence, and an AI explanation as explanation | No automatic permanent preference, personality, inferred emotion, attendance, shared intent or relationship profile. Repetition is not authority. |
| Sensitive and other-person material | Exclude from automatic continuity admission by default; keep only non-sensitive scope markers needed to avoid misattribution, such as “asked for someone else” | Do not create a sensitive-person dossier or carry another person's private details into unrelated help. Explicit protected constraints and governed shared sources remain separate owner paths. |
| Initiative | Continuity can affect a private on-visit contribution without granting interruption, monitoring, sharing or execution | A remembered question is not an accepted task. Existing production-trigger and budget rules still govern preparation. |
| Life | No automatic Life entry for every eligible question; retain existing contextual inspection and conversation access | Life should organize deliberately retained material and lived records, not become a transcript-cleanup queue. |
| Old history | No backfill. Enabling applies only to eligible subsequent contributions | A newly enabled feature cannot reinterpret the basis on which old questions were asked. |

The sensitive exclusion includes health, intimate matters, protected identity,
precise location history, credentials, financial account details and confidential
third-party/work material. A topic classifier is not sufficient authority: when
scope or eligibility is unclear, omit the uncertain material from later use.
Mixed conversations require bounded admissible context; if separating it would
lose meaning or preserve excluded content indirectly, do not admit that unit.
Immediate assistance remains available within its current authority.

**Revised recommendation:** age should affect interpretation and retrieval
selection, not automatically decide whether an exploration can ever help again.
Section 10 tests that choice against the earlier 90-day option and capable
no-history help. This is a broader permission requiring explicit adoption, not a
technical change to a cache window. No research here establishes a preferred
number of days or validates lifelong automatic personalization.

Retention, authorized use and present applicability remain separate. “Tonight”
stops applying tonight even if its historical text remains eligible. Reopening
Chat, viewing Home, retrieval or summarization cannot renew an expired source,
widen a grant or turn a past circumstance into a current fact. A new authored
clarification has its own contribution time and repair effect; copying an old
passage into generated prose cannot give that passage new authority.

Explicit user-directed lookup remains separately available under its actual
history agreement when automatic continuity is off. Neither opening history
nor switching on the proposed longer-range option admits older ineligible chats
or upgrades material collected under a shorter agreement. Existing exclusions
and any actual shorter grants remain effective unless separately changed by the
person; this proposal authorizes no backfill or upgrade flow.

This adds a proposed narrow agreement above Ask's default; it does not relabel
all Ask turns as Bring. Only the material and uses the future agreement
actually covers may receive the exception. No new database schema or writer
is selected by this table.

### 3. What should actually improve tomorrow?

These are synthetic behavioral comparisons, not reports of user outcomes or
claims that particular generated content has passed factual review. World
facts still need current sources; personal context does not supply them.

| Earlier interaction | Later encounter | Worthwhile continuity | Unwanted shortcut |
| --- | --- | --- | --- |
| “Why does restaurant pasta sauce cling differently? I only have one pan at home.” | Tomorrow: “Could I try that with what I have?” | Recover the specific explanation and stated equipment; prepare an applicable method without asking the person to reconstruct the earlier question | “You love Italian cooking,” or a Home reminder to finish a cooking project that never existed |
| Same cooking exploration | Day 5: eligible Home supply contains a substantive, source-backed comparison of two ways to finish a sauce | Use the earlier question to choose a useful comparison, expose the actual difference, and leave further action optional | A recap of the question, an invented recipe, or daily pasta content justified by one exchange |
| An answer explains why a Place's apparent distance can mislead about access | Day 2: “Actually, the problem on that trip was the lift closing before we returned, not the distance.” | Treat the clarification as the person's account and revise the earlier interpretation; don't keep both as equally valid explanations | Treating the model's old theory as the person's own memory |
| That access discussion is eligible | Day 5: the person explicitly asks for step-free access for an evening visit and supplies a new venue's hours | Attend to entrance identity and time, using the new facts; reduce re-explanation without transferring old opening hours | Inferring a permanent mobility constraint, or claiming memory was necessary when the new note already supplied the whole answer |
| A restaurant question was for someone else | Later: the person asks for their own dinner options | Preserve the subject distinction and leave irrelevant prior constraints out | Recommending around the other person's diet or budget as though it belongs to the user |
| “Keep this library,” followed by an eligible ordinary question about its terrace | Later: reopening the exact saved Place | Use the save owner for durable refinding and recent discussion only for justified extra context; avoid repeating an explanation as a new discovery | Treating the question as a visit, or deleting the independent bookmark when the conversation is excluded |
| “Keep it brief for this answer.” | A new question tomorrow asks for depth | Follow the new request; the earlier response-only instruction does not survive as an ongoing style rule | A global brevity preference inferred from one correction |

The day-1/day-2/day-5 pattern does not depend on remaining in the same chat.
Within the proposed agreement, an eligible clarification can update the
understanding of an earlier subject across conversations. Without that
agreement or another existing grant, reuse remains bounded by current Ask/
session rules. Neither a thread ID nor an old message visible in a client is
authority by itself.

Do not require Home to demonstrate a callback after every useful conversation.
Sometimes the best result is a better next answer; sometimes old context should
change nothing. Relevance to the current job matters more than conspicuous
recognition. The prior [delayed-evidence case](situated-value-decision-matrix-2026-09-06.md#64-day-1--day-2--day-5-delayed-explanation-and-new-application)
already covers separately retained evidence; the table above adds the
agreement-dependent conversational branch without replacing it.

### 4. Simple controls with exact consequences

**Latest control recommendation, September 7; still proposed.** Preserve a
simple experience, not a single ambiguous effect. The distinctions below are
requirements on existing authority, settings and repair paths—not a new product
grammar, a memory-management page or four onboarding toggles.

#### 4.1 Separate the use and consequence, not the tabs

| Situation | Intended experience under actual authority | Boundary that remains separate |
| --- | --- | --- |
| Requested assistance | Answer the current question, including an explicitly requested recommendation, using only eligible context that helps | Asking a fresh question does not itself authorize an archive scan, override an existing use exclusion or enroll the answer's sources for future use |
| On-visit discovery | Opening Home or browsing Places invites worthwhile supplied value; an adopted continuity agreement can improve selection without a fresh question | A visit is not a new retention grant, permission for arbitrary personal inference, a production mandate, or authority to bypass a topic/surface exclusion |
| Interruption | Deliver only within the actual notification authority and a justified interruption moment | A useful Home explanation or remembered interest is not permission to push it; no curiosity notification follows by default |
| External or shared consequence | Prepare or execute only the exact effect permitted through its owner and current authority | Continuity never supplies audience, RSVP, spend, provider, publication or monitoring authority; an already authorized command need not acquire a redundant confirmation |

Chat can contain unrequested suggestions; Home can show the result of explicitly
requested work. Therefore, do not implement this distinction as Chat-versus-Home
permissions. The same purpose and exclusion must survive an exact continuation
across roots. A Home-only presentation request remains Home-only; a broad use
restriction must not be bypassed by moving the result to another root.

This follows the existing [initiative separation](vesper-useful-preparation-and-initiative-research-2026-09-06.md#1-answer-and-scope),
not a new autonomy system. Production, eligibility to serve, interruption and
owner execution remain separate. Home still offers substantial reading,
possibilities and human contributions; this does not require an urgent event,
a question before every card or a deliberately sparse page.

#### 4.2 Explain the default early; offer configuration after value

Proposed agreement copy for comprehension review, **not shipping copy**:

> **Let past chats improve future help**
>
> From now on, Vesper can use eligible, non-sensitive text from your new private
> chats to improve later answers and what appears in Home and Places—even
> months or years later, while the history is kept and you allow this use.
> This doesn't keep attachments or create reminders, plans or shares.
>
> You can exclude a conversation or turn this off anytime.

The first layer must name Home/Places and the duration; do not hide the
surprising use in policy detail. The accompanying detail explains material,
exclusions, earlier expiry, history-versus-continuity and repair. This is not
a replacement for a complete privacy/data agreement or an assertion that
current engineering can honor the copy.

Before the first contribution, make the actual default discoverable without a
blocking modal or setup questionnaire. If the proposed feature is implemented
and currently off, a compact explanation such as **“Past-chat personalization
is off”** can expose its meaning and the separate history treatment. That wording
does not mean history is absent, attachments are kept, or all memory/standing
constraints are disabled. Never display a control or promise the runtime cannot
honor; current Ask and source-expiry rules still apply until adoption.

Offer the affirmative choice after useful assistance or through settings, before
any admission under the broader agreement. Neither choice is selected by default.
Enabling after a useful first answer covers eligible subsequent contributions;
it does not silently backfill that first exchange. A deliberate Keep remains a
separate owner gesture, not a prerequisite or a required follow-up prompt.

Once enabled, no per-question acknowledgment, approval queue or repeated notice
for already-covered ordinary uses is needed. Keep mode and contextual controls
discoverable; show exact material boundaries when they arise. Declining must not
lead to repeated solicitation, inferior first answers or an empty Home. Early
explanation and later optional configuration are different moments; comprehension
review must check both, not assume just-in-time consent is always preferable.

#### 4.3 Resolve ordinary language to the intended effect

| User expression/control | Proposed effect |
| --- | --- |
| “Just for this conversation” / exclude this chat | No new continuity admission here; stop later use of this conversation's continuity material and invalidate its dependent uses. History remains under its separate policy. |
| “Stop showing me cooking stuff on Home” | Suppress the resolved cooking-topic presentation on Home, including pending Home delivery. This does not erase cooking history, assert dislike, or prevent cooking help the person requests in Chat. Other uses retain only their actual existing authority; do not relocate a Home card merely to defeat the request. |
| “Don't bring this up” | Stop unrequested resurfacing of the identified material within the resolved scope, including its dependent suggestions. Preserve custody and separately allowed requested assistance; do not silently reinterpret an explicit broader use ban as this narrower treatment. |
| “Don't use this to suggest things” | Stop recommendation use from the identified material in Home, Places and Chat, while leaving separately authorized historical lookup available. Report the actual scope, not a global reset or an exception allowing recommendations in another root. |
| “Don't use this again” | Stop the identified material's future influence across the resolved consumers, not merely its visible mention. A generic later question does not lift the exclusion; any requested change to that restriction must be clear and separately resolved. Custody is not deleted by implication. |
| “That was for my parents” | Correct the subject of the specified evidence and repair dependent uses. Do not create a new permanent profile of the parents. |
| Turn continuity off, with clearing explained | Immediately stop using and admitting material under this agreement; suppress pending dependent delivery; clear its derived continuity representations through bounded cleanup. Eligible history remains under its separate policy. Re-enabling starts prospectively, not by silently rebuilding from old chats. |
| Delete this conversation | Remove its history under the history policy and remove dependent continuity; independently kept Sources remain separately owned and visibly identified, not silently deleted or reused as a loophole |
| “Forget this,” with the continuity target clear | Stop that material's continuity influence and clear its derived continuity representations through repair. State whether the original conversation or independently kept item remains; if deleting an original is clearly the requested job, use its actual owner rather than treating influence removal as complete deletion. |
| “Forget that” with an unclear referent | Stop the identifiable future influence first where safely resolvable; clarify only the destructive or materially ambiguous scope. Do not pretend a vague request deleted every related source. |

An explicitly broad recommendation-use ban covers requested recommendations too;
the separate historical-lookup exception is not permission to build a new
recommendation from excluded material. A narrow “not on Home” request does not
carry that broader effect. Resolve the target, purpose, consumer and any stated
duration from the actual instruction; do not require the person to learn those
internal terms. Do not invent a temporary expiry that makes “stop showing” wear
off, or make “not this weekend” permanent. Use existing scope/repair owners and
clarify only when the ambiguity changes a material effect.

#### 4.4 Recommend off-with-clearing, not an ambiguous pause

For the initial proposed agreement, retain **one global off operation with its
clearing consequence explained**. Do not add a separate prominent pause control
solely because the internal effects differ. Adjacent consequence copy must say
that Vesper stops using these chats, clears the continuity derived from them,
keeps separately eligible history, and starts only with new eligible contributions
if re-enabled. This is a product recommendation, not a research-established
preference or an implemented setting.

A true pause would instead suspend admission and use while retaining previously
authorized material under its unchanged retention limits. If offered later, it
needs an explicit resumption rule: no automatic restart, no admission of chats
from the paused interval, no renewal of expired grants, and revalidation of
surviving eligibility and applicability. It must not silently clear memory or
promise indefinite retention. That additional mode is **not selected for this
initial proposal**. “Pause for now” must not silently invoke the destructive
clearing operation: explain the available effect and resolve the choice before
clearing; do not claim a pause that does not exist.

Off or scoped exclusion must deny the affected use before eventual cleanup,
including pending production and cached results; hiding a card is insufficient.
An independently kept ticket, protected constraint or accepted responsibility
does not disappear merely because chat continuity stops. Reassess any work that
depends on withdrawn context, suppress invalid dependent results, and communicate
a material loss of promised service where necessary. Do not claim all watches
stopped or keep excluded context through another owner as a workaround.

“Why this?” should expose the relevant conversation and the specific basis
that changed the result, with correction/exclusion in context. It should not
display a personality inventory or narrate every retrieval. If admission or
repair fails, state the actual limitation rather than saying “remembered” or
“forgotten everywhere.” Technical deletion timing and any required residual
records must be settled and disclosed before release; this proposal does not
promise instantaneous physical erasure of every backup.

### 5. Research and what it does not settle

Sources rechecked September 7, 2026:

- [Jones et al., CHI EA 2025](https://brennanjones.com/media/documents/publications/chiea25-666.pdf):
  six interviews and a preliminary analysis of 54 Reddit threads found
  incomplete understanding of memory selection/use and differing needs by
  task and time. This supports testing scope and consequences, not assuming a
  universal appetite for either total memory or total separation. The small,
  experienced interview sample does not establish population preferences.
- [Zhang et al., 2025 preprint](https://arxiv.org/abs/2508.07664):
  interviews with 18 users describe both perceived usefulness and concerns
  about control, accuracy and inference. Treat this as qualitative evidence
  for understandable controls, not proof that a larger settings screen earns
  trust or that an opt-in alone resolves discomfort.
- [Huang et al., ACL 2026](https://aclanthology.org/2026.acl-long.670/):
  technical research examines excessive historical anchoring versus excluding
  useful history and proposes controllable reliance. Our implication is to
  test changed purpose and useful non-use. It does not establish that consumers
  want a memory-strength slider; do not add one by analogy.
- [Claude's current documentation](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)
  describes automatic memory, separate chat search, project scope, controls,
  sensitive-topic opt-in and past-chat citations. It also says generated memory
  can survive deletion/expiry of its originating conversation. This is
  documented product behavior, not proof of usefulness. Vesper's proposed
  source-dependent repair intentionally should not copy that survival rule.
- [Liu et al., CHI 2026, *Designing Privacy Choice in Generative AI Chatbot Ecosystems*](https://doi.org/10.1145/3772318.3790809):
  author abstract and publisher-indexed methods/results excerpts reviewed;
  the full PDF was unavailable. Two vignette surveys involved 486 participants,
  followed by 16 interviews. Setup-time choices often supported greater
  perceived control; some participants found just-in-time prompts belated or
  disruptive. In the personalization survey, timing did not significantly
  change trust or willingness to continue. Do not turn the discussion's broader
  claims into a universal causal rule. Our inference is to explain the default
  early without forcing configuration before help; the study does not validate
  Vesper's particular opt-in timing or copy.
- [Huang et al., 2026, *Remembering or monitoring?*](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1934857/abstract):
  accepted August 28; only the accepted abstract was available at review. Six
  experiments with 2,140 participants used fictitious memory references rather
  than actual longitudinal retrieval. Relevant cue packages generally performed
  better than intrusive ones on trust-related outcomes; comparisons with no
  memory varied. An editable dashboard raised average trust without selectively
  removing the intrusive-cue penalty. Bundled differences in relevance,
  sensitivity, source and implied surveillance prevent isolating one mechanism.
  Treat this as limited support for judging whether a use is welcome, not proof
  that a particular control design fixes intrusion or that personalization wins.
- [Mireshghallah et al., 2025 preprint, *CIMemories*](https://arxiv.org/abs/2511.14937):
  the abstract reports a synthetic-profile benchmark of inappropriate
  cross-context information flow and limitations of privacy-conscious prompting.
  It is not a consumer study or a real-world leakage estimate. Our architectural
  inference is to bind use eligibility and purpose to retrieval and repair through
  existing owners, not append a whole profile and rely on an instruction to be
  appropriate. It does not establish which retention or pause policy people want.

**Synthesis:** automatic acquisition, understandable scope, useful application
and causal repair can coexist. These sources do not select 90 days, prove
Vesper's differentiation, measure its retention, or certify a privacy guarantee.
The retention/use duration and private Home/Places inclusion are explicit product
recommendations that still need review. Section 10 adds the longer-range research
and distinguishes measured findings from the revised product judgment.
Section 4's control refinements apply that evidence without promising that an
opt-in or dashboard makes every use welcome. No reviewed study establishes an
optimal pause/restart policy. Keep §8's already-documented human-versus-AI
authorship boundary; richer interpretation must not become attributed user fact.

### 6. Approval boundary and engineering handoff

This packet now offers a decision-ready recommendation for material, duration,
use, inference, controls and low-effort participation. It is not an accepted
decision or permission to enable memory. Founder review should focus on these
consequential choices rather than reopening the whole product philosophy:

1. Does the same clearly explained opt-in cover private Home/Places use as well
   as later answers? Recommendation: yes, with the requested/on-visit distinction
   and scoped resurfacing/use exclusions in §4. Neither interruption nor external
   consequence is bundled into that choice.
2. Can eligible conversations contribute automatically beyond 90 days?
   Recommendation: yes, selectively under the proposed prospective agreement,
   without a universal age ceiling. Compare §10's complete experiences with the
   earlier §9 option; no existing grant changes merely because this is preferred.
3. Are automatic exclusions and dependency-aware deletion the right default?
   Recommendation: yes; scoped protected constraints retain their own paths.
4. What remains when automatic use is unavailable? Recommend eligible text
   history until conversation/account deletion and bounded user-directed lookup
   under the separate history agreement. History-only remains a complete option;
   no-history assistance remains useful. §9 illustrates the earlier age-limited
   variant; §10 specifies the revised long-range recommendation.
5. When is the default explained, and when is continuity enabled? Recommend
   compact mode/history clarity before contribution, then an optional affirmative
   choice after value or in settings before any broader admission. No backfill,
   blocking questionnaire or per-use approval queue follows.
6. What does off do? Recommend the existing stop-and-clear effect, now disclosed
   explicitly, with separately eligible history preserved and re-enabling
   prospective only. Do not add a true pause mode yet or label clearing as pause.
   Keep source/topic resurfacing controls distinct from a broader use ban.

After policy adoption, Contribution resolves the agreement and per-material
authority; existing conversation/Source owners retain eligible evidence;
governed context/memory compiles bounded later use; roots consume it. Integration
must name the exact writer/readers and smallest missing extensions before
implementation. Do not route questions through the legacy personality-observation
writer or introduce a new universal memory store to bypass that review.

Required acceptance includes: off versus on with the same immediate answer;
same and different conversation after inactivity; a later authored correction;
irrelevant history correctly ignored; third-party/sensitive and expired-source
exclusion; Home-only suppression with requested help intact; a broad
recommendation-use ban respected even in a requested recommendation; historical
lookup only where its use remains permitted; off-and-clear during production;
no destructive interpretation of an ambiguous pause; deletion of the source
conversation; no silent renewal or backfill on re-enable; account switching;
and a return months or years later. Evaluate
the actual benefit over an accurate callback and over no history. The existing
system portfolio remains broader than these continuity cases.

No contract, schema, runtime flag, historical migration, production job or app
surface changes are authorized by this documentation update.

### 7. When remembered context earns influence

**Recommendation: remembered context is candidate evidence, not an instruction
to personalize. It earns influence by improving the help, not merely matching
the topic.** This section pressure-tests the proposed agreement above; it does
not adopt that agreement or expand existing grants. Existing eligible
kept material can support analogous comparisons under its own authority.

#### Judge permission, contribution and expression separately

Start with the current job and the actual evidence. Before using earlier
material, ask:

1. **May this evidence be used here?** Resolve material, subject, audience,
   retention and use scope through existing owners. Private recall permission
   cannot authorize a shared explanation, an interruption or an action.
2. **What does it still support?** Preserve authored fact versus AI explanation,
   uncertainty, the original circumstances and subsequent corrections. A valid
   retained sentence can describe a circumstance that has already ended.
3. **What improves because of it?** Less re-explanation, more appropriate depth,
   a better-fitted method, a substantive connection, useful retrieval or a more
   dependable practical judgment can each qualify. A familiar name in otherwise
   unchanged prose does not. Corroboration can improve confidence even when the
   visible result remains the same; do not require novelty for every use.
4. **Does that benefit belong in this moment?** Compare with a strong answer
   without history and, on a feed, with the other available contributions.
   Earlier curiosity should not displace today's explicit request or monopolize
   the page. An exploratory offer need not predict the person's taste.
5. **How much explanation does the person need?** Let ordinary fit do the work;
   expose a premise when it matters for judging or correcting the result. Ask
   only when an unresolved detail materially changes the help and bounded
   alternatives are insufficient.

These are review questions inside the existing situated-value sequence, not
a new scoring service, memory-strength setting or universal model gate.
Protected constraints and accepted responsibilities retain their actual
authority; they are not optional relevance weights. A current request can
supersede a contextual suggestion without silently erasing a standing constraint
whose owner requires a separate correction.

#### Different surfaces, the same evidence discipline

| Surface | What prior context should improve | What does not earn its place |
| --- | --- | --- |
| Chat | Resolve a referent, resume an explanation, avoid setup, adapt useful detail to the current question | A biography preamble; dragging the answer back to an old topic; treating a prior short-answer request as a permanent style rule |
| Home | Deliver something worthwhile now: a developed explanation, feasible possibility, useful preparation, human contribution or timely entrusted item | A callback standing in for substance; a generated article per remembered question; asking the person to document more before receiving value |
| Places | Improve the spatial question, comparison or optional exploration using applicable evidence | Silently filtering the world down to inferred interests; converting a saved place into proof of attendance or preference |
| Life | Refind and inspect material that its actual owner retained, with useful connections and accurate provenance | Automatically turning every remembered exchange or generated interpretation into another object to organize |

Home's higher bar is **standalone contribution and composition**, not mandatory
urgency. A new explanation of an old observation can be worth reading without
a new event. An ordinary friend photograph can be worthwhile without an AI
interpretation. A new world possibility can deserve space without a personal
history match. The whole page should offer breadth; these are not fixed slots
or a requirement to make Home sparse when nothing is pressing.

Do not equate relevance with literal topic repetition. An earlier observation
can provide a useful starting point for a different domain, provided the new
connection is supported and adds substance. It should explain something about
the world, not diagnose what the observation says about the person.

#### Matched situations: use, explain, clarify or leave out

The following are synthetic design expectations, not measured outcomes. Assume
the earlier non-sensitive text is eligible under an adopted agreement; without
that agreement, use only material already authorized by current contracts.

Shared starting evidence: on day 1 the person asks why restaurant pasta sauce
clings differently and says they have one pan available **in that kitchen**.
Vesper gives a grounded explanation. No cooking project, standing equipment
profile or preference is created.

| Later situation | Recommended contribution | Influence boundary |
| --- | --- | --- |
| Day 2, same discussion: “Can I try that with what I have?” | Resolve “that” and give a workable method for the stated setup; briefly identify the one-pan premise if needed | Avoid repeating the equipment question when the referent and circumstances are clear; do not imply that a permanent kitchen profile exists |
| Day 2, “I'm cooking at a friend's place with two pans” | Use the current setup and carry forward only the relevant explanation | The new circumstances supersede the earlier equipment limit; continuity should remove friction, not preserve obsolete constraints |
| Day 5 Home, a supported comparison adds a genuinely useful distinction between two finishing methods | Show the distinction and its practical effect, complete on view, with optional depth | “You asked about pasta” is not the content. No required recipe save, cooking plan, reflection or generated long-form treatment |
| Same Home visit, another eligible contribution offers stronger timely value | Let that contribution lead; the cooking comparison may remain lower or wait | A recent question creates neither a crown entitlement nor an obligation to fill the page with its topic |
| Day 5 Chat: “Somewhere nearby to eat tonight” | Answer the present dining question using current location or a necessary narrow clarification | Leave the one-pan fact out. Asking how a sauce works does not establish a restaurant preference or dietary constraint |
| Day 5, “Could this work with what I have?” in a different conversation, with multiple plausible referents or kitchens | Ask the smallest useful clarification, or present a clearly bounded option | Do not silently choose a kitchen from old context merely to appear seamless |
| A friend shares an eligible photograph of a meal | Deliver the friend's actual contribution with attribution; enrich only if it adds value for the receiving person | Private cooking questions do not become shared commentary. The photograph can succeed without enrichment or reciprocal contribution |

Use the existing day-1/day-2/day-5 access example in
[the situated matrix §6.4](situated-value-decision-matrix-2026-09-06.md)
for a second mechanism: a later authored explanation can correct why an earlier
situation was difficult. Reuse the corrected explanation where relevant, not
the obsolete AI theory alongside it. When day-5 facts already establish the
practical problem, credit continuity for reducing setup or improving attention
to the mechanism—not for discovering something the new evidence says outright.

#### Quiet help must remain correctable

Follow [Graph Legibility](../systems/graph-legibility-doctrine.md): fit may be
quiet; consequential assumptions and actual changes may not be hidden. These
are contextual response choices, not four new user-facing modes:

- **Use quietly** when eligible context removes repetition without a material
  uncertain premise. No recurring memory announcement is needed.
- **Show the specific basis** when it helps the person judge or correct the
  result: “This uses the one-pan setup you mentioned,” not “You prefer simplicity.”
- **Clarify narrowly** when choosing among plausible contexts changes the
  result materially. Do not turn uncertainty into a preference questionnaire.
- **Leave it out** when irrelevant, superseded, outside scope or too uncertain.
  Non-use is successful assistance, not a failure of personalization.

The receiving implementation must preserve enough dependency information to
identify the source, its actual effect and the consumers needing repair. This
is a requirement on existing owner paths, not a new user-facing receipt for
every answer or a separate memory database. Corrections must propagate through
the affected uses; dismissing one card alone does not accomplish that repair.

Nonresponse is not a new preference. Not opening a cooking card does not mean
“dislikes cooking”; passive dwell is not authority to strengthen an interest.
Avoid repeating already-delivered value without interpreting silence as a
verdict about the person. Delivery bookkeeping and personal inference are
different things.

#### Evidence and acceptance

[Microsoft's Human–AI Interaction guidelines](https://www.microsoft.com/en-us/research/articles/guidelines-for-human-ai-interaction-eighteen-best-practices-for-human-centered-ai-design/)
support contextual relevance, appropriate timing, efficient correction and
cautious adaptation. They do not determine which Vesper contribution deserves
Home prominence. The [ACL 2026 memory research](https://aclanthology.org/2026.acl-long.670/)
discussed above identifies the technical problem of excessive historical
anchoring; it does not establish consumer demand for manual memory weighting.
Our synthesis is to evaluate **selective influence**, not expose another control
the person must tune. Both sources rechecked September 7, 2026.

For each fixture, compare a strong no-history response, an accurate callback
and a materially adapted response. Separately compare equal-information quality
and the effort of assembling that information. Include wrong, superseded,
excluded and irrelevant history—not just the impressive successful callback.
Record what changed, whether it helped, whether uncertainty remained legible
and how much correction or re-entry the person needed. Review complete Home
compositions for repetition and breadth as well as individual units. These are
proposed acceptance criteria, not measured gains or a claim that competitors
cannot deliver the same answer.

**The intended experience:** “I don't have to start over, and something useful
can come from what I brought”—without “everything I ask becomes who the app
thinks I am.”

### 8. Continuity lifecycle: clarification, expiry and a long return

**September 7 research-backed recommendation; policy remains proposed.** Preserve
how understanding developed, not just the last compact summary or the first
extracted fact. This extends §§2–7 and the existing source/claim/interpretation
chain; it does not select a new memory store, inference writer or history policy.

#### Three time questions, not one memory clock

| Question | What determines the answer | What must not follow automatically |
| --- | --- | --- |
| Can I revisit the exchange? | The actual conversation-history agreement, plus source-dependent display eligibility | Readable history is not permission to use the exchange in later recommendations. Section 9 proposes until-deletion text history; adoption remains unresolved. |
| May Vesper reuse it automatically? | A separately adopted continuity agreement, material exclusions and still-valid use scope; §10 recommends no universal age cutoff | Opening, retrieving, summarizing or copying material does not renew an expired grant or admit old history. |
| Does it still apply here? | Subject, purpose, circumstances, event time, uncertainty and subsequent evidence | A sentence within its retention window is not necessarily a current fact, preference or instruction. |

The latest recommendation removes a universal 90-day cutoff, not source expiry,
purpose limits or the distinction between past and current facts. Section 9
preserves the age-limited comparison. Kept Sources and standing instructions use
their own owners and agreements. A temporary contextual override does not
silently delete a protected standing constraint.

#### One lifecycle, with independent branches

The cases below are synthetic design expectations. The conversational-continuity
branch assumes a future adopted opt-in; without it, current Ask/session limits
and separately authorized retained material remain the only bases for reuse.
An old client transcript or a familiar thread ID is not an additional grant.

| Event | Desired experience and evidence treatment | Receiving check |
| --- | --- | --- |
| Day 1: an observation and a question | Help immediately. If later admission is authorized, preserve what the person actually supplied, what they asked and what Vesper provisionally explained. | A question is not a belief; the model's explanation is not the person's account or an independently established world fact. |
| Day 2: “That wasn't the issue; the lift had closed” | Reconcile the explanation of the earlier event. Keep the authored correction distinguishable from the obsolete model theory. | A later summary, answer or practical assessment must not revive the rejected explanation as an equally current interpretation. |
| Day 5: related evidence arrives | Apply the corrected understanding only where it helps; investigate the new subject on its own evidence. | Old venue hours cannot certify new access. If the new evidence already supplies the whole answer, credit memory only for any real reduction in setup or improvement in judgment. |
| A new situation changes a constraint | “I'm in a different kitchen now” changes the relevant setup, not what was true in the old kitchen. | Current circumstances lead; historical statements remain scoped rather than being rewritten as though the past changed. |
| A supporting attachment expires | Keep unrelated, independently permitted history readable; withhold source-dependent material under the earlier treatment table. | OCR, thumbnails, summaries, embeddings and generated answers must not reconstruct the released source. |
| Automatic-use eligibility ends | Stop automatic use and repair dependent results; retain only material with a separate surviving basis. | A generated summary cannot extend its dependencies' lifetime. A new clarification has its own time, but does not reauthorize the old source it refers to. |
| The person returns months later | Under §10's proposed agreement, selectively use still-eligible older conversation where it improves the current experience; otherwise use current context/world supply or separately authorized historical lookup. | No invented familiarity, history backfill, expired-context revival or catch-up assignment. A fresh useful answer remains possible without the old exchange. |
| “Don't use that explanation” | Stop the identified interpretation's future influence and repair its dependents, preserving independently retained originals where authorized. | Excluding an interpretation is not deleting every related source. If the requested scope is unclear, use the existing narrow correction/clarification treatment. |
| Continuity is disabled or a conversation is deleted | Apply §4's distinct effects to pending work, derived context and eligible readers. | No late dependent delivery or revival on re-enable; separately kept material is neither silently destroyed nor used to bypass the exclusion. |

Reconciliation need not keep every intermediate model thought. Preserve only
the authorized evidence and dependency distinctions needed to know who said
what, what was provisional, what changed and which uses require repair. Model
reasoning traces are not a new retention category. If a later statement cannot
be understood without expired or excluded material, omit that dependent use
rather than silently retaining the missing context.

#### Recommendation for the long-return promise

Keep three expectations legible: readable history supports bounded lookup;
optional continuity can make eligible older explorations useful without a
past-directed question; deliberately kept material retains its own owner and
scope. None makes all past circumstances current or substitutes for world data.

Founder review still owns history duration, source-dependent answers and the
broader use agreement. Section 10 is the latest recommendation; §9 preserves
the earlier comparison. Select only the context needed for the contribution,
not a general biography. No retrospective opt-in or changed Ask default is
adopted here. A requested lookup must not enroll otherwise ineligible material
into future Home/Places use; current-answer use and later influence are distinct.

#### Research basis and verification

- [Bensal et al., June 2026, *Recalling Too Well*](https://arxiv.org/html/2606.10949v1):
  full-text desk review. In synthetic misconception conversations across three
  memory systems and five model families, extraction could preserve a user's
  misconception while losing corrective context. Tested mitigations reduced
  measured sycophancy without sacrificing reported recall performance. This
  identifies a representation risk, not a universal result about all memory
  systems or evidence of Vesper behavior. Our inference is to verify preservation
  of corrections, not assume either extraction or summarization is sufficient.
- [Zindulka et al., CHI 2026, *The AI Memory Gap*](https://arxiv.org/html/2509.11851v2):
  full-text desk review. A preregistered experiment with 184 participants found
  lower source-attribution accuracy after AI-assisted ideation/writing a week
  later, especially in mixed workflows. This supports investigating visible
  authorship and interpretation boundaries; it does not demonstrate that a
  particular attribution UI fixes the problem or establish effects on life logs.

Add these branches to existing continuity and cross-consumer fixtures, not a
separate evaluation service. Inspect actual later prompt inputs, displayed
history and dependent outputs after each change; a deleted database row or an
accurate callback alone is insufficient. Compare useful continuity with a strong
no-history result under the [whole-experience review](situated-value-decision-matrix-2026-09-06.md#119-whole-experience-review-received-value-context-and-human-work).
Requested preparation must also meet the [receiving lifecycle](complete-system-integration-roadmap-2026-09-05.md#968-complete-receiving-experience-and-supported-service-boundaries).
Neither reference changes this packet's approval boundary.

### 9. Four-month return: a proposed history agreement and complete walkthrough

**Earlier 90-day comparison, not the current automatic-use recommendation.**
Section 10 supersedes the automatic-use ceiling in this walkthrough; the
until-deletion history and bounded-lookup recommendations remain. Keeping this
comparison shows what the narrower agreement delivers and misses. All its
behavior is hypothetical and unadopted; references to “recommended” below name
the earlier option, not a second simultaneously recommended policy.
Ending automatic reuse should not make a conversation disappear. A person should
be able to resume an eligible old exploration without having remembered to Keep
it, while Vesper does not silently turn that archive into permanent personal
influence. This section resolves the proposed experience more specifically than
§8; the contribution contract and actual existing agreements remain in force.

#### Comparison agreement: earlier recommendation

1. **Eligible private text history remains until the person deletes the
   conversation or account**, for conversations covered by an explicit history
   agreement. Do not expire it merely because they stopped visiting or the
   recent-context window ended. This is a proposed no-automatic-age-expiry policy
   for the active account, not a promise of eternal storage. Account closure,
   operational deletion/backup handling and applicable service limits must be
   disclosed before adoption; no unannounced inactivity purge is assumed.
2. **Automatic recent-conversation reuse remains a separate prospective opt-in**
   with the proposed per-contribution 90-day ceiling, exclusions and contextual
   controls in §§2–4. History may be enabled while this is off. The number remains
   a product choice, not a research-established optimum.
3. **An explicit question about past conversation can invoke bounded lookup of
   still-eligible history**, even beyond that window. This use belongs in the
   history agreement: enough surrounding context to answer accurately, including
   relevant corrections, not a whole-account scan for a new biography. The user
   need not know the old title, date, tab or a special command. Asking a follow-up
   about an opened old exchange can establish the current job; merely opening it
   permits display, not automatic re-enrollment into recent context.
4. **Deliberately kept material keeps its own custody and use scope.** It can
   support longer-lived continuity where actually authorized. Neither history
   nor automatic reuse grants attachment retention, a Life entry, an ongoing
   instruction, sharing or monitoring. A no-history/temporary interaction must
   remain available without making the immediate answer deliberately worse.

Until-deletion history is preferable here to deleting every exchange at day 90:
the latter makes ordinary questions unrecoverable unless the person predicts
their future value and saves them. Indefinite automatic reuse is a different,
broader promise, not the necessary consequence of keeping a readable archive.
The recommended separation costs storage, retrieval and dependency-aware repair;
the existing copy inventory and serving-budget work must establish those costs.
Do not introduce a new archive store, vector index or background summarizer by
inference from this recommendation.

The history agreement must specify admissible text and copied/source-dependent
material, as well as duration. An answer quoting an expired attachment does not
become independently retainable merely because it appears in Chat. Existing rows
with uncertain authority need reviewed classification, not retrospective consent,
automatic migration or destructive cleanup. Approval here would still require a
separate accepted contract amendment and implementation verification.

#### Starting record: no saving habit required

This is a synthetic branch of the cooking exploration in §§3 and 7, not additional
claims about the founder. September 7, September 8 and September 11, 2026, and
January 7, 2027, are fixture dates. The January return is hypothetical, not a
scheduled task, observed future behavior or current-world availability claim.
Assume the proposed history agreement and recent-context opt-in were adopted
before these exchanges; the no-opt-in and missing-history branches appear below.

| Moment | Authored interaction / available record | What it does not establish |
| --- | --- | --- |
| September 7 | “Why did the sauce coat the pasta so well in Italy? I only had one pan in the rental kitchen.” Vesper explains a generally supported finishing technique, without claiming to know that restaurant's recipe. | A permanent kitchen constraint, cooking preference, actual meal reconstruction or accepted cooking project |
| September 8 | “The one-pan limit was just the rental kitchen. I'm not asking for a one-pan recipe.” Preserve that clarification with the exchange. | A verified inventory of the person's present or future home kitchen |
| September 11 | “Could I use that finishing method with a jar of tomato sauce?” The answer applies the method to this question. | Proof the person cooked it, liked it, wants future cooking recommendations or supplied a reusable personal outcome |
| Following months | No new input; no Keep, follow request, friend contribution or completed-outcome report. | Failure to engage, boredom, changed taste, an unfinished task, or authority to fabricate new context |
| January 7 | The September material is outside the proposed recent-context ceiling. Eligible text history remains under the separately adopted until-deletion agreement. | Automatic reuse from the old conversation or current applicability of every old circumstance |

The general method has a real public basis: [Barilla's cooking guidance](https://www.barilla.com/en-us/help-with/pasta-kitchen-tips/how-to-cook-pasta),
checked September 7, supports reserving cooking water, not rinsing pasta for a
sauced dish and finishing it in sauce with reserved water as needed. It supports
the method below, not what happened in a particular Italian restaurant. This
source check does not turn the synthetic exchanges into actual app outputs.

#### January return: receive value, not a catch-up assignment

**Opening Home is not a request to reconstruct September.** Use current eligible
world supply and still-authorized retained relationships. Do not manufacture a
January event, assume a selected browsing city is current physical location,
display months-old practical urgency or lead with “you never tried that recipe.”
If there is no kept material in this branch, do not invent it to make the page
personal. No new input is required to receive independent world value. Home is
not required to demonstrate the archive exists by resurfacing the pasta topic.

**A casual question can recover the old exploration directly:**

> What was that pasta technique we talked about after Italy? I want to try it
> tonight. I've got a pot and a frying pan here.

Under the proposed historical-lookup agreement, resolve the relevant exchange
and its clarification without asking the person to find or paste the transcript.
Use today's equipment statement, not an old kitchen inference. Deliver the method
in the answer, not only “I found your chat” or a link that makes the person search
through it. Illustrative complete response:

> **Finish the pasta in the sauce.** Reserve some cooking water before draining,
> don't rinse the pasta, then cook it briefly in the sauce pan, adding the reserved
> water as needed. That helps the sauce coat the pasta rather than sit separately
> on top. This is the general method we discussed, not a reconstruction of the
> restaurant's recipe.

Expose the exact September conversation and public technique source as optional
evidence. No setup questionnaire, compulsory Keep, new cooking Plan or trailing
reflection prompt is needed. The earlier rental-kitchen correction remains
inspectable but need not become another paragraph when today's request already
supplies the equipment.

**Credit the right benefit.** A capable assistant without history can explain the
same technique. Vesper's additional contribution here is resolving which method
“that” refers to, recovering the prior discussion and avoiding stale setup—not
exclusive culinary knowledge. Compare source assembly and re-explanation effort
separately from equal-information answer quality under [the received-value
ledger](situated-value-decision-matrix-2026-09-06.md#119-whole-experience-review-received-value-context-and-human-work).

An explicit past-conversation reference is not a magic phrase requirement. A
clear follow-up in the old exchange can invoke the same bounded lookup. A generic
new question such as “What should I cook tonight?” must not automatically scan
expired recent-context material under the pretense that all cooking questions
are historical requests. Resolve meaningful ambiguity narrowly; do not turn this
boundary into per-turn permission dialogs.

#### Branches that must work without changing the story to help Vesper

| Change only this fact | Desired behavior |
| --- | --- |
| History retained, automatic reuse was never enabled | The user-directed lookup still works under its actual history agreement. No retrospective automatic reuse is implied. |
| The person previously said “don't use this for recommendations” | Honor that exclusion on Home/Places and in other recommendation uses. An expressly requested historical lookup may still work if its separate use was preserved; do not reinterpret a broader “never use this again” exclusion as permission. |
| History was never retained, was deleted or is currently ineligible | State that the old exchange cannot be recovered. Offer a fresh useful method on current evidence without claiming it was the original answer. Ask for a missing detail only if it materially changes the answer. |
| A supporting Ask photograph expired | Do not redisplay, analyze or reconstruct it from thumbnails, OCR or a model summary. Independent eligible text may remain; if asked what the image showed, say the image was not kept. Re-upload is optional and needed only for a new image-specific job. |
| The method was independently kept in another branch | Refind the exact retained owner from Chat or Life, and apply its actual use grant. Conversation deletion does not silently delete it; a use exclusion must not be bypassed through the duplicate reference. |
| The person simply reads and leaves again | No pending decision, automatic watch, reminder, outcome inference or absence debt follows. Home can remain worthwhile without more cooking content. |
| Today's context differs from September | Current instructions and evidence govern. A resumed explanation does not restore an expired circumstance, resurrect a shared arrangement or override a separately governed protected constraint. |

#### Prevent lookup from silently renewing old influence

The January request is a new contribution with its own current purpose. The
retrieved September text and source-dependent portions of the new answer retain
their old dependency and use boundaries; a fresh message timestamp cannot make
them new automatic-continuity evidence. Separate newly authored current facts
from retrieved quotations, summaries and explanations. If they cannot be safely
separated, exclude the dependent material from automatic later admission.

The person can deliberately create new scope—“Keep this method for next time”
or another clearly authorized instruction—through the existing owner path. This
is not required for the current historical answer to work. It also cannot revive
a deleted photo, disclose another person's protected material or silently grant
every later consumer access. A correction still follows the original dependencies,
not just the newest answer's display.

#### What this recommendation does and does not deliver

The intended agreement can be explained as: **keep eligible text conversations
available until deletion; optionally let recent conversations improve later
private help; let an explicit question revisit eligible older history without
turning it into general ongoing influence.** Attachment and source-dependent
limits must be understandable alongside this explanation, not hidden in a promise
that “all your chats stay forever.” This is comprehension-review wording, not
shipping consent copy or a completed data policy.

There is an important strategic limit: this version does **not** automatically
connect every unkept question from years ago to today's Home. Longer-lived kept
evidence can contribute under its own scope, but an old unkept exploration cannot
be revived opportunistically after its recent-use window. If spontaneous
years-spanning conversational connections are essential to the intended promise,
the automatic-use agreement must be reconsidered explicitly. Do not solve that
gap with hidden permanent summaries, silent retention renewal or pressure to
save every question. The four-month case supports dependable return; it does
not by itself establish that the 90-day balance fits the entire long-term vision.

**Earlier decision option:** until-deletion eligible text history plus bounded
user-directed historical lookup, alongside—not substituted for—the proposed
90-day optional automatic continuity. Approving this document's walkthrough is
not accepting those policies on behalf of users. Founder policy adoption, the
account agreement, copy/derivative lifecycle and implementation remain distinct.
Keep the [existing integration roadmap](complete-system-integration-roadmap-2026-09-05.md#968-complete-receiving-experience-and-supported-service-boundaries)
as the execution owner; this is no new launch restriction or strategy framework.

### 10. Selective long-range continuity: four complete experiences

**Latest recommendation, September 7; proposed, not activated.** Replace the
universal 90-day automatic-use ceiling with selective use of eligible older
conversations under the prospective agreement in §§2 and 4. Retain §9 as the
earlier comparison. This is a product-policy recommendation, not an accepted
contract amendment, an account grant, a migration or a claim of implemented
behavior. No canonical contract or runtime setting changes in this pass.

#### 10.1 The agreement these experiences are testing

> With your permission, Vesper can draw on older conversations when they make
> today's help more useful or interesting. Past circumstances don't automatically
> remain current, and past interests don't become permanent labels.

This is the experience promise, not sufficient consent copy on its own. Pair it
with §4's explicit material, prospective scope, Home/Places use and months/years
duration explanation, and the separately disclosed history agreement. Keeping
history available does not turn automatic use on. Temporary/no-history questions
remain possible; a history-only user can still request a bounded old lookup.

“Selective” means something concrete: start from the current question, available
world contribution or authorized human contribution; retrieve only older context
that could improve it; preserve source, subject and corrections; then decide
whether it actually earns influence. Do not insert the whole archive into every
prompt or periodically turn every past question into a Home item. An interesting
explanation can earn space without an urgent event. Present purpose includes
curiosity and enjoyment, not just practical tasks.

#### 10.2 Reading conditions and evidence

These are **written product specimens, not app outputs or user-study results**.
They branch independently; they are not four required steps, fixed Home sections
or an itinerary through four tabs. Dates in 2027 are hypothetical fixture dates.
Every old-chat branch assumes the proposed long-range opt-in and history
agreement covered the contribution **when it was originally admitted**. Merely
turning on a setting in January cannot authorize a September conversation.

The entry check is independent of those enabled-history branches: before a
newcomer's first question, explain the actual off mode and separate history
treatment without blocking assistance. Answer usefully. If they then enable
continuity, only eligible subsequent contributions are admitted. Do not count
that first question as remembered evidence in a later specimen. Declining leaves
fresh answers, independent Home/Places value and separately authorized friend
contributions available. This is a written comprehension scenario, not an
implemented onboarding flow or a claim that participants understood the copy.

The examples draw on the founder's cooking, cliffs, access and social stories,
but all quoted fixture dialogue, other participants and venue notes below are
synthetic. They are not additions to the founder's biography or claims about
actual friends. Public claims have separate sources:

- [Barilla's cooking guidance](https://www.barilla.com/en-us/help-with/pasta-kitchen-tips/how-to-cook-pasta),
  checked September 7, supports reserving water, not rinsing and finishing pasta
  in sauce. It does not identify the method used at a particular restaurant.
- [Palisades Interstate Park's geology account](https://njpalisades.org/nature/),
  checked September 7, describes magma intruding between rock layers about 200
  million years ago, cooling into diabase, and later erosion exposing the sill.
  Its current page also carries a Giant Stairs closure notice. Neither that
  notice nor today's access conditions can be projected into a 2027 fixture.
- Fictional access hours, a fictional Sunday gathering and fictional sharing
  grants are expressly assumed for comparison. They are not researched supply,
  actual invitations or evidence that those owner paths are enabled.

#### 10.3 Experience A — a casual question, without asking to revisit the past

**Earlier eligible exchange, September 7–11:** the person explored why Italian
pasta sauce clings, clarified that a one-pan limitation belonged only to a rental
kitchen, and asked about applying the technique to jarred tomato sauce. No meal
completion, cooking project, durable equipment profile or preference was reported.

**January 7, new Chat:** “Pasta and a jar of tomato sauce tonight. What's the one
thing worth doing differently?” This is a current practical question, not an
explicit historical lookup.

**Proposed answer:**

> **Finish the pasta in the sauce instead of pouring sauce over it.** Have the
> sauce warm before you drain. Reserve some pasta water, drain without rinsing,
> then cook the pasta and sauce together for a minute or two, adding a little
> reserved water as needed. You don't need to replace the jar sauce.

The earlier discussion can establish a relevant method and level of explanation;
the correction prevents a rental-kitchen limitation returning as today's setup.
It does not establish that the person remembers the method or has tried it.
Optional source access leads to the exact eligible exchange and public technique
source. No “you love cooking,” memory announcement, setup questionnaire, Keep
request or closing assignment is needed.

**Capable no-history comparison:** the same current question and public guidance
can produce essentially this same answer. It must be allowed to do so; do not
give the baseline a needless questionnaire or inferior recipe. This case supports
useful ordinary entry and correct non-interference, not exclusive knowledge or
proven answer superiority. Credit less re-explanation only if actual outputs
show it. Under the older 90-day option, answer freshly rather than quietly
retrieving the September exchange as though the question requested it.

**If the person reads and leaves:** the answer is complete. There is no cooking
task, inferred success, follow-up or new Life object. Only the eligible authored
question can enter continuity under the assumed agreement; generated references
keep their source dependencies and never become evidence of a cooked meal.

**Control and long-return branches — change only the stated instruction:**

| After the September exploration | January receiving consequence |
| --- | --- |
| “Stop showing me cooking stuff on Home” | The Home exclusion remains effective unless changed; do not invent an expiry. The requested Chat answer above can still use eligible cooking context where it helps. Suppress pending Home cooking delivery, not the requested answer, and do not infer dislike or create a Life cleanup task. |
| “Don't use this conversation for recommendations” | Do not use the old exchange to recommend tonight's technique, even though a recommendation is now requested. Answer freshly from today's question and public guidance. A separately permitted explicit lookup of the old explanation remains distinct and must not re-enroll it. |
| Turn continuity off after September, then re-enable on January 7 | September's derived continuity was cleared; re-enabling does not rebuild it. Deliver the same useful fresh answer. Eligible history may still support an explicitly requested lookup under its separate agreement, but the generic January question is not one. No catch-up task or request to re-document September follows. |

The new cooking request does not erase a Home exclusion or a broader source-use
ban. If an actual later instruction changes one, acknowledge that exact change
instead of treating renewed topical interest as permission. A known correction
must not be lost through retrieval; when the old exchange is ineligible, omit it
rather than retrieving its original equipment claim without the correction.

#### 10.4 Experience B — Home makes an old observation newly interesting

**Earlier eligible text, September:** “Sorrento is built above these cliffs—how
does a coastline end up looking like that?” The historical exchange does not
prove the exact rock formation in an unkept photograph or a permanent geology
interest. Assume Vesper has not already delivered the Palisades explanation.

**January Home:** the person has explicitly selected New York as the browsing
area. There is no new question, weekend plan or current GPS claim. An eligible
public geology contribution about the nearby region is available. This is
on-visit selection of substantive supply, not a newly commissioned article or
a background promise made on opening Home.

**Proposed compact contribution:**

> **The Palisades aren't a frozen lava flow.**
>
> Their rock cooled underground. About 200 million years ago, magma pushed
> between layers of sandstone and shale and hardened into a sheet of diabase.
> Erosion later exposed its edge: the cliffs along the Hudson.
>
> What looks like a wall is the exposed edge of something once buried.

The source remains available beside optional depth or the exact Place
continuation. This is editorial explanation, not an assertion that a trail is
open or an invitation to walk beneath a rockfall area. A later outing request
requires current access, route and condition evidence through the live owners.

**What older context adds:** it gives a grounded reason to select this mechanism
and nearby place from a broader supply, extending an earlier question beyond the
place where it arose. It does not supply the geology or establish the person's
reaction. Optional “Why this?” can say: “Your September question concerned how
cliffs form. This explains a different cliff landscape in the New York area
you're browsing.” Do not put that callback ahead of the explanation.

**Capable no-history comparison:** the same Palisades contribution is eligible
as worthwhile New York material without a personal match. It might even be
selected in both versions. Compare selection across the same varied supply and
whole scroll, not a rich personalized card against an empty page. The potential
gain is contextual selection and transfer, not exclusive facts. If it repeats
delivered content, crowds out current life or is no better than another unit,
leave the old connection out. Do not assert that Sorrento has a particular
geological origin without identifying and sourcing that formation separately.

**If the person reads and leaves:** they received the explanation. No saved
destination, visit, preference, hiking plan, reminder or request for a reaction
follows. Exposure bookkeeping may prevent repetitive delivery; it does not prove
enjoyment or deepen a personal-interest claim. Life receives no automatic entry.

**Discovery, correction and escalation:** opening Home is the invitation to
receive this explanation, not a request for an archive recap. The continuity
grant permits the eligible selection; the visit does not create that grant.
If the person says “Don't bring up my Italy trip,” stop unrequested trip-derived
resurfacing within that resolved scope, including pending dependent suggestions.
Do not merely remove the visible callback while secretly using the same excluded
trip basis to select the replacement. Independent New York world value remains
available; the instruction is not automatically a ban on all geology. A later
explicit request to compare with Sorrento may use still-eligible history under
the narrower resurfacing restriction, but not under a broader “don't use that
conversation” ban unless the person clearly changes that scope.

If instead they say “Could I go there this afternoon?”, continue to the actual
Place and live assessment using current conditions. The geology does not certify
access, the tap does not select a route or save a destination, and the invitation
to help does not create a watch. Neither the explanation nor the old interest
justifies an unsolicited push notification. The source of practical truth and
the authority for any later action remain distinct from this on-visit value.

#### 10.5 Experience C — changed circumstances and a late correction

**September 7:** an access discussion includes a temporary request for a route
without stairs. **September 8:** “The problem was that the lift closed before
we returned, not the walking distance.” **September 11, another eligible chat:**
“The step-free request was for my parents on that outing, not a standing need
for me.” Preserve the correction's referent across chats; do not synthesize a
profile of either the person or their parents.

**January 7, current request:** “I'm going to this gallery alone and leaving at
7. Which entrance works?” An explicitly fictional, currently valid venue note
supplied with the question states: West Court lift closes at 6; West Court stairs
remain open until 8; Main Street step-free entrance remains open until 8. Assume
there is no separately governed standing accessibility constraint in this case.

**Proposed answer:**

> **Both entrances work for a 7 p.m. departure.** West Court's stairs stay open
> until 8, but its lift closes at 6. Main Street stays step-free until 8, so use
> that entrance if you'd rather avoid the stairs.

No question about the parents, mobility profile or old trip is needed. The
current note supports the answer; the past correction prevents the system from
wrongly excluding West Court or promising a lift for the return. The original
September constraint remains an account of that outing, not rewritten history.

**Capable no-history comparison:** essentially the same answer. This is an
intentional non-use/correction case. Memory should avoid making assistance worse;
it need not manufacture a visible benefit. If a genuine protected standing
constraint exists in a different branch, follow that owner's current rule rather
than treating this fixture as permission to ignore it. If current access evidence
is missing or stale, old venue details cannot fill the gap.

**Repair and ending:** after the September 11 correction, any pending or cached
recommendation depending on a permanent stair-avoidance inference must be
revalidated, not merely hidden in one chat. Other retained evidence survives
under its own basis. A correction to an ineligible old exchange cannot revive
its excluded content. If the January answer is read and left, no visit, route
selection or follow mandate follows. The live engine supplies present feasibility;
memory contributes scope and correction, not operational truth.

**Scope controls must repair the pending result, not just the wording.** The
September 11 correction should preserve only the eligible subject distinction,
not acquire a parents' mobility profile. If a pending suggestion relied on the
wrong permanent self-constraint, repair or withhold that dependent result before
it reaches Home, Places or the next Chat. Source custody and separately governed
protected constraints retain their own rules. If continuity was turned off after
September, January's fresh venue note can still support the answer above without
retrieving the excluded history. Vesper must not require memory to provide
ordinary practical competence.

If the person asks to send the entrance information to a companion, resolve that
exact sharing command through the audience owner; private history is not part of
the message by default. An authorized factual message is not an RSVP, an access
guarantee or an ongoing check. A later change to the venue's hours requires new
world evidence, not confidence derived from remembering the old lift incident.

#### 10.6 Experience D — a friend creates the opening; memory is optional

**Earlier eligible private question:** the person asked what the people playing
boules in Nice were doing and how pétanque scoring works. An explanation was
delivered; no intention to play, skill level or ongoing preference was established.

**Months later, synthetic direct contribution from Maya:** she sends this
recipient a Paris photograph and the following note, under a current grant for
private display in their Home/Places. Her original photograph and words remain
attributed; no group-wide or public reuse is assumed.

> **Maya · Paris last week**
>
> We stopped to watch pétanque for ten minutes and stayed for an hour. I've
> borrowed a set—River Park, Sunday at 3, by the south gate. Come play or just
> hang out; I'll bring it either way.

River Park and this invitation are fictional fixture content. Maya's explicit
offer supplies the time, place and low-pressure participation; Vesper did not
infer current availability from the photograph or manufacture an invitation.

**Proposed Home treatment:** deliver that photograph and original note intact,
with its exact contribution destination and an optional reply. No AI paragraph
is required. The recipient can enjoy the Paris moment, understand the local
offer and leave without replying or supplying an artifact. This belongs on Home
because it is addressed and
offers a current shared possibility. An ordinary unaddressed Paris post belongs
in the existing casual-sharing Places treatment; memory similarity alone does
not promote all friends' posts into Home.

**Pressure-tested memory addition:** “From watching in Nice to joining in here”
is an accurate callback, but adds little to Maya's already complete invitation.
Do **not** ship it merely to demonstrate continuity. If the recipient asks how
to join, give useful current help and avoid re-teaching an explanation solely
because it is stored; do not assume they remember or know how to play. Private
history may shape private assistance only under its actual grant. It is not
included in a reply, shared card or Maya's view by implication.

**Capable no-history comparison:** the same original contribution delivers the
same central value. This is a successful social experience and deliberately not
evidence that long-range memory improved it. A future juxtaposition must add a
real, permissioned difference in perspective; ordinary human sharing does not
owe Vesper an editorial transformation.

**If the recipient leaves:** no RSVP, attendance, reply debt, organizer role or
relationship assessment follows. Maya does not receive a memory-use report or
passive-view notification. Source withdrawal or a changed invitation must
update dependent Vesper views under the existing owners; it cannot promise
erasure of screenshots or messages already sent outside Vesper.

**Control and later-change branches:** with conversational continuity off, Maya's
original note and photograph still deliver the same value under their separate
live share grant. Do not remove them or disable ordinary reply merely because
personal-history use stopped. Conversely, “don't use my Nice conversation” stops
that private context from shaping help; it neither withdraws Maya's offer nor
grants her access to the excluded material. A person-authored restriction on her
contribution is resolved separately rather than confused with a memory setting.

If Maya changes the venue, show the current owner-backed correction and update
dependent receiving views; if she withdraws the source, enforce that withdrawal
even if a private summary still exists. If the recipient opens the old exchange
months after Sunday, retain only still-authorized historical material and make
the expired date clear; do not recreate a live invitation. A message to Maya or
an acceptance requires its own resolved command. No memory grant, card view,
absence or private question supplies that command or authorizes a push report
to either person.

#### 10.7 What the four experiences settle—and leave open

The proposed value is **selective application, not compulsory personalization**.
A generic question can be complete; a substantive Home contribution can extend
old attention; correction can correctly change nothing visible; a friend's
original contribution can be the entire social payoff. The four moves remain
an audit lens across these experiences, not another sequence or set of slots.

The specimens support removing the *design assumption* that all useful automatic
continuity must end at day 90. They do not establish improved retention, broad
consumer demand or that every old exchange should remain eligible. This pass
does not claim an uplift merely because we can write plausible prose.

At the existing [whole-experience review](situated-value-decision-matrix-2026-09-06.md#119-whole-experience-review-received-value-context-and-human-work),
compare three clearly labeled conditions: capable no-history help, the earlier
90-day agreement, and the proposed selective long-range agreement. Hold today's
question, public supply, current grants and tool capability constant; disclose
the intended difference in permitted historical evidence. Separately give a
capable baseline the same historical facts to distinguish answer quality from
the person's work finding and re-explaining them. Do not manufacture baseline
homework or require every case to favor memory.

Inspect the actual result, the historical fact that changed it, the new substance
or effort removed, unwanted assumptions, breadth of Home, control consequences
and whole-service cost. Include an old correction, exclusion, source expiry,
opt-out during production and absence. A quiet read is a complete encounter,
not measured satisfaction. Any voluntary user review should ask whether the
result was useful and whether the historical use was welcome; no routine
in-product rating, recall quiz or memory-cleanup assignment follows.

The §4 refinements add paired checks within these same experiences, not another
research lane: first-answer off versus subsequent opt-in; requested cooking help
after Home-only suppression versus a broad recommendation-use ban; on-visit
cliff discovery versus interruption or practical action; corrected access
context before a pending result serves; and intact friend value with continuity
off versus withdrawal by the source owner. Include off-and-clear followed by a
months-later re-enable, and a request to pause that must not silently clear data.
For each, record the input scope, permitted evidence, actual output, repaired
dependents, preserved independent value and work left to the person. Written
walkthroughs specify expected behavior; they do not establish runtime coverage.

#### 10.8 Integration through existing owners

This is a **contract-level handoff**, not a new code audit or certification of
these paths. The execution owner remains the [integration roadmap](complete-system-integration-roadmap-2026-09-05.md#968-complete-receiving-experience-and-supported-service-boundaries).
Its active receipts govern implementation status; older gap descriptions in
system charters must not be promoted into fresh findings by this document.

| Existing owner / seam | Requirement made explicit by these experiences | What not to build or infer |
| --- | --- | --- |
| Contribution and conversation/Source custody | Resolve prospective history and later-use grants separately; admit only eligible text with original subject, authorship, scope and correction references | No new universal memory table, implicit Ask→Bring conversion, source-copy loophole or historical backfill |
| Governed context / Memory and Preference | Bounded retrieval of still-authorized evidence, including later clarifications across chats; distinguish requested use and on-visit selection, source-use bans and narrower resurfacing exclusions | No permanent personality summary standing in for conversation evidence; no archive appended to every prompt, prompt-only enforcement or preference-vector index by default |
| Source/claim repair and Integration | Preserve dependency identity through old evidence, summaries, caches and current results; recheck eligibility before prompting, publication and read; suppress late excluded delivery; enforce off-and-clear without rebuilding old influence on re-enable | No fresh-summary timestamp laundering, cleanup-only enforcement, silent destructive pause interpretation or correction that stops at one card |
| Home/Places composition and content supply | Select substantive current supply using eligible context where it improves fit; compare whole-scroll breadth, exposure and production budget | No bespoke generation per old question, mandatory callback slot, acquisition-on-GET or profile that limits world discovery |
| Live engine / Place and arrangement owners | Check current access, time and conditions when practical reliance begins; old conversation may identify a question worth checking, never certify the answer | No implied watch, provider booking, automatic route choice or responsibility created by remembering |
| Social contribution / audience and commitment owners | Preserve original human value, attribution, current share purpose and exact invitation; personal history stays private unless separately shared | No memory-based friendship score, inferred availability, manufactured RSVP or merging both people's private outcomes |
| Existing Chat inspection/settings and Life owners | Early actual-mode/history explanation, optional prospective opt-in, contextual correction and exact off consequences; retained objects stay with their owners; no-history/history-only remain useful | No blocking configuration, per-turn memory review, implied first-chat backfill, memory-management tab, compulsory Keep habit or automatic Life object for every question |

Implementation sequence after explicit adoption: map actual writers/readers and
copy lifecycles; name only missing extensions; bind policy and repair through
existing owners; connect retrieval and receiving; review the full portfolio and
combined cost at the roadmap's existing checkpoints. A recent working-set cache
may be useful, but its eviction policy must not silently become either permanent
retention or a consumer-wide age cutoff. No cache, index or service is selected
by this proposal. Unaffected integration and source-lifecycle repairs can proceed
without activating broader continuity or waiting for every specimen to validate.

#### 10.9 Research basis and remaining uncertainty

Research reviewed September 7, 2026. These are the bases for the product judgment,
not evidence that the specimens ran successfully:

- [Zhang et al., CHI 2026, *From Memory to Meaning*](https://www.mingmingfan.com/papers/CHI26-ReminiscenceReview.pdf):
  a systematic review of 60 HCI papers finds strong attention to social/identity
  purposes and less to using the past for present problems. Our inference is to
  explore practical application as well as recollection. The reviewed settings
  and clinical background do not validate an everyday consumer assistant.
- [Jacobsen, *When is the right time to remember?*](https://eprints.whiterose.ac.uk/id/document/2934609):
  26 interviews and four focus groups examined social-media remembering. Timing,
  repetition and perceived insensitivity affected the experience. Our inference
  is to require a worthwhile present contribution, not resurface old material
  simply because it exists or an anniversary arrives. This is qualitative
  evidence, not a ranking formula or optimal cadence.
- [Sumida et al., 2025, *Enhancing Long-term RAG Chatbots*](https://journals.uic.edu/ojs/index.php/dad/article/view/14138):
  the authors report better satisfaction with selective memory/forgetting in
  conversations lasting at least two hours. It challenges “more recall is always
  better,” but is not a months-long consumer study. Their emotional-importance
  strategy is not adopted as Vesper's objective or permission rule.
- [Jiang et al., CHI 2026, *RECALLbot*](https://doi.org/10.1145/3772318.3790714):
  a two-week study of 40 participants evaluated memory bundled with reciprocal
  disclosure/persona behavior, reporting stronger social identity, disclosure
  and trust. Participants were positively disposed toward social chatbots;
  memory's isolated effect and ordinary-life outcomes are not established.
  Vesper should evaluate useful assistance and human-world relationships, not
  substitute AI attachment or greater disclosure for received value.
- [Google Photos' memory controls](https://support.google.com/photos/answer/9454489?co=GENIE.Platform%3DAndroid&hl=en):
  official product guidance separates keeping photos from suppressing particular
  dates, people and memories in featured resurfacing. This is a control precedent,
  not proof that those controls suffice for conversational inference or that users
  should be required to curate their archives.

No source selects 90 days or establishes that unrestricted lifelong automatic
personalization is desirable. Longer-range continuity increases obligations for
comprehension, storage, selection, repair and cost. The unresolved adoption work
is the actual agreement, its operational lifecycle and implementation evidence;
the product recommendation is now specific enough to review without inventing
another philosophy or asking people to save every question.
