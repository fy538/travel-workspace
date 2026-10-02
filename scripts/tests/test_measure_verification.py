from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "measure_verification.py"
SPEC = importlib.util.spec_from_file_location("measure_verification", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


# ── run_command: timeout, nonzero exit, missing command ──────────────────


def test_run_command_captures_success(tmp_path: Path) -> None:
    log_path = tmp_path / "ok.log"
    result = MODULE.run_command(
        [sys.executable, "-c", "print('hi')"], timeout=10, log_path=log_path
    )
    assert result["exit_code"] == 0
    assert result["timed_out"] is False
    assert result["wall_time_seconds"] >= 0
    assert log_path.exists()
    assert "hi" in log_path.read_text()


def test_run_command_captures_nonzero_exit(tmp_path: Path) -> None:
    log_path = tmp_path / "fail.log"
    result = MODULE.run_command(
        [sys.executable, "-c", "import sys; sys.exit(3)"], timeout=10, log_path=log_path
    )
    assert result["exit_code"] == 3
    assert result["timed_out"] is False


def test_run_command_records_timeout_without_crashing(tmp_path: Path) -> None:
    log_path = tmp_path / "slow.log"
    result = MODULE.run_command(
        [sys.executable, "-c", "import time; time.sleep(5)"],
        timeout=0.2,
        log_path=log_path,
    )
    assert result["timed_out"] is True
    assert result["exit_code"] is None
    assert result["wall_time_seconds"] < 5  # actually killed, didn't wait out the sleep


def test_run_command_handles_missing_executable(tmp_path: Path) -> None:
    log_path = tmp_path / "missing.log"
    result = MODULE.run_command(
        ["this-command-does-not-exist-xyz"], timeout=10, log_path=log_path
    )
    assert result["exit_code"] == 127
    assert result["timed_out"] is False
    assert "not found" in log_path.read_text()


def test_tool_version_receipt_versions_primary_and_marks_children_unknown(
    tmp_path: Path, monkeypatch
) -> None:
    tool = tmp_path / "make"
    tool.write_text("#!/bin/sh\nprintf 'GNU Make 4.4\\n'\n", encoding="utf-8")
    tool.chmod(0o755)
    monkeypatch.setattr(
        MODULE.shutil,
        "which",
        lambda requested: str(tool) if requested == "make" else None,
    )

    versions = MODULE.capture_tool_versions(["make", "verify-changed"])

    assert versions["primary_command"] == {
        "name": "make",
        "path": str(tool),
        "version": "GNU Make 4.4",
        "status": "ok",
    }
    assert versions["transitive_tool_versions"] == {
        "status": "unknown",
        "reason": "child process execution is not traced",
    }
    assert versions["recorder_python"] == sys.version.split()[0]


def test_tool_version_receipt_keeps_probe_failure_and_child_scope_explicit(
    tmp_path: Path, monkeypatch
) -> None:
    tool = tmp_path / "make"
    tool.write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")
    tool.chmod(0o755)
    monkeypatch.setattr(
        MODULE.shutil,
        "which",
        lambda requested: str(tool) if requested == "make" else None,
    )

    def unavailable(*_args, **_kwargs):
        raise MODULE.subprocess.TimeoutExpired([str(tool), "--version"], timeout=5)

    monkeypatch.setattr(MODULE.subprocess, "run", unavailable)
    versions = MODULE.capture_tool_versions(["make", "verify-changed"])

    assert versions["primary_command"]["status"] == "unavailable"
    assert versions["primary_command"]["version"] is None
    assert versions["transitive_tool_versions"]["status"] == "unknown"


# ── parse_test_counts: partial-result behavior ────────────────────────────


def test_parse_pytest_summary_all_passed() -> None:
    log = "collected 213 items\n...\n213 passed, 9 skipped in 27.90s\n"
    counts = MODULE.parse_test_counts(log)
    assert counts["framework"] == "pytest"
    assert counts["passed"] == 213
    assert counts["skipped"] == 9
    assert counts["failed"] == 0


def test_parse_pytest_summary_with_failures() -> None:
    log = "1 failed, 213 passed, 9 skipped, 14553 deselected, 38 warnings in 30.51s\n"
    counts = MODULE.parse_test_counts(log)
    assert counts["framework"] == "pytest"
    assert counts["failed"] == 1
    assert counts["passed"] == 213


def test_parse_pytest_collected_count_when_present() -> None:
    log = "19043 tests collected in 7.67s\n0 passed in 0.01s\n"
    counts = MODULE.parse_test_counts(log)
    assert counts["collected"] == 19043


def test_parse_jest_summary() -> None:
    log = (
        "Test Suites: 2 passed, 2 total\nTests:       15 passed, 15 total\nTime: 3.2s\n"
    )
    counts = MODULE.parse_test_counts(log)
    assert counts["framework"] == "jest"
    assert counts["passed"] == 15
    assert counts["failed"] == 0


def test_parse_test_counts_returns_none_when_unrecognized() -> None:
    """Absence must read as 'not measured', never silently as zero — a
    command whose output isn't pytest/jest (ruff, mypy, a shell script)
    should not report passed=0/failed=0 as if it were an empty test run."""
    assert MODULE.parse_test_counts("All checks passed!\n") is None
    assert MODULE.parse_test_counts("") is None


def test_parse_pytest_banner_summary() -> None:
    counts = MODULE.parse_test_counts("===== 71 passed, 2 skipped in 2.31s =====\n")
    assert counts["passed"] == 71
    assert counts["skipped"] == 2


def test_long_non_test_diagnostic_does_not_stall_summary_parsing() -> None:
    # A separate process gives this regression a hard bound even with the
    # original quadratic regex. This is a synthetic schema diagnostic, not a
    # test result; it must not manufacture counts or mask command failure.
    script = (
        "import runpy\n"
        f"module = runpy.run_path({str(MODULE_PATH)!r})\n"
        "noise = 'ERROR: new upgrade operations: ' + 'CheckConstraint(x), ' * 20000\n"
        "assert module['parse_test_counts'](noise) is None\n"
        "counts = module['parse_test_counts']('5 passed in 0.5s\\n' + noise)\n"
        "assert counts['passed'] == 5\n"
        "record = module['build_record'](label='failure', cmd=['check'], "
        "run_result={'exit_code': 255, 'timed_out': False, 'wall_time_seconds': 1, "
        "'log_path': 'synthetic.log'}, repos={}, env={}, log_text=noise)\n"
        "assert record['exit_code'] == 255 and record['test_counts'] is None\n"
    )
    subprocess.run([sys.executable, "-c", script], check=True, timeout=5)


# ── build_record: JSON schema shape ──────────────────────────────────────


def test_build_record_has_the_documented_shape() -> None:
    run_result = {
        "exit_code": 0,
        "timed_out": False,
        "wall_time_seconds": 1.23,
        "log_path": "docs/reliability/runs/x.log",
    }
    record = MODULE.build_record(
        label="unit-test",
        cmd=["echo", "hi"],
        run_result=run_result,
        repos={"workspace": {"commit": "abc123", "dirty": False}},
        env={"os": "Darwin"},
        log_text="3 passed in 0.01s\n",
    )
    # required top-level keys from the spec: command, commit IDs (via repos),
    # environment class, wall time, exit status, collected/passed/failed/
    # skipped when available, and log path
    for key in (
        "schema_version",
        "label",
        "command",
        "repos",
        "environment",
        "exit_code",
        "timed_out",
        "wall_time_seconds",
        "log_path",
        "test_counts",
    ):
        assert key in record, f"missing required key: {key}"
    assert record["command"] == ["echo", "hi"]
    assert record["repos"]["workspace"]["commit"] == "abc123"
    assert record["test_counts"]["passed"] == 3
    json.dumps(record)  # must be JSON-serializable


def test_build_record_test_counts_is_none_when_log_text_is_none() -> None:
    run_result = {
        "exit_code": 0,
        "timed_out": False,
        "wall_time_seconds": 0.1,
        "log_path": "x.log",
    }
    record = MODULE.build_record(
        label="x", cmd=["true"], run_result=run_result, repos={}, env={}, log_text=None
    )
    assert record["test_counts"] is None


# ── append_record: partial-result / accumulation behavior ────────────────


def test_append_record_creates_new_array_file(tmp_path: Path) -> None:
    path = tmp_path / "baseline.json"
    MODULE.append_record(path, {"label": "run1"})
    data = json.loads(path.read_text())
    assert data == [{"label": "run1"}]


def test_append_record_appends_to_existing_array(tmp_path: Path) -> None:
    path = tmp_path / "baseline.json"
    path.write_text(json.dumps([{"label": "run1"}]))
    MODULE.append_record(path, {"label": "run2"})
    data = json.loads(path.read_text())
    assert data == [{"label": "run1"}, {"label": "run2"}]


def test_append_record_refuses_to_clobber_non_array_content(tmp_path: Path) -> None:
    path = tmp_path / "baseline.json"
    path.write_text(json.dumps({"not": "an array"}))
    try:
        MODULE.append_record(path, {"label": "run1"})
        raise AssertionError("expected ValueError")
    except ValueError as exc:
        assert "not a JSON array" in str(exc)


def test_append_record_recovers_from_corrupt_existing_file(tmp_path: Path) -> None:
    """A partially-written or corrupted baseline file shouldn't crash the
    next measurement run — it should be treated as empty, not fatal."""
    path = tmp_path / "baseline.json"
    path.write_text("{not valid json")
    MODULE.append_record(path, {"label": "run1"})
    data = json.loads(path.read_text())
    assert data == [{"label": "run1"}]


# ── git_commit / git_dirty: missing-repo partial-result behavior ─────────


def test_git_commit_returns_none_for_nonexistent_path(tmp_path: Path) -> None:
    assert MODULE.git_commit(tmp_path / "does-not-exist") is None


def test_git_dirty_returns_none_for_nonexistent_path(tmp_path: Path) -> None:
    assert MODULE.git_dirty(tmp_path / "does-not-exist") is None


def test_dirty_input_identity_is_unknown_when_diff_or_listing_cannot_start(
    tmp_path: Path, monkeypatch
) -> None:
    repo = tmp_path / "repo"
    _initialize_repo(repo)
    original = MODULE._bounded_output

    for unavailable_command in ("--no-pager", "ls-files"):
        def bounded_output(command, cwd, limit, unavailable_command=unavailable_command):
            if command[1] == unavailable_command:
                return b"", False, None
            return original(command, cwd, limit)

        with monkeypatch.context() as patch:
            patch.setattr(MODULE, "_bounded_output", bounded_output)
            identity = MODULE.dirty_input_identity(repo)

        assert identity["status"] == "unknown"
        assert identity["sha256"] is None
        assert identity["dirty"] is False


def test_repo_snapshot_contains_all_three_real_repositories() -> None:
    snapshot = MODULE.repo_snapshot()
    assert set(snapshot) == {"workspace", "travel-agent", "travel-app"}
    assert all(
        entry["commit"] and len(entry["commit"]) == 40 for entry in snapshot.values()
    )


def test_git_commit_resolves_real_workspace_head() -> None:
    # sanity check against the actual repo this test lives in
    commit = MODULE.git_commit(MODULE.WORKSPACE_ROOT)
    assert commit is not None
    assert len(commit) == 40


def _initialize_repo(path: Path, *, lockfile: bool = False) -> None:
    path.mkdir(parents=True, exist_ok=True)
    subprocess.run(["git", "init", "--quiet"], cwd=path, check=True)
    subprocess.run(["git", "config", "user.name", "Verification Test"], cwd=path, check=True)
    subprocess.run(["git", "config", "user.email", "verification@example.invalid"], cwd=path, check=True)
    (path / "README.md").write_text("stable input\n", encoding="utf-8")
    if lockfile:
        (path / "package-lock.json").write_text('{"lockfileVersion": 3}\n', encoding="utf-8")
    subprocess.run(["git", "add", "README.md", "package-lock.json"] if lockfile else ["git", "add", "README.md"], cwd=path, check=True)
    subprocess.run(["git", "commit", "--quiet", "-m", "fixture"], cwd=path, check=True)


def _initialize_lane(path: Path, *, missing: str | None = None) -> None:
    path.mkdir(parents=True, exist_ok=True)
    for name in ("workspace", "travel-agent", "travel-app"):
        if name == missing:
            continue
        repo_path = path if name == "workspace" else path / name
        _initialize_repo(repo_path, lockfile=name == "travel-app")
    (path / ".gitignore").write_text(
        "travel-agent/\ntravel-app/\n.workspace-lane.json\n",
        encoding="utf-8",
    )
    subprocess.run(["git", "add", ".gitignore"], cwd=path, check=True)
    subprocess.run(["git", "commit", "--quiet", "-m", "ignore child repos and lane metadata"], cwd=path, check=True)
    backend = path / "travel-agent"
    if backend.exists():
        (backend / ".gitignore").write_text("requirements-dev.txt\n", encoding="utf-8")
        subprocess.run(["git", "add", ".gitignore"], cwd=backend, check=True)
        subprocess.run(["git", "commit", "--quiet", "-m", "ignore generated lock"], cwd=backend, check=True)
        (backend / "requirements-dev.txt").write_text("pytest==1.0\n", encoding="utf-8")
    (path / ".workspace-lane.json").write_text(
        json.dumps({
            "bases": {
                "workspace": "a" * 40,
                "travel-agent": "b" * 40,
                "travel-app": "c" * 40,
            }
        }),
        encoding="utf-8",
    )


def test_recorder_marks_unchanged_repository_inputs_stable(tmp_path: Path, monkeypatch, capsys) -> None:
    lane = tmp_path / "lane"
    _initialize_lane(lane)
    monkeypatch.setattr(MODULE, "WORKSPACE_ROOT", lane)
    status = MODULE.main([
        "--label", "stable",
        "--log-dir", str(tmp_path / "logs"),
        "--base", f"workspace={'d' * 40}",
        "--plan", "focused-recorder-tests",
        "--", sys.executable, "-c", "pass",
    ])
    record = json.loads(capsys.readouterr().out)
    assert status == 0
    assert record["input_identity"]["status"] == "stable"
    assert record["input_identity"]["before"]["workspace"]["path"] == str(lane.resolve())
    assert record["verification"]["plan"] == "focused-recorder-tests"
    assert record["verification"]["plan_source"] == "cli"
    assert record["verification"]["bases"]["workspace"] == {
        "revision": "d" * 40,
        "source": "cli",
    }
    assert record["verification"]["bases"]["travel-agent"]["source"] == "workspace-lane-manifest"
    assert record["verification"]["dependency_locks"]["travel-app"][0]["sha256"]


def test_recorder_detects_repository_input_modified_during_command(
    tmp_path: Path, monkeypatch, capsys
) -> None:
    lane = tmp_path / "lane"
    _initialize_lane(lane)
    monkeypatch.setattr(MODULE, "WORKSPACE_ROOT", lane)
    status = MODULE.main([
        "--label", "mutated",
        "--log-dir", str(tmp_path / "logs"),
        "--", sys.executable, "-c",
        "from pathlib import Path; Path('README.md').write_text('changed during run\\n')",
    ])
    record = json.loads(capsys.readouterr().out)
    assert status == 2
    assert record["exit_code"] == 0
    assert record["input_identity"]["status"] == "changed"
    assert record["input_identity"]["changed_repositories"] == ["workspace"]


def test_recorder_detects_lockfile_changed_even_when_git_ignores_it(
    tmp_path: Path, monkeypatch, capsys
) -> None:
    lane = tmp_path / "lane"
    _initialize_lane(lane)
    monkeypatch.setattr(MODULE, "WORKSPACE_ROOT", lane)
    status = MODULE.main([
        "--label", "mutated-lock",
        "--log-dir", str(tmp_path / "logs"),
        "--", sys.executable, "-c",
        "from pathlib import Path; Path('travel-agent/requirements-dev.txt').write_text('pytest==2.0\\n')",
    ])
    record = json.loads(capsys.readouterr().out)
    assert status == 2
    assert record["input_identity"]["status"] == "changed"
    assert record["input_identity"]["changed_repositories"] == []
    assert record["input_identity"]["changed_dependency_locks"] == ["travel-agent"]
    assert record["verification"]["dependency_locks_stable"] is False


def test_recorder_does_not_fall_back_to_a_sibling_when_a_child_is_missing(
    tmp_path: Path, monkeypatch, capsys
) -> None:
    lane = tmp_path / "lane"
    _initialize_lane(lane, missing="travel-agent")
    sibling = tmp_path / "travel-agent"
    _initialize_repo(sibling)
    monkeypatch.setattr(MODULE, "WORKSPACE_ROOT", lane)
    status = MODULE.main([
        "--label", "missing-child",
        "--log-dir", str(tmp_path / "logs"),
        "--", sys.executable, "-c", "pass",
    ])
    record = json.loads(capsys.readouterr().out)
    assert status == 2
    assert record["exit_code"] == 0
    assert record["input_identity"]["status"] == "unknown"
    assert record["input_identity"]["before"]["travel-agent"]["status"] == "missing"
    assert record["input_identity"]["before"]["travel-agent"]["path"] == str(
        (lane / "travel-agent").resolve()
    )


def test_recorder_retains_completed_command_failure_and_missing_tool(
    tmp_path: Path, monkeypatch, capsys
) -> None:
    lane = tmp_path / "lane"
    _initialize_lane(lane)
    monkeypatch.setattr(MODULE, "WORKSPACE_ROOT", lane)
    status = MODULE.main([
        "--label", "command-failure",
        "--log-dir", str(tmp_path / "logs"),
        "--append-to", str(tmp_path / "failures.json"),
        "--", sys.executable, "-c", "import sys; sys.exit(13)",
    ])
    failed = json.loads(capsys.readouterr().out)
    assert status == 13
    assert failed["exit_code"] == 13
    assert failed["input_identity"]["status"] == "stable"

    missing_status = MODULE.main([
        "--label", "tool-failure",
        "--log-dir", str(tmp_path / "logs"),
        "--append-to", str(tmp_path / "failures.json"),
        "--", "measure-verification-missing-tool",
    ])
    missing = json.loads(capsys.readouterr().out)
    records = json.loads((tmp_path / "failures.json").read_text(encoding="utf-8"))
    assert missing_status == 127
    assert missing["exit_code"] == 127
    assert missing["verification"]["tool_versions"]["primary_command"]["status"] == "not-found"
    assert missing["verification"]["tool_versions"]["transitive_tool_versions"]["status"] == "unknown"
    assert [record["label"] for record in records] == ["command-failure", "tool-failure"]


def test_receipt_redacts_credentials_inline_source_and_unapproved_modes(monkeypatch) -> None:
    command = [
        "node", "script.mjs", "--token=secret-token", "--password", "private-value",
        "https://example.invalid/?access_token=query-secret", "-c", "SOURCE_CONTENT",
    ]
    safe = MODULE.safe_command(command)
    assert "secret-token" not in json.dumps(safe)
    assert "private-value" not in json.dumps(safe)
    assert "query-secret" not in json.dumps(safe)
    assert "SOURCE_CONTENT" not in json.dumps(safe)
    assert "<inline-code-omitted>" in safe

    modes = MODULE.safe_modes({
        "EXPO_PUBLIC_AUTH_MODE": "real",
        "QA_MODE": "private-user-data",
        "EXPO_PUBLIC_API_URL": "https://user:password@example.invalid/token-secret",
        "API_TOKEN": "secret-token",
    })
    assert modes["EXPO_PUBLIC_AUTH_MODE"]["value"] == "real"
    assert modes["QA_MODE"] == {"present": True, "value": None, "status": "unknown"}
    assert "EXPO_PUBLIC_API_URL" not in modes
    assert "API_TOKEN" not in modes
    assert "password" not in json.dumps(modes)
    record = MODULE.build_record(
        label="password=label-secret",
        cmd=command,
        run_result={
            "exit_code": 13,
            "timed_out": False,
            "wall_time_seconds": 0.2,
            "log_path": "/tmp/access_token=path-secret.log",
        },
        repos={},
        env=modes,
        log_text=None,
    )
    serialized = json.dumps(record)
    for secret in (
        "secret-token",
        "private-value",
        "query-secret",
        "SOURCE_CONTENT",
        "label-secret",
        "path-secret",
    ):
        assert secret not in serialized
    assert record["exit_code"] == 13


# ── CLI end-to-end ────────────────────────────────────────────────────────


def test_main_runs_command_and_prints_valid_json(tmp_path: Path, capsys) -> None:
    exit_code = MODULE.main(
        [
            "--label",
            "cli-test",
            "--log-dir",
            str(tmp_path),
            "--",
            sys.executable,
            "-c",
            "print('ok')",
        ]
    )
    assert exit_code == 0
    out = capsys.readouterr().out
    record = json.loads(out)
    assert record["label"] == "cli-test"
    assert record["exit_code"] == 0


def test_main_appends_to_file_when_requested(tmp_path: Path, capsys) -> None:
    append_path = tmp_path / "baseline.json"
    MODULE.main(
        [
            "--label",
            "rep1",
            "--log-dir",
            str(tmp_path),
            "--append-to",
            str(append_path),
            "--",
            sys.executable,
            "-c",
            "print('ok')",
        ]
    )
    capsys.readouterr()
    MODULE.main(
        [
            "--label",
            "rep2",
            "--log-dir",
            str(tmp_path),
            "--append-to",
            str(append_path),
            "--",
            sys.executable,
            "-c",
            "print('ok')",
        ]
    )
    data = json.loads(append_path.read_text())
    assert [r["label"] for r in data] == ["rep1", "rep2"]


def test_main_returns_nonzero_and_records_timeout(tmp_path: Path, capsys) -> None:
    exit_code = MODULE.main(
        [
            "--label",
            "cli-timeout",
            "--log-dir",
            str(tmp_path),
            "--timeout",
            "0.2",
            "--",
            sys.executable,
            "-c",
            "import time; time.sleep(5)",
        ]
    )
    assert exit_code == 1
    record = json.loads(capsys.readouterr().out)
    assert record["timed_out"] is True
    assert record["exit_code"] is None


def test_main_propagates_completed_command_failure(tmp_path: Path, capsys) -> None:
    exit_code = MODULE.main(
        [
            "--label",
            "cli-failure",
            "--log-dir",
            str(tmp_path),
            "--",
            sys.executable,
            "-c",
            "import sys; sys.exit(13)",
        ]
    )
    assert exit_code == 13
    record = json.loads(capsys.readouterr().out)
    assert record["exit_code"] == 13


def test_main_rejects_missing_command() -> None:
    try:
        MODULE.main(["--label", "no-cmd"])
        raise AssertionError("expected SystemExit from argparse error()")
    except SystemExit as exc:
        assert exc.code != 0


def test_identity_ignores_foreign_git_environment(tmp_path, monkeypatch) -> None:
    import subprocess
    repos = []
    for name in ("one", "two"):
        repo = tmp_path / name
        repo.mkdir()
        for args in (["init", "-q"], ["-c", "user.name=Test", "-c", "user.email=test@example.test", "commit", "--allow-empty", "-qm", name]):
            subprocess.run(["git", "-C", str(repo), *args], check=True)
        repos.append(repo)
    expected = MODULE.git_commit(repos[1])
    monkeypatch.setenv("GIT_DIR", str(repos[0] / ".git"))
    monkeypatch.setenv("GIT_WORK_TREE", str(repos[0]))
    (repos[1] / "untracked").write_text("dirty")
    assert MODULE.git_commit(repos[1]) == expected
    assert MODULE.git_dirty(repos[1]) is True
