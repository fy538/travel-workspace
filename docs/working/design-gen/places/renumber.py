"""The cleanup (founder, 09-08): seven boards in reading order. 01 The Field (was 19), 02 The Journeys (21), 03 The Situations (22), 04 The Checks and the Opening (20), 05 Decisions (08), 06 Log (09), 00 Index rebuilt."""
import re, os, sys
sys.path.insert(0, '.')
from kit3 import *
import gen19v3, gen20, gen21, gen22, fix
MAP = {'19': '01', '21': '02', '22': '03', '20': '04', '08': '05', '09': '06'}
def renum(html):
    return re.sub(r'\b(of|on|On|from|to|board|Board|and|with|beside|through|than) (19|20|21|22)\b(?! (?:MIN|min|minutes))', lambda m: f'{m.group(1)} {MAP[m.group(2)]}', html)
os.makedirs('out2', exist_ok=True)
# 01 · The Field
h = gen19v3.board()
h = h.replace('19 &middot; THE SYNTHESIS, WITH THE CANON&rsquo;S INSTRUMENTS &middot; 09-07', '01 &middot; THE FIELD &middot; 09-07').replace('19 &middot; The synthesis, with the canon&rsquo;s instruments', '01 &middot; The field')
h = renum(h); open('out2/01 - The Field.dc.html', 'w').write(h); print('01', len(h))
# 02 · The Journeys
h = gen21.board().replace('21 · THREE CONNECTED JOURNEYS · ORDERED FRAMES · 09-07 (§13.6, §14)', '02 · THE JOURNEYS · ORDERED FRAMES · 09-07 (§13.6, §14)').replace('21 · Three connected journeys, on the chosen terms', '02 · The journeys')
h = renum(h); open('out2/02 - The Journeys.dc.html', 'w').write(h); print('02', len(h))
# 03 · The Situations
h = gen22.board().replace('22 · THE REMAINING SITUATIONS · 09-07 (§14.5)', '03 · THE SITUATIONS · 09-07 (§14.5)').replace('22 · The remaining situations, on the chosen terms', '03 · The situations')
h = renum(h); open('out2/03 - The Situations.dc.html', 'w').write(h); print('03', len(h))
# 04 · The Checks and the Opening
h = gen20.board().replace('20 · THE CHECKS · THE OPENING SEQUENCE · 09-07 (§12.9, §13.3)', '04 · THE CHECKS AND THE OPENING · 09-07 (§12.9, §13.3)').replace('20 · The checks, the opening sequence', '04 · The checks and the opening')
h = renum(h); open('out2/04 - The Checks and the Opening.dc.html', 'w').write(h); print('04', len(h))
# 05 · Decisions (patched from the pushed 08)
p = S('p08.html')
for a, b in [('08 &middot; DECISIONS &middot; CURRENT 09-07', '05 &middot; DECISIONS &middot; CURRENT 09-08'), ('08 &middot; The five decisions', '05 &middot; The five decisions'), ('>19, 18<', '>01<'), ('>18, Z10<', '>01; the archive<'), ('>13, Z12, 19<', '>01<'), ('>18, Z04<', '>01, 02<'), ('>Z06, Z11<', '>02<')]:
    assert a in p, a; p = p.replace(a, b)
p = p.replace('The current expression is on 19; the boards named beside each decision are where it is drawn.', 'The current expression is on 01; the boards named beside each decision are where it is drawn. Earlier numbering (18, 19 and the Z boards) is in the archive in the repository and the response doc.')
open('out2/05 - Decisions.dc.html', 'w').write(p); print('05', len(p))
# 06 · Log (patched from the pushed 09)
p = S('p09.html')
for a, b in [('09 &middot; REVISION LOG &middot; 09-07', '06 &middot; LOG &middot; 09-08'), ('09 &middot; What each pass changed', '06 &middot; What each pass changed')]:
    assert a in p, a; p = p.replace(a, b)
p = p.replace('Boards prefixed Z are the dated comparison material each pass reviewed.', 'Board numbers in the WHERE column are the numbers at the time of each pass; on September 8 the project was renumbered 00 to 06 and the archive moved to the repository (docs/working/design-gen/places/archive). 19 is now 01, 21 is 02, 22 is 03, 20 is 04, 08 is 05, 09 is 06.')
open('out2/06 - Log.dc.html', 'w').write(p); print('06', len(p))
# 00 · Index, rebuilt
def mini(label, html): return f'<div style="display: flex; flex-direction: column; gap: 6px; width: 110px; flex: none;"><div style="width: 110px; height: 200px; overflow: hidden; border-radius: 10px; border: 1px solid {HAIR}; background: {PAPER};"><div style="width: 393px; transform: scale(0.28); transform-origin: 0 0;">{html}</div></div><span class="fn" style="color: {MUTE};">{label}</span></div>'
def blk(t, h): return f'<div style="display: flex; flex-direction: column; gap: 12px;"><div class="shead notes" style="color: {GOLDD};"><span>{t}</span><span class="rule"></span></div>{h}</div>'
minis = blk('THE PROJECT, IN MINIATURE', '<div style="display: flex; gap: 18px; align-items: flex-start;">' + mini('01 · THE FIELD', fix.field(True)) + mini('01 · COLD', fix.field(False)) + mini('02 · A QUESTION', gen21.e2()) + mini('02 · MOVE DINNER?', gen21.p2()) + mini('03 · SORRENTO', gen22.sorrento()) + mini('03 · NO MAP', gen22.map_unavailable()) + mini('04 · WHAT IT OPENS', gen20.destination()) + '</div>')
now = blk('WHERE THINGS STAND', N('<b>Home brings forward what matters in my life. Places lets me explore what the world could offer.</b> The composition is the synthesis of September 7 (a mixed-value field with one pocket) and its expression is the one the founder chose that night: Home&rsquo;s kit for the chrome, the rows and the people, and the canon&rsquo;s kinds and instruments wherever a section has data to show. A photo slot is a hatched plate, never a drawing. 01 is the field, populated and cold; 02 the three journeys; 03 the four situations; 04 the checks and the opening sequence; 05 and 06 the decisions and the log. Everything on every phone is a fixture; every transition is an ordered static frame; nothing inside a phone explains the architecture. Every board has a NOTES control at its top right that hides all commentary.'))
boards = blk('BOARDS', tbl(['BOARD', 'WHAT IT IS', 'WAS'], [['01 - The Field', 'The chosen scroll, populated and cold, with the notes on each section&rsquo;s instrument', '19'], ['02 - The Journeys', 'Exploration; human receiving in three independent branches; practical continuation', '21'], ['03 - The Situations', 'Another city before arrival; sparse supply; the map unavailable; results pending', '22'], ['04 - The Checks and the Opening', 'Long names; text at 1.3&times;; the opening&rsquo;s door, what it opens, and the return', '20'], ['05 - Decisions', 'Five sentences, proposed, not accepted', '08'], ['06 - Log', 'One row per pass since the first export', '09'], ['Archive', 'Every earlier board (01, 02 to 07, 10 to 18, the §12 polish of 19 and 20) as pushed HTML, in the repository under docs/working/design-gen/places/archive, with the generators that draw the current boards', 'Z01 to Z20']]))
outside = blk('OUTSIDE THIS PROJECT', N('The brief: <b>places-complete-experience-design-handoff-2026-09-07.md</b>. The composition revision: <b>places-composition-breadth-design-revision-2026-09-07.md</b>. The response, with every pass item by item: <b>places-complete-experience-design-response-2026-09-07.md</b>, §16 to §21 for the polish, the corrections, the parity draft and the chosen expression. Nothing here is a canon amendment or an implementation authorization.'))
inner = headblock('00 &middot; INDEX &middot; 09-08', 'Vesper &mdash; Places', 'One complete Places experience, iterated through seven critiques on September 7 and cleaned up on September 8. Start with 01, then 02 and 03.') + '<div style="display: flex; flex-direction: column; gap: 34px;">' + minis + now + boards + outside + '</div>'
op = BOARD_OPEN.replace('width: 1900px', 'width: 1560px').replace(re.search(r'min-height: \d+px', BOARD_OPEN).group(0), 'min-height: 1200px')
h = HEAD + op + inner + FOOT + TAIL; open('out2/00 - Index.dc.html', 'w').write(h); print('00', len(h))
