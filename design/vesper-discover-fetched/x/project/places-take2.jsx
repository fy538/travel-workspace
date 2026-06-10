// ═══════════════════════════════════════════════════════════════
// VESPER · PLACES v2 — the structured, selective Take.
// The Take is COMPONENTS, not prose: a verdict chip (opinion +
// confidence + provenance), typed caveats (severity × reason), and
// a DATA-DRIVEN action rail (renders suggested_actions). The page
// shows the verdict + 2–4 decision-changing facts; everything else
// tucks into "the details". Confidence visibly modulates how
// assertive — and how fact-rich — the page is.
// ═══════════════════════════════════════════════════════════════

// ── opinion + confidence vocab ──────────────────────────────────
const OPIN = {
  loved:       { label: 'Loved',       c: '#8A6628', fill: '#B0853A', soft: 'rgba(176,133,58,0.13)' },
  worthit:     { label: 'Worth it',    c: '#8A6628', fill: '#B0853A', soft: 'rgba(176,133,58,0.11)' },
  conditional: { label: 'Conditional', c: '#5E6E55', fill: '#7C8F73', soft: 'rgba(124,143,115,0.14)' },
  skip:        { label: 'Skip',        c: '#A04030', fill: '#A04030', soft: 'rgba(160,64,48,0.09)' },
};
const CONF = { high: 3, medium: 2, low: 1 };

// ── VERDICT CHIP — opinion · confidence · provenance ────────────
function Verdict({ opinion = 'loved', confidence = 'high', provenance }) {
  const o = OPIN[opinion];
  const n = CONF[confidence];
  const filled = confidence === 'high';
  return (
    <div>
      <div style={{ display: 'flex', alignItems: 'center', gap: 9 }}>
        <span style={{
          display: 'inline-flex', alignItems: 'center', gap: 7, padding: '5px 12px 5px 11px', borderRadius: 999,
          background: filled ? o.fill : o.soft, border: filled ? 'none' : `1px solid ${o.fill}`,
        }}>
          <VesperMark s={13} c={filled ? '#fff' : o.c}/>
          <span style={{ fontFamily: T.sans, fontSize: 12.5, fontWeight: 700, letterSpacing: 0.2, color: filled ? '#fff' : o.c }}>{o.label}</span>
        </span>
        {/* confidence as three bars */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 3 }} title={`${confidence} confidence`}>
          {[1, 2, 3].map((i) => <span key={i} style={{ width: 4, height: 11, borderRadius: 2, background: i <= n ? o.fill : 'rgba(27,23,20,0.13)' }}/>)}
          <span style={{ marginLeft: 4, fontSize: 9, letterSpacing: 1, fontWeight: 700, color: T.muteSoft }}>{confidence.toUpperCase()}</span>
        </div>
      </div>
      {provenance && <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginTop: 9 }}>
        <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke={T.muteSoft} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M12 8v4l3 2"/><circle cx="12" cy="12" r="9"/></svg>
        <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.mute }}>{provenance}</span>
      </div>}
    </div>
  );
}

// ── TYPED CAVEATS — severity × reason, only the 1–3 that apply ──
const CAVEAT_ICON = {
  dietary: (c) => <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M11 3C7 3 4 6 4 10c0 5 4 9 7 11 0-6 0-13 0-18Z"/><path d="M16 3c2 2 3 5 3 8s-1 6-3 8"/></svg>,
  accessibility: (c) => <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M4 6h7l2 6h5M6 6l2 9h8M8 19l3-4"/></svg>,
  logistics: (c) => <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M12 21s7-6.4 7-11a7 7 0 1 0-14 0c0 4.6 7 11 7 11Z"/><circle cx="12" cy="10" r="2.2"/></svg>,
  fit: (c) => <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="8" r="3.2"/><path d="M5 20c0-3.5 3-6 7-6s7 2.5 7 6"/></svg>,
  safety: (c) => <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M12 3l7 3v6c0 4-3 7-7 9-4-2-7-5-7-9V6l7-3Z"/></svg>,
  timing: (c) => <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>,
};
function Caveats({ items = [] }) {
  if (!items.length) return null;
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 7 }}>
      {items.map((it, i) => {
        const warn = it.severity === 'warning';
        const c = warn ? PINK : T.inkSoft;
        return (
          <div key={i} style={{ display: 'flex', alignItems: 'flex-start', gap: 9, padding: '9px 12px', borderRadius: 11, background: warn ? 'rgba(160,64,48,0.07)' : T.bg, border: `0.5px solid ${warn ? 'rgba(160,64,48,0.25)' : T.hairline}` }}>
            <span style={{ color: c, flexShrink: 0, marginTop: 1 }}>{CAVEAT_ICON[it.reason](c)}</span>
            <div style={{ flex: 1 }}>
              <span style={{ fontFamily: T.serif, fontSize: 13.5, color: T.ink, lineHeight: 1.35 }}>{it.text}</span>
              <span style={{ fontSize: 8.5, letterSpacing: 1.2, fontWeight: 700, color: T.muteSoft, marginLeft: 7 }}>{it.reason.toUpperCase()}</span>
            </div>
          </div>
        );
      })}
    </div>
  );
}

// ── the structured TAKE card (verdict-led) ──────────────────────
function TakeCard({ opinion, confidence = 'high', provenance, verdict, body, caveats = [], why = [], curator }) {
  const tentative = confidence === 'low';
  return (
    <div style={{ padding: '19px 20px', background: T.cardWarm, borderRadius: 18, border: hp, boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset, 0 14px 30px -22px rgba(0,0,0,0.3)' }}>
      <Verdict opinion={opinion} confidence={confidence} provenance={provenance}/>
      <p style={{ fontFamily: T.serif, fontSize: tentative ? 19 : 22, fontWeight: 500, color: tentative ? T.inkSoft : T.ink, fontStyle: tentative ? 'italic' : 'normal', lineHeight: 1.24, letterSpacing: -0.4, margin: '14px 0 0' }}>{verdict}</p>
      {body && <p style={{ fontFamily: T.serif, fontSize: 15, color: T.inkSoft, lineHeight: 1.5, margin: '10px 0 0' }}>{body}</p>}
      {caveats.length > 0 && <div style={{ marginTop: 15 }}><Caveats items={caveats}/></div>}
      {why.length > 0 && (
        <div style={{ marginTop: 14, display: 'flex', flexWrap: 'wrap', gap: 6 }}>
          {why.map((w) => <span key={w} style={{ padding: '4px 10px', fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.goldDeep, background: T.bg, borderRadius: 999, border: hpT }}>{w}</span>)}
        </div>
      )}
      {curator && (
        <div style={{ marginTop: 15, paddingTop: 13, borderTop: hpT }}>
          <Eye>THE CURATOR’S READ</Eye>
          <p style={{ fontFamily: T.serif, fontSize: 13.5, color: T.mute, lineHeight: 1.5, margin: '6px 0 0' }}>{curator}</p>
        </div>
      )}
      {tentative && (
        <div style={{ marginTop: 15 }}>
          <span style={{ display: 'inline-flex', alignItems: 'center', gap: 7, padding: '8px 14px', borderRadius: 999, border: `0.8px solid ${SAGE}`, color: SAGE, fontSize: 12.5, fontWeight: 600 }}>
            <VesperMark s={13} c={SAGE}/> Tell Vesper one thing to sharpen this
          </span>
        </div>
      )}
    </div>
  );
}

// ── LEAD FACTS — the 2–4 decision-changing facts (verdict-led) ──
function LeadFacts({ items = [] }) {
  return (
    <div style={{ display: 'flex', flexDirection: 'column' }}>
      {items.map((it, i) => (
        <div key={i} style={{ display: 'grid', gridTemplateColumns: '102px 1fr', gap: 12, padding: '11px 0', borderTop: i ? hpT : 'none', alignItems: 'baseline' }}>
          <span style={{ fontSize: 9.5, letterSpacing: 1.3, fontWeight: 700, color: T.mute, paddingTop: 2 }}>{it.label}</span>
          <span style={{ fontFamily: T.serif, fontSize: 14.5, color: it.accent || T.ink, lineHeight: 1.4 }}>{it.value}</span>
        </div>
      ))}
    </div>
  );
}

// ── DATA-DRIVEN action rail — renders suggested_actions ─────────
const ACT = {
  add_to_plan:      { label: 'Add to plan', primary: true, icon: <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round"><path d="M12 5v14M5 12h14"/></svg> },
  ask_concierge:    { label: 'Ask', primary: true, gold: true },
  book:             { label: 'Book', icon: <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><rect x="4" y="5" width="16" height="16" rx="2"/><path d="M4 9h16M8 3v4M16 3v4"/></svg> },
  save:             { label: 'Save', icon: <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M6 4h12v16l-6-4-6 4V4Z"/></svg> },
  share_with_group: { label: 'Share', icon: <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><circle cx="6" cy="12" r="2.4"/><circle cx="17" cy="6" r="2.4"/><circle cx="17" cy="18" r="2.4"/><path d="M8.1 10.9l6.8-3.8M8.1 13.1l6.8 3.8"/></svg> },
  hear:             { label: 'Hear', icon: <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M3 10v4h4l5 4V6L7 10H3Z"/><path d="M16 9a4 4 0 0 1 0 6"/></svg> },
  find_similar:     { label: 'Similar', icon: <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><circle cx="7" cy="7" r="3.4"/><circle cx="17" cy="17" r="3.4"/><path d="M7 10.5v3M17 10.5v3"/></svg> },
};
function DataRail({ actions = ['add_to_plan', 'ask_concierge', 'save', 'hear', 'find_similar'] }) {
  const primaries = actions.filter((a) => ACT[a] && ACT[a].primary);
  const rest = actions.filter((a) => ACT[a] && !ACT[a].primary);
  return (
    <div style={{ position: 'absolute', left: 14, right: 14, bottom: 16, zIndex: 25 }}>
      {primaries.length > 0 && (
        <div style={{ display: 'flex', gap: 8, marginBottom: 9 }}>
          {primaries.map((a) => {
            const it = ACT[a];
            return it.gold
              ? <button key={a} style={{ width: 124, border: `0.8px solid ${T.gold}`, display: 'inline-flex', alignItems: 'center', justifyContent: 'center', gap: 7, padding: '14px 0', background: 'rgba(176,133,58,0.10)', color: T.goldDeep, borderRadius: 16, fontFamily: T.sans, fontSize: 14, fontWeight: 600 }}><VesperMark s={15}/> {it.label}</button>
              : <button key={a} style={{ flex: 1, border: 'none', display: 'inline-flex', alignItems: 'center', justifyContent: 'center', gap: 8, padding: '14px 0', background: INKBLUE, color: '#fff', borderRadius: 16, fontFamily: T.sans, fontSize: 14.5, fontWeight: 600, letterSpacing: -0.1, boxShadow: '0 10px 24px -12px rgba(61,80,102,0.7)' }}>{it.icon} {it.label}</button>;
          })}
        </div>
      )}
      {rest.length > 0 && (
        <div style={{ display: 'flex', alignItems: 'stretch', gap: 6, padding: 6, background: 'rgba(247,242,231,0.9)', backdropFilter: 'blur(18px)', borderRadius: 18, border: '0.5px solid rgba(0,0,0,0.06)', boxShadow: '0 8px 24px -10px rgba(0,0,0,0.16)' }}>
          {rest.map((a) => (
            <div key={a} style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 4, padding: '7px 0', color: T.inkSoft }}>
              {ACT[a].icon}
              <span style={{ fontSize: 9.5, fontWeight: 600, color: T.mute }}>{ACT[a].label}</span>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

// small chips (is_primary / visibility, etc)
function MiniChip({ children, tint = T.mute }) {
  return <span style={{ display: 'inline-flex', alignItems: 'center', gap: 5, padding: '3px 9px', borderRadius: 999, border: `0.5px solid ${T.hairline}`, fontSize: 10, fontWeight: 600, letterSpacing: 0.3, color: tint, background: T.bg }}>{children}</span>;
}

Object.assign(window, { OPIN, Verdict, Caveats, TakeCard, LeadFacts, DataRail, MiniChip });
