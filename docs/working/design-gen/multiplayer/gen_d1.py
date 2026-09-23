"""D1 · A little window into my friends' lives. Enjoy an ordinary moment without performance or reply debt."""
from mp_kit2 import *

EX = tag('EXPLORATORY', OX, 'rgba(122,46,46,0.10)')
PF = tag('PROPOSED FIXTURE', MUTE, 'rgba(110,104,98,0.10)')
SH = lambda t='SHARED COMPONENT': tag(t, PLAN, 'rgba(42,56,75,0.10)')

CAKE = 'It sank in the middle. It was still the best thing I made all week.'

def who_pills(sel='Friends', opts=('Just me', 'Friends', 'Nora only')):
    return '<div style="display: flex; gap: 7px; flex-wrap: wrap;">' + ''.join(
        f'<span style="height: 30px; border-radius: 15px; background: {INK if o == sel else CARD}; color: {CARD if o == sel else INK}; '
        f'border: 1px solid {"transparent" if o == sel else HAIR}; display: inline-flex; align-items: center; padding: 0 12px; '
        f'font-size: 14px; font-weight: 500;">{o}</span>' for o in opts) + '</div>'

CAKE = 'it sank 😭 still ate half of it'
CAKE = 'third attempt. structurally questionable'
# ── 1 · Maya shares ──
def share():
    inner = bar('SHARE')
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{plate("room", 200, tag="PHOTO &middot; YOURS")}</div>', top=18)
    inner += gut(f'<div style="border-bottom: 1px solid rgba(27,23,20,0.14); padding: 10px 0;">{plain(CAKE, size=17, lh=24)}</div>', top=16)
    inner += gut(f'<div class="kickm" style="margin-bottom: 8px;">TO</div>' + who_pills('Friends') + f'<div style="margin-top: 10px;">{plain("Six people", MUTE, 14, 20)}</div>', top=22)
    inner += gut(actions(btn('Send'), door('Not now', MUTE)), top=24)
    return avatar_for(phone2(inner, active='Home'), 'M')

# ── 2 · Nora's Home: non-spatial shares only; a friend's place lives in Places ──
def home():
    inner = anchor_row('NEW YORK', 'FRIDAY 8:10 AM')
    inner += orientation('Clear until four.', 'Friday &middot; 61&deg; &middot; next on your calendar: Tuesday 9:00.')
    inner += sect('From friends') + gut(
        f'<div style="border-radius: 14px; overflow: hidden; margin-bottom: 14px;">{plate("room", 170, tag="PHOTO &middot; MAYA")}</div>'
        + original(100, author='Maya', meta='LAST NIGHT · TO FRIENDS', words=CAKE, door='Reply'))
    inner += gut(rule(original(90, author='Priya', meta='7:52 AM · TO FRIENDS', words='bread’s out of the oven if anyone’s near', door='Reply')), top=18)
    return phone2(inner, active='Home')

# ── 3 · Opened, and a small reply with the original still in view ──
def opened():
    inner = bar('FROM FRIENDS')
    inner += gut(dci('OriginalReader', 520, density='full', show='reader', author='Maya', audience='Last night · to friends',
                     media='PHOTO · MAYA · ASSET NOT SOURCED', words=CAKE, compose='structurally questionable is generous'), top=16)
    inner += gut(f'<div style="display: flex; align-items: center; gap: 8px;">{chip("TO MAYA")}{plain("Only Maya sees your reply.", MUTE, 13, 18)}</div>', top=10)
    inner += gut(dci('OriginalReader', 48, density='full', show='ask', author='Maya', ask='Ask about the cake'), top=16)
    return phone2(inner, active='Home')

# ── 4 · Maya gets it, with what it was about ──
def maya_gets():
    inner = avatar_for(anchor_row('NEW YORK', 'FRIDAY 8:31 AM'), 'M')
    inner += orientation('Rain by six.', 'Friday &middot; 61&deg;')
    inner += sect('Nora replied') + gut(
        f'<div style="display: grid; grid-template-columns: 56px 1fr; column-gap: 12px; align-items: center; margin-bottom: 12px;">'
        f'<div style="border-radius: 10px; overflow: hidden;">{plate("room", 56, tag="")}</div>{plain(CAKE, MUTE, 14, 20)}</div>'
        + original(90, author='Nora', meta='8:29 AM · TO YOU', words='structurally questionable is generous', door='Reply'))
    inner += gut(rule(original(80, author='Sam', meta='8:12 AM · TO YOU', words='😂🍰')), top=18)
    return phone2(inner, active='Home')

# ── 5 · Sunday ──
def quiet():
    inner = anchor_row('NEW YORK', 'SUNDAY 9:40 AM')
    inner += orientation('Clear until four.', 'Sunday &middot; 58&deg; &middot; the greenmarket is at its quietest before 10:00.')
    inner += sect('Near you this morning') + gut('<div>'
        + row('The greenmarket &middot; <span style="color: #6E6862;">until 2:00</span>', mark='dot', color=GOLDD)
        + row('The canal walk &middot; <span style="color: #6E6862;">twenty minutes, flat</span>', mark='dot', color=GOLDD, last=True) + '</div>' + prov('MARKET LISTING &middot; SAT'))
    inner += sect('From friends this week') + gut('<div>'
        + row('Maya&rsquo;s cake &middot; <span style="color: #6E6862;">Thursday</span>', mark='hollow')
        + row('Priya&rsquo;s bread &middot; <span style="color: #6E6862;">Friday</span>', mark='hollow', last=True) + '</div>')
    return phone2(inner, active='Home')

def inset_noreport():
    body = (N('A reply need not be words. Sam answered with two emoji; a photo or a voice note uses the same field. These are formats of one reply, not separate systems.')
            + N('<b>Dependency, kept off the screen:</b> being allowed to see Maya&rsquo;s photo is not permission for Vesper to analyze it. &ldquo;Ask about the cake&rdquo; is drawn assuming she shared it with that use allowed; otherwise Ask answers from general knowledge only.'))
    return inset('3 AND 4 &middot; OTHER WAYS TO ANSWER', body, 'REPLY IS HUMAN-DIRECTED AND GOES TO MAYA ALONE &middot; ASK GOES TO VESPER AND NOWHERE ELSE')

def build():
    cols = [
        col(share(), cap('1', 'Maya shares an ordinary moment', 'One photograph, one line, an audience, Send. Sharing stays a deliberate act.', tags=(EX, PF))),
        col(home(), cap('2', 'Nora opens Home the next morning', 'Recognizable people and what they actually sent. No essay about what their lives mean.', tags=(EX,))),
        col(opened() + inset_noreport(), cap('3', 'Opened, and a small reply', 'Her photo stays in view while Nora answers. The audience of the reply is stated once, where it matters.', tags=(EX, SH('OriginalReader')))),
        col(maya_gets(), cap('4', 'Maya gets it, with what it was about', 'The reply arrives beside the thing it answers. Sam&rsquo;s is two emoji, and that is a whole reply.', tags=(EX,))),
        col(quiet(), cap('5', 'Sunday: nothing arrived', 'A successful empty state. No count, no streak, no prompt to produce.', tags=(EX,))),
    ]
    n1 = notes('WHAT ARRIVES, AND WHAT IT COSTS', led([
        ('MINIMUM CONTEXT', 'One friend, no shared history, no circle, no setup. This is the portfolio&rsquo;s low-context case.'),
        ('SENDER EFFORT', 'Choose a photograph, write one line, confirm an audience, Send. Four actions, all familiar. Fixture walkthrough estimate, not measured.'),
        ('RECIPIENT EFFORT', 'Open Home. Reading is the whole interaction. Reply and private Ask are both optional.'),
        ('KNOWN INPUTS', 'The photograph and words Maya supplied; the audience she chose. Nothing about her location, her evening, or who else she is with.'),
        ('AUDIENCE EFFECT', 'One share to her friends. It grants nothing beyond itself and expires on her terms, per the existing Social rules.'),
        ('LOW PARTICIPATION', 'No reply is a complete, ordinary outcome. Frame 4 is what the app looks like when nobody does anything, and it is not a failure state.'),
        ('ONE FAILURE', 'If the send does not go out, her words and photograph stay in the composer. Result and retry are Social board 09&rsquo;s Notice, reused.'),
    ]), w=600)
    n2 = notes('COMPARED WITH AN ORDINARY APP', led([
        ('BASIC INTERACTION', 'A group message does this well. The bar here is <b>equal ease</b>, not uniqueness. If the share costs more than a text, the direction has failed on its own terms.'),
        ('DIFFERENTIATING?', 'Not yet, and the canvas does not pretend otherwise. The optional layer in frame 3 is the only candidate, and for a joke about a sunken cake it adds nothing worth the attention.'),
        ('SYSTEM ADVANTAGE', 'Deferred, and honestly out of reach here: Sam&rsquo;s cinema may matter when Nora is next on Court Street, but that payoff belongs to D10 and cannot be claimed by this board.'),
        ('REJECTION TEST', 'Reject a conventional feed with generic AI commentary. Reject a viewer count. Reject anything that makes the plain exchange slower than the group chat it replaces.'),
    ]), w=520)
    n3 = notes('VERDICT', verdict('retain',
        'Keep it as the portfolio&rsquo;s baseline of ordinary receiving &mdash; and hold it to the ease bar, not to a novelty bar.',
        'does a person who receives but never replies stay a real participant over months, or quietly become an audience?')
        + N('<b>Named omission:</b> this board does not draw sharing an existing Chat-supported object, only a direct photograph. '
            'That variant is in the brief and is not yet explored.')
        + N('<b>Decided, not displayed:</b> no reply is ever owed, and the screen never says so &middot; no unread count, streak, or prompt to post &middot; no viewer list, count or &ldquo;seen by&rdquo; for the sender &middot; the optional baking layer is removable and must earn its place &middot; Reply goes to Maya; Ask goes to Vesper and she is never told.'), w=440)
    w = bw(5, (600, 520, 440))
    return write('D1 - A little window into my friends lives', board(
        w, hh('D1', 2000),
        'D1 &middot; FEELING INVOLVED &middot; EXPLORATORY',
        'A little window into my friends&rsquo; lives',
        'I want to know what my friends are experiencing without the performance or the obligation. '
        'The payoff is feeling a little more involved without a full catch-up &mdash; and no debt in either direction. '
        'Every person, photograph and world fact on this board is a fixture.',
        cols, (n1, n2, n3)))

if __name__ == '__main__':
    print(build())
