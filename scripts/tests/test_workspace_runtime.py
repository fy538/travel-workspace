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
