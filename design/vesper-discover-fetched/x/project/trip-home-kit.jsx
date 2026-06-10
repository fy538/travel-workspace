// ═══════════════════════════════════════════════════════════════
// TRIP-HOME KIT — the single-trip home as an evolving artifact.
// Four phases: ideation → pre-trip folio → live field guide → memory object.
// Reuses T (design-system), Phone/TabBar, StyleRiso/StyleGouache (discover-styles),
// TR (trips-shared ink-blue) where present.
// ═══════════════════════════════════════════════════════════════

const TH = {
  ink: '#1B1714', soft: '#2C2622', mute: '#86807A', faint: '#B5AFA5',
  paper: '#EFEAE0', card: '#F7F2E7', cardSoft: '#F3EEE3',
  hair: 'rgba(27,23,20,0.10)', hairThin: 'rgba(27,23,20,0.06)',
  gold: '#B0853A', goldDeep: '#8A6628', earth: '#A6703C',
  blue: '#3D5066', blueDeep: '#2A384B',
  serif: '"EB Garamond", Georgia, serif',
  sans: '"DM Sans", system-ui, sans-serif',
  mono: '"JetBrains Mono", monospace',
};

// Quiet trip-home header — back · (title only if no hero) · small controls.
function TripHeader({ title, showTitle = false, controls = true, onDark = false }) {
  const c = onDark ? 'rgba(255,255,255,0.92)' : TH.soft;
  const ico = (d) => <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">{d}</svg>;
  return (
    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '12px 18px 0' }}>
      {ico(<path d="M14 6l-6 6 6 6"/>)}
      {showTitle
        ? <span style={{ fontFamily: TH.serif, fontSize: 16, fontWeight: 500, color: c, letterSpacing: -0.2 }}>{title}</span>
        : <span/>}
      {controls ? (
        <div style={{ display: 'flex', gap: 16 }}>
          {ico(<><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></>)}
          {ico(<><circle cx="12" cy="12" r="3"/><path d="M19 12a7 7 0 0 0-.1-1l2-1.5-2-3.5-2.4 1a7 7 0 0 0-1.7-1l-.4-2.5h-4l-.4 2.5a7 7 0 0 0-1.7 1l-2.4-1-2 3.5 2 1.5a7 7 0 0 0 0 2l-2 1.5 2 3.5 2.4-1a7 7 0 0 0 1.7 1l.4 2.5h4l.4-2.5a7 7 0 0 0 1.7-1l2.4 1 2-3.5-2-1.5a7 7 0 0 0 .1-1z"/></>)}
        </div>
      ) : <span style={{ width: 19 }}/>}
    </div>
  );
}

// Phase ribbon — the four states, current one lit. The artifact's "age".
function PhaseRibbon({ phase, onDark }) {
  const phases = ['Ideation', 'Folio', 'Field guide', 'Memory'];
  const base = onDark ? 'rgba(255,255,255,0.5)' : TH.faint;
  const on = onDark ? '#fff' : TH.ink;
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 7 }}>
      {phases.map((p, i) => (
        <React.Fragment key={p}>
          <span style={{ fontSize: 9, letterSpacing: 1.2, fontWeight: 700, color: i === phase ? on : base, textTransform: 'uppercase' }}>{p}</span>
          {i < 3 && <span style={{ width: 4, height: 4, borderRadius: 4, background: i < phase ? (onDark ? 'rgba(255,255,255,0.7)' : TH.gold) : base, opacity: i === phase ? 1 : 0.6 }}/>}
        </React.Fragment>
      ))}
    </div>
  );
}

// People — overlapping monograms.
function People({ who = [], onDark, size = 24 }) {
  const ring = onDark ? 'rgba(20,14,9,0.4)' : TH.card;
  return (
    <div style={{ display: 'flex' }}>
      {who.map((p, i) => (
        <div key={i} style={{
          width: size, height: size, borderRadius: 999, background: p.c, color: '#fff',
          fontFamily: TH.serif, fontSize: size * 0.42, fontWeight: 500,
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          marginLeft: i ? -size * 0.32 : 0, border: `1.5px solid ${ring}`, flexShrink: 0,
        }}>{p.i}</div>
      ))}
    </div>
  );
}
const CAST = [{ i: 'T', c: '#A0703A' }, { i: 'A', c: '#7C8F73' }, { i: 'M', c: '#3D5066' }];

// Section label.
function Label({ children, right, onDark }) {
  const c = onDark ? 'rgba(255,255,255,0.7)' : TH.mute;
  return (
    <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between' }}>
      <span style={{ fontSize: 9.5, letterSpacing: 2, color: c, fontWeight: 700 }}>{children}</span>
      {right && <span style={{ fontSize: 9.5, letterSpacing: 1.4, color: c, fontWeight: 600, opacity: 0.8 }}>{right}</span>}
    </div>
  );
}

// A Vesper note — the one editorial line. Ochre spark.
function VesperLine({ children, kicker = 'VESPER' }) {
  return (
    <div style={{ display: 'flex', gap: 9, alignItems: 'flex-start' }}>
      <svg width="14" height="14" viewBox="0 0 24 24" fill={TH.gold} style={{ flexShrink: 0, marginTop: 3 }}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>
      <div>
        <div style={{ fontSize: 9, letterSpacing: 1.6, fontWeight: 700, color: TH.goldDeep, marginBottom: 3 }}>{kicker}</div>
        <p style={{ margin: 0, fontFamily: TH.serif, fontSize: 15, color: TH.ink, lineHeight: 1.4, letterSpacing: -0.1, fontStyle: 'italic' }}>{children}</p>
      </div>
    </div>
  );
}

// A day row — the journal's spine.
function DayRow({ n, day, date, title, sub, dim, done }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '40px 1fr', gap: 12, padding: '11px 0', borderTop: `0.5px solid ${TH.hairThin}`, opacity: dim ? 0.55 : 1 }}>
      <div style={{ textAlign: 'center' }}>
        <div style={{ fontSize: 8.5, letterSpacing: 1, color: TH.mute, fontWeight: 700 }}>{day}</div>
        <div style={{ fontFamily: TH.serif, fontSize: 21, fontWeight: 500, color: done ? TH.mute : TH.ink, lineHeight: 1, marginTop: 1, fontVariantNumeric: 'oldstyle-nums', letterSpacing: -0.5 }}>{date}</div>
      </div>
      <div>
        <div style={{ fontFamily: TH.serif, fontSize: 15.5, fontWeight: 500, color: TH.ink, letterSpacing: -0.2, lineHeight: 1.15 }}>{title}</div>
        {sub && <div style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 12, color: TH.mute, marginTop: 3, lineHeight: 1.3 }}>{sub}</div>}
      </div>
    </div>
  );
}

// Object tile — demoted tools as elegant launchers (Map, Photos, Costs, Memory).
function ObjectTile({ glyph, label, meta, accent }) {
  return (
    <div style={{ flex: 1, padding: '12px 12px 11px', background: TH.card, borderRadius: 12, border: `0.5px solid ${accent ? 'rgba(176,133,58,0.4)' : TH.hair}`, boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset' }}>
      <div style={{ color: accent ? TH.goldDeep : TH.soft, marginBottom: 8 }}>{glyph}</div>
      <div style={{ fontFamily: TH.serif, fontSize: 14, fontWeight: 500, color: TH.ink, letterSpacing: -0.2, lineHeight: 1 }}>{label}</div>
      {meta && <div style={{ fontSize: 10, color: TH.mute, fontFamily: TH.mono, letterSpacing: 0.5, marginTop: 4 }}>{meta}</div>}
    </div>
  );
}
const TG = {
  map: <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinejoin="round"><path d="M9 4 L3 6.5 V20 L9 17.5 L15 20 L21 17.5 V4 L15 6.5 L9 4Z"/><path d="M9 4v13.5M15 6.5V20"/></svg>,
  photos: <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinejoin="round"><rect x="3.5" y="6" width="17" height="13" rx="2"/><circle cx="9" cy="11" r="1.6"/><path d="M3.5 16l5-3 4 2.5 3-2 5 3.5"/></svg>,
  costs: <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"><path d="M7 4h10M7 20h10M9 4c0 4 6 4 6 8s-6 4-6 8"/></svg>,
  memory: <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinejoin="round"><path d="M7 4h10v16l-5-3.5L7 20z"/></svg>,
  story: <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinejoin="round"><path d="M5 4h9l5 5v11H5z"/><path d="M14 4v5h5"/></svg>,
  chat: <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinejoin="round"><path d="M4 5h16v11H8l-4 4z"/></svg>,
};

Object.assign(window, { TH, TripHeader, PhaseRibbon, People, CAST, Label, VesperLine, DayRow, ObjectTile, TG });
