// Variant 6 — VESPER'S LETTER: the screen reads as a hand-set letter.
// Prose-first. The four destinations appear as inline footnotes + enclosures.

function VariantLetter() {
  return (
    <Phone bg={T.bg}>
      {/* Top bar — minimal */}
      <div style={{
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        padding: '14px 24px 0',
      }}>
        <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 14, color: T.mute }}>
          a letter from <span style={{ color: T.goldDeep }}>vesper</span>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
          <Marks.Search s={18} c={T.inkSoft}/>
          <div style={{ width: 28, height: 28, borderRadius: 999, background: T.goldDeep,
            color: T.cardWarm, fontFamily: T.serif, fontSize: 13, fontWeight: 500,
            display: 'flex', alignItems: 'center', justifyContent: 'center' }}>T</div>
        </div>
      </div>

      {/* Date line */}
      <div style={{
        padding: '20px 28px 0',
        display: 'flex', alignItems: 'baseline', justifyContent: 'space-between',
      }}>
        <div style={{ fontFamily: T.serif, fontSize: 14, fontStyle: 'italic', color: T.mute }}>
          14 March, slow afternoon —
        </div>
        <div style={{ fontFamily: T.mono, fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.2 }}>
          NO. 047
        </div>
      </div>

      {/* Salutation */}
      <div style={{ padding: '14px 28px 0' }}>
        <h1 style={{
          fontFamily: T.serif, fontWeight: 400, fontSize: 44, lineHeight: 1,
          letterSpacing: -1.2, color: T.ink, margin: 0,
        }}>
          Dear <span style={{ fontStyle: 'italic' }}>Tiger</span>,
        </h1>
      </div>

      {/* Body — the letter, with inline destination references */}
      <div style={{
        padding: '16px 28px 0',
        fontFamily: T.serif, fontSize: 17.5, lineHeight: 1.45,
        color: T.inkSoft, letterSpacing: -0.1,
      }}>
        <p style={{ margin: 0 }}>
          A <em>quieter week</em>, but a good one. You follow the neighborhood
          before the landmark, and I’ve been keeping notes
          <Sup n="I" gold/> on three drafts that found you.
        </p>
        <p style={{ margin: '12px 0 0' }}>
          Your year so far reads like fourteen small towns
          <Sup n="II"/> — and a soul that wakes early
          <Sup n="III"/>. The shelf is bare
          <Sup n="IV"/>, but March is patient.
        </p>
        <div style={{
          marginTop: 14, fontFamily: T.serif, fontStyle: 'italic',
          fontSize: 15, color: T.mute,
        }}>
          — V.
        </div>
      </div>

      {/* Hairline */}
      <div style={{
        margin: '20px 28px 0', display: 'flex', alignItems: 'center', gap: 10,
        color: T.muteSoft, fontSize: 10, letterSpacing: 2, fontWeight: 600,
      }}>
        <span>ENCLOSED</span>
        <span style={{ flex: 1, height: 1, background: T.hairline }}/>
        <span>FOUR</span>
      </div>

      {/* Enclosures — four destination tiles, footnote-style */}
      <div style={{ padding: '14px 22px 0', display: 'flex', flexDirection: 'column', gap: 8 }}>
        {[
          { n: 'I',   name: 'Inbox',      mark: Marks.Inbox,    sub: 'three drafts waiting for you', meta: 'OPEN', fresh: true },
          { n: 'II',  name: 'Map',        mark: Marks.Map,      sub: 'fourteen small towns this year', meta: '14' },
          { n: 'III', name: 'Travel DNA', mark: Marks.DNA,      sub: 'an early-morning soul, six rituals', meta: 'READ' },
          { n: 'IV',  name: 'Postcards',  mark: Marks.Postcard, sub: 'the shelf is bare, March is patient', meta: 'BEGIN' },
        ].map((row) => (
          <div key={row.n} style={{
            display: 'grid', gridTemplateColumns: '24px 44px 1fr auto',
            alignItems: 'center', gap: 12,
            padding: '10px 14px', background: T.cardWarm, borderRadius: 10,
            boxShadow: '0 0 0 0.5px rgba(27,23,20,0.05)',
          }}>
            <div style={{
              fontFamily: T.serif, fontStyle: 'italic', fontSize: 15,
              color: T.gold, letterSpacing: 0,
            }}>{row.n}.</div>
            <div style={{ opacity: 0.85, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
              <row.mark size={44}/>
            </div>
            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                <span style={{ fontFamily: T.serif, fontSize: 18, fontWeight: 500, color: T.ink, letterSpacing: -0.2, lineHeight: 1 }}>
                  {row.name}
                </span>
                {row.fresh && <span style={{ width: 5, height: 5, borderRadius: 5, background: T.gold }}/>}
              </div>
              <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.mute, marginTop: 3, lineHeight: 1.3 }}>
                {row.sub}
              </div>
            </div>
            <div style={{
              fontFamily: T.mono, fontSize: 9, color: T.mute, letterSpacing: 1.4,
              padding: '3px 7px', border: `0.6px solid ${T.hairline}`, borderRadius: 2,
            }}>{row.meta}</div>
          </div>
        ))}
      </div>

      <TabBar active="atlas"/>
    </Phone>
  );
}

function Sup({ n, gold }) {
  return (
    <sup style={{
      fontFamily: T.serif, fontStyle: 'italic', fontSize: 11,
      color: gold ? T.gold : T.goldDeep, marginLeft: 1, marginRight: 1,
      fontWeight: 500,
    }}>{n}</sup>
  );
}

window.VariantLetter = VariantLetter;
