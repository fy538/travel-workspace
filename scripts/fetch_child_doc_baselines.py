#!/usr/bin/env python3
"""Fetch only historical child-doc baseline trees into shallow checkouts."""
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
BASELINE_CONFIG = ROOT / "docs/governance/child-baselines.yaml"
CHILD_REPOS = ("travel-agent", "travel-app")
FULL_SHA = re.compile(r"[0-9a-f]{40}\Z")


def parse_baselines(text: str) -> dict[str, str]:
    """Read the narrow repos/baseline subset without requiring PyYAML in CI."""
    in_repos = False
    current: str | None = None
    entries: set[str] = set()
    baselines: dict[str, str] = {}

    for line_number, line in enumerate(text.splitlines(), start=1):
        if line == "repos:":
            if in_repos:
                raise ValueError(f"duplicate repos mapping at line {line_number}")
            in_repos = True
            continue
        if not in_repos:
            continue
        if line and not line.startswith((" ", "\t")):
            in_repos = False
            current = None
            continue

        entry = re.fullmatch(r"  ([a-z][a-z0-9-]*):", line)
        if entry:
            current = entry.group(1)
            if current in entries:
                raise ValueError(f"duplicate repository {current!r} at line {line_number}")
            entries.add(current)
            continue

        if current is not None and line.startswith("    baseline:"):
            if current in baselines:
                raise ValueError(
                    f"duplicate baseline for {current!r} at line {line_number}"
                )
            sha = line.removeprefix("    baseline:").strip()
            if not FULL_SHA.fullmatch(sha):
                raise ValueError(
                    f"invalid full commit SHA for {current!r} at line {line_number}"
                )
            baselines[current] = sha

    if entries != set(CHILD_REPOS):
        raise ValueError(
            f"expected exactly {sorted(CHILD_REPOS)} under repos, found {sorted(entries)}"
        )
    if set(baselines) != set(CHILD_REPOS):
        raise ValueError(
            f"missing baseline commit for {sorted(set(CHILD_REPOS) - set(baselines))}"
        )
    return baselines


def git(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    # Hooks can export the workspace repo's Git variables; strip them so -C
    # reliably operates on the child checkout.
    env = {
        key: value
        for key, value in os.environ.items()
        if key not in {"GIT_DIR", "GIT_WORK_TREE", "GIT_COMMON_DIR", "GIT_INDEX_FILE"}
    }
    result = subprocess.run(
        ["git", *args], cwd=repo, text=True, capture_output=True, check=False, env=env
    )
    if check and result.returncode:
        detail = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(detail or f"git {' '.join(args)} failed ({result.returncode})")
    return result


def ensure_baseline_tree(repo: Path, baseline: str) -> bool:
    """Ensure a baseline commit/tree exists; return whether a fetch was needed."""
    if not FULL_SHA.fullmatch(baseline):
        raise ValueError(f"invalid baseline commit SHA: {baseline!r}")
    original_head = git(repo, "rev-parse", "HEAD").stdout.strip()
    tree_expression = f"{baseline}^{{tree}}"
    tree_present = git(repo, "cat-file", "-e", tree_expression, check=False).returncode == 0
    if not tree_present:
        git(
            repo,
            "fetch",
            "--no-tags",
            "--filter=blob:none",
            "--depth=1",
            "origin",
            baseline,
        )
        if git(repo, "cat-file", "-e", tree_expression, check=False).returncode:
            raise RuntimeError(f"baseline tree {baseline} is still missing after fetch")
    current_head = git(repo, "rev-parse", "HEAD").stdout.strip()
    if current_head != original_head:
        raise RuntimeError(f"fetch changed {repo} HEAD from {original_head} to {current_head}")
    return not tree_present


def main() -> int:
    try:
        baselines = parse_baselines(BASELINE_CONFIG.read_text(encoding="utf-8"))
        fetched = []
        for name in CHILD_REPOS:
            repo = ROOT / name
            if not (repo / ".git").exists() and not (repo / ".git").is_file():
                raise RuntimeError(f"missing child repository {repo}")
            if ensure_baseline_tree(repo, baselines[name]):
                fetched.append(name)
        fetched_text = ", ".join(fetched) if fetched else "none; baseline trees already present"
        print(f"child-doc-baselines OK: {fetched_text}")
        return 0
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"child-doc-baselines FAILED: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
