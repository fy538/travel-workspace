from __future__ import annotations

import sys
from pathlib import Path

import pytest


sys.path.insert(0, str(Path(__file__).parent))

from api_contract_audit import Consumer, OperationKey  # noqa: E402
from project_app_openapi import (  # noqa: E402
    ProjectionError,
    build_app_projection,
    discover_mobile_schema_consumers,
    render_projection,
    select_app_operations,
)


def _operation(operation_id: str, schema: str) -> dict:
    return {
        "operationId": operation_id,
        "responses": {
            "200": {
                "description": "ok",
                "content": {
                    "application/json": {
                        "schema": {"$ref": f"#/components/schemas/{schema}"}
                    }
                },
            }
        },
    }


def test_selection_uses_lifecycle_audience_and_explicit_mobile_consumers() -> None:
    spec = {
        "paths": {
            "/api/trips": {"get": _operation("listTrips", "Trip")},
            "/admin/mobile": {"get": _operation("mobileStatus", "Status")},
            "/admin/only": {"get": _operation("adminOnly", "Status")},
            "/api/legacy": {"get": _operation("legacy", "Legacy")},
        }
    }
    policy = {
        "defaults": {"audience": "app", "lifecycle": "active"},
        "operations": {
            "GET /admin/mobile": {
                "audience": "operator",
                "consumers": [
                    {"kind": "app_url", "name": "diagnostics", "source": "x.ts"}
                ],
            },
            "GET /admin/only": {
                "audience": "operator",
                "consumers": [{"kind": "operator", "name": "console"}],
            },
            "GET /api/legacy": {"lifecycle": "retiring", "consumers": []},
        },
    }
    selected = select_app_operations(
        spec,
        policy,
        {("GET", "/admin/mobile"): {Consumer("app_direct", "travel-app/status.ts")}},
    )
    assert selected == {
        OperationKey("GET", "/api/trips"),
        OperationKey("GET", "/admin/mobile"),
    }


def test_projection_prunes_paths_and_follows_component_refs_recursively() -> None:
    spec = {
        "openapi": "3.1.0",
        "info": {"title": "Test", "version": "1"},
        "paths": {
            "/api/trips": {
                "summary": "Trips",
                "get": _operation("listTrips", "TripPage"),
                "post": _operation("createTrip", "Unused"),
            },
            "/admin": {"get": _operation("admin", "Unused")},
        },
        "components": {
            "schemas": {
                "Trip": {"type": "object"},
                "TripPage": {
                    "type": "array",
                    "items": {"$ref": "#/components/schemas/Trip"},
                },
                "Unused": {"type": "string"},
            }
        },
    }
    projection = build_app_projection(spec, {OperationKey("GET", "/api/trips")})
    assert set(projection["paths"]) == {"/api/trips"}
    assert set(projection["paths"]["/api/trips"]) == {"summary", "get"}
    assert set(projection["components"]["schemas"]) == {"Trip", "TripPage"}
    assert render_projection(projection).endswith("\n")


def test_projection_retains_schemas_named_directly_by_mobile(tmp_path: Path) -> None:
    source = tmp_path / "types.ts"
    source.write_text(
        "// components['schemas']['ExampleOnly']\n"
        "const docs = 'https://example.test'; "
        "type Direct = components['schemas']['DirectModel'];\n",
        encoding="utf-8",
    )
    spec = {
        "paths": {"/api/trips": {"get": _operation("listTrips", "Trip")}},
        "components": {
            "schemas": {
                "Trip": {"type": "object"},
                "DirectModel": {
                    "properties": {
                        "child": {"$ref": "#/components/schemas/DirectChild"}
                    }
                },
                "DirectChild": {"type": "string"},
                "Unused": {"type": "string"},
            }
        },
    }
    direct = discover_mobile_schema_consumers(tmp_path)
    assert direct == {"DirectModel"}
    projection = build_app_projection(spec, {OperationKey("GET", "/api/trips")}, direct)
    assert set(projection["components"]["schemas"]) == {
        "Trip",
        "DirectModel",
        "DirectChild",
    }


def test_projection_rejects_a_dangling_component_ref() -> None:
    spec = {
        "paths": {"/api/trips": {"get": _operation("listTrips", "Missing")}},
        "components": {"schemas": {}},
    }
    with pytest.raises(ProjectionError, match="missing component"):
        build_app_projection(spec, {OperationKey("GET", "/api/trips")})
