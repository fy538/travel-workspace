"""22 · The remaining situations, on the chosen terms (§14.5): another city before arrival; sparse supply; the map unavailable; results pending."""
from fix import *
def cliff_section():
    """The town on its cliff: a section, not a map. Forty metres between the reading room and the quay."""
    return (f'<svg width="349" height="96" viewBox="0 0 349 96" fill="none" style="display: block; width: 100%; height: auto; margin-top: 8px;">'
            f'<rect x="0" y="0" width="349" height="96" rx="12" fill="{WASH}"/><path d="M14 30 L170 30 L190 34 L206 78 L335 78" stroke="{INK}" stroke-width="1.6" fill="none" stroke-linecap="round"/>'
            f'<path d="M206 78 L335 78 L335 90 L206 90 Z" fill="rgba(61,80,102,0.20)"/><path d="M206 78 L335 78" stroke="{WATER}" stroke-width="2" stroke-linecap="round"/><path d="M14 30 L170 30 L190 34 L206 78 L206 90 L14 90 Z" fill="rgba(176,133,58,0.10)"/>'
            f'<circle cx="150" cy="30" r="4" fill="{GOLD}"/><circle cx="240" cy="78" r="4" fill="{WATER}"/>'
            f'<text x="14" y="20" {LK}>THE TOWN · THE READING ROOM</text><text x="335" y="66" text-anchor="end" {LK}>THE QUAY · SEA LEVEL</text><text x="184" y="60" text-anchor="end" {LG}>40 M ↓</text><text x="335" y="20" text-anchor="end" {LB}>180 M ON THE MAP</text></svg>')
def sorrento():
    inner = anchor('SORRENTO', 'BEFORE ANY VISIT') + orientation('The town is on a cliff; the water is forty metres down.', 'From New York · Capri for a day · the piazza on Thursday evenings') + ask('Anything in Sorrento, any day')
    inner += gut(kick('WORTH KNOWING BEFORE YOU GO') + cliff_section() + f'<div style="margin-top: 8px;">{serifline("The reading room and the quay walk are 180 metres apart on the map and a cliff apart on the ground.")}</div>' + fn('STAIRS, A LIFT OR A ROAD BETWEEN THEM AREN&rsquo;T LISTED HERE YET', 6) + door('The upper town and the quay, on the map'), top=20)
    inner += sect('Worth a day') + gut('<div>' + prow('Capri, for a day', 'FERRIES FROM 7:30 · €22 EACH WAY · 25 MIN ACROSS · LAST BOAT BACK 6:40', unc('Sailings are cancelled in rough seas; check the morning of.'), first=True) + prow('The lemon terraces walk', 'MORNINGS, TILL NOON · FREE · STEPPED PATHS, SHADE UNDER THE NETS', last=True) + '</div>')
    inner += sect('Any evening') + gut('<div>' + prow('Thursday evening market in the piazza', 'THURSDAYS 6–10 PM · FREE · FOOD STALLS AND A BAND AFTER EIGHT', first=True) + prow('The quay walk', 'ANY TIME · FREE · AT SEA LEVEL, STEP-FREE ALONG THE QUAY', last=True) + '</div>')
    inner += sect('Any morning') + gut('<div>' + prow('The reading room, upper town', 'MORNINGS · FREE · AN EXHIBITION PREVIEW · FORTY METRES ABOVE THE QUAY', first=True, last=True) + '</div>')
    inner += gut(door_list(['The upper town', 'Across the harbor', 'Back to New York']), top=24)
    return phone(inner)
def sparse():
    inner = anchor('NEW YORK', 'FRIDAY 5:40 PM') + orientation('Playtime on the lawn by the pier. Saturday, 8:30.', 'Free · Sunset Park · the pier at sunset first, 7:04') + ask()
    inner += gut(kick('SATURDAY, IN THE LIGHT · FREE') + g.daylight_arc(False) + g.film_bar() + f'<div style="margin-top: 10px;">{serifline("Playtime on the lawn by the pier at 8:30, free; the sunset from the west pier first, at 7:04.")}</div>' + fn('TATI&rsquo;S CITY OF GLASS · GET THERE AT EIGHT FOR A SPOT · RAIN PLAN NOT POSTED', 6) + door('Saturday&rsquo;s film'), top=20)
    inner += sect('This Saturday') + gut('<div>' + prow('The greenmarket', 'SATURDAY 8–1 · DOWNTOWN · BREAD GOES FIRST', first=True, last=True) + '</div>')
    inner += g.understanding(g.COLD).replace(g.sect('Worth understanding'), sect('Worth understanding'), 1)
    inner += gut(door_list(['Another neighborhood', 'Sunday, all day']), top=24)
    return phone(inner)
def map_unavailable():
    slot = f'<div style="height: 72px; border-radius: 12px; background: {WASH}; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 3px; text-align: center; padding: 0 20px;"><div style="font-size: 14px; font-weight: 600; color: {INK};">The map isn&rsquo;t available right now</div><div style="font-size: 13px; color: {MUTE};">Everything here is still here</div></div>'
    inner = anchor('NEW YORK', 'FRIDAY 5:40 PM').replace('<svg width="20" height="20" viewBox="0 0 20 20" fill="none" style="flex: none;"><path d="M3 6.5', '<svg width="20" height="20" viewBox="0 0 20 20" fill="none" style="flex: none; opacity: 0.35;"><path d="M3 6.5', 1)
    inner += orientation('The pier at sunset, with Maya. Saturday, 7:04.', 'Kept from her share · Sunset Park · the film on the lawn after · Red Hook by ferry, Saturday or Sunday') + ask()
    inner += sect('Any day', 22) + gut(browse_shelf([('The noodle counter', 'Hand-pulled at the counter', 'CASH'), ('The lunch counter on Columbia Street', 'One plate a day · standing room', 'TILL 4')]))
    inner += sect('Red Hook, by ferry') + gut(slot + burden_strip() + '<div style="margin-top: 4px;">' + redhook_rows(True) + '</div>' + body('Everything here is within twelve minutes of the landing on foot.').replace('<div style=', '<div style="margin-top: 10px; padding-top: 10px; border-top: 1px solid rgba(27,23,20,0.07);" data-x=', 1))
    inner += gut(door_list(['Try the map again', 'Saturday evening']), top=24)
    return phone(inner)
def pending():
    inner = anchor('NEW YORK', 'FRIDAY 5:40 PM') + ask(q='Near Red Hook, Saturday')
    inner += f'<div style="margin: 10px 22px 0 22px; height: 2px; border-radius: 1px; background: rgba(27,23,20,0.08); position: relative;"><div style="position: absolute; left: 0; top: 0; height: 2px; width: 38%; border-radius: 1px; background: {GOLDD};"></div></div>'
    inner += sect('Red Hook, by ferry', 22) + gut(map_block() + burden_strip() + '<div style="margin-top: 4px;">' + redhook_rows(True) + '</div>')
    inner += sect('Saturday, near Red Hook') + gut(ghost_rows(2))
    return phone(inner)
def board():
    cols = [col(sorrento(), caption('ANOTHER CITY, BEFORE ARRIVAL', '', 'Sorrento from New York: the cliff as a section that leads, then a day, an evening, a morning; the anchor says before any visit')),
            col(sparse(), caption('SPARSE SUPPLY', '', 'Three worthwhile things and nothing else: the film in the light, the market, the reading; no history, no friends, no pocket; not an abundant feed with the people removed')),
            col(map_unavailable(), caption('THE MAP UNAVAILABLE', '', 'The pocket keeps its burden strip, its numbered places and its walk; the map slot says so in one line; the anchor&rsquo;s map is dimmed')),
            col(pending(), caption('RESULTS PENDING', '', 'The question stays readable; what the field already knew about Red Hook holds its place; two quiet rows below, no loading report')),
            notecol('What is carried, what stays open (§14.5)', [
                ('CARRIED', tbl(['SITUATION', 'FROM', 'ON THE CHOSEN TERMS'], [['Another city before arrival', 'Z05, the field', 'The cliff as a section instrument with one serif line; serif rows with mono facts; the ferry&rsquo;s uncertainty as an unconfirmed line; the anchor names the city and says before any visit'], ['Sparse supply', '19 cold start; Z10 sparse', 'The film in the light as the opening, one row, one reading as a cover; sections that would be empty are absent rather than thin'], ['Map unavailable', 'Z12', 'Only the map slot changes; the burden strip, the places and the walk stay; one line says what happened, in the slot, not a banner'], ['Results pending', 'Z12', 'The question chip stays; the known pocket holds its place with its map and strip; two ghost rows; no percentage, no words about mechanics']])),
                ('OPEN', N('From Z05: the city sheet and city selection, the Capri page, the return to New York; behaviour unchanged, not redrawn. From Z12: the occurrence opened and no city yet; Stage 3 states. Sparse supply is drawn for New York on the existing fixture; a genuinely thin city would need its own fixture. Nothing here requires new input as the only fallback.')),
                ('NOT EXERCISED', N('Four static states. Nothing verifies the map failing or a query resolving on a device.'))], w=760)]
    return rows_page(2760, '22 · THE REMAINING SITUATIONS · 09-07 (§14.5)', '22 · The remaining situations, on the chosen terms',
                     'Another city before arrival, sparse supply, the map unavailable and results pending, each drawn in the language of 19 from the scenario content of Z05 and Z12 and the cold start of 19. Not a portfolio and not a fixed allocation of sections per state.',
                     [('FOUR SITUATIONS', 'Before arrival; sparse; no map; pending', cols)], 3400)
if __name__ == '__main__':
    import os; os.makedirs('out', exist_ok=True); h = board(); open('out/22 - The Remaining Situations.dc.html', 'w').write(h); print('wrote 22', len(h))
