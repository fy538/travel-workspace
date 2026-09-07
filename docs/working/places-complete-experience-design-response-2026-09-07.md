---
doc_type: working
status: active
owner: founder / Places design lane
created: 2026-09-07
last_verified: 2026-09-07
expires: 2026-10-07
why_new: "Response to the Places complete-experience design handoff of 2026-09-07 - what was drawn in the dedicated Claude Design project, the recommendations on the five decisions, the proposed canon changes, the dependencies engineering still owes, and the one fixture decision taken and flagged."
supersedes: []
source_of_truth_for: []
---

# Places — complete experience design: response

Responds to [the handoff](places-complete-experience-design-handoff-2026-09-07.md).
The work is in the dedicated Claude Design project **Vesper — Places**
(`516a3ea4-00ea-45d4-920c-1c1589a755c5`, a regular project). Nothing below is a
canon amendment or an implementation authorization; every recommendation points
at the phone that is its evidence.

## 1. What was delivered

| Board | What it shows |
| --- | --- |
| `00 - Index` | The assignment, the five situations mapped to boards, the board budget, the fixture decision, the five decisions against the §6.1 baseline, the reference-board catalogue, the completion test |
| `01 - Design System` | Every element the situations may use, at phone width, graded EXISTS / ADAPT / BUILD against the Places renderer families in code; the map grammar with its legend; six new elements (question control, dated event stub, composed possibility, area card, withdrawn line, the collection's end) |
| `02 - A` | The ordinary New York opening: the content-led field, its map form, the map-led alternative on the same evidence, the Print Room opened as a stable place with no dossier, the return, thin supply |
| `03 - B` | "Something Saturday evening": the question visible and editable; the hour leads; the pier as a different evening; what does not fit is said so; the exact occurrence with a labelled external continuation; the return; the question changed as a new set |
| `04 - C` | Through my people: From friends sparse and dense on one semantic map; the Print Room opened with her line, the listing and the reading kept apart; Reply ≠ Ask; a withdrawal; a sub-scope with no supply |
| `05 - D` | Sorrento before arrival: plan view then section; the vertical distinction leads; Dana at city precision, never a pin; the quay walk opened; back to Sorrento, not New York |
| `06 - E` | Taking the hour forward: the private ask with bounded unknowns, the suggestion visibly unsent, the send through the existing arrangement owner and its readback, back to B; for me / with Maya / around the dinner; one bounded practical change |
| `07` | The supply-rich opening and its deliberate widening by area and by time, beside the sparse opening from 02; supply class per unit |
| `08` | The five decisions with recommendations, the keep / adapt / replace inventory, the receiving contract, the proposed canon changes as exact cases and deltas, the unresolved dependencies, the content-cost classes |
| `RA1–RA16`, `RS1–RS5`, `RH1–RH3`, `RE1–RE4`, `RL1–RL2` | Reference boards copied from the five live sibling projects (Home & Places, Social Aperture, Vesper — Home, Entity Object Handoff Lab, Life). Precedent, not adoption |

## 2. The five decisions — recommendations

1. **Default composition.** Content-led field with the map one tap away. Map-led earns the first viewport only when orientation is the job (an unvisited scope, a spatial question). No mandatory crown; one lead, a small contrasting set, then the collection ends and names its widenings. Evidence: 02 phones 1 and 3 on the same evidence; 05 phone 1; 07.
2. **Spatial interaction.** Map and field share one result set and revision; the toggle preserves question, scope, set and position; panning is inspection. A change of city, question, time or friends scope is deliberate, establishes a new set, and the page says so. Out-of-window material stays on the map in ghost ink with its reason. Evidence: 02 phone 2; 03 phones 2 and 5; 05 phone 4.
3. **Content forms.** Pins are one expression. New forms: the dated event stub (series ≠ occurrence), the area card, the composed possibility that says Vesper composed it, the question control, the withdrawn line, the collection's end. Findings stay bare; shares and sendable things are cards. Evidence: 01; 02–07.
4. **Social receiving.** From friends is a scope the person chooses; the original material leads with no preamble; enrichment only where it adds one fact. Outside the scope, one friend line may sit inside the place it is about. Reply to a person and Ask Vesper have distinct recipients; neither auto-sends. Withdrawal is a local honest line; no-supply names the scope; never an invite ending. Evidence: 04; 07 phone 1.
5. **Continuation.** Open the existing destination (the entity page, the exact occurrence, the reading, the route); provider continuations are labelled external. Return restores scope, question, form, selection and position. Sending an idea goes through the existing arrangement owner and reads back once; nothing is duplicated into Home or Life for having been viewed. Evidence: 02, 03, 05, 06.

## 3. Proposed canon changes (exact case and delta; on 08)

- **C1** Finite first collection with deliberate widening replaces "this is all of it today" as a ceiling (anatomy §2.5 / §9.4).
- **C2** Add the dated event stub as a Places kind; series and occurrence are distinct objects. A kind admission is a canon event.
- **C3** The composed possibility renders as one and says so; never an advertised event or an arrangement.
- **C4** The question is a visible, editable control; clearing returns to the parent scope; a changed question is a new set, said so.
- **C5** Out-of-window material stays visible in ghost ink with its reason and an alternative time named.
- **C6** Social anatomy unchanged; the withdrawn line and the friends no-supply line become required treatments; one friend line may sit inside a place outside the friends scope.
- **C7** Content-led by default; map-led earned when orientation is the job.

## 4. The fixture decision, flagged

The brief supplied a fresh packet (W1–W5, H1, H2). Every other current board runs on the shared fixture world. Situations C, D and E cross into Home and Life, so this project mapped the packet onto that world: W3 is the greenmarket, H1 is Maya, H2 is Dana's existing Sorrento status; the Harbor Print Room and *Rooms Remade*, the Canal Hall listening hour, the waterside pair and the room comparison enter the shared world as new venues. Everything is synthetic. If the packet should stay separate, say so; 02 is the first board to change.

## 5. Dependencies engineering still owes

A pre-Plan suggestion to one person and the thin-guest path (Arrangements) — drawn on 06 as a dependency, not a working button. The `PlacesResultSetRef` producer and consumers (Places backend) — every same-set claim assumes it. Dated-occurrence supply with series identity, freshness and licensing (Content). Provider-specific media and map rights (Content). Practical assessment fresh / stale / unknown (Integration). Route-from-origin needs a chosen origin. Reusable enrichment (the room comparison, the shaded-side finding, the three ways home) is assumed to exist, not to be produced. Reply to a person from a share (Chat / People).

## 6. Handback

- Not verified: rendered native layouts, interactions, accessibility, provider integrations, cost. No board proves live behaviour.
- Not drawn: night and dark; live conditions; a real-data evaluation, which needs a reviewed source packet.
- The board budget held at eight. No new boards should be added without a participant observation or a real-source packet attached.

## 7. Revision after the first-export critique (handoff §8, September 7)

Every board was revised in the order §8.11 asked: 02 and 07, then 04, then 06, then 03 and 05, then 01, 08 and 00; a `09 - Revision Log` board carries the outside-phone change log and a self-assessment against the seven review criteria.

- **§8.2** Internal explanations are gone from every phone. Material uncertainty stays, in the person's words, once; a source line only where it matters to the decision.
- **§8.3** The world packet is twelve things across food, music, outdoor, low-cost social, indoor and one spatial discovery. Three lead candidates are compared on that one packet (02); the recommended lead is a discovery a flat map hides (two piers, two directions), made usable by a free Saturday film. The exhibition is one unit, not the identity of Places.
- **§8.4** World supply is held constant (07): a new account and a mature account see the same twelve things; maturity changes selection and judgment. Thin supply is kept.
- **§8.5** No counts, no ceremonial endings; "Explore" replaces "Widen"; further exploration within the same intent. A Saturday-evening question returns evening options only; exclusions appear only when asked for, selected or relied on. The earlier C5 is withdrawn.
- **§8.6** The control model: header (city, search, map), one question line (a pill with ×, one context chip), a three-row sheet. One interaction sequence on 03: an ordinary constraint, a combined and empty scope, "with Maya" as a context distinct from her shares, clearing. Proposed versus supported is stated: the result-set identity in code carries scope and a query digest, not time or social source.
- **§8.7** Friends as people sharing (04): illustrative pictures and naturally authored notes; eighteen contributions from six people grouped by where; the share opened with an in-place reply; a locally empty scope that keeps the intent; quiet withdrawal with two treatments, one a repair. The "nothing else is recomposed" claim is corrected.
- **§8.8** 06 rebuilt on a coherent baseline (the hour is one recording heard whole, 7–9; dinner is 8:15). The answer names the overlap and what leaving early costs, offers three real ways including doing less, and asks one question. Chat, one send, back. One genuine change (last orders at 9) with what got worse, what stands and the one decision. One lens inside the phone; the three-lens comparison outside.
- **§8.9** Supporting text 14/19 and meta 11 inside Places phones, flagged as a token proposal; dates and prices in readable sans; illustrations on leads and shares; a first-viewport marker beside the phone; long-names and 1.3× tests. 05 leads with one usable orientation sentence and five things to do; distance and time kept apart; Dana's note unglossed.
- **§8.10** 08 rewritten as a proposal record: the result-set builder verified in code (`backend/places/result_set.py`: scope + query, parent set, revision hook; consumed by map, search, sections, collections); labels corrected (the social renderer exists as a sentence strip; the receiving view does not); the dated event reclassified as a visual treatment with representation to verify; every change categorized as consumer copy, interaction decision, data/contract gap, engineering task, token proposal or content supply; supply classes carry refresh responsibilities; the seat rule drawn as two expressions, not hidden content.

**Still open:** the map-led versus content-led comparison on the same rich and sparse evidence (scheduled next; content-led remains a hypothesis); the token proposal; the dated-event representation; the arrangements dependency for a pre-Plan message to named people; real pictures in place of illustrations; a real-source packet before any real-data evaluation.
