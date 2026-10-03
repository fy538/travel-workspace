#!/usr/bin/env python3
"""Plan and run an opt-in narrow Reliability trial for roadmap prose PRs.

This pilot never replaces the required full Reliability jobs. A PR is eligible
only when its exact base is current protected main, its immutable child tuple
matches that successful base, and its diff contains only prose edits to the
four roadmap documents admitted by the October 1 measurement. Every uncertain
or unsupported condition returns the full scope.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

from verify_changed import (
    DISPOSABLE_POSTGRES,
    REPOSITORY_OFFLINE_PYTEST_ADDOPTS,
    _SCRIPT_REF_RE,
    _checker_test_candidates,
    checker_test_command,
    default_repositories,
    required_dependency_repositories,
    select_commands,
)

WORKSPACE_ROOT = Path(__file__).resolve().parents[1]
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
ADMITTED_ROADMAPS = frozenset(
    {
        "docs/working/vesper-program-roadmap.md",
        "docs/working/development-qa-research-and-roadmap-2026-09-30.md",
        "docs/working/artifact-experience-engineering-roadmap-2026-09-29.md",
        "docs/working/product-map/adaptive-context-and-research-roadmap-2026-09-29.md",
    }
)
CHILD_LOCK_PATH = "docs/child-repos.ci-lock.json"
CHECKER_TEST_OVERRIDES = {
    # This existing regression suite exercises the checker under its preserved-doc name.
    "check_doc_governance": ("workspace", "scripts/tests/test_preserved_doc_governance.py"),
}


class ScopeError(Exception):
    """A missing, invalid, or unsafe input that must retain full verification."""


def _clean_git_env() -> dict[str, str]:
    return {
        key: value
        for key, value in os.environ.items()
        if key not in {"GIT_DIR", "GIT_WORK_TREE", "GIT_COMMON_DIR", "GIT_INDEX_FILE"}
    }


def _git(
    cwd: Path, args: list[str], *, git_executable: str = "git", binary: bool = False
) -> str | bytes:
    try:
        result = subprocess.run(
            [git_executable, *args],
            cwd=cwd,
            env=_clean_git_env(),
            capture_output=True,
            text=not binary,
            check=False,
            timeout=15,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise ScopeError(f"Git history/tool unavailable: {exc}") from exc
    if result.returncode != 0:
        stderr = result.stderr.decode(errors="replace") if binary else result.stderr
        raise ScopeError(f"Git could not verify {args!r}: {stderr.strip()}")
    return result.stdout


def _resolve_commit(root: Path, ref: str, *, git_executable: str) -> str:
    if not isinstance(ref, str) or not SHA_RE.fullmatch(ref):
        raise ScopeError("The workspace base must be a full immutable commit SHA")
    value = _git(
        root,
        ["rev-parse", "--verify", f"{ref}^{{commit}}"],
        git_executable=git_executable,
    ).strip()
    if not SHA_RE.fullmatch(value):
        raise ScopeError("Git returned an invalid workspace commit identity")
    return value


def _lock_tuple(raw: str, *, label: str) -> dict[str, str]:
    try:
        value = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ScopeError(f"{label} child lock is invalid JSON") from exc
    if not isinstance(value, dict):
        raise ScopeError(f"{label} child lock is not an object")
    result: dict[str, str] = {}
    for repo in ("travel-agent", "travel-app"):
        sha = value.get(repo)
        if not isinstance(sha, str) or not SHA_RE.fullmatch(sha):
            raise ScopeError(f"{label} child lock has no immutable {repo} SHA")
        result[repo] = sha
    return result


def _read_front_matter(text: str) -> str:
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].rstrip("\r\n") != "---":
        raise ScopeError("A roadmap's lifecycle metadata is missing")
    for index in range(1, len(lines)):
        if lines[index].rstrip("\r\n") in {"---", "..."}:
            return "".join(lines[: index + 1])
    raise ScopeError("A roadmap's lifecycle metadata is malformed")


def _changed_entries(root: Path, base_sha: str, head_sha: str, git_executable: str):
    raw = _git(
        root,
        ["diff", "--name-status", "-z", "--no-renames", base_sha, head_sha],
        git_executable=git_executable,
    )
    assert isinstance(raw, str)
    fields = raw.split("\0")
    if fields and fields[-1] == "":
        fields.pop()
    if len(fields) % 2:
        raise ScopeError("Git returned an unreadable changed-file inventory")
    return list(zip(fields[::2], fields[1::2], strict=True))


def _tree_mode(
    root: Path, ref: str, path: str, *, git_executable: str
) -> str:
    raw = _git(
        root,
        ["ls-tree", "-z", ref, "--", path],
        git_executable=git_executable,
    )
    assert isinstance(raw, str)
    entries = [entry for entry in raw.split("\0") if entry]
    if len(entries) != 1:
        raise ScopeError(f"{path}: cannot establish a single file in {ref}")
    return entries[0].split("\t", 1)[0].split(" ", 1)[0]


def _workspace_dirty_paths(root: Path, *, git_executable: str) -> list[str]:
    status = _git(
        root,
        ["status", "--porcelain", "--untracked-files=all"],
        git_executable=git_executable,
    )
    assert isinstance(status, str)
    return [line[3:] for line in status.splitlines() if line]


def _candidate_identity(
    root: Path,
    tuple_path: Path,
    current_lock: dict[str, str],
    head_sha: str,
    *,
    git_executable: str,
) -> dict[str, str]:
    try:
        record = json.loads(tuple_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ScopeError(f"Candidate verification identity is unavailable: {exc}") from exc
    candidate = record.get("candidate") if isinstance(record, dict) else None
    tested = record.get("tested") if isinstance(record, dict) else None
    if not isinstance(candidate, dict) or not isinstance(tested, dict):
        raise ScopeError("Candidate verification identity is incomplete")
    expected = {"workspace": head_sha, **current_lock}
    dirty_workspace = [
        path
        for path in _workspace_dirty_paths(root, git_executable=git_executable)
        if path != "candidate-tuple.json"
    ]
    if dirty_workspace:
        raise ScopeError(
            f"Workspace checkout has uncommitted changes: {', '.join(dirty_workspace)}"
        )
    for repo, sha in expected.items():
        if candidate.get(repo) != sha or tested.get(repo) != sha:
            raise ScopeError(f"Candidate checkout identity does not match {repo}")
        repo_root = root if repo == "workspace" else root / repo
        actual = _git(
            repo_root,
            ["rev-parse", "HEAD"],
            git_executable=git_executable,
        ).strip()
        if actual != sha:
            raise ScopeError(f"Actual {repo} checkout does not match its tested identity")
        if repo != "workspace":
            dirty = _git(
                repo_root,
                ["status", "--porcelain"],
                git_executable=git_executable,
            ).strip()
            if dirty:
                raise ScopeError(f"{repo} checkout has uncommitted changes")
    return expected


def _checker_test_commands(
    docs: dict[str, str], repositories
) -> list[dict[str, Any]]:
    by_key = {repo.key: repo for repo in repositories}
    found: dict[tuple[str, str], dict[str, Any]] = {}
    for doc_path, text in docs.items():
        for name, ext in _SCRIPT_REF_RE.findall(text):
            if not any(
                (repo.root / "scripts" / f"{name}.{ext}").is_file()
                for repo in repositories
            ):
                raise ScopeError(
                    f"{doc_path} references unavailable checker {name}.{ext}"
                )
            candidates = list(
                (CHECKER_TEST_OVERRIDES[name],)
                if name in CHECKER_TEST_OVERRIDES
                else ()
            ) + [
                (repo_key, relative_path)
                for repo_key, relative_path in _checker_test_candidates(name, ext)
                if repo_key in by_key
                and (by_key[repo_key].root / relative_path).is_file()
            ]
            candidates = [
                (repo_key, relative_path)
                for repo_key, relative_path in candidates
                if repo_key in by_key
                and (by_key[repo_key].root / relative_path).is_file()
            ]
            for repo_key, test_path in candidates:
                repo = by_key[repo_key]
                reason = "run the existing test for a checker referenced by changed roadmap prose"
                if test_path.endswith(".py"):
                    command = checker_test_command(
                        by_key["workspace"], repo, test_path, reason
                    )
                    argv = command.argv
                    prerequisites = command.prerequisites
                else:
                    argv = ("node", "--test", test_path)
                    prerequisites = ()
                found[(repo_key, test_path)] = {
                    "repo": repo_key,
                    "argv": argv,
                    "reason": reason,
                    "prerequisites": prerequisites,
                }

    commands = []
    for repo_key, test_path in sorted(found):
        commands.append(found[(repo_key, test_path)])
    return commands


def _seal(plan: dict[str, Any]) -> dict[str, Any]:
    payload = copy.deepcopy(plan)
    payload.pop("plan_sha256", None)
    serialized = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    plan["plan_sha256"] = hashlib.sha256(serialized).hexdigest()
    return plan


def build_plan(
    *,
    root: Path = WORKSPACE_ROOT,
    base_ref: str,
    base_branch: str,
    event_name: str,
    main_ref: str,
    candidate_tuple_path: Path,
    git_executable: str = "git",
) -> dict[str, Any]:
    """Return a narrow plan only when every identity and scope check passes."""

    root = root.resolve()
    candidate_tuple_path = (
        candidate_tuple_path
        if candidate_tuple_path.is_absolute()
        else root / candidate_tuple_path
    )
    plan: dict[str, Any] = {
        "schema_version": 1,
        "scope": "full",
        "eligible": False,
        "reason": "not classified",
        "workspace_root": str(root),
        "base_workspace_sha": base_ref,
        "candidate": None,
        "changed_paths": [],
        "dependencies": [],
        "python_tests": False,
        "node_tests": False,
        "commands": [],
    }
    try:
        if event_name != "pull_request":
            raise ScopeError("Only a pull request can enter the roadmap scope pilot")
        if base_branch != "main":
            raise ScopeError("The pull request base is not protected main")
        if not shutil.which(git_executable):
            raise ScopeError("Git executable is missing")
        if not shutil.which("make") or not shutil.which("python3"):
            raise ScopeError("Required documentation checker tool is missing")

        base_sha = _resolve_commit(root, base_ref, git_executable=git_executable)
        main_sha = _git(
            root,
            ["rev-parse", "--verify", f"{main_ref}^{{commit}}"],
            git_executable=git_executable,
        ).strip()
        if main_sha != base_sha:
            raise ScopeError("PR base is not the current known-successful main commit")
        head_sha = _git(
            root, ["rev-parse", "HEAD"], git_executable=git_executable
        ).strip()
        if not SHA_RE.fullmatch(head_sha):
            raise ScopeError("Candidate workspace identity is invalid")
        ancestor = subprocess.run(
            [git_executable, "-C", str(root), "merge-base", "--is-ancestor", base_sha, head_sha],
            env=_clean_git_env(),
            capture_output=True,
            check=False,
            timeout=15,
        )
        if ancestor.returncode != 0:
            raise ScopeError("Base history is unavailable or is not an ancestor of the candidate")

        entries = _changed_entries(root, base_sha, head_sha, git_executable)
        if not entries:
            raise ScopeError("The candidate has no changed roadmap prose")
        changed_paths = [path for _status, path in entries]
        plan["changed_paths"] = changed_paths
        if any(status != "M" for status, _path in entries):
            raise ScopeError("Only modifications to existing roadmap files are eligible")
        if any(path not in ADMITTED_ROADMAPS for path in changed_paths):
            raise ScopeError("The diff includes a path outside the admitted roadmap set")

        base_lock_raw = _git(
            root,
            ["show", f"{base_sha}:{CHILD_LOCK_PATH}"],
            git_executable=git_executable,
        )
        base_lock = _lock_tuple(base_lock_raw, label="baseline")
        current_lock = _lock_tuple(
            (root / CHILD_LOCK_PATH).read_text(encoding="utf-8"), label="candidate"
        )
        if current_lock != base_lock:
            raise ScopeError("The immutable child repository tuple changed")
        identity = _candidate_identity(
            root,
            candidate_tuple_path,
            current_lock,
            head_sha,
            git_executable=git_executable,
        )

        docs: dict[str, str] = {}
        for path in changed_paths:
            if _tree_mode(root, base_sha, path, git_executable=git_executable) != "100644":
                raise ScopeError(f"{path}: baseline is not a regular Markdown file")
            if _tree_mode(root, head_sha, path, git_executable=git_executable) != "100644":
                raise ScopeError(f"{path}: candidate is not a regular Markdown file")
            old = _git(
                root,
                ["show", f"{base_sha}:{path}"],
                git_executable=git_executable,
            )
            candidate_path = root / path
            try:
                current = candidate_path.read_text(encoding="utf-8")
                old_metadata = _read_front_matter(old)
                current_metadata = _read_front_matter(current)
            except (OSError, UnicodeError, ScopeError) as exc:
                raise ScopeError(f"{path}: document evidence is unsafe: {exc}") from exc
            if old_metadata != current_metadata:
                raise ScopeError(f"{path}: lifecycle metadata changed")
            docs[path] = current

        repositories = default_repositories()
        by_key = {repo.key: repo for repo in repositories}
        selected = select_commands(
            changed_paths,
            doc_texts=docs,
            repositories=repositories,
        )
        if selected.fallback_to_verify:
            raise ScopeError("The existing changed-file selector requested full verification")
        referenced_tests = _checker_test_commands(docs, repositories)
        selected_signatures = {
            (repo.key, tuple(command.argv))
            for command in selected.commands
            for repo in repositories
            if command.cwd.resolve() == repo.root.resolve()
        }
        for required in referenced_tests:
            signature = (required["repo"], tuple(required["argv"]))
            if signature not in selected_signatures:
                selected.add(
                    tuple(required["argv"]),
                    by_key[required["repo"]].root,
                    required["reason"],
                    required["prerequisites"],
                )
                selected_signatures.add(signature)
        by_root = {repo.root.resolve(): repo.key for repo in repositories}
        commands: list[dict[str, Any]] = [
            {
                "repo": "workspace",
                "argv": ["python3", "scripts/check_doc_governance.py", "--new-since", base_sha],
                "reason": "preserve the Reliability new-document metadata guard",
            },
            {
                "repo": "workspace",
                "argv": ["make", "docs-inventory-check", "docs-status-check", "docs-child-governance-check"],
                "reason": "preserve document inventory, generated status, and child-document governance",
            },
        ]
        for command in selected.commands:
            repo_key = by_root.get(command.cwd.resolve())
            if repo_key is None:
                raise ScopeError("The existing selector chose a repository outside this lane")
            allowed = (
                command.argv[0] == "make"
                and set(command.argv[1:]).issubset(
                    {"docs-links-check", "docs-spine-check", "docs-canon-check"}
                )
            ) or (
                command.argv[0] == "python3"
                and "pytest" in command.argv
                and command.argv[-1].endswith(".py")
            ) or (
                repo_key == "agent"
                and len(command.argv) == 9
                and Path(command.argv[1]).resolve()
                == (by_key["workspace"].root / "scripts/run_required_pytest.py").resolve()
                and command.argv[2:5]
                == ("--cwd", str(by_key["agent"].root), "--")
                and command.argv[5:8] == (command.argv[0], "-m", "pytest")
                and command.argv[-1].endswith(".py")
            ) or (
                command.argv[0] == "node"
                and "--test" in command.argv
                and command.argv[-1].endswith((".mjs", ".js"))
            )
            if not allowed:
                raise ScopeError("The existing selector requested a non-roadmap check")
            planned = {
                "repo": repo_key,
                "argv": list(command.argv),
                "reason": command.reason,
                "prerequisites": [
                    {"key": prerequisite.key, "description": prerequisite.description}
                    for prerequisite in command.prerequisites
                ],
            }
            if any(
                prerequisite.key == DISPOSABLE_POSTGRES.key
                for prerequisite in command.prerequisites
            ):
                # The advisory prose pilot has no database service. Keep it
                # aligned with merge-ready's explicit offline subset and leave
                # database acceptance to the required Reliability checks.
                planned["environment"] = {
                    "PYTEST_ADDOPTS": REPOSITORY_OFFLINE_PYTEST_ADDOPTS
                }
            commands.append(planned)

        selected_tests = {
            (command["repo"], command["argv"][-1])
            for command in commands
            if "pytest" in command["argv"] or "--test" in command["argv"]
        }
        for required in referenced_tests:
            if (required["repo"], required["argv"][-1]) not in selected_tests:
                raise ScopeError(
                    "The changed-file selector omitted a referenced checker test"
                )

        dependencies = required_dependency_repositories(selected, repositories)
        plan.update(
            {
                "scope": "working-roadmap-prose",
                "eligible": True,
                "reason": "only admitted roadmap prose changed over the current protected-main child tuple",
                "base_workspace_sha": base_sha,
                "known_successful_baseline": {
                    "workspace": base_sha,
                    "travel-agent": base_lock["travel-agent"],
                    "travel-app": base_lock["travel-app"],
                    "evidence": "current protected main; full Contract and golden paths remains required during this pilot",
                },
                "candidate": identity,
                "changed_paths": changed_paths,
                "dependencies": dependencies,
                "python_tests": any("pytest" in command["argv"] for command in commands),
                "node_tests": any("--test" in command["argv"] for command in commands),
                "commands": commands,
            }
        )
    except (ScopeError, OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        plan["reason"] = str(exc)
    return _seal(plan)


def _verify_plan_integrity(plan: dict[str, Any]) -> None:
    supplied = plan.get("plan_sha256")
    payload = copy.deepcopy(plan)
    payload.pop("plan_sha256", None)
    serialized = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    actual = hashlib.sha256(serialized).hexdigest()
    if not isinstance(supplied, str) or supplied != actual:
        raise ScopeError("Scope plan identity is missing or has changed")


def run_plan(plan: dict[str, Any], *, root: Path = WORKSPACE_ROOT) -> int:
    _verify_plan_integrity(plan)
    if plan.get("scope") != "working-roadmap-prose" or plan.get("eligible") is not True:
        print(f"::error::Scope plan requires full Reliability: {plan.get('reason')}", file=sys.stderr)
        return 2
    root = root.resolve()
    if str(root) != plan.get("workspace_root"):
        print("::error::Plan belongs to a different workspace checkout", file=sys.stderr)
        return 2
    if _git(root, ["rev-parse", "HEAD"]).strip() != plan["candidate"]["workspace"]:
        print("::error::Candidate workspace changed after scope planning", file=sys.stderr)
        return 2
    dirty_workspace = [
        path
        for path in _workspace_dirty_paths(root, git_executable="git")
        if path != "candidate-tuple.json"
    ]
    if dirty_workspace:
        print("::error::Workspace checkout became dirty after scope planning", file=sys.stderr)
        return 2
    if _git(root, ["rev-parse", "--verify", "refs/remotes/origin/main^{commit}"]).strip() != plan["base_workspace_sha"]:
        print("::error::Known-successful main moved after scope planning", file=sys.stderr)
        return 2
    for repo in ("travel-agent", "travel-app"):
        checkout = root / repo
        if _git(checkout, ["rev-parse", "HEAD"]).strip() != plan["candidate"][repo]:
            print(f"::error::{repo} checkout changed after scope planning", file=sys.stderr)
            return 2
        if _git(checkout, ["status", "--porcelain"]).strip():
            print(f"::error::{repo} checkout became dirty after scope planning", file=sys.stderr)
            return 2
    try:
        current_lock = _lock_tuple(
            (root / CHILD_LOCK_PATH).read_text(encoding="utf-8"), label="candidate"
        )
        tuple_record = json.loads((root / "candidate-tuple.json").read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError, ScopeError) as exc:
        print(f"::error::Candidate verification identity changed after planning: {exc}", file=sys.stderr)
        return 2
    if current_lock != {key: plan["candidate"][key] for key in current_lock}:
        print("::error::Child lock changed after scope planning", file=sys.stderr)
        return 2
    tuple_groups = (
        tuple_record.get("candidate") if isinstance(tuple_record, dict) else None,
        tuple_record.get("tested") if isinstance(tuple_record, dict) else None,
    )
    if any(not isinstance(group, dict) for group in tuple_groups) or any(
        group.get(repo) != sha
        for group in tuple_groups
        if isinstance(group, dict)
        for repo, sha in plan["candidate"].items()
    ):
        print("::error::Candidate tuple changed after scope planning", file=sys.stderr)
        return 2

    for command in plan["commands"]:
        repo = command["repo"]
        if repo not in {"workspace", "agent", "app"}:
            print(f"::error::Invalid repository in scope plan: {repo}", file=sys.stderr)
            return 2
        cwd = root if repo == "workspace" else root / ("travel-agent" if repo == "agent" else "travel-app")
        argv = command["argv"]
        prerequisites = command.get("prerequisites", [])
        overrides = command.get("environment", {})
        if not isinstance(prerequisites, list) or not isinstance(overrides, dict):
            print("::error::Invalid prerequisites in roadmap scope plan", file=sys.stderr)
            return 2
        requires_postgres = any(
            isinstance(item, dict) and item.get("key") == DISPOSABLE_POSTGRES.key
            for item in prerequisites
        )
        command_env = None
        if requires_postgres:
            expected_overrides = {
                "PYTEST_ADDOPTS": REPOSITORY_OFFLINE_PYTEST_ADDOPTS
            }
            if overrides != expected_overrides:
                print(
                    "::error::Postgres-backed checker plan must declare the exact repository offline filter",
                    file=sys.stderr,
                )
                return 2
            command_env = dict(os.environ)
            command_env.update(expected_overrides)
            print(
                "[roadmap-scope] explicit offline pytest filter excludes requires_postgres cases; "
                "database cases were not run here"
            )
        elif overrides:
            print("::error::Unexpected environment override in roadmap scope plan", file=sys.stderr)
            return 2
        print(f"[roadmap-scope] ({repo}) {' '.join(argv)} — {command['reason']}")
        try:
            result = subprocess.run(argv, cwd=cwd, check=False, env=command_env)
        except OSError as exc:
            print(f"::error::Roadmap scope checker unavailable: {exc}", file=sys.stderr)
            return 127
        if result.returncode != 0:
            print(f"::error::Roadmap scope checker failed with exit code {result.returncode}", file=sys.stderr)
            return result.returncode
    print("Roadmap prose checks passed. Full required Reliability remains the acceptance gate.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-ref")
    parser.add_argument("--base-branch")
    parser.add_argument("--event-name")
    parser.add_argument("--main-ref", default="refs/remotes/origin/main")
    parser.add_argument("--candidate-tuple", type=Path)
    parser.add_argument("--plan-json", type=Path)
    parser.add_argument("--github-output", type=Path)
    parser.add_argument("--run-plan", type=Path)
    args = parser.parse_args(argv)

    if args.run_plan:
        try:
            plan = json.loads(args.run_plan.read_text(encoding="utf-8"))
            return run_plan(plan)
        except (OSError, json.JSONDecodeError, KeyError, ScopeError) as exc:
            print(f"::error::Cannot execute roadmap scope plan: {exc}", file=sys.stderr)
            return 2

    if not all((args.base_ref, args.base_branch, args.event_name, args.candidate_tuple, args.plan_json)):
        parser.error("planning requires --base-ref, --base-branch, --event-name, --candidate-tuple, and --plan-json")
    plan = build_plan(
        base_ref=args.base_ref,
        base_branch=args.base_branch,
        event_name=args.event_name,
        main_ref=args.main_ref,
        candidate_tuple_path=args.candidate_tuple,
    )
    args.plan_json.parent.mkdir(parents=True, exist_ok=True)
    args.plan_json.write_text(json.dumps(plan, indent=2) + "\n", encoding="utf-8")
    if args.github_output:
        deps = set(plan["dependencies"])
        with args.github_output.open("a", encoding="utf-8") as output:
            output.write(f"eligible={'true' if plan['eligible'] else 'false'}\n")
            output.write(f"travel_agent={'true' if 'travel-agent' in deps else 'false'}\n")
            output.write(f"travel_app={'true' if 'travel-app' in deps else 'false'}\n")
            output.write(f"python_tests={'true' if plan['python_tests'] else 'false'}\n")
            output.write(f"node_tests={'true' if plan['node_tests'] else 'false'}\n")
    print(json.dumps(plan, indent=2))
    if not plan["eligible"]:
        print(
            f"Roadmap scope fell back to full required Reliability: {plan['reason']}",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
