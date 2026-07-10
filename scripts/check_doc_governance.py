#!/usr/bin/env python3
"""Validate governance metadata on newly added workspace Markdown files.

Phase 1 intentionally grandfathers every pre-existing document. The default
mode inspects Markdown files staged as additions. CI passes ``--new-since`` to
inspect additions relative to the push or pull-request base. Explicit paths are
also accepted for tests and manual validation.

Templates under ``docs/templates/`` contain placeholders and are excluded.
Markdown outside ``docs/`` is not part of the workspace documentation system.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
TEMPLATE_ROOT = DOCS / "templates"

ALLOWED_TYPES = {
    "canon",
    "contract",
    "runbook",
    "decision",
    "current_status",
    "working",
    "archive",
}
REQUIRES_LAST_VERIFIED = {"canon", "contract", "runbook", "current_status"}
ALLOWED_STATUSES = {
    "canon": {"active", "superseded"},
    "contract": {"active", "deprecated", "superseded"},
    "runbook": {"active", "deprecated"},
    "decision": {"accepted", "superseded"},
    "current_status": {"active"},
    "working": {"active", "blocked"},
    "archive": {"archived"},
}
REQUIRED_COMMON = {"doc_type", "status", "owner", "created", "why_new"}


@dataclass(frozen=True)
class Finding:
    path: Path
    message: str


def _git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(f"git {' '.join(args)} failed: {detail}")
    return result.stdout


def _is_governed_path(path: Path) -> bool:
    try:
        resolved = path.resolve()
        resolved.relative_to(DOCS.resolve())
    except (OSError, ValueError):
        return False
    try:
        resolved.relative_to(TEMPLATE_ROOT.resolve())
        return False
    except ValueError:
        pass
    return resolved.suffix.lower() == ".md"


def _normalize_paths(raw_paths: list[str]) -> list[Path]:
    paths: list[Path] = []
    for raw in raw_paths:
        path = Path(raw)
        if not path.is_absolute():
            path = ROOT / path
        if path.exists() and _is_governed_path(path):
            paths.append(path.resolve())
    return sorted(set(paths))


def staged_additions() -> list[Path]:
    names = _git("diff", "--cached", "--diff-filter=A", "--name-only", "--", "docs/*.md", "docs/**/*.md")
    return _normalize_paths(names.splitlines())


def local_additions() -> list[Path]:
    staged = staged_additions()
    untracked = _git(
        "ls-files",
        "--others",
        "--exclude-standard",
        "--",
        "docs/*.md",
        "docs/**/*.md",
    )
    return sorted(set(staged + _normalize_paths(untracked.splitlines())))


def additions_since(base: str) -> list[Path]:
    names = _git("diff", "--diff-filter=A", "--name-only", f"{base}...HEAD", "--", "docs/*.md", "docs/**/*.md")
    return _normalize_paths(names.splitlines())


def _frontmatter(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return None, str(exc)
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, "missing YAML frontmatter (file must start with ---)"
    try:
        closing = next(i for i, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration:
        return None, "YAML frontmatter has no closing ---"
    try:
        parsed = yaml.safe_load("\n".join(lines[1:closing]))
    except yaml.YAMLError as exc:
        return None, f"invalid YAML frontmatter: {exc}"
    if not isinstance(parsed, dict):
        return None, "YAML frontmatter must be a mapping"
    return parsed, None


def _as_date(value: Any, field: str) -> tuple[date | None, str | None]:
    if isinstance(value, date):
        return value, None
    if isinstance(value, str):
        try:
            return date.fromisoformat(value)
        except ValueError:
            pass
    return None, f"{field} must be an ISO date (YYYY-MM-DD)"


def validate(path: Path) -> list[Finding]:
    meta, parse_error = _frontmatter(path)
    if parse_error:
        return [Finding(path, parse_error)]
    assert meta is not None
    findings: list[Finding] = []

    missing = sorted(field for field in REQUIRED_COMMON if meta.get(field) in (None, "", []))
    if missing:
        findings.append(Finding(path, "missing required field(s): " + ", ".join(missing)))

    doc_type = meta.get("doc_type")
    if doc_type not in ALLOWED_TYPES:
        findings.append(
            Finding(path, f"doc_type must be one of: {', '.join(sorted(ALLOWED_TYPES))}")
        )
        return findings

    status = meta.get("status")
    if status not in ALLOWED_STATUSES[doc_type]:
        allowed = ", ".join(sorted(ALLOWED_STATUSES[doc_type]))
        findings.append(Finding(path, f"status for {doc_type} must be one of: {allowed}"))

    why_new = meta.get("why_new")
    if isinstance(why_new, str) and len(why_new.strip()) < 20:
        findings.append(Finding(path, "why_new must be a concrete explanation (at least 20 characters)"))

    created, created_error = _as_date(meta.get("created"), "created")
    if created_error:
        findings.append(Finding(path, created_error))

    if doc_type in REQUIRES_LAST_VERIFIED:
        _, error = _as_date(meta.get("last_verified"), "last_verified")
        if error:
            findings.append(Finding(path, error))

    if doc_type == "working":
        expires, error = _as_date(meta.get("expires"), "expires")
        if error:
            findings.append(Finding(path, error))
        elif created and expires and expires > created + timedelta(days=30):
            findings.append(Finding(path, "working document expires must be within 30 days of created"))
        elif created and expires and expires < created:
            findings.append(Finding(path, "working document expires cannot precede created"))

    if doc_type == "decision":
        _, error = _as_date(meta.get("decided"), "decided")
        if error:
            findings.append(Finding(path, error))

    if doc_type == "archive":
        _, error = _as_date(meta.get("archived"), "archived")
        if error:
            findings.append(Finding(path, error))

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--new-since", metavar="GIT_REF")
    mode.add_argument("--staged-new", action="store_true")
    mode.add_argument("--local-new", action="store_true")
    parser.add_argument("paths", nargs="*")
    args = parser.parse_args()

    try:
        if args.paths:
            paths = _normalize_paths(args.paths)
        elif args.new_since:
            paths = additions_since(args.new_since)
        elif args.local_new:
            paths = local_additions()
        else:
            paths = staged_additions()
    except RuntimeError as exc:
        print(f"doc-governance: {exc}", file=sys.stderr)
        return 2

    findings = [finding for path in paths for finding in validate(path)]
    for finding in findings:
        relative = finding.path.relative_to(ROOT)
        print(f"{relative}: {finding.message}", file=sys.stderr)

    if findings:
        print(
            f"doc-governance FAILED: {len(findings)} issue(s) across {len(paths)} new document(s)",
            file=sys.stderr,
        )
        return 1

    print(f"doc-governance OK: {len(paths)} new workspace document(s) checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
