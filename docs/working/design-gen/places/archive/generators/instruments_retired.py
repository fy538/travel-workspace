"""The day charts retired on September 7-8 in favour of pier_line, and the helpers only they used. Kept for history; nothing live imports them.
The Stage 2 instrument brief flags their approximated sun and tide curves as something not to revive."""
from instruments import *

def pier_day(rise='6:31', set_='19:04', plan=('18:30', '19:10', 'THE PIER'), after=('20:30', '21:10', 'THE FILM'), high='8:40', low_window=('14:40', '17:00'), kayaks=('13:00', '16:00', 'KAYAKS'), t0=6, t1=23, h=248):
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
    wpath = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in wpts); wfill = wpath + f' L{ax.x1} {wtop+amp+30} L{ax.x0} {wtop+amp+30} Z'
    lw0, lw1 = hm(low_window[0]), hm(low_window[1]); k0, k1, klab = hm(kayaks[0]), hm(kayaks[1]), kayaks[2]; lowt = hi + T / 2
    svg = f'<svg width="349" height="{h}" viewBox="0 0 349 {h}" fill="none" style="display: block; width: 100%; height: auto; margin-top: 8px;">'
    svg += f'<path d="{fill}" fill="rgba(176,133,58,0.09)"/><path d="{path}" stroke="rgba(27,23,20,0.16)" stroke-width="1.5"/>' + (f'<path d="{ppath}" stroke="{GOLD}" stroke-width="6" stroke-linecap="round"/>' if plan else '')
    svg += f'<line x1="{ax.x0}" y1="{base}" x2="{ax.x1}" y2="{base}" stroke="rgba(27,23,20,0.22)" stroke-width="1"/>'
    svg += f'<rect x="{ax.x(a0):.1f}" y="{base-5}" width="{ax.x(a1)-ax.x(a0):.1f}" height="10" rx="5" fill="{INK}" opacity="0.8"/>'
    svg += f'<circle cx="{ax.x(rise_):.1f}" cy="{base}" r="3" fill="rgba(27,23,20,0.35)"/><circle cx="{ax.x(set__):.1f}" cy="{base}" r="4" fill="{INK}"/>'
    svg += L(ax.x(rise_), base + 15, f'{rise} SUNRISE') + (L(ax.x(p0) - 8, sun_y(p0, rise_, set__, top, base) - 2, f'{plab} · SUNSET {fmt(set__)}', GOLDD, True, 'end') if plan else L(ax.x(set__) - 8, base - 10, f'SUNSET {fmt(set__)}', MUTE, None, 'end')) + L(ax.x(a1), base + 15, f'{alab} {fmt(a0)}', INK, True, 'end')
    svg += f'<path d="{wfill}" fill="rgba(61,80,102,0.18)"/><path d="{wpath}" stroke="{WATER}" stroke-width="2" stroke-linecap="round"/>'
    svg += f'<line x1="{ax.x(lw0):.1f}" y1="{wy(lowt)+6:.1f}" x2="{ax.x(lw1):.1f}" y2="{wy(lowt)+6:.1f}" stroke="{WATER}" stroke-width="3" stroke-linecap="round"/>'
    svg += L(ax.x(hi) + 8, wy(hi) - 8, f'HIGH {high}', WATER) + L(ax.x(lowt), wy(lowt) + 22, f'LOW WATER {fmt(lw0)}–{fmt(lw1)}', INK, True, 'middle')
    ky = wtop + amp + 40; svg += f'<rect x="{ax.x(k0):.1f}" y="{ky}" width="{ax.x(k1)-ax.x(k0):.1f}" height="6" rx="3" fill="{GOLD}"/>' + L(ax.x(k1) + 6, ky + 6, f'{klab} {fmt(k0)}–{fmt(k1)}', GOLDD, True)
    svg += ax.ticks(h - 18, every=3)
    return svg + '</svg>'
def pier_tracks(rise='6:31', set_='19:04', plan=('18:30', '19:04'), after=('20:30', '22:00'), low=('14:40', '17:00'), kayaks=('13:00', '16:00'), t0=6, t1=23, h=76):
    """Three tracks on one axis: the light, the water, the plan. No curves; each track is a bar whose extent is the fact. Two labels."""
    ax = Axis(t0, t1, 2, 347); r, s_, p0, p1, a0, a1, l0, l1, k0, k1 = map(hm, (rise, set_, plan[0], plan[1], after[0], after[1], low[0], low[1], kayaks[0], kayaks[1]))
    svg = f'<svg width="349" height="{h}" viewBox="0 0 349 {h}" fill="none" style="display: block; width: 100%; height: auto; margin-top: 8px;"><defs><linearGradient id="lt" x1="0" x2="1"><stop offset="0" stop-color="{GOLD}" stop-opacity="0.18"/><stop offset="0.5" stop-color="{GOLD}" stop-opacity="0.55"/><stop offset="1" stop-color="{GOLD}" stop-opacity="0.18"/></linearGradient></defs>'
    # light
    svg += f'<rect x="{ax.x(r):.1f}" y="16" width="{ax.x(s_)-ax.x(r):.1f}" height="8" rx="4" fill="url(#lt)"/>'
    svg += f'<rect x="{ax.x(p0):.1f}" y="12" width="{ax.x(p1)-ax.x(p0):.1f}" height="16" rx="8" fill="{GOLD}"/><rect x="{ax.x(a0):.1f}" y="14" width="{ax.x(a1)-ax.x(a0):.1f}" height="12" rx="6" fill="{INK}" opacity="0.8"/>'
    svg += L(ax.x(p0) - 8, 24, f'THE PIER · SUNSET {fmt(s_)}', GOLDD, True, 'end')
    # water: a thin band, lighter where the water is low; the low window as a gap in the band
    svg += f'<rect x="2" y="44" width="345" height="6" rx="3" fill="rgba(61,80,102,0.35)"/><rect x="{ax.x(l0):.1f}" y="44" width="{ax.x(l1)-ax.x(l0):.1f}" height="6" rx="3" fill="{PAPER}"/><rect x="{ax.x(l0):.1f}" y="46" width="{ax.x(l1)-ax.x(l0):.1f}" height="2" fill="rgba(61,80,102,0.35)"/>'
    svg += f'<rect x="{ax.x(k0):.1f}" y="56" width="{ax.x(k1)-ax.x(k0):.1f}" height="4" rx="2" fill="{GOLD}"/>'
    svg += L((ax.x(l0) + ax.x(l1)) / 2, h - 4, f'LOW WATER {fmt(l0)}–{fmt(l1)} · KAYAKS TILL {fmt(k1)}', WATER, True, 'middle')
    return svg + '</svg>'
def pier_arc_small(rise='6:31', set_='19:04', plan=('18:30', '19:04'), after=('20:30', '22:00'), low=('14:40', '17:00'), t0=6, t1=23, h=72):
    """The arc, reduced to the canon's size: the arc, the gold end, an ink bar after dark, the low-water window as a bracket under the baseline. Two labels."""
    ax = Axis(t0, t1, 8, 341); r, s_, p0, p1, a0, a1, l0, l1 = map(hm, (rise, set_, plan[0], plan[1], after[0], after[1], low[0], low[1])); base = 44; top = 10
    pts = [(ax.x(t), sun_y(t, r, s_, top, base)) for t in [r + i * (s_ - r) / 60 for i in range(61)]]
    path = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts)
    ppts = [(ax.x(t), sun_y(t, r, s_, top, base)) for t in [p0 + i * (min(p1, s_) - p0) / 20 for i in range(21)]]
    svg = f'<svg width="349" height="{h}" viewBox="0 0 349 {h}" fill="none" style="display: block; width: 100%; height: auto; margin-top: 8px;">'
    svg += f'<path d="{path}" stroke="rgba(27,23,20,0.18)" stroke-width="1.5"/><path d="M{" L".join(f"{x:.1f} {y:.1f}" for x, y in ppts)}" stroke="{GOLD}" stroke-width="6" stroke-linecap="round"/>'
    svg += f'<line x1="{ax.x0}" y1="{base}" x2="{ax.x1}" y2="{base}" stroke="rgba(27,23,20,0.22)"/><rect x="{ax.x(a0):.1f}" y="{base-5}" width="{ax.x(a1)-ax.x(a0):.1f}" height="10" rx="5" fill="{INK}" opacity="0.8"/><circle cx="{ax.x(s_):.1f}" cy="{base}" r="4" fill="{INK}"/>'
    svg += f'<path d="M{ax.x(l0):.1f} {base+8} v6 h{ax.x(l1)-ax.x(l0):.1f} v-6" stroke="{WATER}" stroke-width="1.5" fill="none"/>'
    svg += L(ax.x(p0) - 8, sun_y(p0, r, s_, top, base) - 2, f'THE PIER · SUNSET {fmt(s_)}', GOLDD, True, 'end') + L((ax.x(l0) + ax.x(l1)) / 2, base + 26, f'LOW WATER {fmt(l0)}–{fmt(l1)}', WATER, True, 'middle')
    return svg + '</svg>'
def sun_y(t, rise, set_, top, base):
    """Elevation as a half-sine between rise and set; below the horizon the curve is not drawn."""
    if t < rise or t > set_: return base
    return base - (top and (base - top)) * math.sin(math.pi * (t - rise) / (set_ - rise))