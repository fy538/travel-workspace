// ─────────────────────────────────────────────────────────────
// CHAT-CARD KIT — distinct from Vesper Home cards.
// Home cards = proactive work objects. Chat cards = conversation
// artifacts produced inside a thread.
//
// Two contexts, switched by `ctx`:
//   'solo'  — 1:1 Vesper. Vesper writes ON THE PAGE. No bubble; a
//             + VESPER note, then the card full-width beneath it.
//   'group' — explicit bubbles, sender attribution, public cards,
//             privacy-softened fields.
//
// Reuses T (design-system), TR (trips-shared), VesperMark / VesperEyebrow
// (vesper-shared), PostcardScene (v3-shared).
// ─────────────────────────────────────────────────────────────

// People in the group demo.
const PEOPLE = {
  vesper: { name: 'Vesper', vesper: true,  color: T.gold },
  tiger:  { name: 'You',    initials: 'T', color: TR.ink },
  ana:    { name: 'Ana',    initials: 'A', color: '#7C8F73' },
  theo:   { name: 'Theo',   initials: 'T', color: '#A0703A' },
};

// A chat viewport slice — a 360-wide column on paper.
function ChatCol({ children, label }) {
  return (
    <div style={{ width: 360 }}>
      {label && (
        <div style={{
          fontSize: 9.5, letterSpacing: 1.8, color: T.muteSoft, fontWeight: 700,
          marginBottom: 10, textAlign: 'center',
        }}>{label}</div>
      )}
      <div style={{
        background: T.bg, borderRadius: 22, padding: '20px 16px',
        border: `0.5px solid ${T.hairline}`,
        display: 'flex', flexDirection: 'column', gap: 12,
      }}>
        {children}
      </div>
    </div>
  );
}

// Avatar — Vesper sparkle, or a person's monogram.
function Avatar({ who, s = 26 }) {
  const p = PEOPLE[who] || PEOPLE.vesper;
  if (p.vesper) {
    return (
      <div style={{
        width: s, height: s, borderRadius: 999, background: 'rgba(176,133,58,0.14)',
        display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0,
      }}>
        <VesperMark s={s * 0.55} c={T.gold}/>
      </div>
    );
  }
  return (
    <div style={{
      width: s, height: s, borderRadius: 999, background: p.color, color: T.cardWarm,
      display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0,
      fontFamily: T.serif, fontSize: s * 0.42, fontWeight: 500,
    }}>{p.initials}</div>
  );
}

// SOLO intro — Vesper writing on the page, above a card.
function VesperSays({ children, trailing }) {
  return (
    <div>
      <VesperEyebrow trailing={trailing}/>
      {children && (
        <p style={{
          fontFamily: T.serif, fontSize: 15.5, color: T.ink, margin: '8px 0 0',
          lineHeight: 1.4, letterSpacing: -0.1,
        }}>{children}</p>
      )}
    </div>
  );
}

// GROUP turn — avatar + name + time, then content (bubble or card).
function GroupTurn({ who = 'vesper', time = '10:14', children, bubble }) {
  const p = PEOPLE[who] || PEOPLE.vesper;
  return (
    <div style={{ display: 'flex', gap: 8, alignItems: 'flex-start' }}>
      <Avatar who={who}/>
      <div style={{ flex: 1, minWidth: 0 }}>
        <div style={{ display: 'flex', alignItems: 'baseline', gap: 8, marginBottom: 5 }}>
          <span style={{ fontSize: 12, fontWeight: 600, color: p.vesper ? T.goldDeep : T.ink, letterSpacing: -0.1 }}>
            {p.name}
          </span>
          <span style={{ fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1 }}>{time}</span>
        </div>
        {bubble ? (
          <div style={{
            background: T.cardWarm, borderRadius: '4px 14px 14px 14px', padding: '12px 14px',
            border: `0.5px solid ${T.hairline}`,
          }}>{children}</div>
        ) : children}
      </div>
    </div>
  );
}

// A group user's short bubble (text only).
function UserBubble({ who, time, children }) {
  const p = PEOPLE[who];
  return (
    <div style={{ display: 'flex', gap: 8, alignItems: 'flex-start' }}>
      <Avatar who={who}/>
      <div style={{ flex: 1 }}>
        <div style={{ display: 'flex', alignItems: 'baseline', gap: 8, marginBottom: 5 }}>
          <span style={{ fontSize: 12, fontWeight: 600, color: T.ink }}>{p.name}</span>
          <span style={{ fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1 }}>{time}</span>
        </div>
        <div style={{
          display: 'inline-block', background: 'rgba(27,23,20,0.05)', borderRadius: '4px 14px 14px 14px',
          padding: '8px 12px', fontFamily: T.serif, fontSize: 13.5, color: T.inkSoft, lineHeight: 1.35,
        }}>{children}</div>
      </div>
    </div>
  );
}

// THE CHAT CARD — a full-width paper object. No coloured spine.
function ChatCard({ children, style, dashed, tint }) {
  return (
    <div style={{
      background: tint || T.cardWarm, borderRadius: 14,
      border: dashed ? `1px dashed ${T.muteSoft}` : `0.5px solid ${T.hairline}`,
      boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset, 0 10px 24px -18px rgba(0,0,0,0.18)',
      overflow: 'hidden', ...style,
    }}>{children}</div>
  );
}

// A card header: glyph + eyebrow + optional right meta.
function CardHead({ glyph, kind, vesper, right, mb = 10 }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: mb }}>
      {vesper ? <VesperMark s={12} c={T.gold}/> : glyph}
      <span style={{ fontSize: 9, letterSpacing: 1.5, fontWeight: 700, color: vesper ? T.goldDeep : T.mute }}>
        {kind}
      </span>
      {right && <span style={{ marginLeft: 'auto', fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1.1, fontWeight: 600 }}>{right}</span>}
    </div>
  );
}

// Action bar — adapts to context. Solo = typographic + one pill.
// Group = filled/outlined buttons (more explicit, public).
function ChatActions({ ctx = 'solo', primary, primaryColor = TR.ink, secondary = [] }) {
  if (ctx === 'group') {
    return (
      <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap' }}>
        {primary && (
          <span style={{
            padding: '8px 14px', background: primaryColor, color: T.cardWarm, borderRadius: 999,
            fontSize: 12, fontWeight: 600, letterSpacing: -0.05,
          }}>{primary}</span>
        )}
        {secondary.map((s, i) => (
          <span key={i} style={{
            padding: '8px 12px', background: T.cardWarm, color: T.inkSoft,
            border: `0.5px solid ${T.hairline}`, borderRadius: 999, fontSize: 12, fontWeight: 500,
          }}>{s}</span>
        ))}
      </div>
    );
  }
  return (
    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: 8 }}>
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
          padding: '7px 14px', background: primaryColor, color: T.cardWarm, borderRadius: 999,
          fontSize: 12, fontWeight: 600, letterSpacing: -0.05, display: 'inline-flex', alignItems: 'center', gap: 5,
        }}>{primary} <span style={{ opacity: 0.8 }}>→</span></span>
      )}
    </div>
  );
}

// Meta chips — mono, for facts (hours, price tier, distance).
function MetaChips({ items }) {
  return (
    <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap' }}>
      {items.map((m, i) => (
        <span key={i} style={{
          padding: '3px 8px', fontFamily: T.mono, fontSize: 8.5, color: T.mute,
          letterSpacing: 1.1, fontWeight: 600, background: T.bg,
          border: `0.5px solid ${T.hairline}`, borderRadius: 999,
        }}>{m}</span>
      ))}
    </div>
  );
}

// Privacy tag — marks a softened/hidden field in group.
function PrivacyTag({ children = 'private' }) {
  return (
    <span style={{
      display: 'inline-flex', alignItems: 'center', gap: 4,
      fontSize: 8.5, letterSpacing: 1.2, fontWeight: 700, color: T.muteSoft,
    }}>
      <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke={T.muteSoft} strokeWidth="2" strokeLinecap="round">
        <rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>
      </svg>
      {children}
    </span>
  );
}

// Small line-art glyphs for chat-card kinds.
const ChatGlyph = {
  pin: (c = T.ink) => <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><path d="M12 3c-4 0-7 3-7 7 0 5 7 11 7 11s7-6 7-11c0-4-3-7-7-7Z"/><circle cx="12" cy="10" r="2.4"/></svg>,
  cal: (c = T.ink) => <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.5" strokeLinecap="round"><rect x="3.5" y="5" width="17" height="15" rx="2"/><path d="M3.5 10h17M8 3v4M16 3v4"/></svg>,
  route: (c = T.ink) => <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><circle cx="6" cy="6" r="2.5"/><circle cx="18" cy="18" r="2.5"/><path d="M6 8.5v4a4 4 0 0 0 4 4h4"/></svg>,
  scale: (c = T.ink) => <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.5" strokeLinecap="round"><path d="M12 4v16M5 8h14M5 8l-2.5 5h5zM19 8l-2.5 5h5z"/></svg>,
  vote: (c = T.ink) => <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><path d="M9 12l2 2 4-5"/><rect x="4" y="4" width="16" height="16" rx="3"/></svg>,
  card: (c = T.ink) => <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.5" strokeLinecap="round"><rect x="3" y="6" width="18" height="12" rx="2"/><path d="M3 10h18"/></svg>,
  check: (c = T.ink) => <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="9"/><path d="M8 12l3 3 5-6"/></svg>,
  diff: (c = T.ink) => <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.5" strokeLinecap="round"><path d="M12 5v14M5 8l-2.5 4L5 16M19 8l2.5 4L19 16"/></svg>,
  why: (c = T.ink) => <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.7" strokeLinecap="round"><path d="M9 9c0-2 1.5-3 3-3s3 1 3 3-3 2-3 4M12 17.5v.5"/></svg>,
  wave: (c = T.ink) => <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.5" strokeLinecap="round"><path d="M4 12h2M8 8v8M12 5v14M16 9v6M20 12h-1"/></svg>,
  guide: (c = T.ink) => <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><path d="M4 5h16v12H7l-3 3z"/><path d="M8 10h8M8 13h5"/></svg>,
  postcard: (c = T.ink) => <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><rect x="3" y="6" width="18" height="13" rx="1.5"/><path d="M3 11q5-3 9 0t9 0"/></svg>,
  research: (c = T.ink) => <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.5" strokeLinecap="round"><circle cx="11" cy="11" r="6.5"/><path d="M16 16l4 4"/></svg>,
  lock: (c = T.ink) => <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.5" strokeLinecap="round"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>,
  alert: (c = T.ink) => <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.6" strokeLinecap="round"><path d="M12 8v5M12 16v.5"/><circle cx="12" cy="12" r="9"/></svg>,
};

Object.assign(window, {
  PEOPLE, ChatCol, Avatar, VesperSays, GroupTurn, UserBubble,
  ChatCard, CardHead, ChatActions, MetaChips, PrivacyTag, ChatGlyph,
});
