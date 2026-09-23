#!/usr/bin/env python3
"""Fail on broken relative Markdown links in living workspace documentation."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
LINK = re.compile(r"(?<!!)\[[^]]*\]\(([^)]+)\)")


def prose_lines(text: str):
    """Yield original line numbers, excluding Markdown code spans and fences."""
    fence = None
    for number, line in enumerate(text.splitlines(), 1):
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            yield number, re.sub(r"(`+).*?\1", "", line)


def target_path(source: Path, raw: str) -> Path | None:
    target = raw.strip().split(" #", 1)[0].strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if not target or target.startswith(("#", "mailto:")) or "://" in target:
        return None
    target = unquote(target.split("#", 1)[0])
    return (source.parent / target).resolve()


def main() -> int:
    problems = []
    files = [
        path for path in DOCS.rglob("*.md")
        if "archive" not in path.relative_to(DOCS).parts
    ]
    for source in sorted(files):
        for line_number, line in prose_lines(source.read_text(errors="replace")):
            for match in LINK.finditer(line):
                target = target_path(source, match.group(1))
                if target is not None and not target.exists():
                    problems.append(
                        f"{source.relative_to(ROOT)}:{line_number}: missing link target {match.group(1)!r}"
                    )
    for problem in problems:
        print("docs-links:", problem, file=sys.stderr)
    if problems:
        print(f"docs-links FAILED: {len(problems)} broken living-doc link(s)", file=sys.stderr)
        return 1
    print(f"docs-links OK: {len(files)} living Markdown files checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
