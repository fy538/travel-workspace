// ═══════════════════════════════════════════════════════════════
// SINGLE-TRIP HOME · composition variations. All keep three movements
// + breath; they differ in how cover/masthead relate to the body.
//   A · Overlap card — facet hero lifts up onto the cover
//   B · Editorial plate — photo as a framed plate, title on paper below
//   C · Full-bleed dossier — tall immersive cover, body on a raised sheet
// All shown needs-you. Reuses DR + StyleRiso + Filmstrip/Ppl/CASTD +
// CIcon/CICO + FacetsHero + QuietSlice + HomeFloor.
// ═══════════════════════════════════════════════════════════════

const vsk = (s = 13, c = DR.gold) => <svg width={s} height={s} viewBox="0 0 24 24" fill={c}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>;
function VShell({ children, bg = DR.paper }) {
  return <div style={{ width: 393, background: bg, borderRadius: 30, overflow: 'hidden', border: `0.5px solid ${DR.hair}`, boxShadow: '0 30px 60px -30px rgba(0,0,0,0.3)', position: 'relative', paddingBottom: 20 }}><div style={{ height: 40 }}/>{children}</div>;
}
function TopIcons() {
  return <div style={{ position: 'absolute', top: 46, left: 16, right: 16, display: 'flex', alignItems: 'center', justifyContent: 'space-between', zIndex: 4 }}>
    <CIcon>{CICO.back}</CIcon><div style={{ display: 'flex', gap: 8 }}><CIcon dot>{CICO.chat}</CIcon><CIcon dot>{CICO.bell}</CIcon><CIcon>{CICO.info}</CIcon></div>
  </div>;
}
function VStandfirst() {
  return <div style={{ display: 'flex', gap: 10 }}>
    {vsk(13)}
    <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 16, color: DR.ink, margin: 0, lineHeight: 1.4, letterSpacing: -0.15 }}>Alfama rewards the slow walker — I’ve kept the quiet corners for your mornings.</p>
  </div>;
}

// ─── A · OVERLAP CARD — the one-thing hero lifts onto the cover ───
function HomeVarA() {
  return (
    <VShell>
      <div style={{ position: 'relative', height: 250, marginTop: -40 }}>
        <div style={{ position: 'absolute', inset: 0 }}><StyleRiso w={393} h={250}/></div>
        <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.44) 0%, rgba(20,14,9,0) 30%, rgba(20,14,9,0.5) 100%)' }}/>
        <TopIcons/>
        <div style={{ position: 'absolute', top: 92, left: 18 }}><Filmstrip truth={1} onDark/></div>
        <div style={{ position: 'absolute', left: 20, right: 20, bottom: 40 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 7 }}><span style={{ padding: '3px 9px', borderRadius: 999, background: 'rgba(255,255,255,0.2)', backdropFilter: 'blur(6px)', fontSize: 9, letterSpacing: 1.4, fontWeight: 700, color: '#fff' }}>IN 23 DAYS</span><Ppl who={CASTD} size={22} onDark/></div>
          <h1 style={{ fontFamily: DR.serif, fontSize: 38, fontWeight: 500, letterSpacing: -1.1, lineHeight: 0.96, color: '#fff', margin: 0 }}>Lisbon, <span style={{ fontStyle: 'italic' }}>slowly</span></h1>
        </div>
      </div>
      {/* hero lifts up onto the cover via negative margin */}
      <div style={{ marginTop: -22, padding: '0 16px', position: 'relative', zIndex: 3 }}><FacetsHero bare/></div>
      <div style={{ padding: '16px 22px 0' }}><VStandfirst/></div>
      <div style={{ height: 24 }}/><QuietSlice/><div style={{ height: 18 }}/><HomeFloor/>
    </VShell>
  );
}

// ─── B · EDITORIAL PLATE — photo framed as a plate, title on paper ───
function HomeVarB() {
  return (
    <VShell>
      <TopIcons/>
      <div style={{ padding: '52px 18px 0' }}>
        {/* framed photo plate */}
        <div style={{ height: 188, borderRadius: 16, overflow: 'hidden', position: 'relative' }}>
          <StyleRiso w={357} h={188}/>
          <div style={{ position: 'absolute', top: 11, left: 12 }}><Filmstrip truth={1} onDark/></div>
          <div style={{ position: 'absolute', right: 12, bottom: 11 }}><Ppl who={CASTD} size={20} onDark/></div>
        </div>
        {/* title on paper, below the plate */}
        <div style={{ marginTop: 14 }}>
          <div style={{ fontFamily: DR.mono, fontSize: 9, color: DR.mute, letterSpacing: 1.4, fontWeight: 600 }}>MAY 18–24 · IN 23 DAYS</div>
          <h1 style={{ fontFamily: DR.serif, fontSize: 36, fontWeight: 500, letterSpacing: -1, lineHeight: 0.98, color: DR.ink, margin: '5px 0 0' }}>Lisbon, <span style={{ fontStyle: 'italic' }}>slowly</span></h1>
          <div style={{ marginTop: 11 }}><VStandfirst/></div>
        </div>
      </div>
      <div style={{ height: 24 }}/>
      <div style={{ padding: '0 18px' }}><FacetsHero bare/></div>
      <div style={{ height: 28 }}/><QuietSlice/><div style={{ height: 18 }}/><HomeFloor/>
    </VShell>
  );
}

// ─── C · FULL-BLEED DOSSIER — tall immersive cover, body on a raised sheet ───
function HomeVarC() {
  return (
    <VShell bg={DR.ink}>
      <div style={{ position: 'absolute', inset: 0, height: 360 }}><StyleRiso w={393} h={360}/><div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.4) 0%, rgba(20,14,9,0) 34%, rgba(20,14,9,0.55) 100%)' }}/></div>
      <TopIcons/>
      <div style={{ position: 'absolute', top: 92, left: 18, zIndex: 2 }}><Filmstrip truth={1} onDark/></div>
      <div style={{ position: 'relative', zIndex: 2, paddingTop: 220, paddingLeft: 22, paddingRight: 22 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 8 }}><span style={{ padding: '3px 9px', borderRadius: 999, background: 'rgba(255,255,255,0.2)', backdropFilter: 'blur(6px)', fontSize: 9, letterSpacing: 1.4, fontWeight: 700, color: '#fff' }}>IN 23 DAYS</span><Ppl who={CASTD} size={22} onDark/></div>
        <h1 style={{ fontFamily: DR.serif, fontSize: 42, fontWeight: 500, letterSpacing: -1.3, lineHeight: 0.94, color: '#fff', margin: 0 }}>Lisbon,<br/><span style={{ fontStyle: 'italic' }}>slowly</span></h1>
      </div>
      {/* raised paper sheet over the bottom of the cover */}
      <div style={{ position: 'relative', zIndex: 2, marginTop: 26, background: DR.paper, borderRadius: '24px 24px 30px 30px', paddingTop: 18, paddingBottom: 4 }}>
        <div style={{ padding: '0 22px' }}><VStandfirst/></div>
        <div style={{ height: 22 }}/>
        <div style={{ padding: '0 18px' }}><FacetsHero bare/></div>
        <div style={{ height: 28 }}/><QuietSlice/><div style={{ height: 18 }}/><HomeFloor/>
      </div>
    </VShell>
  );
}

Object.assign(window, { HomeVarA, HomeVarB, HomeVarC });
