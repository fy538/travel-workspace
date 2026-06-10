// ═══════════════════════════════════════════════════════════════
// MAP + PHOTOS/STORY objects. Map = illustrated trip constellation,
// never Mapbox. Photos/Story = the memory artifact. Reuses TH +
// ObjectHeader + Phone + StyleRiso/StyleGouache + People/CAST.
// ═══════════════════════════════════════════════════════════════

// MAP — an illustrated trip constellation: days/stays/saved as pins
// on a paper map, route drawn between them. Emotional, not navigational.
function TripMap() {
  const pins = [
    { l: 22, t: 30, k: 'stay',  lab: 'Alfama', sub: 'home base' },
    { l: 60, t: 22, k: 'day',   lab: 'Graça' },
    { l: 46, t: 52, k: 'booked',lab: 'Ramiro' },
    { l: 76, t: 60, k: 'saved', lab: 'Belém' },
    { l: 32, t: 74, k: 'day',   lab: 'fado' },
  ];
  const color = (k) => k === 'stay' ? TH.gold : k === 'booked' ? TH.blue : k === 'saved' ? TH.mute : TH.soft;
  return (
    <Phone bg={TH.paper}>
      <div style={{ position: 'absolute', inset: 0, overflow: 'hidden' }}>
        <ObjectHeader kicker="MAP · YOUR LISBON" title="Lisbon, slowly"/>
        {/* paper map field */}
        <div style={{ position: 'relative', margin: '16px 16px 0', height: 420, borderRadius: 16, overflow: 'hidden', background: '#E7DCC6', border: `0.5px solid ${TH.hair}` }}>
          {/* faint contour + river */}
          <svg width="100%" height="100%" viewBox="0 0 360 420" preserveAspectRatio="none" style={{ position: 'absolute', inset: 0 }}>
            <rect width="360" height="420" fill="#E7DCC6"/>
            <path d="M0 300 Q120 280 200 300 T360 290 L360 420 L0 420Z" fill="#AEBEB4" opacity="0.45"/>
            {[80,150,220,360].map((y,i)=><path key={i} d={`M0 ${y} Q160 ${y-18} 360 ${y}`} stroke="#C9B996" strokeWidth="0.7" fill="none" opacity="0.6"/>)}
            {/* route between day/booked pins */}
            <path d="M79 126 Q170 80 216 92 Q250 150 274 252 Q140 300 115 311" stroke={TH.gold} strokeWidth="1.5" strokeDasharray="2 4" fill="none" strokeLinecap="round"/>
          </svg>
          {pins.map((p, i) => (
            <div key={i} style={{ position: 'absolute', left: `${p.l}%`, top: `${p.t}%`, transform: 'translate(-50%,-50%)', display: 'flex', alignItems: 'center', gap: 5 }}>
              {p.k === 'saved'
                ? <span style={{ width: 8, height: 8, borderRadius: 999, border: `1.4px solid ${color(p.k)}`, background: '#E7DCC6' }}/>
                : <span style={{ width: p.k==='stay'?11:8, height: p.k==='stay'?11:8, borderRadius: 999, background: color(p.k), boxShadow: p.k==='stay'?'0 0 0 4px rgba(176,133,58,0.2)':'none' }}/>}
              <div style={{ fontFamily: TH.serif, fontSize: 12, fontWeight: 500, color: TH.ink, letterSpacing: -0.1, whiteSpace: 'nowrap' }}>
                {p.lab}{p.sub && <span style={{ display: 'block', fontSize: 8.5, fontStyle: 'italic', color: TH.mute }}>{p.sub}</span>}
              </div>
            </div>
          ))}
          {/* legend */}
          <div style={{ position: 'absolute', left: 12, bottom: 12, display: 'flex', gap: 12, fontFamily: TH.mono, fontSize: 8, color: TH.soft, letterSpacing: 0.5, fontWeight: 600 }}>
            <span style={{ display: 'flex', alignItems: 'center', gap: 4 }}><span style={{ width: 6, height: 6, borderRadius: 6, background: TH.gold }}/>STAY</span>
            <span style={{ display: 'flex', alignItems: 'center', gap: 4 }}><span style={{ width: 6, height: 6, borderRadius: 6, background: TH.blue }}/>BOOKED</span>
            <span style={{ display: 'flex', alignItems: 'center', gap: 4 }}><span style={{ width: 6, height: 6, borderRadius: 6, border: `1.2px solid ${TH.mute}` }}/>SAVED</span>
          </div>
        </div>
        <div style={{ padding: '14px 22px 0', textAlign: 'center' }}>
          <span style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 13, color: TH.mute }}>five places, one slow loop — tap any to open it</span>
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// PHOTOS / STORY — the memory artifact. A gouache cover story + a
// gathered film-strip, the future of the trip not a utility grid.
function TripStory() {
  return (
    <Phone bg={TH.ink}>
      <div style={{ position: 'absolute', inset: 0, overflow: 'hidden', background: TH.paper }}>
        {/* gouache story cover */}
        <div style={{ position: 'relative', height: 300 }}>
          <div style={{ position: 'absolute', inset: 0 }}><StyleGouache w={393} h={300}/></div>
          <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.36), rgba(20,14,9,0) 40%, rgba(20,14,9,0.7))' }}/>
          <div style={{ paddingTop: 50 }}><TripHeader onDark/></div>
          <div style={{ position: 'absolute', left: 22, right: 22, bottom: 18 }}>
            <div style={{ fontSize: 9, letterSpacing: 1.8, color: 'rgba(255,255,255,0.82)', fontWeight: 700 }}>THE STORY · BY VESPER</div>
            <h1 style={{ fontFamily: TH.serif, fontSize: 30, fontWeight: 500, letterSpacing: -0.6, lineHeight: 1.05, color: '#fff', margin: '6px 0 0' }}>Six days, the slow way</h1>
          </div>
        </div>
        {/* opening line */}
        <div style={{ padding: '18px 22px 0' }}>
          <p style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 16, color: TH.ink, lineHeight: 1.45, margin: 0, letterSpacing: -0.1 }}>
            You arrived tired and left unhurried. Somewhere around the fourth night, the city stopped being a list.
          </p>
        </div>
        {/* film strip of kept frames */}
        <div style={{ padding: '18px 0 0' }}>
          <div style={{ padding: '0 22px' }}><Label right="12 KEPT">THE FRAMES</Label></div>
          <div style={{ marginTop: 12, display: 'flex', gap: 8, padding: '0 16px', overflow: 'hidden' }}>
            {['amber','day','dusk','amber'].map((t,i)=>(
              <div key={i} style={{ flex: '0 0 116px', height: 142, borderRadius: 10, overflow: 'hidden', transform: `rotate(${i%2?1.2:-1.2}deg)`, border: `3px solid #fff`, boxShadow: '0 6px 16px -8px rgba(0,0,0,0.25)' }}>
                <StyleGouache w={116} h={142}/>
              </div>
            ))}
          </div>
        </div>
        {/* to atlas */}
        <div style={{ padding: '18px 18px 0' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '13px 15px', background: TH.card, borderRadius: 14, border: `0.8px solid rgba(176,133,58,0.4)` }}>
            <svg width="15" height="15" viewBox="0 0 24 24" fill={TH.gold}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>
            <span style={{ flex: 1, fontFamily: TH.serif, fontSize: 14.5, color: TH.ink, fontWeight: 500, letterSpacing: -0.1 }}>Keep this story in your Atlas</span>
            <span style={{ padding: '7px 13px', background: TH.gold, color: '#fff', borderRadius: 999, fontSize: 11.5, fontWeight: 600 }}>Save →</span>
          </div>
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

Object.assign(window, { TripMap, TripStory });
