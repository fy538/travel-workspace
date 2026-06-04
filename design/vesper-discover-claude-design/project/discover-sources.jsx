// ═══════════════════════════════════════════════════════════════
// THREE SOURCES — For you / Vesper / Friends. Same place (Lisbon),
// three different "outsides". Rail-pill seg control marks which is active.
// ═══════════════════════════════════════════════════════════════

// 1 · FOR YOU — the world filtered through YOUR taste.
function SourceForYou() {
  return (
    <Phone bg={T.bg}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <DiscoverTop place="Lisbon" context="Lisbon · tuned to you" active={0}/>
        <div style={{ padding: '16px 16px 0' }}>
          <ReadFrame place="Lisbon" kicker="VESPER’S READ · FOR YOU" updated="">
            <div style={{ padding: '10px 16px 4px' }}>
              <p style={{ fontFamily: T.serif, fontSize: 17, fontWeight: 500, color: T.ink, letterSpacing: -0.2, lineHeight: 1.3, margin: 0 }}>
                Given how you travel, <span style={{ fontStyle: 'italic' }}>start with the food.</span>
              </p>
              <div style={{ marginTop: 8, display: 'flex', gap: 6, flexWrap: 'wrap' }}>
                {['quiet streets', 'one dinner alone', 'no chains'].map(t => (
                  <span key={t} style={{ padding: '4px 9px', fontFamily: T.serif, fontStyle: 'italic', fontSize: 11, color: T.inkSoft, background: T.cardSoft, borderRadius: 999, border: `0.5px solid ${T.hairline}` }}>{t}</span>
                ))}
              </div>
            </div>
            <div style={{ padding: '6px 16px 12px' }}>
              <ReadLine tag="FOR YOU" color={D.vesper} lens="Why here" first>Layered food cultures at every price — your kind of city.</ReadLine>
              <ReadLine tag="FOR YOU" color={D.vesper} lens="Ritual">Morning bica on the same step, three days running.</ReadLine>
            </div>
          </ReadFrame>
          <div style={{ marginTop: 8, fontSize: 10.5, color: T.muteSoft, fontStyle: 'italic', fontFamily: T.serif, textAlign: 'center' }}>
            reordered for you · <span style={{ color: D.vesper }}>tune what Vesper weighs</span>
          </div>
        </div>
      </div>
      <TabBar active="discover"/>
    </Phone>
  );
}

// 2 · VESPER — the unfiltered canon. Authoritative, includes the debate.
function SourceVesper() {
  return (
    <Phone bg={T.bg}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <DiscoverTop place="Lisbon" context="Lisbon · Vesper’s own read" active={1}/>
        <div style={{ padding: '16px 16px 0' }}>
          <ReadFrame place="Lisbon" kicker="VESPER’S READ · THE CANON" updated="">
            <div style={{ padding: '10px 16px 4px' }}>
              <p style={{ fontFamily: T.serif, fontSize: 17, fontWeight: 500, color: T.ink, letterSpacing: -0.2, lineHeight: 1.3, margin: 0 }}>
                What matters about Lisbon, <span style={{ fontStyle: 'italic' }}>whoever you are.</span>
              </p>
            </div>
            <div style={{ padding: '2px 16px 12px' }}>
              <ReadLine tag="MATTERS" color={STANCE.matters} lens="Why here" first>The miradouro culture — the city reads from above.</ReadLine>
              <ReadLine tag="DEBATE" color={'#A04030'} lens="The debate">Is Alfama still Alfama, or a stage now? Vesper takes a side.</ReadLine>
              <ReadLine tag="CANON" color={STANCE.matters} lens="Insider">Fado isn’t nightlife here; it’s closer to grief.</ReadLine>
            </div>
          </ReadFrame>
          <div style={{ marginTop: 8, fontSize: 10.5, color: T.muteSoft, fontStyle: 'italic', fontFamily: T.serif, textAlign: 'center' }}>
            not personalized — this is the house view
          </div>
        </div>
      </div>
      <TabBar active="discover"/>
    </Phone>
  );
}

// 3 · FRIENDS — trusted people's actual saves + notes. Attributed.
function SourceFriends() {
  const A = (who, color, init) => (
    <div style={{ width: 22, height: 22, borderRadius: 999, background: color, color: '#fff', display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: T.serif, fontSize: 11, fontWeight: 500, flexShrink: 0 }}>{init}</div>
  );
  return (
    <Phone bg={T.bg}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <DiscoverTop place="Lisbon" context="Lisbon · people you trust" active={2}/>
        <div style={{ padding: '16px 16px 0' }}>
          {/* who's been */}
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, padding: '0 6px 12px' }}>
            <div style={{ display: 'flex' }}>
              {[['#7C8F73','A'],['#A0703A','T'],['#3D5066','M']].map(([c,i],idx)=>(
                <span key={idx} style={{ marginLeft: idx?-7:0 }}>{A('x',c,i)}</span>
              ))}
            </div>
            <span style={{ fontSize: 12, color: T.mute, fontFamily: T.serif, fontStyle: 'italic' }}>Ana, Theo &amp; Mara have been to Lisbon</span>
          </div>

          {/* a friend's saved place w/ their note */}
          <div style={{ background: T.cardWarm, borderRadius: 14, border: `0.5px solid ${T.hairline}`, overflow: 'hidden', boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset' }}>
            <div style={{ display: 'flex', gap: 0 }}>
              <Plate variant="alley" style={{ width: 92, flexShrink: 0 }}/>
              <div style={{ flex: 1, padding: '12px 14px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>{A('x','#7C8F73','A')}<span style={{ fontSize: 11.5, fontWeight: 600, color: T.ink }}>Ana saved</span></div>
                <div style={{ fontFamily: T.serif, fontSize: 16, fontWeight: 500, color: T.ink, letterSpacing: -0.2, lineHeight: 1.15, marginTop: 7 }}>A Cevicheria, Príncipe Real</div>
              </div>
            </div>
            <div style={{ padding: '0 14px 13px' }}>
              <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.inkSoft, lineHeight: 1.4, margin: '2px 0 0', paddingLeft: 11, borderLeft: `2px solid ${'#7C8F73'}` }}>
                “no reservations — go at 6, before the line. the octopus, not the ceviche.”
              </p>
            </div>
          </div>

          {/* a friend reading something */}
          <div style={{ marginTop: 10, display: 'flex', alignItems: 'center', gap: 11, padding: '11px 13px', background: T.cardWarm, borderRadius: 12, border: `0.5px solid ${T.hairline}` }}>
            {A('x','#A0703A','T')}
            <div style={{ flex: 1, minWidth: 0 }}>
              <div style={{ fontSize: 11, color: T.mute }}><b style={{ color: T.ink, fontWeight: 600 }}>Theo</b> is reading</div>
              <div style={{ fontFamily: T.serif, fontSize: 13.5, color: T.ink, letterSpacing: -0.1, marginTop: 2, lineHeight: 1.2 }}>Mouraria’s triple-layered tension</div>
            </div>
            <span style={{ color: T.muteSoft, fontSize: 12 }}>→</span>
          </div>
          <div style={{ marginTop: 10, fontSize: 10.5, color: T.muteSoft, fontStyle: 'italic', fontFamily: T.serif, textAlign: 'center' }}>
            only people you’ve added · no strangers, no metrics
          </div>
        </div>
      </div>
      <TabBar active="discover"/>
    </Phone>
  );
}

Object.assign(window, { SourceForYou, SourceVesper, SourceFriends });
