"""Vesper — Social Experience: 00 Start here, 01 Checkpoint 1 (cast, ledger, sequence; no phones). Revised after the founder's Checkpoint 1 review."""
import os, sys, json
HP = '/private/tmp/claude-501/-Users-feihuyan-Documents-Claude-travel-workspace/2f24dc15-f019-4b4a-9608-e0e947e79ef9/scratchpad/hp'
sys.path.insert(0, HP)
from kit import *
from gen_generous import head, N, FOOT
from gen_merge import tbl, blk
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out'); os.makedirs(OUT, exist_ok=True)
HJ = os.path.join(OUT, 'heights.json')
def hh(k, d=0):
    try: return json.load(open(HJ)).get(k, d)
    except Exception: return d
STAMP = 'SHARED PACKAGE VDL-STAGE1 0.4.1 CONSUMED &middot; 2026-09-11'
FOOT2 = FOOT + ' &middot; THE WRITTEN DOCS ARE CANON; THE SIBLING PROJECTS ARE INSPIRATION &middot; SHARED FIXTURE LEDGER: docs/working/fixtures/shared-fixture-world-2026-09-07.md'

def sheet(w, h, kick, ttl, sub, inner):
    return (HEAD + f'<div style="width: {w}px; min-height: {h}px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head(kick, ttl, sub) + f'<div style="display: flex; flex-direction: column; gap: 34px;">{inner}</div>'
            + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOT2}</div></div>' + TAIL)

def two(a, b, wa=0.5):
    return f'<div style="display: flex; gap: 46px; align-items: flex-start;"><div style="flex: {wa};">{a}</div><div style="flex: {1-wa};">{b}</div></div>'

def tag(t, c=GOLDD, bg='rgba(176,133,58,0.10)'):
    return f'<span style="{MONO} font-size: 9px; font-weight: 700; letter-spacing: 1px; color: {c}; background: {bg}; border-radius: 4px; padding: 2px 6px; white-space: nowrap;">{t}</span>'
ROLE = {'NORA': (UMBER, 'rgba(74,52,40,0.10)'), 'MAYA': (INK, 'rgba(27,23,20,0.08)'), 'SAM': (PLAN, 'rgba(61,112,80,0.12)'), 'DANA': (OX, 'rgba(122,46,46,0.10)'), 'NOTE': (MUTE, 'rgba(110,104,98,0.10)'), 'BOTH': (GOLDD, 'rgba(176,133,58,0.14)')}
def thumb(n, role, root, what, ending, copy_of=None, branch=None):
    rc, rb = ROLE[role]
    src = f'<div class="fn" style="color: {ANCHOR}; margin-top: 4px;">COPY OF {copy_of}</div>' if copy_of else ''
    br = f'<div class="fn" style="color: {OX}; margin-top: 2px;">BRANCH &middot; {branch}</div>' if branch else ''
    dash = 'border: 1px dashed rgba(27,23,20,0.25); background: transparent;' if role == 'NOTE' else f'border: 1px solid rgba(27,23,20,0.10); background: {CARD};'
    return (f'<div style="width: 172px; flex: none; border-radius: 8px; {dash} padding: 10px 12px 12px 12px; display: flex; flex-direction: column; gap: 6px; min-height: 150px; box-sizing: border-box;">'
            f'<div style="display: flex; gap: 6px; align-items: center; flex-wrap: wrap;"><span style="{MONO} font-size: 10px; font-weight: 700; color: {MUTE};">{n}</span>{tag(role, rc, rb)}{tag(root, MUTE, "rgba(27,23,20,0.06)")}</div>'
            f'<div style="font-size: 12.5px; line-height: 17px; color: {INK};">{what}</div>'
            f'<div style="{SERIF} font-style: italic; font-size: 13px; line-height: 17px; color: {INK2}; margin-top: auto;">{ending}</div>{br}{src}</div>')

def strip(items):
    return '<div style="display: flex; gap: 12px; flex-wrap: wrap;">' + ''.join(thumb(*i) for i in items) + '</div>'

def seq(rows):
    return tbl(['STEP', 'ACTOR', 'ENTRY / CONTEXT', 'GESTURE', 'IMMEDIATE VALUE', 'AUDIENCE / EFFECT', 'OWNER', 'RECIPIENT VIEW', 'RETURN / ENDING'], rows)

# ───────────────────────────── 00 · Start here ─────────────────────────────
CAST = [
    ['<b>Nora</b>', 'The account. Home&rsquo;s Persona B for this fixture, back in New York since Sunday Sep 6 after Nice &rarr; Sorrento &rarr; Amalfi &rarr; Rome. Curious about cooking something from the trip', 'Account', 'Trip photographs, kept selectively; the ferry and Rome tickets; Thursday&rsquo;s pasta attempt and her question; the pasta-night invitation; her Saturday constraint; a private memory of the boat couple'],
    ['<b>Maya</b>', 'Nora&rsquo;s friend', 'Account', 'A1 the Print Room photo (friends, Thursday); A2 the Paris evening note (to Nora, Wednesday); B2b her afternoon-stop suggestion, authored to Nora for the dinner; C1 the table photograph, contributed Saturday night'],
    ['<b>Dana</b>', 'A friend, in Sorrento all week', 'Account', 'A3 a city-level Status, her choice of expiry; B2a a dish photo and one tip, deliberately offered to the dinner&rsquo;s named audience; not attending; no address, no guest list'],
    ['<b>Sam</b>', 'Nora&rsquo;s coworker; new to this circle', '<b>No account</b> &middot; a link', 'His answer; B2c &ldquo;must leave by nine&rdquo; in his own words; B2d his Saturday arrival update; C1 the photo he receives later; C5 his side of the ongoing-connection choice'],
    ['<b>The couple from the boat</b>', 'Met once on the Sorrento &rarr; Amalfi ferry, August', 'None', 'Nothing. Nora holds one promised photo and, in the leading branch, an email address written on a ferry receipt'],
]
EXPS = [
    ['<b>A &middot; A little of your world</b>', 'Ordinary human presence, a particular perspective, useful access to a place', 'Ask privately, reply, keep where permitted, or explore', 'Enjoy it and leave'],
    ['<b>B &middot; An easier way to get together</b>', 'A concrete, appealing possibility and clear participation', 'Invite, join, contribute, adapt, meet offline', 'Decline, remain undecided, or join only one part'],
    ['<b>C &middot; Something stays with us</b>', 'A photo I missed, an identifiable shared occasion, a promised continuation, an optional ongoing connection', 'Refinding, a bounded exchange, another occasion, or choosing to remain connected', 'Keep a legitimate record without more contact'],
]
ENTRIES = [
    ['A photo and a question in Chat', 'Nora, Thursday', 'A0 &middot; private first; sharing is a separate, deliberate gesture afterwards'],
    ['A friend&rsquo;s share in Places &middot; From friends', 'Nora, Thursday', 'A1 &middot; receive and leave is complete'],
    ['A link outside the app', 'Sam, Friday', 'B2 &middot; value before adoption; no profile'],
    ['One sentence to Vesper', 'Nora, Thursday', 'B1 &middot; host once; a preview per recipient; one Send'],
    ['A narrow way to contribute, from elsewhere', 'Dana, Friday', 'B2a &middot; her gesture and its result, not a tip that magically arrives'],
    ['Home&rsquo;s addressed region', 'Nora, Sunday', 'C1 &middot; the photo she never took arrives once'],
    ['Life &middot; People', 'Nora, later', 'C2 &middot; the evening, found through more than one lens'],
]
LEGEND = [
    ['RULED', 'Binding canon from a decision record or kernel ruling. Cited, never redrawn differently', 'Seven sentences (Plans); Home social split; Life behavior sequences; contribution contract T0/T1/T2'],
    ['GIVEN', 'A compatible sibling proposal reused as a bounded fixture assumption (handoff &sect;3). Not re-proposed here', 'Places C6, C7; Home&rsquo;s sequence form and one Chat aperture per page'],
    ['AVOIDED', 'An open sibling proposal this project routes around, or a reference behavior the review excluded', 'Places C2/C3 event kinds; &sect;11.16 and rule A vs B; R5&rsquo;s automatic &ldquo;used in tonight&rdquo;; R9&rsquo;s reporting a private Keep or auto-rebinding a link; consumer-facing MAY-USE wording'],
    ['PROPOSED', 'This project&rsquo;s own recommendation. Goes back to a root project as a delta in board 07', 'Every recommendation on boards 02&ndash;05; the ongoing-connection default (C5)'],
    ['FIXTURE', 'Invented for the boards; recorded in the shared ledger; never a product fact or a grant', 'Every person, date, place, message, photo and world condition; the scoped source-use assumption on A1'],
    ['DEPENDENCY', 'A capability the experience assumes and the app does not have; annotated outside the phone, never drawn as a working button', 'Guest delivery without an account; Sam&rsquo;s later photo access; Dana&rsquo;s contributor path; the boat couple&rsquo;s contact path; C5 connection defaults'],
]
BOARDS = [
    ['00 &middot; Start here', 'Promise, cast, the three experiences, entry points, legend, index', 'This board &middot; revised after the review'],
    ['01 &middot; Checkpoint 1', 'Calendar, the ledger with audience, expiry and grants, drift and what wins here, the two content specimens, the three sequences with role-labelled thumbnails, the 24-slot allocation, what each person gains, remaining dependencies, the six decision pairs', 'REVIEWED &middot; corrections incorporated &middot; Checkpoint 2 drawn'],
    ['02 &middot; A little of your world', '7 phones: the private Ask, the deliberate share, the friends scope (copy of R1), the Print Room opened, Reply in context, Ask Vesper, the sender&rsquo;s return', 'SHARED 0.4.1: 02.4 and 02.5 restore the Print Room drawing and the selected order, original to Reply to gallery notes to Priya to private Ask; recipient choice and reply result on Notice'],
    ['03 &middot; An easier way to get together', '8 slots: host once, Sam&rsquo;s link, Dana&rsquo;s contribution, Friday&rsquo;s contributions, the change (unadopted, then the adopted branch), arrival, one offline note', 'SHARED 0.4.1 (InviteCard unchanged since 0.3): 03.1 on InviteCard host, 03.2 on InviteCard guest; the first-host inset; the fair-baseline work account'],
    ['04 &middot; Something stays with us', '9 slots: Maya&rsquo;s gesture, the arrival, Sam&rsquo;s later photo, the record, one retrieval, the ongoing-connection choice from both sides, the boat email, withdrawal', 'SECOND PASS: the table photograph is 8:25, after Maya arrives at eight; 04.8 names what the previous evening supplies and what it does not'],
    ['05 &middot; The important alternatives', '12 frames, one pair per decision D1&ndash;D6, reusing main-route states; each pair carries one recommendation and its cost', 'SHARED 0.4.1: D7-A restored like 02.4, so both sides carry the drawing; matched inputs unchanged; 13 frames = UNRESOLVED SCOPE DISCREPANCY'],
    ['06 &middot; Connected route', 'Linked frames, one route per participant, with an action &rarr; result &rarr; return map and the branches labelled', 'SEPTEMBER 8: routes point only at each person&rsquo;s own views; participation-versus-arrangement branch; board 08 linked'],
    ['08 &middot; Continuations', 'Five slots beyond the twenty-four: a friend&rsquo;s original without a place, received, opened and found again (08.1&ndash;08.3); where Sam returns after both chose connection (08.4&ndash;08.5); the placement proposal', 'SECOND PASS: receiving wording agreed with Life 07.7 / 07.8; the asset gap named on every plate; five slots over the ceiling = UNRESOLVED SCOPE DISCREPANCY'],
    ['09 &middot; Sending, access and control', '7 slots: one eligible recipient resolved and corrected, the preview and Send, the result; the sender&rsquo;s own edit and withdrawal with what survives it; the four supported controls and their effects; the guest access step, conditional', 'NEW &middot; SEPTEMBER 12 COVERAGE ASSIGNMENT &middot; POLICY PROPOSED, NOT ADOPTED'],
    ['10 &middot; Photos, sent and received', '5 slots and one matched comparison, on Life&rsquo;s fixture set: Nora selects two of her pasta-night pictures in the evening&rsquo;s record, previews and sends them to Maya; Maya receives the pair whole on Home, opens it and returns, and finds it later in Life without replying', 'SEPTEMBER 21 EXPORT REVIEW: 10.1 IS LIFE 04b.11&rsquo;S GENERAL SELECTION (SHARE-SPECIFIC MODE AS AN INSET); THE PREVIEW NAMES THE ITEM LEFT OUT; EACH ENDING RETURNS BY OUTCOME; 10.6 TITLES SURVIVE A MISSING HALF; THE SET IS A BOUNDED PROPOSAL &middot; STILL NO APPROVED PHOTOGRAPHS'],
    ['10P &middot; Photo exchange, simulated', 'A stateful prototype: tap tiles to change a mixed selection, type the optional line, Share, Not now or a simulated Send; each outcome follows the one rule (general selection vs pending send), and the delivered log shows nothing is sent twice; Maya&rsquo;s Home to the viewer and back', 'SEPTEMBER 21 SECOND EXPORT REVIEW &middot; THE OUTCOME RULE OFFERED TO LIFE 04c &middot; A SIMULATION: NOTHING IS SENT'],
    ['07 &middot; Decisions and return to the app', 'The recommended composition, the six decisions, accepted vs proposed, the source and cost ledger, dependencies from the capability map, ten root deltas', 'SHARED 0.4.1: what each frame consumes at which version, the missing variants, the coverage follow-through; both budget discrepancies'],
]
SHELF = [
    ['R1', 'Places 516a3ea4 &middot; 04 - C - Through My People &middot; 09-07', 'The share card; three registers on the opened place; Reply to Maya vs Ask Vesper; the withdrawal line; the no-supply line; the Elsewhere doorway. Keep its warm ordinary material and contextual Reply', 'C6 treatments PROPOSED'],
    ['R2', 'Places 516a3ea4 &middot; 06 - E - Taking It Forward &middot; 09-07', 'Prepared-not-sent card; readback once; a bounded live change; three lenses', 'Send door is a marked dependency'],
    ['R3', 'Life e72a2fd2 &middot; 07 - The people in my life &middot; 09-06', '&ldquo;What each person added&rdquo;; quiet arrival; optional reply; withdrawal wording; &ldquo;nothing owed&rdquo;', 'Assumes a long shared record'],
    ['R4', 'Life e72a2fd2 &middot; 03b - Inside a record &middot; 09-06', 'Three doors to one object; the pass at full size; Back returns to the door used', 'Sibling-night ruling not founder-ruled'],
    ['R5', 'Entity dd48304b &middot; 04 - The People Slot &middot; 09-03', 'Byline, inline citation, on-tap sheet; one look for every absence', '<b>Do not inherit</b> the automatic &ldquo;USED IN TONIGHT &middot; she can see this use&rdquo;; a chosen reply is not use reporting'],
    ['R6', 'Entity dd48304b &middot; 12 - Useful Edges &middot; 09-04', 'Three distinct effects behind a face; the honest handoff interstitial', '&ldquo;Keep her words&rdquo; has no receipt in code'],
    ['R7', 'Plans cd2e1f82 &middot; 04 C - A Shared Afternoon and Dinner &middot; 09-04', 'Host sentence &rarr; recipient preview &rarr; one Send; the guest link page; partial attendance; a non-attending contribution', 'Guest delivery without the app is open (Q9)'],
    ['R8', 'Plans cd2e1f82 &middot; 11 Continuations &middot; 09-05', 'Reply vs Ask labels; the tradeoff stated without agreement; the morning after; reactivation by reference', 'I1 proposal door PROPOSED'],
    ['R9', 'Aperture fac2051b &middot; Ambient 8 - The Map as the Invite &middot; 09-02', 'The scoped-link grant sentence; guest page order; reciprocity never prompted', '<b>Do not inherit</b> reporting a recipient&rsquo;s private Keep, or auto-rebinding a bearer link to a new account. NON-CANONICAL'],
    ['R10', 'Home 42876b8c &middot; 11 - Return and Continuity &middot; 09-06', 'The one open chair; since-you-looked rows', '<b>Do not inherit</b> consumer-facing MAY-USE / precision-policy wording. PROPOSED'],
    ['R11', 'Home 42876b8c &middot; 02 - Persona A - The New Yorker &middot; 09-05', '<b>The full-scroll Home baseline</b> for 03&rsquo;s Saturday afternoon (Sunday or Monday phone, social units substituted)', 'Copy, not redesign; stamp the source'],
    ['R12', 'Places 516a3ea4 &middot; 02 - A - The Ordinary Opening &middot; 09-07', '<b>The full-scroll Places baseline</b> alternative to R1 for 02&rsquo;s friends scope', 'Copy, not redesign; C7 PROPOSED'],
]
def start_here():
    promise = blk('THE QUESTION', N('<b>Does Vesper make it easier and more enjoyable to share a little of life, receive something worthwhile through another person, and spend time together, without making either person maintain a social system?</b>'
        '<div style="margin-top: 10px;">The social expression of the product: <i>see a little more of your friends&rsquo; worlds, find something worthwhile through them, and make it easier to do something together.</i> One social world, not one mandatory social journey. Seeing a friend&rsquo;s photo, joining a meal and reconnecting later are each independently worthwhile; none must graduate into the next.</div>'
        '<div style="margin-top: 10px;"><b>Direction after the review:</b> reduce the work around human intention; preserve the human intention. Low pressure is not the absence of meaning: a casual photo can ask nothing, an invitation can clearly need an answer, an accepted arrangement carries real responsibilities. Unequal contribution is normal, but the host must not do everyone else&rsquo;s administration. The distinction to demonstrate once, with real substance, is the combination of human perspective, relevant world understanding, practical assistance and legitimate continuity; ordinary receiving must also work with none of it.</div>'
        '<div style="margin-top: 10px;"><b>Three effects, no three setup workflows:</b> this material is shared with you; this occasion includes you; we choose to remain connected. Accepting a connection enables only a named future capability, never past material, location, availability or automatic inclusion. Someone can reduce what they receive without publicly rejecting the relationship.</div>'))
    cast = blk('THE CAST &middot; FROM THE SHARED FIXTURE LEDGER', tbl(['PERSON', 'WHO', 'VESPER', 'WHAT THEY HOLD IN THIS WORLD'], CAST))
    exps = blk('THE THREE INDEPENDENT EXPERIENCES', tbl(['EXPERIENCE', 'WHAT MAKES IT WORTH OPENING', 'WHAT CAN HAPPEN NEXT', 'AN EQUALLY VALID ENDING'], EXPS))
    entries = blk('ENTRY POINTS &middot; NONE TRAVERSES EVERY ROOT', tbl(['ENTRY', 'WHO, WHEN', 'WHAT IT PROVES'], ENTRIES))
    legend = blk('SOURCE AND AUTHORITY LEGEND &middot; EVERY FRAME CARRIES ONE', tbl(['STAMP', 'MEANING', 'EXAMPLES HERE'], LEGEND))
    boards = blk('BOARDS', tbl(['BOARD', 'WHAT IT HOLDS', 'STATUS'], BOARDS))
    shelf = blk('THE REFERENCE SHELF &middot; COPIED, NOT LINKED &middot; TWELVE BOARDS', tbl(['#', 'SOURCE PROJECT &middot; BOARD &middot; DATE', 'WHAT IS REUSED', 'CAUTION'], SHELF))
    budget = blk('THE BUDGET &middot; A HARD CEILING', N('<b>24 storyboard slots</b> on the recommended route across boards 02&ndash;04, offline notes included, each with a role label and an ending. <b>12 comparison frames</b> on board 05, reusing main-route states. <b>Linked frames</b> only on 06. After the review the allocation is 14 Nora, 3 Maya, 5 Sam, 1 Dana, 1 offline note: repeated host previews, the readback and the second retrieval were given to Dana contributing, Maya contributing the photo, Sam receiving it later, and the ongoing-connection choice from both sides. If coverage still does not fit, the exact tradeoff is reported on board 01, not hidden. September 8 added board 08&rsquo;s five continuation slots, September 12 added board 09&rsquo;s seven sender, access and control slots and September 21 added board 10&rsquo;s five photo slots, each at the assignment&rsquo;s request, so the project holds 41 against a ceiling of 24. Comparison frames: the September 9 second pass added one (05 D7-B, its A side reused from 08.2) and September 21 added three (10.5, the matched D5 treatments of one arrival), so 16 against a ceiling of 12. Both are recorded as unresolved scope discrepancies, not compliance: neither ceiling was amended, and the founder decides whether they move or frames fold.'))
    inner = promise + two(cast, exps, 0.58) + two(entries, legend, 0.42) + budget + boards + shelf
    return sheet(1560, hh('00'), f'VESPER &middot; SOCIAL EXPERIENCE &middot; 00 &middot; START HERE &middot; {STAMP}', 'Vesper &mdash; Social Experience',
                 'One standalone design project for seeing the connective social experience together: three independent situations across Home, Chat, Places, Life and the objects they open, both sides of each exchange, the time between, and the points where the app recedes. The root projects keep their pages; accepted changes flow back as deltas. Everything on every frame is a fixture.', inner)

# ───────────────────────────── 01 · Checkpoint 1 (revised) ─────────────────────────────
CAL = [
    ['Thursday', 'Sep 17', 'Maya&rsquo;s Print Room photo reaches friends. Nora tries a dish from the trip and asks about the sauce (A0). Nora hosts once: the pasta night goes to Maya and Sam (B1)'],
    ['Friday', 'Sep 18', 'Sam opens his link and answers (B2). Dana sends one tip and a dish photo to the dinner&rsquo;s people (B2a). Maya writes her afternoon-stop suggestion to Nora (B2b). Sam says he must leave by nine (B2c)'],
    ['Saturday', 'Sep 19', '1:10 pm Nora states her constraint; 1:12 the possibility (&sect;8.2). Afternoon: Maya proposes eight (B4); the recommended branch stays at seven. Evening: dinner from seven at Nora&rsquo;s; Sam expected around seven-thirty (B3). Maya contributes the table photograph (C1)'],
    ['Sunday', 'Sep 20', 'Nora opens Home: the table photo arrives (C1). Maya&rsquo;s Print Room share reaches its chosen expiry. Branch: Maya takes back her Paris note (C4)'],
    ['Later', '&mdash;', 'Sam receives the photo through his link (C1). Nora and Sam each choose whether to remain occasion-bound or connect (C5). The promised ferry photo to the boat couple (C3)'],
]
LEDGER = [
    ['A1', 'Print Room photo &middot; &ldquo;The side room was my favorite.&rdquo;', 'Maya', 'Friends &middot; place precision', 'Through Sunday, Maya&rsquo;s choice', 'Original viewing. For the Ask comparison only, a hypothetical explicit scoped-use grant for a recipient&rsquo;s immediate private question, labelled a fixture assumption; without it A1 is never sent to the model. No retention, no inference, no onward'],
    ['A2', 'Paris evening note', 'Maya', 'Nora only', 'None; can be taken back', 'Original viewing. A contrast is omitted: no research, no grant'],
    ['A3', 'Sorrento Status; optional dish image', 'Dana', 'Friends &middot; <b>city</b> precision', 'Through the week, Dana&rsquo;s choice', 'A doorway. Never a marker, never availability'],
    ['A4', 'Pasta attempt photo + &ldquo;why did the sauce break?&rdquo;', 'Nora', 'Private Ask (T0)', 'Not retained unless kept', 'The answer is written (&sect;8.1). A later share carries the photo and at most her own line'],
    ['B1', '&ldquo;Pasta trial night at mine Saturday at seven. Invite Maya and Sam. Sam can come at seven-thirty; nothing to bring.&rdquo;', 'Nora', 'Maya (full); Sam (dinner only, a link by text to a number Nora typed); the exact address in Maya&rsquo;s view at once and in Sam&rsquo;s only after a one-time code to that number (branch V)', 'The evening', 'When, where, who; nothing else of Nora&rsquo;s. Sam gains nothing of the friends audience'],
    ['B2a', 'Dana&rsquo;s tip + dish photo', 'Dana', 'Deliberately offered to the dinner&rsquo;s named audience; she is not an attendee, gets no address and no unrelated guest material', 'Dinner record only, under her grant', 'Her entry and her send are drawn. A narrow contributor path is a fixture proposal, not a discovered path'],
    ['B2b', 'Afternoon-stop suggestion: &ldquo;the side room empties after four and the shop shuts at five&rdquo;', 'Maya', 'Nora as arrangement owner', 'Current arrangement', 'A suggestion, not an accepted edit; independent of A1 and A2; it is the authored place knowledge in &sect;8.2'],
    ['B2c', '&ldquo;Must leave by nine&rdquo;', 'Sam', 'Nora, for coordination; no private reason disclosed', 'Current coordination', 'May inform the prepared tradeoff; authorizes no new time and nobody&rsquo;s acceptance'],
    ['B2d', 'Saturday arrival update', 'Sam', 'Nora, for arrival; no presence broadcast', 'Arrival window', 'An authored update, not permission to track'],
    ['B4', 'Maya proposes eight', 'Maya', 'Nora, as owner', 'Until answered', 'The recommended branch stays at seven in every view. The adopted branch is labelled separately: owner-applied revision, only the relevant recipient consequence, nobody&rsquo;s acceptance invented'],
    ['C1', 'The table photograph', 'Maya', 'The dinner&rsquo;s agreed audience, subject to affected-person rights', 'Displayed through Sam&rsquo;s verified link as long as Maya leaves it; the evening&rsquo;s details close Sunday', 'Branch V: Sam confirmed his number for the address; the same principal sees the photo. A send to others is a T2 boundary carried by the one Send. DEPENDENCY outside the phone'],
    ['C3', 'The promised ferry photo', 'Nora', 'The boat couple, by the supplied path', 'One send', 'Email leads; no-path is the valid alternative. Its own record in Life People, linked, never nested in the dinner'],
    ['C3&prime;', 'Another pasta evening: &ldquo;dinner with maya and sam again? saturday the 3rd&rdquo;', 'Nora', 'Maya and Sam, by fresh invitations', 'The new occasion, on Send', 'A private draft carries the place and a proposed start; old personal timings stay history; their fresh answers decide; she may leave the draft'],
    ['C4', 'Withdrawal', 'Maya', '&mdash;', 'Sunday', 'Removes A2 and what derived from it; A1, B2b, C1 and everything held independently stay; no paraphrase'],
    ['C5', 'Optional ongoing connection, sought by Sam under Nora&rsquo;s name (never appended after a photo)', 'Nora and Sam, each choosing', 'Share things and invite each other again; audiences still chosen per share', 'Revocable', 'Separate from invitation, RSVP and the photo. Branch V: Sam&rsquo;s verified number is the principal. Remaining occasion-bound is complete; leaving it is fine'],
]
DRIFT = [
    ['Saturday Sep 19', 'Home: Maya and Alex, restaurant, 8:15; Alex&rsquo;s birthday. Plans: the Georgian room, Court Street, seven. Life: &ldquo;you hosted&rdquo;, Maya&rsquo;s table photo, Alex&rsquo;s receipt. Entity: Hortus, the founder&rsquo;s real dinner', '<b>Pasta night at Nora&rsquo;s home, seven; Maya and Sam.</b> The restaurant variants are not drawn; Alex is absent'],
    ['Nora / Nadia', 'Home: Persona A is Nadia; Persona B unnamed. Plans: the host is Nora', '<b>Nora = Home&rsquo;s Persona B for this fixture.</b> Nadia is a different person, absent. A fixture choice, not personal history'],
    ['Dana', 'Home: lands Saturday the 19th (Persona A&rsquo;s world); Sorrento status. Aperture: &ldquo;two Danas&rdquo;', '<b>In Sorrento all week; contributes remotely; does not land</b>'],
    ['Maya&rsquo;s shares', 'Home: bakery, noodle bar, Red Hook. Life: shared record since 2019; Paris note withdrawn Wednesday', '<b>Print Room photo Thursday; Paris note Wednesday; withdrawal is a Sunday branch.</b> Bakery and Red Hook absent'],
    ['The boat couple', 'Life: &ldquo;Rome, met once&rdquo;', '<b>The Sorrento &rarr; Amalfi ferry, August</b>'],
    ['The live change', 'Home: a flight delayed. Plans: dinner to eight; the table still booked for seven', '<b>Maya proposes eight; Sam must leave by nine; no reservation exists</b>'],
]
SPECIMEN = [
    ['&sect;8.1 The cooking answer (A0)', 'Photo of a grainy, split cheese sauce + &ldquo;why did the sauce break? this was the Sorrento one&rdquo;', '&ldquo;Too much heat is one possibility; the photograph alone cannot confirm it. For the next attempt: off the heat, a ladle of the starchy water first, then the cheese in small handfuls, stirring until it turns glossy. That gives you one concrete thing to change.&rdquo; (Revised September 9: one possible cause, not a diagnosis from a photograph; no guarantee about Saturday&rsquo;s batch.)', 'SYNTHETIC TECHNIQUE &middot; NO LIBRARY &middot; T0 &middot; NOTHING KEPT &middot; no save prompt, no share prompt'],
    ['&sect;8.2 The Vesper-added payoff (A3 / D5)', 'Maya&rsquo;s authored suggestion to Nora for the dinner (&ldquo;the side room empties after four and the shop shuts at five&rdquo;) + Nora&rsquo;s own constraint (&ldquo;home by six to start the pasta&rdquo;) + listed hours 12&ndash;6, shop till 5 (fixture) + a twenty-minute walk (fixture)', '&ldquo;Print Room at four. Maya says the side room empties after four, and the shop shuts at five, so four to a quarter to five covers both; a twenty-minute walk has you home by 5:10, before the pasta. The cost: it is your only free stretch this afternoon, and Maya cannot join until dinner.&rdquo;', 'MAYA&rsquo;S SUGGESTION (AUTHORED, FOR THIS DINNER) + NORA&rsquo;S WORDS + LISTED HOURS (FIXTURE) + WALK (FIXTURE) &middot; NO A1, NO A2 &middot; claims nothing about quiet, access, availability or Maya&rsquo;s free time'],
]
SEQ_A = [
    ['A0', 'Nora', 'Chat, Thursday 7:50 pm, a photo of the pasta', 'Ask', 'The written answer (&sect;8.1); nothing kept', 'Private (T0); no post, no memory', 'Chat', '&mdash;', 'Done. Or: share the photo, deliberately, with at most her line'],
    ['A0&prime;', 'Maya', 'The Print Room&rsquo;s place page', 'Share', 'Her picture and her words reach the people she chose', 'Friends, through Sunday; a send crosses an audience boundary (T2)', 'Contribution', 'Friends see a photo and a line in their scope', 'Sent once; return restores the place page'],
    ['A1', 'Nora', 'Places &middot; From friends (copy of R1 or R12)', 'Open', 'Maya&rsquo;s photo and five words; Dana&rsquo;s Sorrento doorway; the wider field', 'Nothing is marked viewed; nothing kept by looking', 'Places', '&mdash;', '<b>Enjoy it and leave</b>'],
    ['A1&prime;', 'Nora', 'The Print Room, opened', 'Open', 'Her line; the listing in the unverified register; a reading attributed to the gallery', 'Same', 'Places / Entity', '&mdash;', 'Back to the same scroll'],
    ['A2a', 'Nora', 'The same photo', 'Reply to Maya, in context', 'Her words to Maya in the reference&rsquo;s in-context composer; recipient obvious; no trip to the Chat root', 'Maya only; sends nothing until sent; not a memory', 'Chat (directed)', 'Maya: a message from Nora', 'Back to the photo'],
    ['A2b', 'Nora', 'The same photo', 'Ask Vesper about this', 'A private answer, unmistakably addressed to Vesper, with the object as context under the &sect;8.3 assumption or with world help only', 'Nobody; Maya receives nothing', 'Chat (private)', '&mdash;', 'Return restores the question, form and scroll'],
    ['A4', 'Maya', 'Her own contribution, later', 'Look', 'Her photo is still hers: EDIT, TAKE BACK; a chosen reply if one came', 'No viewer list, no count, no use report, no &ldquo;Nora hasn&rsquo;t replied&rdquo;', 'Contribution', 'Herself', 'Silence needs no explaining'],
]
SEQ_B = [
    ['B1', 'Nora', 'One sentence to Vesper', 'Say it once', 'One frame: what Maya gets and what Sam gets, side by side; one Send', 'Nothing sent yet; readback once is a line on Home, not a phone', 'Occasion (owner: Nora)', 'Two previews', 'Send; or Not yet'],
    ['B2', 'Sam', 'A link, no app', 'Open, answer', 'The character of the evening, who invited him, seven-thirty, the neighborhood, nothing to bring, how to answer', 'A provisional answer; confirmed by the one-time code that also unlocks the address (branch V)', 'Occasion (guest view)', 'Nora: provisional, then confirmed', 'I&rsquo;m in &middot; Can&rsquo;t make it (no reason asked)'],
    ['B2a', 'Dana', 'A narrow contributor path from Sorrento (fixture proposal)', 'Send one thing', 'What she sees: the dinner&rsquo;s name and its people, no address, no guest material; her tip and photo go to the dinner', 'The dinner&rsquo;s named audience; she is not enrolled as a guest', 'Contribution', 'Nora, Maya, Sam see it under the row with her name', 'Done; nothing asked of her'],
    ['B2&prime;', 'Nora', 'Home, Friday', 'Read', 'Dana&rsquo;s tip and photo, Maya&rsquo;s suggestion, Sam&rsquo;s answer and his nine, each under the row with its scope', 'No copy-and-paste step for the host', 'Occasion', 'Each contribution attributed', 'Nothing to do'],
    ['B4', 'Nora', 'Home, Saturday 1:12 pm (full scroll, copy of R11)', 'Read', 'The possibility (&sect;8.2); later, Maya&rsquo;s proposal of eight with the prepared alternative and its cost; one ask', 'Recommended branch: dinner stays at seven in every view', 'Home / Occasion', '&mdash;', 'Leave it: seven stands'],
    ['B4&prime;', 'Sam', 'His link', 'Read', 'BRANCH, adopted: Nora applied eight; one sentence on his row with what it means for nine; everyone at the dinner has the new time', 'Tailored to him; his acceptance is not invented', 'Occasion (guest view)', '&mdash;', 'Answer, or not; then the eight arrival (03.7 variant)'],
    ['B3', 'Sam', 'His link, Saturday evening', 'Open', '&ldquo;Dinner from seven; you&rsquo;re expected around seven-thirty&rdquo;; find the host; nothing to bring; Dana&rsquo;s dish as a foothold', 'Supplied facts only; no navigation, no learning where he goes', 'Occasion (guest view)', '&mdash;', 'Phone away'],
    ['B3&prime;', '&mdash;', 'The evening itself', '&mdash;', 'Storyboard note: arrival, the table, an ordinary departure at nine', 'No app action to leave a dinner', '&mdash;', '&mdash;', '&mdash;'],
]
SEQ_C = [
    ['C1', 'Maya', 'The dinner, Saturday night', 'Contribute the table photograph', 'Her photo to the dinner&rsquo;s people, deliberately; the image itself', 'The agreed audience; her grant; not a post', 'Contribution', 'Nora and Sam, later', 'Done; nothing asked'],
    ['C1&prime;', 'Nora', 'Home, Sunday', 'Open', 'The table photograph arrives once, the image itself', 'A view of one source, not an upload', 'Contribution / Home', '&mdash;', 'Enjoy it; nothing asked'],
    ['C1&Prime;', 'Sam', 'His link, later', 'Open', 'The same photograph, displayed through his verified link as long as Maya leaves it; no separate Keep', 'Branch V: his number was confirmed for the address; the same principal sees the photo. DEPENDENCY outside the phone', 'Contribution (guest view)', '&mdash;', 'Receive without contributing'],
    ['C2', 'Nora', 'Life &middot; People, later', 'Open', 'The dinner as one record: what each person added, theirs; her account, hers alone', 'Nothing narrates what anyone felt', 'Life', '&mdash;', 'Recognition, not maintenance'],
    ['C2&prime;', 'Nora', 'Life search', 'Find', '&ldquo;the photograph Maya sent from that dinner&rdquo;: a door with its containment', 'Retrieval writes nothing', 'Life', '&mdash;', 'Open, or leave'],
    ['C5a', 'Sam', 'His link, after the photo', 'Choose', 'Remain occasion-bound, or offer to stay connected: the exact capability named, nothing else', 'Separate from RSVP, the photo and any account; ignoring is comfortable', 'Relationship (proposal)', 'Nora sees a request, or nothing', 'Bound, or connected'],
    ['C5b', 'Nora', 'Home, later', 'Choose', 'Sam&rsquo;s request as one line; accept enables the named capability only', 'No past material, location, availability or future inclusion', 'Relationship (proposal)', 'Sam sees the answer, or nothing', 'Ignored, declined or accepted are all complete'],
    ['C3', 'Nora', 'Life &middot; the boat couple', 'Send once', 'The promised photo through the supplied email', 'One send; no friend upgrade', 'Contribution', 'An email with one photo', 'Edge case; no-path branch noted'],
    ['C4', 'Nora', 'Life, Sunday', 'Read', '&ldquo;Maya took back her Paris note. Everything else here is as it was.&rdquo;', 'A2 and its derivatives gone; A1, B2b, C1 untouched; no paraphrase', 'Contribution', '&mdash;', 'No new contact; nothing owed'],
]
THUMBS_A = [('02.1', 'NORA', 'CHAT', 'Pasta photo, &ldquo;why did the sauce break?&rdquo;: the written answer (&sect;8.1)', 'Nothing kept. Done.'),
            ('02.2', 'MAYA', 'PLACES', 'Maya shares the Print Room directly from its page: one line, who, Send; no prelude', 'Sent to friends, once.', 'R1'),
            ('02.3', 'NORA', 'PLACES', 'From friends, full scroll: Maya&rsquo;s photo; Priya&rsquo;s three-stop map; the pigeons; Dana elsewhere; Red Hook anyway', 'Enjoy it and leave.', 'R1 / R12'),
            ('02.4', 'NORA', 'PLACES', 'The Print Room opened: her line, the listing, a reading kept apart', 'Back to the same scroll.', 'R1'),
            ('02.5', 'NORA', 'IN CONTEXT', 'Reply to Maya in the in-context composer: her words, the recipient obvious', 'Sent when she sends it.', 'R1'),
            ('02.6', 'NORA', 'CHAT', 'Ask Vesper about this: private; Maya receives nothing; the &sect;8.3 assumption labelled', 'Return restores the scroll.'),
            ('02.7', 'MAYA', 'PLACES', 'Her own share later: EDIT, TAKE BACK; a reply if one came; no viewer list, no use report', 'Silence needs no explaining.')]
THUMBS_B = [('03.1', 'NORA', 'CHAT', 'One sentence; what Maya gets and what Sam gets, side by side; one Send', 'Send, or Not yet.', 'R7 C1'),
            ('03.2', 'SAM', 'LINK', 'The invitation: who, when, seven-thirty, where, nothing to bring', 'I&rsquo;m in &middot; Can&rsquo;t make it.', 'R7 C2'),
            ('03.3', 'DANA', 'CONTRIBUTE', 'From Sorrento: the narrow contributor path; what she sees; her tip and dish photo sent to the dinner&rsquo;s people', 'Done; nothing asked of her.'),
            ('03.4', 'NORA', 'OCCASION', 'Friday: Dana&rsquo;s tip and photo, Maya&rsquo;s suggestion, Sam&rsquo;s answer (provisional, then confirmed) and his nine, each under the row with its scope', 'Nothing to do.'),
            ('03.5', 'NORA', 'HOME', 'Saturday afternoon, full scroll: the &sect;8.2 possibility; Maya&rsquo;s eight with the alternative and its cost; one ask; the rest of Home intact', 'Seven stands.', 'R11', 'RECOMMENDED &middot; UNADOPTED'),
            ('03.6', 'SAM', 'LINK', 'Adopted branch, labelled: Nora applied eight; one sentence on his row and what it means for nine', 'Answer, or not.', 'R8 D8', 'ADOPTED &middot; SEPARATE'),
            ('03.7', 'SAM', 'LINK', 'Saturday evening: &ldquo;expected around seven-thirty&rdquo; on the unchanged route, or eight on the adopted branch (the same frame, parameterized); find the host; nothing to bring', 'Phone away.'),
            ('03.8', 'NOTE', '&mdash;', 'Storyboard: arrival, the table, an ordinary departure at nine', 'No app action to leave.')]
THUMBS_C = [('04.1', 'MAYA', 'OCCASION', 'Saturday night: she contributes the table photograph to the dinner&rsquo;s people, deliberately', 'Done; nothing asked.'),
            ('04.2', 'NORA', 'HOME', 'Sunday: the photograph arrives once, the image itself', 'Nothing asked.'),
            ('04.3', 'SAM', 'LINK', 'Later: the same photograph through his verified link, as long as Maya leaves it; no separate Keep', 'Receive without contributing.'),
            ('04.4', 'NORA', 'LIFE', 'People &middot; the dinner: what each person added, theirs; her account. The boat couple are a separate record, inset', 'Recognition, not maintenance.', 'R3'),
            ('04.5', 'NORA', 'LIFE', 'Search: &ldquo;the photograph Maya sent from that dinner&rdquo;', 'A door, with its containment.'),
            ('04.6', 'SAM', 'LINK', 'Sought under Nora&rsquo;s name on his link: share things and invite each other again; leaving it is fine', 'Bound, or connected.'),
            ('04.7', 'NORA', 'HOME', 'Sam&rsquo;s request as one line; accept enables the named capability only; ignored, declined, accepted all complete', 'Nothing inherited.'),
            ('04.8', 'NORA', 'CHAT', 'Two weeks later: a draft for another evening with the place and a proposed start; the photo one tap away; fresh invitations', 'Send with seven, or leave it.', 'R8 F2'),
            ('04.9', 'NORA', 'LIFE', 'Maya took back her Paris note; everything else as it was', 'Nothing owed.', 'R3')]
GAINS = [
    ['A', 'Nora', 'A useful answer about her own cooking; a friend&rsquo;s view of a place; a place worth knowing', 'Nothing. Sharing is optional afterwards'],
    ['A', 'Maya', 'Her photo seen by friends the way she chose; a reply if one comes', 'Nothing beyond the share she already made'],
    ['A', 'Dana', 'Her status seen as a doorway, at the precision she chose', 'Nothing'],
    ['B', 'Nora', 'A dinner arranged in one sentence; contributions she did not have to ask for; a better afternoon from Maya&rsquo;s knowledge and her own constraint; a prepared alternative when the day changes', 'One sentence, one Send'],
    ['B', 'Sam', 'Understanding the evening, his time, the way there, that nothing is expected; a decline with no reason asked', 'An answer, if he wants dinner'],
    ['B', 'Maya', 'The afternoon and the dinner; her suggestion used where it helps, attributed', 'Nothing; her proposal may stay unadopted'],
    ['B', 'Dana', 'A way to be part of the dinner without attending, in one send, without an address or a guest list', 'One send'],
    ['C', 'Nora', 'A photo she never took; the evening findable; a continuation without re-explaining; an optional connection on stated terms', 'Nothing. No curation, no recap'],
    ['C', 'Sam', 'The photo, later, without uploading one; a choice to stay connected or not, with ignoring comfortable', 'Nothing; his access is a dependency, not a task'],
    ['C', 'Maya', 'Her photograph reaching the people it was for, attributed', 'One photo, deliberately'],
    ['C', 'The boat couple', 'The promised photo', 'Nothing; no account, no graph'],
]
THIN = [
    ['Dana&rsquo;s contributor path (B2a)', 'A fixture proposal: how she legitimately reaches the dinner&rsquo;s contribution context. Drawn as intended; support unverified', 'Engineering maps; design owns what she sees'],
    ['Sam&rsquo;s later photo (C1&Prime;)', 'Intended delivery and any verification drawn at the boundary; identity or delivery support is a dependency, not a footnote', 'Engineering maps'],
    ['The ongoing connection (C5)', 'The exact default capability is a recommendation the designer states on 04 and 07; acceptance is not an all-access audience', 'Design recommends; contract decides'],
    ['The scoped-use assumption (A1, &sect;8.3)', 'Labelled on the one frame that uses it; visibility alone never authorizes model use', 'Contract and runtime mapping'],
    ['Cooking guidance (A0)', 'Written (&sect;8.1); synthetic technique, no library', 'Accepted as fixture'],
    ['The Print Room&rsquo;s world information', 'Fixture hours; rendered in the unverified register', 'Accepted as fixture'],
    ['The Paris / Rome contrast', 'Omitted: no research, no grant', 'Closed'],
]
PAIRS = [
    ['D1 &middot; Sharing into possibility', '<b>Openness:</b> natural language alone (&ldquo;thinking of Saturday&rdquo;, &ldquo;happy for company&rdquo;) vs one optional author-controlled openness affordance; which action establishes participation and under what terms', '2 frames'],
    ['D2 &middot; Acknowledgment', 'Reply only vs Reply plus one warm, voluntary, author-only acknowledgment (tested as warmth, not only &ldquo;Useful&rdquo;); no count, no obligation', '2 frames &middot; recommended by principle; first to observe with a real friend'],
    ['D3 &middot; Friend-aware discovery', 'The value and scope of authored signals (Maya&rsquo;s line and precision, Dana&rsquo;s city status, an authored when) vs their absence; supply variants (one friend, none) as an added condition', '2 frames'],
    ['D4 &middot; Hospitality', 'The arrival frame (03.7) vs invitation-only; what makes Sam practically included without a profile or host work', '2 frames'],
    ['D5 &middot; Enrichment', 'Original-only (reused from 02.3) vs the &sect;8.2 context layer vs a generated-led challenger; conclude where original-only wins', '2 new frames'],
    ['D6 &middot; Continuity', 'Occasion-bounded exchange vs optional ongoing connection (reusing 04.6 / 04.7); the email / no-path branch as an edge case', '2 frames'],
]
def checkpoint():
    status = N(f'<b>Reviewed by the founder on September 7; the corrections are incorporated here and in the ledger.</b> Fixture choices settled without another questionnaire: Nora is Persona B and Nadia a different person; the supplied email leads the boat branch with no-path as the valid alternative; withdrawal removes A2 and its derivatives only; the Paris/Rome contrast is omitted. Corrections applied: Dana contributes on her own frame; Maya&rsquo;s photo contribution is a gesture, not an arrival; Sam receives the photo later on a phone; the ongoing-connection choice is drawn from both sides with a comfortable ignored ending; the live change is two labelled branches with the unadopted one recommended and placed before the evening; the two content specimens are written; the ledger&rsquo;s may-see / may-use ambiguity is resolved; D1, D3 and D6 are reframed. <b>Checkpoint 2 proceeds from this board.</b>')
    cal = blk('THE CALENDAR &middot; SEP 17&ndash;20, 2026 &middot; WEEKDAY AND DATE AGREE', tbl(['DAY', 'DATE', 'WHAT HAPPENS'], CAL))
    ledger = blk('THE LEDGER &middot; EVERY FIXTURE OBJECT WITH ITS AUDIENCE, EXPIRY AND GRANT', tbl(['LABEL', 'OBJECT', 'AUTHOR', 'AUDIENCE &middot; PRECISION', 'EXPIRY', 'ON USE'], LEDGER))
    drift = blk('DRIFT AGAINST THE SIBLING PROJECTS, AND WHAT WINS HERE', tbl(['FACT', 'AS DRAWN ELSEWHERE', 'HERE'], DRIFT))
    spec = blk('THE TWO CONTENT SPECIMENS &middot; WRITTEN BEFORE ANY PHONE &middot; LEDGER &sect;8', tbl(['SPECIMEN', 'INPUTS', 'THE ACTUAL TEXT', 'LABELS OUTSIDE THE PHONE'], SPECIMEN))
    def exp(letter, title, q, rows, thumbs, n):
        return (f'<div style="display: flex; flex-direction: column; gap: 6px; margin-top: 8px;"><div class="kick" style="color: {GOLDD};">EXPERIENCE {letter} &middot; {n} SLOTS</div>'
                f'<div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px;">{title}</div><div style="font-size: 13px; line-height: 19px; color: {MUTE}; max-width: 980px;">{q}</div></div>'
                + blk('THE SEQUENCE &middot; actor &rarr; entry &rarr; gesture &rarr; value &rarr; audience &rarr; owner &rarr; recipient &rarr; ending', seq(rows))
                + blk('THE SLOTS, AS THUMBNAILS &middot; ROLE-LABELLED &middot; NOT YET DRAWN', strip(thumbs)))
    a = exp('A', 'A little of your world', 'Can giving and receiving feel casual while the material opens real value, without a post-production ritual or a demand to act?', SEQ_A, THUMBS_A, 7)
    b = exp('B', 'An easier way to get together', 'Can interest become a real gathering without turning leisure into planning work or making the host an unpaid operator of the app?', SEQ_B, THUMBS_B, 8)
    c = exp('C', 'Something stays with us', 'Does shared life become easier to recover and continue without becoming another archive to curate or a friendship-maintenance obligation?', SEQ_C, THUMBS_C, 9)
    alloc = blk('THE ALLOCATION &middot; 24 SLOTS &middot; REVISED PER &sect;14 AND &sect;15', N('14 Nora &middot; 3 Maya &middot; 5 Sam &middot; 1 Dana &middot; 1 offline note. 02.2 is Maya&rsquo;s share from the object (no prelude); 04.8 is another pasta evening; the boat couple are a separate record inset beside 04.4, not a slot; B0 lives on board 05 as D1. The second host preview and the Send readback fold into 03.1 and a line on Home; Maya&rsquo;s unadopted-proposal view is the branch label on 03.5.'))
    gains = blk('WHAT EACH PERSON GAINS BEFORE GIVING ANYTHING', tbl(['EXP', 'PERSON', 'GAINS', 'GIVES'], GAINS))
    thin = blk('REMAINING DEPENDENCIES &middot; DRAWN AS INTENDED, SUPPORT UNVERIFIED', tbl(['PLACE', 'STATE', 'WHO RESOLVES'], THIN))
    pairs = blk('BOARD 05 &middot; THE SIX DECISION PAIRS &middot; 12 FRAMES', tbl(['DECISION', 'THE PAIR', 'BUDGET'], PAIRS))
    inner = status + two(cal, drift, 0.42) + ledger + spec + a + b + c + alloc + two(gains, thin + '<div style="height: 26px;"></div>' + pairs, 0.5)
    return sheet(2200, hh('01'), f'VESPER &middot; SOCIAL EXPERIENCE &middot; 01 &middot; CHECKPOINT 1 &middot; STORY AND CONTENT BEFORE POLISH &middot; {STAMP}', '01 &middot; Checkpoint 1 &middot; Cast, ledger, sequence',
                 'No phone is drawn on this board. It holds the shared fixture ledger, the drift it resolves, the two content specimens, the three sequences as role-labelled rows and thumbnails, the 24-slot allocation with its tradeoff, what each person gains before giving anything, the remaining dependencies, and the six decision pairs for board 05. Reviewed by the founder on September 7; revised; Checkpoint 2 proceeds from here.', inner)

FILES = {'00 - Start Here': start_here, '01 - Checkpoint 1 - Cast, Ledger, Sequence': checkpoint}
if __name__ == '__main__':
    for n, f in FILES.items():
        h = f(); open(os.path.join(OUT, n + '.dc.html'), 'w').write(h); print('wrote', n, len(h))
