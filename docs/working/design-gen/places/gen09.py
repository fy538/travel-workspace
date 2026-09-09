"""09 · Stages: the same Friday in New York for one person at four points of use. Stage changes what leads and what is attributed, never the composition."""
from fix import *
from kinds import returned_understanding
import instruments as I
import gen19v3 as g
def opening(stage):
    day = I.pier_line()
    if stage == 1:
        k = kick('SATURDAY AT THE PIER · FREE'); line = serifline('Playtime on the lawn at 8:30, free; the sunset from the west pier first, at 7:04.'); f = fn('TATI&rsquo;S CITY OF GLASS · GET THERE AT EIGHT FOR A SPOT · RAIN PLAN NOT POSTED', 8); d = doors(('Saturday&rsquo;s film', GOLDD))
    elif stage == 2:
        k = kick('SATURDAY AT THE PIER · KEPT TUESDAY'); line = serifline('Sunset from the west pier at 7:04; it turns cold fast. The lawn is nine minutes on, the film at 8:30.'); f = fn('YOU KEPT THIS ON TUESDAY, FROM THE FIELD', 8); d = doors(('The pier', GOLDD))
    elif stage == 3:
        k = kick('SATURDAY AT THE PIER · KEPT WITH MAYA'); line = serifline('Sunset from the west pier at 7:04; it turns cold fast. The lawn is nine minutes on, the film at 8:30.'); f = fn('MAYA, TUESDAY · &ldquo;TUESDAY, SEVEN.&rdquo;', 8); d = doors(('The pier, with Maya', GOLDD), ('Reply to Maya', MUTE))
    else:
        k = kick('SATURDAY AT THE PIER · YOUR THIRD THIS YEAR'); line = serifline('Sunset from the west pier at 7:04; it turns cold fast. You were last here in May, at low water; the film on the lawn is new.'); f = fn('MAYA: &ldquo;TUESDAY, SEVEN.&rdquo; · YOU, MAY 9 AND JULY 20', 8); d = doors(('The pier, with Maya', GOLDD), ('Reply to Maya', MUTE))
    return gut(f'<div style="display: flex; flex-direction: column;">{k}{day}<div style="margin-top: 12px;">{line}</div>{f}<div style="margin-top: 8px;">{d}</div></div>', top=24)
def top(stage):
    a = anchor('NEW YORK', 'FRIDAY 5:40 PM')
    o = {1: orientation('Playtime on the lawn by the pier. Saturday, 8:30.', 'Free · Sunset Park · the pier at sunset first, 7:04 · Red Hook by ferry, Saturday or Sunday'),
         2: orientation('The pier at sunset. Saturday, 7:04.', 'Kept Tuesday · Sunset Park · the film on the lawn after · Red Hook by ferry, Saturday or Sunday'),
         3: orientation('The pier at sunset, with Maya. Saturday, 7:04.', 'Kept from her share · Sunset Park · the film on the lawn after · Red Hook by ferry, Saturday or Sunday'),
         4: orientation('The pier at sunset, with Maya. Saturday, 7:04.', 'Kept from her share · your third this year · the film on the lawn after · Red Hook by ferry')}[stage]
    return a + o + ask()
def shelf(stage):
    items = list(g.SHELF)
    if stage == 4: items[0] = ('The noodle counter', 'Hand-pulled · you, twice in August', 'CASH'); items[3] = ('The long table at the caf&eacute;', 'One communal table · your Saturday mornings', 'ROOM FOR STRANGERS')
    return sect('Any day') + gut(browse_shelf(items))
def redhook(stage):
    extra = {1: '', 2: fn('KEPT WEDNESDAY, FROM THE READING', 4), 3: fn('MAYA WAS THERE THURSDAY', 4), 4: fn('MAYA WAS THERE THURSDAY · YOU, IN MAY', 4)}[stage]
    rows = ('<div>' + nrow(1, 'The Harbor Print Room', 'TUE–SUN 11–6 · ROOMS REMADE, TO SUNDAY', unc(UNK_ROOM) + extra, first=True) + nrow(2, 'The Red Hook pier', 'FACES THE HARBOR AND THE STATUE') + nrow(3, 'The Red Hook pool', 'LAP SWIM 7–8:30 AM · BRING A LOCK') + nrow(4, 'The lunch counter on Columbia Street', 'TILL 4 · $11 PLATE · STANDING ROOM', last=True) + '</div>')
    walk = f'<div style="font-size: 14px; line-height: 19px; color: {INK2}; margin-top: 12px; padding-top: 12px; border-top: 1px solid {HAIR7};">Everything here is within twelve minutes of the landing on foot.</div>'
    return sect('Red Hook, by ferry') + gut(REDHOOK_MAP + burden_strip() + f'<div style="margin-top: 4px;">{rows}</div>' + walk)
def evening(stage):
    band = I.day_band(18, 23, [('19:15', '20:15', 'THE HOUR', 'gold')], [], [('start', '6:45 DOORS', 'start'), ('end', 'COUNTER TILL 10 · CAFÉ TILL 11', 'end')])
    unit = title('The listening hour at Canal Hall', 17, 22) + sup('Reich, Music for 18 Musicians, heard whole. Lights down, no talking; doors 6:45.') + unc(UNK_HOUR) + fn('SATURDAY 7:15 PM · $12 · CANAL STREET' + (' · YOU, IN MARCH' if stage == 4 else ''), 4)
    if stage >= 3: unit += '<div style="margin-top: 12px;">' + arow('Sam · ' + dim('sit on the left side, that&rsquo;s where the speakers are'), avatars=['S'], last=True) + '</div>'
    unit += door('This Saturday&rsquo;s hour') + '<div style="margin-top: 8px;">' + prow('The noodle counter', 'TILL 10 · THREE MINUTES FROM THE HALL', first=True) + prow('The long table at the caf&eacute;', 'TILL 11 · FOUR MINUTES', last=True) + '</div>'
    return sect('Saturday evening') + gut(band + unit)
def understanding(stage):
    out = g.understanding()
    if stage == 4: out += gut(returned_understanding(), top=24)
    return out
def sunday(stage):
    u = title('Bach on the organ at the old church', 17, 22) + sup('The Passacaglia and two chorale preludes, forty minutes.') + fn('SUNDAY 4 PM · FREE' + (' · YOUR SUNDAY, THREE TIMES SINCE SPRING' if stage == 4 else ''), 4)
    if stage >= 3: u += '<div style="margin-top: 12px;">' + arow('Maya · ' + dim('sat at the back; forty minutes, then coffee · last month'), avatars=['M']) + arow('Priya · ' + dim('fell asleep in the Passacaglia, happily · last month'), avatars=['P'], last=True) + '</div>'
    return sect('Sunday') + gut(u + door('Sunday&rsquo;s organ'))
def morning(stage):
    u = '<div>' + prow('The greenmarket', '8–1 · BREAD GOES FIRST' + (' · YOURS BY TEN, USUALLY' if stage == 4 else ''), first=True) + prow('The pierogi table at the church hall', '11–2 · $8 · GONE BY ONE') + prow('The long table at the caf&eacute;', 'SATURDAY MORNINGS, WHEN THE REGULARS ARE IN', last=True) + '</div>'
    if stage >= 3: u += '<div style="margin-top: 8px;">' + arow('Theo · ' + dim('the bread stall sells out by ten; go early or don&rsquo;t bother'), avatars=['T'], last=True) + '</div>'
    return sect('Saturday morning, downtown') + gut(u + door('All of Saturday morning'))
def field(stage):
    body = top(stage) + opening(stage)
    if stage >= 3: body += g.friends()
    body += shelf(stage) + redhook(stage) + evening(stage) + understanding(stage)
    if stage >= 3: body += g.upclose()
    body += sunday(stage) + morning(stage) + gut(door_list(['Another neighborhood', 'Sunday, all day'] + (['From friends, everything'] if stage >= 3 else [])), top=24)
    return phone(body)
def board():
    caps = [('1 · FIRST OPEN', 'TONIGHT; NOTHING KEPT, NO ONE', 'The world leads: the film in the light; the question line is the only door in; the everyday six, the pocket, the evening, the comparison, the reading, Sunday plain'),
            ('2 · FIRST WEEK', 'TWO KEPT PLACES, NO FRIENDS YET', 'The kept pier leads because it is worthwhile, not because it is kept; the Print Room says kept, from the reading; nothing else moves'),
            ('3 · SETTLED', 'THE CURRENT 01', 'Friends&rsquo; lines under the places they concern; Maya&rsquo;s share leads the opening; Sam at the hour, Theo at the market, Maya and Priya on Sunday'),
            ('4 · A YEAR IN', 'A RECORD DEEP ENOUGH TO SPEAK', 'Your own returns as mono facts on the places that have them; the returned understanding from Sorrento under the comparison; nothing becomes a diary: the world still leads every section')]
    cols = [viewport(col(field(i + 1), caption(*caps[i]), clip=None)) for i in range(4)]
    delta = tbl(['SECTION', 'FIRST OPEN', 'FIRST WEEK', 'SETTLED', 'A YEAR IN', 'NEVER CHANGES'], [
        ['The opening', 'The world&rsquo;s best offering leads: the film', 'A kept place may lead when it is worthwhile; its keeping is one mono line', 'Her share leads; her words are the fact line; two doors', 'The keeping, her words and your returns share one fact line; the sentence gains one clause', 'One instrument, one sentence, one primary door'],
        ['From friends', 'Absent', 'Absent', 'A card for the lead contribution, rows for the rest', 'The same', 'Never a feed; each line once, under its place'],
        ['Any day', 'Six places, six chips', 'The same', 'The same', 'Your returns as the line on two of six', 'The shelf&rsquo;s geometry; photo or hatch'],
        ['Red Hook, by ferry', 'The map, the strip, four places', 'The Print Room says kept, from the reading', 'Maya&rsquo;s line under the Print Room', 'Maya&rsquo;s line and your May', 'The map, the strip, the walk line'],
        ['Saturday evening', 'The hour on the band', 'The same', 'Sam&rsquo;s line', 'Sam&rsquo;s line and your March', 'The band, the unit, two neighbours'],
        ['Worth understanding', 'Two ways in; the flood section', 'The same', 'The same', 'The returned understanding from Sorrento joins', 'Different value, never a repeat of the recommendation'],
        ['Seen up close', 'Absent', 'Absent', 'Priya&rsquo;s note', 'The same', 'A person&rsquo;s own words, once'],
        ['Sunday and Saturday morning', 'Plain', 'Plain', 'Maya, Priya and Theo&rsquo;s lines', 'Your Sunday and your bread as facts', 'Serif rows, mono facts'],
        ['Doors', 'Two', 'Two', 'Three', 'Three', 'Text arrows; no door to your history from here']])
    notes = [notecol('What stage changes, and what it never changes', [('THE RULE', N('Stage changes what leads and what is attributed. It never changes the composition: the same sections in the same order at every stage, with the world&rsquo;s offering first and the person&rsquo;s record as mono facts on the places that have them. A year in, the field must not become a diary; the returns are facts under world places, never sections of their own, and there is no door to the record from here. Life holds the record.')),
                      ('THE FIXTURE', N('Stages 1 and 3 are 01&rsquo;s cold and populated scrolls. Stage 2 adds two keepings and nothing else. Stage 4 adds returns to five places (the pier in May and July, the noodle counter twice in August, the Print Room in May, the hall in March, the organ three times since spring) and the Sorrento understanding; all fixture, all in the same New York.')),
                      ('OPEN', N('Whether a year in should surface a place you have stopped going to (a lapse), and where; drawn nowhere. Whether the kept possibility should lead in the first week at all when the film is the better offering; drawn as leading, per 05, and marked as a judgment. Interaction untested.'))], w=1700)]
    return rows_page(2560, '09 · STAGES · 09-08', '09 · Stages', 'The same Friday in New York for one person at four points of use: first open, first week, settled, a year in. What each stage changes and what never changes.',
                     [('ONE PERSON, FOUR POINTS', 'First open; first week; settled; a year in', cols), ('THE DELTAS', 'Section by section', [f'<div style="width: 1700px;">{delta}</div>']), ('NOTES', '', notes)], 9000)
if __name__ == '__main__':
    import os; os.makedirs('out2', exist_ok=True); h = board(); open('out2/09 - Stages.dc.html', 'w').write(h); print('wrote 09', len(h))
