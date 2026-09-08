import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "living_links", Path(__file__).parents[1] / "check_living_doc_links.py"
)
links = importlib.util.module_from_spec(spec)
spec.loader.exec_module(links)


def test_code_examples_are_not_links_but_adjacent_prose_is_checked():
    source = "`window.LAB_DERIVE[fixture](state)` [real](missing.md)\n```js\n[x](code)\n```\n[after](after.md)"
    found = [
        (line, m.group(1))
        for line, text in links.prose_lines(source)
        for m in links.LINK.finditer(text)
    ]
    assert found == [(1, "missing.md"), (5, "after.md")]


def test_shorter_or_different_fence_does_not_end_code():
    source = "````\n```\n[x](hidden)\n~~~\n````\n[x](visible)"
    assert list(links.prose_lines(source)) == [(6, "[x](visible)")]
