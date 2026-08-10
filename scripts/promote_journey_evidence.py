#!/usr/bin/env python3
"""Promote validated execution receipts into a durable attestation index.

Raw receipts are intentionally short-lived CI/local artifacts. Promotion is an
explicit operation on a clean candidate: it embeds the receipt payload, records
its content hash, and writes the candidate triple-SHA identity used by generated
status and release projections.
"""

from __future__ import annotations

import argparse
import hashlib
import hmac
import json
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import journey_evidence as evidence


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT = ROOT / "docs" / "journeys" / "evidence-attestations.json"
INDEX_SCHEMA_VERSION = 1
ATTESTATION_PROJECTION_PATHS = frozenset(
    {
        "docs/journeys/evidence-attestations.json",
        "docs/journeys/STATUS.md",
        "docs/release/v1-scope.md",
        "docs/status/current-state.md",
    }
)


def _canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def receipt_digest(receipt: dict[str, Any]) -> str:
    payload = {key: value for key, value in receipt.items() if key != "_path"}
    return "sha256:" + hashlib.sha256(_canonical_json(payload).encode()).hexdigest()


def _git_lines(root: Path, *args: str) -> list[str]:
    output = subprocess.check_output(
        ["git", *args],
        cwd=root,
        text=True,
        stderr=subprocess.DEVNULL,
    )
    return [line for line in output.splitlines() if line]


def index_candidate_is_current(
    index: dict[str, Any],
    current: dict[str, str],
    *,
    workspace_root: Path = ROOT,
) -> bool:
    """Return whether a committed index still describes this checkout.

    The attestation file cannot contain the SHA of the commit that contains
    itself.  A promoted candidate is therefore current when app/backend still
    match exactly and the workspace HEAD is either the tested subject itself or
    a descendant whose complete diff is restricted to governed attestation and
    generated-status paths. This permits the index and its projections to land
    in separate commits without allowing product or runner changes to inherit
    an older certification.
    """

    candidate = index.get("candidate") or {}
    if not candidate or set(candidate) != {"workspace_sha", "app_sha", "backend_sha"}:
        return False
    if any(
        current.get(key) == "unknown" or str(current.get(key, "")).endswith("-dirty")
        for key in ("workspace_sha", "app_sha", "backend_sha")
    ):
        return False
    if any(candidate.get(key) != current.get(key) for key in ("app_sha", "backend_sha")):
        return False

    subject_sha = candidate.get("workspace_sha")
    current_sha = current.get("workspace_sha")
    if subject_sha == current_sha:
        return True
    if not isinstance(subject_sha, str) or not isinstance(current_sha, str):
        return False
    try:
        _git_lines(workspace_root, "merge-base", "--is-ancestor", subject_sha, current_sha)
        changed_paths = set(
            _git_lines(workspace_root, "diff", "--name-only", subject_sha, current_sha, "--")
        )
    except (OSError, subprocess.CalledProcessError):
        return False
    return bool(changed_paths) and changed_paths <= ATTESTATION_PROJECTION_PATHS


def build_index(receipts: list[dict[str, Any]], revisions: dict[str, str]) -> dict[str, Any]:
    if any(value == "unknown" or value.endswith("-dirty") for value in revisions.values()):
        raise ValueError("promotion requires a clean workspace, app, and backend candidate")

    attestations: list[dict[str, Any]] = []
    seen: set[str] = set()
    for receipt in receipts:
        if receipt.get("status") != "pass":
            continue
        if not evidence.receipt_is_current(receipt, revisions):
            continue
        digest = receipt_digest(receipt)
        if digest in seen:
            continue
        seen.add(digest)
        payload = {key: value for key, value in receipt.items() if key != "_path"}
        attestations.append({"receipt_sha256": digest, "receipt": payload})

    return {
        "schema_version": INDEX_SCHEMA_VERSION,
        "generated_at": datetime.now(UTC).isoformat(),
        "candidate": revisions,
        "attestations": attestations,
    }


def load_index(path: Path = DEFAULT_OUTPUT) -> dict[str, Any]:
    if not path.exists():
        return {
            "schema_version": INDEX_SCHEMA_VERSION,
            "candidate": {},
            "attestations": [],
        }
    data = json.loads(path.read_text())
    if data.get("schema_version") != INDEX_SCHEMA_VERSION:
        raise ValueError(f"unsupported attestation index schema: {data.get('schema_version')!r}")
    if not isinstance(data.get("attestations"), list):
        raise ValueError("attestation index requires an attestations list")
    candidate = data.get("candidate") or {}
    if candidate and set(candidate) != {"workspace_sha", "app_sha", "backend_sha"}:
        raise ValueError("attestation index candidate must contain the triple-SHA identity")
    for position, attestation in enumerate(data["attestations"]):
        if not isinstance(attestation, dict):
            raise ValueError(f"attestation {position} must be an object")
        receipt = attestation.get("receipt")
        digest = attestation.get("receipt_sha256")
        if not isinstance(receipt, dict) or not isinstance(digest, str):
            raise ValueError(f"attestation {position} requires a receipt and receipt_sha256")
        try:
            evidence.validate_receipt(receipt)
        except evidence.ReceiptError as exc:
            raise ValueError(f"attestation {position} has an invalid receipt: {exc}") from exc
        if receipt.get("status") != "pass":
            raise ValueError(f"attestation {position} must embed a passing receipt")
        if candidate and not evidence.receipt_is_current(receipt, candidate):
            raise ValueError(f"attestation {position} receipt does not match the candidate")
        if not hmac.compare_digest(digest, receipt_digest(receipt)):
            raise ValueError(f"attestation {position} receipt digest mismatch")
    return data


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", type=Path, default=evidence.DEFAULT_DIRECTORY)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args(argv)

    try:
        receipts = evidence.load_receipts(args.directory.resolve())
        index = build_index(receipts, evidence.current_revisions())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"attestation promotion rejected: {exc}", file=sys.stderr)
        return 2

    if not args.write:
        print(json.dumps(index, indent=2, sort_keys=True))
        return 0

    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(index, indent=2, sort_keys=True) + "\n")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
