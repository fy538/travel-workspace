// ═══════════════════════════════════════════════════════════════
// LIVE HOME = THE FOLIO, ZOOMED TO NOW. During the trip the home is
// the itinerary focused on what's happening now + next, Vesper woven
// into the beats, the 4 facet blocks as a quiet footer. Same Folio,
// just zoomed. Distinct from the Vesper tab (which owns the ambient
// "what now" moment). Reuses DR, StyleRiso, EdKick, ed, FT_ICON.
// ═══════════════════════════════════════════════════════════════

const LIH = 852;
const gold = DR.goldDeep;

// Slim today-header — a warm sliver, not a big cover.
function TodayHeader({ time, place = 'LISBON', tod }) {
  return (
    <div style={{ position: 'relative', height: 96, marginTop: -40 }}>
      <div style={{ position: 'absolute', inset: 0, filter: tod === 'evening' ? 'saturate(0.9) brightness(0.72)' : (tod === 'morning' ? 'brightness(1.05)' : 'none') }}><StyleRiso w={393} h={96}/></div>
      <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.4), rgba(20,14,9,0.12) 55%, rgba(20,14,9,0.5))' }}/>
      <div style={{ position: 'absolute', top: 48, left: 20, right: 20, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.92)" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
        <span style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 2.2, color: 'rgba(255,255,255,0.85)', fontWeight: 600 }}>DAY 3 · TUE{time ? ` · ${time}` : ''}</span>
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.92)" strokeWidth="1.6" strokeLinecap="round"><circle cx="5" cy="12" r="1.4"/><circle cx="12" cy="12" r="1.4"/><circle cx="19" cy="12" r="1.4"/></svg>
      </div>
      <div style={{ position: 'absolute', left: 22, bottom: 10 }}>
        <span style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 2.6, color: 'rgba(255,255,255,0.8)', fontWeight: 600 }}>{place}</span>
      </div>
    </div>
  );
}

// Quiet 4-facet footer — live values, taps into each detail page.
function FacetFooter() {
  const cells = [[FT_ICON.transport, '4:50', 'TRAM 28'], [FT_ICON.stay, 'Alecrim', 'TONIGHT'], [FT_ICON.costs, '€42', 'TODAY'], [FT_ICON.route, 'map', 'ROUTE']];
  return (
    <div style={{ padding: '18px 22px 0' }}>
      <div style={{ display: 'flex', gap: 8, paddingTop: 15, borderTop: ed.rule }}>
        {cells.map(([ic, v, l], i) => (
          <div key={i} style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 5 }}>
            <span style={{ color: DR.soft }}>{ic}</span>
            <span style={{ fontFamily: DR.serif, fontSize: 13.5, color: DR.ink, fontWeight: 500, letterSpacing: -0.2, lineHeight: 1 }}>{v}</span>
            <span style={{ fontFamily: DR.mono, fontSize: 7, letterSpacing: 1, color: DR.mute, fontWeight: 700 }}>{l}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

// A Vesper transition note (the connective tissue between beats).
function Trans({ children }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '34px 1fr', gap: 12, padding: '7px 0 7px' }}>
      <div style={{ display: 'flex', justifyContent: 'center' }}><div style={{ width: 0.5, background: DR.hair, flex: 1 }}/></div>
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: 7, padding: '2px 0' }}>
        <svg width="11" height="11" viewBox="0 0 24 24" fill={gold} style={{ marginTop: 3, flexShrink: 0 }}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>
        <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14, color: DR.soft, lineHeight: 1.4, letterSpacing: -0.1 }}>{children}</span>
      </div>
    </div>
  );
}

// ─────────────────────────────────────────────────────────────────
// A · DAY SPINE, auto-scrolled to now. A now-line across the day;
// past recedes above, the current block sits at the line, Vesper in
// the transitions, next + later below.
// ─────────────────────────────────────────────────────────────────
function SpineBeat({ time, title, state, big }) {
  const now = state === 'now', done = state === 'done';
  const dot = now ? gold : (done ? DR.faint : DR.soft);
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '34px 1fr', gap: 12, alignItems: 'flex-start' }}>
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <div style={{ width: now ? 9 : 6, height: now ? 9 : 6, borderRadius: 9, background: done ? 'transparent' : dot, border: done ? `1.2px solid ${DR.faint}` : 'none', marginTop: 5, boxShadow: now ? `0 0 0 4px rgba(176,133,58,0.16)` : 'none' }}/>
      </div>
      <div style={{ paddingBottom: 2 }}>
        <div style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 0.8, color: now ? gold : DR.faint, fontWeight: 600 }}>{time}{now ? ' · NOW' : ''}</div>
        <div style={{ fontFamily: DR.serif, fontSize: big ? 22 : 16, fontWeight: now ? 500 : 400, fontStyle: done ? 'normal' : (now ? 'normal' : 'normal'), color: done ? DR.faint : DR.ink, letterSpacing: -0.3, lineHeight: 1.12, marginTop: 3, textDecoration: done ? 'line-through' : 'none', textDecorationColor: DR.faint }}>{title}</div>
      </div>
    </div>
  );
}
function LiveSpine() {
  return (
    <PFrame h={LIH}>
      <TodayHeader time="1:20"/>
      {/* faint earlier beat (implies scroll above) */}
      <div style={{ padding: '16px 22px 0', opacity: 0.5 }}>
        <SpineBeat time="09.30" title="Alfama, before the heat" state="done"/>
      </div>
      {/* now-line */}
      <div style={{ padding: '10px 22px 0' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
          <span style={{ fontFamily: DR.mono, fontSize: 8.5, letterSpacing: 1.6, color: gold, fontWeight: 700 }}>1:20</span>
          <span style={{ flex: 1, height: 0.5, background: `rgba(176,133,58,0.5)` }}/>
        </div>
      </div>
      <div style={{ padding: '10px 22px 0' }}>
        <SpineBeat time="13.00" title="Lunch at Ramiro" state="now" big/>
        <Trans>No rush — they won’t turn the table. The light at Graça isn’t worth it till five.</Trans>
        <SpineBeat time="16.30" title="Graça, for the light" state="next"/>
        <Trans>Ten minutes uphill — leave by 4:10, the bench on the left opens at five.</Trans>
        <div style={{ opacity: 0.6 }}><SpineBeat time="eve" title="Dinner, loose" state="later"/></div>
      </div>
      <div style={{ padding: '14px 22px 0' }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13.5, color: DR.mute }}>open the full day →</span>
          <span style={{ display: 'inline-flex', alignItems: 'center', gap: 7, fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13.5, color: DR.mute }}><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke={gold} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg> ask</span>
        </div>
      </div>
      <FacetFooter/>
    </PFrame>
  );
}

// ─────────────────────────────────────────────────────────────────
// B · NOW / NEXT focal stack. Two rich beats, Vesper inline, the rest
// collapsed. Calmest.
// ─────────────────────────────────────────────────────────────────
function FocalBeat({ kicker, kc, time, title, vesper, faded }) {
  return (
    <div style={{ padding: '16px 18px', borderRadius: 16, border: `0.8px solid ${faded ? DR.hair : 'rgba(176,133,58,0.4)'}`, background: faded ? 'transparent' : DR.card, marginBottom: 10 }}>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 7 }}>
        <span style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 1.6, color: kc, fontWeight: 700 }}>{kicker}</span>
        <span style={{ fontFamily: DR.mono, fontSize: 9.5, letterSpacing: 0.8, color: DR.mute, fontWeight: 600 }}>{time}</span>
      </div>
      <div style={{ fontFamily: DR.serif, fontSize: 22, fontWeight: 500, color: DR.ink, letterSpacing: -0.4, lineHeight: 1.06 }}>{title}</div>
      {vesper && <div style={{ display: 'flex', alignItems: 'flex-start', gap: 7, marginTop: 9 }}><svg width="11" height="11" viewBox="0 0 24 24" fill={gold} style={{ marginTop: 3, flexShrink: 0 }}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg><span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14, color: DR.soft, lineHeight: 1.4 }}>{vesper}</span></div>}
    </div>
  );
}
function LiveStack() {
  return (
    <PFrame h={LIH}>
      <TodayHeader time="1:20"/>
      <div style={{ padding: '20px 22px 0' }}>
        <FocalBeat kicker="NOW" kc={gold} time="13.00–14.30" title="Lunch at Ramiro" vesper="No rush — they won’t turn the table."/>
        <FocalBeat kicker="NEXT" kc={DR.mute} time="16.30" title="Graça, for the light" vesper="Ten minutes uphill — leave by 4:10."/>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '8px 4px 0' }}>
          <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14, color: DR.mute }}>Later today — dinner, loose (1)</span>
          <span style={{ color: DR.faint, fontSize: 14 }}>→</span>
        </div>
      </div>
      <FacetFooter/>
    </PFrame>
  );
}

// ─────────────────────────────────────────────────────────────────
// C · MOMENT + THREAD. The current moment focal, a Vesper framing
// line up top, then a thin "rest of today" thread. (Your sketch.)
// `tod` shifts emphasis by time of day (morning/midday/evening).
// ─────────────────────────────────────────────────────────────────
// The plan-phase trip heading, kept for the live home (live dateline).
function LiveCover({ time }) {
  return (
    <div style={{ position: 'relative', height: 220, marginTop: 0, flexShrink: 0 }}>
      <div style={{ position: 'absolute', inset: 0 }}><StyleRiso w={393} h={220}/></div>
      <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.42) 0%, rgba(20,14,9,0) 30%, rgba(20,14,9,0) 48%, rgba(20,14,9,0.78) 100%)' }}/>
      <div style={{ position: 'absolute', top: 46, left: 16, right: 16, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <CIcon>{CICO.back}</CIcon>
        <div style={{ display: 'flex', gap: 8 }}><CIcon dot>{CICO.chat}</CIcon><CIcon dot>{CICO.bell}</CIcon><CIcon>{CICO.info}</CIcon></div>
      </div>
      <div style={{ position: 'absolute', left: 20, right: 20, bottom: 16 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 7 }}>
          <span style={{ padding: '3px 9px', borderRadius: 999, background: 'rgba(255,255,255,0.2)', backdropFilter: 'blur(6px)', fontSize: 9, letterSpacing: 1.4, fontWeight: 700, color: '#fff' }}>DAY 3 · TUE · {time}</span>
          <Ppl who={CASTD} size={22} onDark/>
        </div>
        <h1 style={{ fontFamily: DR.serif, fontSize: 34, fontWeight: 500, letterSpacing: -1, lineHeight: 0.98, color: '#fff', margin: 0 }}>Lisbon, <span style={{ fontStyle: 'italic' }}>slowly</span></h1>
      </div>
    </div>
  );
}
const SPARK = <svg width="11" height="11" viewBox="0 0 24 24" fill={gold} style={{ marginTop: 3, flexShrink: 0 }}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>;

// One timeline beat (past / future). Roomy spacing; past recedes with a ✓.
function Beat({ b, last }) {
  const past = b.kind === 'past', save = b.kind === 'save';
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '46px 16px 1fr', columnGap: 11, alignItems: 'start' }}>
      <div style={{ textAlign: 'right', paddingTop: 1 }}>
        <span style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 0.4, color: past ? DR.faint : DR.mute, fontWeight: 600 }}>{b.t}</span>
      </div>
      <div style={{ position: 'relative', display: 'flex', justifyContent: 'center' }}>
        {!last && <div style={{ position: 'absolute', top: 9, bottom: -2, width: 0.5, background: DR.hair, left: '50%', transform: 'translateX(-50%)' }}/>}
        <div style={{ position: 'relative', zIndex: 1, marginTop: 4, width: 6, height: 6, borderRadius: 6, background: past ? 'transparent' : (save ? gold : DR.soft), border: past ? `1.2px solid ${DR.faint}` : 'none' }}/>
      </div>
      <div style={{ paddingBottom: last ? 0 : 20 }}>
        <div style={{ display: 'flex', alignItems: 'baseline', gap: 8 }}>
          <span style={{ fontFamily: DR.serif, fontSize: 15.5, color: past ? DR.faint : (save ? gold : DR.ink), letterSpacing: -0.2, lineHeight: 1.25, textDecoration: past ? 'line-through' : 'none', textDecorationColor: DR.faint }}>{b.title}</span>
          {past && <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#3D7050" strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round" style={{ flexShrink: 0, opacity: 0.7 }}><path d="M4 12l5 5L20 6"/></svg>}
        </div>
        {(b.area || b.book) && <div style={{ fontFamily: DR.mono, fontSize: 8, letterSpacing: 1.2, color: DR.faint, fontWeight: 700, marginTop: 4 }}>{[b.area, b.book].filter(Boolean).join(' · ').toUpperCase()}</div>}
        {b.note && !past && <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13.5, color: DR.mute, marginTop: 6, lineHeight: 1.4 }}>{b.note}</div>}
      </div>
    </div>
  );
}

// Collapsed summary — distant beats folded into one quiet line.
function CollapsedRow({ label, dir }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '46px 16px 1fr', columnGap: 11, alignItems: 'center', paddingBottom: 20 }}>
      <div/>
      <div style={{ position: 'relative', display: 'flex', justifyContent: 'center' }}>
        <div style={{ position: 'absolute', top: 8, bottom: -2, width: 0.5, background: DR.hair, left: '50%', transform: 'translateX(-50%)' }}/>
        <div style={{ position: 'relative', zIndex: 1, width: 5, height: 5, borderRadius: 5, border: `1px solid ${DR.faint}` }}/>
      </div>
      <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
        <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13.5, color: DR.mute }}>{label}</span>
        <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke={DR.faint} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d={dir === 'up' ? 'M6 15l6-6 6 6' : 'M6 9l6 6 6-6'}/></svg>
      </div>
    </div>
  );
}

// The NOW beat — focal, set off by hairlines (a quiet "now band"),
// Vesper woven directly under the title.
function NowBand({ b, kicker, vesper }) {
  return (
    <div style={{ borderTop: `0.5px solid ${DR.hairThin}`, borderBottom: `0.5px solid ${DR.hairThin}`, padding: '17px 0', margin: '2px 0' }}>
      <div style={{ display: 'grid', gridTemplateColumns: '46px 16px 1fr', columnGap: 11, alignItems: 'start' }}>
        <div style={{ textAlign: 'right', paddingTop: 5 }}><span style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 0.4, color: gold, fontWeight: 700 }}>{b.t}</span></div>
        <div style={{ display: 'flex', justifyContent: 'center', paddingTop: 7 }}><div style={{ width: 9, height: 9, borderRadius: 9, background: gold, boxShadow: '0 0 0 4px rgba(176,133,58,0.16)' }}/></div>
        <div>
          <div style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 1.6, color: gold, fontWeight: 700, marginBottom: 4 }}>{kicker}</div>
          <div style={{ fontFamily: DR.serif, fontSize: 23, fontWeight: 500, color: DR.ink, letterSpacing: -0.4, lineHeight: 1.05 }}>{b.title}</div>
          {(b.area || b.book) && <div style={{ fontFamily: DR.mono, fontSize: 8, letterSpacing: 1.2, color: DR.faint, fontWeight: 700, marginTop: 5 }}>{[b.area, b.book].filter(Boolean).join(' · ').toUpperCase()}</div>}
          <div style={{ display: 'flex', alignItems: 'flex-start', gap: 7, marginTop: 9 }}>{SPARK}<span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14.5, color: DR.soft, lineHeight: 1.42 }}>{vesper}</span></div>
        </div>
      </div>
    </div>
  );
}

// Pinned 4-facet footer — a quiet hairline-topped row at the bottom.
function PinnedFacets() {
  const cells = [[FT_ICON.transport, '4:50', 'TRAM 28'], [FT_ICON.stay, 'Alecrim', 'TONIGHT'], [FT_ICON.costs, '€42', 'TODAY'], [FT_ICON.route, 'map', 'ROUTE']];
  return (
    <div style={{ flexShrink: 0, padding: '14px 22px 28px', borderTop: ed.rule }}>
      <div style={{ display: 'flex', gap: 8 }}>
        {cells.map(([ic, v, l], i) => (
          <div key={i} style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 5 }}>
            <span style={{ color: DR.soft }}>{ic}</span>
            <span style={{ fontFamily: DR.serif, fontSize: 13.5, color: DR.ink, fontWeight: 500, letterSpacing: -0.2, lineHeight: 1 }}>{v}</span>
            <span style={{ fontFamily: DR.mono, fontSize: 7, letterSpacing: 1, color: DR.mute, fontWeight: 700 }}>{l}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

// The full day; each time-of-day sets where "now" sits + Vesper's line.
// Distant past collapses; the timeline centres to fill the middle.
const DAY = [
  { t: '08.00', title: 'Coffee at A Brasileira', area: 'Chiado', via: '' },
  { t: '09.30', title: 'Alfama, the miradouros', area: 'Alfama', via: 'Uphill on foot · 8 min' },
  { t: '12.00', title: 'Tiles at the museum', area: 'Madre de Deus', via: 'Down to the water · 10 min' },
  { t: '13.00', title: 'Lunch at Ramiro', area: 'Intendente', book: 'Table for 4', via: 'Tram 28 · 9 min' },
  { t: '16.30', title: 'Graça, for the light', area: 'Graça', note: 'The bench on the left, before five.', via: 'Tram 28 to Graça · 12 min' },
  { t: '20.00', title: 'Dinner near Alecrim', area: 'Príncipe Real', book: '8:00 · booked', via: '10 min on foot, downhill' },
];
const TOD = {
  morning: { time: '8:10', label: 'the day ahead', nowIdx: 1, kicker: 'FIRST · 9:30', vesper: 'Start uphill while it’s cool — the miradouros are yours before the buses come.', tomorrow: 'Sintra, the palaces' },
  midday: { time: '1:20', label: 'where you are', nowIdx: 3, kicker: 'NOW · IN PROGRESS', vesper: 'No rush — they won’t turn the table. Graça’s light isn’t worth it till five.', tomorrow: 'Bélem, early' },
  evening: { time: '7:40', label: 'winding down', nowIdx: 5, kicker: 'NEXT · 8:00', vesper: 'Walk the long way down through the tiles — the table’s held till half past.', tail: [{ t: '—', title: 'Save today’s three photos →', kind: 'save' }], tomorrow: 'Bélem, early' },
};
// Facets as a light row (trip sub-nav) — borderless cells, hairline-framed.
function FacetRow() {
  const cells = [[FT_ICON.transport, '4:50'], [FT_ICON.stay, 'Alecrim'], [FT_ICON.costs, '€42'], [FT_ICON.route, 'Map']];
  return (
    <div style={{ flexShrink: 0, margin: '16px 24px 0', borderTop: ed.rule, borderBottom: ed.rule, display: 'flex' }}>
      {cells.map(([ic, v], i) => (
        <div key={i} style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 5, padding: '12px 4px', borderLeft: i ? `0.5px solid ${DR.hairThin}` : 'none' }}>
          <span style={{ color: DR.soft, display: 'flex' }}>{ic}</span>
          <span style={{ fontFamily: DR.serif, fontSize: 13.5, color: DR.ink, fontWeight: 500, letterSpacing: -0.2, whiteSpace: 'nowrap' }}>{v}</span>
        </div>
      ))}
    </div>
  );
}

// A clock-aware Vesper day-summary — the editorial "read" of the whole day.
const SUMMARY = {
  morning: 'An easy start — the day opens slow, the hills before the heat.',
  midday: 'A slow Tuesday — Alfama’s behind you, and the best light’s still to come.',
  evening: 'A full day, nearly done — just dinner now, then the evening’s yours.',
};
function DaySummary({ tod }) {
  return (
    <div style={{ flexShrink: 0, padding: '18px 24px 0' }}>
      <div style={{ paddingLeft: 13, borderLeft: `2px solid ${DR.gold}` }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 5 }}>
          <svg width="11" height="11" viewBox="0 0 24 24" fill={DR.gold}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>
          <span style={{ fontSize: 8.5, letterSpacing: 1.4, color: DR.goldDeep, fontWeight: 700 }}>VESPER · THE DAY</span>
        </div>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 16, color: DR.ink, margin: 0, lineHeight: 1.4, letterSpacing: -0.12 }}>{SUMMARY[tod]}</p>
      </div>
    </div>
  );
}

// A faint "tomorrow" peek that anchors the day toward the nav.
function TomorrowRow({ text }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '46px 16px 1fr', columnGap: 11, alignItems: 'center', paddingTop: 6 }}>
      <div style={{ textAlign: 'right' }}><span style={{ fontFamily: DR.mono, fontSize: 8.5, letterSpacing: 0.6, color: DR.faint, fontWeight: 600 }}>TOM</span></div>
      <div style={{ display: 'flex', justifyContent: 'center' }}><div style={{ width: 5, height: 5, borderRadius: 5, border: `1px solid ${DR.faint}` }}/></div>
      <div style={{ display: 'flex', alignItems: 'baseline', gap: 6 }}>
        <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14.5, color: DR.mute }}>Tomorrow — {text}</span>
        <span style={{ color: DR.faint, fontSize: 13 }}>→</span>
      </div>
    </div>
  );
}

// Logistics block — the 3 cards (Stay · Next · Map), pinned above the nav.
function LogisticsBlock() {
  const cells = [[FT_ICON.stay, 'Casa do Alecrim', 'STAY'], [FT_ICON.transport, 'Tram 28 · 4:50', 'NEXT'], [FT_ICON.route, '3 cities', 'MAP']];
  return (
    <div style={{ flexShrink: 0, padding: '10px 22px 86px' }}>
      <div style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 2, color: DR.mute, fontWeight: 700, marginBottom: 11 }}>LOGISTICS</div>
      <div style={{ display: 'flex', gap: 8 }}>
        {cells.map(([ic, v, l], i) => (
          <div key={i} style={{ flex: 1, padding: '11px 10px', background: DR.card, borderRadius: 12, border: `0.5px solid ${DR.hair}` }}>
            <span style={{ color: DR.soft, display: 'flex' }}>{ic}</span>
            <div style={{ fontFamily: DR.serif, fontSize: 13, color: DR.ink, fontWeight: 500, letterSpacing: -0.2, marginTop: 8, lineHeight: 1.1 }}>{v}</div>
            <div style={{ fontFamily: DR.mono, fontSize: 7, letterSpacing: 1, color: DR.mute, fontWeight: 700, marginTop: 3 }}>{l}</div>
          </div>
        ))}
      </div>
    </div>
  );
}
// A transit "leg" between two beats — how you get there.
function Leg({ text }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '46px 16px 1fr', columnGap: 11, alignItems: 'center', padding: '2px 0 11px' }}>
      <div/>
      <div style={{ position: 'relative', display: 'flex', justifyContent: 'center' }}>
        <div style={{ position: 'absolute', top: -10, bottom: -10, width: 0.5, background: DR.hair, left: '50%', transform: 'translateX(-50%)' }}/>
      </div>
      <div style={{ display: 'flex', alignItems: 'center', gap: 7 }}>
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke={DR.faint} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><circle cx="13" cy="4.5" r="1.8"/><path d="M12.5 8l-2.5 3.5 2.5 2.5-1.5 5.5M10 11.5l-3.5 1.5M15 10.5l3 1.5"/></svg>
        <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 12.5, color: DR.mute }}>{text}</span>
      </div>
    </div>
  );
}
// Evening capture — "save the day" photo prompt at the foot of the day.
function CaptureBlock() {
  return (
    <div style={{ marginTop: 22, paddingTop: 16, borderTop: `0.5px solid ${DR.hairThin}` }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 9 }}>
        <svg width="12" height="12" viewBox="0 0 24 24" fill={DR.gold}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>
        <span style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 1.6, color: DR.goldDeep, fontWeight: 700 }}>SAVE THE DAY</span>
      </div>
      <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14, color: DR.mute, margin: '0 0 12px', lineHeight: 1.4 }}>Three from today — keep them for the story.</p>
      <div style={{ display: 'flex', gap: 8 }}>
        {[0, 1, 2].map((i) => <div key={i} style={{ flex: 1, aspectRatio: '1', borderRadius: 10, overflow: 'hidden' }}><StyleRiso w={76} h={76}/></div>)}
        <div style={{ flex: 1, aspectRatio: '1', borderRadius: 10, border: `1px dashed ${DR.faint}`, display: 'flex', alignItems: 'center', justifyContent: 'center', color: DR.faint, fontSize: 22, fontWeight: 300 }}>+</div>
      </div>
    </div>
  );
}
function LiveThread({ tod = 'midday' }) {
  const d = TOD[tod];
  const isEvening = tod === 'evening';
  const past = DAY.slice(0, d.nowIdx).map((x) => ({ ...x, kind: 'past' }));
  const now = DAY[d.nowIdx];
  const future = [...DAY.slice(d.nowIdx + 1).map((x) => ({ ...x, kind: 'next' })), ...(d.tail || [])];
  const visFuture = isEvening ? [] : future.slice(0, 3);
  const wantPast = isEvening ? 1 : Math.max(1, 4 - visFuture.length);
  const visiblePast = past.slice(-wantPast);
  const collapsed = past.length - visiblePast.length;
  return (
    <PFrame h={LIH} bare>
      <div style={{ height: LIH, display: 'flex', flexDirection: 'column' }}>
        <LiveCover time={d.time}/>
        <DaySummary tod={tod}/>
        <div style={{ flex: 1, position: 'relative', overflow: 'hidden' }}>
          <div style={{ padding: '16px 24px 24px' }}>
            {collapsed > 0 && <CollapsedRow label={`earlier today · ${collapsed} done`} dir="up"/>}
            {visiblePast.map((b, i) => <Beat key={'p' + i} b={b}/>)}
            <NowBand b={now} kicker={d.kicker} vesper={d.vesper}/>
            <div style={{ height: 14 }}/>
            {visFuture.map((b, i) => (
              <React.Fragment key={'f' + i}>
                {b.via && <Leg text={b.via}/>}
                <Beat b={b} last={i === visFuture.length - 1}/>
              </React.Fragment>
            ))}
            {isEvening && <CaptureBlock/>}
          </div>
          <div style={{ position: 'absolute', top: 0, left: 0, right: 0, height: 16, background: `linear-gradient(to bottom, ${DR.paper}, rgba(239,234,224,0))`, pointerEvents: 'none' }}/>
          <div style={{ position: 'absolute', bottom: 0, left: 0, right: 0, height: 28, background: `linear-gradient(to top, ${DR.paper}, rgba(239,234,224,0))`, pointerEvents: 'none' }}/>
        </div>
        <LogisticsBlock/>
      </div>
      <TabBar active="trips"/>
    </PFrame>
  );
}

// ─────────────────────────────────────────────────────────────────
// E · GLANCE MAP — on a transit beat, the Now carries a "you → next"
// map sliver. (A variant of B, only when you're moving.)
// ─────────────────────────────────────────────────────────────────
function LiveGlance() {
  return (
    <PFrame h={LIH}>
      <TodayHeader time="4:12"/>
      <div style={{ padding: '20px 22px 0' }}>
        <div style={{ borderRadius: 16, overflow: 'hidden', border: `0.8px solid rgba(176,133,58,0.4)`, background: DR.card }}>
          {/* map sliver */}
          <div style={{ height: 116, position: 'relative' }}>
            <svg width="100%" height="100%" viewBox="0 0 350 116" preserveAspectRatio="xMidYMid slice"><rect width="350" height="116" fill="#E7DCC6"/><path d="M0 86 Q120 64 240 90 T350 80 L350 116 L0 116Z" fill="#9DB0AC" opacity="0.5"/><path d="M60 92 Q150 54 250 40" stroke={gold} strokeWidth="1.8" strokeDasharray="2 5" fill="none"/><circle cx="60" cy="92" r="5" fill={DR.blue}/><circle cx="250" cy="40" r="4.5" fill={DR.ink}/></svg>
            <div style={{ position: 'absolute', left: 14, bottom: 9, fontFamily: DR.mono, fontSize: 8.5, letterSpacing: 1.2, color: DR.soft, fontWeight: 700 }}>YOU → GRAÇA · 10 MIN ON FOOT</div>
          </div>
          <div style={{ padding: '14px 18px' }}>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 6 }}><span style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 1.6, color: gold, fontWeight: 700 }}>ON THE WAY</span><span style={{ fontFamily: DR.mono, fontSize: 9.5, color: DR.mute, fontWeight: 600 }}>16.30</span></div>
            <div style={{ fontFamily: DR.serif, fontSize: 22, fontWeight: 500, color: DR.ink, letterSpacing: -0.4 }}>Miradouro da Graça</div>
            <div style={{ display: 'flex', alignItems: 'flex-start', gap: 7, marginTop: 9 }}><svg width="11" height="11" viewBox="0 0 24 24" fill={gold} style={{ marginTop: 3, flexShrink: 0 }}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg><span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14, color: DR.soft, lineHeight: 1.4 }}>Downhill all the way back after — the bench on the left opens at five.</span></div>
          </div>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '12px 4px 0' }}>
          <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14, color: DR.mute }}>Then — dinner, loose</span>
          <span style={{ color: DR.faint, fontSize: 14 }}>→</span>
        </div>
      </div>
      <FacetFooter/>
    </PFrame>
  );
}

Object.assign(window, { LiveSpine, LiveStack, LiveThread, LiveGlance });
