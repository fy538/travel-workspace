"""E4 · The place's people. People who do not know each other, reaching one another through a Place and a deliberate act."""
from mp_kit2 import *

def answer(letter, who, standing, when, words):
    return (f'<div style="padding: 12px 0; border-bottom: 1px solid rgba(27,23,20,0.06);">'
            f'<div style="display: flex; align-items: center; gap: 10px;">'
            f'<span style="width: 28px; height: 28px; border-radius: 14px; background: {INK}; color: {CARD}; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; flex: none;">{letter}</span>'
            f'<span style="font-size: 15px; color: {INK};">{who}</span>{tag(standing, GOLDD)}<span class="fn" style="margin-left: auto;">{when}</span></div>'
            f'<div style="{SERIF} font-size: 16px; line-height: 23px; color: {INK}; margin-top: 8px;">{words}</div></div>')

# ── 1 · A question, asked here ──
def asked():
    inner = header('The Harbor Print Room', 'Red Hook &middot; you&rsquo;re here', back=True)
    inner += gut(box(f'<div class="kickm" style="margin-bottom: 6px;">YOU ASKED</div>' + says('Is the side room always this empty?', 18, 25)), top=18)
    inner += gut('<div>'
        + answer('I', 'In&ecirc;s', 'WORKS HERE', 'TUESDAY', 'Weekday mornings, yes. Saturdays after one it&rsquo;s the busiest room we have.')
        + answer('T', 'Theo', 'LIVES NEARBY', 'APRIL', 'It emptied out when the ferry stop moved. It used to be the first room people walked into.')
        + answer('M', 'Maya', 'YOUR FRIEND', 'THURSDAY', 'Empty when I went. Go on a weekday.') + '</div>', top=10)
    inner += gut(says('It&rsquo;s a weekday room. I&rsquo;d bring your parents on a Tuesday.', 17, 24), top=16)
    return phone2(inner, active='Places')

# ── 2 · The resident's side ──
def contributor():
    inner = avatar_for(header('Your notes on places', 'Three, all public', back=True), 'T')
    inner += gut(box(f'<div class="kickm" style="margin-bottom: 6px;">THE HARBOR PRINT ROOM &middot; APRIL</div>'
        + plain('It emptied out when the ferry stop moved. It used to be the first room people walked into.', size=16, lh=23)
        + '<div class="led" style="margin-top: 12px; grid-template-columns: 110px minmax(0,1fr);">'
          '<div class="k">SHOWN AS</div><div>Theo &middot; lives nearby</div>'
          '<div class="k">SEEN BY</div><div>Anyone asking about this room</div>'
          '<div class="k">THIS MONTH</div><div>Part of an answer someone asked for here</div></div>'), top=18)
    inner += gut(plain('From April. Still true?'), top=18)
    inner += gut(actions(btn('Still true'), btn('It&rsquo;s changed', False), door('Take it down', MUTE)), top=10)
    return phone2(inner, active='Life')

# ── 3 · From a perspective to a walk ──
def walk():
    inner = header('The Harbor Print Room', 'From the gallery', back=True)
    inner += gut(dci('InviteCard', 250, view='guest', shape='rounded', kicker='FROM THE GALLERY · OPEN SIGN-UP',
                     title='A walk through the old print shops', note='“Six stops, about ninety minutes, ending back here. Inês is leading it.”', noteBy='THE GALLERY',
                     **{'lines': 'Saturday at 11:00|twelve places;Starts at the front desk|flat, and step-free throughout'},
                     **{'from': 'the gallery'}, stamp='TWELVE PLACES · SEVEN LEFT'), top=18)
    return phone2(inner, active='Places')

def build():
    cols = [
        col(asked(), cap('1', 'A question, asked from inside the place', 'Three attributed answers with different standing, and an honest disagreement.', tags=(EX, PF, tag('PUBLIC, THROUGH THIS PLACE', GOLDD)))),
        col(contributor(), cap('2', 'The resident&rsquo;s side', 'Self-declared standing, an observation that can expire, and one quiet line about what came of it.', tags=(EX, PRIV('THEO')))),
        col(walk(), cap('3', 'From a perspective to a walk', 'The public-to-group ladder. An institution hosts; people opt in; nobody is matched.', tags=(EX, SH('InviteCard')))),
    ]
    nc = review([
        ('MINIMUM CONTEXT', 'None on the asker&rsquo;s side &mdash; this works for someone with no friends on Vesper at all, which is its strategic point. It needs contributor supply at the place, which is the hard part and is unproven.'),
        ('ASKER EFFORT', 'One question, typed where she stands.'),
        ('CONTRIBUTOR EFFORT', 'Two sentences, a standing he chose to state, and an occasional &ldquo;still true?&rdquo; His effort has to be repaid somehow, and frame 2 is the smallest honest version of that.'),
        ('WHY WOULD THEY?', 'The source docs are direct: residents are not &ldquo;unpaid destination content creators.&rdquo; The reciprocal values named are correcting a misconception, preserving a practice, supporting a local institution, and seeing what became of a contribution.'),
        ('AUDIENCE EFFECT', 'Public, but only through this place and this kind of question. No profile is opened, no follow is created, and the asker&rsquo;s reason never reaches a contributor.'),
        ('LOW PARTICIPATION', 'A place with no contributions shows the listing and says nothing about people. It must not show a prompt to be the first.'),
        ('ONE FAILURE', 'A stale observation presented as current. Hence the dates on every answer and the &ldquo;still true?&rdquo; in frame 2.'),
    ], [
        ('BASIC INTERACTION', 'Reviews and Q&amp;A sections already exist on every map product, at enormous scale. Being a nicer review box is not a reason to exist.'),
        ('WHAT IMPROVES, FOR WHOM', 'The asker: a positioned answer to a real question, from people with different standing, with their disagreement intact. The contributor: what they know does some good. Against a review box: standing instead of stars, a question instead of a rating. Whether people experience that as better is unproven, and supply is the hard part.'),
        ('DIFFERENTIATING?', 'Against reviews: standing instead of stars, a question instead of a rating, disagreement kept instead of averaged. Whether people experience that as better is an open empirical question.'),
        ('SYSTEM ADVANTAGE', 'It is the only territory here that gives a person with no friends on the product a social reason to be there, and the only bridge from solo use to other people that involves no matching.'),
        ('REJECTION TEST', 'Reject nearby-stranger discovery, contributor ranking, follower counts, one synthetic &ldquo;local&rdquo; voice, permanent facts without observation dates, and any inbox that lets a stranger reach a contributor.'),
    ], 'defer',
        'Real, large, and correctly sequenced late: the canon places public Place contribution at step 6 of 9, after private and bounded-group trust is proven. Keep it as the horizon the earlier work must not foreclose.',
        'what sustains a resident&rsquo;s contribution over a year &mdash; and is one quiet line about what came of it enough, or the beginning of a usage report?',
        offscreen=['three people, never &ldquo;locals say&rdquo;; disagreement is kept', 'no contributor knows who asked, or why; the parents&rsquo; visit shapes the answer and stays with Nora', 'standing is self-declared, never inferred', 'no view count, rank, badge, or way for a stranger to message a contributor', 'interest first, invitation second: at no step is one stranger proposed to another'],
        extras=('<b>Ruling needed:</b> frame 2&rsquo;s &ldquo;what came of it&rdquo; line sits on an open conflict &mdash; contributor efficacy (prominence brief MP1; &ldquo;returns the outcome to contributors when allowed&rdquo;, 08-21 §5.5) against the ban on viewed, saved and used reports (social experience brief §3B). Drawn count-free and nameless; still the founder&rsquo;s call.',
                '<b>The settled line:</b> canon §12 forbids stranger discovery around live presence; §11 step 6 sequences public Place contribution. Strangers meet through a place and a deliberate act, never through proximity.',
                '<b>Source:</b> attention-traces doc §8.10; 08-21 strategy §2.3, §5.5, §6.12; canon §4 Relay, §9.'))
    return eboard('E4', 'E4 - The people of a place', 'EXPANDING MY WORLD', 'The place&rsquo;s people',
        'A place becomes legible through the plural people who know, work in, live near and pass through it. The payoff for the asker is a positioned answer '
        'to a real question; for the contributor, that what they know did some good. Nobody is matched to anybody. People, standings and the walk are fixtures.',
        cols, nc, 3)

if __name__ == '__main__':
    print(build())
