// ═══════════════════════════════════════════════════════════════
// THE FOLIO HOME · AGED ACROSS PHASES — 3 variations.
// Pre-trip = the canonical Folio (FolioBodyA/B). Here: Live (during)
// + Memory (after), expressed three ways in the SAME Folio language.
// Reuses DR, StyleRiso, CIcon/CICO, FT_ICON, Ppl/CASTD, SliceRich, ftk.
// ═══════════════════════════════════════════════════════════════

// Shared iPhone device frame — bezel, dynamic island, home indicator.
// Every full-screen mockup on the page renders inside this so they read
// unmistakably as phone screens (not pop-ups or floating cards).
const PFrame = ({ children, h, bare }) => (
  <div style={{ width: 413, padding: 10, borderRadius: 56, background: 'linear-gradient(155deg, #322B25, #0E0B08 62%)', boxShadow: '0 40px 80px -36px rgba(0,0,0,0.5), 0 0 0 1px rgba(0,0,0,0.35)' }}>
    <div style={{ position: 'relative', width: 393, height: h, background: DR.paper, borderRadius: 47, overflow: 'hidden', paddingBottom: bare ? 0 : 30 }}>
      {!bare && <div style={{ height: 40 }}/>}
      {children}
      <div style={{ position: 'absolute', top: 11, left: '50%', transform: 'translateX(-50%)', width: 104, height: 29, background: '#000', borderRadius: 999, zIndex: 60 }}/>
      <div style={{ position: 'absolute', bottom: 8, left: '50%', transform: 'translateX(-50%)', width: 126, height: 5, borderRadius: 999, background: 'rgba(20,14,9,0.32)', zIndex: 60 }}/>
    </div>
  </div>
);

// Phase cover — riso for live, darker "gouache" wash for memory.
function PCover({ phase }) {
  const live = phase === 'live';
  return (
    <div style={{ position: 'relative', height: 204, marginTop: -40 }}>
      <div style={{ position: 'absolute', inset: 0, filter: live ? 'none' : 'saturate(0.82) brightness(0.9)' }}><StyleRiso w={393} h={204}/></div>
      <div style={{ position: 'absolute', inset: 0, background: live
        ? 'linear-gradient(to bottom, rgba(20,14,9,0.42) 0%, rgba(20,14,9,0) 32%, rgba(20,14,9,0) 48%, rgba(20,14,9,0.74) 100%)'
        : 'linear-gradient(to bottom, rgba(20,14,9,0.55) 0%, rgba(20,14,9,0.22) 42%, rgba(20,14,9,0.86) 100%)' }}/>
      <div style={{ position: 'absolute', top: 46, left: 16, right: 16, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <CIcon>{CICO.back}</CIcon>
        <div style={{ display: 'flex', gap: 8 }}><CIcon dot>{CICO.chat}</CIcon><CIcon dot>{CICO.bell}</CIcon><CIcon>{CICO.info}</CIcon></div>
      </div>
      <div style={{ position: 'absolute', left: 20, right: 20, bottom: 16 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 7 }}>
          <span style={{ padding: '3px 9px', borderRadius: 999, background: live ? 'rgba(61,80,102,0.85)' : 'rgba(255,255,255,0.18)', backdropFilter: 'blur(6px)', fontSize: 9, letterSpacing: 1.4, fontWeight: 700, color: '#fff' }}>{live ? 'DAY 3 · TUE' : 'KEPT · NOV 2025'}</span>
          <Ppl who={CASTD} size={22} onDark/>
        </div>
        <h1 style={{ fontFamily: DR.serif, fontSize: 34, fontWeight: 500, letterSpacing: -1, lineHeight: 0.98, color: '#fff', margin: 0 }}>Lisbon, <span style={{ fontStyle: 'italic' }}>{live ? 'today' : 'kept'}</span></h1>
      </div>
    </div>
  );
}

// Vesper block in the home's voice (place/itinerary, never logistics).
function PVesper({ tag, txt, accent = DR.gold, tagColor = DR.goldDeep }) {
  return (
    <div style={{ padding: '16px 22px 4px' }}>
      <div style={{ paddingLeft: 13, borderLeft: `2px solid ${accent}` }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 5 }}>
          <svg width="11" height="11" viewBox="0 0 24 24" fill={accent}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>
          <span style={{ fontSize: 8.5, letterSpacing: 1.4, color: tagColor, fontWeight: 700 }}>VESPER · {tag}</span>
        </div>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 16, color: DR.ink, margin: 0, lineHeight: 1.4, letterSpacing: -0.12 }}>{txt}</p>
      </div>
    </div>
  );
}

const blueGreen = '#3D5066';

// ─────────────────────────────────────────────────────────────────
// V1 · SAME SHELL, AGED — identical anatomy, content shifts by phase.
// ─────────────────────────────────────────────────────────────────
// Live: a "now / next" hero mirroring FacetsHero, then quiet rest.
function V1LiveFacets() {
  return (
    <div style={{ padding: '14px 18px 0' }}>
      <div style={{ padding: '16px 17px', background: DR.card, borderRadius: 16, border: `0.8px solid rgba(61,80,102,0.4)`, marginBottom: 8 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 9 }}><span style={{ width: 6, height: 6, borderRadius: 6, background: blueGreen }}/><span style={{ fontSize: 9, letterSpacing: 1.4, color: blueGreen, fontWeight: 700 }}>NEXT · 4:30</span></div>
        <div style={{ fontFamily: DR.serif, fontSize: 22, fontWeight: 500, color: DR.ink, letterSpacing: -0.4, lineHeight: 1.08 }}>Miradouro da Graça, golden hour</div>
        <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13, color: DR.mute, marginTop: 5 }}>10 min on foot from lunch — leave by 4:10 to catch the light.</div>
        <div style={{ marginTop: 14, display: 'flex', alignItems: 'center', gap: 8 }}><span style={{ padding: '9px 16px', background: DR.blue, color: '#fff', borderRadius: 999, fontSize: 12.5, fontWeight: 600 }}>Directions</span><span style={{ padding: '9px 14px', background: DR.cardSoft, border: `0.5px solid ${DR.hair}`, borderRadius: 999, fontFamily: DR.serif, fontStyle: 'italic', fontSize: 12.5, color: DR.soft }}>save a moment</span></div>
      </div>
      <div style={{ display: 'flex', gap: 8 }}>
        {[['stay', 'Tonight', 'Alecrim'], ['costs', 'Spent today', '€42'], ['route', 'Tram 28', 'next']].map(([key, label, val]) => (
          <div key={key} style={{ flex: 1, padding: '11px 10px', background: DR.card, borderRadius: 12, border: `0.5px solid ${DR.hair}`, textAlign: 'center' }}>
            <div style={{ display: 'flex', justifyContent: 'center', color: DR.soft, marginBottom: 6 }}>{FT_ICON[key]}</div>
            <div style={{ fontFamily: DR.serif, fontSize: 13, fontWeight: 500, color: DR.ink, letterSpacing: -0.1, lineHeight: 1 }}>{val}</div>
            <div style={{ fontSize: 7, letterSpacing: 1, color: DR.mute, fontWeight: 700, marginTop: 4 }}>{label.toUpperCase()}</div>
          </div>
        ))}
      </div>
    </div>
  );
}
// Today's slice — a couple of beats with a "now" marker.
function TodaySlice() {
  const beats = [['done', '09:30', 'Slow morning, Alfama'], ['now', '13:00', 'Lunch at Ramiro'], ['next', '16:30', 'Graça for the light'], ['later', 'eve', 'No plans past first wine']];
  return (
    <div style={{ padding: '18px 20px 0' }}>
      <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginBottom: 11 }}>
        <span style={{ fontSize: 9, letterSpacing: 2, color: DR.mute, fontWeight: 700 }}>TODAY</span>
        <span style={{ fontSize: 9, letterSpacing: 1.2, color: DR.mute, fontWeight: 600 }}>VESPER’S CUT</span>
      </div>
      {beats.map(([state, t, txt], i) => {
        const now = state === 'now';
        const dim = state === 'done';
        return (
          <div key={i} style={{ display: 'grid', gridTemplateColumns: '50px 1fr 12px', gap: 11, padding: '9px 0', borderTop: i ? `0.5px solid ${DR.hairThin}` : 'none', alignItems: 'center' }}>
            <span style={{ fontFamily: DR.mono, fontSize: 9, color: now ? blueGreen : DR.faint, letterSpacing: 0.5, fontWeight: 700, textAlign: 'right' }}>{t}</span>
            <span style={{ fontFamily: DR.serif, fontSize: 14.5, fontWeight: now ? 600 : 500, color: dim ? DR.faint : DR.ink, letterSpacing: -0.2, textDecoration: dim ? 'line-through' : 'none', textDecorationColor: DR.faint }}>{txt}</span>
            {now ? <span style={{ width: 8, height: 8, borderRadius: 8, background: blueGreen, boxShadow: `0 0 0 3px rgba(61,80,102,0.18)` }}/> : <span/>}
          </div>
        );
      })}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginTop: 10, paddingTop: 11, borderTop: `0.5px solid ${DR.hairThin}` }}>
        <span style={{ fontFamily: DR.serif, fontSize: 13.5, fontWeight: 500, color: DR.ink }}>Open today’s plan</span><span style={{ color: DR.blue, fontSize: 14 }}>→</span>
      </div>
    </div>
  );
}
function V1Live() {
  return <PFrame><PCover phase="live"/><PVesper tag="RIGHT NOW" txt="You’re due the light at Graça — I held the evening loose so you can linger." accent={blueGreen} tagColor={blueGreen}/><V1LiveFacets/><TodaySlice/></PFrame>;
}

// Memory: totals where facets were, the record where the slice was.
function MemoryTotals() {
  return (
    <div style={{ padding: '14px 18px 0', display: 'flex', gap: 7 }}>
      {[['6', 'NIGHTS'], ['4', 'CITIES'], ['€1.4k', 'SHARED'], ['142', 'KEPT']].map(([v, l]) => (
        <div key={l} style={{ flex: 1, padding: '12px 6px', background: DR.card, borderRadius: 11, border: `0.5px solid ${DR.hair}`, textAlign: 'center' }}>
          <div style={{ fontFamily: DR.serif, fontSize: 17, fontWeight: 500, color: DR.ink, letterSpacing: -0.3 }}>{v}</div>
          <div style={{ fontSize: 7, letterSpacing: 1, color: DR.mute, fontWeight: 700, marginTop: 3 }}>{l}</div>
        </div>
      ))}
    </div>
  );
}
function RecordSlice() {
  const beats = [['SAT 18', 'The first miradouro, before the heat'], ['SUN 19', 'Ramiro, and the long table'], ['TUE 21', 'Belém at opening, alone with the cloister']];
  return (
    <div style={{ padding: '18px 20px 0' }}>
      <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginBottom: 11 }}>
        <span style={{ fontSize: 9, letterSpacing: 2, color: DR.mute, fontWeight: 700 }}>THE RECORD</span>
        <span style={{ fontSize: 9, letterSpacing: 1.2, color: DR.mute, fontWeight: 600 }}>VESPER’S CUT</span>
      </div>
      <div style={{ display: 'flex', gap: 6, marginBottom: 13 }}>{[0, 1, 2].map(i => <div key={i} style={{ flex: 1, height: 54, borderRadius: 8, overflow: 'hidden' }}><StyleRiso w={108} h={54}/></div>)}</div>
      {beats.map(([d, t], i) => (
        <div key={i} style={{ display: 'grid', gridTemplateColumns: '54px 1fr', gap: 12, padding: '9px 0', borderTop: i ? `0.5px solid ${DR.hairThin}` : 'none', alignItems: 'center' }}>
          <span style={{ fontFamily: DR.mono, fontSize: 9.5, color: DR.mute, letterSpacing: 0.6, fontWeight: 600 }}>{d}</span>
          <span style={{ fontFamily: DR.serif, fontSize: 14, color: DR.ink, letterSpacing: -0.15, lineHeight: 1.3 }}>{t}</span>
        </div>
      ))}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginTop: 11, paddingTop: 11, borderTop: `0.5px solid ${DR.hairThin}` }}>
        <span style={{ fontFamily: DR.serif, fontSize: 13.5, fontWeight: 500, color: DR.ink }}>Read your story</span><span style={{ color: DR.blue, fontSize: 14 }}>→</span>
      </div>
    </div>
  );
}
function V1Memory() {
  return <PFrame><PCover phase="memory"/><PVesper tag="LOOKING BACK" txt="Six days that ran slow in the best way. I’ve written it up — the mornings were the heart of it." accent={DR.gold}/><MemoryTotals/><RecordSlice/></PFrame>;
}

// ─────────────────────────────────────────────────────────────────
// V2 · LIVE TAKES OVER — during the trip the home shifts posture:
// one big NOW card, voice-forward, the rest demoted to a line.
// ─────────────────────────────────────────────────────────────────
function V2Live() {
  return (
    <PFrame>
      <PCover phase="live"/>
      <div style={{ padding: '16px 18px 0' }}>
        {/* the one NOW card */}
        <div style={{ borderRadius: 18, overflow: 'hidden', border: `0.5px solid ${DR.hair}`, boxShadow: '0 12px 30px -18px rgba(0,0,0,0.4)' }}>
          <div style={{ height: 132, position: 'relative' }}>
            <StyleRiso w={357} h={132}/>
            <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to top, rgba(20,14,9,0.7), rgba(20,14,9,0.05) 60%)' }}/>
            <div style={{ position: 'absolute', top: 12, left: 14, display: 'flex', alignItems: 'center', gap: 6 }}><span style={{ width: 6, height: 6, borderRadius: 6, background: '#fff' }}/><span style={{ fontSize: 8.5, letterSpacing: 1.5, color: '#fff', fontWeight: 700 }}>NOW · 4:30</span></div>
            <div style={{ position: 'absolute', left: 14, right: 14, bottom: 12 }}><h2 style={{ fontFamily: DR.serif, fontSize: 24, fontWeight: 500, color: '#fff', margin: 0, letterSpacing: -0.5, lineHeight: 1.04 }}>The light at Graça</h2></div>
          </div>
          <div style={{ padding: '14px 16px', background: DR.card }}>
            <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14.5, color: DR.soft, margin: 0, lineHeight: 1.4 }}>Leave by 4:10 — ten minutes on foot. The bench on the left stays empty till five.</p>
            <div style={{ marginTop: 13, display: 'flex', alignItems: 'center', gap: 8 }}>
              <span style={{ padding: '10px 16px', background: DR.blue, color: '#fff', borderRadius: 999, fontSize: 12.5, fontWeight: 600 }}>Directions</span>
              <span style={{ flex: 1 }}/>
              <span style={{ width: 42, height: 42, borderRadius: 999, background: '#5B4B8A', display: 'flex', alignItems: 'center', justifyContent: 'center' }}><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#fff" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><rect x="9" y="3" width="6" height="12" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg></span>
            </div>
          </div>
        </div>
        {/* later today — one demoted line */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 10, padding: '14px 4px 4px' }}>
          <span style={{ fontSize: 8.5, letterSpacing: 1.3, color: DR.mute, fontWeight: 700 }}>LATER</span>
          <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14, color: DR.soft, flex: 1 }}>dinner loose · tomorrow Belém early</span>
          <span style={{ color: DR.faint, fontSize: 13 }}>›</span>
        </div>
        {/* facets collapsed to a single quiet strip */}
        <div style={{ display: 'flex', gap: 14, padding: '12px 4px 0', borderTop: `0.5px solid ${DR.hairThin}`, marginTop: 4 }}>
          {[['stay', 'Alecrim tonight'], ['costs', '€42 today'], ['route', 'map']].map(([key, val]) => (
            <span key={key} style={{ display: 'inline-flex', alignItems: 'center', gap: 6, fontSize: 12, color: DR.soft, fontFamily: DR.serif }}><span style={{ color: DR.faint, display: 'flex' }}>{FT_ICON[key]}</span>{val}</span>
          ))}
        </div>
      </div>
    </PFrame>
  );
}
function V2Memory() {
  return (
    <PFrame>
      <PCover phase="memory"/>
      <div style={{ padding: '16px 18px 0' }}>
        <div style={{ borderRadius: 18, overflow: 'hidden', border: `0.5px solid ${DR.hair}`, boxShadow: '0 12px 30px -18px rgba(0,0,0,0.4)' }}>
          <div style={{ height: 150, position: 'relative' }}>
            <div style={{ filter: 'saturate(0.85) brightness(0.92)' }}><StyleRiso w={357} h={150}/></div>
            <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to top, rgba(20,14,9,0.78), rgba(20,14,9,0.1) 65%)' }}/>
            <div style={{ position: 'absolute', left: 16, right: 16, bottom: 14 }}>
              <div style={{ fontSize: 8.5, letterSpacing: 1.5, color: 'rgba(255,255,255,0.8)', fontWeight: 700, marginBottom: 5 }}>YOUR STORY IS READY</div>
              <h2 style={{ fontFamily: DR.serif, fontSize: 25, fontWeight: 500, color: '#fff', margin: 0, letterSpacing: -0.5, lineHeight: 1.02 }}>Six slow days in Lisbon</h2>
            </div>
          </div>
          <div style={{ padding: '14px 16px', background: DR.card }}>
            <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14.5, color: DR.soft, margin: 0, lineHeight: 1.4 }}>I’ve written the trip up — the mornings, mostly. Read it, or let it settle into Atlas.</p>
            <div style={{ marginTop: 13, display: 'flex', alignItems: 'center', gap: 8 }}><span style={{ padding: '10px 16px', background: DR.blue, color: '#fff', borderRadius: 999, fontSize: 12.5, fontWeight: 600 }}>Read the story</span><span style={{ padding: '10px 14px', background: DR.cardSoft, border: `0.5px solid ${DR.hair}`, borderRadius: 999, fontFamily: DR.serif, fontStyle: 'italic', fontSize: 12.5, color: DR.soft }}>send to Atlas</span></div>
          </div>
        </div>
        <div style={{ display: 'flex', gap: 14, padding: '14px 4px 0' }}>
          {[['6 nights'], ['4 cities'], ['142 photos'], ['settled']].map(([v], i) => (
            <span key={i} style={{ fontSize: 12, color: DR.soft, fontFamily: DR.serif, fontStyle: 'italic' }}>{v}</span>
          ))}
        </div>
      </div>
    </PFrame>
  );
}

// ─────────────────────────────────────────────────────────────────
// V3 · COMPANION BAND — keep the familiar Folio, add a persistent
// context band at the very top that owns "the present".
// ─────────────────────────────────────────────────────────────────
function LiveBand() {
  return (
    <div style={{ margin: '0 14px', marginTop: -34, position: 'relative', zIndex: 2, background: blueGreen, borderRadius: 16, padding: '12px 15px', color: '#fff', boxShadow: '0 14px 30px -16px rgba(61,80,102,0.7)' }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 6 }}><span style={{ width: 6, height: 6, borderRadius: 6, background: '#fff' }}/><span style={{ fontSize: 8.5, letterSpacing: 1.4, fontWeight: 700, opacity: 0.85 }}>RIGHT NOW · 4:30</span><span style={{ flex: 1 }}/><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.85)" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg></div>
      <div style={{ fontFamily: DR.serif, fontSize: 18, fontWeight: 500, letterSpacing: -0.3, lineHeight: 1.1 }}>Head to Graça for the light — leave by 4:10.</div>
      <div style={{ display: 'flex', gap: 8, marginTop: 11 }}><span style={{ padding: '7px 14px', background: 'rgba(255,255,255,0.16)', borderRadius: 999, fontSize: 11.5, fontWeight: 600 }}>Directions</span><span style={{ padding: '7px 12px', background: 'rgba(255,255,255,0.16)', borderRadius: 999, fontFamily: DR.serif, fontStyle: 'italic', fontSize: 11.5 }}>save a moment</span></div>
    </div>
  );
}
function V3Live() {
  return (
    <PFrame>
      <PCover phase="live"/>
      <LiveBand/>
      <div style={{ paddingTop: 6 }}>
        <PVesper tag="ON LISBON" txt="The rest of the day stays loose — Alfama empties after six if you want it quiet." accent={DR.gold}/>
      </div>
      <TodaySlice/>
    </PFrame>
  );
}
function MemoryBand() {
  return (
    <div style={{ margin: '0 14px', marginTop: -34, position: 'relative', zIndex: 2, background: DR.ink, borderRadius: 16, padding: '12px 15px', color: '#fff', boxShadow: '0 14px 30px -16px rgba(20,14,9,0.6)' }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 6 }}><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.85)" strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round"><path d="M4 12l5 5L20 6"/></svg><span style={{ fontSize: 8.5, letterSpacing: 1.4, fontWeight: 700, opacity: 0.85 }}>TRIP COMPLETE · YOUR STORY IS READY</span></div>
      <div style={{ fontFamily: DR.serif, fontSize: 18, fontWeight: 500, letterSpacing: -0.3, lineHeight: 1.1 }}>Six slow days in Lisbon — written up.</div>
      <div style={{ display: 'flex', gap: 8, marginTop: 11 }}><span style={{ padding: '7px 14px', background: 'rgba(255,255,255,0.16)', borderRadius: 999, fontSize: 11.5, fontWeight: 600 }}>Read the story</span><span style={{ padding: '7px 12px', background: 'rgba(255,255,255,0.16)', borderRadius: 999, fontFamily: DR.serif, fontStyle: 'italic', fontSize: 11.5 }}>send to Atlas</span></div>
    </div>
  );
}
function V3Memory() {
  return (
    <PFrame>
      <PCover phase="memory"/>
      <MemoryBand/>
      <div style={{ paddingTop: 6 }}><PVesper tag="LOOKING BACK" txt="The mornings were the heart of it — I kept the quiet ones." accent={DR.gold}/></div>
      <MemoryTotals/>
      <RecordSlice/>
    </PFrame>
  );
}

Object.assign(window, { V1Live, V1Memory, V2Live, V2Memory, V3Live, V3Memory });
