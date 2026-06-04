// Three more Vesper home directions.
//   D · The Atelier — Vesper at work; process over result; queue/set-aside/finished
//   E · The Logbook — Vesper writes you a dated letter; tap-targets folded into prose
//   F · The Whisper — radical reduction; one item full-bleed; swipe for next

// ─── D · THE ATELIER ────────────────────────────────────────────
function VesperAtelier() {
  return (
    <Phone bg={T.bg}>
      <VesperTopBar ctx={<>VESPER · IN THE WORKSHOP · 9:41</>}/>

      {/* Title */}
      <div style={{ padding: '14px 22px 0' }}>
        <VesperEyebrow trailing="3 ON THE BENCH"/>
        <h1 style={{
          fontFamily: T.serif, fontWeight: 500, fontSize: 32, lineHeight: 0.98,
          letterSpacing: -0.8, color: T.ink, margin: '8px 0 0',
        }}>
          Vesper is shaping —<br/>
          <span style={{ fontStyle: 'italic' }}>Tokyo, nights 5–7.</span>
        </h1>
      </div>

      {/* HERO — work in progress */}
      <div style={{ padding: '18px 16px 0' }}>
        <div style={{
          background: T.cardWarm, borderRadius: 16, padding: 16,
          border: `0.8px solid rgba(176,133,58,0.30)`,
          boxShadow: '0 18px 32px -18px rgba(176,133,58,0.18), 0 0 0 0.5px rgba(27,23,20,0.05)',
        }}>
          {/* live tag */}
          <div style={{
            display: 'flex', alignItems: 'center', gap: 6,
          }}>
            <span style={{
              width: 6, height: 6, borderRadius: 6, background: T.gold,
              boxShadow: `0 0 0 3px rgba(176,133,58,0.18)`,
            }}/>
            <span style={{ fontSize: 9.5, color: T.goldDeep, letterSpacing: 1.8, fontWeight: 700 }}>
              SHAPING NOW · A RYOKAN BRIEF
            </span>
            <span style={{ marginLeft: 'auto', fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1.2 }}>
              ETA 20 MIN
            </span>
          </div>

          <h3 style={{
            fontFamily: T.serif, fontWeight: 500, fontSize: 19, color: T.ink,
            margin: '12px 0 4px', letterSpacing: -0.3, lineHeight: 1.15,
          }}>
            Three ryokans you’d <span style={{ fontStyle: 'italic' }}>actually</span> book.
          </h3>
          <p style={{
            fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.mute,
            margin: '0 0 14px', lineHeight: 1.35,
          }}>
            I’m comparing against your slow-streets pattern and Yanaka’s morning light.
          </p>

          {/* progress steps */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
            {[
              { s: 'done', t: 'Pulled 47 ryokan from your saved areas' },
              { s: 'done', t: 'Filtered for quiet alleys + morning light' },
              { s: 'done', t: 'Cross-checked against “Lisbon pattern”' },
              { s: 'now',  t: 'Writing one-line reads for each' },
              { s: 'next', t: 'Final 3 — ready for you to pick' },
            ].map((row, i) => (
              <div key={i} style={{
                display: 'grid', gridTemplateColumns: '16px 1fr', gap: 10, alignItems: 'center',
              }}>
                <div style={{ display: 'flex', justifyContent: 'center' }}>
                  {row.s === 'done' && (
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke={T.muteSoft} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                      <path d="M4 12l5 5L20 6"/>
                    </svg>
                  )}
                  {row.s === 'now' && (
                    <span style={{
                      width: 9, height: 9, borderRadius: 999, background: T.gold,
                      boxShadow: `0 0 0 3px rgba(176,133,58,0.18)`,
                    }}/>
                  )}
                  {row.s === 'next' && (
                    <span style={{
                      width: 7, height: 7, borderRadius: 999,
                      border: `1px solid ${T.muteSoft}`, background: T.cardWarm,
                    }}/>
                  )}
                </div>
                <span style={{
                  fontFamily: T.serif, fontSize: 13,
                  color: row.s === 'now' ? T.ink : row.s === 'done' ? T.mute : T.muteSoft,
                  fontStyle: row.s === 'now' ? 'italic' : 'normal',
                  letterSpacing: -0.1, lineHeight: 1.3,
                }}>
                  {row.t}
                </span>
              </div>
            ))}
          </div>

          {/* footer row */}
          <div style={{
            marginTop: 14, paddingTop: 12, borderTop: `0.5px solid ${T.hairThin}`,
            display: 'flex', alignItems: 'center', justifyContent: 'space-between',
          }}>
            <span style={{ fontSize: 10, color: T.mute, fontStyle: 'italic', fontFamily: T.serif }}>
              come back, or watch
            </span>
            <div style={{ display: 'flex', gap: 6 }}>
              <span style={{ fontSize: 10, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 600, padding: '5px 8px', border: `0.5px solid ${T.hairline}`, borderRadius: 999 }}>
                FINISH WITHOUT ME
              </span>
              <span style={{
                fontSize: 11, color: T.cardWarm, background: T.ink, fontWeight: 600,
                padding: '5px 10px', borderRadius: 999, letterSpacing: -0.1,
                display: 'inline-flex', alignItems: 'center', gap: 4,
              }}>
                Watch <span>→</span>
              </span>
            </div>
          </div>
        </div>
      </div>

      {/* IN QUEUE */}
      <div style={{ padding: '14px 22px 0' }}>
        <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between' }}>
          <span style={{ fontSize: 10, color: T.mute, letterSpacing: 2, fontWeight: 600 }}>IN QUEUE · 4</span>
          <span style={{ fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 600 }}>REORDER →</span>
        </div>
        <div style={{ marginTop: 8, display: 'flex', flexDirection: 'column', gap: 5 }}>
          {[
            { t: 'Five Lisbon-pattern dinners for Tokyo', est: '~12 min' },
            { t: 'Williamsburg sunday → postcard draft',  est: '~6 min'  },
            { t: 'Porto dates with Ana — three options',   est: 'waiting'  },
            { t: 'Paris flight rebook — quiet redirect',   est: 'after'    },
          ].map((q, i) => (
            <div key={i} style={{
              padding: '8px 12px', background: T.cardWarm, borderRadius: 10,
              border: `0.5px solid ${T.hairline}`,
              display: 'grid', gridTemplateColumns: '18px 1fr auto', gap: 10, alignItems: 'center',
            }}>
              <span style={{ fontFamily: T.mono, fontSize: 9, color: T.muteSoft, fontWeight: 600 }}>
                {String(i + 2).padStart(2, '0')}
              </span>
              <span style={{ fontFamily: T.serif, fontSize: 12.5, color: T.inkSoft, letterSpacing: -0.1, lineHeight: 1.2 }}>
                {q.t}
              </span>
              <span style={{ fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1, fontWeight: 600 }}>
                {q.est.toUpperCase()}
              </span>
            </div>
          ))}
        </div>
      </div>

      {/* SET ASIDE + FINISHED — inline */}
      <div style={{ padding: '12px 22px 0', display: 'flex', gap: 8 }}>
        <div style={{
          flex: 1, padding: '8px 10px', borderRadius: 10,
          border: `1px dashed ${T.muteSoft}`,
        }}>
          <div style={{ fontSize: 9, color: T.mute, letterSpacing: 1.4, fontWeight: 700 }}>
            SET ASIDE · 1
          </div>
          <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 11.5, color: T.inkSoft, marginTop: 2, lineHeight: 1.2 }}>
            "Beach week voting"
          </div>
        </div>
        <div style={{
          flex: 1, padding: '8px 10px', borderRadius: 10, background: T.cardSoft,
          border: `0.5px solid ${T.hairline}`,
        }}>
          <div style={{ fontSize: 9, color: T.mute, letterSpacing: 1.4, fontWeight: 700 }}>
            FINISHED TODAY · 1
          </div>
          <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 11.5, color: T.inkSoft, marginTop: 2, lineHeight: 1.2 }}>
            "Tokyo arrival brief →"
          </div>
        </div>
      </div>

      {/* Composer */}
      <div style={{ position: 'absolute', bottom: 96, left: 16, right: 16 }}>
        <Composer placeholder="Ask Vesper to make…"/>
      </div>

      <TabBar active="vesper"/>
    </Phone>
  );
}

// ─── E · THE LOGBOOK ───────────────────────────────────────────
function VesperLogbook() {
  return (
    <Phone bg={T.bg}>
      <VesperTopBar ctx={<>VESPER · LOGBOOK</>}/>

      {/* Date stamp */}
      <div style={{ padding: '16px 22px 0' }}>
        <div style={{
          display: 'flex', alignItems: 'flex-end', justifyContent: 'space-between',
        }}>
          <div>
            <div style={{ fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.8, fontWeight: 600 }}>
              WEDNESDAY
            </div>
            <h1 style={{
              fontFamily: T.serif, fontWeight: 500, fontSize: 44, lineHeight: 0.92,
              letterSpacing: -1.2, color: T.ink, margin: '4px 0 0',
            }}>
              March <span style={{ fontStyle: 'italic' }}>14.</span>
            </h1>
          </div>
          <div style={{
            border: `0.8px solid ${T.gold}`, padding: '3px 7px', borderRadius: 2,
            fontFamily: T.mono, fontSize: 9, color: T.goldDeep, letterSpacing: 1.6, fontWeight: 500,
            transform: 'rotate(-2deg)',
          }}>ENTRY · 091</div>
        </div>
        <div style={{ marginTop: 8, display: 'flex', alignItems: 'center', gap: 10 }}>
          <VesperMark s={12}/>
          <span style={{ fontSize: 10, color: T.goldDeep, letterSpacing: 1.8, fontWeight: 700 }}>VESPER WROTE</span>
          <span style={{ flex: 1, height: 1, background: T.hairline }}/>
          <span style={{ fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 600 }}>9:41 · QUIET MORNING</span>
        </div>
      </div>

      {/* The page — Vesper's letter */}
      <div style={{ padding: '14px 22px 0' }}>
        <p style={{
          fontFamily: T.serif, fontSize: 16.5, color: T.ink, margin: 0,
          lineHeight: 1.5, letterSpacing: -0.1,
        }}>
          Quiet morning. I sketched three ryokans for{' '}
          <LogLink>Tokyo</LogLink> — <LogLink underline>Sawanoya</LogLink>{' '}
          is the one I’d pick, but I’d like to hear you out. The{' '}
          <LogLink hl>Williamsburg photos</LogLink> kept asking to be a postcard,
          so I drafted one. <LogLink mute>Ana confirmed Porto, Jun 6–13</LogLink>
          {' '}— shall I take that off your desk?
        </p>
        <p style={{
          fontFamily: T.serif, fontSize: 15.5, color: T.inkSoft, margin: '14px 0 0',
          lineHeight: 1.5, letterSpacing: -0.1, fontStyle: 'italic',
        }}>
          One small thing — your Paris flight shifted by an hour. Same airport,
          same evening; I’ll re-quiet the calendar if you nod.
        </p>
        <div style={{
          marginTop: 14, fontFamily: T.serif, fontStyle: 'italic',
          fontSize: 14, color: T.mute, letterSpacing: -0.05,
        }}>
          — V.
        </div>
      </div>

      {/* Older entries strip */}
      <div style={{ padding: '20px 22px 0' }}>
        <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between' }}>
          <span style={{ fontSize: 10, color: T.mute, letterSpacing: 2, fontWeight: 600 }}>EARLIER ENTRIES</span>
          <span style={{ fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 600 }}>ALL · 91</span>
        </div>
        <div style={{ marginTop: 10, display: 'flex', flexDirection: 'column', gap: 5 }}>
          {[
            { d: 'MAR 13', l: 'on the Lisbon postcard, almost done.', mark: '·' },
            { d: 'MAR 12', l: 'I noticed a pattern in your morning saves.', mark: '·' },
            { d: 'MAR 11', l: 'three quiet alleys, for Tokyo.', mark: '·' },
          ].map((e, i) => (
            <div key={i} style={{
              display: 'grid', gridTemplateColumns: '54px 1fr auto', gap: 10,
              padding: '8px 0', borderTop: `0.5px solid ${T.hairThin}`,
              alignItems: 'center',
            }}>
              <span style={{ fontFamily: T.mono, fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.2, fontWeight: 600 }}>
                {e.d}
              </span>
              <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.inkSoft, letterSpacing: -0.05 }}>
                “{e.l}”
              </span>
              <span style={{ fontSize: 11, color: T.muteSoft }}>→</span>
            </div>
          ))}
        </div>
      </div>

      {/* Composer */}
      <div style={{ position: 'absolute', bottom: 96, left: 16, right: 16 }}>
        <Composer placeholder="Reply, or write back…"/>
      </div>

      <TabBar active="vesper"/>
    </Phone>
  );
}

// LogLink — a tappable inline noun in Vesper's prose
function LogLink({ children, underline, hl, mute }) {
  if (hl) return (
    <span style={{
      background: 'rgba(176,133,58,0.16)', padding: '0 3px', borderRadius: 2,
      color: T.goldDeep, fontWeight: 500,
    }}>{children}</span>
  );
  if (underline) return (
    <span style={{
      textDecoration: 'underline',
      textDecorationColor: TR.ink,
      textUnderlineOffset: 3,
      textDecorationThickness: '1px',
      color: T.ink, fontWeight: 500,
    }}>{children}</span>
  );
  if (mute) return (
    <span style={{ color: T.mute, textDecoration: 'line-through', textDecorationThickness: '0.5px' }}>
      {children}
    </span>
  );
  return (
    <span style={{
      color: TR.inkDeep, fontWeight: 500,
      borderBottom: `1px dotted ${T.muteSoft}`,
    }}>
      {children}
    </span>
  );
}

// ─── F · THE WHISPER ───────────────────────────────────────────
function VesperWhisper() {
  return (
    <Phone bg={T.bg}>
      {/* Minimal top — close + position */}
      <div style={{
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        padding: '14px 24px 0',
      }}>
        <span style={{ fontSize: 10.5, color: T.muteSoft, letterSpacing: 1.8, fontWeight: 600 }}>
          CALM MODE
        </span>
        <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
          <VesperMark s={11}/>
          <span style={{ fontFamily: T.mono, fontSize: 10, color: T.mute, letterSpacing: 1.2, fontWeight: 600 }}>
            1 / 4
          </span>
        </div>
      </div>

      {/* The single line — full-bleed serif */}
      <div style={{
        padding: '120px 28px 0',
      }}>
        <div style={{
          display: 'inline-flex', alignItems: 'center', gap: 6,
          color: TR.inkDeep, fontSize: 9.5, letterSpacing: 1.8, fontWeight: 700,
        }}>
          <span style={{ width: 5, height: 5, borderRadius: 5, background: TR.ink }}/>
          NEEDS YOU
        </div>
        <h1 style={{
          fontFamily: T.serif, fontWeight: 500, fontSize: 42, lineHeight: 1.04,
          letterSpacing: -1.2, color: T.ink, margin: '14px 0 0',
        }}>
          Tokyo would like a <span style={{ fontStyle: 'italic' }}>ryokan</span> for nights five through seven.
        </h1>
        <p style={{
          fontFamily: T.serif, fontStyle: 'italic', fontSize: 15, color: T.mute,
          margin: '20px 0 0', lineHeight: 1.45, letterSpacing: -0.05,
        }}>
          I narrowed forty-seven down to three — slow alleys, morning light,
          one old house. Pick one and I’ll handle the rest.
        </p>
      </div>

      {/* Three quiet actions */}
      <div style={{
        position: 'absolute', bottom: 168, left: 28, right: 28,
        display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: 10,
      }}>
        <div style={{
          padding: '11px 18px', background: T.ink, color: T.cardWarm,
          borderRadius: 999, fontSize: 13, fontWeight: 600, letterSpacing: -0.1,
          display: 'inline-flex', alignItems: 'center', gap: 6,
        }}>
          Pick one <span>→</span>
        </div>
        <span style={{
          fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.inkSoft,
        }}>set aside</span>
        <span style={{
          fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.muteSoft,
        }}>tell me more</span>
      </div>

      {/* Escape hatch — "ask something else" + tiny mic */}
      <div style={{
        position: 'absolute', bottom: 124, left: 0, right: 0,
        display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 10,
      }}>
        <span style={{
          fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.muteSoft,
          letterSpacing: -0.05, borderBottom: `1px dotted ${T.muteSoft}`,
          paddingBottom: 1,
        }}>
          ask something else
        </span>
        <div style={{
          width: 22, height: 22, borderRadius: 999, background: T.cardWarm,
          border: `0.5px solid ${T.hairline}`,
          display: 'flex', alignItems: 'center', justifyContent: 'center',
        }}>
          <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="1.8" strokeLinecap="round">
            <rect x="9" y="3" width="6" height="12" rx="3"/>
            <path d="M5 11c0 4 3 7 7 7s7-3 7-7M12 18v3M8 21h8"/>
          </svg>
        </div>
      </div>

      {/* Position ticks */}
      <div style={{
        position: 'absolute', bottom: 92, left: 0, right: 0,
        display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 14,
      }}>
        {[0,1,2,3].map(i => (
          <div key={i} style={{
            width: i === 0 ? 22 : 6, height: 3, borderRadius: 3,
            background: i === 0 ? T.ink : T.muteSoft,
            opacity: i === 0 ? 1 : 0.5,
          }}/>
        ))}
      </div>

      <TabBar active="vesper"/>
    </Phone>
  );
}

Object.assign(window, { VesperAtelier, VesperLogbook, VesperWhisper });
