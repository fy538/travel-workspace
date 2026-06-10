// ═══════════════════════════════════════════════════════════════
// VESPER · ONBOARDING v2 — THE SEAMS. The paths the main flow
// referenced but never showed:
//   A · Maybe-later / declined photos — graceful, no guilt.
//   B · The forming diary — the honest cold-start reveal (no/thin
//       photos): a blank page seeded by taste, not a rich library.
//   C/D · Email auth — entry → six-digit code.
//   E · Welcome back — the returning-user sign-in (cover's
//       "I already have an account" destination).
// Reuses PFrame, Body, T, OB, VesperMark, TabBar (globals) +
// GouacheScene, DiaryTimeline, GlassAuthStack, AuthWash (exported).
// ═══════════════════════════════════════════════════════════════

const sm = { hair: `0.5px solid ${T.hairline}`, hairT: `0.5px solid ${T.hairThin}` };
const GlassBlue = ({ children }) => <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 8, padding: '15px 0', borderRadius: 15, background: 'rgba(61,80,102,0.66)', backdropFilter: 'blur(18px)', WebkitBackdropFilter: 'blur(18px)', border: '0.5px solid rgba(255,255,255,0.34)', boxShadow: '0 14px 30px -12px rgba(42,56,75,0.6), inset 0 1px 0 rgba(255,255,255,0.4)', color: '#fff', fontFamily: T.sans, fontSize: 15, fontWeight: 600 }}>{children}</div>;

function SPrompt({ kicker = 'VESPER', heading, sub, center }) {
  return (
    <div style={{ textAlign: center ? 'center' : 'left' }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 12, justifyContent: center ? 'center' : 'flex-start' }}>
        <VesperMark s={13}/>
        <span style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 2.4, color: T.goldDeep, fontWeight: 600 }}>{kicker}</span>
      </div>
      <h1 style={{ fontFamily: T.serif, fontSize: 27, fontWeight: 500, color: T.ink, letterSpacing: -0.5, lineHeight: 1.18, margin: 0 }}>{heading}</h1>
      {sub && <p style={{ fontFamily: T.serif, fontSize: 15, color: T.soft, lineHeight: 1.5, margin: '11px 0 0' }}>{sub}</p>}
    </div>
  );
}

// ── A · MAYBE LATER / DECLINED — graceful, no guilt ─────────────
function SeamDecline() {
  return (
    <PFrame>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, display: 'flex', flexDirection: 'column' }}>
        <AuthWash scene="forest" h={300}/>
        <div style={{ position: 'relative', padding: '44px 28px 0' }}>
          <SPrompt kicker="VESPER" heading={<>We’ll build it <span style={{ fontStyle: 'italic' }}>as we go.</span></>} sub="No photos needed to start. Tell me what you like, and I’ll learn the rest over time — you can always let me look later."/>
        </div>
        <div style={{ flex: 1 }}/>
        <div style={{ position: 'relative', padding: '0 26px 30px' }}>
          <GlassBlue>Keep going <span style={{ opacity: 0.8 }}>→</span></GlassBlue>
          <div style={{ textAlign: 'center', marginTop: 13 }}>
            <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.mute }}>Change your mind — let Vesper look →</span>
          </div>
        </div>
      </div>
    </PFrame>
  );
}

// ── B · THE FORMING DIARY — honest cold-start reveal ────────────
function LearnedChip({ children }) {
  return <span style={{ padding: '7px 13px', borderRadius: 999, background: 'rgba(176,133,58,0.1)', border: `0.5px solid ${T.goldSoft}`, fontFamily: T.serif, fontSize: 13.5, color: T.goldDeep, letterSpacing: -0.1 }}>{children}</span>;
}
function SeamForming() {
  return (
    <PFrame>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, display: 'flex', flexDirection: 'column' }}>
        <AuthWash scene="coast" h={150}/>
        <div style={{ position: 'relative', padding: '30px 28px 0' }}>
          <SPrompt kicker="VESPER · A FRESH PAGE" heading={<>Your diary <span style={{ fontStyle: 'italic' }}>starts here.</span></>} sub="I couldn’t find much in your photos yet — so we begin with a blank page and what you’ve told me."/>
        </div>
        {/* what taste gave us, even with no history */}
        <div style={{ position: 'relative', padding: '18px 28px 0' }}>
          <div style={{ fontFamily: T.mono, fontSize: 8.5, letterSpacing: 1.8, color: T.mute, fontWeight: 600, marginBottom: 10 }}>WHAT I’VE LEARNED</div>
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8 }}>
            <LearnedChip>Slow & deep</LearnedChip>
            <LearnedChip>Food-led</LearnedChip>
            <LearnedChip>By the water</LearnedChip>
          </div>
        </div>
        {/* the blank page — the empty diary, un-boxed */}
        <div style={{ position: 'relative', flex: 1, margin: '22px 28px 0', paddingTop: 16, borderTop: sm.hair, minHeight: 0 }}>
          <div style={{ fontFamily: T.mono, fontSize: 8.5, letterSpacing: 1.8, color: T.goldDeep, fontWeight: 600, marginBottom: 14 }}>YOUR DIARY · BLANK</div>
          <DiaryTimeline mode="empty" ringBg={T.bg}/>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginTop: 12 }}>
            <VesperMark s={12}/>
            <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.mute }}>It fills as you travel. Lisbon could be the first page.</span>
          </div>
        </div>
        <div style={{ position: 'relative', padding: '16px 26px 28px' }}>
          <GlassAuthStack/>
        </div>
      </div>
    </PFrame>
  );
}

// ── C · EMAIL ENTRY ─────────────────────────────────────────────
function SeamEmail() {
  return (
    <PFrame>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, display: 'flex', flexDirection: 'column' }}>
        <AuthWash scene="city" h={150}/>
        <div style={{ position: 'relative', padding: '44px 28px 0' }}>
          <SPrompt kicker="VESPER" heading={<>What’s your <span style={{ fontStyle: 'italic' }}>email?</span></>} sub="I’ll send a six-digit code — no passwords to remember."/>
          <div style={{ marginTop: 24, display: 'flex', alignItems: 'center', gap: 11, padding: '15px 16px', background: T.cardWarm, border: sm.hair, borderRadius: 14 }}>
            <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke={T.mute} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M3.5 7.5l8.5 5.5 8.5-5.5"/></svg>
            <span style={{ flex: 1, fontFamily: T.serif, fontStyle: 'italic', fontSize: 16, color: T.muteSoft }}>you@email.com</span>
            <span style={{ width: 1.5, height: 20, background: T.gold }}/>
          </div>
        </div>
        <div style={{ flex: 1 }}/>
        <div style={{ position: 'relative', padding: '0 26px 30px' }}>
          <GlassBlue>Send the code <span style={{ opacity: 0.8 }}>→</span></GlassBlue>
          <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.mute, textAlign: 'center', margin: '14px 14px 0', lineHeight: 1.4 }}>By continuing you agree to the Terms & Privacy Policy.</p>
        </div>
      </div>
    </PFrame>
  );
}

// ── D · EMAIL CODE ──────────────────────────────────────────────
function OtpBoxes({ filled = '482' }) {
  const digits = filled.split('');
  return (
    <div style={{ display: 'flex', gap: 9, justifyContent: 'center' }}>
      {[0, 1, 2, 3, 4, 5].map((i) => (
        <div key={i} style={{ width: 46, height: 56, borderRadius: 12, background: T.cardSoft, border: `0.8px solid ${i === digits.length ? T.gold : T.hairline}`, display: 'flex', alignItems: 'center', justifyContent: 'center', position: 'relative' }}>
          <span style={{ fontFamily: T.serif, fontSize: 27, fontWeight: 500, color: T.ink }}>{digits[i] || ''}</span>
          {i === digits.length && <span style={{ width: 1.5, height: 24, background: T.gold }}/>}
        </div>
      ))}
    </div>
  );
}
function SeamCode() {
  return (
    <PFrame>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, display: 'flex', flexDirection: 'column' }}>
        <div style={{ padding: '44px 28px 0', textAlign: 'center' }}>
          <SPrompt center kicker="VESPER" heading={<>Check your <span style={{ fontStyle: 'italic' }}>mail.</span></>} sub="I sent a six-digit code to lina@email.com."/>
        </div>
        <div style={{ padding: '30px 22px 0' }}>
          <OtpBoxes filled="482"/>
        </div>
        <div style={{ textAlign: 'center', marginTop: 22 }}>
          <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.mute }}>Resend code</span>
          <span style={{ color: T.muteSoft, margin: '0 10px' }}>·</span>
          <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.mute }}>Different email</span>
        </div>
        <div style={{ flex: 1 }}/>
      </div>
    </PFrame>
  );
}

// ── E · WELCOME BACK — returning-user sign-in ───────────────────
function SeamReturn() {
  return (
    <PFrame>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, display: 'flex', flexDirection: 'column' }}>
        <AuthWash scene="harbor" h={360}/>
        <div style={{ position: 'relative', flex: 1, display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', padding: '0 36px', textAlign: 'center' }}>
          <VesperMark s={26} c={T.goldDeep}/>
          <h1 style={{ fontFamily: T.serif, fontSize: 34, fontWeight: 500, color: T.ink, letterSpacing: -0.8, lineHeight: 1, margin: '20px 0 0' }}>Welcome <span style={{ fontStyle: 'italic' }}>back.</span></h1>
          <p style={{ fontFamily: T.serif, fontSize: 15, color: T.soft, lineHeight: 1.5, margin: '12px 0 0', maxWidth: 250 }}>Everywhere you’ve been is still here. Pick up where you left off.</p>
        </div>
        <div style={{ position: 'relative', padding: '0 26px 34px' }}>
          <GlassAuthStack/>
        </div>
      </div>
    </PFrame>
  );
}

// ── A2 · DECLINED → SIGN IN (no diary). You said no to the gift,
// but still sign in to make Atlas yours — auth without a diary hook.
function V2DeclineSignIn() {
  return (
    <PFrame>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, display: 'flex', flexDirection: 'column' }}>
        <AuthWash scene="forest" h={300}/>
        <div style={{ position: 'relative', flex: 1, display: 'flex', flexDirection: 'column', justifyContent: 'center', padding: '24px 28px 0' }}>
          <SPrompt kicker="VESPER" heading={<>Make it <span style={{ fontStyle: 'italic' }}>yours.</span></>} sub="No diary for now — that’s fine. Sign in and Vesper’s yours; tell me what you like and I’ll learn the rest. You can let me look at your photos whenever you like."/>
          {/* what taste already gave us — so the no-diary screen isn't empty */}
          <div style={{ marginTop: 26 }}>
            <div style={{ fontFamily: T.mono, fontSize: 8.5, letterSpacing: 1.8, color: T.mute, fontWeight: 600, marginBottom: 10 }}>WHAT I’VE LEARNED</div>
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8 }}>
              <LearnedChip>Slow &amp; deep</LearnedChip>
              <LearnedChip>Food-led</LearnedChip>
              <LearnedChip>By the water</LearnedChip>
            </div>
          </div>
        </div>
        <div style={{ position: 'relative', padding: '0 26px 24px' }}>
          <GlassAuthStack/>
          <div style={{ textAlign: 'center', marginTop: 13 }}>
            <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.mute }}>Change your mind — let Vesper look →</span>
          </div>
        </div>
      </div>
    </PFrame>
  );
}

Object.assign(window, { SeamDecline, V2DeclineSignIn, SeamForming, SeamEmail, SeamCode, SeamReturn });
