// ═══════════════════════════════════════════════════════════════
// FOLIO · CONSOLIDATED BODY — the holistic redesign.
// Cover (chat + bell + trip-info) · Vesper block (voice+action+progress,
// routes) · 2x2 facet tiles (Transportation/Stay/Costs/Route, each w/
// status — replaces the old strip) · intelligence slice (Vesper's
// phase-aware cut, NOT the full itinerary). Two treatments of facets+slice.
// Reuses DR + Filmstrip/Ppl/CASTD + StyleRiso.
// ═══════════════════════════════════════════════════════════════

const CICO = {
  back: <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="#fff" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>,
  chat: <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fff" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M4 5h16v11H8l-4 4z"/></svg>,
  bell: <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fff" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M6 9a6 6 0 0 1 12 0v4l1.5 3h-15L6 13z"/><path d="M10 19a2 2 0 0 0 4 0"/></svg>,
  info: <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fff" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="9" r="3"/><path d="M5 20c0-3.5 3-5.5 7-5.5s7 2 7 5.5"/></svg>,
};
function CIcon({ children, dot }) {
  return <div style={{ position: 'relative', width: 34, height: 34, borderRadius: 999, background: 'rgba(255,255,255,0.2)', backdropFilter: 'blur(8px)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>{children}{dot && <span style={{ position: 'absolute', top: 3, right: 3, width: 7, height: 7, borderRadius: 7, background: DR.gold, border: '1.5px solid rgba(20,14,9,0.5)', boxSizing: 'content-box' }}/>}</div>;
}

// Cover — shared.
function FCover() {
  return (
    <div style={{ position: 'relative', height: 220, marginTop: -40 }}>
      <div style={{ position: 'absolute', inset: 0 }}><StyleRiso w={393} h={220}/></div>
      <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.42) 0%, rgba(20,14,9,0) 30%, rgba(20,14,9,0) 46%, rgba(20,14,9,0.72) 100%)' }}/>
      <div style={{ position: 'absolute', top: 46, left: 16, right: 16, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <CIcon>{CICO.back}</CIcon>
        <div style={{ display: 'flex', gap: 8 }}><CIcon dot>{CICO.chat}</CIcon><CIcon dot>{CICO.bell}</CIcon><CIcon>{CICO.info}</CIcon></div>
      </div>
      <div style={{ position: 'absolute', top: 92, left: 18 }}><Filmstrip truth={1} onDark/></div>
      <div style={{ position: 'absolute', left: 20, right: 20, bottom: 16 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 7 }}>
          <span style={{ padding: '3px 9px', borderRadius: 999, background: 'rgba(255,255,255,0.2)', backdropFilter: 'blur(6px)', fontSize: 9, letterSpacing: 1.4, fontWeight: 700, color: '#fff' }}>IN 23 DAYS</span>
          <Ppl who={CASTD} size={22} onDark/>
        </div>
        <h1 style={{ fontFamily: DR.serif, fontSize: 34, fontWeight: 500, letterSpacing: -1, lineHeight: 0.98, color: '#fff', margin: 0 }}>Lisbon, <span style={{ fontStyle: 'italic' }}>slowly</span></h1>
      </div>
    </div>
  );
}

// Vesper block — V3 "object peek" treatment: shows the shortlist, routes. No big button.
// Vesper block — quiet ledger: ochre rule, prose, text actions. Subtle.
function VBlock() {
  return (
    <div style={{ padding: '16px 22px 0' }}>
      <div style={{ paddingLeft: 14, borderLeft: `2px solid ${DR.gold}` }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 7 }}>
          <svg width="12" height="12" viewBox="0 0 24 24" fill={DR.gold}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>
          <span style={{ fontSize: 9, letterSpacing: 1.6, fontWeight: 700, color: DR.goldDeep }}>VESPER · 1 OF 4 LEFT</span>
        </div>
        <p style={{ fontFamily: DR.serif, fontSize: 16.5, color: DR.ink, lineHeight: 1.38, margin: 0, letterSpacing: -0.12, fontStyle: 'italic' }}>
          Where you sleep nights 5–7 is the last gap — <span style={{ fontStyle: 'normal' }}>Casa do Alecrim</span> is the one I’d hold.
        </p>
        <div style={{ display: 'flex', gap: 16, marginTop: 11 }}>
          <span style={{ fontSize: 13, fontWeight: 600, color: DR.blue, letterSpacing: -0.1 }}>Hold it →</span>
          <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13, color: DR.mute }}>see other two</span>
        </div>
      </div>
    </div>
  );
}

// Facet tile — icon + name + status. `flag` tints the status (needs attn).
function Facet({ g, name, status, flag }) {
  return (
    <div style={{ background: DR.card, borderRadius: 13, border: `0.5px solid ${flag ? 'rgba(176,133,58,0.45)' : DR.hair}`, padding: '13px 14px', boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset' }}>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <div style={{ color: DR.soft }}>{g}</div>
        {flag && <span style={{ width: 6, height: 6, borderRadius: 6, background: DR.gold }}/>}
      </div>
      <div style={{ fontFamily: DR.serif, fontSize: 15, fontWeight: 500, color: DR.ink, letterSpacing: -0.2, marginTop: 9 }}>{name}</div>
      <div style={{ fontFamily: DR.mono, fontSize: 9, color: flag ? DR.goldDeep : DR.mute, letterSpacing: 0.5, marginTop: 4, fontWeight: 600 }}>{status}</div>
    </div>
  );
}
const FCO = {
  transport: <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><path d="M3 16l2-7a3 3 0 0 1 3-2h8a3 3 0 0 1 3 2l2 7M5 16h14M5 16v2M19 16v2"/><circle cx="7.5" cy="16" r="0.5"/><circle cx="16.5" cy="16" r="0.5"/></svg>,
  stay: <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><path d="M3 20V9l9-5 9 5v11M3 20h18M9 20v-6h6v6"/></svg>,
  costs: <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"><path d="M7 4h10M7 20h10M9 4c0 4 6 4 6 8s-6 4-6 8"/></svg>,
  route: <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><circle cx="6" cy="6" r="2.5"/><circle cx="18" cy="18" r="2.5"/><path d="M6 8.5v4a4 4 0 0 0 4 4h4"/></svg>,
};

// Compact 1x4 facet ribbon — icon + value only, no label. Short.
function FacetCell({ g, status, flag }) {
  return (
    <div style={{ flex: 1, minWidth: 0, padding: '9px 8px', background: DR.card, borderRadius: 11, border: `0.5px solid ${flag ? 'rgba(176,133,58,0.45)' : DR.hair}`, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 7, position: 'relative' }}>
      {flag && <span style={{ position: 'absolute', top: 6, right: 6, width: 5, height: 5, borderRadius: 5, background: DR.gold }}/>}
      <div style={{ color: flag ? DR.goldDeep : DR.soft, flexShrink: 0 }}>{g}</div>
      <div style={{ fontFamily: DR.serif, fontSize: 13, color: flag ? DR.goldDeep : DR.ink, fontWeight: 500, letterSpacing: -0.1, lineHeight: 1 }}>{status}</div>
    </div>
  );
}
function Facets() {
  return (
    <div style={{ padding: '14px 18px 0', display: 'flex', gap: 7 }}>
      <FacetCell g={FCO.transport} status="Booked"/>
      <FacetCell g={FCO.stay} status="3/5" flag/>
      <FacetCell g={FCO.costs} status="€1.4k"/>
      <FacetCell g={FCO.route} status="3"/>
    </div>
  );
}

// Intelligence slice — Vesper's phase-aware cut, NOT the full spine.
// Treatment 1: a "shape so far" narrative cut (2 beats + the gap).
function Slice1() {
  return (
    <div style={{ padding: '18px 20px 0' }}>
      <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginBottom: 11 }}>
        <span style={{ fontSize: 9, letterSpacing: 2, color: DR.mute, fontWeight: 700 }}>THE SHAPE SO FAR</span>
        <span style={{ fontSize: 9, letterSpacing: 1.2, color: DR.mute, fontWeight: 600 }}>VESPER’S CUT</span>
      </div>
      <div style={{ display: 'flex', gap: 12 }}>
        <div style={{ width: 60, height: 78, borderRadius: 9, overflow: 'hidden', flexShrink: 0 }}><StyleRiso w={60} h={78}/></div>
        <div style={{ flex: 1 }}>
          <p style={{ fontFamily: DR.serif, fontSize: 15, color: DR.ink, lineHeight: 1.4, margin: 0, letterSpacing: -0.1 }}>
            Two quiet days in <span style={{ fontStyle: 'italic' }}>Alfama</span>, then Belém early before the crowd. The middle’s still open.
          </p>
          <div style={{ marginTop: 10, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
            <span style={{ fontFamily: DR.serif, fontSize: 13.5, fontWeight: 500, color: DR.ink, letterSpacing: -0.1 }}>Open the full itinerary</span>
            <span style={{ color: DR.blue, fontSize: 14 }}>→</span>
          </div>
        </div>
      </div>
    </div>
  );
}

// Treatment 2: a 3-beat mini-timeline (highlights only, not all days).
function Slice2() {
  return (
    <div style={{ padding: '18px 20px 0' }}>
      <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginBottom: 11 }}>
        <span style={{ fontSize: 9, letterSpacing: 2, color: DR.mute, fontWeight: 700 }}>WORTH KNOWING</span>
        <span style={{ fontSize: 9, letterSpacing: 1.2, color: DR.mute, fontWeight: 600 }}>3 OF 6 DAYS</span>
      </div>
      {[['SAT 18', 'Land soft, Alfama', 'set'], ['MON 20', 'still open', 'gap'], ['TUE 21', 'Belém, early', 'set']].map(([d, t, s], i) => (
        <div key={i} style={{ display: 'grid', gridTemplateColumns: '54px 1fr', gap: 12, padding: '9px 0', borderTop: i ? `0.5px solid ${DR.hairThin}` : 'none', alignItems: 'center' }}>
          <span style={{ fontFamily: DR.mono, fontSize: 9.5, color: DR.mute, letterSpacing: 0.8, fontWeight: 600 }}>{d}</span>
          <span style={{ fontFamily: DR.serif, fontSize: 14.5, fontWeight: 500, color: s === 'gap' ? DR.mute : DR.ink, fontStyle: s === 'gap' ? 'italic' : 'normal', letterSpacing: -0.2 }}>{t}</span>
        </div>
      ))}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginTop: 11, paddingTop: 11, borderTop: `0.5px solid ${DR.hairThin}` }}>
        <span style={{ fontFamily: DR.serif, fontSize: 13.5, fontWeight: 500, color: DR.ink, letterSpacing: -0.1 }}>Open the full itinerary</span>
        <span style={{ color: DR.blue, fontSize: 14 }}>→</span>
      </div>
    </div>
  );
}

function FolioFrame({ slice }) {
  return (
    <div style={{ width: 393, background: DR.paper, borderRadius: 30, overflow: 'hidden', border: `0.5px solid ${DR.hair}`, boxShadow: '0 30px 60px -30px rgba(0,0,0,0.3)', position: 'relative', paddingBottom: 16 }}>
      <div style={{ height: 40 }}/>
      <FCover/>
      <Facets/>
      <VBlock/>
      <SliceRich/>
    </div>
  );
}
// Vibe-aware Vesper line — rises from logistics → anticipation as trip settles.
function VLineHome({ vibe }) {
  // Vesper speaks about the PLACE / itinerary — never logistics (the facets own that).
  const txt = vibe
    ? 'Lisbon’s warmest the week you land — pack for long evenings outside and one slow morning in Alfama.'
    : 'Alfama rewards the slow walker — I’ve been pulling the quiet corners for your mornings there.';
  const tag = vibe ? 'WHAT TO EXPECT' : 'ON LISBON';
  const c = vibe ? '#3D7050' : DR.goldDeep;
  return (
    <div style={{ padding: '16px 22px 4px' }}>
      <div style={{ paddingLeft: 13, borderLeft: `2px solid ${vibe ? '#3D7050' : DR.gold}` }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 5 }}>
          <svg width="11" height="11" viewBox="0 0 24 24" fill={vibe ? '#3D7050' : DR.gold}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>
          <span style={{ fontSize: 8.5, letterSpacing: 1.4, color: c, fontWeight: 700 }}>VESPER · {tag}</span>
        </div>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 16, color: DR.ink, margin: 0, lineHeight: 1.4, letterSpacing: -0.12 }}>{txt}</p>
      </div>
    </div>
  );
}

// NEEDS-YOU home — Vesper logistics line + enlarged needs-you facet hero.
function FolioNeedsYou() {
  return (
    <PFrame>
      <FCover/>
      <VLineHome/>
      <div style={{ padding: '14px 18px 0' }}><FacetsHero bare/></div>
      <SliceRich/>
    </PFrame>
  );
}
// ALL-CLEAR home — vibey Vesper line + map-hero facet block.
function FolioAllClear() {
  return (
    <PFrame>
      <FCover/>
      <VLineHome vibe/>
      <div style={{ padding: '14px 18px 0' }}><FacetsAllClear bare/></div>
      <SliceRich/>
    </PFrame>
  );
}
function FolioBodyA() { return <FolioNeedsYou/>; }
function FolioBodyB() { return <FolioAllClear/>; }

Object.assign(window, { FolioBodyA, FolioBodyB, FolioNeedsYou, FolioAllClear, VLineHome });
