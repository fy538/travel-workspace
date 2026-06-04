// ═══════════════════════════════════════════════════════════════
// DISCOVER SEARCH · DIRECTION B — "VESPER INTERPRETS"
// Search = telling Vesper a fuzzy desire. Vesper reads the intent
// (a violet interpretation line), then organises results into
// meaning groups: "I'd start here" (one strong pick) · "Field notes"
// · "Places that match" · and Ask Vesper as the natural overflow.
// This is the direction that most says "Vesper knows how to look."
// ═══════════════════════════════════════════════════════════════

// ── B · EMPTY (prompt-led) ──────────────────────────────────────
function SearchB_Empty() {
  const intents = ['a quiet dinner, just us', 'fado but not touristy', 'where should we stay', 'somewhere good in the rain', 'a long walk with a view'];
  return (
    <Phone bg={T.bg}>
      <div style={{ paddingTop: 8 }}><SearchField query="" placeholder="Tell Vesper what you’re after…" focused/></div>
      <div style={{ padding: '30px 26px 0' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 12 }}>
          <Spark s={15}/>
          <span style={{ fontSize: 10, letterSpacing: 1.8, fontWeight: 700, color: D.vesperDeep }}>ASK IN YOUR OWN WORDS</span>
        </div>
        <h2 style={{ fontFamily: T.serif, fontSize: 25, fontWeight: 500, color: T.ink, letterSpacing: -0.5, lineHeight: 1.18, margin: 0 }}>
          Not what’s nearby — <span style={{ fontStyle: 'italic' }}>what you’re in the mood for.</span>
        </h2>
        <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 14, color: T.mute, lineHeight: 1.5, margin: '10px 0 0' }}>
          I’ll read it the way a friend who knows the city would.
        </p>
      </div>
      <div style={{ padding: '24px 26px 0' }}>
        <SearchGroup>TRY</SearchGroup>
        <div style={{ display: 'flex', flexDirection: 'column' }}>
          {intents.map((t, i) => (
            <div key={t} style={{ display: 'flex', alignItems: 'center', gap: 11, padding: '13px 4px', borderTop: i ? hairT : 'none' }}>
              <span style={{ color: D.vesper, fontSize: 13 }}>“</span>
              <span style={{ flex: 1, fontFamily: T.serif, fontSize: 17, color: T.inkSoft, letterSpacing: -0.2 }}>{t}</span>
              <span style={{ color: T.muteSoft, fontSize: 13 }}>↑</span>
            </div>
          ))}
        </div>
      </div>
    </Phone>
  );
}

// The interpretation line — Vesper restating the intent.
function BInterpret({ read }) {
  return (
    <div style={{ margin: '18px 22px 0', padding: '14px 16px', background: D.vesperSoft, borderRadius: 14, border: `0.5px solid ${D.vesperRule}` }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 7 }}>
        <Spark s={13}/>
        <span style={{ fontSize: 9, letterSpacing: 1.6, fontWeight: 700, color: D.vesperDeep }}>I READ THIS AS</span>
      </div>
      <p style={{ fontFamily: T.serif, fontSize: 16.5, fontStyle: 'italic', color: D.vesperDeep, lineHeight: 1.4, margin: 0, letterSpacing: -0.1 }}>{read}</p>
    </div>
  );
}

// ── B · TYPED (interpreted results) ─────────────────────────────
function SearchB_Typed() {
  return (
    <Phone bg={T.bg}>
      <div style={{ paddingTop: 8 }}><SearchField query="fado but not touristy" focused={false}/></div>
      <BInterpret read="The real thing — a small house where locals still go to listen, not a dinner-and-show."/>
      <div style={{ padding: '20px 22px 0' }}>
        <SearchGroup>I’D START HERE</SearchGroup>
        <div style={{ borderRadius: 16, overflow: 'hidden', border: hair, background: T.card }}>
          <Plate variant="alley" style={{ height: 132 }} dim={0.08}>
            <div style={{ position: 'absolute', top: 11, left: 11 }}><LensChip lens="Insider" onDark/></div>
          </Plate>
          <div style={{ padding: '13px 15px' }}>
            <div style={{ fontFamily: T.serif, fontSize: 19, fontWeight: 500, color: T.ink, letterSpacing: -0.3, lineHeight: 1.1 }}>A Tasca do Chico, late</div>
            <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.mute, lineHeight: 1.4, margin: '6px 0 0' }}>
              No stage, no cover. The singing starts when someone feels like it — usually after eleven.
            </p>
            <div style={{ marginTop: 10, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
              <VesperBy/>
              <span style={{ fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1 }}>ALFAMA · 6 MIN WALK</span>
            </div>
          </div>
        </div>
      </div>
      <div style={{ padding: '20px 22px 0' }}>
        <SearchGroup>FIELD NOTES</SearchGroup>
        <ReadRow title="Why fado isn’t nightlife here" lens="The debate" place="Lisbon"/>
      </div>
      <div style={{ padding: '18px 22px 0' }}>
        <SearchGroup>PLACES THAT MATCH</SearchGroup>
        <VenueRow name="Mesa de Frades" kind="FADO" hook="A tiled former chapel; book the late seating" glyph="tiles"/>
        <div style={{ borderTop: hairT }}><VenueRow name="Sr. Fado" kind="FADO" hook="Family-run; the owners sing" glyph="alley"/></div>
      </div>
      <div style={{ padding: '20px 22px 0' }}>
        <AskVesperRow q="fado but not touristy"/>
      </div>
    </Phone>
  );
}

// ── B · NO RESULTS (Vesper reframes) ────────────────────────────
function SearchB_NoResults() {
  return (
    <Phone bg={T.bg}>
      <div style={{ paddingTop: 8 }}><SearchField query="michelin stars under €20" focused={false}/></div>
      <div style={{ margin: '24px 22px 0', padding: '20px', background: D.vesperSoft, borderRadius: 16, border: `0.5px solid ${D.vesperRule}` }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 10 }}>
          <Spark s={15}/>
          <span style={{ fontSize: 9.5, letterSpacing: 1.6, fontWeight: 700, color: D.vesperDeep }}>HONESTLY</span>
        </div>
        <p style={{ fontFamily: T.serif, fontSize: 18, color: D.vesperDeep, lineHeight: 1.5, margin: 0, letterSpacing: -0.1 }}>
          That exact thing doesn’t really exist in Lisbon — but the <span style={{ fontStyle: 'italic' }}>feeling</span> you’re after does: extraordinary food, almost nothing spent.
        </p>
      </div>
      <div style={{ padding: '20px 22px 0' }}>
        <SearchGroup>WHAT I’D POINT YOU TO INSTEAD</SearchGroup>
        <VenueRow name="O Velho Eurico" kind="TASCA" hook="Chef-run tasca, plates around €9" glyph="alley"/>
        <div style={{ borderTop: hairT }}><VenueRow name="Cervejaria Ramiro" kind="MARISCO" hook="The seafood worth the splurge — still honest" glyph="square"/></div>
      </div>
      <div style={{ padding: '22px 22px 0' }}>
        <AskVesperRow q="cheap but extraordinary"/>
      </div>
    </Phone>
  );
}

// ── B · SELECTED → opens the dossier/venue (continuation) ───────
function SearchB_Selected() {
  return (
    <Phone bg={T.bg}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <Plate variant="alley" style={{ height: 300 }} dim={0.16}>
          <div style={{ position: 'absolute', top: 14, left: 16 }}>{DIcon.back('#fff')}</div>
          <div style={{ position: 'absolute', left: 18, right: 18, bottom: 16 }}>
            <LensChip lens="Insider" onDark/>
            <h1 style={{ fontFamily: T.serif, fontSize: 32, fontWeight: 500, color: '#fff', letterSpacing: -0.6, lineHeight: 1.02, margin: '10px 0 0' }}>A Tasca do Chico, late</h1>
          </div>
        </Plate>
        <div style={{ padding: '18px 22px 0' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 7 }}>
            <FieldEyebrow>VESPER’S THESIS</FieldEyebrow>
          </div>
          <p style={{ fontFamily: T.serif, fontSize: 16.5, color: T.inkSoft, lineHeight: 1.55, margin: '12px 0 0', paddingLeft: 13, borderLeft: `2px solid ${D.vesperRule}` }}>
            You asked for fado without the tourists. This is the room people mean when they say that — you sit close, you order the wine, and you wait.
          </p>
          <p style={{ fontFamily: T.serif, fontSize: 15, color: T.mute, lineHeight: 1.6, margin: '16px 0 0' }}>
            It fills by ten and the first voice comes later. No reservations, so go early for a stool at the back, order the chouriço, and let the night find its own shape…
          </p>
        </div>
        <DossierBar variant="editorial"/>
      </div>
    </Phone>
  );
}

Object.assign(window, { SearchB_Empty, SearchB_Typed, SearchB_NoResults, SearchB_Selected });
