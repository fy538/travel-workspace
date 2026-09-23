"""04 - C · revised (§8.7): friends as people sharing. Illustrative pictures and naturally authored notes; a dense fixture of
eighteen contributions grouped by where, not by who; the share opened with an immediate reply; a locally empty scope that
keeps the person's intent; quiet withdrawal with two treatments. No policy labels inside the phones."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
from gen_generous import col, N, arow, facepile
from gen_generous3 import sect, title, sup, gut, card, fact, author_row
from gen_merge import tbl, daycap
from gen_p2_common import *
from gen_artifact import ways_seq_card

F = FRIENDS
def by(name, place): return next(f for f in F if f[1] == name and f[3] == place)

def maya_print_room(h=170, with_priya=True):
    f = by('Maya', 'print_room')
    extra = (f'<div style="margin-top: 10px;"><div class="kickm" style="margin-bottom: 2px;">ALSO ABOUT THE PRINT ROOM &middot; SEPARATELY</div>{share_line("P", "Priya", by("Priya", "print_room")[2], "was here too", last=True).replace("&middot; was here too", "")}</div>') if with_priya else ''
    return share_v2('M', 'Maya', 'THURSDAY', f[2], kind='room', place=PLACE_NAMES['print_room'], line='Red Hook &middot; <i>Rooms Remade</i> through Sunday', h=h, extra=extra)

def maya_loaf(h=150):
    return share_v2('M', 'Maya', 'LAST FRIDAY', by('Maya', 'bakery')[2], kind='loaf', place=PLACE_NAMES['bakery'], line='Sunset Park &middot; Sunday 7 until it runs out', h=h)

def dense_phone():
    inner = header('NEW YORK', 'From friends') + question_line(ctx='From friends')
    inner += gut(maya_print_room(), top=18)
    inner += sect('Around Canal Street') + gut('<div>' + share_line('S', 'Sam', by('Sam', 'hour')[2], 'Canal Hall') + share_line('M', 'Maya', by('Maya', 'noodles')[2], 'The noodle counter', kind='noodles') + share_line('S', 'Sam', by('Sam', 'noodles')[2], 'The noodle counter', last=True) + '</div>')
    inner += sect('Sunset Park') + gut(share_v2('M', 'Maya', 'TUESDAY', 'Tuesday, seven.', kind='pier', place='The pier', line='Sunset Park', h=150) + '<div style="height: 8px;"></div><div>' + share_line('A', 'Alex', 'First time round the loop without stopping. Barely.', 'The waterfront loop', kind='loop') + share_line('A', 'Alex', by('Alex', 'film')[2], 'The lawn by the pier') + share_line('M', 'Maya', by('Maya', 'bakery')[2], 'The Sunset Park bakery', kind='loaf', last=True) + '</div>')
    inner += sect('Downtown') + gut('<div>' + share_line('T', 'Theo', by('Theo', 'library')[2], 'The branch library', kind='library') + share_line('M', 'Maya', by('Maya', 'organ')[2], 'The old church', kind='organ') + share_line('P', 'Priya', 'Fell asleep in the Passacaglia, happily. Ask Maya, she stayed awake.', 'The old church') + share_line('M', 'Maya', by('Maya', 'table')[2], 'The caf&eacute; with the long table', kind='table', last=True) + '</div>')
    inner += sect('The market') + gut('<div>' + share_line('P', 'Priya', 'The pigeons at the market have a system. I have watched it for twenty minutes.', 'The greenmarket') + share_line('T', 'Theo', by('Theo', 'market')[2], 'The greenmarket', last=True) + '</div>')
    inner += sect('Carroll Gardens') + gut('<div>' + share_line('D', 'Dana', 'Back at the bookshop where we met. Ten years this month.', 'The bookshop on Court Street', last=True) + '</div>')
    inner += sect('Elsewhere') + gut('<div>' + share_line('D', 'Dana', by('Dana', 'sorrento')[2], 'Sorrento, this week', last=True) + '</div>')
    inner += gut(ending(['All of New York', 'Everyone, in Life']), top=28)
    return phone2(inner)

def sparse_phone():
    inner = header('NEW YORK', 'From friends') + question_line(ctx='From friends')
    inner += gut(maya_print_room(with_priya=False), top=18)
    inner += sect('Elsewhere') + gut('<div>' + share_line('D', 'Dana', by('Dana', 'sorrento')[2], 'Sorrento, this week', last=True) + '</div>')
    inner += gut(ending(['All of New York', 'Everyone, in Life']), top=28)
    return phone2(inner)

def opened_phone():
    inner = header('Maya', 'Thursday &middot; to friends', back=True)
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{illo("room", 240)}</div>', top=18)
    inner += gut(f'<div style="{SERIF} font-size: 22px; line-height: 30px; color: {INK};">{by("Maya", "print_room")[2]}</div>', top=16)
    inner += gut(f'<div style="display: flex; align-items: center; gap: 12px; padding: 12px 0; border-top: 1px solid rgba(27,23,20,0.08); border-bottom: 1px solid rgba(27,23,20,0.08);">{thumb("room", 48)}<div style="flex: 1;">{title(PLACE_NAMES["print_room"], 16, 20, 600)}{when_line("Red Hook &middot; Tue&ndash;Sun 11&ndash;6 &middot; <i>Rooms Remade</i> through Sunday")}</div>{CHEV}</div>', top=18)
    inner += gut(f'<div style="display: flex; align-items: center; gap: 10px; min-height: 44px; border: 1px solid rgba(27,23,20,0.14); border-radius: 22px; padding: 0 16px;"><span style="font-size: 15px; color: {GHOST}; flex: 1;">Reply to Maya</span></div>', top=18)
    inner += sect('Also about the Print Room') + gut('<div>' + share_line('P', 'Priya', by('Priya', 'print_room')[2], 'separately, on a rainy Tuesday', last=True) + '</div>' + src('Her own visit, not a reply to Maya'))
    inner += gut(door('Ask about the Print Room') + src('Asks Vesper, not Maya'), top=16)
    return phone2(inner)

def empty_scope_phone():
    inner = header('Red Hook', 'From friends &middot; inside New York', back=True) + question_line(ctx='From friends')
    inner += gut(f'<div style="{SERIF} font-size: 18px; line-height: 25px; color: {INK2};">Nothing from friends around Red Hook yet.</div>', top=22)
    inner += sect('Red Hook, anyway') + gut(place_unit('room', PLACE_NAMES['print_room'], 'Tue&ndash;Sun 11&ndash;6', '<i>Rooms Remade</i> through Sunday; the side room, then and now.', PACKET['print_room']['unknown'], 'The Print Room')
                                             + place_unit('pier', 'The Red Hook pier', 'Any time &middot; free', 'Faces the harbor and the Statue; the Sunset Park pier is the one for sunset.')
                                             + place_unit('quay', 'Three ways home from the water', '', 'By the ferry or the bus; Brooklyn Bridge Park by land; Governors Island only by the crossing.', last=True))
    inner += gut(ending(['From friends, all of New York', 'All of Red Hook']), top=28)
    return phone2(inner)

def withdrawn_collection_phone():
    """After Maya takes back her Print Room note: the collection simply no longer has it. Priya's line stands. Nothing is announced."""
    inner = header('NEW YORK', 'From friends') + question_line(ctx='From friends')
    inner += gut(maya_loaf(170), top=18)
    inner += sect('Red Hook') + gut('<div>' + share_line('P', 'Priya', by('Priya', 'print_room')[2], PLACE_NAMES['print_room']) + share_line('P', 'Priya', by('Priya', 'red_hook')[2], 'The Red Hook pier', kind='pier', last=True) + '</div>')
    inner += sect('Around Canal Street') + gut('<div>' + share_line('S', 'Sam', by('Sam', 'hour')[2], 'Canal Hall') + share_line('M', 'Maya', by('Maya', 'noodles')[2], 'The noodle counter', kind='noodles', last=True) + '</div>')
    inner += sect('Downtown') + gut('<div>' + share_line('T', 'Theo', by('Theo', 'library')[2], 'The branch library', kind='library') + share_line('M', 'Maya', by('Maya', 'organ')[2], 'The old church', kind='organ', last=True) + '</div>')
    inner += gut(ending(['All of New York', 'Everyone, in Life']), top=28)
    return phone2(inner)

def reopened_phone():
    """The exact item, reopened from a saved link: short and unavailable. Below, the one place it was relied on: the Sunday stop still stands on the bakery's own hours."""
    inner = header('Maya', 'Thursday', back=True)
    inner += gut(f'<div style="padding: 40px 12px 30px 12px; text-align: center;"><div style="{SERIF} font-size: 18px; line-height: 25px; color: {INK2};">This share is no longer available.</div></div>', top=18)
    inner += gut(ending(['The Harbor Print Room', 'From friends']), top=0)
    inner += sect('Your Sunday, as it stands') + gut(ways_seq_card('Sunday, if the morning is open', [('10:30', 'The bakery, early', 'Sunday 7 until the loaf runs out; closed by one.', 'ITS OWN HOURS'), ('1:40', 'Low water on the pier', 'The flood line east; the shaded side after two.', 'SUNSET PARK')], meta_t='Maya&rsquo;s note about the bakery is gone. The bakery&rsquo;s own hours still say Sunday; the stop stands.'))
    return phone2(inner)

def board():
    row1 = [col(dense_phone(), daycap('FRIDAY &middot; FROM FRIENDS &middot; SIX PEOPLE, SEVENTEEN THINGS', 'DENSE', 'Grouped by where; pictures where there are pictures', 'MAYA IS PROLIFIC AND IS NOT A SECTION &middot; TWO PLACES HAVE TWO PEOPLE&rsquo;S LINES &middot; NO SCORES, NO PLATES FOR EVERYTHING')),
            col(sparse_phone(), daycap('THE SAME SCOPE &middot; TWO PEOPLE', 'SPARSE', 'One share with a picture; one friend elsewhere', 'THE SAME FORMS AT A SMALLER SCALE &middot; NOTHING INFLATED, NOTHING PROMPTED')),
            col(opened_phone(), daycap('MAYA&rsquo;S SHARE, OPENED', 'THE SHARE VIEW', 'Her picture, her words, the place, a reply', 'REPLY TO MAYA RIGHT HERE &middot; ASK IS A DIFFERENT RECIPIENT AND SAYS SO IN FOUR WORDS &middot; NO DOSSIER DETOUR')),
            notecol('Friends as people sharing', [
                ('THE REVISION', N('&ldquo;What two people made visible&rdquo;, &ldquo;may-use&rdquo;, &ldquo;featured status &middot; city precision&rdquo; are gone. Each contribution is a person, a sentence in their own words, a place, and a picture when they took one. The pictures are illustrations, tagged as such on the plate; no real person&rsquo;s photograph is implied.')),
                ('DENSITY WITHOUT A FEED, AND NOT ONLY ADVICE (&sect;9.7)', N('Seventeen contributions from six people across nine places, grouped by where. Not all of it is advice: Maya&rsquo;s pier picture with two words, Alex&rsquo;s first loop without stopping, Priya&rsquo;s pigeons, Dana back at the bookshop where she met someone ten years ago, and two different experiences of the same recital side by side. The recipient gets enjoyable awareness and easy reasons to reconnect, not only better recommendations. Priya&rsquo;s Print Room line is labelled as her own separate visit, never as a comment on Maya&rsquo;s share.')),
                ('WHAT STAYS OUTSIDE THE PHONE', N('The grants, the precision each person chose, the fact that nothing is where anyone is now. Those remain true and are recorded on 08; the phone does not recite them.')),
            ])]
    row2 = [col(empty_scope_phone(), daycap('RED HOOK &middot; FROM FRIENDS &middot; NOTHING YET', 'A LOCALLY EMPTY SCOPE', 'One sentence, then Red Hook anyway', 'THE INTENT (RED HOOK) IS KEPT &middot; THE WORLD IS OFFERED &middot; NOBODY IS ASKED TO RECRUIT OR POST')),
            col(withdrawn_collection_phone(), daycap('AFTER MAYA TAKES HER NOTE BACK', 'QUIET WITHDRAWAL', 'The collection simply no longer has it', 'NO ANNOUNCEMENT &middot; PRIYA&rsquo;S LINE STANDS &middot; THE PRINT ROOM STAYS IN THE WORLD')),
            col(reopened_phone(), daycap('THE EXACT ITEM, REOPENED &middot; AND ONE THING THAT RELIED ON HER', 'UNAVAILABLE; REPAIRED', 'A short state; the Sunday stop stands on its own hours', 'TWO TREATMENTS: A DECORATIVE SHARE LEAVES SILENTLY; A RELIED-ON RECOMMENDATION IS REPAIRED AND SAYS WHAT STILL HOLDS')),
            notecol('Empty, withdrawn, repaired', [
                ('THE EMPTY SCOPE', N('Red Hook from friends has nothing. The phone says so in one sentence and gives Red Hook anyway, because the person&rsquo;s intent was Red Hook, not the absence of friends. The way back to friends across the whole city is one door.')),
                ('TWO WITHDRAWALS', N('A decorative share leaves without a word: the collection recomposes and nothing marks the gap. The exact item, reopened from a saved link, shows a short unavailable state. When something relied on the share (the Sunday sequence used Maya&rsquo;s bakery note), the dependent unit is repaired under the correction contract and says in one line what still holds and on what authority. Quiet does not mean unrepaired.')),
                ('WHAT WAS CORRECTED FROM THE FIRST EXPORT', N('The blanket &ldquo;nothing else is recomposed&rdquo; claim. Independently supported material survives; dependent explanations, ranking and practical consequences are recomputed. The sequence here is the worked example.')),
            ])]
    from gen_p2_02 import field as ordinary_field
    row3 = [col(ordinary_field('film'), daycap('THE ORDINARY OPENING', '1 &middot; A ROW WITH FACES, UNDER THE LEAD', 'From friends is one tap, with no query and no sheet', 'A RECOGNIZABLE ENTRY, NOT A FILTER (&sect;9.8) &middot; NOT A TAB, NOT A TAKEOVER')),
            col(dense_phone(), daycap('TAP IT', '2 &middot; FROM FRIENDS', 'What people shared, grouped by where', 'THE CHIP APPEARS IN THE LINE; &times; OR THE HEADER GO BACK')),
            col(ordinary_field('film'), daycap('BACK', '3 &middot; THE OPENING, INTACT', 'Same page, same position', 'THE FIRST SOCIAL VISIT NEEDS NO KNOWLEDGE OF THE CONTEXT MODEL')),
            notecol('The minimum path', [('ENTRY WITHOUT A QUERY', N('The ordinary opening carries a row with four faces and a count under the lead. Tapping it opens From friends with the chip set; the &times; on the chip or the header returns to the opening at the same position. The sheet&rsquo;s Who row still exists for combining, but nobody needs it for the first social visit.'))])]
    html = two_rows(1900, '04', f'{STAMP} &middot; 04 &middot; C &middot; THROUGH MY PEOPLE &middot; REVISED 09-07 (&sect;8&ndash;&sect;10)', '04 &middot; C &middot; Friends as people sharing, not records with labels',
                    'Revised through the three critiques: no policy labels; illustrative pictures and naturally authored notes, not only advice; seventeen contributions from six people grouped by where; another friend&rsquo;s separate visit labelled as such; the share opened with an immediate reply; a locally empty scope that keeps the intent; quiet withdrawal with two treatments, one of them a repair; the minimum path in and back, and the three entry treatments.', row1,
                    'EMPTY, WITHDRAWN, REPAIRED', 'What is absent is said once; what leaves, leaves quietly; what relied on it is repaired', row2, default_h=5400)
    html = html.replace('<div class="fn" style="margin-top: 30px; line-height: 16px;">', f'<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12); display: flex; flex-direction: column; gap: 6px;"><div class="kick" style="color: {GOLDD};">THE MINIMUM PATH TO FROM FRIENDS, AND BACK</div><div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px;">Open, tap the faces, come back</div></div><div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + ''.join(row3) + '</div><div class="fn" style="margin-top: 30px; line-height: 16px;">', 1)
    return html.replace('<div class="fn" style="margin-top: 30px; line-height: 16px;">', '<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);">' + blk('CHANGE LOG &middot; 04', changelog([
        ['Dense', 'Six friends&rsquo; own words and moments across nine places, with their pictures', 'Grouped by where; a reply is on the share, not behind the venue', 'Every contribution is under its author&rsquo;s grant (fixture); nothing is where anyone is', 'Original-photo receiving is not implemented; the social renderer today is a sentence strip'],
        ['Sparse', 'Two people, still enjoyable', 'Same forms', '&mdash;', '&mdash;'],
        ['Opened', 'Her picture and words full-size; the place; Priya&rsquo;s line', 'Reply to Maya is a field; Ask says who it asks', '&mdash;', 'Reply to a person from a share (Chat / People)'],
        ['Empty', 'Red Hook anyway', 'Intent kept; one door back to friends citywide', 'Red Hook facts are fixture listings', '&mdash;'],
        ['Withdrawn', 'Nothing to read; the collection is simply current', 'No announcement', 'Withdrawal recompiles dependents (correction contract)', 'Correction propagation across roots'],
        ['Reopened', 'A short truth; the Sunday stop repaired on the bakery&rsquo;s own hours', 'Two doors', 'The bakery&rsquo;s listing', 'Same']])) + '</div><div class="fn" style="margin-top: 30px; line-height: 16px;">', 1)

if __name__ == '__main__':
    html = board(); open(os.path.join(OUT, '04 - C - Through My People.dc.html'), 'w').write(html); print('wrote 04 v2', len(html))
