// Variant 5 — PASSPORT: Atlas as a passport interior.
// Each destination is a stamp, each visit a mark. Dense, tactile, keepsake.

function VariantPassport() {
  return (
    <Phone bg="#E5DECB">
      {/* faint passport guilloché texture using simple SVG */}
      <svg style={{ position: 'absolute', inset: 54, opacity: 0.12, pointerEvents: 'none' }}
           width="100%" height="100%" viewBox="0 0 393 800" preserveAspectRatio="none">
        <defs>
          <pattern id="hatch" width="22" height="22" patternUnits="userSpaceOnUse">
            <path d="M0 22 L22 0" stroke="#1B1714" strokeWidth="0.4"/>
          </pattern>
        </defs>
        <rect width="393" height="800" fill="url(#hatch)"/>
      </svg>

      {/* Top — passport header */}
      <div style={{
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        padding: '14px 24px 0', position: 'relative', zIndex: 2,
      }}>
        <div style={{ fontSize: 10, color: T.mute, letterSpacing: 2, fontWeight: 600 }}>
          ATLAS · PERSONAL ISSUE
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
          <Marks.Search s={17} c={T.inkSoft}/>
          <div style={{ width: 26, height: 26, borderRadius: 999, background: T.goldDeep,
            color: T.cardWarm, fontFamily: T.serif, fontSize: 12, fontWeight: 500,
            display: 'flex', alignItems: 'center', justifyContent: 'center' }}>T</div>
        </div>
      </div>

      {/* Bearer block — like a passport bio page */}
      <div style={{
        margin: '20px 24px 0', padding: '18px 20px',
        background: '#F2ECD9', borderRadius: 6,
        border: `0.8px solid ${T.gold}`, position: 'relative', zIndex: 2,
      }}>
        <div style={{
          display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start',
        }}>
          <div>
            <div style={{ fontSize: 9, color: T.mute, letterSpacing: 1.8, fontWeight: 600 }}>BEARER</div>
            <div style={{
              fontFamily: T.serif, fontSize: 30, color: T.ink, fontWeight: 500,
              letterSpacing: -0.6, lineHeight: 1, marginTop: 4,
            }}>Tiger Wang</div>
            <div style={{ fontSize: 11, color: T.mute, marginTop: 6, fontStyle: 'italic', fontFamily: T.serif }}>
              follows the neighborhood before the landmark
            </div>
          </div>
          <div style={{
            border: `0.8px solid ${T.goldDeep}`, padding: '6px 8px', borderRadius: 2,
            textAlign: 'center', transform: 'rotate(2deg)',
          }}>
            <div style={{ fontFamily: T.mono, fontSize: 9, color: T.goldDeep, letterSpacing: 1.4 }}>NO.</div>
            <div style={{ fontFamily: T.serif, fontSize: 18, color: T.goldDeep, fontWeight: 500, lineHeight: 1 }}>047</div>
          </div>
        </div>
        <div style={{
          display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: 14, marginTop: 14,
          paddingTop: 12, borderTop: `0.5px dashed ${T.hairline}`,
        }}>
          {[
            ['ISSUED', '03 · MAR ’24'],
            ['STAMPS', '14'],
            ['PACE',   'SLOW'],
          ].map(([k, v]) => (
            <div key={k}>
              <div style={{ fontSize: 8.5, color: T.mute, letterSpacing: 1.6, fontWeight: 600 }}>{k}</div>
              <div style={{ fontFamily: T.serif, fontSize: 15, color: T.ink, fontWeight: 500, marginTop: 2 }}>{v}</div>
            </div>
          ))}
        </div>
      </div>

      {/* The four destinations as STAMPS */}
      <div style={{
        margin: '20px 24px 0',
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        color: T.mute, fontSize: 10, letterSpacing: 2, fontWeight: 600,
        position: 'relative', zIndex: 2,
      }}>
        <span>RESIDENT STAMPS</span>
        <span style={{ color: T.muteSoft, letterSpacing: 1.5 }}>TAP TO ENTER</span>
      </div>

      <div style={{
        margin: '12px 22px 0', display: 'grid', gridTemplateColumns: '1fr 1fr',
        gap: 14, position: 'relative', zIndex: 2,
      }}>
        <Stamp name="INBOX"      sub="drafts in transit" count="03 / NEW" rot={-3.4} variant="circle" mark={<Marks.Inbox size={44}/>}/>
        <Stamp name="MAP"        sub="14 cities · 7 countries" count="VOL · III" rot={2.6} variant="rect" mark={<Marks.Map size={44}/>}/>
        <Stamp name="TRAVEL DNA" sub="rituals · pace · habit" count="6 RITUALS" rot={-1.8} variant="rect" mark={<Marks.DNA size={44}/>}/>
        <Stamp name="POSTCARDS"  sub="a shelf of keepsakes" count="— BARE —" rot={3.2} variant="circle" muted mark={<Marks.Postcard size={44}/>}/>
      </div>

      {/* margin notation */}
      <div style={{
        position: 'absolute', bottom: 96, left: 24, right: 24,
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.6, fontWeight: 600,
        zIndex: 2,
      }}>
        <span>NEXT STAMP · TOKYO · MAY ’26</span>
        <Marks.ArrowR s={11} c={T.muteSoft}/>
      </div>

      <TabBar active="atlas"/>
    </Phone>
  );
}

function Stamp({ name, sub, count, rot = 0, variant = 'rect', mark, muted }) {
  const ink = muted ? T.muteSoft : T.goldDeep;
  return (
    <div style={{
      transform: `rotate(${rot}deg)`, position: 'relative',
      padding: variant === 'circle' ? '14px 10px' : '14px 12px',
      border: `1.2px ${muted ? 'dashed' : 'solid'} ${ink}`,
      borderRadius: variant === 'circle' ? 999 : 4,
      aspectRatio: variant === 'circle' ? '1 / 1' : 'auto',
      textAlign: 'center', background: 'rgba(250,246,234,0.55)',
      boxShadow: muted ? 'none' : '0 1px 0 rgba(255,255,255,0.4) inset',
      display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center',
      gap: 4,
    }}>
      <div style={{ opacity: muted ? 0.45 : 0.85 }}>{mark}</div>
      <div style={{
        fontFamily: T.serif, fontSize: variant === 'circle' ? 14 : 15,
        fontWeight: 500, color: muted ? T.mute : T.ink, letterSpacing: 0.4,
        textTransform: 'uppercase', lineHeight: 1,
      }}>{name}</div>
      <div style={{
        fontSize: 9, color: T.mute, fontStyle: 'italic', fontFamily: T.serif,
        marginTop: 2, maxWidth: 130, lineHeight: 1.2,
      }}>{sub}</div>
      <div style={{
        fontFamily: T.mono, fontSize: 8.5, color: ink, letterSpacing: 1.2,
        marginTop: 4, padding: '2px 6px',
        border: `0.6px solid ${ink}`, borderRadius: 2,
      }}>{count}</div>
    </div>
  );
}

window.VariantPassport = VariantPassport;
