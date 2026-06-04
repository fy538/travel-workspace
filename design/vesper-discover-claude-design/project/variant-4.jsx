// Variant 4 — ALMANAC: Atlas as a year-at-a-glance ribbon.
// Time is the spine. Months tick down the left; trips mark the ribbon.
// The four destinations live at the bottom as chapter-tabs.

function VariantAlmanac() {
  const months = [
    { m: 'JAN', dot: null },
    { m: 'FEB', dot: 'mid' },
    { m: 'MAR', dot: 'now', label: 'Lisbon · 6 d' },
    { m: 'APR', dot: null },
    { m: 'MAY', dot: 'planned', label: 'Tokyo · planned' },
    { m: 'JUN', dot: null },
    { m: 'JUL', dot: null },
    { m: 'AUG', dot: 'mid', label: 'Mexico City' },
    { m: 'SEP', dot: null },
    { m: 'OCT', dot: 'mid', label: 'Porto' },
    { m: 'NOV', dot: null },
    { m: 'DEC', dot: null },
  ];

  return (
    <Phone bg={T.bg}>
      {/* Top bar */}
      <div style={{
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        padding: '14px 24px 0',
      }}>
        <div style={{
          width: 30, height: 30, borderRadius: 999, background: T.goldDeep,
          color: T.cardWarm, fontFamily: T.serif, fontWeight: 500, fontSize: 14,
          display: 'flex', alignItems: 'center', justifyContent: 'center',
        }}>T</div>
        <div style={{ fontSize: 10.5, color: T.mute, letterSpacing: 2, fontWeight: 600 }}>
          TIGER’S ALMANAC
        </div>
        <Marks.Search s={19} c={T.inkSoft}/>
      </div>

      {/* Title + meta */}
      <div style={{ padding: '22px 24px 0' }}>
        <div style={{ display: 'flex', alignItems: 'flex-end', justifyContent: 'space-between' }}>
          <h1 style={{
            fontFamily: T.serif, fontWeight: 500, fontSize: 72, lineHeight: 0.92,
            letterSpacing: -2.5, color: T.ink, margin: 0,
          }}>
            <span style={{ fontStyle: 'italic' }}>’26</span>
          </h1>
          <div style={{ textAlign: 'right' }}>
            <div style={{ fontSize: 10.5, color: T.mute, letterSpacing: 1.8, fontWeight: 600 }}>SO FAR</div>
            <div style={{ fontFamily: T.serif, fontSize: 28, fontWeight: 500, color: T.ink, letterSpacing: -0.5, lineHeight: 1, marginTop: 4 }}>
              2 trips · <span style={{ color: T.gold }}>1 ahead</span>
            </div>
          </div>
        </div>
        <p style={{
          fontFamily: T.serif, fontStyle: 'italic', fontSize: 15, color: T.mute,
          margin: '14px 0 0', lineHeight: 1.4, maxWidth: 290,
        }}>
          “You follow the neighborhood before the landmark.”
        </p>
      </div>

      {/* Year ribbon */}
      <div style={{
        margin: '20px 24px 0', display: 'flex', gap: 16,
      }}>
        {/* spine */}
        <div style={{ position: 'relative', width: 14, flexShrink: 0 }}>
          <div style={{
            position: 'absolute', left: 6, top: 6, bottom: 6, width: 1,
            background: T.hairline,
          }}/>
        </div>
        <div style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
          {months.map((mo, i) => (
            <div key={mo.m} style={{
              display: 'grid', gridTemplateColumns: '40px 14px 1fr',
              alignItems: 'center', height: 26, position: 'relative',
              marginLeft: -30, /* pull caption into spine column */
            }}>
              <div style={{
                fontSize: 9.5, color: mo.dot === 'now' ? T.ink : T.muteSoft,
                letterSpacing: 1.6, fontWeight: 600, textAlign: 'right',
                paddingRight: 6,
              }}>{mo.m}</div>
              <div style={{ display: 'flex', justifyContent: 'center' }}>
                {mo.dot === 'now' && (
                  <div style={{
                    width: 9, height: 9, borderRadius: 999, background: T.gold,
                    boxShadow: `0 0 0 4px rgba(176,133,58,0.18)`,
                  }}/>
                )}
                {mo.dot === 'mid' && (
                  <div style={{ width: 6, height: 6, borderRadius: 999, background: T.inkSoft }}/>
                )}
                {mo.dot === 'planned' && (
                  <div style={{
                    width: 7, height: 7, borderRadius: 999,
                    border: `1px solid ${T.gold}`, background: T.bg,
                  }}/>
                )}
                {!mo.dot && (
                  <div style={{ width: 3, height: 3, borderRadius: 999, background: T.muteSoft, opacity: 0.6 }}/>
                )}
              </div>
              <div style={{ paddingLeft: 12, display: 'flex', alignItems: 'center', gap: 8 }}>
                {mo.label && (
                  <>
                    <span style={{
                      fontFamily: T.serif, fontStyle: mo.dot === 'planned' ? 'italic' : 'normal',
                      fontSize: 15, color: mo.dot === 'now' ? T.ink : T.inkSoft,
                      letterSpacing: -0.2, lineHeight: 1, fontWeight: 500,
                    }}>{mo.label}</span>
                    {mo.dot === 'now' && (
                      <span style={{ fontSize: 9, color: T.gold, letterSpacing: 1.6, fontWeight: 700 }}>NOW</span>
                    )}
                  </>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Chapter tabs — the 4 destinations */}
      <div style={{ position: 'absolute', bottom: 96, left: 16, right: 16 }}>
        <div style={{
          display: 'flex', justifyContent: 'space-between', alignItems: 'baseline',
          padding: '0 8px 8px', color: T.mute, fontSize: 10, letterSpacing: 2, fontWeight: 600,
        }}>
          <span>CHAPTERS</span>
          <span style={{ color: T.muteSoft, letterSpacing: 1.5 }}>FOUR</span>
        </div>
        <div style={{
          background: T.cardWarm, borderRadius: 18, padding: '6px',
          display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 2,
          boxShadow: '0 0 0 0.5px rgba(27,23,20,0.06), 0 1px 0 rgba(255,255,255,0.6) inset',
        }}>
          {[
            { n: 'I',   label: 'Inbox',   meta: '3' },
            { n: 'II',  label: 'Map',     meta: '14' },
            { n: 'III', label: 'DNA',     meta: '6' },
            { n: 'IV',  label: 'Postcards', meta: '—' },
          ].map((c, i) => (
            <div key={c.n} style={{
              padding: '14px 8px 12px', textAlign: 'center',
              borderRight: i < 3 ? `0.5px solid ${T.hairline}` : 'none',
              position: 'relative',
            }}>
              <div style={{
                fontFamily: T.serif, fontStyle: 'italic', fontSize: 13,
                color: T.gold, letterSpacing: 0.2,
              }}>{c.n}</div>
              <div style={{
                fontFamily: T.serif, fontSize: 16, fontWeight: 500, color: T.ink,
                letterSpacing: -0.2, lineHeight: 1, marginTop: 6,
              }}>{c.label}</div>
              <div style={{
                fontSize: 10, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 600, marginTop: 4,
              }}>{c.meta}</div>
              {i === 0 && (
                <div style={{
                  position: 'absolute', top: 8, right: 10, width: 5, height: 5,
                  borderRadius: 5, background: T.gold,
                }}/>
              )}
            </div>
          ))}
        </div>
      </div>

      <TabBar active="atlas"/>
    </Phone>
  );
}

window.VariantAlmanac = VariantAlmanac;
