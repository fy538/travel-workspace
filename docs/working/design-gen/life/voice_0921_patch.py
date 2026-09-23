#!/usr/bin/env python3
"""One-shot voice pass (Sep 21) on build_0915.py (boards 08/09) and build_0921.py (04b).
Moves reviewer doctrine out of the phones into the notes ("decided, not displayed"), makes
notice/sheet copy positive and contracted, and fixes British spellings. Every replacement is
asserted to match exactly once. Rule source: memory feedback_board_copy_voice (founder, Sep 20-21)."""
import sys
D = '/Users/feihuyan/travel-workspace/docs/working/design-gen/life/'


def patch(fname, pairs):
    p = D + fname
    s = open(p, encoding='utf-8').read()
    for a, b in pairs:
        assert s.count(a) == 1, (fname, a[:80], s.count(a))
        s = s.replace(a, b)
    open(p, 'w', encoding='utf-8').write(s)
    print(fname, len(pairs), 'replacements')


P15 = [
 # 08.3 — the email body loses its in-card stamp
 ("""'</div>'
                 '<div style="margin-top:14px; border-top:1px solid var(--hair-thin); padding-top:10px;">'
                 + stamp('SHOWN AS RECEIVED &middot; THIS STUDY RENDERS ONLY THE LINES THE RECORD HOLDS &middot; NOTHING IS FILLED IN')
                 + '</div></div>', top=14)""",
  """'</div>'
                 '</div>', top=14)"""),
 ("""                   + sect('THE ORIGINAL &middot; EMAIL', 'KEPT VERBATIM')""", """                   + sect('THE ORIGINAL &middot; EMAIL')"""),
 ("""                   + gut(stamp('THE TICKET ABOVE IS A PROJECTION OF THESE LINES'), top=14)
                   + sect('WHAT THIS IS NOT')
                   + gut('<div class="rsub">Not re-rendered as a ticket, not summarised, not corrected. '
                         'If a line is wrong here, it is wrong in the message you were sent.</div>')
                   + gut(door('Back to ferry capri'), top=16), 1000),
             'The body itself, in the message&rsquo;s own words &mdash; the point of the door. '
             'The fixture holds no further prose, and none is written: the frame says so rather than filling the page.')""",
  """                   + gut(door('Back to ferry capri'), top=20), 1000),
             'The message itself, in its own lines, behind the door 05.9 offers; the ticket is a projection of these lines. '
             'DECIDED, NOT DISPLAYED: the fixture holds no further prose and none is written. Nothing is re-rendered, summarized or corrected; '
             'a wrong line is wrong in the message as sent.')"""),
 # 08.4
 ("""                   + gut(stamp('WHOLE IMAGE &middot; NOTHING CROPPED &middot; PINCH TO ZOOM'), top=10)
""", ""),
 ("""             'The object is the image, so it opens whole before anything is said about it. '
             'Occurrence and containment sit below, as on 04.')""",
  """             'The object is the image, so it opens whole before anything is said about it. '
             'Occurrence and containment sit below, as on 04. DECIDED, NOT DISPLAYED: whole image, nothing cropped.')"""),
 # 08.5
 ("""                   + gut(stamp('2&times; &middot; DRAG TO MOVE &middot; DOUBLE-TAP TO FIT'), top=12)
                   + gut('<div class="rsub">The same file, shown larger. Nothing is sharpened, re-encoded or generated to fill in detail.</div>', top=12), 700),
             'Zoom is reading, not editing. Native pinch, pan, double-tap-to-fit and their behaviour under larger text '
             'need implementation evidence; a static frame cannot show them.')""",
  """                   , 700),
             'Zoom is reading: the same file, larger. DECIDED, NOT DISPLAYED: nothing is sharpened, re-encoded or generated. '
             'Native pinch, pan, double-tap-to-fit and their behavior under larger text need implementation evidence.')"""),
 # 08.6
 ("""stamp('SCANNED &middot; KEPT VERBATIM')""", """stamp('SCANNED')"""),
 ("""                         '<span class="rsub" style="padding-left:6px;">Both pages were scanned</span></div>', top=14)""",
  """                         '</div>', top=14)"""),
 # 08.7
 ("""                   + gut('<div class="rsub">What was parsed stays readable while the message loads.</div>', top=12)
""", ""),
 # 08.8
 ("""title='No connection · the message is not on this phone',
                             body='It is kept, not lost. It opens when you are back.'""",
  """title='No connection',
                             body='The message opens when you’re back online.'"""),
 ("""                   + sect('WHAT IS ON THIS PHONE')
                   + gut('<div class="rsub">The fields Vesper parsed from it, kept verbatim:</div>', top=12)
                   + gut('<div style="font-family:var(--serif); font-size:16px; line-height:24px;">'
                         'Sorrento (SOR) &rarr; Marina Grande &middot; 19 August 2026 &middot; 11:20</div>', top=10)
                   + gut(stamp('NOTHING IS FILLED IN TO STAND FOR THE MESSAGE'), top=12)""",
  """                   + sect('FROM THE TICKET')
                   + gut('<div style="font-family:var(--serif); font-size:16px; line-height:24px;">'
                         'Sorrento (SOR) &rarr; Marina Grande &middot; 19 August 2026 &middot; 11:20</div>', top=12)"""),
 ("""             'Offline is honest and small: what is here, what is not, and when it returns. '""",
  """             'Offline is small: what is here, and when the rest returns. DECIDED, NOT DISPLAYED: nothing stands in for the message. '"""),
 # 08.9
 ("""title='This message cannot be opened',
                             body='The file is here but unreadable. No stand-in is shown.'""",
  """title='This message can’t be opened',
                             body='The file is here but can’t be read.'"""),
 ("""                   + sect('WHAT THE RECORD STILL SAYS')
                   + gut('<div class="rsub">The parsed fields stay, marked as parsed. The day and the episode are unchanged.</div>', top=12)
                   + gut(stamp('NO REPLACEMENT ORIGINAL IS GENERATED &middot; A PROJECTION NEVER BECOMES THE SOURCE'), top=12), 720),""",
  """                   + sect('FROM THE TICKET')
                   + gut('<div style="font-family:var(--serif); font-size:16px; line-height:24px;">'
                         'Sorrento (SOR) &rarr; Marina Grande &middot; 19 August 2026 &middot; 11:20</div>', top=12), 720),"""),
 ("""             'A lost original stays lost in the drawing. Reporting is repair, detaching is containment, and neither invents '""",
  """             'DECIDED, NOT DISPLAYED: no replacement original is generated; a projection never becomes the source; the day and episode are unchanged. '
             'Reporting is repair, detaching is containment, and neither invents '"""),
 # 08.10
 ("""phone(searchbar('ferry capri') + gut(stamp('RETURNED &middot; QUERY, FILTER AND SCROLL KEPT', '--gold-deep'), top=14)
                    + sect('PASSES &amp; TICKETS', '1')""",
  """phone(searchbar('ferry capri') + sect('PASSES &amp; TICKETS', '1', )"""),
 # 09.2
 ("""                   + actionbar('Export 3', 'Delete 3')
                   + gut(stamp('THE SAME THREE FOR BOTH DOORS &middot; NAMED BEFORE EITHER RUNS'), top=12), 900),""",
  """                   + actionbar('Export 3', 'Delete 3'), 900),"""),
 # 09.3
 ("""                           'Two are your camera&rsquo;s and leave as files you keep. Maya&rsquo;s photograph stays in the record: '
                           'a copy of hers is not this door&rsquo;s to give.',
                           'Export 2', 'Cancel',
                           tint='<div style="padding-top:12px;">' + stamp('HERS STAYS &middot; NOTHING OF MAYA&rsquo;S LEAVES HERE') + '</div>'), 900),""",
  """                           'Your two save as files. Maya&rsquo;s stays in the record; it&rsquo;s hers to share.',
                           'Export 2', 'Cancel'), 900),"""),
 # 09.4
 ("""                           'They leave your record. The day and the episode stay, holding less. '
                           'Maya&rsquo;s photograph goes from your record, not from hers.',
                           'Delete 3', 'Cancel',
                           tint='<div style="padding-top:12px;">' + stamp('NOT A CORRECTION &middot; NOT A DETACH &middot; NOT A RELEASE') + '</div>'), 900),
             'Deletion names what disappears and what survives, and distinguishes itself from the three verbs it is often confused with. '
             'The threshold is carried by words, not by colour: oxblood stays a live-time mark in Life.')""",
  """                           'They leave your record. The day and its episode stay. Maya still has hers.',
                           'Delete 3', 'Cancel'), 900),
             'Deletion names what goes and what stays, once, at the moment of action. DECIDED, NOT DISPLAYED: it is not correction, detach or release (09.8). '
             'The threshold is carried by words, not by color: oxblood stays a live-time mark in Life.')"""),
 # 09.5
 ("""                   + actionbar('Export 3', 'Delete 3')
                   + gut(stamp('CANCELLED &middot; NOTHING EXPORTED &middot; NOTHING DELETED &middot; THE SAME THREE ARE STILL CHOSEN'), top=12), 900),
             'Cancel returns to the moment before the sheet, with the selection intact. '
             'Stopping is not an action with consequences of its own, and it says so.')""",
  """                   + actionbar('Export 3', 'Delete 3'), 900),
             'Cancel returns to the moment before the sheet, with the same three still chosen. '
             'DECIDED, NOT DISPLAYED: nothing was exported or deleted, so nothing says so.')"""),
 # 09.6
 ("""title='1 of 2 did not export',
                             body='One file could not be read. The other is saved where you chose.'""",
  """title='1 of 2 didn’t export',
                             body='One file couldn’t be read. The other is saved where you chose.'"""),
 ("""                   + gut(stamp('PART OF A BATCH IS NOT ALL OF IT &middot; EACH FILE REPORTS ITSELF'), top=12), 860),""",
  """                   , 860),"""),
 # 09.7
 ("""                   + gut(door('Undo'), top=12) + GRID
                   + gut(stamp('THE COUNT MOVED 214 &rarr; 211 &middot; THE DAYS THEY WERE IN ARE STILL THERE'), top=12), 980),""",
  """                   + gut(door('Undo'), top=12) + GRID, 980),"""),
 # 09.8
 ("""                   + sect('NOT HERE')
                   + gut('<div class="rsub">Account-level export, imports, what may be used later, and continuing help are '
                         'You &amp; Trust&rsquo;s. Life acts on the things in front of you.</div>', top=12)
                   + gut(door('Open these controls in You &amp; Trust'), top=14)
                   + gut(stamp('LIFE IS NOT A SECOND SETTINGS SYSTEM'), top=14), 760),
             'The four verbs are kept apart because their consequences differ, and the global controls stay with their owner. '
             'A drawing authorises no export and no deletion.')""",
  """                   + sect('EVERYTHING ELSE')
                   + gut(door('Your data, in Settings'), top=12), 760),
             'The four verbs are kept apart because their consequences differ. DECIDED, NOT DISPLAYED: account-level export, imports, '
             'later use and continuing help stay with You &amp; Trust; Life is not a second settings system. A drawing authorizes no export and no deletion.')"""),
 ("""'Export and deletion have different scopes, and nothing here authorises either.'""",
  """'Export and deletion have different scopes, and nothing here authorizes either.'"""),
]
P21 = [
 ("Native pinch, pan, double-tap and behaviour under larger text", "Native pinch, pan, double-tap and behavior under larger text"),
 ("each root shows the same authorised object.", "each root shows the same authorized object."),
 ("neighbours and zoom", "neighbors and zoom"),
 ("natural colour and real low-light", "natural color and real low-light"),
]
patch('build_0915.py', P15)
patch('build_0921.py', P21)
