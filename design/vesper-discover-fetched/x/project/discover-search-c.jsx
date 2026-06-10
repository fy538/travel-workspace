// ═══════════════════════════════════════════════════════════════
// DISCOVER SEARCH · DIRECTION C — "EDITORIAL INDEX"
// Search as a refined gazetteer. Compact, typographic, organised by
// Places / Reads / Venues / Guides. Quiet hairline rows, mono
// section counts, beautiful empty + no-result states. The most
// "reference book" of the three — fast, dense, premium.
// ═══════════════════════════════════════════════════════════════

// An index header line — a category with a count, gazetteer style.
function CIndexHead({ label, count }) {
  return (
    <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', padding: '0 2px 7px', borderBottom: `0.5px solid ${T.ink}` }}>
      <span style={{ fontFamily: T.serif, fontSize: 16, fontWeight: 500, fontStyle: 'italic', color: T.ink, letterSpacing: -0.2 }}>{label}</span>
      <span style={{ fontFamily: T.mono, fontSize: 9.5, letterSpacing: 1, color: T.mute, fontWeight: 600 }}>{count}</span>
    </div>
  );
}

// A tight typographic index row — leader-dot gazetteer feel.
function CIndexRow({ name, meta, lens }) {
  return (
    <div style={{ display: 'flex', alignItems: 'baseline', gap: 8, padding: '9px 2px' }}>
      <span style={{ fontFamily: T.serif, fontSize: 15.5, color: T.ink, letterSpacing: -0.2, whiteSpace: 'nowrap' }}>{name}</span>
      {lens && <span style={{ fontSize: 8.5, letterSpacing: 1.2, fontWeight: 700, color: D.vesperDeep, textTransform: 'uppercase', flexShrink: 0 }}>{lens}</span>}
      <span style={{ flex: 1, borderBottom: `0.5px dotted ${T.muteSoft}`, transform: 'translateY(-3px)', minWidth: 12 }}/>
      <span style={{ fontFamily: T.mono, fontSize: 9, color: T.mute, fontWeight: 600, letterSpacing: 0.5, whiteSpace: 'nowrap', flexShrink: 0 }}>{meta}</span>
    </div>
  );
}

function CHeader({ query, focused }) {
  return (
    <div style={{ paddingTop: 8 }}>
      <SearchField query={query} placeholder="Look up a place, read, or venue…" focused={focused}/>
    </div>
  );
}

// ── C · EMPTY (the index at rest) ───────────────────────────────
function SearchC_Empty() {
  return (
    <Phone bg={T.bg}>
      <CHeader query="" focused/>
      <div style={{ padding: '22px 24px 0' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 4 }}>
          <span style={{ fontSize: 9.5, letterSpacing: 2, color: T.mute, fontWeight: 700 }}>THE INDEX</span>
          <span style={{ flex: 1, borderBottom: hairT }}/>
          <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.mute }}>Lisbon</span>
        </div>
        <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.mute, lineHeight: 1.45, margin: '6px 0 0' }}>
          Everything Vesper has a read on here — by kind.
        </p>
      </div>
      {[['Places', '14 cities'], ['Reads', '38 field notes'], ['Venues', '120 places to go'], ['Guides', '9 itineraries']].map(([l, c], i) => (
        <div key={l} style={{ padding: '20px 24px 0' }}>
          <CIndexHead label={l} count={c.toUpperCase()}/>
          <div style={{ paddingTop: 6 }}>
            {l === 'Places' && <><CIndexRow name="Lisbon" meta="READING" lens=""/><CIndexRow name="Porto" meta="2 SAVED"/></>}
            {l === 'Reads' && <><CIndexRow name="The hill the buses miss" lens="Insider" meta="3 MIN"/><CIndexRow name="Where fado is grief" lens="The debate" meta="5 MIN"/></>}
            {l === 'Venues' && <><CIndexRow name="Cervejaria Ramiro" meta="MARISCO"/><CIndexRow name="A Brasileira" meta="CAFÉ"/></>}
            {l === 'Guides' && <CIndexRow name="Three slow days" meta="VESPER"/>}
          </div>
        </div>
      ))}
    </Phone>
  );
}

// ── C · TYPED (grouped index results) ───────────────────────────
function SearchC_Typed() {
  return (
    <Phone bg={T.bg}>
      <CHeader query="alfama" focused={false}/>
      <div style={{ padding: '20px 24px 0', display: 'flex', alignItems: 'center', gap: 8 }}>
        <span style={{ fontFamily: T.mono, fontSize: 9.5, color: T.mute, letterSpacing: 1, fontWeight: 600 }}>9 ENTRIES</span>
        <span style={{ flex: 1, borderBottom: hairT }}/>
        <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.mute }}>in & around Lisbon</span>
      </div>
      <div style={{ padding: '16px 24px 0' }}>
        <CIndexHead label="Places" count="1"/>
        <div style={{ paddingTop: 6 }}><CIndexRow name="Alfama" meta="DISTRICT →"/></div>
      </div>
      <div style={{ padding: '18px 24px 0' }}>
        <CIndexHead label="Reads" count="3"/>
        <div style={{ paddingTop: 6 }}>
          <CIndexRow name="The hill the buses miss" lens="Insider" meta="3 MIN"/>
          <CIndexRow name="Alfama at first light" lens="A day in" meta="4 MIN"/>
          <CIndexRow name="Living with the fado houses" lens="The debate" meta="6 MIN"/>
        </div>
      </div>
      <div style={{ padding: '18px 24px 0' }}>
        <CIndexHead label="Venues" count="4"/>
        <div style={{ paddingTop: 6 }}>
          <CIndexRow name="A Tasca do Chico" meta="FADO"/>
          <CIndexRow name="Pois Café" meta="CAFÉ"/>
          <CIndexRow name="Memmo Alfama, rooftop" meta="DRINKS"/>
        </div>
      </div>
      <div style={{ padding: '20px 24px 0' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 9, padding: '11px 2px', borderTop: `0.5px solid ${T.ink}` }}>
          <Spark s={14}/>
          <span style={{ flex: 1, fontFamily: T.serif, fontStyle: 'italic', fontSize: 15, color: D.vesperDeep }}>Ask Vesper about Alfama</span>
          <span style={{ color: D.vesper, fontSize: 14 }}>→</span>
        </div>
      </div>
    </Phone>
  );
}

// ── C · NO RESULTS (elegant blank) ──────────────────────────────
function SearchC_NoResults() {
  return (
    <Phone bg={T.bg}>
      <CHeader query="qwertz" focused={false}/>
      <div style={{ padding: '70px 36px 0', textAlign: 'center' }}>
        <div style={{ fontFamily: T.serif, fontSize: 64, fontWeight: 500, color: T.muteSoft, lineHeight: 1, letterSpacing: -1 }}>—</div>
        <h2 style={{ fontFamily: T.serif, fontSize: 22, fontWeight: 500, color: T.ink, letterSpacing: -0.4, margin: '18px 0 0' }}>
          No entry for “<span style={{ fontStyle: 'italic' }}>qwertz</span>”
        </h2>
        <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 14, color: T.mute, lineHeight: 1.5, margin: '10px 0 0' }}>
          Nothing in the index matches. Check the spelling, or ask Vesper directly.
        </p>
      </div>
      <div style={{ padding: '30px 24px 0' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 9, padding: '12px 2px', borderTop: `0.5px solid ${T.ink}`, borderBottom: `0.5px solid ${T.ink}` }}>
          <Spark s={14}/>
          <span style={{ flex: 1, fontFamily: T.serif, fontStyle: 'italic', fontSize: 15, color: D.vesperDeep }}>Ask Vesper anyway</span>
          <span style={{ color: D.vesper, fontSize: 14 }}>→</span>
        </div>
      </div>
    </Phone>
  );
}

// ── C · SELECTED (district entry → re-scope) ────────────────────
function SearchC_Selected() {
  return (
    <Phone bg={T.bg}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <Plate variant="tiles" style={{ height: 196 }} dim={0.18}>
          <div style={{ position: 'absolute', top: 14, left: 16 }}>{DIcon.back('#fff')}</div>
          <div style={{ position: 'absolute', left: 18, bottom: 15 }}>
            <div style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 2, color: 'rgba(255,255,255,0.82)', fontWeight: 600 }}>DISTRICT · LISBON</div>
            <h1 style={{ fontFamily: T.serif, fontSize: 34, fontWeight: 500, color: '#fff', letterSpacing: -0.7, margin: '5px 0 0' }}>Alfama</h1>
          </div>
        </Plate>
        <div style={{ padding: '18px 24px 0' }}>
          <p style={{ fontFamily: T.serif, fontSize: 16, color: T.inkSoft, lineHeight: 1.55, margin: 0 }}>
            The oldest quarter — a knot of stairs and washing lines above the river. Vesper now reads Discover from here.
          </p>
        </div>
        <div style={{ padding: '18px 24px 0' }}>
          <CIndexHead label="Worth your time" count="7"/>
          <div style={{ paddingTop: 6 }}>
            <CIndexRow name="The hill the buses miss" lens="Insider" meta="3 MIN"/>
            <CIndexRow name="A Tasca do Chico" meta="FADO"/>
            <CIndexRow name="Pois Café" meta="CAFÉ"/>
          </div>
        </div>
        <div style={{ position: 'absolute', left: 0, right: 0, bottom: 0, padding: '14px 24px calc(14px + 8px)', background: 'rgba(247,242,231,0.92)', backdropFilter: 'blur(18px)', borderTop: hair, display: 'flex', alignItems: 'center', gap: 10 }}>
          <span style={{ flex: 1, fontFamily: T.serif, fontStyle: 'italic', fontSize: 14.5, color: T.inkSoft }}>Reading Discover from Alfama</span>
          <span style={{ fontFamily: T.sans, fontSize: 12.5, fontWeight: 600, color: D.vesperDeep }}>Open the read →</span>
        </div>
      </div>
    </Phone>
  );
}

Object.assign(window, { SearchC_Empty, SearchC_Typed, SearchC_NoResults, SearchC_Selected });
