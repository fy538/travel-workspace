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
import hashlib
import json
import os
import platform
import re
import shlex
import shutil
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_LOG_DIR = WORKSPACE_ROOT / "docs" / "reliability" / "runs"
SCHEMA_VERSION = 1
DIRTY_INPUT_BYTE_LIMIT = 8 * 1024 * 1024
STATUS_BYTE_LIMIT = 1024 * 1024
LOCK_BYTE_LIMIT = 16 * 1024 * 1024
LOCK_FILENAMES = (
    "package-lock.json",
    "pnpm-lock.yaml",
    "yarn.lock",
    "bun.lock",
    "bun.lockb",
    "requirements.txt",
    "requirements-dev.txt",
    "requirements.lock",
    "poetry.lock",
    "uv.lock",
    "Pipfile.lock",
    "Cargo.lock",
    "Gemfile.lock",
)
SAFE_MODE_VALUES = {
    "CI": {"true", "false", "1", "0"},
    "NODE_ENV": {"development", "test", "production"},
    "EXPO_PUBLIC_AUTH_MODE": {"mock", "skip", "real"},
    "EXPO_PUBLIC_USE_MOCK_DATA": {"true", "false", "1", "0"},
    "EXPO_PUBLIC_USE_MOCK_AUTH": {"true", "false", "1", "0"},
    "EXPO_PUBLIC_USE_MOCK_API": {"true", "false", "1", "0"},
    "QA_MODE": {"mock", "real", "before", "after", "oneoff"},
    "TEST_DATABASE_DISPOSABLE": {"true", "false", "1", "0"},
    "EAS_BUILD_PROFILE": {"development", "preview", "production"},
}
VERSION_ARGV = {
    "python": ["--version"],
    "python3": ["--version"],
    "node": ["--version"],
    "npm": ["--version"],
    "npx": ["--version"],
    "make": ["--version"],
    "pytest": ["--version"],
    "ruff": ["--version"],
    "mypy": ["--version"],
    "xcodebuild": ["-version"],
    "xcrun": ["--version"],
    "maestro": ["--version"],
    "docker": ["--version"],
    "docker-compose": ["--version"],
}


def _git_environment() -> dict[str, str]:
    """Ignore inherited repository selectors; path arguments choose the repo."""
    excluded = {
        "GIT_DIR",
        "GIT_WORK_TREE",
        "GIT_COMMON_DIR",
        "GIT_INDEX_FILE",
        "GIT_EXTERNAL_DIFF",
        "GIT_CONFIG_PARAMETERS",
    }
    return {key: value for key, value in os.environ.items() if key not in excluded}


def _child_repo_root(name: str, workspace_root: Path | None = None) -> Path:
    """Resolve only the documented child path inside this workspace/lane.

    Coordinated lanes own three sibling worktrees under one lane directory.
    Falling back to a same-named checkout elsewhere can silently measure a
    different lane, so a missing child remains missing.
    """
    return (workspace_root or WORKSPACE_ROOT) / name


def child_repositories(workspace_root: Path | None = None) -> dict[str, Path]:
    root = workspace_root or WORKSPACE_ROOT
    return {
        "workspace": root,
        "travel-agent": _child_repo_root("travel-agent", root),
        "travel-app": _child_repo_root("travel-app", root),
    }


# ── Repo / environment fingerprinting ───────────────────────────────────


def git_commit(repo_path: Path) -> str | None:
    if not repo_path.exists():
        return None
    try:
        out = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=repo_path,
            env=_git_environment(),
            capture_output=True,
            text=True,
            check=True,
            timeout=10,
        )
        return out.stdout.strip()
    except (
        subprocess.CalledProcessError,
        subprocess.TimeoutExpired,
        FileNotFoundError,
        OSError,
    ):
        return None


def git_dirty(repo_path: Path) -> bool | None:
    if not repo_path.exists():
        return None
    try:
        out = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=repo_path,
            env=_git_environment(),
            capture_output=True,
            text=True,
            check=True,
            timeout=10,
        )
        return bool(out.stdout.strip())
    except (
        subprocess.CalledProcessError,
        subprocess.TimeoutExpired,
        FileNotFoundError,
        OSError,
    ):
        return None


def _git_root(repo_path: Path) -> Path | None:
    if not repo_path.exists():
        return None
    try:
        result = subprocess.run(
            ['git', 'rev-parse', '--show-toplevel'], cwd=repo_path,
            env=_git_environment(), capture_output=True, text=True,
            check=True, timeout=10,
        )
        return Path(result.stdout.strip()).resolve()
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError, OSError):
        return None


def _bounded_output(command: list[str], cwd: Path, limit: int) -> tuple[bytes, bool, int | None]:
    """Read at most limit+1 bytes, terminating oversized producers."""
    try:
        proc = subprocess.Popen(
            command, cwd=cwd, env=_git_environment(),
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
        )
    except (FileNotFoundError, OSError):
        return b'', False, None
    data = bytearray()
    truncated = False
    assert proc.stdout is not None
    try:
        while True:
            chunk = proc.stdout.read(min(64 * 1024, limit - len(data) + 1))
            if not chunk:
                break
            available = max(0, limit - len(data))
            data.extend(chunk[:available])
            if len(chunk) > available:
                truncated = True
                proc.terminate()
                break
    finally:
        proc.stdout.close()
    try:
        return bytes(data), truncated, proc.wait(timeout=2)
    except subprocess.TimeoutExpired:
        proc.kill()
        return bytes(data), True, proc.wait()


def _unknown_dirty_identity(dirty: bool | None = None) -> dict:
    return {
        'sha256': None, 'bytes_hashed': 0, 'truncated': False,
        'status': 'unknown', 'dirty': dirty,
    }


def dirty_input_identity(repo_path: Path) -> dict:
    """Hash bounded Git status/diff and untracked file inputs without exposing contents."""
    digest = hashlib.sha256()
    status, truncated, return_code = _bounded_output(
        ['git', 'status', '--porcelain=v1', '--untracked-files=all', '-z'],
        repo_path, STATUS_BYTE_LIMIT,
    )
    if return_code != 0:
        return _unknown_dirty_identity()
    dirty = bool(status)
    digest.update(b'status\0' + status)
    consumed = len(status)

    diff, diff_truncated, return_code = _bounded_output(
        ['git', '--no-pager', 'diff', '--binary', '--no-ext-diff', '--no-textconv', 'HEAD', '--'],
        repo_path, max(0, DIRTY_INPUT_BYTE_LIMIT - consumed),
    )
    if return_code not in {0, None}:
        return _unknown_dirty_identity(dirty)
    digest.update(b'diff\0' + diff)
    consumed += len(diff)
    truncated = truncated or diff_truncated

    listing, listing_truncated, return_code = _bounded_output(
        ['git', 'ls-files', '--others', '--exclude-standard', '-z'],
        repo_path, min(STATUS_BYTE_LIMIT, max(0, DIRTY_INPUT_BYTE_LIMIT - consumed)),
    )
    if return_code not in {0, None}:
        return _unknown_dirty_identity(dirty)
    truncated = truncated or listing_truncated
    for raw_path in listing.split(b'\0'):
        if not raw_path:
            continue
        metadata = b'untracked\0' + raw_path + b'\0'
        available = max(0, DIRTY_INPUT_BYTE_LIMIT - consumed)
        digest.update(metadata[:available])
        consumed += min(len(metadata), available)
        if len(metadata) > available:
            truncated = True
            break
        path = repo_path / os.fsdecode(raw_path)
        try:
            if path.is_symlink():
                content = os.fsencode(os.readlink(path))
                available = max(0, DIRTY_INPUT_BYTE_LIMIT - consumed)
                digest.update(content[:available])
                consumed += min(len(content), available)
                truncated = truncated or len(content) > available
            elif path.is_file():
                with path.open('rb') as source:
                    while True:
                        available = DIRTY_INPUT_BYTE_LIMIT - consumed
                        if available <= 0:
                            truncated = True
                            break
                        chunk = source.read(min(64 * 1024, available + 1))
                        if not chunk:
                            break
                        digest.update(chunk[:available])
                        consumed += min(len(chunk), available)
                        if len(chunk) > available:
                            truncated = True
                            break
            else:
                return _unknown_dirty_identity(dirty)
        except OSError:
            return _unknown_dirty_identity(dirty)
    return {
        'sha256': digest.hexdigest(), 'bytes_hashed': consumed,
        'truncated': truncated, 'status': 'truncated' if truncated else 'ok',
        'dirty': dirty,
    }


def repo_snapshot(repositories: dict[str, Path] | None = None) -> dict:
    """Capture the resolved repo roots and input identities for this lane."""
    snapshot = {}
    for name, raw_path in (repositories or child_repositories()).items():
        expected = Path(raw_path).resolve(strict=False)
        root = _git_root(expected)
        if root is None or root != expected:
            status = 'missing' if not expected.exists() else 'unresolved' if root is None else 'wrong-repository-root'
            snapshot[name] = {
                'path': str(expected), 'status': status, 'commit': None,
                'branch': None, 'dirty': None, 'dirty_input': _unknown_dirty_identity(),
            }
            continue
        try:
            result = subprocess.run(
                ['git', 'symbolic-ref', '--quiet', '--short', 'HEAD'],
                cwd=expected, env=_git_environment(), capture_output=True,
                text=True, check=False, timeout=10,
            )
            branch = result.stdout.strip() if result.returncode == 0 else None
        except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
            branch = None
        dirty_input = dirty_input_identity(expected)
        snapshot[name] = {
            'path': str(root), 'status': 'ok', 'commit': git_commit(expected),
            'branch': branch, 'dirty': dirty_input['dirty'], 'dirty_input': dirty_input,
        }
    return snapshot


def compare_repo_snapshots(before: dict, after: dict) -> dict:
    changed, unknown = [], []
    for name in sorted(set(before) | set(after)):
        left, right = before.get(name, {}), after.get(name, {})
        a, b = left.get('dirty_input', {}), right.get('dirty_input', {})
        if (
            left.get('status') != 'ok' or right.get('status') != 'ok'
            or left.get('commit') is None or right.get('commit') is None
            or a.get('status') != 'ok' or b.get('status') != 'ok'
        ):
            unknown.append(name)
        elif any(left.get(key) != right.get(key) for key in ('path', 'commit', 'branch', 'dirty')) or a.get('sha256') != b.get('sha256'):
            changed.append(name)
    status = 'unknown' if unknown else 'changed' if changed else 'stable'
    return {'status': status, 'changed_repositories': changed, 'unknown_repositories': unknown}


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


def _redact_argument(value: str) -> str:
    """Redact common credential forms without storing command source bodies."""
    value = re.sub(
        r"(?i)\b((?:api[_-]?key|access[_-]?token|refresh[_-]?token|token|password|passwd|secret|credential|authorization|cookie)\s*[=:]\s*)[^\s,;]+",
        r"\1<redacted>",
        value,
    )
    value = re.sub(
        r"(?i)(bearer\s+)[A-Za-z0-9._~+/-]+",
        r"\1<redacted>",
        value,
    )
    value = re.sub(
        r"(?i)([?&](?:access_token|token|password|secret|api[_-]?key)=)[^&\s]+",
        r"\1<redacted>",
        value,
    )
    if "://" in value:
        try:
            parts = urlsplit(value)
            if parts.netloc and "@" in parts.netloc:
                host = parts.netloc.rsplit("@", maxsplit=1)[1]
                value = urlunsplit(
                    (parts.scheme, f"<redacted>@{host}", parts.path, parts.query, parts.fragment)
                )
        except ValueError:
            pass
    return value


_SENSITIVE_OPTION_RE = re.compile(
    r"(?i)(?:^|[-_])(?:token|password|passwd|secret|credential|authorization|cookie|api[-_]?key)(?:$|[-_=])"
)
_ATTACHED_SECRET_RE = re.compile(
    r"(?i)^((?:--?)?(?:[a-z0-9_-]*[-_])?(?:token|password|passwd|secret|credential|authorization|cookie|api[-_]?key)(?:=|:))(.+)$"
)


def safe_command(command: list[str]) -> list[str]:
    """Retain useful invocation shape while excluding credentials and inline code."""
    safe: list[str] = []
    redact_next = False
    redact_code_next = False
    for argument in command:
        if redact_next:
            safe.append("<redacted>")
            redact_next = False
            continue
        if redact_code_next:
            safe.append("<inline-code-omitted>")
            redact_code_next = False
            continue
        if argument in {"-c", "-e", "-p", "--eval", "--execute", "--print", "--expression"}:
            safe.append(argument)
            redact_code_next = True
            continue
        attached = _ATTACHED_SECRET_RE.match(argument)
        if attached:
            safe.append(f"{attached.group(1)}<redacted>")
            continue
        if argument.startswith("-") and _SENSITIVE_OPTION_RE.search(argument):
            safe.append(argument)
            if "=" not in argument and ":" not in argument:
                redact_next = True
            continue
        safe.append(_redact_argument(argument))
    if redact_next or redact_code_next:
        safe.append("<omitted>")
    return safe


def safe_modes(env: dict[str, str] | None = None) -> dict:
    """Record only explicitly allowlisted mode variables and enum values."""
    source = os.environ if env is None else env
    result = {}
    for key, allowed in SAFE_MODE_VALUES.items():
        if key not in source:
            continue
        normalized = str(source[key]).strip().lower()
        result[key] = {
            "present": True,
            "value": normalized if normalized in allowed else None,
            "status": "known" if normalized in allowed else "unknown",
        }
    return result


def capture_tool_versions(command: list[str]) -> dict:
    """Record a safe version probe for the primary known command, if available."""
    if not command:
        return {"recorder_python": sys.version.split()[0], "primary_command": None}
    requested = command[0]
    name = Path(requested).name
    entry = {
        "name": name,
        "path": shutil.which(requested),
        "version": None,
        "status": "unsupported-version-probe",
    }
    version_args = VERSION_ARGV.get(name)
    if version_args and entry["path"]:
        try:
            result = subprocess.run(
                [entry["path"], *version_args],
                capture_output=True,
                text=True,
                timeout=5,
                check=False,
                env=_git_environment(),
            )
            output = (result.stdout or result.stderr).strip()
            entry["version"] = _redact_argument(output[:240]) if output else None
            entry["status"] = "ok" if result.returncode == 0 and output else "failed"
        except (OSError, subprocess.TimeoutExpired):
            entry["status"] = "unavailable"
    elif entry["path"] is None:
        entry["status"] = "not-found"
    return {
        "recorder_python": sys.version.split()[0],
        "primary_command": entry,
    }


def dependency_lock_identity(repositories: dict[str, Path]) -> dict:
    """Hash known root-level dependency locks without recording their contents."""
    result = {}
    for repo_name, repo_path in repositories.items():
        locks = []
        if not repo_path.is_dir():
            result[repo_name] = locks
            continue
        for filename in LOCK_FILENAMES:
            path = repo_path / filename
            if not path.is_file():
                continue
            digest = hashlib.sha256()
            size = 0
            truncated = False
            try:
                with path.open("rb") as source:
                    while True:
                        chunk = source.read(min(64 * 1024, LOCK_BYTE_LIMIT - size + 1))
                        if not chunk:
                            break
                        available = max(0, LOCK_BYTE_LIMIT - size)
                        digest.update(chunk[:available])
                        size += min(len(chunk), available)
                        if len(chunk) > available:
                            truncated = True
                            break
            except OSError:
                locks.append(
                    {"path": filename, "sha256": None, "bytes_hashed": size, "status": "unknown"}
                )
                continue
            locks.append(
                {
                    "path": filename,
                    "sha256": digest.hexdigest(),
                    "bytes_hashed": size,
                    "truncated": truncated,
                    "status": "truncated" if truncated else "ok",
                }
            )
        result[repo_name] = locks
    return result


def _workspace_bases(workspace_root: Path) -> dict:
    manifest_path = workspace_root / ".workspace-lane.json"
    if not manifest_path.is_file():
        return {}
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    bases = manifest.get("bases")
    return bases if isinstance(bases, dict) else {}


def verification_context(
    workspace_root: Path,
    command: list[str],
    plan: str,
    explicit_bases: dict[str, str],
    modes: dict | None = None,
    locks: dict | None = None,
) -> dict:
    manifest_bases = _workspace_bases(workspace_root)
    bases = {}
    for repo_name in ("workspace", "travel-agent", "travel-app"):
        if repo_name in explicit_bases:
            bases[repo_name] = {"revision": explicit_bases[repo_name], "source": "cli"}
        elif isinstance(manifest_bases.get(repo_name), str):
            bases[repo_name] = {
                "revision": manifest_bases[repo_name],
                "source": "workspace-lane-manifest",
            }
        else:
            bases[repo_name] = {"revision": None, "source": "unknown"}
    return {
        "plan": plan,
        "plan_source": "cli" if plan else "label",
        "bases": bases,
        "tool_versions": capture_tool_versions(command),
        "dependency_locks": (
            dependency_lock_identity(child_repositories(workspace_root))
            if locks is None
            else locks
        ),
        "modes": safe_modes() if modes is None else modes,
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
        # Summary lines begin with counts (optionally surrounded by pytest's
        # '=' banner). Unanchored search retries the optional-prefix pattern
        # at every position of long non-test diagnostics, causing quadratic
        # work on Alembic's single-line constraint reports.
        m = _PYTEST_SUMMARY_RE.match(line.strip("= \t"))
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
        except OSError as exc:
            log_file.write(
                f"\n[measure_verification] command could not start ({type(exc).__name__})\n"
            )
            exit_code = 126
    wall_time = time.monotonic() - start
    return {
        "exit_code": exit_code,
        "timed_out": timed_out,
        "wall_time_seconds": round(wall_time, 3),
        "log_path": str(log_path.relative_to(WORKSPACE_ROOT))
        if log_path.is_relative_to(WORKSPACE_ROOT)
        else str(log_path),
    }


# ── Record assembly ──────────────────────────────────────────────────────


def build_record(
    label: str,
    cmd: list[str],
    run_result: dict,
    repos: dict,
    env: dict,
    log_text: str | None,
    input_identity: dict | None = None,
    verification: dict | None = None,
) -> dict:
    return {
        "schema_version": SCHEMA_VERSION,
        "label": _redact_argument(label),
        "command": safe_command(cmd),
        "repos": repos,
        "environment": env,
        "input_identity": input_identity or {"status": "unknown"},
        "verification": verification or {},
        "exit_code": run_result["exit_code"],
        "timed_out": run_result["timed_out"],
        "wall_time_seconds": run_result["wall_time_seconds"],
        "log_path": _redact_argument(run_result["log_path"]),
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
            raise ValueError(
                f"{path} exists and is not a JSON array — refusing to overwrite"
            )
    else:
        existing = []
    existing.append(record)
    path.write_text(json.dumps(existing, indent=2) + "\n", encoding="utf-8")


# ── CLI ───────────────────────────────────────────────────────────────────


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--label",
        required=True,
        help="short identifier for this command, e.g. 'backend-ci'",
    )
    parser.add_argument(
        "--append-to",
        metavar="PATH",
        help="JSON array file to append this run's record to",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=None,
        help="seconds before the command is killed",
    )
    parser.add_argument(
        "--plan",
        help="selected verification plan name; defaults to --label and is recorded as such",
    )
    parser.add_argument(
        "--base",
        action="append",
        default=[],
        metavar="REPOSITORY=REVISION",
        help="explicit base revision; repeat for workspace, travel-agent, and travel-app",
    )
    parser.add_argument("--log-dir", default=str(DEFAULT_LOG_DIR))
    parser.add_argument("cmd", nargs=argparse.REMAINDER, help="-- <command to run>")
    args = parser.parse_args(argv)

    cmd = args.cmd
    if cmd and cmd[0] == "--":
        cmd = cmd[1:]
    if not cmd:
        parser.error(
            "no command given — usage: measure_verification.py --label X -- <command>"
        )

    safe_label = re.sub(
        r"[^A-Za-z0-9._-]+",
        "-",
        _redact_argument(args.label),
    ).strip("-._")[:120]
    if not safe_label:
        parser.error("--label must contain at least one letter or number")
    explicit_bases = {}
    for raw_base in args.base:
        if "=" not in raw_base:
            parser.error(f"invalid --base {raw_base!r}; expected REPOSITORY=REVISION")
        repo_name, revision = raw_base.split("=", maxsplit=1)
        if repo_name not in {"workspace", "travel-agent", "travel-app"}:
            parser.error(f"unknown repository in --base: {repo_name!r}")
        if not re.fullmatch(r"[A-Za-z0-9._/-]{1,160}", revision):
            parser.error(f"invalid revision in --base for {repo_name!r}")
        explicit_bases[repo_name] = revision

    selected_plan = args.plan.strip() if args.plan and args.plan.strip() else safe_label
    selected_plan = _redact_argument(selected_plan)
    selected_plan = re.sub(r"[^A-Za-z0-9._:/-]+", "-", selected_plan)[:120]
    ts = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    log_path = Path(args.log_dir) / f"{safe_label}-{ts}.log"

    print(
        f"[measure_verification] running: {' '.join(shlex.quote(c) for c in safe_command(cmd))}",
        file=sys.stderr,
    )
    repositories = child_repositories(WORKSPACE_ROOT)
    before = repo_snapshot(repositories)
    locks_before = dependency_lock_identity(repositories)
    modes = safe_modes()
    verification = verification_context(
        WORKSPACE_ROOT,
        cmd,
        selected_plan,
        explicit_bases,
        modes,
        locks_before,
    )
    verification["plan_source"] = "cli" if args.plan else "label"
    verification["dependency_locks_before"] = locks_before
    run_result = run_command(cmd, args.timeout, log_path)

    log_text: str | None
    try:
        log_text = log_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        log_text = None

    after = repo_snapshot(repositories)
    locks_after = dependency_lock_identity(repositories)
    changed_locks = [
        repo_name
        for repo_name in sorted(set(locks_before) | set(locks_after))
        if locks_before.get(repo_name) != locks_after.get(repo_name)
    ]
    verification["dependency_locks_after"] = locks_after
    verification["dependency_locks_stable"] = not changed_locks
    repo_comparison = compare_repo_snapshots(before, after)
    if changed_locks:
        repo_comparison["status"] = "changed"
    input_identity = {
        "status": repo_comparison["status"],
        "before": before,
        "after": after,
        **repo_comparison,
        "changed_dependency_locks": changed_locks,
    }
    record = build_record(
        label=safe_label,
        cmd=cmd,
        run_result=run_result,
        repos=after,
        env=environment_class(),
        log_text=log_text,
        input_identity=input_identity,
        verification=verification,
    )

    print(json.dumps(record, indent=2))

    if args.append_to:
        append_record(Path(args.append_to), record)
        print(f"[measure_verification] appended to {args.append_to}", file=sys.stderr)

    if run_result["timed_out"]:
        print(
            f"[measure_verification] TIMED OUT after {args.timeout}s", file=sys.stderr
        )
        return 1
    # The recorder is often used for evidence collection, but it is also safe
    # to use in a gate: a completed command's exit code is the recorder's exit
    # code. A missing executable is recorded as 127 above, never swallowed.
    command_exit = int(run_result["exit_code"] or 0)
    if command_exit != 0:
        return command_exit
    if input_identity["status"] != "stable":
        print(
            "[measure_verification] input identity is not fully stable; "
            "the command result is retained but this measurement cannot certify a pass",
            file=sys.stderr,
        )
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
