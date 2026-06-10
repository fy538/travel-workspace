// ═══════════════════════════════════════════════════════════════
// VESPER · ONBOARDING v2 — INVITE FLOW.
// A different (stronger) door: you arrive via a friend's invite, so
// value is already here — a real trip, real dates, a friend who
// vouched. The trip is the hook; the photo-diary gift becomes a
// delightful SECONDARY, offered only once you're in. No fork, no
// taste beats (this IS the trip). Two cases: new invitee + existing
// Vesper user. Reuses PFrame, Body, OB, T, VesperMark, TabBar,
// GouacheScene, PostcardScene.
// ═══════════════════════════════════════════════════════════════

const obi = { hair: `0.5px solid ${T.hairline}`, hairT: `0.5px solid ${T.hairThin}` };
const AV = { A: '#7E9176', B: '#41566E', M: '#B0704A', Y: T.goldDeep, J: '#7C5A63' };

function Avatar({ id, s = 30, ring }) {
  return (
    <div style={{ width: s, height: s, borderRadius: 999, background: AV[id] || T.mute, color: '#F4EFE3', fontFamily: T.serif, fontWeight: 500, fontSize: s * 0.42, display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0, boxShadow: ring ? `0 0 0 2px ${ring}` : 'none' }}>{id}</div>
  );
}
function AvatarStack({ ids, s = 28 }) {
  return (
    <div style={{ display: 'flex' }}>
      {ids.map((id, i) => <div key={i} style={{ marginLeft: i ? -s * 0.32 : 0, borderRadius: 999, boxShadow: `0 0 0 2px ${T.bg}` }}><Avatar id={id} s={s}/></div>)}
    </div>
  );
}
function InvPrompt({ kicker, children }) {
  return (
    <div>
      <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 10 }}>
        <VesperMark s={12}/><span style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 2.4, color: T.goldDeep, fontWeight: 600 }}>{kicker}</span>
      </div>
      <p style={{ fontFamily: T.serif, fontSize: 16.5, fontStyle: 'italic', color: T.ink, lineHeight: 1.5, margin: 0, paddingLeft: 13, borderLeft: `2px solid ${T.gold}` }}>{children}</p>
    </div>
  );
}
const BlueBtn = ({ children }) => <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 8, padding: '15px 0', background: OB.blue, color: '#fff', borderRadius: 14, fontFamily: T.sans, fontSize: 15, fontWeight: 600 }}>{children}</div>;
// primary floating-glass CTA — blue-tinted so it still reads as the main action
const GlassCTA = ({ children }) => <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 8, padding: '15px 0', borderRadius: 15, background: 'rgba(61,80,102,0.66)', backdropFilter: 'blur(18px)', WebkitBackdropFilter: 'blur(18px)', border: '0.5px solid rgba(255,255,255,0.34)', boxShadow: '0 14px 30px -12px rgba(42,56,75,0.6), inset 0 1px 0 rgba(255,255,255,0.4)', color: '#fff', fontFamily: T.sans, fontSize: 15, fontWeight: 600 }}>{children}</div>;

// ── 1 · THE INVITE — the face of the app: a beautiful invitation,
// the whole trip as a sleek illustrated timeline (all six days).
const ITIN = [
  { d: '12', day: 'THU', title: 'Arrival', sub: 'Land at noon, settle into a tiled flat in Alfama.' },
  { d: '13', day: 'FRI', title: 'Into the old city', sub: 'The tile museum, then a long dinner Ana’s holding.' },
  { d: '14', day: 'SAT', title: 'Yours to shape', sub: 'One day left open — tell Vesper what you’re after.', open: true },
  { d: '15', day: 'SUN', title: 'Up to Sintra', sub: 'A slow day in the palaces above the town.' },
  { d: '16', day: 'MON', title: 'The coast', sub: 'Down to Cascais for the afternoon sea.' },
  { d: '17', day: 'TUE', title: 'Last morning', sub: 'One more lunch by the water, then home.' },
];
function DayLine({ r, first, last }) {
  const accent = r.open ? T.goldDeep : T.ink;
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '34px 20px 1fr', columnGap: 12 }}>
      <div style={{ textAlign: 'right', paddingTop: 1 }}>
        <div style={{ fontFamily: T.serif, fontSize: 19, fontWeight: 500, color: accent, lineHeight: 0.9 }}>{r.d}</div>
        <div style={{ fontFamily: T.mono, fontSize: 7, letterSpacing: 1, color: r.open ? T.gold : T.muteSoft, fontWeight: 600, marginTop: 3 }}>{r.day}</div>
      </div>
      <div style={{ position: 'relative' }}>
        {!first && <span style={{ position: 'absolute', left: '50%', top: 0, height: 11, width: 1.5, transform: 'translateX(-50%)', background: T.hairline }}/>}
        {!last && <span style={{ position: 'absolute', left: '50%', top: 11, bottom: -16, width: 1.5, transform: 'translateX(-50%)', background: T.hairline }}/>}
        <span style={{ position: 'absolute', left: '50%', top: 11, transform: 'translate(-50%,-50%)', width: r.open ? 11 : 8, height: r.open ? 11 : 8, borderRadius: 999, background: r.open ? T.gold : T.cardWarm, border: r.open ? 'none' : `1.5px solid ${T.muteSoft}`, boxShadow: r.open ? `0 0 0 4px rgba(176,133,58,0.16)` : 'none' }}/>
      </div>
      <div style={{ paddingBottom: last ? 0 : 16 }}>
        <div style={{ fontFamily: T.serif, fontSize: 17.5, fontWeight: 500, fontStyle: r.open ? 'italic' : 'normal', color: accent, letterSpacing: -0.3, lineHeight: 1.05 }}>{r.title}</div>
        <div style={{ fontFamily: T.serif, fontSize: 13.5, color: r.open ? T.gold : T.mute, lineHeight: 1.35, marginTop: 4, minHeight: 37, display: '-webkit-box', WebkitLineClamp: 2, WebkitBoxOrient: 'vertical', overflow: 'hidden' }}>{r.sub}</div>
      </div>
    </div>
  );
}
function InvInvite() {
  return (
    <PFrame>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, display: 'flex', flexDirection: 'column' }}>
        <AuthWash scene="city" h={158}/>
        {/* cinematic hero */}
        <div style={{ position: 'relative', height: 218, flexShrink: 0 }}>
          <GouacheScene scene="city" w={393} h={218}/>
          <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.42), rgba(20,14,9,0.05) 34%, rgba(20,14,9,0.12) 52%, rgba(20,14,9,0.9))' }}/>
          <div style={{ position: 'absolute', top: 16, left: 22, right: 22, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
            <span style={{ fontFamily: T.mono, fontSize: 8.5, letterSpacing: 3, color: 'rgba(247,242,231,0.92)', fontWeight: 600 }}>AN INVITATION</span>
            <VesperMark s={15} c="rgba(247,242,231,0.92)"/>
          </div>
          <div style={{ position: 'absolute', left: 24, right: 24, bottom: 18 }}>
            <div style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 2, color: 'rgba(247,242,231,0.8)', fontWeight: 600, marginBottom: 7 }}>JUNE 12 – 17 · SIX DAYS</div>
            <h1 style={{ fontFamily: T.serif, fontSize: 52, fontWeight: 500, color: '#F7F2E7', letterSpacing: -1.4, margin: 0, lineHeight: 0.9 }}>Lisbon</h1>
          </div>
        </div>
        {/* the invitation body */}
        <div style={{ position: 'relative', flex: 1, minHeight: 0, display: 'flex', flexDirection: 'column', padding: '18px 26px 0' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 11, flexShrink: 0 }}>
            <Avatar id="A" s={38}/>
            <div style={{ flex: 1, minWidth: 0 }}>
              <div style={{ fontFamily: T.serif, fontSize: 16.5, fontWeight: 500, color: T.ink, letterSpacing: -0.2 }}>Ana invited you along</div>
              <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.mute, marginTop: 1 }}>“it won’t be the same without you.”</div>
            </div>
            <AvatarStack ids={['B', 'M']} s={26}/>
          </div>
          {/* the whole trip — a sleek timeline, scrollable */}
          <div style={{ marginTop: 18, paddingTop: 18, borderTop: obi.hairT, flex: 1, minHeight: 0, overflowY: 'auto' }}>
            {ITIN.map((r, i) => <DayLine key={i} r={r} first={i === 0} last={i === ITIN.length - 1}/>)}
          </div>
        </div>
        {/* the ask */}
        <div style={{ position: 'relative', padding: '16px 26px 26px' }}>
          <GlassCTA>Join the trip <span style={{ opacity: 0.8 }}>→</span></GlassCTA>
          <div style={{ textAlign: 'center', marginTop: 13 }}>
            <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.mute }}>Not now — just set up Vesper for me →</span>
          </div>
        </div>
      </div>
    </PFrame>
  );
}

// ── 3 · AUTH — framed as joining, at peak intent ────────────────
function InvAuth() {
  return (
    <PFrame>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, display: 'flex', flexDirection: 'column' }}>
        <AuthWash scene="city"/>
        <div style={{ position: 'relative', padding: '40px 28px 0', textAlign: 'center' }}>
          <div style={{ display: 'flex', justifyContent: 'center', marginBottom: 20 }}><AvatarStack ids={['A', 'B', 'M']} s={44}/></div>
          <h1 style={{ fontFamily: T.serif, fontSize: 28, fontWeight: 500, color: T.ink, letterSpacing: -0.5, lineHeight: 1.16, margin: 0 }}>Join <span style={{ fontStyle: 'italic' }}>Lisbon.</span></h1>
          <p style={{ fontFamily: T.serif, fontSize: 15, color: T.soft, lineHeight: 1.5, margin: '10px 18px 0' }}>
            Ana, Ben & Mara are waiting. Sign in and you’re in the room.
          </p>
        </div>
        <div style={{ position: 'relative', marginTop: 'auto', padding: '0 26px 30px' }}>
          <GlassAuthStack/>
          <div style={{ display: 'flex', alignItems: 'flex-start', gap: 8, marginTop: 16, padding: '0 6px' }}>
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke={T.mute} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round" style={{ flexShrink: 0, marginTop: 2 }}><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
            <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.mute, lineHeight: 1.4 }}>Your plans are shared with the group. What you tell Vesper privately stays private.</span>
          </div>
        </div>
      </div>
    </PFrame>
  );
}

// ── 4 · LAND IN THE TRIP — social, in-context, not solitary ─────
// ── 4 · THE GIFT, DEFERRED — private, secondary, opt-in ─────────
function InvGift() {
  return (
    <PFrame>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54 }}>
        {/* the trip home, dimmed behind */}
        <div style={{ padding: '14px 20px 0', filter: 'blur(2px)', opacity: 0.45 }}>
          <span style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 2.2, color: T.mute, fontWeight: 600 }}>TRIPS · LISBON · JUNE</span>
          <div style={{ height: 120, marginTop: 14, borderRadius: 16, overflow: 'hidden' }}><GouacheScene scene="city" w={360} h={120}/></div>
        </div>
        <div style={{ position: 'absolute', inset: 0, background: 'rgba(22,18,14,0.34)' }}/>
        {/* the gift sheet */}
        <div style={{ position: 'absolute', left: 14, right: 14, bottom: 18, background: T.bg, borderRadius: 22, overflow: 'hidden', boxShadow: '0 22px 50px -16px rgba(0,0,0,0.5)' }}>
          <div style={{ height: 92, position: 'relative' }}>
            <GouacheScene scene="coast" w={372} h={92}/>
            <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to top, rgba(239,234,224,0.9), rgba(239,234,224,0.1))' }}/>
          </div>
          <div style={{ padding: '4px 22px 24px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 10 }}>
              <VesperMark s={13}/><span style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 2.4, color: T.goldDeep, fontWeight: 600 }}>VESPER · A SIDE NOTE</span>
            </div>
            <h2 style={{ fontFamily: T.serif, fontSize: 23, fontWeight: 500, color: T.ink, letterSpacing: -0.4, lineHeight: 1.18, margin: 0 }}>
              While you’re here — want a <span style={{ fontStyle: 'italic' }}>diary of your own?</span>
            </h2>
            <p style={{ fontFamily: T.serif, fontSize: 14.5, color: T.soft, lineHeight: 1.5, margin: '10px 0 18px' }}>
              I can find the trips in your photos and keep them — just for you, never the group. Lisbon will join them when you’re back.
            </p>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 8, padding: '14px 0', background: T.gold, color: '#1B1714', borderRadius: 13, fontFamily: T.sans, fontSize: 15, fontWeight: 600 }}>
              <VesperMark s={14} c="#1B1714"/> Build my diary
            </div>
            <div style={{ textAlign: 'center', marginTop: 13 }}>
              <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 14, color: T.mute }}>Not now</span>
            </div>
          </div>
        </div>
      </div>
    </PFrame>
  );
}

Object.assign(window, { InvInvite, InvAuth, InvGift });
