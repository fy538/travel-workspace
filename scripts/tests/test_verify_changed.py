from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from types import SimpleNamespace
from pathlib import Path

import pytest

MODULE_PATH = Path(__file__).resolve().parents[1] / "verify_changed.py"
SPEC = importlib.util.spec_from_file_location("verify_changed", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def _git(repo: Path, *args: str) -> None:
    subprocess.run(("git", *args), cwd=repo, check=True, capture_output=True, text=True)


def _init_repo(tmp_path: Path, name: str, filename: str, contents: str) -> Path:
    repo = tmp_path / name
    repo.mkdir()
    _git(repo, "init", "-q")
    _git(repo, "config", "user.email", "verify@example.test")
    _git(repo, "config", "user.name", "Verify Test")
    path = repo / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(contents)
    _git(repo, "add", filename)
    _git(repo, "commit", "-qm", "base")
    return repo


def _repositories(tmp_path: Path) -> tuple[MODULE.Repo, ...]:
    workspace = _init_repo(tmp_path, "workspace", "docs/working/note.md", "base\n")
    agent = _init_repo(tmp_path, "travel-agent", "backend/example.py", "x = 1\n")
    app = _init_repo(
        tmp_path, "travel-app", "components/example.tsx", "export const x = 1;\n"
    )
    return (
        MODULE.Repo("workspace", "workspace", workspace, ""),
        MODULE.Repo("agent", "travel-agent", agent, "travel-agent/"),
        MODULE.Repo("app", "travel-app", app, "travel-app/"),
    )


def _base_refs() -> dict[str, str]:
    return {"workspace": "HEAD", "agent": "HEAD", "app": "HEAD"}


def _lane_postgres_manifest(workspace: Path, port: int = 50568) -> None:
    (workspace / ".workspace-lane.json").write_text(
        json.dumps({"runtime": {"ownership": "isolated", "postgres_port": port}})
    )


# ── Classification and selection ─────────────────────────────────────────


def test_classifies_every_path_class() -> None:
    assert MODULE.classify_path("travel-app/components/Foo.tsx") == "frontend"
    assert MODULE.classify_path("travel-agent/backend/concierge/agent.py") == "backend"
    assert MODULE.classify_path("docs/working/note.md") == "docs"
    assert MODULE.classify_path("travel-agent/alembic/versions/a.py") == "high_risk"
    assert MODULE.classify_path("assets/logo.png") == "unknown"


def test_selects_executable_checker_test_for_referenced_document(
    tmp_path: Path,
) -> None:
    repos = _repositories(tmp_path)
    checker_test = repos[1].root / "tests/scripts/test_check_foo.py"
    checker_test.parent.mkdir(parents=True)
    checker_test.write_text("")
    backend_python = repos[1].root / ".venv/bin/python"
    backend_python.parent.mkdir(parents=True)
    backend_python.write_text("backend test interpreter placeholder\n")
    selection = MODULE.select_commands(
        ["docs/working/note.md"],
        doc_texts={"docs/working/note.md": "Run check_foo.py after edits."},
        repositories=repos,
    )
    assert not selection.fallback_to_verify
    command = next(
        command
        for command in selection.commands
        if command.cwd == repos[1].root and "pytest" in command.argv
    )
    assert command.argv == (
        str(backend_python),
        str(repos[0].root / "scripts/run_required_pytest.py"),
        "--cwd",
        str(repos[1].root),
        "--",
        str(backend_python),
        "-m",
        "pytest",
        "tests/scripts/test_check_foo.py",
    )
    assert command.prerequisites == (MODULE.BACKEND_PYTHON,)
    assert not any(command.display.startswith("<run") for command in selection.commands)


def test_mixed_checker_plan_exposes_disposable_postgres_prerequisite(
    tmp_path: Path,
) -> None:
    repos = _repositories(tmp_path)
    checker_test = repos[1].root / "tests/scripts/test_check_foo.py"
    checker_test.parent.mkdir(parents=True)
    checker_test.write_text(
        "from tests.conftest import requires_postgres\n"
        "@requires_postgres\n"
        "def test_database_case(): pass\n"
    )
    backend_python = repos[1].root / ".venv/bin/python"
    backend_python.parent.mkdir(parents=True)
    backend_python.write_text("backend test interpreter placeholder\n")

    selection = MODULE.select_commands(
        ["docs/working/note.md"],
        doc_texts={"docs/working/note.md": "Run check_foo.py after edits."},
        repositories=repos,
        base_refs={"workspace": "base", "agent": "base"},
    )

    command = next(
        command
        for command in selection.commands
        if command.cwd == repos[1].root and "pytest" in command.argv
    )
    assert command.prerequisites == (
        MODULE.BACKEND_PYTHON,
        MODULE.DISPOSABLE_POSTGRES,
    )
    assert MODULE.required_dependency_repositories(selection, repos) == [
        "travel-agent"
    ]


def test_shared_app_change_delegates_to_app_and_contracts_not_backend_suite() -> None:
    selection = MODULE.select_commands(
        ["travel-app/utils/api/schema.gen.ts"], base_refs={"app": "abc"}
    )
    assert not selection.fallback_to_verify
    assert any("verify:merge" in command.argv for command in selection.commands)
    assert any("contract-check" in command.argv for command in selection.commands)
    assert not any(command.argv == ("make", "ci") for command in selection.commands)


def test_flag_sources_select_registry_gate_and_keep_general_app_edits_out(
    tmp_path: Path,
) -> None:
    repos = _repositories(tmp_path)
    selection = MODULE.select_commands(
        [
            "docs/flags/registry.yaml",
            "travel-agent/backend/core/feature_flags.py",
            "travel-app/constants/featureFlags.ts",
        ],
        repositories=repos,
        base_refs={"agent": "HEAD", "app": "HEAD"},
    )
    assert any(
        command.argv == ("make", "flag-registry-check")
        for command in selection.commands
    )
    assert any(
        command.argv == ("make", "docs-status-check") for command in selection.commands
    )
    assert MODULE.required_dependency_repositories(selection, repos) == [
        "travel-agent",
        "travel-app",
    ]

    ordinary_app = MODULE.select_commands(
        ["travel-app/components/example.tsx"],
        repositories=repos,
        base_refs={"app": "HEAD"},
    )
    assert not any(
        command.argv == ("make", "flag-registry-check")
        for command in ordinary_app.commands
    )

    backend_test = MODULE.select_commands(
        ["travel-agent/backend/tests/test_flags.py"],
        repositories=repos,
        base_refs={"agent": "HEAD"},
    )
    assert not any(
        command.argv == ("make", "flag-registry-check")
        for command in backend_test.commands
    )


def test_policy_gates_precede_broader_suites_for_mixed_flag_changes(
    tmp_path: Path,
) -> None:
    repos = _repositories(tmp_path)
    selection = MODULE.select_commands(
        ["docs/flags/registry.yaml", "travel-app/constants/featureFlags.ts"],
        repositories=repos,
        base_refs={"workspace": "HEAD", "app": "HEAD"},
    )

    gate_positions = [
        index
        for index, command in enumerate(selection.commands)
        if command.argv
        and command.argv[0] == "make"
        and command.argv[1] in {"flag-registry-check", "docs-status-check"}
    ]
    broad_positions = [
        index
        for index, command in enumerate(selection.commands)
        if "verify:merge" in command.argv or "scripts/tests/" in command.argv
    ]

    assert len(gate_positions) == 2
    assert broad_positions
    assert max(gate_positions) < min(broad_positions)


def test_generated_current_state_sources_select_status_gate_and_backend_dependencies(
    tmp_path: Path,
) -> None:
    repos = _repositories(tmp_path)
    selection = MODULE.select_commands(
        ["docs/status/current-state.md"],
        repositories=repos,
        base_refs={"workspace": "HEAD"},
    )
    assert any(
        command.argv == ("make", "docs-status-check") for command in selection.commands
    )
    assert not any(
        command.argv == ("make", "flag-registry-check")
        for command in selection.commands
    )
    assert MODULE.required_dependency_repositories(selection, repos) == ["travel-agent"]


@pytest.mark.parametrize(
    ("path", "present_now"),
    [("docs/working/added.md", True), ("docs/working/note.md", False)],
)
def test_added_or_deleted_markdown_selects_current_state_gate(
    tmp_path: Path, path: str, present_now: bool
) -> None:
    repos = _repositories(tmp_path)
    candidate = repos[0].root / path
    if present_now:
        candidate.parent.mkdir(parents=True, exist_ok=True)
        candidate.write_text("new workspace document\n")
    else:
        candidate.unlink()

    selection = MODULE.select_commands(
        [path], repositories=repos, base_refs={"workspace": "HEAD"}
    )

    assert any(
        command.argv == ("make", "docs-status-check") for command in selection.commands
    )


def test_unknown_workspace_input_runs_workspace_tests_and_contracts():
    selection = MODULE.select_commands(["new-policy.json"])
    assert any("scripts/tests/" in c.argv for c in selection.commands)
    assert any("contract-check" in c.argv for c in selection.commands)


def test_dependency_plan_skips_child_installs_for_workspace_docs(
    tmp_path: Path,
) -> None:
    repos = _repositories(tmp_path)
    selection = MODULE.select_commands(
        ["docs/working/note.md"],
        doc_texts={
            "docs/working/note.md": "A prose-only note with no checker references."
        },
        repositories=repos,
        base_refs={"workspace": "HEAD"},
    )
    assert MODULE.required_dependency_repositories(selection, repos) == []


def test_dependency_plan_matches_selected_child_and_cross_repo_checks(
    tmp_path: Path,
) -> None:
    repos = _repositories(tmp_path)
    backend = MODULE.select_commands(
        ["travel-agent/backend/example.py"],
        repositories=repos,
        base_refs={"agent": "HEAD"},
    )
    assert MODULE.required_dependency_repositories(backend, repos) == ["travel-agent"]

    workspace = MODULE.select_commands(["new-policy.json"], repositories=repos)
    assert MODULE.required_dependency_repositories(workspace, repos) == [
        "travel-agent",
        "travel-app",
    ]

    workspace_policy = MODULE.Selection()
    workspace_policy.add(("make", "flag-registry-check"), repos[0].root, "flag policy")
    workspace_policy.add(
        ("make", "docs-status-check"), repos[0].root, "generated state"
    )
    assert MODULE.required_dependency_repositories(workspace_policy, repos) == [
        "travel-agent"
    ]


def test_child_selection_rejects_missing_base():
    with pytest.raises(MODULE.BaseRefError):
        MODULE.select_commands(["travel-agent/backend/home/feed.py"])


# ── Independent repository discovery ─────────────────────────────────────


def test_collect_changed_paths_reads_committed_changes_from_each_repo(
    tmp_path: Path,
) -> None:
    repos = _repositories(tmp_path)
    base_refs = {repo.key: MODULE.resolve_base_ref(repo, "HEAD") for repo in repos}
    for repo, filename, contents in (
        (repos[0], "docs/working/note.md", "workspace committed\n"),
        (repos[1], "backend/example.py", "agent committed\n"),
        (repos[2], "components/example.tsx", "app committed\n"),
    ):
        (repo.root / filename).write_text(contents)
        _git(repo.root, "add", filename)
        _git(repo.root, "commit", "-qm", "changed")

    resolved, paths = MODULE.collect_changed_paths(base_refs, repos)

    assert set(resolved) == {"workspace", "agent", "app"}
    assert paths == [
        "docs/working/note.md",
        "travel-agent/backend/example.py",
        "travel-app/components/example.tsx",
    ]


def test_final_candidate_retains_earlier_shared_app_change_after_local_edit(
    tmp_path: Path,
) -> None:
    repos = _repositories(tmp_path)
    bases = {repo.key: MODULE.resolve_base_ref(repo, "HEAD") for repo in repos}
    app = repos[2]

    shared = app.root / "utils/api/shared.ts"
    shared.parent.mkdir(parents=True)
    shared.write_text("export const shared = true;\n")
    _git(app.root, "add", "utils/api/shared.ts")
    _git(app.root, "commit", "-qm", "shared API change")
    local = app.root / "components/example.tsx"
    local.write_text("export const x = 2;\n")
    _git(app.root, "add", "components/example.tsx")
    _git(app.root, "commit", "-qm", "later local change")

    resolved, files = MODULE.collect_changed_paths(bases, repos)
    assert "travel-app/utils/api/shared.ts" in files
    assert "travel-app/components/example.tsx" in files
    selection = MODULE.select_commands(files, repositories=repos, base_refs=resolved)
    assert any("verify:merge" in command.argv for command in selection.commands)


def test_collect_changed_paths_reads_staged_unstaged_and_untracked_child_changes(
    tmp_path: Path,
) -> None:
    repos = _repositories(tmp_path)
    (repos[1].root / "backend/example.py").write_text("staged\n")
    _git(repos[1].root, "add", "backend/example.py")
    (repos[2].root / "components/example.tsx").write_text("unstaged\n")
    new_file = repos[2].root / "components/new.tsx"
    new_file.write_text("export const n = 1;\n")

    _resolved, paths = MODULE.collect_changed_paths(_base_refs(), repos)

    assert "travel-agent/backend/example.py" in paths
    assert "travel-app/components/example.tsx" in paths
    assert "travel-app/components/new.tsx" in paths


def test_collect_changed_paths_rejects_missing_or_cross_repo_base_refs(
    tmp_path: Path,
) -> None:
    repos = _repositories(tmp_path)
    with pytest.raises(MODULE.BaseRefError, match="travel-app: no base ref"):
        MODULE.collect_changed_paths({"workspace": "HEAD", "agent": "HEAD"}, repos)
    foreign_commit = MODULE.resolve_base_ref(repos[0], "HEAD")
    with pytest.raises(MODULE.BaseRefError, match="travel-agent"):
        MODULE.collect_changed_paths(
            {"workspace": "HEAD", "agent": foreign_commit, "app": "HEAD"}, repos
        )


def test_ready_commands_propagate_nonzero_exit_code(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repos = _repositories(tmp_path)
    selection = MODULE.Selection()
    selection.add(
        (sys.executable, "-c", "import sys; sys.exit(7)"), repos[0].root, "failure"
    )
    monkeypatch.setattr(MODULE, "default_repositories", lambda: repos)
    monkeypatch.setattr(
        MODULE,
        "collect_changed_paths",
        lambda _refs, _repos: (
            {key: "x" * 40 for key in _refs},
            ["docs/working/note.md"],
        ),
    )
    monkeypatch.setattr(MODULE, "read_doc_texts", lambda _files, _repos: {})
    monkeypatch.setattr(MODULE, "select_commands", lambda *_args, **_kwargs: selection)

    assert (
        MODULE.main(
            [
                "--workspace-base-ref",
                "HEAD",
                "--agent-base-ref",
                "HEAD",
                "--app-base-ref",
                "HEAD",
            ]
        )
        == 7
    )


def test_validator_start_failure_is_reported_and_does_not_skip_later_checks(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    repos = _repositories(tmp_path)
    selection = MODULE.Selection()
    selection.add(("missing-validator",), repos[0].root, "validator unavailable")
    selection.add(("later-validator",), repos[0].root, "later selected check")
    calls: list[tuple[str, ...]] = []

    def run(argv, *, cwd):
        calls.append(tuple(argv))
        if argv[0] == "missing-validator":
            raise FileNotFoundError("missing-validator")
        return SimpleNamespace(returncode=1)

    monkeypatch.setattr(MODULE.subprocess, "run", run)
    monkeypatch.setattr(MODULE, "default_repositories", lambda: repos)
    monkeypatch.setattr(
        MODULE,
        "collect_changed_paths",
        lambda _refs, _repos: (
            {key: "x" * 40 for key in _refs},
            ["docs/working/note.md"],
        ),
    )
    monkeypatch.setattr(MODULE, "read_doc_texts", lambda _files, _repos: {})
    monkeypatch.setattr(MODULE, "select_commands", lambda *_args, **_kwargs: selection)

    result = MODULE.main(
        [
            "--workspace-base-ref",
            "HEAD",
            "--agent-base-ref",
            "HEAD",
            "--app-base-ref",
            "HEAD",
        ]
    )

    assert result == 2
    assert calls == [("missing-validator",), ("later-validator",)]
    assert "could not start selected check missing-validator" in capsys.readouterr().err


def test_cli_requires_all_three_explicit_base_refs(
    capsys: pytest.CaptureFixture[str],
) -> None:
    assert MODULE.main(["--workspace-base-ref", "HEAD"]) == 2
    assert "travel-agent: base ref is required" in capsys.readouterr().err


def test_plan_json_records_backend_interpreter_and_postgres_prerequisites(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repos = _repositories(tmp_path)
    checker_test = repos[1].root / "tests/scripts/test_check_foo.py"
    checker_test.parent.mkdir(parents=True)
    checker_test.write_text("@requires_postgres\ndef test_database_case(): pass\n")
    backend_python = repos[1].root / ".venv/bin/python"
    backend_python.parent.mkdir(parents=True)
    backend_python.write_text("backend test interpreter placeholder\n")
    monkeypatch.setattr(MODULE, "default_repositories", lambda: repos)
    monkeypatch.setattr(
        MODULE,
        "collect_changed_paths",
        lambda _refs, _repos: (
            {"workspace": "w" * 40, "agent": "a" * 40, "app": "p" * 40},
            ["docs/working/note.md"],
        ),
    )
    monkeypatch.setattr(
        MODULE,
        "read_doc_texts",
        lambda _files, _repos: {
            "docs/working/note.md": "Run check_foo.py after edits."
        },
    )
    plan_path = tmp_path / "plan.json"

    result = MODULE.main(
        [
            "--workspace-base-ref",
            "HEAD",
            "--agent-base-ref",
            "HEAD",
            "--app-base-ref",
            "HEAD",
            "--dry-run",
            "--plan-json",
            str(plan_path),
        ]
    )

    assert result == 0
    plan = json.loads(plan_path.read_text())
    command = next(
        item for item in plan["commands"] if "pytest" in item["argv"]
    )
    assert command["argv"][0] == str(backend_python)
    assert {item["key"] for item in command["prerequisites"]} == {
        MODULE.BACKEND_PYTHON.key,
        MODULE.DISPOSABLE_POSTGRES.key,
    }


def test_disposable_postgres_prerequisite_requires_lane_local_fresh_database(
    tmp_path: Path,
) -> None:
    repos = _repositories(tmp_path)
    workspace = repos[0]
    _lane_postgres_manifest(workspace.root)

    assert MODULE._lane_postgres_prerequisite_error(workspace, {})
    assert MODULE._lane_postgres_prerequisite_error(
        workspace,
        {
            "TEST_DATABASE_URL": "postgresql://vesper:localdev@localhost:50568/vesper",
            "TEST_DATABASE_DISPOSABLE": "1",
        },
    )
    assert MODULE._lane_postgres_prerequisite_error(
        workspace,
        {
            "TEST_DATABASE_URL": "postgresql://vesper:localdev@remote.invalid:50568/e3_test",
            "TEST_DATABASE_DISPOSABLE": "1",
        },
    )
    assert MODULE._lane_postgres_prerequisite_error(
        workspace,
        {
            "TEST_DATABASE_URL": "postgresql://vesper:localdev@localhost:50569/e3_test",
            "TEST_DATABASE_DISPOSABLE": "1",
        },
    )
    assert MODULE._lane_postgres_prerequisite_error(
        workspace,
        {
            "TEST_DATABASE_URL": "postgresql://vesper:localdev@localhost:50568/e3_test?host=remote.invalid",
            "TEST_DATABASE_DISPOSABLE": "1",
        },
    )
    assert MODULE._lane_postgres_prerequisite_error(
        workspace,
        {
            "TEST_DATABASE_URL": "postgresql://vesper:localdev@localhost:50568/e3_test",
            "TEST_DATABASE_DISPOSABLE": "1",
            "PGSERVICE": "ambient-service",
        },
    )
    assert (
        MODULE._lane_postgres_prerequisite_error(
            workspace,
            {
                "TEST_DATABASE_URL": "postgresql://vesper:localdev@localhost:50568/e3_test",
                "TEST_DATABASE_DISPOSABLE": "1",
            },
        )
        is None
    )


def test_offline_filter_is_explicit_and_exact() -> None:
    assert MODULE._offline_marker_filter_active(
        {
            "PYTEST_ADDOPTS": (
                '-m "not requires_postgres and not requires_dogfood_wedge '
                'and not requires_api_keys"'
            )
        }
    )
    assert not MODULE._offline_marker_filter_active(
        {"PYTEST_ADDOPTS": "-m 'not requires_postgres'"}
    )


@pytest.mark.parametrize("addopts", [
    '-m "not REQUIRES_POSTGRES and not requires_dogfood_wedge and not requires_api_keys"',
    '-m "not requires_postgres and not requires_dogfood_wedge and not requires_api_keys" -m requires_postgres',
    '-m "not (requires_postgres and not requires_dogfood_wedge and not requires_api_keys)"',
])
def test_altered_offline_filter_cannot_bypass_database_prerequisite(tmp_path, addopts):
    repos = _repositories(tmp_path)
    command = MODULE.Command(
        ("pytest",), repos[1].root, "mixed checker", (MODULE.DISPOSABLE_POSTGRES,)
    )
    assert MODULE._command_prerequisite_errors(
        command, repos[0], {"PYTEST_ADDOPTS": addopts}
    ), "An altered filter must not exempt a mixed checker from database validation"


def test_main_blocks_mixed_checker_before_pytest_when_database_is_absent(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    repos = _repositories(tmp_path)
    selection = MODULE.Selection()
    selection.add(
        (sys.executable, "run_required_pytest.py", "--", "pytest"),
        repos[1].root,
        "mixed checker test",
        (MODULE.BACKEND_PYTHON, MODULE.DISPOSABLE_POSTGRES),
    )
    calls: list[tuple[str, ...]] = []

    def run(argv, **kwargs):
        calls.append(tuple(argv))
        return SimpleNamespace(returncode=0, stdout="Python 3.13.0\n", stderr="")

    monkeypatch.setattr(MODULE.subprocess, "run", run)
    monkeypatch.setattr(MODULE, "default_repositories", lambda: repos)
    monkeypatch.setattr(
        MODULE,
        "collect_changed_paths",
        lambda _refs, _repos: (
            {key: "x" * 40 for key in ("workspace", "agent", "app")},
            ["docs/working/note.md"],
        ),
    )
    monkeypatch.setattr(MODULE, "read_doc_texts", lambda _files, _repos: {})
    monkeypatch.setattr(MODULE, "select_commands", lambda *_args, **_kwargs: selection)
    monkeypatch.delenv("TEST_DATABASE_URL", raising=False)
    monkeypatch.delenv("TEST_DATABASE_DISPOSABLE", raising=False)
    monkeypatch.delenv("PYTEST_ADDOPTS", raising=False)

    result = MODULE.main(
        [
            "--workspace-base-ref",
            "HEAD",
            "--agent-base-ref",
            "HEAD",
            "--app-base-ref",
            "HEAD",
        ]
    )

    assert result == 2
    assert calls == [(sys.executable, "--version")]
    assert "set TEST_DATABASE_URL and TEST_DATABASE_DISPOSABLE=1" in capsys.readouterr().err


def test_main_runs_only_explicit_offline_subset_and_reports_database_deferral(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    repos = _repositories(tmp_path)
    selection = MODULE.Selection()
    selected = (sys.executable, "run_required_pytest.py", "--", "pytest")
    selection.add(
        selected,
        repos[1].root,
        "mixed checker test",
        (MODULE.BACKEND_PYTHON, MODULE.DISPOSABLE_POSTGRES),
    )
    calls: list[tuple[str, ...]] = []

    def run(argv, **kwargs):
        calls.append(tuple(argv))
        if argv[-1] == "--version":
            return SimpleNamespace(returncode=0, stdout="Python 3.13.0\n", stderr="")
        return SimpleNamespace(returncode=0, stdout="", stderr="")

    monkeypatch.setattr(MODULE.subprocess, "run", run)
    monkeypatch.setattr(MODULE, "default_repositories", lambda: repos)
    monkeypatch.setattr(
        MODULE,
        "collect_changed_paths",
        lambda _refs, _repos: (
            {key: "x" * 40 for key in ("workspace", "agent", "app")},
            ["docs/working/note.md"],
        ),
    )
    monkeypatch.setattr(MODULE, "read_doc_texts", lambda _files, _repos: {})
    monkeypatch.setattr(MODULE, "select_commands", lambda *_args, **_kwargs: selection)
    monkeypatch.setenv(
        "PYTEST_ADDOPTS",
        '-m "not requires_postgres and not requires_dogfood_wedge and not requires_api_keys"',
    )
    monkeypatch.delenv("TEST_DATABASE_URL", raising=False)
    monkeypatch.delenv("TEST_DATABASE_DISPOSABLE", raising=False)

    result = MODULE.main(
        [
            "--workspace-base-ref",
            "HEAD",
            "--agent-base-ref",
            "HEAD",
            "--app-base-ref",
            "HEAD",
        ]
    )

    assert result == 0
    assert calls == [(sys.executable, "--version"), selected]
    assert "database cases were not run here" in capsys.readouterr().out


def test_main_blocks_invalid_database_target_without_disclosing_url(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    repos = _repositories(tmp_path)
    _lane_postgres_manifest(repos[0].root)
    selection = MODULE.Selection()
    selected = (sys.executable, "run_required_pytest.py", "--", "pytest")
    selection.add(
        selected,
        repos[1].root,
        "mixed checker test",
        (MODULE.BACKEND_PYTHON, MODULE.DISPOSABLE_POSTGRES),
    )
    calls: list[tuple[str, ...]] = []

    def run(argv, **kwargs):
        calls.append(tuple(argv))
        return SimpleNamespace(returncode=0, stdout="Python 3.13.0\n", stderr="")

    monkeypatch.setattr(MODULE.subprocess, "run", run)
    monkeypatch.setattr(MODULE, "default_repositories", lambda: repos)
    monkeypatch.setattr(
        MODULE,
        "collect_changed_paths",
        lambda _refs, _repos: (
            {key: "x" * 40 for key in ("workspace", "agent", "app")},
            ["docs/working/note.md"],
        ),
    )
    monkeypatch.setattr(MODULE, "read_doc_texts", lambda _files, _repos: {})
    monkeypatch.setattr(MODULE, "select_commands", lambda *_args, **_kwargs: selection)
    monkeypatch.setenv(
        "TEST_DATABASE_URL",
        "postgresql://secret-user:secret-password@remote.invalid:50568/private_db",
    )
    monkeypatch.setenv("TEST_DATABASE_DISPOSABLE", "1")
    monkeypatch.delenv("PYTEST_ADDOPTS", raising=False)

    result = MODULE.main(
        [
            "--workspace-base-ref",
            "HEAD",
            "--agent-base-ref",
            "HEAD",
            "--app-base-ref",
            "HEAD",
        ]
    )

    output = capsys.readouterr()
    assert result == 2
    assert calls == [(sys.executable, "--version")]
    assert "must identify a loopback PostgreSQL database" in output.err
    assert "secret-password" not in output.out + output.err


def test_main_blocks_backend_interpreter_failure_and_continues_other_checks(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    repos = _repositories(tmp_path)
    selection = MODULE.Selection()
    selected = (sys.executable, "run_required_pytest.py", "--", "pytest")
    selection.add(
        selected,
        repos[1].root,
        "mixed checker test",
        (MODULE.BACKEND_PYTHON, MODULE.DISPOSABLE_POSTGRES),
    )
    selection.add(("later-validator",), repos[0].root, "unrelated selected check")
    calls: list[tuple[str, ...]] = []

    def run(argv, **kwargs):
        calls.append(tuple(argv))
        if argv[-1] == "--version":
            return SimpleNamespace(returncode=1, stdout="", stderr="startup error")
        return SimpleNamespace(returncode=0, stdout="", stderr="")

    monkeypatch.setattr(MODULE.subprocess, "run", run)
    monkeypatch.setattr(MODULE, "default_repositories", lambda: repos)
    monkeypatch.setattr(
        MODULE,
        "collect_changed_paths",
        lambda _refs, _repos: (
            {key: "x" * 40 for key in ("workspace", "agent", "app")},
            ["docs/working/note.md"],
        ),
    )
    monkeypatch.setattr(MODULE, "read_doc_texts", lambda _files, _repos: {})
    monkeypatch.setattr(MODULE, "select_commands", lambda *_args, **_kwargs: selection)
    monkeypatch.setenv(
        "PYTEST_ADDOPTS",
        '-m "not requires_postgres and not requires_dogfood_wedge and not requires_api_keys"',
    )
    monkeypatch.delenv("TEST_DATABASE_URL", raising=False)
    monkeypatch.delenv("TEST_DATABASE_DISPOSABLE", raising=False)

    result = MODULE.main(
        [
            "--workspace-base-ref",
            "HEAD",
            "--agent-base-ref",
            "HEAD",
            "--app-base-ref",
            "HEAD",
        ]
    )

    output = capsys.readouterr()
    assert result == 2
    assert calls == [(sys.executable, "--version"), ("later-validator",)]
    assert "not a working Python 3.13" in output.err
    assert "startup error" not in output.out + output.err


def test_git_identity_ignores_hook_environment(tmp_path, monkeypatch):
    repos = _repositories(tmp_path)
    expected = [MODULE._git(r, ["rev-parse", "HEAD"]).stdout for r in repos]
    monkeypatch.setenv("GIT_DIR", str(repos[0].root / ".git"))
    monkeypatch.setenv("GIT_WORK_TREE", str(repos[0].root))
    assert [MODULE._git(r, ["rev-parse", "HEAD"]).stdout for r in repos] == expected
    assert len(set(expected)) == 3


@pytest.mark.parametrize("path", [
    "travel-app/.maestro/polish/new.yaml",
    "travel-app/.maestro/config.pr.yaml",
    "travel-app/package.json",
    "docs/child-repos.ci-lock.json",
    "scripts/validate-maestro-flows.py",
    "travel-app/scripts/maestro/normalize-metadata.mjs",
])
def test_maestro_inputs_check_packaged_inventory_before_child_suites(path):
    selection = MODULE.select_commands([path], base_refs={"workspace": "base", "app": "base"})
    gate = next(i for i,c in enumerate(selection.commands) if c.argv == ("make", "maestro-flow-governance-check"))
    assert all(gate < i for i,c in enumerate(selection.commands) if "verify:merge" in c.argv)
    assert MODULE.required_dependency_repositories(selection) == ["travel-agent", "travel-app"]


def test_ordinary_component_edit_does_not_select_whole_maestro_inventory():
    selection = MODULE.select_commands(["travel-app/components/Foo.tsx"], base_refs={"app": "base"})
    assert not any("maestro-flow-governance-check" in c.argv for c in selection.commands)
