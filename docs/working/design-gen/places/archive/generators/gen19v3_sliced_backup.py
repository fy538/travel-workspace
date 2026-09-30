"""19 v3 · the synthesis with the canon's instruments (founder, 09-07 late). Rebuilt from the pushed HTML after the generator scratchpad was lost:
the head, tail, tab bar and the parity/§12 columns are lifted verbatim from the pushed 19; the new scroll reuses the parity column's sections
where they already fit and replaces the opening, the everyday six, the pocket's access, the evening's time, the comparison and the reading
with kinds and instruments from the a26e3228 canon (field_lead_composition, the daylight arc, the tide curve, field_browse_shelf, the burden strip,
the day band, path_difference_diagram, field_editorial_cover). Hatched plates are photo slots, never drawings."""
import os, re, sys, subprocess
from instruments import pier_day, access_compare, section as ground_section
S = lambda f: open(os.path.join('src', f)).read()
p19 = S('p19.html'); parity = S('col_parity.html'); s12 = S('col_s12.html'); notes = S('notes_col.html'); tail = S('tail.html'); foot = S('footblock.html'); tabbar = S('tabbar.html')
HEAD = p19[:p19.find('<div style="width: 1900px')]
i0 = p19.find('<div style="width: 1900px'); r0 = p19.find('<div style="display: flex; gap: 46px; align-items: flex-start;">')
BOARD_OPEN = p19[i0:p19.find('>', i0)+1]; HEADBLOCK = p19[p19.find('>', i0)+1:r0]
INK='#1B1714'; MUTE='#6E6862'; ANCHOR='#8F877C'; GOLD='#B0853A'; GOLDD='#8A6628'; CARD='#FBF7EC'; WASH='#E8E2D4'; WATER='#3D5066'; PAPER='#EFEAE0'
MONO="font-family: 'JetBrains Mono', ui-monospace, monospace;"; SERIF="font-family: 'EB Garamond', Georgia, serif;"
CHEV = '<svg width="13" height="13" viewBox="0 0 13 13" fill="none" style="flex: none;"><path d="M4.5 2.5L9 6.5L4.5 10.5" stroke="#B5AFA5" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARROW = lambda c=GOLDD: f'<svg width="13" height="13" viewBox="0 0 13 13" fill="none" style="margin-left: 6px;"><path d="M2 6.5H10M6.5 3L10 6.5L6.5 10" stroke="{c}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
HATCH = 'repeating-linear-gradient(135deg, rgba(176,133,58,0.12) 0 6px, rgba(176,133,58,0.04) 6px 12px)'
LB = f'font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="{MUTE}"'
LG = f'font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="{GOLDD}"'
LK = f'font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="{INK}"'

# ── a pushed column, sliced into its sections ──
class Col:
    def __init__(self, html, sects):
        self.ph = html.find('<div style="width: 393px; min-height'); self.cap = html[:self.ph]
        self.open = html[self.ph:html.find('>', self.ph)+1]; self.inner = html[html.find('>', self.ph)+1:]
        self.sects = sects; self.pos = {k: self._sect_pos(k) for k in sects}
        self.doors_at = self.inner.find('<div style="padding: 30px 22px 0 22px;">', self.pos[sects[-1]]); self.tab_at = self.inner.find('<div style="flex-grow: 1;"></div>')
        self.top = self.inner[:self.inner.find('<div style="padding: 20px 22px 0 22px;">')].replace('<span class="fn" style="margin-left: auto;">', '<span class="fn" style="margin-left: auto; color: #6E6862;">'); self.doors = self.inner[self.doors_at:self.tab_at].replace('min-height: 44px;', 'min-height: 40px;')
    def _sect_pos(self, label):
        m = self.inner.find(f'letter-spacing: 0.1px; color: #1B1714;">{label}</span>'); assert m > 0, label
        return self.inner.rfind('<div style="padding: 40px 22px 0 22px;">', 0, m)
    def section(self, label):
        i = self.sects.index(label); a = self.pos[label]; b = self.pos[self.sects[i+1]] if i+1 < len(self.sects) else self.doors_at
        return self.inner[a:b].replace('<div style="padding: 40px 22px 0 22px;">', '<div style="padding: 36px 22px 0 22px;">', 1).replace('color: #8F877C;', 'color: #6E6862;').replace('min-height: 44px;"><span style="font-size: 13px; font-weight: 500;', 'min-height: 40px;"><span style="font-size: 13px; font-weight: 500;')
POP = Col(parity, ['From friends', 'Any day', 'Red Hook, by ferry', 'Saturday evening', 'Worth understanding', 'Seen up close', 'Sunday', 'Saturday morning, downtown'])
COLD = Col(S('col_cold_only.html'), ['Any day', 'Red Hook, by ferry', 'Saturday evening', 'Worth understanding', 'Sunday', 'Saturday morning, downtown'])
CAP_TPL = POP.cap; PHONE_OPEN = POP.open
def section(label, col=None): return (col or POP).section(label)
def sect(t): return f'<div style="padding: 36px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 12px; padding-bottom: 10px;"><span style="font-size: 13px; font-weight: 600; letter-spacing: 0.1px; color: {INK};">{t}</span><span style="flex: 1; height: 1px; background: rgba(27,23,20,0.12);"></span></div></div>'
def gut(h, top=0): return f'<div style="padding: {top}px 22px 0 22px;">{h}</div>'
def kick(t): return f'<div style="display: flex; align-items: center; gap: 10px; {MONO} font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: {GOLDD};"><span>{t}</span><span style="flex:1;height:1px;background:rgba(27,23,20,0.10);"></span></div>'
def serifline(t, size=18, lh=25): return f'<div style="{SERIF} font-size: {size}px; line-height: {lh}px; color: {INK};">{t}</div>'
def fn(t, top=4): return f'<div class="fn" style="margin-top: {top}px; color: {MUTE};">{t}</div>'
def door(t, c=GOLDD, top=2): return f'<div style="display: flex; align-items: center; margin-top: {top}px; min-height: 40px;"><span style="font-size: 13px; font-weight: 500; color: {c};">{t}</span>{ARROW(c)}</div>'
def doors(*ts): return '<div style="display: flex; gap: 18px; align-items: center;">' + ''.join(door(t, c) for t, c in ts) + '</div>'

# ── instruments, at phone width (349) ──
def daylight_arc(populated=True):
    """The day in the light: one arc from sunrise to sunset, the pier as the gold end of it, the film as the dark bar after dark. Labels in one row under the baseline."""
    plan = f'<path d="M10 62 Q174.5 -30 339 62" pathLength="100" stroke="{GOLD}" stroke-width="6" fill="none" stroke-linecap="round" stroke-dasharray="0 87 13 100"/>' if populated else ''
    pier = 'THE PIER · SUNSET 7:04' if populated else 'SUNSET 7:04'
    return (f'<svg width="349" height="88" viewBox="0 0 349 88" fill="none" style="display: block; width: 100%; height: auto; margin-top: 10px;">'
            f'<path d="M10 62 Q174.5 -30 339 62 L339 62 L10 62 Z" fill="rgba(176,133,58,0.09)"/><path d="M10 62 Q174.5 -30 339 62" stroke="rgba(27,23,20,0.16)" stroke-width="1.5" fill="none"/>{plan}'
            f'<circle cx="10" cy="62" r="3" fill="rgba(27,23,20,0.35)"/><circle cx="339" cy="62" r="4" fill="{INK}"/>'
            f'<text x="4" y="82" {LB}>6:31 SUNRISE</text><text x="339" y="82" text-anchor="end" {LG}>{pier}</text></svg>')
def film_bar():
    """After dark: the film as a dark bar on the same baseline, with its own label; a second row so it never sits on the arc."""
    return (f'<svg width="349" height="30" viewBox="0 0 349 30" fill="none" style="display: block; width: 100%; height: auto; margin-top: 8px;">'
            f'<rect x="2" y="9" width="345" height="4" rx="2" fill="rgba(27,23,20,0.07)"/><rect x="250" y="5" width="60" height="12" rx="6" fill="{INK}" opacity="0.8"/>'
            f'<text x="250" y="29" {LK}>8:30 THE FILM</text><text x="4" y="29" {LB}>AFTER DARK · THE LAWN, 9 MIN ON</text></svg>')
def tide_curve():
    """The harbor as water: a low from 2:40 to 5, the kayaks on the low shore, sunset at the right end. Labels sit in the water or above the curve, never on it."""
    return (f'<svg width="349" height="78" viewBox="0 0 349 78" fill="none" style="display: block; width: 100%; height: auto; margin-top: 8px;">'
            f'<path d="M4 26 Q60 22 110 40 Q160 58 214 58 Q270 58 345 30 L345 78 L4 78 Z" fill="rgba(61,80,102,0.20)"/><path d="M4 26 Q60 22 110 40 Q160 58 214 58 Q270 58 345 30" stroke="{WATER}" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
            f'<rect x="150" y="63" width="86" height="6" rx="3" fill="{GOLD}"/><circle cx="345" cy="30" r="4" fill="{INK}"/>'
            f'<text x="4" y="14" {LB}>HIGH 8:40</text><text x="193" y="50" text-anchor="middle" {LK}>LOW 2:40–5</text><text x="244" y="70" {LG}>KAYAKS 1–4</text><text x="345" y="18" text-anchor="end" {LB}>SUNSET 7:04</text></svg>')
def burden_strip():
    """Door to door: dots on foot, the crossing as a solid bar, one number."""
    return (f'<svg width="349" height="46" viewBox="0 0 349 46" fill="none" style="display: block; width: 100%; height: auto; margin-top: 8px;">'
            f'<path d="M8 24 L44 24" stroke="rgba(27,23,20,0.30)" stroke-width="8" stroke-dasharray="0.1 14" stroke-linecap="round"/><rect x="52" y="18" width="196" height="12" rx="6" fill="{INK}" opacity="0.78"/>'
            f'<path d="M258 24 L306 24" stroke="rgba(27,23,20,0.30)" stroke-width="8" stroke-dasharray="0.1 14" stroke-linecap="round"/><text x="318" y="28" {LK}>~40</text>'
            f'<text x="52" y="10" {LG}>THE FERRY · 25 MIN · EVERY 40</text><text x="8" y="44" {LB}>TO PIER 11</text><text x="306" y="44" text-anchor="end" {LB}>9 MIN ON FOOT</text></svg>')
def day_band():
    """The evening on one track: the hour as the gold block; doors before it, the counter and the café after it, as labels."""
    return (f'<svg width="349" height="56" viewBox="0 0 349 56" fill="none" style="display: block; width: 100%; height: auto; margin-top: 8px;">'
            f'<rect x="2" y="26" width="345" height="8" rx="4" fill="rgba(27,23,20,0.07)"/><rect x="88" y="22" width="70" height="16" rx="8" fill="{GOLD}"/>'
            f'<rect x="158" y="28" width="118" height="4" rx="2" fill="rgba(27,23,20,0.16)"/><rect x="276" y="28" width="69" height="4" rx="2" fill="rgba(27,23,20,0.09)"/>'
            f'<text x="88" y="14" {LG}>THE HOUR · 7:15–8:15</text><text x="2" y="54" {LB}>6:45 DOORS</text><text x="345" y="54" text-anchor="end" {LB}>COUNTER TILL 10 · CAFÉ TILL 11</text></svg>')
def two_piers_diagram():
    """path_difference_diagram: two thresholds drawn, one per pier."""
    return (f'<svg width="349" height="118" viewBox="0 0 349 118" fill="none" style="display: block; width: 100%; height: auto; margin-top: 10px;">'
            f'<rect x="0" y="0" width="349" height="118" rx="12" fill="{WASH}"/><line x1="174.5" y1="14" x2="174.5" y2="104" stroke="rgba(27,23,20,0.12)"/>'
            f'<text x="14" y="22" {LK}>SUNSET PARK</text><text x="190" y="22" {LK}>RED HOOK</text>'
            f'<path d="M24 66 L108 66" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/><path d="M34 58 L24 66 L34 74" stroke="{GOLD}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="108" cy="66" r="4.5" fill="{INK}"/>'
            f'<text x="14" y="94" {LB}>FACES WEST · SUNSET 7:04</text><text x="14" y="108" {LB}>THE N OR R · 20 MIN</text>'
            f'<path d="M198 78 Q236 52 274 62 Q300 68 330 50" stroke="{WATER}" stroke-width="2.4" fill="none" stroke-linecap="round"/><circle cx="198" cy="78" r="4.5" fill="{INK}"/><path d="M320 46 L330 50 L326 60" stroke="{WATER}" stroke-width="2" fill="none" stroke-linecap="round"/>'
            f'<text x="190" y="94" {LB}>THE HARBOR · ANY TIME</text><text x="190" y="108" {LB}>FERRY 25 MIN · OR B61</text></svg>')

# ── kinds ──
def lead_composition(populated=True):
    if populated:
        inner_ = kick('SATURDAY AT THE PIER · KEPT WITH MAYA') + pier_day(plan=('18:30', '19:04', 'THE PIER'), after=('20:30', '22:00', 'THE FILM'))
        inner_ += f'<div style="margin-top: 10px;">{serifline("Sunset from the west pier at 7:04; it turns cold fast. The lawn is nine minutes on, and the film starts at 8:30. Low water from 2:40, kayaks till 4.")}</div>'
        inner_ += fn('MAYA, TUESDAY · &ldquo;TUESDAY, SEVEN.&rdquo;', 6)
        inner_ += f'<div style="margin-top: 8px;">{doors(("The pier, with Maya", GOLDD), ("Reply to Maya", MUTE))}</div>'
    else:
        inner_ = kick('SATURDAY AT THE PIER · FREE') + pier_day(plan=('18:30', '19:04', 'THE PIER'), after=('20:30', '22:00', 'THE FILM'))
        inner_ += f'<div style="margin-top: 10px;">{serifline("Playtime on the lawn by the pier at 8:30, free; the sunset from the west pier first, at 7:04. Low water from 2:40, kayaks till 4.")}</div>'
        inner_ += fn('TATI&rsquo;S CITY OF GLASS · GET THERE AT EIGHT FOR A SPOT · RAIN PLAN NOT POSTED', 6)
        inner_ += f'<div style="margin-top: 8px;">{doors(("Saturday&rsquo;s film", GOLDD))}</div>'
    return f'<div style="display: flex; flex-direction: column;">{inner_}</div>'
def shelf_item(name, line, chip):
    plate = f'<div style="height: 84px; border-radius: 12px; position: relative; background: {HATCH};"><span style="position: absolute; left: 10px; top: 9px; {MONO} font-size: 10px; font-weight: 700; letter-spacing: 0.9px; color: {GOLDD};">PHOTO · TO BE SOURCED</span></div>'
    return (f'<div>{plate}<div style="font-size: 15px; font-weight: 600; letter-spacing: -0.2px; line-height: 19px; margin-top: 7px; min-height: 38px;">{name}</div><div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; min-height: 34px;">{line}</div>'
            f'<span style="display: inline-block; {MONO} font-size: 10px; font-weight: 700; letter-spacing: 0.9px; color: {GOLDD}; border: 1px solid rgba(138,102,40,0.4); border-radius: 999px; padding: 2.5px 7px; margin-top: 6px;">{chip}</span></div>')
def browse_shelf():
    items = [('The noodle counter', 'Hand-pulled at the counter', 'CASH'), ('The lunch counter on Columbia Street', 'One plate a day · standing room', 'TILL 4'),
             ('The reading room at the branch library', 'Long tables, lamps, quiet', 'NO ONE ASKING'), ('The long table at the caf&eacute;', 'One communal table', 'ROOM FOR STRANGERS'),
             ('The waterfront loop', 'Five kilometres, flat', 'SHADED AFTER 2'), ('The old ferry waiting room', 'Benches, the harbor', 'USUALLY NOBODY')]
    grid = '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px 11px;">' + ''.join(shelf_item(*it) for it in items) + '</div>'
    return f'<div style="display: flex; flex-direction: column; gap: 10px;">{grid}</div>'
def redhook(col=None):
    sec = section('Red Hook, by ferry', col)
    a = sec.find('<div style="border-radius: 14px; overflow: hidden;">'); b = sec.find('</svg></div>', a) + len('</svg></div>')
    from kit3 import fix_map
    mapdiv = fix_map(sec[a:b])
    rows_start = sec.find('<div>', b); rows = sec[rows_start:]                       # the numbered places and the walk line, as parity drew them
    rows = rows.replace('display: flex; align-items: center; gap: 12px; padding: 10px 0;', 'display: flex; align-items: flex-start; gap: 12px; padding: 10px 0;').replace('font-size: 10px; font-weight: 700; flex: none;">', 'font-size: 10px; font-weight: 700; flex: none; margin-top: 1px;">').replace('<svg class="chev" width="13" height="13" viewBox="0 0 13 13" fill="none">', '<svg class="chev" width="13" height="13" viewBox="0 0 13 13" fill="none" style="margin-top: 4px;">')
    fact = sec[sec.find('<div style="display: flex; flex-direction: column; gap: 3px', b):rows_start]
    return sect('Red Hook, by ferry') + gut(mapdiv + burden_strip() + f'<div style="margin-top: 4px;">{rows}</div>')
def evening(col=None):
    sec = section('Saturday evening', col); body = sec[sec.find('<div style="padding: 0px 22px 0 22px;">'):]
    return sect('Saturday evening') + gut(day_band()) + body
FLOOD = lambda h=150: ground_section([(0, 0.6), (34, 0.6), (34, 1.2), (60, 1.2)], 0.9, [(2, 0.68, 'THE PIER · CREEK BED', 'start', INK), (36, 1.3, 'THE STREET · SILL 1911', 'start', INK), (2, 0.96, 'HARBOR · HIGH WATER', 'start', WATER)], scale_m='m', h=h, zmax=1.42)
def understanding(col=None):
    reading = FLOOD(118) + fn('READING · 4 MIN', 10) + f'<div style="margin-top: 4px;">{serifline("Why the pier floods before the street does", 17, 22)}</div>' + f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 4px;">The pier sits on the old creek bed, two feet below the 1911 sill. It drains only when the harbor is lower than the street.</div>' + door('The rest of the reading')
    piers = (f'<div style="{SERIF} font-size: 17px; line-height: 22px; font-weight: 500; color: {INK};">Two piers, two ways in</div><div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 4px;">Same evening light; a land route and a crossing.</div>'
             + access_compare([('SUNSET PARK', [(3, 'foot'), (20, 'ride'), (9, 'foot')], 'THE N OR R · A LAND ROUTE, EASY TO SHORTEN'), ('RED HOOK', [(6, 'foot'), (25, 'ride'), (9, 'foot')], 'THE FERRY, EVERY 40 · A SCHEDULED WAY IN')]))
    return sect('Worth understanding') + gut(piers) + gut(reading, top=26)

def v3(populated=True):
    col = POP if populated else COLD
    body = col.top + gut(lead_composition(populated), top=26)
    if populated: body += section('From friends')
    body += sect('Any day') + gut(browse_shelf())
    body += redhook(col) + evening(col) + understanding(col)
    if populated: body += section('Seen up close')
    body += section('Sunday', col) + section('Saturday morning, downtown', col) + col.doors
    return col.open + body + '<div style="flex-grow: 1;"></div>' + tabbar + '</div>'
def caption(k1, k2, t):
    c = CAP_TPL
    c = c.replace('PARITY WITH HOME &middot; POPULATED &middot; FRIDAY, NEW YORK', k1).replace('HOME&rsquo;S KIT ON PLACES&rsquo; CONTENT', k2)
    a = c.find('line-height: 22px; color: #1B1714;">') + len('line-height: 22px; color: #1B1714;">'); b = c.find('</div>', a)
    return c[:a] + t + c[b:]
def board(h=5400):
    c1 = caption('THE CANON&rsquo;S INSTRUMENTS &middot; POPULATED &middot; FRIDAY, NEW YORK', 'HOME&rsquo;S KIT, THE CANON&rsquo;S KINDS', 'Each section carries one instrument that earns its ink: the daylight arc and the tide curve on the opening, hatched photo slots on the everyday six, the burden strip on the crossing, the day band on the evening, the two-threshold diagram, the editorial cover') + v3(True) + '</div>'
    c2 = caption('THE CANON&rsquo;S INSTRUMENTS &middot; COLD START', 'THE SAME WORLD, NO HISTORY, NO FRIENDS', 'The film leads the light; no From friends, no contributions; the everyday six, the pocket, the evening, the comparison, the reading and Sunday as before') + v3(False) + '</div>'
    head = HEADBLOCK.replace('19 &middot; THE SYNTHESIS, POLISHED &middot; 09-07 (&sect;12)', '19 &middot; THE SYNTHESIS, WITH THE CANON&rsquo;S INSTRUMENTS &middot; 09-07').replace('19 &middot; The synthesis, in Home&rsquo;s kit', '19 &middot; The synthesis, with the canon&rsquo;s instruments')
    a = head.find('max-width: 980px;">') + len('max-width: 980px;">'); b = head.find('</div>', a)
    head = head[:a] + 'The selected direction, chosen by the founder on September 7: Home&rsquo;s kit for the chrome, the rows and the people; the kinds and instruments of the a26e3228 canon wherever a section has data to show; a photo slot is a hatched plate, never a drawing. Populated and cold. The notes name each section&rsquo;s instrument, what was reversed from &sect;12, and what the previous drafts were.' + head[b:]
    n = notes.replace('>The parity pass</div>', '>The instrument pass</div>' + instrument_notes(), 1)
    n = n.replace('<div class="kickm">WHAT HOME DECIDED THAT PLACES NOW ADOPTS</div>', '<div class="kickm">WHAT HOME DECIDED THAT PLACES ADOPTS (THE PARITY DRAFT, 09-07 EVENING)</div>', 1)
    open_ = BOARD_OPEN.replace(re.search(r'min-height: \d+px', BOARD_OPEN).group(0), f'min-height: {h}px')
    return HEAD + open_ + head + '<div style="display: flex; gap: 46px; align-items: flex-start;">' + c1 + c2 + n + '</div>' + foot + tail
def instrument_notes():
    th = 'style="text-align: left; font-family: JetBrains Mono, monospace; font-size: 10px; font-weight: 700; letter-spacing: 1.1px; color: #6E6862; padding: 6px 10px 8px 0; border-bottom: 1px solid rgba(27,23,20,0.14); vertical-align: bottom;"'
    td = 'style="font-size: 12.5px; line-height: 17px; color: #2C2622; padding: 8px 10px 8px 0; border-bottom: 1px solid rgba(27,23,20,0.06); vertical-align: top;"'
    rows = [['The opening', 'field_lead_composition · the daylight arc · the tide curve', 'The pier placed at the end of the light, the film as the dark bar after it; the harbor as water, low 2:40 to 5, the kayaks on its shore; one serif line, one door'],
            ['Any day', 'field_browse_shelf', 'Six places as hatched photo slots with a name, one line and one mono chip; photo or hatch, never a drawing'],
            ['Red Hook, by ferry', 'Our map · the burden strip', 'Door to door: dots on foot, the crossing as one solid bar, one number'],
            ['Saturday evening', 'The day band', 'The hour as the gold block on the evening&rsquo;s track; doors, the counter and the caf&eacute; as its labels'],
            ['Worth understanding', 'path_difference_diagram · field_editorial_cover', 'Two thresholds drawn side by side instead of a text table; the reading as a cover with its own diagram under the gradient'],
            ['From friends, Seen up close, Sunday, Saturday morning', 'Home&rsquo;s kit, unchanged', 'Author rows, serif quotes, the place strip, facepile rows, arrow doors']]
    tbl = f'<table style="border-collapse: collapse; width: 100%;"><thead><tr><th {th}>SECTION</th><th {th}>KIND OR INSTRUMENT</th><th {th}>WHAT IT SHOWS</th></tr></thead><tbody>' + ''.join('<tr>' + ''.join(f'<td {td}>{c}</td>' for c in r) + '</tr>' for r in rows) + '</tbody></table>'
    return (f'<div style="display: flex; flex-direction: column; gap: 8px;"><div class="kickm">THE INSTRUMENT PASS · WHERE EACH SECTION&rsquo;S PICTURE COMES FROM</div>{tbl}</div>'
            f'<div style="display: flex; flex-direction: column; gap: 8px;"><div class="kickm">WHY NOT ROWS OF TEXT</div><div style="font-size: 14px; line-height: 21px; color: #2C2622;">Home is not sleek because it is plain; every picture on it carries data. The previous draft removed Places&rsquo; drawings and put nothing in their place. This one gives each section that has something to show one kind or instrument from the canon&rsquo;s 34 Places kinds and 23 instruments, at the 10px mono floor, gold for the plan, ink for now, hatch for a photograph not yet sourced. Sections without data to draw keep Home&rsquo;s rows.</div></div>'
            f'<div style="display: flex; flex-direction: column; gap: 8px;"><div class="kickm">THE TWO DRAFTS BEFORE THIS</div><div style="font-size: 14px; line-height: 21px; color: #2C2622;">The &sect;12 polish (illustrated places in their own colour, sans compact titles, a boxed field, an outlined gold pill) and the Home-kit-only draft (the same content as rows of text) were both drawn on this board earlier on September 7 and are recorded in the response doc, &sect;16 and &sect;20. Neither is carried forward.</div></div>'
            f'<div style="display: flex; flex-direction: column; gap: 8px;"><div class="kickm">REBUILT FROM THE PUSHED BOARDS</div><div style="font-size: 14px; line-height: 21px; color: #2C2622;">The generators for these boards were lost with the session&rsquo;s temporary folder. This board is rebuilt from the pushed HTML: chrome, captions and the two comparison scrolls verbatim; the new scroll from the previous draft&rsquo;s sections plus instruments redrawn from the canon&rsquo;s specimen sheets. The instrument values are fixture facts already on 19; the arc&rsquo;s sunrise and the tide&rsquo;s high are placeholders at the fixture&rsquo;s scale, not verified data.</div></div>')

if __name__ == '__main__':
    os.makedirs('out', exist_ok=True)
    html = board(); open('out/19 - The Synthesis Polished.dc.html', 'w').write(html); print('wrote', len(html))
