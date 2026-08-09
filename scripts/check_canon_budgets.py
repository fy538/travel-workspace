#!/usr/bin/env python3
"""Keep first-read canon concise enough to function as an orientation path."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUDGETS = {
    "travel-agent/docs/product/Product Thesis.md": 1600,
    "travel-agent/docs/product/Product Model.md": 3500,
    "travel-agent/docs/product/Product Vision and Scope.md": 2500,
    "travel-agent/docs/product/What We Believe.md": 2500,
    "travel-agent/docs/product/Product Architecture Principles.md": 2800,
    "travel-agent/docs/architecture/Unified Context Graph.md": 1600,
    "travel-app/docs/Design Language.md": 4500,
    "travel-app/docs/Brand Identity.md": 2500,
}


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w’'-]+\b", text))


def main() -> int:
    problems: list[str] = []
    total_orientation = 0
    for relative, maximum in BUDGETS.items():
        path = ROOT / relative
        if not path.is_file():
            problems.append(f"missing canon: {relative}")
            continue
        count = word_count(path.read_text())
        if relative.endswith(("Product Thesis.md", "Product Model.md")):
            total_orientation += count
        if count > maximum:
            problems.append(f"{relative}: {count} words exceeds {maximum}")
    if total_orientation > 5100:
        problems.append(
            f"company orientation: Thesis + Model is {total_orientation} words; maximum 5100"
        )
    for problem in problems:
        print("canon-budget:", problem, file=sys.stderr)
    if problems:
        return 1
    print(
        f"canon-budget OK: {len(BUDGETS)} authorities within limits; "
        f"Thesis + Model = {total_orientation} words"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
