"""19 v3 · the synthesis with the canon's instruments (founder, 09-07 late). Rebuilt from the pushed HTML after the generator scratchpad was lost:
the head, tail, tab bar and the parity/§12 columns are lifted verbatim from the pushed 19; the new scroll reuses the parity column's sections
where they already fit and replaces the opening, the everyday six, the pocket's access, the evening's time, the comparison and the reading
with kinds and instruments from the a26e3228 canon (field_lead_composition, the daylight arc, the tide curve, field_browse_shelf, the burden strip,
the day band, path_difference_diagram, field_editorial_cover). Hatched plates are photo slots, never drawings."""
import os, re, sys, subprocess
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
LB = f'font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="{ANCHOR}"'
LG = f'font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="{GOLDD}"'
LK = f'font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="{INK}"'

# ── the parity column, sliced ──
ph = parity.find('<div style="width: 393px; min-height'); CAP_TPL = parity[:ph]
PHONE_OPEN = parity[ph:parity.find('>', ph)+1]; inner = parity[parity.find('>', ph)+1:]
def sect_pos(label):
    m = inner.find(f'letter-spacing: 0.1px; color: #1B1714;">{label}</span>'); assert m > 0, label
    return inner.rfind('<div style="padding: 40px 22px 0 22px;">', 0, m)
SECTS = ['From friends', 'Any day', 'Red Hook, by ferry', 'Saturday evening', 'Worth understanding', 'Seen up close', 'Sunday', 'Saturday morning, downtown']
POS = {k: sect_pos(k) for k in SECTS}
doors_at = inner.find('<div style="padding: 30px 22px 0 22px;">', POS['Saturday morning, downtown']); tab_at = inner.find('<div style="flex-grow: 1;"></div>')
def section(label):
    i = SECTS.index(label); a = POS[label]; b = POS[SECTS[i+1]] if i+1 < len(SECTS) else doors_at
    return inner[a:b]
TOP = inner[:inner.find('<div style="padding: 20px 22px 0 22px;">')]          # anchor, orientation, the quiet question line
DOORS = inner[doors_at:tab_at]
def sect(t): return f'<div style="padding: 40px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 12px; padding-bottom: 10px;"><span style="font-size: 13px; font-weight: 600; letter-spacing: 0.1px; color: {INK};">{t}</span><span style="flex: 1; height: 1px; background: rgba(27,23,20,0.12);"></span></div></div>'
def gut(h, top=0): return f'<div style="padding: {top}px 22px 0 22px;">{h}</div>'
def kick(t): return f'<div style="display: flex; align-items: center; gap: 10px; {MONO} font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: {GOLDD};"><span>{t}</span><span style="flex:1;height:1px;background:rgba(27,23,20,0.10);"></span></div>'
def serifline(t, size=18, lh=25): return f'<div style="{SERIF} font-size: {size}px; line-height: {lh}px; color: {INK};">{t}</div>'
def fn(t, top=4): return f'<div class="fn" style="margin-top: {top}px; color: {ANCHOR};">{t}</div>'
def door(t, c=GOLDD, top=2): return f'<div style="display: flex; align-items: center; margin-top: {top}px; min-height: 40px;"><span style="font-size: 14px; font-weight: 600; color: {c};">{t}</span>{ARROW(c)}</div>'
def doors(*ts): return '<div style="display: flex; gap: 18px; align-items: center;">' + ''.join(door(t, c) for t, c in ts) + '</div>'

# ── instruments, at phone width (349) ──
def daylight_arc():
    """The day placed in the light: sunrise to sunset; the gold segment is the pier at the end of the light; the dark bar after it is the film."""
    return (f'<svg width="349" height="74" viewBox="0 0 349 74" fill="none" style="display: block; width: 100%; height: auto; margin-top: 8px;">'
            f'<path d="M8 58 Q150 -26 292 58 L292 58 L8 58 Z" fill="rgba(176,133,58,0.09)"/><path d="M8 58 Q150 -26 292 58" stroke="rgba(27,23,20,0.14)" stroke-width="1.5" fill="none"/>'
            f'<path d="M8 58 Q150 -26 292 58" pathLength="100" stroke="{GOLD}" stroke-width="7" fill="none" stroke-linecap="round" stroke-dasharray="0 88 12 100"/>'
            f'<rect x="304" y="54" width="40" height="8" rx="4" fill="{INK}" opacity="0.78"/>'
            f'<text x="2" y="72" {LB}>6:31</text><text x="212" y="72" {LG}>THE PIER · 7:04</text><text x="303" y="49" {LK}>8:30</text></svg>')
def tide_curve():
    """The harbor as a body of water: low water 2:40 to 5; the kayaks on its shore; sunset at the right end."""
    return (f'<svg width="349" height="66" viewBox="0 0 349 66" fill="none" style="display: block; width: 100%; height: auto; margin-top: 6px;">'
            f'<path d="M4 14 Q60 10 110 30 Q160 52 214 52 Q270 52 345 22 L345 66 L4 66 Z" fill="rgba(61,80,102,0.20)"/><path d="M4 14 Q60 10 110 30 Q160 52 214 52 Q270 52 345 22" stroke="{WATER}" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
            f'<rect x="120" y="58" width="90" height="6" rx="3" fill="{GOLD}"/><circle cx="345" cy="22" r="4" fill="{INK}"/>'
            f'<text x="134" y="42" {LK}>LOW 2:40–5</text><text x="120" y="56" {LG}></text><text x="2" y="10" {LB}>HIGH 8:40</text><text x="345" y="12" text-anchor="end" {LB}>SUNSET 7:04</text><text x="224" y="64" {LB}>KAYAKS 1–4</text></svg>')
def burden_strip():
    """Door to door: dots on foot, the crossing as a solid bar, one number."""
    return (f'<svg width="349" height="46" viewBox="0 0 349 46" fill="none" style="display: block; width: 100%; height: auto; margin-top: 8px;">'
            f'<path d="M8 24 L44 24" stroke="rgba(27,23,20,0.30)" stroke-width="8" stroke-dasharray="0.1 14" stroke-linecap="round"/><rect x="52" y="18" width="196" height="12" rx="6" fill="{INK}" opacity="0.78"/>'
            f'<path d="M258 24 L306 24" stroke="rgba(27,23,20,0.30)" stroke-width="8" stroke-dasharray="0.1 14" stroke-linecap="round"/><text x="318" y="28" {LK}>~40</text>'
            f'<text x="52" y="10" {LG}>THE FERRY · 25 MIN · EVERY 40</text><text x="8" y="44" {LB}>TO PIER 11</text><text x="236" y="44" {LB}>9 MIN ON FOOT</text></svg>')
def day_band():
    """The evening on one track: gold is the hour; the counter and the café as the plain track after it."""
    return (f'<svg width="349" height="54" viewBox="0 0 349 54" fill="none" style="display: block; width: 100%; height: auto; margin-top: 8px;">'
            f'<rect x="2" y="26" width="345" height="8" rx="4" fill="rgba(27,23,20,0.07)"/><rect x="88" y="22" width="70" height="16" rx="8" fill="{GOLD}"/>'
            f'<rect x="158" y="28" width="118" height="4" rx="2" fill="rgba(27,23,20,0.18)"/><rect x="158" y="28" width="187" height="4" rx="2" fill="rgba(27,23,20,0.10)"/>'
            f'<text x="88" y="14" {LG}>THE HOUR · 7:15–8:15</text><text x="2" y="52" {LB}>6:45 DOORS</text><text x="186" y="52" {LB}>COUNTER TILL 10</text><text x="292" y="52" {LB}>CAFÉ 11</text></svg>')
def two_piers_diagram():
    """path_difference_diagram: two thresholds drawn, one per pier."""
    return (f'<svg width="349" height="118" viewBox="0 0 349 118" fill="none" style="display: block; width: 100%; height: auto; margin-top: 10px;">'
            f'<rect x="0" y="0" width="349" height="118" rx="12" fill="{WASH}"/><line x1="174.5" y1="14" x2="174.5" y2="104" stroke="rgba(27,23,20,0.12)"/>'
            f'<text x="14" y="22" {LK}>SUNSET PARK</text><text x="190" y="22" {LK}>RED HOOK</text>'
            f'<path d="M24 66 L108 66" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/><path d="M34 58 L24 66 L34 74" stroke="{GOLD}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="108" cy="66" r="4.5" fill="{INK}"/>'
            f'<text x="14" y="94" {LB}>FACES WEST · SUNSET 7:04</text><text x="14" y="108" {LB}>THE N OR R · 20 MIN</text>'
            f'<path d="M198 78 Q236 52 274 62 Q300 68 330 50" stroke="{WATER}" stroke-width="2.4" fill="none" stroke-linecap="round"/><circle cx="198" cy="78" r="4.5" fill="{INK}"/><path d="M320 46 L330 50 L326 60" stroke="{WATER}" stroke-width="2" fill="none" stroke-linecap="round"/>'
            f'<text x="190" y="94" {LB}>THE HARBOR · ANY TIME</text><text x="190" y="108" {LB}>THE FERRY 25 MIN · OR B61</text></svg>')

# ── kinds ──
def lead_composition():
    inner_ = kick('SATURDAY, IN THE LIGHT · KEPT WITH MAYA') + daylight_arc()
    inner_ += f'<div style="margin-top: 8px;">{serifline("Sunset from the west pier at 7:04; the lawn is nine minutes on, and the film starts at 8:30.")}</div>'
    inner_ += fn('MAYA, TUESDAY · &ldquo;TUESDAY, SEVEN.&rdquo; · IT TURNS COLD FAST', 6)
    inner_ += f'<div style="margin-top: 14px;">{serifline("The pier, earlier", 16, 21)}</div>' + tide_curve()
    inner_ += f'<div style="margin-top: 6px;">{doors(("The pier, with Maya", GOLDD), ("Reply to Maya", MUTE))}</div>'
    return f'<div style="display: flex; flex-direction: column;">{inner_}</div>'
def shelf_item(name, line, chip):
    plate = f'<div style="height: 96px; border-radius: 12px; position: relative; background: {HATCH};"><span style="position: absolute; left: 10px; top: 9px; {MONO} font-size: 10px; font-weight: 700; letter-spacing: 0.9px; color: {GOLDD};">PHOTO · TO BE SOURCED</span></div>'
    return (f'<div>{plate}<div style="font-size: 15px; font-weight: 600; letter-spacing: -0.2px; line-height: 19px; margin-top: 7px;">{name}</div><div style="font-size: 12.5px; line-height: 17px; color: {MUTE};">{line}</div>'
            f'<span style="display: inline-block; {MONO} font-size: 10px; font-weight: 700; letter-spacing: 0.9px; color: {GOLDD}; border: 1px solid rgba(138,102,40,0.4); border-radius: 999px; padding: 2.5px 7px; margin-top: 6px;">{chip}</span></div>')
def browse_shelf():
    items = [('The noodle counter', 'Hand-pulled at the counter', 'CASH'), ('The lunch counter on Columbia Street', 'One plate a day · standing room', 'TILL 4'),
             ('The reading room at the branch library', 'Long tables, lamps, quiet', 'NO ONE ASKING'), ('The long table at the caf&eacute;', 'One communal table', 'ROOM FOR STRANGERS'),
             ('The waterfront loop', 'Five kilometres, flat', 'SHADED AFTER 2'), ('The old ferry waiting room', 'Benches, the harbor', 'USUALLY NOBODY')]
    grid = '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px 11px;">' + ''.join(shelf_item(*it) for it in items) + '</div>'
    return f'<div style="display: flex; flex-direction: column; gap: 10px;">{kick("ANY DAY · SIX PLACES")}{grid}</div>'
def redhook():
    sec = section('Red Hook, by ferry')
    a = sec.find('<div style="border-radius: 14px; overflow: hidden;">'); b = sec.find('</svg></div>', a) + len('</svg></div>')
    mapdiv = sec[a:b]
    rows_start = sec.find('<div>', b); rows = sec[rows_start:]                       # the numbered places and the walk line, as parity drew them
    fact = sec[sec.find('<div style="display: flex; flex-direction: column; gap: 3px', b):rows_start]
    return sect('Red Hook, by ferry') + gut(mapdiv + burden_strip() + f'<div style="margin-top: 4px;">{rows}</div>')
def evening():
    sec = section('Saturday evening'); body = sec[sec.find('<div style="padding: 0px 22px 0 22px;">'):]
    return sect('Saturday evening') + gut(day_band()) + body
def understanding():
    sec = section('Worth understanding')
    svg_a = sec.find('<svg', sec.find('CREEK BED') - 3000); svg_b = sec.find('</svg>', sec.find('CREEK BED')) + 6; floods = sec[svg_a:svg_b]
    floods = re.sub(r'^<svg', '<svg style="position: absolute; left: 0; top: -44px; width: 100%; height: auto;"', floods, count=1)
    cover = (f'<div style="height: 186px; border-radius: 12px; overflow: hidden; position: relative; background: {WASH};">{floods}'
             f'<div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(27,23,20,0) 42%, rgba(27,23,20,0.70) 100%);"></div>'
             f'<div style="position: absolute; left: 15px; right: 15px; bottom: 13px;"><div style="{MONO} font-weight: 700; font-size: 10px; letter-spacing: 1.2px; color: #F2E6CC;">READING · 4 MIN</div>'
             f'<div style="{SERIF} font-weight: 600; font-size: 20px; line-height: 24px; color: {CARD}; margin-top: 4px;">Why the pier floods before the street does</div></div></div>')
    piers = (f'<div style="{SERIF} font-size: 17px; line-height: 22px; font-weight: 500; color: {INK};">Two piers, two directions</div><div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 4px;">Same evening light, opposite views.</div>' + two_piers_diagram())
    return sect('Worth understanding') + gut(piers) + gut(cover + f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 8px;">The pier sits on the old creek bed, two feet below the 1911 sill. It drains only when the harbor is lower than the street.</div>' + door('The rest of the reading'), top=26)

def v3():
    body = TOP + gut(lead_composition(), top=20)
    body += section('From friends')
    body += sect('Any day') + gut(browse_shelf())
    body += redhook() + evening() + understanding()
    body += section('Seen up close') + section('Sunday') + section('Saturday morning, downtown') + DOORS
    return PHONE_OPEN + body + '<div style="flex-grow: 1;"></div>' + tabbar + '</div>'

def caption(k1, k2, t):
    c = CAP_TPL
    c = c.replace('PARITY WITH HOME &middot; POPULATED &middot; FRIDAY, NEW YORK', k1).replace('HOME&rsquo;S KIT ON PLACES&rsquo; CONTENT', k2)
    a = c.find('line-height: 22px; color: #1B1714;">') + len('line-height: 22px; color: #1B1714;">'); b = c.find('</div>', a)
    return c[:a] + t + c[b:]
def board(h=5400):
    col3 = caption('THE CANON&rsquo;S INSTRUMENTS &middot; POPULATED &middot; FRIDAY, NEW YORK', 'HOME&rsquo;S KIT, THE CANON&rsquo;S KINDS', 'The same sections; each carries one instrument that earns its ink: the daylight arc and the tide curve on the opening, hatched photo slots on the everyday six, the burden strip on the crossing, the day band on the evening, the two-threshold diagram, the editorial cover') + v3() + '</div>'
    parity_col = parity.replace('PARITY WITH HOME &middot; POPULATED &middot; FRIDAY, NEW YORK', 'HOME&rsquo;S KIT ONLY &middot; THE PREVIOUS DRAFT')
    s12_col = s12
    head = HEADBLOCK.replace('19 &middot; THE SYNTHESIS, POLISHED &middot; 09-07 (&sect;12)', '19 &middot; THE SYNTHESIS, WITH THE CANON&rsquo;S INSTRUMENTS &middot; 09-07').replace('19 &middot; The synthesis, in Home&rsquo;s kit', '19 &middot; The synthesis, with the canon&rsquo;s instruments')
    a = head.find('max-width: 980px;">') + len('max-width: 980px;">'); b = head.find('</div>', a)
    head = head[:a] + 'Three scrolls of the same content. Left: Home&rsquo;s kit with the kinds and instruments of the a26e3228 canon where a section has data to show; a photo slot is a hatched plate, never a drawing. Middle: the previous draft, Home&rsquo;s kit alone. Right: the &sect;12 vocabulary, for comparison. The notes say which kind or instrument each section uses and what was reversed.' + head[b:]
    n = notes.replace('>The parity pass</div>', '>Two passes: Home&rsquo;s kit, then the canon&rsquo;s instruments</div>' + instrument_notes(), 1)
    open_ = BOARD_OPEN.replace('width: 1900px', 'width: 2140px').replace(re.search(r'min-height: \d+px', BOARD_OPEN).group(0), f'min-height: {h}px')
    return HEAD + open_ + head + '<div style="display: flex; gap: 46px; align-items: flex-start;">' + col3 + parity_col + s12_col + n + '</div>' + foot + tail
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
            f'<div style="display: flex; flex-direction: column; gap: 8px;"><div class="kickm">REBUILT FROM THE PUSHED BOARDS</div><div style="font-size: 14px; line-height: 21px; color: #2C2622;">The generators for these boards were lost with the session&rsquo;s temporary folder. This board is rebuilt from the pushed HTML: chrome, captions and the two comparison scrolls verbatim; the new scroll from the previous draft&rsquo;s sections plus instruments redrawn from the canon&rsquo;s specimen sheets. The instrument values are fixture facts already on 19; the arc&rsquo;s sunrise and the tide&rsquo;s high are placeholders at the fixture&rsquo;s scale, not verified data.</div></div>')

if __name__ == '__main__':
    os.makedirs('out', exist_ok=True)
    html = board(); open('out/19 - The Synthesis Polished.dc.html', 'w').write(html); print('wrote', len(html))
