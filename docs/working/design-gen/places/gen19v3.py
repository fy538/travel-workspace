"""01 · The field, generated entirely from the kit (09-08). Earlier versions sliced four sections from the pushed HTML of the parity draft;
this one draws every section from kit3, fix and instruments, so a polish lands in one place. Same content, same fixture."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit3 import *
import instruments as I
S_ = lambda f: open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src', f)).read()
notes = S_('notes_col.html')
UNK_ROOM = 'Whether the exhibition is ticketed hasn&rsquo;t been confirmed.'; UNK_HOUR = 'Seats left for this Saturday haven&rsquo;t been confirmed.'
MAYA_ROOM = 'The side room was my favorite. Go on a weekday, it was empty.'; PRIYA_PIGEONS = 'The pigeons at the market have a system. I have watched it for twenty minutes.'
FLOOD = lambda h=150: I.section([(0, 0.6), (34, 0.6), (34, 1.2), (60, 1.2)], 0.9, [(2, 0.68, 'THE PIER · CREEK BED', 'start', INK), (36, 1.3, 'THE STREET · SILL 1911', 'start', INK), (2, 0.96, 'HARBOR · HIGH WATER', 'start', WATER)], scale_m='m', h=h, zmax=1.42)
SHELF = [('The noodle counter', 'Hand-pulled at the counter', 'CASH'), ('The lunch counter on Columbia Street', 'One plate a day · standing room', 'TILL 4'), ('The reading room at the branch library', 'Long tables, lamps, quiet', 'NO ONE ASKING'), ('The long table at the caf&eacute;', 'One communal table', 'ROOM FOR STRANGERS'), ('The waterfront loop', 'Five kilometres, flat', 'SHADED AFTER 2'), ('The old ferry waiting room', 'Benches, the harbor', 'USUALLY NOBODY')]

def top(populated=True):
    out = anchor('NEW YORK', 'FRIDAY 5:40 PM')
    if populated: out += orientation('The pier at sunset, with Maya. Saturday, 7:04.', 'Kept from her share · Sunset Park · the film on the lawn after · Red Hook by ferry, Saturday or Sunday')
    else: out += orientation('Playtime on the lawn by the pier. Saturday, 8:30.', 'Free · Sunset Park · the pier at sunset first, 7:04 · Red Hook by ferry, Saturday or Sunday')
    return out + ask()
def lead_composition(populated=True):
    day = I.pier_line()
    if populated:
        inner_ = kick('SATURDAY AT THE PIER · KEPT WITH MAYA') + day + f'<div style="margin-top: 10px;">{serifline("Sunset from the west pier at 7:04; it turns cold fast. The lawn is nine minutes on, the film at 8:30.")}</div>'
        inner_ += fn('MAYA, TUESDAY · &ldquo;TUESDAY, SEVEN.&rdquo;', 8) + f'<div style="margin-top: 8px;">{doors(("The pier, with Maya", GOLDD), ("Reply to Maya", MUTE))}</div>'
    else:
        inner_ = kick('SATURDAY AT THE PIER · FREE') + day + f'<div style="margin-top: 10px;">{serifline("Playtime on the lawn at 8:30, free; the sunset from the west pier first, at 7:04.")}</div>'
        inner_ += fn('TATI&rsquo;S CITY OF GLASS · GET THERE AT EIGHT FOR A SPOT · RAIN PLAN NOT POSTED', 8) + f'<div style="margin-top: 8px;">{doors(("Saturday&rsquo;s film", GOLDD))}</div>'
    return f'<div style="display: flex; flex-direction: column;">{inner_}</div>'
def friends():
    c = card(author_row('M', 'Maya', 'THURSDAY · TO FRIENDS') + quote(MAYA_ROOM) + place_strip('The Harbor Print Room', 'RED HOOK · TUE–SUN 11–6') + door('Reply to Maya'))
    rows = arow('Priya · the greenmarket · ' + dim('the pigeons have a system · Saturday'), avatars=['P']) + arow('Theo · the bread stall · ' + dim('sells out by ten · Tuesday'), avatars=['T']) + arow('Sam · Canal Hall · ' + dim('sit on the left, that&rsquo;s where the speakers are'), avatars=['S'], last=True)
    return sect('From friends') + gut(c + '<div style="height: 12px;"></div>' + rows + door('Everything from friends'))
def redhook(populated=True):
    rows = ('<div>' + nrow(1, 'The Harbor Print Room', 'TUE–SUN 11–6 · ROOMS REMADE, TO SUNDAY', unc(UNK_ROOM) + (fn('MAYA WAS THERE THURSDAY', 4) if populated else ''), first=True) + nrow(2, 'The Red Hook pier', 'FACES THE HARBOR AND THE STATUE') + nrow(3, 'The Red Hook pool', 'LAP SWIM 7–8:30 AM · BRING A LOCK') + nrow(4, 'The lunch counter on Columbia Street', 'TILL 4 · $11 PLATE · STANDING ROOM', last=True) + '</div>')
    walk = f'<div style="font-size: 14px; line-height: 19px; color: {INK2}; margin-top: 10px; padding-top: 10px; border-top: 1px solid {HAIR7};">Everything here is within twelve minutes of the landing on foot.</div>'
    return sect('Red Hook, by ferry') + gut(REDHOOK_MAP + burden_strip() + f'<div style="margin-top: 4px;">{rows}</div>' + walk)
def evening(populated=True):
    band = I.day_band(18, 23, [('19:15', '20:15', 'THE HOUR', 'gold')], [], [('start', '6:45 DOORS', 'start'), ('end', 'COUNTER TILL 10 · CAFÉ TILL 11', 'end')])
    unit = title('The listening hour at Canal Hall', 17, 22) + sup('Reich, Music for 18 Musicians, heard whole. Lights down, no talking; doors 6:45.') + unc(UNK_HOUR) + fn('SATURDAY 7:15 PM · $12 · CANAL STREET', 4)
    if populated: unit += '<div style="margin-top: 10px;">' + arow('Sam · ' + dim('sit on the left side, that&rsquo;s where the speakers are'), avatars=['S'], last=True) + '</div>'
    unit += door('This Saturday&rsquo;s hour') + '<div style="margin-top: 6px;">' + prow('The noodle counter', 'TILL 10 · THREE MINUTES FROM THE HALL', first=True) + prow('The long table at the caf&eacute;', 'TILL 11 · FOUR MINUTES', last=True) + '</div>'
    return sect('Saturday evening') + gut(band + unit)
def understanding(col=None):
    reading = FLOOD(118) + fn('READING · 4 MIN', 12) + f'<div style="margin-top: 4px;">{serifline("Why the pier floods before the street does", 17, 22)}</div>' + f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 4px;">The pier sits on the old creek bed, two feet below the 1911 sill. It drains only when the harbor is lower than the street.</div>' + door('The rest of the reading')
    piers = (f'<div style="{SERIF} font-size: 17px; line-height: 22px; font-weight: 500; color: {INK};">Two piers, two ways in</div><div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 4px;">Same evening light; a land route and a crossing.</div>'
             + I.access_compare([('SUNSET PARK', [(3, 'foot'), (20, 'ride'), (9, 'foot')], 'THE N OR R · A LAND ROUTE, EASY TO SHORTEN'), ('RED HOOK', [(6, 'foot'), (25, 'ride'), (9, 'foot')], 'THE FERRY, EVERY 40 · A SCHEDULED WAY IN')]))
    return sect('Worth understanding') + gut(piers) + gut(reading, top=24)
def upclose(): return sect('Seen up close') + gut(author_row('P', 'Priya', 'SATURDAY · TO FRIENDS') + quote(PRIYA_PIGEONS) + place_strip('The greenmarket', 'DOWNTOWN · SATURDAY 8–1'))
def sunday(populated=True):
    u = title('Bach on the organ at the old church', 17, 22) + sup('The Passacaglia and two chorale preludes, forty minutes.') + fn('SUNDAY 4 PM · FREE', 4)
    if populated: u += '<div style="margin-top: 10px;">' + arow('Maya · ' + dim('sat at the back; forty minutes, then coffee · last month'), avatars=['M']) + arow('Priya · ' + dim('fell asleep in the Passacaglia, happily · last month'), avatars=['P'], last=True) + '</div>'
    return sect('Sunday') + gut(u + door('Sunday&rsquo;s organ'))
def morning(populated=True):
    u = '<div>' + prow('The greenmarket', '8–1 · BREAD GOES FIRST', first=True) + prow('The pierogi table at the church hall', '11–2 · $8 · GONE BY ONE') + prow('The long table at the caf&eacute;', 'SATURDAY MORNINGS, WHEN THE REGULARS ARE IN', last=True) + '</div>'
    if populated: u += '<div style="margin-top: 6px;">' + arow('Theo · ' + dim('the bread stall sells out by ten; go early or don&rsquo;t bother'), avatars=['T'], last=True) + '</div>'
    return sect('Saturday morning, downtown') + gut(u + door('All of Saturday morning'))
def v3(populated=True):
    body = top(populated) + gut(lead_composition(populated), top=24)
    if populated: body += friends()
    body += sect('Any day') + gut(browse_shelf(SHELF)) + redhook(populated) + evening(populated) + understanding()
    if populated: body += upclose()
    body += sunday(populated) + morning(populated) + gut(door_list(['Another neighborhood', 'Sunday, all day'] + (['From friends, everything'] if populated else [])), top=24)
    return phone(body)
def board(h=5400):
    c1 = col(v3(True), caption('THE CANON&rsquo;S INSTRUMENTS &middot; POPULATED &middot; FRIDAY, NEW YORK', 'HOME&rsquo;S KIT, THE CANON&rsquo;S KINDS', 'Each section carries one instrument that earns its ink: the pier&rsquo;s day on the opening, hatched photo slots on the everyday six, the burden strip on the crossing, the day band on the evening, two ways in on one scale, the flood section to scale'))
    c2 = col(v3(False), caption('THE CANON&rsquo;S INSTRUMENTS &middot; COLD START', 'THE SAME WORLD, NO HISTORY, NO FRIENDS', 'The film leads the light; no From friends, no contributions; the everyday six, the pocket, the evening, the comparison, the reading and Sunday as before'))
    n = notes.replace('>The parity pass</div>', '>The instrument pass</div>' + instrument_notes(), 1).replace('<div class="kickm">WHAT HOME DECIDED THAT PLACES NOW ADOPTS</div>', '<div class="kickm">WHAT HOME DECIDED THAT PLACES ADOPTS (THE PARITY DRAFT, 09-07 EVENING)</div>', 1)
    hb = headblock('01 &middot; THE FIELD &middot; 09-08', '01 &middot; The field', 'The selected direction, chosen by the founder on September 7: Home&rsquo;s kit for the chrome, the rows and the people; the kinds and instruments of the a26e3228 canon wherever a section has data to show, drawn from data; a photo slot is a hatched plate, never a drawing. Populated and cold. Generated entirely from the kit since September 8.')
    op = BOARD_OPEN.replace(re.search(r'min-height: \d+px', BOARD_OPEN).group(0), f'min-height: {h}px')
    return HEAD + op + hb + '<div style="display: flex; gap: 46px; align-items: flex-start;">' + viewport(c1) + viewport(c2) + n + '</div>' + FOOT + TAIL
def instrument_notes():
    rows = [['The opening', 'field_lead_composition · the pier&rsquo;s day', 'One axis: the sun as a true half-sine, the plan as its gold end, the film after dark; the water as a 12.42-hour harmonic, the low-water window, the kayaks'],
            ['Any day', 'field_browse_shelf', 'Six places as hatched photo slots with a name, one line and one mono chip; photo or hatch, never a drawing'],
            ['Red Hook, by ferry', 'The map · the burden strip', 'Door to door: dots on foot, the crossing as one solid bar, one number'],
            ['Saturday evening', 'The day band, from times', 'The hour as the gold block on the evening&rsquo;s track; doors, the counter and the caf&eacute; as its labels'],
            ['Worth understanding', 'Two ways in · the section to scale', 'Two access structures on one minutes scale; the flood section with the harbor between the pier and the sill'],
            ['From friends, Seen up close, Sunday, Saturday morning', 'Home&rsquo;s kit', 'Author rows, serif quotes, the place strip, facepile rows, arrow doors']]
    return (f'<div style="display: flex; flex-direction: column; gap: 8px;"><div class="kickm">THE INSTRUMENT PASS · WHERE EACH SECTION&rsquo;S PICTURE COMES FROM</div>{tbl(["SECTION", "KIND OR INSTRUMENT", "WHAT IT SHOWS"], rows)}</div>'
            f'<div style="display: flex; flex-direction: column; gap: 8px;"><div class="kickm">WHY NOT ROWS OF TEXT</div>{N("Home is not sleek because it is plain; every picture on it carries data. This scroll gives each section that has something to show one kind or instrument, drawn from data at the 10px mono floor: gold for the plan, ink for now, hatch for a photograph not yet sourced. Sections without data to draw keep Home&rsquo;s rows.")}</div>'
            f'<div style="display: flex; flex-direction: column; gap: 8px;"><div class="kickm">THE TWO DRAFTS BEFORE THIS</div>{N("The &sect;12 polish (illustrated places, sans compact titles, a boxed field, an outlined gold pill) and the Home-kit-only draft (the same content as rows of text) were drawn on September 7 and are recorded in the response doc, &sect;16 and &sect;20. Neither is carried forward.")}</div>')
if __name__ == '__main__':
    os.makedirs('out2', exist_ok=True); h = board(); open('out2/01 - The Field.dc.html', 'w').write(h); print('wrote 01', len(h))
