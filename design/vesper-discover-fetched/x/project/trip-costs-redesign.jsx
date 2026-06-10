// ═══════════════════════════════════════════════════════════════
// COSTS · redesigned — editorial, not a spreadsheet. Money as PEOPLE.
// Leads with the real anxiety: are we settled, who owes whom. Same
// parchment + serif + hairline + ochre-Vesper language as Stay/Transport.
// Reuses DR + SPEEP. Self-contained.
// ═══════════════════════════════════════════════════════════════

const KPC = { T: '#A0703A', A: '#7C8F73', M: '#3D5066' };
function KAv({ who, s = 18, ring = '#EFEAE0' }) {
  return <div style={{ width: s, height: s, borderRadius: 999, background: KPC[who], color: '#fff', fontFamily: DR.serif, fontSize: s * 0.46, fontWeight: 500, display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0, border: `1.5px solid ${ring}` }}>{who}</div>;
}
const ksk = (s = 11, c = DR.gold) => <svg width={s} height={s} viewBox="0 0 24 24" fill={c}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>;
const GREEN = '#3D7050', OX = '#A04030';

function KFrame({ children }) {
  return <Phone bg={DR.paper}><div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>{children}</div><TabBar active="trips"/></Phone>;
}
function KHead({ title }) {
  return (
    <div style={{ padding: '0 24px 16px' }}>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={DR.soft} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
        <span style={{ fontSize: 9.5, letterSpacing: 2, color: DR.mute, fontWeight: 700 }}>COSTS</span>
        <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={DR.soft} strokeWidth="1.6" strokeLinecap="round"><path d="M12 5v14M5 12h14"/></svg>
      </div>
      <h1 style={{ fontFamily: DR.serif, fontSize: 28, fontWeight: 500, letterSpacing: -0.6, lineHeight: 1, color: DR.ink, margin: '14px 0 0' }}>{title}</h1>
    </div>
  );
}

// ─── V1 · BALANCES-FIRST (the page) ───
function CostsV1() {
  const bal = [['T', 'You', '+347', true], ['A', 'Ana', '+126', true], ['M', 'Mara', '−473', false]];
  return (
    <KFrame>
      <KHead title="The split"/>
      {/* calm hero total */}
      <div style={{ textAlign: 'center', padding: '2px 0 18px' }}>
        <div style={{ fontFamily: DR.serif, fontSize: 44, fontWeight: 500, color: DR.ink, letterSpacing: -1.2, lineHeight: 1 }}>€1,420</div>
        <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13, color: DR.mute, marginTop: 6 }}>so far · about €473 each</div>
      </div>
      {/* who's up / down — people, not rows */}
      <div style={{ padding: '0 22px' }}>
        <div style={{ fontSize: 9, letterSpacing: 1.8, color: DR.mute, fontWeight: 700, marginBottom: 4 }}>WHERE EVERYONE STANDS</div>
        {bal.map(([w, name, amt, pos], i) => (
          <div key={w} style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '13px 0', borderTop: i ? `0.5px solid ${DR.hairThin}` : 'none' }}>
            <KAv who={w} s={28} ring={DR.paper}/>
            <div style={{ flex: 1 }}>
              <div style={{ fontFamily: DR.serif, fontSize: 16, fontWeight: 500, color: DR.ink, letterSpacing: -0.2 }}>{name}</div>
              <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 11.5, color: DR.mute, marginTop: 1 }}>{pos ? 'is owed' : 'owes the group'}</div>
            </div>
            <div style={{ fontFamily: DR.serif, fontSize: 18, fontWeight: 500, color: pos ? GREEN : OX, letterSpacing: -0.3 }}>€{amt.replace('+', '').replace('−', '')}</div>
          </div>
        ))}
      </div>
      {/* settle — a gesture */}
      <div style={{ margin: '16px 22px 0', padding: '13px 15px', background: DR.cardSoft, borderRadius: 13, border: `0.8px solid rgba(176,133,58,0.4)` }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 5 }}>{ksk(11)}<span style={{ fontSize: 8.5, letterSpacing: 1.4, color: DR.goldDeep, fontWeight: 700 }}>VESPER</span></div>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14, color: DR.ink, margin: '0 0 11px', lineHeight: 1.4, letterSpacing: -0.1 }}>You’re carrying a bit more because of the ryokan — Mara can square up with one tap.</p>
        <span style={{ display: 'inline-block', padding: '10px 18px', background: DR.blue, color: '#fff', borderRadius: 999, fontSize: 13, fontWeight: 600 }}>Settle up</span>
      </div>
    </KFrame>
  );
}

// ─── V2 · THE LEDGER (editorial expense feed) ───
function CostsV2() {
  const cats = [['Stay', 620, '#C9B79A'], ['Transport', 638, '#9FB0B6'], ['Food', 162, '#C98A57']];
  const tot = 1420;
  const ex = [['Casa do Alecrim', 'T', '€360', 'May 18'], ['Flights, group fare', 'A', '€600', 'May 12'], ['Ramiro dinner', 'T', '€140', 'May 19'], ['Sintra train ×3', 'T', '€38', 'May 21']];
  return (
    <KFrame>
      <KHead title="What’s been spent"/>
      {/* category proportion bar */}
      <div style={{ padding: '0 22px' }}>
        <div style={{ display: 'flex', gap: 2, height: 8, borderRadius: 4, overflow: 'hidden' }}>{cats.map(([n, v, c]) => <span key={n} style={{ width: `${v / tot * 100}%`, background: c }}/>)}</div>
        <div style={{ display: 'flex', gap: 14, marginTop: 10 }}>
          {cats.map(([n, v, c]) => <span key={n} style={{ display: 'flex', alignItems: 'center', gap: 5, fontSize: 10.5, color: DR.soft, fontWeight: 500 }}><span style={{ width: 7, height: 7, borderRadius: 7, background: c }}/>{n} €{v}</span>)}
        </div>
      </div>
      {/* expense feed — hairline rows */}
      <div style={{ padding: '16px 22px 0' }}>
        <div style={{ fontSize: 9, letterSpacing: 1.8, color: DR.mute, fontWeight: 700, marginBottom: 2 }}>EVERY EXPENSE</div>
        {ex.map(([t, who, amt, day], i) => (
          <div key={i} style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '12px 0', borderTop: `0.5px solid ${DR.hairThin}` }}>
            <KAv who={who} s={24} ring={DR.paper}/>
            <div style={{ flex: 1, minWidth: 0 }}>
              <div style={{ fontFamily: DR.serif, fontSize: 15, fontWeight: 500, color: DR.ink, letterSpacing: -0.2, lineHeight: 1.1 }}>{t}</div>
              <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 11.5, color: DR.mute, marginTop: 2 }}>{who === 'T' ? 'you' : who === 'A' ? 'Ana' : 'Mara'} paid · split 3 · {day}</div>
            </div>
            <div style={{ fontFamily: DR.serif, fontSize: 16, fontWeight: 500, color: DR.ink, letterSpacing: -0.2 }}>{amt}</div>
          </div>
        ))}
        <div style={{ borderTop: `0.5px solid ${DR.hairThin}`, marginTop: 0, paddingTop: 13, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <span style={{ fontSize: 12.5, color: DR.blue, fontWeight: 600 }}>+ Add an expense</span>
          <span style={{ fontFamily: DR.serif, fontSize: 13, color: DR.mute, fontStyle: 'italic' }}>€1,420 total</span>
        </div>
      </div>
    </KFrame>
  );
}

// ─── V3 · TAP AN EXPENSE → popover (over dimmed ledger) ───
function CostsV3() {
  return (
    <KFrame>
      <KHead title="What’s been spent"/>
      <div style={{ padding: '0 22px', opacity: 1 }}>
        <div style={{ display: 'flex', gap: 2, height: 8, borderRadius: 4, overflow: 'hidden' }}>{[['#C9B79A', 44], ['#9FB0B6', 45], ['#C98A57', 11]].map(([c, w], i) => <span key={i} style={{ width: `${w}%`, background: c }}/>)}</div>
      </div>
      <div style={{ position: 'absolute', inset: 0, background: 'rgba(20,14,9,0.34)' }}/>
      <div style={{ position: 'absolute', left: 20, right: 20, top: 200 }}>
        <div style={{ background: DR.card, borderRadius: 16, border: `0.5px solid ${DR.hair}`, overflow: 'hidden', boxShadow: '0 22px 48px -16px rgba(0,0,0,0.4)' }}>
          <div style={{ padding: '15px 16px', borderBottom: `0.5px solid ${DR.hairThin}` }}>
            <div style={{ fontFamily: DR.serif, fontSize: 18, fontWeight: 500, color: DR.ink, letterSpacing: -0.3 }}>Casa do Alecrim</div>
            <div style={{ fontFamily: DR.mono, fontSize: 9, color: DR.mute, letterSpacing: 0.5, marginTop: 4 }}>€360 · YOU PAID · MAY 18</div>
          </div>
          {/* split among people */}
          <div style={{ padding: '12px 16px' }}>
            <div style={{ fontSize: 8.5, letterSpacing: 1.4, color: DR.mute, fontWeight: 700, marginBottom: 9 }}>SPLIT THREE WAYS · €120 EACH</div>
            <div style={{ display: 'flex', gap: 14 }}>
              {[['T', 'You'], ['A', 'Ana'], ['M', 'Mara']].map(([w, n]) => (
                <div key={w} style={{ display: 'flex', alignItems: 'center', gap: 6 }}><KAv who={w} s={22} ring={DR.card}/><span style={{ fontFamily: DR.serif, fontSize: 13, color: DR.ink }}>€120</span></div>
              ))}
            </div>
          </div>
          {[['change', 'Ask Vesper to change', DR.goldDeep, true], ['who', 'Change who’s in', DR.soft], ['split', 'Split unevenly', DR.soft]].map(([k, l, c, first]) => (
            <div key={k} style={{ display: 'flex', alignItems: 'center', gap: 10, padding: '12px 16px', borderTop: `0.5px solid ${DR.hairThin}` }}>
              {first && ksk(13)}
              <span style={{ fontFamily: first ? DR.serif : DR.sans, fontStyle: first ? 'italic' : 'normal', fontSize: first ? 14.5 : 13.5, fontWeight: first ? 400 : 500, color: c, letterSpacing: -0.1 }}>{l}</span>
            </div>
          ))}
          <div style={{ padding: '12px 16px', borderTop: `0.5px solid ${DR.hairThin}`, display: 'flex', justifyContent: 'space-between' }}>
            <span style={{ fontSize: 13, color: DR.blue, fontWeight: 600 }}>See receipt →</span>
            <span style={{ fontSize: 13.5, color: OX, fontWeight: 500 }}>Remove</span>
          </div>
        </div>
      </div>
    </KFrame>
  );
}

Object.assign(window, { CostsV1, CostsV2, CostsV3 });
