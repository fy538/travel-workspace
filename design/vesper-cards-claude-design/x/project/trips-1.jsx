// Direction A — PLANNING TABLE
// A tactile planning surface. The alive trip is the main object, surrounded
// by small planning pieces. Trips-in-formation feel like things on a desk.

function TripsPlanningTable() {
  return (
    <Phone bg={T.bg}>
      <TripsTopBar eyebrow="TRIPS · 9 · MARCH ’26"/>

      {/* Title */}
      <div style={{ padding: '18px 22px 0' }}>
        <h1 style={{
          fontFamily: T.serif, fontWeight: 500, fontSize: 38, lineHeight: 0.96,
          letterSpacing: -1, color: T.ink, margin: 0,
        }}>
          Your <span style={{ fontStyle: 'italic' }}>planning table.</span>
        </h1>
        <div style={{
          marginTop: 8, display: 'flex', alignItems: 'center', gap: 10,
          fontSize: 11, color: T.mute, fontFamily: T.serif, fontStyle: 'italic',
        }}>
          <TripPill kind="alive">1 ALIVE</TripPill>
          <span>·</span>
          <span>3 drafts · 2 dreaming · 8 kept</span>
        </div>
      </div>

      {/* ── THE ALIVE TRIP — a hero "trip object" on the table ── */}
      <div style={{ padding: '16px 16px 0', position: 'relative' }}>
        <div style={{
          background: T.cardWarm, borderRadius: 18, padding: '14px',
          boxShadow: '0 16px 32px -18px rgba(0,0,0,0.18), 0 0 0 0.5px rgba(27,23,20,0.06)',
          position: 'relative', overflow: 'hidden',
        }}>
          {/* scene + dates row */}
          <div style={{ display: 'flex', gap: 12 }}>
            <div style={{ width: 96, height: 96, transform: 'rotate(-1.4deg)', flexShrink: 0 }}>
              <TripScene kind="tokyo"/>
            </div>
            <div style={{ flex: 1, minWidth: 0 }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                <TripPill kind="alive">ALIVE · 58 DAYS OUT</TripPill>
              </div>
              <div style={{
                fontFamily: T.serif, fontSize: 24, fontWeight: 500, color: T.ink,
                letterSpacing: -0.4, lineHeight: 1.05, marginTop: 6,
              }}>
                Tokyo, in May
              </div>
              <div style={{
                display: 'flex', alignItems: 'baseline', gap: 8, marginTop: 6,
              }}>
                <span style={{ fontFamily: T.serif, fontSize: 14, color: T.inkSoft, fontStyle: 'italic' }}>
                  Sat 14 → Fri 22
                </span>
                <span style={{ fontSize: 10, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 600 }}>8 NIGHTS</span>
              </div>
            </div>
          </div>

          {/* planning pieces scattered as a strip */}
          <div style={{
            marginTop: 14, display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 8,
          }}>
            {/* travelers */}
            <PlanningPiece label="2 OF 3" sub="haru pending">
              <div style={{ display: 'flex' }}>
                {[TR.ink, T.gold, 'transparent'].map((c, i) => (
                  <div key={i} style={{
                    width: 22, height: 22, borderRadius: 999, background: c === 'transparent' ? T.bg : c,
                    border: `1.5px solid ${T.cardWarm}`, marginLeft: i ? -8 : 0,
                    color: T.cardWarm, fontSize: 10, fontWeight: 600,
                    display: 'flex', alignItems: 'center', justifyContent: 'center',
                    fontFamily: T.serif, letterSpacing: 0,
                    boxShadow: c === 'transparent' ? `inset 0 0 0 1px ${T.muteSoft}` : 'none',
                  }}>{['T','A','?'][i]}</div>
                ))}
              </div>
            </PlanningPiece>

            {/* saved places */}
            <PlanningPiece label="14 SAVED" sub="3 to confirm">
              <div style={{ display: 'flex', gap: 2 }}>
                {[1,2,3,4].map(i => (
                  <TripIcons.Pin key={i} s={12} c={i === 1 ? TR.ink : T.muteSoft}/>
                ))}
              </div>
            </PlanningPiece>

            {/* decisions */}
            <PlanningPiece label="3 OPEN" sub="ryokan choice" accent>
              <TripIcons.Decision s={20}/>
            </PlanningPiece>

            {/* vesper note */}
            <PlanningPiece label="VESPER" sub="found 3 quiet rooms" gold>
              <TripIcons.Sparkle s={18} c={T.gold}/>
            </PlanningPiece>
          </div>

          {/* progress strip */}
          <div style={{
            marginTop: 14, padding: '10px 12px', background: T.bg, borderRadius: 10,
            display: 'flex', alignItems: 'center', justifyContent: 'space-between',
            border: `0.5px solid ${T.hairline}`,
          }}>
            <div>
              <div style={{ fontSize: 9.5, color: T.mute, letterSpacing: 1.6, fontWeight: 600 }}>
                NEXT · ON THE TABLE
              </div>
              <div style={{ fontFamily: T.serif, fontSize: 14, color: T.ink, marginTop: 2, letterSpacing: -0.1 }}>
                Pick a <span style={{ fontStyle: 'italic' }}>ryokan</span> for nights 5–7
              </div>
            </div>
            <div style={{
              padding: '6px 12px', background: TR.ink, color: T.cardWarm,
              borderRadius: 999, fontSize: 11, fontWeight: 600, letterSpacing: -0.1,
              display: 'flex', alignItems: 'center', gap: 4,
            }}>
              Open trip <span>→</span>
            </div>
          </div>
        </div>
      </div>

      {/* ── DRAFTS — scattered small cards ── */}
      <div style={{ padding: '16px 22px 0' }}>
        <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between' }}>
          <span style={{ fontSize: 10.5, color: T.mute, letterSpacing: 2, fontWeight: 600 }}>DRAFTS · 3</span>
          <span style={{ fontSize: 10, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 600 }}>SLIDE →</span>
        </div>
        <div style={{ marginTop: 10, display: 'flex', gap: 8, overflow: 'hidden' }}>
          {[
            { title: 'A weekend somewhere quiet', meta: 'no dates · 1 traveler', kind: 'dreaming', tilt: -1.6 },
            { title: 'Porto, return', meta: 'september · pencilled in', kind: 'alive', tilt: 1.2 },
            { title: 'Beach week', meta: 'two friends interested', kind: 'needs', tilt: -0.8 },
          ].map((d, i) => (
            <div key={i} style={{
              flex: '0 0 168px', padding: 12, background: T.cardWarm, borderRadius: 12,
              transform: `rotate(${d.tilt}deg)`,
              border: `0.5px solid ${T.hairline}`,
              boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset',
            }}>
              <TripPill kind={d.kind}>{d.kind === 'dreaming' ? 'DREAMING' : d.kind === 'needs' ? 'NEEDS YOU' : 'PENCILLED'}</TripPill>
              <div style={{
                fontFamily: T.serif, fontSize: 15, color: T.ink, fontWeight: 500,
                letterSpacing: -0.2, lineHeight: 1.1, marginTop: 8,
              }}>{d.title}</div>
              <div style={{ fontSize: 10.5, color: T.mute, fontStyle: 'italic', fontFamily: T.serif, marginTop: 4 }}>
                {d.meta}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* ── BRIDGE TO ATLAS — gentle nudge ── */}
      <div style={{ padding: '14px 22px 0' }}>
        <div style={{
          padding: '12px 14px', background: T.cardSoft, borderRadius: 12,
          border: `0.8px dashed ${T.gold}`,
          display: 'flex', alignItems: 'center', gap: 12,
        }}>
          <TripIcons.Sparkle s={14}/>
          <div style={{ flex: 1, lineHeight: 1.3 }}>
            <div style={{ fontSize: 9.5, color: T.goldDeep, fontWeight: 600, letterSpacing: 1.4 }}>
              FROM YOUR LAST TRIP · LISBON
            </div>
            <div style={{
              fontFamily: T.serif, fontSize: 14, color: T.ink, fontWeight: 500,
              letterSpacing: -0.1, marginTop: 2,
            }}>
              Vesper drafted a postcard. <span style={{ fontStyle: 'italic', color: T.mute }}>Send it to Atlas?</span>
            </div>
          </div>
          <Marks.ArrowR s={13} c={T.goldDeep}/>
        </div>
      </div>

      <TabBar active="trips"/>
    </Phone>
  );
}

function PlanningPiece({ label, sub, children, accent, gold }) {
  return (
    <div style={{
      padding: '10px 8px 8px', borderRadius: 10,
      background: gold ? 'rgba(176,133,58,0.08)' : accent ? 'rgba(176,133,58,0.06)' : T.bg,
      border: gold ? `0.6px dashed ${T.gold}`
            : accent ? `0.6px solid ${T.gold}` : `0.5px solid ${T.hairline}`,
      display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 6,
      textAlign: 'center',
    }}>
      <div style={{ minHeight: 22, display: 'flex', alignItems: 'center' }}>{children}</div>
      <div style={{ fontSize: 9, color: gold ? T.goldDeep : accent ? T.goldDeep : T.mute, letterSpacing: 1.3, fontWeight: 700 }}>
        {label}
      </div>
      <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 10, color: T.mute, lineHeight: 1.1 }}>
        {sub}
      </div>
    </div>
  );
}

window.TripsPlanningTable = TripsPlanningTable;
