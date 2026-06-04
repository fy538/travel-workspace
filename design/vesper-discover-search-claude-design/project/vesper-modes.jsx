// Two contextual takeovers + the universal voice affordance.
//   VesperOnTrip  — "you're in Tokyo" hour-mode; voice is primary
//   VesperUrgent  — time-sensitive pre-emption; everything else demoted
//   TabBarLongPress — visual aside showing how voice is invoked anywhere

// ─── ON TRIP MODE ───────────────────────────────────────────────
// While you're between depart and return. Vesper stops working *on* you
// and starts working *for* you in this hour.
function VesperOnTrip() {
  return (
    <Phone bg={T.bg}>
      <VesperTopBar
        ctx={<>VESPER · DAY 3 IN TOKYO · 10:14 JST</>}
      />

      {/* Save-a-moment & live tag */}
      <div style={{ padding: '14px 22px 0', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <span style={{
          display: 'inline-flex', alignItems: 'center', gap: 6,
          padding: '3px 10px', borderRadius: 999,
          fontSize: 9.5, letterSpacing: 1.6, fontWeight: 700,
          color: T.cardWarm, background: TR.ink,
        }}>
          <span style={{ width: 6, height: 6, borderRadius: 6, background: '#E5C16F',
            boxShadow: `0 0 0 3px rgba(229,193,111,0.25)` }}/>
          LIVE
        </span>
        <span style={{
          display: 'inline-flex', alignItems: 'center', gap: 5,
          padding: '4px 10px', borderRadius: 999, background: T.cardWarm,
          border: `0.8px dashed ${T.gold}`,
          fontSize: 10, color: T.goldDeep, letterSpacing: 1.4, fontWeight: 700,
        }}>
          <TripIcons.Sparkle s={11}/>
          SAVE A MOMENT
        </span>
      </div>

      {/* Title — about THIS HOUR */}
      <div style={{ padding: '14px 24px 0' }}>
        <div style={{ fontSize: 10, color: T.muteSoft, letterSpacing: 1.8, fontWeight: 600 }}>
          MONDAY · 10 AM · YANAKA
        </div>
        <h1 style={{
          fontFamily: T.serif, fontWeight: 500, fontSize: 32, lineHeight: 0.98,
          letterSpacing: -0.9, color: T.ink, margin: '8px 0 0',
        }}>
          You have an <span style={{ fontStyle: 'italic' }}>open hour.</span>
        </h1>
      </div>

      {/* HERO — a single moment recommendation, no list */}
      <div style={{ padding: '20px 16px 0' }}>
        <div style={{
          background: T.cardWarm, borderRadius: 16, padding: 18,
          boxShadow: '0 18px 32px -18px rgba(0,0,0,0.18), 0 0 0 0.5px rgba(27,23,20,0.06)',
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
            <VesperMark s={11}/>
            <span style={{ fontSize: 9.5, color: T.goldDeep, letterSpacing: 1.6, fontWeight: 700 }}>
              ON YOUR SLOW-STREETS PATTERN
            </span>
          </div>
          <h2 style={{
            fontFamily: T.serif, fontWeight: 500, fontSize: 24, color: T.ink,
            margin: '10px 0 6px', letterSpacing: -0.4, lineHeight: 1.1,
          }}>
            <span style={{ fontStyle: 'italic' }}>Kayaba Coffee</span> — 8 minutes east.
          </h2>
          <p style={{
            fontFamily: T.serif, fontSize: 14.5, color: T.inkSoft, margin: '0 0 12px',
            lineHeight: 1.4, letterSpacing: -0.05,
          }}>
            A pre-war kissaten on the corner of Yanaka Cemetery. Open until 11.
            The morning light is the kind you keep noticing.
          </p>
          {/* meta strip */}
          <div style={{
            display: 'flex', gap: 6, marginBottom: 14,
          }}>
            {['8 min walk', 'no booking', '¥'].map((m, i) => (
              <span key={m} style={{
                padding: '4px 9px', fontFamily: T.mono, fontSize: 9, color: T.mute,
                letterSpacing: 1.2, fontWeight: 600,
                border: `0.5px solid ${T.hairline}`, borderRadius: 999, background: T.bg,
              }}>{m.toUpperCase()}</span>
            ))}
          </div>
          {/* actions */}
          <div style={{
            display: 'flex', alignItems: 'center', justifyContent: 'space-between',
            paddingTop: 12, borderTop: `0.5px solid ${T.hairThin}`,
          }}>
            <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.mute }}>
              something else?
            </span>
            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
              <span style={{
                padding: '6px 11px', fontSize: 11, color: T.inkSoft, fontWeight: 600,
                border: `0.5px solid ${T.hairline}`, borderRadius: 999, letterSpacing: -0.05,
              }}>Walk me there</span>
              <span style={{
                padding: '7px 14px', background: TR.ink, color: T.cardWarm,
                borderRadius: 999, fontSize: 12, fontWeight: 600, letterSpacing: -0.1,
                display: 'inline-flex', alignItems: 'center', gap: 5,
              }}>I'm in <span>→</span></span>
            </div>
          </div>
        </div>
      </div>

      {/* Later today — faint */}
      <div style={{ padding: '14px 22px 0' }}>
        <div style={{ fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.8, fontWeight: 600 }}>
          LATER TODAY · 2 KEPT
        </div>
        <div style={{ marginTop: 8, display: 'flex', flexDirection: 'column', gap: 4 }}>
          {[
            { time: 'AFTERN.', t: 'Senso-ji · saved by you' },
            { time: 'TONIGHT', t: 'Dinner — no plan' },
          ].map((r, i) => (
            <div key={i} style={{
              padding: '8px 12px', display: 'grid', gridTemplateColumns: '54px 1fr auto',
              gap: 10, alignItems: 'center', background: 'transparent',
              borderBottom: `0.5px solid ${T.hairThin}`,
            }}>
              <span style={{ fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1.2, fontWeight: 600 }}>
                {r.time}
              </span>
              <span style={{ fontFamily: T.serif, fontSize: 13, color: T.inkSoft, letterSpacing: -0.1 }}>
                {r.t}
              </span>
              <span style={{ fontSize: 11, color: T.muteSoft }}>→</span>
            </div>
          ))}
        </div>
      </div>

      {/* Voice-prominent dock — voice is the primary affordance on trip */}
      <div style={{
        position: 'absolute', bottom: 96, left: 16, right: 16,
        padding: '8px 8px 8px 18px', background: T.cardWarm, borderRadius: 999,
        border: `0.5px solid ${T.hairline}`,
        boxShadow: '0 8px 22px -14px rgba(0,0,0,0.18), 0 1px 0 rgba(255,255,255,0.6) inset',
        display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: 10,
      }}>
        <span style={{
          fontFamily: T.serif, fontStyle: 'italic', fontSize: 14, color: T.inkSoft,
          letterSpacing: -0.05,
        }}>
          tell me anything — I'll find it
        </span>
        <div style={{
          width: 52, height: 52, borderRadius: 999, background: T.ink, color: T.cardWarm,
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          boxShadow: '0 3px 8px rgba(0,0,0,0.22)',
          position: 'relative',
        }}>
          {/* breath ring */}
          <div style={{
            position: 'absolute', inset: -5, borderRadius: 999,
            border: `1px solid rgba(176,133,58,0.30)`,
          }}/>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round">
            <rect x="9" y="3" width="6" height="12" rx="3"/>
            <path d="M5 11c0 4 3 7 7 7s7-3 7-7M12 18v3M8 21h8"/>
          </svg>
        </div>
      </div>

      <TabBar active="vesper"/>
    </Phone>
  );
}

// ─── URGENT / TIME-SENSITIVE MODE ───────────────────────────────
// One thing pre-empts the desk. Calm-not-screaming red. Everything else
// demoted to a single quiet line.
function VesperUrgent() {
  const red = '#A04030';
  const redDeep = '#7C2F22';
  const redHint = 'rgba(160,64,48,0.10)';
  return (
    <Phone bg={T.bg}>
      <VesperTopBar
        ctx={<><span style={{ color: red }}>TIME-SENSITIVE</span> · 10:42</>}
      />

      {/* Title — quiet, no shouting */}
      <div style={{ padding: '14px 24px 0' }}>
        <div style={{
          display: 'inline-flex', alignItems: 'center', gap: 6,
          color: redDeep, fontSize: 10.5, letterSpacing: 1.8, fontWeight: 700,
        }}>
          <span style={{
            width: 6, height: 6, borderRadius: 6, background: red,
            boxShadow: `0 0 0 3px rgba(160,64,48,0.18)`,
          }}/>
          VESPER · ONE THING FIRST
        </div>
        <h1 style={{
          fontFamily: T.serif, fontWeight: 500, fontSize: 32, lineHeight: 0.98,
          letterSpacing: -0.9, color: T.ink, margin: '12px 0 0',
        }}>
          Your Paris flight just <span style={{ fontStyle: 'italic' }}>shifted.</span>
        </h1>
      </div>

      {/* HERO — single alert, sit-with-it serif */}
      <div style={{ padding: '20px 16px 0' }}>
        <div style={{
          background: redHint, borderRadius: 16, padding: 18,
          border: `0.8px solid rgba(160,64,48,0.30)`,
        }}>
          {/* facts row */}
          <div style={{
            display: 'grid', gridTemplateColumns: '1fr 14px 1fr', gap: 12, alignItems: 'center',
            padding: '6px 4px',
          }}>
            <div>
              <div style={{ fontSize: 9, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 700 }}>WAS</div>
              <div style={{
                fontFamily: T.serif, fontSize: 28, fontWeight: 500, color: T.mute,
                marginTop: 4, letterSpacing: -0.5, lineHeight: 1, fontVariantNumeric: 'oldstyle-nums',
                textDecoration: 'line-through', textDecorationColor: T.muteSoft, textDecorationThickness: '1px',
              }}>
                19:55
              </div>
              <div style={{ fontFamily: T.mono, fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.2, marginTop: 4, fontWeight: 600 }}>
                THU · MAR 28
              </div>
            </div>
            <div style={{ textAlign: 'center' }}>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke={red} strokeWidth="2" strokeLinecap="round">
                <path d="M5 12h14M13 6l6 6-6 6"/>
              </svg>
            </div>
            <div>
              <div style={{ fontSize: 9, color: redDeep, letterSpacing: 1.4, fontWeight: 700 }}>NOW</div>
              <div style={{
                fontFamily: T.serif, fontSize: 28, fontWeight: 500, color: T.ink,
                marginTop: 4, letterSpacing: -0.5, lineHeight: 1, fontVariantNumeric: 'oldstyle-nums',
              }}>
                18:55
              </div>
              <div style={{ fontFamily: T.mono, fontSize: 9.5, color: redDeep, letterSpacing: 1.2, marginTop: 4, fontWeight: 600 }}>
                SAME DAY · CDG
              </div>
            </div>
          </div>

          <p style={{
            fontFamily: T.serif, fontStyle: 'italic', fontSize: 14, color: T.inkSoft,
            margin: '16px 0 14px', lineHeight: 1.4, letterSpacing: -0.05,
            paddingTop: 12, borderTop: `0.5px dashed rgba(160,64,48,0.25)`,
          }}>
            Same airport, same evening. Your seat held. I can re-quiet your
            calendar if you nod.
          </p>

          {/* two calm actions */}
          <div style={{ display: 'flex', gap: 6 }}>
            <span style={{
              flex: 1, padding: '10px 14px', background: T.ink, color: T.cardWarm,
              borderRadius: 999, fontSize: 12.5, fontWeight: 600, letterSpacing: -0.1,
              textAlign: 'center',
            }}>
              I’ll handle it
            </span>
            <span style={{
              flex: 1, padding: '10px 14px', background: T.cardWarm, color: T.inkSoft,
              border: `0.5px solid ${T.hairline}`,
              borderRadius: 999, fontSize: 12.5, fontWeight: 500, letterSpacing: -0.05,
              textAlign: 'center', fontFamily: T.serif, fontStyle: 'italic',
            }}>
              tell me what you want
            </span>
          </div>
        </div>
      </div>

      {/* Demoted line — everything else */}
      <div style={{
        position: 'absolute', bottom: 168, left: 22, right: 22,
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        padding: '12px 14px', background: T.cardSoft, borderRadius: 10,
        border: `0.5px solid ${T.hairline}`,
      }}>
        <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.mute, letterSpacing: -0.05 }}>
          and <span style={{ color: T.inkSoft }}>6 other things</span> on the desk
        </span>
        <Marks.ArrowR s={13} c={T.muteSoft}/>
      </div>

      {/* Composer */}
      <div style={{ position: 'absolute', bottom: 96, left: 16, right: 16 }}>
        <Composer placeholder="Ask Vesper…"/>
      </div>

      <TabBar active="vesper"/>
    </Phone>
  );
}

// ─── TAB-BAR LONG-PRESS · how voice is invoked anywhere ─────────
// A wide visual aside that lives on the canvas as a documentation card.
function TabBarLongPress() {
  return (
    <div style={{
      width: 760, padding: '36px 32px', background: '#F1ECE2', borderRadius: 8,
      color: T.inkSoft, fontFamily: T.sans, fontSize: 13.5, lineHeight: 1.55,
      position: 'relative',
    }}>
      <div style={{ fontSize: 10.5, letterSpacing: 2, color: T.gold, fontWeight: 600, marginBottom: 8 }}>
        VOICE · UNIVERSAL ACCESS
      </div>
      <h2 style={{
        fontFamily: T.serif, fontWeight: 500, fontSize: 30, color: T.ink,
        margin: '0 0 14px', letterSpacing: -0.7, lineHeight: 1.05,
      }}>
        The Vesper tab <em>is</em> the voice button.
      </h2>
      <p style={{ margin: '0 0 22px', maxWidth: 600 }}>
        No floating chat-bot dot, no orb on the side. Voice lives in three places — and
        the bottom-bar Vesper sparkle does the heavy lifting from anywhere in the app.
      </p>

      {/* Visual: a wide tab-bar slice with the Vesper icon mid-long-press */}
      <div style={{
        background: T.bg, borderRadius: 18, padding: 36,
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 24,
        border: `0.5px solid ${T.hairline}`,
      }}>
        {/* "Hold to speak" tooltip */}
        <div style={{
          padding: '8px 14px', background: T.ink, color: T.cardWarm, borderRadius: 12,
          fontFamily: T.serif, fontStyle: 'italic', fontSize: 14, letterSpacing: -0.1,
          boxShadow: '0 8px 22px -10px rgba(0,0,0,0.3)',
          position: 'relative',
        }}>
          Hold to speak
          {/* tail */}
          <div style={{
            position: 'absolute', bottom: -6, left: '50%', transform: 'translateX(-50%) rotate(45deg)',
            width: 10, height: 10, background: T.ink,
          }}/>
        </div>

        {/* tab bar slice */}
        <div style={{
          width: 340, padding: '10px 14px 14px', borderRadius: 32,
          background: T.cardWarm, border: `0.5px solid ${T.hairline}`,
          display: 'flex', alignItems: 'center', justifyContent: 'space-between',
          boxShadow: '0 8px 24px -8px rgba(0,0,0,0.12), 0 1px 0 rgba(255,255,255,0.6) inset',
        }}>
          {/* tabs */}
          {['Trips', 'Vesper', 'Discover', 'Atlas'].map((t, i) => {
            const isVesper = i === 1;
            return (
              <div key={t} style={{
                flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 3,
                color: T.muteSoft, position: 'relative',
              }}>
                {/* active ring on Vesper */}
                {isVesper && (
                  <div style={{
                    position: 'absolute', inset: '-6px -8px 0 -8px', top: -8,
                    borderRadius: 22, background: 'rgba(176,133,58,0.14)',
                    border: `1px solid rgba(176,133,58,0.4)`,
                  }}/>
                )}
                <div style={{ position: 'relative', zIndex: 1 }}>
                  {isVesper ? (
                    <svg width="26" height="26" viewBox="0 0 24 24" fill={T.gold}>
                      <path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/>
                      <path d="M19 16 L19.6 18.4 L22 19 L19.6 19.6 L19 22 L18.4 19.6 L16 19 L18.4 18.4 Z" opacity="0.85"/>
                    </svg>
                  ) : i === 0 ? (
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke={T.muteSoft} strokeWidth="1.5" strokeLinecap="round">
                      <rect x="3.5" y="7" width="17" height="13" rx="2.5"/>
                      <path d="M9 7V5.5A1.5 1.5 0 0 1 10.5 4h3A1.5 1.5 0 0 1 15 5.5V7"/>
                    </svg>
                  ) : i === 2 ? (
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke={T.muteSoft} strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
                      <circle cx="12" cy="12" r="8.5"/>
                      <path d="M15 9l-1.4 4.6L9 15l1.4-4.6L15 9Z" fill={T.muteSoft} fillOpacity="0.2"/>
                    </svg>
                  ) : (
                    <svg width="22" height="22" viewBox="0 0 24 24" fill={T.muteSoft}>
                      <path d="M5 4.5A1.5 1.5 0 0 1 6.5 3H11v17.5L7 19l-2 1V4.5Z" opacity="0.55"/>
                      <path d="M13 3h4.5A1.5 1.5 0 0 1 19 4.5V20l-2-1-4 1.5V3Z" opacity="0.55"/>
                    </svg>
                  )}
                </div>
                <span style={{
                  fontSize: 10, fontWeight: isVesper ? 700 : 500,
                  color: isVesper ? T.goldDeep : T.muteSoft, letterSpacing: 0.2,
                  position: 'relative', zIndex: 1,
                }}>{t}</span>
              </div>
            );
          })}
        </div>

        {/* haptic ring */}
        <div style={{
          fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.muteSoft,
        }}>
          haptic — light, twice
        </div>
      </div>

      {/* Three entry points */}
      <div style={{ marginTop: 26, display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 12 }}>
        {[
          { eb: '01 · IN COMPOSER',  t: 'Tap the mic',                   d: 'inside the Vesper tab\u2019s composer pill. The default voice entry.' },
          { eb: '02 · FROM ANY TAB', t: 'Long-press Vesper',             d: 'opens Calm Listening directly. Light haptic confirms.' },
          { eb: '03 · WHEN PROACTIVE', t: 'Ochre dot on the sparkle',    d: 'tap = open the waiting thing. Same path, not a separate button.' },
        ].map((c, i) => (
          <div key={i} style={{
            padding: '14px 14px', background: '#FBF7EC', borderRadius: 12,
            border: i === 1 ? `0.8px solid ${T.gold}` : `0.5px solid rgba(27,23,20,0.07)`,
          }}>
            <div style={{ fontSize: 9.5, color: i === 1 ? T.goldDeep : T.mute, letterSpacing: 1.6, fontWeight: 700 }}>{c.eb}</div>
            <div style={{ fontFamily: T.serif, fontSize: 15, fontWeight: 500, color: T.ink, marginTop: 6, letterSpacing: -0.2, lineHeight: 1.1 }}>{c.t}</div>
            <div style={{ fontSize: 11.5, color: T.mute, marginTop: 5, lineHeight: 1.45 }}>{c.d}</div>
          </div>
        ))}
      </div>

      {/* What we're NOT doing */}
      <div style={{
        marginTop: 18, padding: 14, background: '#FBF7EC', borderRadius: 8,
        fontSize: 12, color: T.mute, lineHeight: 1.5,
      }}>
        <b style={{ color: T.ink }}>What we&rsquo;re not doing</b> — no floating
        round mic button on every screen, no &ldquo;Hey Vesper&rdquo; wake-word,
        no Siri-style screen takeover from outside the Vesper tab. The tab icon is
        the universal handle; Calm Listening is the universal voice state.
      </div>
    </div>
  );
}

Object.assign(window, { VesperOnTrip, VesperUrgent, TabBarLongPress });
