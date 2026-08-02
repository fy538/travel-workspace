#!/usr/bin/env python3
"""Generate chat card-type registries and pilot attachment schemas from workspace contracts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TYPES_SOURCE = ROOT / "docs/contracts/chat-card-types.json"
SCHEMA_DIR = ROOT / "docs/contracts/chat-attachments"


def _ts_string_union(values: list[str]) -> str:
    return " | ".join(json.dumps(v) for v in values)


def render_ts_types(data: dict) -> str:
    meta = data["metadata_card_types"]
    attachments = data["attachments"]
    no_arrival = data["no_arrival"]
    meta_keys = list(meta.keys())
    rows = []
    for key, item in meta.items():
        attachment = "null" if item["attachment"] is None else json.dumps(item["attachment"])
        rows.append(
            f"  {json.dumps(key)}: {{ message_type: {json.dumps(item['message_type'])}, "
            f"attachment: {attachment}, thread: {json.dumps(item['thread'])} }},"
        )
    no_arrival_rows = "\n".join(
        f"  {json.dumps(k)}: {json.dumps(v)}," for k, v in no_arrival.items()
    )
    return (
        "// Generated from docs/contracts/chat-card-types.json. Do not hand-edit.\n"
        f"export type GeneratedMetadataCardType = {_ts_string_union(meta_keys)};\n"
        f"export type GeneratedChatAttachmentType = {_ts_string_union(attachments)};\n"
        "export const GENERATED_METADATA_CARD_TYPES = "
        f"{json.dumps(meta_keys, indent=2)} as const;\n"
        "export const GENERATED_CHAT_ATTACHMENT_TYPES = "
        f"{json.dumps(attachments, indent=2)} as const;\n"
        "export const GENERATED_METADATA_CARD_TYPE_INFO = {\n"
        + "\n".join(rows)
        + "\n} as const;\n"
        "export const GENERATED_CHAT_ATTACHMENT_NO_ARRIVAL = {\n"
        + no_arrival_rows
        + "\n} as const;\n"
    )


def render_py_types(data: dict) -> str:
    meta = data["metadata_card_types"]
    attachments = data["attachments"]
    no_arrival = data["no_arrival"]
    meta_keys = list(meta.keys())
    info_rows = []
    for key, item in meta.items():
        attachment = "None" if item["attachment"] is None else json.dumps(item["attachment"])
        info_rows.append(
            f'    {json.dumps(key)}: {{"message_type": {json.dumps(item["message_type"])}, '
            f'"attachment": {attachment}, "thread": {json.dumps(item["thread"])}}},'
        )
    no_arrival_rows = "\n".join(
        f"    {json.dumps(k)}: {json.dumps(v)}," for k, v in no_arrival.items()
    )
    return (
        '"""Generated from docs/contracts/chat-card-types.json. Do not hand-edit."""\n\n'
        "from __future__ import annotations\n\n"
        "KNOWN_METADATA_CARD_TYPES: frozenset[str] = frozenset(\n"
        f"    {meta_keys!r}\n"
        ")\n\n"
        "CHAT_ATTACHMENT_TYPES: tuple[str, ...] = tuple(\n"
        f"    {attachments!r}\n"
        ")\n\n"
        "METADATA_CARD_TYPE_INFO: dict[str, dict[str, str | None]] = {\n"
        + "\n".join(info_rows)
        + "\n}\n\n"
        "CHAT_ATTACHMENT_NO_ARRIVAL: dict[str, str] = {\n"
        + no_arrival_rows
        + "\n}\n\n"
        "def require_known_card_type(card_type: str | None) -> None:\n"
        '    """Raise ValueError when metadata.card_type is set but not allowlisted."""\n'
        "    if card_type is None:\n"
        "        return\n"
        "    if card_type not in KNOWN_METADATA_CARD_TYPES:\n"
        "        raise ValueError(f\"Unknown metadata.card_type: {card_type!r}\")\n"
    )


def _zod_line(name: str, spec: dict, *, required: bool) -> str:
    if "const" in spec:
        expr = f"z.literal({json.dumps(spec['const'])})"
    elif "enum" in spec:
        enums = ", ".join(json.dumps(v) for v in spec["enum"])
        expr = f"z.enum([{enums}])"
    else:
        typ = spec.get("type")
        if typ == "string":
            expr = "z.string()"
            if spec.get("minLength"):
                expr += f".min({spec['minLength']})"
        elif typ == "integer":
            expr = "z.number().int()"
            if "minimum" in spec:
                expr += f".min({spec['minimum']})"
        elif typ == "array":
            expr = "z.array(z.unknown())"
            if "minItems" in spec:
                expr += f".min({spec['minItems']})"
        elif isinstance(typ, list) and set(typ) == {"string", "null"}:
            expr = "z.string().nullable()"
        elif isinstance(typ, list) and set(typ) == {"integer", "null"}:
            expr = "z.number().int().nullable()"
        else:
            expr = "z.unknown()"
    if not required:
        expr += ".optional()"
    return f"  {name}: {expr},"


def _py_field(name: str, spec: dict, *, required: bool) -> str:
    if "const" in spec:
        ann = f"Literal[{json.dumps(spec['const'])}]"
    elif "enum" in spec:
        enums = ", ".join(json.dumps(v) for v in spec["enum"])
        ann = f"Literal[{enums}]"
    else:
        typ = spec.get("type")
        if typ == "string":
            ann = "str"
        elif typ == "integer":
            ann = "int"
        elif typ == "array":
            ann = "list[Any]"
        elif isinstance(typ, list) and set(typ) == {"string", "null"}:
            ann = "str | None"
        elif isinstance(typ, list) and set(typ) == {"integer", "null"}:
            ann = "int | None"
        else:
            ann = "Any"
    if required:
        return f"    {name}: {ann}"
    if ann.endswith("| None"):
        return f"    {name}: {ann} = None"
    return f"    {name}: {ann} | None = None"


def render_schemas(pilot_names: list[str]) -> tuple[str, str]:
    ts_parts = [
        "// Generated from docs/contracts/chat-attachments/*.schema.json. Do not hand-edit.\n",
        "import { z } from 'zod';\n\n",
    ]
    py_parts = [
        '"""Generated from docs/contracts/chat-attachments/*.schema.json. Do not hand-edit."""\n\n',
        "from __future__ import annotations\n\n",
        "from typing import Any, Literal\n\n",
        "from pydantic import BaseModel, ConfigDict\n\n",
    ]
    model_map: list[tuple[str, str]] = []
    for name in pilot_names:
        schema = json.loads((SCHEMA_DIR / f"{name}.schema.json").read_text())
        title = schema.get("title") or name
        props = schema.get("properties") or {}
        required = set(schema.get("required") or [])
        additional = schema.get("additionalProperties", True)
        ts_props = [
            _zod_line(prop_name, prop_spec, required=prop_name in required)
            for prop_name, prop_spec in props.items()
        ]
        mode = "strict" if additional is False else "passthrough"
        ts_parts.append(
            f"export const {title}Schema = z.object({{\n"
            + "\n".join(ts_props)
            + f"\n}}).{mode}();\n"
            f"export type {title} = z.infer<typeof {title}Schema>;\n\n"
        )
        py_fields = [
            _py_field(prop_name, prop_spec, required=prop_name in required)
            for prop_name, prop_spec in props.items()
        ]
        extra = "forbid" if additional is False else "allow"
        py_parts.append(
            f"class {title}(BaseModel):\n"
            f"    model_config = ConfigDict(extra={extra!r})\n"
            + "\n".join(py_fields)
            + "\n\n"
        )
        model_map.append((name, title))

    py_parts.append("PILOT_ATTACHMENT_SCHEMA_MODELS = {\n")
    for name, title in model_map:
        py_parts.append(f"    {json.dumps(name)}: {title},\n")
    py_parts.append("}\n\n")
    py_parts.append(
        "def validate_pilot_attachment_payload(schema_name: str, payload: dict[str, Any]) -> None:\n"
        "    model = PILOT_ATTACHMENT_SCHEMA_MODELS.get(schema_name)\n"
        "    if model is None:\n"
        "        raise KeyError(f\"No pilot schema named {schema_name!r}\")\n"
        "    model.model_validate(payload)\n"
    )
    return "".join(ts_parts), "".join(py_parts)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument(
        "--travel-agent-root",
        type=Path,
        default=ROOT / "travel-agent",
        help="Travel Agent checkout to receive generated Python contracts.",
    )
    parser.add_argument(
        "--travel-app-root",
        type=Path,
        default=ROOT / "travel-app",
        help="Travel App checkout to receive generated TypeScript contracts.",
    )
    args = parser.parse_args()
    data = json.loads(TYPES_SOURCE.read_text())
    # Worktree-aware output roots keep contract generation from modifying a
    # concurrently edited primary checkout. The workspace contract itself
    # remains the single source of truth.
    ts_types = args.travel_app_root / "utils/chat/chatCardTypes.generated.ts"
    py_types = args.travel_agent_root / "backend/core/chat_card_types_generated.py"
    ts_schemas = args.travel_app_root / "utils/chat/attachmentSchemas.generated.ts"
    py_schemas = args.travel_agent_root / "backend/concierge/chat_attachment_schemas_generated.py"
    expected = {
        ts_types: render_ts_types(data),
        py_types: render_py_types(data),
        **dict(
            zip(
                (ts_schemas, py_schemas),
                render_schemas(list(data.get("pilot_attachment_schemas") or [])),
                strict=True,
            )
        ),
    }
    stale = [
        path
        for path, content in expected.items()
        if not path.exists() or path.read_text() != content
    ]
    if args.check:
        if stale:
            print(
                "Stale chat-card-types generated files: "
                + ", ".join(str(p.relative_to(ROOT)) for p in stale)
            )
            return 1
        return 0
    for path, content in expected.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        try:
            label = path.relative_to(ROOT)
        except ValueError:
            label = path
        print(f"Wrote {label}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
