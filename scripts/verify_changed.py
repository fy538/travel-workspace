#!/usr/bin/env python3
"""Select and run a conservative verification path for three independent repos.

This is the bounded local merge preflight. GitHub's selected DB/integration
checks and task-specific acceptance remain separate. Each repository requires
its own explicit base ref: a commit from one
repository is not meaningful in either of the other repositories.

Usage:
    scripts/verify-changed.sh \
      --workspace-base-ref origin/main \
      --agent-base-ref origin/main \
      --app-base-ref origin/main
"""

from __future__ import annotations

import argparse
import json
import re
import shlex
import subprocess
import sys
import os
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote, urlsplit

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent


def _child_repo_root(name: str) -> Path:
    """Use only this coordinated lane; never borrow a canonical sibling."""
    return WORKSPACE_ROOT / name


@dataclass(frozen=True)
class Repo:
    key: str
    display_name: str
    root: Path
    prefix: str


@dataclass(frozen=True)
class Prerequisite:
    key: str
    description: str


BACKEND_PYTHON = Prerequisite(
    "backend-python-313",
    "Python 3.13 with the travel-agent development test dependencies",
)
DISPOSABLE_POSTGRES = Prerequisite(
    "lane-disposable-postgres",
    "TEST_DATABASE_URL must target this isolated lane's local Postgres, with "
    "TEST_DATABASE_DISPOSABLE=1 and a database separate from the Compose dev database",
)
PYTEST_MARKER_INVENTORY = Prerequisite(
    "pytest-marker-inventory",
    "the selected pytest file must be readable so its database markers can be planned",
)

REPOSITORY_OFFLINE_PYTEST_ADDOPTS = (
    '-m "not requires_postgres and not requires_dogfood_wedge and not requires_api_keys"'
)


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

FLAG_REGISTRY_PATH = "docs/flags/registry.yaml"
APP_FLAG_SOURCE_PATH = "travel-app/constants/featureFlags.ts"
CURRENT_STATE_INPUT_PATHS = {
    "docs/openapi.json",
    "docs/journeys/STATUS.md",
    "docs/journeys/journeys.yaml",
    FLAG_REGISTRY_PATH,
    "docs/governance/inventory.yaml",
    "docs/release/v1-scope.yaml",
    "docs/status/current-state.md",
}


def _is_flag_registry_input(path: str) -> bool:
    if path in {FLAG_REGISTRY_PATH, APP_FLAG_SOURCE_PATH}:
        return True
    parts = path.split("/")
    return (
        path.startswith("travel-agent/backend/")
        and path.endswith(".py")
        and "tests" not in parts
        and "__pycache__" not in parts
    )


def _is_current_state_input(path: str) -> bool:
    return path in CURRENT_STATE_INPUT_PATHS


def _markdown_inventory_count_changed(
    files: list[str], workspace: Repo, base_ref: str | None
) -> bool:
    """Detect added/deleted docs Markdown because current-state reports its count."""

    if not base_ref:
        return False
    for path in files:
        if not (path.startswith("docs/") and path.endswith(".md")):
            continue
        base_entry = _git(
            workspace, ["cat-file", "-e", f"{base_ref}:{path}"], timeout=10
        )
        existed_at_base = base_entry.returncode == 0
        exists_now = (workspace.root / path).is_file()
        if existed_at_base != exists_now:
            return True
    return False


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


def _backend_test_python(repo: Repo) -> str:
    """Use the backend venv locally, or the already configured CI Python 3.13."""

    venv_python = repo.root / ".venv/bin/python"
    if venv_python.is_file():
        return str(venv_python)
    if sys.version_info[:2] == (3, 13):
        return sys.executable
    return "python3.13"


def _checker_test_prerequisites(repo: Repo, test_path: str) -> tuple[Prerequisite, ...]:
    if repo.key != "agent" or not test_path.endswith(".py"):
        return ()

    prerequisites = [BACKEND_PYTHON]
    try:
        source = (repo.root / test_path).read_text(encoding="utf-8")
    except OSError:
        prerequisites.append(PYTEST_MARKER_INVENTORY)
        return tuple(prerequisites)

    # Conservatively treat any use of the registered marker as a database
    # requirement. A false positive asks for an isolated DB; a false negative
    # could let the backend's collection guard be the first notice.
    if re.search(r"\brequires_postgres\b", source):
        prerequisites.append(DISPOSABLE_POSTGRES)
    return tuple(prerequisites)


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
    prerequisites: tuple[Prerequisite, ...] = ()

    @property
    def display(self) -> str:
        return shlex.join(self.argv)


@dataclass
class Selection:
    commands: list[Command] = field(default_factory=list)
    fallback_to_verify: bool = False
    fallback_reason: str | None = None

    def add(
        self,
        argv: tuple[str, ...],
        cwd: Path,
        reason: str,
        prerequisites: tuple[Prerequisite, ...] = (),
    ) -> None:
        command = Command(
            argv=argv, cwd=cwd, reason=reason, prerequisites=prerequisites
        )
        if command not in self.commands:
            self.commands.append(command)


def checker_test_command(
    workspace: Repo, repo: Repo, test_path: str, reason: str
) -> Command:
    """Build the canonical targeted-test command for a documented checker."""

    prerequisites = _checker_test_prerequisites(repo, test_path)
    if repo.key == "agent":
        python = _backend_test_python(repo)
        runner = workspace.root / "scripts/run_required_pytest.py"
        argv = (
            python,
            str(runner),
            "--cwd",
            str(repo.root),
            "--",
            python,
            "-m",
            "pytest",
            test_path,
        )
    else:
        argv = ("python3", "-m", "pytest", test_path)
    return Command(argv=argv, cwd=repo.root, reason=reason, prerequisites=prerequisites)


def select_commands(
    files: list[str],
    *,
    doc_texts: dict[str, str] | None = None,
    repositories: tuple[Repo, ...] | None = None,
    base_refs: dict[str, str] | None = None,
) -> Selection:
    """Route each affected repo once; child selectors own broad fallbacks."""

    repos = repositories or default_repositories()
    by_key = {repo.key: repo for repo in repos}
    workspace = by_key["workspace"]
    agent = by_key["agent"]
    app = by_key["app"]
    doc_texts = doc_texts or {}

    selection = Selection()
    frontend_files = [p for p in files if p.startswith("travel-app/")]
    backend_files = [p for p in files if p.startswith("travel-agent/")]
    workspace_files = [
        p for p in files if not p.startswith(("travel-app/", "travel-agent/"))
    ]
    docs_files = [p for p in workspace_files if p.endswith(".md")]
    base_refs = base_refs or {}
    for key, paths in (("app", frontend_files), ("agent", backend_files)):
        if paths and not base_refs.get(key):
            raise BaseRefError(f"{key}: explicit base required for merge selection")

    def prose_only(paths: list[str], prefix: str) -> bool:
        relative = [p.removeprefix(prefix) for p in paths]
        return all(
            p.endswith(".md")
            and (p.startswith("docs/") or p in {"README.md", "AGENTS.md", "CLAUDE.md"})
            for p in relative
        )

    # Run policy checks before broad suites so registry or generated-state
    # defects report early.
    if any(_is_flag_registry_input(path) for path in files):
        selection.add(
            ("make", "flag-registry-check"),
            workspace.root,
            "feature-flag registry, backend flag source, or canonical mobile flag source changed",
        )
    if any(
        _is_current_state_input(path) for path in files
    ) or _markdown_inventory_count_changed(
        files, workspace, base_refs.get("workspace")
    ):
        selection.add(
            ("make", "docs-status-check"),
            workspace.root,
            "generated current-state input or output changed",
        )

    if any(
        (path.startswith("travel-app/.maestro/") and path.endswith((".yaml", ".yml")))
        or path in {
            "docs/child-repos.ci-lock.json",
            "travel-app/package.json",
            "scripts/validate-maestro-flows.py",
            "travel-app/scripts/maestro/normalize-metadata.mjs",
        }
        for path in files
    ):
        selection.add(
            ("make", "maestro-flow-governance-check"),
            workspace.root,
            "Maestro flow policy or packaged child revision changed",
        )

    if frontend_files and not prose_only(frontend_files, "travel-app/"):
        selection.add(
            ("npm", "run", "verify:fast"),
            app.root,
            f"{len(frontend_files)} frontend file(s) changed",
        )
        selection.add(
            ("npm", "run", "verify:merge", "--", "--base", base_refs["app"]),
            app.root,
            "related tests + smoke + source-reading conventions; broad fallback when needed",
        )
    if backend_files and not prose_only(backend_files, "travel-agent/"):
        selection.add(
            ("make", "ci-static"),
            agent.root,
            "backend static checks",
        )
        python = (
            str(agent.root / ".venv/bin/python")
            if (agent.root / ".venv/bin/python").exists()
            else "python3"
        )
        selection.add(
            (python, "scripts/merge_scope.py", "--base", base_refs["agent"]),
            agent.root,
            "backend selected offline tests; selected database checks remain required in CI",
        )
    if any(not p.endswith(".md") for p in workspace_files):
        selection.add(
            ("python3", "-m", "pytest", "scripts/tests/", "-q"),
            workspace.root,
            "workspace tooling changes",
        )
    if any(not p.endswith(".md") for p in workspace_files) or any(
        p.startswith(
            (
                "travel-agent/backend/api/",
                "travel-agent/backend/core/",
                "travel-app/utils/api/",
            )
        )
        for p in files
    ):
        selection.add(
            (
                "make",
                "contract-check",
                "api-coverage-check",
                "compatibility-check",
                "card-arrival-check",
                "chat-card-types-check",
            ),
            workspace.root,
            "cross-repository contracts, not a repeat of both child suites",
        )
    if docs_files:
        selection.add(
            ("make", "docs-links-check", "docs-spine-check", "docs-canon-check"),
            workspace.root,
            f"{len(docs_files)} documentation file(s) changed",
        )
        for doc_file in (
            docs_files
            if not (
                frontend_files
                or backend_files
                or any(not p.endswith(".md") for p in workspace_files)
            )
            else []
        ):
            for repo, test_path in referenced_checker_tests(
                doc_texts.get(doc_file, ""), repos
            ):
                if test_path.endswith(".py"):
                    reason = (
                        f"{doc_file} references a checker covered by {test_path}"
                    )
                    command = checker_test_command(
                        workspace, repo, test_path, reason
                    )
                    selection.add(
                        command.argv,
                        command.cwd,
                        command.reason,
                        command.prerequisites,
                    )
                else:
                    selection.add(
                        ("node", "--test", test_path),
                        repo.root,
                        f"{doc_file} references a checker covered by {test_path}",
                    )
    return selection


def required_dependency_repositories(
    selection: Selection, repositories: tuple[Repo, ...] | None = None
) -> list[str]:
    """Return child dependency sets needed by the selected workspace commands."""

    repos = repositories or default_repositories()
    by_key = {repo.key: repo for repo in repos}
    required: set[str] = set()
    for command in selection.commands:
        if command.cwd == by_key["agent"].root:
            required.add("travel-agent")
        elif command.cwd == by_key["app"].root:
            required.add("travel-app")
        elif command.cwd == by_key["workspace"].root:
            if (
                command.argv
                and command.argv[0] == "make"
                and "contract-check" in command.argv
            ):
                required.update(("travel-agent", "travel-app"))
            if (
                command.argv
                and command.argv[0] == "make"
                and any(
                    gate in command.argv
                    for gate in ("flag-registry-check", "docs-status-check", "maestro-flow-governance-check")
                )
            ):
                # Policy gates parse YAML with PyYAML from the backend
                # development requirements. Maestro metadata also uses the
                # app YAML dependency; flag discovery needs only app source.
                required.add("travel-agent")
                if "maestro-flow-governance-check" in command.argv:
                    required.add("travel-app")
            if (
                command.argv
                and command.argv[0] in {"python", "python3"}
                and "pytest" in command.argv
            ):
                if any(
                    arg == "scripts/tests/" or arg.startswith("scripts/tests/")
                    for arg in command.argv
                ):
                    # Workspace tooling tests use PyYAML and backend contract imports
                    # supplied by the backend development environment.
                    required.add("travel-agent")
    return sorted(required)


# ── Independent Git repositories ──────────────────────────────────────────


class BaseRefError(Exception):
    pass


def _git(
    repo: Repo, args: list[str], *, timeout: int = 30
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo.root,
        env={
            k: v
            for k, v in os.environ.items()
            if k not in {"GIT_DIR", "GIT_WORK_TREE", "GIT_COMMON_DIR", "GIT_INDEX_FILE"}
        },
        capture_output=True,
        text=True,
        timeout=timeout,
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
            repo,
            ["rev-parse", "--verify", "--end-of-options", f"{base_ref}^{{commit}}"],
            timeout=10,
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
        ["diff", "--no-renames", "--name-only", "-z", f"{resolved_base_ref}...HEAD"],
        ["diff", "--no-renames", "--cached", "--name-only", "-z"],
        ["diff", "--no-renames", "--name-only", "-z"],
        ["ls-files", "--others", "--exclude-standard", "-z"],
    )
    found: set[str] = set()
    for args in commands:
        out = _git(repo, list(args))
        if out.returncode != 0:
            raise subprocess.CalledProcessError(
                out.returncode, ["git", *args], out.stdout, out.stderr
            )
        found.update(filter(None, out.stdout.split("\0")))
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


def _offline_marker_filter_active(environ: dict[str, str]) -> bool:
    """Recognize only the repository's explicit offline pytest filter."""

    try:
        args = shlex.split(environ.get("PYTEST_ADDOPTS", ""))
    except ValueError:
        return False
    # Pytest marker names are case-sensitive; repeated -m options and grouping
    # can change which tests run. Exempt only the repository's exact argv.
    return args == shlex.split(REPOSITORY_OFFLINE_PYTEST_ADDOPTS)



def _lane_postgres_prerequisite_error(
    workspace: Repo, environ: dict[str, str]
) -> str | None:
    test_url = environ.get("TEST_DATABASE_URL", "").strip()
    if not test_url or environ.get("TEST_DATABASE_DISPOSABLE") != "1":
        return "set TEST_DATABASE_URL and TEST_DATABASE_DISPOSABLE=1 for the selected database tests"
    if any(
        environ.get(key)
        for key in ("PGHOSTADDR", "PGSERVICE", "PGSERVICEFILE", "PGOPTIONS")
    ):
        return "unset libpq host/service/option overrides before selected database tests"
    try:
        target = urlsplit(test_url)
        port = target.port
    except ValueError:
        return "TEST_DATABASE_URL is malformed; its value is not printed"
    database = unquote(target.path.removeprefix("/")).strip()
    if (
        target.scheme not in {"postgresql", "postgresql+psycopg2"}
        or target.hostname not in {"localhost", "127.0.0.1", "::1"}
        or port is None
        or not database
        or database.lower() == "vesper"
        or target.query
        or target.fragment
    ):
        return (
            "TEST_DATABASE_URL must identify a loopback PostgreSQL database on this "
            "lane, without redirects, and use a database separate from the Compose dev database"
        )
    manifest_path = workspace.root / ".workspace-lane.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        runtime = manifest["runtime"]
        expected_port = int(runtime["postgres_port"])
    except (OSError, ValueError, KeyError, TypeError):
        return "this checkout has no valid isolated-lane Postgres assignment"
    if runtime.get("ownership") != "isolated" or port != expected_port:
        return "TEST_DATABASE_URL does not match this checkout's isolated Postgres port"
    return None


def _command_prerequisite_errors(
    command: Command,
    workspace: Repo,
    environ: dict[str, str] | None = None,
) -> list[str]:
    env = os.environ if environ is None else environ
    errors: list[str] = []
    for prerequisite in command.prerequisites:
        if prerequisite.key == BACKEND_PYTHON.key:
            try:
                version = subprocess.run(
                    [command.argv[0], "--version"],
                    capture_output=True,
                    text=True,
                    timeout=5,
                    check=False,
                )
            except (OSError, subprocess.TimeoutExpired) as exc:
                errors.append(f"Python 3.13 test interpreter is unavailable: {exc}")
                continue
            output = f"{version.stdout}\n{version.stderr}"
            if version.returncode != 0 or not re.search(r"\bPython 3\.13(?:\.|\b)", output):
                errors.append(
                    f"selected backend test interpreter is not a working Python 3.13: {command.argv[0]}"
                )
        elif prerequisite.key == DISPOSABLE_POSTGRES.key:
            if _offline_marker_filter_active(env):
                continue
            error = _lane_postgres_prerequisite_error(workspace, env)
            if error:
                errors.append(error)
        elif prerequisite.key == PYTEST_MARKER_INVENTORY.key:
            errors.append(
                "cannot inspect the selected pytest marker inventory; replan before execution"
            )
    return errors


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--workspace-base-ref")
    parser.add_argument("--agent-base-ref")
    parser.add_argument("--app-base-ref")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--workspace-only", action="store_true")
    parser.add_argument(
        "--plan-json",
        type=Path,
        help="write the selected commands and child dependency sets",
    )
    args = parser.parse_args(argv)

    repositories = default_repositories()
    base_refs = {
        "workspace": args.workspace_base_ref,
        "agent": args.agent_base_ref,
        "app": args.app_base_ref,
    }
    try:
        selected_repositories = (
            repositories[:1] if args.workspace_only else repositories
        )
        resolved, files = collect_changed_paths(base_refs, selected_repositories)
    except (BaseRefError, subprocess.CalledProcessError) as exc:
        print(f"verify-changed: {exc}", file=sys.stderr)
        return 2

    selection = select_commands(
        files,
        doc_texts=read_doc_texts(files, repositories),
        repositories=repositories,
        base_refs=resolved,
    )
    print("verify-changed: resolved bases")
    for repo in selected_repositories:
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
        for prerequisite in command.prerequisites:
            print(f"      prerequisite: {prerequisite.description}")
    if args.plan_json:
        args.plan_json.parent.mkdir(parents=True, exist_ok=True)
        plan = {
            "schema_version": 1,
            "dependencies": required_dependency_repositories(selection, repositories),
            "commands": [
                {
                    "cwd": str(command.cwd),
                    "argv": list(command.argv),
                    "reason": command.reason,
                    "prerequisites": [
                        {
                            "key": prerequisite.key,
                            "description": prerequisite.description,
                        }
                        for prerequisite in command.prerequisites
                    ],
                }
                for command in selection.commands
            ],
        }
        args.plan_json.write_text(json.dumps(plan, indent=2) + "\n", encoding="utf-8")
    if args.dry_run:
        return 0
    if selection.fallback_to_verify:
        return run_full_verify(
            next(repo for repo in repositories if repo.key == "workspace")
        )
    workspace = next(repo for repo in repositories if repo.key == "workspace")
    exit_code = 0
    tool_start_failed = False
    for command in selection.commands:
        prerequisite_errors = _command_prerequisite_errors(command, workspace)
        if prerequisite_errors:
            for error in prerequisite_errors:
                print(
                    f"verify-changed: blocked selected check {command.display}: {error}",
                    file=sys.stderr,
                )
            exit_code = 2
            continue
        if (
            any(p.key == DISPOSABLE_POSTGRES.key for p in command.prerequisites)
            and _offline_marker_filter_active(os.environ)
        ):
            print(
                "verify-changed: the explicit offline PYTEST_ADDOPTS filter excludes "
                "requires_postgres cases from this command; those database cases were "
                "not run here"
            )
        print(f"\n({command.cwd}) $ {command.display}")
        try:
            result = subprocess.run(command.argv, cwd=command.cwd).returncode
        except OSError as exc:
            print(
                f"verify-changed: could not start selected check {command.display} "
                f"in {command.cwd}: {exc}",
                file=sys.stderr,
            )
            tool_start_failed = True
            exit_code = 2
            continue
        if result != 0:
            exit_code = result
    return 2 if tool_start_failed else exit_code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
