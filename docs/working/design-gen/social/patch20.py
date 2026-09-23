"""September 9 second-pass strategy alignment (handoff §0, 2026-09-09 19:59): asset gap labelled, per-person work accounted, 03.5 deferred to Plans, receiving wording agreed with Life, evidence corrected."""
MISS = []
def sub(path, pairs):
    s = open(path).read()
    for old, new in pairs:
        n = s.count(old)
        if n == 1: s = s.replace(old, new)
        elif new in s: pass
        else: MISS.append((path, old[:90]))
    open(path, 'w').write(s)

# ───────────────────────────── gen_c2 · §8.1, and the asset gap named on the pasta ─────────────────────────────
sub('gen_c2.py', [
    ("inner += gut(answer('It split because the cheese hit a pan that was still hot: the fat let go of the water. Next time, off the heat, a ladle of the starchy water first, then the cheese in small handfuls, stirring until it turns glossy. If it starts to grain, another splash brings it back. Saturday&rsquo;s batch will hold if the pan is warm, not hot.'), top=18)",
     "inner += gut(answer('Too much heat is one possibility; the photograph alone cannot confirm it. For the next attempt: off the heat, a ladle of the starchy water first, then the cheese in small handfuls, stirring until it turns glossy. That gives you one concrete thing to change.'), top=18)"),
    ("inner += gut(bubble('why did the sauce break? this was the Sorrento one', media=f'<div style=\"width: 220px;\">{standin(150)}</div>'), top=26)",
     "inner += gut(bubble('why did the sauce break? this was the Sorrento one', media=f'<div style=\"width: 220px;\">{standin(150, \"THE PASTA &middot; HER PHONE &middot; ASSET NOT SOURCED\")}</div>'), top=26)"),
    ("('THURSDAY 7:50 PM', 'THE PRIVATE ASK', 'A photo and a question; a compact answer', 'THE &sect;8.1 SPECIMEN &middot; NO SAVE PROMPT, NO SHARE PROMPT')",
     "('THURSDAY 7:50 PM', 'THE PRIVATE ASK', 'A photo and a question; one possible cause and one thing to change', 'THE &sect;8.1 SPECIMEN, REVISED &middot; HEAT IS ONE POSSIBILITY, NOT A DIAGNOSIS FROM A PHOTOGRAPH &middot; NO GUARANTEE ABOUT SATURDAY&rsquo;S BATCH &middot; NO SAVE PROMPT, NO SHARE PROMPT')"),
])

# ───────────────────────────── gen_c3 · 03.8 timing, 03.5 deferred to Plans, the work account ─────────────────────────────
sub('gen_c3.py', [
    ("7:32 &middot; Sam finds the buzzer. Maya opened the door before he pressed it.<br><br>7:50 &middot; The rag&ugrave; is Dana&rsquo;s. Someone photographs the table; it is Maya.<br><br>8:40 &middot; Sam says he has to go at nine and nobody makes it a thing.<br><br>9:02 &middot; He leaves. There is no button for that.",
     "7:32 &middot; Sam finds the buzzer. Nora opens the door before he presses it.<br><br>8:05 &middot; Maya arrives at eight, as she said she would, and eats with them.<br><br>8:25 &middot; The rag&ugrave; is Dana&rsquo;s. Someone photographs the table; it is Maya.<br><br>8:40 &middot; Sam says he has to go at nine and nobody makes it a thing.<br><br>9:02 &middot; He leaves. There is no button for that."),
    ("f'<div class=\"fn\" style=\"color: {ANCHOR}; margin-top: auto;\">NO APP ACTION TO ARRIVE, EAT, OR LEAVE &middot; THE TABLE PHOTOGRAPH IS 04.1</div></div>')",
     "f'<div class=\"fn\" style=\"color: {ANCHOR}; margin-top: auto;\">THE UNCHANGED-SEVEN BRANCH: SEVEN STANDS, SO MAYA COMES AT EIGHT AS 03.5 SAYS &middot; NO APP ACTION TO ARRIVE, EAT, OR LEAVE &middot; THE TABLE PHOTOGRAPH IS 04.1, AT 8:25</div></div>')"),
    ("'COPY OF HOME 02 &middot; 09-05', 'BRANCH &middot; RECOMMENDED &middot; UNADOPTED', 'RECOMMEND ONCE; A DIRECT ACTION; LEAVING IT IS THE UNADOPTED ENDING'",
     "'COPY OF HOME 02 &middot; 09-05', 'BRANCH &middot; RECOMMENDED &middot; UNADOPTED', 'THE TWO DIRECT ACTIONS ARE DEFERRED TO PLANS&rsquo; NARROW AMENDMENT COMPARISON (07 / 11): SOCIAL DOES NOT SET A SECOND DEFAULT FOR THE SAME ACT &middot; AN EDITABLE LOGISTICAL PROPOSAL, NOT INVENTED MEANING &middot; A SENT PROPOSAL IS NOT AN ADOPTED ARRANGEMENT'"),
    ("('THE CHANGE, TWO BRANCHES', N('03.5 is the recommended route: Maya&rsquo;s eight arrives as one ask with the tradeoff stated and two direct actions;",
     "('THE CHANGE, TWO BRANCHES', N('03.5 is the recommended route: Maya&rsquo;s eight arrives as one ask with the tradeoff stated. Whether it carries two direct actions or Plans&rsquo; recommend-once-without-buttons rule is Plans&rsquo; narrow amendment comparison to lead (07 / 11); the frame is drawn with the actions and marked deferred, so the two projects do not set independent defaults for one act. Nora keeps authorship and Send, and a sent proposal is not an adopted arrangement;"),
])

# ───────────────────────────── gen_c4 · the table photograph moves to 8:25 ─────────────────────────────
sub('gen_c4.py', [
    ('standin(250, "THE TABLE &middot; 7:50 PM &middot; STAND-IN")', 'standin(250, "THE TABLE &middot; 8:25 PM &middot; HER PHONE &middot; ASSET NOT SOURCED")'),
    ('standin(210, "THE TABLE &middot; SATURDAY 7:50 PM &middot; STAND-IN")', 'standin(210, "THE TABLE &middot; SATURDAY 8:25 PM &middot; ASSET NOT SOURCED")'),
    ('standin(230, "THE TABLE &middot; SATURDAY 7:50 PM &middot; STAND-IN")', 'standin(230, "THE TABLE &middot; SATURDAY 8:25 PM &middot; ASSET NOT SOURCED")'),
])

# ───────────────────────────── gen_c6 · the agreed receiving wording ─────────────────────────────
sub('gen_c6.py', [
    ("src('A private copy, yours after her share ends.')", "src('A copy to reread, until she takes it back.')"),
    ("entry('photo', 'The pasta, second try', 'you kept this one, Thursday', last=True)", "entry('photo', 'The pasta, second try', 'your copy, until she takes it back', last=True)"),
    ("    inner += bar('KEPT FROM NORA &middot; YOURS AFTER HER SHARE ENDS')", "    inner += bar('KEPT FROM NORA &middot; YOUR COPY, UNTIL SHE TAKES IT BACK')"),
    ("    inner += bar('SHARED WITH YOU &middot; NORA&rsquo;S, WHILE SHE LEAVES IT')", "    inner += bar('SHARED WITH YOU &middot; FINDABLE WHILE SHE SHARES IT')"),
    ("'THE EXACT SOURCE, AND THE ONE OPTIONAL KEEP', 'Her photograph, her line, who, until when; Reply to her; Ask privately; keep a copy if you want one', 'LIFE&rsquo;S EXACT-SOURCE READER (R4 GRAMMAR) &middot; THREE DISTINCT EFFECTS (ENTITY 12.4): CONTINUING SHARED ACCESS IS THE DEFAULT AND NEEDS NO KEEP; KEEP THIS PHOTOGRAPH IS A PRIVATE COPY UNDER HER GRANT, SHE IS NOT TOLD; KEEPING A PLACE IS A DIFFERENT ACT AND THERE IS NO PLACE HERE &middot; OPENING, REFINDING AND ENJOYING REQUIRE NO KEEP, AND NONE IS INFERRED FROM OPENING &middot; HOME-ORIGIN STACK PRESERVED: THE TAB BAR STAYS HOME, BACK RESTORES HOME&rsquo;S SCROLL &middot; RETENTION AGREEMENT PROPOSED, NOT ADOPTED'",
     "'THE EXACT SOURCE, AND THE ONE OPTIONAL KEEP', 'Her photograph, her line, who, until when; Reply to her; Ask privately; keep a copy if you want one', 'WORDING AGREED WITH LIFE 07.7 / 07.8 &middot; OPENING KEEPS NOTHING; IT STAYS FINDABLE WHILE SHE SHARES IT; A COPY IS YOURS TO REREAD UNTIL SHE TAKES IT BACK &middot; SHARE EXPIRY AND HER TAKING IT BACK ARE DIFFERENT CONDITIONS, AND THE COPY SURVIVES ONLY THE FIRST &middot; A KEPT PLACE IS YOURS; KEEPING A PLACE DOES NOT KEEP HER WORDS (ENTITY 12.4) &middot; HOME-ORIGIN STACK PRESERVED &middot; THE SOURCE AGREEMENT BEHIND THE COPY IS PROPOSED, NOT ADOPTED'"),
    ("'THE PULL ROUTE, AND THE ONE DISTINCTION', 'Shared with you while Nora leaves it; the one you kept; yours; held in common', 'COPY OF R3&rsquo;S GRAMMAR &middot; LIFE 04&rsquo;S &ldquo;YOURS, AND WHAT OTHERS SHARED WITH YOU&rdquo; &middot; STILL ACCESSIBLE THROUGH HER SHARE AND DELIBERATELY KEPT ARE TWO ROWS, NOT ONE &middot; A PATH BACK DOES NOT MEAN KEPT &middot; NO SOCIAL TAB, NO FEED'",
     "'THE PULL ROUTE, AND THE ONE DISTINCTION', 'Findable while she shares it; your copy until she takes it back; yours; held in common', 'COPY OF R3&rsquo;S GRAMMAR &middot; LIFE 04&rsquo;S &ldquo;YOURS, AND WHAT OTHERS SHARED WITH YOU&rdquo; &middot; FINDABLE-WHILE-SHARED AND DELIBERATELY KEPT ARE TWO ROWS, NOT ONE &middot; NEITHER OPENING AN ORIGINAL NOR KEEPING A PLACE ESTABLISHES RETENTION &middot; NO SOCIAL TAB, NO FEED'"),
    ('standin(200, "THE PASTA &middot; THURSDAY 7:40 PM &middot; STAND-IN")', 'standin(200, "THE PASTA &middot; HER PHONE, THURSDAY 7:40 PM &middot; ASSET NOT SOURCED")'),
    ('standin(240, "THE PASTA &middot; THURSDAY 7:40 PM &middot; STAND-IN")', 'standin(240, "THE PASTA &middot; HER PHONE, THURSDAY 7:40 PM &middot; ASSET NOT SOURCED")'),
    ("        ('WHAT IS NOT INHERITED',",
     "        ('THE ASSETS, AND THE GAP', N('Every photographic plate on these boards is a labelled stand-in, and the frames therefore argue that a friend&rsquo;s original is the whole benefit while showing nothing worth looking at. The four that matter are named on their plates: the pasta (Nora&rsquo;s phone, Thursday 7:40 pm), the table (Maya&rsquo;s phone, Saturday 8:25 pm), the Print Room (Maya&rsquo;s own visit) and Dana&rsquo;s rag&ugrave; (Sorrento, Wednesday). The Print Room alone has an authored plate, the Places project&rsquo;s own illustration; the rest read &ldquo;asset not sourced&rdquo;. Ordinary rights-cleared photographs, unpolished and unstaged, are still needed and are their own scope: this pass contacts nobody and imports no private library. The authored words beside each plate are real fixture material and carry what they can meanwhile.')),\n        ('WHAT IS NOT INHERITED',"),
])

# ───────────────────────────── gen_se · specimen, stamp, statuses, budget ─────────────────────────────
sub('gen_se.py', [
    ("'&ldquo;It split because the cheese hit a pan that was still hot: the fat let go of the water. Next time, off the heat, a ladle of the starchy water first, then the cheese in small handfuls, stirring until it turns glossy. If it starts to grain, another splash brings it back. Saturday&rsquo;s batch will hold if the pan is warm, not hot.&rdquo;'",
     "'&ldquo;Too much heat is one possibility; the photograph alone cannot confirm it. For the next attempt: off the heat, a ladle of the starchy water first, then the cheese in small handfuls, stirring until it turns glossy. That gives you one concrete thing to change.&rdquo; (Revised September 9: one possible cause, not a diagnosis from a photograph; no guarantee about Saturday&rsquo;s batch.)'"),
    ("STAMP = 'SEPTEMBER 9 &middot; FRESH SIX-PROJECT REVIEW &middot; 2026-09-09'", "STAMP = 'SEPTEMBER 9 &middot; SECOND-PASS STRATEGY ALIGNMENT &middot; 2026-09-09'"),
    ("September 8 added board 08&rsquo;s five continuation slots at the assignment&rsquo;s request, so the route now holds 29 against a ceiling of 24. This is recorded as an unresolved scope discrepancy, not compliance: the ceiling was not amended, and the founder decides whether it moves or two frames fold.",
     "September 8 added board 08&rsquo;s five continuation slots at the assignment&rsquo;s request, so the route holds 29 against a ceiling of 24; the September 9 second pass adds one comparison frame (05 D7-B, the ordinary messaging control) against a ceiling of 12, its A side reused from 08.2. Both are recorded as unresolved scope discrepancies, not compliance: neither ceiling was amended, and the founder decides whether they move or frames fold."),
    ("'SEPTEMBER 9, LATER: one exact-original route with an optional plain Keep; placement settled as an extension of the September 5 Status-doorway permission; five slots over the ceiling = UNRESOLVED SCOPE DISCREPANCY'",
     "'SECOND PASS: receiving wording agreed with Life 07.7 / 07.8; the asset gap named on every plate; five slots over the ceiling = UNRESOLVED SCOPE DISCREPANCY'"),
    ("'CLOSED &sect;15: both dinner branches reach their own arrival view; a link-holder answer is provisional until the address code'",
     "'SECOND PASS: each person&rsquo;s work accounted against a message-and-link workflow; 03.5 deferred to Plans; 03.8&rsquo;s timing reconciled with the unchanged-seven branch'"),
    ("'SEPTEMBER 9, LATER: 04.8 names what the previous evening supplies and what it does not; 04.6 names what Sam holds'",
     "'SECOND PASS: the table photograph is 8:25, after Maya arrives at eight; 04.8 names what the previous evening supplies and what it does not'"),
    ("'CLOSED &sect;15: fair comparisons (same facts, same grants); D4 arrival facts restated per branch'",
     "'SECOND PASS: D7 compares original-only receiving against a capable ordinary messaging app, not a straw control; 13 frames = UNRESOLVED SCOPE DISCREPANCY'"),
])
print('patched; misses:', len(MISS)); [print('  MISS', p, o) for p, o in MISS]
