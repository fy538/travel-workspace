// ═══════════════════════════════════════════════════════════════
// DIRECTION 1 · EDITORIAL FRONT PAGE
// A refined travel-magazine Discover. Strong lead read, then curated
// sections. Calm, premium, highly readable.
// ═══════════════════════════════════════════════════════════════

function D1Home() {
  return (
    <Phone bg={T.bg}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        {/* Header */}
        <div style={{ padding: '14px 22px 0', display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between' }}>
          <div>
            <h1 style={{ fontFamily: T.serif, fontSize: 34, fontWeight: 500, letterSpacing: -1, color: T.ink, margin: 0, lineHeight: 1 }}>Discover</h1>
            <div style={{ marginTop: 6, display: 'flex', alignItems: 'center', gap: 7, color: T.mute, fontSize: 11.5 }}>
              <span style={{ width: 5, height: 5, borderRadius: 5, background: D.earth }}/>
              <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.inkSoft }}>Lisbon</span>
              <span style={{ color: T.muteSoft }}>· tuned to your taste</span>
            </div>
          </div>
          <div style={{ display: 'flex', gap: 14, paddingTop: 4 }}>
            {DIcon.settings()}{DIcon.saved()}
          </div>
        </div>

        {/* Search */}
        <div style={{ padding: '14px 22px 0' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, padding: '11px 14px', background: T.cardWarm, borderRadius: 999, border: `0.5px solid ${T.hairline}` }}>
            {DIcon.search()}
            <span style={{ fontSize: 14, color: T.muteSoft, letterSpacing: -0.1 }}>Search places, restaurants, cities…</span>
          </div>
        </div>

        {/* Seg control — underline editorial */}
        <div style={{ padding: '18px 22px 0' }}>
          <SegControl variant="underline" active={0}/>
        </div>

        {/* LEAD READ */}
        <div style={{ padding: '18px 22px 0' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 10 }}>
            <Spark s={13}/>
            <span style={{ fontSize: 10, letterSpacing: 1.8, fontWeight: 700, color: D.vesperDeep }}>VESPER’S READ · TODAY</span>
          </div>
          <Plate variant="rooftops" style={{ height: 178, borderRadius: 14 }} dim={0.06}>
            <div style={{ position: 'absolute', top: 12, left: 12 }}><LensChip lens="For the obsessed" onDark/></div>
          </Plate>
          <h2 style={{ fontFamily: T.serif, fontSize: 23, fontWeight: 500, letterSpacing: -0.4, lineHeight: 1.15, color: T.ink, margin: '14px 0 0' }}>
            What Lisbon does better than anywhere comparable in Europe.
          </h2>
          <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 14, color: T.mute, lineHeight: 1.4, margin: '8px 0 0' }}>
            The layering of food cultures at every price point — without the theatre.
          </p>
          <div style={{ marginTop: 12, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
            <VesperBy/>
            <span style={{ fontFamily: T.mono, fontSize: 9.5, color: T.muteSoft, letterSpacing: 1 }}>5 MIN READ</span>
          </div>
        </div>

        {/* Curated section */}
        <div style={{ padding: '20px 22px 0' }}>
          <SectionLabel right="6 NOTES">WHERE VESPER WOULD GO FIRST</SectionLabel>
          <div style={{ marginTop: 12, display: 'flex', gap: 13 }}>
            <div style={{ flex: 1, minWidth: 0 }}>
              <Plate variant="alley" style={{ height: 96, borderRadius: 10 }}/>
              <div style={{ marginTop: 8 }}><FieldEyebrow/></div>
              <div style={{ fontFamily: T.serif, fontSize: 15, fontWeight: 500, color: T.ink, letterSpacing: -0.2, lineHeight: 1.15, marginTop: 6 }}>
                Intendente, before it changes again
              </div>
            </div>
            <div style={{ flex: 1, minWidth: 0 }}>
              <Plate variant="coast" style={{ height: 96, borderRadius: 10 }}/>
              <div style={{ marginTop: 8 }}><FieldEyebrow/></div>
              <div style={{ fontFamily: T.serif, fontSize: 15, fontWeight: 500, color: T.ink, letterSpacing: -0.2, lineHeight: 1.15, marginTop: 6 }}>
                Mouraria’s triple-layered tension
              </div>
            </div>
          </div>
        </div>
      </div>
      <TabBar active="discover"/>
    </Phone>
  );
}

function D1Dossier() {
  return (
    <Phone bg={T.bg}>
      <div style={{ position: 'absolute', inset: 0, overflow: 'hidden' }}>
        {/* Hero */}
        <Plate variant="hills" style={{ height: 300 }} dim={0.12}>
          {/* status-safe top controls */}
          <div style={{ position: 'absolute', top: 56, left: 18, right: 18, display: 'flex', justifyContent: 'space-between' }}>
            <div style={{ width: 38, height: 38, borderRadius: 999, background: 'rgba(255,255,255,0.22)', backdropFilter: 'blur(8px)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>{DIcon.back('#fff')}</div>
            <div style={{ width: 38, height: 38, borderRadius: 999, background: 'rgba(255,255,255,0.22)', backdropFilter: 'blur(8px)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>{DIcon.save('#fff')}</div>
          </div>
          <div style={{ position: 'absolute', left: 20, bottom: 18 }}>
            <LensChip lens="For the obsessed" onDark/>
          </div>
        </Plate>

        {/* Body */}
        <div style={{ padding: '20px 22px 0' }}>
          <FieldEyebrow/>
          <h1 style={{ fontFamily: T.serif, fontSize: 27, fontWeight: 500, letterSpacing: -0.6, lineHeight: 1.1, color: T.ink, margin: '10px 0 0' }}>
            What Lisbon does better than anywhere comparable in Europe
          </h1>
          {/* meta row */}
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, margin: '12px 0 0', fontFamily: T.mono, fontSize: 9.5, color: T.muteSoft, letterSpacing: 1 }}>
            <span style={{ color: T.earth, fontWeight: 600 }}>LISBON</span><span>·</span><span>5 MIN</span><span>·</span><span>FIELD NOTE</span>
          </div>
          {/* thesis */}
          <div style={{ marginTop: 16, paddingLeft: 14, borderLeft: `2px solid ${D.vesper}` }}>
            <div style={{ fontSize: 9, letterSpacing: 1.6, fontWeight: 700, color: D.vesperDeep, marginBottom: 5 }}>VESPER’S THESIS</div>
            <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 15.5, color: T.ink, lineHeight: 1.4, margin: 0, letterSpacing: -0.1 }}>
              It layers food cultures at every price point without turning any of them into theatre.
            </p>
          </div>
          {/* body w/ drop cap */}
          <p style={{ fontFamily: T.serif, fontSize: 15.5, color: T.inkSoft, lineHeight: 1.6, margin: '16px 0 0', letterSpacing: -0.05 }}>
            <span style={{ float: 'left', fontFamily: T.serif, fontSize: 50, lineHeight: 0.82, fontWeight: 500, color: T.ink, paddingRight: 8, paddingTop: 3 }}>T</span>
            he tourist tasca and the neighbourhood one share a street, a price, and often a cook. You can eat the same grilled fish for eight euros beside a banker and a bricklayer — and nobody is performing Portugal at you.
          </p>
        </div>
      </div>
      <DossierBar variant="editorial"/>
    </Phone>
  );
}

window.D1Home = D1Home;
window.D1Dossier = D1Dossier;
