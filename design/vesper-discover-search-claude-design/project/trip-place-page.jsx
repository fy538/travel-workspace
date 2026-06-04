// ═══════════════════════════════════════════════════════════════
// INFORMATIONAL PLACE PAGE — "learn more," not just act. Three variants
// of the deep view a block opens into. Reuses TH + Phone/TabBar + StyleRiso.
// ═══════════════════════════════════════════════════════════════

const PlaceBar = () => (
  <div style={{ position: 'absolute', bottom: 0, left: 0, right: 0, padding: '12px 18px 20px', background: 'rgba(247,242,231,0.94)', backdropFilter: 'blur(20px)', borderTop: `0.5px solid ${TH.hair}`, display: 'flex', alignItems: 'center', gap: 12 }}>
    <span style={{ display: 'inline-flex', alignItems: 'center', gap: 6, color: TH.ink, fontSize: 13, fontWeight: 600 }}>
      <svg width="15" height="15" viewBox="0 0 24 24" fill={TH.gold}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg> Ask Vesper
    </span>
    <span style={{ marginLeft: 'auto', display: 'flex', gap: 9 }}>
      <span style={{ padding: '9px 14px', background: TH.card, border: `0.5px solid ${TH.hair}`, borderRadius: 999, fontSize: 12.5, fontWeight: 600, color: TH.soft }}>Move</span>
      <span style={{ padding: '9px 16px', background: TH.blue, color: '#fff', borderRadius: 999, fontSize: 12.5, fontWeight: 600 }}>Book</span>
    </span>
  </div>
);

const Hero = ({ h = 280, kicker, title }) => (
  <div style={{ position: 'relative', height: h }}>
    <div style={{ position: 'absolute', inset: 0 }}><StyleRiso w={393} h={h}/></div>
    <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.32), rgba(20,14,9,0) 36%, rgba(20,14,9,0.74))' }}/>
    <div style={{ position: 'absolute', top: 54, left: 18, width: 38, height: 38, borderRadius: 999, background: 'rgba(255,255,255,0.2)', backdropFilter: 'blur(8px)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
      <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="#fff" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M15 5l-7 7 7 7"/></svg>
    </div>
    <div style={{ position: 'absolute', left: 22, right: 22, bottom: 18 }}>
      <div style={{ fontFamily: TH.mono, fontSize: 9, color: 'rgba(255,255,255,0.82)', letterSpacing: 1.2 }}>{kicker}</div>
      <h1 style={{ fontFamily: TH.serif, fontSize: 31, fontWeight: 500, letterSpacing: -0.6, lineHeight: 1.02, color: '#fff', margin: '5px 0 0' }}>{title}</h1>
    </div>
  </div>
);

// Fact strip — the practical layer.
function Facts({ items }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 0, border: `0.5px solid ${TH.hair}`, borderRadius: 12, overflow: 'hidden' }}>
      {items.map(([k,v],i)=>(
        <div key={k} style={{ padding: '11px 13px', borderTop: i>1?`0.5px solid ${TH.hairThin}`:'none', borderLeft: i%2?`0.5px solid ${TH.hairThin}`:'none' }}>
          <div style={{ fontSize: 8.5, letterSpacing: 1.3, color: TH.faint, fontWeight: 700 }}>{k}</div>
          <div style={{ fontFamily: TH.serif, fontSize: 14, color: TH.ink, fontWeight: 500, marginTop: 3, letterSpacing: -0.1 }}>{v}</div>
        </div>
      ))}
    </div>
  );
}

// P1 · DOSSIER — Vesper's read + thesis + facts. The richest.
function PlaceDossier() {
  return (
    <Phone bg={TH.ink}>
      <div style={{ position: 'absolute', inset: 0, overflow: 'hidden', background: TH.paper }}>
        <Hero kicker="ON YOUR ITINERARY · TUE 21" title="Belém"/>
        <div style={{ padding: '18px 22px 0' }}>
          <div style={{ paddingLeft: 13, borderLeft: `2px solid ${TH.gold}` }}>
            <div style={{ fontSize: 9, letterSpacing: 1.6, fontWeight: 700, color: TH.goldDeep, marginBottom: 5 }}>WHY VESPER PUT THIS HERE</div>
            <p style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 15.5, color: TH.ink, lineHeight: 1.4, margin: 0, letterSpacing: -0.1 }}>Go at 8:30 — the cloister before the tarts, both before the buses.</p>
          </div>
          <p style={{ fontFamily: TH.serif, fontSize: 14.5, color: TH.soft, lineHeight: 1.6, margin: '15px 0 0' }}>The Jerónimos cloister is the reason to come — limestone lacework, quietest at opening. Pastéis de Belém two doors down does the original custard tart; take it at the counter, not the queue.</p>
          <div style={{ marginTop: 15 }}>
            <Facts items={[['BEST','8:30 am'],['HOW LONG','~2 hours'],['GETTING THERE','Tram 15, 20 min'],['COST','€ · tarts €1.40']]}/>
          </div>
        </div>
        <PlaceBar/>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// P2 · GUIDE — practical-first: facts up top, then a short read, then nearby.
function PlaceGuide() {
  return (
    <Phone bg={TH.ink}>
      <div style={{ position: 'absolute', inset: 0, overflow: 'hidden', background: TH.paper }}>
        <Hero h={220} kicker="TUE 21 · MORNING" title="Belém"/>
        <div style={{ padding: '16px 22px 0' }}>
          <Facts items={[['BEST','8:30 am'],['HOW LONG','~2 hours'],['GETTING THERE','Tram 15'],['COST','€']]}/>
          <p style={{ fontFamily: TH.serif, fontSize: 14.5, color: TH.soft, lineHeight: 1.55, margin: '15px 0 0' }}>The cloister is the reason to come; the tarts are the reward. Both quietest right at opening.</p>
          <div style={{ marginTop: 16 }}>
            <div style={{ fontSize: 9, letterSpacing: 1.6, color: TH.mute, fontWeight: 700, marginBottom: 10 }}>NEARBY, IF YOU HAVE TIME</div>
            <div style={{ display: 'flex', gap: 10 }}>
              {[['coast','MAAT museum'],['square','Belém tower']].map(([v,t])=>(
                <div key={t} style={{ flex: 1 }}>
                  <div style={{ height: 64, borderRadius: 9, overflow: 'hidden' }}><StyleRiso w={150} h={64}/></div>
                  <div style={{ fontFamily: TH.serif, fontSize: 13, fontWeight: 500, color: TH.ink, marginTop: 6, letterSpacing: -0.1 }}>{t}</div>
                  <div style={{ fontFamily: TH.mono, fontSize: 8, color: TH.faint, letterSpacing: 0.5, marginTop: 2 }}>6 MIN WALK</div>
                </div>
              ))}
            </div>
          </div>
        </div>
        <PlaceBar/>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// P3 · HALF-SHEET — lighter peek; spine stays visible above. Drags to full.
function PlaceHalfSheet() {
  return (
    <Phone bg={TH.paper}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <RefTopBar/><DateRail/>
        <div style={{ opacity: 0.4, padding: '18px 20px 0' }}>
          <div style={{ display: 'grid', gridTemplateColumns: '50px 1fr', gap: 14 }}>
            <div style={{ textAlign: 'center' }}><div style={{ fontSize: 8, letterSpacing: 1, color: TH.mute, fontWeight: 700 }}>TUE</div><div style={{ fontFamily: TH.serif, fontSize: 30, color: TH.ink }}>21</div></div>
            <div style={{ paddingTop: 6, fontFamily: TH.serif, fontSize: 16, color: TH.ink }}>Belém, early</div>
          </div>
        </div>
        <div style={{ position: 'absolute', inset: 0, top: 250, background: 'rgba(20,14,9,0.26)' }}/>
        <div style={{ position: 'absolute', left: 0, right: 0, bottom: 0, top: 286, background: TH.paper, borderRadius: '22px 22px 0 0', overflow: 'hidden', boxShadow: '0 -18px 44px -18px rgba(0,0,0,0.4)' }}>
          <div style={{ display: 'flex', justifyContent: 'center', paddingTop: 9 }}><div style={{ width: 34, height: 4, borderRadius: 4, background: TH.faint }}/></div>
          <div style={{ height: 104, position: 'relative', margin: '12px 16px 0', borderRadius: 12, overflow: 'hidden' }}>
            <StyleRiso w={361} h={104}/>
            <div style={{ position: 'absolute', left: 13, bottom: 10 }}>
              <span style={{ fontFamily: TH.mono, fontSize: 8.5, color: 'rgba(255,255,255,0.85)', letterSpacing: 1 }}>TUE 21 · MORNING</span>
              <div style={{ fontFamily: TH.serif, fontSize: 21, fontWeight: 500, color: '#fff', letterSpacing: -0.3 }}>Belém</div>
            </div>
          </div>
          <div style={{ padding: '13px 18px' }}>
            <p style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 14.5, color: TH.ink, lineHeight: 1.45, margin: '0 0 12px', letterSpacing: -0.1 }}>The cloister before the tarts — both before the buses.</p>
            <div style={{ display: 'flex', gap: 14, fontFamily: TH.mono, fontSize: 9, color: TH.mute, letterSpacing: 0.5, fontWeight: 600 }}>
              <span>8:30 BEST</span><span>·</span><span>~2 HR</span><span>·</span><span>TRAM 15</span>
            </div>
            <div style={{ marginTop: 13, fontSize: 11, color: TH.faint, fontStyle: 'italic', fontFamily: TH.serif }}>pull up for the full read ↑</div>
          </div>
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

Object.assign(window, { PlaceDossier, PlaceGuide, PlaceHalfSheet });
