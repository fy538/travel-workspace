// ═══════════════════════════════════════════════════════════════
// ITINERARY · REFINED — changes 1-4:
//  1. no banner; group changes become per-day dots on the rail
//  2. subtle past (same blocks, gently de-emphasized — one continuous spine)
//  3. Day/Map as a single top-right icon (not a toggle)
//  4. collapse/expand icon → compact daily index ⇄ full spine
// Reuses TH + Phone/TabBar + StyleRiso.
// ═══════════════════════════════════════════════════════════════

// Top bar: back · date-rail/title · [collapse] [map] icons.
function RefTopBar({ collapsed }) {
  const ico = (d, fill) => <svg width="20" height="20" viewBox="0 0 24 24" fill={fill||'none'} stroke={TH.soft} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">{d}</svg>;
  return (
    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '12px 16px 0' }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 5 }}>
        {ico(<path d="M14 6l-6 6 6 6"/>)}
        <span style={{ fontFamily: TH.serif, fontSize: 16, fontWeight: 500, color: TH.ink, letterSpacing: -0.2 }}>Lisbon, slowly</span>
      </div>
      <div style={{ display: 'flex', gap: 14 }}>
        {/* collapse / expand */}
        {collapsed
          ? ico(<><path d="M4 7h16M4 12h16M4 17h16"/></>)
          : ico(<><path d="M4 6h16M4 12h10M4 18h16"/><path d="M18 10l3 2-3 2"/></>)}
        {/* map */}
        {ico(<><path d="M9 4 L3 6.5 V20 L9 17.5 L15 20 L21 17.5 V4 L15 6.5 L9 4Z"/><path d="M9 4v13.5M15 6.5V20"/></>)}
      </div>
    </div>
  );
}

// Date rail — per-day change dots (ink-blue) signal pending group edits.
function DateRail({ activeIdx = 2 }) {
  const days = [['SAT',18,{planned:true}],['SUN',19,{planned:true}],['MON',20,{planned:true,today:true}],['TUE',21,{planned:true,change:true}],['WED',22,{change:true}],['THU',23,{}]];
  return (
    <div style={{ padding: '12px 16px 4px' }}>
      <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginBottom: 11, padding: '0 2px' }}>
        <span style={{ fontSize: 9, letterSpacing: 1.8, color: TH.mute, fontWeight: 700 }}>MAY · DAY 3 OF 6</span>
        <span style={{ display: 'inline-flex', alignItems: 'center', gap: 5, fontFamily: TH.serif, fontStyle: 'italic', fontSize: 11.5, color: TH.blue }}>
          <span style={{ width: 5, height: 5, borderRadius: 5, background: TH.blue }}/> 2 days have changes
        </span>
      </div>
      <div style={{ display: 'flex', gap: 6 }}>
        {days.map(([d,n,f],i)=>{
          const on = f.today;
          return (
            <div key={i} style={{ flex: 1, textAlign: 'center', padding: '9px 0 8px', borderRadius: 11, background: on?TH.ink:TH.card, border: `0.5px solid ${on?'transparent':TH.hair}`, boxShadow: on?'0 4px 12px -6px rgba(27,23,20,0.4)':'none', position: 'relative' }}>
              <div style={{ fontSize: 7, letterSpacing: 0.6, fontWeight: 700, color: on?'rgba(255,255,255,0.65)':TH.faint }}>{d}</div>
              <div style={{ fontFamily: TH.serif, fontSize: 17, fontWeight: 500, color: on?'#fff':f.planned?TH.ink:TH.faint, lineHeight: 1, marginTop: 3 }}>{n}</div>
              <div style={{ width: 4, height: 4, borderRadius: 4, margin: '6px auto 0', background: f.planned?(on?'#E5C16F':TH.gold):'transparent', border: f.planned?'none':`1px solid ${TH.faint}` }}/>
              {/* change dot */}
              {f.change && <span style={{ position: 'absolute', top: 5, right: 7, width: 6, height: 6, borderRadius: 6, background: TH.blue, border: `1.4px solid ${TH.paper}`, boxSizing: 'content-box' }}/>}
            </div>
          );
        })}
      </div>
    </div>
  );
}

// Refined block — one type, `dim` for past, no special past layout.
function RBlock({ time, title, sub, state, dim, done, skip, recent, by, last, onTap }) {
  const dot = state==='now'?TH.gold:state==='booked'?TH.blue:state==='gap'?'transparent':done?TH.faint:TH.soft;
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '16px 1fr', gap: 15, opacity: dim?0.5:1, cursor: onTap?'pointer':'default' }}>
      <div style={{ display: 'flex', justifyContent: 'center', position: 'relative' }}>
        {!last && <span style={{ position: 'absolute', top: 14, bottom: -8, width: 1, background: TH.hairThin }}/>}
        {done
          ? <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke={TH.faint} strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round" style={{ marginTop: 5, zIndex: 1, background: TH.paper }}><path d="M4 12l5 5L20 6"/></svg>
          : <span style={{ width: state==='now'?10:7, height: state==='now'?10:7, borderRadius: 999, marginTop: 7, background: dot, border: state==='gap'?`1.2px dashed ${TH.faint}`:'none', boxShadow: state==='now'?'0 0 0 4px rgba(176,133,58,0.18)':'none', zIndex: 1 }}/>}
      </div>
      <div style={{ paddingBottom: last?2:22, position: 'relative' }}>
        {recent && <span style={{ position: 'absolute', left: -15, top: 5, bottom: 12, width: 2, borderRadius: 2, background: TH.gold }}/>}
        <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 5 }}>
          <span style={{ fontFamily: TH.mono, fontSize: 8.5, color: state==='now'?TH.goldDeep:TH.mute, letterSpacing: 1.4, fontWeight: 600 }}>{time}</span>
          {state==='now' && <span style={{ fontSize: 7.5, letterSpacing: 1.2, fontWeight: 700, color: TH.goldDeep }}>NOW</span>}
          {state==='booked' && <span style={{ fontSize: 7.5, letterSpacing: 1.2, fontWeight: 700, color: TH.blue }}>BOOKED</span>}
          {recent && <span style={{ fontSize: 7.5, letterSpacing: 1, fontWeight: 700, color: TH.goldDeep, background: 'rgba(176,133,58,0.14)', padding: '1px 5px', borderRadius: 4 }}>NEW</span>}
        </div>
        <div style={{ fontFamily: TH.serif, fontSize: state==='gap'?14.5:16.5, fontStyle: state==='gap'?'italic':'normal', fontWeight: state==='gap'?400:500, color: state==='gap'?TH.mute:TH.ink, letterSpacing: -0.2, lineHeight: 1.25, textDecoration: skip?'line-through':'none', textDecorationColor: skip?TH.faint:'inherit', textDecorationThickness: '1px' }}>{title}</div>
        {sub && <div style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 12.5, color: TH.mute, marginTop: 4, lineHeight: 1.35 }}>{sub}</div>}
        {by && <div style={{ marginTop: 8, display: 'inline-flex', alignItems: 'center', gap: 6 }}><span style={{ width: 16, height: 16, borderRadius: 999, background: by.c, color: '#fff', fontFamily: TH.serif, fontSize: 8.5, fontWeight: 500, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>{by.i}</span><span style={{ fontSize: 9.5, color: TH.mute, fontStyle: 'italic', fontFamily: TH.serif }}>{by.n} · {by.ago}</span></div>}
      </div>
    </div>
  );
}

function RDay({ day, date, weather, today, dim, divider, children }) {
  return (
    <div style={{ marginBottom: 8 }}>
      {divider && <div style={{ height: 0.5, background: TH.hairThin, margin: '0 0 22px' }}/>}
      <div style={{ display: 'grid', gridTemplateColumns: '50px 1fr', gap: 14 }}>
        <div style={{ textAlign: 'center', paddingTop: 2, opacity: dim?0.5:1 }}>
          <div style={{ fontSize: 8, letterSpacing: 1, color: today?TH.goldDeep:TH.mute, fontWeight: 700 }}>{day}</div>
          <div style={{ fontFamily: TH.serif, fontSize: 30, fontWeight: 500, color: today?TH.gold:TH.ink, lineHeight: 0.9, fontVariantNumeric: 'oldstyle-nums', marginTop: 3 }}>{date}</div>
          {weather && <div style={{ fontFamily: TH.mono, fontSize: 8, color: TH.faint, marginTop: 8 }}>{weather}</div>}
          {today && <div style={{ width: 4, height: 4, borderRadius: 4, background: TH.gold, margin: '8px auto 0' }}/>}
        </div>
        <div style={{ paddingTop: 6 }}>{children}</div>
      </div>
    </div>
  );
}

// FULL refined spine — past subtle (same blocks), today live, future plannable.
function ItinRefinedFull() {
  return (
    <Phone bg={TH.paper}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <RefTopBar/>
        <DateRail/>
        <div style={{ padding: '18px 22px 0' }}>
          {/* past — same layout, just dim + done/skip marks */}
          <RDay day="SUN" date="19" dim>
            <RBlock time="MORNING" title="Miradouros, east to west" done/>
            <RBlock time="LUNCH" title="Skipped — you kept walking" skip done last/>
          </RDay>
          {/* today */}
          <RDay day="MON" date="20" weather="18°" today divider>
            <RBlock time="9:30" title="Coffee at Kayaba" done/>
            <RBlock time="NOW · 10:14" title="Cemetery walk, the slow way" state="now"/>
            <RBlock time="21:00" title="Fado, the quiet room" state="booked" last/>
          </RDay>
          {/* future */}
          <RDay day="TUE" date="21" divider>
            <RBlock time="MORNING" title="Belém, early" sub="beat the crowd" recent by={{ i:'A', c:'#7C8F73', n:'Ana added', ago:'2h' }}/>
            <RBlock time="OPEN" title="this afternoon is bare — sketch it?" state="gap" last/>
          </RDay>
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// COLLAPSED daily index — each day one line; tap a day to expand it.
function ItinCollapsed() {
  const days = [
    { day:'SAT', date:18, sum:'Alfama, the long first walk', n:'3 stops', dim:true },
    { day:'SUN', date:19, sum:'Miradouros east to west', n:'4 stops', dim:true },
    { day:'MON', date:20, sum:'Cemetery walk · fado tonight', n:'3 stops', today:true, open:true },
    { day:'TUE', date:21, sum:'Belém, then open', n:'2 stops', change:true },
    { day:'WED', date:22, sum:'—', n:'empty', change:true },
    { day:'THU', date:23, sum:'—', n:'empty' },
  ];
  return (
    <Phone bg={TH.paper}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <RefTopBar collapsed/>
        <div style={{ padding: '16px 18px 0', display: 'flex', flexDirection: 'column', gap: 2 }}>
          {days.map((d,i)=>(
            <div key={i}>
              <div style={{ display: 'grid', gridTemplateColumns: '40px 1fr auto', gap: 12, alignItems: 'center', padding: '11px 4px', borderTop: i?`0.5px solid ${TH.hairThin}`:'none', opacity: d.dim?0.55:1 }}>
                <div style={{ textAlign: 'center' }}>
                  <div style={{ fontSize: 7.5, letterSpacing: 1, color: d.today?TH.goldDeep:TH.mute, fontWeight: 700 }}>{d.day}</div>
                  <div style={{ fontFamily: TH.serif, fontSize: 21, fontWeight: 500, color: d.today?TH.gold:TH.ink, lineHeight: 0.95, fontVariantNumeric: 'oldstyle-nums' }}>{d.date}</div>
                </div>
                <div>
                  <div style={{ fontFamily: TH.serif, fontSize: 14.5, fontWeight: 500, color: d.sum==='—'?TH.faint:TH.ink, fontStyle: d.sum==='—'?'italic':'normal', letterSpacing: -0.15, lineHeight: 1.2 }}>{d.sum==='—'?'open day':d.sum}</div>
                  <div style={{ fontFamily: TH.mono, fontSize: 8.5, color: TH.faint, letterSpacing: 0.5, marginTop: 3 }}>{d.n.toUpperCase()}</div>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: 7 }}>
                  {d.change && <span style={{ width: 6, height: 6, borderRadius: 6, background: TH.blue }}/>}
                  <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke={TH.faint} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ transform: d.open?'rotate(180deg)':'none' }}><path d="M6 9l6 6 6-6"/></svg>
                </div>
              </div>
              {/* expanded day inline */}
              {d.open && (
                <div style={{ padding: '4px 4px 12px 52px' }}>
                  <RBlock time="9:30" title="Coffee at Kayaba" done/>
                  <RBlock time="NOW" title="Cemetery walk" state="now"/>
                  <RBlock time="21:00" title="Fado, the quiet room" state="booked" last/>
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

Object.assign(window, { RefTopBar, DateRail, RBlock, RDay, ItinRefinedFull, ItinCollapsed });
