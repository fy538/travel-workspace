"""E2 · The group decides. Caucus, one recommendation, a mandate, and a split that reads as abundance."""
from mp_kit2 import *

def vote(name, state):
    mark = {'yes': ('dot', GREEN, 'yes'), 'open': ('hollow', MUTE, 'hasn&rsquo;t said')}[state]
    return line(f'{name} &middot; <span style="color: #6E6862;">{mark[2]}</span>', mark=mark[0], color=mark[1])

# ── 1 · Priya, privately ──
def caucus():
    inner = avatar_for(bar('CHAT', 'TUESDAY 8:40 PM'), 'P')
    inner += gut(says('Before I suggest a place to the four of you: anything I should plan around that you&rsquo;d rather keep out of the group?'), top=22)
    inner += gut(bubble('i can&rsquo;t go over 150 a night. please don&rsquo;t make it a thing'), top=16)
    inner += gut(says('I&rsquo;ll only suggest houses under $150 a night each. That leaves two of the three.'), top=16)
    return phone2(inner, active='Chat')

# ── 2 · The room: a suggestion, an objection, a second house ──
def room():
    inner = header('October upstate', 'Nora, Maya, Priya, Dana', back=True)
    inner += gut(box(f'<div style="{SERIF} font-weight: 600; font-size: 19px; line-height: 25px; color: {MUTE}; text-decoration: line-through;">The blue house on Wiltwyck</div>'
        + f'<div style="margin-top: 8px;">' + original(90, author='Dana', meta='TUESDAY · TO THE FOUR OF YOU', words='no AC and it&rsquo;s going to be 85. i can&rsquo;t sleep in that') + '</div>', '14px 16px'), top=18)
    inner += gut(box(f'<div style="{SERIF} font-weight: 600; font-size: 21px; line-height: 27px;">The yellow house on Abeel</div>'
        + f'<div style="margin-top: 2px;">{quiet("Kingston · two nights · sleeps four in beds · AC")}</div>'
        + f'<div style="margin-top: 12px;">{says("Dana&rsquo;s right about the heat. This one has AC and the same beds. You give up the short walk: it&rsquo;s fifteen minutes to town, not ten.", 16, 23)}</div>'
        + prov('LISTINGS &middot; TUE &nbsp;&middot;&nbsp; FORECAST &middot; TUE')
        + f'<div style="margin-top: 14px;">{faces("DM", "Dana and Maya are in")}</div>'
        + f'<div style="margin-top: 14px;">{actions(btn("I’m in"), btn("Not this one", False))}</div>'), top=12)
    inner += gut(plain('Priya and you haven&rsquo;t answered. You decide Thursday evening.'), top=16)
    return phone2(inner, active='Home')

# ── 3 · Nora: where things actually stand ──
def organizer():
    inner = header('October upstate', 'You started this one', back=True)
    inner += sect('Dinners', top=20) + gut(original(80, author='Maya', meta='TUESDAY · TO THE FOUR OF YOU', words='i&rsquo;ll do dinners. both nights')
        + f'<div style="margin-top: 8px;">{quiet("Hers until Sunday, or until she hands it back.")}</div>')
    inner += sect('Still to do') + gut('<div>'
        + line('The house &middot; <span style="color: #6E6862;">not booked. Whoever books pays a $180 deposit.</span>', mark='hollow', color=OX)
        + line('The train &middot; <span style="color: #6E6862;">Fri 5:40 had seats on Tuesday. Nobody has tickets.</span>', mark='hollow', color=OX)
        + line('Priya &middot; <span style="color: #6E6862;">hasn&rsquo;t answered on the house</span>', mark='hollow', color=OX, last=True) + '</div>' + prov('LISTING AND TIMETABLE &middot; TUE'))
    inner += gut(actions(door('Ask who&rsquo;s booking the house')), top=10)
    return phone2(inner, active='Home')

# ── 4 · Saturday afternoon ──
def split():
    inner = header('Saturday afternoon', 'Kingston', back=True)
    inner += gut(f'<div style="{SERIF} font-weight: 600; font-size: 23px; line-height: 29px;">Two good afternoons. Back together at 6:00.</div>', top=18)
    inner += gut(f'<div style="display: flex; gap: 10px;">'
        + f'<div style="flex: 1;">{box("<div class=kickm style=margin-bottom:6px;>THE BARNS</div>" + says("Antiques, a long drive.", 15, 21) + prov("DANA &middot; TUESDAY") + "<div style=margin-top:10px;>" + faces("DN", "Dana, Nora", 22) + "</div>", "14px")}</div>'
        + f'<div style="flex: 1;">{box("<div class=kickm style=margin-bottom:6px;>THE RIVER</div>" + says("Four flat miles. A swim if it&rsquo;s warm.", 15, 21) + prov("MAYA &middot; FRIDAY") + "<div style=margin-top:10px;>" + faces("MP", "Maya, Priya", 22) + "</div>", "14px")}</div></div>', top=14)
    inner += gut(box(f'<div class="kickm" style="margin-bottom: 6px;">6:00</div>' + says('At the house. Maya&rsquo;s cooking, so the river walk turns around at 4:30.', 16, 23)), top=12)
    return phone2(inner, active='Home')

def build():
    cols = [
        col(caucus(), cap('1', 'Priya, asked privately', 'One question before anything is proposed. Vesper says exactly what it will do with her answer, and promises nothing about what the others might guess.', tags=(EX, PF, PRIV('PRIYA')))),
        col(room(), cap('2', 'A suggestion, an objection, a second house', 'Dana says no, in her own words, and gives a reason. The second house answers her reason and names what it costs.', tags=(EX, SHARED()))),
        col(organizer(), cap('3', 'Nora: where things actually stand', 'Maya took dinners because she said so. Nothing is booked, nobody has tickets, and the screen says that.', tags=(EX, PRIV('NORA')))),
        col(split(), cap('4', 'Splitting, as abundance', 'Two afternoons and one time to meet. Each option carries whose idea it was.', tags=(EX, SHARED()))),
    ]
    nc = review([
        ('MINIMUM CONTEXT', 'Four people and one thing to decide. No shared history is needed. At least two of them need to be reachable by Vesper privately, which is the real adoption cost.'),
        ('ORGANIZER EFFORT', 'Nora said &ldquo;upstate in October, the four of us&rdquo; once. She makes one final call. Compare the as-reported baseline: 83 messages, 19 hours and 11 days for the group trips that survive at all.'),
        ('MEMBER EFFORT', 'One private answer (optional) and one tap. Nobody ranks a list or fills in availability.'),
        ('AUDIENCE EFFECT', 'Priya&rsquo;s ceiling: nobody. The recommendation and the votes: all four. The mandate: all four, because a delegation people cannot see is not one. Nora&rsquo;s relief view: Nora.'),
        ('FAIRNESS', 'Dana went along with the house and with Friday dinner. Saturday afternoon leads with the barns because <i>she asked about them on Tuesday</i> &mdash; attributed to what she said, never to a tally of who has compromised. The tally exists internally and is shown to no one.'),
        ('LOW PARTICIPATION', 'Priya and Nora have not voted in frame 2 and the card says so plainly. A member who never answers is unknown, not agreeable.'),
        ('ONE FAILURE', 'Someone works out whose limit shaped the choice. In a group of four that is possible, and the board does not promise otherwise: Vesper promises what it will do with the number, not what the others will infer.'),
    ], [
        ('BASIC INTERACTION', 'A group chat holds the conversation and should keep holding it. This does not replace the thread; it holds what a thread cannot &mdash; one decision, its state, and who may settle it.'),
        ('WHAT IMPROVES, FOR WHOM', 'Priya: she never has to say the number in front of three friends. Dana: her objection changes the outcome. Nora: she sees what is actually undone, not a feeling of progress. Total work: one question each, one tap each. What a thread cannot hold: one decision, its state, and who settles it.'),
        ('DIFFERENTIATING?', 'Yes. &ldquo;Every competitor sells speed of decision. Not one sells relief from the role.&rdquo; Frame 3 is that sentence drawn.'),
        ('SYSTEM ADVANTAGE', 'The design agent earlier reported that proposals, votes, receipts and a private-constraint guard are shipped. That is a report, not a verified fact, and a guard is not a finished experience. Booking is retired: nothing here holds, reserves or pays.'),
        ('REJECTION TEST', 'Reject broad polls, availability grids and preference questionnaires. Reject &ldquo;works for everyone&rdquo; &mdash; the phrase implies someone needed accommodating. Reject any visible fairness score, conflict summary, or label on a person.'),
    ], 'retain',
        'A demanding and valuable specialization. The September 6 consumer strategy calls group travel a strong acquisition candidate that does not gate ordinary-life value; it is not the exclusive way in.',
        'how many of the four need to be reachable privately before this beats a group chat &mdash; and what does it honestly do when the answer is only one?',
        offscreen=['Priya&rsquo;s limit narrows the options and is never quoted, summarized or hinted at, even to Nora', 'one suggestion, not a poll', 'silence is not a yes; a second house is held in reserve', 'Saturday leads with the barns because Dana asked about them, never because of a tally of who compromised', 'one split, once; together stays the default'],
        extras=('<b>Source:</b> canon §4 (Caucus, Mandate), §5, §7 &ldquo;Resolve, do not poll&rdquo;; Interaction Design §7&ndash;§8 (splits, the diplomatic layer); group-social charter (social votes, visible care); 08-07 strategy §4.3&ndash;§4.4.',
                '<b>Named omission:</b> Repair &mdash; the house falls through on Thursday &mdash; and a genuine 2&ndash;2 deadlock are not drawn.'))
    return eboard('E2', 'E2 - The group decides', 'BEING TOGETHER', 'The group decides',
        'Four people, one weekend, and the things nobody wants to say in the group chat. The payoff is one coherent choice without a poll, '
        'a private limit that shapes it without ever being seen, and an organiser who is no longer doing everything. All fixture.',
        cols, nc, 4)

if __name__ == '__main__':
    print(build())
