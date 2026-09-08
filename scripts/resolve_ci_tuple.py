#!/usr/bin/env python3
"""Resolve immutable tested revisions; a dispatch substitutes its verified source SHA."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from pathlib import Path


def sha(value):
    if not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{40}", value):
        raise ValueError("Each candidate revision must be a full immutable commit SHA")
    return value


def resolve_tuple(lock, event, event_name, workspace_sha, owner="fy538"):
    candidate = {
        "workspace": sha(workspace_sha),
        **{name: sha(lock[name]) for name in ("travel-agent", "travel-app")},
    }
    trigger = None
    if event_name == "repository_dispatch":
        payload = event.get("client_payload", {})
        source = payload.get("source_repo")
        mapping = {f"{owner}/{name}": name for name in ("travel-agent", "travel-app")}
        if (
            source not in mapping
            or event.get("action") != f"{mapping[source]}-ci-success"
        ):
            raise ValueError("Dispatch source repository and event type must agree")
        name = mapping[source]
        candidate[name] = sha(payload.get("source_sha"))
        trigger = {
            "repository": source,
            "sha": candidate[name],
            "run_id": payload.get("source_run_id"),
        }
    return {"schema_version": 1, "candidate": candidate, "trigger": trigger}


def assert_checkouts(tuple_record, root):
    clean_env = {
        k: v
        for k, v in os.environ.items()
        if k not in {"GIT_DIR", "GIT_WORK_TREE", "GIT_COMMON_DIR", "GIT_INDEX_FILE"}
    }
    actual = {}
    for name, expected in tuple_record["candidate"].items():
        path = root if name == "workspace" else root / name
        actual[name] = subprocess.check_output(
            ["git", "-C", str(path), "rev-parse", "HEAD"], env=clean_env, text=True
        ).strip()
        if actual[name] != expected:
            raise ValueError(
                f"{name}: checkout {actual[name]} does not match tested candidate {expected}"
            )
    return actual


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    parser.add_argument("--assert-checkouts", action="store_true")
    args = parser.parse_args()
    record_path = args.root / "candidate-tuple.json"
    if args.assert_checkouts:
        record = json.loads(record_path.read_text())
        record["tested"] = assert_checkouts(record, args.root)
    else:
        lock = json.loads((args.root / "docs/child-repos.ci-lock.json").read_text())
        event = json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text())
        clean_env = {
            k: v
            for k, v in os.environ.items()
            if k not in {"GIT_DIR", "GIT_WORK_TREE", "GIT_COMMON_DIR", "GIT_INDEX_FILE"}
        }
        workspace_sha = subprocess.check_output(
            ["git", "-C", str(args.root), "rev-parse", "HEAD"], env=clean_env, text=True
        ).strip()
        record = resolve_tuple(
            lock, event, os.environ["GITHUB_EVENT_NAME"], workspace_sha
        )
        with open(os.environ["GITHUB_OUTPUT"], "a") as out:
            out.write(
                f"agent_ref={record['candidate']['travel-agent']}\napp_ref={record['candidate']['travel-app']}\n"
            )
    record_path.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
