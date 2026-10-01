"""Execute the Make target without assuming CI creates a backend virtualenv."""
from pathlib import Path
import subprocess
import sys

import pytest

ROOT = Path(__file__).resolve().parents[2]


@pytest.mark.parametrize("local_venv", [False, True])
@pytest.mark.parametrize("checker_exit", [0, 1])
def test_occasion_check_runtime_and_failure_propagation(tmp_path, local_venv, checker_exit):
    (tmp_path / "Makefile").write_text((ROOT / "Makefile").read_text())
    (tmp_path / "dogfood.mk").touch()
    scripts = tmp_path / "scripts"
    scripts.mkdir()
    (scripts / "check_occasion_behavior_contract.py").write_text(
        f"print('checker executed')\nraise SystemExit({checker_exit})\n"
    )
    if local_venv:
        executable = tmp_path / "travel-agent/.venv/bin/python"
        executable.parent.mkdir(parents=True)
        executable.symlink_to(sys.executable)
    result = subprocess.run(
        ["make", "occasion-behavior-contract-check"], cwd=tmp_path,
        capture_output=True, text=True,
    )
    assert "checker executed" in result.stdout
    assert (result.returncode == 0) == (checker_exit == 0)


def test_unavailable_explicit_runtime_is_not_a_pass(tmp_path):
    (tmp_path / "Makefile").write_text((ROOT / "Makefile").read_text())
    (tmp_path / "dogfood.mk").touch()
    result = subprocess.run(
        ["make", "occasion-behavior-contract-check", "BACKEND_PYTHON=/missing/python"],
        cwd=tmp_path, capture_output=True, text=True,
    )
    assert result.returncode != 0
