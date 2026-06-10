// ═══════════════════════════════════════════════════════════════
// TRIPS HOME · THE SYSTEM (not a free-for-all).
// The home is dynamic — but dynamism runs on rules. This board
// standardizes the home into a small design system: the card
// vocabulary, the section types (with appear-rules), and the
// governing principles. Reuses global atoms (TripPill, AtlasBridge,
// BPassage, SuggRow, FriendRow).
// ═══════════════════════════════════════════════════════════════

function HomeSystem() {
  const Col = ({ title, children }) => (
    <div style={{ flex: 1, minWidth: 0 }}>
      <div style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 2, color: T.goldDeep, fontWeight: 700, paddingBottom: 12, borderBottom: `0.5px solid ${T.hairline}`, marginBottom: 16 }}>{title}</div>
      {children}
    </div>
  );
  const Spec = ({ name, when, children }) => (
    <div style={{ marginBottom: 20 }}>
      <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginBottom: 8 }}>
        <span style={{ fontFamily: T.serif, fontSize: 15, color: T.ink, fontWeight: 600, letterSpacing: -0.2 }}>{name}</span>
        <span style={{ fontFamily: T.mono, fontSize: 8, color: T.muteSoft, letterSpacing: 1, fontWeight: 600 }}>{when}</span>
      </div>
      <div style={{ width: 300 }}>{children}</div>
    </div>
  );
  const Rule = ({ n, t, children }) => (
    <div style={{ marginBottom: 16 }}>
      <div style={{ fontFamily: T.serif, fontSize: 15.5, color: T.ink, fontWeight: 500, letterSpacing: -0.2 }}><span style={{ color: T.goldDeep, fontStyle: 'italic' }}>{n}.</span> {t}</div>
      <div style={{ fontFamily: T.serif, fontSize: 13, color: T.mute, lineHeight: 1.5, marginTop: 3 }}>{children}</div>
    </div>
  );
  // a sample draft/now tile (the one card grammar)
  const tile = (pill, kind, title, meta) => (
    <div style={{ width: 145, padding: '12px 13px', background: T.cardWarm, borderRadius: 12, border: `0.5px solid ${T.hairline}` }}>
      <TripPill kind={kind}>{pill}</TripPill>
      <div style={{ fontFamily: T.serif, fontSize: 14.5, color: T.ink, fontWeight: 500, letterSpacing: -0.2, marginTop: 8 }}>{title}</div>
      <div style={{ fontSize: 10.5, color: T.mute, fontFamily: T.serif, marginTop: 4 }}>{meta}</div>
    </div>
  );

  return (
    <div style={{ width: 1080, padding: '44px 46px', background: '#F1ECE2', borderRadius: 10, color: T.inkSoft }}>
      <div style={{ fontFamily: T.mono, fontSize: 10.5, letterSpacing: 2, color: T.gold, fontWeight: 600 }}>VESPER · TRIPS HOME · THE SYSTEM</div>
      <h1 style={{ fontFamily: T.serif, fontSize: 44, fontWeight: 500, letterSpacing: -1.2, lineHeight: 0.98, color: T.ink, margin: '8px 0 10px' }}>Dynamic, <span style={{ fontStyle: 'italic' }}>but not a free-for-all.</span></h1>
      <p style={{ fontFamily: T.serif, fontSize: 15, color: T.soft, lineHeight: 1.5, margin: '0 0 30px', maxWidth: 680 }}>The home re-composes itself by what’s true right now — so it needs a fixed vocabulary underneath. Three things hold it together: a single card grammar, a fixed set of sections that each appear only on a rule, and the principles that govern the whole.</p>

      <div style={{ display: 'flex', gap: 40, borderTop: `0.5px solid ${T.hairline}`, paddingTop: 26 }}>
        {/* ── THE CARDS ── */}
        <Col title="THE CARD VOCABULARY">
          <Spec name="The tile" when="DRAFTS · BEATS">
            <div style={{ display: 'flex', gap: 8 }}>
              {tile('PENCILLED', 'alive', 'Porto, return', 'september')}
              {tile('DREAMING', 'dreaming', 'A quiet weekend', 'no dates')}
            </div>
          </Spec>
          <Spec name="Image card" when="SUGGESTIONS">
            <div style={{ display: 'flex', gap: 8, width: 300 }}>
              {['tokyo', 'porto'].map((s) => (
                <div key={s} style={{ flex: 1, background: T.cardWarm, borderRadius: 12, border: `0.5px solid ${T.hairline}`, overflow: 'hidden' }}>
                  <div style={{ height: 64 }}><PostcardScene scene={s}/></div>
                  <div style={{ padding: '8px 10px 10px' }}>
                    <div style={{ fontFamily: T.serif, fontSize: 13.5, color: T.ink, fontWeight: 500 }}>{s === 'tokyo' ? 'Bear Pond' : 'The promenade'}</div>
                    <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 10.5, color: T.mute, marginTop: 2 }}>{s === 'tokyo' ? '6-min walk' : 'your dusk walk'}</div>
                  </div>
                </div>
              ))}
            </div>
          </Spec>
          <Spec name="Person row" when="FRIENDS">
            <FriendRow who="Ana" c="#A0703A" doing="is in Mexico City" first/>
          </Spec>
          <Spec name="Typographic passage" when="VESPER'S VOICE">
            <div style={{ marginLeft: -22 }}><BPassage kicker="VESPER NOTICED" line="Porto flights are up 9%." tail="I’d book this week →"/></div>
          </Spec>
          <Spec name="The hero" when="ELEVATED · ONE">
            <div style={{ width: 300, padding: '13px 14px', background: T.cardWarm, borderRadius: 14, border: `0.5px solid ${T.hairline}`, boxShadow: '0 14px 30px -20px rgba(0,0,0,0.22)' }}>
              <div style={{ fontFamily: T.mono, fontSize: 8, color: T.goldDeep, letterSpacing: 1.4, fontWeight: 700 }}>TOKYO · NEXT</div>
              <div style={{ fontFamily: T.serif, fontSize: 17, color: T.ink, fontWeight: 500, letterSpacing: -0.3, marginTop: 6 }}>Pick a ryokan for nights 5–7.</div>
            </div>
          </Spec>
          <Spec name="Facet glance" when="STATUS ROW">
            <div style={{ width: 300, display: 'grid', gridTemplateColumns: 'repeat(4,1fr)', gap: 6 }}>
              {[['STAY', '✓'], ['TRANS', '2/3'], ['COSTS', '€1.4k'], ['ROUTE', '3']].map(([k, v]) => (
                <div key={k}><div style={{ fontFamily: T.mono, fontSize: 7.5, color: T.mute, letterSpacing: 1, fontWeight: 700 }}>{k}</div><div style={{ fontFamily: T.serif, fontSize: 13, color: T.ink, fontWeight: 500, marginTop: 3 }}>{v}</div></div>
              ))}
            </div>
          </Spec>
          <Spec name="Status pills" when="STATE TAGS">
            <div style={{ display: 'flex', gap: 6 }}>
              <TripPill kind="alive">ALIVE</TripPill><TripPill kind="dreaming">DREAMING</TripPill><TripPill kind="needs">NEEDS YOU</TripPill>
            </div>
          </Spec>
          <Spec name="Seed / shape card" when="COLD · CREATE">
            <SeedCard title="Lisbon" sub="in spring" line="tile light, long lunches, warm evenings out" meta="5–6 DAYS · FOOD-LED"/>
          </Spec>
          <Spec name="Atlas bridge" when="MEMORY LOOP">
            <div style={{ marginLeft: -22 }}><AtlasBridge kicker="FROM YOUR ATLAS" body="A postcard from Lisbon is on your desk." cta="Open in Atlas →"/></div>
          </Spec>
        </Col>

        {/* ── THE SECTIONS ── */}
        <Col title="THE SECTIONS (FIXED SET)">
          {[
            ['Hero', 'always — one only', 'The single elevated block. Its treatment is the state (live / countdown / returned / planning / cold / between).'],
            ['Drafts', 'label: ON THE TABLE · N', 'Upright tiles. The other trips on the table — one canonical eyebrow across every state (no KEPT WARM / STILL ON THE TABLE / ON THE BOARD drift).'],
            ['While you’re here', 'on a trip', 'Taste-matched Discover suggestions for now.'],
            ['Friends', 'when friends are moving', 'Who’s travelling or planning. Peek / ask.'],
            ['Saved, no trip', 'when saves are unplaced', 'Turn Discover saves into a plan.'],
            ['Dream seeds', 'cold / empty', 'Label: OR, SOMEWHERE FOR YOUR TASTE. Taste-led places to begin from — the cold-home invitation. Routes into Begin.'],
            ['Vesper noticed', 'rarely — when it matters', 'One typographic advisory. Never standing.'],
            ['Atlas bridge', 'after a trip / always', 'The memory loop — backward and forward.'],
          ].map(([n, w, d]) => (
            <div key={n} style={{ padding: '11px 0', borderTop: `0.5px solid ${T.hairThin}` }}>
              <div style={{ fontFamily: T.mono, fontSize: 8, color: T.goldDeep, letterSpacing: 1, fontWeight: 700, marginBottom: 3 }}>{w}</div>
              <div style={{ fontFamily: T.serif, fontSize: 15, color: T.ink, fontWeight: 500, letterSpacing: -0.2 }}>{n}</div>
              <div style={{ fontFamily: T.serif, fontSize: 12.5, color: T.mute, lineHeight: 1.4, marginTop: 3 }}>{d}</div>
            </div>
          ))}
        </Col>

        {/* ── THE RULES ── */}
        <Col title="THE GOVERNING RULES">
          <Rule n="1" t="One hero, chosen by a cascade.">on a trip → live · soon → countdown · just back → Atlas · drafts → planning · empty → cold/between. Exactly one is elevated.</Rule>
          <Rule n="2" t="One card grammar.">Flat cardWarm, hairline, upright. No tilt, no shadows except the single hero, no left-stripes, no dashed/coupon borders — ever.</Rule>
          <Rule n="3" t="Sections appear on a rule, never by whim.">Each shows only when it has something true to say; order is fixed. Dynamism = which show, not how they look.</Rule>
          <Rule n="4" t="Italic = Vesper’s voice. Gold = Vesper authored.">Facts are roman. The one saturated accent marks Vesper speaking or an action — nothing decorative.</Rule>
          <Rule n="5" t="Finite, never a feed.">A curated few per section, a visible end. The home reports what’s true, not an endless stream.</Rule>
          <Rule n="6" t="One label per section.">A section keeps the same eyebrow everywhere — Drafts is always “ON THE TABLE · N”, never re-named per state. Tone lives in Vesper’s prose, not the labels.</Rule>
        </Col>
      </div>
    </div>
  );
}

Object.assign(window, { HomeSystem });
