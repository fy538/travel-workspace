// + CREATE TRIP page + NOTIFICATIONS page.
// The + button on every Trips screen opens TripsCreate.
// The bell opens TripsNotifications.

function TripsCreate() {
  return (
    <Phone bg={T.bg}>
      {/* Header */}
      <div style={{
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        padding: '14px 22px 0',
      }}>
        <span style={{ fontSize: 13, color: T.inkSoft, fontWeight: 500, letterSpacing: -0.1 }}>
          Cancel
        </span>
        <span style={{ fontSize: 10.5, color: T.mute, letterSpacing: 2, fontWeight: 600 }}>
          NEW TRIP
        </span>
        <span style={{ width: 40 }}/>
      </div>

      <div style={{ padding: '14px 22px 0' }}>
        <h1 style={{
          fontFamily: T.serif, fontWeight: 500, fontSize: 38, lineHeight: 0.96,
          letterSpacing: -1, color: T.ink, margin: 0,
        }}>
          Begin a <span style={{ fontStyle: 'italic' }}>trip.</span>
        </h1>
        <div style={{ marginTop: 8, fontFamily: T.serif, fontSize: 13.5, color: T.mute, fontStyle: 'italic' }}>
          two ways in — talk it through, or start blank.
        </div>
      </div>

      {/* Two primary paths */}
      <div style={{ padding: '20px 16px 0', display: 'flex', flexDirection: 'column', gap: 10 }}>
        {/* Talk to Vesper — ochre primary */}
        <div style={{
          padding: '18px 18px', background: T.cardWarm, borderRadius: 16,
          border: `0.8px solid ${T.gold}`,
          boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset, 0 10px 22px -16px rgba(176,133,58,0.4)',
          position: 'relative', overflow: 'hidden',
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
            <div style={{
              width: 36, height: 36, borderRadius: 999,
              background: 'rgba(176,133,58,0.14)',
              display: 'flex', alignItems: 'center', justifyContent: 'center',
            }}>
              <TripIcons.Sparkle s={18}/>
            </div>
            <div>
              <Eyebrow color={T.goldDeep}>RECOMMENDED</Eyebrow>
              <div style={{
                fontFamily: T.serif, fontSize: 22, fontWeight: 500, color: T.ink,
                letterSpacing: -0.4, lineHeight: 1, marginTop: 4,
              }}>
                Talk it through with Vesper
              </div>
            </div>
          </div>
          <p style={{
            margin: '12px 0 0', fontFamily: T.serif, fontSize: 13.5, color: T.inkSoft,
            lineHeight: 1.4, letterSpacing: -0.05,
          }}>
            Tell Vesper the shape of the trip — a city, a season, who’s coming.
            It’ll set up the structure and pull places you’ve saved.
          </p>
          <div style={{
            marginTop: 14, padding: '10px 12px', background: T.bg, borderRadius: 10,
            border: `0.5px solid ${T.hairline}`,
            fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.muteSoft,
            letterSpacing: -0.1, display: 'flex', alignItems: 'center', justifyContent: 'space-between',
          }}>
            <span>“a quiet week in september, somewhere coastal…”</span>
            <Marks.ArrowR s={13} c={T.goldDeep}/>
          </div>
        </div>

        {/* Blank canvas — ink-blue secondary */}
        <div style={{
          padding: '14px 16px', background: T.cardWarm, borderRadius: 16,
          border: `0.5px solid ${T.hairline}`,
          display: 'flex', alignItems: 'center', gap: 14,
        }}>
          <div style={{
            width: 36, height: 36, borderRadius: 999,
            background: 'rgba(61,80,102,0.10)',
            display: 'flex', alignItems: 'center', justifyContent: 'center',
          }}>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={TR.ink} strokeWidth="1.6" strokeLinecap="round">
              <rect x="5" y="4" width="14" height="17" rx="2"/>
              <path d="M9 9h6M9 13h6M9 17h3"/>
            </svg>
          </div>
          <div style={{ flex: 1 }}>
            <div style={{
              fontFamily: T.serif, fontSize: 18, fontWeight: 500, color: T.ink,
              letterSpacing: -0.3, lineHeight: 1, marginTop: 2,
            }}>
              Start with a blank canvas
            </div>
            <div style={{
              fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.mute,
              marginTop: 4, lineHeight: 1.3,
            }}>
              just a title and a date — fill it in as you go
            </div>
          </div>
          <Marks.ArrowR s={13} c={TR.ink}/>
        </div>
      </div>

      {/* Quick starts */}
      <div style={{ padding: '20px 22px 0' }}>
        <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between' }}>
          <Eyebrow>OR PICK A SHAPE</Eyebrow>
          <span style={{ fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 600 }}>VESPER FILLS IT IN</span>
        </div>
        <div style={{
          marginTop: 10, display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 8,
        }}>
          {[
            { n: 'City',     g: <StarterGlyphs.City/>,     s: 'a few days in a vibrant city' },
            { n: 'Beach',    g: <StarterGlyphs.Beach/>,    s: 'sun, sea, slow days' },
            { n: 'Mountain', g: <StarterGlyphs.Mountain/>, s: 'walks, cold air, quiet' },
            { n: 'Road',     g: <StarterGlyphs.Road/>,     s: 'a route, not a place' },
            { n: 'Festival', g: <StarterGlyphs.Festival/>, s: 'music, food, crowd' },
            { n: 'Quiet',    g: <StarterGlyphs.Quiet/>,    s: 'nothing in particular' },
          ].map((s) => (
            <div key={s.n} style={{
              padding: '12px 10px 10px', background: T.cardWarm, borderRadius: 12,
              border: `0.5px solid ${T.hairline}`,
              display: 'flex', flexDirection: 'column', gap: 6,
            }}>
              <div style={{
                width: 28, height: 28, borderRadius: 8,
                background: T.cardSoft,
                display: 'flex', alignItems: 'center', justifyContent: 'center',
              }}>{s.g}</div>
              <div style={{
                fontFamily: T.serif, fontSize: 14, fontWeight: 500, color: T.ink,
                letterSpacing: -0.2, lineHeight: 1,
              }}>{s.n}</div>
              <div style={{
                fontFamily: T.serif, fontStyle: 'italic', fontSize: 10, color: T.mute,
                lineHeight: 1.2,
              }}>{s.s}</div>
            </div>
          ))}
        </div>
      </div>

      {/* From discover */}
      <div style={{ padding: '18px 22px 0' }}>
        <div style={{
          padding: '12px 14px', background: T.cardSoft, borderRadius: 12,
          border: `0.5px solid ${T.hairline}`,
          display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        }}>
          <div>
            <Eyebrow>OR CONTINUE FROM</Eyebrow>
            <div style={{
              fontFamily: T.serif, fontSize: 14, fontWeight: 500, color: T.ink,
              letterSpacing: -0.1, marginTop: 4,
            }}>
              <span style={{ fontStyle: 'italic' }}>12 places</span> saved in Discover
            </div>
          </div>
          <Marks.ArrowR s={13} c={T.inkSoft}/>
        </div>
      </div>

      <TabBar active="trips"/>
    </Phone>
  );
}

function TripsNotifications() {
  return (
    <Phone bg={T.bg}>
      {/* Header */}
      <div style={{
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        padding: '14px 22px 0',
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="1.6" strokeLinecap="round">
            <path d="M14 6l-6 6 6 6"/>
          </svg>
          <span style={{ fontSize: 13, color: T.inkSoft, fontWeight: 500 }}>Trips</span>
        </div>
        <span style={{ fontSize: 10.5, color: T.mute, letterSpacing: 2, fontWeight: 600 }}>
          UPDATES
        </span>
        <span style={{ fontSize: 11, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 600 }}>
          MARK ALL
        </span>
      </div>

      {/* Title */}
      <div style={{ padding: '14px 22px 0' }}>
        <h1 style={{
          fontFamily: T.serif, fontWeight: 500, fontSize: 36, lineHeight: 0.96,
          letterSpacing: -1, color: T.ink, margin: 0,
        }}>
          What changed,<br/><span style={{ fontStyle: 'italic' }}>since you looked.</span>
        </h1>
        <div style={{ marginTop: 6, fontSize: 12, color: T.mute, fontStyle: 'italic', fontFamily: T.serif }}>
          eleven updates across four trips
        </div>
      </div>

      {/* — LIVE / NOW — */}
      <NotifSection
        label="LIVE · TOKYO"
        kicker="day 3 of 8"
        accent={TR.ink}
      >
        <NotifRow
          dot={TR.ink}
          when="now"
          title="Cherry blossoms peaked overnight"
          sub="Yoyogi is at 90% bloom — a 12-min walk."
          actionLabel="OPEN"
          source="Vesper"
        />
        <NotifRow
          dot={T.gold}
          when="2h"
          title="Ana added a dinner pin"
          sub="“Den” — Wed, 19:30. Two seats."
          actionLabel="VIEW"
          source="Ana"
        />
      </NotifSection>

      {/* — PLANNING — */}
      <NotifSection
        label="PLANNING · 2 TRIPS"
        kicker="3 decisions waiting"
        accent={T.gold}
      >
        <NotifRow
          dot={T.gold}
          when="this morning"
          title="Vesper drafted 3 ryokans for Tokyo"
          sub="kept the quiet ones, dropped the chain."
          actionLabel="REVIEW"
          source="Vesper"
        />
        <NotifRow
          dot={TR.ink}
          when="yesterday"
          title="Ana said yes to Porto"
          sub="picked the week of Jun 6–13."
          actionLabel="CONFIRM"
          source="Ana"
        />
        <NotifRow
          dot={T.muteSoft}
          when="mar 12"
          title="Two friends are interested in Beach week"
          sub="a vote was opened — your call."
          actionLabel="VOTE"
          source="Group"
        />
      </NotifSection>

      {/* — RETURNED — */}
      <NotifSection
        label="RETURNED · LISBON"
        kicker="2 days ago"
        accent={T.goldDeep}
      >
        <NotifRow
          dot={T.gold}
          when="mar 14"
          title="A postcard is on your desk"
          sub="“Lisbon, the slow way” — keep or refine?"
          actionLabel="OPEN"
          source="Vesper"
          golden
        />
        <NotifRow
          dot={T.muteSoft}
          when="mar 13"
          title="41 entries kept in Atlas"
          sub="six places, three rituals, two patterns."
          actionLabel="SEE"
          source="Atlas"
        />
      </NotifSection>

      <TabBar active="trips"/>
    </Phone>
  );
}

function NotifSection({ label, kicker, accent, children }) {
  return (
    <div style={{ padding: '14px 22px 0' }}>
      <div style={{
        display: 'flex', alignItems: 'baseline', justifyContent: 'space-between',
        marginBottom: 8,
      }}>
        <div style={{ display: 'flex', alignItems: 'baseline', gap: 8 }}>
          <span style={{
            width: 5, height: 5, borderRadius: 5, background: accent, alignSelf: 'center',
            display: 'inline-block',
          }}/>
          <span style={{ fontSize: 10, color: T.mute, letterSpacing: 1.8, fontWeight: 700 }}>
            {label}
          </span>
        </div>
        <span style={{ fontSize: 10, color: T.muteSoft, fontStyle: 'italic', fontFamily: T.serif }}>
          {kicker}
        </span>
      </div>
      <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
        {children}
      </div>
    </div>
  );
}

function NotifRow({ dot, when, title, sub, actionLabel, source, golden }) {
  return (
    <div style={{
      padding: '11px 14px', background: golden ? 'rgba(176,133,58,0.06)' : T.cardWarm,
      borderRadius: 12,
      border: golden ? `0.8px solid rgba(176,133,58,0.4)` : `0.5px solid ${T.hairline}`,
      display: 'grid', gridTemplateColumns: '14px 1fr auto', gap: 10, alignItems: 'flex-start',
    }}>
      <div style={{ paddingTop: 6 }}>
        <div style={{ width: 6, height: 6, borderRadius: 6, background: dot }}/>
      </div>
      <div style={{ minWidth: 0 }}>
        <div style={{
          fontFamily: T.serif, fontSize: 14, color: T.ink, fontWeight: 500,
          letterSpacing: -0.2, lineHeight: 1.2,
        }}>{title}</div>
        <div style={{
          fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.mute,
          marginTop: 2, lineHeight: 1.35,
        }}>{sub}</div>
        <div style={{
          display: 'flex', alignItems: 'center', gap: 6, marginTop: 5,
          fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.2, fontWeight: 600,
        }}>
          <span>{source.toUpperCase()}</span>
          <span>·</span>
          <span>{when.toUpperCase()}</span>
        </div>
      </div>
      <div style={{
        fontSize: 9.5, color: golden ? T.goldDeep : T.inkSoft, letterSpacing: 1.4, fontWeight: 700,
        padding: '4px 8px', border: `0.6px solid ${golden ? T.gold : T.hairline}`,
        borderRadius: 4, alignSelf: 'center',
      }}>
        {actionLabel}
      </div>
    </div>
  );
}

Object.assign(window, { TripsCreate, TripsNotifications });
