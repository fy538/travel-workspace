import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
OUT = os.path.join(os.path.dirname(__file__), 'boards'); os.makedirs(OUT, exist_ok=True)

def col(title, blocks):
    out = f'<div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 18px;"><div style="{SERIF} font-weight: 600; font-size: 19px; line-height: 24px;">{title}</div>'
    for k, html in blocks:
        out += f'<div style="display: flex; flex-direction: column; gap: 6px;"><div class="kickm">{k}</div><div style="font-size: 12.5px; line-height: 18px; color: {INK2};">{html}</div></div>'
    return out + '</div>'

def table(rows, cols):
    out = f'<div style="display: grid; grid-template-columns: {cols}; gap: 6px 14px; font-size: 12.5px; line-height: 18px; color: {INK2};">'
    for r in rows:
        for i, c in enumerate(r):
            out += f'<span style="{"font-weight: 600;" if i == 0 else ""} padding: 6px 0; border-top: 1px solid rgba(27,23,20,0.06);">{c}</span>'
    return out + '</div>'

head = (f'<div style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 26px;">{label(GREEN, "PROPOSAL", "HP value pass 09-04 &middot; index, rationale, reuse, decisions")}'
        f'<div class="kick">HOME AND PLACES &middot; DELIVER THE VALUE, NOT THE PROMISE OF WORK &middot; RESPONSE TO 01-HOME-PLACES.MD &middot; 2026-09-04</div>'
        f'<div style="{SERIF} font-weight: 600; font-size: 32px; line-height: 38px; letter-spacing: -0.01em;">What an ordinary open is worth, drawn</div>'
        f'<div style="font-size: 14px; line-height: 21px; color: {MUTE}; max-width: 980px;">Fifteen boards on one fixture week. Every phone is a full scroll; every retained unit has its ledger outside the phone; every transition names its tap, destination, back, re-entry and what persisted. Proposals, not canon: the accepted C1/Places/MP boards are untouched and remain the reference until the founder rules.</div></div>')

active_map = table([
    ('Board', 'Status', 'Replaces / extends'),
    ('HP A1 &middot; Open', 'proposal', 'New state. Extends C1 &middot; Ordinary Available&rsquo;s world to an open Saturday. Adds Theo (fixture).'),
    ('HP A2 &middot; Commitment', 'proposal', 'C1 &middot; Ordinary Available with the reading composed. The crown is reused verbatim.'),
    ('HP A3 &middot; Next open', 'proposal', 'Would supersede C1 &middot; Quiet (ruled) as the Quiet direction. C1 &middot; Quiet (sparse control) stays the negative control.'),
    ('HP A4 &middot; Thin', 'reused', 'C1 &middot; Thin First Week, unchanged.'),
    ('HP B1&ndash;B5', 'proposal', 'Extend Places &middot; 1 World Field beyond the waterfront; B3 applies the Place Path anatomy; B4 reuses MP1&rsquo;s attributed-lane law.'),
    ('HP B6 &middot; Relation', 'proposal', 'Draws the existing scope/candidate-set contract; one amendment named on B5.'),
    ('HP C1&ndash;C4', 'proposal', 'Transitions. Destinations reused from the Chat lane (reader, Keep-as-page), the Entity lane (board 06), the Life lane (kept drawers, People lens).'),
    ('Home &middot; Quiet', 'historical', 'Legacy negative control; not the current Quiet direction (was already so).'),
    ('C3 &middot; The Thread', 'flagged', 'Its &ldquo;check menus&rdquo; offer is the diagnosis&rsquo;s &ldquo;offer to work&rdquo;; the fix is a decision, recorded below, not a redraw here.'),
], '150px 84px minmax(0, 1fr)')

before_after = table([
    ('Diagnosis', 'Before', 'After'),
    ('Quiet leads with administration', 'Read: &ldquo;the week is already in shape&rdquo;; a kept-Sunday crown; past-show and dentist rows; then the market and reading.', 'A3: one-line read, a complete reading first, the week as a seam, the guarantee as one clause in Dana&rsquo;s row, the past show gone.'),
    ('Offers to work instead of results', 'C3 Thread: &ldquo;a 7:45 two-top can also be tried&rdquo;; the Life-to-Home unit offers to check menus.', 'Decision D3: a bounded check that is already authorized is shown as its result; otherwise the unit shows an already-supported contribution or stays silent. No blanket background research.'),
    ('Reading units promise, don&rsquo;t compose', 'Title + duration + one teaser line; the value is behind the door.', 'A1/A2/A3 compose the passage on the page (110&ndash;140 words). The door is optional depth (C1).'),
    ('Europe subordinates New York', 'Returned Saturday carries Sorrento and Aeneas below the fold.', 'The fixture week has no Europe unit; B5 is the &ldquo;less history&rdquo; case without a memory museum.'),
    ('One curated waterfront', 'World Field = Red Hook, three harbor branches, a harbor reading.', 'B1&ndash;B5: an afternoon with no destination, a question, a curiosity, a friend&rsquo;s note, another neighborhood.'),
], '190px minmax(0, 1fr) minmax(0, 1fr)')

reuse = ('<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0 22px;">'
         '<div><div class="kickm" style="margin-bottom: 6px;">REUSED, UNCHANGED</div><div style="font-size: 12.5px; line-height: 18px;">Crown anatomy (kick &middot; serif title &middot; deck &middot; one instrument &middot; CTA &middot; fn) &middot; day band, rhythm bars, tide curve, span comparison, basis strip &middot; in-motion row (44px) &middot; week seam &middot; section header with rule &middot; Door atom &middot; the scope handle &middot; Place Focus and Place Path anatomies &middot; attributed human card (MP1) &middot; the coda &middot; the four-root shell &middot; the Entity lane&rsquo;s page (stub) &middot; the Chat lane&rsquo;s reader and Keep door &middot; Life&rsquo;s kept drawers and People lens.</div></div>'
         '<div><div class="kickm" style="margin-bottom: 6px;">REMOVAL CANDIDATES</div><div style="font-size: 12.5px; line-height: 18px;">&ldquo;Kept for you&rdquo; as a crown on Quiet (fold into the person&rsquo;s row) &middot; past-event rows on Home (&ldquo;went &middot; nothing to settle&rdquo; &rarr; Life) &middot; reading units with a duration but no passage &middot; the browse pair on World Field when the field already has three branches (it stays only where nothing else beats silence) &middot; the &ldquo;offer to check&rdquo; unit shape (D3) &middot; the four-door foot on Place Focus (already ruled, &sect;12.7 i).</div></div></div>')

decisions = table([
    ('#', 'Decision or assumption', 'Owner &middot; status'),
    ('D1', 'The hero plate on a notice stays as a photo slot until a photograph is sourced (ruled 09-02). No unit here depends on a plate.', 'Founder &middot; ruled'),
    ('D2', 'Quiet is <b>value-first</b>: the first thing on a quiet page is a complete return, never the week&rsquo;s administration. Supersedes the ruled Quiet board&rsquo;s order if accepted.', 'Founder &middot; proposed (A3)'),
    ('D3', 'An &ldquo;offer to check&rdquo; is not a unit. Either the check is already authorized and bounded (then show its result with its basis and expiry), or the unit shows something already supported, or it is silent. Applies to C3 Thread&rsquo;s menu line and to any provider-state unit.', 'Home admission compiler (G6/G10) &middot; proposed'),
    ('D4', 'A friend&rsquo;s contribution appears on Home/Places only where it changes the value, and the change is attributed in one line (&ldquo;this moves your window&rdquo;). Decorative quotes do not qualify.', 'MP0/MP2 laws &middot; consistent, no change'),
    ('D5', 'Intention without a named Plan (C3): drawn as the Home/Places consequence of the Components &amp; Plan task&rsquo;s proposal. Not adopted here; storage is theirs.', 'Components &amp; Plan &middot; assumption'),
    ('D6', 'The scope handle may expose a relationship dimension only where a grant or owner record covers a Place in the field (B5).', 'Places scope contract + C&amp;C &middot; proposed amendment'),
    ('D7', 'External reservation is a link on the Place; the field names what needs one and never holds or books (B2, C2). Returning from a provider marks nothing.', 'Contraction direction &middot; consistent'),
    ('D8', 'Reading is complete on Home; the reader is the Chat lane&rsquo;s editorial family with its Keep-as-page door. Home grows no second reader.', 'Chat lane &middot; assumption (their 09-04 pass)'),
    ('D9', 'The entity page is the Entity lane&rsquo;s board 06; Focus and the entity page are not duplicate detail pages &mdash; Focus is the world/affordance/relationship read, the page is the place itself.', 'Entity lane &middot; assumption (their 09-04 pass)'),
], '36px minmax(0, 1fr) 210px')

gaps = ('<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0 22px;">'
        '<div><div class="kickm" style="margin-bottom: 6px;">CONTENT PRODUCTION &middot; NOT A DESIGN JUDGMENT</div><div style="font-size: 12.5px; line-height: 18px;">Composed passages need a real source-to-passage pipeline (a governed excerpt or a Vesper composition with its Source lineage) &mdash; the fixture passages here are invented. World rhythms (market peaks, tide tables, hours) need an owner with freshness. Photographs for plates are still unsourced. Nothing here is user validation.</div></div>'
        '<div><div class="kickm" style="margin-bottom: 6px;">ENGINEERING &middot; WHAT THE BOARDS ASSUME EXISTS</div><div style="font-size: 12.5px; line-height: 18px;">A context handle echoed by map/list/search (landed 09-04 for map). A viewer-relative grant read for one note (C&amp;C axes). Active-seat arbitration so A1&rsquo;s reading and A3&rsquo;s reading do not both appear (HPL-2, open). An expiring &ldquo;retained intention&rdquo; read (C3) &mdash; not a store. Exact-return envelopes for the four transitions. None of these is claimed built.</div></div></div>')

review = table([
    ('Review question', 'Where it is answered'),
    ('What did I get before tapping or contributing again?', 'A1: a decision (9:30) and an understanding (the flood line), both complete. A3: a complete reading.'),
    ('Useful beyond Rome / pasta / waterfront?', 'A market, a coffee route, a dentist, a bookhall, Jackson Heights. No Europe unit in the week.'),
    ('Enjoy or use it without turning it into a project?', 'No Plan is created anywhere in A or B; C3 keeps an option in the person&rsquo;s words and lets it go nowhere.'),
    ('Does a friend change the value rather than decorate it?', 'A1/B4/C4: Theo moves the window; withdrawal reverts it. The change is the attribution.'),
    ('Practical capability without a travel emergency?', 'A2 (a show), B2 (dinner before it), B1 (a walk timed to the tide).'),
    ('Does the opened destination deliver what the surface promised?', 'C1&ndash;C4 draw each destination and its return; the reader continues the composed passage rather than restarting it.'),
], '300px minmax(0, 1fr)')

inner = head + ('<div style="display: flex; gap: 36px; align-items: flex-start;">'
                + col('Active-board map', [('', active_map)])
                + col('Before &rarr; after', [('', before_after)])
                + '</div>'
                + '<div style="display: flex; gap: 36px; align-items: flex-start; margin-top: 30px;">'
                + col('Reuse and removal', [('', reuse)])
                + col('Decision log &middot; cross-project assumptions', [('', decisions)])
                + '</div>'
                + '<div style="display: flex; gap: 36px; align-items: flex-start; margin-top: 30px;">'
                + col('Gaps, separately', [('', gaps)])
                + col('The review bar, answered', [('', review)])
                + '</div>'
                + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">FIXTURE COPY ONLY &middot; ALL WORLD FACTS (TIDES, HOURS, RHYTHMS, TRANSIT) ARE INVENTED &middot; PROPOSALS MARKED SEPARATELY FROM CANON &middot; RENDERED AT PHONE WIDTH; A LARGE-TEXT PASS WAS NOT RUN ON THESE BOARDS AND IS LISTED AS OPEN</div>')

open(os.path.join(OUT, 'HP0Index.dc.html'), 'w').write(HEAD + f'<div style="width: 1560px; min-height: 1980px; background: #F4F0E7; box-sizing: border-box; padding: 26px 32px 30px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">' + inner + '</div>' + TAIL)
print('wrote HP0Index')
