from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from unittest import mock


SCRIPT = Path(__file__).parents[1] / "clerk_dogfood_sessions.py"
SPEC = importlib.util.spec_from_file_location("clerk_dogfood_sessions", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def test_runs_child_with_private_tokens_and_revokes_sessions(monkeypatch):
    monkeypatch.setenv("CLERK_SECRET_KEY", "test-secret")
    calls: list[tuple[str, str]] = []

    def fake_request(_secret, method, path, body=None):
        calls.append((method, path))
        if path == "/sessions":
            return {"id": f"sess-{body['user_id']}"}
        if path.endswith("/tokens"):
            return {"jwt": f"jwt-{path.split('/')[2]}"}
        return {"status": "revoked"}

    child = mock.Mock(return_value=mock.Mock(returncode=0))
    monkeypatch.setattr(MODULE, "_request", fake_request)
    monkeypatch.setattr(MODULE.subprocess, "run", child)

    result = MODULE.main(
        [
            "--persona-env",
            "mara=PRELAUNCH_JWT_MARA",
            "--persona-env",
            "dao=PRELAUNCH_JWT_DAO",
            "--",
            "python",
            "cert.py",
        ]
    )

    assert result == 0
    child_env = child.call_args.kwargs["env"]
    assert child_env["PRELAUNCH_JWT_MARA"].startswith("jwt-sess-")
    assert child_env["PRELAUNCH_JWT_DAO"].startswith("jwt-sess-")
    assert "CLERK_SECRET_KEY" not in child_env
    assert calls[-2][1].endswith("/revoke")
    assert calls[-1][1].endswith("/revoke")


def test_preserves_supplied_token_without_creating_a_session(monkeypatch):
    monkeypatch.setenv("CLERK_SECRET_KEY", "test-secret")
    monkeypatch.setenv("PRELAUNCH_JWT_MARA", "existing-token")
    request = mock.Mock()
    child = mock.Mock(return_value=mock.Mock(returncode=0))
    monkeypatch.setattr(MODULE, "_request", request)
    monkeypatch.setattr(MODULE.subprocess, "run", child)

    result = MODULE.main(
        ["--persona-env", "mara=PRELAUNCH_JWT_MARA", "--", "python", "cert.py"]
    )

    assert result == 0
    assert child.call_args.kwargs["env"]["PRELAUNCH_JWT_MARA"] == "existing-token"
    request.assert_not_called()


def test_missing_secret_does_not_start_child(monkeypatch):
    monkeypatch.delenv("CLERK_SECRET_KEY", raising=False)
    child = mock.Mock(return_value=mock.Mock(returncode=0))
    monkeypatch.setattr(MODULE.subprocess, "run", child)

    result = MODULE.main(
        ["--persona-env", "mara=PRELAUNCH_JWT_MARA", "--", "python", "cert.py"]
    )

    assert result == 2
    child.assert_not_called()
