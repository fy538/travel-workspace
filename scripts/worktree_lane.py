#!/usr/bin/env python3
"""Create a coordinated workspace with real child checkouts; prepare before publish."""

from __future__ import annotations

import argparse
import json
import os
import re
import socket
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GIT_ENV = {
    k: v
    for k, v in os.environ.items()
    if k not in {"GIT_DIR", "GIT_WORK_TREE", "GIT_COMMON_DIR", "GIT_INDEX_FILE"}
}


def git(repo, *args, capture=True):
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        env=GIT_ENV,
        check=True,
        text=True,
        stdout=subprocess.PIPE if capture else None,
    ).stdout


def repository(path):
    # rev-parse alone would accept a non-repository subdirectory of ROOT.
    if (
        not (path / ".git").exists()
        or Path(git(path, "rev-parse", "--show-toplevel").strip()).resolve()
        != path.resolve()
    ):
        raise ValueError(f"Expected independent Git checkout: {path}")
    return path


def free_ports(count):
    sockets = []
    try:
        for _ in range(count):
            s = socket.socket()
            s.bind(("127.0.0.1", 0))
            sockets.append(s)
        return [s.getsockname()[1] for s in sockets]
    finally:
        for s in sockets:
            s.close()


def create(args):
    branch = args.prefix + args.name
    lane = (
        Path(args.directory).resolve()
        if args.directory
        else ROOT.parent / f"{ROOT.name}--{args.name}"
    )
    if lane.exists():
        raise ValueError(
            f"Lane path already exists; inspect it instead of silently reusing it: {lane}"
        )
    repos = [
        ("", ROOT),
        ("travel-agent", ROOT / "travel-agent"),
        ("travel-app", ROOT / "travel-app"),
    ]
    bases = {}
    for name, repo in repos:
        repository(repo)
        base = args.base or "HEAD"
        bases[name or "workspace"] = git(
            repo, "rev-parse", "--verify", f"{base}^{{commit}}"
        ).strip()
        # Fail before creating any lane if a requested branch already exists.
        if (
            subprocess.run(
                [
                    "git",
                    "-C",
                    str(repo),
                    "show-ref",
                    "--verify",
                    "--quiet",
                    f"refs/heads/{branch}",
                ],
                env=GIT_ENV,
            ).returncode
            == 0
        ):
            raise ValueError(f"{repo}: branch {branch} already exists")
    for name, repo in repos:
        target = lane / name if name else lane
        git(
            repo,
            "worktree",
            "add",
            "-b",
            branch,
            str(target),
            bases[name or "workspace"],
            capture=False,
        )
    pg, qr, grpc, api, expo = free_ports(5)
    runtime = {
        "schema_version": 1,
        "branch": branch,
        "bases": bases,
        "runtime": {
            "ownership": "isolated",
            "compose_project": "vesper-" + args.name.lower(),
            "postgres_port": pg,
            "qdrant_port": qr,
            "qdrant_grpc_port": grpc,
            "api_port": api,
            "expo_port": expo,
            "device": None,
        },
    }
    (lane / ".workspace-lane.json").write_text(json.dumps(runtime, indent=2) + "\n")
    print(
        f"Coordinated lane: {lane}\nInstall dependencies in its child checkouts; select one exclusive device before native work."
    )


def land(args):
    lane = (
        Path(args.directory).resolve()
        if args.directory
        else ROOT.parent / f"{ROOT.name}--{args.name}"
    )
    manifest = json.loads((lane / ".workspace-lane.json").read_text())
    expected = args.prefix + args.name
    if manifest["branch"] != expected:
        raise ValueError("Lane manifest branch does not match the requested branch")
    repos = [
        repository(lane),
        repository(lane / "travel-agent"),
        repository(lane / "travel-app"),
    ]
    for repo in repos:
        if git(repo, "branch", "--show-current").strip() != expected:
            raise ValueError(f"{repo}: expected branch {expected}")
        if git(repo, "status", "--porcelain").strip():
            raise ValueError(
                f"{repo}: commit or resolve lane changes before preparing delivery"
            )
        git(repo, "fetch", "origin", "main", capture=False)
        # Never mutate commit pins by rebasing one repository behind another's
        # back. Merge/rebase deliberately, update the tuple, and re-run this gate.
        if subprocess.run(
            [
                "git",
                "-C",
                str(repo),
                "merge-base",
                "--is-ancestor",
                "origin/main",
                "HEAD",
            ],
            env=GIT_ENV,
        ).returncode:
            raise ValueError(
                f"{repo}: integrate origin/main and refresh cross-repo pins before landing"
            )
    before = [git(r, "rev-parse", "HEAD").strip() for r in repos]
    subprocess.run(["make", "verify"], cwd=lane, env=GIT_ENV, check=True)
    for repo, revision in zip(repos, before):
        if (
            git(repo, "rev-parse", "HEAD").strip() != revision
            or git(repo, "status", "--porcelain").strip()
        ):
            raise ValueError(
                f"{repo}: verification changed the checked revision/tree; review and rerun"
            )
    if args.publish:
        # Protected main requires review. Publish only the checked lane branch;
        # preserve canonical checkouts and all worktrees for review/recovery.
        for repo in repos:
            git(
                repo,
                "push",
                "-u",
                "origin",
                f"HEAD:refs/heads/{expected}",
                capture=False,
            )
    print(
        "Coordinated gate passed. "
        + (
            "Lane branches published for PR review."
            if args.publish
            else "Use --publish to push these lane branches for PR review."
        )
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["create", "land"])
    parser.add_argument("name")
    parser.add_argument("--prefix", default="codex/")
    parser.add_argument(
        "--base",
        help="Explicit base used in each repository; default records each current HEAD",
    )
    parser.add_argument("--directory", help="Coordinated workspace destination")
    parser.add_argument(
        "--publish",
        action="store_true",
        help="After verification, publish branches for protected-main review",
    )
    args = parser.parse_args()
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,50}", args.name):
        parser.error(
            "name must use lowercase letters, digits, and hyphens (max 51 characters)"
        )
    try:
        (create if args.action == "create" else land)(args)
    except (ValueError, OSError, KeyError, subprocess.CalledProcessError) as exc:
        print(f"Lane operation incomplete: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
