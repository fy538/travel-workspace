#!/usr/bin/env python3
"""Resolve physical hardware and content-addressed artifacts for certification."""

from __future__ import annotations

import argparse
import hashlib
import subprocess
import sys
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from pathlib import Path


class PhysicalEvidenceError(ValueError):
    """The requested device or artifact cannot support physical evidence."""


RunCommand = Callable[[Sequence[str]], subprocess.CompletedProcess[str]]


@dataclass(frozen=True)
class PhysicalDevice:
    platform: str
    udid: str
    label: str

    @property
    def receipt_value(self) -> str:
        return f"{self.platform}|{self.udid}|{self.label}"


def _run(command: Sequence[str]) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(command, check=False, capture_output=True, text=True)
    except OSError as exc:
        return subprocess.CompletedProcess(command, 127, "", str(exc))


def _normalized_label(value: str) -> str:
    return " ".join(value.replace("|", "/").split())


def resolve_physical_device(udid: str, *, runner: RunCommand = _run) -> PhysicalDevice:
    """Resolve one UDID from host inventory and reject simulators/emulators."""

    normalized_udid = udid.strip()
    if not normalized_udid:
        raise PhysicalEvidenceError("physical device UDID cannot be empty")

    ios = runner(["xcrun", "xctrace", "list", "devices"])
    if ios.returncode == 0:
        matching = [
            line.strip()
            for line in ios.stdout.splitlines()
            if f"({normalized_udid})" in line or f"[{normalized_udid}]" in line
        ]
        if matching:
            line = matching[0]
            if "simulator" in line.lower():
                raise PhysicalEvidenceError(f"{normalized_udid} resolves to an iOS simulator")
            label = line.replace(f"({normalized_udid})", "").strip()
            return PhysicalDevice("ios", normalized_udid, _normalized_label(label))

    adb = runner(["adb", "devices", "-l"])
    if adb.returncode == 0:
        row = next(
            (
                line.split()
                for line in adb.stdout.splitlines()
                if line.split() and line.split()[0] == normalized_udid
            ),
            None,
        )
        if row is not None:
            if len(row) < 2 or row[1] != "device":
                raise PhysicalEvidenceError(f"Android device {normalized_udid} is not ready")
            qemu = runner(["adb", "-s", normalized_udid, "shell", "getprop", "ro.kernel.qemu"])
            if qemu.returncode != 0 or qemu.stdout.strip().lower() in {"1", "true"}:
                raise PhysicalEvidenceError(f"{normalized_udid} resolves to an Android emulator")
            model_result = runner(
                ["adb", "-s", normalized_udid, "shell", "getprop", "ro.product.model"]
            )
            os_result = runner(
                ["adb", "-s", normalized_udid, "shell", "getprop", "ro.build.version.release"]
            )
            if model_result.returncode != 0 or os_result.returncode != 0:
                raise PhysicalEvidenceError(f"could not read Android identity for {normalized_udid}")
            if not model_result.stdout.strip() or not os_result.stdout.strip():
                raise PhysicalEvidenceError(f"Android identity is incomplete for {normalized_udid}")
            label = _normalized_label(
                f"{model_result.stdout.strip()} / Android {os_result.stdout.strip()}"
            )
            return PhysicalDevice("android", normalized_udid, label)

    raise PhysicalEvidenceError(f"physical device {normalized_udid} is not connected")


def sha256_digest(path: Path) -> str:
    if not path.is_file():
        raise PhysicalEvidenceError(f"artifact does not exist: {path}")
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def artifact_arguments(paths: Sequence[Path], *, not_before: float | None = None) -> list[str]:
    if not paths:
        raise PhysicalEvidenceError("at least one physical artifact path is required")
    names = [path.name for path in paths]
    if len(names) != len(set(names)):
        raise PhysicalEvidenceError("physical artifact basenames must be unique")
    values: list[str] = []
    for path in paths:
        if not path.is_file():
            raise PhysicalEvidenceError(f"artifact does not exist: {path}")
        if not_before is not None and path.stat().st_mtime < not_before:
            raise PhysicalEvidenceError(f"artifact predates this certification run: {path}")
        values.append(f"{path.name}={sha256_digest(path)}")
    return values


def bundle_digest(paths: Sequence[Path]) -> str:
    if not paths:
        raise PhysicalEvidenceError("bundle hash requires at least one file")
    digest = hashlib.sha256()
    for path in paths:
        if not path.is_file():
            raise PhysicalEvidenceError(f"bundle input does not exist: {path}")
        digest.update(path.name.encode())
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return "sha256:" + digest.hexdigest()


def _devices(args: argparse.Namespace) -> None:
    udids = [value.strip() for value in args.udid]
    if len(udids) < 2 or len(set(udids)) != len(udids):
        raise PhysicalEvidenceError("physical certification requires at least two unique UDIDs")
    for udid in udids:
        print(resolve_physical_device(udid).receipt_value)


def _artifacts(args: argparse.Namespace) -> None:
    for value in artifact_arguments(args.path, not_before=args.not_before):
        print(value)


def _digest(args: argparse.Namespace) -> None:
    print(sha256_digest(args.path))


def _bundle(args: argparse.Namespace) -> None:
    print(bundle_digest(args.path))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)

    devices = commands.add_parser("devices")
    devices.add_argument("--udid", action="append", required=True)
    devices.set_defaults(func=_devices)

    artifacts = commands.add_parser("artifacts")
    artifacts.add_argument("--path", action="append", type=Path, required=True)
    artifacts.add_argument("--not-before", type=float)
    artifacts.set_defaults(func=_artifacts)

    digest = commands.add_parser("digest")
    digest.add_argument("--path", type=Path, required=True)
    digest.set_defaults(func=_digest)

    bundle = commands.add_parser("bundle")
    bundle.add_argument("--path", action="append", type=Path, required=True)
    bundle.set_defaults(func=_bundle)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        args.func(args)
    except (OSError, PhysicalEvidenceError) as exc:
        print(f"physical evidence rejected: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
