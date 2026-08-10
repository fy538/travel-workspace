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
import json
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import journey_evidence as evidence


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT = ROOT / "docs" / "journeys" / "evidence-attestations.json"
INDEX_SCHEMA_VERSION = 1


def _canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def receipt_digest(receipt: dict[str, Any]) -> str:
    payload = {key: value for key, value in receipt.items() if key != "_path"}
    return "sha256:" + hashlib.sha256(_canonical_json(payload).encode()).hexdigest()


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
