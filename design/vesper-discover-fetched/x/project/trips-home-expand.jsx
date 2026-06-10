// ═══════════════════════════════════════════════════════════════
// TRIPS HOME · EXPANSION MODULES (exploration).
// NOT a hero redesign — additive sections that slot BELOW the
// existing hero + drafts, in the current card language (flat
// cardWarm, hairline, upright — no stripes, no dashes). Each shows
// only when it has something real to say. Rendered as one long
// "extended home" scroll so you can see them in context.
// ═══════════════════════════════════════════════════════════════

function ExpLabel({ children, action }) {
  return (
    <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginBottom: 11 }}>
      <span style={{ fontFamily: T.mono, fontSize: 9, color: T.mute, letterSpacing: 1.8, fontWeight: 700 }}>{children}</span>
      {action && <span style={{ fontFamily: T.mono, fontSize: 8.5, color: T.goldDeep, letterSpacing: 1.2, fontWeight: 600 }}>{action}</span>}
    </div>
  );
}

// a place/suggestion row — thumb + serif name + Vesper one-liner
function SuggRow({ scene, name, line, first }) {
  return (
    <div style={{ display: 'flex', gap: 12, alignItems: 'center', padding: '12px 0', borderTop: first ? 'none' : `0.5px solid ${T.hairThin}` }}>
      <div style={{ width: 46, height: 46, borderRadius: 9, overflow: 'hidden', flexShrink: 0, background: T.cardSoft, border: `0.5px solid ${T.hairline}` }}>
        {scene && <PostcardScene scene={scene}/>}
      </div>
      <div style={{ flex: 1, minWidth: 0 }}>
        <div style={{ fontFamily: T.serif, fontSize: 16, color: T.ink, fontWeight: 500, letterSpacing: -0.2 }}>{name}</div>
        <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.mute, marginTop: 1, lineHeight: 1.3 }}>{line}</div>
      </div>
      <Marks.ArrowR s={13} c={T.faint}/>
    </div>
  );
}

// a person row — avatar + what they're doing + peek
function FriendRow({ who, c, doing, first }) {
  return (
    <div style={{ display: 'flex', gap: 12, alignItems: 'center', padding: '13px 0', borderTop: first ? 'none' : `0.5px solid ${T.hairThin}` }}>
      <div style={{ width: 36, height: 36, borderRadius: 999, background: c, color: '#fff', display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: T.serif, fontSize: 15, fontWeight: 500, flexShrink: 0, boxShadow: `0 0 0 2px ${T.bg}, 0 0 0 3px ${T.hairline}` }}>{who[0]}</div>
      <div style={{ flex: 1, minWidth: 0 }}>
        <div style={{ fontFamily: T.serif, fontSize: 15.5, color: T.ink, letterSpacing: -0.2, lineHeight: 1.15 }}><b style={{ fontWeight: 600 }}>{who}</b> {doing}</div>
      </div>
      <span style={{ fontFamily: T.mono, fontSize: 8, color: T.goldDeep, letterSpacing: 1, fontWeight: 700, border: `0.5px solid ${T.hairline}`, borderRadius: 999, padding: '5px 10px' }}>PEEK</span>
    </div>
  );
}

const ExpSection = ({ children }) => <div style={{ padding: '20px 22px 0' }}>{children}</div>;

// ── the modules, each standalone (shown stacked in the scroll) ──
function ModWhileHere() {
  const items = [
    ['tokyo', 'Bear Pond Espresso', 'a 6-min walk — the pour-over you’d cross town for'],
    ['tokyo', 'Omoide Yokocho', 'tonight — smoky, tiny, the good kind of loud'],
  ];
  return (
    <ExpSection>
      <ExpLabel action="MORE IN DISCOVER ›">WHILE YOU’RE HERE · TOKYO</ExpLabel>
      <div style={{ display: 'flex', gap: 8 }}>
        {items.map(([s, n, l]) => (
          <div key={n} style={{ flex: 1, background: T.cardWarm, borderRadius: 13, border: `0.5px solid ${T.hairline}`, overflow: 'hidden' }}>
            <div style={{ height: 84 }}><PostcardScene scene={s}/></div>
            <div style={{ padding: '10px 12px 13px' }}>
              <div style={{ fontFamily: T.serif, fontSize: 15.5, color: T.ink, fontWeight: 500, letterSpacing: -0.2, lineHeight: 1.05 }}>{n}</div>
              <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 11.5, color: T.mute, marginTop: 4, lineHeight: 1.32 }}>{l}</div>
            </div>
          </div>
        ))}
      </div>
    </ExpSection>
  );
}
function ModFriends() {
  return (
    <ExpSection>
      <ExpLabel>FRIENDS, OUT THERE</ExpLabel>
      <FriendRow who="Ana" c="#A0703A" doing="is in Mexico City this week" first/>
      <FriendRow who="Theo" c="#3D5066" doing="is planning Seoul for autumn"/>
    </ExpSection>
  );
}
function ModSaved() {
  return (
    <ExpSection>
      <ExpLabel>SAVED · NO TRIP YET</ExpLabel>
      <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
        <div style={{ display: 'flex' }}>
          {['lisbon', 'porto', 'tokyo'].map((s, i) => (
            <div key={s} style={{ width: 46, height: 46, borderRadius: 10, overflow: 'hidden', border: `2px solid ${T.bg}`, marginLeft: i ? -12 : 0, background: T.cardSoft }}><PostcardScene scene={s}/></div>
          ))}
        </div>
        <div style={{ flex: 1 }}>
          <div style={{ fontFamily: T.serif, fontSize: 15.5, color: T.ink, letterSpacing: -0.2 }}>3 places saved in Discover</div>
          <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.mute, marginTop: 1 }}>none of them belong to a trip yet</div>
        </div>
        <span style={{ fontFamily: T.mono, fontSize: 8, color: T.goldDeep, letterSpacing: 1, fontWeight: 700, border: `0.5px solid ${T.hairline}`, borderRadius: 999, padding: '5px 10px' }}>START</span>
      </div>
    </ExpSection>
  );
}
function ModResume() {
  return (
    <ExpSection>
      <ExpLabel>PICK UP WHERE YOU LEFT OFF</ExpLabel>
      <SuggRow name="Your question about Porto" line="asked 3 days ago — Vesper replied" first/>
      <SuggRow name="A draft day in Tokyo" line="two stops in, then you stopped"/>
    </ExpSection>
  );
}
// typographic — no card, like the Atlas bridge
function ModNoticed() {
  return (
    <div style={{ padding: '18px 22px 0' }}>
      <div style={{ paddingTop: 15, borderTop: `0.5px solid ${T.hairline}` }}>
        <div style={{ fontFamily: T.mono, fontSize: 8.5, color: T.goldDeep, fontWeight: 700, letterSpacing: 1.6 }}>VESPER NOTICED</div>
        <div style={{ fontFamily: T.serif, fontSize: 16.5, color: T.ink, fontWeight: 500, letterSpacing: -0.2, marginTop: 7, lineHeight: 1.32 }}>Porto flights are up 9% since you looked.</div>
        <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.goldDeep, marginTop: 6 }}>Still worth it — but I’d book this week →</div>
      </div>
    </div>
  );
}

// ── the assembled extended home — a long scroll, real context ──
function HomeExtendedScroll() {
  return (
    <div style={{ width: 393, background: T.bg, paddingBottom: 30, boxShadow: '0 20px 60px -30px rgba(0,0,0,0.4)', borderRadius: 20, overflow: 'hidden' }}>
      <div style={{ height: 50 }}/>
      <TripsTopBar eyebrow="TRIPS · TOKYO IN 58 DAYS"/>
      <div style={{ padding: '16px 22px 0' }}>
        <h1 style={{ fontFamily: T.serif, fontWeight: 500, fontSize: 36, lineHeight: 0.96, letterSpacing: -1, color: T.ink, margin: 0 }}>Your planning table.</h1>
      </div>
      <HeroAliveTrip title="Tokyo, in May" days="Sat 14 → Fri 22" nights="8 NIGHTS" countdown="ALIVE · 58 DAYS OUT" scene="tokyo" next="Pick a ryokan for nights 5–7"/>
      <DraftsScatter rows={[
        { title: 'Porto, return', meta: 'september · pencilled in', kind: 'alive', pillText: 'PENCILLED' },
        { title: 'A weekend somewhere quiet', meta: 'no dates · 1 traveler', kind: 'dreaming', pillText: 'DREAMING' },
      ]}/>
      {/* the new, additive sections — the home grows downward */}
      <ModWhileHere/>
      <ModFriends/>
      <ModSaved/>
      <ModResume/>
      <ModNoticed/>
      <AtlasBridge body="Vesper has a postcard waiting from Lisbon." kicker="LAST TRIP · LISBON"/>
    </div>
  );
}

Object.assign(window, { HomeExtendedScroll, ModWhileHere, ModFriends, ModSaved, ModResume, ModNoticed });
