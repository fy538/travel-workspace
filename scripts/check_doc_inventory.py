#!/usr/bin/env python3
"""Ensure every workspace Markdown document has one inventory disposition."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
INVENTORY = DOCS / "governance" / "inventory.yaml"
ALLOWED_DISPOSITIONS = {
    "keep_authoritative",
    "keep_reference",
    "merge",
    "archive",
    "delete_candidate",
    "investigate",
}


@dataclass(frozen=True)
class Classification:
    disposition: str
    rationale: str
    source: str
    target: str | None = None


def load_inventory(path: Path = INVENTORY) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("inventory must be a YAML mapping")
    return data


def markdown_paths() -> list[str]:
    return sorted(path.relative_to(ROOT).as_posix() for path in DOCS.rglob("*.md"))


def _entry(value: Any, source: str) -> Classification:
    if not isinstance(value, dict):
        raise ValueError(f"{source} must be a mapping")
    disposition = value.get("disposition")
    rationale = value.get("rationale")
    target = value.get("target")
    if disposition not in ALLOWED_DISPOSITIONS:
        raise ValueError(f"{source} has invalid disposition: {disposition!r}")
    if not isinstance(rationale, str) or len(rationale.strip()) < 15:
        raise ValueError(f"{source} needs a concrete rationale")
    if disposition == "merge" and (not isinstance(target, str) or not target.strip()):
        raise ValueError(f"{source} is merge but has no target")
    return Classification(disposition, rationale.strip(), source, target)


def _path_glob_matches(path: str, pattern: str) -> bool:
    """Match path globs where ``*`` never crosses `/` and ``**`` may.

    ``fnmatch`` is unsuitable here because its ``*`` also consumes path
    separators, making ``docs/reliability/*.md`` accidentally classify nested
    prompt and trace trees.
    """

    pieces: list[str] = ["^"]
    index = 0
    while index < len(pattern):
        if pattern.startswith("**/", index):
            pieces.append("(?:.*/)?")
            index += 3
        elif pattern.startswith("**", index):
            pieces.append(".*")
            index += 2
        elif pattern[index] == "*":
            pieces.append("[^/]*")
            index += 1
        elif pattern[index] == "?":
            pieces.append("[^/]")
            index += 1
        else:
            pieces.append(re.escape(pattern[index]))
            index += 1
    pieces.append("$")
    return re.match("".join(pieces), path) is not None


def classify(path: str, inventory: dict[str, Any]) -> Classification | None:
    overrides = inventory.get("overrides") or {}
    if path in overrides:
        return _entry(overrides[path], f"override:{path}")

    matches: list[Classification] = []
    for index, rule in enumerate(inventory.get("rules") or []):
        if not isinstance(rule, dict) or not isinstance(rule.get("glob"), str):
            raise ValueError(f"rule:{index} must include a glob")
        if _path_glob_matches(path, rule["glob"]):
            matches.append(_entry(rule, f"rule:{index}:{rule['glob']}"))
    if len(matches) > 1:
        sources = ", ".join(match.source for match in matches)
        raise ValueError(f"{path} matches multiple rules: {sources}")
    return matches[0] if matches else None


def location_problem(path: str, classification: Classification) -> str | None:
    """Enforce that historical truth is physically separated from living docs."""
    if classification.disposition == "archive" and not path.startswith("docs/archive/"):
        return f"archive-classified document remains in living tree: {path}"
    return None


def validate(inventory: dict[str, Any]) -> tuple[dict[str, Classification], list[str]]:
    paths = markdown_paths()
    path_set = set(paths)
    problems: list[str] = []
    classifications: dict[str, Classification] = {}

    dispositions = inventory.get("dispositions") or {}
    if set(dispositions) != ALLOWED_DISPOSITIONS:
        missing = sorted(ALLOWED_DISPOSITIONS - set(dispositions))
        extra = sorted(set(dispositions) - ALLOWED_DISPOSITIONS)
        problems.append(f"disposition catalog drift: missing={missing} extra={extra}")

    overrides = inventory.get("overrides") or {}
    stale_overrides = sorted(set(overrides) - path_set)
    if stale_overrides:
        problems.append("override paths do not exist: " + ", ".join(stale_overrides))

    for path in paths:
        try:
            result = classify(path, inventory)
        except ValueError as exc:
            problems.append(str(exc))
            continue
        if result is None:
            problems.append(f"unclassified document: {path}")
        else:
            classifications[path] = result
            problem = location_problem(path, result)
            if problem:
                problems.append(problem)

    return classifications, problems


def report(classifications: dict[str, Classification], *, details: bool) -> None:
    counts = Counter(item.disposition for item in classifications.values())
    print(f"Documentation inventory: {len(classifications)} Markdown files")
    for disposition in sorted(ALLOWED_DISPOSITIONS):
        print(f"  {disposition:20} {counts[disposition]:3}")

    if details:
        for disposition in sorted(ALLOWED_DISPOSITIONS):
            print(f"\n[{disposition}]")
            for path, item in sorted(classifications.items()):
                if item.disposition != disposition:
                    continue
                suffix = f" -> {item.target}" if item.target else ""
                print(f"- {path}{suffix}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--details", action="store_true")
    parser.add_argument(
        "--steady",
        action="store_true",
        help="fail if merge, investigate, or delete_candidate queues are non-empty",
    )
    args = parser.parse_args()

    try:
        inventory = load_inventory()
        classifications, problems = validate(inventory)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"doc-inventory: {exc}", file=sys.stderr)
        return 2

    for problem in problems:
        print(f"doc-inventory: {problem}", file=sys.stderr)
    if problems:
        print(f"doc-inventory FAILED: {len(problems)} issue(s)", file=sys.stderr)
        return 1

    if args.steady:
        transitional = [
            path for path, item in classifications.items()
            if item.disposition in {"merge", "investigate", "delete_candidate"}
        ]
        if transitional:
            for path in transitional:
                print(f"doc-inventory: transitional disposition remains: {path}", file=sys.stderr)
            return 1

    report(classifications, details=args.details)
    print("doc-inventory OK: every workspace Markdown file has one disposition")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
