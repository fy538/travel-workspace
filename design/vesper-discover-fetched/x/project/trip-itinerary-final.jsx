// ═══════════════════════════════════════════════════════════════
// POLISHED ITINERARY — the spine design, refined, with three CONTEXTUAL
// headers that swap by situation:
//   · Date Rail   — a multi-day trip (wayfinding across days)
//   · Quiet Bar   — a single-day trip (header nearly disappears)
//   · Ticket band — 24h before a flight/train (sits ATOP the spine)
// Reuses TH + TripHeader + StyleRiso.
// ═══════════════════════════════════════════════════════════════

// ── Polished block — a moment on the day. Cleaner rhythm, booked/now/gap.
function PBlock({ time, title, sub, by, state, last }) {
  const dot = state === 'now' ? TH.gold : state === 'booked' ? TH.blue : state === 'gap' ? 'transparent' : TH.soft;
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '15px 1fr', gap: 13 }}>
      {/* spine + node */}
      <div style={{ display: 'flex', justifyContent: 'center', position: 'relative' }}>
        {!last && <span style={{ position: 'absolute', top: 11, bottom: -2, width: 1, background: TH.hairThin }}/>}
        <span style={{
          width: state === 'now' ? 9 : 6.5, height: state === 'now' ? 9 : 6.5, borderRadius: 999, marginTop: 6,
          background: dot, border: state === 'gap' ? `1.2px dashed ${TH.faint}` : 'none',
          boxShadow: state === 'now' ? '0 0 0 4px rgba(176,133,58,0.18)' : 'none', zIndex: 1,
        }}/>
      </div>
      <div style={{ paddingBottom: last ? 2 : 18 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 7 }}>
          <span style={{ fontFamily: TH.mono, fontSize: 8.5, color: state === 'now' ? TH.goldDeep : TH.mute, letterSpacing: 1.2, fontWeight: 600 }}>{time}</span>
          {state === 'now' && <span style={{ fontSize: 7.5, letterSpacing: 1.2, fontWeight: 700, color: TH.goldDeep }}>NOW</span>}
          {state === 'booked' && <span style={{ fontSize: 7.5, letterSpacing: 1.2, fontWeight: 700, color: TH.blue }}>BOOKED</span>}
        </div>
        <div style={{ fontFamily: TH.serif, fontSize: state === 'gap' ? 14 : 16, fontStyle: state === 'gap' ? 'italic' : 'normal', fontWeight: state === 'gap' ? 400 : 500, color: state === 'gap' ? TH.mute : TH.ink, letterSpacing: -0.2, lineHeight: 1.2, marginTop: 3 }}>{title}</div>
        {sub && <div style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 12, color: TH.mute, marginTop: 3, lineHeight: 1.3 }}>{sub}</div>}
        {by && <div style={{ marginTop: 7, display: 'inline-flex', alignItems: 'center', gap: 5 }}>
          <span style={{ width: 16, height: 16, borderRadius: 999, background: by.c, color: '#fff', fontFamily: TH.serif, fontSize: 8.5, fontWeight: 500, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>{by.i}</span>
          <span style={{ fontSize: 10, color: TH.mute, fontStyle: 'italic', fontFamily: TH.serif }}>{by.n} added this</span>
        </div>}
      </div>
    </div>
  );
}

// ── Polished day — big date numeral anchoring the day's blocks.
function PDay({ day, date, mo, weather, today, children }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '46px 1fr', gap: 12, marginBottom: 4 }}>
      <div style={{ textAlign: 'center', paddingTop: 1 }}>
        <div style={{ fontSize: 8, letterSpacing: 1, color: today ? TH.goldDeep : TH.mute, fontWeight: 700 }}>{day}</div>
        <div style={{ fontFamily: TH.serif, fontSize: 30, fontWeight: 500, color: today ? TH.gold : TH.ink, lineHeight: 0.9, fontVariantNumeric: 'oldstyle-nums', letterSpacing: -0.5, marginTop: 2 }}>{date}</div>
        <div style={{ fontSize: 7.5, letterSpacing: 1, color: TH.faint, fontWeight: 700, marginTop: 3 }}>{mo}</div>
        {weather && <div style={{ marginTop: 7, fontFamily: TH.mono, fontSize: 8, color: TH.faint }}>{weather}</div>}
      </div>
      <div style={{ paddingTop: 5 }}>{children}</div>
    </div>
  );
}

// ── The full multi-day spine (shared body). dayIdx flags "today".
function FullSpine({ today = -1 }) {
  return (
    <div style={{ padding: '8px 20px 0' }}>
      <PDay day="MON" date="20" mo="MAY" weather="18°" today={today === 0}>
        <PBlock time="MORNING" title="Coffee at Kayaba, cemetery walk" sub="8 min east, the slow way" state={today === 0 ? 'now' : ''}/>
        <PBlock time="MIDDAY" title="Miradouros, east to west" by={{ i: 'A', c: '#7C8F73', n: 'Ana' }}/>
        <PBlock time="21:00" title="Fado, the quiet room" sub="two seats held" state="booked" last/>
      </PDay>
      <PDay day="TUE" date="21" mo="MAY" weather="20°">
        <PBlock time="MORNING" title="Belém, early to beat the crowd"/>
        <PBlock time="OPEN" title="this afternoon is bare — sketch it?" state="gap" last/>
      </PDay>
    </div>
  );
}

// ─────────────────────────────────────────────────────────────
// HEADER 1 · DATE RAIL — multi-day. Polished: month label, refined
// chips, a thin planned-meter under the rail.
function ItinRailHeader() {
  const days = [['MON',20],['TUE',21],['WED',22],['THU',23],['FRI',24],['SAT',25]];
  return (
    <Phone bg={TH.paper}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <TripHeader title="Lisbon, slowly" showTitle/>
        <div style={{ padding: '12px 18px 0' }}>
          <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginBottom: 9, padding: '0 2px' }}>
            <span style={{ fontSize: 9, letterSpacing: 1.8, color: TH.mute, fontWeight: 700 }}>MAY · DAY 1 OF 6</span>
            <span style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 11.5, color: TH.mute }}>4 days sketched</span>
          </div>
          <div style={{ display: 'flex', gap: 5 }}>
            {days.map(([d, n], i) => {
              const on = i === 0, planned = i < 4;
              return (
                <div key={i} style={{ flex: 1, textAlign: 'center', padding: '8px 0 7px', borderRadius: 11, background: on ? TH.ink : TH.card, border: `0.5px solid ${on ? 'transparent' : TH.hair}`, boxShadow: on ? '0 4px 12px -6px rgba(27,23,20,0.4)' : 'none' }}>
                  <div style={{ fontSize: 7, letterSpacing: 0.6, fontWeight: 700, color: on ? 'rgba(255,255,255,0.65)' : TH.faint }}>{d}</div>
                  <div style={{ fontFamily: TH.serif, fontSize: 17, fontWeight: 500, color: on ? '#fff' : planned ? TH.ink : TH.faint, lineHeight: 1, marginTop: 2 }}>{n}</div>
                  <div style={{ width: 4, height: 4, borderRadius: 4, margin: '5px auto 0', background: planned ? (on ? '#E5C16F' : TH.gold) : 'transparent', border: planned ? 'none' : `1px solid ${TH.faint}` }}/>
                </div>
              );
            })}
          </div>
        </div>
        <div style={{ marginTop: 8 }}><FullSpine today={0}/></div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// HEADER 2 · QUIET BAR — single-day trip. Header nearly disappears;
// the one day is the whole screen.
function ItinQuietHeader() {
  return (
    <Phone bg={TH.paper}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '12px 20px 13px', borderBottom: `0.5px solid ${TH.hair}` }}>
          <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={TH.soft} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
          <div style={{ textAlign: 'center' }}>
            <div style={{ fontFamily: TH.serif, fontSize: 16, fontWeight: 500, color: TH.ink, letterSpacing: -0.2, lineHeight: 1 }}>A day in Sintra</div>
            <div style={{ fontFamily: TH.mono, fontSize: 8.5, color: TH.mute, letterSpacing: 1, marginTop: 3 }}>SAT · MAY 25 · ONE DAY</div>
          </div>
          <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={TH.soft} strokeWidth="1.6" strokeLinecap="round"><circle cx="12" cy="5" r="1.4"/><circle cx="12" cy="12" r="1.4"/><circle cx="12" cy="19" r="1.4"/></svg>
        </div>
        {/* a single rich day, no date column needed */}
        <div style={{ padding: '20px 24px 0' }}>
          <div style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 14, color: TH.mute, marginBottom: 16, lineHeight: 1.4 }}>
            One palace, the garden everyone skips, home by dark.
          </div>
          {[['08:40','Train from Rossio','40 min, sit left for the view','booked'],
            ['10:00','Quinta da Regaleira','go straight for the well',''],
            ['13:30','Lunch in the old town','Tascantiga, the petiscos',''],
            ['16:00','Pena, late, fewer crowds','',''],
            ['19:10','Last train back','',  'booked']].map(([tm,t,s,st],i,a)=>(
            <PBlock key={i} time={tm} title={t} sub={s} state={st} last={i===a.length-1}/>
          ))}
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// HEADER 3 · TICKET BAND — 24h before a flight/train. A live boarding
// pass sits ATOP the normal spine, then dissolves once you've travelled.
function ItinTicketBand() {
  return (
    <Phone bg={TH.paper}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <TripHeader title="Lisbon, slowly" showTitle/>
        {/* the live ticket */}
        <div style={{ padding: '12px 18px 0' }}>
          <div style={{ position: 'relative', background: TH.ink, borderRadius: 16, padding: '15px 17px', overflow: 'hidden' }}>
            {/* faint riso texture on the dark stub */}
            <div style={{ position: 'absolute', inset: 0, opacity: 0.16 }}><StyleRiso w={357} h={150}/></div>
            <div style={{ position: 'relative' }}>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                <span style={{ display: 'inline-flex', alignItems: 'center', gap: 6, padding: '3px 9px', borderRadius: 999, background: 'rgba(229,193,111,0.2)', fontSize: 8.5, letterSpacing: 1.4, fontWeight: 700, color: '#E5C16F' }}>
                  <span style={{ width: 5, height: 5, borderRadius: 5, background: '#E5C16F' }}/> TOMORROW · 14:05
                </span>
                <span style={{ fontFamily: TH.mono, fontSize: 9, color: 'rgba(255,255,255,0.6)', letterSpacing: 1 }}>TP 209 · GATE 22</span>
              </div>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginTop: 14 }}>
                <div><div style={{ fontFamily: TH.mono, fontSize: 9, color: 'rgba(255,255,255,0.55)', letterSpacing: 1 }}>JFK</div><div style={{ fontFamily: TH.serif, fontSize: 23, fontWeight: 500, color: '#fff', lineHeight: 1 }}>New York</div></div>
                <div style={{ flex: 1, margin: '0 14px', position: 'relative', height: 1, borderTop: '1px dashed rgba(255,255,255,0.3)' }}>
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="#E5C16F" style={{ position: 'absolute', top: -7, left: '50%', transform: 'translateX(-50%)' }}><path d="M2 12l7-1 4-8 2 0-2 8 6 1-6 1 2 8-2 0-4-8z"/></svg>
                </div>
                <div style={{ textAlign: 'right' }}><div style={{ fontFamily: TH.mono, fontSize: 9, color: '#E5C16F', letterSpacing: 1 }}>LIS</div><div style={{ fontFamily: TH.serif, fontSize: 23, fontWeight: 500, color: '#fff', lineHeight: 1 }}>Lisbon</div></div>
              </div>
              <div style={{ marginTop: 13, paddingTop: 11, borderTop: '1px dashed rgba(255,255,255,0.2)', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                <span style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 12.5, color: 'rgba(255,255,255,0.8)' }}>Vesper checked you in · seat 14A</span>
                <span style={{ fontSize: 11, color: '#E5C16F', fontWeight: 600 }}>Pass →</span>
              </div>
            </div>
          </div>
        </div>
        {/* the spine resumes below, dimmed slightly so the ticket leads */}
        <div style={{ padding: '14px 0 0', opacity: 0.9 }}>
          <div style={{ padding: '0 22px 6px' }}><span style={{ fontSize: 9, letterSpacing: 1.8, color: TH.mute, fontWeight: 700 }}>AND THEN — YOUR FIRST DAY</span></div>
          <div style={{ padding: '0 20px' }}>
            <PDay day="MON" date="20" mo="MAY" weather="18°">
              <PBlock time="EVENING" title="Land soft, settle in Alfama" sub="bags down, no plans" last/>
            </PDay>
          </div>
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

Object.assign(window, { PBlock, PDay, FullSpine, ItinRailHeader, ItinQuietHeader, ItinTicketBand });
