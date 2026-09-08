#!/usr/bin/env python3
"""Read-only, bounded orientation for the actual workspace/lane; never print env."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

ENV = {
    k: v
    for k, v in os.environ.items()
    if k not in {"GIT_DIR", "GIT_WORK_TREE", "GIT_COMMON_DIR", "GIT_INDEX_FILE"}
}


def git(path, *args):
    result = subprocess.run(
        ["git", "-C", str(path), *args],
        env=ENV,
        text=True,
        capture_output=True,
        timeout=5,
    )
    return result.stdout.strip() if result.returncode == 0 else None


def snapshot(root):
    repos = {}
    for name, path in [
        ("workspace", root),
        ("travel-agent", root / "travel-agent"),
        ("travel-app", root / "travel-app"),
    ]:
        if not (path / ".git").exists():
            repos[name] = {"path": str(path), "status": "missing independent checkout"}
            continue
        status = git(path, "status", "--porcelain")
        repos[name] = {
            "path": str(path),
            "branch": git(path, "branch", "--show-current") or "detached",
            "head": git(path, "rev-parse", "HEAD"),
            "dirty": None if status is None else bool(status),
            "changed_paths": (status or "").splitlines()[:12],
            "worktree_count": (
                git(path, "worktree", "list", "--porcelain") or ""
            ).count("worktree "),
        }
    return repos


def main():
    start = Path.cwd().resolve()
    root = next(
        (
            p
            for p in [start, *start.parents]
            if (p / "scripts/session-context.py").is_file()
            and (p / "docs/child-repos.ci-lock.json").is_file()
        ),
        None,
    )
    if root is None:
        print(
            "Workspace orientation unavailable: establish the coordinated workspace path.",
            file=sys.stderr,
        )
        return 1
    print(json.dumps(snapshot(root), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
