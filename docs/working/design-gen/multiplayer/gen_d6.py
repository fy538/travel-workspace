"""D6 · Me and you. The relationship comes first, not a solo recommendation with a friend added afterwards."""
from mp_kit2 import *
EX = tag('EXPLORATORY', OX, 'rgba(122,46,46,0.10)')
PF = tag('PROPOSED FIXTURE', MUTE, 'rgba(110,104,98,0.10)')
SH = lambda t: tag(t, PLAN, 'rgba(42,56,75,0.10)')
SPARSE = tag('SPARSE CONTEXT', MUTE, 'rgba(110,104,98,0.10)')
RICH = tag('WITH SHARED CONTEXT', UMBER, 'rgba(74,52,40,0.10)')

def chat_head(when):
    return f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">CHAT</span><span class="fn" style="margin-left: auto;">{when}</span></div></div>'
def bubble(t):
    return f'<div style="display: flex; justify-content: flex-end;"><div style="max-width: 300px; background: {UMBER}; color: {CARD}; border-radius: 18px 18px 4px 18px; padding: 12px 14px; font-size: 15px; line-height: 20px;">{t}</div></div>'

# ── 1 · Almost nothing known about him ──
def sparse():
    inner = chat_head('THURSDAY 10:05 PM')
    inner += gut(bubble('what would be good for alex and me on saturday? he&rsquo;s been flat out all week'), top=24)
    inner += gut(says('I&rsquo;d do the botanic garden, then sit down somewhere. There&rsquo;s nothing to book, and you can leave the minute he flags.'), top=18)
    inner += gut(box(f'<div class="kickm" style="margin-bottom: 6px;">SATURDAY AFTERNOON</div>'
        + f'<div style="{SERIF} font-size: 19px; line-height: 26px; color: {INK};">The botanic garden, then the Garden Caf&eacute;</div>'
        + f'<div style="margin-top: 4px;">{quiet("Open until 6:00 · chairs with backs")}</div>'
        + dci('SourceList', 44, items='Y=YOU · “FLAT OUT ALL WEEK”;1=GARDEN LISTING · THU;P=PRIYA · SATURDAY')), top=16)
    inner += gut(plain('That&rsquo;s built on one thing you told me about his week. Alex will know better.', INK2, 14, 20), top=14)
    return phone2(inner, active='Chat')

# ── 2 · With real shared context ──
def rich():
    inner = chat_head('THURSDAY 10:05 PM')
    inner += gut(bubble('what would be good for maya and me on saturday?'), top=24)
    inner += gut(says('I&rsquo;d walk Priya&rsquo;s three stops in Red Hook. The Print Room is Maya&rsquo;s own find, and the walk between them is flat &mdash; she said last month she&rsquo;s trying to walk more.'), top=18)
    inner += gut(box(f'<div class="kickm" style="margin-bottom: 6px;">SATURDAY &middot; YOU AND MAYA</div>'
        + f'<div style="{SERIF} font-size: 19px; line-height: 26px; color: {INK};">Red Hook on foot: the Print Room, the pier, the ferry landing</div>'
        + f'<div style="margin-top: 4px;">{quiet("About ninety minutes · Print Room open 11:00–6:00")}</div>'
        + dci('SourceList', 58, items='M=MAYA · THE PRINT ROOM, THU;P=PRIYA · THREE STOPS, AUG;1=GALLERY LISTING · TUE')), top=16)
    inner += gut(actions(door('Ask Maya what she&rsquo;s up for')), top=10)
    return phone2(inner, active='Chat')

# ── 3 · He wants new, she wants easy ──
def nofit():
    inner = chat_head('THURSDAY 10:11 PM')
    inner += gut(bubble('and if he wants something new and i want something easy?'), top=24)
    inner += gut(says('Those can be the same afternoon. The Third Street Annex is new to both of you, free, and ten minutes on foot from the garden caf&eacute;, so there&rsquo;s a familiar place to land if it&rsquo;s crowded.', 18, 25), top=18)
    inner += gut('<div>'
        + row('Third Street Annex &middot; <span style="color: #6E6862;">new to you both · free · open until 6:00</span>', mark='dot', color=GOLDD)
        + row('The Garden Caf&eacute; &middot; <span style="color: #6E6862;">ten minutes away · you&rsquo;ve both been</span>', mark='hollow', last=True) + '</div>' + prov('LISTINGS &middot; THU'), top=14)
    inner += gut(plain('What it costs you: a train there, and a line on Saturdays after 2:00.', INK2, 14, 20), top=12)
    return phone2(inner, active='Chat')

def inset_entrance():
    body = (N('The same question can start from the person instead of from Chat.')
            + box(person('A', 'Alex', 'Friend · since 2018') + f'<div style="margin-top: 8px;">{actions(door("Find something for the two of us"))}</div>', '12px 14px')
            + N('It opens Chat with Alex already named. No separate &ldquo;me and you&rdquo; destination, and nothing about Alex is filled in for her.'))
    return inset('1 &middot; A PERSON-FIRST WAY IN, FROM LIFE &middot; PEOPLE', body, 'AN ENTRANCE, NOT A SURFACE')

def build():
    cols = [
        col(sparse() + inset_entrance(), cap('1', 'Almost nothing is known about him', 'Built on one sentence the asker just said. Likely fit, stated as likely fit.', tags=(EX, SPARSE, SH('SourceList')))),
        col(rich(), cap('2', 'With real shared context', 'Her own contribution is why the answer is good &mdash; and asking her directly stays optional.', tags=(EX, RICH, PF))),
        col(nofit(), cap('3', 'He wants new, she wants easy', 'Not a contradiction: one low-effort new thing, with its actual cost stated.', tags=(EX,))),
    ]
    n1 = notes('WHAT ARRIVES, AND WHAT IT COSTS', led([
        ('MINIMUM CONTEXT', 'Frame 1 is the day-one case and is deliberately first: one sentence from the asker, a friend with no account. Frame 2 needs months of real contributions and says so.'),
        ('ASKER EFFORT', 'One question in plain language. No preference setup, no profile for the friend, no bilateral interview.'),
        ('FRIEND EFFORT', 'Zero, unless asked. In frame 2 the optional ask costs him one sentence and he may decline without a reason.'),
        ('KNOWN INPUTS', 'What the asker said out loud; contributions friends actually made to this person. Not used and not inferred: his calendar, his mood, his location, any private current need.'),
        ('AUDIENCE EFFECT', 'Nothing is sent by asking. Naming Alex to Vesper tells Alex nothing and grants nothing.'),
        ('LOW PARTICIPATION', 'Frame 1 is the whole low-participation story: the friend never touches the product and the answer is still useful.'),
        ('ONE FAILURE', 'Frame 3. No mutually acceptable option exists, and saying so beats inventing a compromise.'),
    ]), w=600)
    n2 = notes('COMPARED WITH AN ORDINARY APP', led([
        ('BASIC INTERACTION', '&ldquo;What do you fancy?&rdquo; is a capable alternative and often better. The result has to beat that conversation, not replace it opaquely.'),
        ('DIFFERENTIATING?', 'Frame 1: barely &mdash; a general assistant given the same sentence lands somewhere similar. Frame 2: yes &mdash; the answer is Maya&rsquo;s own place, which requires her contribution and the permission attached to it.'),
        ('SYSTEM ADVANTAGE', 'This is the direction where the advantage is most tempting to overclaim. The canvas restricts itself to attributed contributions and refuses inference about either person.'),
        ('REJECTION TEST', 'Reject relationship dashboards, compatibility scores and merged taste profiles. Reject lowest-common-denominator suggestions. Reject explanations so specific they leak a private reason back to the other person.'),
    ]), w=520)
    n3 = notes('VERDICT', verdict('rework',
        'The desire is real and the sparse case works. But frames 1 and 2 are the same interaction at two context levels, and neither is yet distinct from D5 once an answer exists.',
        'is &ldquo;start from the person&rdquo; a different product shape, or just a different opening sentence into the same one?')
        + N('<b>Named omission:</b> group-safe options for more than two people, and the guest path for a friend without an account, '
            'are both in the brief and not drawn. The external path would be <i>conditional</i> in any case, on the same unresolved guest-identity dependency as Social.')
        + N('<b>Decided, not displayed:</b> naming Alex to Vesper tells Alex nothing and grants nothing &middot; no compatibility score, merged taste profile or average of two people &middot; a friend&rsquo;s reason stays hers even when she gives one &middot; likely fit is stated as likely fit, never as his wish.'), w=440)
    return write('D6 - Me and you', board(
        bw(3, (600, 520, 440)), hh('D6', 1900),
        'D6 &middot; BEING TOGETHER &middot; EXPLORATORY',
        'Me and you',
        'I want to see this particular person; help us find something good. The relationship comes first, rather than adding a '
        'friend to a solo recommendation afterwards. Drawn at two context levels, with the case where nothing fits. All fixture.',
        cols, (n1, n2, n3)))

if __name__ == '__main__':
    print(build())
