"""Board 18 — Ordinary Photographs (September 21 additive assignment).
Same eligible material in three treatments (original-only, light context, earned enrichment), the selected Sunday full
scroll at ordinary and 1.3x text, open -> browse -> Reply or eligible private Ask -> return to the same Home position, and a
region-local image failure. Fixture: shared-fixture-world-2026-09-07.md §10 (PH-01..PH-07). The pictures are Life's drawn
stand-ins, reused verbatim from design-gen/life/build_0921.py so the three projects show the same picture; Life's viewer
anatomy (top bar, whole image, filmstrip, attribution, doors) is reused, opened from Home and returning to Home.
Copy: product copy and people's words inside the phone; provenance as "source · when"; reasons outside the phone.
Usage: python3 gen18.py <in_dir holding 12 and 00> <out_dir>
"""
import sys, os, re, html
IN, OUT = sys.argv[1], sys.argv[2]
sys.argv = [sys.argv[0], IN, OUT]
import gen_vdl as G

# Life's stand-ins, exactly as Life draws them.
LIFE = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'life', 'build_0921.py')).read()
seg = LIFE[LIFE.index('ASPECT = {'):LIFE.index('ORDER = [')]
ns = {'gut': lambda inner, top=12: f'<div style="margin:{top}px 22px 0 22px;">{inner}</div>'}
exec(seg, ns)
photo, tile, ASPECT = ns['photo'], ns['tile'], ns['ASPECT']
ORDER = ['PH-05', 'PH-02', 'PH-03', 'PH-01', 'PH-04']   # Life's order, by time

MONO, SERIF, SANS, CHEV = G.MONO, G.SERIF, G.SANS, G.CHEV
INK, MUTE, HINT, CARD, PAPER = '#1B1714', '#6E6862', '#8F877C', '#FBF7EC', '#EFEAE0'
fn, cell, notes, gold = G.fn, G.cell, G.notes, G.gold_door
opener, TAB = G.home_parts()
LIFT = 'box-shadow: 0 1px 2px rgba(27,23,20,0.05), 0 5px 14px rgba(27,23,20,0.07)'

def gut(inner, top=0): return f'<div style="padding: {top}px 22px 0 22px;">{inner}</div>'
def anchor(time):
    return (f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">'
            f'<span style="font-family: {MONO}; font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">NEW YORK &middot; SUNDAY</span>'
            f'<span class="fn" style="margin-left: auto;">{time}</span><span style="width: 24px; height: 24px; border-radius: 999px; background: #4A3428; color: {CARD}; font-size: 10px; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; margin-left: 10px; flex: none;">N</span></div></div>')
def read(title, sub):
    return (f'<div style="padding: 6px 22px 0 22px;"><div style="font-family: {SERIF}; font-weight: 600; font-size: 30px; line-height: 34px; letter-spacing: -0.01em; text-wrap: balance;">{title}</div>'
            f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 7px;">{sub}</div></div>')
def sect(name, top=40):
    return (f'<div style="padding: {top}px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 12px; padding-bottom: 10px;">'
            f'<span style="font-size: 13px; font-weight: 600; letter-spacing: 0.1px; color: {INK};">{name}</span><span style="flex: 1; height: 1px; background: rgba(27,23,20,0.12);"></span></div></div>')
def phone(*parts, tab=True): return opener + ''.join(parts) + '<div style="flex-grow: 1;"></div>' + (TAB if tab else '</div>')
def who(initial, name, when, bg=INK):
    return (f'<div style="display: flex; align-items: center; gap: 10px;"><span style="width: 28px; height: 28px; border-radius: 14px; background: {bg}; color: {CARD}; font-size: 12px; font-weight: 700; display: flex; align-items: center; justify-content: center; flex: none;">{initial}</span>'
            f'<span style="font-size: 13px; font-weight: 600; color: {INK};">{name}</span><span class="fn" style="color: {HINT};">{when}</span></div>')
def framed(pid, w=349, radius=6):
    return f'<div style="border-radius: {radius}px; overflow: hidden; width: {w}px;">{photo(pid, w=w)}</div>'
def row_of(pids, width=349, gap=6):
    h = (width - gap * (len(pids) - 1)) / sum(ASPECT[p] for p in pids)
    return f'<div style="display: flex; gap: {gap}px;">' + ''.join(tile(p, h) for p in pids) + '</div>'
REST = ['PH-05', 'PH-02', 'PH-03', 'PH-04']

# ---- the "Last night" region, three ways (same pictures, same grants) --------------------------------
def region(kind, failed=False, receipt=False):
    lead = (f'<div style="border-radius: 6px; overflow: hidden; width: 349px;">{tile("PH-01", 349 / ASPECT["PH-01"], failed=True)}</div>' if failed else framed('PH-01'))
    out = gut(who('M', 'Maya', 'SAT 8:25 PM') + f'<div style="margin-top: 12px;">{lead}</div>' + f'<div style="margin-top: 4px;">{gold("Reply to Maya")}</div>')
    if receipt:
        out += gut('<dc-import name="Notice" tone="applied" title="Sent to Maya &middot; 11:24" hint-size="349px,48px"></dc-import>', 4)
    label = '' if kind == 'original' else (f'<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 10px;"><span style="font-family: {SERIF}; font-size: 17px; line-height: 22px; font-weight: 500;">Pasta night &middot; at yours</span>'
                                           f'<span class="fn" style="color: {HINT}; margin-left: auto;">SAT &middot; SAM, MAYA</span></div>')
    out += gut(label + row_of(REST) + f'<div style="margin-top: 4px;">{gold("All five pictures")}</div>', 22)
    if kind == 'enriched':
        out += gut('<div style="border-top: 1px solid rgba(27,23,20,0.08); padding-top: 14px; display: flex; gap: 14px; align-items: flex-start;">'
                   f'<div style="flex: none; border-radius: 4px; overflow: hidden; border: 1px solid rgba(27,23,20,0.10);">{photo("PH-07", w=64)}</div>'
                   f'<div style="flex: 1; min-width: 0;"><div style="font-family: {SERIF}; font-size: 17px; line-height: 23px; color: {INK};">Next time, the step from the Nerano page you saved: pasta into the pan off the heat, then a ladle of its water.</div>'
                   + fn('YOUR SCREENSHOT &middot; THU 3:12 PM', mt=6) + f'<div style="margin-top: 2px;">{gold("The recipe page")}</div></div></div>', 20)
    return out

def unit_frame(inner):
    return f'<div style="width: 393px; background: {PAPER}; font-family: {SANS}; color: {INK}; box-sizing: border-box; padding: 4px 0 22px 0;">{sect("Last night", 20)}{inner}</div>'

row1 = ('<div style="display: flex; gap: 46px; align-items: flex-start;">'
        + cell('THE SAME PICTURES &middot; THE SAME GRANTS', 'A &middot; ORIGINAL ONLY', 'Who took it, when, and the pictures themselves',
               'PH-01 whole, the other four as one row that keeps their shapes', unit_frame(region('original')))
        + cell('THE SAME PICTURES &middot; THE SAME GRANTS', 'B &middot; LIGHT CONTEXT', 'The evening&rsquo;s own name on the set',
               'Only what the record already holds: Pasta night, at yours, Saturday', unit_frame(region('light')))
        + cell('THE SAME PICTURES &middot; THE SAME GRANTS', 'C &middot; THE SAVED STEP, REPEATED', 'Retrieval dressed as enrichment',
               'Uses PH-07 and PH-02, both Nora&rsquo;s; nothing from Maya&rsquo;s or Dana&rsquo;s pictures', unit_frame(region('enriched')))
        + notes([('SELECTED FOR SUNDAY', 'Maya&rsquo;s picture as it is (A): Nora was at the table, so a line about the evening would tell her what she already knows. The set carries the evening&rsquo;s name (B), because that name is how she&rsquo;ll find the five again. C is not selected.'),
                 ('C IS RETRIEVAL', 'C repeats a step from Nora&rsquo;s own saved page. That can be handy access, but it isn&rsquo;t new understanding, and dressing it as insight overstates it. A real enrichment would need a supported explanation, contrast or transfer beyond the page; this fixture supplies none, so none is drawn. In K the page appears as one row under Saved this week. Maya&rsquo;s and Dana&rsquo;s pictures get no addition.'),
                 ('SAME MATERIAL, SAME GRANTS', 'All three use PH-01 to PH-05 under the same grants. C adds only Nora&rsquo;s own screenshot; it reads nothing from Maya&rsquo;s or Dana&rsquo;s pictures, since their grants don&rsquo;t cover model use. Thursday&rsquo;s broken-sauce photo (A4) was attached to a question and not kept, so it cannot appear.')])
        + '</div>')

# ---- the selected full scroll ------------------------------------------------------------------------
crown = gut(f'<div style="background: {CARD}; border-radius: 16px; {LIFT}; padding: 16px 18px;">'
            f'<div style="font-family: {SERIF}; font-weight: 600; font-size: 20px; line-height: 24px;">Rooms Remade, last day</div>'
            f'<div style="font-size: 14px; line-height: 20px; color: #2C2622; margin-top: 6px;">The Harbor Print Room, Red Hook. Open until six; the side room is at the back.</div>'
            + fn('LISTING &middot; SUN', mt=10) + f'<div style="margin-top: 2px;">{gold("The way there")}</div></div>', 22)
city = (sect('The city this week')
        + gut(f'<div style="border-top: 1px solid rgba(27,23,20,0.06); padding-top: 10px;">{fn("OPEN HOUSE &middot; OCT 17&ndash;18", mt=0, color=MUTE)}'
              f'<div style="font-size: 15px; line-height: 20px; margin-top: 4px;">Registration for the timed sites opens Tuesday at noon; walk-in sites need none.</div></div>'))
def day(d, sub='', on=False):
    mk = f'background: {INK};' if on else 'border: 1px solid rgba(27,23,20,0.15); box-sizing: border-box;'
    return (f'<div style="flex: 1; display: flex; flex-direction: column; align-items: center; gap: 5px; padding: 8px 0 6px;"><span style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 0.8px; color: {INK if on else HINT};">{d}</span>'
            f'<span style="width: 7px; height: 7px; border-radius: 4px; {mk}"></span><span style="font-size: 10px; color: {MUTE if sub else "transparent"};">{sub or "."}</span></div>')
week = ('<div style="margin: 40px 0 0 0; border-top: 1px solid rgba(27,23,20,0.10); border-bottom: 1px solid rgba(27,23,20,0.06); padding: 2px 22px 4px;"><div style="display: flex;">'
        + day('SUN', 'today', True) + day('MON') + day('TUE', 'sign&#8209;ups') + day('WED') + day('THU') + day('FRI') + day('SAT') + '</div></div>'
        + f'<div style="padding: 16px 34px 6px 34px; text-align: center;"><div style="font-family: {SERIF}; font-size: 17px; line-height: 24px;">Rooms Remade, until six.</div></div>')
def scroll(time='11:20 AM', **kw):
    return phone(anchor(time), read('Rooms Remade closes at six today.', 'Clear and mild, 64&deg;.'),
                 crown, sect('Last night'), region('light', **kw), city, week)
def larger(h, k=1.3):
    return re.sub(r'(font-size|line-height): ([\d.]+)px', lambda m: f'{m.group(1)}: {float(m.group(2)) * k:.1f}px', h)

selected = scroll()
TIMEGLYPH = '<svg width="15" height="15" viewBox="0 0 15 15" fill="none" style="flex: none; opacity: 0.62; margin-top: 3px;"><path d="{d}" stroke="#1B1714" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def mrow(d, text, sub, last=False):
    b = '' if last else ' border-bottom: 1px solid rgba(27,23,20,0.06);'
    return (f'<div class="row" style="padding: 10px 0; align-items: flex-start;{b}">{TIMEGLYPH.format(d=d)}<div style="flex: 1; min-width: 0;">'
            f'<div style="font-size: 15px; line-height: 20px; color: {INK};">{text}</div><div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 2px;">{sub}</div></div><span style="padding-top: 3px;">{CHEV}</span></div>')
crown_rel = gut(f'<div style="background: {CARD}; border-radius: 16px; {LIFT}; padding: 16px 18px 6px;">'
                '<dc-import name="OriginalReader" density="open" author="Maya" meta="THU · TO FRIENDS" words="The side room was my favorite. Go on a weekday, it was empty." '
                'place="The Harbor Print Room" placeMeta="RED HOOK · ROOMS REMADE · UNTIL 6 TODAY" door="The way there" hint-size="313px,230px"></dc-import></div>', 22)
worth = (sect('Saved this week')
         + gut('<div class="row" style="padding: 8px 0; border-top: 1px solid rgba(27,23,20,0.06); border-bottom: 1px solid rgba(27,23,20,0.06);">'
               f'<div style="flex: none; border-radius: 3px; overflow: hidden; border: 1px solid rgba(27,23,20,0.10);">{photo("PH-07", h=44)}</div>'
               f'<div style="flex: 1; min-width: 0;"><div style="font-size: 15px; line-height: 20px; color: {INK};">Spaghetti alla Nerano</div>'
               + fn('YOUR SCREENSHOT &middot; THU 3:12 PM', mt=3) + f'</div>{CHEV}</div>'))
friends = gut(f'<div style="margin-top: 30px;">{gold("What your friends have shared")}{fn("PLACES &middot; FROM FRIENDS", mt=0)}</div>')
week2 = week.replace('Rooms Remade, until six.', 'Tuesday at noon, Open House sign&#8209;ups.')
def rich(time='11:20 AM'):
    return phone(anchor(time), read('Rooms Remade ends at six today.', 'Clear and mild, 64&deg; &middot; Maya&rsquo;s pictures from last night are below.'),
                 crown_rel, sect('Last night'), region('light'),
                 sect('In motion'), gut('<div style="border-top: 1px solid rgba(27,23,20,0.10);">'
                     + mrow('M1.5 9.5l12-6-4 9.5-2-3.5-6 0z', 'The Rome flight refund', 'The airline is reviewing it', last=True) + '</div>'),
                 worth, city, friends, week2)
richer = rich()
rowK = ('<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 44px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);">'
        + cell('SELECTED &middot; SUNDAY SEP 20, 11:20 AM', 'K &middot; THE FULL SCROLL', 'Maya&rsquo;s note leads; her pictures follow; the rest of Home stays',
               'Nora (Persona B) &middot; ledger &sect;10 &middot; pictures are drawn stand-ins', richer)
        + cell('THE SAME SCROLL AT 1.3&times; TEXT', 'L &middot; LARGER TEXT', 'Text grows; pictures keep their width and shapes',
               'Type &times;1.3, including the shared reader &middot; images unchanged', '<div class="lt">' + larger(richer) + '</div>')
        + notes([('WHY MAYA&rsquo;S NOTE LEADS', 'It&rsquo;s a friend&rsquo;s recommendation Nora can act on, and today is the last chance to. Her pictures come right after it: a direct offering that&rsquo;s complete as it is. Timing broke the tie between two things from Maya, weighed with who they&rsquo;re from and what Nora can do with them. On another day a friend&rsquo;s picture can lead.'),
                 ('THE REST OF HOME STAYS', 'What&rsquo;s still unfolding (the Rome refund), the recipe she saved this week, the city&rsquo;s week, friends&rsquo; places and the week ahead. Her 9:40 share to Maya got its receipt when she sent it and is findable in Life; a finished send isn&rsquo;t something in motion. These are the kinds of value the 02/03 scrolls carry; none is here as a quota.'),
                 ('SAID ONCE', 'The exhibition is named in the read and carried by Maya&rsquo;s note. The closing line now points to Tuesday&rsquo;s sign-ups instead of repeating it; the focused study (D) had it three times.'),
                 ('THE SAVED RECIPE', 'One row, as retrieval: the page she saved Thursday, a tap from last night&rsquo;s pictures. It claims nothing new about cooking. It would give way to more pressing value, and it drops off once the week it was saved in has passed.')], 520)
        + '</div>')
row2 = ('<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 44px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);">'
        + cell('FOCUSED STUDY &middot; SUNDAY SEP 20', 'D &middot; A NARROW SCROLL', 'The pictures with only a crown and the city around them',
               'Nora (Persona B) &middot; ledger &sect;10 &middot; pictures are drawn stand-ins', selected)
        + cell('THE STUDY AT 1.3&times; TEXT', 'E &middot; LARGER TEXT', 'Text grows; the pictures keep their width and shapes',
               'Every type size and leading &times;1.3 &middot; images unchanged', larger(selected))
        + notes([('A STUDY, NOT THE SELECTION', 'D isolates the pictures to test their placement and larger text. It is too thin to stand for Home; K is the selected scroll. Its crown and closing line both repeated the exhibition, which K fixes.'),
                 ('LETTING THEM STAY PICTURES', 'Natural color, full frame, no filter, no rounding beyond the page&rsquo;s small corner. Cohesion comes from the column width, the gap and the type around them. Board 13&rsquo;s warm-paper grade stays for reference images only.'),
                 ('A SET, NOT FIVE CARDS', 'One lead picture and one row for the rest, each at its own shape. &ldquo;All five pictures&rdquo; opens the set directly in the viewer, with no count cap and nothing implied about pictures that aren&rsquo;t shown.'),
                 ('LARGER TEXT', 'The copy reflows and the scroll grows; the pictures keep their width, so nothing is cropped harder at larger sizes.')])
        + '</div>')

# ---- open -> browse -> reply or ask -> return ------------------------------------------------------------
def topbar(label):
    return (f'<div style="padding: 24px 22px 0 22px; display: flex; align-items: center;"><svg width="20" height="20" viewBox="0 0 20 20" fill="none" style="flex: none;"><path d="M12.5 4L7 10L12.5 16" stroke="{INK}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
            f'<span style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: {MUTE}; margin-left: auto;">{label}</span></div>')
def filmstrip(current):
    return gut('<div style="display: flex; gap: 5px; align-items: center; justify-content: center;">'
               + ''.join(f'<div style="flex: none; border-radius: 3px; overflow: hidden; {"outline: 2px solid " + INK + "; outline-offset: 1px;" if p == current else "opacity: 0.75;"}">{photo(p, h=40)}</div>' for p in ORDER) + '</div>', 14)
def whole(pid):
    return f'<div style="margin-top: 14px;">{photo(pid, w=393) if ASPECT[pid] >= 0.74 else photo(pid, h=460, style="margin: 0 auto;")}</div>'
v1 = phone(topbar('PASTA NIGHT &middot; 4 OF 5'), whole('PH-01'), filmstrip('PH-01'), gut(who('M', 'Maya', 'SAT 8:25 PM'), 16), gut(gold('Reply to Maya'), 8))
v2 = phone(topbar('PASTA NIGHT &middot; 5 OF 5'), whole('PH-04'), filmstrip('PH-04'), gut(fn('YOUR CAMERA &middot; SAT 10:40 PM', mt=0, color=MUTE), 16),
           gut(gold('Ask about this') + gold('Share'), 8))
v3 = phone(topbar('PASTA NIGHT &middot; 4 OF 5'), whole('PH-01'), gut(who('M', 'Maya', 'SAT 8:25 PM'), 16),
           gut('<div class="vdl-field pill focused"><span class="vk-t-bodyMd">that table!! thank you</span></div>'
               '<div style="display: flex; align-items: center; gap: 12px; margin-top: 12px;"><span class="vdl-btn primary pill vk-t-labelSemibold" style="color: var(--vk-color-white); white-space: nowrap;">Send to Maya</span>'
               '<span class="vk-t-caption">She&rsquo;ll see this with her picture.</span></div>', 18))
ret = phone(anchor('11:24 AM'), sect('Last night', 24), region('light', receipt=True), city)
row3 = ('<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 44px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);">'
        + cell('OPEN &middot; FROM HOME', 'F &middot; MAYA&rsquo;S PICTURE, WHOLE', 'Life&rsquo;s viewer, opened straight from Home',
               'Back returns to Home &middot; the strip is the evening&rsquo;s five, in time order', v1)
        + cell('BROWSE', 'G &middot; ONE OF NORA&rsquo;S, AS TAKEN', 'Low light shown dark; her own picture can be asked about',
               'PH-04 &middot; the private Ask appears on her pictures only', v2)
        + cell('REPLY &middot; OPTIONAL', 'H &middot; TO MAYA, ABOUT HER PICTURE', 'Her picture stays above the words',
               'Shared field and Send pill (vdl.css) &middot; Social owns the recipient flow', v3)
        + cell('RETURN', 'I &middot; THE SAME PLACE IN THE SCROLL', 'Home at Last night, with one receipt under her picture',
               'Shared Notice, tone applied', ret)
        + '</div>'
        + '<div style="display: flex; gap: 46px; margin-top: 18px;">' + notes([
            ('THE PATH', 'Home&rsquo;s picture opens the viewer on that picture; the strip browses the evening&rsquo;s five; Reply and Ask are optional; Back lands on Last night at the same scroll position. Life leads the viewer&rsquo;s anatomy; the route doesn&rsquo;t pass through Life&rsquo;s index.'),
            ('ELIGIBILITY BY PICTURE', 'Maya&rsquo;s and Dana&rsquo;s pictures offer Reply to their author and nothing else: no Ask, Share or export, because their grants cover display only. Nora&rsquo;s own offer Ask and Share. Share hands off to Social&rsquo;s recipient flow.'),
            ('LEAVING IS AN ENDING', 'Opening the picture and going back, with no reply, is a complete visit. Nothing on Home changes if she does that.')], 860)
        + '</div>')

# ---- the connected path: one sequence, then its branches --------------------------------------------------
start = phone(anchor('11:20 AM'), sect('Last night', 24), region('light'), sect('In motion'))
v3c = phone(topbar('PASTA NIGHT &middot; 4 OF 5'), whole('PH-01'), gut(who('M', 'Maya', 'SAT 8:25 PM'), 16),
            gut(f'<div style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 1.1px; color: {MUTE}; margin-bottom: 6px;">DRAFT</div>'
                '<div class="vdl-field pill"><span class="vk-t-bodyMd" style="color: var(--vk-ink40);">that table!! thank you</span></div>', 18),
            gut(gold('Reply to Maya'), 8))
vfail = phone(topbar('PASTA NIGHT &middot; 4 OF 5'),
              f'<div style="margin-top: 14px;">{tile("PH-01", 393 / ASPECT["PH-01"], failed=True)}</div>', filmstrip('PH-01'),
              gut(who('M', 'Maya', 'SAT 8:25 PM'), 16), gut(gold('Reply to Maya'), 8))
def pathcell(n, head, title, sub, ph): return cell(head, f'{n}', title, sub, ph)
row3 = ('<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 44px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);">'
        + pathcell('1 &middot; ON HOME', 'THE PATH &middot; FROM HOME', 'Last night, in the selected scroll', 'The same region as K &middot; tap Maya&rsquo;s picture', start)
        + pathcell('2 &middot; OPEN', 'OPEN', 'Maya&rsquo;s picture, whole, in Life&rsquo;s viewer', 'Opened straight from Home &middot; Back returns to 1', v1)
        + pathcell('3 &middot; BROWSE', 'BROWSE', 'The evening&rsquo;s five; one of Nora&rsquo;s, low light as taken', 'Her own picture offers Ask and Share (&rarr; Social)', v2)
        + pathcell('4 &middot; REPLY', 'REPLY &middot; OPTIONAL', 'To Maya, under her picture', 'Shared field and Send pill &middot; Social owns the send', v3)
        + '</div>'
        + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 34px;">'
        + pathcell('5a &middot; CANCEL', 'FROM 4 &middot; CANCEL', 'Back in the viewer; the words kept as a draft', 'Nothing sent &middot; Back from here still lands on 1', v3c)
        + pathcell('5b &middot; SEND, THEN BACK', 'FROM 4 &middot; SEND', 'Home at Last night, one receipt under her picture', 'Shared Notice, tone applied &middot; same scroll position', ret)
        + pathcell('2&prime; &middot; WON&rsquo;T LOAD', 'FROM 1 &middot; THE PICTURE FAILS', 'The viewer keeps the frame, the strip and Reply', 'Life&rsquo;s failed-tile anatomy &middot; retry in place', vfail)
        + notes([('ONE PATH, ALREADY SCRIPTED', '1 &rarr; 2 &rarr; 3 &rarr; 4, then cancel (5a) or send (5b). Life 04c scripts this frame navigation, including Home&rsquo;s direct viewer entry and return; Home does not add a third walkthrough. The same viewer is Life 04b&rsquo;s and Social 10&rsquo;s.'),
                 ('OUTCOMES COME FROM SOCIAL 10P', 'Cancel keeps the words and Home is unchanged; a confirmed send adds one receipt (5b). A partial send offers a retry for the undelivered picture only; an uncertain one offers a status check, not a resend. Home copies none of these states.'),
                 ('ELIGIBILITY BY PICTURE', 'Maya&rsquo;s and Dana&rsquo;s pictures offer Reply to their author only; their grants cover display. Nora&rsquo;s own offer a private Ask and Share. Opening a picture and going back is a complete visit.'),
                 ('EXERCISED VS PICTURED', 'Exercised by 04c/10P: switching between these predetermined frames. Pictured only, on 18: the typed draft surviving cancel (5a), the same scroll position on return (5b), the viewer failure (2&prime;). No script holds an editable field or real scroll offset, so those stay unverified. No message is sent; 17&rsquo;s delivery and access cases stay with their owners.')])
        + '</div>')

# ---- one picture that won't load --------------------------------------------------------------------------
broken = phone(anchor('11:20 AM'), read('Rooms Remade closes at six today.', 'Clear and mild, 64&deg;.'),
               crown, sect('Last night'), region('light', failed=True), city)
row4 = ('<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 44px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);">'
        + cell('ONE PICTURE WON&rsquo;T LOAD', 'J &middot; A REGION, NOT THE PAGE', 'Its frame keeps its shape and offers a retry',
               'Life&rsquo;s failed-tile anatomy &middot; the rest of Home is unaffected', broken)
        + notes([('WHAT STAYS', 'Maya&rsquo;s name and time, Reply to Maya, the other four pictures, the crown and the city section. The frame holds the picture&rsquo;s shape, so nothing jumps when it arrives. 12&rsquo;s region-local states are the donors.'),
                 ('NOT DRAWN HERE', 'PH-06, the lemons with no date or place, stays in Life&rsquo;s Photographs, unplaced; Home doesn&rsquo;t ask anyone to sort it. PH-07, the recipe screenshot, appears only where it helps (treatment C).'),
                 ('GAPS', 'Every picture is a drawn stand-in. Real color, texture and low-light noise can&rsquo;t be judged until approved photographs are supplied (ledger &sect;10). Pinch, swipe, caching and image performance are native checks.')])
        + '</div>')

header = ('<div style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 26px;">'
          '<div class="kick">VESPER &middot; HOME &middot; 18 &middot; ORDINARY PHOTOGRAPHS &middot; ADDITIVE ASSIGNMENT 2026-09-21</div>'
          f'<div style="font-family: {SERIF}; font-weight: 600; font-size: 30px; line-height: 36px; letter-spacing: -0.01em;">18 &middot; Last night&rsquo;s pictures on Sunday&rsquo;s Home</div>'
          f'<div style="font-size: 14px; line-height: 21px; color: {MUTE}; max-width: 980px;">The shared photo set (ledger &sect;10): Maya&rsquo;s picture of the table, Nora&rsquo;s own from the evening, Dana&rsquo;s dish from Sorrento. '
          'The same pictures in three treatments; the selected Sunday scroll (K) at ordinary and larger text, with a narrower focused study beside it; one connected path from a picture to Reply or Ask and back, with cancel and failure; and a picture that won&rsquo;t load on Home. '
          'Extends 13&rsquo;s rule (a person&rsquo;s own photographs are never color-treated), 09&rsquo;s forms and 02/03&rsquo;s selected scrolls. The pictures are Life&rsquo;s drawn stand-ins, identical across Life, Home and Social.</div></div>')

CSS = ('.fn { font-family: ' + MONO + '; font-size: 10px; letter-spacing: 0.9px; color: #B5AFA5; }\n'
       '    .kick { font-family: ' + MONO + '; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: #8A6628; }\n'
       '    .kickm { font-family: ' + MONO + '; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: #6E6862; }\n'
       '    .shead { display: flex; align-items: center; gap: 10px; font-family: ' + MONO + '; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: #6E6862; }\n'
       '    .shead .rule { flex: 1; height: 1px; background: rgba(27,23,20,0.10); }\n'
       '    .row { display: flex; align-items: center; gap: 12px; min-height: 44px; border-top: 1px solid rgba(27,23,20,0.06); }\n'
       '    .row:first-child { border-top: none; }\n    .chev { flex: none; }\n'
       '    .lt .vdl-t-excerpt { font-size: 23.4px; line-height: 32.5px; }\n    .lt .vdl-t-sectionHeading, .lt .vk-t-bodySmMedium { font-size: 16.9px; }\n    .lt .vdl-t-metaLine { font-size: 13px; }\n    .lt .vdl-t-placeName { font-size: 20.8px; line-height: 26px; }\n    :root { --ink: #1B1714; --card: #FBF7EC; --mute: #6E6862; --paper: #EFEAE0; --sans: ' + SANS + '; --mono: ' + MONO + '; }')
board = ('<div style="width: 2000px; min-height: 8259px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; font-family: ' + SANS + '; color: #1B1714; display: flex; flex-direction: column;">'
         + header + row1 + rowK + row2 + row3 + row4
         + '<div class="fn" style="margin-top: 30px; line-height: 16px;">EVERY PERSON, PLACE, TIME AND PICTURE IS A DESIGN FIXTURE &middot; THE PICTURES ARE DRAWN STAND-INS FOR APPROVED PHOTOGRAPHS &middot; REASONS STAY OUTSIDE THE PHONE</div></div>')
out = ('<!doctype html>\n<html>\n<head>\n<meta charset="utf-8">\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
       '  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=JetBrains+Mono:wght@400;700&display=swap">\n'
       f'  <link rel="stylesheet" href="{G.KERNEL}">\n  <link rel="stylesheet" href="vdl.css">\n  <style>\n    body {{ margin: 0; }}\n    a {{ color: #8A6628; }}\n    {CSS}\n  </style>\n</helmet>\n'
       + board + '\n</x-dc>\n</body>\n</html>\n')
open(f'{OUT}/18 - Ordinary Photographs.dc.html', 'w').write(out)
print('wrote 18', len(out), 'svg pictures', out.count('role="img"'), 'notices', out.count('name="Notice"'))

h = G.rd('00')
TD = '<td style="font-size: 12.5px; line-height: 17px; color: #2C2622; padding: 8px 10px 8px 0; border-bottom: 1px solid rgba(27,23,20,0.06); vertical-align: top;">'
r18 = ('<tr>' + TD + '18 - Ordinary Photographs</td>' + TD + 'Additive assignment (09-21): the shared photo set (ledger &sect;10) on Sunday&rsquo;s Home &mdash; the same pictures as original-only, light context and earned enrichment; the selected full scroll (K) at ordinary and 1.3&times; text; one connected path, picture &rarr; viewer &rarr; Reply or eligible Ask &rarr; cancel or send &rarr; the same place in the scroll; image failure on Home and in the viewer. Life&rsquo;s stand-ins and viewer anatomy</td>'
       + TD + 'Additive &middot; 09-21 &middot; drawn stand-ins</td></tr>')
i = h.find('17 - Delivery and Return</td>'); j = h.find('</tr>', i) + 5
assert i > 0
open(f'{OUT}/00 - Index.dc.html', 'w').write(h[:j] + r18 + h[j:]); print('wrote 00 with the 18 row')
