// ═══════════════════════════════════════════════════════════════
// VESPER · ONBOARDING — shared atoms. The concierge speaks first;
// every step collapses "giving data" and "getting value" into one
// moment. Reuses T, Phone, TabBar, VesperMark (design-system /
// vesper-shared) + PostcardScene (v3-shared).
// ═══════════════════════════════════════════════════════════════

const OB = { blue: '#3D5066', blueDeep: '#2A384B', soft: '#5C554D', faint: '#D4CFC8', hair: 'rgba(27,23,20,0.10)' };

// small-caps mono eyebrow
function EdKick({ children, c = T.mute }) {
  return <div style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 2.2, color: c, fontWeight: 600, textTransform: 'uppercase' }}>{children}</div>;
}

// the phone frame — content scrolls under a fixed status bar
function PFrame({ children, bg = T.bg, pad = 54 }) {
  return (
    <Phone bg={bg}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: pad, overflow: 'hidden' }}>{children}</div>
    </Phone>
  );
}

// THE VESPER VOICE ENVELOPE — prose on the page, never a bubble.
function Vesper({ kicker = 'VESPER', children, size = 17 }) {
  return (
    <div style={{ background: T.cardWarm, borderLeft: `2px solid ${T.gold}`, padding: '14px 16px 15px', borderRadius: '0 10px 10px 0' }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 9 }}>
        <VesperMark s={12}/>
        <span style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 2.4, color: T.goldDeep, fontWeight: 600 }}>{kicker}</span>
      </div>
      <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: size, color: T.ink, lineHeight: 1.5, letterSpacing: -0.1 }}>{children}</div>
    </div>
  );
}

// a soft paragraph break inside Vesper prose
function P({ children }) { return <p style={{ margin: '0 0 11px' }}>{children}</p>; }
function PLast({ children }) { return <p style={{ margin: 0 }}>{children}</p>; }

// chat top chrome — back · Vesper · 1:1 PRIVATE
function ChatTop({ tag = '1:1 · PRIVATE' }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '8px 18px 12px', borderBottom: `0.5px solid ${T.hairThin}` }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 6, width: 90 }}>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
        <span style={{ fontFamily: T.serif, fontSize: 15, color: T.ink, fontWeight: 500 }}>Vesper</span>
      </div>
      <span style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 2, color: T.goldDeep, fontWeight: 600 }}>{tag}</span>
      <span style={{ width: 90 }}/>
    </div>
  );
}

// the composer — serif-italic placeholder, gold send
function Composer({ placeholder, typed }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 10, padding: '4px 4px 4px 15px', background: T.cardSoft, borderRadius: 14, border: `0.5px solid ${T.hairline}` }}>
      <span style={{ flex: 1, fontFamily: T.serif, fontStyle: typed ? 'normal' : 'italic', fontSize: 15, color: typed ? T.ink : T.mute, letterSpacing: -0.1, whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
        {placeholder}{typed && <span style={{ display: 'inline-block', width: 1.5, height: 16, background: T.gold, marginLeft: 1, transform: 'translateY(3px)' }}/>}
      </span>
      <div style={{ width: 36, height: 36, borderRadius: 999, background: T.goldDeep, color: T.cardWarm, display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M5 12h13M12 5l7 7-7 7"/></svg>
      </div>
    </div>
  );
}

// a user reply pill (right-aligned dark serif)
function UserSaid({ children }) {
  return (
    <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
      <div style={{ maxWidth: 260, padding: '8px 14px', background: T.ink, color: T.cardWarm, borderRadius: 16, fontFamily: T.serif, fontSize: 14.5, lineHeight: 1.35, letterSpacing: -0.05 }}>{children}</div>
    </div>
  );
}

// an action row under a Vesper draft (hairline separated)
function ActionRow({ children, italic, c = T.ink, arrow = true, top }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '12px 2px', borderTop: top ? `0.5px solid ${T.hairline}` : 'none' }}>
      <span style={{ fontFamily: T.serif, fontStyle: italic ? 'italic' : 'normal', fontSize: 13.5, color: c, letterSpacing: -0.1 }}>{children}</span>
      {arrow && <span style={{ color: T.goldDeep, fontSize: 14 }}>→</span>}
    </div>
  );
}

// a safety / dietary chip
function Chip({ children, on }) {
  return (
    <span style={{ padding: '7px 13px', borderRadius: 999, fontFamily: T.serif, fontSize: 12.5, letterSpacing: -0.05, background: on ? T.cardWarm : T.cardSoft, border: `0.8px solid ${on ? T.gold : OB.hair}`, color: on ? T.goldDeep : T.ink }}>{children}</span>
  );
}

// a body scroll region inside PFrame (gap-stacked)
function Body({ children, gap = 14, pad = '18px 20px 0' }) {
  return <div style={{ padding: pad, display: 'flex', flexDirection: 'column', gap }}>{children}</div>;
}

Object.assign(window, { OB, EdKick, PFrame, Vesper, P, PLast, ChatTop, Composer, UserSaid, ActionRow, Chip, Body });
