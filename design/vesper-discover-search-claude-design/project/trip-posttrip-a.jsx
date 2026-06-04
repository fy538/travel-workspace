// ═══════════════════════════════════════════════════════════════
// POST-TRIP HOME · canonical (A1, scrolling keepsake). A browsable
// page, not a glanceable screen: gouache cover → Vesper look-back →
// the story as a postcard artifact → Atlas handoff right under it →
// the trip in brief (Stay · Map · Costs, no Transport; Costs holds
// the settle-up) → the moments you'll keep. Floating nav over it.
// Reuses PostCover, LookBack (trip-posttrip.jsx) + DR, StyleRiso,
// FT_ICON, ed, PFrame, TabBar.
// ═══════════════════════════════════════════════════════════════

// The story as a stamped postcard "on the desk".
function KeepsakePostcard() {
  return (
    <div style={{ position: 'relative', height: 196 }}>
      <div style={{ position: 'absolute', left: 36, right: 14, top: 16, bottom: 4, background: DR.cardSoft, borderRadius: 7, transform: 'rotate(2.6deg)', border: `0.5px solid ${DR.hair}` }}/>
      <div style={{ position: 'absolute', left: 12, right: 28, top: 2, bottom: 16, borderRadius: 7, overflow: 'hidden', transform: 'rotate(-1.8deg)', border: `0.5px solid ${DR.hair}`, boxShadow: '0 16px 28px -16px rgba(0,0,0,0.34)', background: DR.card }}>
        <div style={{ height: 122, position: 'relative' }}>
          <StyleRiso w={320} h={122}/>
          <div style={{ position: 'absolute', top: 10, right: 10, width: 36, height: 42, border: `1.5px solid ${DR.gold}`, borderRadius: 2, transform: 'rotate(6deg)', display: 'flex', alignItems: 'center', justifyContent: 'center', background: 'rgba(247,242,231,0.55)' }}>
            <span style={{ fontFamily: DR.mono, fontSize: 7.5, letterSpacing: 0.5, color: DR.goldDeep, fontWeight: 700, lineHeight: 1.25, textAlign: 'center' }}>NOV<br/>’25</span>
          </div>
        </div>
        <div style={{ padding: '11px 15px', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <div>
            <div style={{ fontFamily: DR.mono, fontSize: 7.5, letterSpacing: 1.4, color: DR.mute, fontWeight: 700 }}>YOUR STORY · 142 FRAMES</div>
            <div style={{ fontFamily: DR.serif, fontSize: 17.5, fontWeight: 500, color: DR.ink, letterSpacing: -0.3, marginTop: 3 }}>Six slow days in Lisbon</div>
          </div>
          <span style={{ color: DR.goldDeep, fontSize: 15 }}>→</span>
        </div>
      </div>
    </div>
  );
}

// Atlas handoff — a quiet line right under the artifact.
function AtlasLine() {
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginTop: 12, paddingTop: 14, borderTop: ed.rule }}>
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={DR.soft} strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.6 2.6 2.6 15.4 0 18M12 3c-2.6 2.6-2.6 15.4 0 18"/></svg>
      <span style={{ flex: 1, fontFamily: DR.serif, fontSize: 14.5, color: DR.ink, fontWeight: 500, letterSpacing: -0.2 }}>Lisbon settles into your Atlas</span>
      <span style={{ color: DR.goldDeep, fontSize: 15 }}>→</span>
    </div>
  );
}

// The trip in brief — Stay · Map · Costs (Costs carries the settle-up).
function TripInBrief() {
  const cells = [
    [FT_ICON.stay, 'Casa do Alecrim', '5 NIGHTS', false],
    [FT_ICON.route, '4 cities', 'THE ROUTE', false],
    [FT_ICON.costs, 'You’re owed €347', 'SETTLE UP', true],
  ];
  return (
    <div style={{ marginTop: 20 }}>
      <div style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 2, color: DR.mute, fontWeight: 700, marginBottom: 11 }}>THE TRIP IN BRIEF</div>
      <div style={{ display: 'flex', gap: 8 }}>
        {cells.map(([ic, v, l, flag], i) => (
          <div key={i} style={{ flex: 1, padding: '12px 11px', background: flag ? 'rgba(176,133,58,0.07)' : DR.card, borderRadius: 12, border: `0.5px solid ${flag ? 'rgba(176,133,58,0.4)' : DR.hair}` }}>
            <span style={{ color: flag ? DR.goldDeep : DR.soft, display: 'flex' }}>{ic}</span>
            <div style={{ fontFamily: DR.serif, fontSize: 13, color: flag ? DR.goldDeep : DR.ink, fontWeight: 500, letterSpacing: -0.2, marginTop: 9, lineHeight: 1.15 }}>{v}</div>
            <div style={{ fontFamily: DR.mono, fontSize: 7, letterSpacing: 1, color: flag ? DR.goldDeep : DR.mute, fontWeight: 700, marginTop: 4 }}>{l}</div>
          </div>
        ))}
      </div>
    </div>
  );
}

// The moments you'll keep — Vesper's curated standouts (a few, with a thumb).
function MomentsKept() {
  const items = [
    ['The first miradouro, before the heat', 'DAY 1 · ALFAMA'],
    ['Ramiro, and the long table', 'DAY 3 · INTENDENTE'],
    ['Belém at opening, nearly alone', 'DAY 4 · BELÉM'],
  ];
  return (
    <div style={{ marginTop: 22 }}>
      <div style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 2, color: DR.mute, fontWeight: 700, marginBottom: 6 }}>THE MOMENTS YOU’LL KEEP</div>
      {items.map(([t, sub], i) => (
        <div key={i} style={{ display: 'flex', alignItems: 'center', gap: 13, padding: '11px 0', borderTop: i ? `0.5px solid ${DR.hairThin}` : 'none' }}>
          <div style={{ width: 44, height: 44, borderRadius: 9, overflow: 'hidden', flexShrink: 0 }}><StyleRiso w={44} h={44}/></div>
          <div style={{ flex: 1 }}>
            <div style={{ fontFamily: DR.serif, fontSize: 15.5, color: DR.ink, letterSpacing: -0.2, lineHeight: 1.2 }}>{t}</div>
            <div style={{ fontFamily: DR.mono, fontSize: 7.5, letterSpacing: 1, color: DR.faint, fontWeight: 700, marginTop: 3 }}>{sub}</div>
          </div>
        </div>
      ))}
    </div>
  );
}

// Canonical post-trip home — a gentle scroll (taller than a viewport).
function PostTrip() {
  return (
    <PFrame h={980} bare>
      <PostCover/>
      <LookBack/>
      <div style={{ padding: '18px 24px 0' }}>
        <KeepsakePostcard/>
        <AtlasLine/>
        <TripInBrief/>
        <MomentsKept/>
      </div>
      <div style={{ height: 96 }}/>
      <TabBar active="trips"/>
    </PFrame>
  );
}

Object.assign(window, { PostTrip });
