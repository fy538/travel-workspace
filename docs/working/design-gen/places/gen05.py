"""05 · Decisions: what is decided for Places, what is still proposed, and what waits on the founder. Replaces the September 8 board, whose five sentences were proposals."""
import re
from kit3 import *
def blk(t, h): return f'<div style="display: flex; flex-direction: column; gap: 12px;"><div class="shead notes" style="color: {GOLDD};"><span>{t}</span><span class="rule"></span></div>{h}</div>'
DECIDED = [
 ['The field is a mixed-value field with one pocket, in Home&rsquo;s kit, with an instrument wherever a section has data to show', '01', 'Founder&rsquo;s choice, September 7 (response &sect;19&ndash;&sect;21)'],
 ['Instruments are drawn from data; the day line replaced the two-curve chart', '01, 07', 'Founder, September 7&ndash;8 (&sect;26&ndash;&sect;32)'],
 ['A place page keeps one shell and reads for the purpose it was opened with: to look, to judge a visit, or from an arrangement. A friend&rsquo;s contribution opens her original first', '08.7&ndash;08.9; Entity 14', 'Decision of September 9, selecting design convergence'],
 ['When acting on a recommendation means sending words to people already involved, one door may open that message, addressed and editable. The person sends', '02 P3, H4.1; 04.2&ndash;04.4', 'Decision of September 9, amending sentence 6'],
 ['Photographs only, never drawings. A place without its own photograph has no plate', 'Every board', 'Founder, September 7; Entity imagery ruling, September 3 (&sect;43)'],
 ['A reading ends as the reader&rsquo;s own last page, with Back; nothing advances to lunch', '08.12', 'Review of September 9, selected direction (&sect;38)'],
 ['The shared design language, consumed at vdl-stage1 0.4.1', 'Every board; 07', 'Founder, September 11 (&sect;39&ndash;&sect;40)'],
 ['Phones show the object; explanations stay in the notes', 'Every board', 'Founder&rsquo;s voice ruling, September 20&ndash;21 (&sect;43)'],
 ['Home selects the shared Saturday&rsquo;s supply; Places renders its world-facing reading; the facts live in one place', '03.3; fixture ledger &sect;12', 'Review of September 9; ledger &sect;12, September 26 (&sect;44)']]
PROPOSED = [
 ['The field is ordered by kind of value, not by neighborhood; a kept possibility leads only when it is the better offering', '01'],
 ['A map appears inside a section only where proximity or access makes the options easier to grasp; the whole-city map is one tap away', '01, 10'],
 ['A friend&rsquo;s line sits once, under the place it concerns; two people on one place are two attributed lines', '01, 08'],
 ['A wrong inference is repaired where it is held and everywhere it was used; today&rsquo;s treatment expires on its own', '03.7&ndash;03.9'],
 ['A scope looked up from elsewhere never implies you are there; the scope and the question are separate chips', '10.A1&ndash;A6'],
 ['A marker and its row are one selection, reached from either side, and a return keeps the selection and the scroll', '10.B1&ndash;B9']]
WAITING = [
 ['&ldquo;That&rsquo;s not right&rdquo;: a door on the page, as drawn, or a reply in the question line', '03.7'],
 ['Whether a correction stays visible afterward, for instance on the record it came from', '03.8'],
 ['Whether the Open House walk-in sites get their own pocket with a map', '03.3'],
 ['The Stage 2 instrument language: once selected, Places moves its instruments in one change', 'Workbench S2-D; 01, 07'],
 ['Who owns the shared place collection in the September 22 multiplayer brief', 'Not drawn here']]
OTHERS = [
 ['Shared workbench', 'A neutral place glyph on the card reader (it shows a knife and fork beside a print workshop); a chevron on the place row; map labels that grow with the text'],
 ['Home', 'The Saturday notes in fixture ledger &sect;12: 19&rsquo;s morning temperature, 19.3&rsquo;s low-water end and pier name, and 19.3 opening Places&rsquo; own pier reading']]
def board():
    inner = headblock('05 &middot; DECISIONS &middot; 09-26', '05 &middot; Decisions', 'What is decided for Places, what is still proposed, and what waits on you. Each row says where it is drawn and where the decision is recorded.')
    inner += '<div style="display: flex; flex-direction: column; gap: 34px;">'
    inner += blk('DECIDED', tbl(['DECISION', 'DRAWN ON', 'RECORDED IN'], DECIDED))
    inner += blk('PROPOSED, NOT ADOPTED', tbl(['PROPOSED RULE', 'DRAWN ON'], PROPOSED))
    inner += blk('WAITING ON YOU', tbl(['QUESTION', 'WHERE'], WAITING))
    inner += blk('WITH OTHER OWNERS', tbl(['OWNER', 'WHAT PLACES NEEDS'], OTHERS))
    inner += blk('WHAT THIS BOARD REPLACES', N('The September 8 board listed five decisions, all proposed. Their substance survives above, reworded to what the boards draw now: the From friends row became the shared reader card, and the rule about stand-in drawings was replaced by photographs only. The earlier version is kept under before-copy-pass/.'))
    inner += '</div>'
    op = BOARD_OPEN.replace('width: 1900px', 'width: 1720px').replace(re.search(r'min-height: \d+px', BOARD_OPEN).group(0), 'min-height: 1200px')
    return HEAD + op + inner + FOOT + TAIL
if __name__ == '__main__':
    import os; os.makedirs('out2', exist_ok=True); h = board(); open('out2/05 - Decisions.dc.html', 'w').write(h); print('wrote 05', len(h))
