// ─────────────────────────────────────────────────────────────
// VESPER CARD KIT
// Card-object primitives, the seven family kinds, the decision sheet,
// and loading/empty states. One language: paper objects, ochre voice.
// Reuses T (design-system), TR (trips-shared), VesperMark (vesper-shared).
// ─────────────────────────────────────────────────────────────

// Family metadata, keyed by interaction family (not backend kind).
// `accent` is the kind's colour (dot / glyph context); `vesper:true`
// means Vesper-authored → carries the ochre sparkle.
const FAM = {
  call:     { label: 'NEEDS YOUR CALL',  spine: TR.ink,    glyph: 'docket',  vesper: false },
  prepared: { label: 'VESPER PREPARED',  spine: T.gold,    glyph: 'brief',   vesper: true  },
  live:     { label: 'RIGHT NOW',        spine: '#3D5066', glyph: 'live',    vesper: false },
  signal:   { label: 'A PATTERN',        spine: '#7C8F73', glyph: 'signal',  vesper: true  },
  capture:  { label: 'WORTH KEEPING',    spine: T.gold,    glyph: 'capture', vesper: false },
  resume:   { label: 'PICK UP WHERE',    spine: T.mute,    glyph: 'resume',  vesper: false },
  starter:  { label: 'BEGIN',            spine: T.goldDeep,glyph: 'starter', vesper: false },
};

// ─── Kind glyphs — small line-art that signals the card's job ──
const CardGlyph = {
  docket: ({ s = 20, c = T.ink }) => (
    <svg width={s} height={s} viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.4" strokeLinecap="round" strokeLinejoin="round">
      <rect x="5" y="3.5" width="14" height="17" rx="2"/>
      <path d="M9 3.5V6h6V3.5M9 11l2 2 4-4M9 16h6"/>
    </svg>
  ),
  brief: ({ s = 20, c = T.ink }) => (
    <svg width={s} height={s} viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.4" strokeLinecap="round" strokeLinejoin="round">
      <path d="M7 3h7l4 4v14H7z M14 3v4h4"/>
      <path d="M10 12h5M10 15h5" opacity="0.6"/>
    </svg>
  ),
  live: ({ s = 20, c = T.ink }) => (
    <svg width={s} height={s} viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.4" strokeLinecap="round">
      <circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>
    </svg>
  ),
  signal: ({ s = 20, c = T.ink }) => (
    <svg width={s} height={s} viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.3">
      <ellipse cx="12" cy="12" rx="4" ry="6"/>
      <ellipse cx="12" cy="12" rx="7.5" ry="9.5" opacity="0.55"/>
    </svg>
  ),
  capture: ({ s = 20, c = T.ink }) => (
    <svg width={s} height={s} viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.4" strokeLinecap="round" strokeLinejoin="round">
      <rect x="3.5" y="6" width="17" height="13" rx="2"/>
      <path d="M8 6l1.6-2.5h4.8L16 6"/><circle cx="12" cy="12.5" r="3.2"/>
    </svg>
  ),
  resume: ({ s = 20, c = T.ink }) => (
    <svg width={s} height={s} viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.4" strokeLinecap="round" strokeLinejoin="round">
      <path d="M7 3.5h10v17l-5-3.5L7 20.5z"/>
    </svg>
  ),
  starter: ({ s = 20, c = T.ink }) => (
    <svg width={s} height={s} viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.4" strokeLinecap="round">
      <path d="M12 5v14M5 12h14"/>
    </svg>
  ),
};

// ─── KIND TAG — coloured dot + label. Vesper-authored gets the mark ──
function KindTag({ fam, children }) {
  const m = FAM[fam];
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
      {m.vesper
        ? <VesperMark s={11} c={T.gold}/>
        : <span style={{ width: 5, height: 5, borderRadius: 5, background: m.spine }}/>}
      <span style={{
        fontSize: 9, letterSpacing: 1.5, fontWeight: 700,
        color: m.vesper ? T.goldDeep : m.spine,
      }}>
        {children || m.label}
      </span>
    </div>
  );
}

// ─── CARD SHELL — a paper object. ──
function CardShell({ fam, children, dashed, tint, style }) {
  const m = FAM[fam] || {};
  return (
    <div style={{
      position: 'relative',
      background: tint || T.cardWarm,
      borderRadius: 14,
      border: dashed ? `1px dashed ${m.spine || T.muteSoft}` : `0.5px solid ${T.hairline}`,
      boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset, 0 8px 22px -16px rgba(0,0,0,0.16)',
      overflow: 'hidden',
      ...style,
    }}>
      {children}
    </div>
  );
}

// ─── ACTION ROW — one primary, up to two quiet secondaries ──
function ActionRow({ primary, primaryColor = TR.ink, secondary = [], onMore }) {
  return (
    <div style={{
      display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: 8,
    }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
        {secondary.map((s, i) => (
          <span key={i} style={{
            fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5,
            color: i === 0 ? T.inkSoft : T.muteSoft, letterSpacing: -0.05,
          }}>{s}</span>
        ))}
      </div>
      {primary && (
        <span style={{
          padding: '7px 14px', background: primaryColor, color: T.cardWarm,
          borderRadius: 999, fontSize: 12, fontWeight: 600, letterSpacing: -0.1,
          display: 'inline-flex', alignItems: 'center', gap: 5, whiteSpace: 'nowrap',
        }}>
          {primary} <span style={{ opacity: 0.8 }}>→</span>
        </span>
      )}
    </div>
  );
}

// ─── WHY-THIS chip — one-tap explanation affordance ──
function WhyThis({ label = 'Why this' }) {
  const c = T.goldDeep;
  return (
    <span style={{
      display: 'inline-flex', alignItems: 'center', gap: 4,
      fontSize: 10, letterSpacing: 0.3, fontWeight: 600, color: c,
      padding: '3px 8px', borderRadius: 999,
      border: `0.6px solid rgba(176,133,58,0.4)`,
    }}>
      <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="2" strokeLinecap="round">
        <path d="M9 9c0-2 1.5-3 3-3s3 1 3 3-3 2-3 4M12 17.5v.5"/>
      </svg>
      {label}
    </span>
  );
}

// ─── LOADING / EMPTY ────────────────────────────────────────────
function CardLoading({ fam }) {
  const m = FAM[fam] || {};
  return (
    <CardShell fam={fam} style={{ padding: 16 }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 12 }}>
        <span style={{ width: 5, height: 5, borderRadius: 5, background: m.spine, opacity: 0.4 }}/>
        <Bar w={92} h={8}/>
      </div>
      <Bar w={210} h={16} mb={8}/>
      <Bar w={150} h={11} mb={16}/>
      <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
        <Bar w={96} h={28} r={999}/>
      </div>
    </CardShell>
  );
}
function Bar({ w, h, mb = 0, r = 4 }) {
  return <div style={{
    width: w, height: h, marginBottom: mb, borderRadius: r,
    background: 'linear-gradient(90deg, rgba(27,23,20,0.06), rgba(27,23,20,0.10), rgba(27,23,20,0.06))',
  }}/>;
}

function CardEmpty({ title, sub }) {
  return (
    <CardShell fam="starter" dashed style={{ padding: 18, textAlign: 'center' }}>
      <div style={{ display: 'flex', justifyContent: 'center', marginBottom: 8, opacity: 0.5 }}>
        <CardGlyph.starter s={18} c={T.goldDeep}/>
      </div>
      <div style={{ fontFamily: T.serif, fontSize: 15, color: T.ink, fontWeight: 500, letterSpacing: -0.2 }}>{title}</div>
      <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.mute, marginTop: 4 }}>{sub}</div>
    </CardShell>
  );
}

// ─── DECISION SHEET ─────────────────────────────────────────────
// Opened by cards that need deliberation. Six fixed zones.
function DecisionSheet() {
  const vc = T.gold;
  const vcDeep = T.goldDeep;
  return (
    <div style={{
      width: 393, background: T.bg, borderRadius: 28, overflow: 'hidden',
      fontFamily: T.sans, color: T.ink,
      boxShadow: '0 -10px 40px -12px rgba(0,0,0,0.25)',
      border: `0.5px solid ${T.hairline}`,
    }}>
      {/* grabber */}
      <div style={{ display: 'flex', justifyContent: 'center', paddingTop: 10 }}>
        <div style={{ width: 36, height: 4, borderRadius: 4, background: T.muteSoft, opacity: 0.5 }}/>
      </div>

      {/* header — the card this sheet belongs to */}
      <div style={{ padding: '14px 22px 0' }}>
        <KindTag fam="call"/>
        <h2 style={{
          fontFamily: T.serif, fontWeight: 500, fontSize: 24, color: T.ink,
          margin: '8px 0 0', letterSpacing: -0.4, lineHeight: 1.1,
        }}>
          A ryokan for Tokyo, <span style={{ fontStyle: 'italic' }}>nights 5–7.</span>
        </h2>
      </div>

      {/* I noticed */}
      <SheetZone eyebrow="I NOTICED" vc={vc}>
        <p style={{ margin: 0, fontFamily: T.serif, fontSize: 14.5, color: T.inkSoft, lineHeight: 1.45, letterSpacing: -0.05 }}>
          You keep saving quiet alleys over big hotels, and you star morning light in your photos.
        </p>
      </SheetZone>

      {/* My read */}
      <SheetZone eyebrow="MY READ" vc={vc}>
        <p style={{ margin: 0, fontFamily: T.serif, fontStyle: 'italic', fontSize: 14.5, color: T.ink, lineHeight: 1.45, letterSpacing: -0.05 }}>
          Sawanoya in Yanaka is the one I’d book — slowest of the three, and it fits the week you’re building.
        </p>
      </SheetZone>

      {/* Best next step — the primary */}
      <div style={{ padding: '16px 22px 0' }}>
        <div style={{ fontSize: 9.5, letterSpacing: 1.8, fontWeight: 700, color: vcDeep, marginBottom: 8 }}>
          BEST NEXT STEP
        </div>
        <div style={{
          display: 'flex', alignItems: 'center', justifyContent: 'space-between',
          padding: '12px 14px', background: T.cardWarm, borderRadius: 12,
          border: `0.8px solid ${TR.ink}`,
        }}>
          <div>
            <div style={{ fontFamily: T.serif, fontSize: 15, fontWeight: 500, color: T.ink, letterSpacing: -0.2 }}>
              Hold Sawanoya, nights 5–7
            </div>
            <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 11.5, color: T.mute, marginTop: 2 }}>
              free to cancel · I’ll add it to Tokyo
            </div>
          </div>
          <span style={{
            padding: '8px 14px', background: TR.ink, color: T.cardWarm, borderRadius: 999,
            fontSize: 12, fontWeight: 600, letterSpacing: -0.1, whiteSpace: 'nowrap',
          }}>Do it →</span>
        </div>
      </div>

      {/* secondary controls — Ask / Tune / Not now */}
      <div style={{ padding: '14px 22px 22px', display: 'flex', gap: 8 }}>
        {[
          { t: 'Ask Vesper', sub: 'why these three' },
          { t: 'Tune', sub: 'budget, area' },
          { t: 'Not now', sub: 'remind later' },
        ].map((b, i) => (
          <div key={i} style={{
            flex: 1, padding: '10px 10px', background: T.cardWarm, borderRadius: 10,
            border: `0.5px solid ${T.hairline}`, textAlign: 'center',
          }}>
            <div style={{ fontFamily: T.serif, fontSize: 13, fontWeight: 500, color: T.ink, letterSpacing: -0.1 }}>{b.t}</div>
            <div style={{ fontSize: 9.5, color: T.muteSoft, fontStyle: 'italic', fontFamily: T.serif, marginTop: 2 }}>{b.sub}</div>
          </div>
        ))}
      </div>
    </div>
  );
}

function SheetZone({ eyebrow, vc, children }) {
  return (
    <div style={{ padding: '16px 22px 0' }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 8 }}>
        <span style={{ width: 14, height: 1.5, background: vc, borderRadius: 2 }}/>
        <span style={{ fontSize: 9.5, letterSpacing: 1.8, fontWeight: 700, color: T.mute }}>{eyebrow}</span>
      </div>
      {children}
    </div>
  );
}

Object.assign(window, {
  FAM, CardGlyph, KindTag, CardShell, ActionRow, WhyThis,
  CardLoading, CardEmpty, DecisionSheet,
});
