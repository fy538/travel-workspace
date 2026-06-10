// ═══════════════════════════════════════════════════════════════
// VESPER · ONBOARDING v2 — the productive wait → reveal → land.
// The scan runs in the BACKGROUND from permission on; it never has
// its own screen. The fork opens with the first finding; the wait
// is two light taste beats (dreaming) or a quick capture (trip in
// mind). The reveal/save has two states — done & still-cooking
// (never blocks auth) — then you land in Atlas or Trips while the
// diary finishes developing. Reuses onboarding-kit + v2-core +
// gouache (GouacheScene) + v3-shared (PostcardScene).
// ═══════════════════════════════════════════════════════════════

const ob3 = { hair: `0.5px solid ${T.hairline}`, hairT: `0.5px solid ${T.hairThin}` };

// the background work, made concrete: 2 found + 1 still developing
function FoundRow() {
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 11, padding: '12px 14px', background: 'rgba(176,133,58,0.09)', borderRadius: 14, border: `0.5px solid rgba(176,133,58,0.22)` }}>
      <div style={{ display: 'flex', gap: 5 }}>
        {['lisbon', 'tokyo'].map((s) => <div key={s} style={{ width: 28, height: 22, borderRadius: 5, overflow: 'hidden', flexShrink: 0, border: ob3.hair }}><PostcardScene scene={s}/></div>)}
        <div style={{ width: 28, height: 22, borderRadius: 5, border: `1px dashed ${T.goldSoft}`, flexShrink: 0, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <span style={{ width: 5, height: 5, borderRadius: 5, background: T.goldSoft }}/>
        </div>
      </div>
      <span style={{ flex: 1, fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.goldDeep, lineHeight: 1.3 }}>Lisbon, twice. Tokyo one winter — still developing the rest…</span>
    </div>
  );
}

// a faint persistent line for the deeper wait screens
function DevStrip() {
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 9, padding: '8px 13px', background: 'rgba(176,133,58,0.08)', borderRadius: 999, border: `0.5px solid rgba(176,133,58,0.20)` }}>
      <VesperMark s={11} c={T.goldDeep}/>
      <span style={{ flex: 1, fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.goldDeep }}>Still developing your diary — 7 trips so far…</span>
    </div>
  );
}

function V2Prompt({ kicker = 'VESPER', heading, sub }) {
  return (
    <div>
      <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 12 }}>
        <VesperMark s={13}/>
        <span style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 2.4, color: T.goldDeep, fontWeight: 600 }}>{kicker}</span>
      </div>
      <h1 style={{ fontFamily: T.serif, fontSize: 27, fontWeight: 500, color: T.ink, letterSpacing: -0.5, lineHeight: 1.18, margin: 0 }}>{heading}</h1>
      {sub && <p style={{ fontFamily: T.serif, fontSize: 15, color: T.soft, lineHeight: 1.5, margin: '11px 0 0' }}>{sub}</p>}
    </div>
  );
}

// ── 4 · THE FORK — opens with the first finding (develop folded in) ─
const pinG = <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={OB.blue} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M12 21s7-6.4 7-11a7 7 0 1 0-14 0c0 4.6 7 11 7 11Z"/><circle cx="12" cy="10" r="2.3"/></svg>;
const dreamG = <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={T.mute} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M12 3a6 6 0 0 0 0 12 6 6 0 0 1 0 6 9 9 0 0 0 0-18Z"/></svg>;
function ForkRow({ n, title, sub }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 16, padding: '20px 0', borderBottom: ob3.hair }}>
      <span style={{ fontFamily: T.mono, fontSize: 11, letterSpacing: 1, color: T.goldDeep, fontWeight: 600, flexShrink: 0 }}>{n}</span>
      <div style={{ flex: 1, minWidth: 0 }}>
        <div style={{ fontFamily: T.serif, fontSize: 22, fontWeight: 500, color: T.ink, letterSpacing: -0.4, lineHeight: 1.04 }}>{title}</div>
        <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.mute, marginTop: 4 }}>{sub}</div>
      </div>
      <span style={{ color: T.goldDeep, fontSize: 17, flexShrink: 0 }}>→</span>
    </div>
  );
}
function V2Fork() {
  return (
    <PFrame>
      <div style={{ height: '100%', display: 'flex', flexDirection: 'column', padding: '0 26px' }}>
        <div style={{ flex: 1 }}/>
        {/* the question — Vesper's voice, the hero (generic, no scan claim) */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 16 }}>
          <VesperMark s={14}/>
          <span style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 2.4, color: T.goldDeep, fontWeight: 600 }}>VESPER</span>
        </div>
        <h1 style={{ fontFamily: T.serif, fontSize: 36, fontWeight: 500, color: T.ink, letterSpacing: -0.9, lineHeight: 1.02, margin: 0 }}>
          So — <span style={{ fontStyle: 'italic' }}>where are we going?</span>
        </h1>
        <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 16, color: T.mute, lineHeight: 1.5, margin: '14px 0 0', maxWidth: 300 }}>
          Tell me a place, or let me show you one. Either way, this is where it starts.
        </p>
        {/* the numbered split — no boxes */}
        <div style={{ marginTop: 26, borderTop: ob3.hair }}>
          <ForkRow n="01" title="A trip in mind" sub="a place, rough dates, or both"/>
          <ForkRow n="02" title="Still dreaming" sub="show me something worth wanting"/>
        </div>
        <div style={{ flex: 1 }}/>
      </div>
    </PFrame>
  );
}

// ── 5a · TASTE — kind of trip, now with gouache thumbs ──────────
function TasteCard({ scene, tag, title, eg, places }) {
  return (
    <div style={{ display: 'flex', alignItems: 'stretch', gap: 0, background: T.cardWarm, border: ob3.hair, borderRadius: 16, overflow: 'hidden' }}>
      <div style={{ width: 86, flexShrink: 0, position: 'relative' }}><GouacheScene scene={scene} w={140} h={200}/></div>
      <div style={{ flex: 1, minWidth: 0, padding: '13px 16px', display: 'flex', alignItems: 'center', gap: 10 }}>
        <div style={{ flex: 1, minWidth: 0 }}>
          <div style={{ fontFamily: T.mono, fontSize: 8, letterSpacing: 1.6, color: T.goldDeep, fontWeight: 700 }}>{tag}</div>
          <div style={{ fontFamily: T.serif, fontSize: 18, fontWeight: 500, color: T.ink, letterSpacing: -0.3, lineHeight: 1.08, marginTop: 4 }}>{title}</div>
          <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.mute, marginTop: 4, lineHeight: 1.35 }}>{eg}</div>
          {places && <div style={{ fontFamily: T.mono, fontSize: 7.5, letterSpacing: 0.8, color: T.muteSoft, fontWeight: 600, marginTop: 7 }}>{places}</div>}
        </div>
        <span style={{ color: T.goldDeep, fontSize: 15 }}>→</span>
      </div>
    </div>
  );
}
// progress across the two taste beats
function TasteDots({ n, total = 2 }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 6, paddingTop: 4 }}>
      {Array.from({ length: total }).map((_, i) => <span key={i} style={{ width: i === n ? 16 : 5, height: 5, borderRadius: 4, background: i === n ? T.goldDeep : (i < n ? T.goldSoft : T.faint) }}/>)}
    </div>
  );
}

// 1 OF 2 · INTEREST — what you travel FOR (the reward domain)
function V2TasteInterest() {
  return (
    <PFrame>
      <div style={{ height: '100%', display: 'flex', flexDirection: 'column', padding: '26px 22px 0' }}>
        <div style={{ display: 'flex', marginBottom: 22 }}>
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M15 5l-7 7 7 7"/></svg>
        </div>
        <V2Prompt kicker="VESPER · 1 OF 2" heading={<>What makes a trip <span style={{ fontStyle: 'italic' }}>worth it?</span></>} sub="Tap what pulls hardest."/>
        <div style={{ flex: 1, display: 'grid', gridTemplateColumns: '1fr 1fr', gridTemplateRows: '1fr 1fr', gap: 12, marginTop: 18, minHeight: 0 }}>
          <ChoiceTile scene="food" label="Food & drink" sub="markets, counters, long tables" compact/>
          <ChoiceTile scene="city" label="Art & history" sub="museums, old streets" compact/>
          <ChoiceTile scene="forest" label="Nature & air" sub="trails, water, big quiet" compact/>
          <ChoiceTile scene="coast" label="Sea & sun" sub="swims, slow heat, salt" compact/>
        </div>
        <div style={{ padding: '20px 0 30px' }}><TasteDots n={0}/></div>
      </div>
    </PFrame>
  );
}

// ── 5b · TASTE — this-or-that, the low-friction visual beat ─────
function ChoiceTile({ scene, label, sub, compact }) {
  return (
    <div style={{ flex: 1, minHeight: 0, position: 'relative', borderRadius: 18, overflow: 'hidden', border: ob3.hair }}>
      <GouacheScene scene={scene} w={200} h={400}/>
      <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to top, rgba(20,14,9,0.62), rgba(20,14,9,0.04) 58%)' }}/>
      <div style={{ position: 'absolute', left: compact ? 13 : 15, right: 12, bottom: compact ? 12 : 15 }}>
        <div style={{ fontFamily: T.serif, fontSize: compact ? 18 : 22, fontWeight: 500, color: '#F7F2E7', letterSpacing: -0.4, lineHeight: 1.04 }}>{label}</div>
        <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: compact ? 11.5 : 12.5, color: 'rgba(247,242,231,0.82)', marginTop: 3 }}>{sub}</div>
      </div>
    </div>
  );
}
// 2 OF 2 · PACE — how much you pack in (energy), stacked this-or-that
function V2TastePace() {
  return (
    <PFrame>
      <div style={{ height: '100%', display: 'flex', flexDirection: 'column', padding: '26px 22px 0' }}>
        <div style={{ display: 'flex', marginBottom: 22 }}>
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M15 5l-7 7 7 7"/></svg>
        </div>
        <V2Prompt kicker="VESPER · 2 OF 2" heading={<>And your <span style={{ fontStyle: 'italic' }}>pace?</span></>} sub="Same place — two ways to spend the day."/>
        <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: 12, marginTop: 18, minHeight: 0 }}>
          <ChoiceTile scene="island" label="Slow & deep" sub="one place, one long lunch, nowhere to be"/>
          <ChoiceTile scene="harbor" label="Full & restless" sub="six neighbourhoods before dusk"/>
          <ChoiceTile scene="city" label="Depends on the day" sub="some slow, some full — let it breathe"/>
        </div>
        <div style={{ padding: '20px 0 30px' }}><TasteDots n={1}/></div>
      </div>
    </PFrame>
  );
}

// ── 5c · TRIP IN MIND — the trip as a sentence you complete ─────
const Tok = ({ children, state = 'done' }) => {
  if (state === 'empty') return <span style={{ fontStyle: 'italic', color: T.muteSoft, borderBottom: `1.5px dashed ${T.faint}`, paddingBottom: 1 }}>{children}</span>;
  if (state === 'active') return <span style={{ fontStyle: 'italic', color: T.goldDeep, background: 'rgba(176,133,58,0.15)', padding: '1px 5px', borderRadius: 4, borderBottom: `1.5px solid ${T.gold}` }}>{children}</span>;
  return <span style={{ fontStyle: 'italic', color: T.goldDeep, borderBottom: `1.5px solid ${T.gold}`, paddingBottom: 1 }}>{children}</span>;
};
const TokOpt = ({ children, on }) => <span style={{ fontFamily: T.serif, fontSize: 17, letterSpacing: -0.2, color: on ? T.goldDeep : T.soft, fontStyle: on ? 'normal' : 'normal', borderBottom: on ? `1.5px solid ${T.gold}` : '1.5px solid transparent', paddingBottom: 2 }}>{children}</span>;
function CapChip({ label, on }) {
  return (
    <span style={{ padding: '9px 14px', borderRadius: 999, fontFamily: T.serif, fontSize: 14, letterSpacing: -0.1, background: on ? T.cardWarm : 'transparent', border: `0.8px solid ${on ? T.gold : T.hairline}`, color: on ? T.goldDeep : T.soft }}>{label}</span>
  );
}
function CapField({ kicker, children }) {
  return (
    <div>
      <div style={{ fontFamily: T.mono, fontSize: 8.5, letterSpacing: 1.8, color: T.mute, fontWeight: 600, marginBottom: 9 }}>{kicker}</div>
      {children}
    </div>
  );
}
// primary floating-glass CTA (blue), used by the trip capture
const GlassGo = ({ children }) => <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 8, padding: '15px 0', borderRadius: 15, background: 'rgba(61,80,102,0.66)', backdropFilter: 'blur(18px)', WebkitBackdropFilter: 'blur(18px)', border: '0.5px solid rgba(255,255,255,0.34)', boxShadow: '0 14px 30px -12px rgba(42,56,75,0.6), inset 0 1px 0 rgba(255,255,255,0.4)', color: '#fff', fontFamily: T.sans, fontSize: 15, fontWeight: 600 }}>{children}</div>;
// quiet ghost CTA — the same button BEFORE a choice is made (“Skip”);
// it fills into GlassGo (“Next”) the moment the step's token is set.
const GlassGhost = ({ children }) => <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 8, padding: '15px 0', borderRadius: 15, background: 'rgba(255,255,255,0.4)', backdropFilter: 'blur(18px)', WebkitBackdropFilter: 'blur(18px)', border: `0.5px solid ${T.hairline}`, color: T.mute, fontFamily: T.sans, fontSize: 15, fontWeight: 600 }}>{children}</div>;
// ── 5c · TRIP IN MIND — ONE sentence filled across three states:
// where → when → who. Each fills a token, swaps the inline picker,
// and the CTA stays "Next" until the sentence is whole ("Start the trip").
function CapFrame({ sentence, caption, kicker, picker, cta, skip }) {
  return (
    <PFrame>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, display: 'flex', flexDirection: 'column' }}>
        <AuthWash scene="city" h={140}/>
        {/* nav — back through the sentence (per-step skip lives on the primary button) */}
        <div style={{ position: 'absolute', top: 62, left: 20, right: 20, display: 'flex', alignItems: 'center', justifyContent: 'space-between', zIndex: 6 }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M15 5l-7 7 7 7"/></svg>
          </div>
        </div>
        <div style={{ position: 'relative', flex: 1, minHeight: 0, padding: '80px 28px 0', display: 'flex', flexDirection: 'column' }}>
          {/* Vesper's voice — anchored at a fixed top across 3a/3b/3c */}
          <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 16 }}>
            <VesperMark s={13}/>
            <span style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 2.4, color: T.goldDeep, fontWeight: 600 }}>VESPER · THE SHAPE</span>
          </div>
          {/* the trip as a sentence you complete — done / active / blank tokens */}
          <p style={{ fontFamily: T.serif, fontSize: 29, fontWeight: 500, color: T.ink, lineHeight: 1.44, letterSpacing: -0.4, margin: 0 }}>{sentence}</p>
          <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 14, color: T.mute, lineHeight: 1.5, margin: '16px 0 0' }}>{caption}</p>
          {/* the open token: a borderless inline picker (no chips-in-boxes) */}
          <div style={{ marginTop: 28, paddingTop: 18, borderTop: ob3.hair }}>
            <div style={{ fontFamily: T.mono, fontSize: 8.5, letterSpacing: 1.8, color: T.mute, fontWeight: 600, marginBottom: 12 }}>{kicker}</div>
            {picker}
          </div>
        </div>
        <div style={{ position: 'relative', padding: '0 28px 28px' }}>
          {skip
            ? <GlassGhost>{cta} <span style={{ opacity: 0.7 }}>→</span></GlassGhost>
            : <GlassGo>{cta} <span style={{ opacity: 0.8 }}>→</span></GlassGo>}
          {/* the button is dynamic: Skip until the step's token is set, then Next */}
          {skip && <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.muteSoft, textAlign: 'center', margin: '9px 0 0' }}>Pick one above and this becomes <span style={{ color: T.goldDeep }}>Next</span>.</p>}
          {/* secondary — skip the form, just talk */}
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 8, marginTop: 14 }}>
            <VesperMark s={13} c={T.goldDeep}/>
            <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 14, color: T.goldDeep }}>Rather just tell me? Talk it through →</span>
          </div>
        </div>
      </div>
    </PFrame>
  );
}
// a borderless place row for the WHERE search results
function PlaceRow({ name, note, first }) {
  return (
    <div style={{ display: 'flex', alignItems: 'baseline', gap: 10, padding: '11px 0', borderTop: first ? 'none' : ob3.hair }}>
      <span style={{ fontFamily: T.serif, fontSize: 18, fontWeight: 500, color: T.ink, letterSpacing: -0.3 }}>{name}</span>
      <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.mute, flex: 1, minWidth: 0, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>{note}</span>
      <span style={{ fontFamily: T.mono, fontSize: 8, letterSpacing: 1.4, color: T.goldDeep, fontWeight: 600 }}>PICK →</span>
    </div>
  );
}
// 3a · WHERE — place as a type-ahead search + the cities you keep circling
function V2TripWhere() {
  return <CapFrame
    sentence={<>A trip to <Tok state="active">where?</Tok>, for <Tok state="empty">how long</Tok>, with <Tok state="empty">whom</Tok></>}
    caption={<>Start anywhere — name the place, or skip and I’ll ask later. <span style={{ color: T.muteSoft }}>Nothing here is required.</span></>}
    kicker="WHERE — SEARCH OR TAP"
    cta="Skip for now"
    skip
    picker={<div>
      <div style={{ display: 'flex', alignItems: 'center', gap: 9, padding: '11px 14px', background: T.cardWarm, borderRadius: 999, border: `0.5px solid ${T.gold}` }}>
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke={T.mute} strokeWidth="1.8" strokeLinecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>
        <span style={{ width: 1.5, height: 16, background: T.gold, flexShrink: 0 }}/>
        <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 15, color: T.muteSoft, whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>Search a city or country…</span>
      </div>
      <div style={{ marginTop: 8 }}>
        <PlaceRow first name="Lisbon" note="slow mornings, miradouros, tile light"/>
        <PlaceRow name="Mexico City" note="markets, mezcal, your kind of chaos"/>
        <PlaceRow name="Lofoten" note="the quiet you keep circling"/>
      </div>
    </div>}
  />;
}
// 3b · WHEN — place locked, duration the open token
function V2TripWhen() {
  return <CapFrame
    sentence={<>A trip to <Tok>Lisbon</Tok>, for <Tok state="active">about a week</Tok>, with <Tok state="empty">whom?</Tok></>}
    caption={<>Lisbon’s in. How long are you going? <span style={{ color: T.muteSoft }}>— pick below, then I’ll ask who.</span></>}
    kicker="WHEN — TAP ONE"
    cta="Next"
    picker={<div style={{ display: 'flex', flexWrap: 'wrap', gap: '12px 22px' }}>
      <TokOpt>A weekend</TokOpt>
      <TokOpt on>About a week</TokOpt>
      <TokOpt>Two weeks +</TokOpt>
      <TokOpt>Not sure yet</TokOpt>
    </div>}
  />;
}
// 3c · WHO — place + duration locked, companions the open token; the
// invite affordance appears under "a few of us" (seeds the group trip)
function V2TripWho() {
  const dash = <span style={{ width: 24, height: 24, borderRadius: 999, border: `1.4px dashed ${T.gold}`, display: 'inline-flex', alignItems: 'center', justifyContent: 'center', color: T.goldDeep, fontFamily: T.serif, fontSize: 13, marginLeft: -7, background: T.paper }}>+</span>;
  return <CapFrame
    sentence={<>A trip to <Tok>Lisbon</Tok>, for <Tok>about a week</Tok>, with <Tok state="active">a few of us</Tok></>}
    caption={<>A week in Lisbon. Who’s coming? <span style={{ color: T.muteSoft }}>— pick one; I can invite them now or later.</span></>}
    kicker="WHO — TAP ONE"
    cta="Start the trip"
    picker={<div>
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '12px 22px' }}>
        <TokOpt>Just me</TokOpt>
        <TokOpt>A partner</TokOpt>
        <TokOpt on>A few of us</TokOpt>
        <TokOpt>A group</TokOpt>
      </div>
      {/* invite affordance — only when a group is chosen; seeds the shared trip */}
      <div style={{ marginTop: 18, paddingTop: 14, borderTop: ob3.hair, display: 'flex', alignItems: 'center', gap: 11 }}>
        <div style={{ display: 'flex', paddingLeft: 7 }}>{dash}{dash}</div>
        <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.mute, flex: 1, lineHeight: 1.35 }}>Name them now, or invite once the trip’s up.</span>
        <span style={{ fontFamily: T.mono, fontSize: 8.5, letterSpacing: 1.4, color: T.goldDeep, fontWeight: 600 }}>+ ADD</span>
      </div>
    </div>}
  />;
}

// ── THE DIARY DEVELOPS IN ATLAS — not a takeover. The real Atlas
// page (profile · search · ＋ present throughout) shows the diary
// developing; when done, a single "keep it" to save. done=false →
// developing · done=true → developed + the keep-it bar.
function AtlasDeveloping({ done = false, forming = false }) {
  const kept = done || forming;
  const ic = (d) => <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={T.mute} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">{d}</svg>;
  return (
    <PFrame>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, display: 'flex', flexDirection: 'column', overflow: 'hidden' }}>
        {/* Atlas chrome — present even while it loads */}
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '12px 20px 0' }}>
          <div style={{ width: 30, height: 30, borderRadius: 999, background: T.goldDeep, color: T.cardWarm, fontFamily: T.serif, fontWeight: 500, fontSize: 13, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>T</div>
          <div style={{ display: 'flex', gap: 18 }}>
            {ic(<><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></>)}
            {ic(<><path d="M12 5v14M5 12h14"/></>)}
          </div>
        </div>
        {/* Vesper, narrating in-place */}
        <div style={{ padding: '18px 22px 0' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 11 }}>
            <VesperMark s={13} c={kept ? T.goldDeep : T.goldSoft}/>
            <span style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 2.4, color: T.goldDeep, fontWeight: 600 }}>{forming ? 'VESPER · A FRESH PAGE' : done ? 'VESPER · YOUR DIARY' : 'VESPER · READING YOUR PHOTOS'}</span>
          </div>
          <p style={{ fontFamily: T.serif, fontSize: 17, color: T.ink, lineHeight: 1.45, letterSpacing: -0.15, margin: 0 }}>
            {forming
              ? <>Not much in your photos yet — <span style={{ color: T.mute, fontStyle: 'italic' }}>so we start with a blank page, and what you’ve told me.</span></>
              : done
                ? <>Eleven trips, five years — <span style={{ color: T.mute }}>here they are.</span></>
                : <>There you are — Lisbon, twice. Tokyo one winter. <span style={{ color: T.mute, fontStyle: 'italic' }}>Developing the rest…</span></>}
          </p>
          {forming && (
            <div style={{ marginTop: 14, display: 'flex', flexWrap: 'wrap', gap: 8 }}>
              {['Slow & deep', 'Food-led', 'By the water'].map((c) => (
                <span key={c} style={{ padding: '7px 13px', borderRadius: 999, background: 'rgba(176,133,58,0.1)', border: `0.5px solid ${T.goldSoft}`, fontFamily: T.serif, fontSize: 13.5, color: T.goldDeep }}>{c}</span>
              ))}
            </div>
          )}
        </div>
        {/* the diary itself, filling in */}
        <div style={{ margin: '20px 22px 0', flex: 1, minHeight: 0, overflow: 'hidden', position: 'relative', paddingTop: 16, borderTop: ob3.hair }}>
          <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginBottom: 16 }}>
            <span style={{ fontFamily: T.mono, fontSize: 8.5, letterSpacing: 1.8, color: T.goldDeep, fontWeight: 600 }}>{forming ? 'YOUR DIARY · BLANK' : done ? 'YOUR DIARY' : 'YOUR DIARY · DEVELOPING'}</span>
            {!done && !forming && <span style={{ fontFamily: T.mono, fontSize: 8.5, letterSpacing: 1, color: T.muteSoft, fontWeight: 600 }}>7 OF ~11</span>}
          </div>
          <DiaryTimeline mode={forming ? 'empty' : done ? 'full' : 'developing'} ringBg={T.bg}/>
          {forming && (
            <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginTop: 12 }}>
              <VesperMark s={12}/>
              <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.mute }}>It fills as you travel. Lisbon could be the first page.</span>
            </div>
          )}
        </div>
        {/* developed → keep-it bar (the only action); developing → quiet status */}
        {kept ? (
          <div style={{ margin: '14px 16px 0', padding: '13px 14px', background: 'rgba(176,133,58,0.12)', borderRadius: 14, border: `0.8px solid ${T.goldSoft}`, display: 'flex', alignItems: 'center', gap: 11 }}>
            <VesperMark s={15} c={T.goldDeep}/>
            <span style={{ flex: 1, fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.goldDeep, lineHeight: 1.3 }}>{forming ? 'Your diary starts here — sign in to keep it.' : 'Your diary’s ready — sign in to keep it for good.'}</span>
            <span style={{ padding: '8px 16px', background: T.goldDeep, color: T.cardWarm, borderRadius: 999, fontFamily: T.sans, fontSize: 13, fontWeight: 600 }}>Keep it</span>
          </div>
        ) : (
          <div style={{ margin: '14px 22px 0', display: 'flex', alignItems: 'center', gap: 9 }}>
            <span style={{ width: 6, height: 6, borderRadius: 999, background: T.goldSoft }}/>
            <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.mute }}>Still reading your library — look around while I work.</span>
          </div>
        )}
        <div style={{ height: 74 }}/>
      </div>
      <TabBar active="atlas"/>
    </PFrame>
  );
}

// ── 7 · SIGN IN — WHILE THE DIARY CONSTRUCTS. Auth lands right after
// permission; the diary develops in the background as you sign in, so
// it's ready the moment you're in. forming=true → thin-library variant.
function V2Save({ forming = false }) {
  return (
    <PFrame>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, display: 'flex', flexDirection: 'column', overflow: 'hidden' }}>
        {/* Vesper, working in real time */}
        <div style={{ padding: '44px 26px 0' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 12 }}>
            <VesperMark s={13} c={T.goldSoft}/>
            <span style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 2.4, color: T.goldDeep, fontWeight: 600 }}>{forming ? 'VESPER · STARTING YOUR DIARY' : 'VESPER · BUILDING YOUR DIARY'}</span>
            <span style={{ width: 5, height: 5, borderRadius: 999, background: T.goldSoft, marginLeft: 2, animation: 'none' }}/>
          </div>
          <h1 style={{ fontFamily: T.serif, fontSize: 26, fontWeight: 500, color: T.ink, letterSpacing: -0.5, lineHeight: 1.18, margin: 0 }}>
            {forming ? <>Sign in, and it starts <span style={{ fontStyle: 'italic' }}>filling.</span></> : <>Sign in while I <span style={{ fontStyle: 'italic' }}>finish.</span></>}
          </h1>
          <p style={{ fontFamily: T.serif, fontSize: 14.5, color: T.soft, lineHeight: 1.48, margin: '9px 0 0' }}>
            {forming
              ? 'Not much in your photos yet — so your diary starts as a fresh page, ready for Lisbon.'
              : 'I’m reading your photos now. Sign in to keep it — it’ll be ready the moment you’re in.'}
          </p>
        </div>
        {/* the diary constructing — live, behind the ask */}
        <div style={{ margin: '20px 24px 0', flex: 1, minHeight: 0, overflow: 'hidden', position: 'relative', paddingTop: 15, borderTop: ob3.hair }}>
          <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginBottom: 15 }}>
            <span style={{ fontFamily: T.mono, fontSize: 8.5, letterSpacing: 1.8, color: T.goldDeep, fontWeight: 600 }}>{forming ? 'YOUR DIARY · BLANK PAGE' : 'YOUR DIARY · DEVELOPING'}</span>
            {!forming && <span style={{ fontFamily: T.mono, fontSize: 8.5, letterSpacing: 1, color: T.muteSoft, fontWeight: 600 }}>7 OF ~11</span>}
          </div>
          <DiaryTimeline mode={forming ? 'empty' : 'developing'} ringBg={T.bg}/>
          {forming && (
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8, marginTop: 14 }}>
              {['Slow & deep', 'Food-led', 'By the water'].map((c) => (
                <span key={c} style={{ padding: '7px 13px', borderRadius: 999, background: 'rgba(176,133,58,0.1)', border: `0.5px solid ${T.goldSoft}`, fontFamily: T.serif, fontSize: 13, color: T.goldDeep }}>{c}</span>
              ))}
            </div>
          )}
        </div>
        {/* the ask — auth, at peak intent, work already underway */}
        <div style={{ padding: '16px 26px 0' }}>
          <GlassAuthStack/>
          <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.mute, textAlign: 'center', margin: '13px 12px 0', lineHeight: 1.4 }}>
            {forming ? 'It lives on your phone until you say otherwise.' : 'Your diary lives on your phone until you say otherwise.'}
          </p>
        </div>
        <div style={{ height: 20 }}/>
      </div>
    </PFrame>
  );
}

// ── 7a · LAND · ATLAS (dreaming branch) — the real Atlas home ───
function V2Land({ noDiary = false }) {
  const ic = (d) => <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={T.mute} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">{d}</svg>;
  return (
    <PFrame>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, display: 'flex', flexDirection: 'column', overflow: 'hidden' }}>
        {/* utility header — admin door + search / ＋ */}
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '12px 20px 0' }}>
          <div style={{ width: 30, height: 30, borderRadius: 999, background: T.goldDeep, color: T.cardWarm, fontFamily: T.serif, fontWeight: 500, fontSize: 13, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>T</div>
          <div style={{ display: 'flex', gap: 18 }}>
            {ic(<><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></>)}
            {ic(<><path d="M12 5v14M5 12h14"/></>)}
          </div>
        </div>
        {/* the letter hero — Vesper speaks, identity as content */}
        <div style={{ padding: '30px 22px 0' }}>
          <div style={{ marginBottom: 12 }}><span style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 2.2, color: T.goldDeep, fontWeight: 600 }}>VESPER · JUNE</span></div>
          <p style={{ fontFamily: T.serif, fontSize: 23.5, fontWeight: 500, color: T.ink, lineHeight: 1.38, letterSpacing: -0.4, margin: 0 }}>
            {noDiary
              ? <>You’re in. <span style={{ color: T.mute }}>No diary yet — but tell me where you’re headed and I’ll start keeping it.</span></>
              : <>Five years, eleven trips — and the sea keeps winning. <span style={{ color: T.mute }}>You travel slow, and you travel to eat.</span> I’ve kept them all here.</>}
          </p>
        </div>
        {/* the year ribbon */}
        <div style={{ marginTop: 26 }}>
          <YearRibbonH dots={noDiary ? [null, null, null, null, null, null, null, null, null, null, null, null] : ['past', null, 'past', null, null, 'now', null, 'past', null, 'past', null, null]} now={noDiary ? null : 5} leftLabel="YOUR YEARS" rightLabel={noDiary ? 'NONE YET' : '11 KEPT'}/>
        </div>
        {/* one quiet nudge — the full Atlas home lives in its own surface */}
        <div style={{ margin: '26px 20px 0', paddingTop: 15, borderTop: ob3.hair, display: 'flex', alignItems: 'center', gap: 10 }}>
          <VesperMark s={13}/>
          <span style={{ flex: 1, fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.inkSoft }}>The coast keeps pulling you — want somewhere new?</span>
          <span style={{ color: T.goldDeep }}>→</span>
        </div>
        <div style={{ flex: 1 }}/>
      </div>
      <TabBar active="atlas"/>
    </PFrame>
  );
}

// ── EVERY PATH — the full route map: entry doors, the cold-start
// spine with its branches & converges, plus invite and returning.
const PT = { gold: '#9A7636', goldd: '#7C5E27', blue: '#3D5066', red: '#A04030', green: '#3D6B50' };
function PNode({ k, sub, tone = 'gold', dashed }) {
  return (
    <div style={{ padding: '8px 12px', background: dashed ? 'transparent' : '#FBF7EC', borderRadius: 8, border: dashed ? `1px dashed ${PT[tone]}` : `0.5px solid ${T.hairline}`, borderLeft: dashed ? `1px dashed ${PT[tone]}` : `2.5px solid ${PT[tone]}`, display: 'inline-block', maxWidth: 250 }}>
      <div style={{ fontFamily: T.mono, fontSize: 8.5, letterSpacing: 1, color: PT[tone], fontWeight: 700 }}>{k}</div>
      {sub && <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 11.5, color: T.ink, marginTop: 2, lineHeight: 1.25 }}>{sub}</div>}
    </div>
  );
}
const PStep = ({ label }) => (
  <div style={{ display: 'flex', alignItems: 'center', gap: 7, padding: '2px 0 2px 16px' }}>
    <div style={{ width: 2, height: 14, background: T.faint }}/>
    {label && <span style={{ fontFamily: T.mono, fontSize: 7.5, letterSpacing: 0.8, color: T.mute, fontWeight: 600 }}>{label}</span>}
  </div>
);
function PLane({ title, tone = 'blue', children }) {
  return (
    <div style={{ flex: 1, minWidth: 0, paddingLeft: 13, borderLeft: `2px solid ${PT[tone]}` }}>
      <div style={{ fontFamily: T.mono, fontSize: 8, letterSpacing: 1.1, color: PT[tone], fontWeight: 700, marginBottom: 7 }}>{title}</div>
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start' }}>{children}</div>
    </div>
  );
}
const PCap = ({ children }) => <div style={{ fontFamily: T.mono, fontSize: 7.5, letterSpacing: 1.2, color: T.mute, fontWeight: 700, margin: '7px 0 7px 16px' }}>{children}</div>;
function PipelinePaths() {
  return (
    <div style={{ width: 1060, padding: '34px 36px', background: '#F1ECE2', borderRadius: 8, color: T.inkSoft }}>
      <div style={{ fontFamily: T.mono, fontSize: 9.5, letterSpacing: 2, color: PT.goldd, fontWeight: 700 }}>EVERY PATH</div>
      <div style={{ fontFamily: T.serif, fontSize: 28, fontWeight: 500, color: T.ink, letterSpacing: -0.5, margin: '7px 0 0' }}>Three doors in; every branch lands somewhere.</div>
      <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.mute, margin: '4px 0 22px', maxWidth: 620 }}>
        Gold = Vesper / the diary. Blue = a user choice. Red = an opt-out that still lands. Dashed = a deferred or “later” state.
      </p>

      <div style={{ display: 'flex', gap: 26, alignItems: 'flex-start' }}>
        {/* ── DOOR 1 · COLD START ── */}
        <div style={{ flex: '1.7 1 0', minWidth: 0, padding: '14px 16px', background: '#FBF7EC', borderRadius: 10, border: `0.5px solid ${T.hairline}` }}>
          <div style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 1.6, color: PT.goldd, fontWeight: 700, marginBottom: 12 }}>DOOR 1 · COLD START — a new user</div>
          <PNode k="1 · COVER" sub="crafted, not a login" tone="gold"/>
          <PStep/>
          <PNode k="2 · FORK" sub="“So — where are we going?” · no ask, no scan claim" tone="gold"/>
          <PCap>┈ SPLITS — the branch decides the ending ┈</PCap>
          <div style={{ display: 'flex', gap: 18, paddingLeft: 16 }}>
            {/* trip lane — the TRIP is the value; never detours to the gift */}
            <PLane title="A · A TRIP IN MIND" tone="blue">
              <PNode k="3a · WHERE" sub="place search" tone="blue"/>
              <PStep/>
              <PNode k="3b · WHEN" sub="duration" tone="blue"/>
              <PStep/>
              <PNode k="3c · WHO" sub="companions · invite seeds a group" tone="blue"/>
              <PStep label="START THE TRIP"/>
              <PNode k="SIGN IN · OPEN THE TRIP" sub="auth at peak intent — the trip already built" tone="blue"/>
              <PStep/>
              <PNode k="THE TRIP'S VESPER CHAT" sub="land straight in the conversation, planning together" tone="green"/>
              <PStep label="LATER · NOTIFICATION"/>
              <PNode k="THE DIARY, OFFERED" sub="a quiet opt-in nudge — never a full screen here" tone="gold" dashed/>
              <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 11, color: T.mute, marginTop: 6, lineHeight: 1.35 }}>
                ‹ back steps 3c→3b→3a→Fork · <b>Skip →</b> into the app (no trip yet) · “Talk it through” → Vesper assistant
              </div>
            </PLane>
            {/* dreaming lane — the DIARY is the value */}
            <PLane title="B · STILL DREAMING" tone="blue">
              <PNode k="4a · INTEREST" sub="food / art / nature / sea" tone="blue"/>
              <PStep/>
              <PNode k="4b · PACE" sub="slow-deep vs full-restless" tone="blue"/>
              <PStep/>
              <PNode k="THE GIFT" sub="the diary offered · iOS permission asked HERE, never screen 1" tone="gold"/>
              <PCap>┈ granted ┈</PCap>
              <PNode k="SIGN IN · DIARY CONSTRUCTS" sub="auth right after permission, while the diary develops (rich, or a fresh page if thin) — ready the moment you’re in" tone="gold"/>
              <PStep/>
              <PNode k="VESPER HOME" sub="you’re in — the diary is just part of the home now" tone="green"/>
              <PCap>┈ declined ┈</PCap>
              <PNode k="MAYBE LATER / DENY → SIGN IN" sub="no diary, but still sign in to make Atlas yours · then land, no diary · the door stays open" tone="red" dashed/>
            </PLane>
          </div>
        </div>

        {/* ── DOORS 2 & 3 ── */}
        <div style={{ flex: '1 1 0', minWidth: 0, display: 'flex', flexDirection: 'column', gap: 20 }}>
          <div style={{ padding: '14px 16px', background: '#FBF7EC', borderRadius: 10, border: `0.5px solid ${T.hairline}` }}>
            <div style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 1.6, color: PT.goldd, fontWeight: 700, marginBottom: 12 }}>DOOR 2 · INVITE — joining a friend</div>
            <PNode k="INVITE · PEEK" sub="real trip, dates, a friend who vouched + read-only glance" tone="gold"/>
            <PStep/>
            <PNode k="AUTH · “JOIN LISBON”" sub="value already here → sign in at peak intent" tone="blue"/>
            <PStep/>
            <PNode k="SHARED TRIP HOME" sub="lands straight in the real Trips surface" tone="green"/>
            <PStep label="LATER · OPT-IN"/>
            <PNode k="THE GIFT" sub="build your own diary — secondary, private" tone="gold" dashed/>
            <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 11, color: T.mute, marginTop: 8, lineHeight: 1.4 }}>
              Existing Vesper user → same peek, <b>skip auth</b>, straight to the trip. Escape hatch: “just set up Vesper for me” → cold start.
            </div>
          </div>
          <div style={{ padding: '14px 16px', background: '#FBF7EC', borderRadius: 10, border: `0.5px solid ${T.hairline}` }}>
            <div style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 1.6, color: PT.goldd, fontWeight: 700, marginBottom: 12 }}>DOOR 3 · RETURNING — already known</div>
            <PNode k="COVER · “I HAVE AN ACCOUNT”" sub="bypasses the whole pipeline" tone="blue"/>
            <PStep/>
            <PNode k="WELCOME BACK" sub="“everywhere you’ve been is still here”" tone="gold"/>
            <PStep/>
            <PNode k="STRAIGHT INTO THE APP" sub="diary & trips intact — no onboarding" tone="green"/>
          </div>
        </div>
      </div>
    </div>
  );
}

// ═══════════════════════════════════════════════════════════════
// PATH 1 TAIL — a trip in mind. After the capture you SIGN IN to
// open the trip (auth at peak intent), land in the trip's Vesper
// chat, and the photo-diary becomes a later, non-blocking
// notification — never a full screen on this path.
// ═══════════════════════════════════════════════════════════════

// ── 4 · SIGN IN TO OPEN THE TRIP → the Vesper chat. The trip's
// taking shape behind the ask; signing in opens it for good.
function V2TripSignIn() {
  const Line = ({ k, v }) => (
    <div style={{ display: 'flex', alignItems: 'baseline', gap: 10, padding: '9px 0', borderTop: ob3.hair }}>
      <span style={{ fontFamily: T.mono, fontSize: 8.5, letterSpacing: 1.4, color: T.goldDeep, fontWeight: 600, width: 52 }}>{k}</span>
      <span style={{ fontFamily: T.serif, fontSize: 16, color: T.ink, letterSpacing: -0.2 }}>{v}</span>
    </div>
  );
  return (
    <PFrame>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, display: 'flex', flexDirection: 'column', overflow: 'hidden' }}>
        <div style={{ padding: '44px 26px 0' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 12 }}>
            <VesperMark s={13} c={T.goldSoft}/>
            <span style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 2.4, color: T.goldDeep, fontWeight: 600 }}>VESPER · STARTING LISBON</span>
          </div>
          <h1 style={{ fontFamily: T.serif, fontSize: 26, fontWeight: 500, color: T.ink, letterSpacing: -0.5, lineHeight: 1.18, margin: 0 }}>
            Sign in to <span style={{ fontStyle: 'italic' }}>open your trip.</span>
          </h1>
          <p style={{ fontFamily: T.serif, fontSize: 14.5, color: T.soft, lineHeight: 1.48, margin: '9px 0 0' }}>
            Lisbon’s taking shape. Sign in and I’ll open it — we’ll keep planning together from here.
          </p>
        </div>
        {/* the trip, forming — the thing you're opening */}
        <div style={{ margin: '20px 24px 0', flex: 1, minHeight: 0, overflow: 'hidden', position: 'relative', paddingTop: 15, borderTop: ob3.hair }}>
          <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginBottom: 13 }}>
            <span style={{ fontFamily: T.mono, fontSize: 8.5, letterSpacing: 1.8, color: T.goldDeep, fontWeight: 600 }}>YOUR TRIP · TAKING SHAPE</span>
            <span style={{ fontFamily: T.mono, fontSize: 8.5, letterSpacing: 1, color: T.muteSoft, fontWeight: 600 }}>JUST STARTED</span>
          </div>
          <div style={{ height: 96, borderRadius: 14, overflow: 'hidden', position: 'relative', marginBottom: 4 }}>
            <GouacheScene scene="city" w={340} h={96}/>
            <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to top, rgba(239,234,224,0.55), rgba(239,234,224,0))' }}/>
          </div>
          <Line k="WHERE" v="Lisbon"/>
          <Line k="WHEN" v="About a week"/>
          <Line k="WHO" v="A few of you"/>
        </div>
        {/* the ask — auth at peak intent, the trip already built */}
        <div style={{ padding: '15px 26px 0' }}>
          <GlassAuthStack/>
          <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.mute, textAlign: 'center', margin: '13px 12px 0', lineHeight: 1.4 }}>
            Your trip lives on your phone until you say otherwise.
          </p>
        </div>
        <div style={{ height: 20 }}/>
      </div>
    </PFrame>
  );
}

// ── 5 · IN THE TRIP'S VESPER CHAT — you land straight in the
// conversation; Vesper picks up planning where the capture left off.
function V2TripChat({ notif = false }) {
  const ic = (d) => <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round">{d}</svg>;
  return (
    <PFrame>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, display: 'flex', flexDirection: 'column', overflow: 'hidden' }}>
        {/* header — trip-linked */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '10px 18px 14px', borderBottom: ob3.hair }}>
          {ic(<path d="M15 18l-6-6 6-6"/>)}
          <div style={{ flex: 1 }}>
            <div style={{ fontFamily: T.serif, fontSize: 18, fontWeight: 500, color: T.ink, letterSpacing: -0.3 }}>Lisbon, in June</div>
            <div style={{ fontFamily: T.mono, fontSize: 8, letterSpacing: 1.8, color: T.mute, fontWeight: 600, marginTop: 1 }}>PRIVATE · TRIP-LINKED</div>
          </div>
          <svg width="18" height="18" viewBox="0 0 24 24" fill={T.inkSoft}><circle cx="5" cy="12" r="1.5"/><circle cx="12" cy="12" r="1.5"/><circle cx="19" cy="12" r="1.5"/></svg>
        </div>
        {/* the conversation */}
        <div style={{ flex: 1, minHeight: 0, overflow: 'hidden', padding: '18px 22px 0', position: 'relative' }}>
          <div style={{ textAlign: 'center', marginBottom: 16 }}>
            <span style={{ fontFamily: T.mono, fontSize: 8, letterSpacing: 1.8, color: T.muteSoft, fontWeight: 600 }}>JUST NOW</span>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 9 }}>
            <VesperMark s={13}/><span style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 2.2, color: T.goldDeep, fontWeight: 600 }}>VESPER</span>
          </div>
          <p style={{ fontFamily: T.serif, fontSize: 16.5, color: T.ink, lineHeight: 1.5, letterSpacing: -0.15, margin: 0 }}>
            A week in Lisbon, a few of you — <span style={{ color: T.mute }}>good. I’ve started a shape: Alfama to land slow, a day out to Sintra, the coast for the back half.</span>
          </p>
          <p style={{ fontFamily: T.serif, fontSize: 16.5, color: T.ink, lineHeight: 1.5, letterSpacing: -0.15, margin: '13px 0 0' }}>
            Where do you want to begin?
          </p>
          {/* a couple of starter chips */}
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8, marginTop: 16 }}>
            {['Where we sleep', 'Pin the Sintra day', 'Invite the others'].map((c) => (
              <span key={c} style={{ padding: '8px 14px', borderRadius: 999, background: T.cardWarm, border: `0.5px solid ${T.hairline}`, fontFamily: T.serif, fontSize: 14, color: T.inkSoft }}>{c}</span>
            ))}
          </div>
        </div>
        {/* in-app diary notification — slides in later, non-blocking */}
        {notif && (
          <div style={{ position: 'absolute', left: 12, right: 12, top: 92, background: T.bg, borderRadius: 16, border: `0.5px solid ${T.goldSoft}`, boxShadow: '0 16px 36px -14px rgba(0,0,0,0.4)', padding: '13px 15px', display: 'flex', alignItems: 'flex-start', gap: 11 }}>
            <div style={{ width: 30, height: 30, borderRadius: 8, background: T.goldDeep, display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}><VesperMark s={15} c={T.cardWarm}/></div>
            <div style={{ flex: 1, minWidth: 0 }}>
              <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', gap: 8 }}>
                <span style={{ fontFamily: T.mono, fontSize: 8, letterSpacing: 1.6, color: T.goldDeep, fontWeight: 700 }}>VESPER · A SIDE NOTE</span>
                <span style={{ fontFamily: T.mono, fontSize: 8, letterSpacing: 1, color: T.muteSoft, fontWeight: 600 }}>now</span>
              </div>
              <p style={{ fontFamily: T.serif, fontSize: 14.5, color: T.ink, lineHeight: 1.4, margin: '4px 0 0' }}>
                Want a <span style={{ fontStyle: 'italic' }}>diary of your own?</span> I can keep the trips in your photos — privately, just for you.
              </p>
              <div style={{ display: 'flex', alignItems: 'center', gap: 16, marginTop: 10 }}>
                <span style={{ fontFamily: T.sans, fontSize: 13, fontWeight: 600, color: T.goldDeep }}>Build my diary</span>
                <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.mute }}>Not now</span>
              </div>
            </div>
          </div>
        )}
        {/* composer */}
        <div style={{ padding: '10px 16px 0' }}>
          <Composer placeholder="Reply, or pick one above…"/>
        </div>
        <div style={{ height: 14 }}/>
      </div>
      <TabBar active="vesper"/>
    </PFrame>
  );
}

Object.assign(window, { FoundRow, DevStrip, V2Fork, V2TasteInterest, V2TastePace, V2TripWhere, V2TripWhen, V2TripWho, V2TripSignIn, V2TripChat, AtlasDeveloping, V2Save, V2Land, PipelinePaths });
