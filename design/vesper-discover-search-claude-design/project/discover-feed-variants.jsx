// ═══════════════════════════════════════════════════════════════
// FEED CARD VARIATIONS — alternative shapes for the Discover feed.
// The "hero overlay" restores the borderless title-on-image card.
// Reuses discover-kit (Plate, LensChip, VesperBy, FieldEyebrow, D).
// ═══════════════════════════════════════════════════════════════

// A · HERO OVERLAY — full-bleed illustration, title sits ON the image.
// No border, no seam between picture and title. The lost one.
function FeedHero({ v = 'hills', lens = 'For the obsessed', title, hook }) {
  return (
    <div style={{ position: 'relative', borderRadius: 16, overflow: 'hidden', height: 230 }}>
      <Plate variant={v} style={{ position: 'absolute', inset: 0 }} dim={0.04}/>
      {/* single soft bottom scrim so type is legible — no card chrome */}
      <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.16) 0%, rgba(20,14,9,0) 34%, rgba(20,14,9,0) 50%, rgba(20,14,9,0.74) 100%)' }}/>
      <div style={{ position: 'absolute', top: 12, left: 12 }}><LensChip lens={lens} onDark/></div>
      <div style={{ position: 'absolute', left: 16, right: 16, bottom: 14 }}>
        <h3 style={{ fontFamily: T.serif, fontSize: 22, fontWeight: 500, letterSpacing: -0.4, lineHeight: 1.1, color: '#fff', margin: 0 }}>{title}</h3>
        {hook && <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: 'rgba(255,255,255,0.84)', lineHeight: 1.35, margin: '7px 0 0' }}>{hook}</p>}
        <div style={{ marginTop: 9 }}>
          <span style={{ display: 'inline-flex', alignItems: 'center', gap: 4, color: 'rgba(255,255,255,0.82)', fontSize: 12, fontWeight: 600 }}>
            <span style={{ fontSize: 14, marginRight: -1 }}>+</span> Vesper
          </span>
        </div>
      </div>
    </div>
  );
}

// B · CAPTIONED — full-bleed image, caption directly beneath on parchment,
// no card box around it. Borderless; the image edge is the only frame.
function FeedCaptioned({ v = 'coast', lens = 'A day in', title, hook }) {
  return (
    <div>
      <Plate variant={v} style={{ height: 150, borderRadius: 14 }} dim={0.03}>
        <div style={{ position: 'absolute', top: 10, left: 10 }}><LensChip lens={lens} onDark/></div>
      </Plate>
      <div style={{ padding: '11px 4px 0' }}>
        <h3 style={{ fontFamily: T.serif, fontSize: 18, fontWeight: 500, letterSpacing: -0.3, lineHeight: 1.15, color: T.ink, margin: 0 }}>{title}</h3>
        {hook && <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.mute, lineHeight: 1.35, margin: '5px 0 0' }}>{hook}</p>}
      </div>
    </div>
  );
}

// C · SPLIT — tall image left, editorial text right. Magazine column.
function FeedSplit({ v = 'alley', lens = 'Insider', title, hook, meta }) {
  return (
    <div style={{ display: 'flex', gap: 14, alignItems: 'stretch' }}>
      <Plate variant={v} style={{ width: 116, borderRadius: 12, flexShrink: 0, minHeight: 132 }}/>
      <div style={{ flex: 1, minWidth: 0, display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
        <FieldEyebrow>{lens.toUpperCase()}</FieldEyebrow>
        <h3 style={{ fontFamily: T.serif, fontSize: 18, fontWeight: 500, letterSpacing: -0.3, lineHeight: 1.15, color: T.ink, margin: '8px 0 0' }}>{title}</h3>
        {hook && <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.mute, lineHeight: 1.35, margin: '6px 0 0' }}>{hook}</p>}
        {meta && <span style={{ fontFamily: T.mono, fontSize: 8.5, color: T.muteSoft, letterSpacing: 1, marginTop: 9 }}>{meta}</span>}
      </div>
    </div>
  );
}

// D · QUOTE — a Vesper line as the object; the image is a thin band.
function FeedQuote({ v = 'square', quote, place }) {
  return (
    <div style={{ background: T.cardWarm, borderRadius: 14, border: `0.5px solid ${T.hairline}`, overflow: 'hidden' }}>
      <Plate variant={v} style={{ height: 8 }}/>
      <div style={{ padding: '14px 16px 14px', borderLeft: `2px solid ${D.vesper}` }}>
        <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 16, color: T.ink, lineHeight: 1.4, margin: 0, letterSpacing: -0.15 }}>“{quote}”</p>
        <div style={{ marginTop: 10, display: 'flex', alignItems: 'center', gap: 8 }}>
          <span style={{ display: 'inline-flex', alignItems: 'center', gap: 4, color: D.vesper, fontSize: 12, fontWeight: 600 }}><span style={{ fontSize: 14, marginRight: -1 }}>+</span> Vesper</span>
          <span style={{ fontSize: 10, color: T.muteSoft, letterSpacing: 1.2, fontWeight: 600 }}>· {place}</span>
        </div>
      </div>
    </div>
  );
}

// E · DUO — two slim portrait cards side by side. For "either/or" picks.
function FeedDuo({ items }) {
  return (
    <div style={{ display: 'flex', gap: 12 }}>
      {items.map((it, i) => (
        <div key={i} style={{ flex: 1, minWidth: 0 }}>
          <div style={{ position: 'relative', borderRadius: 12, overflow: 'hidden', height: 150 }}>
            <Plate variant={it.v} style={{ position: 'absolute', inset: 0 }} dim={0.06}/>
            <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0) 40%, rgba(20,14,9,0.7) 100%)' }}/>
            <div style={{ position: 'absolute', left: 11, right: 11, bottom: 11 }}>
              <div style={{ fontSize: 8.5, letterSpacing: 1.4, fontWeight: 700, color: 'rgba(255,255,255,0.78)' }}>{it.lens.toUpperCase()}</div>
              <div style={{ fontFamily: T.serif, fontSize: 14.5, fontWeight: 500, color: '#fff', letterSpacing: -0.2, lineHeight: 1.15, marginTop: 4 }}>{it.title}</div>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}

window.FeedHero = FeedHero;
window.FeedCaptioned = FeedCaptioned;
window.FeedSplit = FeedSplit;
window.FeedQuote = FeedQuote;
window.FeedDuo = FeedDuo;
