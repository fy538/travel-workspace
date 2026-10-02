from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest


SCRIPTS_DIR = Path(__file__).resolve().parents[1]
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))
MODULE_PATH = SCRIPTS_DIR / "render_current_state.py"
SPEC = importlib.util.spec_from_file_location("render_current_state", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_current_state_check_accepts_the_generated_document(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(sys, "argv", [str(MODULE_PATH)])

    assert MODULE.main() == 0


def test_current_state_check_rejects_stale_generated_block(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setattr(sys, "argv", [str(MODULE_PATH)])
    original = MODULE.DOC.read_text()
    stale_marker = "<!-- Run `make docs-status-sync` to update this block. -->"
    assert stale_marker in original
    stale_doc = tmp_path / "current-state.md"
    stale_doc.write_text(
        original.replace(stale_marker, "<!-- stale generated block -->", 1)
    )
    monkeypatch.setattr(MODULE, "DOC", stale_doc)

    assert MODULE.main() == 1
    assert "current-state drift" in capsys.readouterr().out
