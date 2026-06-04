// Variant 3 — ARTIFACT-FIRST: the screen IS the keepsake cabinet.
// A hero object up top, with the four destinations as collectible objects below.

function VariantArtifact() {
  return (
    <Phone bg={T.bg}>
      {/* Top crown */}
      <div style={{
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        padding: '14px 22px 0',
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
          <div style={{
            width: 32, height: 32, borderRadius: 999, background: T.goldDeep,
            color: T.cardWarm, fontFamily: T.serif, fontWeight: 500, fontSize: 14,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
          }}>T</div>
          <div>
            <div style={{ fontSize: 10, color: T.muteSoft, letterSpacing: 1.6, fontWeight: 600, lineHeight: 1 }}>
              KEEPING FOR
            </div>
            <div style={{ fontFamily: T.serif, fontSize: 15, color: T.ink, fontWeight: 500, lineHeight: 1.2, marginTop: 2 }}>
              Tiger
            </div>
          </div>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
          <Marks.Search s={19} c={T.inkSoft}/>
          <div style={{
            width: 30, height: 30, borderRadius: 999,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            background: T.cardWarm, border: `0.5px solid ${T.hairline}`,
          }}>
            <Marks.Plus s={14} c={T.inkSoft}/>
          </div>
        </div>
      </div>

      {/* HERO ARTIFACT — a postcard-on-the-desk look */}
      <div style={{ padding: '20px 22px 0', position: 'relative' }}>
        <div style={{ fontSize: 10.5, color: T.mute, letterSpacing: 2, fontWeight: 600, marginBottom: 10 }}>
          ON YOUR DESK
        </div>

        <div style={{
          position: 'relative', height: 220, perspective: 800,
        }}>
          {/* shadow envelope */}
          <div style={{
            position: 'absolute', left: 18, top: 28, right: 6, bottom: 10,
            background: T.cardSoft, borderRadius: 6,
            transform: 'rotate(-3.2deg)',
            boxShadow: '0 10px 22px -12px rgba(0,0,0,0.18)',
            border: `0.5px solid ${T.hairline}`,
          }}/>
          {/* main postcard */}
          <div style={{
            position: 'absolute', left: 6, top: 14, right: 14, bottom: 18,
            background: T.cardWarm, borderRadius: 6,
            transform: 'rotate(2.2deg)',
            boxShadow: '0 16px 30px -14px rgba(0,0,0,0.22), 0 0 0 0.5px rgba(27,23,20,0.06)',
            padding: 14, display: 'flex', flexDirection: 'column',
          }}>
            {/* image area (placeholder, hand-drawn skyline) */}
            <div style={{
              flex: 1, background: T.card, borderRadius: 3, position: 'relative',
              overflow: 'hidden', border: `0.5px solid ${T.hairThin}`,
            }}>
              <svg width="100%" height="100%" viewBox="0 0 300 160" preserveAspectRatio="xMidYMid slice">
                {/* sky bands */}
                <rect width="300" height="160" fill={T.cardWarm}/>
                <rect y="80" width="300" height="80" fill={T.card}/>
                {/* sun */}
                <circle cx="220" cy="60" r="18" fill={T.goldSoft} opacity="0.55"/>
                {/* skyline */}
                <path d="M0 110 L30 90 L40 95 L55 75 L80 95 L100 88 L120 102 L150 80 L170 92 L195 70 L215 88 L240 78 L260 95 L290 86 L300 92 L300 160 L0 160 Z"
                      fill={T.inkSoft} opacity="0.85"/>
                <path d="M0 130 L40 122 L80 128 L130 118 L180 126 L230 116 L300 124 L300 160 L0 160 Z"
                      fill={T.ink}/>
                {/* birds */}
                <path d="M70 40 q4 -3 8 0 q4 -3 8 0" stroke={T.mute} strokeWidth="1" fill="none"/>
              </svg>
              <div style={{
                position: 'absolute', top: 8, right: 8, width: 24, height: 30,
                background: T.cardWarm, border: `0.6px solid ${T.gold}`,
                borderRadius: 1, display: 'flex', alignItems: 'center', justifyContent: 'center',
              }}>
                <div style={{
                  width: 16, height: 16, borderRadius: 999, background: T.gold, opacity: 0.85,
                }}/>
              </div>
            </div>
            {/* caption row */}
            <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginTop: 10 }}>
              <div>
                <div style={{ fontFamily: T.serif, fontSize: 19, color: T.ink, fontWeight: 500, letterSpacing: -0.3, lineHeight: 1 }}>
                  Lisbon, the slow way
                </div>
                <div style={{ fontSize: 11, color: T.mute, marginTop: 4, fontStyle: 'italic', fontFamily: T.serif }}>
                  a draft Vesper sketched for you
                </div>
              </div>
              <div style={{ fontFamily: T.mono, fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.2 }}>
                03·14·26
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* SHELF — four artifact tiles */}
      <div style={{
        margin: '20px 22px 0',
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        color: T.mute, fontSize: 10.5, letterSpacing: 2, fontWeight: 600,
      }}>
        <span>THE SHELF</span>
        <span style={{ color: T.muteSoft, letterSpacing: 1.5 }}>FOUR ROOMS</span>
      </div>

      <div style={{
        margin: '12px 16px 0',
        display: 'grid', gridTemplateColumns: '1.15fr 1fr', gap: 8,
      }}>
        {/* Inbox — tall, has a "new" tag */}
        <ArtifactCard
          mark={<Marks.Inbox size={78}/>}
          eyebrow="01 · INBOX"
          title="Three drafts"
          tail="opened today"
          accent
          tall
        />
        <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
          <ArtifactCard
            mark={<Marks.Map size={58}/>}
            eyebrow="02 · MAP"
            title="14 cities"
            tail="7 countries"
            compact
          />
          <ArtifactCard
            mark={<Marks.DNA size={58}/>}
            eyebrow="03 · DNA"
            title="Early-morning soul"
            tail="6 rituals"
            compact
          />
        </div>
      </div>

      <div style={{ margin: '8px 16px 0' }}>
        <ArtifactCard
          mark={<Marks.Postcard size={64}/>}
          eyebrow="04 · POSTCARDS"
          title="Your shelf is bare"
          tail="press to start one"
          wide
        />
      </div>

      <TabBar active="atlas"/>
    </Phone>
  );
}

function ArtifactCard({ mark, eyebrow, title, tail, accent, tall, compact, wide }) {
  const h = tall ? 218 : compact ? 105 : 86;
  return (
    <div style={{
      background: T.cardWarm, borderRadius: 14, position: 'relative',
      height: h, padding: compact ? '12px 14px' : '14px 16px',
      boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset, 0 0 0 0.5px rgba(27,23,20,0.05)',
      overflow: 'hidden',
      display: wide ? 'flex' : 'block',
      alignItems: 'center', gap: 14,
    }}>
      {/* mark */}
      {tall ? (
        <div style={{ position: 'absolute', top: 24, left: '50%', transform: 'translateX(-50%)' }}>
          {mark}
        </div>
      ) : wide ? (
        <div style={{ flexShrink: 0, opacity: 0.95 }}>{mark}</div>
      ) : (
        <div style={{ position: 'absolute', right: 8, top: 12, opacity: 0.85 }}>{mark}</div>
      )}
      {/* text */}
      <div style={{
        position: tall ? 'absolute' : 'relative',
        bottom: tall ? 14 : 'auto', left: tall ? 16 : 'auto', right: tall ? 16 : 'auto',
        flex: wide ? 1 : 'none',
      }}>
        <div style={{
          fontSize: 9.5, color: accent ? T.goldDeep : T.mute, fontWeight: 600,
          letterSpacing: 1.6,
        }}>
          {eyebrow}
        </div>
        <div style={{
          fontFamily: T.serif, fontSize: compact ? 17 : 20, color: T.ink, fontWeight: 500,
          letterSpacing: -0.3, lineHeight: 1.05, marginTop: 4,
        }}>
          {title}
        </div>
        <div style={{ fontSize: 10.5, color: T.muteSoft, fontStyle: 'italic', fontFamily: T.serif, marginTop: 4 }}>
          {tail}
        </div>
      </div>
      {accent && (
        <div style={{
          position: 'absolute', top: 12, right: 12,
          background: T.gold, color: T.cardWarm, fontSize: 8.5, fontWeight: 700,
          letterSpacing: 1.2, padding: '2px 6px', borderRadius: 2,
        }}>
          NEW
        </div>
      )}
    </div>
  );
}

window.VariantArtifact = VariantArtifact;
