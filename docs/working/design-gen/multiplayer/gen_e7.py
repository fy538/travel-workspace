"""E7 · Someone's city, handed to you. Relay at the scale of a life change."""
from mp_kit2 import *

def stop(n, name, cond, note=''):
    nt = f'<div style="font-size: 13px; line-height: 19px; color: {MUTE}; margin-top: 2px;">{note}</div>' if note else ''
    return (f'<div style="display: flex; gap: 10px; align-items: baseline; padding: 9px 0; border-top: 1px solid rgba(27,23,20,0.06);">'
            f'<span style="{MONO} font-size: 10px; font-weight: 700; color: {GOLDD}; width: 14px;">{n}</span>'
            f'<div style="flex: 1;"><div style="font-size: 15px; color: {INK};">{name}</div>'
            f'<div style="{SERIF} font-size: 15px; line-height: 21px; color: {INK2}; margin-top: 2px;">{cond}</div>{nt}</div></div>')

UP = 'the upstairs room is the reason to go. downstairs gets loud'
def pick(on, name, note, when):
    box_ = (f'<span style="width: 18px; height: 18px; border-radius: 5px; border: 1.5px solid {INK if on else GHOST}; background: {INK if on else "transparent"}; flex: none; display: inline-flex; align-items: center; justify-content: center;">'
            + ('<svg width="11" height="11" viewBox="0 0 14 14" fill="none"><path d="M3 7.2l2.6 2.6L11 4.4" stroke="#FBF7EC" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>' if on else '') + '</span>')
    return (f'<div style="display: grid; grid-template-columns: 18px 1fr; column-gap: 12px; align-items: start; padding: 10px 0; border-top: 1px solid rgba(27,23,20,0.06);">{box_}'
            f'<div><div style="font-size: 15px; color: {INK if on else MUTE};">{name}</div><div style="font-size: 14px; line-height: 20px; color: {INK2 if on else MUTE}; margin-top: 2px;">{note}</div>'
            f'<div class="fn" style="color: {ANCHOR}; margin-top: 3px;">{when}</div></div></div>')

# ── 1 · Priya picks from what she already saved ──
def handover():
    inner = avatar_for(bar('FOR NORA', 'DECEMBER'), 'P')
    inner += gut(f'<div class="vdl-field" style="border-radius: 12px; min-height: 48px; align-items: flex-start; padding: 12px 14px;"><span class="vk-t-bodyMd">three years there. start with these, in this order</span></div>', top=16)
    inner += sect('Your saved places in Mexico City &middot; 14', top=22) + gut('<div>'
        + pick(True, 'Lul&uacute;&rsquo;s, Roma Norte', UP, 'YOUR NOTE &middot; 2021')
        + pick(True, 'The Sunday market', 'don&rsquo;t take it seriously before 11', 'YOUR NOTE &middot; 2020')
        + pick(True, 'The park with the bandstand', 'where i went when the city got too much', 'YOUR NOTE &middot; 2022')
        + pick(False, 'Mezcal bar on &Aacute;lvaro Obreg&oacute;n', 'fun once', 'YOUR NOTE &middot; 2019') + '</div>')
    inner += gut(f'<div style="display: flex; align-items: center; gap: 10px;">{chip("TO NORA")}{plain("Three places, with your notes", MUTE, 13, 18)}</div>', top=14)
    inner += gut(actions(btn('Send to Nora'), door('Not yet', MUTE)), top=12)
    return phone2(inner, active='Life')

# ── 2 · Nora gets it, and it's useful today ──
def arrived():
    inner = anchor_row('NEW YORK', 'DECEMBER 12 &middot; 7:15 PM')
    inner += orientation('Rain until morning.', 'Thursday &middot; 41&deg; &middot; you fly on January 6.')
    inner += sect('From Priya') + gut(original(96, author='Priya', meta='7:02 PM · TO YOU', words='three years there. start with these, in this order', door='Reply')
        + '<div style="margin-top: 10px;">'
        + row('Lul&uacute;&rsquo;s, Roma Norte', mark='dot', color=GOLDD) + row('The Sunday market', mark='dot', color=GOLDD) + row('The park with the bandstand', mark='dot', color=GOLDD, last=True) + '</div>')
    inner += gut(actions(door('See them on the map')), top=8)
    return phone2(inner, active='Home')

# ── 3 · In Places, her note sits beside the place ──
def in_places():
    inner = header('Lul&uacute;&rsquo;s', 'Roma Norte &middot; 12 minutes on foot', back=True)
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{plate("room", 130, tag="LUL&Uacute;&rsquo;S &middot; ILLUSTRATION")}</div>', top=16)
    inner += gut(original(96, author='Priya', meta='2021 · TO YOU IN DECEMBER', words=UP), top=16)
    inner += gut(dci('FactPair', 92, tone='plain', a='TONIGHT', av='Open until 11:00', an='LISTING · MON', b='UPSTAIRS', bv='One flight, no elevator', bn='LISTING · MON'), top=14)
    inner += gut(actions(door('Ask Priya'), door('Somewhere quieter nearby', MUTE)), top=8)
    return phone2(inner, active='Places')

# ── 4 · A month on: her note meets a new situation ──
def parents():
    inner = bar('CHAT', 'FEBRUARY 9')
    inner += gut(bubble('would lulu&rsquo;s work for dinner with my parents on saturday?'), top=22)
    inner += gut(says('Upstairs, yes. Priya&rsquo;s whole point was that it&rsquo;s the quiet room. It&rsquo;s one flight up with no elevator, which matters for your dad&rsquo;s knee. They take bookings for upstairs from 6:00.'), top=16)
    inner += gut(dci('SourceList', 58, items='P=PRIYA · HER NOTE, 2021;Y=YOU · YOUR DAD’S KNEE, JANUARY;1=LULÚ’S LISTING · FRI'), top=10)
    inner += gut(actions(door('Call Lul&uacute;&rsquo;s'), door('Somewhere without stairs', MUTE)), top=8)
    return phone2(inner, active='Chat')

# ── 5 · "You were right about upstairs" ──
def told_her():
    inner = bar('TO PRIYA', 'FEBRUARY 15')
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{plate("room", 170, tag="PHOTO &middot; YOURS")}</div>', top=18)
    inner += gut(f'<div style="border-bottom: 1px solid rgba(27,23,20,0.14); padding: 10px 0;">{plain("you were right about upstairs. my mom wants to move in", size=17, lh=24)}</div>', top=14)
    inner += gut(f'<div style="display: grid; grid-template-columns: 44px 1fr; column-gap: 12px; align-items: center;"><div style="border-radius: 8px; overflow: hidden;">{plate("room", 44, tag="")}</div>{plain("About: Lul&uacute;&rsquo;s · her note from 2021", MUTE, 13, 18)}</div>', top=14)
    inner += gut(f'<div style="display: flex; align-items: center; gap: 10px;">{chip("TO PRIYA")}</div>', top=14)
    inner += gut(actions(btn('Send'), door('Not now', MUTE)), top=14)
    return phone2(inner, active='Places')

def build():
    cols = [
        col(handover(), cap('1', 'Priya picks from what she already saved', 'Three ticks and one sentence. Her notes were written years ago for herself; nothing is composed for the occasion.', tags=(EX, PF, PRIV('PRIYA')))),
        col(arrived(), cap('2', 'Nora gets it that evening', 'Addressed to her, so it is on Home. Useful at once, a month before she flies.', tags=(EX, PRIV('NORA')))),
        col(in_places(), cap('3', 'In Places, beside the place', 'Nora opened Places herself; nothing was delivered on arrival. Priya&rsquo;s judgment and today&rsquo;s facts are two separate things on the page.', tags=(EX, SH('FactPair')))),
        col(parents(), cap('4', 'A month on, a different question', 'Useful beyond arrival: her note, Nora&rsquo;s own private need, and the listing are three inputs, and each is named.', tags=(EX, PRIV('NORA'), SH('SourceList')))),
        col(told_her(), cap('5', '&ldquo;You were right about upstairs&rdquo;', 'Nora chooses to say so. The place and the note make Priya easy to find; nothing prompted this and nothing reports it.', tags=(EX,))),
    ]
    nc = review([
        ('MINIMUM CONTEXT', 'One friend who once lived somewhere, and one person going there. No circle, no shared history in the city. The giver needs places she already kept &mdash; otherwise this is an essay, and nobody writes the essay.'),
        ('GIVER EFFORT', 'Three ticks and one sentence, from fourteen places she had already saved with her own notes. If she had saved nothing, this would be an essay, and nobody writes the essay. <b>Guest requirement:</b> Priya needs the app; whether Nora could receive this as a link without one rests on the unresolved guest path.'),
        ('RECEIVER EFFORT', 'None at the time of need. It surfaces on the right Tuesday rather than sitting in a note she has to remember to open.'),
        ('KNOWN INPUTS', 'Priya&rsquo;s chosen places and words, scoped to Nora. Nora&rsquo;s own situation, which adapts them and is never sent back. Listed hours, labelled as unchecked.'),
        ('AUDIENCE EFFECT', 'One to one, until the recipient is done. Frame 3&rsquo;s onward relay is a new act with its own audience, and the original source controls whether her lines may travel and whether she may be named.'),
        ('LOW PARTICIPATION', 'Nora may never go to any of them, and frame 5 may never happen. Priya is told nothing either way. Both are complete. Passing Priya&rsquo;s notes on to Sam would be a separate act that Priya has to allow.'),
        ('ONE FAILURE', '2022 judgment presented as current fact. Every line carries its year, and today&rsquo;s hours are a separate layer that says it has not been checked.'),
    ], [
        ('BASIC INTERACTION', 'A shared map list or a long message does the handover. People do this now, generously, and the results sit unread in a notes app in a city where the phone has no signal.'),
        ('WHAT IMPROVES, FOR WHOM', 'Nora: a friend&rsquo;s conditional judgment, found where and when it helps, and adapted to a need Priya never hears about. Priya: three ticks, not an essay; later, a photo from someone she helped, if Nora feels like it. Against a saved post: the note is attached to the place, and in frame 4 it answers a question the post never anticipated.'),
        ('DIFFERENTIATING?', 'Conditions instead of pins (&ldquo;alone, the first time, on a Tuesday&rdquo;), and arrival at the moment of use. The canon calls this Relay: &ldquo;from Giulia,&rdquo; &ldquo;adapted for this group,&rdquo; &ldquo;hours independently verified&rdquo; kept as legible layers.'),
        ('SYSTEM ADVANTAGE', 'It is the founder&rsquo;s own sentence drawn: &ldquo;making the world feel like it&rsquo;s mine, even at a foreign place &hellip; especially with people.&rdquo; Moving is the highest-need social moment most adults have, and the product&rsquo;s travel roots and local ambitions meet here.'),
        ('REJECTION TEST', 'Reject a public &ldquo;guide&rdquo; with a follower count. Reject crediting or blaming Priya for how Nora&rsquo;s evening went. Reject any report to the giver of what was used. Reject turning someone who once lived somewhere into a permanent local expert.'),
    ], 'retain',
        'Nobody in the repo has drawn this, and it is the most natural large-scale use of a mode the canon already names. It also gives the long-distance friendship something to be about.',
        'will people assemble a handover if it takes ten minutes &mdash; and does the product have to make it take two before anyone does?',
        offscreen=['Priya learns nothing about Nora&rsquo;s flat, her evening, or whether she went, unless Nora tells her', 'her judgment keeps its year; today&rsquo;s hours are a separate sourced line', 'Nora&rsquo;s line never overwrites Priya&rsquo;s', 'Priya&rsquo;s lines travel onward to Sam only if she said they could, and she is named only if she allowed it', 'a handoff that was never used is not a failed one'],
        extras=('<b>Source:</b> canon §4 Relay and Handoff, §9; foundations doc §3.4 (the local best friend: &ldquo;conditional, situated, attributable judgment&rdquo;) and §12. The life-transition framing &mdash; moving, the friend who left, hosting a visitor &mdash; appears in no document; the 08-07 strategy calls hosting a visitor &ldquo;a hypothesis, not a wedge.&rdquo;',
                '<b>Named omission:</b> the reverse case, hosting a friend who visits your city, and the long-distance friendship with nothing to hand over &mdash; two people simply living in different places &mdash; are not drawn.',
                '<b>Dependency:</b> whether a source&rsquo;s lines may be relayed onward, and whether she may be named when they are, are separate grants (&ldquo;may use&rdquo;, &ldquo;may name&rdquo;, &ldquo;may share&rdquo;).'))
    return eboard('E7', 'E7 - Someones city handed to you', 'EXPANDING MY WORLD', 'Someone&rsquo;s city, handed to you',
        'Arriving somewhere new is the moment a person most needs other people and has the fewest. The payoff is a friend&rsquo;s judgment meeting you on the right evening, '
        'in her words, without her ever learning how your week is going. The city, places and years are fixtures.',
        cols, nc, 5)

if __name__ == '__main__':
    print(build())
