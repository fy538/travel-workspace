#!/usr/bin/env python3
"""Check real mobile enums and generated dogfood snapshots against backend owners.

Run in the coordinated workspace, never silently skip a missing child/input.
Backend standalone tests exercise parsers and backend snapshots independently.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_APP_FILES = (
    "types/booking.ts",
    "types/expense.ts",
    "types/photos.ts",
    "constants/personas/generated/canonical-personas.json",
    "constants/mocks/generated/canonical-angles.json",
)


def check(backend: Path, app: Path, python: str) -> int:
    required = [backend / "scripts/check_enum_parity.py"]
    required.extend(app / name for name in REQUIRED_APP_FILES)
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        print(
            "ERROR: required cross-repository inputs missing:\n" + "\n".join(missing),
            file=sys.stderr,
        )
        return 2
    env = {
        **os.environ,
        "TRAVEL_APP_ROOT": str(app.resolve()),
        "PYTHONPATH": str(backend.resolve()),
    }
    commands = (
        [python, "scripts/check_enum_parity.py", "--ci"],
        [python, "-m", "tools.dogfood.content.export_frontend_personas", "--check"],
        [python, "-m", "tools.dogfood.content.export_frontend_angles", "--check"],
    )
    for command in commands:
        try:
            result = subprocess.run(command, cwd=backend, env=env, check=False)
        except OSError as exc:
            print(f"ERROR: cannot execute {command[0]}: {exc}", file=sys.stderr)
            return 2
        if result.returncode:
            return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--backend", type=Path, default=ROOT / "travel-agent")
    parser.add_argument("--app", type=Path, default=ROOT / "travel-app")
    parser.add_argument("--python", help="Backend dependency environment's interpreter")
    args = parser.parse_args()
    venv = args.backend / ".venv/bin/python"
    python = args.python or (str(venv.absolute()) if venv.exists() else sys.executable)
    return check(args.backend.resolve(), args.app.resolve(), python)


if __name__ == "__main__":
    raise SystemExit(main())
