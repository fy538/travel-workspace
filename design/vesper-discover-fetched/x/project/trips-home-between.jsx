// ═══════════════════════════════════════════════════════════════
// TRIPS HOME · BETWEEN TRIPS + THE EVERYDAY (exploration).
// The thesis surface: a relationship with places is continuous, so
// the home stays alive with NOTHING dated. Powered by the
// memory→intent loop (Atlas taste → Discover world) and the
// everyday (your city). Existing card language — flat tiles,
// hairline, no stripes/dashes. Reuses global ExpLabel/SuggRow/FriendRow.
// ═══════════════════════════════════════════════════════════════

const BSec = ({ children }) => <div style={{ padding: '20px 22px 0' }}>{children}</div>;

// a quiet typographic passage (no card) — Vesper's voice
function BPassage({ kicker, line, tail }) {
  return (
    <div style={{ padding: '18px 22px 0' }}>
      <div style={{ paddingTop: 15, borderTop: `0.5px solid ${T.hairline}` }}>
        <div style={{ fontFamily: T.mono, fontSize: 8.5, color: T.goldDeep, fontWeight: 700, letterSpacing: 1.6 }}>{kicker}</div>
        <div style={{ fontFamily: T.serif, fontSize: 16.5, color: T.ink, fontWeight: 500, letterSpacing: -0.2, marginTop: 7, lineHeight: 1.34 }}>{line}</div>
        {tail && <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.goldDeep, marginTop: 6 }}>{tail}</div>}
      </div>
    </div>
  );
}

// ─── A · BETWEEN TRIPS — nothing dated, still alive ─────────────
function HomeBetween() {
  return (
    <Phone bg={T.bg}>
      <TripsTopBar eyebrow="TRIPS · NOTHING DATED"/>
      {/* Vesper standfirst — the relationship, not an empty state */}
      <div style={{ padding: '16px 22px 0' }}>
        <h1 style={{ fontFamily: T.serif, fontWeight: 500, fontSize: 31, lineHeight: 1.04, letterSpacing: -0.8, color: T.ink, margin: 0 }}>
          Nothing booked — <span style={{ fontStyle: 'italic' }}>which is its own kind of open.</span>
        </h1>
      </div>

      {/* the memory → intent loop (the soul) */}
      <BPassage kicker="VESPER · A READ ON YOU" line="You keep returning to the quiet, food-first corners — Lisbon, Porto, the edges of Mexico City." tail="Porto has more of them. Want me to start something? →"/>

      {/* still circling — saved dreams as tiles */}
      <BSec>
        <ExpLabel action="ALL SAVED ›">STILL CIRCLING</ExpLabel>
        <div style={{ display: 'flex', gap: 8 }}>
          {[['lisbon', 'Lisbon', 'saved 3 times'], ['tokyo', 'Tokyo', 'a someday-soon']].map(([s, n, m]) => (
            <div key={n} style={{ flex: 1, background: T.cardWarm, borderRadius: 12, border: `0.5px solid ${T.hairline}`, overflow: 'hidden' }}>
              <div style={{ height: 70 }}><PostcardScene scene={s}/></div>
              <div style={{ padding: '9px 11px 11px' }}>
                <div style={{ fontFamily: T.serif, fontSize: 15, color: T.ink, fontWeight: 500, letterSpacing: -0.2 }}>{n}</div>
                <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 11.5, color: T.mute, marginTop: 1 }}>{m}</div>
              </div>
            </div>
          ))}
        </div>
      </BSec>

      {/* friends keep the world moving */}
      <BSec>
        <ExpLabel>FRIENDS, OUT THERE</ExpLabel>
        <FriendRow who="Ana" c="#A0703A" doing="is in Mexico City this week" first/>
        <FriendRow who="Theo" c="#3D5066" doing="is planning Seoul for autumn"/>
      </BSec>

      {/* a Discover read worth noticing */}
      <BSec>
        <ExpLabel action="OPEN ›">WORTH READING</ExpLabel>
        <SuggRow scene="porto" name="Why Porto, now" line="a field note — the coast before the crowds return" first/>
      </BSec>

      <AtlasBridge body="A postcard from Lisbon is still on your desk." kicker="FROM YOUR ATLAS" cta="Open in Atlas →"/>
      <TabBar active="trips"/>
    </Phone>
  );
}

// ─── B · NEAR YOU — the everyday, your home city ────────────────
function HomeNearYou() {
  return (
    <div style={{ width: 393, background: T.bg, paddingBottom: 30, boxShadow: '0 20px 60px -30px rgba(0,0,0,0.4)', borderRadius: 20, overflow: 'hidden' }}>
      <div style={{ height: 50 }}/>
      <TripsTopBar eyebrow="HOME · BROOKLYN"/>
      <div style={{ padding: '16px 22px 0' }}>
        <h1 style={{ fontFamily: T.serif, fontWeight: 500, fontSize: 33, lineHeight: 0.98, letterSpacing: -0.9, color: T.ink, margin: 0 }}>
          Your city, <span style={{ fontStyle: 'italic' }}>still being read.</span>
        </h1>
      </div>

      <BPassage kicker="VESPER · NEAR YOU" line="You haven’t tried somewhere new in three weeks." tail="Two places opened in Fort Greene that are your kind of quiet →"/>

      {/* places you return to */}
      <BSec>
        <ExpLabel action="ON YOUR MAP ›">YOU KEEP RETURNING TO</ExpLabel>
        <SuggRow scene="lisbon" name="Saraghina" line="6 visits — the corner table, always" first/>
        <SuggRow scene="porto" name="The promenade" line="your dusk walk, most weeks"/>
      </BSec>

      {/* new near you */}
      <BSec>
        <ExpLabel action="MORE IN DISCOVER ›">NEW, NEARBY</ExpLabel>
        <SuggRow scene="tokyo" name="Cafe Kitsuné" line="just opened, 8 min — Vesper thinks yes" first/>
      </BSec>

      {/* the everyday becomes memory too */}
      <AtlasBridge body="Your Brooklyn year is quietly filling in Atlas." kicker="HOME · KEPT" cta="Open in Atlas →"/>
    </div>
  );
}

Object.assign(window, { HomeBetween, HomeNearYou });
