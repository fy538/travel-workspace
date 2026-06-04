// ═══════════════════════════════════════════════════════════════
// TRIP-HOME FACET TILES · rethought. Each tile = glanceable readiness
// (not a dumb stat) + doorway into its surface. 3 task facets carry a
// needs-you/set state; Route is lens-shaped (just "open the map").
// Reuses DR. Shown as standalone tile blocks (drop into the home body).
// ═══════════════════════════════════════════════════════════════

const FT_ICON = {
  stay: <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><path d="M3 20V9l9-5 9 5v11M3 20h18M9 20v-6h6v6"/></svg>,
  transport: <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><path d="M2 12l20-7-7 20-3-9-10-4z"/></svg>,
  costs: <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"><path d="M7 4h10M7 20h10M9 4c0 4 6 4 6 8s-6 4-6 8"/></svg>,
  route: <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><path d="M9 4 L3 6.5 V20 L9 17.5 L15 20 L21 17.5 V4 L15 6.5 L9 4Z"/><path d="M9 4v13.5M15 6.5V20"/></svg>,
};
// the four facets' live intelligence (needs = ochre flag; set = calm)
const FT = {
  stay:      { k: 'STAY',      head: 'Nights 5–7 open', sub: 'still to book', needs: true },
  transport: { k: 'TRANSPORT', head: 'Mara not booked', sub: '2 of 3 sorted', needs: true },
  costs:     { k: 'COSTS',     head: 'You’re owed €347', sub: 'not settled', needs: false },
  route:     { k: 'ROUTE',     head: '3 cities', sub: 'your map', lens: true },
};
function FShell({ children, bare }) {
  // bare = no card chrome (used inside the trip home, where it's not a floating card)
  if (bare) return <div style={{ width: '100%' }}>{children}</div>;
  return <div style={{ width: 393, background: 'transparent', padding: '4px 0' }}>
    {children}
  </div>;
}
const ftk = (s = 10, c = DR.gold) => <svg width={s} height={s} viewBox="0 0 24 24" fill={c}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>;

// ─── A · STATUS TILES (2×2) — each carries its readiness ───
function FacetsStatus() {
  const cell = (key) => {
    const f = FT[key];
    return (
      <div style={{ flex: 1, minWidth: 0, padding: '13px 13px', background: DR.card, borderRadius: 14, border: `0.5px solid ${f.needs ? 'rgba(176,133,58,0.45)' : DR.hair}`, position: 'relative' }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 9 }}>
          <span style={{ color: f.needs ? DR.goldDeep : DR.soft }}>{FT_ICON[key]}</span>
          {f.needs ? <span style={{ width: 6, height: 6, borderRadius: 6, background: DR.gold }}/> : f.lens ? <span style={{ fontSize: 11, color: DR.faint }}>›</span> : <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#3D7050" strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round"><path d="M4 12l5 5L20 6"/></svg>}
        </div>
        <div style={{ fontSize: 7.5, letterSpacing: 1.2, color: DR.mute, fontWeight: 700 }}>{f.k}</div>
        <div style={{ fontFamily: DR.serif, fontSize: 15, fontWeight: 500, color: DR.ink, letterSpacing: -0.2, lineHeight: 1.1, marginTop: 4 }}>{f.head}</div>
        <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 10.5, color: f.needs ? DR.goldDeep : DR.mute, marginTop: 2 }}>{f.sub}</div>
      </div>
    );
  };
  return <FShell><div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
    <div style={{ display: 'flex', gap: 8 }}>{cell('stay')}{cell('transport')}</div>
    <div style={{ display: 'flex', gap: 8 }}>{cell('costs')}{cell('route')}</div>
  </div></FShell>;
}

// ─── B · NEEDS-YOU LIST + ROUTE MAP — tasks as rows, route as a map thumb ───
function FacetsList() {
  const row = (key) => {
    const f = FT[key];
    return (
      <div style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '12px 0', borderTop: `0.5px solid ${DR.hairThin}` }}>
        <span style={{ color: f.needs ? DR.goldDeep : DR.soft, width: 18, display: 'flex' }}>{FT_ICON[key]}</span>
        <div style={{ flex: 1 }}>
          <div style={{ fontFamily: DR.serif, fontSize: 15, fontWeight: 500, color: DR.ink, letterSpacing: -0.2 }}>{f.head}</div>
          <div style={{ fontSize: 8, letterSpacing: 1.2, color: DR.mute, fontWeight: 700, marginTop: 2 }}>{f.k} · {f.sub.toUpperCase()}</div>
        </div>
        {f.needs ? <span style={{ display: 'inline-flex', alignItems: 'center', gap: 5, fontSize: 11, color: DR.goldDeep, fontWeight: 600 }}>{ftk(10)} fix</span> : <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#3D7050" strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round"><path d="M4 12l5 5L20 6"/></svg>}
      </div>
    );
  };
  return <FShell>
    {row('stay')}{row('transport')}{row('costs')}
    {/* route as a little map strip */}
    <div style={{ marginTop: 12, height: 84, borderRadius: 13, overflow: 'hidden', position: 'relative', border: `0.5px solid ${DR.hair}` }}>
      <svg width="100%" height="100%" viewBox="0 0 357 84" preserveAspectRatio="xMidYMid slice"><rect width="357" height="84" fill="#E7DCC6"/><path d="M0 60 Q120 40 240 64 T357 56 L357 84 L0 84Z" fill="#9DB0AC" opacity="0.55"/><path d="M50 60 Q120 30 200 40 Q280 50 320 24" stroke={DR.gold} strokeWidth="1.5" strokeDasharray="2 4" fill="none"/><circle cx="50" cy="60" r="4" fill={DR.blue}/><circle cx="200" cy="40" r="3.5" fill={DR.ink}/><circle cx="320" cy="24" r="3.5" fill={DR.ink}/></svg>
      <div style={{ position: 'absolute', left: 12, bottom: 9, display: 'flex', alignItems: 'center', gap: 7 }}><span style={{ color: '#fff' }}>{FT_ICON.route}</span><span style={{ fontFamily: DR.serif, fontSize: 14, fontWeight: 500, color: '#fff', letterSpacing: -0.2 }}>Your map · 3 cities</span></div>
    </div>
  </FShell>;
}

// ─── C · ONE HERO + QUIET REST — enlarged needs-you hero ───
function FacetsHero({ bare }) {
  return <FShell bare={bare}>
    {/* hero: the single most-needs-you facet, enlarged */}
    <div style={{ padding: '17px 17px', background: DR.card, borderRadius: 16, border: `0.8px solid rgba(176,133,58,0.45)`, marginBottom: 8, boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset' }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 10 }}>{ftk(12)}<span style={{ fontSize: 9, letterSpacing: 1.4, color: DR.goldDeep, fontWeight: 700 }}>NEEDS YOU · STAY</span></div>
      <div style={{ fontFamily: DR.serif, fontSize: 22, fontWeight: 500, color: DR.ink, letterSpacing: -0.4, lineHeight: 1.08 }}>Nights 5–7 are still open</div>
      <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13, color: DR.mute, marginTop: 5 }}>Casa do Alecrim is the one I’d hold — free to cancel for a week.</div>
      <div style={{ marginTop: 14, display: 'flex', alignItems: 'center', gap: 8 }}><span style={{ padding: '9px 16px', background: DR.blue, color: '#fff', borderRadius: 999, fontSize: 12.5, fontWeight: 600 }}>Hold it</span><span style={{ padding: '9px 14px', background: DR.cardSoft, border: `0.5px solid ${DR.hair}`, borderRadius: 999, fontFamily: DR.serif, fontStyle: 'italic', fontSize: 12.5, color: DR.soft }}>see options</span></div>
    </div>
    {/* quiet rest */}
    <div style={{ display: 'flex', gap: 8 }}>
      {[['transport', 'Transport', '2 of 3', true], ['costs', 'Costs', 'owed €347', true], ['route', 'Route', '3 cities', false]].map(([key, label, val, needs]) => (
        <div key={key} style={{ flex: 1, padding: '11px 10px', background: DR.card, borderRadius: 12, border: `0.5px solid ${DR.hair}`, textAlign: 'center' }}>
          <div style={{ display: 'flex', justifyContent: 'center', color: DR.soft, marginBottom: 6, position: 'relative' }}>{FT_ICON[key]}{needs && <span style={{ position: 'absolute', top: -2, right: '50%', marginRight: -14, width: 5, height: 5, borderRadius: 5, background: DR.gold }}/>}</div>
          <div style={{ fontFamily: DR.serif, fontSize: 13, fontWeight: 500, color: DR.ink, letterSpacing: -0.1, lineHeight: 1 }}>{val}</div>
          <div style={{ fontSize: 7, letterSpacing: 1, color: DR.mute, fontWeight: 700, marginTop: 4 }}>{label.toUpperCase()}</div>
        </div>
      ))}
    </div>
  </FShell>;
}

// ─── C′ · ALL CLEAR — nothing needs you, so the MAP becomes the hero ───
function FacetsAllClear({ bare }) {
  return <FShell bare={bare}>
    {/* map hero */}
    <div style={{ height: 150, borderRadius: 16, overflow: 'hidden', position: 'relative', border: `0.5px solid ${DR.hair}`, marginBottom: 8 }}>
      <svg width="100%" height="100%" viewBox="0 0 357 150" preserveAspectRatio="xMidYMid slice"><rect width="357" height="150" fill="#E7DCC6"/><path d="M0 110 Q120 88 240 116 T357 104 L357 150 L0 150Z" fill="#9DB0AC" opacity="0.55"/><ellipse cx="280" cy="50" rx="56" ry="34" fill="#B6C29A" opacity="0.5"/><path d="M50 110 Q120 60 200 70 Q280 80 320 40" stroke={DR.gold} strokeWidth="1.6" strokeDasharray="2 4" fill="none"/><circle cx="50" cy="110" r="4.5" fill={DR.blue}/><circle cx="200" cy="70" r="3.5" fill={DR.ink}/><circle cx="320" cy="40" r="3.5" fill={DR.ink}/><rect width="357" height="150" fill="url(#fcg)" opacity="0.5"/><defs><pattern id="fcg" width="3" height="3" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="0.4" fill="rgba(60,40,24,0.5)"/></pattern></defs></svg>
      <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to top, rgba(20,14,9,0.5), transparent 55%)' }}/>
      <div style={{ position: 'absolute', left: 14, bottom: 12, right: 14, display: 'flex', alignItems: 'flex-end', justifyContent: 'space-between' }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 4 }}><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.85)" strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round"><path d="M4 12l5 5L20 6"/></svg><span style={{ fontSize: 8.5, letterSpacing: 1.4, color: 'rgba(255,255,255,0.85)', fontWeight: 700 }}>ALL SET</span></div>
          <div style={{ fontFamily: DR.serif, fontSize: 19, fontWeight: 500, color: '#fff', letterSpacing: -0.3 }}>Your map · 3 cities</div>
        </div>
        <span style={{ color: '#fff', fontSize: 15 }}>›</span>
      </div>
    </div>
    {/* the three task facets — Route is the map hero above, so it's dropped here */}
    <div style={{ display: 'flex', gap: 8 }}>
      {[['stay', 'Stay'], ['transport', 'Transport'], ['costs', 'Costs']].map(([key, label]) => (
        <div key={key} style={{ flex: 1, padding: '10px 6px', background: DR.card, borderRadius: 11, border: `0.5px solid ${DR.hair}`, textAlign: 'center' }}>
          <div style={{ display: 'flex', justifyContent: 'center', color: DR.soft, marginBottom: 5 }}>{FT_ICON[key]}</div>
          <div style={{ display: 'flex', justifyContent: 'center' }}><svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="#3D7050" strokeWidth="2.6" strokeLinecap="round" strokeLinejoin="round"><path d="M4 12l5 5L20 6"/></svg></div>
          <div style={{ fontSize: 7, letterSpacing: 1, color: DR.mute, fontWeight: 700, marginTop: 5 }}>{label.toUpperCase()}</div>
        </div>
      ))}
    </div>
  </FShell>;
}

Object.assign(window, { FacetsStatus, FacetsList, FacetsHero, FacetsAllClear });
