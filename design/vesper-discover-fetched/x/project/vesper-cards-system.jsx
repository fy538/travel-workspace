// ─────────────────────────────────────────────────────────────
// NOW CARD + NEXT MOVES RAIL SYSTEM
// One full Now card (paper object) + a horizontal rail of compact,
// glyph-led paper cards (RailGlyph, from vesper-rail-variants).
// ─────────────────────────────────────────────────────────────

// The recommended home composition.
function NowAndRail() {
  return (
    <Phone bg={T.bg}>
      <VesperTopBar ctx={<>VESPER · WED MAR 14 · 9:41</>}/>

      {/* Lead note — Vesper speaks on the page */}
      <div style={{ padding: '14px 22px 0' }}>
        <VesperEyebrow trailing="ONE TO DECIDE"/>
        <p style={{
          fontFamily: T.serif, fontSize: 18, color: T.ink, margin: '10px 0 0',
          lineHeight: 1.4, letterSpacing: -0.1,
        }}>
          Tokyo needs <em>one decision</em> today. The rest can wait — I’ve kept it warm.
        </p>
      </div>

      {/* NOW CARD — the single highest-signal card, full object */}
      <div style={{ padding: '16px 16px 0' }}>
        <div style={{ fontSize: 9.5, letterSpacing: 2, color: T.mute, fontWeight: 700, marginBottom: 8, paddingLeft: 4 }}>
          NOW
        </div>
        <CardCall palette="paper"/>
      </div>

      {/* NEXT MOVES — compact, spine-coded rail */}
      <div style={{ padding: '18px 0 0' }}>
        <div style={{
          display: 'flex', alignItems: 'baseline', justifyContent: 'space-between',
          padding: '0 22px 8px',
        }}>
          <span style={{ fontSize: 9.5, letterSpacing: 2, color: T.mute, fontWeight: 700 }}>NEXT MOVES · 5</span>
          <span style={{ fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 600 }}>SLIDE →</span>
        </div>
        <div style={{
          display: 'flex', gap: 8, overflow: 'hidden', padding: '0 16px',
        }}>
          <RailGlyph fam="prepared" title="Tokyo itinerary draft" meta="6 stops · ready to skim" primary="Open"/>
          <RailGlyph fam="signal" title="Quiet over landmarks" meta="a pattern, across 3 cities" primary="What I saw"/>
          <RailGlyph fam="capture" title="Williamsburg sunday" meta="12 photos · postcard?" primary="Keep"/>
        </div>
      </div>

      {/* Composer */}
      <div style={{ position: 'absolute', bottom: 96, left: 16, right: 16 }}>
        <Composer placeholder="Ask Vesper, or pick one above…"/>
      </div>

      <TabBar active="vesper"/>
    </Phone>
  );
}

window.NowAndRail = NowAndRail;
