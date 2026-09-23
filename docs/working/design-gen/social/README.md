---
doc_type: working
status: active
owner: founder / social design
created: 2026-09-09
last_verified: 2026-09-22
expires: 2026-10-09
why_new: Preserves the recovered generators and reproduction notes for the dated Social Experience design boards, separate from product or native implementation authority.
supersedes: []
source_of_truth_for: []
---

# Social Experience board generators (recovered 2026-09-09)

Generators for Claude Design project `3ef10868` (Vesper — Social Experience), boards 00–07.
Recovered from session transcripts after the scratchpads were wiped; `hp/` holds the Home/Places
kit modules the Social generators import (`kit.py`, `gen_generous*.py`, `gen_merge.py`,
`gen_p2_common.py`, `gen_p2_04.py`, `gen_artifact.py`, `gen_seam.py`, `gen_home.py`).

Run from a scratch directory: put `hp/` where `gen_se.py`/`gen_c2.py` expect it (the `HP`
constant near the top of `gen_se.py` and `gen_c2.py`; point it at this `hp/` folder), create
`out/heights.json`, then `python3 measure.py` (00–01) and `python3 measure_c2.py` (02–07), which
regenerate and ink-measure each board with headless Chrome. Push with DesignSync `finalize_plan`
(deletes: []) + `write_files` with `localPath`. Everything on the boards is labelled fixture.
