"""Copy pass (September 26): the voice rules from the founder's September 20-21 ruling, applied to Places' phones, plus photo-or-nothing and two cleanups."""
import re, os
fails = []
def patch(path, pairs, count_all=False):
    s = open(path).read()
    for a, b in pairs:
        n = s.count(a)
        if n == 0: fails.append((path, a[:70])); continue
        s = s.replace(a, b) if count_all or n == 1 else s.replace(a, b)
    open(path, 'w').write(s)

KEPT_SUB = "From Maya&rsquo;s share, kept · not yet arranged with her · Sunset Park"
NEW_SUB = "Kept from Maya&rsquo;s share · an idea so far · Sunset Park"
CTX_OLD = "FROM MAYA&rsquo;S SHARE · FOR SATURDAY, NOT YET ARRANGED"
CTX_NEW = "FROM MAYA&rsquo;S SHARE · AN IDEA FOR SATURDAY"

# ---------------- 01 ----------------
patch('gen19v3.py', [
 (KEPT_SUB, NEW_SUB),
 ("a photo slot is a hatched plate, never a drawing", "a place without a photograph has no plate, and a drawing never stands in for one"),
 ("Six places as hatched photo slots with a name, one line and one mono chip; photo or hatch, never a drawing", "Six places as text tiles: a name, one line and one mono chip; a photograph appears only when a real one exists"),
 ("hatch for a photograph not yet sourced", "no plate where no photograph exists"),
])
s = open('gen19v3.py').read()
s2 = re.sub(r"One axis: the sun as a true half-sine[^']*'", "One track for the day: the light as a gold wash to sunset, the low-water window as a water bar, the pier as a gold pill where the light ends and the film as an ink pill after dark; three labels, all drawn from times.'", s, count=1)
if s2 == s: fails.append(('gen19v3.py', 'retired-chart note'))
open('gen19v3.py', 'w').write(s2)

# ---------------- 02 ----------------
patch('gen21.py', [
 ("'THE PIER AT SUNSET · KEPT, WITH MAYA'", "'THE PIER AT SUNSET · SUNSET PARK'"),
 ("share_row('S', 'Sam', 'NOT THIS SATURDAY',", "share_row('S', 'Sam', 'LAST SATURDAY',"),
 ("('SEATS', 'The hall posts them at 5 today; not yet, as of 4:42')", "('SEATS', 'Posted by the hall at 5 today')"),
 ("readback('CHECKED 4:42', 'Not posted yet · this was one look at the hall&rsquo;s page, not a watch')", "readback('CHECKED 4:42', 'Seats not posted yet')"),
 ("TO MAYA AND ALEX · PREPARED, NOT SENT · YOU SEND IT", "DRAFT TO MAYA AND ALEX"),
 ("readback('SENT', 'You asked Maya and Alex about 8:45 · Friday 5:14 PM · a proposal, not a change')", "readback('SENT', 'To Maya and Alex · Friday 5:14 PM · &ldquo;Could we make dinner 8:45?&rdquo;')"),
 ("it does not if the hour runs long.", "it doesn&rsquo;t if the hour runs long."),
 ("'YOUR DINNER AS ARRANGED · MAYA AND ALEX NEED NOTHING NEW'", "'AS ARRANGED WITH MAYA AND ALEX'"),
 (" · ASK BEFORE MOVING", ""),
 ("TO MAYA · NOT SENT", "DRAFT TO MAYA"),
 ("readback('PROPOSED', 'To Maya · Saturday 2:00 at the Print Room · not arranged until she answers')", "readback('PROPOSED', 'To Maya · Saturday 2:00 at the Print Room · waiting on her')"),
 ("The Print Room: its photo slot, what is unconfirmed,", "The Print Room: what is unconfirmed,"),
 (" + gut(photo_plate(190), top=16)", ""),
])

# ---------------- 03 ----------------
patch('gen22.py', [
 ("'Clear, 41&deg; · Saturdays through October · nothing else has changed since Thursday'", "'Clear, 41&deg; · Saturdays through October'"),
 ("door('That is not right')", "door('That&rsquo;s not right')"),
 ("orientation('Understood &mdash; that was for your father.', 'Today is still the level afternoon, and the rooms are back on this page', 26, 31)",
  "orientation('The stairs were your father&rsquo;s. Today stays level.', 'Rooms Remade is back on this page · it ends Sunday', 26, 31)"),
 ("'Today reads the same and for the right reason: the level floor, the pier, the 3:20 boat back by 5. Rooms Remade ends tomorrow, so Sunday is the last chance at the rooms upstairs, on your own.'",
  "'Today: the level floor, the pier, and the 3:20 boat back by five. Sunday is the last day for the rooms upstairs, and you&rsquo;d be going on your own.'"),
 ("'Twice you planned a level afternoon here, with your father.', 'NO VISIT RECORDED'", "'Twice you planned a level afternoon here, with your father.', 'FROM YOUR PLANS'"),
 ("'Hours and tides as last seen Thursday · the listings are not reachable right now'", "'Hours and tides as of Thursday · the listings are down'"),
 ("MAYA, TUESDAY · &ldquo;TUESDAY, SEVEN.&rdquo; · NOTHING FRESH SINCE THURSDAY", "MAYA, TUESDAY · &ldquo;TUESDAY, SEVEN.&rdquo; · HER SHARE"),
 ("consequence('WHAT IS NOT FRESH', 'Every hour and every tide here is Thursday&rsquo;s. Nothing is invented to fill the gap, and nothing asks you to.')", "consequence('AS OF THURSDAY', 'Every hour and tide here is from Thursday.')"),
 ("'No times to keep · the workshop is open till 6 · the pier and the pool are on the way back'", "'The workshop&rsquo;s open till 6 · the pier and the pool are on the way back'"),
 ("level; that is the afternoon that serves you both, unless the workshop confirms a lift.", "level; that&rsquo;s the afternoon for you both, unless the workshop confirms a lift."),
 ("    inner += gut(photo_plate(150), top=16)\n", ""),
])

# ---------------- 04 ----------------
patch('gen20.py', [
 ("sub='Kept, with Maya') + gut(photo_plate(200), top=16)", "sub='Kept from Maya&rsquo;s share')"),
 ("fn('YOU KEPT THIS TO DO WITH MAYA, FROM HER SHARE', 8)", "fn('KEPT TUESDAY · FROM MAYA&rsquo;S SHARE', 8)"),
 ("the sentence says from, the fact line says kept, not yet arranged, and only her answer would make it with.", "the sentence says from, the line under it says an idea so far, and only her answer would make it with."),
 ("a photo slot is a hatched plate by default, so the scroll as drawn is the no-photograph state", "a place without a photograph has no plate, so the scroll as drawn is the no-photograph state"),
 ("Its photo slot, her words, the kept line;", "Her words, the kept line;"),
])

# ---------------- 08 ----------------
patch('gen08.py', [
 (CTX_OLD, CTX_NEW),
 ("'A print workshop on Van Brunt Street · the listing is not reachable right now'", "'A print workshop on Van Brunt Street · as of Thursday'"),
 ("upstairs by noon; nothing is arranged. Today, Red Hook", "upstairs by noon. Today, Red Hook"),
 ("relationship_trace('Kept Tuesday, from Maya&rsquo;s share.', 'NOT YET VISITED')", "relationship_trace('Kept Tuesday, from Maya&rsquo;s share.', '')"),
 ("relationship_trace('Kept Tuesday, from Maya&rsquo;s share; closed before a visit. The keeping stays in the record.', 'YOUR LAST VISIT · NONE')", "relationship_trace('Kept Tuesday, from Maya&rsquo;s share. It closed before you went.', '')"),
 ("relationship_trace('Kept Tuesday, from Maya&rsquo;s share; arranged Thursday.', 'NOT YET VISITED')", "relationship_trace('Kept Tuesday, from Maya&rsquo;s share; arranged Thursday.', '')"),
 ("The stairs are part of why it is still here.", "The stairs are part of why it&rsquo;s still here."),
 ("'The Harbor Book, ch. 4 · four minutes · read before you go, or not at all'", "'The Harbor Book, ch. 4 · four minutes'"),
 (", and today there is nothing in them.", ", and today they&rsquo;re dry."),
 ("    inner += gut(photo_plate(150), top=16)\n", ""),
])

# ---------------- 10 ----------------
patch('gen10.py', [
 (KEPT_SUB, NEW_SUB),
 ("'You are in New York · this is 8:41 in the morning there · nothing here is near you'", "'8:41 in the morning there · you&rsquo;re in New York'"),
 ("    inner += gut(fn('LOOKED UP FROM NEW YORK · NO DISTANCES FROM YOU, BECAUSE YOU ARE NOT THERE', 12), top=16)\n", ""),
 ("'You are in New York · this is 8:44 in the morning there'", "'8:44 in the morning there · you&rsquo;re in New York'"),
 ("    inner += gut(fn('THE SCOPE AND THE QUESTION ARE TWO CHIPS · EITHER COMES OFF ON ITS OWN', 12), top=16)\n", ""),
 ("'OPEN TILL 8 · NOBODY THERE AFTER SEVEN'", "'OPEN TILL 8 · EMPTY AFTER SEVEN'"),
 ("orientation('Nothing here is quiet at six on a Friday.', 'The question stands; the town does not answer it', 26, 31)", "orientation('At six on a Friday, only the bench walk is quiet.', 'Twenty minutes uphill from the piazza', 26, 31)"),
 ("K.live_fallback('WHAT IS TRUE INSTEAD', 'The cloister closes at eight and the market has gone. What is quiet at six is the bench walk, and it is twenty minutes uphill.')", "K.live_fallback('THE REST OF THE TOWN AT SIX', 'The market has packed up and the caf&eacute;s on Piazza Tasso are filling. The cloister empties after seven.')"),
 ("sect('Open at six, not quiet')", "sect('Open at six, and busy')"),
 ("    inner += gut(fn('BACK WHERE YOU WERE · THE SCOPE IS CLEAR, THE FIELD IS AS IT WAS, THE PLACE OF THE SCROLL IS KEPT', 12), top=16)\n", ""),
 ("    inner += gut(mark, top=8)\n", ""),
 ("    inner += gut(fn('ASKS VESPER, NOT THE WORKSHOP · MAYA IS NOT A RECIPIENT', 8), top=8)\n", ""),
 ("composer('Ask about the Print Room')", "composer('Ask Vesper about the Print Room')"),
 ("Opens your map app at Van Brunt Street. Vesper is not navigating and does not learn where you go.", "Opens Maps at Van Brunt Street. The route stays in Maps."),
 ("    inner += gut(fn('BACK FROM THE MAP APP · THE SAME POCKET, THE SAME SELECTION, THE SAME PLACE IN THE SCROLL', 12), top=8)\n", ""),
 ("    inner += gut(fn('LARGER TEXT · THE MAP&rsquo;S LABELS DO NOT GROW, SO THE POCKET READS AS ITS ROWS', 12), top=16)\n", ""),
 ("    inner += gut(fn('NARROW · THE MAP KEEPS ITS NUMBERS; THE NAMES ARE IN THE ROWS', 8), top=4)\n", ""),
 ("on its own listing while you were away. Rooms Remade", "on its own listing. Rooms Remade"),
 ("The marker takes a ring, the row takes the wash, and a line says which way the tap went. Nothing has opened yet", "The marker takes a ring and its row takes the wash. Nothing has opened yet"),
 ("The provider handoff states what Vesper does not do: it does not navigate and does not learn where the person goes.", "The provider handoff says where the route goes: to Maps, where it stays."),
])

# ---------------- kit: photo or nothing; an empty trace line stays empty ----------------
k = open('kit3.py').read()
a = k.index('def shelf_item('); b = k.index('\ndef ', a + 5)
k = k[:a] + '''def shelf_item(name, line, chip_):
    """A shelf tile. A place without its own photograph has no plate (photo or nothing), so the tile is its name, one line and one chip."""
    return (f'<div style="border-top: 1px solid {HAIR7}; padding-top: 10px;"><div style="font-size: 15px; font-weight: 600; letter-spacing: -0.2px; line-height: 19px; min-height: 38px;">{name}</div><div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; min-height: 34px;">{line}</div>'
            f'<span style="display: inline-block; {MONO} font-size: 10px; font-weight: 700; letter-spacing: 0.9px; color: {GOLDD}; border: 1px solid rgba(138,102,40,0.4); border-radius: 999px; padding: 2.5px 7px; margin-top: 6px;">{chip_}</span></div>')
''' + k[b:]
a = k.index('def cover('); b = k.index('\ndef ', a + 5)
old_cover = k[a:b]
k = k[:a] + '''def cover(svg_or_none, kick_t, t, h=186):
    """A reading's cover. With its own drawing or photograph it is a plate; without one it opens on its title (photo or nothing)."""
    if not svg_or_none:
        return (f'<div style="border-radius: 12px; background: {CARD}; border: 1px solid {HAIR}; padding: 14px 15px;"><div style="{MONO} font-weight: 700; font-size: 10px; letter-spacing: 1.2px; color: {GOLDD};">{kick_t}</div>'
                f'<div style="{SERIF} font-weight: 600; font-size: 20px; line-height: 24px; color: {INK}; margin-top: 4px;">{t}</div></div>')
''' + old_cover[old_cover.index('\n') + 1:].replace("    inner = svg_or_none or ''", "    inner = svg_or_none", 1) + k[b:]
open('kit3.py', 'w').write(k)
patch('kinds.py', [("{fn(sub, 3)}</div></div>'", "{fn(sub, 3) if sub else \'\'}</div></div>'")])

# ---------------- 07 and the index notes ----------------
patch('gen07.py', [
 ("The everyday six as pairs: a hatched photo slot, a sans name, one line, one mono chip", "The everyday six as pairs: a sans name, one line, one mono chip; a photograph only when a real one exists"),
 (" Photo or hatch, never a drawing.", " A photograph or no plate, never a drawing."),
 ("cell('photo slot · cover · ghost rows', 'canon', G(photo_plate(120) + '<div style=\"height: 12px;\"></div>' + cover(", "cell('reading · ghost rows', 'canon', G(cover("),
 ("Photo or hatch, never a drawing.", "A photograph or no plate, never a drawing."),
])
s = open('gen07.py').read()
s = re.sub(r"A photo slot is a hatched plate with its label[^']*'", "A reading without its own photograph opens on its title, not on an empty plate. Ghost rows hold the place of facts still loading.'", s, count=1)
open('gen07.py', 'w').write(s)
patch('renumber.py', [("A photo slot is a hatched plate, never a drawing.", "A place without a photograph has no plate.")])

# ---------------- American English, everywhere ----------------
BR = [('harbour', 'harbor'), ('Harbour', 'Harbor'), ('HARBOUR', 'HARBOR'), ('colour', 'color'), ('Colour', 'Color'), ('COLOUR', 'COLOR'), ('neighbourhood', 'neighborhood'),
      ('behaviour', 'behavior'), ('Behaviour', 'Behavior'), ('BEHAVIOUR', 'BEHAVIOR'), ('recognis', 'recogniz'), ('Recognis', 'Recogniz')]
for f in ['gen07.py', 'gen08.py', 'gen09.py', 'gen10.py', 'gen19v3.py', 'gen20.py', 'gen21.py', 'gen22.py', 'fix.py', 'kinds.py', 'kit3.py', 'instruments.py', 'renumber.py']:
    s = open(f).read(); t = s
    for x, y in BR: t = t.replace(x, y)
    if t != s: open(f, 'w').write(t)

# ---------------- the retired day charts leave the live library ----------------
s = open('instruments.py').read()
moved = []
for name in ('pier_day', 'pier_tracks', 'pier_arc_small'):
    m = re.search(r'\ndef ' + name + r'\(.*?(?=\ndef |\Z)', s, re.S)
    if m: moved.append(m.group(0)); s = s.replace(m.group(0), '', 1)
    else: fails.append(('instruments.py', 'retire ' + name))
still = [n for n in ('sun_y',) if ('def ' + n) in s and s.count(n + '(') == 1]
for n in still:
    m = re.search(r'\ndef ' + n + r'\(.*?(?=\ndef |\Z)', s, re.S); moved.append(m.group(0)); s = s.replace(m.group(0), '', 1)
open('instruments.py', 'w').write(s)
os.makedirs('archive/generators', exist_ok=True)
open('archive/generators/instruments_retired.py', 'w').write('"""The day charts retired on September 7-8 in favour of pier_line, and the helpers only they used. Kept for history; nothing live imports them.\nThe Stage 2 instrument brief flags their approximated sun and tide curves as something not to revive."""\nfrom instruments import *\n' + ''.join(moved))
for old in ('gen09_stages.py', 'gen19v3_sliced_backup.py', 'test_instr.py', 'test_pier.py'):
    if os.path.exists(old): os.replace(old, 'archive/generators/' + old)
print('moved', len(moved), 'functions; failures:'); [print('  ', f) for f in fails]
