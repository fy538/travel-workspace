import importlib.util
from pathlib import Path
import subprocess

import pytest


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts/fetch_child_doc_baselines.py"
SPEC = importlib.util.spec_from_file_location("fetch_child_doc_baselines", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def test_parse_baselines_reads_only_the_two_pinned_children():
    config = """version: 1
repos:
  travel-agent:
    baseline: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    docs_root: docs
  travel-app:
    baseline: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    docs_root: docs
"""
    assert MODULE.parse_baselines(config) == {
        "travel-agent": "a" * 40,
        "travel-app": "b" * 40,
    }


@pytest.mark.parametrize("baseline", ["short", "A" * 40, "a" * 39])
def test_parse_baselines_rejects_non_full_lowercase_shas(baseline):
    config = f"repos:\n  travel-agent:\n    baseline: {baseline}\n  travel-app:\n    baseline: {'b' * 40}\n"
    with pytest.raises(ValueError, match="invalid full commit SHA"):
        MODULE.parse_baselines(config)


def run_git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=repo, text=True, capture_output=True, check=True
    )
    return result.stdout.strip()


def make_shallow_repo(tmp_path):
    source = tmp_path / "source"
    remote = tmp_path / "origin.git"
    shallow = tmp_path / "shallow"
    source.mkdir()
    run_git(source, "init", "-b", "main")
    run_git(source, "config", "user.name", "Test")
    run_git(source, "config", "user.email", "test@example.invalid")
    (source / "docs").mkdir()
    (source / "docs" / "baseline.md").write_text("baseline\n")
    run_git(source, "add", "docs/baseline.md")
    run_git(source, "commit", "-m", "baseline")
    baseline = run_git(source, "rev-parse", "HEAD")
    (source / "current.txt").write_text("current\n")
    run_git(source, "add", "current.txt")
    run_git(source, "commit", "-m", "current")
    current = run_git(source, "rev-parse", "HEAD")

    run_git(tmp_path, "init", "--bare", str(remote))
    run_git(source, "remote", "add", "origin", str(remote))
    run_git(source, "push", "origin", "main")
    run_git(remote, "config", "uploadpack.allowFilter", "true")
    shallow_url = remote.as_uri()
    run_git(tmp_path, "clone", "--depth=1", "--branch", "main", shallow_url, str(shallow))
    return shallow, remote, baseline, current


def test_fetches_missing_baseline_tree_without_moving_pinned_head(tmp_path):
    shallow, _remote, baseline, current = make_shallow_repo(tmp_path)
    assert run_git(shallow, "rev-parse", "HEAD") == current
    assert subprocess.run(
        ["git", "cat-file", "-e", f"{baseline}^{{tree}}"], cwd=shallow, check=False
    ).returncode != 0

    assert MODULE.ensure_baseline_tree(shallow, baseline) is True
    assert run_git(shallow, "rev-parse", "HEAD") == current
    assert run_git(shallow, "rev-list", "--count", "HEAD") == "1"
    assert run_git(shallow, "rev-list", "--count", baseline) == "1"
    assert (
        run_git(shallow, "ls-tree", "-r", "--name-only", baseline, "--", "docs")
        == "docs/baseline.md"
    )
    assert run_git(shallow, "config", "remote.origin.promisor") == "true"
    assert run_git(shallow, "config", "remote.origin.partialclonefilter") == "blob:none"


def test_fails_closed_when_baseline_fetch_fails_and_preserves_head(tmp_path):
    shallow, _remote, baseline, current = make_shallow_repo(tmp_path)
    run_git(shallow, "remote", "set-url", "origin", str(tmp_path / "missing.git"))

    with pytest.raises(RuntimeError):
        MODULE.ensure_baseline_tree(shallow, baseline)

    assert run_git(shallow, "rev-parse", "HEAD") == current
