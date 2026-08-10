#!/usr/bin/env python3
"""Validate independent AI-DL human reviews without manufacturing H evidence."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


LABELS = {
    "correctness": {"correct", "incorrect", "insufficient_context"},
    "privacy": {"safe", "direct_leak", "inferential_leak", "uncertain"},
    "usefulness": {"useful", "neutral", "harmful"},
    "friction": {"proportionate", "avoidable_question", "premature_action"},
    "trust": {"earns", "neutral", "erodes"},
}
ACTIONS = {"ask_attribute", "show_options", "recommend", "abstain"}
REVIEW_KEYS = {"case_id", "acceptable_actions", *LABELS, "reason_codes"}
REASON_CODE = re.compile(r"^[a-z0-9][a-z0-9_.-]{0,79}$")


class ReviewError(ValueError):
    pass


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ReviewError(f"{path}: cannot read JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise ReviewError(f"{path}: root must be an object")
    return value


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_review(path: Path, case_ids: set[str]) -> tuple[str, dict[str, dict[str, Any]]]:
    packet = load_json(path)
    reviewer_id = packet.get("reviewer_id")
    if not isinstance(reviewer_id, str) or not reviewer_id.strip():
        raise ReviewError(f"{path}: reviewer_id is required")
    if not isinstance(packet.get("completed_at"), str) or not packet["completed_at"].strip():
        raise ReviewError(f"{path}: completed_at is required")
    reviews = packet.get("reviews")
    if not isinstance(reviews, list):
        raise ReviewError(f"{path}: reviews must be an array")
    by_id: dict[str, dict[str, Any]] = {}
    for row in reviews:
        if not isinstance(row, dict) or set(row) != REVIEW_KEYS:
            raise ReviewError(f"{path}: every review must contain only {sorted(REVIEW_KEYS)}")
        case_id = row.get("case_id")
        if not isinstance(case_id, str) or case_id in by_id:
            raise ReviewError(f"{path}: case IDs must be non-empty and unique")
        actions = row.get("acceptable_actions")
        if not isinstance(actions, list) or not actions or len(actions) != len(set(actions)):
            raise ReviewError(f"{path}: {case_id} needs a non-empty unique acceptable_actions list")
        if not set(actions) <= ACTIONS:
            raise ReviewError(f"{path}: {case_id} contains an unknown action")
        for label, allowed in LABELS.items():
            if row.get(label) not in allowed:
                raise ReviewError(f"{path}: {case_id} has invalid {label}")
        reason_codes = row.get("reason_codes")
        if not isinstance(reason_codes, list) or any(
            not isinstance(code, str) or not REASON_CODE.fullmatch(code) for code in reason_codes
        ):
            raise ReviewError(f"{path}: {case_id} reason_codes must be bounded codes, not prose")
        by_id[case_id] = row
    if set(by_id) != case_ids:
        missing = sorted(case_ids - set(by_id))
        extra = sorted(set(by_id) - case_ids)
        raise ReviewError(f"{path}: case mismatch; missing={missing}, extra={extra}")
    return reviewer_id, by_id


def resolution_value(row: dict[str, Any]) -> tuple[Any, ...]:
    return (
        tuple(sorted(row["acceptable_actions"])),
        *(row[label] for label in LABELS),
    )


def validate_adjudication(
    path: Path,
    disagreement_ids: set[str],
    review_hashes: set[str],
) -> str:
    packet = load_json(path)
    adjudicator_id = packet.get("adjudicator_id")
    if not isinstance(adjudicator_id, str) or not adjudicator_id.strip():
        raise ReviewError(f"{path}: adjudicator_id is required")
    if not isinstance(packet.get("completed_at"), str) or not packet["completed_at"].strip():
        raise ReviewError(f"{path}: completed_at is required")
    if set(packet.get("review_packet_sha256", [])) != review_hashes:
        raise ReviewError(f"{path}: review_packet_sha256 must bind the exact reviewer packets")
    resolutions = packet.get("resolutions")
    if not isinstance(resolutions, list):
        raise ReviewError(f"{path}: resolutions must be an array")
    resolved_ids: set[str] = set()
    for row in resolutions:
        if not isinstance(row, dict):
            raise ReviewError(f"{path}: each resolution must be an object")
        required = {"case_id", "acceptable_actions", *LABELS, "resolution_reason_code"}
        if set(row) != required:
            raise ReviewError(f"{path}: each resolution must contain only {sorted(required)}")
        case_id = row.get("case_id")
        if not isinstance(case_id, str) or case_id in resolved_ids:
            raise ReviewError(f"{path}: resolution case IDs must be unique")
        actions = row.get("acceptable_actions")
        if not isinstance(actions, list) or not actions or not set(actions) <= ACTIONS:
            raise ReviewError(f"{path}: {case_id} has invalid acceptable_actions")
        for label, allowed in LABELS.items():
            if row.get(label) not in allowed:
                raise ReviewError(f"{path}: {case_id} has invalid {label}")
        reason = row.get("resolution_reason_code")
        if not isinstance(reason, str) or not REASON_CODE.fullmatch(reason):
            raise ReviewError(f"{path}: {case_id} requires a bounded resolution_reason_code")
        resolved_ids.add(case_id)
    if resolved_ids != disagreement_ids:
        raise ReviewError(
            f"{path}: resolutions must exactly match disagreements; "
            f"missing={sorted(disagreement_ids - resolved_ids)}, "
            f"extra={sorted(resolved_ids - disagreement_ids)}"
        )
    return adjudicator_id


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--corpus", type=Path, required=True)
    parser.add_argument("--review", type=Path, action="append", required=True)
    parser.add_argument("--adjudication", type=Path)
    args = parser.parse_args()
    try:
        corpus = load_json(args.corpus)
        cases = corpus.get("cases")
        if not isinstance(cases, list):
            raise ReviewError("corpus cases must be an array")
        case_ids = {case.get("case_id") for case in cases if isinstance(case, dict)}
        if None in case_ids or len(case_ids) != len(cases):
            raise ReviewError("corpus case IDs must be non-empty and unique")
        if len(args.review) != 2:
            raise ReviewError("exactly two independent review packets are required")
        validated = [validate_review(path, case_ids) for path in args.review]
        reviewer_ids = [item[0] for item in validated]
        if len(set(reviewer_ids)) != 2:
            raise ReviewError("reviewer IDs must be distinct")
        left, right = validated[0][1], validated[1][1]
        disagreements = sorted(
            case_id
            for case_id in case_ids
            if resolution_value(left[case_id]) != resolution_value(right[case_id])
        )
        adjudicator_id = None
        if disagreements:
            if args.adjudication is None:
                result = {
                    "status": "adjudication_required",
                    "reviewer_ids": reviewer_ids,
                    "review_packet_sha256": [digest(path) for path in args.review],
                    "disagreement_case_ids": disagreements,
                    "h_evidence_ready": False,
                }
                print(json.dumps(result, indent=2, sort_keys=True))
                return 2
            adjudicator_id = validate_adjudication(
                args.adjudication,
                set(disagreements),
                {digest(path) for path in args.review},
            )
            if adjudicator_id in reviewer_ids:
                raise ReviewError("adjudicator must be independent of both reviewers")
        result = {
            "status": "adjudicated" if disagreements else "independent_agreement",
            "reviewer_ids": reviewer_ids,
            "adjudicator_id": adjudicator_id,
            "case_count": len(case_ids),
            "disagreement_case_ids": disagreements,
            "review_packet_sha256": [digest(path) for path in args.review],
            "adjudication_sha256": digest(args.adjudication) if args.adjudication else None,
            "h_evidence_ready": True,
        }
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0
    except ReviewError as exc:
        print(f"review validation failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
