// ═══════════════════════════════════════════════════════════════
// LIVE HOME · 3 organizing systems (same content, midday). Flex
// columns so the bottom zone anchors above the floating nav and the
// content brackets the screen (no stranded void). Costs dropped from
// the standing facets. Reuses DR, ed, EdKick, StyleRiso, FT_ICON,
// SPARK, PFrame, TabBar.
// ═══════════════════════════════════════════════════════════════

const ABC_NAV = <TabBar active="trips"/>;
const vesperLine = 'No rush — they won’t turn the table; Graça’s light isn’t worth it till five.';
const NAV_CLEAR = 92; // clearance above the floating nav pill

function MiniHead({ h = 122, big = 25 }) {
  return (
    <div style={{ position: 'relative', height: h, flexShrink: 0 }}>
      <StyleRiso w={393} h={h}/>
      <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.4), rgba(20,14,9,0.05) 45%, rgba(20,14,9,0.7))' }}/>
      <div style={{ position: 'absolute', top: 44, left: 20, right: 20, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.92)" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
        <span style={{ fontFamily: DR.mono, fontSize: 8.5, letterSpacing: 2, color: 'rgba(255,255,255,0.85)', fontWeight: 600 }}>DAY 3 · TUE · 1:20</span>
        <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.92)" strokeWidth="1.6" strokeLinecap="round"><circle cx="5" cy="12" r="1.4"/><circle cx="12" cy="12" r="1.4"/><circle cx="19" cy="12" r="1.4"/></svg>
      </div>
      <div style={{ position: 'absolute', left: 22, bottom: 13 }}><h1 style={{ fontFamily: DR.serif, fontSize: big, fontWeight: 500, color: '#fff', margin: 0, letterSpacing: -0.6 }}>Lisbon, <span style={{ fontStyle: 'italic' }}>slowly</span></h1></div>
    </div>
  );
}

// ── A · ONE HERO + ONE LIST ─────────────────────────────────────
function RowA({ t, title, tom }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '52px 1fr 16px', columnGap: 12, alignItems: 'baseline', padding: '15px 0', borderTop: `0.5px solid ${DR.hairThin}` }}>
      <span style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 0.4, color: DR.faint, fontWeight: 600 }}>{t}</span>
      <span style={{ fontFamily: DR.serif, fontSize: 16.5, color: DR.ink, fontStyle: tom ? 'italic' : 'normal', letterSpacing: -0.2 }}>{title}</span>
      <span style={{ color: DR.faint, fontSize: 13, alignSelf: 'center' }}>{tom ? '→' : ''}</span>
    </div>
  );
}
function LiveA() {
  return (
    <PFrame h={852} bare>
      <div style={{ height: 852, display: 'flex', flexDirection: 'column' }}>
        <MiniHead/>
        <div style={{ flex: 1, display: 'flex', flexDirection: 'column', padding: '28px 24px 0' }}>
          <div style={{ flex: 1, display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
          <div style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 1.8, color: DR.goldDeep, fontWeight: 700 }}>NOW · 1:20</div>
          <h2 style={{ fontFamily: DR.serif, fontSize: 33, fontWeight: 500, color: DR.ink, letterSpacing: -0.6, lineHeight: 1.04, margin: '8px 0 0' }}>Lunch at Ramiro</h2>
          <div style={{ display: 'flex', alignItems: 'flex-start', gap: 7, marginTop: 12 }}>{SPARK}<span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 15, color: DR.soft, lineHeight: 1.45 }}>{vesperLine}</span></div>
          <div style={{ marginTop: 34 }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', paddingBottom: 4 }}><EdKick>The rest of the day</EdKick><EdKick c={DR.faint}>earlier · 2 ↑</EdKick></div>
            <RowA t="16.30" title="Graça, for the light"/>
            <RowA t="20.00" title="Dinner near Alecrim"/>
            <RowA t="TOM" title="Bélem, early" tom/>
          </div>
          </div>
          <div style={{ paddingTop: 16, paddingBottom: NAV_CLEAR, borderTop: ed.rule, display: 'flex', gap: 18 }}>
            {[['Stay', 'Alecrim'], ['Transport', '4:50'], ['Map', '3 cities']].map(([k, v]) => (
              <span key={k} style={{ fontFamily: DR.serif, fontSize: 12.5, color: DR.mute }}><span style={{ fontFamily: DR.mono, fontSize: 8, letterSpacing: 1, fontWeight: 700, color: DR.faint }}>{k.toUpperCase()} </span>{v}</span>
            ))}
          </div>
        </div>
      </div>
      {ABC_NAV}
    </PFrame>
  );
}

// ── B · EDITORIAL COLUMN (rows spread to fill, airy leading) ─────
function RowB({ t, title, now, done, tom }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '50px 1fr', columnGap: 14, alignItems: 'baseline' }}>
      <span style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 0.4, color: now ? DR.goldDeep : DR.faint, fontWeight: now ? 700 : 600, paddingTop: now ? 4 : 0 }}>{now ? '1:20' : t}</span>
      <div>
        <div style={{ display: 'flex', alignItems: 'baseline', gap: 8 }}>
          <span style={{ fontFamily: DR.serif, fontSize: now ? 23 : 16.5, fontWeight: now ? 600 : 400, color: done ? DR.faint : DR.ink, fontStyle: tom ? 'italic' : 'normal', letterSpacing: -0.3, lineHeight: 1.12, textDecoration: done ? 'line-through' : 'none', textDecorationColor: DR.faint }}>{title}</span>
          {done && <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="#3D7050" strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round" style={{ opacity: 0.65 }}><path d="M4 12l5 5L20 6"/></svg>}
        </div>
        {now && <div style={{ display: 'flex', alignItems: 'flex-start', gap: 7, marginTop: 8 }}>{SPARK}<span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14, color: DR.soft, lineHeight: 1.4 }}>{vesperLine}</span></div>}
      </div>
    </div>
  );
}
function LiveB() {
  return (
    <PFrame h={852} bare>
      <div style={{ height: 852, display: 'flex', flexDirection: 'column' }}>
        <div style={{ flexShrink: 0, padding: '32px 26px 0', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={DR.soft} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
          <span style={{ fontFamily: DR.mono, fontSize: 8.5, letterSpacing: 2, color: DR.mute, fontWeight: 600 }}>DAY 3 · TUE · 1:20</span>
          <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={DR.soft} strokeWidth="1.6" strokeLinecap="round"><circle cx="5" cy="12" r="1.4"/><circle cx="12" cy="12" r="1.4"/><circle cx="19" cy="12" r="1.4"/></svg>
        </div>
        <div style={{ flexShrink: 0, padding: '18px 26px 0', display: 'flex', alignItems: 'center', gap: 13 }}>
          <div style={{ width: 46, height: 46, borderRadius: 10, overflow: 'hidden', flexShrink: 0 }}><StyleRiso w={46} h={46}/></div>
          <div>
            <h1 style={{ fontFamily: DR.serif, fontSize: 27, fontWeight: 500, color: DR.ink, margin: 0, letterSpacing: -0.7, lineHeight: 1 }}>Lisbon, <span style={{ fontStyle: 'italic' }}>slowly</span></h1>
            <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13.5, color: DR.mute, marginTop: 2 }}>A slow Tuesday — the best light’s still to come.</div>
          </div>
        </div>
        <div style={{ flex: 1, display: 'flex', flexDirection: 'column', padding: '22px 26px 0' }}>
          <div style={{ paddingBottom: 8, borderBottom: ed.rule }}><EdKick c={DR.faint}>earlier today · 2 done ↑</EdKick></div>
          <div style={{ flex: 1, display: 'flex', flexDirection: 'column', justifyContent: 'space-evenly', paddingTop: 12, paddingBottom: 12 }}>
            <RowB t="12.00" title="Tiles at the museum" done/>
            <RowB now title="Lunch at Ramiro"/>
            <RowB t="16.30" title="Graça, for the light"/>
            <RowB t="20.00" title="Dinner near Alecrim"/>
            <RowB t="TOM" title="Bélem, early" tom/>
          </div>
          <div style={{ paddingTop: 13, paddingBottom: NAV_CLEAR, borderTop: ed.rule }}>
            <EdKick>Stay · Casa do Alecrim&nbsp;&nbsp;·&nbsp;&nbsp;Transport · 4:50&nbsp;&nbsp;·&nbsp;&nbsp;Map</EdKick>
          </div>
        </div>
      </div>
      {ABC_NAV}
    </PFrame>
  );
}

// ── C · SECTIONED (sections distributed, logistics anchored) ─────
function SectionLabelC({ children }) {
  return <div style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 2, color: DR.mute, fontWeight: 700, marginBottom: 12 }}>{children}</div>;
}
function LiveC() {
  return (
    <PFrame h={852} bare>
      <div style={{ height: 852, display: 'flex', flexDirection: 'column' }}>
        <MiniHead h={150} big={27}/>
        <div style={{ flex: 1, display: 'flex', flexDirection: 'column', justifyContent: 'space-between', padding: '24px 24px 0' }}>
          <div>
            <SectionLabelC>NOW</SectionLabelC>
            <h2 style={{ fontFamily: DR.serif, fontSize: 25, fontWeight: 500, color: DR.ink, letterSpacing: -0.5, margin: 0, lineHeight: 1.05 }}>Lunch at Ramiro <span style={{ fontFamily: DR.mono, fontSize: 10, fontWeight: 600, color: DR.faint, letterSpacing: 0.5 }}>· 1:20</span></h2>
            <div style={{ display: 'flex', alignItems: 'flex-start', gap: 7, marginTop: 9 }}>{SPARK}<span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14, color: DR.soft, lineHeight: 1.4 }}>{vesperLine}</span></div>
          </div>
          <div style={{ paddingTop: 20, borderTop: ed.rule }}>
            <SectionLabelC>THE DAY · WHAT’S LEFT</SectionLabelC>
            {[['16.30', 'Graça, for the light'], ['20.00', 'Dinner near Alecrim'], ['TOM', 'Bélem, early']].map(([t, ti], i) => (
              <div key={i} style={{ display: 'grid', gridTemplateColumns: '52px 1fr', columnGap: 14, alignItems: 'baseline', padding: '10px 0' }}>
                <span style={{ fontFamily: DR.mono, fontSize: 9, color: DR.faint, fontWeight: 600 }}>{t}</span>
                <span style={{ fontFamily: DR.serif, fontSize: 16, color: t === 'TOM' ? DR.mute : DR.ink, fontStyle: t === 'TOM' ? 'italic' : 'normal', letterSpacing: -0.2 }}>{ti}</span>
              </div>
            ))}
          </div>
          <div style={{ paddingTop: 20, paddingBottom: NAV_CLEAR, borderTop: ed.rule }}>
            <SectionLabelC>LOGISTICS</SectionLabelC>
            <div style={{ display: 'flex', gap: 8 }}>
              {[[FT_ICON.stay, 'Casa do Alecrim', 'STAY'], [FT_ICON.transport, 'Tram 28 · 4:50', 'NEXT'], [FT_ICON.route, '3 cities', 'MAP']].map(([ic, v, l], i) => (
                <div key={i} style={{ flex: 1, padding: '12px 10px', background: DR.card, borderRadius: 12, border: `0.5px solid ${DR.hair}` }}>
                  <span style={{ color: DR.soft, display: 'flex' }}>{ic}</span>
                  <div style={{ fontFamily: DR.serif, fontSize: 13.5, color: DR.ink, fontWeight: 500, letterSpacing: -0.2, marginTop: 8, lineHeight: 1.1 }}>{v}</div>
                  <div style={{ fontFamily: DR.mono, fontSize: 7, letterSpacing: 1, color: DR.mute, fontWeight: 700, marginTop: 3 }}>{l}</div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
      {ABC_NAV}
    </PFrame>
  );
}

Object.assign(window, { LiveA, LiveB, LiveC });
