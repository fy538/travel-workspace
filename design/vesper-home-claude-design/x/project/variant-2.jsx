// Variant 2 — EDITORIAL INDEX: a journal cover page meets a magazine index.
// Title block + edition stamp; the four destinations are an INDEX with numerals.

function VariantEditorial() {
  return (
    <Phone bg={T.bgDeep}>
      {/* tiny top metadata row */}
      <div style={{
        display: 'flex', justifyContent: 'space-between', alignItems: 'center',
        padding: '14px 24px 0', color: T.mute, fontSize: 10.5, letterSpacing: 1.8, fontWeight: 600,
      }}>
        <span>TIGER · NO. 047</span>
        <span style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
          <Marks.Search s={16} c={T.inkSoft}/>
          <div style={{ width: 24, height: 24, borderRadius: 999, background: T.goldDeep,
            color: T.cardWarm, fontFamily: T.serif, fontSize: 11, fontWeight: 500,
            display: 'flex', alignItems: 'center', justifyContent: 'center' }}>T</div>
        </span>
      </div>

      {/* MASTHEAD — large serif title with edition stamp */}
      <div style={{ padding: '24px 24px 0' }}>
        <div style={{ display: 'flex', alignItems: 'flex-end', justifyContent: 'space-between' }}>
          <div style={{ fontFamily: T.serif, fontSize: 13, color: T.mute, letterSpacing: 4, fontWeight: 500 }}>
            T H E&nbsp;&nbsp;A T L A S
          </div>
          <div style={{
            border: `0.8px solid ${T.gold}`, color: T.goldDeep, fontFamily: T.serif,
            fontSize: 10, letterSpacing: 1.6, fontWeight: 500, padding: '4px 7px',
            borderRadius: 2, transform: 'rotate(-2deg)',
          }}>
            VOL · III
          </div>
        </div>
        <h1 style={{
          fontFamily: T.serif, fontWeight: 400, fontSize: 72, lineHeight: 0.9,
          letterSpacing: -2.5, color: T.ink, margin: '6px 0 0',
        }}>
          Tiger,<br/>
          <span style={{ fontStyle: 'italic' }}>at large.</span>
        </h1>
        <div style={{
          marginTop: 14, display: 'flex', alignItems: 'center', gap: 10,
          color: T.mute, fontSize: 10.5, letterSpacing: 1.4, fontWeight: 600,
        }}>
          <span>SPRING ’26</span>
          <span style={{ flex: 1, height: 1, background: T.hairline }}/>
          <span>QUIET WEEK</span>
        </div>
      </div>

      {/* pull quote */}
      <div style={{
        margin: '20px 24px 0', padding: '14px 0 16px',
        borderTop: `0.5px solid ${T.hairline}`, borderBottom: `0.5px solid ${T.hairline}`,
      }}>
        <p style={{
          fontFamily: T.serif, fontStyle: 'italic', fontSize: 17, color: T.inkSoft,
          margin: 0, lineHeight: 1.35, letterSpacing: -0.2,
        }}>
          “You follow the neighborhood before the landmark.”
        </p>
        <div style={{ color: T.muteSoft, fontSize: 9.5, letterSpacing: 1.8, fontWeight: 600, marginTop: 8 }}>
          — VESPER, READING YOU
        </div>
      </div>

      {/* INDEX */}
      <div style={{ margin: '14px 24px 0' }}>
        <div style={{
          display: 'flex', justifyContent: 'space-between', alignItems: 'baseline',
          color: T.mute, fontSize: 10, letterSpacing: 2, fontWeight: 600, marginBottom: 4,
        }}>
          <span>INDEX</span><span>PG.</span>
        </div>
        {[
          { n: '01', title: 'Inbox',      sub: 'drafts & threads from Vesper', pg: '003', mark: Marks.Inbox,    note: '3 waiting', fresh: true },
          { n: '02', title: 'Map',        sub: 'cities, routes, returnings',   pg: '019', mark: Marks.Map,      note: '14 cities' },
          { n: '03', title: 'Travel DNA', sub: 'rituals, pace, neighborhoods', pg: '041', mark: Marks.DNA,      note: 'morning soul' },
          { n: '04', title: 'Postcards',  sub: 'a shelf of keepsakes',         pg: '063', mark: Marks.Postcard, note: 'bare shelf' },
        ].map((row, i) => (
          <div key={i} style={{
            display: 'grid', gridTemplateColumns: '32px 1fr auto',
            alignItems: 'center', gap: 14, padding: '14px 0',
            borderTop: `0.5px solid ${T.hairline}`,
          }}>
            <div style={{
              fontFamily: T.serif, fontSize: 22, fontWeight: 400, color: T.gold,
              fontVariantNumeric: 'oldstyle-nums', letterSpacing: -0.5,
            }}>{row.n}</div>
            <div>
              <div style={{
                display: 'flex', alignItems: 'center', gap: 8,
                fontFamily: T.serif, fontSize: 24, color: T.ink, fontWeight: 500,
                letterSpacing: -0.5, lineHeight: 1,
              }}>
                {row.title}
                {row.fresh && <span style={{ width: 5, height: 5, borderRadius: 5, background: T.gold }}/>}
              </div>
              <div style={{ fontSize: 11.5, color: T.mute, marginTop: 4, fontStyle: 'italic', fontFamily: T.serif }}>
                {row.sub}
              </div>
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
              <span style={{ fontSize: 10, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 600 }}>{row.note.toUpperCase()}</span>
              <div style={{ opacity: 0.55 }}>
                <row.mark size={36}/>
              </div>
            </div>
          </div>
        ))}
        <div style={{ borderTop: `0.5px solid ${T.hairline}`, marginTop: 0 }}/>
      </div>

      {/* colophon / latest postcard footer */}
      <div style={{
        margin: '14px 24px 0', display: 'flex', alignItems: 'center', justifyContent: 'space-between',
      }}>
        <div>
          <div style={{ fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.8, fontWeight: 600 }}>COLOPHON</div>
          <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.mute, marginTop: 3 }}>
            Set in slow time, by Vesper.
          </div>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 6, color: T.goldDeep, fontSize: 10.5, fontWeight: 600, letterSpacing: 1.6 }}>
          OPEN ISSUE <Marks.ArrowR s={11} c={T.goldDeep}/>
        </div>
      </div>

      <TabBar active="atlas"/>
    </Phone>
  );
}

window.VariantEditorial = VariantEditorial;
