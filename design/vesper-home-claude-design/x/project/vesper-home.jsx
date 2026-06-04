// Three Vesper Home directions.
//   A · The Desk      — object cards arranged like things on an assistant's desk
//   B · The Briefing  — a morning briefing in Vesper's voice, sectioned beneath
//   C · The Dialogue  — composer-forward; proactive prompts orbit the input

// ─── A · THE DESK ───────────────────────────────────────────────
function VesperDesk() {
  return (
    <Phone bg={T.bg}>
      <VesperTopBar ctx={<>WED · MAR 14 · NEW YORK 22°</>}/>

      {/* Greeting */}
      <div style={{ padding: '14px 22px 0' }}>
        <VesperEyebrow trailing="9:41 · 4 ON YOUR DESK"/>
        <h1 style={{
          fontFamily: T.serif, fontWeight: 500, fontSize: 32, lineHeight: 0.98,
          letterSpacing: -0.8, color: T.ink, margin: '8px 0 0',
        }}>
          Hey Tiger —<br/>
          <span style={{ fontStyle: 'italic' }}>Tokyo is asking for one decision.</span>
        </h1>
      </div>

      {/* HERO OBJECT — an envelope-shaped action card */}
      <div style={{ padding: '18px 16px 0' }}>
        <div style={{
          background: T.cardWarm, borderRadius: 14, position: 'relative',
          boxShadow: '0 18px 32px -18px rgba(0,0,0,0.20), 0 0 0 0.5px rgba(27,23,20,0.06)',
          overflow: 'hidden',
        }}>
          {/* envelope flap */}
          <svg width="100%" height="46" viewBox="0 0 360 46" preserveAspectRatio="none" style={{ display: 'block' }}>
            <path d="M0 0 L360 0 L360 8 L180 38 L0 8 Z" fill={T.cardSoft}/>
            <path d="M0 8 L180 38 L360 8" stroke={T.hairline} strokeWidth="0.5" fill="none"/>
          </svg>
          <div style={{ padding: '4px 16px 16px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
              <span style={{ width: 6, height: 6, borderRadius: 6, background: TR.ink }}/>
              <span style={{ fontSize: 9.5, color: TR.inkDeep, letterSpacing: 1.8, fontWeight: 700 }}>
                ACTION · TOKYO IS READY FOR A SECOND PASS
              </span>
            </div>
            <h2 style={{
              fontFamily: T.serif, fontWeight: 500, fontSize: 22, color: T.ink,
              margin: '8px 0 6px', letterSpacing: -0.4, lineHeight: 1.1,
            }}>
              Pick a ryokan for nights <span style={{ fontStyle: 'italic' }}>5 — 7</span>.
            </h2>
            <p style={{
              fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.mute,
              margin: '0 0 12px', lineHeight: 1.35,
            }}>
              I narrowed the list to three that match your slow-streets pattern.
            </p>
            {/* mini list of options */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: 4, marginBottom: 12 }}>
              {[
                { name: 'Shibuya · Hatago, 2-room',     sub: 'quiet alley · ¥¥' },
                { name: 'Asakusa · Sukeroku-no-Yado',   sub: 'morning light · ¥¥' },
                { name: 'Yanaka · Sawanoya',             sub: 'an old house · ¥' },
              ].map((r, i) => (
                <div key={i} style={{
                  display: 'grid', gridTemplateColumns: '14px 1fr auto', gap: 10, alignItems: 'center',
                  padding: '8px 10px', background: T.bg, borderRadius: 8,
                }}>
                  <div style={{
                    width: 14, height: 14, borderRadius: 4, border: `1px solid ${T.muteSoft}`,
                  }}/>
                  <div>
                    <div style={{ fontFamily: T.serif, fontSize: 13, color: T.ink, fontWeight: 500, letterSpacing: -0.1, lineHeight: 1.1 }}>
                      {r.name}
                    </div>
                    <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 10.5, color: T.mute, marginTop: 2 }}>
                      {r.sub}
                    </div>
                  </div>
                  <span style={{ fontSize: 10, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 600 }}>READ</span>
                </div>
              ))}
            </div>
            <div style={{
              display: 'flex', alignItems: 'center', justifyContent: 'space-between',
              gap: 6,
            }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                <span style={{ fontSize: 10, color: T.mute, letterSpacing: 1.3, fontWeight: 600 }}>WHY THESE</span>
                <span style={{ fontSize: 10, color: T.muteSoft, letterSpacing: 1.3, fontWeight: 600 }}>NOT NOW</span>
              </div>
              <div style={{
                padding: '7px 14px', background: TR.ink, color: T.cardWarm,
                borderRadius: 999, fontSize: 11.5, fontWeight: 600,
                display: 'flex', alignItems: 'center', gap: 6,
              }}>
                Open in Trips <span>→</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* TWO SMALLER OBJECTS — sheet (draft) + photo (memory) ─── */}
      <div style={{
        padding: '14px 16px 0', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8,
      }}>
        {/* sheet — DRAFT */}
        <div style={{
          padding: 12, background: T.cardWarm, borderRadius: 12,
          border: `0.5px solid ${T.hairline}`, position: 'relative',
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
            <span style={{ width: 5, height: 5, borderRadius: 5, background: T.goldDeep }}/>
            <span style={{ fontSize: 8.5, color: T.goldDeep, letterSpacing: 1.4, fontWeight: 700 }}>DRAFT</span>
          </div>
          <div style={{
            fontFamily: T.serif, fontSize: 15, fontWeight: 500, color: T.ink,
            letterSpacing: -0.2, lineHeight: 1.15, marginTop: 8,
          }}>
            Five Lisbon-pattern dinners
          </div>
          <div style={{
            fontFamily: T.serif, fontStyle: 'italic', fontSize: 10.5, color: T.mute,
            marginTop: 4, lineHeight: 1.3,
          }}>
            for Tokyo nights 1 &amp; 6
          </div>
          {/* paper margin lines */}
          <div style={{ marginTop: 10, display: 'flex', flexDirection: 'column', gap: 3 }}>
            {[1,2,3,4].map(i => (
              <div key={i} style={{ height: 2, background: T.muteSoft, opacity: 0.18, borderRadius: 1, width: i === 4 ? '60%' : '100%' }}/>
            ))}
          </div>
        </div>

        {/* photo — MEMORY */}
        <div style={{
          padding: 12, background: T.cardWarm, borderRadius: 12,
          border: `0.5px solid ${T.hairline}`,
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
            <span style={{ width: 5, height: 5, borderRadius: 5, background: T.gold }}/>
            <span style={{ fontSize: 8.5, color: T.goldDeep, letterSpacing: 1.4, fontWeight: 700 }}>COULD KEEP</span>
          </div>
          <div style={{
            fontFamily: T.serif, fontSize: 15, fontWeight: 500, color: T.ink,
            letterSpacing: -0.2, lineHeight: 1.15, marginTop: 8,
          }}>
            Williamsburg, Sunday
          </div>
          <div style={{
            fontFamily: T.serif, fontStyle: 'italic', fontSize: 10.5, color: T.mute,
            marginTop: 4, lineHeight: 1.3,
          }}>
            twelve photos · could be a postcard
          </div>
          {/* tiny photo strip placeholder */}
          <div style={{ marginTop: 10, display: 'flex', gap: 3 }}>
            {[0,1,2,3].map(i => (
              <div key={i} style={{
                flex: 1, height: 32, borderRadius: 2, background: T.cardSoft,
                border: `0.5px solid ${T.hairThin}`,
              }}/>
            ))}
          </div>
        </div>
      </div>

      {/* SIGNAL — a small dotted note */}
      <div style={{ padding: '8px 16px 0' }}>
        <div style={{
          padding: '10px 14px', background: 'transparent', borderRadius: 10,
          border: `1px dashed ${T.muteSoft}`,
          display: 'flex', alignItems: 'center', gap: 10,
        }}>
          <span style={{ width: 5, height: 5, borderRadius: 5, background: TR.dreaming }}/>
          <span style={{ fontSize: 8.5, color: TR.dreaming, letterSpacing: 1.4, fontWeight: 700 }}>NOTICED</span>
          <span style={{ flex: 1, fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.inkSoft, letterSpacing: -0.05 }}>
            you save quiet neighborhoods <em>before</em> landmarks.
          </span>
        </div>
      </div>

      {/* Composer — sits above the tab bar */}
      <div style={{ position: 'absolute', bottom: 96, left: 16, right: 16 }}>
        <Composer placeholder="Ask Vesper… or pick one above"/>
      </div>

      <TabBar active="vesper"/>
    </Phone>
  );
}

// ─── B · THE BRIEFING ───────────────────────────────────────────
function VesperBriefing() {
  return (
    <Phone bg={T.bg}>
      <VesperTopBar ctx={<>WEDNESDAY · MAR 14 · TIGER</>}/>

      {/* Masthead */}
      <div style={{ padding: '16px 22px 0' }}>
        <div style={{ display: 'flex', alignItems: 'flex-end', justifyContent: 'space-between' }}>
          <h1 style={{
            fontFamily: T.serif, fontWeight: 400, fontSize: 56, lineHeight: 0.9,
            letterSpacing: -1.8, color: T.ink, margin: 0,
          }}>
            <span style={{ fontStyle: 'italic' }}>Vesper</span>
          </h1>
          <div style={{
            border: `0.8px solid ${T.gold}`, padding: '3px 7px', borderRadius: 2,
            fontFamily: T.mono, fontSize: 9, color: T.goldDeep, letterSpacing: 1.6, fontWeight: 500,
            transform: 'rotate(-1.5deg)',
          }}>EDITION · 047</div>
        </div>
        <div style={{
          marginTop: 8, display: 'flex', alignItems: 'center', gap: 10,
          color: T.mute, fontSize: 10, letterSpacing: 1.4, fontWeight: 600,
        }}>
          <span>YOUR DESK</span>
          <span style={{ flex: 1, height: 1, background: T.hairline }}/>
          <span>4 ITEMS · 9:41</span>
        </div>
      </div>

      {/* TODAY — Vesper's voice */}
      <div style={{ padding: '16px 22px 0' }}>
        <VesperEyebrow trailing="ONE READ"/>
        <p style={{
          fontFamily: T.serif, fontSize: 17, color: T.ink, margin: '10px 0 0',
          lineHeight: 1.4, letterSpacing: -0.1,
        }}>
          Tokyo wants <em>one decision today</em> — a ryokan for nights five through
          seven. Beyond that, your week is quiet: a draft of Lisbon-pattern dinners,
          a sunday in Williamsburg that could become a postcard, and a flight window
          that just shifted by an hour.
        </p>
      </div>

      {/* BELOW THE FOLD — items as editorial cards */}
      <div style={{ padding: '16px 22px 0' }}>
        <div style={{ fontSize: 10, color: T.mute, letterSpacing: 2, fontWeight: 600, marginBottom: 6 }}>
          ON YOUR DESK
        </div>
        <div style={{ display: 'flex', flexDirection: 'column' }}>
          {[
            { kind: 'ACTION',  c: TR.ink,      t: 'Pick a ryokan, Tokyo',     sub: 'three options · nights 5–7', meta: 'OPEN' },
            { kind: 'DRAFT',   c: T.goldDeep,  t: 'Five Lisbon-pattern dinners', sub: 'kept for Tokyo nights 1 & 6', meta: 'READ' },
            { kind: 'MEMORY',  c: T.gold,      t: 'Williamsburg, sunday',    sub: 'twelve photos · postcard candidate', meta: 'KEEP' },
            { kind: 'ALERT',   c: '#A55747',   t: 'Paris flight shifted',     sub: 'now 18:55, was 19:55', meta: 'SEE' },
          ].map((row, i) => (
            <div key={i} style={{
              padding: '14px 0', borderTop: i === 0 ? `0.5px solid ${T.hairline}` : `0.5px solid ${T.hairThin}`,
              display: 'grid', gridTemplateColumns: '60px 1fr auto', gap: 12, alignItems: 'baseline',
            }}>
              <div style={{ display: 'flex', alignItems: 'baseline', gap: 5 }}>
                <span style={{ width: 5, height: 5, borderRadius: 5, background: row.c, transform: 'translateY(-2px)' }}/>
                <span style={{ fontSize: 8.5, color: row.c, letterSpacing: 1.4, fontWeight: 700 }}>{row.kind}</span>
              </div>
              <div>
                <div style={{
                  fontFamily: T.serif, fontSize: 17, color: T.ink, fontWeight: 500,
                  letterSpacing: -0.3, lineHeight: 1.1,
                }}>{row.t}</div>
                <div style={{
                  fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.mute,
                  marginTop: 3, lineHeight: 1.3,
                }}>{row.sub}</div>
              </div>
              <span style={{
                fontSize: 9, color: T.inkSoft, letterSpacing: 1.4, fontWeight: 700,
                padding: '3px 7px', border: `0.6px solid ${T.hairline}`, borderRadius: 3,
              }}>{row.meta}</span>
            </div>
          ))}
          <div style={{ borderTop: `0.5px solid ${T.hairThin}` }}/>
        </div>
      </div>

      {/* Composer */}
      <div style={{ position: 'absolute', bottom: 96, left: 16, right: 16 }}>
        <Composer placeholder="Continue, or ask something new…"/>
      </div>

      <TabBar active="vesper"/>
    </Phone>
  );
}

// ─── C · THE DIALOGUE ───────────────────────────────────────────
function VesperDialogue() {
  return (
    <Phone bg={T.bg}>
      <VesperTopBar ctx={<>VESPER · 9:41</>}/>

      {/* Short greeting */}
      <div style={{ padding: '18px 22px 0', textAlign: 'center' }}>
        <div style={{ display: 'inline-flex', alignItems: 'center', justifyContent: 'center', gap: 6, color: T.goldDeep, fontSize: 10, letterSpacing: 1.8, fontWeight: 600 }}>
          <VesperMark s={12}/> READY WHEN YOU ARE
        </div>
        <h1 style={{
          fontFamily: T.serif, fontWeight: 500, fontSize: 26, lineHeight: 1.05,
          letterSpacing: -0.5, color: T.ink, margin: '10px 0 0',
        }}>
          What are you <span style={{ fontStyle: 'italic' }}>working on,</span><br/>
          Tiger?
        </h1>
      </div>

      {/* THREE FLOATING SUGGESTIONS — orbit the composer ─────── */}
      <div style={{ padding: '24px 16px 0', display: 'flex', flexDirection: 'column', gap: 8 }}>
        {[
          { c: TR.ink,     k: 'NEEDS YOU', t: 'A ryokan for Tokyo, nights 5–7' },
          { c: T.gold,     k: 'I DRAFTED', t: 'Five Lisbon-pattern dinners' },
          { c: TR.dreaming || '#7C8F73', k: 'NOTICED', t: 'You save neighborhoods before landmarks' },
        ].map((s, i) => (
          <div key={i} style={{
            padding: '10px 12px', background: T.cardWarm, borderRadius: 999,
            border: `0.5px solid ${T.hairline}`,
            display: 'grid', gridTemplateColumns: '6px auto 1fr auto', gap: 10, alignItems: 'center',
          }}>
            <span style={{ width: 5, height: 5, borderRadius: 5, background: s.c }}/>
            <span style={{ fontSize: 9, color: s.c, letterSpacing: 1.4, fontWeight: 700 }}>{s.k}</span>
            <span style={{ fontFamily: T.serif, fontSize: 13, color: T.ink, letterSpacing: -0.1, fontWeight: 500 }}>
              {s.t}
            </span>
            <span style={{ fontSize: 11, color: T.mute }}>→</span>
          </div>
        ))}
      </div>

      {/* PROMINENT composer — the centerpiece */}
      <div style={{ padding: '24px 16px 0' }}>
        <Composer placeholder="Tell me what you’re thinking…" prominent/>
        <div style={{
          marginTop: 10, display: 'flex', justifyContent: 'center', gap: 6, flexWrap: 'wrap',
        }}>
          {['plan something', 'find dinner', 'review my week', 'keep a memory'].map((c) => (
            <span key={c} style={{
              padding: '5px 10px', fontFamily: T.serif, fontStyle: 'italic',
              fontSize: 11.5, color: T.inkSoft, background: 'transparent',
              borderRadius: 999, border: `0.5px solid ${T.hairline}`,
            }}>{c}</span>
          ))}
        </div>
      </div>

      {/* RECENT — three thread chips */}
      <div style={{ padding: '24px 22px 0' }}>
        <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between' }}>
          <span style={{ fontSize: 10, color: T.mute, letterSpacing: 2, fontWeight: 600 }}>RECENT THREADS</span>
          <span style={{ fontSize: 10, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 600 }}>ALL · 24</span>
        </div>
        <div style={{ marginTop: 10, display: 'flex', flexDirection: 'column', gap: 6 }}>
          {[
            { trip: 'TOKYO',     when: '2h',  body: 'where to stay near Yanaka quietly' },
            { trip: 'PORTO',     when: 'yest', body: 'when to go with Ana — June or Sept' },
            { trip: 'LISBON',    when: 'mar 14', body: 'a fado room you didn’t tell me about' },
          ].map((t, i) => (
            <div key={i} style={{
              padding: '10px 14px', background: T.cardWarm, borderRadius: 10,
              border: `0.5px solid ${T.hairline}`,
              display: 'grid', gridTemplateColumns: '60px 1fr auto', gap: 10, alignItems: 'center',
            }}>
              <span style={{ fontFamily: T.mono, fontSize: 9, color: T.goldDeep, letterSpacing: 1.4, fontWeight: 600 }}>
                {t.trip}
              </span>
              <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.inkSoft, letterSpacing: -0.05, lineHeight: 1.25 }}>
                “{t.body}”
              </span>
              <span style={{ fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.2, fontWeight: 600 }}>{t.when.toUpperCase()}</span>
            </div>
          ))}
        </div>
      </div>

      <TabBar active="vesper"/>
    </Phone>
  );
}

Object.assign(window, { VesperDesk, VesperBriefing, VesperDialogue });
