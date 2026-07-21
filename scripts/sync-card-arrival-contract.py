#!/usr/bin/env python3
"""Generate both runtime card-arrival registries from one workspace contract."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/contracts/card-arrival.json"
TS_TARGET = ROOT / "travel-app/utils/chat/cardArrivalContract.generated.ts"
PY_TARGET = ROOT / "travel-agent/backend/concierge/card_arrival_contract_generated.py"


def render_ts(data: dict[str, dict[str, object]]) -> str:
    rows = "\n".join(
        f"  {tool}: {{ type: {item['type']!r}, label: {item['label']!r}, "
        f"id_keys: {item['id_keys']!r} }},"
        for tool, item in data.items()
    )
    return "// Generated from docs/contracts/card-arrival.json. Do not hand-edit.\n" + (
        f"export const GENERATED_CARD_ARRIVAL_TOOLS = {{\n{rows}\n}} as const;\n"
    )


def render_py(data: dict[str, dict[str, object]]) -> str:
    rows = "\n".join(f'    "{tool}": "{item["type"]}",' for tool, item in data.items())

    def _tuple_literal(values: object) -> str:
        assert isinstance(values, list) and values
        rendered = ", ".join(json.dumps(str(value)) for value in values)
        return f"({rendered}{',' if len(values) == 1 else ''})"

    id_rows = "\n".join(
        f'    "{tool}": {_tuple_literal(item["id_keys"])},'
        for tool, item in data.items()
    )
    return (
        '"""Generated from docs/contracts/card-arrival.json. Do not hand-edit."""\n\n'
        "CARD_TYPE_BY_TOOL: dict[str, str] = {\n"
        f"{rows}\n}}\n\n"
        "CARD_ID_KEYS_BY_TOOL: dict[str, tuple[str, ...]] = {\n"
        f"{id_rows}\n}}\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = json.loads(SOURCE.read_text())
    expected = {TS_TARGET: render_ts(data), PY_TARGET: render_py(data)}
    stale = [
        path
        for path, content in expected.items()
        if not path.exists() or path.read_text() != content
    ]
    if args.check:
        if stale:
            print(
                "Stale card-arrival generated files: "
                + ", ".join(str(p.relative_to(ROOT)) for p in stale)
            )
            return 1
        return 0
    for path, content in expected.items():
        path.write_text(content)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
