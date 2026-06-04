// 03 · Auxiliary screens reachable from the Atlas top bar:
//   - V3Profile  : the avatar tap-target (a "you" page, not a settings page)
//   - V3Search   : the magnifier tap-target (find a memory, not a query box)
//   - V3Add      : the + tap-target (save a memory — multiple intakes)

function V3Profile() {
  return (
    <Phone bg={T.bg}>
      <ScreenHeader
        eyebrow="ATLAS · YOU"
        title={<>Tiger,<br/><span style={{ fontStyle: 'italic' }}>in their own words.</span></>}
        meta="kept by Vesper since March ’24"
        right={
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="1.6" strokeLinecap="round">
            <circle cx="5" cy="12" r="1.2"/><circle cx="12" cy="12" r="1.2"/><circle cx="19" cy="12" r="1.2"/>
          </svg>
        }
      />

      {/* "Self-portrait" — a large avatar surrounded by tiny stamps of formative places */}
      <div style={{ padding: '18px 22px 0', position: 'relative', height: 200 }}>
        <div style={{
          position: 'absolute', left: '50%', top: 14, transform: 'translateX(-50%)',
          width: 116, height: 116, borderRadius: 999, background: T.goldDeep,
          color: T.cardWarm, fontFamily: T.serif, fontWeight: 400, fontSize: 54,
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          letterSpacing: -1, boxShadow: '0 18px 32px -16px rgba(0,0,0,0.3)',
        }}>T</div>

        {/* tiny "stamp" badges around the avatar — formative places */}
        {[
          { l: 26,  t: 22,  label: 'LISBON',   r: -6 },
          { l: 270, t: 18,  label: 'PORTO',    r: 6 },
          { l: 18,  t: 130, label: 'BANGKOK',  r: 2 },
          { l: 280, t: 124, label: 'CDMX',     r: -4 },
        ].map((s, i) => (
          <div key={i} style={{
            position: 'absolute', left: s.l, top: s.t,
            transform: `rotate(${s.r}deg)`,
            padding: '2px 7px', border: `0.8px dashed ${T.gold}`,
            borderRadius: 2, color: T.goldDeep, fontFamily: T.mono,
            fontSize: 8.5, letterSpacing: 1.4, fontWeight: 500,
            background: 'rgba(250,246,234,0.7)',
          }}>{s.label}</div>
        ))}
      </div>

      {/* "How Vesper sees you" — italic prose */}
      <div style={{ padding: '4px 24px 0' }}>
        <Eyebrow>HOW VESPER SEES YOU</Eyebrow>
        <p style={{
          fontFamily: T.serif, fontSize: 15, color: T.inkSoft, lineHeight: 1.45,
          margin: '8px 0 0', letterSpacing: -0.1,
        }}>
          An <em>early-morning soul</em> who follows the neighborhood before
          the landmark. Returns to one step three times before exploring a fourth.
          Travels slow, writes little, remembers a lot.
        </p>
      </div>

      <Hairline m="18px 24px"/>

      {/* Your taste — chips */}
      <div style={{ padding: '0 22px' }}>
        <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between' }}>
          <Eyebrow>YOUR TASTE</Eyebrow>
          <span style={{ fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.5, fontWeight: 600 }}>VESPER LEARNS</span>
        </div>
        <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap', marginTop: 10 }}>
          {['slow streets','river over harbor','one dinner alone','bookshops','no chains','dusk light','tile patterns'].map((t, i) => (
            <span key={i} style={{
              padding: '5px 10px', fontFamily: T.serif, fontStyle: 'italic',
              fontSize: 12, color: T.inkSoft, background: T.cardWarm,
              borderRadius: 999, border: `0.5px solid ${T.hairline}`,
            }}>{t}</span>
          ))}
          <span style={{
            padding: '5px 10px', fontFamily: T.serif, fontStyle: 'italic',
            fontSize: 12, color: T.goldDeep, background: 'transparent',
            borderRadius: 999, border: `0.6px dashed ${T.gold}`,
          }}>+ teach Vesper</span>
        </div>
      </div>

      {/* Your rhythm — when Vesper writes */}
      <div style={{ padding: '14px 22px 0' }}>
        <Eyebrow>YOUR RHYTHM</Eyebrow>
        <div style={{
          marginTop: 10, padding: '14px 16px', background: T.cardWarm, borderRadius: 12,
          border: `0.5px solid ${T.hairline}`,
        }}>
          <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between' }}>
            <span style={{ fontFamily: T.serif, fontSize: 15, color: T.ink, fontWeight: 500, letterSpacing: -0.2 }}>
              Vesper writes you <span style={{ fontStyle: 'italic' }}>weekly</span>
            </span>
            <span style={{ fontFamily: T.mono, fontSize: 10, color: T.muteSoft, letterSpacing: 1.2 }}>SUN · 10 AM</span>
          </div>
          <div style={{ marginTop: 10, display: 'flex', gap: 4 }}>
            {['daily','weekly','fortnightly','quiet'].map((r, i) => (
              <span key={r} style={{
                flex: 1, textAlign: 'center', padding: '6px 0',
                fontSize: 10.5, letterSpacing: 1.2, fontWeight: 600,
                color: i === 1 ? T.ink : T.muteSoft,
                background: i === 1 ? T.bg : 'transparent',
                borderRadius: 6, textTransform: 'uppercase',
                border: i === 1 ? `0.5px solid ${T.hairline}` : '0.5px solid transparent',
              }}>{r}</span>
            ))}
          </div>
        </div>
      </div>

      {/* Quiet utility row */}
      <div style={{
        position: 'absolute', bottom: 96, left: 22, right: 22,
        display: 'flex', justifyContent: 'space-between',
        fontSize: 11, color: T.muteSoft, letterSpacing: 1.5, fontWeight: 600,
      }}>
        <span>ARCHIVE · 41</span>
        <span>EXPORTED · 0</span>
        <span>SIGN OUT</span>
      </div>

      <TabBar active="atlas"/>
    </Phone>
  );
}

function V3Search() {
  return (
    <Phone bg={T.bg}>
      <ScreenHeader
        eyebrow="ATLAS · SEARCH"
        title={<>Find a <span style={{ fontStyle: 'italic' }}>memory.</span></>}
        meta="places, drafts, rituals, things you almost forgot"
      />

      {/* paper search input */}
      <div style={{ padding: '14px 22px 0' }}>
        <div style={{
          padding: '14px 16px', background: T.cardWarm, borderRadius: 12,
          border: `0.5px solid ${T.hairline}`,
          display: 'flex', alignItems: 'center', gap: 10,
        }}>
          <Marks.Search s={18} c={T.mute}/>
          <span style={{
            fontFamily: T.serif, fontStyle: 'italic', fontSize: 16, color: T.muteSoft,
            letterSpacing: -0.1, flex: 1,
          }}>
            a place, a season, a person…
          </span>
          <span style={{
            fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1.3,
            padding: '3px 6px', border: `0.5px solid ${T.hairline}`, borderRadius: 3,
          }}>RETURN</span>
        </div>
      </div>

      {/* Recent */}
      <div style={{ padding: '18px 22px 0' }}>
        <Eyebrow>RECENT</Eyebrow>
        <div style={{ display: 'flex', gap: 6, marginTop: 10, flexWrap: 'wrap' }}>
          {['lisbon', 'fado', 'porto bridges', 'morning coffee', 'march ’25'].map((t, i) => (
            <span key={t} style={{
              padding: '5px 10px', fontFamily: T.serif, fontStyle: 'italic',
              fontSize: 12, color: T.inkSoft, background: T.cardWarm,
              borderRadius: 999, border: `0.5px solid ${T.hairline}`,
              display: 'flex', alignItems: 'center', gap: 5,
            }}>
              <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke={T.muteSoft} strokeWidth="1.5" strokeLinecap="round">
                <circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>
              </svg>
              {t}
            </span>
          ))}
        </div>
      </div>

      {/* Or wander by... */}
      <div style={{ padding: '20px 22px 0' }}>
        <Eyebrow>OR WANDER BY…</Eyebrow>
        <div style={{
          display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8, marginTop: 10,
        }}>
          {[
            { eb: 'BY · PLACE',  t: 'Cities',     sub: '14 you’ve known' },
            { eb: 'BY · SEASON', t: 'Time',       sub: 'march ’24 → today' },
            { eb: 'BY · RITUAL', t: 'Patterns',   sub: '6 things you repeat' },
            { eb: 'BY · WITH',   t: 'Together',   sub: 'people, occasionally' },
          ].map((c, i) => (
            <div key={i} style={{
              padding: '14px 14px 12px', background: T.cardWarm, borderRadius: 12,
              border: `0.5px solid ${T.hairline}`, minHeight: 88,
              boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset',
            }}>
              <Eyebrow color={T.goldDeep}>{c.eb}</Eyebrow>
              <div style={{
                fontFamily: T.serif, fontSize: 19, fontWeight: 500, color: T.ink,
                letterSpacing: -0.3, lineHeight: 1, marginTop: 6,
              }}>{c.t}</div>
              <div style={{
                fontFamily: T.serif, fontStyle: 'italic', fontSize: 11.5, color: T.mute,
                marginTop: 4,
              }}>{c.sub}</div>
            </div>
          ))}
        </div>
      </div>

      {/* Ask Vesper */}
      <div style={{ padding: '14px 22px 0' }}>
        <div style={{
          padding: '14px 16px', background: T.cardSoft, borderRadius: 12,
          border: `0.8px dashed ${T.gold}`,
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
            <span style={{ width: 5, height: 5, borderRadius: 5, background: T.gold }}/>
            <Eyebrow color={T.goldDeep}>OR ASK VESPER</Eyebrow>
          </div>
          <div style={{
            marginTop: 8, fontFamily: T.serif, fontStyle: 'italic', fontSize: 15,
            color: T.inkSoft, letterSpacing: -0.1, lineHeight: 1.35,
          }}>
            “what did I love about Lisbon?”
          </div>
        </div>
      </div>

      <TabBar active="atlas"/>
    </Phone>
  );
}

function V3Add() {
  return (
    <Phone bg={T.bg}>
      <ScreenHeader
        eyebrow="ATLAS · ADD"
        title={<>Save a <span style={{ fontStyle: 'italic' }}>memory.</span></>}
        meta="vesper will keep it · turn it into something later"
        right={
          <span style={{ fontSize: 12, color: T.inkSoft, fontWeight: 500, letterSpacing: -0.1 }}>
            Cancel
          </span>
        }
      />

      {/* Five intake objects as a curio row */}
      <div style={{ padding: '14px 16px 0' }}>
        <Eyebrow>HOW SHOULD IT ARRIVE?</Eyebrow>
        <div style={{
          marginTop: 10, display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8,
        }}>
          {[
            {
              eb: 'A PHOTO', t: 'Drop an image',
              sub: 'Vesper reads place + light',
              mark: (
                <svg width="42" height="42" viewBox="0 0 48 48" fill="none" stroke={T.ink} strokeWidth="1.2" strokeLinecap="round">
                  <rect x="6" y="11" width="36" height="28" rx="2"/>
                  <path d="M14 11l3-5h14l3 5"/>
                  <circle cx="24" cy="25" r="7"/>
                </svg>
              ),
              accent: true,
            },
            {
              eb: 'A PLACE', t: 'Drop a pin',
              sub: 'a corner, not a country',
              mark: (
                <svg width="42" height="42" viewBox="0 0 48 48" fill="none" stroke={T.ink} strokeWidth="1.2" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M24 6c-7 0-12 5-12 12 0 9 12 22 12 22s12-13 12-22c0-7-5-12-12-12Z"/>
                  <circle cx="24" cy="18" r="4" fill={T.gold} stroke="none"/>
                </svg>
              ),
            },
            {
              eb: 'A NOTE', t: 'Write a line',
              sub: 'one sentence is enough',
              mark: (
                <svg width="42" height="42" viewBox="0 0 48 48" fill="none" stroke={T.ink} strokeWidth="1.2" strokeLinecap="round">
                  <path d="M8 38l3-9 21-21 6 6-21 21-9 3Z"/>
                  <path d="M28 11l6 6"/>
                </svg>
              ),
            },
            {
              eb: 'A VOICE', t: 'Whisper it',
              sub: 'Vesper transcribes loosely',
              mark: (
                <svg width="42" height="42" viewBox="0 0 48 48" fill="none" stroke={T.ink} strokeWidth="1.2" strokeLinecap="round">
                  <rect x="19" y="8" width="10" height="20" rx="5"/>
                  <path d="M12 22c0 7 5 12 12 12s12-5 12-12"/>
                  <path d="M24 34v6M18 40h12"/>
                </svg>
              ),
            },
            {
              eb: 'A SCRAP', t: 'Scan a thing',
              sub: 'receipts, tickets, napkins',
              mark: (
                <svg width="42" height="42" viewBox="0 0 48 48" fill="none" stroke={T.ink} strokeWidth="1.2" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M12 6h18l8 8v28H12z"/>
                  <path d="M30 6v8h8"/>
                  <path d="M18 24h16M18 30h16M18 36h10"/>
                </svg>
              ),
              wide: true,
            },
          ].map((it, i) => (
            <div key={i} style={{
              padding: '14px 14px', background: T.cardWarm, borderRadius: 14,
              border: it.accent ? `0.8px solid ${T.gold}` : `0.5px solid ${T.hairline}`,
              gridColumn: it.wide ? 'span 2' : 'auto',
              display: 'flex', flexDirection: it.wide ? 'row' : 'column',
              gap: 12, alignItems: it.wide ? 'center' : 'flex-start',
              boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset',
              position: 'relative',
            }}>
              <div style={{ opacity: 0.9 }}>{it.mark}</div>
              <div style={{ flex: 1 }}>
                <Eyebrow color={it.accent ? T.goldDeep : T.mute}>{it.eb}</Eyebrow>
                <div style={{
                  fontFamily: T.serif, fontSize: 17, color: T.ink, fontWeight: 500,
                  letterSpacing: -0.2, marginTop: 4, lineHeight: 1,
                }}>{it.t}</div>
                <div style={{
                  fontFamily: T.serif, fontStyle: 'italic', fontSize: 11.5, color: T.mute,
                  marginTop: 4,
                }}>{it.sub}</div>
              </div>
              {it.accent && (
                <div style={{
                  position: 'absolute', top: 10, right: 10,
                  background: T.gold, color: T.cardWarm, fontSize: 8, fontWeight: 700,
                  letterSpacing: 1.2, padding: '2px 6px', borderRadius: 2,
                }}>QUICK</div>
              )}
            </div>
          ))}
        </div>
      </div>

      {/* Or let Vesper draft */}
      <div style={{ padding: '14px 22px 0' }}>
        <div style={{
          padding: '14px 16px', background: T.cardSoft, borderRadius: 12,
          border: `0.8px dashed ${T.gold}`,
        }}>
          <Eyebrow color={T.goldDeep}>OR · LET VESPER DRAFT</Eyebrow>
          <div style={{
            marginTop: 8, fontFamily: T.serif, fontStyle: 'italic', fontSize: 15,
            color: T.inkSoft, lineHeight: 1.35, letterSpacing: -0.1,
          }}>
            “make a postcard from <span style={{ color: T.goldDeep }}>last weekend in Porto</span>”
          </div>
          <div style={{
            marginTop: 10, display: 'flex', alignItems: 'center', justifyContent: 'space-between',
          }}>
            <span style={{ fontSize: 10, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 600 }}>
              VESPER WILL USE 7 ENTRIES
            </span>
            <Marks.ArrowR s={13} c={T.goldDeep}/>
          </div>
        </div>
      </div>

      <TabBar active="atlas"/>
    </Phone>
  );
}

Object.assign(window, { V3Profile, V3Search, V3Add });
