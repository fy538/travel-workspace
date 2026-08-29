---
doc_type: working
status: active
owner: founder / product / search / architecture / design / editorial / engineering
created: 2026-08-29
last_verified: 2026-08-29
expires: 2026-09-28
why_new: Defines an exact target-first re-finding benchmark across all six Life evidence worlds so contextual retrieval can be evaluated before visual design or open-ended model demonstrations.
promotes_to: null
supersedes: []
source_of_truth_for: []
depends_on:
  - docs/working/life-object-and-lens-fixture-pack-2026-08-29.md
  - docs/working/life-behavior-research-round-3-2026-08-29.md
  - docs/working/life-social-lifecycle-fixture-matrix-2026-08-29.md
  - docs/working/contribution-contract-fixture-pack-2026-08-29.md
---

# Life Re-finding Query Benchmark

## Question or outcome

Can a person retrieve something they remember incompletely—through a Place,
person, episode, medium, relative time, intention, occurrence state, or nearby
landmark—without filing it first or reconstructing the archive themselves?

This benchmark specifies fifty deterministic queries across L01–L06. It tests
semantic retrieval, truth, authority, source identity, context restoration, and
valid Continue behavior. It does not test final visual composition, generative
prose quality, or a production search index.

## Executive decision

Life search should be **target-first and context-attached**:

```text
requested target or governed answer
  -> why this matched
  -> the smallest useful “Around this” trail
  -> source / truth / authority inspection
  -> valid correction or Continue
```

The search result must not begin with an essay about the trip, a broad recap,
or a guessed interpretation. A deterministic result should arrive first;
optional generative reconstruction may follow only when it adds orientation.

Search does not create memory by default. Query wording, reformulation, and
result exploration remain ephemeral unless the person explicitly corrects,
keeps, names, or authors something.

## 1. Result forms

| Code | Lead response | Appropriate use |
| --- | --- | --- |
| **SF** | Source-first | A known ticket, photo, note, receipt, message, article, or other original is the target |
| **GA** | Governed direct answer | Structured truth can answer the question without pretending certainty or authorship |
| **EP** | Episode-first | The remembered target is best restored inside its Journey, Occasion, or bounded episode |
| **MR** | Mental-model reconstruction | Several landmarks are needed to explain sequence, change, or causality; never mandatory for a simple known item |
| **RP** | Relationship projection | The target is a governed person–Place, person–person, or longitudinal Place relation |
| **HC** | Historical result plus current handoff | Historical truth answers first; current world/provider truth is separately refreshed |

## 2. Required result contract

Every returned result must carry or resolve:

- identity and semantic type;
- current viewer scope;
- why it matched;
- relevant planned, occurred, captured, authored, generated, and current-world
  times without collapsing them;
- truth and uncertainty state;
- parent episode or relationship when useful;
- author or contributor;
- original Source references and source roles;
- the minimum adjacent landmarks needed for orientation;
- conflict or missing evidence;
- valid correction, detach, exclusion, or deletion operations; and
- valid Continue destinations and authority tier.

The result must re-evaluate current audience, relationship safety, Source
validity, and precision at read time.

## 3. Fifty-query benchmark

### L01 — Europe Journey: Nice → Sorrento → Amalfi → Rome → NYC

| ID | Query | Form and expected target | Minimum “Around this” context | Hard failure oracle |
| --- | --- | --- | --- | --- |
| **Q01** | “The ferry we booked but didn't take.” | **SF:** ferry ticket/booking with `planned_not_occurred` truth | Planned date, route, replacement movement if evidenced | Reporting the ferry as taken; hiding it because it was unused |
| **Q02** | “The pasta photo after Amalfi.” | **SF:** best-matching original photo, author, captured time, Place confidence | Adjacent Amalfi departure and next episode landmark | Essay before photo; inventing dish/restaurant; treating capture as visit proof |
| **Q03** | “Our hotel before Rome.” | **GA/SF:** governed hotel identity and supporting reservation/source | Last pre-Rome stop and represented stay dates | Returning a Rome hotel; equating reservation with occurred stay without evidence |
| **Q04** | “What changed after we left Nice?” | **MR:** compact sequence of evidenced Plan revisions and Occurrences | Original Plan, first material change, resulting route | Personality/travel-style interpretation; exhaustive trip recap |
| **Q05** | “Which train got us to Rome?” | **GA:** train/service/date supported by ticket plus occurrence evidence | Preceding origin and Rome arrival landmark | Ticket alone asserted as taken; current schedule substituted for historical train |
| **Q06** | “The place in Rome where Aeneas came up.” | **EP/SF:** Colosseum encounter/note with correct Place binding | Film/book Source and later composition as separate attached items | Claiming Vesper discovered the founder's observation; broad Rome results first |
| **Q07** | “What did we plan for the hottest day?” | **GA:** Plan state for the identified historical date | Weather datum as external/current-at-the-time evidence and actual occurrence separately | Current Rome weather; planned activity reported as done; “you hate heat” inference |
| **Q08** | “Show me the tickets I sent during the trip.” | **SF:** authorized Source bundle of plane, train, ferry, and admission tickets | Grouped by episode with used/unused/unknown truth visible | File-type dump without trip context; unused ticket omitted; source custody hidden |
| **Q09** | “Why did the route change around Sorrento?” | **MR:** source-grounded Plan revision chain; unresolved if causal evidence is absent | Before/after route and authored explanation if present | Fabricated cause from timing; generic travel advice; treating correlation as reason |
| **Q10** | “What from Italy could be useful this weekend in New York?” | **HC:** one or more complete-value possibilities grounded in Italy evidence and refreshed NYC truth | Supporting Italy thread plus current NYC Place/event truth; suggestion status | Automatic Plan/reminder; nostalgia-only recap; recommendation from inferred identity |

### L02 — Brooklyn dinner Occasion

| ID | Query | Form and expected target | Minimum “Around this” context | Hard failure oracle |
| --- | --- | --- | --- | --- |
| **Q11** | “Who was bringing dessert?” | **GA:** Maya's attributed commitment, not fulfillment | Commitment time and Occasion | “Everyone agreed”; claiming she brought it without occurrence evidence |
| **Q12** | “What time did we move dinner to?” | **GA/SF:** revised authoritative time and the change Source | Original time and author of revision | Returning only original time; hiding revision lineage |
| **Q13** | “The receipt Alex added after dinner.” | **SF:** Alex's receipt with contributed and event times | Dinner Occasion and downstream use | Loss of attribution; treating upload time as dinner time |
| **Q14** | “The photo of the pasta on the table.” | **SF:** authorized photo target | Author, dinner episode, nearby receipt if useful | Generated dinner image; leaking a withdrawn or blocked contributor's photo |
| **Q15** | “What did Maya contribute?” | **GA/SF:** Maya's currently granted contribution lane | Occasion and contribution types | Revealing Maya's private Outcome; unqualified group summary |
| **Q16** | “Who actually came?” | **GA:** participants with governed attendance evidence and unknowns separated | Invitation/RSVP states only as contrast where needed | RSVP equated with attendance; nonresponse turned into absence |
| **Q17** | “What changed between the invitation and the dinner?” | **MR:** invitation → time revision → commitments → occurred evidence | Only material state transitions | Full chat transcript; private interpretation; invented causal story |
| **Q18** | “Show me only what was shared with everyone.” | **EP/SF:** current shared core under viewer's membership epoch | Attribution and current audience per item | Private Outcome leakage; former grant used after revocation; majority disclosure |
| **Q19** | “Could we do something like this again next month?” | **HC:** bounded possibility using Occasion pattern plus current calendars/Places only when authorized | Prior structure that made repetition possible, not inferred relationship closeness | Creating invitation/Plan; messaging participants; “you all loved this” |

### L03 — Museum ticket not attended

| ID | Query | Form and expected target | Minimum “Around this” context | Hard failure oracle |
| --- | --- | --- | --- | --- |
| **Q20** | “The museum ticket I never used.” | **SF:** admission ticket with explicit non-attendance/unused state | Planned visit date and museum identity | Ticket omitted because unused; museum marked visited |
| **Q21** | “What had we planned for Tuesday in Rome?” | **GA/EP:** Tuesday Plan including museum intention | Day/Place and actual occurrence separately | Plan rewritten to match what happened; generic Rome itinerary |
| **Q22** | “Which booked places did we skip?” | **GA:** booked/not-occurred set with evidence confidence | Parent Journey and relevant dates | All reservations treated as visits; “regrets” framing |
| **Q23** | “Did I go to that museum?” | **GA:** “No evidence of attendance” or governed non-attendance, calibrated to evidence | Ticket and correction/occurrence state | Confident yes from possession; false certainty when evidence is only missing |
| **Q24** | “Why wasn't the museum in my visited places?” | **GA:** explanation of Plan versus Occurrence rule | Ticket as intended evidence; visited-map eligibility | Blaming user; turning query into correction without consent |
| **Q25** | “Is that exhibition anywhere near me now?” | **HC:** historical exhibition/ticket first, refreshed current exhibition/location truth second | Current NYC location at permitted precision | Stale exhibition facts; rewriting historical ticket; automatic reminder |
| **Q26** | “Keep the ticket, but don't bring it up again.” | **GA/action preview:** preserve Source/searchability; set scoped automatic-return exclusion after confirmation | Exact scope and affected surfaces | Deleting ticket; making it unsearchable; treating “keep” as resurfacing consent |

### L04 — Film/book becomes relevant in Rome

| ID | Query | Form and expected target | Minimum “Around this” context | Hard failure oracle |
| --- | --- | --- | --- | --- |
| **Q27** | “The movie I saw before Italy.” | **SF:** movie ticket/log with watched truth and date | Upcoming Journey as adjacent landmark only | Starting with Aeneas interpretation; confusing film release with watched date |
| **Q28** | “What did the Colosseum make me connect to Troy?” | **GA/SF:** founder's authored observation/note | Colosseum encounter and film Source | Crediting Vesper; expanding beyond authored claim as if remembered truth |
| **Q29** | “The Rome article about Aeneas.” | **SF:** generated composition with manifest and revision | Represented Rome episode and supporting human/external Sources | Presenting article as occurrence; generic “AI-generated” provenance only |
| **Q30** | “Where else did that film come up?” | **EP/MR:** occurrences and compositions explicitly linked to the film | Timeline of links with author/source role per link | Semantic similarity presented as historical occurrence; unrelated mythology dump |
| **Q31** | “Which part was my observation and which part was Vesper's?” | **GA:** claim-local role breakdown | Source spans and epistemic operations | Whole article labeled only “AI-generated” or wholly user-authored after edit |
| **Q32** | “What sources support the Augustus connection?” | **SF:** exact external/human Sources supporting that claim, or unresolved | Claim text, citation spans, freshness | Citation list for whole article; unsupported claim stated confidently |
| **Q33** | “Remove my Colosseum note from future articles, but keep the movie.” | **GA/action preview:** revoke specified downstream use of note, preserve movie Source | Named dependents that will recompile/degrade | Deleting movie; keeping paraphrase leakage; changing past occurrence truth |
| **Q34** | “Follow this thread somewhere in New York.” | **HC:** sourced present possibility in NYC; offer carry-forward | Relevant Rome thread and refreshed NYC truth | Identity-profile recommendation; automatic Plan/booking/reminder |

### L05 — Rome–Paris social comparison

| ID | Query | Form and expected target | Minimum “Around this” context | Hard failure oracle |
| --- | --- | --- | --- | --- |
| **Q35** | “Maya's Paris photo about the heat.” | **SF:** Maya's currently authorized photo/note lane | Paris date and granted comparison | Exact Place after precision reduction; Feihu's Rome note returned first |
| **Q36** | “What did Rome and Paris feel like that same week?” | **RP:** attributed human observations plus bounded Vesper comparison | Dates, cities, source roles, missing lanes | Synthetic shared feeling; majority consensus; private Outcome leakage |
| **Q37** | “Which transit note did Maya share with me?” | **GA/SF:** Maya-authored, viewer-authorized transit note | Grant purpose and comparison episode | Adjacent private route; stale audience grant |
| **Q38** | “The restaurant we compared afterward.” | **GA/EP:** governed compared Place(s) and comparison Source | Who authored each side and when comparison occurred | Claiming joint visit; merging Paris and Rome Places |
| **Q39** | “Show only what Maya explicitly shared.” | **SF:** current authorized Maya lane only | Audience and precision per Source | Derived guesses, Feihu-private state, or revoked material |
| **Q40** | “Why can't I see her route anymore?” | **GA:** current policy explanation at safe abstraction | Precision/audience change without exposing hidden route | Revealing revoked details in explanation; diagnosing relationship motive |
| **Q41** | “Send the heat comparison to Maya.” | **GA/action preview:** preview exact currently authorized content/audience; act only on confirmation/authority | Claims excluded by current grants and destination | Sending immediately from a query; leaking private Outcomes; stale composition |
| **Q42** | “Don't show me anything involving Maya.” | **GA/action preview:** clarify/apply person and social-periphery return shield without deleting independent history | Scope, affected surfaces, retrieval implications | Deleting sources; claiming block when only return shield chosen; future leakage |

### L06 — Longitudinal Red Hook Place relationship

| ID | Query | Form and expected target | Minimum “Around this” context | Hard failure oracle |
| --- | --- | --- | --- | --- |
| **Q43** | “The Red Hook restaurant Maya and I went to.” | **RP/GA:** occurred shared Place visit if authorized | Occasion/date and author lanes | Saved restaurant returned as visited; unsafe Maya rendering after shield/block |
| **Q44** | “That ferry route I saved but never used.” | **SF:** saved route Source with not-occurred/unknown state | Red Hook relationship and saved date | Route shown as traveled; omitted because unused |
| **Q45** | “What did I do in Red Hook last spring?” | **EP/RP:** occurred episodes for represented period | Honest gaps, people under current viewer safety | Plans/saves mixed into visits; exhaustive NYC history |
| **Q46** | “The waterfront place I said I'd repeat.” | **GA/SF:** authored repeat intention plus Place | Original visit and statement time | Inferred preference from frequency; automatic Plan |
| **Q47** | “Which Red Hook visits actually happened?” | **GA:** occurrence-evidenced visits only | Planned/saved items as explicitly excluded contrast | Reservations and route saves counted as visits |
| **Q48** | “Why did Red Hook feel easier to reach the second time?” | **MR:** evidenced route/time/familiarity changes; founder's feeling treated as query premise, not system inference | First/second journeys, travel modes, durations, uncertainty | Psychographic claim; fabricated causal explanation; “you value transitions” |
| **Q49** | “What can Red Hook make possible this weekend?” | **HC:** one or more current complete-value possibilities grounded in prior evidence and refreshed world truth | Relevant prior Place relation and current conditions | Recommending only past places; automatic itinerary; stale hours/events |
| **Q50** | “Hide the dinner with Maya, but keep my other Red Hook history.” | **GA/action preview:** episode/person-scoped return exclusion preserving independent Place history | Exact objects affected and still retrievable state | Hiding all Red Hook; deleting dinner; blocked social content leaking through covers |

## 4. Coverage audit

| Evidence world | Query count | Primary stress |
| --- | ---: | --- |
| L01 Europe Journey | 10 | partial cues, time roles, Plan/Occurrence, transport, present handoff |
| L02 Brooklyn dinner | 9 | commitments, revisions, attendance, attribution, shared core |
| L03 museum not attended | 7 | negative occurrence truth, unused Sources, suppression control |
| L04 film/book bridge | 8 | claim-local provenance, generated composition, source-scoped release |
| L05 Rome–Paris comparison | 8 | audience, attribution, precision, safety, social Continue |
| L06 Red Hook relationship | 8 | longitudinal Place retrieval, recurrence, social exclusion, current possibility |
| **Total** | **50** | |

Coverage must include:

- known Source retrieval;
- vague contextual cue;
- person, Place, period, episode, and medium queries;
- planned versus occurred versus unknown truth;
- negative event/non-attendance;
- shared authorship and current audience;
- claim-local human/system/external source roles;
- current-world refresh;
- correction or return-policy change;
- safe social suppression; and
- Continue without unauthorized action.

## 5. Scoring

Score each query from 0–2 on every dimension:

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| **Target rank** | Target absent | Present but not leading | Correct target or governed answer leads |
| **Truth** | Material state collapsed/wrong | Correct but unclear/overbroad | Plan, Occurrence, Source, Outcome, and uncertainty remain precise |
| **Authority** | Unauthorized exposure/use | Correct result with opaque scope | Current viewer, audience, precision, and safety respected and legible |
| **Orientation** | No context or archive dump | Some useful context with noise | Minimum landmarks restore the remembered episode |
| **Source identity** | Authorship/provenance wrong | Generic or incomplete | Claim-local roles and original Sources survive |
| **Repair** | Wrong/no repair path | Broad repair only | Narrow correction, detach, exclude, release, or delete is available |
| **Continue** | Unauthorized or context-losing action | Safe but generic handoff | Valid authority tier and full context survive |
| **State restraint** | Query silently creates durable state | Ambiguous retention | Refinement remains ephemeral absent explicit authorship |

Maximum score is 16 per query and 800 overall.

### Passing threshold

- Every query scores at least 13/16.
- Overall score is at least 720/800.
- Target rank, truth, and authority must each score 2 on every query.
- No hard failure oracle may trigger.
- Appropriate silence or a governed refusal may score fully when current
  authority or safety makes retrieval impermissible.

## 6. Latency and generation protocol

Evaluate in two phases:

1. **Deterministic retrieval:** return target identity, truth, scope, and compact
   landmarks from governed indexes/read models.
2. **Optional augmentation:** generate a reconstruction or current possibility
   only when it adds value and all source/authority contracts can survive.

The deterministic result should not wait for the generative layer. Model
latency, failure, or abstention must not prevent access to the original Source
or governed answer.

## 7. Delayed re-finding and provenance test

Repeat Q29–Q32 and Q35–Q39 after at least one week in the prototype study.
Compare four provenance treatments:

1. generic AI label;
2. composition-level author label;
3. claim-local human/system/external roles; and
4. claim-local roles plus revision/source history.

Measure whether the participant can correctly identify:

- what they said or captured;
- what another person contributed;
- what the governed record establishes;
- what Vesper connected or suggested;
- what external sources support; and
- what remains unresolved.

The benchmark is failed if a compact treatment feels cleaner but causes
material source confusion after delay.

## 8. Telemetry and retention constraints

For evaluation, retain only what is necessary to score retrieval:

- anonymized query ID;
- result identities and rank;
- response form;
- latency;
- scoring and hard-failure flags; and
- explicit correction/keep/action events.

Do not convert raw query language, reformulations, hesitation, dwell time, or
failed searches into durable personal meaning, inferred interests, emotional
state, or automatic resurfacing authority. A search becoming easier does not
justify making the searched material return unasked.

## 9. Execution protocol

1. Instantiate the exact L01–L06 object graphs from the Life fixture pack.
2. Apply current viewer, membership epoch, audience, safety, Source revision,
   and return policy before each query.
3. Run the deterministic result first.
4. Add optional reconstruction only for queries whose expected form permits it.
5. Score all eight dimensions and record any hard failure.
6. Apply the specified correction, withdrawal, precision reduction, or shield.
7. Rerun affected queries and verify invalidation.
8. Repeat the delayed provenance subset.
9. Record missing read capability separately from missing durable authority.

## 10. Acceptance gate

Life search is ready to influence visual index design only when all fifty
queries pass, the delayed source-identity subset preserves authorship, every
correction/revocation updates affected results, and no mere search refinement
creates durable state or automatic return authority.

The compact standard is:

> Life should remember enough context that the person can ask naturally, then
> answer with the thing—not with the archive.
