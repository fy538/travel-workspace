// ═══════════════════════════════════════════════════════════════
// TRIP-HOME DRAFTS KIT — shared scaffold for the 3 systems.
// Locked anatomy (per the audit): 4 fixed zones, every phase, same order:
//   1 COVER (identity)  2 VESPER LINE (predictive)  3 SPINE (itinerary)  4 SIBLINGS (tiles)
// Phase = filmstrip (auto truth, browsable, springs back). Forward-peek = evocative empty.
// Reuses T (design-system), Phone/TabBar, StyleRiso/StyleGouache (discover-styles).
// ═══════════════════════════════════════════════════════════════

const DR = {
  ink: '#1B1714', soft: '#2C2622', mute: '#86807A', faint: '#B5AFA5',
  paper: '#EFEAE0', card: '#F7F2E7', cardSoft: '#F3EEE3',
  hair: 'rgba(27,23,20,0.10)', hairThin: 'rgba(27,23,20,0.06)',
  gold: '#B0853A', goldDeep: '#8A6628', blue: '#3D5066',
  serif: '"EB Garamond", Georgia, serif', sans: '"DM Sans", system-ui, sans-serif', mono: '"JetBrains Mono", monospace',
};

const PHASES = ['Ideation', 'Folio', 'Field guide', 'Memory'];

// FILMSTRIP RIBBON — auto-set to `truth`; `at` is where you're looking.
// Peeking (at ≠ truth) shows a faint "· peeking" + the truth dot.
function Filmstrip({ truth = 1, at, onDark }) {
  const here = at == null ? truth : at;
  const baseC = onDark ? 'rgba(255,255,255,0.45)' : DR.faint;
  const onC = onDark ? '#fff' : DR.ink;
  const peeking = here !== truth;
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 7 }}>
      {PHASES.map((p, i) => (
        <React.Fragment key={p}>
          <span style={{ position: 'relative', fontSize: 9, letterSpacing: 1.2, fontWeight: 700, color: i === here ? onC : baseC, textTransform: 'uppercase' }}>
            {p}
            {i === truth && peeking && <span style={{ position: 'absolute', top: -4, right: -6, width: 3.5, height: 3.5, borderRadius: 4, background: DR.gold }}/>}
          </span>
          {i < 3 && <span style={{ width: 10, height: 1, background: i < here ? (onDark ? 'rgba(255,255,255,0.6)' : DR.gold) : baseC, opacity: 0.7 }}/>}
        </React.Fragment>
      ))}
      {peeking && <span style={{ marginLeft: 4, fontFamily: DR.serif, fontStyle: 'italic', fontSize: 10.5, color: onDark ? 'rgba(255,255,255,0.7)' : DR.mute }}>· peeking</span>}
    </div>
  );
}

// Predictive Vesper line — slot 2, always present, forward-looking.
function VLine({ children, kicker = 'VESPER', onDark }) {
  const labelC = onDark ? 'rgba(255,255,255,0.8)' : DR.goldDeep;
  const bodyC = onDark ? '#fff' : DR.ink;
  return (
    <div style={{ display: 'flex', gap: 9, alignItems: 'flex-start' }}>
      <svg width="14" height="14" viewBox="0 0 24 24" fill={onDark ? 'rgba(255,255,255,0.9)' : DR.gold} style={{ flexShrink: 0, marginTop: 2 }}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>
      <div>
        <div style={{ fontSize: 8.5, letterSpacing: 1.6, fontWeight: 700, color: labelC, marginBottom: 3 }}>{kicker}</div>
        <p style={{ margin: 0, fontFamily: DR.serif, fontSize: 15, color: bodyC, lineHeight: 1.38, letterSpacing: -0.1, fontStyle: 'italic' }}>{children}</p>
      </div>
    </div>
  );
}

// People monograms.
function Ppl({ who = [], size = 22, onDark }) {
  const ring = onDark ? 'rgba(20,14,9,0.35)' : DR.card;
  return (
    <div style={{ display: 'flex' }}>
      {who.map((p, i) => (
        <div key={i} style={{ width: size, height: size, borderRadius: 999, background: p.c, color: '#fff', fontFamily: DR.serif, fontSize: size * 0.42, fontWeight: 500, display: 'flex', alignItems: 'center', justifyContent: 'center', marginLeft: i ? -size * 0.3 : 0, border: `1.5px solid ${ring}`, flexShrink: 0 }}>{p.i}</div>
      ))}
    </div>
  );
}
const CASTD = [{ i: 'T', c: '#A0703A' }, { i: 'A', c: '#7C8F73' }, { i: 'M', c: '#3D5066' }];

// Spine preview — a couple of day rows (compact). `empty` shows the gap voice.
function SpinePeek({ rows, openLabel = 'Open the full itinerary' }) {
  return (
    <div>
      {rows.map((r, i) => (
        <div key={i} style={{ display: 'grid', gridTemplateColumns: '34px 1fr', gap: 11, padding: '9px 0', borderTop: i ? `0.5px solid ${DR.hairThin}` : 'none', opacity: r.dim ? 0.5 : 1 }}>
          <div style={{ textAlign: 'center' }}>
            <div style={{ fontSize: 8, letterSpacing: 0.8, color: DR.mute, fontWeight: 700 }}>{r.day}</div>
            <div style={{ fontFamily: DR.serif, fontSize: 18, fontWeight: 500, color: DR.ink, lineHeight: 1, marginTop: 1, letterSpacing: -0.4 }}>{r.date}</div>
          </div>
          <div style={{ alignSelf: 'center' }}>
            <div style={{ fontFamily: DR.serif, fontSize: 14.5, fontWeight: 500, color: r.gap ? DR.mute : DR.ink, fontStyle: r.gap ? 'italic' : 'normal', letterSpacing: -0.2, lineHeight: 1.15 }}>{r.title}</div>
            {r.sub && <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 11, color: DR.mute, marginTop: 2 }}>{r.sub}</div>}
          </div>
        </div>
      ))}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginTop: 11, paddingTop: 11, borderTop: `0.5px solid ${DR.hairThin}` }}>
        <span style={{ fontFamily: DR.serif, fontSize: 14, fontWeight: 500, color: DR.ink, letterSpacing: -0.1 }}>{openLabel}</span>
        <span style={{ color: DR.blue, fontSize: 14 }}>→</span>
      </div>
    </div>
  );
}

// Tile row (siblings, slot 4).
function Tiles({ items }) {
  return (
    <div style={{ display: 'flex', gap: 8 }}>
      {items.map((t, i) => (
        <div key={i} style={{ flex: 1, padding: '11px 12px', background: DR.card, borderRadius: 12, border: `0.5px solid ${t.accent ? 'rgba(176,133,58,0.4)' : DR.hair}` }}>
          <div style={{ color: t.accent ? DR.goldDeep : DR.soft, marginBottom: 7 }}>{t.g}</div>
          <div style={{ fontFamily: DR.serif, fontSize: 13.5, fontWeight: 500, color: DR.ink, letterSpacing: -0.2, lineHeight: 1 }}>{t.label}</div>
          {t.meta && <div style={{ fontSize: 9.5, color: DR.mute, fontFamily: DR.mono, letterSpacing: 0.4, marginTop: 4 }}>{t.meta}</div>}
        </div>
      ))}
    </div>
  );
}
const TGI = {
  map: <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinejoin="round"><path d="M9 4 L3 6.5 V20 L9 17.5 L15 20 L21 17.5 V4 L15 6.5 L9 4Z"/><path d="M9 4v13.5M15 6.5V20"/></svg>,
  costs: <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"><path d="M7 4h10M7 20h10M9 4c0 4 6 4 6 8s-6 4-6 8"/></svg>,
  group: <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinejoin="round"><circle cx="9" cy="9" r="3"/><path d="M3 19c0-3 3-5 6-5s6 2 6 5M16 7a3 3 0 0 1 0 6M21 19c0-2-1.5-3.5-3.5-4.2"/></svg>,
  photos: <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinejoin="round"><rect x="3.5" y="6" width="17" height="13" rx="2"/><circle cx="9" cy="11" r="1.6"/><path d="M3.5 16l5-3 4 2.5 3-2 5 3.5"/></svg>,
  memory: <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinejoin="round"><path d="M7 4h10v16l-5-3.5L7 20z"/></svg>,
  story: <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinejoin="round"><path d="M5 4h9l5 5v11H5z"/><path d="M14 4v5h5"/></svg>,
};

// Tiny section caption.
function Cap({ children, onDark }) {
  return <div style={{ fontSize: 9, letterSpacing: 2, fontWeight: 700, color: onDark ? 'rgba(255,255,255,0.6)' : DR.mute, marginBottom: 9 }}>{children}</div>;
}

// A labelled draft frame for the canvas (title strip above a phone).
function DraftCell({ label, sub, children }) {
  return (
    <div>
      <div style={{ marginBottom: 8 }}>
        <div style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 1.2, color: DR.goldDeep, fontWeight: 600 }}>{label}</div>
        {sub && <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 12, color: DR.mute, marginTop: 1 }}>{sub}</div>}
      </div>
      {children}
    </div>
  );
}

Object.assign(window, { DR, PHASES, Filmstrip, VLine, Ppl, CASTD, SpinePeek, Tiles, TGI, Cap, DraftCell });
