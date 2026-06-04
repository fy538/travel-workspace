// ═══════════════════════════════════════════════════════════════
// DISCOVER · SEARCH — three directions for "how Vesper looks".
// Not web search: search as changing where Vesper is reading, or
// telling Vesper a fuzzy desire, or browsing a refined gazetteer.
//
// Language is the Discover kit: parchment (T.bg/card), restrained
// ink, gold/earth accents, and VIOLET (D.vesper) ONLY when Vesper
// is interpreting/speaking. Reuses Phone, T, D, Plate, DIcon, Spark,
// VesperBy, LensChip, FieldEyebrow.
// ═══════════════════════════════════════════════════════════════

// ─── shared search atoms ────────────────────────────────────────

// The field — focused (with a live caret or a query) + a Cancel.
function SearchField({ query, placeholder = 'Search places, restaurants, cities…', focused = true }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '0 18px' }}>
      <div style={{ flex: 1, minWidth: 0, display: 'flex', alignItems: 'center', gap: 10, padding: '11px 14px', background: T.cardWarm, borderRadius: 999, border: `0.5px solid ${focused ? D.vesperRule : T.hairline}` }}>
        {DIcon.search(query ? T.inkSoft : T.mute)}
        {focused && !query && <span style={{ width: 1.5, height: 18, background: D.vesper, flexShrink: 0 }}/>}
        {query
          ? <span style={{ fontSize: 15, color: T.ink, letterSpacing: -0.1, whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>{query}</span>
          : <span style={{ fontSize: 14.5, color: T.muteSoft, letterSpacing: -0.1, whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis', flex: 1 }}>{placeholder}</span>}
        {query && <span style={{ marginLeft: 'auto', display: 'flex' }}><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke={T.muteSoft} strokeWidth="2" strokeLinecap="round"><circle cx="12" cy="12" r="9" fill="rgba(27,23,20,0.08)" stroke="none"/><path d="M9 9l6 6M15 9l-6 6"/></svg></span>}
      </div>
      <span style={{ fontFamily: T.sans, fontSize: 14.5, color: D.vesperDeep, fontWeight: 500 }}>Cancel</span>
    </div>
  );
}

// Section label inside results.
function SearchGroup({ children, right }) {
  return (
    <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', padding: '0 4px 9px' }}>
      <span style={{ fontSize: 9.5, letterSpacing: 1.9, color: T.mute, fontWeight: 700 }}>{children}</span>
      {right && <span style={{ fontSize: 9.5, letterSpacing: 1, color: T.muteSoft, fontWeight: 600 }}>{right}</span>}
    </div>
  );
}

// The "Ask Vesper" escape hatch — a violet conversational row.
function AskVesperRow({ q = 'fado but not touristy' }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '13px 14px', borderRadius: 14, background: D.vesperSoft, border: `0.5px solid ${D.vesperRule}` }}>
      <Spark s={17}/>
      <div style={{ flex: 1 }}>
        <div style={{ fontFamily: T.sans, fontSize: 13.5, color: D.vesperDeep, fontWeight: 600, letterSpacing: -0.1 }}>Ask Vesper about “{q}”</div>
        <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.mute, marginTop: 1 }}>talk it through, don’t just search</div>
      </div>
      <span style={{ color: D.vesper, fontSize: 15 }}>→</span>
    </div>
  );
}

// A place row (city) — selecting re-scopes Discover.
function PlaceRow({ name, sub, glyph = 'rooftops', live, you }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 13, padding: '10px 4px' }}>
      <div style={{ width: 46, height: 46, borderRadius: 11, overflow: 'hidden', flexShrink: 0, border: `0.5px solid ${T.hairline}` }}><Plate variant={glyph} style={{ height: 46 }}/></div>
      <div style={{ flex: 1, minWidth: 0 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 7 }}>
          <span style={{ fontFamily: T.serif, fontSize: 18, fontWeight: 500, color: T.ink, letterSpacing: -0.3 }}>{name}</span>
          {live && <span style={{ fontSize: 8, letterSpacing: 1, fontWeight: 700, color: D.earth, border: `0.5px solid ${D.earth}`, borderRadius: 4, padding: '1px 4px' }}>HERE</span>}
          {you && <span style={{ fontSize: 8, letterSpacing: 1, fontWeight: 700, color: T.gold, border: `0.5px solid ${T.goldSoft}`, borderRadius: 4, padding: '1px 4px' }}>YOUR TRIP</span>}
        </div>
        <div style={{ fontSize: 12, color: T.mute, marginTop: 1, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>{sub}</div>
      </div>
      <span style={{ fontFamily: T.mono, fontSize: 8.5, letterSpacing: 1, color: T.muteSoft, fontWeight: 600 }}>READ →</span>
    </div>
  );
}

// A venue / place-to-go row.
function VenueRow({ name, kind, hook, glyph = 'alley' }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 13, padding: '10px 4px' }}>
      <div style={{ width: 40, height: 40, borderRadius: 9, overflow: 'hidden', flexShrink: 0, border: `0.5px solid ${T.hairline}` }}><Plate variant={glyph} style={{ height: 40 }}/></div>
      <div style={{ flex: 1, minWidth: 0 }}>
        <div style={{ fontFamily: T.serif, fontSize: 15.5, fontWeight: 500, color: T.ink, letterSpacing: -0.2, lineHeight: 1.15 }}>{name}</div>
        <div style={{ fontSize: 11.5, color: T.mute, marginTop: 1, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>{hook}</div>
      </div>
      <span style={{ fontFamily: T.mono, fontSize: 8, letterSpacing: 0.8, color: T.muteSoft, fontWeight: 700 }}>{kind}</span>
    </div>
  );
}

// A field-note / dossier result row (violet lens).
function ReadRow({ title, lens, place }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '11px 4px' }}>
      <span style={{ flexShrink: 0 }}>{DIcon.read(D.vesper)}</span>
      <div style={{ flex: 1, minWidth: 0 }}>
        <div style={{ fontFamily: T.serif, fontSize: 15, fontWeight: 500, color: T.ink, letterSpacing: -0.2, lineHeight: 1.2 }}>{title}</div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginTop: 3 }}>
          <span style={{ fontSize: 9, letterSpacing: 1.4, fontWeight: 700, color: D.vesperDeep, textTransform: 'uppercase' }}>{lens}</span>
          <span style={{ color: T.muteSoft, fontSize: 10 }}>·</span>
          <span style={{ fontSize: 11, color: T.mute }}>{place}</span>
        </div>
      </div>
      <span style={{ color: T.muteSoft, fontSize: 14 }}>→</span>
    </div>
  );
}

const hair = `0.5px solid ${T.hairline}`;
const hairT = `0.5px solid ${T.hairThin}`;

Object.assign(window, { SearchField, SearchGroup, AskVesperRow, PlaceRow, VenueRow, ReadRow });
