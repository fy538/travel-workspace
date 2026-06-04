// ─── CHAT CARDS 1–8 ─────────────────────────────────────────────
// Each returns the card OBJECT given ctx ('solo'|'group').
// Solo/group framing (Vesper-on-page vs bubble) is applied by the
// section renderer; these handle privacy softening + group affordances.

// 1 · VENUE / PLACE ──────────────────────────────────────────────
function VenueCard({ ctx = 'solo' }) {
  const group = ctx === 'group';
  return (
    <ChatCard>
      <div style={{ display: 'flex', gap: 0 }}>
        <div style={{ width: 96, flexShrink: 0, background: T.cardSoft }}>
          <PostcardScene scene="tokyo"/>
        </div>
        <div style={{ flex: 1, padding: '12px 14px' }}>
          <CardHead glyph={ChatGlyph.pin(T.ink)} kind="PLACE · YANAKA" mb={8}/>
          <div style={{ fontFamily: T.serif, fontSize: 18, fontWeight: 500, color: T.ink, letterSpacing: -0.3, lineHeight: 1.05 }}>
            Kayaba Coffee
          </div>
          <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.mute, marginTop: 3, lineHeight: 1.3 }}>
            {group
              ? 'a pre-war kissaten on the cemetery corner'
              : 'pre-war kissaten — the morning light you keep noticing'}
          </div>
          <div style={{ marginTop: 10 }}>
            <MetaChips items={group ? ['OPEN ·11', '¥¥', '8 MIN'] : ['OPEN ·11', '¥¥', '8 MIN E']}/>
          </div>
        </div>
      </div>
      <div style={{ padding: '0 14px 13px' }}>
        <ChatActions ctx={ctx}
          primary={group ? 'Add to trip' : 'Save'}
          secondary={group ? ['Directions'] : ['directions', 'more like this']}/>
      </div>
    </ChatCard>
  );
}

// 2 · ITINERARY / DAY PLAN ───────────────────────────────────────
function ItineraryCard({ ctx = 'solo' }) {
  const group = ctx === 'group';
  const stops = [
    { t: '09:30', n: 'Kayaba Coffee', by: 'theo' },
    { t: '11:00', n: 'Yanaka Cemetery walk', by: null },
    { t: '13:00', n: 'Kamachiku · udon', by: 'ana' },
    { t: '16:00', n: 'Nezu shrine, slow', by: null },
  ];
  return (
    <ChatCard>
      <div style={{ padding: '13px 15px 12px' }}>
        <CardHead glyph={ChatGlyph.cal(T.ink)} kind="DAY PLAN · TOKYO" right="DAY 3 OF 8"/>
        <div style={{ fontFamily: T.serif, fontSize: 18, fontWeight: 500, color: T.ink, letterSpacing: -0.3, lineHeight: 1.1, marginBottom: 12 }}>
          A slow day in <span style={{ fontStyle: 'italic' }}>Yanaka.</span>
        </div>
        <div style={{ display: 'flex', flexDirection: 'column' }}>
          {stops.map((s, i) => (
            <div key={i} style={{
              display: 'grid', gridTemplateColumns: '46px 1fr auto', gap: 10, alignItems: 'center',
              padding: '8px 0', borderTop: i ? `0.5px solid ${T.hairThin}` : 'none',
            }}>
              <span style={{ fontFamily: T.mono, fontSize: 9.5, color: T.mute, letterSpacing: 0.5, fontWeight: 600 }}>{s.t}</span>
              <span style={{ fontFamily: T.serif, fontSize: 13.5, color: T.ink, letterSpacing: -0.1, lineHeight: 1.15 }}>{s.n}</span>
              {group && s.by
                ? <Avatar who={s.by} s={18}/>
                : <span style={{ width: 18 }}/>}
            </div>
          ))}
        </div>
        {group && (
          <div style={{ marginTop: 8, fontSize: 10, color: T.muteSoft, fontStyle: 'italic', fontFamily: T.serif }}>
            Theo &amp; Ana each added a stop.
          </div>
        )}
      </div>
      <div style={{ padding: '0 15px 13px' }}>
        <ChatActions ctx={ctx} primary={group ? 'Open shared plan' : 'Open full plan'}
          secondary={group ? ['Suggest a stop'] : ['adjust', 'reflow times']}/>
      </div>
    </ChatCard>
  );
}

// 3 · MAP / ROUTE ────────────────────────────────────────────────
function RouteCard({ ctx = 'solo' }) {
  const group = ctx === 'group';
  return (
    <ChatCard>
      <div style={{ position: 'relative', height: 150, background: T.cardSoft, overflow: 'hidden' }}>
        <svg width="100%" height="100%" viewBox="0 0 360 150" preserveAspectRatio="xMidYMid slice">
          <rect width="360" height="150" fill={T.cardSoft}/>
          {/* faint grid */}
          <path d="M0 50 H360 M0 100 H360 M120 0 V150 M240 0 V150" stroke={T.muteSoft} strokeWidth="0.4" opacity="0.35"/>
          {/* route */}
          <path d="M40 110 Q110 70 170 90 Q240 115 310 50" stroke={T.gold} strokeWidth="1.6" strokeDasharray="2 4" fill="none" strokeLinecap="round"/>
          {[[40,110],[170,90],[310,50]].map(([x,y],i)=>(
            <g key={i}><circle cx={x} cy={y} r="4" fill={i===0?T.ink:i===2?T.gold:T.inkSoft}/></g>
          ))}
        </svg>
        <div style={{ position: 'absolute', top: 10, left: 12 }}>
          <CardHead glyph={ChatGlyph.route(T.ink)} kind="ROUTE · 3 STOPS" mb={0}/>
        </div>
        {/* private pin hidden in group */}
        {!group && (
          <div style={{ position: 'absolute', bottom: 10, right: 12, display: 'flex', alignItems: 'center', gap: 4, fontFamily: T.mono, fontSize: 8.5, color: T.mute, letterSpacing: 1, fontWeight: 600 }}>
            <span style={{ width: 5, height: 5, borderRadius: 5, background: TR.ink }}/> YOUR STAY
          </div>
        )}
      </div>
      <div style={{ padding: '12px 15px 13px' }}>
        <div style={{ fontFamily: T.serif, fontSize: 16, fontWeight: 500, color: T.ink, letterSpacing: -0.3 }}>
          Morning loop, mostly downhill.
        </div>
        <div style={{ marginTop: 8, marginBottom: 11 }}>
          <MetaChips items={['2.4 KM', '34 MIN', 'CAFÉ → SHRINE']}/>
        </div>
        <ChatActions ctx={ctx} primary={group ? 'Open in maps' : 'Walk me through'}
          secondary={group ? ['Save'] : ['reverse', 'add a stop']}/>
      </div>
    </ChatCard>
  );
}

// 4 · COMPARISON ─────────────────────────────────────────────────
function ComparisonCard({ ctx = 'solo' }) {
  const group = ctx === 'group';
  const cols = [
    { n: 'Sawanoya', pick: true,  rows: ['Yanaka', '¥¥', 'old house'] },
    { n: 'Hatago',   pick: false, rows: ['Shibuya', '¥¥', 'quiet alley'] },
    { n: 'Sukeroku', pick: false, rows: ['Asakusa', '¥¥¥', 'morning light'] },
  ];
  const rowLabels = ['AREA', group ? 'TIER' : 'NIGHT', 'FEEL'];
  return (
    <ChatCard>
      <div style={{ padding: '13px 15px 13px' }}>
        <CardHead glyph={ChatGlyph.scale(T.ink)} kind="COMPARING · 3 RYOKAN" right={group ? 'OPEN VOTE' : "VESPER'S PICK ★"}/>
        <div style={{ display: 'grid', gridTemplateColumns: '54px 1fr 1fr 1fr', gap: 0, marginTop: 4 }}>
          <div/>
          {cols.map((c) => (
            <div key={c.n} style={{
              textAlign: 'center', padding: '6px 4px', borderRadius: 8,
              background: c.pick && !group ? 'rgba(176,133,58,0.10)' : 'transparent',
            }}>
              <div style={{ fontFamily: T.serif, fontSize: 13, fontWeight: 500, color: T.ink, letterSpacing: -0.2, lineHeight: 1 }}>{c.n}</div>
              {c.pick && !group && <div style={{ fontSize: 8, color: T.goldDeep, letterSpacing: 1, fontWeight: 700, marginTop: 3 }}>PICK</div>}
              {group && <div style={{ marginTop: 4, fontSize: 9, color: T.muteSoft, fontWeight: 700 }}>{['2','1','0'][cols.indexOf(c)]} ●</div>}
            </div>
          ))}
          {rowLabels.map((lab, ri) => (
            <React.Fragment key={lab}>
              <div style={{ fontSize: 8.5, letterSpacing: 1.2, color: T.muteSoft, fontWeight: 700, padding: '9px 0', borderTop: `0.5px solid ${T.hairThin}`, display: 'flex', alignItems: 'center' }}>{lab}</div>
              {cols.map((c) => (
                <div key={c.n+ri} style={{ textAlign: 'center', fontFamily: T.serif, fontSize: 12, color: T.inkSoft, padding: '9px 2px', borderTop: `0.5px solid ${T.hairThin}` }}>
                  {c.rows[ri]}
                </div>
              ))}
            </React.Fragment>
          ))}
        </div>
        <div style={{ marginTop: 12 }}>
          <ChatActions ctx={ctx} primary={group ? 'Cast your vote' : 'Pick Sawanoya'}
            secondary={group ? ['See all'] : ['why this one', 'see all 3']}/>
        </div>
      </div>
    </ChatCard>
  );
}

// 5 · DECISION / VOTE ────────────────────────────────────────────
function DecisionVoteCard({ ctx = 'solo' }) {
  const group = ctx === 'group';
  const opts = [
    { t: 'Jun 6 – 13', votes: ['tiger','ana'] },
    { t: 'Sep 12 – 19', votes: ['theo'] },
  ];
  return (
    <ChatCard>
      <div style={{ padding: '13px 15px 13px' }}>
        <CardHead glyph={group ? ChatGlyph.vote(T.ink) : null} vesper={!group}
          kind={group ? 'GROUP VOTE · PORTO DATES' : 'A CHOICE · PORTO DATES'}
          right={group ? '3 IN' : null}/>
        <div style={{ fontFamily: T.serif, fontSize: 17, fontWeight: 500, color: T.ink, letterSpacing: -0.3, lineHeight: 1.15, marginBottom: 12 }}>
          {group ? 'Which week works for everyone?' : 'Which week feels right?'}
        </div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 7 }}>
          {opts.map((o, i) => (
            <div key={i} style={{
              padding: '10px 12px', borderRadius: 10, border: `0.5px solid ${T.hairline}`,
              background: i === 0 ? (group ? 'rgba(124,143,115,0.10)' : T.cardSoft) : T.cardWarm,
              display: 'flex', alignItems: 'center', justifyContent: 'space-between',
            }}>
              <span style={{ fontFamily: T.serif, fontSize: 14, color: T.ink, letterSpacing: -0.1 }}>{o.t}</span>
              {group ? (
                <div style={{ display: 'flex', alignItems: 'center', gap: -4 }}>
                  {o.votes.map((v, j) => <span key={j} style={{ marginLeft: j ? -6 : 0 }}><Avatar who={v} s={20}/></span>)}
                </div>
              ) : (
                <span style={{ fontSize: 11, color: i === 0 ? T.goldDeep : T.muteSoft, fontWeight: 600, fontStyle: 'italic', fontFamily: T.serif }}>
                  {i === 0 ? 'Vesper leans here' : ''}
                </span>
              )}
            </div>
          ))}
        </div>
        <div style={{ marginTop: 12 }}>
          <ChatActions ctx={ctx} primary={group ? 'Vote Jun 6' : 'Choose Jun 6'}
            primaryColor={group ? '#7C8F73' : TR.ink}
            secondary={group ? ['Add option'] : ['hold', 'ask Ana']}/>
        </div>
      </div>
    </ChatCard>
  );
}

// 6 · BOOKING PROPOSAL ───────────────────────────────────────────
function BookingProposalCard({ ctx = 'solo' }) {
  const group = ctx === 'group';
  return (
    <ChatCard>
      <div style={{ padding: '13px 15px 13px' }}>
        <CardHead glyph={ChatGlyph.card(T.ink)} kind="PROPOSED BOOKING" right="HOLD 24H"/>
        <div style={{ fontFamily: T.serif, fontSize: 17, fontWeight: 500, color: T.ink, letterSpacing: -0.3, lineHeight: 1.1 }}>
          Sawanoya · <span style={{ fontStyle: 'italic' }}>2 nights</span>
        </div>
        <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.mute, marginTop: 3 }}>
          May 18 – 20 · a quiet room
        </div>
        <div style={{ marginTop: 12, padding: '10px 12px', background: T.bg, borderRadius: 10, border: `0.5px solid ${T.hairline}` }}>
          {[
            ['Room', '2-mat, garden view'],
            [group ? 'Per person' : 'Total', group ? '≈ ¥9,000' : '¥36,000'],
            ['Cancellation', 'free until May 11'],
          ].map(([k, v]) => (
            <div key={k} style={{ display: 'flex', justifyContent: 'space-between', padding: '4px 0', fontSize: 12 }}>
              <span style={{ color: T.mute, fontFamily: T.sans }}>{k}</span>
              <span style={{ color: T.ink, fontFamily: T.serif, fontWeight: 500 }}>{v}</span>
            </div>
          ))}
          {group && (
            <div style={{ marginTop: 6, paddingTop: 6, borderTop: `0.5px solid ${T.hairThin}`, display: 'flex', alignItems: 'center', gap: 6 }}>
              <PrivacyTag>payment stays with you</PrivacyTag>
            </div>
          )}
        </div>
        <div style={{ marginTop: 12 }}>
          <ChatActions ctx={ctx} primary={group ? 'Approve my share' : 'Approve & book'}
            secondary={group ? ['Adjust'] : ['adjust', 'not now']}/>
        </div>
      </div>
    </ChatCard>
  );
}

// 7 · BOOKING CONFIRMATION / RECEIPT ─────────────────────────────
function ReceiptCard({ ctx = 'solo' }) {
  const group = ctx === 'group';
  return (
    <ChatCard tint={T.cardSoft}>
      <div style={{ padding: '13px 15px 13px' }}>
        <CardHead glyph={ChatGlyph.check('#3D7050')} kind="CONFIRMED" right={group ? 'BOOKED BY YOU' : 'RECEIPT'}/>
        <div style={{ fontFamily: T.serif, fontSize: 17, fontWeight: 500, color: T.ink, letterSpacing: -0.3, lineHeight: 1.1 }}>
          Sawanoya — <span style={{ fontStyle: 'italic' }}>you’re in.</span>
        </div>
        <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.mute, marginTop: 3 }}>
          May 18 – 20 · check-in from 15:00
        </div>
        {/* perforation */}
        <div style={{ margin: '12px -15px', borderTop: `1px dashed ${T.muteSoft}`, opacity: 0.5 }}/>
        <div>
          {[
            ['Confirmation', group ? '••••  ·  shared on request' : 'SWY-4827-JP'],
            ['Paid', group ? 'settled' : '¥36,000 · Visa ••42'],
            ['Where', 'Yanaka 2-3-11, Taito'],
          ].map(([k, v]) => (
            <div key={k} style={{ display: 'flex', justifyContent: 'space-between', padding: '4px 0', fontSize: 12 }}>
              <span style={{ color: T.mute, fontFamily: T.sans }}>{k}</span>
              <span style={{ color: group && k !== 'Where' ? T.muteSoft : T.ink, fontFamily: k === 'Confirmation' ? T.mono : T.serif, fontWeight: 500, letterSpacing: k === 'Confirmation' ? 0.5 : 0 }}>{v}</span>
            </div>
          ))}
          {group && <div style={{ marginTop: 6 }}><PrivacyTag>confirmation &amp; payment hidden</PrivacyTag></div>}
        </div>
        <div style={{ marginTop: 12 }}>
          <ChatActions ctx={ctx} primaryColor="#3D7050" primary={group ? 'Add to our calendar' : 'Add to calendar'}
            secondary={group ? ['View'] : ['view', 'forward']}/>
        </div>
      </div>
    </ChatCard>
  );
}

// 8 · CHANGE APPLIED ─────────────────────────────────────────────
function ChangeAppliedCard({ ctx = 'solo' }) {
  const group = ctx === 'group';
  return (
    <ChatCard>
      <div style={{ padding: '12px 15px 12px' }}>
        <CardHead glyph={ChatGlyph.diff(T.ink)} vesper={!group}
          kind={group ? 'VESPER UPDATED THE PLAN' : 'I MADE THE CHANGE'} right="JUST NOW"/>
        <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginTop: 2 }}>
          <span style={{ fontFamily: T.serif, fontSize: 14, color: T.muteSoft, textDecoration: 'line-through', textDecorationThickness: '1px' }}>
            Day 4 · Shibuya
          </span>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke={T.gold} strokeWidth="2" strokeLinecap="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
          <span style={{ fontFamily: T.serif, fontSize: 15, color: T.ink, fontWeight: 500, letterSpacing: -0.2 }}>
            Day 4 · longer in Yanaka
          </span>
        </div>
        <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.mute, marginTop: 6 }}>
          {group ? 'Same nights, less crossing the city.' : 'Kept your nights — just less back-and-forth.'}
        </div>
        <div style={{ marginTop: 11 }}>
          <ChatActions ctx={ctx} primary={group ? 'See plan' : 'Keep it'}
            secondary={group ? ['Undo'] : ['undo', 'show both']}/>
        </div>
      </div>
    </ChatCard>
  );
}

Object.assign(window, {
  VenueCard, ItineraryCard, RouteCard, ComparisonCard, DecisionVoteCard,
  BookingProposalCard, ReceiptCard, ChangeAppliedCard,
});
