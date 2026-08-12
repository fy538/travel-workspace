from __future__ import annotations

import importlib.util
import subprocess
import sys
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
    checker_test = repos[0].root / "scripts/tests/test_check_foo.py"
    checker_test.parent.mkdir(parents=True)
    checker_test.write_text("")
    selection = MODULE.select_commands(
        ["docs/working/note.md"],
        doc_texts={"docs/working/note.md": "Run check_foo.py after edits."},
        repositories=repos,
    )
    assert not selection.fallback_to_verify
    assert any(
        command.argv == ("python3", "-m", "pytest", "scripts/tests/test_check_foo.py")
        for command in selection.commands
    )
    assert not any(command.display.startswith("<run") for command in selection.commands)


def test_high_risk_or_unknown_file_selects_full_gate() -> None:
    selection = MODULE.select_commands(["travel-app/utils/api/schema.gen.ts"])
    assert selection.fallback_to_verify
    assert "schema.gen.ts" in selection.fallback_reason


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


def test_cli_requires_all_three_explicit_base_refs(
    capsys: pytest.CaptureFixture[str],
) -> None:
    assert MODULE.main(["--workspace-base-ref", "HEAD"]) == 2
    assert "travel-agent: base ref is required" in capsys.readouterr().err
