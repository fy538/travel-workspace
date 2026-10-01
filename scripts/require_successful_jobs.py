#!/usr/bin/env python3
"""Fail unless every named GitHub Actions dependency completed successfully."""

from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Any


def failed_jobs(needs: Any, required: list[str]) -> list[str]:
    if not isinstance(needs, dict):
        return ["needs context is not an object"]
    failures = []
    for name in required:
        job = needs.get(name)
        result = job.get("result") if isinstance(job, dict) else None
        if result != "success":
            failures.append(f"{name}={result or 'missing'}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("jobs", nargs="+", help="required job IDs from the needs context")
    args = parser.parse_args()

    try:
        needs = json.loads(os.environ["NEEDS_JSON"])
    except (KeyError, json.JSONDecodeError) as exc:
        print(f"::error::Missing or invalid NEEDS_JSON: {exc}", file=sys.stderr)
        return 2

    failures = failed_jobs(needs, args.jobs)
    if failures:
        print(f"::error::Required reliability jobs did not pass: {', '.join(failures)}", file=sys.stderr)
        return 1
    print(f"All required reliability jobs passed: {', '.join(args.jobs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
