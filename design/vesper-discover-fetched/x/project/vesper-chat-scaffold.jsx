// ═══════════════════════════════════════════════════════════════
// VESPER · CHAT — shared screen scaffold.
// The asymmetric grammar: Vesper = full-width serif prose w/ a
// + VESPER eyebrow (never a bubble); the user = a small dark serif
// pill. Paper/ink. Ochre = Vesper's voice · ink-blue (TR.ink) =
// planning / Open-in-Trips · oxblood (OX) = urgency only.
// Reuses T, Phone, TabBar (design-system); VesperMark, VesperEyebrow
// (vesper-shared); TR (trips-shared).
// ═══════════════════════════════════════════════════════════════

const OX = '#A04030';            // oxblood — urgency only
const hl = `0.5px solid ${T.hairline}`;
const hlT = `0.5px solid ${T.hairThin}`;

// ─── Header ─────────────────────────────────────────────────────
// variants: title + sub-eyebrow, optional draft badge, right slot.
function ChatHeader({ title = 'Tokyo, in May', sub = 'PRIVATE · TRIP-LINKED', draft, right = 'menu', members }) {
  const Dots = () => (
    <svg width="18" height="18" viewBox="0 0 24 24" fill={T.inkSoft}><circle cx="5" cy="12" r="1.5"/><circle cx="12" cy="12" r="1.5"/><circle cx="19" cy="12" r="1.5"/></svg>
  );
  return (
    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '12px 20px 11px', borderBottom: hlT }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 5, color: T.inkSoft, width: 70 }}>
        <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
        {!members && <span style={{ fontSize: 13, color: T.inkSoft, fontWeight: 500 }}>Vesper</span>}
      </div>
      <div style={{ textAlign: 'center', flex: 1 }}>
        <div style={{ fontFamily: T.serif, fontSize: 15.5, color: T.ink, fontWeight: 500, letterSpacing: -0.2, lineHeight: 1 }}>{title}</div>
        <div style={{ fontSize: 8.5, color: T.muteSoft, letterSpacing: 1.5, fontWeight: 700, marginTop: 3 }}>{sub}</div>
      </div>
      <div style={{ width: 70, display: 'flex', justifyContent: 'flex-end', alignItems: 'center', gap: 10 }}>
        {draft && <span style={{ padding: '3px 7px', border: `0.8px solid ${T.gold}`, borderRadius: 3, fontSize: 8.5, color: T.goldDeep, letterSpacing: 1.4, fontWeight: 700 }}>{draft}</span>}
        {right === 'menu' && <Dots/>}
        {right === 'members' && members}
      </div>
    </div>
  );
}

// Avatar stack for a group header.
function MemberStack({ who = ['tiger', 'ana', 'theo'], s = 23 }) {
  return (
    <div style={{ display: 'flex' }}>
      {who.map((w, i) => (
        <div key={w} style={{ marginLeft: i ? -8 : 0, borderRadius: 999, border: `1.5px solid ${T.bg}` }}><Avatar who={w} s={s}/></div>
      ))}
    </div>
  );
}

// ─── Day divider ────────────────────────────────────────────────
function DayDivider({ children = 'Yesterday' }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 10, color: T.mute, fontStyle: 'italic', fontFamily: T.serif, fontSize: 11.5, margin: '4px 0' }}>
      <span style={{ flex: 1, height: 1, background: T.hairline }}/>
      <span>{children}</span>
      <span style={{ flex: 1, height: 1, background: T.hairline }}/>
    </div>
  );
}

// ─── User pill (right-aligned dark serif) ───────────────────────
function UserPill({ children, time, optimistic, attach }) {
  return (
    <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
      <div style={{ maxWidth: 286, textAlign: 'right', opacity: optimistic ? 0.55 : 1 }}>
        {attach}
        <div style={{ padding: '8px 14px', background: T.ink, color: T.cardWarm, borderRadius: 18, fontFamily: T.serif, fontSize: 14.5, lineHeight: 1.35, display: 'inline-block', letterSpacing: -0.05 }}>{children}</div>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'flex-end', gap: 5, fontSize: 8.5, color: T.muteSoft, letterSpacing: 1.2, marginTop: 4, fontWeight: 600 }}>
          {optimistic && <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke={T.muteSoft} strokeWidth="2" strokeLinecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>}
          {optimistic ? 'SENDING' : time}
        </div>
      </div>
    </div>
  );
}

// ─── Vesper prose (the page voice) ──────────────────────────────
function VesperProse({ children, trailing, time, caret }) {
  return (
    <div>
      <VesperEyebrow trailing={trailing}/>
      <p style={{ fontFamily: T.serif, fontSize: 16, color: T.ink, lineHeight: 1.46, margin: '9px 0 0', letterSpacing: -0.1 }}>
        {children}
        {caret && <span style={{ display: 'inline-block', width: 2, height: 17, background: T.gold, marginLeft: 2, transform: 'translateY(3px)' }}/>}
      </p>
      {time && <div style={{ fontSize: 8.5, color: T.muteSoft, letterSpacing: 1.2, marginTop: 8, fontWeight: 600 }}>{time} · VESPER</div>}
    </div>
  );
}

// ─── Suggested-action chips (italic; first = ink-blue intent) ───
function SuggestChips({ items = ['add to Tokyo trip', 'show me ¥ tier', 'why these', 'something quieter'] }) {
  return (
    <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap' }}>
      {items.map((c, i) => (
        <span key={c} style={{ padding: '5px 11px', fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: i === 0 ? TR.ink : T.inkSoft, background: T.cardWarm, borderRadius: 999, border: i === 0 ? `0.8px solid ${TR.ink}` : `0.5px solid ${T.hairline}` }}>{c}</span>
      ))}
    </div>
  );
}

// ─── Composer (rest / typing / attachments / listening) ─────────
function ChatComposer({ state = 'rest', value, placeholder = 'Reply, or pick one above…', attachments = 0 }) {
  const typing = state === 'typing';
  return (
    <div>
      {attachments > 0 && (
        <div style={{ display: 'flex', gap: 7, marginBottom: 9, paddingLeft: 2 }}>
          {Array.from({ length: Math.min(attachments, 4) }).map((_, i) => (
            <div key={i} style={{ position: 'relative', width: 48, height: 48, borderRadius: 10, overflow: 'hidden', border: hl, background: i % 2 ? '#C9BBA6' : '#B7A98F' }}>
              <div style={{ position: 'absolute', inset: 0, background: i % 2 ? 'linear-gradient(135deg,#cdbfa6,#9c8a6f)' : 'linear-gradient(135deg,#bfae90,#8d7c5f)' }}/>
              <div style={{ position: 'absolute', top: 2, right: 2, width: 14, height: 14, borderRadius: 999, background: 'rgba(27,23,20,0.6)', color: '#fff', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: 9 }}>×</div>
            </div>
          ))}
        </div>
      )}
      <div style={{ display: 'flex', alignItems: 'center', gap: 10, padding: '4px 4px 4px 14px', background: T.cardWarm, borderRadius: 999, border: `0.5px solid ${typing ? T.goldSoft : T.hairline}`, boxShadow: '0 8px 22px -14px rgba(0,0,0,0.18), 0 1px 0 rgba(255,255,255,0.6) inset' }}>
        <span style={{ flexShrink: 0, color: T.inkSoft, display: 'flex' }}>
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="1.7" strokeLinecap="round"><path d="M12 5v14M5 12h14"/></svg>
        </span>
        <div style={{ flex: 1, fontFamily: T.serif, fontStyle: typing ? 'normal' : 'italic', fontSize: 15, color: typing ? T.ink : T.muteSoft, letterSpacing: -0.1, padding: '8px 0', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
          {typing ? value : placeholder}
          {typing && <span style={{ display: 'inline-block', width: 1.5, height: 16, background: T.gold, marginLeft: 1, transform: 'translateY(3px)' }}/>}
        </div>
        {typing
          ? <div style={{ width: 36, height: 36, borderRadius: 999, background: TR.ink, color: '#fff', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M5 12h13M12 5l7 7-7 7"/></svg></div>
          : <div style={{ width: 36, height: 36, borderRadius: 999, background: T.ink, color: T.cardWarm, display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0, boxShadow: '0 2px 6px rgba(0,0,0,0.2)' }}><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round"><rect x="9" y="3" width="6" height="12" rx="3"/><path d="M5 11c0 4 3 7 7 7s7-3 7-7M12 18v3M8 21h8"/></svg></div>}
      </div>
    </div>
  );
}

// ─── Screen scaffold: header · scroll body · composer · tab bar ─
function ChatScreen({ header, children, composer, fade = true, active = 'vesper' }) {
  return (
    <Phone bg={T.bg}>
      {header}
      <div style={{ position: 'absolute', top: 96, left: 0, right: 0, bottom: 150, overflow: 'hidden' }}>
        <div style={{ padding: '16px 20px 8px', display: 'flex', flexDirection: 'column', gap: 14 }}>{children}</div>
        {fade && <div style={{ position: 'absolute', bottom: 0, left: 0, right: 0, height: 26, background: `linear-gradient(to top, ${T.bg}, rgba(239,234,224,0))`, pointerEvents: 'none' }}/>}
      </div>
      {composer !== null && (
        <div style={{ position: 'absolute', bottom: 92, left: 16, right: 16 }}>{composer || <ChatComposer/>}</div>
      )}
      <TabBar active={active}/>
    </Phone>
  );
}

Object.assign(window, {
  OX, ChatHeader, MemberStack, DayDivider, UserPill, VesperProse,
  SuggestChips, ChatComposer, ChatScreen,
});
