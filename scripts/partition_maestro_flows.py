#!/usr/bin/env python3
"""Assign the complete Maestro flow inventory to deterministic CI shards."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def list_maestro_flows(app_dir: Path) -> list[str]:
    """Match the syntax wrapper's recursive YAML inventory, excluding configs."""
    maestro_dir = app_dir / ".maestro"
    if not maestro_dir.is_dir():
        raise ValueError(f"No .maestro directory under {app_dir}")

    return sorted(
        path.relative_to(app_dir).as_posix()
        for path in maestro_dir.rglob("*")
        if path.is_file()
        and not path.is_symlink()
        and path.suffix in {".yaml", ".yml"}
        and not (path.suffix == ".yaml" and path.name.startswith("config"))
    )


def partition_flows(flows: list[str], shard: int, shard_count: int) -> list[str]:
    if shard_count < 1:
        raise ValueError("shard count must be at least one")
    if shard < 0 or shard >= shard_count:
        raise ValueError(f"shard must be between 0 and {shard_count - 1}")

    selected = [path for index, path in enumerate(flows) if index % shard_count == shard]
    if not selected:
        raise ValueError(
            f"shard {shard} of {shard_count} is empty for {len(flows)} flows; "
            "reduce the shard count or restore the expected flow inventory"
        )
    return selected


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--app-dir", type=Path, default=Path("travel-app"))
    parser.add_argument("--shard", type=int, required=True, help="zero-based shard index")
    parser.add_argument("--shards", type=int, required=True, help="expected total shard count")
    parser.add_argument(
        "--nul-delimited",
        action="store_true",
        help="write paths separated by NUL for safe use with xargs -0",
    )
    args = parser.parse_args()

    try:
        flows = list_maestro_flows(args.app_dir)
        selected = partition_flows(flows, args.shard, args.shards)
    except (OSError, ValueError) as exc:
        print(f"::error::{exc}", file=sys.stderr)
        return 1

    print(
        f"Maestro syntax shard {args.shard + 1}/{args.shards}: "
        f"{len(selected)} of {len(flows)} flow files",
        file=sys.stderr,
    )
    separator = "\0" if args.nul_delimited else "\n"
    sys.stdout.write(separator.join(selected) + separator)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
