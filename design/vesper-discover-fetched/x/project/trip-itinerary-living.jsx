// ═══════════════════════════════════════════════════════════════
// ITINERARY · LIVING LAYER — three additions to the spine:
//   1. Tense spine — past diary → today live → future plannable
//   2. Block-tap sheets — future / past / propose-change→Vesper diff
//   3. Group activity — recently-added tags, ghost proposals, review ribbon
// Top chrome stripped to back + Days/Map toggle only.
// Reuses TH + Phone/TabBar + StyleRiso + PBlock/PDay where useful.
// ═══════════════════════════════════════════════════════════════

// ── Stripped header: back · title · Days/Map toggle (no gear/chat).
function ItinTopBar({ title = 'Lisbon, slowly', face = 'days' }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '12px 16px 0' }}>
      <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={TH.soft} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
      <span style={{ fontFamily: TH.serif, fontSize: 16, fontWeight: 500, color: TH.ink, letterSpacing: -0.2 }}>{title}</span>
      <div style={{ display: 'inline-flex', background: 'rgba(27,23,20,0.06)', borderRadius: 999, padding: 2.5 }}>
        {['Days','Map'].map(t=>{const on=t.toLowerCase()===face;return <span key={t} style={{ padding: '4px 11px', borderRadius: 999, fontSize: 11, fontWeight: on?600:500, color: on?TH.ink:TH.mute, background: on?TH.card:'transparent', boxShadow: on?'0 1px 2px rgba(0,0,0,0.08)':'none' }}>{t}</span>;})}
      </div>
    </div>
  );
}

// ── Review ribbon — the itinerary's own notifications, scoped to the plan.
function ReviewRibbon() {
  return (
    <div style={{ margin: '12px 16px 0', display: 'flex', alignItems: 'center', gap: 10, padding: '9px 13px', background: 'rgba(176,133,58,0.09)', borderRadius: 11, border: `0.6px solid rgba(176,133,58,0.32)` }}>
      <div style={{ display: 'flex' }}>
        {[['A','#7C8F73'],['T','#A0703A']].map(([i,c],k)=><span key={k} style={{ width: 19, height: 19, borderRadius: 999, background: c, color: '#fff', fontFamily: TH.serif, fontSize: 9.5, fontWeight: 500, display: 'flex', alignItems: 'center', justifyContent: 'center', marginLeft: k?-6:0, border: `1.5px solid ${TH.paper}` }}>{i}</span>)}
      </div>
      <span style={{ flex: 1, fontFamily: TH.serif, fontSize: 13, color: TH.ink, letterSpacing: -0.1 }}>3 changes since you looked</span>
      <span style={{ fontSize: 10.5, color: TH.goldDeep, fontWeight: 700, letterSpacing: 0.3 }}>REVIEW</span>
    </div>
  );
}

// ── Past day, compressed to a diary line with a thin arc + photo count.
function PastDay({ day, date, summary, photos }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '46px 1fr', gap: 12, opacity: 0.78, padding: '7px 0' }}>
      <div style={{ textAlign: 'center' }}>
        <div style={{ fontSize: 8, letterSpacing: 1, color: TH.faint, fontWeight: 700 }}>{day}</div>
        <div style={{ fontFamily: TH.serif, fontSize: 22, fontWeight: 500, color: TH.mute, lineHeight: 0.9, fontVariantNumeric: 'oldstyle-nums', marginTop: 2 }}>{date}</div>
      </div>
      <div style={{ paddingTop: 3, display: 'flex', alignItems: 'center', gap: 8 }}>
        <svg width="22" height="10" viewBox="0 0 22 10" style={{ flexShrink: 0 }}><path d="M1 8 Q8 2 21 4" stroke={TH.gold} strokeWidth="1.2" fill="none" opacity="0.6"/></svg>
        <span style={{ flex: 1, fontFamily: TH.serif, fontStyle: 'italic', fontSize: 13, color: TH.soft, letterSpacing: -0.05, lineHeight: 1.3 }}>{summary}</span>
        {photos && <span style={{ fontFamily: TH.mono, fontSize: 8.5, color: TH.faint, letterSpacing: 0.5, fontWeight: 600 }}>{photos}◷</span>}
      </div>
    </div>
  );
}

// ── A living block — supports recency tag + ghost-proposal + states.
function LiveBlock({ time, title, sub, state, recent, by, ghost, proposer, last }) {
  if (ghost) {
    return (
      <div style={{ display: 'grid', gridTemplateColumns: '15px 1fr', gap: 13 }}>
        <div style={{ display: 'flex', justifyContent: 'center', position: 'relative' }}>
          {!last && <span style={{ position: 'absolute', top: 11, bottom: -2, width: 1, background: TH.hairThin }}/>}
          <span style={{ width: 7, height: 7, borderRadius: 999, marginTop: 6, background: 'transparent', border: `1.4px dashed ${TH.blue}`, zIndex: 1 }}/>
        </div>
        <div style={{ paddingBottom: last?2:16 }}>
          <div style={{ padding: '10px 12px', borderRadius: 11, border: `1px dashed ${TH.blue}`, background: 'rgba(61,80,102,0.05)' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
              <span style={{ width: 15, height: 15, borderRadius: 999, background: proposer.c, color: '#fff', fontFamily: TH.serif, fontSize: 8, fontWeight: 500, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>{proposer.i}</span>
              <span style={{ fontSize: 8.5, letterSpacing: 1, fontWeight: 700, color: TH.blueDeep }}>{proposer.n.toUpperCase()} PROPOSES</span>
            </div>
            <div style={{ fontFamily: TH.serif, fontSize: 14.5, color: TH.ink, fontWeight: 500, letterSpacing: -0.2, marginTop: 6 }}>{title}</div>
            {sub && <div style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 11.5, color: TH.mute, marginTop: 2 }}>{sub}</div>}
            <div style={{ marginTop: 9, display: 'flex', gap: 7 }}>
              <span style={{ flex: 1, textAlign: 'center', padding: '6px 0', background: TH.blue, color: '#fff', borderRadius: 999, fontSize: 11, fontWeight: 600 }}>Approve</span>
              <span style={{ flex: 1, textAlign: 'center', padding: '6px 0', background: TH.card, color: TH.soft, border: `0.5px solid ${TH.hair}`, borderRadius: 999, fontSize: 11, fontWeight: 600 }}>Keep current</span>
            </div>
          </div>
        </div>
      </div>
    );
  }
  const dot = state==='now'?TH.gold:state==='booked'?TH.blue:state==='gap'?'transparent':TH.soft;
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '15px 1fr', gap: 13 }}>
      <div style={{ display: 'flex', justifyContent: 'center', position: 'relative' }}>
        {!last && <span style={{ position: 'absolute', top: 11, bottom: -2, width: 1, background: TH.hairThin }}/>}
        <span style={{ width: state==='now'?9:6.5, height: state==='now'?9:6.5, borderRadius: 999, marginTop: 6, background: dot, border: state==='gap'?`1.2px dashed ${TH.faint}`:'none', boxShadow: state==='now'?'0 0 0 4px rgba(176,133,58,0.18)':'none', zIndex: 1 }}/>
      </div>
      <div style={{ paddingBottom: last?2:16, position: 'relative' }}>
        {recent && <span style={{ position: 'absolute', left: -13, top: 4, bottom: 8, width: 2, borderRadius: 2, background: TH.gold }}/>}
        <div style={{ display: 'flex', alignItems: 'center', gap: 7 }}>
          <span style={{ fontFamily: TH.mono, fontSize: 8.5, color: state==='now'?TH.goldDeep:TH.mute, letterSpacing: 1.2, fontWeight: 600 }}>{time}</span>
          {state==='now' && <span style={{ fontSize: 7.5, letterSpacing: 1.2, fontWeight: 700, color: TH.goldDeep }}>NOW</span>}
          {state==='booked' && <span style={{ fontSize: 7.5, letterSpacing: 1.2, fontWeight: 700, color: TH.blue }}>BOOKED</span>}
          {recent && <span style={{ fontSize: 7.5, letterSpacing: 1, fontWeight: 700, color: TH.goldDeep, background: 'rgba(176,133,58,0.14)', padding: '1px 5px', borderRadius: 4 }}>NEW</span>}
        </div>
        <div style={{ fontFamily: TH.serif, fontSize: state==='gap'?14:16, fontStyle: state==='gap'?'italic':'normal', fontWeight: state==='gap'?400:500, color: state==='gap'?TH.mute:TH.ink, letterSpacing: -0.2, lineHeight: 1.2, marginTop: 3 }}>{title}</div>
        {sub && <div style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 12, color: TH.mute, marginTop: 3 }}>{sub}</div>}
        {by && <div style={{ marginTop: 6, display: 'inline-flex', alignItems: 'center', gap: 5 }}><span style={{ width: 15, height: 15, borderRadius: 999, background: by.c, color: '#fff', fontFamily: TH.serif, fontSize: 8, fontWeight: 500, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>{by.i}</span><span style={{ fontSize: 9.5, color: TH.mute, fontStyle: 'italic', fontFamily: TH.serif }}>{by.n} added · {by.ago}</span></div>}
      </div>
    </div>
  );
}

// ═══ 1 · TENSE SPINE — past → today → future in one scroll ═══
function ItinTenseSpine() {
  return (
    <Phone bg={TH.paper}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <ItinTopBar/>
        <ReviewRibbon/>
        {/* PAST — compressed diary */}
        <div style={{ padding: '14px 20px 0' }}>
          <div style={{ fontSize: 8.5, letterSpacing: 1.8, color: TH.faint, fontWeight: 700, paddingLeft: 58, marginBottom: 2 }}>BEHIND YOU</div>
          <PastDay day="SAT" date="18" summary="Alfama, settling, the long first walk" photos="6"/>
          <PastDay day="SUN" date="19" summary="Miradouros east to west — you skipped lunch" photos="11"/>
        </div>
        {/* hairline divider into today */}
        <div style={{ margin: '8px 20px', display: 'flex', alignItems: 'center', gap: 10 }}>
          <span style={{ flex: 1, height: 1, background: TH.hair }}/>
          <span style={{ fontSize: 8.5, letterSpacing: 2, color: TH.goldDeep, fontWeight: 700 }}>TODAY · MON 20</span>
          <span style={{ flex: 1, height: 1, background: TH.hair }}/>
        </div>
        {/* TODAY — live */}
        <div style={{ padding: '4px 20px 0' }}>
          <div style={{ display: 'grid', gridTemplateColumns: '46px 1fr', gap: 12 }}>
            <div style={{ textAlign: 'center', paddingTop: 1 }}>
              <div style={{ fontSize: 8, letterSpacing: 1, color: TH.goldDeep, fontWeight: 700 }}>MON</div>
              <div style={{ fontFamily: TH.serif, fontSize: 30, fontWeight: 500, color: TH.gold, lineHeight: 0.9, fontVariantNumeric: 'oldstyle-nums', marginTop: 2 }}>20</div>
              <div style={{ fontFamily: TH.mono, fontSize: 8, color: TH.faint, marginTop: 7 }}>18°</div>
            </div>
            <div style={{ paddingTop: 5 }}>
              <LiveBlock time="9:30 — DONE" title="Coffee at Kayaba" sub="you were there 40 min"/>
              <LiveBlock time="NOW · 10:14" title="Cemetery walk, the slow way" state="now"/>
              <LiveBlock time="21:00" title="Fado, the quiet room" state="booked" last/>
            </div>
          </div>
        </div>
        {/* FUTURE — plannable, with a ghost proposal */}
        <div style={{ padding: '6px 20px 0' }}>
          <div style={{ display: 'grid', gridTemplateColumns: '46px 1fr', gap: 12 }}>
            <div style={{ textAlign: 'center', paddingTop: 1 }}>
              <div style={{ fontSize: 8, letterSpacing: 1, color: TH.mute, fontWeight: 700 }}>TUE</div>
              <div style={{ fontFamily: TH.serif, fontSize: 30, fontWeight: 500, color: TH.ink, lineHeight: 0.9, fontVariantNumeric: 'oldstyle-nums', marginTop: 2 }}>21</div>
            </div>
            <div style={{ paddingTop: 5 }}>
              <LiveBlock time="MORNING" title="Belém, early" sub="beat the crowd"/>
              <LiveBlock ghost title="Swap museum → Time Out Market" sub="we'll be too tired for two museums" proposer={{ i:'T', c:'#A0703A', n:'Theo' }} last/>
            </div>
          </div>
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// ═══ 2 · BLOCK-TAP SHEETS ═══
// Sheet shell (local, dark-dim over spine).
function BSheet({ children, h = 440 }) {
  return (
    <Phone bg={TH.paper}>
      <div style={{ position: 'absolute', inset: 0, overflow: 'hidden' }}>
        <div style={{ position: 'absolute', inset: 0 }}><StyleRiso w={393} h={852}/></div>
        <div style={{ position: 'absolute', inset: 0, background: 'rgba(20,14,9,0.52)' }}/>
        <div style={{ position: 'absolute', left: 0, right: 0, bottom: 0, height: h, background: TH.paper, borderRadius: '26px 26px 0 0', boxShadow: '0 -16px 40px -12px rgba(0,0,0,0.3)', overflow: 'hidden' }}>
          <div style={{ display: 'flex', justifyContent: 'center', paddingTop: 10 }}><div style={{ width: 36, height: 4, borderRadius: 4, background: TH.faint }}/></div>
          {children}
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// 2a · FUTURE block tapped — place detail + change/replace/book/remove.
function SheetBlockFuture() {
  return (
    <BSheet h={500}>
      <div style={{ padding: '14px 22px 0' }}>
        <div style={{ fontFamily: TH.mono, fontSize: 9, color: TH.mute, letterSpacing: 1 }}>TUE 21 · MORNING</div>
        <h2 style={{ fontFamily: TH.serif, fontSize: 25, fontWeight: 500, letterSpacing: -0.4, color: TH.ink, margin: '4px 0 0' }}>Belém, early</h2>
        <div style={{ marginTop: 12, height: 120, borderRadius: 12, overflow: 'hidden' }}><StyleRiso w={349} h={120}/></div>
        <p style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 13.5, color: TH.mute, lineHeight: 1.4, margin: '12px 0 0' }}>The monastery and the tarts, before the buses. Vesper suggests 8:30.</p>
        {/* primary: ask Vesper to change (the key flow) */}
        <div style={{ marginTop: 16, display: 'flex', alignItems: 'center', gap: 10, padding: '12px 14px', background: TH.ink, borderRadius: 12 }}>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="#E5C16F"><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>
          <span style={{ flex: 1, fontFamily: TH.serif, fontStyle: 'italic', fontSize: 14, color: 'rgba(255,255,255,0.92)' }}>“make this later” · “find a quieter alternative”…</span>
        </div>
        <div style={{ marginTop: 10, display: 'flex', gap: 7 }}>
          {['Move','Book','Remove'].map((t,i)=>(<span key={t} style={{ flex: 1, textAlign: 'center', padding: '10px 0', borderRadius: 10, fontSize: 12.5, fontWeight: 600, color: i===2?'#A04030':TH.soft, background: TH.card, border: `0.5px solid ${TH.hair}` }}>{t}</span>))}
        </div>
      </div>
    </BSheet>
  );
}

// 2b · PROPOSE CHANGE → Vesper diff (the change card, in-itinerary).
function SheetChangeDiff() {
  return (
    <BSheet h={440}>
      <div style={{ padding: '16px 22px 0' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 7 }}>
          <svg width="13" height="13" viewBox="0 0 24 24" fill={TH.gold}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>
          <span style={{ fontSize: 9, letterSpacing: 1.6, fontWeight: 700, color: TH.goldDeep }}>VESPER · A PROPOSED CHANGE</span>
        </div>
        <p style={{ fontFamily: TH.serif, fontSize: 16, color: TH.ink, lineHeight: 1.4, margin: '12px 0 0', letterSpacing: -0.1 }}>You asked for a quieter morning — here’s the swap.</p>
        {/* the diff */}
        <div style={{ marginTop: 14, borderRadius: 12, border: `0.5px solid ${TH.hair}`, overflow: 'hidden' }}>
          <div style={{ padding: '12px 14px', background: 'rgba(160,64,48,0.06)', borderBottom: `0.5px solid ${TH.hair}` }}>
            <div style={{ fontSize: 8.5, letterSpacing: 1.2, color: '#A04030', fontWeight: 700 }}>WAS</div>
            <div style={{ fontFamily: TH.serif, fontSize: 15, color: TH.mute, textDecoration: 'line-through', textDecorationThickness: '1px', marginTop: 2 }}>Belém · monastery + tarts</div>
          </div>
          <div style={{ padding: '12px 14px', background: 'rgba(61,112,80,0.06)' }}>
            <div style={{ fontSize: 8.5, letterSpacing: 1.2, color: '#3D7050', fontWeight: 700 }}>NOW</div>
            <div style={{ fontFamily: TH.serif, fontSize: 15.5, color: TH.ink, fontWeight: 500, marginTop: 2 }}>Gulbenkian garden, slow morning</div>
            <div style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 11.5, color: TH.mute, marginTop: 2 }}>quiet, shaded, ten minutes from your stay</div>
          </div>
        </div>
        <div style={{ marginTop: 14, display: 'flex', gap: 8 }}>
          <span style={{ flex: 1, textAlign: 'center', padding: '12px 0', background: TH.ink, color: '#fff', borderRadius: 999, fontSize: 13.5, fontWeight: 600 }}>Keep the change</span>
          <span style={{ padding: '12px 18px', textAlign: 'center', background: TH.card, color: TH.soft, border: `0.5px solid ${TH.hair}`, borderRadius: 999, fontSize: 13, fontWeight: 600, fontFamily: TH.serif, fontStyle: 'italic' }}>show both</span>
        </div>
      </div>
    </BSheet>
  );
}

// 2c · PAST block tapped — the log view: what happened + to Atlas.
function SheetBlockPast() {
  return (
    <BSheet h={460}>
      <div style={{ padding: '14px 22px 0' }}>
        <div style={{ fontFamily: TH.mono, fontSize: 9, color: TH.mute, letterSpacing: 1 }}>SUN 19 · EVENING · HAPPENED</div>
        <h2 style={{ fontFamily: TH.serif, fontSize: 24, fontWeight: 500, letterSpacing: -0.4, color: TH.ink, margin: '4px 0 0' }}>Fado, the quiet room</h2>
        {/* photo strip you took */}
        <div style={{ marginTop: 14, display: 'flex', gap: 7 }}>
          {['dusk','amber','day'].map((t,i)=>(<div key={i} style={{ flex: 1, height: 86, borderRadius: 8, overflow: 'hidden', border: `2px solid #fff`, boxShadow: '0 4px 10px -6px rgba(0,0,0,0.25)' }}><StyleRiso w={108} h={86}/></div>))}
        </div>
        <p style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 14, color: TH.soft, lineHeight: 1.45, margin: '14px 0 0' }}>You stayed past midnight. Vesper noted the singer’s name for your Atlas.</p>
        <div style={{ marginTop: 16, display: 'flex', alignItems: 'center', gap: 10, padding: '12px 14px', background: TH.card, borderRadius: 12, border: `0.8px solid rgba(176,133,58,0.4)` }}>
          <svg width="14" height="14" viewBox="0 0 24 24" fill={TH.gold}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>
          <span style={{ flex: 1, fontFamily: TH.serif, fontSize: 14, color: TH.ink, fontWeight: 500 }}>Keep this evening in your Atlas</span>
          <span style={{ fontSize: 11, color: TH.goldDeep, fontWeight: 700 }}>SAVE →</span>
        </div>
      </div>
    </BSheet>
  );
}

Object.assign(window, { ItinTopBar, ReviewRibbon, ItinTenseSpine, SheetBlockFuture, SheetChangeDiff, SheetBlockPast });
