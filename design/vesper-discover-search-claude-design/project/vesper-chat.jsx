// Two Vesper chat thread layouts.
//   1 · Editorial Scroll  — Vesper as full-width serif prose, no bubble.
//                            User as small dark serif pill, right-aligned.
//                            Tools render as inline structured cards.
//   2 · Document Edit     — chat treated as side-notes; Vesper's current
//                            draft IS the document, and the conversation
//                            sits as margin annotations.

// ─── 1 · EDITORIAL SCROLL ───────────────────────────────────────
function VesperChatEditorial() {
  return (
    <Phone bg={T.bg}>
      {/* Header */}
      <div style={{
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        padding: '14px 22px 0',
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 6, color: T.inkSoft }}>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
            <path d="M14 6l-6 6 6 6"/>
          </svg>
          <span style={{ fontSize: 13, color: T.inkSoft, fontWeight: 500 }}>Vesper</span>
        </div>
        <div style={{ textAlign: 'center' }}>
          <div style={{ fontFamily: T.serif, fontSize: 14, color: T.ink, fontWeight: 500, letterSpacing: -0.1, lineHeight: 1 }}>
            Tokyo, in May
          </div>
          <div style={{ fontSize: 9, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 600, marginTop: 2 }}>
            PRIVATE · TRIP-LINKED
          </div>
        </div>
        <svg width="18" height="18" viewBox="0 0 24 24" fill={T.inkSoft}>
          <circle cx="5" cy="12" r="1.5"/><circle cx="12" cy="12" r="1.5"/><circle cx="19" cy="12" r="1.5"/>
        </svg>
      </div>

      {/* Day divider */}
      <div style={{
        margin: '20px 22px 0', display: 'flex', alignItems: 'center', gap: 10,
        color: T.mute, fontStyle: 'italic', fontFamily: T.serif, fontSize: 11,
      }}>
        <span style={{ flex: 1, height: 1, background: T.hairline }}/>
        <span>Yesterday</span>
        <span style={{ flex: 1, height: 1, background: T.hairline }}/>
      </div>

      {/* User pill */}
      <div style={{ padding: '14px 22px 0', display: 'flex', justifyContent: 'flex-end' }}>
        <div style={{ maxWidth: 280, textAlign: 'right' }}>
          <div style={{
            padding: '8px 14px', background: T.ink, color: T.cardWarm,
            borderRadius: 18, fontFamily: T.serif, fontSize: 14, lineHeight: 1.35,
            display: 'inline-block', letterSpacing: -0.05,
          }}>
            Find a ryokan I’d actually want, nights 5–7
          </div>
          <div style={{ fontSize: 9, color: T.muteSoft, letterSpacing: 1.2, marginTop: 4, fontWeight: 600 }}>
            9:59 PM
          </div>
        </div>
      </div>

      {/* Vesper prose */}
      <div style={{ padding: '18px 22px 0' }}>
        <VesperEyebrow/>
        <p style={{
          fontFamily: T.serif, fontSize: 16, color: T.ink, lineHeight: 1.45,
          margin: '10px 0 0', letterSpacing: -0.1,
        }}>
          Three I’d actually book. <em>Yanaka’s Sawanoya</em> is the slowest of the
          set — an old house, mornings on the river. <em>Hatago</em> is the quietest
          alley I could find in Shibuya, and Sukeroku in Asakusa has the kind of
          morning light you keep noticing in your photos.
        </p>

        {/* INLINE STRUCTURED CARD — a tool result rendered as object */}
        <div style={{
          marginTop: 14, padding: 12, background: T.cardWarm, borderRadius: 12,
          border: `0.5px solid ${T.hairline}`,
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
            <VesperMark s={11}/>
            <span style={{ fontSize: 9, color: T.goldDeep, letterSpacing: 1.4, fontWeight: 700 }}>
              FOUND · 3 RYOKAN
            </span>
            <span style={{ marginLeft: 'auto', fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1.2 }}>
              FROM 47 SEARCHED
            </span>
          </div>
          <div style={{ marginTop: 8, display: 'flex', flexDirection: 'column', gap: 6 }}>
            {[
              { n: 'Sawanoya', sub: 'Yanaka · an old house', tag: 'SLOW' },
              { n: 'Hatago',   sub: 'Shibuya · quiet alley', tag: 'QUIET' },
              { n: 'Sukeroku', sub: 'Asakusa · morning light', tag: 'WARM' },
            ].map((r, i) => (
              <div key={i} style={{
                display: 'grid', gridTemplateColumns: '1fr auto auto', gap: 8, alignItems: 'center',
                padding: '8px 10px', background: T.bg, borderRadius: 8,
              }}>
                <div>
                  <div style={{ fontFamily: T.serif, fontSize: 13, color: T.ink, fontWeight: 500, letterSpacing: -0.1, lineHeight: 1 }}>{r.n}</div>
                  <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 11, color: T.mute, marginTop: 2 }}>{r.sub}</div>
                </div>
                <span style={{ padding: '2px 6px', background: 'rgba(176,133,58,0.10)', color: T.goldDeep, fontSize: 8.5, letterSpacing: 1.2, fontWeight: 700, borderRadius: 3 }}>
                  {r.tag}
                </span>
                <span style={{ color: T.muteSoft, fontSize: 11 }}>→</span>
              </div>
            ))}
          </div>
        </div>

        {/* Suggested next */}
        <div style={{ marginTop: 12, display: 'flex', gap: 6, flexWrap: 'wrap' }}>
          {['add to Tokyo trip', 'show me ¥ tier', 'why these', 'something quieter'].map((c, i) => (
            <span key={c} style={{
              padding: '5px 10px', fontFamily: T.serif, fontStyle: 'italic',
              fontSize: 11.5, color: T.inkSoft, background: T.cardWarm,
              borderRadius: 999, border: i === 0 ? `0.8px solid ${TR.ink}` : `0.5px solid ${T.hairline}`,
            }}>{c}</span>
          ))}
        </div>
        <div style={{ fontSize: 9, color: T.muteSoft, letterSpacing: 1.2, marginTop: 8, fontWeight: 600 }}>
          10:01 PM · VESPER
        </div>
      </div>

      {/* Composer */}
      <div style={{ position: 'absolute', bottom: 96, left: 16, right: 16 }}>
        <Composer placeholder="Reply, or pick one above…"/>
      </div>

      <TabBar active="vesper"/>
    </Phone>
  );
}

// ─── 2 · DOCUMENT EDIT ──────────────────────────────────────────
// Vesper's current draft IS the screen. User questions live as margin notes.
function VesperChatDocument() {
  return (
    <Phone bg={T.bg}>
      {/* Header */}
      <div style={{
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        padding: '14px 22px 0',
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 6, color: T.inkSoft }}>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
            <path d="M14 6l-6 6 6 6"/>
          </svg>
          <span style={{ fontSize: 13, color: T.inkSoft, fontWeight: 500 }}>Vesper</span>
        </div>
        <div style={{
          padding: '3px 8px', border: `0.8px solid ${T.gold}`, borderRadius: 2,
          fontSize: 9, color: T.goldDeep, letterSpacing: 1.6, fontWeight: 600,
        }}>DRAFT · v4</div>
        <svg width="18" height="18" viewBox="0 0 24 24" fill={T.inkSoft}>
          <circle cx="5" cy="12" r="1.5"/><circle cx="12" cy="12" r="1.5"/><circle cx="19" cy="12" r="1.5"/>
        </svg>
      </div>

      {/* Document title */}
      <div style={{ padding: '14px 22px 0' }}>
        <VesperEyebrow trailing="EDITING TOGETHER"/>
        <h2 style={{
          fontFamily: T.serif, fontWeight: 500, fontSize: 28, color: T.ink,
          margin: '8px 0 0', letterSpacing: -0.6, lineHeight: 1,
        }}>
          Tokyo, in May — <span style={{ fontStyle: 'italic' }}>a quiet itinerary.</span>
        </h2>
      </div>

      {/* The document body */}
      <div style={{ padding: '16px 22px 0' }}>
        <p style={{ fontFamily: T.serif, fontSize: 14, color: T.inkSoft, margin: 0, lineHeight: 1.5 }}>
          <b style={{ color: T.ink }}>Days 1–2.</b> Land soft. Yanaka, the old house. Sentō in
          the evening. <em>No alarms.</em>
        </p>
        <p style={{ fontFamily: T.serif, fontSize: 14, color: T.inkSoft, margin: '10px 0 0', lineHeight: 1.5 }}>
          <b style={{ color: T.ink }}>Days 3–4.</b> Shimokita morning, Daikanyama afternoon.
          One bookshop. <span style={{
            background: 'rgba(176,133,58,0.16)', padding: '0 2px', borderRadius: 2,
            color: T.goldDeep,
          }}>One dinner alone.</span>
        </p>
        <p style={{ fontFamily: T.serif, fontSize: 14, color: T.inkSoft, margin: '10px 0 0', lineHeight: 1.5 }}>
          <b style={{ color: T.ink }}>Days 5–7.</b> <span style={{
            textDecoration: 'underline', textDecorationColor: TR.ink,
            textUnderlineOffset: 3, color: T.ink,
          }}>Ryokan — to be picked.</span> Mornings by the river, evenings open.
        </p>

        {/* MARGIN NOTE — penciled in the margin, not a card */}
        <div style={{
          marginTop: 16, padding: '4px 0 4px 14px',
          borderLeft: `2px solid ${TR.ink}`,
        }}>
          <p style={{
            margin: 0, fontFamily: T.serif, fontStyle: 'italic',
            fontSize: 14.5, color: T.ink, lineHeight: 1.4, letterSpacing: -0.05,
          }}>
            “can we skip days 3–4 and lean longer in yanaka instead?”
          </p>
          <div style={{
            marginTop: 6, fontSize: 9, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 600,
          }}>
            — YOU · 10:14
          </div>
        </div>

        {/* Vesper's reply — proposing a doc edit */}
        <div style={{
          marginTop: 8, padding: '12px 14px', background: T.cardSoft, borderRadius: 12,
          border: `0.5px solid ${T.hairline}`,
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
            <VesperMark s={11}/>
            <span style={{ fontSize: 9.5, color: T.goldDeep, letterSpacing: 1.4, fontWeight: 700 }}>
              I’LL TRY · 10:15
            </span>
          </div>
          <p style={{ margin: '6px 0 8px', fontFamily: T.serif, fontSize: 13.5, color: T.inkSoft, lineHeight: 1.35, letterSpacing: -0.05 }}>
            I rewrote days 3–4 to stay east. Same total nights, less crossing the
            city.
          </p>
          <div style={{ display: 'flex', gap: 6 }}>
            <span style={{
              padding: '5px 10px', fontSize: 11.5, fontWeight: 600,
              color: T.cardWarm, background: TR.ink, borderRadius: 999,
              letterSpacing: -0.1,
            }}>Keep the change</span>
            <span style={{
              padding: '5px 10px', fontFamily: T.serif, fontStyle: 'italic',
              fontSize: 11.5, color: T.inkSoft,
              borderRadius: 999, border: `0.5px solid ${T.hairline}`,
            }}>show me both</span>
            <span style={{
              padding: '5px 10px', fontFamily: T.serif, fontStyle: 'italic',
              fontSize: 11.5, color: T.mute,
            }}>undo</span>
          </div>
        </div>
      </div>

      {/* Composer */}
      <div style={{ position: 'absolute', bottom: 96, left: 16, right: 16 }}>
        <Composer placeholder="Edit the draft, or ask…"/>
      </div>

      <TabBar active="vesper"/>
    </Phone>
  );
}

Object.assign(window, { VesperChatEditorial, VesperChatDocument });
