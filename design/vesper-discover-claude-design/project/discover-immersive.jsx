// ═══════════════════════════════════════════════════════════════
// IMMERSIVE TREATMENT — the "Desire Engine" instinct, folded into the
// system as the Dream shape's full-bleed variant (no-trip, outward).
// Near-full-bleed house illustration, one evocative line, a restrained
// "Next, if this moves you" pair. No influencer captions, no metrics.
// Reuses discover-illus (VesperScene) + discover-kit (D, DIcon, Spark, LensChip).
// ═══════════════════════════════════════════════════════════════

function ImmersiveHome() {
  return (
    <Phone bg={T.ink}>
      <div style={{ position: 'absolute', inset: 0, overflow: 'hidden', background: T.ink }}>
        {/* full-bleed illustrated hero */}
        <div style={{ position: 'absolute', inset: 0, height: 620 }}><VesperScene w={393} h={620} time="amber"/></div>
        <div style={{ position: 'absolute', inset: 0, height: 620, background: 'linear-gradient(to bottom, rgba(20,14,9,0.34) 0%, rgba(20,14,9,0) 26%, rgba(20,14,9,0) 50%, rgba(20,14,9,0.78) 100%)' }}/>

        {/* top */}
        <div style={{ position: 'absolute', top: 56, left: 20, right: 20, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <h1 style={{ fontFamily: T.serif, fontSize: 24, fontWeight: 500, letterSpacing: -0.5, color: '#fff', margin: 0 }}>Discover</h1>
          <div style={{ display: 'flex', gap: 14 }}>{DIcon.settings('rgba(255,255,255,0.9)')}{DIcon.saved('rgba(255,255,255,0.9)')}</div>
        </div>

        {/* glass seg control floating on the image */}
        <div style={{ position: 'absolute', top: 98, left: 20, right: 20 }}>
          <div style={{ display: 'inline-flex', background: 'rgba(255,255,255,0.16)', backdropFilter: 'blur(10px)', borderRadius: 999, padding: 3 }}>
            {['For you','Vesper','Friends'].map((t,i)=>(
              <span key={t} style={{ padding: '7px 15px', borderRadius: 999, fontSize: 12.5, fontWeight: i===1?600:500, color: i===1?T.ink:'rgba(255,255,255,0.85)', background: i===1?'rgba(255,255,255,0.92)':'transparent', letterSpacing: -0.1 }}>{t}</span>
            ))}
          </div>
        </div>

        {/* hero copy low — the first viewport is JUST the read. */}
        <div style={{ position: 'absolute', left: 22, right: 22, bottom: 150 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 11 }}>
            <Spark s={13} c="#fff"/><span style={{ fontSize: 9.5, letterSpacing: 1.6, fontWeight: 700, color: 'rgba(255,255,255,0.92)' }}>VESPER’S READ · WHERE NEXT</span>
          </div>
          <h2 style={{ fontFamily: T.serif, fontSize: 37, fontWeight: 500, letterSpacing: -1, lineHeight: 1.02, color: '#fff', margin: 0 }}>
            Lisbon, after<br/><span style={{ fontStyle: 'italic' }}>the light goes amber.</span>
          </h2>
          <p style={{ fontFamily: T.serif, fontSize: 14.5, color: 'rgba(255,255,255,0.82)', lineHeight: 1.4, margin: '12px 0 0', maxWidth: 300, letterSpacing: -0.1 }}>
            The hour the whole city steps outside and the hills start to glow from within.
          </p>
          <div style={{ marginTop: 16, display: 'flex', alignItems: 'center', gap: 12 }}>
            <span style={{ padding: '11px 20px', background: '#fff', color: T.ink, borderRadius: 999, fontSize: 13.5, fontWeight: 600, letterSpacing: -0.1, display: 'inline-flex', alignItems: 'center', gap: 6 }}>
              Read this <span style={{ color: D.vesper }}>→</span>
            </span>
            <span style={{ display: 'inline-flex', alignItems: 'center', gap: 5, color: 'rgba(255,255,255,0.78)', fontSize: 12.5, fontWeight: 600 }}>
              <span style={{ fontSize: 14 }}>+</span> Vesper
            </span>
          </div>
        </div>

        {/* scroll cue — the feed lives below the fold */}
        <div style={{ position: 'absolute', left: 0, right: 0, bottom: 92, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 5, color: 'rgba(255,255,255,0.7)' }}>
          <span style={{ fontSize: 9, letterSpacing: 2, fontWeight: 700 }}>MORE BELOW</span>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.7)" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M6 9l6 6 6-6"/></svg>
        </div>
      </div>
      <TabBar active="discover"/>
    </Phone>
  );
}

// What you get when you scroll down from the immersive hero: the photo
// recedes to a condensed band and a parchment sheet rises with the
// "Next, if this moves you" pair, then the curated feed.
function ImmersiveScroll() {
  const teaser = (time, lens, t) => (
    <div style={{ flex: 1, borderRadius: 14, overflow: 'hidden', position: 'relative', height: 146 }}>
      <div style={{ position: 'absolute', inset: 0 }}><VesperScene w={170} h={146} time={time}/></div>
      <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0) 38%, rgba(20,14,9,0.72) 100%)' }}/>
      <div style={{ position: 'absolute', left: 11, right: 11, bottom: 11 }}>
        <div style={{ fontSize: 8.5, letterSpacing: 1.4, fontWeight: 700, color: 'rgba(255,255,255,0.78)' }}>{lens}</div>
        <div style={{ fontFamily: T.serif, fontSize: 14, fontWeight: 500, color: '#fff', letterSpacing: -0.2, lineHeight: 1.15, marginTop: 4 }}>{t}</div>
      </div>
    </div>
  );
  return (
    <div style={{ width: 393, background: T.bg, borderRadius: 30, overflow: 'hidden', border: `0.5px solid ${T.hairline}`, boxShadow: '0 30px 60px -30px rgba(0,0,0,0.3)', position: 'relative', paddingBottom: 8 }}>
      {/* condensed hero band — the photo has receded, title pinned small */}
      <div style={{ position: 'relative', height: 168, overflow: 'hidden' }}>
        <div style={{ position: 'absolute', inset: 0 }}><VesperScene w={393} h={168} time="amber"/></div>
        <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.5) 0%, rgba(20,14,9,0.1) 45%, rgba(20,14,9,0.66) 100%)' }}/>
        <div style={{ position: 'absolute', top: 40, left: 22, right: 22, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <span style={{ fontFamily: T.serif, fontSize: 18, fontWeight: 500, color: '#fff', letterSpacing: -0.3 }}>Lisbon, after the amber</span>
          <span style={{ display: 'inline-flex', alignItems: 'center', gap: 4, color: 'rgba(255,255,255,0.85)', fontSize: 11.5, fontWeight: 600 }}><Spark s={11} c="#fff"/> Read</span>
        </div>
        <div style={{ position: 'absolute', left: 0, right: 0, bottom: 0, height: 18, background: T.bg, borderRadius: '18px 18px 0 0' }}/>
      </div>

      {/* parchment continuation */}
      <div style={{ padding: '4px 16px 0' }}>
        <div style={{ fontSize: 9.5, letterSpacing: 2, color: T.mute, fontWeight: 700, marginBottom: 11, paddingLeft: 6 }}>NEXT, IF THIS MOVES YOU</div>
        <div style={{ display: 'flex', gap: 12 }}>
          {teaser('amber','RITUAL','Where to swim within an hour')}
          {teaser('day','THE DEBATE','The street that resists you')}
        </div>
      </div>

      <FeedSection label="THE SAME HOUR, ELSEWHERE" right="VESPER">
        <FeedRow v="coast" lens="Why here" title="Trastevere goes gold at the same clock" meta="ROME · 4 MIN"/>
        <FeedRow v="hills" lens="Insider" title="Valparaíso, when the hills light up" meta="CHILE · 5 MIN"/>
      </FeedSection>
      <FeedSection label="IF YOU’D RATHER CHASE IT" right="DREAM">
        <FeedLead v="coast" lens="A day in" title="Three cities built for the golden hour" hook="Where the light, not the landmark, is the reason to go."/>
      </FeedSection>

      {/* end marker */}
      <div style={{ padding: '22px 22px 16px', textAlign: 'center' }}>
        <div style={{ display: 'inline-flex', alignItems: 'center', gap: 8, color: T.muteSoft }}>
          <span style={{ width: 18, height: 1, background: T.muteSoft, opacity: 0.5 }}/>
          <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.mute }}>that’s what moves Vesper — not everything</span>
          <span style={{ width: 18, height: 1, background: T.muteSoft, opacity: 0.5 }}/>
        </div>
      </div>
      <div style={{ margin: '0 16px 4px', background: 'rgba(247,242,231,0.92)', borderRadius: 26, border: `0.5px solid ${T.hairline}`, boxShadow: '0 8px 24px -8px rgba(0,0,0,0.12)', display: 'flex', justifyContent: 'space-between', padding: '11px 22px' }}>
        {['Trips','Vesper','Discover','Atlas'].map((t,i)=>(<span key={t} style={{ fontSize: 11, fontWeight: i===2?700:500, color: i===2?T.ink:T.muteSoft, letterSpacing: 0.2 }}>{t}</span>))}
      </div>
    </div>
  );
}

function ImmersiveDossier() {
  return (
    <Phone bg={T.ink}>
      <div style={{ position: 'absolute', inset: 0, overflow: 'hidden', background: T.bg }}>
        {/* tall immersive illustrated hero */}
        <div style={{ position: 'absolute', top: 0, left: 0, right: 0, height: 408 }}><VesperScene w={393} h={408} time="amber"/></div>
        <div style={{ position: 'absolute', top: 0, left: 0, right: 0, height: 408, background: 'linear-gradient(to bottom, rgba(20,14,9,0.42) 0%, rgba(20,14,9,0) 30%, rgba(20,14,9,0) 50%, rgba(20,14,9,0.8) 100%)' }}/>
        <div style={{ position: 'absolute', top: 56, left: 18, right: 18, display: 'flex', justifyContent: 'space-between' }}>
          <div style={{ width: 38, height: 38, borderRadius: 999, background: 'rgba(255,255,255,0.2)', backdropFilter: 'blur(8px)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>{DIcon.back('#fff')}</div>
          <div style={{ width: 38, height: 38, borderRadius: 999, background: 'rgba(255,255,255,0.2)', backdropFilter: 'blur(8px)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>{DIcon.save('#fff')}</div>
        </div>
        <div style={{ position: 'absolute', top: 298, left: 22, right: 22 }}>
          <div style={{ marginBottom: 10 }}><LensChip lens="Ritual" onDark/></div>
          <h1 style={{ fontFamily: T.serif, fontSize: 30, fontWeight: 500, letterSpacing: -0.7, lineHeight: 1.05, color: '#fff', margin: 0 }}>
            Lisbon, after the light goes amber
          </h1>
        </div>

        {/* read on parchment */}
        <div style={{ position: 'absolute', top: 408, left: 0, right: 0, bottom: 0, background: T.bg, padding: '18px 22px 0' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, fontFamily: T.mono, fontSize: 9.5, color: T.muteSoft, letterSpacing: 1 }}>
            <span style={{ color: D.earth, fontWeight: 600 }}>LISBON</span><span>·</span><span>6 MIN</span><span>·</span>
            <span style={{ display: 'inline-flex', alignItems: 'center', gap: 4, color: D.vesper, fontWeight: 600 }}><Spark s={10}/> VESPER</span>
          </div>
          <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 17, color: T.ink, lineHeight: 1.4, margin: '14px 0 0', letterSpacing: -0.2 }}>
            There is one hour here you should refuse to spend indoors.
          </p>
          <p style={{ fontFamily: T.serif, fontSize: 15.5, color: T.inkSoft, lineHeight: 1.6, margin: '14px 0 0', letterSpacing: -0.05 }}>
            It starts about forty minutes before sunset, when the limestone stops being white and the whole western face of the city turns the colour of a struck match.
          </p>
        </div>
      </div>
      <DossierBar variant="editorial"/>
    </Phone>
  );
}

Object.assign(window, { ImmersiveHome, ImmersiveScroll, ImmersiveDossier });
