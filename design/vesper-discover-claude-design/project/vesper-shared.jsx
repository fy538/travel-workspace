// Vesper-tab shared atoms.
// Vesper's voice = ochre (continues from Atlas/Trips). Ink-blue stays for
// "open this" actions. Purple/indigo from current screens is removed.

const VES = {
  // Vesper's signature lavender-ink (kept very dilute — only used as a hint
  // behind the Vesper sparkle and on the "I noticed" panels). Not as a
  // primary brand color.
  hint:      'rgba(176,133,58,0.08)',
  hintDeep:  'rgba(176,133,58,0.18)',
};

// ─── Vesper sparkle mark ────────────────────────────────────────
function VesperMark({ s = 14, c = T.gold }) {
  return (
    <svg width={s} height={s} viewBox="0 0 24 24" fill={c}>
      <path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z" opacity="1"/>
      <path d="M19 16 L19.6 18.4 L22 19 L19.6 19.6 L19 22 L18.4 19.6 L16 19 L18.4 18.4 Z" opacity="0.85"/>
    </svg>
  );
}

// ─── + VESPER eyebrow (used above Vesper's prose) ───────────────
function VesperEyebrow({ trailing }) {
  return (
    <div style={{
      display: 'flex', alignItems: 'center', gap: 10,
      fontSize: 10.5, color: T.goldDeep, letterSpacing: 1.8, fontWeight: 700,
    }}>
      <span style={{ display: 'inline-flex', alignItems: 'center', gap: 4 }}>
        <span style={{ color: T.gold, marginRight: -2 }}>+</span> VESPER
      </span>
      {trailing && (
        <>
          <span style={{ flex: 1, height: 1, background: 'rgba(176,133,58,0.30)' }}/>
          <span style={{ color: T.mute, fontSize: 10, letterSpacing: 1.6, fontWeight: 600 }}>
            {trailing}
          </span>
        </>
      )}
    </div>
  );
}

// ─── Vesper top bar (used by all home + chat) ───────────────────
function VesperTopBar({ ctx, history = true }) {
  return (
    <div style={{
      display: 'flex', alignItems: 'center', justifyContent: 'space-between',
      padding: '14px 22px 0',
    }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 6, fontSize: 10.5, color: T.mute, letterSpacing: 1.8, fontWeight: 600 }}>
        {ctx}
      </div>
      <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
        {history && (
          <div style={{
            width: 30, height: 30, borderRadius: 999, border: `0.5px solid ${T.hairline}`,
            background: T.cardWarm, display: 'flex', alignItems: 'center', justifyContent: 'center',
          }}>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="1.5" strokeLinecap="round">
              <circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/>
            </svg>
          </div>
        )}
      </div>
    </div>
  );
}

// ─── Composer pill (text + voice) ───────────────────────────────
function Composer({ placeholder = 'Ask Vesper…', voice = true, prominent }) {
  return (
    <div style={{
      display: 'flex', alignItems: 'center', gap: 10,
      padding: prominent ? '4px 4px 4px 14px' : '4px 4px 4px 12px',
      background: T.cardWarm, borderRadius: 999,
      border: `0.5px solid ${T.hairline}`,
      boxShadow: prominent
        ? '0 8px 22px -14px rgba(0,0,0,0.18), 0 1px 0 rgba(255,255,255,0.6) inset'
        : '0 1px 0 rgba(255,255,255,0.6) inset',
    }}>
      <div style={{ flexShrink: 0, color: T.inkSoft }}>
        <Marks.Plus s={16} c={T.inkSoft}/>
      </div>
      <div style={{
        flex: 1, fontFamily: T.serif, fontStyle: 'italic',
        fontSize: prominent ? 16 : 14, color: T.muteSoft,
        letterSpacing: -0.1, padding: '8px 0',
      }}>{placeholder}</div>
      {voice && (
        <div style={{
          width: prominent ? 44 : 34, height: prominent ? 44 : 34, borderRadius: 999,
          background: T.ink, color: T.cardWarm,
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          boxShadow: '0 2px 6px rgba(0,0,0,0.2)',
        }}>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round">
            <rect x="9" y="3" width="6" height="12" rx="3"/>
            <path d="M5 11c0 4 3 7 7 7s7-3 7-7M12 18v3M8 21h8"/>
          </svg>
        </div>
      )}
    </div>
  );
}

// ─── Pull-quote / Vesper note style ─────────────────────────────
function VesperQuote({ children, attribution }) {
  return (
    <div style={{
      padding: '14px 16px', background: T.cardSoft, borderRadius: 14,
      borderLeft: `2px solid ${T.gold}`,
    }}>
      <p style={{
        fontFamily: T.serif, fontStyle: 'italic', fontSize: 16, color: T.inkSoft,
        margin: 0, lineHeight: 1.35, letterSpacing: -0.05,
      }}>
        {children}
      </p>
      {attribution && (
        <div style={{ marginTop: 8, fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.6, fontWeight: 600 }}>
          {attribution}
        </div>
      )}
    </div>
  );
}

// ─── Tiny "card type" tokens — used across the home directions ──
const CardTypes = {
  Action:   { color: TR.ink,     label: 'NEEDS YOU'    },
  Draft:    { color: T.goldDeep, label: 'DRAFT'        },
  Signal:   { color: TR.dreaming || '#7C8F73', label: 'NOTICED' },
  Memory:   { color: T.gold,     label: 'COULD KEEP'   },
  Alert:    { color: '#A55747',  label: 'TIME-SENSITIVE'},
  Continue: { color: T.mute,     label: 'CONTINUE'     },
};

Object.assign(window, { VES, VesperMark, VesperEyebrow, VesperTopBar, Composer, VesperQuote, CardTypes });
