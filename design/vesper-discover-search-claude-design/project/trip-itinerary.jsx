// ═══════════════════════════════════════════════════════════════
// ITINERARY OBJECT — the journal expanded full-screen. A continuous
// day-spine, editorial blocks, Vesper in the margins. Ages by phase.
// Reuses TH + TripHeader + Phone/TabBar + StyleRiso.
// ═══════════════════════════════════════════════════════════════

// A block hanging off the day spine.
function Block({ time, title, sub, by, live, gap, booked }) {
  return (
    <div style={{ display: 'flex', gap: 13, position: 'relative' }}>
      {/* spine node */}
      <div style={{ width: 14, flexShrink: 0, display: 'flex', justifyContent: 'center', position: 'relative' }}>
        <span style={{
          width: live ? 10 : 7, height: live ? 10 : 7, borderRadius: 999, marginTop: 5,
          background: gap ? 'transparent' : live ? TH.gold : booked ? TH.blue : TH.soft,
          border: gap ? `1.2px dashed ${TH.faint}` : 'none',
          boxShadow: live ? '0 0 0 4px rgba(176,133,58,0.18)' : 'none', zIndex: 1,
        }}/>
      </div>
      <div style={{ flex: 1, minWidth: 0, paddingBottom: 16 }}>
        <div style={{ display: 'flex', alignItems: 'baseline', gap: 8 }}>
          <span style={{ fontFamily: TH.mono, fontSize: 9, color: live ? TH.goldDeep : TH.mute, letterSpacing: 1, fontWeight: 600 }}>{time}</span>
          {live && <span style={{ fontSize: 8, letterSpacing: 1.2, fontWeight: 700, color: TH.goldDeep }}>NOW</span>}
          {booked && <span style={{ fontSize: 8, letterSpacing: 1.2, fontWeight: 700, color: TH.blue }}>BOOKED</span>}
        </div>
        <div style={{ fontFamily: TH.serif, fontSize: gap ? 14 : 15.5, fontStyle: gap ? 'italic' : 'normal', fontWeight: gap ? 400 : 500, color: gap ? TH.mute : TH.ink, letterSpacing: -0.2, lineHeight: 1.2, marginTop: 3 }}>{title}</div>
        {sub && <div style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 12, color: TH.mute, marginTop: 3 }}>{sub}</div>}
        {by && <div style={{ marginTop: 6 }}><span style={{ display: 'inline-block', width: 16, height: 16, borderRadius: 999, background: by.c, color: '#fff', fontFamily: TH.serif, fontSize: 8.5, fontWeight: 500, textAlign: 'center', lineHeight: '16px' }}>{by.i}</span></div>}
      </div>
    </div>
  );
}

// A day on the spine — the date numeral anchors it (same as home day-rows).
function SpineDay({ day, date, mo, children, today }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '44px 1fr', gap: 10, position: 'relative' }}>
      {/* continuous rail behind */}
      <div style={{ position: 'absolute', left: 64, top: 8, bottom: -8, width: 1, background: TH.hairThin }}/>
      <div style={{ textAlign: 'center', paddingTop: 2 }}>
        <div style={{ fontSize: 8, letterSpacing: 1, color: TH.mute, fontWeight: 700 }}>{day}</div>
        <div style={{ fontFamily: TH.serif, fontSize: 26, fontWeight: 500, color: today ? TH.gold : TH.ink, lineHeight: 1, fontVariantNumeric: 'oldstyle-nums', letterSpacing: -0.5 }}>{date}</div>
        <div style={{ fontSize: 7.5, letterSpacing: 1, color: TH.faint, fontWeight: 700, marginTop: 2 }}>{mo}</div>
      </div>
      <div style={{ paddingTop: 4 }}>{children}</div>
    </div>
  );
}

// Slim identity header that keeps you anchored in the trip.
function ObjectHeader({ title, kicker, scene = 'riso' }) {
  return (
    <div style={{ position: 'relative', height: 96, overflow: 'hidden' }}>
      <div style={{ position: 'absolute', inset: 0 }}><StyleRiso w={393} h={96}/></div>
      <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.46), rgba(20,14,9,0.66))' }}/>
      <div style={{ paddingTop: 50 }}><TripHeader onDark/></div>
      <div style={{ position: 'absolute', left: 22, bottom: 12 }}>
        <div style={{ fontSize: 8.5, letterSpacing: 1.8, color: 'rgba(255,255,255,0.8)', fontWeight: 700 }}>{kicker}</div>
        <div style={{ fontFamily: TH.serif, fontSize: 19, fontWeight: 500, color: '#fff', letterSpacing: -0.3, marginTop: 2 }}>{title}</div>
      </div>
    </div>
  );
}

// PRE-TRIP itinerary — a plan being filled, sparse days honest.
function ItineraryPlan() {
  return (
    <Phone bg={TH.paper}>
      <div style={{ position: 'absolute', inset: 0, overflow: 'hidden' }}>
        <ObjectHeader kicker="ITINERARY · TAKING SHAPE" title="Lisbon, slowly"/>
        <div style={{ padding: '18px 20px 0' }}>
          <SpineDay day="SAT" date="18" mo="MAY">
            <Block time="MORNING" title="Land soft, settle in Alfama" sub="bags down, no plans"/>
            <Block time="EVENING" title="Dinner near the stay" by={{ i: 'A', c: '#7C8F73' }}/>
          </SpineDay>
          <SpineDay day="SUN" date="19" mo="MAY">
            <Block time="DAY" title="Miradouros, east to west" sub="Ana’s walking list"/>
          </SpineDay>
          <SpineDay day="MON" date="20" mo="MAY">
            <Block gap time="OPEN" title="this day is bare — want me to sketch it?"/>
          </SpineDay>
        </div>
        {/* Vesper margin nudge */}
        <div style={{ position: 'absolute', bottom: 92, left: 16, right: 16, padding: '11px 14px', background: TH.card, borderRadius: 12, border: `0.8px solid rgba(176,133,58,0.4)`, display: 'flex', alignItems: 'center', gap: 10 }}>
          <svg width="13" height="13" viewBox="0 0 24 24" fill={TH.gold}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>
          <span style={{ flex: 1, fontFamily: TH.serif, fontSize: 13, fontStyle: 'italic', color: TH.ink }}>Two days still open. Sketch them from your taste?</span>
          <span style={{ fontSize: 11, color: TH.goldDeep, fontWeight: 600 }}>→</span>
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// LIVE itinerary — today auto-scrolled in, the now block glows.
function ItineraryLive() {
  return (
    <Phone bg={TH.paper}>
      <div style={{ position: 'absolute', inset: 0, overflow: 'hidden' }}>
        <ObjectHeader kicker="ITINERARY · DAY 3" title="Lisbon, slowly"/>
        <div style={{ padding: '18px 20px 0' }}>
          <SpineDay day="SUN" date="19" mo="MAY">
            <Block time="DONE" title="Miradouros, east to west" sub="you walked all six"/>
          </SpineDay>
          <SpineDay day="MON" date="20" mo="MAY" today>
            <Block live time="NOW · 10:14" title="Coffee at Kayaba, then the cemetery walk" sub="8 min east"/>
            <Block booked time="21:00" title="Fado, the quiet room" sub="Vesper held two seats"/>
          </SpineDay>
          <SpineDay day="TUE" date="21" mo="MAY">
            <Block time="DAY" title="Belém, early to beat the crowd"/>
          </SpineDay>
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

Object.assign(window, { Block, SpineDay, ObjectHeader, ItineraryPlan, ItineraryLive });
