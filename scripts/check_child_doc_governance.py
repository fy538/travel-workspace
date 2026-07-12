#!/usr/bin/env python3
"""Apply workspace new-document metadata policy to both child repositories."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml

from check_doc_governance import validate

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "docs/governance/child-baselines.yaml"


def git(repo: Path, *args: str) -> str:
    # Pre-push/pre-commit set GIT_DIR to the parent repo; clear those so
    # `git -C <child>` actually talks to the child repository.
    env = {
        key: value
        for key, value in __import__("os").environ.items()
        if key not in {"GIT_DIR", "GIT_WORK_TREE", "GIT_COMMON_DIR", "GIT_INDEX_FILE"}
    }
    result = subprocess.run(
        ["git", *args], cwd=repo, text=True, capture_output=True, check=False, env=env
    )
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    return result.stdout


def new_docs(repo: Path, docs_root: str, baseline: str) -> list[Path]:
    legacy = {
        line
        for line in git(
            repo, "-c", "core.quotePath=false", "ls-tree", "-r", "--name-only", baseline, "--", docs_root
        ).splitlines()
        if line.lower().endswith(".md")
    }
    tracked = git(repo, "-c", "core.quotePath=false", "ls-files", "--", docs_root)
    untracked = git(
        repo,
        "-c",
        "core.quotePath=false",
        "ls-files",
        "--others",
        "--exclude-standard",
        "--",
        docs_root,
    )
    current = {
        line for line in (tracked + untracked).splitlines() if line.lower().endswith(".md")
    }
    return [repo / path for path in sorted(current - legacy)]


def main() -> int:
    config = yaml.safe_load(CONFIG.read_text())
    findings = []
    checked = 0
    for name, item in config["repos"].items():
        repo = ROOT / name
        if not (repo / ".git").exists():
            print(f"child-doc-governance: missing child repository {name}", file=sys.stderr)
            return 2
        try:
            paths = new_docs(repo, item["docs_root"], item["baseline"])
        except RuntimeError as exc:
            print(f"child-doc-governance: {name}: {exc}", file=sys.stderr)
            return 2
        checked += len(paths)
        findings.extend((name, finding) for path in paths for finding in validate(path))
    for name, finding in findings:
        print(f"{name}/{finding.path.relative_to(ROOT / name)}: {finding.message}", file=sys.stderr)
    if findings:
        print(f"child-doc-governance FAILED: {len(findings)} issue(s)", file=sys.stderr)
        return 1
    print(f"child-doc-governance OK: {checked} post-baseline document(s) checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
