// ═══════════════════════════════════════════════════════════════
// TRIP HOME — four phase states. Each uses one hero artifact, an
// editorial body, and demoted tool tiles. Reuses trip-home-kit + Phone
// + StyleRiso/StyleGouache (the house illustration).
// ═══════════════════════════════════════════════════════════════

// COLD START — a blank folio, an invitation, no sad empty cards.
function TripCold() {
  return (
    <Phone bg={TH.paper}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <TripHeader controls={false}/>
        <div style={{ padding: '8px 22px 0' }}><PhaseRibbon phase={0}/></div>
        {/* blank folio cover — debossed, waiting */}
        <div style={{ padding: '22px 22px 0' }}>
          <div style={{ height: 232, borderRadius: 16, border: `1.2px dashed ${TH.faint}`, background: TH.cardSoft, position: 'relative', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 14 }}>
            {/* faint compass */}
            <svg width="56" height="56" viewBox="0 0 56 56" fill="none" stroke={TH.faint} strokeWidth="1"><circle cx="28" cy="28" r="22"/><path d="M28 10 L32 28 L28 46 L24 28 Z" fill={TH.faint} stroke="none" opacity="0.5"/><path d="M10 28 H46"/></svg>
            <div style={{ textAlign: 'center' }}>
              <div style={{ fontSize: 9.5, letterSpacing: 2, color: TH.mute, fontWeight: 700 }}>UNTITLED TRIP</div>
              <div style={{ fontFamily: TH.serif, fontSize: 22, fontStyle: 'italic', color: TH.mute, marginTop: 4 }}>somewhere, someday</div>
            </div>
          </div>
        </div>
        {/* invitation */}
        <div style={{ padding: '22px 22px 0' }}>
          <h1 style={{ fontFamily: TH.serif, fontSize: 27, fontWeight: 500, letterSpacing: -0.6, lineHeight: 1.15, color: TH.ink, margin: 0 }}>
            Every trip starts as <span style={{ fontStyle: 'italic' }}>a feeling.</span>
          </h1>
          <p style={{ fontFamily: TH.serif, fontSize: 14, color: TH.mute, fontStyle: 'italic', lineHeight: 1.4, margin: '8px 0 0' }}>
            Tell Vesper one — a place, a month, who’s coming — and it’ll take shape from there.
          </p>
          <div style={{ marginTop: 18, display: 'flex', alignItems: 'center', gap: 10 }}>
            <span style={{ flex: 1, padding: '13px 0', textAlign: 'center', background: TH.gold, color: '#fff', borderRadius: 999, fontSize: 14, fontWeight: 600, letterSpacing: -0.1, display: 'inline-flex', alignItems: 'center', justifyContent: 'center', gap: 7 }}>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="#fff"><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>
              Shape this trip with Vesper
            </span>
          </div>
          <div style={{ marginTop: 14, display: 'flex', gap: 8 }}>
            {['Add destination', 'Invite people', 'Add dates'].map(t => (
              <span key={t} style={{ flex: 1, textAlign: 'center', padding: '9px 4px', borderRadius: 10, border: `0.5px solid ${TH.hair}`, fontFamily: TH.serif, fontSize: 12, color: TH.soft, background: TH.card }}>{t}</span>
            ))}
          </div>
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// VARIANT A · TRIP FOLIO — pre-trip populated. Editorial cover + journal body.
function TripFolio() {
  return (
    <Phone bg={TH.paper}>
      <div style={{ position: 'absolute', inset: 0, overflow: 'hidden' }}>
        {/* riso cover with overlaid identity */}
        <div style={{ position: 'relative', height: 318 }}>
          <div style={{ position: 'absolute', inset: 0 }}><StyleRiso w={393} h={318}/></div>
          <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.30) 0%, rgba(20,14,9,0) 30%, rgba(20,14,9,0) 52%, rgba(20,14,9,0.66) 100%)' }}/>
          <div style={{ paddingTop: 54 }}><TripHeader onDark/></div>
          <div style={{ position: 'absolute', top: 92, left: 22 }}><PhaseRibbon phase={1} onDark/></div>
          {/* identity block, low */}
          <div style={{ position: 'absolute', left: 22, right: 22, bottom: 18 }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 7 }}>
              <span style={{ padding: '3px 9px', borderRadius: 999, background: 'rgba(255,255,255,0.2)', backdropFilter: 'blur(6px)', fontSize: 9, letterSpacing: 1.4, fontWeight: 700, color: '#fff' }}>IN 23 DAYS</span>
              <People who={CAST} onDark size={22}/>
            </div>
            <h1 style={{ fontFamily: TH.serif, fontSize: 38, fontWeight: 500, letterSpacing: -1, lineHeight: 0.98, color: '#fff', margin: 0 }}>
              Lisbon, <span style={{ fontStyle: 'italic' }}>slowly</span>
            </h1>
            <div style={{ fontFamily: TH.mono, fontSize: 10, color: 'rgba(255,255,255,0.85)', letterSpacing: 1, marginTop: 7 }}>MAY 18 – 24 · 6 NIGHTS · 3 OF YOU</div>
          </div>
        </div>

        {/* Vesper note + the one thing to do */}
        <div style={{ padding: '16px 22px 0' }}>
          <VesperLine>You’re three weeks out — the only thing missing is where you sleep nights 5–7.</VesperLine>
          <div style={{ marginTop: 13, display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '11px 14px', background: TH.card, borderRadius: 12, border: `0.8px solid rgba(176,133,58,0.4)` }}>
            <div>
              <div style={{ fontSize: 9, letterSpacing: 1.4, color: TH.goldDeep, fontWeight: 700 }}>TOP NEED · A STAY</div>
              <div style={{ fontFamily: TH.serif, fontSize: 14.5, color: TH.ink, fontWeight: 500, marginTop: 2, letterSpacing: -0.1 }}>Pick a ryokan for nights 5–7</div>
            </div>
            <span style={{ padding: '7px 13px', background: TH.blue, color: '#fff', borderRadius: 999, fontSize: 11.5, fontWeight: 600 }}>Open →</span>
          </div>
        </div>

        {/* Journal — the body */}
        <div style={{ padding: '18px 22px 0' }}>
          <Label right="6 DAYS">THE DAYS, TAKING SHAPE</Label>
          <div style={{ marginTop: 4 }}>
            <DayRow day="SAT" date="18" title="Land soft, settle in Alfama" sub="no plans past the first coffee"/>
            <DayRow day="SUN" date="19" title="Miradouros, east to west" sub="Ana’s walking list"/>
            <DayRow day="MON" date="20" title="—" sub="a sparse day · ask Vesper"/>
          </div>
        </div>

        {/* tool tiles */}
        <div style={{ padding: '14px 18px 0', display: 'flex', gap: 8 }}>
          <ObjectTile glyph={TG.map} label="Route" meta="3 cities"/>
          <ObjectTile glyph={TG.costs} label="Costs" meta="split 3"/>
          <ObjectTile glyph={TG.chat} label="Group" meta="12 new"/>
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// VARIANT B · LIVING MAP / FIELD GUIDE — during trip. Today leads.
function TripLive() {
  return (
    <Phone bg={TH.paper}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <TripHeader title="Lisbon, slowly" showTitle/>
        <div style={{ padding: '8px 22px 0', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <PhaseRibbon phase={2}/>
          <People who={CAST} size={20}/>
        </div>

        {/* TODAY hero — live */}
        <div style={{ padding: '14px 18px 0' }}>
          <div style={{ borderRadius: 16, overflow: 'hidden', border: `0.5px solid ${TH.hair}`, boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset' }}>
            <div style={{ position: 'relative', height: 132 }}>
              <div style={{ position: 'absolute', inset: 0 }}><StyleRiso w={357} h={132}/></div>
              <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.2), rgba(20,14,9,0.55))' }}/>
              <div style={{ position: 'absolute', top: 11, left: 13, display: 'inline-flex', alignItems: 'center', gap: 6, padding: '3px 9px', borderRadius: 999, background: 'rgba(61,80,102,0.92)', fontSize: 9, letterSpacing: 1.4, fontWeight: 700, color: '#fff' }}>
                <span style={{ width: 5, height: 5, borderRadius: 5, background: '#E5C16F' }}/> DAY 3 · LIVE
              </div>
              <div style={{ position: 'absolute', left: 14, right: 14, bottom: 12 }}>
                <div style={{ fontFamily: TH.serif, fontSize: 21, fontWeight: 500, color: '#fff', letterSpacing: -0.3, lineHeight: 1.05 }}>You’re in Alfama</div>
                <div style={{ fontFamily: TH.mono, fontSize: 9.5, color: 'rgba(255,255,255,0.85)', letterSpacing: 1, marginTop: 4 }}>MON · 10:14 · 18° CLEAR</div>
              </div>
            </div>
            <div style={{ padding: '13px 15px' }}>
              <div style={{ fontSize: 9, letterSpacing: 1.4, color: TH.goldDeep, fontWeight: 700 }}>NEXT BLOCK · 11:00</div>
              <div style={{ fontFamily: TH.serif, fontSize: 17, fontWeight: 500, color: TH.ink, letterSpacing: -0.2, marginTop: 3 }}>Coffee at Kayaba, then the cemetery walk</div>
              <div style={{ marginTop: 11, display: 'flex', gap: 7 }}>
                {['Ask Vesper', 'Map', 'Add photo'].map((t, i) => (
                  <span key={t} style={{ flex: 1, textAlign: 'center', padding: '8px 0', borderRadius: 999, fontSize: 11.5, fontWeight: 600, letterSpacing: -0.1, background: i === 0 ? TH.ink : TH.cardSoft, color: i === 0 ? '#fff' : TH.soft, border: i === 0 ? 'none' : `0.5px solid ${TH.hair}` }}>{t}</span>
                ))}
              </div>
            </div>
          </div>
        </div>

        {/* group pulse */}
        <div style={{ padding: '14px 22px 0' }}>
          <Label right="JUST NOW">GROUP PULSE</Label>
          <div style={{ marginTop: 10, display: 'flex', alignItems: 'center', gap: 10 }}>
            <People who={[CAST[1]]} size={22}/>
            <span style={{ flex: 1, fontFamily: TH.serif, fontSize: 13.5, fontStyle: 'italic', color: TH.soft, letterSpacing: -0.05 }}>Ana pinned a lunch spot 4 min away</span>
            <span style={{ color: TH.mute, fontSize: 12 }}>→</span>
          </div>
        </div>

        {/* rest of day */}
        <div style={{ padding: '12px 22px 0' }}>
          <DayRow day="LATER" date="3" title="Fado, the quiet room" sub="Vesper held two seats, 21:00" dim/>
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// VARIANT C · MEMORY OBJECT — post-trip. Gouache cover, arc, story.
function TripMemory() {
  return (
    <Phone bg={TH.ink}>
      <div style={{ position: 'absolute', inset: 0, overflow: 'hidden', background: TH.paper }}>
        {/* gouache cover — the swoon */}
        <div style={{ position: 'relative', height: 360 }}>
          <div style={{ position: 'absolute', inset: 0 }}><StyleGouache w={393} h={360}/></div>
          <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.28) 0%, rgba(20,14,9,0) 32%, rgba(20,14,9,0) 48%, rgba(20,14,9,0.72) 100%)' }}/>
          <div style={{ paddingTop: 54 }}><TripHeader onDark/></div>
          <div style={{ position: 'absolute', top: 92, left: 22 }}><PhaseRibbon phase={3} onDark/></div>
          <div style={{ position: 'absolute', left: 22, right: 22, bottom: 20 }}>
            <div style={{ fontSize: 9.5, letterSpacing: 2, color: 'rgba(255,255,255,0.8)', fontWeight: 700, marginBottom: 8 }}>A TRIP, REMEMBERED</div>
            <h1 style={{ fontFamily: TH.serif, fontSize: 38, fontWeight: 500, letterSpacing: -1, lineHeight: 0.98, color: '#fff', margin: 0 }}>
              Lisbon, <span style={{ fontStyle: 'italic' }}>slowly</span>
            </h1>
            <div style={{ fontFamily: TH.mono, fontSize: 10, color: 'rgba(255,255,255,0.85)', letterSpacing: 1, marginTop: 7 }}>MAY 18 – 24 · 214 PHOTOS · 3 OF YOU</div>
          </div>
        </div>

        {/* story-ready */}
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

        {/* trip arc */}
        <div style={{ padding: '18px 22px 0' }}>
          <Label right="THE ARC">HOW IT WENT</Label>
          <div style={{ marginTop: 12, position: 'relative', height: 44 }}>
            <svg width="100%" height="44" viewBox="0 0 320 44" preserveAspectRatio="none"><path d="M0 32 Q50 30 90 22 T180 14 Q240 10 320 18" stroke={TH.gold} strokeWidth="1.4" fill="none"/></svg>
            {[['18',2],['20',28],['22',56],['24',92]].map(([d,l],i)=>(
              <div key={i} style={{ position: 'absolute', left: `${l}%`, top: i===3?6:i===2?2:i===1?18:24 }}><span style={{ width: 6, height: 6, borderRadius: 6, background: TH.gold, display: 'block' }}/></div>
            ))}
          </div>
          <p style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 13.5, color: TH.mute, lineHeight: 1.4, margin: '6px 0 0' }}>
            Quiet start, peaked at the fado on the fourth night, drifted home full.
          </p>
        </div>

        {/* what it added to Atlas */}
        <div style={{ padding: '16px 18px 0', display: 'flex', gap: 8 }}>
          <ObjectTile glyph={TG.photos} label="214 photos" meta="12 kept" accent/>
          <ObjectTile glyph={TG.memory} label="To Atlas" meta="+1 city"/>
          <ObjectTile glyph={TG.story} label="Travel DNA" meta="+slow"/>
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

Object.assign(window, { TripCold, TripFolio, TripLive, TripMemory });
