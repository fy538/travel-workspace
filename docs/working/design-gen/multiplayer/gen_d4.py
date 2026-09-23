"""D4 · Giving and receiving small acts of help. Participation as care, knowledge, effort or hospitality."""
from mp_kit2 import *
EX = tag('EXPLORATORY', OX, 'rgba(122,46,46,0.10)')
PF = tag('PROPOSED FIXTURE', MUTE, 'rgba(110,104,98,0.10)')
SH = lambda t: tag(t, PLAN, 'rgba(42,56,75,0.10)')

def chat_head(when):
    return f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">CHAT</span><span class="fn" style="margin-left: auto;">{when}</span></div></div>'
def bubble(t):
    return f'<div style="display: flex; justify-content: flex-end;"><div style="max-width: 300px; background: {UMBER}; color: {CARD}; border-radius: 18px 18px 4px 18px; padding: 12px 14px; font-size: 15px; line-height: 20px;">{t}</div></div>'
def recip(letter, name, on=True):
    tick = '<svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M3 7.2l2.6 2.6L11 4.4" stroke="#1B1714" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>' if on else ''
    return (f'<div style="display: grid; grid-template-columns: 28px 1fr 16px; column-gap: 12px; align-items: center; padding: 10px 0; border-bottom: 0.5px solid var(--vk-borderHairline);">'
            f'<span class="vk-t-capsMicro" style="width: 28px; height: 28px; border-radius: 14px; background: #1B1714; color: #FBF7EC; display: flex; align-items: center; justify-content: center; font-weight: 700;">{letter}</span>'
            f'<div class="vk-t-bodyMd" style="color: var(--vk-ink00);">{name}</div>{tick}</div>')

# ── 1 · A bounded offer ──
def offer():
    inner = chat_head('SUNDAY 5:15 PM')
    inner += gut(bubble('made way too much sauce. anyone want some?'), top=24)
    inner += gut(says('Who&rsquo;s it for?'), top=18)
    inner += gut(f'<div class="vdl-sheet" style="border-radius: 18px; padding-bottom: 16px;"><div class="vdl-sheet-handle"></div>'
        '<div class="vdl-sheet-head"><div class="vdl-t-metaLine" style="color: var(--vk-ink60);">YOUR SAUCE</div>'
        '<div class="vdl-t-sectionHeading" style="font-size: 15px; margin-top: 2px;">Offer it to</div></div>'
        '<div style="border-top: 0.5px solid var(--vk-borderHairline);">' + recip('M', 'Maya') + recip('P', 'Priya') + recip('S', 'Sam', False) + '</div>'
        '<div class="vk-t-caption" style="color: var(--vk-ink60); margin-top: 12px;">Maya and Priya &middot; through Tuesday</div>'
        '<div class="vdl-sheet-actions"><span class="vdl-btn primary pill vk-t-labelSemibold" style="color: var(--vk-color-white); width: 100%; box-sizing: border-box;">Offer it</span></div></div>', top=14)
    return phone2(inner, active='Chat')

# ── 2 · Receiving it (Maya's phone) ──
def receive():
    inner = avatar_for(anchor_row('NEW YORK', 'SUNDAY 6:02 PM'), 'M')
    inner += orientation('Dry until nine.', 'Sunday &middot; 58&deg;')
    inner += sect('From Nora') + gut(original(96, author='Nora', meta='JUST NOW · TO YOU AND PRIYA', words='made way too much sauce. anyone want some?')
        + f'<div style="margin-top: 12px;">{actions(btn("Yes please"), btn("Not this time", False))}</div>')
    inner += sect('You and Nora') + gut(
        f'<div style="display: flex; flex-direction: column; gap: 8px;">{bubble("yes please! tomorrow after 6?")}{bubble_in("perfect. buzz 3B")}</div>')
    return phone2(inner, active='Home')

# ── 3 · The bounded request, unanswered ──
def request():
    inner = chat_head('MONDAY 9:10 AM')
    inner += gut(bubble('has anyone taken their parents somewhere nearby that was actually comfortable?'), top=24)
    inner += gut(prov('FRIDAY 9:10 AM &middot; YOU ASKED MAYA AND PRIYA'), top=4)
    inner += gut(box(f'<div style="display: flex; align-items: center; gap: 10px;">{faces("MP", "Asked Friday. No replies yet.")}</div>'
        + f'<div style="margin-top: 10px;">{actions(btn("Answer it for me"), door("Ask again", MUTE), door("Drop it", MUTE))}</div>'), top=14)
    inner += gut(says('I&rsquo;d try the botanic garden caf&eacute;. It has chairs with backs and nobody hurries you.'), top=18)
    inner += gut(prov('GARDEN LISTING &middot; FRI'), top=2)
    return phone2(inner, active='Chat')

def inset_answered():
    body = (N('If Priya had answered, her words arrive in the reader, and Vesper says nothing.') + dci('OriginalReader', 96, density='open', author='Priya', meta='SATURDAY · TO YOU', words='botanic garden cafe. chairs with backs, and you can sit as long as you like'))
    return inset('3 &middot; THE OTHER OUTCOME', body, 'A HUMAN ANSWER REPLACES THE GENERATED ONE; IT IS NOT SUMMARIZED')

def inset_expired():
    body = (N('Tuesday. The sauce is gone.') + dci('Notice', 64, tone='stale', title='Offer ended Tuesday', body='Maya took some on Monday.'))
    return inset('2, LATER &middot; THE OFFER ENDS', body, 'SHARED &middot; Notice tone=stale &middot; IT ENDS BY ITSELF; NOBODY MANAGES IT')

def build():
    cols = [
        col(offer(), cap('1', 'A bounded offer, in her own words', 'Ordinary language in, a chosen audience, an end date. No marketplace listing.', tags=(EX, PF, SH('.vdl-sheet')))),
        col(receive() + inset_expired(), cap('2', 'Receiving it, and finishing', 'Two taps and three messages. Plus what happens when the offer runs out.', tags=(EX, SH('Notice')))),
        col(request() + inset_answered(), cap('3', 'The request, three days on, unanswered', 'The state stays legible because she is relying on it: asked Friday, no replies. She can let Vesper answer, ask again, or drop it.', tags=(EX, PF))),
    ]
    n1 = notes('WHAT ARRIVES, AND WHAT IT COSTS', led([
        ('MINIMUM CONTEXT', 'One friend and nothing else. No history, no circle. This works on day one.'),
        ('GIVER EFFORT', 'One sentence, one audience, one tap. Then a short human exchange she was always going to have.'),
        ('RECEIVER EFFORT', 'One tap to accept, one message to arrange. Declining is a single tap and needs no reason.'),
        ('KNOWN INPUTS', 'Her words; the people she picked; her own expiry. Not used: who is nearby, who likes pasta, who owes whom a favour.'),
        ('AUDIENCE EFFECT', 'Two named people for one offer. It creates no standing &ldquo;helper&rdquo; status and no record of generosity.'),
        ('LOW PARTICIPATION', 'Frame 3 draws silence deliberately. No answer must stay socially ordinary &mdash; no escalation, no reminder sent on the asker&rsquo;s behalf.'),
        ('ONE CHANGE', 'The offer expires. The inset shows it going stale on its own rather than needing management.'),
    ]), w=600)
    n2 = notes('COMPARED WITH AN ORDINARY APP', led([
        ('BASIC INTERACTION', 'A group message already does both the offer and the ask, and does them well. Credit that honestly.'),
        ('DIFFERENTIATING?', 'Thin. The only real candidates are the audience being deliberate rather than the whole group, and the offer ending by itself so nobody has to decline late. Neither is dramatic.'),
        ('SYSTEM ADVANTAGE', 'Not demonstrated. If Priya&rsquo;s answer later improves an afternoon with the parents, that value belongs to D3 and D10, not here.'),
        ('REJECTION TEST', 'Reject a request queue. Reject any hint of a marketplace, reciprocity ledger or helper reputation. Reject volunteering that a particular friend would know &mdash; that turns knowledge into an obligation.'),
    ]), w=520)
    n3 = notes('VERDICT', verdict('merge',
        'Warm and genuinely low-cost, but the interaction is D1&rsquo;s share with an answer attached and an expiry. Explore it as a variant of deliberate sharing rather than a separate shape.',
        'does the bounded expiry actually remove the awkwardness of declining, or does a visible end date create its own small pressure to answer before it runs out?')
        + N('<b>Named omission:</b> hospitality as help &mdash; offering a spare seat, a room, a lift &mdash; is in the desire and is not drawn. '
            'Food examples imply nothing about safety or suitability.')
        + N('<b>Decided, not displayed:</b> Vesper never volunteers that a particular friend would know &middot; silence is ordinary: no reminder, nudge, or &ldquo;unanswered&rdquo; state &middot; no queue, claim tokens or pickup scheduler &middot; an offer ends by itself and creates no standing helper status.'), w=440)
    return write('D4 - Small acts of help', board(
        bw(3, (600, 520, 440)), hh('D4', 1900),
        'D4 &middot; EXPANDING MY WORLD &middot; EXPLORATORY',
        'Giving and receiving small acts of help',
        'I can offer or receive something useful without a big undertaking. Participation counts as care, knowledge, effort '
        'and hospitality, not only as content. One bounded offer, one bounded request, and the ordinary silence. Fixture throughout.',
        cols, (n1, n2, n3)))

if __name__ == '__main__':
    print(build())
