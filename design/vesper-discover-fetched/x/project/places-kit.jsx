// ═══════════════════════════════════════════════════════════════
// VESPER · PLACES — shared spine atoms.
// The Take is the primitive: Personal (gold, Vesper's voice) over
// Curator (the editorial base). Every surface leads with it; when
// signal is thin it says so (the forming state) rather than invent.
// Reuses T, Phone, TabBar, VesperMark, Plate.
// ═══════════════════════════════════════════════════════════════

const PINK = '#A04030';                 // oxblood — urgency only
const SAGE = '#7C8F73';                 // quiet / dreaming
const INKBLUE = '#3D5066';              // planning
const hp = `0.5px solid ${T.hairline}`;
const hpT = `0.5px solid ${T.hairThin}`;

// ─── small letter-spaced caps eyebrow ───────────────────────────
function Eye({ children, c = T.mute }) {
  return <div style={{ fontSize: 9.5, letterSpacing: 1.9, fontWeight: 700, color: c, fontFamily: T.sans }}>{children}</div>;
}

// ─── a back/▾ screen header that floats over a hero ─────────────
function SpotTopBar({ onDark, label }) {
  const c = onDark ? 'rgba(255,255,255,0.95)' : T.inkSoft;
  return (
    <div style={{ position: 'absolute', top: 54, left: 0, right: 0, zIndex: 20, display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '10px 18px' }}>
      <div style={{ width: 34, height: 34, borderRadius: 999, background: onDark ? 'rgba(20,14,9,0.32)' : 'rgba(247,242,231,0.8)', backdropFilter: 'blur(8px)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
      </div>
      {label && <span style={{ fontSize: 8.5, letterSpacing: 1.8, fontWeight: 700, color: c }}>{label}</span>}
      <div style={{ display: 'flex', gap: 8 }}>
        {['save', 'share'].map((k) => (
          <div key={k} style={{ width: 34, height: 34, borderRadius: 999, background: onDark ? 'rgba(20,14,9,0.32)' : 'rgba(247,242,231,0.8)', backdropFilter: 'blur(8px)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            {k === 'save'
              ? <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M6 4h12v16l-6-4-6 4V4Z"/></svg>
              : <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><circle cx="6" cy="12" r="2.4"/><circle cx="17" cy="6" r="2.4"/><circle cx="17" cy="18" r="2.4"/><path d="M8.1 10.9l6.8-3.8M8.1 13.1l6.8 3.8"/></svg>}
          </div>
        ))}
      </div>
    </div>
  );
}

// ─── THE TAKE — the dominant block, Personal over Curator ───────
// state: 'rich' | 'cold' | 'forming'
function TakeBlock({ state = 'rich', verdict, body, curator, pill = 'WORTH REARRANGING A DAY FOR', why = [] }) {
  return (
    <div style={{ padding: '20px 22px', background: T.cardWarm, borderRadius: 18, border: hp, boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset, 0 14px 30px -22px rgba(0,0,0,0.3)' }}>
      {/* Personal layer — Vesper's voice, gold */}
      {state === 'rich' && (
        <>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
            <VesperMark s={15}/>
            <Eye c={T.goldDeep}>VESPER · FOR YOU</Eye>
          </div>
          <p style={{ fontFamily: T.serif, fontSize: 23, fontWeight: 500, color: T.ink, lineHeight: 1.22, letterSpacing: -0.4, margin: '12px 0 0' }}>{verdict}</p>
          <p style={{ fontFamily: T.serif, fontSize: 15.5, color: T.inkSoft, lineHeight: 1.5, margin: '10px 0 0' }}>{body}</p>
          {pill && <div style={{ marginTop: 14, display: 'inline-flex', alignItems: 'center', gap: 7, padding: '6px 12px', background: 'rgba(176,133,58,0.12)', borderRadius: 999 }}>
            <span style={{ fontSize: 9.5, letterSpacing: 1.4, fontWeight: 700, color: T.goldDeep }}>{pill}</span>
          </div>}
        </>
      )}

      {/* Cold-start — curator only; personal layer invites building one */}
      {state === 'cold' && (
        <>
          <Eye c={T.goldDeep}>THE READ</Eye>
          <p style={{ fontFamily: T.serif, fontSize: 21, fontWeight: 500, color: T.ink, lineHeight: 1.26, letterSpacing: -0.3, margin: '11px 0 0' }}>{verdict}</p>
          <p style={{ fontFamily: T.serif, fontSize: 15, color: T.inkSoft, lineHeight: 1.5, margin: '10px 0 0' }}>{curator}</p>
          <div style={{ marginTop: 16, paddingTop: 14, borderTop: hpT, display: 'flex', alignItems: 'center', gap: 10 }}>
            <VesperMark s={15}/>
            <span style={{ flex: 1, fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.mute, lineHeight: 1.4 }}>I don’t know your taste here yet — tell me one thing and I’ll start a read.</span>
          </div>
        </>
      )}

      {/* Forming — the honest, dignified state */}
      {state === 'forming' && (
        <>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
            <VesperMark s={15} c={SAGE}/>
            <Eye c={SAGE}>VESPER · STILL READING</Eye>
          </div>
          <p style={{ fontFamily: T.serif, fontSize: 21, fontWeight: 500, color: T.inkSoft, lineHeight: 1.26, letterSpacing: -0.3, margin: '12px 0 0', fontStyle: 'italic' }}>{verdict}</p>
          <p style={{ fontFamily: T.serif, fontSize: 14.5, color: T.mute, lineHeight: 1.5, margin: '10px 0 0' }}>{body}</p>
          <div style={{ marginTop: 15 }}>
            <span style={{ display: 'inline-flex', alignItems: 'center', gap: 7, padding: '8px 14px', borderRadius: 999, border: `0.8px solid ${SAGE}`, color: SAGE, fontSize: 12.5, fontWeight: 600 }}>
              <VesperMark s={13} c={SAGE}/> Ask Vesper to look closer
            </span>
          </div>
        </>
      )}

      {/* Curator strip — the base layer, always present under personal */}
      {state === 'rich' && curator && (
        <div style={{ marginTop: 16, paddingTop: 14, borderTop: hpT }}>
          <Eye>THE CURATOR’S READ</Eye>
          <p style={{ fontFamily: T.serif, fontSize: 14, color: T.mute, lineHeight: 1.5, margin: '7px 0 0' }}>{curator}</p>
        </div>
      )}

      {/* the "why" — Vesper's reasoning chips */}
      {why.length > 0 && (
        <div style={{ marginTop: 14, display: 'flex', flexWrap: 'wrap', gap: 6 }}>
          {why.map((w) => <span key={w} style={{ padding: '4px 10px', fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.goldDeep, background: T.bg, borderRadius: 999, border: hpT }}>{w}</span>)}
        </div>
      )}
    </div>
  );
}

// ─── loading shimmer for the personal layer ─────────────────────
function TakeLoading() {
  return (
    <div style={{ padding: '20px 22px', background: T.cardWarm, borderRadius: 18, border: hp }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
        <VesperMark s={15}/>
        <Eye c={T.goldDeep}>VESPER IS READING YOU IN…</Eye>
      </div>
      <div style={{ marginTop: 14, display: 'flex', flexDirection: 'column', gap: 9 }}>
        {[100, 92, 64].map((w, i) => <div key={i} style={{ height: 13, width: `${w}%`, borderRadius: 4, background: 'linear-gradient(90deg, rgba(176,133,58,0.14), rgba(176,133,58,0.05))' }}/>)}
      </div>
      <div style={{ marginTop: 16, paddingTop: 14, borderTop: hpT }}>
        <Eye>THE CURATOR’S READ</Eye>
        <p style={{ fontFamily: T.serif, fontSize: 14, color: T.inkSoft, lineHeight: 1.5, margin: '7px 0 0' }}>A tiny counter for natural wine, runs on instinct — the list changes by the night.</p>
      </div>
    </div>
  );
}

// ─── collapsible "the details" header ───────────────────────────
function DetailsHeader({ open = true }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 10, padding: '0 2px' }}>
      <Eye>THE DETAILS</Eye>
      <span style={{ flex: 1, height: 1, background: T.hairline }}/>
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke={T.mute} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ transform: open ? 'none' : 'rotate(-90deg)' }}><path d="M6 9l6 6 6-6"/></svg>
    </div>
  );
}

// a two-column fact row (label · value)
function FactRow({ label, children, accent }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '96px 1fr', gap: 12, padding: '10px 0', borderTop: hpT, alignItems: 'baseline' }}>
      <span style={{ fontSize: 9.5, letterSpacing: 1.3, fontWeight: 700, color: T.mute, paddingTop: 2 }}>{label}</span>
      <span style={{ fontFamily: T.serif, fontSize: 14.5, color: accent || T.ink, lineHeight: 1.4 }}>{children}</span>
    </div>
  );
}

// order / skip two-up
function OrderSkip({ order, skip }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 10, padding: '4px 0 2px' }}>
      <div style={{ padding: '12px 14px', background: 'rgba(124,143,115,0.10)', borderRadius: 12 }}>
        <Eye c={SAGE}>ORDER</Eye>
        <p style={{ fontFamily: T.serif, fontSize: 14, color: T.ink, lineHeight: 1.35, margin: '6px 0 0' }}>{order}</p>
      </div>
      <div style={{ padding: '12px 14px', background: 'rgba(160,64,48,0.07)', borderRadius: 12 }}>
        <Eye c={PINK}>SKIP</Eye>
        <p style={{ fontFamily: T.serif, fontSize: 14, color: T.inkSoft, lineHeight: 1.35, margin: '6px 0 0' }}>{skip}</p>
      </div>
    </div>
  );
}

// energy marks (1–5 small dots)
function EnergyMarks({ rows = [['Physical', 2], ['Cognitive', 1], ['Social', 4]] }) {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
      {rows.map(([k, n]) => (
        <div key={k} style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
          <span style={{ width: 70, fontSize: 11, color: T.mute, fontWeight: 500 }}>{k}</span>
          <div style={{ display: 'flex', gap: 5 }}>
            {[1, 2, 3, 4, 5].map((i) => <span key={i} style={{ width: 7, height: 7, borderRadius: 999, background: i <= n ? T.goldDeep : 'rgba(27,23,20,0.12)' }}/>)}
          </div>
        </div>
      ))}
    </div>
  );
}

// world-model link rows (→ Place, related reads, similar)
function WorldLink({ icon, label, sub, tint = INKBLUE }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '12px 14px', background: T.card, borderRadius: 13, border: hp }}>
      <span style={{ width: 30, height: 30, borderRadius: 8, background: 'rgba(61,80,102,0.10)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: tint, flexShrink: 0 }}>{icon}</span>
      <div style={{ flex: 1, minWidth: 0 }}>
        <div style={{ fontFamily: T.serif, fontSize: 15, fontWeight: 500, color: T.ink, letterSpacing: -0.2 }}>{label}</div>
        <div style={{ fontSize: 11.5, color: T.mute, marginTop: 1 }}>{sub}</div>
      </div>
      <span style={{ color: T.muteSoft, fontSize: 15 }}>→</span>
    </div>
  );
}

// ─── sticky launch-action rail ──────────────────────────────────
function ActionRail({ book }) {
  const rest = [
    ['save', 'Save'], ['hear', 'Hear'], ['map', 'Map'], ...(book ? [['book', book]] : []), ['similar', 'Similar'],
  ];
  const icon = {
    save: <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M6 4h12v16l-6-4-6 4V4Z"/></svg>,
    hear: <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M3 10v4h4l5 4V6L7 10H3Z"/><path d="M16 9a4 4 0 0 1 0 6"/></svg>,
    map: <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M9 4 3 6v14l6-2 6 2 6-2V4l-6 2-6-2Z"/><path d="M9 4v14M15 6v14"/></svg>,
    book: <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><rect x="4" y="5" width="16" height="16" rx="2"/><path d="M4 9h16M8 3v4M16 3v4"/></svg>,
    similar: <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><circle cx="7" cy="7" r="3.4"/><circle cx="17" cy="17" r="3.4"/><path d="M7 10.5v3M17 10.5v3"/></svg>,
  };
  return (
    <div style={{ position: 'absolute', left: 14, right: 14, bottom: 16, zIndex: 25 }}>
      {/* primary: Add to plan + Ask */}
      <div style={{ display: 'flex', gap: 8, marginBottom: 9 }}>
        <button style={{ flex: 1, border: 'none', display: 'inline-flex', alignItems: 'center', justifyContent: 'center', gap: 8, padding: '14px 0', background: INKBLUE, color: '#fff', borderRadius: 16, fontFamily: T.sans, fontSize: 14.5, fontWeight: 600, letterSpacing: -0.1, boxShadow: '0 10px 24px -12px rgba(61,80,102,0.7)' }}>
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round"><path d="M12 5v14M5 12h14"/></svg>
          Add to plan
        </button>
        <button style={{ width: 132, border: `0.8px solid ${T.gold}`, display: 'inline-flex', alignItems: 'center', justifyContent: 'center', gap: 7, padding: '14px 0', background: 'rgba(176,133,58,0.10)', color: T.goldDeep, borderRadius: 16, fontFamily: T.sans, fontSize: 14, fontWeight: 600 }}>
          <VesperMark s={15}/> Ask
        </button>
      </div>
      {/* secondary rail */}
      <div style={{ display: 'flex', alignItems: 'stretch', gap: 6, padding: 6, background: 'rgba(247,242,231,0.9)', backdropFilter: 'blur(18px)', borderRadius: 18, border: '0.5px solid rgba(0,0,0,0.06)', boxShadow: '0 8px 24px -10px rgba(0,0,0,0.16)' }}>
        {rest.map(([k, label]) => (
          <div key={k} style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 4, padding: '7px 0', color: T.inkSoft }}>
            {icon[k]}
            <span style={{ fontSize: 9.5, fontWeight: 600, letterSpacing: 0.1, color: T.mute }}>{label}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

// scroll body that clears the rail
function SpotBody({ children, pad = 232 }) {
  return (
    <div style={{ position: 'absolute', top: 0, left: 0, right: 0, bottom: 0, overflow: 'hidden' }}>
      <div style={{ paddingBottom: pad }}>{children}</div>
    </div>
  );
}

Object.assign(window, {
  PINK, SAGE, INKBLUE, Eye, SpotTopBar, TakeBlock, TakeLoading,
  DetailsHeader, FactRow, OrderSkip, EnergyMarks, WorldLink, ActionRail, SpotBody,
});
