// ═══════════════════════════════════════════════════════════════
// VESPER'S READ — the redesigned, editorial (not tabular) module,
// plus its five context shapes. Rail-pill seg control everywhere.
// Reuses discover-kit (D, Plate, DIcon, Spark, VesperBy, LensChip,
// SegControl, FieldEyebrow) + design-system (Phone, TabBar).
// ═══════════════════════════════════════════════════════════════

// Compact Discover header used by all shape screens (rail seg control).
function DiscoverTop({ place = 'Lisbon', context, active = 1 }) {
  return (
    <div style={{ padding: '14px 22px 0' }}>
      <div style={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between' }}>
        <div>
          <h1 style={{ fontFamily: T.serif, fontSize: 26, fontWeight: 500, letterSpacing: -0.8, color: T.ink, margin: 0, lineHeight: 1 }}>Discover</h1>
          {context && (
            <div style={{ marginTop: 6, display: 'flex', alignItems: 'center', gap: 7, fontSize: 11.5, color: T.mute }}>
              <span style={{ width: 5, height: 5, borderRadius: 5, background: D.earth }}/>
              <span>{context}</span>
            </div>
          )}
        </div>
        <div style={{ display: 'flex', gap: 14, paddingTop: 3 }}>{DIcon.settings()}{DIcon.saved()}</div>
      </div>
      <div style={{ marginTop: 12, display: 'flex', alignItems: 'center', gap: 10, padding: '9px 14px', background: T.cardWarm, borderRadius: 999, border: `0.5px solid ${T.hairline}` }}>
        {DIcon.search()}<span style={{ fontSize: 13.5, color: T.muteSoft }}>Search places, restaurants, cities…</span>
      </div>
      <div style={{ marginTop: 12 }}><SegControl variant="rail" active={active}/></div>
    </div>
  );
}

// ─── The card chrome — warm, editorial, one soft header ─────────
function ReadFrame({ place, updated = 'TODAY', kicker = "VESPER’S READ", children, style }) {
  return (
    <div style={{
      background: T.cardWarm, borderRadius: 16, border: `0.5px solid ${T.hairline}`,
      boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset, 0 10px 26px -18px rgba(0,0,0,0.18)',
      overflow: 'hidden', ...style,
    }}>
      <div style={{ padding: '14px 16px 0', display: 'flex', alignItems: 'center', gap: 7 }}>
        <Spark s={14}/>
        <span style={{ fontSize: 10, letterSpacing: 1.6, fontWeight: 700, color: D.vesperDeep }}>{kicker}</span>
        {place && <span style={{ fontSize: 10, letterSpacing: 1.4, fontWeight: 700, color: D.earth }}>· {place.toUpperCase()}</span>}
        <span style={{ marginLeft: 'auto', fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1 }}>{updated}</span>
      </div>
      {children}
    </div>
  );
}

// A single read line — colored keyword + serif insight + opens-dossier arrow.
// This is the relationship made visible: every line resolves to a lensed dossier.
function ReadLine({ tag, color, lens, children, first }) {
  return (
    <div style={{
      display: 'flex', alignItems: 'flex-start', gap: 10, padding: '11px 0',
      borderTop: first ? 'none' : `0.5px solid ${T.hairThin}`,
    }}>
      <span style={{ fontSize: 9, letterSpacing: 1.2, fontWeight: 700, color, width: 52, flexShrink: 0, paddingTop: 3 }}>{tag}</span>
      <span style={{ flex: 1, fontFamily: T.serif, fontSize: 14, color: T.ink, lineHeight: 1.35, letterSpacing: -0.1 }}>{children}</span>
      <span style={{ flexShrink: 0, paddingTop: 2, display: 'flex', alignItems: 'center', gap: 4 }}>
        <span style={{ fontSize: 8.5, letterSpacing: 1, color: T.muteSoft, fontWeight: 600 }}>{lens}</span>
        <span style={{ color: T.muteSoft, fontSize: 11 }}>→</span>
      </span>
    </div>
  );
}

const STANCE = { matters: D.vesper, notice: D.earth, skip: T.mute, timely: '#3D7050', near: '#3D5066' };

// ─── SHAPE 1 · DISPATCH (no trip — outward, "where next") ───────
function ReadDispatch() {
  return (
    <Phone bg={T.bg}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <DiscoverTop place="Lisbon" context="New York · nothing booked" active={1}/>
        <div style={{ padding: '16px 16px 0' }}>
          <ReadFrame place={null} kicker="VESPER’S READ · WHERE NEXT" updated="">
            <div style={{ padding: '12px 16px 0' }}>
              <Plate variant="hills" style={{ height: 150, borderRadius: 12 }} dim={0.08}>
                <div style={{ position: 'absolute', top: 10, left: 10 }}><LensChip lens="For the obsessed" onDark/></div>
              </Plate>
              <p style={{ fontFamily: T.serif, fontSize: 19, fontWeight: 500, color: T.ink, letterSpacing: -0.3, lineHeight: 1.2, margin: '12px 0 0' }}>
                Three cities are having <span style={{ fontStyle: 'italic' }}>a moment</span> that suits you.
              </p>
            </div>
            <div style={{ padding: '4px 16px 12px' }}>
              <ReadLine tag="LISBON" color={STANCE.matters} lens="Why here" first>Layered food cultures at every price, no theatre.</ReadLine>
              <ReadLine tag="TBILISI" color={STANCE.matters} lens="Insider">Wine country an hour out, still uncrowded.</ReadLine>
              <ReadLine tag="NAPLES" color={STANCE.matters} lens="The debate">Worth it, despite what everyone now says.</ReadLine>
            </div>
          </ReadFrame>
        </div>
        <div style={{ padding: '16px 22px 0' }}>
          <SectionLabel right="FROM VESPER">A SLOW WEEK, IF YOU WANT ONE</SectionLabel>
        </div>
      </div>
      <TabBar active="discover"/>
    </Phone>
  );
}

// ─── SHAPE 2 · BRIEFING (trip booked, pre-departure) ────────────
function ReadBriefing() {
  return (
    <Phone bg={T.bg}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <DiscoverTop place="Lisbon" context="Lisbon · in 3 weeks" active={1}/>
        <div style={{ padding: '16px 16px 0' }}>
          <ReadFrame place="Lisbon" kicker="VESPER’S READ · BEFORE YOU GO" updated="FOR MAY 18–24">
            <div style={{ padding: '10px 16px 4px' }}>
              <p style={{ fontFamily: T.serif, fontSize: 17, fontWeight: 500, color: T.ink, letterSpacing: -0.2, lineHeight: 1.3, margin: 0 }}>
                The city is read from its <span style={{ fontStyle: 'italic' }}>viewpoints</span>, not its monuments.
              </p>
            </div>
            <div style={{ padding: '2px 16px 12px' }}>
              <ReadLine tag="MATTERS" color={STANCE.matters} lens="Why here" first>Miradouro culture — plan your evenings around them.</ReadLine>
              <ReadLine tag="SKIP" color={STANCE.skip} lens="A day in">Tram 28 at midday — walk it in reverse instead.</ReadLine>
              <ReadLine tag="TIMELY" color={STANCE.timely} lens="Insider">Santo António’s feast lands in your window (Jun 12–13).</ReadLine>
            </div>
          </ReadFrame>
        </div>
        <div style={{ padding: '16px 22px 0' }}>
          <SectionLabel right="NEAR YOUR STAY">WORTH THE WALK FROM ALFAMA</SectionLabel>
        </div>
      </div>
      <TabBar active="discover"/>
    </Phone>
  );
}

// ─── SHAPE 3 · PROXIMITY (in-destination, live) ─────────────────
function ReadProximity() {
  return (
    <Phone bg={T.bg}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <DiscoverTop place="Lisbon" context="You’re in Alfama · 10:14" active={1}/>
        <div style={{ padding: '16px 16px 0' }}>
          <ReadFrame place="Alfama" kicker="VESPER’S READ · NEAR YOU NOW" updated="LIVE">
            <div style={{ padding: '12px 16px 0', display: 'flex', gap: 12, alignItems: 'center' }}>
              <Plate variant="alley" style={{ width: 84, height: 84, borderRadius: 12, flexShrink: 0 }}/>
              <div>
                <div style={{ display: 'inline-flex', alignItems: 'center', gap: 5, padding: '3px 9px', borderRadius: 999, background: 'rgba(61,80,102,0.10)', fontSize: 9, letterSpacing: 1.2, fontWeight: 700, color: '#3D5066' }}>
                  <span style={{ width: 5, height: 5, borderRadius: 5, background: '#3D5066' }}/> 6 MIN ON FOOT
                </div>
                <p style={{ fontFamily: T.serif, fontSize: 17, fontWeight: 500, color: T.ink, letterSpacing: -0.2, lineHeight: 1.25, margin: '8px 0 0' }}>
                  You’re a block from the one I’d send you to.
                </p>
              </div>
            </div>
            <div style={{ padding: '6px 16px 12px' }}>
              <ReadLine tag="NOW" color={STANCE.near} lens="Ritual" first>Bica at Pois, Café — before the 11am crowd.</ReadLine>
              <ReadLine tag="LIGHT" color={STANCE.notice} lens="Why here">Portas do Sol glows best in the next hour.</ReadLine>
            </div>
          </ReadFrame>
        </div>
        <div style={{ padding: '16px 22px 0' }}>
          <SectionLabel right="WITHIN 10 MIN">WHILE YOU’RE HERE</SectionLabel>
        </div>
      </div>
      <TabBar active="discover"/>
    </Phone>
  );
}

// ─── SHAPE 4 · RETROSPECTIVE (just back → Atlas) ────────────────
function ReadRetro() {
  return (
    <Phone bg={T.bg}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <DiscoverTop place="Lisbon" context="Home · back 2 days" active={1}/>
        <div style={{ padding: '16px 16px 0' }}>
          <ReadFrame place="Lisbon" kicker="VESPER’S READ · NOW THAT YOU’VE BEEN" updated="">
            <div style={{ padding: '10px 16px 4px' }}>
              <p style={{ fontFamily: T.serif, fontSize: 17, fontWeight: 500, color: T.ink, letterSpacing: -0.2, lineHeight: 1.3, margin: 0 }}>
                The read you <span style={{ fontStyle: 'italic' }}>didn’t have</span> while you were there.
              </p>
            </div>
            <div style={{ padding: '2px 16px 10px' }}>
              <ReadLine tag="YOU DID" color={STANCE.matters} lens="A day in" first>Walked Alfama three times — you were chasing the light.</ReadLine>
              <ReadLine tag="MISSED" color={STANCE.notice} lens="Insider">The fado you found has a quieter sister two streets up.</ReadLine>
            </div>
            <div style={{ margin: '0 16px 14px', padding: '11px 13px', background: T.cardSoft, borderRadius: 12, border: `0.8px dashed ${T.gold}`, display: 'flex', alignItems: 'center', gap: 10 }}>
              <Spark s={13} c={T.gold}/>
              <span style={{ flex: 1, fontFamily: T.serif, fontSize: 13.5, color: T.ink, letterSpacing: -0.1 }}>I drafted a postcard for your Atlas.</span>
              <span style={{ fontSize: 11, color: T.goldDeep, fontWeight: 600 }}>Keep →</span>
            </div>
          </ReadFrame>
        </div>
      </div>
      <TabBar active="discover"/>
    </Phone>
  );
}

// ─── SHAPE 5 · DUAL (location ≠ trip) ───────────────────────────
function ReadDual() {
  return (
    <Phone bg={T.bg}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <DiscoverTop place="Lisbon" context={null} active={1}/>
        {/* context switch */}
        <div style={{ padding: '14px 22px 0', display: 'flex', gap: 8 }}>
          {[{ t: 'Around you', s: 'New York', on: false }, { t: 'Your trip', s: 'Lisbon · 3 wks', on: true }].map((c, i) => (
            <div key={i} style={{
              flex: 1, padding: '9px 12px', borderRadius: 12,
              background: c.on ? T.cardWarm : 'transparent',
              border: c.on ? `0.8px solid ${D.vesperRule}` : `0.5px solid ${T.hairline}`,
            }}>
              <div style={{ fontSize: 8.5, letterSpacing: 1.2, fontWeight: 700, color: c.on ? D.vesperDeep : T.muteSoft }}>{c.t.toUpperCase()}</div>
              <div style={{ fontFamily: T.serif, fontSize: 14, color: c.on ? T.ink : T.mute, fontWeight: 500, marginTop: 2, letterSpacing: -0.1 }}>{c.s}</div>
            </div>
          ))}
        </div>
        <div style={{ padding: '14px 16px 0' }}>
          <ReadFrame place="Lisbon" kicker="VESPER’S READ · YOUR TRIP" updated="IN 3 WEEKS">
            <div style={{ padding: '10px 16px 4px' }}>
              <p style={{ fontFamily: T.serif, fontSize: 16.5, fontWeight: 500, color: T.ink, letterSpacing: -0.2, lineHeight: 1.3, margin: 0 }}>
                Three weeks out — here’s what to read <span style={{ fontStyle: 'italic' }}>before</span> you go.
              </p>
            </div>
            <div style={{ padding: '2px 16px 12px' }}>
              <ReadLine tag="MATTERS" color={STANCE.matters} lens="Why here" first>Miradouro culture — the city reads from above.</ReadLine>
              <ReadLine tag="TIMELY" color={STANCE.timely} lens="Insider">A feast lands right in your window.</ReadLine>
            </div>
          </ReadFrame>
          <div style={{ marginTop: 10, textAlign: 'center', fontSize: 11, color: T.muteSoft, fontStyle: 'italic', fontFamily: T.serif }}>
            switch to <span style={{ color: T.inkSoft }}>Around you</span> for tonight in New York
          </div>
        </div>
      </div>
      <TabBar active="discover"/>
    </Phone>
  );
}

Object.assign(window, { DiscoverTop, ReadFrame, ReadLine, STANCE, ReadDispatch, ReadBriefing, ReadProximity, ReadRetro, ReadDual });
