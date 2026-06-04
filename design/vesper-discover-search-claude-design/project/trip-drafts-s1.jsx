// ═══════════════════════════════════════════════════════════════
// SYSTEM 1 · THE FOLIO — cover-led, editorial. The trip is a book that
// ages: riso covers for plan phases, gouache for memory. Big serif title
// on the cover; Vesper line + spine + tiles on the parchment below.
// ═══════════════════════════════════════════════════════════════

// Shared chrome: a full-bleed cover with overlaid identity, then body.
function FolioShell({ truth, at, cover, kicker, title, meta, gouache, blank, children }) {
  const Scene = gouache ? StyleGouache : StyleRiso;
  return (
    <Phone bg={DR.paper}>
      <div style={{ position: 'absolute', inset: 0, overflow: 'hidden', background: DR.paper }}>
        {/* COVER (zone 1) */}
        <div style={{ position: 'relative', height: 270 }}>
          {blank
            ? <div style={{ position: 'absolute', inset: 0, background: DR.cardSoft }}/>
            : <div style={{ position: 'absolute', inset: 0 }}><Scene w={393} h={270}/></div>}
          {!blank && <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.34) 0%, rgba(20,14,9,0) 32%, rgba(20,14,9,0) 50%, rgba(20,14,9,0.7) 100%)' }}/>}
          {/* top: back + filmstrip */}
          <div style={{ paddingTop: 52, paddingLeft: 18, paddingRight: 18, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
            <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={blank ? DR.soft : '#fff'} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
          </div>
          <div style={{ position: 'absolute', top: 88, left: 18 }}><Filmstrip truth={truth} at={at} onDark={!blank}/></div>
          {/* identity, low */}
          <div style={{ position: 'absolute', left: 22, right: 22, bottom: 18 }}>
            {kicker && <div style={{ fontSize: 9.5, letterSpacing: 2, fontWeight: 700, color: blank ? DR.mute : 'rgba(255,255,255,0.85)', marginBottom: 7 }}>{kicker}</div>}
            <h1 style={{ fontFamily: DR.serif, fontSize: 36, fontWeight: 500, letterSpacing: -1, lineHeight: 0.98, color: blank ? DR.faint : '#fff', margin: 0, fontStyle: blank ? 'italic' : 'normal' }}>{title}</h1>
            {meta && <div style={{ fontFamily: DR.mono, fontSize: 10, color: blank ? DR.mute : 'rgba(255,255,255,0.85)', letterSpacing: 1, marginTop: 7 }}>{meta}</div>}
          </div>
        </div>
        {/* BODY */}
        <div style={{ padding: '16px 22px 0' }}>{children}</div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// ── Phase 1 · IDEATION (cold / forming) ──
function S1Ideation() {
  return (
    <FolioShell truth={0} blank kicker="UNTITLED TRIP" title="somewhere, someday" meta="NO DATES YET">
      <VLine kicker="VESPER">Tell me a place or a feeling — I’ll start the folio from there.</VLine>
      <div style={{ marginTop: 16, display: 'flex', alignItems: 'center', gap: 10 }}>
        <span style={{ flex: 1, padding: '13px 0', textAlign: 'center', background: DR.gold, color: '#fff', borderRadius: 999, fontSize: 14, fontWeight: 600, letterSpacing: -0.1 }}>Shape this trip with Vesper</span>
      </div>
      <div style={{ marginTop: 12, display: 'flex', gap: 8 }}>
        {['Where', 'When', 'Who'].map(t => <span key={t} style={{ flex: 1, textAlign: 'center', padding: '10px 4px', borderRadius: 10, border: `0.5px solid ${DR.hair}`, fontFamily: DR.serif, fontSize: 12.5, color: DR.soft, background: DR.card }}>{t}</span>)}
      </div>
    </FolioShell>
  );
}

// ── Phase 2 · FOLIO (pre-trip) — populated ──
function S1Folio() {
  return (
    <FolioShell truth={1} kicker="IN 23 DAYS" title={<>Lisbon, <span style={{ fontStyle: 'italic' }}>slowly</span></>} meta="MAY 18 – 24 · 6 NIGHTS · 3 OF YOU">
      <VLine>The only thing missing is where you sleep nights 5–7.</VLine>
      <div style={{ marginTop: 16 }}><Cap>THE DAYS, TAKING SHAPE</Cap>
        <SpinePeek rows={[
          { day: 'SAT', date: '18', title: 'Land soft, settle in Alfama' },
          { day: 'SUN', date: '19', title: 'Miradouros, east to west', sub: 'Ana’s walking list' },
          { day: 'MON', date: '20', title: 'a sparse day', gap: true },
        ]}/>
      </div>
      <div style={{ marginTop: 16 }}><Tiles items={[{ g: TGI.map, label: 'Route', meta: '3 cities' }, { g: TGI.costs, label: 'Costs', meta: 'split 3' }, { g: TGI.group, label: 'Group', meta: '12 new' }]}/></div>
    </FolioShell>
  );
}

// ── Phase 3 · FIELD GUIDE (during) ──
function S1Live() {
  return (
    <FolioShell truth={2} kicker="DAY 3 · LIVE" title={<>Lisbon, <span style={{ fontStyle: 'italic' }}>slowly</span></>} meta="MON · 10:14 · 18° CLEAR">
      <VLine>You’re due a slow hour — Kayaba’s coffee is 6 min from here.</VLine>
      <div style={{ marginTop: 16 }}><Cap>TODAY</Cap>
        <SpinePeek openLabel="Open today’s guide" rows={[
          { day: 'NOW', date: '20', title: 'Cemetery walk, then coffee' },
          { day: '13:00', date: '·', title: 'Lunch — Ana pinned a spot', sub: '4 min away' },
          { day: '21:00', date: '·', title: 'Fado, the quiet room', sub: 'held · 2 seats', dim: true },
        ]}/>
      </div>
      <div style={{ marginTop: 16 }}><Tiles items={[{ g: TGI.map, label: 'Map', meta: 'you’re here' }, { g: TGI.group, label: 'Group', meta: 'Ana live' }, { g: TGI.photos, label: 'Capture', meta: '+12' }]}/></div>
    </FolioShell>
  );
}

// ── Phase 4 · MEMORY (post-trip) — gouache ──
function S1Memory() {
  return (
    <FolioShell truth={3} gouache kicker="A TRIP, REMEMBERED" title={<>Lisbon, <span style={{ fontStyle: 'italic' }}>slowly</span></>} meta="MAY 18 – 24 · 214 PHOTOS">
      <VLine>Your story’s ready — six days, in the order you’ll want to remember them.</VLine>
      <div style={{ marginTop: 16 }}><Cap>HOW IT WENT</Cap>
        <SpinePeek openLabel="Read the story" rows={[
          { day: 'PEAK', date: '21', title: 'The fado on the fourth night' },
          { day: 'KEPT', date: '·', title: '12 photos, one postcard', sub: 'saved to Atlas' },
        ]}/>
      </div>
      <div style={{ marginTop: 16 }}><Tiles items={[{ g: TGI.story, label: 'Story', meta: 'ready', accent: true }, { g: TGI.photos, label: '214 photos', meta: '12 kept' }, { g: TGI.memory, label: 'To Atlas', meta: '+1 city' }]}/></div>
    </FolioShell>
  );
}

// ── Empty-state variations (the matrix) ──
// E1 · destination, no dates
function S1_DestNoDate() {
  return (
    <FolioShell truth={1} kicker="DATES NOT SET" title={<>Lisbon, <span style={{ fontStyle: 'italic' }}>someday</span></>} meta="WHEN WORKS?">
      <VLine>I’ve got the place. Give me a month and I’ll find the light you want.</VLine>
      <div style={{ marginTop: 16 }}><Cap>FIRST, A WHEN</Cap>
        <div style={{ display: 'flex', gap: 7 }}>
          {['May', 'Jun', 'Sep', 'Oct'].map((m, i) => <span key={m} style={{ flex: 1, textAlign: 'center', padding: '12px 0', borderRadius: 10, border: `0.5px solid ${i === 0 ? DR.gold : DR.hair}`, background: DR.card, fontFamily: DR.serif, fontSize: 14, color: DR.ink }}>{m}</span>)}
        </div>
      </div>
      <div style={{ marginTop: 14, opacity: 0.5 }}><Tiles items={[{ g: TGI.map, label: 'Route', meta: 'after dates' }, { g: TGI.costs, label: 'Costs', meta: '—' }, { g: TGI.group, label: 'Group', meta: '3' }]}/></div>
    </FolioShell>
  );
}
// E2 · dates, no destination
function S1_DateNoDest() {
  return (
    <FolioShell truth={1} blank kicker="MAY 18 – 24" title="where to?" meta="6 NIGHTS · 3 OF YOU">
      <VLine>You’ve got the week. Based on what you’ve saved, three places fit it.</VLine>
      <div style={{ marginTop: 16 }}><Cap>VESPER SUGGESTS</Cap>
        <SpinePeek openLabel="See all picks" rows={[
          { day: '01', date: '·', title: 'Lisbon, for the food' },
          { day: '02', date: '·', title: 'Tbilisi, still uncrowded' },
          { day: '03', date: '·', title: 'Naples, worth it' },
        ]}/>
      </div>
    </FolioShell>
  );
}

Object.assign(window, { S1Ideation, S1Folio, S1Live, S1Memory, S1_DestNoDate, S1_DateNoDest });
