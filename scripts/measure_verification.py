#!/usr/bin/env python3
"""Run one verification command and record structured evidence: the exact
command, the commit each repo in the workspace was at, an environment
fingerprint, wall time, exit status, parsed test counts when the output
looks like pytest/jest, and the path to the full captured log.

This exists because "the verification loop is trustworthy and fast" was an
assumption, not a measurement — see
docs/working/codebase-architecture-and-agent-velocity-research-2026-08-11.md,
A2. Every claim about loop speed downstream of this tool should point at a
record this script produced, not a remembered number.

Usage:
    python3 scripts/measure_verification.py --label doctor -- make doctor
    python3 scripts/measure_verification.py --label backend-ci \\
        --append-to docs/reliability/test-loop-baseline.json \\
        -- make -C travel-agent ci
    python3 scripts/measure_verification.py --label backend-ci --timeout 1800 -- make -C travel-agent ci

A run that times out is recorded, not discarded: ``timed_out: true``,
``exit_code: null``. A run whose repos aren't in the state you expect is
still recorded — record the actual commits, don't assume them.
"""

from __future__ import annotations

import argparse
import json
import os
import platform
import re
import shlex
import subprocess
import sys
import time
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_LOG_DIR = WORKSPACE_ROOT / "docs" / "reliability" / "runs"
SCHEMA_VERSION = 1

CHILD_REPOS = {
    "workspace": WORKSPACE_ROOT,
    "travel-agent": WORKSPACE_ROOT / "travel-agent",
    "travel-app": WORKSPACE_ROOT / "travel-app",
}


# ── Repo / environment fingerprinting ───────────────────────────────────


def git_commit(repo_path: Path) -> str | None:
    if not repo_path.exists():
        return None
    try:
        out = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=repo_path,
            capture_output=True,
            text=True,
            check=True,
            timeout=10,
        )
        return out.stdout.strip()
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError, OSError):
        return None


def git_dirty(repo_path: Path) -> bool | None:
    if not repo_path.exists():
        return None
    try:
        out = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=repo_path,
            capture_output=True,
            text=True,
            check=True,
            timeout=10,
        )
        return bool(out.stdout.strip())
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError, OSError):
        return None


def repo_snapshot() -> dict:
    return {
        name: {"commit": git_commit(path), "dirty": git_dirty(path)}
        for name, path in CHILD_REPOS.items()
    }


def environment_class() -> dict:
    """A coarse fingerprint, not a full inventory — enough to tell whether
    two runs are comparable (same machine class) without pinning every
    installed package version."""
    cpu_count = os.cpu_count()
    return {
        "os": platform.system(),
        "os_release": platform.release(),
        "machine": platform.machine(),
        "python_version": platform.python_version(),
        "cpu_count": cpu_count,
    }


# ── Test-count parsing (best-effort; absence is not an error) ───────────

_PYTEST_SUMMARY_RE = re.compile(
    r"(?:(?P<failed>\d+) failed, )?(?:(?P<passed>\d+) passed)?(?:, (?P<skipped>\d+) skipped)?"
    r"(?:, (?P<errors>\d+) error)?.*?in [\d.]+s"
)
_PYTEST_COLLECTED_RE = re.compile(r"(\d+) tests? collected")
_JEST_SUITE_RE = re.compile(
    r"Test Suites:\s*(?:(?P<failed>\d+) failed, )?(?:(?P<passed>\d+) passed, )?(?P<total>\d+) total"
)
_JEST_TEST_RE = re.compile(
    r"Tests:\s*(?:(?P<failed>\d+) failed, )?(?:(?P<skipped>\d+) skipped, )?"
    r"(?:(?P<passed>\d+) passed, )?(?P<total>\d+) total"
)


def parse_test_counts(log_text: str) -> dict | None:
    """Best-effort extraction of collected/passed/failed/skipped from
    pytest or jest output. Returns None rather than a partial/misleading
    dict when nothing recognizable is found — a missing count must read as
    "not measured", never as zero."""
    jest_match = _JEST_TEST_RE.search(log_text)
    if jest_match:
        g = jest_match.groupdict()
        return {
            "framework": "jest",
            "collected": int(g["total"]),
            "passed": int(g["passed"]) if g["passed"] else None,
            "failed": int(g["failed"]) if g["failed"] else 0,
            "skipped": int(g["skipped"]) if g["skipped"] else 0,
        }

    pytest_match = None
    for line in reversed(log_text.splitlines()):
        m = _PYTEST_SUMMARY_RE.search(line)
        if m and (m.group("passed") or m.group("failed") or m.group("errors")):
            pytest_match = m
            break
    if pytest_match:
        g = pytest_match.groupdict()
        collected_match = _PYTEST_COLLECTED_RE.search(log_text)
        return {
            "framework": "pytest",
            "collected": int(collected_match.group(1)) if collected_match else None,
            "passed": int(g["passed"]) if g["passed"] else 0,
            "failed": int(g["failed"]) if g["failed"] else 0,
            "skipped": int(g["skipped"]) if g["skipped"] else 0,
            "errors": int(g["errors"]) if g["errors"] else 0,
        }

    return None


# ── Command execution ────────────────────────────────────────────────────


def run_command(cmd: list[str], timeout: float | None, log_path: Path) -> dict:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    start = time.monotonic()
    timed_out = False
    exit_code: int | None
    with open(log_path, "w", encoding="utf-8") as log_file:
        try:
            proc = subprocess.run(
                cmd,
                cwd=WORKSPACE_ROOT,
                stdout=log_file,
                stderr=subprocess.STDOUT,
                timeout=timeout,
            )
            exit_code = proc.returncode
        except subprocess.TimeoutExpired:
            timed_out = True
            exit_code = None
        except FileNotFoundError as exc:
            log_file.write(f"\n[measure_verification] command not found: {exc}\n")
            exit_code = 127
    wall_time = time.monotonic() - start
    return {
        "exit_code": exit_code,
        "timed_out": timed_out,
        "wall_time_seconds": round(wall_time, 3),
        "log_path": str(log_path.relative_to(WORKSPACE_ROOT)) if log_path.is_relative_to(WORKSPACE_ROOT) else str(log_path),
    }


# ── Record assembly ──────────────────────────────────────────────────────


def build_record(label: str, cmd: list[str], run_result: dict, repos: dict, env: dict, log_text: str | None) -> dict:
    return {
        "schema_version": SCHEMA_VERSION,
        "label": label,
        "command": cmd,
        "repos": repos,
        "environment": env,
        "exit_code": run_result["exit_code"],
        "timed_out": run_result["timed_out"],
        "wall_time_seconds": run_result["wall_time_seconds"],
        "log_path": run_result["log_path"],
        "test_counts": parse_test_counts(log_text) if log_text is not None else None,
    }


def append_record(path: Path, record: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        try:
            existing = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            existing = []
        if not isinstance(existing, list):
            raise ValueError(f"{path} exists and is not a JSON array — refusing to overwrite")
    else:
        existing = []
    existing.append(record)
    path.write_text(json.dumps(existing, indent=2) + "\n", encoding="utf-8")


# ── CLI ───────────────────────────────────────────────────────────────────


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--label", required=True, help="short identifier for this command, e.g. 'backend-ci'")
    parser.add_argument("--append-to", metavar="PATH", help="JSON array file to append this run's record to")
    parser.add_argument("--timeout", type=float, default=None, help="seconds before the command is killed")
    parser.add_argument("--log-dir", default=str(DEFAULT_LOG_DIR))
    parser.add_argument("cmd", nargs=argparse.REMAINDER, help="-- <command to run>")
    args = parser.parse_args(argv)

    cmd = args.cmd
    if cmd and cmd[0] == "--":
        cmd = cmd[1:]
    if not cmd:
        parser.error("no command given — usage: measure_verification.py --label X -- <command>")

    ts = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    log_path = Path(args.log_dir) / f"{args.label}-{ts}.log"

    print(f"[measure_verification] running: {' '.join(shlex.quote(c) for c in cmd)}", file=sys.stderr)
    run_result = run_command(cmd, args.timeout, log_path)

    log_text: str | None
    try:
        log_text = log_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        log_text = None

    record = build_record(
        label=args.label,
        cmd=cmd,
        run_result=run_result,
        repos=repo_snapshot(),
        env=environment_class(),
        log_text=log_text,
    )

    print(json.dumps(record, indent=2))

    if args.append_to:
        append_record(Path(args.append_to), record)
        print(f"[measure_verification] appended to {args.append_to}", file=sys.stderr)

    if run_result["timed_out"]:
        print(f"[measure_verification] TIMED OUT after {args.timeout}s", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
