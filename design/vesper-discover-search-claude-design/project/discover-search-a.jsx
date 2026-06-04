// ═══════════════════════════════════════════════════════════════
// DISCOVER SEARCH · DIRECTION A — "PLACE SWITCHER"
// Search = changing the city/place Vesper is reading. Strong active
// place context up top; empty state is recent + saved + suggested
// cities; typed results lead with Places (re-scope), then reads,
// then venues. Selecting a city = a calm "now reading" transition.
// ═══════════════════════════════════════════════════════════════

// Active-context banner — what Vesper is reading right now.
function ANowReading({ place = 'Lisbon', note = 'tuned to your taste' }) {
  return (
    <div style={{ margin: '16px 18px 0', padding: '13px 16px', background: T.card, borderRadius: 14, border: hair, display: 'flex', alignItems: 'center', gap: 12 }}>
      <div style={{ width: 38, height: 38, borderRadius: 9, overflow: 'hidden', flexShrink: 0 }}><Plate variant="rooftops" style={{ height: 38 }}/></div>
      <div style={{ flex: 1 }}>
        <div style={{ fontSize: 9, letterSpacing: 1.6, color: T.mute, fontWeight: 700 }}>VESPER IS READING</div>
        <div style={{ display: 'flex', alignItems: 'baseline', gap: 7, marginTop: 2 }}>
          <span style={{ fontFamily: T.serif, fontSize: 20, fontWeight: 500, color: T.ink, letterSpacing: -0.4 }}>{place}</span>
          <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.mute }}>· {note}</span>
        </div>
      </div>
    </div>
  );
}

function ASearchHeader({ query, focused = true }) {
  return (
    <div style={{ paddingTop: 8 }}>
      <SearchField query={query} focused={focused}/>
    </div>
  );
}

// ── A · EMPTY (before typing) ───────────────────────────────────
function SearchA_Empty() {
  const recents = [['Tokyo', 'read 3 days ago', 'hills'], ['Mexico City', 'saved', 'square'], ['Copenhagen', 'read last week', 'coast']];
  const cities = [['Porto', 'an easy second city', 'alley'], ['Tangier', 'across the water', 'square'], ['San Sebastián', 'for the eating', 'coast']];
  return (
    <Phone bg={T.bg}>
      <ASearchHeader query="" />
      <ANowReading/>
      <div style={{ padding: '20px 22px 0' }}>
        <SearchGroup right="EDIT">RECENT</SearchGroup>
        <div style={{ display: 'flex', flexDirection: 'column' }}>
          {recents.map(([n, s, g], i) => <div key={n} style={{ borderTop: i ? hairT : 'none' }}><PlaceRow name={n} sub={s} glyph={g}/></div>)}
        </div>
      </div>
      <div style={{ padding: '20px 22px 0' }}>
        <SearchGroup>WHERE VESPER WOULD SEND YOU NEXT</SearchGroup>
        <div style={{ display: 'flex', flexDirection: 'column' }}>
          {cities.map(([n, s, g], i) => <div key={n} style={{ borderTop: i ? hairT : 'none' }}><PlaceRow name={n} sub={s} glyph={g}/></div>)}
        </div>
      </div>
      <div style={{ padding: '22px 22px 0', display: 'flex', alignItems: 'center', gap: 8, color: T.mute }}>
        <Spark s={13}/>
        <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.mute }}>Or tell Vesper what you’re in the mood for.</span>
      </div>
    </Phone>
  );
}

// ── A · TYPED (results) ─────────────────────────────────────────
function SearchA_Typed() {
  return (
    <Phone bg={T.bg}>
      <ASearchHeader query="tok" />
      <div style={{ padding: '22px 22px 0' }}>
        <SearchGroup>CHANGE WHERE VESPER LOOKS</SearchGroup>
        <div style={{ display: 'flex', flexDirection: 'column' }}>
          <PlaceRow name="Tokyo" sub="Japan · you read this 3 days ago" glyph="hills"/>
          <div style={{ borderTop: hairT }}><PlaceRow name="Tokushima" sub="Shikoku · the whirlpools & Awa dance" glyph="coast"/></div>
        </div>
      </div>
      <div style={{ padding: '20px 22px 0' }}>
        <SearchGroup>READS</SearchGroup>
        <ReadRow title="Tokyo without the checklist" lens="Why here" place="Tokyo"/>
        <div style={{ borderTop: hairT }}><ReadRow title="The city’s last great kissaten" lens="For the obsessed" place="Tokyo"/></div>
      </div>
      <div style={{ padding: '20px 22px 0' }}>
        <SearchGroup>PLACES TO GO</SearchGroup>
        <VenueRow name="Toki, in Sangenjaya" kind="IZAKAYA" hook="Eight seats, no sign, counter only" glyph="alley"/>
      </div>
      <div style={{ padding: '20px 22px 0' }}>
        <AskVesperRow q="tok"/>
      </div>
    </Phone>
  );
}

// ── A · NO RESULTS ──────────────────────────────────────────────
function SearchA_NoResults() {
  return (
    <Phone bg={T.bg}>
      <ASearchHeader query="Ittoqqortoormiit" />
      <div style={{ padding: '40px 30px 0', textAlign: 'center' }}>
        <div style={{ display: 'inline-flex', marginBottom: 16, opacity: 0.5 }}>{DIcon.search(T.muteSoft)}</div>
        <h2 style={{ fontFamily: T.serif, fontSize: 23, fontWeight: 500, color: T.ink, letterSpacing: -0.4, lineHeight: 1.2, margin: 0 }}>
          Vesper hasn’t formed a read on <span style={{ fontStyle: 'italic' }}>Ittoqqortoormiit</span> yet.
        </h2>
        <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 14.5, color: T.mute, lineHeight: 1.5, margin: '12px 0 0' }}>
          It’s off the edge of the map I know well — but I can look, if you want to go.
        </p>
      </div>
      <div style={{ padding: '26px 22px 0' }}>
        <AskVesperRow q="Ittoqqortoormiit"/>
      </div>
      <div style={{ padding: '22px 22px 0' }}>
        <SearchGroup>DID YOU MEAN</SearchGroup>
        <PlaceRow name="Iceland" sub="the nearest read I have" glyph="coast"/>
      </div>
    </Phone>
  );
}

// ── A · SELECTED (re-scope transition) ──────────────────────────
function SearchA_Selected() {
  return (
    <Phone bg={T.bg}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54 }}>
        <Plate variant="hills" style={{ position: 'absolute', inset: 0, height: '100%' }} dim={0.34}/>
        <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.1), rgba(20,14,9,0.55))' }}/>
        <div style={{ position: 'relative', height: '100%', display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', padding: '0 40px', textAlign: 'center' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 14 }}>
            <Spark s={15} c="rgba(255,255,255,0.95)"/>
            <span style={{ fontSize: 10, letterSpacing: 2, fontWeight: 700, color: 'rgba(255,255,255,0.85)' }}>NOW READING</span>
          </div>
          <h1 style={{ fontFamily: T.serif, fontSize: 44, fontWeight: 500, color: '#fff', letterSpacing: -1, margin: 0, lineHeight: 0.98 }}>Tokyo</h1>
          <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 15.5, color: 'rgba(255,255,255,0.9)', lineHeight: 1.5, margin: '14px 0 0', maxWidth: 280 }}>
            Re-tuning Discover to the city — your reads, your friends’ saves, the canon.
          </p>
          <div style={{ marginTop: 26, display: 'flex', gap: 5 }}>
            {[0, 1, 2].map((i) => <span key={i} style={{ width: 6, height: 6, borderRadius: 6, background: i === 0 ? '#fff' : 'rgba(255,255,255,0.4)' }}/>)}
          </div>
        </div>
      </div>
    </Phone>
  );
}

Object.assign(window, { SearchA_Empty, SearchA_Typed, SearchA_NoResults, SearchA_Selected });
