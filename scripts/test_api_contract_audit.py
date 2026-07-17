from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from api_contract_audit import (  # noqa: E402
    OPENAPI_SNAPSHOT,
    Consumer,
    _iter_call_bodies,
    _method_for_call,
    audit,
    load_openapi,
    normalize_path,
)


class APIContractAuditTests(unittest.TestCase):
    def _files(
        self,
        operations: list[tuple[str, str, str]],
        overrides: dict[str, dict] | None = None,
    ) -> tuple[Path, Path]:
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        root = Path(directory.name)
        paths: dict[str, dict] = {}
        for method, path, operation_id in operations:
            paths.setdefault(path, {})[method.lower()] = {
                "operationId": operation_id,
                "responses": {"200": {"description": "ok"}},
            }
        openapi = root / "openapi.json"
        openapi.write_text(json.dumps({"paths": paths}), encoding="utf-8")
        policy = root / "policy.json"
        policy.write_text(
            json.dumps(
                {
                    "version": 1,
                    "defaults": {
                        "audience": "app",
                        "lifecycle": "active",
                        "owner": "product-engineering",
                        "feature_flag": None,
                        "removal_trigger": None,
                        "review_by": None,
                    },
                    "operations": overrides or {},
                    "retired_operations": {},
                }
            ),
            encoding="utf-8",
        )
        return openapi, policy

    @staticmethod
    def _policy(lifecycle: str = "dark") -> dict:
        return {
            "audience": "app",
            "lifecycle": lifecycle,
            "owner": "test-owner",
            "reason": "Explicit test classification.",
            "feature_flag": "TEST_DARK_FLAG" if lifecycle == "dark" else None,
            "removal_trigger": "Adopt or delete." if lifecycle != "active" else None,
            "review_by": "2026-08-15" if lifecycle != "active" else None,
            "consumers": [],
        }

    def test_parser_handles_optional_nested_generic_and_method(self) -> None:
        source = """
          async saveThing(id: string) {
            return _request<Array<{ id: string }>>(`/api/things/${id}`, {
              method: 'POST', body: '{}',
            });
          }
          async readThing(id: string) {
            return _request(`/api/things/${id}`);
          }
        """
        calls = list(_iter_call_bodies(source, {"_request"}))
        self.assertEqual(len(calls), 2)
        self.assertEqual(_method_for_call(calls[0][0], calls[0][2]), "POST")
        self.assertEqual(_method_for_call(calls[1][0], calls[1][2]), "GET")
        self.assertEqual(normalize_path(calls[0][1]), "/api/things/{*}")

    def test_get_consumer_does_not_cover_post_on_same_path(self) -> None:
        openapi, policy = self._files(
            [
                ("GET", "/api/things/{thing_id}", "get_thing"),
                ("POST", "/api/things/{thing_id}", "post_thing"),
            ]
        )
        consumers = {
            ("GET", "/api/things/{*}"): {
                Consumer("app_source", "travel-app/data/things.ts", "getThing")
            }
        }
        findings, _, _ = audit(openapi, policy, consumers, {"TEST_DARK_FLAG"})
        self.assertIn(
            "POST /api/things/{thing_id} has no detected or declared consumer",
            [f.message for f in findings],
        )

    def test_dark_operation_with_product_caller_fails(self) -> None:
        key = "GET /api/things/{thing_id}"
        openapi, policy = self._files(
            [("GET", "/api/things/{thing_id}", "get_thing")],
            {key: self._policy("dark")},
        )
        consumers = {
            ("GET", "/api/things/{*}"): {
                Consumer("app_source", "travel-app/data/things.ts", "getThing")
            }
        }
        findings, _, _ = audit(openapi, policy, consumers, {"TEST_DARK_FLAG"})
        self.assertIn("dark-has-caller", {finding.code for finding in findings})

    def test_dark_operation_requires_registered_flag(self) -> None:
        key = "GET /api/things/{thing_id}"
        openapi, policy = self._files(
            [("GET", "/api/things/{thing_id}", "get_thing")],
            {key: self._policy("dark")},
        )
        findings, _, _ = audit(openapi, policy, {}, set())
        self.assertIn(
            "is not registered",
            "\n".join(finding.message for finding in findings),
        )

    def test_stale_policy_entry_fails(self) -> None:
        openapi, policy = self._files(
            [("GET", "/api/things", "list_things")],
            {"DELETE /api/things/{thing_id}": self._policy("retiring")},
        )
        consumers = {
            ("GET", "/api/things"): {
                Consumer("app_source", "travel-app/data/things.ts", "listThings")
            }
        }
        findings, _, _ = audit(openapi, policy, consumers, {"TEST_DARK_FLAG"})
        self.assertIn("stale-policy", {finding.code for finding in findings})

    def test_retired_operation_cannot_reappear_in_openapi(self) -> None:
        key = "POST /api/things/{thing_id}/apply"
        openapi, policy = self._files(
            [("POST", "/api/things/{thing_id}/apply", "apply_thing")]
        )
        payload = json.loads(policy.read_text())
        payload["retired_operations"][key] = {
            "owner": "test-owner",
            "reason": "Superseded split mutation route.",
            "replacement": "POST /api/things/{thing_id}/resolve",
            "retired_on": "2026-07-16",
        }
        policy.write_text(json.dumps(payload))

        findings, _, _ = audit(openapi, policy, {}, set())

        self.assertIn("retired-operation-exposed", {finding.code for finding in findings})

    def test_retired_operation_stays_as_absence_ratchet(self) -> None:
        key = "POST /api/things/{thing_id}/apply"
        openapi, policy = self._files(
            [("POST", "/api/things/{thing_id}/resolve", "resolve_thing")],
            {
                "POST /api/things/{thing_id}/resolve": {
                    **self._policy("active"),
                    "consumers": [{"kind": "server", "name": "test"}],
                }
            },
        )
        payload = json.loads(policy.read_text())
        payload["retired_operations"][key] = {
            "owner": "test-owner",
            "reason": "Superseded split mutation route.",
            "replacement": "POST /api/things/{thing_id}/resolve",
            "retired_on": "2026-07-16",
        }
        policy.write_text(json.dumps(payload))

        findings, _, _ = audit(openapi, policy, {}, set())

        self.assertEqual(findings, [])

    def test_retirement_requires_live_replacement(self) -> None:
        key = "POST /api/things/{thing_id}/apply"
        openapi, policy = self._files([])
        payload = json.loads(policy.read_text())
        payload["retired_operations"][key] = {
            "owner": "test-owner",
            "reason": "Superseded split mutation route.",
            "replacement": "POST /api/things/{thing_id}/resolve",
            "retired_on": "2026-07-16",
        }
        policy.write_text(json.dumps(payload))

        findings, _, _ = audit(openapi, policy, {}, set())

        self.assertIn(
            "retirement-replacement-missing", {finding.code for finding in findings}
        )

    def test_expired_dark_policy_fails(self) -> None:
        key = "GET /api/things/{thing_id}"
        expired = self._policy("dark")
        expired["review_by"] = "2020-01-01"
        openapi, policy = self._files(
            [("GET", "/api/things/{thing_id}", "get_thing")],
            {key: expired},
        )
        findings, _, _ = audit(openapi, policy, {}, {"TEST_DARK_FLAG"})
        self.assertIn("expired-policy", {finding.code for finding in findings})

    def test_transport_implementation_without_product_caller_requires_policy(
        self,
    ) -> None:
        openapi, policy = self._files([("GET", "/api/things", "list_things")])
        consumers = {
            ("GET", "/api/things"): {
                Consumer("app_transport", "travel-app/utils/api/http.ts", "listThings")
            }
        }
        findings, _, transport_only = audit(
            openapi, policy, consumers, {"TEST_DARK_FLAG"}
        )
        self.assertIn("transport-only", {finding.code for finding in findings})
        self.assertEqual(transport_only, ["GET /api/things"])

    def test_current_workspace_policy_is_green(self) -> None:
        findings, counts, _ = audit()
        operations, _ = load_openapi(OPENAPI_SNAPSHOT)
        self.assertEqual(findings, [])
        lifecycle_count = sum(
            value for key, value in counts.items() if key.startswith("lifecycle:")
        )
        self.assertEqual(lifecycle_count, len(operations))


if __name__ == "__main__":
    unittest.main()
