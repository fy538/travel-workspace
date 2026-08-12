#!/usr/bin/env python3
"""Change-scoped fast path for the pre-push gate. Classifies files changed
since BASE_REF and selects the smallest set of commands that still covers
the change — falling back to the full `make verify` for anything
unrecognized or historically risky.

This does not replace `make verify` as the required pre-push/merge gate.
It exists to make routine, narrowly-scoped changes fast to verify locally
before the full gate runs — see
docs/working/codebase-architecture-and-agent-velocity-research-2026-08-11.md,
A2.

Usage:
    scripts/verify-changed.sh --base-ref origin/main
    scripts/verify-changed.sh --base-ref origin/main --dry-run
    python3 scripts/verify_changed.py --base-ref HEAD~1 --dry-run

Exits nonzero immediately if BASE_REF is missing or does not resolve to a
commit — it never guesses `main`, especially not in a dirty concurrent
worktree where "main" may not mean what the caller expects.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent

# ── Path classification ──────────────────────────────────────────────────
#
# Order matters: HIGH_RISK is checked first and, if matched by ANY changed
# file, short-circuits the whole selection to `make verify` regardless of
# what else changed. The remaining classes are additive — a change set
# touching both a frontend and a backend file selects the union of both.

HIGH_RISK_PATTERNS = [
    # shared test configuration / harness
    r"(^|/)conftest\.py$",
    r"(^|/)jest\.config\.[jt]s$",
    r"(^|/)pytest\.ini$",
    r"^travel-agent/pyproject\.toml$",
    r"^\.pre-commit-config\.yaml$",
    r"^travel-agent/\.pre-commit-config\.yaml$",
    r"^travel-app/\.pre-commit-config\.yaml$",
    r"(^|/)Makefile$",
    # migrations
    r"^travel-agent/alembic/versions/.*\.py$",
    # dependency manifests
    r"^travel-agent/requirements.*\.txt$",
    r"^travel-app/package(-lock)?\.json$",
    r"^travel-app/poetry\.lock$",
    # workspace-level and child-repo top-level scripts/ (the gates themselves)
    r"^scripts/.*\.(py|sh|mjs)$",
    r"^travel-agent/scripts/.*\.py$",
    r"^travel-app/scripts/.*\.(mjs|sh)$",
    # API models/routes — the contract surface
    r"^travel-agent/backend/api/routes/.*\.py$",
    r"^travel-agent/backend/core/models/.*\.py$",
    # OpenAPI snapshots and generated-schema tooling
    r"^docs/openapi.*\.json$",
    r"^travel-app/utils/api/schema\.gen\.ts$",
]

FRONTEND_PATTERN = r"^travel-app/.*\.(ts|tsx)$"
BACKEND_PATTERN = r"^travel-agent/.*\.py$"
DOCS_PATTERN = r"^docs/.*\.md$"

_HIGH_RISK_RE = [re.compile(p) for p in HIGH_RISK_PATTERNS]
_FRONTEND_RE = re.compile(FRONTEND_PATTERN)
_BACKEND_RE = re.compile(BACKEND_PATTERN)
_DOCS_RE = re.compile(DOCS_PATTERN)


def classify_path(path: str) -> str:
    """Returns one of: high_risk, frontend, backend, docs, unknown."""
    for pattern in _HIGH_RISK_RE:
        if pattern.search(path):
            return "high_risk"
    if _FRONTEND_RE.match(path):
        return "frontend"
    if _BACKEND_RE.match(path):
        return "backend"
    if _DOCS_RE.match(path):
        return "docs"
    return "unknown"


# ── Doc example -> checker-test cross-reference ──────────────────────────
# A documentation-only change that references a check_*.py/.mjs script by
# name additionally runs that script's own test file, if one exists —
# "executable examples additionally run their referenced checker tests."

_SCRIPT_REF_RE = re.compile(r"\b(check[-_][\w-]+)\.(py|mjs)\b")


def referenced_checker_tests(doc_text: str, root: Path = WORKSPACE_ROOT) -> list[str]:
    """Given a changed doc's content, return the (deduped, sorted) checker
    test files it references that actually exist on disk under ``root``.
    ``root`` is injectable so tests aren't coupled to which checkers happen
    to be merged into this exact checkout at test time."""
    found: set[str] = set()
    for name, ext in _SCRIPT_REF_RE.findall(doc_text):
        for candidate in (
            f"scripts/{name}.test.{ext}",
            f"travel-agent/scripts/{name}.test.{ext}",
            f"travel-app/scripts/{name}.test.{ext}",
            f"scripts/tests/test_{name}.py",
            f"travel-agent/tests/scripts/test_{name}.py",
        ):
            if (root / candidate).exists():
                found.add(candidate)
    return sorted(found)


# ── Command selection ─────────────────────────────────────────────────────


@dataclass
class Selection:
    commands: list[tuple[str, str]] = field(default_factory=list)  # (command, reason)
    fallback_to_verify: bool = False
    fallback_reason: str | None = None

    def add(self, command: str, reason: str) -> None:
        if (command, reason) not in self.commands:
            self.commands.append((command, reason))


FULL_VERIFY_COMMAND = "make verify"


def select_commands(
    files: list[str], doc_texts: dict[str, str] | None = None, checker_test_root: Path = WORKSPACE_ROOT
) -> Selection:
    """Pure function: given the changed file list (and, for docs files,
    their content for the checker-reference scan), return the Selection.
    No filesystem/git access beyond what referenced_checker_tests already
    does for existence checks — everything else is string classification,
    which is what makes this exhaustively unit-testable."""
    doc_texts = doc_texts or {}

    if not files:
        sel = Selection()
        sel.fallback_to_verify = True
        sel.fallback_reason = "no changed files resolved against BASE_REF"
        sel.add(FULL_VERIFY_COMMAND, sel.fallback_reason)
        return sel

    classes = {f: classify_path(f) for f in files}

    high_risk = [f for f, c in classes.items() if c == "high_risk"]
    unknown = [f for f, c in classes.items() if c == "unknown"]

    sel = Selection()

    if high_risk or unknown:
        sel.fallback_to_verify = True
        culprits = sorted(high_risk + unknown)
        sel.fallback_reason = (
            f"{len(culprits)} unrecognized-or-high-risk file(s): {', '.join(culprits[:5])}"
            + (f" (+{len(culprits) - 5} more)" if len(culprits) > 5 else "")
        )
        sel.add(FULL_VERIFY_COMMAND, sel.fallback_reason)
        return sel

    frontend_files = sorted(f for f, c in classes.items() if c == "frontend")
    backend_files = sorted(f for f, c in classes.items() if c == "backend")
    docs_files = sorted(f for f, c in classes.items() if c == "docs")

    if frontend_files:
        sel.add("npm run verify:fast", f"{len(frontend_files)} frontend .ts/.tsx file(s) changed")
        rel = [f[len("travel-app/") :] for f in frontend_files]
        sel.add(
            f"npx jest --findRelatedTests {' '.join(rel)}",
            "run only the tests related to the changed frontend files",
        )

    if backend_files:
        # No tested dependency-to-test mapper exists yet (see A2 in the
        # working note) — until one does, ANY backend change conservatively
        # selects the full backend CI rather than guessing which subset of
        # 19k+ tests actually exercises it.
        sel.add(
            "make -C travel-agent ci",
            f"{len(backend_files)} backend .py file(s) changed — no dependency-to-test "
            "mapper exists yet, so the full backend CI runs rather than a guessed subset",
        )

    if docs_files:
        sel.add(
            "make docs-links-check docs-spine-check docs-canon-check",
            f"{len(docs_files)} doc-only file(s) changed",
        )
        for doc_file in docs_files:
            text = doc_texts.get(doc_file, "")
            for test_path in referenced_checker_tests(text, root=checker_test_root):
                sel.add(f"<run {test_path}>", f"{doc_file} references a checker this test covers")

    return sel


# ── Git plumbing ──────────────────────────────────────────────────────────


class BaseRefError(Exception):
    pass


def resolve_base_ref(base_ref: str | None) -> str:
    if not base_ref or not base_ref.strip():
        raise BaseRefError("BASE_REF is required and was not provided — refusing to guess 'main'")
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--verify", f"{base_ref}^{{commit}}"],
            cwd=WORKSPACE_ROOT,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError, OSError) as exc:
        raise BaseRefError(f"could not resolve BASE_REF={base_ref!r}: {exc}") from exc
    if out.returncode != 0:
        raise BaseRefError(f"BASE_REF={base_ref!r} does not resolve to a commit: {out.stderr.strip()}")
    return out.stdout.strip()


def changed_files(base_ref: str) -> list[str]:
    out = subprocess.run(
        ["git", "diff", "--name-only", f"{base_ref}...HEAD"],
        cwd=WORKSPACE_ROOT,
        capture_output=True,
        text=True,
        timeout=30,
        check=True,
    )
    tracked = [line.strip() for line in out.stdout.splitlines() if line.strip()]

    status = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=WORKSPACE_ROOT,
        capture_output=True,
        text=True,
        timeout=30,
        check=True,
    )
    uncommitted = [
        line[3:].strip() for line in status.stdout.splitlines() if line.strip() and line[3:].strip()
    ]

    return sorted(set(tracked) | set(uncommitted))


def read_doc_texts(files: list[str]) -> dict[str, str]:
    out: dict[str, str] = {}
    for f in files:
        if f.endswith(".md"):
            p = WORKSPACE_ROOT / f
            if p.exists():
                try:
                    out[f] = p.read_text(encoding="utf-8", errors="replace")
                except OSError:
                    out[f] = ""
    return out


# ── CLI ───────────────────────────────────────────────────────────────────


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--base-ref", dest="base_ref", default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    try:
        resolved = resolve_base_ref(args.base_ref)
    except BaseRefError as exc:
        print(f"verify-changed: {exc}", file=sys.stderr)
        return 2

    try:
        files = changed_files(resolved)
    except subprocess.CalledProcessError as exc:
        print(f"verify-changed: failed to diff against {resolved}: {exc}", file=sys.stderr)
        return 2

    doc_texts = read_doc_texts(files)
    selection = select_commands(files, doc_texts)

    print(f"verify-changed: BASE_REF={args.base_ref} -> {resolved}")
    print(f"verify-changed: {len(files)} changed file(s)")
    for f in files:
        print(f"  {classify_path(f):10} {f}")
    print()
    print("selected commands:")
    for command, reason in selection.commands:
        print(f"  [{reason}]")
        print(f"    $ {command}")

    if args.dry_run:
        return 0

    if selection.fallback_to_verify:
        print("\nverify-changed: falling back to the full gate.")

    exit_code = 0
    for command, _reason in selection.commands:
        if command.startswith("<run "):
            continue  # referenced-checker-test hint; not yet auto-executed
        print(f"\n$ {command}")
        result = subprocess.run(command, shell=True, cwd=WORKSPACE_ROOT)
        if result.returncode != 0:
            exit_code = result.returncode

    return exit_code


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
