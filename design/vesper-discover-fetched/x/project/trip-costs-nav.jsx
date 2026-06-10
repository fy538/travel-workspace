// ═══════════════════════════════════════════════════════════════
// COSTS · navigation we were missing (Splitwise-informed):
//   1 Balances⇄Ledger toggle  2 Settle-up flow (Vesper-simplified)
//   3 Add-expense sheet (amount, payer, split, category, CURRENCY)
//   4 Person detail (tap a person in balances)
// Reuses DR + KAv/ksk/GREEN/OX from trip-costs-redesign.
// ═══════════════════════════════════════════════════════════════

function NFrame({ children }) {
  return <Phone bg={DR.paper}><div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>{children}</div><TabBar active="trips"/></Phone>;
}
function NHead({ title, right }) {
  return (
    <div style={{ padding: '0 24px 14px' }}>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={DR.soft} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
        <span style={{ fontSize: 9.5, letterSpacing: 2, color: DR.mute, fontWeight: 700 }}>COSTS</span>
        <span style={{ width: 19, textAlign: 'right', fontSize: 13, color: right ? DR.blue : 'transparent', fontWeight: 600 }}>{right || '·'}</span>
      </div>
      {title && <h1 style={{ fontFamily: DR.serif, fontSize: 28, fontWeight: 500, letterSpacing: -0.6, lineHeight: 1, color: DR.ink, margin: '14px 0 0' }}>{title}</h1>}
    </div>
  );
}
// the Balances / Ledger toggle (the "switch modes" answer)
function CostToggle({ on = 'bal' }) {
  return (
    <div style={{ margin: '0 24px 14px', display: 'inline-flex', background: 'rgba(27,23,20,0.05)', borderRadius: 999, padding: 3 }}>
      {[['bal', 'Balances'], ['led', 'Ledger']].map(([k, l]) => (
        <span key={k} style={{ padding: '7px 18px', borderRadius: 999, fontSize: 13, fontWeight: on === k ? 600 : 500, color: on === k ? DR.ink : DR.mute, background: on === k ? DR.card : 'transparent', boxShadow: on === k ? '0 1px 3px rgba(0,0,0,0.08)' : 'none', letterSpacing: -0.1 }}>{l}</span>
      ))}
    </div>
  );
}

// ─── 1 · BALANCES with the toggle + currency note ───
function CostsBalances() {
  const bal = [['T', 'You', '347', true], ['A', 'Ana', '126', true], ['M', 'Mara', '473', false]];
  return (
    <NFrame>
      <NHead/>
      <CostToggle on="bal"/>
      <div style={{ textAlign: 'center', padding: '0 0 6px' }}>
        <div style={{ fontFamily: DR.serif, fontSize: 40, fontWeight: 500, color: DR.ink, letterSpacing: -1, lineHeight: 1 }}>€1,420</div>
        <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 12.5, color: DR.mute, marginTop: 5 }}>incl. $120 + £45, converted</div>
      </div>
      <div style={{ padding: '14px 22px 0' }}>
        {bal.map(([w, name, amt, pos], i) => (
          <div key={w} style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '12px 0', borderTop: `0.5px solid ${DR.hairThin}` }}>
            <KAv who={w} s={26} ring={DR.paper}/>
            <div style={{ flex: 1 }}><div style={{ fontFamily: DR.serif, fontSize: 15.5, fontWeight: 500, color: DR.ink, letterSpacing: -0.2 }}>{name}</div><div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 11, color: DR.mute, marginTop: 1 }}>{pos ? 'is owed' : 'owes'} · tap to see</div></div>
            <span style={{ fontFamily: DR.serif, fontSize: 17, fontWeight: 500, color: pos ? GREEN : OX, letterSpacing: -0.3 }}>€{amt}</span>
          </div>
        ))}
      </div>
      <div style={{ position: 'absolute', bottom: 96, left: 22, right: 22, display: 'flex', gap: 8 }}>
        <span style={{ flex: 1, textAlign: 'center', padding: '12px 0', background: DR.blue, color: '#fff', borderRadius: 999, fontSize: 13, fontWeight: 600 }}>Settle up</span>
        <span style={{ padding: '12px 18px', background: DR.card, border: `0.5px solid ${DR.hair}`, borderRadius: 999, fontSize: 13, fontWeight: 600, color: DR.soft }}>+ Add</span>
      </div>
    </NFrame>
  );
}

// ─── 2 · SETTLE-UP FLOW (Vesper-simplified payments) ───
function CostsSettle() {
  const pays = [['M', 'T', 'Mara', 'you', '347'], ['M', 'A', 'Mara', 'Ana', '126']];
  return (
    <NFrame>
      <NHead title="Settle up"/>
      <div style={{ padding: '4px 22px 0' }}>
        <div style={{ paddingLeft: 13, borderLeft: `2px solid ${DR.gold}`, marginBottom: 16 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 4 }}>{ksk(11)}<span style={{ fontSize: 8.5, letterSpacing: 1.4, color: DR.goldDeep, fontWeight: 700 }}>VESPER · SIMPLIFIED</span></div>
          <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14, color: DR.ink, margin: 0, lineHeight: 1.4, letterSpacing: -0.1 }}>I reduced six IOUs to two payments — settle the whole trip in two taps.</p>
        </div>
        {pays.map(([f, t, fn, tn, amt], i) => (
          <div key={i} style={{ display: 'flex', alignItems: 'center', gap: 11, padding: '13px 0', borderTop: `0.5px solid ${DR.hairThin}` }}>
            <KAv who={f} s={26} ring={DR.paper}/>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke={DR.faint} strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
            <KAv who={t} s={26} ring={DR.paper}/>
            <div style={{ flex: 1 }}><div style={{ fontFamily: DR.serif, fontSize: 14.5, color: DR.ink, letterSpacing: -0.1 }}><b style={{ fontWeight: 500 }}>{fn}</b> pays {tn}</div><div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 11, color: DR.mute, marginTop: 1 }}>Venmo · or mark as paid</div></div>
            <span style={{ fontFamily: DR.serif, fontSize: 16, fontWeight: 500, color: DR.ink }}>€{amt}</span>
          </div>
        ))}
        <div style={{ marginTop: 18, padding: '12px 0', textAlign: 'center', background: DR.blue, color: '#fff', borderRadius: 999, fontSize: 13.5, fontWeight: 600 }}>Record both payments</div>
        <div style={{ marginTop: 10, textAlign: 'center', fontFamily: DR.serif, fontStyle: 'italic', fontSize: 12, color: DR.mute }}>or settle one at a time</div>
      </div>
    </NFrame>
  );
}

// ─── 3 · ADD-EXPENSE SHEET (amount · payer · split · category · currency) ───
function CostsAdd() {
  return (
    <NFrame>
      <NHead title="Add an expense" right="Save"/>
      <div style={{ padding: '8px 22px 0' }}>
        {/* amount + currency */}
        <div style={{ textAlign: 'center', padding: '8px 0 20px', display: 'flex', alignItems: 'baseline', justifyContent: 'center', gap: 8 }}>
          <span style={{ fontFamily: DR.serif, fontSize: 46, fontWeight: 500, color: DR.faint, letterSpacing: -1 }}>€0</span>
          <span style={{ padding: '4px 10px', background: DR.card, border: `0.5px solid ${DR.hair}`, borderRadius: 999, fontFamily: DR.mono, fontSize: 11, color: DR.soft, fontWeight: 600 }}>EUR ▾</span>
        </div>
        {[['WHAT', 'Dinner at…', false], ['WHO PAID', 'You', true], ['SPLIT', 'Evenly · 3 ways', true], ['CATEGORY', 'Food', true], ['WHEN', 'Today', true]].map(([k, v, filled]) => (
          <div key={k} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '13px 14px', background: DR.card, borderRadius: 12, border: `0.5px solid ${DR.hair}`, marginBottom: 8 }}>
            <span style={{ fontSize: 8.5, letterSpacing: 1.4, color: DR.mute, fontWeight: 700 }}>{k}</span>
            <span style={{ display: 'flex', alignItems: 'center', gap: 6, fontFamily: DR.serif, fontSize: 15, color: filled ? DR.ink : DR.faint, letterSpacing: -0.1 }}>{v} <span style={{ color: DR.faint, fontSize: 12 }}>▾</span></span>
          </div>
        ))}
      </div>
    </NFrame>
  );
}

// ─── 4 · PERSON DETAIL (tap a person in balances) ───
function CostsPerson() {
  const items = [['Casa do Alecrim', 'owes you', '120'], ['Ramiro dinner', 'owes you', '47'], ['Flights, group fare', 'you owe', '200']];
  return (
    <NFrame>
      <NHead title="Mara"/>
      <div style={{ padding: '0 22px 0' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '4px 0 16px' }}>
          <KAv who="M" s={44} ring={DR.paper}/>
          <div><div style={{ fontFamily: DR.serif, fontSize: 13, fontStyle: 'italic', color: DR.mute }}>owes the group</div><div style={{ fontFamily: DR.serif, fontSize: 26, fontWeight: 500, color: OX, letterSpacing: -0.5, lineHeight: 1 }}>€473</div></div>
        </div>
        <div style={{ fontSize: 9, letterSpacing: 1.8, color: DR.mute, fontWeight: 700, marginBottom: 2 }}>THE BREAKDOWN</div>
        {items.map(([t, dir, amt], i) => (
          <div key={i} style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '12px 0', borderTop: `0.5px solid ${DR.hairThin}` }}>
            <div style={{ flex: 1 }}><div style={{ fontFamily: DR.serif, fontSize: 14.5, fontWeight: 500, color: DR.ink, letterSpacing: -0.1 }}>{t}</div><div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 11, color: DR.mute, marginTop: 1 }}>{dir}</div></div>
            <span style={{ fontFamily: DR.serif, fontSize: 15, fontWeight: 500, color: dir === 'owes you' ? GREEN : OX }}>€{amt}</span>
          </div>
        ))}
        <div style={{ position: 'absolute', bottom: 96, left: 22, right: 22, padding: '12px 0', textAlign: 'center', background: DR.blue, color: '#fff', borderRadius: 999, fontSize: 13, fontWeight: 600 }}>Nudge Mara to settle</div>
      </div>
    </NFrame>
  );
}

Object.assign(window, { CostsBalances, CostsSettle, CostsAdd, CostsPerson });
