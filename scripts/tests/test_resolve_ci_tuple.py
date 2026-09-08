from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

SPEC = importlib.util.spec_from_file_location(
    "ci_tuple", Path(__file__).resolve().parents[1] / "resolve_ci_tuple.py"
)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)
LOCK = {"travel-agent": "a" * 40, "travel-app": "b" * 40}


def test_dispatch_checks_triggering_revision_not_old_pin():
    event = {
        "action": "travel-agent-ci-success",
        "client_payload": {"source_repo": "fy538/travel-agent", "source_sha": "c" * 40},
    }
    result = M.resolve_tuple(LOCK, event, "repository_dispatch", "d" * 40)
    assert result["candidate"] == {
        "workspace": "d" * 40,
        "travel-agent": "c" * 40,
        "travel-app": "b" * 40,
    }
    assert result["trigger"]["sha"] == result["candidate"]["travel-agent"]


@pytest.mark.parametrize(
    "source,revision",
    [
        ("outsider/travel-agent", "c" * 40),
        ("fy538/travel-agent", "main"),
        ("fy538/travel-app", "c" * 40),
    ],
)
def test_invalid_source_or_floating_revision_fails(source, revision):
    with pytest.raises(ValueError):
        M.resolve_tuple(
            LOCK,
            {
                "action": "travel-agent-ci-success",
                "client_payload": {"source_repo": source, "source_sha": revision},
            },
            "repository_dispatch",
            "d" * 40,
        )


def test_checkout_mismatch_fails(tmp_path, monkeypatch):
    monkeypatch.setattr(M.subprocess, "check_output", lambda *a, **kw: "e" * 40)
    with pytest.raises(ValueError, match="does not match"):
        M.assert_checkouts({"candidate": {"workspace": "d" * 40}}, tmp_path)
