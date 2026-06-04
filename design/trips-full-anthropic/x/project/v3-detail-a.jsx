// 03 · The DESK detail — opening the postcard on the home screen.
// And the INBOX screen — Vesper's drafts arrayed as a reading room.

function V3Desk() {
  return (
    <Phone bg={T.bg}>
      <ScreenHeader
        eyebrow="ON YOUR DESK · DRAFT"
        title={<>Lisbon,<br/><span style={{ fontStyle: 'italic' }}>the slow way</span></>}
        meta="six days · march 8–14, ’26 · drafted by Vesper"
        right={
          <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="1.6" strokeLinecap="round">
              <circle cx="5" cy="12" r="1.2"/><circle cx="12" cy="12" r="1.2"/><circle cx="19" cy="12" r="1.2"/>
            </svg>
          </div>
        }
      />

      {/* The postcard, larger, almost-flat */}
      <div style={{ padding: '18px 22px 0', position: 'relative' }}>
        <div style={{ position: 'relative', height: 230 }}>
          <div style={{
            position: 'absolute', left: 18, top: 12, right: 6, bottom: 6,
            background: T.cardSoft, borderRadius: 6, transform: 'rotate(-2.4deg)',
            border: `0.5px solid ${T.hairline}`,
            boxShadow: '0 10px 22px -12px rgba(0,0,0,0.18)',
          }}/>
          <div style={{
            position: 'absolute', left: 0, top: 4, right: 14, bottom: 12,
            transform: 'rotate(1.2deg)',
          }}>
            <Postcard scene="lisbon" height="100%" stamp={true}/>
          </div>
        </div>
      </div>

      {/* Vesper's prose for the draft */}
      <div style={{ padding: '14px 24px 0' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <span style={{ width: 5, height: 5, borderRadius: 5, background: T.gold }}/>
          <Eyebrow color={T.goldDeep}>VESPER WROTE</Eyebrow>
        </div>
        <p style={{
          fontFamily: T.serif, fontSize: 15, color: T.inkSoft, lineHeight: 1.5,
          margin: '8px 0 0', letterSpacing: -0.05,
        }}>
          You spent the week in <em>Alfama</em> — coffee on the same step three mornings in a row,
          the long way down to the river. You found <em>Cervejaria Ramiro</em> on a Tuesday and
          a fado room nobody told you about.
        </p>
      </div>

      {/* The "what shaped this" mini-timeline */}
      <div style={{ padding: '14px 22px 0' }}>
        <Eyebrow>WHAT SHAPED IT</Eyebrow>
        <div style={{
          marginTop: 10, padding: '10px 12px', background: T.cardWarm, borderRadius: 12,
          display: 'flex', alignItems: 'center', gap: 10,
          border: `0.5px solid ${T.hairline}`,
        }}>
          {[
            { d: '08', l: 'Alfama' },
            { d: '10', l: 'Ramiro' },
            { d: '11', l: 'A Baiuca' },
            { d: '13', l: 'Belém' },
            { d: '14', l: 'home' },
          ].map((p, i, a) => (
            <React.Fragment key={p.d}>
              <div style={{ textAlign: 'center', flexShrink: 0 }}>
                <div style={{ fontFamily: T.mono, fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.2 }}>{p.d}</div>
                <div style={{
                  width: i === a.length - 1 ? 8 : 6, height: i === a.length - 1 ? 8 : 6,
                  borderRadius: 999, background: i === a.length - 1 ? T.gold : T.inkSoft,
                  margin: '4px auto 4px',
                }}/>
                <div style={{ fontFamily: T.serif, fontSize: 11, color: T.ink, fontStyle: 'italic' }}>{p.l}</div>
              </div>
              {i < a.length - 1 && (
                <div style={{ flex: 1, height: 1, borderTop: `1px dashed ${T.hairline}`, marginTop: 4 }}/>
              )}
            </React.Fragment>
          ))}
        </div>
      </div>

      {/* Action row — typographic, not buttons */}
      <div style={{
        position: 'absolute', bottom: 96, left: 22, right: 22,
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        padding: '14px 18px', background: T.cardWarm, borderRadius: 14,
        boxShadow: '0 0 0 0.5px rgba(27,23,20,0.06), 0 6px 18px -10px rgba(0,0,0,0.12)',
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 18 }}>
          <span style={{ fontFamily: T.serif, fontSize: 15, color: T.ink, fontWeight: 500, letterSpacing: -0.2 }}>
            Keep it
          </span>
          <span style={{ fontFamily: T.serif, fontSize: 14, color: T.inkSoft, fontStyle: 'italic' }}>
            refine
          </span>
          <span style={{ fontSize: 12, color: T.muteSoft, fontStyle: 'italic', fontFamily: T.serif }}>
            not this time
          </span>
        </div>
        <Marks.ArrowR s={14} c={T.goldDeep}/>
      </div>

      <TabBar active="atlas"/>
    </Phone>
  );
}

function V3Inbox() {
  return (
    <Phone bg={T.bg}>
      <ScreenHeader
        eyebrow="01 · INBOX"
        title={<>Three things<br/><span style={{ fontStyle: 'italic' }}>found you.</span></>}
        meta="vesper has been keeping notes"
      />

      {/* filter chips */}
      <div style={{ padding: '14px 22px 0', display: 'flex', gap: 6 }}>
        <Chip active>All · 3</Chip>
        <Chip>Drafts</Chip>
        <Chip>Notes</Chip>
        <Chip>Patterns</Chip>
      </div>

      {/* draft cards */}
      <div style={{ padding: '14px 16px 0', display: 'flex', flexDirection: 'column', gap: 10 }}>
        {/* Card 1 — postcard draft */}
        <div style={{
          background: T.cardWarm, borderRadius: 14, padding: '14px',
          display: 'flex', gap: 12,
          boxShadow: '0 0 0 0.5px rgba(27,23,20,0.05), 0 1px 0 rgba(255,255,255,0.6) inset',
        }}>
          <div style={{ width: 76, height: 96, transform: 'rotate(-3deg)', flexShrink: 0 }}>
            <Postcard scene="lisbon" height="100%" stamp={false}/>
          </div>
          <div style={{ flex: 1, minWidth: 0 }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
              <Eyebrow color={T.goldDeep}>POSTCARD · DRAFT</Eyebrow>
              <span style={{ width: 5, height: 5, borderRadius: 5, background: T.gold }}/>
            </div>
            <div style={{
              fontFamily: T.serif, fontSize: 19, color: T.ink, fontWeight: 500,
              letterSpacing: -0.3, lineHeight: 1.1, marginTop: 6,
            }}>
              Lisbon, the slow way
            </div>
            <div style={{
              fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.mute,
              marginTop: 4, lineHeight: 1.35,
            }}>
              six days · Alfama, Ramiro, a fado room nobody told you about
            </div>
            <div style={{
              display: 'flex', alignItems: 'center', justifyContent: 'space-between',
              marginTop: 10,
            }}>
              <span style={{ fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1.2 }}>
                03·14·26
              </span>
              <span style={{ fontSize: 10, color: T.goldDeep, fontWeight: 600, letterSpacing: 1.4 }}>
                ON YOUR DESK →
              </span>
            </div>
          </div>
        </div>

        {/* Card 2 — text note */}
        <div style={{
          background: T.cardWarm, borderRadius: 14, padding: '14px',
          boxShadow: '0 0 0 0.5px rgba(27,23,20,0.05), 0 1px 0 rgba(255,255,255,0.6) inset',
        }}>
          <Eyebrow>NOTE · IN VESPER’S HAND</Eyebrow>
          <div style={{
            fontFamily: T.serif, fontSize: 17, color: T.ink, fontWeight: 500,
            letterSpacing: -0.3, lineHeight: 1.15, marginTop: 6,
          }}>
            A short note about Porto
          </div>
          <p style={{
            fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.mute,
            lineHeight: 1.45, margin: '8px 0 0',
          }}>
            “You walked the Ribeira three times before the bridge. There’s a way you choose streets — Vesper has a theory.”
          </p>
          <div style={{
            display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginTop: 10,
          }}>
            <span style={{ fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1.2 }}>02·22·26</span>
            <span style={{ fontSize: 10, color: T.inkSoft, fontWeight: 600, letterSpacing: 1.4 }}>READ →</span>
          </div>
        </div>

        {/* Card 3 — pattern */}
        <div style={{
          background: T.cardWarm, borderRadius: 14, padding: '14px',
          boxShadow: '0 0 0 0.5px rgba(27,23,20,0.05), 0 1px 0 rgba(255,255,255,0.6) inset',
        }}>
          <Eyebrow>PATTERN · A REPETITION</Eyebrow>
          <div style={{
            fontFamily: T.serif, fontSize: 17, color: T.ink, fontWeight: 500,
            letterSpacing: -0.3, lineHeight: 1.15, marginTop: 6,
          }}>
            Three places that keep returning
          </div>
          <div style={{
            display: 'flex', gap: 8, marginTop: 10, flexWrap: 'wrap',
          }}>
            {['the same coffee step', 'one dinner alone', 'rivers at dusk'].map((p, i) => (
              <span key={i} style={{
                padding: '4px 10px', fontFamily: T.serif, fontStyle: 'italic',
                fontSize: 11.5, color: T.inkSoft, background: T.cardSoft, borderRadius: 999,
                border: `0.5px solid ${T.hairline}`,
              }}>{p}</span>
            ))}
          </div>
          <div style={{
            display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginTop: 12,
          }}>
            <span style={{ fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1.2 }}>02·14·26</span>
            <span style={{ fontSize: 10, color: T.inkSoft, fontWeight: 600, letterSpacing: 1.4 }}>OPEN →</span>
          </div>
        </div>
      </div>

      {/* archived link */}
      <div style={{
        position: 'absolute', bottom: 96, left: 0, right: 0, textAlign: 'center',
        fontSize: 10.5, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 600,
      }}>
        — 41 OLDER · IN THE ARCHIVE —
      </div>

      <TabBar active="atlas"/>
    </Phone>
  );
}

Object.assign(window, { V3Desk, V3Inbox });
