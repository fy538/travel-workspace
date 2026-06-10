// ═══════════════════════════════════════════════════════════════
// VESPER · PLACES v2 — Place/city, lens-led (NOT a Take).
// A place's spine is the lensed editorial reads (travel_lens:
// why_here · day_in · affinity · insider · tension · ritual — each a
// dossier thesis). Feature 2–3, never all six. Then the aggregation
// rooms as counts/entries. Reuses PlaceHero, Room, SpotChip, HoodRow.
// ═══════════════════════════════════════════════════════════════

const LENS = {
  why_here: { label: 'WHY HERE', variant: 'hills' },
  day_in:   { label: 'A DAY IN', variant: 'square' },
  affinity: { label: 'YOUR AFFINITY', variant: 'alley' },
  insider:  { label: 'INSIDER', variant: 'tiles' },
  tension:  { label: 'THE TENSION', variant: 'coast' },
  ritual:   { label: 'A RITUAL', variant: 'rooftops' },
};

// the featured lens — a dossier thesis, editorial
function LensFeature({ lens, thesis, read = '4 min', lead }) {
  const l = LENS[lens];
  return (
    <div style={{ borderRadius: 16, overflow: 'hidden', border: hp, background: T.cardWarm }}>
      <div style={{ position: 'relative', height: lead ? 150 : 0 }}>
        {lead && <><Plate variant={l.variant} style={{ height: 150 }} dim={0.14}/>
          <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to top, rgba(20,14,9,0.55), transparent 60%)' }}/>
          <div style={{ position: 'absolute', left: 14, bottom: 12 }}>
            <span style={{ fontSize: 9, letterSpacing: 1.8, fontWeight: 700, color: 'rgba(255,255,255,0.9)' }}>{l.label}</span>
          </div>
        </>}
      </div>
      <div style={{ padding: '14px 16px' }}>
        {!lead && <span style={{ fontSize: 9, letterSpacing: 1.8, fontWeight: 700, color: T.goldDeep }}>{l.label}</span>}
        <p style={{ fontFamily: T.serif, fontSize: lead ? 18 : 16, fontWeight: 500, color: T.ink, lineHeight: 1.28, letterSpacing: -0.3, margin: lead ? '0' : '7px 0 0' }}>{thesis}</p>
        <div style={{ marginTop: 9, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <span style={{ display: 'inline-flex', alignItems: 'center', gap: 6 }}><VesperMark s={11}/><span style={{ fontSize: 10.5, color: T.goldDeep, fontWeight: 600 }}>Vesper’s read</span></span>
          <span style={{ fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1 }}>{read} · READ →</span>
        </div>
      </div>
    </div>
  );
}

// ─── PLACE · CITY, lens-led (trip mode, rich) ───────────────────
function PlaceCityV2() {
  return (
    <Phone bg={T.bg}>
      <SpotBody pad={40}>
        <PlaceHero variant="hills" name="Lisbon" kind="CITY · PORTUGAL" ctx="YOUR TRIP · MAY 5–13" rel="your third time — you keep coming back for the quiet, food-first corners."/>
        <div style={{ padding: '22px 18px 0', display: 'flex', flexDirection: 'column', gap: 24 }}>
          {/* the spine: 2–3 featured lenses (NOT a Take) */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: 13 }}>
            <div style={{ display: 'flex', alignItems: 'baseline', gap: 10 }}>
              <Eye>VESPER ON LISBON</Eye>
              <span style={{ flex: 1, height: 1, background: T.hairline }}/>
              <span style={{ fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1, fontWeight: 600 }}>6 LENSES</span>
            </div>
            <LensFeature lens="affinity" lead thesis="The city rewards exactly what you already love — eat east, walk the hills, skip the trams."/>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 11 }}>
              <LensFeature lens="insider" thesis="The miradouro everyone photographs is the wrong one. Yours is one hill north."/>
              <LensFeature lens="tension" thesis="Lisbon is being loved to death — go early, tip well, and stay out of the cruise-ship hours."/>
            </div>
            <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: INKBLUE, alignSelf: 'flex-start' }}>three more lenses — why here · a day in · a ritual →</span>
          </div>

          {/* before-you-go (trip mode) */}
          <div style={{ padding: '14px 16px', background: 'rgba(61,80,102,0.07)', borderRadius: 14, border: `0.5px solid rgba(61,80,102,0.2)` }}>
            <Eye c={INKBLUE}>WHAT TO LOCK IN</Eye>
            <div style={{ marginTop: 10, display: 'flex', flexDirection: 'column', gap: 8 }}>
              {[['Where you sleep', 'Príncipe Real held · 4 nights'], ['The one dinner', 'Eurico — go the first night'], ['Fado, done right', 'Mesa de Frades · late seating']].map(([a, b]) => (
                <div key={a} style={{ display: 'flex', alignItems: 'baseline', gap: 8 }}>
                  <span style={{ width: 6, height: 6, borderRadius: 6, background: INKBLUE, flexShrink: 0, transform: 'translateY(-2px)' }}/>
                  <span style={{ fontFamily: T.serif, fontSize: 14, color: T.ink }}>{a} — <span style={{ color: T.mute, fontStyle: 'italic' }}>{b}</span></span>
                </div>
              ))}
            </div>
          </div>

          {/* aggregation rooms — counts & entries */}
          <Room label="YOUR SAVED SPOTS HERE" count="6" action="map">
            <HScroll>
              <SpotChip name="O Velho Eurico" type="WINE BAR · ALFAMA" variant="alley"/>
              <SpotChip name="Casa do Alecrim" type="STAY · P. REAL" variant="rooftops"/>
              <SpotChip name="Graça miradouro" type="VIEW · GRAÇA" variant="hills"/>
            </HScroll>
          </Room>

          <Room label="YOUR MEMORIES HERE" count="2 POSTCARDS" action="atlas">
            <div style={{ display: 'flex', gap: 11 }}>
              <div style={{ flex: 1, padding: 9, background: T.cardWarm, borderRadius: 12, border: hp, transform: 'rotate(-1.4deg)', boxShadow: '0 10px 22px -16px rgba(0,0,0,0.4)' }}>
                <div style={{ height: 74, borderRadius: 7, overflow: 'hidden' }}><Plate variant="coast" style={{ height: 74 }}/></div>
                <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.inkSoft, marginTop: 6 }}>“the last evening, 2023”</div>
              </div>
              <div style={{ flex: 1, padding: 9, background: T.cardWarm, borderRadius: 12, border: hp, transform: 'rotate(1deg)', boxShadow: '0 10px 22px -16px rgba(0,0,0,0.4)' }}>
                <div style={{ height: 74, borderRadius: 7, overflow: 'hidden' }}><Plate variant="square" style={{ height: 74 }}/></div>
                <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.inkSoft, marginTop: 6 }}>“that lunch in Alfama”</div>
              </div>
            </div>
          </Room>

          <Room label="NEIGHBORHOODS" count="DRILL IN">
            <div>
              <HoodRow name="Alfama" note="where you keep returning" spots="14 SPOTS"/>
              <HoodRow name="Graça" note="the light, just above" spots="6 SPOTS"/>
              <HoodRow name="Príncipe Real" note="where you’ll sleep" spots="9 SPOTS"/>
            </div>
          </Room>

          <Room label="WHAT’S HAPPENING" count="WHILE YOU’RE THERE" action="all">
            <div style={{ display: 'flex', alignItems: 'center', gap: 13, padding: '12px 14px', background: T.card, borderRadius: 13, border: hp }}>
              <div style={{ width: 44, textAlign: 'center' }}>
                <div style={{ fontFamily: T.serif, fontSize: 21, color: T.goldDeep, fontWeight: 600, lineHeight: 1 }}>9</div>
                <Eye>MAY</Eye>
              </div>
              <div style={{ flex: 1, borderLeft: hp, paddingLeft: 13 }}>
                <div style={{ fontFamily: T.serif, fontSize: 15, fontWeight: 500, color: T.ink }}>Festa do vinho, Alfama</div>
                <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.mute, marginTop: 1 }}>your kind of night — falls right in your week</div>
              </div>
              <span style={{ color: T.muteSoft }}>→</span>
            </div>
          </Room>
        </div>
      </SpotBody>
      <TabBar active="discover"/>
    </Phone>
  );
}

Object.assign(window, { LENS, LensFeature, PlaceCityV2 });
