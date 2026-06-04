// 03 — MAP, TRAVEL DNA, POSTCARDS detail screens.

// ─── MAP ────────────────────────────────────────────────────────
// Not a literal Mapbox map — an illustrated personal geography.
// Cities as ink dots, trips as ochre routes. Year-ribbon as sidebar.
function V3Map() {
  return (
    <Phone bg={T.bg}>
      <ScreenHeader
        eyebrow="02 · MAP"
        title={<>Where you’ve <span style={{ fontStyle: 'italic' }}>been.</span></>}
        meta="14 cities · 7 countries · a quiet geography"
      />

      {/* illustrated map canvas + vertical year ribbon */}
      <div style={{ padding: '14px 16px 0', display: 'flex', gap: 6 }}>
        {/* sidebar — year ribbon */}
        <div style={{ paddingTop: 10, paddingLeft: 4 }}>
          <YearRibbonV
            height={328}
            items={[
              { m: 'JAN', dot: null },
              { m: 'FEB', dot: 'past', label: 'Porto' },
              { m: 'MAR', dot: 'now',  label: 'Lisbon' },
              { m: 'APR', dot: null },
              { m: 'MAY', dot: 'planned', label: 'Tokyo' },
              { m: 'JUN', dot: null },
              { m: 'JUL', dot: null },
              { m: 'AUG', dot: 'past', label: 'CDMX' },
              { m: 'SEP', dot: null },
              { m: 'OCT', dot: 'past', label: 'Porto' },
              { m: 'NOV', dot: null },
              { m: 'DEC', dot: null },
            ]}
          />
        </div>

        {/* illustrated map */}
        <div style={{
          flex: 1, background: T.cardWarm, borderRadius: 14,
          padding: 14, position: 'relative', height: 350, overflow: 'hidden',
          boxShadow: '0 0 0 0.5px rgba(27,23,20,0.05), 0 1px 0 rgba(255,255,255,0.6) inset',
        }}>
          {/* faint cartographic grid */}
          <svg style={{ position: 'absolute', inset: 0, width: '100%', height: '100%', opacity: 0.5 }} viewBox="0 0 220 320" preserveAspectRatio="none">
            {/* parallels */}
            <path d="M0 60 Q110 50 220 60" stroke={T.muteSoft} strokeWidth="0.4" fill="none" opacity="0.45"/>
            <path d="M0 130 Q110 124 220 130" stroke={T.muteSoft} strokeWidth="0.4" fill="none" opacity="0.45"/>
            <path d="M0 200 Q110 196 220 200" stroke={T.muteSoft} strokeWidth="0.4" fill="none" opacity="0.45"/>
            <path d="M0 270 Q110 268 220 270" stroke={T.muteSoft} strokeWidth="0.4" fill="none" opacity="0.45"/>
            {/* meridians */}
            <path d="M55 0 Q60 160 55 320" stroke={T.muteSoft} strokeWidth="0.4" fill="none" opacity="0.4"/>
            <path d="M165 0 Q160 160 165 320" stroke={T.muteSoft} strokeWidth="0.4" fill="none" opacity="0.4"/>
            {/* routes */}
            <path d="M40 90 Q70 130 100 170 Q130 200 160 240" stroke={T.gold} strokeWidth="1.4" strokeDasharray="2 3" fill="none" strokeLinecap="round"/>
            <path d="M40 90 Q90 70 150 95" stroke={T.gold} strokeWidth="1.4" strokeDasharray="2 3" fill="none" strokeLinecap="round"/>
            <path d="M100 170 Q40 220 60 280" stroke={T.gold} strokeWidth="1" strokeDasharray="1 4" fill="none" strokeLinecap="round" opacity="0.7"/>
          </svg>

          {/* pins */}
          {[
            { l: 30, t: 65,  label: 'Porto',    sub: 'twice',   now: false },
            { l: 100, t: 50, label: 'Paris',    sub: '1 trip',  now: false },
            { l: 160, t: 80, label: 'Berlin',   sub: '1 trip',  now: false },
            { l: 36,  t: 145, label: 'Lisbon',  sub: 'now',     now: true },
            { l: 110, t: 175, label: 'CDMX',    sub: '6 days',  now: false },
            { l: 80,  t: 245, label: 'Bangkok', sub: '1 trip',  now: false },
            { l: 158, t: 260, label: 'Tokyo',   sub: 'planned', planned: true },
          ].map((p, i) => (
            <div key={i} style={{
              position: 'absolute', left: p.l, top: p.t,
              transform: 'translate(-50%, -50%)',
              display: 'flex', alignItems: 'center', gap: 5,
            }}>
              {p.now && (
                <div style={{
                  position: 'absolute', width: 22, height: 22, borderRadius: 999,
                  background: T.gold, opacity: 0.18, left: -2, top: -2,
                }}/>
              )}
              {p.planned ? (
                <div style={{ width: 7, height: 7, borderRadius: 999, border: `1px solid ${T.gold}`, background: T.cardWarm }}/>
              ) : (
                <div style={{
                  width: p.now ? 8 : 5, height: p.now ? 8 : 5, borderRadius: 999,
                  background: p.now ? T.gold : T.ink, position: 'relative', zIndex: 1,
                }}/>
              )}
              <div style={{
                fontFamily: T.serif, fontSize: 11, color: p.now ? T.ink : T.inkSoft,
                fontStyle: p.planned ? 'italic' : 'normal', fontWeight: p.now ? 600 : 500,
                whiteSpace: 'nowrap', lineHeight: 1, letterSpacing: -0.1,
              }}>
                {p.label}
                <span style={{ display: 'block', fontSize: 8.5, color: T.muteSoft, fontStyle: 'italic', marginTop: 1, fontWeight: 500 }}>
                  {p.sub}
                </span>
              </div>
            </div>
          ))}
          {/* compass corner */}
          <div style={{ position: 'absolute', bottom: 8, right: 10, fontFamily: T.serif, fontStyle: 'italic', fontSize: 10, color: T.muteSoft, letterSpacing: 0.8 }}>
            N ↑
          </div>
        </div>
      </div>

      {/* below — small "places remembered" strip */}
      <div style={{ padding: '14px 22px 0' }}>
        <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between' }}>
          <Eyebrow>PLACES REMEMBERED</Eyebrow>
          <span style={{ fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.5, fontWeight: 600 }}>SCROLL</span>
        </div>
        <div style={{ display: 'flex', gap: 8, marginTop: 10, overflow: 'hidden' }}>
          {[
            { name: 'Alfama',  sub: 'a step you keep returning to' },
            { name: 'Ribeira', sub: 'three walks, no bridge' },
            { name: 'Roma Nte.', sub: 'breakfast at La Esquina' },
            { name: 'Shimokita', sub: 'planned' },
          ].map((p, i) => (
            <div key={i} style={{
              flex: '0 0 auto', width: 110, padding: '10px 12px',
              background: T.cardWarm, borderRadius: 10, border: `0.5px solid ${T.hairline}`,
            }}>
              <div style={{ fontFamily: T.serif, fontSize: 13, fontWeight: 500, color: T.ink, letterSpacing: -0.1 }}>
                {p.name}
              </div>
              <div style={{ fontSize: 9.5, color: T.muteSoft, fontStyle: 'italic', fontFamily: T.serif, marginTop: 3, lineHeight: 1.3 }}>
                {p.sub}
              </div>
            </div>
          ))}
        </div>
      </div>

      <TabBar active="atlas"/>
    </Phone>
  );
}

// ─── TRAVEL DNA ─────────────────────────────────────────────────
function V3DNA() {
  return (
    <Phone bg={T.bg}>
      <ScreenHeader
        eyebrow="03 · TRAVEL DNA"
        title={<>A reading,<br/><span style={{ fontStyle: 'italic' }}>by Vesper.</span></>}
        meta="from 41 entries · last refined 03·12"
      />

      {/* central fingerprint with curving phrases */}
      <div style={{ padding: '8px 22px 0', position: 'relative', height: 220 }}>
        <div style={{ position: 'absolute', inset: 0, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <Marks.DNA size={170}/>
        </div>
        {/* curving labels */}
        <div style={{
          position: 'absolute', top: 18, left: 22,
          fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.inkSoft,
          transform: 'rotate(-6deg)', letterSpacing: -0.1,
        }}>early-morning soul</div>
        <div style={{
          position: 'absolute', top: 28, right: 22,
          fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.inkSoft,
          transform: 'rotate(5deg)', letterSpacing: -0.1,
        }}>follows the river</div>
        <div style={{
          position: 'absolute', bottom: 28, left: 30,
          fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.inkSoft,
          transform: 'rotate(-3deg)',
        }}>returns before exploring</div>
        <div style={{
          position: 'absolute', bottom: 18, right: 26,
          fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.goldDeep,
          transform: 'rotate(4deg)',
        }}>slow.</div>
      </div>

      {/* pull-quote summary */}
      <div style={{
        margin: '0 22px', padding: '14px 0',
        borderTop: `0.5px solid ${T.hairline}`, borderBottom: `0.5px solid ${T.hairline}`,
      }}>
        <p style={{
          fontFamily: T.serif, fontSize: 16, color: T.ink, margin: 0, lineHeight: 1.4, letterSpacing: -0.15,
        }}>
          “You follow the neighborhood before the landmark, and the river before
          the museum. You return to one step three times before you find the next.”
        </p>
        <div style={{ marginTop: 8, color: T.muteSoft, fontSize: 9.5, letterSpacing: 1.6, fontWeight: 600 }}>
          — VESPER, READING YOU
        </div>
      </div>

      {/* rituals */}
      <div style={{ padding: '14px 22px 0' }}>
        <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between' }}>
          <Eyebrow>SIX RITUALS</Eyebrow>
          <span style={{ fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.5, fontWeight: 600 }}>EDIT</span>
        </div>
        <div style={{
          marginTop: 10, display: 'grid', gridTemplateColumns: '1fr 1fr',
          gap: 6,
        }}>
          {[
            ['I',   'First coffee, never famous'],
            ['II',  'Walks before maps'],
            ['III', 'One dinner alone'],
            ['IV',  'Rivers at dusk'],
            ['V',   'Same step, three mornings'],
            ['VI',  'Bookshop before bar'],
          ].map(([n, t]) => (
            <div key={n} style={{
              display: 'flex', alignItems: 'center', gap: 8,
              padding: '8px 10px', borderTop: `0.5px solid ${T.hairThin}`,
            }}>
              <span style={{
                fontFamily: T.serif, fontStyle: 'italic', fontSize: 12,
                color: T.gold, width: 18,
              }}>{n}.</span>
              <span style={{ fontFamily: T.serif, fontSize: 12.5, color: T.inkSoft, letterSpacing: -0.1, lineHeight: 1.2 }}>
                {t}
              </span>
            </div>
          ))}
        </div>
      </div>

      <TabBar active="atlas"/>
    </Phone>
  );
}

// ─── POSTCARDS ──────────────────────────────────────────────────
// The shelf. The draft on the desk lives here too, gently highlighted.
function V3Postcards() {
  return (
    <Phone bg={T.bg}>
      <ScreenHeader
        eyebrow="04 · POSTCARDS"
        title={<>The <span style={{ fontStyle: 'italic' }}>shelf.</span></>}
        meta="0 sent · 1 draft on your desk · 41 entries waiting to become one"
      />

      {/* mini Vesper callout — draft preview */}
      <div style={{ padding: '14px 22px 0' }}>
        <div style={{
          background: T.cardWarm, borderRadius: 14, padding: 12,
          display: 'flex', gap: 12, alignItems: 'center',
          border: `0.8px solid ${T.gold}`,
        }}>
          <div style={{ width: 56, height: 72, transform: 'rotate(-3deg)', flexShrink: 0 }}>
            <Postcard scene="lisbon" height="100%" stamp={false}/>
          </div>
          <div style={{ flex: 1 }}>
            <Eyebrow color={T.goldDeep}>VESPER · ON YOUR DESK</Eyebrow>
            <div style={{ fontFamily: T.serif, fontSize: 17, color: T.ink, fontWeight: 500, letterSpacing: -0.2, marginTop: 4, lineHeight: 1.1 }}>
              Lisbon, the slow way
            </div>
            <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 11.5, color: T.mute, marginTop: 3 }}>
              keep it, refine, or not this time
            </div>
          </div>
          <Marks.ArrowR s={14} c={T.goldDeep}/>
        </div>
      </div>

      {/* the shelf — a 2-col grid: 1 draft + 3 placeholders */}
      <div style={{ padding: '14px 22px 0' }}>
        <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between' }}>
          <Eyebrow>YOUR SHELF</Eyebrow>
          <span style={{ fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.5, fontWeight: 600 }}>EMPTY · ROOM TO GROW</span>
        </div>

        {/* "wooden shelf" — a paper plate with a hairline ledge */}
        <div style={{
          marginTop: 12, padding: '14px 12px 18px', background: T.cardSoft, borderRadius: 10,
          border: `0.5px solid ${T.hairline}`,
          backgroundImage: `linear-gradient(${T.bg}, ${T.bg}), linear-gradient(${T.bg}, ${T.bg})`,
        }}>
          <div style={{
            display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: 8,
            alignItems: 'flex-end',
          }}>
            {/* the one real draft */}
            <div style={{ transform: 'rotate(-2.2deg)' }}>
              <Postcard scene="lisbon" height={110} stamp={false}/>
              <div style={{ fontFamily: T.serif, fontSize: 10.5, color: T.ink, fontStyle: 'italic', marginTop: 6, textAlign: 'center' }}>
                Lisbon · draft
              </div>
            </div>
            {[1, 2].map((i) => (
              <div key={i} style={{ transform: `rotate(${i === 1 ? 1.4 : -0.6}deg)` }}>
                <div style={{
                  height: 110, borderRadius: 4, background: T.cardWarm,
                  border: `1px dashed ${T.muteSoft}`,
                  display: 'flex', alignItems: 'center', justifyContent: 'center',
                  color: T.muteSoft, fontFamily: T.serif, fontStyle: 'italic', fontSize: 11,
                  letterSpacing: 0.2, textAlign: 'center', padding: 8,
                }}>
                  a place will land here
                </div>
                <div style={{ height: 14 }}/>
              </div>
            ))}
          </div>
          {/* shelf ledge */}
          <div style={{
            height: 0.5, background: T.hairline, margin: '10px -12px 0',
          }}/>
        </div>

        {/* second shelf — older entries waiting to become postcards */}
        <div style={{
          marginTop: 14, padding: '14px 12px 18px', background: T.cardSoft, borderRadius: 10,
          border: `0.5px solid ${T.hairline}`,
        }}>
          <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginBottom: 8 }}>
            <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.mute }}>
              Waiting in the inbox
            </span>
            <span style={{ fontFamily: T.mono, fontSize: 10, color: T.muteSoft, letterSpacing: 1.2 }}>41</span>
          </div>
          <div style={{ display: 'flex', gap: 6 }}>
            {Array.from({ length: 8 }).map((_, i) => (
              <div key={i} style={{
                flex: 1, height: 24,
                background: T.cardWarm, borderRadius: 2,
                border: `0.4px solid ${T.hairline}`,
                position: 'relative',
              }}>
                <div style={{
                  position: 'absolute', top: 4, left: 4, right: 4, height: 4,
                  background: T.muteSoft, opacity: 0.25, borderRadius: 1,
                }}/>
                <div style={{
                  position: 'absolute', top: 12, left: 4, right: 8, height: 2.5,
                  background: T.muteSoft, opacity: 0.2, borderRadius: 1,
                }}/>
                <div style={{
                  position: 'absolute', top: 17, left: 4, right: 12, height: 2.5,
                  background: T.muteSoft, opacity: 0.2, borderRadius: 1,
                }}/>
              </div>
            ))}
          </div>
        </div>
      </div>

      <TabBar active="atlas"/>
    </Phone>
  );
}

Object.assign(window, { V3Map, V3DNA, V3Postcards });
