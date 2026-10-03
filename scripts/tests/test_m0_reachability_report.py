from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

SCRIPT = ROOT / "scripts/m0_reachability_report.py"
SPEC = importlib.util.spec_from_file_location("m0_reachability_report", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def test_occasion_gate_uses_shared_backend_interpreter_resolver(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    seen: list[Path] = []

    def resolve(backend_root: Path) -> str:
        seen.append(backend_root)
        return "/hostedtoolcache/Python/3.13.15/bin/python"

    monkeypatch.setattr(MODULE, "resolve_backend_python", resolve)

    command = next(
        command for name, command in MODULE.gate_commands() if name == "occasion-behavior"
    )

    assert seen == [ROOT / "travel-agent"]
    assert command == (
        "/hostedtoolcache/Python/3.13.15/bin/python",
        "scripts/check_occasion_behavior_contract.py",
    )


def test_missing_interpreter_is_reported_as_error_evidence(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def missing_tool(command: tuple[str, ...], **_kwargs: object) -> None:
        raise FileNotFoundError(2, "No such file or directory", command[0])

    monkeypatch.setattr(MODULE.subprocess, "run", missing_tool)

    result = MODULE.run_gate("occasion-behavior", ("python3.13", "checker.py"), 5)

    assert result["status"] == "error"
    assert result["returncode"] is None
    assert "FileNotFoundError" in result["output_tail"]
    assert "python3.13" in result["output_tail"]


def test_nonzero_checker_exit_preserves_failure_and_output(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def failing_tool(_command: tuple[str, ...], **_kwargs: object) -> SimpleNamespace:
        return SimpleNamespace(
            returncode=23,
            stdout="checker started",
            stderr="contract mismatch",
        )

    monkeypatch.setattr(MODULE.subprocess, "run", failing_tool)

    result = MODULE.run_gate("occasion-behavior", ("python", "checker.py"), 5)

    assert result["status"] == "fail"
    assert result["returncode"] == 23
    assert "checker started" in result["output_tail"]
    assert "contract mismatch" in result["output_tail"]


def test_report_exits_nonzero_and_emits_spawn_error(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    def missing_tool(command: tuple[str, ...], **_kwargs: object) -> None:
        raise FileNotFoundError(2, "No such file or directory", command[0])

    monkeypatch.setattr(
        MODULE,
        "gate_commands",
        lambda: (("occasion-behavior", ("python3.13", "checker.py")),),
    )
    monkeypatch.setattr(MODULE.subprocess, "run", missing_tool)

    assert MODULE.main(["--json"]) == 1
    result = json.loads(capsys.readouterr().out)["gates"][0]

    assert result["status"] == "error"
    assert result["returncode"] is None
    assert "FileNotFoundError" in result["output_tail"]
