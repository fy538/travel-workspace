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
def sun_y(t, rise, set_, top, base):
    """Elevation as a half-sine between rise and set; below the horizon the curve is not drawn."""
    if t < rise or t > set_: return base
    return base - (top and (base - top)) * math.sin(math.pi * (t - rise) / (set_ - rise))
def _lowlab(ax, wy, lowt, lw0, lw1):
    """The low-water label sits above the curve wherever the curve is highest under the label's span: computed, not guessed."""
    lab = f'LOW WATER {fmt(lw0)}–{fmt(lw1)}'; wpx = len(lab) * 6.4; xr = ax.x(lowt) + 14; xl = xr - wpx
    tl = ax.t0 + (xl - ax.x0) / (ax.x1 - ax.x0) * (ax.t1 - ax.t0); tr = ax.t0 + (xr - ax.x0) / (ax.x1 - ax.x0) * (ax.t1 - ax.t0)
    ytop = min(wy(tl + i * (tr - tl) / 20) for i in range(21))
    return L(xr, ytop - 6, lab, INK, True, 'end')
def pier_day(rise='6:31', set_='19:04', plan=('18:30', '19:10', 'THE PIER'), after=('20:30', '21:10', 'THE FILM'), high='8:40', low_window=('14:40', '17:00'), kayaks=('13:00', '16:00', 'KAYAKS'), t0=6, t1=23, h=224):
    """The pier's day on one axis: the sun above the line, the water below it; the plan as gold on the sun; after dark as ink on the line; the low-water window on the tide.
    Zones: sun 12..96 (base 96); a label row under the base; water 130..190; the kayaks bar under the water; ticks at the foot."""
    ax = Axis(t0, t1); rise_, set__ = hm(rise), hm(set_); base = 96; top = 14
    pts = [(ax.x(t), sun_y(t, rise_, set__, top, base)) for t in [rise_ + i * (set__ - rise_) / 60 for i in range(61)]]
    path = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts); fill = path + f' L{ax.x(set__):.1f} {base} L{ax.x(rise_):.1f} {base} Z'
    if plan:
        p0, p1, plab = hm(plan[0]), hm(plan[1]), plan[2]
        ppts = [(ax.x(t), sun_y(t, rise_, set__, top, base)) for t in [p0 + i * (min(p1, set__) - p0) / 20 for i in range(21)]]
        ppath = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in ppts)
    a0, a1, alab = hm(after[0]), hm(after[1]), after[2]
    hi = hm(high); T = 12.42; wtop = 134; amp = 40
    wy = lambda t: wtop + amp * (1 - math.cos(2 * math.pi * (t - hi) / T)) / 2
    wpts = [(ax.x(t), wy(t)) for t in [t0 + i * (t1 - t0) / 120 for i in range(121)]]
    wpath = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in wpts); wfill = wpath + f' L{ax.x1} {wtop+amp+8} L{ax.x0} {wtop+amp+8} Z'
    lw0, lw1 = hm(low_window[0]), hm(low_window[1]); k0, k1, klab = hm(kayaks[0]), hm(kayaks[1]), kayaks[2]; lowt = hi + T / 2
    svg = f'<svg width="349" height="{h}" viewBox="0 0 349 {h}" fill="none" style="display: block; width: 100%; height: auto; margin-top: 8px;">'
    svg += f'<path d="{fill}" fill="rgba(176,133,58,0.09)"/><path d="{path}" stroke="rgba(27,23,20,0.16)" stroke-width="1.5"/>' + (f'<path d="{ppath}" stroke="{GOLD}" stroke-width="6" stroke-linecap="round"/>' if plan else '')
    svg += f'<line x1="{ax.x0}" y1="{base}" x2="{ax.x1}" y2="{base}" stroke="rgba(27,23,20,0.22)" stroke-width="1"/>'
    svg += f'<rect x="{ax.x(a0):.1f}" y="{base-5}" width="{ax.x(a1)-ax.x(a0):.1f}" height="10" rx="5" fill="{INK}" opacity="0.8"/>'
    svg += f'<circle cx="{ax.x(rise_):.1f}" cy="{base}" r="3" fill="rgba(27,23,20,0.35)"/><circle cx="{ax.x(set__):.1f}" cy="{base}" r="4" fill="{INK}"/>'
    svg += L(ax.x(rise_), base + 15, f'{rise} SUNRISE') + (L(ax.x(p0) - 8, sun_y(p0, rise_, set__, top, base) - 2, f'{plab} · SUNSET {fmt(set__)}', GOLDD, True, 'end') if plan else L(ax.x(set__) - 8, base - 10, f'SUNSET {fmt(set__)}', MUTE, None, 'end')) + L(ax.x(a1), base + 15, f'{alab} {fmt(a0)}', INK, True, 'end')
    svg += f'<path d="{wfill}" fill="rgba(61,80,102,0.18)"/><path d="{wpath}" stroke="{WATER}" stroke-width="2" stroke-linecap="round"/>'
    svg += f'<line x1="{ax.x(lw0):.1f}" y1="{wy(lowt)+7:.1f}" x2="{ax.x(lw1):.1f}" y2="{wy(lowt)+7:.1f}" stroke="{WATER}" stroke-width="3" stroke-linecap="round"/>'
    svg += L(ax.x(hi) + 8, wy(hi) - 8, f'HIGH {high}', WATER) + _lowlab(ax, wy, lowt, lw0, lw1)
    ky = wtop + amp + 18; svg += f'<rect x="{ax.x(k0):.1f}" y="{ky}" width="{ax.x(k1)-ax.x(k0):.1f}" height="6" rx="3" fill="{GOLD}"/>' + L(ax.x(k1) + 6, ky + 6, f'{klab} {fmt(k0)}–{fmt(k1)}', GOLDD, True)
    svg += ax.ticks(h - 18, every=3)
    return svg + '</svg>'
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
def access_compare(rows, h=None):
    """Two ways to a place on one minutes scale: dots on foot, a solid bar for the ride, the total at the end. Same scale for both, so the difference is visible, not asserted."""
    total = max(sum(m for m, k in r[1]) for r in rows); ax = Axis(0, total, 100, 300); h = h or 20 + 44 * len(rows)
    svg = f'<svg width="349" height="{h}" viewBox="0 0 349 {h}" fill="none" style="display: block; width: 100%; height: auto; margin-top: 8px;">'
    for i, (name, legs, note) in enumerate(rows):
        y = 22 + i * 44; svg += L(2, y + 4, name, INK, True); t = 0
        for m, kind in legs:
            x0, x1 = ax.x(t), ax.x(t + m)
            if kind == 'foot': svg += f'<path d="M{x0+4:.1f} {y} L{x1-2:.1f} {y}" stroke="rgba(27,23,20,0.30)" stroke-width="8" stroke-dasharray="0.1 12" stroke-linecap="round"/>'
            else: svg += f'<rect x="{x0:.1f}" y="{y-6}" width="{x1-x0:.1f}" height="12" rx="6" fill="{INK}" opacity="0.78"/>'
            t += m
        svg += L(ax.x(t) + 8, y + 4, f'~{t}', INK, True) + L(2, y + 18, note, MUTE)
    svg += L(100, h - 2, '0', MUTE) + L(300, h - 2, f'{total} MIN', MUTE, None, 'end')
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
