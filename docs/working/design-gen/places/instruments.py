"""Instruments drawn from data, not by hand. One time axis for a day; a true sun elevation curve; a harmonic tide; a shared minutes scale for access;
a section to scale for ground. Every label is placed from the geometry. Inputs are fixture times; a live version takes the date and the place."""
import math
INK='#1B1714'; MUTE='#6E6862'; GOLD='#B0853A'; GOLDD='#8A6628'; WATER='#3D5066'; PAPER='#EFEAE0'; WASH='#E8E2D4'; OX='#7A2E2E'
MONO='font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8"'
def L(x, y, t, fill=MUTE, w=None, anchor='start'): return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" {MONO}{" font-weight=\"700\"" if w else ""} fill="{fill}">{t}</text>'
def hm(t):
    """'7:04' → hours as float; '19:04' too; 'pm' aware when > 12 given as 24h."""
    h, m = t.split(':'); return int(h) + int(m) / 60
def fmt(h):
    hh = int(h) % 24; mm = int(round((h - int(h)) * 60)); return f'{hh if hh <= 12 else hh - 12}:{mm:02d}' if hh else f'12:{mm:02d}'
class Axis:
    def __init__(self, t0, t1, x0=10, x1=339): self.t0, self.t1, self.x0, self.x1 = t0, t1, x0, x1
    def x(self, t): return self.x0 + (t - self.t0) / (self.t1 - self.t0) * (self.x1 - self.x0)
    def ticks(self, y, every=3, fill=MUTE):
        out = ''
        t = math.ceil(self.t0 / every) * every
        while t <= self.t1:
            x = self.x(t); lab = f'{int(t) % 24 or 12}' if t % 24 != 12 else '12'
            lab = {0: 'MIDNIGHT', 12: 'NOON'}.get(int(t) % 24, f'{int(t) % 12 or 12}{"AM" if t % 24 < 12 else "PM"}')
            out += f'<line x1="{x:.1f}" y1="{y-3}" x2="{x:.1f}" y2="{y+3}" stroke="rgba(27,23,20,0.25)" stroke-width="1"/>' + L(x, y + 14, lab, anchor='middle')
            t += every
        return out
def day_band(t0, t1, blocks, marks=(), labels=(), h=56):
    """The evening on one track from times. blocks: (start,end,label,'gold'|'ink'); marks: (time,label,'ring'|'dot'). Labels above are placed from the geometry: gold block label at its start, marks to the right of the mark, pushed to the end anchor when they would run off."""
    ax = Axis(t0, t1, 2, 347); svg = f'<svg width="349" height="{h}" viewBox="0 0 349 {h}" fill="none" style="display: block; width: 100%; height: auto; margin-top: 8px;">'
    svg += f'<rect x="2" y="26" width="345" height="8" rx="4" fill="rgba(27,23,20,0.07)"/>'
    used = []
    for s, e, lab, kind in blocks:
        x0, x1 = ax.x(hm(s)), ax.x(hm(e)); col = GOLD if kind == 'gold' else INK
        svg += f'<rect x="{x0:.1f}" y="22" width="{x1-x0:.1f}" height="16" rx="8" fill="{col}"' + (' opacity="0.8"' if kind == 'ink' else '') + '/>'
        if lab: svg += L(x0, 14, lab, GOLDD if kind == 'gold' else INK, True); used.append((x0, x0 + len(lab) * 6.4))
    for t, lab, kind in marks:
        x = ax.x(hm(t))
        svg += (f'<circle cx="{x:.1f}" cy="30" r="6" stroke="{INK}" stroke-width="1.6" fill="{PAPER}"/>' if kind == 'ring' else f'<circle cx="{x:.1f}" cy="30" r="4" fill="{INK}"/>')
        if lab:
            w = len(lab) * 6.4; lx = x + 10; anchor = 'start'
            if lx + w > 347: lx, anchor = x - 10, 'end'
            if any(a < lx + (w if anchor == 'start' else 0) and lx - (w if anchor == 'end' else 0) < b for a, b in used): lx, anchor = 347, 'end'
            svg += L(lx, 14, lab, INK, True, anchor); used.append((lx - (w if anchor == 'end' else 0), lx + (w if anchor == 'start' else 0)))
    for t, lab, anchor in labels: svg += L(ax.x(hm(t)) if ':' in t else (2 if t == 'start' else 347), h - 2, lab, MUTE, None, anchor)
    return svg + '</svg>'
def access_compare(rows, origin='FROM CANAL STREET', h=None):
    """Ways in on one minutes scale, from a named origin. Legs: 'foot' dots, 'ride' a solid bar, 'wait' a hollow bar, 'stairs' a stepped mark.
    Waiting is drawn apart from movement, so the decisive premise of each way is visible: a scheduled crossing costs a wait; a train does not.
    Each row reads moving+wait for the wait actually drawn. It is not a min-max range: the possible total depends on the headway, which the row note names."""
    total = max(sum(m for m, k in r[1]) for r in rows); ax = Axis(0, total, 100, 300); h = h or 26 + 44 * len(rows)
    svg = f'<svg width="349" height="{h}" viewBox="0 0 349 {h}" fill="none" style="display: block; width: 100%; height: auto; margin-top: 8px;">' + L(2, 10, origin, MUTE)
    for i, (name, legs, note) in enumerate(rows):
        y = 28 + i * 44; svg += L(2, y + 4, name, INK, True); t = 0; moving = 0
        for m, kind in legs:
            x0, x1 = ax.x(t), ax.x(t + m)
            if kind == 'foot': svg += f'<path d="M{x0+4:.1f} {y} L{max(x0+4, x1-2):.1f} {y}" stroke="rgba(27,23,20,0.30)" stroke-width="8" stroke-dasharray="0.1 12" stroke-linecap="round"/>'; moving += m
            elif kind == 'wait': svg += f'<rect x="{x0:.1f}" y="{y-5}" width="{x1-x0:.1f}" height="10" rx="5" fill="none" stroke="rgba(27,23,20,0.35)" stroke-width="1.5" stroke-dasharray="3 3"/>'
            elif kind == 'stairs': svg += f'<path d="M{x0:.1f} {y+4} h4 v-4 h4 v-4 h4" stroke="{INK}" stroke-width="1.6" fill="none"/>'; moving += m
            else: svg += f'<rect x="{x0:.1f}" y="{y-6}" width="{x1-x0:.1f}" height="12" rx="6" fill="{INK}" opacity="0.78"/>'; moving += m
            t += m
        wait = t - moving
        lab = f'{t} MOVING' if not wait else f'{moving}+{wait}'
        lx = ax.x(t) + 8
        svg += (L(347, y - 9, lab, INK, True, 'end') if lx + len(lab) * 6.4 > 347 else L(lx, y + 4, lab, INK, True)) + L(2, y + 18, note, MUTE)
    svg += L(100, h - 2, '0', MUTE) + L(300, h - 2, 'MOVING + THE WAIT AS DRAWN · NOT A RANGE', MUTE, None, 'end')
    return svg + '</svg>'
def section(points, sea, labels, scale_m=None, h=110, w=349, zmax=None):
    """Ground to scale: points (x_m, z_m) along a line; the sea level; labels (x_m, z_m, text, anchor, fill). Water shows only where the ground is below it. A bar at the right says how tall the picture is."""
    xs = [p[0] for p in points]; zs = [p[1] for p in points] + [sea]; x0, x1 = min(xs), max(xs); z0, z1 = min(zs), (zmax if zmax is not None else max(zs))
    pad = 12; sx = (w - 2 * pad - 52) / (x1 - x0 or 1); sz = (h - 2 * pad - 10) / (z1 - z0 or 1)
    X = lambda x: pad + (x - x0) * sx; Z = lambda z: h - pad - (z - z0) * sz
    prof = ' L'.join(f'{X(x):.1f} {Z(z):.1f}' for x, z in points)
    svg = f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" fill="none" style="display: block; width: 100%; height: auto; margin-top: 8px;"><rect x="0" y="0" width="{w}" height="{h}" rx="12" fill="{WASH}"/>'
    svg += f'<rect x="{X(x0):.1f}" y="{Z(sea):.1f}" width="{X(x1)-X(x0):.1f}" height="{h-pad-Z(sea):.1f}" fill="rgba(61,80,102,0.22)"/><line x1="{X(x0):.1f}" y1="{Z(sea):.1f}" x2="{X(x1):.1f}" y2="{Z(sea):.1f}" stroke="{WATER}" stroke-width="1.5"/>'
    svg += f'<path d="M{prof} L{X(x1):.1f} {h-pad:.0f} L{X(x0):.1f} {h-pad:.0f} Z" fill="#E2DAC4"/><path d="M{prof}" stroke="{INK}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'
    for x, z, t, anchor, fill in labels: svg += L(X(x), Z(z), t, fill, fill != MUTE, anchor)
    zr = max(zs) - z0; svg += f'<line x1="{w-pad-4}" y1="{Z(z0):.1f}" x2="{w-pad-4}" y2="{Z(max(zs)):.1f}" stroke="{MUTE}" stroke-width="1"/>' + L(w - pad - 8, (Z(z0) + Z(max(zs))) / 2 + 3, f'{zr:g} {"FT" if scale_m == "ft" else "M"}', MUTE, None, 'end')
    return svg + '</svg>'

# ── the pier's day, redesigned: candidates ──
def pier_line(rise='6:31', set_='18:25', plan=('17:50', '18:25'), after=('20:30', '22:00'), low=('14:40', '17:00'), t0=6, t1=23, h=62):
    """One track, the day. Two overlapping bars: the light (gold wash, sunrise to sunset) and the water (a water bar for the low-water window), offset so both read where they overlap.
    The pier is the gold pill at the light's end; the film is the ink pill after dark, labelled. Three labels, mono."""
    ax = Axis(t0, t1, 2, 347); r, s_, p0, p1, a0, a1, l0, l1 = map(hm, (rise, set_, plan[0], plan[1], after[0], after[1], low[0], low[1])); y = 26
    svg = f'<svg width="349" height="{h}" viewBox="0 0 349 {h}" fill="none" style="display: block; width: 100%; height: auto; margin-top: 8px;">'
    svg += f'<rect x="2" y="{y-4}" width="345" height="8" rx="4" fill="rgba(27,23,20,0.07)"/>'
    svg += f'<rect x="{ax.x(r):.1f}" y="{y-6}" width="{ax.x(s_)-ax.x(r):.1f}" height="8" rx="4" fill="rgba(176,133,58,0.30)"/>'
    svg += f'<rect x="{ax.x(l0):.1f}" y="{y-1}" width="{ax.x(l1)-ax.x(l0):.1f}" height="8" rx="4" fill="rgba(61,80,102,0.45)"/>'
    svg += f'<rect x="{ax.x(p0):.1f}" y="{y-9}" width="{ax.x(p1)-ax.x(p0):.1f}" height="16" rx="8" fill="{GOLD}"/><rect x="{ax.x(a0):.1f}" y="{y-7}" width="{ax.x(a1)-ax.x(a0):.1f}" height="12" rx="6" fill="{INK}" opacity="0.8"/>'
    svg += L(ax.x(p0) - 8, y - 12, f'THE PIER · SUNSET {fmt(s_)}', GOLDD, True, 'end') + L(ax.x(l1), y + 24, f'LOW WATER {fmt(l0)}–{fmt(l1).split(":")[0]}', WATER, True, 'end') + L(347, y + 24, f'FILM {fmt(a0)}', INK, True, 'end')
    return svg + '</svg>'

def gates_and_sill(h=150, w=349):
    """Two grounds against one harbor at the same height: the street raised above the 1911 sill, which drains by itself, and the park built on the fill behind gates, which has to be pumped.
    The relationship is the whole subject, so there are two grounds, one water line, one gate and three pumps."""
    base, water = h - 30, h - 60
    svg = f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" fill="none" style="display: block; width: 100%; height: auto; margin-top: 8px;">'
    svg += f'<rect x="0" y="{water}" width="{w}" height="{base - water}" fill="{WATER}" opacity="0.16"/><line x1="0" y1="{water}" x2="{w}" y2="{water}" stroke="{WATER}" stroke-width="1.4"/>'
    svg += f'<path d="M60 {base} L60 {base - 58} L190 {base - 58} L190 {base} Z" fill="{WASH}" stroke="rgba(27,23,20,0.30)" stroke-width="1"/>'
    svg += f'<path d="M240 {base} L240 {base - 16} L340 {base - 16} L340 {base} Z" fill="{WASH}" stroke="rgba(27,23,20,0.30)" stroke-width="1"/>'
    svg += f'<path d="M240 {base} L240 {water - 14}" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>'
    for px in (272, 296, 320):
        svg += f'<path d="M{px} {base - 8} L{px} {water - 12}" stroke="{GOLDD}" stroke-width="1.6"/><path d="M{px - 4} {water - 6} L{px} {water - 13} L{px + 4} {water - 6}" stroke="{GOLDD}" stroke-width="1.6" fill="none"/>'
    svg += f'<line x1="215" y1="16" x2="215" y2="{base}" stroke="rgba(27,23,20,0.12)" stroke-width="1" stroke-dasharray="3 4"/>'
    svg += L(4, water - 6, 'THE HARBOR, HIGH', WATER, True)
    svg += L(125, base - 64, 'THE STREET', INK, True, 'middle') + L(125, base + 16, 'RAISED TO THE SILL, 1911', MUTE, None, 'middle')
    svg += L(236, water - 18, 'GATES', INK, True, 'end') + L(296, water - 20, 'PUMPS', GOLDD, True, 'middle') + L(290, base + 16, 'BUILT ON THE FILL', MUTE, None, 'middle')
    svg += L(110, 12, 'DRAINS BY ITSELF', MUTE, None, 'middle') + L(280, 12, 'ONLY WHEN PUMPED', MUTE, None, 'middle')
    return svg + '</svg>'
