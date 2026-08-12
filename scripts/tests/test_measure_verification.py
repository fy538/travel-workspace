from __future__ import annotations

import importlib.util
import json
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
        assert False, "expected ValueError"
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
        assert False, "expected SystemExit from argparse error()"
    except SystemExit as exc:
        assert exc.code != 0
