// Direction C — DREAM STACK
// Future-facing and editorial. Possible trips fan as a deck of cards.
// Especially good for users without a booked trip yet.

function TripsDreamStack() {
  return (
    <Phone bg={T.bg}>
      <TripsTopBar eyebrow="TRIPS · DREAMING"/>

      {/* Title */}
      <div style={{ padding: '18px 22px 0' }}>
        <h1 style={{
          fontFamily: T.serif, fontWeight: 500, fontSize: 44, lineHeight: 0.92,
          letterSpacing: -1.4, color: T.ink, margin: 0,
        }}>
          Where <span style={{ fontStyle: 'italic' }}>to?</span>
        </h1>
        <div style={{
          marginTop: 8, fontSize: 12, color: T.mute, fontStyle: 'italic', fontFamily: T.serif,
        }}>
          one trip booked · three pencilled · twelve dreamt of
        </div>
      </div>

      {/* ── THE STACK — a fanned deck of cards ── */}
      <div style={{ padding: '14px 16px 0', position: 'relative' }}>
        <div style={{ position: 'relative', height: 232 }}>
          {/* card 4 — far back, dreaming */}
          <DreamCard
            style={{ left: 14, right: 60, top: 36, transform: 'rotate(-7deg)' }}
            scene="porto"
            kind="dreaming"
            label="DREAMING"
            title="A weekend, somewhere quiet"
            sub="no dates · whispered to Vesper"
            zIndex={1}
          />
          {/* card 3 — back-right */}
          <DreamCard
            style={{ left: 50, right: 18, top: 28, transform: 'rotate(5deg)' }}
            scene="tokyo"
            kind="dreaming"
            label="DREAMING"
            title="Kyoto, in autumn"
            sub="saved from Discover"
            zIndex={2}
          />
          {/* card 2 — middle */}
          <DreamCard
            style={{ left: 32, right: 42, top: 16, transform: 'rotate(-2deg)' }}
            scene="lisbon"
            kind="needs"
            label="NEEDS YOU"
            title="Porto, return"
            sub="dates with Ana — pick a week"
            zIndex={3}
          />
          {/* card 1 — front, alive */}
          <DreamCard
            style={{ left: 6, right: 14, top: 4, transform: 'rotate(1.4deg)' }}
            scene="tokyo"
            kind="alive"
            label="ALIVE · 58 DAYS"
            title="Tokyo, in May"
            sub="Sat 14 → Fri 22 · 2 of 3 travelers"
            zIndex={4}
            primary
          />
        </div>
        {/* deck count chip */}
        <div style={{
          position: 'absolute', right: 22, top: 18, padding: '4px 8px',
          background: 'rgba(27,23,20,0.06)', borderRadius: 999,
          fontSize: 9, fontWeight: 700, color: T.inkSoft, letterSpacing: 1.4,
          fontFamily: T.mono,
        }}>
          1 / 4
        </div>
      </div>

      {/* ── VESPER'S READING ── */}
      <div style={{ padding: '20px 16px 0' }}>
        <div style={{
          padding: '14px 16px', background: T.cardSoft, borderRadius: 14,
          border: `0.8px dashed ${T.gold}`,
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
            <TripIcons.Sparkle s={14}/>
            <span style={{ fontSize: 10, color: T.goldDeep, letterSpacing: 1.8, fontWeight: 600 }}>
              VESPER · BASED ON WHAT YOU’VE SAVED
            </span>
          </div>
          <div style={{
            marginTop: 8, fontFamily: T.serif, fontSize: 17, color: T.ink, fontWeight: 500,
            letterSpacing: -0.3, lineHeight: 1.2,
          }}>
            “Three ideas for <span style={{ fontStyle: 'italic' }}>a slow week</span>—”
          </div>
          <div style={{ marginTop: 10, display: 'flex', gap: 6, flexWrap: 'wrap' }}>
            {['Lyon, in october', 'Mallorca, off-season', 'Tbilisi, by train'].map((t, i) => (
              <span key={t} style={{
                padding: '5px 10px', fontFamily: T.serif, fontStyle: 'italic',
                fontSize: 12, color: T.inkSoft, background: T.cardWarm,
                borderRadius: 999, border: `0.5px solid ${T.hairline}`,
              }}>{t}</span>
            ))}
          </div>
        </div>
      </div>

      {/* ── BEGIN ONE ── */}
      <div style={{ padding: '14px 22px 0' }}>
        <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between' }}>
          <span style={{ fontSize: 10.5, color: T.mute, letterSpacing: 2, fontWeight: 600 }}>BEGIN ONE</span>
          <span style={{ fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 600 }}>OR FROM DISCOVER</span>
        </div>
      </div>
      <div style={{ padding: '10px 16px 0', display: 'flex', gap: 6, overflow: 'hidden' }}>
        {[
          { name: 'City',     glyph: <StarterGlyphs.City/> },
          { name: 'Beach',    glyph: <StarterGlyphs.Beach/> },
          { name: 'Mountain', glyph: <StarterGlyphs.Mountain/> },
          { name: 'Road',     glyph: <StarterGlyphs.Road/> },
          { name: 'Quiet',    glyph: <StarterGlyphs.Quiet/> },
        ].map((s) => (
          <div key={s.name} style={{
            flex: 1, padding: '10px 6px 8px', background: T.cardWarm, borderRadius: 10,
            border: `0.5px solid ${T.hairline}`,
            display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 4,
            boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset',
          }}>
            {s.glyph}
            <span style={{ fontSize: 10, color: T.inkSoft, fontWeight: 500 }}>{s.name}</span>
          </div>
        ))}
      </div>

      <TabBar active="trips"/>
    </Phone>
  );
}

function DreamCard({ style, scene, kind, label, title, sub, zIndex, primary }) {
  return (
    <div style={{
      position: 'absolute', ...style, zIndex,
      background: T.cardWarm, borderRadius: 10, padding: 10,
      boxShadow: primary
        ? '0 18px 32px -16px rgba(0,0,0,0.25), 0 0 0 0.5px rgba(27,23,20,0.06)'
        : '0 10px 22px -14px rgba(0,0,0,0.18), 0 0 0 0.5px rgba(27,23,20,0.05)',
      border: primary ? `0.8px solid ${TR.ink}` : 'none',
    }}>
      {/* scene */}
      <div style={{ height: 92, borderRadius: 4, overflow: 'hidden', border: `0.5px solid ${T.hairThin}` }}>
        <PostcardScene scene={scene}/>
      </div>
      {/* meta */}
      <div style={{ marginTop: 10 }}>
        <TripPill kind={kind}>{label}</TripPill>
        <div style={{
          fontFamily: T.serif, fontSize: primary ? 20 : 17, fontWeight: 500, color: T.ink,
          letterSpacing: -0.3, lineHeight: 1.05, marginTop: 8,
        }}>{title}</div>
        <div style={{
          fontFamily: T.serif, fontStyle: 'italic', fontSize: 11.5, color: T.mute,
          lineHeight: 1.3, marginTop: 4,
        }}>{sub}</div>
      </div>
      {primary && (
        <div style={{
          position: 'absolute', right: 12, bottom: 12,
          width: 28, height: 28, borderRadius: 999, background: TR.ink,
          color: T.cardWarm, display: 'flex', alignItems: 'center', justifyContent: 'center',
        }}>→</div>
      )}
    </div>
  );
}

window.TripsDreamStack = TripsDreamStack;
