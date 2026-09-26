"""Cross-repository evidence must resolve the selected repo, even in Git hooks."""

import os
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import journey_evidence
import promote_journey_evidence
import render_release_scope


@pytest.fixture
def repositories(tmp_path, monkeypatch):
    root = tmp_path / "workspace"
    child = root / "travel-agent"
    revisions = {}
    for repo, filename in ((root, "parent-only.txt"), (child, "child-only.txt")):
        repo.mkdir(parents=True)
        subprocess.run(["git", "init", "-q", str(repo)], check=True)
        (repo / filename).write_text("tracked evidence\n")
        subprocess.run(["git", "-C", str(repo), "add", filename], check=True)
        subprocess.run(
            ["git", "-C", str(repo), "-c", "user.name=Test",
             "-c", "user.email=test@example.test", "commit", "-qm", filename],
            check=True,
        )
        revisions[repo] = subprocess.check_output(
            ["git", "-C", str(repo), "rev-parse", "HEAD"], text=True
        ).strip()
    (child / "parent-only.txt").write_text("exists, but untracked in child\n")
    monkeypatch.setattr(render_release_scope, "ROOT", root)
    for key, value in {
        "GIT_DIR": root / ".git",
        "GIT_WORK_TREE": root,
        "GIT_COMMON_DIR": root / ".git",
        "GIT_INDEX_FILE": root / ".git/index",
    }.items():
        monkeypatch.setenv(key, str(value))
    return root, child, revisions


def test_tracked_child_file_survives_parent_hook_environment(repositories):
    assert render_release_scope._path_is_tracked("travel-agent/child-only.txt")


def test_parent_index_cannot_certify_untracked_child_file(repositories):
    assert not render_release_scope._path_is_tracked("travel-agent/parent-only.txt")


def test_foreign_index_alone_cannot_certify_untracked_child(repositories, monkeypatch):
    for key in ("GIT_DIR", "GIT_WORK_TREE", "GIT_COMMON_DIR"):
        monkeypatch.delenv(key)
    assert not render_release_scope._path_is_tracked("travel-agent/parent-only.txt")


def test_revision_uses_child_head_and_dirty_state(repositories):
    _, child, revisions = repositories
    assert journey_evidence._revision(child) == revisions[child] + "-dirty"


def test_dirty_parent_does_not_taint_clean_child(repositories):
    _, child, revisions = repositories
    (child / "parent-only.txt").unlink()
    assert journey_evidence._revision(child) == revisions[child]


def test_promotion_git_reads_resolve_selected_repository(repositories):
    _, child, revisions = repositories
    assert promote_journey_evidence._git_lines(child, "rev-parse", "HEAD") == [
        revisions[child]
    ]


def test_git_environment_preserves_non_repository_configuration(monkeypatch):
    monkeypatch.setenv("PATH", "/sentinel/bin")
    monkeypatch.setenv("GIT_TERMINAL_PROMPT", "0")
    monkeypatch.setenv("GIT_DIR", "/wrong")
    result = journey_evidence.repository_git_environment()
    assert result["PATH"] == "/sentinel/bin"
    assert result["GIT_TERMINAL_PROMPT"] == "0"
    assert "GIT_DIR" not in result
    assert os.environ["GIT_DIR"] == "/wrong"


def test_git_failure_never_certifies_tracked_evidence(repositories, monkeypatch):
    monkeypatch.setattr(
        render_release_scope.subprocess, "run",
        lambda *args, **kwargs: subprocess.CompletedProcess(args, 128),
    )
    assert not render_release_scope._path_is_tracked("travel-agent/child-only.txt")


def test_missing_git_is_an_error_not_a_pass(repositories, monkeypatch):
    def missing(*args, **kwargs):
        raise FileNotFoundError("git unavailable")
    monkeypatch.setattr(render_release_scope.subprocess, "run", missing)
    with pytest.raises(FileNotFoundError, match="git unavailable"):
        render_release_scope._path_is_tracked("travel-agent/child-only.txt")


def test_unreadable_revision_is_unknown(repositories, monkeypatch):
    def missing(*args, **kwargs):
        raise FileNotFoundError("git unavailable")
    monkeypatch.setattr(journey_evidence.subprocess, "check_output", missing)
    assert journey_evidence._revision(repositories[1]) == "unknown"
