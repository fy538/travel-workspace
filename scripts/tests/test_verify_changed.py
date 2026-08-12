from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "verify_changed.py"
SPEC = importlib.util.spec_from_file_location("verify_changed", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
# verify_changed.py has `from __future__ import annotations` and a
# @dataclass — dataclass's postponed-annotation resolution looks the module
# up via sys.modules[cls.__module__], which only works if the module is
# registered there before exec_module runs (module_from_spec alone doesn't
# register it). Without this line, import fails with
# "AttributeError: 'NoneType' object has no attribute '__dict__'".
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


# ── classify_path: one test per path class ────────────────────────────────


def test_classifies_frontend_ts_and_tsx() -> None:
    assert MODULE.classify_path("travel-app/components/trip/Foo.tsx") == "frontend"
    assert MODULE.classify_path("travel-app/utils/foo.ts") == "frontend"


def test_classifies_backend_py() -> None:
    assert MODULE.classify_path("travel-agent/backend/concierge/agent.py") == "backend"


def test_classifies_docs_md() -> None:
    assert MODULE.classify_path("docs/working/some-note.md") == "docs"


def test_classifies_unknown_path() -> None:
    assert MODULE.classify_path("random/nonsense/file.xyz") == "unknown"
    assert MODULE.classify_path("travel-app/assets/logo.png") == "unknown"


def test_classifies_conftest_as_high_risk() -> None:
    assert MODULE.classify_path("travel-agent/tests/conftest.py") == "high_risk"
    assert MODULE.classify_path("travel-agent/tests/atlas/conftest.py") == "high_risk"


def test_classifies_migrations_as_high_risk() -> None:
    assert (
        MODULE.classify_path("travel-agent/alembic/versions/01648ba7be52_x.py") == "high_risk"
    )


def test_classifies_dependency_manifests_as_high_risk() -> None:
    assert MODULE.classify_path("travel-agent/requirements.txt") == "high_risk"
    assert MODULE.classify_path("travel-agent/requirements-dev.txt") == "high_risk"
    assert MODULE.classify_path("travel-app/package.json") == "high_risk"
    assert MODULE.classify_path("travel-app/package-lock.json") == "high_risk"


def test_classifies_workspace_scripts_as_high_risk() -> None:
    assert MODULE.classify_path("scripts/check_docs.py") == "high_risk"
    assert MODULE.classify_path("travel-agent/scripts/check_imports.py") == "high_risk"
    assert MODULE.classify_path("travel-app/scripts/check-api-boundaries.mjs") == "high_risk"


def test_classifies_api_routes_and_models_as_high_risk() -> None:
    assert MODULE.classify_path("travel-agent/backend/api/routes/trips.py") == "high_risk"
    assert MODULE.classify_path("travel-agent/backend/core/models/trip.py") == "high_risk"


def test_classifies_openapi_snapshots_and_generated_schema_as_high_risk() -> None:
    assert MODULE.classify_path("docs/openapi.json") == "high_risk"
    assert MODULE.classify_path("docs/openapi.app.json") == "high_risk"
    assert MODULE.classify_path("travel-app/utils/api/schema.gen.ts") == "high_risk"


def test_classifies_shared_test_config_as_high_risk() -> None:
    assert MODULE.classify_path("travel-app/jest.config.js") == "high_risk"
    assert MODULE.classify_path("Makefile") == "high_risk"
    assert MODULE.classify_path("travel-agent/Makefile") == "high_risk"
    assert MODULE.classify_path(".pre-commit-config.yaml") == "high_risk"


# ── select_commands: routing decisions per class, and the union case ────


def test_frontend_only_change_selects_verify_fast_and_related_tests() -> None:
    sel = MODULE.select_commands(["travel-app/components/trip/Foo.tsx"])
    assert not sel.fallback_to_verify
    commands = [c for c, _ in sel.commands]
    assert "npm run verify:fast" in commands
    assert any("findRelatedTests" in c and "components/trip/Foo.tsx" in c for c in commands)


def test_backend_only_change_selects_full_backend_ci() -> None:
    sel = MODULE.select_commands(["travel-agent/backend/concierge/agent.py"])
    assert not sel.fallback_to_verify
    commands = [c for c, _ in sel.commands]
    assert "make -C travel-agent ci" in commands
    # the reason must be honest about why: no mapper exists yet
    reason = next(r for c, r in sel.commands if c == "make -C travel-agent ci")
    assert "no dependency-to-test mapper" in reason


def test_docs_only_change_selects_doc_governance_gates() -> None:
    sel = MODULE.select_commands(["docs/working/some-note.md"])
    assert not sel.fallback_to_verify
    commands = [c for c, _ in sel.commands]
    assert any("docs-links-check" in c for c in commands)


def test_mixed_frontend_and_backend_change_unions_both() -> None:
    sel = MODULE.select_commands(
        ["travel-app/components/Foo.tsx", "travel-agent/backend/concierge/agent.py"]
    )
    assert not sel.fallback_to_verify
    commands = [c for c, _ in sel.commands]
    assert "npm run verify:fast" in commands
    assert "make -C travel-agent ci" in commands


def test_high_risk_file_forces_full_verify_even_with_other_changes() -> None:
    sel = MODULE.select_commands(
        ["travel-app/components/Foo.tsx", "travel-agent/requirements.txt"]
    )
    assert sel.fallback_to_verify
    assert sel.commands == [(MODULE.FULL_VERIFY_COMMAND, sel.fallback_reason)]
    assert "requirements.txt" in sel.fallback_reason


def test_unknown_file_forces_full_verify() -> None:
    sel = MODULE.select_commands(["some/random/binary.dat"])
    assert sel.fallback_to_verify
    assert sel.commands == [(MODULE.FULL_VERIFY_COMMAND, sel.fallback_reason)]


def test_empty_change_set_falls_back_to_verify_rather_than_selecting_nothing() -> None:
    sel = MODULE.select_commands([])
    assert sel.fallback_to_verify
    assert sel.commands == [(MODULE.FULL_VERIFY_COMMAND, sel.fallback_reason)]


def test_docs_referencing_a_real_checker_selects_its_test(tmp_path: Path) -> None:
    (tmp_path / "scripts").mkdir()
    (tmp_path / "scripts" / "check_foo.test.py").write_text("")
    doc_text = "Run scripts/check_foo.py to see the ratchet.\n"
    sel = MODULE.select_commands(
        ["docs/working/note.md"],
        doc_texts={"docs/working/note.md": doc_text},
        checker_test_root=tmp_path,
    )
    commands = [c for c, _ in sel.commands]
    assert any("check_foo.test.py" in c for c in commands)


def test_docs_referencing_a_nonexistent_checker_adds_nothing_extra(tmp_path: Path) -> None:
    doc_text = "See scripts/check_totally_made_up_thing.py for details.\n"
    sel = MODULE.select_commands(
        ["docs/working/note.md"],
        doc_texts={"docs/working/note.md": doc_text},
        checker_test_root=tmp_path,
    )
    commands = [c for c, _ in sel.commands]
    assert not any("made_up_thing" in c for c in commands)


# ── referenced_checker_tests: existence-checked, not string-matched ──────


def test_referenced_checker_tests_finds_real_test_file(tmp_path: Path) -> None:
    (tmp_path / "scripts" / "tests").mkdir(parents=True)
    (tmp_path / "scripts" / "tests" / "test_check_foo.py").write_text("")
    refs = MODULE.referenced_checker_tests("see scripts/check_foo.py for the ratchet", root=tmp_path)
    assert "scripts/tests/test_check_foo.py" in refs


def test_referenced_checker_tests_ignores_nonexistent_scripts(tmp_path: Path) -> None:
    refs = MODULE.referenced_checker_tests("see scripts/check_nonexistent_thing.py", root=tmp_path)
    assert refs == []


def test_referenced_checker_tests_dedupes(tmp_path: Path) -> None:
    (tmp_path / "scripts" / "tests").mkdir(parents=True)
    (tmp_path / "scripts" / "tests" / "test_check_foo.py").write_text("")
    text = "scripts/check_foo.py and again scripts/check_foo.py"
    refs = MODULE.referenced_checker_tests(text, root=tmp_path)
    assert len(refs) == len(set(refs))


# ── BASE_REF validation ────────────────────────────────────────────────────


def test_resolve_base_ref_rejects_missing_value() -> None:
    try:
        MODULE.resolve_base_ref(None)
        assert False, "expected BaseRefError"
    except MODULE.BaseRefError as exc:
        assert "required" in str(exc)


def test_resolve_base_ref_rejects_empty_string() -> None:
    try:
        MODULE.resolve_base_ref("   ")
        assert False, "expected BaseRefError"
    except MODULE.BaseRefError:
        pass


def test_resolve_base_ref_rejects_unresolvable_ref() -> None:
    try:
        MODULE.resolve_base_ref("this-branch-does-not-exist-xyz-123")
        assert False, "expected BaseRefError"
    except MODULE.BaseRefError as exc:
        assert "does not resolve" in str(exc)


def test_resolve_base_ref_accepts_head() -> None:
    resolved = MODULE.resolve_base_ref("HEAD")
    assert len(resolved) == 40


# ── dry-run determinism: same diff -> same selection every time ─────────


def test_dry_run_selection_is_deterministic_for_the_same_files() -> None:
    files = ["travel-app/components/Foo.tsx", "travel-agent/backend/concierge/agent.py"]
    first = MODULE.select_commands(list(files))
    second = MODULE.select_commands(list(reversed(files)))  # order of the diff shouldn't matter
    assert first.commands == second.commands
    assert first.fallback_to_verify == second.fallback_to_verify


def test_cli_dry_run_exits_zero_without_running_commands(tmp_path: Path, capsys) -> None:
    # exercise the real CLI end-to-end against this actual repo's git state,
    # using HEAD as base-ref so the diff is empty and the fallback path is
    # exercised without requiring any specific branch topology.
    exit_code = MODULE.main(["--base-ref", "HEAD", "--dry-run"])
    assert exit_code == 0
    out = capsys.readouterr().out
    assert "BASE_REF=HEAD" in out
    assert "selected commands:" in out


def test_cli_exits_nonzero_with_no_base_ref(capsys) -> None:
    exit_code = MODULE.main([])
    assert exit_code == 2
    err = capsys.readouterr().err
    assert "required" in err


def test_wrapper_script_delegates_to_python_module() -> None:
    wrapper = MODULE_PATH.parent / "verify-changed.sh"
    assert wrapper.exists()
    result = subprocess.run(
        [str(wrapper), "--base-ref", "HEAD", "--dry-run"],
        cwd=MODULE.WORKSPACE_ROOT,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert result.returncode == 0
    assert "selected commands:" in result.stdout
