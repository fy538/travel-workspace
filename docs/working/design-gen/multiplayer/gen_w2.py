"""W2 · Far apart (Pass C). A complete experience between two cities that never becomes a gathering."""
from mp_kit2 import *
from gen_merge import daycap
P = lambda t: tag(t, PLAN, 'rgba(42,56,75,0.10)')
END = tag('ENDS HERE', GREEN, 'rgba(61,112,80,0.12)')

def dana_sends():
    inner = avatar_for(bar('SHARE'), 'D')
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{plate("pier", 200, tag="PHOTO &middot; YOURS")}</div>', top=18)
    inner += gut(f'<div style="border-bottom: 1px solid rgba(27,23,20,0.14); padding: 10px 0;">{plain("calanques. 7am. nobody", size=17, lh=24)}</div>', top=16)
    inner += gut(f'<div class="kickm" style="margin-bottom: 8px;">TO</div><span class="vdl-recipient"><span class="vdl-avatar ink sm vk-t-capsMicro">N</span><span class="vk-t-bodySmMedium">Nora</span></span>', top=20)
    inner += gut(actions(btn('Send'), door('Not now', MUTE)), top=22)
    return phone2(inner, active='Home')

def nora_receives():
    inner = anchor_row('NEW YORK', 'TUESDAY 7:40 AM')
    inner += orientation('Rain until noon.', 'Tuesday &middot; 52&deg; &middot; dentist at 9:00, and I&rsquo;d still walk.')
    inner += sect('From Dana') + gut(f'<div style="border-radius: 14px; overflow: hidden; margin-bottom: 14px;">{plate("pier", 190, tag="PHOTO &middot; DANA")}</div>'
        + original(150, author='Dana', meta='1:04 AM · TO YOU', words='calanques. 7am. nobody', place='Calanque de Sugiton, Marseille', placeMeta='6:40 AM THERE NOW · 61°', door='Reply'))
    return phone2(inner, active='Home')

def paired():
    inner = header('Your cliff and Dana&rsquo;s', 'Sorrento, August &middot; Marseille, this week', back=True)
    inner += gut(f'<div style="display: flex; gap: 10px;">'
        f'<div style="flex: 1; border-radius: 12px; overflow: hidden;">{plate("room", 140, tag="SORRENTO &middot; YOURS")}</div>'
        f'<div style="flex: 1; border-radius: 12px; overflow: hidden;">{plate("pier", 140, tag="SUGITON &middot; DANA")}</div></div>', top=18)
    inner += gut(says('Two pale coasts on the same sea, made of different things. Yours is volcanic tuff, in cliffs about fifty meters high. Hers is hard white limestone: valleys cut when the sea stood far lower, then flooded when it rose.', 18, 25), top=14)
    inner += gut(dci('FactPair', 108, tone='lead', a='YOURS &middot; SORRENTO', av='Volcanic tuff, cliffs about 50 m', an='FROM THE CAMPANIAN IGNIMBRITE',
                     b='HERS &middot; SUGITON', bv='Limestone valleys, later flooded', bn='ICE-AGE SEA ABOUT 130 M LOWER'), top=14)
    inner += gut(dci('SourceList', 58, items='1=PARC NATIONAL DES CALANQUES · GEOLOGY AND LANDSCAPES;2=J. SEISMOLOGY, 2022 · TUFF CLIFF, SORRENTO PENINSULA;Y=YOUR PHOTO · AUG;D=DANA · TO YOU · TUE'), top=12)
    inner += gut(actions(btn('Send to Dana'), door('Keep', MUTE)), top=12)
    return phone2(inner, active='Life')

def dana_reads():
    inner = avatar_for(anchor_row('MARSEILLE', 'SUNDAY 9:15 PM'), 'D')
    inner += orientation('Mistral tomorrow.', 'Sunday &middot; 17&deg; &middot; Sugiton&rsquo;s path closes in high wind.')
    inner += sect('From Nora') + gut(f'<div style="display: flex; gap: 8px; margin-bottom: 14px;">'
        f'<div style="flex: 1; border-radius: 10px; overflow: hidden;">{plate("room", 96, tag="HERS")}</div><div style="flex: 1; border-radius: 10px; overflow: hidden;">{plate("pier", 96, tag="YOURS")}</div></div>'
        + original(130, author='Nora', meta='3:02 PM · TO YOU', words='yours is a flooded valley. mine is volcanic ash. apparently', door='Reply'))
    inner += gut(f'<div style="display: flex; flex-direction: column; gap: 8px;">{bubble("ha!! ok that&rsquo;s actually cool")}{bubble("a flooded valley. i&rsquo;m telling everyone")}</div>', top=16)
    return phone2(inner, active='Home')

def between():
    inner = header('You and Dana', 'Since 2021', back=True)
    inner += gut(says('Last together: Sorrento, a year ago.', 17, 24, INK2), top=18)
    inner += sect('Between you') + gut('<div>'
        + row('Eleven photos, three coasts', mark='dot', color=GOLDD)
        + row('Your cliff and hers &middot; <span style="color: #6E6862;">last week</span>', mark='dot', color=GOLDD)
        + row('The dish she told you to try', mark='hollow', color=GOLDD, last=True) + '</div>')
    inner += sect('Marseille, through Dana') + gut('<div>'
        + row('Calanque de Sugiton &middot; <span style="color: #6E6862;">7am, nobody</span>', mark='hollow')
        + row('The fish market at the port &middot; <span style="color: #6E6862;">March</span>', mark='hollow', last=True) + '</div>')
    return phone2(inner, active='Life')

def cell(day, n, title, sub, ph, tags=()):
    return col(ph, (f'<div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 7px;">{"".join(tags)}</div>' if tags else '') + daycap(day, n, title, sub))

def build():
    cols = [cell('TUESDAY &middot; MARSEILLE', '1', 'Dana, at seven in the morning', 'A photo and three words, to one person.', dana_sends(), (P('SEND'),)),
            cell('TUESDAY &middot; NEW YORK', '2', 'Nora, over coffee', 'She looks at it for a while. She doesn&rsquo;t reply.', nora_receives(), (P('THE READER'), END)),
            cell('SUNDAY &middot; NEW YORK', '3', 'A week later, in Life', 'Her own cliff beside Dana&rsquo;s, and why they differ.', paired(), (P('TOGETHER'), P('SEND'))),
            cell('SUNDAY &middot; MARSEILLE', '4', 'Dana, that evening', 'She learns something about the water she swims in.', dana_reads(), (P('THE READER'), END)),
            cell('ANY TIME', '5', 'What is between them', 'A friendship that lives in what they send. Nothing here points toward a visit.', between(), (P('TOGETHER'), END))]
    n1 = notes('WHY THIS IS COMPLETE', led([
        ('NO GATHERING', 'Nobody travels, nobody plans to, and no frame offers it. The value arrived where each of them already was: a Tuesday coffee in New York, a Sunday evening in Marseille.'),
        ('THREE ENDINGS', 'Frame 2 ends with no reply and is a success. Frame 4 ends with two messages and is a success. Frame 5 is what a friendship like this looks like at rest.'),
        ('WHAT VESPER ADDED', 'One line about the world under Dana&rsquo;s photo &mdash; the time and temperature where she is &mdash; and one earned comparison a week later. It did not summarize her, prompt a reply, or notice how long it had been.'),
        ('BOTH DIRECTIONS', 'Dana gets as much as Nora: she learns why her coast is all coves. A remote friendship that only serves the person with the app open is not multiplayer.'),
    ]), w=620)
    n2 = notes('WHAT DID NOT HAPPEN', led([
        ('NO TRIP', 'No &ldquo;flights to Marseille,&rdquo; no &ldquo;plan a visit,&rdquo; no saved-places list for a city Nora has no plan to see. &ldquo;Marseille, through Dana&rdquo; is how she knows a place she may never go to.'),
        ('NO CADENCE', 'Nothing counts the week between frames 2 and 3, or the year since Sorrento.'),
        ('NO FORCED PAIR', 'Most of Dana&rsquo;s photos pair with nothing. Frame 3 rests on two sources: the Calanques national park&rsquo;s own geology page, and a 2022 <i>Journal of Seismology</i> paper on a tuff cliff in the Sorrento Peninsula. An earlier draft explained why one coast has towns and the other coves; no source supported that, and it is gone.'),
    ]), w=560)
    n3 = notes('OMISSIONS AND DEPENDENCIES', N('<b>Dependency:</b> frame 2&rsquo;s place line shows the time and weather where Dana is. That uses the place she attached, never her device; a share with no place shows nothing.')
        + N('<b>Not drawn:</b> three or more friends in different cities; a time-zone problem, such as a reply landing at 3 AM; a remote friend with no account.')
        + N('<b>Source:</b> brief &sect;8 Pass C; D3 variant B; E5 frame 4; canon &sect;9 (&ldquo;people giving one another better access to places&rdquo;).'), w=440)
    return write('04 - Far apart', board(bw(5, (620, 560, 440)), hh('04', 1900),
        '04 &middot; REMOTE, ASYNCHRONOUS, COMPLETE', 'Far apart',
        'Two friends in two cities. One sends a photo; the other enjoys it and says nothing; a week later something true connects their two coasts. '
        'It never becomes a meetup, a trip or a plan, and it is not an abandoned branch of a local story. The geology comes from two named sources, checked September 21; the people, photos and weather are fixtures.',
        cols, (n1, n2, n3)))

if __name__ == '__main__':
    print(build())
