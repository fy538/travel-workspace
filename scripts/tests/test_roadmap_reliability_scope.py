"""Fail-closed contract tests for the opt-in roadmap prose Reliability pilot."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

import roadmap_reliability_scope as scope  # noqa: E402
from verify_changed import Repo  # noqa: E402


ROADMAP = "docs/working/vesper-program-roadmap.md"
CHECKER_TEST = "tests/scripts/test_check-sample.py"
LOCK = "docs/child-repos.ci-lock.json"


def git(root: Path, *args: str) -> str:
    import subprocess

    result = subprocess.run(
        ["git", *args], cwd=root, capture_output=True, text=True, check=True
    )
    return result.stdout.strip()


def init_repo(path: Path, filename: str, content: str) -> str:
    path.mkdir(parents=True, exist_ok=True)
    git(path, "init", "-q")
    git(path, "config", "user.name", "Scope test")
    git(path, "config", "user.email", "scope@example.invalid")
    target = path / filename
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    git(path, "add", filename)
    git(path, "commit", "-qm", "fixture baseline")
    return git(path, "rev-parse", "HEAD")


@pytest.fixture
def candidate_fixture(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    return make_candidate_fixture(tmp_path, monkeypatch, checker_test=True)


def make_candidate_fixture(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, *, checker_test: bool
):
    root = tmp_path / "workspace"
    agent = root / "travel-agent"
    app = root / "travel-app"
    agent_file = CHECKER_TEST if checker_test else "README.md"
    agent_sha = init_repo(agent, agent_file, "def test_checker_contract():\n    assert True\n")
    checker = agent / "scripts/check-sample.py"
    checker.parent.mkdir(parents=True, exist_ok=True)
    checker.write_text("def check():\n    return True\n", encoding="utf-8")
    git(agent, "add", "scripts/check-sample.py")
    git(agent, "commit", "-qm", "add referenced checker")
    agent_sha = git(agent, "rev-parse", "HEAD")
    app_sha = init_repo(app, "README.md", "fixture app\n")

    root.mkdir(parents=True, exist_ok=True)
    git(root, "init", "-q")
    git(root, "config", "user.name", "Scope test")
    git(root, "config", "user.email", "scope@example.invalid")
    (root / ".gitignore").write_text("travel-agent\ntravel-app\n", encoding="utf-8")
    document = root / ROADMAP
    document.parent.mkdir(parents=True, exist_ok=True)
    document.write_text(
        "---\ndoc_type: roadmap\nstatus: active\nowner: engineering\n---\n\n"
        "# Roadmap\n\nBaseline.\n",
        encoding="utf-8",
    )
    lock = root / LOCK
    lock.parent.mkdir(parents=True, exist_ok=True)
    lock.write_text(
        json.dumps({"travel-agent": agent_sha, "travel-app": app_sha}) + "\n",
        encoding="utf-8",
    )
    git(root, "add", ".gitignore", ROADMAP, LOCK)
    git(root, "commit", "-qm", "fixture baseline")
    base_sha = git(root, "rev-parse", "HEAD")
    git(root, "update-ref", "refs/remotes/origin/main", base_sha)

    repositories = (
        Repo("workspace", "workspace", root, ""),
        Repo("agent", "travel-agent", agent, "travel-agent/"),
        Repo("app", "travel-app", app, "travel-app/"),
    )
    monkeypatch.setattr(scope, "default_repositories", lambda: repositories)

    document.write_text(
        document.read_text(encoding="utf-8").replace(
            "Baseline.", "Updated prose; see check-sample.py for the evidence."
        ),
        encoding="utf-8",
    )
    git(root, "add", ROADMAP)
    git(root, "commit", "-qm", "edit roadmap prose")
    head_sha = git(root, "rev-parse", "HEAD")
    tuple_path = root / "candidate-tuple.json"
    write_tuple(tuple_path, head_sha, agent_sha, app_sha)
    return {
        "root": root,
        "agent": agent,
        "app": app,
        "base": base_sha,
        "head": head_sha,
        "agent_sha": agent_sha,
        "app_sha": app_sha,
        "tuple": tuple_path,
    }


def write_tuple(path: Path, workspace_sha: str, agent_sha: str, app_sha: str) -> None:
    candidate = {
        "workspace": workspace_sha,
        "travel-agent": agent_sha,
        "travel-app": app_sha,
    }
    path.write_text(
        json.dumps({"schema_version": 1, "candidate": candidate, "tested": candidate}),
        encoding="utf-8",
    )


def classify(fixture, **overrides):
    args = {
        "root": fixture["root"],
        "base_ref": fixture["base"],
        "base_branch": "main",
        "event_name": "pull_request",
        "main_ref": "refs/remotes/origin/main",
        "candidate_tuple_path": fixture["tuple"],
    }
    args.update(overrides)
    return scope.build_plan(**args)


def commit_workspace_change(root: Path, path: str, content: str | None) -> str:
    target = root / path
    if content is None:
        target.unlink()
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
    git(root, "add", "-A", path)
    git(root, "commit", "-qm", f"change {path}")
    return git(root, "rev-parse", "HEAD")


def test_allowlisted_prose_uses_existing_doc_checks_and_referenced_checker_test(
    candidate_fixture,
):
    plan = classify(candidate_fixture)

    assert plan["eligible"] is True
    assert plan["scope"] == "working-roadmap-prose"
    assert plan["changed_paths"] == [ROADMAP]
    assert "travel-agent" in plan["dependencies"]
    assert any(
        command["repo"] == "agent"
        and command["argv"] == ["python3", "-m", "pytest", CHECKER_TEST]
        for command in plan["commands"]
    )
    assert any(command["argv"] == ["make", "docs-links-check", "docs-spine-check", "docs-canon-check"]
               for command in plan["commands"])
    assert any(command["argv"] == ["make", "docs-inventory-check", "docs-status-check", "docs-child-governance-check"]
               for command in plan["commands"])


@pytest.mark.parametrize(
    "path,content",
    [
        ("src/source.ts", "export const changed = true;\n"),
        ("docs/openapi.json", "{\"openapi\": \"3.1.0\"}\n"),
        ("docs/reliability/CI Plan.md", "---\ndoc_type: runbook\n---\npolicy\n"),
        (".github/workflows/reliability.yml", "name: Changed\n"),
        (
            "docs/working/artifact-experience-engineering-roadmap-2026-09-29.md",
            "---\ndoc_type: roadmap\nstatus: active\nowner: engineering\n---\nnew doc\n",
        ),
    ],
)
def test_unknown_source_policy_workflow_or_new_document_keeps_full_scope(
    candidate_fixture, path, content
):
    fixture = candidate_fixture
    head = commit_workspace_change(fixture["root"], path, content)
    write_tuple(fixture["tuple"], head, fixture["agent_sha"], fixture["app_sha"])

    plan = classify(fixture)

    assert plan["eligible"] is False
    assert plan["scope"] == "full"


def test_metadata_changes_keep_full_scope(candidate_fixture):
    fixture = candidate_fixture
    text = (fixture["root"] / ROADMAP).read_text(encoding="utf-8")
    head = commit_workspace_change(
        fixture["root"], ROADMAP, text.replace("status: active", "status: draft")
    )
    write_tuple(fixture["tuple"], head, fixture["agent_sha"], fixture["app_sha"])

    plan = classify(fixture)

    assert plan["eligible"] is False
    assert "metadata changed" in plan["reason"]


@pytest.mark.parametrize(
    "kwargs",
    [
        {"event_name": "push"},
        {"base_branch": "release"},
        {"base_ref": "0" * 40},
        {"main_ref": "refs/remotes/origin/missing"},
        {"git_executable": "/missing/git"},
    ],
)
def test_missing_or_unsupported_pull_request_evidence_keeps_full_scope(
    candidate_fixture, kwargs
):
    plan = classify(candidate_fixture, **kwargs)
    assert plan["eligible"] is False
    assert plan["scope"] == "full"


@pytest.mark.parametrize("missing", ["make", "python3"])
def test_missing_documentation_tool_keeps_full_scope(
    candidate_fixture, monkeypatch: pytest.MonkeyPatch, missing: str
):
    real_which = scope.shutil.which
    monkeypatch.setattr(
        scope.shutil,
        "which",
        lambda name, *args, **kwargs: None if name == missing else real_which(name, *args, **kwargs),
    )

    plan = classify(candidate_fixture)

    assert plan["eligible"] is False
    assert "tool is missing" in plan["reason"]


def test_tuple_mismatch_keeps_full_scope(candidate_fixture):
    fixture = candidate_fixture
    write_tuple(fixture["tuple"], fixture["head"], fixture["agent_sha"], "f" * 40)

    plan = classify(fixture)

    assert plan["eligible"] is False
    assert "does not match travel-app" in plan["reason"]


@pytest.mark.parametrize("identity", ["missing", "malformed"])
def test_missing_or_malformed_candidate_identity_keeps_full_scope(
    candidate_fixture, identity: str
):
    fixture = candidate_fixture
    if identity == "missing":
        fixture["tuple"].unlink()
    else:
        fixture["tuple"].write_text("not-json\n", encoding="utf-8")

    plan = classify(fixture)

    assert plan["eligible"] is False
    assert "Candidate verification identity" in plan["reason"]


def test_changed_child_lock_keeps_full_scope(candidate_fixture):
    fixture = candidate_fixture
    lock_text = (fixture["root"] / LOCK).read_text(encoding="utf-8")
    updated = json.loads(lock_text)
    updated["travel-app"] = "f" * 40
    head = commit_workspace_change(fixture["root"], LOCK, json.dumps(updated) + "\n")
    write_tuple(fixture["tuple"], head, fixture["agent_sha"], "f" * 40)

    plan = classify(fixture)

    assert plan["eligible"] is False
    assert plan["scope"] == "full"


def test_dirty_child_checkout_keeps_full_scope(candidate_fixture):
    fixture = candidate_fixture
    (fixture["app"] / "uncommitted.txt").write_text("dirty\n", encoding="utf-8")

    plan = classify(fixture)

    assert plan["eligible"] is False
    assert "uncommitted changes" in plan["reason"]


def test_unexpected_workspace_changes_keep_full_scope(candidate_fixture):
    fixture = candidate_fixture
    (fixture["root"] / "untracked.txt").write_text("untrusted workspace state\n", encoding="utf-8")

    plan = classify(fixture)

    assert plan["eligible"] is False
    assert "Workspace checkout has uncommitted changes" in plan["reason"]


def test_checker_reference_without_a_mapped_test_does_not_invent_coverage(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    fixture = make_candidate_fixture(
        tmp_path / "missing-checker", monkeypatch, checker_test=False
    )

    plan = classify(fixture)

    assert plan["eligible"] is True
    assert not any(command["argv"][-1] == CHECKER_TEST for command in plan["commands"])


def test_reference_to_missing_checker_keeps_full_scope(candidate_fixture):
    fixture = candidate_fixture
    text = (fixture["root"] / ROADMAP).read_text(encoding="utf-8")
    head = commit_workspace_change(
        fixture["root"], ROADMAP, text.replace("check-sample.py", "check-missing.py")
    )
    write_tuple(fixture["tuple"], head, fixture["agent_sha"], fixture["app_sha"])

    plan = classify(fixture)

    assert plan["eligible"] is False
    assert "unavailable checker" in plan["reason"]


def test_scope_plan_integrity_rejects_modified_plan(candidate_fixture):
    plan = classify(candidate_fixture)
    plan["commands"].clear()

    with pytest.raises(scope.ScopeError, match="identity is missing or has changed"):
        scope._verify_plan_integrity(plan)
