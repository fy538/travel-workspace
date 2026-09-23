"""Shared design-language adoption on Vesper — Home (2026-09-11).
Consumes vdl-stage1 0.3 from workbench c13ae951 (OriginalReader at its 0.4 reader correction, the only live version).
Usage: python3 gen_vdl.py <in_dir> <out_dir> [board keys...]
  in_dir holds the current boards, byte-identical to the live project; changed boards are written to out_dir.
Adoption is bounded to shared construction that preserves the selected design:
  * Maya's note (Home 02 selected ordinary scroll, and its copy on 08b) -> OriginalReader density=open
  * the gold door (Door.tsx: 13/500 gold text + the one arrow) -> .vdl-door, in phones of the boards touched here
  * kernel styles.css + vdl.css linked in each touched board's helmet
Named cleanups the shared package already applied to Home's own donor (M19, 02D judgement pass), applied to Home's drawing
because Ticket admission cannot host Home's way-there instrument or the upcoming pass (reported as missing variants):
  * reserved violet -> ink on the admission pass, pass labels 8px -> 10px, each fact once on the live pass.
"""
import re, sys, os
IN, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)
KEYS = sys.argv[3:]
NAMES = {'00': '00 - Index', '02': '02 - Persona A - The New Yorker', '04': '04 - Persona C - New User', '08': '08 - Seam with Life',
         '08b': '08b - Seam with Life - Home to Life', '09': '09 - Forms', '12': '12 - Why This, Chat, and Degraded States'}
KERNEL = '_ds/vesper-production-kernel-fc85e38a-72e6-4b40-98a7-fb447dd94529/styles.css'

def rd(k): return open(f'{IN}/{NAMES[k]}.dc.html').read()
def wr(k, h): open(f'{OUT}/{NAMES[k]}.dc.html', 'w').write(h); print('wrote', NAMES[k], len(h))
def must(h, old, new, n=1):
    c = h.count(old)
    if c != n: raise SystemExit(f'expected {n} of {old[:90]!r}, found {c}')
    return h.replace(old, new)

def link(h):
    """Kernel then vdl.css, ahead of the board's own <style> so Home's local classes are untouched."""
    if 'href="vdl.css"' in h: return h
    i = h.find('<helmet>'); k = h.find('<style>', i)
    return h[:k] + f'<link rel="stylesheet" href="{KERNEL}">\n  <link rel="stylesheet" href="vdl.css">\n  ' + h[k:]

def phone_regions(h):
    out = []
    for m in re.finditer(r'<div style="width: 393px;[^"]*background: #EFEAE0', h):
        s = m.start(); depth = 0; e = None
        for mm in re.finditer(r'<div\b|</div>', h[s:]):
            depth += 1 if mm.group() == '<div' else -1
            if depth == 0: e = s + mm.end(); break
        if e and not (out and s < out[-1][1]): out.append((s, e))
    return out

def in_phones(h, fn):
    for s, e in reversed(phone_regions(h)): h = h[:s] + fn(h[s:e]) + h[e:]
    return h

# The gold door as every Home generator draws it, and the shared construction that replaces it.
DOOR = re.compile(r'<span style="font-size: 13px; font-weight: 500; color: #8A6628;">([^<]*)</span><svg width="13" height="13" viewBox="0 0 13 13" fill="none" style="margin-left: 6px;"><path d="M2 6.5H10M6.5 3L10 6.5L6.5 10" stroke="#8A6628" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>')
def doors(h):
    n = [0]
    def f(p):
        p2, k = DOOR.subn(r'<span class="vdl-door vk-t-bodySmMedium">\1</span>', p); n[0] += k; return p2
    h = in_phones(h, f); print('  doors -> .vdl-door:', n[0]); return h

# Maya's note, uncarded, with the Lilia row and the door inside the unit (Home 02 "In motion").
NOTE_OPEN = '<div style="padding: 6px 0 14px 0; border-bottom: 1px solid rgba(27,23,20,0.06); display: flex; flex-direction: column; overflow: hidden;">'
def note_markup(h):
    s = h.find('The current ordinary scroll')
    i = h.find('>M</span><span style="font-size: 13px; font-weight: 600; color: #1B1714;">Maya</span>', s)
    a = h.rfind(NOTE_OPEN, 0, i)
    if a < 0: raise SystemExit('note: unit opener not found')
    depth = 0
    for mm in re.finditer(r'<div\b|</div>', h[a:]):
        depth += 1 if mm.group() == '<div' else -1
        if depth == 0: return h[a:a + mm.end()]
READER = ('<div style="padding: 6px 0 14px 0; border-bottom: 1px solid rgba(27,23,20,0.06);">'
          '<dc-import name="OriginalReader" density="open" author="Maya" meta="AUG 30 · TO YOU" '
          'words="…and if you two ever want a proper pasta night — Lilia. Ask for the corner table." '
          'place="Lilia" placeMeta="TONIGHT AT EIGHT · WITH MAYA · ARRANGED" door="Tonight, at Lilia" hint-size="349px,200px"></dc-import></div>')

def b02():
    h = rd('02'); note = note_markup(h)
    assert 'Tonight, at Lilia' in note and 'Ask for the corner table' in note
    n = h.count(note); print('  note instances on 02:', n)
    h = h.replace(note, READER)
    return doors(link(h)), note


MONO = "'JetBrains Mono', ui-monospace, monospace"; SERIF = "'EB Garamond', Georgia, serif"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif"
ARROW = '<svg width="13" height="13" viewBox="0 0 13 13" fill="none" style="margin-left: 6px;"><path d="M2 6.5H10M6.5 3L10 6.5L6.5 10" stroke="#8A6628" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
CHEV = '<svg class="chev" width="13" height="13" viewBox="0 0 13 13" fill="none"><path d="M4.5 2.5L9 6.5L4.5 10.5" stroke="#B5AFA5" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
HATCH = 'background: repeating-linear-gradient(135deg, rgba(176,133,58,0.14) 0 7px, rgba(176,133,58,0.05) 7px 14px); border: 1px solid rgba(27,23,20,0.08); box-sizing: border-box'
def gold_door(t): return f'<div style="display: flex; align-items: center; min-height: 44px;"><span class="vdl-door vk-t-bodySmMedium">{t}</span></div>'
def ink_door(t): return f'<div style="display: flex; align-items: center; min-height: 44px;"><span style="font-size: 13px; font-weight: 500; color: #1B1714;">{t}</span>{ARROW}</div>'
def fn(t, color='#8F877C', mt=0): return f'<div class="fn" style="margin-top: {mt}px; color: {color};">{t}</div>'
def cell(shead, kick, title, sub, phone, w=393):
    return (f'<div style="width: {w}px; flex: none; display: flex; flex-direction: column;"><div class="shead" style="color: #8A6628; margin-bottom: 10px;"><span>{shead}</span><span class="rule"></span></div>'
            f'<div style="display: flex; flex-direction: column; gap: 3px; padding: 0 0 10px 2px;"><div class="kick" style="color: #8A6628;">{kick}</div>'
            f'<div style="font-family: {SERIF}; font-weight: 600; font-size: 17px; line-height: 22px; color: #1B1714; text-wrap: balance;">{title}</div>'
            f'<div style="font-family: {SANS}; font-size: 12px; line-height: 17px; letter-spacing: 0; color: #6E6862; max-width: 393px;">{sub}</div></div>{phone}</div>')
def notes(blocks, w=560):
    out = f'<div style="width: {w}px; flex: none; display: flex; flex-direction: column; gap: 22px; padding-top: 24px;">'
    for k, t in blocks: out += f'<div style="display: flex; flex-direction: column; gap: 8px;"><div class="kickm">{k}</div><div style="font-size: 12.5px; line-height: 18px; color: #2C2622;">{t}</div></div>'
    return out + '</div>'
def balanced(h, i):
    depth = 0
    for mm in re.finditer(r'<div\b|</div>', h[i:]):
        depth += 1 if mm.group() == '<div' else -1
        if depth == 0: return i + mm.end()
TABBAR = '<div style="border-top: 1px solid rgba(27,23,20,0.10); background: #EFEAE0; display: flex; padding: 10px 22px 22px 22px; margin-top: 28px;">'

def chat_parts():
    """Header and tail (Chat-active tab bar) of 12's seeded Chat turn, the Home project's own Chat drawing."""
    h = rd('12'); s, e = phone_regions(h)[3]; p = h[s:e]
    assert 'SUNDAY 9:12 AM' in p
    head = p[:p.find('<div style="padding: 26px 22px 0 22px;">')]
    tail = p[p.find('<div style="flex-grow: 1;"></div>'):]
    return head, tail
def home_parts():
    h = rd('12'); s, e = phone_regions(h)[0]; p = h[s:e]
    t = p.find(TABBAR); return p[:p.find('>') + 1], p[t:balanced(p, t)] + '</div>'

def pass_cleanup(h):
    """M19: the reserved violet becomes ink, as on 02D; pass labels from 8px to the 10px floor."""
    a = h.count('#7C5BA8'); h = h.replace('#7C5BA8', '#3C352E')
    b = h.count('rgba(124,91,168,0.10)'); h = h.replace('rgba(124,91,168,0.10)', 'rgba(27,23,20,0.05)')
    assert 'rgba(124,91,168' not in h
    LAB = 'font-size: 8px; font-weight: 700; letter-spacing: 1px; color: #B5AFA5;'
    c = h.count(LAB); h = h.replace(LAB, LAB.replace('8px', '10px'))
    print(f'  violet -> ink: {a} + {b} tints; pass labels 8 -> 10px: {c}; 8px left: {h.count("font-size: 8px")}')
    return h
def live_pass(h):
    """02D judgement pass, by Home 09's own rule: each fact once. Doors in the fields, leave-by in the status line, FRIDAY in the date slot."""
    n = h.count('TONIGHT &middot; DOORS 8:00</span>')
    h, k1 = re.subn(r'(ADMISSION &middot; THE HALL</span><span style="[^"]*margin-left: auto; white-space: nowrap;">)TONIGHT(</span>)', r'\1FRIDAY\2', h)
    h = h.replace('TONIGHT &middot; DOORS 8:00</span>', 'TONIGHT &middot; LEAVE BY 7:05</span>')
    h = h.replace('>Doors 8 &middot; set times posted at 6</span>', '>Set times posted at 6</span>')
    h, k2 = re.subn(r'<div style="display: flex; flex-direction: column; gap: 2px;"><span style="[^"]*">LEAVE BY</span><span style="[^"]*">7:05</span></div>', '', h)
    assert n == k1 == k2, (n, k1, k2)
    print('  live passes, each fact once:', n); return h

def b04():
    h = rd('04')
    s2 = h.find('2 &middot; AFTER &middot; THIN-CONTEXT CHECK')
    DOORROW = 'Try with yours</span>' + ARROW + '</div></div>'
    SUBLINE = fn('OPENS CHAT &middot; READ FOR THE ANSWER, NOT KEPT')
    pre, post = h[:s2], h[s2:]
    k = post.count(DOORROW); post = post.replace(DOORROW, DOORROW + SUBLINE); h = pre + post
    print('  04.2/04.6 shortcut names its doorway:', k)
    h = must(h, 'OPENS CHAT &middot; A PHOTO OR A FORWARDED EMAIL</div>', 'OPENS CHAT &middot; A PHOTO OR A FORWARDED EMAIL &middot; READ FOR THE ANSWER, NOT KEPT</div>')
    h = pass_cleanup(h)
    head, tail = chat_parts()
    def chat(time, blocks): return head.replace('SUNDAY 9:12 AM', time) + ''.join(blocks) + tail
    chip = ('<div style="padding: 26px 22px 0 22px;"><div style="display: inline-flex; align-items: center; gap: 8px; border: 1px solid rgba(27,23,20,0.10); background: #FBF7EC; border-radius: 12px; padding: 8px 12px;">'
            f'<span style="width: 6px; height: 6px; border-radius: 3px; background: #B0853A;"></span><span style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 1px; color: #1B1714;">THE SAMPLE TICKET &middot; FROM HOME</span></div>'
            '<div style="font-size: 12.5px; line-height: 17px; color: #6E6862; margin-top: 10px;">Your photo arrives as support for one answer. It is read, not kept.</div></div>')
    def photo(w, hh, note=True):
        n = fn('SENT AS A PHOTO &middot; NO QUESTION NEEDED', mt=6) if note else ''
        return (f'<div style="padding: 22px 22px 0 22px;"><div style="display: flex; flex-direction: column; align-items: flex-end;"><div style="width: {w}px; height: {hh}px; border-radius: 14px; {HATCH}; display: flex; align-items: flex-end; padding: 8px 10px;">'
                f'<span class="fn" style="color: #6E6862;">YOUR PHOTO &middot; A TICKET</span></div>{n}</div></div>')
    field = '<div style="padding: 30px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px; min-height: 44px; border: 1px solid rgba(27,23,20,0.12); border-radius: 999px; padding: 0 16px;"><span style="font-size: 14px; color: #B5AFA5; flex: 1;">Ask about your ticket</span></div></div>'
    answer = (f'<div style="padding: 18px 22px 0 22px;"><div style="max-width: 330px; display: flex; flex-direction: column; gap: 10px;"><div style="font-family: {SERIF}; font-size: 17px; line-height: 24px; color: #1B1714;">'
              'Saturday at The Hall, doors at 7. Arrive by 7:40 and you miss nothing; set times go up the day before. After ten, the way home is the surface route, 25 minutes longer.</div>'
              + fn('FROM YOUR PHOTO + THE HALL&rsquo;S LATE SERVICE &middot; FIXTURE ANSWER') + '</div></div>')
    receipt = ('<div style="padding: 16px 22px 0 22px;"><div style="border-top: 1px solid rgba(27,23,20,0.08); padding-top: 12px;">' + fn('YOUR PHOTO WAS READ FOR THIS ANSWER &middot; NOT KEPT', color='#6E6862')
               + '<div style="display: flex; gap: 20px; align-items: center; margin-top: 2px;">' + ink_door('Keep it in Life') + gold_door('Back to Home') + '</div></div></div>')
    f1 = cell('TUESDAY 8:07 &middot; FROM 04.2', '1 &middot; THE DOORWAY IT INVOKES', 'Try with yours opens Chat, as Ask with the photo attached',
              'Contract &sect;3.2: a supporting attachment to Ask is transient &middot; no wizard, no Keep step', chat('TUESDAY 8:07 AM', [chip, photo(220, 146), field]))
    f2 = cell('TUESDAY 8:07 &middot; THE ANSWER', '2 &middot; THE USEFUL ANSWER, FIRST', 'Their own ticket, read the way the sample was',
              'Doors, the arrive-by, the way home &middot; nothing booked, saved or shared', chat('TUESDAY 8:07 AM', [chip, photo(184, 118, False), answer, field]))
    f3 = cell('TUESDAY 8:08 &middot; AFTER', '3 &middot; THE RECEIPT, OR ITS ABSENCE', 'Not kept, said once; keeping is a separate choice',
              'Keep it in Life is the deliberate Bring on 04.4 &middot; Back returns to Home unchanged', chat('TUESDAY 8:08 AM', [photo(184, 118, False), answer, receipt]))
    nb = notes([('THE TRACE &middot; SEPTEMBER 10 CLARIFICATION', '04.2&rsquo;s &ldquo;Try with yours&rdquo; opens Chat as Ask with the photo attached (Contribution and Consequence &sect;3.2: a supporting attachment to Ask is transient). The answer comes first, read from their ticket the way the sample was read. One line says the photo was read for this answer and not kept. &ldquo;Keep it in Life&rdquo; is optional: it is the deliberate Bring that 04.3 describes and 04.4 draws, kept in Life with one-tap Undo. Back returns to Home as it was: no chip, no receipt row.'),
                ('WHAT CHANGED ON 04 &middot; 09-11', 'The shortcut on 04.2 and 04.6 now names its doorway beneath it (&ldquo;Opens Chat &middot; read for the answer, not kept&rdquo;), and 04.3&rsquo;s line carries the same clause. The admission sample on 04.3 lost the reserved violet (ink, as on 09) and its labels are at 10px. Gold doors on this board are the shared Door construction (vdl.css <span style="font-family: ' + MONO + '; font-size: 11.5px;">.vdl-door</span>).'),
                ('NOT CLAIMED', 'That every ticket question is kept, or that a static board proves retention behaviour. An existing agreement is identified, never inferred from an upload.')])
    row = ('<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);">' + f1 + f2 + f3 + nb + '</div>')
    h = must(h, '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 34px; border-top: 1px solid rgba(27,23,20,0.12);">',
             row + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 34px; border-top: 1px solid rgba(27,23,20,0.12);">')
    return doors(link(h))

def b0809(k):
    return doors(link(live_pass(pass_cleanup(rd(k)))))

def b08b(note):
    h = rd('08b'); print('  note instances on 08b:', h.count(note)); h = must(h, note, READER)
    i = h.find('5 &middot; CHANGED RETURN'); j = h.find('ROW EIGHT', i); seg = h[i:j]
    seg = must(seg, '<span class="fn" style="margin-left: auto;">11:20 AM</span>', '<span class="fn" style="margin-left: auto;">11:52 AM</span>')
    seg = must(seg, 'Sorrento to Capri: the 11:20 ticket unused, the 2:40 boat, the stairs at 2:05, the island by 4:12',
               'Sorrento to Capri: the stairs at 2:05, the 2:40 boat, the island by 4:12; the 11:20 ticket unused')
    seg = must(seg, '>11:20</span><span class="fn" style="color: #8F877C; font-size: 9px; line-height: 11px; text-align: center;">TICKET</span>',
               '>11:20</span><span class="fn" style="color: #8F877C; font-size: 9px; line-height: 11px; text-align: center;">UNUSED</span>')
    h = h[:i] + seg + h[j:]
    h = must(h, 'BACK TO HOME &middot; THE IMPORT FINISHED MEANWHILE', 'BACK TO HOME &middot; 11:52 AM &middot; THE IMPORT FINISHED MEANWHILE')
    return doors(link(h))

def b12():
    h = rd('12')
    h = must(h, 'Contract &sect;3.8: correct, exclude, release, Open the sources &middot; writes nothing about you',
             'Contract &sect;3.8 &middot; only what applies here: open the sources, ask, exclude, correct &middot; release is for an interpretation of you, and none is held &middot; writes nothing about you')
    h = must(h, 'The envelope arrives &middot; no second composer on Home &middot; existing boundary',
             'The envelope arrives &middot; Chat keeps its own field &middot; back returns to the sequence, same scroll position')
    h = must(h, 'ANSWER ONLY &middot; THE SEQUENCE ON HOME IS UNCHANGED UNTIL YOU ASK TO CHANGE IT</div>',
             'ANSWER ONLY &middot; THE SEQUENCE ON HOME IS UNCHANGED UNTIL YOU ASK TO CHANGE IT</div>' + gold_door('Back to Today, in order'))
    opener, tab = home_parts()
    top = (f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;"><svg width="20" height="20" viewBox="0 0 20 20" fill="none" style="flex: none;"><path d="M12.5 4L7 10L12.5 16" stroke="#1B1714" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
           f'<span style="font-family: {MONO}; font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">WHY THIS &middot; SOURCES</span><span class="fn" style="margin-left: auto;">SUNDAY 9:11 AM</span></div></div>'
           f'<div style="padding: 20px 22px 0 22px;"><div style="font-family: {SERIF}; font-weight: 600; font-size: 22px; line-height: 27px; text-wrap: balance;">Where the four degrees came from</div>'
           '<div style="font-size: 12.5px; line-height: 17px; color: #6E6862; margin-top: 6px;">Each row opens its original. Nothing here is newer than its read time.</div></div>')
    def sect(n): return (f'<div style="padding: 30px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 12px; padding-bottom: 6px;"><span style="font-size: 13px; font-weight: 600; letter-spacing: 0.1px; color: #1B1714;">{n}</span><span style="flex: 1; height: 1px; background: rgba(27,23,20,0.12);"></span></div></div>')
    def srow(key, t, m, last=False):
        b = '' if last else ' border-bottom: 1px solid rgba(27,23,20,0.06);'
        return (f'<div class="row" style="padding: 10px 0; align-items: flex-start;{b}"><span style="width: 15px; flex: none; font-family: {MONO}; font-size: 10px; font-weight: 700; color: #6E6862; padding-top: 4px;">{key}</span>'
                f'<div style="flex: 1; min-width: 0;"><div style="font-size: 15px; line-height: 20px; color: #1B1714;">{t}</div>{fn(m, mt=3)}</div><span style="padding-top: 4px;">{CHEV}</span></div>')
    rows = ('<div style="padding: 0 22px;">' + srow('1', 'The waterfront station', '0.4 MI FROM YOUR WALK &middot; READ 6:00 PM &middot; 24&deg; AT 9 PM') + srow('2', 'The avenue station', 'TWO STREETS IN &middot; READ 6:00 PM &middot; 28&deg; AT 9 PM')
            + srow('3', 'Tonight&rsquo;s forecast', 'ISSUED 6:00 AM &middot; WIND OFF THE WATER') + srow('M', 'Why water and masonry differ', 'ONE AUTHORED ENTRY &middot; AN EXPLANATION, NOT A MEASUREMENT', last=True) + '</div>')
    yours = '<div style="padding: 0 22px;">' + srow('Y', 'Your Thursday walk', 'TWO MOVEMENT ROWS &middot; KEPT IN LIFE', last=True) + '</div>'
    foot = ('<div style="padding: 18px 22px 0 22px;">' + fn('THE FOUR-DEGREE FIGURE IS READ FROM 1 AND 2 TONIGHT; IT CHANGES WHEN THEY DO') + gold_door('Back to Why this') + '</div>')
    phone = opener + top + sect('Sources') + rows + sect('Yours') + yours + foot + '<div style="flex-grow: 1;"></div>' + tab
    c = cell('THE SOURCES', '2B &middot; OPEN THE SOURCES', 'The door lands on the sources themselves',
             'The destination the sheet names &middot; a person&rsquo;s words would open in the shared reader (16)', phone)
    nb = notes([('WHAT CHANGED ON 12 &middot; 09-11', '&ldquo;Open the sources&rdquo; now has a drawn destination (2b): the two stations, the forecast and the authored mechanism, each opening its original, and your walk in Life. The sheet&rsquo;s annotation names only the controls it offers: release is for an interpretation of you, and this unit holds none. The Chat turn (4) names its origin, Today, in order, and returns there at the same scroll position; Chat keeps its own field. Gold doors are the shared Door construction.'),
                ('DEGRADED STATES STAY REGION-LOCAL', 'Stale, provider unknown and import pending remain lines inside the affected unit, with unaffected content usable. The shared Notice is a boxed banner; using it here would add the banner these frames deliberately avoid, so it is not adopted and the missing inline variant is reported on 16.'),
                ('FIXTURES', 'Station distances, read times and temperatures are design fixtures, as everywhere on this board.')])
    row = '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + c + nb + '</div>'
    R2 = '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">'
    h = must(h, R2, row + R2)
    return doors(link(h))


READER_HOME_ETAG = os.environ.get('READER_HOME_ETAG', 'UNSET')
NAMES.update({'07': '07 - Ledger and Decisions', '16': '16 - Shared Language Adoption'})
BEFORE = 'Before VDL 0.3 - '
def b00():
    h = rd('00')
    h = must(h, 'Thirteen current boards in reading order', 'The current boards in reading order')
    TD = '<td style="font-size: 12.5px; line-height: 17px; color: #2C2622; padding: 8px 10px 8px 0; border-bottom: 1px solid rgba(27,23,20,0.06); vertical-align: top;">'
    h = must(h, 'Second pass · 09-09 · proposed</td>', 'Second pass · 09-09 · 15.3&ndash;15.4 selected (09-09 decision); the rest proposed</td>')
    row16 = ('<tr>' + TD + '16 - Shared Language Adoption</td>' + TD + 'Shared design-language adoption (09-11): what Home consumes from the workbench package (vdl-stage1 0.4.1 = 0.3 plus the reader correction and the practical-metadata patch), matched live before/after crops of every changed frame, the construction status of the selected scroll, the open &rarr; reply or private Ask &rarr; return continuation on shared components, the missing variants reported instead of built, and the September 10 coverage and recheck items</td>'
             + TD + 'Adoption · 09-11 · the before boards are kept</td></tr>'
             + '<tr>' + TD + 'Before VDL 0.3 - 02, 04, 08, 08b, 09, 12</td>' + TD + 'The six changed boards exactly as they stood before the adoption, kept as before references for 16&rsquo;s live comparisons</td>' + TD + 'Before references · frozen 09-11</td></tr>')
    i = h.find('15 - Learning and Steering</td>'); j = h.find('</tr>', i) + 5
    return h[:j] + row16 + h[j:]
def b07():
    h = rd('07')
    return must(h, 'large-text renders; native behaviour; participant evidence.', 'large-text behaviour beyond the 1.3&times; renders on 09b; native behaviour; participant evidence.')

def ref(path, sig, y=None, hh=None, w=393):
    a = f' data-y="{y}"' if y is not None else ''
    b = f' data-h="{hh}"' if hh is not None else ''
    return f'<div class="cmp-ref" style="width:{w}px" data-ref="{path}" data-sig="{sig}"{a}{b}></div>'
def pair(label, file, sig, y=None, hh=None, w=393, cap=''):
    return ('<div class="vk-t-monoStampStrong" style="color:var(--vk-gold80);margin-top:26px">' + label + '</div><div class="vdl-lane">'
            f'<div class="vdl-cell"><span class="vdl-tag orig vk-t-capsMicro">BEFORE · {BEFORE}{file.split(" - ")[0]}</span>{ref(BEFORE + file + ".dc.html", sig, y, hh, w)}</div>'
            f'<div class="vdl-cell"><span class="vdl-tag vk-t-capsMicro">AFTER · {file.split(" - ")[0]}</span>{ref(file + ".dc.html", sig, y, hh, w)}</div>'
            f'<div class="vdl-cell side"><p class="vk-t-bodySm" style="margin:26px 0 0;color:var(--vk-ink40)">{cap}</p></div></div>')
def table(heads, rows, minw=1100):
    out = f'<div class="vdl-scroll" style="margin-top:8px"><table class="vdl-table pk" style="min-width:{minw}px"><tr>' + ''.join(f'<th class="vk-t-capsMicro">{x}</th>' for x in heads) + '</tr>'
    for r in rows: out += '<tr>' + ''.join(f'<td class="{"vk-t-bodySmMedium" if i == 0 else "vk-t-bodySm"}">{c}</td>' for i, c in enumerate(r)) + '</tr>'
    return out + '</table></div>'
def sec(t): return f'<div class="vdl-rule"></div><div class="vk-t-monoStampStrong" style="color:var(--vk-gold80)">{t}</div>'
NOTE_PROPS = ('author="Maya" meta="AUG 30 · TO YOU" words="…and if you two ever want a proper pasta night — Lilia. Ask for the corner table." '
              'place="Lilia" placeMeta="TONIGHT AT EIGHT · WITH MAYA · ARRANGED" door="Tonight, at Lilia"')
def b16():
    P02, P04, P08b, P09, P12 = NAMES['02'], NAMES['04'], NAMES['08b'], NAMES['09'], NAMES['12']
    consumed = table(['File in Home', 'Identity (as in the workbench package)', 'Used on'], [
        ['_ds/…/styles.css (kernel)', 'sha256 a843ca5b… · 29,657 bytes · travel-app@e2e792913 tokens:80d0648dd300 gen:1', 'every changed board: tokens and type roles'],
        ['vdl.css', 'sha256 7b6fa1d3… · 16,055 bytes · its version string reads 0.3; unchanged in 0.4', 'every changed board: .vdl-door, and the roles inside the components'],
        ['OriginalReader.dc.html', 'etag 1789153753071940 · 13,559 bytes · 0.4.1: the §21.2 reader correction and the §22.2 practical-metadata patch', '02 ×2, 08b ×1, the continuation below ×4'],
        ['Notice.dc.html', 'etag 1789081717510486 · 2,531 bytes', 'the return frame below only'],
        ['vdl-refs.js', 'workbench instrument, not package', 'this board’s live crops']])
    status = table(['Region of the selected ordinary scroll', 'Construction now', 'Owner · next trigger'], [
        ['In motion · Maya’s note', 'Component-built: OriginalReader density=open', 'Shared owner, then native mapping'],
        ['Gold doors', 'Shared construction: .vdl-door (Door.tsx) on 02, 04, 08, 08b, 09 and 12; the other boards draw the same door and move when next edited', 'Shared owner'],
        ['Orientation: place stamp, mast, condition line, avatar', 'Home drawing on kernel values; placeStamp is an owner naming call', 'Home, after the role review'],
        ['Today, in order: sequence line, stops, OR, source line', 'Home-owned; no shared specimen (F03)', 'Home adoption'],
        ['Rows with icons and chevrons', 'Home drawing; F04 targeted addition', 'Kernel steward'],
        ['Paired figures, numbered method, reading card', 'Home drawing; unitTitle and stepNumeral are proposed roles', 'Kernel steward, when the roles are adopted'],
        ['Section headings', 'Home drawing matches the proposed sectionHeading, 13/600', 'textVariants owner'],
        ['Week strip, closing line, tab bar', 'Home-owned (F08); .vdl-tabbar has the geometry but not the icons', 'Home']])
    missing = table(['Where', 'What the shared component lacks', 'What Home keeps meanwhile', 'Owner'], [
        ['09, 08 · the live admission pass', 'Ticket admission has no place between its fields and band. Home’s consequence, way-there instrument and one ask sit there, and §19.4 keeps the instrument Home’s.', 'Home’s drawn pass with the cleanups the package applied to it: violet to ink, labels at 10px, each fact once', 'Shared owner'],
        ['08, 09 · the upcoming admission pass', 'No state without a status line; the band’s right label is always oxblood, where UPCOMING is a quiet stamp', 'Home’s drawn pass, same cleanups', 'Shared owner'],
        ['12.5–12.7 · stale, provider unknown, import pending', 'Notice is only a boxed banner. Home’s selected states are lines inside the affected region, with no banner.', 'Home’s region-local lines', 'Shared owner: an inline Notice'],
        ['Secondary doors · Try with yours, Keep it in Life', '.vdl-door has one tone; Home’s non-purpose door is ink text with the gold arrow', 'Home’s drawn secondary door', 'Shared owner'],
        ['OriginalReader · the practical place line', 'Resolved in 0.4.1 (§22.6): “TONIGHT AT EIGHT · WITH MAYA · ARRANGED” moves from ink80 (1.82:1) to ink60 (4.59:1). It is now darker than Home drew it (#8F877C, 2.96:1) because the kernel has no readable token between the two; a lighter value would be a palette decision. The date beside her name stays ink80 as quiet provenance.', 'The shared patch, consumed; no local override', 'Resolved · kernel color owner for any in-between token'],
        ['OriginalReader open · door', 'No 44px row around the door, which Home reserved; the door sits 12px under the place row', 'Adopted; the hit area is a native check', 'Shared owner'],
        ['OriginalReader full · place row and glyph', 'Always draws a thumbnail, so Lilia, which has no image, shows the patterned fallback (frame 2 below); the utensil glyph does not suit every place. Both are requested as bounded variants: an optional thumbnail and a neutral or supplied place glyph (§22.4, in the manifest’s extension queue).', 'The fallback, unforced: no image added to Lilia', 'Shared owner · requested'],
        ['Span instruments, crown sequence, week strip, reconstruction strip', 'No shared specimen', 'Home-owned drawings', 'Home; kernel steward when a second consumer needs one']], 1200)
    coverage = table(['Item', 'Disposition', 'Drawn now', 'Owner · next trigger'], [
        ['12.1–12.2 · inspect door and Why this', 'Existing donor + targeted addition', '“Open the sources” lands on the sources (12, 2b). The annotation names only the controls offered; release is not offered because the unit holds no interpretation of you.', 'Home · native check of the sheet'],
        ['12.3–12.4 · Chat aperture', 'Owner dependency', 'The origin is named (Today, in order); Back returns to the same scroll position; Chat keeps its own field and Home gains no composer', 'Chat owner · keyboard, focus and restore in native'],
        ['12.5–12.7 · stale, provider unknown, partial import', 'Existing donor (Home) + shared gap', 'Kept region-local, with unaffected content usable; Notice not adopted (see above)', 'Shared owner · inline Notice'],
        ['11.1–11.2 return and next open; 15.3–15.4', 'Existing donor · later native check', 'Unchanged: original first, compact updates, local steering; no catch-up task, no durable preference from a temporary one', 'Home + engineering · native mapping'],
        ['Human original · open → Reply or private Ask → return', 'Shared donor', 'The continuation above, on OriginalReader 0.4 and Notice', 'Shared owner · review']], 1200)
    recheck = table(['September 10 item', 'Found in the current export', 'Changed', 'Still open'], [
        ['04.2 · Try with yours', 'The shortcut opened Chat with nothing saying what happens to the photo', 'The doorway is named under 04.2 and 04.6 and on 04.3; a trace row on 04 shows Ask, the answer first, “not kept”, and the optional Keep, which is 04.4’s Bring', '—'],
        ['08b HL-3 · the returned sequence', 'Frame 5 already drew 2:40 SAILED with 11:20 as the unused ticket. But its clock read 11:20 AM, before the 11:48 correction; the headline listed the 2:40 boat before the 2:05 stairs; and the 11:20 mark read TICKET on 5 and UNUSED on 4.', 'Clock 11:52 AM; headline in time order; the mark reads UNUSED', 'Life’s own day page after the correction, which Life P3 owns'],
        ['02/03 · hierarchy (residual 1)', 'The selected scrolls lead with the benefit and keep the commitments, the human original, the method and the forward possibility (first pair above)', 'Nothing', 'A founder read of 03’s rich scrolls against 14 and 15’s treatment'],
        ['15 · the later piece’s value (residual 3)', '15.4–15.7 follow one subject; the later piece’s added value is argued in 15’s notes, not demonstrated against a repeat', 'Nothing', 'Open: a repeated mechanism still has to earn its reappearance'],
        ['Selection map (residual 4)', '00 still marked 15 as proposed; 07 listed large-text renders as not shown, though 09b exists', '00: 15.3–15.4 selected, the rest proposed; 07 points to 09b', '—'],
        ['Larger text', '09b records the selected scrolls at 1.3×. The adopted 02 phone was rechecked at 320px and at 1.3× text: nothing spills or clips.', '—', 'Native Dynamic Type']], 1200)
    spec = lambda inner, cap, tag: (f'<div class="vdl-cell"><span class="vdl-tag vk-t-capsMicro">{tag}</span><div class="spec">{inner}</div><p class="vk-t-caption cmp-cap">{cap}</p></div>')
    cont = ('<div class="vdl-lane">'
        + spec('<div class="vdl-t-sectionHeading" style="margin-bottom:12px">In motion</div>' + f'<dc-import name="OriginalReader" density="open" {NOTE_PROPS} hint-size="349px,200px"></dc-import>',
               'The same instance as 02. Her words open the original; the Lilia door goes to the arrangement, which Plans owns.', '1 · ON HOME · IN MOTION')
        + spec('<dc-import name="OriginalReader" density="full" author="Maya" audience="Aug 30 · to you" words="…and if you two ever want a proper pasta night — Lilia. Ask for the corner table." place="Lilia" placeDetail="Tonight at eight · with Maya" placeMeta="ARRANGED IN PLANS" ask="Ask about Lilia" hint-size="349px,420px"></dc-import>',
               'No media, so the reader opens on her words. Lilia has no image; the thumbnail is the component’s fallback, and an optional-thumbnail variant is requested rather than an image added.', '2 · HER NOTE, OPENED')
        + spec('<dc-import name="OriginalReader" density="full" author="Maya" audience="Aug 30 · to you" words="…and if you two ever want a proper pasta night — Lilia. Ask for the corner table." compose="Corner table it is. See you at eight." ask="Ask about Lilia" hint-size="349px,420px"></dc-import>',
               'Her words stay above the field; Send names her.', '3 · REPLY, IN CONTEXT')
        + '<div class="vdl-cell"><span class="vdl-tag vk-t-capsMicro">4 · OR ASK VESPER PRIVATELY</span><div class="vdl-phone"><div class="vdl-status"><span class="vk-t-navLabel">9:13</span><span class="vk-t-monoStamp">CHAT</span></div><div class="vdl-page">'
          '<div class="vk-r-flatObject" style="padding:8px 12px;margin-top:6px"><span class="vk-t-monoStampStrong">MAYA’S NOTE · PRIVATE · MAYA SEES NOTHING</span></div>'
          '<div class="cmp-right" style="margin-top:14px"><div class="cmp-bubble"><span class="vk-t-chatTranscript" style="color:var(--vk-color-white)">do we have to ask for the corner table?</span></div></div>'
          '<p class="vk-t-chatTranscript" style="margin:14px 0 0">Her note says to ask for it. The Lilia arrangement in Plans doesn’t record a table request, and nothing about seating has been checked.</p>'
          '<div class="vdl-t-metaLine" style="margin-top:6px;color:var(--vk-ink80)">FROM MAYA’S NOTE + THE ARRANGEMENT · FIXTURE ANSWER</div>'
          '<div class="vdl-doors" style="margin-top:16px"><span class="vdl-door vk-t-bodySmMedium">Back to Maya’s note</span></div></div></div>'
          '<p class="vk-t-caption cmp-cap">Chat as its owner built it; only the context chip and the way back are drawn.</p></div>'
        + spec('<div class="vdl-t-sectionHeading" style="margin-bottom:12px">In motion</div>' + f'<dc-import name="OriginalReader" density="open" {NOTE_PROPS} hint-size="349px,200px"></dc-import>'
               + '<div style="margin-top:10px"><dc-import name="Notice" tone="applied" title="Sent to Maya · 9:14" body="Nothing else here changed." hint-size="349px,64px"></dc-import></div>',
               'Home at In motion, the same scroll position. The result sits under the note, as on the shared continuation; the note is unchanged.', '5 · RETURN · THE SAME PLACE IN THE SCROLL')
        + '</div>')
    body = (
        '<div class="vk-t-capsEyebrow">Vesper — Home · 16 · shared design-language adoption · 2026-09-11</div>'
        '<div class="vk-t-h1Large" style="margin-top:6px">The shared language, adopted where it keeps Home’s selected design</div>'
        '<p class="vk-t-body" style="max-width:860px;margin:8px 0 0;color:var(--vk-ink40)">Home consumes the workbench package as versioned copies. Where a shared component carries the selected design, the drawing is now that component. Where it cannot, Home’s drawing stays and the missing variant is named below instead of being built here. The originals are kept as “Before VDL 0.3” boards, and every comparison is a live crop of the same frame from the before and after files, at the same width.</p>'
        '<div class="vk-t-monoStamp" style="margin-top:10px">PACKAGE VDL-STAGE1 0.4.1 (0.3 + THE §21.2 READER CORRECTION + THE §22.2 METADATA PATCH) · KERNEL travel-app@e2e792913 tokens:80d0648dd300 · CROPS ARE LIVE · FIXTURE CONTENT · NOTHING HERE PROVES NATIVE BEHAVIOUR</div>'
        + sec('WHAT HOME CONSUMES · RECORDED IN vdl-consumed.json') + consumed
        + '<p class="vk-t-bodySm" style="margin:8px 0 0;max-width:860px;color:var(--vk-ink40)">Not copied: Ticket, InviteCard, PlaceHead, FactPair, SourceList, ActionGroup, LocationFooter and PlaceIdentity. No Home region would take one of them without its design changing; see the missing variants.</p>'
        + sec('MATCHED BEFORE AND AFTER · THE SAME FRAMES, LIVE')
        + pair('HOME 02 · THE SELECTED ORDINARY SCROLL, WHOLE', P02, 'The current ordinary scroll', 108, None, 393,
               'Same content, assets and width. Maya’s note is now OriginalReader; the gold doors are .vdl-door; kernel and vdl.css are linked. Everything else is Home’s drawing, unchanged. The phone is 5px shorter.')
        + pair('IN MOTION · MAYA’S NOTE, CLOSER', P02, 'The current ordinary scroll', 683, 260, 393,
               'Kept: uncarded, avatar, name and date, her words at 18/25, the Lilia row, the door inside the unit. Changed by the component: the date beside her name is quiet provenance (ink80); since 0.4.1 the arrangement line reads at ink60; the place glyph is the reader’s; the door sits under the place row without Home’s 44px row.')
        + pair('09 · THE ADMISSION PASS, STANDARD AND LIVE', P09, 'HELD-OBJECT INSTRUMENT', 60, None, 440,
               'Home’s drawing, because Ticket admission cannot hold the way-there instrument or the upcoming state. The package’s cleanups for this donor are applied: the reserved violet is ink, labels are 10px, and each fact is stated once (FRIDAY in the date slot, leave-by in the status line, doors in the fields).')
        + pair('08b HL-3 · FRAME 5, THE CHANGED RETURN', P08b, 'Same position, one more photograph', 0, 900, 393,
               'The clock now follows the 11:48 correction (11:52 AM); the headline runs in time order; the 11:20 mark reads UNUSED, as on frame 4. The strip and its 2:40 sailing were already right.')
        + pair('04.2 · THE SHORTCUT NAMES ITS DOORWAY', P04, 'signature as the sample', None, None, 393,
               'Under “Try with yours”: opens Chat, read for the answer, not kept. The trace is a new row on 04.')
        + pair('12 · 4 · THE CHAT TURN RETURNS', P12, 'Answer only; Home is unchanged until asked', None, None, 393,
               'The turn names its origin and returns to Today, in order, at the same scroll position. The new sources destination (2b) is a new row on 12.')
        + sec('CONSTRUCTION STATUS · HOME 02, THE SELECTED ORDINARY SCROLL') + status
        + sec('CONTINUATION · OPEN → REPLY OR PRIVATE ASK → RETURN · SHARED COMPONENTS') + '<div class="vk-t-monoStamp" style="margin-top:4px">SIMULATED STATES FOR REVIEW · MAYA’S LILIA NOTE THROUGHOUT</div>' + cont
        + sec('MISSING VARIANTS · REPORTED, NOT BUILT LOCALLY') + missing
        + sec('COVERAGE FOLLOW-THROUGH · SEPTEMBER 10') + coverage
        + sec('SEPTEMBER 10 ADDITIVE REVIEW · RECHECKED, NOT REPEATED') + recheck)
    return ('<!DOCTYPE html>\n<html>\n  <head>\n    <meta charset="utf-8" />\n    <meta name="viewport" content="width=device-width, initial-scale=1" />\n    <script src="./support.js"></script>\n  </head>\n  <body>\n    <x-dc>\n      <helmet data-dc-atomics>\n'
            f'        <link rel="stylesheet" href="{KERNEL}" />\n        <link rel="stylesheet" href="vdl.css" />\n        <script src="vdl-refs.js"></script>\n        <style>\n'
            '          .cmp-ref{background:var(--vk-paper30);width:393px;min-height:240px}\n          .cmp-cap{max-width:393px;color:var(--vk-ink40)}\n'
            '          .spec{width:393px;box-sizing:border-box;background:var(--vk-paper20);padding:22px;border-radius:var(--vk-radius-chromeDock);box-shadow:var(--vk-shadow-lg)}\n'
            '          .cmp-bubble{max-width:280px;background:var(--vk-color-action-primary);border-radius:18px;padding:10px 14px}\n          .cmp-right{display:flex;justify-content:flex-end}\n'
            '          .side{max-width:420px}\n          .pk td{font-size:12.5px}\n        </style>\n      </helmet>\n'
            f'      <div class="vdl-board" data-screen-label="16 Shared Language Adoption">{body}</div>\n    </x-dc>\n'
            '    <script type="text/x-dc" data-dc-script data-props=\'{}\'>\n      class Component extends DCLogic {\n        componentDidMount() {\n'
            '          const go = (n) => { if (window.vdlMountRefs) { window.vdlMountRefs(); } else if (n < 60) { setTimeout(() => go(n + 1), 200); } };\n          go(0);\n        }\n        renderVals() { return {}; }\n      }\n    </script>\n  </body>\n</html>\n')
def consumed_json():
    import json
    return json.dumps({
        'consumer': 'Vesper — Home (42876b8c-0d3a-40b2-9420-a953f095d8d1)', 'recorded': '2026-09-11',
        'package': 'vdl-stage1 0.4.1', 'package_note': 'First adopted at 0.4 (09-11, §22 of the Home response). 0.4.1 changes only OriginalReader: the practical place line (placeMeta) moves from ink80 to ink60; provenance stays ink80 (brief §22.6). vdl.css, Notice and the kernel copy are byte-unchanged. Use this manifest for identity, not the vdl.css version string (it still reads 0.3).',
        'workbench': 'c13ae951-0977-4bac-90a6-c964146a9ca6', 'workbench_manifest_etag': '1789154045511825',
        'kernel': 'travel-app@e2e792913 tokens:80d0648dd300 gen:1',
        'files': [
            {'path': KERNEL, 'kind': 'styles', 'sha256': 'a843ca5ba6fe7595ff05c629ed88be8f3051e073a51cda4500e18ee5910d7f6c', 'bytes': 29657, 'home_etag': '1789146510111502'},
            {'path': 'vdl.css', 'kind': 'styles', 'sha256': '7b6fa1d3dfccc92c59be1193cd68cdb032845a54c0316540e3ab58fe0b968515', 'bytes': 16055, 'source_etag': '1789098141934217', 'home_etag': '1789146510274930'},
            {'path': 'OriginalReader.dc.html', 'kind': 'component', 'bytes': 13559, 'source_etag': '1789153753071940', 'home_etag': READER_HOME_ETAG, 'previous': '0.4 · source etag 1789145625170950 · 13,175 bytes'},
            {'path': 'Notice.dc.html', 'kind': 'component', 'bytes': 2531, 'source_etag': '1789081717510486', 'home_etag': '1789146510591686'},
            {'path': 'vdl-refs.js', 'kind': 'workbench instrument (not package)', 'bytes': 2585, 'source_etag': '1789081717510486', 'home_etag': '1789146510749859'}],
        'instances': {'OriginalReader density=open': ['02 (selected ordinary scroll + its history copy)', '08b (row six)', '16 (continuation 1 and 5)'],
                      'OriginalReader density=full': ['16 (continuation 2 and 3)'],
                      'reader instances with a place line, affected by 0.4.1': ['02 ×2', '08b ×1', '16 ×3 (continuation 1, 2 and 5)'], 'Notice tone=applied': ['16 (continuation 5)'],
                      '.vdl-door': ['02', '04', '08', '08b', '09', '12', '16']},
        'before_references': [BEFORE + NAMES[k] + '.dc.html' for k in ('02', '04', '08', '08b', '09', '12')],
        'rule': 'Changes flow from the shared owner. Do not edit these copies in Home; re-copy a newer version and record it here.'}, indent=2, ensure_ascii=False) + '\n'

def stamp(h, n):
    """Root min-height, measured headless after the added row (content height, 2800px viewport)."""
    h2, k = re.subn(r'(width: \d{4}px; min-height: )\d{4,}px', lambda m: m.group(1) + f'{n}px', h, count=1); assert k == 1; return h2

def build(k):
    if k == '02': h, _ = b02(); wr('02', h)
    elif k == '04': wr('04', stamp(b04(), 3003))
    elif k in ('08', '09'): wr(k, b0809(k))
    elif k == '08b': _, note = b02(); wr('08b', b08b(note))
    elif k == '12': wr('12', stamp(b12(), 4896))
    elif k == '00': wr('00', b00())
    elif k == '07': wr('07', b07())
    elif k == '16': wr('16', b16())
    elif k == 'json': open(f'{OUT}/vdl-consumed.json', 'w').write(consumed_json()); print('wrote vdl-consumed.json')
    else: raise SystemExit('unknown board ' + k)

for k in KEYS: build(k)
