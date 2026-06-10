// ═══════════════════════════════════════════════════════════════
// STAY · block-tap interactions. Four screens:
//   1 Stay popover (tap a booked block) · 2 Avatar move-menu (tap your avatar)
//   3 Place page (tap the name) · 4 Gap/decision flow (tap an unbooked block)
// Reuses DR + StyleRiso + Phone/TabBar + SPEEP/SAv from trip-stay-redesign.
// ═══════════════════════════════════════════════════════════════

function StaySeg({ span, nts, name, area, who, dim }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '64px 1fr', gap: 14, opacity: dim ? 0.45 : 1 }}>
      <div style={{ position: 'relative', textAlign: 'right', paddingRight: 16 }}>
        <div style={{ fontFamily: DR.serif, fontSize: 19, fontWeight: 500, color: DR.ink, letterSpacing: -0.4, lineHeight: 1 }}>{span}</div>
        <div style={{ fontFamily: DR.mono, fontSize: 8, color: DR.faint, letterSpacing: 0.8, fontWeight: 600, marginTop: 4 }}>{nts} NIGHTS</div>
        <span style={{ position: 'absolute', right: -5, top: 4, width: 9, height: 9, borderRadius: 999, background: DR.ink }}/>
      </div>
      <div style={{ position: 'relative', paddingBottom: 22 }}>
        <span style={{ position: 'absolute', left: -16, top: 5, bottom: -5, width: 1, background: DR.hairThin }}/>
        <div style={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', gap: 10 }}>
          <div><div style={{ fontFamily: DR.serif, fontSize: 18, fontWeight: 500, color: DR.ink, letterSpacing: -0.3 }}>{name}</div><div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 12.5, color: DR.mute, marginTop: 3 }}>{area}</div></div>
          <div style={{ display: 'flex' }}>{who.map((w, i) => <span key={w} style={{ marginLeft: i ? -5 : 0 }}><SAv who={w} ring={DR.paper}/></span>)}</div>
        </div>
      </div>
    </div>
  );
}
// Full stay page behind the popover — the tapped block stays lit, rest dims.
function StayCtx() {
  return (
    <div>
      <div style={{ padding: '12px 24px 16px' }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={DR.soft} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
          <span style={{ fontSize: 9.5, letterSpacing: 2, color: DR.mute, fontWeight: 700 }}>STAY · 6 NIGHTS</span>
          <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={DR.soft} strokeWidth="1.6" strokeLinecap="round"><path d="M12 5v14M5 12h14"/></svg>
        </div>
        <h1 style={{ fontFamily: DR.serif, fontSize: 28, fontWeight: 500, letterSpacing: -0.6, lineHeight: 1, color: DR.ink, margin: '14px 0 0' }}>Where you sleep</h1>
      </div>
      <div style={{ padding: '0 22px' }}>
        <StaySeg span="18–22" nts="4" name="Casa do Alecrim" area="Alfama · two rooms" who={['T','A','M']}/>
        <StaySeg span="22–24" nts="2" name="Tivoli" area="Cais · river rooms" who={['T','A','M']} dim/>
      </div>
    </div>
  );
}
const sk2 = (s = 11, c = DR.gold) => <svg width={s} height={s} viewBox="0 0 24 24" fill={c}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>;

// 1 · STAY POPOVER — tap a booked block
function StayTapPopover() {
  const rows = [['change', 'Ask Vesper to change', DR.goldDeep, true], ['swap', 'Swap the hotel · keep dates', DR.soft], ['split', 'Change hotels mid-stay', DR.soft], ['dates', 'Adjust the nights', DR.soft]];
  return (
    <Phone bg={DR.paper}><div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
      <StayCtx/>
      <div style={{ position: 'absolute', inset: 0, background: 'rgba(20,14,9,0.34)' }}/>
      <div style={{ position: 'absolute', left: 20, right: 20, top: 210 }}>
        <div style={{ background: DR.card, borderRadius: 16, border: `0.5px solid ${DR.hair}`, overflow: 'hidden', boxShadow: '0 22px 48px -16px rgba(0,0,0,0.4)' }}>
          <div style={{ padding: '14px 16px', borderBottom: `0.5px solid ${DR.hairThin}` }}>
            <div style={{ fontFamily: DR.serif, fontSize: 18, fontWeight: 500, color: DR.ink, letterSpacing: -0.3 }}>Casa do Alecrim</div>
            <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginTop: 5 }}>
              <div style={{ display: 'flex' }}>{['T','A','M'].map((w,i)=><span key={w} style={{ marginLeft: i?-5:0 }}><SAv who={w} s={17} ring={DR.card}/></span>)}</div>
              <span style={{ fontFamily: DR.mono, fontSize: 9, color: DR.mute, letterSpacing: 0.5 }}>MAY 18–22 · €180/NT · ALL THREE</span>
            </div>
          </div>
          {rows.map(([k, l, c, first]) => (
            <div key={k} style={{ display: 'flex', alignItems: 'center', gap: 10, padding: '12px 16px', borderTop: first ? 'none' : `0.5px solid ${DR.hairThin}` }}>
              {first && sk2(13)}
              <span style={{ fontFamily: first ? DR.serif : DR.sans, fontStyle: first ? 'italic' : 'normal', fontSize: first ? 14.5 : 13.5, fontWeight: first ? 400 : 500, color: c, letterSpacing: -0.1 }}>{l}</span>
            </div>
          ))}
          <div style={{ padding: '12px 16px', borderTop: `0.5px solid ${DR.hairThin}`, display: 'flex', justifyContent: 'space-between' }}>
            <span style={{ fontSize: 13, color: DR.blue, fontWeight: 600 }}>See the room →</span>
            <span style={{ fontSize: 13.5, color: '#A04030', fontWeight: 500 }}>Leave this stay</span>
          </div>
        </div>
      </div>
    </div><TabBar active="trips"/></Phone>
  );
}

// 2 · AVATAR MOVE-MENU — tap your own avatar on a stay
function StayTapAvatar() {
  return (
    <Phone bg={DR.paper}><div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
      <StayCtx/>
      <div style={{ position: 'absolute', inset: 0, top: 100, background: 'rgba(20,14,9,0.28)' }}/>
      {/* highlighted avatar */}
      <div style={{ position: 'absolute', right: 30, top: 150 }}><div style={{ boxShadow: '0 0 0 3px rgba(176,133,58,0.6)', borderRadius: 999 }}><SAv who={'M'} s={28} ring={DR.paper}/></div></div>
      <div style={{ position: 'absolute', left: 60, right: 20, top: 196 }}>
        <div style={{ position: 'absolute', top: -7, right: 22, width: 13, height: 13, background: DR.ink, transform: 'rotate(45deg)' }}/>
        <div style={{ position: 'relative', background: DR.ink, borderRadius: 14, padding: 8, boxShadow: '0 18px 40px -14px rgba(0,0,0,0.5)' }}>
          <div style={{ padding: '4px 10px 9px' }}><span style={{ fontSize: 8.5, letterSpacing: 1.4, color: 'rgba(255,255,255,0.55)', fontWeight: 700 }}>MARA · NIGHTS 18–22</span></div>
          {['Move Mara to another stay', 'Give Mara her own place', 'Same as You'].map((l, i) => (
            <div key={l} style={{ padding: '10px 10px', borderTop: i ? '0.5px solid rgba(255,255,255,0.1)' : 'none', fontSize: 13.5, fontWeight: 500, color: i === 1 ? '#E5C16F' : 'rgba(255,255,255,0.9)', letterSpacing: -0.1 }}>{l}</div>
          ))}
        </div>
      </div>
    </div><TabBar active="trips"/></Phone>
  );
}

// 3 · PLACE PAGE — tap the name (the deep, personalized view)
function StayTapPlace() {
  return (
    <Phone bg={DR.ink}><div style={{ position: 'absolute', inset: 0, overflow: 'hidden', background: DR.paper }}>
      <div style={{ position: 'relative', height: 270 }}>
        <StyleRiso w={393} h={270}/>
        <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.34), rgba(20,14,9,0) 42%, rgba(20,14,9,0.72))' }}/>
        <div style={{ position: 'absolute', top: 54, left: 18 }}><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="#fff" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg></div>
        <div style={{ position: 'absolute', left: 20, right: 20, bottom: 16 }}>
          <span style={{ padding: '4px 9px', borderRadius: 999, background: 'rgba(20,14,9,0.5)', backdropFilter: 'blur(6px)', fontSize: 8.5, letterSpacing: 1.2, fontWeight: 700, color: '#fff' }}>YOUR STAY · MAY 18–22</span>
          <h1 style={{ fontFamily: DR.serif, fontSize: 29, fontWeight: 500, letterSpacing: -0.6, lineHeight: 1, color: '#fff', margin: '8px 0 0' }}>Casa do Alecrim</h1>
        </div>
      </div>
      <div style={{ padding: '16px 22px 0' }}>
        <div style={{ paddingLeft: 13, borderLeft: `2px solid ${DR.gold}` }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 5 }}>{sk2(11)}<span style={{ fontSize: 8.5, letterSpacing: 1.4, color: DR.goldDeep, fontWeight: 700 }}>WHY THIS, FOR YOU THREE</span></div>
          <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 15, color: DR.ink, lineHeight: 1.45, margin: 0, letterSpacing: -0.1 }}>Two rooms off one courtyard — you and Ana wanted quiet, Mara wanted her own door. This gives you both.</p>
        </div>
        <div style={{ display: 'flex', gap: 7, marginTop: 14 }}>{['2 ROOMS','€180/NT','FREE CANCEL','ALFAMA'].map(m => <span key={m} style={{ padding: '4px 9px', fontFamily: DR.mono, fontSize: 8.5, color: DR.mute, letterSpacing: 0.8, fontWeight: 600, background: DR.card, border: `0.5px solid ${DR.hair}`, borderRadius: 999 }}>{m}</span>)}</div>
      </div>
      <div style={{ position: 'absolute', bottom: 0, left: 0, right: 0, padding: '12px 18px 20px', background: 'rgba(247,242,231,0.92)', backdropFilter: 'blur(20px)', borderTop: `0.5px solid ${DR.hair}`, display: 'flex', gap: 10, alignItems: 'center' }}>
        <span style={{ display: 'inline-flex', alignItems: 'center', gap: 6, color: DR.ink, fontSize: 13, fontWeight: 600, flex: 1 }}>{sk2(14)} Ask to change</span>
        <span style={{ padding: '10px 16px', background: DR.card, border: `0.5px solid ${DR.hair}`, borderRadius: 999, fontSize: 12.5, fontWeight: 600, color: DR.soft }}>See room</span>
      </div>
    </div><TabBar active="trips"/></Phone>
  );
}

// 4 · GAP DECISION — tap an unbooked block → straight to the choice
function StayTapGap() {
  const opts = [['Casa do Alecrim', 'Alfama · quiet alley', '€180', true], ['Solar dos Mouros', 'Castelo · the view', '€210'], ['Tivoli', 'Cais · river room', '€240']];
  return (
    <Phone bg={DR.paper}><div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
      <div style={{ padding: '12px 22px 16px' }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={DR.soft} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
          <span style={{ fontSize: 9.5, letterSpacing: 2, color: DR.mute, fontWeight: 700 }}>NIGHTS 20–22 · UNBOOKED</span>
          <span style={{ width: 19 }}/>
        </div>
        <h1 style={{ fontFamily: DR.serif, fontSize: 25, fontWeight: 500, letterSpacing: -0.5, lineHeight: 1.05, color: DR.ink, margin: '14px 0 0' }}>Three I’d actually book</h1>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13, color: DR.mute, margin: '6px 0 0' }}>for the two nights you’re missing</p>
      </div>
      <div style={{ padding: '0 18px', display: 'flex', flexDirection: 'column', gap: 10 }}>
        {opts.map(([n, sub, price, pick], i) => (
          <div key={i} style={{ display: 'flex', gap: 12, padding: 11, background: DR.card, borderRadius: 14, border: `0.5px solid ${pick ? 'rgba(176,133,58,0.5)' : DR.hair}` }}>
            <div style={{ width: 58, height: 58, borderRadius: 9, overflow: 'hidden', flexShrink: 0 }}><StyleRiso w={58} h={58}/></div>
            <div style={{ flex: 1, minWidth: 0 }}>
              {pick && <div style={{ display: 'flex', alignItems: 'center', gap: 5, marginBottom: 3 }}>{sk2(10)}<span style={{ fontSize: 8, letterSpacing: 1.2, color: DR.goldDeep, fontWeight: 700 }}>VESPER’S PICK</span></div>}
              <div style={{ fontFamily: DR.serif, fontSize: 16, fontWeight: 500, color: DR.ink, letterSpacing: -0.2, lineHeight: 1.05 }}>{n}</div>
              <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 11.5, color: DR.mute, marginTop: 2 }}>{sub}</div>
            </div>
            <div style={{ textAlign: 'right' }}><div style={{ fontFamily: DR.serif, fontSize: 15, fontWeight: 500, color: DR.ink }}>{price}</div><div style={{ fontFamily: DR.mono, fontSize: 8, color: DR.mute, marginTop: 2 }}>/NT</div></div>
          </div>
        ))}
      </div>
    </div><TabBar active="trips"/></Phone>
  );
}

Object.assign(window, { StayTapPopover, StayTapAvatar, StayTapPlace, StayTapGap });
