// Two Vesper voice mode layouts.
//   1 · Calm Listening      — quiet ambient surface, one sparkle, one transcript line
//   2 · Editorial Transcript — voice IS a typed transcript appearing live

// ─── 1 · CALM LISTENING ─────────────────────────────────────────
function VesperVoiceCalm() {
  return (
    <Phone bg={T.bg}>
      {/* Top — close + state pill */}
      <div style={{
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        padding: '14px 22px 0',
      }}>
        <div style={{
          width: 30, height: 30, borderRadius: 999, border: `0.5px solid ${T.hairline}`,
          background: T.cardWarm,
          display: 'flex', alignItems: 'center', justifyContent: 'center',
        }}>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="1.6" strokeLinecap="round">
            <path d="M6 6l12 12M18 6L6 18"/>
          </svg>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 6, color: T.goldDeep, fontSize: 10.5, letterSpacing: 1.8, fontWeight: 700 }}>
          <span style={{
            width: 6, height: 6, borderRadius: 6, background: T.gold,
            boxShadow: `0 0 0 4px rgba(176,133,58,0.18)`,
          }}/>
          VESPER · LISTENING
        </div>
        <div style={{
          width: 30, height: 30, borderRadius: 999, border: `0.5px solid ${T.hairline}`,
          background: T.cardWarm,
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          fontSize: 11, color: T.inkSoft, letterSpacing: -0.1, fontWeight: 500,
        }}>
          ⇨
        </div>
      </div>

      {/* The mark — large sparkle with quiet halo */}
      <div style={{
        padding: '60px 0 0', display: 'flex', flexDirection: 'column',
        alignItems: 'center', position: 'relative',
      }}>
        {/* concentric ambient rings */}
        <svg width="240" height="240" viewBox="0 0 240 240" style={{ position: 'absolute', top: 30 }}>
          <circle cx="120" cy="120" r="116" fill="none" stroke={T.gold} strokeWidth="0.4" opacity="0.15"/>
          <circle cx="120" cy="120" r="90"  fill="none" stroke={T.gold} strokeWidth="0.5" opacity="0.22"/>
          <circle cx="120" cy="120" r="62"  fill="none" stroke={T.gold} strokeWidth="0.6" opacity="0.30"/>
          <circle cx="120" cy="120" r="36"  fill="none" stroke={T.gold} strokeWidth="0.7" opacity="0.45"/>
        </svg>
        <div style={{
          width: 56, height: 56, borderRadius: 999, background: T.cardWarm,
          border: `0.8px solid rgba(176,133,58,0.4)`,
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          marginTop: 92,
          boxShadow: '0 8px 22px -10px rgba(176,133,58,0.4), 0 1px 0 rgba(255,255,255,0.6) inset',
        }}>
          <VesperMark s={28}/>
        </div>
      </div>

      {/* Live transcript */}
      <div style={{ padding: '36px 26px 0' }}>
        <div style={{ fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.6, fontWeight: 600, textAlign: 'center' }}>
          I’M HEARING
        </div>
        <p style={{
          fontFamily: T.serif, fontStyle: 'italic', fontSize: 22, color: T.ink,
          margin: '12px 0 0', lineHeight: 1.3, letterSpacing: -0.3, textAlign: 'center',
        }}>
          “find me a ryokan that feels like Yanaka, but quieter, for nights five
          through<span style={{ color: T.muteSoft }}>—</span>”
          <span style={{
            display: 'inline-block', width: 2, height: 18, background: T.gold,
            verticalAlign: 'text-bottom', marginLeft: 2, opacity: 0.7,
          }}/>
        </p>
      </div>

      {/* Mic control row */}
      <div style={{
        position: 'absolute', bottom: 36, left: 0, right: 0,
        display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 22,
      }}>
        {/* tap to pause */}
        <div style={{
          width: 48, height: 48, borderRadius: 999, background: T.cardWarm,
          border: `0.5px solid ${T.hairline}`,
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          color: T.inkSoft, fontSize: 13,
        }}>
          <svg width="14" height="14" viewBox="0 0 24 24" fill={T.inkSoft}>
            <rect x="6" y="5" width="4" height="14" rx="1"/><rect x="14" y="5" width="4" height="14" rx="1"/>
          </svg>
        </div>
        {/* mic — large */}
        <div style={{
          width: 78, height: 78, borderRadius: 999, background: T.ink,
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          boxShadow: '0 12px 28px -10px rgba(0,0,0,0.4)',
          position: 'relative',
        }}>
          {/* breath ring */}
          <div style={{
            position: 'absolute', inset: -10, borderRadius: 999,
            border: `1px solid rgba(176,133,58,0.35)`,
          }}/>
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke={T.cardWarm} strokeWidth="1.6" strokeLinecap="round">
            <rect x="9" y="3" width="6" height="12" rx="3"/>
            <path d="M5 11c0 4 3 7 7 7s7-3 7-7M12 18v3M8 21h8"/>
          </svg>
        </div>
        {/* switch to walk-through mode */}
        <div style={{
          width: 48, height: 48, borderRadius: 999, background: T.cardWarm,
          border: `0.5px solid ${T.hairline}`,
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          color: T.inkSoft,
        }}>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="1.5" strokeLinecap="round">
            <path d="M8 4h8M8 20h8M12 4v16"/>
          </svg>
        </div>
      </div>
      <div style={{
        position: 'absolute', bottom: 16, left: 0, right: 0, textAlign: 'center',
        fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.6, fontWeight: 600,
      }}>
        TAP TO PAUSE · WALK ME THROUGH
      </div>
    </Phone>
  );
}

// ─── 2 · EDITORIAL TRANSCRIPT ───────────────────────────────────
// The whole screen becomes a typed transcript. State pill at top, mic at bottom.
function VesperVoiceTranscript() {
  return (
    <Phone bg={T.bg}>
      {/* Top — state pill */}
      <div style={{
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        padding: '14px 22px 0',
      }}>
        <div style={{
          width: 30, height: 30, borderRadius: 999, border: `0.5px solid ${T.hairline}`,
          background: T.cardWarm,
          display: 'flex', alignItems: 'center', justifyContent: 'center',
        }}>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="1.6" strokeLinecap="round">
            <path d="M6 6l12 12M18 6L6 18"/>
          </svg>
        </div>
        <div style={{
          display: 'flex', alignItems: 'center', gap: 6,
          padding: '5px 12px', borderRadius: 999, background: T.cardWarm,
          border: `0.5px solid ${T.hairline}`,
          color: T.goldDeep, fontSize: 10, letterSpacing: 1.8, fontWeight: 700,
        }}>
          <span style={{ width: 6, height: 6, borderRadius: 6, background: T.gold,
            boxShadow: `0 0 0 3px rgba(176,133,58,0.20)` }}/>
          VESPER · THINKING
        </div>
        <div style={{ width: 30 }}/>
      </div>

      {/* Transcript scroll */}
      <div style={{ padding: '24px 22px 0' }}>
        {/* USER 1 */}
        <div style={{ marginBottom: 18 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 6, color: T.mute, fontSize: 9, letterSpacing: 1.6, fontWeight: 700, marginBottom: 6 }}>
            <div style={{ width: 14, height: 14, borderRadius: 999, background: T.ink, color: T.cardWarm,
              fontFamily: T.serif, fontSize: 8, fontWeight: 600,
              display: 'flex', alignItems: 'center', justifyContent: 'center' }}>T</div>
            TIGER · 10:14
          </div>
          <p style={{
            fontFamily: T.serif, fontStyle: 'italic', fontSize: 17, color: T.ink,
            margin: 0, lineHeight: 1.35, letterSpacing: -0.15,
          }}>
            “find me a ryokan that feels like yanaka, but quieter…”
          </p>
        </div>

        {/* VESPER 1 */}
        <div style={{ marginBottom: 18 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 6 }}>
            <VesperMark s={11}/>
            <span style={{ fontSize: 9, color: T.goldDeep, letterSpacing: 1.6, fontWeight: 700 }}>
              VESPER · 10:14
            </span>
          </div>
          <p style={{
            fontFamily: T.serif, fontSize: 16, color: T.inkSoft,
            margin: 0, lineHeight: 1.4, letterSpacing: -0.1,
          }}>
            Three I’d try. <em>Sawanoya</em>, an old house — the slowest of the set.
            <em> Hatago </em>has the quietest alley in Shibuya. And Sukeroku
            catches the morning light you keep noticing.
          </p>
        </div>

        {/* USER 2 — partial, still speaking */}
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 6, color: T.mute, fontSize: 9, letterSpacing: 1.6, fontWeight: 700, marginBottom: 6 }}>
            <div style={{ width: 14, height: 14, borderRadius: 999, background: T.ink, color: T.cardWarm,
              fontFamily: T.serif, fontSize: 8, fontWeight: 600,
              display: 'flex', alignItems: 'center', justifyContent: 'center' }}>T</div>
            TIGER · NOW · <span style={{ color: T.goldDeep }}>SPEAKING</span>
          </div>
          <p style={{
            fontFamily: T.serif, fontStyle: 'italic', fontSize: 17, color: T.ink,
            margin: 0, lineHeight: 1.35, letterSpacing: -0.15,
          }}>
            “go with sawanoya, but only nights five and six<span style={{
              display: 'inline-block', width: 2, height: 16, background: T.gold,
              verticalAlign: 'text-bottom', marginLeft: 2, opacity: 0.7,
            }}/>”
          </p>
        </div>
      </div>

      {/* Bottom dock */}
      <div style={{
        position: 'absolute', bottom: 24, left: 16, right: 16,
        padding: '10px 14px', background: T.cardWarm, borderRadius: 999,
        border: `0.5px solid ${T.hairline}`,
        boxShadow: '0 12px 28px -16px rgba(0,0,0,0.20)',
        display: 'grid', gridTemplateColumns: 'auto 1fr auto', gap: 14, alignItems: 'center',
      }}>
        <span style={{ fontSize: 10, color: T.goldDeep, letterSpacing: 1.6, fontWeight: 700 }}>
          INTERRUPT
        </span>
        {/* waveform */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 2, justifyContent: 'center' }}>
          {[6,11,8,14,10,16,12,18,10,14,7,12,9,5].map((h, i) => (
            <div key={i} style={{ width: 2, height: h, background: T.ink, opacity: 0.7, borderRadius: 1 }}/>
          ))}
        </div>
        <div style={{
          width: 36, height: 36, borderRadius: 999, background: T.ink, color: T.cardWarm,
          display: 'flex', alignItems: 'center', justifyContent: 'center',
        }}>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
            <rect x="6" y="5" width="4" height="14" rx="1"/><rect x="14" y="5" width="4" height="14" rx="1"/>
          </svg>
        </div>
      </div>
    </Phone>
  );
}

Object.assign(window, { VesperVoiceCalm, VesperVoiceTranscript });
