// ═══════════════════════════════════════════════════════════════
// ATLAS · SEARCH + ADD — the two top-bar destinations.
// Search: "Find a memory" — field + wander-by + ask Vesper (the
// current screen, held in the home's editorial system).
// Add: "Give Vesper one memory to hold" — rebuilt from the unpolished
// version: the do-nothing hero card dropped; two clean, weighted
// paths (Vesper scan = recommended, by hand), bare glyphs not heavy
// gold circles, the philosophy folded into a quiet line.
// Reuses Phone, T, Marks, Eyebrow, TabBar.
// ═══════════════════════════════════════════════════════════════

// ─── ATLAS · SEARCH ─────────────────────────────────────────────
function AtlasSearch() {
  const wander = [
    { eb: 'BY · PLACE',  title: 'Cities',    sub: '12 remembered', icon: 'Map' },
    { eb: 'BY · SEASON', title: 'Time',      sub: 'months, trips, returns', icon: 'cal' },
    { eb: 'BY · RITUAL', title: 'Patterns',  sub: '6 things Vesper reads', icon: 'spark' },
    { eb: 'BY · SHELF',  title: 'Postcards', sub: 'kept artifacts', icon: 'Postcard' },
  ];
  const wIcon = (k) => {
    if (k === 'Map') return <Marks.Map size={26}/>;
    if (k === 'Postcard') return <Marks.Postcard size={26}/>;
    if (k === 'cal') return <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={T.muteSoft} strokeWidth="1.4"><rect x="3.5" y="5" width="17" height="16" rx="2"/><path d="M3.5 9.5h17M8 3v4M16 3v4" strokeLinecap="round"/></svg>;
    return <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={T.muteSoft} strokeWidth="1.4" strokeLinecap="round" strokeLinejoin="round"><path d="M12 3l1.6 5.4L19 10l-5.4 1.6L12 17l-1.6-5.4L5 10l5.4-1.6z"/></svg>;
  };
  return (
    <Phone bg={T.bg}>
      {/* header */}
      <div style={{ padding: '14px 22px 0' }}>
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M15 5l-7 7 7 7"/></svg>
        <div style={{ marginTop: 16 }}>
          <Eyebrow color={T.gold}>ATLAS · SEARCH</Eyebrow>
          <h1 style={{ fontFamily: T.serif, fontWeight: 500, fontSize: 38, lineHeight: 0.96, letterSpacing: -1, color: T.ink, margin: '8px 0 0' }}>Find a memory.</h1>
          <div style={{ fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1.6, fontWeight: 600, marginTop: 9 }}>PLACES · DRAFTS · RITUALS · THINGS YOU ALMOST FORGOT</div>
        </div>
      </div>

      {/* field */}
      <div style={{ padding: '18px 22px 0' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 11, padding: '14px 14px', background: T.cardWarm, borderRadius: 14, border: `0.5px solid ${T.hairline}` }}>
          <Marks.Search s={18} c={T.mute}/>
          <span style={{ flex: 1, fontFamily: T.serif, fontStyle: 'italic', fontSize: 15.5, color: T.muteSoft }}>a place, a season, a person…</span>
          <span style={{ fontFamily: T.mono, fontSize: 8.5, letterSpacing: 1.2, color: T.muteSoft, fontWeight: 600, border: `0.5px solid ${T.hairline}`, borderRadius: 6, padding: '4px 7px' }}>RETURN</span>
        </div>
      </div>

      {/* wander by */}
      <div style={{ padding: '20px 22px 0' }}>
        <Eyebrow>OR WANDER BY…</Eyebrow>
        <div style={{ marginTop: 11, display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 9 }}>
          {wander.map((w) => (
            <div key={w.title} style={{ padding: '13px 14px', background: T.cardWarm, borderRadius: 13, border: `0.5px solid ${T.hairline}` }}>
              <div style={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between' }}>
                <span style={{ fontFamily: T.mono, fontSize: 8, color: T.gold, letterSpacing: 1.4, fontWeight: 700 }}>{w.eb}</span>
                <span style={{ opacity: 0.6 }}>{wIcon(w.icon)}</span>
              </div>
              <div style={{ fontFamily: T.serif, fontSize: 21, fontWeight: 500, color: T.ink, letterSpacing: -0.3, marginTop: 8 }}>{w.title}</div>
              <div style={{ fontFamily: T.serif, fontSize: 11.5, color: T.muteSoft, marginTop: 3 }}>{w.sub}</div>
            </div>
          ))}
        </div>
      </div>

      {/* ask vesper */}
      <div style={{ padding: '14px 22px 0' }}>
        <div style={{ padding: '13px 15px', borderRadius: 13, border: `1px dashed ${T.gold}` }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 7 }}>
            <span style={{ width: 5, height: 5, borderRadius: 5, background: T.gold }}/>
            <span style={{ fontFamily: T.mono, fontSize: 9, color: T.goldDeep, letterSpacing: 1.6, fontWeight: 700 }}>OR ASK VESPER</span>
          </div>
          <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 15.5, color: T.ink, marginTop: 7, letterSpacing: -0.1 }}>“what places have I been returning to?”</div>
        </div>
      </div>

      <TabBar active="atlas"/>
    </Phone>
  );
}

// ─── ATLAS · ADD ────────────────────────────────────────────────
function AtlasAdd() {
  const Path = ({ eb, title, sub, gold, last }) => (
    <div style={{ display: 'flex', alignItems: 'center', gap: 14, padding: '18px 2px', borderTop: `0.5px solid ${T.hairline}`, borderBottom: last ? `0.5px solid ${T.hairline}` : 'none' }}>
      <div style={{ flex: 1, minWidth: 0 }}>
        <span style={{ fontFamily: T.mono, fontSize: 8.5, color: gold ? T.goldDeep : T.mute, letterSpacing: 1.6, fontWeight: 700 }}>{eb}</span>
        <div style={{ fontFamily: T.serif, fontSize: 23, fontWeight: 500, color: T.ink, letterSpacing: -0.4, lineHeight: 1.04, marginTop: 6 }}>{title}</div>
        <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.mute, marginTop: 5, lineHeight: 1.35 }}>{sub}</div>
      </div>
      <Marks.ArrowR s={16} c={gold ? T.goldDeep : T.muteSoft}/>
    </div>
  );
  return (
    <Phone bg={T.bg}>
      {/* header — back, top-left */}
      <div style={{ display: 'flex', alignItems: 'center', gap: 6, padding: '14px 22px 0', color: T.inkSoft }}>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
        <span style={{ fontSize: 13, fontWeight: 500, color: T.inkSoft }}>Atlas</span>
      </div>

      {/* title */}
      <div style={{ padding: '22px 24px 0' }}>
        <Eyebrow color={T.gold}>ADD TO ATLAS</Eyebrow>
        <h1 style={{ fontFamily: T.serif, fontWeight: 500, fontSize: 39, lineHeight: 0.98, letterSpacing: -1.1, color: T.ink, margin: '10px 0 0' }}>Give Vesper one memory to hold.</h1>
        <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 15, color: T.mute, lineHeight: 1.45, margin: '14px 0 0', maxWidth: 320 }}>Vesper looks for travel-shaped clusters on this phone, then brings only the promising drafts back to you.</p>
      </div>

      {/* the two paths — clean editorial rows, no boxed icons */}
      <div style={{ padding: '30px 24px 0' }}>
        <Path eb="VESPER SCAN · RECOMMENDED" title="Find memories from photos" sub="Let Vesper read the library and propose a few drafts." gold/>
        <Path eb="BY HAND" title="Choose photos myself" sub="Pick one trip, one day, or one place." last/>
      </div>

      {/* philosophy line — folded in, no do-nothing hero card */}
      <div style={{ padding: '22px 32px 0' }}>
        <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.muteSoft, textAlign: 'center', lineHeight: 1.45, margin: 0 }}>Dates and places first — photos only if you choose to make a story.</p>
      </div>
    </Phone>
  );
}

Object.assign(window, { AtlasSearch, AtlasAdd });
