---
doc_type: working
status: active
owner: founder / product / design / architecture / engineering
created: 2026-08-29
last_verified: 2026-08-29
expires: 2026-09-28
why_new: Executes the six Life evidence worlds against the accepted entrance, re-finding, social-lifecycle, source-identity, return, and Continue contracts before deriving the canonical Life index and episode anatomy.
promotes_to: null
supersedes: []
source_of_truth_for: []
depends_on:
  - docs/decisions/2026-08-29-adopt-life-continuity-and-return-contract.md
  - docs/working/life-object-and-lens-fixture-pack-2026-08-29.md
  - docs/working/life-social-lifecycle-fixture-matrix-2026-08-29.md
  - docs/working/life-refinding-query-benchmark-2026-08-29.md
---

# Life Six-World Fixture Execution Report

## Question or outcome

Do the accepted Life policies produce coherent behavior across all six evidence
worlds, and what index, episode, search, social, provenance, and Continue
requirements survive the comparison?

## Execution level

This is a **deterministic semantic execution**, not a production test. It runs
authored object graphs and expected state transitions against the accepted
contracts.

| Result | Meaning |
| --- | --- |
| **CONTRACT PASS** | The governed expected result is internally coherent and violates no hard gate |
| **CONTRACT SILENCE** | Suppression or no generated treatment is the correct result |
| **IMPLEMENTATION PARTIAL** | Current models contain some necessary primitives but no complete Life behavior is proven |
| **IMPLEMENTATION ABSENT** | The required aggregate read path or transition is not code-evidenced |
| **POLICY BLOCK** | A product-policy choice prevents a deterministic result |

The semantic fixtures must pass before visual design. They do not prove that
the current app can produce the result. Production proof requires read models,
projection fixtures, integration tests, and human evaluation.

## 1. Resolved policy oracle

The execution uses these now-fixed policies:

- inferred Journeys require converging occurrence evidence and a neutral,
  repairable identity;
- prior engagement is not an entrance gate;
- pinning changes access only;
- search returns the target plus no more than three default landmarks;
- raw query reformulations are session-local and expire within 24 hours;
- claim-local source roles survive user editing;
- leaving an ordinary occurred Occasion preserves a frozen historical shared
  core, subject to revocation and safety;
- leaving does not withdraw contributions;
- social suppression follows material dependency, not mere co-occurrence;
- no-directive death expands no audience and creates no synthetic personhood;
- Home receives only complete-value possibilities or explicitly carried
  intentions;
- retrospective push is off;
- dormant intentions do not nag; and
- destination completion returns a receipt, not an invented Outcome.

No fixture remains policy-blocked.

## 2. Entrance-gate execution

`P` means the gate passes for the stated evidence state. `F` means the object
remains governed but cannot use that posture. `C` means the gate is conditional
on the richer evidence described in the fixture.

| Fixture and candidate | Existence | Return identity | Truth | Nonredundant value | Stability | Safe plurality | Repair | Resulting posture |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **L01 Europe Journey, rich** | P | P | P | P | P | P | P | Stable Journey door |
| **L01 Europe Journey, sparse** | P | C | P | C | C | P | P | Searchable Journey candidate or nested period entry |
| **L02 dinner Occasion** | P | P | P | P | P | P | P | Stable lifecycle-aware Occasion door |
| **L03 unused museum ticket** | P | F | P | F | P | P | P | Nested in Journey Plan or search-only |
| **L04 film–Rome bridge** | P | C | P | C | C | P | P | Nested bridge; saved/earned composition may become a door |
| **L05 Rome–Paris comparison** | P | C | P | C | F | C | P | Addressed Together return, never a general stable friend door |
| **L06 Red Hook, one save** | P | F | P | F | F | P | P | Search-only and available to Places context |
| **L06 Red Hook, supported recurrence** | P | P | P | P | P | P | P | Stable longitudinal Place-relationship door |

### Gate findings

1. The index cannot be a list of every valid object. L03, sparse L04, L05, and
   sparse L06 are valuable without independent doors.
2. Truth adequacy is not enough. The unused ticket is highly truthful and
   highly retrievable but still fails independent return value.
3. Social comparison is structurally more volatile than its two constituent
   Journeys. It belongs inside addressed context or a saved composition.
4. The same semantic object may move from search-only to stable door as
   evidence improves; the underlying owner does not change.
5. Stable Life composition requires mixed postures, not one card template.

## 3. Jobs execution by evidence world

### L01 — Europe Journey

| Job | Deterministic result | Status |
| --- | --- | --- |
| **Find** | Tickets, stays, photographs, authored notes, and cultural Sources resolve through Journey order, time roles, Place adjacency, and truth state | CONTRACT PASS |
| **Return** | Supported Occurrences lead; Plan-only, changed, missed, and unresolved segments remain visible but quieter | CONTRACT PASS |
| **See anew** | A transport/terrain reconstruction may explain how actual movement changed reachability; flat itinerary recap and travel-style interpretation are rejected | CONTRACT PASS |
| **Continue** | Current NYC possibility receives supported prior relations and refreshed world truth; it creates no Plan or reminder | CONTRACT PASS |

**Boundary run:** correcting the unused ferry removes it from occurred route and
retains ticket/Plan history. A private photograph excluded from Together still
exists in Mine. Deleting the ferry ticket invalidates ticket-derived claims but
does not erase independently evidenced travel.

**Implementation:** PARTIAL primitives for Sources, Plans, Places, Occurrences,
and canonical artifacts; aggregate Journey, contextual search, invalidation,
and Continue read paths remain absent.

### L02 — Brooklyn dinner

| Job | Deterministic result | Status |
| --- | --- | --- |
| **Find** | Revised time, attributed commitment, receipt, attendance, and shared-core queries resolve without exposing private Outcomes | CONTRACT PASS |
| **Return** | One before/live/after Occasion preserves governed common truth, attributed lanes, and viewer-private overlay | CONTRACT PASS |
| **See anew** | An attributed “what everyone brought” treatment is eligible only when evidence adds structure; “everyone loved it” and homework prompts are rejected | CONTRACT PASS |
| **Continue** | A recipe cue, Place handoff, or proposed new Occasion uses fresh authority and deliberate context reuse | CONTRACT PASS |

**Boundary run:** leaving preserves the frozen shared core visible in the
participant's epoch. It stops later updates and generated social return.
Withdrawing Maya's photo recompiles covers, snippets, and compositions but does
not withdraw her dessert commitment. Unblock restores no grants. Reconciliation
creates a new epoch.

**Implementation:** PARTIAL Occasion, membership, Plan/Commitment, occurrence,
and Outcome primitives; audience epochs, frozen historical projection,
relationship-safety overlay, and derivative recompilation remain absent.

### L03 — Museum ticket not attended

| Job | Deterministic result | Status |
| --- | --- | --- |
| **Find** | Ticket, intended visit, and explicit non-attendance return together | CONTRACT PASS |
| **Return** | Compact Plan-versus-Occurrence truth remains nested in the Journey | CONTRACT PASS |
| **See anew** | No retrospective treatment is generated without present or decision-archaeology value | CONTRACT SILENCE |
| **Continue** | Places may refresh current exhibition/provider truth; historical non-attendance remains unchanged | CONTRACT PASS |

**Boundary run:** `Keep the ticket, but don't bring it up again` preserves
custody and requested retrieval while suppressing automatic return. Deleting
the ticket removes it and unsupported derivatives without manufacturing a
visit or erasing unrelated Rome history.

**Implementation:** PARTIAL Plan/Occurrence distinction; negative occurrence,
stateful Life Map, return-policy compiler, and current-world handoff remain
unproven.

### L04 — Film/book and Rome

| Job | Deterministic result | Status |
| --- | --- | --- |
| **Find** | Film Source, founder observation, Colosseum Encounter, generated article, and citations remain separately retrievable | CONTRACT PASS |
| **Return** | Original Source, human connection, and Vesper contribution remain three distinct layers | CONTRACT PASS |
| **See anew** | `Why Rome needed Troy to lose` is eligible only with external evidence and claim-local provenance; repetition and trivia are rejected | CONTRACT PASS |
| **Continue** | A cited work, Place, or NYC cultural opening may be offered; no mythology identity profile is created | CONTRACT PASS |

**Boundary run:** removing the Colosseum note from future articles preserves the
movie Source and invalidates only note-dependent claims. A heavily edited
article reads `Edited by you · based on a Vesper draft`; claim origins remain.

**Implementation:** ABSENT complete cross-medium relation, claim-local
composition manifest, delayed provenance treatment, and causal regeneration.

### L05 — Rome–Paris comparison

| Job | Deterministic result | Status |
| --- | --- | --- |
| **Find** | Maya's authorized lane and the bounded comparison resolve under current audience and precision | CONTRACT PASS |
| **Return** | Two attributed lanes align around one common axis; neither Journey nor private Outcome is merged | CONTRACT PASS |
| **See anew** | A sourced contrast such as heat adaptation is eligible; coincidence, collage, rankings, and synthetic consensus are rejected | CONTRACT PASS |
| **Continue** | Share preview recompiles from current grants; sending or asking requires explicit authority | CONTRACT PASS |

**Boundary run:** reducing Maya's precision from exact Place to Paris recompiles
Map, search, comparison, export, and Continue. Revocation removes her lane and
degrades to Feihu-only value or silence. A Maya shield suppresses addressed
social return without deleting independent Rome history.

**Implementation:** ABSENT field-level audience epochs, parallel-lane
projection, managed export recompilation, and social-periphery safety traversal.

### L06 — Red Hook across time

| Job | Deterministic result | Status |
| --- | --- | --- |
| **Find** | Saved route, occurred visits, shared dinner, explicit repeat intention, and period query retain distinct states | CONTRACT PASS |
| **Return** | The Place relationship folds constituent episodes without becoming a heatmap, giant album, or identity statement | CONTRACT PASS |
| **See anew** | A reachability reading may compare ferry, bus, walking, companions, weather, and time; recurrence alone is insufficient | CONTRACT PASS |
| **Continue** | Places refreshes ferry, weather, hours, and opportunities before offering a current possibility | CONTRACT PASS |

**Boundary run:** hiding the Maya dinner suppresses the entangled episode and
derived social treatments while preserving Feihu's independent Red Hook
history. A saved-but-unused ferry route never becomes a visit.

**Implementation:** PARTIAL canonical Place and episodic primitives; no
longitudinal Place-relationship projection, truth-state Map, or Life-to-Places
refresh envelope is proven.

## 4. Re-finding benchmark execution

The fifty queries were executed against the policy oracle as authored expected
results. `PASS` means the expected target, truth, authority, orientation,
source identity, repair, Continue, and state-restraint conditions can all be
satisfied without contradiction. It does not mean production retrieval exists.

| Queries | Deterministic lead | Semantic result | Principal implementation gap |
| --- | --- | --- | --- |
| **Q01–Q03** | Ticket/photo/hotel Source or governed identity first | 3/3 PASS | Multi-role time and occurrence-aware retrieval |
| **Q04–Q07** | Compact route/Plan reconstruction or direct answer | 4/4 PASS | Journey graph query and external historical context |
| **Q08–Q10** | Source bundle, change explanation, historical-to-current handoff | 3/3 PASS | Heterogeneous search and refreshed NYC continuation |
| **Q11–Q14** | Attributed commitment/revision/receipt/photo | 4/4 PASS | Occasion union with source authorship and revisions |
| **Q15–Q19** | Contribution lane, attendance truth, shared core, repeat possibility | 5/5 PASS | Viewer-relative Occasion and prospective authority |
| **Q20–Q23** | Unused ticket, intended Tuesday, skipped set, non-attendance answer | 4/4 PASS | Negative occurrence and calibrated missing evidence |
| **Q24–Q26** | Truth explanation, refreshed exhibition, scoped return control | 3/3 PASS | Return-policy mutation and current provider handoff |
| **Q27–Q30** | Film Source, human observation, generated article, governed relation trail | 4/4 PASS | Cross-medium relation and composition retrieval |
| **Q31–Q34** | Claim roles, supporting Sources, scoped release, NYC cultural opening | 4/4 PASS | Claim-local provenance and causal invalidation |
| **Q35–Q38** | Authorized Maya lane and attributed two-city comparison | 4/4 PASS | Audience-epoch and parallel social retrieval |
| **Q39–Q42** | Explicit-share subset, safe policy explanation, share preview, person shield | 4/4 PASS | Relationship safety and action preview |
| **Q43–Q46** | Occurred Place relation, unused route, period episode, repeat intention | 4/4 PASS | Longitudinal Place query with distinct truth states |
| **Q47–Q50** | Occurred visits, sourced reachability explanation, current possibility, scoped hide | 4/4 PASS | Place relationship, current refresh, social exclusion |
| **Total** | Target-first across L01–L06 | **50/50 CONTRACT PASS** | **0/50 production behavior proven** |

### Query-level hard-failure audit

| Hard failure family | Result |
| --- | --- |
| Ticket/save/reservation treated as occurrence | 0 |
| Private or revoked social material exposed | 0 |
| User observation credited to Vesper | 0 |
| Vesper/external claim credited to user after edit | 0 |
| Query refinement persisted as personal meaning | 0 |
| Retrospective possibility promoted to reminder or Plan | 0 |
| Current world truth substituted for historical truth | 0 |
| Psychographic or emotional interpretation inferred | 0 |

The benchmark is semantically coherent. The implementation result remains
**UNPROVEN**, not failed: the required Life aggregate and retrieval service does
not yet exist.

## 5. Social-lifecycle execution

| Transition | Result under accepted policy | Status |
| --- | --- | --- |
| **S01 active** | Shared core plus attributed lanes; private Outcomes stay private | CONTRACT PASS |
| **S02 declined** | Invitation truth remains; no participant or memory state | CONTRACT PASS |
| **S03 deferred** | Uncertainty remains; no attendance or relationship inference | CONTRACT PASS |
| **S04 leaves** | Frozen historical shared core; no later updates or generated return | CONTRACT PASS |
| **S05 withdraws contribution** | Scoped derivative recompile; unrelated contributions remain | CONTRACT PASS |
| **S06 deletes Source** | Causal invalidation; no paraphrase leakage | CONTRACT PASS |
| **S07 narrows audience/precision** | Viewer-relative re-render across Map, search, composition, export, Continue | CONTRACT PASS |
| **S08 blocks** | Dependency-bounded social suppression; independent history remains | CONTRACT PASS |
| **S09 estrangement** | No inferred state; explicit return controls only | CONTRACT PASS |
| **S10 unblocks** | Safety overlay removed; no authority restored | CONTRACT PASS |
| **S11 reconciles** | New epoch and new grants; old compositions stay closed until recompiled | CONTRACT PASS |
| **S12 account deletion** | Product exclusion and dependency invalidation; others' independent state remains | CONTRACT PASS |
| **S13 verified death** | Directive governs; otherwise freeze with no audience expansion or synthetic personhood | CONTRACT PASS |
| **S14 export** | Managed artifact recompiles/closes; screenshots remain uncontrollable | CONTRACT PASS |

All fourteen transitions have a deterministic policy result. Production
coverage remains **ABSENT** for full audience epochs, safety overlays,
dependency invalidation, managed exports, and posthumous state.

## 6. Cross-world findings

### 6.1 One stable spine, several subordinate return modes

The six worlds converge on a stable, period-and-episode index. They do not
support Timeline, Map, People, Library, and generated stories as five competing
home pages. Those are lenses or bounded regions over one corpus.

### 6.2 Sources must be available everywhere but lead almost nowhere

Sources answer many Find queries and support every composition. They usually
remain nested under an episode, relationship, or search result. Their abundance
does not justify an artifact feed or primary Library metaphor.

### 6.3 Active and historical state need one object, not two surfaces

L02 proves that an Occasion should move from upcoming to live to happened
without creating a second memory object. L01 proves that a Journey can contain
planning, lived, and corrected state without becoming a reconstructed perfect
itinerary.

### 6.4 Longitudinal relationships are earned projections

L06 supports a cross-episode Place doorway only after recurrence and meaningful
relations pass the entrance gates. The same logic may later support practices
or threads; it does not authorize an inferred identity graph.

### 6.5 Dynamic value needs a bounded return region

L04 and L05 show why generated compositions can be valuable but volatile.
They should appear in an explicitly derived return region or inside their
episode—not intermixed with stable occurrences in one chronological stream.

### 6.6 Continue belongs at the object boundary

Every fixture needs Continue, but no fixture needs a global Life task queue.
The valid action appears beside the relevant episode, Place, Source, or
composition and follows the delivery ladder.

## 7. Requirements that survived all six worlds

### P0 for semantic prototype

1. Life index projection with stable doors, nested/search-only posture, current
   period, active state, and bounded return region.
2. Episode projection spanning several canonical owners without copying them.
3. Contextual target-first search with multi-role time, truth, author, Place,
   person, medium, and landmark retrieval.
4. Viewer scope and current audience/safety compilation.
5. Timeline and Map as contextual lenses with Plan/Occurrence/source-only
   state.
6. Nested heterogeneous Source retrieval and claim-local provenance.
7. Return-policy and suppression compiler.
8. Causal invalidation across compositions and retrieval infrastructure.
9. Continue envelope with current-world refresh, authority tier, and receipt.

### P1 after semantic prototype

- saved composition history and delayed provenance study;
- global People lens;
- authored cross-episode threads;
- managed export lifecycle;
- advanced recurring practices; and
- automatic Place-relationship entrance proposals.

### Still deferred

- public Life profile;
- inferred identity themes;
- universal knowledge graph UI;
- algorithmic social feed;
- completeness, capture, or travel achievements; and
- generated autobiography.

## 8. Verdict

The Life philosophy and policy contract survive all six evidence worlds.
The fixtures also narrow the shape materially:

- the canonical spine is episodes organized in lived periods;
- active state is an emphasis of the same object;
- Timeline and Map are lenses;
- Sources are nested and searchable;
- Together is viewer-relative shared truth, not a social feed;
- longitudinal Place relationships are earned doors;
- generated value lives in a bounded derived region; and
- Continue stays attached to the object whose context and authority justify it.

The next justified artifact is the canonical Life index and episode anatomy.
The next justified engineering work comes only after that anatomy is accepted.
