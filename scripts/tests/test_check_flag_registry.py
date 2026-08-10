from __future__ import annotations

import importlib.util
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "check_flag_registry.py"
SPEC = importlib.util.spec_from_file_location("check_flag_registry", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_backend_discovery_finds_literal_ad_hoc_flag_calls(tmp_path: Path) -> None:
    backend = tmp_path / "travel-agent" / "backend"
    source = backend / "core" / "feature_flags.py"
    source.parent.mkdir(parents=True)
    source.write_text(
        'enabled = _truthy("EXAMPLE_ENABLED")\n'
        'disabled = truthy_env("SECOND_FLAG")\n'
    )
    (backend / "tests").mkdir()
    (backend / "tests" / "ignored.py").write_text('_truthy("TEST_ONLY")\n')

    found = MODULE._scan_ad_hoc_flag_calls(backend, tmp_path)

    assert found == {
        "EXAMPLE_ENABLED": ["travel-agent/backend/core/feature_flags.py:1"],
        "SECOND_FLAG": ["travel-agent/backend/core/feature_flags.py:2"],
    }


def test_app_discovery_uses_only_canonical_exported_flag_constants(
    tmp_path: Path,
) -> None:
    flag_file = tmp_path / "travel-app" / "constants" / "featureFlags.ts"
    flag_file.parent.mkdir(parents=True)
    flag_file.write_text(
        "export const CANONICAL_ENABLED = false;\n"
        "export const CANONICAL_STUB = true;\n"
        "const PRIVATE_ENABLED = true;\n"
        "export const NOT_A_SETTING = 1;\n"
        "const inline = process.env.EXPO_PUBLIC_INLINE_ENABLED;\n"
    )

    found = MODULE._scan_app_flag_declarations(flag_file, tmp_path)

    assert found == {
        "CANONICAL_ENABLED": ["travel-app/constants/featureFlags.ts:1"],
        "CANONICAL_STUB": ["travel-app/constants/featureFlags.ts:2"],
    }


def test_full_check_fails_closed_when_a_child_repo_is_missing(
    tmp_path: Path,
) -> None:
    missing = MODULE._missing_cross_repo_inputs(
        tmp_path / "travel-agent",
        tmp_path / "travel-agent" / "backend",
        tmp_path / "travel-app",
        tmp_path / "travel-app" / "constants" / "featureFlags.ts",
    )

    assert missing == ["travel-agent/", "travel-app/"]


def test_main_fails_closed_when_child_checkout_is_missing(
    monkeypatch, capsys, tmp_path: Path
) -> None:
    monkeypatch.setattr(MODULE, "_AGENT_REPO", tmp_path / "travel-agent")
    monkeypatch.setattr(MODULE, "_AGENT_BACKEND", tmp_path / "travel-agent" / "backend")
    monkeypatch.setattr(MODULE, "_APP_REPO", tmp_path / "travel-app")
    monkeypatch.setattr(
        MODULE,
        "_APP_FLAG_FILE",
        tmp_path / "travel-app" / "constants" / "featureFlags.ts",
    )

    assert MODULE.main([]) == 1
    captured = capsys.readouterr()
    assert "CROSS-REPO FLAG CHECK BLOCKED" in captured.err
    assert "travel-agent/" in captured.err
    assert "travel-app/" in captured.err


def test_unregistered_check_combines_backend_and_app_findings(tmp_path: Path) -> None:
    backend = tmp_path / "travel-agent" / "backend"
    backend_source = backend / "core" / "feature_flags.py"
    backend_source.parent.mkdir(parents=True)
    backend_source.write_text('_truthy("BACKEND_ONLY_ENABLED")\n')
    app_flag_file = tmp_path / "travel-app" / "constants" / "featureFlags.ts"
    app_flag_file.parent.mkdir(parents=True)
    app_flag_file.write_text("export const APP_ONLY_ENABLED = false;\n")

    unregistered = MODULE._check_unregistered_flags(
        [{"name": "REGISTERED"}],
        backend_root=backend,
        app_flag_file=app_flag_file,
        workspace_root=tmp_path,
    )

    assert [name for name, _sites in unregistered] == [
        "APP_ONLY_ENABLED",
        "BACKEND_ONLY_ENABLED",
    ]
