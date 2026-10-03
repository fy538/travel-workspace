#!/usr/bin/env python3
"""Create, inspect, publish and safely retire coordinated workspace lanes."""

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
READONLY_GIT_ENV = {**GIT_ENV, "GIT_OPTIONAL_LOCKS": "0"}
PATCH_COMPARISON_LIMIT = 1000


def git(repo, *args, capture=True, env=GIT_ENV):
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        env=env,
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


def worktrees(repo):
    """Return Git's registered paths, including detached and unmanaged trees."""
    entries = []
    for block in git(repo, "worktree", "list", "--porcelain").split("\n\n"):
        fields = dict(
            line.split(" ", 1) if " " in line else (line, True)
            for line in block.splitlines()
            if line
        )
        if "worktree" in fields:
            entries.append(fields)
    return entries


def lane_repos(lane):
    return [
        ("workspace", lane, ROOT),
        ("travel-agent", lane / "travel-agent", ROOT / "travel-agent"),
        ("travel-app", lane / "travel-app", ROOT / "travel-app"),
    ]


def readonly_git(repo, *args):
    """Run a Git query without hiding its failure status or diagnostics."""
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        env=READONLY_GIT_ENV,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def adoption(repo, base_ref):
    """Compare a lane HEAD with a named, locally cached commit ref."""
    if not base_ref.startswith("refs/"):
        return {
            "ancestry": "unknown (base ref must be a full refs/... name)",
            "patches": "unknown (invalid base ref)",
        }
    format_check = readonly_git(repo, "check-ref-format", base_ref)
    if format_check.returncode:
        return {
            "ancestry": "unknown (invalid base ref)",
            "patches": "unknown (invalid base ref)",
        }
    ref = readonly_git(
        repo, "rev-parse", "--verify", "--quiet", f"{base_ref}^{{commit}}"
    )
    if ref.returncode:
        detail = ref.stderr.strip() or f"ref unavailable (exit {ref.returncode})"
        return {"ancestry": f"unknown ({detail})", "patches": "unknown (base ref unavailable)"}

    history = readonly_git(repo, "merge-base", "HEAD", base_ref)
    if history.returncode == 1:
        return {"ancestry": "unknown (no common history)", "patches": "unknown (no common history)"}
    if history.returncode:
        detail = history.stderr.strip() or f"history query failed (exit {history.returncode})"
        return {"ancestry": f"unknown ({detail})", "patches": f"unknown ({detail})"}

    ancestor = readonly_git(repo, "merge-base", "--is-ancestor", "HEAD", base_ref)
    if ancestor.returncode == 0:
        ancestry = "merged"
    elif ancestor.returncode == 1:
        ancestry = "not ancestor"
    else:
        detail = ancestor.stderr.strip() or f"ancestry query failed (exit {ancestor.returncode})"
        ancestry = f"unknown ({detail})"

    candidate_count = readonly_git(repo, "rev-list", "--count", f"{base_ref}..HEAD")
    if candidate_count.returncode:
        detail = candidate_count.stderr.strip() or (
            f"patch candidate count failed (exit {candidate_count.returncode})"
        )
        patches = f"unknown (patch query failed: {detail})"
    else:
        try:
            count = int(candidate_count.stdout.strip())
        except ValueError:
            patches = "unknown (Git returned an invalid patch candidate count)"
        else:
            if count > PATCH_COMPARISON_LIMIT:
                patches = (
                    f"unknown (patch comparison limit {PATCH_COMPARISON_LIMIT}; "
                    f"{count} candidate commits)"
                )
            else:
                comparison = readonly_git(repo, "cherry", "-v", base_ref, "HEAD")
                if comparison.returncode:
                    detail = comparison.stderr.strip() or (
                        f"patch query failed (exit {comparison.returncode})"
                    )
                    patches = f"unknown (patch query failed: {detail})"
                else:
                    equivalent, remaining = [], []
                    for line in comparison.stdout.splitlines():
                        fields = line.split(maxsplit=2)
                        if len(fields) < 2 or fields[0] not in {"-", "+"}:
                            continue
                        (equivalent if fields[0] == "-" else remaining).append(
                            fields[1][:12]
                        )
                    patches = {"equivalent": equivalent, "remaining": remaining}
    return {"ancestry": ancestry, "patches": patches}


def summarize_ids(ids, limit=5):
    shown = ", ".join(ids[:limit]) or "none"
    if len(ids) > limit:
        shown += f", and {len(ids) - limit} more"
    return f"{len(ids)} [{shown}]"


def status(args):
    base_ref = getattr(args, "base_ref", None) or "refs/remotes/origin/main"
    print(
        f"Adoption diagnostics use cached ref {base_ref} (no fetch); "
        "patch equivalence is informational only."
    )
    seen = set()
    for entry in worktrees(repository(ROOT)):
        lane = Path(entry["worktree"])
        if lane.resolve() == ROOT.resolve():
            continue
        seen.add(lane.resolve())
        manifest_path = lane / ".workspace-lane.json"
        if not manifest_path.is_file():
            print(f"Unmanaged worktree: {lane} ({entry.get('branch', 'detached')})")
            continue
        try:
            manifest = json.loads(manifest_path.read_text())
        except (OSError, json.JSONDecodeError) as exc:
            print(f"Lane with unreadable manifest: {lane}: {exc}")
            continue
        print(f"Lane: {lane}")
        print(f"  owner: {manifest.get('owner') or 'unspecified'}")
        print(f"  outcome: {manifest.get('outcome') or 'unspecified'}")
        for name, path, source in lane_repos(lane):
            try:
                repository(path)
                registered = any(
                    Path(item["worktree"]).resolve() == path.resolve()
                    for item in worktrees(repository(source))
                )
                head = git(path, "rev-parse", "--short", "HEAD").strip()
                dirty = bool(
                    git(path, "status", "--porcelain", env=READONLY_GIT_ENV).strip()
                )
                branch = git(path, "branch", "--show-current").strip() or "detached"
                remote = f"refs/remotes/origin/{branch}"
                published = subprocess.run(
                    [
                        "git", "-C", str(path), "show-ref", "--verify",
                        "--quiet", remote,
                    ],
                    env=GIT_ENV,
                    check=False,
                ).returncode == 0
                comparison = adoption(path, base_ref)
                patch_summary = comparison["patches"]
                if isinstance(patch_summary, dict):
                    patch_summary = (
                        "equivalent patches "
                        + summarize_ids(patch_summary["equivalent"])
                        + "; remaining patches "
                        + summarize_ids(patch_summary["remaining"])
                    )
                print(
                    f"  {name}: {head} {branch}, "
                    f"{'dirty (uncommitted changes excluded from patch comparison)' if dirty else 'clean'}, "
                    f"{'remote branch seen locally' if published else 'no local remote ref'}, "
                    f"ancestry vs {base_ref}: {comparison['ancestry']}, "
                    f"{patch_summary}, "
                    f"{'registered' if registered else 'not registered'}"
                )
            except (ValueError, OSError, subprocess.CalledProcessError) as exc:
                print(f"  {name}: unavailable ({exc})")
        print("  Remote PR and merge status: not checked")
    for name in ("travel-agent", "travel-app"):
        source = repository(ROOT / name)
        for entry in worktrees(source):
            path = Path(entry["worktree"]).resolve()
            if path == source.resolve() or path.parent in seen:
                continue
            print(f"Unpaired {name} worktree: {path} ({entry.get('branch', 'detached')})")


def create(args):
    branch = args.prefix + args.name
    lane = (
        Path(args.directory).resolve()
        if args.directory
        else ROOT.parent / f"{ROOT.name}--{args.name}"
    )
    if lane.exists() or lane.is_symlink():
        raise ValueError(
            f"Lane path already exists; inspect it instead of silently reusing it: {lane}"
        )
    if not lane.parent.is_dir():
        raise ValueError(f"Lane parent directory does not exist: {lane.parent}")
    branch_format = readonly_git(ROOT, "check-ref-format", "--branch", branch)
    if branch_format.returncode:
        raise ValueError(f"Invalid worktree branch name: {branch}")
    repos = [
        ("", ROOT),
        ("travel-agent", ROOT / "travel-agent"),
        ("travel-app", ROOT / "travel-app"),
    ]
    bases = {}
    targets = {}
    for name, repo in repos:
        repository(repo)
        base = args.base or "HEAD"
        bases[name or "workspace"] = git(
            repo, "rev-parse", "--verify", f"{base}^{{commit}}"
        ).strip()
        # Fail before creating any lane if a requested branch already exists.
        branch_check = readonly_git(
            repo, "show-ref", "--verify", "--quiet", f"refs/heads/{branch}"
        )
        if branch_check.returncode == 0:
            raise ValueError(f"{repo}: branch {branch} already exists")
        if branch_check.returncode != 1:
            detail = branch_check.stderr.strip() or f"Git exit {branch_check.returncode}"
            raise ValueError(f"Could not check branch {branch} in {repo}: {detail}")
        targets[name or "workspace"] = lane / name if name else lane

    # Runtime prerequisites must succeed before the first worktree or branch is
    # created. A denied allocator therefore leaves every repository untouched.
    try:
        ports = free_ports(5)
        if (
            not isinstance(ports, (list, tuple))
            or len(ports) != 5
            or any(
                not isinstance(port, int) or not 1 <= port <= 65535
                for port in ports
            )
            or len(set(ports)) != 5
        ):
            raise ValueError("allocator returned invalid or duplicate ports")
    except Exception as exc:
        raise ValueError(
            f"Runtime allocation failed before worktree creation; no worktrees or "
            f"branches were created: {exc}"
        ) from exc

    completed = []
    for name, repo in repos:
        key = name or "workspace"
        target = targets[key]
        try:
            git(
                repo,
                "worktree",
                "add",
                "-b",
                branch,
                str(target),
                bases[key],
                capture=False,
            )
        except (OSError, subprocess.CalledProcessError) as exc:
            prior = "; ".join(
                f"{item['repo']} path={item['path']} branch={item['branch']}"
                for item in completed
            ) or "none"
            raise ValueError(
                f"Creation failed at stage {key} for path={target} branch={branch}: {exc}. "
                f"Completed worktrees preserved: {prior}. The failed stage may also have "
                "left partial artifacts; inspect its path and branch. No automatic cleanup "
                "was attempted. Recovery: inspect git worktree list/status in each repo, "
                "resolve or manually remove reviewed artifacts, then retry."
            ) from exc
        completed.append({"repo": key, "path": target, "branch": branch})

    pg, qr, grpc, api, expo = ports
    runtime = {
        "schema_version": 1,
        "branch": branch,
        "bases": bases,
        "owner": getattr(args, "owner", None),
        "outcome": getattr(args, "outcome", None),
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
    manifest_path = lane / ".workspace-lane.json"
    try:
        with manifest_path.open("x") as manifest_file:
            json.dump(runtime, manifest_file, indent=2)
            manifest_file.write("\n")
    except (OSError, ValueError, TypeError) as exc:
        preserved = "; ".join(
            f"{item['repo']} path={item['path']} branch={item['branch']}"
            for item in completed
        )
        raise ValueError(
            f"Creation failed at stage manifest write ({manifest_path}): {exc}. "
            f"Completed worktrees preserved: {preserved}. No automatic cleanup was "
            "attempted. Recovery: inspect the manifest path and all three worktrees, "
            "repair or remove reviewed artifacts manually, then retry."
        ) from exc
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
    subprocess.run(
        ["make", "verify-changed", "WORKSPACE_BASE_REF=origin/main",
         "AGENT_BASE_REF=origin/main", "APP_BASE_REF=origin/main"],
        cwd=lane, env=GIT_ENV, check=True,
    )
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


def retire(args):
    """Remove only a fully merged, clean coordinated lane; preview by default."""
    lane = (
        Path(args.directory).resolve()
        if args.directory
        else ROOT.parent / f"{ROOT.name}--{args.name}"
    )
    if lane == ROOT.resolve() or not lane.is_dir():
        raise ValueError(f"Expected an existing noncanonical lane: {lane}")
    manifest = json.loads((lane / ".workspace-lane.json").read_text())
    expected = args.prefix + args.name
    if manifest.get("branch") != expected:
        raise ValueError("Lane manifest branch does not match the requested branch")

    checked = []
    for name, path, source in lane_repos(lane):
        repository(path)
        source = repository(source)
        if not any(
            Path(item["worktree"]).resolve() == path.resolve()
            for item in worktrees(source)
        ):
            raise ValueError(f"{name}: lane is not a registered worktree")
        if git(path, "branch", "--show-current").strip() != expected:
            raise ValueError(f"{name}: expected branch {expected}")
        if git(path, "status", "--porcelain", "--untracked-files=all").strip():
            raise ValueError(f"{name}: tracked or untracked changes need review")
        ignored = [
            item
            for item in git(
                path, "ls-files", "--others", "--ignored",
                "--exclude-standard", "--directory", "-z",
            ).split("\0")
            if item
            and not (
                name == "workspace"
                and item in {".workspace-lane.json", "travel-agent/", "travel-app/"}
            )
        ]
        if ignored:
            raise ValueError(f"{name}: ignored files need review: {ignored[:8]}")
        git(path, "fetch", "--quiet", "origin", "main", capture=False)
        tip = git(path, "rev-parse", "HEAD").strip()
        remote_tip = git(
            path, "ls-remote", "--heads", "origin", f"refs/heads/{expected}"
        ).strip()
        if remote_tip and remote_tip.split()[0] != tip:
            raise ValueError(f"{name}: remote branch has moved beyond local {tip}")
        if subprocess.run(
            [
                "git", "-C", str(path), "merge-base", "--is-ancestor",
                tip, "refs/remotes/origin/main",
            ],
            env=GIT_ENV,
            check=False,
        ).returncode:
            raise ValueError(f"{name}: {tip} is not merged into origin/main")
        checked.append((name, path, source, tip))

    print(f"Eligible for retirement: {lane}")
    for name, _, _, tip in checked:
        print(f"  {name}: {tip} is merged into fetched origin/main")
    if not args.apply:
        print("Dry run only. Stop this lane's runtime, then use --apply --runtime-stopped.")
        return
    if not args.runtime_stopped:
        raise ValueError("Confirm the lane runtime is stopped with --runtime-stopped")
    # Recheck all trees before the first removal. Partial cleanup can be resumed
    # manually; this command never force-removes a checkout or a branch.
    for name, path, _, tip in checked:
        if git(path, "rev-parse", "HEAD").strip() != tip:
            raise ValueError(f"{name}: branch tip changed after review")
        if git(path, "status", "--porcelain", "--untracked-files=all").strip():
            raise ValueError(f"{name}: tree changed after review")
    for name, path, source, tip in reversed(checked):
        git(source, "worktree", "remove", str(path), capture=False)
        git(source, "update-ref", "-d", f"refs/heads/{expected}", tip, capture=False)
        print(f"Retired {name}: {path}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["create", "land", "status", "retire"])
    parser.add_argument("name", nargs="?")
    parser.add_argument("--prefix", default="codex/")
    parser.add_argument(
        "--base",
        help="Explicit base used in each repository; default records each current HEAD",
    )
    parser.add_argument("--directory", help="Coordinated workspace destination")
    parser.add_argument(
        "--base-ref",
        default="refs/remotes/origin/main",
        help="Named local ref for read-only status adoption checks (no fetch)",
    )
    parser.add_argument("--owner", help="Person or task responsible for landing this lane")
    parser.add_argument("--outcome", help="Bounded result this lane will deliver")
    parser.add_argument(
        "--publish",
        action="store_true",
        help="After verification, publish branches for protected-main review",
    )
    parser.add_argument(
        "--apply", action="store_true", help="Retire after all safety checks"
    )
    parser.add_argument(
        "--runtime-stopped", action="store_true",
        help="Acknowledge the lane's services and device session are stopped",
    )
    args = parser.parse_args()
    if args.action != "status" and not args.name:
        parser.error("name is required for create, land and retire")
    if args.name and not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,50}", args.name):
        parser.error(
            "name must use lowercase letters, digits, and hyphens (max 51 characters)"
        )
    try:
        actions = {"create": create, "land": land, "status": status, "retire": retire}
        actions[args.action](args)
    except (ValueError, OSError, KeyError, subprocess.CalledProcessError) as exc:
        print(f"Lane operation incomplete: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
