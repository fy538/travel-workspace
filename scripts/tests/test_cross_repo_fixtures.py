from __future__ import annotations

import importlib.util
from pathlib import Path
import shutil
import subprocess
import sys

import pytest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "cross_repo_fixtures", ROOT / "scripts/check_cross_repo_fixtures.py"
)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


@pytest.fixture
def app(tmp_path):
    """Use real committed mobile inputs, never a self-fulfilling fixture."""
    for relative in M.REQUIRED_APP_FILES:
        target = tmp_path / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / "travel-app" / relative, target)
    return tmp_path


def run_check(app, python=None):
    backend = ROOT / "travel-agent"
    venv = backend / ".venv/bin/python"
    interpreter = python or (str(venv) if venv.exists() else sys.executable)
    return M.check(backend, app, interpreter)


def test_real_cross_repo_inputs_agree(app):
    assert run_check(app) == 0


@pytest.mark.parametrize("relative", M.REQUIRED_APP_FILES)
def test_missing_required_input_fails(app, relative):
    (app / relative).unlink()
    assert run_check(app) == 2


@pytest.mark.parametrize("relative", M.REQUIRED_APP_FILES[-2:])
def test_stale_mobile_snapshot_fails(app, relative):
    (app / relative).write_text("{}\n")
    assert run_check(app) == 1


def test_real_enum_drift_fails(app):
    path = app / "types/expense.ts"
    text = path.read_text()
    assert "'itemized'" in text
    path.write_text(text.replace("'itemized'", "'unsupported_split'"))
    assert run_check(app) == 1


def test_missing_interpreter_is_error(app):
    assert run_check(app, str(app / "absent-python")) == 2


def test_crashed_checker_does_not_pass(app, monkeypatch):
    monkeypatch.setattr(
        M.subprocess,
        "run",
        lambda *args, **kwargs: subprocess.CompletedProcess(args, 7),
    )
    assert run_check(app) == 1
