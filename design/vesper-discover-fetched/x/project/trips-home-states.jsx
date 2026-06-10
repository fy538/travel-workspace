// Trips home — the HYBRID, expanded across every real state.
// One layout grammar (A · Planning Table) auto-switches at the extremes:
//   · 0 upcoming dated trips     → COLD (C · Dream Stack pattern)
//   · 4+ active drafts            → FREQUENT (drafts become B's serif rows)
//   · currently on a trip         → LIVE (hero turns to a "today" card)
//   · trip ended < 14 days ago    → RETURNED (Atlas bridge promoted)
//   · otherwise                   → DEFAULT (the canvas state)

// ─── COLD START · no upcoming dated trips ───────────────────────
function HomeCold() {
  return (
    <Phone bg={T.bg}>
      <TripsTopBar eyebrow="TRIPS · DREAMING"/>

      {/* Vesper's voice — carries the room */}
      <div style={{ padding: '20px 24px 0' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 7 }}>
          <TripIcons.Sparkle s={13}/>
          <span style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 2.2, color: T.goldDeep, fontWeight: 600 }}>VESPER</span>
        </div>
        <h1 style={{ fontFamily: T.serif, fontWeight: 500, fontSize: 33, lineHeight: 1.05, letterSpacing: -0.9, color: T.ink, margin: '12px 0 0' }}>
          The year’s still <span style={{ fontStyle: 'italic' }}>unwritten.</span> Where do we begin?
        </h1>
      </div>

      {/* the first dream — a real postcard, waiting to be filled */}
      <div style={{ padding: '32px 22px 0', position: 'relative', height: 206 }}>
        <div style={{ position: 'absolute', left: 42, right: 42, top: 12, bottom: 8, transform: 'rotate(-1.6deg)' }}>
          <Postcard blank stamp height="100%"
            title="A place you keep imagining"
            sub="whisper one to Vesper"
            date="—·—·26"/>
        </div>
      </div>

      {/* a couple of dreams in Vesper's taste — route into Begin */}
      <div style={{ padding: '20px 24px 0' }}>
        <div style={{ fontFamily: T.mono, fontSize: 8.5, letterSpacing: 1.6, color: T.muteSoft, fontWeight: 600 }}>OR, SOMEWHERE FOR YOUR TASTE</div>
        <DreamSeeds/>
      </div>

      {/* the year, still open */}
      <div style={{ position: 'absolute', left: 24, right: 24, bottom: 152 }}>
        <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginBottom: 9 }}>
          <span style={{ fontFamily: T.mono, fontSize: 9, color: T.mute, letterSpacing: 1.8, fontWeight: 600 }}>YOUR YEAR · ’26</span>
          <span style={{ fontFamily: T.mono, fontSize: 8.5, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 600 }}>STILL OPEN</span>
        </div>
        <div style={{ position: 'relative', height: 10 }}>
          <div style={{ position: 'absolute', left: 2, right: 2, top: '50%', borderTop: `1px dashed ${T.faint}`, transform: 'translateY(-50%)' }}/>
          <div style={{ position: 'absolute', inset: 0, display: 'grid', gridTemplateColumns: 'repeat(12,1fr)' }}>
            {Array.from({ length: 12 }).map((_, i) => (
              <div key={i} style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                <div style={{ width: 2.5, height: 2.5, borderRadius: 999, background: T.faint, boxShadow: `0 0 0 3px ${T.bg}` }}/>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* one clear way in */}
      <div style={{ position: 'absolute', left: 22, right: 22, bottom: 90 }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 8, padding: '14px 0', background: T.cardWarm, borderRadius: 14, border: `0.5px solid ${T.hairline}` }}>
          <span style={{ fontFamily: T.serif, fontSize: 16, color: T.ink, fontWeight: 500, letterSpacing: -0.2 }}>Begin a trip</span>
          <Marks.ArrowR s={14} c={T.goldDeep}/>
        </div>
      </div>

      <TabBar active="trips"/>
    </Phone>
  );
}

// ─── DEFAULT · the canvas state (1–3 trips, one alive) ──────────
function HomeDefault() {
  return (
    <Phone bg={T.bg}>
      <TripsTopBar eyebrow="TRIPS · 3 · MARCH ’26"/>
      <PlanningTitle pill={<TripPill kind="alive">1 ALIVE</TripPill>}
                     meta="2 drafts · 1 dreaming"/>
      <HeroAliveTrip
        title="Tokyo, in May"
        days="Sat 14 → Fri 22"
        nights="8 NIGHTS"
        countdown="ALIVE · 58 DAYS OUT"
        scene="tokyo"
        next="Pick a ryokan for nights 5–7"
      />
      <DraftsScatter rows={[
        { title: 'Porto, return', meta: 'september · pencilled in', kind: 'alive',    pillText: 'PENCILLED', tilt: 1.2 },
        { title: 'A weekend somewhere quiet', meta: 'no dates · 1 traveler', kind: 'dreaming', pillText: 'DREAMING', tilt: -1.6 },
      ]}/>
      <AtlasBridge body="Vesper has a postcard waiting from Lisbon." kicker="LAST TRIP · LISBON"/>
      <TabBar active="trips"/>
    </Phone>
  );
}

// ─── ON TRIP · you're there right now ───────────────────────────
function HomeOnTrip() {
  return (
    <Phone bg={T.bg}>
      <TripsTopBar eyebrow="TRIPS · DAY 3 IN TOKYO"/>

      <div style={{ padding: '18px 22px 0' }}>
        <h1 style={{
          fontFamily: T.serif, fontWeight: 500, fontSize: 38, lineHeight: 0.96,
          letterSpacing: -1, color: T.ink, margin: 0,
        }}>
          You’re in Tokyo.
        </h1>
        <div style={{
          marginTop: 8, fontSize: 11.5, color: T.mute, fontFamily: T.serif,
        }}>
          monday, march 16 · day 3 of 8 · the morning is yours.
        </div>
      </div>

      {/* Live hero — Today */}
      <div style={{ padding: '16px 16px 0' }}>
        <div style={{
          background: T.cardWarm, borderRadius: 18, padding: '14px',
          boxShadow: '0 16px 32px -18px rgba(0,0,0,0.18), 0 0 0 0.5px rgba(27,23,20,0.06)',
          position: 'relative', overflow: 'hidden',
        }}>
          {/* live tag row */}
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
            <span style={{
              display: 'inline-flex', alignItems: 'center', gap: 6,
              padding: '3px 10px', borderRadius: 999,
              fontSize: 9.5, letterSpacing: 1.6, fontWeight: 700,
              color: T.cardWarm, background: TR.ink,
            }}>
              <span style={{ width: 6, height: 6, borderRadius: 6, background: '#E5C16F',
                boxShadow: `0 0 0 3px rgba(229,193,111,0.25)` }}/>
              LIVE · DAY 3
            </span>
            <span style={{ fontFamily: T.mono, fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.2 }}>
              MON · 09:41 JST
            </span>
          </div>

          {/* Today's posture */}
          <h2 style={{
            fontFamily: T.serif, fontWeight: 500, fontSize: 24, color: T.ink,
            margin: '14px 0 6px', letterSpacing: -0.4, lineHeight: 1.05,
          }}>
            You’re due for <span style={{ fontStyle: 'italic' }}>one quiet hour.</span>
          </h2>
          <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.mute, lineHeight: 1.4 }}>
            Vesper noticed you haven’t walked anywhere slow yet today.
          </div>

          {/* today's strip */}
          <div style={{
            marginTop: 14, display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 6,
          }}>
            {[
              { time: 'NOW',     label: 'Coffee',           sub: 'Bear Pond, 6 min', live: true },
              { time: 'AFTERN.', label: 'Senso-ji',         sub: 'saved by you' },
              { time: 'TONIGHT', label: 'Dinner alone?',    sub: '— no plan' },
            ].map((c, i) => (
              <div key={i} style={{
                padding: '10px 10px', background: c.live ? 'rgba(61,80,102,0.10)' : T.bg,
                borderRadius: 10, border: c.live ? `0.6px solid ${TR.ink}` : `0.5px solid ${T.hairline}`,
              }}>
                <div style={{ fontSize: 9, color: c.live ? TR.inkDeep : T.mute, letterSpacing: 1.4, fontWeight: 700 }}>
                  {c.time}
                </div>
                <div style={{
                  fontFamily: T.serif, fontSize: 14, fontWeight: 500, color: T.ink,
                  letterSpacing: -0.2, lineHeight: 1.05, marginTop: 4,
                }}>{c.label}</div>
                <div style={{ fontSize: 10, color: T.muteSoft, fontFamily: T.serif, marginTop: 3 }}>
                  {c.sub}
                </div>
              </div>
            ))}
          </div>

          {/* save a moment */}
          <div style={{
            marginTop: 12, padding: '10px 12px', background: T.bg, borderRadius: 10,
            border: `0.5px solid ${T.hairline}`,
            display: 'flex', alignItems: 'center', justifyContent: 'space-between',
          }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
              <TripIcons.Sparkle s={12}/>
              <span style={{ fontFamily: T.serif, fontSize: 13, color: T.ink, letterSpacing: -0.1 }}>
                Save a moment to Atlas
              </span>
            </div>
            <Marks.ArrowR s={13} c={T.goldDeep}/>
          </div>
        </div>
      </div>

      {/* Drafts kept warm */}
      <div style={{ padding: '14px 22px 0' }}>
        <div style={{ fontSize: 10, color: T.muteSoft, letterSpacing: 1.8, fontWeight: 600 }}>
          ON THE TABLE · 2
        </div>
        <div style={{ marginTop: 8, display: 'flex', gap: 8 }}>
          {['Porto, return', 'A weekend somewhere quiet'].map((t, i) => (
            <div key={t} style={{
              flex: 1, padding: '8px 12px', background: T.cardWarm, borderRadius: 10,
              border: `0.5px solid ${T.hairline}`,
              fontFamily: T.serif, fontSize: 13, color: T.inkSoft, letterSpacing: -0.1,
              lineHeight: 1.1,
            }}>
              {t}
              <div style={{ fontSize: 10, color: T.muteSoft, marginTop: 3 }}>
                paused
              </div>
            </div>
          ))}
        </div>
      </div>

      <TabBar active="trips"/>
    </Phone>
  );
}

// ─── JUST RETURNED · Atlas bridge promoted to top ───────────────
function HomeReturned() {
  return (
    <Phone bg={T.bg}>
      <TripsTopBar eyebrow="TRIPS · WELCOME HOME"/>

      <div style={{ padding: '18px 22px 0' }}>
        <h1 style={{
          fontFamily: T.serif, fontWeight: 500, fontSize: 38, lineHeight: 0.96,
          letterSpacing: -1, color: T.ink, margin: 0,
        }}>
          Lisbon, in your <span style={{ fontStyle: 'italic' }}>hands now.</span>
        </h1>
        <div style={{
          marginTop: 8, fontSize: 11.5, color: T.mute, fontStyle: 'italic', fontFamily: T.serif,
        }}>
          you came home two days ago — vesper kept the week.
        </div>
      </div>

      {/* Atlas bridge as HERO */}
      <div style={{ padding: '16px 16px 0' }}>
        <div style={{
          background: T.cardWarm, borderRadius: 18, padding: '14px',
          border: `0.8px solid ${T.gold}`,
          boxShadow: '0 16px 32px -18px rgba(0,0,0,0.18)',
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
            <TripIcons.Sparkle s={14}/>
            <span style={{ fontSize: 9.5, color: T.goldDeep, letterSpacing: 1.6, fontWeight: 700 }}>
              VESPER DRAFTED A POSTCARD
            </span>
          </div>

          {/* postcard preview, large */}
          <div style={{
            marginTop: 10, height: 180, position: 'relative',
          }}>
            <div style={{
              position: 'absolute', left: 12, top: 8, right: 4, bottom: 8,
              transform: 'rotate(-2deg)', background: T.cardSoft, borderRadius: 6,
              border: `0.5px solid ${T.hairline}`,
            }}/>
            <div style={{
              position: 'absolute', left: 0, top: 0, right: 16, bottom: 12,
              transform: 'rotate(1.6deg)',
            }}>
              <Postcard scene="lisbon" height="100%" stamp={true}/>
            </div>
          </div>

          <div style={{ marginTop: 14 }}>
            <div style={{
              fontFamily: T.serif, fontSize: 22, color: T.ink, fontWeight: 500,
              letterSpacing: -0.4, lineHeight: 1.05,
            }}>
              Lisbon, the slow way
            </div>
            <div style={{
              fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.mute,
              marginTop: 4, lineHeight: 1.4,
            }}>
              six days · Alfama, Ramiro, a fado room nobody told you about
            </div>
          </div>

          <div style={{
            marginTop: 14, display: 'flex', alignItems: 'center', justifyContent: 'space-between',
            padding: '10px 12px', background: T.bg, borderRadius: 10,
          }}>
            <span style={{ fontSize: 11, color: T.mute, fontFamily: T.serif, fontStyle: 'italic' }}>
              refine or not this time
            </span>
            <div style={{
              padding: '7px 14px', background: T.gold, color: T.cardWarm,
              borderRadius: 999, fontSize: 11.5, fontWeight: 600, letterSpacing: -0.1,
              display: 'flex', alignItems: 'center', gap: 4,
            }}>
              Send to Atlas <span>→</span>
            </div>
          </div>
        </div>
      </div>

      {/* Continuing plans */}
      <div style={{ padding: '16px 22px 0' }}>
        <div style={{ fontSize: 10, color: T.mute, letterSpacing: 2, fontWeight: 600 }}>
          ON THE TABLE · 2
        </div>
        <div style={{ marginTop: 10, display: 'flex', flexDirection: 'column', gap: 8 }}>
          {[
            { title: 'Tokyo, in May',    meta: 'alive · 58 days', pill: 'alive', pillText: 'ALIVE' },
            { title: 'Porto, return',    meta: 'pencilled with Ana', pill: 'needs', pillText: 'NEEDS YOU' },
          ].map((row, i) => (
            <div key={i} style={{
              padding: '12px 14px', background: T.cardWarm, borderRadius: 12,
              border: `0.5px solid ${T.hairline}`,
              display: 'flex', alignItems: 'center', justifyContent: 'space-between',
            }}>
              <div>
                <div style={{ fontFamily: T.serif, fontSize: 16, color: T.ink, fontWeight: 500, letterSpacing: -0.2, lineHeight: 1.1 }}>
                  {row.title}
                </div>
                <div style={{ fontFamily: T.serif, fontSize: 11, color: T.mute, marginTop: 3 }}>
                  {row.meta}
                </div>
              </div>
              <TripPill kind={row.pill}>{row.pillText}</TripPill>
            </div>
          ))}
        </div>
      </div>

      <TabBar active="trips"/>
    </Phone>
  );
}

// ─── FREQUENT · 4+ drafts, B's serif rows take over the strip ────
function HomeFrequent() {
  return (
    <Phone bg={T.bg}>
      <TripsTopBar eyebrow="TRIPS · 7 ON THE TABLE"/>
      <PlanningTitle pill={<TripPill kind="alive">1 ALIVE</TripPill>}
                     meta="6 drafts · 4 unresolved"/>
      <HeroAliveTrip
        title="Tokyo, in May"
        days="Sat 14 → Fri 22"
        nights="8 NIGHTS"
        countdown="ALIVE · 58 DAYS OUT"
        scene="tokyo"
        next="Pick a ryokan for nights 5–7"
        compact
      />

      {/* B's serif-numeral row pattern — drafts as a board */}
      <div style={{ padding: '14px 22px 0' }}>
        <div style={{
          display: 'flex', justifyContent: 'space-between', alignItems: 'baseline',
          paddingBottom: 6, borderBottom: `0.5px solid ${T.hairline}`,
          fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.8, fontWeight: 600,
        }}>
          <span>ON THE TABLE · 6</span>
          <span>OPEN</span>
        </div>
        {[
          { mo: 'JUN', dd: '06', t: 'Porto, return',    sub: 'with Ana',           pill: 'needs', txt: 'DATES' },
          { mo: 'SEP', dd: '—',  t: 'Beach week',        sub: 'two friends vote',   pill: 'dreaming', txt: 'VOTING' },
          { mo: 'OCT', dd: '11', t: 'Lyon, in autumn',   sub: 'vesper · slow week',  pill: 'dreaming', txt: 'IDEA' },
          { mo: 'NOV', dd: '—',  t: 'Kyoto, in autumn',  sub: 'saved · Discover',    pill: 'dreaming', txt: 'IDEA' },
        ].map((row, i) => (
          <div key={i} style={{
            padding: '10px 0', borderBottom: `0.5px solid ${T.hairThin}`,
            display: 'grid', gridTemplateColumns: '44px 1fr auto', gap: 10, alignItems: 'center',
          }}>
            <div style={{ textAlign: 'center' }}>
              <div style={{ fontSize: 8.5, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 700 }}>{row.mo}</div>
              <div style={{
                fontFamily: T.serif, fontSize: 22, fontWeight: 500, color: T.inkSoft,
                lineHeight: 1, marginTop: 1, fontVariantNumeric: 'oldstyle-nums', letterSpacing: -0.4,
              }}>{row.dd}</div>
            </div>
            <div>
              <div style={{ fontFamily: T.serif, fontSize: 15, fontWeight: 500, color: T.ink, letterSpacing: -0.2, lineHeight: 1.05 }}>
                {row.t}
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginTop: 4 }}>
                <TripPill kind={row.pill}>{row.txt}</TripPill>
                <span style={{ fontFamily: T.serif, fontSize: 11, color: T.mute }}>
                  {row.sub}
                </span>
              </div>
            </div>
            <Marks.ArrowR s={13} c={T.mute}/>
          </div>
        ))}
      </div>

      <TabBar active="trips"/>
    </Phone>
  );
}

// ── Shared sub-components ───────────────────────────────────────
function PlanningTitle({ pill, meta }) {
  return (
    <div style={{ padding: '18px 22px 0' }}>
      <h1 style={{
        fontFamily: T.serif, fontWeight: 500, fontSize: 38, lineHeight: 0.96,
        letterSpacing: -1, color: T.ink, margin: 0,
      }}>
        Your planning table.
      </h1>
      <div style={{
        marginTop: 8, display: 'flex', alignItems: 'center', gap: 10,
        fontSize: 11, color: T.mute, fontFamily: T.serif,
      }}>
        {pill}
        <span>·</span>
        <span>{meta}</span>
      </div>
    </div>
  );
}

function HeroAliveTrip({ title, days, nights, countdown, scene, next, compact }) {
  return (
    <div style={{ padding: '16px 16px 0' }}>
      <div style={{
        background: T.cardWarm, borderRadius: 18, padding: '14px',
        boxShadow: '0 16px 32px -18px rgba(0,0,0,0.18), 0 0 0 0.5px rgba(27,23,20,0.06)',
        overflow: 'hidden',
      }}>
        <div style={{ display: 'flex', gap: 12 }}>
          <div style={{ width: 88, height: 88, transform: 'rotate(-1.4deg)', flexShrink: 0 }}>
            <TripScene kind={scene}/>
          </div>
          <div style={{ flex: 1, minWidth: 0 }}>
            <TripPill kind="alive">{countdown}</TripPill>
            <div style={{
              fontFamily: T.serif, fontSize: 22, fontWeight: 500, color: T.ink,
              letterSpacing: -0.4, lineHeight: 1.05, marginTop: 6,
            }}>{title}</div>
            <div style={{ display: 'flex', alignItems: 'baseline', gap: 8, marginTop: 4 }}>
              <span style={{ fontFamily: T.serif, fontSize: 13, color: T.inkSoft }}>{days}</span>
              <span style={{ fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 600 }}>{nights}</span>
            </div>
          </div>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke={T.muteSoft} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" style={{ flexShrink: 0, alignSelf: 'center' }}><path d="M9 6l6 6-6 6"/></svg>
        </div>

        {!compact && (
          <div style={{ marginTop: 12, display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 6 }}>
            <Piece label="2 OF 3" sub="haru pending">
              <div style={{ display: 'flex' }}>
                {[TR.ink, T.gold, 'transparent'].map((c, i) => (
                  <div key={i} style={{
                    width: 20, height: 20, borderRadius: 999, background: c === 'transparent' ? T.bg : c,
                    border: `1.5px solid ${T.cardWarm}`, marginLeft: i ? -7 : 0,
                    color: T.cardWarm, fontSize: 9, fontWeight: 600,
                    display: 'flex', alignItems: 'center', justifyContent: 'center',
                    boxShadow: c === 'transparent' ? `inset 0 0 0 1px ${T.muteSoft}` : 'none',
                  }}>{['T','A','?'][i]}</div>
                ))}
              </div>
            </Piece>
            <Piece label="14 SAVED" sub="3 to confirm">
              <div style={{ display: 'flex', gap: 2 }}>
                {[1,2,3,4].map(i => <TripIcons.Pin key={i} s={11} c={i === 1 ? TR.ink : T.muteSoft}/>)}
              </div>
            </Piece>
            <Piece label="3 OPEN" sub="ryokan choice" accent>
              <TripIcons.Decision s={18}/>
            </Piece>
            <Piece label="VESPER" sub="3 quiet rooms" gold>
              <TripIcons.Sparkle s={16} c={T.gold}/>
            </Piece>
          </div>
        )}

        <div style={{
          marginTop: 12, padding: '9px 12px', background: T.bg, borderRadius: 10,
          display: 'flex', alignItems: 'center', justifyContent: 'space-between',
          border: `0.5px solid ${T.hairline}`,
        }}>
          <div>
            <div style={{ fontSize: 9, color: T.mute, letterSpacing: 1.6, fontWeight: 700 }}>
              NEXT · ON THE TABLE
            </div>
            <div style={{ fontFamily: T.serif, fontSize: 13, color: T.ink, marginTop: 2, letterSpacing: -0.1 }}>
              {next}
            </div>
          </div>
          <div style={{
            padding: '6px 12px', background: TR.ink, color: T.cardWarm,
            borderRadius: 999, fontSize: 11, fontWeight: 600,
            display: 'flex', alignItems: 'center', gap: 4,
          }}>
            Open <span>→</span>
          </div>
        </div>
      </div>
    </div>
  );
}

function Piece({ label, sub, children, accent, gold }) {
  return (
    <div style={{
      padding: '8px 6px 6px', borderRadius: 8,
      background: gold ? 'rgba(176,133,58,0.08)' : accent ? 'rgba(176,133,58,0.06)' : T.bg,
      border: gold ? `0.6px solid ${T.gold}` : accent ? `0.6px solid ${T.gold}` : `0.5px solid ${T.hairline}`,
      display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 4, textAlign: 'center',
    }}>
      <div style={{ minHeight: 20, display: 'flex', alignItems: 'center' }}>{children}</div>
      <div style={{ fontSize: 8.5, color: gold || accent ? T.goldDeep : T.mute, letterSpacing: 1.2, fontWeight: 700 }}>
        {label}
      </div>
      <div style={{ fontFamily: T.serif, fontSize: 9, color: T.mute, lineHeight: 1 }}>
        {sub}
      </div>
    </div>
  );
}

function DraftsScatter({ rows }) {
  return (
    <div style={{ padding: '14px 22px 0' }}>
      <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between' }}>
        <span style={{ fontSize: 10, color: T.mute, letterSpacing: 2, fontWeight: 600 }}>ON THE TABLE · {rows.length}</span>
        <span style={{ fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 600 }}>SLIDE →</span>
      </div>
      <div style={{ marginTop: 10, display: 'flex', gap: 8 }}>
        {rows.map((d, i) => (
          <div key={i} style={{
            flex: 1, padding: 12, background: T.cardWarm, borderRadius: 12,
            border: `0.5px solid ${T.hairline}`,
          }}>
            <TripPill kind={d.kind}>{d.pillText}</TripPill>
            <div style={{
              fontFamily: T.serif, fontSize: 14, color: T.ink, fontWeight: 500,
              letterSpacing: -0.2, lineHeight: 1.1, marginTop: 8,
            }}>{d.title}</div>
            <div style={{ fontSize: 10, color: T.mute, fontFamily: T.serif, marginTop: 4 }}>
              {d.meta}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function AtlasBridge({ body, kicker, cta = 'Send to Atlas →' }) {
  return (
    <div style={{ padding: '16px 22px 0' }}>
      <div style={{ paddingTop: 15, borderTop: `0.5px solid ${T.hairline}` }}>
        <div style={{ fontFamily: T.mono, fontSize: 8.5, color: T.goldDeep, fontWeight: 700, letterSpacing: 1.6 }}>{kicker}</div>
        <div style={{ fontFamily: T.serif, fontSize: 16.5, color: T.ink, fontWeight: 500, letterSpacing: -0.2, marginTop: 7, lineHeight: 1.32 }}>{body}</div>
        <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.goldDeep, marginTop: 6 }}>{cta}</div>
      </div>
    </div>
  );
}

Object.assign(window, { HomeCold, HomeDefault, HomeOnTrip, HomeReturned, HomeFrequent });
