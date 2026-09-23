"""10 · Scope and selection: the two interaction sequences the September 12 coverage assignment asks for.
A · a scope chosen, changed, refined, missed and cleared, without ever claiming the person is there.
B · a marker and its row, the entity they open, the practical question or the provider, and the return to the same field.
Every frame is assembled from what this project already draws: the anchor's city chevron, the question line, the Red Hook map and its numbered rows,
the place page (Entity owns the destination) and the private Ask. The sheet is the shared package's .vdl-sheet construction."""
import re
from fix import *
from kinds import *
import instruments as I
import kinds as K
import gen20

SCOPES = [('New York', 'THE CITY YOU CHOSE · CURRENT'), ('Red Hook', 'BY FERRY · THE POCKET YOU WERE READING'), ('Sunset Park', 'THE N OR R · THE LAWN AND THE PIER'), ('Downtown', 'THE GREENMARKET, THE HALL')]
def sheet(rows, head, sub, action):
    """The bounded chooser, on the shared sheet construction: a handle, one question, the scopes this field already knows, and one way out to typing."""
    rs = ''.join(f'<div class="vdl-row" style="padding-block: 12px;"><div class="vdl-row-body">{title(n, 16, 21)}{fn(m, 3)}</div>{CHEV}</div>' for n, m in rows)
    return (f'<div class="vdl-scrim" style="position: absolute; inset: 0; display: flex; align-items: flex-end;">'
            f'<div class="vdl-sheet" style="width: 100%; box-sizing: border-box;"><div class="vdl-sheet-handle"></div>'
            f'<div class="vdl-sheet-head">{title(head, 20, 25, 600)}{fn(sub, 6)}</div>'
            f'<div class="vdl-rows">{rs}</div>'
            f'<div class="vdl-sheet-actions">{door(action)}</div></div></div>')
def framed(inner, overlay=None):
    ph = phone(inner)
    if overlay:
        i = ph.rfind('</div>')
        ph = ph[:i] + overlay + ph[i:]
    return ph
def select_pin(html, keep='THE PRINT ROOM'):
    """The marker for the selected row, ringed. The map itself is unchanged: this adds one ring around an existing marker, it does not redraw geometry."""
    m = re.search(r'<circle cx="(\d+(?:\.\d+)?)" cy="(\d+(?:\.\d+)?)" r="11"[^>]*/>', html)
    if not m: return html
    cx, cy = m.group(1), m.group(2)
    ring = (f'<circle cx="{cx}" cy="{cy}" r="14" fill="none" stroke="{PAPER}" stroke-width="3"/>'
            f'<circle cx="{cx}" cy="{cy}" r="16" fill="none" stroke="{GOLDD}" stroke-width="2"/>')
    return html.replace(m.group(0), ring + m.group(0), 1)
# ---------------------------------------------------------------- A · scope
def a1():
    inner = anchor('NEW YORK', 'FRIDAY 5:40 PM') + orientation('The pier at sunset, then the film on the lawn. Saturday.', 'From Maya&rsquo;s share, kept · not yet arranged with her · Sunset Park', 26, 31) + ask()
    inner += sect('Red Hook, by ferry') + gut(map_block() + f'<div style="margin-top: 4px;">{redhook_rows(True)}</div>')
    inner += gut(door_list(['Another neighborhood']), top=24)
    return phone(inner)
def a2():
    inner = anchor('NEW YORK', 'FRIDAY 5:41 PM') + orientation('The pier at sunset, then the film on the lawn. Saturday.', 'From Maya&rsquo;s share, kept · not yet arranged with her · Sunset Park', 26, 31) + ask()
    inner += sect('Red Hook, by ferry') + gut(map_block())
    return framed(inner, sheet(SCOPES, 'Where should I look?', 'THE CITY YOU CHOSE, AND THE POCKETS THIS FIELD ALREADY HOLDS', 'Somewhere else · type it'))
def a3():
    inner = anchor('SORRENTO', 'FRIDAY 11:41 PM') + orientation('Sorrento, as it stands today.', 'You are in New York · this is 8:41 in the morning there · nothing here is near you', 26, 31) + ask(q='Sorrento')
    inner += gut(fn('LOOKED UP FROM NEW YORK · NO DISTANCES FROM YOU, BECAUSE YOU ARE NOT THERE', 12), top=16)
    inner += sect('The town, today') + gut('<div>' + prow('The lemon terraces above Via Rota', 'OPEN 9–6 · FROM THE TOWN&rsquo;S OWN LISTING', first=True) + prow('The stairs at Marina Grande', 'ALWAYS OPEN · 200 STEPS DOWN TO THE WATER') + prow('The Saturday market at Piazza Tasso', 'SATURDAY 8–1 · TODAY IS FRIDAY', last=True) + '</div>')
    inner += sect('Worth understanding') + gut(K.returned_understanding())
    inner += gut(door_list(['Back to New York']), top=24)
    return phone(inner)
def a4():
    inner = anchor('SORRENTO', 'FRIDAY 11:44 PM') + orientation('Sorrento, as it stands today.', 'You are in New York · this is 8:44 in the morning there', 26, 31) + ask(q='Sorrento', ctx='Quiet, in the evening')
    inner += gut(fn('THE SCOPE AND THE QUESTION ARE TWO CHIPS · EITHER COMES OFF ON ITS OWN', 12), top=16)
    inner += sect('Quiet, in the evening') + gut('<div>' + prow('The cloister at San Francesco', 'OPEN TILL 8 · NOBODY THERE AFTER SEVEN', first=True) + prow('The bench walk above Marina Piccola', 'ALWAYS OPEN · THE LIGHT GOES ABOUT 7:30', last=True) + '</div>')
    inner += gut(door_list(['Back to New York']), top=24)
    return phone(inner)
def a5():
    inner = anchor('SORRENTO', 'FRIDAY 11:46 PM') + orientation('Nothing here is quiet at six on a Friday.', 'The question stands; the town does not answer it', 26, 31) + ask(q='Sorrento', ctx='Quiet, at six')
    inner += gut(K.live_fallback('WHAT IS TRUE INSTEAD', 'The cloister closes at eight and the market has gone. What is quiet at six is the bench walk, and it is twenty minutes uphill.'), top=16)
    inner += sect('Open at six, not quiet') + gut('<div>' + prow('Piazza Tasso', 'THE CAFÉS FILL FROM SIX · LOUD UNTIL LATE', first=True) + prow('The stairs at Marina Grande', 'ALWAYS OPEN · BUSY AT SUNSET', last=True) + '</div>')
    inner += gut(doors(('Drop &ldquo;at six&rdquo;', GOLDD), ('Back to New York', MUTE)), top=16)
    return phone(inner)
def a6():
    inner = anchor('NEW YORK', 'FRIDAY 5:48 PM') + orientation('The pier at sunset, then the film on the lawn. Saturday.', 'From Maya&rsquo;s share, kept · not yet arranged with her · Sunset Park', 26, 31) + ask()
    inner += gut(fn('BACK WHERE YOU WERE · THE SCOPE IS CLEAR, THE FIELD IS AS IT WAS, THE PLACE OF THE SCROLL IS KEPT', 12), top=16)
    inner += sect('Red Hook, by ferry') + gut(map_block() + f'<div style="margin-top: 4px;">{redhook_rows(True)}</div>')
    inner += gut(door_list(['Another neighborhood']), top=24)
    return phone(inner)
# ------------------------------------------------------------ B · selection
def b1():
    inner = anchor('RED HOOK', 'SATURDAY 12:10 PM', back=True, sub='Near Red Hook, Saturday') + gut(map_block(), top=12) + gut(burden_strip(), top=4)
    inner += gut(redhook_rows(True), top=12) + gut(body('Everything here is within twelve minutes of the landing on foot.'), top=12)
    return phone(inner)
def b2(from_row=False):
    inner = anchor('RED HOOK', 'SATURDAY 12:11 PM', back=True, sub='Near Red Hook, Saturday') + gut(select_pin(map_block()), top=12) + gut(burden_strip(), top=4)
    mark = f'<div style="margin-top: 12px; padding: 10px 12px; border-radius: 12px; background: {CARD}; border: 1px solid {HAIR}; display: flex; gap: 10px; align-items: center;"><span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 0.9px; color: {GOLDD}; flex: none;">1</span><div style="font-size: 13px; line-height: 18px; color: {INK2};">{"The row you tapped is the marker on the map." if from_row else "The marker you tapped is this row."}</div></div>'
    inner += gut(mark, top=8)
    rows = redhook_rows(True).replace('<div style="display: flex; align-items: flex-start; gap: 12px; padding: 10px 0;', f'<div style="display: flex; align-items: flex-start; gap: 12px; padding: 10px 0; background: {WASH}; border-radius: 10px; margin: 0 -8px; padding-left: 8px; padding-right: 8px;', 1)
    inner += gut(rows, top=12) + gut(doors(('Open the Print Room', GOLDD), ('Clear the selection', MUTE)), top=8)
    return phone(inner)
def b3():
    import gen08
    return gen08.page('populated', context='FROM THE MAP · RED HOOK, SATURDAY')
def b4():
    inner = anchor('THE PRINT ROOM', 'SATURDAY 12:14 PM', back=True, sub='Red Hook')
    inner += gut(K.hours_register([('HOURS', 'Tue–Sun 11–6'), ('THE ROOMS', 'Upstairs, by a flight of stairs')]), top=16)
    inner += gut(composer('Ask about the Print Room'), top=16)
    inner += gut(fn('ASKS VESPER, NOT THE WORKSHOP · MAYA IS NOT A RECIPIENT', 8), top=8)
    ext = f'<div style="margin-top: 20px; padding: 14px; border-radius: 14px; background: {CARD}; border: 1px solid {HAIR};">{kick("DIRECTIONS · LEAVING VESPER")}<div style="margin-top: 8px;">{serifline("Opens your map app at Van Brunt Street. Vesper is not navigating and does not learn where you go.", 16, 22)}</div><div style="margin-top: 12px; display: flex; gap: 12px;"><span class="vdl-btn primary vk-t-labelSemibold" style="color: var(--vk-color-white);">Open Maps</span><span class="vdl-btn secondary vk-t-labelSemibold">Stay</span></div></div>'
    inner += gut(ext, top=4)
    return phone(inner)
def b5():
    inner = anchor('RED HOOK', 'SATURDAY 12:21 PM', back=True, sub='Near Red Hook, Saturday') + gut(select_pin(map_block()), top=12) + gut(burden_strip(), top=4)
    inner += gut(fn('BACK FROM THE MAP APP · THE SAME POCKET, THE SAME SELECTION, THE SAME PLACE IN THE SCROLL', 12), top=8)
    rows = redhook_rows(True).replace('<div style="display: flex; align-items: flex-start; gap: 12px; padding: 10px 0;', f'<div style="display: flex; align-items: flex-start; gap: 12px; padding: 10px 0; background: {WASH}; border-radius: 10px; margin: 0 -8px; padding-left: 8px; padding-right: 8px;', 1)
    inner += gut(rows, top=12) + gut(doors(('Clear the selection', MUTE),), top=8)
    return phone(inner)
def b6():
    inner = anchor('RED HOOK', 'SATURDAY 12:22 PM', back=True, sub='Near Red Hook, Saturday')
    inner += gut(fn('LARGER TEXT · THE MAP&rsquo;S LABELS DO NOT GROW, SO THE POCKET READS AS ITS ROWS', 12), top=16)
    inner += gut(redhook_rows(True), top=8)
    inner += gut(I.access_compare([('BY FERRY', [(6, 'foot'), (20, 'wait'), (25, 'ride'), (9, 'foot')], 'PIER 11 · EVERY 40 · 40 MOVING, 20 DRAWN, 40 TO 80 IN ALL'), ('BY THE B61', [(4, 'foot'), (6, 'wait'), (28, 'ride'), (3, 'foot')], 'EVERY 12 · 35 MOVING, 6 DRAWN, 35 TO 47 IN ALL')], origin='FROM CANAL STREET', h=112), top=16)
    inner += gut(door_list(['Show the map on its own', 'Back to the field']), top=24)
    return phone(inner)
def narrow_map():
    """The same map at a narrow width. It scales with its column, so its place names would fall below the 10px floor; the readable alternative keeps
    the numbered markers, which the rows already pair with, and drops only the names from the drawing. Geometry is unchanged."""
    m = map_block().replace('height="200" viewBox="0 0 349 200"', 'height="auto" viewBox="0 0 349 200"', 1).replace('<div style="height: 200px; border-radius: 12px;', '<div style="border-radius: 12px;', 1)
    return re.sub(r'<text([^>]*)>(?!\d+</text>)[^<]*</text>', '', m)
def b8():
    inner = anchor('RED HOOK', 'SATURDAY 12:22 PM', back=True, sub='Near Red Hook, Saturday')
    inner += gut(narrow_map(), top=12)
    inner += gut(fn('NARROW · THE MAP KEEPS ITS NUMBERS; THE NAMES ARE IN THE ROWS', 8), top=4)
    inner += gut(redhook_rows(True), top=12)
    inner += gut(door_list(['Back to the field']), top=24)
    return phone(inner).replace('width: 393px', 'width: 320px', 1)
def b9():
    """Back from the map app, and the world moved while the person was away: the selection and the scroll survive, the selected row reads the current fact."""
    inner = anchor('RED HOOK', 'SATURDAY 12:31 PM', back=True, sub='Near Red Hook, Saturday') + gut(select_pin(map_block()), top=12) + gut(burden_strip(), top=4)
    changed = (f'<div style="margin-top: 12px; padding: 10px 12px; border-radius: 12px; background: {CARD}; border: 1px solid {HAIR}; display: flex; gap: 10px; align-items: flex-start;">'
               f'<span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 0.9px; color: {OX}; flex: none; margin-top: 2px;">CHANGED 12:16</span>'
               f'<div style="font-size: 13px; line-height: 18px; color: {INK2};">The Print Room posted &ldquo;closed today, a private event&rdquo; on its own listing while you were away. Rooms Remade is open tomorrow, its last day.</div></div>')
    inner += gut(changed, top=8)
    rows = redhook_rows(True).replace('TUE–SUN 11–6 · ROOMS REMADE, TO SUNDAY', 'CLOSED TODAY · OPEN SUNDAY 11–6, THE LAST DAY', 1)
    rows = rows.replace('<div style="display: flex; align-items: flex-start; gap: 12px; padding: 10px 0;', f'<div style="display: flex; align-items: flex-start; gap: 12px; padding: 10px 0; background: {WASH}; border-radius: 10px; margin: 0 -8px; padding-left: 8px; padding-right: 8px;', 1)
    inner += gut(rows, top=12) + gut(doors(('Sunday, the last day', GOLDD), ('Clear the selection', MUTE)), top=8)
    return phone(inner)
STATUS = [['A · scope chosen, changed, refined, missed, cleared', 'Drawn', 'Proposed for review', 'No', 'No'],
          ['A3 · remote scope never implies presence', 'Drawn', 'Proposed for review', 'No', 'No'],
          ['B · marker and row as one selection, two ways in', 'Drawn', 'Proposed for review', 'No', 'No'],
          ['B4 · the selected entity', 'Drawn from 08', 'Accepted destination direction (decision of 2026-09-09)', 'Partly: the object page is on main behind flags', 'No'],
          ['B5 · provider handoff and its return', 'Drawn', 'Proposed for review', 'No', 'No'],
          ['B7, B8 · larger-text and narrow readings', 'Drawn', 'Proposed for review', 'No', 'No'],
          ['B9 · return with the current state', 'Drawn', 'Proposed for review', 'No', 'No']]
# ---------------------------------------------------------------- the board
def board():
    ra = [viewport(col(a1(), caption('10.A1 · THE SCOPE AS IT STANDS', 'NEW YORK · THE CHEVRON IS THE ONLY SCOPE CONTROL', 'The field as drawn on 01. Scope lives in the anchor&rsquo;s chevron and the question line; there is no filter console and no second navigation'))),
          viewport(col(a2(), caption('10.A2 · THE CHOOSER, BOUNDED', 'THE CITY, AND THE POCKETS THIS FIELD ALREADY HOLDS', 'Four scopes and one way out to typing, on the shared sheet construction. It offers what the field can actually read, not every place in the world'))),
          viewport(col(a3(), caption('10.A3 · CHANGED · SOMEWHERE YOU ARE NOT', 'SORRENTO, LOOKED UP FROM NEW YORK', 'The town as it stands, with its own local time and no distance from you. Nothing claims you or the device is there, and no route is offered from where you are'))),
          viewport(col(a4(), caption('10.A4 · THE QUESTION, REFINED INSIDE THE SCOPE', 'TWO CHIPS: THE SCOPE AND THE QUESTION', 'The scope chip and the question chip are separate, and either comes off on its own. The result is the same field, narrower'))),
          viewport(col(a5(), caption('10.A5 · NO MATCH, HONESTLY', 'THE QUESTION STANDS; THE TOWN DOES NOT ANSWER IT', 'What is true instead, then what is open but not quiet. The world content stays; nothing asks the person to supply more input'))),
          viewport(col(a6(), caption('10.A6 · CLEARED, AND BACK', 'THE FIELD AS IT WAS', 'The scope is clear, the chips are gone, and the field, its pocket and the place in the scroll are as they were. Looking changed nothing')))]
    rb = [viewport(col(b1(), caption('10.B1 · THE POCKET AS DRAWN', 'THE MAP AND ITS NUMBERED ROWS', 'The donor: 01 and 02&rsquo;s Red Hook pocket. The numbers on the map and the numbers in the rows are one set'))),
          viewport(col(b2(), caption('10.B2 · A MARKER TAPPED', 'THE MARKER IS THE ROW', 'The marker takes a ring, the row takes the wash, and a line says which way the tap went. Nothing has opened yet'))),
          viewport(col(b2(True), caption('10.B3 · THE ROW TAPPED', 'THE SAME SELECTION, THE OTHER WAY', 'Row to marker is the same state as marker to row. One selection, two ways in, one way to clear it'))),
          viewport(col(b3(), caption('10.B4 · THE SELECTED ENTITY', 'OPENED FROM THE MAP · ENTITY OWNS THE DESTINATION', 'The place page as 08 draws it, with the context line saying where it was opened from. This project draws the door, not the destination&rsquo;s anatomy'))),
          viewport(col(b4(), caption('10.B5 · A PRACTICAL QUESTION, OR THE PROVIDER', 'ASK VESPER · OR LEAVE FOR THE MAP APP', 'The private question asks Vesper and never the workshop. Directions hand off to the provider and say so; returning is not an arrival'))),
          viewport(col(b5(), caption('10.B6 · BACK, UNCHANGED', 'THE SAME FIELD, SCOPE, SELECTION AND SCROLL', 'The return lands on the pocket that was left: the ring is still on the marker, the row is still selected, and nothing was recorded by going')))]
    rc = [viewport(col(gen20.enlarge(b6()), caption('10.B7 · LARGER TEXT · THE READABLE ALTERNATIVE', 'THE POCKET WITHOUT THE MAP', 'Drawn at 1.3&times;. The map&rsquo;s labels cannot grow with the text, so at this size the pocket reads as its rows and its access comparison, with the map one door away. The information is the same; only its form changes'))),
          viewport(col(b8(), caption('10.B8 · NARROW · THE READABLE ALTERNATIVE', 'THE SAME POCKET AT 320 PIXELS', 'The map scales with its column, so its names would fall below the 10px floor. It keeps its numbers, which the rows already carry, and drops only the names; nothing about the geometry changes'), w=320)),
          viewport(col(b9(), caption('10.B9 · BACK, AND SOMETHING CHANGED', 'THE SELECTION SURVIVES; THE FACT IS CURRENT', 'While the person was in the map app the Print Room posted that it is closed today. The return keeps the pocket, the ring and the scroll, and the selected row reads what is true now, with Sunday named as the last chance'))),
          notecol('Two sequences, and what they rest on', [
              ('WHAT IS NEW HERE', N('Only the controls, the results and the returns. A1, B1 and B4 are the field, the pocket and the page as this project already draws them; A2&rsquo;s chooser, A5&rsquo;s no-match, B2 and B3&rsquo;s selection, B5&rsquo;s provider handoff, B6&rsquo;s return and B7&rsquo;s readable alternative are the missing frames the coverage assignment asks for.')),
              ('DONOR AND ADDITION', tbl(['STEP', 'DONOR', 'WHAT IS ADDED'], [
                  ['Scope control', '07 anchor with its city chevron', 'What the chevron opens: four known scopes and one way out to typing'],
                  ['Refine', '02 E2&rsquo;s typed question and its chip', 'A second chip, so the scope and the question come off separately'],
                  ['No match', '03.4&rsquo;s dated, invented-nothing state', 'What is true instead, and what is open but not quiet'],
                  ['Marker and row', '01 and 02&rsquo;s numbered map and rows', 'One selection, reachable from either side, with one way to clear it'],
                  ['Selected entity', '08.1 the place page', 'The context line that says it was opened from the map'],
                  ['Provider', 'Entity 12.1&rsquo;s honest interstitial', 'The return: the same pocket, selection and scroll'],
                  ['Larger text', '07&rsquo;s instruments at the 10px floor', 'The rows-and-comparison reading when the map&rsquo;s labels cannot grow']])),
              ('REMOTE IS NOT PRESENT', N('A3 and A4 are the same field read from three thousand miles away. The town keeps its own clock, the places keep their hours, and nothing offers a distance, a walk or a route from the person, because the person is not there. Presence, permission and arrival are never implied by a scope.')),
              ('GEOMETRY VERSUS BEHAVIOUR', N('The map is an illustrative drawing: its shoreline, streets and markers are drawn geometry, not a live map. What these frames establish is the selection contract between a marker and its row, the destination it opens and the state that survives a return. Pan, zoom, focus transfer, keyboard order and the back stack are native work; static frames cannot show them.')),
              ('OWNERS', N('Entity owns the destination and its identity; Social owns eligible recipients and addressed sharing, which is why B5&rsquo;s question asks Vesper and stops there. The provider handoff states what Vesper does not do: it does not navigate and does not learn where the person goes.')),
              ('DRAWN, SELECTED, IMPLEMENTED, VERIFIED', tbl(['PART', 'DRAWN', 'SELECTED', 'IMPLEMENTED', 'VERIFIED'], STATUS)),
              ('NOT CLAIMED', N('No turn-by-turn navigation, no standalone map or search product, no filter console, and no scope that outlives the visit. Query, selected-object and return continuity need native verification; drawn here, not exercised.'))], w=760)]
    return rows_page(2660, '10 · SCOPE AND SELECTION · 09-12 COVERAGE', '10 · Scope and selection',
                     'Two small sequences on the field this project already draws: a scope chosen, changed, refined, missed and cleared without ever claiming the person is there; and a marker and its row, the entity they open, the question or the provider, and the return to the same field.',
                     [('A · SCOPE', 'As it stands; the chooser; somewhere you are not; refined; no match; cleared', ra),
                      ('B · MARKER AND ROW', 'The pocket; a marker; the row; the entity; the question or the provider; back unchanged', rb),
                      ('B · READABLE ALTERNATIVES, THE CURRENT STATE, AND THE NOTES', 'Larger text; narrow; back after something changed; donors, owners, status and what is not claimed', rc)], 9000)
if __name__ == '__main__':
    import os; os.makedirs('out2', exist_ok=True); h = board(); open('out2/10 - Scope and Selection.dc.html', 'w').write(h); print('wrote 10', len(h))
