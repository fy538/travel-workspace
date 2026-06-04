// 03 · Atlas Home — FULL state, with the Almanac year ribbon stitched in.

function V3HomeFull() {
  return (
    <Phone bg={T.bg}>
      {/* Top crown */}
      <div style={{
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        padding: '14px 22px 0',
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
          <div style={{
            width: 30, height: 30, borderRadius: 999, background: T.goldDeep,
            color: T.cardWarm, fontFamily: T.serif, fontWeight: 500, fontSize: 13,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
          }}>T</div>
          <div>
            <div style={{ fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.6, fontWeight: 600, lineHeight: 1 }}>
              KEEPING FOR
            </div>
            <div style={{ fontFamily: T.serif, fontSize: 14, color: T.ink, fontWeight: 500, lineHeight: 1.2, marginTop: 2 }}>
              Tiger
            </div>
          </div>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
          <Marks.Search s={18} c={T.inkSoft}/>
          <div style={{
            width: 28, height: 28, borderRadius: 999,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            background: T.cardWarm, border: `0.5px solid ${T.hairline}`,
          }}>
            <Marks.Plus s={13} c={T.inkSoft}/>
          </div>
        </div>
      </div>

      {/* HERO ARTIFACT */}
      <div style={{ padding: '14px 22px 0', position: 'relative' }}>
        <div style={{
          display: 'flex', alignItems: 'baseline', justifyContent: 'space-between',
          marginBottom: 8,
        }}>
          <Eyebrow>ON YOUR DESK</Eyebrow>
          <span style={{ fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.5, fontWeight: 600 }}>VESPER · DRAFT</span>
        </div>

        <div style={{ position: 'relative', height: 196 }}>
          <div style={{
            position: 'absolute', left: 16, top: 22, right: 4, bottom: 8,
            background: T.cardSoft, borderRadius: 6,
            transform: 'rotate(-3.2deg)',
            boxShadow: '0 10px 22px -12px rgba(0,0,0,0.18)',
            border: `0.5px solid ${T.hairline}`,
          }}/>
          <div style={{
            position: 'absolute', left: 4, top: 8, right: 12, bottom: 14,
            transform: 'rotate(2.2deg)',
          }}>
            <Postcard
              scene="lisbon"
              title="Lisbon, the slow way"
              sub="a draft Vesper sketched for you"
              date="03·14·26"
              height="100%"
            />
          </div>
        </div>
      </div>

      {/* YEAR RIBBON — Almanac, distilled */}
      <div style={{ marginTop: 14 }}>
        <YearRibbonH
          dots={[null,'past','now',null,'planned',null,null,'past',null,'past',null,null]}
          now={2}
          leftLabel="YOUR YEAR"
          rightLabel="TOKYO · MAY"
        />
      </div>

      {/* SHELF */}
      <div style={{
        margin: '14px 22px 0',
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
      }}>
        <Eyebrow>THE SHELF</Eyebrow>
        <span style={{ color: T.muteSoft, fontSize: 9.5, letterSpacing: 1.5, fontWeight: 600 }}>FOUR ROOMS</span>
      </div>

      <div style={{
        margin: '8px 16px 0', display: 'grid',
        gridTemplateColumns: '1.15fr 1fr', gap: 8,
      }}>
        <ArtifactCard mark={<Marks.Inbox size={72}/>} eyebrow="01 · INBOX" title="Three drafts" tail="opened today" accent tall heightOverride={184}/>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
          <ArtifactCard mark={<Marks.Map size={54}/>} eyebrow="02 · MAP" title="14 cities" tail="7 countries" compact heightOverride={88}/>
          <ArtifactCard mark={<Marks.DNA size={54}/>} eyebrow="03 · DNA" title="Early-morning soul" tail="6 rituals" compact heightOverride={88}/>
        </div>
      </div>
      <div style={{ margin: '8px 16px 0' }}>
        <ArtifactCard mark={<Marks.Postcard size={56}/>} eyebrow="04 · POSTCARDS" title="Your shelf is bare" tail="press to start one" wide heightOverride={72}/>
      </div>

      <TabBar active="atlas"/>
    </Phone>
  );
}

// 03 · Atlas Home — COLD START. Day 1. Empty everything, but warm.
function V3HomeCold() {
  return (
    <Phone bg={T.bg}>
      {/* Top crown */}
      <div style={{
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        padding: '14px 22px 0',
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
          <div style={{
            width: 30, height: 30, borderRadius: 999,
            background: T.cardWarm, border: `0.8px dashed ${T.gold}`,
            color: T.goldDeep, fontFamily: T.serif, fontWeight: 500, fontSize: 13,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
          }}>T</div>
          <div>
            <div style={{ fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.6, fontWeight: 600, lineHeight: 1 }}>
              JUST BEGINNING
            </div>
            <div style={{ fontFamily: T.serif, fontSize: 14, color: T.ink, fontWeight: 500, lineHeight: 1.2, marginTop: 2 }}>
              Welcome, Tiger
            </div>
          </div>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
          <Marks.Search s={18} c={T.muteSoft}/>
          <div style={{
            width: 28, height: 28, borderRadius: 999,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            background: T.cardWarm, border: `0.5px solid ${T.hairline}`,
          }}>
            <Marks.Plus s={13} c={T.inkSoft}/>
          </div>
        </div>
      </div>

      {/* Vesper-reads-you intro */}
      <div style={{ padding: '14px 22px 0' }}>
        <h1 style={{
          fontFamily: T.serif, fontWeight: 500, fontSize: 30, lineHeight: 1,
          letterSpacing: -0.6, color: T.ink, margin: 0,
        }}>
          Your atlas is <span style={{ fontStyle: 'italic' }}>almost empty</span>—
        </h1>
        <p style={{
          fontFamily: T.serif, fontStyle: 'italic', fontSize: 14, color: T.mute,
          margin: '8px 0 0', lineHeight: 1.4, maxWidth: 320,
        }}>
          which is the best way to start. Tell Vesper one place you’ve loved and it’ll keep the rest.
        </p>
      </div>

      {/* Hero — Vesper's first object: a blank postcard with a soft prompt */}
      <div style={{ padding: '18px 22px 0' }}>
        <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginBottom: 8 }}>
          <Eyebrow>FIRST DRAFT</Eyebrow>
          <span style={{ fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.5, fontWeight: 600 }}>VESPER · WAITING</span>
        </div>
        <div style={{ position: 'relative', height: 196 }}>
          <div style={{
            position: 'absolute', left: 4, top: 8, right: 12, bottom: 14,
            transform: 'rotate(1.6deg)',
          }}>
            <Postcard
              blank stamp={false}
              title="A place you’ve loved"
              sub="tap to whisper one to Vesper"
              date="—·—·26"
              height="100%"
            />
          </div>
          {/* dotted invitation overlay */}
          <div style={{
            position: 'absolute', left: 14, right: 24, top: 36, bottom: 50,
            border: `1px dashed ${T.gold}`, borderRadius: 4, opacity: 0.4,
            transform: 'rotate(1.6deg)', pointerEvents: 'none',
          }}/>
        </div>
      </div>

      {/* Year ribbon — mostly empty, "Start your year" */}
      <div style={{ marginTop: 14 }}>
        <YearRibbonH
          dots={[null,null,'now',null,null,null,null,null,null,null,null,null]}
          now={2}
          leftLabel="START YOUR YEAR"
          rightLabel="MARCH ’26"
        />
      </div>

      {/* Empty shelf with gentle invites */}
      <div style={{
        margin: '14px 22px 0',
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
      }}>
        <Eyebrow>THE SHELF</Eyebrow>
        <span style={{ color: T.muteSoft, fontSize: 9.5, letterSpacing: 1.5, fontWeight: 600 }}>FOUR EMPTY ROOMS</span>
      </div>

      <div style={{ margin: '8px 16px 0', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8 }}>
        {[
          { eyebrow: '01 · INBOX',     title: 'Save a memory',     tail: 'Vesper will hold it' },
          { eyebrow: '02 · MAP',       title: 'Drop your first pin', tail: 'where have you been?' },
          { eyebrow: '03 · DNA',       title: 'A reading awaits',  tail: 'after a few entries' },
          { eyebrow: '04 · POSTCARDS', title: 'No shelf yet',       tail: 'starts after your first draft' },
        ].map((c, i) => (
          <div key={i} style={{
            background: T.cardWarm, borderRadius: 14, padding: '14px 14px',
            height: 116, position: 'relative', overflow: 'hidden',
            border: i === 0 ? `0.8px dashed ${T.gold}` : `0.5px solid ${T.hairline}`,
            boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset',
          }}>
            <div style={{ fontSize: 9, color: i === 0 ? T.goldDeep : T.mute, fontWeight: 600, letterSpacing: 1.6 }}>
              {c.eyebrow}
            </div>
            <div style={{
              fontFamily: T.serif, fontSize: 16, color: i === 0 ? T.ink : T.inkSoft,
              fontWeight: 500, letterSpacing: -0.2, lineHeight: 1.1, marginTop: 6,
            }}>{c.title}</div>
            <div style={{
              fontSize: 10.5, color: T.muteSoft, fontStyle: 'italic',
              fontFamily: T.serif, marginTop: 4,
            }}>{c.tail}</div>
            {i === 0 && (
              <div style={{
                position: 'absolute', right: 10, top: 10,
                background: T.gold, color: T.cardWarm, fontSize: 8, fontWeight: 700,
                letterSpacing: 1.2, padding: '2px 6px', borderRadius: 2,
              }}>BEGIN HERE</div>
            )}
          </div>
        ))}
      </div>

      <TabBar active="atlas"/>
    </Phone>
  );
}

// A slightly more flexible ArtifactCard variant (overrideable height)
function ArtifactCard({ mark, eyebrow, title, tail, accent, tall, compact, wide, heightOverride }) {
  const h = heightOverride || (tall ? 218 : compact ? 105 : 86);
  return (
    <div style={{
      background: T.cardWarm, borderRadius: 14, position: 'relative',
      height: h, padding: compact ? '12px 14px' : '14px 16px',
      boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset, 0 0 0 0.5px rgba(27,23,20,0.05)',
      overflow: 'hidden',
      display: wide ? 'flex' : 'block', alignItems: 'center', gap: 14,
    }}>
      {tall ? (
        <div style={{ position: 'absolute', top: 18, left: '50%', transform: 'translateX(-50%)' }}>{mark}</div>
      ) : wide ? (
        <div style={{ flexShrink: 0, opacity: 0.95 }}>{mark}</div>
      ) : (
        <div style={{ position: 'absolute', right: 8, top: 10, opacity: 0.85 }}>{mark}</div>
      )}
      <div style={{
        position: tall ? 'absolute' : 'relative',
        bottom: tall ? 12 : 'auto', left: tall ? 16 : 'auto', right: tall ? 16 : 'auto',
        flex: wide ? 1 : 'none',
      }}>
        <div style={{ fontSize: 9, color: accent ? T.goldDeep : T.mute, fontWeight: 600, letterSpacing: 1.5 }}>
          {eyebrow}
        </div>
        <div style={{
          fontFamily: T.serif, fontSize: compact ? 16 : 18, color: T.ink, fontWeight: 500,
          letterSpacing: -0.2, lineHeight: 1.05, marginTop: 4,
        }}>
          {title}
        </div>
        <div style={{ fontSize: 10, color: T.muteSoft, fontStyle: 'italic', fontFamily: T.serif, marginTop: 3 }}>
          {tail}
        </div>
      </div>
      {accent && (
        <div style={{
          position: 'absolute', top: 10, right: 10,
          background: T.gold, color: T.cardWarm, fontSize: 8, fontWeight: 700,
          letterSpacing: 1.2, padding: '2px 6px', borderRadius: 2,
        }}>NEW</div>
      )}
    </div>
  );
}

Object.assign(window, { V3HomeFull, V3HomeCold, ArtifactCard });
