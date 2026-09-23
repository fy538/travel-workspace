"""Smoke inventory must admit the added contracts without relaxing failures."""

import json
from pathlib import Path
import subprocess
import sys

import pytest
import yaml


CHECKER = Path(__file__).resolve().parents[1] / "validate-maestro-flows.py"


def make_app(root: Path, count: int = 15) -> Path:
    maestro = root / ".maestro"
    maestro.mkdir()
    for index in range(count):
        header = {
            "appId": "com.fyan.vesper",
            "name": f"contract-{index}",
            "tags": ["stability", "pr-smoke"]
            + (["android-smoke"] if index < 5 else []),
            "properties": {
                "owner": "mobile-platform",
                "lane": "stability",
                "isolation": "mock-reset",
                "fixture": "mock",
            },
        }
        (maestro / f"{index}.yaml").write_text(
            yaml.safe_dump_all([header, [{"assertVisible": "Ready"}]])
        )
    (maestro / "config.pr.yaml").write_text(
        "flows: ['*.yaml']\nincludeTags: [pr-smoke]\n"
    )
    (root / "package.json").write_text(
        json.dumps(
            {"scripts": {"visual-qa:pr": "maestro test .maestro/config.pr.yaml"}}
        )
    )
    return root


def run_check(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(CHECKER), "--app-dir", str(root)],
        capture_output=True,
        text=True,
        check=False,
    )


def test_fifteen_isolated_smoke_contracts_pass(tmp_path: Path) -> None:
    result = run_check(make_app(tmp_path))
    assert result.returncode == 0, result.stderr


def test_missing_smoke_contract_still_fails(tmp_path: Path) -> None:
    result = run_check(make_app(tmp_path, 14))
    assert result.returncode == 1
    assert "expected 15 pr-smoke flows, found 14" in result.stderr


@pytest.mark.parametrize("broken", ["name", "lane", "yaml"])
def test_invalid_metadata_still_fails(tmp_path: Path, broken: str) -> None:
    app = make_app(tmp_path)
    flow = app / ".maestro/0.yaml"
    docs = list(yaml.safe_load_all(flow.read_text()))
    if broken == "name":
        del docs[0]["name"]
    elif broken == "lane":
        docs[0]["properties"]["lane"] = "functional-implementation"
    flow.write_text("[invalid" if broken == "yaml" else yaml.safe_dump_all(docs))
    assert run_check(app).returncode == 1


def test_missing_app_input_is_not_a_pass(tmp_path: Path) -> None:
    result = run_check(tmp_path)
    assert result.returncode == 1
    assert "No .maestro directory" in result.stderr
