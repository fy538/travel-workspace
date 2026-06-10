// ═══════════════════════════════════════════════════════════════
// VESPER · PLACES — Surface 2: Place (the new parent/aggregator).
// City ⊃ Neighborhood ⊃ Spot. Leads with the Place's own Take, then
// paper "rooms": The Read · Saved here · Memories · Trips · Map ·
// Neighborhoods · What's happening. Two modes: trip-city (before you
// go) vs home-city (ongoing relationship). + a neighborhood (recursion).
// ═══════════════════════════════════════════════════════════════

// place hero — riso skyline + name + your-relationship line
function PlaceHero({ variant = 'hills', name, kind, rel, ctx }) {
  return (
    <div style={{ position: 'relative' }}>
      <div style={{ height: 268 }}>
        <Plate variant={variant} style={{ height: 268 }} dim={0.2}/>
        <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.42), rgba(20,14,9,0.06) 36%, rgba(20,14,9,0.66))' }}/>
      </div>
      <SpotTopBar onDark label={ctx}/>
      <div style={{ position: 'absolute', left: 22, right: 22, bottom: 20 }}>
        <Eye c="rgba(255,255,255,0.78)">{kind}</Eye>
        <h1 style={{ fontFamily: T.serif, fontSize: 46, fontWeight: 500, color: '#fff', letterSpacing: -1.1, lineHeight: 0.96, margin: '7px 0 0' }}>{name}</h1>
        <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginTop: 11 }}>
          <VesperMark s={13} c={T.goldSoft}/>
          <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 14, color: 'rgba(255,255,255,0.92)', letterSpacing: -0.1 }}>{rel}</span>
        </div>
      </div>
    </div>
  );
}

// a paper "room" — section header + content
function Room({ label, count, children, action }) {
  return (
    <div>
      <div style={{ display: 'flex', alignItems: 'baseline', gap: 10, marginBottom: 12 }}>
        <Eye>{label}</Eye>
        {count && <span style={{ fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1, fontWeight: 600 }}>{count}</span>}
        <span style={{ flex: 1, height: 1, background: T.hairline }}/>
        {action && <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: INKBLUE }}>{action} →</span>}
      </div>
      {children}
    </div>
  );
}

// small saved-spot card
function SpotChip({ name, type, variant }) {
  return (
    <div style={{ width: 150, flexShrink: 0 }}>
      <div style={{ height: 96, borderRadius: 12, overflow: 'hidden', border: hp }}><Plate variant={variant} style={{ height: 96 }}/></div>
      <div style={{ fontFamily: T.serif, fontSize: 15, fontWeight: 500, color: T.ink, letterSpacing: -0.2, marginTop: 7, lineHeight: 1.1 }}>{name}</div>
      <Eye>{type}</Eye>
    </div>
  );
}

function HScroll({ children }) {
  return <div style={{ display: 'flex', gap: 11, overflow: 'hidden', paddingRight: 18 }}>{children}</div>;
}

// neighborhood drill row
function HoodRow({ name, spots, note, last }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 13, padding: '13px 0', borderTop: hpT }}>
      <div style={{ flex: 1 }}>
        <div style={{ fontFamily: T.serif, fontSize: 17, fontWeight: 500, color: T.ink, letterSpacing: -0.3 }}>{name}</div>
        <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.mute, marginTop: 2 }}>{note}</div>
      </div>
      <span style={{ fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 0.8, fontWeight: 600 }}>{spots}</span>
      <span style={{ color: T.muteSoft, fontSize: 15 }}>→</span>
    </div>
  );
}

// ─── PLACE · CITY, trip-mode, RICH ──────────────────────────────
function PlaceCityRich() {
  return (
    <Phone bg={T.bg}>
      <SpotBody pad={40}>
        <PlaceHero variant="hills" name="Lisbon" kind="CITY · PORTUGAL" ctx="YOUR TRIP · MAY 5–13" rel="your third time — you keep coming back for the quiet, food-first corners."/>
        <div style={{ padding: '22px 18px 0', display: 'flex', flexDirection: 'column', gap: 24 }}>
          {/* the place's own Take */}
          <TakeBlock
            state="rich"
            verdict="Stay east, eat early, and don’t over-plan the hills."
            body="You’ve done the postcard Lisbon. This time it’s about the streets above the river — Alfama mornings, Graça light, the tascas you keep saving. Lock the ryokan-equivalent and leave the afternoons loose."
            pill="BEFORE YOU GO · 3 THINGS TO LOCK"
            curator="A river city of hills and tiles; the south-facing miradouros and the old eastern quarters are the soul of it."
            why={['you return for the quiet corners', '6 spots already saved', 'you travel food-first']}
          />

          {/* before-you-go strip (trip mode) */}
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

          {/* The Read */}
          <Room label="THE READ" count="4 DOSSIERS" action="all">
            <HScroll>
              <SpotChip name="Where Lisbon drinks natural" type="A VESPER READ" variant="alley"/>
              <SpotChip name="The hill the buses miss" type="INSIDER" variant="hills"/>
              <SpotChip name="Tiles, and where to find them" type="A DAY IN" variant="tiles"/>
            </HScroll>
          </Room>

          {/* Saved here */}
          <Room label="YOUR SAVED SPOTS HERE" count="6" action="map">
            <HScroll>
              <SpotChip name="O Velho Eurico" type="WINE BAR · ALFAMA" variant="alley"/>
              <SpotChip name="Casa do Alecrim" type="STAY · P. REAL" variant="rooftops"/>
              <SpotChip name="Graça miradouro" type="VIEW · GRAÇA" variant="hills"/>
            </HScroll>
          </Room>

          {/* Memories (Atlas postcards) */}
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

          {/* Neighborhoods — the recursion */}
          <Room label="NEIGHBORHOODS" count="DRILL IN">
            <div>
              <HoodRow name="Alfama" note="where you keep returning" spots="14 SPOTS"/>
              <HoodRow name="Graça" note="the light, just above" spots="6 SPOTS"/>
              <HoodRow name="Príncipe Real" note="where you’ll sleep" spots="9 SPOTS"/>
            </div>
          </Room>

          {/* What's happening */}
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

// ─── PLACE · CITY, home-mode, but COLD (no relationship) ────────
function PlaceCityCold() {
  return (
    <Phone bg={T.bg}>
      <SpotBody pad={40}>
        <PlaceHero variant="coast" name="Valencia" kind="CITY · SPAIN" ctx="NEW TO YOU" rel="we haven’t been here together yet."/>
        <div style={{ padding: '22px 18px 0', display: 'flex', flexDirection: 'column', gap: 24 }}>
          <TakeBlock
            state="cold"
            verdict="A warm, low-rise city that rewards slowness."
            curator="Spain’s third city, between an old walled core and a long beach; the dry riverbed park threads the two, and the food is rice, citrus, and horchata."
          />

          {/* cold-start building prompt */}
          <div style={{ padding: '16px', background: T.cardWarm, borderRadius: 14, border: hp, textAlign: 'center' }}>
            <VesperMark s={20}/>
            <p style={{ fontFamily: T.serif, fontSize: 16, color: T.ink, lineHeight: 1.4, margin: '10px 0 0' }}>Start a relationship with Valencia.</p>
            <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.mute, lineHeight: 1.45, margin: '6px 16px 0' }}>Save a spot, read a dossier, or just tell me what draws you here — I’ll start a read.</p>
            <div style={{ marginTop: 13, display: 'flex', gap: 8, justifyContent: 'center' }}>
              <span style={{ padding: '8px 14px', borderRadius: 999, background: INKBLUE, color: '#fff', fontSize: 12.5, fontWeight: 600 }}>Plan a trip here</span>
              <span style={{ padding: '8px 14px', borderRadius: 999, border: `0.8px solid ${T.gold}`, color: T.goldDeep, fontSize: 12.5, fontWeight: 600 }}>Ask Vesper</span>
            </div>
          </div>

          {/* curator-only rooms still present */}
          <Room label="THE READ" count="START HERE" action="all">
            <HScroll>
              <SpotChip name="Valencia, beyond the paella" type="WHY HERE" variant="coast"/>
              <SpotChip name="The river that became a park" type="A DAY IN" variant="square"/>
            </HScroll>
          </Room>

          <Room label="NEIGHBORHOODS" count="DRILL IN">
            <div>
              <HoodRow name="El Carmen" note="the old walled heart" spots="CURATOR"/>
              <HoodRow name="Ruzafa" note="where the city eats now" spots="CURATOR"/>
              <HoodRow name="La Malvarrosa" note="the long beach" spots="CURATOR"/>
            </div>
          </Room>
        </div>
      </SpotBody>
      <TabBar active="discover"/>
    </Phone>
  );
}

// ─── PLACE · NEIGHBORHOOD (the recursion, home-city mode) ────────
function PlaceHood() {
  return (
    <Phone bg={T.bg}>
      <SpotBody pad={40}>
        <PlaceHero variant="alley" name="Alfama" kind="NEIGHBORHOOD · LISBON ↑" ctx="YOUR HOME-CITY" rel="the corner you keep returning to — 14 spots, 5 years."/>
        <div style={{ padding: '22px 18px 0', display: 'flex', flexDirection: 'column', gap: 24 }}>
          <TakeBlock
            state="rich"
            verdict="This is your Lisbon — lean all the way in."
            body="Five years of saves say the same thing: you come for the morning quiet before the trams fill, the tascas on the back stairs, and the one miradouro you always end up at. You don’t need a plan here. You need a table."
            pill="YOUR CORNER"
            curator="The oldest quarter — a knot of stairs and washing lines above the river, dense with fado houses and tiny restaurants."
            why={['14 saves over 5 years', 'you always end at the same view', 'food-first, plan-light']}
          />

          <Room label="YOUR SPOTS HERE" count="14" action="map">
            <HScroll>
              <SpotChip name="O Velho Eurico" type="WINE BAR" variant="alley"/>
              <SpotChip name="Pois Café" type="CAFÉ" variant="square"/>
              <SpotChip name="The miradouro" type="VIEW" variant="hills"/>
            </HScroll>
          </Room>

          <Room label="YOUR MEMORIES HERE" count="5 POSTCARDS" action="atlas">
            <div style={{ display: 'flex', gap: 11 }}>
              {['coast', 'tiles', 'square'].map((v, i) => (
                <div key={i} style={{ flex: 1, padding: 8, background: T.cardWarm, borderRadius: 11, border: hp, transform: `rotate(${[-1.5, 0.8, -0.6][i]}deg)` }}>
                  <div style={{ height: 58, borderRadius: 6, overflow: 'hidden' }}><Plate variant={v} style={{ height: 58 }}/></div>
                </div>
              ))}
            </div>
          </Room>

          <Room label="WHAT’S NEW HERE" count="SINCE YOU LAST CAME" action="all">
            <div style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '12px 14px', background: T.card, borderRadius: 13, border: hp }}>
              <span style={{ width: 30, height: 30, borderRadius: 8, background: 'rgba(176,133,58,0.12)', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}><VesperMark s={15}/></span>
              <div style={{ flex: 1 }}>
                <div style={{ fontFamily: T.serif, fontSize: 14.5, fontWeight: 500, color: T.ink }}>A new wine room two doors from Eurico</div>
                <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.mute, marginTop: 1 }}>opened in March · exactly your kind of place</div>
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

Object.assign(window, { PlaceHero, Room, SpotChip, HoodRow, PlaceCityRich, PlaceCityCold, PlaceHood });
