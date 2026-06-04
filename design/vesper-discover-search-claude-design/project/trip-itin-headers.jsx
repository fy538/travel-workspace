// ═══════════════════════════════════════════════════════════════
// ITINERARY HEADER VARIATIONS — five takes on the itinerary object's
// top. Each shown over two spine days for context. Reuses TH +
// TripHeader + SpineDay + Block + StyleRiso.
// ═══════════════════════════════════════════════════════════════

// Shared: a tiny preview of the spine under each header.
function SpinePreview() {
  return (
    <div style={{ padding: '16px 20px 0' }}>
      <SpineDay day="SAT" date="18" mo="MAY">
        <Block time="MORNING" title="Land soft, settle in Alfama" sub="bags down, no plans"/>
      </SpineDay>
      <SpineDay day="SUN" date="19" mo="MAY">
        <Block time="DAY" title="Miradouros, east to west" by={{ i: 'A', c: '#7C8F73' }}/>
      </SpineDay>
    </div>
  );
}

// 1 · SPAN MASTHEAD — no photo. The trip names itself by its length.
// A planned-meter shows how full it is. Calmest, most editorial.
function HdrSpan() {
  return (
    <Phone bg={TH.paper}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <TripHeader/>
        <div style={{ padding: '14px 22px 0' }}>
          <div style={{ fontSize: 9.5, letterSpacing: 1.8, color: TH.mute, fontWeight: 700 }}>LISBON, SLOWLY</div>
          <div style={{ display: 'flex', alignItems: 'flex-end', justifyContent: 'space-between', marginTop: 4 }}>
            <h1 style={{ fontFamily: TH.serif, fontSize: 40, fontWeight: 500, letterSpacing: -1, lineHeight: 0.96, color: TH.ink, margin: 0 }}>Six days</h1>
            <span style={{ fontFamily: TH.mono, fontSize: 10, color: TH.mute, letterSpacing: 1, paddingBottom: 6 }}>MAY 18 – 24</span>
          </div>
          {/* planned meter */}
          <div style={{ marginTop: 14, display: 'flex', alignItems: 'center', gap: 10 }}>
            <div style={{ flex: 1, height: 3, borderRadius: 3, background: TH.hair, overflow: 'hidden' }}>
              <div style={{ width: '64%', height: '100%', background: TH.gold }}/>
            </div>
            <span style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 12, color: TH.mute }}>4 of 6 days sketched</span>
          </div>
        </div>
        <div style={{ marginTop: 6 }}><SpinePreview/></div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// 2 · DATE RAIL — the header IS the top of the spine: a tappable week
// strip. No title repeat; the days themselves are the wayfinding.
function HdrRail() {
  const days = [['SAT',18],['SUN',19],['MON',20],['TUE',21],['WED',22],['THU',23]];
  return (
    <Phone bg={TH.paper}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <TripHeader title="Lisbon, slowly" showTitle/>
        <div style={{ padding: '14px 16px 0' }}>
          <div style={{ display: 'flex', gap: 6 }}>
            {days.map(([d, n], i) => (
              <div key={i} style={{ flex: 1, textAlign: 'center', padding: '9px 0 8px', borderRadius: 10, background: i === 0 ? TH.ink : TH.card, border: `0.5px solid ${i === 0 ? 'transparent' : TH.hair}` }}>
                <div style={{ fontSize: 7.5, letterSpacing: 0.8, fontWeight: 700, color: i === 0 ? 'rgba(255,255,255,0.7)' : TH.mute }}>{d}</div>
                <div style={{ fontFamily: TH.serif, fontSize: 17, fontWeight: 500, color: i === 0 ? '#fff' : TH.ink, lineHeight: 1, marginTop: 2 }}>{n}</div>
                {/* planned dot */}
                <div style={{ width: 4, height: 4, borderRadius: 4, margin: '5px auto 0', background: i < 4 ? (i === 0 ? '#E5C16F' : TH.gold) : 'transparent', border: i >= 4 ? `1px solid ${TH.faint}` : 'none' }}/>
              </div>
            ))}
          </div>
        </div>
        <div style={{ marginTop: 4 }}><SpinePreview/></div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// 3 · QUIET BAR — minimal, type-only. Back · place · a planned count.
// The content carries everything; the header nearly disappears.
function HdrQuiet() {
  return (
    <Phone bg={TH.paper}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '12px 20px 14px', borderBottom: `0.5px solid ${TH.hair}` }}>
          <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={TH.soft} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
          <div style={{ textAlign: 'center' }}>
            <div style={{ fontFamily: TH.serif, fontSize: 16, fontWeight: 500, color: TH.ink, letterSpacing: -0.2, lineHeight: 1 }}>Lisbon · six days</div>
            <div style={{ fontFamily: TH.mono, fontSize: 8.5, color: TH.mute, letterSpacing: 1, marginTop: 3 }}>4 SKETCHED · 1 BOOKED</div>
          </div>
          <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={TH.soft} strokeWidth="1.6" strokeLinecap="round"><circle cx="12" cy="5" r="1.4"/><circle cx="12" cy="12" r="1.4"/><circle cx="12" cy="19" r="1.4"/></svg>
        </div>
        <SpinePreview/>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// 4 · BOARDING PASS — a ticket strip. Origin → destination, dates as
// a perforated stub. Tactile, object-like, a little playful.
function HdrTicket() {
  return (
    <Phone bg={TH.paper}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <TripHeader/>
        <div style={{ padding: '14px 18px 0' }}>
          <div style={{ background: TH.card, borderRadius: 14, border: `0.5px solid ${TH.hair}`, padding: '14px 16px', position: 'relative', boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset' }}>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
              <div>
                <div style={{ fontFamily: TH.mono, fontSize: 9, color: TH.mute, letterSpacing: 1 }}>NYC</div>
                <div style={{ fontFamily: TH.serif, fontSize: 22, fontWeight: 500, color: TH.ink, lineHeight: 1 }}>New York</div>
              </div>
              <div style={{ flex: 1, position: 'relative', margin: '0 14px', height: 1, borderTop: `1px dashed ${TH.faint}` }}>
                <svg width="14" height="14" viewBox="0 0 24 24" fill={TH.gold} style={{ position: 'absolute', top: -7, left: '50%', transform: 'translateX(-50%)' }}><path d="M2 12l7-1 4-8 2 0-2 8 6 1-6 1 2 8-2 0-4-8z"/></svg>
              </div>
              <div style={{ textAlign: 'right' }}>
                <div style={{ fontFamily: TH.mono, fontSize: 9, color: TH.goldDeep, letterSpacing: 1 }}>LIS</div>
                <div style={{ fontFamily: TH.serif, fontSize: 22, fontWeight: 500, color: TH.ink, lineHeight: 1 }}>Lisbon</div>
              </div>
            </div>
            {/* perforation */}
            <div style={{ margin: '13px -16px', borderTop: `1px dashed ${TH.faint}`, position: 'relative' }}>
              <div style={{ position: 'absolute', left: -6, top: -6, width: 12, height: 12, borderRadius: 999, background: TH.paper }}/>
              <div style={{ position: 'absolute', right: -6, top: -6, width: 12, height: 12, borderRadius: 999, background: TH.paper }}/>
            </div>
            <div style={{ display: 'flex', justifyContent: 'space-between' }}>
              {[['DATES','May 18 – 24'],['NIGHTS','6'],['PARTY','3']].map(([k,v])=>(
                <div key={k}><div style={{ fontSize: 8, letterSpacing: 1.2, color: TH.mute, fontWeight: 700 }}>{k}</div><div style={{ fontFamily: TH.serif, fontSize: 14, color: TH.ink, fontWeight: 500, marginTop: 2 }}>{v}</div></div>
              ))}
            </div>
          </div>
        </div>
        <div style={{ marginTop: 2 }}><SpinePreview/></div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// 5 · FOLIO TAB — a folder/chapter tab. The itinerary is one chapter
// of the trip folio; the tab names the section in serif, paper-on-paper.
function HdrFolioTab() {
  return (
    <Phone bg={TH.paper}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <TripHeader title="Lisbon, slowly" showTitle/>
        <div style={{ padding: '16px 0 0' }}>
          {/* chapter tabs */}
          <div style={{ display: 'flex', gap: 0, padding: '0 20px', alignItems: 'flex-end' }}>
            {['The Days', 'Map', 'Costs', 'Story'].map((t, i) => (
              <div key={t} style={{ padding: i === 0 ? '9px 15px' : '7px 13px', background: i === 0 ? TH.card : 'transparent', borderRadius: '10px 10px 0 0', border: i === 0 ? `0.5px solid ${TH.hair}` : 'none', borderBottom: 'none', marginBottom: i === 0 ? -0.5 : 0 }}>
                <span style={{ fontFamily: TH.serif, fontSize: i === 0 ? 15 : 13.5, fontStyle: i === 0 ? 'normal' : 'italic', fontWeight: i === 0 ? 500 : 400, color: i === 0 ? TH.ink : TH.mute, letterSpacing: -0.2 }}>{t}</span>
              </div>
            ))}
          </div>
          <div style={{ borderTop: `0.5px solid ${TH.hair}` }}/>
        </div>
        <SpinePreview/>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

Object.assign(window, { HdrSpan, HdrRail, HdrQuiet, HdrTicket, HdrFolioTab });
