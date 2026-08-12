#!/usr/bin/env python3
"""Select and run a conservative verification path for three independent repos.

This is a local accelerator, never a replacement for the full pre-push/merge
gate. Each repository requires its own explicit base ref: a commit from one
repository is not meaningful in either of the other repositories.

Usage:
    scripts/verify-changed.sh \
      --workspace-base-ref origin/main \
      --agent-base-ref origin/main \
      --app-base-ref origin/main
"""

from __future__ import annotations

import argparse
import re
import shlex
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent


def _child_repo_root(name: str) -> Path:
    """Locate a child repo from either a normal or root-worktree checkout."""

    workspace_name = WORKSPACE_ROOT.name.split("--", maxsplit=1)[0]
    candidates = (
        WORKSPACE_ROOT / name,
        WORKSPACE_ROOT.parent / name,
        WORKSPACE_ROOT.parent / workspace_name / name,
    )
    for candidate in candidates:
        if (candidate / ".git").exists():
            return candidate
    return candidates[0]


@dataclass(frozen=True)
class Repo:
    key: str
    display_name: str
    root: Path
    prefix: str


def default_repositories() -> tuple[Repo, ...]:
    return (
        Repo("workspace", "workspace", WORKSPACE_ROOT, ""),
        Repo(
            "agent", "travel-agent", _child_repo_root("travel-agent"), "travel-agent/"
        ),
        Repo("app", "travel-app", _child_repo_root("travel-app"), "travel-app/"),
    )


# ── Path classification ──────────────────────────────────────────────────

HIGH_RISK_PATTERNS = [
    r"(^|/)conftest\.py$",
    r"(^|/)jest\.config\.[jt]s$",
    r"(^|/)pytest\.ini$",
    r"^travel-agent/pyproject\.toml$",
    r"^\.pre-commit-config\.yaml$",
    r"^travel-agent/\.pre-commit-config\.yaml$",
    r"^travel-app/\.pre-commit-config\.yaml$",
    r"(^|/)Makefile$",
    r"^travel-agent/alembic/versions/.*\.py$",
    r"^travel-agent/requirements.*\.txt$",
    r"^travel-app/package(-lock)?\.json$",
    r"^travel-app/poetry\.lock$",
    r"^scripts/.*\.(py|sh|mjs)$",
    r"^travel-agent/scripts/.*\.py$",
    r"^travel-app/scripts/.*\.(mjs|sh)$",
    r"^travel-agent/backend/api/routes/.*\.py$",
    r"^travel-agent/backend/core/models/.*\.py$",
    r"^docs/openapi.*\.json$",
    r"^travel-app/utils/api/schema\.gen\.ts$",
]
FRONTEND_PATTERN = r"^travel-app/.*\.(ts|tsx)$"
BACKEND_PATTERN = r"^travel-agent/.*\.py$"
DOCS_PATTERN = r"^docs/.*\.md$"

_HIGH_RISK_RE = [re.compile(pattern) for pattern in HIGH_RISK_PATTERNS]
_FRONTEND_RE = re.compile(FRONTEND_PATTERN)
_BACKEND_RE = re.compile(BACKEND_PATTERN)
_DOCS_RE = re.compile(DOCS_PATTERN)
_SCRIPT_REF_RE = re.compile(r"\b(check[-_][\w-]+)\.(py|mjs)\b")


def classify_path(path: str) -> str:
    for pattern in _HIGH_RISK_RE:
        if pattern.search(path):
            return "high_risk"
    if _FRONTEND_RE.match(path):
        return "frontend"
    if _BACKEND_RE.match(path):
        return "backend"
    if _DOCS_RE.match(path):
        return "docs"
    return "unknown"


def _checker_test_candidates(name: str, ext: str) -> tuple[tuple[str, str], ...]:
    return (
        ("workspace", f"scripts/{name}.test.{ext}"),
        ("agent", f"scripts/{name}.test.{ext}"),
        ("app", f"scripts/{name}.test.{ext}"),
        ("workspace", f"scripts/tests/test_{name}.py"),
        ("agent", f"tests/scripts/test_{name}.py"),
    )


def referenced_checker_tests(
    doc_text: str, repositories: tuple[Repo, ...]
) -> list[tuple[Repo, str]]:
    """Return real checker tests with their repository, not display-only hints."""

    by_key = {repo.key: repo for repo in repositories}
    found: set[tuple[str, str]] = set()
    for name, ext in _SCRIPT_REF_RE.findall(doc_text):
        for repo_key, relative_path in _checker_test_candidates(name, ext):
            repo = by_key.get(repo_key)
            if repo and (repo.root / relative_path).is_file():
                found.add((repo_key, relative_path))
    return [(by_key[key], path) for key, path in sorted(found)]


# ── Command selection ─────────────────────────────────────────────────────


@dataclass(frozen=True)
class Command:
    argv: tuple[str, ...]
    cwd: Path
    reason: str

    @property
    def display(self) -> str:
        return shlex.join(self.argv)


@dataclass
class Selection:
    commands: list[Command] = field(default_factory=list)
    fallback_to_verify: bool = False
    fallback_reason: str | None = None

    def add(self, argv: tuple[str, ...], cwd: Path, reason: str) -> None:
        command = Command(argv=argv, cwd=cwd, reason=reason)
        if command not in self.commands:
            self.commands.append(command)


def select_commands(
    files: list[str],
    *,
    doc_texts: dict[str, str] | None = None,
    repositories: tuple[Repo, ...] | None = None,
) -> Selection:
    """Select commands without running them. Unknown/high-risk stays full-gate."""

    repos = repositories or default_repositories()
    by_key = {repo.key: repo for repo in repos}
    workspace = by_key["workspace"]
    agent = by_key["agent"]
    app = by_key["app"]
    doc_texts = doc_texts or {}

    if not files:
        return Selection(
            fallback_to_verify=True, fallback_reason="no changed files resolved"
        )

    classes = {path: classify_path(path) for path in files}
    culprits = sorted(
        path for path, kind in classes.items() if kind in {"high_risk", "unknown"}
    )
    if culprits:
        return Selection(
            fallback_to_verify=True,
            fallback_reason=(
                f"{len(culprits)} unrecognized-or-high-risk file(s): {', '.join(culprits[:5])}"
                + (f" (+{len(culprits) - 5} more)" if len(culprits) > 5 else "")
            ),
        )

    selection = Selection()
    frontend_files = sorted(
        path for path, kind in classes.items() if kind == "frontend"
    )
    backend_files = sorted(path for path, kind in classes.items() if kind == "backend")
    docs_files = sorted(path for path, kind in classes.items() if kind == "docs")

    if frontend_files:
        selection.add(
            ("npm", "run", "verify:fast"),
            app.root,
            f"{len(frontend_files)} frontend file(s) changed",
        )
        related = tuple(path.removeprefix("travel-app/") for path in frontend_files)
        selection.add(
            ("npx", "jest", "--findRelatedTests", *related),
            app.root,
            "run tests related to changed frontend files",
        )
    if backend_files:
        selection.add(
            ("make", "ci"),
            agent.root,
            f"{len(backend_files)} backend file(s) changed — no dependency-to-test mapper exists",
        )
    if docs_files:
        selection.add(
            ("make", "docs-links-check", "docs-spine-check", "docs-canon-check"),
            workspace.root,
            f"{len(docs_files)} documentation file(s) changed",
        )
        for doc_file in docs_files:
            for repo, test_path in referenced_checker_tests(
                doc_texts.get(doc_file, ""), repos
            ):
                if test_path.endswith(".py"):
                    selection.add(
                        ("python3", "-m", "pytest", test_path),
                        repo.root,
                        f"{doc_file} references a checker covered by {test_path}",
                    )
                else:
                    selection.add(
                        ("node", "--test", test_path),
                        repo.root,
                        f"{doc_file} references a checker covered by {test_path}",
                    )
    return selection


# ── Independent Git repositories ──────────────────────────────────────────


class BaseRefError(Exception):
    pass


def _git(
    repo: Repo, args: list[str], *, timeout: int = 30
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args], cwd=repo.root, capture_output=True, text=True, timeout=timeout
    )


def resolve_base_ref(repo: Repo, base_ref: str | None) -> str:
    if not base_ref or not base_ref.strip():
        raise BaseRefError(
            f"{repo.display_name}: base ref is required — refusing to guess 'main'"
        )
    if not (repo.root / ".git").exists():
        raise BaseRefError(f"{repo.display_name}: not a Git repository at {repo.root}")
    try:
        out = _git(
            repo, ["rev-parse", "--verify", f"{base_ref}^{{commit}}"], timeout=10
        )
    except (subprocess.TimeoutExpired, FileNotFoundError, OSError) as exc:
        raise BaseRefError(
            f"{repo.display_name}: could not resolve {base_ref!r}: {exc}"
        ) from exc
    if out.returncode != 0:
        raise BaseRefError(
            f"{repo.display_name}: {base_ref!r} does not resolve to a commit: {out.stderr.strip()}"
        )
    return out.stdout.strip()


def changed_paths(repo: Repo, resolved_base_ref: str) -> list[str]:
    """Read committed, staged, unstaged, and untracked paths from one repo."""

    commands = (
        ["diff", "--name-only", f"{resolved_base_ref}...HEAD"],
        ["diff", "--cached", "--name-only"],
        ["diff", "--name-only"],
        ["ls-files", "--others", "--exclude-standard"],
    )
    found: set[str] = set()
    for args in commands:
        out = _git(repo, list(args))
        if out.returncode != 0:
            raise subprocess.CalledProcessError(
                out.returncode, ["git", *args], out.stdout, out.stderr
            )
        found.update(line.strip() for line in out.stdout.splitlines() if line.strip())
    return sorted(f"{repo.prefix}{path}" for path in found)


def collect_changed_paths(
    base_refs: dict[str, str], repositories: tuple[Repo, ...]
) -> tuple[dict[str, str], list[str]]:
    resolved: dict[str, str] = {}
    files: list[str] = []
    for repo in repositories:
        if repo.key not in base_refs:
            raise BaseRefError(f"{repo.display_name}: no base ref was provided")
        resolved[repo.key] = resolve_base_ref(repo, base_refs[repo.key])
        files.extend(changed_paths(repo, resolved[repo.key]))
    return resolved, sorted(set(files))


def read_doc_texts(files: list[str], repositories: tuple[Repo, ...]) -> dict[str, str]:
    workspace = next(repo for repo in repositories if repo.key == "workspace")
    texts: dict[str, str] = {}
    for path in files:
        if not path.startswith("docs/") or not path.endswith(".md"):
            continue
        candidate = workspace.root / path
        try:
            texts[path] = candidate.read_text(encoding="utf-8", errors="replace")
        except OSError:
            texts[path] = ""
    return texts


def run_full_verify(workspace: Repo) -> int:
    """Run the full gate only when the workspace checkout has both children."""

    if not (
        (workspace.root / "travel-agent").is_dir()
        and (workspace.root / "travel-app").is_dir()
    ):
        print(
            "verify-changed: full verification requires a coordinated workspace containing travel-agent/ and travel-app/; refusing to run a full gate against unrelated canonical checkouts.",
            file=sys.stderr,
        )
        return 2
    return subprocess.run(("make", "verify"), cwd=workspace.root).returncode


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--workspace-base-ref")
    parser.add_argument("--agent-base-ref")
    parser.add_argument("--app-base-ref")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    repositories = default_repositories()
    base_refs = {
        "workspace": args.workspace_base_ref,
        "agent": args.agent_base_ref,
        "app": args.app_base_ref,
    }
    try:
        resolved, files = collect_changed_paths(base_refs, repositories)
    except (BaseRefError, subprocess.CalledProcessError) as exc:
        print(f"verify-changed: {exc}", file=sys.stderr)
        return 2

    selection = select_commands(
        files, doc_texts=read_doc_texts(files, repositories), repositories=repositories
    )
    print("verify-changed: resolved bases")
    for repo in repositories:
        print(f"  {repo.display_name}: {base_refs[repo.key]} -> {resolved[repo.key]}")
    print(f"verify-changed: {len(files)} changed file(s)")
    for path in files:
        print(f"  {classify_path(path):10} {path}")
    print("\nselected commands:")
    if selection.fallback_to_verify:
        print(f"  [full gate: {selection.fallback_reason}]")
        print("    $ make verify")
    for command in selection.commands:
        print(f"  [{command.reason}]")
        print(f"    ({command.cwd}) $ {command.display}")
    if args.dry_run:
        return 0
    if selection.fallback_to_verify:
        return run_full_verify(
            next(repo for repo in repositories if repo.key == "workspace")
        )
    exit_code = 0
    for command in selection.commands:
        print(f"\n({command.cwd}) $ {command.display}")
        result = subprocess.run(command.argv, cwd=command.cwd).returncode
        if result != 0:
            exit_code = result
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
