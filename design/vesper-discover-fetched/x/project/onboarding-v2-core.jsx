// ═══════════════════════════════════════════════════════════════
// VESPER · ONBOARDING v2 — the gift-first pipeline.
// Value before the ask: the diary develops from your photos while a
// light fork/taste beat hides the latency; auth lands at peak intent.
// Reuses onboarding-kit (PFrame, EdKick, Vesper, Composer, Chip,
// Body, OB), design-system (T, Phone, TabBar, VesperMark),
// v3-shared (PostcardScene, YearRibbonH).
// ═══════════════════════════════════════════════════════════════

const ob2 = { hair: `0.5px solid ${T.hairline}`, hairT: `0.5px solid ${T.hairThin}` };

// ── THE DIARY TIMELINE — the gift artifact. A vertical spine whose
// connectors meet exactly at each node centre. mode: empty | developing | full
// ringBg = the surface colour behind it (for the node's halo ring).
function DTRow({ r, first, last, ringBg }) {
  const done = !r.ghost && !r.dev && !r.pending;
  const seg = (half) => (
    <span style={{ position: 'absolute', left: '50%', [half]: 0, height: '50%', width: 1.5, transform: 'translateX(-50%)', background: r.pending || r.dev ? 'transparent' : T.hairline, borderLeft: (r.pending || r.dev) ? `1.5px dashed ${T.faint}` : 'none' }}/>
  );
  let node;
  if (done) node = <span style={{ width: 9, height: 9, borderRadius: 999, background: T.goldDeep, boxShadow: `0 0 0 2.5px ${ringBg}, 0 0 0 3.5px ${T.hairline}` }}/>;
  else if (r.dev) node = <span style={{ width: 10, height: 10, borderRadius: 999, background: T.goldSoft, boxShadow: `0 0 0 2.5px ${ringBg}, 0 0 0 6px rgba(176,133,58,0.16)` }}/>;
  else node = <span style={{ width: 8, height: 8, borderRadius: 999, background: ringBg, border: `1.5px solid ${T.muteSoft}` }}/>;
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '28px 26px 1fr', alignItems: 'stretch' }}>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'flex-end', paddingRight: 3 }}>
        <span style={{ fontFamily: T.mono, fontSize: 9.5, color: r.ghost ? T.muteSoft : T.mute, letterSpacing: 0.4, fontWeight: 600 }}>{r.y}</span>
      </div>
      <div style={{ position: 'relative' }}>
        {!first && seg('top')}
        {!last && seg('bottom')}
        <span style={{ position: 'absolute', left: '50%', top: '50%', transform: 'translate(-50%,-50%)', display: 'flex' }}>{node}</span>
      </div>
      <div style={{ padding: '8px 0 8px 6px', display: 'flex', alignItems: 'center', gap: 12 }}>
        {r.ghost ? (
          <>
            <div style={{ width: 42, height: 31, borderRadius: 7, border: `1px dashed ${T.faint}`, flexShrink: 0 }}/>
            <div style={{ flex: 1 }}>
              <div style={{ width: '52%', height: 7, borderRadius: 4, background: T.faint }}/>
              <div style={{ width: '34%', height: 6, borderRadius: 4, background: T.faint, marginTop: 6, opacity: 0.7 }}/>
            </div>
          </>
        ) : r.pending ? (
          <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.muteSoft }}>still developing…</span>
        ) : (
          <>
            <div style={{ width: 46, height: 35, borderRadius: 7, overflow: 'hidden', flexShrink: 0, border: ob2.hair, filter: r.dev ? 'grayscale(0.55) opacity(0.72)' : 'none' }}><PostcardScene scene={r.scene}/></div>
            <div style={{ flex: 1, minWidth: 0 }}>
              <div style={{ fontFamily: T.serif, fontSize: 16.5, fontWeight: 500, color: r.dev ? T.soft : T.ink, letterSpacing: -0.2, lineHeight: 1.05 }}>{r.place}</div>
              <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.mute, marginTop: 2 }}>{r.dev ? 'developing…' : r.note}</div>
            </div>
          </>
        )}
      </div>
    </div>
  );
}
function DiaryTimeline({ mode = 'full', ringBg = T.cardWarm }) {
  const data = [
    { y: '’26', place: 'Lisbon', note: 'twice this spring', scene: 'lisbon' },
    { y: '’25', place: 'Tokyo', note: 'a winter week', scene: 'tokyo' },
    { y: '’25', place: 'Porto', note: 'the long weekend', scene: 'porto' },
    { y: '’24', place: 'Lisbon', note: 'where it started', scene: 'lisbon' },
  ];
  let rows;
  if (mode === 'empty') rows = ['’26', '’25', '’24', '’23'].map((y) => ({ ghost: true, y }));
  else if (mode === 'developing') rows = [data[0], data[1], { ...data[2], dev: true }, { pending: true, y: '’24' }];
  else rows = data;
  return (
    <div>
      {rows.map((r, i) => <DTRow key={i} r={r} first={i === 0} last={i === rows.length - 1} ringBg={ringBg}/>)}
    </div>
  );
}

// ── 1 · COVER ───────────────────────────────────────────────────
function V2Cover() {
  return (
    <Phone bg="#16120E">
      <div style={{ position: 'absolute', inset: 0 }}>
        <div style={{ position: 'absolute', inset: 0, opacity: 0.32 }}><PostcardScene scene="lisbon"/></div>
        <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(22,18,14,0.55), rgba(22,18,14,0.4) 40%, rgba(22,18,14,0.92))' }}/>
        <div style={{ position: 'absolute', inset: 0, paddingTop: 54, display: 'flex', flexDirection: 'column' }}>
          <div style={{ flex: 1, display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', padding: '0 40px', textAlign: 'center' }}>
            <VesperMark s={30} c={T.goldSoft}/>
            <h1 style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 40, fontWeight: 500, color: '#F7F2E7', letterSpacing: -0.8, lineHeight: 1.05, margin: '24px 0 0' }}>
              Every place<br/>you’ve loved.
            </h1>
            <p style={{ fontFamily: T.mono, fontSize: 10, letterSpacing: 2, color: 'rgba(217,189,134,0.85)', fontWeight: 600, margin: '22px 0 0' }}>A TRAVEL CONCIERGE WITH TASTE</p>
          </div>
          <div style={{ padding: '0 26px 36px' }}>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 8, padding: '15px 0', background: T.gold, color: '#1B1714', borderRadius: 14, fontFamily: T.sans, fontSize: 15, fontWeight: 600 }}>
              Begin <span style={{ opacity: 0.7 }}>→</span>
            </div>
            <div style={{ textAlign: 'center', marginTop: 16 }}>
              <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: 'rgba(247,242,231,0.6)' }}>I already have an account</span>
            </div>
          </div>
        </div>
      </div>
    </Phone>
  );
}

// ── THE GIFT — a contextual offer (after the fork). Sells the diary
// with a LOCKED PREVIEW, not an empty box. Both answers → Atlas.
function V2Gift() {
  return (
    <PFrame>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, display: 'flex', flexDirection: 'column' }}>
        <div style={{ padding: '44px 26px 0' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 12 }}>
            <VesperMark s={13}/><span style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 2.4, color: T.goldDeep, fontWeight: 600 }}>VESPER · ONE MORE THING</span>
          </div>
          <h1 style={{ fontFamily: T.serif, fontSize: 27, fontWeight: 500, color: T.ink, letterSpacing: -0.5, lineHeight: 1.18, margin: 0 }}>
            Want a <span style={{ fontStyle: 'italic' }}>diary of your own?</span>
          </h1>
          <p style={{ fontFamily: T.serif, fontSize: 15, color: T.soft, lineHeight: 1.5, margin: '12px 0 0' }}>
            While we plan this, I can turn your past trips into a diary — the cities, the years, the ones you’d forgotten. Yours to keep, never shared.
          </p>
        </div>
        {/* the locked preview — show what they'd get, frosted */}
        <div style={{ margin: '22px 26px 0', flex: 1, position: 'relative', borderRadius: 18, overflow: 'hidden', border: ob2.hair, background: T.cardWarm }}>
          <div style={{ padding: '18px 16px', filter: 'blur(2.5px)', opacity: 0.5 }}>
            <div style={{ fontFamily: T.mono, fontSize: 8.5, letterSpacing: 1.8, color: T.goldDeep, fontWeight: 600, marginBottom: 16 }}>YOUR DIARY</div>
            <DiaryTimeline mode="full" ringBg={T.cardWarm}/>
          </div>
          <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(251,247,236,0.5), rgba(251,247,236,0.82))', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', textAlign: 'center', padding: '0 30px' }}>
            <div style={{ fontFamily: T.serif, fontSize: 19, fontWeight: 500, color: T.ink, letterSpacing: -0.3 }}>Your years are in here.</div>
            <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.mute, marginTop: 4 }}>unlock them with your photos</div>
          </div>
        </div>
        <div style={{ padding: '18px 26px 30px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 14, justifyContent: 'center' }}>
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke={T.mute} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
            <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.mute }}>I look on your device. Nothing leaves your phone.</span>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 8, padding: '15px 0', background: T.gold, color: '#1B1714', borderRadius: 14, fontFamily: T.sans, fontSize: 15, fontWeight: 600 }}>
            <VesperMark s={15} c="#1B1714"/> Build my diary
          </div>
          <div style={{ textAlign: 'center', marginTop: 14 }}>
            <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.mute }}>Maybe later — take me in</span>
          </div>
        </div>
      </div>
    </PFrame>
  );
}

// ── 3 · PERMISSION — the iOS sheet, Vesper-framed ───────────────
function V2Permission() {
  return (
    <Phone bg={T.bg}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54 }}>
        {/* dimmed diary behind */}
        <div style={{ padding: '34px 26px 0', filter: 'blur(1.5px)', opacity: 0.5 }}>
          <h1 style={{ fontFamily: T.serif, fontSize: 27, fontWeight: 500, color: T.ink, letterSpacing: -0.5, lineHeight: 1.18, margin: 0 }}>Want a <span style={{ fontStyle: 'italic' }}>diary of your own?</span></h1>
        </div>
        <div style={{ position: 'absolute', inset: 0, background: 'rgba(22,18,14,0.32)' }}/>
        {/* the iOS permission sheet */}
        <div style={{ position: 'absolute', left: 18, right: 18, bottom: 24, background: '#F4F1EC', borderRadius: 20, overflow: 'hidden', boxShadow: '0 20px 50px -16px rgba(0,0,0,0.5)' }}>
          <div style={{ padding: '22px 22px 18px', textAlign: 'center', borderBottom: `0.5px solid ${T.hairline}` }}>
            <div style={{ fontFamily: T.sans, fontSize: 15.5, fontWeight: 700, color: '#000', letterSpacing: -0.2 }}>“Vesper” would like to access your Photos</div>
            <div style={{ fontFamily: T.sans, fontSize: 12.5, color: '#3C3C43', lineHeight: 1.45, margin: '8px 14px 0' }}>Vesper reads your library on-device to build your travel diary. Your photos are never uploaded or shared.</div>
            {/* a tiny preview of what it'll make */}
            <div style={{ display: 'flex', gap: 5, justifyContent: 'center', marginTop: 14 }}>
              {['lisbon', 'tokyo', 'porto'].map((s) => <div key={s} style={{ width: 40, height: 30, borderRadius: 5, overflow: 'hidden' }}><PostcardScene scene={s}/></div>)}
            </div>
          </div>
          <div style={{ display: 'flex', flexDirection: 'column' }}>
            {['Select Photos…', 'Allow Access to All Photos'].map((t, i) => (
              <div key={t} style={{ padding: '13px 0', textAlign: 'center', fontFamily: T.sans, fontSize: 15.5, color: '#0A84FF', fontWeight: i === 1 ? 600 : 400, borderBottom: `0.5px solid ${T.hairline}` }}>{t}</div>
            ))}
            <div style={{ padding: '13px 0', textAlign: 'center', fontFamily: T.sans, fontSize: 15.5, color: '#0A84FF' }}>Don’t Allow</div>
          </div>
        </div>
      </div>
    </Phone>
  );
}

// ── FLOATING GLASS AUTH — shared across all auth surfaces. Glass
// reads only over imagery, so the auth zone carries a faint gouache
// wash behind these (see AuthZone). provider: apple | google | email
const AUTH_GLYPH = {
  apple: <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M17.05 12.04c-.03-3.09 2.52-4.57 2.64-4.64-1.44-2.1-3.68-2.39-4.48-2.42-1.9-.19-3.71 1.12-4.68 1.12-.96 0-2.45-1.09-4.03-1.06-2.07.03-3.99 1.21-5.06 3.06-2.16 3.75-.55 9.3 1.55 12.35 1.03 1.49 2.25 3.16 3.86 3.1 1.55-.06 2.13-1 4-1 1.86 0 2.39 1 4.03.97 1.66-.03 2.72-1.52 3.74-3.02 1.18-1.73 1.66-3.4 1.69-3.49-.04-.02-3.24-1.25-3.27-4.93M14.4 4.27c.85-1.03 1.43-2.46 1.27-3.89-1.23.05-2.72.82-3.6 1.85-.79.91-1.48 2.37-1.3 3.77 1.37.11 2.78-.7 3.63-1.73"/></svg>,
  google: <span style={{ fontFamily: T.sans, fontWeight: 700, fontSize: 16, lineHeight: 1 }}>G</span>,
  email: <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M3.5 7.5l8.5 5.5 8.5-5.5"/></svg>,
};
function GlassAuth({ provider, onDark }) {
  return (
    <div style={{
      display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 10, padding: '14px 0', borderRadius: 15,
      background: onDark ? 'rgba(247,242,231,0.13)' : 'rgba(251,247,236,0.5)',
      backdropFilter: 'blur(18px)', WebkitBackdropFilter: 'blur(18px)',
      border: `0.5px solid ${onDark ? 'rgba(247,242,231,0.3)' : 'rgba(255,255,255,0.75)'}`,
      boxShadow: onDark ? '0 12px 30px -14px rgba(0,0,0,0.6), inset 0 1px 0 rgba(255,255,255,0.18)' : '0 12px 28px -14px rgba(20,14,9,0.42), inset 0 1px 0 rgba(255,255,255,0.55)',
      color: onDark ? '#F7F2E7' : T.ink, fontFamily: T.sans, fontSize: 14.5, fontWeight: 600,
    }}>
      <span style={{ display: 'flex' }}>{AUTH_GLYPH[provider]}</span>
      <span>Continue with {provider === 'apple' ? 'Apple' : provider === 'google' ? 'Google' : 'email'}</span>
    </div>
  );
}
function GlassAuthStack({ onDark }) {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
      <GlassAuth provider="apple" onDark={onDark}/>
      <GlassAuth provider="google" onDark={onDark}/>
      <GlassAuth provider="email" onDark={onDark}/>
    </div>
  );
}
// A faint gouache wash so the glass has something to refract.
function AuthWash({ scene = 'coast', h = 320 }) {
  return (
    <div style={{ position: 'absolute', left: 0, right: 0, bottom: 0, height: h, pointerEvents: 'none' }}>
      <div style={{ position: 'absolute', inset: 0, opacity: 0.22 }}><GouacheScene scene={scene} w={393} h={h}/></div>
      <div style={{ position: 'absolute', inset: 0, background: `linear-gradient(to bottom, ${T.bg} 0%, rgba(239,234,224,0.4) 40%, rgba(239,234,224,0.15) 100%)` }}/>
    </div>
  );
}

Object.assign(window, { DiaryTimeline, V2Cover, V2Gift, V2Permission, GlassAuth, GlassAuthStack, AuthWash });
