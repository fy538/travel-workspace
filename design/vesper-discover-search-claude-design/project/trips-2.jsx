// Direction B — DEPARTURE BOARD
// A refined "operations" view. Vertical list with serif date numerals on the
// left, trip name + status on the right. Decisions and starters live below.

function TripsDepartureBoard() {
  return (
    <Phone bg={T.bg}>
      <TripsTopBar eyebrow="TRIPS · BOARD"/>

      {/* Title */}
      <div style={{ padding: '18px 22px 0' }}>
        <div style={{
          display: 'flex', alignItems: 'flex-end', justifyContent: 'space-between',
        }}>
          <h1 style={{
            fontFamily: T.serif, fontWeight: 500, fontSize: 42, lineHeight: 0.96,
            letterSpacing: -1.2, color: T.ink, margin: 0,
          }}>
            Departures.
          </h1>
          <div style={{
            border: `0.8px solid ${TR.ink}`, padding: '3px 8px', borderRadius: 2,
            color: TR.ink, fontFamily: T.mono, fontSize: 10, letterSpacing: 1.5, fontWeight: 500,
          }}>
            MAR 14 · 09:41
          </div>
        </div>
        <div style={{
          marginTop: 8, fontSize: 11.5, color: T.mute, fontStyle: 'italic', fontFamily: T.serif,
        }}>
          three on the board, three on the table.
        </div>
      </div>

      {/* ── DEPARTURE LIST ── */}
      <div style={{ padding: '16px 22px 0' }}>
        <div style={{
          display: 'flex', justifyContent: 'space-between', alignItems: 'baseline',
          fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.8, fontWeight: 600,
          paddingBottom: 8, borderBottom: `0.5px solid ${T.hairline}`,
        }}>
          <span>WHEN · TRIP · STATE</span>
          <span>OPEN</span>
        </div>
        {[
          { date: ['MAY', '14'], days: 58, title: 'Tokyo', sub: 'in cherry-blossom tail', pill: 'alive', pillText: 'ALIVE · 8 NIGHTS', users: 2 },
          { date: ['JUN', '06'], days: 81, title: 'Porto, return', sub: 'pencilled with Ana', pill: 'needs', pillText: 'NEEDS YOU · DATES', users: 2 },
          { date: ['SEP', '—'],  days: null, title: 'Beach week', sub: '“two friends interested”', pill: 'dreaming', pillText: 'IN VOTING', users: 4 },
          { date: ['—',   '—'],  days: null, title: 'A weekend, somewhere quiet', sub: 'no dates yet', pill: 'dreaming', pillText: 'DREAMING' },
        ].map((row, i) => (
          <div key={i} style={{
            padding: '14px 0', borderBottom: `0.5px solid ${T.hairThin}`,
            display: 'grid', gridTemplateColumns: '54px 1fr auto', gap: 12, alignItems: 'center',
          }}>
            {/* date column — train-board style */}
            <div style={{ textAlign: 'center' }}>
              <div style={{
                fontSize: 9, color: row.pill === 'alive' ? TR.ink : T.muteSoft,
                letterSpacing: 1.6, fontWeight: 700,
              }}>{row.date[0]}</div>
              <div style={{
                fontFamily: T.serif, fontSize: 28, fontWeight: 500,
                color: row.pill === 'alive' ? T.ink : T.inkSoft,
                lineHeight: 1, marginTop: 2, fontVariantNumeric: 'oldstyle-nums',
                letterSpacing: -0.5,
              }}>{row.date[1]}</div>
              {row.days != null && (
                <div style={{ fontSize: 8, color: T.muteSoft, letterSpacing: 1, fontWeight: 600, marginTop: 4 }}>
                  {row.days}D OUT
                </div>
              )}
            </div>
            {/* middle */}
            <div>
              <div style={{
                fontFamily: T.serif, fontSize: 20, fontWeight: 500, color: T.ink,
                letterSpacing: -0.3, lineHeight: 1.05,
              }}>{row.title}</div>
              <div style={{
                fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.mute,
                marginTop: 4, lineHeight: 1.3,
              }}>{row.sub}</div>
              <div style={{ marginTop: 6, display: 'flex', alignItems: 'center', gap: 8 }}>
                <TripPill kind={row.pill}>{row.pillText}</TripPill>
                {row.users != null && <TripIcons.Users n={row.users} accent={row.pill === 'alive' ? TR.ink : T.muteSoft}/>}
              </div>
            </div>
            {/* arrow */}
            <Marks.ArrowR s={14} c={T.mute}/>
          </div>
        ))}
      </div>

      {/* ── UNRESOLVED ── */}
      <div style={{ padding: '14px 22px 0' }}>
        <div style={{
          padding: '12px 14px', background: 'rgba(176,133,58,0.08)', borderRadius: 12,
          border: `0.8px solid rgba(176,133,58,0.30)`,
          display: 'flex', alignItems: 'center', gap: 12,
        }}>
          <TripIcons.Decision s={18}/>
          <div style={{ flex: 1 }}>
            <div style={{ fontSize: 9.5, color: T.goldDeep, letterSpacing: 1.4, fontWeight: 700 }}>
              UNRESOLVED · 4
            </div>
            <div style={{
              fontFamily: T.serif, fontSize: 14, color: T.ink, fontWeight: 500,
              letterSpacing: -0.1, marginTop: 2, lineHeight: 1.25,
            }}>
              <span style={{ fontStyle: 'italic' }}>Ryokan</span> in Tokyo · <span style={{ fontStyle: 'italic' }}>dates</span> for Porto · 2 more
            </div>
          </div>
          <Marks.ArrowR s={13} c={T.goldDeep}/>
        </div>
      </div>

      {/* ── STARTERS — tight inline ── */}
      <div style={{ padding: '14px 16px 0' }}>
        <div style={{
          display: 'flex', justifyContent: 'space-between', alignItems: 'baseline',
          padding: '0 6px',
        }}>
          <span style={{ fontSize: 9.5, color: T.mute, letterSpacing: 1.8, fontWeight: 600 }}>QUICK STARTS</span>
          <span style={{ fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 600 }}>OR ASK VESPER</span>
        </div>
        <div style={{ marginTop: 8, display: 'flex', gap: 6, overflow: 'hidden' }}>
          <SmallStart name="City"     glyph={<StarterGlyphs.City/>}/>
          <SmallStart name="Beach"    glyph={<StarterGlyphs.Beach/>}/>
          <SmallStart name="Mountain" glyph={<StarterGlyphs.Mountain/>}/>
          <SmallStart name="Road"     glyph={<StarterGlyphs.Road/>}/>
          <SmallStart name="Festival" glyph={<StarterGlyphs.Festival/>}/>
        </div>
      </div>

      <TabBar active="trips"/>
    </Phone>
  );
}

function SmallStart({ name, glyph }) {
  return (
    <div style={{
      flex: 1, padding: '10px 6px 8px', background: T.cardWarm, borderRadius: 10,
      border: `0.5px solid ${T.hairline}`,
      display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 4,
      boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset',
    }}>
      {glyph}
      <span style={{ fontSize: 10.5, color: T.inkSoft, fontWeight: 500 }}>{name}</span>
    </div>
  );
}

window.TripsDepartureBoard = TripsDepartureBoard;
