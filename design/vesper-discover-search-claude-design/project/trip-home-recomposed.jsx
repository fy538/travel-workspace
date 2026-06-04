// ═══════════════════════════════════════════════════════════════
// SINGLE-TRIP HOME · recomposed. Three movements with real breath:
//   1 MASTHEAD (taller cover + Vesper standfirst as its caption)
//   2 THE ONE THING (dominant facet hero)
//   3 THE QUIET REST (receded day slice) + a footer floor.
// Reuses DR + StyleRiso + StyleGouache + Filmstrip/Ppl/CASTD +
// FCover bits (CIcon/CICO) + FacetsHero/FacetsAllClear + SliceRich.
// ═══════════════════════════════════════════════════════════════

// Taller masthead — identity + Vesper standfirst folded into the cover unit.
function Masthead({ vibe }) {
  const line = vibe
    ? 'Lisbon’s warmest the week you land — long evenings outside, one slow morning in Alfama.'
    : 'Alfama rewards the slow walker — I’ve been keeping the quiet corners for your mornings.';
  return (
    <div>
      {/* taller riso cover */}
      <div style={{ position: 'relative', height: 270, marginTop: -40 }}>
        <div style={{ position: 'absolute', inset: 0 }}><StyleRiso w={393} h={270}/></div>
        <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.44) 0%, rgba(20,14,9,0) 28%, rgba(20,14,9,0) 50%, rgba(20,14,9,0.74) 100%)' }}/>
        <div style={{ position: 'absolute', top: 46, left: 16, right: 16, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <CIcon>{CICO.back}</CIcon>
          <div style={{ display: 'flex', gap: 8 }}><CIcon dot>{CICO.chat}</CIcon><CIcon dot>{CICO.bell}</CIcon><CIcon>{CICO.info}</CIcon></div>
        </div>
        <div style={{ position: 'absolute', top: 92, left: 18 }}><Filmstrip truth={1} onDark/></div>
        <div style={{ position: 'absolute', left: 20, right: 20, bottom: 18 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 8 }}>
            <span style={{ padding: '3px 9px', borderRadius: 999, background: 'rgba(255,255,255,0.2)', backdropFilter: 'blur(6px)', fontSize: 9, letterSpacing: 1.4, fontWeight: 700, color: '#fff' }}>IN 23 DAYS</span>
            <Ppl who={CASTD} size={22} onDark/>
          </div>
          <h1 style={{ fontFamily: DR.serif, fontSize: 38, fontWeight: 500, letterSpacing: -1.1, lineHeight: 0.96, color: '#fff', margin: 0 }}>Lisbon, <span style={{ fontStyle: 'italic' }}>slowly</span></h1>
        </div>
      </div>
      {/* Vesper standfirst — the cover's caption, tightly grouped under the title */}
      <div style={{ padding: '13px 22px 0', display: 'flex', gap: 10 }}>
        <svg width="13" height="13" viewBox="0 0 24 24" fill={DR.gold} style={{ flexShrink: 0, marginTop: 3 }}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 16.5, color: DR.ink, margin: 0, lineHeight: 1.4, letterSpacing: -0.15 }}>{line}</p>
      </div>
    </div>
  );
}

// Quiet, receded day slice — secondary to the facet hero.
function QuietSlice() {
  const D = [['SAT 18', 'Land soft, settle in Alfama'], ['SUN 19', 'Miradouros, east to west'], ['MON 20', 'still open', true]];
  return (
    <div style={{ padding: '0 22px' }}>
      <div style={{ fontSize: 8.5, letterSpacing: 2, color: DR.faint, fontWeight: 700, marginBottom: 6 }}>THE DAYS · 6</div>
      {D.map(([d, t, gap], i) => (
        <div key={i} style={{ display: 'grid', gridTemplateColumns: '50px 1fr 14px', gap: 11, padding: '8px 0', borderTop: i ? `0.5px solid ${DR.hairThin}` : 'none', alignItems: 'center' }}>
          <span style={{ fontFamily: DR.mono, fontSize: 8.5, color: DR.faint, letterSpacing: 0.5, fontWeight: 600 }}>{d}</span>
          <span style={{ fontFamily: DR.serif, fontSize: 13.5, color: gap ? DR.mute : DR.soft, fontStyle: gap ? 'italic' : 'normal', letterSpacing: -0.1 }}>{t}</span>
          <span style={{ color: DR.faint, fontSize: 12 }}>›</span>
        </div>
      ))}
    </div>
  );
}
// Footer floor — closes the composition.
function HomeFloor() {
  return (
    <div style={{ margin: '4px 22px 0', paddingTop: 14, borderTop: `0.5px solid ${DR.hairThin}`, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
      <span style={{ fontFamily: DR.serif, fontSize: 14.5, fontWeight: 500, color: DR.ink, letterSpacing: -0.1 }}>Open the full itinerary</span>
      <span style={{ display: 'inline-flex', alignItems: 'center', justifyContent: 'center', width: 30, height: 30, borderRadius: 999, background: DR.blue, color: '#fff', fontSize: 14 }}>→</span>
    </div>
  );
}

function HomeShell({ children }) {
  return <div style={{ width: 393, background: DR.paper, borderRadius: 30, overflow: 'hidden', border: `0.5px solid ${DR.hair}`, boxShadow: '0 30px 60px -30px rgba(0,0,0,0.3)', position: 'relative', paddingBottom: 20 }}>
    <div style={{ height: 40 }}/>{children}
  </div>;
}

// NEEDS-YOU — three movements with breath: masthead · hero · quiet rest + floor.
function HomeReNeedsYou() {
  return (
    <HomeShell>
      <Masthead/>
      <div style={{ height: 26 }}/>{/* breath before the one thing */}
      <div style={{ padding: '0 18px' }}><FacetsHero bare/></div>
      <div style={{ height: 30 }}/>{/* breath before the quiet rest */}
      <QuietSlice/>
      <div style={{ height: 18 }}/>
      <HomeFloor/>
    </HomeShell>
  );
}
// ALL-CLEAR — masthead (vibey) · map hero · quiet rest + floor.
function HomeReAllClear() {
  return (
    <HomeShell>
      <Masthead vibe/>
      <div style={{ height: 26 }}/>
      <div style={{ padding: '0 18px' }}><FacetsAllClear bare/></div>
      <div style={{ height: 30 }}/>
      <QuietSlice/>
      <div style={{ height: 18 }}/>
      <HomeFloor/>
    </HomeShell>
  );
}

Object.assign(window, { HomeReNeedsYou, HomeReAllClear, Masthead, QuietSlice, HomeFloor });
