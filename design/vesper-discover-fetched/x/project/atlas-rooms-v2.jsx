// ═══════════════════════════════════════════════════════════════
// ATLAS · THE FOUR ROOMS — v2 (the "after").
// Same paper system as the letter-hero home: Cormorant, mono
// eyebrows, ONE gold accent, hairline rules, riso line-art.
// Fixes: Map → a real Atlantic-coast silhouette (not scattered pins);
// DNA → calm, no rotated floating phrases; Postcards → one container,
// no dashed placeholders / fake ledger; Inbox → quieter chips.
// ═══════════════════════════════════════════════════════════════

// quiet tab row — replaces the filled pill chips
function RoomTabs({ tabs, active = 0 }) {
  return (
    <div style={{ display: 'flex', gap: 18, padding: '16px 22px 0', borderBottom: `0.5px solid ${T.hairThin}`, marginBottom: 2 }}>
      {tabs.map((t, i) => (
        <div key={t} style={{ paddingBottom: 9, position: 'relative' }}>
          <span style={{ fontFamily: T.mono, fontSize: 10, letterSpacing: 1.4, fontWeight: 600, color: i === active ? T.ink : T.muteSoft }}>{t}</span>
          {i === active && <div style={{ position: 'absolute', left: 0, right: 0, bottom: -0.5, height: 1.5, background: T.gold }}/>}
        </div>
      ))}
    </div>
  );
}

// a unified inbox card shell — hairline, matches the home cards
function InboxCard({ children }) {
  return <div style={{ background: T.cardWarm, borderRadius: 14, padding: 15, border: `0.5px solid ${T.hairline}` }}>{children}</div>;
}
const CardFoot = ({ date, action, tone = T.inkSoft }) => (
  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginTop: 11 }}>
    <span style={{ fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1.2 }}>{date}</span>
    <span style={{ fontSize: 10, color: tone, fontWeight: 600, letterSpacing: 1.4 }}>{action}</span>
  </div>
);

// ─── 01 · INBOX (light touch) ───────────────────────────────────
function V3Inbox2() {
  return (
    <Phone bg={T.bg}>
      <ScreenHeader eyebrow="01 · INBOX" title={<>Three things<br/><span style={{ fontStyle: 'italic' }}>found you.</span></>} meta="vesper has been keeping notes"/>
      <RoomTabs tabs={['ALL · 3', 'DRAFTS', 'NOTES', 'PATTERNS']}/>
      <div style={{ padding: '14px 16px 0', display: 'flex', flexDirection: 'column', gap: 10 }}>
        {/* postcard draft */}
        <InboxCard>
          <div style={{ display: 'flex', gap: 13 }}>
            <div style={{ width: 76, height: 96, transform: 'rotate(-3deg)', flexShrink: 0 }}>
              <Postcard scene="lisbon" height="100%" stamp={false}/>
            </div>
            <div style={{ flex: 1, minWidth: 0 }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 7 }}>
                <Eyebrow color={T.goldDeep}>POSTCARD · DRAFT</Eyebrow>
                <span style={{ width: 5, height: 5, borderRadius: 5, background: T.gold }}/>
              </div>
              <div style={{ fontFamily: T.serif, fontSize: 19, color: T.ink, fontWeight: 500, letterSpacing: -0.3, lineHeight: 1.1, marginTop: 6 }}>Lisbon, the slow way</div>
              <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.mute, marginTop: 4, lineHeight: 1.35 }}>six days · Alfama, Ramiro, a fado room nobody told you about</div>
              <CardFoot date="03·14·26" action="ON YOUR DESK →" tone={T.goldDeep}/>
            </div>
          </div>
        </InboxCard>
        {/* note */}
        <InboxCard>
          <Eyebrow>NOTE · IN VESPER’S HAND</Eyebrow>
          <div style={{ fontFamily: T.serif, fontSize: 17, color: T.ink, fontWeight: 500, letterSpacing: -0.3, lineHeight: 1.15, marginTop: 6 }}>A short note about Porto</div>
          <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.mute, lineHeight: 1.45, margin: '8px 0 0' }}>“You walked the Ribeira three times before the bridge. There’s a way you choose streets — Vesper has a theory.”</p>
          <CardFoot date="02·22·26" action="READ →"/>
        </InboxCard>
        {/* pattern */}
        <InboxCard>
          <Eyebrow>PATTERN · A REPETITION</Eyebrow>
          <div style={{ fontFamily: T.serif, fontSize: 17, color: T.ink, fontWeight: 500, letterSpacing: -0.3, lineHeight: 1.15, marginTop: 6 }}>Three places that keep returning</div>
          <div style={{ display: 'flex', gap: 8, marginTop: 10, flexWrap: 'wrap' }}>
            {['the same coffee step', 'one dinner alone', 'rivers at dusk'].map((p, i) => (
              <span key={i} style={{ padding: '4px 10px', fontFamily: T.serif, fontStyle: 'italic', fontSize: 11.5, color: T.inkSoft, background: T.cardSoft, borderRadius: 999, border: `0.5px solid ${T.hairline}` }}>{p}</span>
            ))}
          </div>
          <CardFoot date="02·14·26" action="OPEN →"/>
        </InboxCard>
      </div>
      <div style={{ position: 'absolute', bottom: 96, left: 0, right: 0, textAlign: 'center', fontFamily: T.mono, fontSize: 10, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 600 }}>— 41 OLDER · IN THE ARCHIVE —</div>
      <TabBar active="atlas"/>
    </Phone>
  );
}

// ─── 02 · MAP (B — the real Atlantic coast) ─────────────────────
function V3Map2() {
  const afield = [
    { name: 'Tokyo',   sub: 'planned · May', planned: true },
    { name: 'CDMX',    sub: 'six days' },
    { name: 'Bangkok', sub: 'one trip' },
    { name: 'Paris',   sub: 'one trip' },
    { name: 'Berlin',  sub: 'one trip' },
  ];
  return (
    <Phone bg={T.bg}>
      <ScreenHeader eyebrow="02 · MAP" title={<>The coast you keep <span style={{ fontStyle: 'italic' }}>returning to.</span></>} meta="Portugal · two cities, one shore"/>

      {/* the silhouette — coastline drawn for real; labels live inside the SVG so nothing collides */}
      <div style={{ padding: '16px 16px 0' }}>
        <div style={{ position: 'relative', background: T.cardWarm, borderRadius: 16, overflow: 'hidden', border: `0.5px solid ${T.hairline}`, boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset' }}>
          <svg width="100%" viewBox="0 0 320 300" style={{ display: 'block' }}>
            {/* sea (left) — the faintest planning-blue wash */}
            <rect x="0" y="0" width="320" height="300" fill="rgba(61,80,102,0.045)"/>
            {/* land (right of the coastline) — soft gold riso fill, with a 1px offset echo for the riso feel */}
            <path d="M150 0 C140 46 134 86 138 120 C141 150 120 172 150 196 C168 210 150 232 146 262 C143 288 150 300 149 300 L320 300 L320 0 Z" fill="rgba(176,133,58,0.16)"/>
            <path d="M152 0 C142 46 136 86 140 120 C143 150 122 172 152 196 C170 210 152 232 148 262 C145 288 152 300 151 300" fill="none" stroke="rgba(160,64,48,0.18)" strokeWidth="2.5"/>
            {/* the coastline itself */}
            <path d="M150 0 C140 46 134 86 138 120 C141 150 120 172 150 196 C168 210 150 232 146 262 C143 288 150 300 149 300" fill="none" stroke={T.inkSoft} strokeWidth="1.1"/>
            {/* faint graticule, only over the sea */}
            <path d="M0 80 H150 M0 150 H150 M0 220 H150" stroke={T.muteSoft} strokeWidth="0.4" opacity="0.4"/>
            <path d="M60 0 V300 M110 0 V300" stroke={T.muteSoft} strokeWidth="0.4" opacity="0.3"/>

            {/* the route you took twice (Porto ↔ Lisbon) */}
            <path d="M150 74 C176 110 176 150 158 192" stroke={T.gold} strokeWidth="1.4" strokeDasharray="2 3" fill="none" strokeLinecap="round"/>

            {/* Porto — north */}
            <circle cx="150" cy="74" r="4" fill={T.ink}/>
            <text x="162" y="71" fontFamily="EB Garamond, serif" fontSize="16" fontWeight="600" fill={T.ink}>Porto</text>
            <text x="162" y="85" fontFamily="EB Garamond, serif" fontStyle="italic" fontSize="11.5" fill={T.muteSoft}>twice</text>

            {/* Lisbon — south, on the estuary notch · now */}
            <circle cx="152" cy="196" r="13" fill="rgba(176,133,58,0.18)"/>
            <circle cx="152" cy="196" r="5.5" fill={T.gold}/>
            <text x="168" y="193" fontFamily="EB Garamond, serif" fontSize="17" fontWeight="700" fill={T.ink}>Lisbon</text>
            <text x="168" y="208" fontFamily="JetBrains Mono, monospace" fontSize="8.5" letterSpacing="1.4" fill={T.goldDeep}>NOW · DAY 3</text>

            {/* labels for the geography */}
            <text x="14" y="26" fontFamily="JetBrains Mono, monospace" fontSize="8.5" letterSpacing="2" fill={T.muteSoft}>THE ATLANTIC</text>
            <text x="300" y="290" textAnchor="end" fontFamily="EB Garamond, serif" fontStyle="italic" fontSize="11" fill={T.muteSoft}>N ↑</text>
          </svg>
        </div>
      </div>

      {/* further afield — the trips that don't share this shore, kept honest as a list */}
      <div style={{ padding: '18px 22px 0' }}>
        <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginBottom: 4 }}>
          <Eyebrow>FURTHER AFIELD</Eyebrow>
          <span style={{ fontFamily: T.mono, fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 600 }}>5 · 4 COUNTRIES</span>
        </div>
        {afield.map((p, i) => (
          <div key={p.name} style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '10px 0', borderTop: `0.5px solid ${T.hairThin}` }}>
            {p.planned
              ? <span style={{ width: 8, height: 8, borderRadius: 8, border: `1.2px solid ${T.gold}`, background: T.bg, flexShrink: 0 }}/>
              : <span style={{ width: 5, height: 5, borderRadius: 5, background: T.ink, flexShrink: 0, margin: '0 1.5px' }}/>}
            <span style={{ fontFamily: T.serif, fontSize: 16, fontWeight: 500, color: T.ink, fontStyle: p.planned ? 'italic' : 'normal', letterSpacing: -0.2, flex: 1 }}>{p.name}</span>
            <span style={{ fontFamily: T.serif, fontSize: 12.5, color: T.muteSoft }}>{p.sub}</span>
          </div>
        ))}
      </div>
      <TabBar active="atlas"/>
    </Phone>
  );
}

// ─── 03 · TRAVEL DNA (calm — no floating phrases) ───────────────
function V3DNA2() {
  return (
    <Phone bg={T.bg}>
      <ScreenHeader eyebrow="03 · TRAVEL DNA" title={<>A reading,<br/><span style={{ fontStyle: 'italic' }}>by Vesper.</span></>} meta="from 41 entries · last refined 03·12"/>

      {/* centered fingerprint + a quiet centered stack of traits (no rotation) */}
      <div style={{ padding: '18px 22px 0', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <Marks.DNA size={92}/>
        <div style={{ marginTop: 16, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 3 }}>
          {['Early-morning soul', 'Follows the river', 'Returns before exploring'].map((t) => (
            <span key={t} style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 14.5, color: T.inkSoft, letterSpacing: -0.1 }}>{t}</span>
          ))}
          <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 15, color: T.goldDeep, marginTop: 1 }}>Slow.</span>
        </div>
      </div>

      {/* the reading — the strongest thing, given room */}
      <div style={{ margin: '20px 22px 0', padding: '15px 0', borderTop: `0.5px solid ${T.hairline}`, borderBottom: `0.5px solid ${T.hairline}` }}>
        <p style={{ fontFamily: T.serif, fontSize: 16, color: T.ink, margin: 0, lineHeight: 1.42, letterSpacing: -0.15 }}>“You follow the neighborhood before the landmark, and the river before the museum. You return to one step three times before you find the next.”</p>
        <div style={{ marginTop: 9, fontFamily: T.mono, color: T.muteSoft, fontSize: 9, letterSpacing: 1.8, fontWeight: 600 }}>— VESPER, READING YOU</div>
      </div>

      {/* what Vesper tunes to — taste + identity, folded into DNA */}
      <div style={{ padding: '16px 22px 0' }}>
        <Eyebrow>WHAT VESPER TUNES TO</Eyebrow>
        <div style={{ marginTop: 8, display: 'grid', gridTemplateColumns: '1fr 1fr', columnGap: 16 }}>
          {[['ENERGY', 'Relaxed', '4 trips'], ['BUDGET', 'Considered', '5 trips'], ['SOCIAL', 'Small groups', '3 trips'], ['PLANNING', 'Loose', '4 trips']].map(([k, v, n]) => (
            <div key={k} style={{ padding: '9px 0', borderTop: `0.5px solid ${T.hairThin}` }}>
              <div style={{ fontFamily: T.mono, fontSize: 8, color: T.mute, letterSpacing: 1.2, fontWeight: 600 }}>{k}</div>
              <div style={{ fontFamily: T.serif, fontSize: 15, color: T.ink, fontWeight: 500, letterSpacing: -0.2, marginTop: 2 }}>{v}</div>
              <div style={{ fontFamily: T.serif, fontSize: 10.5, color: T.muteSoft, marginTop: 1 }}>learned · {n}</div>
            </div>
          ))}
        </div>
        <div style={{ marginTop: 12, paddingTop: 11, borderTop: `0.5px solid ${T.hairline}`, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <div>
            <span style={{ fontFamily: T.mono, fontSize: 8, color: T.goldDeep, letterSpacing: 1.2, fontWeight: 700 }}>YOU’VE TOLD VESPER</span>
            <div style={{ fontFamily: T.serif, fontSize: 13.5, color: T.inkSoft, marginTop: 3 }}>Vegetarian · step-free where it matters · EN, PT</div>
          </div>
          <span style={{ fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1.2, fontWeight: 600 }}>EDIT</span>
        </div>
      </div>
      <TabBar active="atlas"/>
    </Phone>
  );
}

// ─── 04 · POSTCARDS (one container, no fake scaffolding) ────────
function V3Postcards2() {
  return (
    <Phone bg={T.bg}>
      <ScreenHeader eyebrow="04 · POSTCARDS" title={<>The <span style={{ fontStyle: 'italic' }}>shelf.</span></>} meta="0 sent · 1 draft on your desk"/>

      {/* the draft on the desk — the one real object, given the hero spot */}
      <div style={{ padding: '16px 22px 0' }}>
        <Eyebrow color={T.goldDeep}>VESPER · ON YOUR DESK</Eyebrow>
        <div style={{ marginTop: 12, display: 'flex', justifyContent: 'center' }}>
          <div style={{ width: 230, transform: 'rotate(-1.6deg)', filter: 'drop-shadow(0 18px 30px rgba(27,23,20,0.16))' }}>
            <Postcard scene="lisbon" height={150} title="Lisbon, the slow way" sub="six days, the slow way" date="03·14·26"/>
          </div>
        </div>
        <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.mute, textAlign: 'center', margin: '16px 22px 0', lineHeight: 1.4 }}>Your first postcard, nearly ready. Keep it, refine it, or not this time.</p>
        <div style={{ display: 'flex', justifyContent: 'center', gap: 10, marginTop: 16 }}>
          <div style={{ padding: '11px 22px', borderRadius: 999, background: T.gold, color: T.cardWarm, fontFamily: T.sans, fontSize: 13, fontWeight: 600 }}>Keep it</div>
          <div style={{ padding: '11px 20px', borderRadius: 999, border: `0.5px solid ${T.hairline}`, color: T.inkSoft, fontFamily: T.sans, fontSize: 13, fontWeight: 500 }}>Refine</div>
        </div>
      </div>

      {/* the shelf to come — one honest line, no dashed boxes */}
      <div style={{ position: 'absolute', bottom: 104, left: 22, right: 22 }}>
        <div style={{ paddingTop: 14, borderTop: `0.5px solid ${T.hairline}`, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <div>
            <div style={{ fontFamily: T.serif, fontSize: 15, color: T.ink, fontWeight: 500, letterSpacing: -0.2 }}>The shelf fills as you go</div>
            <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.mute, marginTop: 2 }}>41 entries waiting to become postcards</div>
          </div>
          <Marks.ArrowR s={15} c={T.goldDeep}/>
        </div>
      </div>
      <TabBar active="atlas"/>
    </Phone>
  );
}

Object.assign(window, { V3Inbox2, V3Map2, V3DNA2, V3Postcards2 });
