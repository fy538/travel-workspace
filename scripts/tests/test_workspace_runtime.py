from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

SCRIPTS = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def git(repo, *args):
    return subprocess.check_output(["git", "-C", str(repo), *args], text=True).strip()


def init(repo):
    repo.mkdir(parents=True, exist_ok=True)
    git(repo, "init", "-q")
    git(
        repo,
        "-c",
        "user.name=Test",
        "-c",
        "user.email=test@example.test",
        "commit",
        "--allow-empty",
        "-qm",
        "base",
    )


def coordinated_sources(tmp_path):
    root = tmp_path / "source"
    for name in ("", "travel-agent", "travel-app"):
        source = root / name
        init(source)
        git(source, "branch", "-M", "main")
        if not name:
            (source / ".gitignore").write_text(
                ".workspace-lane.json\ntravel-agent/\ntravel-app/\n"
            )
            git(source, "add", ".gitignore")
            git(
                source, "-c", "user.name=Test", "-c", "user.email=test@example.test",
                "commit", "-qm", "ignore lane artifacts",
            )
        remote = tmp_path / f"{name or 'workspace'}-remote.git"
        git(tmp_path, "init", "--bare", "-q", str(remote))
        git(source, "remote", "add", "origin", str(remote))
        git(source, "push", "-q", "-u", "origin", "main")
    return root


def deterministic_ports(_count):
    return [15501, 16333, 16334, 18101, 18102]


def create_fixture_lane(module, root, lane):
    module.create(
        SimpleNamespace(
            name="fixture",
            prefix="codex/",
            directory=str(lane),
            base=None,
            owner="eng",
            outcome="fixture outcome",
        )
    )


def commit_file(repo, name, value, message):
    (repo / name).write_text(value)
    git(repo, "add", name)
    git(
        repo, "-c", "user.name=Test", "-c", "user.email=test@example.test",
        "commit", "-qm", message,
    )


def test_bootstrap_creates_supported_layout_and_is_idempotent(tmp_path):
    root = tmp_path / "workspace"
    init(root)
    (root / "scripts").mkdir()
    (root / "scripts/bootstrap-repos.sh").write_text(
        (SCRIPTS / "bootstrap-repos.sh").read_text()
    )
    sources = [tmp_path / name for name in ("backend-origin", "frontend-origin")]
    for source in sources:
        init(source)
    env = {
        **os.environ,
        "TRAVEL_AGENT_REPO": str(sources[0]),
        "TRAVEL_APP_REPO": str(sources[1]),
        "GIT_DIR": str(root / ".git"),
    }
    for _ in range(2):
        subprocess.run(
            ["bash", str(root / "scripts/bootstrap-repos.sh")],
            env=env,
            check=True,
            capture_output=True,
        )
    for name in ("travel-agent", "travel-app"):
        assert load("worktree_lane").repository(root / name)
    assert not (root / "Travel Agent").exists()


def test_bootstrap_adopts_legacy_checkout_without_copying(tmp_path):
    init(tmp_path)
    (tmp_path / "scripts").mkdir()
    (tmp_path / "scripts/bootstrap-repos.sh").write_text(
        (SCRIPTS / "bootstrap-repos.sh").read_text()
    )
    for name in ("Travel Agent", "Travel App"):
        init(tmp_path / name)
    subprocess.run(
        ["bash", str(tmp_path / "scripts/bootstrap-repos.sh")],
        check=True,
        capture_output=True,
    )
    assert (tmp_path / "travel-agent").resolve() == tmp_path / "Travel Agent"


def test_linked_checkout_recognized_but_plain_subdirectory_rejected(tmp_path):
    root = tmp_path / "source"
    init(root)
    lane = tmp_path / "linked"
    git(root, "worktree", "add", "-b", "lane", str(lane))
    assert (lane / ".git").is_file()
    assert load("worktree_lane").repository(lane) == lane
    (root / "fake-child").mkdir()
    with pytest.raises(ValueError):
        load("worktree_lane").repository(root / "fake-child")


def test_dev_failure_preserves_status_and_cleans_owned_sibling(tmp_path):
    module = load("dev_runtime")
    command = [sys.executable, "-c", "import sys; sys.exit(42)"]
    with pytest.raises(subprocess.CalledProcessError) as failure:
        module.supervise(
            [("API", command, tmp_path, "http://127.0.0.1:1")],
            os.environ.copy(),
            timeout=3,
        )
    assert failure.value.returncode == 42


def test_dev_readiness_timeout_is_failure_and_stops_process(tmp_path):
    module = load("dev_runtime")
    seen = []
    popen = module.subprocess.Popen

    def start(*args, **kwargs):
        p = popen(*args, **kwargs)
        seen.append(p)
        return p

    module.subprocess = SimpleNamespace(
        Popen=start, CalledProcessError=subprocess.CalledProcessError
    )
    with pytest.raises(TimeoutError):
        module.supervise(
            [
                (
                    "API",
                    [sys.executable, "-c", "import time; time.sleep(60)"],
                    tmp_path,
                    "http://127.0.0.1:1",
                )
            ],
            os.environ.copy(),
            timeout=0.2,
        )
    assert seen[0].poll() is not None


def test_lane_environment_has_distinct_endpoints_and_rejects_ambient_override(
    tmp_path, monkeypatch
):
    module = load("dev_runtime")
    runtime = {
        "ownership": "isolated",
        "compose_project": "vesper-test",
        "postgres_port": 15501,
        "api_port": 8101,
        "expo_port": 8102,
    }
    (tmp_path / ".workspace-lane.json").write_text(json.dumps({"runtime": runtime}))
    monkeypatch.delenv("DATABASE_URL", raising=False)
    env = module.runtime_environment(tmp_path)
    assert env["COMPOSE_PROJECT_NAME"] == "vesper-test"
    assert ":15501/" in env["DATABASE_URL"]
    assert env["EXPO_PUBLIC_API_URL"] == "http://localhost:8101"
    monkeypatch.setenv("API_PORT", "9999")
    with pytest.raises(ValueError, match="conflicts"):
        module.runtime_environment(tmp_path)


def test_create_builds_three_independent_worktrees_with_distinct_runtime(
    tmp_path, monkeypatch
):
    module = load("worktree_lane")
    root = tmp_path / "source"
    for name in ("", "travel-agent", "travel-app"):
        init(root / name)
    monkeypatch.setattr(module, "ROOT", root)
    monkeypatch.setattr(module, "free_ports", deterministic_ports)
    lane = tmp_path / "lane"
    args = SimpleNamespace(
        name="fixture", prefix="codex/", directory=str(lane), base=None
    )
    module.create(args)
    for name in ("", "travel-agent", "travel-app"):
        assert module.repository(lane / name) == lane / name
        assert git(lane / name, "branch", "--show-current") == "codex/fixture"
    runtime = json.loads((lane / ".workspace-lane.json").read_text())["runtime"]
    assert len({value for key, value in runtime.items() if key.endswith("_port")}) == 5
    with pytest.raises(ValueError, match="already exists"):
        module.create(args)


def test_create_allocation_denial_is_nonzero_and_leaves_all_repos_untouched(
    tmp_path, monkeypatch, capsys
):
    module = load("worktree_lane")
    root = coordinated_sources(tmp_path)
    monkeypatch.setattr(module, "ROOT", root)
    lane = tmp_path / "lane"
    before = {
        name: (git(root / name, "worktree", "list", "--porcelain"),
               git(root / name, "branch", "--list"))
        for name in ("", "travel-agent", "travel-app")
    }

    def denied(_count):
        raise PermissionError("fixture allocator denied")

    monkeypatch.setattr(module, "free_ports", denied)
    monkeypatch.setattr(
        sys,
        "argv",
        ["worktree_lane.py", "create", "fixture", "--directory", str(lane)],
    )
    assert module.main() == 1
    error = capsys.readouterr().err
    assert "before worktree creation" in error
    assert "no worktrees or branches were created" in error
    assert "fixture allocator denied" in error
    assert not lane.exists()
    after = {
        name: (git(root / name, "worktree", "list", "--porcelain"),
               git(root / name, "branch", "--list"))
        for name in ("", "travel-agent", "travel-app")
    }
    assert after == before


def test_create_rejects_existing_path_or_late_branch_before_mutation(
    tmp_path, monkeypatch
):
    module = load("worktree_lane")
    root = coordinated_sources(tmp_path)
    monkeypatch.setattr(module, "ROOT", root)
    monkeypatch.setattr(module, "free_ports", deterministic_ports)
    lane = tmp_path / "lane"
    lane.mkdir()
    marker = lane / "keep.txt"
    marker.write_text("preserve")
    args = SimpleNamespace(name="fixture", prefix="codex/", directory=str(lane), base=None)
    with pytest.raises(ValueError, match="already exists"):
        module.create(args)
    assert marker.read_text() == "preserve"
    marker.unlink()
    lane.rmdir()

    git(root / "travel-app", "branch", "codex/fixture")
    before = {
        name: (git(root / name, "worktree", "list", "--porcelain"),
               git(root / name, "branch", "--list"))
        for name in ("", "travel-agent", "travel-app")
    }
    with pytest.raises(ValueError, match="branch codex/fixture already exists"):
        module.create(args)
    after = {
        name: (git(root / name, "worktree", "list", "--porcelain"),
               git(root / name, "branch", "--list"))
        for name in ("", "travel-agent", "travel-app")
    }
    assert after == before
    assert not lane.exists()


@pytest.mark.parametrize(
    ("failed_repo", "completed"),
    [
        ("travel-agent", ["workspace"]),
        ("travel-app", ["workspace", "travel-agent"]),
    ],
)
def test_create_child_failure_reports_and_preserves_exact_partial_work(
    tmp_path, monkeypatch, failed_repo, completed
):
    module = load("worktree_lane")
    root = coordinated_sources(tmp_path)
    monkeypatch.setattr(module, "ROOT", root)
    monkeypatch.setattr(module, "free_ports", deterministic_ports)
    lane = tmp_path / "lane"
    real_git = module.git
    changed = lane / "review-note.txt"

    def fail_child(repo, *args, **kwargs):
        if args[:3] == ("worktree", "add", "-b") and Path(repo) == root / failed_repo:
            raise subprocess.CalledProcessError(37, ["git", "worktree", "add"])
        result = real_git(repo, *args, **kwargs)
        if args[:3] == ("worktree", "add", "-b") and Path(repo) == root:
            changed.write_text("preserve concurrent review work")
        return result

    monkeypatch.setattr(module, "git", fail_child)
    with pytest.raises(ValueError) as failure:
        create_fixture_lane(module, root, lane)
    message = str(failure.value)
    assert f"stage {failed_repo}" in message
    assert "No automatic cleanup was attempted" in message
    assert changed.read_text() == "preserve concurrent review work"
    for repo_name in ("workspace", "travel-agent", "travel-app"):
        repo = root if repo_name == "workspace" else root / repo_name
        path = lane if repo_name == "workspace" else lane / repo_name
        if repo_name in completed:
            assert path.exists()
            assert "codex/fixture" in git(repo, "branch", "--list")
            assert f"{repo_name} path={path} branch=codex/fixture" in message
        else:
            assert not path.exists()
            assert "codex/fixture" not in git(repo, "branch", "--list")


def test_create_manifest_failure_preserves_existing_file_and_all_worktrees(
    tmp_path, monkeypatch
):
    module = load("worktree_lane")
    root = coordinated_sources(tmp_path)
    monkeypatch.setattr(module, "ROOT", root)
    monkeypatch.setattr(module, "free_ports", deterministic_ports)
    lane = tmp_path / "lane"
    real_git = module.git
    manifest = lane / ".workspace-lane.json"
    sentinel = "written by concurrent owner; preserve\n"

    def create_manifest_during_last_add(repo, *args, **kwargs):
        result = real_git(repo, *args, **kwargs)
        if args[:3] == ("worktree", "add", "-b") and Path(repo) == root / "travel-app":
            manifest.write_text(sentinel)
        return result

    monkeypatch.setattr(module, "git", create_manifest_during_last_add)
    with pytest.raises(ValueError) as failure:
        create_fixture_lane(module, root, lane)
    message = str(failure.value)
    assert "stage manifest write" in message
    assert "No automatic cleanup was attempted" in message
    assert manifest.read_text() == sentinel
    for repo_name in ("workspace", "travel-agent", "travel-app"):
        repo = root if repo_name == "workspace" else root / repo_name
        path = lane if repo_name == "workspace" else lane / repo_name
        assert path.exists()
        assert "codex/fixture" in git(repo, "branch", "--list")
        assert f"{repo_name} path={path} branch=codex/fixture" in message


def test_second_process_failure_stops_already_ready_sibling(tmp_path):
    module = load("dev_runtime")
    port = load("worktree_lane").free_ports(1)[0]
    seen = []
    popen = module.subprocess.Popen

    def start(*args, **kwargs):
        p = popen(*args, **kwargs)
        seen.append(p)
        return p

    module.subprocess = SimpleNamespace(
        Popen=start, CalledProcessError=subprocess.CalledProcessError
    )
    commands = [
        (
            "API",
            [sys.executable, "-m", "http.server", str(port), "--bind", "127.0.0.1"],
            tmp_path,
            f"http://127.0.0.1:{port}",
        ),
        (
            "Expo",
            [sys.executable, "-c", "import sys; sys.exit(42)"],
            tmp_path,
            "http://127.0.0.1:1",
        ),
    ]
    with pytest.raises(subprocess.CalledProcessError) as failure:
        module.supervise(commands, os.environ.copy(), timeout=5)
    assert failure.value.returncode == 42
    assert len(seen) == 2 and all(p.poll() is not None for p in seen)


def test_failed_coordinated_gate_never_pushes(tmp_path, monkeypatch):
    module = load("worktree_lane")
    (tmp_path / ".workspace-lane.json").write_text(json.dumps({"branch": "codex/test"}))
    calls = []
    monkeypatch.setattr(module, "repository", lambda p: p)

    def fake_git(repo, *args, **kwargs):
        calls.append(args)
        if args[:2] == ("branch", "--show-current"):
            return "codex/test"
        if args[:2] == ("status", "--porcelain"):
            return ""
        return "a" * 40

    monkeypatch.setattr(module, "git", fake_git)

    def run(command, **kwargs):
        if command[0] == "make":
            raise subprocess.CalledProcessError(7, command)
        return SimpleNamespace(returncode=0)

    monkeypatch.setattr(module.subprocess, "run", run)
    with pytest.raises(subprocess.CalledProcessError):
        module.land(
            SimpleNamespace(
                directory=str(tmp_path), name="test", prefix="codex/", publish=True
            )
        )
    assert not any(args[0] == "push" for args in calls)


def test_status_reports_lanes_without_mutation(tmp_path, monkeypatch, capsys):
    module = load("worktree_lane")
    root = coordinated_sources(tmp_path)
    monkeypatch.setattr(module, "ROOT", root)
    monkeypatch.setattr(module, "free_ports", deterministic_ports)
    lane = tmp_path / "lane"
    create_fixture_lane(module, root, lane)
    capsys.readouterr()
    module.status(None)
    output = capsys.readouterr().out
    assert "owner: eng" in output
    assert "outcome: fixture outcome" in output
    assert "ancestry vs refs/remotes/origin/main: merged" in output
    assert "equivalent patches 0" in output
    assert output.count("registered") == 3
    orphan = tmp_path / "child-only"
    git(root / "travel-agent", "worktree", "add", "--detach", str(orphan))
    module.status(None)
    assert f"Unpaired travel-agent worktree: {orphan}" in capsys.readouterr().out


def test_status_distinguishes_merge_cherry_pick_and_remaining_patches(
    tmp_path, monkeypatch, capsys
):
    module = load("worktree_lane")
    root = coordinated_sources(tmp_path)
    monkeypatch.setattr(module, "ROOT", root)
    monkeypatch.setattr(module, "free_ports", deterministic_ports)
    lane = tmp_path / "lane"
    create_fixture_lane(module, root, lane)

    # A regular merge is ancestry-proven against the cached main ref.
    commit_file(lane, "merged.txt", "merged\n", "merge candidate")
    git(root, "merge", "--no-ff", "-m", "adopt merged candidate", "codex/fixture")
    git(root, "push", "-q", "origin", "main")

    # The same patch on a different commit is equivalent, while ancestry stays false.
    agent_lane = lane / "travel-agent"
    agent_source = root / "travel-agent"
    commit_file(agent_lane, "picked.txt", "picked\n", "cherry-pick candidate")
    picked = git(agent_lane, "rev-parse", "HEAD")
    git(
        agent_source, "-c", "user.name=Test", "-c", "user.email=test@example.test",
        "cherry-pick", "-x", picked,
    )
    git(agent_source, "push", "-q", "origin", "main")

    # Patch equivalence is advisory; retirement still requires ancestry.
    with pytest.raises(ValueError, match="not merged"):
        module.retire(
            SimpleNamespace(
                name="fixture", prefix="codex/", directory=str(lane),
                apply=False, runtime_stopped=False,
            )
        )
    assert lane.exists()

    # Unadopted work remains a positive patch candidate.
    commit_file(lane / "travel-app", "remaining.txt", "remaining\n", "remaining work")

    before = {
        name: (git(root / name, "rev-parse", "HEAD"),
               git(lane if not name else lane / name, "rev-parse", "HEAD"))
        for name in ("", "travel-agent", "travel-app")
    }
    index_state = {}
    for name in ("", "travel-agent", "travel-app"):
        repo = lane if not name else lane / name
        index = Path(git(repo, "rev-parse", "--absolute-git-dir")) / "index"
        index_state[name] = (index.read_bytes(), index.stat().st_mtime_ns)
    capsys.readouterr()
    module.status(SimpleNamespace(base_ref="refs/remotes/origin/main"))
    output = capsys.readouterr().out
    assert "workspace: " in output and "ancestry vs refs/remotes/origin/main: merged" in output
    assert "travel-agent: " in output and "ancestry vs refs/remotes/origin/main: not ancestor" in output
    assert "equivalent patches 1 [" in output and "; remaining patches 0 [none]" in output
    assert "travel-app: " in output and "; remaining patches 1 [" in output
    after = {
        name: (git(root / name, "rev-parse", "HEAD"),
               git(lane if not name else lane / name, "rev-parse", "HEAD"))
        for name in ("", "travel-agent", "travel-app")
    }
    assert after == before
    for name in ("", "travel-agent", "travel-app"):
        repo = lane if not name else lane / name
        index = Path(git(repo, "rev-parse", "--absolute-git-dir")) / "index"
        assert (index.read_bytes(), index.stat().st_mtime_ns) == index_state[name]


def test_status_marks_modified_squash_and_missing_history_as_unknown_or_remaining(
    tmp_path, monkeypatch, capsys
):
    module = load("worktree_lane")
    root = coordinated_sources(tmp_path)
    monkeypatch.setattr(module, "ROOT", root)
    monkeypatch.setattr(module, "free_ports", deterministic_ports)
    lane = tmp_path / "lane"
    create_fixture_lane(module, root, lane)

    feature = lane / "travel-app"
    commit_file(feature, "combined.txt", "one\n", "first feature commit")
    (feature / "combined.txt").write_text("one\ntwo\n")
    git(feature, "add", "combined.txt")
    git(
        feature, "-c", "user.name=Test", "-c", "user.email=test@example.test",
        "commit", "-qm", "second feature commit",
    )
    source = root / "travel-app"
    commit_file(source, "combined.txt", "one\ntwo modified\n", "modified squash")
    git(source, "push", "-q", "origin", "main")

    # A missing cached ref and unrelated history both remain explicitly unknown.
    unrelated_repo = tmp_path / "unrelated-source"
    init(unrelated_repo)
    git(
        unrelated_repo, "-c", "user.name=Test", "-c", "user.email=test@example.test",
        "commit", "--amend", "--allow-empty", "-qm", "unrelated root",
    )
    git(unrelated_repo, "branch", "-M", "unrelated")
    git(source, "fetch", str(unrelated_repo), "unrelated:refs/heads/unrelated")

    capsys.readouterr()
    module.status(SimpleNamespace(base_ref="refs/remotes/origin/main"))
    output = capsys.readouterr().out
    assert "travel-app: " in output
    assert "; remaining patches 2 [" in output

    capsys.readouterr()
    module.status(SimpleNamespace(base_ref="refs/remotes/origin/not-fetched"))
    missing = capsys.readouterr().out
    assert "ancestry vs refs/remotes/origin/not-fetched: unknown" in missing
    assert "unknown (base ref unavailable)" in missing

    capsys.readouterr()
    module.status(SimpleNamespace(base_ref="refs/heads/unrelated"))
    unrelated = capsys.readouterr().out
    assert "travel-app: " in unrelated
    assert "ancestry vs refs/heads/unrelated: unknown (no common history)" in unrelated
    assert "unknown (no common history)" in unrelated


def test_status_surfaces_git_failure_without_claiming_adoption(
    tmp_path, monkeypatch, capsys
):
    module = load("worktree_lane")
    root = coordinated_sources(tmp_path)
    monkeypatch.setattr(module, "ROOT", root)
    monkeypatch.setattr(module, "free_ports", deterministic_ports)
    lane = tmp_path / "lane"
    create_fixture_lane(module, root, lane)
    real_readonly_git = module.readonly_git
    calls = []

    def fail_patch_query(repo, *args):
        calls.append(args)
        if args[:1] == ("cherry",):
            return SimpleNamespace(
                returncode=128, stdout="", stderr="injected Git query failure"
            )
        return real_readonly_git(repo, *args)

    monkeypatch.setattr(module, "readonly_git", fail_patch_query)
    capsys.readouterr()
    module.status(SimpleNamespace(base_ref="refs/remotes/origin/main"))
    output = capsys.readouterr().out
    assert "patch query failed" in output
    assert "injected Git query failure" in output
    assert "merged" in output
    assert not any(args[:1] == ("fetch",) for args in calls)


def test_status_bounds_patch_comparison_work(tmp_path, monkeypatch, capsys):
    module = load("worktree_lane")
    root = coordinated_sources(tmp_path)
    monkeypatch.setattr(module, "ROOT", root)
    monkeypatch.setattr(module, "free_ports", deterministic_ports)
    lane = tmp_path / "lane"
    create_fixture_lane(module, root, lane)
    real_readonly_git = module.readonly_git
    calls = []

    def exceed_comparison_limit(repo, *args):
        calls.append(args)
        if args[:2] == ("rev-list", "--count"):
            return SimpleNamespace(returncode=0, stdout="1001\n", stderr="")
        return real_readonly_git(repo, *args)

    monkeypatch.setattr(module, "readonly_git", exceed_comparison_limit)
    capsys.readouterr()
    module.status(SimpleNamespace(base_ref="refs/remotes/origin/main"))
    output = capsys.readouterr().out
    assert output.count("unknown (patch comparison limit 1000; 1001 candidate commits)") == 3
    assert not any(args[:1] == ("cherry",) for args in calls)


def test_retire_previews_then_removes_only_merged_clean_lane(tmp_path, monkeypatch):
    module = load("worktree_lane")
    root = coordinated_sources(tmp_path)
    monkeypatch.setattr(module, "ROOT", root)
    monkeypatch.setattr(module, "free_ports", deterministic_ports)
    lane = tmp_path / "lane"
    module.create(
        SimpleNamespace(name="fixture", prefix="codex/", directory=str(lane), base=None)
    )
    args = SimpleNamespace(
        name="fixture",
        prefix="codex/",
        directory=str(lane),
        apply=False,
        runtime_stopped=False,
    )
    # An unmerged change in just one child must preserve the entire lane.
    git(
        lane / "travel-agent", "-c", "user.name=Test",
        "-c", "user.email=test@example.test", "commit", "--allow-empty",
        "-qm", "change",
    )
    with pytest.raises(ValueError, match="not merged"):
        module.retire(args)
    assert lane.exists()
    git(
        root / "travel-agent", "-c", "user.name=Test",
        "-c", "user.email=test@example.test", "merge", "--no-ff", "-qm",
        "adopt", "codex/fixture",
    )
    git(root / "travel-agent", "push", "-q", "origin", "main")

    (lane / "travel-app" / "scratch.txt").write_text("keep")
    with pytest.raises(ValueError, match="untracked changes"):
        module.retire(args)
    (lane / "travel-app" / "scratch.txt").unlink()
    (lane / "travel-app" / ".gitignore").write_text("secret.local\n")
    git(lane / "travel-app", "add", ".gitignore")
    git(
        lane / "travel-app", "-c", "user.name=Test",
        "-c", "user.email=test@example.test", "commit", "-qm", "ignore",
    )
    git(
        root / "travel-app", "-c", "user.name=Test",
        "-c", "user.email=test@example.test", "merge", "--no-ff", "-qm",
        "adopt", "codex/fixture",
    )
    git(root / "travel-app", "push", "-q", "origin", "main")
    git(root / "travel-app", "branch", "remote-extra", "codex/fixture")
    git(root / "travel-app", "switch", "-q", "remote-extra")
    git(
        root / "travel-app", "-c", "user.name=Test",
        "-c", "user.email=test@example.test", "commit", "--allow-empty",
        "-qm", "new remote work",
    )
    git(
        root / "travel-app", "push", "-q", "origin",
        "HEAD:refs/heads/codex/fixture",
    )
    git(root / "travel-app", "switch", "-q", "main")
    with pytest.raises(ValueError, match="remote branch has moved"):
        module.retire(args)
    git(root / "travel-app", "push", "-q", "origin", "--delete", "codex/fixture")
    (lane / "travel-app" / "secret.local").write_text("keep")
    with pytest.raises(ValueError, match="ignored files"):
        module.retire(args)
    (lane / "travel-app" / "secret.local").unlink()

    module.retire(args)
    assert lane.exists()
    args.apply = True
    with pytest.raises(ValueError, match="runtime is stopped"):
        module.retire(args)
    args.runtime_stopped = True
    module.retire(args)
    assert not lane.exists()
    for name in ("", "travel-agent", "travel-app"):
        assert "codex/fixture" not in git(root / name, "branch", "--list")
