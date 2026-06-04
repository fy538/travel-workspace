// ═══════════════════════════════════════════════════════════════
// FACET LAYOUT COMPARISON — 5 versions of the consolidated body,
// varying only the facet treatment + placement. Self-contained
// (rebuilds cover + ledger Vesper block locally); reuses SliceRich.
// Reuses DR + StyleRiso + Ppl/CASTD + SliceRich.
// ═══════════════════════════════════════════════════════════════

const fk = (s = 13, c = DR.gold) => <svg width={s} height={s} viewBox="0 0 24 24" fill={c}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>;
const FI = {
  transport: <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><path d="M3 16l2-7a3 3 0 0 1 3-2h8a3 3 0 0 1 3 2l2 7M5 16h14M5 16v2M19 16v2"/></svg>,
  stay: <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><path d="M3 20V9l9-5 9 5v11M3 20h18M9 20v-6h6v6"/></svg>,
  costs: <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"><path d="M7 4h10M7 20h10M9 4c0 4 6 4 6 8s-6 4-6 8"/></svg>,
  route: <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><circle cx="6" cy="6" r="2.5"/><circle cx="18" cy="18" r="2.5"/><path d="M6 8.5v4a4 4 0 0 0 4 4h4"/></svg>,
};
const FDATA = [['transport', 'TRANSPORT', 'Booked', false], ['stay', 'STAY', '3 / 5 nights', true], ['costs', 'COSTS', '€1.4k · split 3', false], ['route', 'ROUTE', '3 cities', false]];

// shared cover
function FXCover() {
  return (
    <div style={{ position: 'relative', height: 196, marginTop: -40 }}>
      <div style={{ position: 'absolute', inset: 0 }}><StyleRiso w={393} h={196}/></div>
      <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.4) 0%, rgba(20,14,9,0) 32%, rgba(20,14,9,0) 48%, rgba(20,14,9,0.72) 100%)' }}/>
      <div style={{ position: 'absolute', top: 46, left: 16, right: 16, display: 'flex', justifyContent: 'space-between' }}>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#fff" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
        <Ppl who={CASTD} size={21} onDark/>
      </div>
      <div style={{ position: 'absolute', left: 20, right: 20, bottom: 14 }}>
        <span style={{ fontFamily: DR.mono, fontSize: 9, color: 'rgba(255,255,255,0.85)', letterSpacing: 1.4 }}>IN 23 DAYS · MAY 18–24</span>
        <h1 style={{ fontFamily: DR.serif, fontSize: 32, fontWeight: 500, letterSpacing: -1, lineHeight: 0.98, color: '#fff', margin: '3px 0 0' }}>Lisbon, <span style={{ fontStyle: 'italic' }}>slowly</span></h1>
      </div>
    </div>
  );
}
// shared ledger Vesper block
function FXVesper() {
  return (
    <div style={{ padding: '15px 22px 0' }}>
      <div style={{ paddingLeft: 14, borderLeft: `2px solid ${DR.gold}` }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 6 }}>{fk(12)}<span style={{ fontSize: 9, letterSpacing: 1.6, fontWeight: 700, color: DR.goldDeep }}>VESPER · 1 OF 4 LEFT</span></div>
        <p style={{ fontFamily: DR.serif, fontSize: 16, color: DR.ink, lineHeight: 1.36, margin: 0, letterSpacing: -0.12, fontStyle: 'italic' }}>Where you sleep nights 5–7 is the last gap — <span style={{ fontStyle: 'normal' }}>Casa do Alecrim</span> is the one I’d hold.</p>
        <div style={{ display: 'flex', gap: 16, marginTop: 10 }}><span style={{ fontSize: 12.5, fontWeight: 600, color: DR.blue }}>Hold it →</span><span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 12.5, color: DR.mute }}>see other two</span></div>
      </div>
    </div>
  );
}

// facet cell — compact (icon+value) or tall (icon+label+value)
function FXCell({ icon, label, value, flag, tall, two }) {
  if (!tall) return (
    <div style={{ flex: 1, minWidth: 0, padding: '9px 8px', background: DR.card, borderRadius: 11, border: `0.5px solid ${flag ? 'rgba(176,133,58,0.45)' : DR.hair}`, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 7, position: 'relative' }}>
      {flag && <span style={{ position: 'absolute', top: 6, right: 6, width: 5, height: 5, borderRadius: 5, background: DR.gold }}/>}
      <div style={{ color: flag ? DR.goldDeep : DR.soft, flexShrink: 0 }}>{icon}</div>
      <div style={{ fontFamily: DR.serif, fontSize: 13, color: flag ? DR.goldDeep : DR.ink, fontWeight: 500, letterSpacing: -0.1, lineHeight: 1 }}>{two ? value : value.split(' · ')[0]}</div>
    </div>
  );
  return (
    <div style={{ flex: two ? 'none' : 1, width: two ? 'auto' : undefined, minWidth: 0, padding: '11px 12px', background: DR.card, borderRadius: 12, border: `0.5px solid ${flag ? 'rgba(176,133,58,0.45)' : DR.hair}`, position: 'relative' }}>
      {flag && <span style={{ position: 'absolute', top: 10, right: 10, width: 5, height: 5, borderRadius: 5, background: DR.gold }}/>}
      <div style={{ color: flag ? DR.goldDeep : DR.soft }}>{icon}</div>
      <div style={{ fontSize: 7.5, letterSpacing: 1, color: DR.mute, fontWeight: 700, marginTop: 8 }}>{label}</div>
      <div style={{ fontFamily: DR.serif, fontSize: 13, color: flag ? DR.goldDeep : DR.ink, fontWeight: 500, letterSpacing: -0.1, marginTop: 3 }}>{value}</div>
    </div>
  );
}
function FacetRow1x4({ tall }) {
  return <div style={{ padding: '14px 18px 0', display: 'flex', gap: 7 }}>{FDATA.map(([k, l, v, f]) => <FXCell key={k} icon={FI[k]} label={l} value={tall ? v : v} flag={f} tall={tall}/>)}</div>;
}
function FacetGrid2x2() {
  return <div style={{ padding: '14px 18px 0', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8 }}>{FDATA.map(([k, l, v, f]) => <FXCell key={k} icon={FI[k]} label={l} value={v} flag={f} tall two/>)}</div>;
}

function Frame({ children }) {
  return <div style={{ width: 393, background: DR.paper, borderRadius: 30, overflow: 'hidden', border: `0.5px solid ${DR.hair}`, boxShadow: '0 24px 50px -28px rgba(0,0,0,0.3)', position: 'relative', paddingBottom: 16 }}><div style={{ height: 40 }}/>{children}</div>;
}

// V1 · current — compact 1x4 above Vesper, no label
function FV1() { return <Frame><FXCover/><FacetRow1x4/><FXVesper/><SliceRich/></Frame>; }
// V2 · tall 1x4 with title, above Vesper
function FV2() { return <Frame><FXCover/><FacetRow1x4 tall/><FXVesper/><SliceRich/></Frame>; }
// V3 · 2x2 with title, above Vesper
function FV3() { return <Frame><FXCover/><FacetGrid2x2/><FXVesper/><SliceRich/></Frame>; }
// V4 · 1x4 (tall, title) at the bottom, below the itinerary
function FV4() { return <Frame><FXCover/><FXVesper/><SliceRich/><FacetRow1x4 tall/><div style={{ height: 6 }}/></Frame>; }
// V5 · 2x2 at the bottom, below the itinerary
function FV5() { return <Frame><FXCover/><FXVesper/><SliceRich/><FacetGrid2x2/><div style={{ height: 6 }}/></Frame>; }

Object.assign(window, { FV1, FV2, FV3, FV4, FV5 });
