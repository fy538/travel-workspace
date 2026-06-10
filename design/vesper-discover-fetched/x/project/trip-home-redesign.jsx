// ═══════════════════════════════════════════════════════════════
// TRIP HOME · REDESIGNED — the itinerary is the body. The home shows
// a day-preview that opens the real itinerary; tools sharpen to true
// siblings. Ages across phases. Reuses trip-home-kit + StyleRiso/Gouache.
// ═══════════════════════════════════════════════════════════════

// A preview row of the itinerary spine — tapping opens the itinerary at that day.
function PreviewDay({ day, date, title, sub, state, today, last }) {
  const dot = state==='now'?TH.gold:state==='booked'?TH.blue:state==='gap'?'transparent':TH.soft;
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '38px 14px 1fr', gap: 11, alignItems: 'flex-start' }}>
      <div style={{ textAlign: 'right', paddingTop: 1 }}>
        <div style={{ fontSize: 7.5, letterSpacing: 1, color: today?TH.goldDeep:TH.mute, fontWeight: 700 }}>{day}</div>
        <div style={{ fontFamily: TH.serif, fontSize: 19, fontWeight: 500, color: today?TH.gold:TH.ink, lineHeight: 0.95, fontVariantNumeric: 'oldstyle-nums' }}>{date}</div>
      </div>
      <div style={{ display: 'flex', justifyContent: 'center', position: 'relative' }}>
        {!last && <span style={{ position: 'absolute', top: 11, bottom: -10, width: 1, background: TH.hairThin }}/>}
        <span style={{ width: state==='now'?9:6.5, height: state==='now'?9:6.5, borderRadius: 999, marginTop: 5, background: dot, border: state==='gap'?`1.2px dashed ${TH.faint}`:'none', boxShadow: state==='now'?'0 0 0 4px rgba(176,133,58,0.18)':'none', zIndex: 1 }}/>
      </div>
      <div style={{ paddingBottom: last?0:14 }}>
        <div style={{ fontFamily: TH.serif, fontSize: state==='gap'?13.5:15, fontStyle: state==='gap'?'italic':'normal', fontWeight: state==='gap'?400:500, color: state==='gap'?TH.mute:TH.ink, letterSpacing: -0.2, lineHeight: 1.2 }}>{title}</div>
        {sub && <div style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 11.5, color: TH.mute, marginTop: 2 }}>{sub}</div>}
      </div>
    </div>
  );
}

// The "open the itinerary" door — the body's primary affordance.
function ItinDoor({ label = 'Open the full itinerary', meta = '6 days · 14 stops' }) {
  return (
    <div style={{ marginTop: 6, display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '12px 14px', background: TH.card, borderRadius: 12, border: `0.5px solid ${TH.hair}`, boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset' }}>
      <div>
        <div style={{ fontFamily: TH.serif, fontSize: 14.5, fontWeight: 500, color: TH.ink, letterSpacing: -0.1 }}>{label}</div>
        <div style={{ fontFamily: TH.mono, fontSize: 8.5, color: TH.faint, letterSpacing: 0.5, marginTop: 3 }}>{meta.toUpperCase()}</div>
      </div>
      <span style={{ width: 30, height: 30, borderRadius: 999, background: TH.ink, color: '#fff', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: 14 }}>→</span>
    </div>
  );
}

// Sharpened tile row — true siblings of the itinerary.
function TileRow({ tiles }) {
  return (
    <div style={{ display: 'flex', gap: 8 }}>
      {tiles.map((t,i)=>(<ObjectTile key={i} glyph={t.g} label={t.l} meta={t.m} accent={t.accent}/>))}
    </div>
  );
}

// ─── FOLIO (pre-trip) — itinerary preview is the body ───────────
function HomeFolio() {
  return (
    <Phone bg={TH.paper}>
      <div style={{ position: 'absolute', inset: 0, overflow: 'hidden' }}>
        <div style={{ position: 'relative', height: 290 }}>
          <div style={{ position: 'absolute', inset: 0 }}><StyleRiso w={393} h={290}/></div>
          <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.28) 0%, rgba(20,14,9,0) 32%, rgba(20,14,9,0) 54%, rgba(20,14,9,0.68) 100%)' }}/>
          <div style={{ paddingTop: 54 }}><TripHeader onDark/></div>
          <div style={{ position: 'absolute', top: 92, left: 22 }}><PhaseRibbon phase={1} onDark/></div>
          <div style={{ position: 'absolute', left: 22, right: 22, bottom: 18 }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 7 }}>
              <span style={{ padding: '3px 9px', borderRadius: 999, background: 'rgba(255,255,255,0.2)', backdropFilter: 'blur(6px)', fontSize: 9, letterSpacing: 1.4, fontWeight: 700, color: '#fff' }}>IN 23 DAYS</span>
              <People who={CAST} onDark size={22}/>
            </div>
            <h1 style={{ fontFamily: TH.serif, fontSize: 38, fontWeight: 500, letterSpacing: -1, lineHeight: 0.98, color: '#fff', margin: 0 }}>Lisbon, <span style={{ fontStyle: 'italic' }}>slowly</span></h1>
            <div style={{ fontFamily: TH.mono, fontSize: 10, color: 'rgba(255,255,255,0.85)', letterSpacing: 1, marginTop: 7 }}>MAY 18 – 24 · 6 NIGHTS · 3 OF YOU</div>
          </div>
        </div>

        <div style={{ padding: '16px 22px 0' }}>
          <VesperLine>Three weeks out — the spine’s taking shape. The only gap is where you sleep nights 5–7.</VesperLine>
        </div>

        {/* THE BODY = itinerary preview */}
        <div style={{ padding: '16px 22px 0' }}>
          <Label right="MAY 18 – 24">THE PLAN, SO FAR</Label>
          <div style={{ marginTop: 12 }}>
            <PreviewDay day="SAT" date="18" title="Land soft, settle in Alfama" sub="no plans past the first coffee"/>
            <PreviewDay day="SUN" date="19" title="Miradouros, east to west" sub="Ana’s walking list"/>
            <PreviewDay day="MON" date="20" title="this day is bare — sketch it?" state="gap" last/>
          </div>
          <ItinDoor/>
        </div>

        {/* sharpened tiles */}
        <div style={{ padding: '16px 18px 0' }}>
          <TileRow tiles={[{g:TG.map,l:'Map',m:'3 areas'},{g:TG.costs,l:'Costs',m:'split 3'},{g:TG.chat,l:'Group',m:'12 new',accent:true}]}/>
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// ─── LIVE (during) — Today preview opens itinerary at today ─────
function HomeLive() {
  return (
    <Phone bg={TH.paper}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <TripHeader title="Lisbon, slowly" showTitle/>
        <div style={{ padding: '8px 22px 0', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <PhaseRibbon phase={2}/><People who={CAST} size={20}/>
        </div>

        {/* live Today hero */}
        <div style={{ padding: '14px 18px 0' }}>
          <div style={{ borderRadius: 16, overflow: 'hidden', border: `0.5px solid ${TH.hair}` }}>
            <div style={{ position: 'relative', height: 116 }}>
              <div style={{ position: 'absolute', inset: 0 }}><StyleRiso w={357} h={116}/></div>
              <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(rgba(20,14,9,0.15),rgba(20,14,9,0.55))' }}/>
              <div style={{ position: 'absolute', top: 11, left: 13, display: 'inline-flex', alignItems: 'center', gap: 6, padding: '3px 9px', borderRadius: 999, background: 'rgba(61,80,102,0.92)', fontSize: 9, letterSpacing: 1.4, fontWeight: 700, color: '#fff' }}>
                <span style={{ width: 5, height: 5, borderRadius: 5, background: '#E5C16F' }}/> DAY 3 · MON
              </div>
              <div style={{ position: 'absolute', left: 14, right: 14, bottom: 12 }}>
                <div style={{ fontFamily: TH.serif, fontSize: 20, fontWeight: 500, color: '#fff', letterSpacing: -0.3 }}>You’re in Alfama</div>
                <div style={{ fontFamily: TH.mono, fontSize: 9.5, color: 'rgba(255,255,255,0.85)', letterSpacing: 1, marginTop: 3 }}>10:14 · 18° CLEAR</div>
              </div>
            </div>
            <div style={{ padding: '13px 15px 6px' }}>
              <div style={{ fontSize: 9, letterSpacing: 1.4, color: TH.goldDeep, fontWeight: 700 }}>NOW</div>
              <PreviewDay day="" date="" title="Cemetery walk, the slow way" sub="then coffee at Kayaba" state="now" last/>
            </div>
            <div style={{ padding: '0 15px 13px' }}><ItinDoor label="Open today’s plan" meta="3 stops left today"/></div>
          </div>
        </div>

        {/* group pulse */}
        <div style={{ padding: '16px 22px 0' }}>
          <Label right="JUST NOW">GROUP PULSE</Label>
          <div style={{ marginTop: 10, display: 'flex', alignItems: 'center', gap: 10 }}>
            <People who={[CAST[1]]} size={22}/>
            <span style={{ flex: 1, fontFamily: TH.serif, fontSize: 13.5, fontStyle: 'italic', color: TH.soft }}>Ana pinned a lunch spot 4 min away</span>
            <span style={{ color: TH.mute, fontSize: 12 }}>→</span>
          </div>
        </div>

        <div style={{ padding: '16px 18px 0' }}>
          <TileRow tiles={[{g:TG.map,l:'Map',m:'you’re here'},{g:TG.costs,l:'Costs',m:'€96 you'},{g:TG.photos,l:'Photos',m:'+22',accent:true}]}/>
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// ─── MEMORY (post-trip) — story-led, itinerary becomes the record ─
function HomeMemory() {
  return (
    <Phone bg={TH.ink}>
      <div style={{ position: 'absolute', inset: 0, overflow: 'hidden', background: TH.paper }}>
        <div style={{ position: 'relative', height: 330 }}>
          <div style={{ position: 'absolute', inset: 0 }}><StyleGouache w={393} h={330}/></div>
          <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.26) 0%, rgba(20,14,9,0) 34%, rgba(20,14,9,0) 50%, rgba(20,14,9,0.72) 100%)' }}/>
          <div style={{ paddingTop: 54 }}><TripHeader onDark/></div>
          <div style={{ position: 'absolute', top: 92, left: 22 }}><PhaseRibbon phase={3} onDark/></div>
          <div style={{ position: 'absolute', left: 22, right: 22, bottom: 20 }}>
            <div style={{ fontSize: 9.5, letterSpacing: 2, color: 'rgba(255,255,255,0.8)', fontWeight: 700, marginBottom: 8 }}>A TRIP, REMEMBERED</div>
            <h1 style={{ fontFamily: TH.serif, fontSize: 38, fontWeight: 500, letterSpacing: -1, lineHeight: 0.98, color: '#fff', margin: 0 }}>Lisbon, <span style={{ fontStyle: 'italic' }}>slowly</span></h1>
            <div style={{ fontFamily: TH.mono, fontSize: 10, color: 'rgba(255,255,255,0.85)', letterSpacing: 1, marginTop: 7 }}>MAY 18 – 24 · 214 PHOTOS · 3 OF YOU</div>
          </div>
        </div>
        <div style={{ padding: '16px 18px 0' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '13px 15px', background: TH.card, borderRadius: 14, border: `0.8px solid rgba(176,133,58,0.4)` }}>
            <div style={{ width: 44, height: 56, transform: 'rotate(-4deg)', flexShrink: 0, borderRadius: 3, overflow: 'hidden', boxShadow: '0 4px 10px -5px rgba(0,0,0,0.3)' }}><StyleGouache w={44} h={56}/></div>
            <div style={{ flex: 1 }}>
              <div style={{ fontSize: 9, letterSpacing: 1.4, color: TH.goldDeep, fontWeight: 700 }}>YOUR STORY IS READY</div>
              <div style={{ fontFamily: TH.serif, fontSize: 16, fontWeight: 500, color: TH.ink, letterSpacing: -0.2, marginTop: 2, lineHeight: 1.1 }}>Six days, in Vesper’s words</div>
            </div>
            <span style={{ padding: '7px 13px', background: TH.gold, color: '#fff', borderRadius: 999, fontSize: 11.5, fontWeight: 600 }}>Read →</span>
          </div>
        </div>
        <div style={{ padding: '14px 22px 0' }}>
          <Label right="THE RECORD">WHERE YOU WENT</Label>
          <div style={{ marginTop: 11 }}>
            <PreviewDay day="MAY" date="20" title="Cemetery walk, then fado" sub="the night it all clicked" state="booked"/>
            <PreviewDay day="MAY" date="21" title="Belém, early" sub="Ana’s grand morning" last/>
          </div>
          <ItinDoor label="Revisit the full trip" meta="6 days · now a record"/>
        </div>
        <div style={{ padding: '14px 18px 0' }}>
          <TileRow tiles={[{g:TG.photos,l:'214 photos',m:'12 kept',accent:true},{g:TG.memory,l:'To Atlas',m:'+1 city'},{g:TG.map,l:'Map',m:'traced'}]}/>
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

Object.assign(window, { PreviewDay, ItinDoor, TileRow, HomeFolio, HomeLive, HomeMemory });
