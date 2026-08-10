from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

import physical_evidence as subject


def _runner(outputs: dict[tuple[str, ...], tuple[int, str]]):
    def run(command):
        returncode, stdout = outputs.get(tuple(command), (127, ""))
        return subprocess.CompletedProcess(command, returncode, stdout, "")

    return run


def test_resolves_named_ios_hardware_and_rejects_simulator() -> None:
    physical = _runner(
        {
            ("xcrun", "xctrace", "list", "devices"): (
                0,
                "Feihu's iPhone (18.6) (00008110-REAL)\n"
                "iPhone 16 Pro Simulator (18.6) (SIM-UUID)\n",
            )
        }
    )
    assert subject.resolve_physical_device("00008110-REAL", runner=physical).receipt_value == (
        "ios|00008110-REAL|Feihu's iPhone (18.6)"
    )
    with pytest.raises(subject.PhysicalEvidenceError, match="simulator"):
        subject.resolve_physical_device("SIM-UUID", runner=physical)


def test_rejects_android_emulator() -> None:
    runner = _runner(
        {
            ("xcrun", "xctrace", "list", "devices"): (127, ""),
            ("adb", "devices", "-l"): (0, "emulator-5554 device model:Pixel\n"),
            ("adb", "-s", "emulator-5554", "shell", "getprop", "ro.kernel.qemu"): (
                0,
                "1\n",
            ),
        }
    )
    with pytest.raises(subject.PhysicalEvidenceError, match="emulator"):
        subject.resolve_physical_device("emulator-5554", runner=runner)


def test_artifacts_are_hashed_and_must_belong_to_current_run(tmp_path: Path) -> None:
    artifact = tmp_path / "walk.png"
    artifact.write_bytes(b"current pixels")
    values = subject.artifact_arguments([artifact], not_before=artifact.stat().st_mtime)
    assert values == [f"walk.png={subject.sha256_digest(artifact)}"]
    with pytest.raises(subject.PhysicalEvidenceError, match="predates"):
        subject.artifact_arguments([artifact], not_before=artifact.stat().st_mtime + 1)


def test_bundle_digest_binds_path_order_and_content(tmp_path: Path) -> None:
    first = tmp_path / "first.yaml"
    second = tmp_path / "second.yaml"
    first.write_text("one")
    second.write_text("two")
    original = subject.bundle_digest([first, second])
    assert original != subject.bundle_digest([second, first])
    second.write_text("changed")
    assert original != subject.bundle_digest([first, second])
