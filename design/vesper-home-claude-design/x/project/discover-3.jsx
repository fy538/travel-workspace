// ═══════════════════════════════════════════════════════════════
// DIRECTION 3 · DESIRE ENGINE
// Immersive and emotionally tempting. Large imagery, fewer/stronger
// cards, more "I want to go there." Tasteful, not influencer-like.
// ═══════════════════════════════════════════════════════════════

function D3Home() {
  return (
    <Phone bg={T.ink}>
      <div style={{ position: 'absolute', inset: 0, overflow: 'hidden', background: T.ink }}>
        {/* Full-bleed hero fills most of the viewport */}
        <Plate variant="hills" style={{ position: 'absolute', inset: 0, height: 620 }} dim={0.28}/>
        <div style={{ position: 'absolute', inset: 0, height: 620, background: 'linear-gradient(to bottom, rgba(20,14,9,0.30) 0%, rgba(20,14,9,0) 28%, rgba(20,14,9,0) 52%, rgba(20,14,9,0.72) 100%)' }}/>

        {/* top controls */}
        <div style={{ position: 'absolute', top: 56, left: 20, right: 20, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <h1 style={{ fontFamily: T.serif, fontSize: 24, fontWeight: 500, letterSpacing: -0.5, color: '#fff', margin: 0 }}>Discover</h1>
          <div style={{ display: 'flex', gap: 14 }}>{DIcon.settings('rgba(255,255,255,0.9)')}{DIcon.saved('rgba(255,255,255,0.9)')}</div>
        </div>

        {/* seg control floating on image */}
        <div style={{ position: 'absolute', top: 98, left: 20, right: 20 }}>
          <div style={{ display: 'inline-flex', background: 'rgba(255,255,255,0.16)', backdropFilter: 'blur(10px)', borderRadius: 999, padding: 3 }}>
            {['For you','Vesper','Friends'].map((t,i)=>(
              <span key={t} style={{ padding: '7px 15px', borderRadius: 999, fontSize: 12.5, fontWeight: i===0?600:500, color: i===0?T.ink:'rgba(255,255,255,0.85)', background: i===0?'rgba(255,255,255,0.92)':'transparent', letterSpacing: -0.1 }}>{t}</span>
            ))}
          </div>
        </div>

        {/* hero copy low */}
        <div style={{ position: 'absolute', left: 22, right: 22, bottom: 244 }}>
          <div style={{ marginBottom: 12 }}><LensChip lens="For the obsessed" onDark/></div>
          <h2 style={{ fontFamily: T.serif, fontSize: 38, fontWeight: 500, letterSpacing: -1, lineHeight: 1.02, color: '#fff', margin: 0 }}>
            Lisbon, after<br/><span style={{ fontStyle: 'italic' }}>the light goes amber.</span>
          </h2>
          <p style={{ fontFamily: T.serif, fontSize: 14.5, color: 'rgba(255,255,255,0.82)', lineHeight: 1.4, margin: '12px 0 0', maxWidth: 300, letterSpacing: -0.1 }}>
            The hour the whole city steps outside and the hills start to glow from within.
          </p>
          <div style={{ marginTop: 14, display: 'flex', alignItems: 'center', gap: 12 }}>
            <span style={{ padding: '10px 18px', background: '#fff', color: T.ink, borderRadius: 999, fontSize: 13.5, fontWeight: 600, letterSpacing: -0.1, display: 'inline-flex', alignItems: 'center', gap: 6 }}>
              Read this <span style={{ color: D.vesper }}>→</span>
            </span>
            <span style={{ display: 'inline-flex', alignItems: 'center', gap: 5, color: 'rgba(255,255,255,0.78)', fontSize: 12.5, fontWeight: 600 }}>
              <span style={{ fontSize: 14 }}>+</span> Vesper
            </span>
          </div>
        </div>

        {/* peeking next card — the "more" tease, on a dark sheet */}
        <div style={{ position: 'absolute', left: 0, right: 0, bottom: 96, padding: '0 16px' }}>
          <div style={{ fontSize: 9.5, letterSpacing: 2, color: 'rgba(255,255,255,0.6)', fontWeight: 700, marginBottom: 10, paddingLeft: 6 }}>NEXT, IF THIS MOVES YOU</div>
          <div style={{ display: 'flex', gap: 12 }}>
            {[{v:'coast',t:'Where to swim within an hour'},{v:'alley',t:'The street that resists you'}].map((c,i)=>(
              <div key={i} style={{ flex: 1, borderRadius: 14, overflow: 'hidden', position: 'relative', height: 132 }}>
                <Plate variant={c.v} style={{ position: 'absolute', inset: 0 }} dim={0.34}/>
                <div style={{ position: 'absolute', left: 11, right: 11, bottom: 11 }}>
                  <div style={{ fontFamily: T.serif, fontSize: 14, fontWeight: 500, color: '#fff', letterSpacing: -0.2, lineHeight: 1.15 }}>{c.t}</div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
      <TabBar active="discover"/>
    </Phone>
  );
}

function D3Dossier() {
  return (
    <Phone bg={T.ink}>
      <div style={{ position: 'absolute', inset: 0, overflow: 'hidden', background: T.bg }}>
        {/* Tall immersive hero */}
        <Plate variant="hills" style={{ height: 408 }} dim={0.22}/>
        <div style={{ position: 'absolute', top: 0, left: 0, right: 0, height: 408, background: 'linear-gradient(to bottom, rgba(20,14,9,0.4) 0%, rgba(20,14,9,0) 30%, rgba(20,14,9,0) 50%, rgba(20,14,9,0.78) 100%)' }}/>
        <div style={{ position: 'absolute', top: 56, left: 18, right: 18, display: 'flex', justifyContent: 'space-between' }}>
          <div style={{ width: 38, height: 38, borderRadius: 999, background: 'rgba(255,255,255,0.2)', backdropFilter: 'blur(8px)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>{DIcon.back('#fff')}</div>
          <div style={{ width: 38, height: 38, borderRadius: 999, background: 'rgba(255,255,255,0.2)', backdropFilter: 'blur(8px)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>{DIcon.save('#fff')}</div>
        </div>
        <div style={{ position: 'absolute', top: 300, left: 22, right: 22 }}>
          <div style={{ marginBottom: 10 }}><LensChip lens="Ritual" onDark/></div>
          <h1 style={{ fontFamily: T.serif, fontSize: 30, fontWeight: 500, letterSpacing: -0.7, lineHeight: 1.05, color: '#fff', margin: 0 }}>
            Lisbon, after the light goes amber
          </h1>
        </div>

        {/* read body on parchment */}
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

window.D3Home = D3Home;
window.D3Dossier = D3Dossier;
