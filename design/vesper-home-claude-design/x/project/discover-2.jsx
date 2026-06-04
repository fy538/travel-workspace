// ═══════════════════════════════════════════════════════════════
// DIRECTION 2 · FIELD NOTES / INTELLIGENCE DESK
// Discover as Vesper's place-intelligence surface. The top module is a
// field briefing: what matters, what to notice, what to skip, what's timely.
// Less photo-led, more structured/typographic.
// ═══════════════════════════════════════════════════════════════

function D2Home() {
  const brief = [
    { k: 'WHAT MATTERS', c: D.vesper, t: 'The miradouro culture — the city is read from its viewpoints, not its monuments.' },
    { k: 'NOTICE', c: D.earth, t: 'Tilework changes by parish; it dates the building better than any plaque.' },
    { k: 'SKIP', c: T.muteSoft, t: 'Tram 28 at midday. The same route walks better in reverse.' },
    { k: 'TIMELY', c: '#3D7050', t: 'Santo António’s feast (Jun 12–13) takes over Alfama after dark.' },
  ];
  return (
    <Phone bg={T.bg}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        {/* Header */}
        <div style={{ padding: '14px 22px 0', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <h1 style={{ fontFamily: T.serif, fontSize: 28, fontWeight: 500, letterSpacing: -0.8, color: T.ink, margin: 0 }}>Discover</h1>
          <div style={{ display: 'flex', gap: 14 }}>{DIcon.settings()}{DIcon.saved()}</div>
        </div>

        {/* Search */}
        <div style={{ padding: '12px 22px 0' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, padding: '10px 14px', background: T.cardWarm, borderRadius: 999, border: `0.5px solid ${T.hairline}` }}>
            {DIcon.search()}
            <span style={{ fontSize: 13.5, color: T.muteSoft }}>Search places, restaurants, cities…</span>
          </div>
        </div>

        {/* Seg — refined rail */}
        <div style={{ padding: '12px 22px 0' }}>
          <SegControl variant="rail" active={0}/>
        </div>

        {/* THE BRIEFING */}
        <div style={{ padding: '16px 16px 0' }}>
          <div style={{ background: T.cardWarm, borderRadius: 16, border: `0.5px solid ${T.hairline}`, boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset', overflow: 'hidden' }}>
            <div style={{ padding: '14px 16px 12px', display: 'flex', alignItems: 'center', gap: 8, borderBottom: `0.5px solid ${T.hairThin}` }}>
              <Spark s={14}/>
              <span style={{ fontSize: 10, letterSpacing: 1.6, fontWeight: 700, color: D.vesperDeep }}>VESPER’S READ · LISBON</span>
              <span style={{ marginLeft: 'auto', fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1 }}>UPDATED TODAY</span>
            </div>
            <div style={{ padding: '4px 16px 14px' }}>
              {brief.map((b, i) => (
                <div key={i} style={{ display: 'grid', gridTemplateColumns: '74px 1fr', gap: 12, padding: '11px 0', borderTop: i ? `0.5px solid ${T.hairThin}` : 'none', alignItems: 'baseline' }}>
                  <div style={{ display: 'flex', alignItems: 'baseline', gap: 5 }}>
                    <span style={{ width: 5, height: 5, borderRadius: 5, background: b.c, transform: 'translateY(-1px)' }}/>
                    <span style={{ fontSize: 8.5, letterSpacing: 1.2, fontWeight: 700, color: b.c === T.muteSoft ? T.mute : b.c }}>{b.k}</span>
                  </div>
                  <span style={{ fontFamily: T.serif, fontSize: 13.5, color: T.ink, lineHeight: 1.35, letterSpacing: -0.1 }}>{b.t}</span>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Field-note dispatches — compact rows w/ small thumbs */}
        <div style={{ padding: '18px 22px 0' }}>
          <SectionLabel right="6">DISPATCHES</SectionLabel>
          <div style={{ marginTop: 10, display: 'flex', flexDirection: 'column', gap: 12 }}>
            {[
              { v: 'alley', lens: 'The debate', t: 'Intendente’s trajectory is the city’s most legible' },
              { v: 'tiles', lens: 'Ritual', t: 'Where to take your morning bica, and why it matters' },
            ].map((d, i) => (
              <div key={i} style={{ display: 'flex', gap: 12, alignItems: 'center' }}>
                <Plate variant={d.v} style={{ width: 64, height: 64, borderRadius: 10, flexShrink: 0 }}/>
                <div style={{ flex: 1, minWidth: 0 }}>
                  <div style={{ fontSize: 9, letterSpacing: 1.4, fontWeight: 700, color: D.vesper }}>{d.lens.toUpperCase()}</div>
                  <div style={{ fontFamily: T.serif, fontSize: 14.5, fontWeight: 500, color: T.ink, letterSpacing: -0.2, lineHeight: 1.2, marginTop: 4 }}>{d.t}</div>
                </div>
                <span style={{ color: T.muteSoft, fontSize: 13 }}>→</span>
              </div>
            ))}
          </div>
        </div>
      </div>
      <TabBar active="discover"/>
    </Phone>
  );
}

function D2Dossier() {
  return (
    <Phone bg={T.bg}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        {/* back */}
        <div style={{ padding: '8px 18px 0', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 4, color: T.inkSoft }}>{DIcon.back()}<span style={{ fontSize: 13, fontWeight: 500 }}>Discover</span></div>
          {DIcon.saved()}
        </div>

        {/* Dossier header — metadata grid, intelligence-style */}
        <div style={{ padding: '14px 22px 0' }}>
          <LensChip lens="The debate"/>
          <h1 style={{ fontFamily: T.serif, fontSize: 25, fontWeight: 500, letterSpacing: -0.5, lineHeight: 1.12, color: T.ink, margin: '12px 0 0' }}>
            Intendente’s trajectory is the city’s most legible
          </h1>
          {/* metadata grid */}
          <div style={{ marginTop: 14, display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 0, border: `0.5px solid ${T.hairline}`, borderRadius: 10, overflow: 'hidden' }}>
            {[['PLACE','Intendente, Lisbon'],['LENS','The debate'],['READ','4 min'],['UPDATED','Today']].map(([k,v],i)=>(
              <div key={k} style={{ padding: '10px 12px', borderTop: i>1?`0.5px solid ${T.hairThin}`:'none', borderLeft: i%2?`0.5px solid ${T.hairThin}`:'none' }}>
                <div style={{ fontSize: 8.5, letterSpacing: 1.3, color: T.muteSoft, fontWeight: 700 }}>{k}</div>
                <div style={{ fontFamily: T.serif, fontSize: 13.5, color: T.ink, fontWeight: 500, marginTop: 3, letterSpacing: -0.1 }}>{v}</div>
              </div>
            ))}
          </div>
        </div>

        {/* thesis */}
        <div style={{ padding: '16px 22px 0' }}>
          <div style={{ paddingLeft: 14, borderLeft: `2px solid ${D.vesper}` }}>
            <div style={{ fontSize: 9, letterSpacing: 1.6, fontWeight: 700, color: D.vesperDeep, marginBottom: 5 }}>VESPER’S THESIS</div>
            <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 15.5, color: T.ink, lineHeight: 1.4, margin: 0, letterSpacing: -0.1 }}>
              You can watch a decade of the city’s argument with itself in three blocks.
            </p>
          </div>
        </div>

        {/* body + margin callout */}
        <div style={{ padding: '16px 22px 0' }}>
          <p style={{ fontFamily: T.serif, fontSize: 15, color: T.inkSoft, lineHeight: 1.6, margin: 0, letterSpacing: -0.05 }}>
            Ten years ago this was the address nobody gave out. The square cleaned up, the rents moved, and the old kiosk stayed — which is the part that tells you how it actually went.
          </p>
          <div style={{ marginTop: 14, padding: '12px 14px', background: T.cardWarm, borderRadius: 12, border: `0.5px solid ${T.hairline}` }}>
            <div style={{ display: 'flex', gap: 18 }}>
              <div style={{ flex: 1 }}>
                <div style={{ fontSize: 8.5, letterSpacing: 1.3, fontWeight: 700, color: D.earth, marginBottom: 5 }}>NOTICE</div>
                <div style={{ fontFamily: T.serif, fontSize: 12.5, color: T.ink, lineHeight: 1.3 }}>the kiosk’s old tile</div>
              </div>
              <div style={{ flex: 1 }}>
                <div style={{ fontSize: 8.5, letterSpacing: 1.3, fontWeight: 700, color: T.mute, marginBottom: 5 }}>SKIP</div>
                <div style={{ fontFamily: T.serif, fontSize: 12.5, color: T.ink, lineHeight: 1.3 }}>the new rooftop bars</div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <DossierBar variant="desk"/>
    </Phone>
  );
}

window.D2Home = D2Home;
window.D2Dossier = D2Dossier;
