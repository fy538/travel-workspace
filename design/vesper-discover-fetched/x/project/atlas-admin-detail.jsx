// ═══════════════════════════════════════════════════════════════
// ATLAS — admin detail screens behind the personal page's rows.
// CRUCIAL: what Vesper INFERRED reads as prose/observation (read-only
// portraits); what the user DECLARED is editable controls.
// Reuses AtlasFrame, Eyebrow, Initial, TabBar, T.
// ═══════════════════════════════════════════════════════════════

const dHair = `0.5px solid ${T.hairline}`;

// a detail-screen header (back · title · concept eyebrow)
function DetailHead({ eyebrow, title, concept }) {
  return (
    <div style={{ padding: '14px 22px 0' }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 6, color: T.inkSoft }}>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
        <span style={{ fontSize: 13, fontWeight: 500, color: T.inkSoft }}>You</span>
      </div>
      <div style={{ marginTop: 18 }}>
        <Eyebrow color={T.goldDeep}>{eyebrow}</Eyebrow>
        <h1 style={{ fontFamily: T.serif, fontWeight: 500, fontSize: 30, lineHeight: 1, letterSpacing: -0.6, color: T.ink, margin: '8px 0 0' }}>{title}</h1>
        {concept && <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.mute, margin: '8px 0 0' }}>{concept}</p>}
      </div>
    </div>
  );
}
function DFrame({ children }) {
  return <AtlasFrame>{children}<div style={{ height: 70 }}/><TabBar active="atlas"/></AtlasFrame>;
}

// a read-only inference badge
function Learned() {
  return <span style={{ display: 'inline-flex', alignItems: 'center', gap: 4, fontFamily: T.mono, fontSize: 7.5, letterSpacing: 1, fontWeight: 600, color: T.mute }}><span style={{ width: 4, height: 4, borderRadius: 999, background: T.goldSoft }}/>LEARNED</span>;
}
function Toggle({ on }) {
  return <div style={{ width: 38, height: 22, borderRadius: 999, background: on ? T.goldDeep : 'rgba(27,23,20,0.14)', position: 'relative', flexShrink: 0 }}><div style={{ position: 'absolute', top: 2, left: on ? 18 : 2, width: 18, height: 18, borderRadius: 999, background: '#fff' }}/></div>;
}

// ─── TRAVEL IDENTITY — read-only portrait ("how Vesper sees you") ─
function DTravelIdentity() {
  const phrases = ['slow mornings, long evenings', 'you follow the neighborhood before the landmark', 'leaves room for serendipity'];
  const dims = [['Energy', 'Relaxed', '4 trips'], ['Budget', 'Balanced', '5 trips'], ['Social', 'Small groups', '3 trips'], ['Planning', 'Loose', '4 trips']];
  return (
    <DFrame>
      <DetailHead eyebrow="HOW VESPER SEES YOU" title="A coastal soul." concept="a reading, drawn from your trips — not a setting"/>
      {/* the portrait, as prose */}
      <div style={{ margin: '24px 24px 0' }}>
        {phrases.map((p, i) => (
          <p key={i} style={{ fontFamily: T.serif, fontSize: 18, color: i === 0 ? T.ink : T.inkSoft, lineHeight: 1.5, margin: i ? '12px 0 0' : 0, letterSpacing: -0.2 }}>{p}.</p>
        ))}
      </div>
      {/* the evidence ledger */}
      <div style={{ margin: '28px 24px 0' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 6 }}><Eyebrow>THE EVIDENCE</Eyebrow><Learned/></div>
        {dims.map(([k, v, n], i) => (
          <div key={k} style={{ display: 'flex', alignItems: 'baseline', gap: 10, padding: '13px 0', borderTop: dHair }}>
            <span style={{ width: 78, fontFamily: T.mono, fontSize: 8.5, color: T.mute, letterSpacing: 1, fontWeight: 600 }}>{k.toUpperCase()}</span>
            <span style={{ flex: 1, fontFamily: T.serif, fontSize: 16, color: T.ink, fontWeight: 500, letterSpacing: -0.2 }}>{v}</span>
            <span style={{ fontFamily: T.serif, fontSize: 12, color: T.muteSoft }}>learned across {n}</span>
          </div>
        ))}
      </div>
      <div style={{ margin: '22px 24px 0', paddingTop: 14, borderTop: dHair }}>
        <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.goldDeep }}>What shaped this — the trips behind the reading →</span>
      </div>
    </DFrame>
  );
}

// ─── WHO YOU TRAVEL WITH — derived companion list ───────────────
function DCompanions() {
  const people = [['A', 'Ana', '6 trips', 'last spring', '#7C8F73'], ['T', 'Theo', '4 trips', 'last summer', '#A0703A'], ['M', 'Mara', '2 trips', 'two years ago', '#6E7E8F'], ['J', 'Jun', '1 trip', 'last winter', '#9A7B5A']];
  return (
    <DFrame>
      <DetailHead eyebrow="WHO YOU TRAVEL WITH" title="Your people." concept="drawn from who you actually travel with, by frequency"/>
      <div style={{ margin: '22px 24px 0' }}>
        {people.map(([ini, name, trips, last, c], i) => (
          <div key={name} style={{ display: 'flex', alignItems: 'center', gap: 13, padding: '14px 0', borderTop: i ? dHair : 'none' }}>
            <div style={{ width: 38, height: 38, borderRadius: 999, background: T.cardWarm, border: `0.5px solid ${T.hairline}`, color: c, fontFamily: T.serif, fontWeight: 500, fontSize: 16, display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>{ini}</div>
            <div style={{ flex: 1 }}>
              <div style={{ fontFamily: T.serif, fontSize: 17, color: T.ink, fontWeight: 500, letterSpacing: -0.2 }}>{name}</div>
              <div style={{ fontFamily: T.serif, fontSize: 12.5, color: T.mute, marginTop: 1 }}>{trips} · {last}</div>
            </div>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke={T.muteSoft} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M9 6l6 6-6 6"/></svg>
          </div>
        ))}
      </div>
      <div style={{ margin: '24px 24px 0' }}>
        <div style={{ padding: '13px 16px', background: T.cardWarm, borderRadius: 13, border: dHair, display: 'flex', alignItems: 'center', gap: 10 }}>
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke={T.goldDeep} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="8" r="3.2"/><path d="M5 20c0-3.5 3-6 7-6s7 2.5 7 6M19 8h4M21 6v4"/></svg>
          <span style={{ flex: 1, fontFamily: T.serif, fontSize: 15, color: T.ink, fontWeight: 500 }}>Invite someone to a trip</span>
          <span style={{ color: T.muteSoft }}>→</span>
        </div>
        <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.muteSoft, margin: '10px 4px 0', lineHeight: 1.4 }}>This isn’t an address book — it’s the people your trips remember. Travel together and they appear here.</p>
      </div>
    </DFrame>
  );
}

// ─── TASTE & PREFERENCES — Learned (read-only) + Declared (editable) ─
function DTaste() {
  const learned = [['Pace', 'Unhurried'], ['Food', 'Markets & tascas over fine dining'], ['Energy', 'One thing a day, done well'], ['Social', 'Small groups, quiet rooms']];
  const declared = [['Dietary', 'Pescatarian · no shellfish'], ['Accessibility', 'None set'], ['Languages', 'English · some Portuguese']];
  return (
    <DFrame>
      <DetailHead eyebrow="WHAT VESPER TUNES TO" title="Your taste." concept="some of this Vesper learned; some you tell it"/>
      {/* learned zone */}
      <div style={{ margin: '24px 24px 0' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 4 }}><Eyebrow>LEARNED</Eyebrow><Learned/></div>
        {learned.map(([k, v], i) => (
          <div key={k} style={{ display: 'flex', alignItems: 'baseline', gap: 10, padding: '12px 0', borderTop: dHair }}>
            <span style={{ width: 64, fontFamily: T.mono, fontSize: 8.5, color: T.mute, letterSpacing: 1, fontWeight: 600 }}>{k.toUpperCase()}</span>
            <span style={{ flex: 1, fontFamily: T.serif, fontSize: 15.5, color: T.inkSoft, letterSpacing: -0.1 }}>{v}</span>
          </div>
        ))}
        <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 11.5, color: T.muteSoft, margin: '10px 0 0' }}>Read-only — these shift as you travel.</p>
      </div>
      {/* declared zone */}
      <div style={{ margin: '28px 24px 0' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 4 }}><Eyebrow>YOU TOLD VESPER</Eyebrow><span style={{ fontFamily: T.mono, fontSize: 7.5, letterSpacing: 1, fontWeight: 600, color: T.goldDeep }}>EDITABLE</span></div>
        {declared.map(([k, v], i) => (
          <div key={k} style={{ display: 'flex', alignItems: 'center', gap: 10, padding: '13px 0', borderTop: dHair }}>
            <div style={{ flex: 1 }}>
              <div style={{ fontFamily: T.mono, fontSize: 8.5, color: T.mute, letterSpacing: 1, fontWeight: 600 }}>{k.toUpperCase()}</div>
              <div style={{ fontFamily: T.serif, fontSize: 15.5, color: v === 'None set' ? T.muteSoft : T.ink, fontStyle: v === 'None set' ? 'italic' : 'normal', fontWeight: 500, letterSpacing: -0.2, marginTop: 3 }}>{v}</div>
            </div>
            <span style={{ fontFamily: T.sans, fontSize: 12.5, fontWeight: 600, color: T.goldDeep }}>Edit</span>
          </div>
        ))}
      </div>
    </DFrame>
  );
}

// ─── PRIVACY — five sharing dimensions + profile + photos ───────
function DPrivacy() {
  const dims = [
    ['Budget', 'Private', 'only the Concierge uses this'],
    ['Taste', 'Shareable', 'helps your group plan together'],
    ['Saved places', 'Private', 'yours alone, by default'],
    ['Trips', 'Shareable', 'shared with the group you travel with'],
    ['Memories', 'Private', 'kept for you unless you share a story'],
  ];
  return (
    <DFrame>
      <DetailHead eyebrow="WHAT YOU SHARE" title="Privacy." concept="saves are private; trips are shared with your group"/>
      <div style={{ margin: '22px 24px 0' }}>
        {dims.map(([k, state, note], i) => {
          const share = state === 'Shareable';
          return (
            <div key={k} style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '14px 0', borderTop: i ? dHair : 'none' }}>
              <div style={{ flex: 1 }}>
                <div style={{ fontFamily: T.serif, fontSize: 16, color: T.ink, fontWeight: 500, letterSpacing: -0.2 }}>{k}</div>
                <div style={{ fontFamily: T.serif, fontSize: 12, color: T.mute, marginTop: 2 }}>{share ? 'Shareable' : 'Private'} — {note}</div>
              </div>
              <Toggle on={share}/>
            </div>
          );
        })}
      </div>
      <div style={{ margin: '26px 24px 0' }}>
        <Eyebrow>YOUR PROFILE</Eyebrow>
        <div style={{ marginTop: 4 }}>
          {[['Discoverable public profile', false], ['Let followers see my shared stories', true]].map(([k, on]) => (
            <div key={k} style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '13px 0', borderTop: dHair }}>
              <span style={{ flex: 1, fontFamily: T.serif, fontSize: 15.5, color: T.ink }}>{k}</span><Toggle on={on}/>
            </div>
          ))}
        </div>
      </div>
      <div style={{ margin: '26px 24px 0' }}>
        <Eyebrow>DEFAULT PHOTO VISIBILITY</Eyebrow>
        <div style={{ marginTop: 10, display: 'flex', gap: 7 }}>
          {['Private', 'Group', 'Group + help Vesper learn'].map((o, i) => (
            <span key={o} style={{ padding: '8px 12px', borderRadius: 999, fontFamily: T.sans, fontSize: 12, fontWeight: 600, color: i === 1 ? T.cardWarm : T.inkSoft, background: i === 1 ? T.goldDeep : T.cardWarm, border: i === 1 ? 'none' : dHair }}>{o}</span>
          ))}
        </div>
      </div>
    </DFrame>
  );
}

// ─── NOTIFICATIONS — cadence · quiet hours · channels ───────────
function DNotifications() {
  return (
    <DFrame>
      <DetailHead eyebrow="QUIET BY DEFAULT" title="Notifications." concept="Vesper speaks only when something’s genuinely worth it"/>
      <div style={{ margin: '22px 24px 0' }}>
        <Eyebrow>CADENCE</Eyebrow>
        <div style={{ marginTop: 10, display: 'flex', gap: 7 }}>
          {['Eager', 'Default', 'Minimal'].map((o, i) => (
            <span key={o} style={{ flex: 1, textAlign: 'center', padding: '10px 0', borderRadius: 11, fontFamily: T.sans, fontSize: 13, fontWeight: 600, color: i === 2 ? T.cardWarm : T.inkSoft, background: i === 2 ? T.goldDeep : T.cardWarm, border: i === 2 ? 'none' : dHair }}>{o}</span>
          ))}
        </div>
      </div>
      <div style={{ margin: '24px 24px 0' }}>
        <Eyebrow>QUIET HOURS</Eyebrow>
        <div style={{ marginTop: 8, display: 'flex', alignItems: 'center', gap: 10, padding: '13px 0', borderTop: dHair, borderBottom: dHair }}>
          <span style={{ fontFamily: T.serif, fontSize: 16, color: T.ink, fontWeight: 500 }}>9:30 PM → 8:00 AM</span>
          <span style={{ marginLeft: 'auto', fontFamily: T.serif, fontSize: 12.5, color: T.mute }}>Lisbon time</span>
        </div>
      </div>
      <div style={{ margin: '24px 24px 0' }}>
        <Eyebrow>CHANNELS</Eyebrow>
        <div style={{ marginTop: 4 }}>
          {[['In-app', true], ['Push', true], ['SMS', false], ['Email', false]].map(([k, on]) => (
            <div key={k} style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '12px 0', borderTop: dHair }}>
              <span style={{ flex: 1, fontFamily: T.serif, fontSize: 15.5, color: T.ink }}>{k}</span><Toggle on={on}/>
            </div>
          ))}
        </div>
      </div>
      <div style={{ margin: '22px 24px 0' }}>
        {[['Critical always', 'booking deadlines pierce quiet hours', true], ['Pause all', 'silence everything for now', false]].map(([k, s, on]) => (
          <div key={k} style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '13px 0', borderTop: dHair }}>
            <div style={{ flex: 1 }}>
              <div style={{ fontFamily: T.serif, fontSize: 15.5, color: T.ink, fontWeight: 500 }}>{k}</div>
              <div style={{ fontFamily: T.serif, fontSize: 12, color: T.mute, marginTop: 1 }}>{s}</div>
            </div>
            <Toggle on={on}/>
          </div>
        ))}
      </div>
    </DFrame>
  );
}

// ─── ACCOUNT — profile + access (billing marked speculative) ────
function DAccount() {
  return (
    <DFrame>
      <DetailHead eyebrow="PROFILE & ACCESS" title="Account." concept="who you are to Vesper, and how you sign in"/>
      <div style={{ margin: '22px 24px 0' }}>
        {[['NAME', 'Tiger Tang', true], ['EMAIL', 'tiger@nyu.edu', true], ['PHONE', '+1 ••• ••• 4821', true]].map(([k, v, verified]) => (
          <div key={k} style={{ display: 'flex', alignItems: 'center', gap: 10, padding: '13px 0', borderTop: dHair }}>
            <div style={{ flex: 1 }}>
              <div style={{ fontFamily: T.mono, fontSize: 8.5, color: T.mute, letterSpacing: 1, fontWeight: 600 }}>{k}</div>
              <div style={{ fontFamily: T.serif, fontSize: 16, color: T.ink, fontWeight: 500, letterSpacing: -0.2, marginTop: 3 }}>{v}</div>
            </div>
            {verified && <span style={{ fontFamily: T.mono, fontSize: 7.5, letterSpacing: 1, fontWeight: 600, color: '#5E7A52' }}>✓ VERIFIED</span>}
            <span style={{ fontFamily: T.sans, fontSize: 12.5, fontWeight: 600, color: T.goldDeep, marginLeft: 4 }}>Edit</span>
          </div>
        ))}
      </div>
      <div style={{ margin: '26px 24px 0' }}>
        <Eyebrow>CONNECTED</Eyebrow>
        <div style={{ marginTop: 4 }}>
          {[['Apple', 'Connected'], ['Google', 'Coming soon']].map(([k, s]) => (
            <div key={k} style={{ display: 'flex', alignItems: 'center', gap: 10, padding: '13px 0', borderTop: dHair }}>
              <span style={{ flex: 1, fontFamily: T.serif, fontSize: 15.5, color: T.ink }}>{k}</span>
              <span style={{ fontFamily: T.serif, fontSize: 12.5, color: s === 'Connected' ? '#5E7A52' : T.muteSoft }}>{s}</span>
            </div>
          ))}
        </div>
      </div>
      {/* membership — identity, not billing */}
      <div style={{ margin: '26px 24px 0', padding: '13px 16px', background: T.cardWarm, borderRadius: 13, border: dHair }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <span style={{ width: 14, height: 14, borderRadius: 999, background: T.gold, display: 'inline-block' }}/><span style={{ fontFamily: T.serif, fontSize: 15, color: T.ink, fontWeight: 500 }}>Vesper · member</span>
        </div>
        <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.mute, margin: '6px 0 0' }}>Your identity here — there’s no plan or payment today.</p>
      </div>
      <div style={{ margin: '24px 24px 0' }}>
        {[['Download my data', T.inkSoft], ['Sign out', T.inkSoft], ['Delete account', '#A04030']].map(([k, c]) => (
          <div key={k} style={{ padding: '13px 0', borderTop: dHair }}>
            <span style={{ fontFamily: T.serif, fontSize: 15, color: c }}>{k}</span>
          </div>
        ))}
      </div>
    </DFrame>
  );
}

Object.assign(window, { DetailHead, DFrame, Learned, Toggle, DTravelIdentity, DCompanions, DTaste, DPrivacy, DNotifications, DAccount });
