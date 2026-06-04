// ─────────────────────────────────────────────────────────────
// RAIL CARD — the canonical Next Moves card. Glyph-led, ink only.
// The line-art kind glyph signals the kind; the ochre Vesper sparkle
// marks authored cards. No coloured spine, no tint, no dog-ear.
// (Earlier tag / footer / dog-ear explorations were retired.)
// ─────────────────────────────────────────────────────────────

const railBase = {
  flex: '0 0 auto', borderRadius: 12, padding: '13px 14px',
  background: T.cardWarm, border: `0.5px solid ${T.hairline}`,
  boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset, 0 8px 22px -16px rgba(0,0,0,0.14)',
  display: 'flex', flexDirection: 'column', justifyContent: 'space-between',
  minHeight: 120, position: 'relative', overflow: 'hidden',
};

function railTitle(title, meta) {
  return (
    <div>
      <div style={{
        fontFamily: T.serif, fontWeight: 500, fontSize: 15.5, color: T.ink,
        letterSpacing: -0.2, lineHeight: 1.15,
      }}>{title}</div>
      <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 11, color: T.mute, marginTop: 4, lineHeight: 1.25 }}>
        {meta}
      </div>
    </div>
  );
}

function railAction(primary, color = T.inkSoft) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
      <span style={{ fontSize: 11, color, fontWeight: 600, letterSpacing: -0.05 }}>{primary}</span>
      <span style={{ fontSize: 11, color: T.muteSoft }}>→</span>
    </div>
  );
}

// ─── 1 · GLYPH-LED (ink only, no colour) ────────────────────────
function RailGlyph({ fam, title, meta, primary, width = 214 }) {
  const m = FAM[fam];
  const Glyph = CardGlyph[m.glyph] || CardGlyph.docket;
  return (
    <div style={{ ...railBase, width }}>
      <div>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 10 }}>
          <Glyph s={19} c={T.ink}/>
          {m.vesper && <VesperMark s={11} c={T.mute}/>}
        </div>
        {railTitle(title, meta)}
      </div>
      <div style={{ marginTop: 10 }}>{railAction(primary)}</div>
    </div>
  );
}

// ─── A rail strip rendering the canonical glyph card, for the spec. ──
function RailStrip({ Comp = RailGlyph }) {
  return (
    <div style={{ display: 'flex', gap: 8, overflow: 'hidden', width: '100%' }}>
      <Comp fam="prepared" title="Tokyo itinerary draft" meta="6 stops · ready to skim" primary="Open"/>
      <Comp fam="signal" title="Quiet over landmarks" meta="a pattern, across 3 cities" primary="What I saw"/>
      <Comp fam="capture" title="Williamsburg sunday" meta="12 photos · postcard?" primary="Keep"/>
    </div>
  );
}

Object.assign(window, { RailGlyph, RailStrip });
