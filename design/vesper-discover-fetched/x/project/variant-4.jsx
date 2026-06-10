// Variant 4 — ALMANAC: Atlas as a year-at-a-glance, the view the
// home's Year ribbon opens into. A scrolling timeline that fills the
// screen and fades at both ends; each trip carries a subtitle.
// Time is the spine — months tick down, trips mark the year.

function VariantAlmanac() {
  const months = [
    { m: 'JAN' },
    { m: 'FEB' },
    { m: 'MAR', dot: 'now', city: 'Lisbon', meta: '6 days', sub: 'Alfama mornings, Ramiro, a fado room nobody told you about' },
    { m: 'APR' },
    { m: 'MAY', dot: 'planned', city: 'Tokyo', meta: 'planned · 8 days', sub: 'the cherry-blossom window, if the timing holds' },
    { m: 'JUN' },
    { m: 'JUL' },
    { m: 'AUG', dot: 'past', city: 'Mexico City', meta: '5 days', sub: 'Roma Norte, La Esquina at dawn, a long Sunday' },
    { m: 'SEP' },
    { m: 'OCT', dot: 'past', city: 'Porto', meta: '4 days', sub: 'the Ribeira — three walks, never the bridge' },
    { m: 'NOV' },
    { m: 'DEC' },
  ];

  const Dot = ({ kind }) => {
    if (kind === 'now') return <div style={{ width: 11, height: 11, borderRadius: 999, background: T.gold, boxShadow: '0 0 0 4px rgba(176,133,58,0.18)' }}/>;
    if (kind === 'planned') return <div style={{ width: 9, height: 9, borderRadius: 999, border: `1.4px solid ${T.gold}`, background: T.bg }}/>;
    if (kind === 'past') return <div style={{ width: 8, height: 8, borderRadius: 999, background: T.inkSoft }}/>;
    return <div style={{ width: 3, height: 3, borderRadius: 999, background: T.muteSoft, opacity: 0.55 }}/>;
  };

  return (
    <Phone bg={T.bg}>
      <div style={{ position: 'absolute', inset: 0, display: 'flex', flexDirection: 'column' }}>
        {/* Top bar — back · title · search (cleared below the status bar) */}
        <div style={{ flexShrink: 0, display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '60px 22px 0' }}>
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M15 5l-7 7 7 7"/></svg>
          <div style={{ fontFamily: T.mono, fontSize: 10, color: T.mute, letterSpacing: 2, fontWeight: 600 }}>TIGER’S ALMANAC</div>
          <Marks.Search s={19} c={T.inkSoft}/>
        </div>

        {/* Title + meta */}
        <div style={{ flexShrink: 0, padding: '18px 24px 0' }}>
          <div style={{ display: 'flex', alignItems: 'flex-end', justifyContent: 'space-between' }}>
            <h1 style={{ fontFamily: T.serif, fontWeight: 500, fontSize: 64, lineHeight: 0.9, letterSpacing: -2.5, color: T.ink, margin: 0 }}>
              <span>’26</span>
            </h1>
            <div style={{ textAlign: 'right' }}>
              <div style={{ fontFamily: T.mono, fontSize: 9, color: T.mute, letterSpacing: 1.8, fontWeight: 600 }}>SO FAR</div>
              <div style={{ fontFamily: T.serif, fontSize: 25, fontWeight: 500, color: T.ink, letterSpacing: -0.5, lineHeight: 1, marginTop: 4 }}>
                3 kept · <span style={{ color: T.gold }}>1 ahead</span>
              </div>
            </div>
          </div>
          <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 14.5, color: T.mute, margin: '12px 0 0', lineHeight: 1.4, maxWidth: 290 }}>
            “You follow the neighborhood before the landmark.”
          </p>
        </div>

        {/* The timeline — fills the rest, fades at both ends, scrolls */}
        <div style={{
          flex: 1, minHeight: 0, marginTop: 16, overflowY: 'auto',
          WebkitMaskImage: 'linear-gradient(to bottom, transparent 0, #000 40px, #000 calc(100% - 40px), transparent 100%)',
          maskImage: 'linear-gradient(to bottom, transparent 0, #000 40px, #000 calc(100% - 40px), transparent 100%)',
        }}>
          <div style={{ padding: '8px 24px 28px' }}>
            {months.map((mo) => {
              const trip = !!mo.city;
              return (
                <div key={mo.m} style={{ display: 'grid', gridTemplateColumns: '40px 18px 1fr', columnGap: 12, alignItems: 'stretch' }}>
                  {/* month */}
                  <div style={{ paddingTop: trip ? 1 : 0, fontFamily: T.mono, fontSize: 9.5, color: mo.dot === 'now' ? T.ink : T.muteSoft, letterSpacing: 1.5, fontWeight: 600, textAlign: 'right' }}>{mo.m}</div>
                  {/* spine + dot */}
                  <div style={{ position: 'relative' }}>
                    <div style={{ position: 'absolute', left: '50%', top: 0, bottom: 0, width: 1, background: T.hairline, transform: 'translateX(-0.5px)' }}/>
                    <div style={{ position: 'absolute', left: '50%', top: 2, transform: 'translateX(-50%)', display: 'flex' }}><Dot kind={mo.dot}/></div>
                  </div>
                  {/* content */}
                  <div style={{ paddingBottom: trip ? 20 : 14, minHeight: trip ? 0 : 16 }}>
                    {trip && (
                      <>
                        <div style={{ display: 'flex', alignItems: 'baseline', gap: 9 }}>
                          <span style={{ fontFamily: T.serif, fontSize: 21, fontWeight: 500, color: mo.dot === 'now' ? T.ink : T.inkSoft, fontStyle: mo.dot === 'planned' ? 'italic' : 'normal', letterSpacing: -0.4, lineHeight: 1 }}>{mo.city}</span>
                          {mo.dot === 'now' && <span style={{ fontFamily: T.mono, fontSize: 8.5, color: T.gold, letterSpacing: 1.6, fontWeight: 700 }}>NOW</span>}
                        </div>
                        <div style={{ fontFamily: T.mono, fontSize: 8.5, color: mo.dot === 'planned' ? T.goldDeep : T.muteSoft, letterSpacing: 1.2, fontWeight: 600, marginTop: 5 }}>{mo.meta.toUpperCase()}</div>
                        <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.mute, lineHeight: 1.4, margin: '6px 0 0' }}>{mo.sub}</p>
                      </>
                    )}
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>

      <TabBar active="atlas"/>
    </Phone>
  );
}

window.VariantAlmanac = VariantAlmanac;
